import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Finset.Basic

/-!
This file records, as Lean propositions, the run's decomposition of the
Singmaster boundary problem (see `research/backward/`, gap
`G-nonfibonacci-pairs-are-bounded`, GOAL.md Fibonacci directive 25-26).  It is
the **statement half** of the deliverable: every theorem here is a *recorded
statement with its gaps named*, ending in `:= by sorry`, not a proof.  The
purpose is to pin down the exact shape of the claim — the hypotheses, the
quantified objects, the convention used for counting multiplicity — so that the
informal lemma and its Lean rendering cannot drift apart while the proof is
pursued.

Files in `Lib/` render the run's established mathematics; this file instead
states the *open* gap and the two lemmas it rests on.  A `#print axioms` run
here enumerates exactly the `sorryAx` holes the run must fill next.

## The informal lemma being recorded

Let `N(a)` be the number of `(n,k)` with `0 ≤ k ≤ n` and `C(n,k) = a`,
counting **both** mirrors `(n,k),(n,n-k)` **and** the trivial pair
`C(a,1) = C(a,a-1)`.  The boundary cut (MRSTT Thm 1.3) is
`T(n) = exp((log n)^(2/3 + eps))` for a fixed admissible `0 < eps < 1`; a
left-half representative `(n,k)` is **boundary** iff `2 ≤ k < T(n)` (the
region MRSTT leaves open is exactly this small-`k` boundary).

The **open lemma** `G-nonfibonacci-pairs-are-bounded` states: there is a
computable absolute constant `C` such that the set of unordered pairs
`{k1,k2}`, with `2 ≤ k1 < k2`, for which there exists **any** boundary
collision

  `C(x,k1) = C(y,k2) = a`  with both reps `(x,k1)`,`(y,k2)` left-half boundary
  (so `(k1:ℝ) < T(x)`, `(k2:ℝ) < T(y)`) **and** with `{k1,k2}` **not** of the
  Fibonacci form `{k,k+1}` — is finite.

Why `{k,k+1}` is excluded: that is the one family with infinitely many lattice
points (CONTEXT.md "only infinite N>=6 family is the Pell/Singmaster one"), so
*without* excluding it finiteness is plainly false; the point of the gap is
that every *other* pair family should contribute only boundedly many
collisions.
-/

namespace Cited

/-- src: this run's `G-nonfibonacci-pairs-are-bounded` gap (GOAL.md
Fibonacci directive 25-26; research/backward/singmaster-uniform-bound).

**Column injectivity.**  For fixed column index `k ≥ 2` and value `a > 1`,
the row-right-half equation `C(n,k) = a` has at most one solution in
`n ≥ 2k` — i.e. any two solutions `n, n' ≥ 2k` with `C(n,k) = C(n',k) = a`
must satisfy `n = n'`.

STATUS: recorded as the first supporting gap (the proof is the monotonicity of
the falling-factorial column `n ↦ C(n,k)` on `n ≥ k`, hence injectivity on
the right half `n ≥ 2k`).  `sorry`.
-/
theorem column_injectivity_at_most_one (k a n n' : ℕ) :
    2 ≤ k → 1 < a → 2 * k ≤ n → 2 * k ≤ n' →
      Nat.choose n k = a → Nat.choose n' k = a → n = n' := by
  sorry

/--
src: this run's counting-convention claim (CONTEXT.md "Counting convention
(fixed)"; OEIS A003016 vs A059233; claim `half-triangle-convention-consistency`).

**Counting identity.**  Let `P` be the finite set of all pairs `(n,k)` with
`C(n,k) = a` (both mirrors and the trivial pair), and let `H` be the number of
**left-half nontrivial** representatives among them, i.e. those with
`2 ≤ k` and `2*k < n` (equivalently `2 ≤ k < n/2`).  Then `P.card = 2*H + 2`:
every left-half nontrivial rep is paired with its mirror `(n, n-k)`, and the
two trivial entries `C(a,1) = C(a,a-1) = a` account for the `+2`.

STATUS: recorded as the second supporting gap (the identity IS the run's fixed
both-mirrors-plus-trivial convention).  `sorry`.
-/
theorem counting_identity (a : ℕ) (P : Finset (ℕ × ℕ))
    (hP : ∀ p : ℕ × ℕ, p ∈ P ↔ ∃ n k : ℕ, Nat.choose n k = a ∧ p = (n, k))
    (H : ℕ)
    (hH : H = (P.filter (fun p : ℕ × ℕ => 2 ≤ p.2 ∧ 2 * p.2 < p.1)).card) :
    P.card = 2 * H + 2 := by
  sorry

/--
src: this run's open gap `G-nonfibonacci-pairs-are-bounded` (GOAL.md, the
directive that the Fibonacci family is the only obstruction to a constant
bound).

**The open lemma, recorded as a statement.**  Let `eps` be an admissible
boundary exponent `0 < eps < 1`.  Consider the set of pairs `(k1,k2)` with
`2 ≤ k1 < k2` for which there exists an integer `a > 1` and representatives
`(x,k1),(y,k2)` with

  • `C(x,k1) = C(y,k2) = a`,
  • both reps left-half boundary: `(k1 : ℝ) < exp((log x)^(2/3+eps))` and
    `(k2 : ℝ) < exp((log y)^(2/3+eps))`,
  • the pair is **not** of the Fibonacci form, i.e. `k2 ≠ k1 + 1`.

THEN this set is finite — bounded by a computable constant `C`, uniform in
`k1,k2,eps`.

STATUS: **open** — recorded with `sorry` (the deliverable's statement, not a
proof).  The constant `C` is required to be computable and uniform.  `sorry`.
-/
def boundaryPairs (eps : ℝ) : Set (ℕ × ℕ) :=
  { p : ℕ × ℕ |
      ∃ (k1 k2 x y a : ℕ),
        k1 < k2 ∧ 2 ≤ k1 ∧ k2 ≠ k1 + 1 ∧ 1 < a ∧
        Nat.choose x k1 = a ∧ Nat.choose y k2 = a ∧
        (k1 : ℝ) < Real.exp ((Real.log (x : ℝ)) ^ (2 / 3 + eps)) ∧
        (k2 : ℝ) < Real.exp ((Real.log (y : ℝ)) ^ (2 / 3 + eps)) ∧
        p = (k1, k2) }

theorem G_nonfibonacci_pairs_are_bounded (eps : ℝ) (heps0 : 0 < eps) (heps1 : eps < 1) :
    (boundaryPairs eps).Finite := by
  sorry

end Cited

-- Axiom census for the verdict.  Each theorem is a recorded statement ending
-- in `:= by sorry`, so each prints exactly `sorryAx`: the kernel checked the
-- statement's elaborations and nothing else.  The three `sorryAx` nodes are
-- the gaps this run must fill next (column injectivity, counting identity,
-- finiteness of the non-Fibonacci boundary-collision pair set).
#print axioms Cited.column_injectivity_at_most_one
#print axioms Cited.counting_identity
#print axioms Cited.G_nonfibonacci_pairs_are_bounded
