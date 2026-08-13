# Thread: Diophantine curve C(x,k1)=C(y,k2) and effective genus/height

## Question

Can the family of curves `C(x,k1)=C(y,k2)` (equivalently Jenkins' `C(x,y)=C(x-a,y+b)`)
yield a bound on `N(a)` that is *uniform* in `(k1,k2)`, with an *effective* constant —
or can we at least prove an effective bound for a specific small-`(k1,k2)` family,
or name the obstruction that makes a uniform effective bound impossible?

## Rest on

- For each fixed `(k1,k2)` the equation is an algebraic curve; genus grows with the
  parameters, Faltings (genus>1) and Siegel (integral points even at genus 1) give
  finiteness for each pair — **but with no count computable in the parameters**
  (ineffective). This is the uniform-in-`k` obstruction.
- Jenkins (arXiv:1411.4111) reformulated `C(x,y)=C(x-a,y+b)` as the curve
  `prod_{r=0}^{a+b-1}(x-y-r) = prod_{p=0}^{a-1}(x-p) prod_{q=1}^{b}(y+q)`.
  He proved finiteness for `a != b` (via non-quadratic limiting ratio, not via genus),
  and left `a=b` (golden-ratio quadratic) open — that is exactly the Singmaster family.
- de Weger (JNT 63 (1997)): `(k,l)=(3,4)` curve has genus 3 (Faltings applies), is a
  double cover of the elliptic curve `Y^2+Y=X^3-X`; all integral points found.
  Small `(k,l)=(2,3),(2,4)` solved by Avanesov / de Weger-Pinter (elliptic, rank 2).
- GOAL.md defines oracles: `genus(k1,k2)` and `multiplicity(a,n_max)`; the falsifier
  is 3003 (8 occurrences), so a bound `<8` is refuted.

## What a bigger run would settle

Computing `genus(k1,k2)` for the concrete family, and finding where it crosses 1, is
a finite algebraic-geometry computation (Gröbner basis / singularity count) — it does
NOT scale with any problem bound and so is the honest part of the Diophantine program.
That is the deliverable GOAL.md explicitly lists ("genus of C(x,k1)=C(y,k2) computed
as a function of k1,k2, threshold above which Faltings applies made explicit").

## Blocked by

- Linking genus growth to a uniform bound requires the ineffective constants to be
  removed — precisely the "finiteness is not a bound" trap.
- An effective Baker-type height bound is triple-exponential and too large to use.

## Next

1. Have tool_builder compute `genus(k1,k2)` for small pairs symbolically (sympy):
   defined curve, singularity count via Groebner of the partials, genus-degree formula.
2. Have the scholar confirm GOAL's candidates against de Weger's (3,4) genus-3 result
   and Jenkins' (2,2) genus-3 computation (both in the library).
3. Open `research/approaches/` proposal documenting which of the four GOAL deliverables
   the genus computation actually delivers, and the uniform-bound obstruction.
