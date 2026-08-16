<!-- source: https://arxiv.org/html/2312.14743v2 | converted from HTML -->

Iterated Entropy Derivatives and Binary Entropy Inequalities

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2312.14743v2 [cs.IT] 14 Jan 2025

# Iterated Entropy Derivatives and Binary Entropy Inequalities

Tanay Wakhare 1 Email address: [twakhare@mit.edu][3]

###### Abstract.

We embark on a systematic study of the ( k + 1) (k+1) -th derivative of x k − r ​ H ​ ( x r) x^{k-r}H(x^{r}), where H ⁡ ( x):= − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) H(x):=-x\log x-(1-x)\log(1-x) is the binary entropy and k ≥ r ≥ 1 k\geq r\geq 1 are integers. Our motivation is the conjectural entropy inequality α k ​ H ​ ( x k) ≥ x k − 1 ​ H ​ ( x) \alpha_{k}H(x^{k})\geq x^{k-1}H(x), where 0 < α k < 1 0<\alpha_{k}<1 is given by a functional equation. The k = 2 k=2 case was the key technical tool driving recent breakthroughs on the union-closed sets conjecture. We express d k + 1 d ​ x k + 1 ​ x k − r ​ H ​ ( x r) \frac{d^{k+1}}{dx^{k+1}}x^{k-r}H(x^{r}) as a rational function, an infinite series, and a sum over generalized Stirling numbers. This allows us to reduce the proof of the entropy inequality for real k k to showing that an associated polynomial has only two real roots in the interval ( 0, 1) (0,1), which also allows us to prove the inequality for fractional exponents such as k = 3 / 2 k=3/2. The proof suggests a new framework for proving tight inequalities for the sum of polynomials times the logarithms of polynomials, which converts the inequality into a statement about the real roots of a simpler associated polynomial.

0 0 footnotetext: 1 Department of Electrical Engineering and Computer Science, MIT, Cambridge, MA 02139, USA 0 0 footnotetext: 0 0 footnotetext: MSC2020: 94A17, 26C10, 11B65, 05A10

## 1. Introduction

The union-closed sets conjecture is a notorious open problem, stating that any set family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} which is union-closed (so that the union of two sets in ℱ \mathcal{F} is also in the system) contains a "popular" element of the ground set contained in at least a 1 / 2 1/2 fraction of the sets of ℱ \mathcal{F}.

Although the conjecture is still unproven, Gilmer made a recent breakthrough stating that any union-closed set system contains an element in at least an 0.01 0.01 fraction of the sets in ℱ \mathcal{F}. The constant 0.01 0.01 was quickly improved to 3 − 5 2 ≈ 0.38197 \frac{3-\sqrt{5}}{2}\approx 0.38197 [AHS22, Saw22, CL22]. Building upon more sophisticated coupling arguments suggested by [Saw22, Yu23, Cam22], the current best constant is ≈ 0.38237 \approx 0.38237 [Liu24], though the method suffers natural limitations. The survey [Cam23] summarizes recent progress and barriers, but new ideas will be needed to prove the full union-closed sets conjecture.

The k = 2 k=2 case of the following inequality ( 1.2) was conjectured by Gilmer, and was one of the key technical tools underlying his breakthrough. This case was proved using computer calculations by [AHS22]. Studying the extension to approximate k k -union closed set systems led to [Yus23] conjecturing inequality ( 1.2) for every integer k ≥ 2 k\geq 2 and proving it for k = 3, 4 k=3,4. It later emerged that Boppana proved the k = 2 k=2 case several decades earlier [Bop85]. He recently republished a simplified proof [Bop23], which forms the basis for Sawin’s [Saw22] improvements and is the proof we build upon. The main contribution of this paper is to reduce the proof of the real k ≥ 1 k\geq 1 case to a conjecture about the roots of an explicit polynomial, which suggests a general framework to prove tight inequalities involving the sum of logarithms of polynomials.

###### Conjecture 1.

Let k ≥ 1 k\geq 1 be real and 0 < α k < 1 0<\alpha_{k}<1 be the unique solution of

(1.1) |  | α k = 1 ( 1 + α k) k − 1 \alpha_{k}=\frac{1}{(1+\alpha_{k})^{k-1}} |  |

in ( 0, 1) (0,1). Then

(1.2) |  | α k ​ H ​ ( x k) ≥ x k − 1 ​ H ​ ( x), 0 ≤ x ≤ 1, \alpha_{k}H(x^{k})\geq x^{k-1}H(x),\quad 0\leq x\leq 1, |  |

where H ⁡ ( x):= − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) H(x):=-x\log x-(1-x)\log(1-x) is the binary entropy. We have equality at x = 0, 1 1 + α k, 1 x=0,\frac{1}{1+\alpha_{k}},1.

Throughout, all logarithms are to base e e. Lemma 16 shows that the functional equation ( 1.1) has a unique solution satisfying 1 / k < α k < 1 1/k<\alpha_{k}<1, and Lemma 17 shows that α k = log ⁡ k k + O k ​ ( log ⁡ log ⁡ k k) \alpha_{k}=\frac{\log k}{k}+O_{k}\left(\frac{\log\log k}{k}\right) asymptotically for large k k.

The natural transformation for this problem is x = 1 1 + y x=\frac{1}{1+y}, since we now study this inequality over y y in ( 0, ∞) (0,\infty) instead of over x x in ( 0, 1) (0,1), which maps the root at x = 1 1 + α k x=\frac{1}{1+\alpha_{k}} to a root at y = α k y=\alpha_{k}. Writing x k = 1 1 + α k x_{k}=\frac{1}{1+\alpha_{k}}, this functional equation is equivalent to x k + x k k = 1 x_{k}+x_{k}^{k}=1. The equation x + x k = 1 x+x^{k}=1 corresponds to the characteristic function of Fibonacci type recurrences like F n = F n − 1 + F n − k F_{n}=F_{n-1}+F_{n-k}. This explains the appearance of the golden ratio in the k = 2 k=2 case studied for the union closed sets conjecture, since x + x 2 = 1 x+x^{2}=1 has roots closely connected to the golden ratio. This also motivates studying x k, α k x_{k},\alpha_{k} in terms of generalized Fibonacci polynomials, related to [Cig22].

We show that Conjecture 2 implies Conjecture 1. This is a strong statement about polynomial roots, since the following polynomial p k, r ​ ( x) p_{k,r}(x) has degree k 2 + k ​ r − r k^{2}+kr-r, but we conjecture it to only have two roots in ( 0, 1) (0,1). The following conjecture also allows us to rigorously prove Conjecture 1 for any rational exponent using a finite calculation, such as for k = 3 / 2 k=3/2.

###### Conjecture 2.

Let k > r ≥ 1 k>r\geq 1 be integers. Define the entropy polynomial

(1.3) |  | h k, r ​ ( x):= ∑ j = 0 k − 1 x r ​ j ​ ∑ v = 0 j ( − 1) j − v v + 1 ​ ( r ​ v + k k) ​ ( k j − v) h_{k,r}(x):=\sum_{j=0}^{k-1}x^{rj}\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v} |  |

and let α k \alpha_{k} satisfy the functional equation ( 1.1). Then the polynomial

(1.4) |  | p k, r ​ ( x):= α k / r ​ k ​ ( 1 − x r) k ​ h k, k ​ ( x) − r ​ ( 1 − x k) k ​ h k, r ​ ( x) p_{k,r}(x):=\alpha_{k/r}k(1-x^{r})^{k}h_{k,k}(x)-r(1-x^{k})^{k}h_{k,r}(x) |  |

has exactly two real roots in ( 0, 1) (0,1), counting multiplicity.

Note that Lemma 16 states that α k / r ​ k r > 1 \alpha_{k/r}\frac{k}{r}>1, so that the first polynomial is multiplied by a larger constant factor.

###### Theorem 3.

If Conjecture 2 holds for a particular k > r k>r pair, then inequality ( 1.2) holds for the exponent k / r k/r. If Conjecture 2 holds for all coprime k > r ≥ 1 k>r\geq 1, then inequality ( 1.2) holds for all real k ≥ 1 k\geq 1.

For instance, a quick calculation shows that Conjecture 2 holds for k = 3, r = 2 k=3,r=2. A natural approach is to use a special case of Descartes’ rules of signs, which states that if a polynomial has two coefficient sign changes, then it has either 0 0 or 2 2 positive real roots. Numerically, under the change of variables x = 1 1 + y x=\frac{1}{1+y}, the polynomial ( 1 + y) k 2 + k ​ r − r ​ p k, r ​ ( 1 1 + y) (1+y)^{k^{2}+kr-r}p_{k,r}\left(\frac{1}{1+y}\right) always has two sign changes. Since h k, r h_{k,r} has degree k ​ r − r kr-r and p k, r p_{k,r} has degree k 2 + k ​ r − r k^{2}+kr-r, the factor of ( 1 + y) k 2 + k ​ r − r (1+y)^{k^{2}+kr-r} ensures that the resulting expression is a polynomial while only introducing extra roots at y = − 1 y=-1. If this has at most two real roots for y y in ( 0, ∞) (0,\infty), these correspond to at most two real roots of p k, r ​ ( x) = p k, r ​ ( 1 1 + y) p_{k,r}(x)=p_{k,r}\left(\frac{1}{1+y}\right) in ( 0, 1) (0,1). However, the coefficients in y y become unwieldy double or triple sums, from which it is difficult to deduce the sign pattern.

Some example cases are

 | h 1, 1 ​ ( x) = 1, h 2, 2 ​ ( x) = 1 + x 2, h 3, 3 ​ ( x) = 1 + 7 ​ x 3 + x 6, h 4, 4 ​ ( x) = 1 + 31 ​ x 4 + 31 ​ x 8 + x 12. \displaystyle h_{1,1}(x)=1,\quad\quad h_{2,2}(x)=1+x^{2},\quad\quad h_{3,3}(x)=1+7x^{3}+x^{6},\quad\quad h_{4,4}(x)=1+31x^{4}+31x^{8}+x^{12}. |  |

and

 | h 4, 1 ​ ( x) \displaystyle h_{4,1}(x) | = 1 − 3 2 ​ x + x 2 − 1 4 ​ x 3, h 4, 2 ​ ( x) = 1 + 7 2 ​ x 2 − 2 3 ​ x 4 + 1 6 ​ x 6, \displaystyle=1-\frac{3}{2}x+x^{2}-\frac{1}{4}x^{3},\quad\quad\quad\thinspace\thinspace h_{4,2}(x)=1+\frac{7}{2}x^{2}-\frac{2}{3}x^{4}+\frac{1}{6}x^{6}, |  |

 | h 4, 3 ​ ( x) \displaystyle h_{4,3}(x) | = 1 + 27 2 ​ x 3 + 6 ​ x 6 − 1 4 ​ x 9, h 4, 4 ​ ( x) = 1 + 31 ​ x 4 + 31 ​ x 8 + x 12. \displaystyle=1+\frac{27}{2}x^{3}+6x^{6}-\frac{1}{4}x^{9},\quad\quad h_{4,4}(x)=1+31x^{4}+31x^{8}+x^{12}. |  |

This motivates the study of the binomial sums

(1.5) |  | h k, r, j:= ∑ v = 0 j ( − 1) j − v v + 1 ​ ( r ​ v + k k) ​ ( k j − v) \displaystyle h_{k,r,j}:=\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v} |  |

for all values of the parameters k, r, j k,r,j. While this is rational valued in general, several rescaled integer valued multiples of h k, r, j h_{k,r,j} do not appear in the OEIS. For instance, using a variation of the proof of Lemma 7 using finite difference operators, we can show that h k, r, k = 1 k + 1 ​ ( r − 1 k) h_{k,r,k}=\frac{1}{k+1}\binom{r-1}{k} for all r, k ≥ 1 r,k\geq 1, which is 0 0 for r ≤ k r\leq k. An interesting and related open problem is computing a simple representation for h k, r ​ ( x) h_{k,r}(x) under the change of variables x ↦ 1 − x x\mapsto 1-x or x r ↦ 1 − x r x^{r}\mapsto 1-x^{r}, mirroring the symmetry of the binary entropy H ⁡ ( x) = H ⁡ ( 1 − x) H(x)=H(1-x).

Our key technical tool is several equivalent expansions for the ( k + 1) (k+1) -st derivative of x k − r ​ H ​ ( x r) x^{k-r}H(x^{r}), which are all functions of x r x^{r}. The first expansion expresses the derivative as a single infinite series, the second factors out a single root at 0 0 and a root of multiplicity k k at 1 1, which leaves the numerator as a polynomial. The last generalizes and simplifies [Yus23, Lemma 3.5, Lemma 3.8] and rewrites the ( k + 1) (k+1) -st derivative in terms of a different rational basis, with coefficients given by generalized Stirling numbers.

###### Theorem 4.

Let S ( k, ℓ | α, β, γ) S(k,\ell|\alpha,\beta,\gamma) denote the generalized Stirling numbers of Hsu and Shiue, defined in Equation ( 2.4). Let k ≥ r ≥ 1 k\geq r\geq 1 be positive integers. For 0 < x < 1 0<x<1 we have

