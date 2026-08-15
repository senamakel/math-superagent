# Pattern-finder: exact structures confirmed on computed data

Session findings. Everything below is a **conjecture** (verified exactly over the
terms/rows supplied, not proved). Sources are the run's own captured data and
scripts; my new scripts are `code/pattern_finder/verify_mersenne_closedform_indep.py`,
`mersenne_ones_position_law.py`, `mersenne_recursion_test.py`, `mersenne_recursion_pin.py`,
`merrecursion candidate` — all ran clean (EXIT 0).

## 1. Mersenne-period affine nu2 — closed form, INDEPENDENTLY confirmed

For the odd-period mod-4 switch word `h = [0]*(P-1)+[1]` with `P = 2^k - 1`
(a Mersenne-length periodic 2-then-odds input), the dyadic nu2 statistic
(= # of 2s in the maximal `{0,2}` suffix of the right diagonal, the run's
canonical convention) is **affine in the column n per residue class of n mod
P**: `nu2(n+P) − nu2(n) = c_{n mod P}` is constant per residue.

Exact facts (verified to k=31, i.e. P ≤ 2^31−1, from-scratch literal full
triangle + the run's `lib.rightdiag`):
- `sum_{r} c_r = 3^k − 3` EXACTLY.  (values: k=2→6, 3→24, 4→78, 5→240, 6→726,
  7→2184, 8→6558, 9→19680, 10→59046; the `3^k−3` sequence is OEIS A058809.)
- `min_r c_r = 2`; every `c_r` is even.
- density slope `= (3^k−3)/(2^k−1)^2 ~ (3/4)^k` (ratio to (3/4)^k → 1.0001 by k=15).
- Fermat-like `P = 2^m+1`: `c_r ≡ 3^m−1` constant, density `(3^m−1)/(2^{2m}−1)`.

My independent literal-triangle builder (no lib import) reproduces `sum c_r =
3^k−3` and `min c_r = 2` for P=3,7,15,31 — the run's earlier claim
`dyadic-oddfactor-affine-modulus-lifting` re-confirmed from first principles.

## 2. Ones-position law (NEW exact detail)

Within the Mersenne c_r/2 array (length P, indices 0..P−1), the positions where
`c_r/2 == 1` are EXACTLY the descending binary partial sums
`{0, 2^{k-1}, 2^{k-1}+2^{k-2}, ..., 2^k−2}`.
- P=15: {0,8,12,14}; P=31: {0,16,24,28,30}; P=63: {0,32,48,56,60,62};
  P=255: {0,128,192,224,240,248,252,254}; P=1023: {0,512,768,896,960,992,1008,1016,1020,1022}.
Verified k=3..10 exactly (k=2 trivial). The whole array is recursively
self-similar: tail of P_k = P_{k−1} with only entry[1] incremented by 1; first
half = 2×P_{k−1} with boundary adjustment at indices 0,1. This gives a complete
recursive closed form for the full per-residue constant array.

## 3. Boundary automaton on REAL rows — exact laws L1–L3 (160 transitions, 0 failures)

For the real prime rows k=1..161 (sieve 2e7, exact int64), with w,i,e = last
three {0,2} entries and c = intruder:
  L1: b_{k+1} ≥ b_k  ⟺  (e_k == 2 and c_k == 4)
  L2: on erosion, c_{k+1} == c_k − e_k
  L3a: on erosion, e_{k+1} == i_k ^ e_k
  L3b: on erosion, i_{k+1} == w_k ^ i_k
All hold with **0 failures** over all 160 transitions (59 regen, 101 erosion).
This is the run's already-proved `step-law-theorem-proved` + Rule-90 boundary;
I only re-ran its own verifier, so it is corroboration, not new.

## 4. Negative results (exact, worth recording)

- nu2 supply sequence (30000 terms), W_switch, excess_e (mod-4 switch ballot
  first 512), regen-gap, jump, and block-profile sequences: **no low-order
  constant-coefficient linear recurrence** (order ≤ 8), **not low-degree
  polynomials**. OEIS: no match for nu2, no match for the switch ballot/ones.
  These are prime-number-theoretic, not low-order arithmetic — consistent with
  the run's ABGS-2011 open-hypothesis position on the mod-4 switch count.
- D(n) = 2·nu2(n)−n is genuinely non-monotone (16,595 negative of 30,000),
  max |D| = 639: no one-sided deviation claim is supportable on nu2 itself
  (the one-sided structure lives only in the switch walk e(n), NOT in nu2).
  This is worth stating because a future attempt could mis-read the nu2
  fluctuation as one-sided.

## Status vs the goal

**None of this closes Gilbreath's conjecture.** The Mersenne affine structure,
the ones-position law and the boundary automaton are all facts about either
(i) periodic odd-factor words (the "dyadic oddfactor" family, where supply is
linear) or (ii) the real rows' local one-step dynamics. The periodic-family
closed form confirms the odd-factor-converse numerically (it is already claimed
`dyadic-oddfactor-affine-modulus-lifting`) but does NOT transfer to the
aperiodic primes (the `abgs-2011-s9-mod4-switch-limit-open` hypothesis stands).
The boundary automaton is the proved step-law, whose regeneration side remains
the only open content: it pins that a (2,4)-event is the sole growth mechanism
but not that events arrive often enough. So the pattern-recognition yield is a
firmed-up exact description of the known linear-supply family and of the local
boundary law — not a proof.

## Verifier status

- `verify_mersenne_closedform_indep.py`: literal full-triangle, no lib import,
  P=3,7,15,31, sum_c_r = 3^k−3 and min c_r=2 CONFIRMED.
- `mersenne_ones_position_law.py`: ones-position law k=3..10, 0 mismatches.
- `mersenne_recursion_test.py` / `pin.py`: pinned the exact self-similar
  recursion (P_k tail = P_{k−1} + increment at index 1; first half = 2·P_{k−1}
  + boundary fix).
- boundary_state.py (run's own): L1–L3 zero failures on real rows.
All EXIT 0. Bound: prime rows to sieve 2e7 depth 161; odd-period words to
P ≤ 2^31−1 measured via lib.rightdiag incremental diagonals.
