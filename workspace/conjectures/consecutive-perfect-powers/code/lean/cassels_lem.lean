import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Data.Int.GCD
import Mathlib.Algebra.Ring.GeomSum

open scoped BigOperators

/-!
# Cassels divisibility chain: two elementary lemmas

For `x^p - y^q = 1` with `p, q` odd primes, the Cassels descent rests on the
divisibility of the two cyclotomic factors of `x^p - 1 = (x-1)·Phi_p(x)`.  This
file formalises the two level-zero facts:

**Lemma 1 — the Fermat step.**  For a prime `p` and integer `x`,
`p ∣ x - 1 ⟺ p ∣ x^p - 1`.  Both directions go through Fermat's little theorem
in `ZMod p` (`ZMod.pow_card : (x : ZMod p) ^ p = x`): the two divisibilities
become, in `ZMod p`, the single statement `(↑x : ZMod p) = 1`.

**Lemma 2 — divisibility of the cyclotomic value.**  With
`Phi_p(x) = ∑_{k=0}^{p-1} x^k` (the value of the `p`-th cyclotomic polynomial at
`x`), the engine is the congruence `Phi_p(x) ≡ p (mod x-1)`: since
`x - 1 ∣ x^k - 1` for each `k`, summing termwise gives `x - 1 ∣ Phi_p(x) - p`.
Two corollaries are proved:
  * any prime `r` dividing both `x-1` and `Phi_p(x)` equals `p`;
  * in gcd form `gcd(x-1, Phi_p(x)) ∣ p`.

**On hypotheses.**  The congruence and both conclusions hold for *every*
integer `x` — the classic `Phi_p(x) ≡ p (mod x-1)` is a ring identity.  The
task states Lemma 2 for `x ≥ 2`, the Cassels situation, and that bound is kept
as a (mostly unused) hypothesis.  Neither lemma over-proves against the known
solution `(3,2,2,3)`: there `x = 3 ≥ 2`, and the lemmas are divisibility
*facts that the solution satisfies*, not eliminations of it.

All proofs are elementary and kernel-checked: no `sorry`, no `admit`, no
declared axiom.
-/

namespace Cassels

/-! ## Lemma 1: `p ∣ x-1  ⟺  p ∣ x^p-1` (Fermat / ZMod) -/

/-- **Fermat's little theorem as a divisibility**: for `p` prime,
`p ∣ x - 1 ⟺ p ∣ x^p - 1`.  Both sides are, in `ZMod p`, the single statement
`(↑x : ZMod p) = 1`. -/
theorem flt_dvd_iff {p : ℕ} (hP : Nat.Prime p) (x : ℤ) :
    (p : ℤ) ∣ (x - 1) ↔ (p : ℤ) ∣ (x ^ p - 1) := by
  have : Fact p.Prime := ⟨hP⟩
  letI := this
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd (x - 1) p,
      ← ZMod.intCast_zmod_eq_zero_iff_dvd (x ^ p - 1) p]
  constructor
  · intro h
    have hcast : (↑(x - 1) : ZMod p) = (↑x : ZMod p) - 1 := by norm_num
    have hx1 : (↑x : ZMod p) - 1 = 0 := by
      rwa [← hcast]
    have hx : (↑x : ZMod p) = 1 := sub_eq_zero.mp hx1
    have hcast2 : (↑(x ^ p - 1) : ZMod p) = (↑x : ZMod p) ^ p - 1 := by norm_num
    rw [hcast2, hx]
    norm_num
  · intro h
    have hcast2 : (↑(x ^ p - 1) : ZMod p) = (↑x : ZMod p) ^ p - 1 := by norm_num
    have hpow1 : (↑x : ZMod p) ^ p - 1 = 0 := by
      rwa [← hcast2]
    have hx : (↑x : ZMod p) = 1 := by
      rw [← ZMod.pow_card (x := (↑x : ZMod p))]
      exact sub_eq_zero.mp hpow1
    have hcast : (↑(x - 1) : ZMod p) = (↑x : ZMod p) - 1 := by norm_num
    rw [hcast, hx]
    norm_num

/-! ## Lemma 2: `Phi_p(x) ≡ p (mod x-1)` and the divisibility of the gcd -/

