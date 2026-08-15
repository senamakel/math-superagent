"""Verify the conservation identity N_switch(x) = pi(x) - 1 - N_nonswitch(x).

N_switch(x) = #{consecutive prime pairs p<q<=x with q != p mod 4}   (switch)
N_nonswitch(x) = #{pairs with q == p mod 4}                        (non-switch)

For ANY binary labeling of the primes (residue 1 or 3 mod 4), the switch count
feeding Granville's nu2 equals the total number of consecutive pairs minus the
non-switch count.  This is exact (not heuristic): every prime except the last
is the first element of exactly one consecutive pair, so grouping by the first
prime's residue gives  N(1,3)+N(1,1) = #{p=1 mod 4 first of a pair}  and
N(3,1)+N(3,3) = #{p=3 mod 4 first of a pair}.  Adding:
   N_switch + N_nonswitch = #{primes <= x excluding the last} = pi(x) - 1.

Consequence:  N_switch >= c*pi(x)  (positive density, the G-supply demand)
              <=>  N_nonswitch <= (1-c)*pi(x).
So a lower bound on the switch count is EXACTLY an upper bound strictly below
density 1 on the non-switch count.  Ruzsa/Shiu give non-switch >= x loglog/log^2
(the WRONG direction, a lower bound on non-switch); they provide no upper bound,
so they give nothing to the switch side.  Checked here on the real primes.
"""
from sympy import primerange

def counts(x):
    ps = list(primerange(2, x+1))
    nsw = sw = 0
    for i in range(len(ps)-1):
        if ps[i] % 4 == ps[i+1] % 4:
            nsw += 1
        else:
            sw += 1
    return sw, nsw, len(ps)

for x in [100, 1000, 10_000, 100_000, 1_000_000]:
    sw, nsw, n = counts(x)
    lhs = sw + nsw          # actual total pairs
    rhs = n - 1             # pi(x) - 1
    assert lhs == rhs, (x, lhs, rhs)
    print(f"x={x:>9}: switch={sw:>7} non_switch={nsw:>7}  pairs={lhs}  pi(x)-1={rhs}  "
          f"switch/pi={sw/n:.4f}  match={lhs==rhs}")

print("CONSERVATION IDENTITY N_switch + N_nonswitch = pi(x) - 1: CONFIRMED on all x")
print("switch density ~ 0.5 at these scales (consistent with nu2/n ~ 0.5 and ABGS m=4 data)")
