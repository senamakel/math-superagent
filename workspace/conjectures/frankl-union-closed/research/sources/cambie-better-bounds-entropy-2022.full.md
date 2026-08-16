<!-- source: https://arxiv.org/html/2212.12500v2 | converted from HTML -->

Better bounds for the union-closed sets conjecture using the entropy approach

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2212.12500v2 [math.CO] 16 Feb 2025

# Better bounds for the union-closed sets conjecture using the entropy approach

Stijn Cambie Thanks: Extremal Combinatorics and Probability Group (ECOPRO), Institute for Basic Science (IBS), Daejeon, South Korea, supported by the Institute for Basic Science (IBS-R029-C4), E-mail: stijn.cambie@hotmail.com

###### Abstract

We improve the best known constant 3 − 5 2 \frac{3-\sqrt{5}}{2} for which the union-closed conjecture is known to be true, by using dependent samples as suggested by Sawin and the entropy approach on this problem initiated by Gilmer. Meanwhile, we focus on the intuition behind this entropy approach and its boundaries.

## 1 Introduction

The union-closed conjecture is a challenging conjecture in extremal set theory, see e.g. [11, sec. 32], which became famous due to its elegance. A union-closed family ℱ \mathcal{F} is a collection of sets such that the union of any two sets belongs to ℱ \mathcal{F} as well. The union-closed conjecture states that if ℱ \mathcal{F} contains at least one nonempty set, then there is an element that belongs to at least half of the sets in ℱ. \mathcal{F}. This can be formally stated as follows, where we recommend the reader who is not familiar with some of the terminology, notations or definitions to first have a look at Subsection 1.1.

###### Conjecture 1 (Union-closed conjecture).

If ℱ ≠ { ∅ } \mathcal{F}\not=\{\emptyset\} is a union-closed family with ground set [n], [n], then there exists an element i ∈ [n] i\in[n] such that at least half of the sets in ℱ \mathcal{F} contain i i, i.e., | ℱ ⁡ ( i) | ≥ | ℱ | 2. \lvert\mathcal{F}(i)\rvert\geq\frac{\lvert\mathcal{F}\rvert}{2}.

This would be tight by taking all subsets of a fixed ground set. Indeed, if ℱ = 2 [m], \mathcal{F}=2^{[m]}, then every integer i ∈ [m] i\in[m] appears in exactly 2 m − 1 2^{m-1} sets of ℱ. \mathcal{F}. Possibly, these are essentially the only tight examples (duplicating elements does not change the structure), as also suggested in the blog on the Polymath project; https://gowers.wordpress.com/2016/01/21/.

According to [2, 3, 11], the union-closed conjecture was already a folklore conjecture since the late 1960s or beginning 1970s, and was made well-known by Frankl, who rediscovered it in the late 1970s (1979 according to [10]), and Ron Graham. Nonetheless, the first formal publication containing it might be [19]. In the 90 90 s, it was proven in [16, 21] that there is an element that appears in at least a Ω ⁡ ( log ⁡ | ℱ | | ℱ |) \Omega\left(\frac{\log\lvert\mathcal{F}\rvert}{\lvert\mathcal{F}\rvert}\right) fraction of all sets. The latter result is also implied by the union-closed size problem by Reimer [18], which was fully resolved in [3]. In contrast to the union-closed size problem, which was solved in 10 10 years, the union-closed conjecture is still open. It has been proven in various specific cases, e.g. for certain random generated union-closed families it has been proven to be true with high probability [2]. More on the history till 2015 2015, with other equivalent formulations of the conjecture, can be found in the survey [5]. One equivalent formulation by [4] states that every bipartite graph with at least one edge has at least one vertex in each bipartition class that belongs to at most half of the maximal independent sets. At the beginning of 2017 2017, Karpas [15] proved the union-closed conjecture for families that contain roughly at least half of all sets.

Very recently, Gilmer [12] proved the first linear bound using an elegant entropy-based method. As such he resolved the ε \varepsilon -Union-Closed Sets Conjecture, as stated in [13]. Gilmer claimed that a tight version of his method could prove a fraction equal to 3 − 5 2, \frac{3-\sqrt{5}}{2}, which was soon verified by [1, 7, 20]. The tight version heavily depends on determining the minimum of a function h ⁡ ( x 2) x ​ h ​ ( x) \frac{h(x^{2})}{xh(x)}, where h h is the binary entropy function. Chase and Lovett [7] gave a clear, short proof using the minimum determined by [1].

A question and conjecture of Gilmer were soon answered in the negative, by [20, 9]. By working with approximate union-closed families in [7], 3 − 5 2 \frac{3-\sqrt{5}}{2} seemed possibly the best constant one could aim for with the idea of Gilmer [12]. Nevertheless, as suggested by Sawin [20], this is not the case. For this, we address the following question, from which the improved constant can be concluded later. Note the inequality cannot be strict, since for any { 0, 1 } \{0,1\} -valued random variable equality does hold.

###### Question 2 (Sawin).

What is the maximum value c c for which there exists an α ∈ [0, 1] \alpha\in[0,1] such that the following is true? For every p, q, r p,q,r identically distributed [0, 1] [0,1] -valued random variables with expectation less than c c, where p p and q q are independent, but p p and r r are not necessarily independent, we have

 | ( 1 − α) ​ 𝔼 ​ [H ⁡ ( p + q − p ​ q)] + α ​ 𝔼 ​ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] ≥ 𝔼 ⁡ [H ⁡ ( p)]. (1-\alpha)\,\mathbb{E}[H(p+q-pq)]+\alpha\,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]\geq\,\mathbb{E}[H(p)]. |  | (1) |

Yu [22] considered the approach and question of Sawin in larger generality and derived bounds expressed in general optimisation forms.

Our contribution consists in solving Question 2 exactly and as such improving the constant for which the union-closed conjecture is true. The core content is written in Section 2. Here, we start with explaining the entropy approach in general. After that, we give some intuition why the bound can be improved despite the sharpness of the approximate union-closed conjecture by [7] and why the direct use of Sawin’s idea cannot improve the constant too much. For this, we provide the upper bound for c c in Question 2, which later will turn out to be sharp. As a last part of this section, in Subsection 2.4, we summarise the additional steps of the proof for the improved constant.

In the next section, Section 3, we prove the best bound of c c in Question 2. In Subsections 3.1 and 3.2, we reduce the possible probability distributions one has to consider and prove that the critical probability distributions have a support containing at most 3 3 values. This is as such the technical core to work out Sawin’s idea and to answer Question 2. After this, we can express the problem as a minimisation problem of a function in 4 4 variables and the optimisation problem can be verified with a computer-verification. In contrast to the detailed work in e.g. [1] for the constant 3 − 5 2 \frac{3-\sqrt{5}}{2}, this is done slightly less rigorous. We need to take into account that the minimisation problem finds a local minimum and there is a finite computer precision involved. By considering some plots, we note that there are two regimes to verify. By observing that the extremal probability distribution is atomic (support has 2 2 elements) in one regime, we prove it more precisely for that regime and conclude. In Section 3.4, we give a precise confirmation by combining our ideas with the strategy of Yu [22]. As such, we can reduce the verification of 2 to a minimisation problem in two variables, which can be solved numerically with graphical confirmation. The graphical confirmation gives information on the behaviour on local and global minima, which in principle is not the case in our previous strategy (3 variables), Yu [22] (4 variables) and Liu [17] (9 variables for a slightly further improved constant). Since the constant is not 1 2 \frac{1}{2} and another core method will be needed for the full resolution, an even more rigorous analysis than has been done is unnecessary, as it does not contribute to further understanding the underlying principles. Finally, in Section 4 we summarise the proof for the improved constant on the union-closed conjecture, based on the answer for Question 2. That is, for c ∼ 0.3823455 c\sim 0.3823455 we prove the following theorem.

###### Theorem 3.

Let ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]} be a nonempty union-closed family. Then there is some element i ∈ [n] i\in[n] that appears in at least c ​ | ℱ | c\lvert\mathcal{F}\rvert many sets of ℱ. \mathcal{F}.

So to recap, in this paper, we prove that by taking a linear combination of probability distributions, not all of them being independent, the bound on the union-closed conjecture derived with the entropy approach of Gilmer [12] can be improved slightly.

### 1.1 Terminology and notation

In this subsection, we collect some basic notation and definitions used in extremal set theory and the entropy method used in the papers related to the work of Gilmer. For more of this, we refer to [11] for extremal set theory and [8] for entropy.

The standard finite set of cardinality n n is denoted with [n] = { 1, 2, …, n }. [n]=\{1,2,\ldots,n\}. A subset of [n] [n] is a set containing some elements from [n] [n] and can possibly be the empty set ∅. \emptyset. A collection of subsets of [n] [n] is called a set system or family ℱ \mathcal{F}. The family 2 [n] 2^{[n]} (the power set of [n] [n]) contains all 2 n 2^{n} possible subsets of [n] [n] and in general a family ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]} is a subset of this power set. A uniform family is a family whose sets all have the same cardinality k. k. The largest k k -uniform family on the ground set [n] [n] is ( [n] k) = { A ⊂ [n]: | A | = k }. \binom{[n]}{k}=\{A\subset[n]\colon\lvert A\rvert=k\}. Similarly we use ( [n] ≥ k) \binom{[n]}{\geq k} to denote { A ⊂ [n]: | A | ≥ k }. \{A\subset[n]\colon\lvert A\rvert\geq k\}.

A family ℱ \mathcal{F} is called union-closed if for every A, B ∈ ℱ A,B\in\mathcal{F} also the union A ∪ B ∈ ℱ. A\cup B\in\mathcal{F}. Using ℱ ∪ ℱ = { A ∪ B: A, B ∈ ℱ }, \mathcal{F}\cup\mathcal{F}=\{A\cup B\colon A,B\in\mathcal{F}\}, a family ℱ \mathcal{F} is union-closed if and only if ℱ ∪ ℱ = ℱ. \mathcal{F}\cup\mathcal{F}=\mathcal{F}. It is approximate union-closed if the latter is true for almost every choice of A, B ∈ ℱ. A,B\in\mathcal{F}. The sets containing a fixed element i i are essentially presented by the family ℱ ⁡ ( i) = { A \ { i }: i ∈ A ∈ ℱ }. \mathcal{F}(i)=\{A\backslash\{i\}\colon i\in A\in\mathcal{F}\}. Similarly, ℱ ⁡ ( i ¯) = { A: i ∉ A ∈ ℱ }. \mathcal{F}(\overline{i})=\{A\colon i\not\in A\in\mathcal{F}\}.

