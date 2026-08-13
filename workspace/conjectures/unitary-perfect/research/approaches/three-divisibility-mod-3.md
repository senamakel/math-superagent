# 3 | n via a mod-3 reduction of the exact unitary-perfect balance

```approach
idea: Settle the listed open question "is 3 | n forced for a sixth example" by
  reducing the exact balance (2^a+1)·Π(p_i^{e_i}+1) = 2^{a+1}·Π p_i^{e_i}
  modulo 3 (and LTE valuations), turning it into a finite congruence/counting
  condition on the odd components — a change of representation from the
  H_even/3-Higgs branch back to the unitary-perfect balance itself.
mechanism: The exact balance gives 2^a+1 | m (the odd part), since
  gcd(2^a+1, 2^{a+1}) = 1. If a is odd then 3 | 2^a+1, hence 3 | m, hence
  3 | n — so odd a forces 3 | n outright (verified on 6 and 90, both a = 1).
  The remaining case is a even with 3 ∤ n. Then 2^a+1 ≡ 2 (mod 3) and, reducing
  the balance mod 3, each component must satisfy p_i^{e_i}+1 ≢ 0 (mod 3), i.e.
  every p_i ≡ 2 (mod 3) must have even exponent e_i, and one obtains the parity
  equation (−1)^{ω+1} ≡ (−1)^{a+1}·(m mod 3) (mod 3) relating ω, a, and m mod 3.
  Combined with the proved budget ω(odd part) ≤ a+1 and Frei's theorem (a UPN
  not divisible by 3 has 2^a | n with a ≥ 144, ω ≥ 144, n > 10^440), this is a
  sharp structural statement: any 3∤n counterexample has a even ≥ 144, all its
  2 mod 3 components to even exponent, and a fixed parity relation among
  (ω, a, m mod 3). The deliverable is a proved lemma ("odd a forces 3 | n";
  the even-a case carries the mod-3 structure above), plus a push to eliminate
  the even-a branch by combining the parity relation with the budget and the
  mod-8/16 seed structure of 2^a+1. This is elementary congruence arithmetic
  (with LTE), not a search and not a re-derivation of the 2-adic budget — it
  uses the budget as an input to force 3-divisibility.
status: proposed
first-step: (1) Verify the lemma against all five witnesses with the oracle
  (all five have 3 | n, so the lemma's 3∤n branch is vacuous for them — check
  it does not forbid any witness); (2) reduce the balance mod 3 in exact
  arithmetic for the five to confirm the parity equation; (3) run a literature
  check on Subbarao–Warren Lemma 2 (the "3-divisibility" lemma already noted in
  CONTEXT) so that what is new is the even-a mod-3 refinement, not the odd-a
  fact, and adjust the claim's novelty statement accordingly.
```

Notes for research to settle: (a) does Subbarao–Warren 1966 (or Frei 1978)
already contain "odd a forces 3 | n" — if so the new content is only the even-a
mod-3 structure and the parity relation, and the claim must be stated that way;
(b) Frei's exact theorem statement (a ≥ 144, ω ≥ 144, n > 10^440 for 3 ∤ n),
currently only OEIS-recorded and unverified against the primary text; (c)
whether the parity relation (−1)^{ω+1} ≡ (−1)^{a+1} m (mod 3) is already in the
literature. Falsifier: a 3∤n example (or a witness showing the parity relation
is wrong) would refute the structural claim; since all five witnesses have 3 | n,
the sharpest check is that the lemma's even-a branch must be *consistent with*
60 (a=2, 3|60), 87360 (a=6, 3|87360) and the fifth (a=18, 3|fifth) — none may be
forbidden.
