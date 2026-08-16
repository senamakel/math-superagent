# Grounding report — the seven adopted approaches (research pass)

The inventor subagent timed out before handing a candidate list, so this pass
grounded the approaches the run is actually alive on: the seven marked
`adopted` in `research/approaches/`. Each was checked against the literature on
three axes — what the reformulation is called, the precise statement of any
theorem it relies on and whether its hypotheses hold here, and whether anyone
has applied it to *this* problem. Statuses were set to `grounded` where the
literature+machine verifications support them, with the still-open arithmetic
input named precisely in each status line. None is refuted this pass.

## Per-candidate verdicts

### downset-row-code-distance-closed-form — grounded
- **Named:** meet/join-matrix spectral theory (Mattila LAA 2014, doi
  10.1016/j.laa.2014.10.001; Ilmonen–Kaarnioja LAA 2017, doi
  10.1016/j.laa.2017.09.023) is the named home of the Boolean-lattice meet
  matrix `(2^{pc(d∧d')}) = ⊗[[1,1],[1,2]]`. The intersection formula
  `|M_d ∩ M_d'| = 2^{pc(d∧d')}` is an instance of the standard subcube fact:
  two affine subcubes of F₂ⁿ intersect in an affine subcube whose dimension is
  the size of the intersection of their free-coordinate sets (Friedgut–Kalai–
  Naor, Proc. AMS 1996; Chung–Sieger arXiv:2209.03573; Kupavskii–Noskov
  arXiv:2209.04756 on downsets).
- **Holds here:** yes — the reflection identity `M_d = {n−1−y : y⊆d}` and
  meet-closure `M_d∩M_d' = M_{d∧d'}` are exactly that subcube fact on this row
  set; the machine verification and the A₂ = Θ((log n)²) check are on disk.
- **Applied to this problem?** No — no source computes the distance
  distribution A_k of a Pascal-fold row set, nor applies Delsarte/MacWilliams
  to a sliding-window fold weight. `F_n(z) = O(n) for |z|<1` is now a theorem
  (popcount split), closing the geometry side of the second-moment program.
- **Buys:** the only number-theoretic content left is the single second-moment
  statement (A): `E[S(n)²] = O(n)` for the prime string.

### meet-join-parseval-self-duality — grounded
- **Named:** Parseval / Krawtchouk–MacWilliams diagonalization + Mattila meet
  matrix. The self-duality `Ĉ_n(ω) = S_ω(n)` is elementary index bookkeeping
  (hand- and machine-verifiable).
- **Holds here:** the identities are exact; the z=0 reproduction of
  `fair-model-exact-binomial` is the Scholze gate.
- **Applied to this problem?** The sharp negative — Parseval bounds a weighted
  average, and `S_h² ≤ O(n)·2^{nH(p)}` is strictly worse than trivial — is the
  key finding: the geometry provably carries **no pointwise force** on a single
  input. This is the honest limit locating exactly where the "fold does work"
  hypothesis ends.
- **Buys:** pins that (A) is irreducibly arithmetic; no input-free spectral
  argument can close SUPPLY.

### derivative-ladder-delta-commutation — grounded
- **Named:** F₂ Frobenius difference operator Δ = 1+σ commuting with the fold
  (Lucas). The backbone (L1) T_{Δ^k h}(n,d) = T(n+k,d+k), (L4) anti-Pascal, and
  (L5) Δh[j] = [q_j ≢ q_{j+2} mod 4] are **machine-verified** on disk (claim
  `derivative-ladder-identities-survive`).
- **Holds here:** yes, over free binary h; (L5) on the real prime residue
  string.
- **Applied to this problem?** No prior source; the arithmetic input is exactly
  the distance-2 index-domain parity barrier, which the literature (LOS 2016;
  Matomäki–Merikoski unter Siegel-zero) leaves open. So the route's honest
  product is the exact invariance/equivalence theorem (GOAL priority 5 flavour),
  not a solution.
- **Buys:** a genuine structural result — SUPPLY is invariant under h → Δ^k h —
  and a clean formulation of the weakest-input question.

### fold-second-moment-krawtchouk — grounded
- **Named:** Delsarte LP bound + MacWilliams identity on the distance
  distribution (standard coding theory). The Krawtchouk diagonalization
  `F_n(z) = 2^{-n} Σ_ω (1−z)^{wt}(1+z)^{n−wt} Ĉ_n(ω)²` is hand-verified.
- **Holds here:** the identity needs no linearity (only the LP bound does);
  condition (C) `F_n(z)=O(n)` is now *proved* by the downset closed form.
