# Approach: genus computation for C(x,k1)=C(y,k2) — deliverable and obstruction

## Claim under test (GOAL.md deliverable)

Compute the genus `g(k1,k2)` of the plane curve `C(x,k1)=C(y,k2)` symbolically,
find where it crosses 1, and make explicit the threshold above which Faltings applies
("finitely many rational points"). This is a finite algebraic-geometry computation:
defined degree, singularities via the Gröbner basis of the partial derivatives, then
the genus-degree formula.

## Why this is the honest part of the Diophantine program

- It does NOT scale with any problem bound: for each small `(k1,k2)` it is a fixed
  symbolic computation. So it satisfies method rule 4 (cost grows with description,
  not with the bound).
- It is one of the four partial results GOAL.md explicitly lists as a deliverable.
- Sources in the library support the pattern: de Weger found `(3,4)` has genus 3
  (Faltings applies) and it is a double cover of the Mordell curve `Y^2+Y=X^3-X`;
  Jenkins computed `(2,2)` ("a=b=2") genus 3 by Gröbner basis and showed no affine
  singularities, so `g=(d-1)(d-2)/2 = 3`.

## The obstruction that blocks turning genus into a uniform bound

Genus>1 for fixed `(k1,k2)` gives finiteness per pair via Faltings — already known,
and INEFFECTIVE (no count computable in the parameters). The same for Siegel at
genus 1. Neither yields a number uniform in `(k1,k2)`. So the genus computation
supplies the threshold (a fact about where Faltings applies) but NOT a uniform bound.
An effective uniform bound would need a general effective Siegel or effective
Schmidt subspace theorem — out of reach.

## What a bigger run would settle / next steps

1. Compute `g(k1,k2)` for small pairs (say k1,k2 <= 6) with sympy: define the curve,
   compute partials, Gröbner basis, singularity count, genus-degree formula.
2. Cross-check Jenkins's (2,2) genus 3 and de Weger's (3,4) genus 3 against the
   computation (both are in the library as primary sources).
3. State precisely: for which (k1,k2) is g>1 (Faltings applies with finiteness only),
   where the curve stays genus 1 (Siegel finite integral points, still ineffective),
   and note that uniformity in (k1,k2) is NOT attained — this is the honest
   partial result: the genus function plus the explicit statement that it does not
   yield a uniform bound.

## Status

Open/proposed. Not yet executed — needs tool_builder/coder to run the sympy genus
computation. Recorded here so the run can pick it up and so the obstruction is on
record before any claim of a uniform bound is made.

## Falsification

If the genus computation shows g<=1 for a wide range of (k1,k2) — i.e. the curves
stay genus 0/1 much longer than expected — then Faltings does NOT apply and the
Diophantine route's premise (genus grows with the parameters, crossing 1) is wrong
for that range; the computation would refute the "genus grows and crosses 1" claim.
Run the computation to find out.
