<!-- source: https://arxiv.org/html/2302.12276v1 | converted from HTML -->

Almost k -union closed set systems

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2302.12276v1 [math.CO] 23 Feb 2023

# Almost k k -union closed set systems

Raphael Yuster Thanks: Department of Mathematics, University of Haifa, Haifa 3498838, Israel. Email: raphael.yuster@gmail.com .

###### Abstract

In a recent breakthrough, Gilmer proved the union closed conjecture up to a constant factor. Using Gilmer’s method and additional ideas, Chase and Lovett proved an optimal result for almost union-closed set systems. Here that result is extended to higher order unions.

## 1 Introduction

In a recent breakthrough, Gilmer [8] established the well-known Frankl’s union closed conjecture up to a constant factor. Shortly after, that factor has been improved by several authors, pushing Gilmer’s method to 3 − 5 2 ≈ 0.3819 \frac{3-\sqrt{5}}{2}\approx 0.3819 [2, 6, 9, 10]. A variation of Gilmer’s method improved the constant slightly to ≈ 0.3824 \approx 0.3824 [5, 10, 11]. Additional ideas may be needed to push the bound further [5, 7, 10]. Interestingly, 3 − 5 2 \frac{3-\sqrt{5}}{2} has been shown by Chase and Lovett [6] to be the optimal constant for the approximate version of the union closed conjecture. Here we show that the method of Gilmer, and the result of Chase and Lovett, can be extended to the approximate version for higher order unions.

###### Definition 1.1 (Approximate k k -union closed set system).

Let k ≥ 2 k\geq 2 be an integer and let 0 ≤ c ≤ 1 0\leq c\leq 1. A finite set system ℱ {\mathcal{F}} is c c -approximate k k -union closed if for at least a c c -fraction of the k k -tuples A 1, …, A k ∈ ℱ A_{1},\ldots,A_{k}\in{\mathcal{F}} we have ∪ i = 1 k A i ∈ ℱ \cup_{i=1}^{k}A_{i}\in{\mathcal{F}}.

Following Chase and Lovett, we say (informally) that ℱ {\mathcal{F}} is almost k k -union closed (or almost union-closed when k = 2 k=2) if it is 1 − o ⁡ ( 1) 1-o(1) approximate k k -union closed. Observe also that if c = 1 c=1 in Definition 1.1, then ℱ {\mathcal{F}} is already union closed, but being almost k k -union closed is a considerably weaker requirement than being union closed, and different from being almost k ′ k^{\prime} -union closed for k ′ ≠ k k^{\prime}\neq k.

The union closed conjecture asserts that in any finite union-closed set system ℱ ≠ { ∅ } {\mathcal{F}}\neq\{\emptyset\} (i.e., nontrivial set systems corresponding to k = 2 k=2 and c = 1 c=1 in Definition 1.1), there exists an element that belongs to at least half of the sets in ℱ {\mathcal{F}}. Gilmer [8] proved this holds for ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]} with the constant 0.01 0.01 instead of 1 2 \frac{1}{2}. Let ψ = 3 − 5 2 ≈ 0.3819 \psi=\frac{3-\sqrt{5}}{2}\approx 0.3819; Gilmer conjectured that the method in [8] can yield the constant ψ \psi. As mentioned earlier, this was proved shortly after by several researchers. In fact, Chase and Lovett [6] proved that ψ \psi is the optimal constant for almost union-closed set systems.

###### Theorem 1.2 ( [6]).

Let ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, ℱ ≠ { ∅ } {\mathcal{F}}\neq\{\emptyset\} be a ( 1 − ε) (1-{\varepsilon}) -approximate union closed set system, where 0 ≤ ε < 1 2 0\leq{\varepsilon}<\frac{1}{2}. Then there is an element contained in a ψ − δ \psi-\delta fraction of sets in ℱ {\mathcal{F}}, where δ = 2 ​ ε ​ ( 1 + log ⁡ 1 ϵ / log ⁡ | ℱ |) \delta=2{\varepsilon}\left(1+\log\frac{1}{\epsilon}/{\log|{\mathcal{F}}|}\right). Moreover, for every n n, there exists such an ℱ {\mathcal{F}} which is 1 − o n ​ ( 1) 1-o_{n}(1) approximate union closed and in which every element is contained in at most ψ + o n ​ ( 1) \psi+o_{n}(1) sets.

As we shall see, Theorem 1.7 below implies the following theorem:

###### Theorem 1.3.

Let ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, ℱ ≠ { ∅ } {\mathcal{F}}\neq\{\emptyset\} be a ( 1 − ε) (1-{\varepsilon}) -approximate k k -union closed set system, where 0 ≤ ε < 1 2 0\leq{\varepsilon}<\frac{1}{2}. Then there is an element contained in a ln ⁡ k 3 ​ k − δ \frac{\ln k}{3k}-\delta fraction of sets in ℱ {\mathcal{F}}, where δ = ( k ​ ε + 2 ​ ε ​ log ⁡ 1 ϵ / log ⁡ | ℱ |) 1 / ( k − 1) \delta=\left(k{\varepsilon}+2{\varepsilon}\log\frac{1}{\epsilon}/\log|{\mathcal{F}}|\right)^{1/(k-1)}.

Let ψ k \psi_{k} be the unique real root of ( 1 − x) k − x (1-x)^{k}-x in [0, 1] [0,1] (so ψ = ψ 2 \psi=\psi_{2}). The construction used to prove the second part of Theorem 1.2 generalizes to almost k k -union closed set systems.

###### Proposition 1.4.

Let k ≥ 2 k\geq 2 be an integer. For every n n, there exists ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, ℱ ≠ { ∅ } {\mathcal{F}}\neq\{\emptyset\} such that ℱ {\mathcal{F}} is 1 − o n ​ ( 1) 1-o_{n}(1) approximate k k -union closed, while every element is contained in at most ψ k + o n ​ ( 1) \psi_{k}+o_{n}(1) sets.

The following conjecture asserts that the first part of Theorem 1.2 also generalizes to almost k k -union closed set systems.

###### Conjecture 1.5.

Let ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, ℱ ≠ { ∅ } {\mathcal{F}}\neq\{\emptyset\} be a ( 1 − ε) (1-{\varepsilon}) -approximate k k -union closed set system, where 0 ≤ ε < 1 2 0\leq{\varepsilon}<\frac{1}{2}. Then there is an element contained in a ψ k − δ \psi_{k}-\delta fraction of sets in ℱ {\mathcal{F}}, where δ = ( k ​ ε + 2 ​ ε ​ log ⁡ 1 ϵ / log ⁡ | ℱ |) 1 / ( k − 1) \delta=\left(k{\varepsilon}+2{\varepsilon}\log\frac{1}{\epsilon}/\log|{\mathcal{F}}|\right)^{1/(k-1)}.

Theorem 1.2 is the case k = 2 k=2 of Conjecture 1.5. We prove the next few cases of Conjecture 1.5.

###### Theorem 1.6.

Conjecture 1.5 holds for k = 3, 4 k=3,4.

We next prove a variant of Conjecture 1.5 for all k k where instead of ψ k \psi_{k}, we use a smaller constant. Moreover, that constant is close to ψ k \psi_{k} in the sense made precise in the following theorem (see Table 1 for a comparison of z k z_{k} and ψ k \psi_{k} for small k k).

###### Theorem 1.7.

Conjecture 1.5 holds with the constant z k z_{k} instead of ψ k \psi_{k} where

 | z k > ln ⁡ k 3 ​ k, 1 2 < z k ψ k ≤ 1, lim k → ∞ z k ψ k = log ⁡ 1 φ log ⁡ 2 ≈ 0.6943. z_{k}>\frac{\ln k}{3k}\;,\qquad\frac{1}{2}<\frac{z_{k}}{\psi_{k}}\leq 1\;,\qquad\lim_{k\rightarrow\infty}\frac{z_{k}}{\psi_{k}}=\frac{\log\frac{1}{\varphi}}{\log 2}\approx 0.6943\;. |  |

An important ingredient in the proof of Theorem 1.2 is a generalization of an inequality stated by Boppana [3] concerning the minimum of some function in [0, 1] [0,1] related to binary entropy. This inequality was proved by Boppana [4] and by Alweiss, Huang, and Sellke [2]. Though technical, this generalization can be proved rigorously for k = 3, 4 k=3,4, while for larger k k, it can be shown to reduce Conjecture 1.5 to a conjecture about roots of certain real polynomials. Assuming this generalization, the arguments of Gilmer and of Chase and Lovett can be rather smoothly generalized to yield Theorems 1.6 and 1.7.

We proceed to prove Proposition 1.4 in Section 2. Section 3 considers the generalization of the aforementioned inequality of Boppana, proving certain properties related to it. These properties are then used in Section 4 to prove a multidimensional version of the Chase-Lovett main lemma and consequently in Section 5 to prove Theorems 1.6 and 1.7.

## 2 The generalized construction

###### Proof of Proposition 1.4.

The construction is a generalization of the one used by Chase and Lovett [6]. Define the following set systems over [n] [n]:

 | ℱ 1 = { x ∈ { 0, 1 } n: | x | = ⌊ ψ k ​ n + n 2 / 3 ⌋ }, ℱ 2 = { x ∈ { 0, 1 } n: | x | ≥ ⌊ ( 1 − ψ k) ​ n ⌋ } {\mathcal{F}}_{1}=\{x\in\{0,1\}^{n}\,:\,|x|=\lfloor\psi_{k}n+n^{2/3}\rfloor\},\quad{\mathcal{F}}_{2}=\{x\in\{0,1\}^{n}\,:\,|x|\geq\lfloor(1-\psi_{k})n\rfloor\} |  |

and let ℱ = ℱ 1 ∪ ℱ 2 {\mathcal{F}}={\mathcal{F}}_{1}\cup{\mathcal{F}}_{2}. As ψ k < 1 2 \psi_{k}<\frac{1}{2}, we obtain that | ℱ 2 | = o n ​ ( | ℱ 1 |) |{\mathcal{F}}_{2}|=o_{n}(|{\mathcal{F}}_{1}|). Clearly, each element is in a ψ k + o n ​ ( 1) \psi_{k}+o_{n}(1) fraction of the sets ℱ 1 {\mathcal{F}}_{1}, hence ℱ {\mathcal{F}}. Finally, with probability 1 − o n ​ ( 1) 1-o_{n}(1), a randomly chosen k k -tuple of sets of ℱ 1 {\mathcal{F}}_{1} almost surely has more than n ⁡ ( ∑ j = 1 k ( − 1) j − 1 ​ ( k j) ​ ψ k j) = n ⁡ ( 1 − ψ k) n(\sum_{j=1}^{k}(-1)^{j-1}\binom{k}{j}\psi_{k}^{j})=n(1-\psi_{k}) elements where we have used ( 1 − ψ k) k = ψ k (1-\psi_{k})^{k}=\psi_{k}. Consequently, a randomly chosen k k -tuple of sets of ℱ {\mathcal{F}} is almost surely in ℱ {\mathcal{F}}, so ℱ {\mathcal{F}} is 1 − o n ​ ( 1) 1-o_{n}(1) approximate k k -union closed. ∎

## 3 An inequality concerning binary entropy

Recall that ψ k \psi_{k} denotes the unique real root of ( 1 − x) k − x (1-x)^{k}-x in [0, 1] [0,1]. Let

 | φ k ≔ 1 − ψ k, α k ≔ φ k k − 1 = 1 φ k − 1 = ψ k φ k. \varphi_{k}\coloneqq 1-\psi_{k}\,,\qquad\alpha_{k}\coloneqq{\varphi_{k}}^{k-1}=\frac{1}{\varphi_{k}}-1=\frac{\psi_{k}}{\varphi_{k}}\,. |  | (1) |

k k | φ k \varphi_{k} | ψ k \psi_{k} | z k z_{k} | α k \alpha_{k} |

2 2 | 0.6180 0.6180 | 0.3819 0.3819 | 0.3819 0.3819 | 0.6180 0.6180 |

3 3 | 0.6823 0.6823 | 0.3176 0.3176 | 0.3176 0.3176 | 0.4655 0.4655 |

4 4 | 0.7244 0.7244 | 0.2755 0.2755 | 0.2755 0.2755 | 0.3802 0.3802 |

5 5 | 0.7548 0.7548 | 0.2451 0.2451 | 0.2416 0.2416 | 0.3247 0.3247 |

6 6 | 0.7780 0.7780 | 0.2219 0.2219 | 0.2183 0.2183 | 0.2851 0.2851 |

7 7 | 0.7965 0.7965 | 0.2034 0.2034 | 0.2006 0.2006 | 0.2554 0.2554 |

8 8 | 0.8116 0.8116 | 0.1883 0.1883 | 0.1863 0.1863 | 0.2319 0.2319 |

16 16 | 0.8771 0.8771 | 0.1228 0.1228 | 0.1204 0.1204 | 0.1400 0.1400 |

Table 1: The values of φ k, ψ k, z k, α k \varphi_{k},\psi_{k},z_{k},\alpha_{k} for several k k, listed with precision 10 − 4 10^{-4}.

Some values of these parameters are given in Table 1.

