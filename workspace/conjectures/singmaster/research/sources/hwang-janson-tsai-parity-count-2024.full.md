<!-- source: https://arxiv.org/html/2408.06817 | converted from HTML -->

Periodic minimum in the count of binomial coefficients not divisible by a prime

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2408.06817v1 [math.NT] 13 Aug 2024

# Periodic minimum in the count of binomial coefficients not divisible by a prime

Hsien-Kuei Hwang Affiliation: Institute of Statistical Science Affiliation: Academia Sinica Affiliation: Taipei 115 Affiliation: Taiwan Svante Janson Affiliation: Department of Mathematics Affiliation: Uppsala University Affiliation: Uppsala Affiliation: Sweden Tsung-Hsi Tsai Affiliation: Institute of Statistical Science Affiliation: Academia Sinica Affiliation: Taipei 115 Affiliation: Taiwan

August 11, 2026

###### Abstract

The summatory function of the number of binomial coefficients not divisible by a prime is known to exhibit regular periodic oscillations, yet identifying the less regularly behaved minimum of the underlying periodic functions has been open for almost all cases. We propose an approach to identify such minimum in some generality, solving particularly a previous conjecture of B. Wilson [Asymptotic behavior of Pascal’s triangle modulo a prime, *Acta Arith.*83 (1998), pp. 105–116].

## 1 Introduction

Let F p ​ ( n) F_{p}(n) denote the number of binomial coefficients ( m k) \binom{m}{k}, 0 ≤ k ≤ m < n 0\leq k\leq m<n, that are not divisible by a given prime p p. In particular, for p = 2 p=2, F 2 ​ ( n) F_{2}(n) is the number of odd numbers in the first n n rows of Pascal’s triangle. The study of the quantity F p ​ ( n) F_{p}(n) has a long history; see, for example, the historical account in Stolarsky’s paper [11]. Some sequences of F p ​ ( n) F_{p}(n) appear in the On-Line Encyclopedia of Integer Sequences (OEIS) [9]: A006046 ( p = 2 p=2), A006048 ( p = 3 p=3), and A194458 ( p = 5 p=5).

Fine [3] proved that “almost all” binomial coefficients are divisible by a prime p p, more precisely that

 | lim n → ∞ F p ​ ( n) ( n + 1 2) = 0. \lim_{n\rightarrow\infty}\frac{F_{p}(n)}{\binom{n+1}{2}}=0. |  | (1.1) |

He [3] also gave the expression (with n = ∑ 0 ≤ i ≤ s b i ​ 2 i n=\sum_{0\leq i\leq s}b_{i}2^{i}, b i ∈ { 0, 1 } b_{i}\in\{0,1\})

 | F p ​ ( n + 1) − F p ​ ( n) = ∏ 0 ≤ i ≤ s ( b i + 1) F_{p}(n+1)-F_{p}(n)=\prod_{0\leq i\leq s}(b_{i}+1) |  | (1.2) |

for the number of binomial coefficients ( n k) \binom{n}{k}, 0 ≤ k ≤ n 0\leq k\leq n, not divisible by p p.

Later Stein [10] observed that, for any prime p p,

 | F p ​ ( p ​ n) = ( p + 1 2) ​ F p ​ ( n), n ≥ 1, \displaystyle F_{p}(pn)=\binom{p+1}{2}F_{p}(n),\qquad n\geq 1, |  | (1.3) |

Thus the sequence ψ p ​ ( n):= F p ​ ( n) / n ϱ p \psi_{p}(n):=F_{p}(n)/n^{\varrho_{p}}, where ϱ p = log p ⁡ ( p + 1 2) \varrho_{p}=\log_{p}\binom{p+1}{2}, satisfies ψ p ​ ( p ​ n) = ψ p ​ ( n) \psi_{p}(pn)=\psi_{p}(n), so that ψ p \psi_{p} can be extended by this property to all positive p p -adic rational numbers. Stein [10] also showed that ψ p \psi_{p} can be further extended to a continuous function on ( 0, ∞) (0,\infty); in other words, there exists a continuous 1-periodic function 𝒫 p ​ ( t) \mathcal{P}_{p}(t) on ℝ \mathbb{R} such that

 | F p ​ ( n) = n ϱ p ​ 𝒫 p ​ ( log p ⁡ n), n ≥ 1. \displaystyle F_{p}(n)=n^{\varrho_{p}}\mathcal{P}_{p}(\log_{p}n),\qquad n\geq 1. |  | (1.4) |

It follows immediately from this that

 | α p \displaystyle\alpha_{p} | : = lim sup n → ∞ F p ​ ( n) n ϱ p = sup n ≥ 1 F p ​ ( n) n ϱ p = max t ∈ [0, 1] ⁡ 𝒫 p ​ ( t) ∈ [0, ∞), \displaystyle:=\limsup_{n\to\infty}\frac{F_{p}(n)}{n^{\varrho_{p}}}=\sup_{n\geq 1}\frac{F_{p}(n)}{n^{\varrho_{p}}}=\max_{t\in[0,1]}\mathcal{P}_{p}(t)\in[0,\infty), |  | (1.5) |

 | β p \displaystyle\beta_{p} | : = lim inf n → ∞ F p ​ ( n) n ϱ p = inf n ≥ 1 F p ​ ( n) n ϱ p = min t ∈ [0, 1] ⁡ 𝒫 p ​ ( t) ∈ [0, ∞), \displaystyle:=\liminf_{n\to\infty}\frac{F_{p}(n)}{n^{\varrho_{p}}}=\inf_{n\geq 1}\frac{F_{p}(n)}{n^{\varrho_{p}}}=\min_{t\in[0,1]}\mathcal{P}_{p}(t)\in[0,\infty), |  | (1.6) |

furthermore, α p = 1 \alpha_{p}=1 for every p p, and that ( p + 1 2) − 1 ≤ β p < 1 \binom{p+1}{2}^{-1}\leq\beta_{p}<1; see [10]. The extremal properties of 𝒫 2 \mathcal{P}_{2} had earlier been treated by Stolarsky [11] and Harborth [5]. In particular, Harborth proved that α 2 = 1 \alpha_{2}=1 and derived the numerical value β 2 ≐ 0.812556 \beta_{2}\doteq 0.812556 to 6 decimal places; see A077464 (Stolarsky-Harborth constant) for more information. Further numerical estimates of β p \beta_{p} for various p p have been made later; of special mention is Chen and Ji’s inequalities [1]:

 | 1 ( 1 + p − r) ϱ p ​ min p r ≤ n ≤ p r + 1 ​ F p ​ ( n) n ϱ p ≤ β p ≤ min p r ≤ n ≤ p r + 1 ⁡ F p ​ ( n) n ϱ p, \displaystyle\frac{1}{(1+p^{-r})^{{\varrho_{p}}}}\min_{p^{r}\leq n\leq p^{r+1}}\frac{F_{p}(n)}{n^{{\varrho_{p}}}}\leq\beta_{p}\leq\min_{p^{r}\leq n\leq p^{r+1}}\frac{F_{p}(n)}{n^{{\varrho_{p}}}}, |  | (1.7) |

which in principle makes it possible to calculate β p \beta_{p} to any given degree of precision. However, an exact expression remains unknown.

For p ≥ 3 p\geq 3, Volodin [13] conjectured that

 | β 3 = ( 3 2) 1 − ϱ 3 = 2 log 3 ⁡ 2 − 1, \beta_{3}=\left(\frac{3}{2}\right)^{1-\varrho_{3}}=2^{\log_{3}2-1}, |  | (1.8) |

which was proved by Franco [4]; however, his proof does not extend to other primes p p.

Wilson [16] calculated β 3, β 5, …, β 19 \beta_{3},\beta_{5},\ldots,\beta_{19} to six decimal places and showed that

 | lim p → ∞ β p = 0.5. \lim_{p\rightarrow\infty}\beta_{p}=0.5. |  | (1.9) |

He furthermore conjectured that

 | β 5 = ( 3 2) 1 − ϱ 5, β 7 = ( 3 2) 1 − ϱ 7, β 11 = 59 44 ​ ( 22 31) ϱ 11. \beta_{5}=\left(\frac{3}{2}\right)^{1-\varrho_{5}},\qquad\beta_{7}=\left(\frac{3}{2}\right)^{1-\varrho_{7}},\qquad\beta_{11}=\frac{59}{44}\left(\frac{22}{31}\right)^{\varrho_{11}}. |  | (1.10) |

The main purpose of the present paper is to prove this conjecture, and to give similar results for further primes p p. More precisely, by a detailed examination of the periodic function 𝒫 p ​ ( x) \mathcal{P}_{p}(x), coupling with analytic bounds and numerical calculations, we are able to find the minimum β p \beta_{p} for all odd primes 3 ≤ p ≤ 113 3\leq p\leq 113, proving particularly Wilson’s conjectures ( 1.10) and differently ( 1.8). Our approach can be readily extended to higher values of p p, but a proof for all odd primes p p remains open.

In our approach we fix an odd prime p p. After a change of variables (see Section 3 for details), we obtain β p = min s ∈ [p − 1, 1] ⁡ G ⁡ ( s) \beta_{p}=\min_{s\in[p^{-1},1]}G(s) for the function G ​ ( s) = G p ​ ( s) G(s)=G_{p}(s) defined in ( 3.2). The main part of our argument is to show that (for the primes p p that we have studied, at least) this minimum is attained at the point

 | s ^ p = s ^ p ​ ( ξ, η):= 2 ​ ξ + 1 2 ​ p − η p 2, \displaystyle\hat{s}_{p}=\hat{s}_{p}(\xi,\eta):=\frac{2\xi+1}{2p}-\frac{\eta}{p^{2}}, |  | (1.11) |

for a suitable pair of integers ( ξ, η) (\xi,\eta) with 1 ≤ ξ < p 1\leq\xi<p and 0 ≤ η ≤ p − 1 2 0\leq\eta\leq\frac{p-1}{2}. In terms of p p -ary expansion,

 | s ^ p = ( 0. b 1 b 2 …), where b 1 = ξ, b 2 = p − 1 2 − η, and b j = p − 1 2 for j ≥ 3. \displaystyle\hat{s}_{p}=(0.b_{1}b_{2}\dots),\quad\text{where }b_{1}=\xi,\;b_{2}=\tfrac{p-1}{2}-\eta,\text{ and }b_{j}=\tfrac{p-1}{2}\text{ for }j\geq 3. |  | (1.12) |

When this holds, we thus have β p = B ξ, η:= G ⁡ ( s ^ p) \beta_{p}=B_{\xi,\eta}:=G(\hat{s}_{p}), which explicitly is given by (see Lemma 4.1)

 | B ξ, η = ( ξ + 1 2) ⁡ ( 1 + ( p − 2 ​ η) ​ ( p − 2 ​ η + 1) 2 ​ ξ ​ p ​ ( p + 1)) ​ ( 2 ​ ξ + 1 2 − η p) − ϱ p. \displaystyle B_{\xi,\eta}=\binom{\xi+1}{2}\left(1+\frac{(p-2\eta)(p-2\eta+1)}{2\xi p(p+1)}\right)\left(\frac{2\xi+1}{2}-\frac{\eta}{p}\right)^{-\varrho_{p}}. |  | (1.13) |

One complication is that the correct choice of ( ξ, η) (\xi,\eta) is not obvious and depends on p p, as is illustrated in the following theorem, which is our main result.

###### Theorem 1.1.

Wilson’s conjecture ( 1.10) holds true. More generally, for an odd prime p p, 3 ≤ p ≤ 113 3\leq p\leq 113, we have β p = B ξ, η \beta_{p}=B_{\xi,\eta} where the pair of values ( ξ, η) (\xi,\eta) (together with s ^ p ​ ( ξ, η) \hat{s}_{p}(\xi,\eta)) are given in the following table:

 |

p p | { 3, 5, 7 } \{3,5,7\} | { 11, 13, 17, 19, 23 } \{11,13,17,19,23\} | { 29 } \{29\} | { 31, 37, 41, 43, 47, 53 } \{31,37,41,43,47,53\} |

( ξ, η) (\xi,\eta) | ( 1, 0) (1,0) | ( 1, 1) (1,1) | ( 2, 1) (2,1) | ( 2, 2) (2,2) |

s ^ p ​ ( ξ, η) \hat{s}_{p}(\xi,\eta) | 3 2 ​ p \frac{3}{2p} | 3 2 ​ p − 1 p 2 \frac{3}{2p}-\frac{1}{p^{2}} | 5 2 ​ p − 1 p 2 \frac{5}{2p}-\frac{1}{p^{2}} | 5 2 ​ p − 2 p 2 \frac{5}{2p}-\frac{2}{p^{2}} |

 |

p p | { 59, 61, 67, 71, 73, 79 } \{59,61,67,71,73,79\} | { 83, 89, 97, 101, 103, 107 } \{83,89,97,101,103,107\} | { 109,113 } \{109,113\} |

( ξ, η) (\xi,\eta) | ( 2, 3) (2,3) | ( 2, 4) (2,4) | ( 2, 5) (2,5) |

s ^ p ​ ( ξ, η) \hat{s}_{p}(\xi,\eta) | 5 2 ​ p − 3 p 2 \frac{5}{2p}-\frac{3}{p^{2}} | 5 2 ​ p − 4 p 2 \frac{5}{2p}-\frac{4}{p^{2}} | 5 2 ​ p − 5 p 2 \frac{5}{2p}-\frac{5}{p^{2}} |

 |

 |  |

Indeed, the same result β p = B ξ, η \beta_{p}=B_{\xi,\eta} holds for larger values of p p with suitably chosen ( ξ, η) (\xi,\eta), and our numerical calculations confirmed this for p p up to several thousand (see Section 6); however, a proof for *all*odd primes remains open.

In particular, we obtain

 |

p p | 13 13 | 17 17 |  | β p ​ ( p = 3, …, 113) \beta_{p}(p=3,\dots,113) |

β p \beta_{p} | 124 91 ​ ( 26 37) log 13 ⁡ 91 \frac{124}{91}\bigl(\frac{26}{37}\bigr)^{\log_{13}91} ≈ 0.73266 \approx 0.73266 | 71 51 ​ ( 34 49) log 17 ⁡ 153 \frac{71}{51}\bigl(\frac{34}{49}\bigr)^{\log_{17}153} ≈ 0.72758 \approx 0.72758 |  |  |

p p | 19 19 | 113 113 |  |

β p \beta_{p} | 533 380 ​ ( 38 55) log 19 ⁡ 190 \frac{533}{380}\bigl(\frac{38}{55}\bigr)^{\log_{19}190} ≈ 0.72575 \approx 0.72575 | 7780 2147 ​ ( 226 555) log 113 ⁡ 6441 \frac{7780}{2147}\bigl(\frac{226}{555}\bigr)^{\log_{113}6441} ≈ 0.68432 \approx 0.68432 |  |  |

 |  |

To prove Theorem 1.1, in view of ( 1.6), it suffices to find the minimum of 𝒫 p ​ ( log p ⁡ s) \mathcal{P}_{p}(\log_{p}s) for s ∈ [p − 1, 1] s\in[p^{-1},1]. Wilson (1998) conjectured (in a different formulation for integers n n, see Remark 3.1 below) that for any p p, the minimum β p \beta_{p} occurs at some point s ^ p {\hat{s}}_{p} such that all but a finite number of its base p p digits are equal to p − 1 2 \frac{p-1}{2}. Note that the point s ^ p \hat{s}_{p} of ( 1.11)–( 1.12) is of the type consistent with Wilson’s conjecture.

We observe that the graph of 𝒫 p ​ ( log ⁡ s) \mathcal{P}_{p}(\log s) has a self-similar nature, and if the graph is “zoomed in” on such points s s, the resulting function converges uniformly. We then find the local behavior from the limiting function. The proof of ( 1.1) then builds on this idea, and this implies in particular Wilson’s conjecture ( 1.10); see Section 4 for the details of the proof.

###### Problem 1.2.

The apparently simplest case p = 2 p=2 seems to be actually the most complicated. Despite many digits of β 2 \beta_{2} are known (see A077464 and the references therein), to the best of our knowledge, no exact expression for β 2 \beta_{2} is available or proposed or conjectured. How to characterize the minimum point s ^ 2 {\hat{s}}_{2}, and what is the corresponding minimum value β 2 \beta_{2}?

###### Problem 1.3.

The main open question is whether β p = B ξ, η \beta_{p}=B_{\xi,\eta} for some ( ξ, η) (\xi,\eta) for all odd primes p p. Equivalently, is the minimum point always some s ^ p \hat{s}_{p} (defined in ( 1.11))?

Our approach is based on the resolution of the recurrence ( 2.1) satisfied by F p ​ ( n) F_{p}(n), which we prove below in Theorem 2.1, following the same arguments used in our previous paper [8]. No other number-theoretic properties are needed. This then yields the representation ( 1.4) with a continuous periodic functions 𝒫 p \mathcal{P}_{p}, and a special explicit formula for 𝒫 p \mathcal{P}_{p} that we will use. Indeed, in the case p = 2 p=2, this recurrence is of the binary form studied in [8], and F 2 ​ ( n) F_{2}(n) was one of the many examples discussed there. We show in Appendix A that the method of [8] can be generalized to a general class of p p -ary recursions including ( 2.1). (The results in the appendix are valid for any integer p ≥ 2 p\geq 2.)

More generally, a number of authors have studied F p, d ​ ( n) F_{p,d}(n), the number of multinomial coefficients ( m j 1, …, j d) \binom{m}{j_{1},\dots,j_{d}} with 0 ≤ m < n 0\leq m<n that are not divisible by p p.

###### Problem 1.4.

Extend the methods and results of the present paper to multinomial coefficients.

## 2 A recurrence and its solutions

In this section, we fix a prime p ≥ 2 p\geq 2.

###### Theorem 2.1.

The total number of binomial coefficients ( m k) \binom{m}{k} with m, k < n m,k<n that are not divisible by p p satisfies the recurrence

 | F p ​ ( n) = ∑ 0 ≤ j < p ( p − j) ​ F p ​ ( ⌊ n + j p ⌋) ( n ≥ p), F_{p}(n)=\sum_{0\leq j<p}(p-j)F_{p}\left(\left\lfloor\frac{n+j}{p}\right\rfloor\right)\qquad(n\geq p), |  | (2.1) |

