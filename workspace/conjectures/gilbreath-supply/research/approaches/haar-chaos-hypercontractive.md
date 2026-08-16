# S(n) as a structured Wiener–Itô/Haar chaos form: hypercontractivity on the cube

```approach
idea: >
  Work directly in the ±1 digit domain s_j = χ(q_j) ∈ {±1}, where each fold
  cell is a genuine monomial: the corrected endpoint identity gives
  (−1)^{T(n,d)} = Π_{R ∈ runs(↓d)} s_{a_R} s_{b_R} (no spurious sign).
  Therefore S(n) = Σ_{d=2}^{n−1} Π_R s_{a_R} s_{b_R} is a STRUCTURED
  multilinear form (a Wiener–Itô / Haar chaos form) in the sequence s, and
  bounding it is a norm inequality on the discrete cube — the domain of the
  Bonami–Beckner–Gross hypercontractive inequality and the Khintchine /
  Marcinkiewicz Lp-equivalences for the Haar system. No probability space over
  the primes is introduced and no basis mismatch arises, because the monomials
  are read in the s domain where the Walsh/Haar system is the native basis.

mechanism: >
  The pairs (a_R, b_R) over all d form the boundary pairs of digital down-sets
  — a dyadic-tree collection (the run decomposition of ↓d, already verified as
  claim g-run-telescope-verified). Order the terms by degree 2·(#runs) and by
  dyadic tree; S(n) is a sum of disjoint-pair products, i.e. a high-degree
  chaos form in the Haar/Walsh expansion of s. Hypercontractivity
  (Bonami–Beckner: ‖f‖_q ≤ (q−1)^{d/2} ‖f‖_2 for degree-d chaos) and the
  unconditional-basis (Schauder) properties of the Haar system bound
  ‖Σ_d Π_R s_{a_R} s_{b_R}‖ in terms of the L² mass and the degrees, PROVIDED
  the degrees and supports have bounded overlap structure — a deterministic
  combinatorial fact about the down-set boundary pairs, the s-domain analogue
  of the already-proved geometry fact F_n(z) = O(n). The arithmetic input is
  then a second-moment condition on s (bounded dyadic autocorrelation — GOAL
  priority 2), and the engine converts it to S(n) = O(√n), hence ν₂/n → 1/2.
  Distinct from the refuted `dyadic-martingale-azuma`: no filtration and no
  randomization of the prime string. Distinct from the refuted
  `gowers-u2-nilsequence-uniformity`: that route's mismatch (fold cells are
  ANF, not Walsh) does not arise here, because in the s domain the cell IS a
  Walsh monomial Π s_{a_R} s_{b_R}.

status: refuted

first-step: >
  (tool_builder, exact ±1 arithmetic on real s_j = χ(q_j))
  (1) BUILD the chaos decomposition: for every d ∈ [2,n−1] write
      Π_R s_{a_R} s_{b_R} as a signed Walsh monomial over its distinct support,
      and record degree 2·(#runs) and the support size. (2) COMPUTE the overlap
      matrix K_{d,d'} = |supp(mon_d) ∩ supp(mon_{d'})| and its profile
      (how many pairs have large overlap) for n ≤ 4000. (3) TEST the
      hypercontractive estimate: for random ±1 s, measure max_n |S(n)|/√n and
      confirm it matches the chaos-norm bound; run all-ones and Thue–Morse s as
      negative controls — they must VIOLATE the second-moment input.
      FALSIFIER: if degrees grow too fast or the overlap matrix is dense
      (K concentrates at high overlap), no hypercontractive bound of the
      claimed shape exists, and the reason is recorded.

killed-by: >
  Two independent defects, either alone fatal.
  (1) HYPERCONTRACTIVITY DOES NOT BOUND A DETERMINISTIC SUM. The Bonami–Beckner
  inequality ‖Σ_|S|=k f̂(S)χ_S‖_q ≤ (q−1)^{k/2} ‖·‖_2 is a statement about a
  RANDOM vector (x uniform on the cube): it controls moments ‖f‖_p of a random
  evaluation. It therefore bounds the SRMS of S(n) over random digit strings s.
  But SUPPLY's S(n) is a FIXED ±1 string s_j = χ(q_j) at one n. A norm bound
  over the cube measure gives, at best, a bound on E_s[|S(n)|^p] over random s —
  which the fair model already supplies exactly (wt(Φ_n h) is Binomial(n−2,1/2),
  claim fair-model-exact-binomial, proved from rank Φ_n = n−2): the random
  model gives |S(n)| ≈ √n with subgaussian tail, including the white-noise
  measurements (g-normalized-fold-weight-white-noise). The transfer from "random
  s gives S=O(√n) w.h.p." to "the FIXED prime string gives S=O(√n)" is precisely
  the finite-prefix transfer every prior route lacks and no source supplies —
  it is the same missing gate that killed `lucas-mixing-finite-transfer` and
  `dyadic-martingale-azuma`. Hypercontractivity only recovers the random bound,
  not the deterministic one.
  (2) THE ARITHMETIC INPUT IS STILL THE PARITY BARRIER AT g=0. The route's
  priced input is "bounded dyadic autocorrelation of s" = the L² mass. But the
  L² mass at g=0 is Σ_j χ(q_j)χ(q_{j+1}) = the mod-4 switch-pair object, whose
  positivity/vanish is the named open problem (abgs-p1-wide-open:
  L-function-inaccessible; lau-nonconstant-pattern-open: even ONE non-constant
  2-term pattern open). So the second-moment condition the chaos bound would
  need is not weaker than positive switch density — it re-encounters the parity
  barrier at the coarsest dyadic scale, which is where the real weight sits
  (the refuted `dyadic-gap-character-correlation` measured the bulk of S(n) in
  the g=0-adjacent strata for the primes). Whether the monomials have
  "bounded-overlap structure" is also open and is not established by any source:
  the monomials reach degree ~n, and no hypercontractive bound with a (q−1)^{d/2}
  constant (exponential in degree) is useful once d ~ n.
  (3) BASIS NOTE: the route claims its s-domain monomial Π s_{a_R}s_{b_R} is a
  genuine Walsh monomial, correctly distinguishing it from the refuted
  gowers-u2 route. This is true and is the one clean thing here — but a Walsh
  monomial in s is a statement about the RANDOM cube; making it a statement
  about the fixed prime string is exactly the gap in (1).

precedent: >
  The hypercontractive inequality is real, correctly stated, and named:
  - Bonami (Ann. Inst. Fourier 1970), Beckner (Ann. of Math. 1975), Gross
    (J. Funct. Anal. 1975): for f of degree ≤ d on {±1}^n,
    ‖f‖_q ≤ (q−1)^{d/2}‖f‖_2 (q≥2) with sharp constant; level-d inequalities.
    Survey with exact statement and constant: Biswal, "Hypercontractivity and its
    applications" (2011), arXiv:1101.2913; O'Donnell, "Analysis of Boolean
    Functions" (CUP 2014), Ch. 9–10.
  - Vector-valued / sharp refinements: Eskenazis–Ivanisvili, "Polynomial
    inequalities on the Hamming cube", Probab. Theory Relat. Fields (2021),
    DOI 10.1007/s00440-020-00973-y; Keller–Lifshitz–Marcus, "Sharp
    Hypercontractivity for Global Functions", arXiv:2307.01356.
  - What bounds a deterministic structured ±1 sum would require is NOT in any of
    these: they are moment/norm inequalities over the random cube. No source
    applies hypercontractivity to force linear fold weight of a FIXED prime
    string; the second-moment + finite-transfer ingredients are exactly what the
    parity barrier names as open.
  Inside-workspace: g-run-telescope-verified (checked), fair-model-exact-binomial
  (proved), g-normalized-fold-weight-white-noise (measured), abgs-p1-wide-open,
  lau-nonconstant-pattern-open (parity barrier).
  Verification caveat: the monomial identity and run decomposition are
  machine-checked on disk; the overlap-matrix profile (degree/support growth) is
  proposed but un-run (no execution tool on this pass).
```

