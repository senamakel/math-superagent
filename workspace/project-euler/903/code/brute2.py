#!/usr/bin/env python3
"""Independent brute-force oracle, method 2 -- orbit / period formula.

Every permutation pi has order d = ord(pi) = lcm of its cycle lengths.  The
power sequence pi^1, pi^2, ... is periodic with period d, and d | n! (each
cycle length divides n!, and the lcm of divisors of n! divides n!), so among
i = 1..n! each of the d *distinct* powers appears exactly n!/d times.  Hence

    sum_{i=1}^{n!} rank(pi^i) = (n! / ord(pi)) * sum_{tau in <pi>} rank(tau),

and  Q(n) = sum_pi (n!/ord(pi)) * sum_{tau in <pi>} rank(tau).

This is a structurally different route from brute.py (orbit structure /
periodicity instead of a literal power-by-power walk) -- the rank table is
rebuilt independently here -- so agreement on every n both reach
cross-validates both implementations.

Time  O((n!)^2) (orbit walk per permutation), space O(n!).
Usage: python brute2.py [n ...]     (default: 2 3 4 5 6 7 8)
"""

import itertools
import json
import sys
import time
from math import factorial, gcd
from pathlib import Path

MOD = 10**9 + 7
ORACLE = {2: 5, 3: 88, 6: 133103808}  # exact Q(n) values given in the statement
RANK_EXAMPLE = ((2, 1, 3), 3)


def lex_ranks(n):
    """Return {permutation tuple -> 1-based lexicographic rank} (independent copy)."""
    rank = {}
    for r, perm in enumerate(itertools.permutations(range(1, n + 1)), start=1):
        rank[perm] = r
    return rank


def order_of(pi):
    """Order of pi = lcm of its cycle lengths (pi given in one-line notation)."""
    n = len(pi)
    seen = [False] * n
    o = 1
    for start in range(n):
        if not seen[start]:
            length = 0
            cur = start
            while not seen[cur]:
                seen[cur] = True
                cur = pi[cur] - 1
                length += 1
            o = o * length // gcd(o, length)
    return o


def distinct_powers(pi):
    """All distinct powers pi^1, pi^2, ..., pi^d (visit order), d = ord(pi)."""
    out = []
    seen = set()
    cur = pi
    while cur not in seen:
        seen.add(cur)
        out.append(cur)
        cur = tuple(pi[v - 1] for v in cur)   # (pi^{k+1})(j) = pi(pi^k(j))
    return out


def q_method2(n):
    """Q(n) by the period formula; returns (exact Q, Q mod MOD)."""
    rank = lex_ranks(n)
    nf = factorial(n)
    total = 0
    for pi in itertools.permutations(range(1, n + 1)):
        d = order_of(pi)
        powers = distinct_powers(pi)
        assert len(powers) == d, "period of the power map != ord(pi)"
        assert nf % d == 0, "ord(pi) does not divide n!"
        total += (nf // d) * sum(rank[t] for t in powers)
    return total, total % MOD


def main(argv):
    ns = [int(a) for a in argv] if argv else [2, 3, 4, 5, 6, 7, 8]

    got = lex_ranks(3)[RANK_EXAMPLE[0]]
    assert got == RANK_EXAMPLE[1], f"rank example failed: got {got}"
    print(f"[check] rank{RANK_EXAMPLE[0]} = {got}  (expected {RANK_EXAMPLE[1]}) OK")

    # read brute.py's results (method 1) for the cross-check
    res_path = Path(__file__).resolve().parent / "results.json"
    if res_path.exists():
        m1 = {r["n"]: r for r in json.loads(res_path.read_text())
              if r.get("method") == "literal" and "Q" in r}
    else:
        m1 = {}
        print("[note] results.json not found; run brute.py first for cross-check")

    results2 = []
    for n in ns:
        t0 = time.perf_counter()
        q, qmod = q_method2(n)
        t = time.perf_counter() - t0
        results2.append({"n": n, "method": "period", "Q": q, "Qmod": qmod})
        print(f"n={n}: Q(n) = {q}   Q(n) mod p = {qmod}   ({t:.2f}s)")
        if n in ORACLE:
            ok = q == ORACLE[n] and qmod == ORACLE[n] % MOD
            print(f"   [oracle {'OK' if ok else 'FAILED'}] expected Q({n}) = {ORACLE[n]}")
            if not ok:
                sys.exit(f"oracle check FAILED for n={n}")
        if n in m1:
            same_q = m1[n]["Q"] == q
            same_mod = m1[n]["Qmod"] == qmod
            print(f"   [cross-check vs method 1] exact {same_q}, mod {same_mod}"
                  + ("" if same_q and same_mod else "  <-- MISMATCH"))
            if not (same_q and same_mod):
                sys.exit(f"methods disagree for n={n}")
        else:
            print(f"   [cross-check] method 1 did not reach n={n} (skipped)")

    # summary table
    print("\n=== agreement table (exact Q) ===")
    for r in results2:
        n = r["n"]
        if n in m1:
            print(f"n={n}: method1={m1[n]['Q']}  method2={r['Q']}  "
                  f"match={m1[n]['Q'] == r['Q']}")
        else:
            print(f"n={n}: method1=not reached  method2={r['Q']}")

    path = Path(__file__).resolve().parent / "results2.json"
    path.write_text(json.dumps(results2, indent=2))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main(sys.argv[1:])