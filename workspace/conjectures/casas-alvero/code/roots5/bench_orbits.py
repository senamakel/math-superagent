#!/usr/bin/env python3
"""Benchmark the 52 S4-orbits of the n=6 coincidence+centroid system.

For each orbit representative of the 625 root-index choices under the S4
symmetry permuting {b,c,d,e}, solve the Rabinowitsch-distinct coincidence+
centroid system over QQ and record whether the reduced lex Groebner basis is
the unit ideal [1] (UNSAT on the distinct-root locus) and the wall clock.

Run with a per-case wall-clock cap so a single pathological choice cannot hang
the sweep; a choice that exceeds the cap is reported as UNKNOWN (not SAT).
"""

import sys
import time
import signal

from sympy import symbols, groebner, expand

from roots5.coincidence_n6 import build_distinct_product


class TimeoutError_(Exception):
    pass


def _handler(signum, frame):
    raise TimeoutError_("case timeout")


ROOTS = ["a", "b", "c", "d", "e"]


def solve_case(witness, cap):
    """Return (label, 'UNSAT'|'SAT'|'UNKNOWN', wall).  witness is a 4-tuple of
    root names: (root for i=2, root for i=3, root for i=4, centroid root)."""
    a, b, c, d, e, t = symbols("a b c d e t")
    x = symbols("x")
    rm = {"a": a, "b": b, "c": c, "d": d, "e": e}
    f = (x - a) ** 2 * (x - b) * (x - c) * (x - d) * (x - e)
    polys = []
    for i, wr in zip([2, 3, 4], witness[:-1]):
        di = expand(f.diff(x, i))
        polys.append(expand(di.subs(x, rm[wr])))
    polys.append(expand((2 * a + b + c + d + e) - 6 * rm[witness[-1]]))
    D = build_distinct_product(a, b, c, d, e)
    ideal = polys + [1 - t * D]

    old = signal.signal(signal.SIGALRM, _handler)
    signal.alarm(cap)
    t0 = time.time()
    try:
        G = groebner(ideal, a, b, c, d, e, t, order="lex")
        basis = list(G)
        trivial = (len(basis) == 1 and basis[0] == 1)
        verdict = "UNSAT" if trivial else "SAT"
    except TimeoutError_:
        verdict = "UNKNOWN"
    except Exception as ex:  # pragma: no cover
        verdict = "ERR:" + type(ex).__name__
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
    wall = time.time() - t0
    return ",".join(witness), verdict, wall


def canon(t):
    """Canonical form of a 4-tuple under S4 permuting b,c,d,e (labels in
    ROOTS).  a is distinguished.  Returns a representative with the same
    fixed-a positions and same equality pattern among the non-a entries."""
    apos = frozenset(i for i, v in enumerate(t) if v == "a")
    others = [v for v in t if v != "a"]
    mp = {}
    cls = []
    for v in others:
        if v not in mp:
            mp[v] = len(mp)
        cls.append(mp[v])
    return (apos, tuple(cls))


def main():
    from itertools import product
    choices = list(product(ROOTS, repeat=4))
    # canonical representatives: pick one tuple per (apos, cls-pattern)
    by = {}
    for t in choices:
        by.setdefault(canon(t), t)
    reps = sorted(by.values(), key=lambda t: (canon(t)))
    print(f"{len(choices)} choices -> {len(reps)} S4 orbit representatives",
          file=sys.stderr)

    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 45
    results = []
    for t in reps:
        label, v, wall = solve_case(t, cap)
        results.append((label, v, wall))
        print(f"  {label:<15} {v:<8} {wall:6.2f}s", flush=True)

    from collections import Counter
    c = Counter(v for _, v, _ in results)
    print("verdict counts:", dict(c))
    total_wall = sum(w for _, _, w in results)
    print(f"total serial wall (incl. UNKNOWN caps): {total_wall:.2f}s")
    n_nonunsat = sum(1 for _, v, _ in results if v != "UNSAT")
    print(f"non-UNSAT (SAT/UNKNOWN/ERR) representatives: {n_nonunsat}")
    good = n_nonunsat == 0
    print("ALL 52 ORBITS UNSAT" if good else "NOT all UNSAT")
    sys.exit(0 if good else 1)


if __name__ == "__main__":
    main()