(1.6) |  | ( d d ​ x) k + 1 ​ x k − r ​ H ​ ( x r) \displaystyle\left(\frac{d}{dx}\right)^{k+1}x^{k-r}H(x^{r}) | = − r ⋅ k! ∑ ℓ = 0 ∞ ( k + r ​ ℓ k) 1 ℓ + 1 x r ​ ℓ − 1 \displaystyle=-r\cdot k!\sum_{\ell=0}^{\infty}\binom{k+r\ell}{k}\frac{1}{\ell+1}x^{r\ell-1} |  |

(1.7) |  |  | = − r ⋅ k! x ​ ( 1 − x r) k ∑ j = 0 k − 1 x r ​ j ∑ v = 0 j ( − 1) j − v v + 1 ( r ​ v + k k) ( k j − v) \displaystyle=-\frac{r\cdot k!}{x(1-x^{r})^{k}}\sum_{j=0}^{k-1}x^{rj}\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v} |  |

(1.8) |  |  | = − ∑ ℓ = 0 k − 1 ℓ! S ( k, ℓ + 1 | 1, r, k − r) r ℓ + 2 x r ​ ℓ − 1 ( 1 − x r) ℓ + 1. \displaystyle=-\sum_{\ell=0}^{k-1}\ell!S(k,\ell+1|1,r,k-r)r^{\ell+2}\frac{x^{r\ell-1}}{(1-x^{r})^{\ell+1}}. |  |

###### Corollary 5.

The special case r = 1 r=1 satisfies

(1.9) |  | ( d d ​ x) k + 1 ​ x k − 1 ​ H ​ ( x) = ( k − 1)! x 2 ​ ( 1 − 1 ( 1 − x) k). \displaystyle\left(\frac{d}{dx}\right)^{k+1}x^{k-1}H(x)=\frac{(k-1)!}{x^{2}}\left(1-\frac{1}{(1-x)^{k}}\right). |  |

###### Corollary 6.

The special case r = k r=k has the following additional simplifications in terms of s s -binomial coefficients defined in Definition ( 5.1), where ω = e 2 ​ π ​ i k \omega=e^{\frac{2\pi i}{k}} is a primitive k k -th root of unity:

(1.10) |  | ( d d ​ x) k + 1 ​ H ​ ( x k) \displaystyle\left(\frac{d}{dx}\right)^{k+1}H(x^{k}) | = − k! x ∑ j = 0 k − 1 1 ( 1 − ω j ​ x) k \displaystyle=-\frac{k!}{x}\sum_{j=0}^{k-1}\frac{1}{(1-\omega^{j}x)^{k}} |  |

(1.11) |  |  | = − k ⋅ k! x ​ ( 1 − x k) k ∑ ℓ = 0 k − 1 ( k ℓ ​ k) k − 1 x k ​ ℓ \displaystyle=-\frac{k\cdot k!}{x(1-x^{k})^{k}}\sum_{\ell=0}^{k-1}\binom{k}{\ell k}_{k-1}x^{k\ell} |  |

(1.12) |  |  | = − k ⋅ k! ∑ ℓ = 0 ∞ ( k + k ​ ℓ − 1 k − 1) x k ​ ℓ − 1. n o \displaystyle=-k\cdot k!\sum_{\ell=0}^{\infty}\binom{k+k\ell-1}{k-1}x^{k\ell-1}.no |  |

The scaling r ​ v rv in the inner binomial coefficient ( r ​ v + k k) \binom{rv+k}{k} in Equation ( 1.7) is what makes the analysis here difficult. One common classical tool to deal with the r ​ v rv scaling is the Rothe-Hagen identity [GKP94, Table 202] and its generalizations, for example due to Gould [Gou61]. However, the Rothe-Hagen identity contains binomials of the form ( r ​ v + k v) \binom{rv+k}{v}, where k, r k,r are parameters and v v is the summation index. The Lagrange inversion formula also yields series with binomial coefficients ( r ​ v + k v) \binom{rv+k}{v}, such as the expression for 1 1 + α k \frac{1}{1+\alpha_{k}} from Lemma 18. Instead, we require binomials of the form ( r ​ v + k k) \binom{rv+k}{k}. We could also compute a Fourier expansion by writing the sum over all v v instead of r ​ v rv, and then inserting 1 r ​ ∑ j = 0 r − 1 ω j ​ v \frac{1}{r}\sum_{j=0}^{r-1}\omega^{jv}, where ω \omega is a primitive r r -th root of unity. However, this only provides a simplification in the case k = r k=r, where it is used in the proof of Corollary 6.

Inequality ( 1.2) also has an information theoretic interpretation. Letting X 1, …, X k ∼ 𝖡𝖾𝗋 ⁡ ( x) X_{1},\ldots,X_{k}\sim\mathsf{Ber}(x) be Bernoulli distributed bits and A j:= ∧ i = 1 j X i A_{j}:=\wedge_{i=1}^{j}X_{i} denote the binary AND of the first j j bits, we have H ⁡ ( x k) = H ⁡ ( A k) H(x^{k})=H(A_{k}) and H ⁡ ( A k | A k − 1) = x k − 1 ​ H ​ ( x) H(A_{k}|A_{k-1})=x^{k-1}H(x) the conditional entropy of the k k -th bit. This gives a strong data processing inequality comparing the entropy of the AND of k k bits to the entropy of the AND of k k -th bit conditioned on the AND of the previous k − 1 k-1 bits.

In Section 2 we introduce the generalized Stirling numbers of Hsu and Shiue, and demonstrate a connection to generalized Bernoulli and Eulerian numbers. In Section 3 we evaluate h k, r, j h_{k,r,j} in certain regimes of k, r, j k,r,j. In Section 4 we prove the entropy expansions of Theorem 4. In Section 5 we prove Corollaries 5 and 6, which are the r = 1 r=1 and r = k r=k cases of Theorem 4. In Section 6 we prove Theorem 3, an equivalence between our main entropy inequality and counting real roots of h k, r ​ ( x) h_{k,r}(x) in ( 0, 1) (0,1). Finally, in Section 7 we study the scaling constant α k \alpha_{k}.

The proof suggests a more general framework for proving tight inequalities for logarithms of polynomials of the form

 | f ⁡ ( x):= ∑ i p i ​ ( x) ​ log ⁡ ( 1 − q i ​ ( x)) ≥ 0, f(x):=\sum_{i}p_{i}(x)\log(1-q_{i}(x))\geq 0, |  |

where both p i ​ ( x) p_{i}(x) and q i ​ ( x) q_{i}(x) are polynomials in x x. Such functions arise as free energies in problems in statistical mechanics or in constraint satisfaction problems, such as in the study of graph k k -coloring [COV13, Equation (8)] or boolean k k -SAT [MMZ06, Equation (3)]. First, we manually find the roots of f ⁡ ( x) f(x). Next, we pass to the ( n + 1) (n+1) -st derivative, where n n is the maximum degree max i ⁡ ( deg ⁡ p i ​ ( x) + deg ⁡ q i ​ ( x)) \max_{i}(\deg p_{i}(x)+\deg q_{i}(x)). Taking this number of derivatives leads to a rational function. We then use classical methods to identify the number of roots of the ( n + 1) (n+1) -st derivative, which is a rational function and more tractable than the original logarithmic f ⁡ ( x) f(x). We then appeal to Rolle’s theorem in the form that a function can have at most one more root than its derivative on a given interval. We use Rolle’s theorem to pass from the ( n + 1) (n+1) -st derivative to the original function, which can have at most ( n + 1) (n+1) more roots than the ( n + 1) (n+1) -st derivative. If we are lucky, then in the first step we identified all roots of f ⁡ ( x) f(x). Finally, we show that f ⁡ ( x) f(x) takes positive values between each root, which implies that it is positive everywhere. The innovation over previous methods is that if we can control the multiplicities of the roots of f ⁡ ( x) f(x) and the multiplicities of the roots of the ( n + 1) (n+1) -st derivative, which is now a polynomial, Rolle’s theorem allows us to deduce the desired inequality.

## 2. Definitions

The ubiquitous Stirling numbers of the second kind are defined as the solutions to the recurrence [GKP94, Equation (6.3)] and have the closed form [GKP94, Equation (6.19)]:

(2.1) |  | S ⁡ ( n + 1, ℓ) \displaystyle S(n+1,\ell) | = S ⁡ ( n, ℓ − 1) + ℓ ​ S ​ ( n, ℓ), \displaystyle=S(n,\ell-1)+\ell S(n,\ell), |  |

(2.2) |  | ℓ! ​ S ​ ( n, ℓ) \displaystyle\ell!S(n,\ell) | = ∑ v = 0 ℓ ( − 1) ℓ − v ​ ( ℓ v) ​ v n. \displaystyle=\sum_{v=0}^{\ell}(-1)^{\ell-v}\binom{\ell}{v}v^{n}. |  |

Define the scaled Pochhammer symbol ( z | α) n:= z ( z − α) ⋯ ( z − ( n − 1) α), n ≥ 1 (z|\alpha)_{n}:=z(z-\alpha)\cdots(z-(n-1)\alpha),n\geq 1. Hsu and Shiue [HS88] introduced generalized Stirling numbers using these scaled Pochhammer symbols. Let α, β, γ ∈ ℝ \alpha,\beta,\gamma\in\mathbb{R}. Define generalized Stirling numbers S ( n, ℓ | α, β, γ) S(n,\ell|\alpha,\beta,\gamma) via the change of basis relation

(2.3) |  | ( z | α) n = ∑ ℓ = 0 n S ( n, ℓ | α, β, γ) ( z − γ | β) n (z|\alpha)_{n}=\sum_{\ell=0}^{n}S(n,\ell|\alpha,\beta,\gamma)(z-\gamma|\beta)_{n} |  |

and initial conditions S ( 0, 0 | α, β, γ) = 1, S ( n, 0 | α, β, γ) = ( γ | α) n S(0,0|\alpha,\beta,\gamma)=1,S(n,0|\alpha,\beta,\gamma)=(\gamma|\alpha)_{n}.

Many properties of these, discovered by subsequent researchers, are surveyed in the book [MS16]. We will require the following recurrence and closed form [MS16, Theorem (4.51), Theorem (4.52)]:

(2.4) |  | S ( n + 1, ℓ | α, β, γ) \displaystyle S(n+1,\ell|\alpha,\beta,\gamma) | = S ( n, ℓ − 1 | α, β, γ) + ( ℓ β − n α + γ) S ( n, ℓ | α, β, γ), \displaystyle=S(n,\ell-1|\alpha,\beta,\gamma)+(\ell\beta-n\alpha+\gamma)S(n,\ell|\alpha,\beta,\gamma), |  |

(2.5) |  | S ( n, ℓ | α, β, γ) \displaystyle S(n,\ell|\alpha,\beta,\gamma) | = ( − 1) ℓ β ℓ ​ ℓ! ​ ∑ j = 0 ℓ ( − 1) j ​ ( ℓ j) ​ ( β ​ j + γ | α) n. \displaystyle=\frac{(-1)^{\ell}}{\beta^{\ell}\ell!}\sum_{j=0}^{\ell}(-1)^{j}\binom{\ell}{j}(\beta j+\gamma|\alpha)_{n}. |  |

In the remainder of this paper, we often take α = 1 \alpha=1 in the definition of the generalized Stirling numbers, which gives

(2.6) |  | ℓ! S ( n, ℓ | 1, β, γ) β ℓ = ∑ v = 0 ℓ ( − 1) ℓ − v ( ℓ v) n! ( β ​ v + γ n). \ell!S(n,\ell|1,\beta,\gamma)\beta^{\ell}=\sum_{v=0}^{\ell}(-1)^{\ell-v}\binom{\ell}{v}n!\binom{\beta v+\gamma}{n}. |  |

We also require the Dobiński type formula [HS88, Equation (27)] which factors e x e^{x} out of the series:

(2.7) |  | ∑ ℓ = 0 ∞ x ℓ ℓ! ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n S ( n, ℓ | 1, r, s) r ℓ e x x ℓ. \sum_{\ell=0}^{\infty}\frac{x^{\ell}}{\ell!}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n}S(n,\ell|1,r,s)r^{\ell}e^{x}x^{\ell}. |  |

Note that by comparing recurrences and initial conditions, we can show that

 | C ( k, t, j) = k j ( k − 1)! S ( t, j | 1, k, 0), C(k,t,j)=\frac{k^{j}}{(k-1)!}S(t,j|1,k,0), |  |

where C ⁡ ( k, t, j) C(k,t,j) are the rational coefficients introduced by Yuster [Yus23] in his work on the approximate k k -union closed sets conjecture, which considers the r = 1, k r=1,k cases of our result. Furthermore, the C ⁡ ( k, t, j) C(k,t,j) coefficients have been studied before and are exactly the generalized factorial coefficients of [Cha02, Definition 8.2], since they satisfy the same recurrence and initial conditions.

### 2.1. Classical analogy

Comparing the two closed form expressions for Stirling numbers ( 2.2) and ( 2.6) shows that, up to normalization by β \beta, we replace the term v n v^{n} with

 | n! ( β ​ v + γ n) = ( β v + γ) ( β v + γ − 1) ⋯ ( β v + γ − n + 1). n!\binom{\beta v+\gamma}{n}=(\beta v+\gamma)(\beta v+\gamma-1)\cdots(\beta v+\gamma-n+1). |  |

If we further specialize γ = 0 \gamma=0, we can take the limit

