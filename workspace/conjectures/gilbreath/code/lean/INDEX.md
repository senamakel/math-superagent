# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `descent_lemma.lean` | Even-unit formalisation of the descent/absorption lemma (Granville Lemma 5.4 core): orbit x_0=v, x_{s+1}= |
| `gilbreath_reduction.lean` | Machine-checked Lean 4 reduction of Gilbreath's conjecture to the {0,2} second-entry claim: defines Step (absolute-difference operator), proves (odd, even, even, ...) shape preservation, |
| `gilbreath_reduction.lean.bak` | Backup of gilbreath_reduction.lean made 2026-08-13 before the Directive 31 re-emission compile (sha256 e6e1a7228be4494aa25ef611b0e5a08db3b5a38419b3ecdbf1880f8317ef0767, byte-identical to the current file). Audit trail for the re-emission; the current gilbreath_reduction.lean is the authoritative copy. |
| `link_a.lean` | Lean 4 formalisation of Link A of Granville Lemma 5.4 (the v <= g*_n bound, combinatorial core): proves dist_le_max ( |
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
