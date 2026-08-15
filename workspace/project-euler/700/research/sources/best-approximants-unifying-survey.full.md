<!-- source: https://arxiv.org/html/2312.13988 | converted from HTML -->

A unifying theory for metrical results on regular continued fraction convergents and mediants

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-NC-ND 4.0][2]

arXiv:2312.13988v3 [math.DS] 07 Nov 2025

# A unifying theory for metrical results on regular continued fraction convergents and mediants Thanks: First published in *Math. Comp.*94 (2025), published by the American Mathematical Society. © 2025 American Mathematical Society.

Karma Dajani Address: Department of Mathematics, Utrecht University, P.O. Box 80010, 3508 TA Utrecht, The Netherlands Email address: [k.dajani@uu.nl][3], Cor Kraaikamp Address: Delft University of Technology, EWI (DIAM), Mekelweg 4, 2628 CD Delft, The Netherlands Email address: [c.kraaikamp@tudelft.nl][4] and Slade Sanderson Address: Université Paris Cité, CNRS, IRIF, F-75013, Paris, France Email address: [slade.sanderson@irif.fr][5]

Date: August 11, 2026

###### Abstract.

We revisit Ito’s ( [27]) natural extension of the Farey tent map, which generates all regular continued fraction convergents and mediants of a given irrational. With a slight shift in perspective on the order in which these convergents and mediants arise, this natural extension is shown to provide an elegant and powerful tool in the metric theory of continued fractions. A wealth of old and new results—including limiting distributions of approximation coefficients, analogues of a theorem of Legendre and their refinements, and a generalisation of Lévy’s Theorem to subsequences of convergents and mediants—are presented as corollaries within this unifying theory.

###### Key words and phrases:

continued fractions, metric theory, ergodic theory

###### 2020 Mathematics Subject Classification

11K50 (Primary) 11A55, 11J70 (Secondary)

## 1. Introduction

Ever since the pioneering work by Shunji Ito, Hitoshi Nakada and Shigeru Tanaka in the late 1970s and early 1980s on the natural extensions of two different classes of continued fraction algorithms (see [48, 50]), natural extensions have played a pivotal role in understanding the metric and arithmetic properties of various families of continued fraction algorithms; see for example 1 1 1 Note this list is far from complete! Nakada’s α \alpha -expansions ( [40, 47, 18]), the Tanaka-Ito α \alpha -expansions ( [10, 49]), the Katok-Ugarcovici ( a, b) (a,b) -continued fractions ( [32, 33, 34, 1]), Rosen fractions ( [8, 41, 38, 42]) and its recent generalisations ( [9]). But also for other number theoretic expansions, such as Lüroth expansions and β \beta -expansions ( [3, 13, 11, 16]), the natural extension turned out to be a very important tool. For example, it gives us an alternative method to find the absolutely continuous invariant measure, to prove weak-Bernoullicity of the β \beta -transformation, and to relate these expansions to Lüroth-series via inducing ( [11]).

In 1989, Shunji Ito published his groundbreaking paper on mediant convergents ( [27]). If x x is a real irrational number, with *regular continued fraction*( rcf) expansion x = [a 0; a 1, a 2, …] x=[a_{0};a_{1},a_{2},\dots], and with regular convergents p n / q n = [a 0; a 1, …, a n] p_{n}/q_{n}=[a_{0};a_{1},\dots,a_{n}] for n ≥ 1 n\geq 1, then the *mediant convergents*of x x are given by:

 | λ ​ p n + p n − 1 λ ​ q n + q n − 1, for λ ∈ ℕ, 1 ≤ λ < a n + 1. \frac{\lambda p_{n}+p_{n-1}}{\lambda q_{n}+q_{n-1}},\quad\text{for $\lambda\in\mathbb{N}$, $1\leq\lambda<a_{n+1}$}. |  |

*Best approximants*2 2 2 This definition of a best approximant is sometimes called a best approximant *of the first kind*. Best approximants *of the second kind*are defined analogously, but with inequality ( 1.1) replaced by | e ​ x − d | ≤ | q ​ x − p | |ex-d|\leq|qx-p|. Best approximants of the second kind are classified as rcf -convergents of x x; see [54]. of an irrational number x x are fractions p / q p/q, q > 0, q>0, in lowest terms, with the property that any other fraction d / e d/e in lowest terms with e > 0 e>0 satisfies

(1.1) |  | | x − d e | ≤ | x − p q | implies that e > q. \left|x-\frac{d}{e}\right|\leq\left|x-\frac{p}{q}\right|\quad\text{implies that}\quad e>q. |  |

Now every best approximant is either a regular convergent or a mediant; see [4].

Classically, regular continued fraction convergents of an irrational number x x have ‘excellent’ approximation properties. For example, a result by Legendre states that if p, q ∈ ℤ p,q\in\mathbb{Z} with q > 0, gcd ​ { p, q } = 1 q>0,\ \text{gcd}\{p,q\}=1 and

 | | x − p q | < 1 2 ​ q 2, \left|x-\frac{p}{q}\right|<\frac{1}{2q^{2}}, |  |

then p / q p/q is a regular continued fraction convergent of x x, i.e., there exists an n n such that p = p n p=p_{n} and q = q n q=q_{n}. Furthermore, one can show that if θ n ​ ( x):= q n 2 ​ | x − p n q n | \theta_{n}(x):=q_{n}^{2}\left|x-\frac{p_{n}}{q_{n}}\right| for any n ∈ ℕ n\in\mathbb{N}, then for every irrational x x and every n ∈ ℕ n\in\mathbb{N} one has

 | min ⁡ { θ n − 1 ​ ( x), θ n ​ ( x), θ n + 1 ​ ( x) } < 1 a n + 1 2 + 4 ≤ 1 5. \min\{\theta_{n-1}(x),\theta_{n}(x),\theta_{n+1}(x)\}<\frac{1}{\sqrt{a_{n+1}^{2}+4}}\leq\frac{1}{\sqrt{5}}. |  |

For proofs of these results, see [15] and the references therein.

In his 1989 paper, Ito studied the natural extension of the so-called *Farey tent map*, an algorithm ‘underlying’ the regular continued fraction expansion which yields all the convergents and mediants of the rcf. Ito obtained various metric results on these mediant convergents. In spite of its groundbreaking nature, Ito’s paper has generated relatively little attention; see for example [6, 31, 7, 14, 25]. In this paper we want to ‘repair’ this by exploring the possibilities this natural extension of the Farey tent map yields. In particular, we exploit the fact that the quantities

 | ( λ ​ q n + q n − 1) 2 ​ | x − λ ​ p n + p n − 1 λ ​ q n + q n − 1 |, 0 ≤ λ < a n + 1, (\lambda q_{n}+q_{n-1})^{2}\left|x-\frac{\lambda p_{n}+p_{n-1}}{\lambda q_{n}+q_{n-1}}\right|,\quad 0\leq\lambda<a_{n+1}, |  |

may be written explicitly in terms of the forward orbit of ( x, 1) (x,1) under Ito’s natural extension (see Proposition 5.1). This fact was essentially known and used in [27] and [7], where the orbit is put into one-to-one correspondence with the sequence of rcf -convergents and mediants of x x, ordered with increasing denominators. However, we consider a natural rearrangement of this sequence of convergents and mediants which lends itself to a geometrically intuitive one-to-one correspondence with the aforementioned orbit. This will lead to unified and simple proofs of results from the just mentioned papers [27, 6, 31, 7], old and classical results by Legendre and Koksma, and various new results such as generalizations of Lévy’s constant and of the Doeblin–Lenstra conjecture to subsequences of convergents and mediants.

This paper is organised as follows: In § 2 we set notation and recall basic facts regarding (semi-)regular continued fractions (§ 2.1), the Gauss map underlying rcf -expansions (§ 2.2), the Farey tent map (§ 2.3) and the Lehner map and its associated semi-regular continued fraction expansions (§ 2.4). In § 3, the Farey tent map is shown to generate semi-regular continued fractions (§ 3.1) whose convergents (§ 3.2) consist of all rcf -convergents and mediants of a given irrational. Special emphasis is placed on the order in which these *Farey convergents*arise, and which *differs*from that historically studied in the literature. In an appendix (§ 6), it is shown that these two orderings do not affect the statements of central results in § 5, and thus a number of old results are re-obtained from our approach. Section 4 recalls Ito’s natural extension of the Farey tent map and the relationship between its dynamics and Farey convergents. Subsection 4.1 sets the framework for inducing Ito’s natural extension to obtain desired subsequences of Farey convergents, and in § 4.2 we prove central results on the equidistribution of the orbit of ( x, 1) (x,1) under the induced maps. The main metrical results—old and new—are contained in § 5. Here we consider limiting distributions of approximation coefficients (§ 5.1), Legendre-type theorems (§ 5.2), consecutive approximation coefficients (§ 5.3) and generalisations of results of Lévy (§ 5.4).

Acknowledgments. We thank the anonymous referees whose comments greatly improved the exposition of this paper. This work is part of project number 613.009.135 of the research programme Mathematics Clusters which is financed by the Dutch Research Council (NWO).

## 2. Background, definitions and notation

### 2.1. (Semi-)regular continued fractions

A semi-regular continued fraction ( srcf) is a formal (infinite or finite) expression of the form

 | [β 0; α 1 / β 1, α 2 / β 2, …] = β 0 + α 1 β 1 + α 2 β 2 + ⋱ [\beta_{0};\alpha_{1}/\beta_{1},\alpha_{2}/\beta_{2},\dots]=\beta_{0}+\cfrac{\alpha_{1}}{\beta_{1}+\cfrac{\alpha_{2}}{\beta_{2}+\ddots}} |  |

with β 0 ∈ ℤ \beta_{0}\in\mathbb{Z}, and for each n ≥ 1, α n = ± 1 n\geq 1,\ \alpha_{n}=\pm 1 and β n ≥ 1 \beta_{n}\geq 1 integers satisfying

 | α n + 1 + β n ≥ 1, \alpha_{n+1}+\beta_{n}\geq 1, |  |

and—in the infinite case—

 | α n + 1 + β n ≥ 2 \alpha_{n+1}+\beta_{n}\geq 2 |  |

infinitely often. Set

 | B 0 = B 0 ​ ( [β 0; α 1 / β 1, …]):= ( 1 β 0 0 1) and B n = B n ​ ( [β 0; α 1 / β 1, …]):= ( 0 α n 1 β n), n > 0, B_{0}=B_{0}([\beta_{0};\alpha_{1}/\beta_{1},\dots]):=\begin{pmatrix}1&\beta_{0}\\ 0&1\end{pmatrix}\quad\text{and}\quad B_{n}=B_{n}([\beta_{0};\alpha_{1}/\beta_{1},\dots]):=\begin{pmatrix}0&\alpha_{n}\\ 1&\beta_{n}\end{pmatrix},\quad n>0, |  |

and for 0 ≤ i ≤ j 0\leq i\leq j,

 | B [i, j] = B [i, j] ( [β 0; α 1 / β 1, …]):= B i B i + 1 ⋯ B j. B_{[i,j]}=B_{[i,j]}([\beta_{0};\alpha_{1}/\beta_{1},\dots]):=B_{i}B_{i+1}\cdots B_{j}. |  |

For a matrix A = ( a b c d) A=\left(\begin{smallmatrix}a&b\\ c&d\end{smallmatrix}\right), we denote by A ⋅ z:= a ​ z + b c ​ z + d, z ∈ ℝ ∪ { ∞ }, A\cdot z:=\frac{az+b}{cz+d},\ z\in\mathbb{R}\cup\{\infty\}, the action of A A as a Möbius transformation. Writing the entries of B [0, n] B_{[0,n]} as ( R n P n S n Q n) \left(\begin{smallmatrix}R_{n}&P_{n}\\ S_{n}&Q_{n}\end{smallmatrix}\right), the fraction

 | P n Q n:= B [0, n] ⋅ 0 = β 0 + α 1 β 1 + α 2 ⋱ + α n β n = [β 0; α 1 / β 1, …, α n / β n] ∈ ℚ \frac{P_{n}}{Q_{n}}:=B_{[0,n]}\cdot 0=\beta_{0}+\cfrac{\alpha_{1}}{\beta_{1}+\cfrac{\alpha_{2}}{\ddots+\cfrac{\alpha_{n}}{\beta_{n}}}}=[\beta_{0};\alpha_{1}/\beta_{1},\dots,\alpha_{n}/\beta_{n}]\in\mathbb{Q} |  |

is called the n th n^{\text{th}} convergent of [β 0; α 1 / β 1, α 2 / β 2, …] [\beta_{0};\alpha_{1}/\beta_{1},\alpha_{2}/\beta_{2},\dots]. By Tietze’s Convergence Theorem (see, say, [53]) the above conditions on the digits α n \alpha_{n} and β n \beta_{n} guarantee that x = lim n → ∞ P n Q n ∈ ℝ x=\lim_{n\to\infty}\frac{P_{n}}{Q_{n}}\in\mathbb{R} always exists, and thus we call [β 0; α 1 / β 1, α 2 / β 2, …] [\beta_{0};\alpha_{1}/\beta_{1},\alpha_{2}/\beta_{2},\dots] a srcf -expansion of x x and refer to the convergents P n / Q n P_{n}/Q_{n} as convergents of x x. 3 3 3 We emphasise that a real number x x has many srcf -expansions, and the convergents of x x depend on the expansion in question. The convergents P n / Q n P_{n}/Q_{n} of any srcf -expansion of x ∈ ℝ x\in\mathbb{R} are reduced, as det ( B 0) = 1 \det(B_{0})=1 and det ( B [0, n]) = α 1 ⋯ α n ( − 1) n ∈ { ± 1 } \det(B_{[0,n]})=\alpha_{1}\cdots\alpha_{n}(-1)^{n}\in\{\pm 1\}, for n ≥ 1 n\geq 1. Notice for any n ≥ 0 n\geq 0 that

 | ( R n + 1 P n + 1 S n + 1 Q n + 1) = B [0, n] ​ B n + 1 = ( R n P n S n Q n) ​ ( 0 α n + 1 1 β n + 1) = ( P n β n + 1 ​ P n + α n + 1 ​ R n Q n β n + 1 ​ Q n + α n + 1 ​ S n). \begin{pmatrix}R_{n+1}&P_{n+1}\\ S_{n+1}&Q_{n+1}\end{pmatrix}=B_{[0,n]}B_{n+1}=\begin{pmatrix}R_{n}&P_{n}\\ S_{n}&Q_{n}\end{pmatrix}\begin{pmatrix}0&\alpha_{n+1}\\ 1&\beta_{n+1}\end{pmatrix}=\begin{pmatrix}P_{n}&\beta_{n+1}P_{n}+\alpha_{n+1}R_{n}\\ Q_{n}&\beta_{n+1}Q_{n}+\alpha_{n+1}S_{n}\end{pmatrix}. |  |

In particular, R n + 1 = P n R_{n+1}=P_{n} and S n + 1 = Q n S_{n+1}=Q_{n}. In view of the definition of B [0, 0] = B 0 B_{[0,0]}=B_{0}, we set P − 1:= R 0 = 1 P_{-1}:=R_{0}=1 and Q − 1:= S 0 = 0 Q_{-1}:=S_{0}=0, and call P − 1 / Q − 1 = 1 / 0 = ∞ P_{-1}/Q_{-1}=1/0=\infty the ( − 1) st (-1)^{\text{st}} convergent of [β 0; α 1 / β 1, α 2 / β 2, …] [\beta_{0};\alpha_{1}/\beta_{1},\alpha_{2}/\beta_{2},\dots] and of x x. This gives the following recurrence relations for all n ≥ 0 n\geq 0:

(2.1) |  | P n + 1 \displaystyle P_{n+1} | = β n + 1 ​ P n + α n + 1 ​ P n − 1, \displaystyle=\beta_{n+1}P_{n}+\alpha_{n+1}P_{n-1},\qquad | P − 1 = 1, \displaystyle P_{-1}=1,\  | P 0 = β 0, \displaystyle P_{0}=\beta_{0}, |  |

 | Q n + 1 \displaystyle Q_{n+1} | = β n + 1 ​ Q n + α n + 1 ​ Q n − 1, \displaystyle=\beta_{n+1}Q_{n}+\alpha_{n+1}Q_{n-1},\qquad | Q − 1 = 0, \displaystyle Q_{-1}=0,\  | Q 0 = 1. \displaystyle Q_{0}=1. |  |

A regular continued fraction ( rcf) is a semi-regular continued fraction with α n = 1, n ≥ 1 \alpha_{n}=1,\ n\geq 1 (note that the conditions of a srcf are now trivially satisfied for any β n ≥ 1 \beta_{n}\geq 1). A rcf is also denoted by

 | [a 0; a 1, a 2, …]:= [a 0; 1 / a 1, 1 / a 2, …] [a_{0};a_{1},a_{2},\dots]:=[a_{0};1/a_{1},1/a_{2},\dots] |  |

and its sequence of convergents by ( p n / q n) n ≥ − 1 (p_{n}/q_{n})_{n\geq-1}. The digit a n a_{n} is the *n th n^{\text{th}} partial quotient*of x = [a 0; a 1, a 2, …] x=[a_{0};a_{1},a_{2},\dots]. The mediant convergents (or, simply, *mediants*) of x x are defined as the fractions

 | λ ​ p n + p n − 1 λ ​ q n + q n − 1, for λ ∈ ℕ, 1 ≤ λ < a n + 1. \frac{\lambda p_{n}+p_{n-1}}{\lambda q_{n}+q_{n-1}},\quad\text{for $\lambda\in\mathbb{N}$, $1\leq\lambda<a_{n+1}$}. |  |

### 2.2. The Gauss map

The Gauss map G: [0, 1] → [0, 1] G:[0,1]\to[0,1] is defined by G ⁡ ( 0) = 0 G(0)=0 and G ⁡ ( x) = 1 / x − ⌊ 1 / x ⌋, x > 0 G(x)=1/x-\lfloor 1/x\rfloor,\ x>0 (see Figure 1). 4 4 4 While G G may also be defined as a self-map of [0, 1) [0,1), we choose to include the endpoint 1 1 in our definition for later notational purposes. For x ∈ ℝ x\in\mathbb{R}, let a 0 = a 0 ​ ( x):= ⌊ x ⌋ a_{0}=a_{0}(x):=\lfloor x\rfloor and x 0:= x − a 0 ∈ [0, 1) x_{0}:=x-a_{0}\in[0,1). Define a ⁡ ( x):= ⌊ 1 / x ⌋, x ≠ 0 a(x):=\lfloor 1/x\rfloor,\ x\neq 0, and set a n = a n ​ ( x):= a ⁡ ( G n − 1 ​ ( x 0)), G n − 1 ​ ( x 0) ≠ 0 a_{n}=a_{n}(x):=a(G^{n-1}(x_{0})),\ G^{n-1}(x_{0})\neq 0. With this notation, for G n − 1 ​ ( x 0) ≠ 0 G^{n-1}(x_{0})\neq 0,

 | G n ​ ( x 0) = 1 G n − 1 ​ ( x 0) − a n, G^{n}(x_{0})=\frac{1}{G^{n-1}(x_{0})}-a_{n}, |  |

which can be rewritten as

 | G n − 1 ​ ( x 0) = 1 a n + G n ​ ( x 0). G^{n-1}(x_{0})=\frac{1}{a_{n}+G^{n}(x_{0})}. |  |

Repeatedly applying this last relation, one finds that

(2.2) |  | x = a 0 + 1 a 1 + 1 a 2 + ⋱ + 1 a n + G n ​ ( x 0) = [a 0; a 1, …, a n − 1, a n + G n ​ ( x 0)]. x=a_{0}+\cfrac{1}{a_{1}+\cfrac{1}{a_{2}+\ddots+\cfrac{1}{a_{n}+G^{n}(x_{0})}}}=[a_{0};a_{1},\dots,a_{n-1},a_{n}+G^{n}(x_{0})]. |  |

From the Euclidean algorithm it follows that for every rational x x there exists an n ≥ 0 n\geq 0 such that G n ​ ( x 0) = 0 G^{n}(x_{0})=0, and we see that the rcf -expansion of x ∈ ℚ x\in\mathbb{Q} generated by G G is finite. In fact, every rational x x has precisely two rcf -expansions, the first of which is generated by G G:

(2.3) |  | x = [a 0; a 1, …, a n] and x = [a 0; a 1, …, a n − 1, 1], x=[a_{0};a_{1},\dots,a_{n}]\quad\text{and}\quad x=[a_{0};a_{1},\dots,a_{n}-1,1], |  |

where a n ≥ 2 a_{n}\geq 2 when n ≥ 1 n\geq 1 (that is, when x ∉ ℤ x\notin\mathbb{Z}). The *depth*of x ∈ ℚ x\in\mathbb{Q} is the number n n occurring in the above two expansions.

For x ∈ ℝ \ ℚ x\in\mathbb{R}\backslash\mathbb{Q}, taking n → ∞ n\to\infty in ( 2.2), we see that the Gauss map G G generates a (unique) rcf -expansion [a 0; a 1, a 2, …] [a_{0};a_{1},a_{2},\dots] of x x. It is well known that the dynamical system ( [0, 1], ℬ, ν G, G) ([0,1],\mathcal{B},\nu_{G},G) is ergodic, where ℬ \mathcal{B} denotes the Borel σ \sigma -algebra and ν G \nu_{G} is the Gauss measure with density 1 log ⁡ 2 ​ ( 1 + x) \frac{1}{\log 2(1+x)} (see, say, [15]).

Let Ω:= [0, 1] 2 \Omega:=[0,1]^{2}, and define 𝒢: Ω → Ω \mathcal{G}:\Omega\to\Omega by 𝒢 ⁡ ( 0, y) = ( 0, y) \mathcal{G}(0,y)=(0,y) and, for x ≠ 0 x\neq 0,

 | 𝒢 ⁡ ( x, y):= ( G ⁡ ( x), 1 a ⁡ ( x) + y). \mathcal{G}(x,y):=\left(G(x),\frac{1}{a(x)+y}\right). |  |

For ( x, y) ∈ Ω, x ∈ ( 0, 1), (x,y)\in\Omega,\ x\in(0,1), with rcf -expansions ( x, y) = ( [0; a 1, a 2, …], [0; b 1, b 2, …]) (x,y)=([0;a_{1},a_{2},\dots],[0;b_{1},b_{2},\dots]), the map 𝒢 \mathcal{G} acts as a two-dimensional shift

(2.4) |  | 𝒢 ⁡ ( x, y) = ( [0; a 2, a 3, a 4, …], [0; a 1, b 1, b 2, …]). \mathcal{G}(x,y)=([0;a_{2},a_{3},a_{4},\dots],[0;a_{1},b_{1},b_{2},\dots]). |  |

In [48, 50], the authors show that the ergodic system ( Ω, ℬ, ν ¯ G, 𝒢) (\Omega,\mathcal{B},\bar{\nu}_{G},\mathcal{G}) is the natural extension of ( [0, 1], ℬ, ν G, G) ([0,1],\mathcal{B},\nu_{G},G), where d ​ ν ¯ G = d ​ x ​ d ​ y log ⁡ 2 ​ ( 1 + x ​ y) 2 d\bar{\nu}_{G}=\frac{dxdy}{\log 2(1+xy)^{2}} (see also [15, 12]). In fact, ( Ω, ℬ, ν ¯ G, 𝒢) (\Omega,\mathcal{B},\bar{\nu}_{G},\mathcal{G}) and ( [0, 1], ℬ, ν G, G) ([0,1],\mathcal{B},\nu_{G},G) are strongly mixing ( [24]).

### 2.3. The Farey tent map

Figure 1. The Gauss map G G (black) and the Farey tent map F F (blue). Both maps coincide on the domain [1 / 2, 1] [1/2,1].

Let F: [0, 1] → [0, 1] F:[0,1]\to[0,1] denote the Farey tent map given by

 | F ⁡ ( x):= { x / ( 1 − x), x ≤ 1 / 2, ( 1 − x) / x, x > 1 / 2; F(x):=\begin{cases}x/(1-x),&x\leq 1/2,\\ (1-x)/x,&x>1/2;\end{cases} |  |

see Figure 1. The dynamical system ( [0, 1], ℬ, μ, F) ([0,1],\mathcal{B},\mu,F) is ergodic, where μ \mu is the absolutely continuous, infinite, σ \sigma -finite, F F -invariant measure with density 1 / x 1/x ( [17, 52, 27]). It follows from the definition of F F that if x ∈ ( 0, 1) x\in(0,1) has rcf -expansion x = [0; a 1, a 2, a 3 ​ …] x=[0;a_{1},a_{2},a_{3}\dots], then

(2.5) |  | F ⁡ ( x) = { [0; a 1 − 1, a 2, a 3, …], a 1 > 1, [0; a 2, a 3, a 4, …], a 1 = 1. F(x)=\begin{cases}[0;a_{1}-1,a_{2},a_{3},\dots],&a_{1}>1,\\ [0;a_{2},a_{3},a_{4},\dots],&a_{1}=1.\end{cases} |  |

From this, one finds that the Gauss map G G is the jump transformation of F F associated to the interval ( 1 / 2, 1] (1/2,1]; in particular, for x x as above,

 | min ⁡ { j ≥ 0 | F j ​ ( x) ∈ ( 1 / 2, 1] } = a 1 − 1, and G ⁡ ( x) = F a 1 ​ ( x). \min\{j\geq 0\ |\ F^{j}(x)\in(1/2,1]\}=a_{1}-1,\quad\text{and}\quad G(x)=F^{a_{1}}(x). |  |

Define ε: [0, 1] → { 0, 1 } \varepsilon:[0,1]\to\{0,1\} by

 | ε ⁡ ( x):= { 0, x ≤ 1 / 2, 1, x > 1 / 2, \varepsilon(x):=\begin{cases}0,&x\leq 1/2,\\ 1,&x>1/2,\end{cases} |  |

and for x ∈ [0, 1] x\in[0,1] and n ≥ 1 n\geq 1, set ε n = ε n ​ ( x):= ε ⁡ ( F n − 1 ​ ( x)) \varepsilon_{n}=\varepsilon_{n}(x):=\varepsilon(F^{n-1}(x)). From ( 2.5), it follows that for x = [0; a 1, a 2, …] x=[0;a_{1},a_{2},\dots],

(2.6) |  | ε 1 ε 2 ε 3 ⋯ = 0 a 1 − 1 10 a 2 − 1 10 a 3 − 1 1 ⋯ \varepsilon_{1}\varepsilon_{2}\varepsilon_{3}\cdots=0^{a_{1}-1}10^{a_{2}-1}10^{a_{3}-1}1\cdots |  |

(see also [27]).

### 2.4. Lehner expansions

It was shown in [27] that the Farey tent map generates all convergents and mediant convergents of the rcf -expansion of any irrational x ∈ ( 0, 1) x\in(0,1). Originally there was no continued fraction algorithm ‘attached’ to the Farey tent map F F. Such a continued fraction expansion does exist, and can be obtain via the so-called Lehner map L L, which was introduced by Joe Lehner in 1994; see [45], and also [14].

Let L: [1, 2] → [1, 2] L:[1,2]\to[1,2] be given by

 | L ⁡ ( x):= { 1 / ( 2 − x), x ≤ 3 / 2, 1 / ( x − 1), x > 3 / 2, L(x):=\begin{cases}1/(2-x),&x\leq 3/2,\\ 1/(x-1),&x>3/2,\end{cases} |  |

and for x ∈ [1, 2] x\in[1,2] and each n ≥ 0 n\geq 0, set

 | ( b n, e n + 1) = ( b n ​ ( x), e n + 1 ​ ( x)):= { ( 2, − 1), L n ​ ( x) ≤ 3 / 2, ( 1, 1), L n ​ ( x) > 3 / 2. (b_{n},e_{n+1})=(b_{n}(x),e_{n+1}(x)):=\begin{cases}(2,-1),&L^{n}(x)\leq 3/2,\\ (1,1),&L^{n}(x)>3/2.\end{cases} |  |

The digits ( b n, e n + 1) (b_{n},e_{n+1}) generate the so-called Lehner expansion of x ∈ [1, 2] x\in[1,2],

(2.7) |  | x = [b 0; e 1 / b 1, e 2 / b 2, …], x=[b_{0};e_{1}/b_{1},e_{2}/b_{2},\dots], |  |

which is a srcf -expansion (see [45, 14]).

## 3. Farey expansions and convergents

### 3.1. Farey expansions

As noted above, Ito ( [27]) studied the ergodic properties of the dynamical system ( [0, 1], ℬ, μ, F) ([0,1],\mathcal{B},\mu,F) without any explicit mention of associated (semi-regular) continued fraction expansions, while Lehner ( [45]) studied expansions of the form ( 2.7) generated by L L but no dynamical properties of this map. In [14] it is observed that the dynamical systems ( [0, 1], ℬ, μ, F) ([0,1],\mathcal{B},\mu,F) and ( [1, 2], ℬ, ρ, L) ([1,2],\mathcal{B},\rho,L) are isomorphic via the translation x ↦ x + 1 x\mapsto x+1, where d ​ ρ = d ​ x / ( x − 1) d\rho=dx/(x-1). Via this isomorphism, the map F F can be used to generate a Farey expansion for each x ∈ [0, 1] x\in[0,1] (see also [26]). Indeed, fix x ∈ [0, 1] x\in[0,1], and let [b 0; e 1 / b 1, e 2 / b 2, …] [b_{0};e_{1}/b_{1},e_{2}/b_{2},\dots] be the Lehner expansion of x + 1 x+1. Then [b 0 − 1; e 1 / b 1, e 2 / b 2, …] [b_{0}-1;e_{1}/b_{1},e_{2}/b_{2},\dots] is a srcf -expansion of x x, and we find that

 | ( b n, e n + 1) \displaystyle(b_{n},e_{n+1}) | = { ( 2, − 1), L n ​ ( x + 1) ≤ 3 / 2 ( 1, 1), L n ​ ( x + 1) > 3 / 2 } = { ( 2, − 1), F n ​ ( x) ≤ 1 / 2 ( 1, 1), F n ​ ( x) > 1 / 2 } \displaystyle=\left.\begin{cases}(2,-1),&L^{n}(x+1)\leq 3/2\\ (1,1),&L^{n}(x+1)>3/2\end{cases}\right\}=\left.\begin{cases}(2,-1),&F^{n}(x)\leq 1/2\\ (1,1),&F^{n}(x)>1/2\end{cases}\right\} |  |

 |  | = { ( 2, − 1), ε n + 1 = 0 ( 1, 1), ε n + 1 = 1 } = ( 2 − ε n + 1, 2 ε n + 1 − 1). \displaystyle=\left.\begin{cases}(2,-1),&\varepsilon_{n+1}=0\\ (1,1),&\varepsilon_{n+1}=1\end{cases}\right\}=(2-\varepsilon_{n+1},2\varepsilon_{n+1}-1). |  |

Hence F F generates the Farey expansion

 | x = [b 0 − 1; e 1 / b 1, e 2 / b 2, …], x=[b_{0}-1;e_{1}/b_{1},e_{2}/b_{2},\dots], |  |

where

(3.1) |  | ( b n, e n + 1) = ( 2 − ε n + 1, 2 ​ ε n + 1 − 1), n ≥ 0. (b_{n},e_{n+1})=(2-\varepsilon_{n+1},2\varepsilon_{n+1}-1),\quad n\geq 0. |  |

The corresponding convergents P n / Q n = [b 0 − 1; e 1 / b 1, e 2 / b 2, …, e n / b n] P_{n}/Q_{n}=[b_{0}-1;e_{1}/b_{1},e_{2}/b_{2},\dots,e_{n}/b_{n}] are called the Farey convergents of x x.

### 3.2. Farey convergents

Fix an irrational x ∈ ( 0, 1) x\in(0,1) with rcf -expansion x = [0; a 1, a 2, …] x=[0;a_{1},a_{2},\dots] and convergents p n / q n p_{n}/q_{n}. In [27] and [14] it is shown that F F (respectively L L) generates all convergents and mediants of the rcf -expansion of x x (respectively x + 1 x+1). We reproduce this fact for F F here, fixing notation 5 5 5 Notation is largely recycled from [27]; however, matrix entries are permuted so as to conform with modern notation of their action via Möbius transformations. along the way and paying special attention to the order in which these convergents and mediants arise.

Set

 | A 0:= ( 1 0 1 1) and A 1:= ( 0 1 1 1), A_{0}:=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}\quad\text{and}\quad A_{1}:=\begin{pmatrix}0&1\\ 1&1\end{pmatrix}, |  |

or, more succinctly,

(3.2) |  | A ε:= ( 1 − ε ε 1 1), ε ∈ { 0, 1 }. A_{\varepsilon}:=\begin{pmatrix}1-\varepsilon&\varepsilon\\ 1&1\end{pmatrix},\quad\varepsilon\in\{0,1\}. |  |

Note that as Möbius transformations, A 0 − 1 A_{0}^{-1} and A 1 − 1 A_{1}^{-1} correspond to the left and right branches of F F, respectively. In particular, F ⁡ ( x) = A ε ⁡ ( x) − 1 ⋅ x, F(x)=A_{\varepsilon(x)}^{-1}\cdot x, so x = A ε ⁡ ( x) ⋅ F ⁡ ( x) x=A_{\varepsilon(x)}\cdot F(x). Setting x n:= F n ​ ( x) x_{n}:=F^{n}(x) for n ≥ 0 n\geq 0, we find that

 | x = ( A ε 1 A ε 2 ⋯ A ε n) ⋅ x n, x=(A_{\varepsilon_{1}}A_{\varepsilon_{2}}\cdots A_{\varepsilon_{n}})\cdot x_{n}, |  |

where ε n = ε n ​ ( x) = ε ⁡ ( F n − 1 ​ ( x)) \varepsilon_{n}=\varepsilon_{n}(x)=\varepsilon(F^{n-1}(x)) for all n ≥ 1 n\geq 1 (see § 2.3). For 0 ≤ i ≤ j 0\leq i\leq j, define

(3.3) |  | A [i, j] = A [i, j] ( x):= A ε i ​ ( x) A ε i + 1 ​ ( x) ⋯ A ε j ​ ( x) and A [j, i] = A [j, i] ( x):= A ε j ​ ( x) A ε j − 1 ​ ( x) ⋯ A ε i ​ ( x), A_{[i,j]}=A_{[i,j]}(x):=A_{\varepsilon_{i}(x)}A_{\varepsilon_{i+1}(x)}\cdots A_{\varepsilon_{j}(x)}\quad\text{and}\quad A_{[j,i]}=A_{[j,i]}(x):=A_{\varepsilon_{j}(x)}A_{\varepsilon_{j-1}(x)}\cdots A_{\varepsilon_{i}(x)}, |  |

where A ε 0 ​ ( x):= I 2 A_{\varepsilon_{0}(x)}:=I_{2} is the two-by-two identity matrix. Denote the entries of A [0, n], n ≥ 0, A_{[0,n]},\ n\geq 0, by

 | ( u n t n s n r n) = ( u n ​ ( x) t n ​ ( x) s n ​ ( x) r n ​ ( x)):= A [0, n]. \begin{pmatrix}u_{n}&t_{n}\\ s_{n}&r_{n}\end{pmatrix}=\begin{pmatrix}u_{n}(x)&t_{n}(x)\\ s_{n}(x)&r_{n}(x)\end{pmatrix}:=A_{[0,n]}. |  |

Observe that for any k ∈ ℤ k\in\mathbb{Z},

(3.4) |  | A 0 k ​ A 1 = ( 1 0 1 1) k ​ ( 0 1 1 1) = ( 1 0 k 1) ​ ( 0 1 1 1) = ( 0 1 1 k + 1). A_{0}^{k}A_{1}=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}^{k}\begin{pmatrix}0&1\\ 1&1\end{pmatrix}=\begin{pmatrix}1&0\\ k&1\end{pmatrix}\begin{pmatrix}0&1\\ 1&1\end{pmatrix}=\begin{pmatrix}0&1\\ 1&k+1\end{pmatrix}. |  |

