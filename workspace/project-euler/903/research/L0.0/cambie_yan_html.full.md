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

For k ∈ ℤ + 𝑘 superscript ℤ k\in\mathbb{Z}^{+} and n ≥ 2 ​ k + 1 𝑛 2 𝑘 1 n\geq 2k+1, the expected number of descents in the k 𝑘 k -th powers of permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} is

 | 1 n! ​ ∑ π ∈ 𝒮 n des ⁡ ( π k) = n − 1 2 − τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k) 2 ​ n. 1 𝑛 subscript 𝜋 subscript 𝒮 𝑛 des superscript 𝜋 𝑘 𝑛 1 2 superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 2 𝑛 \frac{1}{n!}\sum_{\pi\in\mathcal{S}_{n}}\operatorname{des}(\pi^{k})=\frac{n-1}{2}-\frac{\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k)}{2n}. |  |

###### Theorem 1.2.

For k ∈ ℤ + 𝑘 superscript ℤ k\in\mathbb{Z}^{+} and n ≥ 2 ​ k + 1 𝑛 2 𝑘 1 n\geq 2k+1, the expected number of inversions in the k 𝑘 k -th powers of permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} is

 | 1 n! ​ ∑ π ∈ 𝒮 n inv ⁡ ( π k) = n ​ ( n − 1) 4 − ( τ ​ ( k) − 1) ​ n 6 − τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k) 12. 1 𝑛 subscript 𝜋 subscript 𝒮 𝑛 inv superscript 𝜋 𝑘 𝑛 𝑛 1 4 𝜏 𝑘 1 𝑛 6 superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 12 \frac{1}{n!}\sum_{\pi\in\mathcal{S}_{n}}\operatorname{inv}(\pi^{k})=\frac{n(n-1)}{4}-\frac{(\tau(k)-1)n}{6}-\frac{\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k)}{12}. |  |

In Section 2, we first prove a few lemmas that count for all pairs ( i, j) 𝑖 𝑗 (i,j) and ( x, y) 𝑥 𝑦 (x,y), the number of π 𝜋 \pi such that π k superscript 𝜋 𝑘 \pi^{k} sends ( i, j) 𝑖 𝑗 (i,j) to ( x, y) 𝑥 𝑦 (x,y). These lemmas are then used to prove our main results that determine the expected number of descents ( Theorem 1.1) and inversions ( Theorem 1.2) in π k superscript 𝜋 𝑘 \pi^{k} over all π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n}. Note that setting k = 2 𝑘 2 k=2 or k = 3 𝑘 3 k=3 in Theorem 1.1 yield the same expectation of n − 1 2 − 2 n 𝑛 1 2 2 𝑛 \frac{n-1}{2}-\frac{2}{n}, which confirms [1, Conj. 6.1].

In Section 3, we consider Grassmanian permutations, which are permutations π 𝜋 \pi with des ⁡ ( π) ≤ 1 des 𝜋 1 \operatorname{des}(\pi)\leq 1. Specifically, we compute the number of Grassmanian permutations whose k 𝑘 k -th power is also Grassmanian. By [1, Lem. 2.2], it is sufficient to determine the number of such permutations satisfying π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1 and π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n, as those with π ​ ( 1) = 1 𝜋 1 1 \pi(1)=1 or π ​ ( n) = n 𝜋 𝑛 𝑛 \pi(n)=n can be counted recursively. The following result shows that any such permutation π 𝜋 \pi is either a cyclic shift or satisfies π k = id superscript 𝜋 𝑘 id \pi^{k}=\text{id} or π k − 1 = id superscript 𝜋 𝑘 1 id \pi^{k-1}=\text{id}.

###### Theorem 1.3.

Let k ≥ 3 𝑘 3 k\geq 3. If a Grassmanian permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfies π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1, π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n and des ⁡ ( π k) = 1 des superscript 𝜋 𝑘 1 \operatorname{des}({\pi^{k}})=1, then either

- •

there exists some s ∈ [n] 𝑠 delimited-[] 𝑛 s\in[n] such that π ​ ( i) ≡ i + s ( mod n) 𝜋 𝑖 annotated 𝑖 𝑠 pmod 𝑛 \pi(i)\equiv i+s\pmod{n} for all i ∈ [n] 𝑖 delimited-[] 𝑛 i\in[n], or

- •

π 𝜋 \pi is a ( k − 1) 𝑘 1 (k-1) -th root of the identity permutation, i.e., π k − 1 = id superscript 𝜋 𝑘 1 id \pi^{k-1}=\text{id}.

Since the only Grassmanian with π ​ ( 1) ≠ 1, π ​ ( n) ≠ n formulae-sequence 𝜋 1 1 𝜋 𝑛 𝑛 \pi(1)\not=1,\pi(n)\not=n and π 2 = id superscript 𝜋 2 id \pi^{2}=\text{id} is a cyclic shift permutation (see [1, Thm. 2.3]), the k = 3 𝑘 3 k=3 case of Theorem 1.3 confirms [1, Conj. 3.2]. As cyclic shifts are easy to handle, the problem reduces to the following result enumerating Grassmanian permutations that are k 𝑘 k -th roots of the identity permutation. The case when k 𝑘 k is prime gives a nice formula.

###### Theorem 1.4.

For every k ≥ 2 𝑘 2 k\geq 2, let 𝒟 k subscript 𝒟 𝑘 \mathcal{D}_{k} be the set of divisors of k 𝑘 k excluding 1, and let

 | N k = 1 k ​ ∑ d ∣ k, d ≠ k μ ​ ( d) ​ ( 2 k d − 2). subscript 𝑁 𝑘 1 𝑘 subscript conditional 𝑑 𝑘 𝑑 𝑘 𝜇 𝑑 superscript 2 𝑘 𝑑 2 N_{k}=\frac{1}{k}\sum_{d\mid k,d\not=k}\mu(d)(2^{\frac{k}{d}}-2). |  |

Then the number of Grassmanian permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} with π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1, π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n and π k = id superscript 𝜋 𝑘 id \pi^{k}=\text{id} is equal to the number of solutions in non-negative integers of the linear equation

 | ∑ d ∈ 𝒟 k d ⋅ ∑ i = 1 N d x d, i = n. subscript 𝑑 subscript 𝒟 𝑘 ⋅ 𝑑 superscript subscript 𝑖 1 subscript 𝑁 𝑑 subscript 𝑥 𝑑 𝑖 𝑛 \sum_{d\in\mathcal{D}_{k}}d\cdot\sum_{i=1}^{N_{d}}x_{d,i}=n. |  | (1) |

In particular, for a prime p ≥ 2 𝑝 2 p\geq 2, N p = 1 p ​ ( 2 p − 2) subscript 𝑁 𝑝 1 𝑝 superscript 2 𝑝 2 N_{p}=\frac{1}{p}(2^{p}-2) and the number of Grassmanian permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} with π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1, π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n and π p = id superscript 𝜋 𝑝 id \pi^{p}=\text{id} is ( n p + N p − 1 N p − 1) binomial 𝑛 𝑝 subscript 𝑁 𝑝 1 subscript 𝑁 𝑝 1 \binom{\frac{n}{p}+N_{p}-1}{N_{p}-1} if p ∣ n conditional 𝑝 𝑛 p\mid n, and 0 otherwise.

Finally, we provide a short answer to [1, Ques. 5.3], which asks for the number of permutations whose k 𝑘 k -th powers have the maximum number of descents, or equivalently are equal to the decreasing permutation. By doing this for any positive integer k, 𝑘 k, this generalizes [1, Thm. 5.1, 5.2]. Let d 1, d 2, …, d r subscript 𝑑 1 subscript 𝑑 2 … subscript 𝑑 𝑟 d_{1},d_{2},\ldots,d_{r} be the divisors of k 𝑘 k with the same 2 2 2 -adic valuation as k 𝑘 k. Define

 | S k ​ ( n) = { ( a 1, …, a r) ∣ a i ∈ ℕ, ​ ∑ i = 1 r a i ​ d i = ⌊ n 2 ⌋ }. subscript 𝑆 𝑘 𝑛 conditional-set subscript 𝑎 1 … subscript 𝑎 𝑟 formulae-sequence subscript 𝑎 𝑖 ℕ superscript subscript 𝑖 1 𝑟 subscript 𝑎 𝑖 subscript 𝑑 𝑖 𝑛 2 S_{k}(n)=\left\{(a_{1},...,a_{r})\mid a_{i}\in\mathbb{N},\mbox{ }\sum_{i=1}^{r}a_{i}d_{i}=\mathopen{}\left\lfloor\frac{n}{2}\right\rfloor\mathclose{}\right\}. |  |

###### Theorem 1.5.

The number of π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} such that π k superscript 𝜋 𝑘 \pi^{k} is the decreasing permutation is

 | ∑ ( a 1, …, a r) ∈ S k ​ ( n) ⌊ n 2 ⌋! ⋅ ∏ i = 1 r 2 a i ​ ( d i − 1) ∏ i = 1 r a i! ​ d i a i subscript subscript 𝑎 1 … subscript 𝑎 𝑟 subscript 𝑆 𝑘 𝑛 ⋅ 𝑛 2 superscript subscript product 𝑖 1 𝑟 superscript 2 subscript 𝑎 𝑖 subscript 𝑑 𝑖 1 superscript subscript product 𝑖 1 𝑟 subscript 𝑎 𝑖 superscript subscript 𝑑 𝑖 subscript 𝑎 𝑖 \sum_{(a_{1},...,a_{r})\in S_{k}(n)}\frac{\mathopen{}\left\lfloor\frac{n}{2}\right\rfloor\mathclose{}!\cdot\prod_{i=1}^{r}2^{a_{i}(d_{i}-1)}}{\prod_{i=1}^{r}a_{i}!d_{i}^{a_{i}}} |  |

###### Proof.

Since π k superscript 𝜋 𝑘 \pi^{k} is the decreasing permutation and π 2 ​ k superscript 𝜋 2 𝑘 \pi^{2k} is the identity, the only possible fixed point of π 𝜋 \pi is ⌈ n 2 ⌉ 𝑛 2 \mathopen{}\left\lceil\frac{n}{2}\right\rceil\mathclose{} when n 𝑛 n is odd. Also, if a cycle in the cycle decomposition of π 𝜋 \pi has length ℓ ≥ 2 ℓ 2 \ell\geq 2, then we must have ℓ ∣ 2 ​ k conditional ℓ 2 𝑘 \ell\mid 2k and ℓ ∤ k not-divides ℓ 𝑘 \ell\nmid k. This implies that ⌈ n 2 ⌉ 𝑛 2 \mathopen{}\left\lceil\frac{n}{2}\right\rceil\mathclose{} is actually a fixed point of π 𝜋 \pi when n 𝑛 n is odd, and the cycle decomposition of π 𝜋 \pi consists of a i subscript 𝑎 𝑖 a_{i} cycles of length 2 ​ d i 2 subscript 𝑑 𝑖 2d_{i} for every i ∈ [r] 𝑖 delimited-[] 𝑟 i\in[r] for some ( a 1, …, a r) ∈ S k ​ ( n) subscript 𝑎 1 … subscript 𝑎 𝑟 subscript 𝑆 𝑘 𝑛 (a_{1},\ldots,a_{r})\in S_{k}(n), and an additional 1-cycle when n 𝑛 n is odd. Note that if j 𝑗 j is in a cycle of length 2 ​ d i 2 subscript 𝑑 𝑖 2d_{i}, then n − j 𝑛 𝑗 n-j must be in the same cycle at distance d i subscript 𝑑 𝑖 d_{i} away.

Conversely, for each ( a 1, …, a r) ∈ S k ​ ( n), subscript 𝑎 1 … subscript 𝑎 𝑟 subscript 𝑆 𝑘 𝑛 (a_{1},\ldots,a_{r})\in S_{k}(n), there are ⌊ n 2 ⌋! ∏ i = 1 r a i! ​ ( d i!) a i 𝑛 2 superscript subscript product 𝑖 1 𝑟 subscript 𝑎 𝑖 superscript subscript 𝑑 𝑖 subscript 𝑎 𝑖 \frac{\mathopen{}\left\lfloor\frac{n}{2}\right\rfloor\mathclose{}!}{\prod_{i=1}^{r}a_{i}!(d_{i}!)^{a_{i}}} many ways to partition the elements into these collection of cycles, and for each cycle there are ( d i − 1)! ​ 2 d i − 1 subscript 𝑑 𝑖 1 superscript 2 subscript 𝑑 𝑖 1 (d_{i}-1)!2^{d_{i}-1} ways to order its elements. Each of these leads to a permutation π 𝜋 \pi for which π k superscript 𝜋 𝑘 \pi^{k} is the decreasing permutation. ∎

Note that if ⌊ n 2 ⌋ 𝑛 2 \mathopen{}\left\lfloor\frac{n}{2}\right\rfloor\mathclose{} is not a multiple of 2 ν 2 ​ ( k) superscript 2 subscript 𝜈 2 𝑘 2^{\nu_{2}(k)}, or equivalently if n ≢ 0, 1 ( mod 2 ν 2 ​ ( k) + 1), not-equivalent-to 𝑛 0 annotated 1 pmod superscript 2 subscript 𝜈 2 𝑘 1 n\not\equiv 0,1\pmod{2^{\nu_{2}(k)+1}}, then S k ​ ( n) = ∅ subscript 𝑆 𝑘 𝑛 S_{k}(n)=\emptyset, so there are no permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} whose k 𝑘 k -th power is the decreasing permutation.

## 2 Expected numbers of descents and inversions

