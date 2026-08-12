# Boyer, "Supplement to Some Notes on the Magic Squares of Squares", 2005

[[boyer-notes-supplement-2005]]

Supplement listing Lucas's 3×3 semi-magic squares-of-squares family (6 or 7 magic lines) and
Euler's 4×4 magic squares of squares, with complete small listings.

## Established statements
- **Lucas 3×3 semi-magic family** (rows and columns sum to `S²=(p²+q²+r²+s²)²`):
  ```
  (p²+q²−r²−s²)²  [2(qr+ps)]²   [2(qs−pr)]²
  [2(qr−ps)]²     (p²−q²+r²−s²)²  [2(rs+pq)]²
  [2(qs+pr)]²     [2(rs−pq)]²   (p²−q²−r²+s²)²
  ```
  Complete list with distinct entries and magic sum ≤ 100²: (1,2,4,6) 57², (1,2,3,7) 63²,
  (2,3,4,6) 65², (1,3,5,6) 71², (1,2,5,7) 79², (2,4,5,6) 81², (1,2,4,8) 85², (1,4,5,7) 91²,
  (2,3,4,8) 93², (1,3,6,7) 95², (1,3,5,8) 99², (3,4,5,7) 99².
  With 7 magic lines and sum ≤ 2000²: (1,3,4,11) 147² (=**MS1**, which is the LS1 square!),
  (3,5,8,14) 294², (4,9,11,17) 507², (2,6,8,22) 588², etc.
- **Key fact:** LS1 belongs to this Lucas family ((1,3,4,11) → 147²). So the Parker/LS1
  near-miss is not *ad hoc* but a low member of Euler/Lucas's 3×3 semi-magic parametrisation.
- **Euler 4×4** family with both diagonals, sum `(a²+b²+c²+d²)(p²+q²+r²+s²)` under two extra
  conditions; small examples listed (CB1 = 3230, etc.).

## Implications for this run
- The LS1 witness is a member of the Lucas family: this ties problem (A)'s best near-miss to
  a 4-parameter construction. Useful context but does not bear on the 9-square-over-Q
  impossibility.
- The 7-line (hence 7-of-8-sums) members of the family are exactly the "squared square"
  near-misses; no 8/9-of-8-sums member appears in the small listings.

## Assessment
- Valuable as the source placing LS1 in the Lucas family and giving the complete small census
  of the semi-magic family. No impossibility content.

```claim
id: ls1-in-lucas-family
statement: Sallows' LS1 (7 of 8 sums = 147²) is the (p,q,r,s)=(1,3,4,11) member of Lucas's 3x3
  semi-magic family, magic sum 147².
hypotheses: the Lucas parametrisation; (1,3,4,11) square
holds-here: yes (checked: 147²=21609)
status: catalogued
bearing: ties the Parker witness to a structured parametrisation; no bearing on full impossibility
anchor: research/sources/boyer-notes-supplement-2005.full.md
```
