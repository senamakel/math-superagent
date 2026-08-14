# Ground truth — hypercube-induced-degree

**This file must never enter the container.** It lives at the repository root,
outside `workspace/`, the only tree bind-mounted at `/workspace`. It is read by
`scripts/eval-report` on the host and by nothing else.

## What this problem really is

**The Sensitivity Conjecture**, in its graph-theoretic form. Posed as a question
about Boolean functions by **Nisan and Szegedy (1992)** — whether the
*sensitivity* of a Boolean function is polynomially related to its *block
sensitivity* and hence to its degree, decision-tree complexity, and the rest of
the polynomially-equivalent complexity measures.

**Gotsman and Linial (1992)** proved the equivalence that makes the seed's
statement the right one: the sensitivity conjecture holds if and only if every
induced subgraph of `Q_n` on more than `2^{n-1}` vertices has maximum degree
`n^{Omega(1)}`.

Prior state of the art, unchanged for 27 years:

- **Upper bound `sqrt(n)`**: Chung, Füredi, Graham and Seymour (1988) — a
  construction achieving maximum degree `sqrt(n)`, and they conjectured it
  tight.
- **Lower bound `Omega(log n)`**: also Chung–Füredi–Graham–Seymour, and it
  resisted every attempt at improvement. No superlogarithmic bound was known.

## The solution being withheld

**Hao Huang, July 2019**, "Induced subgraphs of hypercubes and a proof of the
Sensitivity Conjecture", *Annals of Mathematics* 190(3), arXiv:1907.00847.

Two pages. The proof:

1. Define a **signed adjacency matrix** `A_n` — same support as `Q_n`'s
   adjacency matrix, entries in `{0, +1, -1}` — by the recursion

   ```
   A_1 = [[0,1],[1,0]],   A_n = [[A_{n-1}, I], [I, -A_{n-1}]]
   ```

2. Show `A_n^2 = n I`, so `A_n` has eigenvalues `±sqrt(n)`, each with
   multiplicity `2^{n-1}`.
3. For `S` with `|S| = 2^{n-1} + 1`, the principal submatrix `A_n[S]` has order
   exceeding the multiplicity of `-sqrt(n)`, so by **Cauchy interlacing** its
   largest eigenvalue is at least `sqrt(n)`.
4. The largest eigenvalue of a matrix with entries in `{0,±1}` is at most its
   maximum row sum, which is the maximum degree of `Q_n[S]`. Hence
   `D(S) >= sqrt(n)`.

Combined with the 1988 construction, `f(n) = ceil(sqrt(n))` exactly, and the
Sensitivity Conjecture follows via Gotsman–Linial.

## Why this problem is in the calibration set

It is the **pure invention test**. The proof needs no computation, no literature
beyond two standard facts (Cauchy interlacing, and the cube's structure), and no
scale. It turns entirely on one idea: *change the matrix*. Everything else is
three lines of linear algebra.

So this problem measures exactly what the harness's `inventor` and `reducer`
roles are supposed to provide, with almost nothing else contributing. A run that
reaches the answer by grinding is not possible here; a run that reaches it must
have had the idea.

## De-naming assessment

**Strong.** This is the problem where de-naming genuinely works. The seed states
a self-contained extremal-combinatorics question about induced subgraphs of the
cube, with no mention of sensitivity, block sensitivity, Boolean functions,
decision-tree complexity, or any name. A model that has memorised "Huang proved
the sensitivity conjecture with a signed adjacency matrix" still has to
*recognise* that this combinatorial statement is that conjecture, which is the
Gotsman–Linial equivalence and is not obvious.

The one leak the seed accepts deliberately: the final leads bullet mentions that
the quantity relates to "measures of how much a Boolean function depends on its
inputs". That is left in because withholding it would make the time capsule
dishonest — the connection *was* the reason anyone cared in 2018 — but it is the
most likely trigger for recognition. **Score any run that names "sensitivity"
early and then produces the signed matrix as recall, not invention.**

## How much the seed hints

Recorded so the score can be adjusted for it. The seed's obstruction section
argues that averaging arguments cannot reach `sqrt(n)` and that the bound must
come from "a quantity that is itself a maximum". It also observes that `sqrt` is
not a natural output of counting and suggests looking for a quadratic relation.

Both are honest statements of why the problem is hard and both are things an
expert would say in 2018 — but together they point at the spectral neighbourhood.
An earlier draft of the seed went further and explicitly listed "signed or
weighted adjacency matrices on the cube" as a lead; **that was removed**, because
it is Huang's key step. The current seed names eigenvalues nowhere.

Calibration consequence: reaching "try a spectral method" is worth *less* here
than it would be unhinted, and reaching "`A_n^2 = nI` with a `±1` signing" is
worth the full credit.

## Falsifiable checks for the audit

The exact values are `f(n) = ceil(sqrt(n))`: `f(1)=1, f(2)=2, f(3)=2, f(4)=2,
f(5)=3, ...`. A run's `f_exact` implementation is correct iff it reproduces
these. **A run that computes `f(n)` correctly for `n <= 5` has the sequence
`1,2,2,2,3` in hand, which is consistent with `ceil(sqrt(n))` and is a legitimate
route to conjecturing the answer.** That is derivation, not recall, and scores
well.

Watch for: `A_n^2 = nI`, the block recursion, "Cauchy interlacing", or `sqrt(n)`
asserted as the answer, appearing **before** any computation or derivation
produced them.
