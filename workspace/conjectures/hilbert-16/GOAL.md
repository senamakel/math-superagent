# Goal — first pass

Attack the second part of Hilbert's 16th problem (`problem.md`): limit cycles of
planar polynomial vector fields. This is the opening pass on a cold workspace.
Nothing here is established yet, and the first job is to make the problem
*legible and formal* for later passes rather than to solve it.

Part I of the problem — real schemes of plane curves — is out of scope, as
`problem.md` says. Do not start it here.

## What this pass is for

Four things, in this order. The run is a success if it delivers the first three
honestly with nothing on the fourth.

### 1. Establish the status, from primary sources

Every "known result" in `problem.md` is recalled from memory and marked as such.
Confirm or strike each one with a citation and its exact hypothesis. Settle in
particular:

- **The DRR list.** How many of the 121 graphics for `n = 2` have had finite
  cyclicity proved, and **exactly which ones remain open**, with the paper that
  settled each of the recently closed ones. This list is the run's target
  inventory; get it right and everything downstream has somewhere to go.
- Which polycycle classes the Ilyashenko–Yakovenko / Kaloshin results cover, and
  the precise genericity and elementarity hypotheses.
- The current best explicit bound for zeros of Abelian integrals, and whether
  anything better than doubly exponential exists for special families.
- The current best lower bounds: `H(2)`, `H(3)`, `M(2)`, `M(3)`, the growth rate.
  A lower bound whose construction is not reproducible is recorded as
  asserted-by-source, not as verified.
- Whether any complete proof of `H(2) < ∞` is claimed anywhere, and if so its
  status — published, refereed, withdrawn, gap found. If one stands, this run's
  target changes to *stress-testing it*: restate its key step, apply the three
  tests in `problem.md`, and say what it does not give.

Record each in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`. A run with a full `research/`
tree and an empty Established section has read everything and concluded nothing.

### 2. Write the mathematics in Lean, and keep writing it

**This is the pass's primary deliverable, not its bookkeeping.** Use Lean for as
much of the mathematics as it will carry, from the first hour, and treat a
statement that cannot yet be typed as a finding rather than as a reason to write
prose instead.

- `code/lean/Lib/Statement.lean` states H16.2 itself: for each `n` there is `N`
  bounding the number of limit cycles of every planar polynomial field of degree
  `≤ n`. That means typing *limit cycle* — a periodic orbit of the flow,
  isolated in the set of periodic orbits — over Mathlib's ODE and flow API,
  ending in `:= by sorry`. You are not asked for a proof; you are asked for a
  type that carries every hypothesis.
- **Report what Mathlib does not have.** Expect gaps: Poincaré–Bendixson, return
  maps, isolatedness of periodic orbits, Dulac functions, polycycles. For each
  gap either state the missing notion yourself under `code/lean/Lib/` with the
  definitions it needs, or record precisely what is absent and what a statement
  would require. **Which parts of H16 are and are not statable in today's
  Mathlib is a reportable result of this pass**, and nobody has written it down.
- Every load-bearing claim from step 1 goes under `code/lean/Lib/<Subject>.lean`
  in `namespace Cited` with a `/-- src: ... -/` docstring naming the paper —
  Écalle–Ilyashenko finiteness, the Roussarie reduction, Bautin's cyclicity 3,
  the BNY Abelian-integral bound, each lower bound. A cited result is an
  `axiom` in `Cited` and earns `conditional`, never `formalised`.
- Every claim this run makes about a minimal object, a cyclicity, or a count is
  stated in Lean **before** the attempt spends itself on it. A claim whose
  hypotheses will not go into binders is one nobody has pinned down, and finding
  that out costs minutes instead of an attempt.
- Anything finite and algebraic that the argument reduces to — a Bautin ideal
  membership, a sign condition on a Dulac function, a resultant vanishing — is
  where Lean can carry a *real* proof rather than a statement. Push those all the
  way to a kernel-checked theorem with `decide`, `norm_num`, `polyrith` or an
  explicit certificate, and prefer the shape of argument that Lean can finish.
- Report `#print axioms` and every remaining `sorry`, every time. A `sorry`
  named and located is progress; an unreported one is a false claim.

