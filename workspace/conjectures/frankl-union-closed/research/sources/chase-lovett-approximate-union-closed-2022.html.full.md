<!-- source: https://arxiv.org/html/2211.11689v1 | converted from HTML -->

Approximate union closed conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2211.11689v1 [math.CO] 21 Nov 2022

# Approximate union closed conjecture

Zachary Chase Thanks: Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory Quarter, Woodstock Road, Oxford OX2 6GG, UK. Partially supported by Ben Green’s Simons Investigator Grant 376201 and gratefully acknowledges the support of the Simons Foundation. Email: zachary.chase@maths.ox.ac.uk. Shachar Lovett Thanks: Department of Computer Science and Engineering, University of California San Diego, CA 92093. Supported by NSF awards CCF-2006443 and DMS-1953928. Email: slovett@cs.ucsd.edu.

###### Abstract

A set system is called union closed if for any two sets in the set system their union is also in the set system. Gilmer recently proved that in any union closed set system some element belongs to at least a 0.01 0.01 fraction of sets, and conjectured that his technique can be pushed to the constant 3 − 5 2 \frac{3-\sqrt{5}}{2}. We verify his conjecture; show that it extends to approximate union closed set systems, where for nearly all pairs of sets their union belong to the set system; and show that for such set systems this bound is optimal.

## 1 Introduction

The union closed conjecture is a well-known conjecture in combinatorics.

###### Definition 1.1 (Union closed set system).

A set system ℱ \mathcal{F} is *union closed*if for all A, B ∈ ℱ A,B\in\mathcal{F} we have A ∪ B ∈ ℱ A\cup B\in\mathcal{F}.

Frankl introduced the conjecture that for any finite union closed set system ℱ \mathcal{F}, there is an element in at least 1 2 \frac{1}{2} of the sets of ℱ \mathcal{F}. Recently, Gilmer [2] established the first constant lower bound for this conjecture, obtaining 1 100 \frac{1}{100} in place of 1 2 \frac{1}{2}. Gilmer conjectured that his technique can be sharpened to give the constant ψ:= 3 − 5 2 ≈ 0.38 \psi:=\frac{3-\sqrt{5}}{2}\approx 0.38. Below we verify his conjecture, and also show that it is optimal for “approximate” union closed set systems.

###### Definition 1.2 (Approximate union closed set system).

Let 0 ≤ c ≤ 1 0\leq c\leq 1. A set system ℱ \mathcal{F} is c c -approximate union closed if for at least a c c -fraction of the pairs A, B ∈ ℱ A,B\in\mathcal{F} we have A ∪ B ∈ ℱ A\cup B\in\mathcal{F}.

Informally, we say that ℱ \mathcal{F} is approximate union closed if it is 1 − o ⁡ ( 1) 1-o(1) approximate union closed. The following theorem shows that in any approximate union closed set system, some element is in a ψ − o ⁡ ( 1) \psi-o(1) fraction of sets.

###### Theorem 1.3.

Let ℱ \mathcal{F} be a ( 1 − ε) (1-\varepsilon) -approximate union closed set system, where ε < 1 / 2 \varepsilon<1/2. Then there is an element which is contained in a ψ − δ \psi-\delta fraction of sets in ℱ \mathcal{F}, where δ = 2 ​ ε ​ ( 1 + log ⁡ ( 1 / ε) log ⁡ | ℱ |) \delta=2\varepsilon\left(1+\frac{\log(1/\varepsilon)}{\log|\mathcal{F}|}\right).

The threshold of ψ \psi is optimal for approximate union closed set systems, as the following example shows.

###### Example 1.4.

Let n n be large enough, and define the following set systems over [n] [n]:

 | ℱ 1 = { x ∈ { 0, 1 } n: | x | = ψ ​ n + n 2 / 3 }, ℱ 2 = { x ∈ { 0, 1 } n: | x | ≥ ( 1 − ψ) ​ n }, ℱ = ℱ 1 ∪ ℱ 2. \mathcal{F}_{1}=\{x\in\{0,1\}^{n}:|x|=\psi n+n^{2/3}\},\qquad\mathcal{F}_{2}=\{x\in\{0,1\}^{n}:|x|\geq(1-\psi)n\},\qquad\mathcal{F}=\mathcal{F}_{1}\cup\mathcal{F}_{2}. |  |

One can verify that: (i) ℱ \mathcal{F} is 1 − o ⁡ ( 1) 1-o(1) approximate union closed (using the fact that 1 − ψ = 2 ​ ψ − ψ 2 1-\psi=2\psi-\psi^{2}); (ii) that | ℱ 2 | = o ⁡ ( | ℱ 1 |) |\mathcal{F}_{2}|=o(|\mathcal{F}_{1}|); and (iii) that hence each element i ∈ [n] i\in[n] is in at most ψ + o ⁡ ( 1) \psi+o(1) fraction of sets in ℱ \mathcal{F}.

