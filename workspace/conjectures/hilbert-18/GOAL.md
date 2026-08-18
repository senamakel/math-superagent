# Goal — first pass

Attack the open combinatorics under Hilbert's 18th problem (`problem.md`):
Heesch numbers, isohedral numbers, and the decidability question behind them.
Bieberbach, Reinhardt and Kepler are settled and are **not** the target.

## What this pass is for

### 1. Establish the records, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- **The current Heesch number record**: the largest value achieved by a known
  shape, the shape itself in exact coordinates, the paper, and — critically —
  how the non-tiling was proved in that case. That proof technique is the run's
  most valuable single import.
- Which isohedral numbers are known to be realised, and by which tiles.
- The exact status of the decidability question for a single polyomino, and what
  the aperiodic monotile result did and did not settle.
- Whether the Heesch number is known to be bounded for **any** restricted class.
- The state of exhaustive Heesch computations: which classes have been searched
  exhaustively, to what size, by whom.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states a tile, an isometric placement, a corona
  and the Heesch number, over integer-coordinate polyominoes first, ending in
  `sorry` where needed.
- **This workspace can reach real Lean theorems, not just statements**: a
  specific corona of a specific polyomino is a `decide` goal, and so is a
  colouring argument for non-tiling. Every certificate this run produces should
  land as a kernel-checked theorem, and generated placement data must sit under
  a `Generated/` folder with a hand-written checker and a soundness theorem
  outside it — never a `theorem` inside `Generated/`, and never `native_decide`.
- Cited records are `axiom`s in `namespace Cited` with `/-- src: ... -/`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library on exact integer coordinates, verified against
controls before anything rests on it:

- **Corona construction**: enumerate admissible placements around a patch and
  solve the exact-cover problem, returning either a corona, a *proved* UNSAT, or
  a stated search bound with a timeout — three distinct return values, in the
  type.
- **A geometric verifier**: decode any solver assignment back into a patch and
  check exactly that the copies are congruent to the tile, pairwise
  non-overlapping, and cover what is claimed. Nothing is reported that has not
  been through this.
- **Guards, asserted on at entry, every run**: a square must report `H = ∞`
  (it tiles); a published shape with known Heesch number must reproduce that
  number exactly; a shape that tiles must never be reported as having finite
  Heesch number. A library that gets a published record wrong may not be pointed
  at a new shape.
- **Non-tiling arguments** as first-class output: colouring and boundary
  invariants, applied automatically, so a shape's status is *proved non-tiling*
  or *unknown* — never inferred from a failed search.
- Record where the exact-cover search stops being feasible, at what corona depth
  and placement count.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- An exhaustive determination of the Heesch numbers of all polyominoes up to a
  size the search can complete, with the bound stated and the record within the
  class confirmed.
- A search for a shape beating the published Heesch record, run only on shapes
  whose non-tiling can be *proved* by the oracle's non-tiling battery.
- A boundedness theorem for a restricted class where the corona structure is
  rigid enough to argue about.
- A new isohedral number realised, with the orbit count proved.

## Rules

- **One canonical oracle per question.** Everything that builds or checks a
  corona calls `code/lib`; nothing does it inline.
- **UNSAT concludes; a timeout measures.** Report which, every time, with the
  search bound.
- **Non-tiling is proved or it is unknown.** A failed tiling search is never
  reported as non-tiling, and a Heesch number is never claimed without it.
- Exact integer or rational coordinates only; no floating point anywhere in the
  decision path.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every enumeration.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

Kepler's conjecture and the sphere-packing half beyond recording its status —
unless the run chooses the Cohn–Elkies bound as its target, in which case say so
explicitly and drop the tiling half. Crystallographic group enumeration
(Bieberbach) is background only.
