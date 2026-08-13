# 3 | n via a mod-3 reduction of the exact unitary-perfect balance

```approach
idea: Settle the listed open question "is 3 | n forced for a sixth example" by
  reducing the exact balance (2^a+1)·Π(p_i^{e_i}+1) = 2^{a+1}·Π p_i^{e_i}
  modulo 3, turning it into a finite congruence/counting condition on the odd
  components.
mechanism: The exact balance gives 2^a+1 | m (the odd part). If a is odd then
  3 | 2^a+1, hence 3 | m, hence 3 | n — so odd a forces 3 | n. The remaining
  case is a even with 3 ∤ n, which yields constraints on exponents of primes
  ≡ 2 (mod 3) and a parity relation (−1)^{ω+1} ≡ (−1)^{a+1}·(m mod 3).
  Combined with Frei's theorem (a ≥ 144 for 3 ∤ n) this constrains any
  counterexample sharply.
status: refuted
killed-by: The odd-a observation ("odd a ⟹ 3 | n") is correct but essentially
  already covered: Subbarao–Warren 1966 classifies a = 1 → {6, 90} and
  eliminates a = 3, 5, 7, so the odd-a case is either already classified
  (a = 1) or already excluded (a = 3, 5, 7). The even-a mod-3 parity relation
  constrains a hypothetical 3∤n counterexample but provides no mechanism to
  eliminate the even-a branch. Frei's bound (a ≥ 144, ω ≥ 144 for 3 ∤ n) is
  not held in the library's primary sources and cannot be checked against the
  original text. The parity relation combined with the 2-adic budget
  ω(odd) ≤ a + 1 does not force a contradiction — it is a constraint, not an
  obstruction. Subbarao–Warren themselves (Lemma 2, 1966 p. 149) explicitly
  state: "The authors have not been able to find any unitary perfect numbers
  not divisible by 3 nor have they been able to prove that there are none."
  60 years later the question is still open, and this approach adds a mod-3
  parity condition without eliminating the even-a branch it describes.
first-step: (1) Verify the lemma against all five witnesses with the oracle
  (all five have 3 | n, so the lemma's 3∤n branch is vacuous for them — check
  it does not forbid any witness); (2) reduce the balance mod 3 in exact
  arithmetic for the five to confirm the parity equation; (3) run a literature
  check on Subbarao–Warren Lemma 2 so that what is new is the even-a mod-3
  refinement, not the odd-a fact, and adjust the claim's novelty statement
  accordingly.
```