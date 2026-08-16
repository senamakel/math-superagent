# Walsh / subset-sum lower bound on wt(Φ x) from the fold's own structure

```approach
idea: Prove wt(Φ_n x) ≥ c·n by a Walsh-spectral (Fourier over F₂) or subset-sum
      lower bound on the submask-supported linear map Φ itself, valid for inputs
      x that are not "complicated" in any of the five refuted senses. This uses
      Φ's structure, not h's complexity — the route the switch-density reduction
      discards.
mechanism: Φ_n is F₂-linear with row support exactly the binary submasks
      (Pascal-mod-2 / Rule-90). For any linear map M, wt(Mx) = (n/2) −
      (1/2) Σ_j (−1)^{(Mx)_j} is a Walsh-spectral quantity, so a lower bound
      reduces to bounding the sum of Walsh coefficients, i.e. to the subset-sum
      (XOR-independence) structure of M's rows. Lucas' theorem parametrizes
      those rows explicitly, so the question becomes combinatorial: which
      families of submask rows force a linear fraction of coordinates to be
      nonzero, independent of how rich x is.
status: refuted
precedent:
  - "Walsh/Fourier identity wt(Mx) = (n/2) − (1/2)Σ_j(−1)^{(Mx)_j} and the
     Walsh-spectrum / nonlinearity theory of Boolean functions (Stănică,
     'Graph eigenvalues and Walsh spectrum of Boolean functions' 2023;
     standard APN nonlinearity literature)."  https://doi.org/10.5281/zenodo.8347748
  - "Image-*size* bounds for nonlinear maps (APN: |Im f| ≥ (2^n+1)/3, etc.) —
     a different quantity (image cardinality) from image *weight* of a fixed
     vector under a LINEAR map; none bounds wt(Φ_n x) for the Pascal-mod-2 fold
     from geometry alone."  https://link.springer.com/article/10.1007/s10623-022-01094-4
  - closed door 4 witnesses (balanced AND anti-dyadic strings with wt(Φ_m h)∈{1,2},
     m=8,16,24,32) — problem.md §4
killed-by: closed door 4 + the kernel vectors.
      The all-ones string is maximally weighted, maximally uncomplicated, and
      lies in ker Φ_n (the corrected kernel span(even-alt, odd-alt) includes
      all-ones as their sum — see fold-rank-is-n-2-nullity-2-alternating), so wt(Φ_n x)=0 for it.
      Door-4's balanced anti-dyadic witnesses are in the candidate's own
      admissible class ("not complicated": balanced, anti-dyadic — none of the
      five doors) and yet have wt(Φ_m h) ∈ {1,2} ≪ m. Therefore any Walsh /
      subset-sum bound of the claimed shape must either (i) presuppose a
      complexity hypothesis on x — re-opening a closed door — or (ii) be false.
      The Walsh identity is correct but the sum of Walsh coefficients is
      controlled by the *input* x, whose extreme (kernel) vectors kill the bound;
      near-injectivity of Φ bounds the kernel, not the image weight, exactly the
      unifying obstruction problem.md names.
open-step: none for the claim as stated. The only survivable re-formulation
      would be a bound valid on a *complexity class of x* strictly disjoint from
      all five closed doors — and no source or computation produces such a class;
      the doors' witnesses are chosen precisely to cover every natural class.
first-step: (closed — but transfer the Walsh bridge to candidate 1, adopted).
      The pointwise identity wt(Φ_n h) = (n−2)/2 − (1/2)Σ_d (−1)^{T(n,d)} is exact
      and correct; what dies here is the claim that it yields a bound from Φ alone.
      In the adopted line (lucas-mixing-finite-transfer) this same identity is the
      transfer bridge, with the input-side correlation bound supplied by Lucas
      mixing rather than by Φ's geometry. Nothing else in this candidate survives.
      Scratch probe code/verify_candidate2_refutex.py was drafted for coder to run
      but was NOT executed in this run (no execution tool held); it is a scratch
      note, not evidence.
```

## Why it is distinct

This is the *harmonic-analytic* route: it leaves h almost entirely alone and
asks what the Walsh spectrum of Φ forces about image weight — the direct
converse of the five refuted "h is complicated enough" hypotheses.

## Literature verdict (research specialist, 2026-02)

- The Walsh identity is standard and correct, but it is not a structural bound:
  `(−1)^{(Mx)_j} = Π_i (−1)^{M_{ji}x_i}` and the character sum is determined by
  the *specific input* x, so no bound from M alone holds without a hypothesis
  on x.
- The APN / perfectly-nonlinear-map literature bounds image *cardinality*
  |Im f| of nonlinear maps — a different object. Nothing there bounds the
  *Hamming weight* of a fixed input's image under the specific Pascal-mod-2
  linear fold.
- The decisive witnesses (all-ones kernel vector; door-4 balanced anti-dyadic
  strings) are in problem.md, sourced as measured, and the corrected kernel fact
  (rank n−2, nullity 2, ker = span(even-alt, odd-alt)) is machine-verified.
  Combining them refutes the claim as stated.
- Honest caveat: I found no *paper* that explicitly states "no Φ-alone bound
  exists"; the refutation is by construction (the witnesses satisfy the
  candidate's own admissions) plus the general near-injectivity-obstruction
  principle, not by a citable theorem. Refuted on evidence, not merely absence.
