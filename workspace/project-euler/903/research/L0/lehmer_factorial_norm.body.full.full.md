<!-- source: https://ar5iv.labs.arxiv.org/html/2111.03951 | converted from HTML -->

[2111.03951] The Lehmer factorial norm on S n

# The Lehmer factorial norm on S n S_{n}

Paweł Zawiślak Affiliation: Department of Mathematics and Mathematical Economics Affiliation: SGH Warsaw School of Economics Affiliation: Al. Niepodległości 162, 02-554 Warszawa, Poland Affiliation: E-mail: pzawis@sgh.waw.pl

August 9, 2026

###### Abstract

We introduce a new family of norms on the permutation groups S n S_{n}. We examine their properties.

† † 2020 *Mathematics Subject Classification*: 05A05, 62H20, 54E35, 20B99 † †*Key words and phrases*: Lehmer code, Lehmer factorial norm, permutation

## 1 Introduction

Metrics on the permutation groups S n S_{n} were considered in many different contexts.

On one side, permutations can be used used as rankings, therefore some metrics on permutations originate from attempts of comparing rankings. Many well known measures of similarity between rankings lead to definition of metric on S n S_{n}. The most popular measures of similarity are Kendall’s τ \tau ( [K]) and Spearman’s ρ \rho ( [S]). These two measures leads to Kendall’s distance and Spearman’s distance. Together with Spearman footrule (also known as Manhattan distance) and Hamming distance, these four metrics are the most popular metrics on S n S_{n} used in the statistics ( [DG] and [DH]).

The generalisations of these metrics in many different contexts we considered for example in [KW], [LH], [LZH], [KV], [QDRL], [LY1], [LY2], [WSSC], [FSS] and [PP].

On the other side, the study of statistical properties of natural valued functions on S n S_{n} has almost two hundred years of history, started with [R] and [M], and continued by many authors (see for example [FZ], [SS] and [CSZ]).

On the third side, natural inclusions of S k S_{k} in S l S_{l} (for k < l k<l) lead to a limit object S ∞ S_{\infty}. Metrics on some limit objects related to groups were explored for example in [C], [TW], [W] and [GMZ].

In this paper we present a slightly different approach, which can be considered as transversal to the previous three. The demand for the metric satisfying conditions ( i)-( vii) of Theorem 3.6 comes from the analysis of the votings’ networks. Presicely, all most popular metrics on S n S_{n} do not differentiate between the change on first two positions of the ranking and the change on last two positions. The metric coming from the norm presented in this paper do – see Theorem 3.6 ( iii). Additionally, Theorems 4.5 and 4.6 describe distributions of the new norm (we call it the Lehmer norm) on all permutation groups S n S_{n} as well as its distribution on S ∞ S_{\infty}.

We do not consider many others research contexts of permutations metrics. For more of these contexts see for example [DH].

This paper is organised as follows. Section 2 contains the basic definitions and notation. In Section 3 we define the main object of this article - the Lehmer factorial norm. The definition bases on the notion on the Lehmer code. The properties of the Lehmer code are described in Lemmas 3.1 and 3.3 as well as in Corollary 3.2. Theorem 3.6 contains the basic attributes of the Lehmer norm. In Section 4 we focus on the distribution of the Lehmer norm. This distribution is fully described in Theorems 4.5 and 4.6 together with Lemma 4.4.

## 2 Basic definitions and notation

In this section we recall some basic definitions used in this paper as well as we set some notation.

In this article ℕ \mathbb{N} denotes the set of all natural numbers, starting at 0 0, whereas ℕ + \mathbb{N}_{+} – the set of all positive natural numbers. For n ∈ ℕ + n\in\mathbb{N}_{+} by [n] [n] we denote the set { 1, 2, …, n } \{1,2,\ldots,n\} and by S n S_{n} – the group of all permutations of [n] [n]. S ∞ S_{\infty} stands for the group of all permutations of ℕ + \mathbb{N}_{+} with a finite support.

A permutation σ ∈ S n \sigma\in S_{n} is denoted by

 | σ = ( σ ⁡ ( 1), σ ⁡ ( 2), …, σ ⁡ ( n)) \sigma=(\sigma(1),\sigma(2),\ldots,\sigma(n)) |  |

In particular e n = ( 1, 2, …, n) e_{n}=(1,2,\ldots,n) denotes the identity permutation.

By σ − 1 \sigma^{-1} we denote the inverse permutation to σ \sigma, by σ ​ τ \sigma\tau – the composition of σ \sigma and τ \tau, defined by ( σ ​ τ) ​ ( i) = σ ⁡ ( τ ⁡ ( i)) (\sigma\tau)(i)=\sigma(\tau(i)) for i = 1, 2, …, n i=1,2,\ldots,n, whereas σ ¯ \bar{\sigma} stands for the permutation reverse to σ \sigma, given by σ ¯ ​ ( i) = σ ​ ( n + 1 − i) \bar{\sigma}(i)=\sigma(n+1-i) for i = 1, 2, …, n i=1,2,\ldots,n.

For s = 1, 2, …, n − 1 s=1,2,\ldots,n-1 let

 | σ s = ( 1, 2, …, s − 1, s + 1, s, s + 2, …, n) \sigma_{s}=(1,2,\ldots,s-1,s+1,s,s+2,\ldots,n) |  |

(so σ s \sigma_{s} is the adjacent transposition – ( s, s + 1) (s,s+1) in the cycle notation).

###### Definition 2.1.

For a permutation σ ∈ S n \sigma\in S_{n} its *Lehmer code*lc ⁡ ( σ) \lehmer(\sigma) (see [G]) is defined by

 | lc ⁡ ( σ) = [c 1 ​ ( σ), c 2 ​ ( σ), …, c n ​ ( σ)] \lehmer(\sigma)=[c_{1}(\sigma),c_{2}(\sigma),\ldots,c_{n}(\sigma)] |  |

where the numbers c i ​ ( σ) c_{i}(\sigma) (for i = 1, 2, …, n i=1,2,\ldots,n) are given by

 | c i ​ ( σ) = | { j ∈ [n]: j > i ​ and ​ σ ​ ( j) < σ ⁡ ( i) } | c_{i}(\sigma)=\left|\{j\in[n]:j>i\textrm{ and }\sigma(j)<\sigma(i)\}\right| |  |

The Lehmer code of σ \sigma coincides with the factorial number system representation of its position in the list of permutations of [n] [n] in the lexicographical order (numbering the positions starting from 0 0) – compare [G] to [L1] and [L2].

The Lehmer codes of permutations σ ∈ S 3 \sigma\in S_{3} are presented in Table 1.

## 3 The Lehmer factorial norm

In this section we define the Lehmer factorial norm on the group S n S_{n}. We also examine its basic features.

We start with establishing some basic properties of the Lehmer code. To do this, we need some technical notation. For a permutation σ ∈ S n \sigma\in S_{n} and for i = 1, 2, …, n i=1,2,\ldots,n let

 | C ​ ( σ) i = { j ∈ [n]: j > i ​ and ​ σ ​ ( j) < σ ⁡ ( i) } ​ and ​ A ​ ( σ) i = [i] ∪ C ​ ( σ) i C(\sigma)_{i}=\{j\in[n]:j>i\textrm{ and }\sigma(j)<\sigma(i)\}\textrm{ and }A(\sigma)_{i}=[i]\cup C(\sigma)_{i} |  |

Note, that if we denote the cardinality of X X by | X | |X|, then | C ​ ( σ) i | = c i ​ ( σ) |C(\sigma)_{i}|=c_{i}(\sigma) and | A ​ ( σ) i | = i + c i ​ ( σ) |A(\sigma)_{i}|=i+c_{i}(\sigma).

###### Lemma 3.1.

For all permutations σ, τ ∈ S n \sigma,\tau\in S_{n} and for all i = 1, 2, …, n i=1,2,\ldots,n the following hold:

1. (i)

σ ⁡ ( i) ≤ i + c i ​ ( σ) \sigma(i)\leq i+c_{i}(\sigma),

2. (ii)

c i ​ ( σ ​ τ) ≤ c i ​ ( τ) + c τ ⁡ ( i) ​ ( σ) c_{i}(\sigma\tau)\leq c_{i}(\tau)+c_{\tau(i)}(\sigma),

3. (iii)

σ − 1 \sigma^{-1} determines the bijection between A ​ ( σ − 1) σ ⁡ ( i) A(\sigma^{-1})_{\sigma(i)} and A ​ ( σ) i A(\sigma)_{i}. In particular

 | i + c i ​ ( σ) = σ ⁡ ( i) + c σ ⁡ ( i) ​ ( σ − 1) i+c_{i}(\sigma)=\sigma(i)+c_{\sigma(i)}(\sigma^{-1}) |  |

Proof. ( i) Note that | { j ∈ [n]: j > i } | = n − i |\{j\in[n]:j>i\}|=n-i, so

 | | { j ∈ [n]: j > i ​ and ​ σ ​ ( j) > σ ⁡ ( i) } | = n − i − c i ​ ( σ) |\{j\in[n]:j>i\textrm{ and }\sigma(j)>\sigma(i)\}|=n-i-c_{i}(\sigma) |  |

On the other hand

 | | { σ ⁡ ( j): j ∈ [n] ​ and ​ σ ​ ( j) > σ ⁡ ( i) } | = n − σ ⁡ ( i) |\{\sigma(j):j\in[n]\textrm{ and }\sigma(j)>\sigma(i)\}|=n-\sigma(i) |  |

And since

 | σ ⁡ [{ j ∈ [n]: j > i ​ and ​ σ ​ ( j) > σ ⁡ ( i) }] ⊆ { σ ⁡ ( j): j ∈ [n] ​ and ​ σ ​ ( j) > σ ⁡ ( i) } \sigma\Big[\{j\in[n]:j>i\textrm{ and }\sigma(j)>\sigma(i)\}\Big]\subseteq\{\sigma(j):j\in[n]\textrm{ and }\sigma(j)>\sigma(i)\} |  |

it follows that n − i − c i ​ ( σ) ≤ n − σ ⁡ ( i) n-i-c_{i}(\sigma)\leq n-\sigma(i).

( ii) Choose k ∈ C ​ ( σ ​ τ) i k\in C(\sigma\tau)_{i}. If τ ⁡ ( k) < τ ⁡ ( i) \tau(k)<\tau(i), then k ∈ C ​ ( τ) i k\in C(\tau)_{i}. Otherwise τ ⁡ ( k) > τ ⁡ ( i) \tau(k)>\tau(i) and σ ⁡ ( τ ⁡ ( k)) < σ ⁡ ( τ ⁡ ( i)) \sigma(\tau(k))<\sigma(\tau(i)), therefore τ ⁡ ( k) ∈ C ​ ( σ) τ ⁡ ( i) \tau(k)\in C(\sigma)_{\tau(i)}.

