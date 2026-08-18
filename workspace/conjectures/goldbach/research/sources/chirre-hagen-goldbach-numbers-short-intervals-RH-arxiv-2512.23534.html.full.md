<!-- source: https://arxiv.org/html/2512.23534v1 | converted from HTML -->

On Goldbach numbers in short intervals

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2512.23534v1 [math.NT] 29 Dec 2025

# On Goldbach numbers in short intervals Thanks: MVH is supported in part by Grant 334466 of the Research Council of Norway.

Andrés Chirre and Markus Valås Hagen Address: Departamento de Ciencias - Sección Matemáticas, Pontificia Universidad Católica del Perú, Av. Universitaria 1801, San Miguel 15088, Lima, Perú Email address: [cchirre@pucp.edu.pe][3] Address: Department of Mathematical Sciences, Norwegian University of Science and Technology (NTNU), 7491 Trondheim, Norway Email address: [markus.v.hagen@ntnu.no][4]

###### Abstract.

Assuming the Riemann Hypothesis, we prove that for all x ≥ 2 x\geq 2, there exists at least one even integer within the interval ( x, x + 123 log 2 x] (x,x+123\log^{2}x], that can be expressed as the sum of two primes. This result is an improvement over the recent work of Cully-Hugill and Dudek, who obtained the constant 9696 9696 instead of 123 123.

###### 2020 Mathematics Subject Classification

11M26, 11P32

## 1. Introduction

One of the most famous open problems in number theory is the Goldbach conjecture. It states that every even number greater than 2 2 can be written as a sum of two primes. Although the conjecture still remains open, a significant amount of progress has been made towards it. One of them is the big breakthrough achieved by Helfgott [9], building on work of Vinogradov, who proved the weak Goldbach conjecture - the statement that every odd number greater than 5 5 can be written as a sum of three primes.

Since the original Goldbach conjecture still seems to be out of reach, it is natural to ask on how short intervals we can exhibit a number that is the sum of two primes. To make this precise, the notion of a Goldbach number has been introduced - this is a positive integer that is the sum of two odd primes. The Goldbach conjecture is the statement that there is a Goldbach number in any interval ( x, x + 2] (x,x+2] for any x > 4 x>4. If we consider the interval ( x, x + H] (x,x+H], how small can we take H H and still ensure the existence of a Goldbach number in our interval?

Using strong unconditional results on zeroes of L L -functions due to Gallagher [8], Montgomery–Vaughan [14] were able to prove that there is a Goldbach number in the interval ( x, x + x 7 72 + ε) (x,x+x^{\frac{7}{72}+\varepsilon}). Assuming the Riemann Hypothesis (RH), the first result on Goldbach numbers in short intervals was obtained by Linnik in [13], where he proved that [x, x + log 3 + ε ⁡ x] [x,x+\log^{3+\varepsilon}x] contains a Goldbach number for sufficiently large x x. Later, Katai [12] and Montgomery–Vaughan [14], improved the interval independently to [x, x + H] [x,x+H] where H = O ⁡ ( log 2 ⁡ x) H=O(\log^{2}x), and with x x still sufficiently large. The order of H H hasn’t been improved since.

In a recent paper [7], Cully-Hugill and Dudek made the method of Montgomery and Vaughan explicit. This allowed them to prove that there is a Goldbach number in the interval ( x, x + 9696 log 2 x] (x,x+9696\log^{2}x] for all x ≥ 2 x\geq 2, assuming RH. The heart of their proof lies in finding an explicit bound for an integral, first studied by Selberg in [18]. For x ≥ 1 x\geq 1 and δ > 0 \delta>0, it is defined by

 | J θ ​ ( x, δ) = ∫ 1 x ( θ ⁡ ( ( 1 + δ) ​ y) − θ ⁡ ( y) − δ ​ y) 2 ​ d ​ y, \displaystyle J_{\theta}(x,\delta)=\int_{1}^{x}\big(\theta((1+\delta)y)-\theta(y)-\delta y\big)^{2}\text{\rm d}y, |  | (1.1) |

where θ ⁡ ( x) = ∑ p ≤ x log ⁡ p \theta(x)=\sum_{p\leq x}\log p. Assuming RH, Cully-Hugill–Dudek proved that J θ ​ ( x, δ) < 202 ​ δ ​ x 2 ​ log 2 ​ x J_{\theta}(x,\delta)<202\delta x^{2}\log^{2}x, for x ≥ 10 8 x\geq 10^{8} and δ ∈ ( 0, 10 − 8] \delta\in(0,10^{-8}]. Their method focuses on bounding the second moment of the logarithmic derivative of the Riemann zeta-function in the critical strip, which they control explicitly via Selberg’s moment formula.

The purpose of this paper is to improve on the interval ( x, x + 9696 log 2 x] (x,x+9696\log^{2}x]. We establish the following result.

###### Theorem 1.

Assume RH. Then there is a Goldbach number in the interval ( x, x + 123 log 2 x] (x,x+123\log^{2}x] for all x ≥ 2 x\geq 2.

Ultimately, we will deduce Theorem 1 from an explicit bound for J θ ​ ( x, δ) J_{\theta}(x,\delta), like Cully-Hugill–Dudek. However, our approach for bounding this quantity differs significantly from theirs. We work directly with the zeros of the Riemann zeta-function, employing the explicit formula for the Chebyshev function ψ ⁡ ( x) = ∑ n ≤ x Λ ⁡ ( n), \psi(x)=\sum_{n\leq x}\Lambda(n), where Λ ⁡ ( n) \Lambda(n) is the von Mangoldt function defined by Λ ⁡ ( n) = log ⁡ p \Lambda(n)=\log p if n = p k n=p^{k} for a prime p p and k ∈ ℕ k\in\mathbb{N}, and Λ ⁡ ( n) = 0 \Lambda(n)=0 otherwise. Then, we use an averaging technique introduced by Saffari and Vaughan in [17], to bound 1 1 1 In fact, in [17], it is proved that J ψ ​ ( x, δ) ≪ δ ​ x 2 ​ log 2 ⁡ ( 2 / δ) J_{\psi}(x,\delta)\ll\delta x^{2}\log^{2}({2}/{\delta}) for x ≥ 4 x\geq 4 and 0 < δ ≤ 1 0<\delta\leq 1. explicitly

 | J ψ ​ ( x, δ):= ∫ 1 x ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y) 2 ​ d ​ y. \displaystyle J_{\psi}(x,\delta):=\int_{1}^{x}\big(\psi((1+\delta)y)-\psi(y)-\delta y\big)^{2}\text{\rm d}y. |  | (1.2) |

The rest of the proof is then devoted to pass from J ψ ​ ( x, δ) J_{\psi}(x,\delta) to J θ ​ ( x, δ) J_{\theta}(x,\delta) which is a surprisingly more delicate process than one would anticipate. This seems to be mainly because we are working with primes in short intervals.

The structure of the paper is as follows. In Section 2, we present several explicit estimates for some objects related to the Riemann zeta-function and its non-trivial zeros. Section 3 is devoted to establishing an explicit bound for J ψ ​ ( x, δ) J_{\psi}(x,\delta) through the averaging method. Building upon this result, in Section 4 we derive a bound for J θ ​ ( x, δ) J_{\theta}(x,\delta) by carefully analyzing the associated error term. In Section 5, we prove Theorem 1 as a consequence of the explicit estimate for J θ ​ ( x, δ) J_{\theta}(x,\delta). Finally, in Section A we write an appendix with some explicit bounds for certain sums of prime numbers that appears in our proof.

## Acknowledgements

We would like to thank Adrian Dudek, Winston Heap, Harald Helfgott, Kristian Seip, Timothy Trudgian and Denis Zelent for their valuable suggestions on earlier versions of the paper. Some of the work present in this paper was carried out while MVH was visiting Louis-Pierre Arguin at the University of Oxford in Spring 2025. He would like to thank the university for the hospitality and the excellent working conditions provided there.

## 2. Lemmas related to the Riemann zeta-function and its zeros

Let ζ ⁡ ( s) \zeta(s) be the Riemann zeta-function, and assume RH, i.e. all non-trivial zeros of ζ ⁡ ( s) \zeta(s) have the form ρ = 1 2 + i ​ γ \rho=\tfrac{1}{2}+i\gamma where γ ∈ ℝ \gamma\in\mathbb{R}.

###### Lemma 2.1.

Assume RH. Then, for 1 ≤ σ ≤ 2 1\leq\sigma\leq 2 and | t | ≥ 100 |t|\geq 100 we have 2 2 2 We should mention that one can do better - the classical conditional bound for the logarithmic derivative of the Riemann zeta-function at the point 1 + i ​ t 1+it is O ⁡ ( log ⁡ log ⁡ t) O(\log\log t). The best explicit result is given by the authors and Simonič in [5, Theorem 5], but this is only useful when t t is really large.

 | | ζ ′ ζ ​ ( σ + i ​ t) | ≤ 4 ​ log ⁡ | t |. \left|\dfrac{\zeta^{\prime}}{\zeta}(\sigma+it)\right|\leq 4\log|t|. |  |

###### Proof.

We adopt Backlund’s approach from [1], where he established bounds for | ζ ⁡ ( σ + i ​ t) | |\zeta(\sigma+it)|. Let N ≥ 3 N\geq 3, 1 < σ < 2 1<\sigma<2 and | t | ≥ 100 |t|\geq 100. By the Dirichlet series representation of ζ ′ / ζ \zeta^{\prime}/\zeta, and integration by parts, one can see that

 | − ζ ′ ζ ​ ( σ + i ​ t) = ∑ n = 1 N − 1 Λ ⁡ ( n) n σ + i ​ t − ψ ⁡ ( N −) − N N σ + i ​ t + N 1 − ( σ + i ​ t) σ + i ​ t − 1 + ( σ + i ​ t) ​ ∫ N ∞ ψ ⁡ ( y) − y y σ + i ​ t + 1 ​ d ​ y. \displaystyle-\dfrac{\zeta^{\prime}}{\zeta}(\sigma+it)=\sum_{n=1}^{N-1}\dfrac{\Lambda(n)}{n^{\sigma+it}}-\dfrac{\psi(N^{-})-N}{N^{\sigma+it}}+\dfrac{N^{1-({\sigma+it})}}{{\sigma+it}-1}+({\sigma+it})\int_{N}^{\infty}\dfrac{\psi(y)-y}{y^{{\sigma+it}+1}}\text{\rm d}y. |  | (2.1) |

Let us bound each term on the right-hand side of ( 2.1). By [11, Lemma 10] we get

 | | ∑ n = 1 N − 1 Λ ⁡ ( n) n σ + i ​ t | ≤ ∑ n = 1 N − 1 Λ ⁡ ( n) n ≤ log ⁡ ( N − 1) − γ + 1.3 log 2 ⁡ ( N − 1). \left|\sum_{n=1}^{N-1}\dfrac{\Lambda(n)}{n^{\sigma+it}}\right|\leq\sum_{n=1}^{N-1}\dfrac{\Lambda(n)}{n}\leq\log(N-1)-\gamma+\dfrac{1.3}{\log^{2}(N-1)}. |  |

We now proceed to bound the other terms appearing in ( 2.1). First we observe the trivial bound | N 1 − ( σ + i ​ t) / ( σ + i ​ t − 1) | ≤ 1 / | t |. |{N^{1-({\sigma+it})}}/{({\sigma+it}-1)}|\leq 1/|t|. To bound the two terms involving ψ \psi, we recall an explicit conditional bound of the error term in the prime number theorem (see [19, Theorem 10]): for all y ≥ 73.2 y\geq 73.2 we have | ψ ⁡ ( y) − y | ≤ y ​ log 2 ​ y / 8 ​ π |\psi(y)-y|\leq{\sqrt{y}\log^{2}y}/{8\pi}. Thus, if N ≠ p k N\neq p^{k} and N ≥ 74 N\geq 74, we have

 | | ψ ⁡ ( N −) − N N σ + i ​ t | ≤ log 2 ⁡ N 8 ​ π ​ N. \left|\dfrac{\psi(N^{-})-N}{N^{\sigma+it}}\right|\leq\dfrac{\log^{2}N}{8\pi\sqrt{N}}. |  |

We bound the last term as follows

 | | ( σ + i ​ t) ​ ∫ N ∞ ψ ⁡ ( y) − y y σ + i ​ t + 1 ​ d ​ y | ≤ | σ + i ​ t | 8 ​ π ​ ∫ N ∞ y ​ log 2 ​ y y 2 ​ 𝑑 y = | σ + i ​ t | 4 ​ π ​ ( log 2 ⁡ N + 4 ​ log ⁡ N + 8 N). \left|({\sigma+it})\int_{N}^{\infty}\dfrac{\psi(y)-y}{y^{{\sigma+it}+1}}\text{\rm d}y\right|\leq\dfrac{|{\sigma+it}|}{8\pi}\int_{N}^{\infty}\dfrac{\sqrt{y}\log^{2}y}{y^{2}}dy=\dfrac{|{\sigma+it}|}{4\pi}\left(\dfrac{\log^{2}N+4\log N+8}{\sqrt{N}}\right). |  |

So, since t ≥ 100 t\geq 100 and 1 < σ < 2 1<\sigma<2, we obtain

 | | ( σ + i ​ t) ​ ∫ N ∞ ψ ⁡ ( y) − y y σ + i ​ t + 1 ​ d ​ y | ≤ 1.001 ​ | t | 4 ​ π ​ ( log 2 ⁡ N + 4 ​ log ⁡ N + 8 N). \left|{(\sigma+it)}\int_{N}^{\infty}\dfrac{\psi(y)-y}{y^{{\sigma+it}+1}}\text{\rm d}y\right|\leq\dfrac{1.001|t|}{4\pi}\left(\dfrac{\log^{2}N+4\log N+8}{\sqrt{N}}\right). |  |

Thus, in ( 2.1),

 | | ζ ′ ζ ​ ( σ + i ​ t) | ≤ log ⁡ ( N − 1) + 1.001 ​ | t | 4 ​ π ​ ( log 2 ⁡ N + 4 ​ log ⁡ N + 8 N) − γ + 1.3 log 2 ⁡ ( N − 1) + 1 | t | + log 2 ⁡ N 8 ​ π ​ N. \left|\dfrac{\zeta^{\prime}}{\zeta}(\sigma+it)\right|\leq\log(N-1)+\dfrac{1.001|t|}{4\pi}\left(\dfrac{\log^{2}N+4\log N+8}{\sqrt{N}}\right)-\gamma+\dfrac{1.3}{\log^{2}(N-1)}+\dfrac{1}{|t|}+\dfrac{\log^{2}N}{8\pi\sqrt{N}}. |  |