We will use some Landau-notation. Given two functions f, g: ℝ → ℝ f,g\colon\mathbb{R}\to\mathbb{R}, we write

- •

f = o ⁡ ( g) f=o(g) if lim x → ∞ f ⁡ ( x) / g ⁡ ( x) = 0, \lim_{x\to\infty}f(x)/g(x)=0,

- •

f ∼ g f\sim g if lim x → ∞ f ⁡ ( x) / g ⁡ ( x) = 1., \lim_{x\to\infty}f(x)/g(x)=1.,

- •

f = O ⁡ ( g) f=O(g) if there is a constant C C such that lim x → ∞ | f ⁡ ( x) / g ⁡ ( x) | < C, \lim_{x\to\infty}\lvert f(x)/g(x)\rvert<C,

- •

f = Ω ⁡ ( g) f=\Omega(g) if g = O ⁡ ( f), g=O(f),

- •

f = Θ ⁡ ( g) f=\Theta(g) if g = O ⁡ ( f) g=O(f) and f = O ⁡ ( g). f=O(g).

A random variable X X can be related with the probability distribution of the outcomes. The entropy H ⁡ ( X) H(X) of a discrete random variable X X equals the Shannon entropy of its probability sequence and is denoted by H ⁡ ( X). H(X). The support of a probability distribution or random variable, is the subset of the possible outcomes which have positive probability (density function). If the support of X X is a finite set A A, and each outcome x ∈ A x\in A has a probability p x, p_{x}, then

 | H ( X) = − ∑ x ∈ A p x log 2 p x. H(X)=-\sum_{x\in A}p_{x}\log_{2}p_{x}. |  |

It is a fundamental result, a corollary of Jensen’s inequality, that this is bounded by log 2 ⁡ | A |. \log_{2}\lvert A\rvert. For a random variable with only two outcomes, occurring with probabilities p p and 1 − p 1-p, we denote the entropy with the binary entropy function h ⁡ ( p) = − ( p ​ log 2 ​ p + ( 1 − p) ​ log 2 ⁡ ( 1 − p)). h(p)=-(p\log_{2}p+(1-p)\log_{2}(1-p)). 1 1 1 For clarity, the binary entropy function is denoted with h h and the entropy function of a variable with H H. A conditional entropy of a random variable Y Y given X X can be computed as

 | H ( Y | X) = − ∑ x ∈ X, y ∈ Y ℙ ( x, y) log 2 ℙ ⁡ ( x, y) ℙ ⁡ ( x). H(Y|X)\ =-\sum_{x\in X,y\in Y}\,\mathbb{P}(x,y)\log_{2}{\frac{\,\mathbb{P}(x,y)}{\,\mathbb{P}(x)}}. |  |

Here ℙ ⁡ ( x, y) \,\mathbb{P}(x,y) is the probability on the outcome { X = x, Y = y }. \{X=x,Y=y\}. The expectation of a random variable X X is 𝔼 ⁡ [X] = ∑ x ∈ A p x ​ x. \,\mathbb{E}[X]=\sum_{x\in A}p_{x}x. We use ∨ \vee for the logical or, that is x ∨ y x\vee y implies that x x or y y has to be satisfied.

## 2 Preliminaries

In this section, we begin by presenting the main idea behind the entropy approach introduced by Gilmer [12]. We then provide some intuition to explain why the examples from [12, 7], which initially suggest that the constant 3 − 5 2 \frac{3-\sqrt{5}}{2} cannot be improved using this method, can actually be refined. Additionally, we (try to) demonstrate why the linear combination in Question 2 is somewhat necessary 2 2 2 i.e., variants will not be simpler and argue that the constant cannot be significantly improved by solving this question 3 3 3 E.g. [17] gave a variant with tiny improvement. Finally, we summarise the key insights behind the proof. More examples and explanations can also be found in the survey [6].

### 2.1 Why the entropy approach works for the union-closed conjecture

The contraposition of the union-closed conjecture states that if every element i ∈ [n] i\in[n] appears in strictly less than half of the sets of a family ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]}, then ℱ \mathcal{F} is not union-closed and thus | ℱ | < | ℱ ∪ ℱ |. \lvert\mathcal{F}\rvert<\lvert\mathcal{F}\cup\mathcal{F}\rvert. The idea behind the entropy approach initiated by Gilmer [12] is that if one can find a way to sample sets from ℱ ∪ ℱ \mathcal{F}\cup\mathcal{F} such that the entropy is strictly larger than log 2 ⁡ | ℱ |, \log_{2}\lvert\mathcal{F}\rvert, one can conclude that | ℱ | < | ℱ ∪ ℱ |. \lvert\mathcal{F}\rvert<\lvert\mathcal{F}\cup\mathcal{F}\rvert. The latter since the entropy of a random variable with N N possible outcomes is bounded by log 2 ⁡ N. \log_{2}N. Proving that H ⁡ ( A ∪ B) > log 2 ⁡ | ℱ | H(A\cup B)>\log_{2}\lvert\mathcal{F}\rvert where A, B A,B are sampled from ℱ \mathcal{F}, is hard when lacking information on ℱ. \mathcal{F}. It is easier to compare H ⁡ ( A ∪ B) H(A\cup B) with H ⁡ ( A) H(A). For the conclusion to hold, A A needs to be sampled uniform random from ℱ \mathcal{F}. Gilmer [12] did this by taking two uniform independent (iid) random samples A, B A,B from ℱ \mathcal{F} and considering the entropy of the union A ∪ B. A\cup B.

For alternatives, one could sample B B non-uniform from ℱ \mathcal{F}, or have two sampled random variables which are not independent. In that case one tries to do this in such a way that A ∪ B A\cup B is as uniformly distributed over ℱ ∪ ℱ \mathcal{F}\cup\mathcal{F} as possible. Exactly uniformly distributed seems impossible. If ℱ \mathcal{F} would be union-closed and A A is uniform random, A ∪ B A\cup B needs to be equal to A A to ensure that A ∪ B A\cup B is uniformly distributed as well. As a concrete example, when ℱ = ( [2] ≥ 1), \mathcal{F}=\binom{[2]}{\geq 1}, then ℙ ⁡ ( A = { 1 }) ​ ℙ ​ ( B = { 1 }) = 1 3 = ℙ ⁡ ( A = { 2 }) ​ ℙ ​ ( B = { 2 }) \,\mathbb{P}(A=\{1\})\,\mathbb{P}(B=\{1\})=\frac{1}{3}=\,\mathbb{P}(A=\{2\})\,\mathbb{P}(B=\{2\}) is impossible. Once one is sampling dependent samples, one would need additional ideas to know more about the conditional probability distributions. Sawin [20] gave the most natural choice when sampling the sets element-wise.

### 2.2 Observations on approximate union-closed set system

Let ψ = 3 − 5 2 \psi=\frac{3-\sqrt{5}}{2} be the smallest root of 2 ​ x − x 2 = 1 − x ⇔ x 2 − 3 ​ x + 1 = 0 2x-x^{2}=1-x\Leftrightarrow x^{2}-3x+1=0 and g: ℕ → ℕ: n ↦ g ⁡ ( n) g\colon\mathbb{N}\to\mathbb{N}\colon n\mapsto g(n) be a function which is both o ⁡ ( n) o(n) and ω ⁡ ( n 0.5). \omega(n^{0.5}). In [7], the authors take g ⁡ ( n) ∼ n 2 / 3. g(n)\sim n^{2/3}. The family

 | ℱ = { A ⊂ [n]: | A | = ψ ​ n + g ⁡ ( n) ∨ | A | ≥ ( 1 − ψ) ​ n } = ( [n] ψ ​ n + g ⁡ ( n)) ∪ ( [n] ≥ ( 1 − ψ) ​ n) \mathcal{F}=\{A\subset[n]\colon\lvert A\rvert=\psi n+g(n)\vee\lvert A\rvert\geq(1-\psi)n\}\\ =\binom{[n]}{\psi n+g(n)}\cup\binom{[n]}{\geq(1-\psi)n} |  |

is an approximate union-closed family. That is, the union of two sets (iid, independent identically distributed, uniform random chosen) in ℱ \mathcal{F} belongs with high probability to ℱ \mathcal{F} as well. Nevertheless, since ψ > 1 3 \psi>\frac{1}{3}, one can also observe that ℱ ∪ ℱ = ( [n] ≥ ψ ​ n + g ⁡ ( n)) \mathcal{F}\cup\mathcal{F}=\binom{[n]}{\geq\psi n+g(n)}. That is, only a small proportion of ℱ ∪ ℱ \mathcal{F}\cup\mathcal{F} belongs to ℱ \mathcal{F}. As such, this construction, which might suggest that improving the constant ψ \psi is impossible with the entropy approach, does not necessarily imply this conclusion. If unions of two sets in ℱ \mathcal{F} are taken with a non-uniform measure or in a dependent manner such that sets with smaller unions are more likely to be selected, the initial argument about the sharpness of this construction no longer holds. The entropy of the union of two random variables, when these variables take values in ℱ \mathcal{F} in a dependent way, can indeed be larger. With the dependency proposed by Sawin, the union of two sets from the approximate union-closed family mentioned above will almost surely have a size of ( 0.5 + o ⁡ ( 1)) ​ n (0.5+o(1))n, for example.

### 2.3 Upper bound for Question 2 and limits on the approach of Sawin

Let h ⁡ ( x) = − x ​ log 2 ⁡ ( x) − ( 1 − x) ​ log 2 ⁡ ( 1 − x). h(x)=-x\log_{2}(x)-(1-x)\log_{2}(1-x). Let the roots of the function h ⁡ ( x) ​ ( 2 − h ⁡ ( x)) − h ⁡ ( 2 ​ x − x 2) h(x)(2-h(x))-h(2x-x^{2}) be 0 < b 1 < b 2 < 1. 0<b_{1}<b_{2}<1. Then b 1 ∼ 0.139499451909862 b_{1}\sim 0.139499451909862 and b 2 ∼ 0.329454738503037. b_{2}\sim 0.329454738503037. Choose b = b 2 b=b_{2} and a = 1 − h ⁡ ( b) 2 − h ⁡ ( b) ∼ 0.0788772927059232. a=\frac{1-h(b)}{2-h(b)}\sim 0.0788772927059232.

