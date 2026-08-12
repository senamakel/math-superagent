# Index — lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | Build instructions for the Lean files in this container (hand-set LEAN_PATH, explicit -o oleans, compile c4_lemma first), the conventions of the formal statement, and the axioms output. |
| `axioms_check.lean` | Reports `#print axioms` for c4_lemma.lean and erdos_gyarfas.lean theorems. |
| `axioms_check.olean` | _(undescribed)_ |
| `c4_lemma.lean` | _(undescribed)_ |
| `c4_lemma.olean` | _(undescribed)_ |
| `cut_vertex.lean` | Kernel-checked Lean 4 formalisation of the geometric heart of the cut-vertex lemma: a simple cycle through v has its two v-neighbours connected inside G−v (so all non-v cycle vertices lie in one component of G−v). Models G−v as `G.induce {x |
| `cut_vertex.olean` | Prebuilt olean for cut_vertex.lean, written explicitly (read-only root). |
| `cut_vertex_axioms.lean` | Reports `#print axioms` for the cut_vertex.lean lemmas — no sorryAx, only propext/Classical.choice/Quot.sound. |
| `cut_vertex_axioms.olean` | Prebuilt olean for cut_vertex_axioms.lean. |
| `erdos_gyarfas.lean` | _(undescribed)_ |
| `erdos_gyarfas.olean` | _(undescribed)_ |
