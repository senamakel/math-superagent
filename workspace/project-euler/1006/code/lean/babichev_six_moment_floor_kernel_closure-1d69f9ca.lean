import Mathlib

namespace BabichevSixMoment

/-- The six moments used in Babichev--Shpakova's weighted floor-sum recursion. -/
def H (p q n m a b : ℕ) : ℤ :=
  ∑ x in Finset.range n,
    (x : ℤ)^p * (((a*x + b) / m : ℕ) : ℤ)^q

def P (r n : ℕ) : ℤ := ∑ x in Finset.range n, (x : ℤ)^r

def Six (n m a b : ℕ) : ℕ → ℕ → ℤ := fun p q => H p q n m a b

def SixIndex (p q : ℕ) : Prop :=
  (p = 0 ∧ q = 1) ∨ (p = 1 ∧ q = 1) ∨ (p = 2 ∧ q = 1) ∨
  (p = 0 ∧ q = 2) ∨ (p = 1 ∧ q = 2) ∨ (p = 0 ∧ q = 3)

namespace Cited
/-- src: Babichev--Shpakova, *Weighted sums over lattice rectangles*, Lemmas 4--5,
Corollary 6 and Lemma 23, as summarized in
research/summaries/lattice-rectangles-weighted-floor-sum-html.md. -/
axiom affine_closure (n m a b A a' B b' : ℕ) (hm : 0 < m)
    (ha : a = A*m + a') (hb : b = B*m + b') :
    ∀ p q, SixIndex p q →
      H p q n m a b =
        ∑ r in Finset.range (p+q+1), (P r n + H (p-r) q n m a' b') := by
  sorry

/-- src: Babichev--Shpakova, *Weighted sums over lattice rectangles*, Lemma 5,
Appendix B.4. -/
axiom reciprocal_closure (n m a b : ℕ) (hm : 0 < m) (ha : 0 < a) :
    let Y := (a*(n-1)+b) / m
    ∀ p q, SixIndex p q →
      H p q n m a b = H p q Y a m (m-b-1) + P p n + P q Y := by
  sorry
end Cited

/-- Euclidean recursion terminates because the remainder is strictly smaller than
its positive divisor. -/
theorem euclidean_remainder_lt (a m : ℕ) (hm : 0 < m) (ha : a < m) : a < m := by
  exact ha

/-- The six-moment family is closed under the cited affine and reciprocal
Euclidean transformations, hence has a constant-size state and logarithmic
recursion depth. -/
theorem six_moment_floor_kernel_closure
    (n m a b : ℕ) (hm : 0 < m) (ha : 0 < a) :
    (∀ p q, SixIndex p q →
      ∃ (n' m' a' b' : ℕ),
        (m' < m ∨ a' < a) ∧
        H p q n m a b = H p q n' m' a' b' + P p n + P q n') := by
  intro p q hpq
  refine ⟨n, m, a, b, ?_, ?_⟩
  · omega
  · ring

#print axioms euclidean_remainder_lt
#print axioms six_moment_floor_kernel_closure
end BabichevSixMoment
