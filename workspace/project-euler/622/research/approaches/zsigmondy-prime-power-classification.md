# Zsigmondy primitive-prime-divisor classification

A route to the Lean-checked answer that never touches inclusion-exclusion over
divisors. It classifies the set {m : ord_m(2)=60} directly by prime-power
structure, then sums the classification.

```approach
idea: Zsigmondy's theorem (primitive prime divisor of a^n−b^n) plus the
  Wieferich lift ord_{p^a}(2)=ord_p(2)·p^{a−1}, used to classify every m with
  ord_m(2)=60 by its prime-power decomposition.
mechanism: The primes p | 2^60−1 partition by their order: {p : ord_p(2)=d}
  over d|60, and these are exactly the primitive prime divisors of Φ_d(2).
  Zsigmondy certifies each class is nonempty for d|60, d≠1 (with the sole
  exception d=6, where 2^6−1=63=3^2·7 and both primes have orders 2,3 — but
  60 needs a factor of 4,3,5 in the lcm anyway, supplied by d=4,3,5, so the
  missing order-6 class is irrelevant). For p with ord_p(2)=d, the Wieferich
  lift (claim wieferich-lift-order: none of the 11 primes divides 2^d−1 twice,
  all checked at p≤1321) gives ord_{p^a}(2)=d·p^{a−1} for every a. Hence
    ord_m(2) = lcm over p^a||m of d_p·p^{a−1} = 60,
  a purely local combinatorial condition over the 11 primes of 2^60−1 with
  exponents ≤2. The set {m} and its sum S(60) then factor per prime (Euler
  factors) subject to the single lcm=60 constraint, giving a certificate
  different from the σ/τ inclusion-exclusion table: an explicit classification
  of the 4456 moduli and a multiplicative formula for S(60).
status: refuted
precedent: "Zsigmondy's theorem: for coprime a>b and n>=2, a^n-b^n has a
  primitive prime divisor except (a,b,n)=(2,1,6) and n=2 with a+b a power of 2.
  For a=2,b=1 the sole exception is n=6. (Avci, arXiv:2011.06136,
  https://arxiv.org/pdf/2011.06136, downloaded; Cambridge conjugacy-classes
  paper Thm 2.4, https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/prime-divisors-and-the-number-of-conjugacy-classes-of-finite-groups/79A16F6CD21CA87BDF4B5E578387FC1F;
  Schinzel, Proc. Camb. Phil. Soc.,
  https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/on-primitive-prime-factors-of-anbn/FF4F8CB4D5BEDD2854151670559F36C6.)
  Order-lift: ord_{p^e}(2)=p^{e-e0}ord_p(2) (Kiriu-Mejia arXiv:2201.02751).
  Library claims order-lcm-over-prime-powers (Naor Thm 6.1.32 + Chappelon Prop
  5), wieferich-lift-order (Packard Cor 4.2, Chappelon Thm 3.6) — both proved.
  Claim zsigmondy-primitive-prime-divisor filed in research/notes/
  grounding-three-approaches.md. The order-class data {3->2,5->4,7->3,11->10,
  13->12,31->5,41->20,61->60,151->15,331->30,1321->60} and v_p(2^ord-1)=1 for
  all 11 primes is machine-checked (claim pe622-answer-order-sixty; fresh check
  filed at code/pe622/research_verify.py). Hypotheses (60 != 6; m odd) hold.
killed-by: Not refuted on mathematics — the literature fully grounds it. It is
  passed over as the *adopted* line is stronger for this specific formalisation:
  (a) it needs a Cited axiom (Zsigmondy) that remains `asserted` in the claim
  ledger, giving a `conditional` verdict; (b) the Euler-factor decoupling of
  the lcm=60 sum is a derivation, not a literature result, and would have to be
  proved from scratch inside Lean; (c) the local lcm=60 condition does not give
  the closed σ/τ form — the Zsigmondy classification computes the same 4456
  moduli but with no smaller certificate than the Möbius/σ path already
  carries. Adopted `mobius-inversion-exponent-lattice` reaches the same number
  through a fully general theorem Mathlib already has (`Nat.sum_mul_moebius`),
  with a `formalised` (not `conditional`) verdict achievable. Caveat: Zsigmondy certifies class-nonemptiness, it does not
  compute the sum; the local lcm=60 condition is standard. The only untested
  step is the explicit Euler-factor decoupling write-up of S(60) — needs
  deriving, not literature.
```

Grounding: `order-lcm-over-prime-powers` (CRT lcm) and `wieferich-lift-order`
are already in the claim library and marked proved, but the `riffle-order-60`
skeleton routes to the answer through G-inclusion-exclusion instead of through
them — this line is what using them as the *main* rung looks like. The "lcm
constraint decouples cleanly" claim is the speculative part: I have not written
the Euler-factor decoupling, and it is plausible only because 60 is small (11
primes, exponents ≤2). It needs the explicit lcm=60 case split before it is
trusted.