( iii) Choose k ∈ A ​ ( σ − 1) σ ⁡ ( i) k\in A(\sigma^{-1})_{\sigma(i)} and let l = σ − 1 ​ ( k) l=\sigma^{-1}(k). We will show that l ∈ A ​ ( σ) i l\in A(\sigma)_{i}. There are two possible cases.

1. (a)

k ≤ σ ⁡ ( i) k\leq\sigma(i): If l ≤ i l\leq i, then l ∈ [i] ⊆ A ​ ( σ) i l\in[i]\subseteq A(\sigma)_{i}. Otherwise l > i l>i, and since σ ⁡ ( l) = k ≤ σ ⁡ ( i) \sigma(l)=k\leq\sigma(i), it follows that σ ⁡ ( l) < σ ⁡ ( i) \sigma(l)<\sigma(i) hence l ∈ C ​ ( σ) i ⊆ A ​ ( σ) i l\in C(\sigma)_{i}\subseteq A(\sigma)_{i}.

2. (b)

k > σ ⁡ ( i) k>\sigma(i): Therefore k ∈ C ​ ( σ − 1) σ ⁡ ( i) k\in C(\sigma^{-1})_{\sigma(i)}, so l = σ − 1 ​ ( k) < σ − 1 ​ ( σ ⁡ ( i)) = i l=\sigma^{-1}(k)<\sigma^{-1}(\sigma(i))=i and thus l ∈ [i] ⊆ A ​ ( σ) i l\in[i]\subseteq A(\sigma)_{i}.

We have shown that σ − 1 ​ [A ​ ( σ − 1) σ ⁡ ( i)] ⊆ A ​ ( σ) i \sigma^{-1}\left[A(\sigma^{-1})_{\sigma(i)}\right]\subseteq A(\sigma)_{i}. Replacing σ \sigma with σ − 1 \sigma^{-1} leads to the second inclusion, which completes the proof. ∎

As an obvious conclusion of Lemma 3.1 ( iii) we get:

###### Corollary 3.2.

Elements of the Lehmer code of the inverse permutation to σ \sigma are given by

 | c i ​ ( σ − 1) = c σ − 1 ​ ( i) ​ ( σ) + σ − 1 ​ ( i) − i c_{i}(\sigma^{-1})=c_{\sigma^{-1}(i)}(\sigma)+\sigma^{-1}(i)-i |  |

for i = 1, 2, …, n i=1,2,\ldots,n.

In the next lemma we describe how the Lehmer code changes when a permutation is multiplied by an adjacent transposition.

###### Lemma 3.3.

1. (i)

c i ​ ( σ s) = δ i ​ s c_{i}(\sigma_{s})=\delta_{is} (the Kronecker delta) for i = 1, 2, …, n i=1,2,\ldots,n and s = 1, 2, …, n − 1 s=1,2,\ldots,n-1.

2. (ii)

Let τ = σ ​ σ s \tau=\sigma\sigma_{s}. If σ ⁡ ( s) < σ ⁡ ( s + 1) \sigma(s)<\sigma(s+1), then

 | { c i ​ ( τ) = c i ​ ( σ) ​ for ​ i ≠ s, s + 1 c s ​ ( τ) = c s + 1 ​ ( σ) + 1 c s + 1 ​ ( τ) = c s ​ ( σ) \begin{cases}c_{i}(\tau)=c_{i}(\sigma)\textrm{ for }i\neq s,s+1\\ c_{s}(\tau)=c_{s+1}(\sigma)+1\\ c_{s+1}(\tau)=c_{s}(\sigma)\end{cases} |  |

otherwise

 | { c i ​ ( τ) = c i ​ ( σ) ​ for ​ i ≠ s, s + 1 c s ​ ( τ) = c s + 1 ​ ( σ) c s + 1 ​ ( τ) = c s ​ ( σ) − 1 \begin{cases}c_{i}(\tau)=c_{i}(\sigma)\textrm{ for }i\neq s,s+1\\ c_{s}(\tau)=c_{s+1}(\sigma)\\ c_{s+1}(\tau)=c_{s}(\sigma)-1\end{cases} |  |

Proof. ( i) Follows definitions of the Lehmer code and σ s \sigma_{s}.

( ii) Note first, that

 | τ = ( σ ⁡ ( 1), σ ⁡ ( 2), …, σ ⁡ ( s − 1), σ ⁡ ( s + 1), σ ⁡ ( s), σ ⁡ ( s + 2), …, σ ⁡ ( n)) \tau=(\sigma(1),\sigma(2),\ldots,\sigma(s-1),\sigma(s+1),\sigma(s),\sigma(s+2),\ldots,\sigma(n)) |  |

Threrefore c i ​ ( σ) = c i ​ ( τ) c_{i}(\sigma)=c_{i}(\tau) for i ≠ s, s + 1 i\neq s,s+1 (for i < s i<s we have: s ∈ C ​ ( σ) i s\in C(\sigma)_{i} if and only if s + 1 ∈ C ​ ( τ) i s+1\in C(\tau)_{i}).

Suppose that σ ⁡ ( s) < σ ⁡ ( s + 1) \sigma(s)<\sigma(s+1). In this case

 | C ​ ( τ) s = C ​ ( σ) s + 1 ∪ { s + 1 } ​ and ​ C ​ ( τ) s + 1 = C ​ ( σ) s C(\tau)_{s}=C(\sigma)_{s+1}\cup\{s+1\}\textrm{ and }C(\tau)_{s+1}=C(\sigma)_{s} |  |

If σ ⁡ ( s) > σ ⁡ ( s + 1) \sigma(s)>\sigma(s+1), then

 | C ​ ( τ) s = C ​ ( σ) s + 1 ​ and ​ C ​ ( τ) s + 1 = C ​ ( σ) s ∖ { s + 1 } C(\tau)_{s}=C(\sigma)_{s+1}\textrm{ and }C(\tau)_{s+1}=C(\sigma)_{s}\setminus\{s+1\} |  |

This finishes the proof. ∎

Now we are ready to define the Lehmer factorial norm on S n S_{n}.

###### Definition 3.4.

Let σ ∈ S n \sigma\in S_{n} be a permutation with the Lehmer code

 | lc ⁡ ( σ) = [c 1 ​ ( σ), c 2 ​ ( σ), …, c n ​ ( σ)] = [k n − 1 ​ ( σ), k n − 2 ​ ( σ), …, k 0 ​ ( σ)] \lehmer(\sigma)=[c_{1}(\sigma),c_{2}(\sigma),\ldots,c_{n}(\sigma)]=[k_{n-1}(\sigma),k_{n-2}(\sigma),\ldots,k_{0}(\sigma)] |  |

(here k i ​ ( σ) = c n − i ​ ( σ) k_{i}(\sigma)=c_{n-i}(\sigma) for i = 0, 1, …, n − 1 i=0,1,\ldots,n-1). The *Lehmer factorial norm (with base 2 2)*ℒ ​ ℱ 2: S n → ℕ \mathcal{LF}_{2}:S_{n}\to\mathbb{N} is given by

 | ℒ ​ ℱ 2 ​ ( σ) = ∑ i = 0 n − 1 [2 i − 2 i − k i ​ ( σ)] \mathcal{LF}_{2}(\sigma)=\sum_{i=0}^{n-1}\left[2^{i}-2^{i-k_{i}(\sigma)}\right] |  |

###### Remark 3.5.

For a number m ∈ ℕ m\in\mathbb{N} let

 | m = k n − 1 ⋅ ( n − 1)! + … + k 1 ⋅ 1! + k 0 ⋅ 0! m=k_{n-1}\cdot(n-1)!+\ldots+k_{1}\cdot 1!+k_{0}\cdot 0! |  |

be the (unique!) decomposition of m m in such a way, that 0 ≤ k i ≤ i! 0\leq k_{i}\leq i! for i = 0, 1, …, n − 1 i=0,1,\ldots,n-1 (in particular k 0 = 0 k_{0}=0). Therefore m m has the following factorial number system representation

 | k n − 1: …: k 1: 0! k_{n-1}:\ldots:k_{1}:0_{!} |  |

Consider the function L ​ F 2: ℕ → ℕ LF_{2}:\mathbb{N}\to\mathbb{N} given by

 | L ​ F 2 ​ ( m) = L ​ F 2 ​ ( k n − 1 ⋅ ( n − 1)! + … + k 1 ⋅ 1! + k 0 ⋅ 0!) = ∑ i = 0 n − 1 [2 i − 2 i − k i] LF_{2}(m)=LF_{2}\left(k_{n-1}\cdot(n-1)!+\ldots+k_{1}\cdot 1!+k_{0}\cdot 0!\right)=\sum_{i=0}^{n-1}\left[2^{i}-2^{i-k_{i}}\right] |  |

For σ ∈ ℕ \sigma\in\mathbb{N} let n lex ⁡ ( σ) \numbering_{\lex}(\sigma) be the position of σ \sigma in the lexicographical order (numbering starting from 0 0). Then

 | ℒ ​ ℱ 2 ​ ( σ) = L ​ F 2 ​ ( n lex ⁡ ( σ)) \mathcal{LF}_{2}(\sigma)=LF_{2}(\numbering_{\lex}(\sigma)) |  |

The values ℒ ​ ℱ 2 ​ ( σ) \mathcal{LF}_{2}(\sigma) for σ ∈ S 3 \sigma\in S_{3} are presented in Table 1.

The next theorem yields information about the basic properties of the Lehmer norm.

###### Theorem 3.6.

The norm ℒ ​ ℱ 2 \mathcal{LF}_{2} satisfies the following:

1. (i)

ℒ ​ ℱ 2 ​ ( e n) = 0 \mathcal{LF}_{2}(e_{n})=0 is minimal and e n e_{n} (the identity) is the only permutation with this property.

2. (ii)

ℒ ​ ℱ 2 ​ ( e n ¯) = 2 n − ( n + 1) \mathcal{LF}_{2}(\bar{e_{n}})=2^{n}-(n+1) is maximal and e n ¯ \bar{e_{n}} (the reverse of the identity) is the only permutation with this property.

3. (iii)

ℒ ​ ℱ 2 ​ ( σ s) = 2 n − 1 − s \mathcal{LF}_{2}(\sigma_{s})=2^{n-1-s} (recall that σ s \sigma_{s} denotes the adjacent transposition) for s = 1, 2, …, n − 1 s=1,2,\ldots,n-1, and therefore

 | ℒ ​ ℱ 2 ​ ( σ 1) > ℒ ​ ℱ 2 ​ ( σ 2) > … > ℒ ​ ℱ 2 ​ ( σ n − 1) \mathcal{LF}_{2}(\sigma_{1})>\mathcal{LF}_{2}(\sigma_{2})>\ldots>\mathcal{LF}_{2}(\sigma_{n-1}) |  |

4. (iv)

The inclusion ι n: S n → S n + 1 \iota_{n}:S_{n}\to S_{n+1} given by

 | ι n ​ ( σ) = ( 1, σ ⁡ ( 1) + 1, σ ⁡ ( 2) + 1, …, σ ⁡ ( n) + 1) \iota_{n}(\sigma)=(1,\sigma(1)+1,\sigma(2)+1,\ldots,\sigma(n)+1) |  |

preserves ℒ ​ ℱ 2 \mathcal{LF}_{2}.

5. (v)

ℒ ​ ℱ 2 ​ ( σ) = ℒ ​ ℱ 2 ​ ( σ − 1) \mathcal{LF}_{2}(\sigma)=\mathcal{LF}_{2}(\sigma^{-1}) for all σ ∈ S n \sigma\in S_{n}.

6. (vi)

ℒ ​ ℱ 2 ​ ( σ ​ τ) ≤ ℒ ​ ℱ 2 ​ ( σ) + ℒ ​ ℱ 2 ​ ( τ) \mathcal{LF}_{2}(\sigma\tau)\leq\mathcal{LF}_{2}(\sigma)+\mathcal{LF}_{2}(\tau) for all σ, τ ∈ S n \sigma,\tau\in S_{n}.

7. (vii)

Let τ = σ ​ σ s \tau=\sigma\sigma_{s}. Then

 | | ℒ ​ ℱ 2 ​ ( τ) − ℒ ​ ℱ 2 ​ ( σ) | = 2 − min ⁡ { c s ​ ( σ), c s + 1 ​ ( σ) } ​ ℒ ​ ℱ 2 ​ ( σ s) \left|\mathcal{LF}_{2}(\tau)-\mathcal{LF}_{2}(\sigma)\right|=2^{-\min\{c_{s}(\sigma),c_{s+1}(\sigma)\}}\mathcal{LF}_{2}(\sigma_{s}) |  |

Proof. ( i) Note that ℒ ​ ℱ 2 ​ ( σ) ≥ 0 \mathcal{LF}_{2}(\sigma)\geq 0 with the equality holds only if k i ​ ( σ) = 0 k_{i}(\sigma)=0 for i = 0, 1, …, n − 1 i=0,1,\ldots,n-1. In such a case σ = e n \sigma=e_{n}.

( ii) The proof is similar to the one of ( i). Namely, ℒ ​ ℱ 2 ​ ( σ) \mathcal{LF}_{2}(\sigma) is maximal only if k i ​ ( σ) = i k_{i}(\sigma)=i for i = 0, 1, …, n − 1 i=0,1,\ldots,n-1 and this implies σ = e ¯ n \sigma=\bar{e}_{n}.

( iii) It is enough to see that c i ​ ( σ s) = δ i ​ s c_{i}(\sigma_{s})=\delta_{is} (see Lemma 3.3 ( i)).

( iv) Follows the fact that for σ = ( σ ⁡ ( 1), σ ⁡ ( 2), …, σ ⁡ ( n)) \sigma=(\sigma(1),\sigma(2),\ldots,\sigma(n)) and ι n ​ ( σ) = ( 1, 1 + σ ⁡ ( 1), 1 + σ ⁡ ( 2), …, 1 + σ ⁡ ( n)) \iota_{n}(\sigma)=(1,1+\sigma(1),1+\sigma(2),\ldots,1+\sigma(n)) we have c 1 ​ ( ι n ​ ( σ)) = 0 c_{1}(\iota_{n}(\sigma))=0 and c i ​ ( ι n ​ ( σ)) = c i − 1 ​ ( σ) c_{i}(\iota_{n}(\sigma))=c_{i-1}(\sigma) for i = 2, 3, …, n + 1 i=2,3,\ldots,n+1.

( v) First note, that

 | ℒ ​ ℱ 2 ​ ( σ) = ∑ i = 0 n − 1 [2 i − 2 i − k i ​ ( σ)] = ∑ i = 0 n − 1 [2 i − 2 i − c n − i ​ ( σ)] = ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( σ)] \mathcal{LF}_{2}(\sigma)=\sum_{i=0}^{n-1}\left[2^{i}-2^{i-k_{i}(\sigma)}\right]=\sum_{i=0}^{n-1}\left[2^{i}-2^{i-c_{n-i}(\sigma)}\right]=\sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\sigma)}\right] |  |

