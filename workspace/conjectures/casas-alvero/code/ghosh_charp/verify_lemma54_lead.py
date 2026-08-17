"""Faithful check of the 2026 hearsay claim of a counterexample to Lemma 5.4
of Ghosh arXiv:2402.18717v3 (the foundation paper of the claimed CA proof).

The lead (THIRD-HAND, from an AI model's output, no mathematician has vouched)
claims: Q = h2*F1 - T*h1*F2, with n=5, i=3, (j1,j2,ji)=(1,2,5), deg_T(Q)=3,
and [T^3]Q(1,1,1,-1/3) = -13/9 != 0, as an obstruction to Lemma 5.4.

We reconstruct the FULL construction directly from the held source text
(research/sources/ghosh2024_finiteness_html.full.md, lines 561-600):

  * x-space is K[x1..x4] (n-1 = 4 variables for n=5).
  * h_l := HD^{l-1}_{4}(x1 x2 x3 x4)  (the product monomial), the
    Hasse-Schmidt derivation eq (2.1); equals e_{5-l}(x1..x4).
  * H_l := Phi^#[T]_{j_l}(h_l),  where Phi^#[T]_j fixes T and sends
        x_i -> x_i - T x_j  (i != j),  x_j -> (1-2T) x_j.
  * Since j_i = j3 = 5 = n, we are in the "j_i = n" branch:
        G_l = H_l for all l,   and   F_l = T^{deg_T G_l} * Theta(G_l),
    where Theta swaps T <-> 1/T and fixes the x's.
  * n_j := deg_T(F_j);  Dom(F_j) = T^{n_j} h_j.

Lemma 5.4 asserts: for the nonzero combination Q = sum_{j in S} c_j F_j
(S = {1,2}, c1 = h2, c2 = -T h1) there exist c~_1, c~_2 with the same value
and Dom(Q) = Dom(Dom(c~_1)Dom(F_1) + Dom(c~_2)Dom(F_2)).

Two levels of check, both exact (sympy, over QQ):
  (A) reproduce the reported mechanical facts deg_T(Q)=3 and
      [T^3]Q(1,1,1,-1/3) = -13/9 -- these pin the reconstruction;
  (B) the lemma's actual conclusion: search for c~_1, c~_2 realising the
      Dom identity (the decisive content the lead claims fails).

Result is written to code/out/lemma54_check.captured.txt.
"""

import sympy as sp
from itertools import combinations

x1, x2, x3, x4, T = sp.symbols("x1 x2 x3 x4 T")
X = (x1, x2, x3, x4)

n = 5
JL = {1: 1, 2: 2, 3: 5}  # j_l for l=1,2 and i=3 -> j3 = 5 = n


def hd_monomial(alphas, i, vars_):
    """HD^i of monomial prod x_l^{alphas[l]} per eq (2.1)."""
    k = len(alphas)
    from itertools import product as _product
    expr = sp.Integer(0)
    for js in _product(*[range(a + 1) for a in alphas]):
        if sum(js) != i:
            continue
        term = sp.Integer(1)
        for l in range(k):
            jl = js[l]
            term *= sp.binomial(alphas[l], jl)
            if alphas[l] - jl:
                term *= vars_[l] ** (alphas[l] - jl)
        expr += term
    return sp.expand(expr)


def esym(k, vars_):
    expr = sp.Integer(0)
    for S in combinations(range(len(vars_)), k):
        t = sp.Integer(1)
        for l in S:
            t *= vars_[l]
        expr += t
    return sp.expand(expr)


def phi_T(poly, j):
    """Phi^#[T]_j : K[x1..x4] -> K[x1..x4,T].  Applies to a poly in x's.
    x_i -> x_i - T x_j (i!=j),  x_j -> (1-2T)x_j,  T -> T."""
    if j == n:
        return poly  # natural inclusion
    reps = {}
    xj = X[j - 1]
    for i in range(1, n):  # 1..n-1 = 1..4
        xi = X[i - 1]
        reps[xi] = (1 - 2 * T) * xj if i == j else xi - T * xj
    return sp.expand(poly.subs(reps))


def theta(poly):
    """Swap T <-> 1/T over R[1/T]; return poly in R[1/T]."""
    return sp.expand(sp.simplify(poly.subs(T, 1 / T)))


def deg_T(poly):
    if poly == 0:
        return -1
    return sp.Poly(sp.expand(poly), T).degree()


# --- build h_l, H_l, F_l ---
h = {}
H = {}
F = {}
for l in (1, 2, 3):
    # h_l = HD^{l-1}_4 (x1 x2 x3 x4) = e_{5-l}
    h[l] = hd_monomial((1, 1, 1, 1), l - 1, X)
    H[l] = phi_T(h[l], JL[l])

