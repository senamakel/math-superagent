# The Erdős–Straus conjecture

## Statement

**Conjecture (Erdős–Straus, 1948).** For every integer `n >= 2` there exist
positive integers `x, y, z` with

```
4/n = 1/x + 1/y + 1/z
```

The conjecture is believed **true** and is verified numerically to very large
bounds. The objective here is a proof or a genuine partial result — new
covering identities for open congruence classes, not another verification
sweep.

## Why identities, not search

The problem has a **covering-system** structure that makes it unusually
tractable to attack symbolically. A single polynomial identity settles an
entire congruence class at once, forever, with no computation per `n`.

The reduction that does most of the work:

- It suffices to treat `n = p` **prime**. If `4/p` is solvable and `m` is a
  multiple of `p`, scaling a solution for `p` by `m/p` solves `m`. So only
  primes are open, and the composite case follows.
- `n` even is trivial: `4/(2m) = 2/m = 1/m + 1/m`, so `4/n = 1/m + 1/(2m) + 1/(2m)`
  with `m = n/2`. Verify this before using it.
- `n ≡ 3 (mod 4)` is covered by the identity in the task brief:

```
4/n = 1/n + 1/((n+1)/2) + 1/(n(n+1)/2)
```

  **Check it symbolically before relying on it.** It is stated here as a lead,
  not as an established fact of this workspace.

Iterating identities of this shape over small moduli kills every residue class
except a handful. The standard statement is that only

```
n ≡ 1, 121, 169, 289, 361, 529   (mod 840)
```

remain open — note that all six are **squares mod 840** (`1, 11², 13², 17²,
19², 23²`), which is not a coincidence and is the structural fact any serious
attempt has to engage with. Confirm this list and the reason for it from a
primary source; do not carry it on this file's word.

## The target

Find explicit **parametric identity families** — polynomials or rational
functions `x(k), y(k), z(k)` with `n = 840k + r` — covering the open classes,
`r = 1` first.

The obstruction, stated honestly: identities of the usual *type I / type II*
shapes have been searched extensively and the residual classes are exactly the
ones that resist them. So a naive symbolic search over low-degree ansätze will
rediscover known families and stop. Any approach must say **how it differs**
from what has already been tried, and what makes it able to reach `n ≡ 1
(mod 840)`.

## The structure worth exploiting

Write a solution in the standard **type I** form: there exist positive
integers `a, b, c, d` with

```
4abcd = n(ab + cd + bd)     or similar Mordell-style parametrisations
```

Several equivalent formulations exist and they are not interchangeable in
practice — one may admit a polynomial family where another does not. Establish
the exact parametrisation this run will use, verify it against a known
solution, and record it before building on it.

Two structural facts worth checking early, each as its own claim:

- **Solvability is equivalent to a congruence-plus-representation condition.**
  For prime `p`, `4/p` is solvable iff certain quadratic conditions hold;
  Mordell's analysis is the standard reference for which classes are settled
  and why the six squares resist.
- **The open classes are quadratic residues.** `1, 121, 169, 289, 361, 529` mod
  840 are all squares. The known identity families produce solutions via
  factorisations that fail precisely when `n` is a square in the relevant
  modulus — find the exact statement of that failure, because it tells you what
  a new family must avoid.

## Leads — verify each before relying on it

Not established facts here. Each needs a primary source and a claim block with
its own status.

- **Mordell**, *Diophantine Equations* — the classical treatment of which
  congruence classes are settled by identities.
- **Elsholtz and Tao**, *Counting the number of solutions to the Erdős–Straus
  equation on unit fractions* — the modern reference; gives strong average
  results, bounds on the number of solutions, and a clear account of exactly
  which classes remain and why. This is the single most useful source for this
  run.
- **Vaughan** — earlier bounds on the count of exceptional `n` up to `x`.
- **Verification bounds** — reported ranges vary; state the bound this run
  reproduces separately from the bound the literature claims.
- **The `5/n` and `4/n` analogues (Sierpiński, Schinzel)** — the general
  `k/n` problem; results there sometimes transfer.
