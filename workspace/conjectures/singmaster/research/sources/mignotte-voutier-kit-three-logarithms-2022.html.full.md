<!-- source: https://arxiv.org/html/2205.08899v3 | converted from HTML -->

A kit for linear forms in three logarithms

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2205.08899v3 [math.NT] 29 Sep 2023

# A kit for linear forms in three logarithms

Maurice Mignotte Address: Maurice Mignotte
Université Louis Pasteur
U. F. R. de mathématiques
7, rue René Descartes
67084 Strasbourg Cedex
France Email address: [mignotte@math.unistra.fr][3] and Paul Voutier Address: Paul Voutier
London
UK Email address: [paul.voutier@gmail.com][4]

Date: August 11, 2026

###### Abstract.

We provide a technique to obtain explicit bounds for problems that can be reduced to linear forms in three complex logarithms of algebraic numbers. This technique can produce bounds significantly better than general results on lower bounds for linear forms in logarithms. We give worked examples to demonstrate both the use of our technique and the improvements it provides. Publicly shared code is also available.

###### Key words and phrases:

linear forms in logarithms, Diophantine equations

###### 2020 Mathematics Subject Classification

Primary 11D61, 11J86, Secondary 11Y50

## 1. Introduction

### 1.1. Background

Many problems in number theory can be reduced to linear forms in the logarithms of algebraic numbers which have a very small absolute value (exponentially small in the coefficients of the linear form) (see [8] for a broad selection of examples). So, lower bounds for these linear forms that exceed the upper bounds and with all the constants involved being explicit reduce such problems to a finite amount of computation. For example, it is in this way (along with the use of reduction techniques as in [30] and [7] to handle the remaining computation) that the solution of Thue equations is now routine, included as a function in PARI/GP [23] and other mathematical software.

Lower bounds for linear forms in two or three logarithms have proven to have especially broad and important applications. In the case of linear forms in three logarithms, such applications include Baker’s solution [2] of the conjecture of Gauss that there are only nine imaginary quadratic fields with class number 1 1; Tijdeman’s proof [29] that there are at most finitely many solutions of Catalan’s equation; and the result of Shorey & Stewart [28], and independently Pethő [24], that there are only finitely many perfect powers in any binary recurrence sequence. The use of effectively computable lower bounds for linear forms in three logarithms gives rise to effectively computable upper bounds for each of these problems.

In this paper, we present a method, our “kit”, that can be used to get good upper bounds on quantities associated to such problems. The present paper has its origins in earlier versions of our kit due to the first author in [9] and [10]. In fact, [9] and [10] provide good examples of how somewhat weaker versions of our kit were used to solve completely some important number theory problems.

Our method is the method of interpolation determinants introduced by Michel Laurent in [15], [16] and [17]. In the case of three logarithms, this method was used by C.D. Bennett et al. [4]. But the present paper brings some progress when compared to [4]: we treat the general case of algebraic numbers (not only multiplicatively independent rational integers, as in [4]) and many important technical details have been improved, including new zero lemmas.

Our aim, suggested by the title “ A kit… ”, is to explain how to obtain results for problems that reduce to the study of linear forms in three logarithms of algebraic numbers.

### 1.2. Steps of the kit

The process contains five steps.

(1) obtain an upper bound for a linear form in logs associated with our problem.

(2) combining the upper bound in step (1) with a general estimate of Matveev, we obtain an upper bound, B 1 B_{1}, for the maximum of the absolute values of the coefficients of the linear form.

(3) supposing the linear form in three logs is non-degenerate, we use the upper bound B 1 B_{1} to obtain a second upper bound, B 2 B_{2}. If B 2 B_{2} is smaller than B 1 B_{1} we proceed to step (4).

(4) supposing the linear form in three logs is degenerate, we consider it as a linear form in two logarithms and we apply the results of Laurent [19] to this linear form, along with the upper bound B 1 B_{1}, to get a third upper bound B 3 B_{3}.
At this point the quantity we have bounded above by min ⁡ { B 1, max ⁡ { B 2, B 3 } } \min\left\{B_{1},\max\left\{B_{2},B_{3}\right\}\right\}.

(5) repeat steps (3) and (4) as often as desired to make the upper bound as small as possible.

In our experience, there is very little further improvement after 3 iterations (see the tables at the end of each example subsection in Section 6 for details).

### 1.3. Uses for the kit

Our kit is most suited to the case when at least one of the algebraic numbers in the linear form is a variable. If all three are fixed algebraic numbers, it is much better to first use Matveev’s result stated below and then apply a reduction technique like the LLL-algorithm [21] or variants of the Baker-Davenport reduction technique [3], like that of Dujella-Pethő [12].

### 1.4. Numerical results

In the first example in Section 6, we are able to reduce the upper bound on the quantity p p from about 2 ⋅ 10 12 2\cdot 10^{12} obtained by Matveev’s result to 18 ⋅ 10 6 18\cdot 10^{6}. In the second example there, we do even better, reducing the upper bound on p p from about 3 ⋅ 10 13 3\cdot 10^{13} to 25 ⋅ 10 6 25\cdot 10^{6}. In our experience, these are typical of the improvements that can be expected from our kit.

To help readers use the kit, code written in Pari, along with examples for how to use it, is available from the authors at \url https://github.com/PV-314/lfl3-kit. We encourage readers to use this code for their applications of the kit, using the examples and documentation as a guide. This code has now been applied to previously published uses of the kit ( [5, 6, 9, 10] – the code for these is available in the above github repository) and several new problems shared with us by researchers. Support is available from the second author and we warmly welcome questions and suggestions from users.

Another feature of our work, and the above code, is the quality of the results. It is reasonable to believe that the degenerate case should play no part in Theorem 2.1 below and that only ( 2.8) should matter (see the proofs in Chapter 7 of [31], for example). In the case of “imaginary” linear forms in logs (see their definition at the start of Section 3 below) we are able to attain such optimal bounds with our code above, while for “real” linear forms in logs, our code produces bounds that are at most 50% larger than the optimal bounds.

### 1.5. Future work

We highlight here three areas where further work would lead to significant improvements in the results, as well as being of considerable theoretical interest for other diophantine and transcendence problems.

(1) Adopting Waldschmidt’s approach for the degenerate case. See Remark 3.14 for more information. This could reduce the bounds by a factor of approximately 1.5 1.5, but more importantly simplify the statement of Theorem 2.1, eliminating the need for conditions ( 2.9) and ( 2.10).

(2) Improving the multiplicity estimates in Lemma 3.6. Calculations suggest that the estimate there should be roughly Θ ⁡ ( 2 ​ K, | ℐ |) \Theta\left(2K,|\mathcal{I}|\right) instead of Θ ⁡ ( K, | ℐ |) \Theta\left(K,|\mathcal{I}|\right). The main term on the left-hand side of ( 2.8) would then become K ​ L KL, rather than K ​ L / 2 KL/2. This would improve the bounds obtained by a factor of roughly 5 5.

(3) Improving the zero estimate in Proposition 3.11. Conjecturally, the constants on the right-hand sides of ( 3.17)–( 3.19) should all be 1 1. The most important of these inequalities for our work is ( 3.19). Replacing 3 ​ K 2 ​ L 3K^{2}L by K 2 ​ L K^{2}L would lead to a further reduction by a factor of roughly 2 2 in the bounds obtained.

### 1.6. Structure of this article

In Section 2, we first provide some conventions and notations that will be used throughout this paper and then present our main result for linear forms in three logs in Theorem 2.1. Section 3 contains the lemmas required to prove it, along with Matveev’s result which we use in step (2). Section 4 contains the proof of Theorem 2.1.

Section 5 provides information on the choice of the parameters in Theorem 2.1. This simplifies the use of Theorem 2.1, reducing the selection of the required parameters to the choice of four parameters. The best choice of these four parameters can be found by a quick and easy brute force search.

To demonstrate both the usage of our kit and its benefits, we provide two examples in Section 6, revisiting the linear forms in [9] and [10]. We obtain significant improvements in both examples. The second example also corrects the use of the kit in [10].

Lastly, we include a zero estimate due to Michel Laurent in Appendix A. This is the unpublished zero estimate [18] used in [10], as well as in an earlier version of this paper. In fact, Laurent’s result was responsible for the original kit, as it allowed improvements over [4]. It is also applicable more generally than our situation here, so it will be of interest to other researchers of diophantine and transcendence problems.

### 1.7. Acknowledgements

Foremost, our thanks go to Michel Waldschmidt. He first proposed investigating linear forms in three logarithms to the second author nearly 30 years ago. Since then, he has been very supportive and encouraging to both authors in many ways. Similarly, Michel Laurent has been very generous to this project and to both authors over the years. Damien Roy and Patrice Philippon thoughtfully answered our many questions about zero estimates. Mike Bennett and Yann Bugeaud also deserve our thanks as they were instrumental in bringing both authors together to complete this work. Lastly, we thank the referee for their very careful reading of our paper and their helpful comments.

## 2. Results

### 2.1. Conventions

We start by presenting the type of linear forms in three logarithms that we shall study. We consider three distinct non-zero algebraic numbers α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3}, positive rational integers b 1 b_{1}, b 2 b_{2}, b 3 b_{3} with gcd ⁡ ( b 1, b 2, b 3) = 1 \gcd\left(b_{1},b_{2},b_{3}\right)=1, and the linear form

(2.1) |  | Λ = b 1 ​ log ⁡ α 1 + b 2 ​ log ⁡ α 2 − b 3 ​ log ⁡ α 3 ≠ 0. \Lambda=b_{1}\log\alpha_{1}+b_{2}\log\alpha_{2}-b_{3}\log\alpha_{3}\neq 0. |  |

We restrict our study to the following two cases:

- •

the real case: α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} are real numbers greater than 1 1, and the logarithms of the α i \alpha_{i} ’s are all real and positive. Furthermore, we assume that α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} are multiplicatively independent over ℚ \mathbb{Q}. Of course, then the log ⁡ α j \log\alpha_{j} ’s are ℚ \mathbb{Q} -linearly independent. For many applications, this last assumption holds, so in practice this should cause little restriction.

- •

the imaginary case: α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} are complex numbers ≠ 1 \neq 1 of modulus one, and the logarithms of the α i \alpha_{i} are arbitrary determinations of the logarithm (then any of these determinations is purely imaginary). Similar to the previous case, here we will assume that at least two of these α \alpha ’s are multiplicatively independent over ℚ \mathbb{Q} and the third one, if not multiplicatively independent of the other two, is a root of unity. We shall see later (see Lemma 3.16) that in this case, the log ⁡ α j \log\alpha_{j} ’s are again ℚ \mathbb{Q} –linearly independent. Once again, in practical examples, this last condition holds.

In practice, these restrictions do not cause any inconvenience since

 | | Λ | ≥ max ⁡ { | Re ⁡ ( Λ) |, | Im ⁡ ( Λ) | }. \left|\Lambda\right|\geq\max\left\{\left|\Real(\Lambda)\right|,\left|\Imag(\Lambda)\right|\right\}. |  |

After possibly rearranging the terms and possibly replacing some logarithms by their negatives in the imaginary case, we may assume that

 | b 3 ​ | log ⁡ α 3 | = b 1 ​ | log ⁡ α 1 | + b 2 ​ | log ⁡ α 2 | ± | Λ |. b_{3}\left|\log\alpha_{3}\right|=b_{1}\left|\log\alpha_{1}\right|+b_{2}\left|\log\alpha_{2}\right|\pm\left|\Lambda\right|. |  |

Notice that this introduces an important assymmetry between the roles of the coefficients b 1 b_{1}, b 2 b_{2} and b 3 b_{3}.

Like the authors of [4], we use Laurent’s method (see [15, 16]), and consider a suitable interpolation determinant, Δ \Delta. However, our interpolation determinant differs from the one in [4] (which was also used in [9, 10]). We follow the construction of Waldschmidt in Section 7.4 of [31]. In examples, this change improves the bounds we obtain by a factor of roughly 4 4 – 5 5.

### 2.2. Notation

We collect here some of the notation that we will use throughout this paper.

ℕ \mathbb{N} will denote the set of non-negative rational integers.

∙ \bullet K K, L L, R R, S S, T T are positive rational integers with K ≥ 3 K\geq 3 and L ≥ 5 L\geq 5.

∙ \bullet Put N = K ⁡ ( K + 1) ​ L / 2 N=K(K+1)L/2 and we assume that R ​ S ​ T ≥ N RST\geq N.

∙ \bullet Let i i be an index from 1 1 to N N such that ( k i, m i, ℓ i) \left(k_{i},m_{i},\ell_{i}\right) runs through all triples of integers with k i ≥ 0 k_{i}\geq 0, m i ≥ 0 m_{i}\geq 0, k i + m i ≤ K − 1 k_{i}+m_{i}\leq K-1 and 0 ≤ ℓ i ≤ L − 1 0\leq\ell_{i}\leq L-1. So each 0 ≤ k i ≤ K − 1 0\leq k_{i}\leq K-1 occurs ( K − k i) ​ L \left(K-k_{i}\right)L times, and similarly each m i m_{i} occurs ( K − m i) ​ L \left(K-m_{i}\right)L times, and each number 0 0, …, L − 1 L-1 occurs K ⁡ ( K + 1) / 2 K(K+1)/2 times as an ℓ i \ell_{i}.

This is the main difference with the construction in [4], where the conditions 0 ≤ k i, m i ≤ K − 1 0\leq k_{i},m_{i}\leq K-1 are used instead.

∙ \bullet Put

(2.2) |  | g = 1 4 − N 12 ​ R ​ S ​ T, G 1 = N ​ L ​ R 2 ​ g, G 2 = N ​ L ​ S 2 ​ g, G 3 = N ​ L ​ T 2 ​ g. g=\frac{1}{4}-\frac{N}{12RST},\quad G_{1}=\frac{NLR}{2}g,\quad G_{2}=\frac{NLS}{2}g,\quad G_{3}=\frac{NLT}{2}g. |  |

∙ \bullet With d 1 = gcd ⁡ ( b 1, b 3) d_{1}=\gcd\left(b_{1},b_{3}\right) and d 2 = gcd ⁡ ( b 2, b 3) d_{2}=\gcd\left(b_{2},b_{3}\right), put

(2.3) |  | b 1 = d 1 ​ b 1 ′, b 2 = d 2 ​ b 2 ′′, b 3 = d 1 ​ b 3 ′ = d 2 ​ b 3 ′′, β 1 = b 1 / b 3 = b 1 ′ / b 3 ′, β 2 = b 2 / b 3 = b 2 ′′ / b 3 ′′. b_{1}=d_{1}b_{1}^{\prime},\ b_{2}=d_{2}b_{2}^{\prime\prime},\ b_{3}=d_{1}b_{3}^{\prime}=d_{2}b_{3}^{\prime\prime},\ \beta_{1}=b_{1}/b_{3}=b_{1}^{\prime}/b_{3}^{\prime},\ \beta_{2}=b_{2}/b_{3}=b_{2}^{\prime\prime}/b_{3}^{\prime\prime}. |  |

∙ \bullet Let

(2.4) |  | λ i = ℓ i − L − 1 2, η 0 = R − 1 2 + β 1 ​ T − 1 2, ζ 0 = S − 1 2 + β 2 ​ T − 1 2. \lambda_{i}=\ell_{i}-\frac{L-1}{2},\quad\eta_{0}=\frac{R-1}{2}+\beta_{1}\frac{T-1}{2},\quad\zeta_{0}=\frac{S-1}{2}+\beta_{2}\frac{T-1}{2}. |  |

∙ \bullet Let

(2.5) |  | b = ( b 3 ′ ​ η 0) ​ ( b 3 ′′ ​ ζ 0) ​ ( ∏ k = 1 K − 1 ( k!) K − k) − 12 K ​ ( K − 1) ​ ( K + 1). b=\left(b_{3}^{\prime}\eta_{0}\right)\left(b_{3}^{\prime\prime}\zeta_{0}\right)\left(\prod_{k=1}^{K-1}(k!)^{K-k}\right)^{-\frac{12}{K(K-1)(K+1)}}. |  |

Similar to the b b in Théorème 1 of [20], this quantity arises naturally in our proof – see the end of the proof of Proposition 3.7.

The expression involving the product of factorials here is also different from that in [4], due to our different construction.

∙ \bullet Now we define the interpolation determinant that we shall use to prove our results,

(2.6) |  | Δ = det ( ( r j ​ b 3 ′ + t j ​ b 1 ′ k i) ​ ( s j ​ b 3 ′′ + t j ​ b 2 ′′ m i) ​ α 1 ℓ i ​ r j ​ α 2 ℓ i ​ s j ​ α 3 ℓ i ​ t j), \Delta=\det\left(\binom{r_{j}b_{3}^{\prime}+t_{j}b_{1}^{\prime}}{k_{i}}\binom{s_{j}b_{3}^{\prime\prime}+t_{j}b_{2}^{\prime\prime}}{m_{i}}\alpha_{1}^{\ell_{i}r_{j}}\alpha_{2}^{\ell_{i}s_{j}}\alpha_{3}^{\ell_{i}t_{j}}\right), |  |

where 1 ≤ i, j ≤ N 1\leq i,j\leq N, r j r_{j}, s j s_{j} and t j t_{j} are non-negative integers less than R R, S S and T T, respectively, such that ( r j, s j, t j) \left(r_{j},s_{j},t_{j}\right) runs over N N distinct triples.

∙ \bullet Lastly, with r j r_{j}, s j s_{j} and t j t_{j} as above in the definition of our interpolation determinant, we let

 | M 1 = L − 1 2 ​ ∑ j = 1 N r j, M 2 = L − 1 2 ​ ∑ j = 1 N s j, M 3 = L − 1 2 ​ ∑ j = 1 N t j. M_{1}=\frac{L-1}{2}\sum_{j=1}^{N}r_{j},\qquad M_{2}=\frac{L-1}{2}\sum_{j=1}^{N}s_{j},\qquad M_{3}=\frac{L-1}{2}\sum_{j=1}^{N}t_{j}. |  |

Here, and throughout, by α β \alpha^{\beta}, we mean exp ⁡ ( β ​ log ⁡ α) \exp\left(\beta\log\alpha\right) for any complex numbers α \alpha and β \beta with α ≠ 0 \alpha\neq 0 and some determination of the logarithm.

### 2.3. Main Theorem

With the above conventions and notation, we can present our main result.

###### Theorem 2.1.

Let α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} be three distinct non-zero algebraic numbers which, along with their logarithms, satisfy one of the two conditions at the start of this section. Also let b 1 b_{1}, b 2 b_{2}, b 3 b_{3} and Λ \Lambda be as there. Assume that

 | 0 < | Λ | < 2 ​ π / w, 0<\left|\Lambda\right|<2\pi/w, |  |

where w w is the maximal order of a root of unity belonging to the number field ℚ ⁡ ( α 1, α 2, α 3) \mathbb{Q}\left(\alpha_{1},\alpha_{2},\alpha_{3}\right) 1 1 1 If D D is the degree of this number field, then φ ⁡ ( w) ≤ D \varphi(w)\leq D, where φ \varphi is the Euler totient function. Using [27, Theorem 15] and some calculation for small w w, we see that φ ⁡ ( w) ≥ ( w / 2) 0.63 \varphi(w)\geq(w/2)^{0.63}, which implies w < 2 ​ D 1.6 w<2D^{1.6}. Hence 0 < | Λ | < 2 ​ π / w 0<\left|\Lambda\right|<2\pi/w is satisfied if 0 < | Λ | ≤ π ​ D − 1.6 0<\left|\Lambda\right|\leq\pi D^{-1.6} and then Λ ∉ i ​ π ​ ℚ \Lambda\not\in i\pi\mathbb{Q}. Obviously, Λ ∉ i ​ π ​ ℚ \Lambda\not\in i\pi\mathbb{Q} is also satisfied when Λ \Lambda is real and non-zero..

Let R 1 R_{1}, R 2 R_{2}, R 3 R_{3}, S 1 S_{1}, S 2 S_{2}, S 3 S_{3}, T 1 T_{1}, T 2 T_{2}, T 3 T_{3} be positive rational integers with

(2.7) |  | R > R 1 + R 2 + R 3, S > S 1 + S 2 + S 3 ​ and ​ T > T 1 + T 2 + T 3. R>R_{1}+R_{2}+R_{3},\quad S>S_{1}+S_{2}+S_{3}\text{ and }T>T_{1}+T_{2}+T_{3}. |  |

Let ρ ≥ 2 \rho\geq 2 be a real number. Suppose that

(2.8) |  | ( K ​ L 2 + L 2 − 0.37 ​ K − 2) ​ log ⁡ ρ ≥ ( 𝒟 + 1) ​ log ⁡ N + g ​ L ​ ( a 1 ​ R + a 2 ​ S + a 3 ​ T) + 2 ​ 𝒟 ​ ( K − 1) ​ log ⁡ b 3. \left(\frac{KL}{2}+\frac{L}{2}-0.37K-2\right)\log\rho\geq(\mathcal{D}+1)\log N+gL\left(a_{1}R+a_{2}S+a_{3}T\right)+\frac{2\mathcal{D}(K-1)\log b}{3}. |  |

where

 | a i ≥ ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i) for i = 1, 2, 3. a_{i}\geq\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right)\quad\text{ for }\quad i=1,~2,~3. |  |

Put 𝒱 = ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) \mathcal{V}=\sqrt{\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)}. If, for some positive real number χ \chi,

(2.9) |  |  | ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) > K ​ max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1, χ ​ 𝒱 }, \displaystyle\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)>K\max\left\{R_{1}+S_{1}+1,S_{1}+T_{1}+1,R_{1}+T_{1}+1,\chi\mathcal{V}\right\}, |  |

(2.10) |  |  | Card { α 1 r α 2 s α 3 t: 0 ≤ r ≤ R 1, 0 ≤ s ≤ S 1, 0 ≤ t ≤ T 1 } > L, \displaystyle\card\,\left\{\alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t}:0\leq r\leq R_{1},\,0\leq s\leq S_{1},\,0\leq t\leq T_{1}\right\}>L, |  |

(2.11) |  |  | Card { α 1 r α 2 s α 3 t: 0 ≤ r ≤ R 2, 0 ≤ s ≤ S 2, 0 ≤ t ≤ T 2 } > 2 K L, \displaystyle\card\,\left\{\alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t}:0\leq r\leq R_{2},0\leq s\leq S_{2},0\leq t\leq T_{2}\right\}>2KL, |  |

(2.12) |  |  | ( R 2 + 1) ​ ( S 2 + 1) ​ ( T 2 + 1) > K 2 ​ and \displaystyle\left(R_{2}+1\right)\left(S_{2}+1\right)\left(T_{2}+1\right)>K^{2}\text{ and} |  |

(2.13) |  |  | ( R 3 + 1) ​ ( S 3 + 1) ​ ( T 3 + 1) > 3 ​ K 2 ​ L \displaystyle\left(R_{3}+1\right)\left(S_{3}+1\right)\left(T_{3}+1\right)>3K^{2}L |  |

all hold, then either

 | Λ ′:= | Λ | ⋅ L ​ T ​ e L ​ T ​ | Λ | / ( 2 ​ b 3) 2 ​ | b 3 | > ρ − K ​ L \Lambda^{\prime}:=\left|\Lambda\right|\cdot\frac{LTe^{LT\left|\Lambda\right|/(2b_{3})}}{2\left|b_{3}\right|}>\rho^{-KL} |  |

or at least one of the following conditions ( 2.14) or ( 2.15) holds:

(2.14) |  | | b 1 | ≤ max ⁡ { R 1, R 2 } and | b 2 | ≤ max ⁡ { S 1, S 2 } and | b 3 | ≤ max ⁡ { T 1, T 2 }, \left|b_{1}\right|\leq\max\left\{R_{1},R_{2}\right\}\quad\text{and}\quad\left|b_{2}\right|\leq\max\left\{S_{1},S_{2}\right\}\quad\text{and}\quad\left|b_{3}\right|\leq\max\left\{T_{1},T_{2}\right\}, |  |

(2.15) |  | there exist u 1, u 2, u 3 ∈ ℤ such that u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = 0, with gcd ⁡ ( u 1, u 2, u 3) = 1, \text{there exist $u_{1},u_{2},u_{3}\in\mathbb{Z}$ such that $u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=0$, with $\gcd\left(u_{1},u_{2},u_{3}\right)=1$}, |  |

 | | u 1 | ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, | u 2 | ≤ ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 } and | u 3 | ≤ ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 }, \left|u_{1}\right|\leq\frac{(S_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{S_{1},T_{1}\}},\quad\left|u_{2}\right|\leq\frac{(R_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{R_{1},T_{1}\}}\quad\text{and}\quad\left|u_{3}\right|\leq\frac{(R_{1}+1)(S_{1}+1)}{\mathcal{M}-\max\{R_{1},S_{1}\}}, |  |

where ℳ = max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1, χ ​ 𝒱 } \mathcal{M}=\max\left\{R_{1}+S_{1}+1,S_{1}+T_{1}+1,R_{1}+T_{1}+1,\chi\mathcal{V}\right\}.

## 3. Preliminaries

### 3.1. Matveev’s theorem for three logarithms

We will need the special case of three logarithms of the theorem of E. M. Matveev. So we quote his result in this case here.

###### Theorem 3.1 (Matveev).

Let α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} be three distinct non-zero algebraic numbers, let log ⁡ α 1 \log\alpha_{1}, log ⁡ α 2 \log\alpha_{2} and log ⁡ α 3 \log\alpha_{3} be ℚ \mathbb{Q} –linearly independent logarithms of these algebraic numbers and let b 1 b_{1}, b 2 b_{2} and b 3 b_{3} be rational integers with b 1 ≠ 0 b_{1}\neq 0. Put

 | Λ = b 1 ​ log ⁡ α 1 + b 2 ​ log ⁡ α 2 + b 3 ​ log ⁡ α 3. \Lambda=b_{1}\log\alpha_{1}+b_{2}\log\alpha_{2}+b_{3}\log\alpha_{3}. |  |

Let

 | D = [ℚ ( α 1, α 2, α 3): ℚ] and χ = [ℝ ( α 1, α 2, α 3): ℝ]. D=\left[\mathbb{Q}\left(\alpha_{1},\alpha_{2},\alpha_{3}\right):\mathbb{Q}\right]\hskip 8.53581pt\text{ and }\hskip 8.53581pt\chi=\left[\mathbb{R}\left(\alpha_{1},\alpha_{2},\alpha_{3}\right):\mathbb{R}\right]. |  |

Let A 1 A_{1}, A 2 A_{2} and A 3 A_{3} be positive real numbers, which satisfy

 | A j ≥ max ⁡ { D ​ h ⁡ ( α j), | log ⁡ α j | } ( 1 ≤ j ≤ 3), A_{j}\geq\max\left\{D\h\left(\alpha_{j}\right),\left|\log\alpha_{j}\right|\right\}\quad(1\leq j\leq 3), |  |

where h \h is the absolute logarithmic Weil height.

Assume that

 | B ≥ max ⁡ { | b j | ​ A j / A 1: 1 ≤ j ≤ 3 }. B\geq\max\left\{\left|b_{j}\right|A_{j}/A_{1}:1\leq j\leq 3\right\}. |  |

Also define

 | C 1 = 5 ⋅ 16 5 6 ​ χ ​ e 3 ​ ( 7 + 2 ​ χ) ​ ( 3 ​ e 2) χ ​ ( 26.25 + log ⁡ ( D 2 ​ log ⁡ ( e ​ D))). C_{1}=\frac{5\cdot 16^{5}}{6\chi}e^{3}(7+2\chi)\left(\frac{3e}{2}\right)^{\chi}\left(26.25+\log\left(D^{2}\log(eD)\right)\right). |  |

Then

 | log ⁡ | Λ | > − C 1 ​ D 2 ​ A 1 ​ A 2 ​ A 3 ​ log ⁡ ( 1.5 ​ e ​ D ​ B ​ log ⁡ ( e ​ D)). \log\left|\Lambda\right|>-C_{1}D^{2}A_{1}A_{2}A_{3}\log\left(1.5eDB\log(eD)\right). |  |

###### Proof.

This is a very slight simplification of Theorem 2.1 of [22] applied with n = 3 n=3. Our only change is to note that | b j | ​ A j / A 1 ≥ 1 \left|b_{j}\right|A_{j}/A_{1}\geq 1 for j = 1 j=1, so the outer max in Matveev’s inequality B ≥ max ⁡ { 1, max ⁡ { | b j | ​ A j / A 1: 1 ≤ j ≤ 3 } } B\geq\max\left\{1,\max\left\{\left|b_{j}\right|A_{j}/A_{1}:1\leq j\leq 3\right\}\right\} is not needed. ∎

It is because the log ⁡ α j \log\alpha_{j} ’s are ℚ \mathbb{Q} –linearly independent in both of the cases that we present in Subsection 2.1 that we can use Theorem 2.1 of [22] in this work.

Note that it is also possible to use the results of Aleksentsev [1] in place of Matveev’s result. This would give a slightly smaller upper bound in Step (2), but make no difference to the final results obtained from the kit.

### 3.2. Some combinatorial inequalities

This subsection contains some results used in the estimates of the interpolation determinant.

###### Lemma 3.2.

Let K K, L L, N N, R R, S S, T T, G 1 G_{1} and M 1 M_{1} be as above. Put

 | ℓ n = ⌊ 2 ​ ( n − 1) K ⁡ ( K + 1) ⌋, 1 ≤ n ≤ N, \ell_{n}=\left\lfloor\frac{2(n-1)}{K(K+1)}\right\rfloor,\quad 1\leq n\leq N, |  |

and ( r 1, …, r N) ∈ { 0, 1, …, R − 1 } N \left(r_{1},\ldots,r_{N}\right)\in\{0,1,\ldots,R-1\}^{N}. Suppose that for each r ∈ { 0, 1, …, R − 1 } r\in\{0,1,\ldots,R-1\} there are at most S ​ T ST indices j j such that r j = r r_{j}=r. Then

 | | ∑ n = 1 N ℓ n ​ r n − M 1 | ≤ G 1. \left|\sum_{n=1}^{N}\ell_{n}r_{n}-M_{1}\right|\leq G_{1}. |  |

###### Proof.

Apply Lemme 4 in [20] with K K there set to K ⁡ ( K + 1) / 2 K(K+1)/2. ∎

As in [4, Section 1.3] or [31, p. 192], for ( k, m) ∈ ℕ 2 (k,m)\in\mathbb{N}^{2}, we put ‖ ( k, m) ‖ = k + m \|(k,m)\|=k+m. And for any I, K 0 ∈ ℕ I,K_{0}\in\mathbb{N}, we put

(3.1) |  | Θ ⁡ ( K 0, I) = min ⁡ { ‖ ( k 1, m 1) ‖ + ⋯ + ‖ ( k I, m I) ‖ }, \Theta\left(K_{0},I\right)=\min\left\{\|\left(k_{1},m_{1}\right)\|+\cdots+\|\left(k_{I},m_{I}\right)\|\right\}, |  |

where the minimum is taken over all the sets of I I pairs ( k 1, m 1) \left(k_{1},m_{1}\right), …, ( k I, m I) ∈ ℕ 2 \left(k_{I},m_{I}\right)\in\mathbb{N}^{2} which are pairwise distinct and satisfy m 1 m_{1}, …, m I ≤ K 0 m_{I}\leq K_{0}. Then, we have

###### Lemma 3.3.

Let K 0 K_{0} and I I be positive integers with I ≥ K 0 ​ ( K 0 + 1) / 2 I\geq K_{0}\left(K_{0}+1\right)/2. Then

 | Θ ⁡ ( K 0, I) ≥ ( I 2 2 ​ ( K 0 + 1)) ​ ( 1 + ( K 0 − 1) ​ ( K 0 + 1) I − K 0 ​ ( K 0 + 2) ​ ( K 0 + 1) 2 12 ​ I 2). \Theta\left(K_{0},I\right)\geq\left(\frac{I^{2}}{2(K_{0}+1)}\right)\left(1+\frac{(K_{0}-1)(K_{0}+1)}{I}-\frac{K_{0}(K_{0}+2)(K_{0}+1)^{2}}{12I^{2}}\right). |  |

###### Remark.

This is an improvement of the Lemma 1.4 of [4]. If I ≡ 0 mod ( K 0 + 1) I\equiv 0\bmod\left(K_{0}+1\right) and K 0 K_{0} even, then this result is best possible. In the worst cases, the difference between the left and right sides is at most roughly K 0 / 8 K_{0}/8.

###### Proof.

We follow more or less the proof of Lemma 1.4 of [4], the main difference being the introduction of the term r r in the expression for I I below.

The smallest value for the sum ‖ ( k 1, m 1) ‖ + ⋯ + ‖ ( k I, m I) ‖ \|\left(k_{1},m_{1}\right)\|+\cdots+\|\left(k_{I},m_{I}\right)\| is reached when we choose successively, for each integer n = 0 n=0, 1, … all the points in the domain

 | D n = { ( k, m) ∈ ℕ 2: m ≤ K 0 ​ and ​ k + m = n }, D_{n}=\left\{(k,m)\in\mathbb{N}^{2}:m\leq K_{0}\text{ and }k+m=n\right\}, |  |