### Acknowledgements.

We thank Ryan Alweiss, Brice Huang, and Mark Sellke for sharing their writeup [1] with us.

## 2 Preliminaries

All logarithms are in base two. Let h ⁡ ( x) = − ( x ​ log ⁡ x + ( 1 − x) ​ log ⁡ ( 1 − x)) h(x)=-(x\log x+(1-x)\log(1-x)) be the binary entropy function. Let φ = 1 − ψ = 5 − 1 2 \varphi=1-\psi=\frac{\sqrt{5}-1}{2} be the positive root of x 2 + x − 1 = 0 x^{2}+x-1=0. We will rely on the following analytic claim which we verified using a computer simulation. It has been proven rigorously in [1].

###### Claim 2.1.

The minimum of h ⁡ ( x 2) x ​ h ​ ( x) \frac{h(x^{2})}{xh(x)} for x ∈ [0, 1] x\in[0,1] is obtained at x = φ x=\varphi.

## 3 Analytic claims

Let f: [0, 1] 2 → ℝ ≥ 0 f:[0,1]^{2}\to\mathbb{R}_{\geq 0} be defined as

 | f ⁡ ( x, y):= h ⁡ ( x ​ y) h ⁡ ( x) ​ y + h ⁡ ( y) ​ x f(x,y):=\frac{h(xy)}{h(x)y+h(y)x} |  |

for ( x, y) ∈ ( 0, 1) 2 (x,y)\in(0,1)^{2} and extended (continuously) to [0, 1] 2 [0,1]^{2} by setting f ⁡ ( x, y) = 1 f(x,y)=1 if x ∈ { 0, 1 } x\in\{0,1\} or y ∈ { 0, 1 } y\in\{0,1\}.

###### Claim 3.1.

The function f f is minimized at ( φ, φ) (\varphi,\varphi). At this point f ⁡ ( φ, φ) = 1 2 ​ φ f(\varphi,\varphi)=\frac{1}{2\varphi}.

###### Proof.

First, by routine calculations one can verify that f f is indeed continuous on [0, 1] 2 [0,1]^{2} and that f ⁡ ( x, y) < 1 f(x,y)<1 for ( x, y) ∈ ( 0, 1) 2 (x,y)\in(0,1)^{2}. Thus, the minimum of f f is attained in ( 0, 1) 2 (0,1)^{2}. Next, let g ⁡ ( x) = h ⁡ ( x) x g(x)=\frac{h(x)}{x}, which is defined on ( 0, 1) (0,1), and note that

 | f ⁡ ( x, y) = g ⁡ ( x ​ y) g ⁡ ( x) + g ⁡ ( y). f(x,y)=\frac{g(xy)}{g(x)+g(y)}. |  |

We first show that f f is minimized on the diagonal, namely at some point ( x, x) (x,x). Assume that f f is minimized at some point ( x ∗, y ∗) (x^{*},y^{*}), and let α = f ⁡ ( x ∗, y ∗) \alpha=f(x^{*},y^{*}). Define

 | F ⁡ ( x, y) = g ⁡ ( x ​ y) − α ⁡ ( g ⁡ ( x) + g ⁡ ( y)). F(x,y)=g(xy)-\alpha(g(x)+g(y)). |  |

Then F ⁡ ( x, y) ≥ 0 F(x,y)\geq 0 for all x, y ∈ ( 0, 1) 2 x,y\in(0,1)^{2} and F ⁡ ( x ∗, y ∗) = 0 F(x^{*},y^{*})=0. Thus the partial derivatives of F F must be zero at the minimum point:

 | ∂ F ∂ x ​ ( x ∗, y ∗) = ∂ F ∂ y ​ ( x ∗, y ∗) = 0. \frac{\partial F}{\partial x}(x^{*},y^{*})=\frac{\partial F}{\partial y}(x^{*},y^{*})=0. |  |

Evaluating the derivatives gives

 | ∂ F ∂ x ​ ( x, y) = g ′ ​ ( x ​ y) ⋅ y − α ​ g ′ ​ ( x), ∂ F ∂ y ​ ( x, y) = g ′ ​ ( x ​ y) ⋅ x − α ​ g ′ ​ ( y). \frac{\partial F}{\partial x}(x,y)=g^{\prime}(xy)\cdot y-\alpha g^{\prime}(x),\qquad\frac{\partial F}{\partial y}(x,y)=g^{\prime}(xy)\cdot x-\alpha g^{\prime}(y). |  |