Let p, q, r p,q,r be three identically distributed [0, 1] [0,1] -valued random variables, where ℙ ⁡ ( p = 1) = a \,\mathbb{P}(p=1)=a and ℙ ⁡ ( p = b) = 1 − a, \,\mathbb{P}(p=b)=1-a, such that p p and q q are independent and p p and r r are as negatively correlated as possible in the sense that ℙ ⁡ ( p = r = 1) = 0. \,\mathbb{P}(p=r=1)=0. For these choices, we have 𝔼 ⁡ [p] = 0.382345533366703 \,\mathbb{E}[p]=0.382345533366703 4 4 4 The computation can be found in https://github.com/StijnCambie/UCconjecture/blob/main/Sharpness.sagews and ( 1 − a) 2 ​ h ​ ( 2 ​ b − b 2) = ( 1 − 2 ​ a) = ( 1 − a) ​ h ​ ( b) (1-a)^{2}h(2b-b^{2})=(1-2a)=(1-a)h(b) which is equivalent with

 | 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] = 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] = 𝔼 ⁡ [H ⁡ ( p)]. \,\mathbb{E}[H(p+q-pq)]=\,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]=\,\mathbb{E}[H(p)]. |  |

Hence no linear combination satisfies Equation 1 with a strict inequality and local perturbations (increasing a a) will result in counterexamples when c c is allowed to be slightly larger.

On a different note, we observe that taking a linear combination, as done in Equation 1, will be necessary to improve the constant 3 − 5 2 \frac{3-\sqrt{5}}{2} in the progress on the union-closed conjecture. To see this, observe that 𝔼 ⁡ [H ⁡ ( max ⁡ ( p, r, min ⁡ ( p + r, 1 / 2)))] < 𝔼 ⁡ [H ⁡ ( p)] \,\mathbb{E}\left[H(\max(p,r,\min(p+r,1/2)))\right]<\,\mathbb{E}[H(p)] for p p and r r identically distributed with ℙ ⁡ ( p = r = 1) = 0 \,\mathbb{P}(p=r=1)=0, ℙ ⁡ ( p = b) = 1 − a \,\mathbb{P}(p=b)=1-a, and ℙ ⁡ ( p = 1) = a \,\mathbb{P}(p=1)=a, where b = 1 4 b=\frac{1}{4} and a = 1 − h ⁡ ( b) 2 − h ⁡ ( b) + ϵ a=\frac{1-h(b)}{2-h(b)}+\epsilon for some small ϵ > 0 \epsilon>0. Since 𝔼 ⁡ [p] < 0.37 < 3 − 5 2 \,\mathbb{E}[p]<0.37<\frac{3-\sqrt{5}}{2}, considering the single term alone would not lead to an improvement.

From these observations, one can conclude that one cannot aim to prove the result with a constant better than 0.382345533366703 0.382345533366703 with the exact suggested approach of Sawin.

### 2.4 Summary of the proof

The idea from Sawin [20] is to sample sets twice element-wise. Here iteratively, one samples A ∩ [k] A\cap[k] and B ∩ [k] B\cap[k] for 0 ≤ k ≤ n 0\leq k\leq n based on the probability that a set in ℱ \mathcal{F}, given the intersection with [k] [k], would contain the additional element k + 1 k+1. The sampling of the element k + 1 k+1 for A A and B B can then be done in a dependent manner, ensuring that both A A and B B are uniform samples over ℱ. \mathcal{F}. Once some elements are sampled, control over the conditional probabilities (the distribution) is lost, so we assume the worst-case scenario. Since the worst-case scenarios for the two different strategies differ, a better bound is obtained by taking a linear combination of these two different ways of sampling in ℱ ∪ ℱ. \mathcal{F}\cup\mathcal{F}. As the entropy of the whole sample can be determined by summing (conditional) entropies for every element k ∈ [n] k\in[n], it is sufficient to prove the inequality for these entropies for for a single element. At this point, the problem reduces to a question that depends purely on the probability distribution of random variables and their expectations.

To attack that question, we perform local optimisation to find properties of an optimal distribution by redistributing the probability mass function and verifying convexity and concavity. As such, we reduce the problem to a simpler inequality involving only 4 4 unknown parameters associated with a probability distribution whose support contains at most 3 3 elements. Combining with the work of Yu [22], this is even further improved to two cases depending on two variables each. The final minimisation problems are verified numerically with a computer program in two ways, together with a plot showing that we obtain the global minimum by the proposed atomic probability distribution.

## 3 Proof for the optimal constant of Question 2

In this section, we prove that the maximum constant c c for Question 2 is approximately 0.382345533366 0.382345533366 (the value derived in Subsection 2.3). We do so by proving it for the optimal choice of α \alpha, α ∼ 0.0356069 \alpha\sim 0.0356069. The latter is obtained from comparing derivatives of the atomic solutions with support on { x, 1 } \{x,1\} and expectation c c around x = b x=b.

That is, the probability p p is given by ℙ ⁡ ( p = 1) = c − x 1 − x \,\mathbb{P}(p=1)=\frac{c-x}{1-x} and ℙ ⁡ ( p = x) = 1 − c − x 1 − x \,\mathbb{P}(p=x)=1-\frac{c-x}{1-x}. Remembering that p, r p,r are negatively correlated, we let

 | g 1 ​ ( x) \displaystyle g_{1}(x) | = 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] − 𝔼 ⁡ [H ⁡ ( p)] = ℙ ​ ( p = x) 2 ​ h ​ ( 2 ​ x − x 2) − ℙ ⁡ ( p = x) ​ h ​ ( x) ​ and \displaystyle=\,\mathbb{E}[H(p+q-pq)]-\,\mathbb{E}[H(p)]=\,\mathbb{P}(p=x)^{2}h(2x-x^{2})-\,\mathbb{P}(p=x)h(x)\mbox{ and } |  |

 | g 2 ​ ( x) \displaystyle g_{2}(x) | = 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] − 𝔼 ⁡ [H ⁡ ( p)] \displaystyle=\,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]-\,\mathbb{E}[H(p)] |  |

 |  | = ( 1 − 2 ​ ℙ ​ ( p = 1)) − ℙ ⁡ ( p = x) ​ h ​ ( x) \displaystyle=\left(1-2\,\mathbb{P}(p=1)\right)-\,\mathbb{P}(p=x)h(x) |  |

Then Eq. 1 is equivalent with ( 1 − α) ​ g 1 ​ ( x) + α ​ g 2 ​ ( x) ≥ 0 (1-\alpha)g_{1}(x)+\alpha g_{2}(x)\geq 0 and thus α \alpha need to satisfy ( 1 − α) ​ g 1 ′ ​ ( b) + α ​ g 2 ′ ​ ( b) = 0 (1-\alpha)g^{\prime}_{1}(b)+\alpha g^{\prime}_{2}(b)=0 or equivalently α = g 1 ′ ​ ( b) g 1 ′ ​ ( b) − g 2 ′ ​ ( b). \alpha=\frac{g^{\prime}_{1}(b)}{g^{\prime}_{1}(b)-g^{\prime}_{2}(b)}.

We first show that it suffices to consider the case where the probability distributions p, q, r p,q,r are not supported on ( 0.5, 1). (0.5,1). Next, by performing analytical computations on the behaviour of the functions in two intervals, similar to what Sawin [20] did, we reduce the problem to finding the minima of a continuous function in three variables on a bounded region, and subsequently to two variables. As such, the remaining problem is a minimisation problem for which the statement can be exactly verified with the help of a computer.

### 3.1 Reduction of support of the probability distribution

First we prove that it is sufficient to consider [0, 1] [0,1] -valued random variables which do not attain values in ( 0.5, 1). (0.5,1).

For readability and since it is sufficient to consider finite supported measures for the application on Conjecture 1, we prove the following lemmas only in the case of discrete probability distributions. The proof of the following lemma can be modified for general probability distributions by replacing sums by integrals and probability ℙ \,\mathbb{P} by probability distribution μ \mu.

###### Lemma 4.

Assume p, q p,q are independent identically distributed (iid) [0, 1] [0,1] -valued random variables with expectation 𝔼 ⁡ [p] = c ≤ 0.39 \,\mathbb{E}[p]=c\leq 0.39 such that ℙ ⁡ ( p = y) > 0 \,\mathbb{P}(p=y)>0 for some 1 / 2 < y < 1 1/2<y<1. Then the modified common probability distribution p ′, q ′ p^{\prime},q^{\prime} of p, q p,q for which ℙ ⁡ ( p ′ = 1) = ℙ ⁡ ( p = 1) + ( 2 ​ y − 1) ​ ℙ ​ ( p = y), ℙ ⁡ ( p ′ = y) = 0, ℙ ⁡ ( p ′ = 0.5) = ℙ ⁡ ( p = 0.5) + ( 2 − 2 ​ y) ​ ℙ ​ ( p = y) \,\mathbb{P}(p^{\prime}=1)=\,\mathbb{P}(p=1)+(2y-1)\,\mathbb{P}(p=y),\,\mathbb{P}(p^{\prime}=y)=0,\,\mathbb{P}(p^{\prime}=0.5)=\,\mathbb{P}(p=0.5)+(2-2y)\,\mathbb{P}(p=y) and ℙ ⁡ ( p ′ = y ′) = ℙ ⁡ ( p = y ′) \,\mathbb{P}(p^{\prime}=y^{\prime})=\,\mathbb{P}(p=y^{\prime}) for every y ′ ∈ [0, 1] \ { 0.5, y, 1 } y^{\prime}\in[0,1]\backslash\{0.5,y,1\} satisfies

- •

𝔼 ⁡ [p ′] = 𝔼 ⁡ [p] \,\mathbb{E}[p^{\prime}]=\,\mathbb{E}[p] and

- •

w ​ 𝔼 ​ [H ⁡ ( p ′)] − 𝔼 ⁡ [H ⁡ ( p ′ + q ′ − p ′ ​ q ′)] > w ​ 𝔼 ​ [H ⁡ ( p)] − 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] w\,\mathbb{E}[H(p^{\prime})]-\,\mathbb{E}[H(p^{\prime}+q^{\prime}-p^{\prime}q^{\prime})]>w\,\mathbb{E}[H(p)]-\,\mathbb{E}[H(p+q-pq)] for every w ≤ 1.044 w\leq 1.044, where p ′, q ′ p^{\prime},q^{\prime} are iid.

###### Proof.