and stop when the total number of points is I I. Moreover,

 | Card ⁡ ( D n) = { n + 1, if n ≤ K 0, K 0 + 1, if n ≥ K 0. \card\left(D_{n}\right)=\begin{cases}n+1,&\text{if $n\leq K_{0}$,}\\ K_{0}+1,&\text{if \ $n\geq K_{0}$.}\end{cases} |  |

Hence, for A ≥ K 0 A\geq K_{0}, the number of points in D 0 ∪ ⋯ ∪ D A − 1 D_{0}\cup\cdots\cup D_{A-1} is

 | ∑ n = 0 K 0 − 1 ( n + 1) + ∑ n = K 0 A − 1 ( K 0 + 1) = K 0 ​ ( K 0 + 1) 2 + ( A − K 0) ​ ( K 0 + 1) = ( A − K 0 2) ​ ( K 0 + 1). \sum_{n=0}^{K_{0}-1}(n+1)+\sum_{n=K_{0}}^{A-1}(K_{0}+1)=\frac{K_{0}\left(K_{0}+1\right)}{2}+\left(A-K_{0}\right)\left(K_{0}+1\right)=\left(A-\frac{K_{0}}{2}\right)(K_{0}+1). |  |

Letting A A be the largest integer such that Card ⁡ ( D 0 ∪ ⋯ ∪ D A − 1) ≤ I \card\left(D_{0}\cup\cdots\cup D_{A-1}\right)\leq I, we can write

 | I = ( A − K 0 2) ​ ( K 0 + 1) + r with 0 ≤ r ≤ K 0, I=\left(A-\frac{K_{0}}{2}\right)\left(K_{0}+1\right)+r\quad\text{with $0\leq r\leq K_{0}$}, |  |

provided that I ≥ K 0 ​ ( K 0 + 1) / 2 I\geq K_{0}\left(K_{0}+1\right)/2. Then

 | Θ ⁡ ( K 0, I) = ∑ n = 0 K 0 − 1 n ⁡ ( n + 1) + ∑ n = K 0 A − 1 n ⁡ ( K 0 + 1) + r ​ A. \Theta\left(K_{0},I\right)=\sum_{n=0}^{K_{0}-1}n(n+1)+\sum_{n=K_{0}}^{A-1}n(K_{0}+1)+rA. |  |

Here

 |  | ∑ n = 0 K 0 − 1 n ⁡ ( n + 1) + ∑ n = K 0 A − 1 n ⁡ ( K 0 + 1) \displaystyle\sum_{n=0}^{K_{0}-1}n(n+1)+\sum_{n=K_{0}}^{A-1}n(K_{0}+1) |  |

 | = \displaystyle= | ( K 0 − 1) ​ K 0 ​ ( 2 ​ K 0 − 1) 6 + ( K 0 − 1) ​ K 0 2 + K 0 + 1 2 ​ ( A ⁡ ( A − 1) − K 0 ​ ( K 0 − 1)) \displaystyle\frac{(K_{0}-1)K_{0}(2K_{0}-1)}{6}+\frac{(K_{0}-1)K_{0}}{2}+\frac{K_{0}+1}{2}\left(A(A-1)-K_{0}(K_{0}-1)\right) |  |

 | = \displaystyle= | ( K 0 − 1) ​ K 0 ​ ( 2 ​ K 0 + 2) 6 + K 0 + 1 2 ​ A ​ ( A − 1) − ( K 0 − 1) ​ K 0 ​ ( K 0 + 1) 2 \displaystyle\frac{(K_{0}-1)K_{0}(2K_{0}+2)}{6}+\frac{K_{0}+1}{2}A(A-1)-\frac{(K_{0}-1)K_{0}(K_{0}+1)}{2} |  |

 | = \displaystyle= | K 0 + 1 2 ​ ( A ​ ( A − 1) − K 0 ​ ( K 0 − 1) 3) \displaystyle\frac{K_{0}+1}{2}\left(A(A-1)-\frac{K_{0}(K_{0}-1)}{3}\right) |  |

and we get

(3.2) |  | Θ ⁡ ( K 0, I) = K 0 + 1 2 ​ ( A ⁡ ( A − 1) − K 0 ​ ( K 0 − 1) 3) + r ​ A. \Theta\left(K_{0},I\right)=\frac{K_{0}+1}{2}\left(A(A-1)-\frac{K_{0}(K_{0}-1)}{3}\right)+rA. |  |

We can write

 | A = K 0 2 + I − r K 0 + 1. A=\frac{K_{0}}{2}+\frac{I-r}{K_{0}+1}. |  |

So using ( 3.2) and then this expression for A A in terms of r r, we have

 | ∂ Θ ∂ r = K 0 + 1 2 ​ ( 2 ​ A − 1) ​ ∂ A ∂ r + A + r ​ ∂ A ∂ r = − 2 ​ A − 1 2 + A − r K 0 + 1 = 1 2 − r K 0 + 1, \frac{\partial\Theta}{\partial r}=\frac{K_{0}+1}{2}(2A-1)\frac{\partial A}{\partial r}+A+r\frac{\partial A}{\partial r}=-\frac{2A-1}{2}+A-\frac{r}{K_{0}+1}=\frac{1}{2}-\frac{r}{K_{0}+1}, |  |

which shows that the minimum of Θ \Theta is reached either for r = 0 r=0 or r = K 0 r=K_{0}. It is easy to verify that Θ \Theta takes the same value for r = 0 r=0 and r = K 0 + 1 r=K_{0}+1 (which is indeed out of the range of r r), this implies that the minimum is reached for r = 0 r=0. It follows that

 | 2 ​ Θ ​ ( K 0, I) K 0 + 1 \displaystyle\frac{2\Theta(K_{0},I)}{K_{0}+1} | ≥ ( K 0 2 + I K 0 + 1) ​ ( K 0 2 + I K 0 + 1 − 1) − K 0 ​ ( K 0 − 1) 3 \displaystyle\geq\left(\frac{K_{0}}{2}+\frac{I}{K_{0}+1}\right)\left(\frac{K_{0}}{2}+\frac{I}{K_{0}+1}-1\right)-\frac{K_{0}(K_{0}-1)}{3} |  |

 |  | = K 0 2 4 + I 2 ( K 0 + 1) 2 + K 0 ​ I K 0 + 1 − K 0 2 − I K 0 + 1 − K 0 2 3 + K 0 3 \displaystyle=\frac{K_{0}^{2}}{4}+\frac{I^{2}}{(K_{0}+1)^{2}}+\frac{K_{0}I}{K_{0}+1}-\frac{K_{0}}{2}-\frac{I}{K_{0}+1}-\frac{K_{0}^{2}}{3}+\frac{K_{0}}{3} |  |

 |  | = I 2 ( K 0 + 1) 2 + ( K 0 − 1) ​ I K 0 + 1 − K 0 2 12 − K 0 6 \displaystyle=\frac{I^{2}}{(K_{0}+1)^{2}}+\frac{(K_{0}-1)I}{K_{0}+1}-\frac{K_{0}^{2}}{12}-\frac{K_{0}}{6} |  |

 |  | = ( I K 0 + 1) 2 ​ ( 1 + ( K 0 − 1) ​ ( K 0 + 1) I − K 0 ​ ( K 0 + 2) ​ ( K 0 + 1) 2 12 ​ I 2). \displaystyle=\left(\frac{I}{K_{0}+1}\right)^{2}\left(1+\frac{(K_{0}-1)(K_{0}+1)}{I}-\frac{K_{0}(K_{0}+2)(K_{0}+1)^{2}}{12I^{2}}\right). |  |

This proves the lemma. ∎

###### Lemma 3.4.

Let K K, L L and N N be as in Subsection 2.2 with the additional assumptions that K ≥ 3 K\geq 3 and L ≥ 5 L\geq 5. Also let 0 ≤ I ≤ N 0\leq I\leq N be an integer and Θ ⁡ ( K 0, I) \Theta\left(K_{0},I\right) be as defined in ( 3.1). Then

 | K ​ L ​ ( N − I) + Θ ⁡ ( K − 1, I) ≥ N 2 2 ​ K ​ ( 1 + 2 L − 6 K ​ L − 1 3 ​ L 2). KL(N-I)+\Theta\left(K-1,I\right)\geq\frac{N^{2}}{2K}\left(1+\frac{2}{L}-\frac{6}{KL}-\frac{1}{3L^{2}}\right). |  |

###### Proof.

Suppose that I ≤ N / 2 I\leq N/2. Then

 | K ​ L ​ ( N − I) ≥ K ​ L ​ N 2 = N 2 K + 1 = 3 2 ​ N 2 2 ​ K, KL(N-I)\geq\frac{KLN}{2}=\frac{N^{2}}{K+1}=\frac{3}{2}\frac{N^{2}}{2K}, |  |

since K ≥ 3 K\geq 3. Since L ≥ 5 L\geq 5, we have 1 + 2 / L − 6 / ( K ​ L) − 1 / ( 3 ​ L 2) < 1 + 2 / L < 3 / 2 1+2/L-6/(KL)-1/\left(3L^{2}\right)<1+2/L<3/2. Since Θ ⁡ ( K − 1, I) ≥ 0 \Theta(K-1,I)\geq 0, the result follows in this case.

We now consider I > N / 2 I>N/2. This and L ≥ 5 L\geq 5 implies that I ≥ ( 5 / 4) ​ K 2 I\geq(5/4)K^{2}, so we can apply Lemma 3.3 with K 0 = K − 1 K_{0}=K-1 to get

 | K ​ L ​ ( N − I) + Θ ⁡ ( K − 1, I) ≥ K ​ L ​ ( N − I) + I 2 2 ​ K ​ ( 1 + ( K − 2) ​ K I − ( K − 1) ​ ( K + 1) ​ K 2 12 ​ I 2). KL(N-I)+\Theta(K-1,I)\geq KL(N-I)+\frac{I^{2}}{2K}\left(1+\frac{(K-2)K}{I}-\frac{(K-1)(K+1)K^{2}}{12I^{2}}\right). |  |

The derivative of the right-hand side with respect to I I is

 | 2 ​ I − 2 ​ K 2 ​ L + K 2 − 2 ​ K 2 ​ K. \frac{2I-2K^{2}L+K^{2}-2K}{2K}. |  |

This is linear in I I and the coefficient of I I is positive, so once the derivative is positive, it remains positive for all larger values of I I. It equals 0 0 at I = K 2 ​ L − K 2 / 2 + K I=K^{2}L-K^{2}/2+K. We can write

 | K 2 ​ L − K 2 / 2 + K = K ⁡ ( K + 1) ​ L / 2 + ( K 2 / 2 − K / 2) ​ ( L − 1) + K / 2. K^{2}L-K^{2}/2+K=K(K+1)L/2+\left(K^{2}/2-K/2\right)(L-1)+K/2. |  |

For K ≥ 2 K\geq 2, we have K 2 / 2 − K / 2 ≥ 1 K^{2}/2-K/2\geq 1 and since L ≥ 1 L\geq 1, we have ( K 2 / 2 − K / 2) ​ ( L − 1) + K / 2 ≥ 1 / 2 \left(K^{2}/2-K/2\right)(L-1)+K/2\geq 1/2. So this critical value of I I is larger than N N. Hence the minimum value of the above lower bound for K ​ L ​ ( N − I) + Θ ⁡ ( K − 1, I) KL(N-I)+\Theta(K-1,I) occurs at I = N I=N. Thus

 | K ​ L ​ ( N − I) + Θ ⁡ ( K − 1, I) ≥ N 2 2 ​ K ​ ( 1 + 2 L − 6 K ​ L − 1 3 ​ L 2) + 2 ​ K + 18 ​ L 3 ​ K ​ ( K + 1) ​ L 2, KL(N-I)+\Theta(K-1,I)\geq\frac{N^{2}}{2K}\left(1+\frac{2}{L}-\frac{6}{KL}-\frac{1}{3L^{2}}\right)+\frac{2K+18L}{3K(K+1)L^{2}}, |  |

where the equality was obtained by using Maple. This implies that the lemma holds for all I I. ∎

###### Lemma 3.5.

(a) Let K > 1 K>1 be an integer, then

(3.3) |  | log ⁡ ( ∏ k = 1 K − 1 ( k!) K − k) 12 / ( K ​ ( K − 1) ​ ( K + 1)) ≥ 2 ​ log ⁡ ( K) − 11 / 3. \log\left(\prod_{k=1}^{K-1}(k!)^{K-k}\right)^{12/(K(K-1)(K+1))}\geq 2\log(K)-11/3. |  |

(b) With b b, d 1 d_{1}, d 2 d_{2}, K K, R R, S S and T T as defined in Subsection 2.2, we have

 | log ⁡ b ≤ \displaystyle\log b\leq | log ⁡ ( R − 1) ​ b 3 + ( T − 1) ​ b 1 2 ​ d 1 + log ⁡ ( S − 1) ​ b 2 + ( T − 1) ​ b 3 2 ​ d 2 \displaystyle\log\frac{(R-1)b_{3}+(T-1)b_{1}}{2d_{1}}+\log\frac{(S-1)b_{2}+(T-1)b_{3}}{2d_{2}} |  |

 |  | − 2 ​ log ⁡ ( K) + 11 / 3. \displaystyle-2\log(K)+11/3. |  |

###### Proof.

Our proof is a variant of the proof of Lemme 8 of [20], which itself is based on the proof of Lemma 9 in [17].

From the inequality k! ≥ ( k / e) k k!\geq(k/e)^{k}, we have

 | ∑ k = 0 K − 1 ( K − k) ​ log ⁡ ( k!) \displaystyle\sum_{k=0}^{K-1}(K-k)\log(k!) | ≥ ∑ k = 1 K − 1 ( K − k) ​ k ​ ( log ⁡ ( k) − 1) \displaystyle\geq\sum_{k=1}^{K-1}(K-k)k(\log(k)-1) |  |

 |  | = ∑ k = 1 K − 1 ( K − k) ​ k ​ log ⁡ ( k) − ∑ k = 0 K − 1 ( K − k) ​ k. \displaystyle=\sum_{k=1}^{K-1}(K-k)k\log(k)-\sum_{k=0}^{K-1}(K-k)k. |  |

The last term is easily shown to be K ​ ( K + 1) ​ ( K − 1) / 6 K(K+1)(K-1)/6, so that

 | ∑ k = 1 K − 1 ( K − k) ​ log ⁡ k! ≥ ∑ k = 1 K − 1 k ⁡ ( K − k) ​ log ⁡ k − K ​ ( K + 1) ​ ( K − 1) 6. \sum_{k=1}^{K-1}(K-k)\log k!\geq\sum_{k=1}^{K-1}k(K-k)\log k-\frac{K(K+1)(K-1)}{6}. |  |

We now estimate the remaining sum, which we break into two sums:

 | K ​ ∑ k = 1 K − 1 k ​ log ⁡ k − ∑ k = 1 K − 1 k 2 ​ log ⁡ k. K\sum_{k=1}^{K-1}k\log k-\sum_{k=1}^{K-1}k^{2}\log k. |  |

We use the Euler-Maclaurin summation formula to estimate these sums. We shall use the formulation of the Euler-Maclaurin summation formula in equation (7.2.4) p. 303 of [11] with r = 1 r=1:

 | f ⁡ ( 1) + ⋯ + f ⁡ ( n) = ∫ 1 n f ⁡ ( x) ​ 𝑑 x + f ⁡ ( 1) + f ⁡ ( n) 2 + f ′ ​ ( n) + f ′ ​ ( 1) 12 + R 1, f(1)+\cdots+f(n)=\int_{1}^{n}f(x)dx+\frac{f(1)+f(n)}{2}+\frac{f^{\prime}(n)+f^{\prime}(1)}{12}+R_{1}, |  |

where

 | R 1 ≤ 1 2 ​ π 2 ​ ∫ 1 n | f ( 3) ​ ( x) | ​ 𝑑 x. R_{1}\leq\frac{1}{2\pi^{2}}\int_{1}^{n}\left|f^{(3)}(x)\right|dx. |  |

From this point onward in the proof, we use Maple extensively to perform the integrations and algebraic manipulations.

In this way, with n = K − 1 n=K-1 and f ⁡ ( n) = x ​ log ⁡ ( x) f(n)=x\log(x), we have f ′ ​ ( x) = log ⁡ ( x) + 1 f^{\prime}(x)=\log(x)+1 and f ( 3) ​ ( x) = − x − 2 f^{(3)}(x)=-x^{-2}, so 1 / ( 2 π 2) ∫ 1 K − 1 x − 2 d x = ( K − 2) / ( 2 π 2 ( K − 1)) 1/\left(2\pi^{2}\right)\int_{1}^{K-1}x^{-2}dx=(K-2)/\left(2\pi^{2}(K-1)\right) and

 | ∑ k = 1 K − 1 k ​ log ⁡ k ≥ ∫ 1 K − 1 x ​ log ⁡ ( x) ​ 𝑑 x + ( K − 1) ​ log ⁡ ( K − 1) 2 + log ⁡ ( K − 1) + 2 12 − 1 2 ​ π 2. \sum_{k=1}^{K-1}k\log k\geq\int_{1}^{K-1}x\log(x)dx+\frac{(K-1)\log(K-1)}{2}+\frac{\log(K-1)+2}{12}-\frac{1}{2\pi^{2}}. |  |

With n = K − 1 n=K-1 and f ⁡ ( n) = x 2 ​ log ⁡ ( x) f(n)=x^{2}\log(x), we have f ′ ​ ( x) = 2 ​ x ​ log ⁡ ( x) + x f^{\prime}(x)=2x\log(x)+x and f ( 3) ​ ( x) = 2 ​ x − 1 f^{(3)}(x)=2x^{-1}, so 1 / ( 2 π 2) ∫ 1 K − 1 2 x − 1 d x = log ( K − 1) / π 2 1/\left(2\pi^{2}\right)\int_{1}^{K-1}2x^{-1}dx=\log(K-1)/\pi^{2} and

 | ∑ k = 1 K − 1 k 2 ​ log ⁡ k ≤ ∫ 1 K − 1 x 2 ​ log ⁡ ( x) ​ 𝑑 x + ( K − 1) 2 ​ log ⁡ ( K − 1) 2 + 2 ​ ( K − 1) ​ log ⁡ ( K − 1) + K 12 + log ⁡ ( K − 1) 2 ​ π 2. \sum_{k=1}^{K-1}k^{2}\log k\leq\int_{1}^{K-1}x^{2}\log(x)dx+\frac{(K-1)^{2}\log(K-1)}{2}+\frac{2(K-1)\log(K-1)+K}{12}+\frac{\log(K-1)}{2\pi^{2}}. |  |

Combining these two estimates, along with

 | ∫ 1 K − 1 x ​ log ⁡ ( x) ​ 𝑑 x = log ⁡ ( K − 1) 2 ​ K 2 − K 2 4 − K ​ log ⁡ ( K − 1) + K 2 + log ⁡ ( K − 1) 2 \int_{1}^{K-1}x\log(x)dx=\frac{\log(K-1)}{2}K^{2}-\frac{K^{2}}{4}-K\log(K-1)+\frac{K}{2}+\frac{\log(K-1)}{2} |  |

and

 | ∫ 1 K − 1 x 2 ​ log ⁡ ( x) ​ 𝑑 x = log ⁡ ( K − 1) 3 ​ K 3 − K 3 9 − log ⁡ ( K − 1) ​ K 2 + K 2 3 + log ⁡ ( K − 1) ​ K − K 3 − log ⁡ ( K − 1) 3 + 2 9, \int_{1}^{K-1}x^{2}\log(x)dx=\frac{\log(K-1)}{3}K^{3}-\frac{K^{3}}{9}-\log(K-1)K^{2}+\frac{K^{2}}{3}+\log(K-1)K-\frac{K}{3}-\frac{\log(K-1)}{3}+\frac{2}{9}, |  |

we obtain

 | ∑ k = 1 K − 1 k ⁡ ( K − k) ​ log ⁡ k ≥ log ⁡ ( K − 1) ​ K 3 6 − 11 ​ K 3 36 + K 2 6 − log ⁡ ( K − 1) ​ K 12 + ( 7 12 − 1 2 ​ π 2) ​ K − log ⁡ ( K − 1) 2 ​ π 2 − 2 9. \sum_{k=1}^{K-1}k(K-k)\log k\geq\frac{\log(K-1)K^{3}}{6}-\frac{11K^{3}}{36}+\frac{K^{2}}{6}-\frac{\log(K-1)K}{12}+\left(\frac{7}{12}-\frac{1}{2\pi^{2}}\right)K-\frac{\log(K-1)}{2\pi^{2}}-\frac{2}{9}. |  |

Subtracting ( 2 ​ log ⁡ ( K) − 11 / 3) ​ K ​ ( K − 1) ​ ( K + 1) / 12 \left(2\log(K)-11/3\right)K(K-1)(K+1)/12, we obtain

(3.4) |  | log ⁡ ( 1 − 1 / K) 6 ​ K 3 + K 2 6 + log ⁡ ( K 2 / ( K − 1)) 12 ​ K + ( 5 18 − 1 2 ​ π 2) ​ K − log ⁡ ( K − 1) 2 ​ π 2 − 2 9. \frac{\log(1-1/K)}{6}K^{3}+\frac{K^{2}}{6}+\frac{\log\left(K^{2}/(K-1)\right)}{12}K+\left(\frac{5}{18}-\frac{1}{2\pi^{2}}\right)K-\frac{\log(K-1)}{2\pi^{2}}-\frac{2}{9}. |  |

From the series expansion of log ⁡ ( 1 − x) \log(1-x), we find that log ( 1 − 1 / K) > − 1 / K − 1 / ( 2 K 2) − 2 / ( 3 K 3) \log(1-1/K)>-1/K-1/\left(2K^{2}\right)-2/\left(3K^{3}\right) for K ≥ 2 K\geq 2, so ( 3.4) is larger than

 | log ⁡ ( K) 12 ​ K + ( 7 36 − 1 2 ​ π 2) ​ K − log ⁡ ( K − 1) 2 ​ π 2 − 1 3 \frac{\log(K)}{12}K+\left(\frac{7}{36}-\frac{1}{2\pi^{2}}\right)K-\frac{\log(K-1)}{2\pi^{2}}-\frac{1}{3} |  |

for K ≥ 2 K\geq 2.

This expression is positive for K ≥ 3 K\geq 3, since 3 / 12 > 1 / ( 2 ​ π 2) 3/12>1/\left(2\pi^{2}\right) and ( 7 36 − 1 2 ​ π 2) > 1 / 3 \left(\frac{7}{36}-\frac{1}{2\pi^{2}}\right)>1/3. So part (a) holds for K ≥ 3 K\geq 3.

Part (a) also holds for K = 2 K=2, since the left-hand side of ( 3.3) is 0 0 for K = 2 K=2, while the right-hand side is − 2.28 ​ … -2.28\ldots.

(b) Using the definitions of b b, η 0 \eta_{0}, ζ 0 \zeta_{0}, β 1 \beta_{1} and β 3 \beta_{3}, we have

 | b = ( b 3 ′ ​ R − 1 2 + b 1 ′ ​ T − 1 2) ​ ( b 3 ′′ ​ S − 1 2 + b 2 ′′ ​ T − 1 2) ​ ( ∏ k = 1 K − 1 k!) − 12 K ​ ( K − 1) ​ ( K + 1). b=\left(b_{3}^{\prime}\frac{R-1}{2}+b_{1}^{\prime}\frac{T-1}{2}\right)\left(b_{3}^{\prime\prime}\frac{S-1}{2}+b_{2}^{\prime\prime}\frac{T-1}{2}\right)\left(\prod_{k=1}^{K-1}k!\right)^{-\frac{12}{K(K-1)(K+1)}}. |  |

Applying the relationships in ( 2.3), part (b) follows immediately. ∎

### 3.3. An upper bound for | Δ | \left|\Delta\right|

In this subsection, we prove the result below, Proposition 3.7, an upper bound for | Δ | \left|\Delta\right| (also see [9, Proposition 12.5]). We start with an estimate for the zero multiplicity of a certain function, the determinant of a particular matrix, at x = 0 x=0. We closely follow Section 7.2 of [31].

Let K K and N N be positive integers, η 1, …, η N \eta_{1},\ldots,\eta_{N}, ζ 1, …, ζ N \zeta_{1},\ldots,\zeta_{N} elements of ℂ \mathbb{C}, f 1, …, f N f_{1},\ldots,f_{N} analytic functions in ℂ \mathbb{C}, θ 1 \theta_{1} and θ 2 \theta_{2} non-zero complex numbers and p 1, …, p N p_{1},\ldots,p_{N} polynomials in ℂ ⁡ [z 1, z 2] \mathbb{C}\left[z_{1},z_{2}\right] of total degree at most K K. We define, for 1 ≤ i ≤ N 1\leq i\leq N,

 | ϕ i ​ ( z 1, z 2) = p i ​ ( z 1, z 2) ​ f i ​ ( θ 1 ​ z 1 + θ 2 ​ z 2). \phi_{i}\left(z_{1},z_{2}\right)=p_{i}\left(z_{1},z_{2}\right)f_{i}\left(\theta_{1}z_{1}+\theta_{2}z_{2}\right). |  |

Let ℐ \mathcal{I} be a subset of { 1, …, N } \{1,\ldots,N\}. We define an N × N N\times N matrix with entries

 | Φ ℐ ​ ( x) i, j = { ϕ i ​ ( x ​ η j, x ​ ζ j), if i ∈ ℐ, δ i, j ​ ϕ i ​ ( x ​ η j, x ​ ζ j), if i ∉ ℐ, \Phi_{\mathcal{I}}(x)_{i,j}=\left\{\begin{array}[]{ll}\phi_{i}\left(x\eta_{j},x\zeta_{j}\right),&\text{if $i\in\mathcal{I}$},\\ \delta_{i,j}\phi_{i}\left(x\eta_{j},x\zeta_{j}\right),&\text{if $i\not\in\mathcal{I}$},\end{array}\right. |  |

where δ i, j \delta_{i,j} are complex numbers and let Ψ ℐ ​ ( x) = det ( Φ ℐ ​ ( x)) \Psi_{\mathcal{I}}(x)=\det\left(\Phi_{\mathcal{I}}(x)\right).

###### Lemma 3.6.

The function Ψ I ​ ( x) \Psi_{I}(x) has a zero at x = 0 x=0 of multiplicity at least Θ ⁡ ( K, | ℐ |) \Theta\left(K,|\mathcal{I}|\right), where | ℐ | |\mathcal{I}| is the number of elements in ℐ \mathcal{I}.

###### Proof.

This is Lemma 7.2 of [31] in the case of n = 2 n=2, since the total degree of each of the polynomials, p 1, …, p N p_{1},\ldots,p_{N} is at most K K. ∎

Returning to our specific situation here, let K K, L L, N N, R R, S S and T T, along with the r j r_{j} ’s, s j s_{j} ’s and t j t_{j} ’s be as defined in Subsection 2.2.

Recalling our definition of the λ i \lambda_{i} ’s in ( 2.4), we have

 | ∑ i = 1 N λ i = K ⁡ ( K + 1) 2 ​ ∑ i = 0 L − 1 ( i − ( L − 1) / 2) = 0 \sum_{i=1}^{N}\lambda_{i}=\frac{K(K+1)}{2}\sum_{i=0}^{L-1}\left(i-(L-1)/2\right)=0 |  |

and the following slight variation of equation (2.1) in [4] (our Λ ′ \Lambda^{\prime} is slightly different from theirs)

(3.5) |  | α 1 λ i ​ r j ​ α 2 λ i ​ s j ​ α 3 λ i ​ t j = α 1 λ i ​ ( r j + t j ​ β 1) ​ α 2 λ i ​ ( s j + t j ​ β 2) ​ e λ i ​ t j ​ Λ / b 3 = α 1 λ i ​ ( r j + t j ​ β 1) ​ α 2 λ i ​ ( s j + t j ​ β 2) ​ ( 1 + θ i, j ​ Λ ′), \alpha_{1}^{\lambda_{i}r_{j}}\alpha_{2}^{\lambda_{i}s_{j}}\alpha_{3}^{\lambda_{i}t_{j}}=\alpha_{1}^{\lambda_{i}(r_{j}+t_{j}\beta_{1})}\alpha_{2}^{\lambda_{i}(s_{j}+t_{j}\beta_{2})}e^{\lambda_{i}t_{j}\Lambda/b_{3}}=\alpha_{1}^{\lambda_{i}(r_{j}+t_{j}\beta_{1})}\alpha_{2}^{\lambda_{i}(s_{j}+t_{j}\beta_{2})}(1+\theta_{i,j}\Lambda^{\prime}), |  |

where

 | θ i, j = e λ i ​ t j ​ Λ / b 3 − 1 Λ ′ \theta_{i,j}=\frac{e^{\lambda_{i}t_{j}\Lambda/b_{3}}-1}{\Lambda^{\prime}} |  |

and

(3.6) |  | Λ ′ = | Λ | ⋅ L ​ T ​ e L ​ T ​ | Λ | / ( 2 ​ b 3) 2 ​ b 3. \Lambda^{\prime}=\left|\Lambda\right|\cdot\frac{LTe^{LT\left|\Lambda\right|/(2b_{3})}}{2b_{3}}. |  |

Let

(3.7) |  | ϕ i ​ ( η, ζ) = b 3 ′ k i ​ b 3 ′′ m i k i! ​ m i! ​ η k i ​ ζ m i ​ α 1 λ i ​ η ​ α 2 λ i ​ ζ, \phi_{i}(\eta,\zeta)=\frac{{b_{3}^{\prime}}^{k_{i}}{b_{3}^{\prime\prime}}^{m_{i}}}{k_{i}!\,m_{i}!}\eta^{k_{i}}\zeta^{m_{i}}\alpha_{1}^{\lambda_{i}\eta}\alpha_{2}^{\lambda_{i}\zeta}, |  |

for any i = 1, …, N i=1,\ldots,N, and

 | Φ ℐ ​ ( x) i, j = { ϕ i ​ ( x ​ η j, x ​ ζ j), if i ∈ ℐ, θ i, j ​ ϕ i ​ ( x ​ η j, x ​ ζ j), if i ∉ ℐ, \Phi_{\mathcal{I}}(x)_{i,j}=\begin{cases}\phi_{i}\left(x\eta_{j},x\zeta_{j}\right),&\text{if $i\in\mathcal{I}$,}\\ \theta_{i,j}\phi_{i}\left(x\eta_{j},x\zeta_{j}\right),&\text{if $i\not\in\mathcal{I}$,}\end{cases} |  |

for any subset ℐ \mathcal{I} of 𝒩 = { 1, …, N } \mathcal{N}=\{1,\ldots,N\} and j = 1, …, N j=1,\ldots,N.

In our notation before Lemma 3.6, here we put p i ​ ( z 1, z 2) = b 3 ′ k i ​ b 3 ′′ m i k i! ​ m i! ​ z 1 k i ​ z 2 m i p_{i}\left(z_{1},z_{2}\right)=\frac{{b_{3}^{\prime}}^{k_{i}}{b_{3}^{\prime\prime}}^{m_{i}}}{k_{i}!\,m_{i}!}z_{1}^{k_{i}}z_{2}^{m_{i}}, f i ​ ( z) = exp ⁡ ( λ i ​ z) f_{i}(z)=\exp\left(\lambda_{i}z\right) and θ i, j = δ i, j \theta_{i,j}=\delta_{i,j}. Hence we can write α 1 λ i ​ z 1 ​ α 2 λ i ​ z 2 = exp ⁡ ( λ i ​ ( log ⁡ ( α 1) ​ z 1 + log ⁡ ( α 2) ​ z 2)) = f i ​ ( θ 1 ​ z 1 + θ 2 ​ z 2) \alpha_{1}^{\lambda_{i}z_{1}}\alpha_{2}^{\lambda_{i}z_{2}}=\exp\left(\lambda_{i}\left(\log\left(\alpha_{1}\right)z_{1}+\log\left(\alpha_{2}\right)z_{2}\right)\right)=f_{i}\left(\theta_{1}z_{1}+\theta_{2}z_{2}\right) with θ 1 = log ⁡ ( α 1) \theta_{1}=\log\left(\alpha_{1}\right) and θ 2 = log ⁡ ( α 2) \theta_{2}=\log\left(\alpha_{2}\right).

We put ℳ ℐ = ( Φ ℐ ​ ( 1) i, j) \mathcal{M}_{\mathcal{I}}=\left(\Phi_{\mathcal{I}}(1)_{i,j}\right), Ψ ℐ ​ ( x) = det ( Φ ℐ ​ ( x) i, j) \Psi_{\mathcal{I}}(x)=\det\left(\Phi_{\mathcal{I}}(x)_{i,j}\right),

(3.8) |  | Δ ℐ = Ψ ℐ ​ ( 1) \Delta_{\mathcal{I}}=\Psi_{\mathcal{I}}(1) |  |

and

 | J ℐ = ord x = 0 ⁡ ( Ψ ℐ ​ ( x)). J_{\mathcal{I}}=\ord_{x=0}\left(\Psi_{\mathcal{I}}(x)\right). |  |

###### Proposition 3.7.

Suppose K K and L L are two integers satisfying K ≥ 3 K\geq 3 and L ≥ 5 L\geq 5. If

(3.9) |  | Λ ′ < ρ − K ​ L \Lambda^{\prime}<\rho^{-KL} |  |

holds for some real number ρ ≥ 2 \rho\geq 2, then

 | log ⁡ | Δ | < \displaystyle\log\left|\Delta\right|< | ∑ i = 1 3 M i ​ log ​ | α i | + ρ ​ ∑ i = 1 3 G i ​ | log ⁡ α i | + log ⁡ ( N!) + N ​ log ​ 2 + N ⁡ ( K − 1) 3 ​ log ​ b \displaystyle\sum_{i=1}^{3}M_{i}\log\left|\alpha_{i}\right|+\rho\sum_{i=1}^{3}G_{i}\left|\log\alpha_{i}\right|+\log(N!)+N\log 2+\frac{N(K-1)}{3}\log b |  |

 |  | − N 2 2 ​ K ​ ( 1 − 2 3 ​ L − 2 3 ​ K ​ L − 1 3 ​ L 2 − 16 3 ​ K 2 ​ L) ​ log ⁡ ρ + 0.001. \displaystyle-\frac{N^{2}}{2K}\left(1-\frac{2}{3L}-\frac{2}{3KL}-\frac{1}{3L^{2}}-\frac{16}{3K^{2}L}\right)\log\rho+0.001. |  |

###### Proof.

We start by proving that | θ i, j | ≤ 1 \left|\theta_{i,j}\right|\leq 1.

Since b 3 b_{3}, L L and | Λ | \left|\Lambda\right| are all positive, 0 ≤ t j ≤ T 0\leq t_{j}\leq T, and | λ i | ≤ L / 2 \left|\lambda_{i}\right|\leq L/2, we have

 | | θ i, j | ≤ e x − 1 x ​ e x ​ where ​ x = L ​ T ​ | Λ | 2 ​ b 3 > 0. \left|\theta_{i,j}\right|\leq\frac{e^{x}-1}{xe^{x}}\hskip 8.53581pt\text{ where }x=\frac{LT\left|\Lambda\right|}{2b_{3}}>0. |  |

Observe that ( e x − 1) / ( x ​ e x) \left(e^{x}-1\right)/\left(xe^{x}\right) is a decreasing function for x > 0 x>0, since its derivative is ( 1 + x − e x) / ( x 2 ​ e x) \left(1+x-e^{x}\right)/\left(x^{2}e^{x}\right). By L’Hôpital’s rule, we find that lim x → 0 + ( e x − 1) / ( x ​ e x) = lim x → 0 + ( 1 + x) − 1 = 1 \lim_{x\rightarrow 0^{+}}\left(e^{x}-1\right)/\left(xe^{x}\right)=\lim_{x\rightarrow 0^{+}}\left(1+x\right)^{-1}=1. Hence,

 | | θ i, j | ≤ 1. \left|\theta_{i,j}\right|\leq 1. |  |

Let

 | η j = r j + t j ​ β 1 − η 0 and ζ j = s j + t j ​ β 2 − ζ 0, \eta_{j}=r_{j}+t_{j}\beta_{1}-\eta_{0}\qquad\text{ and}\qquad\zeta_{j}=s_{j}+t_{j}\beta_{2}-\zeta_{0}, |  |

so | η j | ≤ η 0 \left|\eta_{j}\right|\leq\eta_{0} and | ζ j | ≤ ζ 0 \left|\zeta_{j}\right|\leq\zeta_{0}. Since,

 | ( r j ​ b 3 ′ + t j ​ b 1 ′ k i) = ( b 3 ′ ​ ( η j + η 0) k i) = b 3 ′ k i k i! ​ η j k i + terms in η j of degree less than k i, \binom{r_{j}b_{3}^{\prime}+t_{j}b_{1}^{\prime}}{k_{i}}=\binom{b_{3}^{\prime}\left(\eta_{j}+\eta_{0}\right)}{k_{i}}=\frac{{b_{3}^{\prime}}^{k_{i}}}{k_{i}!}{\eta_{j}}^{k_{i}}+\text{terms in $\eta_{j}$ of degree less than $k_{i}$}, |  |

and similarly for ( s j ​ b 3 ′′ + t j ​ b 2 ′′ m i) \binom{s_{j}b_{3}^{\prime\prime}+t_{j}b_{2}^{\prime\prime}}{m_{i}}, using the multilinearity of determinants we obtain the formula

 | Δ = det ( b 3 ′ k i ​ b 3 ′′ m i k i! ​ m i! ​ η j k i ​ ζ j m i ​ α 1 ℓ i ​ r j ​ α 2 ℓ i ​ s j ​ α 3 ℓ i ​ t j). \Delta=\det\left(\frac{{b_{3}^{\prime}}^{k_{i}}{b_{3}^{\prime\prime}}^{m_{i}}}{k_{i}!\,m_{i}!}{\eta_{j}}^{k_{i}}{\zeta_{j}}^{m_{i}}{\alpha_{1}}^{\ell_{i}r_{j}}{\alpha_{2}}^{\ell_{i}s_{j}}{\alpha_{3}}^{\ell_{i}t_{j}}\right). |  |

Combining this with ( 3.5), along with the definitions of λ i \lambda_{i}, M 1 M_{1}, M 2 M_{2} and M 3 M_{3}, it follows that

 | Δ = α 1 M 1 ​ α 2 M 2 ​ α 3 M 3 ​ det ( b 3 ′ k i ​ b 3 ′′ m i k i! ​ m i! ​ η j k i ​ ζ j m i ​ α 1 λ i ​ ( r j + t j ​ β 1) ​ α 2 λ i ​ ( s j + t j ​ β 2) ​ ( 1 + Λ ′ ​ θ i, j)). \Delta={\alpha_{1}}^{M_{1}}{\alpha_{2}}^{M_{2}}{\alpha_{3}}^{M_{3}}\det\left(\frac{{b_{3}^{\prime}}^{k_{i}}{b_{3}^{\prime\prime}}^{m_{i}}}{k_{i}!\,m_{i}!}\eta_{j}^{k_{i}}\zeta_{j}^{m_{i}}\alpha_{1}^{\lambda_{i}(r_{j}+t_{j}\beta_{1})}\alpha_{2}^{\lambda_{i}(s_{j}+t_{j}\beta_{2})}\left(1+\Lambda^{\prime}\theta_{i,j}\right)\right). |  |

Since ∑ i λ i = 0 \sum_{i}\lambda_{i}=0, we deduce from this and the definitions of η j \eta_{j} and ζ j \zeta_{j} that

 | Δ = α 1 M 1 ​ α 2 M 2 ​ α 3 M 3 ​ det ( b 3 ′ k i ​ b 3 ′′ m i k i! ​ m i! ​ η j k i ​ ζ j m i ​ α 1 λ i ​ η j ​ α 2 λ i ​ ζ j ​ ( 1 + Λ ′ ​ θ i, j)). \Delta=\alpha_{1}^{M_{1}}\alpha_{2}^{M_{2}}\alpha_{3}^{M_{3}}\det\left(\frac{{b_{3}^{\prime}}^{k_{i}}{b_{3}^{\prime\prime}}^{m_{i}}}{k_{i}!\,m_{i}!}{\eta_{j}}^{k_{i}}{\zeta_{j}}^{m_{i}}\alpha_{1}^{\lambda_{i}\eta_{j}}\alpha_{2}^{\lambda_{i}\zeta_{j}}\left(1+\Lambda^{\prime}\theta_{i,j}\right)\right). |  |

Expanding this determinant, we obtain

(3.10) |  | Δ = α 1 M 1 ​ α 2 M 2 ​ α 3 M 3 ​ ∑ ℐ ⊆ 𝒩 ( Λ ′) N − | ℐ | ​ Δ ℐ, \Delta={\alpha_{1}}^{M_{1}}{\alpha_{2}}^{M_{2}}{\alpha_{3}}^{M_{3}}\sum_{\mathcal{I}\subseteq\mathcal{N}}(\Lambda^{\prime})^{N-\left|\mathcal{I}\right|}\Delta_{\mathcal{I}}, |  |

where ℐ \mathcal{I} runs over all subsets of 𝒩 = { 1, …, N } \mathcal{N}=\{1,\ldots,N\} and Δ ℐ \Delta_{\mathcal{I}} is defined in ( 3.8).

From Schwarz’ Lemma (see, for example, Lemma 2.3 on page 37 of [31]), we have

(3.11) |  | | Ψ ℐ ​ ( 1) | ≤ ρ − J ℐ ⋅ max | x | = ρ ⁡ | Ψ ℐ ​ ( x) |, \left|\Psi_{\mathcal{I}}(1)\right|\leq\rho^{-J_{\mathcal{I}}}\cdot\max_{\left|x\right|=\rho}\left|\Psi_{\mathcal{I}}(x)\right|, |  |

recalling that J ℐ = ord x = 0 ⁡ ( Ψ ℐ ​ ( x)) J_{\mathcal{I}}=\ord_{x=0}\left(\Psi_{\mathcal{I}}(x)\right).

Since | θ i, j | ≤ 1 \left|\theta_{i,j}\right|\leq 1, expanding the determinant Ψ ℐ \Psi_{\mathcal{I}} shows that

 | | Ψ ℐ ​ ( x) | ≤ N! ​ max σ ∈ 𝔖 ⁡ ( 𝒩) ​ | ∏ i = 1 N ϕ i ​ ( x ​ η σ ⁡ ( i), x ​ ζ σ ⁡ ( i)) |, \left|\Psi_{\mathcal{I}}(x)\right|\leq N!\max_{\sigma\in\mathfrak{S}(\mathcal{N})}\left|\prod_{i=1}^{N}\phi_{i}\left(x\eta_{\sigma(i)},x\zeta_{\sigma(i)}\right)\right|, |  |

where 𝔖 ⁡ ( 𝒩) \mathfrak{S}(\mathcal{N}) is the group of all permutations of 𝒩 \mathcal{N}. For any σ ∈ 𝔖 ⁡ ( 𝒩) \sigma\in\mathfrak{S}(\mathcal{N}) and any x x satisfying | x | ≤ ρ |x|\leq\rho, we also have

 | | ∏ i = 1 N ϕ i ​ ( x ​ η σ ⁡ ( i), x ​ ζ σ ⁡ ( i)) | ≤ b 3 ′ ∑ k i ​ b 3 ′′ ∑ m i ∏ k i! ​ ∏ m i! ​ ( ρ ​ η 0) ∑ k i ​ ( ρ ​ ζ 0) ∑ m i ​ | α 1 ∑ λ i ​ η σ ⁡ ( i) ​ x | ⋅ | α 2 ∑ λ i ​ ζ σ ⁡ ( i) ​ x |, \left|\prod_{i=1}^{N}\phi_{i}\left(x\eta_{\sigma(i)},x\zeta_{\sigma(i)}\right)\right|\leq\frac{{b_{3}^{\prime}}^{\sum k_{i}}{b_{3}^{\prime\prime}}^{\sum m_{i}}}{\prod k_{i}!\,\prod m_{i}!}\left(\rho\eta_{0}\right)^{\sum k_{i}}\left(\rho\zeta_{0}\right)^{\sum m_{i}}\left|\alpha_{1}^{\sum\lambda_{i}\eta_{\sigma(i)}x}\right|\cdot\left|\alpha_{2}^{\sum\lambda_{i}\zeta_{\sigma(i)}x}\right|, |  |

since | η j | ≤ η 0 \left|\eta_{j}\right|\leq\eta_{0} and | ζ j | ≤ ζ 0 \left|\zeta_{j}\right|\leq\zeta_{0}.

Note that all the sums and products on right-hand side are for i = 1, …, N i=1,\ldots,N. This will also be the case for all sums and products that follow which have i i as the index, but without explicit lower and upper bounds on i i.

Since | exp ⁡ ( z) | ≤ exp ⁡ ( | z |) \left|\exp(z)\right|\leq\exp\left(\left|z\right|\right), it follows that

(3.12) |  | max | x | = ρ ⁡ | Ψ ℐ ​ ( x) | ≤ \displaystyle\max_{\left|x\right|=\rho}\left|\Psi_{\mathcal{I}}(x)\right|\leq | N! ​ b 3 ′ ∑ k i ​ b 3 ′′ ∑ m i ∏ k i! ​ ∏ m i! ​ ( ρ ​ η 0) ∑ k i ​ ( ρ ​ ζ 0) ∑ m i \displaystyle N!\frac{{b_{3}^{\prime}}^{\sum k_{i}}{b_{3}^{\prime\prime}}^{\sum m_{i}}}{\prod k_{i}!\,\prod m_{i}!}\left(\rho\eta_{0}\right)^{\sum k_{i}}\left(\rho\zeta_{0}\right)^{\sum m_{i}} |  |

 |  | × max σ ∈ 𝔖 ⁡ ( 𝒩) ⁡ exp ⁡ { ρ ⁡ ( | ∑ λ i ​ η σ ⁡ ( i) | ​ | log ⁡ α 1 | + | ∑ λ i ​ ζ σ ⁡ ( i) | ​ | log ⁡ α 2 |) }. \displaystyle\times\max_{\sigma\in\mathfrak{S}(\mathcal{N})}\exp\left\{\rho\left(\left|\sum\lambda_{i}\eta_{\sigma(i)}\right|\left|\log\alpha_{1}\right|+\left|\sum\lambda_{i}\zeta_{\sigma(i)}\right|\left|\log\alpha_{2}\right|\right)\right\}. |  |

Using the relation ∑ i = 1 N λ i = 0 \sum_{i=1}^{N}\lambda_{i}=0, we get

 | ∑ i = 1 N λ i ​ η σ ⁡ ( i) \displaystyle\sum_{i=1}^{N}\lambda_{i}\eta_{\sigma(i)} | = ∑ i = 1 N λ i ​ ( r σ ⁡ ( i) + t σ ⁡ ( i) ​ β 1) \displaystyle=\sum_{i=1}^{N}\lambda_{i}\left(r_{\sigma(i)}+t_{\sigma(i)}\beta_{1}\right) |  |

 |  | = ∑ i = 1 N ( ℓ i − L − 1 2) ​ r σ ⁡ ( i) + β 1 ​ ∑ i = 1 N ( ℓ i − L − 1 2) ​ t σ ⁡ ( i) \displaystyle=\sum_{i=1}^{N}\left(\ell_{i}-\frac{L-1}{2}\right)r_{\sigma(i)}+\beta_{1}\sum_{i=1}^{N}\left(\ell_{i}-\frac{L-1}{2}\right)t_{\sigma(i)} |  |

 |  | = ∑ i = 1 N ℓ i ​ r σ ⁡ ( i) − M 1 + β 1 ​ ∑ i = 1 N ℓ i ​ t σ ⁡ ( i) − β 1 ​ M 3. \displaystyle=\sum_{i=1}^{N}\ell_{i}r_{\sigma(i)}-M_{1}+\beta_{1}\sum_{i=1}^{N}\ell_{i}t_{\sigma(i)}-\beta_{1}M_{3}. |  |

Thus, from Lemma 3.2,

 | | ∑ i = 1 N λ i ​ η σ ⁡ ( i) | ≤ G 1 + β 1 ​ G 3. \left|\sum_{i=1}^{N}\lambda_{i}\eta_{\sigma(i)}\right|\leq G_{1}+\beta_{1}G_{3}. |  |

In a similar way,

 | | ∑ i = 1 N λ i ​ ζ σ ⁡ ( i) | ≤ G 2 + β 2 ​ G 3. \left|\sum_{i=1}^{N}\lambda_{i}\zeta_{\sigma(i)}\right|\leq G_{2}+\beta_{2}G_{3}. |  |

Recalling that b 3 ​ | log ⁡ α 3 | = b 1 ​ | log ⁡ α 1 | + b 2 ​ | log ⁡ α 2 | ± | Λ | b_{3}\left|\log\alpha_{3}\right|=b_{1}\left|\log\alpha_{1}\right|+b_{2}\left|\log\alpha_{2}\right|\pm\left|\Lambda\right|, it follows that

(3.13) |  |  | exp ⁡ { ρ ⁡ ( | ∑ λ i ​ η σ ⁡ ( i) | ​ | log ⁡ α 1 | + | ∑ λ i ​ ζ σ ⁡ ( i) | ​ | log ⁡ α 2 |) } \displaystyle\exp\left\{\rho\left(\left|\sum\lambda_{i}\eta_{\sigma(i)}\right|\left|\log\alpha_{1}\right|+\left|\sum\lambda_{i}\zeta_{\sigma(i)}\right|\left|\log\alpha_{2}\right|\right)\right\} |  |

 | ≤ \displaystyle\leq | exp ⁡ { ρ ⁡ ( ( G 1 + β 1 ​ G 3) ​ | log ⁡ α 1 | + ( G 2 + β 2 ​ G 3) ​ | log ⁡ α 2 |) } \displaystyle\exp\left\{\rho\left(\left(G_{1}+\beta_{1}G_{3}\right)\left|\log\alpha_{1}\right|+\left(G_{2}+\beta_{2}G_{3}\right)\left|\log\alpha_{2}\right|\right)\right\} |  |

 | ≤ \displaystyle\leq | exp ⁡ { ρ ⁡ ( G 1 ​ | log ⁡ α 1 | + G 2 ​ | log ⁡ α 2 | + G 3 ​ ( | log ⁡ α 3 | + | Λ | b 3)) }. \displaystyle\exp\left\{\rho\left(G_{1}\left|\log\alpha_{1}\right|+G_{2}\left|\log\alpha_{2}\right|+G_{3}\left(\left|\log\alpha_{3}\right|+\frac{\left|\Lambda\right|}{b_{3}}\right)\right)\right\}. |  |

Recalling ( 3.9) and applying the definitions for the quantities that arise, we have

 | ρ ​ G 3 ​ | Λ | b 3 \displaystyle\rho G_{3}\frac{\left|\Lambda\right|}{b_{3}} | = ρ ​ g ​ N ​ L ​ T b 3 ​ | Λ | 2 = ρ ​ g ​ K ​ ( K + 1) ​ L 2 ​ Λ ′ e L ​ T ​ | Λ | / ( 2 ​ b 3) ≤ ρ ​ g ​ K ​ ( K + 1) ​ L ​ Λ ′ 2 ≤ ρ ​ K ​ ( K + 1) ​ L ​ Λ ′ 8 \displaystyle=\rho g\frac{NLT}{b_{3}}\frac{\left|\Lambda\right|}{2}=\frac{\rho gK(K+1)L}{2}\frac{\Lambda^{\prime}}{e^{LT\left|\Lambda\right|/(2b_{3})}}\leq\frac{\rho gK(K+1)L\Lambda^{\prime}}{2}\leq\frac{\rho K(K+1)L\Lambda^{\prime}}{8} |  |

 |  | < ρ ​ K ​ ( K + 1) ​ L 8 ​ ρ K ​ L. \displaystyle<\frac{\rho K(K+1)L}{8\rho^{KL}}. |  |

By looking at the partial derivatives of this last expression with respect to ρ \rho, K K and L L, we see that it is a non-increasing function in each of these provided that K ​ L ​ log ⁡ ( ρ) ≥ 2 KL\log(\rho)\geq 2 and K ​ L ≥ 1 KL\geq 1. These conditions hold for K ≥ 3 K\geq 3, L ≥ 5 L\geq 5 and ρ ≥ 2 \rho\geq 2. For K = 3 K=3, L = 5 L=5 and ρ = 2 \rho=2, we find that ρ ​ K 2 ​ L / ( 4 ​ ρ K ​ L) < 0.0005 \rho K^{2}L/\left(4\rho^{KL}\right)<0.0005. Hence

(3.14) |  | ρ ​ G 3 ​ | Λ | b 3 < 0.001. \rho G_{3}\frac{\left|\Lambda\right|}{b_{3}}<0.001. |  |

Combining, ( 3.10), ( 3.11), ( 3.12), ( 3.13) and ( 3.14), we find that condition ( 3.9) implies the upper bound

 | log ⁡ | Δ | < \displaystyle\log\left|\Delta\right|< | ∑ i = 1 3 M i ​ log ⁡ | α i | + ρ ​ ∑ i = 1 3 G i ​ | log ⁡ α i | + log ⁡ ( N!) + N ​ log ⁡ ( 2) + log ⁡ ( ρ) ​ ∑ i ( k i + m i) \displaystyle\sum_{i=1}^{3}M_{i}\log\left|\alpha_{i}\right|+\rho\sum_{i=1}^{3}G_{i}\left|\log\alpha_{i}\right|+\log(N!)+N\log(2)+\log(\rho)\sum_{i}\left(k_{i}+m_{i}\right) |  |

 |  | + log ⁡ ( ( b 3 ′ ​ η 0) ∑ k i ∏ k i! ​ ( b 3 ′′ ​ ζ 0) ∑ m i ∏ m i! ​ max ℐ ⊆ 𝒩 ​ | Λ ′ | N − | ℐ | ρ J ℐ) + 0.001. \displaystyle+\log\left(\frac{\left(b_{3}^{\prime}\eta_{0}\right)^{\sum k_{i}}}{\prod k_{i}!}\frac{\left(b_{3}^{\prime\prime}\zeta_{0}\right)^{\sum m_{i}}}{\prod m_{i}!}\max_{\mathcal{I}\subseteq\mathcal{N}}\frac{|\Lambda^{\prime}|^{N-|\mathcal{I}|}}{\rho^{J_{\mathcal{I}}}}\right)+0.001. |  |

Under condition ( 3.9), we have

(3.15) |  | | Λ ′ | N − | ℐ | ρ J ℐ ≤ ρ − K ​ L ​ ( N − | ℐ |) − J ℐ \frac{|\Lambda^{\prime}|^{N-|\mathcal{I}|}}{\rho^{J_{\mathcal{I}}}}\leq\rho^{-KL(N-|\mathcal{I}|)-J_{\mathcal{I}}} |  |

(note that if N = | ℐ | N=|\mathcal{I}|, then we need ≤ \leq here, rather than the < < in ( 3.9)).

From Lemma 3.6, we obtain J ℐ ≥ Θ ⁡ ( K − 1, | ℐ |) J_{\mathcal{I}}\geq\Theta\left(K-1,\left|\mathcal{I}\right|\right). Note that our matrix is not of exactly the same form as used in Lemma 3.6, as we have functions in the entries, Ψ ℐ ​ ( x) i, j \Psi_{\mathcal{I}}(x)_{i,j} when i ∉ ℐ i\not\in\mathcal{I}, rather than complex numbers. But since the ϕ i \phi_{i} ’s are the product of polynomials and analytic functions we can write them as power series (some possibly truncated). Since Ψ ℐ ​ ( x) \Psi_{\mathcal{I}}(x) is a determinant, it is multilinear, these entries cannot reduce J ℐ J_{\mathcal{I}} (see the proof of Lemma 7.2 of [31] for more details).

So applying equation ( 3.15), Lemma 3.4 and using the relations

 | ∑ i = 1 N ( k i + m i) \displaystyle\sum_{i=1}^{N}\left(k_{i}+m_{i}\right) | = L ​ ∑ k = 0 K − 1 ( ∑ m = 0 K − 1 − k k + m) = L ​ ∑ k = 0 K − 1 ( K − 1 + k) ​ ( K − k) 2 = K ​ L ​ ( K + 1) ​ ( K − 1) 3 \displaystyle=L\sum_{k=0}^{K-1}\left(\sum_{m=0}^{K-1-k}k+m\right)=L\sum_{k=0}^{K-1}\frac{(K-1+k)(K-k)}{2}=\frac{KL(K+1)(K-1)}{3} |  |

 |  | = 2 ​ N ​ ( K − 1) 3, \displaystyle=\frac{2N(K-1)}{3}, |  |

we obtain

 |  | log ⁡ ( ρ) ​ ∑ i ( k i + m i) + log ⁡ ( max ℐ ⊆ 𝒩 ⁡ | Λ ′ | N − | ℐ | ρ J ℐ) \displaystyle\log(\rho)\sum_{i}\left(k_{i}+m_{i}\right)+\log\left(\max_{\mathcal{I}\subseteq\mathcal{N}}\frac{|\Lambda^{\prime}|^{N-|\mathcal{I}|}}{\rho^{J_{\mathcal{I}}}}\right) |  |

 |  | ≤ log ⁡ ( ρ) ​ ( 2 ​ N ​ ( K − 1) 3 − K ​ L ​ ( N − | ℐ |) − J ℐ) \displaystyle\leq\log(\rho)\left(\frac{2N(K-1)}{3}-KL(N-|\mathcal{I}|)-J_{\mathcal{I}}\right) |  |

 |  | ≤ log ⁡ ( ρ) ​ ( 2 ​ N ​ ( K − 1) 3 − K ​ L ​ ( N − | ℐ |) − Θ ⁡ ( K − 1, | ℐ |)) \displaystyle\leq\log(\rho)\left(\frac{2N(K-1)}{3}-KL(N-|\mathcal{I}|)-\Theta\left(K-1,\left|\mathcal{I}\right|\right)\right) |  |

 |  | ≤ log ⁡ ( ρ) ​ ( 2 ​ N ​ ( K − 1) 3 − N 2 2 ​ K ​ ( 1 + 2 L − 6 K ​ L − 1 3 ​ L 2)) \displaystyle\leq\log(\rho)\left(\frac{2N(K-1)}{3}-\frac{N^{2}}{2K}\left(1+\frac{2}{L}-\frac{6}{KL}-\frac{1}{3L^{2}}\right)\right) |  |

 |  | = − log ⁡ ( ρ) ​ N 2 2 ​ K ​ ( 1 − 2 3 ​ L − 2 3 ​ K ​ L − 1 3 ​ L 2 − 16 3 ​ K 2 ​ L). \displaystyle=-\log(\rho)\frac{N^{2}}{2K}\left(1-\frac{2}{3L}-\frac{2}{3KL}-\frac{1}{3L^{2}}-\frac{16}{3K^{2}L}\right). |  |

Also note that

(3.16) |  | ∑ i = 1 N k i = L ​ ∑ k = 0 K − 1 ( K − k) ​ k = K ​ ( K − 1) ​ ( K + 1) ​ L 6 = N ⁡ ( K − 1) 3. \sum_{i=1}^{N}k_{i}=L\sum_{k=0}^{K-1}(K-k)k=\frac{K(K-1)(K+1)L}{6}=\frac{N(K-1)}{3}. |  |

So using the definition of b b in ( 2.5), we see that

 | b N ⁡ ( K − 1) / 3 \displaystyle b^{N(K-1)/3} | = ( b 3 ′ ​ η 0) N ⁡ ( K − 1) / 3 ​ ( b 3 ′′ ​ ζ 0) N ⁡ ( K − 1) / 3 ​ ( ∏ k = 1 K − 1 ( k!) K − k) − 2 ​ L \displaystyle=\left(b_{3}^{\prime}\eta_{0}\right)^{N(K-1)/3}\left(b_{3}^{\prime\prime}\zeta_{0}\right)^{N(K-1)/3}\left(\prod_{k=1}^{K-1}(k!)^{K-k}\right)^{-2L} |  |

 |  | = ( b 3 ′ ​ η 0) ∑ k i ∏ k i! ​ ( b 3 ′′ ​ ζ 0) ∑ m i ∏ m i!. \displaystyle=\frac{\left(b_{3}^{\prime}\eta_{0}\right)^{\sum k_{i}}}{\prod k_{i}!}\frac{\left(b_{3}^{\prime\prime}\zeta_{0}\right)^{\sum m_{i}}}{\prod m_{i}!}. |  |

This completes the proof of the proposition. ∎

### 3.4. A lower bound for | Δ | \left|\Delta\right|

Liouville’s inequality is the key tool that we need to obtain a lower bound for | Δ | \left|\Delta\right|. The version of Liouville inequality that we use is the same as in [20] (p. 298–299) (also see Exercises 3.3(a) and 3.5 on pages 106–107 of [31]).

###### Lemma 3.8.

Let α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} be non-zero algebraic numbers and a polynomial f ∈ ℤ ⁡ [X 1, X 2, X 3] f\in\mathbb{Z}\left[X_{1},X_{2},X_{3}\right] such that f ⁡ ( α 1, α 2, α 3) ≠ 0 f\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\neq 0, then

 | | f ⁡ ( α 1, α 2, α 3) | ≥ | f | − 𝒟 + 1 ​ ( α 1 ∗) d 1 ​ ( α 2 ∗) d 2 ​ ( α 3 ∗) d 3 × exp ⁡ { − 𝒟 ⁡ ( d 1 ​ h ⁡ ( α 1) + d 2 ​ h ⁡ ( α 2) + d 3 ​ h ⁡ ( α 3)) }, \left|f\left(\alpha_{1},\alpha_{2},\alpha_{3}\right)\right|\geq|f|^{-{\mathcal{D}+1}}\left(\alpha_{1}^{*}\right)^{d_{1}}\left(\alpha_{2}^{*}\right)^{d_{2}}\left(\alpha_{3}^{*}\right)^{d_{3}}\times\exp\left\{-\mathcal{D}\left(d_{1}\h\left(\alpha_{1}\right)+d_{2}\h\left(\alpha_{2}\right)+d_{3}\h\left(\alpha_{3}\right)\right)\right\}, |  |

where 𝒟 = [ℚ ( α 1, α 2, α 3): ℚ] / [ℝ ( α 1, α 2, α 3): ℝ] \mathcal{D}=\left[\mathbb{Q}\left(\alpha_{1},\alpha_{2},\alpha_{3}\right):\mathbb{Q}\right]\bigm/\left[\mathbb{R}\left(\alpha_{1},\alpha_{2},\alpha_{3}\right):\mathbb{R}\right],

 | d i = deg X i f, i = 1, 2, 3, | f | = max { | f ( z 1, z 2, z 3) |: | z i | ≤ 1, i = 1, 2, 3 }, d_{i}=\deg_{X_{i}}f,\ \ i=1,2,3,\qquad\left|f\right|=\max\left\{\left|f\left(z_{1},z_{2},z_{3}\right)\right|:\left|z_{i}\right|\leq 1,\ i=1,2,3\right\}, |  |

and h ⁡ ( α) \h(\alpha) is the absolute logarithmic height of the algebraic number α \alpha, and α ∗ = max ⁡ { 1, | α | } \alpha^{*}=\max\{1,\left|\alpha\right|\}.

Using Lemma 3.8, we get the following lemma – also see Proposition 12.6 in [9].

###### Proposition 3.9.

If Δ ≠ 0 \Delta\neq 0, then

 | log ⁡ | Δ | ≥ \displaystyle\log\left|\Delta\right|\geq | − 𝒟 − 1 2 ​ N ​ log ⁡ ( N) + ∑ i = 1 3 ( M i + G i) ​ log ⁡ | α i | − 2 ​ 𝒟 ​ ∑ i = 1 3 G i ​ h ⁡ ( α i) \displaystyle-\frac{\mathcal{D}-1}{2}N\log(N)+\sum_{i=1}^{3}\left(M_{i}+G_{i}\right)\log\left|\alpha_{i}\right|-2\mathcal{D}\sum_{i=1}^{3}G_{i}\h\left(\alpha_{i}\right) |  |

 |  | − 𝒟 − 1 3 ​ ( K − 1) ​ N ​ log ⁡ ( b). \displaystyle-\frac{\mathcal{D}-1}{3}(K-1)N\log(b). |  |

###### Proof.

From ( 2.6), we have Δ = P ⁡ ( α 1, α 2, α 3) \Delta=P\left(\alpha_{1},\alpha_{2},\alpha_{3}\right) where P ∈ ℤ ⁡ [X 1, X 2, X 3] P\in\mathbb{Z}\left[X_{1},X_{2},X_{3}\right] is given by

 | P ⁡ ( X 1, X 2, X 3) = ∑ σ ∈ 𝔖 N sg ⁡ ( σ) ​ ( ∏ i = 1 N ( r σ ⁡ ( i) ​ b 3 ′ + t σ ⁡ ( i) ​ b 1 ′ k i) ​ ( s σ ⁡ ( i) ​ b 3 ′′ + t σ ⁡ ( i) ​ b 2 ′′ m i)) ​ X 1 n r, σ ​ X 2 n s, σ ​ X 3 n t, σ, P\left(X_{1},X_{2},X_{3}\right)=\sum_{\sigma\in\mathfrak{S}_{N}}{\rm sg}(\sigma)\left(\prod_{i=1}^{N}\binom{r_{\sigma(i)}b_{3}^{\prime}+t_{\sigma(i)}b_{1}^{\prime}}{k_{i}}\binom{s_{\sigma(i)}b_{3}^{\prime\prime}+t_{\sigma(i)}b_{2}^{\prime\prime}}{m_{i}}\right)X_{1}^{n_{r,\sigma}}X_{2}^{n_{s,\sigma}}X_{3}^{n_{t,\sigma}}, |  |

where sg ⁡ ( σ) {\rm sg}(\sigma) is the signature of the permutation, σ \sigma,

 | n r, σ = ∑ i = 1 N ℓ i r σ ⁡ ( i), n s, σ = ∑ i = 1 N ℓ i s σ ⁡ ( i) and n t, σ = ∑ i = 1 N ℓ i t σ ⁡ ( i). n_{r,\sigma}=\sum_{i=1}^{N}\ell_{i}r_{\sigma(i)},\quad n_{s,\sigma}=\sum_{i=1}^{N}\ell_{i}s_{\sigma(i)}\quad\text{ and }\quad n_{t,\sigma}=\sum_{i=1}^{N}\ell_{i}t_{\sigma(i)}. |  |

By Lemma 3.2,

 | | deg X i ⁡ P − M i | ≤ G i, for i = 1, 2, 3. \left|\deg_{X_{i}}P-M_{i}\right|\leq G_{i},\quad\text{for $i=1,2,3$.} |  |

Let

 | V i = ⌊ M i + G i ⌋, U i = ⌈ M i − G i ⌉, i = 1, 2, 3, V_{i}=\lfloor M_{i}+G_{i}\rfloor,\qquad U_{i}=\lceil M_{i}-G_{i}\rceil,\quad\text{$i=1,2,3$,} |  |

then

 | Δ = α 1 V 1 ​ α 2 V 2 ​ α 3 V 3 ​ P ~ ​ ( α 1 − 1, α 2 − 1, α 3 − 1), \Delta=\alpha_{1}^{V_{1}}\alpha_{2}^{V_{2}}\alpha_{3}^{V_{3}}\widetilde{P}\left(\alpha_{1}^{-1},\alpha_{2}^{-1},\alpha_{3}^{-1}\right), |  |

where

 | deg X i ⁡ P ~ ≤ V i − U i, i = 1, 2, 3. \deg_{X_{i}}\widetilde{P}\leq V_{i}-U_{i},\quad\text{$i=1,2,3$.} |  |

By our Liouville estimate

 | log ⁡ | P ~ ​ ( α 1 − 1, α 2 − 1, α 3 − 1) | ≥ − ( 𝒟 − 1) ​ log ⁡ | P ~ | − 𝒟 ​ ∑ i = 1 3 ( V i − U i) ​ h ⁡ ( α i), \log\left|\widetilde{P}\left(\alpha_{1}^{-1},\alpha_{2}^{-1},\alpha_{3}^{-1}\right)\right|\geq-(\mathcal{D}-1)\log\left|\widetilde{P}\right|-\mathcal{D}\sum_{i=1}^{3}\left(V_{i}-U_{i}\right)\h\left(\alpha_{i}\right), |  |

recalling from our assumptions at the start of Section 2 that | α i | ≥ 1 \left|\alpha_{i}\right|\geq 1, and hence ( α i − 1) ∗ = 1 \left(\alpha_{i}^{-1}\right)^{*}=1, for i = 1, 2, 3 i=1,2,3.

Now we have to find an upper bound for | P ~ | \left|\widetilde{P}\right| (or for | P | |P|, which is equal to | P ~ | \left|\widetilde{P}\right|). By the multilinearity of the determinant, for all η \eta, ζ ∈ ℂ \zeta\in\mathbb{C},

 | P ⁡ ( z 1, z 2, z 3) = det ( ( r j ​ b 3 ′ + t j ​ b 1 ′ − η) k i k i! ​ ( s j ​ b 3 ′′ + t j ​ b 2 ′′ − ζ) m i m i! ​ z 1 ℓ i ​ r j ​ z 2 ℓ i ​ s j ​ z 3 ℓ i ​ t j). P\left(z_{1},z_{2},z_{3}\right)=\det\left(\frac{\left(r_{j}b_{3}^{\prime}+t_{j}b_{1}^{\prime}-\eta\right)^{k_{i}}}{k_{i}!}\frac{\left(s_{j}b_{3}^{\prime\prime}+t_{j}b_{2}^{\prime\prime}-\zeta\right)^{m_{i}}}{m_{i}!}z_{1}^{\ell_{i}r_{j}}z_{2}^{\ell_{i}s_{j}}z_{3}^{\ell_{i}t_{j}}\right). |  |

Choose

 | η = ( R − 1) ​ b 3 ′ + ( T − 1) ​ b 1 ′ 2, ζ = ( S − 1) ​ b 3 ′′ + ( T − 1) ​ b 2 ′′ 2. \eta=\frac{(R-1)b_{3}^{\prime}+(T-1)b_{1}^{\prime}}{2},\quad\zeta=\frac{(S-1)b_{3}^{\prime\prime}+(T-1)b_{2}^{\prime\prime}}{2}. |  |

Notice that, for 1 ≤ j ≤ N 1\leq j\leq N,

 | | r j ​ b 3 ′ + t j ​ b 1 ′ − η | k i ≤ ( ( R − 1) ​ b 3 + ( T − 1) ​ b 1 2 ​ d 1) k i, | s j ​ b 3 ′′ + t j ​ b 2 ′′ − ζ | k i ≤ ( ( S − 1) ​ b 3 + ( T − 1) ​ b 2 2 ​ d 2) m i \left|r_{j}b_{3}^{\prime}+t_{j}b_{1}^{\prime}-\eta\right|^{k_{i}}\leq\left(\frac{(R-1)b_{3}+(T-1)b_{1}}{2d_{1}}\right)^{k_{i}}\!\!,\quad\left|s_{j}b_{3}^{\prime\prime}+t_{j}b_{2}^{\prime\prime}-\zeta\right|^{k_{i}}\leq\left(\frac{(S-1)b_{3}+(T-1)b_{2}}{2d_{2}}\right)^{m_{i}} |  |

and recall from ( 3.16) that

 | ∑ i = 1 N k i = ∑ i = 1 N m i = N ⁡ ( K − 1) 3. \sum_{i=1}^{N}k_{i}=\sum_{i=1}^{N}m_{i}=\frac{N(K-1)}{3}. |  |

So Hadamard’s inequality implies

 | | P | ≤ \displaystyle|P|\leq | N N / 2 ​ ( ( R − 1) ​ b 3 + ( T − 1) ​ b 1 2 ​ d 1) ( K − 1) ​ N / 3 ​ ( ( S − 1) ​ b 3 + ( T − 1) ​ b 2 2 ​ d 2) ( K − 1) ​ N / 3 \displaystyle N^{N/2}\left(\frac{(R-1)b_{3}+(T-1)b_{1}}{2d_{1}}\right)^{(K-1)N/3}\left(\frac{(S-1)b_{3}+(T-1)b_{2}}{2d_{2}}\right)^{(K-1)N/3} |  |

 |  | × ( ∏ i = 1 N k i!) − 1 ​ ( ∏ i = 1 N m i!) − 1. \displaystyle\times\left(\prod_{i=1}^{N}k_{i}!\right)^{-1}\left(\prod_{i=1}^{N}m_{i}!\right)^{-1}. |  |

Recalling the definition of b b, we get

 | | P | ≤ N N / 2 ​ b ( K − 1) ​ N / 3. |P|\leq N^{N/2}b^{(K-1)N/3}. |  |

Collecting all the above estimates, we find

 | log ⁡ | Δ | ≥ − ( 𝒟 − 1) ​ ( log ⁡ ( N N / 2) + ( K − 1) ​ N 3 ​ log ​ b) − 𝒟 ​ ∑ i = 1 3 ( V i − U i) ​ h ⁡ ( α i) + ∑ i = 1 3 V i ​ log ​ | α i |. \log\left|\Delta\right|\geq-(\mathcal{D}-1)\left(\log\left(N^{N/2}\right)+\frac{(K-1)N}{3}\log b\right)-\mathcal{D}\sum_{i=1}^{3}\left(V_{i}-U_{i}\right)\h\left(\alpha_{i}\right)+\sum_{i=1}^{3}V_{i}\log\left|\alpha_{i}\right|. |  |

The inequalities 𝒟 ​ h ⁡ ( α i) ≥ log ⁡ | α i | ≥ 0 \mathcal{D}\h\left(\alpha_{i}\right)\geq\log\left|\alpha_{i}\right|\geq 0 imply

 | V i ​ log ⁡ | α i | − 𝒟 ⁡ ( V i − U i) ​ h ⁡ ( α i) ≥ ( M i + G i) ​ log ⁡ | α i | − 2 ​ 𝒟 ​ G i ​ h ⁡ ( α i) V_{i}\log\left|\alpha_{i}\right|-\mathcal{D}\left(V_{i}-U_{i}\right)\h\left(\alpha_{i}\right)\geq\left(M_{i}+G_{i}\right)\log\left|\alpha_{i}\right|-2\mathcal{D}G_{i}\h\left(\alpha_{i}\right) |  |

and the result follows. ∎

### 3.5. Synthesis

Here we combine the upper and lower bounds for | Δ | \left|\Delta\right| that we obtained in the two previous subsections.

###### Proposition 3.10.

With the previous notation, if K ≥ 3 K\geq 3, L ≥ 5 L\geq 5, ρ ≥ 2 \rho\geq 2, and if Δ ≠ 0 \Delta\neq 0 then

 | Λ ′ ≥ ρ − K ​ L \Lambda^{\prime}\geq\rho^{-KL} |  |

provided that

 | ( K ​ L 2 + L 2 − 0.37 ​ K − 2) ​ log ⁡ ρ ≥ ( 𝒟 + 1) ​ log ⁡ N + g ​ L ​ ( a 1 ​ R + a 2 ​ S + a 3 ​ T) + 2 ​ 𝒟 ​ ( K − 1) 3 ​ log ⁡ b, \left(\frac{KL}{2}+\frac{L}{2}-0.37K-2\right)\log\rho\geq(\mathcal{D}+1)\log N+gL\left(a_{1}R+a_{2}S+a_{3}T\right)+\frac{2\mathcal{D}(K-1)}{3}\log b, |  |

where the a i a_{i} are positive real numbers which satisfy

 | a i ≥ ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i) for i = 1, 2, 3. a_{i}\geq\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right)\qquad\text{for $i=1,2,3$.} |  |

###### Proof.

Under the hypotheses of the Propositions 3.7 and 3.9 (which include the hypothesis that Λ ′ < ρ − K ​ L \Lambda^{\prime}<\rho^{-KL} from ( 3.9)), we get

 |  | − 𝒟 − 1 2 ​ N ​ log ⁡ ( N) + ∑ i = 1 3 ( M i + G i) ​ log ⁡ | α i | − 2 ​ 𝒟 ​ ∑ i = 1 3 G i ​ h ⁡ ( α i) − 𝒟 − 1 3 ​ ( K − 1) ​ N ​ log ⁡ ( b) \displaystyle-\frac{\mathcal{D}-1}{2}N\log(N)+\sum_{i=1}^{3}\left(M_{i}+G_{i}\right)\log\left|\alpha_{i}\right|-2\mathcal{D}\sum_{i=1}^{3}G_{i}\h\left(\alpha_{i}\right)-\frac{\mathcal{D}-1}{3}(K-1)N\log(b) |  |

 | < \displaystyle< | ∑ i = 1 3 M i ​ log ​ | α i | + ρ ​ ∑ i = 1 3 G i ​ | log ⁡ α i | + log ⁡ ( N!) + N ​ log ​ 2 + N 3 ​ ( K − 1) ​ log ​ b \displaystyle\sum_{i=1}^{3}M_{i}\log\left|\alpha_{i}\right|+\rho\sum_{i=1}^{3}G_{i}\left|\log\alpha_{i}\right|+\log(N!)+N\log 2+\frac{N}{3}(K-1)\log b |  |

 |  | − N 2 2 ​ K ​ ( 1 − 2 3 ​ L − 2 3 ​ K ​ L − 1 3 ​ L 2 − 16 3 ​ K 2 ​ L) ​ log ⁡ ρ + 0.001. \displaystyle-\frac{N^{2}}{2K}\left(1-\frac{2}{3L}-\frac{2}{3KL}-\frac{1}{3L^{2}}-\frac{16}{3K^{2}L}\right)\log\rho+0.001. |  |

After combining like terms, we obtain

 |  | N 2 2 ​ K ​ ( 1 − 2 3 ​ L − 2 3 ​ K ​ L − 1 3 ​ L 2 − 16 3 ​ K 2 ​ L) ​ log ⁡ ρ \displaystyle\frac{N^{2}}{2K}\left(1-\frac{2}{3L}-\frac{2}{3KL}-\frac{1}{3L^{2}}-\frac{16}{3K^{2}L}\right)\log\rho |  |

 | < \displaystyle< | 𝒟 − 1 2 ​ N ​ log ⁡ N + ∑ i = 1 3 G i ​ ( ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i)) + log ⁡ ( N!) + N ​ log ⁡ ( 2) + K − 1 3 ​ 𝒟 ​ N ​ log ⁡ ( b) + 0.001. \displaystyle\frac{\mathcal{D}-1}{2}N\log N+\sum_{i=1}^{3}G_{i}\left(\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right)\right)+\log(N!)+N\log(2)+\frac{K-1}{3}\mathcal{D}N\log(b)+0.001. |  |