In view of ( 2.6), for n ≥ 0 n\geq 0 we set

(3.5) |  | j n = j n ​ ( x):= #⁡ { 1 ≤ k ≤ n | ε k = 1 } and λ n = λ n ​ ( x):= n − ∑ k = 1 j n a k. j_{n}=j_{n}(x):=\#\{1\leq k\leq n\ |\ \varepsilon_{k}=1\}\quad\text{and}\quad\lambda_{n}=\lambda_{n}(x):=n-\sum_{k=1}^{j_{n}}a_{k}. |  |

That is, j n j_{n} and λ n \lambda_{n} are the unique integers satisfying

(3.6) |  | n = a 1 + a 2 + ⋯ + a j n + λ n, j n ≥ 0, 0 ≤ λ n < a j n + 1. n=a_{1}+a_{2}+\dots+a_{j_{n}}+\lambda_{n},\qquad j_{n}\geq 0,\quad 0\leq\lambda_{n}<a_{j_{n}+1}. |  |

From ( 2.6) and ( 3.4), it follows for n > 0 n>0 that

 | ( u n t n s n r n) = A [0, n] \displaystyle\begin{pmatrix}u_{n}&t_{n}\\ s_{n}&r_{n}\end{pmatrix}=A_{[0,n]} | = I 2 A ε 1 ⋯ A ε n \displaystyle=I_{2}A_{\varepsilon_{1}}\cdots A_{\varepsilon_{n}} |  |

 |  | = A 0 a 1 − 1 A 1 ⋯ A 0 a j n − 1 A 1 A 0 λ n \displaystyle=A_{0}^{a_{1}-1}A_{1}\cdots A_{0}^{a_{j_{n}}-1}A_{1}A_{0}^{\lambda_{n}} |  |

 |  | = ( 0 1 1 a 1) ⋯ ( 0 1 1 a j n) ( 1 0 λ n 1) \displaystyle=\begin{pmatrix}0&1\\ 1&a_{1}\end{pmatrix}\cdots\begin{pmatrix}0&1\\ 1&a_{j_{n}}\end{pmatrix}\begin{pmatrix}1&0\\ {\lambda_{n}}&1\end{pmatrix} |  |

 |  | = ( p j n − 1 p j n q j n − 1 q j n) ​ ( 1 0 λ n 1) \displaystyle=\begin{pmatrix}p_{{j_{n}}-1}&p_{j_{n}}\\ q_{{j_{n}}-1}&q_{j_{n}}\end{pmatrix}\begin{pmatrix}1&0\\ {\lambda_{n}}&1\end{pmatrix} |  |

(3.7) |  |  | = ( λ n ​ p j n + p j n − 1 p j n λ n ​ q j n + q j n − 1 q j n) \displaystyle=\begin{pmatrix}{\lambda_{n}}p_{j_{n}}+p_{{j_{n}}-1}&p_{j_{n}}\\ {\lambda_{n}}q_{j_{n}}+q_{{j_{n}}-1}&q_{j_{n}}\end{pmatrix} |  |

(see also Lemma 1.1 of [27]). Note that equality of the first and final expressions also holds for n = j n = λ n = 0 n={j_{n}}={\lambda_{n}}=0, for in this case both matrices are the identity I 2 I_{2}. We also have for n > 0 n>0 that

 | A [n, 0] \displaystyle A_{[n,0]} | = A ε n ⋯ A ε 1 I 2 \displaystyle=A_{\varepsilon_{n}}\cdots A_{\varepsilon_{1}}I_{2} |  |

 |  | = A 0 λ n A 1 A 0 a j n − 1 ⋯ A 1 A 0 a 1 − 1 A 1 A 1 − 1 \displaystyle=A_{0}^{\lambda_{n}}A_{1}A_{0}^{a_{j_{n}}-1}\cdots A_{1}A_{0}^{a_{1}-1}A_{1}A_{1}^{-1} |  |

 |  | = ( 0 1 1 λ n + 1) ( 0 1 1 a j n) ⋯ ( 0 1 1 a 1) ( − 1 1 1 0) \displaystyle=\begin{pmatrix}0&1\\ 1&{\lambda_{n}}+1\end{pmatrix}\begin{pmatrix}0&1\\ 1&a_{j_{n}}\end{pmatrix}\cdots\begin{pmatrix}0&1\\ 1&a_{1}\end{pmatrix}\begin{pmatrix}-1&1\\ 1&0\end{pmatrix} |  |

 |  | = ( 0 1 1 λ n + 1) ( ( 0 1 1 a 1) ⋯ ( 0 1 1 a j n)) T ( − 1 1 1 0) \displaystyle=\begin{pmatrix}0&1\\ 1&{\lambda_{n}}+1\end{pmatrix}\left(\begin{pmatrix}0&1\\ 1&a_{1}\end{pmatrix}\cdots\begin{pmatrix}0&1\\ 1&a_{j_{n}}\end{pmatrix}\right)^{T}\begin{pmatrix}-1&1\\ 1&0\end{pmatrix} |  |

 |  | = ( 0 1 1 λ n + 1) ​ ( p j n − 1 q j n − 1 p j n q j n) ​ ( − 1 1 1 0) \displaystyle=\begin{pmatrix}0&1\\ 1&{\lambda_{n}}+1\end{pmatrix}\begin{pmatrix}p_{j_{n}-1}&q_{j_{n}-1}\\ p_{j_{n}}&q_{j_{n}}\end{pmatrix}\begin{pmatrix}-1&1\\ 1&0\end{pmatrix} |  |

 |  | = ( q j n − p j n p j n ( λ n + 1) ​ q j n + q j n − 1 − ( ( λ n + 1) ​ p j n + p j n − 1) ( λ n + 1) ​ p j n + p j n − 1) \displaystyle=\begin{pmatrix}q_{j_{n}}-p_{j_{n}}&p_{j_{n}}\\ ({\lambda_{n}}+1)q_{j_{n}}+q_{j_{n}-1}-(({\lambda_{n}}+1)p_{j_{n}}+p_{j_{n}-1})&({\lambda_{n}}+1)p_{j_{n}}+p_{j_{n}-1}\end{pmatrix} |  |

(3.8) |  |  | = ( r n − t n t n s n + r n − ( u n + t n) u n + t n) \displaystyle=\begin{pmatrix}r_{n}-t_{n}&t_{n}\\ s_{n}+r_{n}-(u_{n}+t_{n})&u_{n}+t_{n}\end{pmatrix} |  |

(cf. ( 3.2)), and the first and final expressions are again also equal to I 2 I_{2} for n = 0 n=0. From ( 3.2) it is clear that the set { u n / s n } n ≥ 0 \{u_{n}/s_{n}\}_{n\geq 0} equals the set

 | { λ ​ p j + p j − 1 λ ​ q j + q j − 1 | j ≥ 0, 0 ≤ λ < a j + 1 } \left\{\frac{\lambda p_{j}+p_{j-1}}{\lambda q_{j}+q_{j-1}}\ \Big|\ j\geq 0,\ 0\leq\lambda<a_{j+1}\right\} |  |

of all convergents and mediants of the rcf -expansion [0; a 1, a 2, …] [0;a_{1},a_{2},\dots] of x x. In fact, the sequence ( u n / s n) n ≥ 0 (u_{n}/s_{n})_{n\geq 0} is precisely the sequence of Farey convergents of x x:

###### Proposition 3.1.

For each n ≥ 0 n\geq 0,

 | ( u n s n) = ( P n − 1 Q n − 1), \begin{pmatrix}u_{n}\\ s_{n}\end{pmatrix}=\begin{pmatrix}P_{n-1}\\ Q_{n-1}\end{pmatrix}, |  |

where P n / Q n = [b 0 − 1; e 1 / b 1, …, e n / b n] P_{n}/Q_{n}=[b_{0}-1;e_{1}/b_{1},\dots,e_{n}/b_{n}] is the n th n^{\text{th}} Farey convergent of x x.

###### Proof.

The proof is by induction. For n = 0 n=0, we have

 | ( u 0 s 0) = ( 1 0) = ( P − 1 Q − 1), \begin{pmatrix}u_{0}\\ s_{0}\end{pmatrix}=\begin{pmatrix}1\\ 0\end{pmatrix}=\begin{pmatrix}P_{-1}\\ Q_{-1}\end{pmatrix}, |  |

and for n = 1 n=1,

 | ( u 1 s 1) = ( 1 − ε 1 1) = ( ( 2 − ε 1) − 1 1) = ( b 0 − 1 1) = ( P 0 Q 0). \begin{pmatrix}u_{1}\\ s_{1}\end{pmatrix}=\begin{pmatrix}1-\varepsilon_{1}\\ 1\end{pmatrix}=\begin{pmatrix}(2-\varepsilon_{1})-1\\ 1\end{pmatrix}=\begin{pmatrix}b_{0}-1\\ 1\end{pmatrix}=\begin{pmatrix}P_{0}\\ Q_{0}\end{pmatrix}. |  |

Now suppose for some n ≥ 1 n\geq 1 it holds for each k ≤ n k\leq n that

 | ( u k s k) = ( P k − 1 Q k − 1). \begin{pmatrix}u_{k}\\ s_{k}\end{pmatrix}=\begin{pmatrix}P_{k-1}\\ Q_{k-1}\end{pmatrix}. |  |

Now

(3.9) |  | ( u n t n s n r n) = ( u n − 1 t n − 1 s n − 1 r n − 1) ​ ( 1 − ε n ε n 1 1) = ( ( 1 − ε n) ​ u n − 1 + t n − 1 ε n ​ u n − 1 + t n − 1 ( 1 − ε n) ​ s n − 1 + r n − 1 ε n ​ s n − 1 + r n − 1). \displaystyle\begin{pmatrix}u_{n}&t_{n}\\ s_{n}&r_{n}\end{pmatrix}=\begin{pmatrix}u_{n-1}&t_{n-1}\\ s_{n-1}&r_{n-1}\end{pmatrix}\begin{pmatrix}1-\varepsilon_{n}&\varepsilon_{n}\\ 1&1\end{pmatrix}=\begin{pmatrix}(1-\varepsilon_{n})u_{n-1}+t_{n-1}&\varepsilon_{n}u_{n-1}+t_{n-1}\\ (1-\varepsilon_{n})s_{n-1}+r_{n-1}&\varepsilon_{n}s_{n-1}+r_{n-1}\end{pmatrix}. |  |

The top-left entries give

 | t n − 1 = u n + ( ε n − 1) ​ u n − 1. t_{n-1}=u_{n}+(\varepsilon_{n}-1)u_{n-1}. |  |

Then the top-right entries—replacing t n − 1 t_{n-1} with the right-hand side of the previous line—give

 | t n = u n + ( 2 ​ ε n − 1) ​ u n − 1. t_{n}=u_{n}+(2\varepsilon_{n}-1)u_{n-1}. |  |

Since ( 3.9) holds for all n ≥ 1 n\geq 1, the top-left entries (replacing n n with n + 1 n+1) together with the previous line, ( 3.1) and ( 2.1) gives

 | u n + 1 = ( 1 − ε n + 1) ​ u n + t n = ( 2 − ε n + 1) ​ u n + ( 2 ​ ε n − 1) ​ u n − 1 = b n ​ P n − 1 + e n ​ P n − 2 = P n. u_{n+1}=(1-\varepsilon_{n+1})u_{n}+t_{n}=(2-\varepsilon_{n+1})u_{n}+(2\varepsilon_{n}-1)u_{n-1}=b_{n}P_{n-1}+e_{n}P_{n-2}=P_{n}. |  |

With similar computations one finds s n + 1 = Q n s_{n+1}=Q_{n}. ∎

As a sequence, ( 3.2) gives

 | ( ( u n t n s n r n)) n ≥ 0 = ( CLOSE \displaystyle\left(\begin{pmatrix}u_{n}&t_{n}\\ s_{n}&r_{n}\end{pmatrix}\right)_{n\geq 0}=\bigg( | ( p − 1 p 0 q − 1 q 0) \displaystyle\begin{pmatrix}p_{-1}&p_{0}\\ q_{-1}&q_{0}\end{pmatrix} |  | , ( p 0 + p − 1 p 0 q 0 + q − 1 q 0) \displaystyle,\begin{pmatrix}p_{0}+p_{-1}&p_{0}\\ q_{0}+q_{-1}&q_{0}\end{pmatrix} |  | , …, ( ( a 1 − 1) ​ p 0 + p − 1 p 0 ( a 1 − 1) ​ q 0 + q − 1 q 0), \displaystyle,\dots,\begin{pmatrix}(a_{1}-1)p_{0}+p_{-1}&p_{0}\\ (a_{1}-1)q_{0}+q_{-1}&q_{0}\end{pmatrix}, |  |

 |  | ( p 0 p 1 q 0 q 1) \displaystyle\begin{pmatrix}p_{0}&p_{1}\\ q_{0}&q_{1}\end{pmatrix} |  | , ( p 1 + p 0 p 1 q 1 + q 0 q 1) \displaystyle,\begin{pmatrix}p_{1}+p_{0}&p_{1}\\ q_{1}+q_{0}&q_{1}\end{pmatrix} |  | , …, ( ( a 2 − 1) ​ p 1 + p 0 p 1 ( a 2 − 1) ​ q 1 + q 0 q 1), …, \displaystyle,\dots,\begin{pmatrix}(a_{2}-1)p_{1}+p_{0}&p_{1}\\ (a_{2}-1)q_{1}+q_{0}&q_{1}\end{pmatrix},\dots, |  |

 |  | ( p j − 1 p j q j − 1 q j) \displaystyle\begin{pmatrix}p_{j-1}&p_{j}\\ q_{j-1}&q_{j}\end{pmatrix} |  | , ( p j + p j − 1 p j q j + q j − 1 q j) \displaystyle,\begin{pmatrix}p_{j}+p_{j-1}&p_{j}\\ q_{j}+q_{j-1}&q_{j}\end{pmatrix} |  | , …, ( ( a j + 1 − 1) ​ p j + p j − 1 p j ( a j + 1 − 1) ​ q j + q j − 1 q j), …), \displaystyle,\dots,\begin{pmatrix}(a_{j+1}-1)p_{j}+p_{j-1}&p_{j}\\ (a_{j+1}-1)q_{j}+q_{j-1}&q_{j}\end{pmatrix},\dots\bigg), |  |

and thus by Proposition 3.1, the Farey convergents occur in the following order:

(3.10) |  | ( P n − 1 Q n − 1) n ≥ 0 = ( u n s n) n ≥ 0 = ( CLOSE \displaystyle\left(\frac{P_{n-1}}{Q_{n-1}}\right)_{n\geq 0}=\left(\frac{u_{n}}{s_{n}}\right)_{n\geq 0}=\bigg( | p − 1 q − 1 \displaystyle\frac{p_{-1}}{q_{-1}} |  | , p 0 + p − 1 q 0 + q − 1 \displaystyle,\frac{p_{0}+p_{-1}}{q_{0}+q_{-1}} |  | , …, ( a 1 − 1) ​ p 0 + p − 1 ( a 1 − 1) ​ q 0 + q − 1, \displaystyle,\dots,\frac{(a_{1}-1)p_{0}+p_{-1}}{(a_{1}-1)q_{0}+q_{-1}}, |  |

 |  | p 0 q 0 \displaystyle\frac{p_{0}}{q_{0}} |  | , p 1 + p 0 q 1 + q 0 \displaystyle,\frac{p_{1}+p_{0}}{q_{1}+q_{0}} |  | , …, ( a 2 − 1) ​ p 1 + p 0 ( a 2 − 1) ​ q 1 + q 0, …, \displaystyle,\dots,\frac{(a_{2}-1)p_{1}+p_{0}}{(a_{2}-1)q_{1}+q_{0}},\dots, |  |

 |  | p j − 1 q j − 1 \displaystyle\frac{p_{j-1}}{q_{j-1}} |  | , p j + p j − 1 q j + q j − 1 \displaystyle,\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}} |  | , …, ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1, …). \displaystyle,\dots,\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}},\dots\bigg). |  |

Notice that the denominators ( s n) n ≥ 0 (s_{n})_{n\geq 0} do not form an increasing sequence. Supposedly to ‘remedy’ this, in [27] Ito instead considers the collection { ( u n + t n) / ( s n + r n) } n ≥ 0 \{(u_{n}+t_{n})/(s_{n}+r_{n})\}_{n\geq 0}. As a sequence, this gives

 | ( u n + t n s n + r n) n ≥ 0 = ( CLOSE \displaystyle\left(\frac{u_{n}+t_{n}}{s_{n}+r_{n}}\right)_{n\geq 0}=\bigg( | p 0 + p − 1 q 0 + q − 1 \displaystyle\frac{p_{0}+p_{-1}}{q_{0}+q_{-1}} |  | , 2 ​ p 0 + p − 1 2 ​ q 0 + q − 1 \displaystyle,\frac{2p_{0}+p_{-1}}{2q_{0}+q_{-1}} |  | , …, ( a 1 − 1) ​ p 0 + p − 1 ( a 1 − 1) ​ q 0 + q − 1 \displaystyle,\dots,\frac{(a_{1}-1)p_{0}+p_{-1}}{(a_{1}-1)q_{0}+q_{-1}} |  | , p 1 q 1, \displaystyle,\frac{p_{1}}{q_{1}}, |  |

 |  | p 1 + p 0 q 1 + q 0 \displaystyle\frac{p_{1}+p_{0}}{q_{1}+q_{0}} |  | , 2 ​ p 1 + p 0 2 ​ q 1 + q 0 \displaystyle,\frac{2p_{1}+p_{0}}{2q_{1}+q_{0}} |  | , …, ( a 2 − 1) ​ p 1 + p 0 ( a 2 − 1) ​ q 1 + q 0 \displaystyle,\dots,\frac{(a_{2}-1)p_{1}+p_{0}}{(a_{2}-1)q_{1}+q_{0}} |  | , p 2 q 2, …, \displaystyle,\frac{p_{2}}{q_{2}},\dots, |  |

 |  | p j + p j − 1 q j + q j − 1 \displaystyle\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}} |  | , 2 ​ p j + p j − 1 2 ​ q j + q j − 1 \displaystyle,\frac{2p_{j}+p_{j-1}}{2q_{j}+q_{j-1}} |  | , …, ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1 \displaystyle,\dots,\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}} |  | , p j + 1 q j + 1, …). \displaystyle,\frac{p_{j+1}}{q_{j+1}},\dots\bigg). |  |

However, in light of Proposition 3.1 and results in the sequel, we find it more natural to study the Farey convergents u n / s n u_{n}/s_{n}.

## 4. Ito’s natural extension of the Farey tent map

In [27], Ito determined a planar natural extension ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}) of the dynamical system ( [0, 1], ℬ, μ, F) ([0,1],\mathcal{B},\mu,F) associated to the Farey tent map. The map ℱ: Ω → Ω \mathcal{F}:\Omega\to\Omega is given by

(4.1) |  | ℱ ⁡ ( x, y):= { ( x 1 − x, y 1 + y), x ≤ 1 / 2, ( 1 − x x, 1 1 + y), x > 1 / 2, \mathcal{F}(x,y):=\begin{cases}\left(\frac{x}{1-x},\frac{y}{1+y}\right),&x\leq 1/2,\\ \left(\frac{1-x}{x},\frac{1}{1+y}\right),&x>1/2,\end{cases} |  |

where again Ω = [0, 1] 2 \Omega=[0,1]^{2}, and μ ¯ \bar{\mu} is the absolutely continuous measure on Ω \Omega with density 1 / ( x + y − x ​ y) 2 1/(x+y-xy)^{2}. The measure μ ¯ \bar{\mu} is infinite, σ \sigma -finite and ℱ \mathcal{F} -invariant, and the natural extension ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}) is ergodic (Theorem 1.3 of [27]). Using the matrix notation from ( 3.2), ℱ \mathcal{F} may be written as

 | ℱ ⁡ ( x, y) = ( A ε ⁡ ( x) − 1 ⋅ x, A ε ⁡ ( x) ⋅ y), \mathcal{F}(x,y)=\left(A_{\varepsilon(x)}^{-1}\cdot x,A_{\varepsilon(x)}\cdot y\right), |  |

and thus the n th n^{\text{th}} iterate is

 | ℱ n ​ ( x, y) = ( A [0, n] − 1 ⋅ x, A [n, 0] ⋅ y) \mathcal{F}^{n}(x,y)=\left(A_{[0,n]}^{-1}\cdot x,A_{[n,0]}\cdot y\right) |  |

(recall ( 3.3)). The map ℱ \mathcal{F} admits a particularly nice geometric interpretation, which we now describe. For each integer k ≥ 1 k\geq 1, let

 | V k:= ( 1 k + 1, 1 k] × [0, 1] and H k:= [0, 1] × ( 1 k + 1, 1 k] V_{k}:=\left(\frac{1}{k+1},\frac{1}{k}\right]\times[0,1]\quad\text{and}\quad H_{k}:=[0,1]\times\left(\frac{1}{k+1},\frac{1}{k}\right] |  |

denote the k th k^{\textit{th}} vertical and horizontal regions, respectively. Now fix ( x, y) ∈ Ω (x,y)\in\Omega with rcf -expansions

 | ( x, y) = ( [0; a 1, a 2, …], [0; b 1, b 2, …]) ∈ V a 1 ∩ H b 1. (x,y)=([0;a_{1},a_{2},\dots],[0;b_{1},b_{2},\dots])\in V_{a_{1}}\cap H_{b_{1}}. |  |

One verifies using ( 2.5) and ( 4.1) that for x ≠ 1 x\neq 1,

(4.2) |  | ℱ ⁡ ( x, y) = { ( [0; a 1 − 1, a 2, …], [0; b 1 + 1, b 2, …]), a 1 > 1, ( [0; a 2, a 3 ​ …], [0; 1, b 1, b 2, …]), a 1 = 1. \mathcal{F}(x,y)=\begin{cases}([0;a_{1}-1,a_{2},\dots],[0;b_{1}+1,b_{2},\dots]),&a_{1}>1,\\ ([0;a_{2},a_{3}\dots],[0;1,b_{1},b_{2},\dots]),&a_{1}=1.\end{cases} |  |

Thus the image of the rectangle V a ∩ H b, a > 1, V_{a}\cap H_{b},\ a>1, is the rectangle ℱ ⁡ ( V a ∩ H b) = V a − 1 ∩ H b + 1 \mathcal{F}(V_{a}\cap H_{b})=V_{a-1}\cap H_{b+1} immediately below and to the right of the original rectangle, and the image of the right-half V 1 V_{1} of Ω \Omega is the top half ℱ ⁡ ( V 1) = H 1 \mathcal{F}(V_{1})=H_{1}, modulo a Lebesgue-null set. In particular, subsequent iterates ℱ λ, 0 ≤ λ < a \mathcal{F}^{\lambda},\ 0\leq\lambda<a, ‘slide’ the rectangle V a ∩ H 1 V_{a}\cap H_{1} ‘diagonally’ along a a rectangles, and the next iterate ℱ a ​ ( V a ∩ H 1) \mathcal{F}^{a}(V_{a}\cap H_{1}) is mapped back as a subset of H 1 H_{1} (see Figure 2).

Figure 2. From left to right: The sets V 3 ∩ H 1, ℱ ⁡ ( V 3 ∩ H 1), ℱ 2 ​ ( V 3 ∩ H 1) V_{3}\cap H_{1},\ \mathcal{F}(V_{3}\cap H_{1}),\ \mathcal{F}^{2}(V_{3}\cap H_{1}) and ℱ 3 ​ ( V 3 ∩ H 1) \mathcal{F}^{3}(V_{3}\cap H_{1}), respectively.

For x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q} and n ≥ 0 n\geq 0 set

(4.3) |  | ( x n, y n):= ℱ n ​ ( x, 1) = ( A [0, n] − 1 ⋅ x, A [n, 0] ⋅ 1). (x_{n},y_{n}):=\mathcal{F}^{n}(x,1)=\left(A_{[0,n]}^{-1}\cdot x,A_{[n,0]}\cdot 1\right). |  |

The above geometric interpretation of ℱ \mathcal{F} provides a natural identification between the orbit ( x n, y n) n ≥ 0 (x_{n},y_{n})_{n\geq 0} in Ω \Omega and the sequence ( P n − 1 / Q n − 1) n ≥ 0 = ( u n / s n) n ≥ 0 (P_{n-1}/Q_{n-1})_{n\geq 0}=(u_{n}/s_{n})_{n\geq 0} of Farey convergents of x x from ( 3.10). In particular, the first a 1 a_{1} points

 | ( x 0, y 0), ( x 1, y 1), …, ( x a 1 − 1, y a 1 − 1) (x_{0},y_{0}),(x_{1},y_{1}),\dots,(x_{a_{1}-1},y_{a_{1}-1}) |  |

in the orbit belong to the rectangles

 | V a 1 ∩ H 1, V a 1 − 1 ∩ H 2, …, V 1 ∩ H a 1 V_{a_{1}}\cap H_{1},V_{a_{1}-1}\cap H_{2},\dots,V_{1}\cap H_{a_{1}} |  |

and correspond to the Farey convergents

 | p − 1 q − 1, p 0 + p − 1 q 0 + q − 1, …, ( a 1 − 1) ​ p 0 + p − 1 ( a 1 − 1) ​ q 0 + q − 1, \frac{p_{-1}}{q_{-1}},\frac{p_{0}+p_{-1}}{q_{0}+q_{-1}},\dots,\frac{(a_{1}-1)p_{0}+p_{-1}}{(a_{1}-1)q_{0}+q_{-1}}, |  |

respectively. Note that ( x a 1, y a 1) = ( [0; a 2, a 3, …], [0; 1, a 1]) (x_{a_{1}},y_{a_{1}})=([0;a_{2},a_{3},\dots],[0;1,a_{1}]), so the next a 2 a_{2} points

 | ( x a 1, y a 1), ( x a 1 + 1, y a 1 + 1), …, ( x a 1 + a 2 − 1, y a 1 + a 2 − 1) (x_{a_{1}},y_{a_{1}}),(x_{a_{1}+1},y_{a_{1}+1}),\dots,(x_{a_{1}+a_{2}-1},y_{a_{1}+a_{2}-1}) |  |

of the orbit belong to (the closures 6 6 6 The closure is needed if and only if a 1 = 1 a_{1}=1, since then y a 1 + λ = [0; λ + 1, a 1] = 1 / ( λ + 2) ∉ H λ + 1 y_{a_{1}+\lambda}=[0;\lambda+1,a_{1}]=1/(\lambda+2)\notin H_{\lambda+1} for 0 ≤ λ < a 2 0\leq\lambda<a_{2}. As shown below, this annoyance is ‘corrected’ for n ≥ a 1 + a 2 n\geq a_{1}+a_{2}, and the closures are no longer needed. Throughout the paper, we shall overlook this innocuous subtlety and make no mention of the special case a 1 = 1 a_{1}=1. Some claims, like those in Example 4.4 below, should thus be understood up to this minor technicality, but this shall not affect the statements of any results. of) the rectangles

 | V a 2 ∩ H 1, V a 2 − 1 ∩ H 2, …, V 1 ∩ H a 2 V_{a_{2}}\cap H_{1},V_{a_{2}-1}\cap H_{2},\dots,V_{1}\cap H_{a_{2}} |  |

and correspond to the Farey convergents

 | p 0 q 0, p 1 + p 0 q 1 + q 0, …, ( a 2 − 1) ​ p 1 + p 0 ( a 2 − 1) ​ q 1 + q 0, \frac{p_{0}}{q_{0}},\frac{p_{1}+p_{0}}{q_{1}+q_{0}},\dots,\frac{(a_{2}-1)p_{1}+p_{0}}{(a_{2}-1)q_{1}+q_{0}}, |  |

respectively. More generally, observe that ( x n, y n) ∈ H 1 (x_{n},y_{n})\in H_{1} if and only if

 | ( x n, y n) = ( [0; a j + 1, a j + 2, …], [0; 1, a j, …, a 1]) (x_{n},y_{n})=([0;a_{j+1},a_{j+2},\dots],[0;1,a_{j},\dots,a_{1}]) |  |

for some j j with j > 1 j>1, or j = 1 j=1 and a 1 > 1 a_{1}>1. In that case, n = a 1 + a 2 + ⋯ + a j n=a_{1}+a_{2}+\dots+a_{j} (i.e., j = j n ​ ( x) j=j_{n}(x); see Equation ( 3.5)), and the points

 | ( x n, y n), ( x n + 1, y n + 1), …, ( x n + a j + 1 − 1, y n + a j + 1 − 1) (x_{n},y_{n}),(x_{n+1},y_{n+1}),\dots,(x_{n+a_{j+1}-1},y_{n+a_{j+1}-1}) |  |

belong to the rectangles

 | V a j + 1 ∩ H 1, V a j + 1 − 1 ∩ H 2, …, V 1 ∩ H a j + 1 V_{a_{j+1}}\cap H_{1},V_{a_{j+1}-1}\cap H_{2},\dots,V_{1}\cap H_{a_{j+1}} |  |

and correspond to the Farey convergents

 | p j − 1 q j − 1, p j + p j − 1 q j + q j − 1, …, ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1, \frac{p_{j-1}}{q_{j-1}},\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}},\dots,\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}}, |  |

respectively.

