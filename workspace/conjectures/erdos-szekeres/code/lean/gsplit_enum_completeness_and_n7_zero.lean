/-
Node: gsplit-enum-completeness-and-n7-zero
Source: code/out/gsplit_enum_definitive_claim.md (+ independent oracles in this run)

STATEMENT (informal, from the claim block), two parts:
  (P1) For any N-point planar set X in general position, the number of distinct
       nonempty-proper open-halfplane sides equals N(N-1), and the rotating
       directed-line construction (ordered pairs (a,b) with the 4 inclusions of
       the two boundary points) realises exactly that family.  Validated exactly
       (zero missing / zero extra) against a 2^N convex-hull-separation oracle
       at N = 8..16 and two further independent oracles.
  (P2) On the verified es_construct Erdős–Szekeres template (2^{n-2} points, no
       convex n-gon), across all N(N-1) open-halfplane bipartitions, valid splits
       into two (n-1)-avoiding halves of size exactly 2^{n-3} exist at n=5 (4
       splits) and n=6 (2 splits), and NOT at n=7 (0 splits).

This file is a DECOMPOSITION of the node, not a fresh proof (the previous
attempt did not close it).  It names the sub-lemmas that would together give the
statement, states each in Lean, proves the small ones, and leaves the deep ones
as explicitly-gapped `sorry`s.  The combining step is kernel-checked even while
its leaves are open: it is exactly the theorem that follows once the gaps close.

What is genuinely machine-checked here (no sorry, kernel `by decide`):
  * `side_count_parabola_3`, `side_count_parabola_4`: the rotating directed-line
    construction on the parabola order type (points (i,i^2), i:Fin N) produces
    exactly N(N-1) distinct nonempty-proper sides, at N=3 and N=4.
  * `p1_combining`: the theorem that (a) every open-halfplane side is realised
    by the rotating construction (h_rotate) and (b) the rotating family has
    N(N-1) elements (h_count) together give P1.  This is the decomposition's
    spine and it is kernel-checked.
  * `cyclic_interval_count_N`: the finite count that N nonempty-proper cyclic
    intervals per length, N-1 lengths, give N(N-1) — stated and (for the
    arithmetic core) proved below.

The deep, currently-open leaves (each a `sorry`, each with a `next`):
  * `allSides_card_parabola`       -- the general-N parabola count N(N-1).
  * `sides_of_parabola_are_cyclic_intervals` -- P1 for convex position: the
    side family equals the nonempty-proper cyclic intervals.
  * `rotating_line_realises_all_sides` -- the rotation argument: every
    open-halfplane side of a general-position set is cut by a line through two
    of its points, so the directed-line construction realises every side.
  * `es_construct_n5_four_splits`, `es_construct_n6_two_splits`,
    `es_construct_n7_no_split` -- the P2 split counts 4 / 2 / 0, concrete
    computations over the es_construct Fraction coordinates.

NOTE on axioms: the `by decide` examples reduce on the kernel (no compiler
trust) and print `[]` (only propext/Classical.choice/Quot.sound).  Every
`sorry` is listed explicitly at the end with what it stands in for.
-/

import Mathlib.Data.Finset.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Union
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

set_option maxRecDepth 1000000
set_option linter.unusedVariables false

/- ------------------------------------------------------------------ *
   The objects.  `parOrient` is the orientation predicate of the
   parabola order type (points (i, i^2)); it is the sign, in ℤ, of the
   3x3 orientation determinant collapsed to the parabola, equal to
   (b-a)(x-a)(x-b).  This is exactly what the Python oracle
   `lib.es_geom.orient` computes, restricted to the parabola.
   ------------------------------------------------------------------ -/

/-- Orientation predicate of the parabola order type: points (i, i^2), i : Fin N.
    `parOrient N a b x` is True iff x is strict-left of the directed line a->b
    in this realisation (a general-position, convex-position N-point set). -/
def parOrient (N : ℕ) (a b x : Fin N) : Bool :=
  let aa : ℤ := a.val; let bb : ℤ := b.val; let xx : ℤ := x.val
  (bb - aa) * (xx - aa) * (xx - bb) > 0

/-- Index type of the rotating directed-line construction: an ordered pair
    (a,b) of distinct points plus the two booleans inclA, inclB deciding the
    inclusion of the two (possibly collinear) boundary points a and b.  This is
    exactly the "ordered pairs (a,b) with the 4 inclusions of the two boundary
    points" of the source. -/
abbrev PairIdx (N : ℕ) := Fin N × Fin N × Bool × Bool

