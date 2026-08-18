<!-- source: https://arxiv.org/html/1804.05561v1 | converted from HTML -->

A new explicit formula in the additive theory of primes with applications I. The explicit formula for the Goldbach and Generalized Twin Prime Problems

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1804.05561v1 [math.NT] 16 Apr 2018

# A new explicit formula in the additive theory of primes with applications I. The explicit formula for the Goldbach and Generalized Twin Prime Problems Thanks: Supported by ERC-AdG. 321104 and National Research Development and Innovation Office, NKFIH, K 119528.

by Affiliation: János Pintz

## 1 Introduction

The well-known explicit formula of Riemann–Von Mangoldt for the number of primes up to x x ( ϱ = β + i ​ γ \varrho=\beta+i\gamma denotes non-trivial zeros of Riemann’s zeta-function, x > 2 x>2, T ≤ x T\leq x),

(1.1) |  | ψ ⁡ ( x) = ∑ n ≤ x Λ ⁡ ( n) = x − ∑ | γ | ≤ T x ρ ρ + O ⁡ ( x T ​ log 2 ​ x), \psi(x)=\sum_{n\leq x}\Lambda(n)=x-\sum_{|\gamma|\leq T}{x^{\rho}\over\rho}+O\left({x\over T}\log^{2}x\right), |  |

and the analogous ones for ψ ⁡ ( x, χ) \psi(x,\chi) [4, §19], play an important role in many problems about primes. For example, when investigating the distribution of primes in short intervals ( x, x + y) (x,x+y), we can subtract the two formulas for x x and x + y x+y and thereby reduce the problem to the density of zeros of ζ ⁡ ( s) \zeta(s).

The aim of the present work is to show that the same approach, that is, to establish an explicit formula in case of the most famous additive problems about primes (Goldbach Problem, Generalized Twin Prime Problem), is possible. The explicit formulas, once established, either lead directly to new results, or, in other cases, help to reach new results by using other methods. Another advantage of the explicit formula is that, apart from the size of the possible exceptional set in Goldbach’s problem, for example, we obtain information about the possible candidates n n for Goldbach-exceptional numbers. (We will call an even number n n a Goldbach number if it can be written as a sum of two primes, otherwise we will call it a Goldbach-exceptional number.) The same reasoning is also valid for the previously mentioned problems. We will now discuss the case of the Goldbach problem in detail.

Let E ⁡ ( X) E(X) denote the number of Goldbach-exceptional numbers up to X X. Then Goldbach’s conjecture is equivalent to E ⁡ ( X) = 1 E(X)=1 for X ≥ 2 X\geq 2. Any non-trivial upper estimate for E ⁡ ( X) E(X) can be considered as an approximation to Goldbach’s problem. After Vinogradov [26] proved his famous three primes theorem in 1937, Cudakov [3], Estermann [6] and Van der Corput [24] observed simultaneously and independently (in 1937–38) that Vinogradov’s method can also yield

(1.2) |  | E ⁡ ( X) ≪ X ​ log − A ​ X for any ​ A > 0. E(X)\ll X\log^{-A}X\quad\text{ for any }A>0. |  |

An important step was made by Vaughan [25] in 1972 with the proof of

(1.3) |  | E ⁡ ( X) ≪ X ​ exp ⁡ ( − c ​ log ⁡ X). E(X)\ll X\exp(-c\sqrt{\log X}). |  |

Later, in their pioneering work of 1975, Montgomery and Vaughan [18] established the estimate

(1.4) |  | E ⁡ ( X) ​ < X 1 − δ for ​ X > ​ X 0 ​ ( δ), E(X)<X^{1-\delta}\quad\text{ for }X>X_{0}(\delta), |  |

with a small (theoretically explicitly calculable) δ \delta and an effective X 0 ​ ( δ) X_{0}(\delta).

It turned out to be a very difficult problem to prove ( 1.4) with some reasonable (not too small) explicit value of δ \delta (even with X 0 ​ ( δ) X_{0}(\delta) ineffective). In 1989 J. R. Chen and J. M. Liu [2] proved ( 1.4) with δ = 0.05 \delta=0.05. This was improved by Hongze Li in 1999 [13] to δ = 0.079 \delta=0.079, and in 2000 [14] to

(1.5) |  | E ( X) < X 0.914 for X > X 1, an ineffective constant. E(X)<X^{0.914}\ \text{ for }X>X_{1},\text{an ineffective constant.} |  |

This was improved further by Wen Chao Lu [15] in 2010 to

(1.6) |  | E ⁡ ( X) < X 0.879 ​ for ​ X > X 2, an ineffective constant. E(X)<X^{0.879}\ \text{ for }\ X>X_{2},\ \text{ an ineffective constant.} |  |

In order to illustrate the differences in the methods of proof of ( 1.2) and ( 1.4), we define

(1.7) |  | S ⁡ ( α) = ∑ X 1 < p ≤ X log ⁡ p ​ e ​ ( α ​ p), e ⁡ ( u) = e 2 ​ π ​ i ​ u, X 1 = X 1 − ε 0, ℒ = log ⁡ X S(\alpha)=\sum_{X_{1}<p\leq X}\log pe(\alpha p),\ e(u)=e^{2\pi iu},\ X_{1}=X^{1-\varepsilon_{0}},\ \mathcal{L}=\log X |  |

with ε 0 \varepsilon_{0}, an arbitrary small positive constant.

To dissect the unit interval, we will choose a P P with

(1.8) |  | ℒ c ≤ P ≤ X, Q = X / P, ϑ = log ⁡ P log ⁡ X \mathcal{L}^{c}\leq P\leq\sqrt{X},\quad Q=X/P,\quad\vartheta=\frac{\log P}{\log X} |  |

and define the major arcs 𝔐 \mathfrak{M} as the union of the non-overlapping arcs 𝔐 ⁡ ( q, a) = [a / q − 1 / q ​ Q, a / q + 1 / q ​ Q] \mathfrak{M}(q,a)=[a/q-1/qQ,a/q+1/qQ] for q ≤ P q\leq P. Let

(1.9) |  | 𝔐 = ⋃ q ≤ P ⋃ a ( a, q) = 1 𝔐 ⁡ ( q, a), \mathfrak{M}=\bigcup_{q\leq P}\bigcup_{\begin{subarray}{c}a\\ (a,q)=1\end{subarray}}\mathfrak{M}(q,a), |  |

and denote the minor arcs by 𝔪 = [1 / Q, 1 + 1 / Q] ∖ 𝔐 {\mathfrak{m}}=[1/Q,1+1/Q]\setminus\mathfrak{M}. Then for any even m ∈ [ℒ ​ X 1, X] m\in[\mathcal{L}X_{1},X] we can write

(1.10) |  | R ⁡ ( m) = ∑ p + p ′ = m p, p ′ > X 1 log ⁡ p ⋅ log ⁡ p ′ = R 1 ​ ( m) + R 2 ​ ( m), R(m)=\sum_{\begin{subarray}{c}p+p^{\prime}=m\\ p,p^{\prime}>X_{1}\end{subarray}}\log p\cdot\log p^{\prime}=R_{1}(m)+R_{2}(m), |  |

where

(1.11) |  | R 1 ​ ( m) = ∫ 𝔐 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α, R 2 ​ ( m) = ∫ 𝔪 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α. R_{1}(m)=\int\limits_{\mathfrak{M}}S^{2}(\alpha)e(-m\alpha)d\alpha,\quad R_{2}(m)=\int\limits_{\mathfrak{m}}S^{2}(\alpha)e(-m\alpha)d\alpha. |  |

We will suppose m ∈ [X / 2, X] m\in[X/2,X] for convenience. In general, in the circle method P P is chosen to be as large as possible, with the condition that the contribution R 1 ​ ( m) R_{1}(m) can be evaluated asymptotically, yielding the expected main term

(1.12) |  | R 1 ​ ( m) ∼ 𝔖 ⁡ ( m) ⋅ I ⁡ ( m), I ⁡ ( m) = ∑ k + ℓ = m k, ℓ ∈ [X 1, X] 1 = m − 2 ​ X 1 + O ⁡ ( 1), R_{1}(m)\sim{\mathfrak{S}}(m)\cdot I(m),\quad I(m)=\sum_{\begin{subarray}{c}k+\ell=m\\ k,\ell\in[X_{1},X]\end{subarray}}1=m-2X_{1}+O(1), |  |

where

(1.13) |  | 𝔖 ⁡ ( m) = ∏ p | m ( 1 + 1 p − 1) ​ ∏ p ∤ m ( 1 − 1 ( p − 1) 2). {\mathfrak{S}}(m)=\prod_{p|m}\left(1+{1\over p-1}\right)\prod_{p\nmid m}\left(1-{1\over(p-1)^{2}}\right). |  |

In order to show ( 1.12), we usually require that primes should be uniformly distributed in all arithmetic progressions modulo q q for all q ≤ P q\leq P. Such a result, the famous Siegel–Walfisz theorem (established in 1936), played a crucial role in the proof of (1.2), and in the Goldbach–Vinogradov theorem as well. By this theorem one can choose P = ℒ A P=\mathcal{L}^{A} ( A A arbitrary large constant). After this, Vinogradov’s famous estimate for S ⁡ ( α) S(\alpha) on the minor arcs (see Lemma 4.10), combined with Parseval’s identity leads to the fact that R 2 ​ ( m) = o ⁡ ( 𝔖 ⁡ ( m) ​ m) R_{2}(m)=o({\mathfrak{S}}(m)m) for all but ℒ C ​ X / P \mathcal{L}^{C}X/P even integers m ≤ X m\leq X (see Section 5).

Montgomery–Vaughan’s ingenious idea is to choose a larger value, P = X δ P=X^{\delta}. In this case possible zeros of Dirichlet L L -functions near to the line σ = 1 \sigma=1 may destroy the uniform distribution of primes with respect to moduli less than P P. If there is no Siegel zero (see ( 4.13)–( 4.14)), then we have a statistically good distribution of primes in arithmetic progressions, the famous Gallagher prime number theorem [7, Theorem 6]. This substitutes for the uniform distribution of primes in all arithmetic progressions, therefore we may prove the (still sufficient) inequality

(1.14) |  | R 1 ​ ( m) ≫ 𝔖 ⁡ ( m) ​ m R_{1}(m)\gg{\mathfrak{S}}(m)m |  |

in place of ( 1.12).

If there is a Siegel zero, this might completely destroy the picture. This can be seen very easily, without the circle method, in the following way. Suppose, for simplicity, that we have a character χ 1 ​ mod ​ q \chi_{1}\,\text{\rm mod}\;q, where χ 1 ​ ( − 1) = − 1 \chi_{1}(-1)=-1, and L ⁡ ( 1 − δ 1, χ 1) = 0 L(1-\delta_{1},\chi_{1})=0 for a very small δ \delta. Let us consider R ⁡ ( m) R(m) (see ( 1.10)) for q | m q|m. If p + p ′ = m p+p^{\prime}=m, p ∤ q p\nmid q, then χ 1 ​ ( p) = 1 \chi_{1}(p)=1 or χ 1 ​ ( p ′) = 1 \chi_{1}(p^{\prime})=1, and so

(1.15) |  | R 1 ​ ( m) ≪ log ⁡ m ​ ∑ p ≤ m χ 1 ​ ( p) = 1 log ⁡ p ≪ log ⁡ m ⁡ ( m − m 1 − δ 1 1 − δ 1) ≪ δ 1 ​ m ​ log 2 ​ m, R_{1}(m)\ll\log m\sum_{\begin{subarray}{c}p\leq m\\ \chi_{1}(p)=1\end{subarray}}\log p\ll\log m\left(m-{m^{1-\delta_{1}}\over 1-\delta_{1}}\right)\ll\delta_{1}m\log^{2}m, |  |

which might be very small, since we can assume only δ 1 ≫ m − ε \delta_{1}\gg m^{-\varepsilon}.

Thus in case of the existence of a Siegel zero, Montgomery and Vaughan evaluate exactly the effect of the Siegel zero for R 1 ​ ( m) R_{1}(m), and they obtain for it an additional term

(1.16) |  | 𝔖 ~ ​ ( m) ​ I ~ ​ ( m), \widetilde{\mathfrak{S}}(m)\widetilde{I}(m), |  |

which may almost cancel the effect of the main term 𝔖 ⁡ ( m) ​ m {\mathfrak{S}}(m)m for many values of m m (for example, for the multiples of q q). But the cancellation cannot be complete, since [18, §6]

(1.17) |  | | 𝔖 ~ ​ ( m) | ≤ 𝔖 ⁡ ( m) (with equality possible) |\widetilde{\mathfrak{S}}(m)|\leq{\mathfrak{S}}(m)\quad\text{(with equality possible)} |  |

and

(1.18) |  | I ~ ​ ( m) = ∑ X 1 < k < X − X 1 ( k ⁡ ( m − k)) − δ 1 ≤ I ⁡ ( m) − c ​ δ 1 ​ m ​ log ⁡ m. \widetilde{I}(m)=\sum_{X_{1}<k<X-X_{1}}(k(m-k))^{-\delta_{1}}\leq I(m)-c\delta_{1}m\log m. |  |

Now, in the case of the existence of a Siegel zero, other L L -functions are free from zeros near σ = 1 \sigma=1 by the Deuring–Heilbronn phenomenon (see Lemma 4.22). Therefore, one can prove the still-sufficient inequality

(1.19) |  | R 1 ​ ( m) ≥ ( 1 + o ⁡ ( 1)) ​ 𝔖 ​ ( m) ​ ( I ⁡ ( m) − I ~ ​ ( m)) ≫ δ 1 ​ 𝔖 ​ ( m) ​ m ​ log ⁡ m. R_{1}(m)\geq(1+o(1)){\mathfrak{S}}(m)(I(m)-\widetilde{I}(m))\gg\delta_{1}{\mathfrak{S}}(m)m\log m. |  |

Our method is a generalization of the Montgomery–Vaughan method. We will choose a P P less than X 4 / 9 − η X^{4/9-\eta}, η > 0 \eta>0 arbitrary. We will introduce singular series 𝔖 ⁡ ( χ 1, χ 2, m) {\mathfrak{S}}(\chi_{1},\chi_{2},m) for every pair of primitive characters χ 1, χ 2 \chi_{1},\chi_{2} modulo r 1, r 2 r_{1},r_{2} with [r 1, r 2] ≤ P [r_{1},r_{2}]\leq P. (We consider the trivial character χ 0 ​ ( n) = 1 \chi_{0}(n)=1 as a primitive character mod ​ 1 \,\text{\rm mod}\;1.) We can evaluate these singular series and show an explicit formula for it, which implies

(1.20) |  | | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ 𝔖 ⁡ ( m), \bigl|{\mathfrak{S}}(\chi_{1},\chi_{2},m)\bigr|\leq{\mathfrak{S}}(m), |  |

and further

(1.21) |  | | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ 𝔖 ⁡ ( m) U ​ log 2 2 ​ U, \bigl|{\mathfrak{S}}(\chi_{1},\chi_{2},m)\bigr|\leq{{\mathfrak{S}}(m)\over\sqrt{U}}\log^{2}_{2}U, |  |

where

(1.22) |  | U = U ⁡ ( χ 1, χ 2, m) = max ⁡ ( r 1 2 ( r 1, r 2) 2, r 2 2 ( r 1, r 2) 2, r 1 ( | m |, r 1), r 2 ( | m |, r 2), cond ​ χ 1 ​ χ 2). U\!=\!U(\chi_{1},\chi_{2},m)\!=\!\max\left(\!{r^{2}_{1}\over(r_{1},r_{2})^{2}},{r^{2}_{2}\over(r_{1},r_{2})^{2}},{r_{1}\over(|m|,r_{1})},{r_{2}\over(|m|,r_{2})},\,\mathrm{cond}\,\chi_{1}\chi_{2}\!\right)\!. |  |

This is proved in our Main Lemma in Section 7. Further, it is shown there that the sum of the absolute values of the elements in the singular series of 𝔖 ⁡ ( χ 1, χ 2, m) {\mathfrak{S}}(\chi_{1},\chi_{2},m) will be ≤ c ​ | 𝔖 ⁡ ( χ 1, χ 2, m) | \leq c|{\mathfrak{S}}(\chi_{1},\chi_{2},m)| (not just ≤ c ​ 𝔖 ​ ( m) \leq c{\mathfrak{S}}(m), as in Lemma 5.5 of [18]).

In the same way as for I ~ ​ ( m) \widetilde{I}(m), one can evaluate the effect of any pair of zeros:

(1.23) |  | I ⁡ ( ϱ 1, ϱ 2, m) = def ∑ m = k + ℓ X 1 < k, ℓ ≤ X k ϱ 1 − 1 ​ ℓ ϱ 2 − 1 = Γ ⁡ ( ϱ 1) ​ Γ ​ ( ϱ 2) Γ ⁡ ( ϱ 1 + ϱ 2) ​ m ϱ 1 + ϱ 2 − 1 + O ⁡ ( X 1), I(\varrho_{1},\varrho_{2},m)\stackrel{{\scriptstyle\mathrm{def}}}{{=}}\sum_{\begin{subarray}{c}m=k+\ell\\ X_{1}<k,\ell\leq X\end{subarray}}k^{\varrho_{1}-1}\ell^{\varrho_{2}-1}={\Gamma(\varrho_{1})\Gamma(\varrho_{2})\over\Gamma(\varrho_{1}+\varrho_{2})}m^{\varrho_{1}+\varrho_{2}-1}+O(X_{1}), |  |

when | γ i | ≤ X 1 − ε 0 |\gamma_{i}|\leq X^{1-\varepsilon_{0}}, for example (see Lemma 4.9).

In such a way we will obtain both the main term 𝔖 ⁡ ( m) ​ I ​ ( m) {\mathfrak{S}}(m)I(m) and a uniformly bounded number of “supplementary main terms” which have the form

(1.24) |  | 𝔖 ⁡ ( χ 1, χ 2, m) ​ I ​ ( ϱ 1, ϱ 2, m) {\mathfrak{S}}(\chi_{1},\chi_{2},m)I(\varrho_{1},\varrho_{2},m) |  |

with a bounded number of possible generalized exceptional zeros ϱ ν \varrho_{\nu} belonging to L ⁡ ( s, χ ν) L(s,\chi_{\nu}) with χ ν \chi_{\nu}, ν = 1, 2, … ​ K \nu=1,2,\dots K, 0 ≤ K ≤ K 0 0\leq K\leq K_{0},

(1.25) |  | ϱ ν = 1 − δ ν + i ​ γ ν, δ ν ≤ H / ℒ, | γ ν | ≤ U, \varrho_{\nu}=1-\delta_{\nu}+i\gamma_{\nu},\quad\delta_{\nu}\leq H/\mathcal{L},\quad|\gamma_{\nu}|\leq U, |  |

where H, U H,U are large constants and K 0 = K 0 ​ ( H, U) K_{0}=K_{0}(H,U).

Using the convention that the pole ϱ 0 = 1 \varrho_{0}=1 of L ⁡ ( s, χ 0) L(s,\chi_{0}) is included with the possibly existing zeros, with the notation

(1.26) |  | A ⁡ ( ϱ) = 1 ​ if ​ ϱ = ϱ 0 = 1, χ = χ 0 ​ ( mod ​ 1) A(\varrho)=1\ \text{ if }\ \varrho=\varrho_{0}=1,\ \chi=\chi_{0}(\,\text{\rm mod}\;1) |  |

(1.27) |  | A ⁡ ( ϱ ν) = − 1 ​ if ​ L ​ ( ϱ ν, χ ν) = 0 ( ν = 1, 2, … ​ K), A(\varrho_{\nu})=-1\ \text{ if }\ L(\varrho_{\nu},\chi_{\nu})=0\quad(\nu=1,2,\dots K), |  |

we obtain the explicit formula for the contribution of the major arcs:

(1.28) |  | R 1 ​ ( m) \displaystyle R_{1}(m) | = ∑ ν = 0 K + 1 ∑ μ = 0 K + 1 A ⁡ ( ϱ ν) ​ A ​ ( ϱ μ) ​ 𝔖 ​ ( χ ν, χ μ, m) ​ I ​ ( ϱ ν, ϱ μ, m) \displaystyle=\sum^{K+1}_{\nu=0}\sum^{K+1}_{\mu=0}A(\varrho_{\nu})A(\varrho_{\mu}){\mathfrak{S}}(\chi_{\nu},\chi_{\mu},m)I(\varrho_{\nu},\varrho_{\mu},m) |  |

 |  | + O ( X e − c ​ H) + O ( X U − 1 / 2). \displaystyle\quad+O(Xe^{-cH})+O(XU^{-1/2}). |  |

This formula and the above mentioned information (cf. ( 1.20)–( 1.22)) about the properties of the generalized singular series 𝔖 ⁡ ( χ ν, χ μ, m) \mathfrak{S}(\chi_{\nu},\chi_{\mu},m), together with its analogue for the Generalized Twin Prime Problem, will have a number of arithmetic consequences, to be proven in later works. For example, we will show in later parts of this series the following

###### Theorem A.

∫ 𝔐 | S ⁡ ( α) | 2 ​ e ​ ( − m ​ α) ​ 𝑑 α = ( 1 + o ⁡ ( 1)) ​ 𝔖 ​ ( m) ​ X \int\limits_{\mathfrak{M}}|S(\alpha)|^{2}e(-m\alpha)d\alpha=(1+o(1)){\mathfrak{S}}(m)X, if m m is fixed, X → ∞ X\to\infty.

###### Theorem B.

All but O ⁡ ( X 3 / 5 ​ log 10 ​ X) O(X^{3/5}\log^{10}X) odd numbers can be written as the sum of three primes with one prime less than C C, a given absolute constant.

We can show about the gaps between consecutive Goldbach numbers

###### Theorem C.

 | ∑ g n ≤ x ( g n + 1 − g n) γ = 2 γ − 1 ​ X + O ⁡ ( X 1 − δ) ​ for ​ γ < 341 21, \sum_{g_{n}\leq x}(g_{n+1}-g_{n})^{\gamma}=2^{\gamma-1}X+O(X^{1-\delta})\ \text{ for }\gamma<{341\over 21}, |  |

where g n g_{n} is the n n -th Goldbach number.

We remark that Mikawa [16] proved the above but just for γ < 3 \gamma<3.

Descartes (1596–1650) expressed a conjecture similar to Goldbach’s one already in the 17 th century, which however appeared in a printed format as late as in 1908 [5].

###### Descartes conjecture.

Every even integer can be expressed as a sum of at most three primes.

Since in this case one of the summands has to be two, at the first sight we might think this is equivalent to the Goldbach conjecture. However, it is in fact equivalent to the assertion that for every even N N at least one of N N or N + 2 N+2 is a Goldbach number (i.e. the sum of two primes). Our new methods are able to handle such type of problems more efficiently than Goldbach’s problem (in contrast to earlier methods).

We can show for example that our present results imply

###### Theorem D.

For every ε > 0 \varepsilon>0, all but O ε ​ ( X 3 / 5 + ε) O_{\varepsilon}(X^{3/5+\varepsilon}) positive integers m ≤ X m\leq X can be written as a sum of at most three primes or prime-powers.

Theorem D will be an easy consequence of

###### Theorem E.

There are explicitly calculable absolute constants K K and C 3 C_{3} such that for all but C 3 ​ X 3 / 5 ​ log 12 ​ X C_{3}X^{3/5}\log^{12}X numbers n ≤ X n\leq X we have

(1.29) |  | E ⁡ ( n + log 2 ⁡ n) − E ⁡ ( n) ≤ K. E(n+\log^{2}n)-E(n)\leq K. |  |

The following results will also be based on the explicit formula, but their proof will require still many further ideas.

###### Theorem F.

(J. Pintz – I. Ruzsa). Every sufficiently large even integer can be written as the sum of two primes and eight powers of two.

The best published unconditional result is due to Heath-Brown and Puchta [10] with 13 13 powers of two.

###### Theorem G.

For every ε > 0 \varepsilon>0, all but O ε ​ ( X 3 / 5 + ε) O_{\varepsilon}(X^{3/5+\varepsilon}) positive integers m ≤ X m\leq X can be written as a sum of at most three primes.

###### Theorem H.

E ⁡ ( X) < X 3 / 4 E(X)<X^{3/4} for X > C X>C.

## 2 Statement of results

In order to formulate the explicit formula we need some more notation. For any χ ​ mod ​ q \chi\,\text{\rm mod}\;q let

(2.1) |  | c χ ​ ( m) = ∑ h = 1 q χ ⁡ ( h) ​ e ​ ( h ​ m q), τ ⁡ ( χ) = c χ ​ ( 1). c_{\chi}(m)=\sum^{q}_{h=1}\chi(h)e\left({hm\over q}\right),\quad\tau(\chi)=c_{\chi}(1). |  |

Further for primitive characters χ i ​ mod ​ r i \chi_{i}\,\text{\rm mod}\;r_{i} ( r i = 1 r_{i}=1 is possible), r i | q r_{i}\mid q ( i = 1, 2) (i=1,2) let

(2.2) |  | c ⁡ ( χ 1, χ 2, q, m) = φ − 2 ​ ( q) ​ c χ 1 ​ χ 2 ​ χ 0, q ​ ( − m) ​ τ ​ ( χ ¯ 1 ​ χ 0, q) ​ τ ​ ( χ ¯ 2 ​ χ 0, q), c(\chi_{1},\chi_{2},q,m)=\varphi^{-2}(q)c_{\chi_{1}\chi_{2}\chi_{0,q}}(-m)\tau(\overline{\chi}_{1}\chi_{0,q})\tau(\overline{\chi}_{2}\chi_{0,q}), |  |

(2.3) |  | 𝔖 ⁡ ( χ 1, χ 2, m) = ∑ q = 1 [r 1, r 2] | q ∞ c ⁡ ( χ 1, χ 2, q, m), {\mathfrak{S}}(\chi_{1},\chi_{2},m)=\sum^{\infty}_{\begin{subarray}{c}q=1\\ [r_{1},r_{2}]\mid q\end{subarray}}c(\chi_{1},\chi_{2},q,m), |  |

where χ 0, q \chi_{0,q} is the principal character mod ​ q \,\text{\rm mod}\;q. Let cond ​ χ \mathrm{cond}\,\chi denote the conductor of a character χ \chi.

In case of the Generalized Twin-Prime Problem we need

(2.4) |  | c ′ ​ ( χ 1, χ 2, q, m) = φ − 2 ​ ( q) ​ c χ 1 ​ χ ¯ 2 ​ χ 0, q ​ ( − m) ​ τ ​ ( χ ¯ 1 ​ χ 0, q) ​ τ ⁡ ( χ ¯ 2 ​ χ 0, q) ¯, c^{\prime}(\chi_{1},\chi_{2},q,m)=\varphi^{-2}(q)c_{\chi_{1}\overline{\chi}_{2}\chi_{0,q}}(-m)\tau(\overline{\chi}_{1}\chi_{0,q})\overline{\tau(\overline{\chi}_{2}\chi_{0,q})}, |  |

(2.5) |  | 𝔖 ′ ​ ( χ 1, χ 2, m) = ∑ q = 1 [r 1, r 2] | q ∞ c ′ ​ ( χ 1, χ 2, q, m), {\mathfrak{S}}^{\prime}(\chi_{1},\chi_{2},m)=\sum^{\infty}_{\begin{subarray}{c}q=1\\ [r_{1},r_{2}]\mid q\end{subarray}}c^{\prime}(\chi_{1},\chi_{2},q,m), |  |

(2.6) |  | R 1 ​ ( m) = ∫ 𝔐 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α, R 1 ′ ​ ( m) = ∫ 𝔐 | S 2 ​ ( α) | ​ e ​ ( − m ​ α) ​ 𝑑 α, R_{1}(m)=\int\limits_{\mathfrak{M}}S^{2}(\alpha)e(-m\alpha)d\alpha,\quad R^{\prime}_{1}(m)=\int\limits_{\mathfrak{M}}|S^{2}(\alpha)|e(-m\alpha)d\alpha, |  |

(2.7) |  | I ⁡ ( ϱ 1, ϱ 2, m) = ∑ m = k + ℓ k, ℓ ∈ ( X 1, X] k ϱ 1 − 1 ​ ℓ ϱ 2 − 1, I ′ ​ ( ϱ 1, ϱ 2, m) = ∑ m = k − ℓ k, ℓ ∈ ( X 1, X] k ϱ 1 − 1 ​ ℓ ϱ 2 ¯ − 1. I(\varrho_{1},\varrho_{2},m)=\sum_{\begin{subarray}{c}m=k+\ell\\ k,\ell\in(X_{1},X]\end{subarray}}k^{\varrho_{1}-1}\ell^{\varrho_{2}-1},\quad I^{\prime}(\varrho_{1},\varrho_{2},m)=\sum_{\begin{subarray}{c}m=k-\ell\\ k,\ell\in(X_{1},X]\end{subarray}}k^{\varrho_{1}-1}\ell^{\overline{\varrho_{2}}-1}. |  |

