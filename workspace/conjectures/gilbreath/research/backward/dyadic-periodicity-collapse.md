# Supply bound via the dyadic kernel — REFUTED (the converse is dead)

This skeleton decomposes the **single remaining open content of the whole
conjecture** — the supply lower bound `ν₂(q_n) ≥ c·n` (id
`SC-supply-nu2-linear`) — along the dyadic axis the thread
`research/threads/dyadic-periodicity-collapse.md` committed to. It is **broken**:
its load-bearing converse rung is refuted by a witness the run already holds, so
the decomposition does **not** move the supply bound. This file is kept as the
authoritative record of *why* the dyadic dichotomy is one-sided; the gap-level
detail lives in `research/backward/dyadic-dichotomy-refuted.md` (distinct `RZ-*`
gap ids).

```skeleton
goal: For the prime sequence, ν₂(q_n) ≥ c·n for an absolute c > 0 and all sufficiently large n, where ν₂(q_n) is the number of 2s in the maximal {0,2} suffix of the right diagonal δ(q_n). (This is SC-supply-nu2-linear; via the discharged runway/demand/equivalence legs it proves Gilbreath's conjecture.)
implies: |
  Let h ∈ {0,1}^ℕ be the mod-4 switch bit, h[j] = ((p_{j+2} − p_{j+1})/2) mod 2
  (so h[j]=1 ⟺ consecutive primes switch residue class mod 4), and Φ_n the
  Pascal-mod-2 fold over the fixed ancestor window [2, n−1].

  (0) LINEARIZATION [DPC-linearization, discharged]  ν₂(q_n) = wt(Φ_n h): the
      halved {0,2}-tail cell at depth d is the XOR of a binom(d,·)-window of h
      (rule90-interior-xor, proved), and the row-1 ancestor union of the tail
      cells is exactly the fixed interval [2, n−1] (verified; promotion of the
      interval fact is housekeeping).

  (1) DYADIC COLLAPSE [DPC-dyadic-collapse, discharged]  h eventually 2^k-periodic
      ⟹ wt(Φ_n h) = O_k(1). Prime-free and PROVED (dyadic-collapse-proved: sharp
      bound ν₂ ≤ N0 + 2^k, attained by the word 0…01). It explains both recorded
      killers of the universal transfer (consecutive odds, period 1; alternating
      2/4, period 2).

  (2) KERNEL CLASSIFICATION [DPC-kernel-classification, refuted]  the converse —
      wt(Φ_n h) sublinear ⟹ h within o(n) of a 2^k-periodic string — is FALSE on
      two independent balanced, dyadically-aperiodic witnesses: half-step strings
      h = 1^{m/2} 0^{m/2} give wt(Φ h) = 1 exactly (Directive 68,
      dyadic_halfstep_large.captured.txt), and Thue–Morse gives measured sublinear
      ν₂ (dyadic-separating-invariant-three-strings).

  (3) PRIME ANTI-DYADICITY [DPC-prime-antidyadic, open but vacuous]  the prime h
      is not asymptotically 2^k-periodic. This stays (likely) true, but without
      the refuted converse (2) it closes nothing toward GC.

  THE INFERENCE THAT DIED: (2)+(3) ⟹ supply. Since (2) is false, the dyadic
  dichotomy does not reduce the supply bound — aperiodicity of h is NOT
  sufficient for ν₂ ≥ c·n. This decomposition therefore implies nothing about
  the goal. The supply bound ν₂ ≥ c·n stands as the single honest residual of
  Route B (abgs-2011-s9-mod4-switch-limit-open).
status: broken
rests-on: rule90-interior-xor, dyadic-collapse-proved, transfer-matrix-kernel-allones, thue-morse-sublinear-supply-witness, thue-morse-subset-zeta-confirmed-identification-refuted, dyadic-separating-invariant-three-strings, gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, lemma54-re-derived-proof, lemma54-descent-lean-formalised-even, gap-bounds-cannot-force-block-growth, li2023-short-interval-052, li2023-not-bottleneck, verification-record-2026, abgs-2011-s9-mod4-switch-limit-open
killed-by: DPC-kernel-classification — the converse on which the inference rested is refuted by two independent balanced aperiodic witnesses with sublinear supply: half-step strings h = 1^{m/2} 0^{m/2} (wt(Φh)=1, dyadic_halfstep_large.captured.txt, Directive 68) and Thue–Morse (measured ν₂/n → 0, dyadic-separating-invariant-three-strings). Aperiodicity/anti-dyadicity does not force ν₂ ≥ c·n, so the dyadic dichotomy yields no supply bound.
```