Applying N! < N ​ ( N / e) N N!<N(N/e)^{N} (which holds for N ≥ 7 N\geq 7), then dividing both sides by N / 2 N/2, it follows that

 |  | ( K ​ L 2 + L 2 − ( 1 3 + 1 6 ​ L) ​ K − 2 3 − 3 K − 1 6 ​ L − 8 3 ​ K 2) ​ log ⁡ ρ \displaystyle\left(\frac{KL}{2}+\frac{L}{2}-\left(\frac{1}{3}+\frac{1}{6L}\right)K-\frac{2}{3}-\frac{3}{K}-\frac{1}{6L}-\frac{8}{3K^{2}}\right)\log\rho |  |

 | < \displaystyle< | ( 𝒟 + 1) ​ log ⁡ N + ( 2 / N) ​ ∑ i = 1 3 G i ​ ( ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i)) + 2 ​ log ⁡ ( N) N − 2 ​ log ⁡ ( e / 2) \displaystyle(\mathcal{D}+1)\log N+(2/N)\sum_{i=1}^{3}G_{i}\left(\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right)\right)+\frac{2\log(N)}{N}-2\log(e/2) |  |

 |  | + 2 ​ ( K − 1) ​ 𝒟 3 ​ log ⁡ ( b) + 0.002 / N. \displaystyle+\frac{2(K-1)\mathcal{D}}{3}\log(b)+0.002/N. |  |