Choosing N = [| t | 4] + 1 N=[|t|^{4}]+1 we get

 | | ζ ′ ζ ​ ( σ + i ​ t) | ≤ 4 ​ log ⁡ | t |. \left|\dfrac{\zeta^{\prime}}{\zeta}(\sigma+it)\right|\leq 4\log|t|. |  |

Finally, by continuity we arrive at the desired result for 1 ≤ σ ≤ 2 1\leq\sigma\leq 2 and | t | ≥ 100 |t|\geq 100. ∎

###### Lemma 2.2.

Assume RH. Then, the following is true, where the sums run over the imaginary parts γ \gamma of the non-trivial zeros of ζ ⁡ ( s) \zeta(s).

1. (1)

For | t | ≥ 4 |t|\geq 4 we have

 | ∑ γ 1 6 + ( t − γ) 2 ≤ log ⁡ | t | 2 ​ 6. \displaystyle\sum_{\gamma}\dfrac{1}{6+(t-\gamma)^{2}}\leq\dfrac{\log|t|}{2\sqrt{6}}. |  | (2.2) |

2. (2)

For | t | ≥ 100 |t|\geq 100 we have

 | ∑ γ 1 1 4 + ( t − γ) 2 ≤ 9 ​ log ⁡ | t |. \displaystyle\sum_{\gamma}\dfrac{1}{\frac{1}{4}+(t-\gamma)^{2}}\leq 9\,{\log|t|}. |  | (2.3) |

###### Proof.

Letting s = α + i ​ t s=\alpha+it, and taking the real part of the fractional decomposition of ζ ⁡ ( s) \zeta(s) (see [15, Corollary 10.14]) one has

 | ∑ ρ α − Re ​ ρ ( α − Re ​ ρ) 2 + ( t − γ) 2 \displaystyle\sum_{\rho}\dfrac{\alpha-{\rm Re}\,{\rho}}{(\alpha-{\rm Re}\,{\rho})^{2}+(t-\gamma)^{2}} | = Re ​ ζ ′ ζ ​ ( s) + 1 2 ​ Re ​ Γ ′ Γ ​ ( s 2 + 1) − log ⁡ π 2 + α − 1 ( α − 1) 2 + t 2. \displaystyle={\rm Re}\,\dfrac{\zeta^{\prime}}{\zeta}(s)+\dfrac{1}{2}\,{\rm Re}\,\dfrac{\Gamma^{\prime}}{\Gamma}\bigg(\dfrac{s}{2}+1\bigg)-\dfrac{\log\pi}{2}+\dfrac{\alpha-1}{(\alpha-1)^{2}+t^{2}}. |  | (2.4) |

Using the inequality Re ​ Γ ′ Γ ​ ( z) ≤ log ⁡ | z | {\rm Re}\,\frac{\Gamma^{\prime}}{\Gamma}(z)\leq\log|z| for Re ​ z ≥ 1 4 {\rm Re}\,{z}\geq\frac{1}{4} (see [4, Lemma 2.3]), it follows that for α ≥ 0 \alpha\geq 0 and t ≠ 0 t\neq 0

 | Re ​ Γ ′ Γ ​ ( α 2 + 1 + i ​ t 2) ≤ log ⁡ | t | − log ⁡ 2 + ( α + 2) 2 2 ​ t 2. \displaystyle{\rm Re}\,\dfrac{\Gamma^{\prime}}{\Gamma}\bigg(\dfrac{\alpha}{2}+1+\dfrac{it}{2}\bigg)\leq\log|t|-\log 2+\frac{(\alpha+2)^{2}}{2t^{2}}. |  |

Since RH holds, combining this and ( 2.4) we get

 | ∑ ρ α − 1 2 ( α − 1 2) 2 + ( t − γ) 2 \displaystyle\sum_{\rho}\dfrac{\alpha-\tfrac{1}{2}}{(\alpha-\tfrac{1}{2})^{2}+(t-\gamma)^{2}} | ≤ Re ​ ζ ′ ζ ​ ( s) + log ⁡ | t | 2 − log ⁡ 2 ​ π 2 + ( α + 2) 2 4 ​ t 2 + α − 1 ( α − 1) 2 + t 2. \displaystyle\leq{\rm Re}\,\dfrac{\zeta^{\prime}}{\zeta}(s)+\frac{\log|t|}{2}-\dfrac{\log 2\pi}{2}+\frac{(\alpha+2)^{2}}{4t^{2}}+\dfrac{\alpha-1}{(\alpha-1)^{2}+t^{2}}. |  | (2.5) |

To prove ( 2.2), we let α = 6 + 1 2 \alpha=\sqrt{6}+\tfrac{1}{2} in ( 2.5) and using the fact that | ζ ′ ζ ​ ( 6 + 1 2 + i ​ t) | ≤ | ζ ′ ζ ​ ( 6 + 1 2) | = 0.1738 ​ … |\frac{\zeta^{\prime}}{\zeta}(\sqrt{6}+\frac{1}{2}+it)|\leq|\frac{\zeta^{\prime}}{\zeta}(\sqrt{6}+\frac{1}{2})|=0.1738\ldots, and | t | ≥ 4 |t|\geq 4 we conclude. To prove ( 2.3), we let α = 1 \alpha=1 in ( 2.5) and using that | t | ≥ 100 |t|\geq 100 we obtain

 | ∑ γ 1 1 4 + ( t − γ) 2 ≤ 2 ​ Re ​ ζ ′ ζ ​ ( 1 + i ​ t) + log ⁡ | t | ≤ 2 ​ | ζ ′ ζ ​ ( 1 + i ​ t) | + log ⁡ | t | \displaystyle\sum_{\gamma}\dfrac{1}{\frac{1}{4}+(t-\gamma)^{2}}\leq 2\,{\rm Re}\,\dfrac{\zeta^{\prime}}{\zeta}(1+it)+{\log|t|}\leq 2\left|\dfrac{\zeta^{\prime}}{\zeta}(1+it)\right|+{\log|t|} |  |

Using Lemma 2.1 with σ = 1 \sigma=1 we conclude. ∎

Throughout the paper, we will encounter situations where we aim to compute the integral of | f + g | 2 |f+g|^{2}, where the L 2 L^{2} -norm of f f and g g by themselves are much easier to compute. To make this passage we shall use the following inequality: for any η > 0 \eta>0

 | ∫ a b | f ⁡ ( x) + g ⁡ ( x) | 2 ​ d ​ x ≤ ( 1 + η) ​ ∫ a b | f ⁡ ( x) | 2 ​ d ​ x + ( 1 + 1 η) ​ ∫ a b | g ⁡ ( x) | 2 ​ d ​ x, \displaystyle\int_{a}^{b}|f(x)+g(x)|^{2}\text{\rm d}x\leq(1+\eta)\int_{a}^{b}|f(x)|^{2}\text{\rm d}x+\left(1+\dfrac{1}{\eta}\right)\int_{a}^{b}|g(x)|^{2}\text{\rm d}x, |  | (2.6) |

which is an immediate consequence of the inequality ( x ​ η − y η) 2 ≥ 0 (x\sqrt{\eta}-\frac{y}{\sqrt{\eta}})^{2}\geq 0.

###### Lemma 2.3.

Assume RH. Then, for T ≥ 4 ⋅ 10 13 T\geq 4\cdot 10^{13} we have

 | ∫ 10 4 T | ζ ′ ζ ​ ( 1 + i ​ t) | 2 ​ d ​ t ≤ 0.8056 ⋅ T. \int_{10^{4}}^{T}\left|\dfrac{\zeta^{\prime}}{\zeta}(1+it)\right|^{2}\!\!\text{\rm d}t\leq 0.8056\cdot T. |  |

###### Proof.

Given x, y ≥ 2 x,y\geq 2 and s = 1 + i ​ t s=1+it with t ≥ 10 4 t\geq 10^{4}, the unconditional formula [15, Eq. (13.35)] states that

 | ζ ′ ζ ( s) = − ∑ ρ ( x ​ y) ρ − s − x ρ − s ( ρ − s) 2 ​ log ⁡ y − ∑ k = 1 ∞ ( x ​ y) − 2 ​ k − s − x − 2 ​ k − s ( 2 ​ k + s) 2 ​ log ⁡ y + ( x ​ y) 1 − s − x 1 − s ( 1 − s) 2 ​ log ⁡ y − ∑ n ≤ x ​ y Λ ⁡ ( n) n s w ( n), \displaystyle\dfrac{\zeta^{\prime}}{\zeta}(s)=-\sum_{\rho}\dfrac{(xy)^{\rho-s}-x^{\rho-s}}{(\rho-s)^{2}\log y}-\sum_{k=1}^{\infty}\dfrac{(xy)^{-2k-s}-x^{-2k-s}}{(2k+s)^{2}\log y}+\dfrac{(xy)^{1-s}-x^{1-s}}{(1-s)^{2}\log y}-\sum_{n\leq xy}\dfrac{\Lambda(n)}{n^{s}}w(n), |  | (2.7) |

where w ⁡ ( n) w(n) is a function that satisfies 0 ≤ w ⁡ ( n) ≤ 1 0\leq w(n)\leq 1. Let us bound each term on the right-hand side of ( 2.7). Since RH holds,

 | | ∑ ρ ( x ​ y) ρ − s − x ρ − s ( ρ − s) 2 ​ log ⁡ y | \displaystyle\left|\sum_{\rho}\dfrac{(xy)^{\rho-s}-x^{\rho-s}}{(\rho-s)^{2}\log y}\right| | = | ∑ γ ( x ​ y) 1 2 + i ​ γ − s − x 1 2 + i ​ γ − s ( 1 2 + i ​ γ − s) 2 ​ log ⁡ y | ≤ x − 1 2 ​ ( y − 1 2 + 1) log ⁡ y ​ ∑ γ 1 1 4 + ( t − γ) 2. \displaystyle=\left|\sum_{\gamma}\dfrac{(xy)^{\frac{1}{2}+i\gamma-s}-x^{\frac{1}{2}+i\gamma-s}}{(\frac{1}{2}+i\gamma-s)^{2}\log y}\right|\leq\dfrac{x^{-\frac{1}{2}}(y^{-\frac{1}{2}}+1)}{\log y}\sum_{\gamma}\dfrac{1}{\frac{1}{4}+(t-\gamma)^{2}}. |  |

Thus, by Lemma 2.2 we arrive at

 | | ∑ ρ ( x ​ y) ρ − s − x ρ − s ( ρ − s) 2 ​ log ⁡ y | ≤ ( 9 ​ x − 1 2 ​ ( y − 1 2 + 1) log ⁡ y) ​ log ⁡ t:= c x, y ​ log ⁡ t. \left|\sum_{\rho}\dfrac{(xy)^{\rho-s}-x^{\rho-s}}{(\rho-s)^{2}\log y}\right|\leq\left(\dfrac{9x^{-\frac{1}{2}}(y^{-\frac{1}{2}}+1)}{\log y}\right)\log t:=c_{x,y}\,\log t. |  |

We estimate the next terms in ( 2.7) trivially as follows

 | | ∑ k = 1 ∞ ( x ​ y) − 2 ​ k − s − x − 2 ​ k − s ( 2 ​ k + s) 2 ​ log ⁡ y | ≤ 0.3 t 2, and | ( x ​ y) 1 − s − x 1 − s ( 1 − s) 2 ​ log ⁡ y | ≤ 2.9 t 2. \displaystyle\Bigg|\sum_{k=1}^{\infty}\dfrac{(xy)^{-2k-s}-x^{-2k-s}}{(2k+s)^{2}\log y}\Bigg|\leq\dfrac{0.3}{t^{2}},\,\,\,\,\,\,\,\,\,\,\,\mbox{and}\,\,\,\,\,\,\,\,\,\,\,\,\Bigg|\dfrac{(xy)^{1-s}-x^{1-s}}{(1-s)^{2}\log y}\Bigg|\leq\dfrac{2.9}{t^{2}}. |  |

Inserting these bounds in ( 2.7) we arrive at

 | ζ ′ ζ ​ ( 1 + i ​ t) = \displaystyle\dfrac{\zeta^{\prime}}{\zeta}(1+it)= | − ∑ n ≤ x ​ y Λ ⁡ ( n) n 1 + i ​ t w ( n) + O ∗ ( c x, y log t + 3.2 t 2). \displaystyle-\sum_{n\leq xy}\dfrac{\Lambda(n)}{n^{1+it}}w(n)+O^{*}\left(c_{x,y}\log t+\dfrac{3.2}{t^{2}}\right). |  |

for t ≥ 10 4 t\geq 10^{4}. Now, we integrate from 10 4 10^{4} to T T (with 10 4 ≤ T 0 ≤ T 10^{4}\leq T_{0}\leq T), and by ( 2.6), for any η > 0 \eta>0:

 | ∫ 10 4 T | ζ ′ ζ ​ ( 1 + i ​ t) | 2 ​ d ​ t \displaystyle\int_{10^{4}}^{T}\left|\dfrac{\zeta^{\prime}}{\zeta}(1+it)\right|^{2}\!\!\text{\rm d}t | ≤ ( 1 + η) ​ ∫ 10 4 T | ∑ n ≤ x ​ y Λ ⁡ ( n) n 1 + i ​ t ​ w ​ ( n) | 2 ​ d ​ t + ( 1 + 1 η) ​ O ∗ ​ ( ∫ 10 4 T | c x, y ​ log ⁡ t + 3.2 t 2 | 2 ​ d ​ t). \displaystyle\leq(1+\eta)\int_{10^{4}}^{T}\left|\sum_{n\leq xy}\dfrac{\Lambda(n)}{n^{1+it}}w(n)\right|^{2}\!\!\text{\rm d}t+\left(1+\dfrac{1}{\eta}\right)O^{*}\left(\int_{10^{4}}^{T}\left|c_{x,y}\log t+\frac{3.2}{t^{2}}\right|^{2}\!\!\text{\rm d}t\right). |  | (2.8) |

Applying the explicit mean value theorem in [6, Proposition 2.11], we get

 | ∫ 10 4 T | ∑ n ≤ x ​ y Λ ⁡ ( n) n 1 + i ​ t ​ w ​ ( n) | 2 ​ d ​ t ≤ ( T − 10 4 + 4.133) ​ ∑ n ≤ x ​ y ( Λ ⁡ ( n) n ​ w ​ ( n)) 2 + 8.265 ​ ∑ n ≤ x ​ y n ​ ( Λ ⁡ ( n) n ​ w ​ ( n)) 2. \int_{10^{4}}^{T}\left|\sum_{n\leq xy}\dfrac{\Lambda(n)}{n^{1+it}}w(n)\right|^{2}\text{\rm d}t\leq\left(T-10^{4}+4.133\right)\sum_{n\leq xy}\left(\dfrac{\Lambda(n)}{n}w(n)\right)^{2}+8.265\sum_{n\leq xy}n\left(\dfrac{\Lambda(n)}{n}w(n)\right)^{2}. |  |

