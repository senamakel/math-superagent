<!-- source: https://arxiv.org/html/1712.00737v1 | converted from HTML -->

Explicit formulae for averages of Goldbach representations

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1712.00737v1 [math.NT] 03 Dec 2017

# Explicit formulae for averages
of Goldbach representations

J.Brüdern, J.Kaczorowski and A.Perelli

Abstract. We prove an explicit formula, analogous to the classical explicit formula for ψ ⁡ ( x) \psi(x), for the Cesàro-Riesz mean of any order k > 0 k>0 of the number of representations of n n as a sum of two primes. Our approach is based on a double Mellin transform and the analytic continuation of certain functions arising therein.

Mathematics Subject Classification (2000): 11P32, 11N05

Keywords: Goldbach problem, explicit formulae

## 1. Introduction

Riemann’s explicit formula reveals an intimate relation between the distribution of primes and the zeros of the Riemann zeta function. A similar formula for the number of prime points in a triangle such as

 | ♯ { ( p, p ′): p + p ′ ≤ N, p and p ′ prime } \sharp\{(p,p^{\prime}):p+p^{\prime}\leq N,\ \text{$p$ and $p^{\prime}$ prime}\} |  | (1.1) |

may be expected, and Fujii [3] was first to step in this direction. In recent years, there has been a flurry of papers on the topic, also analyzing weighted versions of the count ( 1.1); see Bhowmik & Schlage-Puchta [1], Languasco & Zaccagnini [6], [7], Goldston & Yang [4] and Languasco’s survey [5]. So far, all authors have interpreted the quantity in ( 1.1) as the mean of the number of representations of a given number n ≤ N n\leq N as the sum of two primes, and replaced the latter by the analytically simpler expression

 | R ⁡ ( n) = ∑ m + m ′ = n Λ ⁡ ( m) ​ Λ ​ ( m ′), R(n)=\sum_{m+m^{\prime}=n}\Lambda(m)\Lambda(m^{\prime}), |  |

with Λ \Lambda the von Mangoldt function. One is then led to study the sum

 | G 0 ​ ( N) = ∑ ′ n ≤ N ′ ​ R ​ ( n), G_{0}(N)=\sideset{}{{}^{\prime}}{\sum}_{n\leq N}R(n), |  | (1.2) |

where the notation indicates that R ⁡ ( N) / 2 R(N)/2 is to be subtracted from the sum in ( 1.2) should N N be a natural number.

A purely formal application of the method to be described herein suggests that, perhaps, one has

 | G 0 ​ ( N) = lim T → ∞ ∑ | σ | ≤ T, | t | ≤ T | u | ≤ T, | v | ≤ T res 𝑠 ​ res 𝑤 ​ ζ ′ ζ ​ ( s) ​ ζ ′ ζ ​ ( w) ​ N s + w ​ Γ ⁡ ( s) ​ Γ ​ ( w) Γ ⁡ ( w + s + 1). G_{0}(N)=\lim_{T\to\infty}\sum_{\begin{subarray}{c}|\sigma|\leq T,|t|\leq T\\ |u|\leq T,|v|\leq T\end{subarray}}\underset{s}{\res}\,\underset{w}{\res}\,\frac{\zeta^{\prime}}{\zeta}(s)\frac{\zeta^{\prime}}{\zeta}(w)N^{s+w}\frac{\Gamma(s)\Gamma(w)}{\Gamma(w+s+1)}. |  | (1.3) |

Here and later, we write s = σ + i ​ t s=\sigma+it, w = u + i ​ v w=u+iv, with real numbers σ, t, u, v \sigma,t,u,v. If true, then ( 1.3) would correspond to Riemann’s formula, in the form

 | ∑ ′ n ≤ N ′ Λ ( n) = − lim T → ∞ ∑ | σ | ≤ T, | t | ≤ T res 𝑠 ζ ′ ζ ( s) N s s \sideset{}{{}^{\prime}}{\sum}_{n\leq N}\Lambda(n)=-\lim_{T\to\infty}\sum_{|\sigma|\leq T,|t|\leq T}\underset{s}{\res}\,\frac{\zeta^{\prime}}{\zeta}(s)\frac{N^{s}}{s} |  |

(see Chapter 17 of Davenport [2]), in a two-dimensional context.

Our purpose is to present an approach that yields weighted versions of ( 1.3) superior to all previous work. In much recent work, G 0 ​ ( N) G_{0}(N) was examined by means of the circle method, but this procedure apparently puts limitations to the insights obtainable on the problem. Our method is radically different; indeed, we consider the counting problem in its natural framework, as a two-dimensional lattice point count with constraints on the coordinates. The range of summation m + m ′ ≤ N m+m^{\prime}\leq N constitutes a triangle, and the Mellin transform of its indicator function is the analytic function in s s and w w that occurs on the right hand side of ( 1.3). In this way, our hypothetical formula ( 1.3) arises canonically, and any attempt to establish it may well lead to approximations to the conjecture in full.

In a weighted setting, the ideas described above take us well beyond the current state of affairs. We follow Languasco & Zaccagnini [7] and consider the Cesàro-Riesz mean of R ⁡ ( n) R(n) of order k > 0 k>0, defined for N ≥ 2 N\geq 2 by

 | G k ​ ( N) = 1 Γ ⁡ ( k + 1) ​ ∑ n < N R ⁡ ( n) ​ ( 1 − n N) k. G_{k}(N)=\frac{1}{\Gamma(k+1)}\sum_{n<N}R(n)\left(1-\frac{n}{N}\right)^{k}. |  | (1.4) |

They show ( [7, Theorem 1], corrected in [5]) that whenever k > 1 k>1 one has

 | G k ​ ( N) = N 2 Γ ⁡ ( k + 3) − 2 ​ A k ​ ( N) + B k ​ ( N) + O ⁡ ( N), G_{k}(N)=\frac{N^{2}}{\Gamma(k+3)}-2A_{k}(N)+B_{k}(N)+O(N), |  | (1.5) |

in which

 | A k ​ ( N) = ∑ ρ Γ ⁡ ( ρ) Γ ⁡ ( ρ + k + 2) ​ N ρ + 1 and B k ​ ( N) = ∑ ρ ∑ ρ ′ Γ ⁡ ( ρ) ​ Γ ​ ( ρ ′) Γ ⁡ ( ρ + ρ ′ + k + 1) ​ N ρ + ρ ′ A_{k}(N)=\sum_{\rho}\frac{\Gamma(\rho)}{\Gamma(\rho+k+2)}N^{\rho+1}\quad\text{and}\quad B_{k}(N)=\sum_{\rho}\sum_{\rho^{\prime}}\frac{\Gamma(\rho)\Gamma(\rho^{\prime})}{\Gamma(\rho+\rho^{\prime}+k+1)}N^{\rho+\rho^{\prime}} |  | (1.6) |

with the sums running over the non-trivial zeros of ζ ⁡ ( s) \zeta(s), each zero listed according to its multiplicity. We apply this notation throughout the paper. Note that the sums in ( 1.6) are absolutely convergent for k > 1 / 2 k>1/2. Furthermore, observe that ( 1.5) is compatible with a weighted version of ( 1.3) in which only the singularities with σ > 0 \sigma>0 and u > 0 u>0 are made explicit. We are able to handle the wider range k > 0 k>0 while taking into account all the singularities, hence providing a full explicit formula for G k ​ ( N) G_{k}(N). This improves on Languasco & Zaccagnini [7] in several directions, and a recent result by Goldston & Yang [4] for k = 1 k=1, obtained under the Riemann Hypothesis, is also superseded unconditionally.

To initiate our treatment, let N ≥ 4 N\geq 4 be an integer, let k > 0 k>0 be real, and then observe that

 | 1 − m + n N = ( 1 − n N − m) ​ ( 1 − m N) 1-\frac{m+n}{N}=\Big(1-\frac{n}{N-m}\Big)\Big(1-\frac{m}{N}\Big) |  |

to recast ( 1.4) as

 | G k ​ ( N) = 1 Γ ⁡ ( k + 1) ​ ∑ m < N Λ ⁡ ( m) ​ ( 1 − m N) k ​ ∑ n < N − m Λ ⁡ ( n) ​ ( 1 − n N − m) k. G_{k}(N)=\frac{1}{\Gamma(k+1)}\sum_{m<N}\Lambda(m)\left(1-\frac{m}{N}\right)^{k}\sum_{n<N-m}\Lambda(n)\left(1-\frac{n}{N-m}\right)^{k}. |  | (1.7) |

We now recall that whenever x x and c c are positive numbers, and z z is a complex number with with ℜ ⁡ z > 0 \Re z>0, then

 | 1 2 ​ π ​ i ​ ∫ ( c) Γ ⁡ ( s) ​ x − s Γ ⁡ ( s + z + 1) ​ s ⋅ = { ( 1 − x) z / Γ ⁡ ( z + 1) if ​ 0 < x < 1, 0 if ​ x ≥ 1 \frac{1}{2\pi i}\int_{(c)}\frac{\Gamma(s)x^{-s}}{\Gamma(s+z+1)}\,\d{s}=\begin{cases}(1-x)^{z}/\Gamma(z+1)&\text{if}\ 0<x<1,\\ 0&\text{if}\ x\geq 1\end{cases} |  | (1.8) |

(for example, this is formula 5.35 of Section 2.5 on p.195 of Oberhettinger [8], with the choice α = 0 \alpha=0 and β = z + 1 \beta=z+1). We apply ( 1.8) twice, first with z = k z=k to the inner sum in ( 1.7) and then with z = s + k z=s+k to the outer sum. This leads us to

 | G k ​ ( N) = 1 ( 2 ​ π ​ i) 2 ​ ∫ ( 2) ∫ ( 2) ζ ′ ζ ​ ( w) ​ ζ ′ ζ ​ ( s) ​ Γ ⁡ ( w) ​ Γ ​ ( s) Γ ⁡ ( s + w + k + 1) ​ N w + s ​ s ⋅ ​ w ⋅. G_{k}(N)=\frac{1}{(2\pi i)^{2}}\int_{(2)}\int_{(2)}\frac{\zeta^{\prime}}{\zeta}(w)\frac{\zeta^{\prime}}{\zeta}(s)\frac{\Gamma(w)\Gamma(s)}{\Gamma(s+w+k+1)}N^{w+s}\,\d{s}\,\d{w}. |  | (1.9) |

To proceed further, we shift the inner integration from the line ℜ ⁡ s = 2 \Re s=2 to ℜ s = − 1 / 2 \Re s={-}1/2. We shall then encounter the functions

 | T N ( w) = − 1 2 ​ π ​ i ∫ ( − 1 / 2) ζ ′ ζ ( s) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ T_{N}(w)=\frac{{-}1}{2\pi i}\int_{(-1/2)}\frac{\zeta^{\prime}}{\zeta}(s)\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s} |  | (1.10) |

and

 | Z N ​ ( w) = ∑ ρ Γ ⁡ ( ρ) Γ ⁡ ( ρ + w + 1) ​ N ρ. Z_{N}(w)=\sum_{\rho}\frac{\Gamma(\rho)}{\Gamma(\rho+w+1)}N^{\rho}. |  | (1.11) |

By Stirling’s formula, the integral in ( 1.10) and the sum in ( 1.11) are absolutely and compactly convergent in u > 0 u>0, hence T N ​ ( w) T_{N}(w) and Z N ​ ( w) Z_{N}(w) are holomorphic in this half-plane. It is fundamental to this paper to realize that the functions T N ​ ( w) T_{N}(w) and Z N ​ ( w) Z_{N}(w) both extend to entire functions that do not grow too fast. We establish this in Section 2. Equipped with this, it will be possible to shift the integration over ℜ ⁡ w = 2 \Re w=2 to ℜ ⁡ w = − M \Re w=-M, say, and to analyse the limit for M → ∞ M\to\infty. We then arrive at the desired explicit formula for G k ​ ( N) G_{k}(N). The final result features the sums

 | Σ Γ ( N, k) = − ∑ ν = 1 ∞ res w = − ν ζ ′ ζ ( w) Γ ( w) N w Γ ⁡ ( w + k + 1), \Sigma_{\Gamma}(N,k)=-\sum_{\nu=1}^{\infty}\underset{w=-\nu}{\res}\,\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w)\frac{N^{w}}{\Gamma(w+k+1)}, |  | (1.12) |

 | Σ Z ( N, k) = − ∑ ν = 1 ∞ res w = − ν ζ ′ ζ ( w) Γ ( w) Z N ( w + k) N w, \Sigma_{Z}(N,k)=-\sum_{\nu=1}^{\infty}\underset{w=-\nu}{\res}\,\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w)Z_{N}(w+k)N^{w}, |  | (1.13) |

 | Σ T ( N, k) = − ∑ ν = 1 ∞ res w = − ν ζ ′ ζ ( w) Γ ( w) T N ( w + k) N w. \Sigma_{T}(N,k)=-\sum_{\nu=1}^{\infty}\underset{w=-\nu}{\res}\,\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w)T_{N}(w+k)N^{w}. |  | (1.14) |