Let us define the set ℰ = ℰ ⁡ ( H, P, X) \mathcal{E}=\mathcal{E}(H,P,X) of generalized exceptional singularities of the functions L ′ / L L^{\prime}/L for all primitive L L -functions mod ​ r \,\text{\rm mod}\;r, r ≤ P r\leq P, as follows ( χ 0 = χ 0 ​ ( mod ​ 1) CLOSE (\chi_{0}=\chi_{0}(\,\text{\rm mod}\;1) corresponds to ζ ⁡ ( s) \zeta(s)).

(2.8) |  | ( ϱ 0, χ 0) \displaystyle(\varrho_{0},\chi_{0}) | ∈ ℰ ​ with ​ ϱ 0 = 1 \displaystyle\in\mathcal{E}\ \text{ with }\varrho_{0}=1 |  |

 | ( ϱ ν, χ ν) \displaystyle(\varrho_{\nu},\chi_{\nu}) | ∈ ℰ if ∃ χ ν ( ν ≥ 0), cond χ ν = r ν ≤ P, L ( ϱ ν, χ ν) = 0, \displaystyle\in\mathcal{E}\ \text{ if }\exists\chi_{\nu}\ (\nu\geq 0),\,\mathrm{cond}\,\chi_{\nu}=r_{\nu}\leq P,\quad L(\varrho_{\nu},\chi_{\nu})=0, |  |

 | β ν \displaystyle\beta_{\nu} | ≥ 1 − H / ℒ, | γ ν | ≤ X, \displaystyle\geq 1-H/\mathcal{L},|\gamma_{\nu}|\leq\sqrt{X}, |  |

where H H will be a sufficiently large constant to be chosen later. We remark that the best known zero-free regions for ζ ⁡ ( s) \zeta(s) exclude the possibility that ζ ⁡ ( s) \zeta(s) would have additional exceptional singularities beyond ϱ 0 = 1 \varrho_{0}=1 for sufficiently large values of X X.

Further let

 | ℰ T = { ϱ ∈ ℰ; ∣ | Im ϱ | ≤ T }. \mathcal{E}_{T}=\{\varrho\in\mathcal{E};\mid|\mathrm{Im}\varrho|\leq T\}. |  |

Let us consider a P 0 ≤ X 4 / 9 − η 0 P_{0}\leq X^{4/9-\eta_{0}} where η 0 \eta_{0} is any positive number. Every further constant or parameter, as well as ε 0 \varepsilon_{0} in the definition of X 1 X_{1} in (1.6) may depend on η 0 \eta_{0}. We suppose that X X exceeds some effective constant X 0 ​ ( η 0) X_{0}(\eta_{0}).

We can fix a sufficiently small h = h 0 h=h_{0} (depending also on η 0 \eta_{0}, and c 1 c_{1} in ( 4.14)) and introduce the

###### Definition.

We call ϱ 1 = 1 − δ 1 \varrho_{1}=1-\delta_{1}, a real zero of L ⁡ ( s, χ 1) L(s,\chi_{1}) with a real character χ 1 \chi_{1}, a Siegel zero (with respect to h h, P P and X X) if

(2.9) |  | δ 1 ≤ h / ℒ, cond ​ χ 1 ≤ P. \delta_{1}\leq h/\mathcal{L},\quad\text{cond}\,\chi_{1}\leq P. |  |

###### Remark.

If we have chosen h = h 0 h=h_{0} small enough, then in view of Lemma 4.13 we have at most one, simple Siegel zero belonging to one primitive character ( h 0 ≤ c 1 ​ ℒ / log ⁡ P) (h_{0}\leq c_{1}\mathcal{L}/\log P).

With the notation of ( 1.7)–( 1.9), ( 1.26)–( 1.27) and ( 2.1)–( 2.9) we have

###### Theorem 1.

For every P 0 ≤ X 4 / 9 − ε P_{0}\leq X^{4/9-\varepsilon} we can choose a P ∈ [P 0 ​ X − ε, P 0] P\in[P_{0}X^{-\varepsilon},P_{0}] with the following properties. We have for all m ≤ X m\leq X the explicit formulas

(2.10) |  | R 1 ​ ( m) \displaystyle R_{1}(m) | = ∑ ( ϱ i, χ i) ∈ ℰ ∑ ( ϱ j, χ j) ∈ ℰ A ⁡ ( ϱ i) ​ A ​ ( ϱ j) ​ 𝔖 ​ ( χ i, χ j, m) ​ Γ ⁡ ( ϱ i) ​ Γ ​ ( ϱ j) Γ ⁡ ( ϱ i + ϱ j) ​ m ϱ i + ϱ j − 1 \displaystyle=\sum_{(\varrho_{i},\chi_{i})\in\mathcal{E}}\sum_{(\varrho_{j},\chi_{j})\in\mathcal{E}}A(\varrho_{i})A(\varrho_{j}){\mathfrak{S}}(\chi_{i},\chi_{j},m){\Gamma(\varrho_{i})\Gamma(\varrho_{j})\over\Gamma(\varrho_{i}+\varrho_{j})}m^{\varrho_{i}+\varrho_{j}-1} |  |

 |  | + O ε ​ ( 𝔖 ⁡ ( m) ​ X ​ e − c ε ​ H) + O ε ​ ( X 1 − ε 0), \displaystyle+O_{\varepsilon}({\mathfrak{S}}(m)Xe^{-c_{\varepsilon}H})+O_{\varepsilon}(X^{1-\varepsilon_{0}}), |  |

(2.11) |  | R 1 ′ ​ ( m) \displaystyle R_{1}^{\prime}(m) | = ∑ ( ϱ i, χ i) ∈ ℰ ∑ ( ϱ j, χ j) ∈ ℰ A ⁡ ( ϱ i) ​ A ​ ( ϱ j) ​ 𝔖 ′ ​ ( χ i, χ j, m) ​ I ′ ​ ( ϱ i, ϱ j, m) \displaystyle=\sum_{(\varrho_{i},\chi_{i})\in\mathcal{E}}\sum_{(\varrho_{j},\chi_{j})\in\mathcal{E}}A(\varrho_{i})A(\varrho_{j}){\mathfrak{S}}^{\prime}(\chi_{i},\chi_{j},m)I^{\prime}(\varrho_{i},\varrho_{j},m) |  |

 |  | + O ε ​ ( 𝔖 ⁡ ( m) ​ X ​ e − c ε ​ H) + O ε ​ ( X 1 − ε 0). \displaystyle\quad+O_{\varepsilon}({\mathfrak{S}}(m)Xe^{-c_{\varepsilon}H})+O_{\varepsilon}(X^{1-\varepsilon_{0}}). |  |

Suppose additionally m ∈ [X / 4, X / 2] m\in[X/4,X/2]. Then, replacing the summation condition ( 2.10)–( 2.11) by

(2.12) |  | ∑ ( ϱ i, χ i) ∈ ℰ | γ i | ≤ U ∑ ( ϱ j, χ j) ∈ ℰ | γ j | ≤ U [r 1, r 2] ≤ P, U ⁡ ( χ 1, χ 2, m) ≤ U \underset{\hskip 14.22636pt[r_{1},r_{2}]\leq P,\hskip 8.19447ptU(\chi_{1},\chi_{2},m)\leq U}{\sum_{\begin{subarray}{c}(\varrho_{i},\chi_{i})\in\mathcal{E}\\ |\gamma_{i}|\leq U\end{subarray}}\sum_{\begin{subarray}{c}(\varrho_{j},\chi_{j})\in\mathcal{E}\\ |\gamma_{j}|\leq U\end{subarray}}} |  |

(in case of ( 2.11) U ⁡ ( χ 1, χ 2, m) U(\chi_{1},\chi_{2},m) should be replaced by U ⁡ ( χ 1, χ ¯ 2, m) U(\chi_{1},\overline{\chi}_{2},m)), we obtain ( 2.10)–( 2.11) with an additional error term

 | O ⁡ ( 𝔖 ⁡ ( m) ​ X ​ log ⁡ U / U). O({\mathfrak{S}}(m)X\log U/\sqrt{U}). |  |

Formulae ( 2.10) and ( 2.11) are quite satisfactory with respect to the error terms if there is no Siegel zero (in this case one can choose H H and U U large constants). However, this is not the case if we have a Siegel zero.

The following theorem overcomes this difficulty.

Further, in case of ( 2.13) we have for all but O ⁡ ( X 3 / 5 + ε + ε) O(X^{3/5+\varepsilon}+\varepsilon) values of m ∈ [X / 2, X] m\in[X/2,X]: R 1 ( m) ≫ ε m 1 − ε R_{1}(m)\gg_{\varepsilon}m^{1-\varepsilon}, R 1 ′ ( m) ≫ ε m 1 − ε R_{1}^{\prime}(m)\gg_{\varepsilon}m^{1-\varepsilon}.

###### Theorem 2.

Let ε > 0 \varepsilon>0 be arbitrary. If X > X ⁡ ( ε) X>X(\varepsilon), ineffective constant, and there exists a Siegel zero β 1 \beta_{1} of L ⁡ ( s, χ 1) L(s,\chi_{1}) with

(2.13) |  | β 1 > 1 − h / log ⁡ X, cond ​ χ 1 ≤ X 4 / 9 − ε, \beta_{1}>1-h/\log X,\quad\mathrm{cond}\,\chi_{1}\leq X^{4/9-\varepsilon}, |  |

where h h is a sufficiently small constant, depending on ε \varepsilon, then

(2.14) |  | E ⁡ ( X) < X 3 / 5 + ε E(X)<X^{3/5+\varepsilon} |  |

and, similarly

(2.15) |  | E ′ ( X) = | { m ≤ X; 2 ∣ m, m ≠ p − p ′ } | < X 3 / 5 + ε. E^{\prime}(X)=\big|\{m\leq X;\ 2\mid m,\ m\neq p-p^{\prime}\}\big|<X^{3/5+\varepsilon}. |  |

In view of the zero-free region for L L -functions in Lemma 4.12, Theorems 1 and 2 immediately imply

###### Theorem 3.

There are explicitly calculable positive constants C 1, c 2, C 3 C_{1},c_{2},C_{3} with the following property. If L ⁡ ( s, χ) ≠ 0 L(s,\chi)\neq 0 for

(2.16) |  | 1 − C 1 log ⁡ q ≤ σ ≤ 1 − c 2 log ⁡ q, | t | ≤ C 3, 1-{C_{1}\over\log q}\leq\sigma\leq 1-{c_{2}\over\log q},\quad|t|\leq C_{3}, |  |

then the estimates ( 2.14)–( 2.15) hold for every ε > 0 \varepsilon>0 in case of X > X ′ ​ ( ε) X>X^{\prime}(\varepsilon).

The reason for the implication is the following. If there exists a zero with σ ≥ 1 − c 2 / log ⁡ q \sigma\geq 1-c_{2}/\log q, | t | ≤ C 3 |t|\leq C_{3}, q ≤ X 4 / 9 q\leq X^{4/9}, then by Lemma 4.12 this has to be a Siegel zero. Consequently, ( 2.15) follows from Theorem 2. If, on the other hand, the whole range 1 − C 1 / log ⁡ q ≤ σ ≤ 1 1-C_{1}/\log q\leq\sigma\leq 1, | t | ≤ c 3 |t|\leq c_{3}, q ≤ X 4 / 9 q\leq X^{4/9} is zero-free, then the crucial sums in ( 2.10)–( 2.12) contain only the main term if the constants C 1 = H C_{1}=H, C 3 = U C_{3}=U were chosen sufficiently large.

In comparison we note that under the assumption of the Generalized Riemann Hypothesis (in place of the much weaker condition ( 2.16)) Hardy–Littlewood [8] proved in 1924 the estimate E ⁡ ( X) ≪ X 1 / 2 + ε E(X)\ll X^{1/2+\varepsilon}.

We remark further that one can show that Theorems 1 and 2 also imply Montgomery–Vaughan’s estimate ( 1.4).

## 3 Notation

Beyond the notation of Sections 1 and 2 (cf. ( 1.7)–( 1.13), ( 1.18), ( 1.22), ( 1.23), ( 1.25), ( 1.26)–( 1.27), ( 2.6), ( 2.8), ( 2.15)) we will use the following notation. The symbol ϱ = ϱ χ \varrho=\varrho_{\chi} will denote a zero or a pole of L ⁡ ( s, χ) L(s,\chi), where χ \chi will denote mostly primitive characters. Let

(3.1) |  | ϱ = β + i ​ γ = 1 − δ + i ​ γ, \varrho=\beta+i\gamma=1-\delta+i\gamma, |  |

(3.2) |  | N ⁡ ( α, T, χ) = ∑ ϱ = ϱ χ β ≥ α, | γ | ≤ T 1 N(\alpha,T,\chi)=\sum_{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ \beta\geq\alpha,|\gamma|\leq T\end{subarray}}1 |  |

(3.3) |  | N ∗ ​ ( α, T, Q) = ∑ q ≤ Q ∑ ∗ χ ⁡ ( q) ​ N ​ ( α, T, χ), N^{*}(\alpha,T,Q)=\sum_{q\leq Q}\underset{\chi(q)}{\sum\nolimits^{*}}N(\alpha,T,\chi), |  |

where ∑ ∗ χ ⁡ ( q) \underset{\chi(q)}{\sum\nolimits^{*}} means a summation over primitive characters mod ​ q \,\text{\rm mod}\;q. Further ∑ ′ a ⁡ ( q) \underset{a(q)}{\sum\nolimits^{\prime}} will denote summation over all reduced residue classes. Let

(3.4) |  | T ⁡ ( ϱ, η) = ∑ X 1 < n ≤ X n ϱ − 1 ​ e ​ ( n ​ η). T(\varrho,\eta)=\sum_{X_{1}<n\leq X}n^{\varrho-1}e(n\eta). |  |

Further, r ∼ R r\sim R will denote R ≤ r < 2 ​ R R\leq r<2R.

## 4 Auxiliary results

The following arithmetic results appear as Lemmas 5.1–5.4 of [18].

###### Lemma 4.1.

If χ \chi is a primitive character ( mod ​ q) (\,\text{\rm mod}\;q) then | τ ⁡ ( χ) | = q 1 / 2 |\tau(\chi)|=q^{1/2}.

###### Lemma 4.2.

Let χ \chi be a character ( mod ​ k) (\,\text{\rm mod}\;k), induced by a primitive character χ ∗ ​ ( mod ​ r) \chi^{*}(\,\text{\rm mod}\;r). Then r | k r\mid k and

(4.1) |  | τ ⁡ ( χ) = μ ⁡ ( k r) ​ χ ∗ ​ ( k r) ​ τ ​ ( χ ∗). \tau(\chi)=\mu\left({k\over r}\right)\chi^{*}\left({k\over r}\right)\tau(\chi^{*}). |  |

###### Lemma 4.3.

Suppose the above hypotheses hold, and that ( m, k) = 1 (m,k)=1. Then

(4.2) |  | c χ ​ ( m) = χ ∗ ¯ ​ ( m) ​ μ ​ ( k r) ​ χ ∗ ​ ( k r) ​ τ ​ ( χ ∗). c_{\chi}(m)=\overline{\chi^{*}}(m)\mu\left({k\over r}\right)\chi^{*}\left({k\over r}\right)\tau(\chi^{*}). |  |

###### Lemma 4.4.

Let χ \chi be a character ( mod ​ q) (\,\text{\rm mod}\;q), induced by a primitive character χ ∗ ​ ( mod ​ r) \chi^{*}(\,\text{\rm mod}\;r). For an arbitrary integer m m put q 1 = q / ( q, | m |) q_{1}=q/(q,|m|). If r ∤ q 1 r\nmid q_{1} then c χ ​ ( m) = 0 c_{\chi}(m)=0. If r | q 1 r\mid q_{1} then

(4.3) |  | c χ ​ ( m) = χ ∗ ​ ( m ( q, | m |)) ​ φ ⁡ ( q) φ ⁡ ( q 1) ​ μ ​ ( q 1 r) ​ χ ∗ ​ ( q 1 r) ​ τ ​ ( χ ∗). c_{\chi}(m)=\chi^{*}\left({m\over(q,|m|)}\right){\varphi(q)\over\varphi(q_{1})}\mu\left({q_{1}\over r}\right)\chi^{*}\left({q_{1}\over r}\right)\tau(\chi^{*}). |  |

We will use the following (mostly) well-known results from the theory of exponential sums

###### Lemma 4.5.

Let F ⁡ ( x) F(x) be a real differentiable function such that F ′ ​ ( x) F^{\prime}(x) is monotonic and F ′ ​ ( x) ≥ m > 0 F^{\prime}(x)\geq m>0, or F ′ ​ ( x) ≤ − m < 0 F^{\prime}(x)\leq-m<0, in ( a, b) (a,b). Then

(4.4) |  | | ∫ a b e i ​ F ​ ( x) ​ 𝑑 x | ≤ 4 m. \bigg|\int\limits^{b}_{a}e^{iF(x)}dx\bigg|\leq{4\over m}. |  |

This is Lemma 4.2 of Titchmarsh [23].

###### Lemma 4.6.

Let f ⁡ ( x) f(x) be a real differentiable function in ( a, b) (a,b), f ′ ​ ( x) f^{\prime}(x) monotonic, | f ′ ​ ( x) | ≤ θ < 1 |f^{\prime}(x)|\leq\theta<1. Then

(4.5) |  | ∑ a < n ≤ b e ⁡ ( f ⁡ ( n)) = ∫ a b e ⁡ ( f ⁡ ( x)) ​ 𝑑 x + O ⁡ ( 1). \sum_{a<n\leq b}e(f(n))=\int\limits^{b}_{a}e(f(x))dx+O(1). |  |

This is Lemma 4.8 of Titchmarsh [23].

###### Lemma 4.7.

Let 0 ≤ σ ≤ 1 0\leq\sigma\leq 1, | t | ≤ x |t|\leq x. Then we have uniformly

(4.6) |  | ∑ x < n ≤ N n − s = ∫ x N u − s ​ 𝑑 u + O ⁡ ( x − σ), \sum_{x<n\leq N}n^{-s}=\int\limits^{N}_{x}u^{-s}du+O(x^{-\sigma}), |  |

with an absolute constant (independent of s s too) implied by the O O symbol.

###### Proof.

This relation is contained in the proof of Theorem 4.11 of [23]. However, for this part we may allow 0 ≤ σ ≤ 1 0\leq\sigma\leq 1, since the proof follows from Lemma 4.10 of [23]. ∎

###### Lemma 4.8.

The Euler beta function B ⁡ ( u, v) B(u,v), defined below for Re ​ s > 0 \mathrm{Re}\,s>0, Re ​ w > 0 \mathrm{Re}\,w>0 satisfies the equation

(4.7) |  | B ⁡ ( s, w) ​ = def ​ ∫ 0 1 x s − 1 ​ ( 1 − x) w − 1 ​ 𝑑 x = Γ ⁡ ( s) ​ Γ ​ ( w) Γ ⁡ ( s + w). B(s,w)\overset{\mathrm{def}}{=}\int\limits^{1}_{0}x^{s-1}(1-x)^{w-1}dx={\Gamma(s)\Gamma(w)\over\Gamma(s+w)}. |  |

This can be found e.g. in Chapter 3 of [12].

The following lemma may be well known, but we did not find any exact references:

###### Lemma 4.9.

Let s = σ + i ​ t s=\sigma+it, w = λ + i ​ v w=\lambda+iv, 0 < σ 0<\sigma, λ ≤ 1 \lambda\leq 1, Y ≥ 1 Y\geq 1, max ⁡ ( | t |, | v |) ≤ Y \max(|t|,|v|)\leq Y. Then we have for any integer m ≥ 2 ​ Y m\geq 2Y

(4.8) |  | ∑ Y < k ≤ m − Y k s − 1 ​ ( m − k) w − 1 = Γ ⁡ ( s) ​ Γ ​ ( w) Γ ⁡ ( s + w) ​ m s + w − 1 + O ⁡ ( Y). \sum_{Y<k\leq m-Y}k^{s-1}(m-k)^{w-1}={\Gamma(s)\Gamma(w)\over\Gamma(s+w)}m^{s+w-1}+O(Y). |  |

###### Proof.

Let us suppose by symmetry | w | ≤ | s | |w|\leq|s| and denote

(4.9) |  | K ⁡ ( x) = ∑ Y < k ≤ x k s − 1, J ⁡ ( x) = ∫ Y x y s − 1 ​ 𝑑 y. K(x)=\sum_{Y<k\leq x}k^{s-1},\quad J(x)=\int\limits^{x}_{Y}y^{s-1}dy. |  |

Then by partial summation and integration, resp., we obtain by ( 4.6)–( 4.7) for the sum S S in ( 4.8)

(4.10) |  | S \displaystyle S | = K ⁡ ( m − Y) ​ Y w − 1 − ∫ Y m − Y K ⁡ ( u) ​ ( ( m − u) w − 1) ′ ​ 𝑑 u \displaystyle=K(m-Y)Y^{w-1}-\int\limits^{m-Y}_{Y}K(u)((m-u)^{w-1})^{\prime}du |  |

 |  | = J ⁡ ( m − Y) ​ Y w − 1 − ∫ Y m − Y J ⁡ ( u) ​ ( ( m − u) w − 1) ′ ​ 𝑑 u + O ⁡ ( 1) \displaystyle=J(m-Y)Y^{w-1}-\int\limits^{m-Y}_{Y}J(u)((m-u)^{w-1})^{\prime}du+O(1) |  |

 |  | = ∫ Y m − Y J ′ ​ ( u) ​ ( m − u) w − 1 ​ 𝑑 u + O ⁡ ( 1) \displaystyle=\int\limits^{m-Y}_{Y}J^{\prime}(u)(m-u)^{w-1}du+O(1) |  |

 |  | = ∫ 0 m u s − 1 ​ ( m − u) w − 1 ​ 𝑑 u + O ⁡ ( Y) \displaystyle=\int\limits^{m}_{0}u^{s-1}(m-u)^{w-1}du+O(Y) |  |

 |  | = Γ ⁡ ( s) ​ Γ ​ ( w) Γ ⁡ ( s + w) ​ m s + w − 1 + O ⁡ ( Y). ∎ \displaystyle={\Gamma(s)\Gamma(w)\over\Gamma(s+w)}m^{s+w-1}+O(Y).\qed |  |

Vinogradov’s famous estimate on the minor arcs was substantially simplified by Vaughan (for the proof see [4, Chapter 25]).

###### Lemma 4.10.

For | α − a / q | ≤ q − 2 |\alpha-a/q|\leq q^{-2}, ( a, q) = 1 (a,q)=1 we have

(4.11) |  | ∑ p ≤ N log p e ( p α) ≪ ( N q − 1 / 2 + N 4 / 5 + ( N q) 1 / 2) log 4 N. \sum_{p\leq N}\log pe(p\alpha)\ll(Nq^{-1/2}+N^{4/5}+(Nq)^{1/2})\log^{4}N. |  |

The following lemma of Gallagher [7, Lemma 1] makes possible the estimation of integrals for | S i 2 ​ ( α) | |S^{2}_{i}(\alpha)| (see ( 6.3)–( 6.4) via density theorems for zeros of L L -functions).

###### Lemma 4.11.

Let u 1, u 2, …, u N u_{1},u_{2},\dots,u_{N} be arbitrary real numbers. Then for any κ > 0 \kappa>0

(4.12) |  | ∫ − κ κ | ∑ u n ​ e ​ ( n ​ η) | 2 ​ 𝑑 η ≪ ∫ − ∞ ∞ | κ ​ ∑ x x + ( 2 ​ κ) − 1 u n | 2 ​ 𝑑 x. \int\limits^{\kappa}_{-\kappa}\bigg|\sum u_{n}e(n\eta)\bigg|^{2}d\eta\ll\int\limits^{\infty}_{-\infty}\bigg|\kappa\sum^{x+(2\kappa)^{-1}}_{x}u_{n}\bigg|^{2}dx. |  |

The zero-free region for L L -functions can be given by the following

###### Lemma 4.12.

Let q ≥ 1 q\geq 1 be any integer. There exists an absolute constant c 0 c_{0} such that

(4.13) |  | L ⁡ ( s, χ) ≠ 0 ​ for ​ σ > 1 − c 0 max ⁡ ( log ⁡ q, log 3 / 4 ⁡ ( | t | + 2)) L(s,\chi)\neq 0\ \text{ for }\sigma>1-{c_{0}\over\max(\log q,\log^{3/4}(|t|+2))} |  |

with the possible exception of at most one, simple real zero β 1 \beta_{1} of an L L -function corresponding to a real exceptional character χ 1 ​ mod ​ q \chi_{1}\,\text{\rm mod}\;q.

This is Satz 6.2 of Chapter VIII in [21]; the possibly existing exceptional zeros are often called Siegel zeros.

The following result is a reformulation of a theorem of Landau (for a proof see [4, §14]).

###### Lemma 4.13.

There is a constant c 1 > 0 c_{1}>0 such that there is at most one real primitive χ \chi to a modulus ≤ z \leq z for which L ⁡ ( s, χ) L(s,\chi) has a real zero β \beta satisfying

(4.14) |  | β > 1 − c 1 log ⁡ z. \beta>1-{c_{1}\over\log z}. |  |

We remark that for z z large enough, c 1 = 1 2 + o ⁡ ( 1) c_{1}=\frac{1}{2}+o(1) can be chosen [19].

Siegel’s theorem ( [4, §14]) gives an upper estimate for β \beta:

###### Lemma 4.14.

For any ε > 0 \varepsilon>0 there exists a positive ineffective constant c ⁡ ( ε) c(\varepsilon) such that if χ \chi is a real character mod ​ q \,\text{\rm mod}\;q, L ⁡ ( β, χ) = 0 L(\beta,\chi)=0, β \beta real, then

(4.15) |  | β < 1 − c ⁡ ( ε) ​ q − ε. \beta<1-c(\varepsilon)q^{-\varepsilon}. |  |

We will use the explicit formula for ψ ⁡ ( x, χ) \psi(x,\chi) in the following form.

###### Lemma 4.15.

Let χ \chi be any character mod ​ q \,\text{\rm mod}\;q, T ≥ x T\geq\sqrt{x}, x ≥ 2 x\geq 2. Let E ⁡ ( χ) = 1 E(\chi)=1 if χ = χ 0 \chi=\chi_{0}, E ⁡ ( χ) = 0 E(\chi)=0 otherwise. Then we have

(4.16) |  | ψ ⁡ ( x, χ) ​ = def ​ ∑ p ≤ x χ ⁡ ( p) ​ log ⁡ p = E ⁡ ( χ) ​ x − ∑ | γ | ≤ T β ≥ 1 / 2 x ϱ ϱ + O ⁡ ( x ​ log 2 ​ q ​ x). \psi(x,\chi)\overset{\text{\rm def}}{=}\sum_{p\leq x}\chi(p)\log p=E(\chi)x-\sum_{\begin{subarray}{c}|\gamma|\leq T\\ \beta\geq 1/2\end{subarray}}{x^{\varrho}\over\varrho}+O(\sqrt{x}\log^{2}qx). |  |

###### Proof.

It follows from formulas (7)–(8) of §19 of [4], after a trivial estimate for the contribution of prime-powers to ψ ⁡ ( x, χ) \psi(x,\chi). ∎

The following zero-density estimates for L L -functions will be used in the sequel. (In the following Q ≥ 1 Q\geq 1, T ≥ 2 T\geq 2, 1 / 2 ≤ α ≤ 1 1/2\leq\alpha\leq 1, ε > 0 \varepsilon>0 is an arbitrary positive number.)

###### Lemma 4.16.

N ∗ ​ ( α, T, Q) ≪ ( Q 2 ​ T) 3 ​ ( 1 − α) 2 − α ​ log 9 ​ Q ​ T N^{*}(\alpha,T,Q)\ll(Q^{2}T)^{3(1-\alpha)\over 2-\alpha}\log^{9}QT.

This is Theorem 12.2 of Montgomery [17].

###### Lemma 4.17.

N ∗ ( α, T, Q) ≪ ε ( Q 2 T 6 / 5) 20 9 ​ ( 1 − α) + ε N^{*}(\alpha,T,Q)\ll_{\varepsilon}(Q^{2}T^{6/5})^{{20\over 9}(1-\alpha)+\varepsilon}.

This is Theorem 2 of Heath–Brown [9].

###### Lemma 4.18.

N ∗ ( α, T, Q) ≪ ε ( Q 2 T) ( 2 + ε) ​ ( 1 − α) N^{*}(\alpha,T,Q)\ll_{\varepsilon}(Q^{2}T)^{(2+\varepsilon)(1-\alpha)} for α ≥ 4 / 5 \alpha\geq 4/5.

This is Theorem 1 of Jutila [11].

Lemmas 4.17 and 4.18 clearly imply for 1 / 2 ≤ α ≤ 1 1/2\leq\alpha\leq 1

###### Lemma 4.19.

N ∗ ​ ( α, T, Q) ≪ ( Q 2 ​ T 6 / 5) ( 20 9 + ε) ​ ( 1 − α) N^{*}(\alpha,T,Q)\ll(Q^{2}T^{6/5})^{({20\over 9}+\varepsilon)(1-\alpha)}.

The following two “log-free” density theorems were proved [19, Corollary 1 and Theorem 2].

###### Lemma 4.20.

For h < 1 / 5 h<1/5 we have

(4.17) |  | N ∗ ( 1 − h, T, Q) ≪ ε ( Q ( 3 + ε) ​ ( 3 − 4 ​ h) 4 ​ ( 1 − 4 ​ h) ​ ( 1 − 2 ​ h) T 3 + ε 2 ​ ( 1 − 4 ​ h)) h. N^{*}(1-h,T,Q)\ll_{\varepsilon}\left(Q^{(3+\varepsilon)(3-4h)\over 4(1-4h)(1-2h)}T^{3+\varepsilon\over 2(1-4h)}\right)^{h}. |  |

###### Lemma 4.21.

Let ℋ \mathcal{H} be a set of primitive characters χ \chi with moduli ≤ M \leq M, such that cond ​ χ i ​ χ j ¯ ≤ K \mathrm{cond}\,\chi_{i}\overline{\chi_{j}}\leq K for any pair χ i, χ j \chi_{i},\chi_{j} belonging to ℋ \mathcal{H}. Let 𝒮 \mathcal{S} be a set of distinct pairs ( χ j, ϱ j) (\chi_{j},\varrho_{j}) with L ⁡ ( ϱ j, χ j) = 0 L(\varrho_{j},\chi_{j})=0 where χ j ∈ ℋ \chi_{j}\in\mathcal{H}, β j ≥ 1 − h \beta_{j}\geq 1-h, | γ j | ≤ T |\gamma_{j}|\leq T. ( χ i = χ j \chi_{i}=\chi_{j} is possible, if ϱ i ≠ ϱ j \varrho_{i}\neq\varrho_{j}.) If ε \varepsilon is a sufficiently small positive constant, h < ε 3 h<\varepsilon^{3} then we have for any K ≥ 1 K\geq 1, M ≥ 1 M\geq 1, T ≥ 2 T\geq 2

(4.18) |  | | 𝒮 | ≪ ε ( K 2 ( M T) 3 / 4) ( 1 + ε) ​ h, |\mathcal{S}|\ll_{\varepsilon}\big(K^{2}(MT)^{3/4}\big)^{(1+\varepsilon)h}, |  |

and

(4.19) |  | | 𝒮 | ≪ ε ( K 2 M 2 T ε) ( 1 + ε) ​ h. |\mathcal{S}|\ll_{\varepsilon}(K^{2}M^{2}T^{\varepsilon})^{(1+\varepsilon)h}.\hskip 17.07164pt |  |

Finally the following version of the Deuring–Heilbronn phenomenon, proved in [19, Theorem 4] will be needed in case of existence of a Siegel zero (see Section 11).

###### Lemma 4.22.

Let χ 1 \chi_{1} and χ 2 \chi_{2} be primitive characters mod ​ q 1 \,\text{\rm mod}\;q_{1} and q 2 q_{2}, resp., with L ⁡ ( 1 − δ 1, χ 1) = L ⁡ ( 1 − δ + i ​ γ, χ 2) = 0 L(1-\delta_{1},\chi_{1})=L(1-\delta+i\gamma,\chi_{2})=0, where χ 1, δ 1 \chi_{1},\delta_{1} are real, δ 1 < δ < 1 / 7 \delta_{1}<\delta<1/7. Let k = cond ​ χ 1 ​ χ ¯ 2 k=\mathrm{cond}\,\chi_{1}\overline{\chi}_{2}, ε > 0 \varepsilon>0, arbitrary,

(4.20) |  | Y = ( q 1 2 ​ q 2 ​ k ​ ( | γ | + 2) 2) 3 / 8 ≥ Y 0 ​ ( ε) Y=\big(q^{2}_{1}q_{2}k(|\gamma|+2)^{2}\big)^{3/8}\geq Y_{0}(\varepsilon) |  |

sufficiently large. Then we have

(4.21) |  | δ 1 ≥ ( 1 − ε) ( 1 − 6 δ) log 2 ⋅ Y − ( 1 + ε) δ / ( 1 − 6 δ) / log Y. \delta_{1}\geq(1-\varepsilon)(1-6\delta)\log 2\cdot Y^{-(1+\varepsilon)\delta/(1-6\delta)}/\log Y. |  |

## 5 Minor arcs

The treatment of the minor arcs is completely standard. We will use the estimate of Vaughan (Lemma 4.10) on the minor arcs. This determines the value 3 / 5 3/5 in our Theorems 2 and 3.

Using Parseval’s identity we obtain from ( 1.11) and Lemma 4.10:

(5.1) |  | ∑ m R 2 2 ​ ( m) \displaystyle\sum_{m}R^{2}_{2}(m) | = ∫ 𝔪 | 𝒮 4 ​ ( α) | ​ 𝑑 α \displaystyle=\int\limits_{\mathfrak{m}}|\mathcal{S}^{4}(\alpha)|d\alpha |  |

 |  | ≤ ( max 𝔪 ⁡ | 𝒮 ⁡ ( α) |) 2 ​ ∫ 0 1 | 𝒮 ⁡ ( α) | 2 ​ 𝑑 α ≪ max ⁡ ( X 2 P, X 8 5) ​ X ​ ℒ 9. \displaystyle\leq(\max_{\mathfrak{m}}|\mathcal{S}(\alpha)|)^{2}\int\limits^{1}_{0}|\mathcal{S}(\alpha)|^{2}d\alpha\ll\max\left({X^{2}\over P},X^{8\over 5}\right)X\mathcal{L}^{9}. |  |

This result shows that for m ≤ X m\leq X we have

(5.2) |  | | R 2 ​ ( m) | ≤ X ℒ ​ with ≪ ℒ 10 ​ max ⁡ ( X P, X 3 / 5) ​ exceptions, |R_{2}(m)|\leq{X\over\sqrt{\mathcal{L}}}\ \text{ with }\ll\mathcal{L}^{10}\max\left({X\over P},X^{3/5}\right)\text{ exceptions,} |  |

(5.3) |  | | R 2 ( m) | ≤ X 1 − ε with ≪ ε max ( X 1 + 3 ​ ε P, X 3 / 5 + 3 ​ ε) exceptions. |R_{2}(m)|\leq X^{1-\varepsilon}\ \text{ with }\ll_{\varepsilon}\max\left({X^{1+3\varepsilon}\over P},X^{3/5+3\varepsilon}\right)\text{ exceptions.} |  |

The first inequality will be used if we have no Siegel zero, the second if we have one. As we can see, the exact choice of P P will be irrelevant in ( 5.2)–( 5.3) if we can choose P ≥ X 2 / 5 P\geq X^{2/5} (which will be the case in many applications).

## 6 Basic results about major arcs. Dissection of 𝑺 ⁡ ( 𝜶) S(\alpha)

We will follow [18] but extend their arguments beyond the Siegel zero to zeros near to σ = 1 \sigma=1 as well. For α ∈ 𝔐 ⁡ ( q, a) \alpha\in\mathfrak{M}(q,a) let α = a / q + η \alpha=a/q+\eta. By P < X 1 P<X_{1} we have

(6.1) |  | S ⁡ ( α) = 1 φ ⁡ ( q) ​ ∑ χ ⁡ ( q) χ ⁡ ( a) ​ τ ​ ( χ ¯) ​ S ​ ( χ, η) = 1 φ ⁡ ( q) ​ ∑ χ ⁡ ( q) χ ⁡ ( a) ​ τ ​ ( χ ¯) ​ S ​ ( χ ∗, η) S(\alpha)={1\over\varphi(q)}\sum_{\chi(q)}\chi(a)\tau(\overline{\chi})S(\chi,\eta)={1\over\varphi(q)}\sum_{\chi(q)}\chi(a)\tau(\overline{\chi})S(\chi^{*},\eta) |  |

where χ ​ mod ​ q \chi\,\text{\rm mod}\;q, q ≤ P q\leq P is induced by the primitive character χ ∗ \chi^{*}, and S ⁡ ( χ, η) S(\chi,\eta) is defined by

(6.2) |  | S ⁡ ( χ, η) = 1 φ ⁡ ( q) ​ ∑ X 1 < p ≤ X χ ⁡ ( p) ​ log ⁡ p ​ e ​ ( η ​ p). S(\chi,\eta)=\frac{1}{\varphi(q)}\sum_{X_{1}<p\leq X}\chi(p)\log pe(\eta p). |  |

Using the (unusual) notation of Section 1, we can separate from S ⁡ ( χ ∗, η) S(\chi^{*},\eta) the effect of the main term T 0 ​ ( η) T_{0}(\eta) ‘caused’ by the pole of L ⁡ ( s, χ 0) = ζ ⁡ ( s) L(s,\chi_{0})=\zeta(s) at s = 1 s=1 and that of the zeros ϱ \varrho lying near to σ = 1 \sigma=1 (for all L ⁡ ( s, χ) L(s,\chi)). Up to the different sign A ⁡ ( ϱ) A(\varrho) (see ( 1.26)–( 1.27)) their treatment will be the same. Accordingly we write

(6.3) |  | S 1 ​ ( α) = S ⁡ ( α) − S 0 ​ ( α), S 0 ​ ( α) = S 2 ​ ( α) + S 3 ​ ( α), S_{1}(\alpha)=S(\alpha)-S_{0}(\alpha),\quad S_{0}(\alpha)=S_{2}(\alpha)+S_{3}(\alpha), |  |

where we define S 2 ​ ( α) S_{2}(\alpha) and S 3 ​ ( α) S_{3}(\alpha) (and thus S 1 ​ ( α) S_{1}(\alpha) and S 0 ​ ( α) S_{0}(\alpha)) through ( 6.1) and S i ​ ( χ, η) S_{i}(\chi,\eta) ( 0 ≤ i ≤ 3) (0\leq i\leq 3) by

(6.4) |  | S 2 ​ ( χ ∗, η) \displaystyle S_{2}(\chi^{*},\eta) | = ∑ ϱ = ϱ χ H / ℒ < δ ≤ b, | γ | ≤ X A ⁡ ( ϱ) ​ T ​ ( ϱ, η), \displaystyle=\sum_{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ H/\mathcal{L}<\delta\leq b,\ |\gamma|\leq\sqrt{X}\end{subarray}}A(\varrho)T(\varrho,\eta), |  |

 | S 3 ​ ( χ ∗, η) \displaystyle S_{3}(\chi^{*},\eta) | = ∑ ϱ = ϱ χ 0 ≤ δ ≤ H / ℒ, | γ | ≤ X A ⁡ ( ϱ) ​ T ​ ( ϱ, η) \displaystyle=\sum_{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ 0\leq\delta\leq H/\mathcal{L},\ |\gamma|\leq\sqrt{X}\end{subarray}}A(\varrho)T(\varrho,\eta) |  |

where in case of the principal character the pole ϱ = 1 \varrho=1 with A ⁡ ( ϱ) = 1 A(\varrho)=1 is included, b = b ⁡ ( η 0) b=b(\eta_{0}) is a small constant, and for a zero ϱ \varrho we have A ⁡ ( ϱ) = − 1 A(\varrho)=-1. We remark that S i ​ ( χ, η) = S i ​ ( χ ∗, η) S_{i}(\chi,\eta)=S_{i}(\chi^{*},\eta). Then we have

(6.5) |  |  | ∑ q ≤ P ∑ ′ a ⁡ ( q) ​ ∫ 𝔐 ( q, a) S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α \displaystyle\sum_{q\leq P}\underset{a(q)}{\sum\nolimits^{\prime}}\,\int\limits_{\mathfrak{M}_{(q,a)}}S^{2}(\alpha)e(-m\alpha)d\alpha |  |

 |  | = ∑ q ≤ P ∑ ′ a ⁡ ( q) ∑ χ ⁡ ( q) ∑ χ ′ ​ ( q) χ χ ′ ( a) τ ( χ ¯) τ ( χ ¯ ′) e ( − a m / q) φ 2 ​ ( q) ∫ − 1 / q Q 1 / q ​ Q S ( χ, η) S ( χ ′, η) e ( − m η) d η \displaystyle=\!\sum_{q\leq P}\underset{a(q)}{\sum\nolimits^{\prime}}\sum_{\chi(q)}\sum_{\chi^{\prime}(q)}\!{\chi\chi^{\prime}(a)\tau(\overline{\chi})\tau(\overline{\chi}^{\prime})e(-am/q)\over\varphi^{2}(q)}\!\int\limits^{1/qQ}_{-1/qQ}\!\!S(\chi,\eta)S(\chi^{\prime},\eta)e(-m\eta)d\eta |  |

 |  | = ∑ q ≤ P ∑ χ ⁡ ( q) ∑ χ ′ ​ ( q) c χ ​ χ ′ ​ ( − m) ​ τ ​ ( χ ¯) ​ τ ​ ( χ ¯ ′) φ 2 ​ ( q) ∫ − 1 / q Q 1 / q ​ Q S ( χ, η) S ( χ ′, η) e ( − m η) d η \displaystyle=\sum_{q\leq P}\sum_{\chi(q)}\sum_{\chi^{\prime}(q)}{c_{\chi\chi^{\prime}}(-m)\tau(\overline{\chi})\tau(\overline{\chi}^{\prime})\over\varphi^{2}(q)}\int\limits^{1/qQ}_{-1/qQ}S(\chi,\eta)S(\chi^{\prime},\eta)e(-m\eta)d\eta |  |

 |  | = def ∑ ∗ χ r ⁡ ( χ) ≤ P ∑ ∗ χ ′ r ⁡ ( χ ′) ≤ P ∑ q ≤ P [r ⁡ ( χ), r ⁡ ( χ ′)] | q c ( χ, χ ′, q, m) ∫ − 1 / q Q 1 / q ​ Q S ( χ, η) S ( χ ′, η) e ( − m η) d η. \displaystyle\overset{\rm def}{=}\underset{\begin{subarray}{c}\chi\\ r(\chi)\leq P\end{subarray}}{\sum\nolimits^{*}}\underset{\begin{subarray}{c}\chi^{\prime}\\ r(\chi^{\prime})\leq P\end{subarray}}{\sum\nolimits^{*}}\sum_{\begin{subarray}{c}q\leq P\\ [r(\chi),r(\chi^{\prime})]\mid q\end{subarray}}c(\chi,\chi^{\prime},q,m)\int\limits^{1/qQ}_{-1/qQ}S(\chi,\eta)S(\chi^{\prime},\eta)e(-m\eta)d\eta. |  |

Naturally the same formula holds if we replace S ⁡ ( α) S(\alpha) and S ⁡ ( χ, η) S(\chi,\eta) by S i ​ ( α) S_{i}(\alpha) and S i ​ ( χ, η) S_{i}(\chi,\eta), respectively ( 0 ≤ i ≤ 3) (0\leq i\leq 3).

The estimate of these integrals will be performed by the aid of Gallagher’s Lemma 4.11 through the estimates of the quantities ( χ \chi primitive mod ​ r \,\text{\rm mod}\;r)

(6.6) |  | W i ( χ):= ( ∫ − 1 / r Q 1 / r ​ Q | S i ( χ, η) | 2 d η) 1 / 2. W_{i}(\chi):=\biggl(\int\limits_{-1/rQ}^{1/rQ}\bigl|S_{i}(\chi,\eta)\bigr|^{2}d\eta\biggr)^{1/2}. |  |

## 7 Main Lemma. Supplementary singular series

Using the notation of Sections 2 and 3 we can formulate and prove our

###### Main Lemma 1.

Suppose we have two primitive characters χ 1 ​ mod ​ r 1 \chi_{1}\,\text{\rm mod}\;r_{1}, χ 2 ​ mod ​ r 2 \chi_{2}\,\text{\rm mod}\;r_{2}, q 0 = [r 1, r 2] q_{0}=[r_{1},r_{2}], q 1 = q 0 / ( q 0, | m |) q_{1}=q_{0}/(q_{0},|m|), ℓ i = r i / ( r 1, r 2) \ell_{i}=r_{i}/(r_{1},r_{2}), e = ( m, ( r 1, r 2)) e=(m,(r_{1},r_{2})). Let χ ∗ = ( χ 1 ​ χ 2) ∗ \chi^{*}=(\chi_{1}\chi_{2})^{*}, cond ​ χ 1 ​ χ 2 = r ∗ = r ′ ​ ℓ 1 ​ ℓ 2 \mathrm{cond}\,\chi_{1}\chi_{2}=r^{*}=r^{\prime}\ell_{1}\ell_{2}, b ⁡ ( q) = c ⁡ ( χ 1, χ 2, q, m) b(q)=c(\chi_{1},\chi_{2},q,m),

(7.1) |  | f = ∏ p α | ( r 1, r 2) p | m p α, d = ∏ p α | ( r 1, r 2) p ∤ m p α, f=\prod_{\begin{subarray}{c}p^{\alpha}\|(r_{1},r_{2})\\ p\mid m\end{subarray}}p^{\alpha},\quad d=\prod_{\begin{subarray}{c}p^{\alpha}\|(r_{1},r_{2})\\ p\nmid m\end{subarray}}p^{\alpha}, |  |

(7.2) |  | 𝔖 ⁡ ( χ 1, χ 2, m) = ∑ t = 1 ∞ b ⁡ ( q 0 ​ t), A ⁡ ( χ 1, χ 2, m) = ∑ t = 1 ∞ | b ⁡ ( q 0 ​ t) |. {\mathfrak{S}}(\chi_{1},\chi_{2},m)=\sum^{\infty}_{t=1}b(q_{0}t),\quad A(\chi_{1},\chi_{2},m)=\sum^{\infty}_{t=1}|b(q_{0}t)|. |  |

Suppose A ⁡ ( χ 1, χ 2, m) ≠ 0 A(\chi_{1},\chi_{2},m)\neq 0. Then

(7.3) |  | b ( q 0) ≠ 0, r ′ ∣ d ​ f e = ( r 1, r 2) e, b(q_{0})\neq 0,\quad r^{\prime}\mid{df\over e}=\frac{(r_{1},r_{2})}{e}, |  |

(7.4) |  | b ⁡ ( q 0) = τ ⁡ ( χ ¯ 1) ​ τ ​ ( χ ¯ 2) ​ τ ​ ( χ ∗) ​ χ ¯ ∗ ​ ( − m ( q 0, | m |)) ​ μ ​ ( q 1 r ∗) ​ χ ∗ ​ ( q 1 r ∗) ​ μ ​ ( ℓ 1) ​ μ ​ ( ℓ 2) ​ χ ¯ 1 ​ ( ℓ 2) ​ χ ¯ 2 ​ ( ℓ 1) φ 2 ​ ( ℓ 1) ​ φ 2 ​ ( ℓ 2) ​ φ ​ ( d) ​ φ ​ ( f) ​ φ ​ ( d ​ f / e), b(q_{0})={\tau(\overline{\chi}_{1})\tau(\overline{\chi}_{2})\tau(\chi^{*})\overline{\chi}^{*}\left({-m\over(q_{0},|m|)}\right)\mu\left({q_{1}\over r^{*}}\right)\chi^{*}\left(q_{1}\over r^{*}\right)\mu(\ell_{1})\mu(\ell_{2})\overline{\chi}_{1}(\ell_{2})\overline{\chi}_{2}(\ell_{1})\over\varphi^{2}(\ell_{1})\varphi^{2}(\ell_{2})\varphi(d)\varphi(f)\varphi(df/e)}, |  |

(7.5) |  | | b ⁡ ( q 0) | = ℓ 1 φ 2 ​ ( ℓ 1) ⋅ ℓ 2 φ 2 ​ ( ℓ 2) ⋅ d φ ⁡ ( d) ⋅ f φ ⁡ ( f) ​ r ′ φ ⁡ ( d ​ f / e), |b(q_{0})|={\ell_{1}\over\varphi^{2}(\ell_{1})}\cdot{\ell_{2}\over\varphi^{2}(\ell_{2})}\cdot{d\over\varphi(d)}\cdot{f\over\varphi(f)}{\sqrt{r^{\prime}}\over\varphi(df/e)}, |  |

(7.6) |  | 𝔖 ⁡ ( χ 1, χ 2, m) = b ⁡ ( q 0) ​ ∏ p ∤ m p ∤ [r 1, r 2] ( 1 − 1 ( p − 1) 2) ​ ∏ p | m p ∤ [r 1, r 2] ( 1 + 1 ( p − 1)), {\mathfrak{S}}(\chi_{1},\chi_{2},m)=b(q_{0})\prod_{\begin{subarray}{c}p\nmid m\\ p\nmid[r_{1},r_{2}]\end{subarray}}\left(1-{1\over(p-1)^{2}}\right)\prod_{\begin{subarray}{c}p\mid m\\ p\nmid[r_{1},r_{2}]\end{subarray}}\left(1+{1\over(p-1)}\right), |  |

(7.7) |  | | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ 𝔖 ⁡ ( m), | A ⁡ ( χ 1, χ 2, m) | ≤ B ⋅ | 𝔖 ⁡ ( χ 1, χ 2, m) | |{\mathfrak{S}}(\chi_{1},\chi_{2},m)|\leq{\mathfrak{S}}(m),\quad|A(\chi_{1},\chi_{2},m)|\leq B\cdot|{\mathfrak{S}}(\chi_{1},\chi_{2},m)| |  |

with the constant B = ∏ p > 2 ( 1 + 2 / ( p ⁡ ( p − 2))) B=\prod\limits_{p>2}(1+2/(p(p-2))). Further | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ |{\mathfrak{S}}(\chi_{1},\chi_{2},m)|\leq ( 3 / 2) ​ 𝔖 ​ ( m) (\sqrt{3}/2){\mathfrak{S}}(m) unless the following five relations all hold:

(7.8) |  | r i ( r i, m) ∣ 36 ( i = 1, 2), r i ( r 1, r 2) ∣ 3 ( i = 1, 2), r ∗ ∣ 36. {r_{i}\over(r_{i},m)}\mid 36\ (i=1,2),\quad{r_{i}\over(r_{1},r_{2})}\mid 3\ (i=1,2),\quad r^{*}\mid 36. |  |

In case of the Generalized Twin Prime Problem (see ( 2.4)–( 2.5)) nearly everything remains unchanged.

###### Main Lemma 1’.

If we replace 𝔖 ⁡ ( χ 1, χ 2, m) {\mathfrak{S}}(\chi_{1},\chi_{2},m) by 𝔖 ′ ​ ( χ 1, χ 2, m) {\mathfrak{S}}^{\prime}(\chi_{1},\chi_{2},m), A ⁡ ( χ 1, χ 2, m) A(\chi_{1},\chi_{2},m) by the analogous A ′ ​ ( χ 1, χ 2, m) A^{\prime}(\chi_{1},\chi_{2},m), and χ ∗ = ( χ 1 ​ χ 2) ∗ \chi^{*}=(\chi_{1}\chi_{2})^{*} by ( χ 1 ​ χ ¯ 2) ∗ (\chi_{1}\overline{\chi}_{2})^{*} then the results of the Main Lemma 1 hold with the only change that τ ⁡ ( χ ¯ 2) \tau(\overline{\chi}_{2}) and χ ¯ 2 ​ ( ℓ 1) \overline{\chi}_{2}(\ell_{1}) in ( 7.4) are to be replaced by τ ⁡ ( χ ¯ 2) ¯ \overline{\tau(\overline{\chi}_{2})} and χ 2 ​ ( ℓ) \chi_{2}(\ell), respectively.

###### Corollary to the Main Lemma 1.

For the singular series 𝔖 ⁡ ( χ 1, χ 2, m) {\mathfrak{S}}(\chi_{1},\chi_{2},m) the inequality ( 1.21) holds.

###### Corollary to the Main Lemma 1’.

Let us replace 𝔖 ⁡ ( χ 1, χ 2, m) {\mathfrak{S}}(\chi_{1},\chi_{2},m) by 𝔖 ′ ​ ( χ 1, χ 2, m) {\mathfrak{S}}^{\prime}(\chi_{1},\chi_{2},m) in ( 1.21) and cond ​ χ 1 ​ χ 2 \mathrm{cond}\,\chi_{1}\chi_{2} by cond ​ χ 1 ​ χ ¯ 2 \mathrm{cond}\,\chi_{1}\overline{\chi}_{2} in ( 1.22). Then the inequality ( 1.21) remains valid.

The corollaries easily follow by ( 7.5) from the Main Lemmas 1 and 1’. Since the proof of Main Lemma 1’ goes mutatis mutandis, we will restrict ourselves to the proof of Main Lemma 1.

###### Remark.

In case of r 1 = r 2 = 1 r_{1}=r_{2}=1, we clearly have the classical singular series:

 | 𝔖 ⁡ ( χ 0, χ 0, m) = 𝔖 ′ ​ ( χ 0, χ 0, m) = 𝔖 ⁡ ( m) {\mathfrak{S}}(\chi_{0},\chi_{0},m)={\mathfrak{S}}^{\prime}(\chi_{0},\chi_{0},m)={\mathfrak{S}}(m) |  |

from ( 7.4) and ( 7.6).

###### Proof.

Let us investigate an arbitrary non-zero term belonging to q = q 0 ​ t = d ​ f ​ ℓ 1 ​ ℓ 2 ​ t q=q_{0}t=df\ell_{1}\ell_{2}t (with χ 0 = χ 0, q \chi_{0}=\chi_{0,q})

(7.9) |  | b ⁡ ( q 0 ​ t) = φ ​ ( q) − 2 ​ c χ 1 ​ χ 2 ​ χ 0 ​ ( − m) ​ τ ​ ( χ ¯ 1 ​ χ 0) ​ τ ​ ( χ ¯ 2 ​ χ 0) ≠ 0. b(q_{0}t)=\varphi(q)^{-2}c_{\chi_{1}\chi_{2}\chi_{0}}(-m)\tau(\overline{\chi}_{1}\chi_{0})\tau(\overline{\chi}_{2}\chi_{0})\neq 0. |  |

Let o p ​ ( n) = α o_{p}(n)=\alpha if p α | n p^{\alpha}\|n. By Lemma 4.2, τ ⁡ ( χ ¯ i ​ χ 0) ≠ 0 \tau(\overline{\chi}_{i}\chi_{0})\neq 0 implies the relation p ∤ ( q / r i) p\nmid(q/r_{i}) for p | r i p\mid r_{i}. Thus o p ​ ( r i) = o p ​ ( q) o_{p}(r_{i})=o_{p}(q). So we have ( t, [r 1, r 2]) = 1 (t,[r_{1},r_{2}])=1. For p | ( r 1, r 2) p\mid(r_{1},r_{2}) we have by the above o p ​ ( r 1) = o p ​ ( r 2) = o p ​ ( [r 1, r 2]) = o p ​ ( q) o_{p}(r_{1})=o_{p}(r_{2})=o_{p}([r_{1},r_{2}])=o_{p}(q).

If p | r i p\mid r_{i}, p ∤ r j p\nmid r_{j} (equivalently p | ℓ i p\mid\ell_{i}) then τ ⁡ ( χ ¯ j ​ χ 0) ≠ 0 \tau(\overline{\chi}_{j}\chi_{0})\neq 0 implies by Lemma 4.2 that by the μ \mu -factor 1 = o p ​ ( q r j) = o p ​ ( q) = o p ​ ( r i) 1=o_{p}\left({q\over r_{j}}\right)=o_{p}(q)=o_{p}(r_{i}). Similarly we have | μ ⁡ ( t) | = 1 |\mu(t)|=1. Summarizing the above we have

(7.10) |  | | μ ⁡ ( ℓ 1) | = | μ ⁡ ( ℓ 2) | = | μ ⁡ ( t) | = 1, ( t, q 0) = 1. |\mu(\ell_{1})|=|\mu(\ell_{2})|=|\mu(t)|=1,\quad(t,q_{0})=1. |  |

If p | ℓ i p\mid\ell_{i} then o p ​ ( q) = 1 o_{p}(q)=1 and p | r ∗ p\mid r^{*}. This implies, in view of ( 7.9), that by Lemma 4.4 we have p ​ | r ∗ | ​ q / ( q, | m |) p|r^{*}|q/(q,|m|) and so p ∤ m p\nmid m, that is ( m, ℓ i) = 1 (m,\ell_{i})=1 ( i = 1, 2) (i=1,2). Hence, using the definitions of d d, e e, f f, we have

(7.11) |  | ( m, r 1) = ( m, r 2) = ( m, [r 1, r 2]) = ( m, ( r 1, r 2)) = ( m, d ​ f) = ( m, f) = e. (m,r_{1})=(m,r_{2})=(m,[r_{1},r_{2}])=(m,(r_{1},r_{2}))=(m,df)=(m,f)=e. |  |

Suppose A ⁡ ( χ 1, χ 2, m) ≠ 0 A(\chi_{1},\chi_{2},m)\neq 0, equivalently there exists a t t with ( 7.9). Then, in view of ( t, r ∗) = 1 (t,r^{*})=1 and Lemma 4.4, the equivalent assertions

(7.12) |  | r ∗ | q 0 ​ t ( q 0 ​ t, | m |) ⟺ r ∗ | q 0 ( q 0, | m |) = ℓ 1 ​ ℓ 2 ​ d ​ f e r^{*}\Big|{q_{0}t\over(q_{0}t,|m|)}\Longleftrightarrow r^{*}\Big|{q_{0}\over(q_{0},|m|)}=\ell_{1}\ell_{2}d{f\over e} |  |

are both true, thus r ′ | d ​ f / e r^{\prime}\mid df/e. Let j ⁡ ( q) = j m ​ ( q) = q ( q, | m |) j(q)=j_{m}(q)={q\over(q,|m|)}. Then, by Lemmas 4.2 and 4.4, we have

(7.13) |  | b ⁡ ( q) = \displaystyle b(q)={} | 1 φ ⁡ ( q) ⋅ 1 φ ⁡ ( j ⁡ ( q)) χ ¯ ∗ ( − m ( q, | m |)) μ ( j ⁡ ( q) r ∗) χ ∗ ( j ⁡ ( q) r ∗) τ ( χ ∗) ⋅ \displaystyle{1\over\varphi(q)}\cdot{1\over\varphi(j(q))}\overline{\chi}^{*}\left({-m\over(q,|m|)}\right)\mu\left({j(q)\over r^{*}}\right)\chi^{*}\left({j(q)\over r^{*}}\right)\tau(\chi^{*})\cdot |  |

 |  | μ ⁡ ( t ​ ℓ 2) ​ χ ¯ 1 ​ ( t ​ ℓ 2) ​ τ ​ ( χ ¯ 1) ​ μ ​ ( t ​ ℓ 1) ​ χ ¯ 2 ​ ( t ​ ℓ 1) ​ τ ​ ( χ ¯ 2), \displaystyle\mu(t\ell_{2})\overline{\chi}_{1}(t\ell_{2})\tau(\overline{\chi}_{1})\mu(t\ell_{1})\overline{\chi}_{2}(t\ell_{1})\tau(\overline{\chi}_{2}), |  |

where q = q 0 ​ t = q 0 ​ h ​ k q=q_{0}t=q_{0}hk, h = ∏ p | t, p | m p h=\prod\limits_{p\mid t,p\mid m}p, k = ∏ p | t, p ∤ m t k=\prod\limits_{p\mid t,p\nmid m}t. Taking q = q 0 q=q_{0}, that is, t = 1 t=1, we obtain ( 7.4). Since ( q 0 ​ h ​ k, | m |) = h ⁡ ( q 0, | m |) (q_{0}hk,|m|)=h(q_{0},|m|) we have j ⁡ ( q 0 ​ h ​ k) = k ​ j ​ ( q 0) = k ​ q 1 j(q_{0}hk)=kj(q_{0})=kq_{1}. Taking into account ( 7.10), we have in case of b ⁡ ( q 0 ​ t) ≠ 0 b(q_{0}t)\neq 0 from ( 7.13)

(7.14) |  | b ⁡ ( q 0 ​ t) = b ⁡ ( q 0) ​ χ ∗ ​ ( h) ​ μ ​ ( k) ​ χ ∗ ​ ( k) ​ χ ¯ 1 ​ ( k ​ h) ​ χ ¯ 2 ​ ( k ​ h) φ 2 ​ ( k) ​ φ ​ ( h) = b ⁡ ( q 0) ​ μ ⁡ ( k) φ 2 ​ ( k) ⋅ 1 φ ⁡ ( h). b(q_{0}t)=b(q_{0}){\chi^{*}(h)\mu(k)\chi^{*}(k)\overline{\chi}_{1}(kh)\overline{\chi}_{2}(kh)\over\varphi^{2}(k)\varphi(h)}=b(q_{0}){\mu(k)\over\varphi^{2}(k)}\cdot{1\over\varphi(h)}. |  |

Now ( 7.14) shows ( 7.6). Further,

(7.15) |  | ∑ t = 1 ∞ | b ⁡ ( q 0 ​ t) | \displaystyle\sum^{\infty}_{t=1}|b(q_{0}t)| | = | b ⁡ ( q 0) | ​ ∏ p ∤ q 0, p ∤ m ( 1 + 1 ( p − 1) 2) ​ ∏ p ∤ q 0, p | m ( 1 + 1 p − 1) \displaystyle=|b(q_{0})|\prod_{p\nmid q_{0},p\nmid m}\left(1+{1\over(p-1)^{2}}\right)\prod_{p\nmid q_{0},p\mid m}\left(1+{1\over p-1}\right) |  |

 |  | ≤ | 𝔖 ⁡ ( χ 1, χ 2, m) | ⋅ ∏ p > 2 ( ( 1 + 1 ( p − 1) 2) / ( 1 − 1 ( p − 1) 2)) \displaystyle\leq|{\mathfrak{S}}(\chi_{1},\chi_{2},m)|\cdot\prod_{p>2}\left(\left(1+{1\over(p-1)^{2}}\right)\Big/\left(1-{1\over(p-1)^{2}}\right)\right) |  |

 |  | = B ​ | 𝔖 ⁡ ( χ 1, χ 2, m) |. \displaystyle=B|{\mathfrak{S}}(\chi_{1},\chi_{2},m)|. |  |

The first equality in ( 7.15) shows b ⁡ ( q 0) ≠ 0 b(q_{0})\neq 0, when A ⁡ ( χ 1, χ 2, m) ≠ 0 A(\chi_{1},\chi_{2},m)\neq 0, and so by ( 7.4) we have also ( 7.5). Thus it remains to prove | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ 𝔖 ⁡ ( m) |{\mathfrak{S}}(\chi_{1},\chi_{2},m)|\leq{\mathfrak{S}}(m), and ( 7.8).

Let us investigate the ratio ξ \xi of the two sides | 𝔖 ⁡ ( χ 1, χ 2, m) | |{\mathfrak{S}}(\chi_{1},\chi_{2},m)| and 𝔖 ⁡ ( m) {\mathfrak{S}}(m) separately for each prime. If p ∤ [r 1, r 2] p\nmid[r_{1},r_{2}] we have clearly the same factor on both sides. So we have to study the following cases:

(i) If p | ℓ i p\mid\ell_{i}, then by ( m, ℓ i) = 1 (m,\ell_{i})=1 (see ( 7.11)) we have p ∤ m p\nmid m, thus p > 2 p>2.

Now clearly

(7.16) |  | ξ ⁡ ( p) = p ( p − 1) 2: p ⁡ ( p − 2) ( p − 1) 2 = 1 p − 2 ≤ 1. \xi(p)={p\over(p-1)^{2}}:{p(p-2)\over(p-1)^{2}}={1\over p-2}\leq 1. |  |

Equality holds if and only if ℓ i = 3 \ell_{i}=3; otherwise ξ ≤ 1 / 3 \xi\leq 1/3.

(ii) Suppose p | d p\mid d, then by definition p ∤ m p\nmid m, so p > 2 p>2. Let p α | d p^{\alpha}\|d ( α ≥ 1) (\alpha\geq 1), p β | r ′ p^{\beta}\|r^{\prime}. Then r ′ | d ​ f / e r^{\prime}\mid df/e implies 0 ≤ β ≤ α 0\leq\beta\leq\alpha. Thus writing further on ξ \xi for ξ ⁡ ( p) \xi(p),

(7.17) |  | ξ = p p − 1 ⋅ p β / 2 p α − 1 ​ ( p − 1): p ⁡ ( p − 2) ( p − 1) 2 = p 1 + β / 2 − α p − 2 ≤ p 1 − α / 2 p − 2. \xi={p\over p-1}\cdot{p^{\beta/2}\over p^{\alpha-1}(p-1)}:{p(p-2)\over(p-1)^{2}}={p^{1+\beta/2-\alpha}\over p-2}\leq{p^{1-\alpha/2}\over p-2}. |  |

Now, if p ≥ 5 p\geq 5 we have ξ ≤ 5 / 3 \xi\leq\sqrt{5}/3 for every α ≥ 1 \alpha\geq 1. Let p = 3 p=3. Then for α ≥ 3 \alpha\geq 3 we have ξ ≤ 1 / 3 \xi\leq 1/\sqrt{3}. For α = 2 \alpha=2, β ≤ 1 \beta\leq 1 we have ξ ≤ 1 / 3 \xi\leq 1/\sqrt{3}. In case of α = β = 2 \alpha=\beta=2 we have ξ = 1 \xi=1.

For α = 1 \alpha=1 ( p = 3) (p=3) we have 3 1 | r 1 3^{1}\|r_{1}, 3 1 | r 2 3^{1}\|r_{2}, so the mod ​ 3 \,\text{\rm mod}\;3 component of both χ 1 \chi_{1} and χ 2 \chi_{2} are χ 1 | 3 = χ 2 | 3 = χ ′ \chi_{1}\big|_{3}=\chi_{2}\big|_{3}=\chi^{\prime}, the only real non-principal character mod ​ 3 \,\text{\rm mod}\;3. Thus χ ∗ | 3 = χ 1 ​ χ 2 | 3 = χ 0 \chi^{*}\big|_{3}=\chi_{1}\chi_{2}\big|_{3}=\chi_{0}, and consequently 3 ∤ r ∗ 3\nmid r^{*}, β = 0 \beta=0. In this case we have again equality in ( 7.17). Summarizing, we have equality in ( 7.17) if and only if d = 3 d=3, 3 1 | r 1 3^{1}\|r_{1}, 3 1 | r 2 3^{1}\|r_{2} or d = 9 d=9 and 3 2 | r ′ ⇔ 3 2 | r ∗ 3^{2}\|r^{\prime}\Leftrightarrow 3^{2}\|r^{*}.

Otherwise ξ ≤ 5 / 3 \xi\leq\sqrt{5}/3.

(iii) Finally if p | f p\,|\,f, then by definition p | e p\,|\,e, p | m p\,|\,m. Let p α | f / e p^{\alpha}\|f/e, p β | r ′ p^{\beta}\|r^{\prime} ( 0 ≤ β ≤ α) (0\leq\beta\leq\alpha). Then

(7.18) |  | ξ = p p − 1 ⋅ p β / 2 φ ⁡ ( p α): p p − 1 = p β / 2 φ ⁡ ( p α) ≤ p α / 2 φ ⁡ ( p α). \xi={p\over p-1}\cdot{p^{\beta/2}\over\varphi(p^{\alpha})}:{p\over p-1}={p^{\beta/2}\over\varphi(p^{\alpha})}\leq{p^{\alpha/2}\over\varphi(p^{\alpha})}. |  |

If α = 0 \alpha=0 then clearly β = 0 \beta=0 and ξ = 1 \xi=1 (for every p p). Let us suppose α ≥ 1 \alpha\geq 1. If p ≥ 3 p\geq 3 then ξ ≤ 3 / 2 \xi\leq\sqrt{3}/2. Let p = 2 p=2. Then for α ≥ 3 \alpha\geq 3 we have ξ ≤ 1 / 2 \xi\leq 1/\sqrt{2}. For α = 2 \alpha=2, β ≤ 1 \beta\leq 1 we have ξ ≤ 1 / 2 \xi\leq 1/\sqrt{2}. In case of α = β = 2 \alpha=\beta=2 we have ξ = 1 \xi=1. If α = 1 \alpha=1 there is no non-principal character mod ​ 2 \,\text{\rm mod}\;2, so β = 0 \beta=0 and ξ = 1 \xi=1. Summarizing, ξ = 1 \xi=1 holds if and only if α = β = 0 \alpha=\beta=0, p p arbitrary, that is p ∤ f / e p\nmid f/e or

(7.19) |  | p = 2, α = 1, β = 0 ​ or ​ p = 2, α = β = 2, p=2,\ \alpha=1,\ \beta=0\ \text{ or }\ p=2,\ \alpha=\beta=2, |  |

that is

(7.20) |  | 2 | f / e, 2 ∤ r ′ ⇔ 2 ∤ r ∗ ​ or ​ 2 2 | f / e, 2 2 | r ′ ⇔ 2 2 | r ∗. 2\|f/e,\ 2\nmid r^{\prime}\Leftrightarrow 2\nmid r^{*}\ \text{ or }\ 2^{2}\|f/e,\ 2^{2}\|r^{\prime}\Leftrightarrow 2^{2}\|r^{*}. |  |

Otherwise ξ ≤ 3 / 2 \xi\leq\sqrt{3}/2.

The considerations (i), (ii), (iii) really show that we have always

 | | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ 𝔖 ⁡ ( m). \bigl|{\mathfrak{S}}(\chi_{1},\chi_{2},m)\bigr|\leq{\mathfrak{S}}(m). |  |

Further,

 | | 𝔖 ⁡ ( χ 1, χ 2, m) | ≤ ( 3 / 2) ​ 𝔖 ​ ( m) \bigl|{\mathfrak{S}}(\chi_{1},\chi_{2},m)\bigr|\leq(\sqrt{3}/2){\mathfrak{S}}(m) |  |

unless ( 7.8) holds. ∎

## 8 Reduction for zeros near to 𝝈 = 𝟏 \sigma=1

In this section we will show (using the notation of Section 6) that error terms arising from S 1 2 S^{2}_{1} and S 1 ​ S 0 S_{1}S_{0} make a contribution of

(8.1) |  | O ⁡ ( ℒ 8 ​ X 1 − b / 82) O(\mathcal{L}^{8}X^{1-b/82}) |  |

to R 1 ​ ( m) R_{1}(m). Thus, further on, it is enough to study the integral containing S 0 2 S^{2}_{0}. First we estimate the term with S 1 2 S^{2}_{1}. Using the notation from Sections 1, 3 and 6 by Lemmas 4.1 – 4.2 and ( 6.1) we have, with the definition of W 1 ​ ( χ) W_{1}(\chi) in ( 6.6)

(8.2) |  |  | | ∑ q ≤ p ∑ ′ 𝑎 ​ ∫ 𝔐 ⁡ ( q, a) S 1 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α | ≤ \displaystyle\Biggl|\sum_{q\leq p}\underset{a}{\sum\nolimits^{\prime}}\int\limits_{\mathfrak{M}(q,a)}S^{2}_{1}(\alpha)e(-m\alpha)d\alpha\Biggr|\leq |  |

 |  | ≤ ∑ q ≤ P ∑ ′ a ⁡ ( q) ​ ∫ 𝔐 ⁡ ( q, a) | S 1 2 ​ ( α) | ​ 𝑑 α = \displaystyle\leq\sum_{q\leq P}\underset{a(q)}{\sum\nolimits^{\prime}}\int\limits_{\mathfrak{M}(q,a)}|S^{2}_{1}(\alpha)|d\alpha= |  |

 |  | = ∑ q ≤ p ∑ ′ a ⁡ ( q) ∫ − 1 / q Q 1 / q ​ Q | 1 φ ⁡ ( q) ∑ χ ⁡ ( q) χ ( a) τ ( χ ¯) S 1 ( χ, η) | 2 d η = \displaystyle=\sum_{q\leq p}\underset{a(q)}{\sum\nolimits^{\prime}}\int\limits^{1/qQ}_{-1/qQ}\left|{1\over\varphi(q)}\sum_{\chi(q)}\chi(a)\tau(\overline{\chi})S_{1}(\chi,\eta)\right|^{2}d\eta= |  |

 |  | = ∑ q ≤ P 1 φ 2 ​ ( q) ∑ χ ⁡ ( q) ∑ χ ′ ​ ( q) τ ( χ ¯) τ ⁡ ( χ ¯ ′) ¯ ∑ ′ a ⁡ ( q) χ ( a) χ ¯ ′ ( a) ∫ − 1 / q Q 1 / q ​ Q S 1 ( χ, η) S 1 ​ ( χ ′, η) ¯ d η = \displaystyle=\sum_{q\leq P}{1\over\varphi^{2}(q)}\sum_{\chi(q)}\sum_{\chi^{\prime}(q)}\tau(\overline{\chi})\overline{\tau(\overline{\chi}^{\prime})}\underset{a(q)}{\sum\nolimits^{\prime}}\chi(a)\overline{\chi}^{\prime}(a)\int\limits^{1/qQ}_{-1/qQ}S_{1}(\chi,\eta)\overline{S_{1}(\chi^{\prime},\eta)}d\eta= |  |

 |  | = ∑ q ≤ P 1 φ ⁡ ( q) ∑ χ ⁡ ( q) | τ ( χ ¯) | 2 ∫ − 1 / q Q 1 / q ​ Q | S 1 ( χ, η) | 2 d η = \displaystyle=\sum_{q\leq P}{1\over\varphi(q)}\sum_{\chi(q)}|\tau(\overline{\chi})|^{2}\int\limits^{1/qQ}_{-1/qQ}|S_{1}(\chi,\eta)|^{2}d\eta= |  |

 |  | = ∑ q ≤ P 1 φ ⁡ ( q) ∑ χ ⁡ ( q) | τ ( χ ¯) | 2 ∫ − 1 / q Q 1 / q ​ Q | S 1 ( χ ∗, η) | 2 d η ≤ \displaystyle=\sum_{q\leq P}{1\over\varphi(q)}\sum_{\chi(q)}|\tau(\overline{\chi})|^{2}\int\limits^{1/qQ}_{-1/qQ}|S_{1}(\chi^{*},\eta)|^{2}d\eta\leq |  |

 |  | ≤ ∑ r ≤ P ∑ ∗ χ ⁡ ( r) r ∫ − 1 / r Q 1 / r ​ Q | S 1 ( χ, η) | 2 d η ∑ ℓ ≤ P / r ( ℓ, r) = 1 1 φ ⁡ ( r ​ ℓ) ≤ \displaystyle\leq\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}r\int\limits^{1/rQ}_{-1/rQ}|S_{1}(\chi,\eta)|^{2}d\eta\sum_{\begin{subarray}{c}\ell\leq P/r\\ (\ell,r)=1\end{subarray}}{1\over\varphi(r\ell)}\leq |  |

 |  | ≤ ∑ r ≤ P r φ ⁡ ( r) ​ ∑ ∗ χ ⁡ ( r) ​ ( W 1 ​ ( χ)) 2 ​ ∑ ℓ ≤ P / r 1 φ ⁡ ( ℓ) ≪ ℒ 2 ​ ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ W 1 2 ​ ( χ). \displaystyle\leq\sum_{r\leq P}{r\over\varphi(r)}\underset{\chi(r)}{\sum\nolimits^{*}}(W_{1}(\chi))^{2}\sum_{\ell\leq P/r}{1\over\varphi(\ell)}\ll\mathcal{L}^{2}\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}W^{2}_{1}(\chi). |  |