with the initial values { F p ( j) = ( j + 1 2): j = 1, …, p − 1 } \{F_{p}(j)=\binom{j+1}{2}:j=1,\ldots,p-1\}. In fact, ( 2.1) holds for all n ≥ 0 n\geq 0, with F p ​ ( 0):= 0 F_{p}(0):=0.

###### Proof.

It is obvious that ( j k) \binom{j}{k} is not divisible by a prime p p if k ≤ j < p k\leq j<p. Thus the initial values are

 | F p ​ ( j) = ( j + 1 2) for ​ j = 1, …, p − 1. F_{p}(j)=\binom{j+1}{2}\quad\textrm{for }j=1,\ldots,p-1. |  | (2.2) |

We use the following expression from Volodin [12] (there stated more generally for multinomial coefficients):

 | F p ​ ( n) = 1 2 ​ ∑ 0 ≤ j ≤ ν ( p + 1 2) j ​ b j ​ ∏ j ≤ i ≤ ν ( b i + 1), F_{p}(n)=\frac{1}{2}\sum_{0\leq j\leq\nu}\binom{p+1}{2}^{j}b_{j}\prod_{j\leq i\leq\nu}(b_{i}+1), |  | (2.3) |

[see also [1]] where b j ∈ { 0, …, p − 1 } b_{j}\in\{0,\dots,p-1\} are the base p p digits of n = b 0 + b 1 ​ p + ⋯ + b ν ​ p ν n=b_{0}+b_{1}p+\dotsm+b_{\nu}p^{\nu}. (The formula ( 2.3) holds trivially for n = 0 n=0 too, with an empty sum.) If n = k ​ p n=kp, then b 0 = 0 b_{0}=0 and k = b 1 + b 2 ​ p + ⋯ + b ν ​ p ν − 1 k=b_{1}+b_{2}p+\cdots+b_{\nu}p^{\nu-1}. Thus, from ( 2.3),

 | F p ​ ( n) \displaystyle F_{p}(n) | = 1 2 ​ ∑ 1 ≤ j ≤ ν ( p + 1 2) j ​ b j ​ ∏ j ≤ i ≤ ν ( b i + 1) \displaystyle=\frac{1}{2}\sum_{1\leq j\leq\nu}\binom{p+1}{2}^{j}b_{j}\prod_{j\leq i\leq\nu}(b_{i}+1) |  | (2.4) |

 |  | = ( p + 1 2) ⋅ 1 2 ∑ 1 ≤ j ≤ ν ( p + 1 2) j − 1 b j ∏ j ≤ i ≤ ν ( b i + 1) \displaystyle=\binom{p+1}{2}\cdot\frac{1}{2}\sum_{1\leq j\leq\nu}\binom{p+1}{2}^{j-1}b_{j}\prod_{j\leq i\leq\nu}(b_{i}+1) |  |

 |  | = ( p + 1 2) ⋅ 1 2 ∑ 0 ≤ j ≤ ν − 1 ( p + 1 2) j b j + 1 ∏ j ≤ i ≤ ν − 1 ( b i + 1 + 1) \displaystyle=\binom{p+1}{2}\cdot\frac{1}{2}\sum_{0\leq j\leq\nu-1}\binom{p+1}{2}^{j}b_{j+1}\prod_{j\leq i\leq\nu-1}(b_{i+1}+1) |  |

 |  | = ( p + 1 2) ​ F p ​ ( k). \displaystyle=\binom{p+1}{2}F_{p}(k). |  |

In general, suppose n = k ​ p + r n=kp+r, where k ≥ 0 k\geq 0 and 0 ≤ r < p 0\leq r<p. Then b 0 = r b_{0}=r and ( 2.3) yields

 | F p ​ ( n) − F p ​ ( k ​ p) = r 2 ​ ∏ 0 ≤ i ≤ ν ( b i + 1) = r ⁡ ( r + 1) 2 ​ ∏ 1 ≤ i ≤ ν ( b i + 1) F_{p}(n)-F_{p}(kp)=\frac{r}{2}\prod_{0\leq i\leq\nu}(b_{i}+1)=\frac{r(r+1)}{2}\prod_{1\leq i\leq\nu}(b_{i}+1) |  | (2.5) |

since all but the first term in the sums cancel. By Fine’s result ( 1.2), this yields

 | F p ​ ( n) − F p ​ ( k ​ p) = ( r + 1 2) ⁡ ( F p ​ ( k + 1) − F p ​ ( k)). F_{p}(n)-F_{p}(kp)=\binom{r+1}{2}\left(F_{p}(k+1)-F_{p}(k)\right). |  | (2.6) |

Thus we have

 | F p ​ ( n) \displaystyle F_{p}(n) | = F p ​ ( k ​ p) + ( F p ​ ( n) − F p ​ ( k ​ p)) \displaystyle=F_{p}(kp)+\left(F_{p}(n)-F_{p}(kp)\right) |  | (2.7) |

 |  | = ( p + 1 2) ​ F p ​ ( k) + ( r + 1 2) ⁡ ( F p ​ ( k + 1) − F p ​ ( k)) \displaystyle=\binom{p+1}{2}F_{p}(k)+\binom{r+1}{2}\left(F_{p}(k+1)-F_{p}(k)\right) |  |

 |  | = ∑ 0 ≤ j < p ( p − j) ​ F p ​ ( k) + ( r + 1 2) ⁡ ( F p ​ ( k + 1) − F p ​ ( k)) \displaystyle=\sum_{0\leq j<p}(p-j)F_{p}(k)+\binom{r+1}{2}\left(F_{p}(k+1)-F_{p}(k)\right) |  |

 |  | = ∑ 0 ≤ j ≤ p − r − 1 ( p − j) ​ F p ​ ( k) + ∑ p − r ≤ j < p ( p − j) ​ F p ​ ( k + 1) \displaystyle=\sum_{0\leq j\leq p-r-1}(p-j)F_{p}(k)+\sum_{p-r\leq j<p}(p-j)F_{p}(k+1) |  |

 |  | = ∑ 0 ≤ j < p ( p − j) ​ F p ​ ( ⌊ n + j p ⌋). \displaystyle=\sum_{0\leq j<p}(p-j)F_{p}\left(\left\lfloor\frac{n+j}{p}\right\rfloor\right). |  |

This proves the recurrence ( 2.1). ∎

Theorem 2.1 shows that F p ​ ( n) F_{p}(n) satisfies a recurrence of the type treated in Appendix A. From Theorem A.3 we thus immediately obtain the representation ( 1.4), together with the following formula for 𝒫 p ​ ( t) \mathcal{P}_{p}(t). (This formula is essentially given in [2].)

###### Theorem 2.2.

Define

 | A = A p:= ( p + 1 2). \displaystyle A=A_{p}:=\binom{p+1}{2}. |  | (2.8) |

Then the number of binomial coefficients in the first n n rows that are not divisible by p p satisfies

 | F p ​ ( n) = n ϱ ​ 𝒫 ​ ( log p ⁡ n) for all ​ n ≥ 1, F_{p}(n)=n^{\varrho}\mathcal{P}\left(\log_{p}n\right)\qquad\textrm{for all }n\geq 1, |  | (2.9) |

where ϱ = ϱ p:= log p ⁡ A \varrho={\varrho_{p}}:=\log_{p}A and 𝒫 ​ ( t) = 𝒫 p ​ ( t) \mathcal{P}(t)=\mathcal{P}_{p}(t) is a continuous 1 1 -periodic function given by

 | 𝒫 ⁡ ( t):= A 1 − { t } ​ φ ​ ( p { t } − 1), \mathcal{P}(t):=A^{1-\{t\}}\varphi(p^{\{t\}-1}), |  | (2.10) |

with the function φ = φ p: [0, 1] → ℝ \varphi=\varphi_{p}:[0,1]\to\mathbb{R} given by the explicit formula

 | φ ⁡ ( ∑ j ≥ 1 b j ​ p − j) = 1 2 ​ ∑ j ≥ 1 b j A j ​ ∏ 1 ≤ i ≤ j ( b i + 1), \varphi\left(\sum_{j\geq 1}b_{j}p^{-j}\right)=\frac{1}{2}\sum_{j\geq 1}\frac{b_{j}}{A^{j}}\prod_{1\leq i\leq j}(b_{i}+1), |  | (2.11) |

for any b j ∈ { 0, 1, 2, …, p − 1 } b_{j}\in\{0,1,2,\ldots,p-1\}; furthermore, φ \varphi satisfies that for j = 0, 1, …, p − 1 j=0,1,\ldots,p-1,

 | φ ⁡ ( t) = j + 1 A ​ φ ​ ( { p ​ t }) + ( j + 1 2) A, if j p ≤ t ≤ j + 1 p. \varphi(t)=\frac{j+1}{A}\varphi(\{pt\})+\frac{\binom{j+1}{2}}{A},\qquad\mathrm{if}\quad\frac{j}{p}\leq t\leq\,\frac{j+1}{p}. |  | (2.12) |

###### Proof.

By Theorem 2.1, F p ​ ( n) F_{p}(n) satisfies the recurrence ( A.1) with γ i = p − i \gamma_{i}=p-i. We have

 | ∑ p − j ≤ i < p γ i = ( j + 1 2) = F p ( j) for j = 1, …, p − 1, \sum_{p-j\leq i<p}\gamma_{i}=\binom{j+1}{2}=F_{p}(j)\quad\textrm{for }j=1,\ldots,p-1, |  | (2.13) |

and thus the condition ( A.26) is satisfied; see also Remark A.5. Similarly, A A in ( A.2) is given by ( 2.8). The results follow by Theorem A.3 and Lemma A.1; ( 2.12) follows by plugging γ j = p − j \gamma_{j}=p-j into ( A.3), and ( A.4) yields

 | φ ⁡ ( ∑ j ≥ 1 b j ​ p − j) \displaystyle\varphi\left(\sum_{j\geq 1}b_{j}p^{-j}\right) | = ∑ j ≥ 1 ∑ i = p − b j p ( p − i) A j ​ ∏ 1 ≤ i < j ( b i + 1) \displaystyle=\sum_{j\geq 1}\frac{\sum_{i=p-b_{j}}^{p}(p-i)}{A^{j}}\prod_{1\leq i<j}(b_{i}+1) |  | (2.14) |

 |  | = 1 2 ​ ∑ j ≥ 1 b j ​ ( b j + 1) A j ​ ∏ 1 ≤ i < j ( b i + 1) \displaystyle=\frac{1}{2}\sum_{j\geq 1}\frac{b_{j}(b_{j}+1)}{A^{j}}\prod_{1\leq i<j}(b_{i}+1) |  |

 |  | = 1 2 ​ ∑ j ≥ 1 b j A j ​ ∏ 1 ≤ i ≤ j ( b i + 1), \displaystyle=\frac{1}{2}\sum_{j\geq 1}\frac{b_{j}}{A^{j}}\prod_{1\leq i\leq j}(b_{i}+1), |  |

for any b j ∈ { 0, 1, 2, …, p − 1 } b_{j}\in\{0,1,2,\ldots,p-1\}, which is ( 2.11). ∎

## 3 Our approach

In this section, p p is a fixed odd prime. Recall that A = ( p + 1 2) A=\binom{p+1}{2} and ϱ p = log p ⁡ A \varrho_{p}=\log_{p}A.

By ( 1.6) and Theorem 2.2, β p \beta_{p} is the minimum of the periodic function

 | 𝒫 ⁡ ( t):= A 1 − t ​ φ ​ ( p t − 1) for t ∈ [0, 1), \mathcal{P}(t):=A^{1-{t}}\varphi(p^{{t}-1})\qquad\textrm{for}\quad t\in[0,1), |  | (3.1) |

where φ \varphi is given by ( 2.11). (By continuity, we may as well take the minimum for t ∈ [0, 1] t\in[0,1].) We make the change of variables s = p t − 1 s=p^{t-1} and consider

 | G ⁡ ( s):= A − log p ⁡ s ​ φ ​ ( s) for s ∈ [p − 1, 1]; G(s):=A^{-\log_{p}s}\varphi(s)\qquad\textrm{for}\quad s\in[p^{-1},1]; |  | (3.2) |

thus 𝒫 ⁡ ( t) = G ⁡ ( p t − 1) \mathcal{P}(t)=G(p^{t-1}) for t ∈ [0, 1) t\in[0,1), and thus β p = min ⁡ { G ⁡ ( s): s ∈ [p − 1, 1] } \beta_{p}=\min\{G(s):s\in[p^{-1},1]\}. Note that

 | A − log p ⁡ s = p − ϱ p ​ log p ​ s = s − ϱ p. \displaystyle A^{-\log_{p}s}=p^{-{\varrho_{p}}\log_{p}s}=s^{-{\varrho_{p}}}. |  | (3.3) |

###### Remark 3.1.

For any n ≥ 1 n\geq 1, by ( 2.9)–( 2.10) and ( 3.1)–( 3.2), we see that

 | F p ​ ( n) ​ n − ϱ p \displaystyle F_{p}(n)n^{-{\varrho_{p}}} | = 𝒫 ⁡ ( log p ⁡ n) = 𝒫 ⁡ ( { log p ⁡ n }) = G ⁡ ( p { log p ⁡ n } − 1) = G ⁡ ( n ​ p − ⌊ log p ⁡ n ⌋ − 1). \displaystyle=\mathcal{P}(\log_{p}n)=\mathcal{P}(\{\log_{p}n\})=G\bigl(p^{\{\log_{p}n\}-1}\bigr)=G\bigl(np^{-\lfloor\log_{p}n\rfloor-1}\bigr). |  | (3.4) |

It follows that if G G attains its minimum on [p − 1, 1] [p^{-1},1] at s ^ {\hat{s}}, then the sequence n k:= ⌊ p k ​ s ^ ⌋ n_{k}:=\lfloor p^{k}{\hat{s}}\rfloor satisfies

 | F p ​ ( n k) ​ n k − ϱ p → G ⁡ ( s ^) = β p, \displaystyle F_{p}(n_{k})n_{k}^{-{\varrho_{p}}}\to G({\hat{s}})=\beta_{p}, |  | (3.5) |

and thus the infimum β p \beta_{p} is asymptotically reached by the sequence ( n k) (n_{k}). Conversely, Wilson [16] conjectured (in a somewhat stronger form) that

 | β p = lim k → ∞ ( F p ​ ( n k) ​ n k − ϱ p), \displaystyle\beta_{p}=\lim_{k\to\infty}(F_{p}(n_{k})n_{k}^{-{\varrho_{p}}}), |  | (3.6) |

for a sequence n k n_{k} given by the recursion n k + 1 = p ​ n k + p − 1 2 n_{k+1}=pn_{k}+\frac{p-1}{2} for a suitably chosen n 1 n_{1}; this sequence is of the form just mentioned (up to a shift of indices), and Wilson’s conjecture thus would imply that the minimum on [p − 1, 1] [p^{-1},1] is attained at a point s ^ {\hat{s}} such that all but a finite number of the digits in base p p of s ^ {\hat{s}} are p − 1 2 \frac{p-1}{2}. Note that all points s ^ {\hat{s}} that we consider as potential minimum points are of this type, see ( 1.12). △ \triangle

Our methods of proof consists of two major techniques: *magnifying mapping*and *piecewise monotonic majorization*. The former defines first a mapping θ \theta and magnifies the local difference of G ⁡ ( θ ⁡ ( s)) − G ⁡ ( θ ⁡ ( 1 2)) G(\theta(s))-G(\theta(\frac{1}{2})) in a small neighborhood, say J J, of s ^ = θ ⁡ ( 1 2) \hat{s}=\theta(\frac{1}{2}) into the global difference φ ⁡ ( s) − φ ⁡ ( 1 2) \varphi(s)-\varphi(\frac{1}{2}), justifying that G ⁡ ( s ^) G(\hat{s}) is a local minimum in J J. The latter bounds crudely the ratio between two monotonic functions by their extreme values in the targeted interval, which, after partitioning the interval [0, 1] ∖ J [0,1]\setminus J into proper subintervals, is used interval-by-interval to check that G ⁡ ( s ^) G(\hat{s}) is also a minimum in [0, 1] ∖ J [0,1]\setminus J.

### 3.1 A magnifying mapping

As the minimum s ^ \hat{s} of G ⁡ ( s) G(s) we are going to prove all have the form ( 1.11) whose p p -ary expansion has an infinity number of trailing digits of the form p − 1 2 \frac{p-1}{2}, we construct a linear mapping as follows.

Fix M M and m m with 1 ≤ m < p M 1\leq m<p^{M}. Let μ \mu be the middle point of [m p M, m + 1 p M] \bigl[\frac{m}{p^{M}},\frac{m+1}{p^{M}}\bigr]:

 | μ:= m + 1 2 p M. \displaystyle\mu:=\frac{m+\frac{1}{2}}{p^{M}}. |  | (3.7) |

For every k ≥ 0 k\geq 0, define a linear mapping θ k \theta_{k} from [0, 1] [0,1] onto the interval

 | I M + k:= [μ − 1 2 ​ p M + k, μ + 1 2 ​ p M + k] I_{M+k}:=\left[\mu-\frac{1}{2p^{M+k}},\mu+\frac{1}{2p^{M+k}}\right] |  | (3.8) |

by

 | θ k ​ ( t):= m p M + ∑ M < j ≤ M + k p − 1 2 ​ p j + t p M + k, t ∈ [0, 1]. \theta_{k}(t):=\frac{m}{p^{M}}+\sum_{M<j\leq M+k}\frac{p-1}{2\,p^{j}}+\frac{t}{p^{M+k}},\qquad t\in[0,1]. |  | (3.9) |

Thus μ = θ k ​ ( 1 2) \mu=\theta_{k}(\frac{1}{2}). In terms of the p p -ary expansion, if

 | m = a 1 ​ p M − 1 + ⋯ + a M − 1 ​ p + a M, \displaystyle m=a_{1}p^{M-1}+\cdots+a_{M-1}p+a_{M}, |  | (3.10) |