Theorem. Let N ≥ 4 N\geq 4 be an integer and k > 0 k>0. Then

 | G k ​ ( N) = N 2 Γ ⁡ ( k + 3) − 2 ​ N ​ Z N ​ ( k + 1) + ∑ ρ Γ ⁡ ( ρ) ​ Z N ​ ( ρ + k) ​ N ρ − 2 ​ ζ ′ ζ ​ ( 0) ​ N Γ ⁡ ( k + 2) + 2 ​ ζ ′ ζ ​ ( 0) ​ Z N ​ ( k) + N ​ T N ​ ( k + 1) + ζ ′ ζ ​ ( 0) 2 ​ 1 Γ ⁡ ( k + 1) − ∑ ρ Γ ⁡ ( ρ) ​ T N ​ ( ρ + k) ​ N ρ − ζ ′ ζ ​ ( 0) ​ T N ​ ( k) + N ​ Σ Γ ​ ( N, k + 1) − Σ Z ​ ( N, k) − ζ ′ ζ ​ ( 0) ​ Σ Γ ​ ( N, k) + Σ T ​ ( N, k), \begin{split}G_{k}(N)&=\frac{N^{2}}{\Gamma(k+3)}-2NZ_{N}(k+1)+\sum_{\rho}\Gamma(\rho)Z_{N}(\rho+k)N^{\rho}-2\frac{\zeta^{\prime}}{\zeta}(0)\frac{N}{\Gamma(k+2)}\\ &\hskip-19.91684pt+2\frac{\zeta^{\prime}}{\zeta}(0)Z_{N}(k)+NT_{N}(k+1)+\frac{\zeta^{\prime}}{\zeta}(0)^{2}\frac{1}{\Gamma(k+1)}-\sum_{\rho}\Gamma(\rho)T_{N}(\rho+k)N^{\rho}-\frac{\zeta^{\prime}}{\zeta}(0)T_{N}(k)\\ &+N\Sigma_{\Gamma}(N,k+1)-\Sigma_{Z}(N,k)-\frac{\zeta^{\prime}}{\zeta}(0)\Sigma_{\Gamma}(N,k)+\Sigma_{T}(N,k),\end{split} |  |

where the sums ( 1.12), ( 1.13), ( 1.14) and the sums over the non-trivial zeros of ζ ⁡ ( s) \zeta(s) are absolutely convergent.

Some remarks are in order. First note that

 | N ​ Z N ​ ( k + 1) = A k ​ ( N) ​ for ​ k > 0 and ∑ ρ Γ ⁡ ( ρ) ​ Z N ​ ( ρ + k) ​ N ρ = B k ​ ( N) ​ for ​ k > 1 / 2, NZ_{N}(k+1)=A_{k}(N)\ \text{for}\ k>0\quad\text{and}\quad\sum_{\rho}\Gamma(\rho)Z_{N}(\rho+k)N^{\rho}=B_{k}(N)\ \text{for}\ k>1/2, |  |

so that the first three terms in our explicit formula correspond to the explicit terms in ( 1.5). The other terms are listed, roughly, in descending order according to their expected order of magnitude in N N. Moreover, the first nine terms in the explicit formula correspond to the contribution of the poles of − Γ ( s) ζ ′ ( s) / ζ ( s) -\Gamma(s)\zeta^{\prime}(s)/\zeta(s) in σ ≥ 0 \sigma\geq 0, see ( 3.4)–( 3.6) below. The explicit form of the sums in ( 1.12), ( 1.13) and ( 1.14), corresponding to the contribution of the remaining poles, can be found in ( 3.14), ( 3.15) and ( 3.16) below. We also remark that the series expansions for Σ Γ ​ ( N, k) \Sigma_{\Gamma}(N,k) and Σ T ​ ( N, k) \Sigma_{T}(N,k) in ( 3.14) and ( 3.16) are actually asymptotic expansions. Indeed, ( 3.17) below shows that cutting these series at ν = M ≥ 2 \nu=M\geq 2 produces an error of size, roughly, O ⁡ ( N − ( M + 1)) O(N^{-(M+1)}). This does not hold for the sum Σ Z ​ ( N, k) \Sigma_{Z}(N,k), in which case we can only prove that the tail is of order O ⁡ ( N − k + ϵ) O(N^{-k+\epsilon}) for every ϵ > 0 \epsilon>0; see again ( 3.17).

Thus far, we have concentrated on a full explicit formula, but it is worth pointing out that truncated versions are also available, not necessarily obtained by cutting the formula in our theorem. It may be instructive to compare the potential of our approach with that used by Languasco and Zaccagnini [7]. As we have pointed out already, in order to identify the third term in our formula with the sum B k ​ ( N) B_{k}(N) we require that k > 1 / 2 k>1/2. Given this condition, it is then immediate from ( 1.10) and ( 1.11) that ( 1.5) remains valid in this range for k k, but of course one can replace the O ⁡ ( N) O(N) term by a more explicit expression. For example, if one uses the zero-free region for ζ ⁡ ( s) \zeta(s) within ( 1.11), one readily confirms that

 | G k ​ ( N) = N 2 Γ ⁡ ( k + 3) − 2 A k ( N) + B k ( N) − 2 ζ ′ ζ ( 0) N Γ ⁡ ( k + 2) + O ( N exp ( − c log ⁡ N), \begin{split}G_{k}(N)&=\frac{N^{2}}{\Gamma(k+3)}-2A_{k}(N)+B_{k}(N)-2\frac{\zeta^{\prime}}{\zeta}(0)\frac{N}{\Gamma(k+2)}+O(N\exp(-c\sqrt{\log N}),\end{split} |  |

with some c > 0 c>0. However, a sharper truncated formula can be obtained by shifting the integrations in ( 1.9) to the left as much as is allowed by the convergence of the involved quantities. For example, shifting the integrations to (roughly) − 3 / 2 -3/2, we infer that in the range k > 1 / 2 k>1/2 one has

 | G k ​ ( N) = N 2 Γ ⁡ ( k + 3) − 2 ​ A k ​ ( N) + B k ​ ( N) − 2 ​ ζ ′ ζ ​ ( 0) ​ N Γ ⁡ ( k + 2) + 2 ​ ζ ′ ζ ​ ( 0) ​ Z N ​ ( k) + C + o ⁡ ( 1) \begin{split}G_{k}(N)=\frac{N^{2}}{\Gamma(k+3)}-2A_{k}(N)+B_{k}(N)-2\frac{\zeta^{\prime}}{\zeta}(0)\frac{N}{\Gamma(k+2)}+2\frac{\zeta^{\prime}}{\zeta}(0)Z_{N}(k)+C+o(1)\end{split} |  |

with

 | C = ( ζ ′ ζ ​ ( 0) 2 + 2 ​ ζ ′ ζ ​ ( − 1)) ​ 1 Γ ⁡ ( k + 1), C=\left(\frac{\zeta^{\prime}}{\zeta}(0)^{2}+2\frac{\zeta^{\prime}}{\zeta}(-1)\right)\frac{1}{\Gamma(k+1)}, |  |

which, up to an error of size o ⁡ ( 1) o(1), expresses G k ​ ( N) G_{k}(N) in terms of A k A_{k}, B k B_{k} and Z N ​ ( k) Z_{N}(k), all directly defined by sums of the zeros of the Riemann zeta function.

Acknowledgements. This research was partially supported by a grant from Deutsche Forschungsgemeinschaft, the grant PRIN-2015 “Number Theory and Arithmetic Geometry” and by a grant from the National Science Centre, Poland; AP is member of the GNAMPA group of INdAM.

## 2. The auxiliary functions

2.1. The analytic continuation. In this section, we are concerned with the auxiliary functions T N ​ ( w) T_{N}(w) and Z N ​ ( w) Z_{N}(w). Most of our efforts go into the proof of the following facts.

Proposition 1. Let N ≥ 4 N\geq 4, and let γ \gamma denote Euler’s constant. Then T N ​ ( w) T_{N}(w) extends to an entire function and satisfies

 | T N ​ ( w) = 1 Γ ⁡ ( w + 1) { − ∑ n = 1 ∞ Λ ⁡ ( n) n ( ( 1 − 1 n ​ N) w − 1) + ∫ 0 1 ( ( 1 − ξ N) w − 1) ξ ⋅ ξ − ( ( 1 − 1 N) w − 1) ​ log ⁡ ( 2 ​ π ​ e γ) − 1 2 ​ ( 1 − 1 N) w ​ log ⁡ ( 1 − 1 N 2) − ∫ 1 N ( ( 1 − 1 ξ) w − ( 1 − 1 N) w) ξ ​ ξ ⋅ N 2 − ξ 2 + N ∫ N ∞ ( ( 1 − 1 N) w − ( 1 − 1 ξ) w) ξ ⋅ ξ 2 − N 2 }. \begin{split}T_{N}(w)=&\frac{1}{\Gamma(w+1)}\Big\{-\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n}\Big(\big(1-\frac{1}{nN}\big)^{w}-1\Big)+\int_{0}^{1}\Big(\big(1-\frac{\xi}{N}\big)^{w}-1\Big)\,\frac{\d{\xi}}{\xi}\\ &-\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big)\log(2\pi e^{\gamma})-{\frac{1}{2}\big(1-\frac{1}{N}\big)^{w}}\log\big(1-\frac{1}{N^{2}}\big)\\ &-\int_{1}^{N}\Big(\big(1-\frac{1}{\xi}\big)^{w}-\big(1-\frac{1}{N}\big)^{w}\Big)\frac{\xi\,\d{\xi}}{N^{2}-\xi^{2}}\\ &+N\int_{N}^{\infty}\Big(\big(1-\frac{1}{N}\big)^{w}-\big(1-\frac{1}{\xi}\big)^{w}\Big)\frac{\d{\xi}}{\xi^{2}-N^{2}}\Big\}.\end{split} |  | (2.1) |

Moreover, there is a real number K K such that for any δ \delta with 0 < δ < 1 0<\delta<1 and | w + m | > δ |w+m|>\delta for all integers m ≥ 1 m\geq 1 we have

 | T N ​ ( w) ≤ K ​ 2 | u | ​ log ⁡ ( | w | + 2) δ ​ | Γ ⁡ ( w + 1) |. T_{N}(w)\leq K\frac{2^{|u|}\log(|w|+2)}{\delta|\Gamma(w+1)|}. |  | (2.2) |

There is a similar yet less explicit result for the function Z N ​ ( w) Z_{N}(w).

Proposition 2. Let N ≥ 4 N\geq 4. Then Z N ​ ( w) Z_{N}(w) extends to an entire function. Moreover, there is a real number K K such that for any δ \delta with 0 < δ < 1 0<\delta<1 and | w + m | > δ |w+m|>\delta for all integers m ≥ 1 m\geq 1 we have

 | Z N ​ ( w) ≤ K δ ​ | Γ ⁡ ( w + 1) | × { ( N | u | + 1 + 2 | u | ​ log ⁡ ( | w | + 2)) if u ∈ ℝ, ( N | u | ​ log ⁡ N + 2 | u | ​ log ⁡ | w |) if u ≤ − 3 / 2. Z_{N}(w)\leq\frac{K}{\delta|\Gamma(w+1)|}\times\begin{cases}\big(N^{|u|+1}+2^{|u|}\log(|w|+2)\big)&\ \text{if $u\in\mathbb{R}$},\\ \big(N^{|u|}\log N+2^{|u|}\log|w|\big)&\ \text{if $u\leq-3/2$}.\end{cases} |  | (2.3) |

2.2. The function T N ​ ( w) T_{N}(w). First steps. We begin with the proof of Proposition 1. From the functional equation of ζ ⁡ ( s) \zeta(s) in the form

 | ζ ⁡ ( 1 − s) = 2 ​ ( 2 ​ π) − s ​ cos ⁡ ( π ​ s 2) ​ Γ ​ ( s) ​ ζ ​ ( s) \zeta(1-s)=2(2\pi)^{-s}\cos\big(\frac{\pi s}{2}\big)\Gamma(s)\zeta(s) |  |

we obtain

 | ζ ′ ζ ​ ( s) = G ⁡ ( s) − ζ ′ ζ ​ ( 1 − s), \frac{\zeta^{\prime}}{\zeta}(s)=G(s)-\frac{\zeta^{\prime}}{\zeta}(1-s), |  | (2.4) |

where

 | G ⁡ ( s) = log ⁡ ( 2 ​ π) − g ′ g ​ ( s) and g ⁡ ( s) = Γ ⁡ ( s) ​ cos ⁡ π ​ s 2. G(s)=\log(2\pi)-\frac{g^{\prime}}{g}(s)\quad\text{and}\quad g(s)=\Gamma(s)\cos\frac{\pi s}{2}. |  | (2.5) |

Accordingly, for N ≥ 1 N\geq 1 and u > 0 u>0 we have

 | T N ​ ( w) = − 1 2 ​ π ​ i ∫ ( − 1 / 2) G ( s) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ + 1 2 ​ π ​ i ∫ ( − 1 / 2) ζ ′ ζ ( 1 − s) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ = − T N ( 1) ​ ( w) + T N ( 2) ​ ( w), \begin{split}T_{N}(w)&=-\frac{1}{2\pi i}\int_{(-1/2)}G(s)\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s}\\ &\hskip 14.22636pt+\frac{1}{2\pi i}\int_{(-1/2)}\frac{\zeta^{\prime}}{\zeta}(1-s)\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\d{s}\\ &=-T_{N}^{(1)}(w)+T_{N}^{(2)}(w),\end{split} |  | (2.6) |