For K ≥ 3 K\geq 3 and L ≥ 5 L\geq 5, we have 1 / 3 + 1 / ( 6 ​ L) = 0.366 ​ … 1/3+1/(6L)=0.366\ldots and 2 / 3 + 3 / K + 1 / ( 6 ​ L) + 8 / ( 3 ​ K 2) = 1.9962 ​ … 2/3+3/K+1/(6L)+8/\left(3K^{2}\right)=1.9962\ldots, we have

 | ( K ​ L 2 + L 2 − 0.37 ​ K − 2) ​ log ⁡ ρ < \displaystyle\left(\frac{KL}{2}+\frac{L}{2}-0.37K-2\right)\log\rho< | ( 𝒟 + 1) ​ log ⁡ N + ( 2 / N) ​ ∑ i = 1 3 G i ​ ( ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i)) \displaystyle(\mathcal{D}+1)\log N+(2/N)\sum_{i=1}^{3}G_{i}\left(\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right)\right) |  |

 |  | + 2 ​ log ⁡ ( N) N − 2 ​ log ⁡ ( e / 2) + 2 ​ ( K − 1) ​ 𝒟 3 ​ log ⁡ ( b) + 0.002 / N. \displaystyle+\frac{2\log(N)}{N}-2\log(e/2)+\frac{2(K-1)\mathcal{D}}{3}\log(b)+0.002/N. |  |

The proof now follows from 2 ​ log ⁡ ( N) / N − 2 ​ log ⁡ ( e / 2) + 0.002 / N < 0 2\log(N)/N-2\log(e/2)+0.002/N<0 for N ≥ 6 N\geq 6 and the definitions of the G i G_{i} ’s in ( 2.2) and applying the contrapositive to show that the assumption that Λ ′ < p − K ​ L \Lambda^{\prime}<p^{-KL} does not hold. ∎

### 3.6. A zero lemma

To use Proposition 3.9, we need to find conditions under which our determinant Δ \Delta is non-zero, a so-called zero lemma. We use a zero lemma due to N. Gouillon (see [14, Théorème 2.1], which is a refinement of Théorème 1 of [13]. In fact, in our formulation below, we state Gouillon’s result not just for ℂ \mathbb{C}, as he does, but for any algebraically closed field of characteristic zero – there are no changes required to his proof. Also Gouillon’s result applies to multiplicities. We ignore multiplicities of the zeroes here.

Let 𝕂 \mathbb{K} be an algebraically closed field of characteristic zero and let d 0 d_{0} and d 1 d_{1} be two non-negative integers which are not both zero. We denote by G G the group 𝕂 d 0 × ( 𝕂 ×) d 1 \mathbb{K}^{d_{0}}\times\left(\mathbb{K}^{\times}\right)^{d_{1}} The group law on G G will be written additively, hence its neutral element is denoted by 𝟎 G {\mathbf{0}}_{G}. When Σ 1, …, Σ n \Sigma_{1},\ldots,\Sigma_{n} are finite subsets of G G, we define

 | Σ 1 + ⋯ + Σ n = { σ 1 + ⋯ + σ n: σ 1 ∈ Σ 1, …, σ n ∈ Σ n }. \Sigma_{1}+\cdots+\Sigma_{n}=\left\{\sigma_{1}+\cdots+\sigma_{n}:\sigma_{1}\in\Sigma_{1},\ldots,\sigma_{n}\in\Sigma_{n}\right\}. |  |

###### Proposition 3.11.

Suppose that K K and L L are positive integers and that Σ 1 \Sigma_{1}, Σ 2 \Sigma_{2} and Σ 3 \Sigma_{3} are non-empty finite subsets of 𝕂 2 × 𝕂 × \mathbb{K}^{2}\times\mathbb{K}^{\times} such that

(3.17) |  | { Card ⁡ { λ ​ x 1 + μ ​ x 2: ∃ y ∈ 𝕂 × with ( x 1, x 2, y) ∈ Σ 1 } > K, ∀ ( λ, μ) ∈ 𝕂 2 ∖ { ( 0, 0) }, Card ⁡ { y: ∃ ( x 1, x 2) ∈ 𝕂 2 with ( x 1, x 2, y) ∈ Σ 1 } > L, \begin{cases}\card\left\{\lambda x_{1}+\mu x_{2}:\text{$\exists y\in\mathbb{K}^{\times}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{1}$}\right\}&>K,\quad\forall(\lambda,\mu)\in\mathbb{K}^{2}\setminus\{(0,0)\},\\ \card\left\{y:\text{$\exists\left(x_{1},x_{2}\right)\in\mathbb{K}^{2}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{1}$}\right\}&>L,\end{cases} |  |

(3.18) |  | { Card ⁡ { ( λ ​ x 1 + μ ​ x 2, y): ( x 1, x 2, y) ∈ Σ 2 } > 2 K L, ∀ ( λ, μ) ∈ 𝕂 2 ∖ { ( 0, 0) }, Card ⁡ { ( x 1, x 2): ∃ y ∈ 𝕂 × with ( x 1, x 2, y) ∈ Σ 2 } > K 2, \begin{cases}\card\left\{\left(\lambda x_{1}+\mu x_{2},y\right):\left(x_{1},x_{2},y\right)\in\Sigma_{2}\right\}&>2KL,\quad\forall(\lambda,\mu)\in\mathbb{K}^{2}\setminus\{(0,0)\},\\ \card\left\{\left(x_{1},x_{2}\right):\text{$\exists y\in\mathbb{K}^{\times}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{2}$}\right\}&>K^{2},\end{cases} |  |

and

(3.19) |  | Card ⁡ ( Σ 3) > 3 ​ K 2 ​ L. \card\left(\Sigma_{3}\right)>3K^{2}L. |  |

Then the only polynomial P ∈ 𝕂 ⁡ [X 1, X 2, Y] P\in\mathbb{K}\left[X_{1},X_{2},Y\right] of total degree at most K K in X 1 X_{1} and X 2 X_{2} and of degree at most L L in Y Y which is zero on the set Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3} is the zero polynomial.

The proof of this proposition is based on the following generalisation of a special case of a result due to Gouillon.

###### Lemma 3.12.

Let K K and L L be positive integers, 𝕂 \mathbb{K} be an algebraically closed field of characteristic zero and Σ 1, Σ 2, Σ 3 \Sigma_{1},\Sigma_{2},\Sigma_{3} be non-empty finite subsets of 𝕂 2 × 𝕂 × \mathbb{K}^{2}\times\mathbb{K}^{\times}.

Suppose that the following conditions are satisfied.

(1) For j = 1 j=1 and j = 2 j=2 and for all 𝕂 \mathbb{K} -subspaces, W W, of 𝕂 2 \mathbb{K}^{2} of dimension at most 2 − j 2-j, we have

 | Card ⁡ ( Σ j + ( W × 𝕂 ×) W × 𝕂 ×) > K j. \card\left(\frac{\Sigma_{j}+\left(W\times\mathbb{K}^{\times}\right)}{W\times\mathbb{K}^{\times}}\right)>K^{j}. |  |

(2) For each of j = 1 j=1, j = 2 j=2 and j = 3 j=3 and for all 𝕂 \mathbb{K} -subspaces, W W, of 𝕂 2 \mathbb{K}^{2} of dimension at most 3 − j 3-j, we have

 | Card ⁡ ( Σ j + ( W × { 1 }) W × { 1 }) > j ​ K j − 1 ​ L. \card\left(\frac{\Sigma_{j}+\left(W\times\{1\}\right)}{W\times\{1\}}\right)>jK^{j-1}L. |  |

Then the only polynomial P ∈ 𝕂 ⁡ [X 1, X 2, Y] P\in\mathbb{K}\left[X_{1},X_{2},Y\right] of total degree at most K K in X 1 X_{1} and X 2 X_{2} and of degree at most L L in Y Y which is zero on the set Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3} is the zero polynomial.

###### Proof.

This is based on Théorème 2.1 in [14] in the special case of m = 2 m=2 and T 1 = ⋯ = T m + 1 = 0 T_{1}=\cdots=T_{m+1}=0. The only difference is that he stated and proved his result only for ℂ \mathbb{C} in place of our 𝕂 \mathbb{K}. However, his proof only requires that the field be algebraically closed and of characteristic 0 0, rather than requiring any additional properties of ℂ \mathbb{C}.

We have taken his T 1 = ⋯ = T m + 1 = 0 T_{1}=\cdots=T_{m+1}=0 since we are only concerned with the zeroes themselves, not their multiplicities. Also we have used the notation of Waldschmidt [31], which is itself based on the notation of Philippon [26], instead of Gouillon’s similar, but not identical, notation. ∎

###### Proof of Proposition 3.11.

We only show that case j = 1 j=1 of Gouillon’s condition (1) follows from the conditions in our proposition (the first part of condition ( 3.17) of our proposition, in particular), as the proofs of the others are very similar.

In this case, there exists a 𝕂 \mathbb{K} -subspace, W W, of 𝕂 2 \mathbb{K}^{2} of dimension either 0 0 or 1 1.

If the dimension of W W is 0 0, then

(3.20) |  | Card ⁡ ( Σ 1 + ( W × 𝕂 ×) W × 𝕂 ×) = Card ⁡ { ( x 1, x 2): ∃ y ∈ 𝕂 × with ( x 1, x 2, y) ∈ Σ 1 }. \card\left(\frac{\Sigma_{1}+\left(W\times\mathbb{K}^{\times}\right)}{W\times\mathbb{K}^{\times}}\right)=\card\left\{\left(x_{1},x_{2}\right):\text{$\exists y\in\mathbb{K}^{\times}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{1}$}\right\}. |  |

This is because ( x 1, x 2, y) + ( { ( 0, 0) } × 𝕂 ×) = ( x 1, x 2, 1) + ( { ( 0, 0) } × 𝕂 ×) \left(x_{1},x_{2},y\right)+\left(\{(0,0)\}\times\mathbb{K}^{\times}\right)=\left(x_{1},x_{2},1\right)+\left(\{(0,0)\}\times\mathbb{K}^{\times}\right) for any ( x 1, x 2, y) ∈ Σ 1 \left(x_{1},x_{2},y\right)\in\Sigma_{1} and each coset, ( x 1, x 2, 1) + ( { ( 0, 0) } × 𝕂 ×) \left(x_{1},x_{2},1\right)+\left(\{(0,0)\}\times\mathbb{K}^{\times}\right), is distinct.

The first part of our condition ( 3.17) implies that the cardinality in ( 3.20) exceeds K K.

If the dimension of W W is 1 1, then this subspace is

 | { ( x 1, x 2) ∈ 𝕂 2: λ ​ x 1 + μ ​ x 2 = 0 } \left\{\left(x_{1},x_{2}\right)\in\mathbb{K}^{2}:\lambda x_{1}+\mu x_{2}=0\right\} |  |

for some ( λ, μ) ∈ 𝕂 2 \ { ( 0, 0) } (\lambda,\mu)\in\mathbb{K}^{2}\backslash\{(0,0)\}.

For any ( λ, μ) ∈ 𝕂 2 \ { ( 0, 0) } (\lambda,\mu)\in\mathbb{K}^{2}\backslash\{(0,0)\}, there is a bijection between this set and the set in the first part of condition ( 3.17) of our proposition (note that all ( x 1, x 2, y) ∈ Σ 1 \left(x_{1},x_{2},y\right)\in\Sigma_{1} with x 1 x_{1} and x 2 x_{2} fixed map to the same element in the set in Gouillon’s condition (1) with j = 1 j=1). So the first part of condition ( 3.17) of our proposition ensures that Gouillon’s condition (1) holds for j = 1 j=1.

Continuing in a very similar way, we can show that the conditions in our proposition imply that Gouillon’s conditions hold. Hence our conclusion follows from his result. ∎

###### Remark.

Equation ( 3.20) illustrates how the sets on the left-hand sides of ( 3.17)–( 3.19) in Proposition 3.11 arise. They are related to sets of classes of the form ( Σ i + H) / H \left(\Sigma_{i}+H\right)/H for various algebraic subgroups, H H, of 𝕂 2 × 𝕂 × \mathbb{K}^{2}\times\mathbb{K}^{\times}. Such algebraic subgroups, H H, are the obstruction subgroups introduced to the study of zero estimates and multiplicity estimates by Philippon [26].

Also note that any algebraic subgroup of the product of an additive group by a multiplicative group is a product of a subgroup of the additive group and a subgroup of the multiplicative group.

###### Remark 3.13.

For j = 1 j=1, 2 2, 3 3, we shall consider finite sets Σ j \Sigma_{j} defined by

(3.21) |  | Σ j = { ( r + t β 1, s + t β 2, α 1 r α 2 s α 3 t): 0 ≤ r ≤ R j, 0 ≤ s ≤ S j, 0 ≤ t ≤ T j }, \Sigma_{j}=\left\{\left(r+t\beta_{1},s+t\beta_{2},\alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t}\right):0\leq r\leq R_{j},0\leq s\leq S_{j},0\leq t\leq T_{j}\right\}, |  |

where R j R_{j}, S j S_{j} and T j T_{j} are positive integers, β 1 = b 1 / b 3 = b 1 ′ / b 3 ′ \beta_{1}=b_{1}/b_{3}=b_{1}^{\prime}/b_{3}^{\prime} and β 2 = b 2 / b 3 = b 2 ′′ / b 3 ′′ \beta_{2}=b_{2}/b_{3}=b_{2}^{\prime\prime}/b_{3}^{\prime\prime} are as in ( 2.3). This choice corresponds to the entries of the arithmetical matrix used in the definition of Δ \Delta in ( 2.6).

### 3.7. Degeneracies

If the conditions in our zero lemma do not all hold, then there will be a linear dependence relation over ℚ \mathbb{Q} that the b i b_{i} ’s in our linear form satisfy (see conditions ( 2.14) and (C2) in Theorem 2.1). We refer to such cases as degeneracies and present results in this subsection for how we handle them.

###### Remark 3.14.

Note that there is an alternative approach due to Waldschmidt for handling the degenerate case (see the discussion at the end of Section 7.1 of [31, pp. 191–192]). This alternative approach is more efficient in its dependence on b b ( log 2 ⁡ ( b) \log^{2}(b) rather than log 8 / 3 ⁡ ( b) \log^{8/3}(b) as in Subsection 5.3). This would considerably simplify our treatment of the degenerate case as well as the statement of Theorem 2.1. Our attempts to apply it have yielded larger constants, and hence weaker results. But Waldschmidt’s approach certainly warrants further efforts.

Concerning the group, ℂ 2 × ℂ × \mathbb{C}^{2}\times\mathbb{C}^{\times}, the following elementary lemma is important.

###### Lemma 3.15.

The following conditions are equivalent.

(a) The map

 | ψ: ℤ 3 → ℂ 2 × ℂ ×, ( r, s, t) ↦ ( r + β 1 ​ t, s + β 3 ​ t, α 1 r ​ α 2 s ​ α 3 t) \psi:\mathbb{Z}^{3}\to\mathbb{C}^{2}\times\mathbb{C}^{\times},\quad(r,s,t)\mapsto\left(r+\beta_{1}t,s+\beta_{3}t,\alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t}\right) |  |

is not one-to-one ( ( not injective)).

(b) There exists some positive integer m m such that

 | α 3 m ​ b 3 = α 1 m ​ b 1 ​ α 2 m ​ b 2. \alpha_{3}^{mb_{3}}=\alpha_{1}^{mb_{1}}\alpha_{2}^{mb_{2}}. |  |

(c) The number Λ = b 1 ​ log ⁡ α 1 + b 2 ​ log ⁡ α 2 − b 3 ​ log ⁡ α 3 \Lambda=b_{1}\log\alpha_{1}+b_{2}\log\alpha_{2}-b_{3}\log\alpha_{3} belongs to the set i ​ π ​ ℚ i\pi\mathbb{Q}.

###### Proof.

Clearly, without loss of generality, we may assume that gcd ⁡ ( b 1, b 2, b 3) = 1 \gcd\left(b_{1},b_{2},b_{3}\right)=1.

Recall our notation from ( 2.3) with d 1 = gcd ⁡ ( b 1, b 3) d_{1}=\gcd\left(b_{1},b_{3}\right) and d 2 = gcd ⁡ ( b 2, b 3) d_{2}=\gcd\left(b_{2},b_{3}\right). Since gcd ⁡ ( b 1, b 2, b 3) = 1 \gcd\left(b_{1},b_{2},b_{3}\right)=1, we have gcd ⁡ ( d 1, d 2) = 1 \gcd\left(d_{1},d_{2}\right)=1. Thus

 | b 3 = d 1 ​ d 2 ​ b 3 ~ ​ (say), b 3 ′ = d 2 ​ b 3 ~, b 3 ′′ = d 1 ​ b 3 ~. b_{3}=d_{1}d_{2}\widetilde{b_{3}}\ \text{(say)},\quad b_{3}^{\prime}=d_{2}\widetilde{b_{3}},\quad b_{3}^{\prime\prime}=d_{1}\widetilde{b_{3}}. |  |

After these preliminaries, we prove the implication ( a) ⇒ ( b) (a)\Rightarrow(b). Suppose that the map ψ \psi is not injective. Then there exist rational integers r r, s s, t t, not all zero, such that

 | ψ ⁡ ( r, s, t) = ( 0, 0, 1). \psi(r,s,t)=(0,0,1). |  |

That is,

 | r + t ​ β 1 = 0, s + t ​ β 2 = 0, α 1 r ​ α 2 s ​ α 3 t = 1. r+t\beta_{1}=0,\quad s+t\beta_{2}=0,\quad\alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t}=1. |  |

The first relation implies r = − k ​ b 1 ′ r=-kb_{1}^{\prime} for some rational integer, k k. In fact, we have k = t / b 3 ′ k=t/b_{3}^{\prime}. Thus t = k ​ b 3 ′ = k ​ d 2 ​ b 3 ~ t=kb_{3}^{\prime}=kd_{2}\widetilde{b_{3}}. Similarly, from the second relation we have s = − ℓ ​ b 2 ′′ s=-\ell b_{2}^{\prime\prime}, where ℓ = t / b 3 ′′ \ell=t/b_{3}^{\prime\prime}, so t = ℓ ​ b 3 ′′ = ℓ ​ d 1 ​ b 3 ~ t=\ell b_{3}^{\prime\prime}=\ell d_{1}\widetilde{b_{3}}, for some rational integer ℓ \ell. In particular, k ​ d 2 = ℓ ​ d 1 kd_{2}=\ell d_{1}, hence there exists m ∈ ℤ m\in\mathbb{Z} such that k = m ​ d 1 k=md_{1} and ℓ = m ​ d 2 \ell=md_{2}. Thus

 | r = − m b 1, s = − m b 2 and t = m b 3. r=-mb_{1},\quad s=-mb_{2}\quad\text{and}\quad t=mb_{3}. |  |

Since at least one of r r, s s and t t is non-zero, it follows that m ≠ 0 m\neq 0. Thus the third relation gives

 | α 3 m ​ b 3 = α 1 m ​ b 1 ​ α 3 m ​ b 3, \alpha_{3}^{mb_{3}}=\alpha_{1}^{mb_{1}}\alpha_{3}^{mb_{3}}, |  |

as wanted.

Clearly, ( b) (b) implies ( c) (c).

To show that ( c) (c) implies ( a) (a), we suppose that ( c) (c) holds, i.e. that m ​ Λ m\Lambda belongs to 2 ​ i ​ π ​ ℤ 2i\pi\mathbb{Z} for some positive rational integer m m. Then it is clear that ψ ⁡ ( m ​ b 1, m ​ b 2, − m ​ b 3) = ( 0, 0, 1) \psi\left(mb_{1},mb_{2},-mb_{3}\right)=(0,0,1), proving that the map ψ \psi is not injective. ∎

###### Lemma 3.16.

If α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3} are non-zero complex numbers such that (for example) α 1 \alpha_{1} and α 2 \alpha_{2} are multiplicatively independent and α 3 ≠ 1 \alpha_{3}\neq 1 is a root of unity, and if log ⁡ α j \log\alpha_{j} is any determination of the logarithm of α j \alpha_{j} for j = 1 j=1, 2 2, 3 3, then the numbers log ⁡ α 1 \log\alpha_{1}, log ⁡ α 2 \log\alpha_{2} and log ⁡ α 3 \log\alpha_{3} are linearly independent over the rationals.

Furthermore, if b 1 b_{1}, b 2 b_{2} and b 3 b_{3} are rational integers with at least one of b 1 b_{1} and b 2 b_{2} non-zero, then the number b 1 ​ log ⁡ α 1 + b 2 ​ log ⁡ α 2 + b 3 ​ log ⁡ α 3 b_{1}\log\alpha_{1}+b_{2}\log\alpha_{2}+b_{3}\log\alpha_{3} does not belong to the set i ​ π ​ ℚ i\pi\mathbb{Q}.

###### Proof.

Suppose that

 | Λ = b 1 ​ log ⁡ α 1 + b 2 ​ log ⁡ α 2 − b 3 ​ log ⁡ α 3 = 0 \Lambda=b_{1}\log\alpha_{1}+b_{2}\log\alpha_{2}-b_{3}\log\alpha_{3}=0 |  |

where b 1 b_{1}, b 2 b_{2} and b 3 b_{3} are rational integers not all equal to zero. Then α 3 b 3 = α 1 b 1 ​ α 2 b 2 \alpha_{3}^{b_{3}}=\alpha_{1}^{b_{1}}\alpha_{2}^{b_{2}}. Assume that α 3 d = 1 \alpha_{3}^{d}=1 with d > 1 d>1, then α 2 d ​ b 2 = α 1 − d ​ b 1 \alpha_{2}^{db_{2}}=\alpha_{1}^{-db_{1}}, which implies b 1 = b 2 = 0 b_{1}=b_{2}=0 since α 1 \alpha_{1} and α 2 \alpha_{2} are multiplicatively independent. Since we assumed that b 1 b_{1}, b 2 b_{2} and b 3 b_{3} are not all equal to zero, it follows that b 3 ≠ 0 b_{3}\neq 0 and so Λ = b 3 ​ log ⁡ α 3 ≠ 0 \Lambda=b_{3}\log\alpha_{3}\neq 0, since α 3 ≠ 1 \alpha_{3}\neq 1. This contradiction proves the first claim.

Noting that log ⁡ α 3 = 2 ​ π ​ i ​ m / n \log\alpha_{3}=2\pi im/n with n ∤ m n\nmid m, the second claim follows from the first one. ∎

The following very elementary lemma will be useful when investigating conditions ( 3.17) and ( 3.18) of Proposition 3.11.

###### Lemma 3.17.

Suppose that b 1 b_{1}, b 2 b_{2} and b 3 b_{3} are positive rational integers which are coprime. Let R R, S S and T T be positive integers and consider the set

 | Σ ~ = { ( r + t b 1 / b 3, s + t b 2 / b 3): 0 ≤ r ≤ R, 0 ≤ s ≤ S, 0 ≤ t ≤ T }. \widetilde{\Sigma}=\left\{\left(r+tb_{1}/b_{3},s+tb_{2}/b_{3}\right):0\leq r\leq R,\,0\leq s\leq S,\,0\leq t\leq T\right\}. |  |

Then

 | Card ⁡ Σ ~ = ( R + 1) ​ ( S + 1) ​ ( T + 1) \card\widetilde{\Sigma}=(R+1)(S+1)(T+1) |  |

unless

 | b 1 ≤ R and b 2 ≤ S and b 3 ≤ T. b_{1}\leq R\quad\text{and}\quad b_{2}\leq S\quad\text{and}\quad b_{3}\leq T. |  |

###### Proof.

With the same notation as above, suppose that the map

 | ψ: { ( r, s, t): 0 ≤ r ≤ R, 0 ≤ s ≤ S, 0 ≤ t ≤ T } → Σ ~, ( r, s, t) ↦ ( r + β 1 t, s + β 2 t) \psi:\left\{(r,s,t):0\leq r\leq R,0\leq s\leq S,0\leq t\leq T\right\}\to\widetilde{\Sigma},\quad(r,s,t)\mapsto\left(r+\beta_{1}t,s+\beta_{2}t\right) |  |

is not injective. Then there exist two different triples of rational integers ( r, s, t) (r,s,t) and ( r ′, s ′, t ′) (r^{\prime},s^{\prime},t^{\prime}), with 0 ≤ r, r ′ ≤ R 0\leq r,\,r^{\prime}\leq R, 0 ≤ s, s ′ ≤ S 0\leq s,s^{\prime}\leq S and 0 ≤ t, t ′ ≤ T 0\leq t,t^{\prime}\leq T such that ψ ⁡ ( r, s, t) = ψ ⁡ ( r ′, s ′, t ′) \psi(r,s,t)=\psi(r^{\prime},s^{\prime},t^{\prime}). That is,

 | ( r − r ′) + ( t − t ′) ​ β 1 = 0 and ( s − s ′) + ( t − t ′) ​ β 3 = 0. (r-r^{\prime})+(t-t^{\prime})\beta_{1}=0\quad\text{ and}\quad(s-s^{\prime})+(t-t^{\prime})\beta_{3}=0. |  |

As in the proof that (a) implies (b) for Lemma 3.15, these two relations imply that

 | r − r ′ = m ​ b 1, s − s ′ = m ​ b 2, s − s ′ = − m ​ b 3. r-r^{\prime}=mb_{1},\quad s-s^{\prime}=mb_{2},\quad s-s^{\prime}=-mb_{3}. |  |

Thus − R ≤ m ​ b 1 ≤ R -R\leq mb_{1}\leq R, − S ≤ m ​ b 2 ≤ S -S\leq mb_{2}\leq S and − T ≤ m ​ b 3 ≤ T -T\leq mb_{3}\leq T. Since m m is non-zero and the b i b_{i} ’s are positive, the conclusion follows. ∎

The first subcondition of condition ( 3.17) in Proposition 3.11 is the most difficult to handle. For it, we will need the following lemmas, in particular, Lemma 3.21. These lemmas also bring some extra information to Proposition 3.1.1 of [4] (also see [31, Ex 6.4, pp. 184–185]).

###### Lemma 3.18.

Let A A, B B, C C, D D, X > 0 X>0, Y > 0 Y>0 and Z > 0 Z>0 be rational integers with gcd ⁡ ( A, B, C) = 1 \gcd(A,B,C)=1 and A ​ B ​ C ≠ 0 ABC\neq 0. Put

 | Σ = { ( x, y, z) ∈ ℤ 3: 0 ≤ x ≤ X, 0 ≤ y ≤ Y, 0 ≤ z ≤ Z } \Sigma=\left\{(x,y,z)\in\mathbb{Z}^{3}:0\leq x\leq X,0\leq y\leq Y,0\leq z\leq Z\right\} |  |

and

 | M = Card ⁡ { ( x, y, z) ∈ Σ: A ​ x + B ​ y + C ​ z = D }. M=\card\left\{(x,y,z)\in\Sigma:Ax+By+Cz=D\right\}. |  |

(a) We have

 | M ≤ ( 1 + ⌊ X α ⌋) ​ ( 1 + ⌊ Y | C | / α ⌋) and M ≤ ( 1 + ⌊ X α ⌋) ​ ( 1 + ⌊ Z | B | / α ⌋), M\leq\left(1+\left\lfloor\frac{X}{\alpha}\right\rfloor\right)\left(1+\left\lfloor\frac{Y}{|C|/\alpha}\right\rfloor\right)\quad\text{and}\quad M\leq\left(1+\left\lfloor\frac{X}{\alpha}\right\rfloor\right)\left(1+\left\lfloor\frac{Z}{|B|/\alpha}\right\rfloor\right), |  |

where

 | α = gcd ⁡ ( B, C). \alpha=\gcd(B,C). |  |

(b) If we suppose that

 | M ≥ max ⁡ { X + Y + 1, Y + Z + 1, Z + X + 1 } M\geq\max\left\{X+Y+1,\,Y+Z+1,\,Z+X+1\right\} |  |

then

 | | A | ≤ ( Y + 1) ​ ( Z + 1) M − max ⁡ { Y, Z }, | B | ≤ ( X + 1) ​ ( Z + 1) M − max ⁡ { X, Z } and | C | ≤ ( X + 1) ​ ( Y + 1) M − max ⁡ { X, Y }. \left|A\right|\leq\frac{(Y+1)(Z+1)}{M-\max\{Y,Z\}},\quad\left|B\right|\leq\frac{(X+1)(Z+1)}{M-\max\{X,Z\}}\quad\text{and}\quad\left|C\right|\leq\frac{(X+1)(Y+1)}{M-\max\{X,Y\}}. |  |

###### Remark 3.19.

When we apply part (b) of this lemma, we will assume that M M is (possibly) even larger. Let 𝒱 = ( ( X + 1) ​ ( Y + 1) ​ ( Z + 1)) 1 / 2 \mathcal{V}=((X+1)(Y+1)(Z+1))^{1/2} and suppose that χ \chi is a positive real number. We will assume that

 | M ≥ max ⁡ { X + Y + 1, Y + Z + 1, Z + X + 1, χ ​ 𝒱 }. M\geq\max\left\{X+Y+1,\,Y+Z+1,\,Z+X+1,\chi\mathcal{V}\right\}. |  |

###### Proof.

(a) Define

 | Π = { ( x, y, z) ∈ ℂ 3: A ​ x + B ​ y + C ​ z = D }. \Pi=\left\{(x,y,z)\in\mathbb{C}^{3}:Ax+By+Cz=D\right\}. |  |

If the image by the map ( x, y, z) ↦ A ​ x + B ​ y + C ​ z (x,y,z)\mapsto Ax+By+Cz of a point ( x, y, z) ∈ ℤ 3 (x,y,z)\in\mathbb{Z}^{3} belongs to the plane Π \Pi, then

 | A ​ x ≡ D ( mod α), Ax\equiv D\pmod{\alpha}, |  |

where A A and α \alpha are coprime since gcd ⁡ ( A, B, C) = 1 \gcd(A,B,C)=1. This shows that the number of such x x which satisfy 0 ≤ x ≤ X 0\leq x\leq X is at most 1 + ⌊ X / α ⌋ 1+\left\lfloor X/\alpha\right\rfloor.

Now let x x be fixed, with 0 ≤ x ≤ X 0\leq x\leq X, and such that the images of two distinct elements ( x, y, z) (x,y,z) and ( x, y ′, z ′) (x,y^{\prime},z^{\prime}) of Σ \Sigma also belong to Π \Pi. Then

 | B ⁡ ( y ′ − y) = C ⁡ ( z − z ′), B(y^{\prime}-y)=C(z-z^{\prime}), |  |

where we suppose (as we may) that y y is minimal (then y ′ > y y^{\prime}>y). Hence there exists a positive integer k k such that

 | y ′ − y = k ⁡ ( | C | / α) and z − z ′ = ± k ⁡ ( | B | / α). y^{\prime}-y=k(|C|/\alpha)\quad\text{and}\quad z-z^{\prime}=\pm k(|B|/\alpha). |  |

It follows that, for x x fixed, the number of ( x, y, z) ∈ Σ (x,y,z)\in\Sigma whose image belongs to Π \Pi is at most 1 + ⌊ Y / ( | C | / α) ⌋ 1+\lfloor Y/(|C|/\alpha)\rfloor. Hence

(3.22) |  | M ≤ ( 1 + ⌊ X α ⌋) ​ ( 1 + ⌊ Y | C | / α ⌋), M\leq\left(1+\left\lfloor\frac{X}{\alpha}\right\rfloor\right)\left(1+\left\lfloor\frac{Y}{|C|/\alpha}\right\rfloor\right), |  |

which proves the first upper bound for M M in part (a) of the lemma.

The proof of the second upper bound for M M is the same, except for fixed values of x x, we bound the number of possible z z -coordinates rather than the number of possible y y -coordinates.

(b) We start with the upper bound for | C | |C|.

For ξ ≥ 1 \xi\geq 1, put

 | f ⁡ ( ξ) = ( 1 + X ξ) ​ ( 1 + ξ ​ Y | C |). f(\xi)=\left(1+\frac{X}{\xi}\right)\left(1+\frac{\xi Y}{|C|}\right). |  |

From equation ( 3.22), it follows that

 | M ≤ f ⁡ ( α). M\leq f(\alpha). |  |

Clearly, 1 ≤ α ≤ C 1\leq\alpha\leq C. Since f ′′ ​ ( ξ) = 2 ​ X / ξ 3 > 0 f^{\prime\prime}(\xi)=2X/\xi^{3}>0, it follows that f ⁡ ( ξ) f(\xi) is convex and so

 | M ≤ f ⁡ ( α) ≤ max ⁡ { f ⁡ ( 1), f ⁡ ( C) }. M\leq f(\alpha)\leq\max\left\{f(1),f(C)\right\}. |  |

If

 | M ≤ f ⁡ ( 1) = 1 + X ​ Y | C | + X + Y | C |, then | C | ≤ Y ⁡ ( X + 1) M − ( X + 1). M\leq f(1)=1+\frac{XY}{|C|}+X+\frac{Y}{|C|},\quad\text{ then }\quad|C|\leq\frac{Y(X+1)}{M-(X+1)}. |  |

If

 | M ≤ f ⁡ ( C) = 1 + X ​ Y | C | + X | C | + Y, then | C | ≤ X ⁡ ( Y + 1) M − ( Y + 1). M\leq f(C)=1+\frac{XY}{|C|}+\frac{X}{|C|}+Y,\quad\text{ then }\quad|C|\leq\frac{X(Y+1)}{M-(Y+1)}. |  |

Suppose finally that

 | M ≥ max ⁡ { X + Y + 1, Y + Z + 1, Z + X + 1 }. M\geq\max\{X+Y+1,Y+Z+1,Z+X+1\}. |  |

Since M − X ≥ Y + 1 M-X\geq Y+1, we can write

 | Y ⁡ ( X + 1) M − ( X + 1) = X ​ Y + Y ( M − X) ​ ( 1 − 1 / ( M − X)) \displaystyle\frac{Y(X+1)}{M-(X+1)}=\frac{XY+Y}{(M-X)(1-1/(M-X))} | = X ​ Y + Y M − X ​ ( 1 + 1 M − X + 1 ( M − X) 2 + ⋯) \displaystyle=\frac{XY+Y}{M-X}\left(1+\frac{1}{M-X}+\frac{1}{(M-X)^{2}}+\cdots\right) |  |

 |  | ≤ X ​ Y + Y M − X ​ ( 1 + 1 Y + 1 + 1 ( Y + 1) 2 + ⋯) \displaystyle\leq\frac{XY+Y}{M-X}\left(1+\frac{1}{Y+1}+\frac{1}{(Y+1)^{2}}+\cdots\right) |  |

 |  | = X ​ Y + Y M − X ​ Y + 1 Y = ( X + 1) ​ ( Y + 1) M − X. \displaystyle=\frac{XY+Y}{M-X}\frac{Y+1}{Y}=\frac{(X+1)(Y+1)}{M-X}. |  |

Similarly,

 | X ⁡ ( Y + 1) M − ( Y + 1) ≤ ( X + 1) ​ ( Y + 1) M − Y. \frac{X(Y+1)}{M-(Y+1)}\leq\frac{(X+1)(Y+1)}{M-Y}. |  |

