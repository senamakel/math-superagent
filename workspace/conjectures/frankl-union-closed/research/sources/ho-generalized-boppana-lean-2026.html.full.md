<!-- source: https://arxiv.org/html/2601.19327v1 | converted from HTML -->

A generalization of Boppana’s entropy inequality

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2601.19327v1 [math.CO] 27 Jan 2026

# A generalization of Boppana’s entropy inequality

Boon Suan Ho Address: Department of Mathematics, National University of Singapore Email address: [hbs@u.nus.edu][3]

###### Abstract.

In recent progress on the union-closed sets conjecture, a key lemma has been Boppana’s entropy inequality: h ⁡ ( x 2) ≥ ϕ ​ x ​ h ​ ( x) h(x^{2})\geq\phi xh(x), where ϕ = ( 1 + 5) / 2 \phi=(1+\sqrt{5})/2 and h ⁡ ( x) = − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) h(x)=-x\log x-(1-x)\log(1-x). In this note, we prove that the generalized inequality α k ​ h ​ ( x k) ≥ x k − 1 ​ h ​ ( x) \alpha_{k}h(x^{k})\geq x^{k-1}h(x), first conjectured by Yuster, holds for real k > 1 k>1, where α k \alpha_{k} is the unique positive solution to x ​ ( 1 + x) k − 1 = 1 x(1+x)^{k-1}=1. This implies an analogue of the union-closed sets conjecture for approximate k k -union closed set systems. We also formalize our proof in Lean 4.

## 1. Introduction

The *union-closed sets conjecture*states that for every family { ∅ } ≠ ℱ ⊆ 2 [n] \{\varnothing\}\neq\mathcal{F}\subseteq 2^{[n]} of sets closed under unions, there exists i ∈ [n] i\in[n] that is contained in c = 1 / 2 c=1/2 of the sets of ℱ \mathcal{F}. The problem was posed in 1979, but no proof for any c > 0 c>0 was found until 2022, when Gilmer [4] gave an information-theoretic proof for the c = 0.01 c=0.01 case. His argument was quickly optimized to work for c = ( 3 − 5) / 2 ≈ 0.382 c=(3-\sqrt{5})/2\approx 0.382 by several authors, who all made use of *Boppana’s entropy inequality*[6] as a key ingredient:

###### Proposition 1.

Let log \log denote the natural logarithm, and define the binary entropy function h ⁡ ( x) ≔ − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) h(x)\coloneqq-x\log x-(1-x)\log(1-x) for 0 < x < 1 0<x<1, setting h ⁡ ( 0) = h ⁡ ( 1) = 0 h(0)=h(1)=0. Then h ⁡ ( x 2) ≥ ϕ ​ x ​ h ​ ( x) h(x^{2})\geq\phi xh(x) for 0 ≤ x ≤ 1 0\leq x\leq 1, where ϕ = ( 1 + 5) / 2 \phi=(1+\sqrt{5})/2, and equality holds iff x = 0 x=0, 1 / ϕ 1/\phi, or 1 1.

We refer the reader to [5] for further details and references. In this note, we use standard calculus to prove the following generalization of Boppana’s inequality:

###### Theorem 1.

Let k > 1 k>1 be real. Then α k ​ h ​ ( x k) ≥ x k − 1 ​ h ​ ( x) \alpha_{k}h(x^{k})\geq x^{k-1}h(x) for 0 ≤ x ≤ 1 0\leq x\leq 1, where 0 < α k < 1 0<\alpha_{k}<1 is the unique positive solution to x ​ ( 1 + x) k − 1 = 1 x(1+x)^{k-1}=1, and equality holds iff x = 0 x=0, 1 / ( 1 + α k) 1/(1+\alpha_{k}), or 1 1.

Notice that Boppana’s inequality is the case k = 2 k=2. Yuster [2] conjectured this inequality for integer k ≥ 2 k\geq 2, showing that it implied a generalization of Gilmer’s result to what he called “approximate k k -union closed set systems,” and proving it for k = 3 k=3 and k = 4 k=4. Consequently, the following is a corollary of our result:

