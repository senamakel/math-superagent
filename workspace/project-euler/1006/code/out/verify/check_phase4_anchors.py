"""Verify the directive-6 acceptance anchors independently (k=10^4 case).

Directive 6 (steer) discards the old Phase-4 anchors 16242174 / 77578256:
both came from Psi_collapse, the Toeplitz A(d) collapse that solution.py
Phase 3 proves holds only at k = F_n - 1 — invalid at k=10^4 and k=10^6
(claim phase4-anchors-invalid). The replacement anchors, asserted from
outside the container:
  Psi(10^4) = 34432237 mod M, distinct count 10001
  Psi(10^6) = 20938836 mod M, distinct count 1000001
computed by the independent window/residue route: every distinct length-k
window of the Fibonacci word read as a decimal, squares summed mod M, on a
prefix of length k + NextFib(k) - 1 with NextFib the least Fibonacci
STRICTLY greater than k, de-duplicated by residues under two moduli with the
distinct count asserted to equal k+1.

This file checks the k=10^4 anchor by the VALID direct method already
verified in-container (psi_direct / mech_psi, == brute for k<=400). The
k=10^6 anchor needs the window/residue route itself (an O(k * prefix_len)
scan, ~1e13 digit-ops in Python — out of reach here; run it at the largest
feasible k and rely on k=10^4 + k=1..150 + Psi(3), Psi(10) agreement).
"""
import sys, time
sys.path.insert(0, "/workspace/code")
from solution import slope_for, arc_midpoints, v_telescoped, fib_list

M = 101001001
fibs = fib_list(2000)

# (1) is k of the form F_n - 1? (confirms the old anchors' method invalid here)
def is_Fminus1(k):
    a, b = 0, 1
    while b - 1 < k:
        a, b = b, a + b
    return (b - 1) == k

for k in (3, 4, 7, 12, 10000, 10 ** 6):
    print(f"k={k}: of form F_n-1? {is_Fminus1(k)}")

# (2) valid direct computation. psi_direct sums over k+1 arc midpoints each
# O(k) -> O(k^2).  For k=10^4 that is 10^8 big-int ops (slow but bounded).
# We only do k=10^4 here; 10^6 via O(k^2) is ~10^12, not feasible by this route.
def psi_direct_mod(k, a):
    xs = arc_midpoints(k, a)
    return sum(v_telescoped(x, k, a) ** 2 for x in xs) % M

k = 10000
a, n, m, N = slope_for(k, fibs)
t0 = time.time()
v = psi_direct_mod(k, a)
print(f"Psi({k}) mod M by VALID direct method = {v}  (took {time.time()-t0:.1f}s)")
print(f"directive-6 anchor                    = 34432237")
print(f"MATCH?  {v == 34432237}")
print(f"NOTE: 16242174 (old Phase-4 anchor) is NOT an acceptance target — refuted.")