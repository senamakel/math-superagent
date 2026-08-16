# Grounding check: the three proposed routes (research pass)

Research verdict on the three approach blocks the inventor proposed for SUPPLY.
All three named real mathematics; none, on the evidence, gives a distinct engine
for SUPPLY. Each is refuted (with a specific defect), not merely found-missing.
This note records what was real, what the decisive object was, and what killed
each.

## Common context (what "real" means here)

SUPPLY: ν₂(n) = wt(Φ_n h) ≥ c·n for a fixed c>0, h the prime gap-parity string,
Φ_n the Pascal-mod-2 (Rule-90) fold with the run-telescope structure
(claim g-run-telescope-verified). The parity barrier (research/CLAIMS.md
abgs-p1-wide-open, lau-nonconstant-pattern-open) is the named open input: a
positive fraction of consecutive prime pairs differing mod 4, which
Ash–Beltis–Gross–Sinnott §9 say "cannot be treated using L-functions".

## Candidate 1: dyadic-renormalization-selfsimilar — REFUTED

- **Reformulation name:** renormalization-group / fixed-point identity from the
  run structure of the digital down-set ↓d.
- **What is real:** the exact identity S(n) = Σ_g Fold(τ_g)(window) is already
  established in-house (claim g-run-telescope-verified): the down-set ↓d
  partitions into 2^{pc(d)−g} runs of length 2^g, the fold telescopes over a run
  to the distance-2^g switch τ_g(j)=[q_j≠q_{j+2^g} mod 4]. So the "added value"
  is not the identity.
- **Decisive defect:** it is a renormalization in NAME only. Each scale-g stratum
  S_g(n) is the fold of τ_g at the ORIGINAL resolution (τ_g read at separation
  2^g but the same index positions), not a coarser copy of itself, so there is no
  RG operator mapping scale g to g+1 and no fixed-point equation to bootstrap.
  "Average over g of Fold(τ_g)" is therefore an average of different objects, not
  a self-similarity dividend. And the weakest input that makes any single τ_g's
  fold large is the switch correlation at separation 2^g, which at g=0 is the
  adjacent switch correlation — the parity barrier. So the "weaker than g=0"
  hope reduces to the barrier.
- **What it would have bought:** a bootstrap circumventing pointwise control of
  any τ_g. Not achieved, and no literature supplies an RG fixed point on the
  anti-diagonal slice (the only rule-90/Pascal self-similarity is on blocks/rows,
  pascal-cascade refutation).
- **Sources:** in-house claim g-run-telescope-verified; pascal-cascade-block-
  recursion refutation; Edlund–Nilsson Jacobi 10.1007/s10955-010-9974-z
  (RG on probabilistic CA, unrelated fixed points).

## Candidate 2: prime-race-variance-large-sieve — REFUTED

- **Reformulation name:** Hájek/Hoeffding U-statistic decomposition + Barban–
  Davenport–Halberstam / large sieve, intended in the index domain.
- **What is real:** the named machinery (Höeffding 1948; Bloznelis–Götze
  10.1214/aos/1009210694; BDH Vaughan 10.1215/s0012-7094-03-12026-8, Fiorilli
  arXiv:1301.5663) is classical and citable; the mod-4 prime race is a real
  named object (Littlewood, Knapowski–Turán, Rubinstein–Sarnak, Granville–Martin
  on disk, Fiorilli).
- **Decisive defect:** BDH and its refinements are VALUE-domain quantities: they
  bound Σ_{q≤Q}Σ_{(a,q)=1}(ψ(x;q,a)−x/φ(q))² = O(x log Q), averaged over moduli.
  The objects here — two-point products χ(q_j)χ(q_{j+2^g}) at prime-INDEX
  separation — are not a value-modulus quantity; no source bounds them (this
  restates the refuted dispersion route's finding: q_{j+2^g} ≠ q_j + constant).
  Naively Σ_{J≤X}W(J)² is diagonal-dominated ≈ X²/log X, so it is NOT the small
  quantity the route needs; improvement needs cancellation in
  Σ_{j<k}χ(q_j)χ(q_k)(X−k), i.e. exactly the two-point switch correlation, whose
  g=0 stratum is the parity barrier.
- **What it would have bought:** a strictly weaker arithmetic input than switch
  density. Not achieved.
- **Sources:** Vaughan 10.1215/s0012-7094-03-12026-8; Fiorilli arXiv:1301.5663;
  Bloznelis–Götze 10.1214/aos/1009210694; parity-barrier claims abgs-p1-wide-
  open, lau-nonconstant-pattern-open.

## Candidate 3: walsh-discrepancy-erdos-turan — REFUTED

- **Reformulation name:** Erdős–Turán–Koksma inequality for the Walsh/Vilenkin
  system (L^∞ discrepancy of the prime race).
- **What is real:** the ETK-Walsh/Vilenkin machinery is real (Hellekalek
  10.4064/aa-67-3-209-218; Hellekalek 10.1007/bf01470062; Petrova
  10.2478/udt-2021-0004; Dick–Pillichshammer; the (t,m,s)-net corpus).
- **Decisive defect 1 (fatal, scale):** the route needs Σ_ω|ŝ(ω)| = O(N^{1−ε})
  with ŝ(ω)=Σ_{j≤N}χ(q_j)(−1)^{⟨ω,j⟩}. Parseval over the digital group gives
  Σ_ω|ŝ(ω)|² = N; by Cauchy–Schwarz the L¹ norm is minimized by the uniform
  spread and is ≳ N·√N ≫ N. The target O(N^{1−ε}) is impossible for ANY ±1
  sequence — it is a scale error, not a cancellation hypothesis.
- **Decisive defect 2 (direction):** ETK bounds discrepancy (order N·D_N) by a
  coefficient sum; S(n) is a signed sum of the signs of the window's Walsh
  coefficients. The inequality runs discrepancy ≤ coefficients, the WRONG
  direction to lower-bound |S| from small coefficients. It is not a discrepancy
  statement of the needed form.
- **Decisive defect 3 (unprecedented object):** ŝ constrains the binary digits
  of the prime INDEX j, with character values at the prime VALUE. The
  digit-constrained prime-sum literature (Banks–Conflitti–Shparlinski; digit-sum
  of primes; Bohr-set character sums, Hanson 10.4153/cmb-2015-036-2) constrains
  digits of the VALUE p, never the running index. No source computes this sum.
- **What it would have bought:** a linear-in-s single-point character sum input.
  Not achievable; the honest parked form is the open weak-input request
  walsh-spectral-subset-b904.
- **Sources:** Hellekalek 10.4064/aa-67-3-209-218; Hanson 10.4153/cmb-2015-036-2;
  Tezuka 10.1145/31846.31848 (Walsh-spectral tests); walsh-spectral-subset-b904.

## Bottom line

All three are `refuted` in research/APPROACHES.md with killed-by lines and
precedent URLs. Each failed on a specific, citable ground rather than on absence
of a search. The honest positive content of all three is already housed in the
adopted routes: the exact S(n)=Σ_g Fold(τ_g) identity (candidate 1) is a lemma
of dyadic-gap-character-correlation; the second moment (candidate 2) is the
objective of fold-second-moment-krawtchouk; the Walsh-spectral weak-input request
(candidate 3) stays open as walsh-spectral-subset-b904.
