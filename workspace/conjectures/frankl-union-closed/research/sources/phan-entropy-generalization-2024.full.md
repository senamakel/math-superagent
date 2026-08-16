<!-- source: https://arxiv.org/html/2412.18622 | converted from HTML -->

Entropy approach for a generalization of Frankl’s conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2412.18622v1 [math.CO] 17 Dec 2024

# Entropy approach for a generalization of Frankl’s conjecture Thanks: *Ho Chi Minh City; email: [kyubivulpes@gmail.com][3]

Veronica Phan*

###### Abstract.

In this paper, we will use the entropy approach to derive a necessary and sufficient condition for the existence of an element that belongs to at least half of the sets in a finite family of sets.

## 1. Introduction

The union-closed set conjecture, or Frankl’s conjecture, is a famous open problem in combinatorics. A family of set ℱ \mathcal{F} is said to be union-closed if the union of any two sets from ℱ \mathcal{F} belongs to ℱ \mathcal{F} as well.

###### Conjecture (Frankl).

For every finite union-closed family of sets ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}, there exists an element i i such that at least half of the sets in ℱ \mathcal{F} contain i i.

In 2022, Gilmer [1] used entropy method to establish the first constant lower bound 0.01 0.01 for this conjecture, soon later, three preprints [2] [3] [4] improved the bound to 3 − 5 2 \frac{3-\sqrt{5}}{2}, and Lei Yu [5] and Cambie [6] improved it to about 0.38234 0.38234.

In this paper, we won’t just study union-closed family, but arbitrary finite family of sets as well. For S ∈ [n] S\in[n] and family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, denote ℱ ⁡ ( S) \mathcal{F}(S) be the family of sets which have the form S ∪ F, F ∈ ℱ S\cup F,F\in\mathcal{F}. Our main result is:

###### Theorem 1.

For family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, there exists an element i i such that at least half of the sets in ℱ \mathcal{F} contain i i if and only if there exists a family 𝒢 ⊆ 2 [n], | 𝒢 | > 1 \mathcal{G}\subseteq 2^{[n]},|\mathcal{G}|>1 such that

 | ∑ S ∈ ℱ log ⁡ | 𝒢 ⁡ ( S) | ≤ | ℱ | ​ log ⁡ | 𝒢 | 2 \sum_{S\in\mathcal{F}}\log|\mathcal{G}(S)|\leq\frac{|\mathcal{F}|\log|\mathcal{G}|}{2} |  |

.

## 2. Notation and Preliminaries

All the log \log in this paper are of base 2 2. For a random variable X X valued in sets and a set S S, we could define random variables X ∪ S, X / S, … X\cup S,X/S,... in a natural way, and denote H ⁡ ( X), | X | H(X),|X| be the entropy and the number of possible value of | X | |X| For a finite family ℱ \mathcal{F} of set, let X ℱ X_{\mathcal{F}} be a random variable of sets sampled uniformly at random from ℱ \mathcal{F}.

We will use these following properties of entropy:

1. (1)

0 ≤ H ⁡ ( X) ≤ log ⁡ | X | 0\leq H(X)\leq\log|X|

2. (2)

H ⁡ ( X, Y, Z) + H ⁡ ( Z) ≤ H ⁡ ( X, Z) + H ⁡ ( Y, Z) H(X,Y,Z)+H(Z)\leq H(X,Z)+H(Y,Z)

3. (3)

H ⁡ ( X | f ⁡ ( X)) + H ⁡ ( f ⁡ ( X)) = H ⁡ ( X, f ⁡ ( X)) = H ⁡ ( X) H(X|f(X))+H(f(X))=H(X,f(X))=H(X) for function f f.

## 3. Main lemma

First, we will prove the following lemma:

###### Lemma 2.

Let X X be a random variable of sets sampled from 2 [n] 2^{[n]}, then there exists n n nonnegative numbers x 1, x 2, …, x n x_{1},x_{2},...,x_{n} such that H ⁡ ( X) = ∑ i = 1 n x i H(X)=\sum_{i=1}^{n}x_{i} and for every set S ⊆ [n] S\subseteq[n], we have:

 | H ⁡ ( X ∪ S) ≥ ∑ i ∈ [n] / S x i H(X\cup S)\geq\sum_{i\in[n]/S}x_{i} |  |

