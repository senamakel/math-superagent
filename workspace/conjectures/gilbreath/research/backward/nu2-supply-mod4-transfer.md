# ν₂ supply side — what would prove the one open leg of Route B

This decomposes the single open content of Route B (Granville ν₂): the supply
lower bound `ν₂(q_n) ≥ c·n`. The existing `granville-nu2-reduction.md` skeleton
states this as one atomic gap (`GN-supply-nu2-density`); this file splits it
into the two rungs the board's rising-sea post already identified
(`nu2_vs_gap_parity`): a **transfer** (F2-linear, over already-proved Rule-90
structure) and a **mod-4 density** statement (the genuinely hard
number-theoretic core). Everything below the supply line — the `{0,2}`
reduction, the Granville runway (Lemma 5.4), and the Baker–Harman–Pintz demand
side — is discharged, so this file carries exactly two open gaps.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1, equivalently every finite prime prefix q_1..q_n is successful (bottom single entry of its difference triangle is 1).
implies: | Work in right-diagonal coordinates δ(q_n) = (δ_0,...,δ_{n-1}), δ_k = A_k(n-k), so δ_{n-1}(q_n) = A_{n-1}(0) and "q_1..q_n succeeds" ⟺ δ_{n-1}(q_n) = 1. Everything below the supply line is DISCHARGED: (a) {0,2} form: A_k(0)=1 ∀k ⟺ A_k(1)∈{0,2} ∀k (gilbreath-reduces-to-second-in-02, proved; Lean IFF gilbreath-second-entry-equivalence). (b) runway: q_1..q_{n-1} valid & successful ∧ g*_n ≤ 2ν₂(q_{n-1})+2 ⟹ q_1..q_n succeeds (lemma54-re-derived-proof, proved on the even domain — the δ=0 case is the absorption closure, not an exception; lemma54-sufficiency-survives-proper-domain, checked non-vacuously on synthetic failing sisters in both directions). (c) demand: g*_n = max(g_2..g_n) < n^{0.525+ε} for every ε>0 and all large n (Baker–Harman–Pintz 2001, p_{n+1}−p_n ≪ p_n^{0.525}; p_n ~ n log n absorbs the log — gap-bounds-cannot-force-block-growth, visser-large-gaps-survey). SUPPLY, the only open leg, splits into two gaps: S1 (transfer)  ν₂(q_n) ≥ w_n/2, where w_n is the Hamming weight of the halved-gap bit string h[m] = (gap_m / 2) mod 2 over the fixed ancestor interval [2, n−1] of A_1 (so h[m] = 1 ⟺ gap_m ≡ 2 mod 4). This says the halved {0,2}-tail bit vector of δ(q_n) — an F2-linear (Rule-90/XOR) image of h — has weight at least half the input weight. Empirically ν₂/w ∈ [0.689, 0.867], so the constant 2 is safe (board, code/gap_analysis/nu2_vs_gap_parity.py). S2 (density)   w_n ≥ c'·n for a fixed c' > 0 and all large n: the set of consecutive prime pairs with opposite residues mod 4 has positive lower density. COMBINE: ν₂(q_n) ≥ w_n/2 ≥ (c'/2)·n = c·n with c = c'/2 > 0. Any positive-linear bound dominates every sub-1 power (li2023-not-bottleneck), so for large n ν₂(q_{n-1}) ≥ (c'/2)(n−1) > n^{0.526} > n^{0.5255} > g*_n. The runway (b) then turns "q_1..q_{n-1} successful" into "q_1..q_n successful", and strong induction on n from any verified base past the (implicit) BHP/supply thresholds — the run's own depth-1000 record, or the literature's 10^13–10^15 (verification-record-2026) — gives every finite prefix successful, i.e. GC. The {0,2} form (a) is the equivalent left-edge statement.
killed-by: S1-nu2-transfer-weight (ν₂ ≥ w/2) is false universally: a 2-then-odds sequence with every gap ≡ 2 mod 4 (h = 1111…, weight w = n maximal) fails at row 3 with ν₂ = 0. The S1 fork lands on (b) prime-specific, which is its own stated 'not a reduction' case; the prime-specific ν₂ ≥ w/2 is measured (min 0.689) not proved, so S1+S2 adds a second unproved prime statement instead of removing one.
rests-on: gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, lemma54-re-derived-proof, lemma54-sufficiency-survives-proper-domain, gap-bounds-cannot-force-block-growth, li2023-not-bottleneck, verification-record-2026, rule90-interior-xor, edge-interior-invertibility-sharpened
status: broken
```

```gap
id: S1-nu2-transfer-weight
lemma: |
  For the prime right diagonal, ν₂(q_n) ≥ w_n/2, where w_n = #{m in [2, n−1] : gap_m ≡ 2 mod 4}
  is the Hamming weight of the halved-gap bit string h[m] = (gap_m / 2) mod 2. Invariantly:
  the halved {0,2}-tail bit vector of δ(q_n) is the image of h under an F2-linear map (a
  Rule-90/XOR window family fixed by the triangle geometry), and the output weight ν₂ is at
  least half the input weight w_n.
status: open
next: |
  DECIDE THE FORK FIRST — it determines whether this decomposition reduces anything.
  (a) UNIVERSAL: if ν₂ ≥ w/2 holds for ALL h ∈ {0,1}^{n−2}, then S1 is a combinatorial
      identity about the fixed Rule-90 window family and it discharges to pure F2 linear
      algebra; only S2 (density) then carries number-theoretic content.
  (b) PRIME-SPECIFIC: if ν₂ ≥ w/2 holds only for the prime bit string h, then S1 is itself
      a conjecture about the primes and S1+S2 does NOT reduce difficulty — it repackages
      S2 with a transfer that inherits S2's hardness. The skeleton is only a genuine
      decomposition in case (a).

  tool_builder (settles the fork, today): EXHAUST the invariant on all small bit strings —
  this is the falsification oracle, not a search of the answer space. For n = 4..18, generate
  every h ∈ {0,1}^{n−2}, build the {0,2}-tail window family exactly as
  code/gap_analysis/nu2_vs_gap_parity.py does, compute ν₂ and w, and check ν₂ ≥ w/2 with
  zero violations. The FIRST counterexample h refutes case (a) and moves S1 to case (b) —
  in which case this file's two-gap split is not a reduction and must be reported as broken
  (the honest negative result: the supply side has no combinatorial shortcut). O(N · 2^N),
  N ≤ 16, trivial; parallelise across n with code/lib/parallel.py.

  theorem_prover (only if the fork lands on (a)): prove weight(image) ≥ weight(h)/2 for the
  pinned-down window family. The run holds the ingredients — the halved-edge map is
  unitriangular hence invertible over F2 (edge-interior-invertibility-sharpened), the
  interior evolves by Rule 90 (rule90-interior-xor) — but unitriangularity alone does NOT
  force the weight bound (e.g. (h1,h2) ↦ (h1+h2, h2) sends (1,1) to (0,1), weight 2 → 1,
  exactly the w/2 boundary). Encode "∀h, weight(image) ≥ weight(h)/2" as a boolean/first-order
  statement and hand it to eprover or a SAT solver; a clean route is to exhibit, for each
  1-bit of h, a bounded set of tail cells (≤ 2) witnessing it.
thread: research/threads/regeneration.md
```

```gap
id: S2-mod4-gap-density
lemma: |
  #{m ≤ n : p_{m+1} − p_m ≡ 2 mod 4} ≥ c'·n for a fixed c' > 0 and all sufficiently large n.
  Equivalently: the set of consecutive prime pairs (p_m, p_{m+1}) with opposite residues mod 4
  has positive lower density. (Every such pair has gap ≡ 2 mod 4, since all prime gaps after
  2 are even.)
status: open
next: |
  STATUS (already settled by the held library — do NOT re-request research): positive lower
  density of gaps ≡ 2 mod 4 is at Hardy–Littlewood / GRH level, NOT unconditionally available.
  The held claims are decisive and unanimous:
    - shiu-2000-strings-of-congruent-primes: unconditional, but proves NON-switches
      (arbitrarily long same-residue runs) — the opposite of what is needed; no quantitative
      switch bound.
    - lau-2024-consecutive-residue-patterns-existence-only: no prescribed non-constant
      consecutive residue pattern is known to occur with positive frequency; counts distinct
      patterns, never a frequency bound.
    - maynard-2015-existence-not-frequency: existence, never frequency; Route B's supply
      needs Hardy–Littlewood/LOS input, still open.
    - rubinstein-sarnak-bias-oscillates-unconditional-false + rubinstein-sarnak-fluctuation-not-bias:
      the mod-4 race oscillates (Littlewood), so no one-sided unconditional density holds;
      the honest deliverable is a FLUCTUATION bound at GRH/LI + HL level, never a one-sided
      density assertion. ν₂ ≥ c·n "can only be a fluctuation bound".
    - los-2016-consecutive-pair-mod4-bias: the 1/4-per-pair main term for consecutive pairs
      is Hardy–Littlewood / GRH, not unconditional.
  CONCLUSION for this gap: a theorem_prover cannot prove S2 unconditionally from current
  knowledge. The realistic deliverable is one of:
    (i) a GRH/HL-CONDITIONAL theorem — "under the Hardy–Littlewood k-tuple conjecture (or
        GRH), w_n ≫ n, hence GC" — which is a genuine partial result: it reduces GC to one
        clean, named, well-studied conjecture; or
    (ii) an explicit statement that S2 is exactly the unproved mod-4 switch-density
        conjecture, recorded as such (the negative result: the atomic core of Route B's
        supply side is a prime-race frequency statement the literature does not reach).

  tool_builder (parallel, no literature needed): pin the target constant by computing w_n/n
  to the empirical ceiling — sieve to n = 10^5 or 10^6, one pass, O(n) — so the honest c'
  and the gap to n^{0.525} are numbers, not estimates. The board's measurement (w/n ≈ 0.60)
  is at n = 3999; extend it. This supports the conditional theorem's (i) by fixing the
  constant the GRH/HL model would have to certify.
thread: research/threads/regeneration.md
```