Throughout this section, we let n ≥ 2 ​ k + 1 ≥ 3 𝑛 2 𝑘 1 3 n\geq 2k+1\geq 3 and fix distinct i, j ∈ [n] 𝑖 𝑗 delimited-[] 𝑛 i,j\in[n]. We first prove a series of lemmas that counts for distinct x, y ∈ [n] 𝑥 𝑦 delimited-[] 𝑛 x,y\in[n], how many π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfies π k ​ ( i) = x superscript 𝜋 𝑘 𝑖 𝑥 \pi^{k}(i)=x and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y. These lemmas will later be used to prove Theorems 1.1 and 1.2.

###### Lemma 2.1.

If x, y ∈ [n] ∖ { i, j } 𝑥 𝑦 delimited-[] 𝑛 𝑖 𝑗 x,y\in[n]\setminus\{i,j\}, then the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = x superscript 𝜋 𝑘 𝑖 𝑥 \pi^{k}(i)=x and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y is independent of the choice of x 𝑥 x and y 𝑦 y.

###### Proof.

This is clear from the symmetry of all elements in [n] ∖ { i, j } delimited-[] 𝑛 𝑖 𝑗 [n]\setminus\{i,j\}. ∎

Though we do not need it to prove Theorem 1.1 and Theorem 1.2, we record here for completeness that the number of such permutations is

 | ( n 2 − ( 2 ​ τ ​ ( k) + 3) ​ n + τ 2 ​ ( k) + 3 ​ τ ​ ( k) + τ o ​ ( k) + σ ​ ( k)) ​ ( n − 4)!. superscript 𝑛 2 2 𝜏 𝑘 3 𝑛 superscript 𝜏 2 𝑘 3 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 𝑛 4 (n^{2}-(2\tau(k)+3)n+\tau^{2}(k)+3\tau(k)+\tau_{\text{o}}(k)+\sigma(k))(n-4)!. |  |

This formula can be obtained either as a corollary of the following series of lemmas, or by counting directly as in the proofs of those lemmas.

###### Lemma 2.2.

For every i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1], among all permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} for which { π k ​ ( i), π k ​ ( i + 1) } ≠ { i, i + 1 }, superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 𝑖 𝑖 1 \{\pi^{k}(i),\pi^{k}(i+1)\}\not=\{i,i+1\}, half of them satisfy π k ​ ( i) > π k ​ ( i + 1) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 \pi^{k}(i)>\pi^{k}(i+1) and half of them satisfy π k ​ ( i) < π k ​ ( i + 1) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 \pi^{k}(i)<\pi^{k}(i+1).

###### Proof.

By Lemma 2.1, it suffices to consider those π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} such that exactly one of π k ​ ( i), π k ​ ( i + 1) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 \pi^{k}(i),\pi^{k}(i+1) is equal to i 𝑖 i or i + 1 𝑖 1 i+1. This can be proved using Lemmas 2.3 and 2.4 below, but we provide a more direct bijective proof here.

For every x ∈ [n] ∖ { i, i + 1 } 𝑥 delimited-[] 𝑛 𝑖 𝑖 1 x\in[n]\setminus\{i,i+1\}, switching the labels i 𝑖 i and i + 1 𝑖 1 i+1 gives a bijection between π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} for which ( π k ​ ( i), π k ​ ( i + 1)) = ( i, x) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 𝑖 𝑥 (\pi^{k}(i),\pi^{k}(i+1))=(i,x) and those satisfying ( π k ​ ( i), π k ​ ( i + 1)) = ( x, i + 1) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 𝑥 𝑖 1 (\pi^{k}(i),\pi^{k}(i+1))=(x,i+1), and and a bijection between those satisfying ( π k ​ ( i), π k ​ ( i + 1)) = ( x, i) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 𝑥 𝑖 (\pi^{k}(i),\pi^{k}(i+1))=(x,i) and those with ( π k ​ ( i), π k ​ ( i + 1)) = ( i + 1, x) superscript 𝜋 𝑘 𝑖 superscript 𝜋 𝑘 𝑖 1 𝑖 1 𝑥 (\pi^{k}(i),\pi^{k}(i+1))=(i+1,x). Since x > i 𝑥 𝑖 x>i if and only if i + 1 < x 𝑖 1 𝑥 i+1<x under our assumption on x 𝑥 x, these two bijections swaps whether π k superscript 𝜋 𝑘 \pi^{k} has an ascent or descent at position i 𝑖 i, implying that there are equally many of them having each. ∎

###### Lemma 2.3.

For every y ∈ [n] ∖ { i, j } 𝑦 delimited-[] 𝑛 𝑖 𝑗 y\in[n]\setminus\{i,j\}, the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y is

 | ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 3)!. 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 3 (\tau(k)n-\tau^{2}(k)-\sigma(k))(n-3)!. |  |

###### Proof.

Let d 𝑑 d be the length of the cycle that i 𝑖 i belongs to in π 𝜋 \pi, then d ∣ k conditional 𝑑 𝑘 d\mid k as π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i. Note that j 𝑗 j cannot be in the same cycle as i 𝑖 i, as otherwise π k ​ ( j) = j superscript 𝜋 𝑘 𝑗 𝑗 \pi^{k}(j)=j. Let ℓ ℓ \ell be the length of the cycle that j 𝑗 j belongs to, and observe that y 𝑦 y must be in this cycle as well. Let 1 ≤ t ≤ min ⁡ { k, ℓ − 1 } 1 𝑡 𝑘 ℓ 1 1\leq t\leq\min\{k,\ell-1\} be the distance from j 𝑗 j to y 𝑦 y in this cycle, or equivalently the smallest positive integer such that π t ​ ( j) = y superscript 𝜋 𝑡 𝑗 𝑦 \pi^{t}(j)=y.

If t = k 𝑡 𝑘 t=k, then ℓ ≥ k + 1 ℓ 𝑘 1 \ell\geq k+1. On the other hand, for any π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n}, d ∣ k conditional 𝑑 𝑘 d\mid k and k + 1 ≤ ℓ ≤ n − d 𝑘 1 ℓ 𝑛 𝑑 k+1\leq\ell\leq n-d, such that i 𝑖 i is in a length d 𝑑 d cycle and j, y 𝑗 𝑦 j,y are in another length ℓ ℓ \ell cycle with the distance from j 𝑗 j to y 𝑦 y on this cycle being k 𝑘 k, we have π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y. There are ∑ d ∣ k ( n − d − k) ​ ( n − 3)! subscript conditional 𝑑 𝑘 𝑛 𝑑 𝑘 𝑛 3 \sum_{d\mid k}(n-d-k)(n-3)! permutations of this form.

If t < k 𝑡 𝑘 t<k, then as π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y, we must have k ≡ t ( mod ℓ) 𝑘 annotated 𝑡 pmod ℓ k\equiv t\pmod{\ell}, and so ℓ ≤ k ℓ 𝑘 \ell\leq k. Moreover, if ℓ ∣ k conditional ℓ 𝑘 \ell\mid k, then t = 0 𝑡 0 t=0, which is not allowed. Conversely, for any d ∣ k conditional 𝑑 𝑘 d\mid k and every ℓ ∈ [k] ℓ delimited-[] 𝑘 \ell\in[k] not dividing k 𝑘 k, there is exactly one choice of t ∈ [ℓ − 1] 𝑡 delimited-[] ℓ 1 t\in[\ell-1] satisfying k ≡ t ( mod ℓ) 𝑘 annotated 𝑡 pmod ℓ k\equiv t\pmod{\ell}. For any π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} such that i 𝑖 i is in a length d 𝑑 d cycle and j, y 𝑗 𝑦 j,y are in another length ℓ ℓ \ell cycle with the distance from j 𝑗 j to y 𝑦 y on this cycle being t 𝑡 t, we have π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y. There are ∑ d ∣ k ∑ ℓ ∤ k ( n − 3)! subscript conditional 𝑑 𝑘 subscript not-divides ℓ 𝑘 𝑛 3 \sum_{d\mid k}\sum_{\ell\nmid k}(n-3)! permutations of this form.

Therefore, the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y is

 | ∑ d ∣ k ( n − d − k) ​ ( n − 3)! + ∑ d ∣ k ∑ ℓ ∤ k ( n − 3)! subscript conditional 𝑑 𝑘 𝑛 𝑑 𝑘 𝑛 3 subscript conditional 𝑑 𝑘 subscript not-divides ℓ 𝑘 𝑛 3 \displaystyle\sum_{d\mid k}(n-d-k)(n-3)!+\sum_{d\mid k}\sum_{\ell\nmid k}(n-3)! | = ( τ ​ ( k) ​ n − σ ​ ( k) − k ​ τ ​ ( k) + τ ​ ( k) ​ ( k − τ ​ ( k))) ​ ( n − 3)! absent 𝜏 𝑘 𝑛 𝜎 𝑘 𝑘 𝜏 𝑘 𝜏 𝑘 𝑘 𝜏 𝑘 𝑛 3 \displaystyle=(\tau(k)n-\sigma(k)-k\tau(k)+\tau(k)(k-\tau(k)))(n-3)! |  |

 |  | = ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 3)!, absent 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 3 \displaystyle=(\tau(k)n-\tau^{2}(k)-\sigma(k))(n-3)!, |  |

as required. ∎

###### Lemma 2.4.

For every y ∈ [n] ∖ { i, j } 𝑦 delimited-[] 𝑛 𝑖 𝑗 y\in[n]\setminus\{i,j\}, the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y is

 | ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 3)!. 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 (n-\tau(k)-\tau_{\text{o}}(k))(n-3)!. |  |

###### Proof.

From assumption, i, j, y 𝑖 𝑗 𝑦 i,j,y are in the same cycle of π 𝜋 \pi. Let ℓ ℓ \ell be the length of this cycle, and let 1 ≤ t ≤ min ⁡ { ℓ − 1, k } 1 𝑡 ℓ 1 𝑘 1\leq t\leq\min\{\ell-1,k\} be the distance from i 𝑖 i to j 𝑗 j on this cycle, which is also the smallest positive integer such that π t ​ ( i) = j superscript 𝜋 𝑡 𝑖 𝑗 \pi^{t}(i)=j. It follows that k ≡ t ( mod ℓ) 𝑘 annotated 𝑡 pmod ℓ k\equiv t\pmod{\ell}, and so t 𝑡 t must be the distance from j 𝑗 j to y 𝑦 y on this cycle as well. In particular, ℓ ≠ 2 ​ t ℓ 2 𝑡 \ell\not=2t, as otherwise i = π ℓ ​ ( i) = π 2 ​ t ​ ( i) = π t ​ ( j) = y 𝑖 superscript 𝜋 ℓ 𝑖 superscript 𝜋 2 𝑡 𝑖 superscript 𝜋 𝑡 𝑗 𝑦 i=\pi^{\ell}(i)=\pi^{2t}(i)=\pi^{t}(j)=y, contradiction.

If t = k 𝑡 𝑘 t=k, then ℓ ≥ k + 1 ℓ 𝑘 1 \ell\geq k+1 and ℓ ≠ 2 ​ k ℓ 2 𝑘 \ell\not=2k. On the other hand, for any ℓ ≥ k + 1 ℓ 𝑘 1 \ell\geq k+1 and not equal to 2 ​ k 2 𝑘 2k, and any permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} with a cycle of length ℓ ℓ \ell containing i, j, y 𝑖 𝑗 𝑦 i,j,y, such that the distance in this cycle from i 𝑖 i to j 𝑗 j and from j 𝑗 j to y 𝑦 y are both k 𝑘 k, we have π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y. There are ( n − k − 1) ​ ( n − 3)! 𝑛 𝑘 1 𝑛 3 (n-k-1)(n-3)! permutations of this form.

If t < k 𝑡 𝑘 t<k, we must have ℓ < k ℓ 𝑘 \ell<k as k ≡ t ( mod ℓ) 𝑘 annotated 𝑡 pmod ℓ k\equiv t\pmod{\ell}. If ℓ ∣ k conditional ℓ 𝑘 \ell\mid k, then t = 0 𝑡 0 t=0, which is not allowed. Note that given k ≡ t ( mod ℓ) 𝑘 annotated 𝑡 pmod ℓ k\equiv t\pmod{\ell}, then ℓ = 2 ​ t ℓ 2 𝑡 \ell=2t, which is also not allowed from above, implies that 2 ​ k 2 𝑘 2k is an odd multiple of ℓ ℓ \ell. Conversely, for any ℓ ∈ [k] ℓ delimited-[] 𝑘 \ell\in[k] not dividing k 𝑘 k, and such that 2 ​ k 2 𝑘 2k is not an odd multiple of ℓ ℓ \ell, we have that t ∈ [ℓ − 1] 𝑡 delimited-[] ℓ 1 t\in[\ell-1] given by t ≡ k ( mod ℓ) 𝑡 annotated 𝑘 pmod ℓ t\equiv k\pmod{\ell} is not equal to 1 2 ​ ℓ 1 2 ℓ \frac{1}{2}\ell. Moreover, for any permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} with a cycle of length ℓ ℓ \ell containing i, j, y 𝑖 𝑗 𝑦 i,j,y, such that the distance in this cycle from i 𝑖 i to j 𝑗 j and from j 𝑗 j to y 𝑦 y are both t 𝑡 t, we have π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y. Let k = 2 a ​ b 𝑘 superscript 2 𝑎 𝑏 k=2^{a}b, where a, b 𝑎 𝑏 a,b are positive integers and 2 ∤ b not-divides 2 𝑏 2\nmid b. If ℓ ∈ [k] ℓ delimited-[] 𝑘 \ell\in[k], ℓ ∤ k not-divides ℓ 𝑘 \ell\nmid k and 2 ​ k 2 𝑘 2k is an odd multiple of ℓ ℓ \ell, then ℓ ℓ \ell must be of the form 2 a + 1 ​ d superscript 2 𝑎 1 𝑑 2^{a+1}d, where d 𝑑 d is a proper divisor of b 𝑏 b. As the converse of this is also true, the number of such ℓ ℓ \ell is then equal to τ ​ ( b) − 1 = τ o ​ ( k) − 1 𝜏 𝑏 1 subscript 𝜏 o 𝑘 1 \tau(b)-1=\tau_{\text{o}}(k)-1. Hence, the number of the permutations of this form is ( k − τ ​ ( k) − τ o ​ ( k) + 1) ​ ( n − 3)! 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 1 𝑛 3 (k-\tau(k)-\tau_{\text{o}}(k)+1)(n-3)!.