Consequently, the equality ℒ ​ ℱ 2 ​ ( σ) = ℒ ​ ℱ 2 ​ ( σ − 1) \mathcal{LF}_{2}(\sigma)=\mathcal{LF}_{2}(\sigma^{-1}) is equivalent to

 | ∑ j = 1 n 2 n − j − c j ​ ( σ) = ∑ j = 1 n 2 n − j − c j ​ ( σ − 1) \sum_{j=1}^{n}2^{n-j-c_{j}(\sigma)}=\sum_{j=1}^{n}2^{n-j-c_{j}(\sigma^{-1})} |  |

Now according to Corollary 3.2

 | n − j − c j ​ ( σ − 1) = n − j − [c σ − 1 ​ ( j) ​ ( σ) + σ − 1 ​ ( j) − j] = n − σ − 1 ​ ( j) − c σ − 1 ​ ( j) ​ ( σ) n-j-c_{j}(\sigma^{-1})=n-j-[c_{\sigma^{-1}(j)}(\sigma)+\sigma^{-1}(j)-j]=n-\sigma^{-1}(j)-c_{\sigma^{-1}(j)}(\sigma) |  |

hence it is enough to notice that

 | ∑ j = 1 n 2 n − j − c j ​ ( σ) = ∑ j = 1 n 2 n − σ − 1 ​ ( j) − c σ − 1 ​ ( j) ​ ( σ) \sum_{j=1}^{n}2^{n-j-c_{j}(\sigma)}=\sum_{j=1}^{n}2^{n-\sigma^{-1}(j)-c_{\sigma^{-1}(j)}(\sigma)} |  |

is just change of order of summation. The last equality holds since for j j taking all values from [n] [n] the same holds for σ − 1 ​ ( j) \sigma^{-1}(j).

( vi) We have the following equalities:

 | ℒ ​ ℱ 2 ​ ( σ) = ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( σ)] \mathcal{LF}_{2}(\sigma)=\sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\sigma)}\right] |  |

 | ℒ ​ ℱ 2 ​ ( τ) = ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( τ)] \mathcal{LF}_{2}(\tau)=\sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\tau)}\right] |  |

and

 | ℒ ​ ℱ 2 ​ ( σ ​ τ) = ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( σ ​ τ)] \mathcal{LF}_{2}(\sigma\tau)=\sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\sigma\tau)}\right] |  |

Therefore the inequality

 | ℒ ​ ℱ 2 ​ ( σ ​ τ) ≤ ℒ ​ ℱ 2 ​ ( σ) + ℒ ​ ℱ 2 ​ ( τ) \mathcal{LF}_{2}(\sigma\tau)\leq\mathcal{LF}_{2}(\sigma)+\mathcal{LF}_{2}(\tau) |  |

is equivalent to the following ones

 | ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( σ ​ τ)] ≤ ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( σ)] + ∑ j = 1 n [2 n − j − 2 n − j − c j ​ ( τ)] \sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\sigma\tau)}\right]\leq\sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\sigma)}\right]+\sum_{j=1}^{n}\left[2^{n-j}-2^{n-j-c_{j}(\tau)}\right] |  |

 | ∑ j = 1 n 2 n − j − c j ​ ( τ) + ∑ j = 1 n 2 n − j − c j ​ ( σ) ≤ ∑ j = 1 n 2 n − j + ∑ j = 1 n 2 n − j − c j ​ ( σ ​ τ) \sum_{j=1}^{n}2^{n-j-c_{j}(\tau)}+\sum_{j=1}^{n}2^{n-j-c_{j}(\sigma)}\leq\sum_{j=1}^{n}2^{n-j}+\sum_{j=1}^{n}2^{n-j-c_{j}(\sigma\tau)} |  |

 | ∑ j = 1 n 1 2 j + c j ​ ( τ) + ∑ j = 1 n 1 2 j + c j ​ ( σ) ≤ ∑ j = 1 n 1 2 j + ∑ j = 1 n 1 2 j + c j ​ ( σ ​ τ) \sum_{j=1}^{n}\frac{1}{2^{j+c_{j}(\tau)}}+\sum_{j=1}^{n}\frac{1}{2^{j+c_{j}(\sigma)}}\leq\sum_{j=1}^{n}\frac{1}{2^{j}}+\sum_{j=1}^{n}\frac{1}{2^{j+c_{j}(\sigma\tau)}} |  |

 | ∑ j = 1 n 1 2 j + c j ​ ( τ) + ∑ j = 1 n 1 2 τ ​ ( j) + c τ ⁡ ( j) ​ ( σ) ≤ ∑ j = 1 n 1 2 τ ⁡ ( j) + ∑ j = 1 n 1 2 j + c j ​ ( σ ​ τ) \sum_{j=1}^{n}\frac{1}{2^{j+c_{j}(\tau)}}+\sum_{j=1}^{n}\frac{1}{2^{\tau(j)+c_{\tau(j)}(\sigma)}}\leq\sum_{j=1}^{n}\frac{1}{2^{\tau(j)}}+\sum_{j=1}^{n}\frac{1}{2^{j+c_{j}(\sigma\tau)}} |  |

The last inequality holds since for j j taking all values from [n] [n] the same holds for τ ⁡ ( j) \tau(j).

To finish the proof, it is enough to show that for every j = 1, 2, …, n j=1,2,\ldots,n we have

(3.1) |  | 1 2 j + c j ​ ( τ) + 1 2 τ ​ ( j) + c τ ⁡ ( j) ​ ( σ) ≤ 1 2 τ ⁡ ( j) + 1 2 j + c j ​ ( σ ​ τ) \frac{1}{2^{j+c_{j}(\tau)}}+\frac{1}{2^{\tau(j)+c_{\tau(j)}(\sigma)}}\leq\frac{1}{2^{\tau(j)}}+\frac{1}{2^{j+c_{j}(\sigma\tau)}} |  |

By Lemma 3.1 ( i) and ( ii),

(3.2) |  | c j ​ ( σ ​ τ) ≤ c j ​ ( τ) + c τ ⁡ ( j) ​ ( σ) ​ and ​ τ ​ ( j) ≤ j + c j ​ ( τ). c_{j}(\sigma\tau)\leq c_{j}(\tau)+c_{\tau(j)}(\sigma)\textrm{ and }\tau(j)\leq j+c_{j}(\tau). |  |

Since for non negative numbers a a, b b, c c, d d and e e satisfying

 | e ≤ b + d ​ and ​ c ≤ a + b e\leq b+d\textrm{ and }c\leq a+b |  |

it holds

 | 1 2 a + b + 1 2 c + d ≤ 1 2 c + 1 2 a + e \frac{1}{2^{a+b}}+\frac{1}{2^{c+d}}\leq\frac{1}{2^{c}}+\frac{1}{2^{a+e}} |  |

