# fhq_treap — *[学习笔记]万能欧几里得* (universal Euclidean, cnblogs)

Source: https://www.cnblogs.com/dixiao/p/15719155.html
Full text: [[universal-euclidean-geometric-weight-fhq.full]]

## What this source establishes

The **universal Euclidean algorithm** (万能欧几里得, "Chtholly's algorithm" is
a nickname) — a monoid generalisation of the Euclidean/floor-sum algorithm that
handles *geometric-weight* sums, which the ordinary AtCoder `floor_sum` cannot.

**Problem form it solves.** With y = ⌊(px+r)/q⌋, evaluate
  Σ f(x)·aˣ·g(y)·bʸ
for linear-difference quantities f, g. In particular the pure-geometric forms
Σ aˣ·⌊(px+r)/q⌋ and their moments.

**String model.** The floor-sum is encoded as the operation string S with n R's
and m = ⌊(pn+r)/q⌋ U's, the i-th R preceded by ⌊(pi+r)/q⌋ U's. U and R are any
monoid elements; the answer is the product of the whole string.

**Two reductions (exact, O(log)).**
- Merge: if p ≥ q, every R is preceded by ≥ ⌊p/q⌋ U's; absorbing those into R
  gives sol(p, q, r, n, U, R) = sol(p mod q, q, r, n, U, U^(⌊p/q⌋)·R).
- Flip (reciprocal step): count U's instead; with m = ⌊(pn+r)/q⌋,
  sol(p,q,r,n,U,R) = R^(⌊(q−r−1)/p⌋) · U ·
      sol(q, p, (q−r−1) mod p, m−1, R, U) · R^(n − ⌊(qm−r−1)/p⌋),   if m > 0;
  sol = R^n if m = 0.

**Monoid implementation.** The note carries a concrete 6-component monoid
  Po{cntu, cntr, sumi, sums, sqrs, prod}
with the merge rule: adding sequence B after A updates
  sums += cntu_A·cntr_B;  sqrs += cntu_A²·cntr_B + 2·cntu_A·sums_B; …
so it tracks up to second moments of the floor argument with geometric weights —
exactly the (count, Σxⁱ, Σxⁱ·floor, Σxⁱ·floor²) closure directive 2 requires.
U has cntu=1 (increment y), R has cntr=1 and accumulates the contribution.

**Complexity.** Each recursion step swaps (p,q) → (q, p mod q), a Euclidean
step; total O(log max{p,q}) evaluations of the monoid product (which is O(1)
per combine for fixed monoid size).

## What it implies for PE1006

This is the exact primitive for Ψ(k) = second moment of the geometric-weight
floor sum v(x) = ⌊x+ka⌋ − 10^{k−1}⌊x⌋ + 9·Σ_{j=1}^{k−1} 10^{k−1−j}⌊x+ja⌋:
after the telescoping sum, Ψ(k) is a sum over the k+1 arc-midpoint intercepts
x of a quadratic form in the floors ⌊x+ja⌋ with geometric weights 10^{k−1−j}.
Summing v(x)² over x expands into floor-sums with weights 10ⁱ·10ʲ, each
evaluated by this algorithm in O(log) — no ~k² pair enumeration and no k=10^18
factor enumeration.

## Boundary / caution

- The monoid closure hypothesis: carried quantities must be linear in the floor
  argument (or its powers up to 2); the note explicitly lists sums it *cannot*
  handle (Σ√y, Σxʸ, Σa^{xy}, …) because those are not linear-difference. The
  Ψ(k) expression is quadratic in floors — inside closure — but a term like
  x^{⌊…⌋} with the *exponent* depending on floor would break it.
- The note's code is mod 998244353; the run must re-implement with modulus
  M = 101001001 and x = 10^{-1} mod M (valid: gcd(10, M)=1).

## Claims anchored here

`governing-universal-euclidean` (recursion + 6-component monoid + O(log) code),
answering requests `citable-name-treatment-0c91`, `citable-precise-statement-600d`,
`citable-precise-statement-d2e7`.