# Biquadratic character of 2 over the divisors of 2^{2p}+1

```approach
idea: Re-encode the paper's "mod-16 coin flip" (Conjecture 29) as the
  biquadratic (quartic) residue character (2/r)_4 of 2 modulo the primitive
  prime divisors r of 2^{2p}+1, and attack it with Gauss's quartic reciprocity
  in Z[i] and the Aurifeuillean split over Q(√2).
mechanism: For a primitive divisor r of Φ_{4p}(2) one has ord_r(2) = 4p. A
  generator argument gives the exact equivalence
    2 is a fourth power mod r  ⟺  4 | (r−1)/4p  ⟺  16p | r−1  ⟺  v2(r−1) ≥ 4
  (writing 2 = g^j, ord = 4p forces gcd(j, r−1) = (r−1)/4p =: t and j/t odd
  coprime to 4p, so 4 | j ⟺ 4 | t). But v2(r−1) ≤ 3 is exactly the 2-adic part
  of the 3-Higgs condition, so "r ≡ 1 mod 16" ⟺ "r is NOT 3-Higgs". Conjecture
  29 ("some divisor of Φ_{4p}(2) is ≡ 1 mod 16") is therefore exactly: the
  quartic symbol (2/r)_4 equals 1 for at least one primitive divisor r. This is
  an exact (not GRH/Chebotarev) question: Gauss's criterion says 2 is a
  biquadratic residue mod r = a²+b² (a odd, b even) iff r = a²+64b², i.e.
  (2/r)_4 = 1, and quartic reciprocity in Z[i] computes (2/π)_4 from the
  Gaussian prime π above r. The prime divisors r come from the Gaussian
  factorization of 2^p + i (norm 2^{2p}+1), which is exactly the Aurifeuillean
  split 2^{2p}+1 = L_p·M_p with L_p, M_p = 2u² ∓ 2u + 1 at u = 2^{(p−1)/2}
  (2u ∓ 1 is a square root of −1 mod r). So the mod-16 distribution is a
  reciprocity statement about the two halves, and for a congruence class of p
  mod 8 one may be able to *prove* (by an algebraic factorization, not by
  density) that one half carries a divisor with (2/r)_4 = 1 — precisely the
  "algebraic factorization" route the paper lists as its own next step. This is
  not the closed search, not the product-form backtrack, and not thinness: it
  is a named algebraic invariant (quartic reciprocity) applied to a single
  fixed cyclotomic value.
status: proposed
first-step: Recompute v2(q−1) (equivalently q mod 16, equivalently (2/q)_4)
  for every known prime divisor q of L_p and M_p across the paper's open
  candidates, tabulated against p mod 8 and against which factor (L or M) the
  divisor divides. Test the conjecture that q mod 8 is a function of
  (p mod 8, L-vs-M). If it is, apply quartic reciprocity to upgrade the
  observed function to a theorem and hunt a residue class of p where
  q ≡ 1 mod 16 is forced. This is structure-checking compute over the paper's
  own factor cache, not enumeration of n.
```

Notes for research to settle: (a) the exact form of Gauss's biquadratic
criterion (whether `(2/r)_4 = 1 ⟺ r = a²+64b²` and the condition in terms of
`r mod 16` alone vs the representation); (b) the Aurifeuillean factorization
theorem (Schur 1925 / Lucas) stating the residue-class behaviour of prime
divisors of the two factors; (c) whether any literature already proved the
mod-16 equidistribution Conjecture 29, or a special case of it, via quartic
reciprocity. The falsifier: if the tabulation shows no dependence of q mod 8 on
(p mod 8, L-vs-M), the reciprocity route has no handle and the proposal dies.
