# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `descent_lemma.lean` | Even-unit formalisation of the descent/absorption lemma (Granville Lemma 5.4 core): orbit x_0=v, x_{s+1}= |
| `gilbreath_reduction.lean` | Machine-checked Lean 4 reduction of Gilbreath's conjecture to the {0,2} second-entry claim: defines Step (absolute-difference operator), proves (odd, even, even, ...) shape preservation, |
| `gilbreath_reduction.lean.bak` | Backup of gilbreath_reduction.lean made 2026-08-13 before the Directive 31 re-emission compile (sha256 e6e1a7228be4494aa25ef611b0e5a08db3b5a38419b3ecdbf1880f8317ef0767, byte-identical to the current file). Audit trail for the re-emission; the current gilbreath_reduction.lean is the authoritative copy. |
| `lemma54_composition.lean` | Self-contained sorry-free Lean 4 formalisation of leg 2 of Granville Lemma 5.4 (the composition): re-derives Link A's |
| `lemma54_even_domain.lean` | Even-domain theorem of Granville Lemma 5.4, kernel-checked sorry-free in Lean 4 via the halving identity: reduces the {0,2}^L trajectory to the halved {0,1}^L core (descent_claim1/descent_claim2), proving v≤2ν₂+2 ⟹ d_L∈{0,2} (lemma54_even_forward), 2ν₂+2<v ⟹ d_L=v−2ν₂ (lemma54_even_high), their bundling (lemma54_even), and the biconditional (lemma54_even_iff). |
| `link_a.lean` | Consolidated kernel-checked formalisation of Link A + the composition of Granville Lemma 5.4. Defines runAbs/countTwo ONCE (verbatim-identical to descent_lemma.lean's, enforced by link_a_drift_guard.py), carries the descent core (descent_backward) plus Link A (orbit_le_max <= max v (maxAll el)) and the composition (link_a_composition / _via_max / _full: g*_n <= 2*nu2+2 & v even => orbit lands in {0,2}). Directives 53 & the composition prerequisite: because cross-file import cannot pass lean_check in this container (fixed read-only module search path, verified), the fix is to keep the shared orbit machinery in one checkable unit and machine-guard its parity. |
| `link_a_drift_guard.py` | Machine guard enforcing that link_a.lean's shared descent-core region (runAbs, countTwo, dist_even_even, absorbing, run_absorb, dist_even_two, run_high_even, run_inv_even, even_le_two, descent_backward) is byte-identical to descent_lemma.lean's, so the two files cannot silently diverge "by convention". Exit 0 iff all pass. This is the construction-level fix for Directive 53 where a true cross-file import is physically impossible under lean_check. |
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