### 4.1. Inducing Ito’s natural extension

With the above identification of orbits and Farey convergents, we find that certain subregions R ⊂ Ω R\subset\Omega correspond to particular convergents or mediants of the rcf -expansion of x x; for instance, H λ + 1 H_{\lambda+1} corresponds to convergents ( λ = 0 \lambda=0) or mediants ( λ > 0 \lambda>0) of the form ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1), λ < a j + 1 (\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1}),\ \lambda<a_{j+1}. In particular, H 1 H_{1} corresponds to rcf -convergents ( p j / q j) j ≥ − 1 (p_{j}/q_{j})_{j\geq-1}, which are generated by the Gauss map G G. Moreover, the first return of ℱ \mathcal{F} to H 1 H_{1} is reminiscent of the natural extension ( Ω, ℬ, ν ¯ G, 𝒢) (\Omega,\mathcal{B},\bar{\nu}_{G},\mathcal{G}) of the Gauss map (cf. ( 2.4)): if ( x, y) = ( [0; a 1, a 2, …], [0; b 1, b 2, …]) ∈ H 1 (x,y)=([0;a_{1},a_{2},\dots],[0;b_{1},b_{2},\dots])\in H_{1}, i.e., b 1 = 1 b_{1}=1, then

 | ℱ a 1 ​ ( [0; a 1, a 2, …], [0; 1, b 2, b 3, …]) = \displaystyle\mathcal{F}^{a_{1}}([0;a_{1},a_{2},\dots],[0;1,b_{2},b_{3},\dots])= | ℱ a 1 − 1 ​ ( [0; a 1 − 1, a 2, …], [0; 2, b 2, b 3, …]) \displaystyle\ \mathcal{F}^{a_{1}-1}([0;a_{1}-1,a_{2},\dots],[0;2,b_{2},b_{3},\dots]) |  |

 | = \displaystyle= | ℱ a 1 − 2 ​ ( [0; a 1 − 2, a 2, …], [0; 3, b 2, b 3, …]) \displaystyle\ \mathcal{F}^{a_{1}-2}([0;a_{1}-2,a_{2},\dots],[0;3,b_{2},b_{3},\dots]) |  |

 |  |  |

 | = \displaystyle= | ℱ ⁡ ( [0; 1, a 2, …], [0; a 1, b 2, b 3, …]) \displaystyle\ \mathcal{F}([0;1,a_{2},\dots],[0;a_{1},b_{2},b_{3},\dots]) |  |

 | = \displaystyle= | ( [0; a 2, a 3 ​ …], [0; 1, a 1, b 2, b 3, …]). \displaystyle\ ([0;a_{2},a_{3}\dots],[0;1,a_{1},b_{2},b_{3},\dots]). |  |

In fact, Brown and Yin proved in [7] that a copy of the Gauss natural extension is found sitting (inverted, scaled and ‘suspended’ from y = 1 y=1) within ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}):

###### Theorem 4.1 (Theorem 1 of [7]).

The Gauss natural extension ( Ω, ℬ, ν ¯ G, 𝒢) (\Omega,\mathcal{B},\bar{\nu}_{G},\mathcal{G}) is isomorphic via the map ( x, y) ↦ ( x, 1 / ( y + 1)) (x,y)\mapsto(x,1/(y+1)) to the dynamical system induced from ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}) on the horizontal region H 1 H_{1}.

These observations naturally lead one to consider ℱ \mathcal{F} induced on other subregions R ⊂ Ω R\subset\Omega which pick out desired subsequences of Farey convergents.

###### Definition 4.2.

A μ ¯ \bar{\mu} -measurable subset R ⊂ Ω R\subset\Omega is called an *inducible subregion*of Ω \Omega if either

1. (i)

R = Ω R=\Omega, or

2. (ii)

0 < μ ¯ ​ ( R) < ∞ 0<\bar{\mu}(R)<\infty and R R is a *μ ¯ \bar{\mu} -continuity set*, i.e., μ ¯ ​ ( ∂ R) = 0 \bar{\mu}(\partial R)=0.

An inducible subregion R R satisfying (ii) is called *proper*.

###### Remark 4.3.

Due to Proposition 5.1 below, our main interest is in ℱ \mathcal{F} -orbits of points of the form ( x, 1) ∈ Ω (x,1)\in\Omega as in ( 4.3). The conditions of a proper inducible subregion R R guarantee that μ ¯ ​ ( int ​ ( R)) > 0 \bar{\mu}(\text{int}(R))>0 and hence for Lebesgue-a.e. x ∈ [0, 1] x\in[0,1], the ℱ \mathcal{F} -orbit of ( x, 1) (x,1) enters R R infinitely often. (In fact, the stronger requirement that μ ¯ ​ ( ∂ R) = 0 \bar{\mu}(\partial R)=0 is also needed for our purposes; see Remark 4.10.) Indeed, let ( x, z) ∈ Ω (x,z)\in\Omega with x = [0; a 1, a 2, …] ∉ ℚ x=[0;a_{1},a_{2},\dots]\notin\mathbb{Q}. For n ≥ a 1 n\geq a_{1}, Equations ( 3.6) and ( 4.2) give that

(4.4) |  | ( x n, z n):= ℱ n ​ ( x, z) = { ( [0; a j n + 1 − λ n, a j n + 2, …], [0; λ n + 1, a j n, …, a 1 − 1 + z − 1]), z ≠ 0, ( [0; a j n + 1 − λ n, a j n + 2, …], [0; λ n + 1, a j n, …, a 2]), z = 0. (x_{n},z_{n}):=\mathcal{F}^{n}(x,z)=\begin{cases}([0;a_{j_{n}+1}-\lambda_{n},a_{j_{n}+2},\dots],[0;\lambda_{n}+1,a_{j_{n}},\dots,a_{1}-1+z^{-1}]),\ &z\neq 0,\\ ([0;a_{j_{n}+1}-\lambda_{n},a_{j_{n}+2},\dots],[0;\lambda_{n}+1,a_{j_{n}},\dots,a_{2}]),\ &z=0.\end{cases} |  |

In particular, z n z_{n} belongs to the cylinder of points in [0, 1] [0,1] whose rcf -expansions begin with [0; λ n + 1, a j n, …, a 2, …] [0;\lambda_{n}+1,a_{j_{n}},\dots,a_{2},\dots]. The Euclidean diameter of this cylinder is no greater than the reciprocal of the j n th j_{n}^{\text{th}} Fibonacci number squared and thus goes to 0 0 uniformly in z z as n n goes to infinity (see also [7]). Now let E E be the set of irrationals x ∈ ( 0, 1) x\in(0,1) for which ( x n, y n):= ℱ n ​ ( x, 1) (x_{n},y_{n}):=\mathcal{F}^{n}(x,1) enters R R at most finitely often. Since μ ¯ ​ ( int ​ ( R)) > 0 \bar{\mu}(\text{int}(R))>0, there exists some point ( s, t) ∈ int ​ ( R) (s,t)\in\text{int}(R) and some δ > 0 \delta>0 such that B δ ​ ( s, t) ⊂ int ​ ( R) B_{\delta}(s,t)\subset\text{int}(R). If E E has positive Lebesgue measure, then also μ ¯ ​ ( E × [0, 1]) > 0 \bar{\mu}(E\times[0,1])>0. Since ℱ \mathcal{F} is conservative ( [7]), μ ¯ \bar{\mu} -a.e. point ( x, z) ∈ E × [0, 1] (x,z)\in E\times[0,1] enters B δ / 2 ​ ( s, t) B_{\delta/2}(s,t) infinitely often. The observation on the diameter of the cylinder above implies that for n n large enough, | ( x n, z n) − ( x n, y n) | < δ / 2 |(x_{n},z_{n})-(x_{n},y_{n})|<\delta/2, and hence ( x n, y n) (x_{n},y_{n}) enters B δ ​ ( s, t) ⊂ int ​ ( R) B_{\delta}(s,t)\subset\text{int}(R) infinitely often—a contradiction.

For an inducible subregion R ⊂ Ω R\subset\Omega, let r = r R: Ω → ℕ ∪ { ∞ } r=r_{R}:\Omega\to\mathbb{N}\cup\{\infty\} denote the hitting time

(4.5) |  | r R ​ ( x, y):= inf { n ≥ 1 | ℱ n ​ ( x, y) ∈ R } r_{R}(x,y):=\inf\{\ n\geq 1\ |\ \mathcal{F}^{n}(x,y)\in R\} |  |

to R R. (Abusing notation, we assume that the null set of points in any set S ⊂ Ω S\subset\Omega which enter R R at most finitely many times under ℱ \mathcal{F} is removed from S S and denote this new set again by S S.) Let ℱ R: Ω → R \mathcal{F}_{R}:\Omega\to R be defined by

(4.6) |  | ℱ R ​ ( x, y):= ℱ r ​ ( x, y) = ( A [0, r] − 1 ⋅ x, A [r, 0] ⋅ y), where r = r R ​ ( x, y). \mathcal{F}_{R}(x,y):=\mathcal{F}^{r}(x,y)=\left(A_{[0,r]}^{-1}\cdot x\ ,\ A_{[r,0]}\cdot y\right),\quad\text{where}\quad r=r_{R}(x,y). |  |

The map ℱ R \mathcal{F}_{R} restricted to R R is the *induced map*of ℱ \mathcal{F} on R R. If R R is a proper inducible subregion, let μ ¯ R \bar{\mu}_{R} denote the *induced measure*

 | μ ¯ R ​ ( S):= μ ¯ ​ ( S) μ ¯ ​ ( R), S ∈ ℬ ∩ R:= { B ∩ R | B ∈ ℬ }. \bar{\mu}_{R}(S):=\frac{\bar{\mu}(S)}{\bar{\mu}(R)},\quad S\in\mathcal{B}\cap R:=\{B\cap R\ |\ B\in\mathcal{B}\}. |  |

Since ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}) is ergodic, so is the induced system ( R, ℬ ∩ R, μ ¯ R, ℱ R) (R,\mathcal{B}\cap R,\bar{\mu}_{R},\mathcal{F}_{R}). In case R = Ω R=\Omega is not proper, we set μ ¯ R:= μ ¯ \bar{\mu}_{R}:=\bar{\mu} and note that ( Ω, ℬ, μ ¯, ℱ) = ( R, ℬ ∩ R, μ ¯ R, ℱ R) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F})=(R,\mathcal{B}\cap R,\bar{\mu}_{R},\mathcal{F}_{R}). In this case, we may abuse terminology and refer to μ ¯ R \bar{\mu}_{R} as an induced measure and ( R, ℬ ∩ R, μ ¯ R, ℱ R) (R,\mathcal{B}\cap R,\bar{\mu}_{R},\mathcal{F}_{R}) as an induced system. However, we emphasise that μ ¯ R \bar{\mu}_{R} is a finite (probability) measure if and only if R R is a *proper*inducible subregion.

For an inducible subregion R ⊂ Ω R\subset\Omega and ( x, y) ∈ Ω (x,y)\in\Omega, set N 0 R ​ ( x, y):= 0 N_{0}^{R}(x,y):=0 and, for n ≥ 1 n\geq 1,

(4.7) |  | N n R ​ ( x, y):= N n − 1 R ​ ( x, y) + r R ​ ( ℱ R n − 1 ​ ( x, y)). N^{R}_{n}(x,y):=N_{n-1}^{R}(x,y)+r_{R}(\mathcal{F}_{R}^{n-1}(x,y)). |  |

In particular, this gives the following relationship between iterates of ℱ R \mathcal{F}_{R} and of ℱ \mathcal{F}, for each n ≥ 0 n\geq 0 and ( x, y) (x,y):

 | ℱ R n ​ ( x, y) = ℱ N ​ ( x, y) = ( A [0, N] − 1 ⋅ x, A [N, 0] ⋅ y), where N = N n R ​ ( x, y). \mathcal{F}_{R}^{n}(x,y)=\mathcal{F}^{N}(x,y)=\left(A_{[0,N]}^{-1}\cdot x\ ,\ A_{[N,0]}\cdot y\right),\quad\text{where}\quad N=N_{n}^{R}(x,y). |  |

When the subregion R R and an irrational x ∈ ( 0, 1) x\in(0,1) are understood, we use the suppressed notation

(4.8) |  | N n:= N n R ​ ( x, 1). N_{n}:=N_{n}^{R}(x,1). |  |

An inducible subregion R R thus naturally determines a subsequence of the Farey convergents of Lebesgue-a.e. irrational 7 7 7 As suggested by Remark 4.3, there may be a Lebesgue-null set of points that enter R R at most finitely many times. For instance, if R = V a R=V_{a} as in Example 4.4 below and if x = [0; a 1, a 2, …] x=[0;a_{1},a_{2},\dots] with a j < a a_{j}<a for all j ≥ 1 j\geq 1, then ℱ n ​ ( x, 1) \mathcal{F}^{n}(x,1) never enters R R. Such null sets are omitted from consideration throughout. x ∈ ( 0, 1) x\in(0,1): for each n ≥ 0 n\geq 0, set ( x n R, y n R):= ℱ R n ​ ( x, 1) (x_{n}^{R},y_{n}^{R}):=\mathcal{F}_{R}^{n}(x,1) and

(4.9) |  | ( u n R t n R s n R r n R) = ( u n R ​ ( x) t n R ​ ( x) s n R ​ ( x) r n R ​ ( x)):= A [0, N n] = ( u N n t N n s N n r N n) = ( λ ​ p j + p j − 1 p j λ ​ q j + q j − 1 q j), \begin{pmatrix}u_{n}^{R}&t_{n}^{R}\\ s_{n}^{R}&r_{n}^{R}\end{pmatrix}=\begin{pmatrix}u_{n}^{R}(x)&t_{n}^{R}(x)\\ s_{n}^{R}(x)&r_{n}^{R}(x)\end{pmatrix}:=A_{[0,N_{n}]}=\begin{pmatrix}u_{N_{n}}&t_{N_{n}}\\ s_{N_{n}}&r_{N_{n}}\end{pmatrix}=\begin{pmatrix}\lambda p_{j}+p_{j-1}&p_{j}\\ \lambda q_{j}+q_{j-1}&q_{j}\end{pmatrix}, |  |

where j = j N n ​ ( x) j=j_{N_{n}}(x) and λ = λ N n ​ ( x) \lambda=\lambda_{N_{n}}(x) (recall ( 3.5) and ( 3.2)). Informally speaking, the subsequence

 | ( u n R / s n R) n ≥ 0 = ( u N n / s N n) n ≥ 0 = ( P N n − 1 / Q N n − 1) n ≥ 0 (u_{n}^{R}/s_{n}^{R})_{n\geq 0}=(u_{N_{n}}/s_{N_{n}})_{n\geq 0}=(P_{N_{n}-1}/Q_{N_{n}-1})_{n\geq 0} |  |

of Farey convergents corresponding to R R consists of those convergents which are ‘picked up’ when the forward orbit of ( x, 1) (x,1) under ℱ \mathcal{F} enters the region R R.

###### Example 4.4.

As noted above, the region R = H 1 R=H_{1} corresponds to the rcf -convergents of x x (see Figure 4.i). In particular,

 | ( u n H 1 / s n H 1) n ≥ 0 = ( p j − 1 / q j − 1) j ≥ 0. (u_{n}^{H_{1}}/s_{n}^{H_{1}})_{n\geq 0}=(p_{j-1}/q_{j-1})_{j\geq 0}. |  |

Moreover, for λ ≥ 1 \lambda\geq 1 the region R = H λ + 1 R=H_{\lambda+1} gives the λ th \lambda^{\text{th}} mediant convergents

 | { u n H λ + 1 / s n H λ + 1 } n ≥ 0 = { ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) | λ < a j + 1 } j ≥ 0 \{u_{n}^{H_{\lambda+1}}/s_{n}^{H_{\lambda+1}}\}_{n\geq 0}=\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\ |\ \lambda<a_{j+1}\}_{j\geq 0} |  |

(Figure 4.ii). Similarly, the vertical regions V a, a = 1, 2, …, V_{a},\ a=1,2,\dots, give—in addition to the rcf -convergents p j − 1 / q j − 1 p_{j-1}/q_{j-1} for which a j + 1 = a a_{j+1}=a —the final mediants, next-to-final mediants, and so on, respectively (Figure 4.iii):

 | { u n V a / s n V a } n ≥ 0 = { ( ( a j + 1 − a) ​ p j + p j − 1) / ( ( a j + 1 − a) ​ q j + q j − 1) | a j + 1 ≥ a } j ≥ 0. \{u_{n}^{V_{a}}/s_{n}^{V_{a}}\}_{n\geq 0}=\{((a_{j+1}-a)p_{j}+p_{j-1})/((a_{j+1}-a)q_{j}+q_{j-1})\ |\ a_{j+1}\geq a\}_{j\geq 0}. |  |

###### Example 4.5.

The rectangles R = V a ∩ H b R=V_{a}\cap H_{b} pick out particular convergents ( b = 1 b=1) or mediant convergents ( b > 1 b>1) corresponding to specific partial quotients in the rcf -expansion of x x. For instance,

 | { u n V 3 ∩ H 1 / s n V 3 ∩ H 1 } n ≥ 0 = { p j − 1 / q j − 1 | a j + 1 = 3 } j ≥ 0 \{u_{n}^{V_{3}\cap H_{1}}/s_{n}^{V_{3}\cap H_{1}}\}_{n\geq 0}=\{p_{j-1}/q_{j-1}\ |\ a_{j+1}=3\}_{j\geq 0} |  |

 | { u n V 2 ∩ H 2 / s n V 2 ∩ H 2 } n ≥ 0 = { ( p j + p j − 1) / ( q j + q j − 1) | a j + 1 = 3 } j ≥ 0, \{u_{n}^{V_{2}\cap H_{2}}/s_{n}^{V_{2}\cap H_{2}}\}_{n\geq 0}=\{(p_{j}+p_{j-1})/(q_{j}+q_{j-1})\ |\ a_{j+1}=3\}_{j\geq 0}, |  |

and

 | { u n V 1 ∩ H 3 / s n V 1 ∩ H 3 } n ≥ 0 = { ( 2 ​ p j + p j − 1) / ( 2 ​ q j + q j − 1) | a j + 1 = 3 } j ≥ 0 \{u_{n}^{V_{1}\cap H_{3}}/s_{n}^{V_{1}\cap H_{3}}\}_{n\geq 0}=\{(2p_{j}+p_{j-1})/(2q_{j}+q_{j-1})\ |\ a_{j+1}=3\}_{j\geq 0} |  |

(see the three left-most plots of Figure 2).

More generally, for R = V a − λ ∩ H λ + 1 R=V_{a-\lambda}\cap H_{\lambda+1} with a > 0 a>0 and 0 ≤ λ < a 0\leq\lambda<a,

 | { u n R / s n R } n ≥ 0 = { ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) | a j + 1 = a } j ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\ |\ a_{j+1}=a\}_{j\geq 0}. |  |

We end this subsection with a calculation of the measure-theoretic entropy h ⁡ ( ℱ R) = h μ ¯ R ​ ( ℱ R) h(\mathcal{F}_{R})=h_{\bar{\mu}_{R}}(\mathcal{F}_{R}) of the induced transformation ℱ R \mathcal{F}_{R} restricted to a proper inducible R ⊂ Ω R\subset\Omega.

###### Theorem 4.6.

Let R ⊂ Ω R\subset\Omega be a proper inducible subregion. Then

 | h ⁡ ( ℱ R) = π 2 6 ​ μ ¯ ​ ( R). h(\mathcal{F}_{R})=\frac{\pi^{2}}{6\bar{\mu}(R)}. |  |

###### Proof.

We first note that for two proper inducible subregions R 1, R 2 ⊂ Ω R_{1},R_{2}\subset\Omega with R 1 ⊂ R 2 R_{1}\subset R_{2}, the dynamical system ( R 1, ℬ ∩ R 1, μ ¯ R 1, ℱ R 1) (R_{1},\mathcal{B}\cap R_{1},\bar{\mu}_{R_{1}},\mathcal{F}_{R_{1}}) is isomorphic to *the induced system of ( R 2, ℬ ∩ R 2, μ ¯ R 2, ℱ R 2) (R_{2},\mathcal{B}\cap R_{2},\bar{\mu}_{R_{2}},\mathcal{F}_{R_{2}}) on R 1 R_{1}*. Hence, by Abramov’s formula,

 | h ⁡ ( ℱ R 1) = h ⁡ ( ℱ R 2) μ ¯ R 2 ​ ( R 1) = μ ¯ ​ ( R 2) μ ¯ ​ ( R 1) ​ h ​ ( ℱ R 2), h(\mathcal{F}_{R_{1}})=\frac{h(\mathcal{F}_{R_{2}})}{\bar{\mu}_{R_{2}}(R_{1})}=\frac{\bar{\mu}(R_{2})}{\bar{\mu}(R_{1})}h(\mathcal{F}_{R_{2}}), |  |

or

(4.10) |  | μ ¯ ​ ( R 1) ​ h ​ ( ℱ R 1) = μ ¯ ​ ( R 2) ​ h ​ ( ℱ R 2). \bar{\mu}(R_{1})h(\mathcal{F}_{R_{1}})=\bar{\mu}(R_{2})h(\mathcal{F}_{R_{2}}). |  |

It is well-known that the entropy of the Gauss map G G (and hence also its natural extension 𝒢 \mathcal{G}) is π 2 / 6 ​ log ⁡ 2 \pi^{2}/6\log 2, and thus h ⁡ ( ℱ H 1) = π 2 6 ​ log ⁡ 2 h(\mathcal{F}_{H_{1}})=\frac{\pi^{2}}{6\log 2} by Theorem 4.1. Using this, ( 4.10) and a calculation of μ ¯ ​ ( H 1) = log ⁡ 2 \bar{\mu}(H_{1})=\log 2, we compute

 | μ ¯ ​ ( R) ​ h ​ ( ℱ R) = μ ¯ ​ ( R ∪ H 1) ​ h ​ ( ℱ R ∪ H 1) = μ ¯ ​ ( H 1) ​ h ​ ( ℱ H 1) = π 2 6. \bar{\mu}(R)h(\mathcal{F}_{R})=\bar{\mu}(R\cup H_{1})h(\mathcal{F}_{R\cup H_{1}})=\bar{\mu}(H_{1})h(\mathcal{F}_{H_{1}})=\frac{\pi^{2}}{6}. |  |

∎

### 4.2. The (relative) equidistribution of ( ℱ \mathcal{F} -) ℱ R \mathcal{F}_{R} -orbits

In [7], Brown and Yin employ the Ratio Ergodic Theorem to derive metrical results on the system ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}):

###### Theorem 4.7 (Theorem 2 of [7]).

For any f, g ∈ L 1 ​ ( μ ¯) f,g\in L^{1}(\bar{\mu}) with ∫ g ​ 𝑑 μ ¯ ≠ 0 \int gd\bar{\mu}\neq 0,

(4.11) |  | lim n → ∞ ∑ k = 0 n − 1 f ⁡ ( x k, z k) ∑ k = 0 n − 1 g ⁡ ( x k, z k) = ∫ f ​ 𝑑 μ ¯ ∫ g ​ 𝑑 μ ¯ μ ¯ -a.s., \lim_{n\to\infty}\frac{\sum_{k=0}^{n-1}f(x_{k},z_{k})}{\sum_{k=0}^{n-1}g(x_{k},z_{k})}=\frac{\int fd\bar{\mu}}{\int gd\bar{\mu}}\quad\text{$\bar{\mu}$-a.s.,} |  |

where ( x k, z k):= ℱ k ​ ( x, z), k ≥ 0 (x_{k},z_{k}):=\mathcal{F}^{k}(x,z),\ k\geq 0.

Under certain Lipschitz conditions on f f and g g, Brown and Yin are able to replace ( x k, z k) (x_{k},z_{k}) on the left-hand side of ( 4.11) with ( x k, y k):= ℱ k ​ ( x, 1) (x_{k},y_{k}):=\mathcal{F}^{k}(x,1) for almost every 8 8 8 All *almost every*statements are w.r.t. Lebesgue measure. x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} (see Theorem 3 of [7]). The following theorem—which does not require Lipschitz conditions but instead replaces f f and g g by indicator functions—may be seen as an analogue of an important result of Jager for the natural extension of the Gauss map, which states that for almost every irrational x ∈ ( 0, 1) x\in(0,1), the 𝒢 \mathcal{G} -orbit of ( x, 0) (x,0) is ν ¯ G \bar{\nu}_{G} -equidistributed over Ω \Omega (see Theorem 3 of [29]). In fact, by Theorem 4.1 above and Corollary 4.9 below, the following statement may be read as a generalisation of Jager’s result:

###### Theorem 4.8.

For almost every x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}, the ℱ \mathcal{F} -orbit of ( x, 1) (x,1) is *μ ¯ \bar{\mu} -relatively equidistributed*9 9 9 This notion of μ ¯ \bar{\mu} -relative equidistribution differs slightly from that studied by Gerl in [22] and [21]. In particular, Gerl required a Radon measure, but μ ¯ \bar{\mu} is not locally finite. over Ω \Omega. That is, for almost all x ∈ ( 0, 1) \ ℚ, x\in(0,1)\backslash\mathbb{Q},

 | lim n → ∞ ∑ k = 0 n − 1 𝟏 S ​ ( x k, y k) ∑ k = 0 n − 1 𝟏 R ​ ( x k, y k) = μ ¯ ​ ( S) μ ¯ ​ ( R) \lim_{n\to\infty}\frac{\sum_{k=0}^{n-1}\mathbf{1}_{S}(x_{k},y_{k})}{\sum_{k=0}^{n-1}\mathbf{1}_{R}(x_{k},y_{k})}=\frac{\bar{\mu}(S)}{\bar{\mu}(R)} |  |

for any proper inducible or μ ¯ \bar{\mu} -null set S ⊂ Ω S\subset\Omega and any proper inducible R ⊂ Ω R\subset\Omega.

###### Proof.

Let 𝒰 \mathcal{U} be a countable base for the subspace topology on Ω ⊂ ℝ 2 \Omega\subset\mathbb{R}^{2}, and let 𝒞 \mathcal{C} denote the countable collection of all finite unions of finite μ ¯ \bar{\mu} -measure elements of 𝒰 \mathcal{U}, along with the empty set. Moreover, for A, B ∈ 𝒞 A,B\in\mathcal{C} with μ ¯ ​ ( B) > 0 \bar{\mu}(B)>0, let E ⁡ ( A, B) ⊂ ( 0, 1) \ ℚ E(A,B)\subset(0,1)\backslash\mathbb{Q} denote the set of irrational x x for which there is *no*z ∈ [0, 1] z\in[0,1] satisfying

(4.12) |  | lim n → ∞ ∑ k = 0 n − 1 𝟏 A ​ ( x k, z k) ∑ k = 0 n − 1 𝟏 B ​ ( x k, z k) = μ ¯ ​ ( A) μ ¯ ​ ( B). \lim_{n\to\infty}\frac{\sum_{k=0}^{n-1}{\mathbf{1}_{A}(x_{k},z_{k})}}{\sum_{k=0}^{n-1}{\mathbf{1}_{B}(x_{k},z_{k})}}=\frac{\bar{\mu}(A)}{\bar{\mu}(B)}. |  |

Theorem 4.7 implies that E ⁡ ( A, B) E(A,B) is a Lebesgue-null set: otherwise E ⁡ ( A, B) × [0, 1] E(A,B)\times[0,1] is a set of positive μ ¯ \bar{\mu} -measure for which ( 4.11) does not hold. Since 𝒞 \mathcal{C} is countable, the union E E of all such E ⁡ ( A, B) E(A,B) is also a Lebesgue-null set. Hence, for every x ∈ ( 0, 1) \ ( E ∪ ℚ) x\in(0,1)\backslash(E\cup\mathbb{Q}) it follows that for all A, B ∈ 𝒞 A,B\in\mathcal{C} with μ ¯ ​ ( B) > 0 \bar{\mu}(B)>0, there is some z ∈ [0, 1] z\in[0,1] for which ( 4.12) holds.

We claim that for any proper inducible or μ ¯ \bar{\mu} -null set S ⊂ Ω S\subset\Omega and any δ > 0 \delta>0, there exist S + δ, S − δ ∈ 𝒞 S_{+\delta},S_{-\delta}\in\mathcal{C} such that

1. (i)

S − δ ⊂ S ⊂ S + δ, S_{-\delta}\subset S\subset S_{+\delta},

2. (ii)

μ ¯ ​ ( S + δ \ S), μ ¯ ​ ( S \ S − δ) < δ \bar{\mu}(S_{+\delta}\backslash S),\ \bar{\mu}(S\backslash S_{-\delta})<\delta, and

3. (iii)

d ⁡ ( S, Ω \ S + δ) > 0 d(S,\Omega\backslash S_{+\delta})>0, and if μ ¯ ​ ( S) > 0 \bar{\mu}(S)>0, also d ⁡ ( S − δ, Ω \ S) > 0 d(S_{-\delta},\Omega\backslash S)>0,

where for A, B ∈ ℬ A,B\in\mathcal{B},

 | d ( A, B):= inf { | a − b | | a ∈ A, b ∈ B } d(A,B):=\inf\left\{|a-b|\ \big|\ a\in A,\ b\in B\right\} |  |

denotes the Euclidean distance between the sets A A and B B. Indeed, fix S ⊂ Ω S\subset\Omega and δ > 0 \delta>0 as above. By the regularity of μ ¯ \bar{\mu}, there exists an open cover { U i } i ∈ I ⊂ 𝒰 \{U_{i}\}_{i\in I}\subset\mathcal{U} of the closure S ¯ \bar{S} of S S for which μ ¯ ( ∪ i ∈ I U i \ S ¯) < δ \bar{\mu}(\cup_{i\in I}U_{i}\backslash\bar{S})<\delta. Since S ¯ \bar{S} is compact, { U i } i ∈ I \{U_{i}\}_{i\in I} has some finite subcover, the union of whose elements we denote by S + δ S_{+\delta}. Note, then, that S ⊂ S + δ ⊂ ∪ i ∈ I U i S\subset S_{+\delta}\subset\cup_{i\in I}U_{i}, and since the boundary ∂ S \partial S is a μ ¯ \bar{\mu} -null set, μ ¯ ( S + δ \ S) ≤ μ ¯ ( ∪ i ∈ I U i \ S ¯) < δ \bar{\mu}(S_{+\delta}\backslash S)\leq\bar{\mu}(\cup_{i\in I}U_{i}\backslash\bar{S})<\delta. Moreover, since S ¯ \bar{S} and Ω \ S + δ \Omega\backslash S_{+\delta} are compact and disjoint, the distance between them is strictly positive, and thus the distance between S ⊂ S ¯ S\subset\bar{S} and Ω \ S + δ \Omega\backslash S_{+\delta} is strictly positive. Thus S + δ S_{+\delta} satisfies each of the properties of the claim.

If μ ¯ ​ ( S) = 0 \bar{\mu}(S)=0, set S − δ:= ∅ ∈ 𝒞 S_{-\delta}:=\varnothing\in\mathcal{C}, which trivially satisfies the claim. Now suppose μ ¯ ​ ( S) > 0 \bar{\mu}(S)>0. Since μ ¯ ​ ( ∂ S) = 0 \bar{\mu}(\partial S)=0, we have μ ¯ ​ ( int ​ ( S)) > 0 \bar{\mu}(\text{int}(S))>0. Again by regularity of μ ¯ \bar{\mu}, there exists some compact subset K K of int ​ ( S) \text{int}(S) with μ ¯ ​ ( int ​ ( S) \ K) < δ \bar{\mu}(\text{int}(S)\backslash K)<\delta. Since Ω \Omega is normal and Ω \ int ​ ( S) \Omega\backslash\text{int}(S) and K K are closed and disjoint, there exist open, disjoint sets U, V ∈ ℬ U,\ V\in\mathcal{B} containing Ω \ int ​ ( S) \Omega\backslash\text{int}(S) and K K, respectively. Let { V j } j ∈ J \{V_{j}\}_{j\in J} be a collection of open sets from the countable base 𝒰 \mathcal{U} whose union equals V V. This collection of sets forms an open cover of the compact set K K; let S − δ ∈ 𝒞 S_{-\delta}\in\mathcal{C} be the union of elements of a finite subcover. We then have S − δ ⊂ int ​ ( S) ⊂ S S_{-\delta}\subset\text{int}(S)\subset S and, since μ ¯ ​ ( ∂ S) = 0 \bar{\mu}(\partial S)=0, also μ ¯ ​ ( S \ S − δ) ≤ μ ¯ ​ ( int ​ ( S) \ K) < δ \bar{\mu}(S\backslash S_{-\delta})\leq\bar{\mu}(\text{int}(S)\backslash K)<\delta. Furthermore, since S − δ ⊂ Ω \ U S_{-\delta}\subset\Omega\backslash U and Ω \ S ⊂ Ω \ int ​ ( S) \Omega\backslash S\subset\Omega\backslash\text{int}(S), we have d ⁡ ( S − δ, Ω \ S) ≥ d ⁡ ( Ω \ U, Ω \ int ​ ( S)) d(S_{-\delta},\Omega\backslash S)\geq d(\Omega\backslash U,\Omega\backslash\text{int}(S)). But Ω \ U \Omega\backslash U and Ω \ int ​ ( S) \Omega\backslash\text{int}(S) are compact and disjoint, so the distance between them is again strictly positive. Thus S − δ S_{-\delta} also satisfies the desired properties.