As we can see, at the cost of a logarithm we could get rid of all cross-products S 1 ​ ( χ, η) ​ S 1 ​ ( χ ′, η) ¯ S_{1}(\chi,\eta)\overline{S_{1}(\chi^{\prime},\eta)} with χ ≠ χ ′ \chi\neq\chi^{\prime}. The loss of the logarithm would be crucial near σ = 1 \sigma=1 but not here. We can estimate W 1 ​ ( χ) W_{1}(\chi) ( χ \chi primitive mod ​ r \,\text{\rm mod}\;r, 1 ≤ r ≤ P 1\leq r\leq P) by means of Gallagher’s lemma (Lemma 4.11) as follows.

(8.3) |  | W 1 2 ​ ( χ) ≪ ∫ X 1 − Y X | 1 Y ​ ∑ x < n ≤ x + Y X 1 ≤ n ≤ X a n | 2 ​ 𝑑 x ≤ I 1 ​ ( χ) + I 2 ​ ( χ) + I 3 ​ ( χ), W^{2}_{1}(\chi)\ll\int\limits^{X}_{X_{1}-Y}\bigg|{1\over Y}\sum_{\begin{subarray}{c}x<n\leq x+Y\\ X_{1}\leq n\leq X\end{subarray}}a_{n}\bigg|^{2}dx\leq I_{1}(\chi)+I_{2}(\chi)+I_{3}(\chi), |  |

