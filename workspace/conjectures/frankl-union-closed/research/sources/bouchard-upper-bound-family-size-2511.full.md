<!-- source: https://arxiv.org/html/2511.10608 | converted from HTML -->

An upper bound for union-closed family size

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2511.10608v1 [math.CO] 13 Nov 2025

# An upper bound for union-closed family size

Christopher Bouchard

###### Abstract

Let 𝒜 \mathcal{A} be a union-closed family of sets with universe ⋃ A ∈ 𝒜 A = [n] = { 1, ⋯, n } \bigcup_{A\in\mathcal{A}}A=[n]=\{1,\cdots,n\} and length ℓ \ell. We prove that | 𝒜 | ≤ ∑ i = 0 ℓ ( n i) |\mathcal{A}|\leq\sum_{i=0}^{\ell}\binom{n}{i}, with equality if and only if 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}. Additionally, by showing that | 𝒜 | ≤ ℓ p − 1 ℓ − 1 + 2 n ​ ( 1 − 2 − ℓ) p |\mathcal{A}|\leq\frac{\ell^{p}-1}{\ell-1}+2^{n}(1-2^{-\ell})^{p} for any nonnegative integer p p, we establish for all integers 1 ≤ k ≤ n 1\leq k\leq n that ∑ i = 0 k ( n i) ≤ k p ^ − 1 k − 1 + 2 n ​ ( 1 − 2 − k) p ^ \sum_{i=0}^{k}\binom{n}{i}\leq\frac{k^{\hat{p}}-1}{k-1}+2^{n}(1-2^{-k})^{\hat{p}}, where p ^ = ⌊ ( n − k) / log 2 ⁡ ( k 1 − 2 − k) ⌋ + 1 \hat{p}=\lfloor(n-k)/\log_{2}(\frac{k}{1-2^{-k}})\rfloor+1.

## 1. Introduction

Let 𝒜 \mathcal{A} be a finite family of distinct finite sets (at least one of which is nonempty) with universe U ⁡ ( 𝒜) ≔ ⋃ A ∈ 𝒜 A U(\mathcal{A})\coloneqq\bigcup_{A\in\mathcal{A}}A denoted by [n] = { 1, ⋯, n } [n]=\{1,\cdots,n\}. 𝒜 \mathcal{A} is called union-closed if X 1, X 2 ∈ 𝒜 X_{1},X_{2}\in\mathcal{A} implies that X 1 ∪ X 2 ∈ 𝒜 X_{1}\cup X_{2}\in\mathcal{A}. Such families have gained popularity by way of the union-closed sets conjecture, also known as Frankl’s conjecture, which states that in any union-closed 𝒜 \mathcal{A}, there must be an element from [n] [n] that appears in at least half of its member sets (see [1–2] for an overview of many related results). One result, proved by Reimer in [4], can be expressed as an implicit least upper bound for the size of 𝒜 \mathcal{A}, namely | 𝒜 | ≤ ( 2 / log 2 ⁡ | 𝒜 |) ​ ∑ A ∈ 𝒜 | A | |\mathcal{A}|\leq(2/\log_{2}|\mathcal{A}|)\sum_{A\in\mathcal{A}}|A| (or | 𝒜 | ≤ 4 ∑ A ∈ 𝒜 | A | / | 𝒜 | |\mathcal{A}|\leq 4^{\sum_{A\in\mathcal{A}}|A|/|\mathcal{A}|}).

A chain 𝒞 \mathcal{C} in 𝒜 \mathcal{A} is a subfamily of 𝒜 \mathcal{A} such that X 1, X 2 ∈ 𝒞 X_{1},X_{2}\in\mathcal{C} implies that ( X 1 ⊆ X 2) ∨ ( X 2 ⊆ X 1) (X_{1}\subseteq X_{2})\lor(X_{2}\subseteq X_{1}), and the length of 𝒜 \mathcal{A}, denoted by ℓ ≔ ℓ ⁡ ( 𝒜) \ell\coloneqq\ell(\mathcal{A}), is one less than the maximum size of a chain in 𝒜 \mathcal{A}. A result of Erdős (see Theorem 5 of [3]) states that any family of sets 𝒜 \mathcal{A} (not necessarily union-closed) has size less than or equal to the sum of the largest ℓ + 1 \ell+1 binomial coefficients of n n. In the present work, we prove that imposing the union-closed constraint on 𝒜 \mathcal{A} tightens this upper bound to be the sum of the first, rather than largest, ℓ + 1 \ell+1 binomial coefficients. In a similar vein, we also provide an upper bound for the sum of the first k k binomial coefficients of any positive integer n n. Denote by ( S r) \binom{S}{r} the family of r r -subsets of a set S S. The two main theorems are stated as follows:

Theorem 1. For any union-closed family 𝒜 \mathcal{A} with universe [n] [n] and length ℓ \ell,

 | | 𝒜 | ≤ ∑ i = 0 ℓ ( n i) ​, |\mathcal{A}|\leq\sum_{i=0}^{\ell}\binom{n}{i}\textrm{,} |  |

with equality and if and only if

 | 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) ​. \hskip 3.27222pt\mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}\textrm{.} |  |

Theorem 2. For all integers 1 ≤ k ≤ n 1\leq k\leq n,

 | ∑ i = 0 k ( n i) ≤ k p ^ − 1 k − 1 + 2 n ​ ( 1 − 2 − k) p ^ ​, \sum_{i=0}^{k}\binom{n}{i}\leq\frac{k^{\hat{p}}-1}{k-1}+2^{n}(1-2^{-k})^{\hat{p}}\textrm{,} |  |

where

 | p ^ = ⌊ n − k log 2 ⁡ ( k / ( 1 − 2 − k)) ⌋ + 1. \hskip 6.40204pt\hat{p}=\Bigr\lfloor\frac{n-k}{\log_{2}(k/(1-2^{-k}))}\Bigr\rfloor+1\textrm{.} |  |

## 2. Proof of Theorem 1

