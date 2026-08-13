# Biquadratic character of 2 over the divisors of 2^{2p}+1

```approach
idea: Re-encode the paper's "mod-16 coin flip" (Conjecture 29) as the
  biquadratic (quartic) residue character (2/r)_4 of 2 modulo the primitive
  prime divisors r of 2^{2p}+1, and attack it with Gauss's quartic reciprocity
  in Z[i] and the Aurifeuillean split.
mechanism: For a primitive divisor r of Φ_{4p}(2) one has ord_r(2) = 4p. A
  generator argument gives the exact equivalence
    2 is a fourth power mod r  ⟺  4 | (r−1)/4p  ⟺  16p | r−1  ⟺  v2(r−1) ≥ 4
  (writing 2 = g^j, ord = 4p forces gcd(j, r−1) = (r−1)/4p =: t and j/t odd
  coprime to 4p, so 4 | j ⟺ 4 | t). But v2(r−1) ≤ 3 is exactly the 2-adic part
  of the 3-Higgs condition, so "r ≡ 1 mod 16" ⟺ "r is NOT 3-Higgs". Conjecture
  29 ("some divisor of Φ_{4p}(2) is ≡ 1 mod 16") is therefore exactly: the
  quartic symbol (2/r)_4 equals 1 for at least one primitive divisor r.

  The synthesis: 2^{2p}+1 = (2^p + i)(2^p − i) in Z[i]. For a prime r ≡ 1
  (mod 4) dividing 2^{2p}+1, its Gaussian prime factor π | (2^p + i) determines
  the quartic character (2/π)_4, and by quartic reciprocity this is computable
  from the factorization of 2^p + i. The Aurifeuillean split 2^{2p}+1 = L_p·M_p
  separates the integer prime factors into two classes. The conjecture is that
  for sufficiently large p, at least one prime factor of one half has
  (2/r)_4 = 1 — i.e. is ≡ 1 (mod 16) — and for a congruence class of p mod 8
  this may be provable by algebraic factorization in Z[i] rather than by
  density. This is the "algebraic factorization" route the paper names as its
  own next step (§6).

  This is not the closed search, not the product-form backtrack, and not
  thinness/Chebotarev: it is a named algebraic invariant (quartic reciprocity)
  applied to a single fixed cyclotomic value, operating at the divisor level
  where the paper says the missing theorem lives.
status: adopted
first-step: Compute the Gaussian factorization of 2^p + i for the small primes
  p = 3, 5, 7, 11, 13 in Z[i] (via PARI/GP or sympy's factorint over Gaussian
  integers) and tabulate the quartic character (2/π)_4 of each Gaussian prime
  factor against (a) p mod 8 and (b) which Aurifeuillean half L_p or M_p the
  norm falls into. This establishes the empirical quartic-character distribution
  on the known cases. Then prove: for p ≡ 3 (mod 8), L_p ≡ 1 (mod 4) and the
  Gaussian primes above L_p carry a predictable quartic character determined by
  the Legendre symbol (2/p) and the factorization of p in Z[i]. The theorem
  sought is: for p in some congruence class mod 8, one of L_p, M_p necessarily
  has a prime factor r with (2/r)_4 = 1 — i.e. r ≡ 1 (mod 16) — proving
  Conjecture 29 for that infinite class.
```

## Why this beat the others

| Candidate | Status | Reason |
| --- | --- | --- |
| `biquadratic-character-divisors` | **adopted** | Directly attacks Conjecture 29 — the paper's own recommended target for (H1) — with named algebraic machinery (quartic reciprocity in Z[i]), operating at the divisor level where the paper says the missing theorem lives. No GRH, no Chebotarev, no density. The Aurifeuillean split is catalogued; the BHV primitive divisor theorem is catalogued; the generator equivalence (2/r)_4 = 1 ⟺ r ≡ 1 mod 16 is elementary. The gap is applying quartic reciprocity to the Gaussian factor 2^p + i, which nobody has done in this context. |
| `aurifeuillean-perfect-power` | refuted | The ω-formula decomposition is correct but the deliverable (ω ≥ 2) is too weak to matter. The paper needs ω ≥ C log p (H2) or at least unbounded growth. ω ≥ 2 only rules out p = 3. Iterating the same method to reach ω ≥ 3, 4, … would require solving harder Diophantine equations at each step, and the Bugeaud–Mignotte–Siksek machinery for perfect powers in Lucas sequences may not cover numbers of the form 2^p ∓ 2^{(p+1)/2} + 1. Killed by: deliverable gap to H2 is unbridgeable by iteration. |
| `three-divisibility-mod-3` | refuted | The odd-a observation (3 ∤ 2^a+1 for odd a) is correct but Subbarao–Warren 1966 already classified a = 1 → {6, 90} and excluded a = 3, 5, 7 — so the odd-a case is essentially covered. The even-a mod-3 parity relation constrains a hypothetical 3∤n counterexample but provides no mechanism to eliminate the even-a branch; Frei's bound (a ≥ 144) is not held in the library's primary sources and the parity relation plus budget does not force a contradiction. Killed by: the even-a constraint does not eliminate the branch, so "3 ∤ n forced" is not delivered. |