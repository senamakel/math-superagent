# Mersenne-affine classification of per-residue ν₂ on odd periods

**Pattern-finder finding, verified-numerically (conjecture, not proved).**

> **SUPERSEDED IN SCOPE (not in truth): this result has been generalised to ALL
> odd periods** in `dyadic-oddfactor-affine-modulus-lifting.md` — every odd P
> is per-residue affine mod `L = 2^{ord₂(P)} − 1` (smallest Mersenne divisible
> by P); the Mersenne family here is the case `ord₂(P)=log₂(P+1)` so `L=P`.
> See that note.  This file remains the detailed treatment of the Mersenne case.

## Setup

2-then-odds sequence with `q_1=2, q_2=3`, gap `q_{m+1}-q_m = 2` if bit else `4`,
bits = **tail-1 word** `[0]*(P-1)+[1]` of odd period `P`.  `ν₂(n)` = #2s in the
maximal `{0,2}` suffix of the right diagonal `δ(q_n)` (body convention,
`lib.rightdiag.cycle_and_nu2`), the quantity feeding Granville Lemma 5.4's
budget `ν₂ ≥ c·n`.

`ν₂` is **per-residue affine (mod P)** iff for each residue `r mod P`,
`ν₂(n+P) − ν₂(n) = c_r` is an exact constant over the whole window.

## Finding (conjecture)

> **`ν₂(n)` is per-residue affine mod `P` (tail-1 word) iff `P` is a Mersenne
> number `2^k − 1`.**

Verified (exact, 0 contradictions):
- **Affine**, min constant `2`: P = 3, 7, 15, 31, 63, 127, 255, 511, 1023
  (`P = 2^k−1`, k=2..10), over windows up to n=12000.
- **Not affine**: every one of the 40 non-Mersenne odd periods tested
  {5,9,11,13,17,19,21,23,25,27,29,33,35,37,39,41,43,45,47,49,51,53,57,59,61,
  65,69,71,73,75,81,85,87,89,91,95,97,99,111,119,123,125,129,131,133,135,137,
  139,141,143} over n in [500,4000].

## Exact closed form of the affine constants

For `P = 2^k − 1`, the per-residue constants satisfy

    Σ_{r=0}^{P−1} c_r  =  3^k − 3           (= OEIS A058809)

verified exactly for k=2..10 (P=3..1023), hence the density slope

    lim ν₂(n)/n  =  (3^k − 3) / (2^k − 1)²,

e.g. P=3 → 2/3, P=7 → 24/49, P=15 → 26/75, P=31 → 240/961, … decaying like
`(3/4)^k` (no uniform `c` across `P`, consistent with `dyadic-oddfactor-infimum-bounded`).

All `c_r` are even; `c_r/2` is a self-similar word: the value-1 positions are
the partial sums of the descending powers `2^{k−1}, 2^{k−2}, …, 2` (for P=31:
positions 0,16,24,28,30), and min `c_r = 2` always, so
`ν₂(n) ≥ 2n/P − O(1)` on every Mersenne word — positive linear supply.

## Independence

Re-verified by a **from-scratch literal full-triangle** builder (no
`lib.rightdiag`) for P=7 and P=15: affine holds, `Σ c_r = 24` and `78`
respectively, matching `3^k−3` exactly.

## Mechanism (block-stability) — verified

The reason the Mersenne periods are affine is a precise block-stability law of
the {0,2}-suffix word: for Mersenne `P = 2^k−1`, for every residue `r mod P`
there is a **fixed word `w_r` of length `P`** such that over the whole window

    suffix(n+P) = suffix(n)  +  w_r    for all n ≡ r (mod P)

i.e. each period appends exactly one residue-dependent block `w_r`, identical
from period to period. Then `ν₂(n+P) − ν₂(n) = wt(w_r) = c_r` is constant, which
is precisely per-residue affinity. Verified exactly for P=7 and P=15:
`wt(w_r) = c_r` for all r (P=7: [2,6,4,4,2,4,2]; P=15: [2,14,8,8,4,8,4,4,2,8,4,4,2,4,2]).
Non-Mersenne P=9, P=25 fail block-stability (the appended word changes from
period to period). This is the concrete structural fact a derivation must
explain: why `suffix(n+2^k−1)` deterministically appends a fixed residue word
iff the period is 2^k−1.

## Interpretation / bearing

- The **collapse side** of the dyadic dichotomy is proved for periods that are
  *powers of 2* (`dyadic-collapse-proved`, `ν₂ = O(1)`).
- The **affine-linear side** now has a precise structural law at periods *one
  less than* powers of 2 (`P = 2^k−1`): `ν₂` is exactly per-residue affine with
  closed-form constants.
- This is **numerical/verification evidence only** — a conjecture, not a proof,
  and does **not** close G-supply for the aperiodic primes. It sharpens the
  odd-factor converse (positive linear `ν₂`) to an *exact affine law with a
  closed-form density* on the Mersenne family, the cleanest such statement the
  run has produced.

## Files
- `code/pattern_finder/dyadic_mersenne_test.py` (classification attack to P=255 + 40 non-Mersenne)
- `code/pattern_finder/dyadic_mersenne_big.py` (P=255,511,1023 affine)
- `code/pattern_finder/dyadic_mersenne_slope.py` (+ captured: exact Σc_r, slope fractions)
- `code/pattern_finder/dyadic_mersenne_constants.py` (+ captured: c_r arrays)
- `code/pattern_finder/dyadic_mersenne_indep.py` (+ captured: literal-triangle independent check)
- captures: `pf_dyadic_mersenne_test/big/slope/constants/indep.captured.txt`