then μ \mu has the form μ = ( 0. b ^ 1 b ^ 2 ⋯) p \mu=(0.{\hat{b}}_{1}{\hat{b}}_{2}\cdots)_{p}, where

 | b ^ i = a i ​ for ​ 1 ≤ i ≤ M and b ^ i = p − 1 2 ​ for ​ i ≥ M + 1. {\hat{b}}_{i}=a_{i}\;\textrm{for}\;1\leq i\leq M\quad\textrm{and}\quad{\hat{b}}_{i}=\frac{p-1}{2}\;\textrm{for}\;i\geq M+1. |  | (3.11) |

We prove that the “zoomed” functions G ⁡ ( θ k ​ ( t)) − G ⁡ ( μ) G(\theta_{k}(t))-G(\mu), suitably scaled, converge uniformly on [0, 1] [0,1], and we give a sufficient condition for G ⁡ ( μ) G(\mu) to be a minimum in an explicitly specified interval.

Note that φ ⁡ ( μ) \varphi(\mu) has the form, by ( 2.11) and ( 3.11),

 | φ ⁡ ( μ) \displaystyle\varphi(\mu) | = 1 2 ​ ∑ 1 ≤ j ≤ M a j ​ ∏ i = 1 j ( 1 + a i) A j + τ M 4 = 1 2 ​ ∑ 1 ≤ j ≤ M a j ​ ∏ i = 1 j ( 1 + a i) A j + τ M ​ φ ​ ( 1 2), \displaystyle=\frac{1}{2}\sum_{1\leq j\leq M}\frac{a_{j}\prod_{i=1}^{j}(1+a_{i})}{A^{j}}+\frac{\tau_{M}}{4}=\frac{1}{2}\sum_{1\leq j\leq M}\frac{a_{j}\prod_{i=1}^{j}(1+a_{i})}{A^{j}}+\tau_{M}\varphi\left(\frac{1}{2}\right), |  | (3.12) |

where

 | τ M:= ∏ i = 1 M ( 1 + a i) A M. \displaystyle\tau_{M}:=\frac{\prod_{i=1}^{M}(1+a_{i})}{A^{M}}. |  | (3.13) |

The construction of the mapping θ k \theta_{k} is helpful in bringing the local difference φ ⁡ ( θ k ​ ( t)) − φ ⁡ ( θ k ​ ( 1 2)) \varphi(\theta_{k}(t))-\varphi(\theta_{k}(\frac{1}{2})) into a global one in terms of φ ⁡ ( t) − φ ⁡ ( 1 2) \varphi(t)-\varphi(\frac{1}{2}).

###### Lemma 3.2.

We have

 | p k ​ ( φ ⁡ ( θ k ​ ( t)) − φ ⁡ ( μ)) = τ M ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)). p^{k}\bigl(\varphi(\theta_{k}(t))-\varphi(\mu)\bigr)=\tau_{M}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right). |  | (3.14) |

###### Proof.

Let b i b_{i} and b ~ i \tilde{b}_{i} be the base p p digits of t t and θ k ​ ( t) \theta_{k}(t), respectively. Then ( 3.9) shows that the first M + k M+k digits b ~ i \tilde{b}_{i} coincide with those of μ \mu given by ( 3.11):

 | b ~ i = b ^ i = a i ​ for ​ 1 ≤ i ≤ M and b ~ i = b ^ i = p − 1 2 ​ for ​ M + 1 ≤ i ≤ M + k, \tilde{b}_{i}={\hat{b}}_{i}=a_{i}\;\textrm{for}\;1\leq i\leq M\quad\textrm{and}\quad\tilde{b}_{i}={\hat{b}}_{i}=\frac{p-1}{2}\;\textrm{for}\;M+1\leq i\leq M+k, |  | (3.15) |

and also that the remaining digits of b ~ i \tilde{b}_{i} are the digits of t t, i.e.,

 | b ~ i + k + M = b i, i ≥ 1. \tilde{b}_{i+k+M}=b_{i},\qquad i\geq 1. |  | (3.16) |

Hence, if we compute φ ​ ( θ k ​ ( t)) \varphi(\theta_{k}(t)) and φ ⁡ ( μ) \varphi(\mu) by ( 2.11), then the first M + k M+k terms are equal, and we obtain

 | φ ⁡ ( θ k ​ ( t)) − φ ⁡ ( μ) \displaystyle\varphi(\theta_{k}(t))-\varphi(\mu) | = 1 2 ​ ∑ j ≥ k + M + 1 b ~ j ​ ∏ i = 1 j ( b ~ i + 1) A j \displaystyle=\frac{1}{2}\sum_{j\geq k+M+1}\frac{\tilde{b}_{j}\prod_{i=1}^{j}\left(\tilde{b}_{i}+1\right)}{A^{j}} |  | (3.17) |

 |  | − 1 2 ∑ j ≥ k + M + 1 p − 1 2 ​ ∏ i = 1 M ( a i + 1) ​ ∏ i = M + 1 j ( p − 1 2 + 1) A j \displaystyle\qquad-\frac{1}{2}\sum_{j\geq k+M+1}\frac{\frac{p-1}{2}\prod_{i=1}^{M}\left({a}_{i}+1\right)\prod_{i=M+1}^{j}\left(\frac{p-1}{2}+1\right)}{A^{j}} |  |

 |  | = ∏ i = 1 M ( a i + 1) A k + M ​ ( p + 1 2) k ​ 1 2 ​ ( ∑ l ≥ 1 b l ​ ∏ i = 1 l ( b i + 1) A l − ∑ l ≥ 1 p − 1 2 ​ ( p + 1 2) l A l) \displaystyle=\frac{\prod_{i=1}^{M}\left({a}_{i}+1\right)}{A^{k+M}}\left(\frac{p+1}{2}\right)^{k}\frac{1}{2}\left(\sum_{l\geq 1}\frac{b_{l}\prod_{i=1}^{l}\left(b_{i}+1\right)}{A^{l}}-\sum_{l\geq 1}\frac{\frac{p-1}{2}\left(\frac{p+1}{2}\right)^{l}}{A^{l}}\right) |  |

 |  | = τ M p k ​ ( φ ​ ( t) − φ ​ ( 1 2)). ∎ \displaystyle=\frac{\tau_{M}}{p^{k}}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right).\qed |  | (3.18) |

The crucial properties we need of the magnifying mapping θ k \theta_{k} are given as follows, the first for large k k and the second for finite one.

###### Theorem 3.3.

With the notations as above, we have, uniformly for t ∈ [0, 1] t\in[0,1],

 | p k ​ ( G ⁡ ( θ k ​ ( t)) − G ⁡ ( μ)) = μ − ϱ p − 1 ​ ( 𝒬 μ ​ ( t) + O ⁡ ( p − k)), p^{k}\left(G(\theta_{k}(t))-G(\mu)\right)=\mu^{-{\varrho_{p}}-1}\left(\mathcal{Q}_{\mu}(t)+O\left(p^{-k}\right)\right), |  | (3.19) |

for large k k, where the limiting function 𝒬 μ ​ ( t) \mathcal{Q}_{\mu}(t) is given by

 | 𝒬 μ ​ ( t):= τ M ​ μ ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) − ϱ p ​ φ ​ ( μ) p M ​ ( t − 1 2). \mathcal{Q}_{\mu}(t):=\tau_{M}\mu\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)-\frac{{\varrho_{p}}\varphi(\mu)}{p^{M}}\left(t-\frac{1}{2}\right). |  | (3.20) |

Furthermore, if for some k ≥ 0 k\geq 0,

 | 𝒬 μ ​ ( t) ≥ E μ, k ​ ( t) for all t ∈ [0, 1 2 − 1 2 ​ p] ∪ [1 2 + 1 2 ​ p, 1], \mathcal{Q}_{\mu}(t)\geq E_{\mu,k}(t)\qquad\text{for all}\quad t\in\left[0,\frac{1}{2}-\frac{1}{2p}\right]\cup\left[\frac{1}{2}+\frac{1}{2p},1\right], |  | (3.21) |

where

 | E μ, k ​ ( t):= τ M ​ ϱ p p M + k ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) ​ ( t − 1 2), E_{\mu,k}(t):=\frac{\tau_{M}{\varrho_{p}}}{p^{M+k}}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)\left(t-\frac{1}{2}\right), |  | (3.22) |

then G ⁡ ( μ) G(\mu) is the minimum of the function G G in the interval I M + k I_{M+k} (defined in ( 3.8)), and this minimum is attained only at μ \mu.

###### Proof.

For simplicity, we use the abbreviations (with an abuse of notation): ∇ G ​ ( θ):= G ⁡ ( θ k ​ ( t)) − G ⁡ ( μ) \nabla G(\theta):=G(\theta_{k}(t))-G(\mu), ∇ φ ​ ( θ):= φ ⁡ ( θ k ​ ( t)) − φ ⁡ ( μ) \nabla\varphi(\theta):=\varphi(\theta_{k}(t))-\varphi(\mu), ∇ φ:= φ ⁡ ( t) − φ ⁡ ( 1 2) \nabla\varphi:=\varphi(t)-\varphi(\frac{1}{2}), ∇ θ:= θ k ​ ( t) − μ \nabla\theta:=\theta_{k}(t)-\mu and ∇ t:= t − 1 2 \nabla t:=t-\frac{1}{2}. Observe first that a Taylor expansion yields

 | θ − ϱ p − μ − ϱ p + ϱ p ​ μ − ϱ p − 1 ​ ( θ − μ) = J θ, μ ​ μ − ϱ p − 1 ​ ( θ − μ) 2, \displaystyle\theta^{-{\varrho_{p}}}-\mu^{-{\varrho_{p}}}+{\varrho_{p}}\mu^{-{\varrho_{p}}-1}(\theta-\mu)=J_{\theta,\mu}\mu^{-{\varrho_{p}}-1}(\theta-\mu)^{2}, |  | (3.23) |

where

 | J θ, μ:= μ ϱ p + 1 ​ ϱ p ​ ( ϱ p + 1) ​ ∫ 0 1 x ​ ( μ ​ x + θ ⁡ ( 1 − x)) − ϱ p − 2 ​ d ​ x \displaystyle J_{\theta,\mu}:=\mu^{{\varrho_{p}}+1}{\varrho_{p}}({\varrho_{p}}+1)\int_{0}^{1}x(\mu x+\theta(1-x))^{-{\varrho_{p}}-2}\text{d}x |  | (3.24) |

remains positive whenever θ, μ > 0 \theta,\mu>0 and θ ≠ μ \theta\neq\mu (or t ≠ 1 2 t\neq\frac{1}{2}). Applying this expansion, we obtain

 | ∇ G ​ ( θ) \displaystyle\nabla G(\theta) | = θ k ​ ( t) − ϱ p ​ ( φ ⁡ ( θ k ​ ( t)) − φ ⁡ ( μ)) + φ ⁡ ( μ) ​ ( θ k ​ ( t) − ϱ p − μ − ϱ p) \displaystyle=\theta_{k}(t)^{-{\varrho_{p}}}\bigl(\varphi(\theta_{k}(t))-\varphi(\mu)\bigr)+\varphi(\mu)\bigl(\theta_{k}(t)^{-{\varrho_{p}}}-\mu^{-{\varrho_{p}}}\bigr) |  |

 |  | = μ − ϱ p − 1 ∇ φ ( θ) ( μ − ϱ p ∇ θ + J θ k ​ ( t), μ ( ∇ θ) 2) \displaystyle=\mu^{-{\varrho_{p}}-1}\nabla\varphi(\theta)\left(\mu-{\varrho_{p}}\nabla\theta+J_{\theta_{k}(t),\mu}\bigl(\nabla\theta\bigr)^{2}\right) |  |

 |  | − φ ( μ) μ − ϱ p − 1 ( ϱ p ∇ θ − J θ k ​ ( t), μ ( ∇ θ) 2); \displaystyle\qquad-\varphi(\mu)\mu^{-{\varrho_{p}}-1}\left({\varrho_{p}}\nabla\theta-J_{\theta_{k}(t),\mu}\bigl(\nabla\theta\bigr)^{2}\right); |  | (3.25) |

thus

 | μ ϱ p + 1 ∇ G ( θ) = μ ∇ φ ( θ) − ϱ p φ ( μ) ∇ θ − ϱ p ∇ φ ( θ) ∇ θ + J θ k ​ ( t), μ φ ( θ k ( t)) ( ∇ θ) 2. \begin{split}\mu^{{\varrho_{p}}+1}\nabla G(\theta)&=\mu\nabla\varphi(\theta)-{\varrho_{p}}\varphi(\mu)\nabla\theta-{\varrho_{p}}\nabla\varphi(\theta)\nabla\theta+J_{\theta_{k}(t),\mu}\varphi(\theta_{k}(t))\bigl(\nabla\theta\bigr)^{2}.\end{split} |  | (3.26) |

By ( 3.9)

 | p k ∇ θ = p − M ∇ t. p^{k}\nabla\theta=p^{-M}\nabla t. |  | (3.27) |

This, together with ( 3.26), Lemma 3.2, and the definitions ( 3.20) and ( 3.22) of 𝒬 μ \mathcal{Q}_{\mu} and E μ, k E_{\mu,k}, gives

 | p k ∇ G = μ − ϱ p − 1 ( 𝒬 μ ( t) − E μ, k ( t) + R μ, k ( t)), p^{k}\nabla G=\mu^{-{\varrho_{p}}-1}(\mathcal{Q}_{\mu}(t)-E_{\mu,k}(t)+R_{\mu,k}(t)), |  | (3.28) |

where

 | R μ, k ​ ( t):= p k ​ J θ k ​ ( t), μ ​ φ ​ ( θ k ​ ( t)) ​ ( ∇ θ) 2. \displaystyle R_{\mu,k}(t):=p^{k}J_{\theta_{k}(t),\mu}\varphi(\theta_{k}(t))\bigl(\nabla\theta\bigr)^{2}. |  | (3.29) |

We note for later use that, by ( 3.29) and ( 3.24),

 | R μ, k ( t) > 0, if θ k ( t) ≠ μ ( i.e., t ≠ 1 2). \displaystyle R_{\mu,k}(t)>0,\qquad\text{if }\theta_{k}(t)\neq\mu\quad(\text{i.e., }t\neq\tfrac{1}{2}). |  | (3.30) |

Since p p, M M, and ( a i) 1 M (a_{i})_{1}^{M} are fixed, and φ ⁡ ( t) \varphi(t) is bounded, we see that

 | R μ, k ​ ( t) = O ⁡ ( p − k), \displaystyle R_{\mu,k}(t)=O\left(p^{-k}\right), |  | (3.31) |

Similarly, ( 3.22) implies that

 | E μ, k ​ ( t) = O ⁡ ( p − k). E_{\mu,k}(t)=O\left(p^{-k}\right). |  | (3.32) |

Hence, ( 3.19) follows from ( 3.28), ( 3.31), and ( 3.32).

Now assume that ( 3.21) holds for some k k. Then it also holds for all larger k k as well, since E μ, k ​ ( t) ≥ 0 E_{\mu,k}(t)\geq 0 and the only factor in ( 3.22) that depends on k k is p − k p^{-k}.

Let x ∈ I M + k = [μ − 1 2 ​ p − ( M + k), μ + 1 2 ​ p − ( M + k)] x\in I_{M+k}=\left[\mu-\frac{1}{2}p^{-(M+k)},\mu+\frac{1}{2}p^{-(M+k)}\right] with x ≠ μ x\neq\mu. Let k x ≥ k k_{x}\geq k be the largest integer such that x ∈ I M + k x x\in I_{M+k_{x}}, and let t x ∈ [0, 1] t_{x}\in[0,1] be such that θ k x ​ ( t x) = x \theta_{k_{x}}(t_{x})=x. Then x ∉ I M + k x + 1 x\notin I_{M+k_{x}+1} and thus

 | t x ∈ [0, 1 2 − 1 2 ​ p) ∪ ( 1 2 + 1 2 ​ p, 1]. t_{x}\in\left[0,\frac{1}{2}-\frac{1}{2p}\right)\cup\left(\frac{1}{2}+\frac{1}{2p},1\right]. |  | (3.33) |

Hence, by ( 3.28), ( 3.30), and ( 3.21),

 | μ ϱ p + 1 ​ p k x ​ ( G ⁡ ( x) − G ⁡ ( μ)) = μ ϱ p + 1 ​ p k x ​ ( G ⁡ ( θ k x ​ ( t x)) − G ⁡ ( μ)) = 𝒬 μ ​ ( t x) − E μ, k x ​ ( t x) + R μ, k x ​ ( t x) > 𝒬 μ ​ ( t x) − E μ, k x ​ ( t x) ≥ 0. \begin{split}\mu^{{\varrho_{p}}+1}p^{k_{x}}\left(G(x)-G(\mu)\right)&=\mu^{{\varrho_{p}}+1}p^{k_{x}}\bigl(G(\theta_{k_{x}}(t_{x}))-G(\mu)\bigr)\\ &=\mathcal{Q}_{\mu}(t_{x})-E_{\mu,k_{x}}(t_{x})+R_{\mu,k_{x}}(t_{x})\\ &>\mathcal{Q}_{\mu}(t_{x})-E_{\mu,k_{x}}(t_{x})\geq 0.\end{split} |  | (3.34) |

Thus G ⁡ ( x) > G ⁡ ( μ) G(x)>G(\mu) for every x ≠ μ x\neq\mu in I M + k I_{M+k}, which shows that μ \mu is the unique minimum point of G G in the interval I M + k I_{M+k}. ∎

### 3.2 Monotonic majorization

