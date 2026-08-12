import cut_vertex

open SimpleGraph

/-!
# Axiom report for the cut-vertex lemma

Reports `#print axioms` for the kernel-checked lemmas of `cut_vertex.lean`.
Every one is expected to rest only on `propext` / `Classical.choice` /
`Quot.sound` — none on `sorryAx`, because there is no `sorry` in the file.
-/

namespace ErdosGyarfas

#print axioms cycle_in_one_component
#print axioms cycle_middle_avoids_v
#print axioms tail_penultimate
#print axioms cycle_second_ne_last
#print axioms cycle_snd_ne_v
#print axioms cycle_penultimate_ne_v

end ErdosGyarfas