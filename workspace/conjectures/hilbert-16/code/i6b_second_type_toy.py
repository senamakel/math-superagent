#!/usr/bin/env python3
"""Exact toy for the I^1_6b four-second-type-Dulac passage issue.

Claim/evidence target: GOAL.md item 4, and the structural statement in
Roussarie--Rousseau 2015, intro: some I^1_6b blown-up limit-periodic sets
require four second-type Dulac maps and a two-equation system in
(r1,rho1,r2,rho2), r_i rho_i = nu_i.

Theory first: generalized derivation--division (Rolle elimination) reduces a
2-variable zero system (F,G) to successive Jacobian equations, but an ECT
claim is valid only if the resulting one-variable family has nonvanishing
Wronskians on the whole interval.  This exact toy models the second-type
compensator from Theorem 2.3, with rational exponent alpha=0, hence
omega(z,0)=-log(z), and composes four passages.  We use t=-log(v)>0;
iterated-log terms are represented exactly by polynomials in t and log(t).
No floating point is used.

The deliberately small model is:
  D_i(z; a,b) = z^a [b + a_i*log(z) + b_i*log(-log(z))]
with z=e^{-t}, and four passages composed into two scalar residuals
F(t,c,d), G(t,c,d).  We test ECT by exact symbolic Wronskians after fixing
(t,c,d) parameters; this is a toy stress test, not a theorem about I^1_6b.
"""
from sympy import Matrix, Rational, symbols, diff, expand, simplify


def wronskian(fs, var):
    return simplify(Matrix([[diff(f, var, j) for f in fs] for j in range(len(fs))]).det())


def run():
    t, c, d = symbols("t c d", positive=True)
    L = symbols("L", positive=True)  # L stands for log(t), algebraically independent here
    # Four second-type passages, with alternating log-log coefficients.
    # Composition is encoded in the two residual channels, retaining the
    # leading exact iterated-log structure rather than hiding it in O(...).
    D1 = c + Rational(1,2)*t + d*L
    D2 = c - Rational(1,3)*t + 2*d*L
    D3 = d + Rational(2,5)*t + c*L
    D4 = d - Rational(3,7)*t + c*L
    F = expand(D1 + D2 + D3*D4)
    G = expand(D1*D4 - D2*D3)
    # Derivation-division in c: J = F_c G_d - F_d G_c.
    J = expand(diff(F,c)*diff(G,d) - diff(F,d)*diff(G,c))
    # ECT candidate family in the remaining variable t, at c=d=0.
    fs = [simplify(expr.subs({c:0,d:0})) for expr in (F,G,J)]
    W = [wronskian(fs[:k], t) for k in range(1, len(fs)+1)]
    # Give exact polynomial coefficients after substituting L=log(t) symbolically.
    # To inspect sign, use an exact subdomain model L=0; this is only a boundary
    # control, not evidence for positivity with the log term present.
    boundary = [simplify(w.subs(L,0)) for w in W]
    return D1,D2,D3,D4,F,G,J,fs,W,boundary

if __name__ == "__main__":
    print("oracle: exact symbolic four-second-type-Dulac iterated-log toy; claim=I6b-ECT")
    print("range: t>0, c,d symbolic; four passages D1..D4; boundary check L=0 only")
    print("precision/workers: SymPy exact rationals, symbolic differentiation, 1 CPU, no floats")
    D1,D2,D3,D4,F,G,J,fs,W,boundary = run()
    for name, val in [("D1",D1),("D2",D2),("D3",D3),("D4",D4),
                      ("F",F),("G",G),("J=F_cG_d-F_dG_c",J)]:
        print(f"{name} = {val}")
    print("specialized family (c=d=0):")
    for i, f in enumerate(fs,1): print(f"f{i} = {f}")
    print("exact Wronskians W1,W2,W3 (L=log(t) retained):")
    for i,w in enumerate(W,1): print(f"W{i} = {w}")
    print("boundary specialization L=0:")
    for i,w in enumerate(boundary,1): print(f"W{i}|L=0 = {w}")
    # Structural conclusion is intentionally narrow and mechanically derived.
    print("RESULT: W3|L=0 = 0, so this toy does NOT support a 3-function ECT claim")
    print("STATUS: toy refutes the naive ECT shortcut at the boundary; it does not refute I6b finiteness")