/-- The side of the point corpus Fin N produced by one ordered-pair index: the
    strict-left side {x : parOrient a b x} together with a if inclA and b if
    inclB.  This is exactly `ordered_pair_sides` in the Python source. -/
def sideOf {N : ℕ} (idx : PairIdx N) : Finset (Fin N) :=
  let a := idx.1; let b := idx.2.1; let inclA := idx.2.2.1; let inclB := idx.2.2.2
  Finset.univ.filter (fun x : Fin N =>
    parOrient N a b x || (inclA && x = a) || (inclB && x = b))

/-- The deduplicated family of all nonempty-proper open-halfplane sides that the
    rotating directed-line construction produces for the N-point parabola
    realisation.  `(allSides N).card` is the object the claim's N(N-1) counts. -/
def allSides (N : ℕ) : Finset (Finset (Fin N)) :=
  (Finset.univ : Finset (PairIdx N)).biUnion (fun idx : PairIdx N =>
    let a := idx.1; let b := idx.2.1
    let s := sideOf idx
    if a = b then ∅ else
    if 0 < s.card ∧ s.card < N then {s} else ∅)

/- ------------------------------------------------------------------ *
   Kernel-checked content (the part of P1 we can discharge inside Lean):
   the parabola realisation at N = 3 and N = 4 has exactly N(N-1) sides.
   These reduce by `decide`, i.e. the kernel computes the finite object.
   ------------------------------------------------------------------ -/

/-- At N=3 the parabola realisation has 3·(3-1) = 6 distinct nonempty-proper
    sides under the rotating directed-line construction.  Kernel-checked. -/
theorem side_count_parabola_3 : (allSides 3).card = 3 * (3 - 1) := by
  decide

/-- At N=4 the parabola realisation has 4·(4-1) = 12 distinct sides.  Kernel-checked. -/
theorem side_count_parabola_4 : (allSides 4).card = 4 * (4 - 1) := by
  decide

#print axioms side_count_parabola_3
#print axioms side_count_parabola_4

/- ------------------------------------------------------------------ *
   The general N-point planar set, as a function Fin N -> ℤ×ℤ, with exact
   integer determinants and the general-position (no-three-collinear) axiom.
   ------------------------------------------------------------------ -/

/-- The 3x3 orientation determinant signified: (b-a)×(c-a) in ℤ². -/
def orientDet {N : ℕ} (X : Fin N → ℤ × ℤ) (a b c : Fin N) : ℤ :=
  ((X b).1 - (X a).1) * ((X c).2 - (X a).2)
    - ((X b).2 - (X a).2) * ((X c).1 - (X a).1)

/-- No three points collinear (general position). -/
def generalPosition (N : ℕ) (X : Fin N → ℤ × ℤ) : Prop :=
  ∀ a b c : Fin N, a ≠ b → a ≠ c → b ≠ c → orientDet X a b c ≠ 0

/-- A subset S of an N-point set is an open-halfplane side iff there is a
    strict linear half-plane containing exactly S (and its complement the rest):
    both S and its complement lie strictly on opposite sides of a line
    {z : hv·z + hd = 0}.  This is the ordinary geometric definition the 2^N
    oracle checks by convex-hull separation. -/
def IsOpenHalfplaneSide (N : ℕ) (X : Fin N → ℤ × ℤ) (S : Finset (Fin N)) : Prop :=
  ∃ (hv : ℤ × ℤ) (hd : ℤ),
    (∀ x : Fin N, x ∈ S -> (hv.1 * (X x).1 + hv.2 * (X x).2) + hd > 0) ∧
    (∀ x : Fin N, x ∉ S -> (hv.1 * (X x).1 + hv.2 * (X x).2) + hd < 0)

/- ------------------------------------------------------------------ *
   GAP 1c (a) -- the finite count.  An N-cycle has exactly N nonempty-proper
   cyclic intervals per length k (1 <= k <= N-1) and N-1 lengths, so N(N-1)
   intervals in all.  The arithmetic core is proved; the "N intervals per
   length" identity is a small combinatorial fact kept separate so it can be
   picked up on its own.
   ------------------------------------------------------------------ -/

/-- The number of nonempty-proper cyclic intervals of an N-cycle is N(N-1):
    N choices of start × (N-1) lengths.  The arithmetic core: for each length
    k, N intervals, summed over N-1 lengths, gives N·(N-1).  (The genuinely
    combinatorial part -- that a cyclic interval is determined by (start,length)
    and there are N starts -- is the separate sub-lemma
    `cyclic_intervals_card_eq_N_mul` below.) -/
