# Google DeepMind formal-conjectures: Gilbreath.lean

<!-- source: https://raw.githubusercontent.com/google-deepmind/formal-conjectures/ed75a6dd/FormalConjectures/Wikipedia/Gilbreath.lean | the file is 1433 bytes, so the full text IS stored in this summary — no separate .full.md exists -->

A 41-line Lean 4 file from the FormalConjectures project (Google DeepMind;
commit ed75a6dd, Apache 2.0).

## What it contains

- `d : ℕ → (ℕ → ℕ)` — the iterated absolute-difference operator on the primes:
  `d 0 = fun n ↦ n.nth Nat.Prime` (n-th prime via mathlib), `d (k+1) n = Int.natAbs (d k (n+1) − d k n)`.
- `theorem gilbreath_conjecture (k : ℕ+) : d k 0 = 1 := by sorry` — the
  conjecture stated, with a **single `sorry` placeholder**. No proof of the
  parity/shape reduction, no block lemma, no partial result is formalised
  anywhere in the repo's Gilbreath file.

## Bearing

- Closes part of the open REQUESTS row "Lean 4 formalisation status": the
  answer is that nobody has formalised a proof — the DeepMind file is a
  statement-only placeholder.
- GOAL.md's Lean deliverable stays this run's to produce. The right primitive
  is mathlib4's `Nat.dist` (Mathlib/Data/Nat/Dist.lean: `dist n m = n - m +
  (m - n)`, with `dist_comm`, `dist_self`, `dist_eq_sub_of_le`), not a new
  absolute-difference definition.
- Useful as a reference shape for the statement; nothing here is a theorem to
  cite.

## Source status

Downloaded raw file from the pinned commit (the search-result URL). Apache-2.0.
The file's only citation is to Wikipedia's Gilbreath entry (already held).