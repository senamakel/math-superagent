# Lean 4 formalisation of the difference operator and the reduction — checked

## What was run

Three Lean 4 files, each compiled with `lean` against Mathlib 4 (no `#eval`,
no automation of the mathematics, exact proof terms):

- `code/lean/gilbreath_reduction.lean` — NEW, self-contained, the deliverable
  file. Proves:
  - `Step s i = |s i - s (i+1)|` (Nat.dist), `StartsOddEvenEven`
    = (odd, even, even, ...) shape;
  - `dist_one_eq_one`: |1 − n| = 1 ⟺ n = 0 ∨ n = 2;
  - `shape_theorem`: the (odd, even, even, ...) shape is invariant under one
    step;
  - `shape_rows`: every row of a row stream (X(k+1) = Step (X k)) has the
    shape, given row 1 does;
  - `reduction`: under shape + leading entry 1,
    next leading entry = 1 ⟺ second entry ∈ {0,2};
  - `gilbreath_reduction` (THE INDUCTION STEP, machine checked): for any row
    stream with the prime-row shape and leading entry 1 at row 1,
    **GilbreathConjecture ⟺ SecondEntryIn02** — forward direction via
    `reduction.mp` applied to every row, backward direction by induction on k
    using `reduction` as the inductive step.
- `code/lean/reduction.lean` — pre-existing, was BROKEN (did not compile:
  `rw` after `unfold`, stale `hg` reference). Repaired, compiles cleanly now.
- `code/lean/shape.lean` — pre-existing, was BROKEN (referenced undefined
  `dist_odd_even`/`dist_dist_even`; `shape_prime` had nonsense statement on
  `Step` itself). Rewritten self-contained; also proves `shape_iter`.

## Results (exact numbers from the captured outputs)

- `EXIT=0` for all three files.
- **Zero `sorry`; zero `sorryAx` across every declaration.**
- Every declaration's `#print axioms` output:
  `[propext, Classical.choice, Quot.sound]`
  (the standard Lean 4 base axioms that Mathlib itself uses — no math
  axioms, no `sorryAx`, no `Classical.choice`-free variant needed).
  9 dependency lines, 0 `sorryAx` (verified by grep on the captured file).

Captured: `code/out/lean_gilbreath_reduction.captured.txt` (the #print axioms
ledger), `code/out/lean_reduction.captured.txt`, `code/out/lean_shape.captured.txt`.

## What this settles

GOAL.md's deliverable "a Lean 4 formalisation of the difference operator and
the induction step, with `#print axioms` output reported and every remaining
`sorry` listed" is DONE, and done properly: the reduction of Gilbreath's
conjecture to the {0,2} second-entry claim is now a machine-checked theorem
(`gilbreath_reduction`), with the axioms audited to nothing beyond Lean's
standard set.

Boundary of the result (must be stated with it): the input hypotheses for the
prime stream — row 1 is (1, even, even, ...) with leading entry 1 and second
entry 2 — are verified by computation only (`code/lib/gilbreath.py` reproduces
the rows of problem.md exactly, depth 600/1000 in `code/out/witnesses.json`,
`code/out/blocks_depth1000.json`), NOT by a Lean proof. The theorem itself is
pure; the instantiation to the primes is arithmetic.

The regeneration content of the conjecture is untouched: this formalises the
existing reduction, it does not prove that second entries stay in {0,2}.

```claim
id: lean-reduction-machine-checked
statement: In Lean 4 with Mathlib, the difference operator Step s i = |s i - s (i+1)|, the shape predicate StartsOddEvenEven s = (Odd (s 0) ∧ ∀ n, Even (s (n+1))), the pivotal identity |1-n| = 1 ↔ n = 0 ∨ n = 2, and the full reduction theorem are formalised and kernel-checked: gilbreath_reduction {X : ℕ→ℕ→ℕ} (hs : RowStream X) (hshape₁ : StartsOddEvenEven (X 1)) (hlead₁ : X 1 0 = 1) : GilbreathConjecture X ↔ SecondEntryIn02 X, i.e. for any row stream with the prime-row shape and leading entry 1 at row 1, "every row starts with 1" is equivalent to "every row's second entry is 0 or 2". #print axioms on every declaration returns exactly [propext, Classical.choice, Quot.sound] (the standard Lean base set used by Mathlib itself), with zero sorry and zero sorryAx.
hypotheses: the statement is a theorem about arbitrary row streams (X (k+1) = Step (X k)); the hypotheses are that stream row 1 has the shape and leading 1. These hold for the prime triangle by computation only (witnesses.json reproduces A_1 = 1,2,2,4,2,4,2,4,6,2,...) — not instantiated in Lean.
holds-here: yes — the prime rows satisfy the hypotheses (verified computationally), and the theorem gives exactly the run's established claim gilbreath-reduces-to-second-in-02 as a machine-checked statement.
status: checked (three files compile with EXIT=0 and the axiom ledgers are captured: code/out/lean_gilbreath_reduction.captured.txt, code/out/lean_reduction.captured.txt, code/out/lean_shape.captured.txt)
bearing: GOAL.md deliverable "Lean 4 formalisation of the difference operator and the induction step, with #print axioms output and every sorry listed" is complete; the instantiation-to-primes boundary remains computation-checked, not Lean-proved.
anchor: code/lean/gilbreath_reduction.lean (proves everything self-contained); also code/lean/reduction.lean and code/lean/shape.lean (repaired from non-compiling)
```