```gap
id: DPC-linearization
lemma: ν₂(q_n) = wt(Φ_n h), where h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 and Φ_n is the F2 matrix with entries [C(k,j) mod 2] over tail rows k = K..n−2 and ancestor columns j = 2..n−1.
status: discharged
discharged-by: rule90-interior-xor (proved) composed with the ancestor-window interval fact (verified in the nu2_vs_gap_parity session; 0 violations at 8 sparse + 2951 dense samples, code/out/linearization_verify.captured.txt).
next: none — restating this as open re-opens a proved identification.
```

```gap
id: DPC-dyadic-collapse
lemma: If h is eventually periodic with period 2^k (k ≥ 0), then ν₂(q_n) = wt(Φ_n h) = O_k(1), with the sharp bound ν₂ ≤ N0 + 2^k (preperiod N0; attained by the word 0…01).
status: discharged
discharged-by: dyadic-collapse-proved (proved, prime-free; research/notes/dyadic-collapse-proof.md — submask-factorization via Lucas' theorem on the C(d,j) mod 2 kernel).
next: none — restating this as open re-opens a proved theorem.
```

```gap
id: DPC-kernel-classification
lemma: (Quantitative converse of the collapse.) The only way wt(Φ_n h) is sublinear is asymptotic dyadic periodicity: there is ε₀, k₀ such that wt(Φ_n h) < ε₀·n at some n forces h|[1,n] within o(n) Hamming distance of a 2^k-periodic string for some k ≤ k₀.
status: refuted
discharged-by: (refuted, not discharged) half-step strings h = 1^{m/2} 0^{m/2} give wt(Φ h) = 1 exactly (dyadic_halfstep_large.captured.txt, Directive 68); Thue–Morse h[j] = wt(j) mod 2 is aperiodic (exactly n/2 Hamming-far from every 2^k-periodic string) yet has measured sublinear ν₂ (dyadic-separating-invariant-three-strings). Both are balanced and dyadically aperiodic.
next: none — do not re-attack in this form. Any repair needs an extra hypothesis the collapse proof does not require, and without it the dichotomy yields no supply bound.
thread: research/threads/dyadic-periodicity-collapse.md
```

```gap
id: DPC-prime-antidyadic
lemma: The prime mod-4 switch bit h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 is not asymptotically periodic with period a power of 2 (quantitatively: for each k ≤ k₀, h|[1,n] stays ≥ δ_k·n Hamming-far from every 2^k-periodic string).
status: open
next: |
  NOTE: this lemma no longer closes anything toward GC — the inference that used it is refuted at
  the converse (DPC-kernel-classification). It is kept open only as a cheap, likely-provable prime
  statement. First move (tool_builder, low priority): compute the Hamming distance of h|[1,n] to
  the nearest 2^k-periodic string for k = 0..6, n up to 1e6 (sieve ≤ 1.6e7, O(n) memory), report
  distance/n. Expectation: distance/n stays near 0.4–0.6 (h is ~60% ones). Deprioritise behind
  CT-concentration and CT-suffix-length, which are the lemmas that actually move the goal.
thread: research/threads/dyadic-periodicity-collapse.md
```