Once we convert the minimality of G ⁡ ( s) G(s) at s = μ s=\mu in I M + k I_{M+k} to the positivity of Δ μ, k ​ ( t):= 𝒬 μ ​ ( t) − E μ, k ​ ( t) \Delta_{\mu,k}(t):=\mathcal{Q}_{\mu}(t)-E_{\mu,k}(t) for t t in the unit interval excluding a small neighborhood of t = 1 2 t=\frac{1}{2} (see ( 3.21)), we then need means of handling the positivity of the difference of two monotonic functions because Δ μ, k ​ ( t) \Delta_{\mu,k}(t) can be expressed as:

 | Δ μ, k ​ ( t): = 𝒬 μ ​ ( t) − E μ, k ​ ( t) = { ϱ p ​ φ ​ ( μ) p M ​ ( 1 2 − t) − τ M ​ ( φ ⁡ ( 1 2) − φ ⁡ ( t)) ​ ( μ + ϱ p p M + k ​ ( 1 2 − t)), if ​ t ∈ [0, 1 2], τ M ​ μ ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) − ϱ p p M ​ ( t − 1 2) ​ ( φ ⁡ ( μ) + τ M p k ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2))), if ​ t ∈ [1 2, 1], \begin{split}\Delta_{\mu,k}(t)&:=\mathcal{Q}_{\mu}(t)-E_{\mu,k}(t)\\ &=\begin{cases}\frac{{\varrho_{p}}\varphi(\mu)}{p^{M}}\left(\frac{1}{2}-t\right)-\tau_{M}\left(\varphi\left(\frac{1}{2}\right)-\varphi(t)\right)\left(\mu+\frac{{\varrho_{p}}}{p^{M+k}}\left(\frac{1}{2}-t\right)\right),&\text{if }t\in[0,\tfrac{1}{2}],\\ \tau_{M}\mu\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)-\frac{{\varrho_{p}}}{p^{M}}\left(t-\frac{1}{2}\right)\left(\varphi(\mu)+\frac{\tau_{M}}{p^{k}}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)\right),&\text{if }t\in[\frac{1}{2},1],\end{cases}\end{split} |  | (3.35) |

the first being the difference of two positive decreasing functions, the second that of two increasing functions, and the condition ( 3.21) then being equivalent to Δ μ, k ​ ( t) ≥ 0 \Delta_{\mu,k}(t)\geq 0.

On the other hand, G ⁡ ( s) = s − ϱ p ​ φ ​ ( s) G(s)=s^{-{\varrho_{p}}}\varphi(s) can also be regarded as the ratio of two increasing functions. Thus to show that G G attains nowhere the minimum value β \beta for s s outside a small neighborhood of μ \mu, we need to handle the ratio of two increasing functions.

Since the function φ ⁡ ( t) \varphi(t) is of fractal type, we use the following simple idea.

###### Lemma 3.4.

Assume that f, g f,g are increasing functions on [a, b] [a,b] with f ≥ 0 f\geq 0 and g > 0 g>0 there. If f ⁡ ( a) / g ⁡ ( b) > C f(a)/g(b)>C, then f ⁡ ( x) / g ⁡ ( x) > C f(x)/g(x)>C for x ∈ [a, b] x\in[a,b]. Similarly, if f ⁡ ( a) − g ⁡ ( b) > C f(a)-g(b)>C, then f ⁡ ( x) − g ⁡ ( x) > C f(x)-g(x)>C for x ∈ [a, b] x\in[a,b].

###### Proof.

By monotonicity, for x ∈ [a, b] x\in[a,b],

 | f ⁡ ( x) g ⁡ ( x) ≥ f ⁡ ( a) g ⁡ ( b) > C. \displaystyle\frac{f(x)}{g(x)}\geq\frac{f(a)}{g(b)}>C. |  | (3.36) |

The difference version is similar: f ⁡ ( x) − g ⁡ ( x) ≥ f ⁡ ( a) − g ⁡ ( b) > C f(x)-g(x)\geq f(a)-g(b)>C. ∎

The case when f, g f,g are decreasing functions is similar.

In particular, for δ > 0 \delta>0, if ( x + δ) − ϱ p ​ φ ​ ( x) > β (x+\delta)^{-{\varrho_{p}}}\varphi(x)>\beta, then G ⁡ ( t) = t − ϱ p ​ φ ​ ( t) > β G(t)=t^{-{\varrho_{p}}}\varphi(t)>\beta for t ∈ [x, x + δ] t\in[x,x+\delta].

Such a simple idea will be applied numerically to sufficiently small subintervals after a suitable partition of the target interval.

## 4 Proof of Theorem 1.1 for p = 3, 5, 7 p=3,5,7

We begin with the proof of ( 1.13). Again p ≥ 3 p\geq 3 is a prime number.

###### Lemma 4.1.

G ⁡ ( s ^ p) = B ξ, η G(\hat{s}_{p})=B_{\xi,\eta} given in ( 1.13), where s ^ p = 2 ​ ξ + 1 2 ​ p − η p 2 \hat{s}_{p}=\frac{2\xi+1}{2p}-\frac{\eta}{p^{2}}.

###### Proof.

The p p -ary expansion of s ^ p \hat{s}_{p} has the form s ^ p = ( 0. b 1 b 2 …) p \hat{s}_{p}=(0.b_{1}b_{2}\dots)_{p} with b 1 = ξ b_{1}=\xi, b 2 = p − 1 2 − η b_{2}=\frac{p-1}{2}-\eta and b j = p − 1 2 b_{j}=\frac{p-1}{2} for j ≥ 3 j\geq 3. Then, by ( 2.11),

 | 2 ​ φ ​ ( s ^ p) ξ + 1 \displaystyle\frac{2\varphi(\hat{s}_{p})}{\xi+1} | = ξ A + 1 A 2 ​ ( p − 1 2 − η) ​ ( p + 1 2 − η) \displaystyle=\frac{\xi}{A}+\frac{1}{A^{2}}\left(\frac{p-1}{2}-\eta\right)\left(\frac{p+1}{2}-\eta\right) |  |

 |  | + p − 1 2 ( p + 1 2 − η) ∑ k ≥ 3 1 A k ( p + 1 2) k − 2 \displaystyle\qquad+\frac{p-1}{2}\left(\frac{p+1}{2}-\eta\right)\sum_{k\geq 3}\frac{1}{A^{k}}\left(\frac{p+1}{2}\right)^{k-2} |  |

 |  | = ξ A + ( p − 2 ​ η) ​ ( p − 2 ​ η + 1) 4 ​ A 2, \displaystyle=\frac{\xi}{A}+\frac{(p-2\eta)(p-2\eta+1)}{4A^{2}}, |  | (4.1) |

or

 | φ ⁡ ( s ^ p) = ξ + 1 2 ​ A ​ ( ξ + ( p − 2 ​ η) ​ ( p − 2 ​ η + 1) 2 ​ p ​ ( p + 1)). \displaystyle\varphi(\hat{s}_{p})=\frac{\xi+1}{2A}\left(\xi+\frac{(p-2\eta)(p-2\eta+1)}{2p(p+1)}\right). |  | (4.2) |

Thus

 | G ⁡ ( s ^ p) = s ^ p − ϱ p ​ φ ​ ( s ^ p) = ξ + 1 2 ​ ( ξ + ( p − 2 ​ η) ​ ( p − 2 ​ η + 1) 2 ​ p ​ ( p + 1)) ​ ( 2 ​ ξ + 1 2 − η p) − ϱ p, \displaystyle G(\hat{s}_{p})=\hat{s}_{p}^{-{\varrho_{p}}}\varphi(\hat{s}_{p})=\frac{\xi+1}{2}\left(\xi+\frac{(p-2\eta)(p-2\eta+1)}{2p(p+1)}\right)\left(\frac{2\xi+1}{2}-\frac{\eta}{p}\right)^{-\varrho_{p}}, |  | (4.3) |

which is the same as ( 1.13). ∎

We prove Wilson’s conjecture for p = 3, 5, 7 p=3,5,7, and establish the values β 3 \beta_{3}, β 5 \beta_{5}, β 7 \beta_{7} in ( 1.8) and ( 1.10). Let s 1:= s ^ p ​ ( 1, 0) = 3 2 ​ p s_{1}:=\hat{s}_{p}(1,0)=\frac{3}{2p}, whose p p -ary expansion is of the form ( 0.1 ​ b ​ b ​ b ​ …) p (0.1bbb\dots)_{p}, where b = p − 1 2 b=\frac{p-1}{2}.

### 4.1 Minimality of G ⁡ ( s) G(s) in I 2 = [3 2 ​ p − 1 2 ​ p 2, 3 2 ​ p + 1 2 ​ p 2] I_{2}=[\frac{3}{2p}-\frac{1}{2p^{2}},\frac{3}{2p}+\frac{1}{2p^{2}}]

Take m = M = 1 m=M=1 and k = 1 k=1 in Theorem 3.3 so that μ = s 1 = 3 2 ​ p \mu=s_{1}=\frac{3}{2p} and I 2 = [3 2 ​ p − 1 2 ​ p 2, 3 2 ​ p + 1 2 ​ p 2] I_{2}=[\frac{3}{2p}-\frac{1}{2p^{2}},\frac{3}{2p}+\frac{1}{2p^{2}}]. We have a 1 = 1 a_{1}=1 and we obtain from ( 3.13) and ( 4.2) with ( ξ, η) = ( 1, 0) (\xi,\eta)=(1,0),

 | τ 1 = 2 A and φ ⁡ ( μ) = 3 2 ​ A. \displaystyle\tau_{1}=\frac{2}{A}\qquad\text{and}\qquad\varphi(\mu)=\frac{3}{2A}. |  | (4.4) |

Then ( 3.20) and ( 3.22) in Theorem 3.3 yield

 | 𝒬 s 1 ​ ( t) \displaystyle\mathcal{Q}_{s_{1}}(t) | = 3 p ​ A ( φ ⁡ ( t) − φ ⁡ ( 1 2) ⏟ =: K 1 ​ ( t) − ϱ p 2 ​ ( t − 1 2) ⏟ =: K 2 ​ ( t)), \displaystyle=\frac{3}{pA}\biggl(\underbrace{\varphi(t)-\varphi\left(\frac{1}{2}\right)}_{=:K_{1}(t)}\underbrace{-\frac{{\varrho_{p}}}{2}\left(t-\frac{1}{2}\right)}_{=:K_{2}(t)}\biggr), |  | (4.5) |

and

 | E s 1, 1 ​ ( t) = 2 ​ ϱ p A ​ p 2 ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) ​ ( t − 1 2) =: 3 p ​ A ​ K 3 ​ ( t). E_{s_{1},1}(t)=\frac{2{\varrho_{p}}}{Ap^{2}}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)\left(t-\frac{1}{2}\right)=:\frac{3}{pA}K_{3}(t). |  | (4.6) |