We prove the theorem by induction on universe size. For the base case n = 1 n=1, the only union-closed families are 𝒜 = { 1 } \mathcal{A}=\{1\} and 𝒜 = { { 1 }, ∅ } \mathcal{A}=\{\{1\},\emptyset\}. The former has ℓ = 0 \ell=0 and | 𝒜 | = ∑ i = 0 ℓ ( n i) = ( 1 0) = 1 |\mathcal{A}|=\sum_{i=0}^{\ell}\binom{n}{i}=\binom{1}{0}=1, while the latter has ℓ = 1 \ell=1 and | 𝒜 | = ∑ i = 0 ℓ ( n i) = ( 1 0) + ( 1 1) = 2 |\mathcal{A}|=\sum_{i=0}^{\ell}\binom{n}{i}=\binom{1}{0}+\binom{1}{1}=2. For n > 1 n>1, we assume for the induction hypothesis that all union-closed families 𝒜 ′ \mathcal{A}^{\prime} with | U ⁡ ( 𝒜 ′) | < n |U(\mathcal{A}^{\prime})|<n have | 𝒜 ′ | ≤ ∑ i = 0 ℓ ⁡ ( 𝒜 ′) ( | U ⁡ ( 𝒜 ′) | i) |\mathcal{A}^{\prime}|\leq\sum_{i=0}^{\ell(\mathcal{A}^{\prime})}\binom{|U(\mathcal{A}^{\prime})|}{i}, with equality if and only if 𝒜 ′ = ⋃ i = 0 ℓ ⁡ ( 𝒜 ′) ( U ⁡ ( 𝒜 ′) | U ⁡ ( 𝒜 ′) | − i) \mathcal{A}^{\prime}=\bigcup_{i=0}^{\ell(\mathcal{A}^{\prime})}\binom{U(\mathcal{A}^{\prime})}{|U(\mathcal{A}^{\prime})|-i}. We let 𝒜 \mathcal{A} be any union-closed family of sets with universe size n > 1 n>1 and length ℓ < n \ell<n. (If ℓ = n \ell=n, then the theorem is satisfied, as | 𝒜 | ≤ ∑ i = 0 ℓ ( n i) = 2 n |\mathcal{A}|\leq\sum_{i=0}^{\ell}\binom{n}{i}=2^{n} with equality if and only if 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) = 2 [n] \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}=2^{[n]}.) For any x ∈ [n] x\in[n], we define the following families:

 | 𝒜 x = { A ∈ 𝒜 | x ∈ A } ​; \mathcal{A}_{x}=\{A\in\mathcal{A}\ |\ x\in A\}\textrm{;} |  |

 | 𝒜 ^ x = { A ∖ { x } | A ∈ 𝒜 x } ​; \hat{\mathcal{A}}_{x}=\{A\setminus\{x\}\ |\ A\in\mathcal{A}_{x}\}\textrm{;} |  |

 | 𝒜 x ¯ = { A ∈ 𝒜 | x ∉ A } ​. \mathcal{A}_{\bar{x}}=\{A\in\mathcal{A}\ |\ x\not\in A\}\textrm{.} |  |

We observe that 𝒜 = 𝒜 x ∪ 𝒜 x ¯ \mathcal{A}=\mathcal{A}_{x}\cup\mathcal{A}_{\bar{x}}, 𝒜 x ∩ 𝒜 x ¯ = ∅ \mathcal{A}_{x}\cap\mathcal{A}_{\bar{x}}=\emptyset, and | 𝒜 x | = | 𝒜 ^ x | |\mathcal{A}_{x}|=|\hat{\mathcal{A}}_{x}| together imply that | 𝒜 | = | 𝒜 ^ x | + | 𝒜 x ¯ | |\mathcal{A}|=|\hat{\mathcal{A}}_{x}|+|\mathcal{A}_{\bar{x}}|. Because no member set of 𝒜 ^ x \hat{\mathcal{A}}_{x} contains x x, and [n] ∈ 𝒜 x [n]\in\mathcal{A}_{x} implies that [n] ∖ { x } ∈ 𝒜 ^ x [n]\setminus\{x\}\in\hat{\mathcal{A}}_{x}, we have that | U ⁡ ( 𝒜 ^ x) | = n − 1 |U(\hat{\mathcal{A}}_{x})|=n-1. Similarly, because no member set of 𝒜 x ¯ \mathcal{A}_{\bar{x}} contains x x, we have that | 𝒜 x ¯ | ≤ n − 1 |\mathcal{A}_{\bar{x}}|\leq n-1. Now, since 𝒜 x \mathcal{A}_{x} is a subfamily of 𝒜 \mathcal{A} and ℓ ⁡ ( 𝒜 ^ x) = ℓ ⁡ ( 𝒜 x) \ell(\hat{\mathcal{A}}_{x})=\ell(\mathcal{A}_{x}), we have that ℓ ⁡ ( 𝒜 ^ x) ≤ ℓ \ell(\hat{\mathcal{A}}_{x})\leq\ell. Let ℓ ⁡ ( { ∅ }) = 0 \ell(\{\emptyset\})=0. Noting that 𝒜 x ¯ \mathcal{A}_{\bar{x}} is a subfamily of 𝒜 \mathcal{A}, that [n] [n] belongs to any chain of maximum size in 𝒜 \mathcal{A}, and that [n] [n] does not belong to 𝒜 x ¯ \mathcal{A}_{\bar{x}}, we also have that either ℓ = 0 \ell=0 or ℓ ⁡ ( 𝒜 x ¯) ≤ ℓ − 1 \ell(\mathcal{A}_{\bar{x}})\leq\ell-1. Since 𝒜 ^ x \hat{\mathcal{A}}_{x} is itself union-closed, we have by the induction hypothesis that

 | | 𝒜 ^ x | ≤ ∑ i = 0 ℓ ⁡ ( 𝒜 ^ x) ( | U ⁡ ( 𝒜 ^ x) | i) = ∑ i = 0 ℓ ⁡ ( 𝒜 ^ x) ( n − 1 i) ≤ ∑ i = 0 ℓ ( n − 1 i) ​, |\hat{\mathcal{A}}_{x}|\leq\sum_{i=0}^{\ell(\hat{\mathcal{A}}_{x})}\binom{|U(\hat{\mathcal{A}}_{x})|}{i}=\sum_{i=0}^{\ell(\hat{\mathcal{A}}_{x})}\binom{n-1}{i}\leq\sum_{i=0}^{\ell}\binom{n-1}{i}\textrm{,} |  |

