# Weakener ladder: Catalan / consecutive perfect powers

`x^p - y^q = 1`, `x,y > 0`, `p,q > 1`. The goal is the negative statement that
`(3,2,2,3)` is the only solution.

Two tracks meet in this ladder. The **exponent track** (R0–R7) turns the
exponents back on: fixed instance → one-exponent-is-2 → both odd → unbounded.
The **cyclotomic track** (R8–R10) is the one the full proof actually runs on:
it stops asking "is there none?" and instead constrains a hypothetical
both-odd solution, then removes the class-group hypothesis last. R10→goal is
where the open content lives.

Difficulty glossary (the short names in the `difficulties` field):

- `negative-claim` — the target is a negative/uniqueness statement; the
  characteristic failure is over-elimination that kills `(3,2,2,3)`. Every
  rung states where the known solution sits.
- `unbounded-exponents` — `p,q` range over all integers `>1` (all primes after
  the reduction), so no finite case split.
- `unbounded-bases` — `x,y` unbounded, and once both exponents are odd there is
  no elementary a priori bound.
- `both-odd` — both exponents odd prime ⇒ no factorisation in `Z` or `Z[i]`;
  the equation moves into `Q(zeta_p)`.
- `class-group` — ideals of `Z[zeta_p]` need not be principal; the
  ideal→element conversion is the obstruction the problem statement names.
- `p-neq-q` — the exponents are distinct primes (`p=q` is trivially empty).
- `uniqueness` — the goal must pin the solution set to exactly `{(3,2,2,3)}`,
  not merely show it is finite.

```ladder
goal: determine all integer solutions of x^p - y^q = 1 with x,y > 0, p,q > 1; believed to be exactly (x,p,y,q) = (3,2,2,3)
difficulties: negative-claim, unbounded-exponents, unbounded-bases, both-odd, class-group, p-neq-q, uniqueness
status: open
```

```rung
id: R-known-instance
statement: the instance (x,p,y,q) = (3,2,2,3) satisfies 3^2 - 2^3 = 1
off: negative-claim, unbounded-exponents, unbounded-bases, both-odd, class-group, p-neq-q, uniqueness
stance: settled
merge: anchor only, nothing to turn on. The known solution sits inside this rung by definition; every higher rung must be checked against it. Next rung: R-trivial-bases.
```

```rung
id: R-trivial-bases
statement: there is no solution with x = 1 or y = 1; equivalently every solution has x >= 2 and y >= 2
off: unbounded-exponents, unbounded-bases, both-odd, class-group, p-neq-q
stance: open
merge: one-line proof available for the forward loop: x=1 forces y^q = 0 (excluded), y=1 forces x^p = 2 (impossible for integer x>=1, p>=2). Turning unbounded-bases back on with the single smallest nontrivial exponent pair is R-fixed-23; first move: factor y^3 = (x-1)(x+1) with gcd(x-1,x+1) in {1,2}.
```

```rung
id: R-fixed-23
statement: x^2 - y^3 = 1 has (x,y) = (3,2) as its only solution in integers x,y > 0; the known solution (3,2,2,3) is exactly the claimed one
off: unbounded-exponents, both-odd, class-group, p-neq-q
stance: open
merge: classical (Euler / Mordell), re-derive via (x-1)(x+1) = y^3 and the gcd argument, handling the 2-torsion. Turning unbounded-exponents partially on while keeping p = 2 is R-exp2; first move: the same factorisation with q-th-power extraction, gcd(x-1,x+1) | 2.
```

```rung
id: R-exp2
statement: for every odd prime q, x^2 - y^q = 1 has (x,y,q) = (3,2,3) as its only solution in x,y > 0; the known solution sits at q = 3
off: both-odd, class-group, p-neq-q
stance: open
merge: classical (Lebesgue 1850); gcd(x-1,x+1) is 1 or 2, so each factor is a q-th power up to a factor of 2. Mirror it in R-exp2-mirror; first move: write x^p = (y+i)(y-i) in Z[i].
```

