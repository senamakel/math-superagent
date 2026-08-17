# OI Wiki — 类欧几里得算法 / 万能欧几里得算法 (universal Euclidean algorithm)

Source: https://oi.wiki/math/number-theory/euclidean/
Full text: [[oi-wiki-universal-euclidean-floor-sum.full]]

## What this source establishes

A thorough treatment of the floor-sum family: the classic 类欧几里得
(Euclidean-like) algorithm for Σ ⌊(ai+b)/c⌋, and its generalisation
**万能欧几里得 (universal Euclidean)**, which elevates U and R to arbitrary
monoid elements.

**Monoid model (the core idea).** The operation string S(a,b,c,n) has n R's
and m = ⌊(an+b)/c⌋ U's, the i-th R preceded by ⌊(ai+b)/c⌋ U's. Model each
U and R as a monoid element; the answer is the product of the whole string.
The note defines the contribution-merge for the (x, y, Σy) state:
  (x₁,y₁,s₁)·(x₂,y₂,s₂) = (x₁+x₂, y₁+y₂, s₁+s₂+x₂·y₁),
proven associative, with identity (0,0,0). This is the (count, height,
running sum) monoid — a special case of the fhq 6-component one.

**The recursion (verbatim, O(log)).**
  F(a,b,c,n,U,R):
    if b ≥ c:  return U^(⌊b/c⌋) · F(a, b mod c, c, n, U, R)
    if a ≥ c:  return F(a mod c, b, c, n, U, U^(⌊a/c⌋)·R)
    m = ⌊(a·n+b)/c⌋
    if m == 0: return Rⁿ
    return R^(⌊(c−b−1)/a⌋) · U · F(c, (c−b−1) mod a, a, m−1, R, U) · R^(n − ⌊(c·m−b−1)/a⌋)

**Complexity proof (important — this is the go/no-go fact).** Each round
transforms the parameters (a,c) → (c, a mod c) — a Euclidean step — and each
round costs O(log(a/c) + log(c/(a mod c))) for the three binary-exponentiation
steps. The telescoping sum over all rounds gives **total
O(log max{a,c} + log(b/c))**, i.e. O(log) in the parameters, NOT O(n). This is
what makes the k=10^18 evaluation feasible: n appears only inside m and the
final exponent, never as a loop bound.

**Algebraic/geometric view.** The note also derives the classical
类欧几里得 formulas (sum of floors, sum of floor², etc.) by the same
U/R-string; the geometric intuition is the digitised line y = (ax+b)/c: each
crossing of a vertical grid line writes R, of a horizontal line U.

## What it implies for PE1006

1. This is the structural statement of the primitive directive 2 relies on,
   with the O(log) bound proven (not just asserted): the number of monoid
   multiplications is O(log max{p,q}), independent of n.
2. The (x,y,Σy) monoid is the prototype; the run needs its extension to
   geometric weights xⁱ and second moments (handled by the fhq 6-component
   Po or the LOJ138 moment array).
3. The recursion's index arithmetic (⌊(c−b−1)/a⌋, (c−b−1) mod a, m−1,
   n − ⌊(cm−b−1)/a⌋) is exact integer arithmetic — no floating point — which
   is what lets the solver work mod M = 101001001 safely.

## Claims anchored here

`governing-universal-euclidean` (recursion + O(log) proof), answering
`citable-precise-statement-600d`, `citable-precise-statement-d2e7`.

## What it does NOT establish

- Nothing geometric-weight specific; the xⁱ weights are the fhq note's
  contribution (this source's monoid is the un-weighted (x,y,Σy)).
- Nothing about Sturmian words or PE1006 itself.