Thus, we always have

 | | C | ≤ ( X + 1) ​ ( Y + 1) M − max ⁡ { X, Y }. |C|\leq\frac{(X+1)(Y+1)}{M-\max\{X,Y\}}. |  |

The upper bounds for | A | |A| and | B | |B| are proved in the same way. ∎

###### Lemma 3.20.

Let B B, C C, D D, X > 0 X>0, Y > 0 Y>0 and Z > 0 Z>0 be rational integers with gcd ⁡ ( B, C) = 1 \gcd(B,C)=1 and B ​ C ≠ 0 BC\neq 0.

Put

 | Σ = { ( x, y, z) ∈ ℤ 3: 0 ≤ x ≤ X, 0 ≤ y ≤ Y, 0 ≤ z ≤ Z } \Sigma=\left\{(x,y,z)\in\mathbb{Z}^{3}:0\leq x\leq X,0\leq y\leq Y,0\leq z\leq Z\right\} |  |

and

 | M = Card ⁡ { ( x, y, z) ∈ Σ: B ​ y + C ​ z = D }. M=\card\left\{(x,y,z)\in\Sigma:By+Cz=D\right\}. |  |

(a) We have

 | M ≤ ( X + 1) ​ ( 1 + ⌊ Y | C | ⌋) and M ≤ ( X + 1) ​ ( 1 + ⌊ Z | B | ⌋). M\leq(X+1)\left(1+\left\lfloor\frac{Y}{|C|}\right\rfloor\right)\quad\text{and}\quad M\leq(X+1)\left(1+\left\lfloor\frac{Z}{|B|}\right\rfloor\right). |  |

(b) Moreover, if we suppose that

 | M ≥ max ⁡ { X + Y + 1, X + Z + 1 }, M\geq\max\{X+Y+1,X+Z+1\}, |  |

then

 | | B | ≤ ( X + 1) ​ ( Z + 1) M − X and | C | ≤ ( X + 1) ​ ( Y + 1) M − X. \left|B\right|\leq\frac{(X+1)(Z+1)}{M-X}\quad\text{and}\quad\left|C\right|\leq\frac{(X+1)(Y+1)}{M-X}. |  |

###### Remark.

As with Lemma 3.18 (b) and noted in Remark 3.19, when we apply part (b) of this lemma, we will assume that M M is (possibly) even larger. Let 𝒱 = ( ( X + 1) ​ ( Y + 1) ​ ( Z + 1)) 1 / 2 \mathcal{V}=((X+1)(Y+1)(Z+1))^{1/2} and suppose that χ \chi is a positive real number. We will assume that

 | M ≥ max ⁡ { X + Y + 1, Y + Z + 1, Z + X + 1, χ ​ 𝒱 }. M\geq\max\left\{X+Y+1,\,Y+Z+1,\,Z+X+1,\chi\mathcal{V}\right\}. |  |

###### Proof.

The proof is similar to that of Lemma 3.18, but simpler.

(a) Define the plane

 | Π = { ( x, y, z) ∈ ℂ 3: B ​ y + C ​ z = D } \Pi=\left\{(x,y,z)\in\mathbb{C}^{3}:By+Cz=D\right\} |  |

and consider the map ( x, y, z) ↦ B ​ y + C ​ z (x,y,z)\mapsto By+Cz defined on ℂ 3 \mathbb{C}^{3}.

Let x x be fixed with 0 ≤ x ≤ X 0\leq x\leq X and such that the images of two distinct points ( x, y, z) (x,y,z) and ( x, y ′, z ′) (x,y^{\prime},z^{\prime}) in Σ \Sigma belong to Π \Pi. Then

 | B ⁡ ( y ′ − y) = C ⁡ ( z − z ′), B(y^{\prime}-y)=C(z-z^{\prime}), |  |

where we suppose (as we may) that y y is minimal (then y ′ > y y^{\prime}>y). Hence there exists a positive integer k k such that

 | y ′ − y = k ​ | C | and z − z ′ = ± k ​ | B |. y^{\prime}-y=k|C|\quad\text{and}\quad z-z^{\prime}=\pm k|B|. |  |

Since y ′ − y = C ⁡ ( z − z ′) / B y^{\prime}-y=C(z-z^{\prime})/B and gcd ⁡ ( B, C) = 1 \gcd(B,C)=1, it must be the case that B | ( z − z ′) B|(z-z^{\prime}). This is why k k is an integer.

It follows that, for x x fixed, the number of ( x, y, z) ∈ Σ (x,y,z)\in\Sigma whose image belongs to Π \Pi is at most 1 + ⌊ Y / | C | ⌋ 1+\lfloor Y/|C|\rfloor. Hence

(3.23) |  | M ≤ ( 1 + X) ​ ( 1 + ⌊ Y | C | ⌋), M\leq(1+X)\left(1+\left\lfloor\frac{Y}{|C|}\right\rfloor\right), |  |

which proves the first upper bound for M M in the lemma.

The proof of the second upper bound for M M is the same, except for fixed values of x x, we bound the number of possible z z -coordinates rather than the number of possible y y -coordinates.

(b) We turn now to the upper bounds for | B | |B| and | C | |C|, starting with the upper bound for | C | |C|.

From equation ( 3.23), it follows that

 | M ≤ ( 1 + X) ​ ( 1 + Y | C |). M\leq\left(1+X\right)\left(1+\frac{Y}{|C|}\right). |  |

Thus

 | | C | ≤ Y ⁡ ( 1 + X) M − 1 − X. |C|\leq\frac{Y(1+X)}{M-1-X}. |  |

Suppose now

 | M ≥ max ⁡ { X + Y + 1, X + Z + 1 }. M\geq\max\{X+Y+1,X+Z+1\}. |  |

As we saw in the proof of Lemma 3.18, M ≥ X + Y + 1 M\geq X+Y+1 implies that

 | | C | ≤ Y ⁡ ( 1 + X) M − 1 − X ≤ ( X + 1) ​ ( Y + 1) M − X, |C|\leq\frac{Y(1+X)}{M-1-X}\leq\frac{(X+1)(Y+1)}{M-X}, |  |

as required.

The remaining upper bound for | B | |B| at the end of the lemma is proved in the same way. ∎

###### Lemma 3.21.

Let R 1 R_{1}, S 1 S_{1} and T 1 T_{1} be positive integers and consider the set

 | Σ ~ 1 = { ( x 1, x 2) = ( r + t β 1, s + t β 2): 0 ≤ r ≤ R 1, 0 ≤ s ≤ S 1, 0 ≤ t ≤ T 1 }, \widetilde{\Sigma}_{1}=\left\{\left(x_{1},x_{2}\right)=\left(r+t\beta_{1},s+t\beta_{2}\right):0\leq r\leq R_{1},0\leq s\leq S_{1},0\leq t\leq T_{1}\right\}, |  |

where β 1 = b 1 / b 3 \beta_{1}=b_{1}/b_{3} and β 2 = b 2 / b 3 \beta_{2}=b_{2}/b_{3} with b 1 b_{1}, b 2 b_{2} and b 3 b_{3} coprime non-zero rational integers, and assume that

 | Card ⁡ Σ ~ 1 = ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1). \card\widetilde{\Sigma}_{1}=\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right). |  |

Put

 | 𝒱 = ( ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1)) 1 / 2. \mathcal{V}=\left(\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)\right)^{1/2}. |  |

For any ( λ, μ) ∈ ℂ 2 ∖ { ( 0, 0) } (\lambda,\mu)\in\mathbb{C}^{2}\setminus\{(0,0)\} and any complex number c c, let M c M_{c} be the number of elements ( x 1, x 2) ∈ Σ ~ 1 \left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1} such that λ ​ x 1 + μ ​ x 2 = c \lambda x_{1}+\mu x_{2}=c.

(a) Let χ \chi be a positive real number. If

(3.24) |  | M c < ℳ:= max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1, χ ​ 𝒱 } M_{c}<\mathcal{M}:=\max\left\{R_{1}+S_{1}+1,S_{1}+T_{1}+1,R_{1}+T_{1}+1,\chi\mathcal{V}\right\} |  |

does not hold, then there exist rational integers u 1 u_{1}, u 2 u_{2} and u 3 u_{3}, not all zero, such that

 | u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = 0, u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=0, |  |

with gcd ⁡ ( u 1, u 2, u 3) = 1 \gcd\left(u_{1},u_{2},u_{3}\right)=1 and

 | | u 1 | ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, | u 2 | ≤ ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 } and | u 3 | ≤ ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 }. \left|u_{1}\right|\leq\frac{(S_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{S_{1},T_{1}\}},\qquad\left|u_{2}\right|\leq\frac{(R_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{R_{1},T_{1}\}}\quad\text{and}\quad\left|u_{3}\right|\leq\frac{(R_{1}+1)(S_{1}+1)}{\mathcal{M}-\max\{R_{1},S_{1}\}}. |  |

(b) If the upper bound ( 3.24) for M c M_{c} holds then, for all ( λ, μ) ∈ ℂ 2 ∖ { ( 0, 0) } (\lambda,\mu)\in\mathbb{C}^{2}\setminus\{(0,0)\}, we have

 | Card ⁡ { λ ​ x 1 + μ ​ x 2: ( x 1, x 2) ∈ Σ ~ 1 } ≥ ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1, χ ​ 𝒱 }. \card\left\{\lambda x_{1}+\mu x_{2}:\left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1}\right\}\geq\frac{(R_{1}+1)(S_{1}+1)(T_{1}+1)}{\max\left\{R_{1}+S_{1}+1,S_{1}+T_{1}+1,R_{1}+T_{1}+1,\chi\mathcal{V}\right\}}. |  |

###### Remark.

The introduction of χ ​ 𝒱 \chi\mathcal{V} here turns out to be very helpful to us. In many cases, χ ​ 𝒱 \chi\mathcal{V} is much larger than the other terms in the definition of ℳ \mathcal{M} here. So its use here gives us much smaller upper bounds on the sizes of the u i u_{i} ’s. This gives us better results from the kit.

###### Proof.

(a) Suppose that ( 3.24) does not hold for some triple ( λ, μ, c) (\lambda,\mu,c). Let c c be a complex number such that M c M_{c} is maximal and consider the associated values of λ \lambda and μ \mu. We distinguish the following possibilities for μ \mu and λ \lambda.

∙ \bullet μ = 0 \mu=0: suppose that ( x 1, x 2) ∈ Σ ~ 1 \left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1} satisfies λ ​ x 1 + μ ​ x 2 = λ ⁡ ( r + t ​ β 1) = c \lambda x_{1}+\mu x_{2}=\lambda\left(r+t\beta_{1}\right)=c. So b 3 ​ r + b 1 ​ t = c ​ b 3 / λ b_{3}r+b_{1}t=cb_{3}/\lambda for some integers 0 ≤ r ≤ R 1 0\leq r\leq R_{1} and 0 ≤ t ≤ T 1 0\leq t\leq T_{1} (since μ = 0 \mu=0 here and also ( μ, λ) ≠ ( 0, 0) (\mu,\lambda)\neq(0,0), we have λ ≠ 0 \lambda\neq 0).

We will now apply Lemma 3.20. Let ( X, Y, Z) (X,Y,Z) there be ( S 1, R 1, T 1) \left(S_{1},R_{1},T_{1}\right) and ( B, C, D) (B,C,D) there be ( b 3 / d 1, b 1 / d 1, c ​ b 3 / ( λ ​ d 1)) \left(b_{3}/d_{1},b_{1}/d_{1},cb_{3}/\left(\lambda d_{1}\right)\right), where d 1 = gcd ⁡ ( b 1, b 3) d_{1}=\gcd\left(b_{1},b_{3}\right). Taking r r and t t here as y y and z z, respectively, in the definition of M M in Lemma 3.20, the equation B ​ y + C ​ z = D By+Cz=D in the definition of M M becomes our ( b 3 / d 1) ​ r + ( b 1 / d 1) ​ t = c ​ b 3 / ( d 1 ​ λ) \left(b_{3}/d_{1}\right)r+\left(b_{1}/d_{1}\right)t=cb_{3}/\left(d_{1}\lambda\right).

Using the map σ: Σ → Σ ~ 1 \sigma:\Sigma\rightarrow\widetilde{\Sigma}_{1} defined by σ: ( s, r, t) ↦ ( r + t ​ β 1, s + t ​ β 2) \sigma:(s,r,t)\mapsto\left(r+t\beta_{1},s+t\beta_{2}\right), we show that the cardinalities of Σ \Sigma and Σ ~ 1 \widetilde{\Sigma}_{1} are equal. The map is clearly surjective. Suppose that

 | σ ⁡ ( s 1, r 1, t 1) = ( r 1 + t 1 ​ β 1, s 1 + t 1 ​ β 2) = ( r 2 + t 2 ​ β 1, s 2 + t 2 ​ β 2) = σ ⁡ ( s 2, r 2, t 2). \sigma\left(s_{1},r_{1},t_{1}\right)=\left(r_{1}+t_{1}\beta_{1},s_{1}+t_{1}\beta_{2}\right)=\left(r_{2}+t_{2}\beta_{1},s_{2}+t_{2}\beta_{2}\right)=\sigma\left(s_{2},r_{2},t_{2}\right). |  |

Then ( r 1 − r 2) + ( t 1 − t 2) ​ β 2 = ( s 1 − s 2) + ( t 1 − t 2) ​ β 2 = 0 \left(r_{1}-r_{2}\right)+\left(t_{1}-t_{2}\right)\beta_{2}=\left(s_{1}-s_{2}\right)+\left(t_{1}-t_{2}\right)\beta_{2}=0, so r 1 − r 2 = s 1 − s 2 r_{1}-r_{2}=s_{1}-s_{2}. In this case, we can write r 1 = r 2 + k r_{1}=r_{2}+k and s 1 = s 2 + k s_{1}=s_{2}+k. Thus ( r 2 + k + t 1 ​ β 1, s 2 + k + t 1 ​ β 2) = ( r 2 + t 2 ​ β 1, s 2 + t 2 ​ β 2) \left(r_{2}+k+t_{1}\beta_{1},s_{2}+k+t_{1}\beta_{2}\right)=\left(r_{2}+t_{2}\beta_{1},s_{2}+t_{2}\beta_{2}\right), which can only happen if k = 0 k=0. This proves that σ \sigma is injective too. Hence the cardinalities of Σ \Sigma and Σ ~ 1 \widetilde{\Sigma}_{1} are equal

Therefore, since ( 3.24) does not hold, the inequality for M M in Lemma 3.20 (b) holds and we have

 | | b 3 / d 1 | = | B | ≤ ( S 1 + 1) ​ ( T 1 + 1) M c − S 1 ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − S 1 \left|b_{3}/d_{1}\right|=|B|\leq\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{M_{c}-S_{1}}\leq\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-S_{1}} |  |

and

 | | b 1 / d 1 | = | C | ≤ ( S 1 + 1) ​ ( R 1 + 1) M c − S 1 ≤ ( S 1 + 1) ​ ( R 1 + 1) ℳ − S 1. \left|b_{1}/d_{1}\right|=|C|\leq\frac{\left(S_{1}+1\right)\left(R_{1}+1\right)}{M_{c}-S_{1}}\leq\frac{\left(S_{1}+1\right)\left(R_{1}+1\right)}{\mathcal{M}-S_{1}}. |  |

We now use this information to obtain the linear relation we want between the b i b_{i} ’s. We have the trivial relationship ( b 1 / d 1) ​ b 3 − b 1 ​ ( b 3 / d 1) = 0 \left(b_{1}/d_{1}\right)b_{3}-b_{1}\left(b_{3}/d_{1}\right)=0, so we can let u 1 = − b 3 / d 1 u_{1}=-b_{3}/d_{1}, u 2 = 0 u_{2}=0 and u 3 = b 1 / d 1 u_{3}=b_{1}/d_{1}. The upper bounds above on | b 3 / d 1 | \left|b_{3}/d_{1}\right| and | b 1 / d 1 | \left|b_{1}/d_{1}\right| establish our lemma in this case.

Now we assume μ ≠ 0 \mu\neq 0 and, to simplify the notation, we take μ = 1 \mu=1.

∙ \bullet λ = 0 \lambda=0: by the same argument as for μ = 0 \mu=0, we have b 3 ​ ( λ ​ x 1 + μ ​ x 2) = b 3 ​ μ ​ x 2 = b 3 ​ ( s + t ​ β 2) = b 3 ​ s + t ​ b 2 = b 3 ​ c b_{3}\left(\lambda x_{1}+\mu x_{2}\right)=b_{3}\mu x_{2}=b_{3}\left(s+t\beta_{2}\right)=b_{3}s+tb_{2}=b_{3}c for some ( x 1, x 2) ∈ Σ ~ 1 \left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1}. Here we apply Lemma 3.20 with ( R 1, S 1, T 1) \left(R_{1},S_{1},T_{1}\right) for ( X, Y, Z) (X,Y,Z) and ( b 3 / d 1, b 2 / d 1, b 3 ​ c / d 1) \left(b_{3}/d_{1},b_{2}/d_{1},b_{3}c/d_{1}\right) for ( B, C, D) (B,C,D), where d 1 = gcd ⁡ ( b 2, b 3) d_{1}=\gcd\left(b_{2},b_{3}\right). As in the case of μ = 0 \mu=0, Lemma 3.20 (b) gives us

 | | b 3 / d 1 | = | B | ≤ ( R 1 + 1) ​ ( T 1 + 1) ℳ − R 1 and | b 2 / d 1 | = | C | ≤ ( R 1 + 1) ​ ( S 1 + 1) ℳ − S 1. \left|b_{3}/d_{1}\right|=|B|\leq\frac{\left(R_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-R_{1}}\quad\text{and}\quad\left|b_{2}/d_{1}\right|=|C|\leq\frac{\left(R_{1}+1\right)\left(S_{1}+1\right)}{\mathcal{M}-S_{1}}. |  |

As in the case of μ = 0 \mu=0, we have the relationship u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = 0 u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=0 with u 1 = 0 u_{1}=0, u 2 = b 3 / d 1 u_{2}=b_{3}/d_{1} and u 3 = − b 2 / d 1 u_{3}=-b_{2}/d_{1}.

It remains to consider μ ​ λ ≠ 0 \mu\lambda\neq 0. We do so with two cases.

∙ \bullet λ ​ b 1 + b 2 = 0 \lambda b_{1}+b_{2}=0: we proceed in the same way as in the case of λ = 0 \lambda=0. We have λ x 1 + μ x 2 = − b 2 / b 1 ( r + t β 1) + s + t β 2 = c \lambda x_{1}+\mu x_{2}=-b_{2}/b_{1}\left(r+t\beta_{1}\right)+s+t\beta_{2}=c (recalling that we take μ = 1 \mu=1). Expanding this and simplifying it, we obtain − b 2 ​ r + b 1 ​ s = c ​ b 1 -b_{2}r+b_{1}s=cb_{1}, so we use Lemma 3.20 with ( 0, − b 2 / d 2, b 1 / d 2, c b 1 / d 2) \left(0,-b_{2}/d_{2},b_{1}/d_{2},cb_{1}/d_{2}\right) for ( A, B, C, D) (A,B,C,D), ( t, r, s) (t,r,s) for ( x, y, z) (x,y,z) and ( T 1, R 1, S 1) \left(T_{1},R_{1},S_{1}\right) for ( X, Y, Z) \left(X,Y,Z\right), where d 2 = gcd ⁡ ( b 1, b 2) d_{2}=\gcd\left(b_{1},b_{2}\right). Here

 | | b 2 / d 2 | = | B | ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − T 1 and | b 1 / d 2 | = | C | ≤ ( T 1 + 1) ​ ( R 1 + 1) ℳ − T 1. \left|b_{2}/d_{2}\right|=|B|\leq\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-T_{1}}\quad\text{and}\quad\left|b_{1}/d_{2}\right|=|C|\leq\frac{\left(T_{1}+1\right)\left(R_{1}+1\right)}{\mathcal{M}-T_{1}}. |  |

Notice the denominators here differ from those for the case of λ = 0 \lambda=0. This explains why we need the max \max in our upper bounds in the lemma.

The desired relationship, u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = 0 u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=0, holds if we take u 1 = b 2 / d 2 u_{1}=b_{2}/d_{2}, u 2 = − b 1 / d 2 u_{2}=-b_{1}/d_{2} and u 3 = 0 u_{3}=0.

∙ \bullet λ ​ μ ​ ( λ ​ b 1 + b 2) ≠ 0 \lambda\mu\left(\lambda b_{1}+b_{2}\right)\neq 0: we will show that the desired relationship between the b i b_{i} ’s holds here too. To proceed, we put

 | E 1 = { ( r, s, t) ∈ ℤ 3: 0 ≤ r ≤ R 1, 0 ≤ s ≤ S 1, 0 ≤ t ≤ T 1 }. E_{1}=\left\{(r,s,t)\in\mathbb{Z}^{3}:0\leq r\leq R_{1},0\leq s\leq S_{1},0\leq t\leq T_{1}\right\}. |  |

Since M c > T 1 + 1 M_{c}>T_{1}+1 (by our assumption that ( 3.24) does not hold), there exist two distinct triples ( r 1, s 1, t 0) \left(r_{1},s_{1},t_{0}\right) and ( r 1 ′, s 1 ′, t 0) ∈ E 1 \left(r_{1}^{\prime},s_{1}^{\prime},t_{0}\right)\in E_{1} such that

 | λ ⁡ ( r 1 + β 1 ​ t 0) + ( s 1 + β 2 ​ t 0) = λ ⁡ ( r 1 ′ + β 1 ​ t 0) + ( s 1 ′ + β 2 ​ t 0), \lambda\left(r_{1}+\beta_{1}t_{0}\right)+\left(s_{1}+\beta_{2}t_{0}\right)=\lambda\left(r_{1}^{\prime}+\beta_{1}t_{0}\right)+\left(s_{1}^{\prime}+\beta_{2}t_{0}\right), |  |

recalling our assumption (stated just before considering the case λ = 0 \lambda=0) that μ = 1 \mu=1. This gives us a trivial linear relation between the b i b_{i} ’s, but it does tell us that λ ⁡ ( r 1 ′ − r 1) = s 1 − s 1 ′ \lambda\left(r_{1}^{\prime}-r_{1}\right)=s_{1}-s_{1}^{\prime}. Since λ ≠ 0 \lambda\neq 0 and at least one of r 1 ≠ r 1 ′ r_{1}\neq r_{1}^{\prime} or s 1 ≠ s 1 ′ s_{1}\neq s_{1}^{\prime} holds, it follows that both r 1 ≠ r 1 ′ r_{1}\neq r_{1}^{\prime} and s 1 ≠ s 1 ′ s_{1}\neq s_{1}^{\prime} hold. Put r 1 ′′ = ( r 1 ′ − r 1) / gcd ⁡ ( r 1 − r 1 ′, s 1 − s 1 ′) r_{1}^{\prime\prime}=\left(r_{1}^{\prime}-r_{1}\right)/\gcd\left(r_{1}-r_{1}^{\prime},s_{1}-s_{1}^{\prime}\right) and s 1 ′′ = ( s 1 − s 1 ′) / gcd ⁡ ( r 1 − r 1 ′, s 1 − s 1 ′) s_{1}^{\prime\prime}=\left(s_{1}-s_{1}^{\prime}\right)/\gcd\left(r_{1}-r_{1}^{\prime},s_{1}-s_{1}^{\prime}\right), then λ = s 1 ′′ / r 1 ′′ \lambda=s_{1}^{\prime\prime}/r_{1}^{\prime\prime}.

We now use this information about λ \lambda to obtain a non-trivial linear relation between the b i b_{i} ’s whose coefficients we can bound.

We have λ ​ x 1 + μ ​ x 2 = s 1 ′′ / r 1 ′′ ​ ( r + t ​ β 1) + s + t ​ β 2 = c \lambda x_{1}+\mu x_{2}=s_{1}^{\prime\prime}/r_{1}^{\prime\prime}\left(r+t\beta_{1}\right)+s+t\beta_{2}=c (recalling that we take μ = 1 \mu=1). Expanding this and simplifying it, we obtain

 | s 1 ′′ ​ b 3 ​ r + ( s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2) ​ t + r 1 ′′ ​ b 3 ​ s = r 1 ′′ ​ b 3 ​ c, s_{1}^{\prime\prime}b_{3}r+\left(s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}\right)t+r_{1}^{\prime\prime}b_{3}s=r_{1}^{\prime\prime}b_{3}c, |  |

so we use Lemma 3.18 (b) with ( s 1 ′′ ​ b 3 / δ 1, ( s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2) / δ 1, r 1 ′′ ​ b 3 / δ 1, r 1 ′′ ​ b 3 ​ c / δ 1) \left(s_{1}^{\prime\prime}b_{3}/\delta_{1},\left(s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}\right)/\delta_{1},r_{1}^{\prime\prime}b_{3}/\delta_{1},r_{1}^{\prime\prime}b_{3}c/\delta_{1}\right) for ( A, B, C, D) (A,B,C,D), ( r, t, s) (r,t,s) for ( x, y, z) (x,y,z) and ( R 1, T 1, S 1) \left(R_{1},T_{1},S_{1}\right) for ( X, Y, Z) \left(X,Y,Z\right), where

 | δ 1 = gcd ⁡ ( s 1 ′′ ​ b 3, s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2, r 1 ′′ ​ b 3) = gcd ⁡ ( b 3, s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2) \delta_{1}=\gcd\left(s_{1}^{\prime\prime}b_{3},s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2},r_{1}^{\prime\prime}b_{3}\right)=\gcd\left(b_{3},s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}\right) |  |

since r 1 ′′ r_{1}^{\prime\prime} and s 1 ′′ s_{1}^{\prime\prime} are coprime. Here

 | | s 1 ′′ ​ b 3 / δ 1 | = | A | ≤ ( Y + 1) ​ ( Z + 1) ℳ − max ⁡ { Y, Z } ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, \left|s_{1}^{\prime\prime}b_{3}/\delta_{1}\right|=\left|A\right|\leq\frac{\left(Y+1\right)\left(Z+1\right)}{\mathcal{M}-\max\{Y,Z\}}\leq\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-\max\{S_{1},T_{1}\}}, |  |

 | | ( s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2) / δ 1 | = | B | ≤ ( X + 1) ​ ( Z + 1) ℳ − max ⁡ { X, Z } ≤ ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 } \left|\left(s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}\right)/\delta_{1}\right|=\left|B\right|\leq\frac{\left(X+1\right)\left(Z+1\right)}{\mathcal{M}-\max\{X,Z\}}\leq\frac{\left(R_{1}+1\right)\left(S_{1}+1\right)}{\mathcal{M}-\max\{R_{1},S_{1}\}} |  |

and

 | | r 1 ′′ ​ b 3 / δ 1 | = | C | ≤ ( X + 1) ​ ( Y + 1) ℳ − max ⁡ { X, Y } ≤ ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 }. \left|r_{1}^{\prime\prime}b_{3}/\delta_{1}\right|=\left|C\right|\leq\frac{\left(X+1\right)\left(Y+1\right)}{\mathcal{M}-\max\{X,Y\}}\leq\frac{\left(R_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-\max\{R_{1},T_{1}\}}. |  |

Since δ 1 \delta_{1} divides s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2 s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}, we have s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2 = k 1 ​ δ 1 s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}=k_{1}\delta_{1}. Multiplying this by b 3 / δ 1 b_{3}/\delta_{1}, we get a linear relation

 | u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = 0 u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=0 |  |

with u 1 = s 1 ′′ ​ b 3 / δ 1 u_{1}=s_{1}^{\prime\prime}b_{3}/\delta_{1}, u 2 = r 1 ′′ ​ b 3 / δ 1 u_{2}=r_{1}^{\prime\prime}b_{3}/\delta_{1} and u 3 = − ( s 1 ′′ b 1 + r 1 ′′ b 2) / δ 1 u_{3}=-\left(s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}\right)/\delta_{1}. Thus

 | | u 1 | \displaystyle\left|u_{1}\right| | = | s 1 ′′ ​ b 3 / δ 1 | ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, \displaystyle=\left|s_{1}^{\prime\prime}b_{3}/\delta_{1}\right|\leq\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-\max\{S_{1},T_{1}\}}, |  |

 | | u 2 | \displaystyle\left|u_{2}\right| | = | r 1 ′′ b 3 / δ 1 | ≤ ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 } and \displaystyle=\left|r_{1}^{\prime\prime}b_{3}/\delta_{1}\right|\leq\frac{\left(R_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-\max\{R_{1},T_{1}\}}\quad\text{and} |  |

 | | u 3 | \displaystyle\left|u_{3}\right| | = | ( s 1 ′′ ​ b 1 + r 1 ′′ ​ b 2) / δ 1 | ≤ ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 }. \displaystyle=\left|\left(s_{1}^{\prime\prime}b_{1}+r_{1}^{\prime\prime}b_{2}\right)/\delta_{1}\right|\leq\frac{\left(R_{1}+1\right)\left(S_{1}+1\right)}{\mathcal{M}-\max\{R_{1},S_{1}\}}. |  |

(b) For ( λ, μ) ∈ ℂ 2 ∖ { ( 0, 0) } (\lambda,\mu)\in\mathbb{C}^{2}\setminus\{(0,0)\}, we consider the cardinality

 | N = Card ⁡ { λ ​ x 1 + μ ​ x 2: ( x 1, x 2) ∈ Σ ~ 1 }. N=\card\left\{\lambda x_{1}+\mu x_{2}\,:\,\left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1}\right\}. |  |

Putting M = max c ∈ ℂ ⁡ M c M=\max_{c\in\mathbb{C}}M_{c}, we clearly have N ≥ Card ⁡ ( Σ ~ 1) / M N\geq\card\left(\widetilde{\Sigma}_{1}\right)/M, so part (b) of the lemma follows from the assumption in the lemma that

 | Card ⁡ Σ ~ 1 = ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) \card\widetilde{\Sigma}_{1}=\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right) |  |

and the assumption in part (b) that M ≤ ℳ M\leq\mathcal{M}. ∎

## 4. Proof of Main Result

We start by showing that we can apply our zero lemma, Proposition 3.11, to Δ \Delta, so that we have Δ ≠ 0 \Delta\neq 0. This will allow us to use Proposition 3.9 to obtain a lower bound for | Δ | \left|\Delta\right|.

If the N = K ⁡ ( K + 1) ​ L / 2 N=K(K+1)L/2 rows of the matrix used to define the interpolation determinant, Δ \Delta, in ( 2.6) are linearly dependent, then there exists a polynomial, P ⁡ ( X 1, X 2, Y) P\left(X_{1},X_{2},Y\right), not exactly zero, with P ⁡ ( r + t ​ β 1, s + t ​ β 2, α 1 r ​ α 2 s ​ α 3 t) = 0 P\left(r+t\beta_{1},s+t\beta_{2},\alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t}\right)=0 for all triples ( r, s, t) (r,s,t) with 0 ≤ r < R 0\leq r<R, 0 ≤ s < S 0\leq s<S and 0 ≤ t < T 0\leq t<T. Since this polynomial arises from a linear combination of the rows, the maximum exponent of r + t ​ β 1 r+t\beta_{1} plus the maximum exponent of s + t ​ β 2 s+t\beta_{2} is at most K − 1 K-1 and the maximum exponent of α 1 r ​ α 2 s ​ α 3 t \alpha_{1}^{r}\alpha_{2}^{s}\alpha_{3}^{t} is at most L − 1 L-1, deg X ¯ ⁡ ( P) ≤ K − 1 \deg_{\underline{X}}(P)\leq K-1 and deg Y ⁡ ( P) ≤ L − 1 \deg_{Y}(P)\leq L-1.

Using the definition of the Σ j \Sigma_{j} ’s in ( 3.21), along with the lower bounds for R R, S S and T T in ( 2.7), we use that the set of all such triples ( r, s, t) (r,s,t) contains Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3}. Therefore, if conditions ( 3.17), ( 3.18) and ( 3.19) in Proposition 3.11 hold, then we find that P ⁡ ( X 1, X 2, Y) P\left(X_{1},X_{2},Y\right) is the zero polynomial. This contradiction shows that the N = K ⁡ ( K + 1) ​ L / 2 N=K(K+1)L/2 rows of the matrix used to define the interpolation determinant, Δ \Delta, in ( 2.6) are not linearly dependent and hence the interpolation determinant, Δ \Delta, is not zero.

Thus, if we can show that conditions ( 2.9)–( 2.13) in the theorem imply conditions ( 3.17), ( 3.18) and ( 3.19) in Proposition 3.11 (unless conditions ( 2.14) or ( 2.15) hold), then by Proposition 3.10, the lower bound for Λ ′ \Lambda^{\prime} in the theorem will hold (again, unless conditions ( 2.14) or ( 2.15) hold).

Condition ( 3.17) of Proposition 3.11 has two subconditions. The first subcondition is

(4.1) |  | Card ⁡ { λ ​ x 1 + μ ​ x 2: ( x 1, x 2, y) ∈ Σ 1 } > K, ∀ ( λ, μ) ≠ ( 0, 0). \card\left\{\lambda x_{1}+\mu x_{2}\,:\,\left(x_{1},x_{2},y\right)\in\Sigma_{1}\right\}>K,\quad\forall(\lambda,\mu)\neq(0,0). |  |

Recalling the definition of Σ 1 \Sigma_{1} in ( 3.21) and of Σ 1 ~ \widetilde{\Sigma_{1}} in Lemma 3.17, we have

 | Card ⁡ { λ ​ x 1 + μ ​ x 2: ( x 1, x 2, y) ∈ Σ 1 } = Card ⁡ { λ ​ x 1 + μ ​ x 2: ( x 1, x 2) ∈ Σ ~ 1 }. \card\left\{\lambda x_{1}+\mu x_{2}\,:\,\left(x_{1},x_{2},y\right)\in\Sigma_{1}\right\}=\card\left\{\lambda x_{1}+\mu x_{2}\,:\,\left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1}\right\}. |  |

By Lemma 3.17, we find that Card ⁡ Σ ~ 1 = ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) \card\widetilde{\Sigma}_{1}=\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right) holds unless condition ( 2.14) holds. So we may now assume that Card ⁡ Σ ~ 1 = ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) \card\widetilde{\Sigma}_{1}=\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right) holds. Thus, by Lemma 3.21 (b), condition ( 2.9) of the theorem implies that

 | Card ⁡ { λ ​ x 1 + μ ​ x 2: ( x 1, x 2) ∈ Σ ~ 1 } > K, ∀ ( λ, μ) ≠ ( 0, 0). \card\left\{\lambda x_{1}+\mu x_{2}\,:\,\left(x_{1},x_{2}\right)\in\widetilde{\Sigma}_{1}\right\}>K,\quad\forall(\lambda,\mu)\neq(0,0). |  |

holds, unless the condition in Lemma 3.21 (a) holds. This condition in Lemma 3.21 (a) gives rise to condition ( 2.15).

The second subcondition of condition ( 3.17) of Proposition 3.11 is

(4.2) |  | Card ⁡ { y: ( x 1, x 2, y) ∈ Σ 1 } > L. \card\left\{y\,:\,\left(x_{1},x_{2},y\right)\in\Sigma_{1}\right\}>L. |  |

Condition ( 2.10) in this theorem implies that this subcondition holds.

So we have shown that condition ( 3.17) of Proposition 3.11 follows from conditions ( 2.9) and ( 2.10) in this theorem, provided that conditions ( 2.14) and ( 2.15) do not hold.

We now consider condition ( 3.18) of Proposition 3.11.

It is also divided into two subconditions. We replace the first one by the stronger condition

(4.3) |  | Card ⁡ { y: ( x 1, x 2, y) ∈ Σ 2 } > 2 ​ K ​ L. \card\left\{y:\left(x_{1},x_{2},y\right)\in\Sigma_{2}\right\}>2KL. |  |

Condition ( 2.11) in this theorem implies that this subcondition holds.

The second subcondition of condition ( 3.18) of Proposition 3.11 is

(4.4) |  | Card ⁡ { ( x 1, x 2): ( x 1, x 2, y) ∈ Σ 2 } > K 2. \card\left\{\left(x_{1},x_{2}\right):\left(x_{1},x_{2},y\right)\in\Sigma_{2}\right\}>K^{2}. |  |

By Lemma 3.17, Card ⁡ { ( x 1, x 2): ( x 1, x 2, y) ∈ Σ 2 } = ( R 2 + 1) ​ ( S 2 + 1) ​ ( T 2 + 1) \card\left\{\left(x_{1},x_{2}\right)\,:\,\left(x_{1},x_{2},y\right)\in\Sigma_{2}\right\}=\left(R_{2}+1\right)\left(S_{2}+1\right)\left(T_{2}+1\right) holds unless condition ( 2.14) holds. So condition ( 2.12) in this theorem implies that this subcondition holds unless condition ( 2.14) holds.