say. Since the integration is on the line σ = − 1 / 2 \sigma=-1/2, we may expand ζ ′ ζ ​ ( 1 − s) \frac{\zeta^{\prime}}{\zeta}(1-s) and switch summation and integration, thus getting that

 | T N ( 2) ( w) = − ∑ n = 1 ∞ Λ ⁡ ( n) n ∫ ( − 1 / 2) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) ( n N) s s ⋅. T_{N}^{(2)}(w)=-\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n}\int_{(-1/2)}\frac{\Gamma(s)}{\Gamma(s+w+1)}(nN)^{s}\,\d{s}. |  | (2.7) |

We shift the line of integration in ( 2.7) to σ = c > 0 \sigma=c>0 and compute the residue at s = 0 s=0. Recalling that Λ ⁡ ( 1) = 0 \Lambda(1)=0, we infer from ( 1.8) with z = w z=w and x = ( n ​ N) − 1 x=(nN)^{-1} that

 | T N ( 2) ​ ( w) = − 1 Γ ⁡ ( w + 1) ​ ∑ n = 1 ∞ Λ ⁡ ( n) n ​ ( ( 1 − 1 n ​ N) w − 1). T_{N}^{(2)}(w)=\frac{{-}1}{\Gamma(w+1)}\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n}\Big(\big(1-\frac{1}{nN}\big)^{w}-1\Big). |  |

Yet, for N ≥ 1 N\geq 1, one has

 | ( 1 − 1 n ​ N) w − 1 ≪ w 1 n, \big(1-\frac{1}{nN}\big)^{w}-1\ll_{w}\frac{1}{n}, |  |

whence

 | T N ( 2) ​ ( w) = − 1 Γ ⁡ ( w + 1) ​ ∑ n = 1 ∞ Λ ⁡ ( n) n ​ ( ( 1 − 1 n ​ N) w − 1), T_{N}^{(2)}(w)=\frac{{-}1}{\Gamma(w+1)}\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n}\Big(\big(1-\frac{1}{nN}\big)^{w}-1\Big), |  | (2.8) |

the series being absolutely and compactly convergent on ℂ \mathbb{C}. In particular, for all N ≥ 1 N\geq 1, the function T N ( 2) ​ ( w) T_{N}^{(2)}(w) is entire.

2.3. Computing T N ( 1) ​ ( w) T_{N}^{(1)}(w). Recalling the definition of g ⁡ ( s) g(s) in ( 2.5) and the Hadamard products of 1 / Γ ⁡ ( s) 1/\Gamma(s) and cos ⁡ ( π ​ s / 2) \cos(\pi s/2) (Chapter 10 of Davenport [2] and Chapter 1 of Remmert [9], respectively) we obtain

 | g ⁡ ( s) = 1 s ​ e − γ ​ s ​ ∏ 2 | ν ν ≥ 1 ( ν s + ν) ​ e s / ν ​ ∏ 2 ∤ ν ν ≥ 1 ( 1 − s ν) ​ e s / ν, g(s)=\frac{1}{s}e^{-\gamma s}\prod_{\begin{subarray}{c}2|\nu\\ \nu\geq 1\end{subarray}}\left(\frac{\nu}{s+\nu}\right)e^{s/\nu}\prod_{\begin{subarray}{c}2\nmid\nu\\ \nu\geq 1\end{subarray}}\left(1-\frac{s}{\nu}\right)e^{s/\nu}, |  |

the products being absolutely and uniformly convergent on any compact subset of ℂ \mathbb{C} not containing a zero or pole of g ⁡ ( s) g(s). Therefore, away from such points we have

 | g ′ g ​ ( s) = − 1 s − γ − ∑ 2 | ν ν ≥ 1 ( 1 s + ν − 1 ν) + ∑ 2 ∤ ν ν ≥ 1 ( 1 s − ν + 1 ν) = − 1 s − γ − Σ 1 ​ ( s) + Σ 2 ​ ( s), \begin{split}\frac{g^{\prime}}{g}(s)&=-\frac{1}{s}-\gamma-\sum_{\begin{subarray}{c}2|\nu\\ \nu\geq 1\end{subarray}}\left(\frac{1}{s+\nu}-\frac{1}{\nu}\right)+\sum_{\begin{subarray}{c}2\nmid\nu\\ \nu\geq 1\end{subarray}}\left(\frac{1}{s-\nu}+\frac{1}{\nu}\right)\\ &=-\frac{1}{s}-\gamma-\Sigma_{1}(s)+\Sigma_{2}(s),\end{split} |  | (2.9) |

say. Recalling ( 2.5) and inserting ( 2.9) into the expression for T N ( 1) ​ ( w) T_{N}^{(1)}(w) in ( 2.6), for N ≥ 1 N\geq 1 we get

 | T N ( 1) ​ ( w) = 1 2 ​ π ​ i ∫ ( − 1 / 2) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s s ⋅ + ( log ( 2 π) + γ) 1 2 ​ π ​ i ∫ ( − 1 / 2) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ + 1 2 ​ π ​ i ∫ ( − 1 / 2) Σ 1 ( s) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ − 1 2 ​ π ​ i ∫ ( − 1 / 2) Σ 2 ( s) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ = T N ( 1, 1) ​ ( w) + log ⁡ ( 2 ​ π ​ e γ) ​ T N ( 1, 2) ​ ( w) + T N ( 1, 3) ​ ( w) − T N ( 1, 4) ​ ( w), \begin{split}T_{N}^{(1)}(w)&=\frac{1}{2\pi i}\int_{(-1/2)}\frac{\Gamma(s)}{\Gamma(s+w+1)}\,\frac{N^{s}}{s}\,\d{s}+\big(\log(2\pi)+\gamma\big)\frac{1}{2\pi i}\int_{(-1/2)}\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s}\\ &\hskip 17.07182pt+\frac{1}{2\pi i}\int_{(-1/2)}\Sigma_{1}(s)\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s}-\frac{1}{2\pi i}\int_{(-1/2)}\Sigma_{2}(s)\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s}\\ &=T_{N}^{(1,1)}(w)+\log\big(2\pi e^{\gamma}\big)T_{N}^{(1,2)}(w)+T_{N}^{(1,3)}(w)-T_{N}^{(1,4)}(w),\end{split} |  | (2.10) |

say. Next we compute separately the functions T N ( 1, j) ​ ( w) T_{N}^{(1,j)}(w), j = 1, …, 4 j=1,\dots,4, in ( 2.10).

2.4. Computing T N ( 1, 1) ​ ( w) T_{N}^{(1,1)}(w) and T N ( 1, 2) ​ ( w) T_{N}^{(1,2)}(w). We differentiate T N ( 1, 1) ​ ( w) T_{N}^{(1,1)}(w) with respect to N N and then apply ( 1.8) with z = w z=w and x = 1 / N x=1/N. For N ≥ 1 N\geq 1 and u > 0 u>0 this yields

 | ∂ ∂ N T N ( 1, 1) ( w) = 1 2 ​ π ​ i ​ N ∫ ( − 1 / 2) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ = 1 N ​ Γ ​ ( w + 1) ( ( 1 − 1 N) w − 1). \frac{\partial}{\partial N}T_{N}^{(1,1)}(w)=\frac{1}{2\pi iN}\int_{(-1/2)}\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s}=\frac{1}{N\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big). |  | (2.11) |

We remark that, here and later, the expression ( 1 − θ) w (1-\theta)^{w} equals 0 if θ = 1 \theta=1 and u > 0 u>0. Moreover, from the expression of T N ( 1, 1) ​ ( w) T_{N}^{(1,1)}(w) in ( 2.10) and the first equality in ( 2.11) we see that

 | T N ( 1, 1) ( w) ≪ N − 1 / 2 and ∂ ∂ N T N ( 1, 1) ( w) ≪ N − 3 / 2 as N → ∞, T_{N}^{(1,1)}(w)\ll N^{-1/2}\quad\text{and}\quad\frac{\partial}{\partial N}T_{N}^{(1,1)}(w)\ll N^{-3/2}\quad\text{as}\ N\to\infty, |  |

hence from the second equality in ( 2.11) we get

 | T N ( 1, 1) ( w) = − ∫ N ∞ ∂ ∂ x T x ( 1, 1) ( w) x ⋅ = − 1 Γ ⁡ ( w + 1) ∫ N ∞ ( ( 1 − 1 x) w − 1) x ⋅ x. T_{N}^{(1,1)}(w)=-\int_{N}^{\infty}\frac{\partial}{\partial x}T_{x}^{(1,1)}(w)\,\d{x}=-\frac{1}{\Gamma(w+1)}\int_{N}^{\infty}\Big(\big(1-\frac{1}{x}\big)^{w}-1\Big)\,\frac{\d{x}}{x}. |  | (2.12) |

Now we substitute

 | x = N ξ, 0 < ξ < 1, x ⋅ x = − ξ ⋅ ξ x=\frac{N}{\xi},\quad 0<\xi<1,\quad\frac{\d{x}}{x}=-\frac{\d{\xi}}{\xi} |  |

to see from ( 2.12) that

 | T N ( 1, 1) ( w) = − 1 Γ ⁡ ( w + 1) ∫ 0 1 ( ( 1 − ξ N) w − 1) ξ ⋅ ξ. T_{N}^{(1,1)}(w)=-\frac{1}{\Gamma(w+1)}\int_{0}^{1}\Big(\big(1-\frac{\xi}{N}\big)^{w}-1\Big)\,\frac{\d{\xi}}{\xi}. |  | (2.13) |

But as ξ → 0 + \xi\to 0^{+} we have ( 1 − ξ N) w − 1 ≪ ξ \big(1-\frac{\xi}{N}\big)^{w}-1\ll\xi, and this estimate holds uniformly as long as w w ranges over a fixed compact subset of ℂ \mathbb{C}. Hence ( 2.13) shows that T N ( 1, 1) ​ ( w) T_{N}^{(1,1)}(w) is an entire function for every N ≥ 2 N\geq 2.

We now turn to T N ( 1, 2) ​ ( w) T_{N}^{(1,2)}(w). Here, ( 1.8) immediately yields

 | T N ( 1, 2) ​ ( w) = 1 Γ ⁡ ( w + 1) ​ ( ( 1 − 1 N) w − 1), T_{N}^{(1,2)}(w)=\frac{1}{\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big), |  | (2.14) |

hence T N ( 1, 2) ​ ( w) T_{N}^{(1,2)}(w) is an entire function as well, for every N ≥ 2 N\geq 2.

2.5. Computing T N ( 1, 3) ​ ( w) T_{N}^{(1,3)}(w). Suppose that N ≥ 1 N\geq 1 and u > 0 u>0. Then, recalling ( 2.9) and ( 2.10), we infer from ( 1.8) that

 | T N ( 1, 3) ​ ( w) = ∑ ν = 2 2 | ν ∞ { 1 2 ​ π ​ i ∫ ( − 1 / 2) N s s + ν Γ ⁡ ( s) Γ ⁡ ( s + w + 1) s ⋅ − 1 ν ​ Γ ​ ( w + 1) ( ( 1 − 1 N) w − 1) } = ∑ ν = 2 2 | ν ∞ { H N ​ ( w, ν) − 1 ν ​ Γ ​ ( w + 1) ​ ( ( 1 − 1 N) w − 1) }, \begin{split}T_{N}^{(1,3)}(w)&=\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}\Big\{\frac{1}{2\pi i}\int_{(-1/2)}\frac{N^{s}}{s+\nu}\,\frac{\Gamma(s)}{\Gamma(s+w+1)}\,\d{s}-\frac{1}{\nu\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big)\Big\}\\ &=\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}\left\{H_{N}(w,\nu)-\frac{1}{\nu\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big)\right\},\end{split} |  | (2.15) |