If 𝒜 x ¯ = ∅ \mathcal{A}_{\bar{x}}=\emptyset, then | 𝒜 | = | 𝒜 ^ x | ≤ ∑ i = 0 ℓ ( n − 1 i) ≤ ∑ i = 0 ℓ ( n i) |\mathcal{A}|=|\hat{\mathcal{A}}_{x}|\leq\sum_{i=0}^{\ell}\binom{n-1}{i}\leq\sum_{i=0}^{\ell}\binom{n}{i}. If 𝒜 x ¯ = { ∅ } \mathcal{A}_{\bar{x}}=\{\emptyset\}, then ℓ > 0 \ell>0 and | 𝒜 | = | 𝒜 ^ x | + 1 ≤ 1 + ∑ i = 0 ℓ ( n − 1 i) ≤ ∑ i = 0 ℓ ( n i) |\mathcal{A}|=|\hat{\mathcal{A}}_{x}|+1\leq 1+\sum_{i=0}^{\ell}\binom{n-1}{i}\leq\sum_{i=0}^{\ell}\binom{n}{i}. Else, 𝒜 x ¯ ≠ ∅ \mathcal{A}_{\bar{x}}\neq\emptyset and 𝒜 x ¯ ≠ { ∅ } \mathcal{A}_{\bar{x}}\neq\{\emptyset\}, and 𝒜 x ¯ \mathcal{A}_{\bar{x}} is union-closed as well as 𝒜 ^ x \hat{\mathcal{A}}_{x}. In this case, ℓ \ell is again positive, and we apply the induction hypothesis to 𝒜 x ¯ \mathcal{A}_{\bar{x}} in order to obtain that

 | | 𝒜 x ¯ | ≤ ∑ i = 0 ℓ ⁡ ( 𝒜 x ¯) ( | U ⁡ ( 𝒜 x ¯) | i) ≤ ∑ i = 0 ℓ ⁡ ( 𝒜 x ¯) ( n − 1 i) ≤ ∑ i = 0 ℓ − 1 ( n − 1 i) ​. |\mathcal{A}_{\bar{x}}|\leq\sum_{i=0}^{\ell(\mathcal{A}_{\bar{x}})}\binom{|U(\mathcal{A}_{\bar{x}})|}{i}\leq\sum_{i=0}^{\ell(\mathcal{A}_{\bar{x}})}\binom{n-1}{i}\leq\sum_{i=0}^{\ell-1}\binom{n-1}{i}\textrm{.} |  |

Therefore, if 𝒜 x ¯ ≠ ∅ \mathcal{A}_{\bar{x}}\neq\emptyset and 𝒜 x ¯ ≠ { ∅ } \mathcal{A}_{\bar{x}}\neq\{\emptyset\}, then we have that

 |  | | 𝒜 | = | 𝒜 ^ x | + | 𝒜 x ¯ | \displaystyle\hskip-12.44807pt|\mathcal{A}|=|\hat{\mathcal{A}}_{x}|+|\mathcal{A}_{\bar{x}}| |  |

 |  | ≤ ∑ i = 0 ℓ ( n − 1 i) + ∑ i = 0 ℓ − 1 ( n − 1 i) \displaystyle\leq\sum_{i=0}^{\ell}\binom{n-1}{i}+\sum_{i=0}^{\ell-1}\binom{n-1}{i} |  |

 |  | = ( n − 1 0) + ∑ i = 1 ℓ ( ( n − 1 i) + ( n − 1 i − 1)) \displaystyle=\binom{n-1}{0}+\sum_{i=1}^{\ell}\Bigr(\binom{n-1}{i}+\binom{n-1}{i-1}\Bigr) |  |

 |  | = 1 + ∑ i = 1 ℓ ( n i) \displaystyle=1+\sum_{i=1}^{\ell}\binom{n}{i} |  |

 |  | = ∑ i = 0 ℓ ( n i) ​. \displaystyle=\sum_{i=0}^{\ell}\binom{n}{i}\textrm{.} |  |

