# Schuh, "The Erdős–Straus Conjecture and Pythagorean Primes" (2025)

Source: https://arxiv.org/abs/2503.11672 (arXiv:2503.11672, 26 Feb 2025),
Bernd R. Schuh.
Full text: `research/sources/schuh-pythagorean-primes.full.md`

## What it establishes (sourced, preprint)

Works on **Pythagorean primes** p ≡ 1 (mod 4) — the superclass containing all
six open classes mod 840. Introduces `β(w) = 4w − 1` (the r ≡ 3 mod 4 helper).

**Theorem 1 (two-equation reduction).** For n prime, (1) `4/n = 1/x+1/y+1/z`
is solvable iff one of the two equations

```
(A)  z(β(a)n − a) = d              (B)  z(β(a) − na) = d
```

is solvable, with d a divisor of a² (a = x/n since n | x). From (A):
`x = an, y = az/d, z = z`; from (B): `x = an, y = naz/d, z = z`.

**Consequence (corollary):** for a Pythagorean prime, solutions of (A) are
Type I (exactly one denominator divisible by n), solutions of (B) are Type II.

**Theorem 2A (Type I / equation A).** Equation (A) is solvable in a prime
n = 4K+1 **if** K has the form

```
K = β(b)·(μ−1)·κ − b      for some b, μ, κ ∈ N     (5)
```

i.e. n = 4β(b)μκ − 4β(b)κ − 4b + 1. Setting b=μ=1 gives K = κ² − 1 (all odd
K, hence tern all n ≡ 1 mod 4 with odd K); μ=κ=1 gives K = 3b − 2.

**Theorem 2B (Type II / equation B).** Equation (B) is solvable in a prime
n = 4K+1 **if and only if** K = β(a)(μ − 1) − a − d, i.e.

```
n = 4β(a)μ − 4a − 4d − 4(a+1) ...  (equivalently n = 4aβ(a)... see (9))
```

with a, μ ∈ N and d a divisor of a² (equ. (9)). This is a **necessary and
sufficient** four-parameter family for Type-II solutions of Pythagorean
primes. Writing d = a₁a₂ with a₁a₂ | a², condition (9) becomes (11):
`4β(λa₁)/ν ... = n/a₂` — the parametrisation `S_B`.

**Lemma 1.** For equation (A) to be solvable, a must be composite.

**Lemma 2.** `S_A` contains infinitely many primes — by Iwaniec's theorem on
irreducible binary quadratic forms (n = β(b)·xy − x − y with x = μ... ).

**Conjecture A.** Every Pythagorean prime belongs to S_A (three-parameter
family (5)); every member of S_A gives a solution to (1), so ESC follows from
A. Verified by the author for many-digit primes (algorithm given) and
previously by Hernández–Benito–Fernández (arXiv:1010.2035) for p ≡ 1 mod 4,
p < 10^14 — they also proved S_A contains no perfect squares.

**Conjecture B.** Every Pythagorean prime belongs to S_B (four-parameter
family (11)); ESC implies B (B is necessary), B suffices.

## Relation to the rest of the library

- Theorem 2B is the same Type-II characterisation as **Chamberland (Integers
  2026, in library) Theorem 1**, `p = qr − 4s₁s₂`, and both trace to the same
  arithmetic.  The necessity direction is the striking part: Type-II solutions
  of Pythagorean primes are in bijection with the four-parameter family.
- Ionescu–Wilson arXiv:1001.1100 (in library, misnamed ionascu-wilson) is
  the same Hernández–Benito–Fernández trio.
- This is the only source in the library that makes the Type-I *parametrisation
  issue* explicit: (5) is sufficient but **not** necessary for Type I, i.e. the
  Type-I side has no known complete four-parameter family; only the Type-II
  side is both necessary and sufficient.

## Consequences for the run

Since the six open classes are Pythagorean primes, *any* n ≡ 1 (mod 840) that
has a Type-II solution must satisfy Chamberland's/Schuh's necessary-and-
sufficient four-parameter family — and conversely every member of that family
is solved. So for the construction phase: **Type-II solutions of n ≡ 1 mod 840
are exactly `n = 4β(a)μ − 4a − 4d − ...` with d | a², and a sub-family (S_A,
three parameters) accounts for Type-I solutions, but S_A does not exhaust
Type I.** A search for new covering families can restrict to these shapes
without loss for Type II.

```claim
id: schuh-theorem2b-typeII-necessary-sufficient
statement: For n = 4K+1 prime, 4/n has a Type-II solution iff K = β(a)(μ−1) − a − d for some a, μ ≥ 1 and d | a² (equ. (9)); equivalently the four-parameter family S_B parametrises all Type-II solvable Pythagorean primes.
hypotheses: n prime, n ≡ 1 mod 4, Type-II solution (exactly two of x,y,z divisible by n).
holds-here: true — the six open classes consist of Pythagorean primes, so any Type-II cover of n ≡ 1 (mod 840) must lie in S_B; conversely every member of S_B is solved.
status: asserted (Schuh 2025 preprint Theorem 2B, proof in full text; consistent with Chamberland 2026 Theorem 1 and the classical Type-II (Type 2) parametrisation of Elsholtz–Tao §2.6).
bearing: the only known *complete* parametrisation of a solution type for the open classes; a necessary-and-sufficient ansatz family for Type II.
anchor: research/sources/schuh-pythagorean-primes.full.md
```

```claim
id: schuh-typeA-not-necessary
statement: The three-parameter family (5) is sufficient but NOT necessary for Type-I solutions of Pythagorean primes; a complete Type-I parametrisation is not given.
hypotheses: equation (A) of Theorem 1, prime n ≡ 1 mod 4.
holds-here: true — marks the boundary of what a Type-I ansatz can claim: no covering Type-I family of the (5) shape can be complete.
status: asserted (Schuh 2025, Lemma 1 + "unfortunately, condition (5) is only sufficient"; the necessary form (8) is a six-parameter family).
bearing: a Type-I-only search cannot be exhaustive; the run's emptiness claims must be Type-II-complete or degreed.
anchor: research/sources/schuh-pythagorean-primes.full.md
```