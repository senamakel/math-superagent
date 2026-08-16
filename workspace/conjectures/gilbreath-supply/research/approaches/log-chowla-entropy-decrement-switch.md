# Entropy decrement / log-averaged Chowla for the switch-sign product correlations

```approach
idea: >
  The squared-excess route (`squared-excess-higher-order-dyadic-correlations`,
  adopted) reduces density-1 SUPPLY to E[S(n)²] = O(n), equivalently to bounds on
  the products ∏_R χ(q_{a_R}) χ(q_{b_R}) of the switch signs u_j = χ(q_j)χ(q_{j+1})
  at the fold's classified separations. These are higher-order (order ≥ 4 in χ)
  correlations of a sequence built from CONSECUTIVE primes. Attack them with Tao's
  entropy-decrement machine and the logarithmically-averaged Chowla–Elliott
  conjecture (Tao 2016; Matomäki–Radziwill–Tao averaged Chowla) — the named
  machinery purpose-built to show higher-order correlations of "prime-like"
  sequences vanish without any multiplicativity in the index.
mechanism: >
  (1) Entropy decrement does not require the target sequence to be multiplicative
  in its own index; it requires the sequence to FACTOR through a multiplicative
  source. The switch sign u_j = χ(q_j)χ(q_{j+1}) is a 2-point function of the
  multiplicative character χ at consecutive primes, so its higher-order
  correlations are exactly correlations of χ sampled at a structured set of prime
  indices. (2) The standard Möbius inversion on the prime indicator (the same
  device as Mauduit–Rivat's solution of the Gelfond digit-sum problem, in the
  library) expresses Σ_{n≤N} S(n)² — after the squared-excess run telescope — as
  log-averaged correlations of the bounded multiplicative function χ over INTEGER
  arguments at the fold's separations. (3) This is index-domain in n (the averaging
  is over the window length), so it does NOT encounter the value-shift obstruction
  that killed `dispersion-bilinear-large-sieve` and
  `matomaki-radziwill-index-autocorrelation`; and it does NOT claim Walsh/U²
  structure, so it avoids the basis mismatch that killed `gowers-u2-nilsequence-
  uniformity`. The arithmetic content is isolated as a log-averaged Chowla-type
  statement for χ, strictly weaker than positive mod-4 switch density (GOAL
  priority 2), and the second moment closes by Chebyshev (GOAL priority 1).
status: adopted
first-step: >
  tool_builder + research, exact arithmetic, real residue string r_j = q_j mod 4.
  (1) MACHINE-VERIFY the squared run-telescope identity (SQ) for n ≤ 60 and every
      ordered pair (d,d') ∈ [2,n−1]²: ε_d ε_{d'} = ∏_{R∈runs(M_d△M_{d'})}
      (−1)^{[r_{a_R}≠r_{b_R}]}, checked against the literal ε_d ε_{d'} =
      (−1)^{T(n,d)⊕T(n,d')} (raw [r_a≠r_b] form at the position-0 boundary).
      NEGATIVE CONTROL: an r mod 3 boundary must break (SQ) on a positive count,
      else the check is vacuous. This closes the one gap the squared-excess route
      left hand-only.
  (2) STRATIFY the off-diagonal Σ_{d≠d'} ε_d ε_{d'} for the real primes at
      n = 400/1000/4000 by symmetric-difference size k = |M_d△M_{d'}| and by
      run-count, printing per-stratum partial sums. THE GATE (attacks the method
      before trusting it): (i) machine-confirm no stratum equals the standalone
      adjacent switch density Σ_a u_a (even-symmetric-difference theorem); (ii)
      compare the fold-weighted off-diagonal against the unweighted switch-product
      sum to decide whether the fold's A_k weights are load-bearing for the O(n)
      cancellation — if the unweighted sum is already O(n) the fold does no work
      (priority-5 flavour), if only the weighted sum is O(n) the priced object is
      the fold-weighted bilinear form (priority-4 flavour).
  (3) HAND research the precise statement: after Möbius-inverting the prime
      indicator, is Σ_{n≤N} S(n)² a sum of correlations of the bounded
      multiplicative χ at the fold's classified separations to which Tao's
      entropy-decrement / log-averaged Chowla hypotheses apply? FALSIFIER: the
      conversion reproduces the adjacent switch density (⇒ priority 5) instead of
      a strictly weaker weighted statement (⇒ priority 4).
falsifies: >
  (a) the Möbius-inverted identity is wrong (bookkeeping); (b) the product
  correlations cannot be expressed as correlations of a single bounded
  multiplicative function (then entropy decrement is not applicable); (c) research
  shows the needed log-averaged Chowla statement is at least as hard as the switch
  density itself (then priority 5 — equivalence — is the truth, recorded as such).
```
