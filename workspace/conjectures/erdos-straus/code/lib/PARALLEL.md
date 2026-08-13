# Running a search across every core

This container has **28 CPUs and no CPU quota**. Every program in `code/` so
far has used one of them. That is not a small inefficiency: `phi_padic_closure_exact.py`
burned eight minutes on a single core and was killed by the ten-minute tool
ceiling with nothing captured, and it is not the only one. The search that
cannot finish serially finishes comfortably in parallel.

Use `code/lib/parallel.py`. Standard library only — nothing to install, which
matters because the container root filesystem is read-only.

## The import

Programs run with `/workspace` as the working directory, exactly as
`check_near_misses.py` and `checker_selftest.py` already do it:

```python
import sys
sys.path.insert(0, "code")
from lib.parallel import parallel_union, parallel_any, stripes, workers
```

## The one rule that catches everybody

**The worker function must be defined at module top level.** A closure, a
lambda, or a nested `def` cannot be pickled into a child process and the pool
will fail. Pass what it needs as arguments, or read it from a module-level
constant.

## Worked example — searching the ansatz grid

The work here is symbolic: enumerate candidate shapes for `x(k), y(k), z(k)`
and test each as an identity. Ansaetze are independent, so this is the ideal
shape for a pool.

Before, single core:

```python
def search(grid):
    return [a for a in grid if is_identity(a)]
```

After, 26 cores, **same answer**:

```python
def _test_ansatz(chunk):            # top level, so it can be pickled
    return {a for a in chunk if is_identity(a)}

def search(grid):
    return parallel_union(
        _test_ansatz,
        stripes(list(grid), workers()),
        label="ansatz grid",
        space=f"{len(grid)} shapes",
    )
```

To stop at the first family that works, use `parallel_any` instead — it
terminates the pool on the first truthy return.

Symbolic simplification is the slow step and its cost varies wildly between
shapes, so `stripes` matters here: a contiguous split can hand one worker all
the expensive high-degree ansaetze.

## Which helper

| Shape of the search | Use |
| --- | --- |
| Build one set out of many partial sets — `phi_set`, residue sets, closure sets | `parallel_union` |
| Hunt a counterexample and stop at the first hit | `parallel_any` |
| One result per input, order preserved, to compare against the serial answer | `parallel_map` |

`parallel_any` calls `pool.terminate()` the moment a worker returns something
truthy, so a witness stops the rest immediately. It returns `None` when
nothing is found — for an impossibility search that is the interesting
outcome, and it must be reported **with the bound actually covered**, never as
"no counterexample exists".

## Check the parallel version against the serial one

Parallelising must not change the answer, and on this problem a silently
changed answer would be an impossibility result that is simply wrong. Verify
once at a small bound before trusting a large one:

```python
assert phi_set_serial(120) == phi_set(120)
```

The library ships its own check — run `python3 code/lib/parallel.py` and it
compares a pooled union against the serial answer and asserts they agree.

## Always launch under a timeout

The tool ceiling is ten minutes and a killed command captures nothing unless
it printed as it went. Launch every program the way the four phi programs that
*did* produce captures were launched:

```
timeout 540 python3 code/phi_padic_closure_all.py 2>&1 | tee code/out/phi_padic_closure_all.captured.txt; echo "EXIT_CODE=$?"
```

`tee` is the part that has been missing. Output that only reaches the model
dies when the attempt hits its thirty-minute cap.

## Say how wide the search was

Every entry point prints the worker count and the search space to stderr
before starting. Keep that line in the captured output — a result that does
not state the bound it covered is not reproducible, and on an impossibility
claim the bound *is* the result.
