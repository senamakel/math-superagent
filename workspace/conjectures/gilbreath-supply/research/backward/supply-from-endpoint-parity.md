# SUPPLY from endpoint-comparison arithmetic

Reduces SUPPLY to two things: an exact digital dictionary + run-telescoping
identity (pure F₂, cheap to verify), and one arithmetic statement about the
mod-4 residue sequence `r_j = q_j mod 4` at digitally-defined pairs. This is
GOAL.md priority 2 (result 4): a candidate input strictly weaker than adjacent
mod-4 switch density, and it makes the run's hypothesis precise — the fold `Φ`
reads residue comparisons at *non-adjacent*, binary-structured gaps, which the
switch-density form throws away.

```skeleton
goal: >
  SUPPLY — there exists c > 0 with ν₂(n) ≥ c·n for all sufficiently large n,
  for the prime sequence.

implies: >
  Notation: q_i the primes (q_1=2, q_2=3, …); r_j = q_j mod 4 ∈ {1,3} for
  j ≥ 2 (odd primes only, the even prime 2 is an O(1) edge); h[j] = [r_{j+1} ≠ r_j],
  so h[j] = ((q_{j+1} − q_j)/2) mod 2 is the linearisation string. For a window of
  length d+1 ending at position n−1, write the diagonal cell bit

      T(n,d) = ⊕_{o ∈ [0,d], o ⊆ d} h[n−1−d+o],      ⊆ = bitwise submask.

  G-dict gives ν₂(n) = #{d ∈ [2, n−1] : T(n,d) = 1} up to ±1.

  G-run decomposes each digital down-set ↓d = {o ∈ [0,d] : o ⊆ d} into its maximal
  runs (consecutive-integer intervals). By telescoping, a run R = [u,v] satisfies

      ⊕_{o ∈ R} h[n−1−d+o] = [ r_{n−1−d+u} ≢ r_{n−1−d+v+1} mod 4 ],

  hence T(n,d) = ⊕_{R ∈ runs(↓d)} [ r_{a_R} ≢ r_{b_R} mod 4 ] with
  a_R = n−1−d+u_R and b_R = n−1−d+v_R+1 (so a_R < b_R ≤ n and the comparison gap
  b_R − a_R is the run length, which is ≥ 2 for every odd d).

  G-arithmetic supplies an absolute c₀ > 0 with

      #{d ∈ [2, n−1] : T(n,d) = 1} ≥ c₀·n   for all large n.

  Combining: ν₂(n) ≥ c₀·n − O(1) ≥ (c₀/2)·n for all large n, so SUPPLY holds with
  c = c₀/2. Quantifiers: c₀ is absolute and independent of n; the ±1 and the
  suffix-floored-at-2 convention only shift the constant, never the linear rate.
  G-run + G-dict are pure F₂ and are the cheap part; G-arithmetic is the only
  number-theoretic input, and it is strictly weaker than adjacent switch density
  because it averages over digital run pairs rather than demanding a positive
  density of adjacent mod-4 switches.

status: sketched

rests-on: >
  problem.md "established" facts 1 (linearisation ν₂ = wt(Φ_n h)) and 2 (Lucas),
  which together give the dictionary in G-dict. These are asserted by problem.md
  as "imported as proved" but are NOT yet grounded in this workspace (CLAIMS.md is
  empty; no claim block, no oracle output). Grounding them is a task, not a proof
  gap, and the oracle must do it before the chain is relied on. Fact 3 (kernel) is
  not used in this chain beyond what facts 1–2 already give.
```

```gap
id: G-dict-windowed-zeta
lemma: >
  For the prime h defined above, ν₂(n) = #{d ∈ [2, n−1] : T(n,d) = 1} up to ±1,
  where T(n,d) = ⊕_{o ∈ [0,d], o ⊆ d} h[n−1−d+o]; equivalently ν₂(n) = wt(Φ_n h).
status: discharged
discharged-by: >
  problem.md facts 1–2 (linearisation + Lucas), asserted as proved. No claim id
  exists yet — CLAIMS.md is empty — so this is marked discharged on the strength of
  the imported facts only, and must be re-grounded by the oracle before any use.
next: >
  tool_builder: exact checker computing T(n,d) by brute submask-XOR and ν₂(n) by the
  streaming triangle; assert the identity for n ≤ 200 against the direct definition.
  lean_prover: formalise Lucas + the linearisation with #print axioms (no sorryAx).
```

