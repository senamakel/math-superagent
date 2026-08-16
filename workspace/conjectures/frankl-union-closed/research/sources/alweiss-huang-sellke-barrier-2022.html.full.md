<!-- source: https://arxiv.org/html/2211.11731v2 | converted from HTML -->

Improved Lower Bound for Frankl’s Union-Closed Sets Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2211.11731v2 [math.CO] 30 Nov 2022

# Improved Lower Bound for Frankl’s Union-Closed Sets Conjecture

Ryan Alweiss Thanks: Department of Mathematics, Princeton University. Brice Huang Thanks: Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology. Mark Sellke Thanks: School of Mathematics, Institute for Advanced Study and Amazon Core AI.

###### Abstract

We verify an explicit inequality conjectured in [6], thus proving that for any nonempty union-closed family ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, some i ∈ [n] i\in[n] is contained in at least 3 − 5 2 ≈ 0.38 \frac{3-\sqrt{5}}{2}\approx 0.38 fraction of the sets in ℱ {\mathcal{F}}. One case, an explicit one-variable inequality, is checked by computer calculation.

## 1 Introduction

Let ℳ ϕ {\cal M}_{\phi} be the set of probability measures μ ∈ 𝒫 ⁡ ( [0, 1]) \mu\in{\mathcal{P}}([0,1]) with expectation ϕ \phi. Define

 | F ⁡ ( μ) = 𝔼 ( x, y) ∼ μ × μ H ​ ( xy) − 𝔼 x ∼ μ H ​ ( x) F(\mu)=\EE_{(x,y)\sim\mu\times\mu}H(xy)-\EE_{x\sim\mu}H(x) |  | (1) |

where H ⁡ ( x) = − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) H(x)=-x\log x-(1-x)\log(1-x) is the entropy function and log \log denotes natural logarithm. Note that F F is continuous in the weak topology and ℳ ϕ {\cal M}_{\phi} is compact, so F F has a minimizer over ℳ ϕ {\cal M}_{\phi}. In this note, we will show the following results.

###### Theorem 1.

For all ϕ ∈ [0, 1] \phi\in[0,1], the minimum of F ⁡ ( μ) F(\mu) over ℳ ϕ {\cal M}_{\phi} is attained at some μ \mu supported on at most two points. Furthermore, if a minimizer is supported on exactly two points, then one of the points is 0 0.

The case of μ \mu supported on { 0, x } \{0,x\} leads to the following definition:

 | S = { ϕ ∈ [0, 1]: ϕ ​ H ​ ( x 2) ≥ x ​ H ​ ( x) ​ ∀ x ∈ [ϕ, 1] }, ϕ ∗ = min ⁡ ( S). S=\left\{\phi\in[0,1]:\phi H(x^{2})\geq xH(x)~\forall x\in[\phi,1]\right\},\quad\phi^{\ast}=\min(S). |  |

Note that the condition defining S S is monotone in ϕ \phi and S S is clearly closed, so min ⁡ ( S) \min(S) is well defined. As in the recent breakthrough [6] by Gilmer, a bound on Frankl’s union-closed conjecture follows from the above.

###### Theorem 2.

The union-closed conjecture holds with constant 1 − ϕ ∗ 1-\phi^{\ast}, i.e. for any non-empty union-closed family ℱ ⊆ 2 [n] {\mathcal{F}}\subseteq 2^{[n]}, some i ∈ [n] i\in[n] is contained in at least 1 − ϕ ∗ 1-\phi^{\ast} fraction of the sets in ℱ {\mathcal{F}}.

Throughout this paper we set φ = 5 − 1 2 \varphi=\frac{\sqrt{5}-1}{2}. In the Appendix, we give a numerical verification of the following claim. We require certain computer calculations (detailed in an attached Python file) to be accurate to within margin of error 10 − 3 10^{-3}, which can be made completely rigorous using interval arithmetic.

###### Claim 3.

If x ∈ [φ, 1] x\in[\varphi,1], then φ ​ H ​ ( x 2) ≥ x ​ H ​ ( x) \varphi H(x^{2})\geq xH(x), with equality if and only if x ∈ { φ, 1 } x\in\{\varphi,1\}.

Assuming Claim 3, the following claim identifies the value of ϕ ∗ \phi^{\ast}. Then, Theorem 2 implies that the union-closed conjecture holds with constant 1 − φ = 3 − 5 2 1-\varphi=\frac{3-\sqrt{5}}{2}. This is a natural barrier for the method of [6] as explained therein.

###### Claim 4.

We have that ϕ ∗ = φ \phi^{\ast}=\varphi.

#### Related Work.

The union-closed conjecture has been the subject of much study, see [1, 8, 11, 2, 7] or the survey [3]. The recent breakthrough [6] by Gilmer showed that this conjecture holds with constant 0.01 0.01.

Concurrently with and independently of this work, Chase and Lovett [4], Sawin [10], and Peabody [9] also proved the union-closed conjecture with constant 3 − 5 2 \frac{3-\sqrt{5}}{2}, and [10] outlined an argument to improve this bound by an additional small constant. Moreover, [10] and Ellis [5] found counterexamples to [6, Conjecture 1], which would have implied the full union-closed conjecture with constant 1 2 \frac{1}{2}.

#### Acknowledgements.

We thank Zachary Chase and Shachar Lovett for sharing their writeup [4] with us. We thank Mehtaab Sawhney for helpful comments on a previous draft. RA was supported by an NSF Graduate Research Fellowship. BH was supported by an NSF Graduate Research Fellowship, a Siebel scholarship, NSF awards CCF-1940205 and DMS-1940092, and NSF-Simons collaboration grant DMS-2031883.

## 2 Reduction to Two Point Masses

###### Lemma 5.

F F is concave on ℳ ϕ {\cal M}_{\phi} for any ϕ ∈ [0, 1] \phi\in[0,1], i.e.

 | p ​ F ​ ( μ 1) + ( 1 − p) ​ F ​ ( μ 2) ≤ F ⁡ ( p ​ μ 1 + ( 1 − p) ​ μ 2) ∀ μ 1, μ 2 ∈ ℳ ϕ, p ∈ [0, 1]. pF(\mu_{1})+(1-p)F(\mu_{2})\leq F(p\mu_{1}+(1-p)\mu_{2})\quad\forall~\mu_{1},\mu_{2}\in{\cal M}_{\phi},~p\in[0,1]\,. |  | (2) |

###### Proof.

Let γ ⁡ ( x) = μ ⁡ ( [0, x]) \gamma(x)=\mu([0,x]) be the cumulative distribution function of μ \mu. Thus γ ⁡ ( 1) = 1 \gamma(1)=1 and

 | ϕ = ∫ 0 1 x ​ μ ​ ( 𝑑 x) = 1 − ∫ 0 1 γ ⁡ ( x) ​ 𝑑 x, \phi=\int_{0}^{1}x\mu({\rm d}x)=1-\int_{0}^{1}\gamma(x)~{\rm d}x\,, |  |

so

 | ∫ 0 1 γ ⁡ ( x) ​ 𝑑 x = 1 − ϕ. \int_{0}^{1}\gamma(x)~{\rm d}x=1-\phi\,. |  | (3) |