```rung
id: R-exp2-mirror
statement: for every odd prime p, x^p - y^2 = 1 has no solution in x,y > 0; the known solution has q = 3, so it sits outside this rung's case
off: both-odd, class-group, p-neq-q
stance: open
merge: classical (Lebesgue); x^p = y^2 + 1 = (y+i)(y-i) with the two Z[i]-factors coprime, forcing y+i to be a p-th power, and comparing imaginary parts contradicts. Together R-exp2 and R-exp2-mirror close the exponent-2 content. Turning both-odd on in its symmetric special case is R-p-eq-q; first move: the inequality x^p - y^p >= (y+1)^p - y^p > 1.
```

```rung
id: R-p-eq-q
statement: for every odd prime p, x^p - y^p = 1 has no solution in x,y > 0; the known solution has p = 2 != 3 = q, so it sits outside
off: p-neq-q
stance: open
merge: immediate for the forward loop: x^p - y^p = (x-y)(x^{p-1}+...+y^{p-1}) is a product of two positive integers, so it equals 1 only if both are 1, but the second factor is >= p >= 3. Turning p-neq-q on with exponents fixed is R-fixed-pq; first move: apply Siegel/Faltings to the curve X^p - Y^q = 1.
```

```rung
id: R-fixed-pq
statement: for every fixed pair (p,q) of distinct odd primes, x^p - y^q = 1 has at most finitely many solutions in x,y > 0, and the solutions are effectively computable; the known solution sits outside the hypothesis p,q odd
off: unbounded-exponents, uniqueness, negative-claim
stance: open
merge: finiteness by Siegel (genus >= 1) / Faltings (genus >= 2) on the Fermat-type curve, effectivity by Baker's linear forms in logs; attributed, verify against a primary source. Turning unbounded-exponents on while keeping only finiteness is R-uniform-finite; first move: Tijdeman's uniform bound.
```

```rung
id: R-uniform-finite
statement: the full equation x^p - y^q = 1 has finitely many solutions over all x,y > 0, p,q > 1; the known solution (3,2,2,3) is one of the finitely many
off: uniqueness, negative-claim
stance: open
merge: Tijdeman (1976), asserted in problem.md; the effective bound is astronomically larger than any feasible search, so this rung is a theorem, not a computation. Turning uniqueness back on is the full goal and is where the ladder stalls; do not attack it directly — instead constrain a hypothetical solution, which is R-cassels. First move: Cassels' binomial/cyclotomic argument.
```

```rung
id: R-cassels
statement: if x^p - y^q = 1 with p,q odd primes, then p | y and q | x; the known solution has p = 2, q = 3, giving 2 | 2 and 3 | 3, so it is consistent but sits outside the stated hypothesis p,q odd
off: negative-claim
stance: open
merge: classical (Cassels); re-derive in-workspace. Strengthen to mod p^2 and q^2 in R-double-wieferich; first move: Mihailescu's refinement of the same binomial manipulation.
```

```rung
id: R-double-wieferich
statement: if x^p - y^q = 1 with p,q odd primes, then p^{q-1} = 1 (mod q^2) and q^{p-1} = 1 (mod p^2); the known solution has p = 2, so 3^1 != 1 (mod 4) — it fails, and is excluded by the hypothesis p,q odd
off: negative-claim
stance: open
merge: this is the double-Wieferich necessary condition (Mihailescu, after Cassels); verify the exact statement and orientation against a primary source before attacking. It is a structural constraint, not an elimination, so it cannot over-eliminate the known solution. Next: use it together with class-group control, R-regular; first move: verify the exact regular-prime statement, then Kummer's method makes the relevant ideals principal.
```

```rung
id: R-regular
statement: if p and q are distinct odd primes with p ∤ h_p and q ∤ h_q (h_m = class number of Q(zeta_m)), then x^p - y^q = 1 has no solution in x,y > 0; the known solution has p = 2, so it sits outside
off: class-group
stance: open
merge: classical Kummer-type partial result on Catalan; the statement as written is attributed and must be checked against a primary source, since regularity's exact role in the two-sided argument is subtle. Turning class-group back on (dropping regularity) is the full both-odd content; the move is Stickelberger/Thaine-type annihilation of the p-part of the class group. This is the difficulty that actually bites.
```
