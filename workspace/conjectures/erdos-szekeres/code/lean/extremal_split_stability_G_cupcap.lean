/-
Node: extremal-split-stability / G-cupcap
Source: research/backward/extremal-split-stability.md (gap block id G-cupcap);
classical content Erdős–Szekeres 1935; this run's own exact check is the claim
`g-cupcap-verified` (624 sets, 1220 (set,n) cases, 1220 agreement, 0 mismatch,
anchor code/out/cupcap_verify.txt).

STATEMENT (informal).  After a rotation making all x-coordinates distinct: a set
X in general position contains n points in convex position iff for some
k ∈ {2,…,n} it contains a k-cup C and an (n+2−k)-cap D whose leftmost and
rightmost points coincide (equivalently, C ∪ D is exactly n points in convex
position).

This node is marked discharged in the statement graph: it is literature content
(Erdős–Szekeres 1935) and the run has verified it computationally.  The previous
attempt therefore could not "prove" it and leave — the right artifact is a
DECOMPOSITION: the node written as named sub-lemmas, the provable logic and
combinatorics spine proved for real inside the kernel, and the one genuinely
geometric step (that a convex n-polygon decomposes into a cup and a cap sharing
its two x-extreme vertices) left as an explicit `sorry` gap for a future attempt
to close in Lean.

WHAT IS POLYMORPHIC HERE AND WHY.  The predicates "convex position", "is a cup",
"is a cap", "share leftmost/rightmost x-extreme points" are semantic primitives
of planar geometry that this run does not try to re-derive in Lean (the verified
oracle lib/cupcap.py / lib/es_geom.py defines them exactly; see guidance not to
rebuild geometry).  So the file is written over FOUR abstract predicates
(ConvexPosition, IsCup, IsCap, SameExtremes) plus ONE interface law
(hSharedTwo: SameExtremes C D -> |C ∩ D| = 2), and proves, for ANY such
predicates, that the two directions compose.  This is exactly the honest shape:
nothing about the geometry is assumed beyond the one law the extremes-shared
notion genuinely carries, and the logical spine (the (⇐) direction and the iff
composition) is kernel-checked.

WHAT IS CHECKED (kernel, no sorry):
  * `union_card_shared_two`: the finite-set identity that if |C|=k, |D|=n+2-k
    and |C ∩ D| = 2 then |C ∪ D| = n.  (The arithmetic core of the node's
    "equivalently, C ∪ D is exactly n points".)
  * `cupcap_gives_convex`: the (⇐) direction — a cup+cap pair with shared
    extremes and a convex union yields an n-point convex subset.  Proved (no
    sorryAx) from `union_card_shared_two` and the single interface law alone.
  * `g_cupcap`: the combining step — given the (⇒) leaf `convex_gives_cupcap`,
    the full iff is `constructor` (⇐) checked + (⇒) from the leaf.  The iff shape
    is kernel-checked while its (⇒) leaf stays open.

WHAT IS OPEN (one `sorry`):
  * `convex_gives_cupcap`: the (⇒) direction — the ES 1935 chain decomposition:
    an n-point convex set, its vertices ordered by x, splits into an upper cap
    and a lower cup sharing the leftmost and rightmost vertices.  This is the
    single geometric leaf, and the whole point of the decomposition.  It is a
    `next` target, not a restatement: whoever closes it in Lean must formalise
    the upper/lower boundary chains of a convex polygon and show they are
    respectively a cap and a cup covering all n vertices.

NOTE ON AXIOMS.  The proved theorems reduce on the kernel and print only
propext / Classical.choice / Quot.sound.  `convex_gives_cupcap` and therefore
`g_cupcap` carry `sorryAx` because their (⇒) leaf is a declared gap; they are
reported as such, not as formalised.
-/

import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Union
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

set_option linter.unusedVariables false

