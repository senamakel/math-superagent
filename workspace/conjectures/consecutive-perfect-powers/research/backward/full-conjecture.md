# Skeleton — the full conjecture

```skeleton
goal: The only solution of x^p - y^q = 1 in integers x,y > 0, p,q > 1 is
      (x,p,y,q) = (3,2,2,3).
implies: Partition the prime-exponent pairs (p,q) into {p = 2}, {q = 2}, and
      {p,q both odd primes}; these three are exhaustive and disjoint.
      G-full-prime-reduction shows it suffices to treat prime p,q (a composite
      exponent p = P*a yields the prime-exponent solution (x^a)^P - y^q = 1,
      applied to both exponents). G-full-case-p2 disposes of p = 2 and returns
      exactly (x,y,q) = (3,2,3), i.e. (x,p,y,q) = (3,2,2,3). G-full-case-q2
      shows q = 2 gives no solution. G-full-odd-odd shows both-odd-primes gives
      no solution. Hence the only prime-exponent solution is (3,2,2,3), and by
      the reduction it is the only solution at all.
status: sketched
rests-on: (none — fresh run; no claim recorded yet)
```

```gap
id: G-full-prime-reduction
lemma: If x^p - y^q = 1 with x,y >= 2 and p,q >= 2 integers, then there exist
       X,Y >= 2 and primes P,Q with X^P - Y^Q = 1; concretely, writing p = P*a,
       q = Q*b with P,Q prime gives (X,Y) = (x^a, y^b). Consequently a
       classification of all prime-exponent solutions is a classification of
       all solutions.
status: open
known-solution: (3,2,2,3) has prime exponents already; the reduction fixes it.
next: hand the statement to theorem_prover / lean_prover as a three-line
      argument (X = x^a preserves equality and positivity). Verify with the
      exact-integer oracle on composite exponents, e.g. (4,4,?): 2^4 = 4^2 = 16
      has no y with y^q = 15; the reduction must only ever produce *existing*
      prime-exponent solutions from existing ones, never manufacture one.
```

```gap
id: G-full-case-p2
lemma: The only solution of x^2 - y^q = 1 in integers x,y >= 1, q >= 2 prime,
       is (x,y,q) = (3,2,3).
status: open
known-solution: (3,2,2,3) IS this lemma's unique solution; the lemma must be
       exact (admit it and nothing else), or it is wrong in the other
       direction.
next: rederive in Z: q = 2 gives (x-y)(x+y) = 1, no positive solution; q odd
      forces x odd, gcd(x-1,x+1) = 2, so (x-1)/2 and (x+1)/2 are coprime with
      product y^q/4, hence both q-th powers of coprime integers a,b with
      b - a = 1; force q = 3, a = 1, b = 2. Run the descent in symbolic_math,
      then formalise in Lean (Mathlib has the number-theory primitives).
```

```gap
id: G-full-case-q2
lemma: x^p - y^2 = 1 has no solution in integers x,y >= 1, p >= 2 prime.
status: open
known-solution: (3,2,2,3) has q = 3, so it lies *outside* the hypothesis q = 2;
       the lemma is silent about it. This is exclusion by hypothesis, not an
       over-strong claim — the falsifier confirms the lemma does not apply.
next: rederive in Z[i]: p = 2 gives (x-y)(x+y) = 1, impossible; p odd forces
      x odd and y even, x^p = (y+i)(y-i) with the two factors coprime in Z[i],
      so y+i = u(a+bi)^p for a unit u; subtracting the conjugate and comparing
      imaginary parts (binomial expansion) forces b = +-1 and then p | a^2+b^2,
      a contradiction. symbolic_math for the binomial step, then Lean.
```

```gap
id: G-full-odd-odd
lemma: x^p - y^q = 1 has no solution in integers x,y >= 2 with p,q odd primes.
status: open
known-solution: (3,2,2,3) has p = 2 (even), so it lies outside the hypothesis;
       the lemma must be silent about it, never refuted by it.
next: this is the open content and is itself a sub-goal; see
      research/backward/odd-prime-case.md. First concrete move: reconstruct
      Cassels' theorem (gap G-odd-cassels there) — p | y and q | x — which is
      the entry to every divisibility condition downstream.
```

## What the two exponent-2 gaps buy

G-full-case-p2 and G-full-case-q2 together close the reduction to "both
exponents odd primes", which is the hypothesis every later lemma in
`odd-prime-case.md` assumes. They are also the calibration for the
falsification oracle: the known solution (3,2,2,3) must be admitted by the p=2
case and excluded *by hypothesis only* from the q=2 and odd-odd cases.