Condition ( 3.19) of Proposition 3.11 is that Card ⁡ Σ 3 > 3 ​ K 2 ​ L \card\Sigma_{3}>3K^{2}L. From the definition of w w, if Λ ∈ i ​ π ​ ℚ \Lambda\in i\pi\mathbb{Q}, then Λ = i ​ π ​ 2 ​ p / q \Lambda=i\pi 2p/q where p ≠ 0 p\neq 0 and 0 < | q | ≤ w 0<|q|\leq w. So, from the assumption in this theorem that 0 < | Λ | < 2 ​ π / w 0<\left|\Lambda\right|<2\pi/w, it follows that Λ ∉ i ​ π ​ ℚ \Lambda\not\in i\pi\mathbb{Q}. Thus the map in Lemma 3.15 (a) is injective, so hypothesis ( 2.13) of the theorem implies condition ( 3.19) of Proposition 3.11 holds. This finishes the proof.

## 5. How to use Theorem 2.1

We will first consider the multiplicative group generated by the three algebraic numbers α 1 \alpha_{1}, α 2 \alpha_{2} and α 3 \alpha_{3}, which we will denote by 𝒢 \mathcal{G}.

### 5.1. About the multiplicative group 𝒢 \mathcal{G}

In practical examples, generally the following condition holds:

(5.1) |  | { either α 1, α 2 and α 3 are multiplicatively independent, or two of them are multiplicatively independent and the third is a root of unity ≠ 1. \begin{cases}\text{either $\alpha_{1}$, $\alpha_{2}$ and $\alpha_{3}$ are multiplicatively independent, or}\\ \text{two of them are multiplicatively independent and the third is a root of unity $\neq 1$.}\end{cases} |  |

We now use hypothesis ( 5.1), which is clearly stronger than the standard hypothesis that the multiplicative group 𝒢 \mathcal{G} is of rank at least two. We also notice that the order in ℂ × \mathbb{C}^{\times} of a root of unity ≠ 1 {}\neq 1 is at least equal to 2 2, thus the condition ( 4.2) is satisfied if

(5.2) |  | 2 ​ ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) W 1 + 1 > L, \frac{2(R_{1}+1)(S_{1}+1)(T_{1}+1)}{W_{1}+1}>L, |  |

where

 | W 1 = { R 1, if α 1 is a root of unity, S 1, if α 2 is a root of unity, T 1, if α 3 is a root of unity, 1, otherwise, W_{1}=\begin{cases}R_{1},&\text{if $\alpha_{1}$ is a root of unity},\\ S_{1},&\text{if $\alpha_{2}$ is a root of unity},\\ T_{1},&\text{if $\alpha_{3}$ is a root of unity},\\ 1,&\text{otherwise},\end{cases} |  |

and recalling the definition of the Σ j \Sigma_{j} ’s in ( 3.21). But see also the first remark after ( 5.3) below.

In the same way, we see that to satisfy the condition ( 4.3) it is enough to suppose that (when condition ( 5.1) holds)

(5.3) |  | ( R 2 + 1) ​ ( S 2 + 1) ​ ( T 2 + 1) W 2 + 1 > K ​ L, \frac{\left(R_{2}+1\right)\left(S_{2}+1\right)\left(T_{2}+1\right)}{W_{2}+1}>KL, |  |

where W 2 W_{2} is defined by

 | W 2 = { R 2, if α 1 is a root of unity, S 2, if α 2 is a root of unity, T 2, if α 3 is a root of unity, 1, otherwise. W_{2}=\begin{cases}R_{2},&\text{if $\alpha_{1}$ is a root of unity,}\\ S_{2},&\text{if $\alpha_{2}$ is a root of unity,}\\ T_{2},&\text{if $\alpha_{3}$ is a root of unity,}\\ 1,&\text{otherwise}.\end{cases} |  |

###### Remark.

When (for example) α 3 \alpha_{3} is a root of unity of order ν \nu, condition ( 5.2) above can be replaced by

 | ν ⁡ ( R 1 + 1) ​ ( S 1 + 1) > L \nu\left(R_{1}+1\right)\left(S_{1}+1\right)>L |  |

(provided T 1 ≥ ν − 1 T_{1}\geq\nu-1) and condition ( 5.3) can be replaced by

 | ν ⁡ ( R 2 + 1) ​ ( S 2 + 1) > K ​ L \nu\left(R_{2}+1\right)\left(S_{2}+1\right)>KL |  |

(provided T 2 ≥ ν − 1 T_{2}\geq\nu-1).

###### Remark.

Under a weaker condition, one can obtain similar (but slightly weaker) conclusions (see, for instance, [31, Ex. 7.5, p. 229]).

### 5.2. The choice of parameters

Here we assume that condition ( 5.1) holds, then by Lemma 3.16 above we know that Λ ∉ i ​ π ​ ℚ \Lambda\not\in i\pi\mathbb{Q}.

To apply Theorem 2.1, we consider an integer L ≥ 5 L\geq 5 and real parameters m > 0 m>0, ρ ≥ 2 \rho\geq 2 and χ > 0 \chi>0. Note that having chosen ρ \rho, we can set the values of the a i a_{i} ’s too.

Now we put

(5.4) |  | K = ⌊ m ​ L ​ a 1 ​ a 2 ​ a 3 ⌋. K=\lfloor mLa_{1}a_{2}a_{3}\rfloor. |  |

The reason for this choice of K K is as follows. The main term on the left-hand side of equation ( 2.8) is K ​ L ​ log ⁡ ( ρ) / 2 KL\log(\rho)/2, so it must be larger than 𝒟 ⁡ ( K − 1) ​ log ⁡ ( b) \mathcal{D}(K-1)\log(b). This suggests that we let L = O ⁡ ( 𝒟 ​ log ⁡ ( b) / log ⁡ ( ρ)) L=O\left(\mathcal{D}\log(b)/\log(\rho)\right). Thus our lower bound for log ⁡ | Λ | \log\left|\Lambda\right|, which is − log ⁡ ( ρ) ​ K ​ L -\log(\rho)KL, is O ⁡ ( a 1 ​ a 2 ​ a 3 ​ 𝒟 2 ​ log 2 ⁡ ( b) / log ⁡ ( ρ)) O\left(a_{1}a_{2}a_{3}\mathcal{D}^{2}\log^{2}(b)/\log(\rho)\right). This is our desired form and consistent with the bounds for linear forms in two logs that we obtain from this same technique (see, for example, [20, 19]).

We will also assume that

 | m ≥ 1 and Ω:= a 1 ​ a 2 ​ a 3 ≥ 2. m\geq 1\quad\text{and}\quad\Omega:=a_{1}a_{2}a_{3}\geq 2. |  |

We define

 | R 1 \displaystyle R_{1} | = ⌊ c 1 ​ a 2 ​ a 3 ⌋, \displaystyle=\lfloor c_{1}a_{2}a_{3}\rfloor, | S 1 \displaystyle S_{1} | = ⌊ c 1 ​ a 1 ​ a 3 ⌋, \displaystyle=\lfloor c_{1}a_{1}a_{3}\rfloor, | T 1 \displaystyle T_{1} | = ⌊ c 1 ​ a 1 ​ a 2 ⌋, \displaystyle=\lfloor c_{1}a_{1}a_{2}\rfloor, |  |

(5.5) |  | R 2 \displaystyle R_{2} | = ⌊ c 2 ​ a 2 ​ a 3 ⌋, \displaystyle=\lfloor c_{2}a_{2}a_{3}\rfloor, | S 2 \displaystyle S_{2} | = ⌊ c 2 ​ a 1 ​ a 3 ⌋, \displaystyle=\lfloor c_{2}a_{1}a_{3}\rfloor, | T 2 \displaystyle T_{2} | = ⌊ c 2 ​ a 1 ​ a 2 ⌋, \displaystyle=\lfloor c_{2}a_{1}a_{2}\rfloor, |  |

 | R 3 \displaystyle R_{3} | = ⌊ c 3 ​ a 2 ​ a 3 ⌋, \displaystyle=\lfloor c_{3}a_{2}a_{3}\rfloor, | S 3 \displaystyle S_{3} | = ⌊ c 3 ​ a 1 ​ a 3 ⌋, \displaystyle=\lfloor c_{3}a_{1}a_{3}\rfloor, | T 3 \displaystyle T_{3} | = ⌊ c 3 ​ a 1 ​ a 2 ⌋, \displaystyle=\lfloor c_{3}a_{1}a_{2}\rfloor, |  |

where the parameters c 1 c_{1}, c 2 c_{2} and c 3 c_{3} will be chosen so that conditions ( 2.9) through ( 2.13) of Theorem 2.1 are satisfied. The motivation for this choice of these quantities is so that all three terms in a 1 ​ R + a 2 ​ S + a 3 ​ T a_{1}R+a_{2}S+a_{3}T on the right-hand side of equation ( 2.8) are roughly the same size, O ⁡ ( a 1 ​ a 2 ​ a 3) O\left(a_{1}a_{2}a_{3}\right), and so that the g ​ L ​ ( a 1 ​ R + a 2 ​ S + a 3 ​ T) gL\left(a_{1}R+a_{2}S+a_{3}T\right) term on the right-hand side of ( 2.8) is roughly the same size as the other main term on the right-hand side of ( 2.8), 𝒟 ⁡ ( K − 1) ​ log ⁡ b \mathcal{D}(K-1)\log b.

We first consider condition ( 2.9) of Theorem 2.1. Recalling that 𝒱 = ( ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1)) 1 / 2 \mathcal{V}=\left(\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)\right)^{1/2}, we see that ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) > K ​ χ ​ 𝒱 \left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)>K\chi\mathcal{V} holds, if ( c 1 3 ​ ( a 1 ​ a 2 ​ a 3) 2) 1 / 2 ≥ χ ​ m ​ a 1 ​ a 2 ​ a 3 ​ L \left(c_{1}^{3}\left(a_{1}a_{2}a_{3}\right)^{2}\right)^{1/2}\geq\chi ma_{1}a_{2}a_{3}L. I.e., c 1 ≥ ( χ ​ m ​ L) 2 / 3 c_{1}\geq(\chi mL)^{2/3}.

Next we establish conditions for

 | ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) > K ⋅ max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1 } \left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)>K\cdot\max\left\{R_{1}+S_{1}+1,S_{1}+T_{1}+1,R_{1}+T_{1}+1\right\} |  |

to hold. We consider the special case a 1 ≤ a 2 ≤ a 3 a_{1}\leq a_{2}\leq a_{3} (the other cases are the same), then T 1 ≤ S 1 ≤ R 1 T_{1}\leq S_{1}\leq R_{1} and we want to show that

 | ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1) > K ⁡ ( R 1 + S 1 + 1). \left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)>K\left(R_{1}+S_{1}+1\right). |  |

Using the expressions for these quantities, this inequality will hold if

 | ( R 1 + 1) ​ c 1 2 ​ a 1 2 ​ a 2 ​ a 3 > m ​ L ​ a 1 ​ a 2 ​ a 3 ​ ( R 1 + 1 + c 1 ​ a 1 ​ a 3) \left(R_{1}+1\right)c_{1}^{2}a_{1}^{2}a_{2}a_{3}>mLa_{1}a_{2}a_{3}\left(R_{1}+1+c_{1}a_{1}a_{3}\right) |  |

holds. If a ​ x > b ​ x + c ax>bx+c with a, b, c > 0 a,b,c>0 holds for x = x 0 x=x_{0}, then it holds for all x ≥ x 0 x\geq x_{0}. So it suffices to show that c 1 3 ​ a 1 2 ​ a 2 2 ​ a 3 2 ≥ m ​ L ​ a 1 ​ a 2 ​ a 3 ​ ( c 1 ​ a 2 ​ a 3 + c 1 ​ a 1 ​ a 3) c_{1}^{3}a_{1}^{2}a_{2}^{2}a_{3}^{2}\geq mLa_{1}a_{2}a_{3}\left(c_{1}a_{2}a_{3}+c_{1}a_{1}a_{3}\right) holds. This will hold if c 1 2 ​ a 1 2 ​ a 2 2 ​ a 3 2 ≥ 2 ​ m ​ L ​ Ω 2 ​ ( a 1 − 1 + a 2 − 1) c_{1}^{2}a_{1}^{2}a_{2}^{2}a_{3}^{2}\geq 2mL\Omega^{2}\left(a_{1}^{-1}+a_{2}^{-1}\right) holds. That is, when c 1 2 ≥ ( a 1 − 1 + a 2 − 1) ​ m ​ L c_{1}^{2}\geq\left(a_{1}^{-1}+a_{2}^{-1}\right)mL holds. In the general case, the wanted condition holds if

 | c 1 2 ≥ ( a − 1 + a ′ − 1) ​ m ​ L, where ​ a = min ⁡ { a 1, a 2, a 3 } ​ and ​ a ′ = min ⁡ ( { a 1, a 2, a 3 } ∖ { a }). c_{1}^{2}\geq\left(a^{-1}+a^{\prime-1}\right)mL,\quad\text{ where}\ a=\min\left\{a_{1},a_{2},a_{3}\right\}\text{ and }\ a^{\prime}=\min\left(\left\{a_{1},a_{2},a_{3}\right\}\setminus\{a\}\right). |  |

Condition ( 2.10) of Theorem 2.1 holds when 2 ​ c 1 2 ​ a 1 ​ a 2 ​ a 3 ⋅ min ⁡ { a 1, a 2, a 3 } = 2 ​ c 1 2 ​ Ω ​ a > L 2c_{1}^{2}a_{1}a_{2}a_{3}\cdot\min\left\{a_{1},a_{2},a_{3}\right\}=2c_{1}^{2}\Omega a>L, provided that c 1 > 2 1 / 3 c_{1}>2^{1/3} (since Ω ≥ 2 \Omega\geq 2). This inequality arises from the second part of ( 5.1), with the factor of 2 2 on the left-hand side coming from the fact that the order of the root of unity is at least 2 2. The condition that c 1 > 2 1 / 3 c_{1}>2^{1/3} ensures that condition ( 2.10) also holds when the first part of ( 5.1) holds.

Thus, since we suppose m ≥ 1 m\geq 1 and also Ω ≥ 2 \Omega\geq 2, we can take

(5.6) |  | c 1 = max ⁡ { 2 1 / 3, ( χ ​ m ​ L) 2 / 3, ( 2 ​ m ​ L a) 1 / 2 }. c_{1}=\max\left\{2^{1/3},(\chi mL)^{2/3},\left(\frac{2mL}{a}\right)^{1/2}\right\}. |  |

Our treatment of condition ( 2.11) of Theorem 2.1 is very similar to that for condition ( 2.10). We want 2 ​ c 2 2 ​ Ω > 2 ​ K ​ L 2c_{2}^{2}\Omega>2KL. Thus c 2 = m / a ​ L c_{2}=\sqrt{m/a}\,L.

To satisfy condition ( 2.12) of Theorem 2.1, we need

 | ( R 2 + 1) ​ ( S 2 + 1) ​ ( T 2 + 1) > K 2. \left(R_{2}+1\right)\left(S_{2}+1\right)\left(T_{2}+1\right)>K^{2}. |  |

Using our expressions above, this will hold if c 2 3 > m 2 ​ L 2 c_{2}^{3}>m^{2}L^{2}.

Combining these two expressions for c 2 c_{2}, we require

(5.7) |  | c 2 = max ⁡ { ( m ​ L) 2 / 3, m / a ​ L }. c_{2}=\max\left\{(mL)^{2/3},\sqrt{m/a}\,L\right\}. |  |

Note we do not require c 2 ≥ 2 1 / 3 c_{2}\geq 2^{1/3} here explicitly, since m ≥ 1 m\geq 1 and L ≥ 5 L\geq 5 ensures that ( m ​ L) 2 / 3 > 2 1 / 3 (mL)^{2/3}>2^{1/3}.

Finally, because of the hypothesis in ( 5.1), we have Λ ∉ i ​ π ​ ℚ \Lambda\not\in i\pi\mathbb{Q} by Lemma 3.16. So, by Lemma 3.15, condition ( 2.13) of Theorem 2.1 holds for

(5.8) |  | c 3 = ( 3 ​ m 2) 1 / 3 ​ L. c_{3}=\left(3m^{2}\right)^{1/3}L. |  |

###### Remark.

When α 1 \alpha_{1}, α 2 \alpha_{2}, α 3 \alpha_{3} are multiplicatively independent then it is enough to take c 1 c_{1} and c 3 c_{3} as above and

(5.9) |  | c 2 = ( m ​ L) 2 / 3. c_{2}=(mL)^{2/3}. |  |

### 5.3. The degenerate case

In this subsection, we present some informal arguments for what happens in the degenerate case. We obtain

 | log ⁡ | Λ | ≫ − a 1 ​ a 2 ​ a 3 ​ min ⁡ { a 1, a 2, a 3 } ​ ( 𝒟 ​ log ⁡ B) 8 / 3. \log\left|\Lambda\right|\gg-a_{1}a_{2}a_{3}\min\left\{a_{1},a_{2},a_{3}\right\}(\mathcal{D}\log B)^{8/3}. |  |

###### Remark.

It is this worse dependence on log ⁡ B \log B than in the non-degenerate case that leads to the degenerate case having an impact on the results obtained in practice. Fortunately, it is the constants that are important and our estimates should lead to good results when compared to published previously ones (e.g., [22]). See the examples in the next section for evidence of this.

From condition ( 2.14) in Theorem 2.1, we have

 | b 1 ≤ max { R 1, R 2 }, b 2 ≤ max { S 1, S 2 } and b 3 ≤ max { T 1, T 2 }. b_{1}\leq\max\left\{R_{1},R_{2}\right\},\quad b_{2}\leq\max\left\{S_{1},S_{2}\right\}\quad\text{and }\quad b_{3}\leq\max\left\{T_{1},T_{2}\right\}. |  |

We now focus our attention on condition ( 2.15). In the remainder of this subsection we put χ = 1 \chi=1. We have

 | u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = 0, u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=0, |  |

with

 | | u 1 | ≤ ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, | u 2 | ≤ ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 } and | u 3 | ≤ ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 } \left|u_{1}\right|\leq\frac{(S_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{S_{1},T_{1}\}},\quad\left|u_{2}\right|\leq\frac{(R_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{R_{1},T_{1}\}}\quad\text{and}\quad\left|u_{3}\right|\leq\frac{(R_{1}+1)(S_{1}+1)}{\mathcal{M}-\max\{R_{1},S_{1}\}} |  |

where

 | ℳ = max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1, χ ​ 𝒱 }. \mathcal{M}=\max\left\{R_{1}+S_{1}+1,S_{1}+T_{1}+1,R_{1}+T_{1}+1,\chi\mathcal{V}\right\}. |  |

This essentially implies that

 | | u 1 | ≤ c 1 a 1 / χ, | u 2 | ≤ c 1 a 2 / χ and | u 3 | ≤ c 1 a 3 / χ, \left|u_{1}\right|\leq\sqrt{c_{1}}a_{1}/\chi,\quad\left|u_{2}\right|\leq\sqrt{c_{1}}a_{2}/\chi\quad\text{and}\quad\left|u_{3}\right|\leq\sqrt{c_{1}}a_{3}/\chi, |  |

since R 1 ≈ c 1 ​ a 2 ​ a 3 R_{1}\approx c_{1}a_{2}a_{3}, S 1 ≈ c 1 ​ a 1 ​ a 3 S_{1}\approx c_{1}a_{1}a_{3}, T 1 ≈ c 1 ​ a 1 ​ a 2 T_{1}\approx c_{1}a_{1}a_{2} and typically ℳ = χ ​ 𝒱 ≈ χ ​ c 1 3 / 2 ​ a 1 ​ a 2 ​ a 3 \mathcal{M}=\chi\mathcal{V}\approx\chi c_{1}^{3/2}a_{1}a_{2}a_{3}.

Suppose we eliminate b 1 b_{1}. Then

 | u 1 ​ Λ = u 1 ​ b 1 ​ log ​ α 1 + u 1 ​ b 2 ​ log ​ α 2 + u 1 ​ b 3 ​ log ​ α 3 = b 2 ​ ( − u 2 ​ log ​ α 1 + u 1 ​ log ​ α 2) + b 3 ​ ( u 1 ​ log ​ α 3 − u 3 ​ log ​ α 1). u_{1}\Lambda=u_{1}b_{1}\log\alpha_{1}+u_{1}b_{2}\log\alpha_{2}+u_{1}b_{3}\log\alpha_{3}=b_{2}\left(-u_{2}\log\alpha_{1}+u_{1}\log\alpha_{2}\right)+b_{3}\left(u_{1}\log\alpha_{3}-u_{3}\log\alpha_{1}\right). |  |

Applying [20] to this linear form in two logs we get

 | − log ⁡ | Λ | ≪ ( | u 1 | ​ a 2 + | u 2 | ​ a 1) ​ ( | u 1 | ​ a 3 + | u 3 | ​ a 1) ​ 𝒟 2 ​ log 2 ​ B, -\log\left|\Lambda\right|\ll\left(\left|u_{1}\right|a_{2}+\left|u_{2}\right|a_{1}\right)\left(\left|u_{1}\right|a_{3}+\left|u_{3}\right|a_{1}\right)\mathcal{D}^{2}\log^{2}B, |  |

where (being somewhat pessimistic) B = max ⁡ { | b 1 |, | b 2 |, | b 3 | } B=\max\left\{\left|b_{1}\right|,\left|b_{2}\right|,\left|b_{3}\right|\right\}, and the implied constant is an absolute constant. Using the upper bounds for the | u 1 | \left|u_{1}\right| ’s, we get

 | − log ⁡ | Λ | ≪ ( c 1 ​ a 1 ​ a 2 / χ) ​ ( c 1 ​ a 1 ​ a 3 / χ) ​ 𝒟 2 ​ log 2 ​ B ≪ a 1 2 ​ a 2 ​ a 3 ​ L 2 / 3 ​ 𝒟 2 ​ log 2 ​ B / χ 2, -\log\left|\Lambda\right|\ll\left(\sqrt{c_{1}}a_{1}a_{2}/\chi\right)\left(\sqrt{c_{1}}a_{1}a_{3}/\chi\right)\mathcal{D}^{2}\log^{2}B\ll a_{1}^{2}a_{2}a_{3}L^{2/3}\mathcal{D}^{2}\log^{2}B/\chi^{2}, |  |

since we have c 1 ≪ L 2 / 3 c_{1}\ll L^{2/3}. Recalling that L = O ⁡ ( 𝒟 ​ log ⁡ B) L=O\left(\mathcal{D}\log B\right), we get

 | − log ⁡ | Λ | ≪ a 1 2 ​ a 2 ​ a 3 ​ ( 𝒟 ​ log ⁡ B) 8 / 3, -\log\left|\Lambda\right|\ll a_{1}^{2}a_{2}a_{3}(\mathcal{D}\log B)^{8/3}, |  |

where the implied constant is again absolute.

In the two remaining cases, where we eliminate b 2 b_{2} or b 3 b_{3}, the argument is identical and we obtain similar results:

 | − log ⁡ | Λ | ≪ a 1 ​ a 2 ​ a 3 ​ a i ​ ( 𝒟 ​ log ⁡ B) 8 / 3, -\log\left|\Lambda\right|\ll a_{1}a_{2}a_{3}a_{i}(\mathcal{D}\log B)^{8/3}, |  |

where we eliminate b i b_{i}. This suggests eliminating b i b_{i} where a i = min ⁡ { a 1, a 2, a 3 } a_{i}=\min\left\{a_{1},a_{2},a_{3}\right\}. This choice works best in our examples below too.

Of course, one could use [22] (or any log ⁡ B \log B type lower bound) instead of [20]. This would lead to a lower bound for log ⁡ | Λ | \log\left|\Lambda\right| with ( log ⁡ B) 5 / 3 (\log B)^{5/3} instead of ( log ⁡ B) 8 / 3 (\log B)^{8/3}. However, it would also lead to a much larger constant and it is that constant that is more important than the dependence on B B for our use here.

## 6. Examples

To demonstrate how to use our kit, we give two examples here, revisiting the linear forms in three logs that arose in [9] and [10].

These examples also provide comparison for readers. In both [9] and [10], the authors used earlier versions of our kit due to the first author (see Section 12 of [9] and Section 14 of [10]). In the first example [9], the authors showed that if y p = F n y^{p}=F_{n}, then p < 197 ⋅ 10 6 p<197\cdot 10^{6}. Here we obtain p < 18 ⋅ 10 6 p<18\cdot 10^{6}, roughly 11 11 times smaller than the bound in [9]. For the second example, we improve the upper bound in [10] as well as correct mistakes in [10].

We start with the following sharpening of Lemma 2.2 of [25] that we will use throughout this section and in our code. In fact, it is explicit in their proof. Roughly speaking, it removes the factor of 2 h 2^{h} from their result, yielding bounds very close to the actual largest solution.

###### Lemma 6.1.

Let a ≥ 0 a\geq 0, h ≥ 1 h\geq 1 and b > ( 1 / h) h b>\left(1/h\right)^{h} be real numbers and let x ∈ ℝ x\in\mathbb{R} be the largest solution of x = a + b ​ ( log ⁡ x) h x=a+b\left(\log x\right)^{h}. Put c = h ​ b 1 / h c=hb^{1/h}. Then,

 | x < ( c ​ log ⁡ c + log ⁡ c log ⁡ ( c) − 1 ​ ( a 1 / h + c ​ log ⁡ log ⁡ c)) h. x<\left(c\log c+\frac{\log c}{\log(c)-1}\left(a^{1/h}+c\log\log c\right)\right)^{h}. |  |

###### Proof.

This is the inequality on the second-last line of the proof of Lemma 2.2 of [25] with a weaker condition on b b, so we reprove their lemma to justify this weaker condition.

Since h ≥ 1 h\geq 1, we know that ( z 1 + z 2) 1 / h ≤ z 1 1 / h + z 2 1 / h \left(z_{1}+z_{2}\right)^{1/h}\leq z_{1}^{1/h}+z_{2}^{1/h} for any positive real numbers, z 1 z_{1} and z 2 z_{2}. Applying this to our expression for x x, we obtain

 | x 1 / h ≤ a 1 / h + c ​ log ⁡ ( x 1 / h), x^{1/h}\leq a^{1/h}+c\log\left(x^{1/h}\right), |  |

where c = h ​ b 1 / h c=hb^{1/h}, provided a > 0 a>0, c > 0 c>0 and x > 1 x>1. Put x 1 / h = ( 1 + y) ​ c ​ log ⁡ ( c) x^{1/h}=(1+y)c\log(c). We also have c ​ log ⁡ ( x 1 / h) ≤ x 1 / h c\log\left(x^{1/h}\right)\leq x^{1/h} under these conditions. Hence c ​ log ⁡ ( c) + c ​ log ⁡ log ⁡ ( x 1 / h) ≤ x 1 / h c\log(c)+c\log\log\left(x^{1/h}\right)\leq x^{1/h}. So as long as x > e h x>e^{h} and log ⁡ ( c) > 0 \log(c)>0, we have y > 0 y>0 above.

Thus

 | ( 1 + y) ​ c ​ log ⁡ ( c) \displaystyle(1+y)c\log(c) | = x 1 / h ≤ a 1 / h + c ​ log ⁡ ( 1 + y) + c ​ log ⁡ ( c) + c ​ log ⁡ log ⁡ ( c) \displaystyle=x^{1/h}\leq a^{1/h}+c\log(1+y)+c\log(c)+c\log\log(c) |  |

 |  | ≤ a 1 / h + c ​ y + c ​ log ⁡ ( c) + c ​ log ⁡ log ⁡ ( c). \displaystyle\leq a^{1/h}+cy+c\log(c)+c\log\log(c). |  |

Hence

 | y ​ c ​ ( log ⁡ ( c) − 1) < a 1 / h + c ​ log ⁡ log ⁡ ( c). yc\left(\log(c)-1\right)<a^{1/h}+c\log\log(c). |  |

The upper bound for x x in our lemma now follows, as in the proof of Lemma 2.2 of [25] except that the condition c > e 2 c>e^{2} is not needed here. ∎

### 6.1. Example 1: y p = F n y^{p}=F_{n}

###### Theorem 6.2.

If y p = F n y^{p}=F_{n} has a solution for an odd prime p p and y > 1 y>1, then

(6.1) |  | p < 18 ⋅ 10 6. p<18\cdot 10^{6}. |  |

###### Proof.

Following Section 13 of [9], we suppose that y p = F n y^{p}=F_{n}. From Proposition 10.1 of [9], we have

(6.2) |  | log ⁡ y > 10 20. \log y>10^{20}. |  |

Here we will suppose that p > 10 ⋅ 10 6 p>10\cdot 10^{6}, rather than p > 2 ⋅ 10 8 p>2\cdot 10^{8} in [9]. The reason for this weaker bound on p p is to accommodate the improved upper bound we obtain here. We will also use the principal branch of the logarithm throughout the proof.

Step (1): Linear form definition and upper bound

We now define the linear form in logs we will use and obtain an upper bound for it.

In Section 13 of [9], on page 1013, the authors consider

 | Λ = n ​ log ⁡ ( ω) − log ⁡ 5 − p ​ log ⁡ ( y), \Lambda=n\log(\omega)-\log\sqrt{5}-p\log(y), |  |

which they rewrite as

 | Λ = p ​ log ⁡ ( ω k / y) − q ​ log ⁡ ( ω) − log ⁡ 5. \Lambda=p\log\left(\omega^{k}/y\right)-q\log(\omega)-\log\sqrt{5}. |  |

Notice that − Λ -\Lambda is in the form we consider in ( 2.1).

Here ω = ( 1 + 5) / 2 \omega=\left(1+\sqrt{5}\right)/2 and n = k ​ p − q n=kp-q with 0 ≤ q < p 0\leq q<p. Note that if q = 0 q=0, then Λ \Lambda is a linear form in two logs and we obtain a much better upper bound on p p.

They also state (see the start of the proof of Proposition 11.1 on page 1000 or the start of Section 13 on page 1013) that

(6.3) |  | log ⁡ | Λ | < − 2 ​ p ​ log ⁡ ( y) + 1. \log\left|\Lambda\right|<-2p\log(y)+1. |  |

Step (2): Matveev

In the notation of Theorem 3.1, we have D = 2 D=2, α 1 = ω k / y \alpha_{1}=\omega^{k}/y, α 2 = ω \alpha_{2}=\omega, α 3 = 5 \alpha_{3}=\sqrt{5}, b 1 = p b_{1}=p, b 2 = − q > − p b_{2}=-q>-p and b 3 = 1 b_{3}=1.

Recall that A j ≥ max ⁡ { D ​ h ⁡ ( α j), | log ⁡ α j | } A_{j}\geq\max\left\{D\h\left(\alpha_{j}\right),\left|\log\alpha_{j}\right|\right\}. Thus, we can take A 2 = log ⁡ ( ω) A_{2}=\log(\omega) and A 3 = log ⁡ ( 5) A_{3}=\log(5). For A 1 A_{1}, we need a little more work.

From the first expression above for Λ \Lambda and ( 6.3), we have

 | log ⁡ 5 p − e p ​ y 2 ​ p < n p ​ log ⁡ ( ω) − log ⁡ ( y) < log ⁡ 5 p − e p ​ y 2 ​ p. \frac{\log\sqrt{5}}{p}-\frac{e}{py^{2p}}<\frac{n}{p}\log(\omega)-\log(y)<\frac{\log\sqrt{5}}{p}-\frac{e}{py^{2p}}. |  |

Applying n = k ​ p − q n=kp-q and using 0 ≤ q ≤ p − 1 0\leq q\leq p-1, we have

 | 0 < log ⁡ 5 p − e p ​ y 2 ​ p ≤ q p ​ log ⁡ ( ω) + log ⁡ 5 p − e p ​ y 2 ​ p \displaystyle 0<\frac{\log\sqrt{5}}{p}-\frac{e}{py^{2p}}\leq\frac{q}{p}\log(\omega)+\frac{\log\sqrt{5}}{p}-\frac{e}{py^{2p}} | < k ​ log ⁡ ( ω) − log ⁡ ( y) < q p ​ log ⁡ ( ω) + log ⁡ 5 p + e p ​ y 2 ​ p \displaystyle<k\log(\omega)-\log(y)<\frac{q}{p}\log(\omega)+\frac{\log\sqrt{5}}{p}+\frac{e}{py^{2p}} |  |

 |  | ≤ log ⁡ ( ω) − 1 p ​ log ⁡ ( ω) + log ⁡ 5 p + e p ​ y 2 ​ p ≤ log ⁡ ( ω) + 1 3 ​ p. \displaystyle\leq\log(\omega)-\frac{1}{p}\log(\omega)+\frac{\log\sqrt{5}}{p}+\frac{e}{py^{2p}}\leq\log(\omega)+\frac{1}{3p}. |  |

Hence

(6.4) |  | | log ⁡ ( ω k / y) | = log ⁡ | ω k / y | < log ⁡ ( ω) + 10 − 6, \left|\log\left(\omega^{k}/y\right)\right|=\log\left|\omega^{k}/y\right|<\log(\omega)+10^{-6}, |  |

since p > 10 ⋅ 10 6 p>10\cdot 10^{6}.

The conjugate of ω k / y \omega^{k}/y is ω − k / y < 1 \omega^{-k}/y<1, so h ⁡ ( ω k / y) = ( 2 ​ log ⁡ ( y) + k ​ log ⁡ ( ω) − log ⁡ ( y)) / 2 = ( k / 2) ​ log ⁡ ( ω) + ( 1 / 2) ​ log ⁡ ( y) \h\left(\omega^{k}/y\right)=(2\log(y)+k\log(\omega)-\log(y))/2=(k/2)\log(\omega)+(1/2)\log(y) (the 2 ​ log ⁡ ( y) 2\log(y) is because we need a factor of y 2 y^{2} to clear the denominator in the minimal polynomial of ω k / y \omega^{k}/y). From ( 6.4), we have k ​ log ⁡ ( ω) < log ⁡ ( ω) + log ⁡ ( y) + 10 − 6 k\log(\omega)<\log(\omega)+\log(y)+10^{-6}, so

(6.5) |  | h ⁡ ( α 1) = h ⁡ ( ω k / y) < ( 1 / 2) ​ log ⁡ ( ω) + log ⁡ ( y) + 10 − 6 \h\left(\alpha_{1}\right)=\h\left(\omega^{k}/y\right)<(1/2)\log(\omega)+\log(y)+10^{-6} |  |

and A 1 = 2 ​ h ⁡ ( α 1) < 2 ​ log ⁡ ( y) + 0.4813 A_{1}=2\h\left(\alpha_{1}\right)<2\log(y)+0.4813. Thus max ⁡ { | b j | ​ A j / A 1: 1 ≤ j ≤ 3 } = p \max\left\{\left|b_{j}\right|A_{j}/A_{1}:1\leq j\leq 3\right\}=p and we can take B = p B=p.

Applying Matveev’s theorem (Theorem 3.1 above) with χ = 1 \chi=1 and the above quantities gives

 | log ⁡ | Λ | \displaystyle\log\left|\Lambda\right| | > − 5 ⋅ 16 5 6 ⋅ e 3 ⋅ 9 ( 3 e / 2) ⋅ ( 26.25 + log ( 4 log ( 2 e))) ⋅ 4 ⋅ ( 2 log ( y) + 0.4813) ⋅ log ω \displaystyle>-\frac{5\cdot 16^{5}}{6}\cdot e^{3}\cdot 9(3e/2)\cdot\left(26.25+\log(4\log(2e))\right)\cdot 4\cdot\left(2\log(y)+0.4813\right)\cdot\log\omega |  |

 |  | ⋅ log ⁡ ( 5) ⋅ log ⁡ ( 3 ​ e ​ p ​ log ⁡ ( 2 ​ e)) \displaystyle\hskip 14.22636pt\cdot\log(5)\cdot\log\left(3ep\log(2e)\right) |  |

 |  | > − ( 7.10 ⋅ 10 10 + 2.71 ⋅ 10 10 ​ log ⁡ ( p) + 2.96 ⋅ 10 11 ​ log ⁡ ( y) + 1.13 ⋅ 10 11 ​ log ⁡ ( y) ​ log ⁡ ( p)). \displaystyle>-\left(7.10\cdot 10^{10}+2.71\cdot 10^{10}\log(p)+2.96\cdot 10^{11}\log(y)+1.13\cdot 10^{11}\log(y)\log(p)\right). |  |

Combining this lower bound for log ⁡ | Λ | \log\left|\Lambda\right| with the upper bound in ( 6.3), and dividing by 2 ​ log ⁡ ( y) 2\log(y), we obtain

 | 1.476 ⋅ 10 11 + 5.62 ⋅ 10 10 ​ log ⁡ ( p) > p, 1.476\cdot 10^{11}+5.62\cdot 10^{10}\log(p)>p, |  |

using ( 6.2).

Applying Lemma 6.1 with a = 1.476 ⋅ 10 11 a=1.476\cdot 10^{11}, b = 5.62 ⋅ 10 10 b=5.62\cdot 10^{10}, h = 1 h=1 and x = p x=p, so c = h ​ b 1 / h = b c=hb^{1/h}=b and

(6.6) |  | p < b ​ log ⁡ ( b) + log ⁡ ( b) log ⁡ ( b) − 1 ​ ( a + b ​ log ⁡ ( log ⁡ ( b))) < 1.74 ⋅ 10 12. p<b\log(b)+\frac{\log(b)}{\log(b)-1}(a+b\log(\log(b)))<1.74\cdot 10^{12}. |  |

The reason we take this step is because we first need an upper bound on p p to control simultaneously the condition in ( 2.8) and the degenerate cases in our main theorem.

Step (3): Non-degenerate case

Here we apply Theorem 2.1 to reduce our bound on p p.

So that our linear form is in the form ( 2.1), we set

 | α 1 = ω, α 2 = 5, α 3 = ω k / y b 1 = q, b 2 = 1 ​ and ​ b 3 = p \alpha_{1}=\omega,\quad\alpha_{2}=\sqrt{5},\quad\alpha_{3}=\omega^{k}/y\quad b_{1}=q,\quad b_{2}=1\hskip 8.53581pt\text{ and }\hskip 8.53581ptb_{3}=p |  |

and in what follows (Steps (3) and (4)), put

 | Λ = b 1 ​ log ⁡ α 1 + b 2 ​ log ⁡ α 2 − b 3 ​ log ⁡ α 3 = q ​ log ⁡ ( ω) + 1 ⋅ log ⁡ ( 5) − p ​ log ⁡ ( ω k / y). \Lambda=b_{1}\log\alpha_{1}+b_{2}\log\alpha_{2}-b_{3}\log\alpha_{3}=q\log\left(\omega\right)+1\cdot\log\left(\sqrt{5}\right)-p\log\left(\omega^{k}/y\right). |  |

This is − 1 -1 times the Λ \Lambda considered above in Steps (1) and (2).

Recall that we take

 | a i ≥ ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i) a_{i}\geq\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right) |  |

