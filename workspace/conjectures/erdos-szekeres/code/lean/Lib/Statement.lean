import Mathlib.Analysis.Convex.Hull
import Mathlib.Analysis.Convex.Extreme
import Mathlib.Data.Finset.Card
import Mathlib.Data.Real.Basic
import Mathlib.Order.ConditionallyCompleteLattice.Basic

/-!
# The Erdős–Szekeres (''happy ending'') conjecture — formal statement

We work over the real plane `ℝ × ℝ`. A *point set* is a finite subset
(`Finset Point`) of the plane; *general position* means no three are
collinear; *convex position* means that every point is a vertex (extreme
point) of the convex hull of the set.

`ES n` is the least `N` such that every `N`-point set in general position
contains `n` points in convex position.  The conjecture is `ES n = 2^(n-2) + 1`.
-/

abbrev Point := ℝ × ℝ

/-- Three points are collinear iff the doubled signed area (the 2x2
cross product of the two difference vectors) vanishes. -/
def collinear3 (a b c : Point) : Prop :=
  (b.1 - a.1) * (c.2 - a.2) - (b.2 - a.2) * (c.1 - a.1) = 0

/-- A finite point set is in **general position** iff no three of its points
are collinear.  (This is the no-three-collinear convention.) -/
def GeneralPosition (S : Finset Point) : Prop :=
  ∀ ⦃a⦄, a ∈ S → ∀ ⦃b⦄, b ∈ S → ∀ ⦃c⦄, c ∈ S →
    a ≠ b → a ≠ c → b ≠ c → ¬ collinear3 a b c

/-- A finite point set is in **convex position** iff every one of its points is
an extreme point (vertex) of the convex hull of the whole set.  Since a
`Finset` has distinct elements, this says precisely that the points are the
vertex set of their own convex polygon. -/
def ConvexPosition (S : Finset Point) : Prop :=
  (S : Set Point) ⊆ (convexHull ℝ (S : Set Point)).extremePoints ℝ

/-- The set `S` contains `n` points in convex position. -/
def ContainsConvexSubset (S : Finset Point) (n : ℕ) : Prop :=
  ∃ T : Finset Point, T ⊆ S ∧ T.card = n ∧ ConvexPosition T

/-- Every `N`-point set in general position contains `n` points in convex
position.  This is the worst-case predicate that `ES n` is the least `N`
making true. -/
def EveryNSetHasConvexSubset (N n : ℕ) : Prop :=
  ∀ S : Finset Point, S.card = N → GeneralPosition S → ContainsConvexSubset S n

/-- `ES n` = the least `N` such that every `N`-point set in general position
contains `n` points in convex position. -/
noncomputable def ES (n : ℕ) : ℕ :=
  sInf { N : ℕ | EveryNSetHasConvexSubset N n }

/-- **The Erdős–Szekeres conjecture**: for every `n ≥ 3`,
`ES n = 2^(n-2) + 1`.  The lower bound `ES n ≥ 2^(n-2) + 1` is known
(the 1960 construction); the statement `ES n ≤ 2^(n-2) + 1` is open. -/
theorem erdos_szekeres_conjecture (n : ℕ) (hn : 3 ≤ n) :
    ES n = 2 ^ (n - 2) + 1 := by
  sorry

#print axioms erdos_szekeres_conjecture