(2.8) |  | lim β → ∞ S ( n, ℓ | 1, β, 0) β ℓ β n \displaystyle\lim_{\beta\to\infty}\frac{S(n,\ell|1,\beta,0)\beta^{\ell}}{\beta^{n}} | = lim β → ∞ 1 ℓ! ​ β n ​ ∑ v = 0 ℓ ( − 1) ℓ − v ​ ( ℓ v) ​ n! ​ ( β ​ v n) \displaystyle=\lim_{\beta\to\infty}\frac{1}{\ell!\beta^{n}}\sum_{v=0}^{\ell}(-1)^{\ell-v}\binom{\ell}{v}n!\binom{\beta v}{n} |  |

(2.9) |  |  | = 1 ℓ! ​ ∑ v = 0 ℓ ( − 1) ℓ − v ​ ( ℓ v) ​ v n \displaystyle=\frac{1}{\ell!}\sum_{v=0}^{\ell}(-1)^{\ell-v}\binom{\ell}{v}v^{n} |  |

(2.10) |  |  | = S ⁡ ( n, ℓ). \displaystyle=S(n,\ell). |  |

The Eulerian numbers A n, k A_{n,k} have the closed form [GKP94, Equation (6.38)]

(2.11) |  | A n, ℓ \displaystyle A_{n,\ell} | = ∑ v = 0 ℓ ( − 1) ℓ − v ​ ( n + 1 ℓ − v) ​ ( v + 1) n. \displaystyle=\sum_{v=0}^{\ell}(-1)^{\ell-v}\binom{n+1}{\ell-v}(v+1)^{n}. |  |

We introduce the companion sequence of generalized Eulerian numbers

(2.12) |  | A n, ℓ ( r, s) = n! ​ ∑ v = 0 ℓ ( − 1) ℓ − v ​ ( n + 1 ℓ − v) ​ ( ( v + 1) ​ r + s n). A_{n,\ell}^{(r,s)}=n!\sum_{v=0}^{\ell}(-1)^{\ell-v}\binom{n+1}{\ell-v}\binom{(v+1)r+s}{n}. |  |

By a similar argument to the Stirling case we see that

 | lim r → ∞ A n, ℓ ( r, 0) r n = A n, ℓ. \lim_{r\to\infty}\frac{A_{n,\ell}^{(r,0)}}{r^{n}}=A_{n,\ell}. |  |

Note that if γ ≠ 0 \gamma\neq 0 or s ≠ 0 s\neq 0 we do not reduce to standard Eulerian and Stirling numbers in the large r r limit.

There are many classical relations linking Stirling numbers, sum of powers, Eulerian numbers, and Bernoulli numbers. One of the key identities linking moments, Stirling numbers, and Eulerian numbers [GKP94, Equation (7.46)] is

(2.13) |  | ( z ​ d d ​ z) n ​ 1 1 − z = ∑ ℓ = 1 ∞ ℓ n ​ z ℓ = ∑ j = 0 n j! ​ S ​ ( n, j) ​ z j ( 1 − z) j + 1 = z ( 1 − z) n + 1 ​ ∑ j = 0 n A n, j ​ z j. \left(z\frac{d}{dz}\right)^{n}\frac{1}{1-z}=\sum_{\ell=1}^{\infty}\ell^{n}z^{\ell}=\sum_{j=0}^{n}j!S(n,j)\frac{z^{j}}{(1-z)^{j+1}}=\frac{z}{(1-z)^{n+1}}\sum_{j=0}^{n}A_{n,j}z^{j}. |  |

Combining Lemma 4.5 with some further calculations gives a generalization of this transformation involving the parameters r, s r,s:

(2.14) |  | n! ∑ ℓ = 1 ∞ ( r ​ ℓ + s n) z ℓ = ∑ j = 0 n j! S ( n, j | 1, r, s) r j z j ( 1 − z) j + 1 = z ( 1 − z) n + 1 ∑ j = 0 n A n, j ( r, s) z j. \displaystyle n!\sum_{\ell=1}^{\infty}\binom{r\ell+s}{n}z^{\ell}=\sum_{j=0}^{n}j!S(n,j|1,r,s)r^{j}\frac{z^{j}}{(1-z)^{j+1}}=\frac{z}{(1-z)^{n+1}}\sum_{j=0}^{n}A_{n,j}^{(r,s)}z^{j}. |  |

The existence of this transformation is what leads to the definition of A n, j ( r, s) A_{n,j}^{(r,s)}. These definitions of generalized Stirling and Eulerian numbers suggest an analog of the classical calculus where we systematically replace powers v t v^{t} with the scaled Pochhammer t! ( β ​ v t) = ( β v) ( β v − 1) ⋯ ( β v − t + 1) t!\binom{\beta v}{t}=(\beta v)(\beta v-1)\cdots(\beta v-t+1). This introduces the free parameter β \beta, and we can recover all of the classical sequences by normalizing and taking the β → ∞ \beta\to\infty limit.

Beginning with the closed form for Bernoulli numbers [DLMF, Equation (24.6.9)]

(2.15) |  | B n = ∑ ℓ = 0 n ∑ v = 0 ℓ ( − 1) v ℓ + 1 ​ ( ℓ v) ​ v n, B_{n}=\sum_{\ell=0}^{n}\sum_{v=0}^{\ell}\frac{(-1)^{v}}{\ell+1}\binom{\ell}{v}{v^{n}}, |  |

we then define generalized Bernoulli numbers by the closed form

(2.16) |  | B n ( r, s):= n! ​ ∑ ℓ = 0 n ∑ v = 0 ℓ ( − 1) v ℓ + 1 ​ ( ℓ v) ​ ( r ​ v + s n). B_{n}^{(r,s)}:=n!\sum_{\ell=0}^{n}\sum_{v=0}^{\ell}\frac{(-1)^{v}}{\ell+1}\binom{\ell}{v}\binom{rv+s}{n}. |  |

We leave it as an open question to explore the links between these generalizations of Bernoulli, Eulerian, and Stirling numbers.

## 3. Finite differences

We will need to understand h k, r, j h_{k,r,j} in more detail, in particular its vanishing for j ≥ k ≥ r ≥ 1 j\geq k\geq r\geq 1. Using finite difference operators, we can provide an expression for h k, r, j h_{k,r,j} which sums over k − j k-j terms instead of j j terms. This gives explicit expressions for the leading coefficients of h k, r ​ ( x) h_{k,r}(x), since for example we have h k, r, k − 1 = ( − 1) r ​ 1 ( k r) h_{k,r,k-1}=(-1)^{r}\frac{1}{\binom{k}{r}} and ( − 1) k ​ h k, r, k − 2 = ( − 1) r + 1 ​ k ( k r) + ( k − 2 ​ r k) (-1)^{k}h_{k,r,k-2}=(-1)^{r+1}\frac{k}{\binom{k}{r}}+\binom{k-2r}{k}. Note the appearance of binomial coefficients with a negative upper index, defined as ( − n k) = ( − 1) k ​ ( n + k − 1 k) \binom{-n}{k}=(-1)^{k}\binom{n+k-1}{k} for k ≥ 0 k\geq 0 and any integer n n [DLMF, Equation (1.2.6)].

###### Lemma 7.

Consider integer k ≥ r ≥ 1 k\geq r\geq 1. If j ≥ k j\geq k, then h k, r, j = 0 h_{k,r,j}=0. If 1 ≤ j < k 1\leq j<k, then

(3.1) |  | h k, r, j = ( − 1) j + r + 1 ​ ( k j + 1) ( k r) + ∑ v = 2 k − j ( − 1) j + v v − 1 ​ ( k j + v) ​ ( k − r ​ v k). h_{k,r,j}=(-1)^{j+r+1}\frac{\binom{k}{j+1}}{\binom{k}{r}}+\sum_{v=2}^{k-j}\frac{(-1)^{j+v}}{v-1}\binom{k}{j+v}\binom{k-rv}{k}. |  |

###### Proof.

Define the polynomial q ⁡ ( x) = 1 x + 1 ​ ( r ​ x + k k) q(x)=\frac{1}{x+1}\binom{rx+k}{k}. For r ≤ k r\leq k the numerator contains the factor r ​ x + r rx+r which cancels with x + 1 x+1 in the denominator, so that q ⁡ ( x) q(x) is a polynomial of degree ≤ k − 1 \leq k-1. We apply the finite difference operator Δ \Delta defined by Δ ​ q ​ ( x):= q ⁡ ( x + 1) − q ⁡ ( x) \Delta q(x):=q(x+1)-q(x), which lowers the degree of a polynomial q ⁡ ( x) q(x) by 1 1. Therefore, we have the key identity

(3.2) |  | Δ k ​ q ​ ( x) = ∑ v = 0 k ( − 1) k − v ​ ( k v) ​ q ​ ( x + v) = ∑ v = 0 k ( − 1) k − v ​ ( k v) ​ 1 x + v + 1 ​ ( r ​ x + r ​ v + k k) = 0, \Delta^{k}q(x)=\sum_{v=0}^{k}(-1)^{k-v}\binom{k}{v}q(x+v)=\sum_{v=0}^{k}(-1)^{k-v}\binom{k}{v}\frac{1}{x+v+1}\binom{rx+rv+k}{k}=0, |  |

which is 0 0 because we have lowered the degree of a degree k − 1 k-1 polynomial k k times.

Consider the case j ≥ k ≥ r ≥ 1 j\geq k\geq r\geq 1. We rewrite the definition of h k, r, j h_{k,r,j} as

 | h k, r, j \displaystyle h_{k,r,j} | = ∑ v = 0 j ( − 1) j − v v + 1 ​ ( r ​ v + k k) ​ ( k j − v) \displaystyle=\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v} |  |

 |  | = ∑ v = j − k j ( − 1) j − v v + 1 ​ ( r ​ v + k k) ​ ( k j − v) \displaystyle=\sum_{v=j-k}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v} |  |

 |  | = ∑ v = 0 k ( − 1) k − v j − k + v + 1 ​ ( r ​ v + k + r ⁡ ( j − k) k) ​ ( k k − v) \displaystyle=\sum_{v=0}^{k}\frac{(-1)^{k-v}}{j-k+v+1}\binom{rv+k+r(j-k)}{k}\binom{k}{k-v} |  |

 |  | = ∑ v = 0 k ( − 1) k − v j − k + v + 1 ​ ( r ​ v + k + r ⁡ ( j − k) k) ​ ( k v). \displaystyle=\sum_{v=0}^{k}\frac{(-1)^{k-v}}{j-k+v+1}\binom{rv+k+r(j-k)}{k}\binom{k}{v}. |  |

We first truncated the sum from v = j − k ≥ 0 v=j-k\geq 0 to v = k v=k since ( k j − v) \binom{k}{j-v} vanishes outside this range. We then shifted the v v sum by j − k j-k and used the symmetry ( k k − v) = ( k v) \binom{k}{k-v}=\binom{k}{v}. Comparing against Equation ( 3.2), we see that this is exactly Δ k ​ q ​ ( x) | x = j − k = 0 \Delta^{k}q(x)|_{x=j-k}=0, since setting x = j − k ≥ 0 x=j-k\geq 0 does not lead to any singular terms.

Now consider the case k ≥ r ≥ 1 k\geq r\geq 1 and k > j ≥ 1 k>j\geq 1. Consider the limit x → − j x\to-j in Equation ( 3.2), so that the only singular term is at v = j − 1 v=j-1, where we have

 | lim x → − j ( − 1) k − j − 1 \displaystyle\lim_{x\to-j}(-1)^{k-j-1} | ( k j − 1) ​ 1 x + j ​ ( r ​ x + r ​ j + k − r k) = ( − 1) k − j − 1 ​ ( k j − 1) ​ lim x → 0 1 x ​ ( r ​ x + k − r k) \displaystyle\binom{k}{j-1}\frac{1}{x+j}\binom{rx+rj+k-r}{k}=(-1)^{k-j-1}\binom{k}{j-1}\lim_{x\to 0}\frac{1}{x}\binom{rx+k-r}{k} |  |

 |  | = ( − 1) k − j − 1 ​ ( k j − 1) ​ r k! ​ lim x → 0 ( r x + k − r) ( r x + k − r − 1) ⋯ ( r x − r + 1) r ​ x \displaystyle=(-1)^{k-j-1}\binom{k}{j-1}\frac{r}{k!}\lim_{x\to 0}\frac{(rx+k-r)(rx+k-r-1)\cdots(rx-r+1)}{rx} |  |

 |  | = ( − 1) k − j − 1 ​ ( k j − 1) ​ r k! ⋅ ( k − r)! ​ ( r − 1)! ​ ( − 1) r − 1 \displaystyle=(-1)^{k-j-1}\binom{k}{j-1}\frac{r}{k!}\cdot(k-r)!(r-1)!(-1)^{r-1} |  |

 |  | = ( − 1) k − j − r ​ ( k j − 1) ( k r). \displaystyle=(-1)^{k-j-r}\frac{\binom{k}{j-1}}{\binom{k}{r}}. |  |