(Here, the equation ∑ i = 0 ℓ ( n i) = ∑ i = 0 ℓ ( n − 1 i) + ∑ i = 0 ℓ − 1 ( n − 1 i) \sum_{i=0}^{\ell}\binom{n}{i}=\sum_{i=0}^{\ell}\binom{n-1}{i}+\sum_{i=0}^{\ell-1}\binom{n-1}{i} corresponds to case m = 1 m=1 of the identity ∑ i = 0 k ( n i) = ∑ i = 0 m ( m i) ​ ∑ j = 0 k − i ( n − m j) \sum_{i=0}^{k}\binom{n}{i}=\sum_{i=0}^{m}\binom{m}{i}\sum_{j=0}^{k-i}\binom{n-m}{j} for all integers 0 ≤ k ≤ n 0\leq k\leq n, where 0 ≤ m ≤ n 0\leq m\leq n.) This completes the proof that | 𝒜 | ≤ ∑ i = 0 ℓ ( n i) |\mathcal{A}|\leq\sum_{i=0}^{\ell}\binom{n}{i}. Next, we show that | 𝒜 | = ∑ i = 0 ℓ ( n i) |\mathcal{A}|=\sum_{i=0}^{\ell}\binom{n}{i} if and only if 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}. That | 𝒜 | = ∑ i = 0 ℓ ( n i) |\mathcal{A}|=\sum_{i=0}^{\ell}\binom{n}{i} when 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i} is clear from symmetry of the binomial coefficient. It remains to show that the bound is only sharp if 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}, for which we now assume that | 𝒜 | = ∑ i = 0 ℓ ( n i) |\mathcal{A}|=\sum_{i=0}^{\ell}\binom{n}{i}. If ℓ = 0 \ell=0, then | 𝒜 | = ∑ i = 0 ℓ ( n i) = ( n 0) = 1 |\mathcal{A}|=\sum_{i=0}^{\ell}\binom{n}{i}=\binom{n}{0}=1, implying that 𝒜 = { [n] } = ( [n] n) = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\{[n]\}=\binom{[n]}{n}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}. Else, ℓ > 0 \ell>0, and we have that ∑ i = 0 ℓ ( n i) = ∑ i = 0 ℓ ( n − 1 i) + ∑ i = 0 ℓ − 1 ( n − 1 i) \sum_{i=0}^{\ell}\binom{n}{i}=\sum_{i=0}^{\ell}\binom{n-1}{i}+\sum_{i=0}^{\ell-1}\binom{n-1}{i}. Noting that | 𝒜 | = | 𝒜 ^ x | + | 𝒜 x ¯ | |\mathcal{A}|=|\hat{\mathcal{A}}_{x}|+|\mathcal{A}_{\bar{x}}| and | 𝒜 ^ x | ≤ ∑ i = 0 ℓ ( n − 1 i) |\hat{\mathcal{A}}_{x}|\leq\sum_{i=0}^{\ell}\binom{n-1}{i}, we then have that | 𝒜 x ¯ | ≥ ∑ i = 0 ℓ − 1 ( n − 1 i) |\mathcal{A}_{\bar{x}}|\geq\sum_{i=0}^{\ell-1}\binom{n-1}{i}. It again follows that 𝒜 x ¯ \mathcal{A}_{\bar{x}} is union-closed. (Otherwise, 𝒜 x ¯ = ∅ \mathcal{A}_{\bar{x}}=\emptyset and | 𝒜 x ¯ | = 0 ≥ ∑ i = 0 ℓ − 1 ( n − 1 i) ≥ 1 |\mathcal{A}_{\bar{x}}|=0\geq\sum_{i=0}^{\ell-1}\binom{n-1}{i}\geq 1, a contradiction, or 𝒜 x ¯ = { ∅ } \mathcal{A}_{\bar{x}}=\{\emptyset\} and | 𝒜 x ¯ | = 1 ≥ ∑ i = 0 ℓ − 1 ( n − 1 i) |\mathcal{A}_{\bar{x}}|=1\geq\sum_{i=0}^{\ell-1}\binom{n-1}{i} implies that ℓ = 1 \ell=1, making 𝒜 = { [n], ∅ } \mathcal{A}=\{[n],\emptyset\}, which then implies that n = 1 n=1, again a contradiction). Therefore, | 𝒜 x ¯ | ≤ ∑ i = 0 ℓ − 1 ( n − 1 i) |\mathcal{A}_{\bar{x}}|\leq\sum_{i=0}^{\ell-1}\binom{n-1}{i}, which implies that both | 𝒜 ^ x | = ∑ i = 0 ℓ ( n − 1 i) |\hat{\mathcal{A}}_{x}|=\sum_{i=0}^{\ell}\binom{n-1}{i} and | 𝒜 x ¯ | = ∑ i = 0 ℓ − 1 ( n − 1 i) |\mathcal{A}_{\bar{x}}|=\sum_{i=0}^{\ell-1}\binom{n-1}{i}. It follows that U ⁡ ( 𝒜 ^ x) = [n] ∖ { x } U(\hat{\mathcal{A}}_{x})=[n]\setminus\{x\} with ℓ ⁡ ( 𝒜 ^ x) = ℓ \ell(\hat{\mathcal{A}}_{x})=\ell. (If not, then | 𝒜 ^ x | = ∑ i = 0 ℓ ⁡ ( 𝒜 ^ x) ( | U ⁡ ( 𝒜 ^ x) | i) ≤ ∑ i = 0 ℓ ( n − 2 i) |\hat{\mathcal{A}}_{x}|=\sum_{i=0}^{\ell(\hat{\mathcal{A}}_{x})}\binom{|U(\hat{\mathcal{A}}_{x})|}{i}\leq\sum_{i=0}^{\ell}\binom{n-2}{i} or | 𝒜 ^ x | = ∑ i = 0 ℓ ⁡ ( 𝒜 ^ x) ( | U ⁡ ( 𝒜 ^ x) | i) ≤ ∑ i = 0 ℓ − 1 ( n − 1 i) |\hat{\mathcal{A}}_{x}|=\sum_{i=0}^{\ell(\hat{\mathcal{A}}_{x})}\binom{|U(\hat{\mathcal{A}}_{x})|}{i}\leq\sum_{i=0}^{\ell-1}\binom{n-1}{i}, a contradiction.) Therefore, 𝒜 ^ x = ⋃ i = 0 ℓ ( [n] ∖ { x } ( n − 1) − i) \hat{\mathcal{A}}_{x}=\bigcup_{i=0}^{\ell}\binom{[n]\setminus\{x\}}{(n-1)-i} by the induction hypothesis. Similarly, it also follows that U ⁡ ( 𝒜 x ¯) = [n] ∖ { x } U(\mathcal{A}_{\bar{x}})=[n]\setminus\{x\} with ℓ ⁡ ( 𝒜 x ¯) = ℓ − 1 \ell(\mathcal{A}_{\bar{x}})=\ell-1. (When ℓ = 1 \ell=1, having x ∉ A x\not\in A for any A ∈ 𝒜 x ¯ A\in\mathcal{A}_{\bar{x}} implies that | 𝒜 x ¯ | = 1 |\mathcal{A}_{\bar{x}}|=1, making ℓ ⁡ ( 𝒜 x ¯) = 0 = ℓ − 1 \ell(\mathcal{A}_{\bar{x}})=0=\ell-1.) Applying the induction hypothesis now to 𝒜 x ¯ \mathcal{A}_{\bar{x}}, we obtain that 𝒜 x ¯ = ⋃ i = 0 ℓ − 1 ( [n] ∖ { x } ( n − 1) − i) \mathcal{A}_{\bar{x}}=\bigcup_{i=0}^{\ell-1}\binom{[n]\setminus\{x\}}{(n-1)-i}. We thus have that

 |  | 𝒜 = 𝒜 x ∪ 𝒜 x ¯ = { A ∪ { x } | A ∈ 𝒜 ^ x } ∪ 𝒜 x ¯ \displaystyle\hskip-8.5359pt\mathcal{A}=\mathcal{A}_{x}\cup\mathcal{A}_{\bar{x}}=\{A\cup\{x\}\ |\ A\in\hat{\mathcal{A}}_{x}\}\cup\mathcal{A}_{\bar{x}} |  |

 |  | = ⋃ i = 0 ℓ { A ∪ { x } | A ∈ ( [n] ∖ { x } n − i − 1) } ∪ ⋃ i = 0 ℓ − 1 ( [n] ∖ { x } n − i − 1) \displaystyle=\bigcup_{i=0}^{\ell}\Bigr\{A\cup\{x\}\ \Bigr|\ A\in\binom{[n]\setminus\{x\}}{n-i-1}\Bigr\}\cup\bigcup_{i=0}^{\ell-1}\binom{[n]\setminus\{x\}}{n-i-1} |  |

 |  | = { [n] } ∪ ⋃ i = 1 ℓ ( { A ∪ { x } | A ∈ ( [n] ∖ { x } n − i − 1) } ∪ ( [n] ∖ { x } n − i)) \displaystyle=\{[n]\}\cup\bigcup_{i=1}^{\ell}\Bigr(\Bigr\{A\cup\{x\}\ \Bigr|\ A\in\binom{[n]\setminus\{x\}}{n-i-1}\Bigr\}\cup\binom{[n]\setminus\{x\}}{n-i}\Bigr) |  |

 |  | = ( [n] n) ∪ ⋃ i = 1 ℓ ( [n] n − i) \displaystyle=\binom{[n]}{n}\cup\bigcup_{i=1}^{\ell}\binom{[n]}{n-i} |  |

 |  | = ⋃ i = 0 ℓ ( [n] n − i) ​. \displaystyle=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}\textrm{.} |  |

