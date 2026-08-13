# ω(Φ_{4p}(2)) ≥ 2 via the perfect-power structure of the Aurifeuillean halves

```approach
idea: Attack the paper's missing hypothesis (H2) "ω(Φ_{4p}(2)) → ∞" from below,
  starting with the provable step ω ≥ 2, by re-writing Φ_{4p}(2) = Φ_p(−4) =
  (4^p+1)/5 and observing that ω ≥ 2 is equivalent to the Aurifeuillean halves
  L_p = 2^p − 2^{(p+1)/2} + 1 and M_p = 2^p + 2^{(p+1)/2} + 1 not being "both
  prime powers with the right 5-adic valuation". That is a Diophantine
  (perfect-power) statement about near-powers of 2, with named machinery.
mechanism: 2^{2p}+1 = (4)^p + 1 = V_p(5,4) is the Lucas sequence with roots 4
  and 1, and Φ_{4p}(2) = Φ_p(−4) = (4^p+1)/5. The Aurifeuillean split
  2^{2p}+1 = L_p·M_p with gcd(L_p, M_p) = 1 puts the primitive divisors into
  the two coprime halves L_p = 2u²−2u+1, M_p = 2u²+2u+1 at u = 2^{(p−1)/2}.
  Exactly one of L_p, M_p is divisible by 5. Writing ν5 for the 5-adic
  valuation, the divisor count satisfies
      ω(Φ_{4p}(2)) = ω(L_p) + ω(M_p) − 1 + [ν5(L_p) ≥ 2 or ν5(M_p) ≥ 2].
  Hence ω(Φ_{4p}(2)) = 1 iff both halves are prime powers (with the 5-divisible
  half having ν5 = 1), and ω ≥ 2 otherwise. So "ω ≥ 2 for all large p" is
  exactly "L_p and M_p are not both prime powers", a statement of the form
     2^p ∓ 2^{(p+1)/2} + 1 = q^k
  about perfect powers in a near-power-of-2. This is attacked with the
  perfect-power/Lucas literature (Catalan–Mihailescu, Bugeaud–Mignotte–Siksek
  on perfect powers in Lucas sequences, elementary mod-8/16 and order
  arguments). The deliverable is an exact lower bound: for all p ≥ P,
  ω(Φ_{4p}(2)) ≥ 2 (and then push to ≥ 3, ≥ 4 by the same method), which is a
  genuine, exactly-stated partial result on the H2 side of the branch — and
  each increment is one step toward the C·log p target without any search.
  This is distinct from the quartic-reciprocity route and from the congruence
  route: it is a Diophantine/composite-structure argument about the two halves,
  not a character argument about the divisors.
status: proposed
first-step: Reproduce the split and the ω formula on the known small cases
  (p = 3: L=5, M=13, ω(Φ)=1; p = 5: L=25, M=41, ω(Φ)=2; p = 7: L=113,
  M=145=5·29, ω(Φ)=2) in exact integer arithmetic, then reduce the equation
  2^p ∓ 2^{(p+1)/2} + 1 = q^k modulo 8, 16 and small primes to find which
  residue classes of p (mod some modulus) force a composite factor in one half,
  i.e. prove ω ≥ 2 on an explicit infinite set of primes p.
```

Notes for research to settle: (a) whether the equivalence ω = 1 ⟺ both halves
prime powers (with the stated ν5 correction) is exact as written; (b) what is
already proved about perfect powers in 2^n ± 2^{(n+1)/2} + 1 and in Lucas
sequences V_n(5,4), so the first-step's modular sieve is not re-deriving a known
theorem; (c) the current best *proved* lower bound on ω(Φ_p(−4)) (likely ω ≥ 1
by Zsigmondy; is ω ≥ 2 anywhere in the literature for p in an infinite set?).
Falsifier: if L_p and M_p are both prime powers for infinitely many p, ω stays
at 1 and the route cannot reach H2; the small-case check of p = 3, 5 already
shows ω=1 occurs, so the claim must be "all sufficiently large p", and a
computed infinite family of prime-power pairs would kill it.