Therefore, the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y is

 | ( ( n − k − 1) + ( k − τ ​ ( k) − τ o ​ ( k) + 1)) ​ ( n − 3)! = ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 3)!, 𝑛 𝑘 1 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 1 𝑛 3 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 ((n-k-1)+(k-\tau(k)-\tau_{\text{o}}(k)+1))(n-3)!=(n-\tau(k)-\tau_{\text{o}}(k))(n-3)!, |  |

as required. ∎

###### Lemma 2.5.

The number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = j superscript 𝜋 𝑘 𝑗 𝑗 \pi^{k}(j)=j is

 | ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k)) ​ ( n − 2)!. superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 𝑛 2 (\tau^{2}(k)-\tau(k)+\sigma(k))(n-2)!. |  |

###### Proof.

First suppose i 𝑖 i and j 𝑗 j are in distinct cycles of π 𝜋 \pi of length d 1 subscript 𝑑 1 d_{1} and d 2 subscript 𝑑 2 d_{2}, respectively. From assumption, we must have d 1, d 2 ∣ k subscript 𝑑 1 conditional subscript 𝑑 2 𝑘 d_{1},d_{2}\mid k. On the other hand, for any d 1, d 2 ∣ k subscript 𝑑 1 conditional subscript 𝑑 2 𝑘 d_{1},d_{2}\mid k and any π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} with i 𝑖 i in a cycle of length d 1 subscript 𝑑 1 d_{1}, and j 𝑗 j in another cycle of length d 2 subscript 𝑑 2 d_{2}, we have π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = j superscript 𝜋 𝑘 𝑗 𝑗 \pi^{k}(j)=j. There are τ 2 ​ ( k) ​ ( n − 2)! superscript 𝜏 2 𝑘 𝑛 2 \tau^{2}(k)(n-2)! permutations of this form.

Now suppose i 𝑖 i and j 𝑗 j are in the same cycle of π 𝜋 \pi of length d 𝑑 d. Again, d ∣ k conditional 𝑑 𝑘 d\mid k from assumption. Conversely, for any d ∣ k conditional 𝑑 𝑘 d\mid k, and any π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} with i, j 𝑖 𝑗 i,j in the same cycle of length d 𝑑 d, we have π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = j superscript 𝜋 𝑘 𝑗 𝑗 \pi^{k}(j)=j. Since the distance from i 𝑖 i to j 𝑗 j in this cycle can be any number in [d − 1] delimited-[] 𝑑 1 [d-1], there are ∑ d ∣ k ( d − 1) ​ ( n − 2)! = ( σ ​ ( k) − τ ​ ( k)) ​ ( n − 2)! subscript conditional 𝑑 𝑘 𝑑 1 𝑛 2 𝜎 𝑘 𝜏 𝑘 𝑛 2 \sum_{d\mid k}(d-1)(n-2)!=(\sigma(k)-\tau(k))(n-2)! permutations of this form.

Therefore, the number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( j) = j superscript 𝜋 𝑘 𝑗 𝑗 \pi^{k}(j)=j is

 | τ 2 ​ ( k) ​ ( n − 2) + ( σ ​ ( k) − τ ​ ( k)) ​ ( n − 2)! = ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k)) ​ ( n − 2)!, superscript 𝜏 2 𝑘 𝑛 2 𝜎 𝑘 𝜏 𝑘 𝑛 2 superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 𝑛 2 \tau^{2}(k)(n-2)+(\sigma(k)-\tau(k))(n-2)!=(\tau^{2}(k)-\tau(k)+\sigma(k))(n-2)!, |  |

as required. ∎

###### Lemma 2.6.

The number of permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = i superscript 𝜋 𝑘 𝑗 𝑖 \pi^{k}(j)=i is

 | τ o ​ ( k) ​ ( n − 2)!. subscript 𝜏 o 𝑘 𝑛 2 \tau_{\text{o}}(k)(n-2)!. |  |

###### Proof.

From assumption, i 𝑖 i and j 𝑗 j are in the same cycle in π 𝜋 \pi. Let ℓ ℓ \ell be the length of this cycle. Let 1 ≤ t ≤ min ⁡ { k, ℓ − 1 } 1 𝑡 𝑘 ℓ 1 1\leq t\leq\min\{k,\ell-1\} be minimal so that π t ​ ( i) = j superscript 𝜋 𝑡 𝑖 𝑗 \pi^{t}(i)=j, or equivalently t 𝑡 t is the distance from i 𝑖 i to j 𝑗 j in the cycle, then t ≡ k ( mod ℓ) 𝑡 annotated 𝑘 pmod ℓ t\equiv k\pmod{\ell}. It also follows that π ℓ − t ​ ( j) = i superscript 𝜋 ℓ 𝑡 𝑗 𝑖 \pi^{\ell-t}(j)=i, so ℓ − t ≡ − t ≡ k ( mod ℓ) ℓ 𝑡 𝑡 annotated 𝑘 pmod ℓ \ell-t\equiv-t\equiv k\pmod{\ell}. Thus, t ≡ − t ( mod ℓ) 𝑡 annotated 𝑡 pmod ℓ t\equiv-t\pmod{\ell}, and since t ∈ [ℓ − 1] 𝑡 delimited-[] ℓ 1 t\in[\ell-1], we must have ℓ = 2 ​ t ℓ 2 𝑡 \ell=2t. Since π 2 ​ k ​ ( i) = π k ​ ( j) = i superscript 𝜋 2 𝑘 𝑖 superscript 𝜋 𝑘 𝑗 𝑖 \pi^{2k}(i)=\pi^{k}(j)=i, we must have ℓ ∣ 2 ​ k conditional ℓ 2 𝑘 \ell\mid 2k and so t ∣ k conditional 𝑡 𝑘 t\mid k. Also, 2 ​ t ∤ k not-divides 2 𝑡 𝑘 2t\nmid k as otherwise ℓ ∣ k conditional ℓ 𝑘 \ell\mid k and π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i.

Conversely, for any t ≥ 1 𝑡 1 t\geq 1 satisfying t ∣ k conditional 𝑡 𝑘 t\mid k and 2 ​ t ∤ k not-divides 2 𝑡 𝑘 2t\nmid k, we have k ≡ t ( mod 2 ​ t) 𝑘 annotated 𝑡 pmod 2 𝑡 k\equiv t\pmod{2t}. So for any π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} containing a cycle of length 2 ​ t 2 𝑡 2t, in which i 𝑖 i and j 𝑗 j are distance t 𝑡 t apart, we have π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = i superscript 𝜋 𝑘 𝑗 𝑖 \pi^{k}(j)=i.

Therefore, the number of such permutations in 𝒮 n subscript 𝒮 𝑛 \mathcal{S}_{n} is exactly ( n − 2)! 𝑛 2 (n-2)! times the number of divisors t 𝑡 t of k 𝑘 k such that 2 ​ t ∤ k not-divides 2 𝑡 𝑘 2t\nmid k. Let k = 2 a ​ b 𝑘 superscript 2 𝑎 𝑏 k=2^{a}b, where a, b 𝑎 𝑏 a,b are positive integers and 2 ∤ b not-divides 2 𝑏 2\nmid b. Then, every divisor t 𝑡 t of k 𝑘 k satisfying 2 ​ t ∤ k not-divides 2 𝑡 𝑘 2t\nmid k is of the form 2 a ​ d superscript 2 𝑎 𝑑 2^{a}d, where d 𝑑 d is a divisor of b 𝑏 b, and the converse is true as well. Thus, there are exactly τ ​ ( b) = τ o ​ ( k) 𝜏 𝑏 subscript 𝜏 o 𝑘 \tau(b)=\tau_{\text{o}}(k) such divisors, which proves that there are exactly τ o ​ ( k) ​ ( n − 2)! subscript 𝜏 o 𝑘 𝑛 2 \tau_{\text{o}}(k)(n-2)! permutations π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π k ​ ( i) = j superscript 𝜋 𝑘 𝑖 𝑗 \pi^{k}(i)=j and π k ​ ( j) = i superscript 𝜋 𝑘 𝑗 𝑖 \pi^{k}(j)=i. ∎

We now combine these lemmas to prove Theorems 1.1 and 1.2. We prove Theorem 1.2 first as its proof contains most of what we need to prove Theorem 1.1.

###### Proof of Theorem 1.2.

For each π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n}, let ninv ⁡ ( π) = n ​ ( n − 1) 2 − inv ⁡ ( π) ninv 𝜋 𝑛 𝑛 1 2 inv 𝜋 \operatorname{ninv}(\pi)=\frac{n(n-1)}{2}-\operatorname{inv}(\pi) be the number of pairs of indices i < j 𝑖 𝑗 i<j in [n] delimited-[] 𝑛 [n] satisfying π ​ ( i) < π ​ ( j) 𝜋 𝑖 𝜋 𝑗 \pi(i)<\pi(j). We call each pair i < j 𝑖 𝑗 i<j of this form a non-inversion of π 𝜋 \pi. Note that to prove Theorem 1.2, it suffices to show that

 | ∑ π ∈ 𝒮 n ( ninv ⁡ ( π k) − inv ⁡ ( π k)) = ( τ ​ ( k) − 1) ​ n ⋅ n! 3 + ( τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k)) ​ n! 6. subscript 𝜋 subscript 𝒮 𝑛 ninv superscript 𝜋 𝑘 inv superscript 𝜋 𝑘 ⋅ 𝜏 𝑘 1 𝑛 𝑛 3 superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 𝑛 6 \sum_{\pi\in\mathcal{S}_{n}}(\operatorname{ninv}(\pi^{k})-\operatorname{inv}(\pi^{k}))=\frac{(\tau(k)-1)n\cdot n!}{3}+\frac{(\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k))n!}{6}. |  |

Let π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} and i < j 𝑖 𝑗 i<j in [n − 1] delimited-[] 𝑛 1 [n-1] satisfy π k ​ ( i) = x superscript 𝜋 𝑘 𝑖 𝑥 \pi^{k}(i)=x and π k ​ ( j) = y superscript 𝜋 𝑘 𝑗 𝑦 \pi^{k}(j)=y. We consider all possible types of ways we can have an inversion or non-inversion on the pair i < j 𝑖 𝑗 i<j, depending on the values of x 𝑥 x and y 𝑦 y.

Type 1. x, y ∉ { i, j } 𝑥 𝑦 𝑖 𝑗 x,y\not\in\{i,j\}. By Lemma 2.1, it is equally likely to have x < y 𝑥 𝑦 x<y or x > y 𝑥 𝑦 x>y, so inversions and non-inversions of this type cancel out.

Type 2. x = i 𝑥 𝑖 x=i and y ∉ { i, j } 𝑦 𝑖 𝑗 y\not\in\{i,j\}. By Lemma 2.3, there are ( i − 1) ​ ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 3)! 𝑖 1 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 3 (i-1)(\tau(k)n-\tau^{2}(k)-\sigma(k))(n-3)! ways to have an inversion of this type as y 𝑦 y can take any value in [i − 1] delimited-[] 𝑖 1 [i-1], and ( n − i − 1) ​ ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 3)! 𝑛 𝑖 1 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 3 (n-i-1)(\tau(k)n-\tau^{2}(k)-\sigma(k))(n-3)! ways for a non-inversion as y 𝑦 y can take any value in [n] ∖ ( [i] ∪ { j }) delimited-[] 𝑛 delimited-[] 𝑖 𝑗 [n]\setminus([i]\cup\{j\}).

Type 3. x = j 𝑥 𝑗 x=j and y ∉ { i, j } 𝑦 𝑖 𝑗 y\not\in\{i,j\}. By Lemma 2.4, there are ( j − 2) ​ ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 3)! 𝑗 2 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 (j-2)(n-\tau(k)-\tau_{\text{o}}(k))(n-3)! ways to have an inversion of this type, and ( n − j) ​ ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 3)! 𝑛 𝑗 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 (n-j)(n-\tau(k)-\tau_{\text{o}}(k))(n-3)! ways for a non-inversion.

Type 4. x ∉ { i, j } 𝑥 𝑖 𝑗 x\not\in\{i,j\} and y = j 𝑦 𝑗 y=j. By Lemma 2.3, there are ( n − j) ​ ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 3)! 𝑛 𝑗 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 3 (n-j)(\tau(k)n-\tau^{2}(k)-\sigma(k))(n-3)! ways to have an inversion of this type, and ( j − 2) ​ ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 3)! 𝑗 2 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 3 (j-2)(\tau(k)n-\tau^{2}(k)-\sigma(k))(n-3)! ways for a non-inversion.

Type 5. x ∉ { i, j } 𝑥 𝑖 𝑗 x\not\in\{i,j\} and y = i 𝑦 𝑖 y=i. By Lemma 2.4, there are ( n − i − 1) ​ ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 3)! 𝑛 𝑖 1 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 (n-i-1)(n-\tau(k)-\tau_{\text{o}}(k))(n-3)! ways to have an inversion of this type, and ( i − 1) ​ ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 3)! 𝑖 1 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 (i-1)(n-\tau(k)-\tau_{\text{o}}(k))(n-3)! ways for a non-inversion.

