# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `gilbreath_reduction.lean` | Machine-checked Lean 4 reduction of Gilbreath's conjecture to the {0,2} second-entry claim: defines Step (absolute-difference operator), proves (odd, even, even, ...) shape preservation, |
| `probe2.lean` | _(undescribed)_ |
| `probe3.lean` | _(undescribed)_ |
| `probe4.lean` | _(undescribed)_ |
| `probe5.lean` | _(undescribed)_ |
| `probe_even_sub.lean` | _(undescribed)_ |
| `probe_mod.lean` | _(undescribed)_ |
| `reduction.lean` | _(undescribed)_ |
| `shape.lean` | Lean 4 self-contained proof of shape preservation: ShapeTheorem — the (odd, even, even, ...) pattern is invariant under one absolute-difference step (dist_odd_even, dist_dist_even), and ShapeIter for all iterates. Was broken (referenced undefined lemmas), rewritten this run; kernel-checked EXIT=0, #print axioms = [propext, Classical.choice, Quot.sound] (code/out/lean_shape.captured.txt). |
| `t1.lean` | _(undescribed)_ |
| `t2.lean` | _(undescribed)_ |
| `t3.lean` | _(undescribed)_ |
| `t4.lean` | _(undescribed)_ |
| `t5.lean` | _(undescribed)_ |
| `t6.lean` | _(undescribed)_ |
| `t7.lean` | _(undescribed)_ |
| `t8.lean` | _(undescribed)_ |
| `t9.lean` | Scratch Lean proofs of dist_dist_even and dist_odd_even with fully explicit witnesses from the bare definitions (Even a = ∃r, a = r+r; Odd a = ∃k, a = 2k+1). No sorry. Superseded by self-contained shape.lean/gilbreath_reduction.lean. |
| `test_import.lean` | Lean environment probe: Mathlib.Data.Nat.Parity import + Nat.even_or_odd availability check. |
 import + Nat.even_or_odd availability check. |