###### Corollary 1 ( [2], Conjecture 1.5).

Let k ≥ 2 k\geq 2 be an integer and let 0 ≤ c ≤ 1 0\leq c\leq 1. A finite set system ℱ \mathcal{F} is c c -approximate k k -union closed if for at least a c c -fraction of the k k -tuples A 1, …, A k ∈ ℱ A_{1},\dots,A_{k}\in\mathcal{F}, we have ⋃ i = 1 k A i ∈ ℱ \bigcup_{i=1}^{k}A_{i}\in\mathcal{F}.

Let { ∅ } ≠ ℱ ⊆ 2 [n] \{\varnothing\}\neq\mathcal{F}\subseteq 2^{[n]} be a ( 1 − ϵ) (1-\epsilon) -approximate k k -union closed set system, where 0 ≤ ϵ < 1 / 2 0\leq\epsilon<1/2. Then there exists an element contained in an α k / ( 1 + α k) − δ \alpha_{k}/(1+\alpha_{k})-\delta fraction of sets in ℱ \mathcal{F}, where δ = ( k ​ ϵ + 2 ​ ϵ ​ log ⁡ ( 1 / ϵ) / log ⁡ | ℱ |) 1 / ( k − 1) \delta=(k\epsilon+2\epsilon\log(1/\epsilon)/\log|\mathcal{F}|)^{1/(k-1)}.

Later, Yuster and Yashfe [3] proved the inequality for integer 5 ≤ k ≤ 20 5\leq k\leq 20. Wakhare [1] investigated the generalization to real k > 1 k>1.

## 2. The proof

Fix real k > 1 k>1 and write α = α k \alpha=\alpha_{k}. Define q ⁡ ( x) ≔ x k − 1 ​ h ​ ( x) / h ⁡ ( x k) q(x)\coloneqq x^{k-1}h(x)/h(x^{k}) on ( 0, 1) (0,1), and extend q q to 0 0 and 1 1 by taking limits, so that q ⁡ ( 0) = q ⁡ ( 1) = 1 / k q(0)=q(1)=1/k ( Lemma 1). Our goal is to show that q ⁡ ( x) ≤ α q(x)\leq\alpha. Since α = 1 / ( 1 + α) k − 1 \alpha=1/(1+\alpha)^{k-1}, we have

 | q ⁡ ( 1 1 + α) = 1 ( 1 + α) k − 1 ⋅ h ⁡ ( 1 1 + α) h ⁡ ( 1 ( 1 + α) k) = α ⋅ h ⁡ ( 1 1 + α) h ⁡ ( α 1 + α) = α, q\Bigl({1\over 1+\alpha}\Bigr)={1\over(1+\alpha)^{k-1}}\cdot{h\bigl({1\over 1+\alpha}\bigr)\over h\bigl({1\over(1+\alpha)^{k}}\bigr)}=\alpha\cdot{h\bigl({1\over 1+\alpha}\bigr)\over h\bigl({\alpha\over 1+\alpha}\bigr)}=\alpha, |  |

where we used the fact that h ⁡ ( x) = h ⁡ ( 1 − x) h(x)=h(1-x) in the last step.

We will complete the proof by showing that q ′ ​ ( x) = 0 q^{\prime}(x)=0 if and only if x = 1 / ( 1 + α) x=1/(1+\alpha); since q q is differentiable on ( 0, 1) (0,1), continuous on [0, 1] [0,1], and q ⁡ ( 1 / ( 1 + α)) = α > 1 / k = q ⁡ ( 0) = q ⁡ ( 1) q(1/(1+\alpha))=\alpha>1/k=q(0)=q(1) ( Lemma 2), this will imply that q ⁡ ( x) ≤ α q(x)\leq\alpha as needed ( Lemma 3).

Suppose q ′ ​ ( x) = 0 q^{\prime}(x)=0. Since

