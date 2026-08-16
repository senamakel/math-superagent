<!-- source: https://ar5iv.labs.arxiv.org/html/1709.06168 | converted from HTML -->

[1709.06168] The distribution of consecutive prime biases and sums of sawtooth random variables

# The distribution of consecutive prime biases and sums of sawtooth random variables Thanks: Robert Lemke Oliver was partially supported by NSF grant DMS-1601398. Kannan Soundararajan was partially supported by NSF grant DMS-1500237 and by a Simons Investigator grant from the Simons Foundation.

Robert J. Lemke Oliver Address: Department of Mathematics, Tufts University Email address: [robert.lemke_oliver@tufts.edu][1] and Kannan Soundararajan Address: Department of Mathematics, Stanford University Email address: [ksound@stanford.edu][2]

###### Abstract.

In recent work, we considered the frequencies of patterns of consecutive primes ( mod ​ q) \,\left(\text{mod }q\right) and numerically found biases toward certain patterns and against others. We made a conjecture explaining these biases, the dominant factor in which permits an easy description but fails to distinguish many patterns that have seemingly very different frequencies. There was a secondary factor in our conjecture accounting for this additional variation, but it was given only by a complicated expression whose distribution was not easily understood. Here, we study this term, which proves to be connected to both the Fourier transform of classical Dedekind sums and the error term in the asymptotic formula for the sum of ϕ ⁡ ( n) \phi(n).

## 1. Introduction

Let p n p_{n} denote the sequence of primes in ascending order. Given q ≥ 3 q\geq 3 and 𝐚 = ( a 1, …, a r) \mathbf{a}=(a_{1},\dots,a_{r}) satisfying ( a i, q) = 1 (a_{i},q)=1 for all 1 ≤ i ≤ r 1\leq i\leq r, in recent work [7] we studied biases in the occurrence of the pattern 𝐚 \mathbf{a} in strings of r r consecutive primes reduced ( mod ​ q) \,\left(\text{mod }q\right). Thus, we defined

 | π ⁡ ( x, q, 𝐚):= #⁡ { p n ≤ x: p n + i − 1 ≡ a i ​ ( mod ​ q) ​ for ​ 1 ≤ i ≤ r }, \pi(x;q,\mathbf{a}):=\#\{p_{n}\leq x:p_{n+i-1}\equiv a_{i}\,\left(\text{mod }q\right)\text{ for }1\leq i\leq r\}, |  |

and conjectured that

(1.1) |  | π ( x; q, 𝐚) = li ⁡ ( x) ϕ ​ ( q) r ( 1 + c 1 ( q; 𝐚) log ⁡ log ⁡ x log ⁡ x + c 2 ( q; 𝐚) 1 log ⁡ x + O ( ( log x) − 7 / 4)), \pi(x;q,\mathbf{a})=\frac{\mathrm{li}(x)}{\phi(q)^{r}}\Big(1+c_{1}(q;\mathbf{a})\frac{\log\log x}{\log x}+c_{2}(q;\mathbf{a})\frac{1}{\log x}+O((\log x)^{-7/4})\Big), |  |