hence ( 3.1) is a consequence of ( 3.2) by substitution

 | a = j ​, ​ b = c j ​ ( τ) ​, ​ c = τ ⁡ ( j) ​, ​ d = c τ ⁡ ( j) ​ ( σ) ​ and ​ e = c j ​ ( σ ​ τ) a=j\textrm{, }b=c_{j}(\tau)\textrm{, }c=\tau(j)\textrm{, }d=c_{\tau(j)}(\sigma)\textrm{ and }e=c_{j}(\sigma\tau) |  |

( vii)

 | ℒ ​ ℱ 2 ​ ( τ) − ℒ ​ ℱ 2 ​ ( σ) = ∑ i = 0 n − 1 [2 i − 2 i − k i ​ ( τ)] − ∑ i = 0 n − 1 [2 i − 2 i − k i ​ ( σ)] = ∑ i = 0 n − 1 [2 i − k i ​ ( σ) − 2 i − k i ​ ( τ)] = \displaystyle\mathcal{LF}_{2}(\tau)-\mathcal{LF}_{2}(\sigma)=\sum_{i=0}^{n-1}\left[2^{i}-2^{i-k_{i}(\tau)}\right]-\sum_{i=0}^{n-1}\left[2^{i}-2^{i-k_{i}(\sigma)}\right]=\sum_{i=0}^{n-1}\left[2^{i-k_{i}(\sigma)}-2^{i-k_{i}(\tau)}\right]= |  |

 | = ∑ i = 0 n − 1 [2 i − c n − i ​ ( σ) − 2 i − c n − i ​ ( τ)] = ∑ j = 1 n [2 n − j − c j ​ ( σ) − 2 n − j − c j ​ ( τ)] \displaystyle=\sum_{i=0}^{n-1}\left[2^{i-c_{n-i}(\sigma)}-2^{i-c_{n-i}(\tau)}\right]=\sum_{j=1}^{n}\left[2^{n-j-c_{j}(\sigma)}-2^{n-j-c_{j}(\tau)}\right] |  |

Now according to Lemma 3.3 ( ii) c j ​ ( τ) = c j ​ ( σ) c_{j}(\tau)=c_{j}(\sigma) for j ≠ s, s + 1 j\neq s,s+1, hence

 | ℒ ​ ℱ 2 ​ ( τ) − ℒ ​ ℱ 2 ​ ( σ) = [2 n − s − c s ​ ( σ) − 2 n − s − c s ​ ( τ)] + [2 n − s − 1 − c s + 1 ​ ( σ) − 2 n − s − 1 − c s + 1 ​ ( τ)] \mathcal{LF}_{2}(\tau)-\mathcal{LF}_{2}(\sigma)=\left[2^{n-s-c_{s}(\sigma)}-2^{n-s-c_{s}(\tau)}\right]+\left[2^{n-s-1-c_{s+1}(\sigma)}-2^{n-s-1-c_{s+1}(\tau)}\right] |  |

If σ ⁡ ( s) < σ ⁡ ( s + 1) \sigma(s)<\sigma(s+1), then by Lemma 3.3 ( ii)

 | c s ​ ( τ) = c s + 1 ​ ( σ) + 1 ​ and ​ c s + 1 ​ ( τ) = c s ​ ( σ) c_{s}(\tau)=c_{s+1}(\sigma)+1\textrm{ and }c_{s+1}(\tau)=c_{s}(\sigma) |  |

Therefore

 | ℒ ​ ℱ 2 ​ ( τ) − ℒ ​ ℱ 2 ​ ( σ) = [2 n − s − c s ​ ( σ) − 2 n − s − c s + 1 ​ ( σ) − 1] + [2 n − s − 1 − c s + 1 ​ ( σ) − 2 n − s − 1 − c s ​ ( σ)] = \displaystyle\mathcal{LF}_{2}(\tau)-\mathcal{LF}_{2}(\sigma)=\left[2^{n-s-c_{s}(\sigma)}-2^{n-s-c_{s+1}(\sigma)-1}\right]+\left[2^{n-s-1-c_{s+1}(\sigma)}-2^{n-s-1-c_{s}(\sigma)}\right]= |  |

 | = 2 n − s − 1 − c s ​ ( σ) = 2 − c s ​ ( σ) ​ ℒ ​ ℱ 2 ​ ( σ s) \displaystyle=2^{n-s-1-c_{s}(\sigma)}=2^{-c_{s}(\sigma)}\mathcal{LF}_{2}(\sigma_{s}) |  |

Otherwise

 | c s ​ ( τ) = c s + 1 ​ ( σ) ​ and ​ c s + 1 ​ ( τ) = c s ​ ( σ) − 1 c_{s}(\tau)=c_{s+1}(\sigma)\textrm{ and }c_{s+1}(\tau)=c_{s}(\sigma)-1 |  |

and therefore

 | ℒ ​ ℱ 2 ​ ( τ) − ℒ ​ ℱ 2 ​ ( σ) = [2 n − s − c s ​ ( σ) − 2 n − s − c s + 1 ​ ( σ)] + [2 n − s − 1 − c s + 1 ​ ( σ) − 2 n − s − 1 − c s ​ ( σ) + 1] = \displaystyle\mathcal{LF}_{2}(\tau)-\mathcal{LF}_{2}(\sigma)=\left[2^{n-s-c_{s}(\sigma)}-2^{n-s-c_{s+1}(\sigma)}\right]+\left[2^{n-s-1-c_{s+1}(\sigma)}-2^{n-s-1-c_{s}(\sigma)+1}\right]= |  |

 | = − 2 n − s − 1 − c s + 1 ​ ( σ) = − 2 − c s + 1 ​ ( σ) ​ ℒ ​ ℱ 2 ​ ( σ s) \displaystyle=-2^{n-s-1-c_{s+1}(\sigma)}=-2^{-c_{s+1}(\sigma)}\mathcal{LF}_{2}(\sigma_{s}) |  |

The last equalities in both cases are due to ( iii).

To finish the proof, it is enough to notice that: if σ ⁡ ( s) < σ ⁡ ( s + 1) \sigma(s)<\sigma(s+1), then c s ​ ( σ) ≤ c s + 1 ​ ( s) c_{s}(\sigma)\leq c_{s+1}(s), otherwise c s + 1 ​ ( σ) < c s ​ ( σ) c_{s+1}(\sigma)<c_{s}(\sigma). ∎

## 4 The distribution of the Lehmer factorial norm

In this section we examine the properties of the probability distribution function of the values of the Lehmer norm.

We start with the following theorem, the proof of which is due to K. Majcher.

###### Theorem 4.1.

The direct limit of the system of groups ( S n, ι n) (S_{n},\iota_{n}) is given by

 | lim → ⁡ ( S n, ι n) ≅ S ∞ \varinjlim{(S_{n},\iota_{n})}\cong S_{\infty} |  |

Proof. Note first, that

 | S ∞ ≅ lim → ⁡ ( S n, j n) S_{\infty}\cong\varinjlim{(S_{n},j_{n})} |  |

where j n: S n → S n + 1 j_{n}:S_{n}\to S_{n+1} is given by

 | j n ​ ( σ ⁡ ( 1), σ ⁡ ( 2), …, σ ⁡ ( n)) = ( σ ⁡ ( 1), σ ⁡ ( 2), …, σ ⁡ ( n), n + 1) j_{n}(\sigma(1),\sigma(2),\ldots,\sigma(n))=(\sigma(1),\sigma(2),\ldots,\sigma(n),n+1) |  |

