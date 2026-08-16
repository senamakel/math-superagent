<!-- source: https://arxiv.org/html/2211.09055v2 | converted from HTML -->

A constant lower bound for the union-closed sets conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2211.09055v2 [math.CO] 28 Nov 2022

# A constant lower bound for the union-closed sets conjecture

Justin Gilmer Thanks: gilmer@google.com Affiliation: Google Research, Brain Team

###### Abstract

We show that for any union-closed family ℱ ⊆ 2 [n], ℱ ≠ { ∅ } \mathcal{F}\subseteq 2^{[n]},\mathcal{F}\neq\{\emptyset\}, there exists an i ∈ [n] i\in[n] which is contained in a 0.01 0.01 fraction of the sets in ℱ \mathcal{F}. This is the first known constant lower bound, and improves upon the Ω ⁡ ( log 2 ⁡ ( | ℱ |) − 1) \Omega(\log_{2}(|\mathcal{F}|)^{-1}) bounds of Knill and Wójick. Our result follows from an information theoretic strengthening of the conjecture. Specifically, we show that if A, B A,B are independent samples from a distribution over subsets of [n] [n] such that P r [i ∈ A] < 0.01 Pr[i\in A]<0.01 for all i i and H ⁡ ( A) > 0 H(A)>0, then H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A).

## 1 Introduction

We study families of finite sets which are *union-closed*. A family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is said to be *union-closed*if for every A, B ∈ ℱ A,B\in\mathcal{F} the set A ∪ B ∈ ℱ A\cup B\in\mathcal{F}. Frankl in 1979 [8] conjectured that any such family ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\} should contain an *abundant element*—that is an i ∈ [n] i\in[n] which is contained in at least half of the sets in ℱ \mathcal{F}. Due to the simplicity of the problem statement, the union-closed conjecture has received substantial interest over the past 40 years, with over 50 publications proving special cases or providing reformulations of the problem [4]. The problem was also explored in Polymath11 [1], which considered several interesting strengthenings to the conjecture, some of which were shown to be false. The best prior bound which does not place additional assumptions on ℱ \mathcal{F} is due to Knill [10] (with improvement by Wójick [12]), who proves that there is an element contained in at least Ω ⁡ ( | ℱ | log 2 ⁡ ( | ℱ |)) \Omega(\frac{|\mathcal{F}|}{\log_{2}(|\mathcal{F}|)}) sets. Some special cases are known which make strong assumptions on the family ℱ \mathcal{F}. For example Balla, Bollabás, and Eccles [3] show the conjecture holds when | ℱ | ≥ 2 3 ​ 2 n |\mathcal{F}|\geq\frac{2}{3}2^{n}. This was later improved by Karpas [9] under the assumption that | ℱ | ≥ 2 n − 1 |\mathcal{F}|\geq 2^{n-1}. We refer the interested reader to the survey of Bruhn and Schaudt [4] for an in depth survey of prior work on the problem.

In this work, we prove the following theorem.

###### Theorem 1.

Let A A and B B denote independent samples from a distribution over subsets of [n] [n]. Assume that for all i ∈ [n] i\in[n], P r [i ∈ A] ≤ 0.01 Pr[i\in A]\leq 0.01. Then H ⁡ ( A ∪ B) ≥ 1.26 ​ H ​ ( A) H(A\cup B)\geq 1.26H(A).

When H ⁡ ( A) > 0 H(A)>0, Theorem 1 implies that H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A). Note that if we sample A, B A,B independently and uniformly at random from a union-closed family ℱ \mathcal{F}, then H ⁡ ( A ∪ B) ≤ H ⁡ ( A) H(A\cup B)\leq H(A). This follows because A ∪ B A\cup B is a distribution over ℱ \mathcal{F} and the entropy of a distribution over ℱ \mathcal{F} is maximized when it is the uniform distribution. We obtain as an immediate corollary

###### Theorem 2.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a union-closed family, ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}. Then there exists i ∈ [n] i\in[n] that is contained in at least a 0.01 0.01 fraction of the sets in ℱ \mathcal{F}.

We note that Theorem 1 operates in a more general setting than the union-closed conjecture as we allow A A to be sampled from an arbitrary probability distribution over a family ℱ \mathcal{F}. Consider the following illustrative examples.

Example 1: Let A = ( A 1, A 2, ⋯, A n) A=(A_{1},A_{2},\cdots,A_{n}) be a random subset of [n] [n] such that each A i A_{i} are iid Bernoulli random variables with probability p p. Then H ⁡ ( A) = H ⁡ ( p) ​ n H(A)=H(p)n and H ⁡ ( A ∪ B) = H ⁡ ( 2 ​ p − p 2) ​ n H(A\cup B)=H(2p-p^{2})n.

Example 2: Let A = [n] A=[n] with probability p p and A = ∅ A=\emptyset with probability 1 − p 1-p. Then H ⁡ ( A) = H ⁡ ( p) H(A)=H(p) and H ⁡ ( A ∪ B) = H ⁡ ( 2 ​ p − p 2) H(A\cup B)=H(2p-p^{2}).

In examples 1 and 2 the ratio H ⁡ ( A ∪ B) H ⁡ ( A) = H ⁡ ( 2 ​ p − p 2) H ⁡ ( p) \frac{H(A\cup B)}{H(A)}=\frac{H(2p-p^{2})}{H(p)}. For these cases, when p < 3 − 5 2 p<\frac{3-\sqrt{5}}{2}, it follows that H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A). When p = 3 − 5 2 p=\frac{3-\sqrt{5}}{2} then H ⁡ ( A ∪ B) = H ⁡ ( A) H(A\cup B)=H(A) and when p > 3 − 5 2 p>\frac{3-\sqrt{5}}{2} we get H ⁡ ( A ∪ B) < H ⁡ ( A) H(A\cup B)<H(A). We hypothesize that these examples are extremal in the following sense: for any distribution A A, if P r [A i ≤ p] Pr[A_{i}\leq p] for all i i then H ⁡ ( A ∪ B) ≥ H ⁡ ( 2 ​ p − p 2) H ⁡ ( p) ​ H ​ ( A) H(A\cup B)\geq\frac{H(2p-p^{2})}{H(p)}H(A).