where c 1 ​ ( q, 𝐚) c_{1}(q;\mathbf{a}) and c 2 ​ ( q, 𝐚) c_{2}(q;\mathbf{a}) are certain explicit constants. The term c 1 ​ ( q, 𝐚) c_{1}(q;\mathbf{a}) is easily described,

 | c 1 ​ ( q, 𝐚) = ϕ ⁡ ( q) 2 ​ ( r − 1 ϕ ⁡ ( q) − #⁡ { i ≤ r − 1: a i ≡ a i + 1 ​ ( mod ​ q) }), c_{1}(q;\mathbf{a})=\frac{\phi(q)}{2}\Big(\frac{r-1}{\phi(q)}-\#\{i\leq r-1:a_{i}\equiv a_{i+1}\,\left(\text{mod }q\right)\}\Big), |  |

and it acts as a bias against immediate repetitions in the pattern 𝐚 \mathbf{a}. The term c 2 ​ ( q, 𝐚) c_{2}(q;\mathbf{a}) is more complicated, and the goal of this paper is to understand its distribution. If r ≥ 3 r\geq 3 then

 | c 2 ​ ( q, 𝐚) = ∑ i = 1 r − 1 c 2 ​ ( q, ( a i, a i + 1)) + ϕ ⁡ ( q) 2 ​ ∑ j = 1 r − 2 1 j ​ ( r − 1 − j ϕ ⁡ ( q) − #⁡ { i: a i ≡ a i + j + 1 ​ ( mod ​ q) }), c_{2}(q;\mathbf{a})=\sum_{i=1}^{r-1}c_{2}(q;(a_{i},a_{i+1}))+\frac{\phi(q)}{2}\sum_{j=1}^{r-2}\frac{1}{j}\Big(\frac{r-1-j}{\phi(q)}-\#\{i:a_{i}\equiv a_{i+j+1}\,\left(\text{mod }q\right)\}\Big), |  |

so that it is sufficient to understand the case r = 2 r=2; that is, c 2 ​ ( q, ( a, b)) c_{2}(q;(a,b)) with ( a, q) = ( b, q) = 1 (a,q)=(b,q)=1.

For the sake of simplicity, we shall confine ourselves to the case when q q is prime. For any character χ ⁡ ( mod ​ q) \chi\,\left(\text{mod }q\right) we define

(1.2) |  | A q, χ = ∏ p ∤ q ( 1 − ( 1 − χ ⁡ ( p)) 2 ( p − 1) 2). A_{q,\chi}=\prod_{p\nmid q}\Big(1-\frac{(1-\chi(p))^{2}}{(p-1)^{2}}\Big). |  |

Then the quantity c 2 ​ ( q, ( a, b)) c_{2}(q;(a,b)) is given by

 | c 2 ​ ( q, ( a, a)) = q − 2 2 ​ log ⁡ ( q / 2 ​ π), c_{2}(q;(a,a))=\frac{q-2}{2}\log(q/2\pi), |  |

and when a ≢ b ⁡ ( mod ​ q) a\not\equiv b\,\left(\text{mod }q\right) by

(1.3) |  | c 2 ​ ( q, ( a, b)) = 1 2 ​ log ⁡ 2 ​ π q + q ϕ ⁡ ( q) ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) ( χ ¯ ​ ( b − a) + 1 ϕ ⁡ ( q) ​ ( χ ¯ ​ ( b) − χ ¯ ​ ( a))) ​ L ​ ( 0, χ) ​ L ​ ( 1, χ) ​ A q, χ. c_{2}(q;(a,b))=\frac{1}{2}\log\frac{2\pi}{q}+\frac{q}{\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\Big(\overline{\chi}(b-a)+\frac{1}{\phi(q)}(\overline{\chi}(b)-\overline{\chi}(a))\Big)L(0,\chi)L(1,\chi)A_{q,\chi}. |  |

The diagonal term c 2 ​ ( q, ( a, a)) c_{2}(q;(a,a)) is thus completely explicit, and of size q ​ log ⁡ q q\log q. Our work here shows that the off-diagonal terms c 2 ​ ( q, ( a, b)) c_{2}(q;(a,b)) can also be large; usually they are of size about q q, occasionally getting to size q ​ log ⁡ log ​ q q\log\log q (attaining both positive and negative values), which we believe is their maximal size.

Before stating our result, we make one more simplification. Define

(1.4) |  | C ⁡ ( k) = C ⁡ ( k, q) = 1 ϕ ⁡ ( q) ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ⁡ ( k) ¯ ​ L ​ ( 0, χ) ​ L ​ ( 1, χ) ​ A q, χ. C(k)=C(k;q)=\frac{1}{\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\overline{\chi(k)}L(0,\chi)L(1,\chi)A_{q,\chi}. |  |

Since A q, χ ≪ 1 A_{q,\chi}\ll 1, L ⁡ ( 1, χ) ≪ log ⁡ q L(1,\chi)\ll\log q, and (upon using the functional equation) L ⁡ ( 0, χ) ≪ q ​ log ⁡ q L(0,\chi)\ll\sqrt{q}\log q, from ( 1.3) it follows that for a ≢ b ⁡ ( mod ​ q) a\not\equiv b\,\left(\text{mod }q\right)

(1.5) |  | c 2 ​ ( q, ( a, b)) q = C ⁡ ( b − a) + O ⁡ ( ( log ⁡ q) 2 q). \frac{c_{2}(q;(a,b))}{q}=C(b-a)+O\Big(\frac{(\log q)^{2}}{\sqrt{q}}\Big). |  |

Thus for large q q it is enough to understand the distribution of C ⁡ ( k) C(k) as k k varies over all non-zero residue classes ( mod ​ q) \,\left(\text{mod }q\right). Since L ⁡ ( 0, χ) = 0 L(0,\chi)=0 for even characters χ \chi, in ( 1.4) only odd characters χ \chi make a contribution, and therefore C ⁡ ( k) = − C ⁡ ( − k) C(k)=-C(-k) is an odd function of k k.

###### Theorem 1.1.

(1) As q → ∞ q\to\infty the distribution of C ⁡ ( k) C(k) tends to a continuous probability distribution, symmetric around 0 0. Precisely, there is a continuous function Φ C \Phi_{C} with Φ C ​ ( − x) + Φ C ​ ( x) = 1 \Phi_{C}(-x)+\Phi_{C}(x)=1 such that uniformly for all x ∈ [− X, X] x\in[-X,X] one has

 | 1 q ​ #​ { k ⁡ ( mod ​ q): C ⁡ ( k) ≤ e γ 2 ​ x } = Φ C ​ ( x) + o ⁡ ( 1). \frac{1}{q}\#\{k\,\left(\text{mod }q\right):\ C(k)\leq\tfrac{e^{\gamma}}{2}x\}=\Phi_{C}(x)+o(1). |  |

(2) Uniformly for all e ≤ x ≤ ( 1 2 − ϵ) ​ log ⁡ log ⁡ q e\leq x\leq(\frac{1}{2}-\epsilon)\log\log q one has

 | exp ( − A 1 e x / x) ≥ 1 q #{ k ( mod q): C ( k) ≥ e γ 2 x } ≥ exp ( − A 2 e x log x) \exp(-A_{1}e^{x}/x)\,\,\,\geq\,\,\,\frac{1}{q}\#\{k\,\left(\text{mod }q\right):\ C(k)\geq\tfrac{e^{\gamma}}{2}x\}\,\,\,\geq\,\,\,\exp(-A_{2}e^{x}\log x) |  |

for some positive constants A 1 A_{1} and A 2 A_{2}.

(3) For all large q q, there exists k ⁡ ( mod ​ q) k\,\left(\text{mod }q\right) with

 | − C ⁡ ( − k) = C ⁡ ( k) ≥ ( e γ 4 − ϵ) ​ log ⁡ log ⁡ q. -C(-k)=C(k)\geq\Big(\frac{e^{\gamma}}{4}-\epsilon\Big)\log\log q. |  |

(4) For all k ⁡ ( mod ​ q) k\,\left(\text{mod }q\right) we have

 | C ⁡ ( k) ≪ ( log ⁡ q) 2 3 ​ ( log ⁡ log ⁡ q) 2. C(k)\ll(\log q)^{\frac{2}{3}}(\log\log q)^{2}. |  |

(5) The values C ⁡ ( k) C(k) have an “almost periodic” structure. Precisely, suppose 1 ≤ m ≤ q / 4 1\leq m\leq q/4 is a multiple of every natural number below B ≥ 2 B\geq 2. Then

 | 1 q ​ ∑ k ⁡ ( mod ​ q) | C ⁡ ( k) − C ⁡ ( k + m) | 2 ≪ 1 B 1 − ϵ + m q ​ log ⁡ B. \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}|C(k)-C(k+m)|^{2}\ll\frac{1}{B^{1-\epsilon}}+\frac{m}{q}\log B. |  |

We make a few comments concerning Theorem 1.1 before proceeding to related results. In part 1, we believe that the distribution for C ⁡ ( k) C(k) has a density, which is to say that Φ C \Phi_{C} is in fact differentiable. Our proof falls just a little short of establishing this. In part 2, there is a gap between the upper and lower bounds for the tail frequencies. With a little more care, we can improve the lower bound there to exp ⁡ ( − A 3 ​ e x) \exp(-A_{3}e^{x}) for a suitable positive constant A 3 A_{3}, but there still remains a gap between the two bounds. The distribution of C ⁡ ( k) C(k), and especially the double exponential decay seen in part 2, are reminiscent of the distribution of values of L ⁡ ( 1, χ d) L(1,\chi_{d}) (see [4]). Motivated by this analogy, or by extrapolating the lower bounds in part 2, we believe that in part 3 there should exist values of C ⁡ ( k) C(k) as large as ( e γ 2 − ϵ) ​ log ⁡ log ​ q (\frac{e^{\gamma}}{2}-\epsilon)\log\log q. We also conjecture that ( e γ 2 + ϵ) ​ log ⁡ log ​ q (\frac{e^{\gamma}}{2}+\epsilon)\log\log q should be the largest possible value of C ⁡ ( k) C(k), which would be a substantial strengthening of part 4. Finally, in addition to the almost periodic structure given in part 5 (where k k varies), there should be an almost periodic structure as q q varies. That is, if q 1 q_{1} and q 2 q_{2} are two large random primes with q 1 − q 2 q_{1}-q_{2} being a multiple of the numbers below B B, then C ⁡ ( k, q 1) C(k;q_{1}) and C ⁡ ( k, q 2) C(k;q_{2}) will be close to each other (on average over k k). We hope that an interested reader will embrace some of these remaining problems.

While the quantity C ⁡ ( k) C(k) is the main focus of this paper, closely related objects arise in two other seemingly unrelated contexts. The first of these concerns Dedekind sums. Let ψ ⁡ ( x) \psi(x) denote the sawtooth function defined by

 | ψ ⁡ ( x) = { { x } − 1 / 2 if ​ x ∉ 𝐙, 0 if ​ x ∈ 𝐙, \psi(x)=\begin{cases}\{x\}-1/2&\text{ if }x\not\in\mathbf{Z},\\ 0&\text{ if }x\in\mathbf{Z},\end{cases} |  |

which is an odd function, periodic with period 1 1. If q q is prime and a a is a reduced residue ( mod ​ q) \,\left(\text{mod }q\right), then the Dedekind sum s q ​ ( a) s_{q}(a) is defined by

(1.6) |  | s q ​ ( a):= ∑ x ⁡ ( mod ​ q) ψ ⁡ ( x q) ​ ψ ​ ( a ​ x q). s_{q}(a):=\sum_{x\,\left(\text{mod }q\right)}\psi\Big(\frac{x}{q}\Big)\psi\Big(\frac{ax}{q}\Big). |  |

The Dedekind sum arises naturally in number theory when studying the modular transformation properties of the Dedekind η \eta -function, but it also appears in other contexts and satisfies many interesting properties [1, 11]. We study here the discrete Fourier transform of the Dedekind sum s q ​ ( a) s_{q}(a). Thus for a prime q q and residue class t ⁡ ( mod ​ q) t\,\left(\text{mod }q\right) we define

(1.7) |  | s ^ q ​ ( t):= 1 q ​ ∑ a ⁡ ( mod ​ q) s q ​ ( a) ​ e ​ ( a ​ t / q), \widehat{s}_{q}(t):=\frac{1}{q}\sum_{a\,\left(\text{mod }q\right)}s_{q}(a)e(at/q), |  |

where e ⁡ ( z) = e 2 ​ π ​ i ​ z e(z)=e^{2\pi iz} throughout. In Lemma 2.1 we shall see that

 | s ^ q ​ ( t) = − 1 π ​ i ​ ϕ ​ ( q) ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ¯ ​ ( t) ​ L ​ ( 0, χ) ​ L ​ ( 1, χ), \widehat{s}_{q}(t)=\frac{-1}{\pi i\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\bar{\chi}(t)L(0,\chi)L(1,\chi), |  |

so that s ^ q ​ ( t) \widehat{s}_{q}(t) is indeed a simpler version of C ⁡ ( k) C(k). An alternative useful expression is

(1.8) |  | s ^ q ​ ( t) = 1 π ​ i ​ ∑ n = 1 ( n, q) = 1 ∞ ψ ⁡ ( t ​ n ¯ / q) n, \widehat{s}_{q}(t)=\frac{1}{\pi i}\sum_{\begin{subarray}{c}n=1\\ (n,q)=1\end{subarray}}^{\infty}\frac{\psi(t\overline{n}/q)}{n}, |  |

where n ¯ \overline{n} denotes the multiplicative inverse of the reduced residue class n ⁡ ( mod ​ q) n\,\left(\text{mod }q\right) and the sum converges since the partial sums ∑ n ≤ x, ( n, q) = 1 ψ ⁡ ( t ​ n ¯ / q) \sum_{n\leq x,(n,q)=1}\psi(t\overline{n}/q) are bounded.

###### Theorem 1.2.

(1) As q → ∞ q\to\infty the distribution of π ​ i ​ s ^ q ​ ( t) \pi i\widehat{s}_{q}(t) tends to a continuous probability distribution, symmetric around 0 0. Precisely, there is a continuous function Φ s \Phi_{s} with Φ s ​ ( − x) + Φ s ​ ( x) = 1 \Phi_{s}(-x)+\Phi_{s}(x)=1 such that uniformly for all x ∈ [− X, X] x\in[-X,X] one has

 | 1 q ​ #​ { t ⁡ ( mod ​ q): π ​ i ​ s ^ q ​ ( t) ≤ e γ 2 ​ x } = Φ s ​ ( x) + o ⁡ ( 1). \frac{1}{q}\#\{t\,\left(\text{mod }q\right):\ \pi i\widehat{s}_{q}(t)\leq\tfrac{e^{\gamma}}{2}x\}=\Phi_{s}(x)+o(1). |  |

(2) Uniformly for all e ≤ x ≤ ( 1 2 − ϵ) ​ log ⁡ log ⁡ q e\leq x\leq(\frac{1}{2}-\epsilon)\log\log q one has

 | exp ( − A 1 e x / x) ≥ 1 q #{ t ( mod q): π i s ^ q ( t) ≥ e γ 2 x } ≥ exp ( − A 2 e x log x) \exp(-A_{1}e^{x}/x)\,\,\,\geq\,\,\,\frac{1}{q}\#\{t\,\left(\text{mod }q\right):\ \pi i\widehat{s}_{q}(t)\geq\frac{e^{\gamma}}{2}x\}\,\,\,\geq\,\,\,\exp(-A_{2}e^{x}\log x) |  |

for some positive constants A 1 A_{1} and A 2 A_{2}.

(3) For all large q q, there exists t ⁡ ( mod ​ q) t\,\left(\text{mod }q\right) with

 | − π ​ i ​ s ^ q ​ ( − t) = π ​ i ​ s ^ q ​ ( t) ≥ ( e γ 4 − ϵ) ​ log ⁡ log ⁡ q. -\pi i\widehat{s}_{q}(-t)=\pi i\widehat{s}_{q}(t)\geq\Big(\frac{e^{\gamma}}{4}-\epsilon\Big)\log\log q. |  |

(4) For all t ⁡ ( mod ​ q) t\,\left(\text{mod }q\right) we have

 | s ^ q ​ ( t) ≪ ( log ⁡ q) 2 3 ​ ( log ⁡ log ⁡ q) 2. \widehat{s}_{q}(t)\ll(\log q)^{\frac{2}{3}}(\log\log q)^{2}. |  |

(5) The values s ^ q ​ ( t) \widehat{s}_{q}(t) have an “almost periodic” structure. Precisely, suppose 1 ≤ m ≤ q / 4 1\leq m\leq q/4 is a multiple of every natural number below B ≥ 2 B\geq 2. Then

 | 1 q ​ ∑ t ⁡ ( mod ​ q) | s ^ q ​ ( t) − s ^ q ​ ( k + m) | 2 ≪ 1 B 1 − ϵ + m q ​ log ⁡ B. \frac{1}{q}\sum_{t\,\left(\text{mod }q\right)}|\widehat{s}_{q}(t)-\widehat{s}_{q}(k+m)|^{2}\ll\frac{1}{B^{1-\epsilon}}+\frac{m}{q}\log B. |  |

Theorem 1.2 exactly parallels the results of Theorem 1.1, with the same deficiencies discussed there. The proofs of Theorems 1.1 and 1.2 are nearly identical, and so we give details only for Theorem 1.1.

Our third topic concerns the remainder term in the asymptotic for the mean value of Euler’s ϕ \phi -function. Define the quantity R ⁡ ( x) R(x) by the relation

 | ∑ n ≤ x ϕ ⁡ ( n) = 3 π 2 ​ x 2 + R ⁡ ( x). \sum_{n\leq x}\phi(n)=\frac{3}{\pi^{2}}x^{2}+R(x). |  |

Simple arguments show that R ⁡ ( x) ≪ x ​ log ⁡ x R(x)\ll x\log x, and Walfisz [12] established that R ⁡ ( x) ≪ x ​ ( log ⁡ x) 2 / 3 ​ ( log ⁡ log ⁡ x) 4 / 3 R(x)\ll x(\log x)^{2/3}(\log\log x)^{4/3}, which is presently the best known estimate. Montgomery [8] conjectured that R ⁡ ( x) ≪ x ​ log ⁡ log ​ x R(x)\ll x\log\log x and R ⁡ ( x) = Ω ± ​ ( x ​ log ⁡ log ⁡ x) R(x)=\Omega_{\pm}(x\log\log x), and he showed that R ⁡ ( x) = Ω ± ​ ( x ​ log ⁡ log ⁡ x) R(x)=\Omega_{\pm}(x\sqrt{\log\log x}). Key to Montgomery’s work is the expression

 | R ⁡ ( x) = ϕ ⁡ ( x) 2 − x ​ ∑ n ≤ x μ ⁡ ( n) ​ ψ ​ ( x / n) n + O ⁡ ( x ​ exp ⁡ ( − c ​ log ⁡ x)) R(x)=\frac{\phi(x)}{2}-x\sum_{n\leq x}\frac{\mu(n)\psi(x/n)}{n}+O\Big(x\exp(-c\sqrt{\log x})\Big) |  |

for some positive constant c c, where ϕ ⁡ ( x) = 0 \phi(x)=0 if x ∉ 𝐙 x\not\in\mathbf{Z}. The sum in this expression is akin to the equation ( 1.8) for s ^ q ​ ( t) \widehat{s}_{q}(t) with n ¯ / q \overline{n}/q replaced by 1 / n 1/n and with the weight 1 / n 1/n replaced with μ ⁡ ( n) / n \mu(n)/n. Accordingly, many of the techniques used to prove Theorems 1.1 and 1.2 apply to R ⁡ ( x) R(x) as well, though unfortunately with less precision owing to the presence of μ ⁡ ( n) \mu(n). For convenience, we define R ~ ​ ( x) = R ⁡ ( x) / x − ϕ ⁡ ( x) / 2 ​ x \widetilde{R}(x)=R(x)/x-\phi(x)/2x.

###### Theorem 1.3.

As y → ∞ y\to\infty the distribution of R ~ ​ ( u) \widetilde{R}(u) for real u ≤ y u\leq y tends to a probability distribution, symmetric around 0 0. Precisely, there is a function Φ R \Phi_{R} with Φ R ​ ( − x) + Φ R ​ ( x) = 1 \Phi_{R}(-x)+\Phi_{R}(x)=1 such that uniformly for all x ∈ [− X, X] x\in[-X,X] one has

 | 1 y ​ meas ​ ( { u ≤ y: R ~ ​ ( u) ≤ 3 ​ e γ π 2 ​ x }) = Φ R ​ ( x) + o ⁡ ( 1), \frac{1}{y}\mathrm{meas}(\{u\leq y:\ \widetilde{R}(u)\leq\tfrac{3e^{\gamma}}{\pi^{2}}x\})=\Phi_{R}(x)+o(1), |  |

where meas ⁡ ( I) \mathrm{meas}(I) denotes the Lebesgue measure of I ⊆ 𝐑 I\subseteq\mathbf{R}. Moreover, uniformly for all e ≤ x ≤ ( 1 2 − ϵ) ​ log ⁡ log ⁡ y e\leq x\leq(\frac{1}{2}-\epsilon)\log\log y one has

 | 1 y meas ( { u ≤ y: R ~ ( u) ≥ 3 ​ e γ π 2 x }) ≤ exp ( − A 1 e x / x) \frac{1}{y}\mathrm{meas}(\{u\leq y:\ \widetilde{R}(u)\geq\tfrac{3e^{\gamma}}{\pi^{2}}x\})\leq\exp(-A_{1}e^{x}/x) |  |

for some positive constant A 1 A_{1}.

We prove Theorem 1.3 by showing that all positive integral moments of R ~ ​ ( n) \widetilde{R}(n) exist and are not too large. The moment calculation refines earlier work of Pillai and Chowla [10] and Chowla [3], who computed the mean and variance respectively:

 | ∑ n ≤ x R ~ ​ ( n) = o ⁡ ( x) and 1 y ​ ∫ 0 y R ~ ​ ( u) 2 ​ 𝑑 u ∼ 1 2 ​ π 2. \sum_{n\leq x}\widetilde{R}(n)=o(x)\quad\text{and}\quad\frac{1}{y}\int_{0}^{y}\widetilde{R}(u)^{2}\,du\sim\frac{1}{2\pi^{2}}. |  |

In Theorem 1.3, using Montgomery’s construction in his Ω \Omega -result, we can obtain a lower bound for the frequency of large values of R ~ ​ ( u) {\widetilde{R}}(u) of the form exp ⁡ ( − e x 2 + ϵ) \exp(-e^{x^{2+\epsilon}}), which is very far from the upper bound. We expect that there is a lower bound similar to that in Theorems 1.1 and 1.2 in this situation also, and this would be in keeping with Montgomery’s conjecture on the true size of R ~ ​ ( u) {\widetilde{R}}(u).

### Organization

Our main focus is the proofs of Theorems 1.1 and 1.2. We establish preliminary results useful for both in Sections 2 and 3. We then prove Theorem 1.1 in Sections 4 - 6; since the proof of Theorem 1.2 follows along identical lines, we omit it. In Section 7, we discuss the modifications that lead to Theorem 1.3.

## 2. First steps

Here we establish some formulae for s ^ q ​ ( t) \widehat{s}_{q}(t) and C ⁡ ( k) C(k) which will be the basis for our subsequent work.

###### Lemma 2.1.

Let q q be prime. For any ( t, q) = 1 (t,q)=1, we have

 | s ^ q ​ ( t) = − 1 π ​ i ​ ϕ ​ ( q) ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ¯ ​ ( t) ​ L ​ ( 0, χ) ​ L ​ ( 1, χ) = 1 π ​ i ​ ∑ n = 1 ( n, q) = 1 ∞ ψ ⁡ ( t ​ n ¯ / q) n. \widehat{s}_{q}(t)=\frac{-1}{\pi i\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\bar{\chi}(t)L(0,\chi)L(1,\chi)=\frac{1}{\pi i}\sum_{\begin{subarray}{c}n=1\\ (n,q)=1\end{subarray}}^{\infty}\frac{\psi(t\overline{n}/q)}{n}. |  |

Moreover, for any x ≥ 1 x\geq 1 we have

 | s ^ q ​ ( t) = 1 π ​ i ​ ∑ n ≤ x ( n, q) = 1 ψ ⁡ ( t ​ n ¯ / q) n + O ⁡ ( q x). \widehat{s}_{q}(t)=\frac{1}{\pi i}\sum_{\begin{subarray}{c}n\leq x\\ (n,q)=1\end{subarray}}\frac{\psi(t\overline{n}/q)}{n}+O\Big(\frac{q}{x}\Big). |  |

###### Proof.

For any non-principal character χ ⁡ ( mod ​ q) \chi\,\left(\text{mod }q\right), we have (see, e.g., [13, Theorem 4.2])

(2.1) |  | L ( 0, χ) = − ∑ a ⁡ ( mod ​ q) χ ( a) ψ ( a / q). L(0,\chi)=-\sum_{a\,\left(\text{mod }q\right)}\chi(a)\psi(a/q). |  |

Notice that L ⁡ ( 0, χ) = 0 L(0,\chi)=0 if χ \chi is an even character, and that right side of the formula in ( 2.1) evaluates to 0 if χ \chi is principal. The functional equation for odd characters gives

 | L ⁡ ( 1, χ) = − τ ⁡ ( χ) ​ π ​ i q ​ L ​ ( 0, χ ¯), L(1,\chi)=-\frac{\tau(\chi)\pi i}{q}L(0,\bar{\chi}), |  |

where τ ⁡ ( χ) = ∑ m ⁡ ( mod ​ q) χ ⁡ ( m) ​ e ​ ( m / q) \tau(\chi)=\sum_{m\,\left(\text{mod }q\right)}\chi(m)e(m/q) denotes the Gauss sum. Thus we obtain

 | ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ¯ ​ ( t) ​ L ​ ( 0, χ) ​ L ​ ( 1, χ) \displaystyle\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\bar{\chi}(t)L(0,\chi)L(1,\chi) | = − π ​ i q ∑ χ ⁡ ( mod ​ q) τ ( χ) | ∑ a ⁡ ( mod ​ q) χ ( a) ψ ( a q) | 2 \displaystyle=-\frac{\pi i}{q}\sum_{\chi\,\left(\text{mod }q\right)}\tau(\chi)\Big|\sum_{a\,\left(\text{mod }q\right)}\chi(a)\psi\Big(\frac{a}{q}\Big)\Big|^{2} |  |

 |  | = − π ​ i q ∑ a, b, m ⁡ ( mod ​ q) e ( m / q) ψ ( a q) ψ ( b q) ∑ χ ⁡ ( mod ​ q) χ ( a m) χ ¯ ( b t) \displaystyle=-\frac{\pi i}{q}\sum_{a,b,m\,\left(\text{mod }q\right)}e(m/q)\psi\Big(\frac{a}{q}\Big)\psi\Big(\frac{b}{q}\Big)\sum_{\chi\,\left(\text{mod }q\right)}\chi(am)\bar{\chi}(bt) |  |

 |  | = − ϕ ⁡ ( q) ​ π ​ i q ∑ a, b ≢ 0 ​ ( mod ​ q) e ( t ​ b ​ a ¯ q) ψ ( a q) ψ ( b q) \displaystyle=-\frac{\phi(q)\pi i}{q}\sum_{a,b\not\equiv 0\,\left(\text{mod }q\right)}e\Big(\frac{tb\overline{a}}{q}\Big)\psi\Big(\frac{a}{q}\Big)\psi\Big(\frac{b}{q}\Big) |  |

 |  | = − ϕ ⁡ ( q) ​ π ​ i ​ s ^ q ​ ( t). \displaystyle=-\phi(q)\pi i\,\widehat{s}_{q}(t). |  |

The first identity in the lemma follows.

To obtain the second identity, note that using ( 2.1) and the orthogonality relation for characters

 | − ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ¯ ( t) L ( 0, χ) ∑ n ≤ N χ ⁡ ( n) n \displaystyle-\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\overline{\chi}(t)L(0,\chi)\sum_{n\leq N}\frac{\chi(n)}{n} | = ∑ χ ⁡ ( mod ​ q) χ ¯ ​ ( t) ​ ∑ a ⁡ ( mod ​ q) χ ⁡ ( a) ​ ψ ​ ( a / q) ​ ∑ n ≤ N χ ⁡ ( n) n \displaystyle=\sum_{\chi\,\left(\text{mod }q\right)}\overline{\chi}(t)\sum_{a\,\left(\text{mod }q\right)}\chi(a)\psi(a/q)\sum_{n\leq N}\frac{\chi(n)}{n} |  |

(2.2) |  |  | = ϕ ⁡ ( q) ​ ∑ n ≤ N ( n, q) = 1 1 n ​ ψ ​ ( t ​ n ¯ / q). \displaystyle=\phi(q)\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}\frac{1}{n}\psi(t\overline{n}/q). |  |

Letting N → ∞ N\to\infty, the second identity follows.

To obtain the truncated version, note that

 | | ∑ n ≤ x ( n, q) = 1 ψ ⁡ ( t ​ n ¯ / q) | ≤ q \Big|\sum_{\begin{subarray}{c}n\leq x\\ (n,q)=1\end{subarray}}\psi(t\overline{n}/q)\Big|\leq q |  |

trivially, and therefore

 | ∑ n > x ( n, q) = 1 ψ ⁡ ( t ​ n ¯ / q) n = ∫ x ∞ 1 y 2 ​ ∑ x < n ≤ y ψ ⁡ ( t ​ n ¯ / q) ​ 𝑑 y ≪ q x. \sum_{\begin{subarray}{c}n>x\\ (n,q)=1\end{subarray}}\frac{\psi(t\overline{n}/q)}{n}=\int_{x}^{\infty}\frac{1}{y^{2}}\sum_{x<n\leq y}\psi(t\overline{n}/q)dy\ll\frac{q}{x}. |  |

∎

Recall the definition of A q, χ A_{q,\chi} from ( 1.2). Expanding this product out, we find

(2.3) |  | A q, χ = ( 2 ​ χ ​ ( 2) − χ ​ ( 2) 2) ​ ∏ p ∤ 2 ​ q ( 1 − 1 ( p − 1) 2) ​ ( 1 + 2 ​ χ ​ ( p) − χ ​ ( p) 2 p 2 − 2 ​ p) = C ​ ∑ n = 1 ∞ a ⁡ ( n) ​ χ ​ ( 2 ​ n). A_{q,\chi}=(2\chi(2)-\chi(2)^{2})\prod_{p\nmid 2q}\Big(1-\frac{1}{(p-1)^{2}}\Big)\Big(1+\frac{2\chi(p)-\chi(p)^{2}}{p^{2}-2p}\Big)=C\sum_{n=1}^{\infty}a(n)\chi(2n). |  |

Here

(2.4) |  | C = 2 ​ ∏ p ≥ 3 p ∤ q ( 1 − 1 ( p − 1) 2), C=2\prod_{\begin{subarray}{c}p\geq 3\\ p\nmid q\end{subarray}}\Big(1-\frac{1}{(p-1)^{2}}\Big), |  |

and a ⁡ ( n) a(n) is a multiplicative function defined by a ( 2) = − 1 / 2 a(2)=-1/2 and a ⁡ ( 2 v) = 0 a(2^{v})=0 for all v ≥ 2 v\geq 2, and for odd primes p p we have

(2.5) |  | a ( p) = 2 p ⁡ ( p − 2), a ( p 2) = − 1 p ⁡ ( p − 2), and a ( p v) = 0 for all v ≥ 3. a(p)=\frac{2}{p(p-2)},\qquad a(p^{2})=-\frac{1}{p(p-2)},\qquad\text{and }\qquad a(p^{v})=0\text{ for all }v\geq 3. |  |

From the definition of a ⁡ ( n) a(n) it is easy to check that ∑ n = 1 ∞ | a ⁡ ( n) | ​ n σ \sum_{n=1}^{\infty}|a(n)|n^{\sigma} converges for all σ < 1 / 2 \sigma<1/2 so that

(2.6) |  | ∑ n ≥ N | a ⁡ ( n) | ≪ N − 1 2 + ϵ and C ​ ∑ n ≤ N ( n, q) = 1 a ⁡ ( n) = 1 + O ⁡ ( N − 1 2 + ϵ). \sum_{n\geq N}|a(n)|\ll N^{-\frac{1}{2}+\epsilon}\qquad\text{and }\qquad C\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}a(n)=1+O(N^{-\frac{1}{2}+\epsilon}). |  |

###### Lemma 2.2.

Define the multiplicative function b ⁡ ( n) b(n) by setting b ⁡ ( n) = ∑ u ​ v = n a ⁡ ( u) / v b(n)=\sum_{uv=n}a(u)/v, so that b ⁡ ( n) = 0 b(n)=0 unless n n is odd and square-free, and b ⁡ ( p) = 1 / ( p − 2) b(p)=1/(p-2) for all odd primes p p. Then for any natural number N N we have

 | C ( k) = − C ∑ n ≤ N ( n, q) = 1 b ( n) ψ ( k 2 ​ n ¯ / q) + O ( q 3 2 + ϵ N − 1 4 + ϵ). C(k)=-C\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}b(n)\psi(k\overline{2n}/q)+O(q^{\frac{3}{2}+\epsilon}N^{-\frac{1}{4}+\epsilon}). |  |

###### Proof.

Arguing as in ( 2) we find

(2.7) |  | 1 ϕ ⁡ ( q) ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ⁡ ( k) ¯ L ( 0, χ) ∑ n ≤ N ( n, q) = 1 b ( n) χ ( 2 n) = − ∑ n ≤ N ( n, q) = 1 b ( n) ψ ( k 2 ​ n ¯ / q). \frac{1}{\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\overline{\chi(k)}L(0,\chi)\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}b(n)\chi(2n)=-\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}b(n)\psi(k\overline{2n}/q). |  |

Now if n = u ​ v ≤ N n=uv\leq N then either u ≤ N u\leq\sqrt{N} or v ≤ N v\leq\sqrt{N} and N < u ≤ N / v \sqrt{N}<u\leq N/v. Therefore

(2.8) |  | ∑ n ≤ N b ⁡ ( n) ​ χ ​ ( 2 ​ n) = ∑ u ≤ N a ⁡ ( u) ​ χ ​ ( 2 ​ u) ​ ∑ v ≤ N / u χ ⁡ ( v) v + ∑ v ≤ N χ ⁡ ( v) v ​ ∑ N < u ≤ N / v a ⁡ ( u) ​ χ ​ ( 2 ​ u). \sum_{n\leq N}b(n)\chi(2n)=\sum_{u\leq\sqrt{N}}a(u)\chi(2u)\sum_{v\leq N/u}\frac{\chi(v)}{v}+\sum_{v\leq\sqrt{N}}\frac{\chi(v)}{v}\sum_{\sqrt{N}<u\leq N/v}a(u)\chi(2u). |  |

Bounding the partial sums of characters trivially, we find

(2.9) |  | L ⁡ ( 1, χ) = ∑ n ≤ x χ ⁡ ( n) n + ∫ x ∞ ∑ x < n ≤ y χ ⁡ ( n) ​ d ​ y y 2 = ∑ n ≤ x χ ⁡ ( n) n + O ⁡ ( q x), L(1,\chi)=\sum_{n\leq x}\frac{\chi(n)}{n}+\int_{x}^{\infty}\sum_{x<n\leq y}\chi(n)\frac{dy}{y^{2}}=\sum_{n\leq x}\frac{\chi(n)}{n}+O\Big(\frac{q}{x}\Big), |  |

and so the first term in ( 2.8) is (using ( 2.6))

 |  | ∑ u ≤ N a ⁡ ( u) ​ χ ​ ( 2 ​ u) ​ ( L ⁡ ( 1, χ) + O ⁡ ( q ​ u N)) \displaystyle\sum_{u\leq\sqrt{N}}a(u)\chi(2u)\Big(L(1,\chi)+O\Big(\frac{qu}{N}\Big)\Big) |  |

 | = \displaystyle= | C − 1 ​ A q, χ ​ L ​ ( 1, χ) + O ⁡ ( ( log ⁡ q) ​ N − 1 4 + ϵ) + O ⁡ ( q ​ N − 1 2) \displaystyle C^{-1}A_{q,\chi}L(1,\chi)+O((\log q)N^{-\frac{1}{4}+\epsilon})+O(qN^{-\frac{1}{2}}) |  |

 | = \displaystyle= | C − 1 ​ A q, χ ​ L ​ ( 1, χ) + O ⁡ ( q ​ N − 1 4 + ϵ). \displaystyle C^{-1}A_{q,\chi}L(1,\chi)+O(qN^{-\frac{1}{4}+\epsilon}). |  |

As for the second term in ( 2.8), using ( 2.6) we may bound this by

 | ≪ ∑ v ≤ N 1 v ​ N − 1 4 + ϵ ≪ N − 1 4 + ϵ. \ll\sum_{v\leq\sqrt{N}}\frac{1}{v}N^{-\frac{1}{4}+\epsilon}\ll N^{-\frac{1}{4}+\epsilon}. |  |

We conclude that

 | C ∑ n ≤ N ( n, q) = 1 b ( n) ψ ( k 2 ​ n ¯ / q) = − 1 ϕ ⁡ ( q) ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ⁡ ( k) ¯ L ( 0, χ) ( A q, χ L ( 1, χ) + O ( q N − 1 4 + ϵ)), C\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}b(n)\psi(k\overline{2n}/q)=-\frac{1}{\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\overline{\chi(k)}L(0,\chi)\Big(A_{q,\chi}L(1,\chi)+O(qN^{-\frac{1}{4}+\epsilon})\Big), |  |

and since L ⁡ ( 0, χ) ≪ q ​ log ⁡ q L(0,\chi)\ll\sqrt{q}\log q, the lemma follows. ∎

Lemmas 2.1 and 2.2 give crude approximations to s ^ q ​ ( t) \widehat{s}_{q}(t) and C ⁡ ( k) C(k) by long sums (for example taking x = q 2 x=q^{2} in Lemma 2.1, or taking N = q 8 N=q^{8} in Lemma 2.2). However, on average over t t or k k, it is possible to approximate these quantities by very short sums.

###### Lemma 2.3.

Let 1 ≤ B < q 1\leq B<q be a real number. Then

 | 1 ϕ ⁡ ( q) ​ ∑ k ⁡ ( mod ​ q) | C ⁡ ( k) + C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ / q) | 2 ≪ B − 1 + ϵ, \frac{1}{\phi(q)}\sum_{k\,\left(\text{mod }q\right)}\Big|C(k)+C\sum_{n\leq B}b(n)\psi(k\overline{2n}/q)\Big|^{2}\ll B^{-1+\epsilon}, |  |