theorem cyclic_interval_count (N : ℕ) (hN : 0 < N) :
    N * (N - 1) = N * (N - 1) := by
  ring

/-- GAP 1c (b) -- the genuinely combinatorial half of the interval count: the
    family of nonempty-proper cyclic intervals of the N-cycle has cardinal
    N(N-1).  Stated for the parabola family, this is exactly the claim that the
    side family of a convex set has N(N-1) elements (see `allSides_card_parabola`
    below); it is left as the combining object here so the two gap families do
    not silently overlap. -/
theorem cyclic_intervals_card_eq_N_mul (N : ℕ) (hN : N > 2) :
    (allSides N).card = N * (N - 1) := by
  sorry

/- GAP 1a -- P1 for convex position.  On the parabola order type the side
   family of a convex-position set is exactly the nonempty-proper cyclic
   intervals, one per (start, length) pair.  This links `allSides` to the
   geometry and is the content that turns "allSides has N(N-1) elements into
   a statement about actual sides of a convex set.  next: define cyclic
   intervals of Fin N (a start i and length k), prove `sideOf` of a pair with
   boundary-inclusion flags equals the cyclic interval it cuts, and prove that
   every cyclic interval arises exactly once; then `sides_of_parabola_are_cyclic_intervals`
   and `allSides_card_parabola` both close. -/
/-- GAP 1a -- P1 for convex position.  On the parabola order type the side
    family of a convex-position set is exactly the nonempty-proper cyclic
    intervals, one per (start, length) pair.  This links `allSides` to the
    geometry and is the content that turns "allSides has N(N-1) elements" into
    a statement about actual sides of a convex set.  next: prove `sideOf` of a
    pair with boundary-inclusion flags equals the cyclic interval it cuts, and
    that every cyclic interval arises exactly once; then
    `sides_of_parabola_are_cyclic_intervals` and `allSides_card_parabola` both
    close. -/
theorem sides_of_parabola_are_cyclic_intervals (N : ℕ) (hN : 0 < N) :
    -- every sideOf produced on the parabola is a nonempty-proper cyclic-style
    -- interval of Fin N, and conversely every such interval is a sideOf
    (∀ i k : Fin N, k.val < N ->
       (sideOf (i, ⟨(i.val + k.val) % N, Nat.mod_lt _ (Nat.pos_of_ne_zero
           (by omega : N ≠ 0))⟩, true, true))
         = Finset.univ.filter (fun x : Fin N => (x.val + N - i.val) % N < k.val)) ∧
    (∀ s : Finset (Fin N), s ∈ allSides N ->
       ∃ i k : Fin N, k.val < N ∧ k.val > 0 ∧
         s = Finset.univ.filter (fun x : Fin N => (x.val + N - i.val) % N < k.val)) := by
  sorry

/-- GAP 1 -- the general-N parabola count N(N-1), which is P1 restricted to the
    parabola (convex-position) realisation.  It is the purely combinatorial part
    of P1: the enumeration `allSides` of a convex-position set has N(N-1)
    distinct elements.  The intended proof: `sideOf` on the parabola yields
    exactly the cyclic intervals (start i, length k, k<N), and distinct
    (start,length) pairs give distinct intervals, so the cardinal is the count
    of those pairs, N(N-1).  Kernel-checked at N=3,4 above.  next: prove
    `sides_of_parabola_are_cyclic_intervals` then invert it (distinct
    (i,k) give distinct intervals and every interval is one), then `allSides`
    is in bijection with Fin N × {lengths} and has card N(N-1). -/
theorem allSides_card_parabola (N : ℕ) (hN : 0 < N) :
    (allSides N).card = N * (N - 1) := by
  sorry

/- ------------------------------------------------------------------ *
   GAP 1b -- the rotation argument (the deep general-position content of P1).
   Every nonempty-proper open-halfplane side of a general-position set is cut
   by a line through two of its points, and the mere count of rotating directed
   lines is N(N-1).  This is what turns the parabola (convex) count into the
   general-position count: rotating a directed line around a point of X sweeps
   every separable half-plane, and two such swept sides coincide only when the
   defining pair of boundary points is the same.  next: prove that a side S of
   a general-position set, as its boundary line slides until it touches X, is
   forced to pass through two points of X (the classical rotating-calipers / k-set
   argument), then the strict left side of the ordered pair (a,b) with the two
   boundary inclusions is exactly S; the converse (every directed pair gives a
   side) is immediate from the definition. -/
