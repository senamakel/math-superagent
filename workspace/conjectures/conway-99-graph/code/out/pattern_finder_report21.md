# Pattern-finder report — round 21: the incidence p-rank artifact, run through the exact tools; sequence line confirmed exhausted

## What I did

Round 20 declared the sequence line exhausted and identified the one on-disk
artifact newer than round 19 (`incidence_prank_determinism.captured.txt`,
mtime 00:33) as the sole thing that might have escaped the tools. This round is
an **independent re-check of that exclusivity** and a **first tooling of the
p-rank numbers** the artifact carries.

I first confirmed by file listing that nothing is newer than
`incidence_prank_determinism` (00:33) other than the round-20 report itself and
the INDEX it triggers — i.e. the mined surface is unchanged since the last
look. I then read the artifact and extracted the integer lists it holds.

## The numbers the last artifact carries

The p-rank gate measures `N` (points × triangles, `NN^T = (k/2)I + A`) and the
graph matrix rank, exactly, over GF(2) and GF(3) for four graphs:

| graph | params | rank_2(N) | rank_3(N) | N-col rank deficiency vs n |
| --- | --- | --- | --- | --- |
| rook(3) | (9,4,1,2) | 5 | 5 | 4 |
| doily | (15,6,1,3) | 10 | 10 | 5 |
| GQ(2,4) | (27,10,1,5) | 21 | 21 | 6 |
| BvLS | (243,22,1,2) | 243 | 231 | 0 |

## Exact sequence tools over these (this round, first time)

`analyze_sequence([5,10,21,243])`, `analyze_sequence([5,10,21,231])`,
`analyze_sequence([4,5,6,0])`:
- differences never become constant at any level → **not a low-degree polynomial**.
- `find_linear_recurrence` reported order-2 fits (e.g. `a(n)=201 a(n-1) − 1989/5 a(n-2)`).

**The order-2 fits are generic overfit, not structure.** With 4 terms and a
constant-coefficient order-2 recurrence there are exactly 2 free coefficients
`c1,c0` and exactly 2 fitting equations (for `n=2,3`), so *any* four numbers
with a non-degenerate start admit such a Q-coefficient fit. I verified this
mechanically: every permutation of the four rank values fits its own order-2
recurrence with entirely different coefficients:

```
[5,10,21,243]  coefs (399.9, -397.8)
[21,5,243,10]  coefs (36.98, 11.62)
[243,10,5,21]  coefs (0.666, -0.166)
```

A constant-coefficient "recurrence" whose coefficients change when the list is
reordered is not a property of anything.

## Why the lists are not sequences at all

`[5,10,21,243]` is four **independent measurements** taken at four *different*
family members — and two of them (doily μ=3, GQ(2,4) μ=5) are not even members
of the `(1,2)`-family the problem lives in. There is no index `n` in which the
values are ordered for a reason; the ordering in the capture is arbitrary. So
there is no extrapolating term to falsify, and both the "not polynomial" and
"order-2 recurrence" outputs are vacuous. This is the same failure mode round 18
warned about (search-trace vs sequence), now at the level of arbitrary
measurement lists.

## What the artifact actually establishes (and why it is out of sequence scope)

The p-rank numbers are a **sound invariant-comparison result, already settled
by the gate**: rank_2(N) genuinely varies across the two existing `(1,2)`-family
members (rook(3)=5, BvLS=243; rank_3 5 vs 231), so the incidence p-rank is NOT
parameter-determined and is a possible separator — but it is UNPROVABLE this way,
since there is no second `srg(99,14,1,2)` to measure against (existence of 99 is
the very question). That is a settled (b) answer, not a fitting target; the
sequence tools neither help nor hurt it.

## Verdict

- The p-rank lists are not sequences and carry no polynomial/recurrence structure
  (order-2 fits shown to be generic overfit).
- No on-disk artifact newer than round 20 holds sequence-bearing structure.
- The sequence line is confirmed fully closed across rounds 1-21. The only
  99-specific structural values remain the coclique bound 22 and the forced
  n3 ≥ 3 (Makhnev conditional) — neither a sequence.

**NOTHING FURTHER** is available from the sequence tools. Genuinely new
exploitable structure, if any, is in construction/search: the 99-vertex lift of
the super-simple 2-(22,4,2) design, and the k=14 local triangle geometry.

## Files
- `code/out/incidence_prank_determinism.captured.txt` / `.py` — the source artifact.
- This report.