To see this for σ ∈ S ∞ \sigma\in S_{\infty} let K ⁡ ( σ) K(\sigma) be a minimal natural number such that σ ⁡ ( k) = k \sigma(k)=k for all k ≥ K ⁡ ( σ) k\geq K(\sigma). Define

 | F ⁡ ( σ) = { ( 1) ∈ S 1 ​ if ​ K ​ ( σ) = 1 ( σ ⁡ ( 1), …, σ ⁡ ( K ⁡ ( σ) − 1)) ∈ S K ⁡ ( σ) − 1 ​ if ​ K ​ ( σ) > 2 F(\sigma)=\begin{cases}(1)\in S_{1}\textrm{ if }K(\sigma)=1\\ (\sigma(1),\ldots,\sigma(K(\sigma)-1))\in S_{K(\sigma)-1}\textrm{ if }K(\sigma)>2\end{cases} |  |

(note, that it is impossible to have K ⁡ ( σ) = 2 K(\sigma)=2). F ⁡ ( σ) F(\sigma) determines the unique element

 | G ⁡ ( σ) = ( F ⁡ ( σ), j K ⁡ ( σ) − 1 ​ ( F ⁡ ( σ)), …) ∼ ∈ lim → ⁡ ( S n, j n) G(\sigma)=\left(F(\sigma),j_{K(\sigma)-1}(F(\sigma)),\ldots\right)_{\sim}\in\varinjlim{(S_{n},j_{n})} |  |

It is easy to see that G G is the isomorphism between S ∞ S_{\infty} and lim → ⁡ ( S n, j n) \varinjlim{(S_{n},j_{n})}.

To finish the proof it is enough to note that for t n t_{n} being the conjugacy by e ¯ n \bar{e}_{n} the following diagrams commutes:

 | S n → ι n S n + 1 t n ↓ ↓ t n + 1 S n → j n S n + 1 \begin{CD}S_{n}@>{\iota_{n}}>{}>S_{n+1}\\ @V{t_{n}}V{}V@V{}V{t_{n+1}}V\\ S_{n}@>{}>{j_{n}}>S_{n+1}\end{CD} |  |

∎

Note, that due to Theorems 4.1 and 3.6 ( iv), ℒ ​ ℱ 2 \mathcal{LF}_{2} can be seen as a norm on S ∞ S_{\infty}.

We continue with the following observation concerning the properties of permutations from the image ι n − 1 ​ [S n − 1] \iota_{n-1}[S_{n-1}]. According to the Theorem 3.6 ( ii) and ( iv) we have the following:

###### Remark 4.2.

Let σ ∈ S n \sigma\in S_{n} be a permutation. If c 1 ​ ( σ) = 0 c_{1}(\sigma)=0, then

 | ℒ ​ ℱ 2 ​ ( σ) ≤ 2 n − 1 − n \mathcal{LF}_{2}(\sigma)\leq 2^{n-1}-n |  |

On the other hand, if c 1 ​ ( σ) > 0 c_{1}(\sigma)>0, then

 | ℒ ​ ℱ 2 ​ ( σ) ≥ 2 n − 2 \mathcal{LF}_{2}(\sigma)\geq 2^{n-2} |  |

The following definition will be crucial to dermine the distribution of ℒ ​ ℱ 2 \mathcal{LF}_{2} on S ∞ S_{\infty}.

###### Definition 4.3.

For a natural number m > 0 m>0 and for k = 0, 1, … k=0,1,\ldots let

 | S k ( m) = ⋃ t ≥ 1 { ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ ℕ 2 ​ t: k = m 1 > m 2 > … > m t ≥ 0; \displaystyle S_{k}(m)=\bigcup_{t\geq 1}\Big\{((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\mathbb{N}^{2t}:k=m_{1}>m_{2}>\ldots>m_{t}\geq 0\textrm{; } |  |

 | m j ≥ l j ≥ 0 for j = 1, 2, …, t; m = ∑ j = 1 t [∑ p = 0 l j 2 m j − p] } \displaystyle m_{j}\geq l_{j}\geq 0\textrm{ for }j=1,2,\ldots,t\textrm{; }m=\sum_{j=1}^{t}\left[\sum_{p=0}^{l_{j}}2^{m_{j}-p}\right]\Big\} |  |

and let s k ​ ( m) = | S k ​ ( m) | s_{k}(m)=|S_{k}(m)|.

###### Lemma 4.4.

Let m = ∑ j = 1 s 2 m j m=\sum_{j=1}^{s}2^{m_{j}} for some natural numbers m 1 > m 2 > … > m s ≥ 0 m_{1}>m_{2}>\ldots>m_{s}\geq 0. Then s k ​ ( m) = 0 s_{k}(m)=0 for all k ≠ m 1, m 1 − 1 k\neq m_{1},m_{1}-1.

Proof. Suppose first that k > m 1 k>m_{1}. Therefore

 | m = ∑ j = 1 s 2 m j ≤ ∑ i = 0 m 1 2 i = 2 m 1 + 1 − 1 < 2 k m=\sum_{j=1}^{s}2^{m_{j}}\leq\sum_{i=0}^{m_{1}}2^{i}=2^{m_{1}+1}-1<2^{k} |  |

hence m m cannot be decomposed as a sum given by any element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S k ​ ( m) \left((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t})\right)\in S_{k}(m) |  |

On the other hand, if k < m 1 − 1 k<m_{1}-1, then (for m ¯ 1 = k \bar{m}_{1}=k)

 | ∑ j = 1 t [∑ p = 0 l ¯ j 2 m ¯ j − p] ≤ ∑ i = 0 k [∑ r = 0 i 2 r] = ∑ i = 0 k [2 i + 1 − 1] = 2 k + 2 − ( k + 2) < 2 k + 2 ≤ 2 m 1 ≤ m \sum_{j=1}^{t}\left[\sum_{p=0}^{\bar{l}_{j}}2^{\bar{m}_{j}-p}\right]\leq\sum_{i=0}^{k}\left[\sum_{r=0}^{i}2^{r}\right]=\sum_{i=0}^{k}\left[2^{i+1}-1\right]=2^{k+2}-(k+2)<2^{k+2}\leq 2^{m_{1}}\leq m |  |

and similarily, m m cannot be decomposed as a sum given any element

 | ( ( m ¯ 1, l ¯ 1), ( m ¯ 2, l ¯ 2), …, ( m ¯ t, l ¯ t)) ∈ S k ​ ( m) \left((\bar{m}_{1},\bar{l}_{1}),(\bar{m}_{2},\bar{l}_{2}),\ldots,(\bar{m}_{t},\bar{l}_{t})\right)\in S_{k}(m) |  |

∎

According to Lemma 4.4

 | s ⁡ ( m) = ∑ k = 0 ∞ s k ​ ( m) s(m)=\sum_{k=0}^{\infty}s_{k}(m) |  |

is a well defined natural number. Moreover, the following holds:

###### Theorem 4.5.

Put s ⁡ ( 0) = 1 s(0)=1. Then for every natural number m m we have

 | s ⁡ ( m) = | { σ ∈ S ∞: ℒ ​ ℱ 2 ​ ( σ) = m } | s(m)=\left|\left\{\sigma\in S_{\infty}:\mathcal{LF}_{2}(\sigma)=m\right\}\right| |  |

Proof. The statement is obvious for m = 0 m=0.

Consider σ ∈ S ∞ \sigma\in S_{\infty} different from the identity. Let n n be the minimal natural number such that σ \sigma can be regarded as an element of S n S_{n}. Since σ \sigma is not the identity, it follows that n > 1 n>1. Finally, let m = ℒ ​ ℱ 2 ​ ( σ) m=\mathcal{LF}_{2}(\sigma). Therefore

 | m = ℒ ​ ℱ 2 ​ ( σ) = ∑ i = 0 n − 1 [2 i − 2 i − k i ​ ( σ)] = ∑ i = 0 k i ​ ( σ) ≠ 0 n − 1 [∑ p = 0 k i ​ ( σ) − 1 2 ( i − 1) − p] = ∑ i = 1 k i ​ ( σ) ≠ 0 n − 1 [∑ p = 0 k i ​ ( σ) − 1 2 ( i − 1) − p] m=\mathcal{LF}_{2}(\sigma)=\sum_{i=0}^{n-1}\left[2^{i}-2^{i-k_{i}(\sigma)}\right]=\sum_{\begin{subarray}{c}i=0\\ k_{i}(\sigma)\neq 0\end{subarray}}^{n-1}\left[\sum_{p=0}^{k_{i}(\sigma)-1}2^{(i-1)-p}\right]=\sum_{\begin{subarray}{c}i=1\\ k_{i}(\sigma)\neq 0\end{subarray}}^{n-1}\left[\sum_{p=0}^{k_{i}(\sigma)-1}2^{(i-1)-p}\right] |  |

Since n n is minimal, it follows that k n − 1 ​ ( σ) = c 1 ​ ( σ) > 0 k_{n-1}(\sigma)=c_{1}(\sigma)>0.

Let i 1 > i 2 > … > i t i_{1}>i_{2}>\ldots>i_{t} be all elements of [n − 1] [n-1] such that k i j ​ ( σ) ≠ 0 k_{i_{j}}(\sigma)\neq 0 for j = 1, 2, …, t j=1,2,\ldots,t (of course t ≥ 1 t\geq 1) and let m j = i j − 1 m_{j}=i_{j}-1. Thus we have

 | n − 2 = m 1 > m 2 > … > m t ≥ 0 n-2=m_{1}>m_{2}>\ldots>m_{t}\geq 0 |  |

Put l j = k i j ​ ( σ) − 1 l_{j}=k_{i_{j}}(\sigma)-1 and note, that l j ≤ m j l_{j}\leq m_{j}.

Since

 | m = ∑ i = 1 k i ​ ( σ) ≠ 0 n − 1 [∑ p = 0 k i ​ ( σ) − 1 2 ( i − 1) − p] = ∑ j = 1 t [∑ p = 0 l j 2 m j − p] m=\sum_{\begin{subarray}{c}i=1\\ k_{i}(\sigma)\neq 0\end{subarray}}^{n-1}\left[\sum_{p=0}^{k_{i}(\sigma)-1}2^{(i-1)-p}\right]=\sum_{j=1}^{t}\left[\sum_{p=0}^{l_{j}}2^{m_{j}-p}\right] |  |

this decompostition of ℒ ​ ℱ 2 ​ ( σ) = m \mathcal{LF}_{2}(\sigma)=m determines the element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S n − 2 ​ ( m) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{n-2}(m) |  |

On the other hand, for an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S n ​ ( m) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{n}(m) |  |

let σ ∈ S n + 2 \sigma\in S_{n+2} be given by its Lehmer code in the following way:

 | lc ⁡ ( σ) = [c 1 ​ ( σ), c 2 ​ ( σ), …, c n + 2 ​ ( σ)] = [k n + 1 ​ ( σ), k n ​ ( σ), …, k 0 ​ ( σ)] \lehmer(\sigma)=[c_{1}(\sigma),c_{2}(\sigma),\ldots,c_{n+2}(\sigma)]=[k_{n+1}(\sigma),k_{n}(\sigma),\ldots,k_{0}(\sigma)] |  |

where

- •

k m j + 1 ​ ( σ) = l j + 1 k_{m_{j}+1}(\sigma)=l_{j}+1 for j = 1, 2, …, t j=1,2,\ldots,t,

- •

k i ​ ( σ) = 0 k_{i}(\sigma)=0 for i ∈ { 0, 1, …, m + 1 } ∖ { m 1 + 1, m 2 + 1, …, m t + 1 } i\in\{0,1,\ldots,m+1\}\setminus\{m_{1}+1,m_{2}+1,\ldots,m_{t}+1\}

For σ \sigma defined in such a way it holds

 | ℒ ​ ℱ 2 ​ ( σ) = ∑ i = 0 n + 1 [2 i − 2 i − k i ​ ( σ)] = ∑ i = 0 k i ​ ( σ) ≠ 0 n + 1 [∑ p = 0 k i ​ ( σ) − 1 2 ( i − 1) − p] = \displaystyle\mathcal{LF}_{2}(\sigma)=\sum_{i=0}^{n+1}\left[2^{i}-2^{i-k_{i}(\sigma)}\right]=\sum_{\begin{subarray}{c}i=0\\ k_{i}(\sigma)\neq 0\end{subarray}}^{n+1}\left[\sum_{p=0}^{k_{i}(\sigma)-1}2^{(i-1)-p}\right]= |  |

 | = ∑ j = 1 t [∑ p = 0 k m j + 1 ​ ( σ) − 1 2 [( m j + 1) − 1] − p] = ∑ j = 1 t [∑ p = 0 l j 2 m j − p] = m \displaystyle=\sum_{j=1}^{t}\left[\sum_{p=0}^{k_{m_{j}+1}(\sigma)-1}2^{[(m_{j}+1)-1]-p}\right]=\sum_{j=1}^{t}\left[\sum_{p=0}^{l_{j}}2^{m_{j}-p}\right]=m |  |

Moreover, the assigments

 | σ → ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ​ and ​ ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) → σ \sigma\rightarrow((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\textrm{ and }((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\rightarrow\sigma |  |

are mutually inverse.

This finishes the proof. ∎

In the next theorem we present the recursive properties of numbers s k ​ ( m) s_{k}(m). Note, that Theorems 4.5 and 4.6 together with Lemma 4.4 fully describe the distribution of ℒ ​ ℱ 2 \mathcal{LF}_{2} on S ∞ S_{\infty}. The values of s k ​ ( m) s_{k}(m) for m = 1, 2, …, 8 m=1,2,\ldots,8, together with the corresponding permutations can be found in Table 2. The graphs of functions s ⁡ ( m) s(m) and d ⁡ ( m) = ∑ l = 1 m s ⁡ ( l) d(m)=\sum_{l=1}^{m}s(l) for m = 1, 2, …, 256 m=1,2,\ldots,256 are presented in Figure 1.

###### Theorem 4.6.

The following holds:

1. (i)

s ⁡ ( 0) = 1 s(0)=1;

2. (ii)

s 0 ​ ( 1) = 1 s_{0}(1)=1 and s k ​ ( 1) = 0 s_{k}(1)=0 for k > 0 k>0;

3. (iii)

s 0 ​ ( 2) = 0 s_{0}(2)=0, s 1 ​ ( 2) = 1 s_{1}(2)=1 and s k ​ ( 2) = 0 s_{k}(2)=0 for k > 1 k>1;

4. (iv)

s m ​ ( 2 m) = 1 s_{m}\left(2^{m}\right)=1,

 | s m − 1 ​ ( 2 m) = ∑ j = 0 m − 1 [∑ k = 0 m − 2 s k ​ ( 2 m − ( 2 m − 1 + … + 2 j))] s_{m-1}\left(2^{m}\right)=\sum_{j=0}^{m-1}\left[\sum_{k=0}^{m-2}s_{k}\left(2^{m}-\left(2^{m-1}+\ldots+2^{j}\right)\right)\right] |  |

and s k ​ ( 2 m) = 0 s_{k}\left(2^{m}\right)=0 for k ≠ m, m − 1 k\neq m,m-1;

5. (v)

For l = 0, 1, …, m − 1 l=0,1,\ldots,m-1

 | s m ​ ( 2 m + … + 2 l) = 1 + ∑ j = l m − 1 [∑ k = 0 m − 1 s k ​ ( 2 j + … + 2 l)], s_{m}\left(2^{m}+\ldots+2^{l}\right)=1+\sum_{j=l}^{m-1}\left[\sum_{k=0}^{m-1}s_{k}\left(2^{j}+\ldots+2^{l}\right)\right], |  |

 | s m − 1 ​ ( 2 m + … + 2 l) = ∑ j = 0 m − 1 [∑ k = 0 m − 2 s k ​ ( ( 2 m + … + 2 l) − ( 2 m − 1 + … + 2 j))] s_{m-1}\left(2^{m}+\ldots+2^{l}\right)=\sum_{j=0}^{m-1}\left[\sum_{k=0}^{m-2}s_{k}\left(\left(2^{m}+\ldots+2^{l}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right)\right] |  |

and s k ​ ( 2 m + … + 2 l) = 0 s_{k}\left(2^{m}+\ldots+2^{l}\right)=0 for k ≠ m, m − 1 k\neq m,m-1;

6. (vi)

For l = 2, 3, …, m − 1 l=2,3,\ldots,m-1 and for a 0, a 1, …, a l − 2 ∈ { 0, 1 } a_{0},a_{1},\ldots,a_{l-2}\in\{0,1\} not all being equal to 0 0

 | s m ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) = \displaystyle s_{m}\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)= |  |

 | ∑ k = 0 m − 1 [s k ​ ( a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0)] + ∑ j = l m − 1 [∑ k = 0 m − 1 s k ​ ( 2 j + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0)], \displaystyle\sum_{k=0}^{m-1}\left[s_{k}\left(a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)\right]+\sum_{j=l}^{m-1}\left[\sum_{k=0}^{m-1}s_{k}\left(2^{j}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)\right], |  |

 | s m − 1 ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) = \displaystyle s_{m-1}\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)= |  |

 | = ∑ j = 0 m − 1 [∑ k = 0 m − 2 s k ​ ( ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) − ( 2 m − 1 + … + 2 j))] \displaystyle=\sum_{j=0}^{m-1}\left[\sum_{k=0}^{m-2}s_{k}\left(\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right)\right] |  |

and s k ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) = 0 s_{k}\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)=0 for k ≠ m, m − 1 k\neq m,m-1;

