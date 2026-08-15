# Weakener ladder: Catalan / consecutive perfect powers (canonical)

`x^p - y^q = 1`, `x,y > 0`, `p,q > 1`. The goal is the negative statement that
`(3,2,2,3)` is the only solution. This is the run's single ladder for the goal;
the former `catalan.md` ladder is folded in (see the footer).

Two tracks meet in this ladder. The **exponent track** (R-known-instance →
R-trivial-bases → R-fixed-23 → R-exp2/R-exp2-mirror → R-p-eq-q → R-35) turns
the exponents back on: fixed instance → one-exponent-is-2 → both odd in a UFD.
The **cyclotomic track** (R-fixed-pq → R-uniform-finite → R-cassels →
R-double-wieferich → R-regular → goal) is the one the full proof actually runs
on: it stops asking "is there none?" and instead constrains a hypothetical
both-odd solution, then removes the class-group hypothesis last. R-regular →
goal is where the open content lives.

## Difficulty glossary

The short names in the `difficulties` field. Each entry says what "on" costs
and what "off" means, so every rung's `off` field is checkable against the
declaration.

- `negative-claim` — the target is a negative/exclusion statement; the
  characteristic failure is over-elimination that kills `(3,2,2,3)`. Every
  rung states where the known solution sits. **Off** when the rung is an
  identity, a finiteness claim, or a conditional constraint on a hypothetical
  solution rather than an exclusion.
- `unbounded-exponents` — `p,q` range over all integers `>1` (all primes after
  the reduction), so no finite case split. **Off** when exponents are fixed to
  a concrete pair or a concrete value (or one of the two is pinned).
- `unbounded-bases` — `x,y` unbounded, and once both exponents are odd there is
  no elementary a priori bound. **Off** when the bases are fixed, or the claim
  is only about the trivial base values.
- `both-odd` — both exponents odd prime ⇒ no factorisation in `Z` or `Z[i]`;
  the equation moves into `Q(zeta_p)`. **Off** when at least one exponent is 2.
- `class-group` — ideals of `Z[zeta_p]` need not be principal; the
  ideal→element conversion is the obstruction the problem statement names.
  **Off** when the argument stays in a UFD (`Z`, `Z[i]`, `Z[zeta_3]`,
  `Z[zeta_5]`, or under a regularity/class-number hypothesis that forces
  principality). For the final rungs this one difficulty subdivides into two
  distinct switches: (i) *nonprincipal-ideals* — the ideals actually being
  non-principal; and (ii) *unconditional-class-number* — controlling the
  relevant part of the class number (the minus part `h^-`) by a proved bound
  rather than GRH/Cohen–Lenstra. Both must be off for the rung to be elementary.
- `p-neq-q` — distinct exponents with both odd remove the elementary
  factorisation `x^p - y^p`. **Off** when `p = q` (the symmetric case, trivial
  in `Z`) or when one exponent is 2.