say. We differentiate the identity

 | N ν H N ( w, ν) = 1 2 ​ π ​ i ∫ ( − 1 / 2) N s + ν s + ν Γ ⁡ ( s) Γ ⁡ ( s + w + 1) s ⋅, N^{\nu}H_{N}(w,\nu)=\frac{1}{2\pi i}\int_{(-1/2)}\frac{N^{s+\nu}}{s+\nu}\,\frac{\Gamma(s)}{\Gamma(s+w+1)}\d{s}, |  | (2.16) |

with respect to N N and then applying ( 1.8) to confirm that H N ​ ( w, ν) H_{N}(w,\nu) satisfies the differential equation

 | ∂ ∂ N ​ H N ​ ( w, ν) + ν N ​ H N ​ ( w, ν) = 1 N ​ Γ ​ ( w + 1) ​ ( ( 1 − 1 N) w − 1). \frac{\partial}{\partial N}H_{N}(w,\nu)+\frac{\nu}{N}H_{N}(w,\nu)=\frac{1}{N\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big). |  | (2.17) |

We solve ( 2.17) by searching for a function c N ​ ( w, ν) c_{N}(w,\nu) such that

 | H N ​ ( w, ν) = c N ​ ( w, ν) ​ N − ν, H_{N}(w,\nu)=c_{N}(w,\nu)N^{-\nu}, |  | (2.18) |

which in view of ( 2.17) satisfies

 | ∂ ∂ N ​ c N ​ ( w, ν) = N ν − 1 Γ ⁡ ( w + 1) ​ ( ( 1 − 1 N) w − 1). \frac{\partial}{\partial N}c_{N}(w,\nu)=\frac{N^{\nu-1}}{\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big). |  | (2.19) |

Next we take N = 1 N=1 in ( 2.16). A computation based on Stirling’s formula shows that for each ν ≥ 1 \nu\geq 1 one has

 | lim x → + ∞ 1 2 ​ π ​ i ​ ∫ ( x) 1 s + ν ​ Γ ⁡ ( s) Γ ⁡ ( s + w + 1) ​ s ⋅ = 0, \lim_{x\to+\infty}\frac{1}{2\pi i}\int_{(x)}\frac{1}{s+\nu}\,\frac{\Gamma(s)}{\Gamma(s+w+1)}\,\d{s}=0, |  |

uniformly for w w in any fixed compact part of u > 0 u>0; we refer to Section 3 for a more explicit presentation of similar computations. Hence, from ( 2.16) and ( 2.18) with N = 1 N=1, shifting the line of integration to + ∞ +\infty and computing the residue at s = 0 s=0 we obtain the boundary condition

 | c 1 ​ ( w, ν) = − 1 ν ​ Γ ​ ( w + 1). c_{1}(w,\nu)=-\frac{1}{\nu\Gamma(w+1)}. |  |

As a consequence, integrating ( 2.19) from 1 1 to N N we get

 | c N ​ ( w, ν) = − 1 ν ​ Γ ​ ( w + 1) + ∫ 1 N ξ ν − 1 Γ ⁡ ( w + 1) ​ ( ( 1 − 1 ξ) w − 1) ​ ξ ⋅. c_{N}(w,\nu)=-\frac{1}{\nu\Gamma(w+1)}+\int_{1}^{N}\frac{\xi^{\nu-1}}{\Gamma(w+1)}\Big(\big(1-\frac{1}{\xi}\big)^{w}-1\Big)\,\d{\xi}. |  |

Therefore, from ( 2.18) and ( 2.15) we obtain that for N ≥ 1 N\geq 1 and u > 0 u>0 one has

 | T N ( 1, 3) ​ ( w) = 1 Γ ⁡ ( w + 1) ​ ∑ ν = 2 2 | ν ∞ { ∫ 1 N ( ξ N) ν ​ ( ( 1 − 1 ξ) w − 1) ​ ξ ⋅ ξ − N − ν ν − 1 ν ​ ( ( 1 − 1 N) w − 1) }. T_{N}^{(1,3)}(w)=\frac{1}{\Gamma(w+1)}{\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}}\Big\{\int_{1}^{N}\big(\frac{\xi}{N}\big)^{\nu}\Big(\big(1-\frac{1}{\xi}\big)^{w}-1\Big)\,\frac{\d{\xi}}{\xi}-\frac{N^{-\nu}}{\nu}-\frac{1}{\nu}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big)\Big\}. |  | (2.20) |

But for N ≥ 2 N\geq 2 we have

 | ∑ ν = 2 2 | ν ∞ N − ν ν = 1 2 ​ ∑ ν = 1 ∞ N − 2 ​ ν ν = − 1 2 ​ log ⁡ ( 1 − 1 N 2) {\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}}\frac{N^{-\nu}}{\nu}=\frac{1}{2}\sum_{\nu=1}^{\infty}\frac{N^{-2\nu}}{\nu}=-\frac{1}{2}\log\big(1-\frac{1}{N^{2}}\big) |  |

and

 | ∫ 1 N ( ξ N) ν ​ ξ ⋅ ξ + N − ν ν = 1 ν, \int_{1}^{N}\big(\frac{\xi}{N}\big)^{\nu}\,\frac{\d{\xi}}{\xi}+\frac{N^{-\nu}}{\nu}=\frac{1}{\nu}, |  |

so that ( 2.20) becomes

 | = 1 Γ ⁡ ( w + 1) ​ { 1 2 ​ ( 1 − 1 N) w ​ log ⁡ ( 1 − 1 N 2) + ∑ ν = 2 2 | ν ∞ ∫ 1 N ( ξ N) ν ​ ( ( 1 − 1 ξ) w − ( 1 − 1 N) w) ​ ξ ⋅ ξ } = 1 Γ ⁡ ( w + 1) ​ { 1 2 ​ ( 1 − 1 N) w ​ log ⁡ ( 1 − 1 N 2) + ∫ 1 N ( ( 1 − 1 ξ) w − ( 1 − 1 N) w) ​ ξ 2 / N 2 1 − ξ 2 / N 2 ​ ξ ⋅ ξ }. \begin{split}&=\frac{1}{\Gamma(w+1)}\Big\{\frac{1}{2}\big(1-\frac{1}{N}\big)^{w}\log\big(1-\frac{1}{N^{2}}\big)+{\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}}\int_{1}^{N}\big(\frac{\xi}{N}\big)^{\nu}\Big(\big(1-\frac{1}{\xi}\big)^{w}-\big(1-\frac{1}{N}\big)^{w}\Big)\,\frac{\d{\xi}}{\xi}\Big\}\\ &=\frac{1}{\Gamma(w+1)}\Big\{\frac{1}{2}\big(1-\frac{1}{N}\big)^{w}\log\big(1-\frac{1}{N^{2}}\big)+\int_{1}^{N}\Big(\big(1-\frac{1}{\xi}\big)^{w}-\big(1-\frac{1}{N}\big)^{w}\Big)\frac{\xi^{2}/N^{2}}{1-\xi^{2}/N^{2}}\,\frac{\d{\xi}}{\xi}\Big\}.\end{split} |  |

Note that the above integral is convergent at ξ = N \xi=N since for N ≥ 2 N\geq 2 and w w in a compact part of ℂ \mathbb{C} we have

 | ( 1 − 1 ξ) w − ( 1 − 1 N) w ≪ N − ξ \big(1-\frac{1}{\xi}\big)^{w}-\big(1-\frac{1}{N}\big)^{w}\ll N-\xi |  | (2.21) |

uniformly in w w as ξ → N − \xi\to N^{-}. Therefore, for N ≥ 2 N\geq 2 and u > 0 u>0 we deduce that

 | T N ( 1, 3) ​ ( w) = 1 Γ ⁡ ( w + 1) ​ { 1 2 ​ ( 1 − 1 N) w ​ log ⁡ ( 1 − 1 N 2) + ∫ 1 N ( ( 1 − 1 ξ) w − ( 1 − 1 N) w) ​ ξ ​ ξ ⋅ N 2 − ξ 2 }. T_{N}^{(1,3)}(w)=\frac{1}{\Gamma(w+1)}\Big\{\frac{1}{2}\big(1-\frac{1}{N}\big)^{w}\log\big(1-\frac{1}{N^{2}}\big)+\int_{1}^{N}\Big(\big(1-\frac{1}{\xi}\big)^{w}-\big(1-\frac{1}{N}\big)^{w}\Big)\frac{\xi\,\d{\xi}}{N^{2}-\xi^{2}}\Big\}. |  | (2.22) |

Moreover, thanks to ( 2.21), if N ≥ 3 N\geq 3 the part of the integral in ( 2.22) over [2, N] [2,N] extends to an entire function, and clearly the function

 | ∫ 1 2 ( 1 − 1 N) w ​ ξ ​ ξ ⋅ N 2 − ξ 2 \int_{1}^{2}\big(1-\frac{1}{N}\big)^{w}\frac{\xi\,\d{\xi}}{N^{2}-\xi^{2}} |  |

is also entire.

Consider now the remaining part of the second term on the right hand side of ( 2.22), namely

 | I ⁡ ( w) = 1 Γ ⁡ ( w + 1) ​ ∫ 1 2 ( 1 − 1 ξ) w ​ ξ ​ ξ ⋅ N 2 − ξ 2. I(w)=\frac{1}{\Gamma(w+1)}\int_{1}^{2}\big(1-\frac{1}{\xi}\big)^{w}\frac{\xi\,\d{\xi}}{N^{2}-\xi^{2}}. |  | (2.23) |

By the substitution 1 − 1 / ξ = x 1-1/\xi=x, and hence ξ = 1 / ( 1 − x) \xi=1/(1-x) and ξ ⋅ = x ⋅ / ( 1 − x) 2 \d{\xi}=\d{x}/(1-x)^{2}, we find that

 | I ⁡ ( w) = 1 Γ ⁡ ( w + 1) ​ ∫ 0 1 / 2 x w ​ x ⋅ ( 1 − x) ​ ( N 2 ​ ( 1 − x) 2 − 1). I(w)=\frac{1}{\Gamma(w+1)}\int_{0}^{1/2}x^{w}\frac{\d{x}}{(1-x)(N^{2}(1-x)^{2}-1)}. |  | (2.24) |

Now we assume N ≥ 4 N\geq 4 and consider the function

 | h N ​ ( z) = 1 ( 1 − z) ​ ( N 2 ​ ( 1 − z) 2 − 1) = ∑ m = 0 ∞ a N ​ ( m) ​ z m, h_{N}(z)=\frac{1}{(1-z)(N^{2}(1-z)^{2}-1)}=\sum_{m=0}^{\infty}a_{N}(m)z^{m}, |  |

which is holomorphic in | z | < 1 − 1 / N |z|<1-1/N. By Cauchy’s coefficient formula we see that whenever 0 < δ < 1 − 1 / N 0<\delta<1-1/N we have | a N ​ ( m) | ≤ δ − m ​ max | z | = δ ​ | h N ​ ( z) | |a_{N}(m)|\leq\delta^{-m}\max_{|z|=\delta}|h_{N}(z)|. We take δ = 2 / 3 \delta=2/3 and infer that

 | a N ​ ( m) ≤ 10 ​ ( 3 / 2) m. a_{N}(m)\leq 10(3/2)^{m}. |  | (2.25) |

From ( 2.24) and ( 2.25) we therefore obtain that

 | I ⁡ ( w) = 1 Γ ⁡ ( w + 1) ​ ∑ m = 0 ∞ a N ​ ( m) ​ ∫ 0 1 / 2 x w + m ​ x ⋅ = 2 − ( w + 1) Γ ⁡ ( w + 1) ​ ∑ m = 0 ∞ a N ​ ( m) ​ 2 − m w + 1 + m. I(w)=\frac{1}{\Gamma(w+1)}\sum_{m=0}^{\infty}a_{N}(m)\int_{0}^{1/2}x^{w+m}\d{x}=\frac{2^{-(w+1)}}{\Gamma(w+1)}\sum_{m=0}^{\infty}\frac{a_{N}(m)2^{-m}}{w+1+m}. |  | (2.26) |

By ( 2.25), the last series converges absolutely, and uniformly on any compact part of ℂ \mathbb{C} not containing any of the points w + 1 = − m w+1=-m with m ≥ 0 m\geq 0, and hence it represents a meromorphic function with at most simple poles at w + 1 = − m w+1=-m, m ≥ 0 m\geq 0. But such poles cancel with the zeros of 1 / Γ ⁡ ( w + 1) 1/\Gamma(w+1), so that I ⁡ ( w) I(w) is an entire function. Gathering the previous results of this subsection, we finally conclude that T N ( 1, 3) ​ ( w) T_{N}^{(1,3)}(w) is an entire function, for each N ≥ 4 N\geq 4.

