<!-- source: https://ar5iv.labs.arxiv.org/html/2211.11504 | converted from HTML -->

[2211.11504] An improved lower bound for the union-closed sets conjecture

# An improved lower bound for the union-closed sets conjecture

Will Sawin

###### Abstract.

Gilmer [6] has recently shown that in any nonempty union-closed family ℱ \mathcal{F} of subsets of a finite set, there exists an element contained in at least a proportion .01.01 of the sets of ℱ \mathcal{F}. We improve the proportion from .01.01 to 3 − 5 2 ≈.382 \frac{3-\sqrt{5}}{2}\approx.382 in this result. An improvement to 1 2 \frac{1}{2} would be the Frankl union-closed set conjecture. We follow Gilmer’s method, replacing one key estimate by a sharp estimate. We then suggest a new addition to this method and sketch a proof that it can obtain a constant strictly greater than 3 − 5 2 \frac{3-\sqrt{5}}{2}. We also disprove a conjecture of Gilmer that would have implied the union-closed set conjecture.

We prove the following weak form of the Frankl union-closed conjecture.

###### Theorem 1.

Let ℱ \mathcal{F} be a nonempty union-closed family of subsets of [n] [n]. Then there exists i ∈ [n] i\in[n] contained in a proportion at least 3 − 5 2 \frac{3-\sqrt{5}}{2} of the sets in ℱ \mathcal{F}.

Theorem 1 follows from Theorem 2, which itself follows from Lemma 3. For a random variable A A valued in sets, we let H ⁡ ( A) H(A) be the entropy of A A. For p ∈ [0, 1] p\in[0,1], we let H ⁡ ( p) = − p ​ log ⁡ p − ( 1 − p) ​ log ⁡ ( 1 − p) H(p)=-p\log p-(1-p)\log(1-p) be the Shannon entropy, i.e. the entropy of a Bernoulli random variable with parameter p p. (We never use H H to denote the entropy of a real-valued random variable, so there will be no ambiguity.)

###### Theorem 2.

Let u ∈ [0, 1] u\in[0,1]. Let A A and B B denote independent samples from a distribution over subsets of [n] [n]. Assume that, for all i ∈ [n] i\in[n], Pr [i ∈ A] ≤ u \operatorname{Pr}[i\in A]\leq u. Then

 | H ⁡ ( A ∪ B) ≥ H ⁡ ( A) ⋅ { H ⁡ ( 2 ​ u − u 2) H ⁡ ( u) if ​ u ≤ 3 − 5 2 ( 1 − u) ​ 2 5 − 1 if ​ u ≥ 3 − 5 2. H(A\cup B)\geq H(A)\cdot\begin{cases}\frac{H(2u-u^{2})}{H(u)}&\textrm{ if }u\leq\frac{3-\sqrt{5}}{2}\\ (1-u)\frac{2}{\sqrt{5}-1}&\textrm{ if }u\geq\frac{3-\sqrt{5}}{2}\end{cases}. |  |

###### Lemma 3.

Let u ∈ [0, 1] u\in[0,1]. Let p, q p,q be i.i.d. [0, 1] [0,1] -valued random variables with expectation ≤ u \leq u. Then

 | 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] ≥ 𝔼 ⁡ [H ⁡ ( p)] ⋅ { H ⁡ ( 2 ​ u − u 2) H ⁡ ( u) if ​ u ≤ 3 − 5 2 ( 1 − u) ​ 2 5 − 1 if ​ u ≥ 3 − 5 2 \mathbb{E}[H(p+q-pq)]\geq\mathbb{E}[H(p)]\cdot\begin{cases}\frac{H(2u-u^{2})}{H(u)}&\textrm{ if }u\leq\frac{3-\sqrt{5}}{2}\\ (1-u)\frac{2}{\sqrt{5}-1}&\textrm{ if }u\geq\frac{3-\sqrt{5}}{2}\end{cases} |  |

All three of these represent quantitative improvements of corresponding results of Gilmer [6, Theorem 1, Theorem 2, and Lemma 1], who in particular proved a lower bound of .01.01 for the maximum proportion of the sets in a union-closed family ℱ \mathcal{F} containing an element. The work of Gilmer itself improved on work of Knill [5] and Wójick [7] who proved lower bounds on the proportion comparable to 1 log ⁡ | ℱ | \frac{1}{\log\absolutevalue{\mathcal F}}.

The deduction of Theorem 1 from Theorem 2, and Theorem 2 from Lemma 3, is identical to the one by Gilmer, and relies on taking A A and B B independent samples from the uniform distribution on ℱ \mathcal{F} and estimating the entropy by induction on the restrictions of A A and B B to [i] [i] for i i from 1 1 to n n. The innovation is entirely in the proof of Lemma 3.

Furthermore, Lemma 3 and Theorem 2 are completely sharp – there are examples meeting the inequality for any particular value of u ∈ ( 0, 1) u\in(0,1). Indeed:

###### Example 4.

Theorem 2 is sharp for u ≤ 3 − 5 2 u\leq\frac{3-\sqrt{5}}{2} because of the example, due to Gilmer, where the events i ∈ A i\in A for i ∈ [n] i\in[n] are independent of probability u u. In this case, A A has entropy n ​ H ​ ( u) nH(u) and the events i ∈ A ∪ B i\in A\cup B are independent of probability 2 ​ u − u 2 2u-u^{2} so A ∪ B A\cup B has entropy H ⁡ ( 2 ​ u − u 2) H(2u-u^{2}).

###### Example 5.

Theorem 2 is sharp for u ≥ 3 − 5 2 u\geq\frac{3-\sqrt{5}}{2} because of the example where, with probability ( 1 − u) ​ 2 5 − 1 (1-u)\frac{2}{\sqrt{5}-1}, we choose each element i ∈ [n] i\in[n] to lie in A A independently with probability 3 − 5 2 \frac{3-\sqrt{5}}{2} and with probability 1 − ( 1 − u) ​ 2 5 − 1 1-(1-u)\frac{2}{\sqrt{5}-1}, we choose A = [n] A=[n]. Then A A has entropy ( 1 − u) ​ 2 5 − 1 ​ n ​ H ​ ( 3 − 5 2) + O ⁡ ( 1) (1-u)\frac{2}{\sqrt{5}-1}nH(\frac{3-\sqrt{5}}{2})+O(1) because a convex combination of two probability distributions has entropy that differs from the convex combination of their entropies by ≤ log ⁡ 2 \leq\log 2. Furthermore, with probability ( ( 1 − u) ​ 2 5 − 1) 2 \left((1-u)\frac{2}{\sqrt{5}-1}\right)^{2}, each element i ∈ [n] i\in[n] lies in A ∪ B A\cup B independently with probability 5 − 1 2 \frac{\sqrt{5}-1}{2} and with probability 1 − ( ( 1 − u) ​ 2 5 − 1) 2 1-\left((1-u)\frac{2}{\sqrt{5}-1}\right)^{2}, we have A ∪ B = [n] A\cup B=[n]. Thus A ∪ B A\cup B has entropy ( ( 1 − u) ​ 2 5 − 1) 2 ​ n ​ H ​ ( 5 − 1 2) + O ⁡ ( 1) \left((1-u)\frac{2}{\sqrt{5}-1}\right)^{2}nH(\frac{\sqrt{5}-1}{2})+O(1) for the same reason. Dividing, and ignoring the lower-order O ⁡ ( 1) O(1) term, we see that Theorem 3 is sharp since H ⁡ ( 3 − 5 2) = H ⁡ ( 5 − 1 2) H(\frac{3-\sqrt{5}}{2})=H(\frac{\sqrt{5}-1}{2}). This gives a negative answer to a question of Gilmer [6, first bulleted question on p.9] for u > 3 − 5 2 u>\frac{3-\sqrt{5}}{2}, while Theorem 2 gives a positive answer to that question for u ≤ 3 − 5 2 u\leq\frac{3-\sqrt{5}}{2}.

The sharpness of Lemma 3 arises from, for u ≤ 3 − 5 2 u\leq\frac{3-\sqrt{5}}{2}, a random variable equal to u u with probability 1 1, or, if u ≥ 3 − 5 2 u\geq\frac{3-\sqrt{5}}{2}, a random variable equal to 3 − 5 2 \frac{3-\sqrt{5}}{2} with probability ( 1 − u) ​ 2 5 − 1 (1-u)\frac{2}{\sqrt{5}-1} and equal to 1 1 with probability 1 − ( 1 − u) ​ 2 5 − 1 1-(1-u)\frac{2}{\sqrt{5}-1}.

Furthermore, we demonstrate that, contrary to [6, Conjecture 1 on p. 9], incorporating the KL divergence does not improve the estimate:

###### Proposition 6.

For any u < 1 u<1 and d > H ⁡ ( 2 ​ u − u 2) H ⁡ ( u) d>\frac{H(2u-u^{2})}{H(u)}, for all sufficiently large n n, there exist a random variable A A valued in subsets of [n] [n], containing each element with probability ≤ u \leq u, such that H ⁡ ( A ∪ B) ≤ d ​ H ​ ( A) H(A\cup B)\leq dH(A), but D ( A ∪ B | | A) = O ( 1) D(A\cup B||A)=O(1) while H ⁡ ( A) H(A) grows linearly in n n.

The proof of Lemma 3 uses calculus of variations to replace the quadratic form 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] \mathbb{E}[H(p+q-pq)] with a bilinear form. The key idea is that, while we cannot use Jensen’s inequality since the relevant functions like H ⁡ ( p + q − p ​ q) − λ ​ H ​ ( p) H(p+q-pq)-\lambda H(p) are not convex, we can show that a relevant function is convex on one region and concave on another region, and there are also strong (but very different) inequalities for the expectation of a concave function.

