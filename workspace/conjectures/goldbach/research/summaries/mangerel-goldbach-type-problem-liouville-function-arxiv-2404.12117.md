# Mangerel (2024), Liouville Goldbach-type convolution
[[mangerel-goldbach-type-problem-liouville-function-arxiv-2404.12117.full]]

Source: https://arxiv.org/abs/2404.12117 (v2, 2 May 2024).

```claim
id: mangerel-liouville-convolution-bound
statement: For all sufficiently large N, |Σ_{1≤n<N} λ(n)λ(N−n)| < N−1, where λ is the Liouville function.
hypotheses: N sufficiently large.
holds-here: yes
status: asserted
bearing: An analogue for the Liouville function of the Goldbach convolution: it shows the λ-version of Goldbach is "almost always" true in a strong quantitative sense, but it is about the multiplicative sign pattern of a convolution, not about the presence of primes. It answers (essentially) a 2018 AIM workshop question on Sarnak's conjecture, and does not transfer to a statement about prime sums.
anchor: research/sources/mangerel-goldbach-type-problem-liouville-function-arxiv-2404.12117.full.md
```

This is the unconditional counterpart in a line of results that requires GRH in related work; no direct implication for binary Goldbach.

```claim
id: mangerel-shusterman-sign-patterns
statement: Assuming GRH for Dirichlet L-functions, for every sufficiently large even integer N there are a,b≥1 with a+b=N and λ(a)=λ(b)=−1; moreover for every sign pattern (η1,η2)∈{−1,1}² and every prime N≥N0, |{n<N : (λ(n),λ(N−n))=(η1,η2)}| ≫ N exp(−C(log log N)^6).
hypotheses: GRH; N sufficiently large (even for the first statement; prime for the second).
holds-here: yes
status: asserted
bearing: A GRH-conditional analogue of binary Goldbach for the Liouville function; the proof uses Pierce expansions of rationals n/N. Shows the parity/sign structure of a Goldbach-type convolution is fully flexible under GRH, but again is a statement about λ-signs, not primes.
anchor: research/sources/mangerel-shusterman-goldbach-sign-patterns-liouville-arxiv-2412.17199.full.md
```