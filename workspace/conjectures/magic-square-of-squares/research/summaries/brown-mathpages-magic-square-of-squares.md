# Brown (MathPages), "Magic Square of Squares", kmath417

[[brown-mathpages-magic-square-of-squares]]

A recreational but careful page. Confirms the structure: the common sum `S = 3E` with `E`
the central number, each row/column/diagonal through the centre is an AP, and every 3×3 magic
square is parametrized by `n=E`, `m=C−E` (equivalently the run's `(c,u,v)`).

**Proposition 1.** Any square whose elements satisfy the central (four-through-centre) sums
and whose central number is expressible as a sum of two squares in **no more than four distinct
ways** will *not* give the required sums for the outer rows and columns.

## Implications / assessment
- Proposition 1 is a genuine small partial result: a MSS needs the centre to be a sum of two
  squares in *at least five* distinct ways. This matches the run's observation that Bremner's
  centre `425²` has the Pythagorean decompositions 385²+180² and 408²+119² (both endpoints of
  two AP-differences square). This is an elementary bound on the multiplicity of the centre's
  two-square representations.
- It is a *necessary* condition of limited strength (five representations are easy to have);
  not a path to non-existence by itself.
- Restates (no proof of) the general problem.

## Does not help for the impossibility goal beyond Prop. 1
- The "no more than four ways ⇒ no solution" bound. The companion orthomagic page
  (kmath427) generalises this to the orthomagic framing; see that note.

```claim
id: centre-five-representations
statement: A 3x3 magic square of squares whose centre is a sum of two positive squares in at
  most 4 distinct ways is impossible.
hypotheses: distinct square entries; centre's two-square representation count ≤ 4
holds-here: yes (a real MSS centre would need ≥5)
status: asserted (Brown's page; no refereed proof cited)
bearing: elementary necessary condition; weak alone but sharpens where a descent must look
anchor: research/sources/brown-mathpages-magic-square-of-squares.full.md
```