Using integration by parts,

 | ∫ 0 1 H ⁡ ( x) ​ μ ​ ( 𝑑 x) = H ⁡ ( x) ​ γ ​ ( x) | 0 1 − ∫ 0 1 H ′ ​ ( x) ​ γ ​ ( x) ​ 𝑑 x = ∫ 0 1 ( log ⁡ x 1 − x) ​ γ ​ ( x) ​ 𝑑 x. \int_{0}^{1}H(x)\mu({\rm d}x)=H(x)\gamma(x)\bigg|_{0}^{1}-\int_{0}^{1}H^{\prime}(x)\gamma(x)~{\rm d}x=\int_{0}^{1}\left(\log\frac{x}{1-x}\right)\gamma(x)~{\rm d}x\,. |  |

Similarly,

 | ∫ 0 1 H ⁡ ( x ​ y) ​ μ ​ ( 𝑑 y) \displaystyle\int_{0}^{1}H(xy)\mu({\rm d}y) | = H ⁡ ( x ​ y) ​ γ ​ ( y) | 0 1 − ∫ 0 1 x ​ H ′ ​ ( x ​ y) ​ γ ​ ( y) ​ 𝑑 y \displaystyle=H(xy)\gamma(y)\bigg|_{0}^{1}-\int_{0}^{1}xH^{\prime}(xy)\gamma(y)~{\rm d}y |  |

 |  | = H ⁡ ( x) + ∫ 0 1 ( x ​ log ⁡ x ​ y 1 − x ​ y) ​ γ ​ ( y) ​ 𝑑 y; \displaystyle=H(x)+\int_{0}^{1}\left(x\log\frac{xy}{1-xy}\right)\gamma(y)~{\rm d}y\,; |  |

 | ∫ 0 1 ( x ​ log ⁡ x ​ y 1 − x ​ y) ​ μ ​ ( 𝑑 x) \displaystyle\int_{0}^{1}\left(x\log\frac{xy}{1-xy}\right)\mu({\rm d}x) | = ( x ​ log ⁡ x ​ y 1 − x ​ y) ​ γ ​ ( x) | 0 1 − ∫ 0 1 d d ​ x ​ ( x ​ log ⁡ x ​ y 1 − x ​ y) ​ γ ​ ( x) ​ 𝑑 x, \displaystyle=\left(x\log\frac{xy}{1-xy}\right)\gamma(x)\bigg|_{0}^{1}-\int_{0}^{1}\frac{{\rm d}}{{\rm d}x}\left(x\log\frac{xy}{1-xy}\right)\gamma(x)~{\rm d}x\,, |  |

 |  | = log ⁡ y 1 − y − ∫ 0 1 ( 1 1 − x ​ y + log ⁡ x ​ y 1 − x ​ y) ​ γ ​ ( x) ​ 𝑑 x; \displaystyle=\log\frac{y}{1-y}-\int_{0}^{1}\left(\frac{1}{1-xy}+\log\frac{xy}{1-xy}\right)\gamma(x)~{\rm d}x\,; |  |

 | ∬ [0, 1] 2 H ⁡ ( x ​ y) ​ μ ​ ( 𝑑 x) ​ μ ​ ( 𝑑 y) \displaystyle\iint_{[0,1]^{2}}H(xy)\mu({\rm d}x)\mu({\rm d}y) | = ∫ 0 1 H ⁡ ( x) ​ μ ​ ( 𝑑 x) + ∫ 0 1 γ ⁡ ( y) ​ ∫ 0 1 x ​ log ⁡ x ​ y 1 − x ​ y ​ μ ​ ( 𝑑 x) ​ 𝑑 y, \displaystyle=\int_{0}^{1}H(x)\mu({\rm d}x)+\int_{0}^{1}\gamma(y)\int_{0}^{1}x\log\frac{xy}{1-xy}\mu({\rm d}x)~{\rm d}y\,, |  |

 |  | = 2 ​ ∫ 0 1 ( log ⁡ x 1 − x) ​ γ ​ ( x) ​ 𝑑 x − ∬ [0, 1] 2 ( 1 1 − x ​ y + log ⁡ x ​ y 1 − x ​ y) ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y. \displaystyle=2\int_{0}^{1}\left(\log\frac{x}{1-x}\right)\gamma(x)~{\rm d}x-\iint_{[0,1]^{2}}\left(\frac{1}{1-xy}+\log\frac{xy}{1-xy}\right)\gamma(x)\gamma(y)~{\rm d}x~{\rm d}y\,. |  |

So, letting F ⁡ ( γ) = F ⁡ ( μ) F(\gamma)=F(\mu) by slight abuse of notation, we have

 | F ⁡ ( γ) = ∫ 0 1 ( log ⁡ x 1 − x) ​ γ ​ ( x) ​ 𝑑 x − ∬ [0, 1] 2 ( log ⁡ x + log ⁡ y + 1 1 − x ​ y + log ⁡ 1 1 − x ​ y) ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y. F(\gamma)=\int_{0}^{1}\left(\log\frac{x}{1-x}\right)\gamma(x)~{\rm d}x-\iint_{[0,1]^{2}}\left(\log x+\log y+\frac{1}{1-xy}+\log\frac{1}{1-xy}\right)\gamma(x)\gamma(y)~{\rm d}x~{\rm d}y\,. |  |

We will show this is concave in γ \gamma. The first integral is manifestly linear in γ \gamma, and the contributions of log ⁡ x \log x and log ⁡ y \log y are linear because, in light of ( 3),

 | ∬ [0, 1] 2 ( log ⁡ x) ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y = ( 1 − ϕ) ​ ∫ 0 1 ( log ⁡ x) ​ γ ​ ( x) ​ 𝑑 x. \iint_{[0,1]^{2}}(\log x)\gamma(x)\gamma(y)~{\rm d}x~{\rm d}y=(1-\phi)\int_{0}^{1}(\log x)\gamma(x)~{\rm d}x\,. |  |

After removing these terms, we are reduced to showing convexity of

 | ∬ [0, 1] 2 ( 1 1 − x ​ y + log ⁡ 1 1 − x ​ y) ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y. \iint_{[0,1]^{2}}\left(\frac{1}{1-xy}+\log\frac{1}{1-xy}\right)\gamma(x)\gamma(y){\rm d}x{\rm d}y\,. |  |

Note that both 1 1 − x ​ y \frac{1}{1-xy} and log ⁡ 1 1 − x ​ y \log\frac{1}{1-xy} are of the form ∑ k ≥ 0 a k ​ x k ​ y k \sum_{k\geq 0}a_{k}x^{k}y^{k} for constants a k ≥ 0 a_{k}\geq 0. Hence it suffices to prove convexity of

 | ∬ [0, 1] 2 x k ​ y k ​ γ ​ ( x) ​ γ ​ ( y) ​ 𝑑 x ​ 𝑑 y = ( ∫ 0 1 x k ​ γ ​ ( x) ​ 𝑑 x) 2 \iint_{[0,1]^{2}}x^{k}y^{k}\gamma(x)\gamma(y){\rm d}x{\rm d}y=\left(\int_{0}^{1}x^{k}\gamma(x){\rm d}x\right)^{2} |  |

