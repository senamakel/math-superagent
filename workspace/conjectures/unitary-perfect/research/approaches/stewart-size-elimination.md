```approach
idea: Stewart-type lower bound on the largest primitive divisor of Φ_{4p}(2)
  forces it to be too large to be 3-Higgs for large p, closing H_even from the
  size direction rather than the counting/density direction.
mechanism: For n = 4p with p odd, Stewart (2013, Crelle 680) proves the largest
  primitive prime divisor P_n of a^n - b^n satisfies P_n > C n log n for all
  n > n_0 with explicit constants. For (a,b)=(2,1) and n=4p, the largest prime
  r | Φ_{4p}(2) is primitive and satisfies r > C' p log p. If r is 3-Higgs,
  then (r-1)/(4p) ∈ S_3^{(≤3)} — the 3-Higgs cubefree semigroup. The elements
  of S_3^{(≤3)} up to X are all composed of primes ≤ X with specific
  multiplicative constraints. In particular, the smallest 3-Higgs primes grow
  slowly (the set is thin, Π_3(x) ~ x^{0.62...}), so a number of size
  ~ p log p formed only from 3-Higgs prime factors would require many small
  primes, each contributing at least one factor of 4p to r-1. The tension:
  r-1 = 4p·k where k ∈ S_3^{(≤3)} and r ≫ p log p. If we can bound the maximal
  element of S_3^{(≤3)} that can be formed from 3-Higgs primes smaller than
  some function of p, we get an upper bound on r that contradicts the Stewart
  lower bound. This is a size gap (not the log-mass/reciprocal-mass counting
  gap the paper identifies), and it uses the actual magnitude of the primitive
  divisor, which Stewart-type results control directly.
status: refuted
killed-by: The 3-Higgs semigroup S_3^{(≤3)} is infinite and contains arbitrarily
  large elements — it is thin (Π_3(x) ~ x^{0.62}) but not bounded. The Stewart
  bound gives r ≫ p log p, so k = (r-1)/(4p) ≫ (C/4) log p. But k only needs to
  be ~ log p in size, which is well within the range where S_3^{(≤3)} has
  abundant elements. There is no "maximal element" contradiction: thinness at
  scale X means few elements up to X, not that no large elements exist. The
  category error is confusing thinness (density → 0) with boundedness (finite
  support). The paper already proves #{m ≤ X : m ∈ H} ≪ X^{1-η} (Theorem 21)
  — that is thinness — and explicitly states this does not imply finiteness.
  A size bound on the largest primitive divisor does not change the logic: the
  gap is between log-mass (~2p log 2) and reciprocal mass (~1/p), and a single
  large r does not bridge it.
first-step: Retrieve the exact Stewart (2013) bound for 2^n - 1 with explicit
  constants C and n_0; compute the growth function of the 3-Higgs cubefree
  semigroup S_3^{(≤3)} (maximal element ≤ X composed of 3-Higgs primes with
  exponents ≤ 3); state the inequality that would close H_even and test whether
  the constants cross for realistic p.
```