For S ⊂ Ω S\subset\Omega and δ > 0 \delta>0 as above, let

 | d S ​ ( δ):= { d ⁡ ( S, Ω \ S + δ), μ ¯ ​ ( S) = 0, min ⁡ { d ⁡ ( S, Ω \ S + δ), d ⁡ ( S − δ, Ω \ S) }, μ ¯ ​ ( S) > 0. d_{S}(\delta):=\begin{cases}d(S,\Omega\backslash S_{+\delta}),\ &\bar{\mu}(S)=0,\\ \min\{d(S,\Omega\backslash S_{+\delta}),d(S_{-\delta},\Omega\backslash S)\},\ &\bar{\mu}(S)>0.\end{cases} |  |

Recall from Remark 4.3 that for any x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}, the distances between ( x n, y n):= ℱ n ​ ( x, 1) (x_{n},y_{n}):=\mathcal{F}^{n}(x,1) and ( x n, z n):= ℱ n ​ ( x, z) (x_{n},z_{n}):=\mathcal{F}^{n}(x,z) approach zero uniformly in z ∈ [0, 1] z\in[0,1]. Thus for any x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} there exists some n S ​ ( δ) ∈ ℕ n_{S}(\delta)\in\mathbb{N} such that for any z ∈ [0, 1] z\in[0,1] and n ≥ n S ​ ( δ) n\geq n_{S}(\delta),

 | | ( x n, y n) − ( x n, z n) | < d S ​ ( δ). |(x_{n},y_{n})-(x_{n},z_{n})|<d_{S}(\delta). |  |

In particular, by definition of d S ​ ( δ) d_{S}(\delta), for any n ≥ n S ​ ( δ) n\geq n_{S}(\delta),

 | ( x n, y n) ∈ S implies ( x n, z n) ∈ S + δ, (x_{n},y_{n})\in S\quad\text{implies}\quad(x_{n},z_{n})\in S_{+\delta}, |  |

and if μ ¯ ​ ( S) > 0 \bar{\mu}(S)>0,

 | ( x n, z n) ∈ S − δ implies ( x n, y n) ∈ S. (x_{n},z_{n})\in S_{-\delta}\quad\text{implies}\quad(x_{n},y_{n})\in S. |  |

Now let x ∈ ( 0, 1) \ ( E ∪ ℚ) x\in(0,1)\backslash(E\cup\mathbb{Q}), S ⊂ Ω S\subset\Omega a proper inducible subregion or μ ¯ \bar{\mu} -null set and R ⊂ Ω R\subset\Omega a proper inducible subregion. For δ > 0 \delta>0, let S ± δ, R ± δ ∈ 𝒞 S_{\pm\delta},R_{\pm\delta}\in\mathcal{C} be the sets constructed above. When δ \delta is sufficiently small, the observations at the beginning of the proof imply that there exist z, z ′ ∈ [0, 1] z,z^{\prime}\in[0,1] such that

 | μ ¯ ​ ( S − δ) μ ¯ ​ ( R + δ) = lim inf n → ∞ ∑ k = 0 n − 1 𝟏 S − δ ​ ( x k, z k) ∑ k = 0 n − 1 𝟏 R + δ ​ ( x k, z k) ≤ \displaystyle\frac{\bar{\mu}(S_{-\delta})}{\bar{\mu}(R_{+\delta})}=\liminf_{n\to\infty}\frac{\sum_{k=0}^{n-1}{\mathbf{1}_{S_{-\delta}}(x_{k},z_{k})}}{\sum_{k=0}^{n-1}{\mathbf{1}_{R_{+\delta}}(x_{k},z_{k})}}\leq | lim inf n → ∞ ∑ k = 0 n − 1 𝟏 S ​ ( x k, y k) ∑ k = 0 n − 1 𝟏 R ​ ( x k, y k) \displaystyle\liminf_{n\to\infty}\frac{\sum_{k=0}^{n-1}{\mathbf{1}_{S}(x_{k},y_{k})}}{\sum_{k=0}^{n-1}{\mathbf{1}_{R}(x_{k},y_{k})}} |  |

 | ≤ \displaystyle\leq | lim sup n → ∞ ∑ k = 0 n − 1 𝟏 S ​ ( x k, y k) ∑ k = 0 n − 1 𝟏 R ​ ( x k, y k) \displaystyle\limsup_{n\to\infty}\frac{\sum_{k=0}^{n-1}{\mathbf{1}_{S}(x_{k},y_{k})}}{\sum_{k=0}^{n-1}{\mathbf{1}_{R}(x_{k},y_{k})}} |  |

 | ≤ \displaystyle\leq | lim sup n → ∞ ∑ k = 0 n − 1 𝟏 S + δ ​ ( x k, z k ′) ∑ k = 0 n − 1 𝟏 R − δ ​ ( x k, z k ′) = μ ¯ ​ ( S + δ) μ ¯ ​ ( R − δ). \displaystyle\limsup_{n\to\infty}\frac{\sum_{k=0}^{n-1}{\mathbf{1}_{S_{+\delta}}(x_{k},z^{\prime}_{k})}}{\sum_{k=0}^{n-1}{\mathbf{1}_{R_{-\delta}}(x_{k},z^{\prime}_{k})}}=\frac{\bar{\mu}(S_{+\delta})}{\bar{\mu}(R_{-\delta})}. |  |

By properties (i) and (ii) above, taking δ → 0 \delta\to 0 gives the result. ∎

As a corollary, we obtain the following:

###### Corollary 4.9.

For almost every x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}, the ℱ R \mathcal{F}_{R} -orbit of ( x, 1) (x,1) is μ ¯ R \bar{\mu}_{R} -equidistributed for any proper inducible R ⊂ Ω R\subset\Omega. That is, for almost every x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q},

 | lim n → ∞ 1 n ​ ∑ k = 0 n − 1 𝟏 S ​ ( x k R, y k R) = μ ¯ R ​ ( S) \lim_{n\to\infty}\frac{1}{n}\sum_{k=0}^{n-1}\mathbf{1}_{S}(x_{k}^{R},y_{k}^{R})=\bar{\mu}_{R}(S) |  |

for any proper inducible R ⊂ Ω R\subset\Omega and any S ∈ ℬ ∩ R S\in\mathcal{B}\cap R with μ ¯ R ​ ( ∂ S) = 0 \bar{\mu}_{R}(\partial S)=0.

###### Proof.

When S ⊂ R S\subset R,

 | lim n → ∞ 1 n ​ ∑ k = 0 n − 1 𝟏 S ​ ( x k R, y k R) = lim n → ∞ ∑ k = 0 n − 1 𝟏 S ​ ( x k R, y k R) ∑ k = 0 n − 1 𝟏 R ​ ( x k R, y k R) = lim n → ∞ ∑ k = 0 N n − 1 𝟏 S ​ ( x k, y k) ∑ k = 0 N n − 1 𝟏 R ​ ( x k, y k), \lim_{n\to\infty}\frac{1}{n}\sum_{k=0}^{n-1}\mathbf{1}_{S}(x_{k}^{R},y_{k}^{R})=\lim_{n\to\infty}\frac{\sum_{k=0}^{n-1}\mathbf{1}_{S}(x_{k}^{R},y_{k}^{R})}{\sum_{k=0}^{n-1}\mathbf{1}_{R}(x_{k}^{R},y_{k}^{R})}=\lim_{n\to\infty}\frac{\sum_{k=0}^{N_{n}-1}\mathbf{1}_{S}(x_{k},y_{k})}{\sum_{k=0}^{N_{n}-1}\mathbf{1}_{R}(x_{k},y_{k})}, |  |

where N n = N n R ​ ( x, 1) N_{n}=N_{n}^{R}(x,1). The result follows from Theorem 4.8 and the fact that μ ¯ R ​ ( S) = μ ¯ ​ ( S) / μ ¯ ​ ( R) \bar{\mu}_{R}(S)=\bar{\mu}(S)/\bar{\mu}(R). ∎

###### Remark 4.10.

The μ ¯ \bar{\mu} -continuity condition on R R, namely that μ ¯ ​ ( ∂ R) = 0 \bar{\mu}(\partial R)=0, is necessary to avoid ‘pathological’ counter-examples to the above result. Indeed, since y n R ∈ ℚ y_{n}^{R}\in\mathbb{Q} for all n n, if R ⊂ [0, 1] × ( [0, 1] \ ℚ) R\subset[0,1]\times([0,1]\backslash\mathbb{Q}), then ( x n R, y n R) (x_{n}^{R},y_{n}^{R}) never enters R R. Using similar ideas, one can easily construct R ∈ ℬ R\in\mathcal{B} with 0 < μ ¯ ​ ( R) < ∞ 0<\bar{\mu}(R)<\infty and μ ¯ ​ ( ∂ R), μ ¯ ​ ( int ​ ( R)) > 0 \bar{\mu}(\partial R),\ \bar{\mu}(\text{int}(R))>0 so that ( x n R, y n R) (x_{n}^{R},y_{n}^{R}) almost surely enters R R infinitely often but the conclusion of Corollary 4.9 is false (cf. Remark 4.3).

## 5. Metrical results

An important reason to study the rcf -expansion is that this algorithm yields rational approximations to irrational numbers of ‘very high quality.’ By this, we mean that the rcf -convergents ( p n / q n) n ≥ 0 (p_{n}/q_{n})_{n\geq 0} of an irrational number x x have the so-called *best approximation property*(recall ( 1.1)). This result was essentially already known to Christiaan Huygens when he constructed his planetarium in 1680 at the request of Jean-Baptiste Colbert (see Chapter IV in [54]). Later in this section (§ 5.2) we will revisit an old result by Legendre and some of its refinements. Legendre’s result states that if p / q p/q is a rational number in its lowest terms with q q positive, and

(5.1) |  | | x − p q | < 1 2 ​ q 2, \left|x-\frac{p}{q}\right|<\frac{1}{2q^{2}}, |  |

one has that there exists an n ∈ ℕ n\in\mathbb{N} such that p = p n p=p_{n} and q = q n q=q_{n}. In other words, in order to approximate an irrational x x ‘well’ by a rational p / q p/q (‘well’ in the sense that ( 5.1) holds) one is bound to find a rcf -convergent of x x. In view of this, for over a century so-called *rcf -approximation coefficients*θ n \theta_{n}, defined by

 | θ n = θ n ​ ( x):= q n 2 ​ | x − p n q n |, for n ∈ ℕ, \theta_{n}=\theta_{n}(x):=q_{n}^{2}\left|x-\frac{p_{n}}{q_{n}}\right|,\qquad\text{for $n\in\mathbb{N}$}, |  |

have been studied. Independently, Doeblin and Lenstra conjectured the distribution for almost all x x of the sequence ( θ n ​ ( x)) n ∈ ℕ (\theta_{n}(x))_{n\in\mathbb{N}}. The proof of this so-called Doeblin–Lenstra conjecture by Bosma, Jager and Wiedijk in [5] (cf. the approach of Knuth in [36]) lead to many new results in Diophantine approximation, some of which are mentioned below. In § 5.1 we consider a number of old and new Doeblin–Lenstra-type theorems for subsequences of approximation coefficients corresponding to rcf -convergents and mediants.

Apart from the Legendre-type results considered in § 5.2, we mention here some classical results which hold for all irrational x x and all n ∈ ℕ n\in\mathbb{N}:

 | min ⁡ { θ n − 1 ​ ( x), θ n ​ ( x) } < 1 2 (Vahlen, 1895 [56]; see also § 5.3.1 below); \min\{\theta_{n-1}(x),\theta_{n}(x)\}<\frac{1}{2}\quad\text{(Vahlen, 1895 \cite[cite]{[\@@bibref{}{V95}{}{}]}; see also \lx@sectionsign\ref{Consecutive rcf-convergents} below)}; |  |

 | min ⁡ { θ n − 1 ​ ( x), θ n ​ ( x), θ n + 1 ​ ( x) } ≤ 1 5 (Borel, 1903 [B03]); \min\{\theta_{n-1}(x),\theta_{n}(x),\theta_{n+1}(x)\}\leq\frac{1}{\sqrt{5}}\quad\text{(Borel, 1903 \cite[cite]{[\@@bibref{}{B03}{}{}]})}; |  |

which in itself is a corollary of the following result

 | min ⁡ { θ n − 1 ​ ( x), θ n ​ ( x), θ n + 1 ​ ( x) } < 1 a n + 1 2 + 4 (Bagemihl & McLaughlin, 1966 [BM66]). \min\{\theta_{n-1}(x),\theta_{n}(x),\theta_{n+1}(x)\}<\frac{1}{\sqrt{a_{n+1}^{2}+4}}\quad\text{(Bagemihl \& McLaughlin, 1966 \cite[cite]{[\@@bibref{}{BM66}{}{}]})}. |  |

Related to this last result is the result by Tong from 1983 ( [55]), which states that:

 | max ⁡ { θ n − 1 ​ ( x), θ n ​ ( x), θ n + 1 ​ ( x) } > 1 a n + 1 2 + 4. \max\{\theta_{n-1}(x),\theta_{n}(x),\theta_{n+1}(x)\}>\frac{1}{\sqrt{a_{n+1}^{2}+4}}. |  |

These results can easily be derived using the natural extension of the Gauss map (see e.g. [28, 15]), and thus by Theorem 4.1 may also be derived through the set-up of this paper. Subsection 5.3 builds a general framework for studying consecutive approximation coefficients corresponding to subsequences of rcf -convergents and mediants determined by inducible R ⊂ Ω R\subset\Omega.

In 1936, Paul Lévy ( [46]) proved the following important and classical result: for almost all x ∈ [0, 1] x\in[0,1],

(5.2) |  | lim n → ∞ 1 n ​ log ⁡ q n = π 2 12 ​ log ⁡ 2. \lim_{n\to\infty}\frac{1}{n}\log q_{n}=\frac{\pi^{2}}{12\log 2}. |  |

As a corollary of this and the fact that 1 / 2 ​ q n ​ q n + 1 < | x − p n / q n | < 1 / q n ​ q n + 1 1/2q_{n}q_{n+1}<|x-p_{n}/q_{n}|<1/q_{n}q_{n+1}, it follows that for almost every x ∈ [0, 1] x\in[0,1],

(5.3) |  | lim n → ∞ 1 n ​ log ⁡ | x − p n q n | = − π 2 6 ​ log ⁡ 2. \lim_{n\to\infty}\frac{1}{n}\log\left|x-\frac{p_{n}}{q_{n}}\right|=-\frac{\pi^{2}}{6\log 2}. |  |

In § 5.4, we obtain a Lévy-type theorem for subsequences of rcf -convergents and mediants corresponding to proper inducible subregions R ⊂ Ω R\subset\Omega, which generalises a number of existing results from the literature. It should be mentioned that originally Lévy’s result (and similar other results by Lévy and Khintchine) also gave a ‘speed of convergence,’ as its proof relied on probability theory and was derived from the Gauss-Kuzmin-Lévy Theorem; see e.g. [24] for more details. As we use ergodic theory, such speeds cannot be given.

### 5.1. Approximation coefficients and their limiting distributions

In this subsection we obtain—among new results—several metrical theorems of [5, 27, 6, 31, 7] as simple corollaries. Some of the theorems of [6] are obtained in a similar fashion in [25] using the natural extension of *Denjoy’s canonical continued fraction map*T d: [0, ∞) → [0, ∞) T_{d}:[0,\infty)\to[0,\infty), defined by

 | T d ​ ( x):= { 0 x = 0, 1 − x x x ≤ 1, 1 x x > 1. T_{d}(x):=\begin{cases}0&x=0,\\ \frac{1-x}{x}&x\leq 1,\\ \frac{1}{x}&x>1.\end{cases} |  |

In fact, the Farey tent map F F is the first-return map of T d T_{d} to [0, 1] [0,1], and the proofs of [25] and those found below are closely related. However, while the domain Ω \Omega of the natural extension of F F is bounded, the domain of the natural extension of T d T_{d} considered in [25] is the unbounded region ( [0, 1) × [0, ∞)) ∪ ( [1, ∞) × [0, 1]) ([0,1)\times[0,\infty))\cup([1,\infty)\times[0,1]). We find the new proofs in the setting of ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}) to be particularly insightful given their concrete geometric realisation within Ω \Omega.

For any x ∈ ℝ x\in\mathbb{R} and p / q ∈ ℚ p/q\in\mathbb{Q} with gcd ​ { p, q } = 1 \text{gcd}\{p,q\}=1 and q > 0 q>0, set

 | Θ ⁡ ( x, p / q):= q ​ | q ​ x − p |. \Theta(x,p/q):=q|qx-p|. |  |

Observe that

 | | x − p q | = Θ ⁡ ( x, p / q) q 2, \left|x-\frac{p}{q}\right|=\frac{\Theta(x,p/q)}{q^{2}}, |  |

so the approximation coefficient Θ ⁡ ( x, p / q) \Theta(x,p/q) gives a measure of how well the rational p / q p/q approximates x x. Notice that Θ ⁡ ( x, p n / q n) = θ n ​ ( x) \Theta(x,p_{n}/q_{n})=\theta_{n}(x) when p n / q n p_{n}/q_{n} is the n th n^{\text{th}} rcf -convergent of x x. When p / q = u n / s n = P n − 1 / Q n − 1 p/q=u_{n}/s_{n}=P_{n-1}/Q_{n-1} is the ( n − 1) st (n-1)^{\text{st}} Farey convergent of x x, we use the special notation

 | Θ n ​ ( x):= Θ ⁡ ( x, u n / s n). \Theta_{n}(x):=\Theta(x,u_{n}/s_{n}). |  |

Similarly, for an inducible subregion R ⊂ Ω R\subset\Omega, we set

(5.4) |  | Θ n R ​ ( x):= Θ ⁡ ( x, u n R / s n R). \Theta_{n}^{R}(x):=\Theta(x,u_{n}^{R}/s_{n}^{R}). |  |

The following result—which is central to the remainder of the paper—states that the n th n^{\text{th}} approximation coefficient Θ n ​ ( x) \Theta_{n}(x) is computed explicitly in terms of the n th n^{\text{th}} point ( x n, y n) (x_{n},y_{n}) in the ℱ \mathcal{F} -orbit of ( x, 1) (x,1) and thus depends on both the ‘future’ and the ‘past’ of the F F -orbit of x x. Hence—although the statements of results regarding approximations coefficients are about x ∈ ( 0, 1) x\in(0,1) —the proofs exploit the two-dimensional system ( Ω, ℬ, μ ¯, ℱ) (\Omega,\mathcal{B},\bar{\mu},\mathcal{F}). Define h: Ω \ { ( 0, 0) } → [0, ∞) h:\Omega\backslash\{(0,0)\}\to[0,\infty) by

 | h ⁡ ( x, y):= 1 − y x + y − x ​ y. h(x,y):=\frac{1-y}{x+y-xy}. |  |

###### Proposition 5.1 (cf. Propositions 1.2 and 2.2 of [27]).

For any inducible R ⊂ Ω R\subset\Omega and n ≥ 0 n\geq 0,

 | Θ n ​ ( x) = h ⁡ ( x n, y n) and Θ n R ​ ( x) = h ⁡ ( x n R, y n R). \Theta_{n}(x)=h(x_{n},y_{n})\quad\text{and}\quad\Theta_{n}^{R}(x)=h(x_{n}^{R},y_{n}^{R}). |  |

###### Proof.

Notice from Equations ( 3.2) and ( 4.3) that

 | y n = A [n, 0] ⋅ 1 = r n s n + r n, y_{n}=A_{[n,0]}\cdot 1=\frac{r_{n}}{s_{n}+r_{n}}, |  |

so

 | h ⁡ ( x n, y n) = 1 − y n x n + y n − x n ​ y n = 1 − y n ( 1 − y n) ​ x n + y n = s n s n ​ x n + r n. h(x_{n},y_{n})=\frac{1-y_{n}}{x_{n}+y_{n}-x_{n}y_{n}}=\frac{1-y_{n}}{(1-y_{n})x_{n}+y_{n}}=\frac{s_{n}}{s_{n}x_{n}+r_{n}}. |  |

On the other hand,

 | x = A [0, n] ⋅ x n = u n ​ x n + t n s n ​ x n + r n, x=A_{[0,n]}\cdot x_{n}=\frac{u_{n}x_{n}+t_{n}}{s_{n}x_{n}+r_{n}}, |  |

so

 | Θ n ​ ( x) = s n 2 ​ | x − u n s n | = s n 2 ​ | u n ​ x n + t n s n ​ x n + r n − u n s n | = s n ​ | t n ​ s n − u n ​ r n | s n ​ x n + r n = s n s n ​ x n + r n = h ⁡ ( x n, y n), \Theta_{n}(x)=s_{n}^{2}\left|x-\frac{u_{n}}{s_{n}}\right|=s_{n}^{2}\left|\frac{u_{n}x_{n}+t_{n}}{s_{n}x_{n}+r_{n}}-\frac{u_{n}}{s_{n}}\right|=\frac{s_{n}\left|t_{n}s_{n}-u_{n}r_{n}\right|}{s_{n}x_{n}+r_{n}}=\frac{s_{n}}{s_{n}x_{n}+r_{n}}=h(x_{n},y_{n}), |  |

where the penultimate equality follows from det ​ ( A [0, n]) = ± 1 \text{det}(A_{[0,n]})=\pm 1. The second equality of the proposition statement now follows from the first:

 | Θ n R ​ ( x) = Θ ⁡ ( x, u n R / s n R) = Θ ⁡ ( x, u N n / s N n) = Θ N n ​ ( x) = h ⁡ ( x N n, y N n) = h ⁡ ( x n R, y n R). \Theta_{n}^{R}(x)=\Theta(x,u_{n}^{R}/s_{n}^{R})=\Theta(x,u_{N_{n}}/s_{N_{n}})=\Theta_{N_{n}}(x)=h(x_{N_{n}},y_{N_{n}})=h(x_{n}^{R},y_{n}^{R}). |  |

∎

Figure 3. The curves h ⁡ ( x, y) = z h(x,y)=z for z ∈ { 0, 1, 2, 3, 4 } z\in\{0,1,2,3,4\}. The region S 1 S_{1} is the shaded region above the curve h ⁡ ( x, y) = 1 h(x,y)=1.

For z ∈ [0, ∞) z\in[0,\infty), let

 | S z:= { ( x, y) ∈ Ω | h ⁡ ( x, y) ≤ z }; S_{z}:=\{(x,y)\in\Omega\ |\ h(x,y)\leq z\}; |  |

see Figure 3. The previous result together with Corollary 4.9 allows us to calculate the asymptotic relative frequency of bounded approximation coefficients Θ n R ​ ( x) ≤ z \Theta_{n}^{R}(x)\leq z as the μ ¯ R \bar{\mu}_{R} -measure of S z ∩ R S_{z}\cap R:

###### Theorem 5.2.

For any proper inducible subregion R ⊂ Ω R\subset\Omega, almost every x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} satisfies

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = μ ¯ R ​ ( S z ∩ R) for all z ∈ [0, ∞). \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}=\bar{\mu}_{R}(S_{z}\cap R)\quad\text{for all}\quad z\in[0,\infty). |  |

###### Proof.

With the stated assumptions, Proposition 5.1 and Corollary 4.9 give that for almost every irrational x ∈ ( 0, 1) x\in(0,1), it follows for every z ∈ [0, ∞) z\in[0,\infty)

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = \displaystyle\lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}= | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | h ⁡ ( x k R, y k R) ≤ z } \displaystyle\lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ h(x_{k}^{R},y_{k}^{R})\leq z\} |  |

 | = \displaystyle= | lim n → ∞ 1 n ​ ∑ k = 0 n − 1 𝟏 S z ∩ R ​ ( x k R, y k R) \displaystyle\lim_{n\to\infty}\frac{1}{n}\sum_{k=0}^{n-1}\mathbf{1}_{S_{z}\cap R}(x_{k}^{R},y_{k}^{R}) |  |

 | = \displaystyle= | μ ¯ R ​ ( S z ∩ R). \displaystyle\bar{\mu}_{R}(S_{z}\cap R). |  |

∎

Figure 4. The regions R R considered in Corollaries 5.4 – 5.11 and 5.13.

Theorem 5.2 allows us to easily obtain a number of classical and new results on the limiting distributions of approximation coefficients corresponding to particular subsequences of rcf -convergents and mediants of generic x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}. The proofs of the corollaries below follow the same general procedure. For a given proper inducible subregion R ⊂ Ω R\subset\Omega, one first finds the infimum, z − z_{-}, and supremum, z + z_{+}, values of z z for which h ⁡ ( x, y) = z h(x,y)=z intersects R R. By Proposition 5.1, these give bounds on Θ n R ​ ( x) \Theta_{n}^{R}(x). That the bounds are optimal follows from Theorem 5.2: for any z ∈ ( z −, z +) z\in(z_{-},z_{+}) one finds μ ¯ R ​ ( S z ∩ R) ∈ ( 0, 1) \bar{\mu}_{R}(S_{z}\cap R)\in(0,1), and thus the limiting distribution of Theorem 5.2 implies that for almost every x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}, there exist n n for which Θ n R ​ ( x) ≤ z \Theta_{n}^{R}(x)\leq z and n n for which Θ n R ​ ( x) > z \Theta_{n}^{R}(x)>z. Moreover, Theorem 5.2 leads to an explicit computation of the asymptotic relative frequency

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z }; \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}; |  |

it is simply a matter of calculating the μ ¯ \bar{\mu} -measures of S z ∩ R S_{z}\cap R and R R and taking their quotient. The former measure depends on how the curve h ⁡ ( x, y) = z h(x,y)=z intersects the region R R, and these different possible intersections give rise to the different branches of the frequency functions seen below. The limiting distributions in each of the following corollaries are plotted here ( [https://www.desmos.com/calculator/pnsu8hcytq][6]) via Desmos ( [19]).

###### Remark 5.3.

Each of the limiting distributions that we ‘re-obtain’ below were originally formulated assuming that the corresponding subsequences of rcf -convergents and mediants are ordered with increasing denominators. However, recall from ( 3.10) that the denominators of the sequence ( u n / s n) n ≥ 0 (u_{n}/s_{n})_{n\geq 0} of Farey convergents are not necessarily increasing, and hence the same is true of the subsequence ( u n R / s n R) n ≥ 0 (u_{n}^{R}/s_{n}^{R})_{n\geq 0} for inducible R ⊂ Ω R\subset\Omega. Proposition 6.1 —the statement and proof of which are found in the appendix (§ 6)—states that for the purposes of these limiting distributions, our reordering is innocuous and thus the original results do in fact follow from our methods.

The first of our corollaries is the Doeblin–Lenstra conjecture, which was first proven in [5]; see Example 4.4 and Figure 4.i. For this we sketch the computations outlined above Remark 5.3; proofs of the remaining corollaries are similar, though at times more tedious.

###### Corollary 5.4 (Doeblin–Lenstra, Theorem 1 of [5]).

Set R:= H 1 R:=H_{1} so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = { p j − 1 / q j − 1 } j ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{p_{j-1}/q_{j-1}\}_{j\geq 0}. |  |

Then for n > 0 n>0,

 | 0 < Θ n R ​ ( x) < 1, 0<\Theta_{n}^{R}(x)<1, |  |

with the upper and lower bounds optimal, and for almost every such x x,

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = { 1 C ​ z, 0 ≤ z ≤ 1 / 2, 1 C ​ ( 1 − z + log ⁡ ( 2 ​ z)), 1 / 2 ≤ z ≤ 1, \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}=\begin{cases}\frac{1}{C}z,&0\leq z\leq 1/2,\\ \frac{1}{C}\left(1-z+\log\left(2z\right)\right),&1/2\leq z\leq 1,\end{cases} |  |

where C:= μ ¯ ​ ( H 1) = log ⁡ 2 C:=\bar{\mu}(H_{1})=\log 2.

###### Proof.

The lower and upper bounds on Θ n R ​ ( x) \Theta_{n}^{R}(x) follow from the argument above Remark 5.3: the infimum, z − z_{-}, and supremum, z + z_{+}, of values z z for which h ⁡ ( x, y) = z h(x,y)=z intersects R = H 1 R=H_{1} are 0 0 and 1 1, respectively (see Figure 3).

For the limiting distribution of approximation coefficients, it suffices to compute μ ¯ R ​ ( S z ∩ H 1) \bar{\mu}_{R}(S_{z}\cap H_{1}) for each z ∈ [0, 1] z\in[0,1], and to set C = μ ¯ ​ ( H 1) = μ ¯ ​ ( S 1 ∩ H 1) C=\bar{\mu}(H_{1})=\bar{\mu}(S_{1}\cap H_{1}). Fix z ∈ [0, 1] z\in[0,1]. Rearranging terms, h ⁡ ( x, y) = z h(x,y)=z may be written as y = f ⁡ ( x, z) y=f(x,z), where

 | f ⁡ ( x, z) = 1 − x ​ z 1 − x ​ z + z. f(x,z)=\frac{1-xz}{1-xz+z}. |  |

Now ∂ f ∂ x ≤ 0, \frac{\partial f}{\partial x}\leq 0, so f f is monotone decreasing as a function of x x. For 0 ≤ z ≤ 1 / 2 0\leq z\leq 1/2, both f ⁡ ( 0, z) = 1 / ( 1 + z) f(0,z)=1/(1+z) and f ⁡ ( 1, z) = 1 − z f(1,z)=1-z are bounded between 1 / 2 1/2 and 1 1, so the same is true of f ⁡ ( x, z) f(x,z) for all 0 ≤ x ≤ 1 0\leq x\leq 1. Hence for 0 ≤ z ≤ 1 / 2, 0\leq z\leq 1/2, one calculates

 | μ ¯ ​ ( S z ∩ H 1) = ∫ 0 1 ∫ f ⁡ ( x, z) 1 d ​ y ​ d ​ x ( x + y − x ​ y) 2 = z. \bar{\mu}(S_{z}\cap H_{1})=\int_{0}^{1}\int_{f(x,z)}^{1}\frac{dydx}{(x+y-xy)^{2}}=z. |  |

On the other hand, if 1 / 2 ≤ z ≤ 1 1/2\leq z\leq 1, then 1 / 2 ≤ f ⁡ ( 0, z) ≤ 1 1/2\leq f(0,z)\leq 1 while f ⁡ ( 1, z) ≤ 1 / 2 f(1,z)\leq 1/2. One finds that f ⁡ ( ( 1 − z) / z, z) = 1 / 2 f((1-z)/z,z)=1/2 and thus computes

 | μ ¯ ​ ( S z ∩ H 1) = ∫ 0 1 − z z ∫ f ⁡ ( x, z) 1 d ​ y ​ d ​ x ( x + y − x ​ y) 2 + ∫ 1 − z z 1 ∫ 1 / 2 1 d ​ y ​ d ​ x ( x + y − x ​ y) 2 = 1 − z + log ⁡ ( 2 ​ z). \bar{\mu}(S_{z}\cap H_{1})=\int_{0}^{\frac{1-z}{z}}\int_{f(x,z)}^{1}\frac{dydx}{(x+y-xy)^{2}}+\int_{\frac{1-z}{z}}^{1}\int_{1/2}^{1}\frac{dydx}{(x+y-xy)^{2}}=1-z+\log(2z). |  |

In particular, C = μ ¯ ​ ( H 1) = μ ¯ ​ ( S 1 ∩ H 1) = log ⁡ 2 C=\bar{\mu}(H_{1})=\bar{\mu}(S_{1}\cap H_{1})=\log 2. ∎

###### Remark 5.5.

Note that the limiting distribution of Θ n R ​ ( x), R = H 1, \Theta_{n}^{R}(x),\ R=H_{1}, in Corollary 5.4 is linear on the (maximal) interval [0, 1 / 2] [0,1/2]; the supremum 1 / 2 1/2 of this interval is called the *Lenstra constant*. The Lenstra constant coincides with the *Legendre constant*, which is defined as the infimum of real numbers c > 0 c>0 for which Θ ⁡ ( x, p / q) < c \Theta(x,p/q)<c implies that p / q p/q is a rcf -convergent of x x (that is, p / q = u n R / s n R p/q=u_{n}^{R}/s_{n}^{R} for some n n); see Theorem 5.14 below. Analogues of Lenstra and Legendre constants can be defined for other continued fraction algorithms. In [51], Nakada shows that for a large class of algorithms for which the Legendre constant exists, the Lenstra constant also exists and equals the Legendre constant.

In each of the limiting distributions of approximation coefficients Θ n R ​ ( x) \Theta_{n}^{R}(x) below, a Lenstra-type constant may be defined as the supremum of the domain of the linear part. However, we caution the reader that the existence of a Lenstra-type constant for R R does *not*necessarily imply the existence of a Legendre-type constant for R R; in fact, results of Erdös and of Brown and Yin imply that for any c > 1 c>1, there is no proper inducible R R for which 1 < Θ ⁡ ( x, p / q) < c 1<\Theta(x,p/q)<c implies that p / q = u n R / s n R p/q=u_{n}^{R}/s_{n}^{R} for some n n (see [7]).

The next corollary is a result of Bosma ( [6]) and concerns approximation coefficients of the λ th \lambda^{\text{th}} mediant convergents; see Example 4.4 and Figure 4.ii.

###### Corollary 5.6 (Theorem 1.9 of [6]).

Set R:= H λ + 1, λ > 0, R:=H_{\lambda+1},\ \lambda>0, so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = { ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) | λ < a j + 1 } j ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\ |\ \lambda<a_{j+1}\}_{j\geq 0}. |  |