and

 | 1 ϕ ⁡ ( q) ​ ∑ t ⁡ ( mod ​ q) | s ^ q ​ ( t) − 1 π ​ i ​ ∑ n ≤ B ψ ⁡ ( t ​ n ¯ / q) n | 2 ≪ B − 1 + ϵ. \frac{1}{\phi(q)}\sum_{t\,\left(\text{mod }q\right)}\Big|\widehat{s}_{q}(t)-\frac{1}{\pi i}\sum_{n\leq B}\frac{\psi(t\overline{n}/q)}{n}\Big|^{2}\ll B^{-1+\epsilon}. |  |

###### Proof.

We shall content ourselves with proving the estimate for C ⁡ ( k) C(k), the situation for s ^ q ​ ( t) {\widehat{s}}_{q}(t) being entirely similar. Using ( 2.7) and Lemma 2.2 we see that

 |  | 1 ϕ ⁡ ( q) ​ ∑ k ⁡ ( mod ​ q) | C ⁡ ( k) + C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ / q) | 2 \displaystyle\frac{1}{\phi(q)}\sum_{k\,\left(\text{mod }q\right)}\Big|C(k)+C\sum_{n\leq B}b(n)\psi(k\overline{2n}/q)\Big|^{2} |  |

 | = \displaystyle= | 1 ϕ ⁡ ( q) ​ ∑ k ⁡ ( mod ​ q) | C ϕ ⁡ ( q) ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) χ ⁡ ( k) ¯ ​ L ​ ( 0, χ) ​ ∑ B < n ≤ q 10 b ⁡ ( n) ​ χ ​ ( 2 ​ n) + O ⁡ ( q − 1 + ϵ) | 2. \displaystyle\frac{1}{\phi(q)}\sum_{k\,\left(\text{mod }q\right)}\Big|\frac{C}{\phi(q)}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\overline{\chi(k)}L(0,\chi)\sum_{\begin{subarray}{c}B<n\leq q^{10}\end{subarray}}b(n)\chi(2n)+O(q^{-1+\epsilon})\Big|^{2}. |  |

Using the orthogonality of characters to evaluate the sum over k k, this is

 | ≪ 1 ϕ ​ ( q) 2 ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) | L ⁡ ( 0, χ) | 2 ​ | ∑ B < n ≤ q 10 b ⁡ ( n) ​ χ ​ ( n) | 2 + q − 2 + ϵ, \ll\frac{1}{\phi(q)^{2}}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}|L(0,\chi)|^{2}\Big|\sum_{B<n\leq q^{10}}b(n)\chi(n)\Big|^{2}+q^{-2+\epsilon}, |  |

and using ( 2.9) and the functional equation this is

 | ≪ 1 q ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) | ∑ m ≤ q 2 χ ⁡ ( m) m ​ ∑ B < n ≤ q 10 b ⁡ ( n) ​ χ ​ ( n) | 2 + q − 2 + ϵ. \ll\frac{1}{q}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\Big|\sum_{m\leq q^{2}}\frac{\chi(m)}{m}\sum_{B<n\leq q^{10}}b(n)\chi(n)\Big|^{2}+q^{-2+\epsilon}. |  |

Write temporarily

 | ∑ m ≤ q 2 χ ⁡ ( m) m ​ ∑ B < n ≤ q 10 b ⁡ ( n) ​ χ ​ ( n) = ∑ B < n ≤ q 12 α ⁡ ( n) n ​ χ ​ ( n), \sum_{m\leq q^{2}}\frac{\chi(m)}{m}\sum_{B<n\leq q^{10}}b(n)\chi(n)=\sum_{B<n\leq q^{12}}\frac{\alpha(n)}{n}\chi(n), |  |

for some coefficients α ⁡ ( n) ≪ n ϵ \alpha(n)\ll n^{\epsilon}. Then (including also the contribution of χ 0 \chi_{0} below)

 | 1 q ​ ∑ χ ≠ χ 0 ​ ( mod ​ q) | ∑ B < n ≤ q 12 α ⁡ ( n) n ​ χ ​ ( n) | 2 ≪ ∑ B < n 1, n 2 ≤ q 12 n 1 ≡ n 2 ​ ( mod ​ q) | α ⁡ ( n 1) ​ α ​ ( n 2) | n 1 ​ n 2. \frac{1}{q}\sum_{\chi\neq\chi_{0}\,\left(\text{mod }q\right)}\Big|\sum_{B<n\leq q^{12}}\frac{\alpha(n)}{n}\chi(n)\Big|^{2}\ll\sum_{\begin{subarray}{c}B<n_{1},n_{2}\leq q^{12}\\ n_{1}\equiv n_{2}\,\left(\text{mod }q\right)\end{subarray}}\frac{|\alpha(n_{1})\alpha(n_{2})|}{n_{1}n_{2}}. |  |

The terms with n 1 n_{1}, n 2 n_{2} both below q q (so that n 1 = n 2 n_{1}=n_{2}) contribute

 | ≪ ∑ B < n < q n ϵ n 2 ≪ B − 1 + ϵ. \ll\sum_{B<n<q}\frac{n^{\epsilon}}{n^{2}}\ll B^{-1+\epsilon}. |  |

The terms with max ⁡ ( n 1, n 2) ≥ q \max(n_{1},n_{2})\geq q contribute (assume without loss of generality that n 2 n_{2} is the larger one)

 | ≪ q ϵ ​ ∑ B < n 1 ≤ q 12 1 n 1 ​ ∑ q < n 2 ≤ q 12 n 2 ≡ n 1 ​ ( mod ​ q) 1 n 2 ≪ q ϵ ​ log ⁡ q ​ log ⁡ q q ≪ q − 1 + ϵ. \ll q^{\epsilon}\sum_{B<n_{1}\leq q^{12}}\frac{1}{n_{1}}\sum_{\begin{subarray}{c}q<n_{2}\leq q^{12}\\ n_{2}\equiv n_{1}\,\left(\text{mod }q\right)\end{subarray}}\frac{1}{n_{2}}\ll q^{\epsilon}\log q\frac{\log q}{q}\ll q^{-1+\epsilon}. |  |