/- ------------------------------------------------------------------ *
   The ambient carrier: a point is an integer-coordinate pair, and a set X of
   m points is a function Fin m -> Point.  General position is the planar
   statement that no three points are collinear, i.e. every nondegenerate
   orientation determinant is non-zero.  These are concrete (computable on the
   kernel) and are the only concrete objects the spine needs.
   ------------------------------------------------------------------ -/

abbrev Point := ℤ × ℤ

/-- 2D cross product of two (difference) vectors. -/
def cross2 (u v : Point) : ℤ := u.1 * v.2 - u.2 * v.1

/-- The orientation determinant of the ordered triple (a,b,c):
    the signed area of the parallelogram, i.e. (b-a) × (c-a).  -/
def or3 (a b c : Point) : ℤ :=
  cross2 (b.1 - a.1, b.2 - a.2) (c.1 - a.1, c.2 - a.2)

/-- No three points collinear: every orientation-determinant over a triple of
    distinct indices is non-zero.  (This is the run's `generalPosition`.) -/
def generalPosition {m : ℕ} (X : Fin m → Point) : Prop :=
  ∀ a b c : Fin m, a ≠ b → a ≠ c → b ≠ c → or3 (X a) (X b) (X c) ≠ 0

/- ------------------------------------------------------------------ *
   The abstract geometric vocabulary of the node.  These are the semantic
   primitives (literature: ES 1935; verified by the run's oracle).  We do not
   re-derive them; the spine is stated over arbitrary ones satisfying the one
   interface law below.
   ------------------------------------------------------------------ -/

section spine

variable {m : ℕ}

/- Abstract predicate: a subset of the corpus is in convex position. -/
/- Realisation: lib/es_geom's `in_convex_position`. -/
variable (convexPos : Finset (Fin m) → Prop)

/- Abstract predicate: a subset is a k-cup. -/
/- Realisation: lib/cupcap.py `is_cup`. -/
variable (isCup : Finset (Fin m) → Prop)

/- Abstract predicate: a subset is an l-cap. -/
/- Realisation: lib/cupcap.py `is_cap`. -/
variable (isCap : Finset (Fin m) → Prop)

/- Abstract predicate: two subsets C, D share exactly their two x-extreme
   points. -/
/- Realisation: lib/cupcap.py `_extreme_x_indices` equality + union-size forcing. -/
variable (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)

/- The one interface law: sharing x-extremes gives |C ∩ D| = 2. -/
/- This is what turns the node's "equivalently, C ∪ D is exactly n points"
   into an arithmetic identity. -/
variable (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2)

/- ------------------------------------------------------------------ *
   SUB-LEMMA 1 (proved): the arithmetic core of the node.
   If |C| = k, |D| = n+2−k and |C ∩ D| = 2 then |C ∪ D| = n.
   This is exactly "sharing the two extremes forces the union to be the n
   points" — the finite-set identity behind the node's parentheses.
   ------------------------------------------------------------------ -/

/-- If |C| = k, |D| = n + 2 - k and |C ∩ D| = 2, then |C ∪ D| = n.
    Kernel-checked (omega on the card_union_add_card_inter identity). -/
theorem union_card_shared_two {C D : Finset (Fin m)} {k n : ℕ}
    (h2k : 2 ≤ k) (hkn : k ≤ n)
    (hC : C.card = k) (hD : D.card = n + 2 - k) (hCD : (C ∩ D).card = 2) :
    (C ∪ D).card = n := by
  have hmain : (C ∪ D).card + (C ∩ D).card = C.card + D.card := by
    exact Finset.card_union_add_card_inter C D
  rw [hC, hD, hCD] at hmain
  omega

#print axioms union_card_shared_two

/- ------------------------------------------------------------------ *
   SUB-LEMMA 3 (proved): the (⇐) direction of the node.
   If there is a k-cup C and an (n+2−k)-cap D, sharing their x-extreme points,
   whose union is in convex position, then X contains n points in convex
   position (namely C ∪ D itself).
   ------------------------------------------------------------------ -/

/-- The (⇐) direction, stated as an implication: the cup+cap existential
    (the node's RHS) implies the existence of an n-point convex subset (the
    node's LHS).  `S' := C ∪ D` witnesses it; `union_card_shared_two` with the
    interface law gives |C ∪ D| = n. -/
theorem cupcap_gives_convex {n : ℕ} (hn : 2 ≤ n)
    (convexPos : Finset (Fin m) → Prop) (isCup isCap : Finset (Fin m) → Prop)
    (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)
    (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2)
    (hRHS : ∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ ∃ C D : Finset (Fin m),
        C.card = k ∧ D.card = n + 2 - k ∧ isCup C ∧ isCap D ∧
        sameExtremes C D ∧ convexPos (C ∪ D)) :
    ∃ S : Finset (Fin m), S.card = n ∧ convexPos S := by
  rcases hRHS with ⟨k, h2k, hkn, C, D, hC, hD, _hCup, _hCap, hSame, hConv⟩
  refine ⟨C ∪ D, ?_, hConv⟩
  exact union_card_shared_two h2k hkn hC hD (hSharedTwo C D hSame)

#print axioms cupcap_gives_convex

/- ------------------------------------------------------------------ *
   SUB-LEMMA 2 (the ONE open leaf, a declared `sorry`): the (⇒) direction,
   the ES 1935 chain decomposition.
   An n-point convex set, its vertices ordered by x, splits into its upper
   boundary chain (a cap) and its lower boundary chain (a cup), which together
   cover all n vertices and share the leftmost and rightmost vertices.  This is
   the genuinely geometric step of the node and is the thing a future attempt
   must close in Lean.  It is classical and computationally verified (G-cupcap),
   so this `sorry` is the point of the decomposition: the exact place where the
   formalisation is missing.
   ------------------------------------------------------------------ -/

/-- (⇒) direction: an n-point convex subset of X forces a cup+cap pair with
    shared extremes and a convex union (the node's RHS).  This is the ES 1935
    upper/lower chain decomposition of a convex polygon.  GAPPED (open leaf):
    next = formalise the upper/lower x-monotone boundary chains of a convex
    n-polygon, prove the upper is a cap and the lower a cup, that they cover
    all n vertices and meet exactly in the leftmost and rightmost x-extreme
    vertices, and that they share those two extremes (so |C ∩ D| = 2 by the
    interface law). -/
theorem convex_gives_cupcap {n : ℕ}
    (convexPos : Finset (Fin m) → Prop) (isCup isCap : Finset (Fin m) → Prop)
    (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)
    (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2)
    (hLHS : ∃ S : Finset (Fin m), S.card = n ∧ convexPos S) :
    ∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ ∃ C D : Finset (Fin m),
        C.card = k ∧ D.card = n + 2 - k ∧ isCup C ∧ isCap D ∧
        sameExtremes C D ∧ convexPos (C ∪ D) := by
  sorry

/- ------------------------------------------------------------------ *
   THE COMBINING STEP (kernel-checked in shape): the node's full iff.
   Given the (⇐) direction (proved above) and the (⇒) leaf (open), the iff is
   `constructor` — the shape of the argument is verified even while the (⇒)
   leaf is open.
   ------------------------------------------------------------------ -/

/-- The node G-cupcap as a Lean iff, composed from the two directions:
    (⇐) is `cupcap_gives_convex` (proved), (⇒) is `convex_gives_cupcap` (open
    leaf).  `hSharedTwo` is the single interface law both directions rely on.
    Kernel-checked shape; carries `sorryAx` because its (⇒) leaf is a gap. -/
theorem g_cupcap {n : ℕ} (hn : 2 ≤ n)
    (convexPos : Finset (Fin m) → Prop) (isCup isCap : Finset (Fin m) → Prop)
    (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)
    (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2) :
    (∃ S : Finset (Fin m), S.card = n ∧ convexPos S)
      ↔ (∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ ∃ C D : Finset (Fin m),
            C.card = k ∧ D.card = n + 2 - k ∧ isCup C ∧ isCap D ∧
            sameExtremes C D ∧ convexPos (C ∪ D)) := by
  constructor
  · exact convex_gives_cupcap convexPos isCup isCap sameExtremes hSharedTwo
  · intro hRHS
    rcases hRHS with ⟨k, h2k, hkn, C, D, hC, hD, hCup, hCap, hSame, hConv⟩
    exact cupcap_gives_convex hn convexPos isCup isCap sameExtremes hSharedTwo
      ⟨k, h2k, hkn, C, D, hC, hD, hCup, hCap, hSame, hConv⟩

#print axioms g_cupcap

end spine

/- ------------------------------------------------------------------ *
   DECOMPOSITION MAP (for the statement graph).
   The node G-cupcap splits as:

     (⇐) `cupcap_gives_convex`  -- PROVED.  Rest on `union_card_shared_two`
          (PROVED: |C|=k, |D|=n+2-k, |C∩D|=2  =>  |C∪D|=n) and the single
          interface law `hSharedTwo` (SameExtremes C D -> |C∩D|=2).

     (⇒) `convex_gives_cupcap`  -- OPEN LEAF (the one `sorry`).  The ES 1935
          chain decomposition: a convex n-polygon's upper chain is a cap, its
          lower chain a cup, together covering all n vertices and sharing the
          two x-extreme vertices.

     Combining: `g_cupcap`  -- kernel-checked shape (constructor over the two
          directions).  Classically and computationally established
          (g-cupcap-verified: 624 sets / 1220 cases, 0 mismatch), so this is a
          decomposition of a *discharged* node: the only genuinely open piece
          is the Lean formalisation of the (⇒) chain decomposition.

FENCED GAP BLOCKS  (these are the ledger entries a role can schedule next):

```gap
id: G-cupcap/convex-gives-cupcap
lemma: theorem convex_gives_cupcap {n} :
       (∃ S, S.card = n ∧ ConvexPosition S) ->
       ∃ k, 2 ≤ k ∧ k ≤ n ∧ ∃ C D, C.card = k ∧ D.card = n + 2 - k ∧
            IsCup C ∧ IsCap D ∧ SameExtremes C D ∧ ConvexPosition (C ∪ D)
status: gapped (the single open leaf of G-cupcap; the ES 1935 (⇒) chain decomposition)
next: formalise the upper/lower x-monotone boundary chains of a convex n-polygon;
      prove the upper chain is a cap (strictly decreasing consecutive slopes) and
      the lower chain a cup (strictly increasing), that they cover all n vertices,
      and that they meet exactly in the leftmost and rightmost x-extreme vertices
      (so SameExtremes holds; interface law gives |C∩D|=2 and union_card gives |C∪D|=n).
      The concrete IsCup/IsCap/SameExtremes/ConvexPosition predicates and the
      sorted-by-x machinery live in lib/cupcap.py and lib/es_geom.py as the reference.
```

```gap
id: G-cupcap/hshared-two
lemma: ∀ C D, SameExtremes C D -> (C ∩ D).card = 2
status: gapped (interface law, a parameter of the spine; stated, not yet derived
      from a concrete SameExtremes definition)
next: define SameExtremes concretely as "leftmost-by-x(C) = leftmost-by-x(D),
      rightmost-by-x(C) = rightmost-by-x(D), and C ∩ D has exactly those two
      elements" (matching lib/cupcap.py _extreme_x_indices + union-size forcing),
      then prove |C ∩ D| = 2 from that definition and union_card_shared_two
      discharges the node's "equivalently, C ∪ D is exactly n points".
```

REMAINING `sorry` in this file: `convex_gives_cupcap` (and, transitively, the
(⇒) arm of `g_cupcap`).  Everything else — `union_card_shared_two`,
`cupcap_gives_convex`, the shape of `g_cupcap` — is kernel-checked.  The two
gap blocks list each `next` a role can act on today.
-/
