# S(n) is the 2-adic discrepancy of the prime-race sequence — an Erdős–Turán–Koksma (L^∞) route

```approach
idea: >
  Bound S(n) = Σ_d (−1)^{T(n,d)} by the DISCREPANCY (uniform-distribution error)
  of the prime-race sequence s_j = χ(q_j) = (−1/q_j) over the 2-adic
  (Walsh/Vilenkin) group, via the Erdős–Turán–Koksma inequality for the Walsh
  system. This gives ν₂(n) ≥ n/2 − (discrepancy term), and the discrepancy is
  priced in terms of Walsh-modulated character sums
  Σ_{j≤N} χ(q_j)(−1)^{⟨ω,j⟩} along the prime index — an L^∞ (sup-norm) route,
  the dual of the second-moment route.

mechanism: >
  ε_d = (−1)^{T(n,d)} is the sign of the d-th zeta/Walsh coefficient of the
  window, so S(n) = Σ_d ε_d is a weighted sum of Walsh-exponentiated
  coefficients and is governed by how uniformly the residue sequence s (and
  hence the window h) is distributed over the digital group {0,1}^m. The
  Erdős–Turán–Koksma inequality for the Vilenkin/Walsh system (the digital
  counterpart of the classical E–T–K bound; developed in the theory of
  (t,m,s)-nets and digital sequences, e.g. Dick–Pillichshammer) bounds the
  discrepancy of a sequence by a finite sum of its Walsh coefficients. Applying
  it with the sequence s_j = χ(q_j) indexed by the digital group converts the
  bound on S(n) into a bound on Walsh coefficients of s. Each coefficient is

      ŝ(ω) = Σ_{j≤N} χ(q_j) (−1)^{⟨ω,j⟩},

  the nontrivial character mod 4 evaluated at primes whose INDEX lies in a
  prescribed binary-digit pattern — a character sum at primes along a digital
  subsequence. This is the new named object, and it is an L^∞ statement (max
  over ω), distinct from the L² variance route. Low-ω coefficients (few digit
  constraints) are provable from Siegel–Walfisz; high-ω coefficients require a
  new digital form of the Pólya–Vinogradov / Vinogradov bound along the prime
  index. Speculative half, to be priced: whether Σ_ω |ŝ(ω)| = O(N^{1−ε}) holds,
  which is exactly what makes the discrepancy bound non-vacuous. No value-shift
  of χ appears (the modulation is in the INDEX), so the refuted dispersion
  route's obstruction does not arise.

first-step: >
  tool_builder: (1) compute the Walsh coefficients Σ_{j≤N} χ(q_j)(−1)^{⟨ω,j⟩}
  for the real primes up to the oracle ceiling, print max over ω and its scaling
  in N; (2) verify the Erdős–Turán–Koksma-type bound numerically — check that
  |S(n)| ≤ (a finite Walsh coefficient sum of s) for n ≤ 200; (3) run negative
  controls: all-ones h (⇒ S(n) = n−2 large, discrepancy maximal) and Thue–Morse
  (⇒ decay) to confirm the discrepancy reading separates them. Falsifier: if the
  max Walsh coefficient of s_j scales like N (no cancellation), the discrepancy
  bound is vacuous and the route dies with the reason recorded.
status: refuted
killed-by: >
  The speculative half that makes the route non-vacuous is impossible as
  stated, and the discrepancy reading does not reach S(n) in the direction
  needed. Three independent defects.
  (1) Parseval kills the input. The route needs Σ_ω |ŝ(ω)| = O(N^{1−ε}) with
  ŝ(ω)=Σ_{j≤N}χ(q_j)(−1)^{⟨ω,j⟩}. But Parseval over the digital group gives
  Σ_ω |ŝ(ω)|² = Σ_j |χ(q_j)|² = N (exactly, since |s_j|=1 for all N terms).
  For any length-N ±1 sequence, by Cauchy–Schwarz Σ_ω|ŝ(ω)| ≥ (Σ|ŝ|²)/√(2^m) ≈
  N/√N = √N among the full character group, and — more importantly — the L¹
  norm of a Walsh spectrum is minimized when the mass spreads uniformly, giving
  Σ_ω|ŝ(ω)| ≳ N·√N, which is ≫ N, not O(N^{1−ε}). So the target
  "Σ_ω|ŝ(ω)|=O(N^{1−ε})" cannot hold for any ±1 sequence, real primes or not;
  it is not a hypothesis about cancellation in χ, it is a scale error about the
  size of a Walsh-L1 norm. (2) S(n) is not a point-set discrepancy in the
  direction ETK bounds. The Erdős–Turán–Koksma-class inequalities (real:
  Hellekalek 10.4064/aa-67-3-209-218, Walsh function system; Dick–Pillichshammer,
  Vilenkin digital nets) bound the DISCREPANCY (counting-function minus volume,
  a quantity of order N·D_N) by a finite sum of trigonometric/Walsh coefficients.
  S(n) = Σ_d (−1)^{T(n,d)} is the signed sum of the SIGN OF the zeta/Walsh
  coefficients of the window, i.e. an L^∞-weighted sum of Walsh-exponentiated
  values; it is not the point-set discrepancy of s_j over the digital group, and
  no ETK-type inequality lower-bounds an arbitrary sign-sum of this shape from
  an upper bound on |S| — the inequality runs the other way (discrepancy ≤
  coefficients). The direction needed for SUPPLY (small coefficients imply small
  S) is not a discrepancy statement at all. (3) The needed Walsh sum is
  unprecedented. ŝ(ω) constrains the binary digits of the prime INDEX j with a
  character value χ(q_j) at the prime VALUE; the digit-constrained prime-sum
  literature (Banks–Conflitti–Shparlinski, digit-sums of primes; digit-pattern
  sums, "Primes with an average sum of digits"; character sums over Bohr sets,
  Hanson 10.4153/cmb-2015-036-2) constrains digits of the prime VALUE p, never
  the running index of the prime sequence. No source evaluates χ at primes whose
  INDEX lies in a binary-digit pattern, so the non-vacuousness of the bound is
  not an input anyone has computed or bounded. Refuted as a standalone route;
  its honest content (the weak-input request for a Walsh-spectral bound on h
  along binary-submask sets, request walsh-spectral-subset-b904) is already
  parked.
precedent: >
  The ETK-Walsh/Vilenkin machinery is real: Hellekalek, "General discrepancy
  estimates: the Walsh function system", Acta Arith. 67 (1994) 209–218,
  doi 10.4064/aa-67-3-209-218; Hellekalek, "General discrepancy estimates III:
  the ETK inequality for the Haar function system", 10.1007/bf01470062;
  Petrova 10.2478/udt-2021-0004 (ETK in Vilenkin/Cantor bases); the digital
  (t,m,s)-net / low-discrepancy corpus (Dick–Pillichshammer; Faure–Kritzer–
  Pillichshammer 10.1016/j.indag.2015.09.001; Niederreiter). The direction all
  of it supports is discrepancy ≤ coefficient-sum, not a lower bound on a signed
  sum of coefficient-signs. Walsh-spectral tests of pseudorandomness (Tezuka
  10.1145/31846.31848) use orthogonality the same way. Character sums over
  digit-constrained integers: Banks–Conflitti–Shparlinski, "Character sums over
  integers with restricted g-ary digits"; character sums over Bohr sets, Hanson
  10.4153/cmb-2015-036-2 — none over the prime INDEX. Inside-workspace: the
  Walsh/Fourier identity wt(Φ_n h)=(n−2)/2−(1/2)Σ_d(−1)^{T(n,d)} is exact and
  adopted (fold-second-moment-krawtchouk); request walsh-spectral-subset-b904
  stays open as the honest parked form of this idea.
```

## Distinctness (not a restatement)

- Not `walsh-subset-sum-fold-structure` (refuted): that route sought a bound on wt(Φ_n x) from Φ alone, valid for all x, and died on the kernel vectors; this route bounds S(n) through the discrepancy of the ARITHMETIC sequence s_j = χ(q_j), an input about the primes, not a property of Φ.
- Not `fold-second-moment-krawtchouk` (adopted, L²): this is the L^∞ dual — sup-norm discrepancy of the race rather than second moment of the fold.
- Not `dyadic-gap-character-correlation` (adopted): that route prices two-point products χ(q_j)χ(q_{j+2^g}); this route prices single-point character sums with a Walsh index-modulation, a different (linear in s) object.
