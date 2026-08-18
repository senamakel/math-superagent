# Akeno (2026), level of distribution of Goldbach primes
[[akeno-level-of-distribution-goldbach-primes-arxiv-2606.29559.full]]

Source: https://arxiv.org/abs/2606.29559 (v1, 28 Jun 2026).

```claim
id: akeno-2026-level-1-over-6
statement: For almost all even N>0, the Goldbach primes P∩(N−P) have level of distribution 1/6. Applications: for almost all even N, N=p1+p2 with p1−p2+1∈P4; for almost all N with 6|N, N=p1+p2 with 2p1p2+1∈P13.
hypotheses: N even, N large; P_k = integers with at most k prime factors.
holds-here: yes
status: asserted
bearing: A level-of-distribution statement for the Goldbach primes themselves: the set of representations p1+p2=N is equidistributed in APs up to modulus N^(1/6) for almost all N. It yields restricted-class corollaries (p1−p2+1∈P4, 2p1p2+1∈P13) for almost all N. An almost-all statement, not an every-n theorem; the 1/6 level is the natural barrier for this method (per the paper's framing).
anchor: research/sources/akeno-level-of-distribution-goldbach-primes-arxiv-2606.29559.full.md
```

This paper comes with computable constants (ancillary C code computes M_k values), which is unusual and useful: the auxiliary constant computations are supplied. It is the level-of-distribution companion to Akeno's small-gaps paper.