The following example was useful in motivating some of the proof techniques we employ:

Example 3: Sample A ⊆ [n] A\subseteq[n] in the following manner. First sample A 1 A_{1} from a Bernoulli distribution with probability p p. Then, conditioned on the event that A 1 = 1 A_{1}=1, sample each A i A_{i} from iid Bernoulli distributions with probability q = 0.99 q=0.99. Otherwise, if A 1 = 0 A_{1}=0 then each A i = 0 A_{i}=0. To calculate H ⁡ ( A) H(A), we apply the chain rule to get H ⁡ ( A) = H ⁡ ( A 1, A > 1) = H ⁡ ( A 1) + H ⁡ ( A > 1 | A 1) H(A)=H(A_{1},A_{>1})=H(A_{1})+H(A_{>1}|A_{1}). The conditional entropy can be computed as

 | H ( A > 1 | A 1) = P r [A 1 = 0] ⋅ 0 + P r [A 1 = 1] H ( q) ( n − 1). H(A_{>1}|A_{1})=Pr[A_{1}=0]\cdot 0+Pr[A_{1}=1]H(q)(n-1). |  |

Thus H ⁡ ( A) = H ⁡ ( p) + p ​ H ​ ( q) ​ ( n − 1) H(A)=H(p)+pH(q)(n-1). Via a similar calculation we get H ⁡ ( A ∪ B) = H ⁡ ( 2 ​ p − p 2) + 2 ​ p ​ ( 1 − p) ​ H ​ ( q) ​ ( n − 1) + p 2 ​ H ​ ( 2 ​ q − q 2) ​ ( n − 1) H(A\cup B)=H(2p-p^{2})+2p(1-p)H(q)(n-1)+p^{2}H(2q-q^{2})(n-1).

In Example 3, for n n large and p p small, H ⁡ ( A ∪ B) H(A\cup B) is dominated by the term 2 ​ p ​ ( 1 − p) ​ H ​ ( q) ​ ( n − 1) 2p(1-p)H(q)(n-1). This corresponds to the event that exactly one of A 1, B 1 A_{1},B_{1} is equal to 1 1. It follows that H ⁡ ( A ∪ B) H ⁡ ( A) ≈ 2 ​ ( 1 − p) \frac{H(A\cup B)}{H(A)}\approx 2(1-p). Note in this case, the entropy H ⁡ ( A ∪ B | A 1 = B 1 = 1) H(A\cup B|A_{1}=B_{1}=1) is small relative to H ⁡ ( A | A 1 = 1) H(A|A_{1}=1). We will discuss this example further in Section 4.

Examples 1 and 2 imply that if P r [A i = 1] ≥ 3 − 5 2 Pr[A_{i}=1]\geq\frac{3-\sqrt{5}}{2} then it is possible that H ⁡ ( A ∪ B) ≤ H ⁡ ( A) H(A\cup B)\leq H(A). Because 3 − 5 2 < 0.5 \frac{3-\sqrt{5}}{2}<0.5, any stronger bound for Theorem 1 will not be sufficient to resolve the union-closed conjecture. In Section 5 we discuss a promising direction for additionally leveraging the assumption that A A is chosen uniformly over the family ℱ \mathcal{F} which might improve the bound to 0.5.

## 2 Notation and Preliminaries

Throughout the paper we use log ⁡ ( x) \log(x) to denote the base 2 logarithm of x x. If X, X ′ X,X^{\prime} are Bernoulli random variables, we will use X ∪ X ′ X\cup X^{\prime} to denote max ⁡ ( X, X ′) \max(X,X^{\prime}).

We quickly review two properties of conditional entropy that we require to complete the proofs. We refer the reader to Cover and Thomas [6] for additional background on information theory.

1. 1.

Chain Rule for Entropy: For a sequence of random variables X 1, ⋯, X n X_{1},\cdots,X_{n}, denote X < i = ( X 1, ⋯, X i − 1) X_{<i}=(X_{1},\cdots,X_{i-1}). Then H ⁡ ( X 1, ⋯, X n) = ∑ i H ⁡ ( X i | X < i) H(X_{1},\cdots,X_{n})=\sum\limits_{i}H(X_{i}|X_{<i}).

2. 2.

For random variables X X and Y Y and a function f ⁡ ( Y) f(Y),

 | H ⁡ ( X | Y) ≤ H ⁡ ( X | f ⁡ ( Y)). H(X|Y)\leq H(X|f(Y)). |  |

We quickly prove property (2).

###### Proof.

The sequence X → Y → f ⁡ ( Y) X\rightarrow Y\rightarrow f(Y) forms a Markov chain. Thus by the data processing inequality:

 | I ⁡ ( X: f ⁡ ( Y)) \displaystyle I(X:f(Y)) | ≤ I ⁡ ( X: Y) \displaystyle\leq I(X:Y) |  |

 | H ⁡ ( X) − H ⁡ ( X | f ⁡ ( Y)) \displaystyle H(X)-H(X|f(Y)) | ≤ H ⁡ ( X) − H ⁡ ( X | Y) \displaystyle\leq H(X)-H(X|Y) |  |

 | H ⁡ ( X | Y) \displaystyle H(X|Y) | ≤ H ⁡ ( X | f ⁡ ( Y)) \displaystyle\leq H(X|f(Y)) |  |

∎

## 3 Main Result

In this section we prove our main result. We use A < i = ( A 1, ⋯, A i − 1) A_{<i}=(A_{1},\cdots,A_{i-1}) to denote the sequence of indicator random variables, where A i = 1 A_{i}=1 if and only if i ∈ A i\in A. The proof strategy relies on revealing the bits of A ∪ B A\cup B and A A one at a time and showing at each step that

 | H ⁡ ( ( A ∪ B) i | ( A ∪ B) < i) ≥ 1.26 ​ H ​ ( A i | A < i). H((A\cup B)_{i}|(A\cup B)_{<i})\geq 1.26H(A_{i}|A_{<i}). |  | (1) |

