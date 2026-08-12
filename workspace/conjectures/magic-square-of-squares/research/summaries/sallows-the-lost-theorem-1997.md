# Sallows, "The Lost Theorem", Math. Intelligencer 19.4 (1997) 51–54

[[sallows-the-lost-theorem-1997]]

Origin of the LS1 near-miss (the "Parker square" / squared-square witness this run carries)
and a structural theorem about 3×3 magic squares via parallelograms.

## Established statements

**LS1.** A squared square with all rows, all columns, and *one* diagonal summing to the same
number, itself a square `147²`; the other diagonal fails. This is the 7-of-8-line-sums witness
(the run's Sallows LS1). In Sallows' notation:
```
58² 46² 127²
94² 113²  2²
97² 82²  74²
```
(the user's `[127,46,58;2,113,94;74,82,97]` is its transpose; squares identical).

**Theorem (parallelogram correspondence).** To every parallelogram on the plane there
corresponds a unique equivalence class of 8 complex 3×3 magic squares, and conversely. Every
3×3 magic square contains eight 3-term APs (4 through the centre, 4 on the pandiagonals),
which correspond to the 4 edges and 4 bisectors of the parallelogram.

**Atomic square.** The canonical magic square with the nine smallest Gaussian integers:
```
−1−i  1−i  1+i
 1−i  0   −1+i
 1+i  −1+i −1−i
```
(sum 0), the a=b=1, c=0 case of Lucas's formula; a perfect "equal-side, equal-angle"
parallelogram (a square) gives a non-degenerate complex magic square.

## Implications for this run

- Confirms the standard parametrisation and the eight-AP structure.
- The LS1 grid is one of the two mandatory near-miss witnesses (7-of-8 sums). Any
  impossibility lemma must not forbid it.
- The parallelogram/8-complex-square correspondence is structural but does not bear on the
  arithmetic square problem (no new diophantine constraint); the real content for this run
  is the witness and the AP census.

## Does not help

The parallelogram theorem is a beautiful classification of *structure* but gives no new
obstruction to all-nine-squares-over-Q; it is the geometry behind the AP census already in
the parametrisation. Low value for the impossibility goal beyond the witness value.

```claim
id: ls1-witness
statement: Sallows LS1: rows, columns and one diagonal all sum to 147²=21609; the other
  diagonal sums to 38307; all nine entries are distinct squares.
hypotheses: none (explicit grid)
holds-here: yes (reproduced exactly by this run, code/out/near_misses.json)
status: checked
bearing: mandatory near-miss witness; the falsifier for every impossibility lemma
anchor: research/sources/sallows-the-lost-theorem-1997.full.md
```