(1) |  | q ′ ​ ( x) = ( k − 1) ​ x k − 2 ​ h ​ ( x) + x k − 1 ​ h ′ ​ ( x) h ⁡ ( x k) − x k − 1 ​ h ​ ( x) ​ h ′ ​ ( x k) ​ k ​ x k − 1 h ​ ( x k) 2, q^{\prime}(x)={(k-1)x^{k-2}h(x)+x^{k-1}h^{\prime}(x)\over h(x^{k})}-x^{k-1}h(x){h^{\prime}(x^{k})kx^{k-1}\over h(x^{k})^{2}}, |  |

the condition q ′ ​ ( x) = 0 q^{\prime}(x)=0 is equivalent (after multiplying by h ​ ( x k) 2 / x k − 2 h(x^{k})^{2}/x^{k-2}) to

(2) |  | ( ( k − 1) ​ h ​ ( x) + x ​ h ′ ​ ( x)) ​ h ​ ( x k) = k ​ x k ​ h ​ ( x) ​ h ′ ​ ( x k). \Bigl((k-1)h(x)+xh^{\prime}(x)\Bigr)h(x^{k})=kx^{k}h(x)h^{\prime}(x^{k}). |  |

Since h ′ ​ ( x) = log ⁡ ( 1 − x) − log ⁡ x h^{\prime}(x)=\log(1-x)-\log x, we have x ​ h ′ ​ ( x) − h ⁡ ( x) = log ⁡ ( 1 − x) xh^{\prime}(x)-h(x)=\log(1-x), so

(3) |  | x ​ h ′ ​ ( x) = h ⁡ ( x) + log ⁡ ( 1 − x) and x k ​ h ′ ​ ( x k) = h ⁡ ( x k) + log ⁡ ( 1 − x k). xh^{\prime}(x)=h(x)+\log(1-x)\quad\text{and}\quad x^{k}h^{\prime}(x^{k})=h(x^{k})+\log(1-x^{k}). |  |

Substituting into ( 2) then yields

(4) |  | ( k ​ h ​ ( x) + log ⁡ ( 1 − x)) ​ h ​ ( x k) = k ​ h ​ ( x) ​ ( h ⁡ ( x k) + log ⁡ ( 1 − x k)), \Bigl(kh(x)+\log(1-x)\Bigr)h(x^{k})=kh(x)\Bigl(h(x^{k})+\log(1-x^{k})\Bigr), |  |

or

(5) |  | log ⁡ ( 1 − x) ​ h ​ ( x k) = k ​ h ​ ( x) ​ log ⁡ ( 1 − x k). \log(1-x)h(x^{k})=kh(x)\log(1-x^{k}). |  |

Multiplying by log ⁡ x \log x and dividing by h ⁡ ( x) ​ h ​ ( x k) h(x)h(x^{k}) then gives

(6) |  | log ⁡ ( x) ​ log ⁡ ( 1 − x) h ⁡ ( x) = k ​ log ⁡ ( x) ​ log ⁡ ( 1 − x k) h ⁡ ( x k), {\log(x)\log(1-x)\over h(x)}={k\log(x)\log(1-x^{k})\over h(x^{k})}, |  |

and since log ⁡ ( x k) = k ​ log ⁡ x \log(x^{k})=k\log x, this equation becomes

(7) |  | U ⁡ ( x) = U ⁡ ( x k), U(x)=U(x^{k}), |  |

where

(8) |  | U ⁡ ( x) = log ⁡ ( x) ​ log ⁡ ( 1 − x) h ⁡ ( x). U(x)={\log(x)\log(1-x)\over h(x)}. |  |

Since U ⁡ ( x) = U ⁡ ( 1 − x) U(x)=U(1-x), and since U U is strictly decreasing on ( 0, 1 / 2] (0,1/2] ( Lemma 4), it follows that every value of U U is attained at exactly two points x x and 1 − x 1-x (except at x = 1 / 2 x=1/2, where they coincide). Thus U ⁡ ( x) = U ⁡ ( x k) U(x)=U(x^{k}) implies x k = x x^{k}=x or x k = 1 − x x^{k}=1-x. Since k > 1 k>1 and 0 < x < 1 0<x<1, it follows that x k = 1 − x x^{k}=1-x, which in turn implies that x = 1 / ( 1 + α) x=1/(1+\alpha) ( Lemma 5). This completes the proof.

