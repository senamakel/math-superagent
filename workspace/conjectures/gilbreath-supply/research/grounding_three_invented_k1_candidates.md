# Grounding report — the three invented K>1 candidates (research pass)

The inventor proposed three lines for the reopened question (a functional of the
fold sensitive to correlation order `K ∈ (1, n/2]`, controllable by an input
strictly weaker than pointwise mod-4 switch density). All three have been taken
to the literature and all three are **refuted on evidence**. This is a genuine
negative result, not an absence: each was killed by a structural fact that does
not depend on the primes.

## Objective of the pass

Per GOAL priority 2, the three candidates were priced the same way:
1. what the reformulation is actually called,
2. the precise statement of any theorem it relies on and whether its hypotheses
   hold here,
3. whether anyone has applied it to *this* problem,
4. what it would buy (or why it cannot).

## Per-candidate verdicts

### parity-shadow-kruskal-katona — refuted
- **Named:** Kruskal–Katona theorem (minimal shadow at the compressed /
  colex-initial-segment extremal, Lovász form), Harper's vertex-isoperimetric
  theorem on the cube, and the shadow-isoperimetry stability results
  (Keevash–Long arXiv:1807.09618; Keevash Adv. Math. 2008;
  Chowdhury; Harper 1964).
- **All real and correctly stated.** But they bound `|∂F|` — the CARDINALITY of
  the ordinary shadow — a cardinality-valued quantity. The candidate's object
  is the **parity (odd) shadow** `#{d : |S' ∩ down(d)| odd} = wt(Φ_n h)`, a
  mod-2 zeta transform, which can cancel entirely for a spread family.
- **Holds here? The engine does not apply.** Isoperimetric shadow theorems
  never bound the number of ODD intersections of a family with a down-set.
- **Applied to this problem?** No. No source applies Kruskal–Katona/Harper to a
  parity shadow of a prime-gap switch set. I found no theorem lower-bounding a
  parity (mod-2) shadow at all — because the parity shadow is the F2 zeta
  transform, not the ordinary shadow.
- **Killed by (decisive, structural, prime-independent):** the kernel vectors
  `even-alt`/`odd-alt` (claim fold-rank-is-n-2-nullity-2-alternating,
  machine-verified) have `wt(Φ_n x)=0`, yet `even-alt` is a *maximally spread*
  set — ~half of every popcount layer of the m-cube. So the candidate's own
  falsifier ("if a SPREAD set has nu2 = o(n), the bound cannot work") fires
  with `nu2 = 0`. The escape "unless S' cancels into the kernel" names the one
  fact the run cannot prove about the primes (that the prime switch set avoids
  the 2-dim kernel), and measured nu2~n/2 showing it does is the conclusion of
  SUPPLY, not an available input.

### hl-ktuple-moment-method — refuted
- **Named:** Hardy–Littlewood prime k-tuple conjecture with singular series
  `S(h)=∏_p (1−|H mod p|/p)/(1−1/p)^{|H|}` (Kowalski Acta Arith. 2011; Invent.
  Math. 2023 probabilistic reinterpretation; Merikoski arXiv:1605.04757) and
  the moment method / number-theoretic CLT (Leung arXiv:2402.07941; de la
  Bretèche–Fiorilli Proc. LMS; Dixit–Murty).
- **All real.** But:
- **Holds here? Three defects, any one fatal.**
  - **(Price reversal)** HL k-tuples is **stronger**, not weaker, than switch
    density. Switch density IS the m=2 HL pattern frequency; the higher moments
    need k>2 HL. So the route accepts a stronger price to buy a weaker-grade
    conclusion — the reverse of the target.
  - **(Gaussian resummation is the hard step, not a finite check)** E[S²ʳ]
    under HL is not a finite combinatorial count; the factorization F_n(z)^r
    fails for r≥2; and measured kurtosis ~2.95 (claim
    fourth-moment-plateau-3n2) is not cleanly Gaussian.
  - **(Main-term mod-4 unbiased)** The leading 2-tuple singular series assigns
    equal weight to the four pair classes; the LOS 57.5% switch is a
    lower-order/secondary correction (claim los-scale-bias-slowdecay). Same
    unbias-defect that killed cramer-gallagher-second-moment.