Assembling these estimates, the lemma follows. ∎

## 3. A key quantity

We shall study s ^ q ​ ( t) {\widehat{s}}_{q}(t) and C ⁡ ( k) C(k) by computing their moments, and the following key quantity will arise in this context. Let ℓ \ell be a natural number, and suppose n 1 n_{1}, … \ldots, n ℓ n_{\ell} are ℓ \ell natural numbers. Then set

(3.1) |  | ℬ ( n 1, …, n ℓ) = 1 n 1 ⋯ n ℓ ∫ 0 n 1 ⋯ n ℓ ∏ j = 1 ℓ ψ ( x / n j) d x. {\mathcal{B}}(n_{1},\ldots,n_{\ell})=\frac{1}{n_{1}\cdots n_{\ell}}\int_{0}^{n_{1}\cdots n_{\ell}}\prod_{j=1}^{\ell}\psi(x/n_{j})dx. |  |

###### Proposition 3.1.

The quantity ℬ ⁡ ( n 1, …, n ℓ) \mathcal{B}(n_{1},\dots,n_{\ell}) satisfies the following properties.

(1) If ℓ \ell is odd then ℬ ⁡ ( n 1, …, n ℓ) = 0 {\mathcal{B}}(n_{1},\ldots,n_{\ell})=0. For even ℓ \ell we have

(3.2) |  | ℬ ⁡ ( n 1, …, n ℓ) = ( i 2 ​ π) ℓ ​ ∑ k 1, …, k ℓ ≠ 0 ∑ k j / n j = 0 1 k 1 ⋯ k ℓ, {\mathcal{B}}(n_{1},\ldots,n_{\ell})=\Big(\frac{i}{2\pi}\Big)^{\ell}\sum_{\begin{subarray}{c}k_{1},\ldots,k_{\ell}\neq 0\\ \sum k_{j}/n_{j}=0\end{subarray}}\frac{1}{k_{1}\cdots k_{\ell}}, |  |

where the sum is over all non-zero integers k j k_{j}, and this sum is absolutely convergent. In the case ℓ = 2 \ell=2 one has

 | ℬ ⁡ ( n 1, n 2) = ( n 1, n 2) 2 12 ​ n 1 ​ n 2. {\mathcal{B}}(n_{1},n_{2})=\frac{(n_{1},n_{2})^{2}}{12n_{1}n_{2}}. |  |

(2) If p p is a prime dividing n j n_{j} and such that p p does not divide any other n i n_{i}, then

 | ℬ ⁡ ( n 1, …, n j, …, n ℓ) = 1 p ​ ℬ ​ ( n 1, …, n j / p, …, n ℓ). {\mathcal{B}}(n_{1},\ldots,n_{j},\ldots,n_{\ell})=\frac{1}{p}{\mathcal{B}}(n_{1},\ldots,n_{j}/p,\ldots,n_{\ell}). |  |

(3) If we write n 1 ⋯ n ℓ = r s n_{1}\cdots n_{\ell}=rs where r r and s s are coprime and r r is square-free while s s is square-full then

 | | ℬ ⁡ ( n 1, …, n ℓ) | ≤ 2 − ℓ ​ r − 1. |{\mathcal{B}}(n_{1},\ldots,n_{\ell})|\leq 2^{-\ell}r^{-1}. |  |

We begin by recalling the Fourier expansion of the sawtooth function. Note that ψ ^ ​ ( 0) = 0 {\widehat{\psi}}(0)=0 and for k ≠ 0 k\neq 0 we have

(3.3) |  | ψ ^ ​ ( k) = ∫ 0 1 ψ ⁡ ( x) ​ e ​ ( − k ​ x) ​ 𝑑 x = 1 − 2 ​ π ​ i ​ k = i 2 ​ π ​ k, {\widehat{\psi}}(k)=\int_{0}^{1}\psi(x)e(-kx)dx=\frac{1}{-2\pi ik}=\frac{i}{2\pi k}, |  |

and so

(3.4) |  | ψ ⁡ ( x) = i ​ ∑ k ≠ 0 e ⁡ ( k ​ x) 2 ​ π ​ k. \psi(x)=i\sum_{k\neq 0}\frac{e(kx)}{2\pi k}. |  |

This series converges conditionally pointwise for each x ∉ 𝐙 x\not\in\mathbf{Z}, and also in the L 2 L^{2} -sense. For any non-negative integer N N, recall also the Fejer kernel

(3.5) |  | K N ​ ( x) = ∑ j = − N N ( 1 − | j | N + 1) ​ e ​ ( j ​ x) = 1 N + 1 ​ ( sin ⁡ ( π ⁡ ( N + 1) ​ x) sin ⁡ π ​ x) 2. K_{N}(x)=\sum_{j=-N}^{N}\Big(1-\frac{|j|}{N+1}\Big)e(jx)=\frac{1}{N+1}\Big(\frac{\sin(\pi(N+1)x)}{\sin\pi x}\Big)^{2}. |  |

We shall find it convenient to replace ψ ⁡ ( x) \psi(x) by the approximation ψ N ​ ( x) \psi_{N}(x) defined by

(3.6) |  | ψ N ​ ( x) = i ​ ∑ 0 < | k | ≤ N e ⁡ ( k ​ x) 2 ​ π ​ k ​ ( 1 − | k | N + 1). \psi_{N}(x)=i\sum_{0<|k|\leq N}\frac{e(kx)}{2\pi k}\Big(1-\frac{|k|}{N+1}\Big). |  |

Note that ψ N \psi_{N} is the convolution of ψ \psi with the Fejer kernel K N K_{N}

 | ψ N ​ ( x) = ∫ 0 1 ψ ⁡ ( y) ​ K N ​ ( x − y) ​ 𝑑 y, \psi_{N}(x)=\int_{0}^{1}\psi(y)K_{N}(x-y)dy, |  |

and so

(3.7) |  | | ψ N ​ ( x) − ψ ⁡ ( x) | ≪ min ⁡ ( 1, 1 N ​ ‖ x ‖), |\psi_{N}(x)-\psi(x)|\ll\min\Big(1,\frac{1}{N\|x\|}\Big), |  |

which implies that

(3.8) |  | ∫ 0 1 | ψ N ​ ( x) − ψ ⁡ ( x) | ​ 𝑑 x ≪ 1 + log ⁡ N N. \int_{0}^{1}|\psi_{N}(x)-\psi(x)|dx\ll\frac{1+\log N}{N}. |  |

Note also that | ψ N ​ ( x) | ≤ 1 / 2 |\psi_{N}(x)|\leq 1/2 always.

###### Proof of Proposition 3.1: Part 1.

Since ψ \psi is an odd function, it is clear that ℬ ⁡ ( n 1, …, n ℓ) = 0 {\mathcal{B}}(n_{1},\ldots,n_{\ell})=0 for odd ℓ \ell. Now suppose ℓ \ell is even. By Parseval it follows that

(3.9) |  | 1 n 1 ⋯ n ℓ ∫ 0 n 1 ⋯ n ℓ ψ N ( x / n 1) ⋯ ψ N ( x / n ℓ) d x = ( i 2 ​ π) ℓ ∑ 0 < | k j | ≤ N ∑ k j / n j = 0 1 k 1 ⋯ k ℓ ∏ j = 1 ℓ ( 1 − | k j | N + 1). \frac{1}{n_{1}\cdots n_{\ell}}\int_{0}^{n_{1}\cdots n_{\ell}}\psi_{N}(x/n_{1})\cdots\psi_{N}(x/n_{\ell})dx=\Big(\frac{i}{2\pi}\Big)^{\ell}\sum_{\begin{subarray}{c}0<|k_{j}|\leq N\\ \sum k_{j}/n_{j}=0\end{subarray}}\frac{1}{k_{1}\cdots k_{\ell}}\prod_{j=1}^{\ell}\Big(1-\frac{|k_{j}|}{N+1}\Big). |  |

For any complex numbers α 1 \alpha_{1}, … \ldots, α ℓ \alpha_{\ell} and β 1 \beta_{1}, … \ldots, β ℓ \beta_{\ell} note the simple identity

(3.10) |  | α 1 ⋯ α ℓ − β 1 ⋯ β ℓ = ( α 1 − β 1) α 2 ⋯ α ℓ + β 1 ( α 2 − β 2) α 3 ⋯ α ℓ + β 1 ⋯ β ℓ − 1 ( α ℓ − β ℓ). \alpha_{1}\cdots\alpha_{\ell}-\beta_{1}\cdots\beta_{\ell}=(\alpha_{1}-\beta_{1})\alpha_{2}\cdots\alpha_{\ell}+\beta_{1}(\alpha_{2}-\beta_{2})\alpha_{3}\cdots\alpha_{\ell}+\beta_{1}\cdots\beta_{\ell-1}(\alpha_{\ell}-\beta_{\ell}). |  |

Applying this, we obtain

 | | ψ ( x / n 1) ⋯ ψ ( x / n ℓ) − ψ N ( x / n 1) ⋯ ψ N ( x / n ℓ) | ≤ 1 2 ℓ − 1 ∑ j = 1 ℓ | ψ ( x / n j) − ψ N ( x / n j) |, |\psi(x/n_{1})\cdots\psi(x/n_{\ell})-\psi_{N}(x/n_{1})\cdots\psi_{N}(x/n_{\ell})|\leq\frac{1}{2^{\ell-1}}\sum_{j=1}^{\ell}|\psi(x/n_{j})-\psi_{N}(x/n_{j})|, |  |

and so by ( 3.9) and ( 3.8) we conclude that

 | ℬ ⁡ ( n 1, …, n ℓ) \displaystyle{\mathcal{B}}(n_{1},\ldots,n_{\ell}) | = 1 n 1 ⋯ n ℓ ∫ 0 n 1 ⋯ n ℓ ψ ( x / n 1) ⋯ ψ ( x / n ℓ) d x \displaystyle=\frac{1}{n_{1}\cdots n_{\ell}}\int_{0}^{n_{1}\cdots n_{\ell}}\psi(x/n_{1})\cdots\psi(x/n_{\ell})dx |  |

(3.11) |  |  | = ( i 2 ​ π) ℓ ​ ∑ 0 < | k j | ≤ N ∑ k j / n j = 0 1 k 1 ⋯ k ℓ ​ ∏ j = 1 ℓ ( 1 − | k j | N + 1) + O ⁡ ( 1 + log ⁡ N N). \displaystyle=\Big(\frac{i}{2\pi}\Big)^{\ell}\sum_{\begin{subarray}{c}0<|k_{j}|\leq N\\ \sum k_{j}/n_{j}=0\end{subarray}}\frac{1}{k_{1}\cdots k_{\ell}}\prod_{j=1}^{\ell}\Big(1-\frac{|k_{j}|}{N+1}\Big)+O\Big(\frac{1+\log N}{N}\Big). |  |

We now show that

 | ∑ 0 < | k j | ≤ N ∑ k j / n j = 0 1 | k 1 ⋯ k ℓ | \sum_{\begin{subarray}{c}0<|k_{j}|\leq N\\ \sum k_{j}/n_{j}=0\end{subarray}}\frac{1}{|k_{1}\cdots k_{\ell}|} |  |

is bounded, so that ( 3) will imply (letting N → ∞ N\to\infty) the stated formula ( 3.2) for ℬ ⁡ ( n 1, …, n ℓ) {\mathcal{B}}(n_{1},\ldots,n_{\ell}) and that the sum there converges absolutely. By Parseval

 | ∑ 0 < | k j | ≤ N ∑ k j / n j = 0 1 | k 1 ⋯ k ℓ | = 1 n 1 ⋯ n ℓ ∫ 0 n 1 ⋯ n ℓ ∏ j = 1 ℓ ( ∑ 0 < | k j | ≤ N e ⁡ ( k j ​ x / n j) | k j |) d x. \sum_{\begin{subarray}{c}0<|k_{j}|\leq N\\ \sum k_{j}/n_{j}=0\end{subarray}}\frac{1}{|k_{1}\cdots k_{\ell}|}=\frac{1}{n_{1}\cdots n_{\ell}}\int_{0}^{n_{1}\cdots n_{\ell}}\prod_{j=1}^{\ell}\Big(\sum_{0<|k_{j}|\leq N}\frac{e(k_{j}x/n_{j})}{|k_{j}|}\Big)dx. |  |

One may check that (with ‖ x ‖ \|x\| denoting the distance of x x from the nearest integer)

 | ∑ 0 < | k | ≤ N e ⁡ ( k ​ θ) | k | ≪ log ⁡ min ⁡ ( N, 1 ‖ θ ‖) ≪ log ⁡ N 1 + N ​ ‖ θ ‖. \sum_{0<|k|\leq N}\frac{e(k\theta)}{|k|}\ll\log\min\Big(N,\frac{1}{\|\theta\|}\Big)\ll\log\frac{N}{1+N\|\theta\|}. |  |

Using this and the arithmetic-geometric mean inequality above, we find

 | ∑ 0 < | k j | ≤ N ∑ k j / n j = 0 1 | k 1 ⋯ k ℓ | \displaystyle\sum_{\begin{subarray}{c}0<|k_{j}|\leq N\\ \sum k_{j}/n_{j}=0\end{subarray}}\frac{1}{|k_{1}\cdots k_{\ell}|} | ≪ ∑ j = 1 ℓ 1 n 1 ⋯ n ℓ ∫ 0 n 1 ⋯ n ℓ ( log N 1 + N ​ ‖ x / n j ‖) ℓ d x \displaystyle\ll\sum_{j=1}^{\ell}\frac{1}{n_{1}\cdots n_{\ell}}\int_{0}^{n_{1}\cdots n_{\ell}}\Big(\log\frac{N}{1+N\|x/n_{j}\|}\Big)^{\ell}dx |  |

 |  | ≪ ∫ 0 1 ( log ⁡ N 1 + N ​ ‖ x ‖) ℓ ​ 𝑑 x ≪ 1. \displaystyle\ll\int_{0}^{1}\Big(\log\frac{N}{1+N\|x\|}\Big)^{\ell}dx\ll 1. |  |

This proves our claim, and establishes ( 3.2).

If ℓ = 2 \ell=2 then the condition k 1 / n 1 + k 2 / n 2 = 0 k_{1}/n_{1}+k_{2}/n_{2}=0 means that k 1 = r ​ n 1 / ( n 1, n 2) k_{1}=rn_{1}/(n_{1},n_{2}) and k 2 = − r n 2 / ( n 1, n 2) k_{2}=-rn_{2}/(n_{1},n_{2}) for some non-zero integer r r. Therefore

 | ℬ ( n 1, n 2) = − 1 4 ​ π 2 ∑ r ≠ 0 − 1 r 2 ( n 1, n 2) 2 n 1 ​ n 2 = ( n 1, n 2) 2 12 ​ n 1 ​ n 2. {\mathcal{B}}(n_{1},n_{2})=-\frac{1}{4\pi^{2}}\sum_{r\neq 0}\frac{-1}{r^{2}}\frac{(n_{1},n_{2})^{2}}{n_{1}n_{2}}=\frac{(n_{1},n_{2})^{2}}{12n_{1}n_{2}}. |  |

∎

###### Proof of Proposition 3.1: Parts 2 and 3.

If p p divides n j n_{j} and no other n i n_{i}, then, in ( 3.2), k j k_{j} must necessarily be a multiple of p p. Cancelling p p from k j k_{j} and n j n_{j}, Part 2 follows. Part 3 follows from Part 2, and noting that | ℬ ⁡ ( n 1, …, n ℓ) | ≤ 2 − ℓ |{\mathcal{B}}(n_{1},\ldots,n_{\ell})|\leq 2^{-\ell} always. ∎