Define G ⁡ ( x) = x ​ g ′ ​ ( x) G(x)=xg^{\prime}(x) and note that we obtained that G ⁡ ( x ∗) = G ⁡ ( y ∗) G(x^{*})=G(y^{*}). A direct calculation gives g ′ ​ ( x) = log ⁡ ( 1 − x) x 2 g^{\prime}(x)=\frac{\log(1-x)}{x^{2}}, which implies that G G is monotonically decreasing, and so we must have x ∗ = y ∗ x^{*}=y^{*}.

Finally, restricting to x = y x=y, we have

 | f ⁡ ( x, x) = h ⁡ ( x 2) 2 ​ x ​ h ​ ( x). f(x,x)=\frac{h(x^{2})}{2xh(x)}. |  |

2.1 gives that f ⁡ ( x, x) f(x,x) is minimized at x = φ x=\varphi. Since φ 2 = 1 − φ \varphi^{2}=1-\varphi we have h ⁡ ( φ 2) = h ⁡ ( φ) h(\varphi^{2})=h(\varphi) and hence

 | f ⁡ ( φ, φ) = 1 2 ​ φ. f(\varphi,\varphi)=\frac{1}{2\varphi}. |  |

∎

###### Corollary 3.2.

For x, y ∈ [0, 1] x,y\in[0,1] we have

 | h ⁡ ( x ​ y) ≥ 1 2 ​ φ ​ ( x ​ h ​ ( y) + y ​ h ​ ( x)). h(xy)\geq\frac{1}{2\varphi}\Big(xh(y)+yh(x)\Big). |  |

## 4 Proof of the main theorem

###### Claim 4.1.

Let A, B A,B be two independent random variables taking values in { 0, 1 } n \{0,1\}^{n}. Assume for all i ∈ [n] i\in[n] that Pr [A i = 0] ≥ p \Pr[A_{i}=0]\geq p and Pr [B i = 0] ≥ p \Pr[B_{i}=0]\geq p. Then

 | H ⁡ ( A ∪ B) ≥ p 2 ​ φ ​ ( H ⁡ ( A) + H ⁡ ( B)). H(A\cup B)\geq\frac{p}{2\varphi}\Big(H(A)+H(B)\Big). |  |

###### Proof.

The chain rule and data processing inequality yield

 | H ⁡ ( A ∪ B) = ∑ i ∈ [n] H ⁡ ( A i ∪ B i | ( A ∪ B) < i) ≥ ∑ i ∈ [n] H ⁡ ( A i ∪ B i | A < i, B < i). H(A\cup B)=\sum_{i\in[n]}H(A_{i}\cup B_{i}|(A\cup B)_{<i})\geq\sum_{i\in[n]}H(A_{i}\cup B_{i}|A_{<i},B_{<i}). |  |

Let p ⁡ ( x) = Pr ⁡ [A i = 0 | A < i = x] p(x)=\Pr[A_{i}=0|A_{<i}=x] and q ⁡ ( y) = Pr ⁡ [B i = 0 | B < i = y] q(y)=\Pr[B_{i}=0|B_{<i}=y]. Then by Corollary 3.2

 | H ⁡ ( A i ∪ B i | A < i = x, B < i = y) = h ⁡ ( p ⁡ ( x) ​ q ​ ( y)) ≥ 1 2 ​ φ ​ ( p ⁡ ( x) ​ h ​ ( q ⁡ ( y)) + q ⁡ ( y) ​ h ​ ( p ⁡ ( x))). H\Big(A_{i}\cup B_{i}|A_{<i}=x,B_{<i}=y\Big)=h\Big(p(x)q(y)\Big)\geq\frac{1}{2\varphi}\Big(p(x)h(q(y))+q(y)h(p(x))\Big). |  |

Averaging over A < i, B < i A_{<i},B_{<i} which are independent gives

 | H ⁡ ( A i ∪ B i | A < i, B < i) \displaystyle H(A_{i}\cup B_{i}|A_{<i},B_{<i}) | ≥ 1 2 ​ φ ​ ( 𝔼 A < i ​ [p ⁡ ( A < i)] ⋅ 𝔼 B < i ​ [h ⁡ ( q ⁡ ( B < i))] + 𝔼 B < i ​ [q ⁡ ( B < i)] ⋅ 𝔼 A < i ​ [h ⁡ ( p ⁡ ( A < i))]) \displaystyle\geq\frac{1}{2\varphi}\Big(\mathbb{E}_{A_{<i}}[p(A_{<i})]\cdot\mathbb{E}_{B_{<i}}[h(q(B_{<i}))]+\mathbb{E}_{B_{<i}}[q(B_{<i})]\cdot\mathbb{E}_{A_{<i}}[h(p(A_{<i}))]\Big) |  |

 |  | = 1 2 ​ φ ( Pr [A i = 0] ⋅ H ( B i | B < i) + Pr [B i = 0] ⋅ H ( A i | A < i)). \displaystyle=\frac{1}{2\varphi}\Big(\Pr[A_{i}=0]\cdot H(B_{i}|B_{<i})+\Pr[B_{i}=0]\cdot H(A_{i}|A_{<i})\Big). |  |

