# Hilbert's 13th problem — the algebraic form, and resolvent degree

## Two problems under one number

Hilbert asked whether the general degree-7 equation

```
x⁷ + a x³ + b x² + c x + 1 = 0
```

can be solved by functions of **two** variables. The question splits, and the
two halves have opposite fates:

- **Continuous version.** Kolmogorov (1956) and Arnold (1957) proved every
  continuous function of `n` variables is a superposition of continuous
  functions of two variables — so the answer is *yes*, and the continuous
  problem is closed. It is **not** this workspace's target.
- **Algebraic version.** Can the roots be written as a superposition of
  *algebraic* functions of at most two variables? This is what Hilbert
  evidently meant, it is **open**, and it is the target.

The modern frame for the algebraic version is **resolvent degree**.

## Resolvent degree

For a branched cover / an enumerative problem `E → X` (paradigmatically: the
degree-`n` polynomial and its roots), `RD(E)` is the smallest `d` such that `E`
can be solved by a tower of finite covers each of which is pulled back from a
base of dimension `≤ d`. Write `RD(n) = RD` of the general degree-`n` polynomial.

Recalled facts — **every one to be confirmed or struck against a primary
source before anything rests on it**:

- `RD(n) = 1` for `n ≤ 5`. Solvability by radicals gives `n ≤ 4`; the quintic
  reduces to a one-parameter family (Bring radical, Tschirnhaus).
- `RD(6) ≤ 2`, `RD(7) ≤ 3` (Hilbert), `RD(8) ≤ 4`, `RD(9) ≤ 4` (Hilbert /
  Wiman), with `RD(n) ≤ n − 4` for `n ≥ 9` and improvements of the form
  `n − 5`, `n − 6`, … in ranges that must be pinned down exactly.
- **Hilbert's 13th, in this language, asks whether `RD(7) ≤ 2`.** His 12th-ish
  companion questions ask the same for the sextic (`RD(6) ≤ 1`?) and the
  degree-8 case.
- **No lower bound above 1 is known for any `n`.** `RD(n) ≥ 2` is not known
  for a single `n`. This is the state of the art and it is the most striking
  fact about the subject: a century of upper-bound improvements against no
  lower bound at all.
- Essential dimension is the nearest *provable* lower-bound technology:
  `ed(S_n) ≥ ⌊n/2⌋` (Buhler–Reichstein). Essential dimension bounds
  **do not** bound resolvent degree from below, because RD allows towers, and
  understanding exactly why is the first thing this run must get right.
- Farb–Wolfson revived the subject with a modern definition and a program;
  Sutherland, Heberle and others have computed and reduced specific cases.

## The cheap tests every candidate must pass first

1. **The tower test.** Resolvent degree permits an arbitrary *tower* of
   solutions, each of bounded base dimension. Every proposed lower-bound
   argument must say what it does against a tower — an argument bounding a
   single cover proves an essential-dimension statement, which is already known
   and is *not* a resolvent degree bound. This is the exact trap the subject
   sets, and an argument that does not name its answer to it is refuted.
2. **The `n ≤ 5` test.** Any claimed lower bound must return `RD(n) = 1` for
   `n ≤ 5` and `RD(6) ≤ 2`. A method that would prove `RD(5) ≥ 2` is wrong, and
   running it on the quintic is a five-minute refutation.
3. **The accessory-parameter test.** Every upper bound is a Tschirnhaus-style
   construction, and its content is entirely in *how many parameters survive*
   after the normalisation. A claimed improvement must exhibit the
   transformation explicitly and have its parameter count verified by an exact
   elimination — never by a dimension count done in prose.

## What is genuinely unknown

- `RD(7) ≤ 2`? — Hilbert's 13th, algebraic form. Open.
- `RD(6) ≤ 1`? — Hilbert's sextic question. Open.
- **Any lower bound at all**: is `RD(n) ≥ 2` for some `n`? Open, and the
  greatest prize here. A proof for a single `n` would be a landmark.
- The exact value of `RD(n)` for every `n ≥ 6`.
- Whether the known upper bounds `n − 4`, `n − 5`, … can be pushed to a
  sublinear function of `n`.
- Resolvent degree of other enumerative problems — the 27 lines on a cubic
  surface, the 28 bitangents, Schubert problems — where explicit Galois theory
  makes the question computable.

## What counts as a result

In descending order of value.

1. **A lower bound.** `RD(n) ≥ 2` for any `n`, or any general obstruction that
   survives the tower test. The subject has none.
2. An improved upper bound for a specific `n` — a Tschirnhaus tower with fewer
   accessory parameters than published, exhibited explicitly with the parameter
   count verified by exact elimination.
3. Resolvent degree, exactly or bounded, for a named enumerative problem
   (lines on a cubic surface, bitangents, a Schubert problem), computed with
   the Galois group and the tower written down.
4. A precise statement, proved, of *why* essential dimension does not bound RD
   below — an explicit family where the two differ, which would be the sharpest
   thing anyone could say about the obstruction.
5. A machine-checked verification of one published Tschirnhaus reduction, with
   the elimination reproduced exactly over `Q` and stated in Lean.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not claim `RD(7) ≤ 2` or any lower bound on prose.** Every upper bound is
an explicit transformation whose parameter count is checkable by elimination;
every lower bound must answer the tower test in its first paragraph.