Type 6. x = i, y = j formulae-sequence 𝑥 𝑖 𝑦 𝑗 x=i,y=j. By Lemma 2.5, there are ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k)) ​ ( n − 2)! superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 𝑛 2 (\tau^{2}(k)-\tau(k)+\sigma(k))(n-2)! ways for this to happen, each resulting in a non-inversion.

Type 7. x = j, y = i formulae-sequence 𝑥 𝑗 𝑦 𝑖 x=j,y=i. By Lemma 2.6, there are τ o ​ ( k) ​ ( n − 2)! subscript 𝜏 o 𝑘 𝑛 2 \tau_{\text{o}}(k)(n-2)! ways for this to happen, each resulting in an inversion.

Summing from Type 2 to Type 7, the total number of ways to have a non-inversion at i < j 𝑖 𝑗 i<j of these types is

 | ( ( n − i + j − 3) ​ ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) + ( n + i − j − 1) ​ ( n − τ ​ ( k) − τ o ​ ( k))) ​ ( n − 3)! + ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k)) ​ ( n − 2)!, 𝑛 𝑖 𝑗 3 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 𝑖 𝑗 1 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 𝑛 2 ((n-i+j-3)(\tau(k)n-\tau^{2}(k)-\sigma(k))+(n+i-j-1)(n-\tau(k)-\tau_{\text{o}}(k)))(n-3)!+(\tau^{2}(k)-\tau(k)+\sigma(k))(n-2)!, |  |

while the total number of ways to have an inversion at i < j 𝑖 𝑗 i<j of these types is

 | ( ( n + i − j − 1) ​ ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) + ( n − i + j − 3) ​ ( n − τ ​ ( k) − τ o ​ ( k))) ​ ( n − 3)! + τ o ​ ( k) ​ ( n − 2)!. 𝑛 𝑖 𝑗 1 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 𝑖 𝑗 3 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 subscript 𝜏 o 𝑘 𝑛 2 ((n+i-j-1)(\tau(k)n-\tau^{2}(k)-\sigma(k))+(n-i+j-3)(n-\tau(k)-\tau_{\text{o}}(k)))(n-3)!+\tau_{\text{o}}(k)(n-2)!. |  |

The difference of the first two terms of the two expressions above, summed over all i < j 𝑖 𝑗 i<j in [n] delimited-[] 𝑛 [n], is

 | ∑ i = 1 n − 1 ∑ j = i + 1 n 2 ​ ( j − i − 1) ​ ( ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) − ( n − τ ​ ( k) − τ o ​ ( k))) ​ ( n − 3)! superscript subscript 𝑖 1 𝑛 1 superscript subscript 𝑗 𝑖 1 𝑛 2 𝑗 𝑖 1 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 \displaystyle\phantom{==}\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}2(j-i-1)((\tau(k)n-\tau^{2}(k)-\sigma(k))-(n-\tau(k)-\tau_{\text{o}}(k)))(n-3)! |  |

 | = ( ( τ ​ ( k) − 1) ​ n − τ 2 ​ ( k) − σ ​ ( k) + τ ​ ( k) + τ o ​ ( k)) ​ ( n − 3)! ​ ∑ i = 1 n − 1 ∑ j = i + 1 n 2 ​ ( j − i − 1) absent 𝜏 𝑘 1 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 superscript subscript 𝑖 1 𝑛 1 superscript subscript 𝑗 𝑖 1 𝑛 2 𝑗 𝑖 1 \displaystyle=((\tau(k)-1)n-\tau^{2}(k)-\sigma(k)+\tau(k)+\tau_{\text{o}}(k))(n-3)!\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}2(j-i-1) |  |

 | = ( ( τ ​ ( k) − 1) ​ n − τ 2 ​ ( k) − σ ​ ( k) + τ ​ ( k) + τ o ​ ( k)) ​ ( n − 3)! ​ n ​ ( n − 1) ​ ( n − 2) 3 absent 𝜏 𝑘 1 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 𝑛 𝑛 1 𝑛 2 3 \displaystyle=((\tau(k)-1)n-\tau^{2}(k)-\sigma(k)+\tau(k)+\tau_{\text{o}}(k))(n-3)!\frac{n(n-1)(n-2)}{3} |  |

 | = ( ( τ ​ ( k) − 1) ​ n − τ 2 ​ ( k) − σ ​ ( k) + τ ​ ( k) + τ o ​ ( k)) ​ n! 3. absent 𝜏 𝑘 1 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 \displaystyle=((\tau(k)-1)n-\tau^{2}(k)-\sigma(k)+\tau(k)+\tau_{\text{o}}(k))\frac{n!}{3}. |  |

The difference of the last term of the two expressions above, again summed over all i < j 𝑖 𝑗 i<j in [n] delimited-[] 𝑛 [n], is

 | ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k) − τ o ​ ( k)) ​ ( n − 2)! ​ n ​ ( n − 1) 2 = ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k) − τ o ​ ( k)) ​ n! 2. superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 subscript 𝜏 o 𝑘 𝑛 2 𝑛 𝑛 1 2 superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 subscript 𝜏 o 𝑘 𝑛 2 (\tau^{2}(k)-\tau(k)+\sigma(k)-\tau_{\text{o}}(k))(n-2)!\frac{n(n-1)}{2}=(\tau^{2}(k)-\tau(k)+\sigma(k)-\tau_{\text{o}}(k))\frac{n!}{2}. |  |

Hence,

 | ∑ π ∈ 𝒮 n ( ninv ⁡ ( π k) − inv ⁡ ( π k)) subscript 𝜋 subscript 𝒮 𝑛 ninv superscript 𝜋 𝑘 inv superscript 𝜋 𝑘 \displaystyle\phantom{=}\sum_{\pi\in\mathcal{S}_{n}}(\operatorname{ninv}(\pi^{k})-\operatorname{inv}(\pi^{k})) |  |

 | = ( ( τ ​ ( k) − 1) ​ n − τ 2 ​ ( k) − σ ​ ( k) + τ ​ ( k) + τ o ​ ( k)) ​ n! 3 + ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k) − τ o ​ ( k)) ​ n! 2 absent 𝜏 𝑘 1 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 3 superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 subscript 𝜏 o 𝑘 𝑛 2 \displaystyle=((\tau(k)-1)n-\tau^{2}(k)-\sigma(k)+\tau(k)+\tau_{\text{o}}(k))\frac{n!}{3}+(\tau^{2}(k)-\tau(k)+\sigma(k)-\tau_{\text{o}}(k))\frac{n!}{2} |  |

 | = ( τ ​ ( k) − 1) ​ n ⋅ n! 3 + ( τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k)) ​ n! 6, absent ⋅ 𝜏 𝑘 1 𝑛 𝑛 3 superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 𝑛 6 \displaystyle=\frac{(\tau(k)-1)n\cdot n!}{3}+\frac{(\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k))n!}{6}, |  |

as required. ∎

###### Proof of Theorem 1.1.

For each π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n}, let asc ⁡ ( π) = n − 1 − des ⁡ ( π) asc 𝜋 𝑛 1 des 𝜋 \operatorname{asc}(\pi)=n-1-\operatorname{des}(\pi) be the number of indices i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1] satisfying π ​ ( i) < π ​ ( i + 1) 𝜋 𝑖 𝜋 𝑖 1 \pi(i)<\pi(i+1). We say that π 𝜋 \pi has an ascent at i 𝑖 i in these situations. Note that to prove Theorem 1.1, it suffices to show that

 | ∑ π ∈ 𝒮 n ( asc ⁡ ( π k) − des ⁡ ( π k)) = ( τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k)) ​ ( n − 1)!. subscript 𝜋 subscript 𝒮 𝑛 asc superscript 𝜋 𝑘 des superscript 𝜋 𝑘 superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 𝑛 1 \sum_{\pi\in\mathcal{S}_{n}}(\operatorname{asc}(\pi^{k})-\operatorname{des}(\pi^{k}))=(\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k))(n-1)!. |  |

Let π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} and i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1] satisfy π k ​ ( i) = x superscript 𝜋 𝑘 𝑖 𝑥 \pi^{k}(i)=x and π k ​ ( i + 1) = y superscript 𝜋 𝑘 𝑖 1 𝑦 \pi^{k}(i+1)=y. Setting j = i + 1 𝑗 𝑖 1 j=i+1 in Type 1 to Type 7 in the proof of Theorem 1.2 above, we see that if x, y ∉ { i, i + 1 } 𝑥 𝑦 𝑖 𝑖 1 x,y\not\in\{i,i+1\}, descents and ascents of Type 1 cancel out, and by summing from Type 2 to Type 7, the total number of ways to have an ascent at i 𝑖 i of those types is

 | ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 2)! + ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 2)! + ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k)) ​ ( n − 2)!, 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 2 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 2 superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 𝑛 2 (\tau(k)n-\tau^{2}(k)-\sigma(k))(n-2)!+(n-\tau(k)-\tau_{\text{o}}(k))(n-2)!+(\tau^{2}(k)-\tau(k)+\sigma(k))(n-2)!, |  |

while the total number of ways to have an descent at i 𝑖 i of those types is

 | ( τ ​ ( k) ​ n − τ 2 ​ ( k) − σ ​ ( k)) ​ ( n − 2)! + ( n − τ ​ ( k) − τ o ​ ( k)) ​ ( n − 2)! + τ o ​ ( k) ​ ( n − 2)!. 𝜏 𝑘 𝑛 superscript 𝜏 2 𝑘 𝜎 𝑘 𝑛 2 𝑛 𝜏 𝑘 subscript 𝜏 o 𝑘 𝑛 2 subscript 𝜏 o 𝑘 𝑛 2 (\tau(k)n-\tau^{2}(k)-\sigma(k))(n-2)!+(n-\tau(k)-\tau_{\text{o}}(k))(n-2)!+\tau_{\text{o}}(k)(n-2)!. |  |

Hence,

 | ∑ π ∈ 𝒮 n ( asc ⁡ ( π k) − des ⁡ ( π k)) subscript 𝜋 subscript 𝒮 𝑛 asc superscript 𝜋 𝑘 des superscript 𝜋 𝑘 \displaystyle\sum_{\pi\in\mathcal{S}_{n}}(\operatorname{asc}(\pi^{k})-\operatorname{des}(\pi^{k})) | = ∑ i = 1 n − 1 ( τ 2 ​ ( k) − τ ​ ( k) + σ ​ ( k) − τ o ​ ( k)) ​ ( n − 2)! absent superscript subscript 𝑖 1 𝑛 1 superscript 𝜏 2 𝑘 𝜏 𝑘 𝜎 𝑘 subscript 𝜏 o 𝑘 𝑛 2 \displaystyle=\sum_{i=1}^{n-1}(\tau^{2}(k)-\tau(k)+\sigma(k)-\tau_{\text{o}}(k))(n-2)! |  |

 |  | = ( τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k)) ​ ( n − 1)!, absent superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 𝑛 1 \displaystyle=(\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k))(n-1)!, |  |

as required. ∎

Note that as both τ 2 ​ ( k) − τ ​ ( k) superscript 𝜏 2 𝑘 𝜏 𝑘 \tau^{2}(k)-\tau(k) and τ o ​ ( k) − σ ​ ( k) subscript 𝜏 o 𝑘 𝜎 𝑘 \tau_{\text{o}}(k)-\sigma(k) are even, 1 2 ​ ( τ 2 ​ ( k) − τ ​ ( k) − τ o ​ ( k) + σ ​ ( k)) 1 2 superscript 𝜏 2 𝑘 𝜏 𝑘 subscript 𝜏 o 𝑘 𝜎 𝑘 \frac{1}{2}(\tau^{2}(k)-\tau(k)-\tau_{\text{o}}(k)+\sigma(k)) is an integer. In the case when k = p 𝑘 𝑝 k=p is an odd prime, the formula for the expectation of des ⁡ ( π p) des superscript 𝜋 𝑝 \operatorname{des}(\pi^{p}) simplifies to n − 1 2 − p + 1 2 ​ n 𝑛 1 2 𝑝 1 2 𝑛 \frac{n-1}{2}-\frac{p+1}{2n}, while the one for inv ⁡ ( π p) inv superscript 𝜋 𝑝 \operatorname{inv}(\pi^{p}) simplifies to n ​ ( n − 1) 4 − n 6 − p + 1 12 𝑛 𝑛 1 4 𝑛 6 𝑝 1 12 \frac{n(n-1)}{4}-\frac{n}{6}-\frac{p+1}{12}.

Finally, we remark that Theorem 1.1 is actually valid for every n ≥ k + ℓ ​ ( k) 𝑛 𝑘 ℓ 𝑘 n\geq k+\ell(k), where ℓ ​ ( k) ℓ 𝑘 \ell(k) is defined to be the largest proper divisor of k 𝑘 k. By Lemma 2.2, we only need to compare permutations counted in Lemmas 2.5 and 2.6 when j = i + 1 𝑗 𝑖 1 j=i+1. There are only two situations there in which we considered a union of cycles with total length at least k + ℓ ​ ( k) 𝑘 ℓ 𝑘 k+\ell(k): the disjoint union of two cycles of length k 𝑘 k, one containing i 𝑖 i and the other containing i + 1 𝑖 1 i+1 in Lemma 2.5, and a cycle of length 2 ​ k 2 𝑘 2k with i 𝑖 i and i + 1 𝑖 1 i+1 being diametrically opposite in Lemma 2.6. The former contributes ( n − 2)! 𝑛 2 (n-2)! ascents while the latter ( n − 2)! 𝑛 2 (n-2)! descents, which cancel out. Thus, the formula is valid for every n ≥ k + ℓ ​ ( k). 𝑛 𝑘 ℓ 𝑘 n\geq k+\ell(k).

## 3 On Grassmanian permutations π 𝜋 \pi with des ⁡ ( π k) ∈ { 0, 1 } des superscript 𝜋 𝑘 0 1 \operatorname{des}(\pi^{k})\in\{0,1\}

