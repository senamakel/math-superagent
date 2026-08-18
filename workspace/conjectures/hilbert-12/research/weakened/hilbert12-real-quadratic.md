# Hilbert's 12th — real quadratic case: ladder of weakened targets

The full-strength goal is H12.rq: a **complex-analytic** construction whose
special values generate the abelian extensions of a real quadratic field
`K = Q(√D)`. The `p`-adic side (Dasgupta–Kakde, Brumer–Stark) is a different
question and is not this goal. The run's realistic contribution, per
`GOAL.md` "What counts as a result" #2, is a verified extension of the
published Stark-unit tables; the ladder climbs from there toward the goal,
turning one named difficulty back on per rung.

The difficulties are named as specific obstructions, not topics.

```ladder
goal: H12.rq — give explicit complex-analytic functions and special values generating the abelian extensions of a real quadratic field K = Q(√D), for all D and all moduli, in the archimedean sense (not the p-adic one).
difficulties: archimedean-construction-unknown, stark-conjecture-unproved, recognition-not-proof, unbounded-D-and-conductor, generation-vs-containment, exact-verification-bounded, p-adic-vs-archimedean-conflation
status: open
```

```rung
id: R1-reproduce-published-control
statement: Reproduce one published real-quadratic Stark unit for a single small (D, m) taken from the literature: compute it from partial zeta values to high precision, recognize its minimal polynomial over Q, and verify exactly — degree, discriminant, ramification, Galois group — that the field it defines is the ray class field the ray class group predicts. This is the oracle guard GOAL.md requires before any open case is touched.
off: archimedean-construction-unknown, stark-conjecture-unproved, unbounded-D-and-conductor, generation-vs-containment, p-adic-vs-archimedean-conflation
stance: open
merge: Take a (D, m) NOT in the published tables. That turns on unbounded-D-and-conductor (one step past the known) and makes recognition-not-proof and generation-vs-containment genuinely tested rather than confirmed by a known answer.
```

```rung
id: R2-one-new-case
statement: Compute a Stark unit for one real-quadratic (D, m) outside the published tables, recognize its minimal polynomial with precision/height/margin reported, and verify exactly that the field it cuts out is the predicted ray class field. The verification — not the recognition — is what concludes.
off: archimedean-construction-unknown, stark-conjecture-unproved, p-adic-vs-archimedean-conflation
stance: open
merge: Take several new (D, m) pairs instead of one. That turns the single case into a table and pushes exact-verification-bounded toward the (D, m) where recognition or class-group computation first stalls.
```

```rung
id: R3-verified-table-extension
statement: A verified extension of the published Stark-unit table by several new real-quadratic (D, m) pairs past the published range, each with the unit computed, its minimal polynomial recognized (precision, coefficient height, margin all reported), and the generated field verified exactly against the ray class group. This is GOAL.md result #2 and the run's most likely real contribution.
off: archimedean-construction-unknown, stark-conjecture-unproved, p-adic-vs-archimedean-conflation
stance: open
merge: Stop adding cases and instead name the (D, m) ceiling where verification stalls. That drops the obligation to keep verifying new cases and turns the table into a frontier statement about exact-verification-bounded itself.
```

```rung
id: R4-verification-frontier
statement: Determine and report the exact (D, m) ceiling at which Stark-unit recognition (working precision versus minimal-polynomial coefficient height) or ray-class-group computation stops being feasible, with the obstruction named — precision shortfall, height blow-up, or class-group size — and the largest (D, m) verified on each side of it. This is the "record where precision or class-group computation stops being feasible" requirement of GOAL.md §3.
off: archimedean-construction-unknown, stark-conjecture-unproved, p-adic-vs-archimedean-conflation, generation-vs-containment
stance: open
merge: Ask what a complex-analytic construction would have to satisfy to get past that ceiling. That turns on archimedean-construction-unknown — the central obstruction — and p-adic-vs-archimedean-conflation, since the only existing construction is p-adic.
```

```rung
id: R5-archimedean-spec
statement: A precise specification of what a complex-analytic counterpart of the p-adic Dasgupta–Kakde / Brumer–Stark construction must satisfy, derived from the p-adic side: which special values, at which real-quadratic points, with which transformation law, generating which ray class field. The obstruction to producing such a function named. This is GOAL.md result #5.
off: stark-conjecture-unproved, recognition-not-proof, unbounded-D-and-conductor, generation-vs-containment, exact-verification-bounded
stance: open
merge: Produce the construction itself. That turns every difficulty back on — archimedean-construction-unknown from characterized to solved, and unbounded-D-and-conductor, generation-vs-containment, exact-verification-bounded with it — which is the goal.
```

```rung
id: R6-goal-h12rq
statement: A proved complex-analytic construction whose special values generate a class field (equivalently, all abelian extensions) of a real quadratic field K = Q(√D): the Jugendtraum for the first open case of Hilbert's twelfth. Do not claim this on an argument that has not survived attack.
off: 
stance: open
merge: 
```

## Notes on the ordering

The ladder starts at the oracle guard (R1), because nothing above it is
trustworthy until the checker reproduces a known answer — and the workspace
currently has no oracle, no claims, and no prior attempts, so R1 is the first
concrete move and is genuinely open. Each rung turns on exactly one more
declared difficulty:

- R1 → R2 turns on `unbounded-D-and-conductor` (one step past the known) and
  re-activates `recognition-not-proof` and `generation-vs-containment` as live
  tests rather than confirmations.
- R2 → R3 keeps the same difficulties off but pushes `exact-verification-bounded`
  toward its ceiling by taking many cases.
- R3 → R4 reframes `exact-verification-bounded` from an obstacle to the object
  of study, and drops `generation-vs-containment`.
- R4 → R5 turns on `archimedean-construction-unknown` (characterized) and
  `p-adic-vs-archimedean-conflation`, dropping the computational difficulties.
- R5 → R6 turns everything on; that is the goal.

## Which difficulty bites

The deep obstruction is `archimedean-construction-unknown` — there is no known
complex-analytic special function on the upper half plane whose real-quadratic
values generate class fields, and that is the goal itself. But the difficulty
the run will actually hit, and hit early, is `exact-verification-bounded`
together with `recognition-not-proof`: as `D` and the conductor `m` grow, the
coefficient height of the Stark unit's minimal polynomial outruns the
precision that partial zeta values deliver, and the recognition step stops
being justified by its margin. That ceiling — not the construction problem —
is where the computational programme dies, and naming it exactly (R4) is the
finding a run that cannot prove the conjecture can still produce.