for any k ≥ 0 k\geq 0. This is the square of a linear function of γ \gamma, and hence is convex. (Note that all integrands are in L 1 L^{1} and so there are no convergence issues.) ∎

###### Lemma 6.

arg ⁡ min μ ∈ ℳ ϕ ​ F ​ ( μ) \arg\min_{\mu\in{\cal M}_{\phi}}F(\mu) contains some μ \mu supported on at most two points.

###### Proof.

This follows immediately from Lemma 5 and the Krein-Milman theorem since ℳ ϕ {\cal M}_{\phi} is compact in the weak topology and convex, and all extreme measures in ℳ ϕ {\cal M}_{\phi} are supported on 1 1 or 2 2 points.

We also include a more explicit and elementary version of this argument which proceeds as follows. First let μ ∈ ℳ ϕ \mu\in{\cal M}_{\phi} be any minimizer of F F and note that μ \mu can be approximated arbitrarily well in the weak topology by μ ^ \hat{\mu} with finite support. In particular for any ε > 0 \varepsilon>0, there exists μ ^ ∈ ℳ ϕ \hat{\mu}\in{\cal M}_{\phi} with F ⁡ ( μ ^) ≥ F ⁡ ( μ) − ε F(\hat{\mu})\geq F(\mu)-\varepsilon of the form

 | μ ^ ​ ( a i) = b i − b i − 1, 1 ≤ i ≤ k \hat{\mu}(a_{i})=b_{i}-b_{i-1},\quad 1\leq i\leq k |  |

for constants 0 ≤ a 1 < ⋯ < a k ≤ 1 0\leq a_{1}<\cdots<a_{k}\leq 1 and 0 = b 0 < b 1 < ⋯ < b k = 1 0=b_{0}<b_{1}<\cdots<b_{k}=1. We claim that for any ε > 0 \varepsilon>0, the minimal k k such that such a μ ^ \hat{\mu} exists is at most two. Indeed given such a μ ^ \hat{\mu} with k ≥ 3 k\geq 3, we may consider μ ^ η \hat{\mu}_{\eta} defined by

 | μ ^ η ​ ( a 1) \displaystyle\hat{\mu}_{\eta}(a_{1}) | = b 1 − b 0 + η ⁡ ( a 3 − a 2), \displaystyle=b_{1}-b_{0}+\eta(a_{3}-a_{2}), |  |

 | μ ^ η ​ ( a 2) \displaystyle\hat{\mu}_{\eta}(a_{2}) | = b 2 − b 1 − η ⁡ ( a 3 − a 1), \displaystyle=b_{2}-b_{1}-\eta(a_{3}-a_{1}), |  |

 | μ ^ η ​ ( a 3) \displaystyle\hat{\mu}_{\eta}(a_{3}) | = b 3 − b 2 + η ⁡ ( a 2 − a 1). \displaystyle=b_{3}-b_{2}+\eta(a_{2}-a_{1}). |  |

Then μ ^ η ∈ ℳ ϕ \hat{\mu}_{\eta}\in{\cal M}_{\phi} if and only if − c 1 ≤ η ≤ c 2 -c_{1}\leq\eta\leq c_{2} for some c 1, c 2 > 0 c_{1},c_{2}>0 and moreover the map η ↦ F ⁡ ( μ ^ η) \eta\mapsto F(\hat{\mu}_{\eta}) is concave by Lemma 5. It is easy to see that both μ ^ − c 1, μ ^ c 2 \hat{\mu}_{-c_{1}},\hat{\mu}_{c_{2}} have support size at most k − 1 k-1, and at least one of F ⁡ ( μ ^ − c 1), F ⁡ ( μ ^ c 2) F(\hat{\mu}_{-c_{1}}),F(\hat{\mu}_{c_{2}}) is at most F ⁡ ( μ ^) F(\hat{\mu}) by concavity. Iterating this argument, we find a μ ~ ∈ ℳ ϕ \tilde{\mu}\in{\cal M}_{\phi} with support size at most 2 2 and with F ⁡ ( μ ~) ≥ F ⁡ ( μ ^) ≥ F ⁡ ( μ) − ε F(\tilde{\mu})\geq F(\hat{\mu})\geq F(\mu)-\varepsilon. Taking a subsequential weak limit of the resulting μ ~ \tilde{\mu} as ε → 0 \varepsilon\to 0 completes the proof. ∎

## 3 Optimization over Two Point Masses

###### Lemma 7.

If μ \mu is supported on exactly two points, neither of which is 0 0, then μ \mu is not a minimizer of F F over ℳ ϕ {\cal M}_{\phi}.

###### Proof.

Suppose μ = p ​ δ x + ( 1 − p) ​ δ y \mu=p\delta_{x}+(1-p)\delta_{y} is a minimizer for F F over ℳ ϕ {\cal M}_{\phi} for 0 < y < x < 1 0<y<x<1 distinct and 0 < p < 1 0<p<1. Then any z ∈ [0, 1] z\in[0,1] can be written as z = q ​ x + ( 1 − q) ​ y z=qx+(1-q)y for some q ∈ ℝ q\in{\mathbb{R}} (which may be negative). We have

 | μ + t ​ δ z − t ​ q ​ δ x − t ⁡ ( 1 − q) ​ δ y ∈ ℳ ϕ \mu+t\delta_{z}-tq\delta_{x}-t(1-q)\delta_{y}\in{\cal M}_{\phi} |  |

for sufficiently small t ≥ 0 t\geq 0 and so

 | lim t → 0 + F ⁡ ( μ + t ​ δ z − t ​ q ​ δ x − t ⁡ ( 1 − q) ​ δ y) − F ⁡ ( μ) t ≥ 0. \lim_{t\to 0^{+}}\frac{F\big(\mu+t\delta_{z}-tq\delta_{x}-t(1-q)\delta_{y}\big)-F(\mu)}{t}\geq 0. |  |

It is not difficult to see from the definition ( 1) of F F that the left-hand limit equals

 | f ⁡ ( z) − q ​ f ​ ( x) − ( 1 − q) ​ f ​ ( y) ≥ 0, f(z)-qf(x)-(1-q)f(y)\geq 0\,, |  | (4) |

for

 | f ⁡ ( w):= 2 ​ [p ​ H ​ ( x ​ w) + ( 1 − p) ​ H ​ ( y ​ w)] − H ⁡ ( w). f(w):=2[pH(xw)+(1-p)H(yw)]-H(w). |  |

Equation ( 4) implies that f f lies above the line passing through ( x, f ⁡ ( x)) (x,f(x)) and ( y, f ⁡ ( y)) (y,f(y)). Since f f is a smooth function and x, y x,y are in the interior of [0, 1] [0,1], we deduce that

1. (a)

f ′ ​ ( x) = f ′ ​ ( y) = f ⁡ ( x) − f ⁡ ( y) x − y f^{\prime}(x)=f^{\prime}(y)=\frac{f(x)-f(y)}{x-y}, and

2. (b)

f ′′ ​ ( x), f ′′ ​ ( y) ≥ 0 f^{\prime\prime}(x),f^{\prime\prime}(y)\geq 0.

Moreover, (a) implies

1. (c)

