# Goal — first pass

Attack the open descendants of Hilbert's third problem (`problem.md`):
completeness of volume and the Dehn invariant in dimension ≥ 5, and the Dehn
invariant sufficiency conjecture in hyperbolic and spherical 3-space. Dehn's
original answer and Sydler's theorem are settled and are **not** the target.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- The exact statements of Sydler and Jessen, and precisely **which dimensions
  are settled** — the run's whole target depends on `n ≥ 5` genuinely being
  open, and on `n = 4` genuinely being closed.
- The current status of the hyperbolic and spherical conjecture: what is proved
  (rigidity results, partial results for specific families), what is
  conjectural, and who has claimed what.
- The definition of the scissors congruence group in each geometry, in one
  fixed form used unchanged for the rest of the run.
- Whether any additional invariant beyond volume and Dehn has been proposed in
  dimension 5, and what became of it.
- What the `K`-theoretic reframing actually gives — a new theorem, or a new
  language for the same open question. Say which.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states scissors congruence as an equivalence
  relation on polytopes, the Dehn invariant as an element of `R ⊗_Z R/πQ`, and
  the completeness conjecture, ending in `sorry`. Expect the tensor product over
  `R/πQ` to be awkward; **where it will not type, that is a finding to record.**
- **Invariance of the Dehn invariant under a single cut is provable in Lean**
  and is where this workspace should reach a real theorem rather than a
  statement. So is the Dehn invariant of a named polytope with algebraic angles.
- Cited results — Sydler, Jessen, Dupont–Sah — are `axiom`s in `namespace Cited`
  with `/-- src: ... -/`, earning `conditional`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library over an algebraic number field, verified
against controls before anything rests on it:

- **Exact Dehn invariant computation** for a polytope given by exact vertex
  data, in Euclidean, hyperbolic and spherical geometry, returning an exact
  element and a *proved* verdict on whether it vanishes — with the
  `Q`-linear-independence argument for the angles attached, or the verdict
  labelled numerical.
- **A dissection checker**: given two polytopes and a list of pieces with
  isometries, verify exactly that the pieces tile the source, that their images
  tile the target, and that each map is an isometry of the right geometry.
- **Guards, asserted on at entry, every run**: the cube must return Dehn
  invariant `0`; the regular tetrahedron must return a *provably* nonzero one
  (this is the arccos(1/3)/π irrationality, which must be proved, not observed);
  a published dissection of a prism must verify. A library that reports the
  regular tetrahedron as zero is broken and every result it produced is void.
- Record where exact arithmetic in the number field stops being feasible.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- An explicit scissors congruence between two named hyperbolic polytopes of
  equal volume and Dehn invariant, searched for and certified.
- Completeness for a named subclass of 5-dimensional polytopes (orthoschemes,
  products of lower-dimensional pieces).
- A precise statement of which step of Sydler's argument fails to lift to
  dimension 5 — a smaller result than the conjecture and a genuinely useful one.
- An exact vanishing/non-vanishing determination for the Dehn invariants of a
  named hyperbolic family, with the linear independence proved.

## Rules

- **One canonical oracle per question.** Everything that computes a Dehn
  invariant or checks a dissection calls `code/lib`; nothing does either inline.
- **Numerical vanishing is a lead.** An invariant vanishes when the linear
  independence of the angles has been proved, and not before.
- Keep the three geometries strictly apart, and say which every claim is about.
  Test 3 in `problem.md` runs on every argument transported between them.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

Dehn's original theorem and Sydler's, except as background and as controls.
Banach–Tarski and measure-theoretic paradoxical decompositions — a different
subject that shares vocabulary. Higher `K`-theory beyond what bears on the two
target statements.
