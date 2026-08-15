# Granville ν₂ reduction — what would prove Gilbreath via Route B

This is the backward decomposition of the run's declared primary route
(`research/threads/regeneration.md`, Route B). It complements the two existing
skeletons: `counterexample-backward.md` (minimal-counterexample geometry) and
`event-rate-sufficiency.md` (the run's own recharge/event accounting). All three
are decompositions of the same goal; this one is the sourced reduction of
Granville 2026 (arXiv:2607.04166, §5), read in full at
`research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md`.

The reduction is genuine: **two** of the four load-bearing statements are
already established (the `{0,2}` reduction and the prime-gap demand side), one
(Granville's Lemma 5.4) has a complete proof sketch whose only missing piece is
machine-checking a three-line budget, and one (the ν₂ density lower bound) is
the entire open content.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1, equivalently every finite prime prefix q_1..q_n (n ≥ 2) is "successful" (the bottom single entry of its difference triangle is 1).
implies: |
  Work on the right diagonal δ(q_n) = (δ_0, ..., δ_{n-1}), δ_k(q_n) = A_k(n-k) (1-based),
  so δ_{n-1}(q_n) = A_{n-1}(0) is the bottom single entry of the finite triangle of q_1..q_n,
  and "q_1..q_n succeeds" ⟺ δ_{n-1}(q_n) = 1.

  (1) DEMAND  [GN-demand-record-gap-bhp, DISCHARGED]  For every ε > 0 and all large n the
      record gap g*_n = max(g_2, ..., g_n) satisfies g*_n < n^{0.525+ε}
      (Baker–Harman–Pintz 2001 gives p_{n+1} − p_n ≪ p_n^{0.525}; p_n ~ n log n absorbs the log factor).

  (2) RUNWAY  [GN-lemma54-runway, OPEN]  If q_1..q_{n-1} is valid and successful and
      g*_n ≤ 2·ν₂(q_{n-1}) + 2, then q_1..q_n succeeds. The load-bearing step is the exact budget:
      the gray-block entry evolves v → |v − t| over the 0-2 cycle entries t ∈ {0,2}; t=0 is a no-op
      and t=2 is the map (0↦2, 2↦0, 2m↦2(m−1)) on evens, so after ν₂ two-steps the final entry lies
      in {0,2} ⟺ v_n ≤ 2ν₂ + 2; and v_n ≤ g*_n (Granville Lemma 5.3(8) for τ_n ≥ 2; v_n = g_n ≤ g*_n for τ_n = 1).

  (3) SUPPLY  [GN-supply-nu2-density, OPEN]  ν₂(q_{n-1}) > n^{0.526} for all large n
      (any fixed β > 0.525 works).

  COMBINE:  choose ε = 0.0005. For n large, g*_n < n^{0.5255} < n^{0.526} < ν₂(q_{n-1}) ≤ 2ν₂(q_{n-1}) + 2,
  so Lemma 5.4 turns "q_1..q_{n-1} successful" into "q_1..q_n successful". Strong induction on n
  from a verified base past the (implicit, so to-be-checked) BHP/supply thresholds — the run's own
  depth 1000, or the literature's 10^13–10^15 — gives every finite prefix successful, i.e. A_k(0) = 1
  for all k ≥ 1. The discharged reduction gilbreath-reduces-to-second-in-02 supplies the equivalent
  {0,2} second-entry form; the Lean IFF gilbreath-second-entry-equivalence certifies the equivalence.
status: sketched
rests-on: gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, step-law-theorem-proved, verification-record-2026
```

```gap
id: GN-demand-record-gap-bhp
lemma: For the primes, the record gap g*_n = max_{2≤k≤n}(p_k − p_{k−1}) satisfies g*_n < n^{0.525+ε} for every ε > 0 and all n ≥ n₀(ε).
status: discharged
discharged-by: sourced — Baker–Harman–Pintz 2001 (p_{n+1} − p_n ≪ p_n^{0.525}), referenced in claim gap-bounds-cannot-force-block-growth (research/notes/block-growth-literature.md). Not re-derived here; the only non-trivial step (absorbing p_n ~ n log n into the exponent) is elementary.
next: —
```

```gap
id: GN-lemma54-runway
lemma: (Granville Lemma 5.4, re-derived) Let q_1..q_{n-1} be valid (strictly increasing odd terms after q_2 = 3) and successful, with 0-2 cycle (maximal {0,2} suffix of δ(q_{n-1}) before the final 1) having ν₂ = #{t = 2}. If the record gap g*_n = max(g_2..g_n) satisfies g*_n ≤ 2ν₂ + 2, then q_1..q_n succeeds. Equivalent exact form: success at q_n ⟺ v_n ≤ 2ν₂ + 2, where v_n = δ_{τ_n}(q_n) is the first gray-block entry.
status: open
next: |
  The published proof is broken at exactly the δ = 0 case (claim lemma54-discarded-case-universal:
  the "exception" occurs in 100% of rows), but the repair is that δ = 0 is a no-op, not an exception.
  A complete three-line proof is ready to be formalised and machine-checked:

    1. The gray block is v_{τ_n} = v_n and v_k = |v_{k−1} − t_{k−1}| over the 0-2 cycle entries t ∈ {0,2}.
       t = 0 is the identity; t = 2 is the map (0 ↦ 2, 2 ↦ 0, 2m ↦ 2(m−1) for m ≥ 2) on even integers.
    2. Hence 0-entries drop out (no-ops), and only the count ν₂ of 2s matters: after ν₂ two-steps the
       value is in {0,2} ⟺ v_n ≤ 2ν₂ + 2 (boundary v_n = 2ν₂ + 2 lands on 2; v_n < 2ν₂+2 oscillates in {0,2}).
    3. By Granville Lemma 5.3(8), v_n = δ_{τ_n}(q_n) ≤ g*_n − 2 when τ_n ≥ 2, and v_n = δ_1(q_n) = g_n ≤ g*_n
       when τ_n = 1 (the yellow value is then the new gap itself). Either way g*_n ≤ 2ν₂ + 2 forces
       v_n ≤ 2ν₂ + 2, so by step 2 the last gray-block entry e_{n-2} lies in {0,2}; then
       δ_{n-1}(q_n) = |e_{n-2} − d_{n-2}| = |e_{n-2} − 1| = 1, since d_{n-2} = 1 is the successful
       bottom entry of δ(q_{n-1}).

  theorem_prover / lean_prover task: formalise this budget against the existing
  code/lean/gilbreath_reduction.lean (Step operator), report #print axioms and zero sorry.
  sat_solver / tool_builder check first: run the iff in BOTH directions on sequences that actually fail —
  Granville's length-11 corridor failure (2,3,5,9,11,13,15,17,25,27,29), Colonna's delete-5 example, and
  Poisson-gap failing sisters — confirming the hypothesis g*_n ≤ 2ν₂+2 fails exactly when they fail.
  (lemma54_iff_check could not exercise the failing direction on primes, which all succeed.)
thread: research/threads/regeneration.md
```

```gap
id: GN-supply-nu2-density
lemma: For the prime sequence, the count ν₂(q_n) of 2s in the 0-2 cycle of the right diagonal satisfies ν₂(q_n) > n^β for some fixed β > 0.525 (e.g. β = 0.526), for all sufficiently large n.
status: open
next: |
  This is the entire open content of Route B; everything else in the skeleton is discharged or has a
  complete proof sketch. Two first moves, one computational and one theoretical:

  tool_builder: compute ν₂ incrementally — each new diagonal δ(q_n) is one length-n vector operation from
  δ(q_{n-1}), total O(N²) abs-diffs and O(N) memory (a 1D computation, far below the 8 GiB / empirical
  ceiling, unlike the full triangle). Run to n = 10^5 or 10^6; record ν₂, ν₂/n, and the signed fluctuation
  ν₂ − n/2 with its running max |ν₂ − n/2|. This decides the honest proof target: if ν₂ = n/2 + O(√(n log n)),
  the target is a variance bound on XOR-folds; if the fluctuation grows faster, only ν₂ > n^{0.526} is realistic.

  theorem_prover: inside the 0-2 cycle the halved entries evolve by the proved Rule-90/XOR law
  (claim rule90-interior-xor), so ν₂ counts the 1s of a Rule-90 descendant of the halved-gap bit string
  (prime gap ≡ 0 mod 4 ↔ halved bit 1). Reduce ν₂ ≳ n^{1/2+ε} to a non-concentration condition on that bit
  string — the same 2-separation / no-long-{0,d}-block dichotomy as CHT Theorem 1.6, whose obstruction family
  the run already scanned as absent (claim cht-right-half-0d-scan-6e8). First concrete theorem: the random
  analogue — for i.i.d. unbiased halved bits, ν₂ = n/2 + O(√(n log n)) with high probability (an Azuma/variance
  bound over XOR-folds) — then state the deterministic non-concentration hypothesis on halved prime gaps that
  lifts it.

  Empirical anchor: ν₂/n ≈ 0.42–0.52 measured to n = 3999 (claim granville-nu2-density-measured), already a
  factor ~26 above the n^{0.525} threshold — the needed bound is far from tight.
thread: research/threads/regeneration.md
```
