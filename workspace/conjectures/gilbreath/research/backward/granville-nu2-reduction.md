# Proof skeleton: Granville's ν₂ reduction of Gilbreath to a density of 2s

```skeleton
goal: Gilbreath's conjecture — for the iterated absolute-difference triangle of the primes, A_k(0) = 1 for all k ≥ 1.
implies: |
  Work in right-diagonal coordinates (Granville's notation, re-derived here).
  Let p_n be the n-th prime, g_n = p_n − p_{n−1} (n ≥ 2) the gap, and
  g*_n = max(g_2,…,g_n) the record gap. Define the diagonal through p_n by
  δ_0(q_n) = p_n, δ_1(q_n) = g_n, δ_{k+1}(q_n) = |δ_k(q_n) − δ_k(q_{n−1})|.
  Then δ_k(q_n) = A_k(n−k), the usual triangle read along the diagonal, and
  the left edge is A_k(0) = δ_k(q_k). By the reduction (DISCHARGED,
  gilbreath-reduces-to-second-in-02) the conjecture is equivalent to
  "q_1..q_n succeeds for all n", where success means δ_k(q_k) = 1 for all
  1 ≤ k ≤ n.

  INDUCT on n. Base: q_1..q_{N_0} succeed — finitely many rows, computed
  exactly in the run's verification record (depth 1000 suffices; see
  granville-nu2-density-measured).

  Step: assume q_1..q_{n−1} succeed. The new diagonal δ(q_n) must be shown to
  reach the {0,2} regime and stay there (so δ_n(q_n) = 1). G-L54 (Lemma 5.4,
  re-derived with the δ=0 case as the main case) is the load-bearing
  induction step: it gives
        q_1..q_n succeed  provided  g*_n ≤ 2·ν_2(q_{n−1}) + 2,
  where ν_2(q_{n−1}) counts the 2s in the maximal {0,2} suffix of δ(q_{n−1}).

  Now close the budget:
    G-demand  (Baker–Harman–Pintz): for every ε > 0, g*_n < n^{0.525+ε} for
               all n ≥ N_0(ε). Fix any β > 0.525 and choose ε = (β−0.525)/2.
    G-supply: ν_2(q_{n−1}) > n^β for all n ≥ N_0.
  Then for n large, 2·ν_2(q_{n−1}) + 2 > 2 n^β + 2 ≥ n^{0.525+ε} > g*_n
  (the middle inequality because 2 n^β / n^{0.525+ε} = 2 n^{(β−0.525)/2} → ∞).
  So G-L54 applies and q_1..q_n succeeds. The induction closes for all n, and
  by the diagonal restatement of the reduction, A_k(0) = 1 for all k ≥ 1.

  The three gaps are exactly the three hypotheses consumed above. G-L54 is a
  finite, elementary statement about one diagonal (attackable today); G-demand
  is standard unconditional mathematics needing only a record-gap corollary;
  G-supply is the entire open content of the conjecture in this route — a
  lower bound on the density of 2s in the diagonal, empirically ν_2 ~ n/2
  (DISCHARGED as a measurement, granville-nu2-density-measured), far above the
  n^β threshold required.

status: sketched
rests-on: gilbreath-reduces-to-second-in-02, granville-nu2-density-measured, lemma54-discarded-case-universal, rule90-interior-xor, edge-interior-invertibility-sharpened, cht-normalized-gap-definition
```

```gap
id: G-L54
lemma: |
  Granville's Lemma 5.4, RE-DERIVED (the published proof discards the δ=0 case,
  which occurs in 100% of columns — lemma54-discarded-case-universal — so the
  lemma currently has no proof in this run's ledger). Statement: if q_1..q_{n−1}
  is valid and successful, and g*_n ≤ 2·ν_2(q_{n−1}) + 2, then q_1..q_n succeeds.
  Equivalently: along the new diagonal δ(q_n), starting from v_n = δ_{τ_n}(q_n)
  (the entry where the previous diagonal's maximal {0,2} suffix begins), the
  entry descends by 2 at each 2 of that suffix while it is ≥ 2, and once it hits
  0 it is ABSORBED — from then on |0 − {0,2}| ∈ {0,2} keeps the new diagonal in
  {0,2} forever, which is success. The descent budget 2·ν_2 therefore suffices to
  force v_n down to ≤ 2 provided v_n ≤ 2·ν_2 + 2, and v_n < g*_n ≤ 2·ν_2 + 2.
  The δ=0 "exception" is the absorption case and must be proved, not waved away.

  The exact claims to formalise, with δ_k = δ_k(q_n), ε_k = δ_k(q_{n−1}) in the
  suffix region (ε_k ∈ {0,2}):
    (i)  ε_k = 2 and δ_{k−1} ≥ 2  ⟹  δ_k = δ_{k−1} − 2        (descent, −2 per 2);
    (ii) δ_{k−1} = 0             ⟹  δ_k = ε_k ∈ {0,2}         (absorption: the
         discarded case; thereafter δ stays in {0,2} because ε stays in {0,2});
    (iii) ε_k = 2 and δ_{k−1} = 1 ⟹  δ_k = 1                  (bounce to ≤ 2);
  hence the potential δ_k + 2·(# of remaining 2s in the suffix after position k)
  never increases, and drops by 2 at each genuine descent.
status: open
next: |
  Two moves, both runnable today.
  (1) theorem_prover / lean_prover: formalise the three bullet cases (i)–(iii)
      plus the absorption invariant, and prove the resulting potential argument
      gives: if v_n ≤ 2·ν_2 + 2 then δ_k ∈ {0,2} eventually and stays. State the
      lemma for an abstract pair of diagonals (δ, ε) with ε ∈ {0,2} on a suffix
      and δ_{k+1} = |δ_k − ε_k|, so no prime-specific input is used.
  (2) tool_builder: VALIDATE THE FAILURE DIRECTION. The real primes never fail,
      so the biconditional cannot be tested on them (lemma54-discarded-case-universal
      flags this vacuity). Build synthetic failing sequences — Granville's own
      "closest failing sister" (his §5.1) and Poisson-gap sequences (his §4) — and
      check the contrapositive: whenever the budget g*_n > 2·ν_2 + 2, some such
      sequence does fail at q_n, and whenever the budget holds the repaired argument
      predicts success. A tool_builder task: code/gap_analysis/lemma54_failing_sisters.py.
```