Since | w ⁡ ( n) | ≤ 1 |w(n)|\leq 1, by (2) in Lemma A.1, the first sum is bounded by 0.8053 0.8053, and the second sum is bounded by ∑ n ≤ x ​ y Λ 2 ​ ( n) n \sum_{n\leq xy}\frac{\Lambda^{2}(n)}{n}. Thus, writing x ​ y = e α xy=e^{\alpha}, by Lemma A.2 we conclude that

 | ∫ 10 4 T | ∑ n ≤ x ​ y Λ ⁡ ( n) n 1 + i ​ t ​ w ​ ( n) | 2 ​ d ​ t ≤ 0.8053 ​ T + 4.1325 ​ α 2 − 8 ⋅ 10 3. \displaystyle\int_{10^{4}}^{T}\left|\sum_{n\leq xy}\dfrac{\Lambda(n)}{n^{1+it}}w(n)\right|^{2}\text{\rm d}t\leq 0.8053\,T+4.1325\,\alpha^{2}-8\cdot 10^{3}. |  | (2.9) |

Moreover

 | ∫ 10 4 T | c x, y ​ log ⁡ t + 3.2 t 2 | 2 ​ d ​ t \displaystyle\int_{10^{4}}^{T}\left|c_{x,y}\log t+\frac{3.2}{t^{2}}\right|^{2}\!\!\text{\rm d}t | ≤ 2 ​ ∫ 10 4 T | c x, y ​ log ⁡ t | 2 ​ d ​ t + 2 ​ ∫ 10 4 T | 3.2 t 2 | 2 ​ d ​ t < 2 ​ ( c x, y) 2 ​ T ​ log 2 ​ T + 7 ⋅ 10 − 12. \displaystyle\leq 2\int_{10^{4}}^{T}|c_{x,y}\log t|^{2}\text{\rm d}t+2\int_{10^{4}}^{T}\left|\frac{3.2}{t^{2}}\right|^{2}\!\!\text{\rm d}t<2(c_{x,y})^{2}T\log^{2}T+7\cdot 10^{-12}. |  | (2.10) |

Letting y = e 2 ​ λ y=e^{2\lambda}, with λ ≥ ( log ⁡ 2) / 2 \lambda\geq(\log 2)/2, note that

 | ( 1 + η) ​ 4.1325 ​ α 2 + ( 1 + 1 η) ​ 2 ​ ( c x, y) 2 ​ T ​ log 2 ​ T = 4.1325 ​ ( 1 + η) ​ α 2 + 40.5 ​ ( 1 + 1 η) ​ ( 1 + e λ λ) 2 ​ T ​ log 2 ​ T e α. \displaystyle(1+\eta)4.1325\,\alpha^{2}+\left(1+\dfrac{1}{\eta}\right)2(c_{x,y})^{2}T\log^{2}T={4.1325\left(1+{\eta}\right)\alpha^{2}}+40.5\left(1+\dfrac{1}{\eta}\right)\left(\dfrac{1+e^{\lambda}}{\lambda}\right)^{2}\dfrac{T\log^{2}T}{e^{\alpha}}. |  |

In order to reduce the contribution from the above expression, we choose λ = 1.278 \lambda=1.278, and α = log ⁡ T \alpha=\log T. Then, inserting ( 2.9) and ( 2.10) in ( 2.8) we get

 | ∫ 10 4 T | ζ ′ ζ ​ ( 1 + i ​ t) | 2 ​ d ​ t \displaystyle\int_{10^{4}}^{T}\left|\dfrac{\zeta^{\prime}}{\zeta}(1+it)\right|^{2}\!\!\text{\rm d}t | ≤ ( 1 + η) ​ 0.8053 ​ T + ( 4.1325 ​ ( 1 + η) + 522.295 ​ ( 1 + 1 η)) ​ log 2 ​ T + κ n, \displaystyle\leq(1+\eta)0.8053T+\left({4.1325\left(1+{\eta}\right)}+522.295\left(1+\dfrac{1}{\eta}\right)\right)\log^{2}T+\kappa_{n}, |  |

where κ n = − ( 1 + η) 8 ⋅ 10 3 + ( 1 + η − 1) 7 ⋅ 10 − 12 \kappa_{n}=-(1+\eta)8\cdot 10^{3}+(1+{\eta^{-1}})7\cdot 10^{-12}. Finally, choosing η = 10 − 4 \eta=10^{-4}, using κ n < 0 \kappa_{n}<0, and T ≥ 4 ⋅ 10 13 T\geq 4\cdot 10^{13}, the proof is done. ∎

###### Lemma 2.4.

For 0 < t ≤ 1 2 0<t\leq\frac{1}{2} we have the unconditional bound

 | | ζ ′ ζ ​ ( 1 + i ​ t) + 1 i ​ t | ≤ 2.635. \displaystyle\left|\frac{\zeta^{\prime}}{\zeta}(1+it)+\frac{1}{it}\right|\leq 2.635. |  |

###### Proof.

By the Laurent expansion

 | ζ ⁡ ( s) = 1 s − 1 + ∑ n = 0 ∞ ( − 1) n ​ γ n n! ​ ( s − 1) n, \displaystyle\zeta(s)=\frac{1}{s-1}+\sum_{n=0}^{\infty}\frac{(-1)^{n}\gamma_{n}}{n!}(s-1)^{n}, |  | (2.11) |

together with the bound | γ n | ≤ 4 ​ ( n − 1)! / π n |\gamma_{n}|\leq{4(n-1)!}/{\pi^{n}} for all n ≥ 2 n\geq 2 even, and | γ n | ≤ 2 ​ ( n − 1)! / π n |\gamma_{n}|\leq{2(n-1)!}/{\pi^{n}} for all n ≥ 1 n\geq 1 odd (see [2]), we have for 0 < t ≤ 1 2 0<t\leq\frac{1}{2} (letting s = 1 + i ​ t s=1+it),

 | | ζ ⁡ ( 1 + i ​ t) − 1 i ​ t | \displaystyle\left|\zeta(1+it)-\dfrac{1}{it}\right| | ≤ | γ 0 | + ∑ n ​ e ​ v ​ e ​ n n ≥ 2 | γ n | n! ​ t n + ∑ n ​ o ​ d ​ d n ≥ 1 | γ n | n! ​ t n < 0.578 + 2 ​ ∑ n = 1 ∞ 1 n ​ ( 2 ​ π) n + 2 ​ ∑ n ​ e ​ v ​ e ​ n n ≥ 2 1 n ​ ( 2 ​ π) n \displaystyle\leq|\gamma_{0}|+\sum_{\begin{subarray}{c}n\,even\\ n\geq 2\end{subarray}}\dfrac{|\gamma_{n}|}{n!}t^{n}+\sum_{\begin{subarray}{c}n\,odd\\ n\geq 1\end{subarray}}\dfrac{|\gamma_{n}|}{n!}t^{n}<0.578+2\sum_{n=1}^{\infty}\dfrac{1}{n(2\pi)^{n}}+2\sum_{\begin{subarray}{c}n\,even\\ n\geq 2\end{subarray}}\dfrac{1}{n(2\pi)^{n}} |  |

 |  | = 0.578 − 2 ​ log ⁡ ( 1 − 1 2 ​ π) − log ⁡ ( 1 − 1 4 ​ π 2) < 0.951. \displaystyle=0.578-2\log\left(1-\dfrac{1}{2\pi}\right)-\log\left(1-\dfrac{1}{4\pi^{2}}\right)<0.951. |  |

Moreover, differentiating ( 2.11), we bound similarly as before to get

 | | ζ ′ ​ ( 1 + i ​ t) − 1 t 2 | ≤ 4 ​ ∑ n = 1 ∞ 1 ( 2 ​ π) n + 4 ​ ∑ n ​ e ​ v ​ e ​ n n ≥ 2 1 ( 2 ​ π) n = 4 2 ​ π − 1 + 4 4 ​ π 2 − 1 < 0.862. \left|\zeta^{\prime}(1+it)-\dfrac{1}{t^{2}}\right|\leq 4\sum_{n=1}^{\infty}\dfrac{1}{(2\pi)^{n}}+4\sum_{\begin{subarray}{c}n\,even\\ n\geq 2\end{subarray}}\dfrac{1}{(2\pi)^{n}}=\dfrac{4}{2\pi-1}+\dfrac{4}{4\pi^{2}-1}<0.862. |  |

Thus

 | ζ ′ ζ ​ ( 1 + i ​ t) + 1 i ​ t = 1 / t 2 + O ∗ ​ ( 0.862) 1 / i ​ t + O ∗ ​ ( 0.951) + 1 i ​ t = O ∗ ​ ( 0.862 ​ t) + O ∗ ​ ( 0.951) 1 + O ∗ ​ ( 0.951 ​ t). \displaystyle\frac{\zeta^{\prime}}{\zeta}(1+it)+\frac{1}{it}=\dfrac{1/t^{2}+O^{*}(0.862)}{1/it+O^{*}(0.951)}+\dfrac{1}{it}=\dfrac{O^{*}(0.862t)+O^{*}(0.951)}{1+O^{*}(0.951t)}. |  |

Therefore, for 0 < t ≤ 1 2 0<t\leq\frac{1}{2}:

 | | ζ ′ ζ ​ ( 1 + i ​ t) + 1 i ​ t | ≤ 0.862 / 2 + 0.951 1 − 0.951 / 2 ≤ 2.635. \displaystyle\left|\frac{\zeta^{\prime}}{\zeta}(1+it)+\frac{1}{it}\right|\leq\dfrac{0.862/2+0.951}{1-0.951/2}\leq 2.635. |  |

∎

###### Lemma 2.5.

For any 0 < δ ≤ 1 0<\delta\leq 1 and any t ≠ 0 t\neq 0 we have the bound

 | | ( 1 + δ) 1 2 + i ​ t − 1 1 2 + i ​ t | ≤ min ⁡ { δ, ℓ | t | }, \left|\dfrac{(1+\delta)^{\frac{1}{2}+it}-1}{\frac{1}{2}+it}\right|\leq\min\bigg\{\delta,\dfrac{\ell}{|t|}\bigg\}, |  |

where ℓ = 1 + δ + 1 \ell=\sqrt{1+\delta}+1. In particular, assuming RH,

 | | ( 1 + δ) ρ − 1 ρ | ≤ min ⁡ { δ, ℓ | γ | }, \left|\dfrac{(1+\delta)^{\rho}-1}{\rho}\right|\leq\min\bigg\{\delta,\dfrac{\ell}{|\gamma|}\bigg\}, |  |

for any non-trivial zero ρ \rho.

###### Proof.

Clearly

 | | ( 1 + δ) 1 2 + i ​ t − 1 1 2 + i ​ t | = | ∫ 1 1 + δ x − 1 2 + i ​ t ​ d ​ x | ≤ ∫ 1 1 + δ x − 1 2 ​ d ​ x ≤ δ. \left|\dfrac{(1+\delta)^{\frac{1}{2}+it}-1}{\frac{1}{2}+it}\right|=\left|\int_{1}^{1+\delta}x^{-\frac{1}{2}+it}\text{\rm d}x\right|\leq\int_{1}^{1+\delta}x^{-\frac{1}{2}}\text{\rm d}x\leq\delta. |  |

On the other hand we also have,

 | | ( 1 + δ) 1 2 + i ​ t − 1 1 2 + i ​ t | = | e ( 1 2 + i ​ t) ​ log ⁡ ( 1 + δ) − 1 1 2 + i ​ t | ≤ e 1 2 ​ log ⁡ ( 1 + δ) + 1 | t | = 1 + δ + 1 | t |, \left|\dfrac{(1+\delta)^{\frac{1}{2}+it}-1}{\frac{1}{2}+it}\right|=\left|\dfrac{e^{(\frac{1}{2}+it)\log(1+\delta)}-1}{\frac{1}{2}+it}\right|\leq\dfrac{e^{\frac{1}{2}{\log(1+\delta)}}+1}{|t|}=\dfrac{\sqrt{1+\delta}+1}{|t|}, |  |

which gives the desired conclusion. ∎

###### Lemma 2.6.

We have the following estimates for T ≥ 10 13 T\geq 10^{13}:

 | ∑ 0 < γ ≤ T log ⁡ γ ≤ 1 2 ​ π ⋅ T ​ log 2 ​ T, and ∑ γ > T log ⁡ γ γ 2 ≤ 1.028 2 ​ π ⋅ log 2 ⁡ T T, \sum_{0<\gamma\leq T}\log\gamma\leq\dfrac{1}{2\pi}\cdot T\log^{2}T,\,\,\,\,\,\,\,\,\mbox{and}\,\,\,\,\,\,\,\,\,\sum_{\gamma>T}\dfrac{\log\gamma}{\gamma^{2}}\leq\dfrac{1.028}{2\pi}\cdot\dfrac{\log^{2}T}{T}, |  |

where the sums run over the imaginary parts γ \gamma of the non-trivial zeros of ζ ⁡ ( s) \zeta(s).

###### Proof.

To prove the first estimate, we apply [3, Lemma 3] with ϕ ⁡ ( t) = log ⁡ t \phi(t)=\log t, T 1 = 2 ​ π ​ e T_{1}=2\pi e, T 2 = T T_{2}=T, A = 0.28 A=0.28, to get

 | ∑ 2 ​ π ​ e < γ ≤ T log ⁡ γ ≤ 1 2 ​ π ​ ∫ 2 ​ π ​ e T log ⁡ t ​ log ⁡ ( t 2 ​ π) ​ d ​ t + 0.56 ​ log 2 ​ T + 0.28 ​ ∫ 2 ​ π ​ e T log ⁡ t t ​ d ​ t. \sum_{2\pi e<\gamma\leq T}\log\gamma\leq\dfrac{1}{2\pi}\int_{2\pi e}^{T}\log t\log\left(\dfrac{t}{2\pi}\right)\text{\rm d}t+0.56\log^{2}T+0.28\int_{2\pi e}^{T}\dfrac{\log t}{t}\text{\rm d}t. |  |