In this section, we show that a permutation being Grassmanian is so rare, that both π 𝜋 \pi and π k superscript 𝜋 𝑘 \pi^{k} being so implies a lot of structure, and so we can count the number of them precisely. By [1, Lem. 2.2], it is sufficient to determine the number of such permutations for which π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1 or π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n, as those satisfying π ​ ( 1) = 1 𝜋 1 1 \pi(1)=1 or π ​ ( n) = n 𝜋 𝑛 𝑛 \pi(n)=n can be counted recursively.

We begin with a technical lemma that we will use shortly to prove Theorem 1.3.

###### Lemma 3.1.

Let k ≥ 3 𝑘 3 k\geq 3, i, j ∈ [n − 1] 𝑖 𝑗 delimited-[] 𝑛 1 i,j\in[n-1]. Suppose π, π k 𝜋 superscript 𝜋 𝑘 \pi,\pi^{k} are both Grassmanian permutations with π ​ ( i) = π k ​ ( j) = n 𝜋 𝑖 superscript 𝜋 𝑘 𝑗 𝑛 \pi(i)=\pi^{k}(j)=n, π ​ ( i + 1) = π k ​ ( j + 1) = 1 𝜋 𝑖 1 superscript 𝜋 𝑘 𝑗 1 1 \pi(i+1)=\pi^{k}(j+1)=1. If there exists some 0 ≤ t ≤ i − 1 0 𝑡 𝑖 1 0\leq t\leq i-1, such that π ​ ( i − ℓ) = π k ​ ( j − ℓ) = n − ℓ 𝜋 𝑖 ℓ superscript 𝜋 𝑘 𝑗 ℓ 𝑛 ℓ \pi(i-\ell)=\pi^{k}(j-\ell)=n-\ell for all ℓ ∈ [t] ℓ delimited-[] 𝑡 \ell\in[t], and π ​ ( n) = π k ​ ( n) = n − t − 1 𝜋 𝑛 superscript 𝜋 𝑘 𝑛 𝑛 𝑡 1 \pi(n)=\pi^{k}(n)=n-t-1, then i = j 𝑖 𝑗 i=j and π k − 1 = id superscript 𝜋 𝑘 1 id \pi^{k-1}=\text{id}.

###### Proof.

Since π ​ ( n) = π k ​ ( n) = n − t − 1 𝜋 𝑛 superscript 𝜋 𝑘 𝑛 𝑛 𝑡 1 \pi(n)=\pi^{k}(n)=n-t-1, we have π k − 1 ​ ( n) = n superscript 𝜋 𝑘 1 𝑛 𝑛 \pi^{k-1}(n)=n. Thus, π k − 2 ​ ( n) = i superscript 𝜋 𝑘 2 𝑛 𝑖 \pi^{k-2}(n)=i as π ​ ( i) = n 𝜋 𝑖 𝑛 \pi(i)=n, and so π k − 1 ​ ( i) = i superscript 𝜋 𝑘 1 𝑖 𝑖 \pi^{k-1}(i)=i. However, we also have π k − 1 ​ ( j) = i superscript 𝜋 𝑘 1 𝑗 𝑖 \pi^{k-1}(j)=i as π k ​ ( j) = n superscript 𝜋 𝑘 𝑗 𝑛 \pi^{k}(j)=n. Hence, we must have i = j 𝑖 𝑗 i=j.

We now use induction to show that π k − 1 ​ ( n − ℓ) = n − ℓ superscript 𝜋 𝑘 1 𝑛 ℓ 𝑛 ℓ \pi^{k-1}(n-\ell)=n-\ell for all 0 ≤ ℓ ≤ n − 1 0 ℓ 𝑛 1 0\leq\ell\leq n-1, or equivalently π − 1 ​ ( n − ℓ) = π − k ​ ( n − ℓ) superscript 𝜋 1 𝑛 ℓ superscript 𝜋 𝑘 𝑛 ℓ \pi^{-1}(n-\ell)=\pi^{-k}(n-\ell). The case ℓ = 0 ℓ 0 \ell=0 follows from above. For all ℓ ∈ [t] ℓ delimited-[] 𝑡 \ell\in[t], since i = j 𝑖 𝑗 i=j, from assumption we have π ​ ( i − ℓ) = π k ​ ( i − ℓ) = n − ℓ 𝜋 𝑖 ℓ superscript 𝜋 𝑘 𝑖 ℓ 𝑛 ℓ \pi(i-\ell)=\pi^{k}(i-\ell)=n-\ell, and so π k − 1 ​ ( n − ℓ) = n − ℓ superscript 𝜋 𝑘 1 𝑛 ℓ 𝑛 ℓ \pi^{k-1}(n-\ell)=n-\ell. The case ℓ = t + 1 ℓ 𝑡 1 \ell=t+1 follows similarly from π ​ ( n) = π k ​ ( n) = n − t − 1 𝜋 𝑛 superscript 𝜋 𝑘 𝑛 𝑛 𝑡 1 \pi(n)=\pi^{k}(n)=n-t-1. Now assume r > t + 1 𝑟 𝑡 1 r>t+1 and π k − 1 ​ ( n − ℓ) = n − ℓ superscript 𝜋 𝑘 1 𝑛 ℓ 𝑛 ℓ \pi^{k-1}(n-\ell)=n-\ell for all 0 ≤ ℓ ≤ r − 1 0 ℓ 𝑟 1 0\leq\ell\leq r-1.

Let x, y 𝑥 𝑦 x,y be such that π ​ ( x) = π k ​ ( y) = n − r 𝜋 𝑥 superscript 𝜋 𝑘 𝑦 𝑛 𝑟 \pi(x)=\pi^{k}(y)=n-r. From induction hypothesis, π − 1 ​ ( n − ℓ) = π − k ​ ( n − ℓ) superscript 𝜋 1 𝑛 ℓ superscript 𝜋 𝑘 𝑛 ℓ \pi^{-1}(n-\ell)=\pi^{-k}(n-\ell) for all 0 ≤ ℓ ≤ r − 1 0 ℓ 𝑟 1 0\leq\ell\leq r-1. Let x 1 subscript 𝑥 1 x_{1} be the smallest index such that π ​ ( x 1) ∈ { n − r + 1, …, n } 𝜋 subscript 𝑥 1 𝑛 𝑟 1 … 𝑛 \pi(x_{1})\in\{n-r+1,\ldots,n\} and let x 2 subscript 𝑥 2 x_{2} be the smallest index larger than i + 1 𝑖 1 i+1 such that π ​ ( x 2) ∈ { n − r + 1, …, n } 𝜋 subscript 𝑥 2 𝑛 𝑟 1 … 𝑛 \pi(x_{2})\in\{n-r+1,\ldots,n\}. Since the unique descent of π 𝜋 \pi is at i 𝑖 i, we must have x, y ∈ { x 1 − 1, x 2 − 1 } 𝑥 𝑦 subscript 𝑥 1 1 subscript 𝑥 2 1 x,y\in\{x_{1}-1,x_{2}-1\}. If x = y 𝑥 𝑦 x=y, then π k − 1 ​ ( n − r) = n − r superscript 𝜋 𝑘 1 𝑛 𝑟 𝑛 𝑟 \pi^{k-1}(n-r)=n-r and we are done. Otherwise, x = x 2 − 1 𝑥 subscript 𝑥 2 1 x=x_{2}-1 or y = x 2 − 1 𝑦 subscript 𝑥 2 1 y=x_{2}-1. Since x 2 > i + 1 subscript 𝑥 2 𝑖 1 x_{2}>i+1, we have π ​ ( x 2) < ⋯ < π ​ ( n) = n − t − 1 𝜋 subscript 𝑥 2 ⋯ 𝜋 𝑛 𝑛 𝑡 1 \pi(x_{2})<\cdots<\pi(n)=n-t-1, which implies n − r + 1 ≤ π ​ ( x 2) ≤ x 2 − t − 1 𝑛 𝑟 1 𝜋 subscript 𝑥 2 subscript 𝑥 2 𝑡 1 n-r+1\leq\pi(x_{2})\leq x_{2}-t-1, and so x 2 − 1 ≥ n − r + 1 + t ≥ n − r + 1 subscript 𝑥 2 1 𝑛 𝑟 1 𝑡 𝑛 𝑟 1 x_{2}-1\geq n-r+1+t\geq n-r+1. If x = x 2 − 1 𝑥 subscript 𝑥 2 1 x=x_{2}-1, then from induction hypothesis, π k − 1 ​ ( x) = π k − 1 ​ ( x 2 − 1) = x 2 − 1 = x superscript 𝜋 𝑘 1 𝑥 superscript 𝜋 𝑘 1 subscript 𝑥 2 1 subscript 𝑥 2 1 𝑥 \pi^{k-1}(x)=\pi^{k-1}(x_{2}-1)=x_{2}-1=x, so n − r = π ​ ( x) = π k ​ ( x) 𝑛 𝑟 𝜋 𝑥 superscript 𝜋 𝑘 𝑥 n-r=\pi(x)=\pi^{k}(x) and π k − 1 ​ ( n − r) = n − r superscript 𝜋 𝑘 1 𝑛 𝑟 𝑛 𝑟 \pi^{k-1}(n-r)=n-r, as required. If y = x 2 − 1 𝑦 subscript 𝑥 2 1 y=x_{2}-1, then similarly, n − r = π k ​ ( y) = π ​ ( π k − 1 ​ ( y)) = π ​ ( y) 𝑛 𝑟 superscript 𝜋 𝑘 𝑦 𝜋 superscript 𝜋 𝑘 1 𝑦 𝜋 𝑦 n-r=\pi^{k}(y)=\pi(\pi^{k-1}(y))=\pi(y) and so π k − 1 ​ ( n − r) = n − r superscript 𝜋 𝑘 1 𝑛 𝑟 𝑛 𝑟 \pi^{k-1}(n-r)=n-r as well. This completes the induction and the proof that π k − 1 = id superscript 𝜋 𝑘 1 id \pi^{k-1}=\text{id}. ∎

###### Proof of Theorem 1.3.

It is clear that a Grassmanian permutation π ∈ 𝒮 n 𝜋 subscript 𝒮 𝑛 \pi\in\mathcal{S}_{n} satisfying π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1, π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n is of the form

 | π = π ​ ( 1) ​ … ​ π ​ ( i − 1) ​ n ​ 1 ​ π ​ ( i + 2) ​ … ​ π ​ ( n), 𝜋 𝜋 1 … 𝜋 𝑖 1 𝑛 1 𝜋 𝑖 2 … 𝜋 𝑛 \pi=\pi(1)\ldots\pi(i-1)n1\pi(i+2)\ldots\pi(n), |  |

where i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1], π ​ ( 1) < ⋯ < π ​ ( i − 1) 𝜋 1 ⋯ 𝜋 𝑖 1 \pi(1)<\cdots<\pi(i-1), and π ​ ( i + 2) < ⋯ < π ​ ( n) 𝜋 𝑖 2 ⋯ 𝜋 𝑛 \pi(i+2)<\cdots<\pi(n). Let π 𝜋 \pi be such a permutation satisfying des ⁡ ( π k) = 1 des superscript 𝜋 𝑘 1 \operatorname{des}({\pi^{k}})=1. From above, there exists i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1] such that π ​ ( i) = n 𝜋 𝑖 𝑛 \pi(i)=n and π ​ ( i + 1) = 1 𝜋 𝑖 1 1 \pi(i+1)=1.

###### Claim 3.2.

π k ​ ( 1) ≠ 1 superscript 𝜋 𝑘 1 1 \pi^{k}(1)\not=1 and π k ​ ( n) ≠ n superscript 𝜋 𝑘 𝑛 𝑛 \pi^{k}(n)\not=n.

###### Proof.

Assume for a contradiction that at least one of π k ​ ( 1) = 1 superscript 𝜋 𝑘 1 1 \pi^{k}(1)=1 and π k ​ ( n) = n superscript 𝜋 𝑘 𝑛 𝑛 \pi^{k}(n)=n holds. We first prove that in fact both have to hold simultaneously. Indeed, if π k ​ ( 1) = 1 superscript 𝜋 𝑘 1 1 \pi^{k}(1)=1 and π k ​ ( j) = n superscript 𝜋 𝑘 𝑗 𝑛 \pi^{k}(j)=n for some j ≠ n 𝑗 𝑛 j\not=n, then the unique descent of π k superscript 𝜋 𝑘 \pi^{k} is at j 𝑗 j. Note that π k − 1 ​ ( 1) = i + 1 superscript 𝜋 𝑘 1 1 𝑖 1 \pi^{k-1}(1)=i+1 as π ​ ( i + 1) = 1 𝜋 𝑖 1 1 \pi(i+1)=1. It follows that π k ​ ( i + 1) = i + 1 superscript 𝜋 𝑘 𝑖 1 𝑖 1 \pi^{k}(i+1)=i+1. If j ≥ i + 1 𝑗 𝑖 1 j\geq i+1, then we get π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i as 1 = π k ​ ( 1) < ⋯ < π k ​ ( i + 1) = i + 1 1 superscript 𝜋 𝑘 1 ⋯ superscript 𝜋 𝑘 𝑖 1 𝑖 1 1=\pi^{k}(1)<\cdots<\pi^{k}(i+1)=i+1. But this together with π ​ ( i) = n = π k ​ ( j) 𝜋 𝑖 𝑛 superscript 𝜋 𝑘 𝑗 \pi(i)=n=\pi^{k}(j) implies that π k − 1 ​ ( n) = i = π k − 1 ​ ( j) superscript 𝜋 𝑘 1 𝑛 𝑖 superscript 𝜋 𝑘 1 𝑗 \pi^{k-1}(n)=i=\pi^{k-1}(j), so j = n 𝑗 𝑛 j=n, contradiction. If j ≤ i 𝑗 𝑖 j\leq i, then from i + 1 = π k ​ ( i + 1) < ⋯ < π k ​ ( n) ≤ n 𝑖 1 superscript 𝜋 𝑘 𝑖 1 ⋯ superscript 𝜋 𝑘 𝑛 𝑛 i+1=\pi^{k}(i+1)<\cdots<\pi^{k}(n)\leq n, we get π k ​ ( n) = n superscript 𝜋 𝑘 𝑛 𝑛 \pi^{k}(n)=n, so again j = n 𝑗 𝑛 j=n, contradiction. The case when π k ​ ( n) = n superscript 𝜋 𝑘 𝑛 𝑛 \pi^{k}(n)=n and π k ​ ( j) = 1 superscript 𝜋 𝑘 𝑗 1 \pi^{k}(j)=1 for some j ≠ 1 𝑗 1 j\not=1 is similar, so we have both π k ​ ( 1) = 1 superscript 𝜋 𝑘 1 1 \pi^{k}(1)=1 and π k ​ ( n) = n superscript 𝜋 𝑘 𝑛 𝑛 \pi^{k}(n)=n. It follows from π ​ ( i) = n 𝜋 𝑖 𝑛 \pi(i)=n and π ​ ( i + 1) = 1 𝜋 𝑖 1 1 \pi(i+1)=1 that π k ​ ( i) = i superscript 𝜋 𝑘 𝑖 𝑖 \pi^{k}(i)=i and π k ​ ( i + 1) = i + 1 superscript 𝜋 𝑘 𝑖 1 𝑖 1 \pi^{k}(i+1)=i+1.

