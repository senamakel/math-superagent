# ROOT.md — Gilbreath's conjecture: state of the run

## The object and the reduction

`A_0 = (2,3,5,7,...)` primes, `A_{k+1}(i) = |A_k(i) - A_k(i+1)|`. The conjecture
is `A_k(0) = 1` for all `k ≥ 1`. By elementary parity (see
`notes/reduction.md`), the shape `(odd, even, even, ...)` is preserved and
`A_{k+1}(0) = |1 - A_k(1)|`, so the conjecture is **equivalent** to

> `A_k(1) ∈ {0, 2}` for every `k ≥ 1`.

This is proved, not conjectural, within a parity induction. **Which side the
run is on:** the general-class side. As `problem.md` argues, the reduction is a
statement about *any* sequence `(2, odd, odd, ...)`; primality enters only to
make `2` the sole even prime and to give small gaps. A theorem for a general
Gilbreath-like class of odd-gap sequences would settle the prime case as a
corollary. The run does **not** lean on prime distribution.

## Structure of a minimal counterexample

A minimal counterexample is a row whose second entry is `4, 6, 8, ...` (any even
`≥ 4`) — equivalently, the first row index `k` with `A_k(1) ≥ 4`. Then
`A_{k+1}(0) = |1 - A_k(1)| ≥ 3` and the leading `1` is lost. By the OEIS note
(M. F. Hasler, A036262) such a value `≥ 4`, once it has zeros ahead of it, keeps
its value and "propagates" toward the front; so the smallest counterexample is
searched for among rows whose leading `{0,2}` block has *ended* and cannot be
regenerated in time. Consumption (a block of length `n` protects `n` rows per
Odlyzko's exact lemma — see below; the `≈ n/2` figure in the original brief is
superseded by the sourced constant) vs regeneration is the whole obstruction.

## Current verification bound

- **This run, computed:** `code/out/witnesses.json`, exact integer arithmetic,
  sieve to 400000 (33860 primes), `depth_verified = 600`, with
  `leading_entry_is_1 = true`, `second_entry_always_0_or_2 = true`,
  `min_leading_02_block = 2`. Checked against problem.md's rows `A_1..A_5`.
  `code/pattern/blocks_deep.py` pushed to **depth 1000** (sieve to 20,000,000,
  1,270,607 primes): `first_bad = None`, agrees on k=1..40, longest pure
  erosion run 838 rows, regeneration still occurring (max jump 360698 at
  k=146); see `code/out/blocks_depth1000.json`.
- **Cross-checked against the OEIS catalogue:** `block_profile(k) = A000232(k) − 1`
  for k=1..16 (independent source agreement on the data).
- **Reported in the literature:** Odlyzko verified the conjecture for primes
  `≤ 10^13` (i.e. out to `pi(10^13) ≈ 3·10^11` rows of primes), Math. Comp. 61
  (1993) 373–380. This is *sourced* (encyclopedia-of-math, mathworld,
  oeis-A036262) but **not reproduced here** and not a proof.

These two numbers must never be conflated in a claim: depth 600 (ours) vs
`10^13` (Odlyzko, cited).

## Restricted classes of Gilbreath-like sequences settled, with hypotheses

All three below are **proved** by the elementary mechanism in
`notes/reduction.md` (once a row reaches a shape `(1, c, c, ...)`, `c ∈ {0,2}`,
the leading `1` persists forever). They are the "regeneration already complete"
corner cases — they show the mechanism but do **not** settle the open
regeneration question, which is about rows that must *enter* the `{0,2}` regime
repeatedly.

1. **Consecutive odds.** `A_0 = (2, 3, 5, 7, 9, ...)` (all odd integers ≥ 3).
   Then `A_1 = (1, 2, 2, 2, ...)`, so `A_2 = (1, 0, 0, ...)` and leading `1`
   persists forever. Hypotheses: gaps between consecutive non-initial terms are
   exactly `2`. Status: proved.
2. **First-difference constant-tail of 2s.** Any sequence with
   `A_1 = (1, 2, 2, ..., 2)`. Then leading `1` persists forever (same
   argument). Hypotheses: `A_0` is `(2, odd, odd, ...)` and `A_1` is `1` then a
   constant tail of `2`s. Generalises (1). Status: proved.
3. **Reaching a constant `(1, c, c, c, ...)` row.** Any sequence whose
   iterated-difference triangle reaches a row of the form `(1, c, c, c, ...)`
   with `c ∈ {0, 2}`. From that row the leading entry is `1` forever.
   Hypotheses: the triangle attains such a row (full regeneration into a
   constant tail). Status: proved.

**Not settled (open goals)**: the general class "2 followed by odd numbers with
gaps bounded by `g`", and the regeneration claim that the `{0,2}` regime is
entered infinitely often.

Odlyzko's block lemma is now **sourced with its exact constant**: if
`d_K(1)=1` and `d_K(n) ∈ {0,2}` for `1 ≤ n ≤ N`, then `d_k(1)=1` for
`K ≤ k ≤ N+K−1` — a leading `{0,2}` block of length `N` protects **`N`
subsequent rows** (one per block entry), not `≈ n/2`. Primary source: Odlyzko
1993, *Iterated absolute values of differences of consecutive primes*, Math.
Comp. 61(203) 373–380, intro (full LaTeX at
`sources/odlyzko-1993-iterated-differences-latex-source.full.md`); independently
stated in Killgrove–Ralston 1959, Math. Comp. 13:121–122 (full PDF at
`sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`).
Sourced, not yet re-derived here — see `notes/library-state.md` claim
`gc-block-lemma-odlyzko`.

```claim
id: block-profile-equals-a000232-minus-1
statement: The length of the leading {0,2} block in row A_k of the prime Gilbreath triangle satisfies block_profile(k) = A000232(k) - 1 (number of terms before the first term > 2 in the (k)-th difference, minus 1).
hypotheses: A_0 = primes; block counts consecutive initial {0,2} entries of A_k.
holds-here: yes
status: catalogued (matches the OEIS b-file terms for k=1..16); our own profile computed to depth 600 in witnesses.json
bearing: independently confirms the run's row data against the published catalogue; lets claims about block length be phrased in a catalogue-backed quantity.
anchor: code/out/witnesses.json + oeis-A000232
answers: are-our-block-lengths-reliable
```

## Sources in the library

- `oeis-A036262` (iterated prime differences) and `oeis-A000232` (block lengths):
  catalogue terms, the `≥4`-propagation note (Hasler, agrees with our reduction),
  Odlyzko `10^13` citation. **Digested.**
- `encyclopedia-of-math`, `mathworld` (Gilbreath's conjecture): statement,
  Odlyzko `10^13`, Killgrove–Ralston 1959 `k<63419`. **Digested.**
- `odlyzko-publications-page`: bibliography only; confirms the Odlyzko 1993
  paper exists (pp. 373–380) but contains no statements. **No help for content.**
- **Pending:** the Odlyzko 1993 block lemma itself, and any *proved* theorem on
  a nontrivial Gilbreath-like class (e.g. bounded-gap odds). Neither is yet in
  the library.

Dependencies that have **not** landed: the Odlyzko 1993 full text (block lemma
with constant), and any source proving a nontrivial restricted class. The three
restricted classes above are stated from this run's own elementary proof, not
from a landed source.
