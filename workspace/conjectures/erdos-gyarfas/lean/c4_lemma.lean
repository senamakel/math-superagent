import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Walk.Basic
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# A 4-cycle satisfies the Erdős–Gyárfás conclusion

**Claim.** If a finite simple graph `G` contains a simple cycle of length 4
(the `C₄` — a closed trail `p : G.Walk v v` with `p.IsCycle` and
`p.length = 4`), then `G` already satisfies the Erdős–Gyárfás conclusion:
there is some `k ≥ 2` and a cycle of length `2 ^ k`.

This is the *"a counterexample must be C4-free"* direction of the run: since
`4 = 2²` is itself a power of two, a graph that already contains a 4-cycle is
not a counterexample, so any search for a counterexample may restrict to
C4-free graphs (`nauty-geng -f`).

**Proof shape.** Witness `k = 2`; a 4-cycle has length `2²`. The two
arithmetical facts need — `4 = 2^2` and `2 ≤ 2` — close with `norm_num`.

No `sorry` is used; see `#print axioms c4_gives_eg_conclusion` at the bottom.
-/
theorem c4_gives_eg_conclusion {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (h : ∃ (v : V) (p : G.Walk v v), p.IsCycle ∧ p.length = 4) :
    ∃ (k : ℕ) (v : V) (p : G.Walk v v),
      p.IsCycle ∧ p.length = 2 ^ k ∧ 2 ≤ k := by
  rcases h with ⟨v, p, hpcycle, hplen⟩
  refine ⟨2, v, p, hpcycle, ?_, by norm_num⟩
  rw [hplen]
  norm_num

#print axioms c4_gives_eg_conclusion