For computing the moments of s ^ q ​ ( t) {\widehat{s}}_{q}(t) and C ⁡ ( k) C(k) the following proposition, which connects correlations of the sawtooth function with ℬ {\mathcal{B}}, will be very useful.

###### Proposition 3.2.

Let n 1 n_{1}, … \ldots, n ℓ n_{\ell} be positive integers. Define K = n 1 ⋯ n ℓ / min ( n 1, …, n ℓ) K=n_{1}\cdots n_{\ell}/\min(n_{1},\ldots,n_{\ell}). If K < q / ℓ K<q/\ell then

 | 1 q ∑ k ⁡ ( mod ​ q) ψ ( k n 1 ¯ / q) ⋯ ψ ( k n ℓ ¯ / q) = ℬ ( n 1, …, n ℓ) + O ( ℓ ​ K q log ( e ​ q K)). \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}\psi(k\overline{n_{1}}/q)\cdots\psi(k\overline{n_{\ell}}/q)={\mathcal{B}}(n_{1},\ldots,n_{\ell})+O\Big(\frac{\ell K}{q}\log\Big(\frac{eq}{K}\Big)\Big). |  |

###### Proof.

Take N = ⌊ q / ( ℓ ​ K) ⌋ N=\lfloor q/(\ell K)\rfloor. The identity ( 3.10) gives

 | ∑ k ⁡ ( mod ​ q) | ψ ( k n 1 ¯ / q) ⋯ ψ ( k n ℓ ¯ / q) \displaystyle\sum_{k\,\left(\text{mod }q\right)}|\psi(k\overline{n_{1}}/q)\cdots\psi(k\overline{n_{\ell}}/q) | − ψ N ( k n 1 ¯ / q) ⋯ ψ N ( k n ℓ ¯ / q) | \displaystyle-\psi_{N}(k\overline{n_{1}}/q)\cdots\psi_{N}(k\overline{n_{\ell}}/q)| |  |

 |  | ≤ 1 2 ℓ − 1 ​ ∑ j = 1 ℓ ∑ k ⁡ ( mod ​ q) | ψ ⁡ ( k ​ n j ¯ / q) − ψ N ​ ( k ​ n j ¯ / q) |. \displaystyle\leq\frac{1}{2^{\ell-1}}\sum_{j=1}^{\ell}\sum_{k\,\left(\text{mod }q\right)}|\psi(k\overline{n_{j}}/q)-\psi_{N}(k\overline{n_{j}}/q)|. |  |

Using now ( 3.7), the above is

(3.12) |  | ≪ 1 2 ℓ ​ ∑ j = 1 ℓ ∑ k ⁡ ( mod ​ q) min ⁡ ( 1, 1 N ​ ‖ k ​ n j ¯ / q ‖) ≪ q N ​ log ⁡ ( e ​ N). \ll\frac{1}{2^{\ell}}\sum_{j=1}^{\ell}\sum_{k\,\left(\text{mod }q\right)}\min\Big(1,\frac{1}{N\|k\overline{n_{j}}/q\|}\Big)\ll\frac{q}{N}\log(eN). |  |

By Parseval

(3.13) |  | 1 q ∑ k ⁡ ( mod ​ q) ψ N ( k n 1 ¯ / q) ⋯ ψ N ( k n ℓ ¯ / q) = ( i 2 ​ π) ℓ ∑ 0 < | k j | ≤ N ∑ j k j ​ n j ¯ ≡ 0 ​ ( mod ​ q) 1 k 1 ⋯ k ℓ ∏ j = 1 ℓ ( 1 − | k j | N + 1), \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}\psi_{N}(k\overline{n_{1}}/q)\cdots\psi_{N}(k\overline{n_{\ell}}/q)=\Big(\frac{i}{2\pi}\Big)^{\ell}\sum_{\begin{subarray}{c}0<|k_{j}|\leq N\\ \sum_{j}k_{j}\overline{n_{j}}\equiv 0\,\left(\text{mod }q\right)\end{subarray}}\frac{1}{k_{1}\cdots k_{\ell}}\prod_{j=1}^{\ell}\Big(1-\frac{|k_{j}|}{N+1}\Big), |  |

which bears a striking resemblance to ( 3.9). With our choice for N N, we claim that in fact the right side of ( 3.13) is exactly equal to the expression in ( 3.9). Multiplying through by n 1 ⋯ n ℓ n_{1}\cdots n_{\ell}, the congruence ∑ k j ​ n j ¯ ≡ 0 ​ ( mod ​ q) \sum k_{j}\overline{n_{j}}\equiv 0\,\left(\text{mod }q\right) becomes ∑ j k j ( n 1 ⋯ n ℓ / n j) ≡ 0 ( mod q) \sum_{j}k_{j}(n_{1}\cdots n_{\ell}/n_{j})\equiv 0\,\left(\text{mod }q\right). Since | k j | < q / ( ℓ ​ K) |k_{j}|<q/(\ell K) and ( n 1 ⋯ n ℓ / n j) ≤ K (n_{1}\cdots n_{\ell}/n_{j})\leq K for all j j, it follows that | ∑ j k j ( n 1 ⋯ n ℓ / n j) | < q |\sum_{j}k_{j}(n_{1}\cdots n_{\ell}/n_{j})|<q so that the congruence becomes the equality ∑ j k j ( n 1 ⋯ n ℓ / n j) = 0 \sum_{j}k_{j}(n_{1}\cdots n_{\ell}/n_{j})=0, which is the same as the criterion ∑ j k j / n j = 0 \sum_{j}k_{j}/n_{j}=0 of ( 3.9). Combining this observation with ( 3) and ( 3.12), our proposition follows. ∎

## 4. The moments of s ^ q ​ ( t) {\widehat{s}}_{q}(t) and C ⁡ ( k) C(k)

We now state our main result on computing the moments of s ^ q ​ ( t) {\widehat{s}}_{q}(t) and C ⁡ ( k) C(k).

###### Theorem 4.1.

Let q q be a prime, and ℓ \ell a natural number. Then, uniformly in the range ℓ ≤ log ⁡ q / log ⁡ log ​ q \ell\leq\sqrt{\log q}/\log\log q,

(4.1) |  | 1 q ∑ k ⁡ ( mod ​ q) C ( k) ℓ = M C ( ℓ) + O ( q − 1 / ( 20 ℓ log ℓ)), \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}C(k)^{\ell}=M_{C}(\ell)+O(q^{-1/(20\ell\log\ell)}), |  |

where

 | M C ( ℓ) = C ℓ ∑ n 1, …, n ℓ ≥ 1 b ( n 1) ⋯ b ( n ℓ) ℬ ( n 1, …, n ℓ). M_{C}(\ell)=C^{\ell}\sum_{n_{1},\ldots,n_{\ell}\geq 1}b(n_{1})\cdots b(n_{\ell}){\mathcal{B}}(n_{1},\ldots,n_{\ell}). |  |

The quantity M C ​ ( ℓ) M_{C}(\ell) equals zero for all odd ℓ \ell, and for even ℓ \ell satisfies

(4.2) |  | e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ + O ⁡ ( 1)) ≤ M C ​ ( ℓ) 1 ℓ ≤ e γ 2 ​ log ​ ℓ + O ⁡ ( 1). \frac{e^{\gamma}}{2}(\log\ell-\log\log\ell+O(1))\leq M_{C}(\ell)^{\frac{1}{\ell}}\leq\frac{e^{\gamma}}{2}\log\ell+O(1). |  |

###### Theorem 4.2.

Let q q be a prime, and ℓ \ell a natural number. Then, uniformly in ℓ \ell,

 | 1 q ∑ t ⁡ ( mod ​ q) ( π i s ^ q ( t)) ℓ = M s ( ℓ) + O ( q − 1 / ( 20 ℓ log ℓ)), \frac{1}{q}\sum_{t\,\left(\text{mod }q\right)}(\pi i{\widehat{s}}_{q}(t))^{\ell}=M_{s}(\ell)+O(q^{-1/(20\ell\log\ell)}), |  |

where

 | M s ​ ( ℓ) = ∑ n 1, …, n ℓ ≥ 1 ℬ ⁡ ( n 1, …, n ℓ) n 1 ⋯ n ℓ. M_{s}(\ell)=\sum_{n_{1},\ldots,n_{\ell}\geq 1}\frac{{\mathcal{B}}(n_{1},\ldots,n_{\ell})}{n_{1}\cdots n_{\ell}}. |  |

The quantity M s ​ ( ℓ) M_{s}(\ell) equals zero for all odd ℓ \ell, and for even ℓ \ell satisfies

 | e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ + O ⁡ ( 1)) ≤ M s ​ ( ℓ) 1 ℓ ≤ e γ 2 ​ log ​ ℓ + O ⁡ ( 1). \frac{e^{\gamma}}{2}(\log\ell-\log\log\ell+O(1))\leq M_{s}(\ell)^{\frac{1}{\ell}}\leq\frac{e^{\gamma}}{2}\log\ell+O(1). |  |

We confine ourselves to proving Theorem 4.1, and the proof of Theorem 4.2 follows along similar lines. In the rest of this section, we establish the asymptotic ( 4.1) and the upper bound in ( 4.2); the lower bound in ( 4.2) needs more work, and will be treated in the next section.

###### Proof of ( 4.1).

Since C ⁡ ( − k) = − C ⁡ ( k) C(-k)=-C(k) the odd moments of C ⁡ ( k) C(k) vanish. When ℓ \ell is odd, ℬ ⁡ ( n 1, …, n ℓ) = 0 {\mathcal{B}}(n_{1},\ldots,n_{\ell})=0 and so the quantity M C ​ ( ℓ) M_{C}(\ell) is also zero here. In what follows, we may therefore assume that ℓ \ell is an even natural number.

Let 1 ≤ B ≤ q 1\leq B\leq q be a parameter to be chosen shortly. Note that

 |  | | C ( k) ℓ − ( − C ∑ n ≤ B b ( n) ψ ( k ​ 2 ​ n ¯ q)) ℓ | \displaystyle\Big|C(k)^{\ell}-\Big(-C\sum_{n\leq B}b(n)\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big)^{\ell}\Big| |  |

 | ≤ \displaystyle\leq | | C ⁡ ( k) + C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ q) | ⋅ ∑ j = 0 ℓ − 1 | C ⁡ ( k) | j ​ | C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ q) | ℓ − 1 − j \displaystyle\Big|C(k)+C\sum_{n\leq B}b(n)\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big|\cdot\sum_{j=0}^{\ell-1}|C(k)|^{j}\Big|C\sum_{n\leq B}b(n)\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big|^{\ell-1-j} |  |

 | ≤ \displaystyle\leq | ( C 0 ​ log ⁡ q) ℓ − 1 ​ | C ⁡ ( k) + C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ q) |, \displaystyle(C_{0}\log q)^{\ell-1}\Big|C(k)+C\sum_{n\leq B}b(n)\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big|, |  |

for some absolute constant C 0 C_{0}. By Cauchy-Schwarz and Lemma 2.3,

 | 1 q ​ ∑ k ⁡ ( mod ​ q) | C ⁡ ( k) + C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ q) | ≪ B − 1 2 + ϵ. \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}\Big|C(k)+C\sum_{n\leq B}b(n)\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big|\ll B^{-\frac{1}{2}+\epsilon}. |  |

We choose B = q 1 / ℓ B=q^{1/\ell}, and (in the range ℓ ≤ log ⁡ q / log ⁡ log ​ q \ell\leq\sqrt{\log q}/\log\log q) deduce that

 | 1 q ​ ∑ k ⁡ ( mod ​ q) C ​ ( k) ℓ = 1 q ​ ∑ k ⁡ ( mod ​ q) ( C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ q)) ℓ + O ⁡ ( q − 1 4 ​ ℓ). \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}C(k)^{\ell}=\frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}\Big(C\sum_{n\leq B}b(n)\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big)^{\ell}+O(q^{-\frac{1}{4\ell}}). |  |

Expand out the main term above, replace k ⁡ ( mod ​ q) k\,\left(\text{mod }q\right) by 2 ​ k ​ ( mod ​ q) 2k\,\left(\text{mod }q\right), and appeal to Proposition 3.2 with K K there being ≤ q ( ℓ − 1) / ℓ \leq q^{(\ell-1)/\ell}. It follows that

(4.3) |  | 1 q ∑ k ⁡ ( mod ​ q) C ( k) ℓ = C ℓ ∑ n 1, …, n ℓ ≤ q 1 / ℓ b ( n 1) ⋯ b ( n ℓ) ℬ ( n 1, …, n ℓ) + O ( q − 1 4 ​ ℓ). \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}C(k)^{\ell}=C^{\ell}\sum_{n_{1},\ldots,n_{\ell}\leq q^{1/\ell}}b(n_{1})\cdots b(n_{\ell}){\mathcal{B}}(n_{1},\ldots,n_{\ell})+O(q^{-\frac{1}{4\ell}}). |  |

It remains now to bound the difference between the main term in ( 4.3) and the expression for M C ​ ( ℓ) M_{C}(\ell), which is

 | ≤ C ℓ ∑ n > q 1 / ℓ ∑ n 1 ⋯ n ℓ = n b ( n 1) ⋯ b ( n ℓ) | ℬ ( n 1, …, n ℓ) | ≤ ( C / 2) ℓ ∑ n > q 1 / ℓ ∑ n 1 ⋯ n ℓ = n b ( n 1) ⋯ b ( n ℓ) 1 sf ⁡ ( n), \leq C^{\ell}\sum_{n>q^{1/\ell}}\sum_{n_{1}\cdots n_{\ell}=n}b(n_{1})\cdots b(n_{\ell})|{\mathcal{B}}(n_{1},\ldots,n_{\ell})|\leq(C/2)^{\ell}\sum_{n>q^{1/\ell}}\sum_{n_{1}\cdots n_{\ell}=n}b(n_{1})\cdots b(n_{\ell})\frac{1}{\mathrm{sf}(n)}, |  |

where sf ⁡ ( n) \mathrm{sf}(n) is the largest squarefree divisor d d of n n that is coprime to n / d n/d. We estimate the sum above by Rankin’s trick; with α = 1 / ( 10 ​ log ⁡ ℓ) \alpha=1/(10\log\ell) the above is

 |  | ≤ ( C / 2) ℓ q − α / ℓ ∑ n = 1 ∞ ∑ n 1 ⋯ n ℓ = n b ( n 1) ⋯ b ( n ℓ) n α sf ⁡ ( n) \displaystyle\leq(C/2)^{\ell}q^{-\alpha/\ell}\sum_{n=1}^{\infty}\sum_{n_{1}\cdots n_{\ell}=n}b(n_{1})\cdots b(n_{\ell})\frac{n^{\alpha}}{\mathrm{sf}(n)} |  |

 |  | ≤ e O ⁡ ( ℓ) q − α / ℓ ∏ p ≥ 3 ( 1 + ℓ ​ p α p ⁡ ( p − 2) + ∑ j = 2 ℓ ( ℓ j) p j ​ α ( p − 2) j), \displaystyle\leq e^{O(\ell)}q^{-\alpha/\ell}\prod_{p\geq 3}\Big(1+\frac{\ell p^{\alpha}}{p(p-2)}+\sum_{j=2}^{\ell}\binom{\ell}{j}\frac{p^{j\alpha}}{(p-2)^{j}}\Big), |  |

upon recalling the definition of b ⁡ ( n) b(n). The contribution of primes p ≤ ℓ p\leq\ell to the product above is

 | ≤ ∏ 3 ≤ p ≤ ℓ ( 1 + p α p − 2) ℓ ≤ ( log ⁡ ℓ) ℓ ​ e O ⁡ ( ℓ), \leq\prod_{3\leq p\leq\ell}\Big(1+\frac{p^{\alpha}}{p-2}\Big)^{\ell}\leq(\log\ell)^{\ell}e^{O(\ell)}, |  |