Thus, we can write

 | p ​ A 3 ​ Δ μ, 1 ​ ( t) = { K 2 ​ ( t) − ( − K 1 ​ ( t) + K 3 ​ ( t)), if ​ t ∈ [0, 1 2], K 1 ​ ( t) − ( − K 2 ​ ( t) + K 3 ​ ( t)), if ​ t ∈ [1 2, 1], \displaystyle\frac{pA}{3}\,\Delta_{\mu,1}(t)=\begin{cases}K_{2}(t)-(-K_{1}(t)+K_{3}(t)),&\text{if }t\in[0,\frac{1}{2}],\\ K_{1}(t)-(-K_{2}(t)+K_{3}(t)),&\text{if }t\in[\frac{1}{2},1],\end{cases} |  | (4.7) |

where K 2 ​ ( t) K_{2}(t) and − K 1 ​ ( t) + K 3 ​ ( t) -K_{1}(t)+K_{3}(t) are both positive and decreasing for t ∈ [0, 1 2] t\in[0,\frac{1}{2}], and K 1 ​ ( t) K_{1}(t) and − K 2 ​ ( t) + K 3 ​ ( t) -K_{2}(t)+K_{3}(t) are both positive and increasing for t ∈ [1 2, 1] t\in[\frac{1}{2},1]. According to Theorem 3.3, if

 | Δ μ, 1 ​ ( t) ≥ 0 for t ∈ [0, 1 2 − 1 2 ​ p] ∪ [1 2 + 1 2 ​ p, 1], \displaystyle\Delta_{\mu,1}(t)\geq 0\quad\text{for}\quad t\in\left[0,\frac{1}{2}-\frac{1}{2p}\right]\cup\left[\frac{1}{2}+\frac{1}{2p},1\right], |  | (4.8) |

then s 1 s_{1} is the minimum of G ⁡ ( s) G(s) for s ∈ [1 2 − 1 2 ​ p 2, 1 2 + 1 2 ​ p 2] s\in[\frac{1}{2}-\frac{1}{2p^{2}},\frac{1}{2}+\frac{1}{2p^{2}}]. To check the validity of ( 4.8), we partition the two intervals in ( 4.8) into equally-spaced subintervals in each of which we apply the idea used in Lemma 3.4; namely, for some (large) integers N 1 N_{1} and N 2 N_{2},

 | { K 2 ​ ( t j + 1) − ( − K 1 ​ ( t j) + K 3 ​ ( t j)) ≥ 0, with ​ t j = ( p − 1) ​ j 2 ​ p ​ N 1, K 1 ​ ( t ~ j) − ( − K 2 ​ ( t ~ j + 1) + K 3 ​ ( t ~ j + 1)) ≥ 0, with ​ t ~ j = 1 2 + 1 2 ​ p + ( p − 1) ​ j 2 ​ p ​ N 2, \displaystyle\begin{cases}K_{2}(t_{j+1})-\left(-K_{1}(t_{j})+K_{3}(t_{j})\right)\geq 0,&\text{with }t_{j}=\frac{(p-1)j}{2pN_{1}},\\ K_{1}(\tilde{t}_{j})-\left(-K_{2}(\tilde{t}_{j+1})+K_{3}(\tilde{t}_{j+1})\right)\geq 0,&\text{with }\tilde{t}_{j}=\frac{1}{2}+\frac{1}{2p}+\frac{(p-1)j}{2pN_{2}},\end{cases} |  | (4.9) |

for j = 0, 1, …, N i − 1 j=0,1,\dots,N_{i}-1, i = 1, 2 i=1,2. This process is purely numerical and brings the condition ( 4.8) into a finitely computable one.

For example, take p = 3 p=3. Then N 1 = 9 N_{1}=9 is sufficient for t ∈ [0, 1 2 − 1 2 ​ p] t\in[0,\frac{1}{2}-\frac{1}{2p}], and N 2 = 7 N_{2}=7 for t ∈ [1 2 + 1 2 ​ p, 1] t\in[\frac{1}{2}+\frac{1}{2p},1]. More precisely, we have the numerical values in each case:

Δ μ, 1 ​ ( t) > K 2 ​ ( t j + 1) − ( − K 1 ​ ( t j) + K 3 ​ ( t j)) \Delta_{\mu,1}(t)>K_{2}(t_{j+1})-\left(-K_{1}(t_{j})+K_{3}(t_{j})\right), t j = ( p − 1) ​ j 2 ​ p ​ N 1 t_{j}=\frac{(p-1)j}{2pN_{1}} & N 1 = 9 N_{1}=9 |

j j | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 | 8 8 | 9 9 |

Δ μ, 1 > \Delta_{\mu,1}> | 0.082 0.082 | 0.060 0.060 | 0.044 0.044 | 0.033 0.033 | 0.016 0.016 | 0.009 0.009 | 0.012 0.012 | 0.00001 0.00001 | 0.001 0.001 |

Δ μ, 1 ​ ( t) > K 1 ​ ( t ~ j) − ( − K 2 ​ ( t ~ j + 1) + K 3 ​ ( t ~ j + 1)) \Delta_{\mu,1}(t)>K_{1}(\tilde{t}_{j})-\left(-K_{2}(\tilde{t}_{j+1})+K_{3}(\tilde{t}_{j+1})\right) t ~ j = 1 2 + 1 2 ​ p + ( p − 1) ​ j 2 ​ p ​ N 2 \tilde{t}_{j}=\frac{1}{2}+\frac{1}{2p}+\frac{(p-1)j}{2pN_{2}} & N 2 = 7 N_{2}=7 |

j j | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 |

Δ μ, 1 > \Delta_{\mu,1}> | 0.054 0.054 | 0.023 0.023 | 0.013 0.013 | 0.006 0.006 | 0.016 0.016 | 0.043 0.043 | 0.023 0.023 |

Similarly, for p = 5 p=5, we use ( N 1, N 2) = ( 35, 10) (N_{1},N_{2})=(35,10), and for p = 7 p=7, ( N 1, N 2) = ( 114, 17) (N_{1},N_{2})=(114,17), respectively.

In this way, we prove, by Theorem 3.3, that s = s 1 = 3 2 ​ p s=s_{1}=\frac{3}{2p} is the minimum of G ⁡ ( s) G(s) for s ∈ I 2 = [s 1 − 1 2 ​ p 2, s 1 + 1 2 ​ p 2] s\in I_{2}=[s_{1}-\frac{1}{2p^{2}},s_{1}+\frac{1}{2p^{2}}].

### 4.2 G ⁡ ( s) G(s) in [1 p, 1] ∖ I 2 [\frac{1}{p},1]\setminus I_{2}

Following the same numerical procedure used above for justifying the minimality of G ⁡ ( s) G(s) at s = s 1 s=s_{1} for s ∈ I 2 s\in I_{2}, we partition the two intervals [1 p, 3 2 ​ p − 1 2 ​ p 2] [\frac{1}{p},\frac{3}{2p}-\frac{1}{2p^{2}}] and [3 2 ​ p + 1 2 ​ p 2, 1] [\frac{3}{2p}+\frac{1}{2p^{2}},1] into N 3 N_{3} and N 4 N_{4} subintervals, and check, by the simple monotonic bounds in Lemma 3.4, that G ⁡ ( s) > β G(s)>\beta for s s in each of these subintervals.

Since G ⁡ ( s) = s − ϱ p ​ φ ​ ( s) G(s)=s^{-{\varrho_{p}}}\varphi(s) is the ratio of two increasing functions in the unit interval, we check the conditions

 | G ⁡ ( s) − β > { σ j + 1 − ϱ p ​ φ ​ ( σ j) − β > 0, if ​ σ j:= 1 p + ( p − 1) ​ j 2 ​ p 2 ​ N 3, j = 0, …, N 3 − 1 σ ~ j + 1 − ϱ p ​ φ ​ ( σ ~ j) − β > 0, if ​ σ ~ j:= 3 2 ​ p + 1 2 ​ p 2 + ( 2 ​ p 2 − 3 ​ p − 1) ​ j 2 ​ p 2 ​ N 4, j = 0, 1, …, N 4 − 1, \begin{split}&G(s)-\beta\\ &\quad>\left\{\begin{array}[]{lll}\sigma_{j+1}^{-{\varrho_{p}}}\varphi(\sigma_{j})-\beta>0,&\text{if }\sigma_{j}:=\frac{1}{p}+\frac{(p-1)j}{2p^{2}N_{3}},&j=0,\dots,N_{3}-1\\ \tilde{\sigma}_{j+1}^{-{\varrho_{p}}}\varphi(\tilde{\sigma}_{j})-\beta>0,&\text{if }\tilde{\sigma}_{j}:=\frac{3}{2p}+\frac{1}{2p^{2}}+\frac{(2p^{2}-3p-1)j}{2p^{2}N_{4}},&j=0,1,\dots,N_{4}-1,\end{array}\right.\end{split} |  | (4.10) |

for s s in each of the subintervals [σ j, σ j + 1] [\sigma_{j},\sigma_{j+1}] and [σ ~ j, σ ~ j + 1] [\tilde{\sigma}_{j},\tilde{\sigma}_{j+1}], respectively.

For example, for p = 3 p=3, we can take N 3 = 9 N_{3}=9 and N 4 = 16 N_{4}=16 for which the corresponding numerical values are listed as follows.

G ⁡ ( s) − β > σ j + 1 − ϱ p ​ φ ​ ( σ j) − β > 0 G(s)-\beta>\sigma_{j+1}^{-{\varrho_{p}}}\varphi(\sigma_{j})-\beta>0, σ j \sigma_{j} given in ( 4.10) & N 3 = 9 N_{3}=9 |

j j | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 | 8 8 | 9 9 |

σ j + 1 − ϱ p ​ φ ​ ( σ j) − β \sigma_{j+1}^{-{\varrho_{p}}}\varphi(\sigma_{j})-\beta | 0.168 0.168 | 0.123 0.123 | 0.091 0.091 | 0.067 0.067 | 0.040 0.040 | 0.027 0.027 | 0.023 0.023 | 0.008 0.008 | 0.008 0.008 |

G ⁡ ( s) − β > σ ~ j + 1 − ϱ p ​ φ ​ ( σ ~ j) − β > 0 G(s)-\beta>\tilde{\sigma}_{j+1}^{-{\varrho_{p}}}\varphi(\tilde{\sigma}_{j})-\beta>0, σ ~ j \tilde{\sigma}_{j} given in ( 4.10) & N 4 = 16 N_{4}=16 |

j j | 1 1 | 2 2 | 3 3 | 4 4 | 5 5 | 6 6 | 7 7 | 8 8 |

σ ~ j + 1 − ϱ p ​ φ ​ ( σ ~ j) − β \tilde{\sigma}_{j+1}^{-{\varrho_{p}}}\varphi(\tilde{\sigma}_{j})-\beta) | 0.029 0.029 | 0.002 0.002 | 0.006 0.006 | 0.044 0.044 | 0.131 0.131 | 0.090 0.090 | 0.060 0.060 | 0.049 0.049 |

j j | 9 9 | 10 10 | 11 11 | 12 12 | 13 13 | 14 14 | 15 15 | 16 16 |

σ ~ j + 1 − ϱ p ​ φ ​ ( σ ~ j) − β \tilde{\sigma}_{j+1}^{-{\varrho_{p}}}\varphi(\tilde{\sigma}_{j})-\beta | 0.054 0.054 | 0.033 0.033 | 0.026 0.026 | 0.042 0.042 | 0.088 0.088 | 0.076 0.076 | 0.079 0.079 | 0.112 0.112 |

Similarly, for p = 5 p=5, we can take ( N 3, N 4) = ( 35, 77) (N_{3},N_{4})=(35,77), and for p = 7 p=7, ( N 3, N 4) = ( 147,214) (N_{3},N_{4})=(147,214). This completes the proof that G ⁡ ( s) G(s) attains its minimum in [1 p, 1] [\frac{1}{p},1] at s 1 s_{1} for p = 3, 5, 7 p=3,5,7; consequently β p = G ⁡ ( s 1) \beta_{p}=G(s_{1}) which yields the values β 3 \beta_{3}, β 5 \beta_{5}, β 7 \beta_{7} in ( 1.8) and ( 1.10) and proves Theorem 1.1 (and Wilson’s conjecture) for these p p.

 |  |  |

Figure 1: Fluctuations of G ⁡ ( s) G(s), s ∈ [p − 1, 1] s\in[p^{-1},1], for p = 3, 5, 7 p=3,5,7.

 |  |  |

Figure 2: Graphical rendering of 𝒬 s 1 ​ ( t) \mathcal{Q}_{s_{1}}(t) (in blue) and E s 1, 1 ​ ( t) E_{s_{1},1}(t) (in red) for p = 3, 5, 7 p=3,5,7.

 |  |  |

Figure 3: A closer look at the fluctuations of G G in the smaller interval [1 p, 2 p] \bigl[\frac{1}{p},\frac{2}{p}\bigr] for p = 3, 5, 7 p=3,5,7.

## 5 Proof of Theorem 1.1 for p ≥ 11 p\geq 11

When p ≥ 11 p\geq 11, we take M = 2 M=2, k = 0 k=0 and μ = s ^ p ​ ( ξ, η) = 2 ​ ξ + 1 2 ​ p − η p 2 \mu=\hat{s}_{p}(\xi,\eta)=\frac{2\xi+1}{2p}-\frac{\eta}{p^{2}} in Theorem 3.3, so that a 1 = ξ a_{1}=\xi, a 2 = p − 1 2 − η a_{2}=\frac{p-1}{2}-\eta (recall ( 1.12) and ( 3.11)). Then ( 3.13) yields

 | τ 2 = ( ξ + 1) ​ ( p + 1 − 2 ​ η) 2 ​ A 2, \displaystyle\tau_{2}=\frac{(\xi+1)(p+1-2\eta)}{2A^{2}}, |  | (5.1) |

and φ ⁡ ( μ) \varphi(\mu) is given in ( 4.2). Thus ( 3.20) and ( 3.22) yield

 | p 2 ​ ( 𝒬 μ ​ ( t) − E μ, 0 ​ ( t)) ϱ p ​ φ ​ ( μ) \displaystyle\frac{p^{2}(\mathcal{Q}_{\mu}(t)-E_{\mu,0}(t))}{{\varrho_{p}}\varphi(\mu)} | = C ⁡ ( t) ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) − ( t − 1 2), \displaystyle=C(t)\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)-\left(t-\frac{1}{2}\right), |  | (5.2) |

where

 | C ⁡ ( t):= τ 2 ϱ p ​ φ ​ ( μ) ​ ( p 2 ​ μ − ϱ p ​ ( t − 1 2)). \displaystyle C(t):=\frac{\tau_{2}}{{\varrho_{p}}\varphi(\mu)}\left(p^{2}\mu-{\varrho_{p}}\left(t-\frac{1}{2}\right)\right). |  | (5.3) |

### 5.1 p = 11, 13, 17, 19, 23 p=11,13,17,19,23: ( ξ, η) = ( 1, 1) (\xi,\eta)=(1,1)

For p = 11 p=11, s 1 = 3 22 = 0.13636 ​ … s_{1}=\frac{3}{22}=0.13636\dots is no longer the minimum point of G G; see Figures 4 and 5. In this case, Wilson [16] conjectured (in an equivalent form) that the minimum occurs at s 2:= s 1 − 1 p 2 = 0.12809 ​ … s_{2}:=s_{1}-\frac{1}{p^{2}}=0.12809\dots, which yields his conjecture for β 11 \beta_{11} in ( 1.10); see Lemma 4.1. (In base 11 11, s 2 = 0.14555 ​ … s_{2}=0.14555\dots.) Numerically, we have G ⁡ ( s 1) = 0.7386 ​ … G(s_{1})=0.7386\ldots and G ⁡ ( s 2) = 0.7364 ​ … G(s_{2})=0.7364\ldots.

To verify his conjecture, we apply Theorem 3.3 with M = 2, k = 0 M=2,k=0 and ( ξ, η) = ( 1, 1) (\xi,\eta)=(1,1); thus μ = s 2 = 3 2 ​ p − 1 p 2 \mu=s_{2}=\frac{3}{2p}-\frac{1}{p^{2}}, which gives a 1 = 1 a_{1}=1, a 2 = p − 3 2 a_{2}=\frac{p-3}{2}, and then by ( 3.20)

 | 𝒬 s 2 ​ ( t) = ( p − 1) ​ s 2 A 2 ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) − ϱ p p 2 ​ φ ​ ( s 2) ​ ( t − 1 2), \mathcal{Q}_{s_{2}}(t)=\frac{(p-1)s_{2}}{A^{2}}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)-\frac{{\varrho_{p}}}{p^{2}}\varphi(s_{2})\left(t-\frac{1}{2}\right), |  | (5.4) |

and by ( 3.22)

 | E s 2, 0 ​ ( t) = ( p − 1) ​ ϱ p p k + 2 ​ A 2 ​ ( φ ⁡ ( t) − φ ⁡ ( 1 2)) ​ ( t − 1 2); E_{s_{2},0}(t)=\frac{(p-1){\varrho_{p}}}{p^{k+2}A^{2}}\left(\varphi(t)-\varphi\left(\frac{1}{2}\right)\right)\left(t-\frac{1}{2}\right); |  | (5.5) |

see Figure 4 for an illustration of the different effects for 𝒬 μ ​ ( t) \mathcal{Q}_{\mu}(t) and E μ, k ​ ( t) E_{\mu,k}(t) between s 1 s_{1} and s 2 s_{2}.

The same numerical recipes used in the previous section for p = 3, 5, 7 p=3,5,7 applies here with ( N 1, N 2) = ( 40,148) (N_{1},N_{2})=(40,148), which shows that ( 3.21) holds for μ = s 2 \mu=s_{2} and k = 0 k=0, but not for μ = s 1 \mu=s_{1}. Thus, Theorem 3.3 guarantees that G ⁡ ( s 2) G(s_{2}) is the minimum of G G in the interval I 2 = [15 11 2, 16 11 2] I_{2}=\left[\frac{15}{11^{2}},\frac{16}{11^{2}}\right]. The same bounding techniques with ( N 3, N 4) = ( 32,236) (N_{3},N_{4})=(32,236) also shows (see Figure 5) that G ⁡ ( s) > G ⁡ ( s 2) G(s)>G(s_{2}) outside [15 11 2, 16 11 2] \left[\frac{15}{11^{2}},\frac{16}{11^{2}}\right]. Thus, G ⁡ ( s 2) G(s_{2}) is the minimum, and β 11 = G ⁡ ( s 2) \beta_{11}=G(s_{2}) (see ( 1.10)).

 |  |

𝒬 s 1 ​ ( t) \mathcal{Q}_{s_{1}}(t) vs E s 1, 0 E_{s_{1},0} | 𝒬 s 2 ​ ( t) \mathcal{Q}_{s_{2}}(t) vs E s 2, 0 ​ ( t) E_{s_{2},0}(t) |

Figure 4: p = 11 p=11: 𝒬 s i ​ ( t) \mathcal{Q}_{s_{i}}(t) (in blue) and E s i, 0 E_{s_{i},0} (in red) for i = 1, 2 i=1,2.

 |  |

Figure 5: p = 11 p=11: G ⁡ ( x) G(x) for x ∈ [1 11, 1] x\in\left[\frac{1}{11},1\right] (left) and [14 11 2, 17 11 2] \left[\frac{14}{11^{2}},\frac{17}{11^{2}}\right] (right), respectively.

Similarly, the same procedure applies to p = 13, 17, 19, 23 p=13,17,19,23 with

p p | ( N 1, N 2, N 3, N 4) (N_{1},N_{2},N_{3},N_{4}) |

13 13 | ( 62,131, 53, 373) (62,131,53,373) |

17 17 | ( 135,132,134,331) (135,132,134,331) |

19 19 | ( 211,144,257, 1517) (211,144,257,1517) |

23 23 | ( 611,151,992, 6812) (611,151,992,6812) |

for which G G also attains its minimum β p \beta_{p} at s 2 s_{2}; see Figures 6 and 7.

This proves Theorem 1.1 for 11 ≤ p ≤ 23 11\leq p\leq 23. Using Lemma 4.1, we obtain the values of β p \beta_{p}:

p p | 13 13 | 17 17 | 19 19 | 23 23 |

β p \beta_{p} | 124 91 ​ ( 26 37) ϱ 13 \dfrac{124}{91}\Bigl(\dfrac{26}{37}\Bigr)^{\varrho_{13}} | 71 51 ​ ( 34 49) ϱ 17 \dfrac{71}{51}\Bigl(\dfrac{34}{49}\Bigr)^{\varrho_{17}} | 533 380 ​ ( 38 55) ϱ 19 \dfrac{533}{380}\Bigl(\dfrac{38}{55}\Bigr)^{\varrho_{19}} | 261 184 ​ ( 46 67) ϱ 23 \dfrac{261}{184}\Bigl(\dfrac{46}{67}\Bigr)^{\varrho_{23}} |

### 5.2 p = 29 p=29: ( ξ, η) = ( 2, 1) (\xi,\eta)=(2,1)

For p = 29 p=29, s 2 = s ^ p ​ ( 1, 1) = 3 2 ​ p − 1 p 2 s_{2}=\hat{s}_{p}(1,1)=\frac{3}{2p}-\frac{1}{p^{2}} is no longer the global minimum point of G ⁡ ( s) G(s). Instead s ^ p ​ ( 1, 2) = 3 2 ​ p − 2 p 2 \hat{s}_{p}(1,2)=\frac{3}{2p}-\frac{2}{p^{2}} gives a smaller value of G ⁡ ( s) G(s), and an even smaller value of G G is reached at s 3:= s ^ p ​ ( 2, 1) = 5 2 ​ p − 1 p 2 s_{3}:=\hat{s}_{p}(2,1)=\frac{5}{2p}-\frac{1}{p^{2}}, which can be proved to be the minimum point by Theorem 3.3 with the same numerical recipes used above.

When it comes to numerical check, a direct use of the preceding numerical recipes gives the (minimum) numbers of partitions required in each of the intervals [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}], [1 2 + 1 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},1], [1 p, 5 2 ​ p − 3 2 ​ p 2] [\frac{1}{p},\frac{5}{2p}-\frac{3}{2p^{2}}] and [5 2 ​ p − 1 2 ​ p 2] [\frac{5}{2p}-\frac{1}{2p^{2}}]: ( N 1, N 2, N 3, N 4) = ( 3011,216, 14996, 11942) (N_{1},N_{2},N_{3},N_{4})=(3011,216,14996,11942), respectively, which are somewhat too large. We used above subintervals of the same length, but this is not optimal, and the computational complexity can be reduced by the following procedure: instead of fixing first the interval and then finding a large enough number of subintervals (of equal length) such that the monotonicity inequality holds in each of the subintervals, we fix first N N, the number of subintervals to be processed in each step, and then check either from the left end or the right end of the interval how far towards the other end of the interval we can go with N N subintervals of the same size such that the monotonicity inequality holds in all subintervals. Then repeat the same procedure until reaching the other end of the interval. Alternatively, a binary splitting technique of the target interval can be used to identify a range where N N partitions suffice.

For example, to check if 𝒬 s 3 ​ ( t) > E s 3, 0 ​ ( t) \mathcal{Q}_{s_{3}}(t)>E_{s_{3},0}(t) holds in the interval [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}], we choose, say N = p 2 = 841 N=p^{2}=841, which then suffices if we partition first [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}] into the two subintervals [0, 1 2 − 4 p] [0,\frac{1}{2}-\frac{4}{p}] and [1 2 − 4 p, 1 2 − 1 2 ​ p] [\frac{1}{2}-\frac{4}{p},\frac{1}{2}-\frac{1}{2p}], and then further partition each into N + 1 N+1 smaller subintervals before checking the monotonicity inequality. Similarly, instead of using N 3 = 14996 N_{3}=14996 for the interval [1 p, 5 2 ​ p − 3 2 ​ p 2] [\frac{1}{p},\frac{5}{2p}-\frac{3}{2p^{2}}], we choose again N = p 2 N=p^{2} and split first this interval into [1 p, 3 p 2] [\frac{1}{p},\frac{3}{p^{2}}] and [5 2 ​ p − 3 p 2, 5 2 ​ p − 3 2 ​ p 2] [\frac{5}{2p}-\frac{3}{p^{2}},\frac{5}{2p}-\frac{3}{2p^{2}}] before the numerical check in both subintervals. Finally, the use of the number N 4 = 11942 N_{4}=11942 for the interval [5 2 ​ p − 1 2 ​ p 2, 1] [\frac{5}{2p}-\frac{1}{2p^{2}},1] can be replaced by taking N = p 2 N=p^{2} and splitting [5 2 ​ p − 1 2 ​ p 2, 1] [\frac{5}{2p}-\frac{1}{2p^{2}},1] into [5 2 ​ p − 1 2 ​ p 2, 4 p] [\frac{5}{2p}-\frac{1}{2p^{2}},\frac{4}{p}] and [4 p, 1] [\frac{4}{p},1].

### 5.3 Primes from 31 31 to 113 113: ξ = 2 \xi=2

Exactly the same method of proof used above applies to higher values of p p with the minimum point of G G in [1 p, 1] [\frac{1}{p},1] given in ( 1.1). The two-stage partitioning procedure is computationally more efficient. For example, when p = 113 p=113, we have:

variable | Interval | first partition | split each into N N subintervals (equal spacing) |

t t | [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}] | [0, 1 2 − 3 p] ∪ [1 2 − 3 p, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{3}{p}]\cup[\frac{1}{2}-\frac{3}{p},\frac{1}{2}-\frac{1}{2p}] | N = 500 N=500 |

[1 2 + 1 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},1] | [1 2 + 1 2 ​ p, 1 2 + 7 2 ​ p] ∪ [1 2 + 1 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},\frac{1}{2}+\frac{7}{2p}]\cup[\frac{1}{2}+\frac{1}{2p},1] | N = 700 N=700 |