```gap
id: G-run-telescope
lemma: >
  Every digital down-set ↓d = {o ∈ [0,d] : o ⊆ d} is a disjoint union of maximal
  runs of consecutive integers. With g = ν₂(d+1) (the number of trailing 1-bits of
  d, i.e. the position of d's lowest 0-bit), each run has length 2^g and there are
  2^{popcount(d)−g} of them; the runs are the blocks
  [m·2^g, (m+1)·2^g − 1] for the 2^{popcount(d)−g} top-bits choices m. For every
  run R = [u,v], the telescoping identity holds over any {0,1} sequence h:

      ⊕_{o ∈ R} h[n−1−d+o] = [ r_{n−1−d+u} ≢ r_{n−1−d+v+1} mod 4 ],

  where r is the boundary sequence of h (h[j] = [r_{j+1} ≠ r_j]). Consequently
  T(n,d) = ⊕_{R ∈ runs(↓d)} [ r_{a_R} ≢ r_{b_R} mod 4 ] with a_R < b_R and
  b_R − a_R = 2^{ν₂(d+1)}.
status: open
next: >
  tool_builder: enumerate runs(↓d) for d ≤ 2^14, check the run-length/count formula
  (2^{ν₂(d+1)} length, 2^{popcount(d)−ν₂(d+1)} count) and the telescoping identity
  against brute submask-XOR, on the real prime h and on random h as a control.
  pattern_finder: confirm the run-endpoint map (a_R, b_R) as a function of d's binary
  expansion. lean_prover: formalise the run decomposition as an F₂ identity holding
  for all {0,1} strings h — this is pure Boolean algebra, no number theory.
```

```gap
id: G-endpoint-comparison-density
lemma: >
  For r_j = q_j mod 4 ∈ {1,3} (odd primes), the digitally-defined endpoint
  comparisons [ r_{a_R} ≢ r_{b_R} mod 4 ] are balanced and sufficiently uncorrelated
  that #{d ∈ [2, n−1] : T(n,d) = 1} ≥ c₀·n for an absolute c₀ > 0 and all large n.
  This single statement is strictly weaker than adjacent switch density: for odd d
  the run length is ≥ 2, so it reads q_a vs q_b with b−a ≥ 2 (non-adjacent primes),
  and for even d it reads the parity of many adjacent switches at once rather than
  demanding any one switch occur.
status: open
next: >
  Attack in two halves. (a) Reduction to a character-sum/bias bound: with χ the
  non-trivial character mod 4, [r_a ≢ r_b] = 1 iff χ(r_a)χ(r_b) = −1, so
  (−1)^{T(n,d)} = ∏_{R} χ(r_{a_R}) χ(r_{b_R})  [corrected: no (−1)^{#runs(d)}
  prefactor — each run telescopes independently and XOR carries signs
  multiplicatively; the spurious form is false for every binary string at odd d,
  refuter_endpoint_sign.md, verified on 6868 (n,d) pairs n=20..120], and the
  density of T=1 is controlled by the bias S(n) = Σ_d (−1)^{T(n,d)} =
  Σ_d ∏_{R} χ(r_{a_R}) χ(r_{b_R}). The lemma is equivalent to |S(n)| ≤ (1−2c₀)n.
  (b) Concrete first computation: tool_builder computes S(n) and the empirical
  density of T(n,d)=1 for n up to the oracle ceiling, with a negative control
  (all-ones h ⇒ T = 0 almost everywhere, S(n) ≈ n) to confirm the signal is real.
  theorem_prover/research then prices the character sum over the binary-structured
  pairs (a_R, b_R): Dirichlet gives each χ(r_a)χ(r_b) mean ≈ 0 for random a,b; the
  open part is the correlation across the digital run pairs, which is where a
  second-moment/variance bound on q mod 4 over binary-structured intervals enters.
```

## Relation to the equivalence (result 5)

This skeleton proves result 4 (a weaker input suffices) if G-arithmetic can be
established. Its *falsifier* is exactly result 5: if no such c₀ exists because
the digital comparisons are as hard as adjacent switch density, then SUPPLY is
equivalent to SWITCH. See `supply-switch-equivalence.md`, whose single gap is the
contrapositive direction; refuting that gap is what sends the run back here.