Finally, we sketch a proof of Theorem 1 with the lower bound replaced by 3 − 5 2 + δ \frac{3-\sqrt{5}}{2}+\delta for some δ > 0 \delta>0. The idea is to consider, in addition to A A and B B independent uniform samples for ℱ \mathcal{F}, also A A and C C uniform but correlated samples from ℱ \mathcal{F}. We choose the correlation greedily to maximize the entropy increase at each step in the inductive argument. This gives a gain in entropy compared to the independent samples but also a loss as the correlations in previous steps can cause problems in future steps. However, for distributions close to the optimum in Lemma 3, the gain is greater than the loss, so we gain overall by considering a suitable linear combination of the two entropies.

The author was supported by NSF grant DMS-2101491 while working on the paper and would like to thank Ryan Alweiss, Stijn Cambie, Zachary Chase, and Lucas Gerardo Hernández Chávez for helpful comments on earlier versions of this manuscript. I would especially like to thank Bhavik Mehta for pointing out an error in the original proof of Lemma 8 and Ravi Bopanna for pointing me to the techniques for a corrected proof based on his proof in [2] of a special case sufficient for Theorem 1.

The same day this article first appeared on arXiv, two independent proofs [1, 3] of Theorem 1 also did. Since [3] depended on [1] for a key lemma, and the proof of a similar lemma in the first version of this article contained an error, only [1] gave a completely independent proof. The next day, an independent construction [4] of a counterexample similar to Proposition 6 (for n = 2 n=2 instead of for fixed n n) appeared.

## 1. Proofs

###### Proof of Theorem 1 using Theorem 2.

The proof is identical to [6, p. 2], but we repeat it here for convenience.

Let A A and B B be independent uniform samples from ℱ \mathcal{F}. Assuming for contradiction that there does not exist i ∈ [n] i\in[n] contained in a proportion at least 3 − 5 2 \frac{3-\sqrt{5}}{2} of the sets in ℱ \mathcal{F}, there must be u < 3 − 5 2 u<\frac{3-\sqrt{5}}{2} for which each element of [n] [n] is contained in a proportion ≤ u \leq u of sets in ℱ \mathcal{F} and thus for which Pr [i ∈ A] ≤ u \operatorname{Pr}[i\in A]\leq u for all i ∈ n i\in n. We then have

 | H ⁡ ( A ∪ B) ≥ H ⁡ ( A) ⋅ H ⁡ ( 2 ​ u − u 2) H ⁡ ( u) > H ⁡ ( A) H(A\cup B)\geq H(A)\cdot\frac{H(2u-u^{2})}{H(u)}>H(A) |  |

which contradicts the fact that the uniform distribution on ℱ \mathcal{F} is the maximum-entropy random variable supported on ℱ \mathcal{F}. ∎

