# Supply-side split: the one open statement of Route B, cut into two attackable lemmas

This refines the single open gap `GN-supply-nu2-density` in
`granville-nu2-reduction.md`. That gap asked for the monolithic bound
`ν₂(q_n) > n^β, β > 0.525`. Here the supply side is split into:

1. `G-supply-transfer` — a **combinatorial** statement, pure F₂ linear algebra
   on the already-proved Rule-90/XOR law (`rule90-interior-xor`), with no
   number theory in it: `ν₂(q_n) ≥ (2/3)·w(n)`, where `w(n)` is the Hamming
   weight of the halved-gap bit window.
2. `G-supply-mod4-frequency` — a **two-point prime input**: the frequency of
   prime gaps `≡ 2 (mod 4)` (equivalently, consecutive primes in different
   residue classes mod 4).

Together they give the linear supply bound and close Route B. Note what this
buys even if the second lemma stays open: the pair is a general-class theorem —
"any successful 2-then-odds sequence with `w(n) ≥ 2 n^{0.526}` is Gilbreath" —
which is exactly the GOAL.md deliverable shape, since it is a theorem about the
operator, not about primality.

```skeleton
goal: For the prime Gilbreath triangle, the count ν₂(q_n) of 2s in the maximal {0,2} suffix (0-2 cycle) of the right diagonal through q_n satisfies ν₂(q_n) > n^β with β = 0.526 for all sufficiently large n. This is the supply side of Granville's Theorem 5.5 reduction; its demand side is already unconditional, so this bound proves Gilbreath's conjecture.
implies: Induct on n over the right diagonals (the `implies` of granville-nu2-reduction). At the step extending the successful prefix q_1..q_{n-1} to q_n, Lemma 5.4 (DISCHARGED, lemma54-re-derived-proof) turns the budget g*_n ≤ 2·ν₂(q_{n-1}) + 2 into success of q_n. That budget holds because g*_n ≤ n^{0.525+ε} (DISCHARGED, GN-demand-record-gap-bhp, BHP) while ν₂(q_{n-1}) ≥ (2/3)·w(n−1) [G-supply-transfer] ≥ (2/3)·2(n−1)^{0.526} = (4/3)(n−1)^{0.526} > (n−1)^{0.526} [G-supply-mod4-frequency], so 2·ν₂(q_{n-1}) + 2 > 2(n−1)^{0.526} > n^{0.525+ε} for ε < 0.001 and n large (the exponent gap 0.526 > 0.525 is the whole point). Base case n = 2, 3 is direct. Hence every finite prime prefix is successful, and by gilbreath-reduces-to-second-in-02 this is Gilbreath's conjecture.
status: sketched
rests-on: gilbreath-reduces-to-second-in-02, lemma54-re-derived-proof, gap-bounds-cannot-force-block-growth, rule90-interior-xor
```

```gap
id: G-supply-transfer
lemma: For every successful 2-then-odds prefix q_1..q_n (q_1 = 2, q_2 = 3, q_j strictly increasing odd for j ≥ 3, all gaps even), let w(n) = #{ j ∈ [2, n−1] : q_{j+1} − q_j ≡ 2 (mod 4) } be the Hamming weight of the halved-gap bit window, and let ν₂(q_n) be the number of 2s in the maximal {0,2} suffix of the right diagonal δ(q_n) = (A_0(n), A_1(n−1), …, A_{n−1}(0)). Then ν₂(q_n) ≥ (2/3)·w(n).
status: REFUTED (closed) — see claim g-supply-transfer-universal-refuted, research/notes/g-supply-transfer-universal-refuted.md
closed-by: g-supply-transfer-universal-refuted
next: GONE — the universal transfer is false. Counterexample family: consecutive odds (all gaps=2) are successful for every n but the triangle collapses to (1,0,0,...) from row 2 on, so nu2 = 0 for every n>=4 while w = n-2 (maximal); hence nu2 < (2/3)w for all n>=4. Even the weaker nu2 >= w/2 is not a universal F2 identity (all-2 length-12 string: w=12, nu2=1). S1 fork resolves to case (b) prime-specific: the nu2 >= c*w supply decomposition cannot offload the mod-4 number-theoretic content onto a clean XOR/Rule-90 weight inequality. The primes still measure nu2/w in [0.689, 0.867] (g-supply-transfer-measured), so the supply statement survives for the primes; only the universal shortcut is dead. Route B's remaining content is the single named-open two-point mod-4 supply bound (abgs-2011-s9-mod4-switch-limit-open), conditional at HL/LOS level. Lemma 5.4 (budget 2*nu2+2) and the recharge identity are unaffected.
```

```gap
id: G-supply-mod4-frequency
lemma: For the primes, w(n) = #{ j ∈ [2, n−1] : p_{j+1} − p_j ≡ 2 (mod 4) } (equivalently: the number of consecutive-prime pairs p_j ≢ p_{j+1} (mod 4)) satisfies w(n) ≥ 2 n^{0.526} for all sufficiently large n.
status: open
next: STATUS HONESTY FIRST — this lemma is NOT attackable as an unconditional theorem. The library already carries the landscape: Shiu 2000 (claim shiu-2000-strings-of-congruent-primes) proves infinitely many NON-switches, arbitrarily long equal-residue runs — the wrong direction; Lau 2024 (claim lau-2024-consecutive-residue-patterns-existence-only) proves no unconditional frequency lower bound on a prescribed consecutive pattern; Maynard 2015 (claim maynard-2015-existence-not-frequency) is existence-only. So w(n) ≥ 2 n^{0.526} needs Hardy–Littlewood / Lemke-Oliver–Soundararajan level input, which is unproved. Two attackable moves remain, one for each role: (1) theorem_prover: prove the CONDITIONAL theorem "HL k-tuple conjecture ⟹ w(n) = n/2 + O(√(n log n))" (or the LOS pair-bias form n/2 + (n/2)(1/2 log x)·log(2π log x/q) + o(...), claim los-2016-consecutive-pair-mod4-bias) — this is a real corollary-level theorem, not open, and it pins exactly what the primes must satisfy. (2) tool_builder: extend code/gap_analysis/nu2_vs_gap_parity.py to compute w(n) exactly for n = 10^4, 10^5, 10^6 (sieve ≤ ~1.6·10^7, seconds, no full triangle) and report w(n)/n and the fluctuation w(n) − n/2. The measured w ≈ 0.6·n makes the needed 2 n^{0.526} ~200× looser than the truth at n = 10^6 (needed 2·(10^6)^{0.526} = 2·10^{3.156} ≈ 2,900; measured w ≈ 0.6·10^6 = 600,000; ratio ≈ 200×, not 10^5×). BECAUSE the unconditional bound is out of reach, the honest deliverable this skeleton produces is the general-class theorem: "any successful 2-then-odds sequence with w(n) ≥ 2 n^{0.526} is Gilbreath" (combinatorial transfer + Lemma 5.4, both prime-free), with the primes' satisfaction of the hypothesis the sole remaining open number-theoretic input — an exactly-stated partial result, not a claim of GC.
```
