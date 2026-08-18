# Ladder — universal quadratic forms over real quadratic fields

The full-strength target is T1 of `problem.md`: for a real quadratic field
`K = Q(√D)`, determine the minimal rank of a universal quadratic form over
`O_K`, with the lower bound **proved** (not searched) and the upper bound
exhibited as an explicit form, and establish whether a finite critical set
decides universality. Hasse–Minkowski over fields is settled and is not the
target; this is the ring-of-integers case, where local–global fails.

The rungs climb from a single kernel-checkable witness over `Z` to the general-`D`
rank problem. Each rung switches off named difficulties; the `merge` line says
what turning the next difficulty back on would take. A rung that fails stays on
the ladder with the reason.

```ladder
goal: For a real quadratic field K = Q(√D), determine the minimal rank of a universal positive-definite quadratic form over O_K (integer-matrix convention) representing every totally positive element of O_K, with the lower bound proved by a structural argument (continued fraction of √D / fundamental unit) and the upper bound exhibited as an explicit form; establish whether a finite critical set decides universality. This is T1 of problem.md.
difficulties: general-D, proved-lower-bound, totally-positive-target, O_K-arithmetic, complete-escalation, definite-no-local-global, matrix-vs-coefficient
status: open
```

```rung
id: R-z-witness
statement: Over Z, by Lean computation (decide / explicit witness), verify that the sum of four squares represents 7 (witness 2²+1²+1²+1²) and that the sum of three squares does not represent 7 (no integer solution to x²+y²+z²=7); and compute the determinant and Hasse invariant of an explicit small integer-matrix lattice. These are the single-representation guards of GOAL.md, kernel-checkable with no escalation engine.
off: general-D, proved-lower-bound, totally-positive-target, O_K-arithmetic, complete-escalation, definite-no-local-global, matrix-vs-coefficient
stance: open
merge: Turn on complete-escalation: from checking one representation at a time, build the escalation engine that adjoins a vector for the smallest unrepresented value, branches on the finitely many possibilities, and reproduces the 15-theorem critical set over Z.
```

```rung
id: R-z-fifteen-escalation
statement: Over Z, for positive definite integer-matrix forms, the escalation engine reproduces the 15-theorem critical set {1,2,3,5,6,7,10,14,15} and confirms the sum of four squares is universal while the sum of three squares is not (with 7 as the exception). This is the GOAL.md guard an engine must pass before it is pointed at a number field; the 15 theorem is known (Conway–Schneeberger / Bhargava) and this rung rederives it computationally as the oracle's control.
off: general-D, proved-lower-bound, totally-positive-target, O_K-arithmetic, definite-no-local-global, matrix-vs-coefficient
stance: open
merge: Turn on O_K-arithmetic, totally-positive-target, definite-no-local-global, and matrix-vs-coefficient: move from Z to O_K for one fixed small real quadratic field, fixing the integer-matrix convention and representing totally positive elements (positive under both embeddings) rather than positive integers.
```

```rung
id: R-fixed-D-critical-set
statement: For one fixed small real quadratic field K = Q(√D) (e.g. D = 2), integer-matrix positive definite forms over O_K, produce a complete escalation tree and a finite critical set deciding universality over the totally positive elements of O_K, with the tree's size and every leaf's verdict reported. This is a 290-type critical set over a named number field (problem.md result value #2); a partial tree proves nothing.
off: general-D, proved-lower-bound
stance: open
merge: Turn on proved-lower-bound: instead of only exhibiting a critical set (an upper bound on what must be checked), prove the minimal universal rank for this D exactly — a lower bound from the continued fraction of √D and the fundamental unit, with an explicit universal form giving the upper bound.
```

```rung
id: R-fixed-D-rank
statement: For one fixed real quadratic field K = Q(√D) where the minimal universal rank is currently unknown, determine that rank exactly: a proved lower bound from the continued-fraction / fundamental-unit arithmetic of √D (not a search), and an upper bound from an explicit universal form whose universality is certified by a complete escalation tree. This is problem.md result value #1 for a single field.
off: general-D
stance: open
merge: Turn on general-D: extend from one settled D to a range of D, and ultimately to arbitrary D, where the continued-fraction structure of √D and the fundamental unit vary and no single computation settles the rank.
```

```rung
id: R-general-D-rank
statement: For general real quadratic K = Q(√D), determine the minimal universal rank with a proved lower bound (continued-fraction / fundamental-unit argument valid for all D) and an exhibited upper bound, and establish whether a finite critical set decides universality over O_K. This is the full goal T1.
off:
stance: open
merge: All difficulties on; this is the goal. The ladder is exhausted when this rung is settled, which would constitute solving the open problem.
```

## What the ladder says

The bottom rung `R-z-witness` is the one an attempt could settle today: it is
pure finite computation over `Z`, kernel-checkable in Lean by `decide`, and
requires no escalation engine and no field arithmetic. `R-z-fifteen-escalation`
is the oracle guard every universality claim must pass before the engine is
trusted on a number field; it rederives the 15 theorem, which is known, so its
value is verifying the engine rather than new mathematics.

The first rung that is a genuine new result is `R-fixed-D-critical-set` — a
290-type critical set over a named real quadratic field, which problem.md ranks
as result value #2. The rung above it, `R-fixed-D-rank`, is result value #1 and
is where the real obstruction lives.

## The difficulty that actually bites

`proved-lower-bound`. Every universality result in this subject is a complete
escalation tree plus a leaf check; the upper bound is mechanical once the engine
is trusted. The lower bound on rank is not: it must come from the continued
fraction of `√D` and the fundamental unit, and "no exception found below `N`" is
explicitly not a proof (problem.md's first caution). This is the difficulty that
separates `R-fixed-D-critical-set` (exhibit a critical set) from
`R-fixed-D-rank` (prove the rank), and it is the one that has resisted
specialists. Its companion is `O_K-arithmetic`, where the silent errors live —
the integer-matrix / integer-coefficient and totally-positive / positive
distinctions — which is why `research/ROOT.md` is required to fix the
conventions before any field computation is trusted.

## Rung to attack next

`R-z-witness`, then `R-z-fifteen-escalation`. These are the oracle's controls:
they settle nothing new, but an engine that cannot rederive the 15 theorem may
not be pointed at a number field (GOAL.md). They are the prerequisite for every
rung above, and they are the cheapest things the run can settle.