The first part is immediate since the choice of redistribution is chosen in such a way that the following two linear combinations are true; ( 2 ​ y − 1) + ( 2 − 2 ​ y) ​ 0.5 = y (2y-1)+(2-2y)0.5=y and ( 2 ​ y − 1) + ( 2 − 2 ​ y) = 1 (2y-1)+(2-2y)=1. The latter to ensure that we still have a probability distribution. Hence it remains to prove the second part. For this, we first take a very small value ε = ℙ ⁡ ( p = y) N \varepsilon=\frac{\,\mathbb{P}(p=y)}{N} by choosing a large positive integer N N. Let I I be the support (set with all values x x for which ℙ ⁡ ( p = x) > 0 \,\mathbb{P}(p=x)>0) with 1 / 2 1/2 and 1 1 included as well.

First, we do the redistribution of only an ε \varepsilon -fraction in the probability distribution, that is ℙ ⁡ ( p ′ = 1) = ℙ ⁡ ( p = 1) + ( 2 ​ y − 1) ​ ε, ℙ ⁡ ( p ′ = y) = ℙ ⁡ ( p = y) − ε, ℙ ⁡ ( p ′ = 0.5) = ℙ ⁡ ( p = 0.5) + ( 2 − 2 ​ y) ​ ε. \,\mathbb{P}(p^{\prime}=1)=\,\mathbb{P}(p=1)+(2y-1)\varepsilon,\,\mathbb{P}(p^{\prime}=y)=\,\mathbb{P}(p=y)-\varepsilon,\,\mathbb{P}(p^{\prime}=0.5)=\,\mathbb{P}(p=0.5)+(2-2y)\varepsilon. Now 𝔼 ⁡ [H ⁡ ( p ′ + q ′ − p ′ ​ q ′)] − 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] \,\mathbb{E}[H(p^{\prime}+q^{\prime}-p^{\prime}q^{\prime})]-\,\mathbb{E}[H(p+q-pq)] is equal to ε ​ λ + O ⁡ ( ε 2) \varepsilon\lambda+O(\varepsilon^{2}), where λ \lambda equals

 | 2 ​ ∑ x ∈ I ( ( 2 − 2 ​ y) ​ h ​ ( 0.5 ​ ( 1 − x)) − h ⁡ ( ( 1 − y) ​ ( 1 − x))) ​ ℙ ​ ( p = x). \displaystyle 2\sum_{x\in I}\left((2-2y)h(0.5(1-x))-h((1-y)(1-x))\right)\,\mathbb{P}(p=x). |  |

Here we have used that h ⁡ ( x + y − x ​ y) = h ⁡ ( ( 1 − x) ​ ( 1 − y)) h(x+y-xy)=h((1-x)(1-y)) (by symmetry of h h and 1 − ( x + y − y ​ x) = ( 1 − x) ​ ( 1 − y) 1-(x+y-yx)=(1-x)(1-y)) and h ⁡ ( 0) = 0 h(0)=0. Let g ⁡ ( x) = ( 2 − 2 ​ y) ​ h ​ ( 0.5 ​ ( 1 − x)) − h ⁡ ( ( 1 − y) ​ ( 1 − x)). g(x)=(2-2y)h(0.5(1-x))-h((1-y)(1-x)). Note that

 | ln ⁡ 2 ​ d d ​ x ​ g ​ ( x) \displaystyle\ln 2\frac{d}{dx}g(x) | = ( y − 1) ​ ln ⁡ ( ( 1 − y) ​ ( 1 + x) x + y − x ​ y) > 0 ​ and \displaystyle=(y-1)\ln\left(\frac{(1-y)(1+x)}{x+y-xy}\right)>0\mbox{ and} |  |

 | ln ⁡ 2 ​ d 2 d ​ x 2 ​ g ​ ( x) \displaystyle\ln 2\frac{d^{2}}{dx^{2}}g(x) | = − ( 1 − y) ​ ( 2 ​ y − 1) ( x + 1) ​ ( x + y − x ​ y) < 0 \displaystyle=-\frac{(1-y)(2y-1)}{(x+1)(x+y-xy)}<0 |  |

since 0 < ( 1 − y) ​ ( 1 + x) < x + y − x ​ y 0<(1-y)(1+x)<x+y-xy for 1 > y > 0.5 1>y>0.5 and every 1 ≥ x ≥ 0. 1\geq x\geq 0. Due to Jensen’s inequality for the concave function g g, λ = 2 ​ 𝔼 ​ [g ⁡ ( p)] \lambda=2\,\mathbb{E}[g(p)] is upper bounded by 2 ​ g ​ ( c). 2g(c). This upper bound is independent of ℙ ⁡ ( p = y). \,\mathbb{P}(p=y). Hence we can do this N N times and conclude that for p ′, q ′ p^{\prime},q^{\prime} distributed as in the lemma, we have 𝔼 ⁡ [H ⁡ ( p ′ + q ′ − p ′ ​ q ′)] − 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] ≤ 2 ​ g ​ ( c) ​ ℙ ​ ( p = y) + O ⁡ ( ε). \,\mathbb{E}[H(p^{\prime}+q^{\prime}-p^{\prime}q^{\prime})]-\,\mathbb{E}[H(p+q-pq)]\leq 2g(c)\,\mathbb{P}(p=y)+O(\varepsilon). It is also straightforward to compute that 𝔼 ⁡ [H ⁡ ( p)] − 𝔼 ⁡ [H ⁡ ( p ′)] = ℙ ⁡ ( p = y) ​ ( h ⁡ ( y) − ( 2 − 2 ​ y) ​ h ​ ( 0.5)) = − g ⁡ ( 0) ​ ℙ ​ ( p = y). \,\mathbb{E}[H(p)]-\,\mathbb{E}[H(p^{\prime})]=\,\mathbb{P}(p=y)\left(h(y)-(2-2y)h(0.5)\right)=-g(0)\,\mathbb{P}(p=y). Finally, it suffices to prove that

 | 2 ​ g ​ ( c) − g ⁡ ( 0) < 0 2g(c)-g(0)<0 |  |

since then ε \varepsilon can be chosen sufficiently small such that after adding the O ⁡ ( ε) O(\varepsilon) term, it is still negative. Since g g is an increasing function and g ⁡ ( 0) < 0 g(0)<0 (due to h h being concave), it suffices to prove that 2 ​ g ​ ( 0.39) − 1.044 ​ g ​ ( 0) < 0. 2g(0.39)-1.044g(0)<0. This is the case for every 1 2 < y < 1. \frac{1}{2}<y<1. 5 5 5 Verification at https://github.com/StijnCambie/UCconjecture/blob/main/reduction\_UC.sagews ∎

###### Lemma 5.

Let p, r p,r be identically distributed [0, 1] [0,1] -valued random variables, not necessarily independent. Then one can modify the underlying common probability distribution by distributing the probability mass function on ( 0.5, 1) (0.5,1) over 0.5 0.5 and 1 1 such that 𝔼 ⁡ [p] \,\mathbb{E}[p] is the same and

 | 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p ′, r ′, min ⁡ ( p ′ + r ′, 1 / 2)))] ≤ 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))]. \,\mathbb{E}\left[H\left(max\left(p^{\prime},r^{\prime},\min\left(p^{\prime}+r^{\prime},1/2\right)\right)\right)\right]\leq\,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]. |  |

###### Proof.

We do the following procedure as long as there is some value in ( 0, 1) (0,1) with positive probability. Let y = max ⁡ { y ∣ 0.5 < y < 1 ∧ ℙ ⁡ ( p = y) > 0 } y=\max\{y\mid 0.5<y<1\wedge\,\mathbb{P}(p=y)>0\} be the largest value in ( 0, 1) (0,1) with positive probability and y ′ y^{\prime} the second largest such value, or 0.5 0.5 if no other value in ( 0, 1) (0,1) has positive probability. We distribute the probability mass function of y y over y ′ y^{\prime} and 1 1 (such that we still end with a probability measure). We let p ′ p^{\prime} and r ′ r^{\prime} be dependent as before, with the corresponding distribution taken into account (made clear below). We claim that the considered quantity 𝔼 ⁡ [H ⁡ ( max ⁡ ( p, r, min ⁡ ( p + r, 1 / 2)))] \,\mathbb{E}\left[H\left(\max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right] did not increase by doing so. If ℙ ⁡ ( p = y, r = y) > 0 \,\mathbb{P}(p=y,r=y)>0, we increase ℙ ⁡ ( p = y ′, r = y ′) \,\mathbb{P}(p=y^{\prime},r=y^{\prime}) and ℙ ⁡ ( p = 1, r = 1) \,\mathbb{P}(p=1,r=1) accordingly and conclude by concavity of h h. If ℙ ⁡ ( p = y, r = 1) > 0 \,\mathbb{P}(p=y,r=1)>0, then max ⁡ { p, r, min ⁡ ( p + r, 1 / 2) } = 1 \max\{p,r,\min(p+r,1/2)\}=1 both before and after the local adaptation of p p (similarly when p p and r r are switched) and so there is no change by this term. If ℙ ⁡ ( p = y, r = z) > 0 \,\mathbb{P}(p=y,r=z)>0, for some z ≤ y ′ z\leq y^{\prime}, then we conclude again by concavity of h. h. By iterating this process, the probability measure on ( 0.5, 1) (0.5,1) is distributed over 0.5 0.5 and 1 1 and the condition in the lemma is satisfied. ∎

Now, assume there are random variables p, q, r p,q,r satisfying the conditions of Question 2 for which 𝔼 ⁡ [H ⁡ ( p)] ≤ c \,\mathbb{E}[H(p)]\leq c and ( 1 − α) ​ 𝔼 ​ [H ⁡ ( p + q − p ​ q)] + α ​ 𝔼 ​ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] ≤ 𝔼 ⁡ [H ⁡ ( p)] (1-\alpha)\,\mathbb{E}[H(p+q-pq)]+\alpha\,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]\leq\,\mathbb{E}[H(p)] for some α ∈ [0, 1]. \alpha\in[0,1]. Next, we consider the modified random variables p ′, q ′, r ′ p^{\prime},q^{\prime},r^{\prime}, where the probability distribution is iteratively adapted by distributing the probability ℙ ⁡ ( p = y) \,\mathbb{P}(p=y) for some 0.5 < y < 1 0.5<y<1 over ℙ ⁡ ( p = 0.5) \,\mathbb{P}(p=0.5) and ℙ ⁡ ( p = 1) \,\mathbb{P}(p=1). Since 1.044 > 1 1 − α, 1.044>\frac{1}{1-\alpha}, Lemma 4 implies that 𝔼 ⁡ [H ⁡ ( p ′)] − ( 1 − α) ​ 𝔼 ​ [H ⁡ ( p ′ + q ′ − p ′ ​ q ′)] > 𝔼 ⁡ [H ⁡ ( p)] − ( 1 − α) ​ 𝔼 ​ [H ⁡ ( p + q − p ​ q)] \,\mathbb{E}[H(p^{\prime})]-(1-\alpha)\,\mathbb{E}[H(p^{\prime}+q^{\prime}-p^{\prime}q^{\prime})]>\,\mathbb{E}[H(p)]-(1-\alpha)\,\mathbb{E}[H(p+q-pq)]. Also 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p ′, r ′, min ⁡ ( p ′ + r ′, 1 / 2)))] ≤ 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] \,\mathbb{E}\left[H\left(max\left(p^{\prime},r^{\prime},\min\left(p^{\prime}+r^{\prime},1/2\right)\right)\right)\right]\leq\,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right] for the natural choice of the adapted dependency of p p and r r by Lemma 5. Thus, if there are probability distributions p, q p,q and r r for which Equation 1 is not satisfied for some value of c c, then these distributions must have support disjoint from ( 0.5, 1) (0.5,1).