Using the assumption that Pr [A i = 0] ≥ p \Pr[A_{i}=0]\geq p and Pr [B i = 0] ≥ p \Pr[B_{i}=0]\geq p gives

 | H ⁡ ( A i ∪ B i) ≥ p 2 ​ φ ​ ( H ⁡ ( A i | A < i) + H ⁡ ( B i | B < i)). H(A_{i}\cup B_{i})\geq\frac{p}{2\varphi}\Big(H(A_{i}|A_{<i})+H(B_{i}|B_{<i})\Big). |  |

The claim follows by summing over i ∈ [n] i\in[n]. ∎

###### Proof of Theorem 1.3.

Let ℱ \mathcal{F} be a ( 1 − ε) (1-\varepsilon) -approximate union closed family over [n] [n]. Let p = min i ∈ [n] Pr A ∈ ℱ [A i = 0] p=\min_{i\in[n]}\Pr_{A\in\mathcal{F}}[A_{i}=0], where our goal is to lower bound 1 − p 1-p. Let A, B ∈ ℱ A,B\in\mathcal{F} be uniformly and independently chosen. 4.1 then gives

 | H ⁡ ( A ∪ B) ≥ p 2 ​ φ ​ ( H ⁡ ( A) + H ⁡ ( B)) = p φ ​ log ⁡ | ℱ |. H(A\cup B)\geq\frac{p}{2\varphi}\Big(H(A)+H(B)\Big)=\frac{p}{\varphi}\log|\mathcal{F}|. |  |

Next we show that H ⁡ ( A ∪ B) H(A\cup B) cannot be much larger than log ⁡ | ℱ | \log|\mathcal{F}|. Let I I be the indicator for the event A ∪ B ∈ ℱ A\cup B\in\mathcal{F}, where by assumption Pr [I = 1] ≥ 1 − ε \Pr[I=1]\geq 1-\varepsilon. Then

 | H ( A ∪ B) ≤ H ( A ∪ B, I) = H ( I) + H ( A ∪ B | I = 0) Pr [I = 0] + H ( A ∪ B | I = 1) Pr [I = 1]. H(A\cup B)\leq H(A\cup B,I)=H(I)+H(A\cup B|I=0)\Pr[I=0]+H(A\cup B|I=1)\Pr[I=1]. |  |

We bound the terms one by one. First, since I I is binary and Pr [I = 0] ≤ ε < 1 / 2 \Pr[I=0]\leq\varepsilon<1/2 we have H ⁡ ( I) ≤ h ⁡ ( ε) ≤ 2 ​ ε ​ log ⁡ ( 1 / ε) H(I)\leq h(\varepsilon)\leq 2\varepsilon\log(1/\varepsilon). Next, when I = 0 I=0, we use the naive bound H ⁡ ( A ∪ B | I = 0) ≤ H ⁡ ( A, B | I = 0) ≤ 2 ​ log ⁡ | ℱ | H(A\cup B|I=0)\leq H(A,B|I=0)\leq 2\log|\mathcal{F}|. Finally, when I = 1 I=1 we have that A ∪ B | I = 1 A\cup B|I=1 is a distribution supported on ℱ \mathcal{F} and so H ⁡ ( A ∪ B | I = 1) ≤ log ⁡ | ℱ | H(A\cup B|I=1)\leq\log|\mathcal{F}|. Putting these together gives

 | p φ ​ log ⁡ | ℱ | ≤ H ⁡ ( A ∪ B) ≤ 2 ​ ε ​ log ⁡ ( 1 / ε) + ( 1 + 2 ​ ε) ​ log ⁡ | ℱ |. \frac{p}{\varphi}\log|\mathcal{F}|\leq H(A\cup B)\leq 2\varepsilon\log(1/\varepsilon)+(1+2\varepsilon)\log|\mathcal{F}|. |  |

We thus obtain

 | 1 − p ≥ 1 − φ − 2 ​ ε ​ ( 1 + log ⁡ ( 1 / ε) log ⁡ | ℱ |). 1-p\geq 1-\varphi-2\varepsilon\left(1+\frac{\log(1/\varepsilon)}{\log|\mathcal{F}|}\right). |  |

The proof follows, as 1 − φ = 3 − 5 2 = ψ 1-\varphi=\frac{3-\sqrt{5}}{2}=\psi. ∎

## References

- [1] R. Alweiss, B. Huang, M. Sellke. In preparation.
- [2] J. Gilmer. A constant lower bound for the union-closed sets conjecture. ArXiv e-prints arXiv:2211.09055, November 2022.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
