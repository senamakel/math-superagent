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
rests-on: gilbreath-reduces-to-second-in-02, lemma54-re-derived-proof, GN-demand-record-gap-bhp, rule90-interior-xor
```

```gap
id: G-supply-transfer
lemma: For every successful 2-then-odds prefix q_1..q_n (q_1 = 2, q_2 = 3, q_j strictly increasing odd for j ≥ 3, all gaps even), let w(n) = #{ j ∈ [2, n−1] : q_{j+1} − q_j ≡ 2 (mod 4) } be the Hamming weight of the halved-gap bit window, and let ν₂(q_n) be the number of 2s in the maximal {0,2} suffix of the right diagonal δ(q_n) = (A_0(n), A_1(n−1), …, A_{n−1}(0)). Then ν₂(q_n) ≥ (2/3)·w(n).
status: open
next: The halved entries of the 0-2 cycle are an explicit F₂-linear image of the halved-gap bit vector h_j = (g_j/2) mod 2 via the proved XOR law (rule90-interior-xor): the tail cells (k, n−k) of δ(q_n) have A_1-ancestor windows whose union is the fixed interval [2, n−1] (derived in code/gap_analysis/nu2_vs_gap_parity.py). First move: write down M_n, the F₂ matrix with wt(M_n h) = ν₂(q_n). tool_builder: exhaustively compute the exact worst-case ratio min_{h≠0} wt(M_n h)/wt(h) for n ≤ 20 (2^{n−2} ≤ 2^{18} vectors, trivial) and check it against the measured ν₂/w ∈ [0.689, 0.867] on the real rows (code/out/witnesses.json); theorem_prover: prove wt(M_n h) ≥ (2/3) wt(h) from the structure of M_n — the union-of-windows fact says every input bit lands in ≥ 1 tail coordinate, and the target 2/3 is a covering / double-counting statement. If the true ratio is below 2/3, raise the constant C in G-supply-mod4-frequency to keep the product (ratio)·C > 1.
```

```gap
id: G-supply-mod4-frequency
lemma: For the primes, w(n) = #{ j ∈ [2, n−1] : p_{j+1} − p_j ≡ 2 (mod 4) } (equivalently: the number of consecutive-prime pairs p_j ≢ p_{j+1} (mod 4)) satisfies w(n) ≥ 2 n^{0.526} for all sufficiently large n.
status: open
next: STATUS HONESTY FIRST — this lemma is NOT attackable as an unconditional theorem. The library already carries the landscape: Shiu 2000 (claim shiu-2000-strings-of-congruent-primes) proves infinitely many NON-switches, arbitrarily long equal-residue runs — the wrong direction; Lau 2024 (claim lau-2024-consecutive-residue-patterns-existence-only) proves no unconditional frequency lower bound on a prescribed consecutive pattern; Maynard 2015 (claim maynard-2015-existence-not-frequency) is existence-only. So w(n) ≥ 2 n^{0.526} needs Hardy–Littlewood / Lemke-Oliver–Soundararajan level input, which is unproved. Two attackable moves remain, one for each role: (1) theorem_prover: prove the CONDITIONAL theorem "HL k-tuple conjecture ⟹ w(n) = n/2 + O(√(n log n))" (or the LOS pair-bias form n/2 + (n/2)(1/2 log x)·log(2π log x/q) + o(...), claim los-2016-consecutive-pair-mod4-bias) — this is a real corollary-level theorem, not open, and it pins exactly what the primes must satisfy. (2) tool_builder: extend code/gap_analysis/nu2_vs_gap_parity.py to compute w(n) exactly for n = 10^4, 10^5, 10^6 (sieve ≤ ~1.6·10^7, seconds, no full triangle) and report w(n)/n and the fluctuation w(n) − n/2. The measured w ≈ 0.6·n makes the needed 2 n^{0.526} ~10^5× looser than the truth at n = 10^6. BECAUSE the unconditional bound is out of reach, the honest deliverable this skeleton produces is the general-class theorem: "any successful 2-then-odds sequence with w(n) ≥ 2 n^{0.526} is Gilbreath" (combinatorial transfer + Lemma 5.4, both prime-free), with the primes' satisfaction of the hypothesis the sole remaining open number-theoretic input — an exactly-stated partial result, not a claim of GC.
```
