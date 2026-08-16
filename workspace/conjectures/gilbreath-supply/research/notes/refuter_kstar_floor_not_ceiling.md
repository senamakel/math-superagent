# Refuter finding — the budget closed form is floor(n/2), not ceil(n/2)

Status: verified / clarification, NOT a new refutation of a live open claim.
The budget is settled internally (directive 41); this note records the
definitional mechanism that made the run's own captures disagree, with an
explicit pair confirmed by `find_counterexample`, so nobody reopens it.

## What I attacked

The rungs `R-budget-n32` and `R-kstar-closed-form` and the gap
`G-order-budget` each assert (for the SUPPly fold's order-K correlation
budget) that

    K*(n) = ⌈n/2⌉   (6 ≤ n ≤ 32, n = 5 the sole exception)

where K*(n) is the correlation order at which the squared excess S(n)² =
((n−2) − 2·ν₂(n))² becomes a function of the order-K correlation data of the
binary string h.  GOAL.md priority 3 flags "the closed form is not yet right"
(n = 5 mismatch), and the rung's own "expected bite" is whether the ⌈n/2⌉
growth re-collapses as n grows.

## What is actually true (run's own faithful captures + this confirmation)

The faithful *cumulative* reading (equal on C_1..C_K = equal (k+1)-gram
histograms for every k = 1..K) gives

    K*(n) = ⌊n/2⌋

for n = 2..18, established by five captures (`kstar_exact`, `kstar_settle`,
`kstar_resolve`, `kstar_structural_capture`, `cum_floor18`) and two independent
cumulative implementations.  ⌈n/2⌉ and ⌊n/2⌋ agree at every even n; they
disagree exactly at odd n, where K* sits one below the ceiling
(n = 7 → 3, 9 → 4, 11 → 5, 13 → 6, 15 → 7).  The n = 5 "mismatch" this run
noted was the first tell of this: K*(5) = 2 = ⌊5/2⌋.

So the budget claim as stated in the open rungs (⌈n/2⌉) is **false**; the true
closed form is ⌊n/2⌋.  This is a settled correction, not a live open question
— the substance of the reopen survives (K*(n) is still linear ≈ n/2, so the
`1 < K ≲ n/2` territory GOAL.md claims is real).

## The definitional mechanism the captures disagreed over

The earlier captures `kstar_resolve` and `kstar_budget_explicit` grouped by the
*single* `(K+1)`-gram histogram `C_K` alone (the `C_1..C_K ⟺ C_K` reduction),
and got non-monotone, larger budgets (e.g. B(14)=8 < B(13)=11 — impossible
under the nested cumulative reading, self-refuting).  The faithful reading
must use the **nested cumulative** family C_1..C_K, which refines
monotonically.  `kstar_exact.py` and `refute_kstar.py` are the correct
implementations; the single-C_K grouping is the refuted reduction and must not
be used (already recorded in `research/notes/kstar_budget_not_ceiling.md`).

## Independent n=8 witness confirmed by `find_counterexample`

Encoding `code/refute/kstar_n8_k4.p` asks: does there exist h,h' in F₂⁸ with
identical order-4 correlation (identical multiset of the four 5-bit windows)
but different S²?  `find_counterexample` returned **refuted** with the model

    h     = 01110111   5-gram multiset {01110, 11101, 11011, 10111}
    h'    = 10111011   5-gram multiset {10111, 01110, 11101, 11011}   (same)
    h     cells(d=2..7) = (0,1,0,0,0,0)   tot=1   S=4   S²=16
    h'    cells(d=2..7) = (1,1,0,0,0,0)   tot=2   S=2   S²=4

S² differs (16 vs 4) with identical C₄.  Hand-verified against the literal
submask-XOR cell definition (t_direct): the four 5-grams are a cyclic shift /
permutation of one another, and the fold counts differ.  This is a genuine
*single-C₄* witness.

Crucially, this pair has **different C₁** (2-gram histograms): h has
(00:0, 01:2, 10:1, 11:4), h' has (00:0, 01:2, 10:2, 11:3).  So it does NOT
witness the *cumulative* claim — it is exactly the pair that illustrates why
the single-C_K grouping (which `kstar_resolve` misused) found longer "witnesses"
than the correct nested reading.  It is consistent with the settled
K*(8) = 4 = ⌊8/2⌋.

## Why this is worth banking

- The open rungs still *carry* the ⌈n/2⌉ claim as their stated target.  Since
  that closed form is false (it is ⌊n/2⌋), nobody should spend a proof attempt
  on ⌈n/2⌉ — that is the concrete negative result: **the rung's stated closed
  form is wrong**, and the run should state ⌊n/2⌋.
- The explicit single-C₄ pair (01110111 / 10111011) and its C₁ difference make
  the single-vs-cumulative definitional split concrete, so a future capture
  that groups by single C_K is caught by inspection.

## Bound and honesty

The ⌊n/2⌋ verdict is verified to n = 18 (exhaustive 2^n oracle).  It is a
*verification bound*, not a proof for all n — the question "does K*(n) stay
⌊n/2⌋ for all n, or re-collapse" remains open past the brute reach, and is best
settled by the closed-form proof (R-kstar-closed-form with functional-construction
turned on), not by further brute force.  I did not re-derive anything the run
already owns; this confirms the settled budget and pins the mechanism.