By applying the chain rule this will imply that H ⁡ ( A ∪ B) ≥ 1.26 ​ H ​ ( A) H(A\cup B)\geq 1.26H(A).

The proof of equation ( 1) will rely on this key technical lemma, the proof of which is provided in Section 4.

###### Lemma 1.

Let C C denote a random variable over a finite set S S. For each c ∈ S c\in S, let p c p_{c} be a real number in [0, 1] [0,1]. Let X X be a Bernoulli random variable sampled according to the following process: first sample c ∼ C c\sim C, then sample X X with P ​ r ​ [X = 1 | C = c] = p c Pr[X=1|C=c]=p_{c}. Assume further that 𝔼 ⁡ [X] ≤ 0.01 \mathbb{E}[X]\leq 0.01. Let C ′ C^{\prime} be an iid copy of C C, and sample X ′ X^{\prime} conditioned on C ′ C^{\prime} according to the same process (so P ​ r ​ [X ′ = 1 | C ′ = c] = p c Pr[X^{\prime}=1|C^{\prime}=c]=p_{c}, and X ′ X^{\prime} is independent of X X and C C). Then

 | H ⁡ ( X ∪ X ′ | C, C ′) ≥ 1.26 ​ H ​ ( X | C). H(X\cup X^{\prime}|C,C^{\prime})\geq 1.26H(X|C). |  |

We note that Lemma 1 can be restated a bit more succinctly that assuming { p c } c ∈ S ⊂ [0, 1] \{p_{c}\}_{c\in S}\subset[0,1] is a finite sequence of real numbers satisfying 𝔼 c ​ [p c] ≤ 0.01 \mathbb{E}_{c}[p_{c}]\leq 0.01, then:

 | 𝔼 c, c ′ ​ [H ⁡ ( p c + p c ′ − p c ​ p c ′)] ≥ 1.26 ​ 𝔼 c ​ [H ⁡ ( p c)]. \mathbb{E}_{c,c^{\prime}}\left[H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})\right]\geq 1.26\mathbb{E}_{c}\left[H(p_{c})\right]. |  |

Here, X, X ′ X,X^{\prime} correspond to the random bits A i, B i A_{i},B_{i} respectively, and C, C ′ C,C^{\prime} correspond to the histories A < i, B < i A_{<i},B_{<i}. The constant 0.01 0.01 was not optimized as new ideas will be needed to achieve a tight result. We hypothesize that if 𝔼 ⁡ [X] < 3 − 5 2 \mathbb{E}[X]<\frac{3-\sqrt{5}}{2}, then H ⁡ ( X ∪ X ′ | C, C ′) ≥ ( 1 + ϵ) ​ H ​ ( X | C) H(X\cup X^{\prime}|C,C^{\prime})\geq(1+\epsilon)H(X|C) for an ϵ > 0 \epsilon>0 which depends on the value of 𝔼 ⁡ [X] \mathbb{E}[X]. We discuss challenges in obtaining a stronger bound for Lemma 1 along with counter examples to natural strengthenings in Section 4.

Assuming Lemma 1, we now prove our main result:

###### Theorem 1.

Let A, B A,B be independent samples from a distribution over subsets of [n] [n] such that P r [i ∈ A] ≤ 0.01 Pr[i\in A]\leq 0.01 for all i i. Then H ⁡ ( A ∪ B) ≥ 1.26 ​ H ​ ( A) H(A\cup B)\geq 1.26H(A).

###### Proof.

We first show for all i i,

 | H ⁡ ( ( A ∪ B) i | ( A ∪ B) < i) ≥ 1.26 ​ H ​ ( A i | A < i). H((A\cup B)_{i}|(A\cup B)_{<i})\geq 1.26H(A_{i}|A_{<i}). |  |

By applying property (2) of conditional entropy we get

 | H ⁡ ( ( A ∪ B) i | ( A ∪ B) < i) ≥ H ⁡ ( ( A ∪ B) i | A < i, B < i). H((A\cup B)_{i}|(A\cup B)_{<i})\geq H((A\cup B)_{i}|A_{<i},B_{<i}). |  | (2) |

We pause here to remark that ( 2) is the crucial step which takes advantage of the power of the information theoretic formulation. Because ( A ∪ B) < i (A\cup B)_{<i} is simply a function of A < i, B < i A_{<i},B_{<i}, the entropy in ( A ∪ B) i (A\cup B)_{i} can not increase if we additionally assume we know the full history of A < i, B < i A_{<i},B_{<i}. Conditioning on A < i, B < i A_{<i},B_{<i} dramatically simplifies the analysis, as these are iid. Additionally, A i A_{i} and B i B_{i} are Bernoulli random variables whose distribution are determined by the sampled values of A < i A_{<i} and B < i B_{<i} respectively. Thus by Lemma 1 we conclude that

 | H ⁡ ( ( A ∪ B) i | A < i, B < i) ≥ 1.26 ​ H ​ ( A i | A < i). H((A\cup B)_{i}|A_{<i},B_{<i})\geq 1.26H(A_{i}|A_{<i}). |  | (3) |

To end the proof we repeatedly apply the chain rule to conclude that

 | H ⁡ ( A ∪ B) ≥ 1.26 ​ H ​ ( A). H(A\cup B)\geq 1.26H(A). |  | (4) |

∎

## 4 Proof of Lemma 1

For this section, we can forget all of the structure contained in the random variables A < i A_{<i} and B < i B_{<i}. Lemma 1 only assumes that they are iid over some finite set S S. Recall that Lemma 1 can be stated as

 | 𝔼 c, c ′ ​ [H ⁡ ( p c + p c ′ − p c ​ p c ′)] ≥ 1.26 ​ 𝔼 c ​ [H ⁡ ( p c)] \mathbb{E}_{c,c^{\prime}}\left[H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})\right]\geq 1.26\mathbb{E}_{c}\left[H(p_{c})\right] |  | (5) |

