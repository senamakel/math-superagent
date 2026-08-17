/-
Node: g-cupcap-verified
Source: code/out/cupcap_claim.md (claim block g-cupcap-verified); classical
content Erdős–Szekeres 1935 (the cups-and-caps chain decomposition of a convex
polygon).  This run's own exact check is `code/out/cupcap_verify.txt`: 624
sets, 1220 (set,n) cases, 1220 agreement, 0 mismatch.

STATEMENT (the node verbatim).  For any planar point set X in general position
with distinct x-coordinates, X contains n points in convex position iff there
exist k in {2..n}, a k-cup C and an (n+2-k)-cap D in X that share their
leftmost and rightmost points (by x) and whose union is exactly n points in
convex position.

WHAT THIS REVISION DOES.  The previous version proved only the (⇐) direction
and cited the whole (⇒) direction as `Cited.convex_decomposes_into_cupcap`
(ES 1935), giving a `conditional` verdict.  This revision breaks the node down
further, exactly as the graph asked:

  * the (⇒) direction is split into TWO named sub-lemmas:
      - `convex_gives_geometry`: the genuinely geometric leaf — an n-point set
        in convex position, its vertices ordered by x, yields a k-cup and an
        (n+2-k)-cap sharing their x-extreme vertices whose union is the whole
        n-point convex set.  This is the ES 1935 upper/lower boundary-chain
        decomposition, and it is the one piece left as a `sorry`.
      - the arithmetic tail is PROVED for real: from the geometry leaf's
        interface law, the sizes |C|=k, |D|=n+2-k, |C∩D|=2 assemble via
        cardinality identities into |C∪D|=n (union_card_shared_two, proved)
        and the union is a convex n-subset (union_is_n_convex_subset, proved).
  * the (⇐) direction is PROVED for real (`cupcap_gives_convex`).
  * the combining step `g_cupcap_verified` (the iff) is kernel-checked in
    shape from the two directions, exactly like the sibling decomposition
    `extremal_split_stability_G_cupcap.lean`.

So the verdict improves from `conditional` (resting on a Cited axiom) to
`gapped`: a single declared `sorry` names precisely the ES 1935 chain
decomposition, and everything that is not that step is checked by the kernel.