Making the computations, using the facts that T ≥ 10 13 T\geq 10^{13}, γ 1 = 14.1347 ​ … \gamma_{1}=14.1347\ldots and γ 2 = 21.0220 ​ … \gamma_{2}=21.0220\ldots we conclude. To prove the second estimate, we apply [3, Lemma 5 and Lemma 6] to get

 | ∑ γ > T log ⁡ γ γ 2 ≤ 1 2 ​ π ​ ( log 2 ⁡ T T + ln ⁡ ( 2 ​ π / e) ​ log ⁡ T T). \sum_{\gamma>T}\dfrac{\log\gamma}{\gamma^{2}}\leq\dfrac{1}{2\pi}\left(\dfrac{\log^{2}T}{T}+\dfrac{\ln(2\pi/e)\log T}{T}\right). |  |

This implies the desired result. ∎

## 3. An explicit bound for J ψ ​ ( x, δ) J_{\psi}(x,\delta)

To derive an explicit bound for J θ ​ ( x, δ) J_{\theta}(x,\delta), we begin by estimating the integral defined in ( 1.2), employing the averaging technique introduced by Saffari and Vaughan in [17].

###### Theorem 2.

Assume RH. Then, for x ≥ 10 13 x\geq 10^{13} and δ ∈ ( 0, 10 − 13] \delta\in(0,10^{-13}] we have that

 | J ψ ​ ( x, δ) ≤ 2.2258 ⋅ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2. \displaystyle J_{\psi}(x,\delta)\leq 2.2258\cdot\delta\,\log^{2}\left(\dfrac{2.0001}{\delta}\right)x^{2}. |  |

###### Proof.

Let λ > 1 \lambda>1 and κ > 1 \kappa>1 be two parameters to be chosen later. For any x > 0 x>0, note that [x, κ ​ x] ⊂ [x ​ ν / λ, κ ​ x ​ ν] [x,\kappa x]\subset[x\nu/\lambda,\kappa x\nu] for 1 ≤ ν ≤ λ 1\leq\nu\leq\lambda. This implies that

 | ∫ x κ ​ x ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y) 2 ​ d ​ y ≤ 1 ( λ − 1) ​ ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y) 2 ​ d ​ y) ​ d ​ ν. \displaystyle\int_{x}^{\kappa x}\big(\psi((1+\delta)y)-\psi(y)-\delta y\big)^{2}\text{\rm d}y\leq\dfrac{1}{(\lambda-1)}\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\big(\psi((1+\delta)y)-\psi(y)-\delta y\big)^{2}\text{\rm d}y\right)\text{\rm d}\nu. |  | (3.1) |

Let us concentrate on bounding the double integral on the right-hand side of ( 3.1). For all y > 0 y>0, y ∉ ℤ y\notin\mathbb{Z} we have the explicit formula [15, Eq. (12.1)] given by

 | ψ ⁡ ( y) = y − lim T → ∞ ∑ | γ | ≤ T y ρ ρ − ζ ′ ​ ( 0) ζ ⁡ ( 0) − 1 2 ​ log ⁡ ( 1 − y − 2). \displaystyle\psi(y)=y-\lim_{T\to\infty}\sum_{|\gamma|\leq T}\dfrac{y^{\rho}}{\rho}-\dfrac{\zeta^{\prime}(0)}{\zeta(0)}-\dfrac{1}{2}\log(1-y^{-2}). |  | (3.2) |

We write ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y = A δ ​ ( y) + B δ ​ ( y) \psi((1+\delta)y)-\psi(y)-\delta y=A_{\delta}(y)+B_{\delta}(y), where

 | A δ ( y) = − lim T → ∞ ∑ | γ | ≤ T ( 1 + δ) ρ − 1 ρ y ρ, and B δ ( y) = − 1 2 ( log ( 1 − ( ( 1 + δ) y) − 2) − log ( 1 − y − 2)). \,\,\,\,\,\,\,\,\,\,\,\,A_{\delta}(y)=-\lim_{T\to\infty}\displaystyle\sum_{|\gamma|\leq T}\dfrac{(1+\delta)^{\rho}-1}{\rho}y^{\rho},\,\,\,\,\,\,\,\,\,\mbox{and}\,\,\,\,\,\,\,\,\,B_{\delta}(y)=-\dfrac{1}{2}\left(\log(1-((1+\delta)y)^{-2})-\log(1-y^{-2})\right). |  |

By 2.6 we see that

 | ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y) 2 ​ d ​ y) ​ d ​ ν ≤ ( 1 + η) ​ ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | A δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν + ( 1 + 1 η) ​ ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | B δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν. \displaystyle\begin{split}\int_{1}^{\lambda}&\left(\int_{x\nu/\lambda}^{\kappa x\nu}\big(\psi((1+\delta)y)-\psi(y)-\delta y\big)^{2}\text{\rm d}y\right)\text{\rm d}\nu\\ &\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\leq(1+\eta)\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|A_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu+\left(1+\dfrac{1}{\eta}\right)\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|B_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu.\end{split} |  | (3.3) |

Let us analyze the double integral of A δ ​ ( y) A_{\delta}(y) in the above expression. Since RH holds, we write ρ 1 = 1 2 + i ​ γ 1 \rho_{1}=\tfrac{1}{2}+i\gamma_{1} and ρ 2 = 1 2 + i ​ γ 2 \rho_{2}=\tfrac{1}{2}+i\gamma_{2}. Clearly

 | ∫ x ​ ν / λ κ ​ x ​ ν | A δ ​ ( y) | 2 ​ d ​ y = ∑ ρ 1 ∑ ρ 2 ( ( 1 + δ) ρ 1 − 1 ρ 1) ​ ( ( 1 + δ) ρ 2 ¯ − 1 ρ 2 ¯) ​ ( κ 1 + ρ 1 + ρ 2 ¯ − ( 1 / λ) 1 + ρ 1 + ρ 2 ¯ 1 + ρ 1 + ρ 2 ¯) ​ ( x ​ ν) 1 + ρ 1 + ρ 2 ¯, \displaystyle\int_{x\nu/\lambda}^{\kappa x\nu}\left|A_{\delta}(y)\right|^{2}\text{\rm d}y=\sum_{\rho_{1}}\sum_{\rho_{2}}\bigg(\dfrac{(1+\delta)^{\rho_{1}}-1}{\rho_{1}}\bigg)\bigg(\dfrac{(1+\delta)^{\overline{\rho_{2}}}-1}{{\overline{\rho_{2}}}}\bigg)\bigg(\dfrac{\kappa^{1+\rho_{1}+\overline{\rho_{2}}}-(1/\lambda)^{1+\rho_{1}+\overline{\rho_{2}}}}{1+\rho_{1}+\overline{\rho_{2}}}\bigg)(x\nu)^{1+\rho_{1}+\overline{\rho_{2}}}, |  |

by dominated convergence theorem, since the double sum

 | ∑ γ 1 ∑ γ 2 1 | γ 1 | ​ 1 | γ 2 | ​ 1 2 + | γ 1 − γ 2 | \sum_{\gamma_{1}}\sum_{\gamma_{2}}\dfrac{1}{|\gamma_{1}|}\dfrac{1}{|\gamma_{2}|}\dfrac{1}{2+|\gamma_{1}-\gamma_{2}|} |  |

is bounded (Lemma 2.5 and [3, Eq. (9)]). Now, integrating over ν \nu we have that

 |  | ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | A δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν \displaystyle\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|A_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu |  |

 |  | = ∑ ρ 1 ∑ ρ 2 ( ( 1 + δ) ρ 1 − 1 ρ 1) ​ ( ( 1 + δ) ρ 2 ¯ − 1 ρ 2 ¯) ​ ( κ 1 + ρ 1 + ρ 2 ¯ − ( 1 / λ) 1 + ρ 1 + ρ 2 ¯ 1 + ρ 1 + ρ 2 ¯) ​ ( λ 2 + ρ 1 + ρ 2 ¯ − 1 2 + ρ 1 + ρ 2 ¯) ​ x 1 + ρ 1 + ρ 2 ¯. \displaystyle=\sum_{\rho_{1}}\sum_{\rho_{2}}\bigg(\dfrac{(1+\delta)^{\rho_{1}}-1}{\rho_{1}}\bigg)\bigg(\dfrac{(1+\delta)^{\overline{\rho_{2}}}-1}{{\overline{\rho_{2}}}}\bigg)\bigg(\dfrac{\kappa^{1+\rho_{1}+\overline{\rho_{2}}}-(1/\lambda)^{1+\rho_{1}+\overline{\rho_{2}}}}{1+\rho_{1}+\overline{\rho_{2}}}\bigg)\bigg(\dfrac{\lambda^{2+\rho_{1}+\overline{\rho_{2}}}-1}{2+\rho_{1}+\overline{\rho_{2}}}\bigg)x^{1+\rho_{1}+\overline{\rho_{2}}}. |  |

Note that | 1 + ρ 1 + ρ 2 ¯ | ​ | 2 + ρ 1 + ρ 2 ¯ | = 6 2 + 13 ​ ( γ 1 − γ 2) 2 + ( γ 1 − γ 2) 4 ≥ 6 + ( γ 1 − γ 2) 2 |1+\rho_{1}+\overline{\rho_{2}}||2+\rho_{1}+\overline{\rho_{2}}|=\sqrt{6^{2}+13(\gamma_{1}-\gamma_{2})^{2}+(\gamma_{1}-\gamma_{2})^{4}}\geq 6+(\gamma_{1}-\gamma_{2})^{2}. We then use Lemma 2.5, RH and the estimate 2 ​ | a ​ b | ≤ | a | 2 + | b | 2 2|ab|\leq|a|^{2}+|b|^{2} to conclude that

 | ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | A δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν \displaystyle\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|A_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu | ≤ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ ∑ γ 1 ∑ γ 2 min ⁡ { δ, ℓ | γ 1 | } ​ min ​ { δ, ℓ | γ 2 | } ​ 1 6 + ( γ 1 − γ 2) 2 ​ x 2 \displaystyle\leq\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\displaystyle\sum_{\gamma_{1}}\displaystyle\sum_{\gamma_{2}}\min\bigg\{\delta,\dfrac{\ell}{|\gamma_{1}|}\bigg\}\min\bigg\{\delta,\dfrac{\ell}{|\gamma_{2}|}\bigg\}\dfrac{1}{6+(\gamma_{1}-\gamma_{2})^{2}}\,x^{2} |  |

 |  | ≤ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ ∑ γ 1 min ⁡ { δ 2, ℓ 2 | γ 1 | 2 } ​ ( ∑ γ 2 1 6 + ( γ 1 − γ 2) 2) ​ x 2. \displaystyle\leq\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\displaystyle\sum_{\gamma_{1}}\min\bigg\{\delta^{2},\dfrac{\ell^{2}}{|\gamma_{1}|^{2}}\bigg\}\displaystyle\left(\sum_{\gamma_{2}}\dfrac{1}{6+(\gamma_{1}-\gamma_{2})^{2}}\right)x^{2}. |  |

Using that | γ | > 14 |\gamma|>14, Lemma 2.2 and the symmetry of the zeros we have that

 | ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | A δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν \displaystyle\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|A_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu | ≤ 1 2 ​ 6 ​ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ ∑ γ min ⁡ { δ 2, ℓ 2 | γ | 2 } ​ log ​ | γ | ​ x 2 \displaystyle\leq\frac{1}{2\sqrt{6}}\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\displaystyle\sum_{\gamma}\min\bigg\{\delta^{2},\dfrac{\ell^{2}}{|\gamma|^{2}}\bigg\}\log|\gamma|x^{2} |  |

 |  | = 1 6 ​ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ ( ∑ γ > 0 min ⁡ { δ 2, ℓ 2 γ 2 } ​ log ⁡ γ) ​ x 2 \displaystyle=\frac{1}{\sqrt{6}}\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\left(\displaystyle\sum_{\gamma>0}\min\bigg\{\delta^{2},\dfrac{\ell^{2}}{\gamma^{2}}\bigg\}\log\gamma\right)x^{2} |  |

 |  | = 1 6 ​ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ ( δ 2 ​ ∑ 0 < γ ≤ ℓ / δ log ⁡ γ + ℓ 2 ​ ∑ γ > ℓ / δ log ⁡ γ γ 2) ​ x 2. \displaystyle=\frac{1}{\sqrt{6}}\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\left(\delta^{2}\displaystyle\sum_{0<\gamma\leq\ell/\delta}\log\gamma+\ell^{2}\displaystyle\sum_{\gamma>\ell/\delta}\dfrac{\log\gamma}{{\gamma^{2}}}\right)x^{2}. |  |

Since 0 < δ ≤ 10 − 13 0<\delta\leq 10^{-13} we see that ℓ / δ ≥ 2 ⋅ 10 13 \ell/\delta\geq 2\cdot 10^{13}. Applying Lemma 2.6 we arrive at

 | ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | A δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν ≤ 2.028 2 ​ 6 ​ π ​ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ δ ​ ℓ ​ log 2 ⁡ ( ℓ δ) ​ x 2 < 2.0282 6 ​ π ​ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1) ​ δ ​ log 2 ⁡ ( ℓ δ) ​ x 2, \displaystyle\begin{split}\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|A_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu&\leq\dfrac{2.028}{2\sqrt{6}\pi}\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\,\delta\,\ell\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2}\\ &<\dfrac{2.0282}{\sqrt{6}\pi}\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)(\lambda^{3}+1)\,\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2},\end{split} |  | (3.4) |

where we used that ℓ < 2.0001 \ell<2.0001.

Now, let us analyze the double integral of B δ ​ ( y) B_{\delta}(y). By the mean value theorem we get

 | B δ ​ ( y) = 1 2 ​ | log ⁡ ( 1 − ( ( 1 + δ) ​ y) − 2) − log ⁡ ( 1 − y − 2) | ≤ δ ​ y y ⁡ ( y 2 − 1) ≤ 2 ​ δ y 2 B_{\delta}(y)=\dfrac{1}{2}\left|\log(1-((1+\delta)y)^{-2})-\log(1-y^{-2})\right|\leq\dfrac{\delta y}{y(y^{2}-1)}\leq\dfrac{2\delta}{y^{2}} |  |

