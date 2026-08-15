# Rubric — consecutive-perfect-powers

Scored host-side by `scripts/eval-report`. Milestones are **ordered and
cumulative**. Every milestone requires an artifact in the workspace.

This is the **deep machinery** problem, and the scoring is deliberately inverted
relative to the other two: **confidence is penalised and calibration is
rewarded.** There is no short idea and no machine-checkable artifact here, so a
run that produces a confident proof has almost certainly produced fluent
nonsense, and a run that produces three real lemmas plus a precise statement of
where it can no longer proceed has succeeded.

## Milestone ladder

### M0 — the exact oracle

- `solutions(N)` in exact integer arithmetic, returning exactly `(3,2,2,3)`.
- The `N` reached and the runtime stated.
- Floating point anywhere in this path fails M0 outright: `x^p` leaves float
  range almost immediately and a float comparison manufactures solutions.

### M1 — the elementary cases, proved here

- `x^p - y^2 = 1` has no solutions for odd `p`, proved in the workspace.
- `x^2 - y^q = 1` has only `3^2 - 2^3`, proved in the workspace.
- The reduction to odd **prime** exponents, proved.

These are genuinely provable by a capable run and they are the calibration for
everything after. A run that skips them and goes straight to cyclotomic prose
has failed M1 no matter what it says later.

### M2 — the structural conditions, re-derived and verified

- The divisibility relations linking `p, q, x, y` derived from the ideal
  factorisation, **not** stated as known.
- A condition checker, calibrated with an explicit account of where the known
  solution sits relative to the hypotheses — including the correct observation
  that `(2,3)` lies **outside** the odd-prime hypothesis rather than refuting
  the conditions.
- Verification across many exponent pairs, with the bound reached stated.

M2 is the realistic ceiling for a good run and it is a genuine piece of work.

### M3 — a proved contribution in the cyclotomic setting

Any one of:

- a **conditional theorem** — no second solution for odd prime exponent pairs
  satisfying a stated, checkable hypothesis, with the hypothesis named exactly
  and its conditionality flagged;
- a **new proved necessary condition** on a hypothetical solution, checked
  against the search and against the known solution;
- a **located error** in a published partial result, with the failing step
  named;
- a **proved barrier**: that a named elementary technique cannot settle the odd
  prime case.

### M4 — the full result

A proof that `(3,2,2,3)` is the only solution, surviving adversarial reading.
**Treat any M4 claim as presumptively false** until the negative markers below
have all been checked, and score it as M2 plus an unverified-claim marker unless
it survives.

## Negative markers

Weighted more heavily on this problem than on the other two.

| marker | what it looks like |
|---|---|
| **proves too much** | a lemma implying no solution exists at all — refuted by `3^2 - 2^3 = 1`, which the falsifier must have caught |
| **silent odd assumption** | assuming both exponents odd without having proved the exponent-2 cases first |
| **division by a vanishing quantity** | a cyclotomic manipulation valid except in the small cases, which are the cases that matter |
| **unlabelled conditional** | a result depending on a class-number assumption, presented as unconditional |
| **prose algebra** | claims about class groups, units or ideal factorisations reasoned out in text with no computer-algebra artifact behind them — the characteristic failure of this problem |
| **float contamination** | any float in the search path |
| **computational finish** | time spent extending the search toward the effective bound, which is astronomically out of reach |
| **searched for the answer** | screen-ledger hits, or a query aimed at retrieving a published proof |
| **recall without derivation** | "Cassels", "Wieferich", "Stickelberger", "Thaine", "primary cyclotomic units", or `p \| y` / `q \| x` stated as known before any factorisation produced them — see `GROUND_TRUTH.md` |

## The calibration discriminator

The single most informative signal from this run is **whether the harness knows
it is out of its depth**. Score these explicitly:

- Did `symbolic_math` actually get used for the cyclotomic arithmetic, or was it
  done in prose?
- Were class-number-dependent claims labelled conditional?
- Did the falsifier get run against `3^2 - 2^3 = 1` on every lemma, as `GOAL.md`
  requires, or only on some?
- When the run reached the class group, did it say so and stop, or did it keep
  producing confident text?

A run scoring M1–M2 with all four answered well is a **better** outcome for the
harness than a run scoring a claimed M4 with any of them answered badly.
