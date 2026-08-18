# The minimal $L^2$ Lebesgue-type constant for Lagrange interpolation

*Erdős Problem #1131 (erdosproblems.com/1131), from [Er61, p.67], [ESVV94],
[Er95e], [Va99, 2.45].*

## Statement

For distinct nodes `x_1, ..., x_n` in `[-1,1]` let

```
l_k(x) = prod_{i != k} (x - x_i) / prod_{i != k} (x_k - x_i)
```

be the Lagrange fundamental polynomials, so `l_k(x_k) = 1` and `l_k(x_i) = 0`
for `i != k`. Define

```
I(x_1, ..., x_n) = integral_{-1}^{1}  sum_k |l_k(x)|^2  dx.
```

> **Question.** What is `min I` over all node choices? In particular, is it true
> that
>
> ```
> min I = 2 - (1 + o(1)) / n ?
> ```

## What the statement does and does not say

- The integrand `sum_k l_k(x)^2` is a **polynomial of degree `2n-2` with
  rational coefficients** in the nodes. `I` is therefore an *exact rational
  function of the nodes*, and for any given node vector it is an exact rational
  number. There is no numerical integration anywhere in this problem, and a run
  that uses quadrature has introduced an error where none exists.
- `sum_k l_k(x) = 1` identically (the fundamental polynomials are a partition of
  unity), so by Cauchy–Schwarz `sum_k l_k(x)^2 >= 1/n` pointwise, giving the
  trivial floor `I >= 2/n`. That floor is far below the truth; the interesting
  regime is `I` just *below* `2`, and `2 = integral_{-1}^{1} 1` is the value the
  minimum approaches from below.
- The `L^2` norm, not the `L^infty` norm. Fejér's classical result is about
  `max_{x in [-1,1]} sum_k l_k(x)^2`; this problem replaces the max by an
  integral, and **the two have different minimisers.** That is the whole point.
- Every `n` is a separate finite optimisation problem. Solve them exactly.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **Fejér [Fe32]** showed that the nodes minimising
  `max_{x in [-1,1]} sum_k |l_k(x)|^2` are the roots of the integral of the
  Legendre polynomial (i.e. the zeros of `(1-x^2) P'_{n-1}(x)`, the
  Gauss–Lobatto-type points — establish the exact description here).
- **Erdős first conjectured the same nodes minimise `I`.** This was
  **disproved by Szabados [Sz66] for every `n > 3`.** Get the disproof: it is a
  construction, so it is checkable exactly by the oracle, and reproducing it is
  the single best calibration available for this run.
- **Erdős, Szabados, Varma and Vértesi [ESVV94]** proved
  ```
  2 - O( (log n)^2 / n )   <=   min I   <=   2 - 2/(2n - 1),
  ```
  the upper bound witnessed by the roots of the integral of the Legendre
  polynomial. So the conjecture `min I = 2 - (1+o(1))/n` sits **between** these:
  the upper bound already gives `2 - (1+o(1))/n` from one side, and the open
  half is **the lower bound**, where `(log n)^2` must be replaced by `1`.

**State this clearly in `CONTEXT.md` on day one:** the conjecture is equivalent
to closing a `(log n)^2` factor in the *lower* bound of [ESVV94]. Everything the
run does is measured against that.

## The obstruction, stated honestly

1. **The optimum is not a classical node system.** Szabados killed the natural
   guess. So there is no closed form to aim at, and any argument that assumes a
   symmetric or classical minimiser is assuming something false. **Compute the
   true minimisers and look at them** — for small `n` they are exactly
   obtainable, and what they look like is the mathematical content of this run.

2. **The lower bound is where the `(log n)^2` lives.** `I <= 2 - c/n` is
   constructive and settled. A lower bound `I >= 2 - C/n` must show that *no*
   node system does better, which is a statement about all of `[-1,1]^n` and
   cannot come from any single test function. The `(log n)^2` loss in [ESVV94]
   comes from a specific step; **find that step, name it, and say what it would
   take to remove it.** That is a well-posed and achievable objective.

3. **The relevant identity is a quadrature identity.** `integral l_k(x) dx` is
   the interpolatory quadrature weight `w_k` for the node system, and
   `integral l_k^2` is a closely related quantity. Formulating `I` in terms of
   quadrature weights and Gram matrices of the node system turns the problem
   into linear algebra with an explicit matrix, and that reformulation should
   be the first thing this run establishes.

Stated as the thing to beat:

> **The lower bound must control `2 - I` uniformly over all node systems, and
> the known argument loses a `(log n)^2` factor at one identifiable step.
> Removing that loss, or showing it is necessary, is the problem.**

## The oracle: exact rational optimisation

1. **`I(x_1,...,x_n)` exactly**, as a rational number for a rational node vector,
   and as a symbolic rational function for symbolic nodes. Compute
   `sum_k l_k(x)^2` as a polynomial and integrate term by term. Verify by hand:
   for `n = 2` with nodes `{-1, 1}`, `l_1 = (1-x)/2`, `l_2 = (1+x)/2`, so
   `sum l_k^2 = (1+x^2)/2` and `I = 4/3`. **The oracle must reproduce `4/3`
   exactly before anything else is run.**

2. **`min I` for each `n`, exactly or to certified precision.** For small `n` the
   critical-point equations `dI/dx_k = 0` are a polynomial system solvable by
   Groebner basis / resultants — do that, and report the exact minimiser and the
   exact minimum. Past that degree, use certified global optimisation and say
   which method produced which number. **Report the largest `n` reached and how
   far it is exact.**

3. **The comparison table**, which is the real deliverable of the oracle: for
   each `n`, the exact `min I`, the value at the Legendre-integral nodes, the
   value at Chebyshev nodes, the value at Szabados' construction, and
   `n * (2 - min I)`. **If the conjecture is right, the last column tends to 1.**
   That single column is what every claim in this run is checked against.

4. **The falsification oracle.** Any claimed lower bound `min I >= g(n)` is
   refuted the instant the optimiser produces a node system with `I < g(n)` —
   record it refuted, not weakened. Any claimed minimiser is checked against the
   exact optimum. **And every claimed minimiser family must be tested at
   `n = 4,5,6,7`, where Szabados' disproof bites: a lemma implying the
   Legendre-integral nodes are optimal is false, and this catches it in
   seconds.**

## Leads — verify each before relying on it

- **[ESVV94]** in full: both bounds, and precisely where the `(log n)^2` enters.
- **Szabados [Sz66]**: the construction beating the Legendre nodes, reproduced
  exactly here.
- **Fejér [Fe32]** and the `L^infty` problem, for the contrast.
- **Quadrature reformulation**: interpolatory weights, Gauss and Gauss–Lobatto
  rules, and the Gram matrix of `{l_k}` in `L^2([-1,1])` — note that
  `I = trace(G)` where `G` is that Gram matrix, which is a promising handle.
- **Lebesgue constants** and the `L^p` theory of interpolation more broadly,
  for which node systems are known to be near-optimal and in what norm.