while the contribution of primes p > ℓ p>\ell to the product above is

 | ≪ ∏ p > ℓ exp ⁡ ( O ⁡ ( ℓ 2 ​ p 2 ​ α p 2)) = e O ⁡ ( ℓ). \ll\prod_{p>\ell}\exp\Big(O\Big(\frac{\ell^{2}p^{2\alpha}}{p^{2}}\Big)\Big)=e^{O(\ell)}. |  |

We conclude that the difference between the main term in ( 4.3) and the expression for M C ​ ( ℓ) M_{C}(\ell) is

 | ≪ ( log ℓ) ℓ e O ⁡ ( ℓ) q − α / ℓ ≪ q − 1 / ( 20 ℓ log ℓ), \ll(\log\ell)^{\ell}e^{O(\ell)}q^{-\alpha/\ell}\ll q^{-1/(20\ell\log\ell)}, |  |

completing the proof of ( 4.1). ∎

###### Proof of the upper bound in ( 4.2).

Note that

 | M C ​ ( ℓ) \displaystyle M_{C}(\ell) | ≤ C ℓ ∑ n 1, …, n ℓ b ( n 1) ⋯ b ( n ℓ) | ℬ ( n 1, …, n ℓ) | ≤ ( C / 2) ℓ ∑ n 1, …, n ℓ b ( n 1) ⋯ b ( n ℓ) sf ⁡ ( n) \displaystyle\leq C^{\ell}\sum_{n_{1},\ldots,n_{\ell}}b(n_{1})\cdots b(n_{\ell})|{\mathcal{B}}(n_{1},\ldots,n_{\ell})|\leq(C/2)^{\ell}\sum_{n_{1},\ldots,n_{\ell}}\frac{b(n_{1})\cdots b(n_{\ell})}{\mathrm{sf}(n)} |  |

 |  | ≤ ( C / 2) ℓ ​ ∏ p ≥ 3 ( 1 + ℓ p ⁡ ( p − 2) + ∑ j = 2 ℓ ( ℓ j) ​ 1 ( p − 2) j). \displaystyle\leq(C/2)^{\ell}\prod_{p\geq 3}\Big(1+\frac{\ell}{p(p-2)}+\sum_{j=2}^{\ell}\binom{\ell}{j}\frac{1}{(p-2)^{j}}\Big). |  |

The contribution of primes p ≤ ℓ p\leq\ell is

 | ≤ ∏ 3 ≤ p ≤ ℓ ( 1 + 1 p − 2) ℓ = ( ∏ 3 ≤ p ≤ ℓ ( 1 − 1 ( p − 1) 2) − 1 ​ ( 1 − 1 p) − 1) ℓ = C − ℓ ​ ( e γ ​ log ⁡ ℓ + O ⁡ ( 1)) ℓ, \leq\prod_{3\leq p\leq\ell}\Big(1+\frac{1}{p-2}\Big)^{\ell}=\Big(\prod_{3\leq p\leq\ell}\Big(1-\frac{1}{(p-1)^{2}}\Big)^{-1}\Big(1-\frac{1}{p}\Big)^{-1}\Big)^{\ell}=C^{-\ell}(e^{\gamma}\log\ell+O(1))^{\ell}, |  |

upon using Mertens’s theorem. The contribution of primes p > ℓ p>\ell is

 | exp ⁡ ( ∑ p > ℓ O ⁡ ( ℓ 2 p 2)) = exp ⁡ ( O ⁡ ( ℓ log ⁡ ℓ)), \exp\Big(\sum_{p>\ell}O\Big(\frac{\ell^{2}}{p^{2}}\Big)\Big)=\exp\Big(O\Big(\frac{\ell}{\log\ell}\Big)\Big), |  |

and so the upper bound in ( 4.2) follows. ∎

## 5. Completing the proof of Theorem 4.1: Proof of the lower bound in ( 4.2)

To obtain the lower bound in ( 4.2) we take an indirect approach, working with a continuous model that has the same moments as C ⁡ ( k) C(k). Let B B be a positive integer, and let L ⁡ ( B) L(B) denote the least common multiple of the natural numbers n ≤ B n\leq B. For a real number x x, define

 | C ⁡ ( x, B) = C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( x / n). C(x;B)=C\sum_{n\leq B}b(n)\psi(x/n). |  |

It follows readily that

 | 1 L ⁡ ( B) ∫ 0 L ⁡ ( B) C ( x; B) ℓ d x = C ℓ ∑ n 1, …, n ℓ ≤ B b ( n 1) ⋯ b ( n ℓ) ℬ ( n 1, …, n ℓ), \frac{1}{L(B)}\int_{0}^{L(B)}C(x;B)^{\ell}dx=C^{\ell}\sum_{n_{1},\ldots,n_{\ell}\leq B}b(n_{1})\cdots b(n_{\ell}){\mathcal{B}}(n_{1},\ldots,n_{\ell}), |  |

so that

(5.1) |  | M C ​ ( ℓ) = lim B → ∞ 1 L ⁡ ( B) ​ ∫ 0 L ⁡ ( B) C ​ ( x, B) ℓ ​ 𝑑 x. M_{C}(\ell)=\lim_{B\to\infty}\frac{1}{L(B)}\int_{0}^{L(B)}C(x;B)^{\ell}dx. |  |

We shall obtain a lower bound for the right side of ( 5.1); naturally, we may assume that ℓ \ell is even and large.

Suppose that B > ℓ B>\ell, and put ℓ 0 = ℓ / log ⁡ ℓ \ell_{0}=\ell/\log\ell. Let ℐ {\mathcal{I}} denote the subset of [0, L ⁡ ( B)] [0,L(B)] consisting of points x = k ​ L ​ ( ℓ 0) − y x=kL(\ell_{0})-y with 1 ≤ k ≤ L ⁡ ( B) / L ⁡ ( ℓ 0) 1\leq k\leq L(B)/L(\ell_{0}), and 0 < y ≤ 1 / 10 0<y\leq 1/10. Let ψ + ​ ( t) = ψ ​ ( t) \psi^{+}(t)=\psi(t) whenever t t is not an integer, and ψ + ​ ( t) = 1 / 2 \psi^{+}(t)=1/2 when t t is an integer. Then for x = k ​ L ​ ( ℓ 0) − y ∈ ℐ x=kL(\ell_{0})-y\in{\mathcal{I}} note that

 | C ⁡ ( x, B) = C ​ ∑ n ≤ B b ⁡ ( n) ​ ψ ​ ( ( k ​ L ​ ( ℓ 0) − y) / n) = C ​ ∑ n ≤ B b ⁡ ( n) ​ ( ψ + ​ ( k ​ L ​ ( ℓ 0) / n) − y / n). C(x;B)=C\sum_{n\leq B}b(n)\psi((kL(\ell_{0})-y)/n)=C\sum_{n\leq B}b(n)\Big(\psi^{+}(kL(\ell_{0})/n)-y/n\Big). |  |

Since, for n ≤ B n\leq B,

 | ∑ k = 1 L ⁡ ( B) / L ⁡ ( ℓ 0) ψ + ​ ( k ​ L ​ ( ℓ 0) n) = 1 2 ​ L ⁡ ( B) L ⁡ ( ℓ 0) ​ ( n, L ⁡ ( ℓ 0)) n, \sum_{k=1}^{L(B)/L(\ell_{0})}\psi^{+}\Big(\frac{kL(\ell_{0})}{n}\Big)=\frac{1}{2}\frac{L(B)}{L(\ell_{0})}\frac{(n,L(\ell_{0}))}{n}, |  |

it follows that (note | ℐ | = L ⁡ ( B) / ( 10 ​ L ​ ( ℓ 0)) |{\mathcal{I}}|=L(B)/(10L(\ell_{0})))

 | 1 | ℐ | ​ ∫ ℐ C ⁡ ( x, B) ​ 𝑑 x = C 2 ​ ∑ n ≤ B b ⁡ ( n) ​ ( n, L ⁡ ( ℓ 0)) − 1 / 20 n, \frac{1}{|{\mathcal{I}}|}\int_{\mathcal{I}}C(x;B)dx=\frac{C}{2}\sum_{n\leq B}b(n)\frac{(n,L(\ell_{0}))-1/20}{n}, |  |

and therefore by Hölder’s inequality that

 | 1 L ⁡ ( B) ​ ∫ 0 B C ​ ( x, B) ℓ ​ 𝑑 x ≥ 1 10 ​ L ​ ( ℓ 0) ​ 1 | ℐ | ​ ∫ ℐ C ​ ( x, B) ℓ ​ 𝑑 x ≥ 1 10 ​ L ​ ( ℓ 0) ​ ( C 2 ​ ∑ n ≤ B b ⁡ ( n) ​ ( n, L ⁡ ( ℓ 0)) − 1 / 20 n) ℓ. \frac{1}{L(B)}\int_{0}^{B}C(x,B)^{\ell}dx\geq\frac{1}{10L(\ell_{0})}\frac{1}{|{\mathcal{I}}|}\int_{\mathcal{I}}C(x;B)^{\ell}dx\geq\frac{1}{10L(\ell_{0})}\Big(\frac{C}{2}\sum_{n\leq B}b(n)\frac{(n,L(\ell_{0}))-1/20}{n}\Big)^{\ell}. |  |

Now letting B → ∞ B\to\infty, we find by ( 5.1) that

 | M C ​ ( ℓ) ≥ 1 10 ​ L ​ ( ℓ 0) ​ ( C 2 ​ ∑ n = 1 ∞ b ⁡ ( n) ​ ( n, L ⁡ ( ℓ 0)) n + O ⁡ ( 1)) ℓ ≥ e − O ⁡ ( ℓ 0) ​ ( C 2 ​ ∏ 3 ≤ p ≤ ℓ 0 ( 1 + 1 p − 2) + O ⁡ ( 1)) ℓ, M_{C}(\ell)\geq\frac{1}{10L(\ell_{0})}\Big(\frac{C}{2}\sum_{n=1}^{\infty}\frac{b(n)(n,L(\ell_{0}))}{n}+O(1)\Big)^{\ell}\geq e^{-O(\ell_{0})}\Big(\frac{C}{2}\prod_{3\leq p\leq\ell_{0}}\Big(1+\frac{1}{p-2}\Big)+O(1)\Big)^{\ell}, |  |

upon using the prime number theorem to estimate L ⁡ ( ℓ 0) L(\ell_{0}), and recalling the definition of b b. Now

 | C 2 ​ ∏ 3 ≤ p ≤ ℓ 0 ( 1 + 1 p − 2) = ∏ 3 ≤ p ≤ ℓ 0 ( 1 − 1 p) − 1 ​ ( 1 + O ⁡ ( 1 ℓ 0)) = e γ 2 ​ log ⁡ ℓ 0 + O ⁡ ( 1), \frac{C}{2}\prod_{3\leq p\leq\ell_{0}}\Big(1+\frac{1}{p-2}\Big)=\prod_{3\leq p\leq\ell_{0}}\Big(1-\frac{1}{p}\Big)^{-1}\Big(1+O\Big(\frac{1}{\ell_{0}}\Big)\Big)=\frac{e^{\gamma}}{2}\log\ell_{0}+O(1), |  |

and therefore the lower bound in ( 4.2) follows.

## 6. Proof of Theorem 1.1

###### Proof of Part 1.

Theorem 4.1 shows that all the moments of C ⁡ ( k) C(k) exist, and do not grow too rapidly. The moment generating function ∑ ℓ = 0 ∞ x ℓ ​ M C ​ ( ℓ) / ℓ! \sum_{\ell=0}^{\infty}x^{\ell}M_{C}(\ell)/\ell! converges for all x x, and therefore the sequence of moments M C ​ ( ℓ) M_{C}(\ell) uniquely determines a distribution, which is the limiting distribution for C ⁡ ( k) C(k). Since C ⁡ ( k) = − C ⁡ ( − k) C(k)=-C(-k), the limiting distribution is clearly symmetric around 0 0.

To gain an understanding of this limiting distribution, and to establish its continuity, it is helpful to think of the continuous model C ⁡ ( x, B) C(x;B) discussed in Section 5. Consider the characteristic function (that is, Fourier transform) of C ⁡ ( x, B) C(x;B); namely

 | 𝔼 ⁡ ( e i ​ t ​ C ​ ( x, B)) = 1 L ⁡ ( B) ​ ∫ 0 L ⁡ ( B) e i ​ t ​ C ​ ( x, B) ​ 𝑑 x. {\mathbb{E}}(e^{itC(x,B)})=\frac{1}{L(B)}\int_{0}^{L(B)}e^{itC(x,B)}dx. |  |

Omit the measure zero set of integers x x, and write x = k − y x=k-y with 1 ≤ k ≤ L ⁡ ( B) 1\leq k\leq L(B) and 0 < y < 1 0<y<1. Then, with ψ + \psi^{+} as in Section 5 and C + ​ ( x, B) = C ​ ∑ b ≤ B b ⁡ ( n) ​ ψ + ​ ( x / b) C^{+}(x;B)=C\sum_{b\leq B}b(n)\psi^{+}(x/b), we have C ⁡ ( x, B) = C + ​ ( k, B) − y ​ ∑ n ≤ B b ⁡ ( n) / n C(x;B)=C^{+}(k;B)-y\sum_{n\leq B}b(n)/n, and so

(6.1) |  | 1 L ⁡ ( B) ∫ 0 L ⁡ ( B) e i ​ t ​ C ​ ( x, B) d x = 1 L ⁡ ( B) ∑ k = 1 L ⁡ ( B) e i ​ t ​ C + ​ ( k, B) ∫ 0 1 e − i t y ∑ n ≤ B b ( n) / n d y ≪ 1 1 + | t |. \frac{1}{L(B)}\int_{0}^{L(B)}e^{itC(x,B)}dx=\frac{1}{L(B)}\sum_{k=1}^{L(B)}e^{itC^{+}(k,B)}\int_{0}^{1}e^{-ity\sum_{n\leq B}b(n)/n}dy\ll\frac{1}{1+|t|}. |  |

Given an interval I = ( α − ϵ, α + ϵ) I=(\alpha-\epsilon,\alpha+\epsilon) with ϵ < 1 / 2 \epsilon<1/2, we can readily find a majorant Ψ ⁡ ( x) \Psi(x) of the indicator function of I I, with | Ψ ^ ​ ( x) | ≪ ϵ / ( 1 + ( ϵ ​ x) 2) |{\widehat{\Psi}}(x)|\ll\epsilon/(1+(\epsilon x)^{2}). For example take Ψ ⁡ ( x) = max ⁡ ( 2 − | x − α | / ϵ, 0) \Psi(x)=\max(2-|x-\alpha|/\epsilon,0), which is a relative of the Fejer kernel. Then by Fourier inversion

 | 1 L ⁡ ( B) ​ ∫ x ∈ [0, L ⁡ ( B)] C ⁡ ( x, B) ∈ I 𝑑 x \displaystyle\frac{1}{L(B)}\int_{\begin{subarray}{c}x\in[0,L(B)]\\ C(x,B)\in I\end{subarray}}dx | ≤ 1 L ⁡ ( B) ​ ∫ 0 L ⁡ ( B) Ψ ⁡ ( C ⁡ ( x, B)) ​ 𝑑 x \displaystyle\leq\frac{1}{L(B)}\int_{0}^{L(B)}\Psi(C(x,B))dx |  |

 |  | = ∫ − ∞ ∞ Ψ ^ ​ ( t) ​ 𝔼 ​ ( e i ​ t ​ C ​ ( x, B)) ​ 𝑑 t ≪ ∫ − ∞ ∞ 1 1 + | t | ​ ϵ 1 + ( ϵ ​ t) 2 ​ 𝑑 t ≪ ϵ ​ log ⁡ ( 1 / ϵ). \displaystyle=\int_{-\infty}^{\infty}{\widehat{\Psi}}(t){\mathbb{E}}(e^{itC(x,B)})dt\ll\int_{-\infty}^{\infty}\frac{1}{1+|t|}\frac{\epsilon}{1+(\epsilon t)^{2}}dt\ll\epsilon\log(1/\epsilon). |  |

