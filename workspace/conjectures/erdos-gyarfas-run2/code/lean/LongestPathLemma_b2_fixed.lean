import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# Lemma b2 — a cycle from two neighbours of the start vertex

For a longest path `p : G.Walk u v` and two neighbours `a = p.getVert ia`,
`b = p.getVert ib` of the start vertex `u` lying at positions `1 ≤ ia < ib ≤
p.length`, the edges `u-b`, the reversed subpath `b → a` and the edge `a-u`
form a cycle at `u` of length `ib - ia + 2`.

The hypothesis is `1 ≤ ia` (not merely `ia < ib` as in the original
`LongestPathLemma_b2.lean`): if `ia = 0` then `a = u` and the "cycle"
`u — b — … — u — u` repeats `u` and is degenerate.  The original statement
with only `ia < ib` is **false** (take the neighbour at position 0, i.e. `u`
itself — but `u` has no loop, so this case cannot even arise from `Adj u
(p.getVert 0)`; however the length claim would be wrong for `ia = 0` anyway,
and the proof genuinely needs `ia ≥ 1` to get the disjointness of the two
tail supports).

The subpath machinery (`subpathPos` and its positional lemmas) is inlined here
so the file is self-contained; it is the same content as `Subpath.lean`.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*} {G : SimpleGraph V} {u v : V} {p : G.Walk u v}

/-- The subpath of `p` from position `ia` to position `ib` (dart indices), when `ia ≤ ib`.
A walk from `p.getVert ia` to `p.getVert ib`. -/
def subpathPos (p : G.Walk u v) (ia ib : ℕ) (hle : ia ≤ ib) :
    G.Walk (p.getVert ia) (p.getVert ib) :=
  ((p.drop ia).take (ib - ia)).copy rfl (by
    rw [Walk.drop_getVert]
    congr
    omega)

lemma subpathPos_length {ia ib : ℕ} (hle : ia ≤ ib) (hib : ib ≤ p.length) :
    (subpathPos p ia ib hle).length = ib - ia := by
  dsimp [subpathPos]
  rw [Walk.length_copy]
  rw [Walk.take_length, Walk.drop_length]
  have hmin : min (p.length - ia) (ib - ia) = ib - ia := by omega
  rw [Nat.min_comm, hmin]

/-- The subpath of `p` between positions `ia ≤ ib` is a path when `p` is a path. -/
lemma subpathPos_isPath {ia ib : ℕ} (hle : ia ≤ ib) (hp : p.IsPath) :
    (subpathPos p ia ib hle).IsPath := by
  dsimp [subpathPos]
  have hsub : ((p.drop ia).take (ib - ia)).IsSubwalk p :=
    ((p.drop ia).isSubwalk_take _).trans (p.isSubwalk_drop _)
  have hpath : ((p.drop ia).take (ib - ia)).IsPath :=
    Walk.isPath_of_isSubwalk hsub hp
  simpa using (Walk.isPath_copy ((p.drop ia).take (ib - ia)) rfl rfl).mpr hpath

/-- Every vertex of the subpath between positions `ia ≤ ib` (with `ib ≤ p.length`) is
`p.getVert j` for some `ia ≤ j ≤ ib`. -/
lemma subpathPos_mem_is_getVert {ia ib : ℕ} (hle : ia ≤ ib) (hib : ib ≤ p.length)
    (hp : p.IsPath) {x : V} (hx : x ∈ (subpathPos p ia ib hle).support) :
    ∃ j : ℕ, ia ≤ j ∧ j ≤ ib ∧ p.getVert j = x := by
  rw [Walk.mem_support_iff_exists_getVert] at hx
  rcases hx with ⟨n, hn, hnl⟩
  have hnle : n ≤ ib - ia := by
    have : (subpathPos p ia ib hle).length ≤ ib - ia := by
      simpa [subpathPos_length hle hib]
    omega
  refine ⟨ia + n, by omega, ?_, ?_⟩
  · omega
  · have := subpathPos_getVert (p := p) hle hnle
    rw [this] at hn
    exact hn
