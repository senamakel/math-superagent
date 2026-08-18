import Mathlib

/-!
# Hercher's Main Theorem 23: no Collatz m-cycle with m ≤ 91

Node `hercher-m92` (research/summaries/hercher-no-collatz-m-cycles.md):
there is no non-trivial Collatz m-cycle with m ≤ 91 local minima; equivalently,
every non-trivial cycle has at least 92 local minima (Main Theorem 23).

The accelerated Collatz map is C(n) = n/2 if n is even, (3n+1)/2 if n is odd
(Hercher, Definition 1).  An m-cycle is a non-trivial cycle with exactly m local
minima (Definition 5).  A local minimum of the cycle is an element that opens a
maximal block of consecutive odd elements (an o-run), i.e. an odd element whose
predecessor in the cycle is even.

Rendering choices, and where each hypothesis of the original is carried:

* "non-trivial cycle" — the paper works on Z>0 and calls a cycle non-trivial when
  its elements exceed 2 (equivalently, when it is not the trivial cycle {1, 2}).
  Rendered as `∀ x ∈ Ω, 2 < x`.  This also excludes the fixed point {0}, which
  exists in ℕ but not in the paper's domain Z>0; for cycles of T the two
  conditions agree, since the only cycles meeting {0, 1, 2} are {0} and {1, 2}.
* "m counts local minima" — `localMinimaCount Ω = m` is an explicit binder in the
  cited axiom, exactly as the node states it; the local-minima count is a pure
  function of the cycle Ω.
* The Main Theorem itself is cited (axiom `Cited.no_m_cycle_le_91`), not
  re-proved: its proof is a multi-page Diophantine-approximation argument with a
  computer-assisted case analysis (continued fractions, Theorem 21 and Lemma 22
  of the paper).  What is proved here, kernel-checked, is the corollary that the
  node's second phrasing — "any non-trivial cycle has at least m = 92 local
  minima" — follows from the cited exclusion.
-/

namespace Hercher

/-- The accelerated Collatz map C : Z>0 → Z>0, rendered total on ℕ:
    C(n) = n/2 if n is even, (3n+1)/2 if n is odd (Hercher, Definition 1). -/
def T (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

/-- A finite cycle of the accelerated map: Ω is nonempty and C permutes Ω. -/
def IsCycle (Ω : Finset ℕ) : Prop :=
  Ω.Nonempty ∧ Finset.image T Ω = Ω

/-- A non-trivial cycle: a cycle all of whose elements exceed 2.  In the paper's
    domain Z>0 a non-trivial cycle is one other than the trivial cycle {1, 2};
    since the only cycles of T meeting {0, 1, 2} are {0} and {1, 2}, the two
    renderings agree on cycles. -/
def IsNontrivialCycle (Ω : Finset ℕ) : Prop :=
  IsCycle Ω ∧ ∀ x ∈ Ω, 2 < x

/-- x is a local minimum of the cycle Ω: x is odd and is not the image under C of
    an odd element of Ω.  Equivalently (C is a bijection on a cycle) the
    predecessor of x in the cycle is even, so x opens a maximal block of
    consecutive odd elements — an o-run, in Hercher's terminology (Definition 6). -/
def IsLocalMinimum (Ω : Finset ℕ) (x : ℕ) : Prop :=
  x ∈ Ω ∧ x % 2 = 1 ∧ ∀ y ∈ Ω, y % 2 = 1 → T y ≠ x

/-- The set of local minima of Ω: odd elements not reached from an odd element. -/
def localMinima (Ω : Finset ℕ) : Finset ℕ :=
  Ω.filter fun x => x % 2 = 1 ∧ ∀ y ∈ Ω, y % 2 = 1 → T y ≠ x

/-- The number m of local minima of the cycle Ω (Hercher, Definition 5). -/
def localMinimaCount (Ω : Finset ℕ) : ℕ :=
  (localMinima Ω).card

end Hercher

namespace Cited

/-- src: Hercher 2022, "There are no Collatz m-Cycles with m ≤ 91",
    arXiv:2201.00406v3, Main Theorem 23.
    There is no non-trivial m-cycle of the accelerated Collatz map with
    m ≤ 91 local minima.  Cited from the paper; the proof is a
    Diophantine-approximation and computer-assisted argument not re-derived here. -/
axiom no_m_cycle_le_91
    (Ω : Finset ℕ) (m : ℕ)
    (hΩ : Hercher.IsNontrivialCycle Ω)
    (hm : Hercher.localMinimaCount Ω = m) :
    ¬ m ≤ 91

end Cited

/-- Main Theorem 23 of Hercher (2022) as a lower bound: every non-trivial cycle
    of the accelerated Collatz map has at least 92 local minima. -/
theorem hercher_m92 (Ω : Finset ℕ) (hΩ : Hercher.IsNontrivialCycle Ω) :
    92 ≤ Hercher.localMinimaCount Ω := by
  by_contra h
  have hm91 : Hercher.localMinimaCount Ω ≤ 91 := by omega
  exact (Cited.no_m_cycle_le_91 Ω (Hercher.localMinimaCount Ω) hΩ rfl) hm91

#print axioms hercher_m92
#print axioms Cited.no_m_cycle_le_91
