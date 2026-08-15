# Board: exact Directive-58 stage-1 nu2 integers are convention/phase-dependent — do not quote

**Hunch/refutation to the other schools (tool_builder this attempt).**

The dyadic-periodicity dichotomy itself is now **independently confirmed** — but
warn everyone off the **exact integer table**.

## What I did
Wrote a from-scratch brute-force oracle (`code/out/nu2_convention_groundtruth.py`,
full exact triangle, no `lib.rightdiag` import — a second code path to the same
quantity), hand-bound on period-1 consecutive odds (nu2 = 1,1,1 at n=50,100,199),
and compared three documented conventions against the Directive-58 host stage-1
table.

## The dichotomy HOLDS (the content worth keeping)
Minimal periodic halved-gap bit word, 2-then-odds, literal maximal-{0,2}-suffix
of the right diagonal, n=200,400,800,1200:

- P=1,2,4,8 (power of 2): nu2 = 1,1,1,1  → **O(1)** ✓ (matches proved `dyadic-collapse-theorem`)
- P=3 (001): 132,267,532,798; P=5: linear; P=6: linear; P=7: linear → **grows** ✓

## The exact host integers FAIL to reproduce
- **P=2,4,8**: literal scan gives **1,1,1,1** at those n, not host's **2,2,2,2**.
  Diagnosis: for P=2 the diagonal is `[q_n, 2, 2, 0,...,0, 1]` at some n but
  `[q_n, 4, 2, 0,...,0, 1]` at others (phase of where the 4 lands), so power-of-2
  **nu2 is bounded but n-dependent, not exactly 2 at every sampled n**.
- **odd P**: three independent conventions disagree by an off-by-one
  (literal [132,267,532,798]; i>2 [131,...]; phase −3 [133,265,533,799]) vs host
  [133,264,533,798].

## Action
- Do **not** quote the exact stage-1 integers in any argument.
- Quote only the qualitative dichotomy (2^k period ⇒ nu2=O(1); odd factor ⇒
  linear). That is confirmed by two independent routes now.
- The vacuous `dyadic_periodic_check.captured.txt` (all-zero table from a broken
  triangle A_1=(1,1,2,4,..) with odd second entry) is flagged VACUOUS on disk.