under the assumption that 𝔼 c ​ [p c] ≤ 0.01 = μ \mathbb{E}_{c}[p_{c}]\leq 0.01=\mu.

A natural approach to Lemma 1 is to try to apply Jensen’s inequality to the function f ⁡ ( p c, p c ′) = H ⁡ ( p c + p c ′ − p c ​ p c ′) − H ⁡ ( p c) f(p_{c},p_{c^{\prime}})=H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})-H(p_{c}). However, this f f is not convex in p c ′ p_{c^{\prime}}. Additionally, it does not hold in general that 𝔼 c, c ′ ​ [H ⁡ ( p c + p c ′ − p c ​ p c ′) − H ⁡ ( p c)] ≥ H ⁡ ( 2 ​ μ − μ 2) − H ⁡ ( μ) \mathbb{E}_{c,c^{\prime}}\left[H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})-H(p_{c})\right]\geq H(2\mu-\mu^{2})-H(\mu). For example, conditioned on C C there may be no entropy left in X X, in which case the left hand side is 0! This is exactly what will happen in Example 2 discussed in the introduction—after revealing the first bit A 1 A_{1}, all subsequent bits become deterministic. This example demonstrates that some natural symmetrizations such as g ⁡ ( p c, p c ′) = H ⁡ ( p c + p c ′ − p c ​ p c ′) − H ⁡ ( p c) + H ⁡ ( p c ′) 2 g(p_{c},p_{c^{\prime}})=H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})-\frac{H(p_{c})+H(p_{c^{\prime}})}{2} are not convex.

Another natural approach is to look for a purely information theoretic proof of Lemma 1. Indeed, one hypothesis is that there is nothing special about the union function here, but for any function f f, H ⁡ ( f ⁡ ( X, X ′) | C, C ′) ≥ H ⁡ ( X | C) H(f(X,X^{\prime})|C,C^{\prime})\geq H(X|C) whenever H ⁡ ( f ⁡ ( X, X ′)) ≥ H ⁡ ( X) H(f(X,X^{\prime}))\geq H(X). However, this strengthening turns out to be false. Consider the case where both X X and C C are uniform over the set { 0, 1, 2, 3 } \{0,1,2,3\}. Furthermore, let X | C X|C be uniform over { 0, 2 } \{0,2\} when C ∈ { 0, 2 } C\in\{0,2\}, and X | C X|C be uniform over { 1, 3 } \{1,3\} when C ∈ { 1, 3 } C\in\{1,3\}. Finally, define f ⁡ ( x, x ′) = ( x mod 2, x ′ mod 2) f(x,x^{\prime})=(x\mod 2,x^{\prime}\mod 2). Then H ⁡ ( f ⁡ ( X, X ′)) = H ⁡ ( X) = log ⁡ ( 4) H(f(X,X^{\prime}))=H(X)=\log(4), H ⁡ ( X | C) = 1 H(X|C)=1, but H ⁡ ( f ⁡ ( X, X ′) | C, C ′) = 0 H(f(X,X^{\prime})|C,C^{\prime})=0. Thus any proof of Lemma 1 will need to make careful use of properties of the union function.

Having been unable to make the above two proof strategies work, we resort to a more direct estimation of the terms in inequality ( 5). Our argument is quite wasteful and surely is far from tight. First we provide a proof sketch. We let 𝒞 0 = { c | p c ≤ 0.1 } \mathcal{C}_{0}=\{c|p_{c}\leq 0.1\} and let 𝒞 1 = 𝒞 0 c \mathcal{C}_{1}=\mathcal{C}_{0}^{c}.

Using the assumption that E ⁡ [X] ≤ 0.01 E[X]\leq 0.01 we apply Markov’s inequality to get that

 | P r [c ∈ 𝒞 1] = P r [p c > 0.1] ≤ E c ​ [p c] 0.1 ≤ 0.1 Pr[c\in\mathcal{C}_{1}]=Pr[p_{c}>0.1]\leq\frac{E_{c}[p_{c}]}{0.1}\leq 0.1 |  | (6) |

This implies that P ​ r ​ [C 0] ≥ 0.9 Pr[C_{0}]\geq 0.9. In what follows we will sometimes write 𝒞 0 \mathcal{C}_{0} as shorthand for the event that C ∈ 𝒞 0 C\in\mathcal{C}_{0}. Similarly 𝒞 0 ′ \mathcal{C}_{0}^{\prime} refers to the event that C ′ ∈ 𝒞 0 C^{\prime}\in\mathcal{C}_{0}. For example, the conditional entropy H ⁡ ( X | C) H(X|C) can be written as

 | H ⁡ ( X | C) = P ​ r ​ [𝒞 0] ​ H ​ ( X | 𝒞 0) + P ​ r ​ [𝒞 1] ​ H ​ ( X | 𝒞 1). H(X|C)=Pr[\mathcal{C}_{0}]H(X|\mathcal{C}_{0})+Pr[\mathcal{C}_{1}]H(X|\mathcal{C}_{1}). |  |

We first note that conditioned on the event that both C, C ′ ∈ C 0 C,C^{\prime}\in C_{0}, the entropy H ⁡ ( X ∪ X ′) H(X\cup X^{\prime}) will be a constant factor larger than H ⁡ ( X) + H ⁡ ( X ′) 2 \frac{H(X)+H(X^{\prime})}{2}. This can be leveraged to prove that

 | P ​ r ​ [𝒞 0] 2 ​ H ​ ( X ∪ X ′ | 𝒞 0, 𝒞 0 ′) ≥ 1.26 ​ P ​ r ​ [𝒞 0] ​ H ​ ( X | 𝒞 0). Pr[\mathcal{C}_{0}]^{2}H(X\cup X^{\prime}|\mathcal{C}_{0},\mathcal{C}_{0}^{\prime})\geq 1.26Pr[\mathcal{C}_{0}]H(X|\mathcal{C}_{0}). |  | (7) |

