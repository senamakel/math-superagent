# Pattern-finder report — round 11: independent re-check corrects the induced-C4 count (was 2× too large)

## What changed since round 10

Round 10 reported induced C4 = `C(mu,2)·#nonedges` (= `#nonedges` in the μ=2
subfamily), with family sequence `[18, 4158, 26730, ...]`. An independent
exact brute force over all C(n,4) subsets (induced subgraph = exactly 4 edges,
all degrees 2) on the small members **contradicts it by a factor of 2**:

| graph | #nonedges | TRUE induced C4 | report-10 value | (1/2)C(mu,2)·ne |
|---|---|---|---|---|
| rook(3) | 18 | **9**  | 18 | 9 |
| doily | 60 | **90** | 180 | 90 |
| GQ(2,4) | 216 | **1080** | 2160 | 1080 |
| BvLS | 26730 | **13365** | 26730 | 13365 |

## The corrected identity (a proof, not just a count)

For every `srg(v,k,1,2)`:

```
induced C4  =  (1/2) · C(mu,2) · #nonedges .
```

**Proof.** (a) c7 (proved in round 10, derived from λ=1): the μ common
neighbours of any non-adjacent pair are pairwise non-adjacent (otherwise edge
`ai·aj` lies in two distinct triangles, contradicting λ=1 = every edge in a
unique triangle). (b) Hence every (nonedge pair, non-adjacent common-neighbour
pair) is an induced C4, so summing `C(mu,2)` over the `#nonedges` nonedges
counts every induced C4. (c) But **each induced C4 is produced by exactly two
of its nonedge pairs** (the two opposite vertex pairs), so the sum over
nonedges double-counts. Dividing by 2 gives the formula. (a)+(c) are the
argument; this is a derivation, not a fit. The μ-specific factor means the
μ=3/5 members (doily, GQ(2,4)) carry genuinely larger induced-C4 counts, which
the corrected brute force confirms.

A direct anchored computation (each nonedge's non-adjacent cn-pairs summed,
then ÷2) gives the same four values exactly (`code/out/pf_inducedC4_fixed.py`)
and matches the closed form on all four members including BvLS=13365.

## Consequence for the μ=2 subfamily (the 99-relevant family)

In the μ=2 family (`k∈{4,14,22,112,994}`, `v=1+k²/2`) the corrected closed
form is

```
induced C4  =  #nonedges / 2  =  v·k(k−2)/8 ,
```

family `[9, 2079, 13365, 9660420, 60890805864]`
(rook 9, 99: 99·14·12/8 = 2079, BvLS 243·22·20/8 = 13365 — checked exactly).

Round 10's sequence `[18, 4158, 26730, ...]` (= `v·k(k−2)/4`) is the **#nonedges
itself**, i.e. exactly 2× the induced-C4 count. The structural source of the
round-10 error: it omitted the ÷2 (each C4 owns two of its nonedges).

## Status and bearing

- **c7 (round 10 Finding 1) is UNAFFECTED and correct** — it is a λ=1 theorem,
  re-verified here on all four members.
- **The induced-C4 count is corrected** from `v·k(k−2)/4` to `v·k(k−2)/8` in
  the μ=2 family. It is still fully parameter-determined and still holds on
  both controls, so like every family count it **does not separate 99**. The
  correction does not open or close a lever; it fixes the value a hard target
  would need to match.
- Everything else in the round-1..10 catalogue was independently re-derived and
  reproduced exactly this round (see `code/out/pf_indep_family_check.py`):
  triangles `{6,231,891,117096,81842481}`, pentagons, hexagons, outer blocks,
  distance-2, coclique `{3,22,45,561,15408}`, n3 cap `{18,4158,...}` — all
  unchanged. The n3 radius trajectory (round 8) is an enumeration count, not an
  algebraic sequence; the incidence p-ranks (round 9) showed no low-degree law
  and are control values, not a catalogue field.

## Defect to record

Report 10's Finding 2 stands corrected (2×). The family-count line remains
exhausted and none of its quantities separates 99; the standing 99-specific
levers (coclique bound 22; forced n3≥3) are unchanged by this correction.

## Files

- `code/out/inducedC4_correction.captured.txt` — the correction, exact values + proof.
- `code/out/pf_indep_inducedC4_small.py` — full brute force on rook/doily GQ(2,4).
- `code/out/pf_inducedC4_fixed.py` — anchored exact count, all four members.
- `code/out/pf_indep_family_check.py` — independent reproduction of the whole family-count catalogue.
- This report.