Then for n > 0 n>0,

 | λ λ + 1 < Θ n R ​ ( x) < λ + 1, \frac{\lambda}{\lambda+1}<\Theta_{n}^{R}(x)<\lambda+1, |  |

with the upper and lower bounds optimal, and for almost every such x x,

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = { 1 C ​ ( λ + 1 λ ​ z − 1 + log ⁡ λ ( λ + 1) ​ z), λ λ + 1 ≤ z ≤ λ + 1 λ + 2, 1 C ​ ( 1 λ ⁡ ( λ + 1) ​ z + log ⁡ λ ⁡ ( λ + 2) ( λ + 1) 2), λ + 1 λ + 2 ≤ z ≤ λ, 1 C ​ ( 1 − 1 λ + 1 ​ z + log ⁡ ( λ + 2 ( λ + 1) 2 ​ z)), λ ≤ z ≤ λ + 1, \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}=\begin{cases}\frac{1}{C}\left(\frac{\lambda+1}{\lambda}z-1+\log\frac{\lambda}{(\lambda+1)z}\right),&\frac{\lambda}{\lambda+1}\leq z\leq\frac{\lambda+1}{\lambda+2},\\ \frac{1}{C}\left(\frac{1}{\lambda(\lambda+1)}z+\log\frac{\lambda(\lambda+2)}{(\lambda+1)^{2}}\right),&\frac{\lambda+1}{\lambda+2}\leq z\leq\lambda,\\ \frac{1}{C}\left(1-\frac{1}{\lambda+1}z+\log\left(\frac{\lambda+2}{(\lambda+1)^{2}}z\right)\right),&\lambda\leq z\leq\lambda+1,\end{cases} |  |

where C:= μ ¯ ​ ( H λ + 1) = log ⁡ λ + 2 λ + 1 C:=\bar{\mu}(H_{\lambda+1})=\log\frac{\lambda+2}{\lambda+1}.

Next we consider R:= V a, a > 0 R:=V_{a},\ a>0, which gives—in addition to the rcf -convergents p j − 1 / q j − 1 p_{j-1}/q_{j-1} for which a j + 1 = a a_{j+1}=a —final, next-to-final, and so on mediant convergents when a = 1, a = 2, a=1,\ a=2, and so on, respectively; see Example 4.4 and Figure 4.iii.

###### Corollary 5.7.

Set R:= V a, a > 0, R:=V_{a},\ a>0, so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = { ( ( a j + 1 − a) ​ p j + p j − 1) / ( ( a j + 1 − a) ​ q j + q j − 1) | a j + 1 ≥ a } j ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{((a_{j+1}-a)p_{j}+p_{j-1})/((a_{j+1}-a)q_{j}+q_{j-1})\ |\ a_{j+1}\geq a\}_{j\geq 0}. |  |

Then for n > 0 n>0,

 | 0 < Θ n R ​ ( x) < a + 1, 0<\Theta_{n}^{R}(x)<a+1, |  |

with the upper and lower bounds optimal, and for almost every such x x,

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = { 1 C ​ ( 1 a ⁡ ( a + 1) ​ z), 0 ≤ z ≤ a, 1 C ​ ( 1 − 1 a + 1 ​ z + log ⁡ ( 1 a ​ z)), a ≤ z ≤ a + 1, \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}=\begin{cases}\frac{1}{C}\left(\frac{1}{a(a+1)}z\right),&0\leq z\leq a,\\ \frac{1}{C}\left(1-\frac{1}{a+1}z+\log\left(\frac{1}{a}z\right)\right),&a\leq z\leq a+1,\end{cases} |  |

where C:= μ ¯ ​ ( V a) = log ⁡ a + 1 a C:=\bar{\mu}(V_{a})=\log\frac{a+1}{a}.

When a = 1 a=1, Corollary 5.7 above is similar to Theorem 3.2 of [6] which investigates approximation coefficients of final mediants of x x, i.e., of mediants of the form

 | ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1. \frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}}. |  |

However, when R = V 1 R=V_{1}, the Farey convergents { u n R / s n R } n ≥ 0 \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0} consist not only of these final mediants, but also of convergents of the form p j − 1 / q j − 1 p_{j-1}/q_{j-1} where a j + 1 = 1 a_{j+1}=1. By removing the region H 1 H_{1} from R R, we omit these convergents from the set { u n R / s n R } n ≥ 0 \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0} and obtain the following generalisation of Bosma’s result (see Figure 4.iv):

###### Corollary 5.8 (Contains Theorem 3.2 of [6] as a special case, namely a = 1 a=1).

Set R:= V a \ H 1, a > 0 R:=V_{a}\backslash H_{1},\ a>0 so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = { ( ( a j + 1 − a) ​ p j + p j − 1) / ( ( a j + 1 − a) ​ q j + q j − 1) | a j + 1 > a } j ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{((a_{j+1}-a)p_{j}+p_{j-1})/((a_{j+1}-a)q_{j}+q_{j-1})\ |\ a_{j+1}>a\}_{j\geq 0}. |  |

Then for n > 0 n>0,

 | a a + 1 < Θ n R ​ ( x) < a + 1, \frac{a}{a+1}<\Theta_{n}^{R}(x)<a+1, |  |

with the upper and lower bounds optimal, and for almost every such x x,

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = { 1 C ​ ( a + 1 a ​ z − 1 + log ⁡ a ( a + 1) ​ z), a a + 1 ≤ z ≤ a + 1 a + 2, 1 C ​ ( 1 a ⁡ ( a + 1) ​ z + log ⁡ a ⁡ ( a + 2) ( a + 1) 2), a + 1 a + 2 ≤ z ≤ a, 1 C ​ ( 1 − 1 a + 1 ​ z + log ⁡ ( a + 2 ( a + 1) 2 ​ z)), a ≤ z ≤ a + 1, \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}=\begin{cases}\frac{1}{C}\left(\frac{a+1}{a}z-1+\log\frac{a}{(a+1)z}\right),&\frac{a}{a+1}\leq z\leq\frac{a+1}{a+2},\\ \frac{1}{C}\left(\frac{1}{a(a+1)}z+\log\frac{a(a+2)}{(a+1)^{2}}\right),&\frac{a+1}{a+2}\leq z\leq a,\\ \frac{1}{C}\left(1-\frac{1}{a+1}z+\log\left(\frac{a+2}{(a+1)^{2}}z\right)\right),&a\leq z\leq a+1,\end{cases} |  |

where C:= μ ¯ ​ ( V a \ H 1) = log ⁡ a + 2 a + 1 C:=\bar{\mu}(V_{a}\backslash H_{1})=\log\frac{a+2}{a+1}.

Bosma ( [6]) also considers all rcf -convergents and mediants whose approximation coefficients are no greater than some fixed z 0 ≥ 0 z_{0}\geq 0, and of these, considers the asymptotic relative frequency of those whose approximation coefficients are no greater than z ≤ z 0 z\leq z_{0} (see Figure 4.v.):

###### Corollary 5.9 (Theorem 2.2 of [6]).

Let z 0 ≥ 0 z_{0}\geq 0 and set R:= S z 0 R:=S_{z_{0}} so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = { u n / s n | Θ ⁡ ( x, u n / s n) ≤ z 0 } n ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{u_{n}/s_{n}\ |\ \Theta(x,u_{n}/s_{n})\leq z_{0}\}_{n\geq 0}. |  |

For almost every such x x,

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = { z z 0, 0 ≤ z ≤ z 0 ≤ 1, z 1 + log ⁡ z 0, 0 ≤ z ≤ 1 ≤ z 0, 1 + log ⁡ z 1 + log ⁡ z 0, 1 ≤ z ≤ z 0. \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}=\begin{cases}\frac{z}{z_{0}},&0\leq z\leq z_{0}\leq 1,\\ \frac{z}{1+\log z_{0}},&0\leq z\leq 1\leq z_{0},\\ \frac{1+\log z}{1+\log z_{0}},&1\leq z\leq z_{0}.\end{cases} |  |

###### Remark 5.10.

Some of the cases in the frequency function of Corollary 5.9 are vacuous, depending on the value of z 0 z_{0}. For instance, if z 0 < 1 z_{0}<1, then only the first case applies. There are similarly vacuous cases in Corollaries 5.11 and 5.13 below.

The next result generalises Theorem 3.1 of [6], which considers approximation coefficients of final mediants corresponding to partial quotients a j + 1 = a a_{j+1}=a for some fixed a ≥ 2 a\geq 2. Here we consider approximation coefficients of rcf -convergents ( λ = 0 \lambda=0) or λ th \lambda^{\text{th}} mediants ( λ > 0 \lambda>0) corresponding to partial quotients a j + 1 = a a_{j+1}=a for fixed a > 0 a>0; see Example 4.5 and Figure 4.vi.

###### Corollary 5.11 (Contains Theorem 3.1 of [6] as a special case, namely a ≥ 2, λ = a − 1 a\geq 2,\ \lambda=a-1).

Let a > 0 a>0 and λ ∈ { 0, …, a − 1 } \lambda\in\{0,\dots,a-1\}, and set R:= V a − λ ∩ H λ + 1 R:=V_{a-\lambda}\cap H_{\lambda+1} so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = { ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) | a j + 1 = a } j ≥ 0. \{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}=\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\ |\ a_{j+1}=a\}_{j\geq 0}. |  |

Then for n > 0 n>0,

 | ( a − λ) ​ λ a < Θ n R ​ ( x) < ( a − λ + 1) ​ ( λ + 1) a + 2, \frac{(a-\lambda)\lambda}{a}<\Theta_{n}^{R}(x)<\frac{(a-\lambda+1)(\lambda+1)}{a+2}, |  |

with the upper and lower bounds optimal, and for almost every such x x,

 |  | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } \displaystyle\lim_{n\to\infty}\frac{1}{n}\#\left\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\right\} |  |

 | = \displaystyle= | { 1 C ​ ( a ( a − λ) ​ λ ​ z − 1 + log ⁡ ( a − λ) ​ λ a ​ z), ( a − λ) ​ λ a ≤ z ≤ min ⁡ { ( a − λ + 1) ​ λ a + 1, ( a − λ) ​ ( λ + 1) a + 1 }, 1 C ​ ( 1 λ ⁡ ( λ + 1) ​ z + log ⁡ ( a + 1) ​ λ a ⁡ ( λ + 1)), ( a − λ) ​ ( λ + 1) a + 1 ≤ z ≤ ( a − λ + 1) ​ λ a + 1, 1 C ​ ( 1 ( a − λ) ​ ( a − λ + 1) ​ z + log ⁡ ( a + 1) ​ ( a − λ) a ⁡ ( a − λ + 1)), ( a − λ + 1) ​ λ a + 1 ≤ z ≤ ( a − λ) ​ ( λ + 1) a + 1, 1 C ​ ( 1 − a + 2 ( a − λ + 1) ​ ( λ + 1) ​ z + log ⁡ ( ( a + 1) 2 a ​ ( a − λ + 1) ​ ( λ + 1) ​ z)), max ⁡ { ( a − λ + 1) ​ λ a + 1, ( a − λ) ​ ( λ + 1) a + 1 } ≤ z ≤ ( a − λ + 1) ​ ( λ + 1) a + 2, \displaystyle\begin{cases}\frac{1}{C}\left(\frac{a}{(a-\lambda)\lambda}z-1+\log\frac{(a-\lambda)\lambda}{az}\right),&\frac{(a-\lambda)\lambda}{a}\leq z\leq\min\left\{\frac{(a-\lambda+1)\lambda}{a+1},\frac{(a-\lambda)(\lambda+1)}{a+1}\right\},\\ \frac{1}{C}\left(\frac{1}{\lambda(\lambda+1)}z+\log\frac{(a+1)\lambda}{a(\lambda+1)}\right),&\frac{(a-\lambda)(\lambda+1)}{a+1}\leq z\leq\frac{(a-\lambda+1)\lambda}{a+1},\\ \frac{1}{C}\left(\frac{1}{(a-\lambda)(a-\lambda+1)}z+\log\frac{(a+1)(a-\lambda)}{a(a-\lambda+1)}\right),&\frac{(a-\lambda+1)\lambda}{a+1}\leq z\leq\frac{(a-\lambda)(\lambda+1)}{a+1},\\ \frac{1}{C}\left(1-\frac{a+2}{(a-\lambda+1)(\lambda+1)}z+\log\left(\frac{(a+1)^{2}}{a(a-\lambda+1)(\lambda+1)}z\right)\right),&\max\left\{\frac{(a-\lambda+1)\lambda}{a+1},\frac{(a-\lambda)(\lambda+1)}{a+1}\right\}\leq z\leq\frac{(a-\lambda+1)(\lambda+1)}{a+2},\end{cases} |  |

where C:= μ ¯ ​ ( V a − λ ∩ H λ + 1) = log ⁡ ( a + 1) 2 a ⁡ ( a + 2) C:=\bar{\mu}(V_{a-\lambda}\cap H_{\lambda+1})=\log\frac{(a+1)^{2}}{a(a+2)}.

As Bosma based his proofs in [6] on the natural extension of the Gauss transformation, which is a dynamical system only dealing with rcf -convergents and no mediant convergents, his proofs are quite involved. Using essentially the same approach but to a ‘larger’ dynamical system (induced transformations on the natural extension of the Farey tent map) makes the proofs of the results from [6] and their generalisations easier.

Notice that for λ ≠ 0 \lambda\neq 0, replacing λ \lambda by a − λ a-\lambda in the previous result leaves the limiting distribution unchanged. Hence we obtain:

###### Corollary 5.12.

Let a > 1, λ ∈ { 1, …, a − 1 }, R 1 = V a − λ ∩ H λ + 1 a>1,\ \lambda\in\{1,\dots,a-1\},\ R_{1}=V_{a-\lambda}\cap H_{\lambda+1} and R 2 = V λ ∩ H a − λ + 1 R_{2}=V_{\lambda}\cap H_{a-\lambda+1} so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R 1 / s n R 1 } n ≥ 0 = { ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) | a j + 1 = a } j ≥ 0 \{u_{n}^{R_{1}}/s_{n}^{R_{1}}\}_{n\geq 0}=\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\ |\ a_{j+1}=a\}_{j\geq 0} |  |

and

 | { u n R 2 / s n R 2 } n ≥ 0 = { ( ( a − λ) ​ p j + p j − 1) / ( ( a − λ) ​ q j + q j − 1) | a j + 1 = a } j ≥ 0. \{u_{n}^{R_{2}}/s_{n}^{R_{2}}\}_{n\geq 0}=\{((a-\lambda)p_{j}+p_{j-1})/((a-\lambda)q_{j}+q_{j-1})\ |\ a_{j+1}=a\}_{j\geq 0}. |  |

Then for almost every such x x, the limiting distributions

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R 1 ​ ( x) ≤ z } = lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R 2 ​ ( x) ≤ z } \lim_{n\to\infty}\frac{1}{n}\#\left\{0\leq k<n\ |\ \Theta_{k}^{R_{1}}(x)\leq z\right\}=\lim_{n\to\infty}\frac{1}{n}\#\left\{0\leq k<n\ |\ \Theta_{k}^{R_{2}}(x)\leq z\right\} |  |

both exist and are equal to that given in Corollary 5.11.

Lastly, we generalise Theorem 4.iii of [7], which considers for fixed k k the approximation coefficients of convergents and the first k k and final k k mediant convergents (see also Theorems 3.1, 3.3 and 2.20 of [27, 6, 31], respectively, when k = 1 k=1). Here—for fixed Λ ≥ 0 \Lambda\geq 0 and A ≥ 1 A\geq 1 —we consider convergents and the first Λ \Lambda and final A A mediant convergents (see Figure 4.vii):

###### Corollary 5.13 (Contains Theorem 4.iii of [7] as a special case, namely Λ = A \Lambda=A).

Let Λ ≥ 0 \Lambda\geq 0 and A ≥ 1 A\geq 1, and set

 | R:= ⋃ λ = 0 Λ H λ + 1 ∪ ⋃ a = 1 A V a R:=\bigcup_{\lambda=0}^{\Lambda}H_{\lambda+1}\cup\bigcup_{a=1}^{A}V_{a} |  |

so that for any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q},

 | { u n R / s n R } n ≥ 0 = \displaystyle\{u_{n}^{R}/s_{n}^{R}\}_{n\geq 0}= | { ( λ p j + p j − 1) / ( λ q j + q j − 1) | 0 ≤ λ ≤ Λ and λ < a j + 1 } j ≥ 0 \displaystyle\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\ |\ 0\leq\lambda\leq\Lambda\quad\text{and}\quad\lambda<a_{j+1}\}_{j\geq 0} |  |

 |  | ∪ { ( ( a j + 1 − a) p j + p j − 1) / ( ( a j + 1 − a) q j + q j − 1) | 1 ≤ a ≤ A and a ≤ a j + 1 } j ≥ 0. \displaystyle\cup\{((a_{j+1}-a)p_{j}+p_{j-1})/((a_{j+1}-a)q_{j}+q_{j-1})\ |\ 1\leq a\leq A\quad\text{and}\quad a\leq a_{j+1}\}_{j\geq 0}. |  |

Then for n > 0 n>0,

 | 0 < Θ n R ​ ( x) < max ⁡ { Λ + 1, A + 1 }, 0<\Theta_{n}^{R}(x)<\max\{\Lambda+1,A+1\}, |  |

with the upper and lower bounds optimal, and for almost every such x x,

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } = μ ¯ R ​ ( S z ∩ R 1) + μ ¯ R ​ ( S z ∩ R 2), \lim_{n\to\infty}\frac{1}{n}\#\left\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\right\}=\bar{\mu}_{R}(S_{z}\cap R_{1})+\bar{\mu}_{R}(S_{z}\cap R_{2}), |  |

where R 1:= ⋃ λ = 0 Λ H λ + 1, R 2 = R \ R 1 R_{1}:=\bigcup_{\lambda=0}^{\Lambda}H_{\lambda+1},\ R_{2}=R\backslash R_{1},

 | μ ¯ R ​ ( S z ∩ R 1) = { 1 C ​ z, 0 ≤ z ≤ Λ + 1 Λ + 2, 1 C ​ ( 1 − 1 Λ + 1 ​ z + log ⁡ ( Λ + 2 Λ + 1 ​ z)), Λ + 1 Λ + 2 ≤ z ≤ Λ + 1, 1 C ​ log ⁡ ( Λ + 2), Λ + 1 ≤ z, \bar{\mu}_{R}(S_{z}\cap R_{1})=\begin{cases}\frac{1}{C}z,&0\leq z\leq\frac{\Lambda+1}{\Lambda+2},\\ \frac{1}{C}\left(1-\frac{1}{\Lambda+1}z+\log\left(\frac{\Lambda+2}{\Lambda+1}z\right)\right),&\frac{\Lambda+1}{\Lambda+2}\leq z\leq\Lambda+1,\\ \frac{1}{C}\log(\Lambda+2),&\Lambda+1\leq z,\end{cases} |  |

and

 | μ ¯ R ​ ( S z ∩ R 2) = { 0, 0 ≤ z ≤ Λ + 1 Λ + 2, 1 C ​ ( Λ + 2 Λ + 1 ​ z − 1 + log ⁡ Λ + 1 ( Λ + 2) ​ z), Λ + 1 Λ + 2 ≤ z ≤ min ⁡ { ( Λ + 1) ​ ( A + 1) Λ + A + 2, 1 }, 1 C ​ ( 1 Λ + 1 ​ z + log ⁡ Λ + 1 Λ + 2), 1 ≤ z ≤ ( Λ + 1) ​ ( A + 1) Λ + A + 2, 1 C ​ ( A A + 1 ​ z + log ⁡ Λ + A + 2 ( Λ + 2) ​ ( A + 1)), ( Λ + 1) ​ ( A + 1) Λ + A + 2 ≤ z ≤ 1, 1 C ​ ( 1 − 1 A + 1 ​ z + log ⁡ ( Λ + A + 2 ( Λ + 2) ​ ( A + 1) ​ z)), max ⁡ { ( Λ + 1) ​ ( A + 1) Λ + A + 2, 1 } ≤ z ≤ A + 1, 1 C ​ ( log ⁡ Λ + A + 2 Λ + 2), A + 1 ≤ z, \bar{\mu}_{R}(S_{z}\cap R_{2})=\begin{cases}0,&0\leq z\leq\frac{\Lambda+1}{\Lambda+2},\\ \frac{1}{C}\left(\frac{\Lambda+2}{\Lambda+1}z-1+\log\frac{\Lambda+1}{(\Lambda+2)z}\right),&\frac{\Lambda+1}{\Lambda+2}\leq z\leq\min\left\{\frac{(\Lambda+1)(A+1)}{\Lambda+A+2},1\right\},\\ \frac{1}{C}\left(\frac{1}{\Lambda+1}z+\log\frac{\Lambda+1}{\Lambda+2}\right),&1\leq z\leq\frac{(\Lambda+1)(A+1)}{\Lambda+A+2},\\ \frac{1}{C}\left(\frac{A}{A+1}z+\log\frac{\Lambda+A+2}{(\Lambda+2)(A+1)}\right),&\frac{(\Lambda+1)(A+1)}{\Lambda+A+2}\leq z\leq 1,\\ \frac{1}{C}\left(1-\frac{1}{A+1}z+\log\left(\frac{\Lambda+A+2}{(\Lambda+2)(A+1)}z\right)\right),&\max\left\{\frac{(\Lambda+1)(A+1)}{\Lambda+A+2},1\right\}\leq z\leq A+1,\\ \frac{1}{C}\left(\log\frac{\Lambda+A+2}{\Lambda+2}\right),&A+1\leq z,\\ \end{cases} |  |

with C = μ ¯ ​ ( R) = log ⁡ ( Λ + A + 2). C=\bar{\mu}(R)=\log(\Lambda+A+2).

### 5.2. On the theorems of Legendre, Fatou–Grace and Koksma

Let p / q ∈ ℚ ∩ [0, 1] p/q\in\mathbb{Q}\cap[0,1] with gcd ​ { p, q } = 1, q > 0, \text{gcd}\{p,q\}=1,\ q>0, and x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}. We recall here the important result of Legendre in the theory of continued fractions:

###### Theorem 5.14 (Legendre, 1798 [44]).

If Θ ⁡ ( x, p / q) < 1 / 2 \Theta(x,p/q)<1/2, then p / q p/q is a rcf -convergent of x x. Moreover, the constant 1 / 2 1/2 is optimal.

That the so-called Legendre constant 1 / 2 1/2 is optimal means that for any c > 1 / 2 c>1/2, there exist p / q p/q and x x as above with Θ ⁡ ( x, p / q) < c \Theta(x,p/q)<c but such that p / q p/q is not a rcf -convergent of x x. As mentioned in § 1 and the introduction to § 5, Legendre’s Theorem implies that the ‘excellent’ rational approximations p / q p/q to an irrational x x are all rcf -convergents of x x. Interpreted in a slightly different way, Legendre’s Theorem gives a sufficient condition to verify that p / q p/q is a rcf -convergent of x x without computing the expansion of x x.

A similar result, first stated by Fatou and proven by Grace (and later Koksma), gives a sufficient condition to verify that p / q p/q is either a rcf -convergent or nearest mediant (i.e., a first or final mediant) of x x:

###### Theorem 5.15 (Fatou–Grace, 1904–1918 [20, 23, 37]).

If Θ ⁡ ( x, p / q) < 1 \Theta(x,p/q)<1, then p / q p/q is either a rcf -convergent or nearest mediant of x x. The constant 1 1 is optimal.

Later, Koksma formulated and proved a similar statement regarding rcf -convergents and first mediants:

###### Theorem 5.16 (Koksma, 1937 [37]).

If Θ ⁡ ( x, p / q) < 2 / 3 \Theta(x,p/q)<2/3, then p / q p/q is either a rcf -convergent or a first mediant of x x. The constant 2 / 3 2/3 is optimal.

In [2], Barbolosi and Jager give refinements of the theorems of Legendre, Fatou–Grace and Koksma. The connections above between the map ℱ \mathcal{F} and Farey convergents allow us to easily reobtain these refinements, assuming Fatou–Grace. We remark here that Barbolosi and Jager’s proofs are in a sense more elementary, as they do not make this assumption. Nevertheless, we find it worthwhile to present a new approach to these results to further highlight the versatility of the natural extension map ℱ \mathcal{F} for studying rcf -convergents and mediants.

We begin by setting necessary notation for the statements of the Barbolosi–Jager refinements. Following [2], for any nonzero rational 10 10 10 Since for any x ∈ ( 0, 1) x\in(0,1) both p − 1 / q − 1 = 1 / 0 p_{-1}/q_{-1}=1/0 and p 0 / q 0 = 0 / 1 p_{0}/q_{0}=0/1 are rcf -convergents of x x, we only consider nonzero rationals p / q p/q in what follows. p / q ∈ ℚ ∩ ( 0, 1] p/q\in\mathbb{Q}\cap(0,1] with gcd ​ { p, q } = 1 \text{gcd}\{p,q\}=1 we set ϵ ⁡ ( p / q):= ( − 1) n \epsilon(p/q):=(-1)^{n}, where n n is the depth of p / q p/q (recall ( 2.3) and the definition of depth succeeding it). For x ∈ ( 0, 1) \ ℚ, x\in(0,1)\backslash\mathbb{Q}, we also set

 | ϵ ⁡ ( x, p / q):= { − 1, x < p / q, 1, p / q < x. \epsilon(x,p/q):=\begin{cases}-1,&x<p/q,\\ 1,&p/q<x.\end{cases} |  |

The signature of p / q p/q with respect to x x is defined as

 | δ ⁡ ( x, p / q):= ϵ ⁡ ( p / q) ​ ϵ ​ ( x, p / q) ∈ { ± 1 }. \delta(x,p/q):=\epsilon(p/q)\epsilon(x,p/q)\in\{\pm 1\}. |  |

The following lemma classifies the signatures of the nonzero and finite Farey convergents of x x:

###### Lemma 5.17.

Suppose x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} has rcf -expansion [0; a 1, a 2, …] [0;a_{1},a_{2},\dots], and let

 | u n / s n = ( λ n ​ p j n + p j n − 1) / ( λ n ​ q j n + q j n − 1) ∈ ℚ \ { 0 } u_{n}/s_{n}=(\lambda_{n}p_{j_{n}}+p_{j_{n}-1})/(\lambda_{n}q_{j_{n}}+q_{j_{n}-1})\in\mathbb{Q}\backslash\{0\} |  |

be the ( n − 1) s ​ t (n-1)^{st} Farey convergent of x x, where 0 ≤ λ n < a j n + 1 0\leq\lambda_{n}<a_{j_{n}+1}. Then δ ⁡ ( x, u n / s n) = − 1 \delta(x,u_{n}/s_{n})=-1 if and only if u n / s n u_{n}/s_{n} is

1. (i)

a rcf -convergent (i.e., λ n = 0 \lambda_{n}=0) with a j n − 1 = 1, j n > 1 a_{j_{n}-1}=1,\ j_{n}>1, or

2. (ii)

a first mediant (i.e., λ n = 1 \lambda_{n}=1).

###### Proof.

It is well-known that the odd- and even-order rcf -convergents ( p 2 ​ k − 1 / q 2 ​ k − 1) k ≥ 0 (p_{2k-1}/q_{2k-1})_{k\geq 0} and ( p 2 ​ k / q 2 ​ k) k ≥ 0 (p_{2k}/q_{2k})_{k\geq 0} form strictly decreasing and strictly increasing sequences, respectively, converging to x x. Moreover, for k ≥ 0 k\geq 0, the mediants satisfy (see §1.4 of [35])

 | x < p 2 ​ k + 1 q 2 ​ k + 1 = a 2 ​ k + 1 ​ p 2 ​ k + p 2 ​ k − 1 a 2 ​ k + 1 ​ q 2 ​ k + q 2 ​ k − 1 < ( a 2 ​ k + 1 − 1) ​ p 2 ​ k + p 2 ​ k − 1 ( a 2 ​ k + 1 − 1) ​ q 2 ​ k + q 2 ​ k − 1 < ⋯ < p 2 ​ k + p 2 ​ k − 1 q 2 ​ k + q 2 ​ k − 1 < p 2 ​ k − 1 q 2 ​ k − 1 x<\frac{p_{2k+1}}{q_{2k+1}}=\frac{a_{2k+1}p_{2k}+p_{2k-1}}{a_{2k+1}q_{2k}+q_{2k-1}}<\frac{(a_{2k+1}-1)p_{2k}+p_{2k-1}}{(a_{2k+1}-1)q_{2k}+q_{2k-1}}<\dots<\frac{p_{2k}+p_{2k-1}}{q_{2k}+q_{2k-1}}<\frac{p_{2k-1}}{q_{2k-1}} |  |

and

 | p 2 ​ k q 2 ​ k < p 2 ​ k + 1 + p 2 ​ k q 2 ​ k + 1 + q 2 ​ k < ⋯ < ( a 2 ​ k + 2 − 1) ​ p 2 ​ k + 1 + p 2 ​ k ( a 2 ​ k + 2 − 1) ​ q 2 ​ k + 1 + q 2 ​ k < a 2 ​ k + 2 ​ p 2 ​ k + 1 + p 2 ​ k a 2 ​ k + 2 ​ q 2 ​ k + 1 + q 2 ​ k = p 2 ​ k + 2 q 2 ​ k + 2 < x. \frac{p_{2k}}{q_{2k}}<\frac{p_{2k+1}+p_{2k}}{q_{2k+1}+q_{2k}}<\dots<\frac{(a_{2k+2}-1)p_{2k+1}+p_{2k}}{(a_{2k+2}-1)q_{2k+1}+q_{2k}}<\frac{a_{2k+2}p_{2k+1}+p_{2k}}{a_{2k+2}q_{2k+1}+q_{2k}}=\frac{p_{2k+2}}{q_{2k+2}}<x. |  |

Thus u n / s n = ( λ n ​ p j n + p j n − 1) / ( λ n ​ q j n + q j n − 1) u_{n}/s_{n}=(\lambda_{n}p_{j_{n}}+p_{j_{n}-1})/(\lambda_{n}q_{j_{n}}+q_{j_{n}-1}) lies between p j n − 1 / q j n − 1 p_{j_{n}-1}/q_{j_{n}-1} and p j n + 1 / q j n + 1 p_{j_{n}+1}/q_{j_{n}+1}, and

 | ϵ ⁡ ( x, u n / s n) = { − 1, j n is even, 1, j n is odd. \epsilon(x,u_{n}/s_{n})=\begin{cases}-1,&\text{$j_{n}$ is even},\\ 1,&\text{$j_{n}$ is odd}.\end{cases} |  |

We now consider the value of ϵ ⁡ ( u n / s n) \epsilon(u_{n}/s_{n}) in cases:

1. (a)

Suppose that λ n = 0 \lambda_{n}=0 and a j n − 1 = 1 a_{j_{n}-1}=1 (the assumption that u n / s n ∈ ℚ \ { 0 } u_{n}/s_{n}\in\mathbb{Q}\backslash\{0\} implies j n > 1 j_{n}>1). Then

 | u n / s n = p j n − 1 / q j n − 1 = [0; a 1, …, a j n − 1] = [0; a 1, …, a j n − 2 + 1], u_{n}/s_{n}=p_{j_{n}-1}/q_{j_{n}-1}=[0;a_{1},\dots,a_{j_{n}-1}]=[0;a_{1},\dots,a_{j_{n}-2}+1], |  |

so the depth of u n / s n u_{n}/s_{n} is j n − 2 j_{n}-2, and

 | ϵ ⁡ ( u n / s n) = { − 1, j n is odd, 1, j n is even. \epsilon(u_{n}/s_{n})=\begin{cases}-1,&\text{$j_{n}$ is odd},\\ 1,&\text{$j_{n}$ is even}.\end{cases} |  |

2. (b)

Suppose that λ n = 0 \lambda_{n}=0 and a j n − 1 > 1 a_{j_{n}-1}>1 (here again j n > 1 j_{n}>1). Then

 | u n / s n = p j n − 1 / q j n − 1 = [0; a 1, …, a j n − 1] = [0; a 1, …, a j n − 1 − 1, 1], u_{n}/s_{n}=p_{j_{n}-1}/q_{j_{n}-1}=[0;a_{1},\dots,a_{j_{n}-1}]=[0;a_{1},\dots,a_{j_{n}-1}-1,1], |  |

so the depth of u n / s n u_{n}/s_{n} is j n − 1 j_{n}-1, and

 | ϵ ⁡ ( u n / s n) = { − 1, j n is even, 1, j n is odd. \epsilon(u_{n}/s_{n})=\begin{cases}-1,&\text{$j_{n}$ is even},\\ 1,&\text{$j_{n}$ is odd}.\end{cases} |  |

3. (c)

Suppose that λ n = 1 \lambda_{n}=1. Then

 | u n / s n = ( p j n + p j n − 1) / ( q j n + q j n − 1) = [0; a 1, …, a j n, 1] = [0; a 1, …, a j n + 1], u_{n}/s_{n}=(p_{j_{n}}+p_{j_{n}-1})/(q_{j_{n}}+q_{j_{n}-1})=[0;a_{1},\dots,a_{j_{n}},1]=[0;a_{1},\dots,a_{j_{n}}+1], |  |

so the depth of u n / s n u_{n}/s_{n} is j n j_{n}, and

 | ϵ ⁡ ( u n / s n) = { − 1, j n is odd, 1, j n is even. \epsilon(u_{n}/s_{n})=\begin{cases}-1,&\text{$j_{n}$ is odd},\\ 1,&\text{$j_{n}$ is even}.\end{cases} |  |

4. (d)

Lastly, if λ n > 1 \lambda_{n}>1, then

 | u n / s n = ( λ n ​ p j n + p j n − 1) / ( λ n ​ q j n + q j n − 1) = [0; a 1, …, a j n, λ n] = [0; a 1, …, a j n, λ n − 1, 1], u_{n}/s_{n}=(\lambda_{n}p_{j_{n}}+p_{j_{n}-1})/(\lambda_{n}q_{j_{n}}+q_{j_{n}-1})=[0;a_{1},\dots,a_{j_{n}},\lambda_{n}]=[0;a_{1},\dots,a_{j_{n}},\lambda_{n}-1,1], |  |

so the depth of u n / s n u_{n}/s_{n} is j n + 1 j_{n}+1, and

 | ϵ ⁡ ( u n / s n) = { − 1, j n is even, 1, j n is odd. \epsilon(u_{n}/s_{n})=\begin{cases}-1,&\text{$j_{n}$ is even},\\ 1,&\text{$j_{n}$ is odd}.\end{cases} |  |

The result now follows by setting δ ⁡ ( x, u n / s n) = ϵ ⁡ ( u n / s n) ​ ϵ ​ ( x, u n / s n) \delta(x,u_{n}/s_{n})=\epsilon(u_{n}/s_{n})\epsilon(x,u_{n}/s_{n}). ∎

Figure 5. Red and blue regions correspond to negative and positive signatures δ ⁡ ( x, u n / s n) = − 1, 1 \delta(x,u_{n}/s_{n})=-1,1, respectively. The curves h ⁡ ( x, y) = z h(x,y)=z are shown in yellow for z ∈ { 1 / 2, 2 / 3, 1, 2 } z\in\{1/2,2/3,1,2\}.

With Lemma 5.17, one may decompose the domain Ω \Omega of ℱ \mathcal{F} according to the signatures of Farey convergents; confer Figure 5. Recall (Example 4.4) that for fixed λ \lambda, the horizontal region H λ + 1 ⊂ Ω H_{\lambda+1}\subset\Omega corresponds to Farey convergents of x x of the form u n / s n = ( λ n ​ p j n + p j n − 1) / ( λ n ​ q j n + q j n − 1) u_{n}/s_{n}=(\lambda_{n}p_{j_{n}}+p_{j_{n}-1})/(\lambda_{n}q_{j_{n}}+q_{j_{n}-1}) with λ n = λ \lambda_{n}=\lambda. Thus Lemma 5.17 implies that the region H 2 H_{2} corresponds to Farey convergents with negative signature δ ⁡ ( x, u n / s n) = − 1 \delta(x,u_{n}/s_{n})=-1, and the region ∪ λ > 1 H λ + 1 \cup_{\lambda>1}H_{\lambda+1} corresponds to Farey convergents with positive signature δ ⁡ ( x, u n / s n) = 1 \delta(x,u_{n}/s_{n})=1. The region H 1 H_{1} corresponding to rcf -convergents u n / s n = p j n − 1 / q j n − 1 u_{n}/s_{n}=p_{j_{n}-1}/q_{j_{n}-1} is further decomposed depending on the value of the partial quotient a j n − 1 a_{j_{n}-1} in the rcf -expansion of x x. Recall from ( 4.4) that if ( x n, y n) = ℱ n ​ ( x, 1) ∈ H 1 (x_{n},y_{n})=\mathcal{F}^{n}(x,1)\in H_{1}, then

 | ( x n, y n) = ( [0; a j n + 1, a j n + 2, …], [0; 1, a j n, a j n − 1, …, a 1]). (x_{n},y_{n})=\big([0;a_{j_{n}+1},a_{j_{n}+2},\dots],[0;1,a_{j_{n}},a_{j_{n}-1},\dots,a_{1}]\big). |  |

The cylinder of points with rcf -expansion beginning with [0; 1, a, b, …] [0;1,a,b,\dots] is the interval

 | ( [0; 1, a, b + 1], [0; 1, a, b]]. \big([0;1,a,b+1],[0;1,a,b]\big]. |  |

Thus, by Lemma 5.17, the regions

 | [0, 1] × ( [0; 1, a, 2], [0; 1, a, 1]] = [0, 1] × ( 2 ​ a + 1 2 ​ a + 3, a + 1 a + 2], a ≥ 1 [0,1]\times\big([0;1,a,2],[0;1,a,1]\big]=[0,1]\times\left(\frac{2a+1}{2a+3},\frac{a+1}{a+2}\right],\quad a\geq 1 |  |

correspond to Farey convergents with negative signature δ ⁡ ( x, u n / s n) = − 1 \delta(x,u_{n}/s_{n})=-1, while the regions

 | [0, 1] × ⋃ b > 1 ( [0; 1, a, b + 1], [0; 1, a, b]] = [0, 1] × ( [0; 1, a], [0; 1, a, 2]] = [0, 1] × ( a a + 1, 2 ​ a + 1 2 ​ a + 3], a ≥ 1. [0,1]\times\bigcup_{b>1}\big([0;1,a,b+1],[0;1,a,b]\big]=[0,1]\times\big([0;1,a],[0;1,a,2]\big]=[0,1]\times\left(\frac{a}{a+1},\frac{2a+1}{2a+3}\right],\quad a\geq 1. |  |

correspond to Farey convergents with positive signature δ ⁡ ( x, u n / s n) = 1 \delta(x,u_{n}/s_{n})=1.

Recall that Theorem 5.15 implies that if Θ ⁡ ( x, p / q) < 1 \Theta(x,p/q)<1, then p / q p/q is *some*Farey convergent 11 11 11 Of course, Theorem 5.15 makes the stronger claim that p / q p/q is a rcf -convergent or nearest mediant, but only this weaker implication is needed. u n / s n u_{n}/s_{n} of x x. With this in mind, Barbolosi and Jager’s refinements now follow easily from Proposition 5.1 and Figure 5:

###### Corollary 5.18 (Theorem 2.2 of [2]).

Let p / q ∈ ℚ ∩ ( 0, 1] p/q\in\mathbb{Q}\cap(0,1] with gcd ​ { p, q } = 1 \text{gcd}\{p,q\}=1 and x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}.

- •

When δ ⁡ ( x, p / q) = − 1 \delta(x,p/q)=-1, Θ ⁡ ( x, p / q) < 1 / 2 \Theta(x,p/q)<1/2 implies that p / q p/q is a rcf -convergent of x x, while Θ ⁡ ( x, p / q) > 2 / 3 \Theta(x,p/q)>2/3 implies that p / q p/q is not a rcf -convergent of x x.

- •

When δ ⁡ ( x, p / q) = 1 \delta(x,p/q)=1, Θ ⁡ ( x, p / q) < 2 / 3 \Theta(x,p/q)<2/3 implies that p / q p/q is a rcf -convergent of x x, while Θ ⁡ ( x, p / q) > 1 \Theta(x,p/q)>1 implies that p / q p/q is not a rcf -convergent of x x.

All constants are optimal.

###### Corollary 5.19 (Theorem 4.3 of [2]).

Let p / q ∈ ℚ ∩ ( 0, 1] p/q\in\mathbb{Q}\cap(0,1] with gcd ​ { p, q } = 1 \text{gcd}\{p,q\}=1 and x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}.

- •

When δ ⁡ ( x, p / q) = − 1 \delta(x,p/q)=-1, Θ ⁡ ( x, p / q) < 1 \Theta(x,p/q)<1 implies p / q p/q is a rcf -convergent or first mediant of x x, while Θ ⁡ ( x, p / q) > 2 \Theta(x,p/q)>2 implies p / q p/q is neither a rcf -convergent nor first mediant of x x.

- •

If δ ⁡ ( x, p / q) = 1 \delta(x,p/q)=1, then p / q p/q is not a first mediant of x x.

All constants are optimal.

Notice that Corollary 5.18 implies Legendre’s Theorem (Theorem 5.14), and Corollaries 5.18 and 5.19 imply Koksma’s Theorem (Theorem 5.16).

###### Corollary 5.20 (Theorem 4.7 of [2]).

Let p / q ∈ ℚ ∩ ( 0, 1] p/q\in\mathbb{Q}\cap(0,1] with gcd ​ { p, q } = 1 \text{gcd}\{p,q\}=1 and x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q}.

- •

Suppose that δ ⁡ ( x, p / q) = − 1 \delta(x,p/q)=-1. If p / q p/q is a final mediant of x x, then it is also a first mediant of x x. Moreover, Θ ⁡ ( x, p / q) < 2 / 3 \Theta(x,p/q)<2/3 implies p / q p/q is a rcf -convergent or a final mediant of x x, while Θ ⁡ ( x, p / q) > 1 \Theta(x,p/q)>1 implies p / q p/q is neither a rcf -convergent nor a final mediant of x x.

- •

When δ ⁡ ( x, p / q) = 1 \delta(x,p/q)=1, Θ ⁡ ( x, p / q) < 1 \Theta(x,p/q)<1 implies that p / q p/q is a rcf -convergent or a final mediant of x x, while Θ ⁡ ( x, p / q) > 2 \Theta(x,p/q)>2 implies that p / q p/q is neither a rcf -convergent nor a nearest mediant of x x.

All constants are optimal.

The Barbolosi–Jager refinements of Legendre, Fatou–Grace and Koksma are refinements of the assumptions on the rational p / q p/q (namely, its signature) which approximates x x. One could instead ask for refinements of the bounds 1 / 2, 2 / 3, 1 1/2,\ 2/3,\ 1 which occur in Theorems 5.14, 5.15 and 5.16. As the next theorem shows, such refinements give information about certain partial quotients occurring in the rcf -expansion of x x.

###### Theorem 5.21.

Fix some positive integer k k. If p / q ∈ ℚ ∩ ( 0, 1) p/q\in\mathbb{Q}\cap(0,1) with gcd ​ { p, q } = 1 \text{gcd}\{p,q\}=1, x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} and

 | k k + 1 ≤ Θ ⁡ ( x, p / q) < k + 1 k + 2, \frac{k}{k+1}\leq\Theta(x,p/q)<\frac{k+1}{k+2}, |  |

then one of the following holds:

1. (i)

p / q p/q is a rcf -convergent of the form

 | p q = p j − 1 q j − 1 \frac{p}{q}=\frac{p_{j-1}}{q_{j-1}} |  |

for some j j such that a j = 1 a_{j}=1 and a j + 1 ≥ k a_{j+1}\geq k,

2. (ii)

p / q p/q is a first mediant of the form

 | p q = p j + p j − 1 q j + q j − 1 \frac{p}{q}=\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}} |  |