- **Applied to this problem?** No prior application of Delsarte/MacWilliams to
  a fold weight; the application is the speculative half.
- **Buys:** second moment `E[S²] = O(n)`; reduces SUPPLY's density-1 form to
  the single arithmetic statement (A).

### lucas-mixing-finite-transfer — grounded
- **Named:** Pivato–Yassawi Thm 7.1 (arXiv:math/0306136): for Φ = 1+σ over
  Z/2, "Φ asymptotically randomizes µ (on a density-one Cesàro set) ⟺ µ is
  Lucas mixing". The hypothesis holds here because SUPPLY's fold is the finite
  1+σ and Lucas is its engine.
- **Applied to the primes?** No — searches return the CA-mixing literature and
  the prime-residue literature, but no paper connects them. Lucas mixing of the
  prime string is not established anywhere.
- **Open content:** the finite transfer (a)+(b). Step (a) is orthogonal to the
  mod-4 switch-density mean (Bernoulli(ρ) is Lucas mixing for every ρ), so it
  does NOT inherit the ABGS switch-side dead end — but it is an
  unestablished correlation-decay statement on the primes, not a theorem.
- **Buys:** a named, sharp target for the weakest-input question.

### function-field-fqt-model — grounded
- **Named:** function-field PNT-in-AP / Chebotarev: PPT in AP Ψ(n;Q,A) ~
  q^n/Φ(Q) (Keating–Rudnick arXiv:1204.0708); short-interval and AP results
  (Bank–Bary-Soroker–Rosenzweig Duke 2015, doi 10.1215/00127094-2856728;
  Kurlberg–Rosenzweig FFA 2021, doi 10.1016/j.ffa.2021.101838;
  Bary-Soroker–Gorodetsky–Karidi–Sawin Trans. AMS 2019, doi 10.1090/tran/7945).
- **Gap:** every one of these is a one-point / value-domain statement; none
  controls the degree-ordered CONSECUTIVE switch statistic the fold reads. The
  transfer is open — so this is grounded as a *model test*, not a proof.
- **Buys:** settles (in the model) whether Φ does work on an input whose
  arithmetic is fully explicit, localizing the obstruction.

### squared-excess-higher-order-dyadic-correlations — grounded
- **Named:** run-telescope across symmetric differences + character products;
  the evenness corollary (no standalone switch-sign term in S(n)²) is a
  theorem of the meet formula.
- **Holds here:** hand-verified; machine verification is the route's first step.
- **Applied to this problem?** The literature (LOS 2016: r≥2 consecutive-prime
  patterns are open; Matomäki–Merikoski only under Siegel-zero hypotheses)
  gives **no** orthogonality theorem for products of switch signs at the fold's
  classified separations. So the honest position is geometry grounded, the
  arithmetic (priority-4-vs-5 question) open.
- **Buys:** pins the minimal priced object; whether products of switch signs
  are strictly weaker than switch density is now decidable in principle.

## Cross-cutting conclusion

The single repeated fact, confirmed by every route into the arithmetic: **the
mod-4 consecutive-prime two-point correlation** (switch density, and the
distance-2 / index-domain products the fold reads) **is genuinely open**. LOS
2016 explicitly states that for r ≥ 2 consecutive primes little is known about
the pattern distribution, and ABGS §9 says it cannot be treated using
L-functions; Matomäki–Merikoski only reach two-point correlations under a
Siegel-zero hypothesis. No source supplies a weaker-input correlation statement
that would close SUPPLY's (A). Every geometry route is grounded; the arithmetic
gap is the single open door, and it sits exactly as GOAL.md predicts.

## Sources used (URLs)

- LOS 2016: https://doi.org/10.1073/pnas.1605366113
- Mattila 2014: https://doi.org/10.1016/j.laa.2014.10.001
- Ilmonen–Kaarnioja 2017: https://doi.org/10.1016/j.laa.2017.09.023
- Pivato–Yassawi: https://arxiv.org/pdf/math/0306136
- Keating–Rudnick: https://doi.org/10.48550/arxiv.1204.0708
- Bank–Bary-Soroker–Rosenzweig: https://doi.org/10.1215/00127094-2856728
- Kurlberg–Rosenzweig: https://doi.org/10.1016/j.ffa.2021.101838
- BGKS 2019: https://doi.org/10.1090/tran/7945
- Chung–Sieger: https://arxiv.org/abs/2209.03573
- Kupavskii–Noskov: https://arxiv.org/abs/2209.04756
- Matomäki–Merikoski: https://arxiv.org/abs/2112.11412