The r ​ x rx terms in the numerator and denominator cancelled, so that substituting x = 0 x=0 was a well defined operation. Hence the finite difference result ( 3.2) reduces to

 | 0 = Δ k ​ q ​ ( x) | x = − j \displaystyle 0=\Delta^{k}q(x)\big|_{x=-j} | = ( − 1) k − j − r ​ ( k j − 1) ( k r) + ∑ v = 0 j − 2 ( − 1) k − v v − j + 1 ​ ( k v) ​ ( r ​ v − r ​ j + k k) + ∑ v = j k ( − 1) k − v v − j + 1 ​ ( k v) ​ ( r ​ v − r ​ j + k k) \displaystyle=(-1)^{k-j-r}\frac{\binom{k}{j-1}}{\binom{k}{r}}+\sum_{v=0}^{j-2}\frac{(-1)^{k-v}}{v-j+1}\binom{k}{v}\binom{rv-rj+k}{k}+\sum_{v=j}^{k}\frac{(-1)^{k-v}}{v-j+1}\binom{k}{v}\binom{rv-rj+k}{k} |  |

(3.3) |  |  | = ( − 1) k − j − r ​ ( k j − 1) ( k r) + h k, r, k − j + ∑ v = 0 j − 2 ( − 1) k − v v − j + 1 ​ ( k v) ​ ( r ​ v − r ​ j + k k). \displaystyle=(-1)^{k-j-r}\frac{\binom{k}{j-1}}{\binom{k}{r}}+h_{k,r,k-j}+\sum_{v=0}^{j-2}\frac{(-1)^{k-v}}{v-j+1}\binom{k}{v}\binom{rv-rj+k}{k}. |  |

Here, we rewrote h k, r, k − j h_{k,r,k-j} as

 | h k, r, k − j: \displaystyle h_{k,r,k-j}: | = ∑ v = 0 k − j ( − 1) k − j − v v + 1 ​ ( r ​ v + k k) ​ ( k k − j − v) \displaystyle=\sum_{v=0}^{k-j}\frac{(-1)^{k-j-v}}{v+1}\binom{rv+k}{k}\binom{k}{k-j-v} |  |

 |  | = ∑ v = j k ( − 1) k − v v − j + 1 ​ ( r ​ v − r ​ j + k k) ​ ( k k − v) \displaystyle=\sum_{v=j}^{k}\frac{(-1)^{k-v}}{v-j+1}\binom{rv-rj+k}{k}\binom{k}{k-v} |  |

 |  | = ∑ v = j k ( − 1) k − v v − j + 1 ​ ( r ​ v − r ​ j + k k) ​ ( k v), \displaystyle=\sum_{v=j}^{k}\frac{(-1)^{k-v}}{v-j+1}\binom{rv-rj+k}{k}\binom{k}{v}, |  |

where we shifted the summation index v v by j j, reversed the order of summation, and used the symmetry ( k k − v) = ( k v) \binom{k}{k-v}=\binom{k}{v}.

We also have

 | ∑ v = 0 j − 2 ( − 1) k − v v − j + 1 ​ ( k v) ​ ( r ​ v − r ​ j + k k) \displaystyle\sum_{v=0}^{j-2}\frac{(-1)^{k-v}}{v-j+1}\binom{k}{v}\binom{rv-rj+k}{k} | = ∑ v = 0 j − 2 ( − 1) k + j − v − ( v + 1) ​ ( k j − v − 2) ​ ( − r ​ v − 2 ​ r + k k) \displaystyle=\sum_{v=0}^{j-2}\frac{(-1)^{k+j-v}}{-(v+1)}\binom{k}{j-v-2}\binom{-rv-2r+k}{k} |  |

 |  | = ∑ v = 2 j ( − 1) k + j − v + 1 v − 1 ​ ( k j − v) ​ ( k − r ​ v k), \displaystyle=\sum_{v=2}^{j}\frac{(-1)^{k+j-v+1}}{v-1}\binom{k}{j-v}\binom{k-rv}{k}, |  |

where we reversed the order of summation and then shifted the summation over v v by 2 2. Finally, reversing j ↦ k − j j\mapsto k-j in Equation ( 3.3) and noting ( k k − j − v) = ( k j + v) \binom{k}{k-j-v}=\binom{k}{j+v} completes the proof. ∎

## 4. Entropy derivative closed forms

This section proves the closed forms for iterated entropy derivatives from Theorem 4. We begin with a fundamental infinite series expansion for the binary entropy. The key is that we consider x k ​ log ⁡ x x^{k}\log x as an analytic function around 0 0, which we do not series expand, while we series expand log ⁡ ( 1 − x k) \log(1-x^{k}).

###### Lemma 8.

For integer k ≥ 1 k\geq 1 and real 0 ≤ x ≤ 1 0\leq x\leq 1 we have the expansion

(4.1) |  | H ⁡ ( x k) = − x k ​ log ​ x k − ( 1 − x k) ​ log ⁡ ( 1 − x k) = − k ​ x k ​ log ​ x + x k − ∑ ℓ = 1 ∞ x k ⁡ ( ℓ + 1) ℓ ⁡ ( ℓ + 1). H(x^{k})=-x^{k}\log x^{k}-(1-x^{k})\log(1-x^{k})=-kx^{k}\log x+x^{k}-\sum_{\ell=1}^{\infty}\frac{x^{k(\ell+1)}}{\ell(\ell+1)}. |  |

###### Proof.

Recall that − log ⁡ ( 1 − x) = ∑ ℓ = 1 ∞ x ℓ ℓ -\log(1-x)=\sum_{\ell=1}^{\infty}\frac{x^{\ell}}{\ell} for 0 < x < 1 0<x<1. Consider the series

 | ∑ ℓ = 1 ∞ x ℓ + 1 ℓ ⁡ ( ℓ + 1) \displaystyle\sum_{\ell=1}^{\infty}\frac{x^{\ell+1}}{\ell(\ell+1)} | = ∑ ℓ = 1 ∞ x ℓ + 1 ​ ( 1 ℓ − 1 ℓ + 1) \displaystyle=\sum_{\ell=1}^{\infty}{x^{\ell+1}}\left(\frac{1}{\ell}-\frac{1}{\ell+1}\right) |  |

 |  | = x ​ ∑ ℓ = 1 ∞ x ℓ ℓ − ∑ ℓ = 2 ∞ x ℓ ℓ \displaystyle=x\sum_{\ell=1}^{\infty}\frac{x^{\ell}}{\ell}-\sum_{\ell=2}^{\infty}\frac{x^{\ell}}{\ell} |  |

 |  | = − x ​ log ⁡ ( 1 − x) + ( x + log ⁡ ( 1 − x)) \displaystyle=-x\log(1-x)+(x+\log(1-x)) |  |

 |  | = x + ( 1 − x) ​ log ⁡ ( 1 − x). \displaystyle=x+(1-x)\log(1-x). |  |

Mapping x ↦ x k x\mapsto x^{k} and substituting into the definition of H ⁡ ( x k) = − x k ​ log ⁡ x k − ( 1 − x k) ​ log ⁡ ( 1 − x k) H(x^{k})=-x^{k}\log x^{k}-(1-x^{k})\log(1-x^{k}) finishes the proof.

Note that at x = 0 x=0 this approaches H ⁡ ( 0) = 0 H(0)=0 and at x = 1 x=1 we can telescope

 | ∑ ℓ = 1 ∞ 1 ℓ ⁡ ( ℓ + 1) = ∑ ℓ = 1 ∞ ( 1 ℓ − 1 ℓ + 1) = 1, \sum_{\ell=1}^{\infty}\frac{1}{\ell(\ell+1)}=\sum_{\ell=1}^{\infty}\left(\frac{1}{\ell}-\frac{1}{\ell+1}\right)=1, |  |

so that the series converges for 0 ≤ x ≤ 1 0\leq x\leq 1. ∎

We now differentiate termwise to obtain an expression for the ( k + 1) (k+1) -st derivative.

###### Lemma 9.

For integer k ≥ r ≥ 1 k\geq r\geq 1 and real 0 < x < 1 0<x<1 we have

(4.2) |  | ( d d ​ x) k + 1 ​ x k − r ​ H ​ ( x r) \displaystyle\left(\frac{d}{dx}\right)^{k+1}x^{k-r}H(x^{r}) | = − r ⋅ k! ∑ ℓ = 0 ∞ ( k + r ​ ℓ k) 1 ℓ + 1 x r ​ ℓ − 1. \displaystyle=-r\cdot k!\sum_{\ell=0}^{\infty}\binom{k+r\ell}{k}\frac{1}{\ell+1}x^{r\ell-1}. |  |

###### Proof.

We begin with Lemma 8 in the form

(4.3) |  | x k − r ​ H ​ ( x r) = − r ​ x k ​ log ⁡ x + x k − ∑ ℓ = 1 ∞ x k + r ​ ℓ ℓ ⁡ ( ℓ + 1). x^{k-r}H(x^{r})=-rx^{k}\log x+x^{k}-\sum_{\ell=1}^{\infty}\frac{x^{k+r\ell}}{\ell(\ell+1)}. |  |

Note that

 | ( d d ​ x) k + 1 ​ x k ​ log ⁡ x = k! x \left(\frac{d}{dx}\right)^{k+1}x^{k}\log x=\frac{k!}{x} |  |

and

 | ( d d ​ x) k + 1 ​ x k + r ​ ℓ = ( k + r ​ ℓ)! ( r ​ ℓ − 1)! ​ x r ​ ℓ − 1, \left(\frac{d}{dx}\right)^{k+1}x^{k+r\ell}=\frac{(k+r\ell)!}{(r\ell-1)!}x^{r\ell-1}, |  |

so that after differentiating ( k + 1) (k+1) times termwise we have

(4.4) |  | ( d d ​ x) k + 1 ​ x k − r ​ H ​ ( x r) = − r ⋅ k! x − ∑ ℓ = 1 ∞ ( k + r ​ ℓ)! ( r ​ ℓ − 1)! ​ ( ℓ) ​ ( ℓ + 1) ​ x r ​ ℓ − 1. \displaystyle\left(\frac{d}{dx}\right)^{k+1}x^{k-r}H(x^{r})=-\frac{r\cdot k!}{x}-\sum_{\ell=1}^{\infty}\frac{(k+r\ell)!}{(r\ell-1)!(\ell)(\ell+1)}x^{r\ell-1}. |  |

Rewrite the factorials as

 | ( k + r ​ ℓ)! ( r ​ ℓ − 1)! ​ ( ℓ) ​ ( ℓ + 1) = r ⋅ k! ​ ( k + r ​ ℓ)! ( r ​ ℓ − 1)! ​ k! ​ ( r ​ ℓ) ​ ( ℓ + 1) = r ⋅ k! ​ ( k + r ​ ℓ k) ​ 1 ℓ + 1, \frac{(k+r\ell)!}{(r\ell-1)!(\ell)(\ell+1)}=r\cdot k!\frac{(k+r\ell)!}{(r\ell-1)!k!(r\ell)(\ell+1)}=r\cdot k!\binom{k+r\ell}{k}\frac{1}{\ell+1}, |  |

and then recognize − r ⋅ k! x -\frac{r\cdot k!}{x} as the ℓ = 0 \ell=0 term of the sum. The key observation is that the factorial ratio cancels nontrivially. Finally, the sum in Equation ( 4.4) becomes

 | ( d d ​ x) k + 1 ​ x k − r ​ H ​ ( x r) \displaystyle\left(\frac{d}{dx}\right)^{k+1}x^{k-r}H(x^{r}) | = − r ⋅ k! ∑ ℓ = 0 ∞ ( k + r ​ ℓ k) 1 ℓ + 1 x r ​ ℓ − 1 \displaystyle=-r\cdot k!\sum_{\ell=0}^{\infty}\binom{k+r\ell}{k}\frac{1}{\ell+1}x^{r\ell-1} |  |

and we are done. ∎

To show that the ( k + 1) (k+1) -st derivative is a rational function in x x, we consider the product with ( 1 − x r) k (1-x^{r})^{k} and show that this is a polynomial, which is not an obvious result.

###### Lemma 10.

For integer k ≥ 1 k\geq 1 and real 0 < x < 1 0<x<1 we have

 | ( d d ​ x) k + 1 x k − r H ( x r) = − r ⋅ k! x ​ ( 1 − x r) k ∑ j = 0 k − 1 x r ​ j ∑ v = 0 j ( − 1) j − v v + 1 ( r ​ v + k k) ( k j − v). \left(\frac{d}{dx}\right)^{k+1}x^{k-r}H(x^{r})=-\frac{r\cdot k!}{x(1-x^{r})^{k}}\sum_{j=0}^{k-1}x^{rj}\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v}. |  |

###### Proof.

For 0 < x < 1 0<x<1, where the entropy series converges, reindex the product

 | ( 1 − x r) k ​ ∑ ℓ = 0 ∞ ( k + r ​ ℓ k) ​ 1 ℓ + 1 ​ x r ​ ℓ \displaystyle(1-x^{r})^{k}\sum_{\ell=0}^{\infty}\binom{k+r\ell}{k}\frac{1}{\ell+1}x^{r\ell} | = ∑ m = 0 k ( − 1) m ​ ( k m) ​ x r ​ m ​ ∑ ℓ = 0 ∞ ( k + r ​ ℓ k) ​ 1 ℓ + 1 ​ x r ​ ℓ \displaystyle=\sum_{m=0}^{k}(-1)^{m}\binom{k}{m}x^{rm}\sum_{\ell=0}^{\infty}\binom{k+r\ell}{k}\frac{1}{\ell+1}x^{r\ell} |  |

 |  | = ∑ j = 0 ∞ x r ​ j ​ ∑ v = 0 j ( − 1) j − v v + 1 ​ ( k + r ​ v k) ​ ( k j − v) \displaystyle=\sum_{j=0}^{\infty}x^{rj}\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{k+rv}{k}\binom{k}{j-v} |  |

 |  | = ∑ j = 0 ∞ x r ​ j ​ h k, r, j \displaystyle=\sum_{j=0}^{\infty}x^{rj}h_{k,r,j} |  |