Therefore, | 𝒜 | = ∑ i = 1 ℓ ( n i) |\mathcal{A}|=\sum_{i=1}^{\ell}\binom{n}{i} implies that 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}, completing the proof of Theorem 1.

Corollary 2.1. For any union-closed family 𝒜 \mathcal{A}, there is an element from its universe [n] [n] that is in at most ∑ i = 0 ℓ ( n − 1 i) \sum_{i=0}^{\ell}\binom{n-1}{i} of its member sets.

Proof. Because | 𝒜 | ≤ ∑ i = 0 ℓ ( n i) |\mathcal{A}|\leq\sum_{i=0}^{\ell}\binom{n}{i}, it holds that | 𝒜 ∖ ⋃ i = 0 ℓ ( [n] n − i) | ≤ | ⋃ i = 0 ℓ ( [n] n − i) ∖ 𝒜 | |\mathcal{A}\setminus\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}|\leq|\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}\setminus\mathcal{A}|. We also have that | X | < | Y | |X|<|Y| for any X ∈ 𝒜 ∖ ⋃ i = 0 ℓ ( [n] n − i) X\in\mathcal{A}\setminus\bigcup_{i=0}^{\ell}\binom{[n]}{n-i} and Y ∈ ⋃ i = 0 ℓ ( [n] n − i) ∖ 𝒜 Y\in\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}\setminus\mathcal{A}. Together these observations imply that ∑ A ∈ 𝒜 | A | ≤ ∑ A ∈ ⋃ i = 0 ℓ ( [n] n − i) | A | = ∑ i = 0 ℓ ( n − i) ​ ( n i) \sum_{A\in\mathcal{A}}|A|\leq\sum_{A\in\bigcup_{i=0}^{\ell}\binom{[n]}{n-i}}|A|=\sum_{i=0}^{\ell}(n-i)\binom{n}{i}. Because ∑ A ∈ 𝒜 | A | = ∑ x ∈ [n] | 𝒜 x | \sum_{A\in\mathcal{A}}|A|=\sum_{x\in[n]}|\mathcal{A}_{x}|, we also have that ∑ x ∈ [n] | 𝒜 x | ≤ ∑ i = 0 ℓ ( n − i) ​ ( n i) \sum_{x\in[n]}|\mathcal{A}_{x}|\leq\sum_{i=0}^{\ell}(n-i)\binom{n}{i}. It follows that | 𝒜 y | ≤ ∑ i = 0 ℓ ( 1 − i n) ​ ( n i) |\mathcal{A}_{y}|\leq\sum_{i=0}^{\ell}(1-\frac{i}{n})\binom{n}{i} for some y ∈ [n] y\in[n]. (If not, then | 𝒜 x | > ∑ i = 0 ℓ ( 1 − i n) ​ ( n i) |\mathcal{A}_{x}|>\sum_{i=0}^{\ell}(1-\frac{i}{n})\binom{n}{i} for all x ∈ [n] x\in[n], implying that ∑ x ∈ [n] | 𝒜 x | > n ⁡ ( ∑ i = 0 ℓ ( 1 − i n) ​ ( n i)) = ∑ i = 0 ℓ ( n − i) ​ ( n i) \sum_{x\in[n]}|\mathcal{A}_{x}|>n(\sum_{i=0}^{\ell}(1-\frac{i}{n})\binom{n}{i})=\sum_{i=0}^{\ell}(n-i)\binom{n}{i}, a contradiction.) Finally, considering that ∑ i = 0 ℓ ( 1 − i n) ​ ( n i) \sum_{i=0}^{\ell}(1-\frac{i}{n})\binom{n}{i} is equal to the size of 𝒜 x \mathcal{A}_{x} for 𝒜 = ⋃ i = 0 ℓ ( [n] n − i) \mathcal{A}=\bigcup_{i=0}^{\ell}\binom{[n]}{n-i} and any x ∈ [n] x\in[n], we have by double counting that ∑ i = 0 ℓ ( 1 − i n) ​ ( n i) = ∑ i = 0 ℓ ( n − 1 n − i − 1) \sum_{i=0}^{\ell}(1-\frac{i}{n})\binom{n}{i}=\sum_{i=0}^{\ell}\binom{n-1}{n-i-1}, making | 𝒜 y | ≤ ∑ i = 0 ℓ ( n − 1 i) |\mathcal{A}_{y}|\leq\sum_{i=0}^{\ell}\binom{n-1}{i}.

## 3. Proof of Theorem 2

Let 𝒜 \mathcal{A} be any union-closed family with universe [n] [n] and length ℓ \ell, and consider any chain 𝒞 = { C 1, ⋯, C ℓ + 1 } \mathcal{C}=\{C_{1},\cdots,C_{\ell+1}\} in 𝒜 \mathcal{A} of maximum size, where 1 ≤ i < j ≤ ℓ + 1 1\leq i<j\leq\ell+1 implies that C j ⊊ C i C_{j}\subsetneq C_{i} without loss of generality. Because every member set of 𝒜 \mathcal{A} is a subset of [n] [n], and [n] [n] must belong to 𝒜 \mathcal{A}, we have that C 1 = [n] C_{1}=[n]. Let [0] = ∅ [0]=\emptyset. For each i ∈ [ℓ] i\in[\ell], we define

 | 𝒟 i = { X ∖ ( C i ∖ C i + 1) | X ∈ 𝒞 i }, \mathcal{D}_{i}=\ \Bigr\{X\setminus(C_{i}\setminus C_{i+1})\ \Bigr|\ X\in\mathcal{C}_{i}\Bigr\}\textrm{,} |  |