Throughout this paper, all logarithms are natural. Let h ⁡ ( x) = − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) h(x)=-x\log x-(1-x)\log(1-x) be the binary entropy function defined continuously in [0, 1] [0,1] by h ⁡ ( 0) = h ⁡ ( 1) = 0 h(0)=h(1)=0. As in [3], it will be convenient to extend h ⁡ ( x) h(x) (continuously) to ℝ {\mathbb{R}} as follows:

 | h ⁡ ( x) ≔ { − x ​ log ⁡ | x | − ( 1 − x) ​ log ⁡ | 1 − x | if ​ x ∈ ℝ ∖ { 0, 1 }; 0 if ​ x ∈ { 0, 1 }. h(x)\coloneqq\begin{cases}-x\log|x|-(1-x)\log|1-x|&{\rm if}~~x\in{\mathbb{R}}\setminus\{0,1\}\,;\\ 0&{\rm if}~~x\in\{0,1\}\,.\end{cases} |  |

For k ≥ 2 k\geq 2, let r k ​ ( x) r_{k}(x), s k ​ ( x) s_{k}(x) and f k ​ ( x) f_{k}(x) be the functions with domain ℝ {\mathbb{R}} defined as:

 | r k ​ ( x) ≔ h ⁡ ( x k), s k ​ ( x) ≔ x k − 1 ​ h ​ ( x), f k ​ ( x) ≔ α k ​ r k ​ ( x) − s k ​ ( x). r_{k}(x)\coloneqq h(x^{k})\,,\qquad s_{k}(x)\coloneqq x^{k-1}h(x)\,,\qquad f_{k}(x)\coloneqq\alpha_{k}r_{k}(x)-s_{k}(x)\,. |  | (2) |

In [2, 4] it is proved that f 2 ​ ( x) f_{2}(x) is nonnegative on [0, 1] [0,1]. The proof in [4] uses only differential calculus and the proof in [2] uses both differential calculus and interval arithmetic.

###### Conjecture 3.1.

f k ​ ( x) f_{k}(x) is nonnegative on [0, 1] [0,1].

As we shall see in the following sections, Conjecture 1.5 reduces to Conjecture 3.1. Being non-parameterized, it seems hopeless to extend the interval arithmetic part of the proof in [2] to general k k. On the other hand, as [4] uses only differential calculus, it may not be hopeless to extend its proof to arbitrary k k. In fact, we manage to do so completely rigorously for k = 3, 4 k=3,4. The next several lemmata prove properties of f k ​ ( x) f_{k}(x), valid for all k k.

###### Lemma 3.2.

f k ​ ( 0) = f k ​ ( 1) = f k ​ ( φ k) = f k ′ ​ ( φ k) = 0 f_{k}(0)=f_{k}(1)=f_{k}(\varphi_{k})=f_{k}^{\prime}(\varphi_{k})=0.

###### Proof.

By assignment, f k ​ ( 0) = f k ​ ( 1) = 0 f_{k}(0)=f_{k}(1)=0. We verify the remaining claims:

 | f k ​ ( φ k) = α k ​ h ​ ( φ k k) − α k ​ h ​ ( φ k) = α k ​ ( h ⁡ ( 1 − φ k) − h ⁡ ( φ k)) = 0. f_{k}(\varphi_{k})=\alpha_{k}h({\varphi_{k}}^{k})-\alpha_{k}h(\varphi_{k})=\alpha_{k}(h(1-\varphi_{k})-h(\varphi_{k}))=0\,. |  |

For x ∈ ( 0, 1) x\in(0,1) we have

 | f k ′ ​ ( x) = α k ​ k ​ x k − 1 ​ log ⁡ ( x − k − 1) − x k − 2 ​ ( ( k ⁡ ( x − 1) + 1) ​ log ⁡ ( 1 − x) − k ​ x ​ log ⁡ x) f_{k}^{\prime}(x)=\alpha_{k}kx^{k-1}\log(x^{-k}-1)-x^{k-2}((k(x-1)+1)\log(1-x)-kx\log x) |  |

so we must prove that α k ​ k ​ x ​ log ⁡ ( x − k − 1) − ( k ⁡ ( x − 1) + 1) ​ log ⁡ ( 1 − x) + k ​ x ​ log ⁡ x \alpha_{k}kx\log(x^{-k}-1)-(k(x-1)+1)\log(1-x)+kx\log x vanishes at x = φ k x=\varphi_{k}. Indeed, substituting x x with φ k \varphi_{k} in the last expression we obtain

 |  | k ​ α k ​ φ k ​ log ⁡ ( φ k − k − 1) − ( k ⁡ ( φ k − 1) + 1) ​ log ⁡ ( 1 − φ k) + k ​ φ k ​ log ⁡ φ k \displaystyle\;k\alpha_{k}\varphi_{k}\log({\varphi_{k}}^{-k}-1)-(k(\varphi_{k}-1)+1)\log(1-\varphi_{k})+k\varphi_{k}\log\varphi_{k} |  |

 | = \displaystyle= | k ⁡ ( 1 − φ k) ​ ( log ⁡ φ k − log ⁡ ( 1 − φ k)) − ( k ⁡ ( φ k − 1) + 1) ​ log ⁡ ( 1 − φ k) + k ​ φ k ​ log ​ φ k \displaystyle\;k(1-\varphi_{k})(\log{\varphi_{k}}-\log(1-{\varphi_{k}}))-(k(\varphi_{k}-1)+1)\log(1-\varphi_{k})+k\varphi_{k}\log\varphi_{k} |  |

 | = \displaystyle= | k ​ log ⁡ φ k − log ⁡ ( 1 − φ k) \displaystyle\;k\log\varphi_{k}-\log(1-\varphi_{k}) |  |

 | = \displaystyle= | log ⁡ ( 1 − φ k) − log ⁡ ( 1 − φ k) \displaystyle\;\log(1-\varphi_{k})-\log(1-\varphi_{k}) |  |

 | = \displaystyle= | 0. \displaystyle\;0\,. |  |

∎

###### Lemma 3.3.

f k ​ ( x) f_{k}(x) is positive in ( 0, ε) (0,{\varepsilon}) for some small ε > 0 {\varepsilon}>0.

###### Proof.

The Taylor expansion of log ⁡ ( 1 − ε) \log(1-{\varepsilon}) gives that for all ε ∈ ( 0, 1) {\varepsilon}\in(0,1),

 | ε ⁡ ( log ⁡ 1 ε + 1 − ε) ≤ h ⁡ ( ε) ≤ ε ⁡ ( log ⁡ 1 ε + 1). {\varepsilon}\left(\log\frac{1}{{\varepsilon}}+1-{\varepsilon}\right)\leq h({\varepsilon})\leq{\varepsilon}\left(\log\frac{1}{{\varepsilon}}+1\right)\,. |  |

We therefore have

 | α k ​ r k ​ ( ϵ) \displaystyle\alpha_{k}r_{k}(\epsilon) | = α k ​ h ​ ( ε k) ≥ α k ​ ε k ​ ( log ⁡ 1 ε k + 1 − ε k); \displaystyle=\alpha_{k}h({\varepsilon}^{k})\geq\alpha_{k}{\varepsilon}^{k}\left(\log\frac{1}{{\varepsilon}^{k}}+1-{\varepsilon}^{k}\right); |  |

 | s k ​ ( ϵ) \displaystyle s_{k}(\epsilon) | = ε k − 1 ​ h ​ ( ε) ≤ ε k ​ ( log ⁡ 1 ε + 1). \displaystyle={\varepsilon}^{k-1}h({\varepsilon})\leq{\varepsilon}^{k}\left(\log\frac{1}{{\varepsilon}}+1\right). |  |

Dividing both inequalities by ε k {\varepsilon}^{k} it remains to prove that for small ε > 0 {\varepsilon}>0,

 | α k ​ ( log ⁡ 1 ε k + 1 − ε k) > ( log ⁡ 1 ε + 1). \alpha_{k}\left(\log\frac{1}{{\varepsilon}^{k}}+1-{\varepsilon}^{k}\right)>\left(\log\frac{1}{{\varepsilon}}+1\right)\,. |  |

Equivalently, we must show that for small ε > 0 {\varepsilon}>0,

 | α k > log ⁡ 1 ε + 1 k ​ log ⁡ 1 ε + 1 − ε k. \alpha_{k}>\frac{\log\frac{1}{{\varepsilon}}+1}{k\log\frac{1}{{\varepsilon}}+1-{\varepsilon}^{k}}\;. |  |

Since α k = 1 φ k − 1 \alpha_{k}=\frac{1}{\varphi_{k}}-1 it suffices to show that for small ε > 0 {\varepsilon}>0,

 | φ k < k ​ log ⁡ 1 ε + 1 − ε k ( k + 1) ​ log ⁡ 1 ε + 2 − ε k. \varphi_{k}<\frac{k\log\frac{1}{{\varepsilon}}+1-{\varepsilon}^{k}}{(k+1)\log\frac{1}{{\varepsilon}}+2-{\varepsilon}^{k}}\;. |  |

We will show the stronger statement that for small ε > 0 {\varepsilon}>0,

 | φ k < k ​ log ⁡ 1 ε ( k + 1) ​ log ⁡ 1 ε + 2. \varphi_{k}<\frac{k\log\frac{1}{{\varepsilon}}}{(k+1)\log\frac{1}{{\varepsilon}}+2}\;. |  |

Indeed, notice that since ( 1 − 1 / ( k + 1)) k > 1 / ( k + 1) (1-1/(k+1))^{k}>1/(k+1), we have that φ k < k / ( k + 1) \varphi_{k}<k/(k+1), so for some 0 < δ < 1 0<\delta<1 we have φ k = δ ​ k / ( k + 1) \varphi_{k}=\delta k/(k+1). We may therefore choose ε > 0 {\varepsilon}>0 sufficiently small such that

 | k ​ log ⁡ 1 ε ( k + 1) ​ log ⁡ 1 ε + 2 > δ ​ k k + 1 = φ k. \frac{k\log\frac{1}{{\varepsilon}}}{(k+1)\log\frac{1}{{\varepsilon}}+2}>\frac{\delta k}{k+1}=\varphi_{k}\;. |  |

∎

The derivatives of h ⁡ ( x) h(x) in ( − 1, 1) ∖ { 0 } (-1,1)\setminus\{0\} are required for the next two lemmas. By induction, it holds that:

 | h ′ ​ ( x) \displaystyle h^{\prime}(x) | = log ⁡ ( 1 − x | x |); \displaystyle=\log\left(\frac{1-x}{|x|}\right); |  | (3) |

 | h ( t) ​ ( x) \displaystyle h^{(t)}(x) | = ( t − 2)! ​ ( − 1) t ​ ( 1 ( x − 1) t − 1 − 1 x t − 1) ​ for ​ all ​ t ≥ 2. \displaystyle=(t-2)!(-1)^{t}\left(\frac{1}{(x-1)^{t-1}}-\frac{1}{x^{t-1}}\right)~{\rm for~all}~t\geq 2\;. |  | (4) |

###### Lemma 3.4.

Let t ≥ 0 t\geq 0.
(i) The t t ’th derivative of s k ​ ( x) s_{k}(x) in ( − 1, 1) ∖ { 0 } (-1,1)\setminus\{0\} is

 | s k ​ ( x) ( t) = ∑ j = 0 t h ( j) ​ ( x) ​ ( k − 1 t − j) ​ t! j! ​ x k − t + j − 1. s_{k}(x)^{(t)}=\sum_{j=0}^{t}h^{(j)}(x)\binom{k-1}{t-j}\frac{t!}{j!}x^{k-t+j-1}\;. |  |

(ii) For all 0 ≤ t ≤ k − 1 0\leq t\leq k-1, s k ​ ( 0) ( t) = 0 s_{k}(0)^{(t)}=0.
(iii) s k ​ ( x) ( k + 1) s_{k}(x)^{(k+1)} is a rational function in ( 0, 1) (0,1) given by:

 | s k ​ ( x) ( k + 1) \displaystyle s_{k}(x)^{(k+1)} | = ∑ j = 0 k − 1 ( − 1) j ​ ( k − 1)! ​ ( k + 1 j + 2) ​ ( x j + 1 − ( x − 1) j + 1 x ​ ( x − 1) j + 1). \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}(k-1)!\binom{k+1}{j+2}\left(\frac{x^{j+1}-(x-1)^{j+1}}{x(x-1)^{j+1}}\right). |  |

###### Proof.

Recall that s k ​ ( x) = x k − 1 ​ h ​ ( x) s_{k}(x)=x^{k-1}h(x) so (i) is obtained directly by induction and the product rule.

As for (ii), notice first that s k ​ ( 0) = 0 s_{k}(0)=0. Now, suppose 1 ≤ t ≤ k − 1 1\leq t\leq k-1, and consider the limit of (i) as x x goes to 0 0. We compute this limit for each term j j separately. The term corresponding to j = 0 j=0 is just a constant multiple of h ⁡ ( x) ​ x k − t − 1 h(x)x^{k-t-1} so it goes to 0 0. By ( 3), the term corresponding to j = 1 j=1 is a constant multiple of

 | log ⁡ ( 1 − x | x |) ​ x k − t \log\left(\frac{1-x}{|x|}\right)x^{k-t} |  |

and since k − t > 0 k-t>0, it goes to zero. By ( 4), the term corresponding to 2 ≤ j ≤ t 2\leq j\leq t is a constant multiple of

 | ( 1 ( x − 1) j − 1 − 1 x j − 1) ​ x k − t + j − 1 = x k − t + j − 1 ( x − 1) j − 1 − x k − t \left(\frac{1}{(x-1)^{j-1}}-\frac{1}{x^{j-1}}\right)x^{k-t+j-1}=\frac{x^{k-t+j-1}}{(x-1)^{j-1}}-x^{k-t} |  |

and since k − t > 0 k-t>0, it goes to zero as well.

As for (iii), observe that by (i), the terms involving h ⁡ ( x) h(x) and h ′ ​ ( x) h^{\prime}(x) vanish, so we are left with a rational function, explicitly given by

 | s k ​ ( x) ( k + 1) \displaystyle s_{k}(x)^{(k+1)} | = ∑ j = 0 k − 1 h ( j + 2) ​ ( x) ​ ( k − 1 k − 1 − j) ​ ( k + 1)! ( j + 2)! ​ x j \displaystyle=\sum_{j=0}^{k-1}h^{(j+2)}(x)\binom{k-1}{k-1-j}\frac{(k+1)!}{(j+2)!}x^{j} |  |

 |  | = ∑ j = 0 k − 1 ( − 1) j ​ j! ​ ( 1 ( x − 1) j + 1 − 1 x j + 1) ​ ( k − 1 k − 1 − j) ​ ( k + 1)! ( j + 2)! ​ x j \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}j!\left(\frac{1}{(x-1)^{j+1}}-\frac{1}{x^{j+1}}\right)\binom{k-1}{k-1-j}\frac{(k+1)!}{(j+2)!}x^{j} |  |

 |  | = ∑ j = 0 k − 1 ( − 1) j ​ ( k − 1)! ​ ( k + 1 j + 2) ​ ( x j + 1 − ( x − 1) j + 1 x ​ ( x − 1) j + 1). \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}(k-1)!\binom{k+1}{j+2}\left(\frac{x^{j+1}-(x-1)^{j+1}}{x(x-1)^{j+1}}\right)\;. |  |

∎

###### Lemma 3.5.

Let t ≥ 0 t\geq 0.
(i) The t t ’th derivative of r k ​ ( x) r_{k}(x) in ( − 1, 1) ∖ { 0 } (-1,1)\setminus\{0\} is

 | r k ​ ( x) ( t) = ∑ j = 0 t ( k − 1)! ​ C ​ ( k, t, j) ​ h ( j) ​ ( x k) ​ x k ​ j − t r_{k}(x)^{(t)}=\sum_{j=0}^{t}(k-1)!C(k,t,j)h^{(j)}(x^{k})x^{kj-t} |  |

where the coefficient C ⁡ ( k, t, j) C(k,t,j) satisfies C ⁡ ( k, 0, 0) = 1 / ( k − 1)! C(k,0,0)=1/(k-1)!, otherwise C ⁡ ( k, t, j) = 0 C(k,t,j)=0 if t ⋅ j = 0 t\cdot j=0 and otherwise

 | C ⁡ ( k, t, j) = ( k ​ j − t + 1) ​ C ​ ( k, t − 1, j) + k ​ C ​ ( k, t − 1, j − 1). C(k,t,j)=(kj-t+1)C(k,t-1,j)+kC(k,t-1,j-1)\;. |  |

(ii) For all 0 ≤ t ≤ k − 1 0\leq t\leq k-1, r k ​ ( 0) ( t) = 0 r_{k}(0)^{(t)}=0.
(iii) r k ​ ( x) ( k + 1) r_{k}(x)^{(k+1)} is a rational function in ( 0, 1) (0,1) given by:

 | r k ​ ( x) ( k + 1) \displaystyle r_{k}(x)^{(k+1)} | = ∑ j = 0 k − 1 ( − 1) j ​ j! ​ ( k − 1)! ​ C ​ ( k, k + 1, j + 2) ​ ( x k ​ j + k − ( x k − 1) j + 1 x ​ ( x k − 1) j + 1). \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}j!(k-1)!C(k,k+1,j+2)\left(\frac{x^{kj+k}-(x^{k}-1)^{j+1}}{x(x^{k}-1)^{j+1}}\right). |  |

###### Proof.

Recall that r k ​ ( x) = h ⁡ ( x k) r_{k}(x)=h(x^{k}) so (i) is obtained directly by induction, the product rule, and the definition of the coefficients C ⁡ ( k, t, j) C(k,t,j). We note that there is no simple “sum-free” expression in the general case of C ⁡ ( k, t, j) C(k,t,j) (e.g., ( k − 1)! ​ C ​ ( k, 6, 2) = k 2 ​ ( k − 1) ​ ( k − 2) ​ ( 31 ​ k 2 − 132 ​ k + 137) (k-1)!C(k,6,2)=k^{2}(k-1)(k-2)(31k^{2}-132k+137)), but notice that we do have that for all 1 ≤ t ≤ k 1\leq t\leq k,

 | C ⁡ ( k, t, 1) = k ( k − t)! C(k,t,1)=\frac{k}{(k-t)!} |  |

and hence C ⁡ ( k, t, 1) = 0 C(k,t,1)=0 for all t > k t>k. Also notice that since C ⁡ ( k, t, j) = 0 C(k,t,j)=0 when exactly one of t t or j j is zero, we inductively have that when 0 ≤ t < j 0\leq t<j,

 | C ⁡ ( k, t, j) = 0. C(k,t,j)=0\;. |  |