.

###### Proposition 3.

For every set S ⊆ [n], n ∉ S S\subseteq[n],n\notin S, we have:

 | H ⁡ ( X) − H ⁡ ( X ∪ { n }) ≤ H ⁡ ( X ∪ S) − H ⁡ ( X ∪ S ∪ { n }) H(X)-H(X\cup\{n\})\leq H(X\cup S)-H(X\cup S\cup\{n\}) |  |

###### Proof.

For R ⊆ [n] R\subseteq[n], if we know R ∪ S R\cup S and R ∪ { n } R\cup\{n\}, we could determine R R, which is R ∪ { n } R\cup\{n\} if n ∈ R ∪ S n\in R\cup S and ( R ∪ { n }) / { n } (R\cup\{n\})/\{n\} if otherwise. From this, we could deduce that H ⁡ ( X) = H ⁡ ( X, X ∪ S, X ∪ { n }) = H ⁡ ( X ∪ S, X ∪ { n }) H(X)=H(X,X\cup S,X\cup\{n\})=H(X\cup S,X\cup\{n\}).

Now we have:

 | H ⁡ ( X ∪ S, X ∪ { n }, X ∪ S ∪ { n }) + H ⁡ ( X ∪ S ∪ { n }) ≤ H ⁡ ( X ∪ S, X ∪ S ∪ { n }) + H ⁡ ( X ∪ { n }, X ∪ S ∪ { n }) ⇒ H ⁡ ( X) + H ⁡ ( X ∪ S ∪ { n }) ≤ H ⁡ ( X ∪ S) + H ⁡ ( X ∪ { n }) ⇒ H ⁡ ( X) − H ⁡ ( X ∪ { n }) ≤ H ⁡ ( X ∪ S) − H ⁡ ( X ∪ S ∪ { n }) \begin{split}&H(X\cup S,X\cup\{n\},X\cup S\cup\{n\})+H(X\cup S\cup\{n\})\leq H(X\cup S,X\cup S\cup\{n\})+H(X\cup\{n\},X\cup S\cup\{n\})\\ &\Rightarrow H(X)+H(X\cup S\cup\{n\})\leq H(X\cup S)+H(X\cup\{n\})\\ &\Rightarrow H(X)-H(X\cup\{n\})\leq H(X\cup S)-H(X\cup S\cup\{n\})\end{split} |  |

∎

###### Proof of lemma 2.

We will prove by induction on n n. For n = 1 n=1, we could choose x 1 = H ⁡ ( X) x_{1}=H(X) and it’s easy to show x 1 x_{1} satisfies the lemma.

Assume the lemma is true with n = k − 1 n=k-1. For n = k n=k and random variable X X of sets sampled from 2 [n] 2^{[n]}, consider ( X ∪ { n }) / { n } (X\cup\{n\})/\{n\} and view it as random variable of sets sampled from 2 [n − 1] 2^{[n-1]}. Apply the induction hypothesis, there exists nonnegative numbers x 1, x 2, …, x n − 1 x_{1},x_{2},...,x_{n-1} such that H ⁡ ( X ∪ { n }) = H ⁡ ( ( X ∪ { n }) / { n }) = ∑ i = 1 n − 1 x i H(X\cup\{n\})=H((X\cup\{n\})/\{n\})=\sum_{i=1}^{n-1}x_{i} and for every set S ∈ [n − 1] S\in[n-1], we have:

 | H ⁡ ( X ∪ S ∪ { n }) = H ⁡ ( ( ( X ∪ { n }) / { n }) ∪ S) ≥ ∑ i ∈ [n − 1] / S x i H(X\cup S\cup\{n\})=H(((X\cup\{n\})/\{n\})\cup S)\geq\sum_{i\in[n-1]/S}x_{i} |  |

