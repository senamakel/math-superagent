# Inventor convergence decision — round candidates closed, new line adopted

Memory server was down at write time; this note is the durable record (persist to Cognee once it recovers).

## Verdicts on the three round candidates

1. **Martinet–Ramis–Écalle–Voronin moduli and codimension — refuted.** The classification is by FUNCTIONAL (infinite-dimensional) Stokes/transition moduli, not a finite-dimensional moduli space. No theorem converts codimension in those moduli into parameter-uniform cyclicity. Sources: Ilyashenko 2024 (doi:10.1088/1361-6544/ad76f3), Martinet–Ramis (doi:10.24033/asens.1462).

2. **Noetherian-chain Khovanskii–Rolle — refuted.** Noetherian/LN zero theorems (Gabrielov–Khovanskii; Binyamini arXiv:2405.16963) require an explicitly supplied finite algebraic differential system, a domain avoiding its singular locus, and bounded complexity. The open DRR return map has no such uniform representation; its transseries (singular, parameter-dependent exponents, iterated logs/exponentials) does not imply Noetherianity.

3. **Iterated-Abelian Gauss–Manin rank — narrowed.** Ordinary Abelian integrals are a finite C[t]-module (Novikov–Yakovenko), and higher Melnikov functions are iterated integrals in integrable foliations (Gavrilov; IMPA namo-2006). This survives only for Hamiltonian/near-Hamiltonian perturbations at a fixed finite Melnikov order; it does not cover the full nonlinear displacement of I^1_6b, H^3_13, DI_2b, H^3_14.

## The adopted synthesis

**`dulac-cochain-stokes-consistency`** — do not deny the transseries; keep the full functional cochain and locate the finite core *inside* the classification.

- Ilyashenko's Centennial History §4.7 **Theorem 4.12**: the flat correspondence map of a real analytic saddle-node decomposes as
  `F = g ∘ f0 ∘ h_{k,a} ∘ H`,  with `f0 = e^{-1/x}`, `h_{k,a}(x) = kx^k / (1 − a k x^k log x)`, `g` a holomorphic germ, and `H` a **normalizing cochain** for a parabolic germ.
- **Theorem 4.10**: a functional cochain is uniquely determined by its formal Taylor series.
- **Theorem 4.11**: a functional cochain flat on (R_+, 0) is identically zero.

So the genuinely functional part `H` is determined by formal data, and the finite data part is `(k, a, 1-jet of g)`. The proposal: cyclicity of a polycycle is controlled by the finite composition shape (which vertices, resonance data k, a) together with the Stokes-cocycle consistency relations across overlapping sectors — a finite consistency system in the coefficient algebra over Q. Zero counting = counting simultaneous solutions of the cocycle consistency system, not counting transseries zeros.

- **Analyticity / Test 1** is located at the cochain/Stokes step: a smooth-but-not-analytic passage has no cochain, no Stokes cocycle, no finite consistency system.
- **Status**: adopted but unproven. The local Theorem 4.12 is sourced and held; the global finite-consistency-system step is the open target.

## First concrete step

1. (lean_prover) State `FlatCorrespondenceMapDecomp : ∃ k a H g, F = g ∘ f0 ∘ h_{k,a} ∘ H` in `code/lean/Lib/DulacCochain.lean` as a Cited axiom (src: Ilyashenko Centennial History §4.7 Thm 4.12), plus Cited axioms for Thm 4.10 and 4.11.
2. (tool_builder) Build the two-sector cochain consistency condition `H2 ∘ H1^{-1} = flat` from the DIR normal form, reduce to a finite algebraic relation on the coefficients, and count solutions over Q — capture to `code/out/cochain_consistency.captured.txt`.

## Falsifiers

- (a) The Stokes-cocycle consistency system is not finitely generated over the coefficient algebra (infinitely many independent 2-sector relations) → no finite core → narrows to individual-finiteness.
- (b) The cochain H is not eliminable via Thm 4.10, i.e. finite data do not determine the zero count → refuted as a uniform route.
- (c) The cochain signature (k, a) jumps across the parameter stratum → narrows to stratum-by-stratum cyclicity (the DRR program itself).
