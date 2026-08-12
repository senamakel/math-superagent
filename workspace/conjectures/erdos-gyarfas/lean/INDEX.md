# Index — lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | Build instructions for the Lean files in this container (hand-set LEAN_PATH, explicit -o oleans, compile c4_lemma first), the conventions of the formal statement, and the axioms output. |
| `axioms_check.lean` | Reports `#print axioms` for c4_lemma.lean and erdos_gyarfas.lean theorems. |
| `cut_vertex.lean` | Kernel-checked Lean 4 formalisation of the geometric heart of the cut-vertex lemma: a simple cycle through v has its two v-neighbours connected inside G−v (so all non-v cycle vertices lie in one component of G−v). Models G−v as `G.induce {x | x≠v}`; main theorem `cycle_in_one_component`. Proved with Mathlib SimpleGraph/Walk/IsCycle machinery, no sorry. |
| `cut_vertex_axioms.lean` | Reports `#print axioms` for the cut_vertex.lean lemmas — no sorryAx, only propext/Classical.choice/Quot.sound. |
| `cut_vertex.olean` | Prebuilt olean for cut_vertex.lean, written explicitly (read-only root). |
| `cut_vertex_axioms.olean` | Prebuilt olean for cut_vertex_axioms.lean. |