```gap
id: G-demand
lemma: |
  The demand side is unconditional: for every ε > 0 there is N_0(ε) such that the
  record gap satisfies g*_n = max(g_2,…,g_n) < n^{0.525+ε} for all n ≥ N_0(ε).
  Source: Baker–Harman–Pintz (2001), p_{n+1} − p_n ≪ p_n^{0.525}. The corollary
  to the record gap is immediate from p_n ≍ n log n: each gap is O(p_n^{0.525}) =
  O((n log n)^{0.525}) = O(n^{0.525+ε}), and g*_n is a max over n gaps, so
  g*_n = O(n^{0.525+ε}). The finitely many n < N_0(ε) are absorbed into the
  induction base.

  This is a sourced standard theorem plus a one-line corollary; the gap in the
  ledger is that no claim block states the record-gap consequence, so the
  skeleton cannot yet cite it as discharged.
status: open
next: |
  librarian: fetch the exact Baker–Harman–Pintz statement (p_{n+1} − p_n ≪ p_n^{0.525})
  with a citable anchor. theorem_prover / symbolic_math: write the two-line
  derivation g*_n ≤ C p_n^{0.525} ≤ C′ (n log n)^{0.525} = O(n^{0.525+ε}) for every
  ε > 0, and record it as a claim `record-gap-bhp-0525` with `holds-here: yes`.
  This closes G-demand without new mathematics.
```

```gap
id: G-supply
lemma: |
  The supply side: there exists β > 0.525 and N_0 such that ν_2(q_n) > n^β for all
  n ≥ N_0, where ν_2(q_n) is the number of 2s in the maximal {0,2} suffix of the
  diagonal δ(q_n). This is the ENTIRE remaining content of the conjecture in this
  route. Empirically ν_2/n ∈ [0.42, 0.52] for n = 50..3999, i.e. ν_2 ~ n/2
  (DISCHARGED as a measurement, granville-nu2-density-measured) — 26× the threshold
  at n = 3999 — so the bound is far from tight, but no lower bound at all is proved.

  The structural handle: inside the {0,2} suffix, halving gives a {0,1} string and
  the diagonal entries are XOR (Rule 90 / Pascal mod 2) folds of the halved gap
  bits (DISCHARGED, rule90-interior-xor). The halved gap bit is (g/2) mod 2, i.e.
  whether the prime gap is ≡ 2 mod 4. The halved-edge map from an initial {0,2}
  block to the diagonal sequence is an F2-linear, unitriangular (hence invertible)
  map (DISCHARGED, edge-interior-invertibility-sharpened). Therefore ν_2 is a
  linear function of the gap-parity string, and a lower bound on ν_2 is a statement
  about the arrangement of prime gaps mod 4 — NOT about gap magnitude (consistent
  with gap-bounds-cannot-force-block-growth: upper bounds on gap size cannot force
  block growth, but the mod-4 arrangement is a different, non-concentration axis).

  This gap is the mirror of `CB-prime-exclusion` in counterexample-backward, which
  asserts XOR-non-degeneracy of the halved gaps; proving either is a partial result.
status: open
next: |
  (1) tool_builder — identify the exact transfer relation empirically. For each
      sampled column n in {50,100,200,400,800,1600,3200,3999} (reuse the machinery
      behind granville-nu2-density-measured), record ν_2(q_n), the ancestor window
      of halved gap bits, and that window's weight w(n). Report the empirical ratio
      ν_2/w and the smallest ν_2/n seen. This decides whether a clean transfer
      ν_2 ≥ w/c (small constant c) is plausible. A tool_builder task:
      code/gap_analysis/nu2_vs_gap_parity.py.
  (2) theorem_prover — prove the transfer. Using the unitriangularity in
      edge-interior-invertibility-sharpened, derive a lower bound on the number of
      1s in the diagonal suffix in terms of the number of 1s in the ancestor halved
      gap window (e.g. ν_2 ≥ w/2, or ν_2 ≥ w − c·(number of runs)). This reduces
      G-supply to a prime-gap-mod-4 density claim: every window of length Θ(n) of
      the gap-parity string contains ≥ n^β ones (gaps ≡ 2 mod 4 are not too sparse).
  (3) request_research — the density of prime gaps ≡ 2 mod 4 (or the maximal gap
      between such primes). What is known unconditionally about how often
      p_{n+1} − p_n ≡ 2 (mod 4)? This is the statement whose proof would close the
      gap via step (2). Falsifier for the transfer hypothesis: a window of halved
      gaps with many 1s whose diagonal suffix has few 1s (would refute ν_2 ≥ w/c).
```

# Ledger note

This is the third skeleton and the only one that matches the run's primary
theoretical route (Route B, Granville ν₂, per GOAL.md / CONTEXT.md). It leaves
three gaps: G-L54 (a proof of Lemma 5.4 — elementary, attackable now), G-demand
(a sourced corollary — near-discharged), and G-supply (the whole conjecture in
this route). G-L54 is the first to attack: it is finite, elementary, and the
skeleton is dead without it regardless of the other two.