where

 | 𝒞 i = { X ∈ 𝒜 | ( C i ∖ C i + 1 ⊆ X) ∧ ( X ∩ ⋃ j ∈ [i − 1] C j ∖ C j + 1 = ∅) }. \mathcal{C}_{i}=\Bigr\{X\in\mathcal{A}\ \Bigr|\ (C_{i}\setminus C_{i+1}\subseteq X)\land(X\cap\bigcup_{j\in[i-1]}C_{j}\setminus C_{j+1}=\emptyset)\Bigr\}\textrm{.} |  |

Theorem 3.1. For any i ∈ [ℓ] i\in[\ell], if C i + 1 ≠ ∅ C_{i+1}\neq\emptyset, then 𝒟 i \mathcal{D}_{i} is union-closed.

Proof. Let i i be any element of [ℓ] [\ell] such that C i + 1 ≠ ∅ C_{i+1}\neq\emptyset. Assuming any X 1, X 2 ∈ 𝒞 i X_{1},X_{2}\in\mathcal{C}_{i}, we first have that ( C i ∖ C i + 1 ⊆ X 1) ∧ ( C i ∖ C i + 1 ⊆ X 2) ⟹ C i ∖ C i + 1 ⊆ X 1 ∪ X 2 (C_{i}\setminus C_{i+1}\subseteq X_{1})\ \land\ (C_{i}\setminus C_{i+1}\subseteq X_{2})\implies C_{i}\setminus C_{i+1}\subseteq X_{1}\cup X_{2} and ( X 1 ∩ ⋃ j ∈ [i − 1] C j ∖ C j + 1 = ∅) ∧ ( X 2 ∩ ⋃ j ∈ [i − 1] C j ∖ C j + 1 = ∅) ⟹ ( X 1 ∪ X 2) ∩ ⋃ j ∈ [i − 1] C j ∖ C j + 1 = ∅ (X_{1}\cap\bigcup_{j\in[i-1]}C_{j}\setminus C_{j+1}=\emptyset)\ \land\ (X_{2}\cap\bigcup_{j\in[i-1]}C_{j}\setminus C_{j+1}=\emptyset)\implies(X_{1}\cup X_{2})\cap\bigcup_{j\in[i-1]}C_{j}\setminus C_{j+1}=\emptyset. Hence, X 1 ∪ X 2 X_{1}\cup X_{2} satisfies both conditions for membership in 𝒞 i \mathcal{C}_{i}. Because C i ∈ 𝒞 i C_{i}\in\mathcal{C}_{i} and C i ≠ ∅ C_{i}\neq\emptyset, it then follows that 𝒞 i \mathcal{C}_{i} is union-closed. Now, assuming any Y 1, Y 2 ∈ 𝒟 i Y_{1},Y_{2}\in\mathcal{D}_{i}, we have that Y 1 ∪ ( C i ∖ C i + 1) ∈ 𝒞 i Y_{1}\cup(C_{i}\setminus C_{i+1})\in\mathcal{C}_{i} and Y 2 ∪ ( C i ∖ C i + 1) ∈ 𝒞 i Y_{2}\cup(C_{i}\setminus C_{i+1})\in\mathcal{C}_{i}. Since 𝒞 i \mathcal{C}_{i} is union-closed, we then also have that ( Y 1 ∪ ( C i ∖ C i + 1)) ∪ ( Y 2 ∪ ( C i ∖ C i + 1)) = ( Y 1 ∪ Y 2) ∪ ( C i ∖ C i + 1) ∈ 𝒞 i (Y_{1}\cup(C_{i}\setminus C_{i+1}))\cup(Y_{2}\cup(C_{i}\setminus C_{i+1}))=(Y_{1}\cup Y_{2})\cup(C_{i}\setminus C_{i+1})\in\mathcal{C}_{i}. It follows that ( ( Y 1 ∪ Y 2) ∪ ( C i ∖ C i + 1)) ∖ ( C i ∖ C i + 1) = Y 1 ∪ Y 2 ∈ 𝒟 i ((Y_{1}\cup Y_{2})\cup(C_{i}\setminus C_{i+1}))\setminus(C_{i}\setminus C_{i+1})=Y_{1}\cup Y_{2}\in\mathcal{D}_{i}. Because C i + 1 ∈ 𝒟 i C_{i+1}\in\mathcal{D}_{i} and C i + 1 ≠ ∅ C_{i+1}\neq\emptyset, it then follows that 𝒟 i \mathcal{D}_{i} is also union-closed, proving Theorem 3.1.

Theorem 3.2.

 | | 𝒜 | = 1 + ∑ i = 1 ℓ | 𝒟 i | ​. \hskip-14.22636pt|\mathcal{A}|=1+\sum_{i=1}^{\ell}|\mathcal{D}_{i}|\textit{.} |  |