where X 2 = max ⁡ ( X 1, 6 ​ Y) X_{2}=\max(X_{1},6Y),

(8.4) |  | Y = r Q / 2 ( ≤ X / 2), I 1 = ∫ X 1 − Y X 2, I 2 = ∫ min ⁡ ( X 2, X − Y) X − Y, I 3 = ∫ X − Y X Y=rQ/2(\leq X/2),\ \ I_{1}=\int\limits^{X_{2}}_{X_{1}-Y},\ \ I_{2}=\int\limits^{X-Y}_{\min(X_{2},X-Y)},\ \ I_{3}=\int\limits^{X}_{X-Y} |  |

(where I 2 I_{2} is missing if Y ≥ X / 7 Y\geq X/7) and with the notation ( 1.26)–( 1.27)

(8.5) |  | a n = { χ ⁡ ( p) ​ log ⁡ p − b n if ​ n = p − b n if ​ n ≠ p, b n = ∑ ′ ϱ = ϱ χ 0 ≤ δ ≤ b, | γ | ≤ X ​ A ​ ( ϱ) ​ n ϱ − 1. a_{n}=\begin{cases}\chi(p)\log p-b_{n}&\text{if }n=p\\ -b_{n}&\text{if }n\neq p\end{cases},\quad b_{n}=\underset{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ 0\leq\delta\leq b,\ |\gamma|\leq\sqrt{X}\end{subarray}}{\sum\nolimits^{\prime}}A(\varrho)n^{\varrho-1}. |  |

The dash at the summation sign means that the summation is extended for ϱ = 1 \varrho=1 in case of χ ⁡ ( mod ​ 1) \chi(\,\text{\rm mod}\;1).

The treatment of the two tails, I 1 I_{1} and I 3 I_{3} are simpler and basically the same. Using the explicit form of ψ ⁡ ( x, χ) \psi(x,\chi) (see ( 4.16)) we obtain for any x ∈ [X − Y, X] x\in[X-Y,X], in view of Lemma 4.15

(8.6) |  | 1 Y ​ ∑ x ≤ n ≤ X a n \displaystyle{1\over Y}\sum_{x\leq n\leq X}a_{n} | = − 1 Y ​ ∑ ϱ = ϱ χ b < δ ≤ 1 / 2, | γ | ≤ X X ϱ − x ϱ ϱ + O ⁡ ( X Y ​ ℒ 2) \displaystyle={-1\over Y}\sum_{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ b<\delta\leq 1/2,\ |\gamma|\leq\sqrt{X}\end{subarray}}{X^{\varrho}-x^{\varrho}\over\varrho}+O\left({\sqrt{X}\over Y}\mathcal{L}^{2}\right) |  |

 |  | ≪ ∑ ϱ = ϱ χ b < δ ≤ 1 / 2, | γ | ≤ X min ⁡ ( X 1 − δ Y ⁡ ( | γ | + 1), X − δ) + O ⁡ ( X Y ​ ℒ 2). \displaystyle\ll\sum_{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ b<\delta\leq 1/2,|\gamma|\leq\sqrt{X}\end{subarray}}\min\left({X^{1-\delta}\over Y(|\gamma|+1)},X^{-\delta}\right)+O\left({\sqrt{X}\over Y}\mathcal{L}^{2}\right). |  |

The effect of the last error terms of the form ℒ 2 ​ X / Y \mathcal{L}^{2}\sqrt{X}/Y is, after squaring, integrating and summing for all characters,

(8.7) |  | ≪ ℒ 4 ​ ∑ r ≤ P r ​ X ​ r ​ Q ( r ​ Q) 2 = ℒ 4 ​ X ​ P Q = ℒ 4 ​ P 2. \ll\mathcal{L}^{4}\sum_{r\leq P}r{XrQ\over(rQ)^{2}}={\mathcal{L}^{4}XP\over Q}=\mathcal{L}^{4}P^{2}. |  |

We divide the remaining zeros into ≪ ℒ 3 \ll\mathcal{L}^{3} classes according to their real, imaginary parts and the conductor r r of the relevant primitive character as follows:

(8.8) |  | r ∼ R, ( 2 μ − 1) ​ X R ​ Q ≤ | γ | ≤ ( 2 μ + 1 − 1) ​ X R ​ Q, h ν − 1 ℒ ≤ δ ≤ h ν, h ν = ν ℒ r\!\sim\!R,\ (2^{\mu}\!-\!1){X\over RQ}\leq|\gamma|\leq(2^{\mu+1}-1){X\over RQ},\ h_{\nu}\!-\!{1\over\mathcal{L}}\leq\delta\leq h_{\nu},\ \ h_{\nu}={\nu\over\mathcal{L}} |  |

where

(8.9) |  | 2 k = R ≤ P / 2, μ = 0, 1, … [log X / log 2], b ℒ ≤ ν ≤ ⌈ ℒ / 2 ⌉. 2^{k}=R\leq P/2,\ \ \mu=0,1,\dots[\log\sqrt{X}/\log 2],\ \ b\mathcal{L}\leq\nu\leq\lceil\mathcal{L}/2\rceil. |  |

Let us denote the contribution of any given class ( R, μ, ν) (R,\mu,\nu) to ∑ r ∑ ∗ χ ⁡ ( r) ​ I 3 ​ ( χ) \sum\limits_{r}\underset{\chi(r)}{\sum\nolimits^{*}}I_{3}(\chi) (with the notation 2 μ = M 2^{\mu}=M) by J 3 ​ ( R, M, h) J_{3}(R,M,h). Then by the Cauchy–Schwarz inequality and X / Y = 2 ​ P / r X/Y=2P/r we have (the conditions R ≥ 1 R\geq 1, M ≥ 1 M\geq 1 will be omitted)

(8.10) |  |  | ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ I 3 ​ ( χ) ≪ ℒ 6 ​ max R ≤ P, M ≤ X b ≤ h ≤ 1 / 2 ​ J 3 ​ ( R, M, h) \displaystyle\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}I_{3}(\chi)\ll\mathcal{L}^{6}\max_{\begin{subarray}{c}R\leq P,M\leq X\\ b\leq h\leq 1/2\end{subarray}}J_{3}(R,M,h) |  |

 |  | ≪ ℒ 6 ​ max R ≤ P, M ≤ X b ≤ h ≤ 1 / 2 ​ ∑ r ∼ R ∑ ∗ χ ⁡ ( r) ​ N 2 ​ ( 1 − h, X ​ M R ​ Q, χ) ​ ( X − h M) 2 ⋅ R ​ Q \displaystyle\ll\mathcal{L}^{6}\max_{\begin{subarray}{c}R\leq P,M\leq X\\ b\leq h\leq 1/2\end{subarray}}\sum_{r\sim R}\underset{\chi(r)}{\sum\nolimits^{*}}N^{2}\left(1-h,{XM\over RQ},\chi\right)\left({X^{-h}\over M}\right)^{2}\cdot RQ |  |

 |  | ≪ ℒ 6 ​ max R ≤ P, M ≤ X b ≤ h ≤ 1 / 2 ​ X ​ M R ​ Q ​ ℒ ​ R ​ Q M ⋅ M − 1 ​ N ∗ ​ ( 1 − h, X ​ M R ​ Q, 2 ​ R) ⋅ X − 2 ​ h \displaystyle\ll\mathcal{L}^{6}\max_{\begin{subarray}{c}R\leq P,M\leq X\\ b\leq h\leq 1/2\end{subarray}}{XM\over RQ}\mathcal{L}{RQ\over M}\cdot M^{-1}N^{*}\left(1-h,{XM\over RQ},2R\right)\cdot X^{-2h} |  |

 |  | = X ​ ℒ 7 ​ max R ≤ P, M ≤ X b ≤ h ≤ 1 / 2 ​ M − 1 ​ N ∗ ​ ( 1 − h, X ​ M R ​ Q, 2 ​ R) ⋅ X − 2 ​ h. \displaystyle=X\mathcal{L}^{7}\max_{\begin{subarray}{c}R\leq P,M\leq X\\ b\leq h\leq 1/2\end{subarray}}M^{-1}N^{*}\left(1-h,{XM\over RQ},2R\right)\cdot X^{-2h}. |  |

If h ≤ 3 / 8 − ε h\leq 3/8-\varepsilon we apply the imperfect density theorem of Heath–Brown (Lemma 4.19) and obtain

(8.11) |  | M − 1 ​ N ∗ ​ ( − h, X ​ M R ​ Q, 2 ​ R) ​ X − 2 ​ h \displaystyle M^{-1}N^{*}\left(\!1\!-\!h,{XM\over RQ},2R\!\right)X^{-2h} | ≪ ( R 2 ​ P 6 / 5 R 6 / 5) ( 20 9 + ε) ​ h ​ M ( 8 3 + 6 5 ​ ε) ​ h − 1 ​ X − 2 ​ h \displaystyle\ll\left(R^{2}{P^{6/5}\over R^{6/5}}\right)^{\left({20\over 9}+\varepsilon\right)h}M^{\left({8\over 3}+{6\over 5}\varepsilon\right)h-1}X^{-2h} |  |

 | ≪ ( X − 1 ​ P 20 9 + ε) 2 ​ h \displaystyle\ll\big(X^{-1}P^{{20\over 9}+\varepsilon}\big)^{2h} | ≪ X − ( 1 − ( 20 9 + ε) ​ ϑ) ​ 2 ​ b ≪ X − b / 41. \displaystyle\ll X^{-\left(1-\left({20\over 9}+\varepsilon\right)\vartheta\right)2b}\ll X^{-b/41}. |  |

