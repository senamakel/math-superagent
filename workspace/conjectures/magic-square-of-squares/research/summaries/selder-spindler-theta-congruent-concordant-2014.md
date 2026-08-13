# Selder & Spindler, "On θ-congruent numbers, rational squares in arithmetic progressions, concordant forms and elliptic curves" (2014)

**Source:** arXiv:1408.1522v2 [math.NT], 22 Aug 2014 (v1 7 Aug 2014). Full text at
`research/sources/selder-spindler-theta-congruent-concordant-2014.html.full.md`.
Published form: *Mathematics* 3(1), 2015, 2–15 (MDPI, 403 on direct download; arXiv is the access).

## Authors' project

They unify, in one bijective framework, four classical objects:
**concordant quadratic forms**, **rational squares in arithmetic progressions** (not
necessarily consecutive), **θ-congruent numbers** (rational triangles with a fixed
angle θ), and **rational points on elliptic curves** E(m,n): y² = x(x+m)(x+n).
The paper's contribution over earlier treatments ([Ono, Fermat's concordant forms;
Fujiwara; Koblitz]) is that the correspondence Q(m,n) → E(m,n) is a *true
isomorphism*, not the degree-4 map to the doubled subgroup 2E used classically. That
defect mattered: with the degree-4 map, 4-torsion points collapse to 2-torsion in the
image and legitimate concordant-form solutions are lost.

## Key statements (with the exact hypotheses)

**Definition (concordant forms).** X² + mY² and X² + nY² (m ≠ n nonzero) are
*concordant* iff X² + mY² = Z², X² + nY² = W² has a nontrivial solution (Y ≠ 0; trivial
solutions are (1,0,±1,±1)). WLOG m < 0 < n, write m = −pk, n = qk, (p,q) coprime, k
squarefree. A triplet (p,q,k) is a *solution of the concordant form problem* iff there
is a 3-term AP of rational squares of maximal step k whose low/high ends are separated
from the middle by pk and qk respectively. **This is exactly the structure of each
three-term AP of squares through the MSS centre**: middle β²=e², ends α²,γ² with
α² = e²−d, γ² = e²+d gives p,q,k with pk=qk=d, i.e. p=q=1, k=d.

**Theorem 2.2.** X²+mY², X²+nY² concordant ⟺ E(m,n) has a rational point of order > 2
(finite or infinite).

**Theorem 3.1 (complete torsion classification).** For m = −pk, n = qk, (p,q)=1, k
squarefree:
- (i) order-4 points ⟺ −m and n−m are squares, say −m = u², n = v²−u².
- (ii) order-8 points ⟺ ∃ coprime ξ,η with ξ²+η²=ζ² and m = −ξ⁴, n = η⁴−ξ⁴.
- (iii) order-3 (equiv. order-6) points ⟺ ∃ coprime a,b with the generic conditions and
  m = a³(a+2b), n = b³(b+2a).

**Theorem 3.3.** If torsion T ≅ Z/2×Z/4 or Z/2×Z/8 then k = 1; if T ≅ Z/2×Z/6 then
k = 1 or 3. (So non-trivial torsion concordance forces the step to be essentially 1.)

**Theorem 4.7.** For a rational point P on E(m,n) (m=−pk, n=qk coprime/squarefree k)
with associated 3-square AP triplet T: P has order four ⟺ T contains 0 ⟺ the
associated θ-triangle is isosceles.

**Theorem 4.8.** An isosceles rational θ-triangle exists ⟺ sin(θ/2) ∈ Q, with explicit
sides a,a,c = 2a·sin(θ/2) and k = 1 or 2.

## Bearing on the 3×3 magic square of squares

This is the primary source that answers the *concordant-forms / congruent-numbers /
four-AP* question that `problem.md` names as one to settle early.

- **Yes, the four-AP condition maps onto concordant forms.** Each of the four lines
  through the MSS centre (differences u, v, u+v, u−v) is a 3-term AP of squares
  α², e², γ² and is therefore a concordant-form problem for (m,n) = (−d, d), i.e. p=q=1,
  k=d, on the curve E(−d,d): y² = x(x−d)(x+d) = x³−d²x — the **congruent-number curve**
  for d. So each satisfied AP is equivalent to a rational point of order > 2 on the
  congruent-number curve E_{−d,d}. This is precisely the run's already-established
  `phi-universal-set`/`simultaneous-congruent-numbers` identification, but now anchored
  to a complete published torsion classification.
- **Order-4 meaning for an MSS AP.** The satisfied-difference APs in Bremner's witness
  (d=v=138600, d=u+v=97104 with e=425²=385²+180²=408²+119², d=2xy of Pythagorean pairs)
  correspond, under Theorem 4.7, to information about whether the associated congruent
  curve point has order 4 — i.e. whether the 3-square AP contains 0 (α=0), equivalent to
  the θ-triangle being isosceles. This gives a concrete torsion-meaning to the run's
  structural finding that exactly two of the four differences are fully realised.
- **The additive relation is NOT in this source.** The four differences u,v,u+v,u−v are
  additively linked; a single AP-of-squares only uses one difference. Nothing in this
  paper addresses the constraint that the four steps share one middle term *and* are
  additively linked. So the concordant-form dictionary is necessary context, not an
  obstruction.

## What this library now can and cannot claim from this source

- `Concordant forms ↔ rational points of order > 2 on the congruent curve` — *sourced
  (proved)*.
- `Order-4 torsion ⟺ the AP contains 0 ⟺ isosceles triangle` — *sourced (proved)*.
- `For a single MSS AP-difference, curvature reduces to the classical congruent-number
  curve E(−d,d)` — *this is the standard identification, matches `phi-universal-set`
  (checked by this run, exact).* This source is the citation for the concordant-forms
  direction, not the MSS obstruction.