Proof. We first have that 𝒜 ∖ { C ℓ + 1 } = ⋃ i ∈ [ℓ] 𝒞 i \mathcal{A}\setminus\{C_{\ell+1}\}=\bigcup_{i\in[\ell]}\mathcal{C}_{i}. (If not, then there exists some X ∈ 𝒜 ∖ { C ℓ + 1 } X\in\mathcal{A}\setminus\{C_{\ell+1}\} such that either X ⊊ C ℓ + 1 X\subsetneq C_{\ell+1} or ∃ i ∈ [ℓ] | ( ∅ ⊊ ( C i ∖ C i + 1) ∩ X ⊊ C i ∖ C i + 1 ∧ ∀ j ∈ [i − 1] | ( C j ∖ C j + 1) ∩ X = ∅) \exists i\in[\ell]\ |\ (\emptyset\subsetneq(C_{i}\setminus C_{i+1})\cap X\subsetneq C_{i}\setminus C_{i+1}\ \land\ \forall j\in[i-1]\ |\ (C_{j}\setminus C_{j+1})\cap X=\emptyset), and it follows that either { C 1, ⋯, C ℓ + 1, X } \{C_{1},\cdots,C_{\ell+1},X\} or { C 1, ⋯, C i, C i + 1 ∪ X, C i + 1, ⋯, C ℓ + 1 } \{C_{1},\cdots,C_{i},C_{i+1}\cup X,C_{i+1},\cdots,C_{\ell+1}\} is a chain in 𝒜 \mathcal{A} of size ℓ + 2 \ell+2, contradicting the definition of ℓ \ell.) Next, we observe that 𝒞 i ∩ 𝒞 j = ∅ \mathcal{C}_{i}\cap\mathcal{C}_{j}=\emptyset for any distinct i i and j j in [ℓ] [\ell]. (Otherwise, there exist distinct i i and j j in [ℓ] [\ell] with at least one member set X X in 𝒞 i ∩ 𝒞 j \mathcal{C}_{i}\cap\mathcal{C}_{j}, where j < i j<i without loss of generality, and X ∈ 𝒞 j X\in\mathcal{C}_{j} implies that C j ∖ C j + 1 ⊆ X C_{j}\setminus C_{j+1}\subseteq X, while X ∈ 𝒞 i X\in\mathcal{C}_{i} and j ∈ [i − 1] j\in[i-1] together imply that X ∩ ( C j ∖ C j + 1) = ∅ X\cap(C_{j}\setminus C_{j+1})=\emptyset, a contradiction.) It follows that | 𝒜 ∖ { C ℓ + 1 } | = ∑ i = 1 ℓ | 𝒞 i | |\mathcal{A}\setminus\{C_{\ell+1}\}|=\sum_{i=1}^{\ell}|\mathcal{C}_{i}|, making | 𝒜 | = 1 + ∑ i = 1 ℓ | 𝒞 i | |\mathcal{A}|=1+\sum_{i=1}^{\ell}|\mathcal{C}_{i}|. Finally, because C i ∖ C i + 1 ⊆ X C_{i}\setminus C_{i+1}\subseteq X for any i ∈ [ℓ] i\in[\ell] and any X ∈ 𝒞 i X\in\mathcal{C}_{i}, we have that | 𝒟 i | = | 𝒞 i | |\mathcal{D}_{i}|=|\mathcal{C}_{i}| for each i i. It then follows that | 𝒜 | = 1 + ∑ i = 1 ℓ | 𝒟 i | |\mathcal{A}|=1+\sum_{i=1}^{\ell}|\mathcal{D}_{i}|, proving Theorem 3.2.

Lemma 3.3. | U ⁡ ( 𝒟 i) | ≤ n − i \ \ |U(\mathcal{D}_{i})|\leq n-i and ℓ ⁡ ( 𝒟 i) ≤ ℓ \ell(\mathcal{D}_{i})\leq\ell for all i ∈ [ℓ] i\in[\ell].

Proof. For all i ∈ [ℓ] i\in[\ell], | U ⁡ ( 𝒟 i) | ≤ n − i |U(\mathcal{D}_{i})|\leq n-i follows from having X ∩ ⋃ j ∈ [i] C j ∖ C j + 1 = ∅ X\cap\bigcup_{j\in[i]}C_{j}\setminus C_{j+1}=\emptyset for any X ∈ 𝒟 i X\in\mathcal{D}_{i}, and ℓ ⁡ ( 𝒟 i) ≤ ℓ \ell(\mathcal{D}_{i})\leq\ell follows from ℓ ⁡ ( 𝒞 i) = ℓ ⁡ ( 𝒟 i) \ell(\mathcal{C}_{i})=\ell(\mathcal{D}_{i}) and 𝒞 i \mathcal{C}_{i} being a subfamily of 𝒜 \mathcal{A}.

We now define Θ: ℤ ≥ 0 3 → ℤ ≥ 0 \Theta\colon{\mathbb{Z}^{3}_{\geq 0}}\to\mathbb{Z}_{\geq 0} such that

 | Θ ⁡ ( x, y, z) = x z − 1 x − 1 + 2 y ​ ( 1 − 2 − x) z ​. \Theta(x,y,z)=\frac{x^{z}-1}{x-1}+2^{y}(1-2^{-x})^{z}\textrm{.} |  |