7. (vii)

For m > 1 m>1 and for a 0, a 1, …, a m − 2 ∈ { 0, 1 } a_{0},a_{1},\ldots,a_{m-2}\in\{0,1\} not all being equal to 0 0

 | s m ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) = ∑ k = 0 m − 1 [s k ​ ( a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0)], s_{m}\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)=\sum_{k=0}^{m-1}\left[s_{k}\left(a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)\right], |  |

 | s m − 1 ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) = \displaystyle s_{m-1}\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)= |  |

 | = ∑ j = 0 m − 1 [∑ k = 0 m − 2 s k ​ ( ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) − ( 2 m − 1 + … + 2 j))] \displaystyle=\sum_{j=0}^{m-1}\left[\sum_{k=0}^{m-2}s_{k}\left(\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right)\right] |  |

and s k ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) = 0 s_{k}\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)=0 for k ≠ m, m − 1 k\neq m,m-1.

Proof. ( i) follows the definition of s s.

( ii) and ( iii) follows the equations S 0 ​ ( 1) = { ( 0, 0) } S_{0}(1)=\{(0,0)\} and S 1 ​ ( 2) = { ( 1, 0) } S_{1}(2)=\{(1,0)\} respectively, as well as Lemma 4.4.

( iv) There are three cases to consider when determining S k ​ ( 2 m) S_{k}(2^{m}), namely k = m k=m, k = m − 1 k=m-1 and k ≠ m, m − 1 k\neq m,m-1.

1. (a)

S m ​ ( 2 m) = { ( m, 0) } S_{m}(2^{m})=\{(m,0)\}, hence s m ​ ( 2 m) = 1 s_{m}(2^{m})=1.

2. (b)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}) |  |

Therefore m 1 = m − 1 m_{1}=m-1. Putting j = m − 1 − l 1 j=m-1-l_{1} we get m − 1 ≥ j ≥ 0 m-1\geq j\geq 0. And since

 | 2 m > ∑ i = j m − 1 2 i = ∑ p = 0 l 1 2 ( m − 1) − p = ∑ p = 0 l 1 2 m 1 − p 2^{m}>\sum_{i=j}^{m-1}2^{i}=\sum_{p=0}^{l_{1}}2^{(m-1)-p}=\sum_{p=0}^{l_{1}}2^{m_{1}-p} |  |

one must have t > 1 t>1. Therefore (note that m 2 ≤ m − 2 m_{2}\leq m-2)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 2 ​ S k ​ ( 2 m − ( ∑ p = 0 l 1 2 m 1 − p)) = \bigcupdot k = 0 m − 2 ​ S k ​ ( 2 m − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-2}S_{k}\left(2^{m}-\left(\sum_{p=0}^{l_{1}}2^{m_{1}-p}\right)\right)=\bigcupdot_{k=0}^{m-2}S_{k}\left(2^{m}-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

Conversely, for every j = 0, 1, …, m − 1 j=0,1,\ldots,m-1 an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 2 ​ S k ​ ( 2 m − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-2}S_{k}\left(2^{m}-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

determines

 | ( ( m − 1, m − 1 − j), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m) ((m-1,m-1-j),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}) |  |

3. (c)

The equality s k ​ ( 2 m) = 0 s_{k}\left(2^{m}\right)=0 for k ≠ m, m − 1 k\neq m,m-1 follows Lemma 4.4.

( v) There are three cases to consider when determining S k ​ ( 2 m + … + 2 l) S_{k}(2^{m}+\ldots+2^{l}), namely k = m k=m, k = m − 1 k=m-1 and k ≠ m, m − 1 k\neq m,m-1.

1. (a)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + … + 2 l) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}(2^{m}+\ldots+2^{l}) |  |

If t = 1 t=1, then ( m 1, l 1) = ( m, m − l) (m_{1},l_{1})=(m,m-l).

Otherwise l 1 < m − l l_{1}<m-l. To see this note that for l 1 ≥ m − l l_{1}\geq m-l we have

 | [2 m + … + 2 m − l 1] + [2 m 2 + … + 2 m 2 − l 2] ≥ [2 m + … + 2 l] + [2 m 2] > 2 m + … + 2 l [2^{m}+\ldots+2^{m-l_{1}}]+[2^{m_{2}}+\ldots+2^{m_{2}-l_{2}}]\geq[2^{m}+\ldots+2^{l}]+[2^{m_{2}}]>2^{m}+\ldots+2^{l} |  |

hence

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∉ S m ​ ( 2 m + … + 2 l) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\notin S_{m}(2^{m}+\ldots+2^{l}) |  |

Let j = m − 1 − l 1 j=m-1-l_{1} (in particular m − 1 ≥ j > l − 1 m-1\geq j>l-1). Now

 | 2 m + … + 2 l > ∑ i = j + 1 m 2 i = ∑ p = 0 l 1 2 m − p = ∑ p = 0 l 1 2 m 1 − p 2^{m}+\ldots+2^{l}>\sum_{i=j+1}^{m}2^{i}=\sum_{p=0}^{l_{1}}2^{m-p}=\sum_{p=0}^{l_{1}}2^{m_{1}-p} |  |

and therefore (since m 2 ≤ m − 1 m_{2}\leq m-1)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( ( 2 m + … + 2 l) − ∑ p = 0 l 1 2 m 1 − p) = \bigcupdot k = 0 m − 1 ​ S k ​ ( 2 j + … + 2 l) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}\left(\left(2^{m}+\ldots+2^{l}\right)-\sum_{p=0}^{l_{1}}2^{m_{1}-p}\right)=\bigcupdot_{k=0}^{m-1}S_{k}\left(2^{j}+\ldots+2^{l}\right) |  |

Conversely, for every j = l, …, m − 1 j=l,\ldots,m-1 an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( 2 j + … + 2 l) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}\left(2^{j}+\ldots+2^{l}\right) |  |

defines

 | ( ( m, m − 1 − j), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + … + 2 l) ((m,m-1-j),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}\left(2^{m}+\ldots+2^{l}\right) |  |

Together with ( m, m − l) (m,m-l) these are all elements of S m ​ ( 2 m + … + 2 l) S_{m}\left(2^{m}+\ldots+2^{l}\right).

2. (b)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m + … + 2 l) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}+\ldots+2^{l}) |  |

Therefore m 1 = m − 1 m_{1}=m-1. Putting j = m − 1 − l 1 j=m-1-l_{1} we get m − 1 ≥ j ≥ 0 m-1\geq j\geq 0. Since

 | 2 m + … + 2 l > ∑ i = j m − 1 2 i = ∑ p = 0 l 1 2 ( m − 1) − p = ∑ p = 0 l 1 2 m 1 − p 2^{m}+\ldots+2^{l}>\sum_{i=j}^{m-1}2^{i}=\sum_{p=0}^{l_{1}}2^{(m-1)-p}=\sum_{p=0}^{l_{1}}2^{m_{1}-p} |  |