Prose in `research/` is how the run reads the literature. Lean is how it *holds*
what it believes. When the two disagree, Lean wins and the prose is corrected.

### 3. Build the oracles, as evidence for those statements

Three checkers, in `code/`, each exact or interval-certified. **Numerics may
search; only a certificate decides.**

- **A certified limit-cycle counter.** Given explicit `P, Q` over `Q`, produce
  *proved* existence of limit cycles: a trapping annulus plus a return map with
  a sign change, verified in interval arithmetic, or an equivalent
  Poincaré-map contraction argument. Verify it against textbook cases with known
  counts, and against a linear field (must report zero) and a field with a
  known centre (must not report a limit cycle) as negative controls.
- **A nonexistence certificate.** A Dulac function `B` with `div(B·X)` of one
  sign on a region proves no limit cycle there. Search for `B` in a polynomial
  ansatz; discharge the sign condition through `smt_solver` or a
  sum-of-squares certificate, then re-state the discharged certificate in Lean.
- **The Bautin / Lyapunov machinery, exactly.** Lyapunov quantities of a focus
  as polynomials in the coefficients over `Q`, and the ideal they generate via
  Gröbner bases. Reproduce Bautin's `M(2) = 3` — the literature boundary — before
  trusting anything computed past it, and record where the computation stops
  being feasible and why. That wall is a fact about the problem worth writing
  down.

Each program says which Lean file or claim id it bears on. A computation nobody
has stated is a number the next attempt cannot use.

### 4. Attack one precise claim

Choose it, state it in Lean before testing it, and hunt the counterexample as
hard as the proof. Candidates, none endorsed — pick on the evidence step 1
produces, not on this ordering:

- **Finite cyclicity of one open graphic from the DRR list.** The most valuable
  and the most self-contained target in the problem. Requires the normal form
  and blow-up at each vertex, the transition maps, and the argument that the
  displacement function has finitely many zeros.
- A sharp zero-count for Abelian integrals in one named Hamiltonian family, via
  its Picard–Fuchs system and an argument-principle count.
- A certified configuration beating a published lower bound in degree 3, or a
  twelfth small-amplitude cycle at a cubic focus.
- A finite bound on `H(2)` restricted to an explicitly stated subfamily, with
  the obstruction to removing the restriction named.

## Rules

- **One canonical oracle per question.** Everything that decides existence of a
  limit cycle calls `code/lib`; nothing decides it inline. Every experiment
  asserts on a guard set at entry — a linear field with no cycle, a known centre,
  a textbook field with a known count — and asserts on the *produced* data.
- **Certificates decide, numerics search.** A phase portrait, a simulated orbit
  that looks closed, a Melnikov integral evaluated in floating point: all leads.
  An interval-arithmetic return-map bracket, an exact ideal membership, an SOS
  certificate, a kernel-checked Lean theorem: those conclude.
- **A measurement is not a proof.** Label every statement
  proved / verified-computationally / conjectured / asserted-by-source, and name
  the ceiling of every computation.
- **Apply the three tests in `problem.md` to every candidate argument** and
  record which step failed each test. The smooth test is not optional: an
  argument that never uses analyticity is refuted.
- **`problem.md` is not authoritative.** It is written from memory and expects
  correction. When a source disagrees with it, print both and say which won.
- **Captures write to a temp file and move on exit 0**, and each states in its
  first three lines what it ran, which oracle function, and the exact range or
  parameter box. An empty capture is a failed run, not a missing one.
- **Cite, do not re-derive**, once something is in `CLAIMS.md` with a source.
- **Do not claim `H(n) < ∞` and do not claim `H(2) = 4`.**

## Out of scope

Part I (real schemes, Harnack, Gudkov, patchworking) — background only; enough
to know why the two halves share a number, then leave it. Higher-dimensional
analogues, limit cycles of non-polynomial families, and the Hilbert–Arnold
problem for general smooth families are out of scope unless a source shows the
generalisation is *easier* and implies a case of H16.2.