Then, in the event that exactly one of c, c ′ ∈ 𝒞 0 c,c^{\prime}\in\mathcal{C}_{0} we can show that H ⁡ ( X ∪ X ′) ≥ 0.9 ​ H ​ ( X) H(X\cup X^{\prime})\geq 0.9H(X). Using this property, we will show that

 | 2 ​ P ​ r ​ [𝒞 0] ​ P ​ r ​ [𝒞 1] ​ H ​ ( X ∪ X ′ | 𝒞 0, 𝒞 1 ′) ≥ 1.62 ​ P ​ r ​ [𝒞 1] ​ H ​ ( X | 𝒞 1). 2Pr[\mathcal{C}_{0}]Pr[\mathcal{C}_{1}]H(X\cup X^{\prime}|\mathcal{C}_{0},\mathcal{C}_{1}^{\prime})\geq 1.62Pr[\mathcal{C}_{1}]H(X|\mathcal{C}_{1}). |  | (8) |

Example 3 discussed in the introduction helped to motivate the decomposition considered in equations ( 7) and ( 8). In this example, most of the entropy in H ⁡ ( X | C) H(X|C) comes from the event that A 1 = 1 A_{1}=1 (this corresponds to the event 𝒞 1 \mathcal{C}_{1}). This entropy is dominated by the corresponding event that exactly one of A 1 A_{1} and B 1 B_{1} are equal to 1, which is exactly the conclusion of equation ( 8). This example also demonstrates that entropy coming from the term P r [𝒞 1] 2 H ( X, X ′ | C, C ′ ∈ 𝒞 1) Pr[\mathcal{C}_{1}]^{2}H(X,X^{\prime}|C,C^{\prime}\in\mathcal{C}_{1}) may be small relative to P ​ r ​ [𝒞 1] ​ H ​ ( X | 𝒞 1) Pr[\mathcal{C}_{1}]H(X|\mathcal{C}_{1}). In this work we throw this term away, it is non-negative and the sum of the left hand side of ( 7) and ( 8) are already larger than H ⁡ ( X | C) H(X|C). However, a tight version of Lemma 1 will require a more careful analysis.

We now make the above proof sketch rigorous with the following sequence of lemmas.

###### Lemma 2.

Assume p, p ′ ≤ 0.1 p,p^{\prime}\leq 0.1. Then H ⁡ ( p + p ′ − p ​ p ′) ≥ 1.4 ​ ( H ⁡ ( p) + H ⁡ ( p ′) 2) H(p+p^{\prime}-pp^{\prime})\geq 1.4\left(\frac{H(p)+H(p^{\prime})}{2}\right).

###### Proof.

Note the lemma holds when p = p ′ = 0 p=p^{\prime}=0. We let D = [0, 0.1] × [0, 0.1] − { ( 0, 0) } D=[0,0.1]\times[0,0.1]-\{(0,0)\}. Figure 1 plots the function f ⁡ ( p, p ′) = 2 ​ H ​ ( p + p ′ − p ​ p ′) H ⁡ ( p) + H ⁡ ( p ′) f(p,p^{\prime})=\frac{2H(p+p^{\prime}-pp^{\prime})}{H(p)+H(p^{\prime})} for ( p, p ′) ∈ D (p,p^{\prime})\in D where the lemma can be checked visually. More formally, by concavity of H H, H ⁡ ( p) + H ⁡ ( p ′) 2 ≤ H ⁡ ( p + p ′ 2) \frac{H(p)+H(p^{\prime})}{2}\leq H\left(\frac{p+p^{\prime}}{2}\right). Additionally, when 0 ≤ p, p ′ ≤ 0.1 0\leq p,p^{\prime}\leq 0.1, we have p + p ′ − p ​ p ′ ≥ 0.9 ​ ( p + p ′) p+p^{\prime}-pp^{\prime}\geq 0.9(p+p^{\prime}). Thus in the given domain, f ⁡ ( p, p ′) ≥ H ​ ( 0.9 ​ ( p + p ′)) H ​ ( 0.5 ​ ( p + p ′)) f(p,p^{\prime})\geq\frac{H(0.9(p+p^{\prime}))}{H(0.5(p+p^{\prime}))}. The function g ⁡ ( p) = H ⁡ ( 0.9 ​ p) H ⁡ ( 0.5 ​ p) g(p)=\frac{H(0.9p)}{H(0.5p)} for p ∈ ( 0, 0.2] p\in(0,0.2] is minimized at p = 0.2 p=0.2. This implies that over the domain, f ⁡ ( p, p ′) > g ⁡ ( 0.2) = 1.45 f(p,p^{\prime})>g(0.2)=1.45. ∎

###### Lemma 3.

For any p, p ′ ∈ [0, 1] p,p^{\prime}\in[0,1], H ⁡ ( p + p ′ − p ​ p ′) ≥ ( 1 − p) ​ H ​ ( p ′) H(p+p^{\prime}-pp^{\prime})\geq(1-p)H(p^{\prime}).

###### Proof.

By concavity of H H,

 | H ⁡ ( p ⋅ 1 + ( 1 − p) ​ p ′) ≥ p ​ H ​ ( 1) + ( 1 − p) ​ H ​ ( p ′) = ( 1 − p) ​ H ​ ( p ′). H(p\cdot 1+(1-p)p^{\prime})\geq pH(1)+(1-p)H(p^{\prime})=(1-p)H(p^{\prime}). |  |

∎

For the next lemmas, we use q q to denote the distribution of C C, that is q ( c) = P r [C = c] q(c)=Pr[C=c]. Additionally q 0 q_{0} denotes the distribution of C C conditioned on the event that C ∈ 𝒞 0 C\in\mathcal{C}_{0}. So for c ∈ 𝒞 0 c\in\mathcal{C}_{0}, q 0 ​ ( c) = q ⁡ ( c) P r [C ∈ 𝒞 0] q_{0}(c)=\frac{q(c)}{Pr[C\in\mathcal{C}_{0}]}.