Let λ = { H ⁡ ( 2 ​ u − u 2) H ⁡ ( u) if ​ u ≤ 3 − 5 2 ( 1 − u) ​ 2 5 − 1 if ​ u ≥ 3 − 5 2 \lambda=\begin{cases}\frac{H(2u-u^{2})}{H(u)}&\textrm{ if }u\leq\frac{3-\sqrt{5}}{2}\\ (1-u)\frac{2}{\sqrt{5}-1}&\textrm{ if }u\geq\frac{3-\sqrt{5}}{2}\end{cases}.

###### Proof of Theorem 2 using Lemma 3.

The proof is identical to [6, Proof of Theorem 1 on p. 4], but we repeat it here for convenience.

Let A < i A_{<i} be the intersection of A A with [i − 1] [i-1], and similarly for B < i B_{<i} and ( A ∪ B) < i = A < i ∪ B < i (A\cup B)_{<i}=A_{<i}\cup B_{<i}. We prove

(1) |  | H ⁡ ( ( A ∪ B) < i) ≥ H ⁡ ( A < i) ⋅ λ H((A\cup B)_{<i})\geq H(A_{<i})\cdot\lambda |  |

by induction on i i. The case i = n + 1 i=n+1 will prove the theorem. The base case i = 1 i=1 is trivial as both sides are 0 0. For the induction step, by the chain rule for entropy, we have

 | H ( ( A ∪ B) < i + 1) = H ( ( A ∪ B) < ( i + 1) | ( A ∪ B) < i) + H ( ( A ∪ B) < i) H((A\cup B)_{{}_{<i+1}})=H((A\cup B)_{<(i+1)}|(A\cup B)_{<i})+H((A\cup B)_{<i}) |  |

and

 | H ( A < i + 1) = H ( A < ( i + 1) | A < i) + H ( A < i) H(A_{{}_{<i+1}})=H(A_{<(i+1)}|A_{<i})+H(A_{<i}) |  |

so assuming ( 1) for i i, to obtain ( 1) for i + 1 i+1 it suffices to check

(2) |  | H ⁡ ( ( A ∪ B) < ( i + 1) | ( A ∪ B) < i) ≥ λ ​ H ​ ( A < ( i + 1) | A < i). H((A\cup B)_{<(i+1)}|(A\cup B)_{<i})\geq\lambda H(A_{<(i+1)}|A_{<i}). |  |

We have

 | H ⁡ ( ( A ∪ B) < ( i + 1) | ( A ∪ B) < i) ≥ H ⁡ ( ( A ∪ B) < ( i + 1) | A < i, B < i) H((A\cup B)_{<(i+1)}|(A\cup B)_{<i})\geq H((A\cup B)_{<(i+1)}|A_{<i},B_{<i}) |  |

by the data processing inequality. Let p i = Pr ⁡ [i ∈ A | A < i] p_{i}=\operatorname{Pr}[i\in A|A_{<i}] and q i = Pr ⁡ [i ∈ B | B < i] q_{i}=\operatorname{Pr}[i\in B|B_{<i}] be the conditional probabilities. Then because A A and B B are independent and identically distributed, p i p_{i} and q i q_{i} are independent, identically distributed random variables with expectation ≤ u \leq u. Furthermore, the probability that i ∈ ( A ∪ B) < ( i + 1) i\in(A\cup B)_{<(i+1)} conditional on A < i A_{<i} and B < i B_{<i} is p i + q i − p i ​ q i p_{i}+q_{i}-p_{i}q_{i}. Since i ∈ A i\in A is the only information contained in A < ( i + 1) A_{<(i+1)} but not A < i A_{<i}, we have H ⁡ ( A < ( i + 1) | A < i) = 𝔼 ⁡ [H ⁡ ( p i)] H(A_{<(i+1)}|A_{<i})=\mathbb{E}[H(p_{i})] and similarly H ⁡ ( ( A ∪ B) < ( i + 1) | A < i, B < i) = 𝔼 ⁡ [H ⁡ ( p i + q i − p i ​ q i)] H((A\cup B)_{<(i+1)}|A_{<i},B_{<i})=\mathbb{E}[H(p_{i}+q_{i}-p_{i}q_{i})]. ( 2) then follows from Lemma 3.

∎

###### Proof of Lemma 3.

An equivalent statement is that the minimum value of

(3) |  | 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)] \mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]-\lambda\mathbb{E}_{p\sim\mu}[H(p)] |  |

among all probability measures μ \mu on [0, 1] [0,1] with expectation ≤ u \leq u is nonnegative.

The minimum value is attained by a measure since every sequence of probability measures μ \mu on [0, 1] [0,1] has a weakly convergent subsequence and the functions H ⁡ ( p + q − p ​ q) H(p+q-pq), H ⁡ ( p) H(p), and p p are all continuous, so their expectations over weakly convergent sequences of measures converge.

Let us first check that, if μ \mu an optimal measure, then μ \mu also minimizes

(4) |  | 2 ​ 𝔼 ( p, q) ∼ μ × ν ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 q ∼ ν ​ [H ⁡ ( q)] = 𝔼 q ∼ ν ​ [2 ​ 𝔼 p ∼ μ ​ [H ⁡ ( p + q − p ​ q)] − λ ​ H ​ ( q)] 2\mathbb{E}_{(p,q)\sim\mu\times\nu}[H(p+q-pq)]-\lambda\mathbb{E}_{q\sim\nu}[H(q)]=\mathbb{E}_{q\sim\nu}\left[2\mathbb{E}_{p\sim\mu}[H(p+q-pq)]-\lambda H(q)\right] |  |

among all probability measures ν \nu on [0, 1] [0,1] with expectation ≤ u \leq u. Indeed, otherwise, taking μ ′ = ( 1 − ϵ) ​ μ + ϵ ​ ν \mu^{\prime}=(1-\epsilon)\mu+\epsilon\nu

 | 𝔼 ( p, q) ∼ μ ′ × μ ′ ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 p ∼ μ ′ ​ [H ⁡ ( p)] \mathbb{E}_{(p,q)\sim\mu^{\prime}\times\mu^{\prime}}[H(p+q-pq)]-\lambda\mathbb{E}_{p\sim\mu^{\prime}}[H(p)] |  |

 | = ( 1 − ϵ) 2 ​ 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] + 2 ​ ϵ ​ ( 1 − ϵ) ​ 𝔼 ( p, q) ∼ μ × ν ​ [H ⁡ ( p + q − p ​ q)] =(1-\epsilon)^{2}\mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]+2\epsilon(1-\epsilon)\mathbb{E}_{(p,q)\sim\mu\times\nu}[H(p+q-pq)] |  |

 | + ϵ 2 ​ 𝔼 ( p, q) ∼ ν × ν ​ [H ⁡ ( p + q − p ​ q)] − λ ⁡ ( 1 − ϵ) ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)] − λ ​ ϵ ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)] +\epsilon^{2}\mathbb{E}_{(p,q)\sim\nu\times\nu}[H(p+q-pq)]-\lambda(1-\epsilon)\mathbb{E}_{p\sim\mu}[H(p)]-\lambda\epsilon\mathbb{E}_{p\sim\mu}[H(p)] |  |

 | = 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)] =\mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]-\lambda\mathbb{E}_{p\sim\mu}[H(p)] |  |

 | + ϵ ⁡ ( 2 ​ 𝔼 ( p, q) ∼ μ × ν ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 p ∼ ν ​ [H ⁡ ( p)] − 2 ​ 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] + λ ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)]) + O ⁡ ( ϵ 2) +\epsilon\left(2\mathbb{E}_{(p,q)\sim\mu\times\nu}[H(p+q-pq)]-\lambda\mathbb{E}_{p\sim\nu}[H(p)]-2\mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]+\lambda\mathbb{E}_{p\sim\mu}[H(p)]\right)+O(\epsilon^{2}) |  |

which if the coefficient of ϵ \epsilon is negative will be < 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)] <\mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]-\lambda\mathbb{E}_{p\sim\mu}[H(p)] for small ϵ \epsilon, contradicting the minimality of μ \mu, and verifying that the minimal value of ( 4) is attained by ν = μ \nu=\mu.

We now study the function F μ ​ ( q) = 2 ​ 𝔼 p ∼ μ ​ [H ⁡ ( p + q − p ​ q) − λ ​ H ​ ( q)] F_{\mu}(q)=2\mathbb{E}_{p\sim\mu}[H(p+q-pq)-\lambda H(q)]. Specifically, we calculate d d ​ q ​ q ​ ( 1 − q) ​ d 2 d ​ q 2 ​ F μ ​ ( q) \frac{d}{dq}q(1-q)\frac{d^{2}}{dq^{2}}F_{\mu}(q).

