#!/usr/bin/env python3
"""
Directive 60 / item 1b — the single most important number.

For each odd-factor period P in {3,5,7,9} (plus power-of-2 P in {1,2,4} as
the degenerate contrast, and P=15 as the recorded plateau case), build the
2-then-odds sequence with the periodic halved-gap bit string h (period P,
word h = [0,...,0,1], the tail-1 word used through the dyadic corpus), walk
the right diagonals incrementally, and report the INFIMUM of nu2(n)/n over
all n in [n_first, n_max], NOT the trend.

Why the infimum: the supply line needs nu2(n) >= c*n uniformly.  A dichotomy
that grows "in the mean" but has an inf decaying toward 0 means nu2 >= c*n
fails at the plateau points (P=15 recorded at 1064,1064; P=7 at 284,284).
If inf_n nu2(n)/n is bounded below by a positive c for a period P, the
dichotomy is USEFUL for supply on that period; if the inf decays with n, the
dichotomy is true but DEAD for supply.

Exact integers.  O(N^2) diffs per period, O(N) memory (one diagonal live).
"""
import sys, time
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(h_pattern, n_terms):
    q = [2, 3]
    per = len(h_pattern)
    while len(q) < n_terms:
        m = len(q)
        j = m - 2
        bit = h_pattern[j % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def inf_measure(word, n_max, n_first=100):
    """Walk diagonals incrementally; for each n in [n_first, n_max] read
    nu2(n) from the live diagonal; track inf of nu2/n and argmin. Return dict."""
    q = build_seq(word, n_max + 1)
    best_ratio = float('inf')
    best_n = None
    best_nu2 = None
    last_nu2 = None
    n = 0
    for diag in incremental_diagonals(q):
        # diag is delta(q_n): length n+1
        tau, nu2 = cycle_and_nu2(diag)
        last_nu2 = nu2
        if n >= n_first:
            r = nu2 / n
            if r < best_ratio:
                best_ratio, best_n, best_nu2 = r, n, nu2
        n += 1
    return {'best_ratio': best_ratio, 'best_n': best_n,
            'best_nu2': best_nu2, 'last_nu2': last_nu2,
            'n_max_used': n - 1}


def main():
    n_max = 20000
    n_first = 100
    print(f"dyadic periodic halved-gap bit string — inf nu2(n)/n over "
          f"n in [{n_first},{n_max}]")
    print("word: h=[0,...,0,1] (tail-1), period P.  q_1=2,q_2=3, gap=2 if "
          "h=1 else 4.")
    print("=" * 78)
    # Contrast: power-of-2 degenerate periods first.
    for P in (1, 2, 4):
        t = time.time()
        word = [0] * (P - 1) + [1]
        m = inf_measure(word, n_max, n_first)
        print(f"P={P:>3} (power of 2)  inf nu2/n = {m['best_ratio']:.6f}  "
              f"at n={m['best_n']} (nu2={m['best_nu2']})  "
              f"last nu2={m['last_nu2']}  [{time.time()-t:.0f}s]")
    print("-" * 78)
    for P in (3, 5, 7, 9, 15):
        t = time.time()
        word = [0] * (P - 1) + [1]
        m = inf_measure(word, n_max, n_first)
        print(f"P={P:>3} (odd factor)  inf nu2/n = {m['best_ratio']:.6f}  "
              f"at n={m['best_n']} (nu2={m['best_nu2']})  "
              f"last nu2={m['last_nu2']}  [{time.time()-t:.0f}s]")
    print("=" * 78)
    print("Reading: inf_n nu2(n)/n bounded below by positive c => nu2 >= c*n "
          "would hold uniformly on THAT period bit string (non-primal). "
          "If inf ~ 1/n -> 0, the odd-factor dichotomy is real but DEAD for "
          "a uniform supply bound on that word.")
    print("NOTE: these are PERIODIC words, explicitly NOT the primes; the "
          "prime bit string is aperiodic. This measures only whether the "
          "dyadic dichotomy is supply-useful on the periodic families, per "
          "Directive 60 item 1b.")


if __name__ == "__main__":
    main()