and here 𝒟 = 2 \mathcal{D}=2.

We have h ⁡ ( ω) = log ⁡ ( ω) / 2 \h(\omega)=\log(\omega)/2, so we can take a 1 = ( ρ + 1) ​ log ⁡ ( ω) a_{1}=(\rho+1)\log(\omega).

Similarly, h ⁡ ( 5) = log ⁡ ( 5) \h\left(\sqrt{5}\right)=\log\left(\sqrt{5}\right), so a 2 = ( ρ + 3) ​ log ⁡ ( 5) a_{2}=(\rho+3)\log\left(\sqrt{5}\right).

In Step (2), we saw that log ⁡ | α 3 | = log ⁡ | α 3 | \log\left|\alpha_{3}\right|=\log\left|\alpha_{3}\right| (recall that α 3 \alpha_{3} here was denoted by α 1 \alpha_{1} there), so ρ ​ | log ⁡ α 3 | − log ⁡ | α 3 | = ( ρ − 1) ​ log ​ | α 3 | \rho\left|\log\alpha_{3}\right|-\log\left|\alpha_{3}\right|=(\rho-1)\log\left|\alpha_{3}\right|. Applying ( 6.4), we obtain

 | ρ ​ | log ⁡ α 3 | − log ⁡ | α 3 | < ( ρ − 1) ​ log ​ ω + ( ρ − 1) ​ 10 − 6. \rho\left|\log\alpha_{3}\right|-\log\left|\alpha_{3}\right|<(\rho-1)\log\omega+(\rho-1)10^{-6}. |  |

Combining this with ( 6.5), we can take

 | a 3 = ( ρ − 1) ​ log ⁡ ( ω) + 2 ​ log ⁡ ( ω) + 4 ​ log ⁡ ( y) + ( ρ + 3) ​ 10 − 6 = ( ρ + 1) ​ log ⁡ ( ω) + 4 ​ log ⁡ ( y) + ( ρ + 3) ​ 10 − 6. a_{3}=(\rho-1)\log(\omega)+2\log(\omega)+4\log(y)+(\rho+3)10^{-6}=(\rho+1)\log(\omega)+4\log(y)+(\rho+3)10^{-6}. |  |

To apply Theorem 2.1, we need to select values for all the parameters there. I.e., the positive rational integers K K, L L, R R, R 1 R_{1}, R 2 R_{2}, R 3 R_{3}, S S, S 1 S_{1}, S 2 S_{2}, S 3 S_{3}, T T, T 1 T_{1}, T 2 T_{2} and T 3 T_{3}, along with the real numbers ρ \rho and χ \chi.

We use the work in Section 5 to reduce the amount of choice involved here.

From ( 5.4), we see that K K depends on a 1 a_{1}, a 2 a_{2}, a 3 a_{3}, L L and a real number m ≥ 1 m\geq 1.

From ( 5.2), we see that the R i R_{i} ’s, S i S_{i} ’s and T i T_{i} ’s depend on a 1 a_{1}, a 2 a_{2}, a 3 a_{3} and three positive real parameters c 1 c_{1}, c 2 c_{2} and c 3 c_{3}. Furthermore, we put R = R 1 + R 2 + R 3 + 1 R=R_{1}+R_{2}+R_{3}+1, S = S 1 + S 2 + S 3 + 1 S=S_{1}+S_{2}+S_{3}+1 and T = T 1 + T 2 + T 3 + 1 T=T_{1}+T_{2}+T_{3}+1.

From ( 5.6), ( 5.7), ( 5.8) and ( 5.9), we have values for c 1 c_{1}, c 2 c_{2} and c 3 c_{3} in terms of m m, L L, a 1 a_{1}, a 2 a_{2}, a 3 a_{3} and χ \chi. For our linear form, this just leaves m m, L L, ρ \rho and χ \chi as unspecified parameters.

To apply Theorem 2.1, we do a brute force search. To minimise the effect of the degenerate case we will use Theorem 2 of [19]. But this also involves a search to obtain the best results, so we do not want to do such an additional search for every choice of m m, L L, ρ \rho and χ \chi that we consider. Instead we do the degenerate case only once for each value of χ \chi.

For each of 20 20 equidistributed values of χ \chi satisfying 0.5 ≤ χ ≤ 1.5 0.5\leq\chi\leq 1.5, we proceed as follows. First, we search over integer values of L L with 100 ≤ L ≤ 200 100\leq L\leq 200, 20 values of each of m m and ρ \rho evenly distributed with 4 ≤ m ≤ 9 4\leq m\leq 9 and 7 ≤ ρ ≤ 12 7\leq\rho\leq 12 that lead to ( 2.8) being satisfied and so that K ​ L ​ log ⁡ ( ρ) KL\log(\rho) is as small as possible. With such a minimal choice of parameters for Step 3 for each value of χ \chi, we find the associated bound for Step 4 (the degenerate case) for this choice of parameters. The choice of χ \chi that leads to the best bound for both Step 3 and Step 4 is the one we use.

There is nothing special about using 20 such values. It was only chosen to give a good balance between speed and finding small admissible values of K ​ L ​ log ⁡ ( ρ) KL\log(\rho). The ranges on the parameters were found by experimentation.

This search led to the choice

 | χ = 0.75, L = 167, m = 6 and ρ = 10. \chi=0.75,\quad L=167,\quad m=6\quad\text{ and }\quad\rho=10. |  |

We have

 | K = ⌊ L ​ m ​ a 1 ​ a 2 ​ a 3 ⌋ = ⌊ 221,945 ​ log ⁡ ( y) ⌋. K=\lfloor Lma_{1}a_{2}a_{3}\rfloor=\lfloor 221,945\log(y)\rfloor. |  |

Since a = a 1 a=a_{1} and a ′ = a 2 a^{\prime}=a_{2}, we put

 | c 1 = 82.65 ​ …, c 2 = 100.13 ​ …, c 3 = 795.28 ​ …. c_{1}=82.65\ldots,\quad c_{2}=100.13\ldots,\quad c_{3}=795.28\ldots. |  |

Using these values and the values of the R i R_{i} ’s in ( 5.2), we get

 | R 1 = ⌊ c 1 ​ a 2 ​ a 3 ⌋ = ⌊ 3458.9 ​ log ⁡ ( y) ⌋, R 2 = ⌊ c 2 ​ a 2 ​ a 3 ⌋ = ⌊ 4190.2 ​ log ⁡ ( y) ⌋, R_{1}=\lfloor c_{1}a_{2}a_{3}\rfloor=\lfloor 3458.9\log(y)\rfloor,\quad R_{2}=\lfloor c_{2}a_{2}a_{3}\rfloor=\lfloor 4190.2\log(y)\rfloor, |  |

and

 | R 3 = ⌊ c 3 ​ a 2 ​ a 3 ⌋ = ⌊ 33280 ​ log ⁡ ( y) ⌋. R_{3}=\lfloor c_{3}a_{2}a_{3}\rfloor=\lfloor 33280\log(y)\rfloor. |  |

Further

 | S 1 = ⌊ c 1 ​ a 1 ​ a 3 ⌋ = ⌊ 1750.2 ​ log ⁡ ( y) ⌋, S 2 = ⌊ c 2 ​ a 1 ​ a 3 ⌋ = ⌊ 2120.2 ​ log ⁡ ( y) ⌋, S 3 = ⌊ c 3 ​ a 1 ​ a 3 ⌋ = ⌊ 16839 ​ log ⁡ ( y) ⌋ S_{1}=\lfloor c_{1}a_{1}a_{3}\rfloor=\lfloor 1750.2\log(y)\rfloor,\quad S_{2}=\lfloor c_{2}a_{1}a_{3}\rfloor=\lfloor 2120.2\log(y)\rfloor,\quad S_{3}=\lfloor c_{3}a_{1}a_{3}\rfloor=\lfloor 16839\log(y)\rfloor |  |

and finally

 | T 1 = ⌊ c 1 ​ a 1 ​ a 2 ⌋ = 4577, T 2 = ⌊ c 2 ​ a 1 ​ a 2 ⌋ = 5544, T_{1}=\lfloor c_{1}a_{1}a_{2}\rfloor=4577,\quad T_{2}=\lfloor c_{2}a_{1}a_{2}\rfloor=5544, |  |

and

 | T 3 = ⌊ c 3 ​ a 1 ​ a 2 ⌋ = 44,039. T_{3}=\lfloor c_{3}a_{1}a_{2}\rfloor=44,039. |  |

With 𝒱 = ( ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1)) 1 / 2 \mathcal{V}=\left(\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)\right)^{1/2}, we have χ ​ 𝒱 > 124,000 ​ log ⁡ ( y) \chi\mathcal{V}>124,000\log(y), while 5210 ​ log ⁡ ( y) > R 1 + S 1 + 1 = max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1 } 5210\log(y)>R_{1}+S_{1}+1=\max\left\{R_{1}+S_{1}+1,\,S_{1}+T_{1}+1,\,R_{1}+T_{1}+1\right\}, since log ⁡ ( y) > 10 20 \log(y)>10^{20}, so ℳ = χ ​ 𝒱 \mathcal{M}=\chi\mathcal{V}.

With these choices, along with our lower bound for y y and upper bound for p p, we also find that

 | log ⁡ ( b 3 ′ ​ η 0) \displaystyle\log\left(b_{3}^{\prime}\eta_{0}\right) | < log ( ( 20465 log ( y) + 27080) p) < log log ( y) + 38.11 and \displaystyle<\log\left((20465\log(y)+27080)p\right)<\log\log(y)+38.11\quad\text{ and} |  |

 | log ⁡ ( b 3 ′′ ​ ζ 0) \displaystyle\log\left(b_{3}^{\prime\prime}\zeta_{0}\right) | < log ⁡ ( ( 10355 ​ log ⁡ ( y) − 1 / 2) ​ p + 27080) < log ⁡ log ⁡ ( y) + 37.43. \displaystyle<\log\left((10355\log(y)-1/2)p+27080\right)<\log\log(y)+37.43. |  |

Combining these estimates with Lemma 3.5 (a) and our expression above for K K, we obtain

 | log ⁡ ( b ′) < 54.58. \log(b^{\prime})<54.58. |  |

As seen in Subsection 5.2, these choices imply that the conditions ( 2.9)–( 2.13) of Theorem 2.1 hold. Moreover, the above choices have been made so that condition ( 2.8) holds.

Thus we have

 | log | Λ | ≥ − K L log ρ − log ( K L) > − 8.535 ⋅ 10 7 log ( y). \log\left|\Lambda\right|\geq-KL\log\rho-\log(KL)>-8.535\cdot 10^{7}\log(y). |  |

Combining this with the upper bound from ( 6.3), we get

 | p < 42.68 ⋅ 10 6. p<42.68\cdot 10^{6}. |  |

Step (4): Degenerate case

Under condition ( 2.14) of Theorem 2.1, we obtain

 | p = b 3 ≤ max ⁡ { T 1, T 2 } < 5600, p=b_{3}\leq\max\left\{T_{1},T_{2}\right\}<5600, |  |

which is excluded since we assume p > 10 ⋅ 10 6 p>10\cdot 10^{6}.

So we now consider condition ( 2.15) of Theorem 2.1, where we have

 | u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = u 1 ​ q + u 2 + u 3 ​ p = 0 u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=u_{1}q+u_{2}+u_{3}p=0 |  |

with gcd ⁡ ( u 1, u 2, u 3) = 1 \gcd\left(u_{1},u_{2},u_{3}\right)=1.

We put

 | U 1:= ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, U 2:= ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 } ​ and ​ U 3:= ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 }. U_{1}:=\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-\max\{S_{1},T_{1}\}},\hskip 5.69054ptU_{2}:=\frac{(R_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{R_{1},T_{1}\}}\hskip 5.69054pt\text{ and }\hskip 5.69054ptU_{3}:=\frac{\left(R_{1}+1\right)\left(S_{1}+1\right)}{\mathcal{M}-\max\{R_{1},S_{1}\}}. |  |

From the values of the relevant quantities in Step (3) and log ⁡ ( y) > 10 20 \log(y)>10^{20}, we obtain

 | | u 1 | ≤ ⌊ U 1 ⌋ = 65, | u 2 | ≤ U 2 = 130 ​ and ​ | u 3 | ≤ ⌊ U 3 ⌋ < 49.87 ​ log ⁡ ( y). \left|u_{1}\right|\leq\lfloor U_{1}\rfloor=65,\hskip 8.53581pt\left|u_{2}\right|\leq U_{2}=130\hskip 8.53581pt\text{ and }\left|u_{3}\right|\leq\lfloor U_{3}\rfloor<49.87\log(y). |  |

We will use this linear relation between the b i b_{i} ’s to reduce the linear form, Λ \Lambda, to one in two logarithms. Let us make a remark here about how we choose which b i b_{i} to eliminate.

###### Remark.

We can only eliminate a b i b_{i} with U i U_{i} bounded above by a constant. Trying to eliminate a b i b_{i} with U i U_{i} depending on some parameter (like U 3 U_{3} here depending on log ⁡ y \log y) leads to both the quantities a 1 a_{1} and a 2 a_{2} in Theorem 2 of [19] depending on that parameter, so we do not get an absolute upper bound on the quantity we are interested in (i.e., p p here).

Here this means that we eliminate either b 1 = q b_{1}=q or b 2 = 1 b_{2}=1. Since a 1 < a 2 a_{1}<a_{2} here, our heuristic argument in Subsection 5.3 above suggests that we eliminate b 1 b_{1}.

In our Pari/GP code, we tried eliminating both possibilities ( b 1 b_{1} and b 2 b_{2}) and the best upper bound for p p comes from eliminating b 1 = q b_{1}=q. As noted above, this is in keeping with our heuristic argument in Subsection 5.3. So we consider u 1 ​ Λ u_{1}\Lambda:

 | u 1 ​ Λ \displaystyle u_{1}\Lambda | = u 1 ​ q ​ log ⁡ ( ω) + u 1 ​ log ⁡ ( 5) − u 1 ​ p ​ log ⁡ ( ω k / y) \displaystyle=u_{1}q\log(\omega)+u_{1}\log\left(\sqrt{5}\right)-u_{1}p\log\left(\omega^{k}/y\right) |  |

 |  | = − ( u 2 ​ q + u 3 ​ p) ​ log ⁡ ( ω) + u 1 ​ log ⁡ ( 5) − u 1 ​ p ​ log ⁡ ( ω k / y) \displaystyle=-\left(u_{2}q+u_{3}p\right)\log\left(\omega\right)+u_{1}\log\left(\sqrt{5}\right)-u_{1}p\log\left(\omega^{k}/y\right) |  |

 |  | = log ⁡ ( 5 u 1 ⋅ ω − u 2) − p ​ log ⁡ ( ( ω k / y) u 1 ⋅ ω u 3). \displaystyle=\log\left(\sqrt{5}^{u_{1}}\cdot\omega^{-u_{2}}\right)-p\log\left(\left(\omega^{k}/y\right)^{u_{1}}\cdot\omega^{u_{3}}\right). |  |

We will use Theorem 2 in [19] to obtain lower bounds for this linear form.

We put α 1 ′ = 5 u 1 ⋅ ω − u 2 \alpha_{1}^{\prime}=\sqrt{5}^{u_{1}}\cdot\omega^{-u_{2}}, α 2 ′ = ( ω k / y) u 1 ⋅ ω u 3 \alpha_{2}^{\prime}=\left(\omega^{k}/y\right)^{u_{1}}\cdot\omega^{u_{3}}, b 1 = 1 b_{1}=1 and b 2 = p b_{2}=p. We use α 1 ′ \alpha_{1}^{\prime} and α 2 ′ \alpha_{2}^{\prime} here for α 1 \alpha_{1} and α 2 \alpha_{2} in [19] in order not to confuse it with our α 1 \alpha_{1} and α 2 \alpha_{2} above. As mentioned above, using Laurent’s Theorem 2 requires a search, here for the quantities that he labels as ϱ \varrho (which plays the analogous role for linear forms in two logs as our ρ \rho) and μ \mu. Once again, we do a brute force search over 20 20 equidistributed values of each parameter with 7 ≤ ϱ ≤ 11 7\leq\varrho\leq 11 and 0.5 ≤ μ ≤ 0.7 0.5\leq\mu\leq 0.7. In this way, we take

 | ϱ = 10, μ = 0.61, a 1 = 1368.2 and a 2 = 524 log ( y). \varrho=10,\qquad\mu=0.61,\qquad a_{1}=1368.2\qquad\text{ and }\qquad a_{2}=524\log(y). |  |

We have

 | b 1 a 2 + b 2 a 1 < 0.00074 ​ p. \frac{b_{1}}{a_{2}}+\frac{b_{2}}{a_{1}}<0.00074p. |  |

So 2 ​ log ⁡ ( p) − 9.373 < h < log ⁡ ( p) − 2 ​ log ⁡ ( p) − 9.372 2\log(p)-9.373<h<\log(p)-2\log(p)-9.372. Thus

 | log ⁡ | Λ | > 423,900 ​ ( log ⁡ ( p) − 4.687) 2 ​ log ⁡ ( y). \log\left|\Lambda\right|>423,900\left(\log(p)-4.687\right)^{2}\log(y). |  |

Combining this with the upper bound for Λ \Lambda in ( 6.3), we get

 | − 423,900 ​ ( log ⁡ ( p) − 4.687) 2 ​ log ⁡ ( y) < − 2 ​ p ​ log ⁡ ( y) + log ⁡ | e |. -423,900\left(\log(p)-4.687\right)^{2}\log(y)<-2p\log(y)+\log\left|e\right|. |  |

Dividing both sides by 2 ​ log ⁡ ( y) 2\log(y), using log ⁡ ( y) > 10 20 \log(y)>10^{20} and again applying Lemma 6.1 with a = log ⁡ ( e) / ( 2 ⋅ 10 20 ​ exp ⁡ ( 4.687)) < 10 − 6 a=\log(e)/\left(2\cdot 10^{20}\exp(4.687)\right)<10^{-6}, b = 423,900 / ( 2 ​ exp ⁡ ( 4.687)) b=423,900/\left(2\exp(4.687)\right), h = 2 h=2 and x = p / exp ⁡ ( 4.687) x=p/\exp(4.687), we get c < 88.41 c<88.41 and

 | p < 34.86 ⋅ 10 6. p<34.86\cdot 10^{6}. |  |

But we also have to consider the case that we cannot eliminate b 1 b_{1}. This is the case when u 1 = 0 u_{1}=0. We proceed in the same way as we just did, but now eliminate b 2 b_{2}, since u 2 u_{2} is bounded above by a constant. Doing so gives us the upper bound p < 39 ⋅ 10 6 p<39\cdot 10^{6}.

Combining this with the result of Step (3), we have proved that p ≤ 42.68 ⋅ 10 6 p\leq 42.68\cdot 10^{6}.

Step (5): Iteration of Steps (3) and (4)

As in [9], we repeated Steps (3) and (4) a second time to obtain the improved upper bound p ≤ 19.4 ⋅ 10 6 p\leq 19.4\cdot 10^{6}.

We repeat this same search a third time with this further improved upper bound for p p to obtain p < 17.92 ⋅ 10 6 p<17.92\cdot 10^{6}.

iteration | initial upper bound for p p | L L | m m | ρ \rho | χ \chi | ϱ \varrho | μ \mu | new upper bound for p p |

1 1 | 1.8 ⋅ 10 12 1.8\cdot 10^{12} | 167 167 | 6 6 | 10 10 | 0.75 0.75 | 10 10 | 0.61 0.61 | 43 ⋅ 10 6 43\cdot 10^{6} |

2 2 | 43 ⋅ 10 6 43\cdot 10^{6} | 105 105 | 7.25 7.25 | 9.75 9.75 | 1.03 1.03 | 10 10 | 0.61 0.61 | 19.4 ⋅ 10 6 19.4\cdot 10^{6} |

3 3 | 19.4 ⋅ 10 6 19.4\cdot 10^{6} | 104 104 | 7.4 7.4 | 9.4 9.4 | 1.06 1.06 | 9.8 9.8 | 0.61 0.61 | 17.92 ⋅ 10 6 17.92\cdot 10^{6} |

The three iterations took 180, 187 and 70 seconds on a Windows laptop with an Intel i7-9750H 2.60GHz CPU and 16Gb of RAM.

The third iteration gives us the upper bound for p p stated in the theorem. ∎

From the table, one can see that little improvement is obtained after the second iteration.

If one could ignore the degenerate case, as we conjecture should be possible, and only consider the inequality ( 2.8) for the non-degenerate case, then one would obtain p < 12.4 ⋅ 10 6 p<12.4\cdot 10^{6} instead. So we are within 50 % 50\% of the best possible result that our transcendence argument can provide. Our kit should always provide such proximity to the optimal result when considering the real case for our linear forms in logs (as described in Subsection 2.1).

### 6.2. Example 2: x 2 + 7 = y p x^{2}+7=y^{p}

This is the case D = 7 D=7 examined in detail in Section 15 of [10]. There the authors claimed that p < 130 ⋅ 10 6 p<130\cdot 10^{6}. Our work here suggests that the best possible bound they could have obtained was p < 156 ⋅ 10 6 p<156\cdot 10^{6}. While our result here is over 6 6 times smaller than this, our improvement here is not as large as for the previous example. The reason is because in [10], the zero estimate of Laurent [18], given in Appendix A below, was used. This was an improvement over the zero estimate used in [9].

So we take the opportunity here to correct the handling of D = 7 D=7 in that paper. In addition to the above, not all of the R i R_{i} ’s, S i S_{i} ’s and T i T_{i} ’s can be constants as stated in Section 15 of [10]. A dependence on log ⁡ ( y) \log(y) is required. See our correct choice of these parameters in Step (3) below.

One last note about our result here. The upper bound for p p is the best possible one, given our inequality ( 2.8) for the non-degenerate case. The degenerate case does not adversely affect the results we obtain here. This turns out to always happen when, as here, we are considering the imaginary case for our linear forms in logs (as described in Subsection 2.1).

###### Theorem 6.3.

If x 2 + 7 = y p x^{2}+7=y^{p} has a solution for a prime p ≥ 3 p\geq 3 with x, y ∈ ℤ x,y\in\mathbb{Z}, then

(6.7) |  | p < 25 ⋅ 10 6. p<25\cdot 10^{6}. |  |

###### Proof.

We will assume that p > 20 ⋅ 10 6 p>20\cdot 10^{6} and use the modular lower bound for y y in equation (14) of [10]:

(6.8) |  | y ≥ ( p − 1) 2 > 19.9 ⋅ 10 6. y\geq\left(\sqrt{p}\,-1\right)^{2}>19.9\cdot 10^{6}. |  |

We will use the principal branch of the logarithm throughout the proof.

Step (1): Linear form definition and upper bound

In Section 15 of [10], on page 56, the authors consider

 | Λ = 2 ​ log ⁡ ( ε 1 ​ α 0 ¯ / α 0) + p ​ log ⁡ ( ε 2 ​ γ ¯ / γ) + i ​ q ​ π, \Lambda=2\log\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)+p\log\left(\varepsilon_{2}\overline{\gamma}/\gamma\right)+iq\pi, |  |

for some rational integer q q with | q | < p |q|<p, ε 1, ε 2 = ± 1 \varepsilon_{1},\varepsilon_{2}=\pm 1, α 0 = ( 1 + − 7) / 2 \alpha_{0}=\left(1+\sqrt{-7}\right)/2 and γ \gamma is an algebraic integer in ℚ ⁡ ( − 7) \mathbb{Q}\left(\sqrt{-7}\right) with norm y y such that

 | ( x − − 7 x + − 7) k = ( α 0 ¯ / α 0) κ ( ± γ ¯ / γ) p. \left(\frac{x-\sqrt{-7}}{x+\sqrt{-7}}\right)^{k}=\left(\overline{\alpha_{0}}/\alpha_{0}\right)^{\kappa}\left(\pm\overline{\gamma}/\gamma\right)^{p}. |  |

This expression comes from Lemma 13.1 of [10] and its proof since ℚ ⁡ ( − 7) \mathbb{Q}\left(\sqrt{-7}\right) has class number 1 1, so k 0 = 1 k_{0}=1 there. As a result, their κ = 2 \kappa=2 and k = 1 k=1. They assert in the proof of their Lemma 13.4 that this value of α 0 \alpha_{0} is valid.

From their Lemma 13.3, we have

(6.9) |  | log ⁡ | Λ | < − p 2 ​ log ⁡ ( y) + log ⁡ ( 2.2 ​ 7), \log\left|\Lambda\right|<-\frac{p}{2}\log(y)+\log\left(2.2\sqrt{7}\right), |  |

since D 1 = 1 D_{1}=1 and D 2 = 7 D_{2}=7.

This is the case (I) linear form that they consider there.

Step (2): Matveev
In the notation of Theorem 3.1, we have α 1 = ε 2 ​ γ ¯ / γ \alpha_{1}=\varepsilon_{2}\overline{\gamma}/\gamma, α 2 = ε 1 ​ α 0 ¯ / α 0 \alpha_{2}=\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}, α 3 = − 1 \alpha_{3}=-1, b 1 = p b_{1}=p, b 2 = 2 b_{2}=2 and b 3 = q b_{3}=q. So D = χ = 2 D=\chi=2.

Note that we have swapped the α 1 \alpha_{1} term with the α 2 \alpha_{2} term here with those in the case (I) linear form in [10]. This will result in A 1 A_{1} being the largest of the A i A_{i} ’s, Doing so lets us take B = p B=p in Theorem 3.1.

Recall that A j ≥ max ⁡ { D ​ h ⁡ ( α j), | log ⁡ α j | } A_{j}\geq\max\left\{D\h\left(\alpha_{j}\right),\left|\log\alpha_{j}\right|\right\}. Since the norm of γ \gamma is y y, we have h ⁡ ( γ) = log ⁡ ( y) / 2 \h\left(\gamma\right)=\log(y)/2 and since α 1 \alpha_{1} is on the unit circle, by our choice of ε 2 \varepsilon_{2}, we have | log ⁡ α 1 | < π / 2 \left|\log\alpha_{1}\right|<\pi/2. Thus, we can take A 1 = log ⁡ ( y) A_{1}=\log(y), since y > 20 ⋅ 10 6 y>20\cdot 10^{6} (by ( 6.8)).

Similarly, for A 2 A_{2}, we have d = 2 d=2 by Lemma 13.1 and Table 4 of [10]. So from their Lemma 13.1, h ⁡ ( α 2) = log ⁡ ( 2) / 2 \h\left(\alpha_{2}\right)=\log(2)/2. Also, | log ⁡ α 2 | = 0.722734 ​ … \left|\log\alpha_{2}\right|=0.722734\ldots, so we can take A 2 = 0.73 A_{2}=0.73.

Lastly, we can take A 3 = π A_{3}=\pi.

Applying Matveev’s theorem (Theorem 3.1 above) with the above quantities gives

 | log ⁡ | Λ | \displaystyle\log\left|\Lambda\right| | > − 5 ⋅ 16 5 6 ⋅ 2 e 3 ( 7 + 2 ⋅ 2) ( 3 e / 2) 2 ⋅ ( 26.25 + log ( 2 2 log ( 2 e))) ⋅ 2 2 log ( y) 0.73 π log ( 1.5 e ⋅ 2 p log ( 2 e)) \displaystyle>-\frac{5\cdot 16^{5}}{6\cdot 2}e^{3}(7+2\cdot 2)(3e/2)^{2}\cdot\left(26.25+\log\left(2^{2}\log(2e)\right)\right)\cdot 2^{2}\log(y)0.73\pi\log\left(1.5e\cdot 2p\log(2e)\right) |  |

 |  | > − 4.11 ⋅ 10 11 log ( y) log ( 13.81 p). \displaystyle>-4.11\cdot 10^{11}\log(y)\log(13.81p). |  |

Combining this lower bound for log ⁡ | Λ | \log\left|\Lambda\right| with the upper bound in ( 6.9), and dividing by log ⁡ ( y) / 2 \log(y)/2, we obtain

 | 8.21 ⋅ 10 11 ​ log ⁡ ( p) + 2.16 ⋅ 10 12 > 8.21 ⋅ 10 11 ​ log ⁡ ( 13.81 ​ p) + 2 ​ log ⁡ ( 2.2 ​ 7) / log ⁡ ( y) > p, 8.21\cdot 10^{11}\log(p)+2.16\cdot 10^{12}>8.21\cdot 10^{11}\log(13.81p)+2\log\left(2.2\sqrt{7}\right)/\log(y)>p, |  |

using ( 6.8).

Applying Lemma 6.1 with a = 2.16 ⋅ 10 12 a=2.16\cdot 10^{12}, b = 8.21 ⋅ 10 11 b=8.21\cdot 10^{11}, h = 1 h=1 and x = p x=p, so c = h ​ b 1 / h = b c=hb^{1/h}=b and

(6.10) |  | p < b ​ log ⁡ ( b) + log ⁡ ( b) log ⁡ ( b) − 1 ​ ( a + b ​ log ⁡ ( log ⁡ ( b))) < 2.76 ⋅ 10 13. p<b\log(b)+\frac{\log(b)}{\log(b)-1}(a+b\log(\log(b)))<2.76\cdot 10^{13}. |  |

Step (3): Non-degenerate case
Here we apply Theorem 2.1 to reduce our bound on p p.

Recall that we take a i ≥ ρ ​ | log ⁡ α i | − log ⁡ | α i | + 2 ​ 𝒟 ​ h ⁡ ( α i) a_{i}\geq\rho\left|\log\alpha_{i}\right|-\log\left|\alpha_{i}\right|+2\mathcal{D}\h\left(\alpha_{i}\right) and here 𝒟 = 1 \mathcal{D}=1.

Using the values of h ⁡ ( α i) \h\left(\alpha_{i}\right) and | log ⁡ α i | \left|\log\alpha_{i}\right| that we found in Step (2), we can take a 1 = ρ ​ π / 2 + log ⁡ ( y) a_{1}=\rho\pi/2+\log(y), a 2 = 0.723 ​ ρ + log ⁡ ( 2) a_{2}=0.723\rho+\log(2) and a 3 = ρ ​ π a_{3}=\rho\pi.

To apply Theorem 2.1, we do a brute force search in the same way as we did in the first example. For each of 20 20 equidistributed values of χ \chi satisfying 0.04 ≤ χ ≤ 0.24 0.04\leq\chi\leq 0.24, we proceed as follows. First, we search over integer values of L L with 30 ≤ L ≤ 200 30\leq L\leq 200, 20 values of each of m m and ρ \rho evenly distributed with 10 ≤ m ≤ 30 10\leq m\leq 30 and 3 ≤ ρ ≤ 13 3\leq\rho\leq 13 that lead to ( 2.8) being satisfied and so that K ​ L ​ log ⁡ ( ρ) KL\log(\rho) is as small as possible. With such a minimal choice of parameters for Step 3 for each value of χ \chi, we find the associated bound for Step 4 (the degenerate case) for this choice of parameters. The choice of χ \chi that leads to the best bound for both Step 3 and Step 4 is the one we use.

This search led to the choice

 | χ = 0.08, L = 106, m = 21.0 and ρ = 5.5. \chi=0.08,\quad L=106,\quad m=21.0\quad\text{ and }\quad\rho=5.5. |  |

Since ⌊ L ​ m ​ a 1 ​ a 2 ​ a 3 ⌋ < ⌊ 300,476 ​ log ⁡ ( y) ⌋ \lfloor Lma_{1}a_{2}a_{3}\rfloor<\lfloor 300,476\log(y)\rfloor, we put

 | K = ⌊ 231,600 ​ log ⁡ ( y) ⌋. K=\lfloor 231,600\log(y)\rfloor. |  |

We have a = a 2 a=a_{2} and a ′ = a 3 a^{\prime}=a_{3} and put

 | c 1 = 33.46 ​ …, c 2 = 243.59 ​ …, c 3 = 1163.65 ​ …. c_{1}=33.46\ldots,\quad c_{2}=243.59\ldots,\quad c_{3}=1163.65\ldots. |  |

Using these values and the values of the R i R_{i} ’s in ( 5.2), we get

 | R 1 = ⌊ c 1 ​ a 2 ​ a 3 ⌋ = 2299, R 2 = ⌊ c 2 ​ a 2 ​ a 3 ⌋ = 16,737, R_{1}=\lfloor c_{1}a_{2}a_{3}\rfloor=2299,\quad R_{2}=\lfloor c_{2}a_{2}a_{3}\rfloor=16,737, |  |

and

 | R 3 = ⌊ c 3 ​ a 2 ​ a 3 ⌋ = 79,953. R_{3}=\lfloor c_{3}a_{2}a_{3}\rfloor=79,953. |  |

Further,

 | S 1 = ⌊ c 1 ​ a 1 ​ a 3 ⌋ = ⌊ 876 ​ log ⁡ y ⌋, S 2 = ⌊ c 2 ​ a 1 ​ a 3 ⌋ = ⌊ 6373 ​ log ⁡ y ⌋, S 3 = ⌊ c 3 ​ a 1 ​ a 3 ⌋ = ⌊ 30440 ​ log ⁡ y ⌋ S_{1}=\lfloor c_{1}a_{1}a_{3}\rfloor=\lfloor 876\log y\rfloor,\quad S_{2}=\lfloor c_{2}a_{1}a_{3}\rfloor=\lfloor 6373\log y\rfloor,\quad S_{3}=\lfloor c_{3}a_{1}a_{3}\rfloor=\lfloor 30440\log y\rfloor |  |

and finally

 | T 1 = ⌊ c 1 ​ a 1 ​ a 2 ⌋ = ⌊ 202 ​ log ⁡ y ⌋, T 2 = ⌊ c 2 ​ a 1 ​ a 2 ⌋ = ⌊ 1467 ​ log ⁡ y ⌋, T_{1}=\lfloor c_{1}a_{1}a_{2}\rfloor=\lfloor 202\log y\rfloor,\quad T_{2}=\lfloor c_{2}a_{1}a_{2}\rfloor=\lfloor 1467\log y\rfloor, |  |

and

 | T 3 = ⌊ c 3 ​ a 1 ​ a 2 ⌋ = ⌊ 7006 ​ log ⁡ y ⌋. T_{3}=\lfloor c_{3}a_{1}a_{2}\rfloor=\lfloor 7006\log y\rfloor. |  |

With 𝒱 = ( ( R 1 + 1) ​ ( S 1 + 1) ​ ( T 1 + 1)) 1 / 2 \mathcal{V}=\left(\left(R_{1}+1\right)\left(S_{1}+1\right)\left(T_{1}+1\right)\right)^{1/2}, we have χ ​ 𝒱 > 1611 ​ log ⁡ ( y) \chi\mathcal{V}>1611\log(y), while 1100 ​ log ⁡ ( y) > S 1 + T 1 + 1 = max ⁡ { R 1 + S 1 + 1, S 1 + T 1 + 1, R 1 + T 1 + 1 } 1100\log(y)>S_{1}+T_{1}+1=\max\left\{R_{1}+S_{1}+1,\,S_{1}+T_{1}+1,\,R_{1}+T_{1}+1\right\}, since log ⁡ ( y) > 17.4 \log(y)>17.4, so ℳ = χ ​ 𝒱 \mathcal{M}=\chi\mathcal{V}.