for some j j such that a j + 1 ≤ k + 1 a_{j+1}\leq k+1, or

3. (iii)

p / q p/q is a final mediant of the form

 | p q = ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1 \frac{p}{q}=\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}} |  |

for some j j such that a j + 1 ≤ k + 1 a_{j+1}\leq k+1.

###### Proof.

Since Θ ⁡ ( x, p / q) < 1 \Theta(x,p/q)<1, Theorem 5.15 implies that there exists some n n such that

 | p q = u n s n = λ n ​ p j n + p j n − 1 λ n ​ q j n + q j n − 1 \frac{p}{q}=\frac{u_{n}}{s_{n}}=\frac{\lambda_{n}p_{j_{n}}+p_{j_{n-1}}}{\lambda_{n}q_{j_{n}}+q_{j_{n-1}}} |  |

is a rcf -convergent or nearest mediant of x x. Moreover, Proposition 5.1 implies that ( x n, y n) ∈ S (x_{n},y_{n})\in S, where

 | S:= { ( x, y) ∈ Ω | k k + 1 ≤ h ⁡ ( x, y) < k + 1 k + 2 } ⊂ V 1 ∪ H 1 ∪ H 2. S:=\left\{(x,y)\in\Omega\ \Big|\ \frac{k}{k+1}\leq h(x,y)<\frac{k+1}{k+2}\right\}\subset V_{1}\cup H_{1}\cup H_{2}. |  |

Suppose ( x n, y n) ∈ S ∩ H 1 (x_{n},y_{n})\in S\cap H_{1}, so that u n / s n = p j n − 1 / q j n − 1 u_{n}/s_{n}=p_{j_{n-1}}/q_{j_{n-1}}. The curve h ⁡ ( x, y) = k / ( k + 1) h(x,y)=k/(k+1) passes through the points ( 0, k + 1 2 ​ k + 1) \left(0,\frac{k+1}{2k+1}\right) and ( 1 k, 1 2) \left(\frac{1}{k},\frac{1}{2}\right) (see, for instance, the curves determined by z = 1 / 2 z=1/2 and z = 2 / 3 z=2/3 in Figure 5 for k = 1 k=1 and k = 2 k=2, respectively). Using this, one finds S ∩ H 1 ⊂ [0, 1 / k] × ( 1 / 2, 2 / 3] S\cap H_{1}\subset[0,1/k]\times(1/2,2/3], which is contained in the union of { 0, 1 } × ( 1 / 2, 2 / 3] \{0,1\}\times(1/2,2/3] and

 | ℱ ⁡ ( V 1 ∩ H 1) ∩ ⋃ a ≥ k V a. \mathcal{F}(V_{1}\cap H_{1})\cap\bigcup_{a\geq k}V_{a}. |  |

Irrationality of x x implies x n ∉ { 0, 1 }, x_{n}\notin\{0,1\}, so ( x n, y n) ∈ ℱ ⁡ ( V 1 ∩ H 1) ∩ ⋃ a ≥ k V a (x_{n},y_{n})\in\mathcal{F}(V_{1}\cap H_{1})\cap\bigcup_{a\geq k}V_{a}. That ( x n, y n) ∈ ℱ ⁡ ( V 1 ∩ H 1) (x_{n},y_{n})\in\mathcal{F}(V_{1}\cap H_{1}) implies a j n = 1 a_{j_{n}}=1, and that ( x n, y n) ∈ ⋃ a ≥ k V a (x_{n},y_{n})\in\bigcup_{a\geq k}V_{a} implies a j n + 1 ≥ k a_{j_{n}+1}\geq k, proving case (i). The other two cases are proven similarly, considering instead when ( x n, y n) (x_{n},y_{n}) belongs to S ∩ H 2 S\cap H_{2} and S ∩ V 1 S\cap V_{1}, respectively. ∎

In [43], Kuipers and Meulenbeld give sufficient conditions to guarantee that the approximation coefficients corresponding to first and final mediants are less than 1 1. This partial converse of Theorem 5.15 is also easily obtained via ℱ \mathcal{F}:

###### Corollary 5.22 (Theorem 1 of [43]).

Let x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}. Suppose that a j + 1 ≥ 2 a_{j+1}\geq 2 for some j ≥ 0 j\geq 0. If a j + 1 ≤ a j + 1 a_{j+1}\leq a_{j}+1, then

 | Θ ⁡ ( x, p j + p j − 1 q j + q j − 1) < 1, \Theta\left(x,\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}}\right)<1, |  |

while if a j + 1 ≤ a j + 2 + 1 a_{j+1}\leq a_{j+2}+1, then

 | Θ ⁡ ( x, ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1) < 1. \Theta\left(x,\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}}\right)<1. |  |

###### Proof.

With notation as in the statement, let n n be such that u n / s n = ( p j + p j − 1) / ( q j + q j − 1) u_{n}/s_{n}=(p_{j}+p_{j-1})/(q_{j}+q_{j-1}), and suppose a j + 1 ≤ a j + 1 a_{j+1}\leq a_{j}+1. Then

 | ( x n, y n) = ( [0; a j + 1 − 1, a j + 2, a j + 3, …], [0; 2, a j, …, a 1]) ∈ V a j + 1 − 1 ∩ H 2, (x_{n},y_{n})=([0;a_{j+1}-1,a_{j+2},a_{j+3},\dots],[0;2,a_{j},\dots,a_{1}])\in V_{a_{j+1}-1}\cap H_{2}, |  |

and we have both x n > 1 / a j + 1 x_{n}>1/a_{j+1} and—since a j ≥ a j + 1 − 1 a_{j}\geq a_{j+1}-1 —also y n ≥ [0; 2, a j + 1 − 1] = ( a j + 1 − 1) / ( 2 ​ a j + 1 − 1) y_{n}\geq[0;2,a_{j+1}-1]=(a_{j+1}-1)/(2a_{j+1}-1). By Proposition 5.1,

 | Θ ⁡ ( x, p j + p j − 1 q j + q j − 1) = h ⁡ ( x n, y n) < h ⁡ ( 1 a j + 1, a j + 1 − 1 2 ​ a j + 1 − 1) = 1. \Theta\left(x,\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}}\right)=h(x_{n},y_{n})<h\left(\frac{1}{a_{j+1}},\frac{a_{j+1}-1}{2a_{j+1}-1}\right)=1. |  |

A similar argument proves the claim for final mediants. ∎

### 5.3. Consecutive approximation coefficients

In [29] and [30] a two-dimensional, ergodic dynamical system ( Δ, ℬ, ν, ℋ) (\Delta,\mathcal{B},\nu,\mathcal{H}) was introduced to study consecutive approximation coefficients θ n ​ ( x) \theta_{n}(x) of rcf -convergents. The map ℋ \mathcal{H} satisfies

(5.5) |  | ℋ ⁡ ( θ n − 1 ​ ( x), θ n ​ ( x)) = ( θ n ​ ( x), θ n + 1 ​ ( x)), n > 0, \mathcal{H}(\theta_{n-1}(x),\theta_{n}(x))=(\theta_{n}(x),\theta_{n+1}(x)),\quad n>0, |  |

and is conjugate to the natural extension map 𝒢 \mathcal{G} of the Gauss map. This system has been used to obtain deep insights into metrical properties of approximation coefficients ( [29, 30, 28, 39]). Maps which satisfy the property analogous to ( 5.5) have also been developed for S S -expansions, which contain a wide class of well-studied continued fractions algorithms including the rcf, Hurwitz’ singular continued fraction, Minkowski’s diagonal continued fraction and Nakada’s α \alpha -continued fractions for 1 / 2 ≤ α ≤ 1 1/2\leq\alpha\leq 1 ( [40]). In this subsection we introduce the analogous framework for the induced systems ( R, ℬ ∩ R, μ ¯ R, ℱ R) (R,\mathcal{B}\cap R,\bar{\mu}_{R},\mathcal{F}_{R}). We briefly remark that as S S -expansions are obtained via induced maps of the Gauss natural extension, Theorem 4.1 implies that each of the aforementioned analogues of ℋ \mathcal{H} may be obtained from the current setting.

###### Proposition 5.23.

Let R ⊂ Ω R\subset\Omega be an inducible subregion and x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}. Then the ( n + 1) st (n+1)^{\text{st}} approximation coefficient Θ n + 1 R ​ ( x) \Theta_{n+1}^{R}(x) corresponding to R R may be written in terms of ( x n R, y n R), n ≥ 0, (x_{n}^{R},y_{n}^{R}),\ n\geq 0, as

 | Θ n + 1 R ​ ( x) = det ( A) ​ ( u − s ​ x n R) ​ ( u + ( s − u) ​ y n R) x n R + y n R − x n R ​ y n R, \Theta_{n+1}^{R}(x)=\det(A)\frac{(u-sx_{n}^{R})(u+(s-u)y_{n}^{R})}{x_{n}^{R}+y_{n}^{R}-x_{n}^{R}y_{n}^{R}}, |  |

where

 | A = ( u t s r):= A [0, r R ​ ( x n R, y n R)] ​ ( x n R), A=\begin{pmatrix}u&t\\ s&r\end{pmatrix}:=A_{[0,r_{R}(x_{n}^{R},y_{n}^{R})]}(x_{n}^{R}), |  |

with A [0, r R ​ ( x n R, y n R)] ​ ( x n R) A_{[0,r_{R}(x_{n}^{R},y_{n}^{R})]}(x_{n}^{R}) and r R ​ ( x n R, y n R) r_{R}(x_{n}^{R},y_{n}^{R}) defined as in ( 3.3) and ( 4.5), respectively.

###### Proof.

From ( 4.6), we have n ≥ 0 n\geq 0,

 | ( x n + 1 R, y n + 1 R) = ℱ R ​ ( x n R, y n R) = ( ( A [0, r R ​ ( x n R, y n R)] ​ ( x n R)) − 1 ⋅ x n R, A [r R ​ ( x n R, y n R), 0] ​ ( x n R) ⋅ y n R). (x_{n+1}^{R},y_{n+1}^{R})=\mathcal{F}_{R}(x_{n}^{R},y_{n}^{R})=\left(\left(A_{[0,r_{R}(x_{n}^{R},y_{n}^{R})]}(x_{n}^{R})\right)^{-1}\cdot x_{n}^{R},A_{[r_{R}(x_{n}^{R},y_{n}^{R}),0]}(x_{n}^{R})\cdot y_{n}^{R}\right). |  |

A computation essentially identical to that of ( 3.2) gives

 | A [r R ​ ( x n R, y n R), 0] ​ ( x n R) = ( r − t t s + r − ( u + t) u + t), A_{[r_{R}(x_{n}^{R},y_{n}^{R}),0]}(x_{n}^{R})=\begin{pmatrix}r-t&t\\ s+r-(u+t)&u+t\end{pmatrix}, |  |

and thus

 | ( x n + 1 R, y n + 1 R) = ( r ​ x n R − t − s ​ x n R + u, ( r − t) ​ y n R + t ( s + r − ( u + t)) ​ y n R + u + t). (x_{n+1}^{R},y_{n+1}^{R})=\left(\frac{rx_{n}^{R}-t}{-sx_{n}^{R}+u},\frac{(r-t)y_{n}^{R}+t}{(s+r-(u+t))y_{n}^{R}+u+t}\right). |  |

The result is obtained from a computation using this, Proposition 5.1 and the fact that det ( A) = ± 1 \det(A)=\pm 1. ∎

By partitioning R R into subregions on which the left columns of the matrices A [0, r R ​ ( x, y)] ​ ( x) A_{[0,r_{R}(x,y)]}(x) are constant, one can define an explicit function ψ R: R \ { ( 0, 0) } → ℝ 2 \psi_{R}:R\backslash\{(0,0)\}\to\mathbb{R}^{2} satisfying

 | ψ R ​ ( x n R, y n R) = ( Θ n R ​ ( x), Θ n + 1 R ​ ( x)), n ≥ 0, \psi_{R}(x_{n}^{R},y_{n}^{R})=(\Theta_{n}^{R}(x),\Theta_{n+1}^{R}(x)),\quad n\geq 0, |  |

and thus gain insights into consecutive approximation coefficients. This process is demonstrated for three specific inducible subregions R ⊂ Ω R\subset\Omega below.

#### 5.3.1. Consecutive rcf -convergents

Let R = H 1 R=H_{1} as in Example 4.4. For any a ≥ 1 a\geq 1, if ( x, y) ∈ V a ∩ H 1 (x,y)\in V_{a}\cap H_{1}, then

 | A [0, r R ​ ( x, y)] ​ ( x) = A 0 a − 1 ​ A 1 = ( 0 1 1 a). A_{[0,r_{R}(x,y)]}(x)=A_{0}^{a-1}A_{1}=\begin{pmatrix}0&1\\ 1&a\end{pmatrix}. |  |

Define ψ R: R → ℝ 2 \psi_{R}:R\to\mathbb{R}^{2} by

 | ψ R ​ ( x, y) = 1 x + y − x ​ y ​ ( 1 − y, x ​ y). \psi_{R}(x,y)=\frac{1}{x+y-xy}(1-y,xy). |  |

Propositions 5.1 and 5.23 then give that for any irrational x ∈ ( 0, 1) x\in(0,1),

 | ψ R ​ ( x n R, y n R) = ( Θ n R ​ ( x), Θ n + 1 R ​ ( x)), n ≥ 0. \psi_{R}(x_{n}^{R},y_{n}^{R})=(\Theta_{n}^{R}(x),\Theta_{n+1}^{R}(x)),\quad n\geq 0. |  |

One finds that ψ R \psi_{R} is a diffeomorphism between the interior of R R and the interior of the Euclidean triangle with vertices ( 0, 0), ( 0, 1) (0,0),\ (0,1) and ( 1, 0) (1,0); see Figure 6.

Figure 6. Left: The region R = H 1 R=H_{1} from § 5.3.1. Right: The image ψ R ​ ( R) \psi_{R}(R).

From this, one immediately obtains Vahlen’s result that min ⁡ { Θ n R ​ ( x), Θ n + 1 R ​ ( x) } < 1 / 2 \min\{\Theta_{n}^{R}(x),\Theta_{n+1}^{R}(x)\}<1/2 for all n ≥ 0 n\geq 0 ( [56]; see also [30]). Up to the isomorphism of Theorem 4.1, in [30] it is shown that ( Δ, ℬ, ν, ℋ):= ( ψ R ​ ( R), ℬ, ν, ψ R ∘ ℱ R ∘ ψ R − 1) (\Delta,\mathcal{B},\nu,\mathcal{H}):=(\psi_{R}(R),\mathcal{B},\nu,\psi_{R}\circ\mathcal{F}_{R}\circ\psi_{R}^{-1}) forms an ergodic system, where d ​ ν = d ​ x ​ d ​ y / ( log ⁡ 2 ​ 1 − 4 ​ x ​ y) d\nu=dxdy/(\log 2\sqrt{1-4xy}). We refer the reader to [29, 30, 28, 39] for further metrical results which follow from a deeper analysis of this system.

#### 5.3.2. Consecutive Farey convergents

Let R = Ω R=\Omega. Then for any ( x, y) ∈ R (x,y)\in R,

 | A [0, r R ​ ( x, y)] ​ ( x) = A ε ⁡ ( x) = ( 1 − ε ⁡ ( x) ε ⁡ ( x) 1 1). A_{[0,r_{R}(x,y)]}(x)=A_{\varepsilon(x)}=\begin{pmatrix}1-\varepsilon(x)&\varepsilon(x)\\ 1&1\end{pmatrix}. |  |

Define ψ R: R \ { ( 0, 0) } → ℝ 2 \psi_{R}:R\backslash\{(0,0)\}\to\mathbb{R}^{2} by

(5.6) |  | ψ R ​ ( x, y) = { 1 x + y − x ​ y ​ ( 1 − y, 1 − x), x ≤ 1 / 2, 1 x + y − x ​ y ​ ( 1 − y, x ​ y), x > 1 / 2, \psi_{R}(x,y)=\begin{cases}\frac{1}{x+y-xy}(1-y,1-x),&x\leq 1/2,\\ \frac{1}{x+y-xy}(1-y,xy),&x>1/2,\\ \end{cases} |  |

Now Θ n R = Θ n, x n R = x n \Theta_{n}^{R}=\Theta_{n},\ x_{n}^{R}=x_{n} and y n R = y n y_{n}^{R}=y_{n} for each n ≥ 0 n\geq 0, so Propositions 5.1 and 5.23 give

(5.7) |  | ψ R ​ ( x n, y n) = ( Θ n ​ ( x), Θ n + 1 ​ ( x)), n ≥ 0; \psi_{R}(x_{n},y_{n})=\left(\Theta_{n}(x),\Theta_{n+1}(x)\right),\quad n\geq 0; |  |

see Figure 7.

Figure 7. Left: The region R = Ω R=\Omega from § 5.3.2. Right: The image ψ R ​ ( R \ { ( 0, 0) }) \psi_{R}(R\backslash\{(0,0)\}).

The map ψ R \psi_{R} allows one to easily compare consecutive approximation coefficients:

###### Proposition 5.24.

Let x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}. Then for any j ≥ 0 j\geq 0,

 | 1 < 2 ​ Θ ​ ( x, p j q j) + Θ ⁡ ( x, ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1) < 2 1<2\Theta\left(x,\frac{p_{j}}{q_{j}}\right)+\Theta\left(x,\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}}\right)<2 |  |