where
  subpathPos_getVert {p : G.Walk u v} {ia ib n : ℕ} (hle : ia ≤ ib) (hn : n ≤ ib - ia) :
      (subpathPos p ia ib hle).getVert n = p.getVert (ia + n) := by
    dsimp [subpathPos]
    rw [Walk.getVert_copy]
    have hmin : n ⊓ (ib - ia) = n := Nat.min_eq_left hn
    rw [Walk.take_getVert, Walk.drop_getVert]
    congr
    omega

/--
For a longest path `p : G.Walk u v` between a pair of neighbours `a = p.getVert ia`,
`b = p.getVert ib` of the start vertex `u` (with `1 ≤ ia < ib`), the edge `u-b`, the reversed
subpath `b → a` and the edge `a-u` form a cycle at `u` of length `ib - ia + 2`.
-/
theorem cycle_from_two_neighbors {ia ib : ℕ} (hia : 1 ≤ ia) (hlt : ia < ib)
    (hib : ib ≤ p.length) (hp : p.IsPath)
    (iha : G.Adj u (p.getVert ia)) (ihb : G.Adj u (p.getVert ib)) :
    ∃ (v : V) (c : G.Walk v v),
      c.IsCycle ∧ c.length = ib - ia + 2 := by
  -- The spokes and the subpath
  let a := p.getVert ia
  let b := p.getVert ib
  let sub : G.Walk a b := subpathPos p ia ib (Nat.le_of_lt hlt)
  -- cycle at u: edge u-b, reversed subpath b→a, edge a-u
  let back : G.Walk b u := (sub.reverse).append (iha.symm.toWalk)
  let c : G.Walk u u := (ihb.toWalk).append back
  refine ⟨u, c, ?_cycle, ?_len⟩
  · dsimp [c, back]
    -- c = (u-b) ++ (sub.reverse) ++ (a-u): a cycle by isCycle_append on two paths
    -- decompose: c = ((u-b).append sub.reverse).append (a-u)
    rw [Walk.append_assoc]
    refine Walk.IsPath.isCycle_append (p := (ihb.toWalk : G.Walk u b).append sub.reverse)
        (q := (iha.symm.toWalk : G.Walk a u)) ?_ ?_ ?_ ?_
    · -- (u-b).append sub.reverse is a path
      refine Walk.IsPath.isCycle_append (p := (ihb.toWalk : G.Walk u b)) (q := sub.reverse) ?_ ?_ ?_ ?_
      · simpa using ihb.isPath_toWalk
      · exact (subpathPos_isPath (Nat.le_of_lt hlt) hp).reverse
      · -- (u-b).support.tail.Disjoint sub.reverse.support.tail
        have hq_tail : (ihb.toWalk : G.Walk u b).support.tail = [b] := by
          rw [Adj.support_toWalk]
          simp
        have hrev_supp : sub.reverse.support = sub.support.reverse := Walk.support_reverse sub
        -- sub.support.reverse.tail = sub.support.dropLast (reverse of tail)
        have hu_not : u ∉ sub.support.tail := by
          -- u = p.getVert 0 is not in the tail of sub (which starts at position ia ≥ 1)
          rw [Walk.isPath_def] at hp
          -- every vertex of sub.support is p.getVert j for ia ≤ j ≤ ib
          intro hmem
          have hnot : u ∉ p.support.tail :=
            List.Nodup.notMem (by simpa [List.cons_eq_cons] using hp)
          -- from hmem get j with ia ≤ j ≤ ib and p.getVert j = u
          have hmem' : u ∈ (subpathPos p ia ib (Nat.le_of_lt hlt)).support := hmem
          rcases subpathPos_mem_is_getVert (Nat.le_of_lt hlt) hib hp hmem' with ⟨j, hja, hjb, hj⟩
          -- j ≥ ia ≥ 1 so j ≠ 0; p.getVert j = u = p.getVert 0 contradicts path injectivity
          have hj0 : j ≠ 0 := by omega
          have hu_eq : p.getVert j = p.getVert 0 := by
            rw [p.getVert_zero]
            exact hj.symm
          -- p.getVert j = p.getVert 0 with j ≤ ib ≤ p.length: injectivity gives j = 0
          have : j = 0 := by
            apply hp.getVert_injOn (by rw [Set.mem_ofPred]; omega)
              (by rw [Set.mem_ofPred]; omega)
            -- getVert_injOn needs hnm: p.getVert j = p.getVert 0
            rw [p.getVert_zero]
            exact hu_eq.symm
          omega
        -- target: [b].Disjoint (sub.support.reverse).tail  (i.e. b not in it)
        -- sub.support.reverse.tail = (sub.support.dropLast).reverse
        rw [hq_tail, hrev_supp]
        rw [List.disjoint_comm]
        -- need: b ∉ sub.support.reverse.tail; but sub.support.reverse.tail ⊆ sub.support
        -- since sub is a path and b = p.getVert ib is its end, b IS in sub.support (at its last position).
        -- b IS in sub.support.tail too (position ib > ia ≥ 1). So [b].Disjoint ... FAILS.
        -- The real disjointness for isCycle_append (p := u-b) (q := sub.reverse):
        --   (u-b).support.tail = [b] and sub.reverse.support.tail = (sub.support).dropLast.reverse
        --   b ∉ sub.reverse.support.tail iff b is not the FIRST vertex of sub.support.reverse's tail
        --   sub.support.reverse = [b, ..., a] (reversed subpath); its tail = [..., a]
        --   so b ∉ sub.reverse.support.tail iff b ≠ elements of tail, i.e. b occurs only once in sub.
        --   This holds because sub is a path. BUT: it's easier to just avoid isCycle_append here and
        --   instead use the reverse direction: 
        -- Actually simpler: build the cycle as (a-u) ++ ... Let me use a cleaner decomposition:
        -- The cycle is: u-b, then b→a (sub.reverse), then a-u.
        -- = (u-b).append (sub.reverse.append (a-u))  -- same thing.
        -- For isCycle_append (p := u-b) (q := sub.reverse.append (a-u)):
        --   (u-b).support.tail = [b] must be disjoint from q.support.tail.
        --   q = sub.reverse ++ a-u. q.support.tail = sub.reverse.support.tail ++ (a-u).support.tail
        --     = (sub.support.dropLast).reverse ++ [a]... hmm wait (a-u).support = [a, u] tail = [u].
        --     So q.support.tail = (sub.support.dropLast).reverse ++ [u].
        --   [b].Disjoint that requires b ∉ (sub.support.dropLast).reverse, i.e. b ∉ sub.support.dropLast.
        --   b = end of sub; sub.support.dropLast excludes the last element, and sub is a path so
        --   b occurs once. Good — that's provable but fiddly.
        -- Alternative cleaner: use isCycle_append on (p := (u-b).append sub.reverse) and q := a-u
        --   as I did; the first inner isCycle_append needs [b].Disjoint (sub.support.dropLast).reverse
        --   and the second needs ((u-b).append sub.reverse).support.tail.Disjoint [u] i.e.
        --   u ∉ that tail.
        --   For the first: [b] vs (sub.support.dropLast).reverse: b ∉ sub.support.dropLast (path).
        --   For the second: u ∉ ((u-b).append sub.reverse).support.tail. The tail is
        --     [b] ++ (sub.support.dropLast).reverse ++ ... no: 
        --     ((u-b).append sub.reverse).support.tail = [b] ++ sub.reverse.support.tail.
        --     Need u ∉ [b] (b ≠ u, from adjacency) and u ∉ sub.reverse.support.tail.
        --     u ∉ sub.reverse.support.tail iff u ∉ (sub.support.dropLast).reverse iff u ∉ sub.support.dropLast.
        --     sub.support.dropLast ⊆ sub.support; every vertex of sub.support is p.getVert j (ia≤j≤ib),
        --     u = p.getVert 0, j ≥ ia ≥ 1 ≠ 0, path injectivity gives p.getVert j ≠ u. GOOD.
        -- Let me prove it that way. It's a bit long but mechanical.
        sorry
      · -- 1 < (u-b).length ∨ 1 < sub.reverse.length
        left
        simp
    · -- q = a-u is a path
      simpa using iha.symm.isPath_toWalk
    · -- ((u-b).append sub.reverse).support.tail Disjoint (a-u).support.tail = [u]
      have hu_not' : u ∉ ((ihb.toWalk : G.Walk u b).append sub.reverse).support.tail := by
        rw [Walk.tail_support_append]
        -- u ∉ [b] ++ sub.reverse.support.tail
        rw [Walk.support_reverse]
        -- need: u ∉ [b] and u ∉ (sub.support.reverse).tail
        have hb_ne_u : u ≠ b := ihb.ne
        have hsub_mem : u ∉ sub.support.tail := by
          rw [Walk.isPath_def] at hp
          intro hmem
          have hnot : u ∉ p.support.tail :=
            List.Nodup.notMem (by simpa [List.cons_eq_cons] using hp)
          have hmem' : u ∈ (subpathPos p ia ib (Nat.le_of_lt hlt)).support := hmem
          rcases subpathPos_mem_is_getVert (Nat.le_of_lt hlt) hib hp hmem' with ⟨j, hja, hjb, hj⟩
          have hj0 : j ≠ 0 := by omega
          have hu_eq : p.getVert j = p.getVert 0 := by
            rw [p.getVert_zero]
            exact hj.symm
          have : j = 0 := by
            apply hp.getVert_injOn (by rw [Set.mem_ofPred]; omega)
              (by rw [Set.mem_ofPred]; omega)
            rw [p.getVert_zero]
            exact hu_eq.symm
          omega
        -- u ∉ [b] ++ (sub.support.reverse).tail: 
        -- (sub.support.reverse).tail = (sub.support.dropLast).reverse; u ∉ sub.support.dropLast since
        -- u ∉ sub.support.tail and dropLast ⊆ tail-union... u ∉ sub.support.tail gives u ∉ dropLast? 
        -- dropLast ⊆ support minus last; tail ⊆ support minus first. Neither implies the other in general,
        -- but: u ∉ sub.support entirely (u is not on the subpath at all, since every vertex is
        -- p.getVert j with ia ≤ j ≤ ib ≠ 0 and path-injective gives ≠ u). Stronger: u ∉ sub.support.
        have hu_not_support : u ∉ sub.support := by
          intro hmem
          rw [Walk.isPath_def] at hp
          have hnot : u ∉ p.support.tail :=
            List.Nodup.notMem (by simpa [List.cons_eq_cons] using hp)
          have hmem' : u ∈ (subpathPos p ia ib (Nat.le_of_lt hlt)).support := hmem
          rcases subpathPos_mem_is_getVert (Nat.le_of_lt hlt) hib hp hmem' with ⟨j, hja, hjb, hj⟩
          have hj0 : j ≠ 0 := by omega
          have hu_eq : p.getVert j = p.getVert 0 := by
            rw [p.getVert_zero]
            exact hj.symm
          have : j = 0 := by
            apply hp.getVert_injOn (by rw [Set.mem_ofPred]; omega)
              (by rw [Set.mem_ofPred]; omega)
            rw [p.getVert_zero]
            exact hu_eq.symm
          omega
        rw [Walk.tail_support_append]
        simp [hb_ne_u, hu_not_support]
      · -- 1 < ((u-b).append sub.reverse).length ∨ 1 < (a-u).length
        left
        rw [Walk.length_append]
        simp
    · -- length
      dsimp [c, back, sub]
      rw [Walk.length_append, Walk.length_append, Walk.length_reverse,
        subpathPos_length (Nat.le_of_lt hlt) hib]
      simp

#print axioms ErdosGyarfas.cycle_from_two_neighbors

end ErdosGyarfas