As for (ii), notice first that r k ​ ( 0) = 0 r_{k}(0)=0. Now, suppose 1 ≤ t ≤ k − 1 1\leq t\leq k-1, and consider the limit of (i) as x x goes to 0 0. We compute this limit for each term j j separately. The term corresponding to j = 0 j=0 is just 0 0. By ( 3), the term corresponding to j = 1 j=1 is a constant multiple of

 | log ⁡ ( 1 − x k | x k |) ​ x k − t \log\left(\frac{1-x^{k}}{|x^{k}|}\right)x^{k-t} |  |

and since k − t > 0 k-t>0, it goes to zero. By ( 4), the term corresponding to 2 ≤ j ≤ t 2\leq j\leq t is a constant multiple of

 | ( 1 ( x k − 1) j − 1 − 1 x k ​ j − k) ​ x k ​ j − t = x k ​ j − t ( x k − 1) j − 1 − x k − t \left(\frac{1}{(x^{k}-1)^{j-1}}-\frac{1}{x^{kj-k}}\right)x^{kj-t}=\frac{x^{kj-t}}{(x^{k}-1)^{j-1}}-x^{k-t} |  |

and since k − t > 0 k-t>0, it goes to zero as well.

As for (iii), observe that by (i), and since C ⁡ ( k, t, 1) = 0 C(k,t,1)=0 for all t > k t>k, we see that in r k ​ ( x) ( k + 1) r_{k}(x)^{(k+1)}, the terms involving h ⁡ ( x) h(x) and h ′ ​ ( x) h^{\prime}(x) vanish, so we are left with a rational function explicitly given by

 | r k ​ ( x) ( k + 1) \displaystyle r_{k}(x)^{(k+1)} | = ∑ j = 0 k − 1 h ( j + 2) ​ ( x k) ​ ( k − 1)! ​ C ​ ( k, k + 1, j + 2) ​ x k ​ j + k − 1 \displaystyle=\sum_{j=0}^{k-1}h^{(j+2)}(x^{k})(k-1)!C(k,k+1,j+2)x^{kj+k-1} |  |

 |  | = ∑ j = 0 k − 1 ( − 1) j ​ j! ​ ( 1 ( x k − 1) j + 1 − 1 x k ​ j + k) ​ ( k − 1)! ​ C ​ ( k, k + 1, j + 2) ​ x k ​ j + k − 1 \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}j!\left(\frac{1}{(x^{k}-1)^{j+1}}-\frac{1}{x^{kj+k}}\right)(k-1)!C(k,k+1,j+2)x^{kj+k-1} |  |

 |  | = ∑ j = 0 k − 1 ( − 1) j ​ j! ​ ( k − 1)! ​ C ​ ( k, k + 1, j + 2) ​ ( x k ​ j + k − ( x k − 1) j + 1 x ​ ( x k − 1) j + 1). \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}j!(k-1)!C(k,k+1,j+2)\left(\frac{x^{kj+k}-(x^{k}-1)^{j+1}}{x(x^{k}-1)^{j+1}}\right). |  |

∎

The following corollary is immediate from Lemma 3.4 item (ii) and Lemma 3.5 item (ii).

###### Corollary 3.6.

f k ​ ( x) f_{k}(x) has a root of multiplicity k k at x = 0 x=0.

The following corollary follows from Lemma 3.4 item (iii) and Lemma 3.5 item (iii).

###### Corollary 3.7.

The ( k + 1) (k+1) ’th derivative of f k ​ ( x) f_{k}(x) in ( 0, 1) (0,1) is a rational function of the form ( k − 1)! ​ p k ​ ( x) / ( x ​ ( x k − 1) k) (k-1)!p_{k}(x)/(x(x^{k}-1)^{k}) where p ⁡ ( x) p(x) is a polynomial of degree k 2 − 1 k^{2}-1 given by

 | p k ​ ( x) = α k ​ ρ k ​ ( x) − σ k ​ ( x) p_{k}(x)=\alpha_{k}\rho_{k}(x)-\sigma_{k}(x) |  |

where

 | ρ k ​ ( x) \displaystyle\rho_{k}(x) | = ∑ j = 0 k − 1 ( − 1) j ​ j! ​ C ​ ( k, k + 1, j + 2) ​ ( ( x k − 1) k − j − 1 ​ x k ​ j + k − ( x k − 1) k); \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}j!C(k,k+1,j+2)\left((x^{k}-1)^{k-j-1}x^{kj+k}-(x^{k}-1)^{k}\right); |  |

 | σ k ​ ( x) \displaystyle\sigma_{k}(x) | = ∑ j = 0 k − 1 ( − 1) j ​ ( k + 1 j + 2) ​ ( x j + 1 ​ ( x − 1) k − j − 1 ​ ( 1 + x + ⋯ + x k − 1) k − ( x k − 1) k) \displaystyle=\sum_{j=0}^{k-1}(-1)^{j}\binom{k+1}{j+2}\left(x^{j+1}(x-1)^{k-j-1}(1+x+\cdots+x^{k-1})^{k}-(x^{k}-1)^{k}\right) |  |

and where the coefficient C ⁡ ( k, t, j) C(k,t,j) satisfies C ⁡ ( k, 0, 0) = 1 / ( k − 1)! C(k,0,0)=1/(k-1)!, C ⁡ ( k, t, 0) = 0 C(k,t,0)=0 if t > 0 t>0 and otherwise

 | C ⁡ ( k, t, j) = ( k ​ j − t + 1) ​ C ​ ( k, t − 1, j) + k ​ C ​ ( k, t − 1, j − 1). C(k,t,j)=(kj-t+1)C(k,t-1,j)+kC(k,t-1,j-1)\;. |  |

###### Proof.

By Lemma 3.4 item (iii) and Lemma 3.5 item (iii) we obtain that

 | f k ​ ( x) ( k + 1) = ∑ j = 0 k − 1 α k ​ ( − 1) j ​ j! ​ ( k − 1)! ​ C ​ ( k, k + 1, j + 2) ​ ( x k ​ j + k − ( x k − 1) j + 1 x ​ ( x k − 1) j + 1) − f_{k}(x)^{(k+1)}=\sum_{j=0}^{k-1}\alpha_{k}(-1)^{j}j!(k-1)!C(k,k+1,j+2)\left(\frac{x^{kj+k}-(x^{k}-1)^{j+1}}{x(x^{k}-1)^{j+1}}\right)- |  |

 | ∑ j = 0 k − 1 ( − 1) j ​ ( k − 1)! ​ ( k + 1 j + 2) ​ ( x j + 1 − ( x − 1) j + 1 x ​ ( x − 1) j + 1). \sum_{j=0}^{k-1}(-1)^{j}(k-1)!\binom{k+1}{j+2}\left(\frac{x^{j+1}-(x-1)^{j+1}}{x(x-1)^{j+1}}\right)\;. |  |

The common denominator of all terms is x ​ ( x k − 1) k x(x^{k}-1)^{k}, so f k ​ ( x) ( k + 1) = ( k − 1)! ​ p k ​ ( x) / ( x ​ ( x k − 1) k) f_{k}(x)^{(k+1)}=(k-1)!p_{k}(x)/(x(x^{k}-1)^{k}) where

 | p k ​ ( x) = α k ​ ρ k ​ ( x) − σ k ​ ( x) p_{k}(x)=\alpha_{k}\rho_{k}(x)-\sigma_{k}(x) |  |

and where ρ k ​ ( x) \rho_{k}(x) and σ k ​ ( x) \sigma_{k}(x) are as defined is the statement of the corollary. Notice that σ k ​ ( x) \sigma_{k}(x) is of degree k 2 − 1 k^{2}-1 and ρ k ​ ( x) \rho_{k}(x) is of degree k 2 − k k^{2}-k, so p k ​ ( x) p_{k}(x) is of degree k 2 − 1 k^{2}-1. ∎

Note: setting x k = y x^{k}=y we can rewrite ρ k ​ ( x) \rho_{k}(x) as

 | ρ k ​ ( x) = ∑ j = 0 k − 1 ( − 1) j ​ j! ​ C ​ ( k, k + 1, j + 2) ​ ( ( y − 1) k − j − 1 ​ y j + 1 − ( y − 1) k). \rho_{k}(x)=\sum_{j=0}^{k-1}(-1)^{j}j!C(k,k+1,j+2)\left((y-1)^{k-j-1}y^{j+1}-(y-1)^{k}\right). |  |

Written in this way, the coefficients of ρ k ​ ( x) \rho_{k}(x) are closely related to OEIS A108267 [1] (the latter having no “sum free” expression as well) and shows that ρ k ​ ( x) \rho_{k}(x) has exactly k k nonzero terms. It is also not too difficult to show that all terms of σ k ​ ( x) \sigma_{k}(x) but one, have the same sign. So, by using Descartes’ rule of signs, we already have that p k ​ ( x) p_{k}(x) has at most 2 ​ k + 2 2k+2 positive roots. However, we require a stronger statement.

###### Lemma 3.8.

The leading coefficient of p k ​ ( x) p_{k}(x) is − 1 -1. If k k is odd then p k ​ ( 0) > 0 p_{k}(0)>0, otherwise p k ​ ( 0) < 0 p_{k}(0)<0. In particular, p k ​ ( x) p_{k}(x) has at least one negative root.

###### Proof.

The leading coefficient of p k ​ ( x) p_{k}(x) is − 1 -1 if and only if σ k ​ ( x) \sigma_{k}(x) is monic. Considering the terms of the sum defining σ k ​ ( x) \sigma_{k}(x), the coefficient of x k 2 − 1 x^{k^{2}-1} in the expression

 | x j + 1 ​ ( x − 1) k − j − 1 ​ ( 1 + x + ⋯ + x k − 1) k x^{j+1}(x-1)^{k-j-1}(1+x+\cdots+x^{k-1})^{k} |  |

is j + 1 j+1, so the leading coefficient of σ k ​ ( x) \sigma_{k}(x) is

 | ∑ j = 0 k − 1 ( − 1) j ​ ( k + 1 j + 2) ​ ( j + 1) = 1. \sum_{j=0}^{k-1}(-1)^{j}\binom{k+1}{j+2}(j+1)=1\,. |  |

For the second part of the claim, note that p k ​ ( 0) = α k ​ ρ k ​ ( 0) − σ k ​ ( 0) p_{k}(0)=\alpha_{k}\rho_{k}(0)-\sigma_{k}(0). As for ρ k ​ ( 0) \rho_{k}(0) we have that

 | ρ k ​ ( 0) \displaystyle\rho_{k}(0) | = ∑ j = 0 k − 1 ( − 1) j + k + 1 ​ j! ​ C ​ ( k, k + 1, j + 2) \displaystyle=\sum_{j=0}^{k-1}(-1)^{j+k+1}j!C(k,k+1,j+2) |  |

 |  | = ∑ j = 0 k − 1 ( − 1) j + k + 1 ​ j! ​ ( ( k ​ j + k) ​ C ​ ( k, k, j + 2) + k ​ C ​ ( k, k, j + 1)) \displaystyle=\sum_{j=0}^{k-1}(-1)^{j+k+1}j!\left((kj+k)C(k,k,j+2)+kC(k,k,j+1)\right) |  |

 |  | = ( − 1) k + 1 ​ k ​ C ​ ( k, k, 1) + ( k − 1)! ​ k 2 ​ C ​ ( k, k, k + 1) \displaystyle=(-1)^{k+1}kC(k,k,1)+(k-1)!k^{2}C(k,k,k+1) |  |

 |  | = ( − 1) k + 1 ​ k ​ C ​ ( k, k, 1) + 0 \displaystyle=(-1)^{k+1}kC(k,k,1)+0 |  |

 |  | = ( − 1) k + 1 ​ k 2 \displaystyle=(-1)^{k+1}k^{2} |  |

while σ k ​ ( 0) = ( − 1) k + 1 ​ k \sigma_{k}(0)=(-1)^{k+1}k. Thus, we must show that α k > 1 / k \alpha_{k}>1/k. Indeed, this holds from ( 1) and since φ k < k / ( k + 1) \varphi_{k}<k/(k+1). ∎

###### Conjecture 3.9.

p k ​ ( x) p_{k}(x) has at most two real roots in ( 0, 1) (0,1), counting multiplicity.

###### Lemma 3.10.

Conjecture 3.9 implies Conjecture 3.1.

###### Proof.

We use a similar argument as in [4]. Assume that p k ​ ( x) p_{k}(x) has at most two real roots in ( 0, 1) (0,1), counting multiplicity. By Rolle’s theorem, applied k + 1 k+1 times, it follows that f k ​ ( x) f_{k}(x) has at most k + 3 k+3 roots in [0, 1] [0,1], counting multiplicity. By Corollary 3.6, there is a root of multiplicity k k at 0 0. By Lemma 3.2, there is a root at 1 1 and a double root at φ k \varphi_{k}. Thus we have found all k + 3 k+3 roots of f k ​ ( x) f_{k}(x) in [0, 1] [0,1]. Because f k ​ ( x) f_{k}(x) has a double root at φ k \varphi_{k}, it is either all nonnegative or all non-positive on [0, 1] [0,1]. By Lemma 3.3, it must be all nonnegative on [0, 1] [0,1]. ∎

Observe that the proof of Lemma 3.10 shows that Conjecture 3.9 is equivalent to the same conjecture with at most replaced with exactly. Table 2 list p k ​ ( x) p_{k}(x) explicitly for 2 ≤ k ≤ 6 2\leq k\leq 6 where we have written α = α k \alpha=\alpha_{k} for clarity. A Python script generating p k ​ ( x) p_{k}(x) for a given k k can be obtained from https://github.com/raphaelyuster/almost-k-union-closed/blob/main/polynomial.py.

Boppana observed that p 2 ​ ( x) p_{2}(x) has exactly two distinct real roots in ( 0, 1) (0,1), both simple. This can also be observed from Table 2 using Descartes’ rule of signs. We show that p 3 ​ ( x) p_{3}(x) and p 4 ​ ( x) p_{4}(x) have at most two real roots in ( 0, 1) (0,1), counting multiplicity.

k k | p k ​ ( x) p_{k}(x) |

2 2 | ( − 4 ​ α + 2) + 3 ​ x − 4 ​ α ​ x 2 − x 3 (-4\alpha+2)+3x-4\alpha x^{2}-x^{3} |

3 3 | ( 9 ​ α − 3) − 6 ​ x − 10 ​ x 2 + ( 63 ​ α − 6) ​ x 3 − 3 ​ x 4 + 2 ​ x 5 + 9 ​ α ​ x 6 − x 8 (9\alpha-3)-6x-10x^{2}+(63\alpha-6)x^{3}-3x^{4}+2x^{5}+9\alpha x^{6}-x^{8} |

4 4 | ( − 16 ​ α + 4) + 10 ​ x + 20 ​ x 2 + 35 ​ x 3 + ( − 496 ​ α + 40) ​ x 4 + 44 ​ x 5 + 40 ​ x 6 + 25 ​ x 7 + ( − 496 ​ α + 20) ​ x 8 + 10 ​ x 9 + 4 ​ x 10 + 5 ​ x 11 − 16 ​ α ​ x 12 − x 15 (-16\alpha+4)+10x+20x^{2}+35x^{3}+(-496\alpha+40)x^{4}+44x^{5}+40x^{6}+25x^{7}+(-496\alpha+20)x^{8}+10x^{9}+4x^{10}+5x^{11}-16\alpha x^{12}-x^{15} |

5 5 | ( 25 ​ α − 5) − 15 ​ x − 35 ​ x 2 − 70 ​ x 3 − 126 ​ x 4 + ( 3025 ​ α − 185) ​ x 5 − 255 ​ x 6 − 320 ​ x 7 − 365 ​ x 8 − 371 ​ x 9 + ( 9525 ​ α − 365) ​ x 10 − 320 ​ x 11 − 255 ​ x 12 − 185 ​ x 13 − 131 ​ x 14 + ( 3025 ​ α − 70) ​ x 15 − 35 ​ x 16 − 15 ​ x 17 − 5 ​ x 18 + 4 ​ x 19 + 25 ​ α ​ x 20 − x 24 (25\alpha-5)-15x-35x^{2}-70x^{3}-126x^{4}+(3025\alpha-185)x^{5}-255x^{6}-320x^{7}-365x^{8}-371x^{9}+(9525\alpha-365)x^{10}-320x^{11}-255x^{12}-185x^{13}-131x^{14}+(3025\alpha-70)x^{15}-35x^{16}-15x^{17}-5x^{18}+4x^{19}+25\alpha x^{20}-x^{24} |