it follows that t > 1 t>1. Therefore (note that m 2 ≤ m − 2 m_{2}\leq m-2)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 2 ​ S k ​ ( ( 2 m + … + 2 l) − ( ∑ p = 0 l 1 2 m 1 − p)) = \displaystyle((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-2}S_{k}\left(\left(2^{m}+\ldots+2^{l}\right)-\left(\sum_{p=0}^{l_{1}}2^{m_{1}-p}\right)\right)= |  |

 | = \bigcupdot k = 0 m − 2 ​ S k ​ ( ( 2 m + … + 2 l) − ( 2 m − 1 + … + 2 j)) \displaystyle=\bigcupdot_{k=0}^{m-2}S_{k}\left(\left(2^{m}+\ldots+2^{l}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

Conversely, for every j = 0, 1, …, m − 1 j=0,1,\ldots,m-1, an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 2 ​ S k ​ ( ( 2 m + … + 2 l) − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-2}S_{k}\left(\left(2^{m}+\ldots+2^{l}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

determines

 | ( ( m − 1, m − 1 − j), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m + … + 2 l) ((m-1,m-1-j),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}\left(2^{m}+\ldots+2^{l}\right) |  |

3. (c)

The equality s k ​ ( 2 m + … + 2 l) = 0 s_{k}\left(2^{m}+\ldots+2^{l}\right)=0 for k ≠ m, m − 1 k\neq m,m-1 follows Lemma 4.4.

( vi) There are three cases to consider when determining S k ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) S_{k}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}), namely k = m k=m, k = m − 1 k=m-1 and k ≠ m, m − 1 k\neq m,m-1.

1. (a)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

For l 1 > m − l l_{1}>m-l we have

 | 2 m + … + 2 m − l 1 ≥ 2 m + … + 2 l + 2 l − 1 > 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 2 2^{m}+\ldots+2^{m-l_{1}}\geq 2^{m}+\ldots+2^{l}+2^{l-1}>2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{2} |  |

and therefore

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∉ S m ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\notin S_{m}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

hence l 1 ≤ m − l l_{1}\leq m-l. And since

 | ∑ p = 0 l 1 2 m 1 − p ≤ ∑ p = 0 m − l 2 m 1 − p = ∑ p = 0 m − l 2 m − p < 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0 \sum_{p=0}^{l_{1}}2^{m_{1}-p}\leq\sum_{p=0}^{m-l}2^{m_{1}-p}=\sum_{p=0}^{m-l}2^{m-p}<2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0} |  |

it follows that t > 1 t>1.

If l 1 = m − l l_{1}=m-l, then

 | ∑ p = 0 l 1 2 m 1 − p = 2 m + … + 2 l \sum_{p=0}^{l_{1}}2^{m_{1}-p}=2^{m}+\ldots+2^{l} |  |

and therefore (since m 2 ≤ m − 1 m_{2}\leq m-1)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}\left(a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right) |  |

If l 1 < m − l l_{1}<m-l, putting j = m − 1 − l 1 j=m-1-l_{1} we get l ≤ j ≤ m − 1 l\leq j\leq m-1. In this case

 | ∑ p = 0 l 1 2 m 1 − p = ∑ p = 0 m − 1 − j 2 m − p = 2 m + … + 2 j + 1 \sum_{p=0}^{l_{1}}2^{m_{1}-p}=\sum_{p=0}^{m-1-j}2^{m-p}=2^{m}+\ldots+2^{j+1} |  |

thus (since m 2 ≤ m − 1 m_{2}\leq m-1)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( 2 j + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}\left(2^{j}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right) |  |

Conversely, an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}\left(a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right) |  |

determines

 | ( ( m, m − l), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m,m-l),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

and, for j = l, …, m − 1 j=l,\ldots,m-1, an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( 2 j + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}\left(2^{j}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right) |  |

determines

 | ( ( m, m − 1 − j), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m,m-1-j),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

2. (b)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

Since m 1 = m − 1 m_{1}=m-1, we get l 1 ≤ m − 1 l_{1}\leq m-1. Therefore

 | ∑ p = 0 l 1 2 m 1 − p ≤ ∑ p = 0 m − 1 2 m − 1 − p < 2 m < 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0 \sum_{p=0}^{l_{1}}2^{m_{1}-p}\leq\sum_{p=0}^{m-1}2^{m-1-p}<2^{m}<2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0} |  |

and hence t > 1 t>1. Putting j = m 1 − l 1 j=m_{1}-l_{1} we get 0 ≤ j ≤ m − 1 0\leq j\leq m-1. Now

 | ∑ p = 0 l 1 2 m 1 − p = ∑ p = 0 m − 1 − j 2 m − 1 − p = 2 m − 1 + … + 2 j \sum_{p=0}^{l_{1}}2^{m_{1}-p}=\sum_{p=0}^{m-1-j}2^{m-1-p}=2^{m-1}+\ldots+2^{j} |  |

and therefore (since m 2 ≤ m − 2 m_{2}\leq m-2)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 1 m − 2 ​ S k ​ ( ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=1}^{m-2}S_{k}\left(\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

Conversely, for every j = 0, 1, …, k − 1 j=0,1,\ldots,k-1 an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 2 ​ S k ​ ( ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-2}S_{k}\left(\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

determines

 | ( ( m − 1, m − 1 − j), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m-1,m-1-j),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

3. (c)

The equality s k ​ ( 2 m + … + 2 l + a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) = 0 s_{k}\left(2^{m}+\ldots+2^{l}+a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}\right)=0 for k ≠ m, m − 1 k\neq m,m-1 follows Lemma 4.4.

( vii) There are three cases to consider when determining S k ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) S_{k}(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}), namely k = m k=m, k = m − 1 k=m-1 and k ≠ m, m − 1 k\neq m,m-1.

1. (a)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}) |  |

For l 1 > 0 l_{1}>0 we have

 | ∑ p = 0 l 1 2 m 1 − p ≥ 2 m + 2 m − 1 > 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0 \sum_{p=0}^{l_{1}}2^{m_{1}-p}\geq 2^{m}+2^{m-1}>2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0} |  |

and therefore

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∉ S m ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\notin S_{m}(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}) |  |

hence l 1 = 0 l_{1}=0 and t > 1 t>1. Therefore (since m 2 < m m_{2}<m)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( a l − 2 ​ 2 l − 2 + … + a 0 ​ 2 0) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}(a_{l-2}2^{l-2}+\ldots+a_{0}2^{0}) |  |

Conversely, an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 1 ​ S k ​ ( a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-1}S_{k}(a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}) |  |

determines

 | ( ( m, 0), ( m 2, l 2), …, ( m t, l t)) ∈ S m ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) ((m,0),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m}(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}) |  |

2. (b)

Consider first an element

 | ( ( m 1, l 1), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) ((m_{1},l_{1}),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}) |  |

Since m 1 = m − 1 m_{1}=m-1, we get l 1 ≤ m − 1 l_{1}\leq m-1. Therefore

 | ∑ p = 0 l 1 2 m 1 − p ≤ ∑ p = 0 m − 1 2 m − 1 − p < 2 m < 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0 \sum_{p=0}^{l_{1}}2^{m_{1}-p}\leq\sum_{p=0}^{m-1}2^{m-1-p}<2^{m}<2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0} |  |

and hence t > 1 t>1. Putting j = m 1 − l 1 j=m_{1}-l_{1} we get 0 ≤ j ≤ m − 1 0\leq j\leq m-1. Now

 | ∑ p = 0 l 1 2 m 1 − p = ∑ p = 0 m − 1 − j 2 m − 1 − p = 2 m − 1 + … + 2 j \sum_{p=0}^{l_{1}}2^{m_{1}-p}=\sum_{p=0}^{m-1-j}2^{m-1-p}=2^{m-1}+\ldots+2^{j} |  |

and therefore (since m 2 ≤ m − 2 m_{2}\leq m-2)

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 1 m − 2 ​ S k ​ ( ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=1}^{m-2}S_{k}\left(\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

Conversely, for every j = 0, 1, …, k − 1 j=0,1,\ldots,k-1, an element

 | ( ( m 2, l 2), …, ( m t, l t)) ∈ \bigcupdot k = 0 m − 2 ​ S k ​ ( ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) − ( 2 m − 1 + … + 2 j)) ((m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in\bigcupdot_{k=0}^{m-2}S_{k}\left(\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)-\left(2^{m-1}+\ldots+2^{j}\right)\right) |  |

determines

 | ( ( m − 1, m − 1 − j), ( m 2, l 2), …, ( m t, l t)) ∈ S m − 1 ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) ((m-1,m-1-j),(m_{2},l_{2}),\ldots,(m_{t},l_{t}))\in S_{m-1}(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}) |  |

3. (c)

The equality s k ​ ( 2 m + a m − 2 ​ 2 m − 2 + … + a 0 ​ 2 0) = 0 s_{k}\left(2^{m}+a_{m-2}2^{m-2}+\ldots+a_{0}2^{0}\right)=0 for k ≠ m, m − 1 k\neq m,m-1 follows Lemma 4.4.

This finishes the proof. ∎

### Acknowledgements

The author is grateful to K. Majcher for the proof of Theorem 4.1, to P. Józiak for the improvement of the proof of Theorem 3.6 ( vi) as well as for carefully reading of this paper, and to J. Gismatullin for inspiring converations.

Last, but not least, the author wants to thank his whife for her strong and loving support as well as for her inspiring *”try to think nonstandard”*.

All calculations were performed with R 4.0.3 ( [RPackage]).

During the work on this paper the author was partially supported by the SGH fund KAE/S21 and by the NCN fund UMO-2018/31/B/HS4/01005.

## References