### 3.2 Reduction to small support of the probability distribution

In the previous subsection, we established that for 2, it is sufficient to consider probability distributions whose support does not include values in ( 0.5, 1) (0.5,1), and we now further restrict the support to at most three elements.

First, we observe that the quantity 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] \,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right] is minimised (under the condition that p p and r r have the same fixed distribution) when ℙ ⁡ ( p = r = 1) = 0 \,\mathbb{P}(p=r=1)=0. If ℙ ⁡ ( p = r = 1) \,\mathbb{P}(p=r=1) and ℙ ⁡ ( p = x, r = y) > ϵ > 0 \,\mathbb{P}(p=x,r=y)>\epsilon>0 for some values 0 < max ⁡ x, y < 1 0<\max{x,y}<1, we modify the probability distribution by increasing ℙ ⁡ ( p = x, r = 1) \,\mathbb{P}(p=x,r=1) and ℙ ⁡ ( p = 1, r = y) \,\mathbb{P}(p=1,r=y) by ϵ \epsilon, and decreasing ℙ ⁡ ( p = r = 1) \,\mathbb{P}(p=r=1) and ℙ ⁡ ( p = x, r = y) \,\mathbb{P}(p=x,r=y) by ϵ \epsilon. This decreases the expectation of the entropy function 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] \,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]. Note that in the remaining case ℙ ⁡ ( p = r = 0) \,\mathbb{P}(p=r=0) would be the only other positive probability and so the whole expectation 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] = ℙ ⁡ ( p = r = 0) ​ h ​ ( 0) + ℙ ⁡ ( p = r = 1) ​ h ​ ( 1) \,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]=\,\mathbb{P}(p=r=0)h(0)+\,\mathbb{P}(p=r=1)h(1) is zero. Similarly, we can make analogous modifications, decreasing ℙ ⁡ ( p = r = 1) \,\mathbb{P}(p=r=1) and ℙ ⁡ ( p = 0, r = 0) \,\mathbb{P}(p=0,r=0) with ε = ℙ ⁡ ( p = r = 1) \varepsilon=\,\mathbb{P}(p=r=1) and increasing ℙ ⁡ ( p = 0, r = 1) \,\mathbb{P}(p=0,r=1) and ℙ ⁡ ( p = 1, r = 0) \,\mathbb{P}(p=1,r=0) with ε \varepsilon. The latter is possible since we assumed ℙ ⁡ ( p = 1) ≤ 1 2. \,\mathbb{P}(p=1)\leq\frac{1}{2}. Thus, without loss of generality, we may assume that ℙ ⁡ ( p = r = 1) = 0 \,\mathbb{P}(p=r=1)=0.

Now, by the result of the previous subsection, Section 3.1, whenever p, r < 1, p,r<1, we have p, r ≤ 1 2 p,r\leq\frac{1}{2} and hence m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)) = min ⁡ ( p + r, 1 / 2). max\left(p,r,\min\left(p+r,1/2\right)\right)=\min\left(p+r,1/2\right).

For the remainder of this subsection, let ℙ ⁡ ( p = 1) = a \,\mathbb{P}(p=1)=a. Define x 0 x_{0} as the ( 1 − 2 ​ a) (1-2a) -quantile of p p, i.e., the smallest value satisfying ℙ ⁡ ( p ≤ x 0) ≥ 1 − 2 ​ a. \,\mathbb{P}(p\leq x_{0})\geq 1-2a.

###### Lemma 6.

We can assume that ℙ ⁡ ( p = r) = 1 − 2 ​ a \,\mathbb{P}(p=r)=1-2a and this happens exactly for the ( 1 − 2 ​ a) (1-2a) -quantile x 0 x_{0}, that is, for every x < x 0, x<x_{0}, we have ℙ ⁡ ( p = r = x) = ℙ ⁡ ( p = x) \,\mathbb{P}(p=r=x)=\,\mathbb{P}(p=x) and ℙ ⁡ ( p = r = x 0) = 1 − 2 ​ a − ℙ ⁡ ( p < x 0). \,\mathbb{P}(p=r=x_{0})=1-2a-\,\mathbb{P}(p<x_{0}).

###### Proof.

To prove the statement, we show that probability mass can be redistributed without increasing the studied expectation.

Since h h is an increasing function on [0, 1 / 2] [0,1/2], we can assume that the values x, y ∈ [0, 1 / 2] x,y\in[0,1/2] for which ℙ ⁡ ( p = x, r = y) > 0 \,\mathbb{P}(p=x,r=y)>0 satisfy x, y ≤ x 0 x,y\leq x_{0}. In particular, for x 0 < x ≤ 1 / 2 x_{0}<x\leq 1/2 and y 0 < y ≤ 1 / 2 y_{0}<y\leq 1/2, we have the following condition: if ℙ ⁡ ( p = x, r = z) > 0 \,\mathbb{P}(p=x,r=z)>0 or ℙ ⁡ ( p = z, r = y) > 0 \,\mathbb{P}(p=z,r=y)>0, then z = 1 z=1. This cancels the largest values in [0, 1 / 2] [0,1/2], as their combination with 1 1 results in a contribution of 0 0 due to h ⁡ ( 1) = 0 h(1)=0.

If ℙ ⁡ ( p = x, r = y), ℙ ⁡ ( p = x ′, r = y ′) ≥ ε > 0, \,\mathbb{P}(p=x,r=y),\,\mathbb{P}(p=x^{\prime},r=y^{\prime})\geq\varepsilon>0, where x < x ′ < x 0 ≤ 1 / 2 x<x^{\prime}<x_{0}\leq 1/2 and 1 / 2 ≥ x 0 ≥ y > y ′ 1/2\geq x_{0}\geq y>y^{\prime}, we can decrease ℙ ⁡ ( p = x, r = y) \,\mathbb{P}(p=x,r=y) and ℙ ⁡ ( p = x ′, r = y ′) \,\mathbb{P}(p=x^{\prime},r=y^{\prime}) with ε \varepsilon and increase ℙ ⁡ ( p = x, r = y ′), ℙ ⁡ ( p = x ′, r = y) \,\mathbb{P}(p=x,r=y^{\prime}),\,\mathbb{P}(p=x^{\prime},r=y) with ε. \varepsilon. The studied expectation does not increase, by the follow claim.

###### Claim 7.

The function g: [0, 1] → [0, 1]: x ↦ h ⁡ ( m ​ i ​ n ​ ( x, 1 / 2)) g\colon[0,1]\to[0,1]\colon x\mapsto h(min(x,1/2)) is a concave function. For all x, x ′, y, y ′ ∈ [0, 1 / 2] x,x^{\prime},y,y^{\prime}\in[0,1/2] such that x < x ′ x<x^{\prime} and y > y ′ y>y^{\prime}, we have g ⁡ ( x + y) + g ⁡ ( x ′ + y ′) ≥ g ⁡ ( x + y ′) + g ⁡ ( x ′ + y). g(x+y)+g(x^{\prime}+y^{\prime})\geq g(x+y^{\prime})+g(x^{\prime}+y).

###### Proof.

The second derivative of g g equals that one of h h on [0, 1 / 2) [0,1/2) and is therefore strictly negative on this interval. The second derivative of g g is zero for x ≥ 1 / 2. x\geq 1/2.

Since ( x + y) + ( x ′ + y ′) = ( x + y ′) + ( x ′ + y) (x+y)+(x^{\prime}+y^{\prime})=(x+y^{\prime})+(x^{\prime}+y) and x + y ′ < min ⁡ { x + y, x ′ + y ′ } x+y^{\prime}<\min\{x+y,x^{\prime}+y^{\prime}\} and max ⁡ { x + y, x ′ + y ′ } < x ′ + y, \max\{x+y,x^{\prime}+y^{\prime}\}<x^{\prime}+y, the pair { x ′ + y, x + y ′ } \{x^{\prime}+y,x+y^{\prime}\} majorises { x + y, x ′ + y ′ }. \{x+y,x^{\prime}+y^{\prime}\}. The claim now follows from Karamata’s inequality [14]. ∎

We conclude that we can assume that ℙ ⁡ ( p = r) = 1 − 2 ​ a \,\mathbb{P}(p=r)=1-2a and this happens exactly for the ( 1 − 2 ​ a) (1-2a) -quantile, that is, for every x < x 0, x<x_{0}, we have ℙ ⁡ ( p = r = x) = ℙ ⁡ ( p = x) \,\mathbb{P}(p=r=x)=\,\mathbb{P}(p=x) and ℙ ⁡ ( p = r = x 0) = 1 − 2 ​ a − ℙ ⁡ ( p < x 0). \,\mathbb{P}(p=r=x_{0})=1-2a-\,\mathbb{P}(p<x_{0}). ∎

Next, we use the same approach as Sawin. Let μ \mu be a probability distribution which minimises

 | H μ = ( 1 − α) ​ 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] + α ​ 𝔼 p ∼ μ ′ ​ [H ⁡ ( min ⁡ ( 2 ​ p, 1 / 2))] − 𝔼 p ∼ μ ​ [H ⁡ ( p)] H_{\mu}=(1-\alpha)\,\mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]+\alpha\,\mathbb{E}^{\prime}_{p\sim\mu}\left[H\left(\min\left(2p,1/2\right)\right)\right]-\,\mathbb{E}_{p\sim\mu}[H(p)] |  | (2) |