6 6 | ( − 36 ​ α + 6) + 21 ​ x + 56 ​ x 2 + 126 ​ x 3 + 252 ​ x 4 + 462 ​ x 5 + ( − 16416 ​ α + 756) ​ x 6 + 1161 ​ x 7 + 1666 ​ x 8 + 2247 ​ x 9 + 2856 ​ x 10 + 3416 ​ x 11 + ( − 123516 ​ α + 3906) ​ x 12 + 4221 ​ x 13 + 4332 ​ x 14 + 4221 ​ x 15 + 3906 ​ x 16 + 3451 ​ x 17 + ( − 123516 ​ α + 2856) ​ x 18 + 2247 ​ x 19 + 1666 ​ x 20 + 1161 ​ x 21 + 756 ​ x 22 + 441 ​ x 23 + ( − 16416 ​ α + 252) ​ x 24 + 126 ​ x 25 + 56 ​ x 26 + 21 ​ x 27 + 6 ​ x 28 + 7 ​ x 29 − 36 ​ α ​ x 30 − x 35 (-36\alpha+6)+21x+56x^{2}+126x^{3}+252x^{4}+462x^{5}+(-16416\alpha+756)x^{6}+1161x^{7}+1666x^{8}+2247x^{9}+2856x^{10}+3416x^{11}+(-123516\alpha+3906)x^{12}+4221x^{13}+4332x^{14}+4221x^{15}+3906x^{16}+3451x^{17}+(-123516\alpha+2856)x^{18}+2247x^{19}+1666x^{20}+1161x^{21}+756x^{22}+441x^{23}+(-16416\alpha+252)x^{24}+126x^{25}+56x^{26}+21x^{27}+6x^{28}+7x^{29}-36\alpha x^{30}-x^{35} |

Table 2: p k ​ ( x) p_{k}(x) for k = 2, …, 6 k=2,\ldots,6. For notational clarity, α = α k \alpha=\alpha_{k}.

###### Proposition 3.11.

p 3 ​ ( x) p_{3}(x) has at most two real roots in ( 0, 1) (0,1), counting multiplicity.

###### Proof.

By Table 2, and since α 3 ≈ 0.4655 \alpha_{3}\approx 0.4655, we have that p 3 ​ ( 1) = 81 ​ α 3 − 27 > 0 p_{3}(1)=81\alpha_{3}-27>0. Since its degree is even and its leading coefficient is negative, this implies that p 3 ​ ( x) p_{3}(x) has a root larger than 1 1. By Lemma 3.8, p 3 ​ ( x) p_{3}(x) has a negative root. It therefore suffices to prove that p 3 ​ ( x) p_{3}(x) has at most four real roots counting multiplicity. To this end, it suffices to prove that the third derivative of p 3 ​ ( x) p_{3}(x) has precisely one simple real root. The third and fourth derivatives of p 3 ​ ( x) p_{3}(x) are:

 | p 3 ( 3) ​ ( x) \displaystyle{p_{3}}^{(3)}(x) | = ( 378 ​ α 3 − 36) − 72 ​ x + 120 ​ x 2 + 1080 ​ α 3 ​ x 3 − 336 ​ x 5; \displaystyle=(378\alpha_{3}-36)-72x+120x^{2}+1080\alpha_{3}x^{3}-336x^{5}\,; |  |

 | p 3 ( 4) ​ ( x) \displaystyle{p_{3}}^{(4)}(x) | = − 72 + 240 ​ x + 3240 ​ α ​ x 2 − 1680 ​ x 4. \displaystyle=-72+240x+3240\alpha x^{2}-1680x^{4}\,. |  |

We show that p 3 ( 4) ​ ( x) {p_{3}}^{(4)}(x) has exactly four real roots, all simple:

 |  | p 3 ( 4) ​ ( − 0.9) \displaystyle{p_{3}}^{(4)}\left(-0.9\right) | = \displaystyle~= | 9 125 ​ ( 36450 ​ α 3 − 19309) \displaystyle~\tfrac{9}{125}(36450\alpha_{3}-19309) | < 0, \displaystyle~<0\,, |  |

 |  | p 3 ( 4) ​ ( − 0.8) \displaystyle{p_{3}}^{(4)}\left(-0.8\right) | = \displaystyle~= | 216 125 ​ ( 1200 ​ α 3 − 551) \displaystyle~\tfrac{216}{125}(1200\alpha_{3}-551) | > 0, \displaystyle>0\,, |  |

 |  | p 3 ( 4) ​ ( 0) \displaystyle{p_{3}}^{(4)}\left(0\right) | = \displaystyle~= | − 72 \displaystyle~-72 | < 0, \displaystyle<0\,, |  |

 |  | p 3 ( 4) ​ ( 0.5) \displaystyle{p_{3}}^{(4)}\left(0.5\right) | = \displaystyle~= | 810 ​ α 3 − 57 \displaystyle~810\alpha_{3}-57 | > 0. \displaystyle>0\,. |  |

Denoting the roots of p 3 ( 4) ​ ( x) {p_{3}}^{(4)}(x) by γ 1 < γ 2 < γ 3 < γ 4 \gamma_{1}<\gamma_{2}<\gamma_{3}<\gamma_{4}, we have γ 1 ∈ ( − 0.9, − 0.8) \gamma_{1}\in(-0.9,-0.8), γ 2 ∈ ( − 0.8, 0) \gamma_{2}\in(-0.8,0), γ 3 ∈ ( 0, 0.5) \gamma_{3}\in(0,0.5), γ 4 ∈ ( 0.5, ∞) \gamma_{4}\in(0.5,\infty).

As the leading coefficient of p 3 ( 3) ​ ( x) {p_{3}}^{(3)}(x) is negative, it must be that γ 1, γ 3 \gamma_{1},\gamma_{3} are local minima of p 3 ( 3) ​ ( x) {p_{3}}^{(3)}(x) and γ 2, γ 4 \gamma_{2},\gamma_{4} are local maxima of p 3 ( 3) ​ ( x) {p_{3}}^{(3)}(x). To show that p 3 ( 3) ​ ( x) {p_{3}}^{(3)}(x) only has one simple real root, it suffices to prove that the value of p 3 ( 3) ​ ( x) {p_{3}}^{(3)}(x) at both local minima is positive. First observe that p 3 ( 3) ​ ( 0) = 378 ​ α 3 − 36 > 100 {p_{3}}^{(3)}{(0)}=378\alpha_{3}-36>100. Now, for every x ∈ [0, 0.5] x\in[0,0.5] we have that

 | p 3 ( 3) ​ ( x) ≥ p 3 ( 3) ​ ( 0) − 72 ⋅ 1 2 − 336 ⋅ 1 32 > 50. {p_{3}}^{(3)}(x)\geq{p_{3}}^{(3)}(0)-72\cdot\tfrac{1}{2}-336\cdot\tfrac{1}{32}>50\;. |  |

As γ 3 ∈ ( 0, 0.5) \gamma_{3}\in(0,0.5), we have that p 3 ( 3) ​ ( γ 3) > 0 {p_{3}}^{(3)}{(\gamma_{3})}>0. We next show that p 3 ( 3) ​ ( γ 1) > 0 {p_{3}}^{(3)}{(\gamma_{1})}>0.

 | p 3 ( 3) ​ ( − 0.9) = 9 6250 ​ ( 225281 − 284250 ​ α 3) > 133. {p_{3}}^{(3)}(-0.9)=\tfrac{9}{6250}(225281-284250\alpha_{3})>133\;. |  |

For every x ∈ [− 0.9, − 0.8] x\in[-0.9,-0.8] we have

 | p 3 ( 3) ​ ( x) − p 3 ( 3) ​ ( − 0.9) \displaystyle{p_{3}}^{(3)}(x)-{p_{3}}^{(3)}(-0.9) | = − 72 ​ ( x + 9 10) + 120 ​ ( x 2 − 81 100) + 1080 ​ α 3 ​ ( x 3 + 729 1000) − 336 ​ ( x 5 + 59049 100000) \displaystyle=-72\left(x+\tfrac{9}{10}\right)+120\left(x^{2}-\tfrac{81}{100}\right)+1080\alpha_{3}\left(x^{3}+\tfrac{729}{1000}\right)-336\left(x^{5}+\tfrac{59049}{100000}\right) |  |

 |  | ≥ − 72 ​ ( − 8 10 + 9 10) + 120 ​ ( 16 25 − 81 100) − 336 ​ ( − 1024 3125 + 59049 100000) = − 724401 6250 \displaystyle\geq-72\left(-\tfrac{8}{10}+\tfrac{9}{10}\right)+120\left(\tfrac{16}{25}-\tfrac{81}{100}\right)-336\left(-\tfrac{1024}{3125}+\tfrac{59049}{100000}\right)=-\tfrac{724401}{6250} |  |

 |  | > − 116. \displaystyle>-116\;. |  |

As γ 1 ∈ ( − 0.9, − 0.8) \gamma_{1}\in(-0.9,-0.8), we have p 3 ( 3) ​ ( γ 1) > 0 {p_{3}}^{(3)}{(\gamma_{1})}>0. ∎

###### Proposition 3.12.

p 4 ​ ( x) p_{4}(x) has at most two real roots in ( 0, 1) (0,1), counting multiplicity.

###### Proof.

By Lemma 3.8, p 4 ​ ( x) p_{4}(x) has a negative root. It therefore suffices to prove that p 4 ​ ( x) p_{4}(x) has at most three real roots, counting multiplicity.

There are two distinct ways to prove this fact. The one we will not pursue in detail here, is by considering the signs of the discriminants of all the derivatives of p 4 ​ ( x) p_{4}(x). It turns out that the sign pattern of these discriminants is ( +, +, −, −, −, +, −, −, −, +, −, −, −, 0, +) (+,+,-,-,-,+,-,-,-,+,-,-,-,0,+) where the i i ’th coordinate (starting at i = 0 i=0) is the sign of the discriminant of p 4 ( i) ​ ( x) {p_{4}}^{(i)}(x). Recalling that the discriminant of a (real, univariate) polynomial is zero if and only if it has a multiple root and otherwise it is positive if and only if the number of non-real roots (counting multiplicity) is a multiple of 4 4, we easily obtain that the number of real roots of the derivatives follows the sequence ( 3, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 1) (3,2,3,2,1,2,3,2,1,2,3,2,1,2,1) where the i i ’th coordinate (starting at i = 0 i=0) is the number of real roots of p 4 ( i) ​ ( x) {p_{4}}^{(i)}(x). This is seen, starting as follows: the 14 14 ’th derivative is a linear polynomial so has precisely one real root. The 13 13 ’th derivative has discriminant 0 0, and has a multiple root (at x = 0 x=0, in fact). The 12 12 ’th derivative has negative discriminant, so it must have two conjugate non-real roots, and one real root. The 11 11 ’th derivative has negative discriminant, so again has only two non-real conjugate roots, and hence two real roots. Continuing this way, we see that for this particular sign pattern of discriminants, the number of real roots of p 4 ( i) ​ ( x) {p_{4}}^{(i)}(x) is uniquely determined from the number of real roots of p 4 ( i + 1) ​ ( x) {p_{4}}^{(i+1)}(x), from the sign of the discriminant of p 4 ( i) ​ ( x) {p_{4}}^{(i)}(x), from the fundamental theorem of algebra, and from the fact that the number or real roots of a polynomial is at most one larger than the number of real roots of its derivative. Finally, we obtain that the number of real roots of p 4 ( 0) ​ ( x) {p_{4}}^{(0)}(x), i.e. p 4 ​ ( x) {p_{4}}(x), is 3 3. A Maple worksheet computing these discriminant signs is available at https://github.com/raphaelyuster/almost-k-union-closed/blob/main/p4.mw. Observe that each discriminant is an integer polynomial in α 4 \alpha_{4}, and hence an integer polynomial in φ 4 \varphi_{4}. But recall that φ 4 4 = 1 − φ 4 \varphi_{4}^{4}=1-\varphi_{4}, so each of these discriminants can be reduced to an integer cubic polynomial in φ 4 \varphi_{4} (the polynomial x 4 + x − 1 x^{4}+x-1 is irreducible over ℚ {\mathbb{Q}}). Thus, the discriminant signs are easy to obtain by simply assigning φ 4 \varphi_{4} into explicit integer cubic polynomials.

A more direct approach is similar to the one in Proposition 3.12 and requires considering a few derivatives (but not all). A detailed rigorous account is given in Appendix A where we prove that the real-root pattern of the derivatives of p 4 ​ ( x) p_{4}(x) is ( 3, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 1) (3,2,3,2,1,2,3,2,1,2,3,2,1,2,1) as stated above. ∎

By Lemma 3.10, Proposition 3.11 and Proposition 3.12, we have

###### Corollary 3.13.

f k ​ ( x) f_{k}(x) is nonnegative in [0, 1] [0,1] for k = 3, 4 k=3,4 (and for k = 2 k=2, as shown in [2, 4]).

## 4 The multidimensional Chase-Lovett function

For x ∈ ( 0, 1) x\in(0,1), let

 | F k ​ ( x) ≔ h ⁡ ( x k) x k − 1 ​ h ​ ( x). F_{k}(x)\coloneqq\frac{h(x^{k})}{x^{k-1}h(x)}\;. |  |

Let φ = φ 2 = 5 − 1 2 \varphi=\varphi_{2}=\frac{\sqrt{5}-1}{2}. The following lemma is proved in [6].

###### Lemma 4.1 ( [6]).

For x, y ∈ [0, 1] x,y\in[0,1] it holds that

 | h ⁡ ( x ​ y) ≥ 1 2 ​ φ ​ ( x ​ h ​ ( y) + y ​ h ​ ( x)). ∎ h(xy)\geq\frac{1}{2\varphi}\left(xh(y)+yh(x)\right)\,.\qed |  |