2.6. Computing T N ( 1, 4) ​ ( w) T_{N}^{(1,4)}(w). Since the term T N ( 1, 4) ​ ( w) T_{N}^{(1,4)}(w) is similar to T N ( 1, 3) ​ ( w) T_{N}^{(1,3)}(w), a treatment along the lines of the previous subsection is possible. The details turn out to be somewhat simpler, and hence we shall be more sketchy here. In analogy with ( 2.15), ( 2.16) and ( 2.17), for N ≥ 1 N\geq 1 and u > 0 u>0 we have

 | T N ( 1, 4) ​ ( w) = ∑ ν = 2 2 | ν ∞ { H ~ N ​ ( w, ν) + 1 ν ​ Γ ​ ( w + 1) ​ ( ( 1 − 1 N) w − 1) }, T_{N}^{(1,4)}(w)={\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}}\left\{\widetilde{H}_{N}(w,\nu)+\frac{1}{\nu\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big)\right\}, |  | (2.27) |

where H ~ N ​ ( w, ν) \widetilde{H}_{N}(w,\nu) satisfies

 | N − ν H ~ N ( w, ν) = 1 2 ​ π ​ i ∫ ( − 1 / 2) N s − ν s − ν Γ ⁡ ( s) Γ ⁡ ( s + w + 1) s ⋅ N^{-\nu}\widetilde{H}_{N}(w,\nu)=\frac{1}{2\pi i}\int_{(-1/2)}\frac{N^{s-\nu}}{s-\nu}\,\frac{\Gamma(s)}{\Gamma(s+w+1)}\,\d{s} |  | (2.28) |

and

 | ∂ ∂ N ​ H ~ N ​ ( w, ν) − ν N ​ H ~ N ​ ( w, ν) = 1 N ​ Γ ​ ( w + 1) ​ ( ( 1 − 1 N) w − 1). \frac{\partial}{\partial N}\widetilde{H}_{N}(w,\nu)-\frac{\nu}{N}\widetilde{H}_{N}(w,\nu)=\frac{1}{N\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big). |  |

Moreover, as in ( 2.18) we search for a function c ~ N ​ ( w, ν) \widetilde{c}_{N}(w,\nu) such that

 | H ~ N ​ ( w, ν) = c ~ N ​ ( w, ν) ​ N ν, \widetilde{H}_{N}(w,\nu)=\widetilde{c}_{N}(w,\nu)N^{\nu}, |  | (2.29) |

which in analogy with ( 2.19) satisfies

 | ∂ ∂ N ​ c ~ N ​ ( w, ν) = N − ν − 1 Γ ⁡ ( w + 1) ​ ( ( 1 − 1 N) w − 1). \frac{\partial}{\partial N}\widetilde{c}_{N}(w,\nu)=\frac{N^{-\nu-1}}{\Gamma(w+1)}\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big). |  |

Now, from ( 2.28) and ( 2.29) we have that for any given ν ≥ 1 \nu\geq 1 and w w with u > 0 u>0, as N → ∞ N\to\infty

 | c ~ N ( w, ν) ≪ N − 1 / 2 − ν, \widetilde{c}_{N}(w,\nu)\ll N^{-1/2-\nu}, |  |

hence

 | c ~ N ( w, ν) = − 1 Γ ⁡ ( w + 1) ∫ N ∞ ( ( 1 − 1 ξ) w − 1) ξ − ν − 1 ξ ⋅ \widetilde{c}_{N}(w,\nu)=-\frac{1}{\Gamma(w+1)}\int_{N}^{\infty}\Big(\big(1-\frac{1}{\xi}\big)^{w}-1\Big)\xi^{-\nu-1}\,\d{\xi} |  |

and therefore

 | H ~ N ( w, ν) = − 1 Γ ⁡ ( w + 1) ∫ N ∞ ( ( 1 − 1 ξ) w − 1) ( N ξ) ν ξ ⋅ ξ. \widetilde{H}_{N}(w,\nu)=-\frac{1}{\Gamma(w+1)}\int_{N}^{\infty}\Big(\big(1-\frac{1}{\xi}\big)^{w}-1\Big)\big(\frac{N}{\xi}\big)^{\nu}\,\frac{\d{\xi}}{\xi}. |  |

Inserting this into ( 2.27), in analogy with ( 2.22) we obtain that for N ≥ 2 N\geq 2 and u > 0 u>0

 | T N ( 1, 4) ​ ( w) = 1 Γ ⁡ ( w + 1) ​ ∑ ν = 2 2 | ν ∞ { ( ( 1 − 1 N) w − 1) ​ ∫ N ∞ ( N ξ) ν ​ ξ ⋅ ξ − ∫ N ∞ ( ( 1 − 1 ξ) w − 1) ​ ( N ξ) ν ​ ξ ⋅ ξ } = 1 Γ ⁡ ( w + 1) ​ ∫ N ∞ ( ( 1 − 1 N) w − ( 1 − 1 ξ) w) ​ N / ξ 1 − N 2 / ξ 2 ​ ξ ⋅ ξ = N Γ ⁡ ( w + 1) ​ ∫ N ∞ ( ( 1 − 1 N) w − ( 1 − 1 ξ) w) ​ ξ ⋅ ξ 2 − N 2. \begin{split}T_{N}^{(1,4)}(w)&=\frac{1}{\Gamma(w+1)}{\sum_{\begin{subarray}{c}\nu=2\\ 2\mid\nu\end{subarray}}^{\infty}}\Big\{\Big(\big(1-\frac{1}{N}\big)^{w}-1\Big)\int_{N}^{\infty}\big(\frac{N}{\xi}\big)^{\nu}\,\frac{\d{\xi}}{\xi}-\int_{N}^{\infty}\Big(\big(1-\frac{1}{\xi}\big)^{w}-1\Big)\big(\frac{N}{\xi}\big)^{\nu}\,\frac{\d{\xi}}{\xi}\Big\}\\ &=\frac{1}{\Gamma(w+1)}\int_{N}^{\infty}\Big(\big(1-\frac{1}{N}\big)^{w}-\big(1-\frac{1}{\xi}\big)^{w}\Big)\frac{N/\xi}{1-N^{2}/\xi^{2}}\,\frac{\d{\xi}}{\xi}\\ &=\frac{N}{\Gamma(w+1)}\int_{N}^{\infty}\Big(\big(1-\frac{1}{N}\big)^{w}-\big(1-\frac{1}{\xi}\big)^{w}\Big)\,\frac{\d{\xi}}{\xi^{2}-N^{2}}.\end{split} |  |

Finally, since the last integral is uniformly convergent at N N as long as w w ranges over a compact part of ℂ \mathbb{C}, thanks to ( 2.21), and clearly the same holds at ∞ \infty, the function

 | T N ( 1, 4) ​ ( w) = N Γ ⁡ ( w + 1) ​ ∫ N ∞ ( ( 1 − 1 N) w − ( 1 − 1 ξ) w) ​ ξ ⋅ ξ 2 − N 2 T_{N}^{(1,4)}(w)=\frac{N}{\Gamma(w+1)}\int_{N}^{\infty}\Big(\big(1-\frac{1}{N}\big)^{w}-\big(1-\frac{1}{\xi}\big)^{w}\Big)\,\frac{\d{\xi}}{\xi^{2}-N^{2}} |  | (2.30) |

is entire.

The expression ( 2.1) in Proposition 1 and the fact that T N ​ ( w) T_{N}(w) is an entire function now follow gathering ( 2.6), ( 2.8), ( 2.10), ( 2.13), ( 2.14), ( 2.22), the conclusion of Subsection 2.5 and ( 2.30).

2.7. Estimating T N ​ ( w) T_{N}(w). In order to prove ( 2.2) we estimate the terms inside the brackets on the right hand side of ( 2.1). The first term is bounded by

 | ≪ ∑ n ≤ | w | Λ ⁡ ( n) n ​ ( ( 1 − 1 n ​ N) u + 1) + ∑ n > | w | Λ ⁡ ( n) n ​ | ( 1 − 1 n ​ N) w − 1 |, \ll\sum_{n\leq|w|}\frac{\Lambda(n)}{n}\Big(\big(1-\frac{1}{nN}\big)^{u}+1\Big)+\sum_{n>|w|}\frac{\Lambda(n)}{n}\Big|\big(1-\frac{1}{nN}\big)^{w}-1\Big|, |  |

and, uniformly for N ≥ 4 N\geq 4, we have that

 | ( 1 − 1 n ​ N) u + 1 ≪ 2 | u |, ( 1 − 1 n ​ N) w − 1 = e w ​ log ⁡ ( 1 − 1 / ( n ​ N)) − 1 ≪ | w | n for n > | w |. \big(1-\frac{1}{nN}\big)^{u}+1\ll 2^{|u|},\qquad\big(1-\frac{1}{nN}\big)^{w}-1=e^{w\log(1-1/(nN))}-1\ll\frac{|w|}{n}\ \ \text{for}\ \ n>|w|. |  |

Therefore, by standard elementary bounds the above two sums are bounded by

 | ≪ 2 | u | log ( | w | + 2) and ≪ | w | ∑ n > | w | log ⁡ n n 2 ≪ log ( | w | + 2) \ll 2^{|u|}\log(|w|+2)\qquad\text{and}\qquad\ll|w|\sum_{n>|w|}\frac{\log n}{n^{2}}\ll\log(|w|+2) |  |

respectively, and hence for any w ∈ ℂ w\in\mathbb{C} and N ≥ 4 N\geq 4 one has

 | ∑ n = 1 ∞ Λ ⁡ ( n) n ​ ( ( 1 − 1 n ​ N) w − 1) ≪ 2 | u | ​ log ⁡ ( | w | + 2). \sum_{n=1}^{\infty}\frac{\Lambda(n)}{n}\Big(\big(1-\frac{1}{nN}\big)^{w}-1\Big)\ll 2^{|u|}\log(|w|+2). |  | (2.31) |

The second term in ( 2.1) vanishes for w = 0 w=0, and ( 1 − ξ / N) w − 1 ≪ | w | ​ ξ (1-\xi/N)^{w}-1\ll|w|\xi holds for ξ < 1 / | w | \xi<1/|w|, for every N ≥ 4 N\geq 4. Hence such a term is ≪ 1 \ll 1 when | w | ≤ 1 |w|\leq 1, while we split the range of integration into [0, 1 / | w |] ∪ [1 / | w |, 1] [0,1/|w|]\cup[1/|w|,1] when | w | > 1 |w|>1. In this case we have

 | ∫ 0 1 ( ( 1 − ξ N) w − 1) ​ ξ ⋅ ξ ≪ 1 + 2 | u | ​ ∫ 1 / | w | 1 ξ ⋅ ξ ≪ 2 | u | ​ log ⁡ ( | w | + 2), \int_{0}^{1}\Big(\big(1-\frac{\xi}{N}\big)^{w}-1\Big)\,\frac{\d{\xi}}{\xi}\ll 1+2^{|u|}\int_{1/|w|}^{1}\frac{\d{\xi}}{\xi}\ll 2^{|u|}\log(|w|+2), |  | (2.32) |

and clearly the last bound in ( 2.32) holds for every w ∈ ℂ w\in\mathbb{C} and N ≥ 4 N\geq 4.

Obviously, the third and fourth term in ( 2.1) are bounded, for every w ∈ ℂ w\in\mathbb{C} and N ≥ 4 N\geq 4, by

 | ≪ 2 | u |. \ll 2^{|u|}. |  | (2.33) |

More care is required for the fifth term in ( 2.1), stemming from the integral in ( 2.22). In this integral we denote by A ⁡ ( w) A(w) the part over [1, 2] [1,2]. For w ∈ ℂ w\in\mathbb{C} and N ≥ 4 N\geq 4 we have

 | A ⁡ ( w) = ∫ 1 2 ( 1 − 1 ξ) w ​ ξ ​ ξ ⋅ N 2 − ξ 2 + O ⁡ ( 2 | u | ​ ∫ 1 2 ξ ​ ξ ⋅ N 2 − ξ 2) = A 1 ​ ( w) + O ⁡ ( 2 | u |), A(w)=\int_{1}^{2}\big(1-\frac{1}{\xi}\big)^{w}\,\frac{\xi\,\d{\xi}}{N^{2}-\xi^{2}}+O\Big(2^{|u|}\int_{1}^{2}\frac{\xi\,\d{\xi}}{N^{2}-\xi^{2}}\Big)=A_{1}(w)+O\big(2^{|u|}\big), |  |

