# Second-type Dulac maps, slow divergence, and ECT: precise status

## Source-backed result

Rousseau–Shan–Zhu (2015), §2.6 distinguishes first-type maps (between blow-up sections `rho=rho0` and `r=r0`) from second-type maps (from `ybar=y0` to `r=r0` or `rho=rho0`). It explicitly says that only first-type maps are needed in that paper (source lines 147–152). Its Theorem 2.3 gives the first-type rational-resonance formula with the Ecalle compensator `omega(x,alpha)=(x^{-alpha}-1)/alpha` (and `-log x` at alpha=0), a displayed remainder having property J, and the refined hyperbolicity-ratio-one formula. Theorem 2.5 gives a separate ordinary saddle transition in a normal form, with property-I remainder; Theorem 2.7 treats saddle-node central and stable-center transitions.

The same paper proves finite cyclicity for `I^1_12` and `I^1_13`, not the open center graphics `I^1_6b`, `H^3_13`, and `DI_2b`. Its Theorem 1.1 closes only the boundary limit-periodic sets of those three graphics. In the proof of the relevant convex graphics, finite cyclicity follows from a displacement equation involving maps for which the cited first-type formulas suffice; this is not a theorem about the unprovided second-type endpoint germ in `I^1_6b`.

Huzak (2018) closes a different graphic, `DF_2a`, by family blow-up, slow divergence integral, and slow-fast analysis. This validates the mechanism in that geometry but does not transfer its hypotheses to `I^1_6b`.

GMV (2008/2010) proves a sufficient ECT criterion for Abelian integrals over Hamiltonian ovals of separated form `H=Phi(x)+Psi(y)` (and `H=A(x)+B(x)y^(2m)`), under explicit balance/CT/Wronskian and endpoint little-o hypotheses. It applies to a first-order Abelian/Melnikov family only. No source identifies the complete `I^1_6b` displacement with such a family.

## Exact missing hypothesis

The missing implication is not “more slow-divergence estimates.” To lift first-order slow-divergence control to full cyclicity one needs a theorem, uniform on every parameter stratum (including the identically-zero slow-divergence locus), of the following form:

1. derive all four actual second-type Dulac endpoint maps in the RR blow-up coordinates, with a common analytic/quasianalytic or sufficiently strong parameter-uniform flat/transseries remainder class;
2. prove that the complete displacement germ (the composition/sum of these endpoint maps and regular transitions) is contact-equivalent, or otherwise zero-count equivalent, to a *specified finite-rank* ECT/derivation–division family, with all parameter-dependent coefficients and degeneracies included; and
3. verify the nonvanishing Wronskians/CT conditions uniformly, plus endpoint/domain and section transversality hypotheses.

Without (1), there is no source-backed second-type germ. Without (2), a slow-divergence integral is only the first displacement/Melnikov term. Without (3), GMV cannot be invoked. In particular, a sum of passage-wise ECT-like terms need not itself be ECT (the exact toy Wronskian probe in `code/out/i6b_second_type_toy.captured.txt` gives zero Wronskian); this is an obstruction to the shortcut, not a dynamical counterexample.

Marín–Villadelprat's Dulac-map results show why the remainder hypothesis matters: the relevant uniform class controls mixed parameter/state derivatives, while mere pointwise or state-only flatness is insufficient for a Rolle/implicit-function argument. Their 2024 coefficient theorem is for hyperbolic saddles, not the unresolved second-type semihyperbolic endpoint germ.

## Verdict

Known: first-order slow-divergence/Abelian ECT tools separately; complete closure of DF_2a; RR boundary-set closure. Unknown: the second-type endpoint formula and the uniform finite-rank reduction of the full `I^1_6b` displacement. The ECT route remains a conditional approach, not a proof of finite cyclicity.

Sources: [[rousseau-shan-zhu-2015-second-type-dulac-full.full]], [[huzak-cyclicity-degenerate-df2a.full]], [[grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full]], [[marin-villadelprat-dulac-coefficient-properties-2024-arxiv.full]].