f ′′ ​ ( z) ≤ 0 f^{\prime\prime}(z)\leq 0 for some z ∈ [y, x] z\in[y,x].

However we compute using H ′ ​ ( w) = log ⁡ 1 − w w H^{\prime}(w)=\log\frac{1-w}{w} that:

 | f ′ ​ ( z) \displaystyle f^{\prime}(z) | = 2 ​ [p ​ x ​ log ⁡ 1 − x ​ z x ​ z + ( 1 − p) ​ y ​ log ⁡ 1 − y ​ z y ​ z] − log ⁡ 1 − z z, \displaystyle=2\left[px\log\frac{1-xz}{xz}+(1-p)y\log\frac{1-yz}{yz}\right]-\log\frac{1-z}{z}\,, |  |

 | f ′′ ​ ( z) \displaystyle f^{\prime\prime}(z) | = − 2 ​ [p ​ x z ⁡ ( 1 − x ​ z) + ( 1 − p) ​ y z ⁡ ( 1 − y ​ z)] + 1 z ⁡ ( 1 − z). \displaystyle=-2\left[\frac{px}{z(1-xz)}+\frac{(1-p)y}{z(1-yz)}\right]+\frac{1}{z(1-z)}\,. |  |

Note that g ⁡ ( z):= z ⁡ ( 1 − z) ​ ( 1 − x ​ z) ​ ( 1 − y ​ z) ​ f ′′ ​ ( z) g(z):=z(1-z)(1-xz)(1-yz)f^{\prime\prime}(z) has the same sign as f ′′ ​ ( z) f^{\prime\prime}(z) and is a quadratic function in z z with leading coefficient

 | − 2 ​ p ​ x ​ y − 2 ​ ( 1 − p) ​ x ​ y + x ​ y = − x ​ y ≤ 0. -2pxy-2(1-p)xy+xy=-xy\leq 0\,. |  |

Hence the inequalities g ⁡ ( x), g ⁡ ( y) ≥ 0 g(x),g(y)\geq 0 and g ⁡ ( z) ≤ 0 g(z)\leq 0 can hold only if g g and hence f ′′ f^{\prime\prime} vanishes on the entire interval [x, y] [x,y]. However f ′′ ​ ( z) f^{\prime\prime}(z) is a rational function with a pole at z = 1 / y z=1/y so this is impossible.

The case x = 1 x=1, y > 0 y>0 is very similar. While we have f ′′ ​ ( y) ≥ 0 f^{\prime\prime}(y)\geq 0 as above, since 1 1 is not in the interior of [0, 1] [0,1] we cannot immediately deduce that f ′′ ​ ( 1) ≥ 0 f^{\prime\prime}(1)\geq 0. However in this case g ⁡ ( z) g(z) is a multiple of 1 − z 1-z and so g ⁡ ( 1) = 0 ≥ 0 g(1)=0\geq 0. Then the same argument applies: g ⁡ ( z) g(z) is a quadratic polynomial with negative leading coefficient − y < 0 -y<0. Because g g takes non-negative values at y y and 1 1, it takes positive values in between. However since f f is continuous on [0, 1] [0,1] and smooth on ( 0, 1) (0,1) and stays above the line segment through ( y, f ⁡ ( y)) (y,f(y)) and ( 1, f ⁡ ( 1)) (1,f(1)) it must have non-positive second derivative at some z ∈ ( y, 1) z\in(y,1). Since g g and f ′′ f^{\prime\prime} have the same sign on ( 0, 1) (0,1), this is a contradiction. (Note that f ′′ ​ ( 1) f^{\prime\prime}(1) does not actually exist if x = 1 x=1 and is not used in this argument.) ∎

## 4 Conclusion

###### Proof of Theorem 1.

Follows from Lemmas 6 and 7. ∎

###### Lemma 8.

We have that ϕ ∗ ≥ φ \phi^{\ast}\geq\varphi.

###### Proof.

Note that H ⁡ ( φ 2) = H ⁡ ( φ) H(\varphi^{2})=H(\varphi). If ϕ < φ \phi<\varphi, then ϕ ​ H ​ ( φ 2) < φ ​ H ​ ( φ) \phi H(\varphi^{2})<\varphi H(\varphi), and so ϕ ∉ S \phi\not\in S. ∎

###### Corollary 9.

If ϕ ≥ ϕ ∗ \phi\geq\phi^{\ast}, then F ⁡ ( μ) ≥ 0 F(\mu)\geq 0 for all μ ∈ ℳ ϕ \mu\in{\cal M}_{\phi}.

###### Proof.

By Theorem 1, it suffices to check F ⁡ ( μ) ≥ 0 F(\mu)\geq 0 for μ = δ ϕ \mu=\delta_{\phi} and μ = p ​ δ x + ( 1 − p) ​ δ 0 \mu=p\delta_{x}+(1-p)\delta_{0} with p = ϕ / x p=\phi/x and x ∈ [ϕ, 1] x\in[\phi,1]. In the former case,

 | F ⁡ ( μ) = H ⁡ ( ϕ 2) − H ⁡ ( ϕ) ≥ 0 F(\mu)=H(\phi^{2})-H(\phi)\geq 0 |  |

because ϕ ≥ ϕ ∗ ≥ φ \phi\geq\phi^{\ast}\geq\varphi by Lemma 8. In the latter case,

 | F ⁡ ( μ) = ϕ 2 x 2 ​ H ​ ( x 2) − ϕ x ​ H ​ ( x) = ϕ x 2 ​ ( ϕ ​ H ​ ( x 2) − x ​ H ​ ( x)) ≥ 0. F(\mu)=\frac{\phi^{2}}{x^{2}}H(x^{2})-\frac{\phi}{x}H(x)=\frac{\phi}{x^{2}}(\phi H(x^{2})-xH(x))\geq 0\,. |  |

∎

From Theorem 1, we deduce the following tight version of [6, Lemma 1]. Theorem 2 follows from Corollary 10 by the same argument as in [6, Proof of Theorem 1].

###### Corollary 10.

Suppose { p c } c ∈ 𝒮 ⊂ [0, 1] \{p_{c}\}_{c\in{\mathcal{S}}}\subset[0,1] is a finite sequence of real numbers and c c is a random variable supported on 𝒮 {\mathcal{S}} such that 𝔼 c [p c] ≤ 1 − ϕ ∗ \EE_{c}[p_{c}]\leq 1-\phi^{\ast}. If c ′ c^{\prime} is an independent copy of c c, then

 | 𝔼 c, c ′ [H ⁡ ( p c + p c ′ − p c ​ p c ′)] ≥ 𝔼 c [H ⁡ ( p c)]. \EE_{c,c^{\prime}}[H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})]\geq\EE_{c}[H(p_{c})]\,. |  |

###### Proof.