## 3. Lemmas

###### Lemma 1.

We have lim x → 0 + q ⁡ ( x) = lim x → 1 − q ⁡ ( x) = 1 / k \lim_{x\to 0^{+}}q(x)=\lim_{x\to 1^{-}}q(x)=1/k.

###### Proof.

The x → 0 + x\to 0^{+} case follows from making the asymptotic estimate h ⁡ ( x) = − x ​ log ⁡ x ⁡ ( 1 + o ⁡ ( 1)) h(x)=-x\log x(1+o(1)), since then h ⁡ ( x k) = − x k ​ log ⁡ ( x k) ​ ( 1 + o ⁡ ( 1)) = − k ​ x k ​ log ⁡ x ⁡ ( 1 + o ⁡ ( 1)) h(x^{k})=-x^{k}\log(x^{k})(1+o(1))=-kx^{k}\log x(1+o(1)) and

(9) |  | q ⁡ ( x) = x k − 1 ​ h ​ ( x) h ⁡ ( x k) = x k − 1 ​ x ​ log ⁡ x ⁡ ( 1 + o ⁡ ( 1)) k ​ x k ​ log ⁡ x ⁡ ( 1 + o ⁡ ( 1)) → 1 k; q(x)={x^{k-1}h(x)\over h(x^{k})}={x^{k-1}x\log x(1+o(1))\over kx^{k}\log x(1+o(1))}\to{1\over k}; |  |

a similar approach works for x → 1 − x\to 1^{-} by using the symmetry h ⁡ ( 1 − x) = h ⁡ ( x) h(1-x)=h(x). ∎

###### Lemma 2.

We have α > 1 / k \alpha>1/k.

###### Proof.

Recall that α ​ ( 1 + α) k − 1 = 1 \alpha(1+\alpha)^{k-1}=1. Set f ⁡ ( x) = x ​ ( 1 + x) k − 1 f(x)=x(1+x)^{k-1}. Then f f is strictly increasing on ( 0, ∞) (0,\infty), as can be seen by considering f ′ f^{\prime}. Thus it suffices to check that f ⁡ ( 1 / k) = ( 1 / k) ​ ( 1 + 1 / k) k − 1 < 1 f(1/k)=(1/k)(1+1/k)^{k-1}<1, or ( k + 1) k − 1 < k k (k+1)^{k-1}<k^{k}. This follows from taking logarithms and doing calculus, or alternatively from the weighted AM-GM inequality with numbers x 1 = 1 x_{1}=1, x 2 = k + 1 x_{2}=k+1 and weights w 1 = 1 w_{1}=1, w 2 = k − 1 w_{2}=k-1. ∎

###### Lemma 3.

Given M > 0 M>0, 0 < a < 1 0<a<1, and a continuous function f: [0, 1] → 𝐑 f\colon[0,1]\to\mathbf{R} that is differentiable on ( 0, 1) (0,1), suppose that f ⁡ ( 0) < M f(0)<M, f ⁡ ( a) = M f(a)=M, f ⁡ ( 1) < M f(1)<M, and f ′ ​ ( x) = 0 f^{\prime}(x)=0 iff x = a x=a. Then f ⁡ ( x) ≤ M f(x)\leq M with equality iff x = a x=a.

###### Proof.

This follows from the extreme value theorem and Fermat’s theorem. ∎

###### Lemma 4.

Let U ⁡ ( x) = log ⁡ ( x) ​ log ⁡ ( 1 − x) / h ⁡ ( x) U(x)=\log(x)\log(1-x)/h(x). Then U U is decreasing on ( 0, 1 / 2] (0,1/2].

###### Proof.

It suffices to prove that 1 / U 1/U is increasing on ( 0, 1 / 2) (0,1/2). Since

