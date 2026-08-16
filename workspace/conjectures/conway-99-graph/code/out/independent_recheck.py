#!/usr/bin/env python3
"""
Independent re-derivation, from scratch, of two core claims of the Conway
99-graph solution report. Exact integer / Fraction arithmetic only.

What it ran:
  - Claim A: five-member integrality of the srg(v,k,1,2) family
        k = u^2+u+2,  v = 1 + k^2/2,  a = sqrt(4k-7) = 2u+1 (odd integer)
        negative-eigenvalue multiplicity
            f = (1/2) * ( (v-1) - (2k-(v-1))/a )
        Scan u = 1..200000; integral members should be exactly
        u in {1,3,4,10,31}; integrality holds iff a | 63.
  - Claim B: multiplicity integrality of srg(33,12,1,6)
        characteristic x^2 - (lam-mu)x - (k-mu) = 0, roots r,s, and the two
        nontrivial multiplicities; show they are not integers, hence the
        parameter set is infeasible.

No existing capture is reused; every number is recomputed here.

Oracle function used: none — this is pure parameter-level integrality with
exact integer/Fraction arithmetic. The canonical oracle (code/lib/srg.py) is a
graph matcher and is not needed for the parameter feasibility check.

Search space: a scan over the DESCRIPTION index u of a closed-form family,
verifying a claimed classification, O(N) with O(1) work per u. The range
[1,200000] is the bound in the statement; this is verification, not a search
of the answer space.
"""

from fractions import Fraction

print("=== CLAIM A: five-member integrality of srg(v,k,1,2) ===\n")

def family(u):
    """Return (k, v, a) for the srg(v,k,1,2) member at parameter u.
    k = u^2+u+2, v = 1+k^2/2, a = sqrt(4k-7) = 2u+1."""
    k = u*u + u + 2
    v = 1 + (k*k)//2          # exact since k even => k^2 even
    a = 2*u + 1
    assert a*a == 4*k - 7, "a must be sqrt(4k-7)"
    return k, v, a

def f_neg(u):
    """Negative-eigenvalue multiplicity f of the (1,2) member at u, exact.
    f = (1/2)*((v-1) - (2k-(v-1))/a)."""
    k, v, a = family(u)
    return Fraction(1,2) * ( Fraction(v-1) - Fraction(2*k - (v-1), a) )

N = 200000
integral_u = [u for u in range(1, N+1)
              if (lambda f: f.denominator == 1 and f >= 0)(f_neg(u))]

print(f"Scan u in [1,{N}]")
print("  Integral members found: ", integral_u)
print("  Expected integral members:", [1,3,4,10,31])
print("  Match:", integral_u == [1,3,4,10,31])

# integrality iff a | 63
mismatch = 0
for u in range(1, N+1):
    _, _, a = family(u)
    f = f_neg(u)
    is_int = (f.denominator == 1 and f >= 0)
    a63 = (63 % a == 0)
    if is_int != a63:
        mismatch += 1
        if mismatch <= 5:
            print(f"  MISMATCH u={u} a={a} f={f} is_int={is_int} a|63={a63}")
print(f"  Integrality-iff-(a|63) mismatches over [1,{N}]: {mismatch}\n")

print("  f (negative-eigenvalue multiplicity) values for the five members:")
print(f"  {'u':>3} {'a':>3} {'k':>5} {'v':>8} {'f':>8}  integral?")
for u in integral_u:
    k, v, a = family(u)
    f = f_neg(u)
    print(f"  {u:>3} {a:>3} {k:>5} {v:>8} {str(f):>8}  {f.denominator==1}")

# both nontrivial multiplicities for completeness (sum must be v-1)
print("\n  Both nontrivial multiplicities (m_r for r>0, m_s for s<0); "
      "1+m_r+m_s must equal v:")
for u in integral_u:
    k, v, a = family(u)
    T = 2*k - (v-1)                # = 2k + (v-1)(lam-mu), lam-mu=-1 here
    mr = Fraction(1,2)*( Fraction(v-1) - Fraction(T, a) )
    ms = Fraction(1,2)*( Fraction(v-1) + Fraction(T, a) )
    print(f"   u={u:>2}: m_r={str(mr):>8} m_s={str(ms):>8} "
          f"sum+1={int(1+mr+ms)} (v={v}) integral={mr.denominator==1 and ms.denominator==1}")

print("\n=== CLAIM B: multiplicity integrality of srg(33,12,1,6) ===\n")

v, k, lam, mu = 33, 12, 1, 6
print(f"  params: v={v}, k={k}, lam={lam}, mu={mu}")

dl = lam - mu                    # lambda - mu
D  = dl*dl + 4*(k - mu)          # discriminant of characteristic equation
print(f"  lam-mu = {dl}")
print(f"  characteristic: x^2 - (lam-mu)x - (k-mu) = 0")
print(f"      x^2 {-(dl):+d}x {-(k-mu):+d} = 0")
print(f"  D = (lam-mu)^2 + 4(k-mu) = {dl}^2 + 4({k-mu}) = {D}")

import math
sq = math.isqrt(D)
assert sq*sq == D, "D should be a perfect square here"
print(f"  sqrt(D) = {sq}  (exact integer)")

r = Fraction(dl + sq, 2)
s = Fraction(dl - sq, 2)
print(f"  r = (lam-mu + sqrtD)/2 = ({dl}+{sq})/2 = {r}")
print(f"  s = (lam-mu - sqrtD)/2 = ({dl}-{sq})/2 = {s}")
print(f"  check: r and s are roots of x^2 {-(dl):+d}x {-(k-mu):+d} = 0: "
      f"r^2-({dl})r-{k-mu}={r*r-dl*r-(k-mu)}, s^2-({dl})s-{k-mu}={s*s-dl*s-(k-mu)}")

# multiplicities  m_r,m_s = (1/2)[ (v-1) +/- (2k+(v-1)(lam-mu))/(r-s) ]
T = 2*k + (v-1)*dl
print(f"  2k + (v-1)(lam-mu) = {2*k} + {v-1}*({dl}) = {T}")
mr = Fraction(1,2) * ( Fraction(v-1) - Fraction(T, sq) )
ms = Fraction(1,2) * ( Fraction(v-1) + Fraction(T, sq) )
print(f"  m_r = (1/2)[(v-1) - T/(r-s)] = (1/2)[{v-1} - ({T})/{sq}] = {mr}")
print(f"  m_s = (1/2)[(v-1) + T/(r-s)] = (1/2)[{v-1} + ({T})/{sq}] = {ms}")
print(f"  m_r integral? {mr.denominator==1}   m_s integral? {ms.denominator==1}")
print(f"  check m_r+m_s+1 == v: {1+mr+ms} == {v} ? {1+mr+ms==v}")
print(f"  CONCLUSION: the nontrivial multiplicities are non-integral "
      f"({mr}, {ms}), so srg(33,12,1,6) is parameter-infeasible by "
      f"eigenvalue-multiplicity integrality.")

print("\n  --- note on the task's 'sqrt(4k-7)=sqrt(41)' phrasing ---")
print(f"  4k-7 = {4*k-7}, sqrt = sqrt({4*k-7}) which is NOT an integer.")
print("  sqrt(4k-7) is the discriminant expression for the srg(v,k,1,2) family")
print("  ONLY (where lam-mu=1, mu=2 gives D=1+4(k-2)=4k-7). It does NOT apply")
print("  to srg(33,12,1,6). The correct discriminant here is D=49 -> sqrt=7.")
print("  Either route yields non-integrality, but the correct/cleaner one is D=49.")
print("\nDONE")