Suppose { π k ​ ( 2), …, π k ​ ( i − 1) } ≠ { 2, …, i − 1 } superscript 𝜋 𝑘 2 … superscript 𝜋 𝑘 𝑖 1 2 … 𝑖 1 \{\pi^{k}(2),\ldots,\pi^{k}(i-1)\}\not=\{2,\ldots,i-1\}, then let j 1 ∈ { 2, …, i − 1 } subscript 𝑗 1 2 … 𝑖 1 j_{1}\in\{2,\ldots,i-1\} be minimal such that π − k ​ ( j 1) > i + 1 superscript 𝜋 𝑘 subscript 𝑗 1 𝑖 1 \pi^{-k}(j_{1})>i+1 and let j 2 ∈ { i + 2, …, n − 1 } subscript 𝑗 2 𝑖 2 … 𝑛 1 j_{2}\in\{i+2,\ldots,n-1\} be maximal such that π − k ​ ( j 2) < i superscript 𝜋 𝑘 subscript 𝑗 2 𝑖 \pi^{-k}(j_{2})<i. Then π k superscript 𝜋 𝑘 \pi^{k} has descents at both π − k ​ ( j 1) − 1 superscript 𝜋 𝑘 subscript 𝑗 1 1 \pi^{-k}(j_{1})-1 and π − k ​ ( j 2) superscript 𝜋 𝑘 subscript 𝑗 2 \pi^{-k}(j_{2}), contradicting des ⁡ ( π k) = 1 des superscript 𝜋 𝑘 1 \operatorname{des}(\pi^{k})=1. Thus { π k ​ ( 2), …, π k ​ ( i − 1) } = { 2, …, i − 1 } superscript 𝜋 𝑘 2 … superscript 𝜋 𝑘 𝑖 1 2 … 𝑖 1 \{\pi^{k}(2),\ldots,\pi^{k}(i-1)\}=\{2,\ldots,i-1\} and { π k ​ ( i + 2), …, π k ​ ( n − 1) } = { i + 2, …, n − 1 } superscript 𝜋 𝑘 𝑖 2 … superscript 𝜋 𝑘 𝑛 1 𝑖 2 … 𝑛 1 \{\pi^{k}(i+2),\ldots,\pi^{k}(n-1)\}=\{i+2,\ldots,n-1\}.

We now show that π k = id superscript 𝜋 𝑘 id \pi^{k}=\text{id}, which contradicts des ⁡ ( π k) = 1 des superscript 𝜋 𝑘 1 \operatorname{des}(\pi^{k})=1 and proves the claim. First, we use induction to show that π k ​ ( ℓ) = ℓ superscript 𝜋 𝑘 ℓ ℓ \pi^{k}(\ell)=\ell for all 1 ≤ ℓ ≤ i − 1 1 ℓ 𝑖 1 1\leq\ell\leq i-1. The base case ℓ = 1 ℓ 1 \ell=1 follows from assumption. Suppose this is true for all 1 ≤ ℓ ≤ t < i − 1 1 ℓ 𝑡 𝑖 1 1\leq\ell\leq t<i-1, and suppose for a contradiction that π k ​ ( j) = t + 1 superscript 𝜋 𝑘 𝑗 𝑡 1 \pi^{k}(j)=t+1 for some j > t + 1 𝑗 𝑡 1 j>t+1. Note that j < i − 1 𝑗 𝑖 1 j<i-1 and the unique descent of π k superscript 𝜋 𝑘 \pi^{k} must be at j − 1 𝑗 1 j-1. It follows that π k ​ ( ℓ) = ℓ superscript 𝜋 𝑘 ℓ ℓ \pi^{k}(\ell)=\ell for all ℓ ≥ i ℓ 𝑖 \ell\geq i. Let x 𝑥 x be such that π ​ ( x) = t + 1 𝜋 𝑥 𝑡 1 \pi(x)=t+1, then π k − 1 ​ ( j) = x superscript 𝜋 𝑘 1 𝑗 𝑥 \pi^{k-1}(j)=x. Since π 𝜋 \pi has exactly one descent which is at i 𝑖 i, and π ​ ( 1) ≥ 2 𝜋 1 2 \pi(1)\geq 2, we must have x ≤ t 𝑥 𝑡 x\leq t or x ≥ i + 2 𝑥 𝑖 2 x\geq i+2. If x ≤ t 𝑥 𝑡 x\leq t, then from induction hypothesis, we have π k ​ ( x) = x superscript 𝜋 𝑘 𝑥 𝑥 \pi^{k}(x)=x. But then π k − 1 ​ ( t + 1) = x superscript 𝜋 𝑘 1 𝑡 1 𝑥 \pi^{k-1}(t+1)=x as well, so j = t + 1 𝑗 𝑡 1 j=t+1, contradiction. If x ≥ i + 2 𝑥 𝑖 2 x\geq i+2, then π k ​ ( x) = x superscript 𝜋 𝑘 𝑥 𝑥 \pi^{k}(x)=x from above, so again π k − 1 ​ ( t + 1) = x superscript 𝜋 𝑘 1 𝑡 1 𝑥 \pi^{k-1}(t+1)=x and j = t + 1 𝑗 𝑡 1 j=t+1, contradiction. Similarly, we can use induction to show that π k ​ ( ℓ) = ℓ superscript 𝜋 𝑘 ℓ ℓ \pi^{k}(\ell)=\ell for all i + 1 ≤ ℓ ≤ n 𝑖 1 ℓ 𝑛 i+1\leq\ell\leq n, so π k = id superscript 𝜋 𝑘 id \pi^{k}=\text{id}, as required. ∎

From 3.2, there exists j ∈ [n − 1] 𝑗 delimited-[] 𝑛 1 j\in[n-1] such that π k ​ ( j) = n superscript 𝜋 𝑘 𝑗 𝑛 \pi^{k}(j)=n and π k ​ ( j + 1) = 1 superscript 𝜋 𝑘 𝑗 1 1 \pi^{k}(j+1)=1. Suppose that π k − 1 ≠ id superscript 𝜋 𝑘 1 id \pi^{k-1}\not=\text{id}, we show that π 𝜋 \pi is a cyclic shift permutation.

First assume that i ≤ j 𝑖 𝑗 i\leq j. We use induction on ℓ ℓ \ell to show that π ​ ( i − ℓ) = π k ​ ( j − ℓ) = n − ℓ 𝜋 𝑖 ℓ superscript 𝜋 𝑘 𝑗 ℓ 𝑛 ℓ \pi(i-\ell)=\pi^{k}(j-\ell)=n-\ell for all 0 ≤ ℓ ≤ i − 1 0 ℓ 𝑖 1 0\leq\ell\leq i-1. Assuming this, we have { π ​ ( i + 2), …, π ​ ( n) } = { 2, …, n − i } 𝜋 𝑖 2 … 𝜋 𝑛 2 … 𝑛 𝑖 \{\pi(i+2),\ldots,\pi(n)\}=\{2,\ldots,n-i\}. It then follows from π ​ ( i + 2) < ⋯ < π ​ ( n) 𝜋 𝑖 2 ⋯ 𝜋 𝑛 \pi(i+2)<\cdots<\pi(n) that π ​ ( i + t) = t 𝜋 𝑖 𝑡 𝑡 \pi(i+t)=t for 2 ≤ t ≤ n − i 2 𝑡 𝑛 𝑖 2\leq t\leq n-i, and thus that π 𝜋 \pi is the cyclic shift permutation given by π ​ ( ℓ) ≡ ℓ + n − i ( mod n) 𝜋 ℓ annotated ℓ 𝑛 𝑖 pmod 𝑛 \pi(\ell)\equiv\ell+n-i\pmod{n}, as required.

The base case ℓ = 0 ℓ 0 \ell=0 follows from assumptions. Now assume this has been proved for all 0 ≤ ℓ ≤ t < i − 1 0 ℓ 𝑡 𝑖 1 0\leq\ell\leq t<i-1, and assume for a contradiction that π ​ ( i − t − 1) = π k ​ ( j − t − 1) = n − t − 1 𝜋 𝑖 𝑡 1 superscript 𝜋 𝑘 𝑗 𝑡 1 𝑛 𝑡 1 \pi(i-t-1)=\pi^{k}(j-t-1)=n-t-1 is not true. Note that as π 𝜋 \pi and π k superscript 𝜋 𝑘 \pi^{k} both have exactly one descent, we must have either π ​ ( i − t − 1) = n − t − 1 𝜋 𝑖 𝑡 1 𝑛 𝑡 1 \pi(i-t-1)=n-t-1 or π ​ ( n) = n − t − 1 𝜋 𝑛 𝑛 𝑡 1 \pi(n)=n-t-1, and either π k ​ ( j − t − 1) = n − t − 1 superscript 𝜋 𝑘 𝑗 𝑡 1 𝑛 𝑡 1 \pi^{k}(j-t-1)=n-t-1 or π k ​ ( n) = n − t − 1 superscript 𝜋 𝑘 𝑛 𝑛 𝑡 1 \pi^{k}(n)=n-t-1.

Case 1. π ​ ( n) = n − t − 1 𝜋 𝑛 𝑛 𝑡 1 \pi(n)=n-t-1 and π k ​ ( n) = n − t − 1 superscript 𝜋 𝑘 𝑛 𝑛 𝑡 1 \pi^{k}(n)=n-t-1. Then by Lemma 3.1, π k − 1 = id superscript 𝜋 𝑘 1 id \pi^{k-1}=\text{id}, contradiction.

Case 2. π ​ ( n) = n − t − 1 𝜋 𝑛 𝑛 𝑡 1 \pi(n)=n-t-1 and π k ​ ( j − t − 1) = n − t − 1 superscript 𝜋 𝑘 𝑗 𝑡 1 𝑛 𝑡 1 \pi^{k}(j-t-1)=n-t-1. It follows that π k − 1 ​ ( j − t − 1) = n superscript 𝜋 𝑘 1 𝑗 𝑡 1 𝑛 \pi^{k-1}(j-t-1)=n, and so π ​ ( j) = j − t − 1 𝜋 𝑗 𝑗 𝑡 1 \pi(j)=j-t-1 as π k ​ ( j) = n superscript 𝜋 𝑘 𝑗 𝑛 \pi^{k}(j)=n. Since j − t − 1 ≠ n 𝑗 𝑡 1 𝑛 j-t-1\not=n and π ​ ( i) = n 𝜋 𝑖 𝑛 \pi(i)=n, we have j ≠ i 𝑗 𝑖 j\not=i and so j ≥ i + 1 𝑗 𝑖 1 j\geq i+1. It follows that j − t − 1 = π ​ ( j) < ⋯ < π ​ ( n) = n − t − 1 𝑗 𝑡 1 𝜋 𝑗 ⋯ 𝜋 𝑛 𝑛 𝑡 1 j-t-1=\pi(j)<\cdots<\pi(n)=n-t-1, so we must have π ​ ( j + ℓ) = j − t − 1 + ℓ 𝜋 𝑗 ℓ 𝑗 𝑡 1 ℓ \pi(j+\ell)=j-t-1+\ell for all 0 ≤ ℓ ≤ n − j 0 ℓ 𝑛 𝑗 0\leq\ell\leq n-j. In particular, π ​ ( j + 1) = j − t 𝜋 𝑗 1 𝑗 𝑡 \pi(j+1)=j-t. Since π k ​ ( j + 1) = 1 superscript 𝜋 𝑘 𝑗 1 1 \pi^{k}(j+1)=1, we have π k − 1 ​ ( j − t) = 1 superscript 𝜋 𝑘 1 𝑗 𝑡 1 \pi^{k-1}(j-t)=1 and so π k ​ ( j − t) = π ​ ( 1) superscript 𝜋 𝑘 𝑗 𝑡 𝜋 1 \pi^{k}(j-t)=\pi(1). But from induction hypothesis, π k ​ ( j − t) = n − t = π ​ ( i − t) superscript 𝜋 𝑘 𝑗 𝑡 𝑛 𝑡 𝜋 𝑖 𝑡 \pi^{k}(j-t)=n-t=\pi(i-t), so π ​ ( 1) = n − t = π ​ ( i − t) 𝜋 1 𝑛 𝑡 𝜋 𝑖 𝑡 \pi(1)=n-t=\pi(i-t), and thus i − t = 1 𝑖 𝑡 1 i-t=1, contradiction.

