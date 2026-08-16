# Scored program search: Casas–Alvero at degree 20

## The search

Degree 20 is the smallest open degree of the Casas–Alvero conjecture. The
conjecture says:

> If a monic polynomial `f` of degree `n` over `Q` shares a root with each of
> its first `n-1` derivatives `f', f'', ..., f^(n-1)`, then `f = (x-a)^n`
> for some `a`.

A *true* counterexample at degree 20 is **not** expected — the conjecture is
believed true, degree 12 has already been settled, and degree 20 has not. So
the point of this search is not to find one. The point is the **score
distribution**: how many of the 19 derivatives a monic degree-20 polynomial
`f` over `Q` can share a root with, and **which constraint binds** to stop it
reaching 19 (or 18, ...).

## The scored quantity

`score(f) = #{ j in 1..19 : deg(gcd(f, f^(j))) > 0 over Q[x] }`.

That is: the number of the 19 derivatives `f`,..., which share a genuine
(non-constant) factor with `f`, computed **exactly** over the rationals —
sympy `Poly.gcd` over `QQ`, never floating point.

- `score = 19` would mean the CA hypothesis holds — {monic deg-20 sharing a
  root with every derivative}. By the conjecture this is exactly the trivial
  family `(x-a)^20`, which the scorer must reject. So a supposed output of 19
  from anything else is a bug.
- `score` near the top (e.g. 17, 18) is a "near-miss" candidate: a polynomial
  whose first few derivatives share roots but that eventually breaks. The
  interesting question for the search is exactly **which `j` first fails** —
  that is the binding constraint, and it is what the searcher hunts over.
- `score = 0` is a generic polynomial with no shared-root structure at all.

## The trivial family (why it is rejected)

`(x-a)^20` shares a root with **all** 19 derivatives (the root `a` to
multiplicity 20). It would trivially score 19 — but it is precisely the family
the conjecture allows as the only satisfiers, so it carries no information.
The scorer must reject it with `INVALID`. This is the "obvious exploit" of the
search and rejecting it is what keeps the score distribution meaningful.

## Valid inputs and the scorer's contract

`score.py` takes one command-line argument — a path to a candidate module —
imports it, and looks for a polynomial it exposes. Contract (verbatim):

- expecting the module to expose a **monic degree-20 polynomial over `Q`** in
  `x` (any attribute name, conventionally `f`).
- prints exactly one line `SCORE: k` where `k` is computed exactly as above via
  sympy over `QQ`; no floats anywhere.
- answers `INVALID: <reason>` when:
  - **(a)** `f` is `(x-a)^20` for some `a` (the trivial family — the exploit);
  - **(b)** `f` is not monic, not degree exactly 20, or has non-rational
    coefficients;
  - **(c)** the module fails to import or does not expose the polynomial.

The import is done robustly with `importlib` from the literal path given, so
the candidate never needs to be on `PYTHONPATH`.

## What counts as "the score distribution" vs "which constraint binds"

A candidate module's score is a single integer. The distribution and the
binding constraint emerge only from **running many candidates** — which is the
searcher role's job, not this one. `score.py` merely instruments one candidate.
The searcher should record, over its population of candidates, the histogram
of scores and, for each near-miss, the first `j` at which
`deg(gcd(f, f^(j))) = 0`.

## Files

- `PROBLEM.md` — this file: what the search is and why score is exact.
- `score.py` — the scorer. One candidate module path on argv → exactly one
  line, `SCORE: k` or `INVALID: <reason>`.
- `smoketest.txt` — the scorer self-test on four cases (see below),
  recorded by this pass.
- `smoketest/` — the four tiny candidate modules used by the self-test.

## Smoke test (already run, see `smoketest.txt`)

1. `x^20 - x` — genuine candidate; shares a root (`0`) with `f''..f^(19)`
   (their leading terms are scalar monomials vanishing at 0) but not with
   `f'`. Expected `SCORE: 18`.
2. `(x-3)^20` — the trivial family; must give `INVALID: ...(x-a)^20...`.
3. degree-19 / non-monic — must give `INVALID:` for the correct reason.
4. a module exposing no polynomial — must give `INVALID:` (wrong import /
   no polynomial).

These four are run and recorded in `smoketest.txt` by the tool-builder pass
that wrote the scorer.