and for a j + 1 > 1 a_{j+1}>1 and 0 ≤ λ < a j + 1 − 1 0\leq\lambda<a_{j+1}-1,

 | | Θ ⁡ ( x, ( λ + 1) ​ p j + p j − 1 ( λ + 1) ​ q j + q j − 1) − Θ ⁡ ( x, ( λ ​ p j + p j − 1 CLOSE ( λ ​ q j + q j − 1 CLOSE) | < 1. \left|\Theta\left(x,\frac{(\lambda+1)p_{j}+p_{j-1}}{(\lambda+1)q_{j}+q_{j-1}}\right)-\Theta\left(x,\frac{(\lambda p_{j}+p_{j-1}}{(\lambda q_{j}+q_{j-1}}\right)\right|<1. |  |

###### Proof.

Up to non-strict inequalities, the first statement follows from ( 3.10), ( 5.7) and the fact that the image of V 1 V_{1} under ψ R \psi_{R} is bounded 12 12 12 These lines do *not*describe the boundary of ψ R ​ ( V 1) \psi_{R}(V_{1}) (see Figure 7), but rather give upper and lower bounding lines of equal slope. More precise—though less elegant—statements can be made by analysing the boundary of the image. by the lines y = − x / 2 + 1 y=-x/2+1 and y = − x / 2 + 1 / 2 y=-x/2+1/2, and the second from ( 3.10), ( 5.7) and the fact that ψ R ​ ( Ω \ ( V 1 ∪ { ( 0, 0) })) \psi_{R}(\Omega\backslash(V_{1}\cup\{(0,0)\})) is bounded by y = x + 1 y=x+1 and y = x − 1 y=x-1 (see Figure 7). The strict inequalities follow from the irrationality of x x. ∎

The map ψ R \psi_{R} also gives information on the monotonicity of finite sequences of consecutive approximation coefficients. In particular, we find that the approximation coefficients of the mediant convergents ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1), 0 < λ < a j + 1 (\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1}),\ 0<\lambda<a_{j+1}, between p j − 1 / q j − 1 p_{j-1}/q_{j-1} and p j / q j p_{j}/q_{j} first increase and then decrease monotonically in λ \lambda, with the maximum occurring in the middle. This statement is made precise in the following:

###### Theorem 5.25.

Let x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}, and suppose a j + 1 > 1 a_{j+1}>1 for some fixed j ≥ 0 j\geq 0. Then for each p / q ∈ { p j / q j } ∪ { ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) } 0 ≤ λ < a j + 1, p / q ≠ 1 / 0, p/q\in\{p_{j}/q_{j}\}\cup\{(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1})\}_{0\leq\lambda<a_{j+1}},\ p/q\neq 1/0,

 | 0 < Θ ⁡ ( x, p / q) < { a j + 1 + 2 4, a j + 1 even, ( a j + 1 + 1) ​ ( a j + 1 + 3) 4 ​ ( a j + 1 + 2), a j + 1 odd, 0<\Theta(x,p/q)<\begin{cases}\frac{a_{j+1}+2}{4},&\text{$a_{j+1}$ even},\\ \frac{(a_{j+1}+1)(a_{j+1}+3)}{4(a_{j+1}+2)},&\text{$a_{j+1}$ odd},\end{cases} |  |

with the bounds optimal. Moreover,

 | Θ ⁡ ( x, λ ​ p j + p j − 1 λ ​ q j + q j − 1) < Θ ⁡ ( x, λ ′ ​ p j + p j − 1 λ ′ ​ q j + q j − 1) for all 0 ≤ λ < λ ′ ≤ ⌊ a j + 1 / 2 ⌋ \Theta\left(x,\frac{\lambda p_{j}+p_{j-1}}{\lambda q_{j}+q_{j-1}}\right)<\Theta\left(x,\frac{\lambda^{\prime}p_{j}+p_{j-1}}{\lambda^{\prime}q_{j}+q_{j-1}}\right)\quad\text{for all}\quad 0\leq\lambda<\lambda^{\prime}\leq\lfloor a_{j+1}/2\rfloor |  |

and

 | Θ ⁡ ( x, λ ​ p j + p j − 1 λ ​ q j + q j − 1) > Θ ⁡ ( x, λ ′ ​ p j + p j − 1 λ ′ ​ q j + q j − 1) > Θ ⁡ ( x, p j q j) for all ⌈ a j + 1 / 2 ⌉ ≤ λ < λ ′ < a j + 1. \Theta\left(x,\frac{\lambda p_{j}+p_{j-1}}{\lambda q_{j}+q_{j-1}}\right)>\Theta\left(x,\frac{\lambda^{\prime}p_{j}+p_{j-1}}{\lambda^{\prime}q_{j}+q_{j-1}}\right)>\Theta\left(x,\frac{p_{j}}{q_{j}}\right)\quad\text{for all}\quad\lceil a_{j+1}/2\rceil\leq\lambda<\lambda^{\prime}<a_{j+1}. |  |

###### Proof.

Let x x and a j + 1 a_{j+1} be as in the statement, 0 ≤ λ ≤ a j + 1 0\leq\lambda\leq a_{j+1} and let n n be such that u n / s n = p j − 1 / q j − 1 u_{n}/s_{n}=p_{j-1}/q_{j-1}. We begin with the latter claims. We have (recall ( 3.10))

 | Θ n + λ ​ ( x) = Θ ⁡ ( x, u n + λ s n + λ) = { Θ ⁡ ( x, λ ​ p j + p j − 1 λ ​ q j + q j − 1), λ < a j + 1, Θ ⁡ ( x, p j q j), λ = a j + 1, \Theta_{n+\lambda}(x)=\Theta\left(x,\frac{u_{n+\lambda}}{s_{n+\lambda}}\right)=\begin{cases}\Theta\left(x,\frac{\lambda p_{j}+p_{j-1}}{\lambda q_{j}+q_{j-1}}\right),&\lambda<a_{j+1},\\ \Theta\left(x,\frac{p_{j}}{q_{j}}\right),&\lambda=a_{j+1},\\ \end{cases} |  |

so it suffices to show

(5.8) |  | Θ n + λ ​ ( x) < Θ n + λ + 1 ​ ( x), 0 ≤ λ < ⌊ a j + 1 / 2 ⌋ \Theta_{n+\lambda}(x)<\Theta_{n+\lambda+1}(x),\quad 0\leq\lambda<\lfloor a_{j+1}/2\rfloor |  |

and

(5.9) |  | Θ n + λ ​ ( x) > Θ n + λ + 1 ​ ( x), ⌈ a j + 1 / 2 ⌉ ≤ λ < a j + 1. \Theta_{n+\lambda}(x)>\Theta_{n+\lambda+1}(x),\quad\lceil a_{j+1}/2\rceil\leq\lambda<a_{j+1}. |  |

For λ < a j + 1 \lambda<a_{j+1},

 | ( x n + λ, y n + λ) ∈ V a j + 1 − λ ∩ H λ + 1 = ( 1 a j + 1 − λ + 1, 1 a j + 1 − λ] × ( 1 λ + 2, 1 λ + 1]. (x_{n+\lambda},y_{n+\lambda})\in V_{a_{j+1}-\lambda}\cap H_{\lambda+1}=\left(\frac{1}{a_{j+1}-\lambda+1},\frac{1}{a_{j+1}-\lambda}\right]\times\left(\frac{1}{\lambda+2},\frac{1}{\lambda+1}\right]. |  |

First, suppose λ ≠ a j + 1 − 1 \lambda\neq a_{j+1}-1. Then x n + λ ≤ 1 / 2 x_{n+\lambda}\leq 1/2, so by Equations ( 5.6) and ( 5.7), Θ n + λ ​ ( x) < Θ n + λ + 1 ​ ( x) \Theta_{n+\lambda}(x)<\Theta_{n+\lambda+1}(x) if x n + λ < y n + λ x_{n+\lambda}<y_{n+\lambda}, and similarly with the reverse inequalities. If λ < ⌊ a j + 1 / 2 ⌋ \lambda<\lfloor a_{j+1}/2\rfloor, then λ ≤ a j + 1 / 2 − 1 \lambda\leq a_{j+1}/2-1, which implies that λ + 2 ≤ a j + 1 − λ \lambda+2\leq a_{j+1}-\lambda. Thus in this case

 | x n + λ ≤ 1 a j + 1 − λ ≤ 1 λ + 2 < y n + λ, x_{n+\lambda}\leq\frac{1}{a_{j+1}-\lambda}\leq\frac{1}{\lambda+2}<y_{n+\lambda}, |  |

proving ( 5.8). On the other hand, if ⌈ a j + 1 / 2 ⌉ ≤ λ \lceil a_{j+1}/2\rceil\leq\lambda, then a j + 1 / 2 ≤ λ a_{j+1}/2\leq\lambda. This implies a j + 1 − λ ≤ λ a_{j+1}-\lambda\leq\lambda, so in this case

 | y n + λ ≤ 1 λ + 1 ≤ 1 a j + 1 − λ + 1 < x n + λ, y_{n+\lambda}\leq\frac{1}{\lambda+1}\leq\frac{1}{a_{j+1}-\lambda+1}<x_{n+\lambda}, |  |

proving ( 5.9) for λ < a j + 1 − 1 \lambda<a_{j+1}-1.

If λ = a j + 1 − 1 \lambda=a_{j+1}-1, then since a j + 1 > 1 a_{j+1}>1 by assumption, ( x n + λ, y n + λ) ∈ V 1 \ H 1 (x_{n+\lambda},y_{n+\lambda})\in V_{1}\backslash H_{1}. By Equations ( 5.6) and ( 5.7), Θ n + λ ​ ( x) > Θ n + λ + 1 ​ ( x) \Theta_{n+\lambda}(x)>\Theta_{n+\lambda+1}(x) if and only if 1 − y n + λ > x n + λ ​ y n + λ, 1-y_{n+\lambda}>x_{n+\lambda}y_{n+\lambda}, or, equivalently, y n + λ < 1 / ( 1 + x n + λ) y_{n+\lambda}<1/(1+x_{n+\lambda}), but this inequality holds since x n + λ < 1 x_{n+\lambda}<1 and y n + λ ≤ 1 / 2 y_{n+\lambda}\leq 1/2. Thus ( 5.9) is also true for λ = a j + 1 − 1 \lambda=a_{j+1}-1.

The optimal bounds on Θ ⁡ ( x, p / q) \Theta(x,p/q) follow from these monotonicity statements and the bounds of Corollary 5.11. ∎

As a corollary of the previous result, we find a lower bound on the maximum of the approximation coefficients of rcf -convergents and mediants corresponding to particular partial quotients.

###### Corollary 5.26.

Let x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}, and suppose a j + 1 > 1 a_{j+1}>1 for some fixed j ≥ 0 j\geq 0. Then

 | max { Θ ( x, p / q) | p q ∈ { p j q j } ∪ { λ ​ p j + p j − 1 λ ​ q j + q j − 1 } 0 ≤ λ < a j + 1, p / q ≠ 1 / 0 } > { a j + 1 4, a j + 1 ​ even, a j + 1 2 − 1 4 ​ a j + 1, a j + 1 ​ odd, \max\left\{\Theta\left(x,p/q\right)\ \Big|\ \frac{p}{q}\in\left\{\frac{p_{j}}{q_{j}}\right\}\cup\left\{\frac{\lambda p_{j}+p_{j-1}}{\lambda q_{j}+q_{j-1}}\right\}_{0\leq\lambda<a_{j+1}},\ p/q\neq 1/0\right\}>\begin{cases}\frac{a_{j+1}}{4},&a_{j+1}\ \text{even},\\ \vskip 8.0pt\cr\frac{a_{j+1}^{2}-1}{4a_{j+1}},&a_{j+1}\ \text{odd},\end{cases} |  |

with the lower bound optimal.

###### Proof.

By Theorem 5.25, the maximum occurs when p / q = ( λ ​ p j + p j − 1) / ( λ ​ q j + q j − 1) p/q=(\lambda p_{j}+p_{j-1})/(\lambda q_{j}+q_{j-1}) with λ = ⌊ a j + 1 / 2 ⌋ \lambda=\lfloor a_{j+1}/2\rfloor or λ = ⌈ a j + 1 / 2 ⌉ \lambda=\lceil a_{j+1}/2\rceil. By Corollary 5.11,

(5.10) |  | Θ ⁡ ( x, λ ​ p j + p j − 1 λ ​ q j + q j − 1) > ( a j + 1 − λ) ​ λ a j + 1, \Theta\left(x,\frac{\lambda p_{j}+p_{j-1}}{\lambda q_{j}+q_{j-1}}\right)>\frac{(a_{j+1}-\lambda)\lambda}{a_{j+1}}, |  |

with the lower bound optimal. When a j + 1 a_{j+1} is even, ⌊ a j + 1 / 2 ⌋ = ⌈ a j + 1 / 2 ⌉ = a j + 1 / 2 \lfloor a_{j+1}/2\rfloor=\lceil a_{j+1}/2\rceil=a_{j+1}/2, and for either choice of λ \lambda the right-hand side of ( 5.10) equals a j + 1 / 4 a_{j+1}/4. When a j + 1 a_{j+1} is odd, ⌊ a j + 1 / 2 ⌋ = ( a j + 1 − 1) / 2 \lfloor a_{j+1}/2\rfloor=(a_{j+1}-1)/2 and ⌈ a j + 1 / 2 ⌉ = ( a j + 1 + 1) / 2 \lceil a_{j+1}/2\rceil=(a_{j+1}+1)/2, and for each choice of λ \lambda the right-hand side of ( 5.10) equals ( a j + 1 2 − 1) / 4 ​ a j + 1 (a_{j+1}^{2}-1)/4a_{j+1}. ∎

###### Remark 5.27.

Since the partial quotients of a.e. x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} are unbounded (see, say, Chapter V of [54]), the previous corollary implies that the approximation coefficients of the rcf -convergents and mediants of a.e. x x are unbounded. This is also seen intuitively in Figure 7; when a partial quotient a j + 1 a_{j+1} is large, points in the ℱ \mathcal{F} -orbit of ( x, 1) (x,1) will ‘dip’ close to the origin on the left-hand side of the figure, and, consequently, the coordinates of the corresponding images under ψ R \psi_{R} on the right-hand side become large.

From Figure 7 it is clear that ψ R \psi_{R} is not injective, 13 13 13 The image of the red and blue regions clearly overlap, but ψ R \psi_{R} also ‘folds’ the blue and yellow regions in V 1 ∩ H 2 V_{1}\cap H_{2} over one another. The boundary of ψ R ​ ( V 1 ∩ H 2) \psi_{R}(V_{1}\cap H_{2}) is given by the curves y = 1 − x, y = ( 2 − x) / 4, y=1-x,\ y=(2-x)/4, and y = 1 / 4 ​ x y=1/4x. and thus one cannot immediately conjugate ℱ R \mathcal{F}_{R} with ψ R \psi_{R} to study the dynamics of consecutive Farey convergents as done with consecutive rcf -convergents (§ 5.3.1). The same difficulty arises when studying consecutive convergents of the nearest integer continued fraction map ( [28]). As in [28], this difficulty can be overcome by introducing a third coordinate to the image of the function ψ R \psi_{R} which ‘flags’ the color of the subregion that a point in the domain belongs to. This extra coordinate makes ψ R \psi_{R} invertible and could lead to the study of further metrical results on Farey convergents. We leave the details to future work.

#### 5.3.3. Consecutive rcf -convergents and extreme mediants

Let R = H 1 ∪ H 2 ∪ V 1 R=H_{1}\cup H_{2}\cup V_{1}, which corresponds to rcf -convergents and extreme (i.e., first and final) mediants. For ( x, y) ∈ R (x,y)\in R, we find

 | A [0, r R ​ ( x, y)] ​ ( x) = { A 1 = ( 0 1 1 1), ( x, y) ∈ V 1, A 0 = ( 1 0 1 1), ( x, y) ∈ H 1 \ V 1, A 0 a − 1 = ( 1 0 a − 1 1), ( x, y) ∈ V a ∩ H 2, a > 1; A_{[0,r_{R}(x,y)]}(x)=\begin{cases}A_{1}=\begin{pmatrix}0&1\\ 1&1\end{pmatrix},&(x,y)\in V_{1},\\ A_{0}=\begin{pmatrix}1&0\\ 1&1\end{pmatrix},&(x,y)\in H_{1}\backslash V_{1},\\ A_{0}^{a-1}=\begin{pmatrix}1&0\\ a-1&1\end{pmatrix},&(x,y)\in V_{a}\cap H_{2},\ a>1;\end{cases} |  |

see Figure 8. Define ψ R: R → ℝ 2 \psi_{R}:R\to\mathbb{R}^{2} by

 | ψ R ​ ( x, y) = { 1 x + y − x ​ y ​ ( 1 − y, x ​ y), ( x, y) ∈ V 1, 1 x + y − x ​ y ​ ( 1 − y, 1 − x), ( x, y) ∈ H 1 \ V 1, 1 x + y − x ​ y ​ ( 1 − y, ( 1 − ( a − 1) ​ x) ​ ( 1 + ( a − 2) ​ y)), ( x, y) ∈ V a ∩ H 2, a > 1. \psi_{R}(x,y)=\begin{cases}\frac{1}{x+y-xy}\left(1-y,xy\right),&(x,y)\in V_{1},\\ \frac{1}{x+y-xy}\left(1-y,1-x\right),&(x,y)\in H_{1}\backslash V_{1},\\ \frac{1}{x+y-xy}\left(1-y,(1-(a-1)x)(1+(a-2)y)\right),&(x,y)\in V_{a}\cap H_{2},\ a>1.\end{cases} |  |

By Propositions 5.1 and 5.23, we have for irrational x ∈ ( 0, 1) x\in(0,1),

 | ψ R ​ ( x n R, y n R) = ( Θ n R ​ ( x), Θ n + 1 R ​ ( x)), n ≥ 0. \psi_{R}(x_{n}^{R},y_{n}^{R})=\left(\Theta_{n}^{R}(x),\Theta_{n+1}^{R}(x)\right),\quad n\geq 0. |  |

Figure 8. Left: The region R = H 1 ∪ H 2 ∪ V 1 R=H_{1}\cup H_{2}\cup V_{1} from § 5.3.3. Right: The image ψ R ​ ( R) \psi_{R}(R).

As with Proposition 5.24, the images under ψ R \psi_{R} of subregions of R R yield immediate information regarding consecutive rcf -convergents and extreme mediants. The first statement below—which is also a corollary of Proposition 5.24 and Theorem 5.25 —corresponds to the image of H 1 \ V 1 H_{1}\backslash V_{1}, and the second to the image of H 2 H_{2} (see Figure 8; the latter image is the union of green regions and the region whose boundary is given by the curves y = 1 − x, y = ( 2 − x) / 4, y=1-x,\ y=(2-x)/4, and y = 1 / 4 ​ x y=1/4x). These two images are bounded 14 14 14 As in the proof of Proposition 5.24, these lines are simply upper and lower bounding lines of equal slope and do *not*necessarily describe the boundaries of the images. by the pairs of lines y = x + 1 y=x+1, y = x y=x, and y = x + 1 y=x+1, y = x − 1 y=x-1, respectively.

###### Proposition 5.28.

Let x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}. For any j ≥ 0 j\geq 0 for which a j + 1 > 1 a_{j+1}>1,

 | 0 < Θ ⁡ ( x, p j + p j − 1 q j + q j − 1) − Θ ⁡ ( x, p j − 1 q j − 1) < 1, 0<\Theta\left(x,\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}}\right)-\Theta\left(x,\frac{p_{j-1}}{q_{j-1}}\right)<1, |  |

and

 | | Θ ⁡ ( x, ( a j + 1 − 1) ​ p j + p j − 1 ( a j + 1 − 1) ​ q j + q j − 1) − Θ ⁡ ( x, p j + p j − 1 q j + q j − 1) | < 1. \left|\Theta\left(x,\frac{(a_{j+1}-1)p_{j}+p_{j-1}}{(a_{j+1}-1)q_{j}+q_{j-1}}\right)-\Theta\left(x,\frac{p_{j}+p_{j-1}}{q_{j}+q_{j-1}}\right)\right|<1. |  |

The map ψ R \psi_{R} is again not injective, but a similar process to that of [28] as mentioned in § 5.3.2 may be used to overcome this difficulty and thus investigate further metrical results on rcf -convergents and extreme mediants. We again leave the details to future work.

### 5.4. A generalised Lévy-type theorem

Recall the results ( 5.2) and ( 5.3) due to Lévy on the growth of the denominators of rcf -convergents and on the rate at which these convergents approach their limit x x. Analogues of these results have been proven for a number of continued fraction algorithms and for various subsequences of rcf -convergents and mediants (see, e.g., [27, 31, 40, 7]). Theorem 5.29 below generalises ( 5.2) and ( 5.3) to subsequences of rcf -convergents and mediants determined by proper inducible subregions R R. The results of [27, 31, 40, 7] then follow as special cases.

Recall from ( 3.5) the function

 | j n = j n ​ ( x):= #⁡ { 1 ≤ k ≤ n | ε k ​ ( x) = 1 } j_{n}=j_{n}(x):=\#\{1\leq k\leq n\ |\ \varepsilon_{k}(x)=1\} |  |

which counts the number of times that the F F -orbit of an irrational x ∈ ( 0, 1) x\in(0,1) visits the region ( 1 / 2, 1] (1/2,1] in its first n n steps x, F ⁡ ( x), …, F n − 1 ​ ( x) x,F(x),\dots,F^{n-1}(x). Key to the proof of Theorem 5.29 is the simple observation that the number j n j_{n} may equivalently be thought of as the number of times that the ℱ \mathcal{F} -orbit of ( x, 1) (x,1) visits V 1 ⊂ Ω V_{1}\subset\Omega in its first n n steps:

 | j n = #⁡ { 1 ≤ k ≤ n | ( x k, y k) ∈ V 1 } = ∑ k = 0 n − 1 𝟏 V 1 ​ ( x k, y k). j_{n}=\#\{1\leq k\leq n\ |\ (x_{k},y_{k})\in V_{1}\}=\sum_{k=0}^{n-1}\mathbf{1}_{V_{1}}(x_{k},y_{k}). |  |

###### Theorem 5.29.

For almost every x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q},

1. (i)

lim n → ∞ 1 n ​ log ⁡ s n R = 1 2 ​ h ​ ( ℱ R) \lim_{n\to\infty}\frac{1}{n}\log s_{n}^{R}=\frac{1}{2}h(\mathcal{F}_{R}) and

2. (ii)

lim n → ∞ 1 n ​ log ⁡ | x − u n R s n R | = − h ⁡ ( ℱ R) \lim_{n\to\infty}\frac{1}{n}\log\left|x-\frac{u_{n}^{R}}{s_{n}^{R}}\right|=-h(\mathcal{F}_{R})

for any proper inducible R ⊂ Ω R\subset\Omega, where h ⁡ ( ℱ R) = π 2 6 ​ μ ¯ ​ ( R) h(\mathcal{F}_{R})=\frac{\pi^{2}}{6\bar{\mu}(R)} is the measure-theoretic entropy of ( R, ℬ ∩ R, μ ¯ R, ℱ R) (R,\mathcal{B}\cap R,\bar{\mu}_{R},\mathcal{F}_{R}).

###### Proof.

Let x x belong to the full-measure subset of ( 0, 1) \ ℚ (0,1)\backslash\mathbb{Q} for which Theorem 4.8 and ( 5.2) both hold, and let R ⊂ Ω R\subset\Omega be a proper inducible subregion. Theorem 4.6 gives h ⁡ ( ℱ R) = π 2 6 ​ μ ¯ ​ ( R) h(\mathcal{F}_{R})=\frac{\pi^{2}}{6\bar{\mu}(R)}, and by Theorem 4.8,

(5.11) |  | lim n → ∞ j N n n = lim n → ∞ ∑ k = 0 N n − 1 𝟏 V 1 ​ ( x k, y k) ∑ k = 0 N n − 1 𝟏 R ​ ( x k, y k) = μ ¯ ​ ( V 1) μ ¯ ​ ( R) = log ⁡ 2 μ ¯ ​ ( R), \lim_{n\to\infty}\frac{j_{N_{n}}}{n}=\lim_{n\to\infty}\frac{\sum_{k=0}^{N_{n}-1}\mathbf{1}_{V_{1}}(x_{k},y_{k})}{\sum_{k=0}^{N_{n}-1}\mathbf{1}_{R}(x_{k},y_{k})}=\frac{\bar{\mu}(V_{1})}{\bar{\mu}(R)}=\frac{\log 2}{\bar{\mu}(R)}, |  |

where N n = N n R ​ ( x, 1) N_{n}=N_{n}^{R}(x,1). Now recall from ( 4.9) that s n R = λ N n ​ q j N n + q j N n − 1 s_{n}^{R}=\lambda_{N_{n}}q_{j_{N_{n}}}+q_{j_{N_{n}}-1}, so

(5.12) |  | q j N n − 1 ≤ s n R < q j N n + 1. q_{j_{N_{n}}-1}\leq s_{n}^{R}<q_{j_{N_{n}}+1}. |  |

Taking logarithms and dividing by n n, this gives

 | j N n − 1 n ​ 1 j N n − 1 ​ log ⁡ q j N n − 1 ≤ 1 n ​ log ⁡ s n R < j N n + 1 n ​ 1 j N n + 1 ​ log ⁡ q j N n + 1. \frac{j_{N_{n}}-1}{n}\frac{1}{j_{N_{n}}-1}\log q_{j_{N_{n}}-1}\leq\frac{1}{n}\log s_{n}^{R}<\frac{j_{N_{n}}+1}{n}\frac{1}{j_{N_{n}}+1}\log q_{j_{N_{n}}+1}. |  |

Using Equations ( 5.2) and ( 5.11), the limits as n → ∞ n\to\infty of both the left- and right-hand sides of the previous line equal π 2 12 ​ μ ¯ ​ ( R) \frac{\pi^{2}}{12\bar{\mu}(R)}, proving (i).

For (ii), notice that

 | | x − u n R s n R | = 1 s n R ​ ( s n R ​ x n R + r n R) \left|x-\frac{u_{n}^{R}}{s_{n}^{R}}\right|=\frac{1}{s_{n}^{R}(s_{n}^{R}x_{n}^{R}+r_{n}^{R})} |  |

(see the proof of Proposition 5.1). Since x n R ∈ ( 0, 1) x_{n}^{R}\in(0,1), we have

 | 1 s n R ​ ( s n R + r n R) < | x − u n R s n R | < 1 s n R ​ r n R. \frac{1}{s_{n}^{R}(s_{n}^{R}+r_{n}^{R})}<\left|x-\frac{u_{n}^{R}}{s_{n}^{R}}\right|<\frac{1}{s_{n}^{R}r_{n}^{R}}. |  |

Using ( 5.12), r n R = q j N n r_{n}^{R}=q_{j_{N_{n}}} (see ( 4.9)) and the fact that q j < q j + 1 q_{j}<q_{j+1} for all j j, one obtains from the previous line

 | 1 2 ​ q j N n + 1 2 < | x − u n R s n R | < 1 q j N n − 1 2. \frac{1}{2q_{j_{N_{n}}+1}^{2}}<\left|x-\frac{u_{n}^{R}}{s_{n}^{R}}\right|<\frac{1}{q_{j_{N_{n}}-1}^{2}}. |  |

Taking logarithms and dividing by n n gives

 | q j N n + 1 n ​ 1 q j N n + 1 ​ ( − log ⁡ 2 − 2 ​ log ⁡ q j N n + 1) < 1 n ​ log ⁡ | x − u n R s n R | < q j N n − 1 n ​ 1 q j N n − 1 ​ ( − 2 ​ log ⁡ q j N n − 1). \frac{q_{j_{N_{n}}+1}}{n}\frac{1}{q_{j_{N_{n}}+1}}\left(-\log 2-2\log q_{j_{N_{n}}+1}\right)<\frac{1}{n}\log\left|x-\frac{u_{n}^{R}}{s_{n}^{R}}\right|<\frac{q_{j_{N_{n}}-1}}{n}\frac{1}{q_{j_{N_{n}}-1}}\left(-2\log q_{j_{N_{n}}-1}\right). |  |

Again from Equations ( 5.2) and ( 5.11), the limits as n → ∞ n\to\infty of both the left- and right-hand sides equal − π 2 6 ​ μ ¯ ​ ( R) -\frac{\pi^{2}}{6\bar{\mu}(R)}, proving (ii). ∎

###### Remark 5.30.

As mentioned in Remark 5.3 in the context of limiting distributions of approximation coefficients, the historical precedent has been to study subsequences of rcf -convergents and mediants arranged with increasing denominators, while ( s n R) n ≥ 0 (s_{n}^{R})_{n\geq 0} is not necessarily increasing. Proposition 6.2 in the appendix (§ 6) implies that a number of previously considered analogues of ( 5.2) and ( 5.3) do indeed follow from Theorem 5.29. In particular, setting

 | R = ⋃ λ = 0 Λ H λ + 1 ∪ ⋃ a = 1 A V a R=\bigcup_{\lambda=0}^{\Lambda}H_{\lambda+1}\cup\bigcup_{a=1}^{A}V_{a} |  |

for fixed Λ ≥ 0, A ≥ 1 \Lambda\geq 0,\ A\geq 1, one has μ ¯ ​ ( R) = log ⁡ ( Λ + A + 2) \bar{\mu}(R)=\log(\Lambda+A+2) (see Corollary 5.13). When Λ = A = 1 \Lambda=A=1, Theorem 5.29 (together with Proposition 6.2) gives Propositions 3.1 and 3.3(ii) of [27] and Theorem 2.11 of [31] concerning rcf -convergents and nearest mediants. More generally, for Λ = A ≥ 1 \Lambda=A\geq 1, Theorem 5.29 gives Theorem 4.i and 4.ii of [7] on rcf -convergents and the first Λ \Lambda and final Λ \Lambda mediant convergents.

Now let Q = H 1 \ R Q=H_{1}\backslash R with R ⊂ H 1 R\subset H_{1} a proper inducible subregion, and let S S be the image in Ω \Omega of Q Q under the isomorphism of Theorem 4.1. Then ν ¯ G ​ ( S) = μ ¯ H 1 ​ ( Q) = μ ¯ ​ ( Q) / log ⁡ 2 \bar{\nu}_{G}(S)=\bar{\mu}_{H_{1}}(Q)=\bar{\mu}(Q)/\log 2 and

 | μ ¯ ​ ( R) = μ ¯ ​ ( H 1) − μ ¯ ​ ( Q) = log ⁡ 2 ​ ( 1 − ν ¯ G ​ ( S)). \bar{\mu}(R)=\bar{\mu}(H_{1})-\bar{\mu}(Q)=\log 2(1-\bar{\nu}_{G}(S)). |  |

Thus Theorem 5.29 generalises Corollary 4.15 of [40] on S S -expansions.

## 6. Appendix: Rearranging (sub-)sequences of Farey convergents

Let x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q} with rcf -expansion x = [0; a 1, a 2, …] x=[0;a_{1},a_{2},\dots]. Recall from ( 3.10) that the denominators of the sequence of Farey convergents ( u n / s n) n ≥ 0 (u_{n}/s_{n})_{n\geq 0} of x x are given by

(6.1) |  | ( s n) n ≥ 0 = ( CLOSE \displaystyle(s_{n})_{n\geq 0}=( | q − 1 \displaystyle q_{-1} |  | , q 0 + q − 1 \displaystyle,q_{0}+q_{-1} |  | , …, ( a 1 − 1) q 0 + q − 1, \displaystyle,\dots,(a_{1}-1)q_{0}+q_{-1}, |  |

 |  | q 0 \displaystyle q_{0} |  | , q 1 + q 0 \displaystyle,q_{1}+q_{0} |  | , …, ( a 2 − 1) q 1 + q 0, …, \displaystyle,\dots,(a_{2}-1)q_{1}+q_{0},\dots, |  |

 |  | q j − 1 \displaystyle q_{j-1} |  | , q j + q j − 1 \displaystyle,q_{j}+q_{j-1} |  | , …, ( a j + 1 − 1) q j + q j − 1, …). \displaystyle,\dots,(a_{j+1}-1)q_{j}+q_{j-1},\dots). |  |

Let ρ \rho be the bijection 15 15 15 For a 1 > 1 a_{1}>1 there are in fact two such bijections since s n = s m s_{n}=s_{m} if and only if n = m n=m or (since q − 1 = 0 q_{-1}=0) { n, m } = { 1, a 1 } \{n,m\}=\{1,a_{1}\}. However, in the limits considered below, the choice between these two bijections becomes irrelevant. of non-negative integers for which these denominators are arranged in increasing order:

(6.2) |  | ( s ρ ⁡ ( n)) n ≥ 0 = ( q − 1 CLOSE, \displaystyle(s_{\rho(n)})_{n\geq 0}=(q_{-1}, | q 0 \displaystyle q_{0} |  | , q 0 + q − 1 \displaystyle,q_{0}+q_{-1} |  | , …, ( a 1 − 1) q 0 + q − 1, \displaystyle,\dots,(a_{1}-1)q_{0}+q_{-1}, |  |

 |  | q 1 \displaystyle q_{1} |  | , q 1 + q 0 \displaystyle,q_{1}+q_{0} |  | , …, ( a 2 − 1) q 1 + q 0, …, \displaystyle,\dots,(a_{2}-1)q_{1}+q_{0},\dots, |  |

 |  | q j \displaystyle q_{j} |  | , q j + q j − 1 \displaystyle,q_{j}+q_{j-1} |  | , …, ( a j + 1 − 1) q j + q j − 1, …). \displaystyle,\dots,(a_{j+1}-1)q_{j}+q_{j-1},\dots). |  |

For an inducible subregion R ⊂ Ω R\subset\Omega, let ρ R \rho_{R} be the bijection of non-negative integers which ( u ρ R ​ ( n) R / s ρ R ​ ( n) R) n ≥ 0 (u_{\rho_{R}(n)}^{R}/s_{\rho_{R}(n)}^{R})_{n\geq 0} forms a subsequence of ( u ρ ⁡ ( n) / s ρ ⁡ ( n)) n ≥ 0 (u_{\rho(n)}/s_{\rho(n)})_{n\geq 0}. That is, ρ R \rho_{R} permutes elements of the sequence of ( u n R / s n R) n ≥ 0 (u_{n}^{R}/s_{n}^{R})_{n\geq 0} of Farey convergents determined by R R so as to have increasing denominators. We aim to prove the following two results:

###### Proposition 6.1.

Let R ⊂ Ω R\subset\Omega be a proper inducible subregion and z ∈ [0, ∞) z\in[0,\infty). Then for any x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q},

 | lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ ρ R ​ ( k) R ​ ( x) ≤ z } = lim n → ∞ 1 n ​ #​ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } \lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{\rho_{R}(k)}^{R}(x)\leq z\}=\lim_{n\to\infty}\frac{1}{n}\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\} |  |

when either limit exists.

###### Proposition 6.2.

