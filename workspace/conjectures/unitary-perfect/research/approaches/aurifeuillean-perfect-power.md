# ω(Φ_{4p}(2)) ≥ 2 via the perfect-power structure of the Aurifeuillean halves

```approach
idea: Attack the paper's missing hypothesis (H2) "ω(Φ_{4p}(2)) → ∞" from below,
  starting with the provable step ω ≥ 2, by re-writing Φ_{4p}(2) = Φ_p(−4) =
  (4^p+1)/5 and observing that ω ≥ 2 is equivalent to the Aurifeuillean halves
  L_p = 2^p − 2^{(p+1)/2} + 1 and M_p = 2^p + 2^{(p+1)/2} + 1 not being "both
  prime powers with the right 5-adic valuation".
mechanism: 2^{2p}+1 = (4)^p + 1 = V_p(5,4) is the Lucas sequence with roots 4
  and 1, and Φ_{4p}(2) = Φ_p(−4) = (4^p+1)/5. The Aurifeuillean split
  2^{2p}+1 = L_p·M_p with gcd(L_p, M_p) = 1 puts the primitive divisors into
  the two coprime halves. Exactly one of L_p, M_p is divisible by 5. The
  divisor count satisfies
      ω(Φ_{4p}(2)) = ω(L_p) + ω(M_p) − 1 + [ν5(L_p) ≥ 2 or ν5(M_p) ≥ 2].
  Hence ω(Φ_{4p}(2)) = 1 iff both halves are prime powers, and ω ≥ 2 otherwise.
  So "ω ≥ 2 for all large p" is exactly "L_p and M_p are not both prime
  powers", a statement of the form 2^p ∓ 2^{(p+1)/2} + 1 = q^k.
status: refuted
killed-by: The ω-formula decomposition is mathematically correct, but the
  deliverable — ω(Φ_{4p}(2)) ≥ 2 for all large p — is too weak to contribute
  to the paper's (H2) target. (H2) requires ω ≥ C log p for the conditional
  Theorem 30, or at minimum unbounded growth. ω ≥ 2 only excludes p = 3
  (where ω = 1: L_3 = 5, M_3 = 13, both prime). Iterating the same
  Diophantine method to reach ω ≥ 3, ω ≥ 4, … would require progressively
  harder perfect-power equations — each step a separate Bugeaud–Mignotte–Siksek
  problem — and the machinery for perfect powers in Lucas sequences may not
  cover numbers of the specific form 2^p ∓ 2^{(p+1)/2} + 1. The gap from ω ≥ 2
  to the paper's target is not bridgeable by iteration of the same method,
  and a modular congruence sieve (mod 8, 16) on the two halves cannot deliver
  ω ≥ C log p either.
first-step: Reproduce the split and the ω formula on the known small cases
  (p = 3: L=5, M=13, ω(Φ)=1; p = 5: L=25, M=41, ω(Φ)=2; p = 7: L=113,
  M=145=5·29, ω(Φ)=2) in exact integer arithmetic, then reduce the equation
  2^p ∓ 2^{(p+1)/2} + 1 = q^k modulo 8, 16 and small primes to find which
  residue classes of p (mod some modulus) force a composite factor in one half,
  i.e. prove ω ≥ 2 on an explicit infinite set of primes p.
```