[image: Refer to caption] Figure 1: Plotting the function f ⁡ ( p, p ′) = 2 ​ H ​ ( p + p ′ − p ​ p ′) H ⁡ ( p) + H ⁡ ( p ′) f(p,p^{\prime})=\frac{2H(p+p^{\prime}-pp^{\prime})}{H(p)+H(p^{\prime})} over 0 ≤ p, p ′ ≤ 0.1 0\leq p,p^{\prime}\leq 0.1. The minimum value of 1.496 1.496 is achieved at p = p ′ = 0.1 p=p^{\prime}=0.1.

###### Lemma 4.

Under the assumption that 𝔼 ⁡ [X] ≤ 0.01 \mathbb{E}[X]\leq 0.01,

 | P ​ r ​ [𝒞 0] 2 ​ H ​ ( X ∪ X ′ | 𝒞 0, 𝒞 0 ′) ≥ 1.26 ​ P ​ r ​ [𝒞 0] ​ H ​ ( X | C ∈ 𝒞 0) Pr[\mathcal{C}_{0}]^{2}H(X\cup X^{\prime}|\mathcal{C}_{0},\mathcal{C}_{0}^{\prime})\geq 1.26Pr[\mathcal{C}_{0}]H(X|C\in\mathcal{C}_{0}) |  |

###### Proof.

 | P ​ r ​ [𝒞 0] ​ H ​ ( X | C ∈ 𝒞 0) \displaystyle Pr[\mathcal{C}_{0}]H(X|C\in\mathcal{C}_{0}) | = P ​ r ​ [𝒞 0] ​ 𝔼 c ∼ q 0 ​ H ​ ( p c) \displaystyle=Pr[\mathcal{C}_{0}]\mathbb{E}_{c\sim q_{0}}H(p_{c}) |  |

 |  | = P ​ r ​ [𝒞 0] 2 ​ 𝔼 c ∼ q 0 ​ [H ⁡ ( p c) + 𝔼 c ′ ∼ q 0 ​ H ​ ( p c ′)] \displaystyle=\frac{Pr[\mathcal{C}_{0}]}{2}\mathbb{E}_{c\sim q_{0}}\left[H(p_{c})+\mathbb{E}_{c^{\prime}\sim q_{0}}H(p_{c^{\prime}})\right] |  |

 |  | = P ​ r ​ [𝒞 0] ​ 𝔼 c, c ′ ∼ q 0 ​ [H ⁡ ( p c) + H ⁡ ( p c ′) 2] \displaystyle=Pr[\mathcal{C}_{0}]\mathbb{E}_{c,c^{\prime}\sim q_{0}}\left[\frac{H(p_{c})+H(p_{c^{\prime}})}{2}\right] |  |

 | (By Lemma 2) | ≤ P ​ r ​ [𝒞 0] 1.4 ​ [𝔼 c, c ′ ∼ q 0 ​ H ​ ( p c + p c ′ − p c ​ p c ′)] \displaystyle\leq\frac{Pr[\mathcal{C}_{0}]}{1.4}\left[\mathbb{E}_{c,c^{\prime}\sim q_{0}}H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})\right] |  |

 | ( P ​ r ​ [𝒞 0] ≥ 0.9 Pr[\mathcal{C}_{0}]\geq 0.9) | ≤ P ​ r ​ [𝒞 0] 2 1.26 ​ H ​ ( X ∪ X ′ | C, C ′ ∈ 𝒞 0) \displaystyle\leq\frac{Pr[\mathcal{C}_{0}]^{2}}{1.26}H(X\cup X^{\prime}|C,C^{\prime}\in\mathcal{C}_{0}) |  |

Multiplying both sides by 1.26 1.26 yields the desired result.

∎

###### Lemma 5.

Under the assumption that 𝔼 ⁡ [X] ≤ 0.01 \mathbb{E}[X]\leq 0.01,

 | 2 ​ P ​ r ​ [𝒞 0, 𝒞 1 ′] ​ H ​ ( X ∪ X ′ | 𝒞 0, 𝒞 1 ′) ≥ 1.62 ​ P ​ r ​ [𝒞 1] ​ H ​ ( X | C ∈ 𝒞 1) 2Pr[\mathcal{C}_{0},\mathcal{C}_{1}^{\prime}]H(X\cup X^{\prime}|\mathcal{C}_{0},\mathcal{C}_{1}^{\prime})\geq 1.62Pr[\mathcal{C}_{1}]H(X|C\in\mathcal{C}_{1}) |  |