where we recall the definition of h k, r, j h_{k,r,j} in Equation ( 1.5). Now Lemma 7 says that for k ≥ r ≥ 1 k\geq r\geq 1 and j ≥ k j\geq k, we have h k, r, j = 0 h_{k,r,j}=0. Therefore this sum is actually a polynomial, and

 | ∑ ℓ = 0 ∞ ( k + r ​ ℓ k) ​ 1 ℓ + 1 ​ x r ​ ℓ = 1 ( 1 − x r) k ​ ∑ j = 0 k − 1 x r ​ j ​ h k, r, j. \sum_{\ell=0}^{\infty}\binom{k+r\ell}{k}\frac{1}{\ell+1}x^{r\ell}=\frac{1}{(1-x^{r})^{k}}\sum_{j=0}^{k-1}x^{rj}h_{k,r,j}. |  |

Comparing with Lemma 9 completes the proof. ∎

###### Lemma 11.

Let r, n ≥ 1 r,n\geq 1 be integers and r ≤ s ≤ n + r − 1 r\leq s\leq n+r-1 an integer. For complex w w with ℜ ⁡ ( w) < 1 \Re(w)<1 we have

(4.5) |  | ∑ ℓ = 0 ∞ w r ​ ℓ − 1 ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n ℓ! S ( n, ℓ | 1, r, s) r ℓ w r ​ ℓ − 1 ( 1 − w r) ℓ + 1 \sum_{\ell=0}^{\infty}w^{r\ell-1}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n}\ell!S(n,\ell|1,r,s)r^{\ell}\frac{w^{r\ell-1}}{(1-w^{r})^{\ell+1}} |  |

and

(4.6) |  | ∑ ℓ = 0 ∞ w r ​ ℓ − 1 ℓ + 1 ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n ℓ! S ( n, ℓ + 1 | 1, r, s − r) r ℓ + 1 w r ​ ℓ − 1 ( 1 − w r) ℓ + 1. \sum_{\ell=0}^{\infty}\frac{w^{r\ell-1}}{\ell+1}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n}\ell!S(n,\ell+1|1,r,s-r)r^{\ell+1}\frac{w^{r\ell-1}}{(1-w^{r})^{\ell+1}}. |  |

###### Proof.

We begin with the Dobiński-type formula of Equation ( 2.7):

(4.7) |  | ∑ ℓ = 0 ∞ x ℓ ℓ! ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n S ( n, ℓ | 1, r, s) r ℓ e x x ℓ. \sum_{\ell=0}^{\infty}\frac{x^{\ell}}{\ell!}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n}S(n,\ell|1,r,s)r^{\ell}e^{x}x^{\ell}. |  |

We will take Laplace transforms of both sides. Note that the Laplace transform with ℜ ⁡ ( w) > 1 \Re(w)>1 acts on monomials as

 | ∫ 0 ∞ e − w ​ x ​ x ℓ ​ 𝑑 x = ℓ! w ℓ + 1, \int_{0}^{\infty}e^{-wx}x^{\ell}dx=\frac{\ell!}{w^{\ell+1}}, |  |

so that

 | ∫ 0 ∞ e − w ​ x ​ e x ​ x ℓ ​ 𝑑 x = ℓ! ( w − 1) ℓ + 1. \int_{0}^{\infty}e^{-wx}e^{x}x^{\ell}dx=\frac{\ell!}{(w-1)^{\ell+1}}. |  |

Laplace transforming both sides gives

(4.8) |  | ∑ ℓ = 0 ∞ 1 w ℓ + 1 ​ ( r ​ ℓ + s n) \displaystyle\sum_{\ell=0}^{\infty}\frac{1}{w^{\ell+1}}\binom{r\ell+s}{n} | = 1 n! ∑ ℓ = 0 n S ( n, ℓ | 1, r, s) r ℓ ∫ 0 ∞ e ( 1 − w) ​ x x ℓ d x \displaystyle=\frac{1}{n!}\sum_{\ell=0}^{n}S(n,\ell|1,r,s)r^{\ell}\int_{0}^{\infty}e^{(1-w)x}x^{\ell}dx |  |

(4.9) |  |  | = 1 n! ∑ ℓ = 0 n S ( n, ℓ | 1, r, s) r ℓ ℓ! ( w − 1) ℓ + 1 \displaystyle=\frac{1}{n!}\sum_{\ell=0}^{n}S(n,\ell|1,r,s)r^{\ell}\frac{\ell!}{(w-1)^{\ell+1}} |  |

with ℜ ⁡ ( w) > 1 \Re(w)>1. Now mapping w ↦ 1 / w w\mapsto 1/w gives

 | ∑ ℓ = 0 ∞ w ℓ + 1 ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n ℓ! S ( n, ℓ | 1, r, s) r ℓ w ℓ + 1 ( 1 − w) ℓ + 1 \sum_{\ell=0}^{\infty}{w^{\ell+1}}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n}\ell!S(n,\ell|1,r,s)r^{\ell}\frac{w^{\ell+1}}{(1-w)^{\ell+1}} |  |

with ℜ ⁡ ( w) < 1 \Re(w)<1. Dividing by w w, mapping w ↦ w r w\mapsto w^{r}, and dividing by w w again gives the first result.

For the second result with the 1 ℓ + 1 \frac{1}{\ell+1} factor, we again begin with

 | ∑ ℓ = 0 ∞ x ℓ ℓ! ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n S ( n, ℓ | 1, r, s) r ℓ e x x ℓ, \sum_{\ell=0}^{\infty}\frac{x^{\ell}}{\ell!}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n}S(n,\ell|1,r,s)r^{\ell}e^{x}x^{\ell}, |  |

separate out the ℓ = 0 \ell=0 terms on both sides, shift ℓ \ell by 1 1, and divide through by x x:

 | ( s n) + ∑ ℓ = 1 ∞ x ℓ ℓ! ( r ​ ℓ + s n) = 1 n! S ( n, 0 | 1, r, s) e x + 1 n! ∑ ℓ = 1 n S ( n, ℓ | 1, r, s) r ℓ e x x ℓ \binom{s}{n}+\sum_{\ell=1}^{\infty}\frac{x^{\ell}}{\ell!}\binom{r\ell+s}{n}=\frac{1}{n!}S(n,0|1,r,s)e^{x}+\frac{1}{n!}\sum_{\ell=1}^{n}S(n,\ell|1,r,s)r^{\ell}e^{x}x^{\ell} |  |

and

 | 1 x ( s n) + ∑ ℓ = 0 ∞ x ℓ ( ℓ + 1)! ( r ​ ℓ + r + s n) = 1 n! S ( n, 0 | 1, r, s) e x x + 1 n! ∑ ℓ = 0 n − 1 S ( n, ℓ + 1 | 1, r, s) r ℓ + 1 e x x ℓ. \frac{1}{x}\binom{s}{n}+\sum_{\ell=0}^{\infty}\frac{x^{\ell}}{(\ell+1)!}\binom{r\ell+r+s}{n}=\frac{1}{n!}S(n,0|1,r,s)\frac{e^{x}}{x}+\frac{1}{n!}\sum_{\ell=0}^{n-1}S(n,\ell+1|1,r,s)r^{\ell+1}e^{x}x^{\ell}. |  |

Note that the Laplace transform of 1 / x 1/x does not exist, so we need both of the initial terms to drop. When 0 ≤ s < n 0\leq s<n is an integer, the binomial coefficient evaluates to 0 0 and S ( n, 0 | 1, r, s) = s ( s − 1) ⋯ ( s − n + 1) = 0 S(n,0|1,r,s)=s(s-1)\cdots(s-n+1)=0. Now Laplace transform both sides with ℜ ⁡ ( w) > 1 \Re(w)>1:

 | ∑ ℓ = 0 ∞ 1 ( ℓ + 1) ​ w ℓ + 1 ( r ​ ℓ + r + s n) = 1 n! ∑ ℓ = 0 n − 1 S ( n, ℓ + 1 | 1, r, s) r ℓ + 1 ℓ! ( w − 1) ℓ + 1. \sum_{\ell=0}^{\infty}\frac{1}{(\ell+1)w^{\ell+1}}\binom{r\ell+r+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n-1}S(n,\ell+1|1,r,s)r^{\ell+1}\frac{\ell!}{(w-1)^{\ell+1}}. |  |

Map w ↦ 1 / w w\mapsto 1/w, so ℜ ⁡ ( w) < 1 \Re(w)<1, divide by w w, and map s ↦ s − r s\mapsto s-r so that r ≤ s < n + r r\leq s<n+r:

(4.10) |  | ∑ ℓ = 0 ∞ w ℓ ℓ + 1 ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n − 1 S ( n, ℓ + 1 | 1, r, s − r) r ℓ + 1 ℓ! w ℓ ( 1 − w) ℓ + 1. \sum_{\ell=0}^{\infty}\frac{w^{\ell}}{\ell+1}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n-1}S(n,\ell+1|1,r,s-r)r^{\ell+1}\ell!\frac{w^{\ell}}{(1-w)^{\ell+1}}. |  |

Map w ↦ w r w\mapsto w^{r} and divide by w w:

 | ∑ ℓ = 0 ∞ w r ​ ℓ − 1 ℓ + 1 ( r ​ ℓ + s n) = 1 n! ∑ ℓ = 0 n − 1 ℓ! S ( n, ℓ + 1 | 1, r, s − r) r ℓ + 1 w r ​ ℓ − 1 ( 1 − w r) ℓ + 1 \sum_{\ell=0}^{\infty}\frac{w^{r\ell-1}}{\ell+1}\binom{r\ell+s}{n}=\frac{1}{n!}\sum_{\ell=0}^{n-1}\ell!S(n,\ell+1|1,r,s-r)r^{\ell+1}\frac{w^{r\ell-1}}{(1-w^{r})^{\ell+1}} |  |

to finish. ∎

An alternate proof of Lemma 10 proceeds by starting with Equation ( 4.6), clearing denominators by ( 1 − w r) n (1-w^{r})^{n}, using the binomial theorem on ( 1 − w r) n − ℓ (1-w^{r})^{n-\ell}, and inserting the closed form expression for generalized Stirling numbers from Equation ( 2.6). Then we can switch the order of summation in the triple sum and evaluate the innermost sum using a classical binomial identity to get back down to a double sum.

Combining all of these lemmas proves Theorem 4, giving closed forms for the ( k + 1) (k+1) -st derivative of x k − r ​ H ​ ( x r) x^{k-r}H(x^{r}).

## 5. Special cases

We will simplify the cases r = 1, k r=1,k which Yuster originally studied in [Yus23]. This will prove Corollaries 5 and 6. The following sequence, which has been studied many times, makes an appearance.

###### Definition 12.

Define the s s -binomial coefficients through the generating function

(5.1) |  | ∑ ℓ = 0 k ​ s ( k ℓ) s ​ x ℓ:= ( 1 + x + x 2 + ⋯ + x s) k = ( 1 − x s + 1 1 − x) k. \sum_{\ell=0}^{ks}\binom{k}{\ell}_{s}x^{\ell}:=(1+x+x^{2}+\cdots+x^{s})^{k}=\left(\frac{1-x^{s+1}}{1-x}\right)^{k}. |  |

A 1731 result of de Moivre [dM31] gives the closed form

(5.2) |  | ( k ℓ) s − 1 = ∑ v = 0 ⌊ ℓ / s ⌋ ( − 1) v ​ ( k v) ​ ( ℓ − v ​ s + k − 1 k − 1), \binom{k}{\ell}_{s-1}=\sum_{v=0}^{\left\lfloor\ell/s\right\rfloor}(-1)^{v}\binom{k}{v}\binom{\ell-vs+k-1}{k-1}, |  |

where the restriction v ≤ ⌊ ℓ / s ⌋ v\leq\left\lfloor\ell/s\right\rfloor comes from setting ℓ − s + k − 1 ≥ k − 1 \ell-s+k-1\geq k-1 so that the second binomial coefficient is positive.

We repeat the statement of Corollary 6. Equation ( 5.5) proves an observation of Yuster that the coefficients are given by OEIS sequence A108267, which is ( k ℓ ​ k) k − 1 \binom{k}{\ell k}_{k-1}.

###### Corollary 13.

Consider real 0 < x < 1 0<x<1 and ω = e 2 ​ π ​ i k \omega=e^{\frac{2\pi i}{k}} a primitive k k -th root of unity. In terms of s s -binomial coefficients defined in Definition ( 5.1),

(5.3) |  | ( d d ​ x) k + 1 ​ H ​ ( x k) \displaystyle\left(\frac{d}{dx}\right)^{k+1}H(x^{k}) | = − k ⋅ k! ∑ ℓ = 0 ∞ ( k + k ​ ℓ − 1 k − 1) x k ​ ℓ − 1 \displaystyle=-k\cdot k!\sum_{\ell=0}^{\infty}\binom{k+k\ell-1}{k-1}x^{k\ell-1} |  |

