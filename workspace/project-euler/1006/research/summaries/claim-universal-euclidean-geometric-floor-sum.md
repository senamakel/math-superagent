# Claim: universal Euclidean algorithm / generalized floor_sum with geometric weights, O(log)

Answers requests `citable-name-treatment-0c91`, `citable-precise-statement-600d`,
`citable-precise-statement-d2e7`: the primitive that evaluates sums of the form
sum_{i} x^i * floor((a*i+b)/c) (and the count / sum x^i / sum x^i*floor /
sum x^i*floor^2 tuple, i.e. the geometric-weight floor sum up to second moment)
in O(log), via the monoid generalisation of the Euclidean algorithm (AtCoder
floor_sum / "universal Euclidean", 万能欧几里得).

```claim
id: universal-euclidean-geometric-floor-sum
statement: Let a,b,c,n be nonnegative integers, c>0. Define the operation string
S(a,b,c,n) --- the "universal Euclidean" object --- to have exactly n R's and
m = floor((a*n+b)/c) U's, where the i-th R is preceded by floor((a*i+b)/c) U's.
For any linear-difference quantities carried as a monoid (e.g. the fhq 6-component
tuple {cntu,cntr,sumi,sums,sqrs,prod}, or a matrix monoid case), the product of
the whole string is computed exactly by
  F(a,b,c,n,U,R)
    = if m == 0: R^n
    = else: R^{floor((q-r-1)/p)} * U * F(q,p,(q-r-1) mod p, m-1, R, U) * R^{n - floor((q*m-r-1)/p)}
after first reducing (a mod c via merging U^{floor(a/c)} into each R, and b mod c
by stripping a leading U^{floor(b/c)}), which is exactly the reciprocal (Euclidean)
step. This evaluates sum_{i} x^i * y^{floor((a*i+b)/c)}-type geometric-weight sums,
and in particular the tuple (count, sum x^i, sum x^i * floor, sum x^i * floor^2)
is preserved through the reduction, in O(log n) — not O(n) terms.
hypotheses: quantities are linear in their argument (the monoid closure property
the method requires); U,R are linear operators / monoid elements; a,b,c,n in Z>=0.
holds-here: true for PE1006. The run needs sum over the k+1 representatives of
the second moment of v(x) = sum_j digit_j * 10^(k-1-j), which is a geometric
(10^j)-weighted floor sum; x = 10^-1 mod M is invertible (gcd(10, 101001001)=1),
so the geometric weights are well defined mod M. All weights are linear in the
floor argument, so the monoid closure applies.
status: sourced
bearing: This is the O(log) primitive directive 2 asserts Psi(k) collapses into:
the second moment of the geometrically-weighted floor sum. Without it, Psi(10^18)
would be a sum over ~10^18 terms — infeasible; with it the evaluation is O(log).
The fhq note carries the (cntu,cntr,sumi,sums,sqrs,prod) monoid and its merge
rule, and the recursion above verbatim; LOJ138 covers the k1/k2 moment-array
generalisation; OI-wiki gives the monoid proof and O(log) complexity.
anchor: research/sources/universal-euclidean-geometric-weight-fhq.full.md
(recursion + 6-component Po monoid + O(log) code, for sum f(x) a^x g(y) b^y);
research/sources/oi-wiki-universal-euclidean-floor-sum.full.md (monoid product
definition, merge/flip recursion, O(log n) proof);
research/sources/loj138-universal-euclidean-floor-moments.full.md
(Node ans[k1][k2] = sum x^k1 floor^k2, binomial combination);
research/sources/atcoder-math-hpp-v151.full.md (official floor_sum source + O(log) spec)
answers: citable-name-treatment-0c91, citable-precise-statement-600d,
citable-precise-statement-d2e7
```

## What the sources say

**fhq_treap "万能欧几里得 (universal Euclidean)" study note**
(`research/sources/universal-euclidean-geometric-weight-fhq.full.md`, source URL
https://www.cnblogs.com/dixiao/p/15719155.html).
States the problem form y = floor((px+r)/q), sum f(x) a^x g(y) b^y; uses a column
vector (sum_x y; y; 1) hit by U (increment y) and R (accumulate contribution).
Gives the merge identity
  sol(p,q,r,n,U,R) = sol(p mod q, q, r, n, U, U^{floor(p/q)} R)
and the flip (reciprocal step), with the closed recursion
  sol(p,q,r,n,U,R) = R^{floor((q-r-1)/p)} U * sol(q,p,(q-r-1) mod p, m-1, R, U)
                     * R^{n - floor((q*m-r-1)/p)},   m = floor((p*n+r)/q);
  if m = 0: sol = R^n.
Implements it with a 6-component monoid
  Po{ cntu, cntr, sumi, sums, sqrs, prod }
with the merge rule (a+b) carrying, through binomial-style cross terms, the
second moment — exactly the (count, sum x, sum x*floor, sum x*floor^2) closure
the run needs for Psi's sum-of-squares.

**OI-Wiki "万能欧几里得算法"**
(`research/sources/oi-wiki-universal-euclidean-floor-sum.full.md`, URL
https://oi.wiki/math/number-theory/euclidean/). Asserts the monoid model: view
each operation as a monoid element (or matrix), the whole string as their
product, and merge via (x1,y1,s1)*(x2,y2,s2)=(x1+x2,y1+y2,s1+s2+x2*y1), proven
associative. States the two reductions (strip leading U^{floor(b/c)}; merge
U^{floor(a/c)} into each R) and the axis-flip reciprocal step, and proves the
iteration is O(log n) (every two rounds halve the range). This is the structural
statement of the primitive directive 2 relies on.

**LOJ138 "万能欧几里得" (floor moments)**
(`research/sources/loj138-universal-euclidean-floor-moments.full.md`). Carries the
generalisation Node{ cnt1, cnt2, ans[k1][k2] } where ans = sum x^k1 * floor^k2,
combined via binomial expansion — the moment-array form that includes both x^i
and floor^i weighting, consistent with the geometric-weight floor sum.

**AtCoder Library** (`research/sources/atcoder-math-hpp-v151.full.md`, official source: spec for
`floor_sum(n,m,a,b) = sum_{i=0}^{n-1} floor((a i + b)/m)`, complexity O(log m)) is
the official reference for the base floor_sum; the universal-Euclidean note is
its generalisation to geometric weights.

## Why this is the right primitive, and its boundary

The reduction needs the run to evaluate, for the k+1 arc-midpoint
representatives, the second moment of v(x)=sum_j digit_j 10^(k-1-j); after
telescoping this is a sum of 10^j * floor(x + j a) terms (linear in the floor
argument). The universal-Euclidean recursion above evaluates any such linear
geometric-weight floor sum in O(log), and its tuple closure (count, sum x,
sum x*floor, sum x*floor^2) is preserved through both reduction rules.

The boundary the run must check before trusting it here: the monoid closure
hypothesis is that all carried quantities are linear in the floor argument. If
the run's Psi expression required a nonlinear quantity (e.g. a geometric term
whose exponent itself depends on floor), the closure would break and the method
would not apply. That is not the case for Psi — sum of squares of a linear-in-
floor digit value is exactly quadratic in floor, within closure — but it is the
hypothesis to re-verify against brute before running at 10^18.