If 3 / 8 − ε ≤ h ≤ 1 / 2 3/8-\varepsilon\leq h\leq 1/2 we will use Lemma 4.16. Then we have by 3 ​ h ≤ 1 + h 3h\leq 1+h

(8.12) |  | M − 1 ​ N ∗ ​ ( 1 − h, X ​ M R ​ Q, R) ​ X − 2 ​ h \displaystyle M^{-1}N^{*}\left(1-h,{XM\over RQ},R\right)X^{-2h} | ≪ ℒ 9 ​ ( R 2 ⋅ P R) 3 ​ h 1 + h ​ M 3 ​ h 1 + h − 1 ​ X − 2 ​ h \displaystyle\ll\mathcal{L}^{9}\left(R^{2}\cdot{P\over R}\right)^{3h\over 1+h}M^{{3h\over 1+h}-1}X^{-2h} |  |

 | ≪ ℒ 9 ​ ( P 3 1 + h ​ X − 1) 2 ​ h \displaystyle\ll\mathcal{L}^{9}\big(P^{3\over 1+h}X^{-1}\big)^{2h} | ≪ ℒ 9 ⋅ X ( ( 24 11 + 2 ​ ε) ​ ϑ − 1) ​ ( 3 / 4 − 2 ​ ε) ≪ X − 1 / 45. \displaystyle\ll\mathcal{L}^{9}\cdot X^{\left(\left({24\over 11}+2\varepsilon\right)\vartheta-1\right)(3/4-2\varepsilon)}\ll X^{-1/45}. |  |

Since the estimation of I 1 I_{1} runs completely analogously,

(8.13) |  | ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ ( I 1 ​ ( χ) + I 3 ​ ( χ)) ≪ ℒ 7 ​ X 1 − b / 41. \sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}(I_{1}(\chi)+I_{3}(\chi))\ll\mathcal{L}^{7}X^{1-b/41}. |  |

Suppose now that X 2 < X − Y X_{2}<X-Y, that is Y < X / 7 Y<X/7, otherwise we are ready. If x ∈ ( X 2, X − Y) x\in(X_{2},X-Y), then x ≥ 6 ​ Y x\geq 6Y and

(8.14) |  | [x, x + Y] ⊂ [X 1, X]. [x,x+Y]\subset[X_{1},X]. |  |

Thus the condition X 1 < n ≤ X X_{1}<n\leq X can be omitted in ( 8.3). So let us suppose that Y ≤ x / 6 Y\leq x/6 and consider with the notation ( 8.5)

(8.15) |  | I 2 ′ ​ ( χ, x) = Y − 2 ​ ∫ x 2 ​ x | ϑ ⁡ ( u + Y) − ϑ ⁡ ( u) | 2 ​ 𝑑 u, ϑ ⁡ ( u) = ∑ n ≤ u a n. I^{\prime}_{2}(\chi,x)=Y^{-2}\int\limits^{2x}_{x}|\vartheta(u+Y)-\vartheta(u)|^{2}du,\quad\vartheta(u)=\sum_{n\leq u}a_{n}. |  |

For this integral we can apply the idea of Saffari and Vaughan [22], to replace u + Y u+Y by u + θ ​ u u+\theta u. Although the proof runs completely analogously to [22, Lemma 6], for the sake of completeness we will present their arguments here, since our function ϑ ⁡ ( u) \vartheta(u) is different now.

Suppose that 2 ​ Y ≤ v ≤ 3 ​ Y 2Y\leq v\leq 3Y, x ≤ u ≤ 2 ​ x x\leq u\leq 2x. In this case we have Y ≤ v − Y ≤ 2 ​ Y Y\leq v-Y\leq 2Y, x ≤ u + Y ≤ u + v ≤ 3 ​ x x\leq u+Y\leq u+v\leq 3x. Further

(8.16) |  | | ϑ ⁡ ( u + Y) − ϑ ⁡ ( u) | 2 ≤ 2 ​ ( | ϑ ⁡ ( u + v) − ϑ ⁡ ( u) | 2 + | ϑ ⁡ ( u + Y + v − Y) − ϑ ⁡ ( u + Y) | 2). |\vartheta(u+Y)-\vartheta(u)|^{2}\leq 2\big(|\vartheta(u+v)-\vartheta(u)|^{2}+|\vartheta(u+Y+v-Y)-\vartheta(u+Y)|^{2}\big). |  |

Thus on the right-hand side the starting points of the intervals are in [x, 3 ​ x] [x,3x] and the length is in [Y, 3 ​ Y] [Y,3Y]. So we can write ( 8.16) for all possible values of v ∈ ( 2 ​ Y, 3 ​ Y) v\in(2Y,3Y) for any u u to obtain

(8.17) |  | Y ​ ∫ x 2 ​ x | ϑ ⁡ ( u + Y) − ϑ ⁡ ( u) | 2 ​ 𝑑 u \displaystyle Y\int\limits^{2x}_{x}|\vartheta(u+Y)\!-\!\vartheta(u)|^{2}du | ≤ 4 ​ ∫ x 3 ​ x ∫ Y 3 ​ Y | ϑ ⁡ ( u + v ′) − ϑ ⁡ ( u) | 2 ​ d ​ v ′ ​ 𝑑 u = \displaystyle\leq 4\int\limits^{3x}_{x}\int\limits^{3Y}_{Y}|\vartheta(u+v^{\prime})-\vartheta(u)|^{2}dv^{\prime}\,du= |  |

 |  | = 4 ​ ∫ x 3 ​ x ∫ Y / u 3 ​ Y / u | ϑ ⁡ ( u + θ ​ u) − ϑ ⁡ ( u) | 2 ​ u ​ 𝑑 θ ​ 𝑑 u ≤ \displaystyle=4\int\limits^{3x}_{x}\int\limits^{3Y/u}_{Y/u}|\vartheta(u+\theta u)-\vartheta(u)|^{2}ud\theta du\leq |  |

 |  | ≤ 4 ⋅ 3 x ∫ x 3 ​ x ∫ Y / 2 ​ x 3 ​ Y / x | ϑ ( u + θ u) − ϑ ( u) | 2 d θ d u = \displaystyle\leq 4\cdot 3x\int\limits^{3x}_{x}\int\limits^{3Y/x}_{Y/2x}|\vartheta(u+\theta u)-\vartheta(u)|^{2}d\theta du= |  |

 |  | = 12 ​ x ⋅ ∫ Y / 2 ​ x 3 ​ Y / x ( ∫ x 3 ​ x | ϑ ⁡ ( u + θ ​ u) − ϑ ⁡ ( u) | 2 ​ 𝑑 u) ​ 𝑑 θ ≤ \displaystyle=12x\cdot\int\limits^{3Y/x}_{Y/2x}\bigg(\int\limits^{3x}_{x}|\vartheta(u+\theta u)-\vartheta(u)|^{2}du\bigg)d\theta\leq |  |

 |  | ≤ 30 ​ Y ​ max ⁡ ∫ x 3 ​ x Y / 2 ​ x ≤ θ ≤ 3 ​ Y / x ⁡ | ϑ ⁡ ( u + θ ​ u) − ϑ ⁡ ( u) | 2 ​ 𝑑 u. \displaystyle\leq 30Y\max_{Y/2x\leq\theta\leq 3Y/x}\int\limits^{3x}_{x}|\vartheta(u+\theta u)-\vartheta(u)|^{2}du. |  |

Hence,

(8.18) |  | I 2 ′ ​ ( χ, x) ≤ 30 ​ Y − 2 ​ max ⁡ ∫ x 3 ​ x Y / 2 ​ x ≤ θ ≤ 3 ​ Y / x ⁡ | ϑ ⁡ ( u + θ ​ u) − ϑ ⁡ ( u) | 2 ​ 𝑑 u. I^{\prime}_{2}(\chi,x)\leq 30Y^{-2}\max_{Y/2x\leq\theta\leq 3Y/x}\int\limits^{3x}_{x}|\vartheta(u+\theta u)-\vartheta(u)|^{2}du. |  |

Similarly to ( 8.6) we have

(8.19) |  | ϑ ⁡ ( u + θ ​ u) − ϑ ⁡ ( u) = − 1 Y ​ ∑ ′ ϱ = ϱ χ 1 / 2 ≥ δ ≥ b, | γ | ≤ X ​ u ϱ ​ ( ( 1 + θ) ϱ − 1) ϱ + O ⁡ ( x ​ ℒ 2 Y). \vartheta(u+\theta u)-\vartheta(u)={-1\over Y}\underset{\begin{subarray}{c}\varrho=\varrho_{\chi}\\ 1/2\geq\delta\geq b,\ |\gamma|\leq\sqrt{X}\end{subarray}}{\sum\nolimits^{\prime}}{u^{\varrho}((1+\theta)^{\varrho}-1)\over\varrho}+O\left({\sqrt{x}\mathcal{L}^{2}\over Y}\right). |  |

The contribution coming from the term ℒ 2 ​ x / Y \mathcal{L}^{2}\sqrt{x}/Y towards the final value of ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ I 2 ​ ( x) \sum\limits_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}I_{2}(x) will be similar to ( 8.7):

(8.20) |  | ≪ ℒ 4 ​ ∑ x = 2 ν 2 ν ≤ X ∑ r ≤ P r ⋅ x ⋅ r ​ Q r 2 ​ Q 2 ≪ ℒ 5 ​ X ​ P Q = ℒ 5 ​ P 2. \ll\mathcal{L}^{4}\sum_{\begin{subarray}{c}x=2^{\nu}\\ 2^{\nu}\leq X\end{subarray}}\sum_{r\leq P}r\cdot{x\cdot rQ\over r^{2}Q^{2}}\ll{\mathcal{L}^{5}XP\over Q}=\mathcal{L}^{5}P^{2}. |  |

Using the trivial inequality 0 ≤ θ ≤ 1 0\leq\theta\leq 1

(8.21) |  | ( 1 + θ) ϱ − 1 ϱ ≪ min ⁡ ( θ, 1 | ϱ |) {(1+\theta)^{\varrho}-1\over\varrho}\ll\min\left(\theta,{1\over|\varrho|}\right) |  |

we obtain after squaring and integration in ( 8.19), abbreviating the summation conditions by ∑ ′′ \sum^{\prime\prime}, for the term I 2 ′′ ​ ( χ, x) {I_{2}}^{\prime\prime}(\chi,x) containing the zeros, the following inequality:

(8.22) |  | I 2 ′′ ​ ( χ, x) \displaystyle I^{\prime\prime}_{2}(\chi,x) | ≪ Y − 2 ​ ∑ ′′ ϱ ​ ∑ ′′ ϱ ′ ​ | x ϱ + ϱ ¯ ′ + 1 | | ϱ + ϱ ¯ ′ + 1 | ​ min ⁡ ( θ, 1 | ϱ |) ​ min ⁡ ( θ, 1 | ϱ ′ |) \displaystyle\ll Y^{-2}\underset{\varrho}{\sum\nolimits^{\prime\prime}}\underset{\varrho^{\prime}}{\sum\nolimits^{\prime\prime}}{|x^{\varrho+\overline{\varrho}^{\prime}+1}|\over|\varrho+\overline{\varrho}^{\prime}+1|}\min\left(\theta,{1\over|\varrho|}\right)\min\left(\theta,{1\over|\varrho^{\prime}|}\right) |  |

 |  | ≪ Y − 2 ​ ∑ ′′ ϱ ​ ∑ ′′ ϱ ′ δ ′ ≥ δ ​ θ ​ x 3 − δ − δ ′ 1 + | γ − γ ′ | ​ min ⁡ ( θ, 1 | ϱ |) \displaystyle\ll Y^{-2}\underset{\delta^{\prime}\geq\delta}{\underset{\varrho}{\sum\nolimits^{\prime\prime}}\underset{\varrho^{\prime}}{\sum\nolimits^{\prime\prime}}}{\theta x^{3-\delta-\delta^{\prime}}\over 1+|\gamma-\gamma^{\prime}|}\min\left(\theta,{1\over|\varrho|}\right) |  |

 |  | ≪ Y − 1 ​ ∑ ′′ ϱ ​ ℒ 2 ​ x 2 − 2 ​ δ ​ min ⁡ ( θ, 1 | ϱ |). \displaystyle\ll Y^{-1}\underset{\varrho}{\sum\nolimits^{\prime\prime}}\mathcal{L}^{2}x^{2-2\delta}\min\left(\theta,{1\over|\varrho|}\right). |  |

Using the same classification of moduli and zeros as in ( 8.9) (with x x in place of X X) we obtain by ( 8.11) and ( 8.12)

(8.23) |  | ∑ r ≤ x / Q ∑ ∗ χ ⁡ ( r) ​ I 2 ′′ ​ ( χ, x) \displaystyle\sum_{r\leq x/Q}\underset{\chi(r)}{\sum\nolimits^{*}}I^{\prime\prime}_{2}(\chi,x) | ≪ ℒ 5 ​ Y − 1 ⋅ Y x ​ max R ≤ P, 1 ≤ M ≤ X b ≤ h ≤ 1 / 2 ​ M − 1 ​ N ∗ ​ ( − h, x ​ M R ​ Q, 2 ​ R) ​ x 2 − 2 ​ h \displaystyle\ll\mathcal{L}^{5}Y^{-1}\cdot{Y\over x}\max_{\begin{subarray}{c}R\leq P,\ 1\leq M\leq X\\ b\leq h\leq 1/2\end{subarray}}M^{-1}N^{*}\!\left(\!1\!-\!h,{xM\over RQ},2R\!\right)\!x^{2-2h} |  |

 |  | ≤ ℒ 5 ​ max R ≤ P, 1 ≤ M ≤ X b ≤ h ≤ 1 / 2 ​ M − 1 ​ N ∗ ​ ( 1 − h, X ​ M R ​ Q, 2 ​ R) ​ X 1 − 2 ​ h \displaystyle\leq\mathcal{L}^{5}\max_{\begin{subarray}{c}R\leq P,\ 1\leq M\leq X\\ b\leq h\leq 1/2\end{subarray}}M^{-1}N^{*}\left(1-h,{XM\over RQ},2R\right)X^{1-2h} |  |

 |  | ≪ ℒ 5 ​ X 1 − b / 41. \displaystyle\ll\mathcal{L}^{5}X^{1-b/41}. |  |

Summing over x = 2 ν x=2^{\nu}, X 2 / 2 ≤ 2 ν ≤ X X_{2}/2\leq 2^{\nu}\leq X we finally have from ( 8.20)–( 8.23)

(8.24) |  | ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ I 2 ​ ( χ) ≪ ℒ 6 ​ X 1 − b / 41 + ℒ 5 ​ P 2 ≪ ℒ 6 ​ X 1 − b / 41. \sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}I_{2}(\chi)\ll\mathcal{L}^{6}X^{1-b/41}+\mathcal{L}^{5}P^{2}\ll\mathcal{L}^{6}X^{1-b/41}. |  |

This together with ( 8.2)–( 8.4) and ( 8.13) gives the estimate

(8.25) |  | ∫ 𝔐 | S 1 2 ​ ( α) | ​ 𝑑 α ≪ ℒ ​ ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ W 1 2 ​ ( χ) ≪ ℒ 8 ​ X 1 − b / 41. \int\limits_{\mathfrak{M}}|S^{2}_{1}(\alpha)|d\alpha\ll\mathcal{L}\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}W^{2}_{1}(\chi)\ll\mathcal{L}^{8}X^{1-b/41}. |  |

Since the above arguments were valid for any b ≥ 0 b\geq 0, we have mutatis mutandis

(8.26) |  | ∫ 𝔐 | S 0 ​ ( α) | 2 ​ 𝑑 α ≪ ℒ 8 ​ X. \int\limits_{\mathfrak{M}}|S_{0}(\alpha)|^{2}d\alpha\ll\mathcal{L}^{8}X. |  |

Thus, together with ( 8.25), we obtain by the Cauchy–Schwarz inequality

(8.27) |  | ∫ 𝔐 | S 0 ​ ( α) ​ S 1 ​ ( α) | ​ 𝑑 α ≪ ℒ 8 ​ X 1 − b / 82. \int\limits_{\mathfrak{M}}|S_{0}(\alpha)S_{1}(\alpha)|d\alpha\ll\mathcal{L}^{8}X^{1-b/82}. |  |

Summarizing, we proved

(8.28) |  | R 1 ​ ( m) = ∫ 𝔐 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α = ∫ 𝔐 S 0 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α + O ⁡ ( ℒ 8 ​ X 1 − b / 82). R_{1}(m)=\int\limits_{\mathfrak{M}}S^{2}(\alpha)e(-m\alpha)d\alpha=\int\limits_{\mathfrak{M}}S^{2}_{0}(\alpha)e(-m\alpha)d\alpha+O(\mathcal{L}^{8}X^{1-b/82}). |  |

## 9 Reduction to generalized exceptional zeros

We will continue with the investigation of S 0 2 = ( S 2 + S 3) 2 S^{2}_{0}=(S_{2}+S_{3})^{2} and show that the contribution of S 2 2 S^{2}_{2} and S 2 ​ S 3 S_{2}S_{3} to R 1 ​ ( m) R_{1}(m) are both

(9.1) |  | O η 0 ​ ( 𝔖 ⁡ ( m) ​ e − c ⁡ ( η 0) ​ H ​ X). O_{\eta_{0}}({\mathfrak{S}}(m)e^{-c(\eta_{0})H}X). |  |

If there is no Siegel zero, then ( 8.1) and ( 9.1) will imply that the study of S ⁡ ( α) S(\alpha) on the major arcs can be restricted to that of S 3 ​ ( α) S_{3}(\alpha). S 3 ​ ( α) S_{3}(\alpha) contains only a bounded number of terms, since by Lemma 4.18, there are only c ⁡ ( η 0) ​ e C ​ H c(\eta_{0})e^{CH} zeros in the definition of S 3 ​ ( α) S_{3}(\alpha). If there is a Siegel zero then we need an estimate sharper than ( 9.1). This will be made possible by the Deuring–Heilbronn phenomenon (Lemma 4.22). This shows that a part of the region, associated with the definition of S 2 ​ ( α) S_{2}(\alpha) will be free of zeros of any L L -functions with a primitive character modulo any r ≤ P r\leq P.

Now we have to be more careful than in Section 8, because it is not allowed to loose any logarithms. First we consider S 2 2 S^{2}_{2}. By the Main Lemma 1 we have with the notation of Section 2 and r ⁡ ( χ) = cond ​ χ r(\chi)=\mathrm{cond}\,\chi, r ⁡ ( χ ′) = r ′ r(\chi^{\prime})=r^{\prime}, B = ∏ p > 2 ( 1 + 2 / p ⁡ ( p − 2)) B=\prod\limits_{p>2}(1+2/p(p-2)), similarly to ( 6.5), with W 2 ​ ( χ) W_{2}(\chi) defined by ( 6.6)

(9.2) |  |  | | ∑ q ≤ p ∑ ′ 𝑎 ​ ∫ 𝔐 ⁡ ( q, a) S 2 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α | \displaystyle\bigg|\sum_{q\leq p}\underset{a}{\sum\nolimits^{\prime}}\int\limits_{\mathfrak{M}(q,a)}S^{2}_{2}(\alpha)e(-m\alpha)d\alpha\bigg| |  |

 |  | = | ∑ ∗ r ⁡ ( χ) ≤ P ∑ ∗ r ⁡ ( χ ′) ≤ P ∑ q ≤ P [r ⁡ ( χ), r ⁡ ( χ ′)] | q c ( χ, χ ′, q, m) ∫ − 1 / q Q 1 / q ​ Q S 2 ( χ, η) S 2 ( χ ′, η) e ( − m η) d η | \displaystyle=\bigg|\underset{r(\chi)\leq P}{\sum\nolimits^{*}}\ \underset{r(\chi^{\prime})\leq P}{\sum\nolimits^{*}}\sum_{\begin{subarray}{c}q\leq P\\ [r(\chi),r(\chi^{\prime})]\mid q\end{subarray}}c(\chi,\chi^{\prime},q,m)\int\limits^{1/qQ}_{-1/qQ}S_{2}(\chi,\eta)S_{2}(\chi^{\prime},\eta)e(-m\eta)d\eta\bigg| |  |

 |  | ≤ ∑ ∗ r ⁡ ( χ) ≤ P ∑ ∗ r ⁡ ( χ ′) ≤ P ∑ q = 1 [r ⁡ ( χ), r ⁡ ( χ ′)] | q ∞ | c ( χ, χ ′, q, m) | ∫ − 1 / Q [r, r ′] 1 / Q ⁡ [r, r ′] | S 2 ( χ, η) | | S 2 ( χ ′, η) | d η \displaystyle\leq\underset{r(\chi)\leq P}{\sum\nolimits^{*}}\ \underset{r(\chi^{\prime})\leq P}{\sum\nolimits^{*}}\sum^{\infty}_{\begin{subarray}{c}q=1\\ [r(\chi),r(\chi^{\prime})]\mid q\end{subarray}}|c(\chi,\chi^{\prime},q,m)|\int\limits^{1/Q[r,r^{\prime}]}_{-1/Q[r,r^{\prime}]}|S_{2}(\chi,\eta)|\,|S_{2}(\chi^{\prime},\eta)|d\eta |  |

 |  | ≤ ∑ ∗ r ⁡ ( χ) ≤ P ∑ ∗ r ⁡ ( χ ′) ≤ P B 𝔖 ( χ, χ ′, m) ( ∫ − 1 / r Q 1 / r ​ Q | S 2 ( χ, η) | 2 d η) 1 / 2 ( ∫ − 1 / r ′ Q 1 / r ′ ​ Q | S 2 ( χ ′, η) 2 | d η) 1 / 2 \displaystyle\leq\underset{r(\chi)\leq P}{\sum\nolimits^{*}}\,\underset{r(\chi^{\prime})\leq P}{\sum\nolimits^{*}}\!\!B{\mathfrak{S}}(\chi,\chi^{\prime},m)\bigg(\int\limits^{1/rQ}_{-1/rQ}\!\!|S_{2}(\chi,\eta)|^{2}d\eta\!\bigg)^{\!\!1/2}\!\bigg(\int\limits^{1/r^{\prime}Q}_{-1/r^{\prime}Q}\!\!|S_{2}(\chi^{\prime},\eta)^{2}|d\eta\!\bigg)^{\!\!1/2} |  |

 |  | ≤ B ​ 𝔖 ​ ( m) ​ ( ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ W 2 ​ ( χ)) 2. \displaystyle\leq B{\mathfrak{S}}(m)\bigg(\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}W_{2}(\chi)\bigg)^{2}. |  |

We will treat W 2 ​ ( χ) W_{2}(\chi) similarly, but somewhat simpler than W 1 ​ ( χ) W_{1}(\chi) in Section 8. For example, the tails will be estimated the same way as the essential part. The Dirichlet series appearing in the definition of S 2 ​ ( χ, η) S_{2}(\chi,\eta) is now (cf. ( 6.1)–( 6.4))

(9.3) |  | b n ′ = ∑ + ϱ ​ A ​ ( ϱ) ​ n ϱ − 1, b^{\prime}_{n}=\underset{\varrho}{\sum\nolimits^{+}}A(\varrho)n^{\varrho-1}, |  |

where by ∑ + \sum\nolimits^{+} we denote the summation conditions

 | ϱ = ϱ χ, H / ℒ < δ ≤ b, | γ | ≤ X, \varrho=\varrho_{\chi},\ H/\mathcal{L}<\delta\leq b,\ |\gamma|\leq\sqrt{X}, |  |

where H H will be a large constant to be chosen later.

In order to estimate ∑ ∑ ∗ W 2 ​ ( χ) \sum\sum^{*}W_{2}(\chi) by Gallagher’s lemma (Lemma 4.11) let us consider first for a fixed χ \chi an arbitrary interval of type ( x x, x + y x+y), where

(9.4) |  | 1 ≤ x ≤ X, 1 ≤ y ≤ Y = r ​ Q / 2, 1\leq x\leq X,\ \ 1\leq y\leq Y=rQ/2, |  |

and apply again Gallagher’s lemma (Lemma 4.11). Then we have for any χ \chi by Lemma 4.7

(9.5) |  | 1 Y ​ ∑ n = x x + y b n ′ \displaystyle{1\over Y}\sum^{x+y}_{n=x}b^{\prime}_{n} | = ∑ + ϱ ​ { ( x + y) ϱ − x ϱ ϱ ​ Y + O ⁡ ( 1 Y) } \displaystyle=\underset{\varrho\phantom{+}}{\sum\nolimits^{+}}\left\{{(x+y)^{\varrho}-x^{\varrho}\over\varrho Y}+O\left({1\over Y}\right)\right\} |  |

 |  | ≪ ∑ + ϱ ​ x − δ ​ min ⁡ ( y Y, X | ϱ | ​ Y) + Y − 1 ​ N ​ ( 1 − b, X, χ). \displaystyle\ll\underset{\varrho\phantom{+}}{\sum\nolimits^{+}}x^{-\delta}\min\left({y\over Y},{X\over|\varrho|Y}\right)+Y^{-1}N(1-b,\sqrt{X},\chi). |  |

The total contribution of the last error term to ∑ r ≤ P ∑ ∗ χ ⁡ ( r) ​ W 2 ​ ( χ) \sum\limits_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}W_{2}(\chi) after squaring, summing and integrating will be by Lemma 4.16 for any b ≤ 1 / 4 b\leq 1/4

(9.6) |  | ≪ X ​ ℒ C ​ max R ≤ P ​ ( R ​ Q) − 1 ​ N ∗ ​ ( 3 4, X, R) ≪ X ​ ℒ C ​ P 1 / 5 ​ X 3 / 10 Q ≪ ℒ C ​ X 1 / 3, \ll\sqrt{X}\mathcal{L}^{C}\max_{R\leq P}(RQ)^{-1}N^{*}\left({3\over 4},\sqrt{X},R\right)\ll{\sqrt{X}\mathcal{L}^{C}P^{1/5}X^{3/10}\over Q}\ll\mathcal{L}^{C}X^{1/3}, |  |

which is negligible.

Denoting the contribution of zeros after squaring, integrating and summing to W 2 ​ ( χ) W_{2}(\chi) by W 2 ′ ​ ( χ) W^{\prime}_{2}(\chi), let us define the positive coefficients

(9.7) |  | a ϱ = min ⁡ ( 1, X Q ​ R ​ | ϱ |) = min ⁡ ( 1, P R ​ | ϱ |) for ​ r ∈ [R, R ​ X ε]. a_{\varrho}=\min\left(1,{X\over QR|\varrho|}\right)=\min\left(1,{P\over R|\varrho|}\right)\quad\text{ for }r\in[R,RX^{\varepsilon}]. |  |

Then if b ≤ 1 / 4 b\leq 1/4 we have δ ≤ 1 / 4 \delta\leq 1/4 and so

(9.8) |  | ( W 2 ′ ​ ( χ)) 2 ≪ ∫ 1 X ( ∑ ϱ a ϱ ​ x − δ) 2 ​ 𝑑 x = ∑ ∑ a ϱ ​ a ϱ ′ ​ ∫ 1 X x − δ − δ ′ ​ 𝑑 x. (W^{\prime}_{2}(\chi))^{2}\ll\int\limits^{X}_{1}\bigg(\sum_{\varrho}a_{\varrho}x^{-\delta}\bigg)^{2}dx=\sum\sum a_{\varrho}a_{\varrho^{\prime}}\int\limits^{X}_{1}x^{-\delta-\delta^{\prime}}dx. |  |

Hence

(9.9) |  | W 2 ′ ​ ( χ) ≪ ( ∑ ϱ ∑ ϱ ′ a ϱ ​ a ϱ ′ ​ X 1 − δ − δ ′) 1 / 2 = X 1 / 2 ​ ∑ a ϱ ​ X − δ. W^{\prime}_{2}(\chi)\ll\bigg(\sum_{\varrho}\sum_{\varrho^{\prime}}a_{\varrho}a_{\varrho^{\prime}}X^{1-\delta-\delta^{\prime}}\bigg)^{1/2}=X^{1/2}\sum a_{\varrho}X^{-\delta}. |  |

Let us consider now the contribution of all zeros ϱ = ϱ χ \varrho=\varrho_{\chi}, cond ​ χ = r \mathrm{cond}\,\chi=r with the property

(9.10) |  | ( 2 μ − 1) ​ P R ν ≤ | γ | ≤ ( 2 μ + 1 − 1) ​ P R ν, r ∈ [R ν, R ν ​ X ε], R ν = X ν ​ ε ≤ P, (2^{\mu}-1){P\over R_{\nu}}\leq|\gamma|\leq(2^{\mu+1}-1){P\over R_{\nu}},\quad r\in[R_{\nu},R_{\nu}X^{\varepsilon}],\ R_{\nu}=X^{\nu\varepsilon}\leq P, |  |

to ∑ ∑ ⁡ W 2 ′ ​ ( χ) \sum\sum W^{\prime}_{2}(\chi), where ε \varepsilon is a small absolute constant, to be chosen later, depending on η \eta. Let M μ = ( 2 μ + 1 − 1) = [2 ​ X ​ R ν P] M_{\mu}=(2^{\mu+1}-1)=\left[{2\sqrt{X}R_{\nu}\over P}\right]. Let us fix now the constant b = b ⁡ ( η 0) ≤ 1 / 6 b=b(\eta_{0})\leq 1/6 in such a way that with the notation