Case 3. π ​ ( i − t − 1) = n − t − 1 𝜋 𝑖 𝑡 1 𝑛 𝑡 1 \pi(i-t-1)=n-t-1 and π k ​ ( n) = n − t − 1 superscript 𝜋 𝑘 𝑛 𝑛 𝑡 1 \pi^{k}(n)=n-t-1. Then, π k − 1 ​ ( n) = i − t − 1 superscript 𝜋 𝑘 1 𝑛 𝑖 𝑡 1 \pi^{k-1}(n)=i-t-1, and from π ​ ( i) = n 𝜋 𝑖 𝑛 \pi(i)=n we get π k ​ ( i) = i − t − 1 superscript 𝜋 𝑘 𝑖 𝑖 𝑡 1 \pi^{k}(i)=i-t-1. But as i ≤ j 𝑖 𝑗 i\leq j, we have 1 ≤ π k ​ ( 1) < ⋯ < π k ​ ( i) = i − t − 1 < i 1 superscript 𝜋 𝑘 1 ⋯ superscript 𝜋 𝑘 𝑖 𝑖 𝑡 1 𝑖 1\leq\pi^{k}(1)<\cdots<\pi^{k}(i)=i-t-1<i, contradiction.

If i > j 𝑖 𝑗 i>j, we can similarly use induction to show that π ​ ( i + ℓ) = π k ​ ( j + ℓ) = ℓ 𝜋 𝑖 ℓ superscript 𝜋 𝑘 𝑗 ℓ ℓ \pi(i+\ell)=\pi^{k}(j+\ell)=\ell for all 1 ≤ ℓ ≤ n − i 1 ℓ 𝑛 𝑖 1\leq\ell\leq n-i, which again implies that π 𝜋 \pi is the cyclic shift given by π ​ ( ℓ) ≡ ℓ + n − i ( mod n) 𝜋 ℓ annotated ℓ 𝑛 𝑖 pmod 𝑛 \pi(\ell)\equiv\ell+n-i\pmod{n}, as required. ∎

By Theorem 1.3, and as cyclic shifts are easy to handle, it suffices now to prove Theorem 1.4, which counts the number of k 𝑘 k -th roots of the identity permutation that are Grassmanian. This generalises the essence of [1, Thm. 2.3, 3.1], where the k = 2, 3 𝑘 2 3 k=2,3 cases are solved.

We call a permutation whose cycle decomposition is a single cycle of length n 𝑛 n an n 𝑛 n -cycle. Note that an n 𝑛 n -cycle π 𝜋 \pi, where n > 1 𝑛 1 n>1, automatically satisfies π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1 and π ​ ( n) ≠ n. 𝜋 𝑛 𝑛 \pi(n)\not=n. We first prove a series of lemmas about Grassmanian n 𝑛 n -cycles.

###### Lemma 3.3.

[2, Thm. 9.4] For all 1 ≤ i ≤ n − 1 1 𝑖 𝑛 1 1\leq i\leq n-1, the number of n 𝑛 n -cycles with a unique descent at position i 𝑖 i is

 | 1 n ​ ∑ d ∣ gcd ⁡ ( i, n) μ ​ ( d) ​ ( n / d i / d). 1 𝑛 subscript conditional 𝑑 𝑖 𝑛 𝜇 𝑑 binomial 𝑛 𝑑 𝑖 𝑑 \frac{1}{n}\sum_{d\mid\gcd(i,n)}\mu(d)\binom{n/d}{i/d}. |  |

###### Lemma 3.4.

The number N n subscript 𝑁 𝑛 N_{n} of Grassmanian n 𝑛 n -cycles is

 | 1 n ​ ∑ d ∣ n, d ≠ n μ ​ ( d) ​ ( 2 n d − 2). 1 𝑛 subscript conditional 𝑑 𝑛 𝑑 𝑛 𝜇 𝑑 superscript 2 𝑛 𝑑 2 \frac{1}{n}\sum_{d\mid n,d\not=n}\mu(d)(2^{\frac{n}{d}}-2). |  |

In particular, if n = p 𝑛 𝑝 n=p is prime, then N p = 1 p ​ ( 2 p − 2) subscript 𝑁 𝑝 1 𝑝 superscript 2 𝑝 2 N_{p}=\frac{1}{p}(2^{p}-2).

###### Proof.

Every Grassmanian n 𝑛 n -cycle has a unique descent at some index i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1], so by Lemma 3.3,

 | N n = 1 n ​ ∑ i = 1 n − 1 ∑ d ∣ gcd ⁡ ( i, n) μ ​ ( d) ​ ( n / d i / d) = 1 n ​ ∑ d ∣ n, d ≠ n μ ​ ( d) ​ ∑ i = 1 n d − 1 ( n / d i) = 1 n ​ ∑ d ∣ n, d ≠ n μ ​ ( d) ​ ( 2 n d − 2). subscript 𝑁 𝑛 1 𝑛 superscript subscript 𝑖 1 𝑛 1 subscript conditional 𝑑 𝑖 𝑛 𝜇 𝑑 binomial 𝑛 𝑑 𝑖 𝑑 1 𝑛 subscript conditional 𝑑 𝑛 𝑑 𝑛 𝜇 𝑑 superscript subscript 𝑖 1 𝑛 𝑑 1 binomial 𝑛 𝑑 𝑖 1 𝑛 subscript conditional 𝑑 𝑛 𝑑 𝑛 𝜇 𝑑 superscript 2 𝑛 𝑑 2 N_{n}=\frac{1}{n}\sum_{i=1}^{n-1}\sum_{d\mid\gcd(i,n)}\mu(d)\binom{n/d}{i/d}=\frac{1}{n}\sum_{d\mid n,d\not=n}\mu(d)\sum_{i=1}^{\frac{n}{d}-1}\binom{n/d}{i}=\frac{1}{n}\sum_{d\mid n,d\not=n}\mu(d)(2^{\frac{n}{d}}-2). |  |

When n = p 𝑛 𝑝 n=p is a prime number, the sum above contains only one term and equals 1 p ​ ( 2 p − 2) 1 𝑝 superscript 2 𝑝 2 \frac{1}{p}(2^{p}-2). ∎

###### Lemma 3.5.

Let α ∈ 𝒮 r, β ∈ 𝒮 s formulae-sequence 𝛼 subscript 𝒮 𝑟 𝛽 subscript 𝒮 𝑠 \alpha\in\mathcal{S}_{r},\beta\in\mathcal{S}_{s} be Grassmanian permutations with no fixed point. Then, there exists a Grassmanian permutation π ∈ 𝒮 r + s 𝜋 subscript 𝒮 𝑟 𝑠 \pi\in\mathcal{S}_{r+s} with a partition [r + s] = A ∪ B delimited-[] 𝑟 𝑠 𝐴 𝐵 [r+s]=A\cup B, such that the restrictions of π 𝜋 \pi to A 𝐴 A and B 𝐵 B are permutations isomorphic to α 𝛼 \alpha and β 𝛽 \beta, respectively.

###### Proof.

To distinguish it from α 𝛼 \alpha, we view β 𝛽 \beta as a permutation on the set [s ¯] = { 1 ¯, 2 ¯, …, s ¯ } delimited-[] ¯ 𝑠 ¯ 1 ¯ 2 … ¯ 𝑠 [\overline{s}]=\{\overline{1},\overline{2},\ldots,\overline{s}\}. For notational convenience, define f: [r] ∪ [s ¯] → [r] ∪ [s ¯]: 𝑓 → delimited-[] 𝑟 delimited-[] ¯ 𝑠 delimited-[] 𝑟 delimited-[] ¯ 𝑠 f:[r]\cup[\overline{s}]\to[r]\cup[\overline{s}] by f ​ ( i) = α ​ ( i) 𝑓 𝑖 𝛼 𝑖 f(i)=\alpha(i) for i ∈ [r] 𝑖 delimited-[] 𝑟 i\in[r] and f ​ ( i ¯) = β ​ ( i ¯) 𝑓 ¯ 𝑖 𝛽 ¯ 𝑖 f(\overline{i})=\beta(\overline{i}) for i ¯ ∈ [s ¯] ¯ 𝑖 delimited-[] ¯ 𝑠 \overline{i}\in[\overline{s}]. Suppose α ​ ( t) = r, α ​ ( t + 1) = 1 formulae-sequence 𝛼 𝑡 𝑟 𝛼 𝑡 1 1 \alpha(t)=r,\alpha(t+1)=1 and β ​ ( m ¯) = s ¯, β ​ ( m + 1 ¯) = 1 ¯ formulae-sequence 𝛽 ¯ 𝑚 ¯ 𝑠 𝛽 ¯ 𝑚 1 ¯ 1 \beta(\overline{m})=\overline{s},\beta(\overline{m+1})=\overline{1}.

After relabelling each x i subscript 𝑥 𝑖 x_{i} to i 𝑖 i, the desired permutation π 𝜋 \pi is equivalent to an ordering x 1 ≺ x 2 ≺ ⋯ ≺ x r + s precedes subscript 𝑥 1 subscript 𝑥 2 precedes ⋯ precedes subscript 𝑥 𝑟 𝑠 x_{1}\prec x_{2}\prec\cdots\prec x_{r+s} of the elements in [r] ∪ [s ¯] delimited-[] 𝑟 delimited-[] ¯ 𝑠 [r]\cup[\overline{s}], such that the elements in [r] delimited-[] 𝑟 [r] and the elements in [s ¯] delimited-[] ¯ 𝑠 [\overline{s}] are still ordered in the usual way, and the sequence f ​ ( x 1), f ​ ( x 2), …, f ​ ( x r + s) 𝑓 subscript 𝑥 1 𝑓 subscript 𝑥 2 … 𝑓 subscript 𝑥 𝑟 𝑠 f(x_{1}),f(x_{2}),\ldots,f(x_{r+s}) has exactly one descent in this ordering ≺ precedes \prec. Note that as t ≺ t + 1 precedes 𝑡 𝑡 1 t\prec t+1 and f ​ ( t + 1) = α ​ ( t + 1) ≺ α ​ ( t) = f ​ ( t) 𝑓 𝑡 1 𝛼 𝑡 1 precedes 𝛼 𝑡 𝑓 𝑡 f(t+1)=\alpha(t+1)\prec\alpha(t)=f(t), there must be a descent somewhere between t 𝑡 t and t + 1 𝑡 1 t+1. Similarly, there is a descent between m ¯ ¯ 𝑚 \overline{m} and m + 1 ¯ ¯ 𝑚 1 \overline{m+1}. Hence, for f ​ ( x 1), f ​ ( x 2), …, f ​ ( x r + s) 𝑓 subscript 𝑥 1 𝑓 subscript 𝑥 2 … 𝑓 subscript 𝑥 𝑟 𝑠 f(x_{1}),f(x_{2}),\ldots,f(x_{r+s}) to have at most one descent, we must have t ≺ m + 1 ¯ precedes 𝑡 ¯ 𝑚 1 t\prec\overline{m+1} and m ¯ ≺ t + 1 precedes ¯ 𝑚 𝑡 1 \overline{m}\prec t+1, and that the unique descent is at x t + m subscript 𝑥 𝑡 𝑚 x_{t+m}. It follows that the smallest t + m 𝑡 𝑚 t+m elements under ≺ precedes \prec must be [t] ∪ [m ¯] delimited-[] 𝑡 delimited-[] ¯ 𝑚 [t]\cup[\overline{m}], and we call them the first part of ≺ precedes \prec. The largest r + s − t − m 𝑟 𝑠 𝑡 𝑚 r+s-t-m elements under ≺ precedes \prec are called the second part of ≺ precedes \prec.

We construct such an ordering with the following process. Start with the ordering 1 ≺ 2 ≺ ⋯ ≺ t ≺ 1 ¯ ≺ 2 ¯ ≺ ⋯ ≺ m ¯ ≺ t + 1 ≺ ⋯ ≺ r ≺ m + 1 ¯ ≺ ⋯ ≺ s ¯ precedes 1 2 precedes ⋯ precedes 𝑡 precedes ¯ 1 precedes ¯ 2 precedes ⋯ precedes ¯ 𝑚 precedes 𝑡 1 precedes ⋯ precedes 𝑟 precedes ¯ 𝑚 1 precedes ⋯ precedes ¯ 𝑠 1\prec 2\prec\cdots\prec t\prec\overline{1}\prec\overline{2}\prec\cdots\prec\overline{m}\prec t+1\prec\cdots\prec r\prec\overline{m+1}\prec\cdots\prec\overline{s}. In every step, if within the same part of ≺ precedes \prec there is some i 𝑖 i immediately preceding some j ¯ ¯ 𝑗 \overline{j}, but f ​ ( i) ≻ f ​ ( j ¯) succeeds 𝑓 𝑖 𝑓 ¯ 𝑗 f(i)\succ f(\overline{j}), then we swap the order of i 𝑖 i and j ¯ ¯ 𝑗 \overline{j} in ≺ precedes \prec. Since elements in [r] delimited-[] 𝑟 [r] are only ever moved up in the ordering ≺ precedes \prec, if at some point during the process we have i ≻ j ¯ succeeds 𝑖 ¯ 𝑗 i\succ\overline{j}, then this is true from then on. Also, if within the same part we have i ≻ j ¯ succeeds 𝑖 ¯ 𝑗 i\succ\overline{j} at some point, then i 𝑖 i must have been swapped with j ¯ ¯ 𝑗 \overline{j} in some previous step, so from that point on we have f ​ ( i) ≻ f ​ ( j ¯) succeeds 𝑓 𝑖 𝑓 ¯ 𝑗 f(i)\succ f(\overline{j}).