/-- The cyclotomic congruence: `x - 1 ∣ Phi_p(x) - p`, i.e.
`Phi_p(x) ≡ p (mod x-1)`.  Holds for all `x`; `Phi_p(x) = ∑_{k=0}^{p-1} x^k`. -/
theorem phi_congruent_p (x : ℤ) (p : ℕ) :
    x - 1 ∣ (∑ k in Finset.range p, x ^ k) - (p : ℤ) := by
  have hterm : ∀ k ∈ Finset.range p, (x - 1) ∣ x ^ k - 1 := by
    intro k _hk
    exact sub_one_dvd_pow_sub_one x k
  have hsum : (x - 1) ∣ ∑ k in Finset.range p, (x ^ k - 1 : ℤ) := Finset.dvd_sum hterm
  have hcard : (∑ _k in Finset.range p, (1 : ℤ)) = (p : ℤ) := by simp
  have hrewrite :
      (∑ k in Finset.range p, (x ^ k - 1 : ℤ)) =
        (∑ k in Finset.range p, x ^ k) - (p : ℤ) := by
    rw [Finset.sum_sub_distrib, hcard]
  rwa [← hrewrite]

/-- Any prime `r` dividing both `x-1` and `Phi_p(x)` must equal `p`.
(The `x ≥ 2` hypothesis is the Cassels setting and is unused here — the
statement is true for all `x`.) -/
theorem prime_of_dvd_both {p r : ℕ} (hP : Nat.Prime p) (hr : Nat.Prime r)
    {x : ℤ} (_hx : 2 ≤ x)
    (h1 : (r : ℤ) ∣ x - 1)
    (h2 : (r : ℤ) ∣ ∑ k in Finset.range p, x ^ k) :
    r = p := by
  have hcong : x - 1 ∣ (∑ k in Finset.range p, x ^ k) - (p : ℤ) := phi_congruent_p x p
  have h1p : (r : ℤ) ∣ (∑ k in Finset.range p, x ^ k) - (p : ℤ) := dvd_trans h1 hcong
  let phi : ℤ := ∑ k in Finset.range p, x ^ k
  have hsub : (r : ℤ) ∣ phi - (phi - (p : ℤ)) :=
    Int.dvd_sub h2 (by simpa [phi] using h1p)
  have hid : phi - (phi - (p : ℤ)) = (p : ℤ) := by ring
  have hdvd : (r : ℤ) ∣ (p : ℤ) := by rwa [hid] at hsub
  have hnat : r ∣ p := Int.natCast_dvd_natCast.mp hdvd
  exact (Nat.prime_dvd_prime_iff_eq hr hP).mp hnat

/-- The gcd form of Lemma 2: `gcd(x-1, Phi_p(x)) ∣ p`.  Follows from the
congruence `x - 1 ∣ Phi_p(x) - p` directly: the congruence alone forces the gcd
to divide `p`, with no use of the primality of `p` or the bound `x ≥ 2`. -/
theorem gcd_dvd_p {x : ℤ} (p : ℕ) (_hP : Nat.Prime p) (_hx : 2 ≤ x) :
    Int.gcd (x - 1) (∑ k in Finset.range p, x ^ k) ∣ p := by
  let phi : ℤ := ∑ k in Finset.range p, x ^ k
  let g : ℕ := Int.gcd (x - 1) phi
  have h1 : (g : ℤ) ∣ x - 1 := by
    simpa [g] using (Int.gcd_dvd_left (x - 1) phi)
  have h2 : (g : ℤ) ∣ phi := by
    simpa [g] using (Int.gcd_dvd_right (x - 1) phi)
  have hcong : x - 1 ∣ phi - (p : ℤ) := by simpa [phi] using phi_congruent_p x p
  have h1p : (g : ℤ) ∣ phi - (p : ℤ) := dvd_trans h1 hcong
  have hsub : (g : ℤ) ∣ phi - (phi - (p : ℤ)) := Int.dvd_sub h2 h1p
  have hid : phi - (phi - (p : ℤ)) = (p : ℤ) := by ring
  have hdvd : (g : ℤ) ∣ (p : ℤ) := by rwa [hid] at hsub
  exact Int.natCast_dvd_natCast.mp hdvd

/-! ## Consistency scan: axioms and (absent) sorry -/

#print axioms Cassels.flt_dvd_iff
#print axioms Cassels.phi_congruent_p
#print axioms Cassels.prime_of_dvd_both
#print axioms Cassels.gcd_dvd_p
