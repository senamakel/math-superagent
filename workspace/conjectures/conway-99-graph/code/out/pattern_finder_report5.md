# Pattern-finder report — round 5

## What changed since round 4

Round 4 closed the last *untested* family count (induced C5) and catalogued every
family sequence as a quartic-in-`u` closed form with no low-order recurrence and no
OEIS entry. Round 5 adds one genuinely new checked fact — the **induced K₄−e
(diamond) count is strictly degenerate (0) for the whole family** — which was the
one counting quantity GOAL.md names as a potential lever that the prior rounds had
never tabulated. It also runs the sequence tools on the eigenvalue-multiplicity
sequences, which had never been formally fed to them.

## Finding 1 — induced K₄−e count is identically 0 family-wide (CHECKED, and it is a proof)

GOAL.md lists "a counting identity in the number of induced C₅, C₆, or **K₄−e**"
as a candidate structural lever. The previous four rounds tabulated C₅, C₆,
triangles, outer blocks, distance-2, coclique bounds — but never K₄−e. I computed it:

| graph | 4-subset edge-count histogram (edges → #subsets) | max edges | K₄−e (5-edge) | K₄ (6-edge) |
|---|---|---|---|---|
| rook(3) srg(9,4,1,2) | {2:45, 3:36, 4:45} | 4 | **0** | **0** |
| BvLS srg(243,22,1,2) | {0:79708860, 1:48354570, 2:12095325, 3:1496880, 4:66825} | 4 | **0** | **0** |

Exact integer count over every C(n,4) subset using the adjacency matrix, entry
guarded by both controls passing `lib.srg.is_srg`. **Both controls have zero
5-edge and zero 6-edge 4-subsets — no diamond and no K₄.**
(`code/out/…` command run this round; input `lib.srg.rook(3)`, `lib.srg.bvls_graph()`.)

**Structural reason (a proof, not just a count):** an induced K₄−e is exactly two
triangles sharing a common edge. But λ=1 means every edge lies in a *unique*
triangle, so no edge is in two triangles — hence the induced K₄−e count is **0 for
every member of the srg(v,k,1,2) family**, including the putative (99,14,1,2).
Equivalently, the family is diamond-free and K₄-free (consistent with ω=3 for λ=1).

**Bearing:** this closes the last counting quantity GOAL.md names. The K₄−e lever
is degenerate family-wide and **cannot** separate 99 from the controls 9 and 243 —
it is the kind of identity that is refuted on arrival (it rejects nothing). It adds
nothing to the n₃/hexagon axis or to the coclique-design branch. This is a negative
result, recorded so no later pass spends effort deriving a K₄−e count for 99.

## Finding 2 — the eigenvalue-multiplicity sequences, formally run through the tools

The two multiplicity sequences from `code/out/derived_design_sequences.py`
(f(r) and g(s), the eigenvalue multiplicities):

```
f(r): 4, 54, 132, 3280, 250914
g(s): 4, 44, 110, 2992, 243104
```

`analyze_sequence` over these exact terms: neither is a low-degree polynomial
(differences do not stabilise; leading ratios grow 13.5→76.5 and 11→81.3), both are
even, residues mod 2 have period 1. `find_linear_recurrence(order ≤ 4)`: **no
constant-coefficient linear recurrence of order ≤ 4 fits either sequence.**
This matches every other family sequence (triangles, pentagons, hexagons, outer
blocks, distance-2, multiplicities): all are the quartic-in-`u` closed forms from
`k = u²+u+2`, `v = 1+k²/2`, `a = 2u+1 | 63` — a polynomial in `v,k` with quintic
growth, which no low-order constant-coefficient recurrence fits. Confirms the
report-4/3/2/1 catalogue: **no independent hidden law; all governed by the a|63
integrality mechanism.**

## Sequences with no further structure (re-confirmed exactly)

As in rounds 1–4, over exactly the terms supplied, `analyze_sequence` /
`find_linear_recurrence` find no order-≤4 linear recurrence and no low-degree
polynomial fit for:

- Triangles `{6, 231, 891, 117096, 81842481}`
- Pentagons `{0, 33264, 384912, 1669320576, 96451036488576}`
- Hexagons `{6, 209286, 4980690, 146767540920, 79371206037594576}`
- Outer blocks `{0, 140, 660, 110880, 81348960}`
- Distance-2 counts `{4, 84, 220, 6160, 493024}`
- Coclique bounds `{3, 22, 45, 561, 15408}`
- Multiplicities f `{4, 54, 132, 3280, 250914}`, g `{4, 44, 110, 2992, 243104}`

All are exactly the quartic-in-`u` closed forms; none has an independent law; the
OEIS misses were recorded in prior rounds.

## First falsifying terms

- **K₄−e count = 0:** is a *proof* (λ=1 ⇒ every edge in a unique triangle ⇒ no
  edge in two triangles ⇒ no K₄−e), so it cannot be falsified by more terms of the
  family; it would be falsified only by a non-λ=1 setting, which is outside the
  family. The honest statement is that the count has a first-falsifying-vacuity:
  it inherits from λ=1, so it is not a 99-structural fact at all.
- **Multiplicity/etc. closed forms:** fit is not the basis — each is derived from
  `k=u²+u+2`, `v=1+k²/2`, `s=−(u+1)`, `a|63`, and independently verified by
  enumeration on both existing graphs as far as the family reaches. They would be
  falsified only by a sixth feasible member with different `u`-arithmetic, which
  the `a|63` integrality excludes. So "first falsifying term" is empty for these —
  the honest statement.

## Bearing on the phase-4 target (n₃)

None of the family-count sequences — including the now-closed K₄−e lever — bears
directly on the open question *"is n₃ ≥ 1 forced for a putative (99,14,1,2)?"*.
Both controls have n₃=0 (checked in `n3_deduction_check.py`, confirmed two ways)
and exist; Makhnev 1988 Thm 2 is the sourced conditional that n₃=0 ⇒ no
srg(99,14,1,2). The family-count catalogue being complete means the phase-4 target
must be attacked structurally (a counting argument in the 84/140/5 outer partial
STS, or a coclique-design argument at 22), not by finding a new parameter-determined
sequence — every parameter-determined count is the same quartic family and none
separates 99.
