import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- Link A of Granville Lemma 5.4 -- the "v <= g*_n" bound, proved by the
-- |a-b| <= max(a,b) induction.
--
-- In the right-diagonal reduction the orbit is
--     x_0 = v,   x_{s+1} = |x_s - e_s|
-- (the same `runAbs` as descent_lemma.lean), and g*_n is the record gap -- a
-- common upper bound M for the start v and every epsilon e_s.  Link A is the
-- claim that the whole orbit never exceeds that bound:
--
--     runAbs v el <= M    for any M with  v <= M  and  forall e in el, e <= M.
--
-- The engine is the pointwise inequality  |a - b| <= max(a,b) (every descent
-- step keeps the value <= the running max), and the "running max" is supplied
-- concretely as  max v (maxAll el)  -- i.e.  [0, max(v, max_s e_s)].  The
-- lower bound 0 is automatic for naturals, so the invariant is exactly "the
-- orbit stays within [0, max(v, max e_s)]".
--
-- This file does NOT construct g*_n from the triangle: that needs the
-- reduction-passage geometry Delta_k(q_n) = |Delta_{k-1}(q_n) - eps_k| with
-- eps_k = Delta_{k-1}(q_{n-1}) (claim reduction-passage-exact), and the record
-- gap g*_n itself.  What is proved here, sorry-free, is the part of Link A
-- that is purely combinatorial and independent of the geometry.
-- ============================================================================

-- The orbit / trajectory:  x_0 = w,  x_{s+1} = |x_s - e_s|.
-- (Same convention and name as descent_lemma.lean; redefined here so this
-- file is self-contained.)
def runAbs : Nat → List Nat → Nat
  | w, [] => w
  | w, e :: rest => runAbs (Nat.dist w e) rest

-- ===========================================================================
-- The core induction lemma: |a - b| <= max(a, b) for all naturals.
-- Each descent step keeps the value <= the running max.
-- ===========================================================================
lemma dist_le_max (a b : Nat) : Nat.dist a b ≤ max a b := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    omega

-- ===========================================================================
-- maxAll : the maximum of a list of naturals (0 for the empty list).
-- ===========================================================================
def maxAll : List Nat → Nat
  | [] => 0
  | e :: rest => max e (maxAll rest)

-- Every element of a list is at most its maxAll.
lemma maxAll_ge : ∀ el : List Nat, ∀ e : Nat, e ∈ el → e ≤ maxAll el
  | [], e, he => by simp at he
  | a :: rest, e, he => by
      cases he with
      | head => exact le_max_left a (maxAll rest)
      | tail hrest =>
          exact le_trans (maxAll_ge rest e hrest) (le_max_right a (maxAll rest))

-- ===========================================================================
-- The generic orbit invariant (Link A, combinatorial core):
-- if the start w and every epsilon e_s are all bounded above by M, then the
-- whole orbit runAbs w el is bounded above by M.  The lower bound 0 is
-- automatic for naturals, so the orbit lives inside [0, M].
-- ===========================================================================
lemma run_le : ∀ el : List Nat, ∀ w M : Nat,
    w ≤ M → (∀ e ∈ el, e ≤ M) → runAbs w el ≤ M
  | [], w, M, hw, hM => by
      simpa [runAbs] using hw
  | e :: rest, w, M, hw, hM => by
      have he : e ≤ M := hM e (by simp)
      have hdM : Nat.dist w e ≤ M :=
        le_trans (dist_le_max w e) (max_le hw he)
      have hrest : ∀ e' ∈ rest, e' ≤ M := by
        intro e' he'
        exact hM e' (by simp [he'])
      exact run_le rest (Nat.dist w e) M hdM hrest

-- ===========================================================================
-- The boundedness invariant with the maximal bound made explicit:
--   runAbs v el <= max v (maxAll el).
-- This is Link A modulo the identification of g*_n as a common upper bound
-- of v and the e_s.
-- ===========================================================================
theorem orbit_le_max (el : List Nat) (v : Nat) :
    runAbs v el ≤ max v (maxAll el) := by
  apply run_le
  · exact le_max_left v (maxAll el)
  · intro e he
    exact le_trans (maxAll_ge el e he) (le_max_right v (maxAll el))

-- ---------------------------------------------------------------------------
-- Axiom footprint.
-- ---------------------------------------------------------------------------
#print axioms dist_le_max
#print axioms maxAll_ge
#print axioms run_le
#print axioms orbit_le_max