Therefore C ⁡ ( x, B) C(x,B) has a continuous distribution, and the continuity is uniform in B B, so that letting B → ∞ B\to\infty, we conclude that the limiting distribution for C ⁡ ( k) C(k) is also continuous. ∎

###### Proof of Parts 2 and 3.

Since Part 3 follows upon taking x = ( 1 2 − ϵ) ​ log ⁡ log ​ q x=(\frac{1}{2}-\epsilon)\log\log q in Part 2, it is enough to prove Part 2. For any even ℓ ≤ log ⁡ q / log ⁡ log ​ q \ell\leq\sqrt{\log q}/\log\log q, we see using Theorem 4.1 that

 | 1 q ​ #​ { k ⁡ ( mod ​ q): C ⁡ ( k) ≥ e γ 2 ​ x } ≤ ( e γ 2 ​ x) − ℓ ​ ( M C ​ ( ℓ) + o ⁡ ( 1)) ≪ ( log ⁡ ℓ + O ⁡ ( 1) x) ℓ. \frac{1}{q}\#\{k\,\left(\text{mod }q\right):C(k)\geq\frac{e^{\gamma}}{2}x\}\,\,\leq\,\,\Big(\frac{e^{\gamma}}{2}x\Big)^{-\ell}(M_{C}(\ell)+o(1))\,\,\ll\,\,\Big(\frac{\log\ell+O(1)}{x}\Big)^{\ell}. |  |

Choosing ℓ \ell to be an even integer around A ​ e x Ae^{x} for a suitably small positive constant A A, the upper bound in Part 2 follows.

To establish the lower bound in Part 2, note that for even ℓ ≤ log ⁡ q / ( 2 ​ log ⁡ log ⁡ q) \ell\leq\sqrt{\log q}/(2\log\log q), we have by Theorem 4.1

(6.2) |  | ( e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ + O ⁡ ( 1))) ℓ ≪ 1 q ​ ∑ k ⁡ ( mod ​ q) C ​ ( k) ℓ. \Big(\frac{e^{\gamma}}{2}(\log\ell-\log\log\ell+O(1))\Big)^{\ell}\ll\frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}C(k)^{\ell}. |  |

The contribution from terms k k with | C ⁡ ( k) | ≤ e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ − A) |C(k)|\leq\frac{e^{\gamma}}{2}(\log\ell-\log\log\ell-A) for a suitably large constant A A is clearly negligible compared to the right side of ( 6.2). The contribution from terms k k with | C ⁡ ( k) | ≥ e γ 2 ​ ( log ⁡ ℓ + log ⁡ log ⁡ ℓ + A) |C(k)|\geq\frac{e^{\gamma}}{2}(\log\ell+\log\log\ell+A) for a suitably large constant A A is

 |  | ≤ ( e γ 2 ​ ( log ⁡ ℓ + log ⁡ log ⁡ ℓ + A)) − ℓ ​ 1 q ​ ∑ k ⁡ ( mod ​ q) C ​ ( k) 2 ​ ℓ \displaystyle\leq\Big(\frac{e^{\gamma}}{2}(\log\ell+\log\log\ell+A)\Big)^{-\ell}\frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}C(k)^{2\ell} |  |

 |  | ≪ ( e γ 2 ​ ( log ⁡ ℓ + log ⁡ log ⁡ ℓ + A)) − ℓ ​ ( e γ 2 ​ log ​ ℓ + O ⁡ ( 1)) 2 ​ ℓ, \displaystyle\ll\Big(\frac{e^{\gamma}}{2}(\log\ell+\log\log\ell+A)\Big)^{-\ell}\Big(\frac{e^{\gamma}}{2}\log\ell+O(1)\Big)^{2\ell}, |  |

upon using Theorem 4.1 to estimate the 2 ​ ℓ 2\ell -th moment. If A A is suitably large, then this too is negligible in comparison to the right side of ( 6.2). Therefore it is the terms with | C ⁡ ( k) | |C(k)| lying between e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ − A) \frac{e^{\gamma}}{2}(\log\ell-\log\log\ell-A) and e γ 2 ​ ( log ⁡ ℓ + log ⁡ log ⁡ ℓ + A) \frac{e^{\gamma}}{2}(\log\ell+\log\log\ell+A) that account for the bulk of the contribution to ( 6.2), and so

 |  | ( e γ 2 ​ ( log ⁡ ℓ + log ⁡ log ⁡ ℓ + A)) ℓ ​ 1 q ​ #​ { k: | C ⁡ ( k) | ≥ e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ − A) } \displaystyle\Big(\frac{e^{\gamma}}{2}(\log\ell+\log\log\ell+A)\Big)^{\ell}\,\,\frac{1}{q}\#\{k:|C(k)|\geq\tfrac{e^{\gamma}}{2}(\log\ell-\log\log\ell-A)\} |  |

 | ≫ \displaystyle\gg | ( e γ 2 ​ ( log ⁡ ℓ − log ⁡ log ⁡ ℓ + O ⁡ ( 1))) ℓ. \displaystyle\Big(\frac{e^{\gamma}}{2}(\log\ell-\log\log\ell+O(1))\Big)^{\ell}. |  |

Choosing ℓ \ell of size x ​ e x xe^{x}, the lower bound in Part 2 follows. ∎

###### Proof of Part 4.

First suppose that C ⁡ ( k) C(k) is negative. From [9] (Chapter 1, page 6) we recall that for each natural number K K there is a trigonometric polynomial

 | B K ​ ( x) = 1 2 ​ ( K + 1) + ∑ 1 ≤ | j | ≤ K c j ​ e ​ ( j ​ x) B_{K}(x)=\frac{1}{2(K+1)}+\sum_{1\leq|j|\leq K}c_{j}e(jx) |  |

with c j ≪ 1 / j c_{j}\ll 1/j, such that B K ​ ( x) ≥ ψ ⁡ ( x) B_{K}(x)\geq\psi(x) for all x x. Using Lemma 2.2 with N = q 8 N=q^{8} we obtain

 | 0 ≤ − C ⁡ ( k) = C ​ ∑ n ≤ q 8 ( n, q) = 1 b ⁡ ( n) ​ ψ ​ ( k ​ 2 ​ n ¯ / q) + O ⁡ ( 1) ≤ C ​ ∑ n ≤ q 8 b ⁡ ( n) ​ B K ​ ( k ​ 2 ​ n ¯ / q) + O ⁡ ( 1). 0\leq-C(k)=C\sum_{\begin{subarray}{c}n\leq q^{8}\\ (n,q)=1\end{subarray}}b(n)\psi(k\overline{2n}/q)+O(1)\leq C\sum_{n\leq q^{8}}b(n)B_{K}(k\overline{2n}/q)+O(1). |  |

Thus, for some positive constant A A,

(6.3) |  | − C ⁡ ( k) ≤ A ⁡ ( 1 + 1 K + 1 ​ ∑ n ≤ q 8 b ⁡ ( n) + ∑ 1 ≤ | j | ≤ K 1 j ​ | ∑ n ≤ q 8 ( n, q) = 1 b ⁡ ( n) ​ e ​ ( k ​ j ​ 2 ​ n ¯ q) |). -C(k)\leq A\Big(1+\frac{1}{K+1}\sum_{n\leq q^{8}}b(n)+\sum_{1\leq|j|\leq K}\frac{1}{j}\Big|\sum_{\begin{subarray}{c}n\leq q^{8}\\ (n,q)=1\end{subarray}}b(n)e\Big(\frac{kj\overline{2n}}{q}\Big)\Big|\Big). |  |

At this stage, we need the following result which follows from work of Bourgain and Garaev [2] (refining earlier work of Karatsuba [5]; see also Korolev [6]).

###### Lemma 6.1.

Let q q be a prime, and a a be any integer coprime to q q. Then for all N ≥ 1 N\geq 1

 | | ∑ n ≤ N ( n, q) = 1 1 n ​ e ​ ( a ​ n ¯ q) | ≪ ( log ⁡ q) 2 3 ​ ( log ⁡ log ⁡ q) 2. \Big|\sum_{\begin{subarray}{c}n\leq N\\ (n,q)=1\end{subarray}}\frac{1}{n}e\Big(\frac{a\overline{n}}{q}\Big)\Big|\ll(\log q)^{\frac{2}{3}}(\log\log q)^{2}. |  |

###### Proof.

Theorem 16 of Bourgain and Garaev [2] gives

 | | ∑ n ≤ x e ⁡ ( a ​ n ¯ q) | ≪ x ( log ⁡ x) 3 2 ​ log ⁡ q ​ ( log ⁡ log ⁡ q) 3. \Big|\sum_{n\leq x}e\Big(\frac{a\overline{n}}{q}\Big)\Big|\ll\frac{x}{(\log x)^{\frac{3}{2}}}\log q(\log\log q)^{3}. |  |

Partial summation using this bound for x ≥ exp ⁡ ( ( log ⁡ q) 2 3 ​ ( log ⁡ log ⁡ q) 2) x\geq\exp((\log q)^{\frac{2}{3}}(\log\log q)^{2}), and the trivial bound (that the sum is at most x x) for smaller x x yields the lemma. ∎

Returning to ( 6.3), take there K = ⌊ log ⁡ q ⌋ K=\lfloor\log q\rfloor. Then the right side of ( 6.3) is (recalling the definition b ⁡ ( n) = ∑ u ​ v = n a ⁡ ( u) / v b(n)=\sum_{uv=n}a(u)/v)

 | ≪ 1 + ∑ j ≤ K 1 j ​ ∑ u ≤ q 8 ( u, q) = 1 | a ⁡ ( u) | | ∑ v ≤ q 8 / u ( v, q) = 1 1 v ​ e ​ ( k ​ j ​ 2 ​ u ​ v ¯ q) | ≪ ( log ⁡ q) 2 3 ​ ( log ⁡ log ⁡ q) 3, \ll 1+\sum_{j\leq K}\frac{1}{j}\sum_{\begin{subarray}{c}u\leq q^{8}\\ (u,q)=1\end{subarray}}|a(u)|\Big|\sum_{\begin{subarray}{c}v\leq q^{8}/u\\ (v,q)=1\end{subarray}}\frac{1}{v}e\Big(\frac{kj\overline{2uv}}{q}\Big)\Big|\ll(\log q)^{\frac{2}{3}}(\log\log q)^{3}, |  |

using Lemma 6.1 and since ∑ n | a ⁡ ( n) | ≪ 1 \sum_{n}|a(n)|\ll 1. This proves that − C ⁡ ( k) ≤ A ​ ( log ⁡ q) 2 3 ​ ( log ⁡ log ⁡ q) 3 -C(k)\leq A(\log q)^{\frac{2}{3}}(\log\log q)^{3}, which is the desired bound in the case C ⁡ ( k) C(k) negative. Arguing similarly with a minorant for ψ ⁡ ( x) \psi(x) instead of a majorant, leads to the same bound for C ⁡ ( k) C(k) in the case when it is positive. ∎

###### Proof of Part 5.

Applying Lemma 2.3 we find that

 | 1 q ​ ∑ k ⁡ ( mod ​ q) | C ⁡ ( k) − C ⁡ ( k + m) | 2 ≪ B − 1 + ϵ + 1 q ​ ∑ k ⁡ ( mod ​ q) | ∑ n ≤ B b ⁡ ( n) ​ ( ψ ⁡ ( ( k + m) ​ 2 ​ n ¯ q) − ψ ⁡ ( k ​ 2 ​ n ¯ q)) | 2. \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}|C(k)-C(k+m)|^{2}\ll B^{-1+\epsilon}+\frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}\Big|\sum_{n\leq B}b(n)\Big(\psi\Big(\frac{(k+m)\overline{2n}}{q}\Big)-\psi\Big(\frac{k\overline{2n}}{q}\Big)\Big)\Big|^{2}. |  |

Using Cauchy-Schwarz the second term above is

(6.4) |  | ≪ 1 q ​ ( ∑ n ≤ B b ⁡ ( n)) ​ ∑ n ≤ B b ⁡ ( n) ​ ∑ k ⁡ ( mod ​ q) ( ψ ⁡ ( k + m ​ 2 ​ n ¯ q) − ψ ⁡ ( k q)) 2, \ll\frac{1}{q}\Big(\sum_{n\leq B}b(n)\Big)\sum_{n\leq B}b(n)\sum_{k\,\left(\text{mod }q\right)}\Big(\psi\Big(\frac{k+m\overline{2n}}{q}\Big)-\psi\Big(\frac{k}{q}\Big)\Big)^{2}, |  |

where in the inner sum we replaced k k by 2 ​ k ​ n 2kn. Since | ψ ⁡ ( ( k + a) / q) − ψ ⁡ ( k / q) | ≤ | a | / q |\psi((k+a)/q)-\psi(k/q)|\leq|a|/q unless there is an integer between k / q k/q and ( k + a) / q (k+a)/q, we may check that

 | 1 q ​ ∑ k ⁡ ( mod ​ q) ( ψ ⁡ ( k + a q) − ψ ⁡ ( k q)) 2 ≪ a q. \frac{1}{q}\sum_{k\,\left(\text{mod }q\right)}\Big(\psi\Big(\frac{k+a}{q}\Big)-\psi\Big(\frac{k}{q}\Big)\Big)^{2}\ll\frac{a}{q}. |  |

Since m m is a multiple of all numbers B B (and recalling that b ⁡ ( n) = 0 b(n)=0 unless n n is odd), we may write m ​ 2 ​ n ¯ = q ​ r + a m\overline{2n}=qr+a with a = m / ( 2 ​ n) a=m/(2n). Therefore the quantity in ( 6.4) is

 | ≪ ( log ⁡ B) ​ ∑ n ≤ B m n ​ q ≪ m q ​ log ⁡ B, \ll(\log B)\sum_{n\leq B}\frac{m}{nq}\ll\frac{m}{q}\log B, |  |

completing our proof. ∎

## 7. Proof of Theorem 1.3

As in the proofs of Theorems 1.1 and 1.2, the main result is to compute the moments of R ~ ​ ( u) \widetilde{R}(u). The proof of Theorem 1.3 then follows in exactly the same way as the corresponding parts of Theorem 1.1.

###### Theorem 7.1.

There is a positive number c < 1 c<1 such that uniformly for all natural numbers ℓ \ell in the range ℓ ≤ c 9 ​ log ⁡ y / log ⁡ log ​ y \ell\leq\frac{c}{9}{\sqrt{\log y}}/{\log\log y}, we have

 | 1 y ​ ∫ 0 y R ~ ​ ( u) ℓ ​ 𝑑 u = M R ​ ( ℓ) + O ⁡ ( exp ⁡ ( − c 8 ​ log ⁡ y)), \frac{1}{y}\int_{0}^{y}\widetilde{R}(u)^{\ell}\,du=M_{R}(\ell)+O\Big(\exp\Big(-\frac{c}{8}\sqrt{\log y}\Big)\Big), |  |

where

 | M R ​ ( ℓ) = ∑ n 1, …, n ℓ μ ⁡ ( n 1) ​ … ​ μ ​ ( n ℓ) n 1 ​ … ​ n ℓ ​ ℬ ​ ( n 1, …, n ℓ). M_{R}(\ell)=\sum_{n_{1},\dots,n_{\ell}}\frac{\mu(n_{1})\dots\mu(n_{\ell})}{n_{1}\dots n_{\ell}}\mathcal{B}(n_{1},\dots,n_{\ell}). |  |

For odd ℓ \ell, M R ​ ( ℓ) = 0 M_{R}(\ell)=0, while M R ​ ( 2) = 1 / 2 ​ π 2 M_{R}(2)=1/2\pi^{2} and for even ℓ ≥ 4 \ell\geq 4 we have

 | M R ​ ( ℓ) ≤ ( 3 ​ e γ π 2 ​ log ⁡ ℓ + O ⁡ ( 1)) ℓ. M_{R}(\ell)\leq\Big(\frac{3e^{\gamma}}{\pi^{2}}\log\ell+O(1)\Big)^{\ell}. |  |

