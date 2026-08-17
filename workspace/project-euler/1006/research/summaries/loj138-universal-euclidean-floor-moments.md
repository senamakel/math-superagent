# LOJ138 (mizu164) — 万能欧几里得 *floor moments* (cnblogs)

Source: https://www.cnblogs.com/AThousandMoons/p/13129167.html
Full text: [[loj138-universal-euclidean-floor-moments.full]]

## What this source establishes

The **moment-array** generalisation of the universal Euclidean algorithm: it
computes
  Σ_{x=0}^{n} ⌊(px+r)/q⌋^{k₁} · x^{k₂}   (mod 1e9+7)
for all k₁,k₂ with k₁+k₂ ≤ 10, in O(225·log max{p,q}).

**The Node monoid.** A Node is (cnt1, cnt2, ans[k₁][k₂]) where cnt1, cnt2 are
the counts of U and R in the sequence fragment, and ans[a][b] is the moment
sum over the fragment. Concatenation C = A·B merges by the binomial expansion:
  C.ans[a][b] = A.ans[a][b]
    + Σ_{i=0..a} Σ_{j=0..b} C(a,i)·C(b,j)·A.cnt1^i·A.cnt2^j·B.ans[a−i][b−j]
(derived from expanding (y + A.cnt1)^a·(x + A.cnt2)^b: the fragment B's
contributions shift by the accumulated counts of the prefix A).

**The same recursion.** calc(p,q,r,n,a=U,b=R) with
  m = (p·n+r)/q;
  if m=0: return bⁿ;
  if p ≥ q: return calc(p mod q, q, r, n, a, a^(p/q)·b);
  else: return b^((q−r−1)/p) · a · calc(q, p, (q−r−1) mod p, m−1, b, a)
        · b^(n − (m·q−r−1)/p).
Complexity O(225·log max{p,q}) (fixed moment bound k₁+k₂≤10, so 11×11 array).

## What it implies for PE1006

1. This is the full generalisation the run needs: Ψ(k) is a sum over the k+1
   representatives of v(x)², and v(x)² expanded as a polynomial in the floors
   ⌊x+ja⌋ with geometric weights = sums of the form Σ x^{j}·⌊…⌋ and
   Σ x^{j}·⌊…⌋² — exactly the k₁=1,2 / k₂=0,1 moments of this primitive.
2. The binomial merge rule shows the closure hypothesis concretely: moments up
   to second order in floor and arbitrary order in the geometric exponent
   stay closed under concatenation — the exact boundary directive 2's reduction
   needs.
3. The recursion is a second, independent statement of the same algorithm as
   fhq/OI-wiki — good for cross-checking an implementation (they should agree
   on the floor-moment values for the same inputs; use that as an oracle test
   before running at k=10^18).

## Claims anchored here

`governing-universal-euclidean` (moment-array form), answering
`citable-precise-statement-600d`, `citable-precise-statement-d2e7`.

## What it does NOT establish

- Nothing about Sturmian words or Psi(k) itself.
- It is a competitive-programming blog (mizu164), not peer-reviewed; treat the
  recursion as independently confirmed by fhq and OI-wiki (which agree) and
  by the brute oracle in-container.