Now we take x n = H ⁡ ( X | X ∪ { n }) = H ⁡ ( X) − H ⁡ ( X ∪ { n }) ≥ 0 x_{n}=H(X|X\cup\{n\})=H(X)-H(X\cup\{n\})\geq 0, then we just need to check H ⁡ ( X ∪ S) ≥ ∑ [n] / S x i H(X\cup S)\geq\sum_{[n]/S}x_{i} for every set S ⊆ [n], n ∉ S S\subseteq[n],n\notin S. By proposition 3 we have:

 | ∑ i ∈ [n] / S x i = ∑ i ∈ [n − 1] / S x i + x n ≤ H ⁡ ( X ∪ S ∪ { n }) + ( H ⁡ ( X ∪ S) − H ⁡ ( X ∪ S ∪ { n })) = H ⁡ ( X ∪ S) \begin{split}\sum_{i\in[n]/S}x_{i}&=\sum_{i\in[n-1]/S}x_{i}+x_{n}\\ &\leq H(X\cup S\cup\{n\})+(H(X\cup S)-H(X\cup S\cup\{n\}))\\ &=H(X\cup S)\end{split} |  |

as we want. ∎

## 4. Proof of the main theorem

For finite family of sets ℱ \mathcal{F}, denote w ℱ ​ ( i) w_{\mathcal{F}}(i) be the number of sets in ℱ \mathcal{F} that not contain i i.

###### Proof of theorem 1.