## Speculation, marked

That the down-set boundary-pair family has the bounded-overlap structure
hypercontractivity needs is speculation: the monomials can have degree as large
as ~n (d with many runs), and no source is known to bound the L⁴ norm of this
particular structured sum. The first step prices that overlap structure before
any norm inequality is trusted. What is established and checkable today: the
monomial identity (endpoint-sign-corrected-identity, checked) and the dyadic
run decomposition (g-run-telescope-verified, checked).

## Distinctness check

- Not `dyadic-martingale-azuma` (refuted: Azuma applies only to a random
  process). Here the final bound is a deterministic norm inequality.
  — But as defect (1) shows, hypercontractivity is ALSO a random-process
  statement, so the route inherits exactly the defect it claimed to avoid.
- Not `gowers-u2-nilsequence-uniformity` (refuted: basis mismatch). Here the
  cells are read in the s domain where they ARE Walsh monomials.
  — True, but the basis is orthogonal to the failure: the deterministic-to-random
  transfer is the gap, not the basis.
- Not `fold-second-moment-krawtchouk` (adopted: second moment in the h domain
  via the row-code distance). This is the same second moment re-expressed in
  the s domain as a chaos form, with a different engine (hypercontractivity
  rather than Delsarte/MacWilliams).
  — The adopted route at least computes the ROW-CODE distance distribution as a
  deterministic object; this route's engine is inherently randomised.