(10) |  | 1 U ⁡ ( x) = − x log ⁡ ( 1 − x) + − ( 1 − x) log ⁡ x = L ⁡ ( 1, 1 − x) + L ⁡ ( 1, x) {1\over U(x)}={-x\over\log(1-x)}+{-(1-x)\over\log x}=L(1,1-x)+L(1,x) |  |

where L ⁡ ( a, b) ≔ ( a − b) / ( log ⁡ a − log ⁡ b) L(a,b)\coloneqq(a-b)/(\log a-\log b) is the *logarithmic mean*, the identity L ⁡ ( a, b) = ∫ 0 1 a 1 − s ​ b s ​ 𝑑 s L(a,b)=\int_{0}^{1}a^{1-s}b^{s}\,ds yields f ⁡ ( t) ≔ L ⁡ ( 1, t) = ∫ 0 1 t s ​ 𝑑 s f(t)\coloneqq L(1,t)=\int_{0}^{1}t^{s}\,ds. Then f ′′ ​ ( t) = ∫ 0 1 s ⁡ ( s − 1) ​ t s − 2 ​ 𝑑 s < 0 f^{\prime\prime}(t)=\int_{0}^{1}s(s-1)t^{s-2}\,ds<0 on ( 0, 1) (0,1), so f ⁡ ( t) f(t) is strictly concave. Thus f ′ ​ ( t) f^{\prime}(t) is strictly decreasing, and we conclude that ( 1 / U ⁡ ( x)) ′ = f ′ ​ ( x) − f ′ ​ ( 1 − x) > 0 (1/U(x))^{\prime}=f^{\prime}(x)-f^{\prime}(1-x)>0 for x ∈ ( 0, 1 / 2) x\in(0,1/2) as needed. ∎

###### Lemma 5.

Suppose x k = 1 − x x^{k}=1-x. Then x = 1 / ( 1 + α) x=1/(1+\alpha), where α \alpha is the unique positive solution to α ​ ( 1 + α) k − 1 = 1 \alpha(1+\alpha)^{k-1}=1.

###### Proof.

Substitute x = 1 / ( 1 + α) x=1/(1+\alpha) into x k = 1 − x x^{k}=1-x to get 1 / ( 1 + α) k = α / ( 1 + α) 1/(1+\alpha)^{k}=\alpha/(1+\alpha), then multiply both sides by ( 1 + α) k (1+\alpha)^{k}. ∎

## 4. Remarks

Though this paper was written and checked carefully by hand, key steps in some proofs were generated with the assistance of GPT-5.2 pro. The result has also been formalized in Lean 4 using Harmonic Aristotle and Gemini 3 Pro Preview; the code is available from [https://github.com/boonsuan/entropy-inequality][4].

## 5. Acknowledgements

The author thanks Hao Huang for helpful comments on a draft of this note.

## References

- [1] Tanay Wakhare, “Iterated entropy derivatives and binary entropy inequalities,” Journal of Approximation Theory 307 (2025), 106143.
- [2] Raphael Yuster, “Almost k k -union closed set systems,” [arXiv:2302.12276v1][5] [math.CO]
- [3] Raphael Yuster, “An entropy inequality and almost k k -union closed set systems,” Combinatorics seminar abstract (13 Nov 2024), Technion. Accessed January 26, 2026. [https://math.technion.ac.il/en/events/raphael-yuster/][6]
- [4] Justin Gilmer, “A constant lower bound for the union-closed sets conjecture,” [arXiv:2211.09055v2][7] [math.CO]
- [5] Stijn Cambie, “Progress on the union-closed conjecture and offsprings in winter 2022–2023,” [arXiv:2306.12351v1][8] [math.CO]
- [6] Ravi Boppana, “A Useful Inequality for the Binary Entropy Function,” [arXiv:2301.09664v1][9] [math.CO]


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:hbs@u.nus.edu
[4]: https://github.com/boonsuan/entropy-inequality
[5]: https://arxiv.org/pdf/2302.12276
[6]: https://math.technion.ac.il/en/events/raphael-yuster/
[7]: https://arxiv.org/pdf/2211.09055
[8]: https://arxiv.org/pdf/2306.12351
[9]: https://arxiv.org/pdf/2301.09664
