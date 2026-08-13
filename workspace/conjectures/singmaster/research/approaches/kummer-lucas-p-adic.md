```approach
idea: Kummer–Lucas p-adic constraints on multiple binomial-coefficient representations of the same integer — a combinatorial/number-theoretic line that uses base-p digit structure rather than algebraic geometry.

mechanism: Kummer's theorem (1852): v_p(C(n,k)) = the number of carries when adding k and n−k in base p. Lucas' theorem (1878): C(n,k) ≡ ∏_{i} C(n_i, k_i) (mod p) where n_i, k_i are base-p digits. If C(n,k) = C(m,l) = a with N(a) large, then for every prime p, all the representing pairs must produce the SAME carry-count (hence same v_p) and the SAME Lucas product mod p. This is an extremely strong constraint on the simultaneous base-p digit structures of all the n's. In particular, if N(a) ≥ 8 (as with 3003), the digit patterns for p=2,3,5,7,... must interlock across (3003,1), (78,2), (15,5), (14,6) simultaneously. The conjecture would follow if one could prove that for any given prime p, the number of (n,k) pairs with the same v_p(C(n,k)) and same Lucas residue grows at most logarithmically in the size of the numbers — and then intersect over enough primes to reduce the count to O(1). This is genuinely different from the algebraic-geometry (Faltings/Siegel) and analytic (MRSTT exponential-sum) lines because it works prime-by-prime in the combinatorial structure of the triangle rather than treating C(n,k) as a polynomial or analytic function.

status: refuted
killed-by: kummer-lucas-class-not-logarithmic — the proposed core lemma is unconditionally false. For p=2, every entry of row n=2^m−1 is odd and ≡1 (mod 2) with v_2=0 (all m binary digits of 2^m−1 are 1; Lucas rowwise product C(1,k_i)≡1), so the single p-adic class (v_2=0, residue 1) contains all 2^m pairs (2^m−1,k), k=0..2^m−1 — exponential in the bit-length, not logarithmic. Same for generic p via row n=(p^a-1)/(p-1) congruence-to-1 results (Lucas's theorem / generalized Lucas; MDPI 2020 generalization: a row is all ≡1 (mod p^e) iff n=(p^e m -1)/(p^e-1)). Hence fixed p-adic classes are large/infinite and no finite intersection of prime-class constraints bounds N(a). Per-prime local information does not control how many globally-distinct (n,k) land on one integer — the same structural wall as Faltings/Siegel.
precedent:
  https://www.mdpi.com/2073-8994/12/2/288  (generalized Lucas: row n all ≡1 mod p^e iff n=(p^e m-1)/(p^e-1); special case n=2^m-1 all odd — confirms the refutation)
  https://arxiv.org/abs/1001.1783 (Rowland, nonzero binomial coefficients mod p^α — Kummer/Lucas base-p digit structure)
  https://doi.org/10.48550/arxiv.0812.3089 (Sun & Zhang, binomial coefficients and the p-adic integral ring — p-adic density, not level-set bounds)
  claim: kummer-lucas-class-not-logarithmic
first-step: none — the mechanism's engine is false; do not re-propose.
```
