# Short-index orthogonality of the prime character — the Matomäki–Radziwill engine in the index domain

```approach
idea: >
  The refuted dispersion route died for one precise reason: the object lives in
  the PRIME INDEX, not the prime value, so value-shifted character sums
  (χ(n−a)) do not apply. But there is a modern, named toolbox built for exactly
  the index-domain orthogonality that the run telescope actually needs — the
  Matomäki–Radziwill theory of multiplicative functions on short blocks. Recast
  the averaged form of SUPPLY as a second moment of the prime-race sequence
  s_j = χ(q_j) = (−1/q_j) = (−1)^{(q_j−1)/2}, and price that second moment by
  the orthogonality of a multiplicative function along the PRIME INDEX at dyadic
  separations, not by two-point residue frequency. Target: Σ_{n≤N} S(n)² =
  O(N^{2−δ}), which by Chebyshev gives ν₂(n)/n → 1/2 on a density-1 set
  (GOAL priority 1).

mechanism: >
  By the run telescope (claim g-run-telescope-verified, checked),
  (−1)^{T(n,d)} = ∏_R s_{a_R} s_{b_R} with every run of the down-set ↓d of
  length 2^{ν₂(d+1)}, so each depth-d sign is a product of the character at
  index pairs (a_R, b_R) with b_R − a_R = 2^{ν₂(d+1)} — a dyadic INDEX shift.
  Squaring S(n) = Σ_d (−1)^{T(n,d)} and averaging over n ≤ N expands into
  correlations of s at dyadic index separations. This is the index-domain
  bilinear form the refuted route could not reach by value shifts.

  The engine is Matomäki–Radziwill "Multiplicative functions in short
  intervals" (Ann. Math. 183 (2016)): for a bounded multiplicative f of small
  mean, the short sums Σ_{x<n≤x+H} f(n) are o(H) on average over x, for H a
  power of x. The arithmetic object here, s along primes, is recovered by the
  standard passage Σ_{j≤J} s_j ↔ Σ_{n≤X} Λ(n) χ(n) (von Mangoldt weighting), so
  the dyadic-shift autocorrelation Σ_j s_j s_{j+2^g} is an index-domain
  two-point correlation of a multiplicative function at a controlled separation
  — precisely the shape the MRT/Teräväinen circle treats (their "short
  intervals" are short value-intervals; the index-domain version is the
  literal statement the run needs, and is strictly weaker than the pointwise
  switch density because it is an AVERAGED/L² statement, not a mean).

  The priced input is therefore (i) for each fixed g, the averaged dyadic
  autocorrelation Σ_{j≤N} s_j s_{j+2^g} = o(N), or the still weaker (ii) a
  single second-moment bound Σ_{n≤N} S(n)² = o(N²). Both are orthogonal to the
  mod-4 switch-density mean (an L²/autocorrelation statement vs a one-point
  frequency), and neither reopens the five doors: all-ones h gives s the
  alternating string whose dyadic autocorrelations are deterministic (the
  collapse), Thue–Morse gives a 2-automatic s (the collapse) — both must and do
  FAIL the orthogonality input, so the negative controls are built in.

status: refuted

precedent:
  - "Matomäki & Radziwill, Multiplicative functions in short intervals, Ann. of
    Math. 183 (2016) 1015–1056, DOI 10.4007/annals.2016.183.3.6. EXACT
    statement grounded: for f multiplicative, |f(n)|≤1, for any ε>0 there is
    H(ε) such that for H(ε)<h≤X, (1/X)Σ_{x∈[X,2X]} |(1/h)Σ_{n=x}^{x+h} f(n) −
    (1/N)Σ_{n≤N}f(n)| ≤ ε. The blocks are VALUE intervals of the argument n."
  - "Matomäki, Radziwill, Tao, An averaged form of Chowla's conjecture, Algebra
    & Number Theory 9 (2015) 2167–2196, DOI 10.2140/ant.2015.9.2167: averaged
    Chowla, sums λ(a_1 n+b_1)···λ(a_k n+b_k) over value shifts. Value-domain."
  - "Tao, The logarithmically averaged Chowla and Elliott conjectures for
    two-point correlations, Forum Math. Pi 4 (2016), DOI 10.1017/fmp.2016.6:
    logarithmically averaged λ(n)λ(n+h), value-domain; breaks the parity
    barrier for the VALUE-shifted two-point object, not the index-shifted one."
  - "Tao & Teräväinen, The structure of logarithmically averaged correlations,
    Duke Math. J., DOI 10.1215/00127094-2019-0002 (2019)."
  - "On-disk: g-run-telescope-verified (checked),
    excess-is-negative-character-sum (checked), abgs-p1-wide-open (asserted),
    lau-nonconstant-pattern-open (asserted), dispersion-bilinear-large-sieve
    (refuted)."
killed-by: >
  Two independent objections, either alone fatal. (1) HYPOTHESES DO NOT HOLD:
  MRT's engine is short VALUE-intervals [x,x+H] of a MULTIPLICATIVE function
  f(n); the object here is the index-domain two-point correlation
  Σ_j χ(q_j)χ(q_{j+2^g}), and the sequence j ↦ χ(q_j) (the quadratic character
  at the j-th prime) is NOT multiplicative in the prime INDEX j (the primes are
  not multiplicative in j). So MRT, its averaged-Chowla extension, and its
  log-averaged form — every statement grounded above is a value-domain block or
  a value-shifted correlation λ(a n+b) — do not reach an index-domain
  correlation along the prime index. This is the SAME root obstruction that
  refuted dispersion-bilinear-large-sieve: the object lives in the prime index,
  and MRT (like Linnik dispersion) is a value-domain tool. The candidate's own
  open-step concedes this transfer is the crux. (2) THE g=0 STRATUM IS EXACTLY
  SWITCH DENSITY, NOT A WEAKER AVERAGED INPUT: the bridge back to MRT's domain
  is the von Mangoldt passage Σ_j s_j s_{j+2^g} ↔ Σ_p χ(p)χ(p') over prime pairs
  at INDEX separation 2^g; at g=0 (index-adjacent) this is
  Σ_j χ_4(q_j)χ_4(q_{j+1}), the mod-4 consecutive-pair switch correlation, whose
  positivity/decay is the named open parity barrier (abgs-p1-wide-open,
  lau-nonconstant-pattern-open). Hence the claimed 'averaged form orthogonal to
  switch density and weaker than it' is false: the L² average at the coarsest
  dyadic scale contains the implication of positive switch density, so a
  second-moment bound Σ_{n≤N}S(n)²=O(N^{2−δ}) is not reachable without
  resolving the switch-side parity barrier. The engine is real; it is refuted
  as applied to THIS index-domain object, for the same reason the dispersion
  route died and with the additional internal collapse at g=0.
open-step: >
  The exact index-domain transfer. MRT controls Σ_{x<n≤x+H} f(n) with the
  interval in the VALUE of the argument; the object here is Σ over a block of
  the PRIME-INDEX sequence s_j. The passage through Σ Λ(n)χ(n) makes the
  one-point object accessible, but the dyadic two-point autocorrelation
  Σ_j s_j s_{j+2^g} is a genuine two-point correlation along the prime index —
  pricing it is the open step. This must be priced honestly: it is weaker than
  pointwise switch density but may still be as hard as the parity barrier at
  g=0 (adjacent indices). The averaged-over-g second-moment (ii) is the form
  most likely to close.
first-step: >
  tool_builder, exact integer/F₂ arithmetic, real residue string s_j = χ(q_j):
  (1) compute the dyadic-shift autocorrelation A_g(N) = Σ_{j≤N} s_j s_{j+2^g}
  for g = 0..10 and N up to the oracle ceiling, print A_g(N)/N — the falsifier:
  if A_g(N)/N does not decay (in particular g=0, adjacent-index), the input (i)
  is as hard as the parity barrier and the route must retreat to the
  averaged-over-g form (ii); (2) compute Σ_{n≤N} S(n)² and its growth exponent
  against the oracle, and confirm the negative controls (all-ones, Thue–Morse)
  fail to decay; (3) hand off the per-g decay table to research as the priced
  arithmetic input, clearly labelled as a measurement, not a proof.
```

## Distinctness and honesty

- **Not** `dispersion-bilinear-large-sieve` (refuted): that route squared S(n) and applied Linnik dispersion with value-shifts χ(n−a); it died because `q_{j+2^g}` is not `q_j + const`. This route stays entirely in the index domain and uses MRT orthogonality, which is the index-domain engine the refutation note itself pointed at.
- **Not** `dyadic-gap-character-correlation` (adopted): that route prices the two-point correlations χ(q_j)χ(q_{j+2^g}) *pointwise*, i.e. asks for each g a separate mean statement. This route prices the *averaged* second moment, the L² form GOAL priority 1 explicitly favours.
- **Not** `prime-race-variance-large-sieve` (in-folder, distinct): that route bounds everything by the one-point race W(J) via BDH. This route uses MRT-style short-block orthogonality of a multiplicative function, a different engine for a possibly weaker input.

**Speculative half:** whether the averaged second moment Σ_{n≤N} S(n)² = o(N²) is strictly weaker than positive switch density. It is not claimed; it is the thing research must price. If the g=0 (adjacent-index) stratum dominates and its decay IS the parity barrier, this route collapses to GOAL priority 3 (the equivalence), and that would be a genuine negative finding worth recording.
