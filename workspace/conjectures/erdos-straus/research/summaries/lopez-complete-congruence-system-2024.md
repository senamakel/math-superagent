# Lopez, "A Complete Congruence System for the Erdős–Straus Conjecture"

Source: https://arxiv.org/abs/2404.01508 (arXiv:2404.01508v3, 15 Apr 2024, 19 pp),
Miguel Angel Lopez (UCM). Full text:
`research/sources/lopez-complete-congruence-html.full.md`.

## What it establishes

A **transversal classification of Erdős–Straus solutions by form** (not by
residue class), defined to sit inside the standard Type-II family but to
isolate the congruences that each specific *shape* can solve. All of it is
for the hard case `p ≡ 1 (mod 4)`.

**Type A** — solution shape `(du, dv, duv)`, i.e. one denominator the product
of the other two:
- For prime `p = 4k+1`, a Type-A solution exists **iff** there is `t ≥ 0` and a
  divisor `w | k+1+t` with `w ≡ −1 (mod 3+4t)` (Theorem 1, from Lopez 2022
  arXiv:2206.10319). Equivalently (**Thm 7**) iff `∃ d,n : p ≡ −4d (mod 4dn−1)`.
- Every prime `p ≢ 1 (mod 24)` has a Type-A solution (the `t=0` case).

**Type B** — solution shape `(duv, dup, dvp)` (two denominators carry the
prime):
- For prime `p = 4k+1`, a Type-B solution exists **iff** `∃ d,n : p ≡ −n
  (mod 4dn−1)` (Theorem 4), equivalently (`Thm 6`) iff `∃ t ≥ 0` and divisors
  `a,b | k+1+t` with `a+b = 3+4t`.

**Conjecture 1**: every prime `p` has a Type-A *or* Type-B solution, i.e. lies
in the union of the congruence systems `p ≡ −4d (mod 4dn−1)` and
`p ≡ −n (mod 4dn−1)`. Verified experimentally for all primes ≤ 104729
(first 10,000 primes). If true, ESC follows: each congruence carries a
polynomial identity off the quadratic-residue obstruction (Mordell).

**Theorem 8 — the three polynomial generators** (all ≡ 1 mod 4, variables
natural):
- `P(x,y,t) = (4xy−1)(3+4t) − 4x²y` ⇒ Type B.
- `Q(x,y,t) = (4xy−1)(3+4t) − 4y` ⇒ Type A.
- `R(x,y,t,z) = (4xyz−1)(3+4t) − 4x²y` ⇒ Type II (general).
- `R(x,y,t,1) = P(x,y,t)`; `R(1,y,t,x) = Q(x,y,t)`.
- The `y=1` reduction `R(x,1,t,z)=(4xz−1)(3+4t)−4x²` is called **Type C**
  (`Thm 9`): `n = R(x,1,t,z)` iff `−n ≡ 4d² (mod 4dm−1)` iff there are divisors
  `a,b | k+1+t` with `3+4t | a+b`. Conjecture 2 adds this Type-C congruence
  `p ≡ −4d² (mod 4dn−1)`.

**Two primes are special** (both of them ≡ 1 mod 24, one in an open class):
among the first 9000 naturals the **only** primes lacking Type-A solutions are
**193** and **2521**; both have Type-B solutions (Theorem 6). `2521` has only
one Type-B solution with associated moduli 87 and 1275 (neither prime). Lopez
observes all primes ≡ 1 (mod 840) have all of 1..10 as quadratic residues
mod p — "perhaps in part because of this special property" that the class is
so resistant.

## Implication for this run

- This is a **2024 primary source giving new family shapes** (the Type A/B/C
  congruence/divisor systems) that are distinct coordinates from the standard
  Type-I/II and from Salez's "seven equations are complete for degree-1". It
  does **not** contradict Schinzel/Salez: those rule out *single-class*
  polynomial identities for the six open residues; Lopez's system is a
  *covering by sub-progressions* inside `4dn−1`, which is exactly the regime
  the run's `search_subprogression` machinery (moduli 11..43) operates in.
- **2521 ≡ 1 (mod 840)** is a run witness (`code/out/witnesses.json`) — the
  paper's claim that 2521 lacks Type A but has Type B is directly checkable
  against the oracle and is a concrete, independent structural property of a
  prime in the run's target class.
- The congruence forms `p ≡ −4d`, `p ≡ −n`, `p ≡ −4d² (mod 4dn−1)` are a
  natural additional ansatz family for the saturation question (modulus 11):
  vary `d, n` and test which residues of `t = (n−1)/840` the resulting
  polynomial identities cover.

## Status

Asserted-by-source (the congruences/conjectures/proofs are in the full text;
the run has not verified them against its oracle). Theorems 1–9 are proved in
the paper; Conjectures 1–2 are experimental (first 10,000 primes).

```claim
id: lopez-type-b-iff-congruence
statement: For prime p = 4k+1, a Type-B solution (duv, dup, dvp) of
  4/p = 1/x+1/y+1/z exists iff there exist d,n ∈ N with p ≡ −n (mod 4dn−1),
  equivalently iff ∃ t ≥ 0 and divisors a,b | k+1+t with a+b = 3+4t; such a
  solution is of Type II.
hypotheses: p prime, p = 4k+1
holds-here: yes (the open classes are all ≡ 1 mod 4)
status: asserted
bearing: a new sub-progression congruence family p ≡ −n (mod 4dn−1) to test
  against the run's six open classes and its saturation question; the solving
  x,y,z are polynomial in p once d,n are fixed, so this is a candidate
  generator for the modulus-11 saturation families.
anchor: research/summaries/lopez-complete-congruence-system-2024.md
```

```claim
id: lopez-type-a-b-only-exceptions-193-2521
statement: Among the first 9000 natural numbers the only primes lacking a
  Type-A solution (du, dv, duv) are 193 and 2521; both have a Type-B solution
  (193: 5(10, 386, 965); 2521: 11(58, 5042, 73109)).
hypotheses: p prime ≤ 9000, Type-A as defined
holds-here: yes (2521 ≡ 1 mod 840 is a run witness in an open class)
status: asserted
bearing: 2521 ≡ 1 (mod 840) is one of this run's verified witnesses (n=2521);
  the claim that it lacks Type A but has Type B is a concrete structural
  property of a prime in the target class, checkable against the oracle.
anchor: research/summaries/lopez-complete-congruence-system-2024.md
```