where we have assumed that y ≥ 2 y\geq\sqrt{2}. Therefore, for x ≥ 2 ​ λ x\geq\sqrt{2}\lambda we have that

 | ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν | B δ ​ ( y) | 2 ​ d ​ y) ​ d ​ ν ≤ ∫ 1 λ ( ∫ x ​ ν / λ κ ​ x ​ ν 4 ​ δ 2 y 4 ​ d ​ y) ​ d ​ ν = 2 3 ​ ( λ 3 − 1 κ 3) ​ ( 1 − 1 λ 2) ​ δ 2 ​ x − 3 = 2 3 ​ ( λ 3 − 1 κ 3) ​ ( 1 − 1 λ 2) ​ ( δ ​ x − 5 log 2 ⁡ ( ℓ / δ)) ​ δ ​ log 2 ⁡ ( ℓ δ) ​ x 2 < 1.3 ⋅ 10 − 17 ​ ( λ 3 − 1 κ 3) ​ ( 1 − 1 λ 2) ​ δ ​ log 2 ⁡ ( ℓ δ) ​ x 2, \displaystyle\begin{split}\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\left|B_{\delta}(y)\right|^{2}\text{\rm d}y\right)\text{\rm d}\nu&\leq\int_{1}^{\lambda}\left(\int_{x\nu/\lambda}^{\kappa x\nu}\dfrac{4\delta^{2}}{y^{4}}\text{\rm d}y\right)\text{\rm d}\nu=\dfrac{2}{3}\left(\lambda^{3}-\dfrac{1}{\kappa^{3}}\right)\left(1-\dfrac{1}{\lambda^{2}}\right)\delta^{2}x^{-3}\\ &=\dfrac{2}{3}\left(\lambda^{3}-\dfrac{1}{\kappa^{3}}\right)\left(1-\dfrac{1}{\lambda^{2}}\right)\left(\dfrac{\delta x^{-5}}{\log^{2}(\ell/\delta)}\right)\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2}\\ &<1.3\cdot 10^{-17}\left(\lambda^{3}-\dfrac{1}{\kappa^{3}}\right)\left(1-\dfrac{1}{\lambda^{2}}\right)\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2},\end{split} |  | (3.5) |

where we used that δ ↦ ℓ / δ \delta\mapsto\ell/\delta is a decreasing function for δ > 0 \delta>0 and x > 2 x>\sqrt{2}. Combining ( 3.4) and ( 3.5) in ( 3.3) and then in ( 3.1) we get that for λ > 1 \lambda>1, κ > 1 \kappa>1, η > 0 \eta>0 and x ≥ 2 ​ λ x\geq\sqrt{2}\lambda:

 | ∫ x κ ​ x \displaystyle\int_{x}^{\kappa x} | ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y) 2 ​ d ​ y ≤ 𝒞 ⁡ ( κ, λ, η) ⋅ δ ​ log 2 ⁡ ( ℓ δ) ​ x 2, \displaystyle\big(\psi((1+\delta)y)-\psi(y)-\delta y\big)^{2}\text{\rm d}y\leq\mathcal{C}(\kappa,\lambda,\eta)\cdot\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2}, |  | (3.6) |

where

 | 𝒞 ⁡ ( κ, λ, η) = ( 1 + η) ​ 2.0282 6 ​ π ​ ( κ 2 + 1 λ 2) ​ ( λ 3 + 1 λ − 1) + 1.3 ⋅ 10 − 17 ​ ( 1 + 1 η) ​ ( λ 3 − 1 κ 3) ​ ( λ + 1 λ 2). \mathcal{C}(\kappa,\lambda,\eta)=(1+\eta)\dfrac{2.0282}{\sqrt{6}\pi}\left(\kappa^{2}+\dfrac{1}{\lambda^{2}}\right)\left(\dfrac{\lambda^{3}+1}{\lambda-1}\right)+1.3\cdot 10^{-17}\left(1+\frac{1}{\eta}\right)\left(\lambda^{3}-\dfrac{1}{\kappa^{3}}\right)\left(\dfrac{\lambda+1}{\lambda^{2}}\right). |  |

