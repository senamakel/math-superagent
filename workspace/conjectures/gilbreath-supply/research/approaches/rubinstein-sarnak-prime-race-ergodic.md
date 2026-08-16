# The fold as a functional of the mod-4 prime race (Rubinstein–Sarnak measure)

```approach
idea: Treat ν₂(n) as a functional of the mod-4 prime race sample path r_j =
q_j mod 4, and attack the density-1 form of SUPPLY by transferring the
Rubinstein–Sarnak limiting measure of the Chebyshev-bias process (the one-point
race δ(x;4,3,1) under logarithmic density) through the fold, using the measure's
dilation-invariance/ergodicity.

mechanism: h is the first difference of r (h_j = [r_j ≠ r_{j+1}]), and Φ_n h is a
bounded multi-scale digital filter of r. The run telescope collapses each row to
products χ(r_{a_R})χ(r_{b_R}) over dyadic-separated endpoints, so S(n) =
Σ_{d} ∏_R χ(r_{a_R})χ(r_{b_R}) is a multilinear statistic of the race path. The
classical, fully proved object is the ONE-POINT race: Rubinstein–Sarnak establish
that the bias δ(x) = π(x;4,3) − π(x;4,1) has, under the logarithmic density, a
non-atomic limiting distribution (a measure on R invariant in an appropriate
sense under the dilation x → 2x), refined by the Lemke Oliver–Soundararajan
sawtooth. The candidate move: under that one-point limiting measure, show the
fold statistic S(n)/n → 0 (so ν₂/n → 1/2 on a log-density-1 set of n), and then
upgrade from log-density to natural density using the known regularity of the
race. The arithmetic input is the one-point race only — NOT the pair pattern,
which is the open barrier. The fold is exactly the device that reads a
one-point-biased sequence and returns a second-moment-type statistic, which is
the route to making the fold "do work the switch-density form cannot see".

falsifier: the g=0 stratum of S(n) contains the ADJACENT pair product
χ(r_j)χ(r_{j+1}), i.e. the pair pattern. If the Rubinstein–Sarnak one-point
measure does not determine the distribution of a digitally-filtered race (and the
g=0 term genuinely needs pair data), the route collapses to switch density.
Research must check whether ANY source computes the RS limiting measure of a
filtered/functional race, or whether the g=0 term is forced to vanish from the
one-point input alone.

status: refuted
killed-by: >
  The Rubinstein-Sarnak engine is real but conditional and one-point, and the
  fold's g=0 stratum is an unconditionally-open two-point object. (1) The RS
  limiting distribution for the mod-4 bias δ(x)=π(x;4,3)-π(x;4,1) (logarithmic
  density of {x: δ(x)>0} ≈ 0.9959) holds only under GRH and LI (linear
  independence of the non-negative imaginary parts of the nontrivial zeros of
  Dirichlet L-functions); it is conditional, so it cannot ground an unconditional
  SUPPLY. (2) By the run telescope (g-run-telescope-verified, checked), the g=0
  stratum of S(n) reads the residue string at ADJACENT indices: it is Σ_j
  χ(r_j)χ(r_{j+1}), the mod-4 switch-pair correlation. A one-point race
  distribution (counts per residue class) does not determine the joint
  distribution of adjacent residues — that is exactly the parity barrier (ABGS
  §9, abgs-p1-wide-open, lau-nonconstant-pattern-open: positive mod-4 switch
  density "cannot be treated using L-functions"). One-point input cannot force
  the g=0 term to vanish; no source computes a digital/fold functional of the
  race from the one-point measure alone. (3) The consecutive-prime (mod q)
  pattern asymptotics (Lemke Oliver-Soundararajan) — the two-point side that the
  g=0 term would need — are CONJECTURAL (Hardy-Littlewood/k-tuple based), so they
  are not an available resource either.
precedent:
  - "Rubinstein, Sarnak, Chebyshev's bias, Experiment. Math. 3 (1994) 173-197,
    DOI 10.1080/10586458.1994.10504289: under GRH+LI, normalized pi(x;4,3)-
    pi(x;4,1) has a limiting distribution under LOGARITHMIC density; log-density
    of the set {x: π(x;4,3)>π(x;4,1)} ≈ 0.9959."
  - "Fiorilli, Martin, Inequities in the Shanks-Rényi prime number race,
    Crelle 2012, DOI 10.1515/crelle.2012.004 (GRH+LI asymptotic series for the
    logarithmic densities)."
  - "Harper, Lamzouri, Orderings of weakly correlated random variables, and
    prime number races with many contestants, Probab. Theory Relat. Fields 2017,
    DOI 10.1007/s00440-017-0800-2 (races from one-point data under GRH+LI)."
  - "Granville, Martin, Prime number races, Amer. Math. Monthly 113 (2006),
    DOI 10.1080/00029890.2006.11920275 (survey; GRH+LI conditional)."
  - "Lemke Oliver, Soundararajan, Unexpected biases in the distribution of
    consecutive primes, PNAS 113 (2016), DOI 10.1073/pnas.1605366113
    (consecutive-prime mod q patterns, conjectural)."
  - "In-workspace: g-run-telescope-verified (checked), abgs-p1-wide-open,
    lau-nonconstant-pattern-open (mod-4 pair parity barrier)."
first-step: research: locate the precise statement of the Rubinstein–Sarnak
limiting measure and any result on its invariance or ergodicity under dilation by
2; and whether any source bounds a digital/fold statistic of the race from the
one-point race alone. tool_builder (measurement only): compute the empirical
log-density measure of S(n)/n for the primes up to the oracle ceiling, and test
its dilation-invariance (compare windows [X,2X] against [2X,4X]) against the RS
one-point measure — if the fold statistic is dilation-invariant in distribution,
the route is live; if it visibly depends on pair data, it is dead.
```