Let

 | μ k ≔ { 1 α k if ​ 2 ≤ k ≤ 4; 2 p − q 2 p ​ φ p + q 2 p ​ φ p + 1 if k ≥ 5, p = ⌊ log 2 ( k) ⌋, q = k − 2 p. \mu_{k}\coloneqq\begin{cases}\frac{1}{\alpha_{k}}&{\rm if}~~2\leq k\leq 4\,;\\ \frac{2^{p}-q}{2^{p}\varphi^{p}}+\frac{q}{2^{p}\varphi^{p+1}}&{\rm if}~~k\geq 5,\,p=\lfloor\log_{2}(k)\rfloor,\,q=k-2^{p}\,.\end{cases} |  |

We apply Lemma 4.1 and our results from the previous section to lower-bound F k ​ ( x) F_{k}(x).

###### Lemma 4.2.

For x ∈ ( 0, 1) x\in(0,1) we have

 | F k ​ ( x) ≥ μ k. F_{k}(x)\geq\mu_{k}\;. |  |

###### Proof.

We proceed by induction on k k, where k = 2, 3, 4 k=2,3,4 hold by Corollary 3.13.

For the sake of the induction, observe also that the expression defining μ k \mu_{k} for k ≥ 5 k\geq 5 can be naively used for k = 2, 3, 4 k=2,3,4. Indeed, for k = 2 k=2 the expression equals 1 / φ = 1 / α 2 1/\varphi=1/\alpha_{2}, for k = 3 k=3 the expression is 1 / 2 ​ φ + 1 / 2 ​ φ 2 = 2.118.. < 2.148.. = 1 / α 3 1/2\varphi+1/2\varphi^{2}=2.118..<2.148..=1/\alpha_{3} and for k = 4 k=4 the expression is 1 / φ 2 = 2.618.. < 2.630.. = 1 / α 4 1/\varphi^{2}=2.618..<2.630..=1/\alpha_{4}. Assume that k = 2 p + q ≥ 5 k=2^{p}+q\geq 5 where 0 ≤ q < 2 p 0\leq q<2^{p} and that the lemma holds for values smaller than k k. By Lemma 4.1 we have

 | F k ​ ( x) \displaystyle F_{k}(x) | = h ⁡ ( x k) x k − 1 ​ h ​ ( x) \displaystyle=\frac{h(x^{k})}{x^{k-1}h(x)} |  |

 |  | = h ⁡ ( x ⌊ k / 2 ⌋ ​ x ⌈ k / 2 ⌉) x k − 1 ​ h ​ ( x) \displaystyle=\frac{h(x^{\lfloor k/2\rfloor}x^{\lceil k/2\rceil})}{x^{k-1}h(x)} |  |

 |  | ≥ 1 2 ​ φ ​ ( x ⌊ k / 2 ⌋ ​ h ​ ( x ⌈ k / 2 ⌉) + x ⌈ k / 2 ⌉ ​ h ​ ( x ⌊ k / 2 ⌋) x k − 1 ​ h ​ ( x)) \displaystyle\geq\frac{1}{2\varphi}\left(\frac{x^{\lfloor k/2\rfloor}h(x^{\lceil k/2\rceil})+x^{\lceil k/2\rceil}h(x^{\lfloor k/2\rfloor})}{x^{k-1}h(x)}\right) |  |

 |  | = 1 2 ​ φ ​ ( F ⌈ k / 2 ⌉ ​ ( x) + F ⌊ k / 2 ⌋ ​ ( x)) \displaystyle=\frac{1}{2\varphi}\left(F_{\lceil k/2\rceil}(x)+F_{\lfloor k/2\rfloor}(x)\right) |  |

 |  | ≥ 1 2 ​ φ ​ ( 2 p − 1 − ⌈ q / 2 ⌉ 2 p − 1 ​ φ p − 1 + ⌈ q / 2 ⌉ 2 p − 1 ​ φ p + 2 p − 1 − ⌊ q / 2 ⌋ 2 p − 1 ​ φ p − 1 + ⌊ q / 2 ⌋ 2 p − 1 ​ φ p) \displaystyle\geq\frac{1}{2\varphi}\left(\frac{2^{p-1}-\lceil q/2\rceil}{2^{p-1}\varphi^{p-1}}+\frac{\lceil q/2\rceil}{2^{p-1}\varphi^{p}}+\frac{2^{p-1}-\lfloor q/2\rfloor}{2^{p-1}\varphi^{p-1}}+\frac{\lfloor q/2\rfloor}{2^{p-1}\varphi^{p}}\right) |  |

 |  | = 2 p − q 2 p ​ φ p + q 2 p ​ φ p + 1. \displaystyle=\frac{2^{p}-q}{2^{p}\varphi^{p}}+\frac{q}{2^{p}\varphi^{p+1}}\;. |  |

∎

###### Lemma 4.3.

Let 1 ≤ m ≤ k − 2 1\leq m\leq k-2. Then, μ k − m / ( k − m) > μ k / k \mu_{k-m}/(k-m)>\mu_{k}/k.

###### Proof.

By telescoping product and induction, it suffices to prove that for all k ≥ 2 k\geq 2, μ k − 1 / μ k > ( k − 1) / k \mu_{k-1}/\mu_{k}>(k-1)/k.

For k = 3 k=3 we have μ 2 / μ 3 = α 3 / α 2 = 0.4655.. / 0.6180.. ≈ 0.7523.. > 2 / 3 \mu_{2}/\mu_{3}=\alpha_{3}/\alpha_{2}=0.4655../0.6180..\approx 0.7523..>2/3. For k = 4 k=4 we have μ 3 / μ 4 = α 4 / α 3 = 0.3802.. / 0.4655.. ≈ 0.8167.. > 3 / 4 \mu_{3}/\mu_{4}=\alpha_{4}/\alpha_{3}=0.3802../0.4655..\approx 0.8167..>3/4. For k = 5 k=5 we have μ 4 / μ 5 = 1 / ( α 4 ( 3 / 4 φ 2 + 1 / 4 φ 3)) = 1 / ( 0.3802.. ⋅ 3.0229.. ≈ 0.8700..) > 4 / 5 \mu_{4}/\mu_{5}=1/(\alpha_{4}(3/4\varphi^{2}+1/4\varphi^{3}))=1/(0.3802..\cdot 3.0229..\approx 0.8700..)>4/5. Se we may now assume that k ≥ 6 k\geq 6.

Consider first the case that k = 2 p + q k=2^{p}+q and 1 ≤ q < 2 p 1\leq q<2^{p}, so k − 1 = 2 p + q − 1 k-1=2^{p}+q-1. We have

 | μ k − 1 μ k \displaystyle\frac{\mu_{k-1}}{\mu_{k}} | = 2 p − q + 1 2 p ​ φ p + q − 1 2 p ​ φ p + 1 2 p − q 2 p ​ φ p + q 2 p ​ φ p + 1 \displaystyle=\frac{\frac{2^{p}-q+1}{2^{p}\varphi^{p}}+\frac{q-1}{2^{p}\varphi^{p+1}}}{\frac{2^{p}-q}{2^{p}\varphi^{p}}+\frac{q}{2^{p}\varphi^{p+1}}} |  |

 |  | = φ ⁡ ( 2 p − q + 1) + q − 1 φ ⁡ ( 2 p − q) + q \displaystyle=\frac{\varphi(2^{p}-q+1)+q-1}{\varphi(2^{p}-q)+q} |  |

 |  | = 1 − 1 − φ φ ⁡ ( 2 p − q) + q \displaystyle=1-\frac{1-\varphi}{\varphi(2^{p}-q)+q} |  |

so it remains to prove that

 | φ ⁡ ( 2 p − q) + q 1 − φ = φ ​ k − 2 ​ q ​ φ + q 1 − φ > k \frac{\varphi(2^{p}-q)+q}{1-\varphi}=\frac{\varphi k-2q\varphi+q}{1-\varphi}>k |  |

which is equivalent to k > q k>q, which indeed holds.

Consider next the case where k = 2 p k=2^{p}, so k − 1 = 2 p − 1 + q k-1=2^{p-1}+q where q = 2 p − 1 − 1 q=2^{p-1}-1. We have

 | μ k − 1 μ k = 1 2 p − 1 ​ φ p − 1 + 2 p − 1 − 1 2 p − 1 ​ φ p 1 φ p = φ + 2 p − 1 − 1 2 p − 1 = φ + k / 2 − 1 k / 2 > 1 − 1 k. \frac{\mu_{k-1}}{\mu_{k}}=\frac{\frac{1}{2^{p-1}\varphi^{p-1}}+\frac{2^{p-1}-1}{2^{p-1}\varphi^{p}}}{\frac{1}{\varphi^{p}}}=\frac{\varphi+2^{p-1}-1}{2^{p-1}}=\frac{\varphi+k/2-1}{k/2}>1-\frac{1}{k}\;. |  |

∎

Let g ⁡ ( x) = h ⁡ ( x) / x g(x)=h(x)/x and let M k: ( 0, 1) k → ℝ ≥ 0 M_{k}:(0,1)^{k}\rightarrow{\mathbb{R}}_{\geq 0} be defined as

 | M k ​ ( x 1, …, x k) ≔ g ⁡ ( ∏ i = 1 k x i) ∑ i = 1 k g ⁡ ( x i). M_{k}(x_{1},\ldots,x_{k})\coloneqq\frac{g(\prod_{i=1}^{k}x_{i})}{\sum_{i=1}^{k}g(x_{i})}\;. |  |

The function M 2 M_{2} plays a crucial role in the proof of [6], and so does its generalization here. Notice that M k M_{k} is smooth in ( 0, 1) k (0,1)^{k}. By routine calculations (e.g. l’Hospital’s rule) it is easily shown:

###### Lemma 4.4.

M k ​ ( x) M_{k}(x) is extended continuously to [0, 1] k [0,1]^{k} as follows: Suppose ( x 1, …, x k) (x_{1},\ldots,x_{k}) contains ℓ \ell zeroes and m m ones, where ℓ + m > 0 \ell+m>0. If ℓ > 0 \ell>0 or m ≥ k − 1 m\geq k-1, then M k ​ ( x 1, …, x k) = 1 M_{k}(x_{1},\ldots,x_{k})=1. Otherwise, suppose that x i 1, …, x i k − m x_{i_{1}},\ldots,x_{i_{k-m}} are not 1 1, then, M k ​ ( x 1, …, x k) = M k − m ​ ( x i 1, …, x i k − m) M_{k}(x_{1},\ldots,x_{k})=M_{k-m}(x_{i_{1}},\ldots,x_{i_{k-m}}). ∎

We call a point in [0, 1] k [0,1]^{k} diagonal if it is supported on { t, 1 } \{t,1\} for some t ∈ ( 0, 1) t\in(0,1).

###### Lemma 4.5.

μ k / k ≤ M k < 1 \mu_{k}/k\leq M_{k}<1 in ( 0, 1) k (0,1)^{k}. Furthermore, every minimum of M k M_{k} in [0, 1] k [0,1]^{k} is obtained in some diagonal point.

###### Proof.

The proof proceeds by induction on k k. The case k = 2 k=2 is proved in [6] and the unique minimum is at ( φ, φ) (\varphi,\varphi) where M 2 ​ ( φ, φ) = 1 / 2 ​ φ = 1 / 2 ​ α 2 = μ 2 / 2 M_{2}(\varphi,\varphi)=1/2\varphi=1/2\alpha_{2}=\mu_{2}/2. Let k ≥ 3 k\geq 3 and assume the lemma holds for values smaller than k k. In ( 0, 1) k (0,1)^{k} we have that

 | M k ​ ( x 1, …, x k) \displaystyle M_{k}(x_{1},\ldots,x_{k}) | = g ⁡ ( ∏ i = 1 k x i) ∑ i = 1 k g ⁡ ( x i) \displaystyle=\frac{g(\prod_{i=1}^{k}x_{i})}{\sum_{i=1}^{k}g(x_{i})} |  |

 |  | = g ⁡ ( x 1 ​ x 2 ​ ∏ i = 3 k x i) g ⁡ ( x 1) + g ⁡ ( x 2) + ∑ i = 3 k g ⁡ ( x i) \displaystyle=\frac{g(x_{1}x_{2}\prod_{i=3}^{k}x_{i})}{g(x_{1})+g(x_{2})+\sum_{i=3}^{k}g(x_{i})} |  |

 |  | < g ⁡ ( x 1 ​ x 2 ​ ∏ i = 3 k x i) g ⁡ ( x 1 ​ x 2) + ∑ i = 3 k g ⁡ ( x i) \displaystyle<\frac{g(x_{1}x_{2}\prod_{i=3}^{k}x_{i})}{g(x_{1}x_{2})+\sum_{i=3}^{k}g(x_{i})} |  |

 |  | = M k − 1 ​ ( x 1 ​ x 2, x 3, …, x k) \displaystyle=M_{k-1}(x_{1}x_{2},x_{3},\ldots,x_{k}) |  |

 |  | < 1. \displaystyle<1\;. |  |

By Lemma 4.4, the values at boundary points are either 1 1, or of the form M k − m ​ ( x 1, …, x k − m) M_{k-m}(x_{1},\ldots,x_{k-m}) for some point ( x 1, …, x k − m) ∈ ( 0, 1) k − m (x_{1},\ldots,x_{k-m})\in(0,1)^{k-m} with 1 ≤ m ≤ k − 2 1\leq m\leq k-2. As we already proved that M k < 1 M_{k}<1 in ( 0, 1) k (0,1)^{k}, only the latter points are “potential” minimum points. Suppose first that ( x 1, …, x k − m) (x_{1},\ldots,x_{k-m}) is not a diagonal point. By the induction hypothesis, it is not a minimum point of M k − m M_{k-m}. So there exist some δ 1, …, δ k − m \delta_{1},\ldots,\delta_{k-m} (some may be negative) such that x i + δ i ∈ ( 0, 1) x_{i}+\delta_{i}\in(0,1) for i ∈ [k − m] i\in[k-m] and such that M k − m ​ ( x 1, …, x k − m) > M k − m ​ ( x 1 + δ 1, …, x k − m + δ k − m) M_{k-m}(x_{1},\ldots,x_{k-m})>M_{k-m}(x_{1}+\delta_{1},\ldots,x_{k-m}+\delta_{k-m}). Since M k ​ ( x 1 + δ 1, …, x k − m + δ k − m, 1, …, 1) = M k − m ​ ( x 1 + δ 1, …, x k − m + δ k − m) M_{k}(x_{1}+\delta_{1},\ldots,x_{k-m}+\delta_{k-m},1,\ldots,1)=M_{k-m}(x_{1}+\delta_{1},\ldots,x_{k-m}+\delta_{k-m}), we have that M k M_{k} does not attain minimum at the stated boundary point. Consider next the case that x i = t x_{i}=t for i ∈ [k − m] i\in[k-m] and some t ∈ ( 0, 1) t\in(0,1). Then M k − m ​ ( t, …, t) = F k − m ​ ( t) / ( k − m) ≥ μ k − m / ( k − m) M_{k-m}(t,\ldots,t)=F_{k-m}(t)/(k-m)\geq\mu_{k-m}/(k-m) by Lemma 4.2 and μ k − m / ( k − m) ≥ μ k / k \mu_{k-m}/(k-m)\geq\mu_{k}/k by Lemma 4.3.

It remains to consider the case where the minimum is attained at an internal point. Here we use the same approach as in [6]. Assume that M k M_{k} is minimized at some point ( x 1 ∗, …, x k ∗) ∈ ( 0, 1) k (x_{1}^{*},\ldots,x_{k}^{*})\in(0,1)^{k}, and let β = M k ​ ( x 1 ∗, …, x k ∗) \beta=M_{k}(x_{1}^{*},\ldots,x_{k}^{*}). Let

 | G ⁡ ( x 1, …, x k) = g ⁡ ( ∏ i = 1 k x i) − β ⁡ ( ∑ i = 1 k g ⁡ ( x i)). G(x_{1},\ldots,x_{k})=g\left(\prod_{i=1}^{k}x_{i}\right)-\beta\left(\sum_{i=1}^{k}g(x_{i})\right)\;. |  |

Then G G is nonnegative in ( 0, 1) k (0,1)^{k} and ( x 1 ∗, …, x k ∗) = 0 (x_{1}^{*},\ldots,x_{k}^{*})=0. Thus the partial derivatives of G G are zero at the minimum point:

 | ∂ G ∂ x i ​ ( x 1 ∗, …, x k ∗) = 0 for ​ all ​ 1 ≤ i ≤ k. \frac{\partial G}{\partial x_{i}}(x_{1}^{*},\ldots,x_{k}^{*})=0\quad{\rm for~all~}1\leq i\leq k\;. |  |

Evaluating the derivatives gives

 | ∂ G ∂ x i ​ ( x 1, …, x k) = g ′ ​ ( ∏ j = 1 k x j) ​ ∏ j = 1 k x j x i − β ​ g ′ ​ ( x i) for ​ all ​ 1 ≤ i ≤ k. \frac{\partial G}{\partial x_{i}}(x_{1},\ldots,x_{k})=g^{\prime}\left(\prod_{j=1}^{k}x_{j}\right)\frac{\prod_{j=1}^{k}x_{j}}{x_{i}}-\beta g^{\prime}(x_{i})\quad{\rm for~all~}1\leq i\leq k\;. |  |

Defining Q ⁡ ( x) = x ​ g ′ ​ ( x) Q(x)=xg^{\prime}(x) we obtain that Q ⁡ ( x 1 ∗) = Q ⁡ ( x 2 ∗) = ⋯ = Q ⁡ ( x k ∗) Q(x_{1}^{*})=Q(x_{2}^{*})=\cdots=Q(x_{k}^{*}). Since Q ⁡ ( x) = log ⁡ ( 1 − x) / x Q(x)=\log(1-x)/x is strictly decreasing, we must have x 1 ∗ = x 2 ∗ = ⋯ = x k ∗ = t x_{1}^{*}=x_{2}^{*}=\cdots=x_{k}^{*}=t for some t ∈ ( 0, 1) t\in(0,1). But notice that in this case we have M k ​ ( t, …, t) = F k ​ ( t) / k ≥ μ k / k M_{k}(t,\ldots,t)=F_{k}(t)/k\geq\mu_{k}/k by Lemma 4.2. ∎

###### Corollary 4.6.

For ( x 1, …, x k) ∈ [0, 1] k (x_{1},\ldots,x_{k})\in[0,1]^{k} it holds that

 | h ⁡ ( ∏ i = 1 k x i) ≥ μ k k ​ ( ∑ i = 1 k h ⁡ ( x i) ⋅ ∏ j ∈ [k] ∖ i x j). h\left(\prod_{i=1}^{k}x_{i}\right)\geq\frac{\mu_{k}}{k}\left(\sum_{i=1}^{k}h(x_{i})\cdot\prod_{j\in[k]\setminus i}x_{j}\right). |  |

###### Proof.

For k = 2 k=2 this is just Lemma 4.1. Assume that k ≥ 3 k\geq 3 and that the claim holds for smaller k k. If ( x 1, …, x k) (x_{1},\ldots,x_{k}) is an internal point, then the claim follows from Lemma 4.5. If ( x 1, …, x k) (x_{1},\ldots,x_{k}) contains a zero, then the claim amount to 0 = 0 0=0. Otherwise, we may assume that x k = 1 x_{k}=1. In this case we have by induction that

 | h ⁡ ( ∏ i = 1 k x i) = h ⁡ ( ∏ i = 1 k − 1 x i) ≥ μ k − 1 k − 1 ​ ( ∑ i = 1 k − 1 h ⁡ ( x i) ⋅ ∏ j ∈ [k − 1] ∖ i x j) = μ k − 1 k − 1 ​ ( ∑ i = 1 k h ⁡ ( x i) ⋅ ∏ j ∈ [k] ∖ i x j) h\left(\prod_{i=1}^{k}x_{i}\right)=h\left(\prod_{i=1}^{k-1}x_{i}\right)\geq\frac{\mu_{k-1}}{k-1}\left(\sum_{i=1}^{k-1}h(x_{i})\cdot\prod_{j\in[k-1]\setminus i}x_{j}\right)=\frac{\mu_{k-1}}{k-1}\left(\sum_{i=1}^{k}h(x_{i})\cdot\prod_{j\in[k]\setminus i}x_{j}\right) |  |

and the claim follows from Lemma 4.3. ∎

## 5 Proofs of the main results

For random variables A 1, …, A k A_{1},\ldots,A_{k} taking values in { 0, 1 } n \{0,1\}^{n}, let A j, i ∈ { 0, 1 } A_{j,i}\in\{0,1\} be the restriction of A j A_{j} to the i i ’th coordinate and let A j, < i ∈ { 0, 1 } i − 1 A_{j,<i}\in\{0,1\}^{i-1} be the restriction of A j A_{j} to the first i − 1 i-1 coordinates. Let ∪ j = 1 k A j \cup_{j=1}^{k}A_{j} be the random variable taking values in { 0, 1 } n \{0,1\}^{n} whose i i ’th coordinate is zero if and only if A j, i = 0 A_{j,i}=0 for all j ∈ [k] j\in[k]. We similarly define ∪ j = 1 k A j, i ∈ { 0, 1 } \cup_{j=1}^{k}A_{j,i}\in\{0,1\} and ∪ j = 1 k A j, < i ∈ { 0, 1 } i − 1 \cup_{j=1}^{k}A_{j,<i}\in\{0,1\}^{i-1}. Given Corollary 4.6, we can generalize Claim 4.1 of [6].

###### Lemma 5.1.

Let A 1, …, A k A_{1},\ldots,A_{k} be mutually independent random variables taking values in { 0, 1 } n \{0,1\}^{n}. Assume for all i ∈ [n] i\in[n] and j ∈ [k] j\in[k] that Pr [A j, i = 0] ≥ p \Pr[A_{j,i}=0]\geq p. Then,

 | H ( ∪ j = 1 k A j) ≥ p k − 1 ​ μ k k ( ∑ j = 1 k H ( A j)). H(\cup_{j=1}^{k}A_{j})\geq\frac{p^{k-1}\mu_{k}}{k}\left(\sum_{j=1}^{k}H(A_{j})\right). |  |

###### Proof.

By the chain rule for entropy,

 | H ( ∪ j = 1 k A j) = ∑ i = 1 n H ( ∪ j = 1 k A j, i | ∪ j = 1 k A j, < i). H(\cup_{j=1}^{k}A_{j})=\sum_{i=1}^{n}H(\cup_{j=1}^{k}A_{j,i}\,|\,\cup_{j=1}^{k}A_{j,<i})\;. |  |

By the data processing inequality,

 | ∑ i = 1 n H ( ∪ j = 1 k A j, i | ∪ j = 1 k A j, < i) ≥ ∑ i = 1 n H ( ∪ j = 1 k A j, i | A 1, < i, A 2, < i, …, A k, < i). \sum_{i=1}^{n}H(\cup_{j=1}^{k}A_{j,i}\,|\,\cup_{j=1}^{k}A_{j,<i})\geq\sum_{i=1}^{n}H(\cup_{j=1}^{k}A_{j,i}\,|\,A_{1,<i},A_{2,<i},\ldots,A_{k,<i})\;. |  |

Let q j, i ​ ( x) = Pr ⁡ [A j, i = 0 | A j, < i = x] q_{j,i}(x)=\Pr[A_{j,i}=0\,|\,A_{j,<i}=x] (here x ∈ { 0, 1 } i − 1 x\in\{0,1\}^{i-1}). By Corollary 4.6,

 |  | H ( ∪ j = 1 k A j, i | A 1, < i = x 1, A 2, < i = x 2, …, A k, < i = x k) \displaystyle H(\cup_{j=1}^{k}A_{j,i}\,|\,A_{1,<i}=x_{1},A_{2,<i}=x_{2},\ldots,A_{k,<i}=x_{k}) |  |

 | = \displaystyle= | h ⁡ ( ∏ j = 1 k q j, i ​ ( x j)) ≥ μ k k ​ ( ∑ j = 1 k h ⁡ ( q j, i ​ ( x j)) ⋅ ∏ ℓ ∈ [k] ∖ j q ℓ, i ​ ( x ℓ)). \displaystyle h\left(\prod_{j=1}^{k}q_{j,i}(x_{j})\right)\geq\frac{\mu_{k}}{k}\left(\sum_{j=1}^{k}h(q_{j,i}(x_{j}))\cdot\prod_{\ell\in[k]\setminus j}q_{\ell,i}(x_{\ell})\right). |  |

Averaging over A 1, < i, …, A k, < i A_{1,<i},\ldots,A_{k,<i} which are mutually independent gives

 | H ( ∪ j = 1 k A j, i | A 1, < i, A 2, < i, …, A k, < i) \displaystyle H(\cup_{j=1}^{k}A_{j,i}\,|\,A_{1,<i},A_{2,<i},\ldots,A_{k,<i}) | ≥ μ k k ​ ( ∑ j = 1 k 𝔼 A j, < i ​ [h ⁡ ( q j, i ​ ( A j, < i))] ⋅ ∏ ℓ ∈ [k] ∖ j 𝔼 A ℓ, < i ​ [q ℓ, i ​ ( A ℓ, < i)]) \displaystyle\geq\frac{\mu_{k}}{k}\left(\sum_{j=1}^{k}{\mathbb{E}}_{A_{j,<i}}[h(q_{j,i}(A_{j,<i}))]\cdot\prod_{\ell\in[k]\setminus j}{\mathbb{E}}_{A_{\ell,<i}}[q_{\ell,i}(A_{\ell,<i})]\right) |  |

 |  | = μ k k ( ∑ j = 1 k H ( A j, i | A j, < i) ⋅ ∏ ℓ ∈ [k] ∖ j Pr [A ℓ, i = 0]). \displaystyle=\frac{\mu_{k}}{k}\left(\sum_{j=1}^{k}H(A_{j,i}\,|\,A_{j,<i})\cdot\prod_{\ell\in[k]\setminus j}\Pr[A_{\ell,i}=0]\right). |  |

Since Pr [A j, i = 0] ≥ p \Pr[A_{j,i}=0]\geq p we have

 | Pr [∪ j = 1 k A j, i] ≥ p k − 1 ​ μ k k ( ∑ j = 1 k H ( A j, i | A j, < i)). \Pr\left[\cup_{j=1}^{k}A_{j,i}\right]\geq\frac{p^{k-1}\mu_{k}}{k}\left(\sum_{j=1}^{k}H(A_{j,i}\,|\,A_{j,<i})\right)\;. |  |

The lemma then follows by summing over i ∈ [n] i\in[n]. ∎

Prior to proving our main results, we define the constant z k z_{k} stated in Theorem 1.6 and establish its correspondence with ψ k \psi_{k}. Let

 | z k ≔ 1 − μ k 1 / ( 1 − k). z_{k}\coloneqq 1-{\mu_{k}}^{1/(1-k)}\;. |  |

###### Proposition 5.2.

z k = ψ k z_{k}=\psi_{k} for k = 2, 3, 4 k=2,3,4. Furthermore,

 | z k > log ⁡ k 3 ​ k, 1 2 < z k ψ k ≤ 1, lim k → ∞ z k ψ k = log ⁡ 1 φ log ⁡ 2 ≈ 0.6943. z_{k}>\frac{\log k}{3k}\;,\qquad\frac{1}{2}<\frac{z_{k}}{\psi_{k}}\leq 1\;,\qquad\lim_{k\rightarrow\infty}\frac{z_{k}}{\psi_{k}}=\frac{\log\frac{1}{\varphi}}{\log 2}\approx 0.6943\;. |  |

###### Proof.

By the definitions of z k z_{k}, μ k \mu_{k}, φ k \varphi_{k}, α k \alpha_{k}, ψ k \psi_{k} we have z 2 = 1 − α 2 = ψ 2 z_{2}=1-\alpha_{2}=\psi_{2}, z 3 = 1 − ( α 3) 1 / 2 = 1 − φ 3 = ψ 3 z_{3}=1-(\alpha_{3})^{1/2}=1-\varphi_{3}=\psi_{3} and z 4 = 1 − ( α 4) 1 / 3 = 1 − φ 4 = ψ 4 z_{4}=1-(\alpha_{4})^{1/3}=1-\varphi_{4}=\psi_{4}.

By the definitions of φ k \varphi_{k} and α k \alpha_{k}, we have that F k ​ ( φ k) = 1 / α k F_{k}(\varphi_{k})=1/\alpha_{k}. By Lemma 4.2,

 | z k = 1 − μ k 1 / ( 1 − k) ≤ 1 − F k ​ ( φ k) 1 / ( 1 − k) = 1 − ( 1 α k) 1 / ( 1 − k) = 1 − α k 1 / ( k − 1) = 1 − φ k = ψ k. z_{k}=1-{\mu_{k}}^{1/(1-k)}\leq 1-F_{k}(\varphi_{k})^{1/(1-k)}=1-\left(\frac{1}{\alpha_{k}}\right)^{1/(1-k)}=1-\alpha_{k}^{1/(k-1)}=1-\varphi_{k}=\psi_{k}\;. |  |

Consider the function ( 1 − x) k − x (1-x)^{k}-x for which ψ k \psi_{k} is a root in ( 0, 1) (0,1). As this function is monotone decreasing in ( 0, 1) (0,1), ψ k \psi_{k} is its only root there. Since ( 1 − log ⁡ k / k) k − log ⁡ k / k < 0 (1-\log k/k)^{k}-\log k/k<0 for all k ≥ 3 k\geq 3, we have that ψ k < log ⁡ k / k \psi_{k}<\log k/k for all k ≥ 3 k\geq 3. Notice also that for every ε ∈ ( 0, 1) {\varepsilon}\in(0,1), ( 1 − ( 1 − ε) ​ log ⁡ k / k) k − ( 1 − ε) ​ log ⁡ k / k > 0 (1-(1-{\varepsilon})\log k/k)^{k}-(1-{\varepsilon})\log k/k>0 for all sufficiently large k k, thus ψ k = ( 1 − o ⁡ ( 1)) ​ log ⁡ k / k \psi_{k}=(1-o(1))\log k/k. In fact, it is easily verified that ϵ = 1 3 \epsilon=\frac{1}{3} works for all k ≥ 2 k\geq 2, hence ψ k ≥ ( 2 ​ log ⁡ k) / ( 3 ​ k) \psi_{k}\geq(2\log k)/(3k).

Now suppose that k = 2 p + q k=2^{p}+q where p = ⌊ log 2 ⁡ k ⌋ p=\lfloor\log_{2}k\rfloor. Notice that since μ k \mu_{k} is increasing with k k, we have that z k = 1 − μ k 1 / ( 1 − k) ≥ 1 − μ 2 p 1 / ( 1 − k) = 1 − φ ⌊ log 2 ⁡ k ⌋ / ( k − 1) z_{k}=1-{\mu_{k}}^{1/(1-k)}\geq 1-{\mu_{2^{p}}}^{1/(1-k)}=1-\varphi^{\lfloor\log_{2}k\rfloor/(k-1)}.

Using the inequality e − x ≤ 1 − x + x 2 / 2 e^{-x}\leq 1-x+x^{2}/2 valid for all x ≥ 0 x\geq 0 we have

 | z k ψ k \displaystyle\frac{z_{k}}{\psi_{k}} | ≥ 1 − φ ⌊ log 2 ⁡ k ⌋ / ( k − 1) log ⁡ k / k \displaystyle\geq\frac{1-\varphi^{\lfloor\log_{2}k\rfloor/(k-1)}}{\log k/k} |  | (5) |

 |  | = 1 − e − log ⁡ ( 1 / φ) ​ ⌊ log 2 ⁡ k ⌋ k − 1 log ⁡ k / k \displaystyle=\frac{1-e^{-\log(1/\varphi)\frac{\lfloor\log_{2}k\rfloor}{k-1}}}{\log k/k} |  |

 |  | ≥ 1 − e − log ⁡ ( 1 / φ) log ⁡ 2 ​ ( log ⁡ k) − 1 k − 1 log ⁡ k / k \displaystyle\geq\frac{1-e^{-\frac{\log(1/\varphi)}{\log 2}\frac{(\log k)-1}{k-1}}}{\log k/k} |  |

 |  | ≥ log ⁡ ( 1 / φ) log ⁡ 2 ​ ( log ⁡ k) − 1 k − 1 − log 2 ⁡ ( 1 / φ) 2 ​ log 2 ​ 2 ​ ( ( log ⁡ k) − 1) 2 ( k − 1) 2 log ⁡ k / k \displaystyle\geq\frac{\frac{\log(1/\varphi)}{\log 2}\frac{(\log k)-1}{k-1}-\frac{\log^{2}(1/\varphi)}{2\log^{2}2}\frac{((\log k)-1)^{2}}{(k-1)^{2}}}{\log k/k} |  |

 |  | ≥ log ⁡ ( 1 / φ) log ⁡ 2 ​ ( ( log ⁡ k) − 1) − log 2 ⁡ ( 1 / φ) 2 ​ log 2 ​ 2 ​ ( ( log ⁡ k) − 1) 2 ( k − 1) log ⁡ k. \displaystyle\geq\frac{\frac{\log(1/\varphi)}{\log 2}((\log k)-1)-\frac{\log^{2}(1/\varphi)}{2\log^{2}2}\frac{((\log k)-1)^{2}}{(k-1)}}{\log k}\;. |  | (6) |

We immediately obtain from the last inequality that

 | lim inf k → ∞ z k ψ k ≥ log ⁡ 1 φ log ⁡ 2. \liminf_{k\rightarrow\infty}\frac{z_{k}}{\psi_{k}}\geq\frac{\log\frac{1}{\varphi}}{\log 2}\;. |  |

To see that this is, in fact, a limit, just repeat the last series of inequalities by (i) reversing each inequality; (ii) using the lower bound ψ k ≥ ( 1 − o ⁡ ( 1) ​ log ⁡ k / k CLOSE \psi_{k}\geq(1-o(1)\log k/k; (iii) using the upper bound z k = 1 − μ k 1 / ( 1 − k) ≤ 1 − μ 2 p + 1 1 / ( 1 − k) = 1 − φ 1 + ⌊ log 2 ⁡ k ⌋ / ( k − 1) z_{k}=1-{\mu_{k}}^{1/(1-k)}\leq 1-{\mu_{2^{p+1}}}^{1/(1-k)}=1-\varphi^{1+\lfloor\log_{2}k\rfloor/(k-1)}; (iv) apply the inequality e − x ≥ 1 − x e^{-x}\geq 1-x.

Finally, it is easily verified that ( 5) is larger than 1 2 \frac{1}{2} for k ≤ 100 k\leq 100 and ( 6) is larger than 1 2 \frac{1}{2} for k > 100 k>100. Thus, z k / ψ k > 1 2 z_{k}/\psi_{k}>\frac{1}{2} and z k > ψ k / 2 ≥ ( log ⁡ k) / ( 3 ​ k) z_{k}>\psi_{k}/2\geq(\log k)/(3k). ∎

###### Proof of Theorems 1.6 and 1.7.

Let ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, ℱ ≠ { ∅ } {\mathcal{F}}\neq\{\emptyset\} be a ( 1 − ε) (1-{\varepsilon}) -approximate k k -union closed set system, where 0 ≤ ε < 1 2 0\leq{\varepsilon}<\frac{1}{2}. Let p i p_{i} be the fraction of sets in ℱ {\mathcal{F}} that do not contain i i and let p = min i ∈ [n] ⁡ p i p=\min_{i\in[n]}p_{i}. Let A 1, …, A k A_{1},\ldots,A_{k} be a k k -tuple of sets of ℱ {\mathcal{F}}, where A j A_{j} is chosen uniformly and independently of the other sets. By Lemma 5.1 we obtain:

 | H ( ∪ j = 1 k A j) ≥ p k − 1 ​ μ k k ( ∑ j = 1 k H ( A j)) = p k − 1 μ k log | ℱ |. H(\cup_{j=1}^{k}A_{j})\geq\frac{p^{k-1}\mu_{k}}{k}\left(\sum_{j=1}^{k}H(A_{j})\right)=p^{k-1}\mu_{k}\log|{\mathcal{F}}|\;. |  |

As in [6], we show that H ( ∪ j = 1 k A j) H(\cup_{j=1}^{k}A_{j}) cannot be much larger than log ⁡ | ℱ | \log|{\mathcal{F}}|. Let I I be the indicator for the event ∪ j = 1 k A j ∈ ℱ \cup_{j=1}^{k}A_{j}\in{\mathcal{F}} where by assumption Pr [I = 1] ≥ 1 − ϵ \Pr[I=1]\geq 1-\epsilon. We have

 | H ( ∪ j = 1 k A j) ≤ H ( ∪ j = 1 k A j, I) = H ( I) + H ( ∪ j = 1 k A j | I = 0) Pr [I = 0] + H ( ∪ j = 1 k A j | I = 1) P r [I = 1]. H(\cup_{j=1}^{k}A_{j})\leq H(\cup_{j=1}^{k}A_{j},I)=H(I)+H(\cup_{j=1}^{k}A_{j}\,|\,I=0)\Pr[I=0]+H(\cup_{j=1}^{k}A_{j}\,|\,I=1)Pr[I=1]\;. |  |

We bound the terms in the last inequality. Since I ∈ { 0, 1 } I\in\{0,1\}, and Pr [I = 0] ≤ ε < 1 2 \Pr[I=0]\leq{\varepsilon}<\frac{1}{2}, we have H ⁡ ( I) ≤ h ⁡ ( ε) ≤ 2 ​ ε ​ log ⁡ ( 1 / ε) H(I)\leq h({\varepsilon})\leq 2{\varepsilon}\log(1/{\varepsilon}). Also note that H ( ∪ j = 1 k A j | I = 0) ≤ H ( A 1, A 2, …, A k | I = 0) ≤ k log | F | H(\cup_{j=1}^{k}A_{j}\,|\,I=0)\leq H(A_{1},A_{2},\ldots,A_{k}\,|\,I=0)\leq k\log|F|. Finally, notice that ( ∪ j = 1 k A j | I = 1) (\cup_{j=1}^{k}A_{j}\,|\,I=1) is a distribution supported on ℱ {\mathcal{F}} and so H ( ∪ j = 1 k A j | I = 1) ≤ log | ℱ | H(\cup_{j=1}^{k}A_{j}\,|\,I=1)\leq\log|{\mathcal{F}}|. We therefore have

 | p k − 1 μ k log | ℱ | ≤ H ( ∪ j = 1 k A j) ≤ 2 ε log ( 1 / ε) + ( 1 + k ϵ) log | ℱ | p^{k-1}\mu_{k}\log|{\mathcal{F}}|\leq H(\cup_{j=1}^{k}A_{j})\leq 2{\varepsilon}\log(1/{\varepsilon})+(1+k\epsilon)\log|{\mathcal{F}}| |  |

from which we immediately obtain

 | 1 − p ≥ 1 − μ k 1 / ( 1 − k) − ( k ​ ε + 2 ​ ε ​ log ⁡ ( 1 / ε) log ⁡ | ℱ |) 1 / ( k − 1) = z k − ( k ​ ε + 2 ​ ε ​ log ⁡ ( 1 / ε) log ⁡ | ℱ |) 1 / ( k − 1). 1-p\geq 1-{\mu_{k}}^{1/(1-k)}-\left(k{\varepsilon}+\frac{2{\varepsilon}\log(1/{\varepsilon})}{\log|{\mathcal{F}}|}\right)^{1/(k-1)}=z_{k}-\left(k{\varepsilon}+\frac{2{\varepsilon}\log(1/{\varepsilon})}{\log|{\mathcal{F}}|}\right)^{1/(k-1)}\;. |  |

Theorems 1.6 and 1.7 now follow from Proposition 5.2. ∎

Finally, by Lemma 3.10, Conjecture 3.9 implies Conjecture 3.1, and Conjecture 3.1 implies the validity of Corollary 3.13 for all k k (not just k = 2, 3, 4 k=2,3,4), which in turn, means that we can define μ k = 1 / α k \mu_{k}=1/\alpha_{k} for all k k (not just k = 2, 3, 4 k=2,3,4), which implies Conjecture 1.5. Stated directly: if p k ​ ( x) p_{k}(x) has at most two real roots in ( 0, 1) (0,1), then Conjecture 1.5 holds.

## References

- [1] The On-line Encyclopedia of Integer Sequences, sequence a108267. https://oeis.org/A108267.
- [2] R. Alweiss, B. Huang, and M. Sellke. Improved lower bound for Frankl’s union-closed sets conjecture. arXiv preprint arXiv:2211.11731, 2022.
- [3] R. B. Boppana. Amplification of probabilistic boolean formulas. In 26th Annual Symposium on Foundations of Computer Science (FOCS), pages 20–29. IEEE, 1985.
- [4] R. B. Boppana. A useful inequality for the binary entropy function. arXiv preprint arXiv:2301.09664, 2023.
- [5] S. Cambie. Better bounds for the union-closed sets conjecture using the entropy approach. arXiv preprint arXiv:2212.12500, 2022.
- [6] Z. Chase and S. Lovett. Approximate union closed conjecture. arXiv preprint arXiv:2211.11689, 2022.
- [7] D. Ellis. Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture. arXiv preprint arXiv:2211.12401, 2022.
- [8] J. Gilmer. A constant lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.09055, 2022.
- [9] L. Pebody. Extension of a method of Gilmer. arXiv preprint arXiv:2211.13139, 2022.
- [10] W. Sawin. An improved lower bound for the union-closed set conjecture. arXiv preprint arXiv:2211.11504, 2022.
- [11] L. Yu. Dimension-free bounds for the union-closed sets conjecture. arXiv preprint arXiv:2212.00658, 2022.

## Appendix A The real root pattern of the derivatives of p 4 p_{4}

we prove that the number of real roots of the derivatives of p 4 p_{4} follows the sequence

 | ( 3, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 1) (3,2,3,2,1,2,3,2,1,2,3,2,1,2,1) |  |

where the i i ’th coordinate (starting at i = 0 i=0) is the number of real roots of p 4 ( i) ​ ( x) {p_{4}}^{(i)}(x). For referential convenience, the derivatives of interest are:

 | p 4 ( 1) \displaystyle{p_{4}}^{(1)} | = 10 + 40 ​ x + 105 ​ x 2 + 4 ​ ( − 496 ​ α 4 + 40) ​ x 3 + 220 ​ x 4 + 240 ​ x 5 + 175 ​ x 6 + 8 ​ ( − 496 ​ α 4 + 20) ​ x 7 + 90 ​ x 8 + 40 ​ x 9 + 55 ​ x 10 − 192 ​ α 4 ​ x 11 − 15 ​ x 14; \displaystyle={\scriptstyle 10+40x+105x^{2}+4(-496\alpha_{4}+40)x^{3}+220x^{4}+240x^{5}+175x^{6}+8(-496\alpha_{4}+20)x^{7}+90x^{8}+40x^{9}+55x^{10}-192\alpha_{4}x^{11}-15x^{14}}; |  |

 | p 4 ( 2) \displaystyle{p_{4}}^{(2)} | = 40 + 210 ​ x + 12 ​ ( − 496 ​ α 4 + 40) ​ x 2 + 880 ​ x 3 + 1200 ​ x 4 + 1050 ​ x 5 + 56 ​ ( − 496 ​ α 4 + 20) ​ x 6 + 720 ​ x 7 + 360 ​ x 8 + 550 ​ x 9 − 2112 ​ α 4 ​ x 10 − 210 ​ x 13; \displaystyle={\scriptstyle 40+210x+12(-496\alpha_{4}+40)x^{2}+880x^{3}+1200x^{4}+1050x^{5}+56(-496\alpha_{4}+20)x^{6}+720x^{7}+360x^{8}+550x^{9}-2112\alpha_{4}x^{10}-210x^{13}}; |  |

 | p 4 ( 4) \displaystyle{p_{4}}^{(4)} | = − 11904 ​ α 4 + 960 + 5280 ​ x + 14400 ​ x 2 + 21000 ​ x 3 + 1680 ​ ( − 496 ​ α 4 + 20) ​ x 4 + 30240 ​ x 5 + 20160 ​ x 6 + 39600 ​ x 7 − 190080 ​ α 4 ​ x 8 − 32760 ​ x 11; \displaystyle={\scriptstyle-11904\alpha_{4}+960+5280x+14400x^{2}+21000x^{3}+1680(-496\alpha_{4}+20)x^{4}+30240x^{5}+20160x^{6}+39600x^{7}-190080\alpha_{4}x^{8}-32760x^{11}}; |  |

 | p 4 ( 5) \displaystyle{p_{4}}^{(5)} | = 5280 + 28800 ​ x + 63000 ​ x 2 + 6720 ​ ( − 496 ​ α 4 + 20) ​ x 3 + 151200 ​ x 4 + 120960 ​ x 5 + 277200 ​ x 6 − 1520640 ​ α 4 ​ x 7 − 360360 ​ x 10; \displaystyle={\scriptstyle 5280+28800x+63000x^{2}+6720(-496\alpha_{4}+20)x^{3}+151200x^{4}+120960x^{5}+277200x^{6}-1520640\alpha_{4}x^{7}-360360x^{10}}; |  |

 | p 4 ( 6) \displaystyle{p_{4}}^{(6)} | = 28800 + 126000 ​ x + 20160 ​ ( − 496 ​ α 4 + 20) ​ x 2 + 604800 ​ x 3 + 604800 ​ x 4 + 1663200 ​ x 5 − 10644480 ​ α 4 ​ x 6 − 3603600 ​ x 9; \displaystyle={\scriptstyle 28800+126000x+20160(-496\alpha_{4}+20)x^{2}+604800x^{3}+604800x^{4}+1663200x^{5}-10644480\alpha_{4}x^{6}-3603600x^{9}}; |  |

 | p 4 ( 8) \displaystyle{p_{4}}^{(8)} | = − 19998720 ​ α 4 + 806400 + 3628800 ​ x + 7257600 ​ x 2 + 33264000 ​ x 3 − 319334400 ​ α 4 ​ x 4 − 259459200 ​ x 7; \displaystyle={\scriptstyle-19998720\alpha_{4}+806400+3628800x+7257600x^{2}+33264000x^{3}-319334400\alpha_{4}x^{4}-259459200x^{7}}; |  |

 | p 4 ( 9) \displaystyle{p_{4}}^{(9)} | = 3628800 + 14515200 ​ x + 99792000 ​ x 2 − 1277337600 ​ α 4 ​ x 3 − 1816214400 ​ x 6; \displaystyle={\scriptstyle 3628800+14515200x+99792000x^{2}-1277337600\alpha_{4}x^{3}-1816214400x^{6}}; |  |

 | p 4 ( 10) \displaystyle{p_{4}}^{(10)} | = 14515200 + 199584000 ​ x − 3832012800 ​ α 4 ​ x 2 − 10897286400 ​ x 5; \displaystyle={\scriptstyle 14515200+199584000x-3832012800\alpha_{4}x^{2}-10897286400x^{5}}; |  |

 | p 4 ( 12) \displaystyle{p_{4}}^{(12)} | = − 7664025600 ​ α 4 − 217945728000 ​ x 3; \displaystyle={\scriptstyle-7664025600\alpha_{4}-217945728000x^{3}}; |  |

Clearly p 4 ( 13) ​ ( x) {p_{4}}^{(13)}(x) is a parabola with a double root at x = 0 x=0 and p 4 ( 14) ​ ( x) {p_{4}}^{(14)}(x) is linear, so has a single root. Observing the cubic p 4 ( 12) ​ ( x) {p_{4}}^{(12)}(x), we see that it has one real root. This implies that p 4 ( 10) ​ ( x) {p_{4}}^{(10)}(x) has at most three real roots. Indeed, it has three since α 4 ≈ 0.3802 \alpha_{4}\approx 0.3802 and

 |  | p 4 ( 10) ​ ( − 0.2) \displaystyle{p_{4}}^{(10)}\left(-0.2\right) | = \displaystyle~= | − 2739308544 125 − 153280512 ​ α 4 \displaystyle~-\tfrac{2739308544}{125}-153280512\alpha_{4} | < 0, \displaystyle~<0\,, |  |

 |  | p 4 ( 10) ​ ( 0) \displaystyle{p_{4}}^{(10)}\left(0\right) | = \displaystyle~= | 14515200 \displaystyle~14515200 | > 0. \displaystyle>0\,. |  |

Let γ 10, 1 ∈ ( − ∞, − 0.2) \gamma_{10,1}\in(-\infty,-0.2), γ 10, 2 ∈ ( − 0.2, 0) \gamma_{10,2}\in(-0.2,0), γ 10, 3 ∈ ( 0, ∞) \gamma_{10,3}\in(0,\infty) be the real roots of p 4 ( 10) ​ ( x) {p_{4}}^{(10)}(x).

As p 4 ( 9) ​ ( x) {p_{4}}^{(9)}(x) has even degree and negative leading coefficient, it must be that γ 10, 2 \gamma_{10,2} is a local minimum of p 4 ( 9) ​ ( x) {p_{4}}^{(9)}(x). To prove that p 4 ( 9) ​ ( x) {p_{4}}^{(9)}(x) has at most two real roots, we show that p 4 ( 9) ​ ( γ 10, 2) > 0 {p_{4}}^{(9)}(\gamma_{10,2})>0. Indeed, p 4 ( 9) ​ ( 0) = 3628800 {p_{4}}^{(9)}(0)=3628800. Now, for every x ∈ [− 0.2, 0] x\in[-0.2,0] we have

 | p 4 ( 9) ​ ( x) − p 4 ( 9) ​ ( 0) \displaystyle{p_{4}}^{(9)}(x)-{p_{4}}^{(9)}(0) | = 14515200 ​ x + 99792000 ​ x 2 − 1277337600 ​ α 4 ​ x 3 − 1816214400 ​ x 6 \displaystyle=14515200x+99792000x^{2}-1277337600\alpha_{4}x^{3}-1816214400x^{6} |  |

 |  | ≥ 14515200 ​ ( − 1 5) − 1816214400 ​ ( 1 5 6) \displaystyle\geq 14515200\left(-\tfrac{1}{5}\right)-1816214400\left(\tfrac{1}{5^{6}}\right) |  |

 |  | > − 3628800. \displaystyle>-3628800\;. |  |

As γ 10, 2 ∈ ( − 0.2, 0) \gamma_{10,2}\in(-0.2,0), we have that p 4 ( 9) ​ ( γ 10, 2) > 0 {p_{4}}^{(9)}(\gamma_{10,2})>0. We have shown that p 4 ( 9) ​ ( x) {p_{4}}^{(9)}(x) has at most two real roots. Indeed, it has two since

 |  | p 4 ( 9) ​ ( 0) \displaystyle{p_{4}}^{(9)}\left(0\right) | = \displaystyle~= | 3628800 \displaystyle~3628800 | > 0, \displaystyle>0\,, |  |

 |  | p 4 ( 9) ​ ( 0.4) \displaystyle{p_{4}}^{(9)}\left(0.4\right) | = \displaystyle~= | 11226491136 625 − 408748032 5 ​ α 4 \displaystyle~\tfrac{11226491136}{625}-\tfrac{408748032}{5}\alpha_{4} | < 0. \displaystyle~<0\,. |  |

Let γ 9, 1 ∈ ( − ∞, 0) \gamma_{9,1}\in(-\infty,0), γ 9, 2 ∈ ( 0, 0.4) \gamma_{9,2}\in(0,0.4) be the real roots of p 4 ( 9) ​ ( x) {p_{4}}^{(9)}(x).

As p 4 ( 8) ​ ( x) {p_{4}}^{(8)}(x) has odd degree and negative leading coefficient, it must be that γ 9, 2 \gamma_{9,2} is a local maximum of p 4 ( 8) ​ ( x) {p_{4}}^{(8)}(x). To prove that p 4 ( 8) ​ ( x) {p_{4}}^{(8)}(x) has at most one real root, we show that p 4 ( 8) ​ ( γ 9, 2) < 0 {p_{4}}^{(8)}(\gamma_{9,2})<0. Indeed, p 4 ( 8) ​ ( 0) = − 19998720 ​ α 4 + 806400 < − 6000000 {p_{4}}^{(8)}(0)=-19998720\alpha_{4}+806400<-6000000. Now, for every x ∈ [0, 0.4] x\in[0,0.4] we have

 | p 4 ( 8) ​ ( x) − p 4 ( 8) ​ ( 0) \displaystyle{p_{4}}^{(8)}(x)-{p_{4}}^{(8)}(0) | = 3628800 ​ x + 7257600 ​ x 2 + 33264000 ​ x 3 − 319334400 ​ α 4 ​ x 4 − 259459200 ​ x 7 \displaystyle=3628800x+7257600x^{2}+33264000x^{3}-319334400\alpha_{4}x^{4}-259459200x^{7} |  |

 |  | ≤ 3628800 ​ ( 2 5) + 7257600 ​ ( 4 25) + 33264000 ​ ( 8 125) \displaystyle\leq 3628800\left(\tfrac{2}{5}\right)+7257600\left(\tfrac{4}{25}\right)+33264000\left(\tfrac{8}{125}\right) |  |

 |  | < 5000000. \displaystyle<5000000\;. |  |

As γ 9, 2 ∈ ( 0, 0.4) \gamma_{9,2}\in(0,0.4), we have that p 4 ( 8) ​ ( γ 9, 2) < 0 {p_{4}}^{(8)}(\gamma_{9,2})<0. We have shown that p 4 ( 8) ​ ( x) {p_{4}}^{(8)}(x) has at most one real root.

As p 4 ( 8) ​ ( x) {p_{4}}^{(8)}(x) has at most one real root, it follows that p 4 ( 6) ​ ( x) {p_{4}}^{(6)}(x) has at most three real roots. Indeed, it has three since

 |  | p 4 ( 6) ​ ( − 0.15) \displaystyle{p_{4}}^{(6)}\left(-0.15\right) | = \displaystyle~= | 21901848684147 1280000000 − 2813835591 12500 ​ α 4 \displaystyle~\tfrac{21901848684147}{1280000000}-\tfrac{2813835591}{12500}\alpha_{4} | < 0, \displaystyle~<0\,, |  |

 |  | p 4 ( 6) ​ ( 0) \displaystyle{p_{4}}^{(6)}\left(0\right) | = \displaystyle~= | 28800 \displaystyle~28800 | > 0. \displaystyle>0\,. |  |

Let γ 6, 1 ∈ ( − ∞, − 0.2) \gamma_{6,1}\in(-\infty,-0.2), γ 6, 2 ∈ ( − 0.15, 0) \gamma_{6,2}\in(-0.15,0), γ 6, 3 ∈ ( 0, ∞) \gamma_{6,3}\in(0,\infty) be the real roots of p 4 ( 6) ​ ( x) {p_{4}}^{(6)}(x).

As p 4 ( 5) ​ ( x) {p_{4}}^{(5)}(x) has even degree and negative leading coefficient, it must be that γ 6, 2 \gamma_{6,2} is a local minimum of p 4 ( 5) ​ ( x) {p_{4}}^{(5)}(x). To prove that p 4 ( 5) ​ ( x) {p_{4}}^{(5)}(x) has at most two real roots, we show that p 4 ( 5) ​ ( γ 6, 2) > 0 {p_{4}}^{(5)}(\gamma_{6,2})>0. Indeed, p 4 ( 5) ​ ( 0) = 5280 {p_{4}}^{(5)}(0)=5280. Now, for every x ∈ [− 0.15, 0] x\in[-0.15,0] we have

 | p 4 ( 5) ​ ( x) − p 4 ( 5) ​ ( 0) \displaystyle{p_{4}}^{(5)}(x)-{p_{4}}^{(5)}(0) | = 28800 ​ x + 63000 ​ x 2 + 6720 ​ ( − 496 ​ α 4 + 20) ​ x 3 + 151200 ​ x 4 + 120960 ​ x 5 \displaystyle=28800x+63000x^{2}+6720(-496\alpha_{4}+20)x^{3}+151200x^{4}+120960x^{5} |  |

 |  | + 277200 ​ x 6 − 1520640 ​ α 4 ​ x 7 − 360360 ​ x 10 \displaystyle\quad+277200x^{6}-1520640\alpha_{4}x^{7}-360360x^{10} |  |

 |  | ≥ 28800 ​ ( − 3 20) + 120960 ​ ( − 3 20) 5 − 360360 ​ ( − 3 20) 10 \displaystyle\geq 28800\left(-\tfrac{3}{20}\right)+120960\left(-\tfrac{3}{20}\right)^{5}-360360\left(-\tfrac{3}{20}\right)^{10} |  |

 |  | > − 4400. \displaystyle>-4400\;. |  |

As γ 6, 2 ∈ ( − 0.15, 0) \gamma_{6,2}\in(-0.15,0), we have that p 4 ( 5) ​ ( γ 6, 2) > 0 {p_{4}}^{(5)}(\gamma_{6,2})>0. We have shown that p 4 ( 5) ​ ( x) {p_{4}}^{(5)}(x) has at most two real roots. Indeed, it has two since

 |  | p 4 ( 5) ​ ( 0) \displaystyle{p_{4}}^{(5)}\left(0\right) | = \displaystyle~= | 5280 \displaystyle~5280 | > 0, \displaystyle>0\,, |  |

 |  | p 4 ( 5) ​ ( 0.25) \displaystyle{p_{4}}^{(5)}\left(0.25\right) | = \displaystyle~= | 2528848395 131072 − 834765 16 ​ α 4 \displaystyle~\tfrac{2528848395}{131072}-\tfrac{834765}{16}\alpha_{4} | < 0. \displaystyle~<0\,. |  |

Let γ 5, 1 ∈ ( − ∞, 0) \gamma_{5,1}\in(-\infty,0), γ 5, 2 ∈ ( 0, 0.25) \gamma_{5,2}\in(0,0.25) be the real roots of p 4 ( 5) ​ ( x) {p_{4}}^{(5)}(x).

As p 4 ( 4) ​ ( x) {p_{4}}^{(4)}(x) has odd degree and negative leading coefficient, it must be that γ 5, 2 \gamma_{5,2} is its local maximum. To prove that p 4 ( 4) ​ ( x) {p_{4}}^{(4)}(x) has at most one real root, we show that p 4 ( 4) ​ ( γ 5, 2) < 0 {p_{4}}^{(4)}(\gamma_{5,2})<0. Indeed, p 4 ( 4) ​ ( 0) = − 11904 ​ α 4 + 960 < − 3565 {p_{4}}^{(4)}(0)=-11904\alpha_{4}+960<-3565. Now, for every x ∈ [0, 0.25] x\in[0,0.25] we have

 | p 4 ( 4) ​ ( x) − p 4 ( 4) ​ ( 0) \displaystyle{p_{4}}^{(4)}(x)-{p_{4}}^{(4)}(0) | = 5280 ​ x + 14400 ​ x 2 + 21000 ​ x 3 + 1680 ​ ( − 496 ​ α 4 + 20) ​ x 4 + 30240 ​ x 5 + 20160 ​ x 6 \displaystyle=5280x+14400x^{2}+21000x^{3}+1680(-496\alpha_{4}+20)x^{4}+30240x^{5}+20160x^{6} |  |

 |  | + 39600 ​ x 7 − 190080 ​ α 4 ​ x 8 − 32760 ​ x 11 \displaystyle\quad+39600x^{7}-190080\alpha_{4}x^{8}-32760x^{11} |  |

 |  | ≤ 5280 ​ x + 14400 ​ x 2 + 21000 ​ x 3 + 30240 ​ x 5 + 20160 ​ x 6 + 39600 ​ x 7 \displaystyle\leq 5280x+14400x^{2}+21000x^{3}+30240x^{5}+20160x^{6}+39600x^{7} |  |

 |  | < 5280 ​ ( 1 4) + 14400 ​ ( 1 4) 2 + 21000 ​ ( 1 4) 3 + 30240 ​ ( 1 4) 5 + 20160 ​ ( 1 4) 6 + 39600 ​ ( 1 4) 7 \displaystyle<5280\left(\tfrac{1}{4}\right)+14400\left(\tfrac{1}{4}\right)^{2}+21000\left(\tfrac{1}{4}\right)^{3}+30240\left(\tfrac{1}{4}\right)^{5}+20160\left(\tfrac{1}{4}\right)^{6}+39600\left(\tfrac{1}{4}\right)^{7} |  |

 |  | < 2600. \displaystyle<2600\;. |  |

As γ 5, 2 ∈ ( 0, 0.25) \gamma_{5,2}\in(0,0.25), we have that p 4 ( 4) ​ ( γ 5, 2) < 0 {p_{4}}^{(4)}(\gamma_{5,2})<0. Hence, p 4 ( 4) ​ ( x) {p_{4}}^{(4)}(x) has at most one real root.

As p 4 ( 4) ​ ( x) {p_{4}}^{(4)}(x) has at most one real root, it follows that p 4 ( 2) ​ ( x) {p_{4}}^{(2)}(x) has at most three real roots. Indeed, it has three since

 |  | p 4 ( 2) ​ ( − 0.2) \displaystyle{p_{4}}^{(2)}\left(-0.2\right) | = \displaystyle~= | 2882593792 244140625 − 2342362112 9765625 ​ α 4 \displaystyle~\tfrac{2882593792}{244140625}-\tfrac{2342362112}{9765625}\alpha_{4} | < 0, \displaystyle~<0\,, |  |

 |  | p 4 ( 2) ​ ( 0) \displaystyle{p_{4}}^{(2)}\left(0\right) | = \displaystyle~= | 40 \displaystyle~40 | > 0. \displaystyle>0\,. |  |

Let γ 2, 1 ∈ ( − ∞, − 0.2) \gamma_{2,1}\in(-\infty,-0.2), γ 2, 2 ∈ ( − 0.2, 0) \gamma_{2,2}\in(-0.2,0), γ 2, 3 ∈ ( 0, ∞) \gamma_{2,3}\in(0,\infty) be the real roots of p 4 ( 2) ​ ( x) {p_{4}}^{(2)}(x).

As p 4 ( 1) ​ ( x) {p_{4}}^{(1)}(x) has even degree and negative leading coefficient, it must be that γ 2, 2 \gamma_{2,2} is a local minimum of p 4 ( 1) ​ ( x) {p_{4}}^{(1)}(x). To prove that p 4 ( 1) ​ ( x) {p_{4}}^{(1)}(x) has at most two real roots, we show that p 4 ( 1) ​ ( γ 2, 2) > 0 {p_{4}}^{(1)}(\gamma_{2,2})>0. Indeed, p 4 ( 1) ​ ( 0) = 10 {p_{4}}^{(1)}(0)=10. Now, for every x ∈ [− 0.2, 0] x\in[-0.2,0] we have

 | p 4 ( 1) ​ ( x) − p 4 ( 1) ​ ( 0) \displaystyle{p_{4}}^{(1)}(x)-{p_{4}}^{(1)}(0) | = 40 ​ x + 105 ​ x 2 + 4 ​ ( − 496 ​ α 4 + 40) ​ x 3 + 220 ​ x 4 + 240 ​ x 5 + 175 ​ x 6 \displaystyle=40x+105x^{2}+4(-496\alpha_{4}+40)x^{3}+220x^{4}+240x^{5}+175x^{6} |  |

 |  | + 8 ​ ( − 496 ​ α 4 + 20) ​ x 7 + 90 ​ x 8 + 40 ​ x 9 + 55 ​ x 10 − 192 ​ α 4 ​ x 11 − 15 ​ x 14 \displaystyle\quad+8(-496\alpha_{4}+20)x^{7}+90x^{8}+40x^{9}+55x^{10}-192\alpha_{4}x^{11}-15x^{14} |  |

 |  | ≥ 40 ​ x + 240 ​ x 5 + 40 ​ x 9 − 15 ​ x 14 \displaystyle\geq 40x+240x^{5}+40x^{9}-15x^{14} |  |

 |  | ≥ 40 ​ ( − 1 5) + 240 ​ ( − 1 5) 5 + 40 ​ ( − 1 5) 9 − 15 ​ ( − 1 5) 14 \displaystyle\geq 40\left(-\tfrac{1}{5}\right)+240\left(-\tfrac{1}{5}\right)^{5}+40\left(-\tfrac{1}{5}\right)^{9}-15\left(-\tfrac{1}{5}\right)^{14} |  |

 |  | > − 9. \displaystyle>-9\;. |  |

As γ 2, 2 ∈ ( − 0.2, 0) \gamma_{2,2}\in(-0.2,0), we have that p 4 ( 1) ​ ( γ 2, 2) > 0 {p_{4}}^{(1)}(\gamma_{2,2})>0. We have shown that p 4 ( 1) ​ ( x) {p_{4}}^{(1)}(x) has at most two real roots. Hence p 4 ​ ( x) p_{4}(x) has at most three real roots. By the comment after Lemma 3.10, it must have precisely three. ∎


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