With these choices, along with our lower bound for y y and upper bound for n n, we also find that

 | log ⁡ ( b 3 ′ ​ η 0) \displaystyle\log\left(b_{3}^{\prime}\eta_{0}\right) | < log ( ( 4337 log ( y) + 49,500) n) < log log ( y) + 39.85 and \displaystyle<\log\left(\left(4337\log(y)+49,500\right)n\right)<\log\log(y)+39.85\quad\text{ and} |  |

 | log ⁡ ( b 3 ′′ ​ ζ 0) \displaystyle\log\left(b_{3}^{\prime\prime}\zeta_{0}\right) | < log ⁡ ( ( 8680 + 18,850 ​ n) ​ log ⁡ ( y)) < log ⁡ log ⁡ ( y) + 40.8. \displaystyle<\log\left(\left(8680+18,850n\right)\log(y)\right)<\log\log(y)+40.8. |  |

Combining these estimates with Lemma 3.5 (a) and our expression above for K K, we obtain

 | log ⁡ ( b ′) < 59.6. \log(b^{\prime})<59.6. |  |

As seen above, these choices imply that the conditions ( 2.9)–( 2.13) of Theorem 2.1 hold. Moreover, the above choices have been made so that condition ( 2.8) holds.

Thus we have

 | log | Λ | ≥ − K L log ρ − log ( K L) > − 4.185 ⋅ 10 7 log ( y). \log\left|\Lambda\right|\geq-KL\log\rho-\log(KL)>-4.185\cdot 10^{7}\log(y). |  |

Combining this with the upper bound from ( 6.3), we get

 | p < 83.69 ⋅ 10 6. p<83.69\cdot 10^{6}. |  |

Step (4): Degenerate case
Under condition ( 2.14) of Theorem 2.1, we obtain

 | p = b 1 ≤ max ⁡ { R 1, R 2 } < 16,800, p=b_{1}\leq\max\left\{R_{1},R_{2}\right\}<16,800, |  |

which is excluded since we assume p > 20 ⋅ 10 6 p>20\cdot 10^{6}.

So we now consider condition ( 2.15) of Theorem 2.1, where we have

 | u 1 ​ b 1 + u 2 ​ b 2 + u 3 ​ b 3 = u 1 ​ q + u 2 + u 3 ​ p = 0 u_{1}b_{1}+u_{2}b_{2}+u_{3}b_{3}=u_{1}q+u_{2}+u_{3}p=0 |  |

with gcd ⁡ ( u 1, u 2, u 3) = 1 \gcd\left(u_{1},u_{2},u_{3}\right)=1.

We put

 | U 1:= ( S 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { S 1, T 1 }, U 2:= ( R 1 + 1) ​ ( T 1 + 1) ℳ − max ⁡ { R 1, T 1 } ​ and ​ U 3:= ( R 1 + 1) ​ ( S 1 + 1) ℳ − max ⁡ { R 1, S 1 }. U_{1}:=\frac{\left(S_{1}+1\right)\left(T_{1}+1\right)}{\mathcal{M}-\max\{S_{1},T_{1}\}},\hskip 5.69054ptU_{2}:=\frac{(R_{1}+1)(T_{1}+1)}{\mathcal{M}-\max\{R_{1},T_{1}\}}\hskip 5.69054pt\text{ and }\hskip 5.69054ptU_{3}:=\frac{\left(R_{1}+1\right)\left(S_{1}+1\right)}{\mathcal{M}-\max\{R_{1},S_{1}\}}. |  |

From the values of the relevant quantities in Step (3) and log ⁡ ( y) > 17.4 \log(y)>17.4, we obtain

 | | u 1 | ≤ U 1 < 239.64 ​ log ⁡ ( y), | u 2 | ≤ ⌊ U 2 ⌋ = 328 ​ and ​ | u 3 | ≤ ⌊ U 3 ⌋ = 2735. \left|u_{1}\right|\leq U_{1}<239.64\log(y),\hskip 8.53581pt\left|u_{2}\right|\leq\lfloor U_{2}\rfloor=328\hskip 8.53581pt\text{ and }\left|u_{3}\right|\leq\lfloor U_{3}\rfloor=2735. |  |

Here we use this linear relation between the b i b_{i} ’s to reduce the linear form, Λ \Lambda, to one in two logarithms by eliminating b 2 b_{2}:

 | u 2 ​ Λ \displaystyle u_{2}\Lambda | = 2 ​ u 2 ​ log ⁡ ( ε 1 ​ α 0 ¯ / α 0) + u 2 ​ p ​ log ⁡ ( ε 2 ​ γ ¯ / γ) + u 2 ​ q ​ log ⁡ ( − 1) \displaystyle=2u_{2}\log\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)+u_{2}p\log\left(\varepsilon_{2}\overline{\gamma}/\gamma\right)+u_{2}q\log(-1) |  |

 |  | = − ( u 1 ​ p + u 3 ​ q) ​ log ⁡ ( ε 1 ​ α 0 ¯ / α 0) + u 2 ​ p ​ log ⁡ ( ε 2 ​ γ ¯ / γ) + u 2 ​ q ​ log ⁡ ( − 1) \displaystyle=-\left(u_{1}p+u_{3}q\right)\log\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)+u_{2}p\log\left(\varepsilon_{2}\overline{\gamma}/\gamma\right)+u_{2}q\log(-1) |  |

 |  | = p ​ log ⁡ ( ( ε 2 ​ γ ¯ / γ) u 2 ⋅ ( ε 1 ​ α 0 ¯ / α 0) − u 1) − q ​ log ⁡ ( ( ε 1 ​ α 0 ¯ / α 0) u 3 ⋅ ( − 1) − u 2). \displaystyle=p\log\left(\left(\varepsilon_{2}\overline{\gamma}/\gamma\right)^{u_{2}}\cdot\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)^{-u_{1}}\right)-q\log\left(\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)^{u_{3}}\cdot(-1)^{-u_{2}}\right). |  |

So we put α 1 = ( ε 2 ​ γ ¯ / γ) u 2 ⋅ ( ε 1 ​ α 0 ¯ / α 0) − u 1 \alpha_{1}=\left(\varepsilon_{2}\overline{\gamma}/\gamma\right)^{u_{2}}\cdot\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)^{-u_{1}}, α 2 = ( ε 1 ​ α 0 ¯ / α 0) u 3 ⋅ ( − 1) − u 2 \alpha_{2}=\left(\varepsilon_{1}\overline{\alpha_{0}}/\alpha_{0}\right)^{u_{3}}\cdot(-1)^{-u_{2}}, b 1 = p b_{1}=p and b 2 = q b_{2}=q in Theorem 2 of [19]. In the same way as in Example 1, we take

 | ϱ = 180, μ = 0.61, a 1 = 495.2 log ( y) + 565.5 and a 2 = 2461.3. \varrho=180,\qquad\mu=0.61,\qquad a_{1}=495.2\log(y)+565.5\qquad\text{ and }\qquad a_{2}=2461.3. |  |

We have

 | b 1 a 2 + b 2 a 1 < 0.00052 ​ p, \frac{b_{1}}{a_{2}}+\frac{b_{2}}{a_{1}}<0.00052p, |  |

since D = 1 D=1, log ⁡ ( y) > 17.4 \log(y)>17.4 and p > 20 ⋅ 10 6 p>20\cdot 10^{6}. So log ⁡ ( p) − 4.431 < h < log ⁡ ( p) − 4.185 \log(p)-4.431<h<\log(p)-4.185. Thus

 | log ⁡ | Λ | > 28,100 ​ ( log ⁡ ( p) − 4.185) 2 ​ log ⁡ ( y). \log\left|\Lambda\right|>28,100\left(\log(p)-4.185\right)^{2}\log(y). |  |

Combining this with the upper bound for Λ \Lambda in ( 6.9), we get

 | − 28,100 ​ ( log ⁡ ( p) − 4.185) 2 ​ log ⁡ ( y) < − ( p / 2) ​ log ⁡ ( y) + log ⁡ | 2.2 ​ 7 |. -28,100\left(\log(p)-4.185\right)^{2}\log(y)<-(p/2)\log(y)+\log\left|2.2\sqrt{7}\right|. |  |

Dividing both sides by − ( 1 / 2) ​ log ⁡ ( y) -(1/2)\log(y) and again applying Lemma 6.1 with

 | a = log ⁡ ( 2.2 ​ 7) ( 1 / 2) ​ log ⁡ ( 19.9 ⋅ 10 6) ​ exp ⁡ ( 4.185) < 0.0032, a=\frac{\log\left(2.2\sqrt{7}\right)}{(1/2)\log\left(19.9\cdot 10^{6}\right)\exp(4.185)}<0.0032, |  |

b = 28,100 / ( 0.5 ​ exp ⁡ ( 4.185)) b=28,100/(0.5\exp(4.185)), h = 2 h=2 and x = p / exp ⁡ ( 4.185) x=p/\exp(4.185), we get c < 58.46 c<58.46 and

 | p < exp ⁡ ( 4.185) ⋅ 347 2 < 79.2 ⋅ 10 6. p<\exp(4.185)\cdot 347^{2}<79.2\cdot 10^{6}. |  |

Similarly, when we consider the possibility that u 2 = 0 u_{2}=0, we find that p < 54.2 ⋅ 10 6 p<54.2\cdot 10^{6}.

Combining this with the result of Step (3), we have proved that p < 84 ⋅ 10 6 p<84\cdot 10^{6}.

Step (5): Iteration of Steps (3) and (4)
As in [10], we repeated Steps (3) and (4) a second time using the improved upper bound p < 84 ⋅ 10 6 p<84\cdot 10^{6}.

iteration | initial upper bound for p p | L L | m m | ρ \rho | χ \chi | ϱ \varrho | μ \mu | new upper bound for p p |

1 1 | 2.76 ⋅ 10 13 2.76\cdot 10^{13} | 106 106 | 21.0 21.0 | 5.5 5.5 | 0.08 0.08 | 180 180 | 0.61 0.61 | 84 ⋅ 10 6 84\cdot 10^{6} |

2 2 | 84 ⋅ 10 6 84\cdot 10^{6} | 59 59 | 18.0 18.0 | 6.0 6.0 | 0.1 0.1 | 180 180 | 0.61 0.61 | 29 ⋅ 10 6 29\cdot 10^{6} |

3 3 | 29 ⋅ 10 6 29\cdot 10^{6} | 59 59 | 18.0 18.0 | 5.75 5.75 | 0.1 0.1 | 180 180 | 0.61 0.61 | 25.4 ⋅ 10 6 25.4\cdot 10^{6} |

4 4 | 25.5 ⋅ 10 6 25.5\cdot 10^{6} | 57 57 | 19.0 19.0 | 5.75 5.75 | 0.1 0.1 | 180 180 | 0.61 0.61 | 24.94 ⋅ 10 6 24.94\cdot 10^{6} |

The four iterations took 191, 188, 103 and 104 seconds on a Windows laptop with an Intel i7-9750H 2.60GHz CPU and 16Gb of RAM.

The fourth iteration gives us the upper bound for p p stated in the theorem. ∎

## References

- [1] Y. M. Aleksentsev, *The Hilbert polynomial and linear forms in the logarithms of algebraic numbers*, Izv. Math. 72 (2008), 1063–1110.
- [2] A. Baker, *Linear forms in the logarithms of algebraic numbers. I*, Mathematika 12 (1966), 204–216.
- [3] A. Baker, H. Davenport, *The equations 3 ​ x 2 − 2 = y 2 3x^{2}-2=y^{2} and 8 ​ x 2 − 7 = z 2 8x^{2}-7=z^{2}*, Quart. J. Math. Oxford Ser. (2) 20 (1969), 129–137.
- [4] C. D. Bennett, J. Blass, A. M. W. Glass, D. B. Meronk, R. P. Steiner, *Linear forms in the logarithms of three positive rational numbers*, J. Théor. Nombres Bordeaux 9 (1997), 97–136.
- [5] M.A. Bennett, K. Győry, Mignotte, Á. Pintér, *Binomial Thue equations and polynomial powers*, Comp. Math. 142 (2006), 1103–1121.
- [6] M.A. Bennett, S. Dahmen, Mignotte, S. Siksek, *Shifted powers in binary recurrence sequences*, Math. Proc. Camb. Phil. Soc. 158 (2015), 305–329.
- [7] Yu. Bilu, G. Hanrot, *Solving Thue Equations of High Degree*, J. Number Theory 60 (1996), 373–392.
- [8] Y. Bugeaud, *Linear Forms in Logarithms and Applications*, European Mathematical Society, Zurich, 2018.
- [9] Y. Bugeaud, M. Mignotte, S. Siksek, *Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers*, Ann. Math. 163 (2006), 969–1018.
- [10] Y. Bugeaud, M. Mignotte, S. Siksek, *Classical and Modular Approaches to Exponential Diophantine Equations II. The Lebesgue–Nagell Equation*, Comp. Math. 142 (2006), 31–62.
- [11] J. Dieudonné, *Calcul infinitésimal*(2nd ed), Hermann, Paris, 1980.
- [12] A. Dujella, A. Pethő, *A generalization of a theorem of Baker and Davenport*, Quart. J. Math. Oxford Ser. (2) 49 (1998), 291–306.
- [13] N. Gouillon, *Un lemme de zéros*, Comptes Rendus Acad. Sci. Paris, Ser. I, 335 (2002), 167–170.
- [14] N. Gouillon, *Minorations explicites de formes linéaires en deux logarithmes*, Thèse de Docteur de l’université de la Méditerranée - Aix-Marseille II, (2003) \url https://tel.archives-ouvertes.fr/tel-00003964.
- [15] M. Laurent, *Sur quelques résultats récents de transcendance*, Astérisque 198–200 (1991), 209–230.
- [16] M. Laurent, *Hauteurs de matrices d’interpolation*, Approximations diophantiennes et nombres transcendants, Luminy (1990), ed. P. Philippon, de Gruyter (1992), 215–238.
- [17] M. Laurent, *Linear forms in two logarithms and interpolation determinants*, Acta Arith. 66 (1994), 181–199.
- [18] M. Laurent, Personal communication to M. Mignotte, Nov. 2003.
- [19] M. Laurent, *Linear forms in two logarithms and interpolation determinants II*, Acta Arith. 133 (2008), 325–348.
- [20] M. Laurent, M. Mignotte, Y. Nesterenko, *Formes linéaires en deux logarithmes et déterminants d’interpolation*, J. Number Theory 55 (1995), 285–321.
- [21] A.K. Lenstra, H.W. Lenstra Jr., L. Lovász, *Factoring polynomials with rational coefficients*, Math. Ann. 261 (1982), 515–534.
- [22] E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in logarithms of algebraic numbers. II*, Izv. Ross. Akad. Nauk Ser. Mat. 64 (2000), 125–180. English transl. in Izv. Math. 64 (2000), 1217–1269.
- [23] The PARI Group, PARI/GP version 2.14.0, Univ. Bordeaux, 2021, \url http://pari.math.u-bordeaux.fr/.
- [24] A. Pethő, *Perfect powers in second order linear recurrences*, J. Number Theory 15 (1982), 5–13.
- [25] A. Pethő, B.M.M. de Weger, *Products of Prime Powers in Binary Recurrence Sequences Part I: The hyperbolic Case, with an Application to the generalized Ramanujan-Nagell equation*, Math. Comp. 47 (1986), 713–727.
- [26] P. Philippon, Lemmes de zéros dans les groupes algébriques commutatifs, Bull. Soc. Math. France, 114 (1987), 355–383. Errata et addenda, id., 115 (1987), 397–398.
- [27] J. B. Rosser, L. Schoenfeld, *Approximate Formulas for Some Functions of Prime Numbers*, Ill. J. Math. 6 (1962), 64–94.
- [28] T. N. Shorey, C. L. Stewart, *On the Diophantine equation a ​ x 2 ​ t + b ​ x t ​ y + c ​ y 2 = d ax^{2t}+bx^{t}y+cy^{2}=d and pure powers in recurrence sequences*, Math. Scand. 52 (1983), 24–36.
- [29] R. Tijdeman, *On the equation of Catalan*, Acta Arith. 29 (1976), 197–209.
- [30] N. Tzanakis, B. M. M. de Weger, *On the practical solution of the Thue equation*, J. Number Theory 31 (1989), 99–132.
- [31] M. Waldschmidt, *Diophantine Approximation on Linear Algebraic Groups*, Springer, Berlin, 2000.

## Appendix A A Zero Estimate by Michel Laurent

We revisit the original argument due to Masser [2], establishing zero lemmas in algebraic commutative groups. Starting with a hypersurface, his approach is based on the construction of complete intersections in successive codimensions 2 2, 3 3, …, using subsets of points Σ 1 \Sigma_{1}, Σ 2 \Sigma_{2}, … \ldots as translation operators. Compared with subsequent works, see [3] for instance, the process enables us to control efficiently the possible degeneracies at each step of the construction. We take advantage of this feature to minimise the size of the sets Σ 1 \Sigma_{1}, Σ 2 \Sigma_{2} and Σ 3 \Sigma_{3} occurring in the following proposition.

###### Proposition A.1.

Let 𝕂 \mathbb{K} be an algebraically closed field of characteristic 0 0. Let K 1 K_{1}, K 2 K_{2} and L L be non-negative integers and let Σ 1 \Sigma_{1}, Σ 2 \Sigma_{2} and Σ 3 \Sigma_{3} be finite subsets of the group G = 𝕂 2 × 𝕂 × G=\mathbb{K}^{2}\times\mathbb{K}^{\times} ( ( whose composition law is written additively)). Assume that Σ 1 \Sigma_{1}, Σ 2 \Sigma_{2} and Σ 3 \Sigma_{3} contain the origin ( 0, 0, 1) (0,0,1) of G G and that

(A.1) |  | { Card ⁡ { a ​ x 1 + b ​ x 2: ∃ y ∈ 𝕂 × with ( x 1, x 2, y) ∈ Σ 1 } > max { K 1, K 2 }, ∀ ( a, b) ∈ 𝕂 2 ∖ { ( 0, 0) }, Card ⁡ { y: ∃ ( x 1, x 2) ∈ 𝕂 2 with ( x 1, x 2, y) ∈ Σ 1 } > L, \begin{cases}\card\left\{ax_{1}+bx_{2}:\text{$\exists y\in\mathbb{K}^{\times}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{1}$}\right\}&>\max\left\{K_{1},K_{2}\right\},\hskip 2.84526pt\forall(a,b)\in\mathbb{K}^{2}\setminus\{(0,0)\},\\ \card\left\{y:\text{$\exists\left(x_{1},x_{2}\right)\in\mathbb{K}^{2}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{1}$}\right\}&>L,\end{cases} |  |

(A.2) |  | { Card ⁡ { ( a ​ x 1 + b ​ x 2, y): ( x 1, x 2, y) ∈ Σ 2 } > 2 max { K 1, K 2 } L, ∀ ( a, b) ∈ 𝕂 2 ∖ { ( 0, 0) }, Card ⁡ { ( x 1, x 2): ∃ y ∈ 𝕂 × with ( x 1, x 2, y) ∈ Σ 2 } > 2 ​ K 1 ​ K 2, \begin{cases}\card\left\{\left(ax_{1}+bx_{2},y\right):\left(x_{1},x_{2},y\right)\in\Sigma_{2}\right\}&>2\max\left\{K_{1},K_{2}\right\}L,\hskip 2.84526pt\forall(a,b)\in\mathbb{K}^{2}\setminus\{(0,0)\},\\ \card\left\{\left(x_{1},x_{2}\right):\text{$\exists y\in\mathbb{K}^{\times}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{2}$}\right\}&>2K_{1}K_{2},\end{cases} |  |

and

(A.3) |  | Card ⁡ Σ 3 > 6 ​ K 1 ​ K 2 ​ L. \card\Sigma_{3}>6K_{1}K_{2}L. |  |

Let s s be a non-zero polynomial of 𝕂 ⁡ [X 1, X 2, Y] \mathbb{K}\left[X_{1},X_{2},Y\right], whose partial degrees in the variables X 1, X 2 X_{1},X_{2} and Y Y are bounded by K 1 K_{1}, K 2 K_{2} and L L, respectively. Then s s does not vanish identically on the set Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3}.

Notice that a similar result has been obtained by Gouillon [1] for polynomials s s of total degree in X 1 X_{1} and X 2 X_{2} bounded by 2 ​ max ⁡ { K 1, K 2 } 2\max\left\{K_{1},K_{2}\right\}, with a constant 12 12 instead of 6 6 in the above main condition ( A.3) and where 𝕂 = ℂ \mathbb{K}=\mathbb{C}.

### A.1. Geometrical preliminaries

We embed naturally the group G G in the product

 | 𝐏 = 𝐏 1 ​ ( 𝕂) × 𝐏 1 ​ ( 𝕂) × 𝐏 1 ​ ( 𝕂). \mathbf{P}=\mathbf{P}^{1}(\mathbb{K})\times\mathbf{P}^{1}(\mathbb{K})\times\mathbf{P}^{1}(\mathbb{K}). |  |

For any closed irreducible subvarieties V ⊆ 𝐏 V\subseteq\mathbf{P} of codimension 0 ≤ r ≤ 3 0\leq r\leq 3, and any triple of integers ( a, b, c) (a,b,c) with

 | a ∈ { 0, 1 }, b ∈ { 0, 1 }, c ∈ { 0, 1 } ​ and ​ a + b + c = r, a\in\{0,1\},b\in\{0,1\},c\in\{0,1\}\text{ and }a+b+c=r, |  |

we define the multidegrees δ a, b, c ​ ( V) \delta_{a,b,c}(V) as the intersection degree

 | δ a, b, c ​ ( V) = Card ⁡ { V ∩ π 1 − 1 ​ ( L a) ∩ π 2 − 1 ​ ( L b) ∩ π 3 − 1 ​ ( L c) }, \delta_{a,b,c}(V)=\card\left\{V\ \cap\pi_{1}^{-1}\left(L_{a}\right)\cap\pi_{2}^{-1}\left(L_{b}\right)\cap\pi_{3}^{-1}\left(L_{c}\right)\right\}, |  |

where L a L_{a}, L b L_{b} and L c L_{c} stand for generic linear subvarieties in 𝐏 1 ​ ( 𝕂) \mathbf{P}^{1}(\mathbb{K}) with respective dimensions a a, b b and c c (thus L 1 = 𝐏 1 ​ ( 𝕂) L_{1}=\mathbf{P}^{1}(\mathbb{K}) and L 0 L_{0} is a point) and where the maps π j: 𝐏 → 𝐏 1 ​ ( 𝕂) \pi_{j}:\mathbf{P}\rightarrow\mathbf{P}^{1}(\mathbb{K}) denote the three canonical projections. We also extend to cycles (meaning formal linear combinations with integer coefficients of closed irreducible subvarieties of codimension r r in 𝐏 \mathbf{P}) the above definition of the multidegrees δ a, b, c \delta_{a,b,c}. Let Z Z be a cycle of codimension r ≤ 2 r\leq 2 in 𝐏 \mathbf{P} and let s ∈ 𝕂 ⁡ [X 1, U 1; X 2, U 2; Y, V] s\in\mathbb{K}\left[X_{1},U_{1};X_{2},U_{2};Y,V\right] be a non-zero polynomial which is homogeneous of respective degrees D X 1 D_{X_{1}}, D X 2 D_{X_{2}}, D Y D_{Y} in each of the three pairs of variables ( X 1, U 1) \left(X_{1},U_{1}\right), ( X 2, U 2) \left(X_{2},U_{2}\right) and ( Y, V) (Y,V). Assume that s s does not vanish identically on each component of Z Z. Then Bezout’s Theorem gives us the multidegrees of the intersection cycle Z ⋅ ( s) Z\cdot(s) of codimension r + 1 r+1 in 𝐏 \mathbf{P}. For any a a, b b and c c as above with a + b + c = r + 1 a+b+c=r+1, we have the equalities:

(A.4) |  | δ a, b, c ​ ( Z ⋅ ( s)) = D X 1 ​ δ a − 1, b, c ​ ( Z) + D X 2 ​ δ a, b − 1, c ​ ( Z) + D Y ​ δ a, b, c − 1 ​ ( Z), \delta_{a,b,c}(Z\cdot(s))=D_{X_{1}}\delta_{a-1,b,c}(Z)+D_{X_{2}}\delta_{a,b-1,c}(Z)+D_{Y}\delta_{a,b,c-1}(Z), |  |

where the multidegrees δ \delta appearing on the right-hand side are understood to be zero whenever the indices a − 1 a-1 or b − 1 b-1 or c − 1 c-1 are negative.

Now the above Bezout equalities on 𝐏 \mathbf{P} induce upper bounds on G G in the following way. For any irreducible subvarieties V ⊆ G V\subseteq G, we denote by δ a, b, c ​ ( V) \delta_{a,b,c}(V) the corresponding multidegree δ a, b, c ​ ( V ¯) \delta_{a,b,c}\left(\overline{V}\right) of its Zariski closure V ¯ \overline{V} in 𝐏 \mathbf{P}, and if Z Z is any cycle in G G, that is to say some formal linear combination of irreducible subvarieties of G G of the same codimension, we define δ a, b, c ​ ( Z) \delta_{a,b,c}(Z) by linearity.

Let s 1 s_{1}, s 2 s_{2} and s 3 s_{3} be three non-zero polynomials of 𝕂 ⁡ [X 1, X 2, Y] \mathbb{K}\left[X_{1},X_{2},Y\right] with partial degrees in X 1 X_{1}, X 2 X_{2} and Y Y respectively bounded by K 1 K_{1}, K 2 K_{2} and L L. Denote by Z 1 = ( s 1) Z_{1}=\left(s_{1}\right) the (eventually null) divisor of the zeroes of s 1 s_{1} on G G and assume that s 2 s_{2} does not vanish identically on any component of Z 1 Z_{1}. Let Z 2 = Z 1 ⋅ ( s 2) Z_{2}=Z_{1}\cdot\left(s_{2}\right) be the (eventually null) intersection cycle on G G of codimension 2 2. Assume again that s 3 s_{3} does not vanish identically on any component of Z 2 Z_{2} and put Z 3 = Z 2 ⋅ ( s 3) Z_{3}=Z_{2}\cdot\left(s_{3}\right). Notice that our assumptions mean equivalently that the sequence ( s 1, s 2, s 3) \left(s_{1},s_{2},s_{3}\right) is a regular sequence in the local ring of any common zero of s 1 s_{1}, s 2 s_{2} and s 3 s_{3} on G G. Then the above trihomogeneous version of Bezout’s theorem in equation ( A.4) implies inductively the upper bounds for the multidegrees of the intersection cycles Z 1 Z_{1}, Z 2 Z_{2} and Z 3 Z_{3}:

(A.5) |  | δ 1, 0, 0 ​ ( Z 1) ≤ K 1, δ 0, 1, 0 ​ ( Z 1) ≤ K 2, δ 0, 0, 1 ​ ( Z 1) ≤ L, \delta_{1,0,0}\left(Z_{1}\right)\leq K_{1},\quad\delta_{0,1,0}\left(Z_{1}\right)\leq K_{2},\quad\delta_{0,0,1}\left(Z_{1}\right)\leq L, |  |

(A.6) |  | δ 1, 1, 0 ( Z 2) ≤ 2 K 1 K 2, δ 0, 1, 1 ( Z 2) ≤ 2 K 2 L, δ 1, 0, 1 ( Z 2) ≤ 2 K 1 L and \delta_{1,1,0}\left(Z_{2}\right)\leq 2K_{1}K_{2},\quad\delta_{0,1,1}\left(Z_{2}\right)\leq 2K_{2}L,\quad\delta_{1,0,1}\left(Z_{2}\right)\leq 2K_{1}L\quad\text{and} |  |

(A.7) |  | δ 1, 1, 1 ​ ( Z 3) ≤ 6 ​ K 1 ​ K 2 ​ L. \quad\delta_{1,1,1}\left(Z_{3}\right)\leq 6K_{1}K_{2}L. |  |

### A.2. Proof of Proposition A.1

Suppose on the contrary that there exists a non-zero polynomial s ∈ 𝕂 ⁡ [X 1, X 2, Y] s\in\mathbb{K}\left[X_{1},X_{2},Y\right] with partial degrees in X 1 X_{1}, X 2 X_{2} and Y Y bounded by K 1 K_{1}, K 2 K_{2} and L L and vanishing on Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3}. Then we plan to construct polynomials s 1 s_{1}, s 2 s_{2} and s 3 s_{3} as in Section A.1 and vanishing moreover respectively on the subsets Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3}, Σ 2 + Σ 3 \Sigma_{2}+\Sigma_{3} and Σ 3 \Sigma_{3}. Since

 | δ 1, 1, 1 ​ ( Z 3) ≥ Card ⁡ Σ 3, \delta_{1,1,1}\left(Z_{3}\right)\geq\card\Sigma_{3}, |  |

the assumption ( A.3) of the proposition will contradict equation ( A.7).

We start with s 1 = s s_{1}=s. Notice that the cycle Z 1 = ( s 1) Z_{1}=\left(s_{1}\right) is non-zero since the points Σ 1 + Σ 2 + Σ 3 \Sigma_{1}+\Sigma_{2}+\Sigma_{3} are contained in its support.

Let us construct s 2 s_{2}. Observe first that for any component V V of Z 1 Z_{1}, there exists a translated variety g + V g+V, for some g ∈ Σ 1 g\in\Sigma_{1}, which is not a component of Z 1 Z_{1}. Otherwise by equation ( A.5), we should have the upper bounds

 | Card ⁡ ( Σ 1 / H) ​ δ 1, 0, 0 ​ ( V) ≤ δ 1, 0, 0 ​ ( Z 1) \displaystyle\card\left(\Sigma_{1}/H\right)\delta_{1,0,0}(V)\leq\delta_{1,0,0}\left(Z_{1}\right) | ≤ K 1, \displaystyle\leq K_{1}, |  |

 | Card ⁡ ( Σ 1 / H) ​ δ 0, 1, 0 ​ ( V) ≤ δ 0, 1, 0 ​ ( Z 1) \displaystyle\card\left(\Sigma_{1}/H\right)\delta_{0,1,0}(V)\leq\delta_{0,1,0}\left(Z_{1}\right) | ≤ K 2 and \displaystyle\leq K_{2}\quad\text{and} |  |

 | Card ⁡ ( Σ 1 / H) ​ δ 0, 0, 1 ​ ( V) ≤ δ 0, 0, 1 ​ ( Z 1) \displaystyle\card\left(\Sigma_{1}/H\right)\delta_{0,0,1}(V)\leq\delta_{0,0,1}\left(Z_{1}\right) | ≤ L, \displaystyle\leq L, |  |

where H = { g ∈ G: g + V = V } H=\{g\in G:g+V=V\} is the stabiliser of V V. Clearly H H is an algebraic subgroup of G G and dim H ≤ 2 \dim H\leq 2.

When H = W × 𝕂 × H=W\times\mathbb{K}^{\times}, where W W is either { 0 } \{0\} or a line a ​ X 1 + b ​ X 2 = 0 aX_{1}+bX_{2}=0 in 𝕂 2 \mathbb{K}^{2}, at least one of the degrees δ 1, 0, 0 ​ ( V) \delta_{1,0,0}(V) or δ 0, 1, 0 ​ ( V) \delta_{0,1,0}(V) is positive and we get a contradiction with the first lower bound of ( A.1).

When H = W × μ H=W\times\mu, with a finite multiplicative group μ \mu, then δ 0, 0, 1 ​ ( V) ≥ Card ⁡ ( μ) \delta_{0,0,1}(V)\geq\card(\mu), and we deduce from the last upper bound

 | Card ⁡ { y: ∃ ( x 1, x 2) ∈ 𝕂 2 with ( x 1, x 2, y) ∈ Σ 1 } \displaystyle\card\left\{y:\text{$\exists\left(x_{1},x_{2}\right)\in\mathbb{K}^{2}$ with $\left(x_{1},x_{2},y\right)\in\Sigma_{1}$}\right\} | ≤ Card ⁡ ( Σ 1 / ( W × { 1 })) \displaystyle\leq\card\left(\Sigma_{1}/(W\times\{1\})\right) |  |

 |  | ≤ Card ⁡ ( Σ 1 / ( W × μ)) ​ Card ⁡ ( μ) ≤ L, \displaystyle\leq\card\left(\Sigma_{1}/(W\times\mu)\right)\card(\mu)\leq L, |  |

which contradicts the second lower bound of ( A.1).

Therefore, for some g ∈ Σ 1 g\in\Sigma_{1}, the translated polynomial s 1 ∘ τ g s_{1}\circ\tau_{g} does not vanish identically on V V. Now a generic linear combination s 2 s_{2} of the polynomials s 1 ∘ τ g, g ∈ Σ 1 s_{1}\circ\tau_{g},g\in\Sigma_{1} has the required properties.

We construct s 3 s_{3} in a similar way, proving first that for any component V V of Z 2 = Z 1 ⋅ ( s 2) Z_{2}=Z_{1}\cdot\left(s_{2}\right), the translated varieties g + V, g ∈ Σ 2 g+V,g\in\Sigma_{2}, are not all components of Z 2 Z_{2}. Otherwise we should deduce from ( A.6) the upper bounds

(A.8) |  | Card ⁡ ( Σ 2 / H) ​ δ 1, 1, 0 ​ ( V) ≤ δ 1, 1, 0 ​ ( Z 2) \displaystyle\card\left(\Sigma_{2}/H\right)\delta_{1,1,0}(V)\leq\delta_{1,1,0}\left(Z_{2}\right) | ≤ 2 ​ K 1 ​ K 2, \displaystyle\leq 2K_{1}K_{2}, |  |

 | Card ⁡ ( Σ 2 / H) ​ δ 1, 0, 1 ​ ( V) ≤ δ 1, 0, 1 ​ ( Z 2) \displaystyle\card\left(\Sigma_{2}/H\right)\delta_{1,0,1}(V)\leq\delta_{1,0,1}\left(Z_{2}\right) | ≤ 2 K 1 L and \displaystyle\leq 2K_{1}L\quad\text{and} |  |

 | Card ⁡ ( Σ 2 / H) ​ δ 0, 1, 1 ​ ( V) ≤ δ 0, 1, 1 ​ ( Z 2) \displaystyle\card\left(\Sigma_{2}/H\right)\delta_{0,1,1}(V)\leq\delta_{0,1,1}\left(Z_{2}\right) | ≤ 2 ​ K 2 ​ L, \displaystyle\leq 2K_{2}L, |  |

where H = { g ∈ G: g + V = V } H=\{g\in G:g+V=V\} is again the stabiliser of V V. Now dim H ≤ 1 \dim H\leq 1. When H = { 0 } × 𝕂 × H=\{0\}\times\mathbb{K}^{\times}, the curve V V is some line ( u, v, 𝕂 ×) \left(u,v,\mathbb{K}^{\times}\right) and δ 1, 1, 0 ​ ( V) = 1 \delta_{1,1,0}(V)=1. Then the first upper bound in ( A.8) contradicts the second lower bound of ( A.2).

Suppose now that H = W × μ H=W\times\mu, where μ \mu is a finite multiplicative group and W W is either { 0 } \{0\} or a line a ​ X 1 + b ​ X 2 = 0 aX_{1}+bX_{2}=0. The projection π 1 × π 2 \pi_{1}\times\pi_{2} restricted to V V is then a finite map on to its image in 𝕂 2 \mathbb{K}^{2} of degree ≥ Card ⁡ ( μ) \geq\card(\mu). Then at least one of the multidegrees δ 1, 0, 1 ​ ( V) \delta_{1,0,1}(V) or δ 0, 1, 1 ​ ( V) \delta_{0,1,1}(V) is ≥ Card ⁡ ( μ) \geq\card(\mu). Thus we find the upper bounds

 | Card ⁡ { ( a ​ x 1 + b ​ x 2, y): ( x 1, x 2, y) ∈ Σ 2 } \displaystyle\card\left\{\left(ax_{1}+bx_{2},y\right):\left(x_{1},x_{2},y\right)\in\Sigma_{2}\right\} | ≤ Card ⁡ ( Σ 2 / ( W × { 1 })) \displaystyle\leq\card\left(\Sigma_{2}/(W\times\{1\})\right) |  |

 |  | ≤ Card ⁡ ( Σ 2 / ( W × μ)) ​ Card ⁡ ( μ) ≤ 2 ​ max ​ { K 1, K 2 } ​ L, \displaystyle\leq\card\left(\Sigma_{2}/(W\times\mu)\right)\card(\mu)\leq 2\max\left\{K_{1},K_{2}\right\}L, |  |

which contradict the first lower bound of ( A.2).

Finally, we take for s 3 s_{3} a generic linear combination of the polynomials s 1 ∘ τ g s_{1}\circ\tau_{g} and s 2 ∘ τ g s_{2}\circ\tau_{g}, for g ∈ Σ 2 g\in\Sigma_{2}.

## References

- [1] N. Gouillon, Un lemme de zéros, Comptes Rendus Acad. Sci. Paris, Ser. I, 335 (2002), 167–170.
- [2] D. W. Masser, On polynomials and exponential polynomials in several variables, Invent. Math. 63 (1981), 81–95.
- [3] P. Philippon, Lemmes de zéros dans les groupes algébriques commutatifs, Bull. Soc. Math. France, 114 (1987), 355–383. Errata et addenda, id., 115 (1987), 397–398.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:mignotte@math.unistra.fr
[4]: mailto:paul.voutier@gmail.com