###### Proof.

 | 2 ​ P ​ r ​ [𝒞 0, 𝒞 1 ′] ​ H ​ ( X ∪ X ′ | 𝒞 0, 𝒞 1 ′) \displaystyle 2Pr[\mathcal{C}_{0},\mathcal{C}_{1}^{\prime}]H(X\cup X^{\prime}|\mathcal{C}_{0},\mathcal{C}_{1}^{\prime}) | = 2 ​ ∑ c ∈ 𝒞 0, c ′ ∈ 𝒞 1 q ⁡ ( c) ​ q ​ ( c ′) ​ H ​ ( p c + p c ′ − p c ​ p c ′) \displaystyle=2\sum\limits_{c\in\mathcal{C}_{0},c^{\prime}\in\mathcal{C}_{1}}q(c)q(c^{\prime})H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}}) |  |

 | (by Lemma 3) | ≥ 2 ​ ∑ c ∈ 𝒞 0, c ′ ∈ 𝒞 1 q ⁡ ( c) ​ q ​ ( c ′) ​ ( 1 − p c) ​ H ​ ( p c ′) \displaystyle\geq 2\sum\limits_{c\in\mathcal{C}_{0},c^{\prime}\in\mathcal{C}_{1}}q(c)q(c^{\prime})(1-p_{c})H(p_{c^{\prime}}) |  |

 |  | = 2 ​ ∑ c ∈ 𝒞 0 q ⁡ ( c) ​ ( 1 − p c) ​ [∑ c ′ ∈ 𝒞 1 q ⁡ ( c ′) ​ H ​ ( p c ′)] \displaystyle=2\sum\limits_{c\in\mathcal{C}_{0}}q(c)(1-p_{c})\left[\sum\limits_{c^{\prime}\in\mathcal{C}_{1}}q(c^{\prime})H(p_{c^{\prime}})\right] |  |

 |  | = 2 ​ P ​ r ​ [𝒞 1 ′] ​ H ​ ( X ′ | 𝒞 1 ′) ​ ∑ c ∈ 𝒞 0 q ⁡ ( c) ​ ( 1 − p c) \displaystyle=2Pr[\mathcal{C}_{1}^{\prime}]H(X^{\prime}|\mathcal{C}_{1}^{\prime})\sum_{c\in\mathcal{C}_{0}}q(c)(1-p_{c}) |  |

 | (using p c ≤ 0.1 p_{c}\leq 0.1) | ≥ 2 ​ P ​ r ​ [𝒞 1 ′] ​ H ​ ( X | 𝒞 1 ′) ​ ∑ c ∈ 𝒞 0 q ⁡ ( c) ​ 0.9 \displaystyle\geq 2Pr[\mathcal{C}_{1}^{\prime}]H(X|\mathcal{C}_{1}^{\prime})\sum_{c\in\mathcal{C}_{0}}q(c)0.9 |  |

 |  | = 1.8 ​ P ​ r ​ [𝒞 0] ​ P ​ r ​ [𝒞 1 ′] ​ H ​ ( X ′ | 𝒞 1 ′) \displaystyle=1.8Pr[\mathcal{C}_{0}]Pr[\mathcal{C}_{1}^{\prime}]H(X^{\prime}|\mathcal{C}_{1}^{\prime}) |  |

 | (using P ​ r ​ [𝒞 0] ≥ 0.9 Pr[\mathcal{C}_{0}]\geq 0.9) | ≥ 1.62 ​ P ​ r ​ [𝒞 1 ′] ​ H ​ ( X ′ | 𝒞 1 ′) \displaystyle\geq 1.62Pr[\mathcal{C}_{1}^{\prime}]H(X^{\prime}|\mathcal{C}_{1}^{\prime}) |  |

∎

We can now quickly finish the proof of Lemma 1.

###### Proof.

To show that H ⁡ ( X ∪ X ′ | C, C ′) ≥ 1.26 ​ H ​ ( X | C) H(X\cup X^{\prime}|C,C^{\prime})\geq 1.26H(X|C), we write H ⁡ ( X ∪ X ′ | C, C ′) H(X\cup X^{\prime}|C,C^{\prime}) as a sum of three disjoint events:

1. 1.

P ​ r ​ [C, C ′ ∈ 𝒞 0] ​ H ​ ( X ∪ X ′ | C, C ′ ∈ 𝒞 0) Pr[C,C^{\prime}\in\mathcal{C}_{0}]H(X\cup X^{\prime}|C,C^{\prime}\in\mathcal{C}_{0})

2. 2.

2 P r [C ∈ 𝒞 0] P r [C ′ ∈ 𝒞 1] H ( X ∪ X ′ | C ∈ 𝒞 0, C ′ ∈ 𝒞 1) 2Pr[C\in\mathcal{C}_{0}]Pr[C^{\prime}\in\mathcal{C}_{1}]H(X\cup X^{\prime}|C\in\mathcal{C}_{0},C^{\prime}\in\mathcal{C}_{1})

3. 3.

P ​ r ​ [C, C ′ ∈ 𝒞 1] ​ H ​ ( X ∪ X ′ | C, C ′ ∈ 𝒞 1) Pr[C,C^{\prime}\in\mathcal{C}_{1}]H(X\cup X^{\prime}|C,C^{\prime}\in\mathcal{C}_{1})

By Lemma 4, event (1) has higher entropy than 1.26 P r [C ∈ 𝒞 0] H ( X | C ∈ 𝒞 0) 1.26Pr[C\in\mathcal{C}_{0}]H(X|C\in\mathcal{C}_{0}). By Lemma 5, event (2) has higher entropy than 1.62 P r [C ∈ 𝒞 1] H ( X | C ∈ 𝒞 1) 1.62Pr[C\in\mathcal{C}_{1}]H(X|C\in\mathcal{C}_{1}). Finally, event (3) has non-negative entropy. Thus H ⁡ ( X ∪ X ′ | C, C ′) ≥ 1.26 ​ H ​ ( X | C) H(X\cup X^{\prime}|C,C^{\prime})\geq 1.26H(X|C).

∎

## 5 A possible path towards resolving the conjecture

It is clear that there is more ground to be covered with the information theoretic approach we have initiated in this work. A tight version of Lemma 1 would imply a 3 − 5 2 \frac{3-\sqrt{5}}{2} lower bound on the maximum element frequency for union-closed families. Because 3 − 5 2 < 1 2 \frac{3-\sqrt{5}}{2}<\frac{1}{2}, additional ideas will be needed to resolve union-closed conjecture. In this section we discuss a potential direction towards this strengthening.

In cases where p p is close to 1 2 \frac{1}{2}, the distribution of A ∪ B A\cup B seems to be far from uniform. Thus it may still hold that | ℱ ∪ ℱ | > | ℱ | |\mathcal{F}\cup\mathcal{F}|>|\mathcal{F}| 1 1 1 We use ℱ ∪ ℱ \mathcal{F}\cup\mathcal{F} to denote { A ∪ B | A, B ∈ ℱ } \{A\cup B|A,B\in\mathcal{F}\}. even though H ⁡ ( A ∪ B) ≤ H ⁡ ( A) H(A\cup B)\leq H(A). To quantify how far from uniform the distribution A ∪ B A\cup B is, it is useful to consider the KL-divergence D ( A ∪ B | | A) D(A\cup B||A). When A A is the uniform distribution over a union-closed family ℱ \mathcal{F}, it holds that 2 2 2 See [6] Theorem 2.6.4.

 | D ( A ∪ B | | A) + H ( A ∪ B) = H ( A) = log ( | ℱ |). D(A\cup B||A)+H(A\cup B)=H(A)=\log(|\mathcal{F}|). |  | (9) |