(5.4) |  |  | = − k! x ∑ j = 0 k − 1 1 ( 1 − ω j ​ x) k \displaystyle=-\frac{k!}{x}\sum_{j=0}^{k-1}\frac{1}{(1-\omega^{j}x)^{k}} |  |

(5.5) |  |  | = − k ⋅ k! x ​ ( 1 − x k) k ∑ ℓ = 0 k − 1 ( k ℓ ​ k) k − 1 x k ​ ℓ. \displaystyle=-\frac{k\cdot k!}{x(1-x^{k})^{k}}\sum_{\ell=0}^{k-1}\binom{k}{\ell k}_{k-1}x^{k\ell}. |  |

###### Proof.

Specializing Theorem 4 to r = k r=k and noting the binomial coefficient identity

 | ( k + k ​ ℓ k) ​ 1 ℓ + 1 = k + k ​ ℓ k ​ ( k + k ​ ℓ − 1 k − 1) ​ 1 ℓ + 1 = ( k + k ​ ℓ − 1 k − 1) \binom{k+k\ell}{k}\frac{1}{\ell+1}=\frac{k+k\ell}{k}\binom{k+k\ell-1}{k-1}\frac{1}{\ell+1}=\binom{k+k\ell-1}{k-1} |  |

proves Equation ( 5.3). Now let ω = e 2 ​ π ​ i / k \omega=e^{2\pi i/k} be a primitive k k -th root of unity and write

 | ( d d ​ x) k + 1 ​ H ​ ( x k) \displaystyle\left(\frac{d}{dx}\right)^{k+1}H(x^{k}) | = − k ⋅ k! x ∑ ℓ = 0 ∞ ( k + k ​ ℓ − 1 k ​ ℓ) x k ​ ℓ \displaystyle=-\frac{k\cdot k!}{x}\sum_{\ell=0}^{\infty}\binom{k+k\ell-1}{k\ell}x^{k\ell} |  |

 |  | = − k ⋅ k! x ∑ ℓ = 0 ∞ ( k + ℓ − 1 ℓ) x ℓ 𝟙 [ℓ ≡ 0 ( mod k)] \displaystyle=-\frac{k\cdot k!}{x}\sum_{\ell=0}^{\infty}\binom{k+\ell-1}{\ell}x^{\ell}\mathbbm{1}\left[\ell\equiv 0\pmod{k}\right] |  |

 |  | = − k! x ∑ ℓ = 0 ∞ x ℓ ( k + ℓ − 1 ℓ) ∑ j = 0 k − 1 ω j ​ ℓ. \displaystyle=-\frac{k!}{x}\sum_{\ell=0}^{\infty}x^{\ell}\binom{k+\ell-1}{\ell}\sum_{j=0}^{k-1}\omega^{j\ell}. |  |

We divided by k k since the inner sum along roots of unity is zero unless ℓ ≡ 0 ( mod k) \ell\equiv 0\pmod{k}, in which case it is k k. Now, we use the generalized binomial theorem to deduce Equation ( 5.4)

 | − k! x ∑ ℓ = 0 ∞ x ℓ ( k + ℓ − 1 ℓ) ∑ j = 0 k − 1 ω j ​ ℓ \displaystyle-\frac{k!}{x}\sum_{\ell=0}^{\infty}x^{\ell}\binom{k+\ell-1}{\ell}\sum_{j=0}^{k-1}\omega^{j\ell} | = − k! x ∑ j = 0 k − 1 ∑ ℓ = 0 ∞ ( k + ℓ − 1 ℓ) ( ω j x) ℓ = − k! x ∑ j = 0 k − 1 1 ( 1 − ω j ​ x) k. \displaystyle=-\frac{k!}{x}\sum_{j=0}^{k-1}\sum_{\ell=0}^{\infty}\binom{k+\ell-1}{\ell}(\omega^{j}x)^{\ell}=-\frac{k!}{x}\sum_{j=0}^{k-1}\frac{1}{(1-\omega^{j}x)^{k}}. |  |

Now note that if F ⁡ ( z) = ∑ n = 0 ∞ a n ​ z n F(z)=\sum_{n=0}^{\infty}a_{n}z^{n}, we have ∑ n = 0 ∞ a k ​ n ​ z k ​ n = 1 k ​ ∑ j = 0 k − 1 F ⁡ ( w j ​ z) \sum_{n=0}^{\infty}a_{kn}z^{kn}=\frac{1}{k}\sum_{j=0}^{k-1}{F(w^{j}z)}, where ω \omega is a primitive k k -th root of unity. Then by setting F ⁡ ( x) = ( 1 − x k 1 − x) k F(x)=\left(\frac{1-x^{k}}{1-x}\right)^{k} to be the generating function of ( k ℓ) k − 1 \binom{k}{\ell}_{k-1}, we have

(5.6) |  | ∑ ℓ = 0 k ( k k ​ ℓ) k − 1 ​ x k ​ ℓ = 1 k ​ ∑ j = 0 k − 1 ( 1 − ( ω j ​ x) k 1 − ω j ​ x) k = ( 1 − x k) k k ​ ∑ j = 0 k − 1 1 ( 1 − ω j ​ x) k, \displaystyle\sum_{\ell=0}^{k}\binom{k}{k\ell}_{k-1}x^{k\ell}=\frac{1}{k}\sum_{j=0}^{k-1}\left(\frac{1-(\omega^{j}x)^{k}}{1-\omega^{j}x}\right)^{k}=\frac{(1-x^{k})^{k}}{k}\sum_{j=0}^{k-1}\frac{1}{(1-\omega^{j}x)^{k}}, |  |

which proves Equation ( 5.5). Note that this is a multisection identity which essentially computed the Fourier expansion of the ( k − 1) (k-1) -binomial generating function. ∎

###### Corollary 14.

We have

(5.7) |  | ( d d ​ x) k + 1 ​ x k − 1 ​ H ​ ( x) = ( k − 1)! x 2 ​ ( 1 − 1 ( 1 − x) k). \left(\frac{d}{dx}\right)^{k+1}x^{k-1}H(x)=\frac{(k-1)!}{x^{2}}\left(1-\frac{1}{(1-x)^{k}}\right). |  |

###### Proof.

Consider Equation ( 1.6) with r = 1 r=1, so that

 | ( d d ​ x) k + 1 x k − 1 H ( x) = − k! ∑ ℓ = 0 ∞ ( k + ℓ k) 1 ℓ + 1 x ℓ − 1. \left(\frac{d}{dx}\right)^{k+1}x^{k-1}H(x)=-k!\sum_{\ell=0}^{\infty}\binom{k+\ell}{k}\frac{1}{\ell+1}x^{\ell-1}. |  |

Now use the generalized binomial theorem to show

 | ∑ ℓ = 0 ∞ ( k + ℓ k) ​ 1 ℓ + 1 ​ x ℓ = 1 k ​ ∑ ℓ = 0 ∞ ( k + ℓ ℓ + 1) ​ x ℓ = 1 k ​ ∑ ℓ = 1 ∞ ( k + ℓ − 1 ℓ) ​ x ℓ − 1 = 1 k ​ x ​ ( 1 ( 1 − x) k − 1), \sum_{\ell=0}^{\infty}\binom{k+\ell}{k}\frac{1}{\ell+1}x^{\ell}=\frac{1}{k}\sum_{\ell=0}^{\infty}\binom{k+\ell}{\ell+1}x^{\ell}=\frac{1}{k}\sum_{\ell=1}^{\infty}\binom{k+\ell-1}{\ell}x^{\ell-1}=\frac{1}{kx}\left(\frac{1}{(1-x)^{k}}-1\right), |  |

and we are done. ∎

## 6. Real rootedness reduction

We finally show that Conjecture 2 about real roots implies inequality ( 1.2) for real exponents.

###### Theorem 15.

The real rootedness Conjecture 2 implies the entropy inequality of Conjecture 1 for all real k ≥ 1 k\geq 1.

###### Proof.

Our proof follows the framework of [Yus23], but with the extra parameter r r. The flexibility given by the extra r r parameter is crucial to proving the reduction for real exponents, as opposed to integer exponents. Consider the function

 | f k, r ​ ( x):= α ​ H ​ ( x k) − x k − r ​ H ​ ( x r), f_{k,r}(x):=\alpha H(x^{k})-x^{k-r}H(x^{r}), |  |

where α:= α k / r \alpha:=\alpha_{k/r} satisfies the function equation ( 1.1) with parameter k / r k/r, which is equivalent to

(6.1) |  | α r = 1 ( 1 + α) k − r. \alpha^{r}=\frac{1}{(1+\alpha)^{k-r}}. |  |

We omit the subscript in α k / r \alpha_{k/r} for clarity. Our goal is to compute all roots of f k, r ​ ( x) f_{k,r}(x) in [0, 1] [0,1].

We have a trivial root at x = 1 x=1 since H ⁡ ( 1) = 0 H(1)=0.

We have a double root at 1 ( 1 + α) 1 / r \frac{1}{(1+\alpha)^{1/r}} since we can calculate that f k, r ​ ( 1 ( 1 + α) 1 / r) = f k, r ′ ​ ( 1 ( 1 + α) 1 / r) = 0 f_{k,r}\left(\frac{1}{(1+\alpha)^{1/r}}\right)=f^{\prime}_{k,r}\left(\frac{1}{(1+\alpha)^{1/r}}\right)=0. Using the symmetry H ⁡ ( x) = H ⁡ ( 1 − x) H(x)=H(1-x) and the functional equation for α \alpha, we have

 | f k, r ​ ( 1 ( 1 + α) 1 / r) \displaystyle f_{k,r}\left(\frac{1}{(1+\alpha)^{1/r}}\right) | = α ​ H ​ ( 1 ( 1 + α) k / r) − 1 ( 1 + α) k / r − 1 ​ H ​ ( 1 1 + α) \displaystyle=\alpha H\left(\frac{1}{(1+\alpha)^{k/r}}\right)-\frac{1}{(1+\alpha)^{k/r-1}}H\left(\frac{1}{1+\alpha}\right) |  |

 |  | = α ​ H ​ ( α 1 + α) − α ​ H ​ ( 1 1 + α) \displaystyle=\alpha H\left(\frac{\alpha}{1+\alpha}\right)-\alpha H\left(\frac{1}{1+\alpha}\right) |  |

 |  | = 0. \displaystyle=0. |  |

We now compute the derivative

(6.2) |  | 1 x k − r − 1 ​ d d ​ x ​ f k, r ​ ( x) = α ​ k ​ x r ​ log ⁡ ( 1 − x k x k) − k ​ x r ​ log ⁡ ( 1 − x r x r) + ( k − r) ​ log ⁡ ( 1 − x r). \displaystyle\frac{1}{x^{k-r-1}}\frac{d}{dx}f_{k,r}(x)=\alpha kx^{r}\log\left(\frac{1-x^{k}}{x^{k}}\right)-kx^{r}\log\left(\frac{1-x^{r}}{x^{r}}\right)+(k-r)\log(1-x^{r}). |  |

Using the functional equation for α \alpha several times, at x = 1 ( 1 + α) 1 / r x=\frac{1}{(1+\alpha)^{1/r}} we have

 | 1 − x r = α 1 + α, 1 − x r x r = α, 1 − x k x k = ( 1 + α) k / r − 1 = 1 + α α − 1 = 1 α. 1-x^{r}=\frac{\alpha}{1+\alpha},\quad\frac{1-x^{r}}{x^{r}}=\alpha,\quad\frac{1-x^{k}}{x^{k}}=(1+\alpha)^{k/r}-1=\frac{1+\alpha}{\alpha}-1=\frac{1}{\alpha}. |  |

Now note that

 | ( k − r) ​ log ⁡ ( α 1 + α) = k ​ log ⁡ ( α 1 + α) − log ⁡ ( α 1 + α) r = k ​ log ​ α 1 + α − log ⁡ 1 ( 1 + α) k = k ​ log ​ α. (k-r)\log\left(\frac{\alpha}{1+\alpha}\right)=k\log\left(\frac{\alpha}{1+\alpha}\right)-\log\left(\frac{\alpha}{1+\alpha}\right)^{r}=k\log\frac{\alpha}{1+\alpha}-\log\frac{1}{(1+\alpha)^{k}}=k\log\alpha. |  |

Substituting this into the derivative ( 6.2) gives

 | ( 1 + α) k − r − 1 r ​ f k, r ′ ​ ( 1 ( 1 + α) 1 / r) \displaystyle(1+\alpha)^{\frac{k-r-1}{r}}f^{\prime}_{k,r}\left(\frac{1}{(1+\alpha)^{1/r}}\right) | = k ​ α 1 + α ​ log ⁡ 1 α − k 1 + α ​ log ⁡ α + ( k − r) ​ log ⁡ ( α 1 + α) \displaystyle=k\frac{\alpha}{1+\alpha}\log\frac{1}{\alpha}-\frac{k}{1+\alpha}\log\alpha+(k-r)\log\left(\frac{\alpha}{1+\alpha}\right) |  |

 |  | = − k ​ α 1 + α ​ log ⁡ α − k 1 + α ​ log ⁡ α + k ​ log ⁡ α \displaystyle=-k\frac{\alpha}{1+\alpha}\log\alpha-\frac{k}{1+\alpha}\log\alpha+k\log\alpha |  |

 |  | = 0. \displaystyle=0. |  |

