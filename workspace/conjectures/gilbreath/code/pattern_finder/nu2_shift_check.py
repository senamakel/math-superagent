#!/usr/bin/env python3
"""Verify the claimed n-vs-n+1 shift between the two nu2 conventions.

Reference (nu2_vs_gap_parity.py) reports nu2 ~ {26,42,98,203,389,785,1604,2048}
at n in {50,100,200,400,800,1600,3200,3999}.
Incremental (nu2_incremental_to_1e5.py) reports nu2 at the same n labels as
{20,46,106,216,...}.  The run's docstring claims they are the same 0-2-cycle
notion off-by-one in the n label (gap_parity(n) = incremental(n+1)).

Check that claim exactly.
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2

P = primes_up_to(500_000)
D = [P[0]]
inc = {}
# incremental nu2(n) = nu2(delta(q_n)) where delta(q_n) has length n
for n in range(1, 5000):
    if n >= 2:
        newD = [0]*n; newD[0] = P[n-1]
        for k in range(1, n):
            newD[k] = abs(newD[k-1]-D[k-1])
        D = newD
    _, nu2 = cycle_and_nu2(D)
    inc[n] = nu2

gap_parity_vals = {50:26, 100:42, 200:98, 400:203, 800:389,
                   1600:785, 3200:1604, 3999:2048}
print("n    gap_parity  inc(n)  inc(n+1)   match shift?")
all_ok = True
for n, gp in gap_parity_vals.items():
    m_shift = (inc.get(n+1) == gp)
    m_flat = (inc.get(n) == gp)
    all_ok &= m_shift
    print("%-5d %-11d %-7d %-9d %-12s flat=%s" %
          (n, gp, inc.get(n), inc.get(n+1), m_shift, m_flat))
print("\nShift hypothesis gap_parity(n)==inc(n+1) holds for all samples:", all_ok)
