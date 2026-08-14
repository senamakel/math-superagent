# Skeleton — the two exponent-2 cases, proved in full in-workspace

This decomposes GOAL.md deliverable "the exponent-2 cases proved in full, both
of them". The other skeletons carry `G-exp2-a` / `G-exp2-b` as single
monolithic gaps; this file breaks each into elementary sub-lemmas a
theorem_prover can close today in Z and Z[i], with no external source (which
CONTEXT.md says is dead at the network layer anyway). It is the foundation
every later lemma is calibrated against, because it is the only part of the
full proof whose conclusion must *contain* the known solution.

```skeleton
goal: >
  (A) x^2 - y^q = 1 with x, y > 0 and q prime has exactly the solution
  (x, y, q) = (3, 2, 3); and (B) x^p - y^2 = 1 with x, y > 0 and p prime has
  no solution. Together these are the two exponent-2 cases of
  x^p - y^q = 1.
implies: >
  (A) x = 1 gives y^q = 0, excluded, so x >= 2. If q = 2 then
  (x - y)(x + y) = 1 forces x + y = 1 and hence y = 0, excluded; so q is an
  odd prime. Split on x: if x is even, gap exp2-a-even shows no solution;
  if x is odd, gap exp2-a-odd-descent shows (x, y, q) = (3, 2, 3). The two
  sub-cases are exhaustive, so (A) holds.
  (B) If p = 2 then (x - y)(x + y) = 1 forces y = 0, excluded; so p is an
  odd prime. Gap exp2-b-nosolution shows no solution for p odd, hence (B).
  The known solution (3, 2, 2, 3) satisfies (A) at (x, y, q) = (3, 2, 3)
  — exp2-a-odd-descent must *return* it, never exclude it — and lies outside
  (B)'s hypothesis (its y-exponent is 3, not 2).
status: sketched
rests-on: none — research/CLAIMS.md is empty and search_claims finds no claim.
killed-by: none
```

```gap
id: exp2-a-even
lemma: >
  x^2 - y^q = 1 with x, y > 0, x even, and q an odd prime, has no solution.
status: open
known-solution: the known solution has x = 3 odd, so it is outside the
  hypothesis; this lemma is silent about it and claims no solution only for
  even x.
next: >
  theorem_prover / lean_prover: if x is even then x-1 and x+1 are odd and
  coprime (their gcd divides 2 and is odd, hence 1), and their product is
  y^q. A q-th power written as a product of two coprime integers has both
  factors q-th powers, so x-1 = a^q and x+1 = b^q with b > a >= 1; then
  b^q - a^q >= (a+1)^q - a^q >= 2^q - 1 >= 7 for q >= 3, contradicting
  b^q - a^q = 2. Formalise in Mathlib, report #print axioms, no sorry.
  Cross-check with the exact-integer oracle solutions(N): for even x below
  the reachable N, x^2 - 1 is never a q-th power for odd prime q.
```

```gap
id: exp2-a-odd-descent
lemma: >
  x^2 - y^q = 1 with x >= 3 odd, y > 0, and q an odd prime, has exactly the
  solution (x, y, q) = (3, 2, 3).
status: open
known-solution: this is the positive case — (3, 2, 3) is the unique solution
  it asserts, so the lemma must return it and must not be stated as
  "no solutions".
next: >
  First the exact reduction (symbolic_math, exact integer/cyclotomic-free):
  x odd gives x-1 = 2u, x+1 = 2v with gcd(u,v) = 1 and v-u = 1, and y is
  even, y = 2^m z with m >= 1 and z odd. Then uv = y^q/4 = 2^{mq-2} z^q, and
  gcd(u,v)=1 forces {u,v} = {r^q, 2^{mq-2} s^q} for coprime r,s >= 1 with
  z = rs; v-u = 1 becomes r^q - 2^{mq-2} s^q = +-1. Then the descent
  (theorem_prover): prove that this Thue-type equation, with q an odd prime,
  m >= 1, r,s >= 1, gcd(r,s) = 1, has only the solution q = 3, m = 1,
  r = s = 1 — the classical Lebesgue descent for x^2 = y^n + 1. That solution
  gives u = 1, v = 2, hence x = 3, y = 2^m rs = 2. symbolic_math checks the
  reduction and each descent step on small cases; lean_prover formalises the
  descent and the parity split. Falsifier: solutions(N) must show no odd x
  other than 3 with x^2 - y^q = 1 below the reachable bound.
```

```gap
id: exp2-b-nosolution
lemma: >
  x^p - y^2 = 1 with x, y > 0 and p an odd prime has no solution.
status: open
known-solution: the known solution has y-exponent 3, not 2, so it is outside
  the hypothesis; the lemma is silent about it.
next: >
  theorem_prover / lean_prover in Z[i]. Parity first: if y is odd then
  y^2 + 1 = 2 (mod 4), which is not a p-th power, so y is even. Then
  x^p = (y+i)(y-i) with gcd(y+i, y-i) = 1 (a common divisor divides 2i and
  has norm dividing the odd integer y^2+1, so it is a unit), hence
  y+i = u (a+bi)^p for a unit u; since p is odd every unit of Z[i] is a
  p-th power, so absorb u and write y+i = (a+bi)^p. The imaginary part of
  (a+bi)^p is b times an integer, so b | 1 and b = +-1. Then reduce
  (a +- i)^p = y +- i modulo p: for p = 3 (mod 4) this gives 1 = -1 (mod p),
  impossible; for p = 1 (mod 4) compare the real parts of (a +- i)^p to y to
  force a = 0 and then y = 0, contradicting y > 0. symbolic_math expands
  (a+bi)^p symbolically and verifies the b-divisibility of the imaginary part
  and the mod-p congruence; lean_prover formalises. The p = 2 case is the
  difference of squares (x-y)(x+y) = 1 and must stay outside the odd-prime
  hypothesis. Falsifier: never state this for p = 2.
```

## Where this sits in the full proof

`exp2-a-even` and `exp2-a-odd-descent` jointly discharge the `G-exp2-a` gap of
`reduce-to-prime-exponents.md` and `catalan-mihailescu-full.md`;
`exp2-b-nosolution` discharges their `G-exp2-b`. None is discharged yet — no
claim blocks exist in `research/CLAIMS.md`, so all three are open. This file is
the in-workspace re-derivation of the two classical exponent-2 results
(Lebesgue), which the calibration workspace requires to be re-derived rather
than fetched.