We can study the quantity D ( A ∪ B | | A) + H ( A ∪ B) D(A\cup B||A)+H(A\cup B) for more general distributions A A —say if A A is not the uniform distribution, or ℱ \mathcal{F} is not union-closed. For example, if A A denotes a single bit with probability p p of being 1, then when p = 0.5 p=0.5 it holds exactly that D ( A ∪ B | | A) + H ( A ∪ B) D(A\cup B||A)+H(A\cup B) = H ⁡ ( A) = 1.0 H(A)=1.0. However, if p < 0.5 p<0.5 it holds that

 | D ( A ∪ B | | A) + H ( A ∪ B) > H ( A). D(A\cup B||A)+H(A\cup B)>H(A). |  | (10) |

If equation ( 10) ever holds for a distribution A A, we can conclude that either A A is not the uniform distribution over ℱ \mathcal{F} or the distribution A ∪ B A\cup B has support outside of ℱ \mathcal{F}.

Thus the union-closed sets conjecture would follow from showing the following:

###### Conjecture 1.

Let A, B A,B be iid samples from a distribution over a family of subsets of [n] [n]. Assume that P r [i ∈ A] < 0.5 Pr[i\in A]<0.5 for all i i, and H ⁡ ( A) > 0 H(A)>0. Then H ( A ∪ B) + D ( A ∪ B | | A) > H ( A) H(A\cup B)+D(A\cup B||A)>H(A).

## 6 Conclusion

We have established the first constant lower bound for the union-closed conjecture by studying the entropy of the union of two iid samples from a family ℱ \mathcal{F}. The methods presented are strong enough to derive the stronger conclusion that H ⁡ ( A ∪ B) ≥ C p ​ H ​ ( a) H(A\cup B)\geq C_{p}H(a) for a constant C p > 0 C_{p}>0 which depends on p = max i P r [A i = 1] p=\max\limits_{i}{Pr[A_{i}=1]}. However, we certainly have not derived the strongest possible bound C p C_{p}. We are hopeful that the approach initiated in this work will lead to a proof of the conjecture. Beyond proving the union-closed conjecture, the following questions could be interesting to consider

1. 1.

Does it hold for any distribution A A with P r [A i = 1] ≤ p Pr[A_{i}=1]\leq p for all i i that H ⁡ ( A ∪ B) ≥ H ⁡ ( 2 ​ p − p 2) H ⁡ ( p) ​ H ​ ( A) H(A\cup B)\geq\frac{H(2p-p^{2})}{H(p)}H(A)?

2. 2.

Does Conjecture 1 hold?

3. 3.

Under what other assumptions on the distributions A, B A,B does it hold that H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A)? Suppose for example that for fixed k k it holds that for every X ∈ ( [n] k) X\in\binom{[n]}{k}, P r [X ⊆ A] < p Pr[X\subseteq A]<p. How small does p p need to be to conclude that H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A)?

Update (11/27/2022) Shortly after publication of this preprint, three publications appeared which all prove tight versions of our Lemma 1 [5, 11, 2]. These results improve the resulting bound on Frankl’s conjecture to 3 − 5 2 ≈.38 \frac{3-\sqrt{5}}{2}\approx.38. Sawin [11] confirm Question 1 when p ≤ 3 − 5 2 p\leq\frac{3-\sqrt{5}}{2}. However, when p > 3 − 5 2 p>\frac{3-\sqrt{5}}{2} it only holds that H ⁡ ( A ∪ B) ≥ ( 1 − p) ​ 2 5 − 1 H(A\cup B)\geq(1-p)\frac{2}{\sqrt{5}-1}. Sawin [11] and Ellis [7] provide constructions refuting Conjecture 1. It is noteworthy that Sawin’s construction demonstrates that, without placing additional assumptions on the distribution A A, incorporating the KL term cannot improve the resulting bound on Frankl’s conjecture.

## Acknowledgement

The author is grateful to Michael Saks and Swastik Kopparty for enlightening discussions and for reviewing initial versions of this work. Additionally, the author thanks Phil Long for his careful reading and feedback on the manuscript.

## References

- [1] Polymath11. https://gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/.
- [2] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.11731, 2022.
- [3] Igor Balla, Béla Bollobás, and Tom Eccles. Union-closed families of sets. Journal of Combinatorial Theory, Series A, 120(3):531–544, 2013.
- [4] Henning Bruhn and Oliver Schaudt. The journey of the union-closed sets conjecture. Graphs and Combinatorics, 31(6):2043–2074, 2015.
- [5] Zachary Chase and Shachar Lovett. Approximate union closed conjecture. arXiv preprint arXiv:2211.11689, 2022.
- [6] Thomas M Cover and A Thomas Joy. Elements of information theory. John Wiley & Sons, 1999.
- [7] David Ellis. Note: a counterexample to a conjecture of gilmer which would imply the union-closed conjecture. arXiv preprint arXiv:2211.12401, 2022.
- [8] P Frankl. Extremal set systems. Handbook of combinatorics, 2:1293–1329, 1995.
- [9] Ilan Karpas. Two results on union-closed families. arXiv preprint arXiv:1708.01434, 2017.
- [10] Emanuel Knill. Graph generated union-closed families of sets. arXiv preprint math/9409215, 1994.
- [11] Will Sawin. An improved lower bound for the union-closed set conjecture. arXiv preprint arXiv:2211.11504, 2022.
- [12] Piotr Wójcik. Union-closed families of sets. Discrete Mathematics, 199(1-3):173–182, 1999.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