To do this, note that H ⁡ ( q) = − q ​ log ⁡ q − ( 1 − q) ​ log ⁡ ( 1 − q) H(q)=-q\log q-(1-q)\log(1-q), so d d ​ q ​ H ​ ( q) = − log ⁡ q + log ⁡ ( 1 − q) \frac{d}{dq}H(q)=-\log q+\log(1-q) and d 2 d ​ q 2 ​ H ​ ( q) = − 1 q − 1 1 − q = − 1 q ⁡ ( 1 − q) \frac{d^{2}}{dq^{2}}H(q)=-\frac{1}{q}-\frac{1}{1-q}=-\frac{1}{q(1-q)}. By the chain rule for a linear change of coordinates, d 2 d ​ q 2 ​ H ​ ( p + q − p ​ q) = − ( 1 − p) 2 ( p + q − p ​ q) ​ ( 1 − p − q + p ​ q) = − 1 − p ( p + q − p ​ q) ​ ( 1 − q) \frac{d^{2}}{dq^{2}}H(p+q-pq)=-\frac{(1-p)^{2}}{(p+q-pq)(1-p-q+pq)}=-\frac{1-p}{(p+q-pq)(1-q)}. Thus

 | d 2 d ​ q 2 ​ F μ ​ ( q) = − 2 ​ 𝔼 p ∼ μ ​ [1 − p ( p + q − p ​ q) ​ ( 1 − q)] + λ ​ 1 q ⁡ ( 1 − q), \frac{d^{2}}{dq^{2}}F_{\mu}(q)=-2\mathbb{E}_{p\sim\mu}\left[\frac{1-p}{(p+q-pq)(1-q)}\right]+\lambda\frac{1}{q(1-q)}, |  |

 | q ⁡ ( 1 − q) ​ d 2 d ​ q 2 ​ F μ ​ ( q) = − 2 ​ 𝔼 p ∼ μ ​ [( 1 − p) ​ q p + q − p ​ q] + λ, q(1-q)\frac{d^{2}}{dq^{2}}F_{\mu}(q)=-2\mathbb{E}_{p\sim\mu}\left[\frac{(1-p)q}{p+q-pq}\right]+\lambda, |  |

and therefore

 | d d ​ q ​ q ​ ( 1 − q) ​ d 2 d ​ q 2 ​ F μ ​ ( q) = − 2 ​ 𝔼 p ∼ μ ​ [( 1 − p) ​ p ( p + q − p ​ q) 2] < 0, \frac{d}{dq}q(1-q)\frac{d^{2}}{dq^{2}}F_{\mu}(q)=-2\mathbb{E}_{p\sim\mu}\left[\frac{(1-p)p}{(p+q-pq)^{2}}\right]<0, |  |

at least outside the degenerate case when μ \mu is supported on 0 0 and 1 1 and ( 3) is zero.

It follows that q ⁡ ( 1 − q) ​ d 2 d ​ q 2 ​ F μ ​ ( q) q(1-q)\frac{d^{2}}{dq^{2}}F_{\mu}(q) is strictly decreasing. In particular, it either takes positive values on some interval [0, a) [0,a), zero value at a a, and negative values on ( a, 1] (a,1], or is positive on all of [0, 1] [0,1], or negative on all of [0, 1] [0,1].

d 2 d ​ q 2 ​ F μ ​ ( q) \frac{d^{2}}{dq^{2}}F_{\mu}(q) is positive or negative exactly where q ⁡ ( 1 − q) ​ d 2 d ​ q 2 ​ F μ ​ ( q) q(1-q)\frac{d^{2}}{dq^{2}}F_{\mu}(q) is. Thus F μ ​ ( q) F_{\mu}(q) is either strictly convex on some interval [0, a) [0,a) and strictly concave on ( a, 1] (a,1], convex on the whole interval, or concave on the whole interval.

If μ \mu minimizes the expectation of F μ ​ ( q) F_{\mu}(q) then μ \mu must assign zero measure to the concave interval ( a, 1) (a,1), except its boundary points { a, 1 } \{a,1\}, since otherwise we could push the mass to the boundary while preserving the expectation of q q and lower the expectation of F μ ​ ( q) F_{\mu}(q). Similarly, μ \mu restricted to the convex interval [0, a] [0,a] must be an atom since otherwise we could push the mass to the center while preserving the expectation of q q and lower the expectation of F μ ​ ( q) F_{\mu}(q).

So μ \mu is atomic, supported on the point 1 1 and at most one other point. (In the convex or concave case, the reasoning is similar but simpler). It therefore suffices to show ( 3) is nonnegative for all measures μ \mu of this form.

Let μ \mu place mass w w on the point v v and mass 1 − w 1-w on the point 1 1. Then 𝔼 p ∼ μ ​ [H ​ ( p)] \mathbb{E}_{p\sim\mu}[H(p)] is w ​ H ​ ( v) wH(v) and 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] \mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)] is w 2 ​ H ​ ( 2 ​ v − v 2) w^{2}H(2v-v^{2}), and thus

 | 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] − λ ​ 𝔼 p ∼ μ ​ [H ⁡ ( p)] ≥ 0 \mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]-\lambda\mathbb{E}_{p\sim\mu}[H(p)]\geq 0 |  |

as long as

 | w 2 ​ H ​ ( 2 ​ v − v 2) ≥ λ ​ w ​ H ​ ( v), w^{2}H(2v-v^{2})\geq\lambda wH(v), |  |

i.e. as long as

 | w ​ H ⁡ ( 2 ​ v − v 2) H ⁡ ( v) ≥ λ. w\frac{H(2v-v^{2})}{H(v)}\geq\lambda. |  |

Since the left side is increasing in w w, this holds for all such measures with expectation 1 − w ⁡ ( 1 − v) ≤ u 1-w(1-v)\leq u if and only if it holds for w = 1 − u 1 − v w=\frac{1-u}{1-v}, i.e. if and only if

 | ( 1 − u) ​ min v ∈ [0, u] ⁡ ( H ⁡ ( 2 ​ v − v 2) H ​ ( v) ​ ( 1 − v)) ≥ λ. (1-u)\min_{v\in[0,u]}\left(\frac{H(2v-v^{2})}{H(v)(1-v)}\right)\geq\lambda. |  |

