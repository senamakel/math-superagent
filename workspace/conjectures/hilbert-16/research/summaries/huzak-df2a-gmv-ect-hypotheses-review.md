# Exact hypotheses review: Huzak DF2a and GMV ECT

Sources: [[research/sources/huzak-cyclicity-degenerate-df2a.full.md]], [[research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md]], [[research/sources/grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full.md]], [[research/sources/rousseau-shan-zhu-2015-second-type-dulac-full.full.md]].

## Huzak / DF2a

Huzak 2018's abstract explicitly proves finite cyclicity for the DRR graphic DF2a using family blow-up and geometric singular perturbation theory, including a slow-divergence integral. The underlying Dumortier–Rousseau normal form identifies DF2a as the center case `b0=0` of a finite-plane line-of-singular-points family:
`xdot=y+bxy-y^2+mu1+mu2*x+mu3*x^2`, `ydot=xy+mu4` (five-parameter unfolding). Their Theorem 3.1 applies to compact `K subset (0,infinity)` of graphic locations `x0`, and normalized perturbations `(D,E0,E1,E2)` in the compact boundary cylinder `C1`, but excludes every `delta`-neighborhood of the exceptional point `P*=(D,E0,E1,E2)=(0,0,0,1)`. For DF2a it gives at most 5 cycles off that excluded neighborhood; the sharper one-cycle conclusions require `b E1 >= 0`, while case (iii) gives one cycle away from the circle `D=E1=0`; the source explicitly says the P* case cannot be desingularized and remains untreated.

Therefore the safe claim is **not** “the slow-divergence theorem applies to I^1_6b.” I^1_6b is a different triple-nilpotent-at-infinity, center-surrounding graphic. No source here identifies its unfolding with the DF2a normal form, its slow curve, its compact cylinder, or its exceptional stratum. Huzak's result cannot be transferred without a new analytic conjugacy/normal-form identification and a proof that the transformed full parameter family satisfies the DF2a blow-up hypotheses, including treatment of the analogue of P*.

## GMV ECT

Grau–Manosas–Villadelprat Theorem A concerns analytic Abelian integrals over a period annulus of ovals of a separated Hamiltonian `H=Phi(x)+Psi(y)`, with integrands `fi(x) g(y) dx`. It requires the two specified involutions, the balance families `B_sigma1(fi/Phi')` and `B_sigma2(gi)` to be CT-systems, and `B_sigma2(g0)=o(y^(2m(n-2)))`. Theorem B concerns the special Hamiltonian form `H=A(x)+B(x)y^(2m)` and `g=y^(2s-1)`, requiring `s>m(n-2)` and the corresponding balance functions `ell_i` to be a CT-system. The theorem bounds zeros of this Abelian-integral vector space; it is a first-order Hamiltonian perturbation result, not a theorem about the complete nonlinear displacement map near a nonhyperbolic graphic.

No held source computes an I^1_6b return/displacement map in GMV's Abelian form, verifies a period annulus of ovals for the relevant full family, or checks the balance/CT and endpoint conditions uniformly over all blown-up parameter directions. The RR 2015 source proves only boundary limit-periodic sets for I^1_6b (and H^3_13, DI_2b), not the complete graphic. Thus GMV may be a conditional tool for a specifically reduced Hamiltonian/Melnikov subproblem, but currently does not apply to I^1_6b.

## Correction

Any claim saying Huzak's slow-divergence result or GMV ECT directly covers I^1_6b is overclaimed and should be downgraded to a conditional proposal/unverified applicability. The precise falsifier is an explicit I^1_6b normal form plus a parameter-uniform reduction of its full displacement to the stated DF2a slow-fast model or to GMV's Abelian-integral hypotheses; failure at any parameter stratum (especially slow-divergence-zero or non-Hamiltonian sectors) refutes the transfer.