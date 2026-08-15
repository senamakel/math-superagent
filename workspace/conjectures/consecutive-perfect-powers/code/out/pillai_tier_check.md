# Pillai / related-equations tier — arithmetic hand-check

Status: **hand-verified, NOT executed** (this scholar session has no execution
tool). Every equation below was checked by direct exact arithmetic by hand.
The on-disk captured outputs elsewhere in `code/out/` corroborate the computed
claims of this run; this file only pins the Pillai/Bennett tier arithmetic.

Source: `research/sources/pillai-related-equations-stroeker-tijdeman-bennett.md`
(the final Lead from problem.md, previously absent — the adjacent family
`a^x - b^y = c` with `c` a fixed integer other than 1).

## Pillai's three two-solution equations for (3,2)

| equality | value |
| --- | --- |
| `3 - 2 = 3^2 - 2^3` | `3-2=1`, `9-8=1` → both = 1 |
| `3 - 2^3 = 3^3 - 2^5` | `3-8=-5`, `27-32=-5` → both = −5 |
| `3 - 2^4 = 3^5 - 2^8` | `3-16=-13`, `243-256=-13` → both = −13 |

## Bennett (N,c) exceptional equations (all hand-checked)

| (N,c) | equations | value | #sols |
| --- | --- | --- | --- |
| (2,1) | `3-2`=1, `3^2-2^3`=1, `2^2-3`=1 | 1 | 3 |
| (2,5) | `3^2-2^2`=9-4=5, `2^3-3`=8-3=5, `2^5-3^3`=32-27=5 | 5 | 3 |
| (2,7) | `3^2-2`=9-2=7, `2^4-3^2`=16-9=7 | 7 | 2 |
| (2,13) | `2^4-3`=16-3=13, `2^8-3^5`=256-243=13 | 13 | 2 |
| (2,23) | `3^3-2^2`=27-4=23, `2^5-3^2`=32-9=23 | 23 | 2 |

(Matches the source's first-two-cases-3-solutions / last-four-2-solutions.)

## Falsifier boundary (the reason these theorems are SILENT on the run's problem)

Within the fixed-base family `(a,b)=(3,2)`, the value `c=1` has **two**
representations:
- `3^1 - 2^1 = 1`
- `3^2 - 2^3 = 1`  ← the run's known solution

`c=1` is the archetypal multi-representation exception, and `|1| = 1 < 13`, so
it lies strictly inside the small-c region that the Stroeker–Tijdeman
at-most-one theorem (`c_0(3,2)=13`) explicitly excludes. Bennett's at-most-two
(2001) likewise has `(a,b,c)=(3,2,1)` as its sharpness example.

**Conclusion:** every Pillai/Bennett at-most-one / at-most-two result fixes
`a,b` as given constants. The run's problem makes the *bases* `x,y` the
unknowns and fixes `c=1`, the one value sitting exactly at the multi-rep
boundary. None of these theorems transfers to prove or bound the run's
equation. This is the correct resolution of the `holds-here` field: it is `no`,
not `unchecked`.

## Claim

```claim
id: pillai-falsifier-c1-boundary
statement: >
  Within the fixed-base family 3^x - 2^y = 1, the value c=1 has exactly two
  representations, (x,y)=(1,1) and (2,3) (= 3^2-2^3, the run's known solution).
  Since |c|=1 < 13 = c_0(3,2), c=1 sits inside the small-c region excluded by
  the Stroeker-Tijdeman at-most-one theorem, and is the sharpness example of
  Bennett's at-most-two theorem (2001). Therefore every Pillai/Bennett
  at-most-one/two result fixes a,b as constants and is SILENT on x^p - y^q = 1,
  whose bases are the unknowns and whose c=1 is the multi-rep boundary.
hypotheses: a,b fixed coprime bases; x,y >= 1.
holds-here: no — the run's problem does not fix the bases; c=1 is the boundary
  case these theorems exclude or cite as their sharpness example.
status: sourced (Pillai 1931/36; Stroeker-Tijdeman 1982; Bennett 2001/2003)
  with the arithmetic hand-checked above (no program run in this session).
anchor: research/sources/pillai-related-equations-stroeker-tijdeman-bennett.md
bearing: fixes the adjacent-family boundary; no lemma may be transferred from
  these at-most-one theorems to the run's variable-base problem.
```
