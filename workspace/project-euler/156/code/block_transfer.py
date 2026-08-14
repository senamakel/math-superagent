#!/usr/bin/env python3
"""Block-transfer classification of the PE156 solution sets.

Structural closed-form route (research/approaches/block-transfer-
classification.md), executed for the first time in this run.

Residue identity at the self-similarity scale: for 0 <= x < 10^10 and
1 <= k <= d-1,
        f_d(k*10^10 + x) - f_d(x) = k*10^10,
so x is a fixed point of f_d iff k*10^10 + x is.  With the
Khovanova-Marton bound n <= d*10^10 the full solution set is the disjoint
union of d translated copies of the seed block
        S0(d) = {x < 10^10 : f(x,d) = x},
and the per-digit sum has the closed form
        s(d) = d * sum(S0(d)) + (d(d-1)/2) * 10^10 * |S0(d)|.

Per digit d in 1..9 this program:
  (a) enumerates S0(d) with the jump iterator (reused from code/solution.py,
      whose f_place evaluator is the same place-value identity as
      lib.digits.f_place_value) restricted to [0, 10^10); every seed is then
      re-checked with lib.digits.f_place_value;
  (b) verifies the bijection term-by-term: the rebuilt set
      {k*10^10 + x : k=0..d-1, x in S0(d)} equals the on-disk solution
      files code/out/solutions-d*.txt; the residue identity itself is
      re-evaluated for every (d, k, seed) pair, and every one of the 661
      rebuilt solutions is re-checked with f_place_value;
  (c) computes s(d) by the closed form and compares with the file sums and
      the verified grand total 21295121502550.

Exact integer arithmetic throughout.  Time: O(#solutions * #digits)
f-evaluations (~10^4 total), independent of the 10^10 bound; space O(1)
beyond the stored solution lists.
"""
import os
import sys

OUT = "/workspace/code/out"

from lib.digits import f_place_value      # exact O(#digits) evaluator
from solution import solutions_by_jump    # jump iterator, reused not rewritten

GRAND = 21295121502550


def read_solutions(d):
    with open(os.path.join(OUT, f"solutions-d{d}.txt")) as fh:
        return [int(x) for x in fh.read().split()]


def main():
    grand_closed = 0
    grand_file = 0
    all_ok = True
    evals_total = 0
    for d in range(1, 10):
        # (a) seed block inside [0, 10^10)
        seeds, evals = solutions_by_jump(d, bound=10**10 - 1)
        evals_total += evals
        seeds_ok = all(f_place_value(x, d) == x for x in seeds)

        # (b) bijection + identity + re-check of every rebuilt solution
        rebuilt = sorted(k * 10**10 + x for k in range(d) for x in seeds)
        file_sols = read_solutions(d)
        bijection_ok = (rebuilt == file_sols)
        identity_ok = all(
            f_place_value(k * 10**10 + x, d) - f_place_value(x, d) == k * 10**10
            for k in range(1, d) for x in seeds)
        sols_ok = all(f_place_value(n, d) == n for n in rebuilt)

        # (c) closed form vs file sum
        s_closed = d * sum(seeds) + (d * (d - 1) // 2) * 10**10 * len(seeds)
        s_file = sum(file_sols)
        sum_ok = (s_closed == s_file)

        ok = seeds_ok and bijection_ok and identity_ok and sols_ok and sum_ok
        all_ok = all_ok and ok
        grand_closed += s_closed
        grand_file += s_file
        print(f"d={d}: |S0|={len(seeds):>2} (evals {evals:>5}) "
              f"seeds={seeds_ok} identity={identity_ok} bijection={bijection_ok} "
              f"sols={sols_ok} s(d) closed={s_closed} file={s_file} "
              f"match={sum_ok} {'OK' if ok else 'FAIL'}")

    print()
    print("total f-evaluations for all nine seed enumerations:", evals_total)
    print("s(d) closed-form total =", grand_closed)
    print("s(d) file-sum total    =", grand_file)
    print("grand total == 21295121502550:",
          "OK" if grand_closed == grand_file == GRAND else "FAIL")
    print("ALL BLOCK-TRANSFER CHECKS:",
          "OK" if all_ok and grand_closed == GRAND else "FAIL")
    if not (all_ok and grand_closed == GRAND):
        sys.exit(1)


if __name__ == "__main__":
    main()