Let μ \mu be the distribution of x = 1 − p c x=1-p_{c}. Let ϕ = 𝔼 x ∼ μ [x] \phi=\EE_{x\sim\mu}[x], so ϕ > ϕ ∗ \phi>\phi^{\ast}. By Corollary 9,

 | 𝔼 c, c ′ [H ⁡ ( p c + p c ′ − p c ​ p c ′)] − 𝔼 c [H ⁡ ( p c)] = 𝔼 ( x, y) ∼ μ × μ H ​ ( xy) − 𝔼 x ∼ μ H ​ ( x) = F ⁡ ( μ) ≥ 0. \EE_{c,c^{\prime}}[H(p_{c}+p_{c^{\prime}}-p_{c}p_{c^{\prime}})]-\EE_{c}[H(p_{c})]=\EE_{(x,y)\sim\mu\times\mu}H(xy)-\EE_{x\sim\mu}H(x)=F(\mu)\geq 0\,. |  |

∎

Finally, we verify Claim 4 assuming Claim 3.

###### Proof of Claim 4.

Claim 3 and monotonicity of the condition defining S S imply that ϕ ∗ ≤ φ \phi^{\ast}\leq\varphi, while Lemma 8 gives ϕ ∗ ≥ φ \phi^{\ast}\geq\varphi. ∎

## References

- [1] Polymath 11. https://gowers.wordpress.com/2016/01/21/
frankls-union-closed-conjecture-a-possible-polymath-project/.
- [2] Balla, I., Bollobás, B., and Eccles, T. Union-closed families of sets. Journal of Combinatorial Theory, Series A 120, 3 (2013), 531–544.
- [3] Bruhn, H., and Schaudt, O. The journey of the union-closed sets conjecture. Graphs and Combinatorics 31, 6 (2015), 2043–2074.
- [4] Chase, Z., and Lovett, S. Approximate union closed conjecture. arXiv preprint arXiv:2211.11689 (2022).
- [5] Ellis, D. Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture. arXiv preprint arXiv:2211.12401 (2022).
- [6] Gilmer, J. A constant lower bound for the union-closed sets conjecture. arXiv preprint arXiv:2211.09055 (2022).
- [7] Karpas, I. Two results on union-closed families. arXiv preprint arXiv:1708.01434 (2017).
- [8] Knill, E. Graph generated union-closed families of sets. arXiv preprint math/9409215 (1994).
- [9] Peabody, L. Extension of a Method of Gilmer. arXiv preprint arXiv:2211.13139 (2022).
- [10] Sawin, W. An improved lower bound for the union-closed set conjecture. arXiv preprint arXiv:2211.11504 (2022).
- [11] Wójcik, P. Union-closed families of sets. Discrete Mathematics 199, 1-3 (1999), 173–182.

## Appendix A Proof of Claim 3

In this appendix, we prove Claim 3. Throughout this appendix, we use Claims to indicate results requiring the correctness of computer outputs within margin of error 10 − 3 10^{-3} or greater. The only computations which rely on a computer are the entries in Tables 1 and 2. Figure 1 plots the function

 | G ⁡ ( x) = φ ​ H ​ ( x 2) − x ​ H ​ ( x), G(x)=\varphi H(x^{2})-xH(x), |  |

from which Claim 3 can be checked visually.

[image: Refer to caption] Figure 1: Plot of G ⁡ ( x) G(x) for x ∈ [0.6, 1] x\in[0.6,1]. Claim 3 states the minimum value of 0 0 on x ∈ [φ, 1] x\in[\varphi,1] is achieved precisely at the endpoints x ∈ { φ, 1 } x\in\{\varphi,1\}.

We show below that, assuming correctness of certain computer calculations to within margin of error 10 − 3 10^{-3},

 | G ⁡ ( x) ≥ 0, ∀ x ∈ [φ, 1]. G(x)\geq 0,\quad\forall x\in[\varphi,1]. |  |

The verification is done separately on the three intervals I 1 = [φ, 0.77], I 2 = [0.76, 0.98], I 3 = [0.98, 1] I_{1}=[\varphi,0.77],I_{2}=[0.76,0.98],I_{3}=[0.98,1].

### A.1 Verification on I 1 I_{1}

We first compute the derivative of G G:

 | G ′ ​ ( x) = \displaystyle G^{\prime}(x)= | 2 ​ x ​ φ ​ log ⁡ 1 − x 2 x 2 − H ⁡ ( x) − x ​ log ⁡ 1 − x x \displaystyle 2x\varphi\log\frac{1-x^{2}}{x^{2}}-H(x)-x\log\frac{1-x}{x} |  |

 |  | = 2 ​ x ​ φ ​ log ​ 1 − x 2 x 2 + x ​ log ​ x + ( 1 − x) ​ log ⁡ ( 1 − x) + x ​ log ​ x − x ​ log ⁡ ( 1 − x) \displaystyle=2x\varphi\log\frac{1-x^{2}}{x^{2}}+x\log x+(1-x)\log(1-x)+x\log x-x\log(1-x) |  |

 |  | = 2 ​ x ​ φ ​ log ⁡ 1 − x 2 x 2 + 2 ​ x ​ log ⁡ x + ( 1 − 2 ​ x) ​ log ⁡ ( 1 − x) \displaystyle=2x\varphi\log\frac{1-x^{2}}{x^{2}}+2x\log x+(1-2x)\log(1-x) |  |

Note that G ⁡ ( φ) = G ′ ​ ( φ) = 0 G(\varphi)=G^{\prime}(\varphi)=0, the latter since

 | G ′ ​ ( φ) \displaystyle G^{\prime}(\varphi) | = 2 ​ φ 2 ​ log ⁡ ( 1 / φ) + 2 ​ φ ​ log ⁡ ( φ) + ( 1 − 2 ​ φ) ​ log ⁡ ( φ 2) \displaystyle=2\varphi^{2}\log(1/\varphi)+2\varphi\log(\varphi)+(1-2\varphi)\log(\varphi^{2}) |  |

 |  | = ( − 2 ​ φ 2 + 2 ​ φ + 2 ​ ( 1 − 2 ​ φ)) ​ log ⁡ φ \displaystyle=(-2\varphi^{2}+2\varphi+2(1-2\varphi))\log\varphi |  |

 |  | = 2 ​ ( 1 − φ − φ 2) ​ log ⁡ ( φ) = 0. \displaystyle=2(1-\varphi-\varphi^{2})\log(\varphi)=0. |  |

###### Claim 11.

Claim 3 holds on I 1 = [φ, 0.77] I_{1}=[\varphi,0.77].

###### Proof.

As G ⁡ ( φ) = G ′ ​ ( φ) = 0 G(\varphi)=G^{\prime}(\varphi)=0, it suffices to verify that G G is convex on I 1 I_{1}. It is not hard to check that its second derivative equals G ′′ ​ ( x) = L ⁡ ( x) / ( 1 − x 2) G^{\prime\prime}(x)=L(x)/(1-x^{2}), where

 | L ⁡ ( x):= 2 ​ φ ​ ( 1 − x 2) ​ log ⁡ ( x − 2 − 1) − 4 ​ φ − 2 ​ x 2 ​ log ⁡ x + 2 ​ ( x 2 − 1) ​ log ⁡ ( 1 − x) + x + 2 ​ log ⁡ ( x) + 1. L(x):=2\varphi(1-x^{2})\log(x^{-2}-1)-4\varphi-2x^{2}\log x+2(x^{2}-1)\log(1-x)+x+2\log(x)+1\,. |  |