s s | [1 p, 5 2 ​ p − 11 2 ​ p 2] [\frac{1}{p},\frac{5}{2p}-\frac{11}{2p^{2}}] | [1 p, 5 2 ​ p − 11 p 2] ∪ [5 2 ​ p − 11 p 2, 5 2 ​ p − 11 2 ​ p 2] [\frac{1}{p},\frac{5}{2p}-\frac{11}{p^{2}}]\cup[\frac{5}{2p}-\frac{11}{p^{2}},\frac{5}{2p}-\frac{11}{2p^{2}}] | N = 500 N=500 |

[5 2 ​ p − 9 2 ​ p 2, 1] [\frac{5}{2p}-\frac{9}{2p^{2}},1] | [5 2 ​ p − 9 2 ​ p 2, 5 2 ​ p] [\frac{5}{2p}-\frac{9}{2p^{2}},\frac{5}{2p}] ∪ \cup [5 2 ​ p, 5 p] [\frac{5}{2p},\frac{5}{p}] ∪ \cup [5 p, 1] [\frac{5}{p},1] | N = 5000 N=5000 |

 |  |  |

Figure 6: A graphical rendering of G ⁡ ( s) G(s) for p = 13, 17, 19 p=13,17,19.

 |  |  |

 |  |  |

Figure 7: 𝒬 s 2 ​ ( t) \mathcal{Q}_{s_{2}}(t) (in blue) vs E s 2, 0 ​ ( t) E_{s_{2},0}(t) (in red) for p = 13, 17, 19 p=13,17,19.

## 6 p ≥ 127 p\geq 127

In this section, we discuss briefly the extension of our approach to larger primes.

### 6.1 p = 127, …, 2221 p=127,\dots,2221

The same approach used so far is readily extended to primes of larger values. As far as our numerical check was conducted, the minimum G ⁡ ( s) G(s) is always reached at s = s ^ p = 2 ​ ξ + 1 2 ​ p − η p 2 s=\hat{s}_{p}=\frac{2\xi+1}{2p}-\frac{\eta}{p^{2}} for a suitable choice of ( ξ, η) (\xi,\eta); consequently, then β p \beta_{p} is given by ( 1.13). In general, the first-stage partition can be chosen by standard binary search. The following table shows the choices of ( ξ, η) (\xi,\eta) for p ≤ 2221 p\leq 2221.

3 3 – 7 7 | 11 11 – 23 23 | 29 29 | 31 31 – 53 53 | 59 59 – 79 79 | 83 83 – 107 107 |

( 1, 0) (1,0) | ( 1, 1) (1,1) | ( 2, 1) (2,1) | ( 2, 2) (2,2) | ( 2, 3) (2,3) | ( 2, 4) (2,4) |

109 109 – 113 113 | 127 127 – 139 139 | 149 149 – 173 173 | 179 179 – 199 199 | 211 211 – 241 241 | 251 251 – 277 277 |

( 2, 5) (2,5) | ( 3, 5) (3,5) | ( 3, 6) (3,6) | ( 3, 7) (3,7) | ( 3, 8) (3,8) | ( 3, 9) (3,9) |

281 281 – 311 311 | 313 313 – 347 347 | 349 349 – 383 383 | 389 389 – 419 419 | 421 421 – 449 449 | 457 457 – 487 487 |

( 3, 10) (3,10) | ( 3, 11) (3,11) | ( 3, 12) (3,12) | ( 3, 13) (3,13) | ( 3, 14) (3,14) | ( 3, 15) (3,15) |

491 491 – 509 509 | 521 521 – 547 547 | 557 557 – 587 587 | 593 593 – 619 619 | 631 631 – 661 661 | 673 673 – 701 701 |

( 4, 15) (4,15) | ( 4, 16) (4,16) | ( 4, 17) (4,17) | ( 4, 18) (4,18) | ( 4, 19) (4,19) | ( 4, 20) (4,20) |

709 709 – 743 743 | 751 751 – 787 787 | 797 797 – 829 829 | 839 839 – 863 863 | 877 877 – 911 911 | 919 919 – 953 953 |

( 4, 21) (4,21) | ( 4, 22) (4,22) | ( 4, 23) (4,23) | ( 4, 24) (4,24) | ( 4, 25) (4,25) | ( 4, 26) (4,26) |

967 967 – 991 991 | 997 997 – 1033 1033 | 1039 1039 – 1069 1069 | 1087 1087 – 1117 1117 | 1123 1123 – 1163 1163 | 1171 1171 – 1201 1201 |

( 4, 27) (4,27) | ( 4, 28) (4,28) | ( 4, 29) (4,29) | ( 4, 30) (4,30) | ( 4, 31) (4,31) | ( 4, 32) (4,32) |

1213 1213 – 1249 1249 | 1259 1259 – 1291 1291 | 1297 1297 – 1327 1327 | 1361 1361 – 1373 1373 | 1381 1381 – 1423 1423 | 1427 1427 – 1459 1459 |

( 4, 33) (4,33) | ( 4, 34) (4,34) | ( 4, 35) (4,35) | ( 4, 36) (4,36) | ( 4, 37) (4,37) | ( 4, 38) (4,38) |

1471 1471 – 1511 1511 | 1523 1523 – 1553 1553 | 1559 1559 – 1597 1597 | 1601 1601 – 1637 1637 | 1657 1657 – 1669 1669 | 1693 1693 – 1723 1723 |

( 4, 39) (4,39) | ( 4, 40) (4,40) | ( 4, 41) (4,41) | ( 4, 42) (4,42) | ( 4, 43) (4,43) | ( 4, 44) (4,44) |

1733 1733 – 1777 1777 | 1783 1783 – 1811 1811 | 1823 1823 – 1867 1867 | 1871 1871 – 1907 1907 | 1913 1913 – 1951 1951 | 1973 1973 – 1987 1987 |

( 4, 45) (4,45) | ( 4, 46) (4,46) | ( 4, 47) (4,47) | ( 4, 48) (4,48) | ( 4, 49) (4,49) | ( 4, 50) (4,50) |

1993 1993 – 2003 2003 | 2011 2011 – 2039 2039 | 2053 2053 – 2089 2089 | 2099 2099 – 2141 2141 | 2143 2143 – 2179 2179 | 2203 2203 – 2221 2221 |

( 5, 49) (5,49) | ( 5, 50) (5,50) | ( 5, 51) (5,51) | ( 5, 52) (5,52) | ( 5, 53) (5,53) | ( 5, 54) (5,54) |

Table 1: The optimal pair ( ξ, η) (\xi,\eta) at which G ⁡ ( s) G(s) reaches its minimum at s = 2 ​ ξ + 1 2 ​ p − η p 2 s=\frac{2\xi+1}{2p}-\frac{\eta}{p^{2}} for odd primes p = 3, …, 2221 p=3,\dots,2221.

We list the partitions used in our numerical check for p = 127 p=127, p = 491 p=491 and p = 1993 p=1993 for which ξ \xi jumps from i i to i + 1 i+1, and the minimum of G G is attained with the choices ( ξ, η) = ( 3, 5) (\xi,\eta)=(3,5), ( 4, 15) (4,15) and ( 5, 49) (5,49), respectively. For simplicity, we use the notation [a, b] = [x 0, x 1, …, x d] [a,b]=[x_{0},x_{1},\dots,x_{d}] to mean the union ∪ i = 1 d [x i − 1, x i] \cup_{i=1}^{d}[x_{i-1},x_{i}] with x 0 = a x_{0}=a and x d = b x_{d}=b.

p = 127 p=127: ( ξ, η) = ( 3, 5) (\xi,\eta)=(3,5) |

variable | Interval | first partition | split each into N N subintervals (equal spacing) |

t t | [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}] | [0, 1 2 − 4 p, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{4}{p},\frac{1}{2}-\frac{1}{2p}] | N = 500 N=500 |

[1 2 + 1 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},1] | [1 2 + 1 2 ​ p, 1 2 + 9 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},\frac{1}{2}+\frac{9}{2p},1] | N = 500 N=500 |

s s | [1 p, 7 2 ​ p − 11 2 ​ p 2] [\frac{1}{p},\frac{7}{2p}-\frac{11}{2p^{2}}] | [1 p, 2.3 p, 3.4 p, 7 2 ​ p − 11 2 ​ p 2] [\frac{1}{p},\frac{2.3}{p},\frac{3.4}{p},\frac{7}{2p}-\frac{11}{2p^{2}}] | N = 1000 N=1000 |

[7 2 ​ p − 9 2 ​ p 2, 1] [\frac{7}{2p}-\frac{9}{2p^{2}},1] | [7 2 ​ p − 9 2 ​ p 2, 3.51 p, 6 p, 1] [\frac{7}{2p}-\frac{9}{2p^{2}},\frac{3.51}{p},\frac{6}{p},1] | N = 1200 N=1200 |

p = 491 p=491: ( ξ, η) = ( 4, 15) (\xi,\eta)=(4,15) |

variable | Interval | first partition | split each into N N subintervals (equal spacing) |

t t | [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}] | [0, 0.46, 1 2 − 5 2 ​ p, 1 2 − 1 2 ​ p] [0,0.46,\frac{1}{2}-\frac{5}{2p},\frac{1}{2}-\frac{1}{2p}] | N = 1000 N=1000 |

[1 2 + 1 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},1] | [1 2 + 1 2 ​ p, 1 2 + 2.1 p, 0.53, 1] [\frac{1}{2}+\frac{1}{2p},\frac{1}{2}+\frac{2.1}{p},0.53,1] | N = 1000 N=1000 |

s s | [1 p, 4.5 p − 15.5 p 2] [\frac{1}{p},\frac{4.5}{p}-\frac{15.5}{p^{2}}] | [1 p, 3.4 p, 3.5 p, 4.45 p, 4.5 p − 15.5 p 2] [\frac{1}{p},\frac{3.4}{p},\frac{3.5}{p},\frac{4.45}{p},\frac{4.5}{p}-\frac{15.5}{p^{2}}] | N = 5000 N=5000 |

[4.5 p − 14.5 p 2, 1] [\frac{4.5}{p}-\frac{14.5}{p^{2}},1] | [4.5 p − 14.5 p 2, 4.5 p − 6 p 2, 5 p, 8 p, 1] [\frac{4.5}{p}-\frac{14.5}{p^{2}},\frac{4.5}{p}-\frac{6}{p^{2}},\frac{5}{p},\frac{8}{p},1] | N = 5000 N=5000 |

p = 1993 p=1993: ( ξ, η) = ( 5, 49) (\xi,\eta)=(5,49) |

variable | Interval | first partition | split each into N N subintervals (equal spacing) |

t t | [0, 1 2 − 1 2 ​ p] [0,\frac{1}{2}-\frac{1}{2p}] | [0, 0.485, 0.498, 0.4994, 1 2 − 1 2 ​ p] [0,0.485,0.498,0.4994,\frac{1}{2}-\frac{1}{2p}] | N = 4000 N=4000 |

[1 2 + 1 2 ​ p, 1] [\frac{1}{2}+\frac{1}{2p},1] | [1 2 + 1 2 ​ p, 0.501, 0.504, 0.515, 1] [\frac{1}{2}+\frac{1}{2p},0.501,0.504,0.515,1] | N = 3000 N=3000 |

s s | [1 p, 5.5 p − 49.5 p 2] [\frac{1}{p},\frac{5.5}{p}-\frac{49.5}{p^{2}}] | [1 p, 4.45 p, 4.5 p, 5.46 p, 5.474 p, 5.5 p − 49.5 p 2] [\frac{1}{p},\frac{4.45}{p},\frac{4.5}{p},\frac{5.46}{p},\frac{5.474}{p},\frac{5.5}{p}-\frac{49.5}{p^{2}}] | N = 12000 N=12000 |

[5.5 p − 48.5 p 2, 1] [\frac{5.5}{p}-\frac{48.5}{p^{2}},1] | [5.5 p − 48.5 p 2, 5.5 p − 41 p 2, 5.6 p, 15 p, 1] [\frac{5.5}{p}-\frac{48.5}{p^{2}},\frac{5.5}{p}-\frac{41}{p^{2}},\frac{5.6}{p},\frac{15}{p},1] | N = 10000 N=10000 |

### 6.2 Large p p asymptotics

Assuming that G G reaches its minimum at s = s ^ p ​ ( ξ, η) s=\hat{s}_{p}(\xi,\eta) for some ( ξ, η) (\xi,\eta), so that the minimum value β p \beta_{p} is given by ( 1.13), we give here some simple, not completely rigorous, estimates of the two parameters ( ξ, η) (\xi,\eta) and the minimum point s ^ p \hat{s}_{p} for a given large p p. We note first that

 | ϱ p = log ⁡ ( 1 2 ​ p ​ ( p + 1)) log ⁡ p = 2 + log ⁡ ( 1 + 1 p) − log ⁡ 2 log ⁡ p = 2 − 1 log 2 ⁡ p + O ⁡ ( 1 p ​ log ⁡ p). \displaystyle{\varrho_{p}}=\frac{\log(\frac{1}{2}p(p+1))}{\log p}=2+\frac{\log(1+\frac{1}{p})-\log 2}{\log p}=2-\frac{1}{\log_{2}p}+O\Bigl(\frac{1}{p\log p}\Bigr). |  | (6.1) |

We see from Table 1 in Section 6.1 that ξ \xi and η \eta both seem to grow as p p grows (although not monotonically in case of η \eta). In fact, it is easy to see that at least ξ + η \xi+\eta must tend to infinity, because otherwise there would be an infinite subsequence with some fixed values of ξ \xi and η \eta, but then it would follow from ( 1.13) that as p → ∞ p\to\infty along this subsequence, using ρ p → 2 \rho_{p}\to 2 from ( 6.1),

 | β p = B ξ, η → ξ + 1 2 ​ ξ + 1 > 1 2, \displaystyle\beta_{p}=B_{\xi,\eta}\to\frac{\xi+1}{2\xi+1}>\frac{1}{2}, |  | (6.2) |

which contradicts ( 1.9).