among all probability distributions with expectation bounded by c c; 𝔼 p ∼ μ ​ [H ⁡ ( p)] ≤ c. \,\mathbb{E}_{p\sim\mu}[H(p)]\leq c. Let ℙ p ∼ μ ​ ( p = 1) = a \,\mathbb{P}_{p\sim\mu}(p=1)=a and let the ( 1 − 2 ​ a) (1-2a) -quantile of μ \mu be x 0 x_{0}. Such a distribution exists, as explained in the proof of Sawin’s Lemma 3. Here 𝔼 ′ \,\mathbb{E}^{\prime} has to be interpreted as the expectation over the ( 1 − 2 ​ a) (1-2a) -quantile (due to Lemma 6).

###### Lemma 8.

The probability distribution μ \mu also minimises

 | 2 ​ ( 1 − α) ​ 𝔼 ( p, q) ∼ μ × ν ​ [H ⁡ ( p + q − p ​ q)] − 𝔼 p ∼ ν ​ H ​ [p] + α ​ 𝔼 p ∼ ν ′ ​ [H ⁡ ( min ⁡ ( 2 ​ p, 1 / 2))] \displaystyle 2(1-\alpha)\,\mathbb{E}_{(p,q)\sim\mu\times\nu}[H(p+q-pq)]-\,\mathbb{E}_{p\sim\nu}H[p]+\alpha\,\mathbb{E}^{\prime}_{p\sim\nu}\left[H\left(\min\left(2p,1/2\right)\right)\right] |  |

 | = 𝔼 q ∼ ν ​ ( 2 ​ ( 1 − α) ​ 𝔼 p ∼ μ ​ [H ⁡ ( p + q − p ​ q)] − H ⁡ ( q)) + 𝔼 q ∼ ν ′ ​ [H ⁡ ( min ⁡ ( 2 ​ q, 1 / 2))] \displaystyle=\,\mathbb{E}_{q\sim\nu}\left(2(1-\alpha)\,\mathbb{E}_{p\sim\mu}[H(p+q-pq)]-H(q)\right)+\,\mathbb{E}^{\prime}_{q\sim\nu}\left[H\left(\min\left(2q,1/2\right)\right)\right] |  |

among all probability measures ν \nu for which the ( 1 − 2 ​ a) (1-2a) -quantile is x 0 x_{0}, 𝔼 p ∼ ν ​ H ​ [p] ≤ c \,\mathbb{E}_{p\sim\nu}H[p]\leq c and ℙ p ∼ ν ​ ( p = 1) = a \,\mathbb{P}_{p\sim\nu}(p=1)=a.

###### Proof.

Consider the combination μ ′ = ( 1 − ε) ​ μ + ε ​ ν \mu^{\prime}=(1-\varepsilon)\mu+\varepsilon\nu, which has the same values for x 0 x_{0} and a = ℙ ⁡ ( p = 1) a=\,\mathbb{P}(p=1). By definition of μ \mu being a minimiser, H μ ′ − H μ ≥ 0 H_{\mu^{\prime}}-H_{\mu}\geq 0. Now H μ ′ − H μ ε \frac{H_{\mu^{\prime}}-H_{\mu}}{\varepsilon} equals, up to a O ⁡ ( ε) O(\varepsilon) function,

 |  | 2 ​ ( 1 − α) ​ ( ( 𝔼 ( p, q) ∼ μ × ν − 𝔼 ( p, q) ∼ μ × μ) ​ [H ⁡ ( p + q − p ​ q)]) − ( 𝔼 p ∼ ν − 𝔼 p ∼ μ) ​ [H ⁡ ( p)] \displaystyle 2(1-\alpha)\left(\left(\,\mathbb{E}_{(p,q)\sim\mu\times\nu}-\,\mathbb{E}_{(p,q)\sim\mu\times\mu}\right)[H(p+q-pq)]\right)-(\,\mathbb{E}_{p\sim\nu}-\,\mathbb{E}_{p\sim\mu})[H(p)] |  |

 |  | + α ⁡ ( ( 𝔼 p ∼ ν ′ − 𝔼 p ∼ μ ′) ​ [H ⁡ ( min ⁡ ( 2 ​ p, 1 / 2))]). \displaystyle+\alpha\left((\,\mathbb{E}^{\prime}_{p\sim\nu}-\,\mathbb{E}^{\prime}_{p\sim\mu})\left[H\left(\min\left(2p,1/2\right)\right)\right]\right). |  |

So by taking ε \varepsilon sufficiently small, we conclude. ∎

Now for every fixed constant 0 ≤ q ≤ 1, 0\leq q\leq 1, the function F μ ​ ( q) = 𝔼 p ∼ μ ​ [2 ​ ( 1 − α) ​ H ​ ( p + q − p ​ q) − h ⁡ ( q)] F_{\mu}(q)=\,\mathbb{E}_{p\sim\mu}[2(1-\alpha)H(p+q-pq)-h(q)] satisfies d d ​ q ​ ( q ⁡ ( 1 − q) ​ d 2 d ​ q 2 ​ F μ ​ ( q)) < 0 \frac{d}{dq}\left(q(1-q)\frac{d^{2}}{dq^{2}}F_{\mu}(q)\right)<0, as verified in the proof of [20, Lem. 3]. By direct computation, we verify that ln ⁡ 2 ​ d 2 d ​ q 2 ​ h ​ ( 2 ​ q) = − 2 ​ ( 1 − q) ( 1 − 2 ​ q) \ln 2\frac{d^{2}}{dq^{2}}h\left(2q\right)=\frac{-2(1-q)}{(1-2q)} and d d ​ q ​ ( q ⁡ ( 1 − q) ​ ln ⁡ 2 ​ d 2 d ​ q 2 ​ h ​ ( 2 ​ q)) = d d ​ q ​ ( − 2 ( 1 − 2 ​ q) ​ q) = − 2 ( 1 − 2 ​ q) 2 < 0. \frac{d}{dq}\left(q(1-q)\ln 2\frac{d^{2}}{dq^{2}}h\left(2q\right)\right)=\frac{d}{dq}\left(\frac{-2}{(1-2q)q}\right)=\frac{-2}{(1-2q)^{2}}<0. Hence q ⁡ ( 1 − q) ​ ln ⁡ 2 ​ d 2 d ​ q 2 ​ ( F μ ​ ( q) + h ⁡ ( 2 ​ q)) q(1-q)\ln 2\frac{d^{2}}{dq^{2}}\left(F_{\mu}(q)+h\left(2q\right)\right) is a strictly decreasing function. This implies that if we consider the function F μ ​ ( q) + h ​ ( 2 ​ q) F_{\mu}(q)+h\left(2q\right) on the interval I 1 = [0, m ​ i ​ n ​ { x 0, 1 / 4 }] I_{1}=[0,min\{x_{0},1/4\}] and F μ ​ ( q) F_{\mu}(q) on the interval I 2 = [m ​ i ​ n ​ { x 0, 1 / 4 }, 1 / 2] I_{2}=[min\{x_{0},1/4\},1/2] separately, we observe that the second derivative of each function behaves in one of three ways: it is either strictly positive, strictly negative, or changes sign at a critical point z 1 z_{1} or z 2 z_{2}.