By Lemma 8 below, H ⁡ ( 2 ​ v − v 2) H ​ ( v) ​ ( 1 − v) \frac{H(2v-v^{2})}{H(v)(1-v)} is decreasing for v < 3 − 5 2 v<\frac{3-\sqrt{5}}{2} and increasing for v > 3 − 5 2 v>\frac{3-\sqrt{5}}{2}. Furthermore at v = 3 − 5 2 v=\frac{3-\sqrt{5}}{2}, we have H ⁡ ( 2 ​ v − v 2) H ⁡ ( v) = 1 \frac{H(2v-v^{2})}{H(v)}=1 so H ⁡ ( 2 ​ v − v 2) H ​ ( v) ​ ( 1 − v) = 2 5 − 1 \frac{H(2v-v^{2})}{H(v)(1-v)}=\frac{2}{\sqrt{5}-1}. It follows that

 | min v ∈ [0, u] ⁡ ( H ⁡ ( 2 ​ v − v 2) H ​ ( v) ​ ( 1 − v)) = { H ⁡ ( 2 ​ u − u 2) H ​ ( u) ​ ( 1 − u) if ​ u ≤ 3 − 5 2 2 5 − 1 if ​ u ≥ 3 − 5 2 = λ ( 1 − u), \min_{v\in[0,u]}\left(\frac{H(2v-v^{2})}{H(v)(1-v)}\right)=\begin{cases}\frac{H(2u-u^{2})}{H(u)(1-u)}&\textrm{ if }u\leq\frac{3-\sqrt{5}}{2}\\ \frac{2}{\sqrt{5}-1}&\textrm{ if }u\geq\frac{3-\sqrt{5}}{2}\end{cases}=\frac{\lambda}{(1-u)}, |  |

giving the claim. ∎

###### Lemma 7.

For all s ∈ ( 0, 1) s\in(0,1), we have H ⁡ ( s 2) < 2 ​ s ​ H ​ ( s) H(s^{2})<2sH(s).

###### Proof.

We have 2 ​ ( 1 − s) > ( 1 − s 2) 2(1-s)>(1-s^{2}) since their difference is ( 1 − s) 2 > 0 (1-s)^{2}>0 and we have

 | − s ​ log ⁡ ( 1 − s) = s 2 + s 3 / 2 + s 4 / 3 + ⋯ > s 2 + s 4 / 2 + s 6 / 3 + ⋯ = − log ⁡ ( 1 − s 2) -s\log(1-s)=s^{2}+s^{3}/2+s^{4}/3+\dots>s^{2}+s^{4}/2+s^{6}/3+\dots=-\log(1-s^2) |  |

so

 | H ⁡ ( s 2) = − s 2 ​ log ⁡ ( s 2) − ( 1 − s 2) ​ log ⁡ ( 1 − s 2) < − s 2 ​ log ⁡ ( s 2) − 2 ​ ( 1 − s) ​ log ⁡ ( 1 − s 2) H(s^{2})=-s^{2}\log(s^2)-(1-s^{2})\log(1-s^2)<-s^{2}\log(s^2)-2(1-s)\log(1-s^2) |  |

 | < − s 2 ​ log ⁡ ( s 2) − 2 ​ s ​ ( 1 − s) ​ log ⁡ ( 1 − s) = 2 ​ s ​ H ​ ( s). <-s^{2}\log(s^2)-2s(1-s)\log(1-s)=2sH(s). |  |

∎

###### Lemma 8.

The function H ⁡ ( 2 ​ v − v 2) H ​ ( v) ​ ( 1 − v) \frac{H(2v-v^{2})}{H(v)(1-v)} from ( 0, 1) (0,1) to ℝ \mathbb{R} is decreasing for v < 3 − 5 2 v<\frac{3-\sqrt{5}}{2} and increasing for v > 3 − 5 2 v>\frac{3-\sqrt{5}}{2}.

###### Proof.

Making the change of variables s = 1 − v s=1-v, the expression H ⁡ ( 2 ​ v − v 2) H ​ ( v) ​ ( 1 − v) \frac{H(2v-v^{2})}{H(v)(1-v)} simplifies slightly to H ⁡ ( s 2) s ​ H ​ ( s) \frac{H(s^{2})}{sH(s)}, which we denote by F ⁡ ( s) F(s). We must show F ⁡ ( s) F(s) is decreasing for s < 5 − 1 2 = ϕ − 1 s<\frac{\sqrt{5}-1}{2}=\phi^{-1} and increasing for s > ϕ − 1 s>\phi^{-1}. Owing to the fact that ϕ − 1 \phi^{-1} is a local minimum of F ⁡ ( s) F(s) (by direct calculation or [2]), it suffices to show the derivative of F ⁡ ( s) F(s) is nonvanishing for all s ∈ ( 0, 1) ∖ { 5 − 1 2 } s\in(0,1)\setminus\{\frac{\sqrt{5}-1}{2}\}.

Fix an s 0 s_{0} where the derivative of F ⁡ ( s) F(s) vanishes, from which we will derive a contradiction, and let β = F ⁡ ( s 0) \beta=F(s_{0}). Then H ⁡ ( s 2) s ​ H ​ ( s) − β \frac{H(s^{2})}{sH(s)}-\beta vanishes to second order at s 0 s_{0} so H ⁡ ( s 2) − β ​ s ​ H ​ ( s) H(s^{2})-\beta sH(s) vanishes to second order at s 0 s_{0} as well.

The function H ⁡ ( s 2) − β ​ s ​ H ​ ( s) H(s^{2})-\beta sH(s) also vanishes to second order at 0 0, and to first order at 1 1. If those are the only zeroes of H ⁡ ( s 2) − β ​ s ​ H ​ ( s) H(s^{2})-\beta sH(s) in the interval [0, 1] [0,1], then H ⁡ ( s 2) − β ​ s ​ H ​ ( s) H(s^{2})-\beta sH(s) never changes sign on ( 0, 1) ∖ { s 0 } (0,1)\setminus\{s_{0}\}, making s 0 s_{0} either a unique global minimum or a unique global maximum of F ⁡ ( s) F(s). But this is impossible as we know ϕ − 1 \phi^{-1} is a global minimum [2, Lemma on p. 2] and the global maximum is not attained since F ⁡ ( s) < 2 F(s)<2 for all s ∈ ( 0, 1) s\in(0,1) by Lemma 7 but F ⁡ ( s) F(s) converges to 2 2 as s → 0 s\to 0 or s → 1 s\to 1 by an easy calculation.

So H ⁡ ( s 2) − β ​ s ​ H ​ ( s) H(s^{2})-\beta sH(s) must have at least one more zero and thus it has zeroes in [0, 1] [0,1] of total order at least six, so its third derivative has zeroes in [0, 1] [0,1] of total order at least three by Rolle’s theorem.

Differentiating H ⁡ ( s 2) − β ​ s ​ H ​ ( s) H(s^{2})-\beta sH(s) three times, we obtain

 | d 3 d ​ s 3 ​ H ​ ( s 2) = d 2 d ​ s 2 ​ 2 ​ s ​ H ′ ​ ( s 2) = d d ​ s ​ ( 2 ​ H ′ ​ ( s 2) + 4 ​ s 2 ​ H ′′ ​ ( s 2)) = 12 ​ s ​ H ′′ ​ ( s 2) + 8 ​ s 3 ​ H ′′′ ​ ( s 2) \frac{d^{3}}{ds^{3}}H(s^{2})=\frac{d^{2}}{ds^{2}}2sH^{\prime}(s^{2})=\frac{d}{ds}(2H^{\prime}(s^{2})+4s^{2}H^{\prime\prime}(s^{2}))=12sH^{\prime\prime}(s^{2})+8s^{3}H^{\prime\prime\prime}(s^{2}) |  |

 | = − 12 ​ s s 2 ​ ( 1 − s 2) + 8 ​ s 3 ​ ( 1 − 2 ​ s 2) ( s 2 ​ ( 1 − s 2)) 2 = − 4 − 4 ​ s 2 s ​ ( 1 − s 2) 2 =\frac{-12s}{s^{2}(1-s^{2})}+\frac{8s^{3}(1-2s^{2})}{(s^{2}(1-s^{2}))^{2}}=\frac{-4-4s^{2}}{s(1-s^{2})^{2}} |  |

and

 | d 3 d ​ s 3 ​ s ​ H ​ ( s) = 3 ​ d 2 d ​ s 2 ​ H ​ ( s) + s ​ d 3 d ​ s 3 ​ H ​ ( s) = − 3 s ⁡ ( 1 − s) + s ​ 1 − 2 ​ s s 2 ​ ( 1 − s) 2 = s ⁡ ( 1 − 2 ​ s) − 3 ​ s ​ ( 1 − s) s 2 ​ ( 1 − s) 2 = s − 2 s ​ ( 1 − s) 2. \frac{d^{3}}{ds^{3}}sH(s)=3\frac{d^{2}}{ds^{2}}H(s)+s\frac{d^{3}}{ds^{3}}H(s)=\frac{-3}{s(1-s)}+s\frac{1-2s}{s^{2}(1-s)^{2}}=\frac{s(1-2s)-3s(1-s)}{s^{2}(1-s)^{2}}=\frac{s-2}{s(1-s)^{2}}. |  |

so

 | d 3 d ​ s 3 ​ H ​ ( s 2) − β ​ s ​ H ​ ( s) = − 4 − 4 ​ s 2 − β ⁡ ( s − 2) ​ ( 1 + s) 2 s ​ ( 1 − s 2) 2. \frac{d^{3}}{ds^{3}}H(s^{2})-\beta sH(s)=\frac{-4-4s^{2}-\beta(s-2)(1+s)^{2}}{s(1-s^{2})^{2}}. |  |

The numerator is a polynomial in s s of degree 3 3 with leading coefficient − β -\beta. Since the leading coefficient is negative, and the numerator takes the value − 4 + 2 ​ β < 0 -4+2\beta<0 at 0 0 (because β < 2 \beta<2 by Lemma 7), the numerator must have at least one negative real zero. Thus it has at most two zeroes in [0, 1] [0,1], giving the desired contradiction.

∎

###### Proof of Proposition 6.

Fix u ¯ < u \overline{u}<u such that d > H ⁡ ( 2 ​ u ¯ − u ¯ 2) H ⁡ ( u ¯) d>\frac{H(2\overline{u}-\overline{u}^{2})}{H(\overline{u})}.

Define a distribution A A as follows. First generate a nonnegative-integer-valued random variable k k according to the geometric distribution with parameter θ \theta, i.e. the probability of attaining k k is ( 1 − θ) ​ θ k (1-\theta)\theta^{k}. Then choose each i ∈ [n] i\in[n] to lie in A A independently, uniformly, with probability 1 − ( 1 − u ¯) k + 1 1-(1-\overline{u})^{k+1}. We choose θ \theta sufficiently small to ensure various inequalities are satisfied.

Each element lies in A A with probability ∑ k = 0 ∞ ( 1 − θ) ​ θ k ​ ( 1 − ( 1 − u ¯) k + 1) \sum_{k=0}^{\infty}(1-\theta)\theta^{k}(1-(1-\overline{u})^{k+1}). As θ → 0 \theta\to 0, this converges to u ¯ \overline{u}, so for θ \theta sufficiently small this probability is at most u u.

The entropy of A A is at least the average over values of k k of the entropy conditional on k k, which is ∑ k = 0 ∞ ( 1 − θ) ​ θ k ​ n ​ H ​ ( ( 1 − u ¯) k + 1) \sum_{k=0}^{\infty}(1-\theta)\theta^{k}nH((1-\overline{u})^{k+1}).

For A, B A,B two independent samples from the same distribution, let k A k_{A} and k B k_{B} be the k k values used to sample A A and B B, and let k ′ = k A + k B + 1 k^{\prime}=k_{A}+k_{B}+1. Then k ′ k^{\prime} is a positive integer, the probability of obtaining a given value k ′ k^{\prime} is ( 1 − θ) 2 ​ k ′ ​ θ k ′ − 1 (1-\theta)^{2}k^{\prime}\theta^{k^{\prime}-1}, and each element i ∈ [n] i\in[n] lies in A ∪ B A\cup B independently, uniformly, with probability 1 − ( 1 − u ¯) k ′ + 1 1-(1-\overline{u})^{k^{\prime}+1}.

The entropy of A ∪ B A\cup B is at most the entropy of the random variable k ′ k^{\prime}, which is finite, plus the average over k ′ k^{\prime} of the entropy conditionally on k ′ k^{\prime}, which is ∑ k ′ = 1 ∞ ( 1 − θ) ​ k ′ ​ θ k ′ − 1 ​ n ​ H ​ ( ( 1 − u ¯) k ′ + 1) \sum_{k^{\prime}=1}^{\infty}(1-\theta){k^{\prime}}\theta^{k^{\prime}-1}nH((1-\overline{u})^{k^{\prime}+1}). So the ratio of entropies is at most

 | O ⁡ ( 1) + ∑ k ′ = 0 ∞ ( 1 − θ) ​ k ′ ​ θ k ′ − 1 ​ n ​ H ​ ( ( 1 − u ¯) k ′ + 1) ∑ k = 0 ∞ ( 1 − θ) ​ θ k ​ n ​ H ​ ( ( 1 − u ¯) k + 1) = o ⁡ ( 1) + ∑ k ′ = 0 ∞ ( 1 − θ) ​ k ′ ​ θ k ′ − 1 ​ H ​ ( ( 1 − u ¯) k ′ + 1) ∑ k = 0 ∞ ( 1 − θ) ​ θ k ​ H ​ ( ( 1 − u ¯) k + 1). \frac{O(1)+\sum_{k^{\prime}=0}^{\infty}(1-\theta){k^{\prime}}\theta^{k^{\prime}-1}nH((1-\overline{u})^{k^{\prime}+1})}{\sum_{k=0}^{\infty}(1-\theta)\theta^{k}nH((1-\overline{u})^{k+1})}=o(1)+\frac{\sum_{k^{\prime}=0}^{\infty}(1-\theta){k^{\prime}}\theta^{k^{\prime}-1}H((1-\overline{u})^{k^{\prime}+1})}{\sum_{k=0}^{\infty}(1-\theta)\theta^{k}H((1-\overline{u})^{k+1})}. |  |

As θ → 0 \theta\to 0, the numerator and denominator of the fraction converge to H ⁡ ( 2 ​ u ¯ − u ¯ 2) H(2\overline{u}-\overline{u}^{2}) and H ⁡ ( u ¯) H(\overline{u}) respectively, so for θ \theta sufficiently small the fraction is strictly less than d d, and then for n n sufficiently large the ratio of entropies is at most d d.

Finally, by the convexity of KL divergence,

 | D ( A ∪ B | | A) ≤ ∑ k ′ = 1 ∞ ( 1 − θ) k ′ θ k ′ − 1 D ( S k ′ | | A),, D(A\cup B||A)\leq\sum_{k^{\prime}=1}^{\infty}(1-\theta){k^{\prime}}\theta^{k^{\prime}-1}D(S_{k^{\prime}}||A),, |  |

where each i i lies in S k ′ S_{k^{\prime}} independently, uniformly, with probability 1 − ( 1 − u ¯) k ′ + 1 1-(1-\overline{u})^{k^{\prime}+1}. The distribution of S k ′ S_{k^{\prime}} can be obtained by conditioning A A on an event with probability ( 1 − θ) ​ θ k ′ (1-\theta)\theta^{k^{\prime}}, so the probability that S k ′ = S S_{k^{\prime}}=S is always at most 1 ( 1 − θ) ​ θ k ′ \frac{1}{(1-\theta)\theta^{k^{\prime}}} times the probability that A = S A=S, giving

 | D ( S k ′ | | A) ≤ log ( 1 ( 1 − θ) ​ θ k ′) = − k ′ log θ − log ⁡ ( 1 − θ) D(S_{k^{\prime}}||A)\leq\log\left(\frac{1}{(1-\theta)\theta^{k^{\prime}}}\right)=-k^{\prime}\log\theta-\log(1-\theta) |  |

so that

 | D ( A ∪ B | | A) ≤ ∑ k ′ = 1 ∞ ( 1 − θ) k ′ θ k ′ − 1 ( − k ′ log θ − log ⁡ ( 1 − θ)) = O ( 1) D(A\cup B||A)\leq\sum_{k^{\prime}=1}^{\infty}(1-\theta){k^{\prime}}\theta^{k^{\prime}-1}(-k^{\prime}\log\theta-\log(1-\theta))=O(1) |  |

since the sum of a quadratic function against an exponentially decreasing function is bounded.

∎

## 2. Proof Sketch

We sketch a proof that there exists δ > 0 \delta>0 such that, for ℱ \mathcal{F} a nonempty union-closed family of subsets of [n] [n], there exists i ∈ [n] i\in[n] contained in a proportion at least 3 − 5 2 + δ \frac{3-\sqrt{5}}{2}+\delta of the sets in ℱ \mathcal{F}.

To do this, in addition to considering A, B A,B two independent uniform samples from ℱ \mathcal{F}, we choose C C a uniform sample from ℱ \mathcal{F} that is not necessarily independent from A A. Since ℱ \mathcal{F} is union-closed, we have A ∪ B, A ∪ C ∈ ℱ A\cup B,A\cup C\in\mathcal{F} and thus

 | H ⁡ ( A ∪ B), H ⁡ ( A ∪ C) ≤ log ⁡ | ℱ | = H ⁡ ( A). H(A\cup B),H(A\cup C)\leq\log\absolutevalue{\mathcal F}=H(A). |  |

We will prove that if each i ∈ [n] i\in[n] is contained in A A with probability < 3 − 5 2 + δ <\frac{3-\sqrt{5}}{2}+\delta that

 | ( 1 − α) ​ H ​ ( A ∪ B) + α ​ H ​ ( A ∪ C) > H ⁡ ( A). (1-\alpha)H(A\cup B)+\alpha H(A\cup C)>H(A). |  |

This will give a contradiction and thus let us conclude some i i is contained in A A with probability ≥ 3 − 5 2 + δ \geq\frac{3-\sqrt{5}}{2}+\delta.

Let A i = 1 A_{i}=1 if i ∈ A i\in A and 0 0 if i ≠ A i\neq A, and similarly for B i B_{i} and C i C_{i}.

We describe a random process that, at the i i th step, determines A i A_{i} and C i C_{i}. Thus at the i i th step A < i A_{<i} and C < i C_{<i} are fixed. We will choose this in such a way that A A and C C are uniformly distributed on ℱ \mathcal{F}.

Let p i p_{i} be the proportion of { S ∈ ℱ ∣ S < i = C < i } \{S\in\mathcal{F}\mid S_{<i}=C_{<i}\} that contain i i and let r i r_{i} be the proportion of { S ∈ ℱ ∣ S < i = A < i } \{S\in\mathcal{F}\mid S_{<i}=A_{<i}\} that contain i i. We will choose A i A_{i} to be a random variable that is 1 1 with probability p i p_{i} and 0 0 with probability 1 − p i 1-p_{i}, and choose C i C_{i} to be 1 1 with probability r i r_{i} and 1 1 with probability 1 − r i 1-r_{i}. We will choose A i A_{i} and C i C_{i} to be correlated in a way that maximizes the conditional entropy of max ⁡ ( A i, C i) \max(A_{i},C_{i}). Specifically, if p i ≥ 1 / 2 p_{i}\geq 1/2 or r i ≥ 1 / 2 r_{i}\geq 1/2 we generate a uniformly random x ∈ [0, 1] x\in[0,1] and take A i = [x < p i] A_{i}=[x<p_{i}] and C i = [x < r i] C_{i}=[x<r_{i}] so that

 | Pr [max ( A i, C i) = 1 | A < i, C < i] = max ( p i, r i). \operatorname{Pr}[\max(A_{i},C_{i})=1|A_{<i},C_{<i}]=\max(p_{i},r_{i}). |  |

and if p i, r i < 1 / 2 p_{i},r_{i}<1/2 we generate a uniformly random x ∈ [0, 1] x\in[0,1] and take A i = [x < p i] A_{i}=[x<p_{i}] and C i = [0 ≤ 1 / 2 − x < r i] C_{i}=[0\leq 1/2-x<r_{i}], so that

 | Pr [max ( A i, C i) = 1 | A < i, C < i] = min ( p i + r i, 1 / 2). \operatorname{Pr}[\max(A_{i},C_{i})=1|A_{<i},C_{<i}]=\min(p_{i}+r_{i},1/2). |  |

Since the conditional probability that i ∈ A i\in A is p i p_{i}, the probability of getting any given sequence is the product of conditional probabilities which matches the probability when A A is uniformly distributed in ℱ \mathcal{F}. This shows A A and C C are uniformly distributed in ℱ \mathcal{F}. Letting q i = Pr ⁡ [i ∈ B | B < i] q_{i}=\operatorname{Pr}[i\in B|B_{<i}], we have

 | ( 1 − α) ​ H ​ ( ( A ∪ B) < i + 1) + α ​ H ​ ( ( A ∪ C) < i + 1) (1-\alpha)H((A\cup B)_{<i+1})+\alpha H((A\cup C)_{<i+1}) |  |

 | = ( 1 − α) ​ H ​ ( ( A ∪ B) < i) + α ​ H ​ ( ( A ∪ C) < i) + ( 1 − α) ​ H ​ ( ( A ∪ B) < i + 1 | ( A ∪ B) < i) + α ​ H ​ ( ( A ∪ C) < i + 1 | ( A ∪ C) < i) =(1-\alpha)H((A\cup B)_{<i})+\alpha H((A\cup C)_{<i})+(1-\alpha)H((A\cup B)_{<i+1}|(A\cup B)_{<i})+\alpha H((A\cup C)_{<i+1}|(A\cup C)_{<i}) |  |

 | ≥ ( 1 − α) ​ H ​ ( ( A ∪ B) < i) + α ​ H ​ ( ( A ∪ C) < i) + ( 1 − α) ​ H ​ ( ( A ∪ B) < i + 1 | A < i, B < i) + α ​ H ​ ( ( A ∪ C) < i + 1 | A < i, C < i) \geq(1-\alpha)H((A\cup B)_{<i})+\alpha H((A\cup C)_{<i})+(1-\alpha)H((A\cup B)_{<i+1}|A_{<i},B_{<i})+\alpha H((A\cup C)_{<i+1}|A_{<i},C_{<i}) |  |

 | ≥ ( 1 − α) ​ H ​ ( ( A ∪ B) < i) + α ​ H ​ ( ( A ∪ C) < i) + ( 1 − α) ​ 𝔼 ​ [H ⁡ ( p i + q i − p i ​ q i)] + α ​ E ​ [H ⁡ ( max ⁡ ( p i, r i, min ⁡ ( p i + r i, 1 / 2)))]. \geq(1-\alpha)H((A\cup B)_{<i})+\alpha H((A\cup C)_{<i})+(1-\alpha)\mathbb{E}[H(p_{i}+q_{i}-p_{i}q_{i})]+\alpha E[H(\max(p_{i},r_{i},\min(p_{i}+r_{i},1/2)))]. |  |

Thus to inductively prove the entropy bound, it suffices to prove that for p, q, r p,q,r identically distributed [0, 1] [0,1] -valued random variables with expectation ≤ 3 − 5 2 + δ \leq\frac{3-\sqrt{5}}{2}+\delta with p p and q q independent but p p and r r not necessarily independent, we have

(5) |  | ( 1 − α) ​ 𝔼 ​ [H ⁡ ( p + q − p ​ q)] + α ​ 𝔼 ​ [H ⁡ ( max ⁡ ( p, r, min ⁡ ( p + r, 1 / 2)))] > 𝔼 ⁡ [H ⁡ ( p)]. (1-\alpha)\mathbb{E}[H(p+q-pq)]+\alpha\mathbb{E}[H(\max(p,r,\min(p+r,1/2)))]>\mathbb{E}[H(p)]. |  |

We can do this by choosing α \alpha sufficiently small and δ \delta sufficiently small depending on α \alpha.

The proof of Lemma 3 shows that the only measures μ \mu on [0, 1] [0,1] with 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] ≤ 𝔼 p ∼ μ ​ [H ⁡ ( p)] \mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]\leq\mathbb{E}_{p\sim\mu}[H(p)] and expectation ≤ 3 − 5 2 \leq\frac{3-\sqrt{5}}{2} are the delta measure at the point 3 − 5 2 \frac{3-\sqrt{5}}{2} and measures supported on { 0, 1 } \{0,1\}. So any weakly convergent sequence of measures with ratio 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] / 𝔼 p ∼ μ ​ [H ⁡ ( p)] \mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]/\mathbb{E}_{p\sim\mu}[H(p)] converging to something ≤ 1 \leq 1 and expectation convergent to something ≤ 3 − 5 2 \leq\frac{3-\sqrt{5}}{2} must converge to one of those two. It can’t converge to a { 0, 1 } \{0,1\} -supported measure as measures close to that one with low expectation are easily seen to have high entropy ratio, so it must converge to the delta measure at { 3 − 5 2 } \{\frac{3-\sqrt{5}}{2}\}. It follows that for α, δ \alpha,\delta sufficiently small depending on ϵ \epsilon, any measure with 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] / 𝔼 p ∼ μ ​ [H ⁡ ( p)] ≤ 1 / ( 1 − α) \mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]/\mathbb{E}_{p\sim\mu}[H(p)]\leq 1/(1-\alpha) and expectation ≤ 𝔼 ( p, q) ∼ μ × μ ​ [H ⁡ ( p + q − p ​ q)] / 𝔼 p ∼ μ ​ [H ⁡ ( p)] + δ \leq\mathbb{E}_{(p,q)\sim\mu\times\mu}[H(p+q-pq)]/\mathbb{E}_{p\sim\mu}[H(p)]+\delta must be close to the delta measure at 3 − 5 2 \frac{3-\sqrt{5}}{2} in the sense that 𝔼 ⁡ [| p − 3 − 5 2 |] < ϵ \mathbb{E}[\absolutevalue{ p - \frac{3- \sqrt{5}}{2} }]<\epsilon.

