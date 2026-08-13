#!/usr/bin/env python3
"""code/lib/parallel.py — spread a search over every core in the container.

The box has 28 CPUs and the container has no CPU quota (`cpu.max` is `max`),
so a single-threaded search is using about 3.5% of what is available.  A
`phi_padic_closure_exact.py` that needed eight minutes on one core needs
roughly twenty seconds across the pool.  That is the difference between
finishing inside the ten-minute tool ceiling and being killed with nothing to
show, which is what has happened repeatedly here.

Standard library only — `multiprocessing` ships with Python.  Nothing to
install, which matters because the container root filesystem is read-only.

Three rules that cover every mistake available in this module:

1. **The worker function must be defined at module top level.**  A closure or
   a lambda cannot be pickled to a child.  Take the parameters it needs as
   arguments, or read them from module-level constants.

2. **Return data, not objects.**  `Fraction`, `int`, `tuple`, `set`, `dict`,
   `list` all cross the process boundary fine.  Anything holding a file handle
   or a lock does not.

3. **Chunk by stripe, not by block.**  The loops here are triangular —
   `for m in 2..M for n in 1..m` — so the work in `m` grows linearly and a
   block split leaves one worker with the whole heavy end.  `stripes()` deals
   the values out round-robin instead, which balances a triangular loop to
   within one row.

Every entry point prints the worker count and the search space to stderr
before it starts, because a captured output that does not say how wide the
search was is not reproducible.
"""

from __future__ import annotations

import multiprocessing as mp
import os
import sys
from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")

__all__ = [
    "workers",
    "stripes",
    "parallel_map",
    "parallel_union",
    "parallel_any",
    "announce",
]


def workers(reserve: int = 2) -> int:
    """How many processes to run, leaving `reserve` cores for the runtime.

    The Rust runtime, its child agent runs and Qdrant share this container, so
    taking every core makes the whole run stutter without making the search
    finish sooner.
    """
    available = os.cpu_count() or 1
    return max(1, available - reserve)


def stripes(values: Sequence[T], count: int) -> list[list[T]]:
    """Deals `values` round-robin into `count` lists.

    For a triangular loop this is what keeps the workers even: striping `m` in
    `2..M` gives every worker a mix of cheap small rows and expensive large
    ones, where a contiguous split would give the last worker the tail that
    dominates the runtime.
    """
    if count < 1:
        count = 1
    out: list[list[T]] = [[] for _ in range(count)]
    for index, value in enumerate(values):
        out[index % count].append(value)
    return [stripe for stripe in out if stripe]


def announce(label: str, space: str, count: int) -> None:
    """States the search width on stderr, so the capture is reproducible."""
    print(
        f"[parallel] {label}: {space} across {count} worker(s) "
        f"of {os.cpu_count()} CPUs",
        file=sys.stderr,
        flush=True,
    )


def parallel_map(
    function: Callable[[T], R],
    items: Iterable[T],
    *,
    label: str = "map",
    space: str = "",
    count: int | None = None,
) -> list[R]:
    """Applies `function` to every item, in order, across the pool.

    Order is preserved, so a result list can be compared against the serial
    version element by element — which is how you check that parallelising did
    not change the answer.
    """
    items = list(items)
    count = count or workers()
    announce(label, space or f"{len(items)} item(s)", count)
    if count == 1 or len(items) <= 1:
        return [function(item) for item in items]
    with mp.Pool(processes=count) as pool:
        return list(pool.imap(function, items, chunksize=1))


def parallel_union(
    function: Callable[[T], set],
    items: Iterable[T],
    *,
    label: str = "union",
    space: str = "",
    count: int | None = None,
) -> set:
    """Unions the sets each worker returns.

    This is the shape `phi_set(M)` wants: hand each worker a stripe of `m`
    values, have it return the set of `f(m, n)` it found, and union what comes
    back.  The union is exact and order-independent, so the result is
    identical to the serial one.
    """
    parts = parallel_map(function, items, label=label, space=space, count=count)
    found: set = set()
    for part in parts:
        found |= part
    return found


def parallel_any(
    function: Callable[[T], object],
    items: Iterable[T],
    *,
    label: str = "search",
    space: str = "",
    count: int | None = None,
):
    """Returns the first truthy result and stops the remaining workers.

    For a counterexample hunt: the moment one worker finds a witness there is
    no reason to keep the others running.  Returns `None` when nothing is
    found, which for an impossibility search is the interesting outcome and
    must be reported with the bound that was actually covered.
    """
    items = list(items)
    count = count or workers()
    announce(label, space or f"{len(items)} item(s)", count)
    if count == 1 or len(items) <= 1:
        for item in items:
            got = function(item)
            if got:
                return got
        return None
    with mp.Pool(processes=count) as pool:
        for got in pool.imap_unordered(function, items, chunksize=1):
            if got:
                pool.terminate()
                return got
    return None


# --- self-check -------------------------------------------------------------
#
# Run this file directly to confirm the pool agrees with the serial answer
# before trusting it for anything:  python3 code/lib/parallel.py

def _squares_in(stripe: list[int]) -> set:
    return {value * value for value in stripe}


if __name__ == "__main__":
    values = list(range(1, 2001))
    serial = {value * value for value in values}
    pooled = parallel_union(
        _squares_in,
        stripes(values, workers()),
        label="self-check",
        space="n = 1..2000",
    )
    assert serial == pooled, "the pool disagreed with the serial answer"
    print(f"self-check PASS: {len(pooled)} values, {workers()} workers")
