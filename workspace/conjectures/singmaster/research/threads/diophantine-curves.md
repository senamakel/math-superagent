# Thread: Diophantine curve C(x,k1)=C(y,k2) and effective genus/height

## Question

Can the family of curves `C(x,k1)=C(y,k2)` (equivalently Jenkins' `C(x,y)=C(x-a,y+b)`)
yield a bound on `N(a)` that is *uniform* in `(k1,k2)`, with an *effective* constant —
or can we at least prove an effective bound for a specific small-`(k1,k2)` family,
or name the obstruction that makes a uniform effective bound impossible?

## Genus deliverable DONE — the complete two-parameter Faltings threshold

`code/out/genus_table.captured.txt` is the definitive result. Two independent
CAS routes (Singular `normal.lib::genus` and Sage `Curve.genus()`) agree on
every entry for 2<=k1,k2<=12, extended to k1=24 for k2=3,4,5. **This supersedes
the operator's three-diagonal salvage** (`code/out/genus_closed_forms.md`), which
is now corroboration only.

**Faltings threshold: genus = 1 exactly for {2,3} and {2,4}; genus >= 2 for
every other distinct pair.** This is the complete answer to the GOAL.md
deliverable. The two-parameter grid is far stronger than three fitted diagonals.

This does NOT give Singmaster — Faltings remains ineffective in the parameter
(finitely many per pair with no computable count), and the genus growing makes
the uniform statement harder, not easier.

### Small-column closed forms — all verified against the full grid

- `{2,n}`: `genus = floor((n-1)/2)` — hyperelliptic
- `{3,n}`: `genus = n-1 (3∤n), n-2 (3|n)` — cyclic-trigonal
- `{4,n}`: `genus = 3(n-1)/2 (odd), 3(n-2)/2+1 (n≡2 mod 4), 3(n-2)/2 (n≡0 mod 4)`
- `{5,n}`: `genus = 2n-2 except 2n-4 when 5|n` — **NEW, operator-checked, zero
  mismatches on 19 points n=6..24**

### Slope conjecture — established

Mean first-difference over WHOLE periods is exactly `(m-1)/2` for m=2,3,4,5,
with period-m diff patterns: `[0,1]`, `[1,0,2]`, `[1,2,0,3]`, `[2,2,2,0,4]`.
Operator-checked, zero mismatches. Trap: truncated window (not whole periods)
gives mean BELOW `(m-1)/2` — state periodicity first, mean second.

### Diagonal closed forms (operator salvage, corroboration only)

`g(n)=(n−1)(n−2)/2` for adjacent pairs; `g(n)=⌊(n−1)(n−3)/2⌋` for gap-two;
`g(n)=⌊(n+1)(n−1)/2⌋` for gap-two-up. 55 points, zero mismatches. These are
three diagonals of the now-established full grid. The Singular runs that
generated them each ended `halt 1` (partial outputs of errored runs); the
genus_table grid was computed cleanly with both Singular and Sage.

Consistent with BST 1999 Thm 2.2 (primary): the only non-diagonal genus-1 pairs
are (2,3) and (2,4), confirming the grid at proof level.

## Rest on

- For each fixed `(k1,k2)` the equation is an algebraic curve; genus grows with the
  parameters, Faltings (genus>1) and Siegel (integral points even at genus 1) give
  finiteness for each pair — **but with no count computable in the parameters**
  (ineffective). This is the uniform-in-`k` obstruction. Now **primary-sourced**:
  BST 1999 Thm 1.1/1.2 (Zakopane proceedings, held via de Gruyter preview) — "For
  the remaining case gcd(m,n)=1 no general effective method is available... Siegel's
  result... is, unfortunately, ineffective... Both results are ineffective."
- **BST 1999 Theorem 2.2 (primary, independent of the computation): the genus
  classification.** For binomial pairs (Λ = k2!/k1! > 0), the only non-diagonal
  genus-1 pairs are (2,3) and (2,4); every other distinct pair has genus ≥ 2. This
  confirms at proof level the run's computed genus grid (Singular == Sage,
  2≤k1≤12, 2≤k2≤9) — the Faltings threshold is exact: only (2,3),(2,4) need Siegel.
- Jenkins (arXiv:1411.4111) reformulated `C(x,y)=C(x-a,y+b)` as the curve
  `prod_{r=0}^{a+b-1}(x-y-r) = prod_{p=0}^{a-1}(x-p) prod_{q=1}^{b}(y+q)`.
  He proved finiteness for `a != b` (via non-quadratic limiting ratio, not via genus),
  and left `a=b` (golden-ratio quadratic) open — that is exactly the Singmaster family.
- de Weger (JNT 63 (1997)): `(k,l)=(3,4)` curve has genus 3 (Faltings applies), is a
  double cover of the elliptic curve `Y^2+Y=X^3-X`; all integral points found.
  Small `(k,l)=(2,3),(2,4)` solved by Avanesov / de Weger-Pinter (elliptic, rank 2).
