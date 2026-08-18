# Goal — first pass

Attack the effective side of Hilbert's 17th problem (`problem.md`): the number
of squares, the denominator degrees, and the certificates that decide them.
Artin's theorem is settled and is **not** the target; do not re-prove it.

This is the opening pass on a cold workspace. The first job is to make the
quantitative questions legible and formal, and to build the certificate
pipeline everything downstream will run on.

## What this pass is for

### 1. Establish the status, from primary sources

Every result in `problem.md` is recalled from memory. Confirm or strike each
one with its citation and its exact hypothesis, and settle in particular:

- Hilbert's 1888 classification of the `(n, d)` where psd = sos, in one fixed
  normalisation, with the convention written down.
- Pfister's `2^n`, and the best published **lower** bound on the number of
  squares for each `n ≤ 5` — with, for each, whether it is proved or asserted.
- Whether `n = 2` genuinely requires four squares, and the form that shows it.
- Reznick's uniform denominator theorem: its exact hypothesis (strict
  positivity), the `N` it gives, and what is known when `f` has a real zero.
- The current best effective Positivstellensatz degree bounds, and for which
  representation (Schmüdgen, Putinar, Krivine–Stengle) each was proved.

File each in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states the questions themselves: `IsSOS`,
  `IsSOSOfRationalFunctions`, and the square-counting function, over
  `MvPolynomial`. Ending in `sorry` is expected; a type that carries every
  hypothesis is the deliverable.
- Every cited bound goes under `code/lean/Lib/<Subject>.lean` in
  `namespace Cited` with `/-- src: ... -/`, as an `axiom`, earning
  `conditional` and never `formalised`.
- **This problem is unusually well suited to real Lean proofs, not just
  statements.** A verified rational SOS identity is a `ring`/`norm_num` goal.
  Every certificate this run produces must land as a kernel-checked theorem,
  and the count of certificates that did is this pass's headline number.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical certificate library, verified against controls
*before* anything rests on it:

- **SOS search**: build the monomial vector from the Newton polytope, set up
  the Gram spectrahedron, solve the SDP, project to the rational slice, round,
  and expand symbolically to verify. Return a *typed* result: exact
  certificate, numerical-only, or infeasible — never a bare number.
- **Guards, asserted on at entry, every run**: `x²+y²` must certify at once;
  the Motzkin polynomial must come back **not sos** as a polynomial and *sos
  after multiplying by `x²+y²+z²`*; a form with a negative value somewhere must
  be reported not psd. A pipeline that certifies Motzkin directly is broken and
  every result it produced is void.
- **Exact lower-bound machinery**: the dual side — search for a separating
  linear functional nonnegative on all squares and negative on `f`, exhibited
  over `Q`. This is what makes a lower bound possible at all.
- Reproduce one published decomposition exactly before computing past it, and
  record where the SDP stops being solvable and why.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- The minimal number of squares for one named ternary sextic, pushed from
  below via the dual certificate.
- A denominator degree bound for psd ternary forms with exactly one real zero.
- An exact rational certificate for a form the literature reports numerically.
- The measured Putinar degree against the proved bound on a generated family.

## Rules

- **One canonical oracle.** Everything that decides sos-ness calls `code/lib`.
  Nothing decides it inline, and no experiment re-implements the rounding.
- **Certificates decide, numerics search.** An SDP output is a lead. An exact
  rational Gram matrix verified by expansion, and again by the Lean kernel,
  concludes.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation — the degree
  and variable count at which the SDP stopped being solvable is a fact worth
  recording.
- Apply the three tests in `problem.md` to every candidate and record which
  step failed.
- **`problem.md` is written from memory and expects correction.** When a source
  disagrees, print both and say which won.
- Say, every time, whether a bound is about squares of polynomials or squares
  of rational functions.

## Out of scope

Hilbert's 1888 classification as such (settled, background only), general SDP
solver engineering beyond what the oracle needs, and noncommutative or matrix
sums of squares unless a source shows the commutative case follows.