Only if: Take i ∈ [n] i\in[n] such that at least half of the sets in ℱ \mathcal{F} contain i i, then w ℱ ​ ( i) ≤ | ℱ | 2 w_{\mathcal{F}}(i)\leq\frac{|\mathcal{F}|}{2}. We take 𝒢 = { ∅, { i } } \mathcal{G}=\{\emptyset,\{i\}\}, then | 𝒢 | = 2 |\mathcal{G}|=2, for S ∈ ℱ S\in\mathcal{F}, | 𝒢 ⁡ ( S) | = | { S } | = 1 |\mathcal{G}(S)|=|\{S\}|=1 if i ∈ S i\in S and | 𝒢 ( S) | = | { S, S ∪ { i } | = 2 |\mathcal{G}(S)|=|\{S,S\cup\{i\}|=2 if otherwise, so we have:

 | ∑ S ∈ ℱ log ⁡ | 𝒢 ⁡ ( S) | = ∑ S ∈ ℱ, i ∈ S log ⁡ | 𝒢 ⁡ ( S) | + ∑ S ∈ ℱ, i ∉ S log ⁡ | 𝒢 ⁡ ( S) | = ( | ℱ | − w ℱ ​ ( i)) ​ log ⁡ 1 + w ℱ ​ ( i) ​ log ⁡ 2 = w ℱ ​ ( i) ≤ | ℱ | 2 = | ℱ | ​ log ⁡ | 𝒢 | 2 \begin{split}\sum_{S\in\mathcal{F}}\log|\mathcal{G}(S)|&=\sum_{S\in\mathcal{F},i\in S}\log|\mathcal{G}(S)|+\sum_{S\in\mathcal{F},i\notin S}\log|\mathcal{G}(S)|\\ &=(|\mathcal{F}|-w_{\mathcal{F}}(i))\log 1+w_{\mathcal{F}}(i)\log 2=w_{\mathcal{F}}(i)\\ &\leq\frac{|\mathcal{F}|}{2}=\frac{|\mathcal{F}|\log|\mathcal{G}|}{2}\end{split} |  |

If: For family of sets 𝒢 \mathcal{G} satisfies the condition of the theorem, take n n nonnegative numbers x 1, x 2, …, x n x_{1},x_{2},...,x_{n} by applying lemma 2 for the random variable X 𝒢 X_{\mathcal{G}}, then we have:

 | ∑ i = 1 n x i ​ w ℱ ​ ( i) = ∑ i = 1 n ∑ S ∈ ℱ, i ∉ S x i = ∑ S ∈ ℱ ∑ i ∈ [n] / S x i ≤ ∑ S ∈ ℱ H ⁡ ( X 𝒢 ∪ S) ≤ ∑ S ∈ ℱ log ⁡ | X 𝒢 ∪ S | = ∑ S ∈ ℱ log ⁡ | 𝒢 ⁡ ( S) | ≤ | ℱ | ​ log ⁡ | 𝒢 | 2 = | ℱ | ​ H ​ ( X 𝒢) 2 = | ℱ | 2 ​ ∑ i = 1 n x i \begin{split}\sum_{i=1}^{n}x_{i}w_{\mathcal{F}}(i)&=\sum_{i=1}^{n}\sum_{S\in\mathcal{F},i\notin S}x_{i}\\ &=\sum_{S\in\mathcal{F}}\sum_{i\in[n]/S}x_{i}\\ &\leq\sum_{S\in\mathcal{F}}H(X_{\mathcal{G}}\cup S)\\ &\leq\sum_{S\in\mathcal{F}}\log|X_{\mathcal{G}}\cup S|\\ &=\sum_{S\in\mathcal{F}}\log|\mathcal{G}(S)|\\ &\leq\frac{|\mathcal{F}|\log|\mathcal{G}|}{2}\\ &=\frac{|\mathcal{F}|H(X_{\mathcal{G}})}{2}=\frac{|\mathcal{F}|}{2}\sum_{i=1}^{n}x_{i}\end{split} |  |

so there exists i ∈ [n] i\in[n] such that w ℱ ​ ( i) ≤ | ℱ | 2 w_{\mathcal{F}}(i)\leq\frac{|\mathcal{F}|}{2} (as ∑ i = 1 n x i = H ⁡ ( X 𝒢) = log ⁡ | 𝒢 | > 0 \sum_{i=1}^{n}x_{i}=H(X_{\mathcal{G}})=\log|\mathcal{G}|>0), in other word, at least half of the sets in ℱ \mathcal{F} contain i i ∎

###### Corollary 4.

The union-closed conjecture is true for finite union-closed family of sets ℱ \mathcal{F} if there exists subfamily 𝒢 ⊆ ℱ, | 𝒢 | > 1 \mathcal{G}\subseteq\mathcal{F},|\mathcal{G}|>1 such that:

 | ∑ S ∈ ℱ log ⁡ | 𝒢 ⁡ ( S) | ≤ | ℱ | ​ log ⁡ | 𝒢 | 2 \sum_{S\in\mathcal{F}}\log|\mathcal{G}(S)|\leq\frac{|\mathcal{F}|\log|\mathcal{G}|}{2} |  |

This corollary does not depend on the base set but only the union structure of the family ℱ \mathcal{F}. We have some strategies to prove the union-closed conjecture for ℱ \mathcal{F}

A natural way to choose the subfamily 𝒢 \mathcal{G} is the family ℱ \mathcal{F} itself, but the condition ∑ S ∈ ℱ log ⁡ | ℱ ⁡ ( S) | ≤ | ℱ | ​ log ⁡ | ℱ | 2 \sum_{S\in\mathcal{F}}\log|\mathcal{F}(S)|\leq\frac{|\mathcal{F}|\log|\mathcal{F}|}{2} is not always true, for example ℱ = { ∅, { 1 }, { 1, 2 } } \mathcal{F}=\{\emptyset,\{1\},\{1,2\}\}. We may need another quantity on random variable valued on sets which behave like entropy to prove the union-closed conjecture this way.

Another strategy is note that the union-closed conjecture is true for ℱ \mathcal{F} if it is true for ℱ N \mathcal{F}^{N} for some N N. For very small ϵ > 0 \epsilon>0 and very large N N depend on ϵ \epsilon, take 𝒢 \mathcal{G} be the subfamily of ℱ N \mathcal{F}^{N} consist all the set S S such that | ℱ N ​ ( S) | ≥ | ℱ | ϵ ⁡ ( N − 2) |\mathcal{F}^{N}(S)|\geq|\mathcal{F}|^{\epsilon(N-2)}. We expect that for many cases, | 𝒢 | ≤ ( 1 2 − ϵ) ​ | ℱ N | |\mathcal{G}|\leq(\frac{1}{2}-\epsilon)|\mathcal{F}^{N}|, then:

 | ∑ S ∈ ℱ N log ⁡ | 𝒢 ⁡ ( S) | = ∑ S ∈ 𝒢 log ⁡ | 𝒢 ⁡ ( S) | + ∑ S ∈ ℱ N / 𝒢 log ⁡ | 𝒢 ⁡ ( S) | ≤ ∑ S ∈ 𝒢 log ⁡ | 𝒢 | + ∑ S ∈ ℱ N / 𝒢 log ⁡ | ℱ 𝒩 ​ ( S) | ≤ | 𝒢 | ​ log ⁡ | 𝒢 | + | ℱ N ​ | log | ​ ℱ | ϵ ⁡ ( N − 2) ≤ ( 1 2 − ϵ) ​ | ℱ N ​ | log ⁡ | 𝒢 | + | ​ ℱ N | ​ ( log ⁡ | ℱ | N ​ ϵ − log ⁡ | ℱ | 2 ​ ϵ) ≤ ( 1 2 − ϵ) ​ | ℱ N ​ | log ⁡ | 𝒢 | + | ​ ℱ N | ​ ( log ⁡ | ℱ N | ϵ − log ⁡ 2 2 ​ ϵ) = ( 1 2 − ϵ) ​ | ℱ N | ​ log | 𝒢 | + ϵ ⁡ ( | ℱ N | ​ ( log ⁡ | ℱ N | − 2) CLOSE ≤ ( 1 2 − ϵ) ​ | ℱ N | ​ log | 𝒢 | + ϵ ⁡ ( | ℱ N | ​ ( log ⁡ | 𝒢 |) = | ℱ N | ​ log ⁡ | 𝒢 | 2 CLOSE \begin{split}\sum_{S\in\mathcal{F}^{N}}\log|\mathcal{G}(S)|&=\sum_{S\in\mathcal{G}}\log|\mathcal{G}(S)|+\sum_{S\in\mathcal{F}^{N}/\mathcal{G}}\log|\mathcal{G}(S)|\\ &\leq\sum_{S\in\mathcal{G}}\log|\mathcal{G}|+\sum_{S\in\mathcal{F}^{N}/\mathcal{G}}\log|\mathcal{F^{N}}(S)|\\ &\leq|\mathcal{G}|\log|\mathcal{G}|+|\mathcal{F}^{N}|\log|\mathcal{F}|^{\epsilon(N-2)}\\ &\leq(\frac{1}{2}-\epsilon)|\mathcal{F}^{N}|\log|\mathcal{G}|+|\mathcal{F}^{N}|(\log|\mathcal{F}|^{N\epsilon}-\log|\mathcal{F}|^{2\epsilon})\\ &\leq(\frac{1}{2}-\epsilon)|\mathcal{F}^{N}|\log|\mathcal{G}|+|\mathcal{F}^{N}|(\log|\mathcal{F}^{N}|^{\epsilon}-\log 2^{2\epsilon})\\ &=(\frac{1}{2}-\epsilon)|\mathcal{F}^{N}|\log|\mathcal{G}|+\epsilon(|\mathcal{F}^{N}|(\log|\mathcal{F}^{N}|-2)\\ &\leq(\frac{1}{2}-\epsilon)|\mathcal{F}^{N}|\log|\mathcal{G}|+\epsilon(|\mathcal{F}^{N}|(\log|\mathcal{G}|)=\frac{|\mathcal{F}^{N}|\log|\mathcal{G}|}{2}\end{split} |  |

so ℱ N \mathcal{F}^{N} as well as ℱ \mathcal{F} statisfies the union-closed conjecture.

## References

- [1] Justin Gilmer. ”A constant lower bound for the union-closed sets conjecture”. arXiv: [2211.09055][4].
- [2] Zachary Chase, Shachar Lovett. ”Approximate union closed conjecture”. arXiv: [2211.11689][5].
- [3] Ryan Alweiss, Brice Huang, Mark Sellke. ”Improved Lower Bound for Frankl’s Union-Closed Sets Conjecture”. arXiv: [2211.11731][6].
- [4] Will Sawin. ”An improved lower bound for the union-closed set conjecture”. arXiv: [2211.11504][7].
- [5] Lei Yu. ”Dimension-Free Bounds for the Union-Closed Sets Conjecture”. arXiv: [2212.00658][8].
- [6] Stijn Cambie. ”Better bounds for the union-closed sets conjecture using the entropy approach”. arXiv: [2212.12500][9].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:kyubivulpes@gmail.com
[4]: https://arxiv.org/pdf/2211.09055
[5]: https://arxiv.org/pdf/2211.11689
[6]: https://arxiv.org/pdf/2211.11731
[7]: https://arxiv.org/pdf/2211.11504
[8]: https://arxiv.org/pdf/2212.00658
[9]: https://arxiv.org/pdf/2212.12500