- `uniqueness` — the goal must pin the solution set to exactly `{(3,2,2,3)}`,
  not merely show it is finite. **Off** when the rung claims only nonexistence,
  finiteness, or a constraint.

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
merge: anchor, nothing to turn on. Settled as given: problem.md states (3,2,2,3) is a solution, and 3^2 - 2^3 = 9 - 8 = 1 is direct integer arithmetic. Until the exact-integer oracle solutions(N) is built, this is anchored by the statement, not by a run claim block (research/CLAIMS.md has none). This identity is the falsifier's calibration: solutions(N) must return exactly (3,2,2,3) for every reachable N >= 9, and every higher rung is checked against this instance before it is believed. Next rung: R-trivial-bases.
```

```rung
id: R-trivial-bases
statement: there is no solution with x = 1 or y = 1; equivalently every solution has x >= 2 and y >= 2
off: unbounded-exponents, unbounded-bases, both-odd, class-group, p-neq-q, uniqueness
stance: settled
merge: one-line proof for the forward loop: x=1 forces y^q = 0 (excluded by y>0), and y=1 forces x^p = 2 (impossible for integer x>=1, p>=2). negative-claim stays on — the claim is still an exclusion — but the known solution (3,2,2,3) has both bases >= 2, so it is not eliminated. SETTLED by code/elementary/elementary_rungs.py (code/out/elementary_rungs.captured.txt): proved, consistency-checked against exact oracle solutions(10^8) = [(3,2,2,3)]. Turning unbounded-bases back on at the single smallest nontrivial exponent pair is R-fixed-23; first move: factor y^3 = (x-1)(x+1) with gcd(x-1,x+1) in {1,2}.
```

```rung
id: R-fixed-23
statement: x^2 - y^3 = 1 has (x,y) = (3,2) as its only solution in integers x,y > 0; the known solution (3,2,2,3) is exactly the claimed one
off: unbounded-exponents, both-odd, class-group, p-neq-q
stance: proved (descent + PARI thue complete; claim exp2-fixed23-proved-thue)
merge: proved in full in-workspace by an explicit descent + complete Thue resolution:
  y^3 = (x-1)(x+1), gcd(x-1,x+1) | 2; x even impossible (min cube gap 7 > 2);
  x odd forces {k,k+1} = {c^3, 2d^3} for x = 2k+1, giving the two Thue equations
  c^3 - 2d^3 = +-1, resolved completely by PARI's proven thue() (code/refute/
  thue_descent_full.py, thue_nf.gp; output code/out/thue_descent_full.captured.txt,
  thue_gp.captured.txt). Final filtering x,y > 0 selects exactly (x,y) = (3,2).
  This is the claim exp2-fixed23-proved-thue (status: proved) and closes the
  rank-4 GOAL item "exponent-2 cases proved in full". The known solution is
  precisely this case, so the proof does not over-eliminate it. Numeric
  cross-check against code/elementary/elementary_rungs.py to x = 10^7 still
  holds (only (3,2)). Turning unbounded-exponents partially on while keeping
  p = 2 is R-exp2; first move: the same factorisation with q-th-power
  extraction, gcd(x-1,x+1) | 2.
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
off: p-neq-q, class-group, uniqueness
stance: settled
merge: immediate for the forward loop in Z: x^p - y^p = (x-y)(x^{p-1}+...+y^{p-1}) is a product of two positive integers, so it equals 1 only if both are 1, but the second factor is >= p >= 3. SETTLED by code/elementary/elementary_rungs.py (code/out/elementary_rungs.captured.txt): proved, brute-force-confirmed over primes<=19, x<3000 (0 hits). p=q restores the Z-factorisation, so class-group and p-neq-q are off and uniqueness is not at stake (the claim is pure nonexistence); both-odd stays on but does not bite because the symmetric factorisation exists. Turning p-neq-q back on at the smallest distinct odd pair, with the cyclotomic rings still UFDs, is R-35.
```

```rung
id: R-35
statement: x^3 - y^5 = 1 has no solution in integers x,y > 0; the known solution has p = 2, so it sits outside this rung's case
off: class-group, unbounded-exponents, uniqueness
stance: open
merge: the first rung where both-odd actually bites: no Z/Z[i] factorisation, so the argument must live in a cyclotomic ring. Both Q(zeta_3) (Eisenstein integers) and Q(zeta_5) have class number 1, so class-group stays off and the ideal→element lift is free. This is the cleanest place to watch the cyclotomic method work: write x^3 - 1 = y^5, factor x^3 - 1 = (x-1)(x^2+x+1), then x^2+x+1 = (x-zeta_3)(x-zeta_3^2) in Z[zeta_3], a UFD. Merge upward by either letting one exponent vary (x^3 - y^q with q an odd prime — subsumed by the R-cassels/R-double-wieferich/R-regular track) or turning class-group back on at the first prime p with Q(zeta_p) not a UFD: p = 23, where h(Q(zeta_23)) = 3 (asserted, verify against a source). That step is where the ideal→element lift first fails.
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
merge: Tijdeman (1976), asserted in problem.md; the effective bound is astronomically larger than any feasible search, so this rung is a theorem, not a computation (this is the `astronomical-bound` difficulty from the folded-in ladder). Turning uniqueness back on is the full goal and is where the ladder stalls; do not attack it directly — instead constrain a hypothetical solution, which is R-cassels. First move: Cassels' binomial/cyclotomic argument.
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
merge: classical Kummer-type partial result on Catalan; the statement as written is attributed and must be checked against a primary source, since regularity's exact role in the two-sided argument is subtle. Turning class-group back on (dropping regularity) is the full both-odd content; the move is Stickelberger/Thaine-type annihilation of the p-part of the class group. This is the difficulty that actually bites, and it subdivides: one must (i) handle genuinely nonprincipal ideals, and (ii) control the minus class number h^- unconditionally (a proved bound, not GRH). Neither is sourced in this run yet.
```

## The last step (R-regular → goal)

Dropping regularity re-enables `class-group` in both of its sub-switches:
nonprincipal ideals in `Z[zeta_p]` must be converted to element relations, and
the relevant part of the class number must be controlled by a *proved* bound
(the minus part `h^-`, on Mihailescu's route) rather than by GRH or
Cohen–Lenstra heuristics. Together with the double-Wieferich exclusion this is
the open content problem.md names. The ladder does not contain a rung for it
because a rung that switches the class group back on *is* the goal.

## Folded-in note

The former second ladder `catalan.md` used the finer difficulty vocabulary
`odd-prime-both`, `nonprincipal-ideals`, `unbounded-exponents`,
`independent-pq`, `unconditional-class-number`, `astronomical-bound`. Its
distinct content is preserved here: `x^3 - y^5 = 1` is now `R-35`;
`x^3 - y^q = 1` is subsumed by the R-cassels → R-double-wieferich → R-regular
track (the "one exponent fixed, one varies" partial-result shape); and the
finer sub-switches are recorded inside the `class-group` glossary entry and
`R-uniform-finite`/`R-regular` merge fields. There is one ladder now.
