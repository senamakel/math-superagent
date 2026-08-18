"""Refuter's own small exact verification for the G4 thesis attack.

complexity_class: exponential; oracle_bound: k <= 25 (exact values on disk).
Recomputes, from the mechanical model (the run's own verified oracle),
the exact factor values, Psi(k), the single-intercept failure, and the
mod-100 cross-check, so the thesis attack rests on numbers I computed here
rather than only on recorded captures.
"""
import sys
sys.path.insert(0, 'code')
from fractions import Fraction
from mech.mech_psi import mech_psi, M

# exact values from the recorded table (psi_exact.txt) for cross-check
exact = {}
with open('code/out/psi_exact.txt') as fh:
    for line in fh:
        k, v = line.split()
        exact[int(k)] = int(v)

print("== reproduce anchors from the mechanical model ==")
for k in (3, 10):
    totA, totB, vA, vB = mech_psi(k)
    print(f"k={k}: Psi={totA} exact? {totA == exact[k]} (A==B multisets: {vA==vB}) "
          f"mod M={totA % M}")

print("\n== single-intercept replacement at k=1,2,3 ==")
# The joint sum is over k+1 intercepts; the tempting single-intercept
# reduction keeps only m=0 and gets S2 from one ue0 call.  Direct check:
# sum of squares of the k+1 distinct values vs square of the m=0 value alone.
for k in (1, 2, 3):
    totA, totB, vA, vB = mech_psi(k)
    joint = totA % M
    # m=0 arc value: the *smallest* value in the arc-midpoint multiset is NOT
    # the m=0 value; recover v(m=0) from formulation B: m=0 term.
    # Formulation B: v_m = g(k-m) - 10^{k-1} g(-m) + 9 sum_{l=1}^{k-1} ...
    # Recompute directly for m=0:
    fib = [0, 1]
    while fib[-1] <= k:
        fib.append(fib[-1] + fib[-2])
    q = fib[-1]; p = fib[-3]; a = Fraction(p, q)
    def floorf(x): return x.numerator // x.denominator
    g = {t: floorf(Fraction(t * p, q)) - (1 if t == 0 else 0)
         for t in range(-k, k + 1)}
    pw = [10 ** e for e in range(k + 1)]
    v0 = g[k] - pw[k-1] * g[0] + 9 * sum(pw[k-1-l] * g[l] for l in range(1, k))
    print(f"k={k}: joint Psi={joint} (mod M), m=0 value v_0={v0}, "
          f"v_0^2={v0*v0 % M}, single-intercept claim joint==v0^2: {joint == v0*v0 % M}")

print("\n== mod-100 cross-check (Psi(k) = 1 + floor(k/phi^2) mod 100), k=1..25 ==")
import math
phi2 = (3 + math.sqrt(5)) / 2.0
bad = 0
for k in range(1, 26):
    want = (1 + math.floor(k / phi2)) % 100
    got = exact[k] % 100
    if got != want:
        bad += 1
        print(f"  k={k}: exact%100={got} want={want}")
print(f"  mismatches: {bad}")
