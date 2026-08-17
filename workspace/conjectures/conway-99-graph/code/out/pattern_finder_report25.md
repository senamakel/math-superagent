# Pattern-finder report — round 25: re-check that nothing has changed since report24

## What I did

Headline task: look for exploitable structure in on-disk results, extract the
integer sequences, run the exact sequence tools. Since the previous 24 rounds
all reported the sequence line closed, the only route to a *new* finding this
round is an artifact created since report24 containing an untooled sequence.

## What I found

`ls -lt` over `code/out/*.captured.txt` and `code/out/*.md` puts the newest file
on disk at `pattern_finder_report24.md` (01:02), preceded by
`c3_spectrum_exact_verify.captured.txt` (00:52) and
`incidence_prank_determinism.captured.txt` (00:37). **Nothing on disk postdates
report24.** No new artifact exists to mine.

Report24 already ran the exact sequence tools over the one on-disk list earlier
rounds had not tooled — the n3-seed survivor-count-per-radius
`[1,2,5,11,19,19,19]` from `n3_grow_radius.captured.txt`:
- `analyze_sequence`: no low-degree polynomial (differences never constant),
  not exponential.
- `find_linear_recurrence(max_order=4)`: no constant-coefficient recurrence of
  order ≤ 4 fits all 7 terms.
- `oeis_lookup`: no match.
- It argued the list is an enumeration-mechanism trace (witness-materialisation
  order dependent), so it has no definable extrapolation and hence **no first
  term that would falsify a pattern** — not a real sequence.

## Standing verdict (cross-checked with CONTEXT.md and durable memory)

Every parameter-determined count on disk is `a = 2u+1 | 63`-governed
(u ∈ {1,3,4,10,31}) and fails to separate the open 99 case from its existing
controls rook(3)=srg(9,4,1,2) and BvLS=srg(243,22,1,2). The incidence p-rank
lists (`[5,10,21,243]`, `[5,10,21,231]`, deficiencies `[4,5,6,0]`) are 4
independent measurements at 4 distinct family members (two outside the
λ=1,μ=2 family), not an indexed sequence — any order-2 recurrence fit is
generic overfit (verified in round 21).

The only 99-specific structural values are the coclique bound 22 and the
forced n3 ≥ 3 (Makhnev conditional); neither is a sequence the sequence tools
can extend or falsify.

## Conclusion

NOTHING FURTHER. The results have not changed since the last look, and no
untooled on-disk sequence exists. Reporting a polynomial/recurrence fit on a
search-trace or a 4-point p-rank list would be invented pattern, and is
withheld. Any genuinely new exploitable structure belongs to construction/search
(the 99-vertex lift of the super-simple 2-(22,4,2) design; the k=14 local
triangle geometry), not to the sequence line.
