#!/usr/bin/env python3
"""
Settle the ideal memberships of the Bautin focal-value obstructions
L4, L6, L8, L10, L12 for the blow-up chart family

    Q1 = A u^2 + C u v + D v^2 ,   Q2 = E u v + F v^2 ,
    linear part = rotation  R(p) = -v dp/du + u dp/dv ,
    V2 = (u^2 + v^2)/2 ,
    homological (Lyapunov) recurrence at degree k:
        R(c_k) + Q1*(V_{k-1})_u + Q2*(V_{k-1})_v
            - L_k*(u^2+v^2)^{k/2}  ==  0   (even k: radial obstruction L_k),
    gauge c_{k,0} = 0.

WHAT IT COMPUTES (all exact, sympy over QQ, no floats):
  (1) L4, L6, L8, L10, L12 from the recurrence above.
  (2) sanity guards reproducing the held audit:
       8*L4 == AC+CD+2DF-EF
       192*L6 + P30 == 0   (P30 the 30-monomial degree-6 obstruction)
  (3) exact ideal memberships over Q, lex order, decided by Groebner
      reduction remainder == 0 AND cross-checked by G.contains():
       L8  in <L4,L6>?      (False => third generator genuinely needed)
       L6  in <L4>?         (independence of first two)
       L10 in <L4,L6,L8>?   (Bautin-trick step: next focal value in ideal)
       L12 in <L4,L6,L8>?   (ditto, degree 12)
  (4) positive controls: a generator is always in its own ideal and an
      explicit combination is in the ideal -- these must be True, or the
      reduction machinery is broken and every result is void.

NOTES ON SYMPY API: in sympy 1.11, GroebnerBasis.reduce(poly) returns
(quotients_list, remainder); the remainder is the LAST element. Earlier
versions of this script read red[0] (the quotients), which made generators
reduce to nonzero "remainders" -- every later run used the corrected
extraction and the positive controls passed before the memberships were
read.

WHICH LEAN / CLAIM THIS BEARS ON: CONTEXT gap 3 -- the "Bautin trick"
ideal-membership statement L_d in <L4,L6,L8> that lyap_extend.py was going
to establish but crashed before printing. Decides whether Lu's route
(higher focal values lie in the ideal of the first three) survives.
"""
import sympy as sp
import time

u, v = sp.symbols("u v")
A, C, D, E, F = sp.symbols("A C D E F")
params = [A, C, D, E, F]
Q1 = A * u**2 + C * u * v + D * v**2
Q2 = E * u * v + F * v**2

# ---- capture header (first three lines: what ran, which defs, the range) ----
print("ran: python code/bautin/verify_membership.py")
print("definitions: chart family Q1=A u^2+C u v+D v^2, Q2=E u v+F v^2; rotation R(p)=-v dp/du+u dp/dv; V2=(u^2+v^2)/2; recurrence R(c_k)+Q1 V_{k-1,u}+Q2 V_{k-1,v}=L_k (u^2+v^2)^{k/2}, gauge c_{k,0}=0; L_d = d-th focal-value obstruction")
print("range: even degrees 4..12; exact sympy over QQ, lex Groebner; checks L8 in <L4,L6>, L6 in <L4>, L10 & L12 in <L4,L6,L8>")

t_start = time.time()


def rotation(poly):
    return sp.expand(-v * sp.diff(poly, u) + u * sp.diff(poly, v))