(9.11) |  | c 2 ​ ( δ) \displaystyle c_{2}(\delta) | = 3 2 ​ ( 1 − 4 ​ δ) < 3 4 ​ ( 2 1 − 4 ​ δ + 1 ( 1 − 2 ​ δ) ​ ( 1 − 4 ​ δ)) = \displaystyle={3\over 2(1-4\delta)}<{3\over 4}\left({2\over 1-4\delta}+{1\over(1-2\delta)(1-4\delta)}\right)= |  |

 |  | = 3 ​ ( 3 − 4 ​ δ) 4 ​ ( 1 − 4 ​ δ) ​ ( 1 − 2 ​ δ) = c 1 ​ ( δ), \displaystyle={3(3-4\delta)\over 4(1-4\delta)(1-2\delta)}=c_{1}(\delta), |  |

the relation

 | c 3 ​ ( δ) = 1 − ( 4 9 − η) ​ c 1 ​ ( δ) > 0 c_{3}(\delta)=1-\left({4\over 9}-\eta\right)c_{1}(\delta)>0 |  |

should hold for 0 ≤ δ ≤ b 0\leq\delta\leq b (that is, for δ = b \delta=b), and apply Lemma 4.20. From ( 9.7)–( 9.11) in view of δ ​ c 2 ​ ( δ) ≤ b ​ c 2 ​ ( b) ≤ 3 / 4 \delta c_{2}(\delta)\leq bc_{2}(b)\leq 3/4, we obtain by partial integration with respect to δ \delta the inequality

(9.12) |  |  |  | X − 1 / 2 ∑ r ≤ P ∑ ′ χ ⁡ ( r) W 2 ′ ( χ) \displaystyle\hskip-21.33955ptX^{-1/2}\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{\prime}}W^{\prime}_{2}(\chi) |  |

 |  | ≪ \displaystyle\ll | ∑ R ν ≤ P ∑ M μ ≤ X M μ − 1 ​ ∫ H / ℒ b X − δ ​ d δ ​ N ∗ ​ ( 1 − δ, P ​ M μ R ν, R ν ​ X ε) ​ 𝑑 δ \displaystyle\sum_{R_{\nu}\leq P}\sum_{M_{\mu}\leq X}M^{-1}_{\mu}\int\limits^{b}_{H/\mathcal{L}}X^{-\delta}d_{\delta}N^{*}\left(1-\delta,{PM_{\mu}\over R_{\nu}},R_{\nu}X^{\varepsilon}\right)d\delta |  |

 |  | ≪ ε \displaystyle\ll_{\varepsilon} | max R ν ≤ P ∑ M μ ≤ X M μ − 1 { X − b N ∗ ( 1 − b, P ​ M μ R ν, R ν X ε) \displaystyle\max_{R_{\nu}\leq P}\sum_{M_{\mu}\leq X}M^{-1}_{\mu}\Bigg\{X^{-b}N^{*}\left(1-b,{PM_{\mu}\over R_{\nu}},R_{\nu}X^{\varepsilon}\right) |  |

 |  |  | + ℒ ∫ H / ℒ b N ∗ ( 1 − δ, P ​ M μ R ν, R ν X ε) X − δ d δ } \displaystyle+\mathcal{L}\int\limits^{b}_{H/\mathcal{L}}N^{*}\left(1-\delta,{PM_{\mu}\over R_{\nu}},R_{\nu}X^{\varepsilon}\right)X^{-\delta}d\delta\Bigg\} |  |

 |  | ≪ ε \displaystyle\ll_{\varepsilon} | max R ν < P ∑ M μ ≤ X M μ − 1 + b ​ c 2 ​ ( b) ​ ( 1 + ε) { ( R ν c 1 ​ ( b) P c 2 ​ ( b) R ν c 2 ​ ( b) X − 1 + 3 ​ ε) b \displaystyle\max_{R_{\nu}<P}\sum_{M_{\mu}\leq X}M^{-1+bc_{2}(b)(1+\varepsilon)}_{\mu}\bigg\{\left(R_{\nu}^{c_{1}(b)}{P^{c_{2}(b)}\over R^{c_{2}(b)}_{\nu}}X^{-1+3\varepsilon}\right)^{b} |  |

 |  |  | + ℒ ∫ H / ℒ b ( R ν c 1 ​ ( δ) P c 2 ​ ( δ) R ν c 2 ​ ( δ) ⋅ X − 1 + 3 ​ ε) δ d δ } \displaystyle+\mathcal{L}\int\limits^{b}_{H/\mathcal{L}}\left(R_{\nu}^{c_{1}(\delta)}{P^{c_{2}(\delta)}\over R_{\nu}^{c_{2}(\delta)}}\cdot X^{-1+3\varepsilon}\right)^{\delta}d\delta\bigg\} |  |

 |  | ≪ ε \displaystyle\ll_{\varepsilon} | ( P c 1 ​ ( b) ​ X − 1 + 3 ​ ε) b + ℒ ​ ∫ H / ℒ b ( P c 1 ​ ( δ) ​ X − 1 + 3 ​ ε) δ ​ 𝑑 δ \displaystyle\big(P^{c_{1}(b)}X^{-1+3\varepsilon}\big)^{b}+\mathcal{L}\int\limits^{b}_{H/\mathcal{L}}(P^{c_{1}(\delta)}X^{-1+3\varepsilon})^{\delta}d\delta |  |

 |  | ≪ ε \displaystyle\ll_{\varepsilon} | X − ( c 3 ​ ( b) − 3 ​ ε) ​ b + ℒ ​ ∫ H / ℒ b X − ( c 3 ​ ( b) − 3 ​ ε) ​ δ ​ 𝑑 δ \displaystyle X^{-(c_{3}(b)-3\varepsilon)b}+\mathcal{L}\int\limits^{b}_{H/\mathcal{L}}X^{-(c_{3}(b)-3\varepsilon)\delta}d\delta |  |

 |  | ≪ ε \displaystyle\ll_{\varepsilon} | 1 c 3 ​ ( b) − 3 ​ ε e − ( c 3 ​ ( b) − 3 ​ ε) ​ H ≪ η 0 e − c 4 ​ ( η 0) ​ H. \displaystyle{1\over c_{3}(b)-3\varepsilon}e^{-(c_{3}(b)-3\varepsilon)H}\ll_{\eta_{0}}e^{-c_{4}(\eta_{0})H}. |  |

Hence, from ( 9.2) we get

(9.13) |  | ∫ 𝔐 S 2 2 ( α) e ( − m α) d α ≪ η 0 𝔖 ( m) e − 2 ​ c 4 ​ ( η 0) ​ H. \int\limits_{\mathfrak{M}}S^{2}_{2}(\alpha)e(-m\alpha)d\alpha\ll_{\eta_{0}}{\mathfrak{S}}(m)e^{-2c_{4}(\eta_{0})H}. |  |

We can repeat the same procedure as above for S 3 ​ ( α) S_{3}(\alpha) in place of S 2 ​ ( α) S_{2}(\alpha) to obtain the same result with H = 0 H=0, that is

(9.14) |  | X − 1 / 2 ∑ r ≤ P ∑ ∗ χ ⁡ ( r) W 3 ( χ) ≪ η 0 𝔖 ( m). X^{-1/2}\sum_{r\leq P}\underset{\chi(r)}{\sum\nolimits^{*}}W_{3}(\chi)\ll_{\eta_{0}}{\mathfrak{S}}(m). |  |

Analogously to (9.2) we can estimate

(9.15) |  | ∫ 𝔐 S 2 ​ ( α) ​ S 3 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α \displaystyle\int\limits_{\mathfrak{M}}S_{2}(\alpha)S_{3}(\alpha)e(-m\alpha)d\alpha | ≪ 𝔖 ⁡ ( m) ​ ( ∑ ∗ r ⁡ ( χ) ≤ P ​ W 2 ​ ( χ)) ​ ( ∑ ∗ r ⁡ ( χ) ≤ P ​ W 3 ​ ( χ)) \displaystyle\ll{\mathfrak{S}}(m)\bigg(\underset{r(\chi)\leq P}{\sum\nolimits^{*}}W_{2}(\chi)\bigg)\bigg(\underset{r(\chi)\leq P}{\sum\nolimits^{*}}W_{3}(\chi)\bigg) |  |

 |  | ≪ η 0 𝔖 ( m) e − c 4 ​ ( η 0) ​ H X. \displaystyle\ll_{\eta_{0}}{\mathfrak{S}}(m)e^{-c_{4}(\eta_{0})H}X. |  |

Summarizing, we have from ( 9.13) and ( 9.15)

(9.16) |  | ∫ 𝔐 S 0 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α = ∫ 𝔐 S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α + O η 0 ​ ( 𝔖 ⁡ ( m) ​ e − c ⁡ ( η 0) ​ H ​ X). \int\limits_{\mathfrak{M}}S^{2}_{0}(\alpha)e(-m\alpha)d\alpha=\int\limits_{\mathfrak{M}}S^{2}_{3}(\alpha)e(-m\alpha)d\alpha+O_{\eta_{0}}({\mathfrak{S}}(m)e^{-c(\eta_{0})H}X). |  |

## 10 Effect of the generalized exceptional zeros

Finally we examine the crucial part of the contribution of the major arcs, namely

(10.1) |  | ∫ 𝔐 S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α. \int\limits_{\mathfrak{M}}S^{2}_{3}(\alpha)e(-m\alpha)d\alpha. |  |

As mentioned already in the last section, S 3 ​ ( α) S_{3}(\alpha) consists of only a bounded number of terms if H H is bounded: the main term, corresponding to the pole at s = 1 s=1 and possibly those arising from the generalized exceptional zeros ϱ \varrho with

(10.2) |  | δ ≤ H / ℒ, | γ | ≤ X. \delta\leq H/\mathcal{L},\quad|\gamma|\leq\sqrt{X}. |  |

The number of the generalized exceptional zeros in ( 10.2) is by Lemma 4.18

(10.3) |  | ≤ C ​ e 3 ​ H \leq Ce^{3H} |  |

with an absolute constant C C, where H H will be chosen as a large constant ( H = H ⁡ ( η 0) H=H(\eta_{0})) depending on η 0 \eta_{0}. (The value of H H will be determined later in the next section.) In the following we will omit in our notation the dependence of the constants on η 0 \eta_{0}. At any rate, if ϑ ≤ 0.44 \vartheta\leq 0.44, that is, η 0 = 4 / 9 − 0.44 \eta_{0}=4/9-0.44 for example, then all constants will be absolute constants.

Let ϱ 0 = 1 \varrho_{0}=1 and ϱ ν \varrho_{\nu} ( ν = 1, …, M) (\nu=1,\dots,M) denote the possible generalized exceptional zeros of L ⁡ ( s, χ ν) L(s,\chi_{\nu}) with primitive characters χ ν \chi_{\nu}, possibly equal, belonging to conductors r ν r_{\nu}. Here M = 0 M=0 is naturally possible, in which case we have only the main term corresponding to ϱ 0 = 1 \varrho_{0}=1. We list multiple zeros according to their multiplicity. Similarly to ( 6.5) we obtain

(10.4) |  |  | ∑ q ≤ P ∑ ′ 𝑎 ​ ∫ 𝔐 ⁡ ( q, a) S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α = \displaystyle\sum_{q\leq P}\underset{a}{\sum\nolimits^{\prime}}\int\limits_{\mathfrak{M}(q,a)}S^{2}_{3}(\alpha)e(-m\alpha)d\alpha= |  |

 |  | = ∑ ν = 0 M ∑ μ = 0 M ∑ q ≤ P [r ν, r μ] | q A ( ϱ ν) A ( ϱ μ) c ( χ ν, χ μ, q, m) ∫ − 1 / q Q 1 / q ​ Q T ϱ ν ( η) T ϱ μ ( η) e ( − m η) d η. \displaystyle=\sum^{M}_{\nu=0}\sum^{M}_{\mu=0}\sum_{\begin{subarray}{c}q\leq P\\ [r_{\nu},r_{\mu}]\mid q\end{subarray}}A(\varrho_{\nu})A(\varrho_{\mu})c(\chi_{\nu},\chi_{\mu},q,m)\int\limits^{1/qQ}_{-1/qQ}T_{\varrho_{\nu}}(\eta)T_{\varrho_{\mu}}(\eta)e(-m\eta)d\eta. |  |

Until now the value of P P could be arbitrary. However, if a P 0 = X ϑ 0 P_{0}=X^{\vartheta_{0}} ( ϑ 0 = 4 9 − η 0 CLOSE (\vartheta_{0}={4\over 9}-\eta_{0}, OPEN η 0 > 0) \,\eta_{0}>0) is given, we will choose P P suitably within the range ( ε ′ > 0 \varepsilon^{\prime}>0, sufficiently small)

(10.5) |  | P ∈ [P 0 ​ X − ε ′, P 0] P\in[P_{0}X^{-\varepsilon^{\prime}},P_{0}] |  |

as to satisfy the following conditions (with ε 0 = ε ′ / 10 ​ ( M + 1) 2 \varepsilon_{0}=\varepsilon^{\prime}/10(M+1)^{2}):

(10.6) |  |  | if [r μ, r ν] ≤ P then [r μ, r ν] ≤ P ​ X − ε 0 ( ν, μ ∈ [0, M]) \displaystyle\text{if $[r_{\mu},r_{\nu}]\leq P$ then $[r_{\mu},r_{\nu}]\leq PX^{-\varepsilon_{0}}\ \ (\nu,\mu\in[0,M])$} |  |

 |  | if | γ ν | ≤ P r ν ​ X ε 0 then | γ ν | ≤ P r ν ​ X − 4 ​ ε 0 ( ν ∈ [0, M]) \displaystyle\text{if $|\gamma_{\nu}|\leq{P\over r_{\nu}}X^{\varepsilon_{0}}$ then $|\gamma_{\nu}|\leq{P\over r_{\nu}}X^{-4\varepsilon_{0}}\ \ (\nu\in[0,M])$} |  |

First we will show that the effect of singularity pairs ℓ, μ \ell,\mu satisfying

(10.7) |  | P r ℓ ​ X ε 0 ≤ | γ ℓ | ≤ X {P\over r_{\ell}}X^{\varepsilon_{0}}\leq|\gamma_{\ell}|\leq\sqrt{X} |  |

will be negligible, namely

(10.8) |  | ≪ 𝔖 ⁡ ( m) ​ X 1 − ε 0 \ll{\mathfrak{S}}(m)X^{1-\varepsilon_{0}} |  |

for any pair ( ℓ, μ) (\ell,\mu) ( μ = 0, 1, …, M) (\mu=0,1,\dots,M). Namely, similarly to ( 9.4 – 9.5) we obtain by Gallagher’s lemma (Lemma 4.11)

(10.9) |  | ∫ − 1 / r ℓ Q 1 / r ℓ ​ Q | T ϱ ℓ 2 ( η) | d η \displaystyle\int\limits^{1/r_{\ell}Q}_{-1/r_{\ell}Q}|T^{2}_{\varrho_{\ell}}(\eta)|d\eta | ≪ ∫ X − r ℓ Q / 2 | 1 r ℓ ​ Q ∑ X n = X 1 x < n < x + r ℓ ​ Q / 2 n ϱ ℓ − 1 | 2 d x ≪ \displaystyle\ll\int\limits^{X}_{-r_{\ell}Q/2}\left|{1\over r_{\ell}Q}\sum^{X}_{\begin{subarray}{c}n=X_{1}\\ x<n<x+r_{\ell}Q/2\end{subarray}}n^{\varrho_{\ell}-1}\right|^{2}dx\ll |  |

 |  | ≪ X ⋅ ( X 1 − δ ℓ r ℓ ​ Q ​ | ϱ ℓ |) 2 ≪ X 1 − 2 ​ δ ℓ − 2 ​ ε 0 ≪ X 1 − 2 ​ ε 0. \displaystyle\ll X\cdot\left({X^{1-\delta_{\ell}}\over r_{\ell}Q|\varrho_{\ell}|}\right)^{2}\ll X^{1-2\delta_{\ell}-2\varepsilon_{0}}\ll X^{1-2\varepsilon_{0}}. |  |

Since we have trivially by Parseval’s identity for any μ \mu

(10.10) |  | ∫ − 1 / r Q 1 / r ​ Q | T ϱ μ 2 ( η) | d η ≤ ∫ 0 1 | T ϱ μ 2 ( η) | d η = ∑ n = X 1 X n − 2 ​ δ μ ≤ X, \int\limits^{1/rQ}_{-1/rQ}|T^{2}_{\varrho_{\mu}}(\eta)|d\eta\leq\int\limits^{1}_{0}|T^{2}_{\varrho_{\mu}}(\eta)|d\eta=\sum^{X}_{n=X_{1}}n^{-2\delta_{\mu}}\leq X, |  |

the Cauchy–Schwarz inequality yields for all q q with any ϱ ℓ \varrho_{\ell} in ( 10.7) and [r ℓ, r μ] | q [r_{\ell},r_{\mu}]\mid q

(10.11) |  | ∫ − 1 / q Q 1 / q ​ Q | T ϱ μ ( η) T ϱ ℓ ( η) | d η ≪ X 1 − ε 0. \int\limits^{1/qQ}_{-1/qQ}|T_{\varrho_{\mu}}(\eta)T_{\varrho_{\ell}}(\eta)|d\eta\ll X^{1-\varepsilon_{0}}. |  |

This, together with ( 10.3), shows ( 10.8).

So we can reduce our attention to zeros ϱ ν \varrho_{\nu} satisfying

(10.12) |  | | γ ν | ≤ P r ν ​ X − 4 ​ ε 0 |\gamma_{\nu}|\leq{P\over r_{\nu}}X^{-4\varepsilon_{0}} |  |

and we can delete with an error of O ⁡ ( 𝔖 ⁡ ( m) ​ X 1 − ε 0) O({\mathfrak{S}}(m)X^{1-\varepsilon_{0}}) all others. Let us denote the remaining zeros (satisfying ( 10.12)) by ϱ ν \varrho_{\nu}, ν = 1, …, K \nu=1,\dots,K. Now ( 10.12) implies immediately

(10.13) |  | | γ ν | X 1 = | γ ν | ​ X ε 0 X ≤ X − 3 ​ ε 0 r ν ​ Q ≤ 1 q ​ Q ​ if ​ q ≤ X 3 ​ ε 0 ​ r ν. {|\gamma_{\nu}|\over X_{1}}={|\gamma_{\nu}|X^{\varepsilon_{0}}\over X}\leq{X^{-3\varepsilon_{0}}\over r_{\nu}Q}\leq{1\over qQ}\ \text{ if }q\leq X^{3\varepsilon_{0}}r_{\nu}. |  |

We will show the following

###### Proposition.

Let ϱ ν \varrho_{\nu} satisfy ( 10.13). Then

(10.14) |  | T ϱ ν ​ ( η) ≪ ( X 1 δ ν ​ η) − 1 ≪ | η | − 1 ​ if ​ | γ ν | X 1 ≤ | η | ≤ 1 / 2. T_{\varrho_{\nu}}(\eta)\ll(X^{\delta_{\nu}}_{1}\eta)^{-1}\ll|\eta|^{-1}\ \text{ if }{|\gamma_{\nu}|\over X_{1}}\leq|\eta|\leq 1/2. |  |

###### Proof.

Let us consider the trigonometric sum

(10.15) |  | U ⁡ ( γ ν, η, y) = ∑ X 1 < n ≤ y n i ​ γ ν ​ e ​ ( n ​ η) = ∑ X 1 < n ≤ y e ⁡ ( f ⁡ ( n)), X 1 < y ≤ X, U(\gamma_{\nu},\eta,y)=\sum_{X_{1}<n\leq y}n^{i\gamma_{\nu}}e(n\eta)=\sum_{X_{1}<n\leq y}e(f(n)),\quad X_{1}<y\leq X, |  |

where

(10.16) |  | f ⁡ ( u) = γ ν 2 ​ π ​ log ⁡ u + η ​ u. f(u)={\gamma_{\nu}\over 2\pi}\log u+\eta u. |  |

For u ∈ [X 1, X] u\in[X_{1},X] we clearly have f ′ ​ ( u) = η − γ ν / 2 ​ π ​ u f^{\prime}(u)=\eta-\gamma_{\nu}/2\pi u monotonic, the same sign as η \eta and by | γ ν | / u ≤ | γ ν | / X 1 ≤ | η | |\gamma_{\nu}|/u\leq|\gamma_{\nu}|/X_{1}\leq|\eta| we have also

(10.17) |  | | η | / 2 < | f ′ ​ ( u) | < 3 ​ | η | / 2. |\eta|/2<|f^{\prime}(u)|<3|\eta|/2. |  |

Thus Lemmas 4.5 and 4.6 give

(10.18) |  | U ⁡ ( γ ν, η, y) ≪ | η | − 1. U(\gamma_{\nu},\eta,y)\ll|\eta|^{-1}. |  |

Now ( 10.14) follows by partial summation. ∎