- **Applied to this problem?** No. No source applies the HL moment method to
  the fold weight or the submask-correlation excess; the moment-CLT works all
  ASSUME a uniform HL variant (inside the conjecture, not cheaper).

### radon-transform-z2k-uncertainty — refuted
- **Named:** Diaconis–Graham, "The Radon transform on Z_2^k", Pacific J. Math
  118 (1985) 323–345; DG/Vance Fourier-transform certainty; Krawtchouk spectral
  machinery (same toolbox as the grounded fold-second-moment-krawtchouk and
  meet-join-parseval-self-duality routes).
- **Holds here?** DG 1985 is for the FULL hyperplane transform; the candidate's
  partial subcube family `{M_d}` is exactly where their theorems stop — their
  Krawtchouk eigenvalue theorem and uncertainty inequality are not stated for a
  partial subcube family.
- **Killed by (decisive, proven in this workspace):** spectral machinery bounds
  the Walsh-side SUPPORT of an operator/distribution — not the fixed-input F2
  image weight wt(Φ_n h). The grounded route `meet-join-parseval-self-duality`
  already PROVED the spectral geometry carries no pointwise force on a single
  input (S_h² ≤ O(n)·2^{nH(p)} is worse than trivial). This candidate is
  another spectral route on the same row-set Walsh spectrum and inherits that
  negative; calling the operator "partial" does not change that the
  diagonalization is a distributional identity. Plus the K*(n)=floor(n/2)
  correlation order and Walsh degree are conflated in a way the witness does
  not support.
- **Applied to this problem?** No. No source applies the Radon/uncertainty
  machinery to the Pascal-mod-2 fold weight.

## Cross-cutting conclusion

Each of the three candidate languages — spectral/Radon, lattice-isoperimetric,
analytic-number-theory moment method — is real and correctly named, and none was
previously applied to this object. All three collapse for reasons that do NOT
depend on the primes: the parity-shadow candidate dies on the kernel-vector
spread witness (even-alt spread, shadow 0); the HL candidate dies on price
reversal + main-term mod-4 unbiasedness + asserted Gaussian resummation; the
Radon candidate dies on the proven pointwise-no-force spectral negative and the
partial-vs-full-engine mismatch.

The single surviving pattern is unchanged and is now stronger for having swept
three more languages: **no input-free (or prime-unconditional) spectral,
isoperimetric, or moment input forces wt(Φ_n h) ≥ c·n** — the run's own spectral
route proved the pointwise-no-force half, and the two arithmetic-heavy
candidates (HL k-tuples, isoperimetric shadow) either price a stronger input or
rely on cancellation physics that the mod-2 zeta transform provably annihilates.
This corroborates GOAL priority 5 (SUPPLY equivalent to a switch-density-type
statement) as the honest remaining close, with request walsh-spectral-subset-b904
still open as the only genuine candidate gap.

## Sources used (URLs)

- Diaconis–Graham, "The Radon transform on Z_2^k", Pacific J. Math 118 (1985),
  https://doi.org/10.2140/pjm.1985.118.323
- Keevash–Long, "Stability for vertex isoperimetry in the cube",
  https://doi.org/10.48550/arxiv.1807.09618
- Keevash, "Shadows and intersections", Adv. Math. 2008,
  https://doi.org/10.1016/j.aim.2008.03.023
- Kowalski, "Averages of Euler products...", Acta Arith. 2011,
  https://doi.org/10.4064/aa148-2-4
- "Large prime gaps and probabilistic models", Invent. Math. 2023,
  https://doi.org/10.1007/s00222-023-01199-0
- Merikoski, "Averaged form of the Hardy-Littlewood conjecture",
  https://doi.org/10.48550/arxiv.1605.04757
- Leung, "Moments of primes in progressions to a large modulus",
  https://doi.org/10.48550/arxiv.2402.07941
- de la Bretèche–Fiorilli, "Moments of moments of primes in arithmetic
  progressions", https://doi.org/10.1112/plms.12542
