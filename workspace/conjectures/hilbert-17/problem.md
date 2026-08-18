# Hilbert's 17th problem — sums of squares

## The original question, and its answer

> Given a real polynomial `f ∈ R[x_1, …, x_n]` that is nonnegative on all of
> `R^n`, is `f` a sum of squares of **rational** functions?

Artin (1927) proved yes. That closes the problem as Hilbert asked it, so the
target of this workspace is the family of **quantitative and effective**
questions Artin's theorem left completely open. Every one of them is about
polynomials with rational coefficients, is finite once a degree is fixed, and
ends in an object a machine can check: a certificate.

Hilbert himself had already shown the naive version fails: a nonnegative
polynomial need **not** be a sum of squares of *polynomials*. The recalled
classification (Hilbert, 1888) is that psd = sos exactly for `(n, d)` with
`n = 1`, `d = 2`, or `(n, d) = (2, 4)` in the form/degree normalisation — with
Motzkin's `x⁴y² + x²y⁴ − 3x²y²z² + z⁶` the standard explicit witness on the
first failing case. **Recalled; confirm the exact normalisation before using
it, because the indexing convention differs between sources and an off-by-one
here silently changes which case is a counterexample.**

## The targets

### T1. Pfister's bound and whether it is sharp

Pfister proved every psd `f` in `n` variables is a sum of at most `2^n` squares
of rational functions. `n = 1` needs 2, `n = 2` needs 4 (recalled as sharp,
Cassels–Ellison–Pfister supplying the form needing four). **For `n ≥ 3` no
example is known requiring more than `n + 2` squares, and no bound better than
`2^n` is known.** The gap between `n + 2` and `2^n` at `n = 3` — between 5 and
8 — is the single most concrete open question in this circle, and it is a
question about explicit ternary forms.

### T2. Degree bounds on the denominator

Artin's theorem is non-constructive. Write `f = Σ (p_i/q)²`, equivalently
`q² f = Σ p_i²`. How large must `deg q` be, as a function of `n` and `deg f`?
Recalled: Reznick proved that for *strictly positive* forms `(Σ x_i²)^N · f` is
a sum of squares of forms for some `N`, with an explicit `N` depending on the
degree and on how close `f` comes to zero; and that no such uniform denominator
works when `f` has a real zero. The general effective bound descends from
Lombardi–Perrucci–Roy and is a tower of exponentials. **Any lowering of a
degree bound on a named family is a result.**

### T3. Positivstellensatz degree bounds in practice

For a semialgebraic set `K = {g_1 ≥ 0, …, g_m ≥ 0}` and `f > 0` on `K`,
Putinar's and Schmüdgen's representations give `f` as a weighted sum of squares
at some degree. The known general bounds are astronomically worse than what a
solver finds on real instances. The gap between the proved bound and the
observed degree, measured on a family this run can generate, is a publishable
measurement even if no bound moves.

## The cheap tests every candidate must pass first

1. **The zero test.** Every claim about denominators or square-counts changes
   character depending on whether `f` has a real zero. An argument that never
   mentions the zero set of `f` is either about strictly positive forms only —
   in which case say so in the statement — or it is wrong. Reznick's uniform
   denominator fails exactly at a real zero, and that is where the difficulty
   lives.
2. **The rounding test.** An SDP produces a floating-point Gram matrix. A
   floating-point Gram matrix is **not** a proof, and a psd-looking numerical
   solution routinely fails to admit any exact rational psd Gram matrix at all
   when `f` sits on the boundary of the SOS cone. Every claimed decomposition
   must be exhibited as an exact rational identity and verified by expanding it
   symbolically. A rounding that fails is itself information: it says the form
   is on the boundary.
3. **The counting test.** A claimed sum of `k` squares must be checked against
   the known lower bounds for its `n` (`n + 2` recalled as the best general
   lower bound; 4 for `n = 2`). A decomposition beating a proved lower bound is
   an error in the algebra, located immediately by expanding it.

## What is genuinely unknown

- Whether five squares suffice for every psd ternary form — or any bound below
  `2^3 = 8` for `n = 3`.
- Whether the Pfister bound `2^n` is attained for any `n ≥ 3`, i.e. an explicit
  psd form provably not a sum of `2^n − 1` squares.
- Sharp denominator degree bounds for a psd polynomial with a real zero, even
  for ternary sextics.
- Effective Positivstellensatz degree in any regime where the proved bound and
  the observed degree are within reach of each other.
- The exact minimal number of squares for named forms — Motzkin, Robinson,
  Choi–Lam, Schmüdgen — as sums of squares of rational functions. Even here
  the literature records upper bounds and few matching lower bounds.

## What counts as a result

In descending order of value.

1. A **lower** bound: an explicit psd form in `n ≥ 3` variables, with rational
   coefficients, proved not to be a sum of `k` squares of rational functions
   for a `k` larger than anything published. Lower bounds are what this subject
   lacks; an upper bound is a search, a lower bound is a theorem.
2. An improved **upper** bound on the number of squares for a named class of
   forms (ternary sextics, forms with prescribed zeros), with the
   decomposition exhibited exactly and checked in Lean.
3. A denominator degree bound for a named family, better than the general
   bound, with the obstruction to removing the family restriction named.
4. An exact rational SOS certificate for a form the literature reports only
   numerically, verified by expansion and by `decide`/`norm_num` in Lean.
5. A measured gap: for a generated family, the observed Positivstellensatz
   degree against the proved bound, with the generator and the ceiling of the
   computation both stated.
6. A refutation of a folklore expectation — an explicit form where the
   plausible small-denominator guess provably fails.

**Do not claim a proof that `2^n` is or is not sharp**, and do not report a
numerical SDP solution as a decomposition. A Gram matrix without an exact
rational witness is a lead.