say. In view of ( 2.23) and ( 2.26) we have

 | A 1 ​ ( w) = 2 − ( w + 1) ​ ∑ m = 0 ∞ a N ​ ( m) ​ 2 − m w + 1 + m, A_{1}(w)=2^{-(w+1)}\sum_{m=0}^{\infty}\frac{a_{N}(m)2^{-m}}{w+1+m}, |  |

and thanks to ( 2.25), for | w + m + 1 | > δ |w+m+1|>\delta we get A 1 ​ ( w) ≪ 2 | u | / δ A_{1}(w)\ll 2^{|u|}/\delta. Hence

 | A ⁡ ( w) ≪ 2 | u | δ. A(w)\ll\frac{2^{|u|}}{\delta}. |  |

In order to deal with the part over [2, N] [2,N] of the integral in ( 2.22) we note that

 | ( 1 − 1 ξ) ​ ( 1 − 1 N) − 1 = 1 + O ⁡ ( | N − ξ | N), \big(1-\frac{1}{\xi}\big)\big(1-\frac{1}{N}\big)^{-1}=1+O\big(\frac{|N-\xi|}{N}\big), |  |

and hence for ξ > N ⁡ ( 1 − 1 / | w |) \xi>N(1-1/|w|) we have

 | ( 1 − 1 ξ) w − ( 1 − 1 N) w = ( 1 − 1 N) w ​ ( e w ​ log ⁡ ( 1 − 1 / ξ) ​ ( 1 − 1 / N) − 1 − 1) ≪ 2 | u | ​ | w | ​ | N − ξ | N. \big(1-\frac{1}{\xi}\big)^{w}-\big(1-\frac{1}{N}\big)^{w}=\big(1-\frac{1}{N}\big)^{w}\Big(e^{w\log(1-1/\xi)(1-1/N)^{-1}}-1\Big)\ll 2^{|u|}|w|\frac{|N-\xi|}{N}. |  | (2.34) |

We temporarily assume that | w | > ( 1 − 2 / N) − 1 |w|>(1-2/N)^{-1}, and split the integral over [2, N) [2,{N}) into the part over [2, N ⁡ ( 1 − 1 / | w |)] [2,N(1-1/|w|)] and the part over [N ⁡ ( 1 − 1 / | w |), N] [N(1-1/|w|),N], and denote by B ⁡ ( w) B(w) and C ⁡ ( w) C(w) these parts, respectively. A direct estimate gives

 | B ⁡ ( w) ≪ 2 | u | ​ ∫ 2 N ⁡ ( 1 − 1 / | w |) ξ ⋅ N − ξ ≪ 2 | u | ​ log ⁡ ( | w | + 2), B(w)\ll 2^{|u|}\int_{2}^{N(1-1/|w|)}\frac{\d{\xi}}{N-\xi}\ll 2^{|u|}\log(|w|+2), |  |

while thanks to ( 2.34) we obtain

 | C ⁡ ( w) ≪ 2 | u | ​ | w | ​ ∫ N ⁡ ( 1 − 1 / | w |) N N − ξ N 2 − ξ 2 ​ ξ ⋅ ≪ 2 | u |. C(w)\ll 2^{|u|}|w|\int_{N(1-1/|w|)}^{N}\frac{N-\xi}{N^{2}-\xi^{2}}\,\d{\xi}\ll 2^{|u|}. |  | (2.35) |

The case where | w | ≤ ( 1 − 2 / N) − 1 |w|\leq(1-2/N)^{-1} is simpler. Here the whole integral over [2, N] [2,N] can be estimated as we bounded C ⁡ ( w) C(w). Therefore, gathering the above bounds for A ⁡ ( w), B ⁡ ( w) A(w),B(w) and C ⁡ ( w) C(w) we conclude that the fifth term in ( 2.1) is bounded by

 | ≪ 2 | u | ​ log ⁡ ( | w | + 2) δ \ll\frac{2^{|u|}\log(|w|+2)}{\delta} |  | (2.36) |

for every N ≥ 4 N\geq 4 and w ∈ ℂ w\in\mathbb{C} satisfying | w + n + 2 | > δ |w+n+2|>\delta.

Similarly, we split the integral over [N, ∞) [N,\infty) in the sixth term of ( 2.1) into the part over [N, N ⁡ ( 1 + 1 / | w |)] [N,N(1+1/|w|)] plus the part over [N ⁡ ( 1 + 1 / | w |), ∞) [N(1+1/|w|),\infty), which we denote by D ⁡ ( w) D(w) and E ⁡ ( w) E(w), respectively. Arguing as in ( 2.35) we have

 | N ​ D ​ ( w) ≪ 2 | u | ​ | w | ​ ∫ N N ⁡ ( 1 + 1 / | w |) ξ − N ξ 2 − N 2 ​ ξ ⋅ ≪ 2 | u |, ND(w)\ll 2^{|u|}|w|\int_{N}^{N(1+1/|w|)}\frac{\xi-N}{\xi^{2}-N^{2}}\,\d{\xi}\ll 2^{|u|}, |  |

while a direct estimate gives

 | N ​ E ​ ( w) ≪ 2 | u | ​ N ​ ∫ N ⁡ ( 1 + 1 / | w |) ∞ ξ ⋅ ξ 2 − N 2. NE(w)\ll 2^{|u|}N\int_{N(1+1/|w|)}^{\infty}\frac{\d{\xi}}{\xi^{2}-N^{2}}. |  |

Substituting ξ − N = y \xi-N=y, decomposing y − 1 ​ ( y + 2 ​ N) − 1 y^{-1}(y+2N)^{-1} into partial fractions and computing the resulting integrals we obtain

 | ∫ N ⁡ ( 1 + 1 / | w |) ∞ ξ ⋅ ξ 2 − N 2 = 1 2 ​ N ​ log ⁡ ( 2 ​ | w | + 1). \int_{N(1+1/|w|)}^{\infty}\frac{\d{\xi}}{\xi^{2}-N^{2}}=\frac{1}{2N}\log(2|w|+1). |  |

Hence the sixth term in ( 2.1) is bounded by

 | ≪ 2 | u | ​ log ⁡ ( | w | + 2) \ll 2^{|u|}\log(|w|+2) |  | (2.37) |

for every N ≥ 4 N\geq 4 and w ∈ ℂ w\in\mathbb{C}.

Gathering ( 2.31),( 2.32),( 2.33),( 2.36) and ( 2.37), we obtain ( 2.2), and the proof of Proposition 1 is complete. ∎

2.8. Proof of Proposition 2. Let u > 0 u>0. An application of ( 1.8), followed by a shift of the line of integration to σ = − 1 / 2 \sigma=-1/2, yields the identities

 | 1 Γ ⁡ ( w + 1) ​ ∑ n < N Λ ⁡ ( n) ​ ( 1 − n N) w = − 1 2 ​ π ​ i ∫ ( 2) ζ ′ ζ ( s) Γ ⁡ ( s) Γ ⁡ ( s + w + 1) N s s ⋅ = N Γ ⁡ ( w + 2) − Z N ​ ( w) − ζ ′ ζ ​ ( 0) ​ 1 Γ ⁡ ( w + 1) + T N ​ ( w). \begin{split}\frac{1}{\Gamma(w+1)}\sum_{n<N}\Lambda(n)\big(1-\frac{n}{N}\big)^{w}&=-\frac{1}{2\pi i}\int_{(2)}\frac{\zeta^{\prime}}{\zeta}(s)\frac{\Gamma(s)}{\Gamma(s+w+1)}N^{s}\,\d{s}\\ &=\frac{N}{\Gamma(w+2)}-Z_{N}(w)-\frac{\zeta^{\prime}}{\zeta}(0)\frac{1}{\Gamma(w+1)}+T_{N}(w).\end{split} |  | (2.38) |

In view of Proposition 1, ( 2.38) gives the analytic continuation of Z N ​ ( w) Z_{N}(w) to ℂ \mathbb{C}. Moreover, for | s + m | > δ |s+m|>\delta we have

 | Z N ​ ( w) ≪ 1 | Γ ⁡ ( w + 1) | ​ ∑ n < N Λ ⁡ ( n) ​ ( 1 − n N) u + N δ ​ | Γ ⁡ ( w + 1) | + 1 | Γ ⁡ ( w + 1) | + | T N ​ ( w) |. Z_{N}(w)\ll\frac{1}{|\Gamma(w+1)|}\sum_{n<N}\Lambda(n)\big(1-\frac{n}{N}\big)^{u}+\frac{N}{\delta|\Gamma(w+1)|}+\frac{1}{|\Gamma(w+1)|}+|T_{N}(w)|. |  |

But clearly we have

 | ∑ n < N Λ ⁡ ( n) ​ ( 1 − n N) u ≪ N | u | + 1 \sum_{n<N}\Lambda(n)\big(1-\frac{n}{N}\big)^{u}\ll N^{|u|+1} |  |

for every u ∈ ℝ u\in\mathbb{R}, and for u ≤ − 3 / 2 u\leq-3/2

 | ∑ n < N Λ ⁡ ( n) ​ ( 1 − n N) u ≪ N − u ​ log ⁡ N ​ ∑ n < N n u ≪ N | u | ​ log ⁡ N. \sum_{n<N}\Lambda(n)\big(1-\frac{n}{N}\big)^{u}\ll N^{-u}\log N\sum_{n<N}n^{u}\ll N^{|u|}\log N. |  |

Proposition 2 now follows from the above bounds, thanks to ( 2.2). ∎

## 3. Proof of the theorem

3.1. The first shift. Our point of departure is ( 1.9) where we shift the s s -integration to the line σ = − 1 / 2 \sigma=-1/2. We recall ( 1.10) and ( 1.11), thus getting

 | G k ​ ( N) = 1 2 ​ π ​ i ∫ ( 2) − ζ ′ ζ ( w) Γ ⁡ ( w) Γ ⁡ ( w + k + 2) N w + 1 w ⋅ − 1 2 ​ π ​ i ∫ ( 2) − ζ ′ ζ ( w) Γ ( w) Z N ( w + k) N w w ⋅ − ζ ′ ζ ( 0) 1 2 ​ π ​ i ∫ ( 2) − ζ ′ ζ ( w) Γ ⁡ ( w) Γ ⁡ ( w + k + 1) N w w ⋅ + 1 2 ​ π ​ i ∫ ( 2) − ζ ′ ζ ( w) Γ ( w) T N ( w + k) N w w ⋅ = N ​ Γ ​ ( N, k + 1) − Z ⁡ ( N, k) − ζ ′ ζ ​ ( 0) ​ Γ ​ ( N, k) + T ⁡ ( N, k), \begin{split}G_{k}(N)&=\frac{1}{2\pi i}\int_{(2)}-\frac{\zeta^{\prime}}{\zeta}(w)\frac{\Gamma(w)}{\Gamma(w+k+2)}N^{w+1}\,\d{w}-\frac{1}{2\pi i}\int_{(2)}-\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w)Z_{N}(w+k)N^{w}\,\d{w}\\ &\hskip 28.45274pt-\frac{\zeta^{\prime}}{\zeta}(0)\frac{1}{2\pi i}\int_{(2)}-\frac{\zeta^{\prime}}{\zeta}(w)\frac{\Gamma(w)}{\Gamma(w+k+1)}N^{w}\,\d{w}\\ \ &\hskip 28.45274pt+\frac{1}{2\pi i}\int_{(2)}-\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w)T_{N}(w+k)N^{w}\,\d{w}\\ &=N\Gamma(N,k+1)-Z(N,k)-\frac{\zeta^{\prime}}{\zeta}(0)\Gamma(N,k)+T(N,k),\end{split} |  | (3.1) |

say. All integrals here are absolutely convergent for k > 0 k>0, thanks to Stirling’s formula and the bounds ( 2.2) and ( 2.3).

3.2. Shifting to − ∞ -\infty. Next, we want to shift to − ∞ -\infty all w w -integrations in ( 3.1). To this end, we first need to get suitable bounds for the integrands. We may clearly assume that | w | |w| is sufficiently large and | w + m | ≥ 1 / 4 |w+m|\geq 1/4 for every integer m ≥ 1 m\geq 1. Recalling ( 2.4), ( 2.5) and the reflection formula for the Γ \Gamma function, we have

 | ζ ′ ζ ​ ( w) ≪ | g ′ g ​ ( w) | + 1 ≪ | Γ ′ Γ ​ ( 1 − w) | + | sin ⁡ ( π ​ w / 2) cos ⁡ ( π ​ w / 2) | + | cos ⁡ ( π ​ w) sin ⁡ ( π ​ w) | + 1 ≪ log ⁡ | w |, \frac{\zeta^{\prime}}{\zeta}(w)\ll\left|\frac{g^{\prime}}{g}(w)\right|+1\ll\left|\frac{\Gamma^{\prime}}{\Gamma}(1-w)\right|+\left|\frac{\sin(\pi w/2)}{\cos(\pi w/2)}\right|+\left|\frac{\cos(\pi w)}{\sin(\pi w)}\right|+1\ll\log|w|, |  | (3.2) |