We prove by induction that, for any nonnegative integer p p, | 𝒜 | ≤ Θ ⁡ ( ℓ, n, p) |\mathcal{A}|\leq\Theta(\ell,n,p) for all union-closed families 𝒜 \mathcal{A} with universe [n] [n] and length ℓ \ell. For the base case p = 0 p=0, we have that | 𝒜 | ≤ Θ ⁡ ( ℓ, n, p) = 2 n |\mathcal{A}|\leq\Theta(\ell,n,p)=2^{n} for any such 𝒜 \mathcal{A}. For p > 0 p>0, we again let 𝒜 \mathcal{A} be any union-closed family with universe [n] [n] and length ℓ \ell, and we assume for the induction hypothesis that any union-closed family 𝒜 ′ \mathcal{A}^{\prime} with universe of size n ′ n^{\prime} and length ℓ ′ \ell^{\prime} satisfies | 𝒜 ′ | ≤ Θ ⁡ ( ℓ ′, n ′, p − 1) |\mathcal{A}^{\prime}|\leq\Theta(\ell^{\prime},n^{\prime},p-1). By Theorem 3.1, we apply this hypothesis to all families 𝒟 i: i ∈ [ℓ] \mathcal{D}_{i}\colon i\in[\ell] that have C i + 1 ≠ ∅ C_{i+1}\neq\emptyset in order to obtain that | 𝒟 i | ≤ Θ ⁡ ( ℓ ⁡ ( 𝒟 i), | U ⁡ ( 𝒟 i) |, p − 1) |\mathcal{D}_{i}|\leq\Theta(\ell(\mathcal{D}_{i}),|U(\mathcal{D}_{i})|,p-1) for all such i i. (If C i + 1 = ∅ C_{i+1}=\emptyset, then we may directly compute that | 𝒟 i | = Θ ⁡ ( ℓ ⁡ ( 𝒟 i), | U ⁡ ( 𝒟 i) |, p − 1) = Θ ⁡ ( 0, 0, p − 1) = 1 |\mathcal{D}_{i}|=\Theta(\ell(\mathcal{D}_{i}),|U(\mathcal{D}_{i})|,p-1)=\Theta(0,0,p-1)=1.) Noting that Θ ⁡ ( x, y, z) \Theta(x,y,z) is always increasing with respect to each of the variables x x and y y, it then follows from Lemma 3.3 that | 𝒟 i | ≤ Θ ⁡ ( ℓ, n − i, p − 1) |\mathcal{D}_{i}|\leq\Theta(\ell,n-i,p-1) for all i ∈ [ℓ] i\in[\ell]. Recall that by Theorem 3.2, | 𝒜 | = 1 + ∑ i = 1 ℓ | 𝒟 i | |\mathcal{A}|=1+\sum_{i=1}^{\ell}|\mathcal{D}_{i}|. We substitute Θ ⁡ ( ℓ, n − i, p − 1) \Theta(\ell,n-i,p-1) into this equation for every | 𝒟 i | |\mathcal{D}_{i}| to obtain an upper bound for the size of 𝒜 \mathcal{A} as follows:

 |  | | 𝒜 | = 1 + ∑ i = 1 ℓ | 𝒟 i | \displaystyle\hskip 20.34361pt|\mathcal{A}|=1+\sum_{i=1}^{\ell}|\mathcal{D}_{i}| |  |

 |  | ≤ 1 + ∑ i = 1 ℓ Θ ⁡ ( ℓ, n − i, p − 1) \displaystyle\hskip 16.36024pt\hskip 16.36024pt\leq 1+\sum_{i=1}^{\ell}\Theta(\ell,n-i,p-1) |  |

 |  | = 1 + ∑ i = 1 ℓ ( ℓ p − 1 − 1 ℓ − 1 + 2 n − i ( 1 − 2 − ℓ) p − 1) \displaystyle\hskip 16.36024pt\hskip 16.36024pt=1+\sum_{i=1}^{\ell}\Bigr(\frac{\ell^{p-1}-1}{\ell-1}+2^{n-i}(1-2^{-\ell})^{p-1}\Bigr) |  |

 |  | = 1 + ℓ ( ℓ p − 1 − 1 ℓ − 1) + ( 1 − 2 − ℓ) p − 1 ∑ i = 1 ℓ 2 n − i \displaystyle\hskip 16.36024pt\hskip 16.36024pt=1+\ell\Bigr(\frac{\ell^{p-1}-1}{\ell-1}\Bigr)+(1-2^{-\ell})^{p-1}\sum_{i=1}^{\ell}2^{n-i} |  |

 |  | = ℓ p − 1 ℓ − 1 + ( 1 − 2 − ℓ) p − 1 ​ ( 2 n − 2 n − ℓ) \displaystyle\hskip 16.36024pt\hskip 16.36024pt=\frac{\ell^{p}-1}{\ell-1}+(1-2^{-\ell})^{p-1}(2^{n}-2^{n-\ell}) |  |

 |  | = ℓ p − 1 ℓ − 1 + 2 n ​ ( 1 − 2 − ℓ) p \displaystyle\hskip 16.36024pt\hskip 16.36024pt=\frac{\ell^{p}-1}{\ell-1}+2^{n}(1-2^{-\ell})^{p} |  |

 |  | = Θ ⁡ ( ℓ, n, p) ​. \displaystyle\hskip 16.36024pt\hskip 16.36024pt=\Theta(\ell,n,p)\textrm{.} |  |

This resolves the induction step. It follows that | 𝒜 | ≤ min p ∈ ℤ ≥ 0 ⁡ { Θ ⁡ ( ℓ, n, p) } |\mathcal{A}|\leq\min_{p\in\mathbb{Z}_{\geq 0}}\{\Theta(\ell,n,p)\} for any union-closed family 𝒜 \mathcal{A} with universe [n] [n] and length ℓ \ell.

For all integers 1 ≤ k ≤ n 1\leq k\leq n, we set 𝒜 \mathcal{A} equal to ⋃ i = 0 k ( [n] n − i) \bigcup_{i=0}^{k}\binom{[n]}{n-i} to obtain that ∑ i = 0 k ( n i) ≤ min p ∈ ℤ ≥ 0 ⁡ { Θ ⁡ ( k, n, p) } \sum_{i=0}^{k}\binom{n}{i}\leq\min_{p\in\mathbb{Z}_{\geq 0}}\{\Theta(k,n,p)\}. As p ^ ∈ ℤ ≥ 0 \hat{p}\in\mathbb{Z}_{\geq 0}, this completes the proof of Theorem 2.

To demonstrate that p ^ \hat{p} is optimal, we compute that Θ ⁡ ( k, n, p + 1) ≤ Θ ⁡ ( k, n, p) \Theta(k,n,p+1)\leq\Theta(k,n,p) if and only if

 | p ≤ log k 1 − 2 − k ⁡ ( 2 n − k) = n − k log 2 ⁡ ( k / ( 1 − 2 − k)) ​. p\leq\log_{\frac{k}{1-2^{-k}}}(2^{n-k})=\frac{n-k}{\log_{2}(k/(1-2^{-k}))}\textrm{.} |  |

Thus, Θ \Theta is decreasing with respect to p p if and only if p ≤ ⌊ n − k log 2 ⁡ ( k / ( 1 − 2 − k)) ⌋ p\leq\lfloor\frac{n-k}{\log_{2}(k/(1-2^{-k}))}\rfloor, and it follows that

 | Θ ( k, n, ⌊ n − k log 2 ⁡ ( k / ( 1 − 2 − k)) ⌋ + 1) = Θ ( k, n, p ^) = min p ∈ ℤ ≥ 0 { Θ ( k, n, p) }. \Theta\Bigr(k,n,\Bigr\lfloor\frac{n-k}{\log_{2}(k/(1-2^{-k}))}\Bigr\rfloor+1\Bigr)=\Theta(k,n,\hat{p})=\min_{p\in\mathbb{Z}_{\geq 0}}\{\Theta(k,n,p)\}\textrm{.} |  |

## References

- [1] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture, Graphs Combin. 31 (2015), 2043–2074.
- [2] S. Cambie, Progress on the union-closed conjecture and offsprings in winter 2022-2023, preprint (2023), arXiv:2306.12351.
- [3] P. Erdős, On a lemma of Littlewood and Offord, Bull. Amer. Math. Soc. 51 (1945), 898–902.
- [4] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003), 89–93.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
