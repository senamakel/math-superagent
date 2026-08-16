# Schaub–Spivakovsky, *On the set of bad primes in the study of the CA conjecture* (arXiv:2307.05997; Res. Math. Sci. (2024) 11:31)

Full text: [[schaub_spivakovsky_bad-primes_2023.full]]

The resultants `/ Groebner interpretation` paper — the closest existing work to the run's stated method (commutative algebra over Z, resultants, radic ideal membership). Establishes the exact resultant structure of the CA ideal and a clean sufficient condition for a prime to be bad.

## Resultant reformulation that IS the run's target

```claim
id: resultant-reformulation
statement: With f = x^d + a_1 x^{d−1} + … + a_{d−1} x (a_d normalized to 0), and
  R_i = Res_x(f, H_i(f)) ∈ Z[a_1,…,a_{d−1}], the polynomial f is a CA-polynomial
  iff (a_1,…,a_{d−1}) ∈ V(R_1,…,R_{d−1}) ⊂ K^{d−1}. CA in degree d over char-0 K is
  equivalent to sqrt(R_1,…,R_{d−1}) = (a_1,…,a_{d−1}), i.e. a_i^N ∈ (R_1,…,R_{d−1})
  for all i and some N. Truth depends only on char K, not on K (faithfully flat extension).
hypotheses: monic degree d, a_d = 0 (translate a shared root of H_{d−1} to 0)
holds-here: yes — this is precisely the affine scheme over Z the problem statement names
status: proved (Def 1, Conj 2, Remark 2–3)
bearing: Gives the run its decision object: ideal-membership (radical membership) in
  Z[a_1,…,a_{d−1}], exact, no root-finding.
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (§1)
falsifies: A counterexample-degree where sqrt≠(a_1,…) yet CA holds — impossible by construction.
```

## Distinguished monomials in the resultants

```claim
id: resultant-monomials
statement: For each i∈{1,…,d−1}, the monomial
  (−1)^{d−i}((d choose i) − 1)^{d−i} a_{d−i}^d appears in R_i, and a_{d−i}^d are the
  ONLY pure powers appearing in any R_i. For i≥2, (−1)^{(d−1)(d−i)}(d choose i)^{d−1}
  a_{d−1}^{d−i} a_{d−i} appears in R_i and is the unique degree-(d−i+1) monomial there,
  all others having strictly larger degree. (Coefficient identity: sum_k (−1)^k
  (d−i choose k)(d choose i)^k = (−1)^{d−i}((d choose i)−1)^{d−i}.)
hypotheses: Z coefficients, ad=0
holds-here: yes
status: proved (Theorem 6, Theorem 9; the pure-power fact first proved by R. de Frutos,
  PhD thesis, Prop 2.2.1)
bearing: Lets one read off bad primes from pure powers, and constrains the Gröbner/
  Newton-polytope structure of the CA ideal — the "which monomials survive reduction"
  question the run wants to answer.
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (Thm 6, Thm 9)
falsifies: a computation of R_i for some (d,i) lacking these monomials.
```

## Sufficient criterion: a prime is bad

```claim
id: bad-prime-criterion
statement: If p is a prime with p | ((d choose i) − 1) for some i∈{1,…,d−1}, then
  CA_{d,p} is false. Reason: for such p, no pure power of any a_j appears in any
  R_j mod p, so the point e_i (i-th coordinate 1, rest 0) lies in V(R_1,…,R_{d−1}).
hypotheses: char p
holds-here: yes
status: proved (Corollary 8)
follows-from: resultant-monomials
bearing: A cheap generator of bad primes for any d — useful as a sanity filter for
  which primes the reduction-mod-p method can lift through.
anchor: research/sources/schaub_spivakovsky_bad-primes_2023.full.md (Cor 8)
falsifies: a prime p|((d,i)−1) for which CA_{d,p} nevertheless holds.
```

## What it does not settle
The list is **non-exhaustive** — there may be bad primes not of the form `p | ((d,i)−1)`. It gives no upper bound on bad primes by itself; the companion paper (upper-bound, 2411.13967) supplies that. It establishes the `sqrt = (a_1,…)` reformulation but does not prove it for any open degree.