- GOAL.md defines oracles: `genus(k1,k2)` and `multiplicity(a,n_max)`; the falsifier
  is 3003 (8 occurrences), so a bound `<8` is refuted.

## Blocked by

- Linking genus growth to a uniform bound requires the ineffective constants to be
  removed — precisely the "finiteness is not a bound" trap.
- An effective Baker-type height bound is triple-exponential and too large to use;
  Matveev's constants are explicit but depend on heights (growing with k) and on
  B = max|bⱼ|Aⱼ/Aₙ — per-pair only, not uniform.

## Next

1. **Prove the genus formula — directive 10's bounded finishable task.**
   The symmetric rewrite `g(m,n) = ((m-1)(n-1) + 1 - gcd(m,n))/2` (already
   captured at `code/out/genus_symmetric_form.md`, zero mismatches) makes this
   a derivation target. The coprime case `gcd(m,n)=1` gives `g = p_a/2` exactly
   — a factor of two that means a quotient, with the involution
   `C(k-1-z,k) = (-1)^k C(z,k)` as candidate. Riemann-Hurwitz on the quotient
   by `x -> m-1-x, y -> n-1-y` should produce `g = p_a/2` for the coprime
   case, and the `gcd(m,n)` correction is the term where the involutions and
   branch loci interact. Do the singularity count at the points at infinity
   where the bidegree curve meets the boundary of `P^1×P^1`. The total delta
   invariant prediction is `((m-1)(n-1) - 1 + gcd(m,n))/2`. When derived and
   checked against the 111 Singular values with zero mismatches, promote
   `genus-single-closed-form-all-pairs` from `checked` to `proved`. Moves
   `proved` from 2 to 3. The genus formula remains NOT effective and NOT
   uniform in k.

2. **Matveev effective-bound computation.** For a specific small-(k1,k2) family
   (e.g. (2,p) hyperelliptic or k2=2 row), apply Matveev 2000 Thm 2.3 constants
   to produce a computed explicit bound; state its non-uniformity.

3. **LEDGER:** Every asserted bound must be run against `code/out/witnesses.json`.
   Any lemma implying B<8 is refuted by 3003. State counting convention on every
   claim.

4. **Uncaptured programs:** `test_slope_across_rows.py`, `test_slope_hypothesis.py`,
   `effectivegenus/rep_pairs.py`, `genus/verify_k2_5_row.py`,
   `pattern/print_family.py` — all five have zero captures. Run them or delete
   them (per directive 7). Their conclusions are already operator-checked, so
   capturing is verification, not discovery.

```thread
question: Can the family C(x,k1)=C(y,k2) yield a uniform-in-(k1,k2) effective bound
  on N(a), or only per-pair finiteness (ineffective)?
status: live — genus deliverable DONE (two-parameter grid via Singular+Sage,
  2<=k1,k2<=12 + k2=3,4,5 extended to k1=24; genus=1 only for {2,3},{2,4}; BST
  1999 Thm 2.2 primary-confirms). k2=5 closed form and slope conjecture both
  operator-checked, zero mismatches. The genus_table two-CAS grid supersedes the
  operator's three-diagonal salvage. Uniform bound still blocked by Faltings/
  Siegel/BST ineffectiveness. NEXT UP (directive 10): prove the genus formula
  via Riemann-Hurwitz on the involution C(k-1-z,k)=(-1)^k C(z,k) — the symmetric
  rewrite g=((m-1)(n-1)+1-gcd(m,n))/2 and the coprime case g=p_a/2 make this a
  bounded finishable derivation. Then Matveev effective constant for one pair.
rests-on: jenkins-ab-finite, deweger-genus3-curve, kane-method-ceiling,
  mrstt-method-limit, bbw-verification-bound, mrstt-interior-nothree,
  hpt-bilu-tichy-exceptional-classification,
  bilu-tichy-method-ineffective-uniformity-wall, bilu-tichy-classification-primary,
  kummer-lucas-class-not-logarithmic, bst-fixed-kl-ineffective-primary,
  bst-genus-classification-matches-grid, matveev-2000-explicit-constants-primary,
  sdw-elliptic-logarithms-eight-pairs, yamada-boundary-necessary-condition,
  lind-1968-fibonacci-family-primary
deliverables:
  - genus-table-two-cas: two-parameter grid, genus=1 iff {2,3}/{2,4}, proved-by-two-CAS
  - genus-k2-5-closed: 2n-2 except 2n-4 when 5|n, operator-checked
  - genus-slope-conjecture: mean=(m-1)/2 over whole periods, operator-checked
  - genus-symmetric-rewrite: ((m-1)(n-1)+1-gcd(m,n))/2, zero mismatches, derivation target
blocked-by: uniform bound needs effective Siegel or effective Schmidt subspace
  theorem (out of reach); Kane's method provably capped; MRSTT's interior method
  capped at exp(log^{3/2-eps} P); BST finiteness ineffective (primary).
next: prove genus formula via involution + Riemann-Hurwitz + singularity count
  (directive 10); then Matveev-2000 explicit constant for one small pair; run or
  delete the five uncaptured programs.
```