We also have a root of multiplicity k k at x = 0 x=0. Equation ( 4.3) states that

 | x k − r ​ H ​ ( x r) = − r ​ x k ​ log ⁡ x + x k − ∑ ℓ = 1 ∞ x k + r ​ ℓ ℓ ⁡ ( ℓ + 1), x^{k-r}H(x^{r})=-rx^{k}\log x+x^{k}-\sum_{\ell=1}^{\infty}\frac{x^{k+r\ell}}{\ell(\ell+1)}, |  |

so that for 0 ≤ t ≤ k − 1 0\leq t\leq k-1 we have

 | ( d d ​ x) t ​ x k − r ​ H ​ ( x r) | x = 0 \displaystyle\left(\frac{d}{dx}\right)^{t}x^{k-r}H(x^{r})\bigg|_{x=0} | = − r ​ ( d d ​ x) t ​ x k ​ log ⁡ x | x = 0. \displaystyle=-r\left(\frac{d}{dx}\right)^{t}x^{k}\log x\bigg|_{x=0}. |  |

Using the iterated product rule and separating the term at ℓ = 0 \ell=0 gives

 | ( d d ​ x) t ​ x k ​ log ⁡ x \displaystyle\left(\frac{d}{dx}\right)^{t}x^{k}\log x | = − r ∑ ℓ = 0 t ( t ℓ) ( d d ​ x) t − ℓ x k ⋅ ( d d ​ x) ℓ log x \displaystyle=-r\sum_{\ell=0}^{t}\binom{t}{\ell}\left(\frac{d}{dx}\right)^{t-\ell}x^{k}\cdot\left(\frac{d}{dx}\right)^{\ell}\log x |  |

 |  | = − r ​ k! ( k − t)! ​ x k − t ​ log ⁡ x − r ​ ∑ ℓ = 1 t ( t ℓ) ​ k! ( k − t + ℓ)! ​ x k − t + ℓ ​ ( − 1) ℓ − 1 x ℓ \displaystyle=-r\frac{k!}{(k-t)!}x^{k-t}\log x-r\sum_{\ell=1}^{t}\binom{t}{\ell}\frac{k!}{(k-t+\ell)!}x^{k-t+\ell}\frac{(-1)^{\ell-1}}{x^{\ell}} |  |

 |  | = − r ​ k! ( k − t)! ​ x k − t ​ log ⁡ x − r ​ ∑ ℓ = 1 t ( − 1) ℓ − 1 ​ ( t ℓ) ​ k! ( k − t + ℓ)! ​ x k − t. \displaystyle=-r\frac{k!}{(k-t)!}x^{k-t}\log x-r\sum_{\ell=1}^{t}(-1)^{\ell-1}\binom{t}{\ell}\frac{k!}{(k-t+\ell)!}x^{k-t}. |  |

Irrespective of the value of r r, for 0 ≤ t ≤ k − 1 0\leq t\leq k-1 we have lim x → 0 x k − t ​ log ⁡ x = 0 \lim_{x\to 0}x^{k-t}\log x=0, which in turn means that

 | ( d d ​ x) t ​ f k, r ​ ( x) | x = 0 = 0. \left(\frac{d}{dx}\right)^{t}f_{k,r}(x)\bigg|_{x=0}=0. |  |

Now, we appeal to Theorem 4, which states that

 | ( d d ​ x) k + 1 ​ f k, r ​ ( x) \displaystyle\left(\frac{d}{dx}\right)^{k+1}f_{k,r}(x) | = − α ​ k ⋅ k! x ​ ( 1 − x k) k ​ h k, k ​ ( x) + r ⋅ k! x ​ ( 1 − x r) k ​ h k, r ​ ( x) \displaystyle=-\alpha\frac{k\cdot k!}{x(1-x^{k})^{k}}h_{k,k}(x)+\frac{r\cdot k!}{x(1-x^{r})^{k}}h_{k,r}(x) |  |

 |  | = − k! x ​ ( 1 − x r) k ​ ( 1 − x k) k ​ ( α ​ k ​ ( 1 − x r) k ​ h k, k ​ ( x) − r ​ ( 1 − x k) k ​ h k, r ​ ( x)), \displaystyle=-\frac{k!}{x(1-x^{r})^{k}(1-x^{k})^{k}}\left(\alpha k(1-x^{r})^{k}h_{k,k}(x)-r(1-x^{k})^{k}h_{k,r}(x)\right), |  |

where

 | h k, r ​ ( x) = ∑ j = 0 k − 1 x r ​ j ​ ∑ v = 0 j ( − 1) j − v v + 1 ​ ( r ​ v + k k) ​ ( k j − v) h_{k,r}(x)=\sum_{j=0}^{k-1}x^{rj}\sum_{v=0}^{j}\frac{(-1)^{j-v}}{v+1}\binom{rv+k}{k}\binom{k}{j-v} |  |

as before. Now assume the conjecture that the numerator has two real roots in 0 < x < 1 0<x<1. By Rolle’s theorem applied k + 1 k+1 times to the ( k + 1) (k+1) -st derivative, it follows that f k, r ​ ( x) f_{k,r}(x) contains at most k + 3 k+3 roots in [0, 1] [0,1], counting multiplicity. We have a trivial root at x = 1 x=1, a double root at x = 1 ( 1 + α) 1 / r x=\frac{1}{(1+\alpha)^{1/r}}, and a root of multiplicity k k at x = 0 x=0. Therefore, we have found all k + 3 k+3 roots of f k, r ​ ( x) f_{k,r}(x) in [0, 1] [0,1].

Because f k, r ​ ( x) f_{k,r}(x) has a double root at 1 ( 1 + α) 1 / r \frac{1}{(1+\alpha)^{1/r}}, and the other roots are at the endpoints of the interval [0, 1] [0,1], it must be either non-positive or non-negative on [0, 1] [0,1]. Yuster [Yus23, Lemma 3.3] showed that there is a small ε \varepsilon such that f k, 1 ​ ( x) > 0 f_{k,1}(x)>0 for 0 < x < ε 0<x<\varepsilon and integers k ≥ 2 k\geq 2. The exact same proof shows that there is an ε r \varepsilon_{r} so that f k, r ​ ( x 1 / r) > 0 f_{k,r}(x^{1/r})>0 for 0 < x < ε r 0<x<\varepsilon_{r} and k / r > 1 k/r>1. Since f k, r f_{k,r} takes a positive value, it must be non-negative on [0, 1] [0,1].

Given that f k, r ​ ( x) = α k / r ​ H ​ ( x k) − x k − r ​ H ​ ( x r) ≥ 0, 0 ≤ x ≤ 1 f_{k,r}(x)=\alpha_{k/r}H(x^{k})-x^{k-r}H(x^{r})\geq 0,0\leq x\leq 1, we now map x ↦ x 1 / r x\mapsto x^{1/r}, which sends [0, 1] [0,1] to [0, 1] [0,1]. Therefore α k / r ​ H ​ ( x k / r) − x k / r − 1 ​ H ​ ( x) ≥ 0 \alpha_{k/r}H\left(x^{k/r}\right)-x^{k/r-1}H(x)\geq 0. However we picked k > r ≥ 1 k>r\geq 1 as arbitrary coprime integers, so that k / r k/r runs through all rationals greater than 1, and the inequality α q ​ H ​ ( x q) − x q − 1 ​ H ​ ( x) ≥ 0 \alpha_{q}H(x^{q})-x^{q-1}H(x)\geq 0 holds for all rational q > 1 q>1. Since each term α q, H ⁡ ( x q), x q − 1 \alpha_{q},H(x^{q}),x^{q-1} is continuous in q > 1 q>1, the inequality must also hold for all real q > 1 q>1. The inequality is also trivial at q = 1 q=1, which finishes the proof. ∎

The previous proof shows that if we can verify that p k, r ​ ( x):= α k / r ​ k ​ ( 1 − x r) k ​ h k, k ​ ( x) − r ​ ( 1 − x k) k ​ h k, r ​ ( x) p_{k,r}(x):=\alpha_{k/r}k(1-x^{r})^{k}h_{k,k}(x)-r(1-x^{k})^{k}h_{k,r}(x) has two roots in ( 0, 1) (0,1) for a fixed pair of integers k, r k,r, then we have verified inequality ( 1.2) for the rational exponent k / r k/r. For instance, at k = 3, r = 2, α 3 / 2 ≈ 0.754878, k=3,r=2,\alpha_{3/2}\approx 0.754878, this polynomial is

 | p 3, 2 ​ ( x) \displaystyle p_{3,2}(x) | = 3 ​ α 3 / 2 ​ ( − x 12 + 3 ​ x 10 − 7 ​ x 9 − 3 ​ x 8 + 21 ​ x 7 − 21 ​ x 5 + 3 ​ x 4 + 7 ​ x 3 − 3 ​ x 2 + 1) \displaystyle=3\alpha_{3/2}\left(-x^{12}+3x^{10}-7x^{9}-3x^{8}+21x^{7}-21x^{5}+3x^{4}+7x^{3}-3x^{2}+1\right) |  |

 |  | − ( 2 ​ x 13 3 − 4 ​ x 11 − 2 ​ x 10 − 2 ​ x 9 + 12 ​ x 8 + 2 ​ x 7 + 6 ​ x 6 − 12 ​ x 5 − 2 ​ x 4 3 − 6 ​ x 3 + 4 ​ x 2 + 2) \displaystyle\quad-\left(\frac{2x^{13}}{3}-4x^{11}-2x^{10}-2x^{9}+12x^{8}+2x^{7}+6x^{6}-12x^{5}-\frac{2x^{4}}{3}-6x^{3}+4x^{2}+2\right) |  |

 |  | ≈ − 2 ​ x 13 3 − 2.26 ​ x 12 + 4 ​ x 11 + 8.79 ​ x 10 − 13.85 ​ x 9 − 18.79 ​ x 8 + 45.56 ​ x 7 − 6 ​ x 6 − 35.56 ​ x 5 + 7.46 ​ x 4 \displaystyle\approx-\frac{2x^{13}}{3}-2.26x^{12}+4x^{11}+8.79x^{10}-13.85x^{9}-18.79x^{8}+45.56x^{7}-6x^{6}-35.56x^{5}+7.46x^{4} |  |

 |  | + 21.885 ​ x 3 − 10.79 ​ x 2 + 0.26, \displaystyle\quad+21.885x^{3}-10.79x^{2}+0.26, |  |

which has seven sign changes in the coefficients and is not suited to an application of Descartes’ rule of signs. Instead, we can numerically evaluate that this has two real roots in ( 0, 1) (0,1) at ≈ 0.204863, 0.74186, \approx 0.204863,0.74186, which proves the main entropy inequality ( 1.2) for the fractional exponent 3 / 2 3/2.

Alternatively, as noted in the introduction we could consider the transformed polynomial

 | ( 1 + y) k 2 + k ​ r − r ​ p k, r ​ ( 1 1 + y) = ( 1 + y) 13 \displaystyle(1+y)^{k^{2}+kr-r}p_{k,r}\left(\frac{1}{1+y}\right)=(1+y)^{13} | p 3, 2 ​ ( 1 1 + y) ≈ 0.26 ​ y 13 + 3.44 ​ y 12 + 9.85 ​ y 11 − 21.20 ​ y 10 − 178.47 ​ y 9 \displaystyle p_{3,2}\left(\frac{1}{1+y}\right)\approx 0.26y^{13}+3.44y^{12}+9.85y^{11}-21.20y^{10}-178.47y^{9} |  |

 |  | − 425.46 ​ y 8 − 507.46 ​ y 7 − 309.02 ​ y 6 − 62.01 ​ y 5 + 32.79 ​ y 4 + 19.05 ​ y 3. \displaystyle-425.46y^{8}-507.46y^{7}-309.02y^{6}-62.01y^{5}+32.79y^{4}+19.05y^{3}. |  |

The coefficients can be provably correctly computed to arbitrary accuracy using interval arithmetic, so we can read off that there are exactly two sign changes in the coefficients, which correspond to two real roots y 1, y 2 ∈ ( 0, ∞) y_{1},y_{2}\in(0,\infty) by Descartes’ rule of signs. This then corresponds to two real roots of p 3, 2 ​ ( x) p_{3,2}(x) in ( 0, 1) (0,1).

Also note that we can factor ( 1 − x) k (1-x)^{k} out of p k, r ​ ( x) p_{k,r}(x), while still leaving a polynomial. Equivalently, we can show that

 | α k / r ​ k ​ ( 1 − x r 1 − x) k ​ h k, k ​ ( x) − r ​ ( 1 − x k 1 − x) k ​ h k, r ​ ( x) \alpha_{k/r}k\left(\frac{1-x^{r}}{1-x}\right)^{k}h_{k,k}(x)-r\left(\frac{1-x^{k}}{1-x}\right)^{k}h_{k,r}(x) |  |

has two real roots in ( 0, 1) (0,1), counting multiplicity. The term ( 1 − x r 1 − x) k \left(\frac{1-x^{r}}{1-x}\right)^{k} is the generating function for ( r − 1) (r-1) -binomial coefficients given in Definition ( 5.1). The r = 1 r=1 case of this factored polynomial is exactly the polynomial p k ​ ( x) p_{k}(x) of Yuster [Yus23, Corollary 3.7] which arose in his study of inequality ( 1.2) for integer k k. The k = 2, r = 1 k=2,r=1 case is additionally the polynomial p ⁡ ( x) p(x) of Boppana [Bop23].

