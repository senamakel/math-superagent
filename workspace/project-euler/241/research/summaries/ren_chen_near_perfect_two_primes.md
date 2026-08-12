# Ren & Chen — On near-perfect numbers with two distinct prime factors (Bull. Aust. Math. Soc. 2013)

**Source:** X.-Z. Ren, Y.-G. Chen, Bull. Aust. Math. Soc. 88 (2013) 520–524,
doi:10.1017/S0004972713000178 — `[[ren_chen_near_perfect_two_primes.full]]`.

## What it establishes

A positive integer n is **near-perfect** if it is the sum of all but one of its proper
divisors (missing div d = "redundant"), equivalently σ(n) = 2n + d. Following Pollack &
Shevelev (J. Number Theory 132 (2012) 3037–3046), the three families:

- **Type 1**: n = 2^{t−1}(2^t − 2^k − 1), 2^t−2^k−1 prime, redundant 2^k.
- **Type 2**: n = 2^{2p−1}(2^p − 1), p and 2p−1 prime, redundant 2^p(2^p−1).
- **Type 3**: n = 2^{p−1}(2^p−1)², p and 2p−1 prime, redundant 2^p−1.

**Theorem 1.2.** *All near-perfect numbers with two distinct prime factors are of types
1, 2 and 3, together with 40.* (40 = 2³·5, redundant divisor 10, not of any type.)

## What it means for PE 241

Near-perfect numbers satisfy σ(n) = 2n + d, i.e. **σ(n)/n = 2 + d/n — not a half-integer
with a fixed k** for all n. The hemiperfect condition σ(n)/n = (2k+1)/2 is a different,
ability-to-fix-the-ratio problem (2σ(n)=(2k+1)n is c=0, a=2 in Alekseyev's equation).
So near-perfect numbers are an **adjacent family**, not the hemiperfect set. This source is
background on the same σ-linear-equation family (the d=±1 near-perfect case of
Alekseyev's Theorem 3.1); it does **not** enumerate hemiperfects or bound the sum.

Do not re-read for the solver. The operative Alekseyev reference that covers the
σ(n)=2n+d family is `[[alekseyev_diophantine_sigma_html]]`.