This process must terminate. If it ends with 1 ¯ ≺ 2 ¯ ≺ ⋯ ≺ m ¯ ≺ 1 ≺ 2 ≺ ⋯ ≺ t ≺ m + 1 ¯ ≺ ⋯ ≺ s ¯ ≺ t + 1 ≺ ⋯ ≺ r precedes ¯ 1 ¯ 2 precedes ⋯ precedes ¯ 𝑚 precedes 1 precedes 2 precedes ⋯ precedes 𝑡 precedes ¯ 𝑚 1 precedes ⋯ precedes ¯ 𝑠 precedes 𝑡 1 precedes ⋯ precedes 𝑟 \overline{1}\prec\overline{2}\prec\cdots\prec\overline{m}\prec 1\prec 2\prec\cdots\prec t\prec\overline{m+1}\prec\cdots\prec\overline{s}\prec t+1\prec\cdots\prec r, then from the observation above f ​ ( x 1), f ​ ( x 2), …, f ​ ( x r + s) 𝑓 subscript 𝑥 1 𝑓 subscript 𝑥 2 … 𝑓 subscript 𝑥 𝑟 𝑠 f(x_{1}),f(x_{2}),\ldots,f(x_{r+s}) has exactly one descent. If the process ends earlier because no further swap is needed, then from the definition of swaps, f 𝑓 f is increasing within both parts, and thus has exactly one descent. ∎

###### Example 3.6.

Let α = 231 𝛼 231 \alpha=231 and β = 2 ¯ ​ 5 ¯ ​ 1 ¯ ​ 3 ¯ ​ 4 ¯ 𝛽 ¯ 2 ¯ 5 ¯ 1 ¯ 3 ¯ 4 \beta=\overline{2}\overline{5}\overline{1}\overline{3}\overline{4}. The process above starts with 2 ≺ 3 ≺ 2 ¯ ≺ 5 ¯ ≺ 1 ≺ 1 ¯ ≺ 3 ¯ ≺ 4 ¯ precedes 2 3 precedes ¯ 2 precedes ¯ 5 precedes 1 precedes ¯ 1 precedes ¯ 3 precedes ¯ 4 2\prec 3\prec\overline{2}\prec\overline{5}\prec 1\prec\overline{1}\prec\overline{3}\prec\overline{4}. The first step swaps 3 3 3 and 2 ¯ ¯ 2 \overline{2}, and changes it to 2 ≺ 2 ¯ ≺ 3 ≺ 5 ¯ ≺ 1 ≺ 1 ¯ ≺ 3 ¯ ≺ 4 ¯ precedes 2 ¯ 2 precedes 3 precedes ¯ 5 precedes 1 precedes ¯ 1 precedes ¯ 3 precedes ¯ 4 2\prec\overline{2}\prec 3\prec\overline{5}\prec 1\prec\overline{1}\prec\overline{3}\prec\overline{4}, because α ​ ( 3) = 1 ≻ 5 ¯ = β ​ ( 2 ¯) 𝛼 3 1 succeeds ¯ 5 𝛽 ¯ 2 \alpha(3)=1\succ\overline{5}=\beta(\overline{2}). The process now terminates as no more swap is needed. By relabelling, we get the desired permutation π = 34581267 𝜋 34581267 \pi=34581267, which indeed has exactly one descent.

###### Lemma 3.7.

Given distinct Grassmanian cycles α, β 𝛼 𝛽 \alpha,\beta of length at least two, there is at most one Grassmanian permutation which decomposes exactly into two cycles isomorphic to α 𝛼 \alpha and β 𝛽 \beta.

###### Proof.

We use the same notations as in the proof of Lemma 3.5. Suppose ≺ 1, ≺ 2 subscript precedes 1 subscript precedes 2 \prec_{1},\prec_{2} are two different orderings that would produce two distinct Grassmanian permutations satisfying the required conditions. As proved before, ≺ 1, ≺ 2 subscript precedes 1 subscript precedes 2 \prec_{1},\prec_{2} have the same first part and the same second part.

Suppose i ∈ [r] 𝑖 delimited-[] 𝑟 i\in[r] is the index that maximises v 2 − v 1 subscript 𝑣 2 subscript 𝑣 1 v_{2}-v_{1}, where v 1 subscript 𝑣 1 v_{1} is the number of elements in [s ¯] delimited-[] ¯ 𝑠 [\overline{s}] that i 𝑖 i is greater than under ≺ 1 subscript precedes 1 \prec_{1}, or equivalently the unique element such that v 1 ¯ ≺ 1 i ≺ 1 v 1 + 1 ¯ subscript precedes 1 ¯ subscript 𝑣 1 𝑖 subscript precedes 1 ¯ subscript 𝑣 1 1 \overline{v_{1}}\prec_{1}i\prec_{1}\overline{v_{1}+1}, and similarly for v 2 subscript 𝑣 2 v_{2}. Let j 𝑗 j be this maximum, and note we can assume without loss of generality that j ≥ 1 𝑗 1 j\geq 1, which means that i 𝑖 i surpasses j 𝑗 j additional elements of [s ¯] delimited-[] ¯ 𝑠 [\overline{s}] when we go from ≺ 1 subscript precedes 1 \prec_{1} to ≺ 2 subscript precedes 2 \prec_{2}. Since i 𝑖 i is in the same part of ≺ 1 subscript precedes 1 \prec_{1} and ≺ 2 subscript precedes 2 \prec_{2} and f 𝑓 f is increasing in that part, it follows that α ​ ( i) 𝛼 𝑖 \alpha(i) also surpasses at least j 𝑗 j elements of [s ¯] delimited-[] ¯ 𝑠 [\overline{s}], and thus exactly j 𝑗 j by maximality. Repeating the argument, since α 𝛼 \alpha is a cycle, α k ​ ( i) superscript 𝛼 𝑘 𝑖 \alpha^{k}(i) attains all values of α 𝛼 \alpha, so each i ∈ [r] 𝑖 delimited-[] 𝑟 i\in[r] surpasses exactly j 𝑗 j elements of [s ¯] delimited-[] ¯ 𝑠 [\overline{s}] going from ≺ 1 subscript precedes 1 \prec_{1} to ≺ 2 subscript precedes 2 \prec_{2}. By symmetry, there is some j ′ ≥ 1 superscript 𝑗 ′ 1 j^{\prime}\geq 1 such that each i ¯ ∈ [s ¯] ¯ 𝑖 delimited-[] ¯ 𝑠 \overline{i}\in[\overline{s}] is surpassed by j ′ superscript 𝑗 ′ j^{\prime} elements of [r] delimited-[] 𝑟 [r].

It follows that ≺ 1, ≺ 2 subscript precedes 1 subscript precedes 2 \prec_{1},\prec_{2} both consists of groups of j + j ′ 𝑗 superscript 𝑗 ′ j+j^{\prime} elements, where in ≺ 1 subscript precedes 1 \prec_{1} each group begins with a block of j ′ superscript 𝑗 ′ j^{\prime} elements in [r] delimited-[] 𝑟 [r] and ends with a block of j 𝑗 j elements in [s ¯] delimited-[] ¯ 𝑠 [\overline{s}], and in ≺ 2 subscript precedes 2 \prec_{2} the two blocks in each group of ≺ 1 subscript precedes 1 \prec_{1} are swapped. Since these are the only order swaps, α 𝛼 \alpha must send each block of j ′ superscript 𝑗 ′ j^{\prime} elements in [r] delimited-[] 𝑟 [r] to another block of j ′ superscript 𝑗 ′ j^{\prime} elements in [r] delimited-[] 𝑟 [r]. As α 𝛼 \alpha is increasing in each block, it follows that if i 𝑖 i is the ℓ ℓ \ell -th element in a block, then so is α ​ ( i) 𝛼 𝑖 \alpha(i). Repeating this argument shows that for every ℓ ∈ [j ′] ℓ delimited-[] superscript 𝑗 ′ \ell\in[j^{\prime}], α 𝛼 \alpha only sends the ℓ ℓ \ell -th elements in these block to each other, contradicting α 𝛼 \alpha is a cycle if j ′ > 1 superscript 𝑗 ′ 1 j^{\prime}>1. Similarly, j > 1 𝑗 1 j>1 would contradict that β 𝛽 \beta is a cycle. Therefore, we must have j = j ′ = 1 𝑗 superscript 𝑗 ′ 1 j=j^{\prime}=1, and so r = s 𝑟 𝑠 r=s. We show that α 𝛼 \alpha is isomorphic to β 𝛽 \beta, which is a contradiction. Indeed, for every i ∈ [r] 𝑖 delimited-[] 𝑟 i\in[r], the groups containing i 𝑖 i is just i 𝑖 i and i ¯ ¯ 𝑖 \overline{i}. Going from ≺ 1 subscript precedes 1 \prec_{1} to ≺ 2 subscript precedes 2 \prec_{2}, i 𝑖 i swapped with i ¯ ¯ 𝑖 \overline{i}, so α ​ ( i) 𝛼 𝑖 \alpha(i) swapped with β ​ ( i ¯) 𝛽 ¯ 𝑖 \beta(\overline{i}), implying that they are in the same group and hence α ​ ( i) ¯ = β ​ ( i ¯) ¯ 𝛼 𝑖 𝛽 ¯ 𝑖 \overline{\alpha(i)}=\beta(\overline{i}). ∎

###### Example 3.8.

A situation where j = 1, j ′ = 2 formulae-sequence 𝑗 1 superscript 𝑗 ′ 2 j=1,j^{\prime}=2 could be 3 ≺ 1 4 ≺ 1 2 ¯ ≺ 1 5 ≺ 1 6 ≺ 1 3 ¯ ≺ 1 1 ≺ 1 2 ≺ 1 1 ¯ subscript precedes 1 3 4 subscript precedes 1 ¯ 2 subscript precedes 1 5 subscript precedes 1 6 subscript precedes 1 ¯ 3 subscript precedes 1 1 subscript precedes 1 2 subscript precedes 1 ¯ 1 3\prec_{1}4\prec_{1}\overline{2}\prec_{1}5\prec_{1}6\prec_{1}\overline{3}\prec_{1}1\prec_{1}2\prec_{1}\overline{1} and 2 ¯ ≺ 2 3 ≺ 2 4 ≺ 2 3 ¯ ≺ 2 5 ≺ 2 6 ≺ 2 1 ¯ ≺ 2 1 ≺ 2 2 subscript precedes 2 ¯ 2 3 subscript precedes 2 4 subscript precedes 2 ¯ 3 subscript precedes 2 5 subscript precedes 2 6 subscript precedes 2 ¯ 1 subscript precedes 2 1 subscript precedes 2 2 \overline{2}\prec_{2}3\prec_{2}4\prec_{2}\overline{3}\prec_{2}5\prec_{2}6\prec_{2}\overline{1}\prec_{2}1\prec_{2}2. It follows that α 𝛼 \alpha must send 3, 5, 1 3 5 1 3,5,1 to each other and 4, 6, 2 4 6 2 4,6,2 to each other, and thus is not a 6-cycle.

###### Proof of Theorem 1.4.

The cycle decomposition of a permutation π 𝜋 \pi for which π k = id superscript 𝜋 𝑘 id \pi^{k}=\text{id} only contains cycles whose lengths are divisors of k 𝑘 k. Since π 𝜋 \pi is Grassmanian, every cycle has to be Grassmanian. Also, π ​ ( 1) ≠ 1 𝜋 1 1 \pi(1)\not=1, π ​ ( n) ≠ n 𝜋 𝑛 𝑛 \pi(n)\not=n and des ⁡ ( π) = 1 des 𝜋 1 \operatorname{des}(\pi)=1 implies that π 𝜋 \pi has no fixed point, or equivalently 1-cycle.

By applying Lemma 3.5 iteratively, for any solution to Equation ( 1), we can combine x d, i subscript 𝑥 𝑑 𝑖 x_{d,i} Grassmanian d 𝑑 d -cycles of type i 𝑖 i over all d ∈ 𝒟 k 𝑑 subscript 𝒟 𝑘 d\in\mathcal{D}_{k} and i ∈ [N d] 𝑖 delimited-[] subscript 𝑁 𝑑 i\in[N_{d}] together into a single Grassmanian permutation whose k 𝑘 k -th power is the identity. On the other hand, if such a collection of cycles can be combined in two different ways, then we can find two of these cycles that do not have the same relative order in these two combinations, contradicting Lemma 3.7.

For a prime p 𝑝 p, N p = 1 p ​ ( 2 p − 2) subscript 𝑁 𝑝 1 𝑝 superscript 2 𝑝 2 N_{p}=\frac{1}{p}(2^{p}-2) by Lemma 3.4, and Equation ( 1) reduces to ∑ i = 1 N p x i = n p superscript subscript 𝑖 1 subscript 𝑁 𝑝 subscript 𝑥 𝑖 𝑛 𝑝 \sum_{i=1}^{N_{p}}x_{i}=\frac{n}{p}. If p ∤ n not-divides 𝑝 𝑛 p\nmid n, there is no non-negative integer solution. If p ∣ n conditional 𝑝 𝑛 p\mid n, it is well-known that this equation has ( N p + n p − 1 N p − 1) binomial subscript 𝑁 𝑝 𝑛 𝑝 1 subscript 𝑁 𝑝 1 \binom{N_{p}+\frac{n}{p}-1}{N_{p}-1} solutions in non-negative integers. ∎

## References

- [1] K. Archer and A. Geary. Descents in powers of permutations. arXiv:2406.09369.
- [2] I. M. Gessel and C. Reutenauer. Counting permutations with given cycle structure and descent set. J. Comb. Theory, Ser. A, 64(2):189–215, 1993.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2408.01210
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2408.01211
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2408.01211
[7]: https://arxiv.org/abs/2408.01211
[8]: /html/2408.01212