Let R ⊂ Ω R\subset\Omega be a proper inducible subregion. Then for any x ∈ ( 0, 1) \ ℚ x\in(0,1)\backslash\mathbb{Q},

1. (i)

lim n → ∞ 1 n ​ log ⁡ s ρ R ​ ( n) R = lim n → ∞ 1 n ​ log ⁡ s n R \lim\limits_{n\to\infty}\frac{1}{n}\log s_{\rho_{R}(n)}^{R}=\lim\limits_{n\to\infty}\frac{1}{n}\log s_{n}^{R} and

2. (ii)

lim n → ∞ 1 n ​ log ⁡ | x − u ρ R ​ ( n) R s ρ R ​ ( n) R | = lim n → ∞ 1 n ​ log ⁡ | x − u n R s n R | \lim\limits_{n\to\infty}\frac{1}{n}\log\left|x-\frac{u_{\rho_{R}(n)}^{R}}{s_{\rho_{R}(n)}^{R}}\right|=\lim\limits_{n\to\infty}\frac{1}{n}\log\left|x-\frac{u_{n}^{R}}{s_{n}^{R}}\right|

when any of the limits exist.

To prove these, we need the following:

###### Lemma 6.3.

For any x = [0; a 1, a 2, …] ∈ ( 0, 1) \ ℚ x=[0;a_{1},a_{2},\dots]\in(0,1)\backslash\mathbb{Q}, any inducible R ⊂ Ω R\subset\Omega and any n ≥ 0 n\geq 0, the cardinality of the symmetric difference between the sets { N k } k = 0 n \{N_{k}\}_{k=0}^{n} and { N ρ R ​ ( k) } k = 0 n \{N_{\rho_{R}(k)}\}_{k=0}^{n} is at most two, and | j N ρ R ​ ( n) − j N n | ≤ 1 |j_{N_{\rho_{R}(n)}}-j_{N_{n}}|\leq 1.

###### Proof.

We begin with preliminary notation and observations. Set A 0:= 0 A_{0}:=0 and for j ≥ 1 j\geq 1 set A j:= ∑ k = 1 j a k A_{j}:=\sum_{k=1}^{j}a_{k}. From ( 6.1) and ( 6.2), one finds that ρ \rho fixes A 0 = 0 A_{0}=0 and, for j ≥ 0 j\geq 0, acts as a ‘cyclic permutation’ on subsequent blocks of length a j + 1 a_{j+1}, namely

(6.3) |  | ( A j + 1, A j + 2, …, A j + a j + 1 − 1, A j + 1) ↦ 𝜌 ( A j + 1, A j + 1, A j + 2, …, A j + a j + 1 − 1), (A_{j}+1,A_{j}+2,\dots,A_{j}+a_{j+1}-1,A_{j+1})\xmapsto{\rho}(A_{j+1},A_{j}+1,A_{j}+2,\dots,A_{j}+a_{j+1}-1), |  |

where ρ \rho is applied entry-wise. In particular, for N > 0 N>0 with A j < N ≤ A j + 1 A_{j}<N\leq A_{j+1},

(6.4) |  | ρ ⁡ ( { 0, 1, …, N }) = { 0, 1, …, N − 1 } ∪ { A j + 1 }. \rho(\{0,1,\dots,N\})=\{0,1,\dots,N-1\}\cup\{A_{j+1}\}. |  |

Also observe that since s k R = s N k s_{k}^{R}=s_{N_{k}} and s ρ R ​ ( k) R = s N ρ R ​ ( k) s_{\rho_{R}(k)}^{R}=s_{N_{\rho_{R}(k)}}, the numbers N k N_{k} and N ρ R ​ ( k) N_{\rho_{R}(k)} are the indices of the ( k + 1) st (k+1)^{\text{st}} elements of the set { s n R } n ≥ 0 = { s ρ R ​ ( n) R } n ≥ 0 \{s_{n}^{R}\}_{n\geq 0}=\{s_{\rho_{R}(n)}^{R}\}_{n\geq 0} to appear in the sequences ( s n) n ≥ 0 (s_{n})_{n\geq 0} and ( s ρ ⁡ ( n)) n ≥ 0 (s_{\rho(n)})_{n\geq 0}, respectively.

If n = 0 n=0, then since N 0 = N ρ R ​ ( 0) = 0 N_{0}=N_{\rho_{R}(0)}=0, the statement of the lemma holds. Now fix n > 0 n>0 and let j j be such that A j < N n ≤ A j + 1 A_{j}<N_{n}\leq A_{j+1}. We consider two cases:

1. (i)

If s A j + 1 ∉ { s k R } k ≥ 0 s_{A_{j+1}}\notin\{s_{k}^{R}\}_{k\geq 0}, then ( 6.4) implies that { s N ρ R ​ ( k) } k = 0 n = { s N k } k = 0 n \{s_{N_{\rho_{R}(k)}}\}_{k=0}^{n}=\{s_{N_{k}}\}_{k=0}^{n}, so 16 16 16 Recall that s n = s m s_{n}=s_{m} if and only if n = m n=m or { n, m } = { 1, a 1 } \{n,m\}=\{1,a_{1}\}. Throughout, we consider s 1 s_{1} and s a 1 s_{a_{1}} for a 1 > 1 a_{1}>1 as distinct elements of { s n } n ≥ 0 \{s_{n}\}_{n\geq 0}, even though as integers these both equal q 0 = 1 q_{0}=1. { N k } k = 0 n = { N ρ R ​ ( k) } k = 0 n \{N_{k}\}_{k=0}^{n}=\{N_{\rho_{R}(k)}\}_{k=0}^{n}. Moreover, ( 6.3) implies that N ρ R ​ ( n) = N n N_{\rho_{R}(n)}=N_{n}, and thus the claim holds in this case.

2. (ii)

Suppose s A j + 1 ∈ { s k R } k ≥ 0 s_{A_{j+1}}\in\{s_{k}^{R}\}_{k\geq 0}. Then ( 6.4) gives that { s N ρ R ​ ( k) } k = 0 n = { s N k } k = 0 n − 1 ∪ { s A j + 1 } \{s_{N_{\rho_{R}(k)}}\}_{k=0}^{n}=\{s_{N_{k}}\}_{k=0}^{n-1}\cup\{s_{A_{j+1}}\}. In particular, the symmetric difference between { N k } k = 0 n \{N_{k}\}_{k=0}^{n} and { N ρ R ​ ( k) } k = 0 n \{N_{\rho_{R}(k)}\}_{k=0}^{n} is zero if N n = A j + 1 N_{n}=A_{j+1} and two if N n < A j + 1 N_{n}<A_{j+1}. Moreover, ( 6.3) implies that

 | N ρ R ​ ( n) = { N n − 1 if A j < N n − 1, A j + 1 otherwise. N_{\rho_{R}(n)}=\begin{cases}N_{n-1}&\text{if $A_{j}<N_{n-1}$},\\ A_{j+1}&\text{otherwise}.\end{cases} |  |

If N ρ R ​ ( n) = N n − 1 N_{\rho_{R}(n)}=N_{n-1}, then A j < N n − 1 < N n ≤ A j + 1 A_{j}<N_{n-1}<N_{n}\leq A_{j+1} implies j N ρ R ​ ( n) = j j_{N_{\rho_{R}(n)}}=j, while if N ρ R ​ ( n) = A j + 1 N_{\rho_{R}(n)}=A_{j+1} we have j N ρ R ​ ( n) = j + 1 j_{N_{\rho_{R}(n)}}=j+1. But also A j < N n ≤ A j + 1 A_{j}<N_{n}\leq A_{j+1} implies j N n = j j_{N_{n}}=j or j N n = j + 1 j_{N_{n}}=j+1 (with the latter occurring if and only if N n = A j + 1 N_{n}=A_{j+1}). Thus | j N ρ R ​ ( n) − j N n | ≤ 1. |j_{N_{\rho_{R}(n)}}-j_{N_{n}}|\leq 1.

∎

Propositions 6.1 and 6.2 now follow almost immediately from Lemma 6.3:

###### Proof of Proposition 6.1.

By definition (see ( 4.9) and ( 5.4)), Θ ρ R ​ ( k) R ​ ( x) = Θ ⁡ ( x, u N ρ R ​ ( k) / s N ρ R ​ ( k)) \Theta_{\rho_{R}(k)}^{R}(x)=\Theta(x,u_{N_{\rho_{R}(k)}}/s_{N_{\rho_{R}(k)}}) and Θ k R ​ ( x) = Θ ⁡ ( x, u N k / s N k) \Theta_{k}^{R}(x)=\Theta(x,u_{N_{k}}/s_{N_{k}}), so Lemma 6.3 implies that for any n > 0 n>0,

 | | #⁡ { 0 ≤ k < n | Θ ρ R ​ ( k) R ​ ( x) ≤ z } − #⁡ { 0 ≤ k < n | Θ k R ​ ( x) ≤ z } | ≤ 2. \left|\#\{0\leq k<n\ |\ \Theta_{\rho_{R}(k)}^{R}(x)\leq z\}-\#\{0\leq k<n\ |\ \Theta_{k}^{R}(x)\leq z\}\right|\leq 2. |  |

Dividing by n n and taking n → ∞ n\to\infty gives the result. ∎

###### Proof of Proposition 6.2.

By Lemma 6.3,

 | lim n → ∞ j N ρ R ​ ( n) n = lim n → ∞ j N n n \lim_{n\to\infty}\frac{j_{N_{\rho_{R}(n)}}}{n}=\lim_{n\to\infty}\frac{j_{N_{n}}}{n} |  |

whenever either limit exists. After equation ( 5.11), the proof of Theorem 5.29 goes through with each of s n R, r n R, x n R s_{n}^{R},\ r_{n}^{R},\ x_{n}^{R} and N n N_{n} replaced by s ρ R ​ ( n) R, r ρ R ​ ( n) R, x ρ R ​ ( n) R s_{\rho_{R}(n)}^{R},\ r_{\rho_{R}(n)}^{R},\ x_{\rho_{R}(n)}^{R} and N ρ R ​ ( n) N_{\rho_{R}(n)}, respectively. ∎

## References

- [1] A. Abrams, S. Katok, and I. Ugarcovici (2023) On the topological entropy of ( a, b) (a,b) -continued fraction transformations. Nonlinearity 36 ( 5), pp. 2894–2908. External Links: ISSN 0951-7715, [Document][7], [Link][8], [MathReview Entry][9] Cited by: §1.
- [2] D. Barbolosi and H. Jager (1994) On a theorem of Legendre in the theory of continued fractions. J. Théor. Nombres Bordeaux 6 ( 1), pp. 81–94. Cited by: §5.2, §5.2, Corollary 5.18, Corollary 5.19, Corollary 5.20.
- [3] J. Barrionuevo, R. M. Burton, K. Dajani, and C. Kraaikamp (1996) Ergodic properties of generalized Lüroth series. Acta Arith. 74 ( 4), pp. 311–327. External Links: ISSN 0065-1036, [Document][10], [Link][11], [MathReview (Wieb Bosma)][12] Cited by: §1.
- [4] J. Blom (1992) Metrical properties of best approximants. J. Austral. Math. Soc. Ser. A 53 ( 1), pp. 78–91. External Links: ISSN 0263-6115, [MathReview (G. Ramharter)][13] Cited by: §1.
- [5] W. Bosma, H. Jager, and F. Wiedijk (1983) Some metrical observations on the approximation by continued fractions. Nederl. Akad. Wetensch. Indag. Math. 45 ( 3), pp. 281–299. Cited by: §5.1, §5.1, Corollary 5.4, §5.
- [6] W. Bosma (1990) Approximation by mediants. Math. Comp. 54 ( 189), pp. 421–434. External Links: ISSN 0025-5718, [Document][14], [Link][15], [MathReview (G. Ramharter)][16] Cited by: §1, §1, §5.1, §5.1, §5.1, §5.1, §5.1, §5.1, §5.1, Corollary 5.11, Corollary 5.6, Corollary 5.8, Corollary 5.9.
- [7] G. Brown and Q. Yin (1996) Metrical theory for Farey continued fractions. Osaka J. Math. 33 ( 4), pp. 951–970. External Links: ISSN 0030-6126, [Link][17], [MathReview (Wieb Bosma)][18] Cited by: §1, §1, §4.1, §4.2, §4.2, Theorem 4.1, Remark 4.3, Theorem 4.7, §5.1, §5.1, §5.4, Corollary 5.13, Remark 5.30, Remark 5.5.
- [8] R. M. Burton, C. Kraaikamp, and T. A. Schmidt (2000) Natural extensions for the Rosen fractions. Trans. Amer. Math. Soc. 352 ( 3), pp. 1277–1298. External Links: ISSN 0002-9947, [Document][19], [Link][20], [MathReview (Thomas Ward)][21] Cited by: §1.
- [9] K. Calta, C. Kraaikamp, and T. A. Schmidt (2020) Synchronization is full measure for all α \alpha -deformations of an infinite class of continued fractions. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 20 ( 3), pp. 951–1008. External Links: ISSN 0391-173X, [MathReview (Niels Langeveld)][22] Cited by: §1.
- [10] C. Carminati, N. Langeveld, and W. Steiner (2021) Tanaka-Ito α \alpha -continued fractions and matching. Nonlinearity 34 ( 6), pp. 3565–3582. External Links: ISSN 0951-7715, [Document][23], [Link][24], [MathReview (Qinglong Zhou)][25] Cited by: §1.
- [11] K. Dajani, C. Kraaikamp, and B. Solomyak (1996) The natural extension of the β \beta -transformation. Acta Math. Hungar. 73 ( 1-2), pp. 97–109. External Links: ISSN 0236-5294, [Document][26], [Link][27], [MathReview (Meir Smorodinsky)][28] Cited by: §1.
- [12] K. Dajani and C. Kalle (2021) A first course in ergodic theory. CRC Press, Boca Raton, FL. Cited by: §2.2.
- [13] K. Dajani and C. Kraaikamp (1996) On approximation by Lüroth series. J. Théor. Nombres Bordeaux 8 ( 2), pp. 331–346. External Links: ISSN 1246-7405, [Link][29], [MathReview (Wieb Bosma)][30] Cited by: §1.
- [14] K. Dajani and C. Kraaikamp (2000) “The mother of all continued fractions”. Colloq. Math. 84/85 ( part 1), pp. 109–123. Note: Dedicated to the memory of Anzelm Iwanik External Links: ISSN 0010-1354, [Document][31], [Link][32], [MathReview (Anne Broise-Alamichel)][33] Cited by: §1, §2.4, §2.4, §3.1, §3.2.
- [15] K. Dajani and C. Kraaikamp (2002) Ergodic theory of numbers. Carus Mathematical Monographs, Vol. 29, Mathematical Association of America, Washington, DC. External Links: ISBN 0-88385-034-6, [MathReview (Thomas Ward)][34] Cited by: §1, §2.2, §2.2, §5.
- [16] K. Dajani and C. Kraaikamp (2002) From greedy to lazy expansions and their driving dynamics. Expo. Math. 20 ( 4), pp. 315–327. External Links: ISSN 0723-0869, [Document][35], [Link][36], [MathReview (Reinhard Winkler)][37] Cited by: §1.
- [17] H. E. Daniels (1962) Processes generating permutation expansions. Biometrika 49, pp. 139–149. Cited by: §2.3.
- [18] J. de Jonge and C. Kraaikamp (2018) Natural extensions for Nakada’s α \alpha -expansions: descending from 1 to g 2 g^{2}. J. Number Theory 183, pp. 172–212. External Links: ISSN 0022-314X, [Document][38], [Link][39], [MathReview (Zhenliang Zhang)][40] Cited by: §1.
- [19] Desmos. Note: [https://www.desmos.com][41] Accessed: 2023-12-14 Cited by: §5.1.
- [20] P. Fatou (1904) Sur l’approximation des incommensurables et les séries trigonométriques. C. R. Acad. Sci. Paris 139, pp. 1019–1021. Cited by: Theorem 5.15.
- [21] P. Gerl (1971) Relative Gleichverteilung in lokalkompakten Räumen. II. Monatsh. Math. 75, pp. 410–422. External Links: ISSN 0026-9255,1436-5081, [Document][42], [Link][43], [MathReview (J. E. Cigler)][44] Cited by: footnote 9.
- [22] P. Gerl (1971) Relative Gleichverteilung in lokalkompakten Räumen. Math. Z. 121, pp. 24–50. External Links: ISSN 0025-5874,1432-1823, [Document][45], [Link][46], [MathReview (J. E. Cigler)][47] Cited by: footnote 9.
- [23] J. H. Grace (1918) The classification of rational approximations. Proc. London Math. Soc. (2) 17, pp. 247–258. Cited by: Theorem 5.15.
- [24] M. Iosifescu and C. Kraaikamp (2002) Metrical theory of continued fractions. Kluwer Academic Publishers, Dordrecht. Note: Math. Appl., 547 External Links: ISBN 1-4020-0892-9 Cited by: §2.2, §5.
- [25] M. Iosifescu and C. Kraaikamp (2008) Metric properties of Denjoy’s canonical continued fraction expansion. Tokyo J. Math. 31 ( 2), pp. 495–510. External Links: ISSN 0387-3870, [Document][48], [Link][49], [MathReview (Carlo Carminati)][50] Cited by: §1, §5.1, §5.1.
- [26] M. Iosifescu and G. I. Sebe (2008) On the metrical theory of a peculiar continued fraction expansion. Rev. Roumaine Math. Pures Appl. 53 ( 5-6), pp. 465–477. Cited by: §3.1.
- [27] S. Ito (1989) Algorithms with mediant convergents and their metrical theory. Osaka J. Math. 26 ( 3), pp. 557–578. External Links: ISSN 0030-6126, [Link][51], [MathReview (F. Schweiger)][52] Cited by: §1, §1, §2.3, §2.3, §2.4, §3.1, §3.2, §3.2, §3.2, §4, §4, §5.1, §5.1, §5.4, Proposition 5.1, Remark 5.30, Abstract., footnote 5.
- [28] H. Jager and C. Kraaikamp (1989) On the approximation by continued fractions. Nederl. Akad. Wetensch. Indag. Math. 51 ( 3), pp. 289–307. Cited by: §5.3.1, §5.3.2, §5.3.3, §5.3, §5.
- [29] H. Jager (1986) Continued fractions and ergodic theory, transcendental numbers and related topics. RIMS Kokyuroko 599 ( 1), pp. 55–59. Cited by: §4.2, §5.3.1, §5.3, §5.3.
- [30] H. Jager (1986) The distribution of certain sequences connected with the continued fraction. Nederl. Akad. Wetensch. Indag. Math. 48 ( 1), pp. 61–69. Cited by: §5.3.1, §5.3, §5.3.
- [31] H. Jager (1991) Some metrical observations on the approximation of an irrational number by its nearest mediants. Period. Math. Hungar. 23 ( 1), pp. 5–16. Cited by: §1, §1, §5.1, §5.1, §5.4, Remark 5.30.
- [32] S. Katok and I. Ugarcovici (2010) Structure of attractors for ( a, b) (a,b) -continued fraction transformations. J. Mod. Dyn. 4 ( 4), pp. 637–691. External Links: ISSN 1930-5311, [Document][53], [Link][54], [MathReview (Ilya D. Shkredov)][55] Cited by: §1.
- [33] S. Katok and I. Ugarcovici (2010) Theory of ( a, b) (a,b) -continued fraction transformations and applications. Electron. Res. Announc. Math. Sci. 17, pp. 20–33. External Links: [Document][56], [Link][57], [MathReview (Carlo Carminati)][58] Cited by: §1.
- [34] S. Katok and I. Ugarcovici (2012) Applications of ( a, b) (a,b) -continued fraction transformations. Ergodic Theory Dynam. Systems 32 ( 2), pp. 755–777. External Links: ISSN 0143-3857, [Document][59], [Link][60], [MathReview (Carlo Carminati)][61] Cited by: §1.
- [35] A. Ya. Khinchin (1997) Continued fractions. Dover Publications, Inc., Mineola, NY. Note: With a preface by B. V. Gnedenko. Translated from the third (1961) Russian edition. Reprint of the 1964 translation External Links: ISBN 0-486-69630-8, [MathReview Entry][62] Cited by: §5.2.
- [36] D. E. Knuth (1984) The distribution of continued fraction approximations. J. Number Theory 19 ( 3), pp. 443–448. External Links: ISSN 0022-314X,1096-1658, [Document][63], [Link][64], [MathReview (John H. Loxton)][65] Cited by: §5.
- [37] J. F. Koksma (1937) Bewijs van een stelling over kettingbreuken. Mathematica A 6, pp. 226–231. Cited by: Theorem 5.15, Theorem 5.16.
- [38] C. Kraaikamp, H. Nakada, and T. A. Schmidt (2009) Metric and arithmetic properties of mediant-Rosen maps. Acta Arith. 137 ( 4), pp. 295–324. External Links: ISSN 0065-1036, [Document][66], [Link][67], [MathReview (Radhakrishnan Nair)][68] Cited by: §1.
- [39] C. Kraaikamp (1990) On the approximation by continued fractions. ii. Indag. Math. 1 ( 1), pp. 63–75. Cited by: §5.3.1, §5.3.
- [40] C. Kraaikamp (1991) A new class of continued fraction expansions. Acta Arith. 57 ( 1), pp. 1–39. External Links: ISSN 0065-1036, [Document][69], [Link][70], [MathReview (F. Schweiger)][71] Cited by: §1, §5.3, §5.4, Remark 5.30.
- [41] C. Kraaikamp, T. A. Schmidt, and I. Smeets (2007) Tong’s spectrum for Rosen continued fractions. J. Théor. Nombres Bordeaux 19 ( 3), pp. 641–661. External Links: ISSN 1246-7405, [Link][72], [MathReview (Karma Dajani)][73] Cited by: §1.
- [42] C. Kraaikamp, T. A. Schmidt, and I. Smeets (2010) Natural extensions for α \alpha -Rosen continued fractions. J. Math. Soc. Japan 62 ( 2), pp. 649–671. External Links: ISSN 0025-5645, [Link][74], [MathReview (Radhakrishnan Nair)][75] Cited by: §1.
- [43] L. Kuipers and B. Meulenbeld (1952) Some properties of continued fractions. Acta Math. 87, pp. 1–12. Cited by: §5.2, Corollary 5.22.
- [44] A. M. Legendre (1798) Essai sur la théorie des nombres. Paris, Duprat, an VI. Cited by: Theorem 5.14.
- [45] J. Lehner (1994) Semiregular continued fractions whose partial denominators are 1 or 2. In The mathematical legacy of Wilhelm Magnus: groups, geometry and special functions (Brooklyn, NY, 1992), Contemp. Math., Vol. 169, pp. 407–410. Cited by: §2.4, §2.4, §3.1.
- [46] P. Lévy (1936) Sur le développement en fraction continue d’un nombre choisi au hasard. Compositio Math. 3, pp. 286–303. External Links: ISSN 0010-437X,1570-5846, [Link][76], [MathReview Entry][77] Cited by: §5.
- [47] L. Luzzi and S. Marmi (2008) On the entropy of Japanese continued fractions. Discrete Contin. Dyn. Syst. 20 ( 3), pp. 673–711. External Links: ISSN 1078-0947, [Document][78], [Link][79], [MathReview (Anne Broise-Alamichel)][80] Cited by: §1.
- [48] H. Nakada, S. Ito, and S. Tanaka (1977) On the invariant measure for the transformations associated with some real continued-fractions. Keio Engineering Reports 30 ( 13), pp. 159–175. Cited by: §1, §2.2.
- [49] H. Nakada and W. Steiner (2021) On the ergodic theory of Tanaka-Ito type α \alpha -continued fractions. Tokyo J. Math. 44 ( 2), pp. 451–465. External Links: ISSN 0387-3870, [Document][81], [Link][82], [MathReview (Chunyun Cao)][83] Cited by: §1.
- [50] H. Nakada (1981) Metrical theory for a class of continued fraction transformations and their natural extensions. Tokyo J. Math. 4 ( 2), pp. 399–426. External Links: ISSN 0387-3870, [Document][84], [Link][85], [MathReview (F. Schweiger)][86] Cited by: §1, §2.2.
- [51] H. Nakada (2010) On the Lenstra constant associated to the Rosen continued fractions. J. Eur. Math. Soc. (JEMS) 12 ( 1), pp. 55–70. External Links: ISSN 1435-9855,1435-9863, [Document][87], [Link][88], [MathReview (Thomas Ward)][89] Cited by: Remark 5.5.
- [52] W. Parry (1962) Ergodic properties of some permutation processes. Biometrika 49, pp. 151–154. Cited by: §2.3.
- [53] O. Perron (1954) Die Lehre von den Kettenbrüchen. Bd I. Elementare Kettenbrüche.. B. G. Teubner Verlagsgesellschaft, Stuttgart. Note: 3te Aufl. Cited by: §2.1.
- [54] A. M. Rockett and P. Szüsz (1992) Continued fractions. World Scientific Publishing Co., Inc., River Edge, NJ. Cited by: Remark 5.27, §5, footnote 2.
- [55] J. C. Tong (1983) The conjugate property of the Borel theorem on Diophantine approximation. Math. Z. 184 ( 2), pp. 151–153. External Links: ISSN 0025-5874,1432-1823, [Document][90], [Link][91], [MathReview Entry][92] Cited by: §5.
- [56] K. Th. Vahlen (1895) Ueber Näherungswerthe und Kettenbrüche. J. Reine Angew. Math. 115, pp. 221–233. External Links: ISSN 0075-4102,1435-5345, [Document][93], [Link][94], [MathReview Entry][95] Cited by: §5.3.1.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:k.dajani@uu.nl
[4]: mailto:c.kraaikamp@tudelft.nl
[5]: mailto:slade.sanderson@irif.fr
[6]: https://www.desmos.com/calculator/pnsu8hcytq
[7]: https://dx.doi.org/10.1088/1361-6544/acc6b2
[8]: https://doi-org.tudelft.idm.oclc.org/10.1088/1361-6544/acc6b2
[9]: https://www.ams.org/mathscinet-getitem?mr=4580666
[10]: https://dx.doi.org/10.4064/aa-74-4-311-327
[11]: https://doi-org.tudelft.idm.oclc.org/10.4064/aa-74-4-311-327
[12]: https://www.ams.org/mathscinet-getitem?mr=1378226
[13]: https://www.ams.org/mathscinet-getitem?mr=1164778
[14]: https://dx.doi.org/10.2307/2008703
[15]: https://doi-org.tudelft.idm.oclc.org/10.2307/2008703
[16]: https://www.ams.org/mathscinet-getitem?mr=995207
[17]: http://projecteuclid.org.tudelft.idm.oclc.org/euclid.ojm/1200787226
[18]: https://www.ams.org/mathscinet-getitem?mr=1435463
[19]: https://dx.doi.org/10.1090/S0002-9947-99-02442-3
[20]: https://doi-org.tudelft.idm.oclc.org/10.1090/S0002-9947-99-02442-3
[21]: https://www.ams.org/mathscinet-getitem?mr=1650073
[22]: https://www.ams.org/mathscinet-getitem?mr=4166798
[23]: https://dx.doi.org/10.1088/1361-6544/abef75
[24]: https://doi-org.tudelft.idm.oclc.org/10.1088/1361-6544/abef75
[25]: https://www.ams.org/mathscinet-getitem?mr=4281424
[26]: https://dx.doi.org/10.1007/BF00058946
[27]: https://doi-org.tudelft.idm.oclc.org/10.1007/BF00058946
[28]: https://www.ams.org/mathscinet-getitem?mr=1415923
[29]: http://jtnb.cedram.org/item?id=JTNB_1996__8_2_331_0
[30]: https://www.ams.org/mathscinet-getitem?mr=1438473
[31]: https://dx.doi.org/10.4064/cm-84/85-1-109-123
[32]: https://doi-org.tudelft.idm.oclc.org/10.4064/cm-84/85-1-109-123
[33]: https://www.ams.org/mathscinet-getitem?mr=1778844
[34]: https://www.ams.org/mathscinet-getitem?mr=1917322
[35]: https://dx.doi.org/10.1016/S0723-0869%2802%2980010-X
[36]: https://doi-org.tudelft.idm.oclc.org/10.1016/S0723-0869(02)80010-X
[37]: https://www.ams.org/mathscinet-getitem?mr=1940010
[38]: https://dx.doi.org/10.1016/j.jnt.2017.07.012
[39]: https://doi-org.tudelft.idm.oclc.org/10.1016/j.jnt.2017.07.012
[40]: https://www.ams.org/mathscinet-getitem?mr=3715233
[41]: https://www.desmos.com
[42]: https://dx.doi.org/10.1007/BF01297010
[43]: https://doi.org/10.1007/BF01297010
[44]: https://www.ams.org/mathscinet-getitem?mr=306143
[45]: https://dx.doi.org/10.1007/BF01110364
[46]: https://doi.org/10.1007/BF01110364
[47]: https://www.ams.org/mathscinet-getitem?mr=298376
[48]: https://dx.doi.org/10.3836/tjm/1233844066
[49]: https://doi-org.tudelft.idm.oclc.org/10.3836/tjm/1233844066
[50]: https://www.ams.org/mathscinet-getitem?mr=2477886
[51]: http://projecteuclid.org.tudelft.idm.oclc.org/euclid.ojm/1200781697
[52]: https://www.ams.org/mathscinet-getitem?mr=1021431
[53]: https://dx.doi.org/10.3934/jmd.2010.4.637
[54]: https://doi-org.tudelft.idm.oclc.org/10.3934/jmd.2010.4.637
[55]: https://www.ams.org/mathscinet-getitem?mr=2753948
[56]: https://dx.doi.org/10.3934/era.2010.17.20
[57]: https://doi-org.tudelft.idm.oclc.org/10.3934/era.2010.17.20
[58]: https://www.ams.org/mathscinet-getitem?mr=2644834
[59]: https://dx.doi.org/10.1017/S0143385711000460
[60]: https://doi-org.tudelft.idm.oclc.org/10.1017/S0143385711000460
[61]: https://www.ams.org/mathscinet-getitem?mr=2901369
[62]: https://www.ams.org/mathscinet-getitem?mr=1451873
[63]: https://dx.doi.org/10.1016/0022-314X%2884%2990083-0
[64]: https://doi.org/10.1016/0022-314X(84)90083-0
[65]: https://www.ams.org/mathscinet-getitem?mr=769794
[66]: https://dx.doi.org/10.4064/aa137-4-1
[67]: https://doi-org.tudelft.idm.oclc.org/10.4064/aa137-4-1
[68]: https://www.ams.org/mathscinet-getitem?mr=2506585
[69]: https://dx.doi.org/10.4064/aa-57-1-1-39
[70]: https://doi-org.tudelft.idm.oclc.org/10.4064/aa-57-1-1-39
[71]: https://www.ams.org/mathscinet-getitem?mr=1093246
[72]: http://jtnb.cedram.org/item?id=JTNB_2007__19_3_641_0
[73]: https://www.ams.org/mathscinet-getitem?mr=2388792
[74]: http://projecteuclid.org.tudelft.idm.oclc.org/euclid.jmsj/1273236716
[75]: https://www.ams.org/mathscinet-getitem?mr=2662856
[76]: http://www.numdam.org/item?id=CM_1936__3__286_0
[77]: https://www.ams.org/mathscinet-getitem?mr=1556945
[78]: https://dx.doi.org/10.3934/dcds.2008.20.673
[79]: https://doi-org.tudelft.idm.oclc.org/10.3934/dcds.2008.20.673
[80]: https://www.ams.org/mathscinet-getitem?mr=2373210
[81]: https://dx.doi.org/10.3836/tjm/1502179343
[82]: https://doi-org.tudelft.idm.oclc.org/10.3836/tjm/1502179343
[83]: https://www.ams.org/mathscinet-getitem?mr=4379737
[84]: https://dx.doi.org/10.3836/tjm/1270215165
[85]: https://doi-org.tudelft.idm.oclc.org/10.3836/tjm/1270215165
[86]: https://www.ams.org/mathscinet-getitem?mr=646050
[87]: https://dx.doi.org/10.4171/JEMS/189
[88]: https://doi.org/10.4171/JEMS/189
[89]: https://www.ams.org/mathscinet-getitem?mr=2578603
[90]: https://dx.doi.org/10.1007/BF01252854
[91]: https://doi.org/10.1007/BF01252854
[92]: https://www.ams.org/mathscinet-getitem?mr=716268
[93]: https://dx.doi.org/10.1515/crll.1895.115.221
[94]: https://doi.org/10.1515/crll.1895.115.221
[95]: https://www.ams.org/mathscinet-getitem?mr=1580401
