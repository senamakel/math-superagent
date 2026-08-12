# Boyer, "Supplement: Some Notes on the Magic Squares of Squares Problem" (2005) — [[boyer-notes-supplement-2005.full]]

Boyer's supplement to his Mathematical Intelligencer survey. Content is almost entirely about **larger order** and **other** problems, not the 3×3 target:
- Lucas's 3×3 **semi-magic** squares of squares (rows and columns equal, diagonals not): parametrisation with (p,q,r,s), magic sum S2 = (p²+q²+r²+s²)². Lists all (p,q,r,s) giving 6 magic lines with sum ≤100², and 7 magic lines with sum ≤2000² (e.g. (1,3,4,11) → 147² = the LS1 near-miss; (3,5,8,14) → 294²; …). These are **near-misses of variant (A)** (7 of 8 line sums), not magic squares.
- Euler's 4×4 magic squares of squares (rows, columns and diagonals equal): parametrisation with (a,b,c,d,p,q,r,s), magic sum S2 = (a²+b²+c²+d²)(p²+q²+r²+s²)², two extra conditions for the diagonals. Lists the family ≤10000 (CB1, CB15…).
- Prime-number magic squares of order 4 and 5 (CB16, CB17, CB18) and bimagic/cube-of-primes open problems.

**Bearing on the 3×3 problem: marginal.** Confirms only the existence of the LS1 near-miss (7 of its 8 line sums equal), already in the witness set, and provides Lucas's family from which LS1 comes. The 4×4 and 5×5 material does not bear on the 3×3 hard case. The 3×3 semi-magic family is nonetheless useful context: it shows the difficulty is specifically making the *two diagonals* also equal, i.e. the diagonal/centre-line constraint, not the row/column constraint.

**Does not help** the primary question beyond confirming what the 3×3 problem reduces to (lines versus diagonals). Useful as a source for the Lucas family that produces LS1 and for the historical Euler 4×4.

```claim
id: lucas-family-lines
statement: Lucas's (p,q,r,s) family gives 3×3 semi-magic squares of distinct squares with
  all 3 rows and 3 columns equal (sum (p²+q²+r²+s²)²); it produces examples with 6 or 7 lines
  equal, e.g. (1,3,4,11)→147² (the Sallows LS1 near-miss). The diagonals are the obstruction:
  making them also equal is what the hard 3×3 problem demands.
hypotheses: semi-magic (rows+columns) 3×3; distinct entries
holds-here: yes
status: catalogued (term lists in-source)
bearing: places LS1 in Lucas's family; isolates that the open problem is forcing the two
  diagonals to also match, i.e. the through-centre AP differences to be additive-coupled
anchor: research/sources/boyer-notes-supplement-2005.full.md
```