I.e., F μ ​ ( q) + H ​ ( 2 ​ q) F_{\mu}(q)+H\left(2q\right) is either strictly convex on one part of I 1 I_{1} (which is of the form [0, z 1] [0,z_{1}] and strictly concave at the other part ( [z 1, m ​ i ​ n ​ { x 0, 1 / 4 }] [z_{1},min\{x_{0},1/4\}]), convex on the whole interval, or concave on all of I 1. I_{1}. Similarly F μ ​ ( q) F_{\mu}(q) is either strictly convex on one part of I 2 I_{2}, [m ​ i ​ n ​ { x 0, 1 / 4 }, z 2] [min\{x_{0},1/4\},z_{2}], and strictly concave at the remaining part, [z 2, 1] [z_{2},1], convex on all of I 2 I_{2}, or concave on the whole interval I 2 I_{2}.

On each interval (so for both I 1 I_{1} and I 2 I_{2}), the minimum is attained by a probability distribution that either has only one value with positive probability (if the studied function is convex), or two, one of them being the maximum of the interval. When the latter occurs on I 2 I_{2}, one can extend I 2 I_{2} to [min ⁡ { x 0, 1 / 4 }, 1] [\min\{x_{0},1/4\},1] and redistribute the mass from 1 / 2 1/2 over 1 1 and the inflection point z 2 z_{2} of I 2 I_{2} and repeat as before. Increasing the probability mass of 1 1 even further decreases 𝔼 p ∼ μ ′ ​ [H ⁡ ( min ⁡ ( 2 ​ p, 1 / 2))] \,\mathbb{E}^{\prime}_{p\sim\mu}[H(\min(2p,1/2))], so the latter distribution was not a minimising probability distribution in Lemma 8.

This results into candidate probability distributions with at most 4 4 different values with positive mass.

In total there are 3 2 = 9 3^{2}=9 combinations (which one can double based on x 0 < 1 / 4 x_{0}<1/4 and x 0 ≥ 1 / 4 x_{0}\geq 1/4, but each such pair works by the same ideas) to consider for the behaviour on the two intervals. The 3 combinations where the considered function on I 1 I_{1} is convex are almost immediate. In the other situations we can modify the probability measure even further in steps and conclude at the end that a probability distribution that is a solution in Lemma 8 has at most 3 3 values with positive mass.

If m ​ i ​ n ​ { x 0, 1 / 4 } = x 0 min\{x_{0},1/4\}=x_{0} has positive probability on the first interval and this is different from the (smallest) value y 0 y_{0} on the second interval that got positive probability, one can repeat the argument by replacing x 0 x_{0} by min ⁡ { y 0, 1 / 4 }. \min\{y_{0},1/4\}. This implies that in case there are 4 4 values with positive probability, the values 1 1 and 1 4 \frac{1}{4} are among them. But when we would have x 0 ≥ 1 4, x_{0}\geq\frac{1}{4}, we know that 𝔼 ′ [H ( min { 2 p, 1 / 2 }) \,\mathbb{E}^{\prime}[H(\min\{2p,1/2\}) does not depend on the distribution on the interval [1 / 4, 1] [1/4,1] and as such, we can repeat the argument about the extremum for F μ ​ ( q) F_{\mu}(q). At the end, we conclude that the support has no more than 3 3 elements with positive probability. Furthermore, if the support contains exactly 3 3 elements with positive probability, at least one of them is at most 1 / 4. 1/4.

We illustrate this for an example where the function F μ ​ ( q) + H ​ ( 2 ​ q) F_{\mu}(q)+H\left(2q\right) on I 1 ⊊ [0, 1 / 4] I_{1}\subsetneq[0,1/4] is both convex and concave (there is an inflection point z 1 ∈ I 1 z_{1}\in I_{1}), y 0 > 1 / 4 y_{0}>1/4 and F μ ​ ( q) F_{\mu}(q) is convex (convex and concave works similar) on [x 0, 1 / 2] [x_{0},1/2], in Fig. 1. Here the red dots represent the values ( q, f ⁡ ( q)) (q,f(q)), where f ⁡ ( q) = F μ ​ ( q) + H ⁡ ( 2 ​ q) ​ 1 q ≤ m ​ i ​ n ​ { x 0, 1 / 4 } f(q)=F_{\mu}(q)+H\left(2q\right)1_{q\leq min\{x_{0},1/4\}}, for those q q that have a positive probability under the candidate probability measure μ \mu.

First we extend I 1 = [0, x 0] I_{1}=[0,x_{0}] to [0, min ⁡ { y 0, 1 / 4 }] [0,\min\{y_{0},1/4\}] and redistribute the mass. We redefine I 1 I_{1} and I 2 I_{2} and redistribute the mass on [1 / 4, 1] [1/4,1] (here it is within [1 / 4, 1 / 2] [1/4,1/2]), to end with a candidate probability distribution for Lemma 8 which has less than 4 4 values with positive probability.

x x y y 1 1 1 / 2 1/2 1 / 4 1/4

x x y y 1 1 1 / 2 1/2 1 / 4 1/4

x x y y 1 1 1 / 2 1/2 1 / 4 1/4

x x y y 1 1 1 / 2 1/2 1 / 4 1/4

Figure 1: An example of improving the distribution

### 3.3 Verification for distributions with support of size at most 3 3

Once the support is reduced to 3 3 elements, { a 1, a 2, 1 } \{a_{1},a_{2},1\}, by knowing the associated probabilities p 1, p 2, 1 − p 1 − p 2 p_{1},p_{2},1-p_{1}-p_{2} of each element, the inequality in Question 2 can be checked. As such, we find an optimisation problem in 4 4 variables. Using Maple, it has been checked in multiple ways; by solving a minimisation problem in multiple regimes, and by plotting an implicit plot, as well as plots with a fixed choice for a 1 a_{1} assuming 𝔼 ⁡ [p] = c \,\mathbb{E}[p]=c. From these, we note that there are two local regions where the minima occur; around a 1 = 0 a_{1}=0 and around p 1 = 0 p_{1}=0 6 6 6 See https://github.com/StijnCambie/UCconjecture, documents FinalComputation23, corresponding with the cases where p p is { 0, 1 } \{0,1\} -valued and the atomic one used to show sharpness in Subsection 2.3.

Finally, we also give a more rigorous proof for the case where the distribution is atomic, i.e., ℙ ⁡ ( p = b) = 1 − a \,\mathbb{P}(p=b)=1-a and ℙ ⁡ ( p = 1) = a \,\mathbb{P}(p=1)=a and 𝔼 ⁡ [p] = a + ( 1 − a) ​ b ≤ c \,\mathbb{E}[p]=a+(1-a)b\leq c, where c ∼ 0.3823455 c\sim 0.3823455 is the claimed optimum. Then 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] = ( 1 − a) 2 ​ h ​ ( 2 ​ b − b 2), 𝔼 ⁡ [H ⁡ ( p)] = ( 1 − a) ​ h ​ ( b) \,\mathbb{E}[H(p+q-pq)]=(1-a)^{2}h(2b-b^{2}),\,\mathbb{E}[H(p)]=(1-a)h(b) and 𝔼 ⁡ [H ⁡ ( m ​ a ​ x ​ ( p, r, min ⁡ ( p + r, 1 / 2)))] ≥ ( 1 − 2 ​ a) ​ h ​ ( min ⁡ ( 2 ​ b, 1 / 2)). \,\mathbb{E}\left[H\left(max\left(p,r,\min\left(p+r,1/2\right)\right)\right)\right]\geq(1-2a)h(\min(2b,1/2)). Since the case where ℙ ⁡ ( p = r = 1) = 0 \,\mathbb{P}(p=r=1)=0 is the worst case, we need to show that

 | ( 1 − α) ​ ( 1 − a) 2 ​ h ​ ( 2 ​ b − b 2) + α ⁡ ( 1 − 2 ​ a) ​ h ​ ( min ⁡ ( 2 ​ b, 1 / 2)) − ( 1 − a) ​ h ​ ( b) ≥ 0, or equivalently (1-\alpha)(1-a)^{2}h(2b-b^{2})+\alpha(1-2a)h(\min(2b,1/2))-(1-a)h(b)\geq 0,\mbox{ or equivalently} |  |

 | ( 1 − α) ​ h ​ ( 2 ​ b − b 2) ​ a 2 + ( − 2 ​ ( 1 − α) ​ h ​ ( 2 ​ b − b 2) − 2 ​ α ​ h ​ ( min ⁡ ( 2 ​ b, 1 / 2)) + h ⁡ ( b)) ​ a + O b, α ​ ( 1) ≥ 0 (1-\alpha)h(2b-b^{2})a^{2}+\left(-2(1-\alpha)h(2b-b^{2})-2\alpha h(\min(2b,1/2))+h(b)\right)a+O_{b,\alpha}(1)\geq 0 |  |

For fixed (non-zero) b b, this is a quadratic function in a a with positive leading coefficient, which attains its minimum at a = 1 + 2 ​ α ​ h ​ ( min ⁡ ( 2 ​ b, 1 / 2)) − h ⁡ ( b) 2 ​ ( 1 − α) ​ h ​ ( 2 ​ b − b 2) > c − b 1 − b a=1+\frac{2\alpha h(\min(2b,1/2))-h(b)}{2(1-\alpha)h(2b-b^{2})}>\frac{c-b}{1-b} and thus it is sufficient to prove this in the case where a = c − b 1 − b. a=\frac{c-b}{1-b}. 7 7 7 See https://github.com/StijnCambie/UCconjecture/blob/main/Sharpness.sagews

### 3.4 Precise verification

If we combine our conclusions from Subsections 3.2 and 3.1 with the one from [22], we obtain that there are two possible forms for the joint distribution of ( p, r). (p,r). Either p = r p=r and the support of p p has size bounded by 2 2 (the elements being bounded by 1 / 2 1/2), or the support has 3 3 elements { a 1, a 2, 1 } \{a_{1},a_{2},1\} and p 1 = 1 − 2 ​ p 2 p_{1}=1-2p_{2}, where ℙ ⁡ ( p = a 2, r = 1) = ℙ ⁡ ( p = 1, r = a 2) = p 2 \,\mathbb{P}(p=a_{2},r=1)=\,\mathbb{P}(p=1,r=a_{2})=p_{2}. Equivalently, with the notation of [22], the distribution P p ​ r P_{pr} is of the form ( 1 − β) ​ Q a, a + β ​ Q b, b (1-\beta)Q_{a,a}+\beta Q_{b,b} or ( 1 − β) ​ Q a, a + β ​ Q 1, b (1-\beta)Q_{a,a}+\beta Q_{1,b} (where a ≤ b a\leq b).

Hereby for a fixed choice of c c, β \beta is a function of a a and b. b. In the first case, a < c < b a<c<b and β = c − a b − a \beta=\frac{c-a}{b-a}. In the second case, β = 2 ​ ( c − a) 1 + b − 2 ​ a. \beta=\frac{2(c-a)}{1+b-2a}.

As such, the final verification for 2 can be deduced from an inequality involving only two variables. This final verification has been done in https://github.com/StijnCambie/UCconjecture, documents FinalComputation24 8 8 8 For some reason, minus is replaced by K K in the PDF., If p = r p=r, the inequality is strict. In the case with the support containing 1 1, we deduce that the atomic distribution from Section 2.3 is the (unique) minimiser, and the inequality is true and tight.

## 4 Proof of bound for sharper union-closed conjecture

Having established the answer to 2 in the previous section, we now present the formal proof of Theorem 3, as sketched in [20], to complete the exposition Let α ∼ 0.0356069 \alpha\sim 0.0356069 and c ∼ 0.3823455 c\sim 0.3823455 be the previously determined optimal constants for Question 2.

###### Proof of Theorem 3.

Assume there is a (nonempty) union-closed family ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]} for which every element i ∈ [n] i\in[n] appears in at most a c c -fraction of the sets in ℱ \mathcal{F}. Without loss of generality, we can assume that 1 1 appears in at least one set in ℱ. \mathcal{F}. We consider random variables A, B, C A,B,C, which are three uniform samples from ℱ \mathcal{F}, defined as follows. The uniform sampling of B B happens independently of the sampling of A A and C. C. The latter two are sampled element-wise and in a dependent way. We denote A i = 1 A_{i}=1 if i ∈ A i\in A and otherwise A i = 0 A_{i}=0, i.e., it is the indicator function 1 i ∈ A 1_{i\in A}, and A < i = ( A 1, …, A i − 1) A_{<i}=(A_{1},\ldots,A_{i-1}) is the sequence of the first i − 1 i-1 indicator random variables. Analogously C i C_{i} and C < i C_{<i} are defined.

For every i ∈ [n] i\in[n] and given (fixed) realisations a < i = ( a 1, …, a i − 1) a_{<i}=(a_{1},\ldots,a_{i-1}) and c < i = ( c 1, …, c i − 1) c_{<i}=(c_{1},\ldots,c_{i-1}), we consider the fractions

 | f a = | { S ∈ ℱ: i ∈ S, S < i = a < i } | | { S ∈ ℱ: S < i = a < i } | and f c = | { S ∈ ℱ: i ∈ S, S < i = c < i } | | { S ∈ ℱ: S < i = c < i } |. f_{a}=\frac{\lvert\{S\in\mathcal{F}\colon i\in S,S_{<i}=a_{<i}\}\rvert}{\lvert\{S\in\mathcal{F}\colon S_{<i}=a_{<i}\}\rvert}\mbox{ and }f_{c}=\frac{\lvert\{S\in\mathcal{F}\colon i\in S,S_{<i}=c_{<i}\}\rvert}{\lvert\{S\in\mathcal{F}\colon S_{<i}=c_{<i}\}\rvert}. |  |

