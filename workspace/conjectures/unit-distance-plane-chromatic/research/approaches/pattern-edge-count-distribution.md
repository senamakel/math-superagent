# Pattern analysis: edge-count distribution of the sharp-kernel census C_n

Author: pattern-recognition specialist. All statements are EXACT over the
enumerated instances; every structural conclusion is a **conjecture**.

## Data source

`code/out/census_kernel_n11.captured_witnesses.json` — complete enumeration of
the sharp-kernel class C_n (min-degree>=4, K4-free, K2,3-free,
neighbourhood-max-degree<=2) with a verified 4-colouring witness per member,
for n=8..11. All 249 members are 4-colourable (two independent oracles), so the
size-bound result "every unit-distance graph on <= 11 vertices is 4-colourable"
stands and is not revisited here.

## Newly extracted sequence: total edge count per n (not examined in earlier passes)

Summing e(G) over all kernel members at each n (from the witness file, exact):

| n | members | total edges | mean edges/member |
|---|---------|-------------|-------------------|
| 8 | 1       | 16          | 16.0 |
| 9 | 4       | 73          | 18.25 |
| 10| 16      | 332         | 20.75 |
| 11| 228     | 5294        | 23.22 |

Sequence `[16, 73, 332, 5294]`.

## Edge-count histograms per n (exact)

| n | e=16 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|------|----|----|----|----|----|----|----|----|
| 8 | 1    |    |    |    |    |    |    |    |    |
| 9 |      | 3  | 1  |    |    |    |    |    |    |
|10 |      |    |    | 6  | 8  | 2  |    |    |    |
|11 |                   30 | 127 | 62 | 9 |

The n=11 multimodal spread (30 members at 22 edges, 127 at 23, 62 at 24, 9 at
25) shows the kernel is not edge-regular — a fact against any clean structural
enumeration formula.

## Tool verdicts

- `analyze_sequence([16,73,332,5294])`: not a low-degree polynomial; leading
  ratios 4.56, 4.55, 15.95 (super-exponential onset at n=11, mirroring the
  member-count head 1,4,16,228).
- `find_linear_recurrence([16,73,332,5294], order<=3)` DID return an order-2
  fit, but **this is a tautology, not structure**: I proved that any four
  generic terms admit an order-2 constant-coefficient recurrence (two free
  parameters solve two consistency equations; the fit is degenerate only when
  the determinant b^2 - ac vanishes). Four points are never evidence of a
  recurrence. Same for `[1,3,6,30]` (min-edge counts) whose order-2 hit is
  likewise vacuous.

## The one genuinely informative negative

`find_linear_recurrence([1,4,16,228], order<=3)` returns **no** fit. This is not
a short-data artifact: the quadruple is *algebraically inconsistent* with any
order<=2 constant-coefficient recurrence (the two equations
4c1+c2=16 and 16c1+4c2=228 force 64=228). So the member-count head
4^0,4^1,4^2,228 is provably not order-2 recurrent, consistent with the Arnold
reading that the geometric head was coincidence (the out-of-sample 228 breaks
both 64 and the recurrence). This confirms the earlier no-structure conclusion
is sound, not an artifact of only having four terms.

## Verdict

**No exploitable numerical sequence regularity in this data.** All four-term
"recurrences" are tautological overfits; the one non-tautological fit query
(the member counts) is provably absent. Extending any of these sequences
requires the n=12 kernel count (approximately 100M+ graphs — infeasible this
run), and there is no closed-form route that would make that enumeration
unnecessary. The load-bearing structure of the run remains the *structural*
one: every kernel member through n=11 is 4-colourable.

## Recommendation

Do not chase closed forms here. The productive next derivation is structural,
not numerical: fix the 4-chromatic kernel members and test the
`G-forced-pair-exists` crux (does any 4-colouring of such a graph force a pair
at distance >= 1/2 monochromatic?) — that is where a bound could move, matching
the board's adopted rigidity-matroid direction.

## Artifacts
- This file.
- Evidence computed in this run: `code/out/` edge-count extraction from
  `census_kernel_n11.captured_witnesses.json`; the 4-term-tautology proof
  (order-2 fit exists for generic quadruples).