We now estimate the Lipschitz constant of each non-constant term of L L on x ∈ I 1 x\in I_{1}. For the first term,

 | | d d ​ x ​ ( 2 ​ φ ​ ( 1 − x 2) ​ log ⁡ ( x − 2 − 1)) | \displaystyle\left|\frac{d}{dx}\big(2\varphi(1-x^{2})\log(x^{-2}-1)\big)\right| | ≤ 2 ​ φ ​ sup x ∈ I 1 ( | 2 ​ x 3 | + 2 ​ | x ​ log ⁡ ( x − 2 − 1) |) \displaystyle\leq 2\varphi\sup_{x\in I_{1}}\big(|2x^{3}|+2|x\log(x^{-2}-1)|\big) |  | (5) |

 |  | ≤ 2 ​ φ ​ ( 1.1 + 1.6 ⋅ log ⁡ ( 2)) \displaystyle\leq 2\varphi(1.1+1.6\cdot\log(2)) |  |

 |  | ≤ 2 ​ φ ⋅ 2.3 ≤ 3 \displaystyle\leq 2\varphi\cdot 2.3\leq 3 |  |

since log ⁡ ( 2) ≤ 0.75 \log(2)\leq 0.75 and φ ≤ 5 / 8 \varphi\leq 5/8. Next,

 | | d d ​ x ​ ( 2 ​ x 2 ​ log ⁡ ( x)) | \displaystyle\left|\frac{d}{dx}\big(2x^{2}\log(x)\big)\right| | ≤ sup x ∈ I 1 | 4 ​ x ​ log ⁡ ( x) + 2 ​ x | \displaystyle\leq\sup_{x\in I_{1}}|4x\log(x)+2x| |  |

 |  | ≤ 1.6 ​ sup x ∈ I 1 | 2 ​ log ⁡ ( x) + 1 | \displaystyle\leq 1.6\sup_{x\in I_{1}}|2\log(x)+1| |  |

 |  | ≤ 1.6 \displaystyle\leq 1.6 |  |

since log ⁡ ( x) ∈ [− 1, 0] \log(x)\in[-1,0] for all x ∈ I 1 x\in I_{1}. Continuing, using log ⁡ ( 5) ≤ 2 \log(5)\leq 2,

 | | d d ​ x ​ ( 2 ​ ( x 2 − 1) ​ log ⁡ ( 1 − x)) | \displaystyle\left|\frac{d}{dx}\big(2(x^{2}-1)\log(1-x)\big)\right| | ≤ 2 ​ sup x ∈ I 1 | 2 ​ x ​ log ⁡ ( 1 − x) − x 2 − 1 1 − x | \displaystyle\leq 2\sup_{x\in I_{1}}|2x\log(1-x)-\frac{x^{2}-1}{1-x}| |  |

 |  | ≤ 2 ​ sup x ∈ I 1 | 2 ​ x ​ log ⁡ ( 1 − x) + x + 1 | \displaystyle\leq 2\sup_{x\in I_{1}}|2x\log(1-x)+x+1| |  |

 |  | ≤ 2 ⋅ max ⁡ ( 1.6 ​ log ⁡ ( 5), 1.8) \displaystyle\leq 2\cdot\max(1.6\log(5),1.8) |  |

 |  | ≤ 2 ⋅ 1.6 ⋅ 2 = 6.4. \displaystyle\leq 2\cdot 1.6\cdot 2=6.4. |  |

Finally d d ​ x ​ ( x) = 1 \frac{d}{dx}(x)=1 and d d ​ x ​ ( 2 ​ log ⁡ x) = 2 / x ≤ 3.5 \frac{d}{dx}(2\log x)=2/x\leq 3.5. Moreover the derivative from the term ( 5) is negative as both terms are positive and decreasing, while the derivative from 2 ​ log ⁡ x 2\log x is clearly positive. Combining, we find that L ⁡ ( x) L(x) restricted to I 1 I_{1} has Lipschitz constant at most

 | 1.6 + 6.4 + 1 + max ⁡ ( 3, 3.5) ≤ 12.5. 1.6+6.4+1+\max(3,3.5)\leq 12.5. |  |

Therefore to show G G is convex and hence non-negative on I 1 = [φ, 0.77] I_{1}=[\varphi,0.77] it suffices to exhibit a 1 250 \frac{1}{250} -dense subset of I 1 I_{1} on which L ⁡ ( x) = ( 1 − x 2) ​ G ′′ ​ ( x) ≥ 12.5 250 = 0.05 L(x)=(1-x^{2})G^{\prime\prime}(x)\geq\frac{12.5}{250}=0.05. In Table 1 below we compute the values of L L on each multiple of 1 200 \frac{1}{200} from 0.6 0.6 to 0.77 0.77 inclusive. We in fact find that L ⁡ ( x) ≥ 0.09 L(x)\geq 0.09 holds at all of these points, completing the numerical verification on I 1 I_{1}. ∎

x x | L ⁡ ( x) L(x) | x x | L ⁡ ( x) L(x) | x x | L ⁡ ( x) L(x) | x x | L ⁡ ( x) L(x) | x x | L ⁡ ( x) L(x) | x x | L ⁡ ( x) L(x) |

0.600 | 0.1020 | 0.630 | 0.1117 | 0.660 | 0.1173 | 0.690 | 0.1182 | 0.720 | 0.1137 | 0.750 | 0.1032 |

0.605 | 0.1039 | 0.635 | 0.1130 | 0.665 | 0.1178 | 0.695 | 0.1178 | 0.725 | 0.1124 | 0.755 | 0.1009 |

0.610 | 0.1057 | 0.640 | 0.1141 | 0.670 | 0.1182 | 0.700 | 0.1173 | 0.730 | 0.1109 | 0.760 | 0.0983 |

0.615 | 0.1074 | 0.645 | 0.1151 | 0.675 | 0.1184 | 0.705 | 0.1167 | 0.735 | 0.1093 | 0.765 | 0.0955 |

0.620 | 0.1089 | 0.650 | 0.1159 | 0.680 | 0.1185 | 0.710 | 0.1159 | 0.740 | 0.1075 | 0.770 | 0.0925 |

0.625 | 0.1104 | 0.655 | 0.1167 | 0.685 | 0.1184 | 0.715 | 0.1149 | 0.745 | 0.1054 |  |  |

Table 1: Evaluations of L L to precision 10 − 4 10^{-4}. All values appear to be at least 0.09 0.09, and it suffices for all values to be at least 0.05 0.05.

### A.2 Verification on I 2 I_{2}

Our verification for x ∈ I 2 x\in I_{2} is based on evaluating G G. We write G ⁡ ( x) = g 1 ​ ( x) − g 2 ​ ( x) G(x)=g_{1}(x)-g_{2}(x) for

 | g 1 ​ ( x) \displaystyle g_{1}(x) | = φ ​ H ​ ( x 2), \displaystyle=\varphi H(x^{2}), |  |

 | g 2 ​ ( x) \displaystyle g_{2}(x) | = x ​ H ​ ( x). \displaystyle=xH(x). |  |

Note that g 1 g_{1} is clearly decreasing on I 2 I_{2}. The next lemma shows the same for g 2 g_{2}.

###### Lemma 12.

g 2 g_{2} is decreasing on [5 / 7, 1] ⊇ I 2 [5/7,1]\supseteq I_{2}.