thanks to (6) in Chapter 10 of [2] and the bounds O ⁡ ( 1) O(1) for the two trigonometric terms. In view of the shape of the bounds ( 2.2) and ( 2.3), we apply again the reflection formula and then Stirling’s formula to bound Γ ⁡ ( w) / Γ ⁡ ( w + k + 1) \Gamma(w)/\Gamma(w+k+1) to conclude that

 | Γ ⁡ ( w) Γ ⁡ ( w + k + 1) ≪ | w | − ( k + 1). \frac{\Gamma(w)}{\Gamma(w+k+1)}\ll|w|^{-(k+1)}. |  | (3.3) |

Since the computations involved in the shift to − ∞ -\infty of the integrals in ( 3.1) are now quite standard, we only give a sketch of the argument. We treat explicitly only the integral Z ⁡ ( N, k) Z(N,k), since T ⁡ ( N, k) T(N,k) is similar but easier and Γ ⁡ ( N, k) \Gamma(N,k) gives rise to a classical weighted explicit formula. We first restrict the integration on the line u = − 1 / 2 u=-1/2 to the segment with | v | ≤ V |v|\leq V and then shift such a segment to u = − ( U + 1 / 2) u=-(U+1/2), where 0 < U < V 0<U<V are sufficiently large and U ∈ ℕ U\in\mathbb{N}. We denote by Z U, V hor ​ ( N, k) Z_{U,V}^{\text{hor}}(N,k) the integral over the two horizontal sides [− ( U + 1 / 2) ± i V, − 1 / 2 ± i V] [-(U+1/2)\pm iV,-1/2\pm iV] and by Z U, V vert ​ ( N, k) Z_{U,V}^{\text{vert}}(N,k) the one over the vertical side [− ( U + 1 / 2) − i ​ V, − ( U + 1 / 2) + i ​ V] [-(U+1/2)-iV,-(U+1/2)+iV]. Thanks to ( 2.3) with δ = 1 / 4 \delta=1/4, ( 3.2) and ( 3.3) we have

 | Z U, V hor ​ ( N, k) ≪ N c ​ U ​ log 2 ⁡ V V k + 1 and Z U, V vert ​ ( N, k) ≪ N c ​ log 2 ⁡ U U k Z_{U,V}^{\text{hor}}(N,k)\ll N^{c}U\frac{\log^{2}V}{V^{k+1}}\quad\text{and}\quad Z_{U,V}^{\text{vert}}(N,k)\ll N^{c}\frac{\log^{2}U}{U^{k}} |  |

for some c > 0 c>0, and hence

 | lim U → + ∞ ( lim V → + ∞ Z U, V hor ​ ( N, k) + Z U, V vert ​ ( N, k)) = 0. \lim_{U\to+\infty}\big(\lim_{V\to+\infty}Z_{U,V}^{\text{hor}}(N,k)+Z_{U,V}^{\text{vert}}(N,k)\big)=0. |  |

Therefore, Z ⁡ ( N, k) Z(N,k) equals the sum of the residues − ζ ′ ζ ​ ( w) ​ Γ ​ ( w) ​ Z N ​ ( w + k) ​ N w -\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w)Z_{N}(w+k)N^{w}. Clearly, this argument also applies to the other three integrals in ( 3.1).

3.3. Computing the residues. For each of the four integrals in ( 3.1) we have to compute the following residues:

(a) at the simple pole of − ζ ′ / ζ ( w) -\zeta^{\prime}/\zeta(w) at w = 1 w=1;

(b) at the simple poles of − ζ ′ / ζ ( w) -\zeta^{\prime}/\zeta(w) at w = ρ w=\rho, ρ \rho non-trivial zero;

(c) at the simple poles of Γ ⁡ ( w) \Gamma(w) at w = 0 w=0 and w = − ν w=-\nu, ν ≥ 1 \nu\geq 1 and 2 ∤ ν 2\nmid\nu;

(d) at the double poles of − ζ ′ ζ ​ ( w) ​ Γ ​ ( w) -\frac{\zeta^{\prime}}{\zeta}(w)\Gamma(w) at w = − ν w=-\nu, ν ≥ 1 \nu\geq 1 and 2 | ν 2|\nu.

The residues of type (a) produce the terms

 | N 2 Γ ⁡ ( k + 3) − N ​ Z N ​ ( k + 1) − ζ ′ ζ ​ ( 0) ​ N Γ ⁡ ( k + 2) + N ​ T N ​ ( k + 1), \frac{N^{2}}{\Gamma(k+3)}-NZ_{N}(k+1)-\frac{\zeta^{\prime}}{\zeta}(0)\frac{N}{\Gamma(k+2)}+NT_{N}(k+1), |  | (3.4) |

while the type (b) residues give rise to the sums

 | − ∑ ρ Γ ⁡ ( ρ) Γ ⁡ ( ρ + k + 2) N ρ + 1 + ∑ ρ Γ ( ρ) Z N ( ρ + k) N ρ + ζ ′ ζ ( 0) ∑ ρ Γ ⁡ ( ρ) Γ ⁡ ( ρ + k + 1) N ρ − ∑ ρ Γ ( ρ) T N ( ρ + k) N ρ. \begin{split}&-\sum_{\rho}\frac{\Gamma(\rho)}{\Gamma(\rho+k+2)}N^{\rho+1}+\sum_{\rho}\Gamma(\rho)Z_{N}(\rho+k)N^{\rho}\\ &+\frac{\zeta^{\prime}}{\zeta}(0)\sum_{\rho}\frac{\Gamma(\rho)}{\Gamma(\rho+k+1)}N^{\rho}-\sum_{\rho}\Gamma(\rho)T_{N}(\rho+k)N^{\rho}.\end{split} |  | (3.5) |

By Stirling’s formula, the sums in ( 3.5) are absolutely convergent thanks to ( 2.2) and ( 2.3), since k > 0 k>0. The residues of type (c) produce the terms

 | − ζ ′ ζ ​ ( 0) ​ N Γ ⁡ ( k + 2) + ζ ′ ζ ​ ( 0) ​ Z N ​ ( k) + ζ ′ ζ ​ ( 0) 2 ​ 1 Γ ⁡ ( k + 1) − ζ ′ ζ ​ ( 0) ​ T N ​ ( k) -\frac{\zeta^{\prime}}{\zeta}(0)\frac{N}{\Gamma(k+2)}+\frac{\zeta^{\prime}}{\zeta}(0)Z_{N}(k)+\frac{\zeta^{\prime}}{\zeta}(0)^{2}\frac{1}{\Gamma(k+1)}-\frac{\zeta^{\prime}}{\zeta}(0)T_{N}(k) |  | (3.6) |

plus the sums

 | ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ​ ( − ν) ​ N − ν + 1 ν! ​ Γ ​ ( − ν + k + 2) − ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ​ ( − ν) ​ Z N ​ ( − ν + k) ​ N − ν ν! − ζ ′ ζ ( 0) ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ( − ν) N − ν ν! ​ Γ ​ ( − ν + k + 1) + ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ( − ν) T N ( − ν + k) N − ν ν!. \begin{split}&\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)\frac{N^{-\nu+1}}{\nu!\Gamma(-\nu+k+2)}-\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)Z_{N}(-\nu+k)\frac{N^{-\nu}}{\nu!}\\ &-\frac{\zeta^{\prime}}{\zeta}(0)\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)\frac{N^{-\nu}}{\nu!\Gamma(-\nu+k+1)}+\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)T_{N}(-\nu+k)\frac{N^{-\nu}}{\nu!}.\end{split} |  | (3.7) |

Again, the sums in ( 3.7) are absolutely convergent for k > 0 k>0, thanks to ( 2.2), ( 2.3), ( 3.2) and Stirling’s formula.

A bit more care is required for residues of type (d). For even integers ν ≥ 1 \nu\geq 1, let a ν a_{\nu} and b ν b_{\nu} be defined by the following Laurent expansions at w = − ν w=-\nu via

 | − ζ ′ ζ ​ ( w) = 1 w + ν + a ν + … Γ ⁡ ( w) = 1 ν! ​ ( w + ν) + b ν ν! + …, -\frac{\zeta^{\prime}}{\zeta}(w)=\frac{1}{w+\nu}+a_{\nu}+\dots\qquad\Gamma(w)=\frac{1}{\nu!(w+\nu)}+\frac{b_{\nu}}{\nu!}+\dots, |  | (3.8) |

and let

 | A ν ​ ( N) = { a ν + b ν + log ⁡ N if 2 | ν − ζ ′ ζ ​ ( − ν) if 2 ∤ ν. A_{\nu}(N)=\begin{cases}a_{\nu}+b_{\nu}+\log N&\text{if $2|\nu$}\\ -\frac{\zeta^{\prime}}{\zeta}(-\nu)&\text{if $2\nmid\nu$.}\end{cases} |  | (3.9) |

Moreover, denoting by F ⁡ ( w) F(w) any of the four functions

 | N w + 1 Γ ⁡ ( w + k + 2), Z N ​ ( w + k) ​ N w, N w Γ ⁡ ( w + k + 1), T N ​ ( w + k) ​ N w, \frac{N^{w+1}}{\Gamma(w+k+2)},\quad Z_{N}(w+k)N^{w},\quad\frac{N^{w}}{\Gamma(w+k+1)},\quad T_{N}(w+k)N^{w}, |  |

in view of ( 3.8) the residues of type (d) at w = − ν w=-\nu are of the form

 | a ν + b ν ν! ​ F ​ ( − ν) + 1 ν! ​ F ′ ​ ( − ν). \frac{a_{\nu}+b_{\nu}}{\nu!}F(-\nu)+\frac{1}{\nu!}F^{\prime}(-\nu). |  |

Hence by ( 3.9) the contribution of the residues of type (d) is

 | ∑ ν ≥ 1 2 | ν A ν ​ ( N) ν! ​ N − ν + 1 Γ ⁡ ( − ν + k + 2) − ∑ ν ≥ 1 2 | ν Γ ′ ​ ( − ν + k + 2) Γ 2 ​ ( − ν + k + 2) ​ N − ν + 1 ν! − ∑ ν ≥ 1 2 | ν A ν ​ ( N) ν! Z N ( k − ν) N − ν − ∑ ν ≥ 1 2 | ν Z ′ N ( k − ν) N − ν ν! − ζ ′ ζ ( 0) ∑ ν ≥ 1 2 | ν A ν ​ ( N) ν! N − ν Γ ⁡ ( − ν + k + 1) + ζ ′ ζ ( 0) ∑ ν ≥ 1 2 | ν Γ ′ ​ ( − ν + k + 1) Γ 2 ​ ( − ν + k + 1) N − ν ν! + ∑ ν ≥ 1 2 | ν A ν ​ ( N) ν! T N ( k − ν) N − ν + ∑ ν ≥ 1 2 | ν T ′ N ( k − ν) N − ν ν!. \begin{split}&\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\frac{A_{\nu}(N)}{\nu!}\frac{N^{-\nu+1}}{\Gamma(-\nu+k+2)}-\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\frac{\Gamma^{\prime}(-\nu+k+2)}{\Gamma^{2}(-\nu+k+2)}\frac{N^{-\nu+1}}{\nu!}\\ &\hskip 14.22636pt-\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\frac{A_{\nu}(N)}{\nu!}Z_{N}(k-\nu)N^{-\nu}-\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}Z^{\prime}_{N}(k-\nu)\frac{N^{-\nu}}{\nu!}\\ &\hskip 14.22636pt-\frac{\zeta^{\prime}}{\zeta}(0)\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\frac{A_{\nu}(N)}{\nu!}\frac{N^{-\nu}}{\Gamma(-\nu+k+1)}+\frac{\zeta^{\prime}}{\zeta}(0)\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\frac{\Gamma^{\prime}(-\nu+k+1)}{\Gamma^{2}(-\nu+k+1)}\frac{N^{-\nu}}{\nu!}\\ &\hskip 14.22636pt+\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\frac{A_{\nu}(N)}{\nu!}T_{N}(k-\nu)N^{-\nu}+\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}T^{\prime}_{N}(k-\nu)\frac{N^{-\nu}}{\nu!}.\end{split} |  | (3.10) |