# ---------------- (1) recurrence -> L_d, degrees 3..12 ----------------
V = {2: (u**2 + v**2) / 2}
obstruction = {}
t_recur = time.time()
for degree in range(3, 13):
    coeffs = sp.symbols(f"c{degree}_0:{degree + 1}")
    correction = sum(coeffs[j] * u ** (degree - j) * v**j
                     for j in range(degree + 1))
    unknowns = list(coeffs)
    equation = sp.expand(
        rotation(correction)
        + Q1 * sp.diff(V[degree - 1], u)
        + Q2 * sp.diff(V[degree - 1], v)
    )
    radial = None
    if degree % 2 == 0:
        radial = sp.symbols(f"L{degree}")
        unknowns.append(radial)
        equation -= radial * (u**2 + v**2) ** (degree // 2)
    polynomial = sp.Poly(equation, u, v)
    equations = [polynomial.coeff_monomial(u ** (degree - j) * v**j)
                 for j in range(degree + 1)]
    if degree % 2 == 0:
        equations.append(coeffs[0])          # gauge c_{k,0}=0
    sol = sp.solve(equations, unknowns, dict=True, simplify=False)[0]
    V[degree] = sp.expand(correction.subs(sol))
    if radial is not None:
        obstruction[degree] = sp.factor(sol[radial])
    print(f"degree {degree}: done ({time.time() - t_recur:.0f}s cumulative)",
          flush=True)

L4, L6, L8, L10, L12 = (obstruction[d] for d in (4, 6, 8, 10, 12))
print(f"recurrence through degree 12: {time.time() - t_recur:.1f}s", flush=True)

# ---------------- (2) sanity guards reproducing the held audit ----------------
P30 = (
    76 * A**3 * C + 24 * A**3 * F + 142 * A**2 * C * D
    + 29 * A**2 * C * E + 192 * A**2 * D * F - 96 * A**2 * E * F
    + 23 * A * C**3 + 109 * A * C**2 * F + 76 * A * C * D**2
    + 42 * A * C * D * E + 3 * A * C * E**2 + 144 * A * C * F**2
    + 132 * A * D**2 * F - 28 * A * D * E * F - 37 * A * E**2 * F
    - 24 * A * F**3 + 23 * C**3 * D + 159 * C**2 * D * F
    - 27 * C**2 * E * F + 10 * C * D**3 + 13 * C * D**2 * E
    + 3 * C * D * E**2 + 350 * C * D * F**2 - 101 * C * E * F**2
    + 20 * D**3 * F + 16 * D**2 * E * F - 27 * D * E**2 * F
    + 248 * D * F**3 + E**3 * F - 124 * E * F**3
)
assert sp.factor(8 * L4 - (A * C + C * D + 2 * D * F - E * F)) == 0
print("sanity guard: 8*L4 == AC+CD+2DF-EF : PASS", flush=True)
assert sp.factor(192 * L6 + P30) == 0
print("sanity guard: 192*L6 + P30 == 0 (P30 30-monomial) : PASS", flush=True)
assert len(sp.Poly(P30, *params).terms()) == 30
print("sanity guard: P30 has 30 monomials : PASS", flush=True)
print(f"guards elapsed: {time.time() - t_start:.1f}s", flush=True)

# report each L_d's monomial count / homogeneous degree (exact)
print("\nd  monomials  hdeg", flush=True)
counts = {}
for d in (4, 6, 8, 10, 12):
    e = sp.expand(sp.together(obstruction[d]))
    num, den = sp.fraction(e)
    assert den == 1, f"L{d} has denominator — not polynomial"
    p = sp.Poly(num, *params)
    monoms = p.terms()
    degs = [sum(m) for m, _ in monoms]
    hdeg = degs[0] if all(x == degs[0] for x in degs) else None
    counts[d] = len(monoms)
    print(f"{d}  {len(monoms):9d}  {str(hdeg):5s}", flush=True)
print("monomial counts L_d:", [counts[d] for d in (4, 6, 8, 10, 12)],
      flush=True)

# ---------------- (3) ideal memberships, exact Groebner over QQ ----------------
def membership(lab, poly, gens, order="lex"):
    """Decide poly in <L_gens> over QQ, lex order, by Groebner reduction.
    Returns True/False AND prints the basis, the reduction remainder and
    whether it is 0, plus the cross-check G.contains(poly).  Additionally
    verifies the reduction identity  poly == sum(q_i * b_i) + rem  exactly
    over the returned Groebner basis b_i and quotient list q_i."""
    gpolys = [sp.expand(obstruction[gid]) for gid in gens]
    t = time.time()
    G = sp.groebner(gpolys, *params, order=order)
    tb = time.time()
    poly_e = sp.expand(sp.together(poly))
    red = G.reduce(poly_e)
    # sympy 1.11: red = (quotients_list, remainder); take the LAST element
    rem = red[-1] if isinstance(red, tuple) else red
    if isinstance(rem, (list, tuple)):
        rem = rem[-1] if len(rem) else sp.Integer(0)
    tr = time.time()
    iszero = sp.simplify(rem) == 0
    contains = G.contains(poly_e)
    # cofactor/remainder identity: poly == sum(q_i * b_i) + rem
    if isinstance(red, tuple) and len(red) > 0 and isinstance(red[0], list):
        quot = red[0]
        basis = [sp.Poly(b, *params).as_expr() for b in G.polys]
        if len(quot) == len(basis):
            ident = sp.expand(poly_e - (sum(q * b for q, b in zip(quot, basis))
                                        + rem))
            ident_ok = ident == 0
        else:
            ident_ok = None
    else:
        ident_ok = None
    print(f"\n[{lab}] generators: <{', '.join(['L'+str(gid) for gid in gens])}> "
          f"(lex)", flush=True)
    print(f"[{lab}] groebner basis size: {len(G.polys)} "
          f"({tb - t:.1f}s), reduce: {tr - tb:.1f}s", flush=True)
    print(f"[{lab}] reduction remainder == 0 ?  {iszero}", flush=True)
    print(f"[{lab}] reduction identity poly == sum(qi*bi)+rem verified :  "
          f"{ident_ok}", flush=True)
    if not iszero:
        rp = sp.Poly(sp.expand(rem), *params)
        print(f"[{lab}] nonzero remainder: {len(rp.terms())} monomials "
              f"(certificate of non-membership)", flush=True)
    print(f"[{lab}] G.contains(poly) cross-check :  {contains}", flush=True)
    if iszero != contains:
        print(f"[{lab}] !! MISMATCH between remainder==0 and contains — "
              f"machinery suspect", flush=True)
    return iszero and contains


m_L8_in_46 = membership("m1", L8, [4, 6])
m_L6_in_4 = membership("m2", L6, [4])
m_L10_in_468 = membership("m3", L10, [4, 6, 8])
m_L12_in_468 = membership("m4", L12, [4, 6, 8])

# ---- positive controls: validate the reduction machinery (a False here
#      means reduce() is broken, and every result above is void) ----
print("\n" + "=" * 72, flush=True)
print("POSITIVE CONTROLS (machinery soundness: must all be True):", flush=True)
c1 = membership("ctrl1", L4, [4, 6])                  # generator in own ideal
c2 = membership("ctrl2", L8, [4, 6, 8])               # generator in own ideal
c3 = membership("ctrl3", sp.expand(L4 * L8 + L6), [4, 6])  # explicit combo
all_ok = c1 and c2 and c3
print(f"\ncontrols all True: {all_ok}", flush=True)
if not all_ok:
    print("ABORT: reduction machinery failed its positive controls; "
          "m1..m4 are NOT trustworthy", flush=True)
    raise SystemExit(2)

print("\n" + "=" * 72, flush=True)
print("MEMBERSHIP SUMMARY (lex order, exact over Q):", flush=True)
print(f"  L8  in <L4,L6>     -> {m_L8_in_46}   "
      "(False = third generator independent/needed)", flush=True)
print(f"  L6  in <L4>        -> {m_L6_in_4}    "
      "(False = first two generators independent)", flush=True)
print(f"  L10 in <L4,L6,L8>  -> {m_L10_in_468} "
      "(True = Bautin-trick step survives)", flush=True)
print(f"  L12 in <L4,L6,L8>  -> {m_L12_in_468} "
      "(True = Bautin-trick step survives)", flush=True)
print("=" * 72, flush=True)
print(f"total wall time: {time.time() - t_start:.1f}s", flush=True)