###### Proof.

First we claim that it suffices to show g 2 ′ ​ ( 5 / 7) ≤ 0 g_{2}^{\prime}(5/7)\leq 0. This is because

 | g 2 ′ ​ ( x) \displaystyle g_{2}^{\prime}(x) | = H ⁡ ( x) + x ​ log ⁡ 1 − x x \displaystyle=H(x)+x\log\frac{1-x}{x} |  |

 |  | = 2 ​ x ​ log ⁡ 1 x − ( 2 ​ x − 1) ​ log ⁡ 1 1 − x \displaystyle=2x\log\frac{1}{x}-(2x-1)\log\frac{1}{1-x} |  |

so g 2 ′ ​ ( x) ≤ 0 g_{2}^{\prime}(x)\leq 0 if and only if

 | ( 1 − 1 2 ​ x) ​ log ⁡ 1 1 − x ≥ log ⁡ 1 x \left(1-\frac{1}{2x}\right)\log\frac{1}{1-x}\geq\log\frac{1}{x} |  | (6) |

and here both terms on the left-hand side are increasing while the right-hand side is decreasing.

It remains to show that g 2 ′ ​ ( 5 / 7) ≤ 0 g_{2}^{\prime}(5/7)\leq 0 which in light of ( 6) is equivalent to showing

 | 3 10 ​ log ⁡ ( 7 / 2) ≥ log ⁡ ( 7 / 5), \frac{3}{10}\log(7/2)\geq\log(7/5), |  |

i.e. ( 7 / 5) 10 / 3 ≤ 7 / 2 (7/5)^{10/3}\leq 7/2. This holds because ( 7 / 5) 3 ≤ 2 ​ ( 7 / 5) = 14 / 5 (7/5)^{3}\leq 2(7/5)=14/5 and 7 / 5 ≤ ( 5 4) 3 = ( 7 / 2 14 / 5) 3 7/5\leq\left(\frac{5}{4}\right)^{3}=\left(\frac{7/2}{14/5}\right)^{3}. ∎

###### Claim 13.

Claim 3 holds for x ∈ I 2 x\in I_{2}.

###### Proof.

We computer-evaluate g 1, g 2 g_{1},g_{2} at a finite set of values x 1 < x 2 < ⋯ < x 97 x_{1}<x_{2}<\dots<x_{97} with 5 / 7 < x 1 < 0.76 5/7<x_{1}<0.76 and x 9 = 0.98 x_{9}=0.98 and verify that g 1 ​ ( x i + 1) ≥ g 2 ​ ( x i) g_{1}(x_{i+1})\geq g_{2}(x_{i}) for each i i. The values are shown in Table 2; note that in all cases g 1 ​ ( x i + 1) − g 2 ​ ( x i) ≥ 2 1000 g_{1}(x_{i+1})-g_{2}(x_{i})\geq\frac{2}{1000} holds, modulo rounding to four decimal places. The intervals [x i, x i + 1] [x_{i},x_{i+1}] cover I 2 I_{2}, and for all x ∈ [x i, x i + 1] x\in[x_{i},x_{i+1}] we have

 | g 2 ​ ( x) ≤ g 2 ​ ( x i) ≤ g 1 ​ ( x i + 1) ≤ g 1 ​ ( x). g_{2}(x)\leq g_{2}(x_{i})\leq g_{1}(x_{i+1})\leq g_{1}(x)\,. |  |

∎

x x | g 1 ​ ( x) g_{1}(x) | g 2 ​ ( x) g_{2}(x) | x x | g 1 ​ ( x) g_{1}(x) | g 2 ​ ( x) g_{2}(x) | x x | g 1 ​ ( x) g_{1}(x) | g 2 ​ ( x) g_{2}(x) | x x | g 1 ​ ( x) g_{1}(x) | g 2 ​ ( x) g_{2}(x) |

0.7598 | 0.4210 | 0.4189 | 0.7797 | 0.4139 | 0.4111 | 0.8472 | 0.3678 | 0.3622 | 0.9350 | 0.2338 | 0.2249 |

0.7600 | 0.4209 | 0.4188 | 0.7814 | 0.4131 | 0.4103 | 0.8507 | 0.3643 | 0.3586 | 0.9380 | 0.2270 | 0.2180 |

0.7603 | 0.4208 | 0.4187 | 0.7832 | 0.4124 | 0.4095 | 0.8543 | 0.3606 | 0.3547 | 0.9409 | 0.2202 | 0.2112 |

0.7606 | 0.4207 | 0.4186 | 0.7851 | 0.4115 | 0.4085 | 0.8579 | 0.3567 | 0.3507 | 0.9437 | 0.2134 | 0.2045 |

0.7609 | 0.4206 | 0.4185 | 0.7871 | 0.4106 | 0.4075 | 0.8615 | 0.3528 | 0.3465 | 0.9465 | 0.2065 | 0.1975 |

0.7613 | 0.4205 | 0.4184 | 0.7892 | 0.4095 | 0.4064 | 0.8651 | 0.3486 | 0.3422 | 0.9492 | 0.1996 | 0.1907 |

0.7617 | 0.4204 | 0.4183 | 0.7913 | 0.4085 | 0.4053 | 0.8688 | 0.3442 | 0.3377 | 0.9518 | 0.1927 | 0.1839 |

0.7621 | 0.4203 | 0.4181 | 0.7935 | 0.4074 | 0.4041 | 0.8725 | 0.3397 | 0.3330 | 0.9543 | 0.1860 | 0.1772 |

0.7626 | 0.4201 | 0.4180 | 0.7958 | 0.4062 | 0.4028 | 0.8762 | 0.3350 | 0.3281 | 0.9567 | 0.1793 | 0.1706 |

0.7631 | 0.4200 | 0.4178 | 0.7982 | 0.4048 | 0.4014 | 0.8799 | 0.3301 | 0.3230 | 0.9590 | 0.1728 | 0.1641 |

0.7637 | 0.4198 | 0.4176 | 0.8007 | 0.4034 | 0.3999 | 0.8836 | 0.3251 | 0.3178 | 0.9612 | 0.1663 | 0.1577 |

0.7643 | 0.4196 | 0.4174 | 0.8033 | 0.4019 | 0.3983 | 0.8873 | 0.3198 | 0.3124 | 0.9633 | 0.1600 | 0.1515 |

0.7650 | 0.4194 | 0.4171 | 0.8060 | 0.4003 | 0.3965 | 0.8909 | 0.3146 | 0.3070 | 0.9654 | 0.1535 | 0.1452 |

0.7657 | 0.4191 | 0.4169 | 0.8088 | 0.3985 | 0.3947 | 0.8945 | 0.3092 | 0.3014 | 0.9674 | 0.1472 | 0.1390 |

0.7665 | 0.4189 | 0.4166 | 0.8116 | 0.3967 | 0.3927 | 0.8981 | 0.3035 | 0.2957 | 0.9693 | 0.1411 | 0.1330 |

0.7673 | 0.4186 | 0.4163 | 0.8145 | 0.3948 | 0.3907 | 0.9017 | 0.2977 | 0.2897 | 0.9711 | 0.1351 | 0.1271 |