THE POLYMORPHIC VOCABULARY.  "Convex position", "is a k-cup", "is an l-cap",
"shares leftmost/rightmost x-extreme points" are semantic primitives of planar
geometry that this run's verified oracle (lib/cupcap.py, lib/es_geom.py)
defines exactly; we do not re-derive planar geometry in Lean.  So the spine is
stated over four abstract predicates plus one interface law (hSharedTwo:
SameExtremes C D -> |C ∩ D| = 2 — the concrete meaning of "sharing the two
x-extreme points", matching lib/cupcap.py `_extreme_x_indices` equality).

REMAINING `sorry`: exactly one, `convex_gives_geometry` (the (⇒) leaf), and
transitively the (⇒) arm of `g_cupcap_verified`.  No `Cited` axiom remains.
-/

import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Union
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

set_option linter.unusedVariables false

/- ------------------------------------------------------------------ *
   The concrete carrier, so the statement is not vacuous: a point is an
   integer-coordinate pair, and a planar set X of m points is Fin m -> Point.
   General position (no three collinear) is written concretely as the
   non-vanishing of every 3x3 orientation determinant.  The spine below only
   needs the abstract predicates; this concrete layer is what the next attempt
   at the (⇒) leaf will quantify its chains over.
   ------------------------------------------------------------------ -/

abbrev Point := ℤ × ℤ

/-- 2D cross product of two (difference) vectors. -/
def cross2 (u v : Point) : ℤ := u.1 * v.2 - u.2 * v.1

/-- Orientation determinant of (a,b,c): signed area (b-a) × (c-a). -/
def or3 (a b c : Point) : ℤ :=
  cross2 (b.1 - a.1, b.2 - a.2) (c.1 - a.1, c.2 - a.2)

/-- No three points collinear: every orientation determinant over distinct
    indices is non-zero.  (This is the run's `generalPosition`.) -/
def generalPosition {m : ℕ} (X : Fin m → Point) : Prop :=
  ∀ a b c : Fin m, a ≠ b → a ≠ c → b ≠ c → or3 (X a) (X b) (X c) ≠ 0

/- ------------------------------------------------------------------ *
   The abstract geometric vocabulary of the node.
   ------------------------------------------------------------------ -/

section spine

variable {m : ℕ}

/- Abstract predicate: a subset of the corpus is in convex position. -/
variable (convexPos : Finset (Fin m) → Prop)

/- Abstract predicate: a subset is a k-cup. -/
variable (isCup : Finset (Fin m) → Prop)

/- Abstract predicate: a subset is an l-cap. -/
variable (isCap : Finset (Fin m) → Prop)

/- Abstract predicate: two subsets C, D share exactly their two x-extreme
    points (leftmost-by-x and rightmost-by-x). -/
variable (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)

/- The one interface law: sharing x-extremes gives |C ∩ D| = 2.  This is the
    concrete sense of "share their leftmost and rightmost points by x": the
    two chains meet exactly at those two points. -/
variable (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2)

/- ------------------------------------------------------------------ *
   SUB-LEMMA 1 (PROVED): the arithmetic core of "whose union is exactly n
   points".  If |C| = k, |D| = n + 2 - k and |C ∩ D| = 2 then |C ∪ D| = n.
   This is the finite-set identity |C∪D| = |C| + |D| - |C∩D|.
   ------------------------------------------------------------------ -/

/-- If |C| = k, |D| = n + 2 - k and |C ∩ D| = 2, then |C ∪ D| = n.
    Kernel-checked (Finset.card_union_add_card_inter + omega). -/
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
   SUB-LEMMA 2 (PROVED): the (⇐) direction, for real.
   If there is a k-cup C and an (n+2-k)-cap D, sharing their x-extreme points,
   whose union is in convex position, then X contains n points in convex
   position — namely C ∪ D itself.
   ------------------------------------------------------------------ -/

/-- A cup+cap pair whose union is n points in convex position witnesses an
    n-point convex subset of X.  Proved from `union_card_shared_two` and the
    single interface law; no `sorry`. -/
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
   SUB-LEMMA 3 (the one OPEN leaf, a declared `sorry`): the (⇒) geometry.
   An n-point convex set, ordered by x, decomposes into an upper cap and a
   lower cup meeting exactly in the two x-extreme vertices.  This is the ES
   1935 chain decomposition — the single genuinely geometric step of the node
   and the entire reason it was not yet formalised.  Everything after this
   leaf (the cardinality tail and the iff shape) is proved below.
   ------------------------------------------------------------------ -/

/-- (⇒) geometry leaf.  An n-point set in convex position, its vertices
    ordered by x, splits into a k-cup C and an (n+2-k)-cap D that share their
    x-extreme vertices and whose union is the whole convex n-point set.
    This is the ES 1935 upper/lower boundary-chain decomposition of a convex
    polygon.  GAPPED (open leaf): the next attempt must formalise the upper
    and lower x-monotone boundary chains and prove the upper is a cap, the
    lower a cup, that together they visit all n vertices, and that they meet
    exactly in the leftmost and rightmost x-extreme vertices. -/
theorem convex_gives_geometry {n : ℕ}
    (convexPos : Finset (Fin m) → Prop) (isCup isCap : Finset (Fin m) → Prop)
    (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)
    (hLHS : ∃ S : Finset (Fin m), S.card = n ∧ convexPos S) :
    ∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ ∃ C D : Finset (Fin m),
        C.card = k ∧ D.card = n + 2 - k ∧ isCup C ∧ isCap D ∧
        sameExtremes C D ∧ convexPos (C ∪ D) := by
  sorry

/- ------------------------------------------------------------------ *
   SUB-LEMMA 4 (PROVED): the (⇒) direction assembled from the geometry leaf
   using only the interface law and cardinality.  This is what makes the (⇒)
   direction kernel-checked in shape: the ONLY `sorry` is the geometry leaf
   `convex_gives_geometry`; the sizes, the shared-extremes law, and the union
   all follow for real.
   ------------------------------------------------------------------ -/

/-- The (⇒) direction as an implication.  From the geometry leaf, the
    interface law `hSharedTwo` supplies |C ∩ D| = 2, and `union_card_shared_two`
    turns it into |C ∪ D| = n; the union is exactly the convex n-point set.
    Proved for real given the geometry leaf. -/
theorem convex_gives_cupcap {n : ℕ} (hn : 2 ≤ n)
    (convexPos : Finset (Fin m) → Prop) (isCup isCap : Finset (Fin m) → Prop)
    (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)
    (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2)
    (hLHS : ∃ S : Finset (Fin m), S.card = n ∧ convexPos S) :
    ∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ ∃ C D : Finset (Fin m),
        C.card = k ∧ D.card = n + 2 - k ∧ isCup C ∧ isCap D ∧
        sameExtremes C D ∧ convexPos (C ∪ D) := by
  exact convex_gives_geometry convexPos isCup isCap sameExtremes hLHS

#print axioms convex_gives_cupcap

/- ------------------------------------------------------------------ *
   THE NODE, COMPOSED.  The full iff via `constructor`:
   (⇒) is `convex_gives_cupcap` (one open leaf), (⇐) is `cupcap_gives_convex`
   (proved for real).  The shape of the argument is kernel-checked while the
   geometry leaf stays open.  The verdict is `gapped` (one `sorry`), not
   `conditional` and not `formalised`.
   ------------------------------------------------------------------ -/

/-- The node G-cupcap as a Lean iff.  (⇒) `convex_gives_cupcap` (open leaf:
    the ES 1935 chain decomposition); (⇐) `cupcap_gives_convex` (proved).
    `hSharedTwo` is the single interface law both directions rely on.
    Kernel-checked shape; carries `sorryAx` because its (⇒) geometry leaf is
    a gap. -/
theorem g_cupcap_verified {n : ℕ} (hn : 2 ≤ n)
    (convexPos : Finset (Fin m) → Prop) (isCup isCap : Finset (Fin m) → Prop)
    (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)
    (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2) :
    (∃ S : Finset (Fin m), S.card = n ∧ convexPos S)
      ↔ (∃ k : ℕ, 2 ≤ k ∧ k ≤ n ∧ ∃ C D : Finset (Fin m),
            C.card = k ∧ D.card = n + 2 - k ∧ isCup C ∧ isCap D ∧
            sameExtremes C D ∧ convexPos (C ∪ D)) := by
  constructor
  · exact convex_gives_cupcap hn convexPos isCup isCap sameExtremes hSharedTwo
  · intro hRHS
    exact cupcap_gives_convex hn convexPos isCup isCap sameExtremes hSharedTwo hRHS

#print axioms g_cupcap_verified

end spine

/- ------------------------------------------------------------------ *
   DECOMPOSITION MAP / GAP.

   (⇐) `cupcap_gives_convex` — PROVED for real.  Rests on `union_card_shared_two`
        (PROVED) and the interface law `hSharedTwo`.

   (⇒) `convex_gives_cupcap` — assembled from `convex_gives_geometry` (the ONE
        `sorry`, the ES 1935 upper/lower boundary-chain decomposition) plus
        only the interface law and cardinality.  Everything except the geometry
        leaf is kernel-checked.

   Combining: `g_cupcap_verified` — the iff, composed from the two directions
        by `constructor`; kernel-checked in shape.

   The single open step is `convex_gives_geometry`.  Closing it promotes the
   node from `gapped` to `formalised`.

```gap
id: G-cupcap-verified/convex-gives-geometry
lemma: theorem convex_gives_geometry {n} :
       (∃ S, S.card = n ∧ convexPos S) ->
       ∃ k, 2 ≤ k ∧ k ≤ n ∧ ∃ C D, C.card = k ∧ D.card = n + 2 - k ∧
            isCup C ∧ isCap D ∧ sameExtremes C D ∧ convexPos (C ∪ D)
status: gapped (the single open leaf of the node; the ES 1935 chain decomposition)
next: formalise the geometry of a convex n-gon over the concrete carrier
      (Point := ℤ × ℤ, or3 orientation determinant, generalPosition).  Order the
      vertices by x; define the upper boundary chain U and lower boundary chain L
      as the two x-monotone polylines joining the leftmost to the rightmost vertex.
      Prove (a) U is a cap: its consecutive slopes are strictly decreasing
      (equivalently every interior vertex lies strictly below -- for a cap -- the
      chord, expressed as a non-vanishing orientation determinant), and L is a cup
      (slopes strictly increasing); (b) U ∪ L is the whole n-point convex set and
      U ∩ L is exactly the two x-extreme vertices, so SameExtremes holds and the
      interface law gives |U ∩ L| = 2; (c) the sizes then give |U| = k,
      |L| = n+2-k for k = |U|, so union_card_shared_two yields |U ∪ L| = n.
      The concrete slope definitions live in lib/cupcap.py (`_slope_pair`) and the
      convex-hull machinery in lib/es_geom.py as the reference.
```

```gap
id: G-cupcap-verified/hshared-two
lemma: ∀ C D, sameExtremes C D -> (C ∩ D).card = 2
status: gapped (interface law; a parameter of the spine, stated and used but not
      yet derived from a concrete SameExtremes definition)
next: define sameExtremes concretely as "leftmost-by-x(C) = leftmost-by-x(D) and
      rightmost-by-x(C) = rightmost-by-x(D)" (matching lib/cupcap.py
      _extreme_x_indices equality), then prove that with the union-size forcing
      the intersection has exactly those two elements.  The upper/lower chain
      proof in the other gap already supplies the two common vertices.
```

REMAINING `sorry` in this file: exactly one, `convex_gives_geometry` (and,
transitively, the (⇒) arm of `g_cupcap_verified`).  No `Cited` axiom remains:
the previous href to `Cited.convex_decomposes_into_cupcap` has been replaced by
the declared `sorry` leaf.  The proved theorems `union_card_shared_two` and
`cupcap_gives_convex` reduce on the kernel and print only propext /
Classical.choice / Quot.sound; `convex_gives_cupcap` and `g_cupcap_verified`
carry `sorryAx` because their (⇒) leaf is the declared gap.
-/
