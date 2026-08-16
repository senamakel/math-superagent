# Pattern-finder report: sequences and structure in the run's computed ES data

## 1. THE disambiguation gap is resolved: es_construct.es_set is a CORRECT ES construction

The run's CONTEXT.md recorded a live gap: the ES lower-bound construction fails its own
property (largest convex subset too large) and it was unresolved which part was wrong.
Working on the correct `es_construct.es_set` (`code/lib/es_construct.py`):

| n | \|S\| | general position | largest convex subset | want | verdict |
|---|---|---|---|---|---|
| 4 | 4 | True | 3 | 3 | PASS |
| 5 | 8 | True | 4 | 4 | PASS |
| 6 | 16 | True | 5 | 5 | PASS |
| 7 | 32 | True | no convex 7-gon | none | PASS |

Verified with the exact es_geom oracle (`out/verify_es_construct.py`) **and** independently
with a from-scratch gift-wrapping hull over all subsets (`out/verify_es_construct_indep.py`):
two different algorithms agree on every value. General position checked by raw cross products.

So: the checker (es_geom) is correct AND `es_construct.es_set` is a valid 2^{n-2}-point
no-convex-n-gon realization. The broken ones are `es_lower_set` (integer, es_construction.py:
rounding introduces collinearities at n>=5) and `es_set` (rational, esz.py: largestConvex 6 at
n=5, 9 at n=6). Any later structural argument may now be measured against `es_construct`.

## 2. The square ES threshold: a(n) = 2^{n-2}+1 is A000051

`3, 5, 9, 17, 33, 65, 129, 257` (ES(3..10) conjecture).
- Constant-ratio: leading ratio -> 2; equidivisible by... every term odd.
- `find_linear_recurrence` (order 2): a(n) = 3a(n-1) - 2a(n-2), reproduces all 8 terms.
- Closed form a(n)=2^{n-2}+1 is the catalogued A000051. So ES(n)=2^{n-2}+1 has the exact
  linear recurrence a(n)=2a(n-1)-1. This is a *conjecture* (only terms 3..6 are proved
  values; 7..10 are the conjecture itselt), not a proof.

## 3. The cups/caps threshold f(k,k) is OEIS A323230

`2, 3, 7, 21, 71, 253, 925, 3433` (k=2..9), f(k,k)=C(2k-4,k-2)+1.
- OEIS A323230: a(n) = C(2(n-1),n-1)+1 with n=k-1. Verified exact match for k=2..9.
- The DP F(k,l)=C(k+l-4,k-2) obeys the Pascal recurrence F(k,l)=F(k,l-1)+F(k-1,l),
  verified exactly for all k,l in 2..6.
- This is the function behind the 1935 bound ES(n) <= f(n,n) = C(2n-4,n-2)+1.
- NOTE: the order-4 "recurrence" the tool fit on these terms (a(n)=39/5 a(n-1) - 187/10
  a(n-2) + ...) has arbitrary rational coefficients and is a meaningless fit — binomial
  coefficients are NOT linearly recurrent. Do not cite it.

## 4. Structural finding: the even/odd block split of the extremal construction

The ES construction X_n has blocks T_0..T_{n-2}, |T_i| = C(n-2,i). Split into even and
odd index groups. Verified exactly (n=5,6,7):

- each group has size sum_{i even} C(n-2,i) = 2^{n-3}  (exact binomial identity, m=1..8);
- each group has NO convex (n-1)-gon.

So each half is a 2^{n-3}-point set with no convex (n-1)-gon — i.e. an extremal-size
ES(n-1)-type avoiding set. This is exactly the recursion step the G-split induction
goal needs: |X_n| splits into two (n-1)-avoiding blocks of size 2^{n-3}, each the
maximum possible size for avoiding an (n-1)-gon. It confirms G-split-consistent on the
trusted construction.

Caveat (checked): in this particular radial placement the two halves are NOT strictly
straight-line separable (searched all lines through point pairs). A valid separating-line
placement does exist by the literature (radial placement with increasing polar angle), so
this is a property of es_construct's coordinates, not a refutation of G-split.

## Non-findings (recorded so nobody re-derives)

- Convex-layer sizes [3,1], [4,4], [5,5,3,3], [6,6,6,5,6,3] (hull peeling) show no clean
  sequence; they're an artifact of this specific radial placement. Not reported as structure.
- The whole-set cup/cap spectrum of es_construct (cup=3,4,5 and cap=2,2,2 for n=4,5,6) is
  dominated by the block structure and carries no independent regularity.
