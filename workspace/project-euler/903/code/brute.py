#!/usr/bin/env python3
"""Brute-force oracle, method 1 -- literal double sum.

Q(n) = sum over all pi of [ sum_{i=1}^{n!} rank(pi^i) ].

Method:
  * enumerate all n! permutations in lexicographic order and build a dict
    permutation-tuple -> 1-based rank.  itertools.permutations(range(1, n+1))
    yields exactly the lexicographic order, so the enumerate index (1-based)
    is the rank;
  * for each permutation pi, walk the orbit pi^1, ..., pi^{n!} by repeated
    element-wise composition: (pi^{k+1})(j) = pi(pi^k(j)), i.e. in 0-based
    terms next[v] = pi[cur[v] - 1], and accumulate the ranks;
  * keep the total as an exact Python int; reduce mod 10^9+7 at the end.

Time  O((n!)^2) tuple compositions + dict lookups.
Space O(n!)  for the rank dict.

Usage: python brute.py [n ...]     (default: 2 3 4 5 6 7 8)
Writes results.json next to this script.
n >= 8 is attempted only when the measured speed at n-1 predicts completion
within ~5 min, and even then has a hard wall-clock cap of 300 s.
"""

import itertools
import json
import sys
import time
from math import factorial
from pathlib import Path

MOD = 10**9 + 7
ORACLE = {2: 5, 3: 88, 6: 133103808}  # exact Q(n) values given in the statement
RANK_EXAMPLE = ((2, 1, 3), 3)
HARD_BUDGET_S = 300  # hard wall-clock cap for n >= 8


def lex_ranks(n):
    """Return {permutation tuple -> 1-based lexicographic rank} for {1..n}."""
    rank = {}
    for r, perm in enumerate(itertools.permutations(range(1, n + 1)), start=1):
        rank[perm] = r
    return rank


def q_method1(n, budget_s=None):
    """Literal Q(n); returns dict with exact Q and Q mod MOD.

    Raises TimeoutError if budget_s wall-clock seconds are exceeded (checked
    periodically, so it is a cap, not a precise stopwatch).
    """
    t0 = time.perf_counter()
    rank = lex_ranks(n)
    t_ranks = time.perf_counter() - t0

    nf = factorial(n)
    total = 0                                          # exact Python int
    deadline = time.perf_counter() + budget_s if budget_s is not None else None

    t0c = time.perf_counter()
    pi_count = 0
    for pi in itertools.permutations(range(1, n + 1)):
        s = 0
        cur = pi                                        # pi^1
        for _ in range(nf):
            s += rank[cur]
            cur = tuple(pi[v - 1] for v in cur)         # advance to next power
        total += s
        pi_count += 1
        if deadline is not None and pi_count % 250 == 0:
            if time.perf_counter() > deadline:
                raise TimeoutError(f"n={n}: method 1 exceeded {budget_s}s budget")
    t_comp = time.perf_counter() - t0c

    return {
        "n": n,
        "method": "literal",
        "Q": total,                      # exact integer
        "Qmod": total % MOD,
        "t_ranks_s": round(t_ranks, 3),
        "t_compute_s": round(t_comp, 3),
        "steps": nf * nf,
    }


def main(argv):
    ns = [int(a) for a in argv] if argv else [2, 3, 4, 5, 6, 7, 8]
    out = []

    # --- reproduce the worked rank example from the statement ---
    got = lex_ranks(3)[RANK_EXAMPLE[0]]
    assert got == RANK_EXAMPLE[1], f"rank example failed: got {got}"
    print(f"[check] rank{RANK_EXAMPLE[0]} = {got}  (expected {RANK_EXAMPLE[1]}) OK")

    for n in ns:
        # Gate for large n: predict from the previous n's measured speed.
        if n >= 8 and out and "t_ranks_s" in out[-1]:
            prev = out[-1]
            last_n = prev["n"]
            last_time = prev["t_ranks_s"] + prev["t_compute_s"]
            est = last_time * (factorial(n) / factorial(last_n)) ** 2 * (n / last_n)
            print(f"[gate] n={n}: estimated {est / 60:.1f} min from n={last_n} run")
            if est > HARD_BUDGET_S:
                print(f"[gate] n={n}: estimate too large -> method 1 skipped "
                      f"(budget {HARD_BUDGET_S}s)")
                out.append({"n": n, "method": "literal",
                            "skipped": "estimated time exceeds budget"})
                continue

        try:
            r = q_method1(n, budget_s=HARD_BUDGET_S if n >= 8 else None)
        except TimeoutError as e:
            print(f"[gate] n={n}: {e} -> method 1 skipped")
            out.append({"n": n, "method": "literal", "skipped": str(e)})
            continue

        print(f"n={n}: Q(n) = {r['Q']}   Q(n) mod p = {r['Qmod']}   "
              f"(rank build {r['t_ranks_s']}s, compute {r['t_compute_s']}s, "
              f"{r['steps']} power-steps)")
        if n in ORACLE:
            ok = r["Q"] == ORACLE[n] and r["Qmod"] == ORACLE[n] % MOD
            print(f"   [oracle {'OK' if ok else 'FAILED'}] "
                  f"expected Q({n}) = {ORACLE[n]}")
            if not ok:
                sys.exit(f"oracle check FAILED for n={n}")
        out.append(r)

    path = Path(__file__).resolve().parent / "results.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main(sys.argv[1:])