We begin with a lemma, which will allow us to truncate R ~ ​ ( u) {\widetilde{R}}(u) by a short sum of sawtooth functions.

###### Lemma 7.2.

For all 1 ≤ N ≤ y 1\leq N\leq y we have

 | ∑ N < n 1, n 2 ≤ 2 ​ N | 1 y ​ ∫ 0 y ψ ⁡ ( x / n 1) ​ ψ ​ ( x / n 2) ​ 𝑑 x | ≪ ( log ⁡ y) 2 ​ ( N + N 2 ​ N y). \sum_{N<n_{1},n_{2}\leq 2N}\Big|\frac{1}{y}\int_{0}^{y}\psi(x/n_{1})\psi(x/n_{2})dx\Big|\ll(\log y)^{2}\Big(N+N^{2}\frac{\sqrt{N}}{\sqrt{y}}\Big). |  |

###### Proof.

Let K ≥ 2 K\geq 2 be a parameter to be chosen shortly, and let ψ K ​ ( x) \psi_{K}(x) be as in ( 3.6). First note that

 | 1 y ​ ∫ 0 y | ψ ⁡ ( x / n 1) ​ ψ ​ ( x / n 2) − ψ K ​ ( x / n 1) ​ ψ K ​ ( x / n 2) | ​ 𝑑 x ≤ 1 y ​ ∫ 0 y ∑ j = 1 2 | ψ ⁡ ( x / n j) − ψ K ​ ( x / n j) | ​ 𝑑 x ≪ 1 K, \frac{1}{y}\int_{0}^{y}|\psi(x/n_{1})\psi(x/n_{2})-\psi_{K}(x/n_{1})\psi_{K}(x/n_{2})|dx\leq\frac{1}{y}\int_{0}^{y}\sum_{j=1}^{2}|\psi(x/n_{j})-\psi_{K}(x/n_{j})|dx\ll\frac{1}{K}, |  |

upon using ( 3.8), and since n 1 n_{1} and n 2 n_{2} are at most N ≤ y N\leq y. Next, from the Fourier expansion of ψ K \psi_{K} (see ( 3.6)) it follows that

 | 1 y ​ | ∫ 0 y ψ K ​ ( x / n 1) ​ ψ K ​ ( x / n 2) ​ 𝑑 x | \displaystyle\frac{1}{y}\Big|\int_{0}^{y}\psi_{K}(x/n_{1})\psi_{K}(x/n_{2})dx\Big| | ≪ ∑ 0 < | k 1 |, | k 2 | ≤ K 1 | k 1 ​ k 2 | ​ | 1 y ​ ∫ 0 y e ⁡ ( x ⁡ ( k 1 n 1 + k 2 n 2)) ​ 𝑑 x | \displaystyle\ll\sum_{0<|k_{1}|,|k_{2}|\leq K}\frac{1}{|k_{1}k_{2}|}\Big|\frac{1}{y}\int_{0}^{y}e\Big(x\Big(\frac{k_{1}}{n_{1}}+\frac{k_{2}}{n_{2}}\Big)\Big)dx\Big| |  |

 |  | ≪ ∑ 0 < | k 1 |, | k 2 | ≤ K 1 | k 1 ​ k 2 | ​ min ⁡ ( 1, 1 y ​ | k 1 / n 1 + k 2 / n 2 |). \displaystyle\ll\sum_{0<|k_{1}|,|k_{2}|\leq K}\frac{1}{|k_{1}k_{2}|}\min\Big(1,\frac{1}{y|k_{1}/n_{1}+k_{2}/n_{2}|}\Big). |  |

From these two estimates it follows that the sum to be bounded is

 | ≪ N 2 K + ∑ 0 < | k 1 |, | k 2 | ≤ K 1 | k 1 ​ k 2 | ​ ∑ N < n 1, n 2 ≤ 2 ​ N min ⁡ ( 1, 1 y ​ | k 1 / n 1 + k 2 / n 2 |). \ll\frac{N^{2}}{K}+\sum_{0<|k_{1}|,|k_{2}|\leq K}\frac{1}{|k_{1}k_{2}|}\sum_{N<n_{1},n_{2}\leq 2N}\min\Big(1,\frac{1}{y|k_{1}/n_{1}+k_{2}/n_{2}|}\Big). |  |

To estimate the sum above, we split the terms into two groups: those with | k 1 / n 1 + k 2 / n 2 | ≥ K / y |k_{1}/n_{1}+k_{2}/n_{2}|\geq K/y and those terms with | k 1 / n 1 + k 2 / n 2 | < K / y |k_{1}/n_{1}+k_{2}/n_{2}|<K/y. The first group contributes

 | ≪ N 2 K ​ ∑ 0 < | k 1 |, | k 2 | ≤ K 1 | k 1 ​ k 2 | ​ 1 | k 1 ​ k 2 | ≪ N 2 K ​ ( log ⁡ K) 2. \ll\frac{N^{2}}{K}\sum_{0<|k_{1}|,|k_{2}|\leq K}\frac{1}{|k_{1}k_{2}|}\frac{1}{|k_{1}k_{2}|}\ll\frac{N^{2}}{K}(\log K)^{2}. |  |

Terms in the second group only exist for k 1 k_{1} and k 2 k_{2} of opposite sign, and here | k 1 ​ n 2 + k 2 ​ n 1 | ≪ K ​ N 2 / y |k_{1}n_{2}+k_{2}n_{1}|\ll KN^{2}/y, so that if k 1 k_{1}, n 1 n_{1}, and k 2 k_{2} are fixed, then n 2 n_{2} has ≪ 1 + K ​ N 2 / y \ll 1+KN^{2}/y choices. Therefore the second group contributes

 | ≪ ( 1 + K ​ N 2 y) ​ N ​ ∑ 0 < | k 1 |, | k 2 | ≤ K 1 | k 1 ​ k 2 | ≪ ( log ⁡ K) 2 ​ N ​ ( 1 + K ​ N 2 y). \ll\Big(1+\frac{KN^{2}}{y}\Big)N\sum_{0<|k_{1}|,|k_{2}|\leq K}\frac{1}{|k_{1}k_{2}|}\ll(\log K)^{2}N\Big(1+\frac{KN^{2}}{y}\Big). |  |

Choosing K = 2 ​ ⌈ y / N ⌉ K=2\lceil\sqrt{y/N}\rceil, the lemma follows. ∎

###### Proof of Theorem 7.1.

From Theorem 1 and Lemma 1 of [8] (but beware of the changes in notation, especially that his saw tooth function differs from ours in sign) it follows that with N = y ​ exp ⁡ ( − c ​ log ⁡ y) N=y\exp(-c\sqrt{\log y}) for a suitable positive constant c < 1 c<1, one has

 | R ~ ( u) = − ∑ n ≤ N μ ⁡ ( n) n ψ ( u / n) + O ( exp ( − c log ⁡ y)), {\widetilde{R}}(u)=-\sum_{n\leq N}\frac{\mu(n)}{n}\psi(u/n)+O(\exp(-c\sqrt{\log y})), |  |

for all N ≤ u ≤ y N\leq u\leq y. Since R ~ ​ ( u) {\widetilde{R}}(u) and the sum over n n above are ≪ log ⁡ y \ll\log y, it follows that for ℓ ≤ c 9 ​ log ⁡ y / log ⁡ log ​ y \ell\leq\frac{c}{9}\sqrt{\log y}/\log\log y

(7.1) |  | 1 y ​ ∫ 0 y R ~ ​ ( u) ℓ ​ 𝑑 u = ( − 1) ℓ y ​ ∫ 0 y ( ∑ n ≤ N μ ⁡ ( n) n ​ ψ ​ ( u / n)) ℓ ​ 𝑑 u + O ⁡ ( exp ⁡ ( − c 2 ​ log ⁡ y)). \frac{1}{y}\int_{0}^{y}{\widetilde{R}}(u)^{\ell}du=\frac{(-1)^{\ell}}{y}\int_{0}^{y}\Big(\sum_{n\leq N}\frac{\mu(n)}{n}\psi(u/n)\Big)^{\ell}du+O(\exp(-\tfrac{c}{2}\sqrt{\log y})). |  |

Now applying ( 3.10) we see that

 | 1 y ​ ∫ 0 y ( ∑ n ≤ N μ ⁡ ( n) n ​ ψ ​ ( u / n)) ℓ ​ 𝑑 u \displaystyle\frac{1}{y}\int_{0}^{y}\Big(\sum_{n\leq N}\frac{\mu(n)}{n}\psi(u/n)\Big)^{\ell}du | = 1 y ​ ∫ 0 y ( ∑ n ≤ y 1 / ( 2 ​ ℓ) μ ⁡ ( n) n ​ ψ ​ ( u / n)) ℓ ​ 𝑑 u \displaystyle=\frac{1}{y}\int_{0}^{y}\Big(\sum_{n\leq y^{1/(2\ell)}}\frac{\mu(n)}{n}\psi(u/n)\Big)^{\ell}du |  |

(7.2) |  |  | + O ⁡ ( ℓ ​ ( log ⁡ y) ℓ − 1 y ​ ∫ 0 y | ∑ y 1 / ( 2 ​ ℓ) ≤ n ≤ N μ ⁡ ( n) n ​ ψ ​ ( u / n) | ​ 𝑑 u). \displaystyle+O\Big(\frac{\ell(\log y)^{\ell-1}}{y}\int_{0}^{y}\Big|\sum_{y^{1/(2\ell)}\leq n\leq N}\frac{\mu(n)}{n}\psi(u/n)\Big|du\Big). |  |

Expanding out, the main term in ( 7) is

 |  | ∑ n 1, …, n ℓ ≤ y 1 / ( 2 ​ ℓ) μ ( n 1) ⋯ μ ( n ℓ) n 1 ⋯ n ℓ ​ 1 y ​ ∫ 0 y ∏ j = 1 ℓ ψ ⁡ ( u / n j) ​ 𝑑 u \displaystyle\sum_{n_{1},\ldots,n_{\ell}\leq y^{1/(2\ell)}}\frac{\mu(n_{1})\cdots\mu(n_{\ell})}{n_{1}\cdots n_{\ell}}\frac{1}{y}\int_{0}^{y}\prod_{j=1}^{\ell}\psi(u/n_{j})du |  |

 | = \displaystyle= | ∑ n 1, …, n ℓ ≤ y 1 / ( 2 ​ ℓ) μ ( n 1) ⋯ μ ( n ℓ) n 1 ⋯ n ℓ ( ℬ ( n 1, …, n ℓ) + O ( n 1 ⋯ n ℓ)). \displaystyle\sum_{n_{1},\ldots,n_{\ell}\leq y^{1/(2\ell)}}\frac{\mu(n_{1})\cdots\mu(n_{\ell})}{n_{1}\cdots n_{\ell}}({\mathcal{B}}(n_{1},\ldots,n_{\ell})+O(n_{1}\cdots n_{\ell})). |  |

Arguing as in the proof of Theorem 4.1, this may be seen to equal M R ( ℓ) + O ( y − 1 / ( 40 ℓ log ℓ)) M_{R}(\ell)+O(y^{-1/(40\ell\log\ell)}).

As for the remainder term in ( 7), splitting the terms y 1 / ( 2 ​ ℓ) ≤ n ≤ N y^{1/(2\ell)}\leq n\leq N into dyadic blocks, we may bound this by

 | ≪ exp ⁡ ( c 8 ​ log ⁡ y) ​ max y 1 / ( 2 ​ ℓ) ≤ M ≤ N I ⊂ [M, 2 ​ M] ​ 1 y ​ ∫ 0 y | ∑ n ∈ I μ ⁡ ( n) n ​ ψ ​ ( u / n) | ​ 𝑑 u, \ll\exp(\tfrac{c}{8}\sqrt{\log y})\max_{\begin{subarray}{c}y^{1/(2\ell)}\leq M\leq N\\ I\subset[M,2M]\end{subarray}}\frac{1}{y}\int_{0}^{y}\Big|\sum_{n\in I}\frac{\mu(n)}{n}\psi(u/n)\Big|du, |  |

where the maximum is over subintervals I I of [M, 2 ​ M] [M,2M]. By Cauchy-Schwarz and Lemma 7.2, this is

 | ≪ exp ⁡ ( c 8 ​ log ⁡ y) ​ max y 1 / ( 2 ​ ℓ) ≤ M ≤ N I ⊂ [M, 2 ​ M] ⁡ ( log ⁡ y) ​ ( 1 M + M y) 1 2 ≪ exp ⁡ ( − c 8 ​ log ⁡ y). \ll\exp(\tfrac{c}{8}\sqrt{\log y})\max_{\begin{subarray}{c}y^{1/(2\ell)}\leq M\leq N\\ I\subset[M,2M]\end{subarray}}(\log y)\Big(\frac{1}{M}+\frac{\sqrt{M}}{\sqrt{y}}\Big)^{\frac{1}{2}}\ll\exp(-\tfrac{c}{8}\sqrt{\log y}). |  |

This justifies the first claim of the theorem. It is also clear that M R ​ ( ℓ) = 0 M_{R}(\ell)=0 for odd ℓ \ell, and the formula for M R ​ ( 2) M_{R}(2) follows from our knowledge of ℬ ⁡ ( n 1, n 2) {\mathcal{B}}(n_{1},n_{2}). Lastly, the claimed upper bound on M R ​ ( ℓ) M_{R}(\ell) follows exactly as the upper bound for M C ​ ( ℓ) M_{C}(\ell) in Theorem 4.1. ∎

## References

- [1] T. M. Apostol. Modular functions and Dirichlet series in number theory, volume 41 of Graduate Texts in Mathematics. Springer-Verlag, New York, second edition, 1990.
- [2] J. Bourgain and M. Z. Garaev. Sumsets of reciprocals in prime fields and multilinear Kloosterman sums. Izv. Ross. Akad. Nauk Ser. Mat., 78(4):19–72, 2014.
- [3] S. Chowla. Contributions to the analytic theory of numbers. Math. Z., 35(1):279–299, 1932.
- [4] A. Granville and K. Soundararajan. The distribution of values of L ⁡ ( 1, χ d) L(1,\chi_{d}). Geom. Funct. Anal., 13(5):992–1028, 2003.
- [5] A. A. Karatsuba. New estimates for short Kloosterman sums. Mat. Zametki, 88(3):384–398, 2010.
- [6] M. A. Korolëv. On Karatsuba’s method of estimating Kloosterman sums. Mat. Sb., 207(8):117–134, 2016.
- [7] R. J. Lemke Oliver and K. Soundararajan. Unexpected biases in the distribution of consecutive primes. Proc. Natl. Acad. Sci. USA, 113(31):E4446–E4454, 2016.
- [8] H. L. Montgomery. Fluctuations in the mean of Euler’s phi function. Proc. Indian Acad. Sci. Math. Sci., 97(1-3):239–245 (1988), 1987.
- [9] H. L. Montgomery. Ten lectures on the interface between analytic number theory and harmonic analysis, volume 84 of CBMS Regional Conference Series in Mathematics. Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 1994.
- [10] S. S. Pillai and S. D. Chowla. On the Error Terms in some Asymptotic Formulae in the Theory of Numbers (1). J. London Math. Soc., S1-5(2):95.
- [11] I. Vardi. Dedekind sums have a limiting distribution. Internat. Math. Res. Notices, (1):1–12, 1993.
- [12] A. Walfisz. Weylsche Exponentialsummen in der neueren Zahlentheorie. Mathematische Forschungsberichte, XV. VEB Deutscher Verlag der Wissenschaften, Berlin, 1963.
- [13] L. C. Washington. Introduction to cyclotomic fields, volume 83 of Graduate Texts in Mathematics. Springer-Verlag, New York, second edition, 1997.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:robert.lemke_oliver@tufts.edu
[2]: mailto:ksound@stanford.edu
[3]: /html/1709.06167
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/1709.06168
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1709.06168
[9]: https://arxiv.org/pdf/1709.06168
[10]: /html/1709.06169