The absolute convergence of the second and sixth sum in ( 3.10) follows by computations similar to those leading to ( 3.2) and ( 3.3), giving in particular that for a > 0 a>0

 | 1 ν! ​ Γ ​ ( − ν + a) ≪ 1 ν a. \frac{1}{\nu!\Gamma(-\nu+a)}\ll\frac{1}{\nu^{a}}. |  | (3.11) |

Hence now we concentrate on the remaining six sums. However, it is already clear from ( 3.1), ( 3.4)-( 3.6) after a simple a rearrangement of terms, ( 3.7) and ( 3.10) that the explicit formula in the theorem holds as a formal identity.

3.4. The final estimates. We need the following lemma.

Lemma 3.1. For N ≥ 4 N\geq 4 and ν ≥ 1 \nu\geq 1 we have

 | A ν ​ ( N) ≪ log ⁡ ( ν ​ N). A_{\nu}(N)\ll\log(\nu N). |  |

Proof. The lemma follows at once from ( 3.2) and ( 3.9) if 2 ∤ ν 2\nmid\nu. If 2 | ν 2|\nu, then by ( 3.8) we have

 | a ν = − 1 2 ​ π ​ i ∫ | w + ν | = 1 ( ζ ′ ζ ( w) + 1 w + ν) w ⋅ ≪ log ( ν + 1) a_{\nu}=-\frac{1}{2\pi i}\int_{|w+\nu|=1}\big(\frac{\zeta^{\prime}}{\zeta}(w)+\frac{1}{w+\nu}\big)\d{w}\ll\log(\nu+1) |  |

thanks to ( 3.2), and

 | b ν = ν! ​ lim w → − ν ( Γ ⁡ ( w) − 1 ν! ​ ( w + ν)) = ν! ​ lim w → − ν ( Γ ⁡ ( w) ​ ( w + ν) − 1 / ν! w + ν) = ν! ​ lim w → − ν ( Γ ⁡ ( w) + ( w + ν) ​ Γ ′ ​ ( w)) = ν! ​ lim w → − ν ( ( w + ν) ​ Γ ​ ( w)) ​ ( 1 w + ν + Γ ′ Γ ​ ( w)) = lim w → − ν ( Γ ′ Γ ​ ( w) + 1 w + ν), \begin{split}b_{\nu}&=\nu!\lim_{w\to-\nu}\big(\Gamma(w)-\frac{1}{\nu!(w+\nu)}\big)=\nu!\lim_{w\to-\nu}\Big(\frac{\Gamma(w)(w+\nu)-1/\nu!}{w+\nu}\Big)\\ &=\nu!\lim_{w\to-\nu}\big(\Gamma(w)+(w+\nu)\Gamma^{\prime}(w)\big)=\nu!\lim_{w\to-\nu}\big((w+\nu)\Gamma(w)\big)\Big(\frac{1}{w+\nu}+\frac{\Gamma^{\prime}}{\Gamma}(w)\Big)\\ &=\lim_{w\to-\nu}\Big(\frac{\Gamma^{\prime}}{\Gamma}(w)+\frac{1}{w+\nu}\Big),\end{split} |  |

since 2 | ν 2|\nu. Taking the logarithmic derivative of the Hadamard product of 1 / Γ ⁡ ( w) 1/\Gamma(w) as in ( 2.9) we see that

 | Γ ′ Γ ​ ( w) = − γ − 1 w + ∑ n = 1 ∞ ( 1 n − 1 w + n), \frac{\Gamma^{\prime}}{\Gamma}(w)=-\gamma-\frac{1}{w}+\sum_{n=1}^{\infty}\Big(\frac{1}{n}-\frac{1}{w+n}\Big), |  |

hence

 | b ν = − γ + 2 ν + ∑ n ≠ ν ( 1 n − 1 n − ν) ≪ log ⁡ ( ν + 1). b_{\nu}=-\gamma+\frac{2}{\nu}+\sum_{n\neq\nu}\Big(\frac{1}{n}-\frac{1}{n-\nu}\Big)\ll\log(\nu+1). |  |

The lemma now follows thanks to ( 3.9). ∎

Now we prove the absolute convergence of the above mentioned six sums in ( 3.10). Thanks to Lemma 3.1, the absolute convergence of the fifth sum in ( 3.10) follows from ( 3.11). Next we deal with the two sums involving the function Z N ​ ( w) Z_{N}(w), those involving T N ​ ( w) T_{N}(w) being similar and easier; we may clearly assume that ν \nu is sufficiently large. If k k is not an integer we may apply directly the second bound for Z N ​ ( k − ν) Z_{N}(k-\nu) in ( 2.3), choosing any 0 < δ < k 0<\delta<k. If k k is an integer, by the maximum principle we have that

 | | Z N ​ ( k − ν) | ≤ max | w + k − ν | = δ ⁡ | Z N ​ ( w) | |Z_{N}(k-\nu)|\leq\max_{|w+k-\nu|=\delta}|Z_{N}(w)| |  |

with a small 0 < δ < k 0<\delta<k, and then we apply again the second bound in ( 2.3). Hence in both cases we have

 | Z N ​ ( k − ν) ≪ N ν − k + δ ​ log ⁡ N + 2 ν − k + δ ​ log ⁡ ν | Γ ⁡ ( − ν + k − δ + 1) |. Z_{N}(k-\nu)\ll\frac{N^{\nu-k+\delta}\log N+2^{\nu-k+\delta}\log\nu}{|\Gamma(-\nu+k-\delta+1)|}. |  | (3.12) |

The bound for Z N ′ ​ ( k − ν) Z^{\prime}_{N}(k-\nu) is obtained in a similar way, using of Cauchy’s formula

 | Z N ′ ​ ( k − ν) = 1 2 ​ π ​ i ​ ∫ | w + ν − k | = δ Z N ​ ( w) ( w + ν − k) 2 ​ w ⋅ Z^{\prime}_{N}(k-\nu)=\frac{1}{2\pi i}\int_{|w+\nu-k|=\delta}\frac{Z_{N}(w)}{(w+\nu-k)^{2}}\d{w} |  |

and hence getting that

 | Z N ′ ​ ( k − ν) ≪ N ν − k + δ ​ log ⁡ N + 2 ν − k + δ ​ log ⁡ ν | Γ ⁡ ( − ν + k − δ + 1) |. Z^{\prime}_{N}(k-\nu)\ll\frac{N^{\nu-k+\delta}\log N+2^{\nu-k+\delta}\log\nu}{|\Gamma(-\nu+k-\delta+1)|}. |  | (3.13) |

with any 0 < δ < k 0<\delta<k. The absolute convergence of the third and fourth sum in ( 3.10) follows now from Lemma 3.1, ( 3.11), ( 3.12) and ( 3.13), since 0 < δ < k 0<\delta<k. The theorem is therefore proved.

Finally, from ( 1.12)-( 1.14), ( 3.7) and ( 3.10) we have that

 | Σ Γ ​ ( N, k) = ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ​ ( − ν) ​ N − ν ν! ​ Γ ​ ( − ν + k + 1) + ∑ ν ≥ 1 2 | ν ( A ν ​ ( N) Γ ⁡ ( − ν + k + 1) − Γ ′ ​ ( − ν + k + 2) Γ 2 ​ ( − ν + k + 1)) ​ N − ν ν!, \Sigma_{\Gamma}(N,k)=\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)\frac{N^{-\nu}}{\nu!\Gamma(-\nu+k+1)}+\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\Big(\frac{A_{\nu}(N)}{\Gamma(-\nu+k+1)}-\frac{\Gamma^{\prime}(-\nu+k+2)}{\Gamma^{2}(-\nu+k+1)}\Big)\frac{N^{-\nu}}{\nu!}, |  | (3.14) |

 | Σ Z ​ ( N, k) = ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ​ ( − ν) ​ Z N ​ ( − ν + k) ​ N − ν ν! + ∑ ν ≥ 1 2 | ν ( A ν ​ ( N) ​ Z N ​ ( k − ν) + Z N ′ ​ ( k − ν)) ​ N − ν ν!, \Sigma_{Z}(N,k)=\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)Z_{N}(-\nu+k)\frac{N^{-\nu}}{\nu!}+\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\Big(A_{\nu}(N)Z_{N}(k-\nu)+Z^{\prime}_{N}(k-\nu)\Big)\frac{N^{-\nu}}{\nu!}, |  | (3.15) |

 | Σ T ​ ( N, k) = ∑ ν ≥ 1 2 ∤ ν ζ ′ ζ ​ ( − ν) ​ T N ​ ( − ν + k) ​ N − ν ν! + ∑ ν ≥ 1 2 | ν ( A ν ​ ( N) ​ T N ​ ( k − ν) + T N ′ ​ ( k − ν)) ​ N − ν ν!; \Sigma_{T}(N,k)=\sum_{\begin{subarray}{c}\nu\geq 1\\ 2\nmid\nu\end{subarray}}\frac{\zeta^{\prime}}{\zeta}(-\nu)T_{N}(-\nu+k)\frac{N^{-\nu}}{\nu!}+\sum_{\begin{subarray}{c}\nu\geq 1\\ 2|\nu\end{subarray}}\Big(A_{\nu}(N)T_{N}(k-\nu)+T^{\prime}_{N}(k-\nu)\Big)\frac{N^{-\nu}}{\nu!}; |  | (3.16) |

moreover, we denote by Σ Γ M ​ ( N, k) \Sigma_{\Gamma}^{M}(N,k), Σ Z M ​ ( N, k) \Sigma_{Z}^{M}(N,k) and Σ T M ​ ( N, k) \Sigma_{T}^{M}(N,k) the tail of such sums, from ν = M + 1 \nu=M+1 to ∞ \infty. Hence from ( 3.2), ( 3.11), Lemma 3.1, ( 3.12) and ( 3.13), and the analogues of ( 3.12) and ( 3.13) for T N ​ ( k − ν) T_{N}(k-\nu) where the term N ν − k + δ ​ log ⁡ N N^{\nu-k+\delta}\log N is missing, it follows that cutting the above sums at ν = M ≥ 2 \nu=M\geq 2 produces the errors

 | Σ Γ M ​ ( N, k) ≪ N − ( M + 1) ​ log ⁡ ( N ​ M) M k, Σ Z M ​ ( N, k) ≪ δ N − k + δ ​ log 2 ⁡ ( N ​ M) M k − δ, Σ T M ​ ( N, k) ≪ δ ( N / 2) − ( M + 1) ​ log 2 ⁡ ( N ​ M) M k − δ, \begin{split}\Sigma_{\Gamma}^{M}(N,k)&\ll\frac{N^{-(M+1)}\log(NM)}{M^{k}},\\ \Sigma_{Z}^{M}(N,k)&\ll_{\delta}\frac{N^{-k+\delta}\log^{2}(NM)}{M^{k-\delta}},\\ \Sigma_{T}^{M}(N,k)&\ll_{\delta}\frac{(N/2)^{-(M+1)}\log^{2}(NM)}{M^{k-\delta}},\end{split} |  | (3.17) |

for every δ > 0 \delta>0. All the statements are now proved.

## References

- [1] G.Bhowmik, J.-C.Schlage-Puchta - Mean representation number of integers as the sum of primes - Nagoya Math. J. 200 (2010), 27–33.
- [2] H.Davenport - Multiplicative Number Theory - 2nd ed., Springer 1980.
- [3] A.Fujii - An additive problem of prime numbers. II - Proc. Japan Acad. Ser. A Math. Sci. 67 (1991), no. 7, 248–252.
- [4] D.A.Goldston, L.Yang - The average number of Goldbach representations - arXiv:1601.06902v1, 2016.
- [5] A.Languasco - Applications of some exponential sums on prime powers: a survey - Riv. Mat. Univ. Parma 7 (2016), 19–37.
- [6] A.Languasco, A.Zaccagnini - The number of Goldbach representations of an integer - Proc. Amer. Math. Soc. 140 (2012), 795–804.
- [7] A.Languasco, A.Zaccagnini - A Cesàro average of Goldbach numbers - Forum Math. 27 (2015), 1945–1960.
- [8] F.Oberhettinger - Tables of Mellin Transforms - Springer Verlag 1974.
- [9] R.Remmert - Classical Topics in Complex Function Theory - Springer 1998.

Jörg Brüdern, Mathematisches Institut, Bunsenstr. 3-5, 37073 Göttingen, Germany. e-mail: bruedern@uni-math.gwdg.de

Jerzy Kaczorowski, Faculty of Mathematics and Computer Science, A.Mickiewicz University, 61-614 Poznań, Poland and Institute of Mathematics of the Polish Academy of Sciences, 00-956 Warsaw, Poland. e-mail: kjerzy@amu.edu.pl

Alberto Perelli, Dipartimento di Matematica, Università di Genova, via Dodecaneso 35, 16146 Genova, Italy. e-mail: perelli@dima.unige.it


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
