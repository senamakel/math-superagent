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

## What a bigger run would settle

The genus deliverable is DONE for 2≤k1≤12, 2≤k2≤9 (Singular == Sage; see CONTEXT.md
"Genus grid" and `code/out/genus_table.captured.txt`), and BST 1999 Thm 2.2 now gives a
primary-source proof that only (2,3),(2,4) are genus 1. What remains is the
secondary deliverable: an effective height bound with a **computed** constant for a
specific small-`(k1,k2)` family, using Matveev 2000's explicit constants
(`matveev-2000-explicit-constants-primary`) as the primary constant-supplier.

## Blocked by

- Linking genus growth to a uniform bound requires the ineffective constants to be
  removed — precisely the "finiteness is not a bound" trap.
- An effective Baker-type height bound is triple-exponential and too large to use;
  Matveev's constants are explicit but depend on heights (growing with k) and on
  B = max|bⱼ|Aⱼ/Aₙ — per-pair only, not uniform.

## Next

1. **MRSTT effectiveness RESOLVED (scholar, full-text):** Remark 1.7 states the
   "t sufficiently large" thresholds ARE effective (computable, unoptimized, likely
   astronomically large). Interior theorem yields a numerical B in principle;
   boundary `2 ≤ m ≤ (log t)/(log₂t)^{3/2−ε}` remains the whole open gap.
2. **Primary BST obtained:** `research/sources/number-theory-in-progress-vol1-preview.full.md`
   (de Gruyter Zakopane vol. 1 preview, pp. 11–26) holds BST 1999 readable; the
   author-hosted `best1.ps` is raw PostScript (not readable). The ineffectivity
   quote is now primary-sourced.
3. Genus deliverable: report the computed grid + BST 1999 Thm 2.2 confirmation +
   the explicit statement that genus>1 gives per-pair finiteness only, never a
   uniform bound.
4. Effective-bound deliverable: for a specific small (k1,k2) (e.g. (2,p) hyperelliptic
   family or the k2=2 row) apply Matveev 2000 Thm 2.3 constants to produce a
   computed explicit bound; state its (lack of) uniformity in k.
5. **LEDGER:** Every asserted bound must be run against `code/out/witnesses.json`.
   Any lemma implying B<8 is refuted by 3003. State counting convention on every claim.

```thread
question: Can the family C(x,k1)=C(y,k2) yield a uniform-in-(k1,k2) effective bound
  on N(a), or only per-pair finiteness (ineffective)?
status: live — genus deliverable DONE (grid computed, Singular==Sage, 2<=k1<=12,
  2<=k2<=9; BST 1999 Thm 2.2 primary-confirms only (2,3),(2,4) have genus 1); the
  uniform bound is blocked by ineffectiveness of Faltings/Siegel/BST (primary-
  sourced via BST 1999 Thm 1.1); effective-bound path is Matveev 2000 with
  explicit but per-pair (non-uniform) constants.
rests-on: jenkins-ab-finite, deweger-genus3-curve, kane-method-ceiling, mrstt-method-limit,
  bbw-verification-bound, mrstt-interior-nothree, hpt-bilu-tichy-exceptional-classification,
  bilu-tichy-method-ineffective-uniformity-wall, kummer-lucas-class-not-logarithmic,
  bst-fixed-kl-ineffective-primary, bst-genus-classification-matches-grid,
  matveev-2000-explicit-constants
blocked-by: uniform bound needs effective Siegel or effective Schmidt subspace
  theorem (out of reach); Kane's method provably capped; MRSTT's interior method
  capped at exp(log^{3/2-eps} P); BST finiteness ineffective (primary).
next: report genus grid + Faltings threshold as the honest deliverable; compute a
  Matveev-2000-based explicit constant for one small (k1,k2) family, stating its
  non-uniformity.
```

