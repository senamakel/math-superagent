# Courtois–Bard–Ault: Statistics of Random Permutations & Periodic Block Ciphers

Courtois, N.T., Bard, G.V., Ault, S.V. arXiv:0905.3682 [math.CO]; published
Cryptologia 36 (2012) 240–262. Source: https://arxiv.org/abs/0905.3682 ; full text:
[[../../L0.3/courtois_bard_ault_ppowers_body.full.md]] (ar5iv HTML).

## What it establishes — cycle structure of POWERS π^k (the key mechanism)

Uses analytic combinatorics (Weak/Strong Cycle Structure Theorem: the class of
permutations with cycles of lengths in A, cyclistically reordered, has EGF
exp(Σ_{i∈A} z^i/i); derivatives of double EGFs give expected values). New here
vs. the rest of the library is a rigorous treatment of *iterates* π^k:

- **Fixed points of a power (Thm 3.11 / Cor 3.13):** x is a fixed point of π^k
  iff x lies in a π-cycle of length i dividing k. So the fixed points of π^k are
  exactly the points in π-cycles whose length ∈ divisors(k).
- **Expected number of fixed points of π^k (Thm 3.14):** = τ(k), the number of
  positive divisors of k, in the n→∞ limit — a divisor-function statement about
  powers, complementing Nathanson's cycle-count↔fixed-points-of-powers Möbius
  identity.
- **Cycle splitting under powers (worked example §3.1):** an odd cycle stays one
  cycle, an even cycle (length 2c) splits into two cycles (odds/evens); general
  splitting: raising to k-th power replaces a cycle of length i by
  gcd(i,k) cycles each of length i/gcd(i,k). The fixed points of the k-th power
  come exactly from the divisor-length cycles.
- **Fixed-point-count distribution of π^k (Thm 5.1):** probability-generating
  EGF for #fixed(π^k) is exp(Σ_{i|k} (y^i − 1)/i). Specializes (App A): derivation
  probability of π^k is e^{−σ(k)/k} (σ = sum-of-divisors).
- Paper's applications (number of fixed points of a ~10^6-fold iterate of a
  random permutation; τ(10^6)=49, highly-composite exponents maximize fixed
  points) are cryptanalytic, not relevant to Q(n) directly.

## What it implies for THIS run

The run's core (memory.md) is f_n(k) = #{(π,i): (π^i)(k) < (π^i)(0)} = A_n + (k−1)B_n
and the reduction Q(n)=(n!)²+A_n(n!−1)+(B_n/2)T(n); the missing piece is closed
forms for A_n, B_n, which come from summing the pair-inversion probability of the
random power σ=π^i over cycle types. The random power's distribution is governed
by exactly this cycle-splitting/divisor-of-exponent structure: whether two points
of σ are fixed, or swapped, or fall in a given relative order depends on the
gcd/lcm of their π-cycle lengths and the divisibility of the exponent. This paper
supplies the *power-side* cycle-splitting facts (a cycle of length i contributes
gcd(i,k) cycles to π^k; fixed points come from divisor-length cycles) that the
conjugacy-class/Ewens sources treat only for the base permutation π. It is a
mechanism source for the open A_n,B_n, NOT a computation of Q(n).

## Caveat
Fixed-point/cycle structure of the power π^k only; does not give the Lehmer/rank
sum over the cyclic subgroup {π^i} — that remains the genuinely open core,
unsolved by every source located.