0.7682 | 0.4183 | 0.4159 | 0.8175 | 0.3927 | 0.3884 | 0.9052 | 0.2919 | 0.2838 | 0.9728 | 0.1293 | 0.1215 |

0.7692 | 0.4179 | 0.4156 | 0.8206 | 0.3904 | 0.3861 | 0.9087 | 0.2859 | 0.2776 | 0.9744 | 0.1237 | 0.1160 |

0.7702 | 0.4176 | 0.4152 | 0.8237 | 0.3881 | 0.3836 | 0.9122 | 0.2797 | 0.2713 | 0.9759 | 0.1183 | 0.1109 |

0.7713 | 0.4172 | 0.4147 | 0.8269 | 0.3857 | 0.3810 | 0.9156 | 0.2734 | 0.2650 | 0.9773 | 0.1132 | 0.1059 |

0.7725 | 0.4167 | 0.4142 | 0.8301 | 0.3831 | 0.3783 | 0.9190 | 0.2670 | 0.2584 | 0.9787 | 0.1080 | 0.1009 |

0.7738 | 0.4163 | 0.4137 | 0.8334 | 0.3803 | 0.3754 | 0.9223 | 0.2606 | 0.2519 | 0.9800 | 0.1030 | 0.0961 |

0.7752 | 0.4157 | 0.4131 | 0.8368 | 0.3774 | 0.3723 | 0.9256 | 0.2539 | 0.2452 |  |  |  |

0.7766 | 0.4152 | 0.4125 | 0.8402 | 0.3744 | 0.3691 | 0.9288 | 0.2473 | 0.2385 |  |  |  |

0.7781 | 0.4145 | 0.4119 | 0.8437 | 0.3711 | 0.3657 | 0.9319 | 0.2406 | 0.2318 |  |  |  |

Table 2: Evaluations of g 1 g_{1} and g 2 g_{2} to precision 10 − 4 10^{-4}. We require that for consecutive inputs x i < x i + 1 x_{i}<x_{i+1} in the table, g 1 ​ ( x i + 1) − g 2 ​ ( x i) ≥ 0 g_{1}(x_{i+1})-g_{2}(x_{i})\geq 0. The values shown in fact satisfy g 1 ​ ( x i + 1) − g 2 ​ ( x i) ≥ 2 1000 g_{1}(x_{i+1})-g_{2}(x_{i})\geq\frac{2}{1000} modulo rounding.

### A.3 Verification on I 3 I_{3}

###### Proposition 14.

Claim 3 holds for x ∈ I 3 x\in I_{3}.

###### Proof.

Taylor expansion of log ⁡ ( 1 − ε) \log(1-\varepsilon) gives that for all ε ∈ ( 0, 1) \varepsilon\in(0,1),

 | ε ⁡ ( log ⁡ 1 ε + 1 − ε) ≤ H ⁡ ( ε) ≤ ε ⁡ ( log ⁡ 1 ε + 1). \varepsilon\left(\log\frac{1}{\varepsilon}+1-\varepsilon\right)\leq H(\varepsilon)\leq\varepsilon\left(\log\frac{1}{\varepsilon}+1\right)\,. |  |

Let x = 1 − ε x=1-\varepsilon for ε ∈ [0, 0.02] \varepsilon\in[0,0.02]. Then

 | g 1 ​ ( x) \displaystyle g_{1}(x) | = φ ​ H ​ ( 2 ​ ε − ε 2) ≥ φ ​ ε ​ ( 2 − ε) ​ ( log ⁡ 1 ε − log ⁡ ( 2 − ε) + ( 1 − ε) 2), \displaystyle=\varphi H(2\varepsilon-\varepsilon^{2})\geq\varphi\varepsilon(2-\varepsilon)\big(\log\frac{1}{\varepsilon}-\log(2-\varepsilon)+(1-\varepsilon)^{2}\big)\,, |  |

 | g 2 ​ ( x) \displaystyle g_{2}(x) | = ( 1 − ε) ​ H ​ ( ε) ≤ ε ⁡ ( 1 − ε) ​ ( log ⁡ 1 ε + 1). \displaystyle=(1-\varepsilon)H(\varepsilon)\leq\varepsilon(1-\varepsilon)\big(\log\frac{1}{\varepsilon}+1\big)\,. |  |

Dividing by ε \varepsilon, it suffices to prove

 | ( ( 2 ​ φ − 1) + ( 1 − φ) ​ ε) ​ log ⁡ 1 ε ≥ ( 1 − ε) ​ ( 1 − φ ⁡ ( 1 − ε) ​ ( 2 − ε)) + φ ⁡ ( 2 − ε) ​ log ⁡ ( 2 − ε). \big((2\varphi-1)+(1-\varphi)\varepsilon\big)\log\frac{1}{\varepsilon}\geq(1-\varepsilon)\left(1-\varphi(1-\varepsilon)(2-\varepsilon)\right)+\varphi(2-\varepsilon)\log(2-\varepsilon). |  |

Noting φ ⁡ ( 1 − ε) ​ ( 2 − ε) ≥ 1 \varphi(1-\varepsilon)(2-\varepsilon)\geq 1 in the first line below, we next find

 |  | ( 1 − ε) ​ ( 1 − φ ⁡ ( 1 − ε) ​ ( 2 − ε)) + φ ⁡ ( 2 − ε) ​ log ⁡ ( 2 − ε) ≤ 2 ​ φ ​ log ​ 2 = ( 5 − 1) ​ log ​ 2, \displaystyle(1-\varepsilon)\left(1-\varphi(1-\varepsilon)(2-\varepsilon)\right)+\varphi(2-\varepsilon)\log(2-\varepsilon)\leq 2\varphi\log 2=(\sqrt{5}-1)\log 2, |  |

 |  | ( ( 2 ​ φ − 1) + ( 1 − φ) ​ ε) ​ log ⁡ 1 ε ≥ ( 2 ​ φ − 1) ​ log ⁡ 1 ε ≥ ( 5 − 2) ​ log ⁡ 50. \displaystyle\left((2\varphi-1)+(1-\varphi)\varepsilon\right)\log\frac{1}{\varepsilon}\geq(2\varphi-1)\log\frac{1}{\varepsilon}\geq(\sqrt{5}-2)\log 50. |  |

Finally ( 5 − 2) ​ log ⁡ 50 ≥ ( 5 − 1) ​ log ⁡ 2 (\sqrt{5}-2)\log 50\geq(\sqrt{5}-1)\log 2 because

 | log 2 ⁡ ( 50) \displaystyle\log_{2}(50) | ≥ log 2 ⁡ ( 2 5 ⋅ 1.5) ≥ 5.5 \displaystyle\geq\log_{2}(2^{5}\cdot 1.5)\geq 5.5 |  |

 |  | ≥ 3 + 5 = ( 5 − 1) / ( 5 − 2). \displaystyle\geq 3+\sqrt{5}=(\sqrt{5}-1)/(\sqrt{5}-2). |  |

Hence the proof is complete. Equality holds if and only if ε = 0 \varepsilon=0, i.e. x = 1 x=1. ∎

###### Proof of Claim 3.

Follows by combining Claims 11, 13 and Proposition 14. ∎


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