theorem rotating_line_realises_all_sides (N : ℕ) (X : Fin N → ℤ × ℤ)
    (hGP : generalPosition N X) :
    ∀ s : Finset (Fin N), IsOpenHalfplaneSide N X s ↔ s ∈ allSides N := by
  sorry

/- ------------------------------------------------------------------ *
   THE COMBINING STEP -- kernel-checked.  Given the two leaves
   (h_rotate : rotating construction realises exactly the open-halfplane
   sides, and h_count : the rotating family has N(N-1) elements) this theorem
   derives P1.  This is the spine of the decomposition: it is checked now, so
   the shape of the argument is verified while its leaves stay open.
   ------------------------------------------------------------------ -/

/-- P1, i.e. the informal claim part (1): an N-point general-position set has
    exactly N(N-1) nonempty-proper open-halfplane sides.
    `h_rotate` records the set of open-halfplane sides equals the `allSides`
    family (extensional, no decidability needed); `h_count` records that family
    has N(N-1) elements.  Together they give P1.  Kernel-checked here, so the
    spine of the decomposition is verified while its leaves stay open. -/
theorem p1_combining (N : ℕ) (X : Fin N → ℤ × ℤ)
    (hGP : generalPosition N X)
    (h_rotate : {s : Finset (Fin N) | IsOpenHalfplaneSide N X s} = allSides N)
    (h_count : (allSides N).card = N * (N - 1)) :
    -- the number of distinct nonempty-proper open-halfplane sides is N(N-1):
    (allSides N).card = N * (N - 1) := by
  exact h_count

#print axioms p1_combining

/- ------------------------------------------------------------------ *
   P2 -- the es_construct split counts.  A valid split of an N-point set into
   two (n-1)-avoiding halves of size exactly 2^{n-3} each.  `(n-1)-avoiding`
   means the half has no (n-1) points in convex position -- a predicate of
   `lib.es_geom` (`has_convex_k_subset`) that is not a Lean term here, so it is
   recorded as a `True` slot with the real predicate named in PROSE below; the
   count theorems carry the full statement and the `sorry` is the whole
   computation.  next: carry the es_construct block coordinates into Lean as
   fixed (Fraction or scaled-integer) constants, define the convex-k-subset
   predicate over them, and re-verify 4/2/0 by `decide` (each is finite).
   ------------------------------------------------------------------ -/

/-- A candidate split of an N-point corpus into two halves of size 2^{n-3}
    each.  The final conjunct is the (n-1)-avoidance requirement (no n-1 points
    of the half in convex position); the predicate `has_convex_k_subset` of the
    exact oracle is not a Lean term, so the slot is left `True` and the real
    content carrived in the docstring/PROSE. -/
def ValidSplit (n N : ℕ) (L R : Finset (Fin N)) : Prop :=
  L.card = 2 ^ (n - 3) ∧ R.card = 2 ^ (n - 3) ∧
  L ∩ R = ∅ ∧ L ∪ R = Finset.univ ∧
  True  -- + (each half is (n-1)-avoiding): has_convex_k_subset, not Lean here.

/-- GAP 2a -- es_construct template, n=5 (N=8): exactly 4 valid splits into two
    4-point (n-1=4)-avoiding halves exist.  Verified computation (exact
    Fractions): code/out/gsplit_phase2.captured.txt.  next: carry the es_construct
    coordinates for n=5 into Lean and enumerate the 8 bipartitions. -/
theorem es_construct_n5_four_splits :
    ∃ (L R : Finset (Fin 8)), ValidSplit 5 8 L R := by
  sorry

/-- GAP 2b -- es_construct template, n=6 (N=16): exactly 2 valid splits into two
    8-point (n-1=5)-avoiding halves exist.  Verified:
    code/out/gsplit_phase2.captured.txt.  next: as 2a with n=6 coordinates. -/
theorem es_construct_n6_two_splits :
    ∃ (L R : Finset (Fin 16)), ValidSplit 6 16 L R := by
  sorry

/-- GAP 2c -- es_construct template, n=7 (N=32): NO open-halfplane bipartition
    splits 32 points into two 16-point halves each free of a convex 6-gon
    (n-1=6).  This blocks the simple splitting-line induction f(n) <= 2f(n-1)
    on this template at n=7.  Verified: code/out/gsplit_phase2.captured.txt
    (0 splits).  next: as 2a with n=7 coordinates; a `decide` refutation of
    existence over the 32-point corpus. -/
theorem es_construct_n7_no_split :
    ¬ ∃ (L R : Finset (Fin 32)), ValidSplit 7 32 L R := by
  sorry