We obtain more precise estimates by regarding ξ \xi and η \eta as continuous variables in ( 1.13) and setting the partial derivatives of ( 1.13) with respect to ξ \xi and η \eta equal to 0. This yields the equations:

 | { ( 4 ​ ξ + 3) ​ p 2 + ( 4 ​ ξ − 4 ​ η + 3) ​ p + 2 ​ η ​ ( 2 ​ η − 1) ( ξ + 1) ​ ( 2 ​ ξ + 1) ​ p 2 + ( ξ + 1) ​ ( 2 ​ ξ − 4 ​ η + 1) ​ p + 2 ​ η ​ ( ξ + 1) ​ ( 2 ​ η − 1) − 2 ​ ϱ p ​ p ( 2 ​ ξ + 1) ​ p − 2 ​ η = 0, ϱ p ( 2 ​ ξ + 1) ​ p − 2 ​ η − 2 ​ p − 4 ​ η + 1 ( 2 ​ ξ + 1) ​ p 2 + ( 2 ​ ξ − 4 ​ η + 1) ​ p + 2 ​ η ​ ( 2 ​ η − 1) = 0. \displaystyle\begin{cases}\displaystyle\frac{(4\xi+3)p^{2}+(4\xi-4\eta+3)p+2\eta(2\eta-1)}{(\xi+1)(2\xi+1)p^{2}+(\xi+1)(2\xi-4\eta+1)p+2\eta(\xi+1)(2\eta-1)}-\frac{2{\varrho_{p}}p}{(2\xi+1)p-2\eta}=0,\\ \displaystyle\frac{{\varrho_{p}}}{(2\xi+1)p-2\eta}-\frac{2p-4\eta+1}{(2\xi+1)p^{2}+(2\xi-4\eta+1)p+2\eta(2\eta-1)}=0.\end{cases} |  | (6.3) |

The positive solution pair, say ( ξ +, η +) (\xi_{+},\eta_{+}), already gives a very good approximation to the true values of ( ξ, η) (\xi,\eta). Empirically, ( ⌊ ξ + + 0.5 ⌋, ⌊ η + + 0.45 ⌋) (\lfloor\xi_{+}+0.5\rfloor,\lfloor\eta_{+}+0.45\rfloor) is identical to the true pair ( ξ, η) (\xi,\eta) at which G G attains the minimum for primes p p from 11 11 to 79 79, and differs by at most 1 1 (at either ξ \xi or η \eta but not both) for primes up to 7907 7907. For p p as large as p = 1,000,003 p=1,000,003, such a solution pair gives ( 9, 13206) (9,13206), while the true minimum of G G is reached at ( ξ, η) = ( 9, 13203) (\xi,\eta)=(9,13203).

For large p p, we may approximate the equations ( 6.3) by ignoring all terms that are O ⁡ ( 1 p) O(\frac{1}{p}) or O ⁡ ( η p ​ ξ) O(\frac{\eta}{p\xi}) times the leading terms in the various numerators and denominators. (We assume that η p ​ ξ \frac{\eta}{p\xi} is small.) This gives the equations, using the notation Δ:= 1 p + η p ​ ξ \Delta:=\frac{1}{p}+\frac{\eta}{p\xi},

 |

 | 4 ​ ξ + 3 ( ξ + 1) ​ ( 2 ​ ξ + 1) \displaystyle\frac{4\xi+3}{(\xi+1)(2\xi+1)} | = 2 ​ ϱ p 2 ​ ξ + 1 ​ ( 1 + O ​ ( Δ)), \displaystyle=\frac{2{\varrho_{p}}}{2\xi+1}\bigl(1+O(\Delta)\bigr), |  | (6.4a) |

 | ϱ p 2 ​ ξ + 1 \displaystyle\frac{{\varrho_{p}}}{2\xi+1} | = 2 − 4 p ​ η 2 ​ ξ + 1 ​ ( 1 + O ​ ( Δ)). \displaystyle=\frac{2-\frac{4}{p}\eta}{2\xi+1}\bigl(1+O(\Delta)\bigr). |  | (6.4b) |

If we further define δ p:= 2 − ϱ p ∼ 1 log 2 ⁡ p \delta_{p}:=2-{\varrho_{p}}\sim\frac{1}{\log_{2}p} (see ( 6.1)), then ( 6.4a) yields

 | ( 4 − 2 ​ δ p) ​ ( ξ + 1) = 2 ​ ϱ p ​ ( ξ + 1) = ( 4 ​ ξ + 3) ​ ( 1 + O ⁡ ( Δ)) = 4 ​ ξ + 3 + O ⁡ ( ξ ​ Δ). \displaystyle(4-2\delta_{p})(\xi+1)=2{\varrho_{p}}(\xi+1)=(4\xi+3)\bigl(1+O(\Delta)\bigr)=4\xi+3+O(\xi\Delta). |  | (6.5) |

Assuming ξ, η = o ⁡ ( p) \xi,\eta=o(p), we have ξ ​ Δ = ξ + η p = o ⁡ ( 1) \xi\Delta=\frac{\xi+\eta}{p}=o(1) and then ( 6.5) yields 2 ​ δ p ​ ξ = 1 + o ⁡ ( 1) 2\delta_{p}\xi=1+o(1) and finally, using ( 6.1),

 | ξ ∼ 1 2 ​ δ p ∼ log 2 ⁡ p 2 = log 4 ⁡ p. \displaystyle\xi\sim\frac{1}{2\delta_{p}}\sim\frac{\log_{2}p}{2}=\log_{4}p. |  | (6.6) |

Similarly, ( 6.4b) yields

 | 2 − 4 ​ η p = ρ p + O ⁡ ( Δ) = 2 − δ p + O ⁡ ( Δ) \displaystyle 2-\frac{4\eta}{p}=\rho_{p}+O(\Delta)=2-\delta_{p}+O(\Delta) |  | (6.7) |

leading to the empirical approximation for η \eta:

 | η ∼ 1 4 ​ p ​ δ p ∼ p 4 ​ log 2 ​ p. \displaystyle\eta\sim\frac{1}{4}p\delta_{p}\sim\frac{p}{4\log_{2}p}. |  | (6.8) |

The values ( 6.6) and ( 6.8) yield by ( 1.11) the estimate for the minimum point

 | s ^ p ∼ ξ p ∼ log 4 ⁡ p p. \displaystyle\hat{s}_{p}\sim\frac{\xi}{p}\sim\frac{\log_{4}p}{p}. |  | (6.9) |

Finally, observe that if

 | x = ∑ j ≥ 1 b j p − j = ( 0. b 1 b 2 …) p, \displaystyle x=\sum_{j\geq 1}b_{j}p^{-j}=(0.b_{1}b_{2}\dots)_{p}, |  | (6.10) |

then b 1 = ⌊ p ​ x ⌋ b_{1}=\lfloor{px\rfloor}, and

 | b m = ⌊ p m ​ x ⌋ − p ⁡ ⌊ p m − 1 ​ x ⌋ = p ⁡ { p m − 1 ​ x } − { p m ​ x } ( m ≥ 2). \displaystyle b_{m}=\lfloor p^{m}x\rfloor-p\lfloor p^{m-1}x\rfloor=p\{p^{m-1}x\}-\{p^{m}x\}\qquad(m\geq 2). |  | (6.11) |

Thus

 | φ ⁡ ( x) \displaystyle\varphi(x) | = 1 2 ​ ∑ j ≥ 1 ⌊ p j ​ x ⌋ − p ⁡ ⌊ p j − 1 ​ x ⌋ A j ​ ∏ 1 ≤ i ≤ j ( 1 + ⌊ p i ​ x ⌋ − p ⁡ ⌊ p i − 1 ​ x ⌋) \displaystyle=\frac{1}{2}\sum_{j\geq 1}\frac{\lfloor p^{j}x\rfloor-p\lfloor p^{j-1}x\rfloor}{A^{j}}\prod_{1\leq i\leq j}\left(1+\lfloor p^{i}x\rfloor-p\lfloor p^{i-1}x\rfloor\right) |  |

 |  | = 1 + ⌊ p ​ x ⌋ 2 ​ ( ⌊ p ​ x ⌋ A + ∑ j ≥ 2 p ⁡ { p j − 1 ​ x } − { p j ​ x } A j ​ ∏ 2 ≤ i ≤ j ( 1 + p ⁡ { p i − 1 ​ x } − { p i ​ x })) \displaystyle=\frac{1+\lfloor{px\rfloor}}{2}\left(\frac{\lfloor px\rfloor}{A}+\sum_{j\geq 2}\frac{p\{p^{j-1}x\}-\{p^{j}x\}}{A^{j}}\prod_{2\leq i\leq j}\left(1+p\{p^{i-1}x\}-\{p^{i}x\}\right)\right) |  | (6.12) |

For large p p, each term in the sum on the right-hand side is asymptotic to

 | 2 j − 1 p j − 1 x { p x } ⋯ { p j − 2 x } { p j − 1 x } 2 ( 1 + O ( p − 1)), \displaystyle\frac{2^{j-1}}{p^{j-1}}\,x\{px\}\cdots\{p^{j-2}x\}\{p^{j-1}x\}^{2}\left(1+O\left(p^{-1}\right)\right), |  | (6.13) |

for j ≥ 2 j\geq 2, and for j = 1 j=1:

 | ⌊ p ​ x ⌋ ​ ( ⌊ p ​ x ⌋ + 1) p ⁡ ( p + 1) = x 2 + x ⁡ ( 1 − x − 2 ​ { p ​ x }) p + O ⁡ ( p − 2). \displaystyle\frac{\lfloor px\rfloor(\lfloor px\rfloor+1)}{p(p+1)}=x^{2}+\frac{x(1-x-2\{px\})}{p}+O\left(p^{-2}\right). |  | (6.14) |

We then obtain

 | φ ⁡ ( x) = x 2 \displaystyle\varphi(x)=x^{2} | + x ⁡ ( 1 − x − 2 ​ { p ​ x } + 2 ​ { p ​ x } 2) p + O ⁡ ( p − 2). \displaystyle+\frac{x(1-x-2\{px\}+2\{px\}^{2})}{p}+O\bigl(p^{-2}\bigr). |  | (6.15) |

Then

 | G ⁡ ( x) = x 2 − ϱ p + x 1 − ϱ p ​ ( 1 − x − 2 ​ { p ​ x } + 2 ​ { p ​ x } 2) p + ⋯, \displaystyle G(x)=x^{2-{\varrho_{p}}}+\frac{x^{1-{\varrho_{p}}}(1-x-2\{px\}+2\{px\}^{2})}{p}+\cdots, |  | (6.16) |

where the piecewise differentiability of the terms on the right-hand side might be useful in further identifying the true minimum of G G for large p p.

## Appendix A The p-ary recurrence

In this appendix we study a more general recurrence, using the methods of [7] and [8] where binary recurrences are studied; see also Section 7.1 in the [earlier version of [8]][3] on arXiv.

Let p p be any integer larger than 1 1. Consider the recurrence

 | f ⁡ ( n) = ∑ 0 ≤ j < p γ j ​ f ​ ( ⌊ n + j p ⌋) for n ≥ p, f(n)=\sum_{0\leq j<p}\gamma_{j}f\left(\left\lfloor\frac{n+j}{p}\right\rfloor\right)\qquad\textrm{for $n\geq p$}, |  | (A.1) |

with given coefficients γ 0, …, γ p − 1 \gamma_{0},\ldots,\gamma_{p-1} and given initial values f ⁡ ( 1), …, f ⁡ ( p − 1) f(1),\ldots,f(p-1). We assume for simplicity that γ 0, …, γ p − 1 > 0 \gamma_{0},\ldots,\gamma_{p-1}>0. Let

 | A:= ∑ 0 ≤ j < p γ j. A:=\sum_{0\leq j<p}\gamma_{j}. |  | (A.2) |

###### Lemma A.1.

Let γ 0, …, γ p − 1 > 0 \gamma_{0},\ldots,\gamma_{p-1}>0. Then there exists a unique strictly increasing continuous function φ \varphi on [0, 1] [0,1] such that φ ⁡ ( 0) = 0, φ ⁡ ( 1) = 1 \varphi(0)=0,\varphi(1)=1 and for j = 0, 1, …, p − 1 j=0,1,\ldots,p-1,

 | φ ⁡ ( t) = γ p − j − 1 A ​ φ ​ ( p ​ t − j) + ∑ p − j ≤ i < p γ i A if j p ≤ t ≤ j + 1 p. \varphi(t)=\frac{\gamma_{p-j-1}}{A}\varphi(pt-j)+\frac{\sum_{p-j\leq i<p}\gamma_{i}}{A}\qquad\mathrm{if}\quad\frac{j}{p}\leq t\leq\,\frac{j+1}{p}. |  | (A.3) |

Moreover, we have the explicit formula

 | φ ⁡ ( ∑ j ≥ 1 b j ​ p − j) = ∑ j ≥ 1 A − j ​ ( ∑ p − b j ≤ i < p γ i) ​ ( ∏ 1 ≤ i < j γ p − 1 − b i), \varphi\left(\sum_{j\geq 1}b_{j}p^{-j}\right)=\sum_{j\geq 1}A^{-j}\left(\sum_{p-b_{j}\leq i<p}\gamma_{i}\right)\left(\prod_{1\leq i<j}\gamma_{p-1-b_{i}}\right), |  | (A.4) |

when b j ∈ { 0, 1, 2, …, p − 1 } b_{j}\in\{0,1,2,\ldots,p-1\} for j ≥ 1 j\geq 1.

###### Proof.

Define φ 0 ​ ( t):= t \varphi_{0}(t):=t for t ∈ [0, 1] t\in[0,1], and recursively let

 | φ k + 1 ​ ( t):= γ p − j − 1 A ​ φ k ​ ( p ​ t − j) + ∑ p − j ≤ i < p γ i A if j p ≤ t ≤ j + 1 p, \varphi_{k+1}(t):=\frac{\gamma_{p-j-1}}{A}\varphi_{k}(pt-j)+\frac{\sum_{p-j\leq i<p}\gamma_{i}}{A}\qquad\mathrm{if}\quad\frac{j}{p}\leq t\leq\,\frac{j+1}{p}, |  | (A.5) |

for j = 0, 1, …, p − 1 j=0,1,\ldots,p-1. (Thus φ k + 1 \varphi_{k+1} consists of p p suitably scaled copies of φ k \varphi_{k}.) Observe first that φ k ​ ( 0) = 0 \varphi_{k}(0)=0 and φ k ​ ( 1) = 1 \varphi_{k}(1)=1 by induction. Note also that if t 0 = j 0 p t_{0}=\frac{j_{0}}{p} for j 0 ∈ { 1, …, p − 1 } j_{0}\in\{1,\ldots,p-1\}, then the definition ( A.5) can be applied with both j = j 0 − 1 j=j_{0}-1 and j = j 0 j=j_{0}. The first choice gives

 | φ k + 1 ​ ( t 0) = γ p − j 0 A ​ φ k ​ ( 1) + ∑ p − j 0 + 1 ≤ i < p γ i A = ∑ p − j 0 ≤ i < p γ i A, \varphi_{k+1}\left(t_{0}\right)=\frac{\gamma_{p-j_{0}}}{A}\varphi_{k}(1)+\frac{\sum_{p-j_{0}+1\leq i<p}\gamma_{i}}{A}=\frac{\sum_{p-j_{0}\leq i<p}\gamma_{i}}{A}, |  | (A.6) |

and the second one gives

 | φ k + 1 ​ ( t 0) = γ p − j 0 − 1 A ​ φ k ​ ( 0) + ∑ p − j 0 ≤ i < p γ i A = ∑ p − j 0 ≤ i < p γ i A. \varphi_{k+1}\left(t_{0}\right)=\frac{\gamma_{p-j_{0}-1}}{A}\varphi_{k}(0)+\frac{\sum_{p-j_{0}\leq i<p}\gamma_{i}}{A}=\frac{\sum_{p-j_{0}\leq i<p}\gamma_{i}}{A}. |  | (A.7) |

Since these are equal, the definition ( A.5) is consistent. It is now obvious by induction that φ k \varphi_{k} is continuous and strictly increasing.

We claim that

 | | φ k + 1 ​ ( t) − φ k ​ ( t) | ≤ ( max 0 ≤ j < p ⁡ γ j A) k for all k ≥ 0 and ​ t ∈ [0, 1]. \left|\varphi_{k+1}(t)-\varphi_{k}(t)\right|\leq\left(\frac{\max_{0\leq j<p}\gamma_{j}}{A}\right)^{k}\qquad\textrm{for all $k\geq 0$ and }t\in[0,1]. |  | (A.8) |

We prove this by induction. The case k = 0 k=0 is clear, since | φ 1 ​ ( t) − φ 0 ​ ( t) | ≤ 1 \left|\varphi_{1}(t)-\varphi_{0}(t)\right|\leq 1. Assume now that ( A.8) holds for k − 1 k-1. If j p ≤ t ≤ j + 1 p \frac{j}{p}\leq t\leq\,\frac{j+1}{p} then

 | | φ k + 1 ​ ( t) − φ k ​ ( t) | \displaystyle\left|\varphi_{k+1}(t)-\varphi_{k}(t)\right| | = γ p − j − 1 A ​ | φ k ​ ( p ​ t − j) − φ k − 1 ​ ( p ​ t − j) | \displaystyle=\frac{\gamma_{p-j-1}}{A}\left|\varphi_{k}(pt-j)-\varphi_{k-1}(pt-j)\right| |  | (A.9) |

 |  | ≤ γ p − j − 1 A ​ ( max 0 ≤ j < p ⁡ γ j A) k − 1 \displaystyle\leq\frac{\gamma_{p-j-1}}{A}\left(\frac{\max_{0\leq j<p}\gamma_{j}}{A}\right)^{k-1} |  |

 |  | ≤ ( max 0 ≤ j < p ⁡ γ j A) k. \displaystyle\leq\left(\frac{\max_{0\leq j<p}\gamma_{j}}{A}\right)^{k}. |  |

Thus, ( A.8) holds, and since max 0 ≤ j < p ⁡ γ j / A < 1 \max_{0\leq j<p}\gamma_{j}/A<1, it follows that the sequence φ k \varphi_{k} converges uniformly to a function φ: [0, 1] → [0, 1] \varphi:[0,1]\to[0,1]. By ( A.5), φ \varphi satisfies ( A.3). Since each φ k \varphi_{k} is continuous and strictly increasing, the limiting function φ \varphi is continuous and non-decreasing.

We next prove by induction that

 | φ N ​ ( ∑ 1 ≤ j ≤ N b j ​ p − j) = ∑ 1 ≤ j ≤ N A − j ​ ( ∑ p − b j ≤ i < p γ i) ​ ( ∏ 1 ≤ i < j γ p − 1 − b i), \varphi_{N}\left(\sum_{1\leq j\leq N}b_{j}p^{-j}\right)=\sum_{1\leq j\leq N}A^{-j}\left(\sum_{p-b_{j}\leq i<p}\gamma_{i}\right)\left(\prod_{1\leq i<j}\gamma_{p-1-b_{i}}\right), |  | (A.10) |

for any N ≥ 0 N\geq 0, where b j ∈ { 0, 1, 2, …, p − 1 } b_{j}\in\{0,1,2,\ldots,p-1\}. This is trivial for N = 0 N=0. Suppose that ( A.10) holds for N N. Let t = ∑ 1 ≤ j ≤ N + 1 b j ​ p − j t=\sum_{1\leq j\leq N+1}b_{j}p^{-j}, where b j ∈ { 0, 1, 2, …, p − 1 } b_{j}\in\{0,1,2,\ldots,p-1\}. Then, by ( A.5),

 | φ N + 1 ​ ( t) \displaystyle\varphi_{N+1}(t) | = γ p − b 1 − 1 A ​ φ N ​ ( p ​ t − b 1) + ∑ p − b 1 ≤ i < p γ i A \displaystyle=\frac{\gamma_{p-b_{1}-1}}{A}\varphi_{N}\left(pt-b_{1}\right)+\frac{\sum_{p-b_{1}\leq i<p}\gamma_{i}}{A} |  |

 |  | = γ p − b 1 − 1 A ​ ( ∑ 1 ≤ j ≤ N A − j ​ ( ∑ p − b j + 1 ≤ i < p γ i) ​ ( ∏ 1 ≤ i < j γ p − 1 − b i + 1)) + ∑ p − b 1 ≤ i < p γ i A \displaystyle=\frac{\gamma_{p-b_{1}-1}}{A}\left(\sum_{1\leq j\leq N}A^{-j}\left(\sum_{p-b_{j+1}\leq i<p}\gamma_{i}\right)\left(\prod_{1\leq i<j}\gamma_{p-1-b_{i+1}}\right)\right)+\frac{\sum_{p-b_{1}\leq i<p}\gamma_{i}}{A} |  |

 |  | = ∑ 2 ≤ j ≤ N + 1 A − j ​ ( ∑ p − b j ≤ i < p γ i) ​ ( ∏ 1 ≤ i < j γ p − 1 − b i) + ∑ p − b 1 ≤ i < p γ i A \displaystyle=\sum_{2\leq j\leq N+1}A^{-j}\left(\sum_{p-b_{j}\leq i<p}\gamma_{i}\right)\left(\prod_{1\leq i<j}\gamma_{p-1-b_{i}}\right)+\frac{\sum_{p-b_{1}\leq i<p}\gamma_{i}}{A} |  |

 |  | = ∑ 1 ≤ j ≤ N + 1 A − j ​ ( ∑ p − b j ≤ i < p γ i) ​ ( ∏ 1 ≤ i < j γ p − 1 − b i). \displaystyle=\sum_{1\leq j\leq N+1}A^{-j}\left(\sum_{p-b_{j}\leq i<p}\gamma_{i}\right)\left(\prod_{1\leq i<j}\gamma_{p-1-b_{i}}\right). |  | (A.11) |

Hence ( A.10) holds for N + 1 N+1, and thus it holds in general by induction.

For any p p -adic rational t = ∑ 1 ≤ j ≤ M b j ​ p − j t=\sum_{1\leq j\leq M}b_{j}p^{-j}, let b j:= 0 b_{j}:=0 for j > M j>M and apply ( A.10) with N ≥ M N\geq M. Letting N → ∞ N\to\infty, we see that ( A.4) holds for t t. Since we have shown that φ \varphi is continuous, it follows that ( A.4) holds in general, for any ∑ 1 ≤ j < ∞ b j ​ p − j \sum_{1\leq j<\infty}b_{j}p^{-j}. Furthermore, it follows from ( A.10) that for every N ≥ M N\geq M, we have

 | φ N ​ ( t) = φ M ​ ( t). \varphi_{N}(t)=\varphi_{M}(t). |  | (A.12) |

Thus φ ⁡ ( t) = lim N → ∞ φ N ​ ( t) = φ M ​ ( t) \varphi(t)=\lim_{N\rightarrow\infty}\varphi_{N}(t)=\varphi_{M}(t). Accordingly,

 | φ ⁡ ( t) = φ N ​ ( t) < φ N ​ ( t + p − N) = φ ⁡ ( t + p − N). \varphi(t)=\varphi_{N}(t)<\varphi_{N}(t+p^{-N})=\varphi(t+p^{-N}). |  | (A.13) |

This shows that φ \varphi is strictly increasing on p p -adic rationals. In general, for 0 ≤ s 1 < s 2 ≤ 1 0\leq s_{1}<s_{2}\leq 1, there exist p p -adic rationals t 1 t_{1} and t 2 t_{2} such that s 1 ≤ t 1 < t 2 ≤ s 2 s_{1}\leq t_{1}<t_{2}\leq s_{2}. Then

 | φ ⁡ ( s 1) ≤ φ ⁡ ( t 1) < φ ⁡ ( t 2) ≤ φ ⁡ ( s 2). \varphi(s_{1})\leq\varphi(t_{1})<\varphi(t_{2})\leq\varphi(s_{2}). |  | (A.14) |

Consequently, φ \varphi is strictly increasing. ∎

We next extend f ⁡ ( n) f(n) to a function of a real variable x ≥ 1 x\geq 1 by

 | f ⁡ ( n + t):= ( 1 − φ ⁡ ( t)) ​ f ​ ( n) + φ ⁡ ( t) ​ f ​ ( n + 1) f(n+t):=(1-\varphi(t))f(n)+\varphi(t)f(n+1) |  | (A.15) |

for n ≥ 1 n\geq 1 and 0 ≤ t ≤ 1 0\leq t\leq 1.

###### Lemma A.2.

Assume that the recurrence ( A.1) holds. Then

 | f ⁡ ( x) = A ​ f ​ ( x p) for all real ​ x ≥ p. f(x)=Af\left(\frac{x}{p}\right)\qquad\textrm{for all real }x\geq p. |  | (A.16) |

###### Proof.

Define

 | A k −:= ∑ 0 ≤ i < k γ i and A k +:= ∑ k ≤ i < p γ i. A_{k}^{-}:=\sum_{0\leq i<k}\gamma_{i}\qquad\textrm{and}\qquad A_{k}^{+}:=\sum_{k\leq i<p}\gamma_{i}. |  | (A.17) |

Rewrite ( A.1) as

 | f ⁡ ( p ​ n + j) = A p − j − ​ f ​ ( n) + A p − j + ​ f ​ ( n + 1) f(pn+j)=A_{p-j}^{-}f(n)+A_{p-j}^{+}f(n+1) |  | (A.18) |

for n ≥ 1 n\geq 1 and j = 0, 1, …, p − 1 j=0,1,\ldots,p-1; note that for j = 0 j=0 ( A.18) is f ⁡ ( p ​ n) = A ​ f ​ ( n) f(pn)=Af(n), and it follows that ( A.18) holds for j = p j=p too. Also rewrite ( A.3) as

 | γ p − 1 − j ​ φ ​ ( p ​ t) = A ​ φ ​ ( j p + t) − A p − j + \gamma_{p-1-j}\varphi(pt)=A\varphi\left(\frac{j}{p}+t\right)-A_{p-j}^{+} |  | (A.19) |

for 0 ≤ t ≤ 1 p 0\leq t\leq\frac{1}{p} and j = 0, 1, …, p − 1 j=0,1,\ldots,p-1.

Now, for x ≥ p x\geq p, write

 | x = p ​ n + j + p ​ t, x=pn+j+pt, |  | (A.20) |

where

 | n = ⌊ x p ⌋, j = ⌊ x ⌋ ​ mod ​ p, t = { x } p. n=\left\lfloor\frac{x}{p}\right\rfloor,\quad j=\left\lfloor x\right\rfloor\ \mathrm{mod\ }p,\quad t=\frac{\{x\}}{p}. |  | (A.21) |

Then, by ( A.15), ( A.18) and ( A.19),

 | f ⁡ ( x) \displaystyle f(x) | = f ⁡ ( p ​ n + j + p ​ t) \displaystyle=f(pn+j+pt) |  |

 |  | = ( 1 − φ ⁡ ( p ​ t)) ​ f ​ ( p ​ n + j) + φ ⁡ ( p ​ t) ​ f ​ ( p ​ n + j + 1) \displaystyle=(1-\varphi(pt))f(pn+j)+\varphi(pt)f(pn+j+1) |  |

 |  | = ( 1 − φ ⁡ ( p ​ t)) ​ ( A p − j − ​ f ​ ( n) + A p − j + ​ f ​ ( n + 1)) \displaystyle=(1-\varphi(pt))\left(A_{p-j}^{-}f(n)+A_{p-j}^{+}f(n+1)\right) |  | (A.22) |

 |  | + φ ⁡ ( p ​ t) ​ ( A p − j − 1 − ​ f ​ ( n) + A p − j − 1 + ​ f ​ ( n + 1)) \displaystyle\qquad\quad+\varphi(pt)\left(A_{p-j-1}^{-}f(n)+A_{p-j-1}^{+}f(n+1)\right) |  |

 |  | = ( A p − j − ​ f ​ ( n) + A p − j + ​ f ​ ( n + 1)) − φ ⁡ ( p ​ t) ​ γ p − j − 1 ​ ( f ⁡ ( n) − f ⁡ ( n + 1)) \displaystyle=\left(A_{p-j}^{-}f(n)+A_{p-j}^{+}f(n+1)\right)-\varphi(pt)\gamma_{p-j-1}\left(f(n)-f(n+1)\right) |  |

 |  | = ( A p − j − ​ f ​ ( n) + A p − j + ​ f ​ ( n + 1)) − ( A ​ φ ​ ( j p + t) − A p − j +) ​ ( f ⁡ ( n) − f ⁡ ( n + 1)) \displaystyle=\left(A_{p-j}^{-}f(n)+A_{p-j}^{+}f(n+1)\right)-\left(A\varphi\left(\frac{j}{p}+t\right)-A_{p-j}^{+}\right)\left(f(n)-f(n+1)\right) |  |

 |  | = A ​ f ​ ( n) − A ​ φ ​ ( j p + t) ​ f ​ ( n) + A ​ φ ​ ( j p + t) ​ f ​ ( n + 1) \displaystyle=Af(n)-A\varphi\left(\frac{j}{p}+t\right)f(n)+A\varphi\left(\frac{j}{p}+t\right)f(n+1) |  |

 |  | = A ⁡ ( ( 1 − φ ⁡ ( j p + t)) ​ f ​ ( n) + φ ⁡ ( j p + t) ​ f ​ ( n + 1)) \displaystyle=A\left(\left(1-\varphi\left(\frac{j}{p}+t\right)\right)f(n)+\varphi\left(\frac{j}{p}+t\right)f(n+1)\right) |  |

 |  | = A ​ f ​ ( n + j p + t) \displaystyle=Af\left(n+\frac{j}{p}+t\right) |  |

 |  | = A ​ f ​ ( x p), \displaystyle=Af\left(\frac{x}{p}\right), |  | (A.23) |

which proves ( A.16). ∎

###### Theorem A.3.

Assume that the recurrence ( A.1) holds, with γ 0, …, γ p − 1 > 0 \gamma_{0},\dots,\gamma_{p-1}>0. Then

 | f ⁡ ( n) = n ϱ ​ 𝒫 ​ ( log p ⁡ n) for all ​ n ≥ 1, f(n)=n^{\varrho}\mathcal{P}\left(\log_{p}n\right)\qquad\textrm{for all }n\geq 1, |  | (A.24) |

where ϱ:= log p ⁡ A \varrho:=\log_{p}A and

 | 𝒫 ⁡ ( t):= A − { t } ​ f ​ ( p { t }) \mathcal{P}(t):=A^{-\{t\}}f(p^{\{t\}}) |  | (A.25) |

is a continuous 1 1 -periodic function.

Moreover, if the initial values satisfy

 | f ⁡ ( j) = ∑ p − j ≤ i < p γ i for ​ j = 1, …, p − 1 f(j)=\sum_{p-j\leq i<p}\gamma_{i}\qquad\textrm{for }j=1,\ldots,p-1 |  | (A.26) |

then

 | 𝒫 ⁡ ( t) = A 1 − { t } ​ φ ​ ( p { t } − 1), \mathcal{P}(t)=A^{1-\{t\}}\varphi(p^{\{t\}-1}), |  | (A.27) |

where φ \varphi is defined in Lemma A.1.

###### Proof.

Since f ⁡ ( x) f(x) is continuous, 𝒫 ⁡ ( t) \mathcal{P}(t) is continuous on [0, 1) [0,1), and by ( A.16)

 | lim t ↗ 1 𝒫 ⁡ ( t) = A − 1 ​ f ​ ( p) = f ⁡ ( 1) = 𝒫 ⁡ ( 0) = 𝒫 ⁡ ( 1), \lim_{t\nearrow 1}\mathcal{P}(t)=A^{-1}f(p)=f(1)=\mathcal{P}(0)=\mathcal{P}(1), |  | (A.28) |

which shows that 𝒫 ⁡ ( t) \mathcal{P}(t) is a continuous 1-periodic function. For y ∈ [1, p) y\in[1,p)

 | f ⁡ ( y) = f ⁡ ( p log p ⁡ y) = A log p ⁡ y ​ ( A − log p ⁡ y ​ f ​ ( p log p ⁡ y)) = A log p ⁡ y ​ 𝒫 ​ ( log p ⁡ y), f(y)=f(p^{\log_{p}y})=A^{\log_{p}y}\left(A^{-\log_{p}y}f(p^{\log_{p}y})\right)=A^{\log_{p}y}\mathcal{P}\left(\log_{p}y\right), |  | (A.29) |

and, for each x ≥ 1 x\geq 1,

 | p − ⌊ log p ⁡ x ⌋ ​ x ∈ [1, p). p^{-\lfloor\log_{p}x\rfloor}x\in[1,p). |  | (A.30) |

By applying Lemma A.2 repeatedly ⌊ log p ⁡ x ⌋ \lfloor\log_{p}x\rfloor times:

 | f ⁡ ( x) = A ⌊ log p ⁡ x ⌋ ​ f ​ ( p − ⌊ log p ⁡ x ⌋ ​ x) = A ⌊ log p ⁡ x ⌋ + log p ⁡ ( p − ⌊ log p ⁡ x ⌋ ​ x) ​ 𝒫 ​ ( log p ⁡ ( p − ⌊ log p ⁡ x ⌋ ​ x)) = A log p ⁡ x ​ 𝒫 ​ ( log p ⁡ x). \begin{split}f(x)&=A^{\lfloor\log_{p}x\rfloor}f\left(p^{-\lfloor\log_{p}x\rfloor}x\right)\\ &=A^{\lfloor\log_{p}x\rfloor+\log_{p}\left(p^{-\lfloor\log_{p}x\rfloor}x\right)}\mathcal{P}\left(\log_{p}\left(p^{-\lfloor\log_{p}x\rfloor}x\right)\right)\\ &=A^{\log_{p}x}\mathcal{P}\left(\log_{p}x\right).\end{split} |  | (A.31) |

Thus we get

 | f ⁡ ( n) = A log p ⁡ n ​ 𝒫 ​ ( log p ⁡ n) = p ϱ ​ log p ​ n ​ 𝒫 ​ ( log p ⁡ n) = n ϱ ​ 𝒫 ​ ( log p ⁡ n), f(n)=A^{\log_{p}n}\mathcal{P}\left(\log_{p}n\right)=p^{\varrho\log_{p}n}\mathcal{P}\left(\log_{p}n\right)=n^{\varrho}\mathcal{P}\left(\log_{p}n\right), |  | (A.32) |

proving ( A.24).

Finally, suppose that condition ( A.26) holds. For 1 ≤ x < p 1\leq x<p, let j = ⌊ x ⌋ j=\left\lfloor x\right\rfloor. Then, using ( A.15) and ( A.3),

 | f ⁡ ( x) \displaystyle f(x) | = f ⁡ ( j) + φ ⁡ ( x − j) ​ ( f ⁡ ( j + 1) − f ⁡ ( j)) \displaystyle=f(j)+\varphi(x-j)\left(f(j+1)-f(j)\right) |  | (A.33) |

 |  | = ∑ p − j ≤ i < p γ i + φ ⁡ ( x − j) ​ γ p − j − 1 \displaystyle=\sum_{p-j\leq i<p}\gamma_{i}+\varphi(x-j)\gamma_{p-j-1} |  |

 |  | = A ⁡ ( γ p − j − 1 A ​ φ ​ ( x − j) + ∑ p − j ≤ i < p γ i A) \displaystyle=A\left(\frac{\gamma_{p-j-1}}{A}\varphi(x-j)+\frac{\sum_{p-j\leq i<p}\gamma_{i}}{A}\right) |  |

 |  | = A ​ φ ​ ( x p). \displaystyle=A\varphi\left(\frac{x}{p}\right). |  |

Thus we have

 | 𝒫 ⁡ ( t) = A − { t } ​ f ​ ( p { t }) = A 1 − { t } ​ φ ​ ( p { t } − 1). ∎ \mathcal{P}(t)=A^{-\{t\}}f(p^{\{t\}})=A^{1-\{t\}}\varphi(p^{\{t\}-1}).\qed |  | (A.34) |

###### Corollary A.4.

Assume that the recurrence ( A.1) holds, with γ 0, …, γ p − 1 > 0 \gamma_{0},\dots,\gamma_{p-1}>0. Then

 | sup n ≥ 1 f ⁡ ( n) n ϱ \displaystyle\sup_{n\geq 1}\frac{f(n)}{n^{\varrho}} | = lim sup n → ∞ f ⁡ ( n) n ϱ = max t ∈ [0, 1] ⁡ 𝒫 ⁡ ( t), \displaystyle=\limsup_{n\rightarrow\infty}\frac{f(n)}{n^{\varrho}}=\max_{t\in[0,1]}\mathcal{P}(t), |  | (A.35) |

 | inf n ≥ 1 f ⁡ ( n) n ϱ \displaystyle\inf_{n\geq 1}\frac{f(n)}{n^{\varrho}} | = lim inf n → ∞ f ⁡ ( n) n ϱ = min t ∈ [0, 1] ⁡ 𝒫 ⁡ ( t). \displaystyle=\liminf_{n\rightarrow\infty}\frac{f(n)}{n^{\varrho}}=\min_{t\in[0,1]}\mathcal{P}(t). |  | (A.36) |

###### Proof.

By ( A.24), since 𝒫 ⁡ ( t) \mathcal{P}(t) is a continuous 1-periodic function. ∎

###### Remark A.5.

In the case that γ p − 1 = 1 \gamma_{p-1}=1, the condition ( A.26) on the initial values is equivalent to assuming that the recurrence ( A.1) extends to all n ≥ 2 n\geq 2, with f ⁡ ( 0) = 0 f(0)=0 and f ⁡ ( 1) = 1 f(1)=1. △ \triangle

## References

- [1] Chen, Y.-G. and Ji, C. (1998), The number of multinomial coefficients not divided by a prime. *Acta Sci. Math. (Szeged)*64(1-2), 37–48.
- [2] Chen, Y. G. and Ji, C. G. (2002), On a function related to multinomial coefficients. I. *Acta Math. Sin. (Engl. Ser.)*18(4), 647–660.
- [3] Fine, N. J. (1947), Binomial coefficients modulo a prime. *Amer. Math. Monthly*54, 589–592.
- [4] Franco, Z. M. (1998), Distribution of binomial coefficients modulo three. *Fibonacci Quart.*36(3), 272–275.
- [5] Harborth, H. (1977), Number of odd binomial coefficients. *Proc. Amer. Math. Soc.*62, 19–22.
- [6] Howard, F. T. (1974), The number of multinomial coefficients divisible by a fixed power of a prime, *Pacific J. Math.*50, 99–108.
- [7] Hwang, H.-K., Janson, S., and Tsai, T.-H. (2017), Exact and asymptotic solutions of a divide-and-conquer recurrence dividing at half: theory and applications. *ACM Trans. Algorithms*13(4), Art. 47, 43 pp.
- [8] Hwang, H.-K., Janson, S., and Tsai, T.-H. (2024), Identities and periodic oscillations of divide-and-conquer recurrences splitting at half. *Adv. in Appl. Math.*155, Paper No. 102653, 53 pp.
- [9] OEIS Foundation Inc., The On-Line Encyclopedia of Integer Sequences (OEIS). Available electronically at http://oeis.org.
- [10] Stein, A. H. (1989), Binomial coefficients not divisible by a prime. *Lecture Notes in Mathematics*1383, pp. 170–177, Springer-Verlag,
- [11] Stolarsky, K. B. (1977), Power and exponential sums of digital sums related to binomial coefficient parity, *SIAM J. Appl. Math.*32, 717–730.
- [12] Volodin, N. A. (1989), Distribution of polynomial coefficients congruent modulo p N p^{N}, *Math. Notes*45, 195–99.
- [13] Volodin, N. A. (1994), Number of multinomial coefficients not divisible by a prime, *Fibonacci Quart.*32, 402–406.
- [14] Volodin, N. A. (1999), Multinomial coefficients modulo a prime. *Proc. Amer. Math. Soc.*127(2), 349–353.
- [15] Wilson, B. (1996), LIM INF bounds for multinomial coefficients modulo a prime, Preprint, SUNY College at Brockport, New York, 16 pp.
- [16] Wilson, B. (1998), Asymptotic behavior of Pascal’s triangle modulo a prime. *Acta Arith.*83(2), 105–116.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://arxiv.org/abs/2210.10968