To reduce the notation, let us write 𝒱 ⁡ ( δ, y) = ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y \mathcal{V}(\delta,y)=\psi((1+\delta)y)-\psi(y)-\delta y. Consider x ≥ max ⁡ ( 10 13, 2 ​ λ) x\geq\max(10^{13},\sqrt{2}\lambda), and let N ≥ 0 N\geq 0 be the integer such that x / κ N + 1 < 2 ​ λ ≤ x / κ N {x}/{\kappa^{N+1}}<\sqrt{2}\lambda\leq{x}/{\kappa^{N}}. Then,

 | ∫ 1 x ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y ≤ ∑ n = 0 N ∫ x / κ n + 1 x / κ n ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y + ∫ 1 2 ​ λ ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y. \displaystyle\begin{split}\int_{1}^{x}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y&\leq\sum_{n=0}^{N}\int_{x/\kappa^{n+1}}^{x/\kappa^{n}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y+\int_{1}^{\sqrt{2}\lambda}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y.\end{split} |  | (3.7) |

Since 𝒱 ⁡ ( δ, y) = 0 \mathcal{V}(\delta,y)=0 for y < 2 1 + δ y<\frac{2}{1+\delta}, we bound the last term in the above sum as follows,

 | ∫ x / κ N + 1 x / κ N ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y ≤ ∫ 2 1 + δ 2 ​ κ ​ λ ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y ≤ ∑ j = 2 [2 ​ κ ​ λ] + 1 ∫ j 1 + δ j ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y + ∑ j = 2 [2 ​ κ ​ λ] ∫ j j + 1 1 + δ ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y. \displaystyle\begin{split}\int_{x/\kappa^{N+1}}^{x/\kappa^{N}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y&\leq\int_{\frac{2}{1+\delta}}^{\sqrt{2}\kappa\lambda}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y\leq\sum_{j=2}^{[\sqrt{2}\kappa\lambda]+1}\int_{\frac{j}{1+\delta}}^{j}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y+\sum_{j=2}^{[\sqrt{2}\kappa\lambda]}\int_{j}^{\frac{j+1}{1+\delta}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y.\end{split} |  | (3.8) |

Let us bound each sum in the above expression. By [19, Theorem 10] we know the bound | ψ ⁡ ( y) − y | ≤ 1 8 ​ π ​ y ​ log 2 ​ y |\psi(y)-y|\leq\frac{1}{8\pi}{\sqrt{y}\log^{2}y} for y ≥ 73.2 y\geq 73.2. A numerical computation for the cases less than 73.2 73.2 shows the estimate | ψ ⁡ ( y) − y | ≤ 2 ​ y ​ log 2 ​ y |\psi(y)-y|\leq{2\sqrt{y}\log^{2}y} for y ≥ 2 1 + δ y\geq\frac{2}{1+\delta}. Therefore, ( 𝒱 ⁡ ( δ, y)) 2 ≤ 2 ​ ( ψ ⁡ ( ( 1 + δ) ​ y) − ( 1 + δ) ​ y) 2 + 2 ​ ( ψ ⁡ ( y) − y) 2 ≤ 16.01 ​ y ​ log 4 ​ y (\mathcal{V}(\delta,y))^{2}\leq 2(\psi((1+\delta)y)-(1+\delta)y)^{2}+2(\psi(y)-y)^{2}\leq 16.01y\log^{4}y for y ≥ 2 1 + δ y\geq\frac{2}{1+\delta}. This implies that

 | ∑ j = 2 [2 ​ κ ​ λ] + 1 ∫ j 1 + δ j ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y \displaystyle\sum_{j=2}^{[\sqrt{2}\kappa\lambda]+1}\int_{\frac{j}{1+\delta}}^{j}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y | ≤ ∑ j = 2 [2 ​ κ ​ λ] + 1 ( j − j 1 + δ) ​ sup y ∈ [2 / ( 1 + δ), [2 ​ κ ​ λ] + 1] ( 𝒱 ⁡ ( δ, y)) 2 \displaystyle\leq\sum_{j=2}^{[\sqrt{2}\kappa\lambda]+1}\left(j-\dfrac{j}{1+\delta}\right)\sup_{y\in[2/(1+\delta),[\sqrt{2}\kappa\lambda]+1]}(\mathcal{V}(\delta,y))^{2} |  |

 |  | ≤ 16.01 ​ ( [2 ​ κ ​ λ] + 1) ​ log 4 ⁡ ( [2 ​ κ ​ λ] + 1) ​ ∑ j = 2 [2 ​ κ ​ λ] + 1 ( j − j 1 + δ) \displaystyle\leq 16.01([\sqrt{2}\kappa\lambda]+1)\log^{4}([\sqrt{2}\kappa\lambda]+1)\sum_{j=2}^{[\sqrt{2}\kappa\lambda]+1}\left(j-\dfrac{j}{1+\delta}\right) |  |

 |  | = 16.01 ​ ( [2 ​ κ ​ λ] + 1) ​ log 4 ⁡ ( [2 ​ κ ​ λ] + 1) ​ ( [2 ​ κ ​ λ] + 3) ​ [2 ​ κ ​ λ] 2 ​ δ 1 + δ:= α ⁡ ( κ, λ) 1 + δ ⋅ δ. \displaystyle=16.01([\sqrt{2}\kappa\lambda]+1)\log^{4}([\sqrt{2}\kappa\lambda]+1)\dfrac{([\sqrt{2}\kappa\lambda]+3)[\sqrt{2}\kappa\lambda]}{2}\dfrac{\delta}{1+\delta}:=\dfrac{\alpha(\kappa,\lambda)}{1+\delta}\cdot\delta. |  |

On the other hand, note that for j ≤ y ≤ j + 1 1 + δ j\leq y\leq\frac{j+1}{1+\delta}, we have that ψ ⁡ ( ( 1 + δ) ​ y) = ψ ⁡ ( y) \psi((1+\delta)y)=\psi(y). Then

 | ∑ j = 2 [2 ​ κ ​ λ] ∫ j j + 1 1 + δ ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y = ∑ j = 2 [2 ​ κ ​ λ] ∫ j j + 1 1 + δ ( δ ​ y) 2 ​ d ​ y ≤ ( [2 ​ κ ​ λ] + 1) 3 3 ⋅ δ 2:= β ⁡ ( κ, λ) ⋅ δ 2. \sum_{j=2}^{[\sqrt{2}\kappa\lambda]}\int_{j}^{\frac{j+1}{1+\delta}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y=\sum_{j=2}^{[\sqrt{2}\kappa\lambda]}\int_{j}^{\frac{j+1}{1+\delta}}(\delta y)^{2}\text{\rm d}y\leq\dfrac{([\sqrt{2}\kappa\lambda]+1)^{3}}{3}\cdot\delta^{2}:=\beta(\kappa,\lambda)\cdot\delta^{2}. |  |

Inserting these bounds in ( 3.8),

 | ∫ x / κ N + 1 x / κ N ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y ≤ α ⁡ ( κ, λ) 1 + δ ⋅ δ + β ⁡ ( κ, λ) ⋅ δ 2. \displaystyle\int_{x/\kappa^{N+1}}^{x/\kappa^{N}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y\leq\dfrac{\alpha(\kappa,\lambda)}{1+\delta}\cdot\delta+\beta(\kappa,\lambda)\cdot\delta^{2}. |  |

Now, assume that λ < 2 \lambda<2. Applying ( 3.6) for x ≥ 10 13 x\geq 10^{13}, we see that 3 3 3 If N = 0 N=0 this sum is empty.

 | ∑ n = 0 N − 1 ∫ x / κ n + 1 x / κ n ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y \displaystyle\sum_{n=0}^{N-1}\int_{x/\kappa^{n+1}}^{x/\kappa^{n}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y | ≤ 𝒞 ( κ, λ, η) ⋅ δ log 2 ( ℓ δ) ∑ n = 0 N − 1 ( x κ n + 1) 2 ≤ 𝒞 ⁡ ( κ, λ, η) κ 2 − 1 ⋅ δ log 2 ( ℓ δ) x 2. \displaystyle\leq\mathcal{C}(\kappa,\lambda,\eta)\cdot\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)\sum_{n=0}^{N-1}\left(\dfrac{x}{\kappa^{n+1}}\right)^{2}\leq\dfrac{\mathcal{C}(\kappa,\lambda,\eta)}{\kappa^{2}-1}\cdot\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2}. |  |

Finally,

 | ∫ 1 2 ​ λ ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y \displaystyle\int_{1}^{\sqrt{2}\lambda}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y | ≤ ∫ 1 2.9 ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y ≤ ∫ 2 1 + δ 2 ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y + ∫ 2 3 1 + δ ( 𝒱 ⁡ ( δ, y)) 2 ​ d ​ y \displaystyle\leq\int_{1}^{2.9}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y\leq\int_{\frac{2}{1+\delta}}^{2}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y+\int_{2}^{\frac{3}{1+\delta}}(\mathcal{V}(\delta,y))^{2}\text{\rm d}y |  |

 |  | ≤ 2 ​ ( log ⁡ 2) 2 ​ δ 1 + δ + ∫ 2 3 1 + δ δ 2 ​ y 2 ​ d ​ y < 0.961 ​ δ. \displaystyle\leq\dfrac{2(\log 2)^{2}\delta}{1+\delta}+\int_{2}^{\frac{3}{1+\delta}}\delta^{2}y^{2}\text{\rm d}y<0.961\delta. |  |

Combining the previous bounds in ( 3.7) we conclude for 1 < λ < 2 1<\lambda<2, κ > 1 \kappa>1, η > 0 \eta>0 and x ≥ 10 13 x\geq 10^{13},

 | ∫ 1 x ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − δ ​ y) 2 ​ d ​ y \displaystyle\int_{1}^{x}\big(\psi((1+\delta)y)-\psi(y)-\delta y\big)^{2}\text{\rm d}y | ≤ 𝒞 ⁡ ( κ, λ, η) κ 2 − 1 ⋅ δ ​ log 2 ⁡ ( ℓ δ) ​ x 2 + ( α ⁡ ( κ, λ) 1 + δ + 0.961 + β ⁡ ( κ, λ) ​ δ) ​ δ. \displaystyle\leq\dfrac{\mathcal{C}(\kappa,\lambda,\eta)}{\kappa^{2}-1}\cdot\delta\,\log^{2}\left(\dfrac{\ell}{\delta}\right)x^{2}+\left(\dfrac{\alpha(\kappa,\lambda)}{1+\delta}+0.961+\beta(\kappa,\lambda)\delta\right)\delta. |  |

Minimizing the expression 𝒞 ⁡ ( κ, λ, η) / ( κ 2 − 1) {\mathcal{C}(\kappa,\lambda,\eta)}/{(\kappa^{2}-1)} for 1 < λ < 2 1<\lambda<2, κ > 1 \kappa>1, η > 0 \eta>0, we choose κ = 100 \kappa=100, λ = 1.677 \lambda=1.677 y η = 5 ⋅ 10 − 11 \eta=5\cdot 10^{-11}. Then

 | 𝒞 ⁡ ( κ, λ, η) κ 2 − 1 = 2.22571 ​ …, α ⁡ ( κ, λ) 1 + δ ≤ 9.8 ⋅ 10 10, and ​ β ​ ( κ, λ) ≤ 4.5 ⋅ 10 6. \dfrac{\mathcal{C}(\kappa,\lambda,\eta)}{\kappa^{2}-1}=2.22571\ldots,\,\,\,\,\dfrac{\alpha(\kappa,\lambda)}{1+\delta}\leq 9.8\cdot 10^{10},\,\,\,\,\mbox{and}\,\,\,\,\beta(\kappa,\lambda)\leq 4.5\cdot 10^{6}. |  |

Since 0 < δ ≤ 10 − 13 0<\delta\leq 10^{-13}, δ ↦ ℓ / δ \delta\mapsto\ell/\delta is a decreasing function for δ > 0 \delta>0, and x ≥ 10 13 x\geq 10^{13} we conclude. ∎

## 4. An explicit bound for J θ ​ ( x, δ) J_{\theta}(x,\delta)

As we mentioned in the introduction, we want an explicit bound for J θ ​ ( x, δ) J_{\theta}(x,\delta). Our goal in this section is to establish the following result.

###### Theorem 3.

Assume RH. Then, for x ≥ 10 13 x\geq 10^{13} and δ ∈ ( 0, 10 − 13] \delta\in(0,10^{-13}] we have that 4 4 4 We highlight that one can prove that J θ ​ ( x, δ) ≤ 2.2259 ⋅ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2 J_{\theta}(x,\delta)\leq 2.2259\cdot\delta\,\log^{2}\left(\frac{2.0001}{\delta}\right)x^{2}, for x x sufficiently large and δ \delta sufficiently small.

 | J θ ​ ( x, δ) ≤ 2.5571 ⋅ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2. \displaystyle J_{\theta}(x,\delta)\leq 2.5571\cdot\delta\,\log^{2}\left(\dfrac{2.0001}{\delta}\right)x^{2}. |  |

The proof relies on comparing the integrals J θ ​ ( x, δ) J_{\theta}(x,\delta) and J ψ ​ ( x, δ) J_{\psi}(x,\delta), and noting that their difference is a negligible error term. At first such a passage sounds trivial: the difference is a sum supported on prime powers p ℓ p^{\ell} with ℓ ≥ 2 \ell\geq 2, and should thus be negligable straight away. However, since we are working in the short interval [y, ( 1 + δ) ​ y] [y,(1+\delta)y], this naive approach seems to fall short. To bound the difference we follow the method Saffari–Vaughan presented in [17, p. 22] only partially. In their approach, the mentioned error term is bounded by O ⁡ ( δ ​ log 2 ⁡ ( 1 δ) ​ x 2) O(\delta\,\log^{2}\left(\tfrac{1}{\delta}\right)x^{2}), i.e. the same as the main term. In our case, however, a more refined estimation of the error term is required, to get the sharpest constant possible.

### 4.1. Proof of Theorem 3: first step

We start by applying ( 2.6) two times. Thus, for any η > 0 \eta>0

 | J θ ​ ( x, δ) \displaystyle J_{\theta}(x,\delta) | ≤ ( 1 + η) ​ J ψ ​ ( x, δ) + ( 1 + 1 η) ​ ∫ 1 x ( ψ ⁡ ( ( 1 + δ) ​ y) − ψ ⁡ ( y) − θ ⁡ ( ( 1 + δ) ​ y) + θ ⁡ ( y)) 2 ​ d ​ y \displaystyle\leq\left(1+{\eta}\right)J_{\psi}(x,\delta)+\left(1+\frac{1}{\eta}\right)\int_{1}^{x}\big(\psi((1+\delta)y)-\psi(y)-\theta((1+\delta)y)+\theta(y)\big)^{2}\text{\rm d}y |  |

 |  | ≤ ( 1 + η) ​ J ψ ​ ( x, δ) + ( 1 + 1 η) 2 ​ ∫ 1 x ( ( 1 + δ) 1 2 ​ y 1 2 − y 1 2) 2 ​ d ​ y \displaystyle\leq\left(1+{\eta}\right)J_{\psi}(x,\delta)+\left(1+\frac{1}{\eta}\right)^{2}\int_{1}^{x}\left((1+\delta)^{\frac{1}{2}}y^{\frac{1}{2}}-y^{\frac{1}{2}}\right)^{2}\text{\rm d}y |  |

 |  | + ( 1 + η) 2 η ∫ 1 x ( ψ ( ( 1 + δ) y) − ψ ( y) − θ ( ( 1 + δ) y) + θ ( y) − ( 1 + δ) 1 2 y 1 2 + y 1 2) 2 d y \displaystyle\,\,\,\,\,\,\,\,\,\,\,\,\,+\dfrac{(1+\eta)^{2}}{\eta}\int_{1}^{x}\left(\psi((1+\delta)y)-\psi(y)-\theta((1+\delta)y)+\theta(y)-(1+\delta)^{\frac{1}{2}}y^{\frac{1}{2}}+y^{\frac{1}{2}}\right)^{2}\text{\rm d}y |  |

 |  | ≤ ( 1 + η) ​ J ψ ​ ( x, δ) + ( 1 + 1 η) 2 ​ δ 2 ​ x 2 2 \displaystyle\leq\left(1+{\eta}\right)J_{\psi}(x,\delta)+\left(1+\dfrac{1}{\eta}\right)^{2}\dfrac{\delta^{2}x^{2}}{2} |  |

 |  | + ( 1 + η) 2 η ∫ 1 x ( ψ ( ( 1 + δ) y) − ψ ( y) − θ ( ( 1 + δ) y) + θ ( y) − ( 1 + δ) 1 2 y 1 2 + y 1 2) 2 d y. \displaystyle\,\,\,\,\,\,\,\,\,\,\,\,\,+\dfrac{(1+\eta)^{2}}{\eta}\int_{1}^{x}\left(\psi((1+\delta)y)-\psi(y)-\theta((1+\delta)y)+\theta(y)-(1+\delta)^{\frac{1}{2}}y^{\frac{1}{2}}+y^{\frac{1}{2}}\right)^{2}\text{\rm d}y. |  |

Thus, we need to bound the last integral on the right-hand side of the above expression. By a change of variable y = e ν y=e^{\nu}, we have that this integral is exactly

 | ∫ 0 log ⁡ x | Δ δ ​ ( ν) ​ e ν | 2 ​ d ​ ν, \int_{0}^{\log x}|\Delta_{\delta}(\nu)e^{\nu}|^{2}\text{\rm d}\nu, |  |

where Δ δ ​ ( ν) ≔ ( ψ ⁡ ( ( 1 + δ) ​ e ν) − ψ ⁡ ( e ν) − θ ⁡ ( ( 1 + δ) ​ e ν) + θ ⁡ ( e ν) − ( 1 + δ) 1 2 ​ e ν 2 + e ν 2) ​ e − ν 2 \Delta_{\delta}(\nu)\coloneq\left(\psi((1+\delta)e^{\nu})-\psi(e^{\nu})-\theta((1+\delta)e^{\nu})+\theta(e^{\nu})-(1+\delta)^{\frac{1}{2}}e^{\frac{\nu}{2}}+e^{\frac{\nu}{2}}\right)e^{-\frac{\nu}{2}}. Therefore,

 | J θ ​ ( x, δ) ≤ ( 1 + η) ​ J ψ ​ ( x, δ) + ( 1 + 1 η) 2 ​ δ 2 ​ x 2 2 + ( 1 + η) 2 η ​ ∫ 0 log ⁡ x | Δ δ ​ ( ν) ​ e ν | 2 ​ d ​ ν ≤ ( 1 + η) ​ J ψ ​ ( x, δ) + ( 1 + 1 η) 2 ​ δ 2 ​ x 2 2 + ( 1 + η) 2 η ​ x 2 ​ ∫ 0 ∞ | Δ δ ​ ( ν) | 2 ​ d ​ ν. \displaystyle\begin{split}J_{\theta}(x,\delta)&\leq\left(1+{\eta}\right)J_{\psi}(x,\delta)+\left(1+\dfrac{1}{\eta}\right)^{2}\dfrac{\delta^{2}x^{2}}{2}+\dfrac{(1+\eta)^{2}}{\eta}\int_{0}^{\log x}|\Delta_{\delta}(\nu)e^{\nu}|^{2}\text{\rm d}\nu\\ &\leq\left(1+{\eta}\right)J_{\psi}(x,\delta)+\left(1+\dfrac{1}{\eta}\right)^{2}\dfrac{\delta^{2}x^{2}}{2}+\dfrac{(1+\eta)^{2}}{\eta}\,x^{2}\int_{0}^{\infty}|\Delta_{\delta}(\nu)|^{2}\text{\rm d}\nu.\end{split} |  | (4.1) |

To bound the last integral in ( 4.1), we shall use Plancherel’s theorem. By Perron’s formula we have, for y ≥ 1 y\geq 1 and y ∉ ℤ y\not\in\mathbb{Z}, that (see [17, p. 22])

 | ψ ⁡ ( y) − θ ⁡ ( y) − y 1 2 + 1 = 1 2 ​ π ​ i ​ lim T → ∞ ∫ 1 2 − i ​ T 1 2 + i ​ T ( − ζ ′ ζ ​ ( 2 ​ s) − 1 2 ​ s − 1 + ∑ p log ⁡ p p s ​ ( p 2 ​ s − 1)) ​ y s s ​ d ​ s. \displaystyle\psi(y)-\theta(y)-y^{\frac{1}{2}}+1=\frac{1}{2\pi i}\lim_{T\to\infty}\int_{\frac{1}{2}-iT}^{\frac{1}{2}+iT}\left(-\frac{\zeta^{\prime}}{\zeta}(2s)-\frac{1}{2s-1}+\sum_{p}\frac{\log p}{p^{s}(p^{2s}-1)}\right)\frac{y^{s}}{s}\text{\rm d}s. |  | (4.2) |

Letting

 | F ⁡ ( t) ≔ − ζ ′ ζ ​ ( 1 + 2 ​ i ​ t) − 1 2 ​ i ​ t + ∑ p log ⁡ p p 1 2 + i ​ t ​ ( p 1 + 2 ​ i ​ t − 1), \displaystyle F(t)\coloneq-\frac{\zeta^{\prime}}{\zeta}(1+2it)-\frac{1}{2it}+\sum_{p}\frac{\log p}{p^{\frac{1}{2}+it}(p^{1+2it}-1)}, |  | (4.3) |

by ( 4.2), we have the following equality for almost every ν ≥ 0 \nu\geq 0,

 | Δ δ ​ ( ν) = 1 2 ​ π ​ lim T → ∞ ∫ − T T F ⁡ ( t) ​ ( ( 1 + δ) 1 2 + i ​ t − 1 1 2 + i ​ t) ​ e ν ​ i ​ t ​ d ​ t. \Delta_{\delta}(\nu)=\frac{1}{2\pi}\lim_{T\to\infty}\int_{-T}^{T}F(t)\left(\dfrac{(1+\delta)^{\frac{1}{2}+it}-1}{\frac{1}{2}+it}\right)e^{\nu it}\text{\rm d}t. |  |

By Lemma 2.1 and ( 2.11), F F is continuous on ℝ \mathbb{R} and F ⁡ ( t) = O ⁡ ( log ⁡ t) F(t)=O(\log t). Then, we conclude that the integrand belongs to L 2 ​ ( ℝ) L^{2}(\mathbb{R}). By Fourier inversion formula and Plancherel’s theorem we obtain that

 | ∫ 0 ∞ | Δ δ ​ ( ν) | 2 ​ d ​ ν ≤ 1 2 ​ π ​ ∫ − ∞ ∞ | F ⁡ ( t) ​ ( ( 1 + δ) 1 2 + i ​ t − 1 1 2 + i ​ t) | 2 ​ d ​ t. \int_{0}^{\infty}|\Delta_{\delta}(\nu)|^{2}\text{\rm d}\nu\leq\frac{1}{2\pi}\int_{-\infty}^{\infty}\left|F(t)\left(\dfrac{(1+\delta)^{\frac{1}{2}+it}-1}{\frac{1}{2}+it}\right)\right|^{2}\text{\rm d}t. |  |

We now split up the integral on the right hand side. By Lemma 2.5 and the fact that | F ⁡ ( t) | = | F ⁡ ( − t) | |F(t)|=|F(-t)| we get

 | ∫ 0 ∞ | Δ δ ​ ( ν) | 2 ​ d ​ ν ≤ δ 2 π ​ ∫ 0 ℓ δ | F ⁡ ( t) | 2 ​ d ​ t + ℓ 2 π ​ ∫ ℓ δ ∞ | F ⁡ ( t) | 2 t 2 ​ d ​ t. \displaystyle\int_{0}^{\infty}|\Delta_{\delta}(\nu)|^{2}\text{\rm d}\nu\leq\frac{\delta^{2}}{\pi}\int_{0}^{\frac{\ell}{\delta}}\left|F(t)\right|^{2}\text{\rm d}t+\frac{\ell^{2}}{\pi}\int_{\frac{\ell}{\delta}}^{\infty}\dfrac{|F(t)|^{2}}{t^{2}}\text{\rm d}t. |  |

Therefore, by Theorem 2 in ( 4.1) we arrive at

 | J θ ​ ( x, δ) ≤ ( 1 + η) ⋅ 2.2258 ⋅ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2 + ( 1 + 1 η) 2 ​ δ 2 ​ x 2 2 + ( 1 + η) 2 ​ δ 2 ​ x 2 η ​ π ∫ 0 ℓ δ | F ( t) | 2 d t + ( 1 + η) 2 ​ ℓ 2 ​ x 2 η ​ π ∫ ℓ δ ∞ | F ⁡ ( t) | 2 t 2 d t. \displaystyle\begin{split}\!\!J_{\theta}(x,\delta)\leq&\left(1+{\eta}\right)\cdot 2.2258\cdot\delta\,\log^{2}\left(\dfrac{2.0001}{\delta}\right)x^{2}+\left(1+\dfrac{1}{\eta}\right)^{2}\dfrac{\delta^{2}x^{2}}{2}\\ &\,\,\,\,\,\,+\dfrac{(1+\eta)^{2}\delta^{2}x^{2}}{\eta\pi}\int_{0}^{\frac{\ell}{\delta}}\left|F(t)\right|^{2}\text{\rm d}t+\dfrac{(1+\eta)^{2}\ell^{2}x^{2}}{\eta\pi}\int_{\frac{\ell}{\delta}}^{\infty}\dfrac{|F(t)|^{2}}{t^{2}}\text{\rm d}t.\end{split} |  | (4.4) |

### 4.2. The error term

In order to complete the proof of Theorem 3, it remains to verify that all terms on the right-hand side of ( 4.4), beginning with the second, are suitably small. It is immediate that δ 2 ​ x 2 2 \frac{\delta^{2}x^{2}}{2} is negligible. Our next task is to estimate the integrals related to F ⁡ ( t) F(t). From ( 4.3), ( 2.6) and (1) in Lemma A.1, for any a ≥ b ≥ 0 a\geq b\geq 0 and η 1 > 0 \eta_{1}>0:

 | ∫ a b | F ⁡ ( t) | 2 ​ d ​ t ≤ ( 1 + 1 η 1) ​ ∫ a b | ζ ′ ζ ​ ( 1 + 2 ​ i ​ t) + 1 2 ​ i ​ t | 2 ​ d ​ t + ( 1 + η 1) ​ ∫ a b | ∑ p log ⁡ p p 1 2 + i ​ t ​ ( p 1 + 2 ​ i ​ t − 1) | 2 ​ d ​ t ≤ 1 2 ​ ( 1 + 1 η 1) ​ ∫ 2 ​ a 2 ​ b | ζ ′ ζ ​ ( 1 + i ​ t) + 1 i ​ t | 2 ​ d ​ t + 2.9636 ​ ( 1 + η 1) ​ ( b − a). \displaystyle\begin{split}\int_{a}^{b}|F(t)|^{2}\,\text{\rm d}t&\leq\left(1+\dfrac{1}{\eta_{1}}\right)\int_{a}^{b}\left|\frac{\zeta^{\prime}}{\zeta}(1+2it)+\frac{1}{2it}\right|^{2}\!\!\text{\rm d}t+(1+\eta_{1})\int_{a}^{b}\left|\sum_{p}\frac{\log p}{p^{\frac{1}{2}+it}(p^{1+2it}-1)}\right|^{2}\!\!\text{\rm d}t\\ &\leq\dfrac{1}{2}\left(1+\dfrac{1}{\eta_{1}}\right)\int_{2a}^{2b}\left|\frac{\zeta^{\prime}}{\zeta}(1+it)+\frac{1}{it}\right|^{2}\!\!\text{\rm d}t+2.9636(1+\eta_{1})(b-a).\end{split} |  | (4.5) |

#### 4.2.1. The first integral in ( 4.4)

Here we split as follows

 | ∫ 0 ℓ δ | F ⁡ ( t) | 2 ​ d ​ t = ∫ 0 1 4 | F ⁡ ( t) | 2 ​ d ​ t + ∫ 1 4 10 4 2 | F ⁡ ( t) | 2 ​ d ​ t + ∫ 10 4 2 ℓ δ | F ⁡ ( t) | 2 ​ d ​ t:= I 1 + I 2 + I 3. \displaystyle\int_{0}^{\frac{\ell}{\delta}}\left|F(t)\right|^{2}\text{\rm d}t=\int_{0}^{\frac{1}{4}}\left|F(t)\right|^{2}\text{\rm d}t+\int_{\frac{1}{4}}^{\frac{10^{4}}{2}}\left|F(t)\right|^{2}\text{\rm d}t+\int_{\frac{10^{4}}{2}}^{\frac{\ell}{\delta}}\left|F(t)\right|^{2}\text{\rm d}t:=I_{1}+I_{2}+I_{3}. |  | (4.6) |

To bound I 1 I_{1}, we apply ( 4.5) with a = 0 a=0, b = 1 4 b=\frac{1}{4}, Lemma 2.4 and η 1 = 1.5307 \eta_{1}=1.5307 obtaining I 1 ≤ 4.8 I_{1}\leq 4.8. To bound I 2 I_{2}, we use computational methods 5 5 5 More specifically, we have checked this numerically in python with mpmath.quad and mpmath.zeta from the mpmath-package. to get

 | ∫ 1 2 10 4 | ζ ′ ζ ​ ( 1 + i ​ t) + 1 i ​ t | 2 ​ d ​ t ≤ 8400. \displaystyle\int_{\frac{1}{2}}^{10^{4}}\left|\frac{\zeta^{\prime}}{\zeta}(1+it)+\frac{1}{it}\right|^{2}\text{\rm d}t\leq 8400. |  |

Then, applying ( 4.5) with a = 1 4 a=\frac{1}{4}, b = 10 4 2 b=\frac{10^{4}}{2} and η 1 = 0.5324 \eta_{1}=0.5324 we obtain I 2 ≤ 34794.8 I_{2}\leq 34794.8. Finally, to bound I 3 I_{3}, we start applying ( 2.6) with η 2 = 10 − 8 \eta_{2}=10^{-8} and Lemma 2.3 with T = 2 ​ ℓ δ ≥ 4 ⋅ 10 13 T=\frac{2\ell}{\delta}\geq 4\cdot 10^{13} to see that

 | ∫ 10 4 2 ​ ℓ δ | ζ ′ ζ ​ ( 1 + i ​ t) + 1 i ​ t | 2 ​ d ​ t ≤ ( 1 + 10 − 8) ​ ∫ 10 4 2 ​ ℓ δ | ζ ′ ζ ​ ( 1 + i ​ t) | 2 ​ d ​ t + ( 1 + 10 8) ​ ∫ 10 4 2 ​ ℓ δ 1 t 2 ​ d ​ t ≤ 1.6113 ​ ℓ δ, \displaystyle\int_{10^{4}}^{\frac{2\ell}{\delta}}\left|\frac{\zeta^{\prime}}{\zeta}(1+it)+\frac{1}{it}\right|^{2}\text{\rm d}t\leq(1+10^{-8})\int_{10^{4}}^{\frac{2\ell}{\delta}}\left|\frac{\zeta^{\prime}}{\zeta}(1+it)\right|^{2}\!\!\text{\rm d}t+(1+10^{8})\int_{10^{4}}^{\frac{2\ell}{\delta}}\,\dfrac{1}{t^{2}}\text{\rm d}t\leq 1.6113\,\dfrac{\ell}{\delta}, |  |

where we used that ℓ > 2 \ell>2. Thus, applying ( 4.5) with a = 10 4 2 a=\frac{10^{4}}{2}, b = ℓ δ b=\frac{\ell}{\delta} and η 1 = 0.5213 \eta_{1}=0.5213 we obtain I 3 ≤ 6.8597 ​ ℓ δ − 22542.6 I_{3}\leq 6.8597\frac{\ell}{\delta}-22542.6. Finally, in ( 4.6) we get

 | ∫ 0 ℓ δ | F ⁡ ( t) | 2 ​ d ​ t ≤ 6.8598 ​ ℓ δ. \displaystyle\int_{0}^{\frac{\ell}{\delta}}\left|F(t)\right|^{2}\text{\rm d}t\leq 6.8598\,\dfrac{\ell}{\delta}. |  | (4.7) |

#### 4.2.2. The second integral in ( 4.4)

For t ≥ ℓ δ > 2 ⋅ 10 13 t\geq\frac{\ell}{\delta}>2\cdot 10^{13}, we apply ( 2.6) with η 2 = 10 − 8 \eta_{2}=10^{-8} and Lemma 2.3 with T = 2 ​ t T=2t to get

 | ∫ 2 ​ ℓ δ 2 ​ t | ζ ′ ζ ​ ( 1 + i ​ u) + 1 i ​ u | 2 ​ d ​ u ≤ ( 1 + 10 − 8) ​ ∫ 2 ​ ℓ δ 2 ​ t | ζ ′ ζ ​ ( 1 + i ​ u) | 2 ​ d ​ u + ( 1 + 10 8) ​ ∫ 2 ​ ℓ δ 2 ​ t 1 u 2 ​ d ​ u ≤ 1.6113 ​ t. \displaystyle\int_{\frac{2\ell}{\delta}}^{2t}\left|\frac{\zeta^{\prime}}{\zeta}(1+iu)+\frac{1}{iu}\right|^{2}\text{\rm d}u\leq(1+10^{-8})\int_{\frac{2\ell}{\delta}}^{2t}\left|\frac{\zeta^{\prime}}{\zeta}(1+iu)\right|^{2}\!\!\text{\rm d}u+(1+10^{8})\int_{\frac{2\ell}{\delta}}^{2t}\dfrac{1}{u^{2}}\text{\rm d}u\leq 1.6113\,t. |  | (4.8) |

Now, since F ⁡ ( t) = O ⁡ ( log ⁡ t) F(t)=O(\log t) as t → ∞ t\to\infty, we can use integration by parts to arrive at

 | ∫ ℓ δ ∞ | F ⁡ ( t) | 2 t 2 ​ d ​ t = 2 ​ ∫ ℓ δ ∞ ( ∫ ℓ δ t | F ⁡ ( u) | 2 ​ d ​ u) ​ 1 t 3 ​ d ​ t. \displaystyle\int_{\frac{\ell}{\delta}}^{\infty}\dfrac{|F(t)|^{2}}{t^{2}}\text{\rm d}t=2\int_{\frac{\ell}{\delta}}^{\infty}\left(\int_{\frac{\ell}{\delta}}^{t}|F(u)|^{2}\text{\rm d}u\right)\dfrac{1}{t^{3}}\text{\rm d}t. |  |

Now, in ( 4.5) choose a = ℓ δ a=\frac{\ell}{\delta}, b = t b=t, η 1 = 0.7373 \eta_{1}=0.7373, and use ( 4.8) , to see that

 | ∫ ℓ δ ∞ | F ⁡ ( t) | 2 t 2 ​ d ​ t ≤ ( 1 + 1 η 1) ​ ∫ ℓ δ ∞ ( ∫ 2 ​ ℓ δ 2 ​ t | ζ ′ ζ ​ ( 1 + i ​ u) + 1 i ​ u | 2 ​ d ​ u) ​ 1 t 3 ​ d ​ t + 5.9272 ​ ( 1 + η 1) ​ ∫ ℓ δ ∞ ( t − ℓ δ) ​ 1 t 3 ​ d ​ t ≤ 8.9454 ​ δ ℓ. \displaystyle\begin{split}\int_{\frac{\ell}{\delta}}^{\infty}\dfrac{|F(t)|^{2}}{t^{2}}\text{\rm d}t&\leq\left(1+\dfrac{1}{\eta_{1}}\right)\int_{\frac{\ell}{\delta}}^{\infty}\left(\int_{\frac{2\ell}{\delta}}^{2t}\left|\frac{\zeta^{\prime}}{\zeta}(1+iu)+\frac{1}{iu}\right|^{2}\text{\rm d}u\right)\dfrac{1}{t^{3}}\text{\rm d}t+5.9272(1+\eta_{1})\int_{\frac{\ell}{\delta}}^{\infty}\left(t-\dfrac{\ell}{\delta}\right)\dfrac{1}{t^{3}}\text{\rm d}t\\ &\leq 8.9454\,\dfrac{\delta}{\ell}.\end{split} |  | (4.9) |

Finally, inserting ( 4.7) and ( 4.9) in ( 4.4), using that ℓ < 2.0001 \ell<2.0001 and δ ≤ 10 − 13 \delta\leq 10^{-13},

 | J θ ​ ( x, δ) \displaystyle\!\!J_{\theta}(x,\delta) | ≤ ( 1 + η) ⋅ 2.2258 ⋅ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2 + ( 1 + 1 η) 2 ​ δ 2 ​ x 2 2 + ( 15.8052 ​ ( 1 + η) 2 ​ ℓ η ​ π) ​ δ ​ x 2 \displaystyle\leq\left(1+{\eta}\right)\cdot 2.2258\cdot\delta\,\log^{2}\left(\dfrac{2.0001}{\delta}\right)x^{2}+\left(1+\dfrac{1}{\eta}\right)^{2}\dfrac{\delta^{2}x^{2}}{2}+\left(\dfrac{15.8052(1+\eta)^{2}\ell}{\eta\pi}\right)\delta x^{2} |  |

 |  | < [( 1 + η) ⋅ 2.2258 + 31.612 ​ ( 1 + η) 2 η ​ π ​ log 2 ⁡ ( 2.0001 ⋅ 10 13)] ​ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2 + ( 1 + 1 η) 2 ​ δ 2 ​ x 2 2. \displaystyle<\left[\left(1+{\eta}\right)\cdot 2.2258+\dfrac{31.612(1+\eta)^{2}}{\eta\pi\log^{2}\left({2.0001}\cdot{10^{13}}\right)}\right]\delta\,\log^{2}\left(\dfrac{2.0001}{\delta}\right)x^{2}+\left(1+\dfrac{1}{\eta}\right)^{2}\dfrac{\delta^{2}x^{2}}{2}. |  |

The expression in the brackets is optimized by choosing η = 0.0693 \eta=0.0693.

## 5. Proof of Theorem 1

We closely follow the argument in [7, Section 4], some of which is restated here for convenience of the reader.

Let a ∈ [10 − 13, 1) a\in[10^{-13},1), and x ≥ 10 13 x\geq 10^{13}, Theorem 3 implies

 | ∫ a ​ x x ( θ ⁡ ( ( 1 + δ) ​ y) − θ ⁡ ( y) − δ ​ y) 2 ​ d ​ y ≤ 2.5571 ⋅ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2 \int_{ax}^{x}\big(\theta((1+\delta)y)-\theta(y)-\delta y\big)^{2}\text{\rm d}y\leq 2.5571\cdot\delta\,\log^{2}\left(\dfrac{2.0001}{\delta}\right)x^{2} |  | (5.1) |

holds for any δ ∈ ( 0, 10 − 13] \delta\in(0,10^{-13}]. Assume there is no Goldbach number in the interval ( x, x + h] (x,x+h] for any 1 ≤ h ≤ x 1\leq h\leq x Following *verbatim*[7, Section 4], this implies that

 | ∫ a ​ x x ( θ ⁡ ( ( 1 + δ) ​ y) − θ ⁡ ( y) − δ ​ y) 2 ​ d ​ y > δ 2 ​ x 3 3 ​ ( 1 8 − a 3), \int_{ax}^{x}\big(\theta((1+\delta)y)-\theta(y)-\delta y\big)^{2}\text{\rm d}y>\frac{\delta^{2}x^{3}}{3}\left(\frac{1}{8}-a^{3}\right), |  |

under the assumption δ ≤ h 2 ​ x \delta\leq\frac{h}{2x}. By ( 5.1), we then have

 | δ 2 ​ x 3 3 ​ ( 1 8 − a 3) < 2.5571 ​ δ ​ log 2 ⁡ ( 2.0001 δ) ​ x 2, \frac{\delta^{2}x^{3}}{3}\left(\frac{1}{8}-a^{3}\right)<2.5571\,\delta\log^{2}\left(\frac{2.0001}{\delta}\right)x^{2}, |  |

Choosing δ = h / ( 2 ​ x) \delta=h/(2x) with h = C ​ ( log ⁡ x) 2 h=C(\log x)^{2}, with C > 1 C>1, we have

 | C ​ ( log ⁡ x) 2 6 ​ ( 1 8 − a 3) \displaystyle\frac{C(\log x)^{2}}{6}\left(\frac{1}{8}-a^{3}\right) | < 2.5571 ​ log 2 ⁡ ( 2.0001 ⋅ 2 ​ x C ​ ( log ⁡ x) 2) \displaystyle<2.5571\log^{2}\left(\frac{2.0001\cdot 2x}{C(\log x)^{2}}\right) |  |

 |  | = 2.5571 ​ ( log ⁡ x) 2 ​ ( 1 + 1 log ⁡ x ​ log ⁡ ( 4.0002 C ​ ( log ⁡ x) 2)) 2 ≤ 2.5571 ​ ( log ⁡ x) 2. \displaystyle=2.5571(\log x)^{2}\left(1+\frac{1}{\log x}\log\left(\frac{4.0002}{C(\log x)^{2}}\right)\right)^{2}\leq 2.5571(\log x)^{2}. |  |

This inequality is contradicted when

 | C > 6 ⋅ 2.5571 1 8 − a 3. C>\frac{6\cdot 2.5571}{\frac{1}{8}-a^{3}}. |  |

Choosing a = 10 − 13 a=10^{-13}, this implies we can take C = 122.75 C=122.75, as long as 122.75 ​ ( log ⁡ x) 2 / 2 ​ x ≤ 10 − 13 {122.75(\log x)^{2}}/{2x}\leq 10^{-13}, which is true whenever x ≥ 1.1 ⋅ 10 18 x\geq 1.1\cdot 10^{18}. In [10], Goldbach’s conjecture is proven up to 4 ⋅ 10 18 4\cdot 10^{18}, so this finishes the proof.

## Appendix A Some sums over primes

###### Lemma A.1.

We have the following bounds:

1. (1)

 | ∑ p log ⁡ p p 1 2 ​ ( p − 1) < 1.7215, \sum_{p}\frac{\log p}{p^{\frac{1}{2}}(p-1)}<1.7215, |  |

2. (2)

 | ∑ n = 1 ∞ Λ 2 ​ ( n) n 2 < 0.8053, \sum_{n=1}^{\infty}\dfrac{\Lambda^{2}(n)}{n^{2}}<0.8053, |  |

3. (3)

 | ∑ p log 2 ⁡ p p 2 − p < 0.982. \sum_{p}\dfrac{\log^{2}p}{p^{2}-p}<0.982. |  |

###### Proof.

To prove (1), we use the fact that p n > n ​ log ⁡ n p_{n}>n\log n for all n ≥ 1 n\geq 1, where p n p_{n} is the n-th prime number (see [16, Corollary, p. 69]). Thus, letting n 0 = 26355867 n_{0}=26355867,

 | ∑ p log ⁡ p p 1 2 ​ ( p − 1) \displaystyle\sum_{p}\frac{\log p}{p^{\frac{1}{2}}(p-1)} | = ∑ p ≤ p n 0 log ⁡ p p 1 2 ​ ( p − 1) + ∑ p > p n 0 log ⁡ p p 1 2 ​ ( p − 1) \displaystyle=\sum_{p\leq p_{n_{0}}}\frac{\log p}{p^{\frac{1}{2}}(p-1)}+\sum_{p>p_{n_{0}}}\frac{\log p}{p^{\frac{1}{2}}(p-1)} |  |

 |  | < ∑ p ≤ p n 0 log ⁡ p p 1 2 ​ ( p − 1) + ∑ n > n 0 log ⁡ ( n ​ log ⁡ n) ( n ​ log ⁡ n) 1 2 ​ ( n ​ log ⁡ n − 1) \displaystyle<\sum_{p\leq p_{n_{0}}}\frac{\log p}{p^{\frac{1}{2}}(p-1)}+\sum_{n>{n_{0}}}\frac{\log(n\log n)}{(n\log n)^{\frac{1}{2}}(n\log n-1)} |  |

 |  | < ∑ p ≤ p n 0 log ⁡ p p 1 2 ​ ( p − 1) + ∫ n 0 ∞ log ⁡ ( x ​ log ⁡ x) ( x ​ log ⁡ x) 1 2 ​ ( x ​ log ⁡ x − 1) ​ d ​ x < 1.721381 + 0.000104 < 1.7215, \displaystyle<\sum_{p\leq p_{n_{0}}}\frac{\log p}{p^{\frac{1}{2}}(p-1)}+\int_{{n_{0}}}^{\infty}\frac{\log(x\log x)}{(x\log x)^{\frac{1}{2}}(x\log x-1)}\text{\rm d}x<1.721381+0.000104<1.7215, |  |

where the numerical bounds are evaluated computationally. With a similar approach we get (3). To prove (2), note that

 | ∑ n = 1 ∞ Λ ​ ( n) 2 n 2 = ∑ p log 2 ⁡ p ​ ∑ k = 1 ∞ 1 p 2 ​ k = ∑ p log 2 ⁡ p ⁡ ( 1 1 − p − 2 − 1) = ∑ p log 2 ⁡ p p 2 − 1. \sum_{n=1}^{\infty}\frac{\Lambda(n)^{2}}{n^{2}}=\sum_{p}\log^{2}p\sum_{k=1}^{\infty}\frac{1}{p^{2k}}=\sum_{p}\log^{2}p\left(\frac{1}{1-p^{-2}}-1\right)=\sum_{p}\frac{\log^{2}p}{p^{2}-1}. |  |

Then, we bound this sum as in (1). ∎

###### Lemma A.2.

Assume RH. Then, for all x ≥ 10 13 x\geq 10^{13} we have

 | ∑ n ≤ x Λ 2 ​ ( n) n ≤ log 2 ⁡ x 2 + 4.5222. \sum_{n\leq x}\dfrac{\Lambda^{2}(n)}{n}\leq\dfrac{\log^{2}x}{2}+4.5222. |  |

###### Proof.

Using (3) from Lemma A.1,

 | ∑ n ≤ x Λ 2 ​ ( n) n ≤ ∑ p ≤ x log 2 ⁡ p p + ∑ p ≤ x log 2 ⁡ p ​ ∑ k = 2 ∞ 1 p k = ∑ p ≤ x log 2 ⁡ p p + ∑ p log 2 ⁡ p p 2 − p < ∑ p ≤ x log 2 ⁡ p p + 0.982. \displaystyle\begin{split}\sum_{n\leq x}\frac{\Lambda^{2}(n)}{n}&\leq\sum_{p\leq x}\frac{\log^{2}p}{p}+\sum_{p\leq\sqrt{x}}\log^{2}p\sum_{k=2}^{\infty}\dfrac{1}{p^{k}}=\sum_{p\leq x}\frac{\log^{2}p}{p}+\sum_{p}\dfrac{\log^{2}p}{p^{2}-p}<\sum_{p\leq x}\frac{\log^{2}p}{p}+0.982.\end{split} |  | (A.1) |

To bound the sum on the right hand-side of ( A.1) we use integration by parts and the bound θ ⁡ ( y) < y + y ​ log 2 ​ y / 8 ​ π \theta(y)<y+\sqrt{y}\log^{2}y/8\pi, for y > 0 y>0 (by [19, Theorem 10, Eq (6.5)]), where θ ⁡ ( y) = ∑ p ≤ y log ⁡ p \theta(y)=\sum_{p\leq y}\log p. Thus

 | ∑ p ≤ x log 2 ⁡ p p \displaystyle\sum_{p\leq x}\frac{\log^{2}p}{p} | = log 2 ⁡ 2 2 + log ⁡ x x ​ θ ​ ( x) − log ⁡ 3 3 ​ θ ​ ( 3 −) + ∫ 3 x ( − log ⁡ y y) ′ ​ θ ​ ( y) ​ d ​ y \displaystyle=\frac{\log^{2}2}{2}+\dfrac{\log x}{x}\theta(x)-\dfrac{\log 3}{3}\theta(3^{-})+\int_{3}^{x}\left(-\dfrac{\log y}{y}\right)^{\prime}\theta(y)\text{\rm d}y |  |

 |  | < log 2 ⁡ 2 2 − log ⁡ 3 ​ log ⁡ 2 3 + log ⁡ 3 + ∫ 3 x log ⁡ y y ​ d ​ y + log 3 ⁡ x 8 ​ π ​ x + ∫ 3 x ( − log ⁡ y y) ′ ​ y ​ log 2 ​ y 8 ​ π ​ d ​ y \displaystyle<\frac{\log^{2}2}{2}-\dfrac{\log 3\log 2}{3}+\log 3+\int_{3}^{x}\dfrac{\log y}{y}\text{\rm d}y+\dfrac{\log^{3}x}{8\pi\sqrt{x}}+\int_{3}^{x}\left(-\dfrac{\log y}{y}\right)^{\prime}\dfrac{\sqrt{y}\log^{2}y}{8\pi}\text{\rm d}y |  |

 |  | < log 2 ⁡ 2 2 − log ⁡ 3 ​ log ⁡ 2 3 + log ⁡ 3 + log 2 ⁡ x 2 − log 2 ⁡ 3 2 + log 3 ⁡ x 8 ​ π ​ x + ∫ 3 ∞ ( − log ⁡ y y) ′ ​ y ​ log 2 ​ y 8 ​ π ​ d ​ y \displaystyle<\frac{\log^{2}2}{2}-\dfrac{\log 3\log 2}{3}+\log 3+\dfrac{\log^{2}x}{2}-\dfrac{\log^{2}3}{2}+\dfrac{\log^{3}x}{8\pi\sqrt{x}}+\int_{3}^{\infty}\left(-\dfrac{\log y}{y}\right)^{\prime}\dfrac{\sqrt{y}\log^{2}y}{8\pi}\text{\rm d}y |  |

 |  | < log 2 ⁡ x 2 + 3.5401 + log 3 ⁡ x 8 ​ π ​ x < log 2 ⁡ x 2 + 3.5402, \displaystyle<\dfrac{\log^{2}x}{2}+3.5401+\dfrac{\log^{3}x}{8\pi\sqrt{x}}<\dfrac{\log^{2}x}{2}+3.5402, |  |

where in the final inequality we used that x ≥ 10 13 x\geq 10^{13}. Inserting this in ( A.1) we arrive at the desired result. ∎

## References

- [1] R. J. Backlund, *Über die Nullstellen der Riemannschen Zetafunktion*, Acta Math. 41 (1916), no. 1, 345–375.
- [2] B. C. Berndt, *On the Hurwitz zeta-function*, Rocky Mountain J. Math. 2 (1972), no. 1, 151–157.
- [3] R. P. Brent, D. J. Platt, T. S. Trudgian, *The mean square of the error term in the prime number theorem*, J. Number Theory 238 (2022), 740–762.
- [4] V. Chandee, *Explicit upper bounds for L-functions on the critical line*, Proc. Amer. Math. Soc. 137 (2009), no. 12, 4049–4063.
- [5] A. Chirre, M. V. Hagen and A. Simonič, *Conditional estimates for the logarithmic derivative of Dirichlet L L -functions*, Indag. Math. (N.S.) 35 (2024), no. 1, 14–27.
- [6] D. Dona, H. A. Helfgott, and S. Zuniga Alterman. *Explicit L 2 L^{2} bounds for the Riemann ζ \zeta function*, J. Théor. Nombres Bordeaux 34 (2022), no. 1, 91–133.
- [7] M. Cully-Hugill and A. Dudek, *An explicit mean-value estimate for the prime number theorem in intervals*, J. Aust. Math. Soc. 117 (2024), no. 1, 1–15.
- [8] P. X. Gallagher, *A large sieve density estimate near σ = 1 \sigma=1*, Invent. Math. 11 (1970), 329–339.
- [9] H. A. Helfgott, *The ternary Goldbach problem*, Second preliminary version. To appear in Ann. of Math. Studies, available at [https://webusers.imj-prg.fr/~harald.helfgott/anglais/book.html][5].
- [10] S. Herzog, T. Oliviera e Silva, S. Pardi, *Empirical verification of the even Goldbach conjecture and computation of prime gaps up to 4 ⋅ 10 18 4\cdot 10^{18}*, Math. Comp. 83 (2014), no. 288, 2033–2060.
- [11] D. R. Johnston, O. Ramaré and T. Trudgian, An explicit upper bound for L ⁡ ( 1, χ) L(1,\chi) when χ \chi is quadratic, Res. Number Theory 9 (2023), no. 4, Paper No. 72, 20 pp.
- [12] I. Kátai, *A comment on a paper of Ju. V. Linnik*, Magyar Tud. Akad. Mat. Fiz. Oszt. Közl. 17 (1967), 99–100.
- [13] Yu. V. Linnik, *Some conditional theorems concerning the binary Goldbach problem*, Izv. Akad. Nauk SSSR Ser. Mat. 16 (1952), 503–520.
- [14] H. L. Montgomery and R. C. Vaughan, *The exceptional set in Goldbach’s problem*, Acta Arith. 27 (1975), 353–370.
- [15] H. L. Montgomery and R. C. Vaughan, Multiplicative Number Theory: I. Classical Theory, Cambridge Studies in Advanced Mathematics 97, Cambridge University Press, 2006.
- [16] J. B. Rosser and L. Schoenfeld, Approximate formulas for some functions of prime numbers, Illinois J. Math. 6 (1962), 64–94.
- [17] B. Saffari and R. C. Vaughan, *On the fractional parts of x/n related sequences. II*, Ann. Inst. Fourier (Grenoble) 27 (1977), no. 2, v, 1–30.
- [18] A. Selberg, *On the normal density of primes in small intervals, and the difference between consecutive primes*, Arch. Math. Naturvid. 47 (1943), no. 6, 87–105.
- [19] L. Schoenfeld, Sharper bounds for the Chebyshev functions θ ⁡ ( x) \theta(x) and ψ ⁡ ( x) \psi(x). II, Math. Comp. 30 (1976), no. 134, 337–360.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:cchirre@pucp.edu.pe
[4]: mailto:markus.v.hagen@ntnu.no
[5]: https://webusers.imj-prg.fr/~harald.helfgott/anglais/book.html
