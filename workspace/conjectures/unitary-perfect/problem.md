# Erdős problem 1052 — are there only finitely many unitary perfect numbers?

https://www.erdosproblems.com/1052

A **unitary divisor** of `n` is a divisor `d | n` with `gcd(d, n/d) = 1`.
Equivalently, `d` is a product of full prime-power components of `n`: if
`p^a || n` then `d` contains `p^a` or no power of `p` at all.

Write `σ*(n)` for the sum of the unitary divisors of `n`. It is multiplicative
over prime powers with

```
σ*(p^a) = p^a + 1
```

so `σ*(n) = Π_{p^a || n} (p^a + 1)`.

`n ≥ 1` is **unitary perfect** if it is the sum of its unitary divisors other
than itself, i.e.

```
σ*(n) = 2n.
```

**The question is whether there are only finitely many.** It is open. Nobody
has proved finiteness and nobody has produced a sixth example.

## The five known

```
6                        = 2 · 3
60                       = 2^2 · 3 · 5
90                       = 2 · 3^2 · 5
87360                    = 2^6 · 3 · 5 · 7 · 13
146361946186458562560000 = 2^18 · 3 · 5^4 · 7 · 11 · 13 · 19 · 37 · 79 · 109 · 157 · 313
```

The first four are Subbarao–Warren (1966); the fifth is Wall (1975). All five
are verified in this workspace against the exact integer oracle, in
`code/out/known_five_verified.captured.txt`.

**Wall searched past 10^102 and found no sixth.** That number is the reason the
obvious instrument is the wrong one; see `GOAL.md`.

## The form the problem actually has

Dividing `σ*(n) = 2n` by `n` turns the additive statement into an exact product
identity over the unitary components:

```
Π_{p^a || n} (1 + 1/p^a) = 2
```

so a unitary perfect number *is* a way of writing `2` as a product of terms
`(q+1)/q` with `q = p^a` running over prime powers of **distinct** primes.
Equivalently, in the form the recent literature uses, with `2^a || n` kept
explicit and `p_i` odd:

```
(2^a + 1) · Π_i (p_i^{e_i} + 1) = 2^{a+1} · Π_i p_i^{e_i}
```

This is the "full balance". It is a finite, exact Diophantine condition with no
analytic slack in it, which is why partial results take the form of eliminating
structural classes rather than shrinking a search region.

## What is already known, and must not be re-derived

- **There is no odd unitary perfect number** (Subbarao–Warren 1966). The proof
  is three lines and is written out in
  `research/notes/parity-and-2-adic-budget.md`. Every unitary perfect number is
  even, so `a ≥ 1` always.
- **All five known examples are divisible by 3.** Whether a sixth must be is
  open and is one of the live structural questions.
- **Graham (1989)** determined all unitary perfect numbers with squarefree odd
  part: they are exactly `6`, `60`, `87360`. So any sixth example has a
  non-squarefree odd part — a repeated odd prime, as in `90 = 2 · 3^2 · 5` and
  in the fifth example's `5^4`.
- **Subbarao** conjectured that there are only finitely many, which is this
  problem.

## The current structural frontier

Maciejewski, *Bounded-box reductions in the Subbarao–Warren problem for unitary
perfect numbers*, arXiv:2605.20475 (May 2026). Its abstract is held in this
workspace; **the full text is not, and getting it is the librarian's first
task.** From the abstract:

- It keeps the seed factor `2^a + 1` explicit in the full balance above.
- Within a bounded enumeration of source components of the *odd dependency
  graph*, every admissible **source kernel** is either one of the two kernels
  occurring in the known non-squarefree examples — `3^2` and `5^4` — or one of
  **five additional "impostor" kernels**.
- It gives a reproducible three-filter certificate eliminating those impostor
  kernels for all relevant seed classes with `1 ≤ a ≤ 10000`, combining
  Zsigmondy-type exponent obstructions, inherited non-3-Higgs witnesses, and
  deterministic 2-adic budget overshoot.
- **It does not prove finiteness.** What is left is one branch, controlled by
  the auxiliary set

  ```
  H_even = { even m : every prime divisor of 2^m + 1 is 3-Higgs }
  ```

  with the stated bounds `|H_even ∩ [2, 40000]| ≤ 201` and
  `|H_even ∩ [2, 50000]| ≤ 272`, and the stated analytic target being a
  divisor-level problem for the cyclotomic values `Φ_{4p}(2)`.

The definition of a *3-Higgs* prime, the construction of the odd dependency
graph, the five impostor kernels, and the three filters are **not** in this
workspace. They are in the paper. Do not guess them.