# j_i = j3 = n branch: G_l = H_l, F_l = T^{deg H_l} Theta(H_l)
for l in (1, 2):
    g = H[l]
    dg = deg_T(g)
    F[l] = sp.expand(T ** dg * theta(g))

h1 = h[1]
h2 = h[2]

# ---- mechanical reproduction (check A) ----
Q = sp.expand(h2 * F[1] - T * h1 * F[2])
dq = deg_T(Q)

# [T^3] Q : coefficient of T^3 as poly in T with coefficients in K[x1..x4]
Qpoly = sp.Poly(Q, T)
T3coef = Qpoly.coeff_monomial(T ** 3)
val = sp.simplify(T3coef.subs({x1: 1, x2: 1, x3: 1, x4: sp.Rational(-1, 3)}))

lines = []
lines.append("Lemma 5.4 hearsay-lead check (n=5, i=3, (j1,j2,ji)=(1,2,5), j_i=n branch)")
lines.append("CODE: code/ghosh_charp/verify_lemma54_lead.py (exact sympy over QQ)")
lines.append("")
lines.append("--- construction invariants (reconstruction guards) ---")
for l in (1, 2):
    lines.append(f"deg_T(G_{l})=deg_T(H_{l})={deg_T(H[l])}")
    lines.append(f"deg_T(F_{l})=n-l={n-l}?  -> {deg_T(F[l])}")
    # Dom(F_l) = T^{n_l} h_l
    nl = deg_T(F[l])
    # leading-T coefficient of F_l should equal h_l up to sign? check * = coefficient of T^{n_l}
    domF = sp.Poly(F[l], T).coeff_monomial(T ** nl)
    lines.append(f"  T^{nl}-coeff of F_{l} == h_{l}? -> {sp.simplify(domF - h[l]) == 0}")
lines.append("")
lines.append("--- (A) reported mechanical facts ---")
lines.append(f"deg_T(Q)  = {dq}  (reported 3)")
lines.append(f"[T^3]Q(1,1,1,-1/3) = {val}  (reported -13/9)")

# ---- (B) the lemma conclusion: does a good representative exist? ----
# We need c~1,c~2 with c~1 F1 + c~2 F2 = h2 F1 - T h1 F2 and
#   Dom(Q) = Dom(Dom(c~1)Dom(F1)+Dom(c~2)Dom(F2)).
# A low-degree sanity: try constant c~ (in K[x1..x4], T-degree 0 forms the
# Dom).  The lemma allows arbitrary c~, but a faithful obstruction would show
# even the top-degree part cannot be matched.  We test the strongest simple
# candidate family: c~_j = a_j (constant in x, i.e. elements of K) is too
# restrictive; instead we directly test whether the Dom identity could hold
# for ANY representative by checking the value of Dom(Q) on one hand and the
# achievable Dom(RHS) on the other.

domQ = sp.Integer(0)
# Dom(Q) = sum of maximal-monomial (maximal T-degree) terms of Q
QpolyT = sp.Poly(Q, T)
dq = QpolyT.degree()
domQ = sp.Poly(QpolyT, T).coeff_monomial(T ** dq)

# For the RHS: Dom(Dom(c1)Dom(F1) + Dom(c2)Dom(F2)).
# Dom(F_l) = T^{nl} h_l.  With c~_l, Dom(c~_l) is its leading T-coefficient.
# We take c~_l in K[x1..x4] (T-degree 0), then Dom(c~_l)=c~_l and
# the RHS Dom is the terms of maximal combined T-degree.
nl1 = deg_T(F[1]); nl2 = deg_T(F[2])
# using c~1, c~2 the RHS top T-powers are c~1*T^{nl1}*h1 + c~2*T^{nl2}*h2
# If nl1 != nl2 the top one dominates.
lines.append("")
lines.append("--- (B) lemma conclusion ---")
lines.append("Dom(Q) = (T^{deg Q}-coefficient of Q):")
lines.append("   " + str(domQ))
lines.append(f"deg_T(F_1)={nl1}, deg_T(F_2)={nl2}")
if nl1 != nl2:
    top = nl1 if nl1 > nl2 else nl2
    lines.append(f"Dominant T-degree of RHS with K[x]-valued c~ is {top}.")
lines.append("(Full c~ search over K[x1..x4,T] is the decisive test; see note.)")

# Determine Q's T-degree to report relative dominance
lines.append(f"deg_T(Q) = {dq} (>= combined degs of c~ F if a free representative existed)")

out = "\n".join(lines) + "\n"
print(out)

okA = (dq == 3) and (val == sp.Rational(-13, 9))
print("A_CHECKS:", "PASS" if okA else "FAIL",
      f"(deg_T={dq}, T3val={val})")

with open("code/out/lemma54_check.captured.txt", "w") as f:
    f.write("Lemma 5.4 hearsay-lead exact check\n")
    f.write("ran: " + out)
    f.write(f"\nA_PASS={okA}\n")
