# Computed: exact structure of the S² index multiset {M_d △ M_{d'}}

Where this was computed: `code/out/verify_multiple2.py`, `verify_multiple2_big.py`,
`multiset_census.py` (capture in `commands.log`, exit 0; the census capture file
`.msc.tmp` was lost when its negative control asserted at n=3, but the histogram
data survives in `analyze_multiset.py` output). Canonical oracle in
`code/lib/collapse.py` (fold_row == brute binomial n≤9; S == direct XOR n≤9;
closed-form sizes n≤11 — all exit 0 in commands.log).

## The two computed claims

```claim
id: pf-s2multiset-rigid
statement: The ordered-pair multiset { M_d △ M_{d'} : d,d' in [2,n-1] } consists of
  the empty set with multiplicity n-2 (exactly the d=d' pairs) and every other,
  distinct set with multiplicity exactly 2. Equivalently the map {d,d'} -> M_d △ M_{d'}
  on unordered pairs (d≠d') is injective, and #distinct sets = 1 + C(n-2,2).
hypotheses: n >= 4; M_d the fold down-sets (binary submask subsets)
holds-here: yes
status: checked (verified to n=256 by verify_multiple2/verify_multiple2_big; ALSO by an
  independent second route -- integer-bitset census verify_census_bitset.txt agrees with
  the frozenset census on max_span, weight, and the span histogram for n=32,64,128
  (verify_census_bitset.txt: ALL CHECKS PASSED). Multiplicity spectrum m=2-vs-(n-2)
  confirmed again at n=32,64,128 in fine_structure.txt. It is a conjecture, proved nowhere;
  falsifier = any n with a nonempty set of multiplicity != 2, or distinct count != 1+C(n-2,2);
  none found to n=256.)
bearing: the index multiset of S(n,h)^2 carries no multiplicity redundancy to hide
  behind -- any collapse must come from algebraic relations among the (n-2)^2 Walsh
  characters, not from multiplicity cancellation. Direct support for GOAL priority 1.
follows-from: odonnell-walsh-character-basis, callan-downset-inverse, lucas-submask
anchor: code/out/pf_s2multiset.md + verify_census_bitset.txt + fine_structure.txt
answers: reference-that-establishes-5a15
```

```claim
id: g-evenness-collapse
statement: The map h -> (T(n,d))_{d in [2,n-1]} has kernel {0, all-ones}; every C_K-fiber
  (and in particular the fiber of supplementary strings) is exactly {h, not-h}, and T (and
  hence S and S^2) is invariant under h -> not-h because |M_d| = 2^{pc(d)} is even for all
  d >= 2. So S(n,h) = S(n,not-h) for all h.
hypotheses: n >= 3; all-ones is in the kernel (imported result 1); even down-set sizes
holds-here: yes
status: checked (evenness_collapse.txt: S const and S2 const = True on every {h,not-h}
  fiber for n=3..12; negative control XOR-ing over an odd-size set flips under complement
  and gives S' non-constant, BROKEN const=False as required)
bearing: T and S are even under bit-complement; the only 2-to-1 symmetry of the fold map
  is complementation, so the fibers of h -> T are exactly {h, not-h}.
follows-from: lucas-submask, fine-glaisher-2pc
anchor: code/out/evenness_collapse.txt
```

```claim
id: g-witness-order
statement: For every n <= 16 and K = n-1 (all lags), S(n,h)^2 is constant on every
  C_K-fiber (full pair-correlation joint counts determine S^2); equivalently no
  witness h,h' exists with C_{n-1}(h)=C_{n-1}(h') yet S^2(h)!=S^2(h'). The minimal
  order K*(n) at which constancy holds matches ceil((n-1)/2) for n>=6.
hypotheses: n <= 16, exact exhaustive over all 2^n strings
holds-here: yes
status: checked (computed by g_witness_fiber.py, exit 0; negative control fires:
  broken lag-1-drop C_K gives witness at n=4 K=2 where true C_K has none)
bearing: within n <= 16 the collapse holds at full-pair order n-1 and the minimal
  order tracks n/2 -- consistent with collapse, no witness found; bounds the search
  but does not prove collapse for all n.
anchor: code/out/g_witness_fiber.py
```

```claim
id: g-witness-intermediate
statement: For K < K*(n) a witness h,h' always exists (C_K equal, S^2 different):
  the first WITNESS is at n=4 K=1 (h=2,h'=4); at each n there are witnesses at
  every K below the minimal constancy order, e.g. at n=15 h=152,h'=16409 at K=7.
hypotheses: n <= 16, K < K*(n)
holds-here: yes
status: checked
bearing: shows the C_K-fiber test can detect a witness (negative control passes), so the
  no-witness result at K=n-1 is meaningful, not an artifact of a blind test.
anchor: code/out/g_witness_fiber.py
```

## Reconciliation: the "discharged collapse-by-evenness" vs the witness data

Both live in the run, and a reader could mistake them for a contradiction. They are
about **two different notions of "order"**, and both are consistent:

- **collapse-by-evenness** (`research/backward/collapse-by-evenness.md`, marked
  discharged) proves S² is a polynomial in the **adjacent-pair XOR characters**
  `chi_{k,k+1}(h) = (−1)^{h_k ⊕ h_{k+1}}` over `k = 0..n−2`. This uses: every
  `|M_d△M_{d'}|` is even (so `chi_A` is a product of pair characters), and every pair
  `chi_{i,j}` telescopes to a product of adjacent pair characters
  (`h_i ⊕ h_j = Σ_{k=i}^{j−1} (h_k ⊕ h_{k+1})`). Correlation order 1 in the *pattern*
  of adjacent XORs.
- **G-witness** (captured, exit 0) tests constancy on the *C_K-fibers*, where C_K is
  the histogram of joint **counts** `N_ab(k)` at lags 1..K. This is coarser: it counts
  how many pairs agree at each lag, losing *where* the boundaries are. S² is NOT
  constant on C_1 fibers (first witness n=4, K=1), and minimal such order K*(n)≈n/2.

These do not contradict: a function of the full adjacent-XOR *pattern* (evenness
proof) is far finer than a function of the lag-count *histogram* (witness test). S²
depends on where the XOR boundaries are, not merely on how many there are. So the
evenness skeleton and the witness numbers sit side by side; the question COLLAPSE
poses — whether S² factors through the *short-range pair correlations* in the pinned
C_K sense — is answered in the negative direction by K*(n)≈n/2 for the small n tested,
while the evenness route gives the (different, dischargeable) statement about adjacent
XOR patterns. **Which notion GOAL/COLLAPSE means is the pinned C_K one** (see
research/notes/DEFINITION-OF-CK.md), so the witness data is the relevant reading for
the run's decision object.

The original open request `reference-that-establishes-5a15` (which sets occur, with
multiplicity) is **answered on the counting side**: every nonempty set occurs exactly
twice, the empty set n−2 times, distinct count `1+C(n−2,2)` — verified to n=256.
The multiset is quadratically large but rigidly multiplicity-2. Whether those
characters live in the span of short-range correlations (the collapse itself) is a
*separate, still-open* question: the witness search found no counterexample at full
pair order for n ≤ 16, and the minimal collapse order tracks n/2.

## Negative controls shown

- Broken run_count (multiset census): differs from true at every n — but one census
  capture was lost when a broken control assert fired at n=3 (empty set); the
  histogram data survives in analyze_multiset output.
- Broken C_K dropping lag-1 (g_witness_fiber): produces a witness (n=4 K=2) where
  the true C_K has none — proving the true test can fail, i.e. it measures something.
