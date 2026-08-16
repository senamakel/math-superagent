# Census of the S² index multiset — claims

The weighted span histogram and run structure of `{ M_d △ M_{d'} }` for
`d,d' ∈ [2, n−1]`, computed by two independent routes:

1. `code/out/multiset_census.py` — canonical `lib.collapse` frozensets,
   per `n = 3..128`, all assertions passed, negative control shown failing.
2. `code/out/verify_census_bitset.py` — self-contained integer-bitset route
   (no `lib.collapse` imports), agrees set-for-set, multiplicity-for-
   multiplicity and span-for-span with route 1 at every n = 3..128.

Capture: `code/out/multiset_census_n128.txt` (full print), plus
`code/out/verify_census_bitset.txt` and `code/out/fine_structure.txt`.

```claim
id: census-full-span-support
statement: >
  The weighted span histogram H_n(k) = Σ_{A : span(A)=k} m(A) has support
  exactly {0} ∪ [3, n−1] for every n = 3..128: max span = n−1 carries weight
  n−2, and every span 3..n−1 carries positive weight. Weighted mean span
  n=32: 19.42, n=64: 40.29, n=128: 82.48; weight on span ≥ n/2 is
  69.8% (n=32), 71.7% (n=64), 73.0% (n=128). So the support is NOT
  concentrated on bounded span — long-span sets (span comparable to n) carry
  positive weight m(A) ≥ 1 throughout.
hypotheses: n in [3,128]; d,d' in [2,n-1]; span(A)=max-min+1
holds-here: yes
status: checked
bearing: >
  Refutes the sufficient condition that "the index multiset is dominated by
  unions of a bounded number of adjacent positions": long-span sets carry
  weight 2 at every span up to n−1. Does NOT refute collapse: the chisel
  school's evenness/matching argument (every |A| even, so χ_A reduces to
  adjacent pair characters) shows collapse can hold despite long spans, and
  the census confirms all sets have even size.
anchor: code/out/multiset_census_n128.txt (A, span units), code/out/verify_census_bitset.txt
```

```claim
id: census-multiplicity-injective-pairs
statement: >
  For every n = 3..128: the distinct index sets are C(n−2,2)+1 in number; the
  empty set M_d △ M_d occurs with multiplicity n−2; and every nonempty A in
  the image occurs with multiplicity exactly 2. Hence (d,d') ↦ M_d △ M_{d'}
  is injective on unordered pairs {d,d'}, d,d' ∈ [2,n−1].
hypotheses: n in [3,128]
holds-here: yes
status: checked
bearing: >
  The S² coefficient m(A) is exactly 2 for every nontrivial character in the
  expansion S² = Σ_A m(A) χ_A: no coincidence/cancellation among pairs of
  rows exists to exploit or to fear; the multiset is determined by the
  injective image. This is the exact "which sets occur" answer GOAL priority 1
  asks for at the level of distinctness, and the next step is the closed-form
  description of that injective image.
anchor: code/out/fine_structure.txt (B), structure check n=3..128 (all assertions)
```

```claim
id: census-dyadic-families
statement: >
  The three hand-derived dyadic families are confirmed for all k with 2^k ≤
  n−2 (checked n = 64 and n = 128, all such k):
  (i)  M_{2^k−1} △ M_{2^k} is one maximal run of length 2^k (span = |A| = 2^k);
  (ii) M_{2^k−1} △ M_{2^k−2} is 2^{k−1} singleton runs;
  (iii) M_{2^k} △ M_{2^k+1} = {n−2^k−2, n−2}, a two-point set of span 2^k+1.
  Family (iii) is the "far pair" of the backwards note; family (ii) is the
  "Θ(n) alternating singletons" of the note, and (i) is the one-run block.
hypotheses: n in {64,128}; 1 ≤ k, 2^k ≤ n−1
holds-here: yes
status: checked
bearing: >
  The dyadic families are the extreme long-span elements of the image: they
  realize spans Θ(n), with |A| from 2 up to Θ(n), all with multiplicity 2.
  They are the must-witness candidates for any fiber test that claims a
  bounded correlation order; the evenness (all sizes even: 2, 2^{k−1}, 2^k)
  is what the order-1 matching argument survives on.
anchor: code/out/multiset_census_n128.txt, code/out/verify_census_bitset.txt
```

```claim
id: census-run-count-powers-of-two
statement: >
  The weighted run-count histogram R_n(r) = Σ_{A : runs(A)=r} m(A) at
  n = 64 concentrates on even run counts, dominated by powers of two
  (r = 2: 350, 4: 780, 8: 850, 16: 362, 32: 2, and r=64: 2 for family (i)
  with k = 6), with smaller weight on other even counts and only
  r ∈ {1(=fam(i) k=1),3,5,7,9} odd counts (n=64 max odd weight 120 at r=5,
  vs 780 at r=4); n=128: r=8 carries 2950, r=16 2496, r=4 1810, r=32 864,
  r=64 2, odd counts ≤ 612. The conjecture "run counts are powers of two"
  is FALSE as a statement about every set (odd counts 3,5,7,9,11 occur), but
  the weight is extremely concentrated at powers of two.
hypotheses: n in {32,64,128}
holds-here: yes
status: checked
bearing: >
  A power-of-two run count is what a dyadic-fold cookie-cutter analysis would
  predict; the census shows the true picture is weight-concentrated at,
  but not confined to, powers of two — a finer structural fact for the
  G-collapse-range gap than "few runs per set".
anchor: code/out/negative_control.txt (true histograms)
```

```claim
id: census-even-sizes
statement: >
  Every |M_d △ M_{d'}| is even for all n = 3..128 (cross-checked against the
  closed form 2^pc(d)+2^pc(d')−2^{pc(d∧d')+1}, which is even termwise;
  agreement pairwise throughout). Mean |A| grows ~linearly: 9.40 (n=32),
  15.45 (n=64), 24.90 (n=128) — the per-set sizes are NOT O(1).
hypotheses: n in [3,128]
holds-here: yes
status: checked
bearing: >
  Corroborates the chisel school's order-1 collapse argument: an even A admits
  a perfect matching, χ_A = ∏_{(i,j) in matching} χ_{i,j}, and each pair
  character telescopes through adjacent pairs, so S² = Σ m(A) χ_A is a
  function of the lag-1 (adjacent-pair) correlations only — long spans are
  cancelled by telescoping, not by weight. The census thereby turns the
  bounded-span sufficient condition into a necessary-but-not-required fact.
anchor: code/out/multiset_census_n128.txt (cross-check 3), even-size sweep n=3..128
```

```claim
id: census-negative-control
statement: >
  A deliberately wrong run_count (every set's count shifted by +1) changes the
  weighted run-count histogram at every n = 3..128, shown concretely at
  n = 32, 64, 128 (true {0:30, 1:36, 2:176, ...} vs broken {1:30, 2:36, ...}
  at n=32). The census measure is therefore not blind to run structure.
hypotheses: n in [3,128]
holds-here: yes
status: checked
bearing: >
  Rules out a degenerate run_count that trivially satisfies any hypothesis
  about the run structure: the reported run histograms distinguish true from
  broken, so a claim conditioned on them is measuring the real quantity.
anchor: code/out/negative_control.txt
```