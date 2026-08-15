# Kempe universality: the construction technique behind Maehara's converse

**Subject:** The classical linkage-construction machinery that underlies the
*constructive* half of Maehara's theorem (the direction the run's exact
coordinate constructions ultimately rely on: any algebraic number occurs as a
distance between vertices of a rigid unit-distance graph). This is technique
tier, not the published answer to `problem.md`.

**Source URLs (retrieved via search passages):**
- A.B. Kempe, *On a general method of describing plane curves of the nth degree
  by linkwork*, Proc. London Math. Soc. s1-7 (1875) 213–216, DOI
  10.1112/plms/s1-7.1.213 (Zenodo record 1447760, CC0).
- S.C. Power, *Elementary proofs of Kempe universality*, Math. Proc. Royal Irish
  Academy 117A (2017), DOI 10.3318/pria.2017.117.04.
- T.G. Abbott, *Generalizations of Kempe's universality theorem* (M.Eng. thesis,
  MIT 2008), http://hdl.handle.net/1721.1/44375.

## Exact content

**Kempe's universality theorem (original form).** Any plane algebraic curve —
the zero set in the plane of a real polynomial — can be traced by a finite
pinned planar linkage (a finite set of rigid bars joined at revolute joints).

**The mechanism.** Kempe builds linkages from four "computing" gadgets —
the *additor* (adds angles), *reversor* (negates/reflects an angle), and
*multiplicator* (multiplies an angle) — so that the endpoints of a two-bar
serial chain are constrained to trace a prescribed algebraic locus. Abbott gives
a corrected, simpler proof using a *contraparallelogram* bracing; Power gives
elementary proofs and notes the uniform-bounded-valency infinite version.

**Why it applies here.** Maehara's converse — every positive algebraic number
d occurs as a distance between two vertices of some rigid unit-distance graph —
is proved by realising a rational-coefficient coordinate system via linkages of
this Kempe type, then "tightening" them into a unit-distance graph whose
distances are algebraic. So the exact algebraic-coordinate machinery the run
uses is the modern incarnation of Kempe's constructions: multiply, divide, and
reflect angles/distsances to force prescribed algebraic coordinates while
keeping every edge at length exactly 1.

**Boundary.** Kempe universality is about *tracing curves*, not about colouring;
it does not and cannot contribute a chromatic-number statement. It is recorded
only as the constructive backbone of the algebraic-rigidity claim, which is
itself a technique claim backing the exact-arithmetic discipline.

## Basis and status

- Statement and mechanism corroborated by the original 1875 paper record and two
  independent modern treatments (Power 2017; Abbott 2008). Standard, accepted.
- Not re-derived here; recorded as the sourced technique behind `maehara-algebraic-rigid-distances`.

## Claim block

```claim
id: kempe-universality
statement: Every plane algebraic curve (zero set of a real polynomial) can be
  traced by a finite pinned planar linkage; Maehara's converse — every positive
  algebraic number is a rigid-unit-distance-graph distance — is proved through
  this Kempe-style construction machinery.
hypotheses: plane algebraic curves; rigid planar bars at revolute joints;
  coordinates built from algebraic field operations (add, negate, multiply).
holds-here: YES — it is the construction technique that justifies "exact
  algebraic coordinates suffice to realise arbitrary algebraic distances", the
  foundation of the run's coordinate machinery.
status: asserted-by-source (Kempe 1875; Power 2017; Abbott 2008).
bearing: technique backbone of the exact-coordinate machinery; explains why
  rigid unit-distance constructions can be carried out in finite algebraic
  extensions rather than needing transcendental coordinates.
anchor: research/sources/kempe-universality-linkages.md
falsifies: an algebraic number provably not realisable as a rigid-unit-distance
  distance — none known (Maehara's theorem asserts all are).
```