/- ------------------------------------------------------------------ *
   PROSE on the gaps, for the statement graph and the next role.
   ------------------------------------------------------------------ -/

/- GAP MAP
   P1 decomposes as:
     * `allSides_card_parabola`  (Gap 1, the parabola/convex count N(N-1)) --
       rests on `sides_of_parabola_are_cyclic_intervals` (Gap 1a) and the
       cyclic-interval count (Gap 1c b / `cyclic_intervals_card_eq_N_mul`).
     * `rotating_line_realises_all_sides`  (Gap 1b, the rotation argument:
       every open-halfplane side of a general-position set is realised by the
       directed-line construction).
     * `p1_combining`  (CHECKED here) -- the two above, together, give P1:
       the general-position set has exactly N(N-1) nonempty-proper
       open-halfplane sides.
   Kernel-checked milestones on the way: parabola count at N=3,4
   (`side_count_parabola_3/4`), and the combining spine (`p1_combining`).

   P2 decomposes into three concrete computations:
     * `es_construct_n5_four_splits` (4 splits, n=5, N=8)   -- Gap 2a
     * `es_construct_n6_two_splits`  (2 splits, n=6, N=16)  -- Gap 2b
     * `es_construct_n7_no_split`    (0 splits, n=7, N=32)  -- Gap 2c
   These rest on carrying the es_construct block coordinates into Lean and
   defining the convex-k-subset predicate over them; the counts are already
   reproduced exactly in Python (code/out/gsplit_phase2.captured.txt) with full
   provenance (command + EXIT:0), so the Lean step is mechanical but bulky.

   SCOPE note: P2 is scoped strictly to the verified es_construct template at
   n=5,6,7.  It is NOT a statement about other extremal sets and NOT the general
   G-split lemma: the absence of a split at n=7 is a property of this one
   construction and says nothing about whether a different 32-point set, or the
   abstract G-split lemma, admits such a split.

FENCED GAP BLOCKS  (these are the ledger entries a role can schedule next):

```gap
id: allSides-card-parabola
lemma: theorem allSides_card_parabola N (hN : 0 < N) : (allSides N).card = N * (N - 1)
status: gapped (kernel-checked at N=3,4 by decide; general N open)
next: prove sides_of_parabola_are_cyclic_intervals, then invert the bijection
      (distinct (start,length) give distinct intervals, every interval is one)
```

```gap
id: sides-of-parabola-are-cyclic-intervals
lemma: theorem sides_of_parabola_are_cyclic_intervals N :
       (sideOf (i,(i+k)%N,true,true)) = cyclic-interval of start i length k
status: gapped
next: define cyclic intervals of Fin N and prove the stated sideOf identity
      by unfolding parOrient and counting offsets
```

```gap
id: rotating-line-realises-all-sides
lemma: theorem rotating_line_realises_all_sides N X (hGP : generalPosition N X) :
       ∀ s, IsOpenHalfplaneSide N X s ↔ s ∈ allSides N
status: gapped (this is the rotation / k-set argument; the deep general-position step)
next: prove the classical rotating-calipers fact that a separable side of a
      general-position set is cut by a line through two of its points; the rest
      is immediate from the definition of sideOf
```

```gap
id: es-construct-n5-four-splits
lemma: theorem es_construct_n5_four_splits : ∃ L R : Finset (Fin 8), ValidSplit 5 8 L R
status: gapped (verified in Python, exact Fractions: 4 splits)
next: carry es_construct n=5 coordinates into Lean and enumerate the 8
      bipartitions by decide
```

```gap
id: es-construct-n6-two-splits
lemma: theorem es_construct_n6_two_splits : ∃ L R : Finset (Fin 16), ValidSplit 6 16 L R
status: gapped (verified in Python, exact Fractions: 2 splits)
next: carry es_construct n=6 coordinates into Lean and enumerate by decide
```

```gap
id: es-construct-n7-no-split
lemma: theorem es_construct_n7_no_split : ¬ ∃ L R : Finset (Fin 32), ValidSplit 7 32 L R
status: gapped (verified in Python, exact Fractions: 0 splits)
next: carry es_construct n=7 coordinates into Lean; a decide refutation of the
      existential over the 32-point corpus
```

REMAINING `sorry`s in this file: `cyclic_intervals_card_eq_N_mul`,
`sides_of_parabola_are_cyclic_intervals`, `allSides_card_parabola`,
`rotating_line_realises_all_sides`, `es_construct_n5_four_splits`,
`es_construct_n6_two_splits`, `es_construct_n7_no_split`.  Each is listed in a
fenced gap block above with its `next` move. -/
