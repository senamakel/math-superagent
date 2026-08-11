> **Excerpt only — read this first.** The complete text is beside it at `research/cambie_yan_html.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://ar5iv.labs.arxiv.org/html/2408.01211 | converted from HTML -->

[2408.01211] Descents and inversions in powers of permutations

# Descents and inversions in powers of permutations

Stijn Cambie Department of Computer Science, KU Leuven Campus Kulak-Kortrijk, 8500 Kortrijk, Belgium. Supported by a postdoctoral fellowship by the Research Foundation Flanders (FWO) with grant number 1225224N. Email: stijn.cambie@hotmail.com. Jun Yan Mathematics Institute, University of Warwick, UK. Email: jun.yan@warwick.ac.uk. Supported by the Warwick Mathematics Institute CDT and funding from the UK EPSRC (Grant number: EP/W523793/1).

###### Abstract

In this paper, we generalise several recent results by Archer and Geary on descents in powers of permutations, and confirm all their conjectures. Specifically, for all k ∈ ℤ + 𝑘 superscript ℤ k\in\mathbb{Z}^{+}, we prove explicit formulas for the expected numbers of descents and inversions in the k 𝑘 k -th powers of permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} for all n ≥ 2 ​ k + 1 𝑛 2 𝑘 1 n\geq 2k+1. We also compute the number of Grassmanian permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} whose k 𝑘 k -th powers remain Grassmanian, and the number of permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} whose k 𝑘 k -th powers have the maximum number of descents.

## 1 Introduction

Given a permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n}, a descent in π 𝜋 \pi is an index i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1] satisfying π ​ ( i) > π ​ ( i + 1) 𝜋 𝑖 𝜋 𝑖 1 \pi(i)>\pi(i+1), while an inversion in π 𝜋 \pi is a pair i < j 𝑖 𝑗 i<j of indices in [n] delimited-[] 𝑛 [n] satisfying π ​ ( i) > π ​ ( j) 𝜋 𝑖 𝜋 𝑗 \pi(i)>\pi(j). The number of descents and the number of inversions in π 𝜋 \pi are denoted by des ⁡ ( π) des 𝜋 \operatorname{des}(\pi) and inv ⁡ ( π) inv 𝜋 \operatorname{inv}(\pi), respectively.

It is easy to show that the expected number of descents in a random permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} is n − 1 2 𝑛 1 2 \frac{n-1}{2}, as for each i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1], the events π ​ ( i) > π ​ ( i + 1) 𝜋 𝑖 𝜋 𝑖 1 \pi(i)>\pi(i+1) and π ​ ( i) < π ​ ( i + 1) 𝜋 𝑖 𝜋 𝑖 1 \pi(i)<\pi(i+1) are equally likely. A similar argument shows that the expected number of inversions in a permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} is n ​ ( n − 1) 4 𝑛 𝑛 1 4 \frac{n(n-1)}{4}.

Recently, in [1], while studying the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} whose square, or whose cube, have a fixed small number of descents, Archer and Geary conjectured that for all but the first few values of n 𝑛 n, the expected number of descents in π 2 superscript 𝜋 2 \pi^{2} and in π 3 superscript 𝜋 3 \pi^{3} for π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} are both n − 1 2 − 2 n 𝑛 1 2 2 𝑛 \frac{n-1}{2}-\frac{2}{n}.

In this paper, we confirm this conjecture. Moreover, we prove explicit formulas for the expected numbers of descents and inversions in the k 𝑘 k -th powers of permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} for all k ∈ ℤ + 𝑘 superscript ℤ k\in\mathbb{Z}^{+} and n ≥ 2 ​ k + 1 𝑛 2 𝑘 1 n\geq 2k+1.

These formulas will be expressed in terms of several divisor functions. Recall that for k ∈ ℤ + 𝑘 superscript ℤ k\in\mathbb{Z}^{+}, τ ​ ( k) 𝜏 𝑘 \tau(k) denotes the number of divisors of k 𝑘 k and σ ​ ( k) = ∑ d ∣ k d 𝜎 𝑘 subscript conditional 𝑑 𝑘 𝑑 \sigma(k)=\sum_{d\mid k}d denotes the sum of the divisors of k 𝑘 k. Let ν 2 ​ ( k) subscript 𝜈 2 𝑘 \nu_{2}(k) be the 2 2 2 -adic valuation of k 𝑘 k, i.e., the number of prime factors 2 2 2 in the prime factorization of k 𝑘 k. Define τ o ​ ( k) = τ ​ ( k / 2 ν 2 ​ ( k)) subscript 𝜏 o 𝑘 𝜏 𝑘 superscript 2 subscript 𝜈 2 𝑘 \tau_{\text{o}}(k)=\tau\left(k/2^{\nu_{2}(k)}\right) to be the number of odd divisors of k 𝑘 k. We will show that

###### Theorem 1.1.


*[excerpt ends; 67357 characters not shown — see `research/cambie_yan_html.full.md`]*
