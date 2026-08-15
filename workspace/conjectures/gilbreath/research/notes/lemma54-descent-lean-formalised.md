# Lemma 5.4 abstract core — kernel-checked in Lean (Directive 50 scoping)

## Status

`id: lemma54-descent-lean-formalised`
`status: formalised` (see canonical claim `descent-lemma-halved-formalised`,
  `code/out/descent_lemma_formalised.notes.md`, which carries the kernel verdict)
`formalisation: code/lean/descent_lemma.lean` (compiled true, verified true,
  no `sorryAx`; axioms only `propext` / `Classical.choice` / `Quot.sound`)
`bearing:` the combinatorial core of Granville Lemma 5.4 in halved units.
  This is the first kernel-checked result of the run (Directive 50).

This note records the **scope** the operator attached to the result; the claim
itself lives in `code/out/descent_lemma_formalised.notes.md` (id
`descent-lemma-halved-formalised`) so the ledger keeps exactly one kernel-backed
row.

## Scope — exactly what is machine-checked

The Lean file formalises the **abstract combinatorial core in halved units**
and nothing more:

- pattern `el : List Nat` with every entry in `{0,1}` (hypothesis
  `∀ e ∈ el, e = 0 ∨ e = 1`);
- arbitrary starting halved value `w : Nat`;
- `runAbs w el` = the genuine iterated `Nat.dist` fold
  (`d_0 = w`, `d_{k+1} = |d_k − e_k|`);
- `countOnes el` = ν₁;
- `descent_claim1`: `w ≤ countOnes el + 1` ⟹ `runAbs w el ∈ {0,1}`;
- `descent_claim2`: `countOnes el + 1 < w` ⟹ `runAbs w el = w − countOnes el`
  (exact value);
- `run_inv` (engine invariant) and `run_absorb` (`{0,1}` absorbing under
  `|x − e|` for `e ∈ {0,1}`).

Both directions, exact value, unchanged (Directive 50). Axiom footprint:
`absorbing` — no axioms; `run_absorb` — `[propext]`; `run_high`, `run_inv`,
`descent_claim1`, `descent_claim2` — `[propext, Classical.choice, Quot.sound]`.
No `sorryAx` anywhere.

## What it does NOT cover (do not let it grow in the retelling)

- **Link A** (`v ≤ g*_n`) — **VERIFIED non-vacuously** (supersedes the older "still unverified after Directive 45 vacuity": `code/out/verify_lemma54_v_le_gstar.captured.txt` checks 1181 real prime columns, 0 violations, margin 35.882; only the `captured2.txt` invocation was vacuous — see `scholar-reconciliation-lean-and-linkA-current.md` and claim `lemma54-lean-and-linkA-current-verified`).
- **The composition** `g*_n ≤ 2ν₂+2 ⟹ success`.
- **The reduction** from real column dynamics to the `(pattern, v)` model —
  the Directive 48 item 1 proof, still to be written.
- **The supply side** (the ν₂ lower bound).

So this result is **strictly less** than `lemma54-re-derived-proof` (the full
lemma on the even domain). It must not be cited as upgrading that claim to
`proved`; the honest path to a Lean-proved full Lemma 5.4 is to formalise
Link A and the composition as well.

## Why this matters

The defective prose step ("each 2 contributed −2", false on bounce
trajectories) that Directive 43/44 flagged in
`research/notes/lemma54-re-derived-proof.md` is now superseded by a
kernel-checked case split, not by more prose. The Lean file certifies the
abstract core; `lemma54-re-derived-proof.md` cites it and deletes the
defective algebra.