If p p and r r are both supported on such a measure, then both p p and r r are usually close to 3 − 5 2 \frac{3-\sqrt{5}}{2}, so, regardless of how p p and r r are correlated, max ⁡ ( p, r, min ⁡ ( p + r, 1 / 2)) \max(p,r,\min(p+r,1/2)) is usually close to 1 / 2 1/2, and thus E ⁡ [H ⁡ ( max ⁡ ( p, r, min ⁡ ( p + r, 1 / 2)))] / 𝔼 ⁡ [H ⁡ ( p)] E[H(\max(p,r,\min(p+r,1/2)))]/\mathbb{E}[H(p)] is close to H ⁡ ( 1 / 2) / H ⁡ ( 3 − 5 2) > 1 H(1/2)/H(\frac{3-\sqrt{5}}{2})>1. We can choose δ \delta close enough to 0 0, depending on α \alpha, that 𝔼 ⁡ [H ⁡ ( p + q − p ​ q)] / 𝔼 ⁡ [H ⁡ ( p)] \mathbb{E}[H(p+q-pq)]/\mathbb{E}[H(p)] is sufficiently close to 1 1 to ensure that ( 5) is satisfied.

It would be interesting to modify this argument to obtain an explicit value of δ \delta.

Motivated by this argument, we raise the question:

