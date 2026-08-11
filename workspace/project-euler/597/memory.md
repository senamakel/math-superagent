# Working memory

## Problem
Torpids (PE-style). n boats, start positions p_j=40j (j=1 lowest), finish at L.
Speeds v_j ~ Exp(1) iid. Constant speed until finish or bump (catch nearest
ROWING boat ahead, then OUT/transparent; bumped boat continues). New order from
bump chains; parity = sign of permutation from starting ascending listing to
new ascending listing. p(n,L) = P(new order is even permutation). Examples:
p(3,160)=56/135≈0.4148; p(4,400)=0.5107843137. Goal: p(13,1800).

## Established results
- `brute.simulate_order` + `parity_of_new_order` faithfully implement the race
  and now reproduce ALL five rows of the n=3,L=160 table (verified: none even,
  B bumps C odd, A bumps B odd, both-bump-C even, chain odd).
- `brute.parity_of_new_order` had a comparator bug (inverted `above` test) that
  shipped in the original run: it reported identity order for every non-trivial
  bump structure, giving MC 1.000000. FIXED (see Failed approaches).

## Failed approaches / dead ends
- Structural hypothesis H: "final parity is a function of the ranking by
  decreasing w_j = v_j/(L-p_j) only." **REFUTED.** With the corrected parity,
  `verify_hypothesis.py` N=200000 reports w-order buckets containing BOTH
  parities: n=3 L=160 has 1 inconsistent order, n=4 (both L) 9, n=5 L=400 66,
  n=5 L=1800 67.
- Concrete counterexample (n=3, L=160), w-order (0,1,2) in both:
    speeds [0.88083,0.60364,0.35634] -> parity 1
    speeds [0.72906,0.43938,0.02941] -> parity 0
  (membership of a w-order bucket carries no parity info).
- Hence the race outcome depends on speed magnitudes, not just their rank
  order: must solve with the true continuous dynamics (exact integration over
  the Exp speeds), not a permutation-only reduction.

## Open questions
- Correct exact method for p(13,1800). The chronology (bump vs finish inter-
  leaving) means events are not merely pairwise-catch comparisons; need an
  exact/analytic route, likely order-statistics/memoryless exponential
  structure. Not yet attacked.
