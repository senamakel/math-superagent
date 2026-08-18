# The measure of the sublevel set of a real-rooted monic polynomial

*Erdős Problem #1038 (erdosproblems.com/1038), from Erdős–Herzog–Piranian
[EHP58, p.131].*

## Statement

Let `f` be a **non-constant monic polynomial in `R[x]`, all of whose roots are
real and lie in `[-1,1]`**. Write

```
E(f) = { x in R : |f(x)| < 1 },      mu(f) = Lebesgue measure of E(f).
```

> **Question.** Determine
>
> ```
> inf  mu(f)      and      sup  mu(f)
> ```
>
> as `f` ranges over all such polynomials.

## What the statement does and does not say

- **Monic, real-rooted, roots in `[-1,1]`.** All three matter. Drop monic and
  scaling makes `mu` anything. Drop real-rootedness and the problem changes
  character entirely. Widen the root interval to `[-2,2]` and the infimum
  becomes `0` (a small perturbation of the Chebyshev polynomials witnesses it) —
  so `[-1,1]` versus `[-2,2]` is exactly the transition, and understanding why
  is the first thing this run should establish.
- **`E(f)` is not contained in `[-1,1]`.** It is a union of open intervals
  around the roots, and it extends outside `[-1,1]` — the outer parts are where
  the measure at the *supremum* end comes from.
- **The degree is not fixed.** Both extrema are over all degrees `n >= 1`, so
  each is a limit of the per-degree extrema. Compute the per-degree extrema
  exactly; they are what the answer is a limit of.
- **`mu(f)` is a finite computation for fixed roots.** `E(f)` is bounded by the
  real solutions of `f(x) = 1` and `f(x) = -1`, so `mu(f)` is an exact algebraic
  number obtainable by real root isolation. There is no analysis in evaluating
  it, only exact arithmetic.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **Erdős–Herzog–Piranian [EHP58]** proved `mu(f) <= 2*sqrt(2)` under the
  restriction that **all roots lie in `{-1, +1}`** (the two endpoints only), and
  conjectured that this is the best possible upper bound in general.
- The same paper notes `inf mu < 2`, witnessed by `f(x) = (x+1)(x-1)^m` for
  `m >= 3`. **Reproduce this computation exactly here** — it is small, it is
  checkable, and it calibrates the oracle.
- If the roots are allowed in `[-2,2]` the infimum is `0`, via a perturbation of
  the Chebyshev polynomials. EHP further conjectured that in that regime
  `mu(f) >> n^{-c}`; **Pommerenke [Po61]** proved this, in fact showing `E(f)`
  contains an interval of width `>> n^{-4}`.
- The **current best known bounds** reported on the problem page are
  ```
  1.519... ~= 2^{4/3} - 1  <=  inf mu  <=  1.835...        and        sup mu = 2*sqrt(2).
  ```
  Treat the supremum as *reported settled* and the infimum as the open half —
  but **verify both**, including which paper closed the supremum, before
  building on either. If the supremum is genuinely closed, this problem is the
  infimum problem and the run should say so in `CONTEXT.md` on day one.

## The obstruction, stated honestly

1. **The two ends are different problems.** The supremum is attained by spreading
   the roots to the endpoints — a compactness-plus-symmetrisation question. The
   infimum is attained by clustering, and the extremal configuration is *not*
   symmetric (the witness `(x+1)(x-1)^m` is as lopsided as it gets). Do not
   expect one technique to do both.

2. **The infimum is a genuine optimisation with no known extremal family.** The
   gap `1.519 <= inf <= 1.835` is a gap between a proof technique and a
   construction, and neither side is known to be tight. **The most likely real
   contribution of this run is on one of those two numbers**, by finding a better
   construction (which is checkable, exactly) or by improving the lower-bound
   argument.

3. **`[-1,1]` versus `[-2,2]` is the whole phenomenon.** The interval `[-2,2]`
   is exactly where Chebyshev polynomials have sup norm `2` on the interval, and
   the transition to `inf = 0` there says the answer is governed by logarithmic
   capacity / transfinite diameter (`cap([-1,1]) = 1/2`, `cap([-2,2]) = 1`).
   **An approach that does not have a potential-theoretic reading is probably
   not seeing the mechanism.**

Stated as the thing to beat:

> **A better lower bound on `inf mu` must control how much measure a cluster of
> roots can lose, uniformly in the degree — the difficulty is that the extremal
> configuration is asymmetric and degenerates as the degree grows.**

## The oracle: exact measure, and a certified optimiser

1. **`mu(f)` exactly, for a given root multiset.** Compute `f` from its roots in
   exact arithmetic; isolate the real roots of `f(x) - 1` and `f(x) + 1`; sort
   them; sum the lengths of the intervals on which `|f| < 1`. Use exact/interval
   arithmetic and **certify the isolation** — a sampled or floating-point
   estimate of `mu` is not `mu`, and this problem's answer is a third decimal
   place. Verify by hand on `f(x) = x` (where `mu = 2`) and on
   `f(x) = (x+1)(x-1)^3`.

2. **Per-degree extrema.** `mu_n^min = inf` and `mu_n^max = sup` over root
   vectors in `[-1,1]^n`. This is a smooth `n`-dimensional optimisation with an
   exactly evaluable objective. Do it with a global method plus certified local
   refinement, and **report the degrees reached, the optimising root vectors,
   and whether the optimiser is at an interior point or a boundary/multiple-root
   configuration.** The shape of the optimiser is the mathematical content.

3. **The falsification oracle.** Any claimed lower bound `inf mu >= B` is refuted
   the moment the optimiser finds an `f` with `mu(f) < B` — record it refuted,
   not weakened. Any claimed upper-bound construction must pass (1) exactly.
   **Run every claimed bound against `(x+1)(x-1)^m` for `m = 3..30` and against
   `x^n`, `(x^2-1)^m`, and the Chebyshev-like configurations, every time.**

## Leads — verify each before relying on it

- **[EHP58] itself.** Get the actual theorem, the actual conjecture, and the
  exact hypotheses on the roots. Everything downstream is measured against it.
- **The `2^{4/3} - 1` lower bound** and the `1.835...` construction: where do
  they come from, and which is more likely to move?
- **Pommerenke [Po61]** and the `n^{-4}` interval — the technique that survives
  when the infimum is zero, and what it says at `[-1,1]`.
- **Logarithmic capacity and transfinite diameter** of `[-1,1]` and `[-2,2]`,
  Chebyshev polynomials, and the Cartan / Remez-type lemmas bounding the measure
  of `{|f| < 1}` for a monic degree-`n` polynomial. The classical Cartan lemma
  gives a bound of exactly this shape and is the standard tool; establish what
  it gives here and where it is lossy.
- **Erdős Problem #1040** (the same quantity for roots in a general closed set,
  and whether it is determined by transfinite diameter) — the conceptual frame
  for this problem, and worth reading even though it is not the target.