###### Question 9.

For any probability measure μ \mu on subsets of [n] [n], with nonzero entropy, such that μ ⁡ ( { A ⊆ [n] ∣ i ∈ A }) < 1 / 2 \mu(\{A\subseteq[n]\mid i\in A\})<1/2 for all i ∈ [n] i\in[n], do there exist random variables A, B A,B, identically distributed with measure μ \mu but not necessarily independent, such that H ⁡ ( A ∪ B) > H ⁡ ( A) H(A\cup B)>H(A)?

A positive answer would imply the union-closed conjecture.

## References

- [1] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for Frankl’s union-closed sets conjecture. [arxiv:2211.11731][1], 2022.
- [2] Ravi B. Bopanna. A Useful Inequality for the Binary Entropy Function. [arxiv:2301.09664][2], 2023.
- [3] Zachary Chase and Shachar Lovett. Approximate union closed conjecture. [arxiv:2211.11689][3], 2022.
- [4] David Ellis. Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture. [arxiv:2211.12401][4], 2022.
- [5] Emanuel Knill. Graph generated union-closed families of sets. [math/9409215][5], 1994
- [6] Justin Gilmer. A constant lower bound for the union-closed sets conjecture. [arxiv:2211.09055][6], 2022.
- [7] Piotr Wójcik. Union-closed families of sets. *Discrete Mathematics*, 199 (1-3):173–182, 1999.

[◄][7][image: ar5iv homepage] [8]
[Feeling lucky?][9] [10]
[Conversion report][11]
[Report an issue][12]
[View original on arXiv][13] [►][14]


## Links

[1]: https:///arxiv.org/abs/2211.11731
[2]: https://arxiv.org/pdf/2301.09664
[3]: https://arxiv/abs/2211.11689
[4]: https://arxiv.org/pdf/2211.12401
[5]: https://arxiv.org/pdf/math/9409215
[6]: https://arxiv.org/pdf/2211.09055
[7]: /html/2211.11503
[8]: /
[9]: /feeling_lucky
[10]: /land_of_honey_and_milk
[11]: /log/2211.11504
[12]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2211.11504
[13]: https://arxiv.org/pdf/2211.11504
[14]: /html/2211.11505
