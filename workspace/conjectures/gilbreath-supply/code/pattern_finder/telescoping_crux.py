#!/usr/bin/env python3
"""Verify the telescoping identity exactly:
    mean of D(n)=S(n+1)-S(n) over n=2..N-1  =  (S(N)-S(2))/(N-2)  =  S(N)/(N-2)
since S(2)=0.  This is EXACT (telescoping), so 'increment mean -> 0'
is IDENTICALLY equivalent to S(N)=o(N), i.e. POINTWISE SUPPLY.

If true, the fold's -1/2 ACF is real structure but it cannot be the lever:
the balancing it provides reduces to the very conjecture it would prove.
This is the honest structural negative (goal candidate 5's spirit).
"""
import sys, math, random
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    assert_supply_guard(4000)
    for label, h in [
            ("PRIMES", prime_h(N + 1)),
            ("iid p=0.5", ([1 if random.random() < 0.5 else 0
                            for _ in range(N + 1)]) )]:
        random.seed(1)
        S = {n: s_sos(n, h)[0] for n in range(2, N + 1)}
        D = [S[n + 1] - S[n] for n in range(2, N)]
        meanD = sum(D) / len(D)
        tel = (S[N] - S[2]) / (N - 2)
        print(f"{label}: mean(D)={meanD:+.6f}   (S(N)-S(2))/(N-2)={tel:+.6f}  "
              f"exact-match={abs(meanD-tel)<1e-12}   S(N)={S[N]}")


if __name__ == "__main__":
    main()