- [1]
- [C] P.J. Cameron, *Metric and Topological Aspects of the Symmetric Group of Countable Degree*, Europ. J. Combinatorics 17, pp. 135 – 142 (1996).
- [CSZ] R. J. Clarke, E. Steingrímsson and J. Zeng, *New Euler-Mahonian statistics on permutations and words*, Adv. in Appl. Math. 18, 237–270, (1997).
- [DH] M. Deza and T. Huang, *Metrics on Permutations, a Survey*, J. Combin. Inform. System Sci. 23, pp. 173-185, (1998).
- [DG] P. Diaconis and R. L. Graham, *Spearman’s footrule as a measure of disarray*, J. Royal. Stat. Soc. Ser. B 39, pp. 262-268, (1977).
- [FSS] S. Fischer, A. Schumann and A. Schnurr, *Ordinal pattern dependence between hydrological time series*. J. Hydrol. 548, pp. 536–551, (2017).
- [FZ] D. Foata and D. Zeilberger, *Denert’s permutation statistic is indeed Euler-Mahonian*, Studies in Appl. Math. 83, pp. 31-59, (1990).
- [GMZ] J. Gismatullin, K. Majcher and M.Ziegler, *New compactness theorem for metric ultraproducts and simplicity*, 7 October 2020, arxiv:2010.03394v1.
- [G] D. Grinberg, *Notes on the combinatorial fundamentals of algebra*; 10 January 2019, arXiv:2008.09862v1.
- [KW] K. Keller and K. Wittfeld, *Distances of time series components by means of symbolic dynamics*, Internat. J. Bifur. Chaos 14, pp. 693–703, (2004).
- [K] M. Kendall, *A new measure of rank correlation*, Biometrika 30 (1–2), pp. 81–89, (1938).
- [KV] R. Kumar and S. Vassilvitskii, *Generalized distances between rankings*, in: Proc. 19th Int. Conf. World Wide Web (M. Rappa, P. Jones, J. Freire and S. Chakrabarti Eds.), ACM, New York, pp. 571–580, (2010).
- [LY1] P.H. Lee and P.L.H. Yu, *Distance-based tree models for ranking data*, Comput. Statist. Data Anal. 54 (6), pp. 1672–1682, (2010).
- [LY2] P.H. Lee and P.L.H. Yu, *Mixtures of weighted distance-based models for ranking data with applications in political studies*, Comput. Statist. Data Anal. 56 (8), pp. 2486–2500, (2012).
- [L1] D.E. Lehmer, *Teaching combinatorial tricks to a computer*, in: Combinatorial Analysis: Proceedings of Symposia in Applied Mathematics Volume X (R. Bellman and M. Hall Jr Eds.), Amer. Math. Soc., Providence, pp. 179-193, (1960).
- [L2] D.E. Lehmer, *The machine tools of combinatorics*, in: Applied Combinatorial Mathematics (E.F. Beckenbach Ed.), Wiley, New York, pp. 5–31, (1964).
- [LH] C. Liu and J. Han *Failure proximity: a fault localization-based approach*, inn: Proceedings of the 14th ACM SIGSOFT international symposium on Foundations of software engineering, Association for Computing Machinery, New York, pp. 46–56, (2006).
- [LZH] C. Liu, X. Zhang and J. Han, *A systematic study of failure proximity*, IEEE Trans. on Softw. Eng. 34 (6), pp. 826–843, (2008).
- [M] P.A. MacMahon, *The indices of permutations and the derivation therefrom of functions of a singlevariable associated with the permutations of any assemblage of objects*, Amer. J. Math. 35, 281–322 (1913).
- [PP] A.B. Piek and E. Petrov, *On a Weighted Generalization of Kendall’s Tau Distance*, Ann. Comb. 25, pp. 33–50, (2021).
- [QDRL] G. Ouyang, C. Dang, D.A. Richards and X. Li, *Ordinal pattern based similarity analysis for eeg recordings*, Clin. Neurophysiol. 121 (5), pp. 694–703, (2010).
- [RPackage] R Core Team, *R: A language and environment for statistical computing*; Home page: http://www.R-project.org/
- [R] O. Rodriguez, *Note sur les inversions, ou dérangements produits dans les permutations*, J. de Math. 4, pp. 236–240 (1839).
- [SS] R. Simion and D. Stanton, *Octabasic Laguerre polynomials and permutation statistics*, J. Comput. Appl. Math. 68, 297–329 (1996).
- [S] C. Spearman, *The proof and measurement of association between two things*, Amer. J. of Psych. 15 (1), pp. 72–101, (1904).
- [TW] A. Thom and J. S. Wilson, *Metric ultraproducts of finite simple groups*, C. R. Math. Acad. Sci. Paris 352, pp. 463–466, (2014).
- [WSSC] L. Wang, P. Shang, W. Shi and X. Cui, *Dissimilarity measure based on ordinal pattern for physiological signals*Commun. Nonlinear Sci. Numer. Simul. 37, pp. 115–124, (2016).
- [W] J.S. Wilson, *Metric ultraproducts of classical groups*, Arch. Math. 109, pp. 407–412, (2017).

Table 1: The Lehmer factorial norm on S 3 S_{3}

n lex ⁡ ( σ) \numbering_{\lex}(\sigma) | σ \sigma | lc ⁡ ( σ) \lehmer(\sigma) | ℒ ​ ℱ 2 ​ ( σ) \mathcal{LF}_{2}(\sigma) | n lex ⁡ ( σ) \numbering_{\lex}(\sigma) in the factorial number system representation |

0 0 | ( 1, 2, 3) (1,2,3) | [0, 0, 0] [0,0,0] | 0 0 | 0 = 0 ⋅ 2! + 0 ⋅ 1! + 0 ⋅ 0! 0=0\cdot 2!+0\cdot 1!+0\cdot 0! |

1 1 | ( 1, 3, 2) (1,3,2) | [0, 1, 0] [0,1,0] | 1 1 | 1 = 0 ⋅ 2! + 1 ⋅ 1! + 0 ⋅ 0! 1=0\cdot 2!+1\cdot 1!+0\cdot 0! |

2 2 | ( 2, 1, 3) (2,1,3) | [1, 0, 0] [1,0,0] | 2 2 | 2 = 1 ⋅ 2! + 0 ⋅ 1! + 0 ⋅ 0! 2=1\cdot 2!+0\cdot 1!+0\cdot 0! |

3 3 | ( 2, 3, 1) (2,3,1) | [1, 1, 0] [1,1,0] | 3 3 | 3 = 1 ⋅ 2! + 1 ⋅ 1! + 0 ⋅ 0! 3=1\cdot 2!+1\cdot 1!+0\cdot 0! |

4 4 | ( 3, 1, 2) (3,1,2) | [2, 0, 0] [2,0,0] | 3 3 | 4 = 2 ⋅ 2! + 0 ⋅ 1! + 0 ⋅ 0! 4=2\cdot 2!+0\cdot 1!+0\cdot 0! |

5 5 | ( 3, 2, 1) (3,2,1) | [2, 1, 0] [2,1,0] | 4 4 | 5 = 2 ⋅ 2! + 1 ⋅ 1! + 0 ⋅ 0! 5=2\cdot 2!+1\cdot 1!+0\cdot 0! |

Table 2: The elements of S k ​ ( m) S_{k}(m)

m m | decomposition of m m | lc ⁡ ( σ) \lehmer(\sigma) | ( ( m 1, l 1), …, ( m t, l t)) ((m_{1},l_{1}),\ldots,(m_{t},l_{t})) | element of |

1 1 | 1 = [2 0] 1=[2^{0}] | [1, 0] [1,0] | ( 0, 0) (0,0) | S 0 ​ ( 1) S_{0}(1) |

2 2 | 2 = [2 1] 2=[2^{1}] | [1, 0, 0] [1,0,0] | ( 1, 0) (1,0) | S 1 ​ ( 2) S_{1}(2) |

3 3 | 3 = [2 1] + [2 0] 3=[2^{1}]+[2^{0}] | [1, 1, 0] [1,1,0] | ( ( 1, 0), ( 0, 0)) ((1,0),(0,0)) | S 1 ​ ( 3) S_{1}(3) |

3 3 | 3 = [2 1 + 2 0] 3=[2^{1}+2^{0}] | [2, 0, 0] [2,0,0] | ( 1, 1) (1,1) | S 1 ​ ( 3) S_{1}(3) |

4 4 | 4 = [2 1 + 2 0] + [2 0] 4=[2^{1}+2^{0}]+[2^{0}] | [2, 1, 0] [2,1,0] | ( ( 1, 1), ( 0, 0)) ((1,1),(0,0)) | S 1 ​ ( 4) S_{1}(4) |

4 4 | 4 = [2 2] 4=[2^{2}] | [1, 0, 0, 0] [1,0,0,0] | ( 2, 0) (2,0) | S 2 ​ ( 4) S_{2}(4) |

5 5 | 5 = [2 2] + [2 0] 5=[2^{2}]+[2^{0}] | [1, 0, 1, 0] [1,0,1,0] | ( ( 2, 0), ( 0, 0)) ((2,0),(0,0)) | S 2 ​ ( 5) S_{2}(5) |

6 6 | 6 = [2 2] + [2 1] 6=[2^{2}]+[2^{1}] | [1, 1, 0, 0] [1,1,0,0] | ( ( 2, 0), ( 1, 0)) ((2,0),(1,0)) | S 2 ​ ( 6) S_{2}(6) |

6 6 | 6 = [2 2 + 2 1] 6=[2^{2}+2^{1}] | [2, 0, 0, 0] [2,0,0,0] | ( 2, 1) (2,1) | S 2 ​ ( 6) S_{2}(6) |

7 7 | 7 = [2 2] + [2 1] + [2 0] 7=[2^{2}]+[2^{1}]+[2^{0}] | [1, 1, 1, 0] [1,1,1,0] | ( ( 2, 0), ( 1, 0), ( 0, 0)) ((2,0),(1,0),(0,0)) | S 2 ​ ( 7) S_{2}(7) |

7 7 | 7 = [2 2] + [2 1 + 2 0] 7=[2^{2}]+[2^{1}+2^{0}] | [1, 2, 0, 0] [1,2,0,0] | ( ( 2, 0), ( 1, 1)) ((2,0),(1,1)) | S 2 ​ ( 7) S_{2}(7) |

7 7 | 7 = [2 2 + 2 1] + [2 0] 7=[2^{2}+2^{1}]+[2^{0}] | [2, 0, 1, 0] [2,0,1,0] | ( ( 2, 1), ( 0, 0)) ((2,1),(0,0)) | S 2 ​ ( 7) S_{2}(7) |

7 7 | 7 = [2 2 + 2 1 + 2 0] 7=[2^{2}+2^{1}+2^{0}] | [3, 0, 0, 0] [3,0,0,0] | ( 2, 2) (2,2) | S 2 ​ ( 7) S_{2}(7) |

8 8 | 8 = [2 2] + [2 1 + 2 0] + [2 0] 8=[2^{2}]+[2^{1}+2^{0}]+[2^{0}] | [1, 2, 1, 0] [1,2,1,0] | ( ( 2, 0), ( 1, 1), ( 0, 0)) ((2,0),(1,1),(0,0)) | S 2 ​ ( 8) S_{2}(8) |

8 8 | 8 = [2 2 + 2 1] + [2 1] 8=[2^{2}+2^{1}]+[2^{1}] | [2, 1, 0, 0] [2,1,0,0] | ( ( 2, 1), ( 1, 0)) ((2,1),(1,0)) | S 2 ​ ( 8) S_{2}(8) |

8 8 | 8 = [2 2 + 2 1 + 2 0] + [2 0] 8=[2^{2}+2^{1}+2^{0}]+[2^{0}] | [3, 0, 1, 0] [3,0,1,0] | ( ( 2, 2), ( 0, 0)) ((2,2),(0,0)) | S 2 ​ ( 8) S_{2}(8) |

8 8 | 8 = [2 3] 8=[2^{3}] | [1, 0, 0, 0, 0] [1,0,0,0,0] | ( 3, 0) (3,0) | S 3 ​ ( 8) S_{3}(8) |

Figure 1: The graphs of functions s ⁡ ( m) s(m) and d ⁡ ( m) d(m)

0 0 50 50 100 100 150 150 200 200 250 250 300 300 0 0 200 200 400 400 600 600 m m s ⁡ ( m) s(m) Function s ⁡ ( m) s(m)

0 0 50 50 100 100 150 150 200 200 250 250 300 300 0 0 10,000 10{,}000 20,000 20{,}000 30,000 30{,}000 40,000 40{,}000 50,000 50{,}000 m m d ⁡ ( m) = ∑ l = 1 m s ⁡ ( l) d(m)=\sum_{l=1}^{m}s(l) Function d ⁡ ( m) d(m)

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2111.03950
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2111.03951
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2111.03951
[7]: https://arxiv.org/abs/2111.03951
[8]: /html/2111.03952