If max ⁡ { f a, f c } > 0.5, \max\{f_{a},f_{c}\}>0.5, we take x ∈ U ⁡ ( [0, 1]) x\in U([0,1]), a uniformly random element from [0, 1] [0,1], and take a i = [x < f a] a_{i}=[x<f_{a}] and c i = [x < f c] c_{i}=[x<f_{c}]. That is, a i = 1 a_{i}=1 if x < f a x<f_{a} and otherwise a i = 0. a_{i}=0. Similarly, if f a, f c ≤ 1 / 2, f_{a},f_{c}\leq 1/2, we take a i = [x < f a] a_{i}=[x<f_{a}] and c i = [0.5 − f c < x < 0.5] c_{i}=[0.5-f_{c}<x<0.5] for the uniform random generated x ∈ [0, 1]. x\in[0,1].

If we do the previous steps for every i ∈ [n], i\in[n], there are up to 2 i − 1 2^{i-1} different realisations and fractions.

Let p i = ℙ ⁡ ( A < i + 1 ∣ A < i) p_{i}=\,\mathbb{P}(A_{<i+1}\mid A_{<i}) be the conditional probability distribution, associated with the probability (fraction) for a < i + 1 a_{<i+1} given any realisation of a < i. a_{<i}. Define r i = ℙ ⁡ ( C < i + 1 ∣ C < i) r_{i}=\,\mathbb{P}(C_{<i+1}\mid C_{<i}) completely analogous.

Then with the above steps for concrete realisations, for the random variable A ∪ C, A\cup C, we have

 | ℙ [( A ∪ C) i ∣ A < i, C < i] = max { p i, r i, min ( p i + r i, 1 / 2) }. \,\mathbb{P}[(A\cup C)_{i}\mid A_{<i},C_{<i}]=\max\{p_{i},r_{i},\min(p_{i}+r_{i},1/2)\}. |  |

By the product rule applied to the conditional probabilities p i p_{i}, we have that A A (and similarly C C) will be uniformly distributed over ℱ \mathcal{F}, that is for a particular set T ∈ ℱ, T\in\mathcal{F}, we have

 | ℙ ( A = T) = ∏ i ∈ T | { S ∈ ℱ: i ∈ S, S < i = T < i } | | { S ∈ ℱ: S < i = T < i } | ⋅ ∏ i ∉ T | { S ∈ ℱ: i ∉ S, S < i = T < i } | | { S ∈ ℱ: S < i = T < i } | = 1 | ℱ |. \,\mathbb{P}(A=T)=\prod_{i\in T}\frac{\lvert\{S\in\mathcal{F}\colon i\in S,S_{<i}=T_{<i}\}\rvert}{\lvert\{S\in\mathcal{F}\colon S_{<i}=T_{<i}\}\rvert}\cdot\prod_{i\not\in T}\frac{\lvert\{S\in\mathcal{F}\colon i\not\in S,S_{<i}=T_{<i}\}\rvert}{\lvert\{S\in\mathcal{F}\colon S_{<i}=T_{<i}\}\rvert}=\frac{1}{\lvert\mathcal{F}\rvert}. |  |

Hence A, B, C A,B,C all have the (same) uniform probability distribution. Let q i = ℙ ⁡ ( i ∈ B ∣ B < i) q_{i}=\,\mathbb{P}(i\in B\mid B_{<i}) be a conditional probability distribution. Now p i, q i p_{i},q_{i} and r i r_{i} are identically distributed conditional probability distributions, where q i q_{i} is independent from the other two, but p i p_{i} and q i q_{i} are dependent.

The chain rule and data processing inequality respectively yield

 | H ⁡ ( ( A ∪ B) < i + 1) = H ⁡ ( ( A ∪ B) < i) + H ⁡ ( ( A ∪ B) < i + 1 ∣ ( A ∪ B) < i) ≥ H ⁡ ( ( A ∪ B) < i) + H ⁡ ( ( A ∪ B) < i + 1 ∣ A < i, B < i), H((A\cup B)_{<i+1})=H((A\cup B)_{<i})+H((A\cup B)_{<i+1}\mid(A\cup B)_{<i})\geq H((A\cup B)_{<i})+H((A\cup B)_{<i+1}\mid A_{<i},B_{<i}), |  |

while H ⁡ ( A < i + 1) = H ⁡ ( A < i) + H ⁡ ( A < i + 1 ∣ A < i). H(A_{<i+1})=H(A_{<i})+H(A_{<i+1}\mid A_{<i}). As such to prove that

 | ( 1 − α) ​ H ​ ( A ∪ B) + α ​ H ​ ( A ∪ C) > H ⁡ ( A), (1-\alpha)H(A\cup B)+\alpha H(A\cup C)>H(A), |  |

it is sufficient to prove that ( 1 − α) ​ H ​ ( ( A ∪ B) 1) + α ​ H ​ ( ( A ∪ C) 1) > H ⁡ ( A 1) (1-\alpha)H((A\cup B)_{1})+\alpha H((A\cup C)_{1})>H(A_{1}) and ( 1 − α) ​ H ​ ( ( A ∪ B) < i + 1 ∣ A < i, B < i) + α ​ H ​ ( ( A ∪ C) < i + 1 ∣ A < i, C < i) ≥ H ⁡ ( A < i + 1 ∣ A < i) (1-\alpha)H((A\cup B)_{<i+1}\mid A_{<i},B_{<i})+\alpha H((A\cup C)_{<i+1}\mid A_{<i},C_{<i})\geq H(A_{<i+1}\mid A_{<i}) for every i ≥ 2. i\geq 2. But with the conditional probability distribution of ( A ∪ B) i (A\cup B)_{i}, with which we refer to ℙ ⁡ ( ( A ∪ B) < i + 1 ∣ ( A ∪ B) < i) \,\mathbb{P}((A\cup B)_{<i+1}\mid(A\cup B)_{<i}), being p i + q i − p i ​ q i p_{i}+q_{i}-p_{i}q_{i} (by the principle of inclusion-exclusion) and of ( A ∪ C) i (A\cup C)_{i} being max ⁡ { p i, r i, min ⁡ ( p i + r i, 0.5) } \max\{p_{i},r_{i},\min(p_{i}+r_{i},0.5)\} (by the choice of the samples), where p i, q i, r i p_{i},q_{i},r_{i} all have expectation less than c c, this follows from the answer to Question 2. Since equality cannot appear for i = 1 i=1, the inequality is strict. We conclude that max ⁡ { H ⁡ ( A ∪ C), H ⁡ ( A ∪ B) } > H ⁡ ( A) = log 2 ⁡ | ℱ | \max\{H(A\cup C),H(A\cup B)\}>H(A)=\log_{2}\lvert\mathcal{F}\rvert, which is a contradiction. So no such family ℱ \mathcal{F} as initially assumed exists. ∎

### Acknowledgement

We thank an anonymous referee for their careful reading and valuable suggestions, including critical remarks on readability that helped improve the presentation of the paper. Their recommendation to consider connections with the work of Yu [22] led to the addition of Subsection 3.4, strengthening the resolution of 2.

#### Open access statement.

For the purpose of open access, a CC BY public copyright license is applied to any Author Accepted Manuscript (AAM) arising from this submission.

## References

- [1] R. Alweiss, B. Huang, and M. Sellke, Improved Lower Bound for the Union-Closed Sets Conjecture, arXiv e-prints (2022), arXiv:2211.11731.
- [2] P. Balister and B. Bollobás, Random union-closed families, in Number theory, analysis, and combinatorics, De Gruyter Proc. Math., De Gruyter, Berlin, 2014, pp. 1–9.
- [3] I. Balla, B. Bollobás, and T. Eccles, Union-closed families of sets, J. Combin. Theory Ser. A 120 (2013)(3), 531–544, URL https://doi.org/10.1016/j.jcta.2012.10.005.
- [4] H. Bruhn, P. Charbit, O. Schaudt, and J. A. Telle, The graph formulation of the union-closed sets conjecture, European J. Combin. 43 (2015), 210–219, URL https://doi.org/10.1016/j.ejc.2014.08.030.
- [5] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture, Graphs Combin. 31 (2015)(6), 2043–2074, URL https://doi.org/10.1007/s00373-014-1515-0.
- [6] S. Cambie, Progress on the union-closed conjecture and offsprings in winter 2022-2023, arXiv e-prints (2023), arXiv:2306.12351.
- [7] Z. Chase and S. Lovett, Approximate union closed conjecture, arXiv e-prints (2022), arXiv:2211.11689.
- [8] T. M. Cover and J. A. Thomas, Elements of information theory, Wiley-Interscience [John Wiley & Sons], Hoboken, NJ, second edn., 2006.
- [9] D. Ellis, Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture, arXiv e-prints (2022), arXiv:2211.12401.
- [10] P. Frankl, Extremal set systems, in Handbook of combinatorics, Vol. 1, 2, Elsevier Sci. B. V., Amsterdam, 1995, pp. 1293–1329.
- [11] P. Frankl and N. Tokushige, Extremal problems for finite sets, vol. 86, American Mathematical Soc., 2018.
- [12] J. Gilmer, A constant lower bound for the union-closed sets conjecture, arXiv e-prints (2022), arXiv:2211.09055.
- [13] Y. Hu, On the Union-Closed Sets Conjecture, arXiv e-prints (2017), arXiv:1706.06167.
- [14] J. Karamata, Sur une inégalité rélative aux fonctions convexes., Publ. Math. Univ. Belgrade 1 (1932), 145–148.
- [15] I. Karpas, Two Results on Union-Closed Families, arXiv e-prints (2017), arXiv:1708.01434.
- [16] E. Knill, Graph generated union-closed families of sets, arXiv preprint math/9409215 (1994).
- [17] J. Liu, Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling, arXiv e-prints (2023), arXiv:2306.08824.
- [18] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003)(1), 89–93, URL https://doi.org/10.1017/S0963548302005230.
- [19] I. Rival, Graphs and order, nato asi series, vol. 147, 1985.
- [20] W. Sawin, An improved lower bound for the union-closed set conjecture, arXiv e-prints (2022), arXiv:2211.11504.
- [21] P. Wójcik, Union-closed families of sets, Discrete Math. 199 (1999)(1-3), 173–182, URL https://doi.org/10.1016/S0012-365X(98)00208-8.
- [22] L. Yu, Dimension-free bounds for the union-closed sets conjecture, Entropy 25 (2023)(5), URL https://www.mdpi.com/1099-4300/25/5/767.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