## 7. Functional equation

We now collect some useful properties of α k \alpha_{k}, including basic bounds and first order asymptotics. Recall that α k \alpha_{k} satisfies the functional equation ( 1.1)

 | α k = 1 ( 1 + α k) k − 1. \alpha_{k}=\frac{1}{(1+\alpha_{k})^{k-1}}. |  |

Note that the following result is tight since lim k → 1 + α k = 1 \lim_{k\to 1^{+}}\alpha_{k}=1.

###### Lemma 16.

For real k > 1 k>1, α k \alpha_{k} monotonically decreases in k k and satisfies

(7.1) |  | 1 k < α k < 1. \frac{1}{k}<\alpha_{k}<1. |  |

###### Proof.

Consider the functional equation x k + x k k = 1 x_{k}+x_{k}^{k}=1, written in terms of x k = 1 1 + α k x_{k}=\frac{1}{1+\alpha_{k}}. This is monotonic in 0 < x k < 1 0<x_{k}<1 so has a unique solution in ( 0, 1) (0,1), which corresponds to a unique value of α k \alpha_{k} in ( 0, 1) (0,1) satisfying ( 1.1). If k k increases, the power 0 < x k k < 1 0<x_{k}^{k}<1 decreases, so x k x_{k} must monotonically increase. Then α k = 1 x k − 1 \alpha_{k}=\frac{1}{x_{k}}-1 monotonically decreases. Noting that lim k → 1 + α k = 1 \lim_{k\to 1^{+}}\alpha_{k}=1 gives the upper bound.

Assume α k ≤ 1 / k \alpha_{k}\leq 1/k, then x k = 1 1 + α k ≥ k k + 1 x_{k}=\frac{1}{1+\alpha_{k}}\geq\frac{k}{k+1}. Then we apply Bernoulli’s (strict) inequality to x k + x k k ≥ k k + 1 + ( 1 − 1 k + 1) k > k k + 1 + 1 k + 1 = 1 x_{k}+x_{k}^{k}\geq\frac{k}{k+1}+\left(1-\frac{1}{k+1}\right)^{k}>\frac{k}{k+1}+\frac{1}{k+1}=1, which contradicts the functional equation x k + x k k = 1 x_{k}+x_{k}^{k}=1 and gives the lower bound. ∎

We can compute the large k k asymptotics of α k \alpha_{k}. Note that b k ≈ log ⁡ log ⁡ k b_{k}\approx\log\log k to first order, but there are multiplicative corrections of order 1 log ⁡ k, 1 log 2 ⁡ k, … \frac{1}{\log k},\frac{1}{\log^{2}k},\ldots. The point of making b k b_{k} the solution to an exact equation is that the remaining error term in Lemma 17 is much smaller.

###### Lemma 17.

Let b k b_{k} be the unique solution to

(7.2) |  | b k − log ⁡ ( 1 − b k log ⁡ k) = log ⁡ log ⁡ k. b_{k}-\log\left(1-\frac{b_{k}}{\log k}\right)=\log\log k. |  |

In the large k k limit, we have

(7.3) |  | α k \displaystyle\alpha_{k} | = log ⁡ k − b k k + O ⁡ ( log 2 ⁡ k k 2) \displaystyle=\frac{\log k-b_{k}}{k}+O\left(\frac{\log^{2}k}{k^{2}}\right) |  |

(7.4) |  |  | = log ⁡ k k + O ⁡ ( log ⁡ log ⁡ k k). \displaystyle=\frac{\log k}{k}+O\left(\frac{\log\log k}{k}\right). |  |

###### Proof.

We will do our calculations in x k = 1 1 + α k x_{k}=\frac{1}{1+\alpha_{k}}, which is the unique solution of x k + x k k = 1 x_{k}+x_{k}^{k}=1.

We will guess for now that x k = 1 − log ⁡ k − δ k x_{k}=1-\frac{\log k-\delta}{k} for δ ∈ [0, 2 ​ log ⁡ log ​ k] \delta\in[0,2\log\log k]. We will see below that there is a solution x k x_{k} of this form, which must be the unique solution. We calculate

 | log ⁡ x k \displaystyle\log x_{k} | = log ⁡ ( 1 − log ⁡ k − δ k) = − log ⁡ k − δ k + O ⁡ ( log 2 ⁡ k k 2), \displaystyle=\log\left(1-\frac{\log k-\delta}{k}\right)=-\frac{\log k-\delta}{k}+O\left(\frac{\log^{2}k}{k^{2}}\right), |  |

 | log ⁡ x k k \displaystyle\log x_{k}^{k} | = δ − log ⁡ k + O ⁡ ( log 2 ⁡ k k). \displaystyle=\delta-\log k+O\left(\frac{\log^{2}k}{k}\right). |  |

Moreover

 | log ⁡ ( 1 − x k) = log ⁡ ( log ⁡ k − δ) − log ⁡ k = log ⁡ log ⁡ k + log ⁡ ( 1 − δ log ⁡ k) − log ⁡ k. \log(1-x_{k})=\log(\log k-\delta)-\log k=\log\log k+\log\left(1-\frac{\delta}{\log k}\right)-\log k. |  |

The equation x k + x k k = 1 x_{k}+x_{k}^{k}=1 implies log ⁡ x k k = log ⁡ ( 1 − x k) \log x_{k}^{k}=\log(1-x_{k}), so

 | δ − log ⁡ k + O ⁡ ( log 2 ⁡ k k) = log ⁡ log ⁡ k + log ⁡ ( 1 − δ log ⁡ k) − log ⁡ k, \delta-\log k+O\left(\frac{\log^{2}k}{k}\right)=\log\log k+\log\left(1-\frac{\delta}{\log k}\right)-\log k, |  |

which rearranges to

 | δ − log ⁡ ( 1 − δ log ⁡ k) = log ⁡ log ⁡ k + O ⁡ ( log 2 ⁡ k k). \delta-\log\left(1-\frac{\delta}{\log k}\right)=\log\log k+O\left(\frac{\log^{2}k}{k}\right). |  |

This equation has a solution δ ∈ [0, 2 ​ log ⁡ log ​ k] \delta\in[0,2\log\log k] by the intermediate value theorem, and by inspection δ = b k + O ⁡ ( log 2 ⁡ k / k) \delta=b_{k}+O(\log^{2}k/k). Therefore

 | x k = 1 − log ⁡ k − b k + O ⁡ ( log 2 ⁡ k / k) k, x_{k}=1-\frac{\log k-b_{k}+O(\log^{2}k/k)}{k}, |  |

which implies the estimate on α k = 1 − x k x k \alpha_{k}=\frac{1-x_{k}}{x_{k}}. ∎

Finally, we can give a series expansion for x k x_{k} using Lagrange inversion. Note that the lower index of the binomial coefficient is j j, as opposed to the k ​ j kj which appears in the definition of h k, r ​ ( x) h_{k,r}(x).

###### Lemma 18.

We have the following series expansion for α k \alpha_{k}:

(7.5) |  | x k N = 1 ( 1 + α k) N = ∑ j = 0 ∞ ( − 1) j ​ N ( k − 1) ​ j + N ​ ( k ​ j + N − 1 j). x_{k}^{N}=\frac{1}{(1+\alpha_{k})^{N}}=\sum_{j=0}^{\infty}(-1)^{j}\frac{N}{(k-1)j+N}\binom{kj+N-1}{j}. |  |

###### Proof.

Rewrite the functional equation x k + x k k = 1 x_{k}+x_{k}^{k}=1 as x k = 1 1 + x k k − 1 x_{k}=\frac{1}{1+x_{k}^{k-1}}. Consider x k ​ ( z) x_{k}(z) given as the solution of

 | x k ​ ( z) = z 1 + x k ​ ( z) k − 1. x_{k}(z)=\frac{z}{1+x_{k}(z)^{k-1}}. |  |

We now perform Lagrange inversion along the variable z z in x k ​ ( z) x_{k}(z) before setting z = 1 z=1, following [Ges16, Equation (2.2.1)]. We have

 | [z n] ​ x k ​ ( z) N = N n ​ [t n − N] ​ 1 ( 1 + t k − 1) n = N n ​ [t n − N] ​ ∑ j = 0 ∞ ( n − 1 + j j) ​ ( − 1) j ​ t ( k − 1) ​ j. [z^{n}]x_{k}(z)^{N}=\frac{N}{n}\left[t^{n-N}\right]\frac{1}{(1+t^{k-1})^{n}}=\frac{N}{n}\left[t^{n-N}\right]\sum_{j=0}^{\infty}\binom{n-1+j}{j}(-1)^{j}t^{(k-1)j}. |  |

The inner coefficient is only nonzero when n − N = ( k − 1) ​ j n-N=(k-1)j, or when n = ( k − 1) ​ j + N n=(k-1)j+N for some j j. Therefore

 | x k ​ ( z) N \displaystyle x_{k}(z)^{N} | = ∑ n = 0 ∞ z n ​ N n ​ [t n − N] ​ 1 ( 1 + t k − 1) n \displaystyle=\sum_{n=0}^{\infty}z^{n}\frac{N}{n}\left[t^{n-N}\right]\frac{1}{(1+t^{k-1})^{n}} |  |

 |  | = ∑ j = 0 ∞ z ( k − 1) ​ j + N ​ N ( k − 1) ​ j + N ​ ( k ​ j + N − 1 j) ​ ( − 1) j. \displaystyle=\sum_{j=0}^{\infty}z^{(k-1)j+N}\frac{N}{(k-1)j+N}\binom{kj+N-1}{j}(-1)^{j}. |  |

Now setting z = 1 z=1 recovers x k N x_{k}^{N}. ∎

## 8. Acknowledgements

We thanks Brice Huang for his proof of the precise asymptotics of α k \alpha_{k} and Christian Krattenthaler for his introduction of finite difference operators. As always, we thank Christophe Vignat for helpful discussions.

## References

- [AHS22] Ryan Alweiss, Brice Huang, and Mark Sellke, *Improved lower bound for Frankl’s union-closed sets conjecture*, arXiv preprint arXiv:2211.11731 (2022).
- [Bop85] Ravi B. Boppana, *Amplification of probabilistic boolean formulas*, 26th Annual Symposium on Foundations of Computer Science, 1985, pp. 449–458.
- [Bop23] by same author, *A useful inequality for the binary entropy function*, arXiv preprint arXiv:2301.09664 (2023).
- [Cam22] Stijn Cambie, *Better bounds for the union-closed sets conjecture using the entropy approach*, arXiv preprint arXiv:2212.12500 (2022).
- [Cam23] by same author, *Progress on the union-closed conjecture and offsprings in winter 2022-2023*, arXiv preprint arXiv:2306.12351 (2023).
- [Cha02] Charalambos A. Charalambides, *Enumerative combinatorics*, Chapman & Hall/CRC, 2002.
- [Cig22] Johann Cigler, *Recurrences for certain sequences of binomial sums in terms of (generalized) Fibonacci and Lucas polynomials*, arXiv preprint arXiv:2212.02118 (2022).
- [CL22] Zachary Chase and Shachar Lovett, *Approximate union closed conjecture*, arXiv preprint arXiv:2211.11689 (2022).
- [COV13] Amin Coja-Oghlan and Dan Vilenchik, *Chasing the k-colorability threshold*, 2013 IEEE 54th Annual Symposium on Foundations of Computer Science, 2013, pp. 380–389.
- [DLMF]*NIST Digital Library of Mathematical Functions*, F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds.
- [dM31] A de Moivre, *Miscellanca analytica de scrichus et quadraturis*, Tomson and J. Watts, London (1731).
- [Ges16] Ira M. Gessel, *Lagrange inversion*, Journal of Combinatorial Theory, Series A 144 (2016), 212–249.
- [GKP94] Ronald L. Graham, Donald E. Knuth, and Oren Patashnik, *Concrete mathematics*, second ed., Addison-Wesley Publishing Company, Reading, MA, 1994.
- [Gou61] Henry W. Gould, *A series transformation for finding convolution identities*, Duke Math. J. 28 (1961), 193–202.
- [HS88] Leetsch C. Hsu and Peter Jau-Shyong Shiue, *A unified approach to generalized Stirling numbers*, Advances in Applied Mathematics (1988).
- [Liu24] Jingbo Liu, *Improving the lower bound for the union-closed sets conjecture via conditionally iid coupling*, 2024 58th Annual Conference on Information Sciences and Systems (CISS), IEEE, 2024, pp. 1–6.
- [MMZ06] Stephan Mertens, Marc Mézard, and Riccardo Zecchina, *Threshold values of random k-sat from the cavity method*, Random Structures & Algorithms 28 (2006), no. 3, 340–373.
- [MS16] Toufik Mansour and Matthias Schork, *Commutation relations, normal ordering, and Stirling numbers*, CRC Press, 2016.
- [Saw22] Will Sawin, *An improved lower bound for the union-closed set conjecture*, arXiv preprint arXiv:2211.11504 (2022).
- [Yu23] Lei Yu, *Dimension-free bounds for the union-closed sets conjecture*, Entropy 25 (2023), no. 5, 767.
- [Yus23] Raphael Yuster, *Almost k k -union closed set systems*, arXiv preprint arXiv:2302.12276 (2023).


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:twakhare@mit.edu
