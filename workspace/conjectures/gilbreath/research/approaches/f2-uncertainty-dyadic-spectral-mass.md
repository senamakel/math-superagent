# ν₂ supply via an F₂ uncertainty principle on the dyadic spectral mass of the switch bit

```approach
idea: Express the supply deficit w/2 − ν₂ as a dyadic Fourier (Walsh) coefficient of the mod-4 switch bit h, and apply a harmonic-analytic uncertainty principle over F₂ (Donoho–Stark / Matolcsi–Szűcs) to convert "small dyadic spectral mass" into ν₂ ≥ c·w. The supply theorem becomes conditional on one checkable arithmetic hypothesis about the prime bit: bounded 2-adic autocorrelation.
mechanism: |
  ν₂(q_n) = wt(Φ_n h). The proposal decomposes h = h_D + h_⊥ with h_D the
  projection onto the "dyadic-periodic subspace D_n", asserts Φ_n h = Φ_n h_⊥,
  and applies an F₂ uncertainty principle to bound wt(Φ_n h) below by a
  constant times (w − dyadic-spectral-mass).
status: refuted
killed-by: transfer-matrix-kernel-allones — the collapse is a single direction, not a dyadic subspace; and the uncertainty principle cannot fire on a surjective fold
  (1) WRONG OBJECT FOR "DYADIC SPECTRAL MASS": the kernel of Φ_n is NOT a
      dyadic-periodic subspace. It is the SINGLE vector span(111..1)
      (checked claim `transfer-matrix-kernel-allones`; hand-check n=5). There
      is no "diagonalisable on dyadic characters" / min period a power of 2
      structure to project h onto — the whole "dyadic spectral mass" premise
      (h_D, the characters constant on D_n, Φ singular on D_n) does not
      correspond to the actual linear algebra of Φ_n. The character that Φ_n
      is singular on is the CONSTANT character (all-ones), not a period-2^m
      family.
  (2) AN UNCERTAINTY PRINCIPLE CANNOT BOUND wt(Φ_n h) FOR A SURJECTIVE MAP.
      wt(Φ_n h) is the (ordinary) weight of the image of h under a fold whose
      image is the FULL space F₂^{n−3}. A nonzero h with wt(h) large can have
      wt(Φ_n h)=1 (any h mapping to a weight-1 codeword) — the classic finite-
      abelian Donoho–Stark bound |supp(f)|·|supp(f̂)| ≥ |G| bounds a product of
      the function with its FOURIER transform, not with the image under an
      arbitrary linear fold. There is no uncertainty inequality that forces the
      image weight of a surjective linear map to be large; the very statement
      is refuted by the all-ones h (wt(h)=n−2 maximal, wt(Φ_n h)=0).
  (3) The empirical, prime-specific content (nu2/w ∈ [0.515, 0.87]) that the
      candidate wanted to capture is NOT a spectral inequality — it is case (b)
      of `g-supply-transfer-refuted`: a fact about the specific prime bit
      string, equivalent to the two-point mod-4 correlation whose unconditional
      lower bound is named-open (`abgs-2011-s9-mod4-switch-limit-open`). The
      uncertainty route would still have to prove that bound.
precedent: |
  Uncertainty principles over finite abelian groups are real and sharp:
  Donoho–Stark; Matusiak–Przebinda, "The Donoho–Stark uncertainty principle for
  a finite abelian group" (Apl. Math. 73 (2004)); Tao's prime-order improvement;
  "An uncertainty inequality for finite abelian groups" (Europ. J. Combin. 2004,
  doi:S0195669804001453); Feng–Hollmann–Xiang "The shift bound for abelian
  codes and generalizations of the Donoho–Stark uncertainty principle" (2018,
  arXiv:1804.00367). All bound a product/sum of |supp| with |supp| of the
  FOURIER transform; none transfers to the image weight under a surjective
  fold, and none is applied to Gilbreath. Consistent with
  `block-growth-literature-not-covered`.
first-step: (was) compute Walsh coefficients of the prime h — this is real and cheap but
  does NOT feed the claimed inequality, because the inequality's object (dyadic
  spectral mass vs image weight) is not the one Φ_n defines.
side: regeneration (supply side)
named-mathematics: Walsh–Hadamard transform, dyadic characters, Donoho–Stark / Matolcsi–Szűcs uncertainty, Krawtchouk polynomials
speculative: (moot) the sharp constant and whether the prime h has bounded dyadic spectral mass.
falsifier: (moot at the mechanism level) a dense scan showing the prime h's dyadic spectral mass stays bounded away from 0.
```