The above proposition implies ( κ = ± 1) (\kappa=\pm 1) for any pair of remaining singularities ϱ ν, ϱ μ \varrho_{\nu},\varrho_{\mu} of L ′ / L ⁡ ( s, χ) L^{\prime}/L(s,\chi) ( ν, μ ∈ [0, K] CLOSE \,(\nu,\mu\in[0,K], OPEN q 0 = [r ν, r μ] ≤ P) q_{0}=[r_{\nu},r_{\mu}]\leq P) by ( 10.6), ( 10.12)–( 10.13), and the Main Lemma (cf. ( 7.7) and ( 7.14, t = h ​ k t=hk)

(10.19) |  |  | ∑ q ≤ X 3 ​ ε 0 ​ min ⁡ ( r ν, r μ), q ≤ P [r ν, r μ] | q | c ⁡ ( χ ν, χ μ, q, m) | ​ ∫ κ / q ​ Q κ / 2 | T ϱ ν ​ ( η) | ​ | T ϱ μ ​ ( η) | ​ d η ≪ \displaystyle\sum_{\begin{subarray}{c}q\leq X^{3\varepsilon_{0}}\min(r_{\nu},r_{\mu}),\ q\leq P\\ [r_{\nu},r_{\mu}]\mid q\end{subarray}}|c(\chi_{\nu},\chi_{\mu},q,m)|\int\limits^{\kappa/2}_{\kappa/qQ}|T_{\varrho_{\nu}}(\eta)|\,|T_{\varrho_{\mu}}(\eta)|d\eta\ll |  |

 |  | ≪ Q ​ ∑ h ≤ P / q 0 h | m ∑ k ≤ P / h ​ q 0 𝔖 ⁡ ( m) ⋅ q 0 ​ h ​ k φ ⁡ ( h) ​ φ 2 ​ ( k) ≪ Q ⁡ [r ν, r μ] ​ X ε 0 / 2 ≪ X 1 − ε 0 / 2. \displaystyle\ll Q\sum_{\begin{subarray}{c}h\leq P/q_{0}\\ h\mid m\end{subarray}}\sum_{k\leq P/hq_{0}}{\mathfrak{S}}(m)\cdot{q_{0}hk\over\varphi(h)\varphi^{2}(k)}\ll Q[r_{\nu},r_{\mu}]X^{\varepsilon_{0}/2}\ll X^{1-\varepsilon_{0}/2}. |  |

Using the trivial estimate

(10.20) |  | ∫ 0 1 | T ϱ ​ ( η) ​ T ϱ ′ ​ ( η) | ​ 𝑑 η ≤ ( ∫ 0 1 | T ϱ 2 ​ ( η) | ​ 𝑑 η) 1 / 2 ​ ( ∫ 0 1 | T ϱ ′ 2 ​ ( η) | ​ 𝑑 η) 1 / 2 ≤ X, \int\limits^{1}_{0}|T_{\varrho}(\eta)T_{\varrho^{\prime}}(\eta)|d\eta\leq\bigg(\int\limits^{1}_{0}|T^{2}_{\varrho}(\eta)|d\eta\bigg)^{1/2}\bigg(\int\limits^{1}_{0}|T^{2}_{\varrho^{\prime}}(\eta)|d\eta\bigg)^{1/2}\leq X, |  |

we obtain for the contribution of the terms with

 | q > [r ν, r μ] ​ X ε 0 = q 0 ​ X ε 0, q>[r_{\nu},r_{\mu}]X^{\varepsilon_{0}}=q_{0}X^{\varepsilon_{0}}, |  |

by ( 7.14), similarly to ( 10.19), the following bound:

(10.21) |  |  | X ​ ∑ t > X ε 0 | c ⁡ ( χ ν, χ μ, q 0 ​ t, m) | ≪ X ​ 𝔖 ​ ( m) ​ ∑ h | m 1 φ ⁡ ( h) ​ ∑ k ≥ X ε 0 / h 1 φ 2 ​ ( k) \displaystyle X\sum_{t>X^{\varepsilon_{0}}}\bigl|c(\chi_{\nu},\chi_{\mu},q_{0}t,m)\bigr|\ll X{\mathfrak{S}}(m)\sum_{h\mid m}{1\over\varphi(h)}\sum_{k\geq X^{\varepsilon_{0}}/h}{1\over\varphi^{2}(k)} |  |

 |  | ≪ X ​ 𝔖 ​ ( m) ​ ∑ h | m h φ ⁡ ( h) ​ X − ε 0 ≪ 𝔖 ⁡ ( m) ​ X 1 − ε 0 / 2, \displaystyle\ll X{\mathfrak{S}}(m)\sum_{h\mid m}{h\over\varphi(h)}X^{-\varepsilon_{0}}\ll{\mathfrak{S}}(m)X^{1-\varepsilon_{0}/2}, |  |

which is negligible.

However, if

 | X 3 ​ ε 0 ​ min ⁡ ( r ν, r μ) ≤ [r ν, r μ] ​ X ε 0 X^{3\varepsilon_{0}}\min(r_{\nu},r_{\mu})\leq[r_{\nu},r_{\mu}]X^{\varepsilon_{0}} |  |

then in ( 1.22) we have

 | U ≥ max ⁡ ( r ν ( r ν, r μ), r μ ( r ν, r μ)) ≥ X 2 ​ ε 0 \sqrt{U}\geq\max\left({r_{\nu}\over(r_{\nu},r_{\mu})},{r_{\mu}\over(r_{\nu},r_{\mu})}\right)\geq X^{2\varepsilon_{0}} |  |

and consequently by the Corollary to the Main Lemma (cf. ( 1.21)) we have

 | | 𝔖 ⁡ ( χ ν, χ μ, m) | ≤ 𝔖 ⁡ ( m) ​ X − ε 0. \bigl|{\mathfrak{S}}(\chi_{\nu},\chi_{\mu},m)\bigr|\leq{\mathfrak{S}}(m)X^{-\varepsilon_{0}}. |  |

This implies for the possible contribution of the intermediate terms with

 | X 3 ​ ε 0 ​ min ⁡ ( r ν, r μ) ≤ q ≤ [r ν, r μ] ​ X ε 0 X^{3\varepsilon_{0}}\min(r_{\nu},r_{\mu})\leq q\leq[r_{\nu},r_{\mu}]X^{\varepsilon_{0}} |  |

similarly to ( 10.19) the estimate (cf. ( 7.2) and ( 7.7) in the Main Lemma)

 | O ⁡ ( X ​ 𝔖 ​ ( m) ​ X − ε 0) ≪ 𝔖 ⁡ ( m) ​ X 1 − ε 0. O\bigl(X{\mathfrak{S}}(m)X^{-\varepsilon_{0}}\bigr)\ll{\mathfrak{S}}(m)X^{1-\varepsilon_{0}}. |  |

Summarizing, we have for all pairs ν, μ ∈ [0, K] \nu,\mu\in[0,K]:

(10.22) |  | ∑ q ≤ P [r ν, r μ] | q | c ⁡ ( χ ν, χ μ, q, m) | ∫ κ / q ​ Q κ / 2 | T ϱ ν ​ ( η) ​ T ϱ μ ​ ( η) | 𝑑 η ≪ 𝔖 ⁡ ( m) ​ X 1 − ε 0 / 2. \sum_{\begin{subarray}{c}q\leq P\\ [r_{\nu},r_{\mu}]\mid q\end{subarray}}|c(\chi_{\nu},\chi_{\mu},q,m)|\int\limits^{\kappa/2}_{\kappa/qQ}|T_{\varrho_{\nu}}(\eta)T_{\varrho_{\mu}}(\eta)|d\eta\ll{\mathfrak{S}}(m)X^{1-\varepsilon_{0}/2}. |  |

Now ( 10.22) means that we can extend the integration on the right-hand side of ( 10.4), for the remaining singularities ϱ ν \varrho_{\nu}, ϱ μ \varrho_{\mu} ( ν, μ = 0, 1, …, K \nu,\mu=0,1,\dots,K) for the full interval [0, 1] [0,1] in place of [− 1 / q Q, 1 / q Q] [-1/qQ,1/qQ], with an error of size O ⁡ ( 𝔖 ⁡ ( m) ​ X 1 − ε 0 / 2) O(\mathfrak{S}(m)X^{1-\varepsilon_{0}/2}). Here the full integral can be expressed by the Γ \Gamma -function (cf. Lemmas 4.8 – 4.9) as follows:

(10.23) |  | ∫ 0 1 T ϱ ν ​ ( η) ​ T ϱ μ ​ ( η) ​ e ​ ( − m ​ η) ​ 𝑑 η = Γ ⁡ ( ϱ ν) ​ Γ ​ ( ϱ μ) Γ ⁡ ( ϱ ν + ϱ μ) ​ m ϱ ν + ϱ μ − 1 + O ⁡ ( X 1). \int\limits^{1}_{0}T_{\varrho_{\nu}}(\eta)T_{\varrho_{\mu}}(\eta)e(-m\eta)d\eta={\Gamma(\varrho_{\nu})\Gamma(\varrho_{\mu})\over\Gamma(\varrho_{\nu}+\varrho_{\mu})}m^{\varrho_{\nu}+\varrho_{\mu}-1}+O(X_{1}). |  |

Further, as [r ν, r μ) < P [r_{\nu},r_{\mu})<P implies [r ν, r μ] ​ X ε 0 < P [r_{\nu},r_{\mu}]X^{\varepsilon_{0}}<P, the effect of all terms with q ≥ P q\geq P is by ( 10.21) negligible. So, from ( 10.1), ( 10.4), ( 10.8), ( 10.19), ( 10.22) and ( 10.23) we have

(10.24) |  |  | ∫ 𝔐 S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α \displaystyle\int\limits_{\mathfrak{M}}S^{2}_{3}(\alpha)e(-m\alpha)d\alpha |  |

 |  | = ∑ K ν = 0 ∑ K μ = 0 [r ν, r μ] ≤ P ​ 𝔖 ​ ( χ ν, χ μ, m) ​ A ​ ( ϱ ν) ​ A ​ ( ϱ μ) ​ Γ ⁡ ( ϱ ν) ​ Γ ​ ( ϱ μ) Γ ⁡ ( ϱ ν + ϱ μ) ​ m ϱ ν + ϱ μ − 1 + O ⁡ ( X 1 − ε 0 / 2). \displaystyle=\underset{[r_{\nu},r_{\mu}]\leq P}{\sum^{K}_{\nu=0}\sum^{K}_{\mu=0}}{\mathfrak{S}}(\chi_{\nu},\chi_{\mu},m)A(\varrho_{\nu})A(\varrho_{\mu}){\Gamma(\varrho_{\nu})\Gamma(\varrho_{\mu})\over\Gamma(\varrho_{\nu}+\varrho_{\mu})}m^{\varrho_{\nu}+\varrho_{\mu}-1}+O(X^{1-\varepsilon_{0}/2}). |  |

Since we have for the generalized exceptional singularities

(10.25) |  | Γ ⁡ ( ϱ ν) ​ Γ ​ ( ϱ μ) Γ ⁡ ( ϱ ν + ϱ μ) ≪ ( max ( | γ ν |, | γ μ |)) − 1 / 2 {\Gamma(\varrho_{\nu})\Gamma(\varrho_{\mu})\over\Gamma(\varrho_{\nu}+\varrho_{\mu})}\ll\big(\max(|\gamma_{\nu}|,|\gamma_{\mu}|)\big)^{-1/2} |  |

we can further learn from our formula ( 10.24) that up to an error of O ⁡ ( 𝔖 ⁡ ( m) ​ X / T 0) O({\mathfrak{S}}(m)X/\sqrt{T_{0}}), zeros of height

(10.26) |  | | γ | ≥ T 0 |\gamma|\geq T_{0} |  |

may be neglected as well. If we have no Siegel zero, then the error 𝔖 ⁡ ( m) ​ X / T 0 {\mathfrak{S}}(m)X/\sqrt{T_{0}} will be admissible if we choose T 0 T_{0} as a large constant. This can be seen from ( 10.24) since we have our main term corresponding to ( ϱ 0, ϱ 0) = ( 1, 1) (\varrho_{0},\varrho_{0})=(1,1) in the sum – which yields 𝔖 ⁡ ( m) ​ m {\mathfrak{S}}(m)m. Therefore, in addition to ( 10.24) the following formula summarizes the results of this section:

(10.27) |  |  | ∫ 𝔐 S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α \displaystyle\int\limits_{\mathfrak{M}}\!S^{2}_{3}(\alpha)e(-m\alpha)d\alpha |  |

 |  | = ∑ K ν = 0 | γ ν | ≤ T 0 ∑ K μ = 0 | γ μ | ≤ T 0 [r ν, r μ] ≤ P ​ 𝔖 ​ ( χ ν, χ μ, m) ​ A ​ ( ϱ ν) ​ A ​ ( ϱ μ) ​ Γ ⁡ ( ϱ ν) ​ Γ ​ ( ϱ μ) Γ ⁡ ( ϱ ν + ϱ μ) ​ m ϱ ν + ϱ μ − 1 \displaystyle=\underset{[r_{\nu},r_{\mu}]\leq P}{\sum^{K}_{\begin{subarray}{c}\nu=0\\ |\gamma_{\nu}|\leq T_{0}\end{subarray}}\sum^{K}_{\begin{subarray}{c}\mu=0\\ |\gamma_{\mu}|\leq T_{0}\end{subarray}}}\!{\mathfrak{S}}(\chi_{\nu},\chi_{\mu},m)A(\varrho_{\nu})A(\varrho_{\mu}){\Gamma(\varrho_{\nu})\Gamma(\varrho_{\mu})\over\Gamma(\varrho_{\nu}+\varrho_{\mu})}m^{\varrho_{\nu}+\varrho_{\mu}-1} |  |

 |  | + O ⁡ ( 𝔖 ⁡ ( m) ​ X / T 0) + O ⁡ ( X 1 − ε 0 / 2). \displaystyle\quad+O({\mathfrak{S}}(m)X/\sqrt{T_{0}})+O(X^{1-\varepsilon_{0}/2}). |  |

The relations ( 10.24), ( 10.27) actually prove the explicit formula ( 2.10) if we take into account ( 1.21)–( 1.22) which follows from the Main Lemma 1. Therefore our Theorem 1 is proved.

## 11 Proof of Theorem 2

Suppose that after choosing suitably P P in ( 10.5)–( 10.6) we have the following case:

There is a unique real primitive character χ 1 ​ ( mod ​ r 1) \chi_{1}(\,\text{\rm mod}\;r_{1}), r 1 ≤ P r_{1}\leq P such that L ⁡ ( s, χ 1) L(s,\chi_{1}) has a real zero ϱ 1 = β 1 = 1 − δ 1 \varrho_{1}=\beta_{1}=1-\delta_{1} with

(11.1) |  | δ 1 ≤ h / log ⁡ X = h / ℒ, \delta_{1}\leq h/\log X=h/\mathcal{L}, |  |

where h h is a constant, to be chosen at the end of the section which may depend on η 0 \eta_{0}.

We remark here that h h will be a small constant and the constant H H (cf. ( 2.8), ( 10.2)) will be a large constant depending on h h. We also remark that by the procedure in ( 10.5)–( 10.6) we will have actually r 1 = [1, r 1] ≤ P ​ X − ε 0 r_{1}=[1,r_{1}]\leq PX^{-\varepsilon_{0}}.

In this case we will show, using the Deuring–Heilbronn phenomenon (Lemma 4.22) that S 3 ​ ( α) S_{3}(\alpha) consists exactly of two terms: those corresponding to ϱ 0 = 1 \varrho_{0}=1 and the Siegel zero ϱ 1 \varrho_{1} above. Further also some part of the region

 | ℛ = { s; σ ≥ 1 − b, | t | ≤ X } \mathcal{R}=\big\{s;\sigma\geq 1-b,|t|\leq\sqrt{X}\big\} |  |

associated with the definition of terms in S 2 ​ ( α) S_{2}(\alpha) will be free of zeros of L ⁡ ( s, χ, r) L(s,\chi,r) if r ≤ P r\leq P. The size of the actual zero-free part of ℛ \mathcal{R} will depend on δ 1 \delta_{1}, that is, how close the real zero ϱ 1 = β 1 \varrho_{1}=\beta_{1} lies to 1 1.

We remark first that in case of an arbitrary primitive character χ 2 \chi_{2} mod ​ r 2 ≤ P \,\text{\rm mod}\;r_{2}\leq P and ϱ 2 = 1 − δ 2 + i ​ γ 2 \varrho_{2}=1-\delta_{2}+i\gamma_{2} with

(11.2) |  | δ 2 ≤ H ℒ, | γ 2 | ≤ X, \delta_{2}\leq{H\over\mathcal{L}},\quad|\gamma_{2}|\leq\sqrt{X}, |  |

we have in Lemma 4.22 the “trivial” estimate

(11.3) |  | Y = ( r 1 2 ​ r 2 ​ k ​ ( | γ | + 2) 2) 3 8 ≪ ( P 5 ​ X) 3 8 ≤ X 29 24, Y=(r^{2}_{1}r_{2}k(|\gamma|+2)^{2})^{3\over 8}\ll(P^{5}X)^{3\over 8}\leq X^{29\over 24}, |  |

where k = cond ​ χ 1 ​ χ 2 k=\mathrm{cond}\,\chi_{1}\chi_{2}. This implies in case of δ 2 < 1 / 200 \delta_{2}<1/200 by ( 4.20)

(11.4) |  | h ≥ ℒ ​ δ 1 ≥ 24 29 ​ δ 1 ​ log ⁡ Y > 1 2 ​ Y − ( 1 + ε) 1 − 6 ​ δ 2 ​ δ 2 > 1 2 ​ X − 5 4 ​ δ 2. h\geq\mathcal{L}\delta_{1}\geq{24\over 29}\delta_{1}\log Y>{1\over 2}Y^{-{(1+\varepsilon)\over 1-6\delta_{2}}\delta_{2}}>{1\over 2}X^{-{5\over 4}\delta_{2}}. |  |

From this we obtain

(11.5) |  | δ 2 ​ ℒ > 4 5 ​ log ⁡ 1 2 ​ h = H 0 ​ ( h). \delta_{2}\mathcal{L}>{4\over 5}\log{1\over 2h}=H_{0}(h). |  |

This means that choosing H = H 0 ​ ( h) H=H_{0}(h), the existence of a Siegel zero will really imply that there are no other zeros in the region ( 11.2).

By Y ≥ r 1 3 / 4 Y\geq r^{3/4}_{1}, the ineffective theorem of Siegel (Lemma 4.14) implies for any ε 1 \varepsilon_{1}

(11.6) |  | δ 1 ≥ max ⁡ ( P − ε 1, Y − ε 1) ​ if ​ X ≥ X 1 ​ ( ε), Y ≥ Y 1 ​ ( ε). \delta_{1}\geq\max(P^{-\varepsilon_{1}},Y^{-\varepsilon_{1}})\ \text{ if }X\geq X_{1}(\varepsilon),\ Y\geq Y_{1}(\varepsilon). |  |

So we have for δ < 1 / 200 \delta<1/200 from ( 4.21) the inequality

(11.7) |  | δ 2 1 − 6 ​ δ 2 > ( 1 − ε 1) ​ log ⁡ 2 3 ​ δ 1 ​ log ⁡ Y log ⁡ Y. {\delta_{2}\over 1-6\delta_{2}}>(1-\varepsilon_{1}){\log{2\over 3\delta_{1}\log Y}\over\log Y}. |  |

Since by ( 11.6) the right-hand side is here < ε 1 <\varepsilon_{1}, ( 11.7) implies that

(11.8) |  | δ 2 > ( 1 − 7 ​ ε 1) ​ log ⁡ 2 3 ​ δ 1 ​ log ⁡ Y log ⁡ Y ​ = def ​ φ 0 ​ ( Y) \delta_{2}>(1-7\varepsilon_{1}){\log{2\over 3\delta_{1}\log Y}\over\log Y}\overset{\mathrm{def}}{=}\varphi_{0}(Y) |  |

for any ε 1 \varepsilon_{1}, Y ≥ Y ⁡ ( ε 1) Y\geq Y(\varepsilon_{1}). Here φ 0 ​ ( Y) < ε \varphi_{0}(Y)<\varepsilon, if Y ≥ Y 2 ​ ( ε, ε 1) Y\geq Y_{2}(\varepsilon,\varepsilon_{1}). Let us denote now (cf. ( 11.3))

(11.9) |  | ( δ 1 ​ ℒ) − 1 = G 1 ≥ h − 1, G ⁡ ( Y) = G = 2 3 ​ δ 1 ​ log ⁡ Y > G 1 2. (\delta_{1}\mathcal{L})^{-1}=G_{1}\geq h^{-1},\quad G(Y)=G={2\over 3\delta_{1}\log Y}>{G_{1}\over 2}. |  |

We recall (cf. [20]) that effectively δ 1 ≫ r − 1 / 2 1 \delta_{1}\gg r^{-1/2}_{1}, consequently r 1 ≫ ℒ 2 r_{1}\gg\mathcal{L}^{2}. Further by the Main Lemma 1 (cf. ( 7.5)–( 7.7) and ( 1.21)–( 1.22))

 | 𝔖 ⁡ ( χ 0, χ 0, m) \displaystyle{\mathfrak{S}}(\chi_{0},\chi_{0},m) | = \displaystyle= | 𝔖 ⁡ ( m) \displaystyle{\mathfrak{S}}(m) |  |

(11.10) |  | 𝔖 ⁡ ( χ 1, χ 0, m) \displaystyle{\mathfrak{S}}(\chi_{1},\chi_{0},m) | ≪ \displaystyle\ll | r 1 φ 2 ​ ( r 1) ​ 𝔖 ​ ( m) ≪ 𝔖 ⁡ ( m) ​ log ⁡ r 1 r 1, \displaystyle{r_{1}\over\varphi^{2}(r_{1})}{\mathfrak{S}}(m)\ll{\mathfrak{S}}(m){\log r_{1}\over r_{1}}, |  |

 | | 𝔖 ⁡ ( χ, χ ′, m) | \displaystyle|{\mathfrak{S}}(\chi,\chi^{\prime},m)| | ≤ \displaystyle\leq | 𝔖 ⁡ ( m) ​ for any ​ χ, χ ′. \displaystyle{\mathfrak{S}}(m)\ \text{ for any }\chi,\chi^{\prime}. |  |

Hence the asymptotic formula ( 10.24) tells us that

(11.11) |  |  | ∫ 𝔐 S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α \displaystyle\int\limits_{\mathfrak{M}}S^{2}_{3}(\alpha)e(-m\alpha)d\alpha |  |

 |  | = 𝔖 ⁡ ( m) ​ m + 𝔖 ⁡ ( χ 1, χ 1, m) ​ Γ ​ ( 1 − δ 1) 2 Γ ⁡ ( 2 − 2 ​ δ 1) ​ m 1 − 2 ​ δ 1 \displaystyle={\mathfrak{S}}(m)m+{\mathfrak{S}}(\chi_{1},\chi_{1},m){\Gamma(1-\delta_{1})^{2}\over\Gamma(2-2\delta_{1})}m^{1-2\delta_{1}} |  |

 |  | + O ⁡ ( 𝔖 ⁡ ( m) ​ m ​ log ⁡ r 1 r 1) + O ⁡ ( X 1 − ε 0 / 2) \displaystyle\quad+O\left({\mathfrak{S}}(m)m{\log r_{1}\over r_{1}}\right)+O(X^{1-\varepsilon_{0}/2}) |  |

 |  | ≥ 𝔖 ( m) m ( 1 − e − 2 ​ δ 1 ​ log ⁡ m + O ( δ 1) + O ( X − ε 0 / 2)) \displaystyle\geq{\mathfrak{S}}(m)m(1-e^{-2\delta_{1}\log m}+O(\delta_{1})+O(X^{-\varepsilon_{0}/2})) |  |

 |  | > 1.9 ⋅ 𝔖 ⁡ ( m) ​ m G 1 \displaystyle>1.9\cdot{{\mathfrak{S}}(m)m\over G_{1}} |  |

if m > X 1 − ε 0 / 3 m>X^{1-\varepsilon_{0}/3}, since the last error term is negligible in view of Siegel’s theorem (cf. ( 11.6)).

Now, using the zero-free region ( 11.8) we try to show that, possibly for all [m ∈ X / 2, X] [m\in X/2,X]

(11.12) |  | | ∫ 𝔐 ( S 2 2 ​ ( α) + 2 ​ S 2 ​ S 3 ​ ( α)) ​ e ​ ( − m ​ α) ​ 𝑑 α | ≤ 5 ​ 𝔖 ​ ( m) ​ m 6 ​ G 1. \bigg|\int\limits_{\mathfrak{M}}\big(S^{2}_{2}(\alpha)+2S_{2}S_{3}(\alpha)\big)e(-m\alpha)d\alpha\bigg|\leq{5{\mathfrak{S}}(m)m\over 6G_{1}}. |  |

We remark that ( 11.12) is sufficient to show our Theorem, in view of the notation ( 6.3)–( 6.4), the final result of Section 8 ( 8.28) and G 1 − 1 ≥ P − ε G^{-1}_{1}\geq P^{-\varepsilon} (cf. ( 11.6)). It would actually be possible to show ( 11.12) for all m m for some smaller value of ϑ \vartheta than 4 / 9 4/9 ( ϑ = 16 / 39) (\vartheta=16/39). However, we can also show for any ϑ < 4 / 9 \vartheta<4/9 that ( 11.12) holds for all but

(11.13) |  | O ⁡ ( X 1 + ε P) O\left({X^{1+\varepsilon}\over P}\right) |  |

values m ∈ [X / 2, X] m\in[X/2,X] which is an admissible size exceptional set; the same as or better than the cardinality of the exceptional set arising from the minor arcs (cf. ( 5.3)).

Let us investigate now ∫ ( S 2 2 ​ ( α) + 2 ​ S 2 ​ ( α) ​ S 3 ​ ( α)) ​ e ​ ( − m ​ α) ​ 𝑑 α \int(S^{2}_{2}(\alpha)+2S_{2}(\alpha)S_{3}(\alpha))e(-m\alpha)d\alpha. The number of zeros appearing in S 0 ​ ( α) S_{0}(\alpha) is by Lemma 4.18

(11.14) |  | ≪ ( P 2 ​ X) ( 2 + ε) ​ b ≪ X 3 ​ b \ll(P^{2}\sqrt{X})^{(2+\varepsilon)b}\ll X^{3b} |  |

and b b can be chosen arbitrarily small. The number of pairs of zeros is consequently ≪ X 6 ​ b \ll X^{6b}.

In the present section we will suppose b < b 1 ​ ( η 0) b<b_{1}(\eta_{0}) a fixed constant, whose value will be determined later. First we can observe that the total contribution of all zeros ϱ \varrho of all L ⁡ ( s, χ) L(s,\chi) belonging to primitive characters χ ​ mod ​ r \chi\,\text{\rm mod}\;r with

(11.15) |  | 0 ≤ δ ≤ b, | γ | > P R ​ X b, r ∈ [R, R ​ X b], R ≤ P 0\leq\delta\leq b,\quad|\gamma|>{P\over R}X^{b},\quad r\in[R,RX^{b}],\quad R\leq P |  |

to ∑ ∑ ⁡ W 2 ′ ​ ( x) \sum\sum W^{\prime}_{2}(x) in ( 9.12) is – according to the argumentation in ( 9.12) – for b ≤ 1 / 8 b\leq 1/8:

(11.16) |  | ≪ X 1 / 2 ​ ∑ μ 2 μ ≥ X b ( 2 μ) − 1 + b ​ c 2 ​ ( b) ​ ( 1 + ε) ​ e − c ​ H ≪ X 1 / 2 − b / 2. \ll X^{1/2}\sum_{\begin{subarray}{c}\mu\\ 2^{\mu}\geq X^{b}\end{subarray}}(2^{\mu})^{-1+bc_{2}(b)(1+\varepsilon)}e^{-cH}\ll X^{1/2-b/2}. |  |

This implies for their total contribution to ∫ S 2 2 + 2 ​ S 2 ​ S 3 \int S^{2}_{2}+2S_{2}S_{3}, by ( 9.12) and ( 9.14), the estimate

(11.17) |  | ≪ 𝔖 ⁡ ( m) ​ X 1 − b / 2 = o ⁡ ( 𝔖 ⁡ ( m) ⋅ m G) \ll{\mathfrak{S}}(m)X^{1-b/2}=o\left({{\mathfrak{S}}(m)\cdot m\over G}\right) |  |

(naturally S 3 ​ ( α) S_{3}(\alpha) is completely known by Section 10 explicitly, since it has now only the two terms ϱ 0 = 1 \varrho_{0}=1, ϱ 1 = 1 − δ 1 \varrho_{1}=1-\delta_{1}).

So we will suppose from now on, in this section, that

(11.18) |  | 0 ≤ δ ≤ b, | γ | ≤ P R ​ X b, r ∈ [R, R ​ X b] 0\leq\delta\leq b,\quad|\gamma|\leq{P\over R}X^{b},\quad r\in[R,RX^{b}] |  |

for the zeros associated with S 2 ​ ( α) S_{2}(\alpha) (cf. ( 6.3)–( 6.4)).

Further we can suppose that for the given m m we have for all χ ν ​ ( mod ​ r ν) \chi_{\nu}(\,\text{\rm mod}\;r_{\nu}), χ μ ​ ( mod ​ r μ) \chi_{\mu}(\,\text{\rm mod}\;r_{\mu})

(11.19) |  | | 𝔖 ⁡ ( χ ν, χ μ, m) | ≥ X − b ​ 𝔖 ​ ( m) |{\mathfrak{S}}(\chi_{\nu},\chi_{\mu},m)|\geq X^{-b}{\mathfrak{S}}(m) |  |

since for the total contribution of pairs not satisfying ( 11.19) we have directly by ( 9.2) and ( 9.12)–( 9.14) the estimate

(11.20) |  | B ​ 𝔖 ​ ( m) ​ X − b ​ { ( ∑ ∗ r ⁡ ( χ) ≤ P ​ W 2 ​ ( χ)) 2 + ∑ r ⁡ ( χ) ≤ P ∑ ∗ r ⁡ ( χ ′) ≤ P ​ W 2 ​ ( χ) ​ W 3 ​ ( χ ′) } ≪ X 1 − b ​ 𝔖 ​ ( m). B{\mathfrak{S}}(m)X^{-b}\Biggl\{\!\biggl(\underset{r(\chi)\leq P}{\sum\nolimits^{*}}W_{2}(\chi)\biggr)^{\!2}\!+\!\sum_{r(\chi)\leq P}\ \underset{r(\chi^{\prime})\leq P}{\sum\nolimits^{*}}W_{2}(\chi)W_{3}(\chi^{\prime})\!\Biggr\}\ll X^{1-b}{\mathfrak{S}}(m). |  |

However, according to the Main Lemma, ( 11.19) implies (see ( 1.21)–( 1.22))

(11.21) |  | U ⁡ ( χ ν, χ μ, m) ≪ X 3 ​ b. U(\chi_{\nu},\chi_{\mu},m)\ll X^{3b}. |  |

In what follows we will delete pairs in S 2 2 S^{2}_{2} contradicting to ( 11.19). ( 11.21) implies also

(11.22) |  | X − 3 b / 2 ≪ r ν / r μ ≪ X 3 ​ b / 2. X^{-3b/2}\ll r_{\nu}/r_{\mu}\ll X^{3b/2}. |  |

Let us consider first the easier case S 3 ⋅ S 2 S_{3}\cdot S_{2}. In this case the term ( ϱ j, χ j, r j) (\varrho_{j},\chi_{j},r_{j}) coming from S 3 S_{3} is either

(11.23) |  | ( 1, χ 0, 1) ​ or ​ ( 1 − δ 1, χ 1, r 1) ( j = 0 ​ or ​ 1). (1,\chi_{0},1)\ \text{ or }\ (1-\delta_{1},\chi_{1},r_{1})\quad(j=0\text{ or }1). |  |

Let us suppose first that j = 1 j=1. If for the term ( ϱ, χ, r) (\varrho,\chi,r) ( 11.19) is false we can delete it. So we can suppose here by ( 1.21)–( 1.22) that we have for all ( ϱ, χ, r) (\varrho,\chi,r) in S 2 S_{2}

(11.24) |  | r j X − 3 b / 2 ≪ r ≪ r j X 3 ​ b / 2, cond χ χ j ≪ X 3 ​ b r_{j}X^{-3b/2}\ll r\ll r_{j}X^{3b/2},\quad\mathrm{cond}\,\chi\chi_{j}\ll X^{3b} |  |

at least for the examination of S 2 ⋅ S 31 S_{2}\cdot S_{31}, the part coming from χ 1 \chi_{1}. Thus we have for any pair χ, χ ′ \chi,\chi^{\prime} of characters remaining in S 2 S_{2} after the deletion

(11.25) |  | cond ​ χ ​ χ ¯ ′ ≤ cond ​ χ 1 ​ χ ⋅ cond ​ χ 1 ​ χ ′ ¯ ≤ X 6 ​ b. \mathrm{cond}\,\chi\overline{\chi}^{\prime}\leq\mathrm{cond}\,\chi_{1}\chi\cdot\mathrm{cond}\,\overline{\chi_{1}\chi^{\prime}}\leq X^{6b}. |  |

Let us denote the corresponding new set by S 21 ′ S^{\prime}_{21}. Now we are able to use our density Lemma 4.21, more exactly ( 4.18). If the constant b b is chosen sufficiently small in dependence on η 0 \eta_{0} we have for any R ν = X ν ​ b ≤ P R_{\nu}=X^{\nu b}\leq P, δ ≤ b \delta\leq b

(11.26) |  |  | ∑ R ν < r ν < R ν ​ X b r ν ≤ P ∑ ∗ χ ν ​ ( r ν) ∈ S 21 ′ ​ N ​ ( 1 − δ, P R ν ​ X b, χ ν) \displaystyle\sum_{\begin{subarray}{c}R_{\nu}<r_{\nu}<R_{\nu}X^{b}\\ r_{\nu}\leq P\end{subarray}}\ \underset{\chi_{\nu}(r_{\nu})\in S^{\prime}_{21}}{\sum\nolimits^{*}}N\left(1-\delta,{P\over R_{\nu}}X^{b},\chi_{\nu}\right) |  |

 |  | ≪ b ( P X 18 ​ b) ( 3 / 4 + b 3) ​ δ ≪ b P ( 3 / 4 + 2 ​ b 3) ​ δ ≪ η 0, b X δ / 3. \displaystyle\ll_{b}(PX^{18b})^{(3/4+\sqrt[3]{b})\delta}\ll_{b}P^{(3/4+2\sqrt[3]{b})\delta}\ll_{\eta_{0},b}X^{\delta/3}. |  |

Thus we obtain by the Deuring–Heilbronn phenomenon ( 11.8), similarly to ( 9.12)

(11.27) |  | S 231 ∗ = def X − 1 2 ∑ r ν ≤ P ∑ χ ν ​ ( r ν) ∈ S 21 ′ W 2 ′ ( χ) ≪ η, b X − ( 2 / 3) ​ φ 0 ​ ( Y). S^{*}_{231}\overset{\rm def}{=}X^{-{1\over 2}}\sum_{r_{\nu}\leq P}\sum_{\chi_{\nu}(r_{\nu})\in S^{\prime}_{21}}W^{\prime}_{2}(\chi)\ll_{\eta,b}X^{-(2/3)\varphi_{0}(Y)}. |  |

Now we will show an estimate sharper than ( 11.3) for Y Y. In view of ( 11.22) and ( 11.18) we have for any pair ( ϱ, χ) (\varrho,\chi), χ ​ mod ​ r \chi\,\text{\rm mod}\;r, remaining in S 21 ′ S^{\prime}_{21}

(11.28) |  | Y = ( r 1 2 ​ r ​ k ​ ( | γ | + 2) 2) 3 / 8 ≪ ( r 3 ​ X 6 ​ b ​ ( P r ​ X 2 ​ b) 2) 3 8 ≪ P 9 8 ​ X 4 ​ b ≤ X. Y=\big(r^{2}_{1}rk(|\gamma|+2)^{2}\big)^{3/8}\ll\left(r^{3}X^{6b}\left({P\over r}X^{2b}\right)^{2}\right)^{3\over 8}\ll P^{9\over 8}X^{4b}\leq\sqrt{X}. |  |

Substituting this into ( 11.27) we obtain

(11.29) |  | S 231 ∗ \displaystyle S^{*}_{231} | ≪ η 0, b exp ( − 2 3 ℒ ( 1 − 7 ​ ε 1) ​ log ⁡ G ⁡ ( X) ℒ / 2) ≪ η 0, b G ( X) − 4 / 3 + 10 ε 1 \displaystyle\ll_{\eta_{0},b}\exp\left(-{2\over 3}\mathcal{L}{(1-7\varepsilon_{1})\log G(\sqrt{X})\over\mathcal{L}/2}\right)\ll_{\eta_{0},b}G(\sqrt{X})^{-4/3+10\varepsilon_{1}} |  |

 |  | ≪ η 0, b G ( X) − 5 4 \displaystyle\ll_{\eta_{0},b}G(\sqrt{X})^{-\frac{5}{4}} |  |

if ε 1 < 1 / 120 \varepsilon_{1}<1/120. Now let us fix a small b b in dependence on η 0 \eta_{0}. If now h h is chosen small enough in dependence on η 0 \eta_{0}, then G ⁡ ( X) = 4 ​ G 1 / 3 ≥ 4 ​ h 1 − 1 / 3 G(\sqrt{X})=4G_{1}/3\geq 4h_{1}^{-1}/3 will be sufficiently large in dependence on η 0 \eta_{0}, and so we obtain from ( 11.29) finally

(11.30) |  | | ∫ 𝔐 S 2 ​ ( α) ​ S 31 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α | < 𝔖 ⁡ ( m) ​ X 12 ​ G 1 < 𝔖 ⁡ ( m) ​ m 6 ​ G 1. \bigg|\int\limits_{\mathfrak{M}}S_{2}(\alpha)S_{31}(\alpha)e(-m\alpha)d\alpha\bigg|<{{\mathfrak{S}}(m)X\over 12G_{1}}<{{\mathfrak{S}}(m)m\over 6G_{1}}. |  |

If we take ϱ = ϱ 0 = 1 \varrho=\varrho_{0}=1, χ 0 \chi_{0}, r 0 = 1 r_{0}=1, then we have by ( 11.24) for the undeleted terms

(11.31) |  | r ≪ X 3 ​ b / 2. r\ll X^{3b/2}. |  |

Consequently, using ( 4.19) in place of ( 4.18) we obtain the improved estimate X 10 ​ b ​ δ X^{10b\delta} in place of ( 11.26). Accordingly we obtain the estimate X − ( 1 − 10 ​ b) ​ φ 0 ​ ( Y) X^{-(1-10b)\varphi_{0}(Y)} instead of ( 11.27). Further,

(11.32) |  | Y = ( r 1 2 ​ r ​ k ​ ( | γ | + 2) 2) 3 / 8 ≪ ( P 3 ​ r 2 ​ ( P r ​ X 2 ​ b) 2) 3 / 8 = P 15 8 ​ X 3 ​ b 2 ≤ X 5 6. Y=\bigl(r^{2}_{1}rk(|\gamma|+2)^{2}\bigr)^{3/8}\ll\left(P^{3}r^{2}\left(\frac{P}{r}X^{2b}\right)^{2}\right)^{3/8}=P^{\frac{15}{8}}X^{\frac{3b}{2}}\leq X^{\frac{5}{6}}. |  |

Therefore we obtain, similarly to ( 11.29) for the analogous quantity S 230 ∗ S^{*}_{230}

(11.33) |  | S 230 ∗ ≪ η 0, b exp ( − ( 1 − 10 b) ℒ ( 1 − 7 ​ ε 1) ​ log ⁡ G ⁡ ( X 5 / 6) 5 ​ ℒ / 6) ≪ η 0, b G ( X 5 / 6) − 7 / 6. S^{*}_{230}\ll_{\eta_{0,b}}\exp\left(-(1-10b)\mathcal{L}\frac{(1-7\varepsilon_{1})\log G(X^{5/6})}{5\mathcal{L}/6}\right)\ll_{\eta_{0,b}}G(X^{5/6})^{-7/6}. |  |

Therefore we have by ( 11.9) also

(11.34) |  | | ∫ 𝔐 S 2 ​ ( α) ​ S 30 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α | < 𝔖 ⁡ ( m) ​ m 6 ​ G 1, \bigg|\int\limits_{\mathfrak{M}}S_{2}(\alpha)S_{30}(\alpha)e(-m\alpha)d\alpha\bigg|<{{\mathfrak{S}}(m)m\over 6G_{1}}, |  |

where S 30 S_{30} denotes the part of S 3 S_{3} corresponding to ϱ 0 = 1 \varrho_{0}=1.

In order to treat ∫ S 2 2 ​ ( α) \int S^{2}_{2}(\alpha) let us consider any fixed pair ( χ j, ϱ j) ​ mod ​ r j ∈ [R, R ​ X b] (\chi_{j},\varrho_{j})\,\text{\rm mod}\;r_{j}\in[R,RX^{b}] and consider the set 𝒮 ⁡ ( ϱ j, χ j) \mathcal{S}(\varrho_{j},\chi_{j}) of all pairs ( ϱ μ, χ μ) (\varrho_{\mu},\chi_{\mu}) χ μ ​ mod ​ r μ \chi_{\mu}\,\text{\rm mod}\;r_{\mu} in S 2 ​ j S_{2j} for which ( 11.19) and therefore ( 11.21), ( 11.22) and ( 11.24) hold (with ϱ = ϱ j \varrho=\varrho_{j}). By symmetry we can suppose δ μ ≥ δ j \delta_{\mu}\geq\delta_{j}.

The upper estimate for all possible Y = Y ⁡ ( ϱ ′) Y=Y(\varrho^{\prime}), ( ϱ ′, χ ′) ∈ 𝒮 ⁡ ( ϱ j, χ j) (\varrho^{\prime},\chi^{\prime})\in\mathcal{S}(\varrho_{j},\chi_{j}) will be now, again by ( 11.18), ( 11.22), ( 11.24), similarly to ( 11.28):

(11.35) |  | Y = ( r 1 2 ​ r μ ​ k ​ ( | γ μ | + 1) 2) 3 / 8 ≪ r 1 3 / 4 ​ k 3 / 8 ​ R 3 / 8 ​ ( P R) 3 / 4 ​ X 2 ​ b ≪ P 3 / 2 ​ k 3 / 8 ​ R − 3 8 ​ X 2 ​ b. Y=(r^{2}_{1}r_{\mu}k(|\gamma_{\mu}|+1)^{2})^{3/8}\ll r^{3/4}_{1}k^{3/8}R^{3/8}\left({P\over R}\right)^{3/4}X^{2b}\ll P^{3/2}k^{3/8}R^{-{3\over 8}}X^{2b}. |  |

If we would like to have an estimate, valid for all m ∈ [X / 2, X] m\in[X/2,X] we can estimate k k by P 2 P^{2} from above and obtain

(11.36) |  | Y ≪ P 9 / 4 ​ R − 3 8 ​ X 2 ​ b =: Z. Y\ll P^{9/4}R^{-{3\over 8}}X^{2b}=:Z. |  |

Further, due to δ μ ≥ δ j \delta_{\mu}\geq\delta_{j} we obtain, as in ( 11.26)–( 11.27)

(11.37) |  | X − 1 / 2 ∑ χ μ W 2 ′′ ( χ μ) ≪ ( P 3 4 + 2 ​ b 3 X − 1) δ j, X^{-1/2}\sum_{\chi_{\mu}}W^{\prime\prime}_{2}(\chi_{\mu})\ll\big(P^{{3\over 4}+2\sqrt[3]{b}}X^{-1}\big)^{\delta_{j}}, |  |

where the summation runs over all χ μ \chi_{\mu} for which there exists ϱ μ \varrho_{\mu} with ϱ μ \varrho_{\mu}, χ μ ∈ 𝒮 ⁡ ( ϱ j, χ j) \chi_{\mu}\in\mathcal{S}(\varrho_{j},\chi_{j}).

On the other hand, the contribution of all pairs ( χ j, ϱ j) (\chi_{j},\varrho_{j}) with χ j ​ mod ​ r j ∈ [R, R ​ X b] \chi_{j}\,\text{\rm mod}\;r_{j}\in[R,RX^{b}], | γ j | ≤ P r j ​ X b ≤ P R ​ X b |\gamma_{j}|\leq{P\over r_{j}}X^{b}\leq{P\over R}X^{b} to ∑ ∑ ⁡ W ⁡ ( χ j) \sum\sum W(\chi_{j}) is, multiplied by ( 11.37), similarly to ( 9.12)

(11.38) |  |  | ≪ ℒ ​ ∫ φ 0 ​ ( Z) b ( R c 1 ​ ( b) − c 2 ​ ( b) ​ P c 2 ​ ( b) ​ X − 1 + 6 ​ b ​ P 3 4 + 2 ​ b 3 ​ X − 1) δ ​ 𝑑 δ \displaystyle\ll\mathcal{L}\int\limits^{b}_{\varphi_{0}(Z)}\big(R^{c_{1}(b)-c_{2}(b)}P^{c_{2}(b)}X^{-1+6b}P^{{3\over 4}+2\sqrt[3]{b}}X^{-1}\big)^{\delta}d\delta |  |

 |  | ≪ η, b ( R 3 / 4 P 9 / 4 + 3 ​ b 3 X − 2) φ ⁡ ( Z). \displaystyle\ll_{\eta,b}\big(R^{3/4}P^{9/4+3\sqrt[3]{b}}X^{-2}\big)^{\varphi(Z)}. |  |

Let u = log ⁡ R / ℒ ( ≤ ϑ − η 0) u=\log R/\mathcal{L}(\leq\vartheta-\eta_{0}). Then the above estimate is by ( 11.8) and ( 11.36)

(11.39) |  | ≤ c ⁡ ( η 0, b) ​ exp ⁡ ( − ( 2 − ( 9 / 4) ​ ϑ − ( 3 / 4) ​ u ( 9 / 4) ​ ϑ − ( 3 / 8) ​ u − η 0) ​ log ⁡ G) ≤ c ⁡ ( η 0, b) ​ G − 1 − η 0 \leq c(\eta_{0},b)\exp\left(-\left({2-(9/4)\vartheta-(3/4)u\over(9/4)\vartheta-(3/8)u}-\eta_{0}\right)\log G\right)\leq c(\eta_{0},b)G^{-1-\eta_{0}} |  |

if now, exceptionally P ≤ X ϑ − η P\leq X^{\vartheta-\eta} with ϑ = 16 / 39 < 4 / 9 \vartheta=16/39<4/9, and b b is small enough in dependence on η \eta.

In this way we get analogously to ( 11.30)–( 11.34)

(11.40) |  | | ∫ 𝔐 S 2 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α | < 𝔖 ⁡ ( m) ​ m 2 ​ G 1. \bigg|\int\limits_{\mathfrak{M}}S^{2}_{2}(\alpha)e(-m\alpha)d\alpha\bigg|<{{\mathfrak{S}}(m)m\over 2G_{1}}. |  |

In order to reach ϑ = 4 9 \vartheta={4\over 9}, we need a further idea. First we can remark that according to the Main Lemma 1 we have

(11.41) |  | | 𝔖 ⁡ ( χ 1, χ 1, m) | ≤ ( 3 / 2) ​ 𝔖 ​ ( m), if ​ r 1 ∤ 36 ​ m. |{\mathfrak{S}}(\chi_{1},\chi_{1},m)|\leq(\sqrt{3}/2){\mathfrak{S}}(m),\quad\text{if }r_{1}\nmid 36m. |  |

In this case the effect of the Siegel zero cannot destroy the main term. Therefore in this case, according to Sections 8 – 10

(11.42) |  | ∫ 𝔐 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α \displaystyle\int\limits_{\mathfrak{M}}S^{2}(\alpha)e(-m\alpha)d\alpha | = ∫ 𝔐 S 3 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α + O ⁡ ( e − c ​ H ⋅ X) \displaystyle=\int\limits_{\mathfrak{M}}S^{2}_{3}(\alpha)e(-m\alpha)d\alpha+O(e^{-cH}\cdot X) |  |

 |  | ≥ 1 8 ​ m ​ 𝔖 ​ ( m) + O ⁡ ( e − c ​ H ​ X) > 1 9 ​ m ​ 𝔖 ​ ( m), \displaystyle\geq{1\over 8}m{\mathfrak{S}}(m)+O(e^{-cH}X)>{1\over 9}m{\mathfrak{S}}(m), |  |

and we are ready without any further analysis. So we can suppose further on that r 1 | 36 ​ m r_{1}\mid 36m. In the argumentation ( 11.35)–( 11.40) we are allowed to suppose ( 11.21), consequently,

(11.43) |  | g μ ​ ( m) = r μ ( r μ, m) ≪ X 3 ​ b. g_{\mu}(m)={r_{\mu}\over(r_{\mu},m)}\ll X^{3b}. |  |

Now we can distinguish two cases.

### Case A. [r 1, r μ] ≤ P [r_{1},r_{\mu}]\leq P.

In this case we have k = cond ​ χ 1 ​ χ μ ≤ P k=\mathrm{cond}\,\chi_{1}\chi_{\mu}\leq P, and from ( 11.35) we have now

(11.44) |  | Y ≪ P 15 / 8 R − 3 / 8 X 4 ​ b =: Z. Y\ll P^{15/8}R^{-3/8}X^{4b}=:Z. |  |

We have this in place of ( 11.36). ( 11.37) and ( 11.38) remain true, whereas we have now instead of ( 11.39) the final estimate

(11.45) |  | c ⁡ ( η, b) ​ exp ⁡ { − ( 2 − ( 9 / 4) ​ ϑ − ( 3 / 4) ​ u ( 15 / 8) ​ ϑ − ( 3 / 8) ​ u − η) ​ log ⁡ G } ≤ c ⁡ ( η, b) ​ G − 1 − η c(\eta,b)\exp\left\{-\left({2-(9/4)\vartheta-(3/4)u\over(15/8)\vartheta-(3/8)u}-\eta\right)\log G\right\}\leq c(\eta,b)G^{-1-\eta} |  |

if u ≤ ϑ = 4 / 9 − η u\leq\vartheta=4/9-\eta, that is R ≤ P = X 4 / 9 − η R\leq P=X^{4/9-\eta}.

### Case B. [r 1, r μ] > P [r_{1},r_{\mu}]>P.

Let us denote by d μ ​ k d_{\mu k} the divisors of r μ r_{\mu} with d μ ​ k ≤ X 3 ​ b d_{\mu k}\leq X^{3b}. If we consider any fixed pair r μ, d μ ​ k r_{\mu},d_{\mu k} then let us consider the set

(11.46) |  | M ( r μ, d μ ​ k) = { 36 m; X / 2 ≤ m ≤ X; r 1 ∣ 36 m, r μ ( r μ, m) = d μ ​ k }. M(r_{\mu},d_{\mu k})=\left\{36m;\ X/2\leq m\leq X;\ r_{1}\mid 36m,\ {r_{\mu}\over(r_{\mu},m)}=d_{\mu k}\right\}. |  |

Since r 1 | 36 ​ m r_{1}\mid 36m, r μ d μ ​ k | m | 36 ​ m {r_{\mu}\over d_{\mu k}}|m|36m, all elements of M ⁡ ( r μ, d μ ​ k) M(r_{\mu},d_{\mu k}) are multiples of

(11.47) |  | [r 1, r μ d μ ​ k] > P d μ ​ k ≥ P ​ X − 3 ​ b, \left[r_{1},{r_{\mu}\over d_{\mu k}}\right]>{P\over d_{\mu k}}\geq PX^{-3b}, |  |

so

(11.48) |  | | M ⁡ ( r μ, d μ ​ k) | ≪ X 1 + 3 ​ b P. |M(r_{\mu},d_{\mu k})|\ll{X^{1+3b}\over P}. |  |

The number of all moduli is by ( 11.14) ≪ X 3 ​ b \ll X^{3b}, so the number of all pairs r μ r_{\mu}, d μ ​ k d_{\mu k} is clearly ≪ X 6 ​ b \ll X^{6b}.

Thus, throwing away all m m ’s with

(11.49) |  | ℳ = { m; 36 ​ m ∈ ⋃ r μ, d μ ​ k M ⁡ ( r μ, d μ ​ k) } \mathcal{M}=\left\{m;\ 36m\in\bigcup_{r_{\mu},d_{\mu k}}M(r_{\mu},d_{\mu k})\right\} |  |

the cardinality of the arising new exceptional set will be

(11.50) |  | | ℳ | ≤ X 1 + 9 ​ b P. |\mathcal{M}|\leq{X^{1+9b}\over P}. |  |

For all m ∈ [X / 2, X] ∖ ℳ m\in[X/2,X]\setminus\mathcal{M} we have Case A and therefore we obtain, by ( 11.45), similarly to ( 11.40) (with ϑ = 4 / 9 \vartheta=4/9)

(11.51) |  | | ∫ 𝔐 S 2 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α | < 𝔖 ⁡ ( m) ​ m 2 ​ G 1. \bigg|\int\limits_{\mathfrak{M}}S^{2}_{2}(\alpha)e(-m\alpha)d\alpha\bigg|<{{\mathfrak{S}}(m)m\over 2G_{1}}. |  |

This, together with ( 11.30) and ( 11.34), really shows ( 11.12). So by ( 11.11) we have

(11.52) |  | ∫ 𝔐 S 0 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α ≥ 1.05 ​ 𝔖 ​ ( m) ​ m G 1. \int\limits_{\mathfrak{M}}S^{2}_{0}(\alpha)e(-m\alpha)d\alpha\geq{1.05{\mathfrak{S}}(m)m\over G_{1}}. |  |

Hence, inequalities ( 11.52) and ( 8.28) prove in case of the existence of a Siegel zero

(11.53) |  | R 1 ​ ( m) ≥ 1.05 ​ 𝔖 ​ ( m) ​ m G 1 + O ⁡ ( ℒ 8 ​ X 1 − b / 82) > 𝔖 ⁡ ( m) ​ m ​ δ 1 ​ ℒ, R_{1}(m)\geq{1.05{\mathfrak{S}}(m)m\over G_{1}}+O(\mathcal{L}^{8}X^{1-b/82})>{\mathfrak{S}}(m)m\delta_{1}\mathcal{L}, |  |

in view of Siegel’s theorem ( 11.6) and ( 11.9), for all values of m ∈ [X / 2, X] \ ℳ m\!\in\![X/2,X]\backslash\mathcal{M}, where the exceptional set ℳ \mathcal{M} satisfies ( 11.50). The constant b b can be chosen arbitrarily small here. Thus ( 11.53) proves our Theorem 2.

## 12 Conclusion

In what follows we will investigate the sum

(12.1) |  | I ′ ​ ( ϱ 1, ϱ 2, m) = ∑ X 2 < k ≤ X − m k ϱ 1 − 1 ​ ( k + m) ϱ ¯ 2 − 1, ( X 2 = X / 4) I^{\prime}(\varrho_{1},\varrho_{2},m)=\sum_{X_{2}<k\leq X-m}k^{\varrho_{1}-1}(k+m)^{\overline{\varrho}_{2}-1},\quad(X_{2}=X/4) |  |

or, more precisely, first

(12.2) |  | J ⁡ ( γ 1, γ 2, m, u) = ∑ X 2 < k ≤ u e ⁡ ( f ⁡ ( k) 2 ​ π) ( u ≤ X − m) J(\gamma_{1},\gamma_{2},m,u)=\sum_{X_{2}<k\leq u}e\left(\frac{f(k)}{2\pi}\right)\qquad(u\leq X-m) |  |

where

(12.3) |  | f ⁡ ( y) = γ 1 ​ log ⁡ y − γ 2 ​ log ⁡ ( y + m), m ∈ [X / 4, X / 2], X / 4 ≤ y ≤ X − m. f(y)=\gamma_{1}\log y-\gamma_{2}\log(y+m),\quad m\in[X/4,X/2],\ X/4\leq y\leq X-m. |  |

By symmetry we can clearly suppose γ 1 ≥ 0 \gamma_{1}\geq 0. Let

(12.4) |  | M = max ⁡ ( | γ 1 |, | γ 2 |) > C, M=\max(|\gamma_{1}|,|\gamma_{2}|)>C, |  |

a suitably chosen large constant. With the aim to apply Lemma 4.4 we calculate f ′ ​ ( y) f^{\prime}(y):

(12.5) |  | f ′ ​ ( y) = γ 1 y − γ 2 y + m = γ 1 ​ m − ( γ 2 − γ 1) ​ y y ⁡ ( y + m). f^{\prime}(y)={\gamma_{1}\over y}-{\gamma_{2}\over y+m}={\gamma_{1}m-(\gamma_{2}-\gamma_{1})y\over y(y+m)}. |  |

We have

(12.6) |  | f ′ ​ ( y) \displaystyle f^{\prime}(y) | ≥ γ 1 + | γ 2 | X ≥ M X \displaystyle\geq{\gamma_{1}+|\gamma_{2}|\over X}\geq{M\over X} |  | if ​ γ 2 ≤ 0, \displaystyle\text{if }\gamma_{2}\leq 0, |  |

 | f ′ ​ ( y) \displaystyle f^{\prime}(y) | ≥ γ 1 4 ​ X = M 4 ​ X \displaystyle\geq{\gamma_{1}\over 4X}={M\over 4X} |  | if ​ 0 ≤ γ 2 ≤ γ 1, \displaystyle\text{if }0\leq\gamma_{2}\leq\gamma_{1}, |  |

 | f ′ ​ ( y) \displaystyle f^{\prime}(y) | ≥ 4 ​ γ 1 3 ​ ( y + m) − 7 ​ γ 1 6 ​ ( y + m) ≥ γ 2 7 ​ X = M 7 ​ X \displaystyle\geq{4\gamma_{1}\over 3(y+m)}-{7\gamma_{1}\over 6(y+m)}\geq{\gamma_{2}\over 7X}={M\over 7X}\quad |  | if ​ γ 1 ≤ γ 2 ≤ ( 7 / 6) ​ γ 1. \displaystyle\text{if }\gamma_{1}\leq\gamma_{2}\leq(7/6)\gamma_{1}. |  |

Thus, let us suppose γ 2 > ( 7 / 6) ​ γ 1 \gamma_{2}>(7/6)\gamma_{1}, γ 2 = M > C \gamma_{2}=M>C further on. In this case we have

(12.7) |  | f ′ ​ ( y) ​ > = < ​ 0 if y ​ < = > ​ m ​ γ 1 γ 2 − γ 1. f^{\prime}(y)\,\begin{aligned} >\\[-9.95845pt] =\\[-9.95845pt] <\end{aligned}\,0\quad\text{ if }\quad y\,\begin{aligned} <\\[-9.95845pt] =\\[-9.95845pt] >\end{aligned}\,{m\gamma_{1}\over\gamma_{2}-\gamma_{1}}. |  |

Let D = M = γ 2 D=\sqrt{M}=\sqrt{\gamma_{2}}. Now

(12.8) |  | f ′ ​ ( y) > D ​ X y ⁡ ( y + m) > D X if ​ y < m ​ γ 1 − D ​ X γ 2 − γ 1 f^{\prime}(y)>{DX\over y(y+m)}>{D\over X}\quad\text{if }y<{m\gamma_{1}-DX\over\gamma_{2}-\gamma_{1}} |  |

and

(12.9) |  | f ′ ​ ( y) < − D ​ X y ⁡ ( y + m) < − D X if ​ y > m ​ γ 1 + D ​ X γ 2 − γ 1. f^{\prime}(y)<-{DX\over y(y+m)}<-{D\over X}\quad\text{if }y>{m\gamma_{1}+DX\over\gamma_{2}-\gamma_{1}}. |  |

So we can apply Lemma 4.4 if

(12.10) |  | y ∉ [m ​ γ 1 γ 2 − γ 1 − D ​ X γ 2 − γ 1, m ​ γ 1 γ 2 − γ 1 + D ​ X γ 2 − γ 1] = I 0. y\notin\left[{m\gamma_{1}\over\gamma_{2}-\gamma_{1}}-{DX\over\gamma_{2}-\gamma_{1}},{m\gamma_{1}\over\gamma_{2}-\gamma_{1}}+{DX\over\gamma_{2}-\gamma_{1}}\right]=I_{0}. |  |

Estimating the sum in ( 12.2) trivially if k ∈ I 0 k\in I_{0}, and otherwise by Lemma 4.4, we obtain by γ 2 − γ 1 > M / 7 \gamma_{2}-\gamma_{1}>M/7

(12.11) |  | J ⁡ ( γ 1, γ 2, m, u) ≪ X D + D ​ X M ≪ X M. J(\gamma_{1},\gamma_{2},m,u)\ll{X\over D}+{DX\over M}\ll{X\over\sqrt{M}}. |  |

Finally, by partial summation, ( 12.11) implies

(12.12) |  | I ′ ​ ( ϱ 1, ϱ 2, m) ≪ X 1 − δ 1 − δ 2 max ⁡ ( | γ 1 |, | γ 2 |). I^{\prime}(\varrho_{1},\varrho_{2},m)\ll{X^{1-\delta_{1}-\delta_{2}}\over\sqrt{\max(|\gamma_{1}|,|\gamma_{2}|)}}. |  |

The above estimate holds trivially if ( 12.4) is false. Thus we obtain an estimate, similar to ( 10.25), in case of the Generalized Twin Prime Problem, too. Theorem 1 is therefore completed by the above arguments and by the results of Sections 8 – 10, more precisely by ( 8.28), ( 9.16) and ( 10.27).

## References

- [2] Jing Run Chen, Jian Min Liu, The exceptional set of Goldbach numbers III, Chinese Quart. J. Math. 4 (1989), 1–15.
- [3] N. G. Cudakov, On the density of the set of even numbers which are not representable as a sum of two primes, Izv. Akad. Nauk SSSR 2 (1938), 25–40.
- [4] H. Davenport, Multiplicative number theory, 2nd edition. Revised by Hugh L. Montgomery, Graduate Texts in Mathematics, 74, Springer-Verlag, New York–Berlin, 1980. xiii+177 pp.
- [5] R. Descartes, Oeuvres, Publié par Ch. Adam and P. Tannery, Paris, 1908.
- [6] T. Estermann, On Goldbach’s problem: Proof that almost all even positive integers are sums of two primes, Proc. London Math. Soc. (2) 44 (1938), 307–314.
- [7] P. X. Gallagher, The large sieve, Mathematika 14 (1967), 14-–20.
- [8] G. H. Hardy, J. E. Littlewood, Some problems of ‘Partitito Numerorum’, V: A further contribution to the study of Goldbach’s problem, Proc. London Math. Soc. (2) 22 (1924), 46–56.
- [9] D. R. Heath-Brown, The density of zeros of Dirichlet’s L L -functions, Canad. J. Math. 31 (1979), no. 2, 231–-240.
- [10] D. R. Heath-Brown, J.-C. Puchta, Integers represented as a sum of primes and powers of two, Asian J. Math. 6 (2002), no. 3, 535–565.
- [11] M. Jutila, On Linnik’s constant, Math. Scand. 41 (1975), 45–62.
- [12] Anatolij A. Karatsuba, Basic analytic number theory. Translated from the second (1983) Russian edition and with a preface by Melvyn B. Nathanson, Springer-Verlag, Berlin, 1993. xiv+222 pp.
- [13] Hongze Li, The exceptional set of Goldbach numbers I, Quart J. Math. Oxford Ser. (2) 50 (2000), no. 200, 471–482.
- [14] Hongze Li, The exceptional set of Goldbach numbers II, Acta Arith. 92 (2000), no. 1, 71–88.
- [15] Wen Chao Lu, Exceptional set of Goldbach number, J. Number Theory 130 (2010), no. 10, 2359-–2392.
- [16] H. Mikawa, On the exceptional set in Goldbach’s problem, Tsukuba J. Math. 16 (1992), 513–543.
- [17] H. L. Montgomery, Topics in multiplicative number theory, Lecture Notes in Mathematics, Vol. 227. Springer-Verlag, Berlin–New York, 1971. ix+178 pp.
- [18] H. L. Montgomery, R. C. Vaughan, The exceptional set in Goldbach’s problem. Collection of articles in memory of Juriĭ Vladimirovič Linnik, Acta Arith. 27 (1975), 353-–370.
- [19] J. Pintz, Some new density theorems for Dirichlet L-functions, submitted.
- [20] J. Pintz, Elementary methods in the theory of L L -functions II. On the greatest real zero of a real L L -function, Acta Arith. 31 (1976), no. 1, 273–289.
- [21] K. Prachar, Primzahlverteilung (German), Springer-Verlag, Berlin–Göttingen–Heidelberg, 1957. x+415 pp.
- [22] B. Saffari, R. C. Vaughan, On the fractional parts of x / n x/n and related sequences. II, Ann. Inst. Fourier (Grenoble) 27 (1977), no. 2, 1-–30.
- [23] E. C. Titchmarsh, The theory of the Riemann zeta function, Clarendon press, Oxford, 1951.
- [24] J. G. van der Corput, Sur l’hypothése de Goldbach pour Presque tous les nombres pairs, Acta Arith. 2 (1937), 266–290.
- [25] R. C. Vaughan, On Goldbach’s problem, Acta Arith. 22 (1972), 21-–48.
- [26] I. M. Vinogradov, Representation of an odd number as a sum of three prime numbers, Doklady Akad. Nauk SSSR 15 (1937), 291–294 (Russian).

János Pintz
Rényi Mathematical Institute
of the Hungarian Academy of Sciences
Budapest, Reáltanoda u. 13–15
H-1053 Hungary
e-mail: pintz.janos@renyi.mta.hu


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
