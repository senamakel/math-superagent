<!-- source: https://arxiv.org/html/1907.02148 | converted from HTML -->

An Algorithm to Find Rational Points on Elliptic Curves Related to the Concordant Form Problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1907.02148v1 [math.AG] 03 Jul 2019

# An Algorithm to Find Rational Points on Elliptic Curves Related to the Concordant Form Problem

Hagen Knaf Erich Selder Karlheinz Spindler

Abstract We derive an efficient algorithm to find solutions to Euler’s concordant form problem and rational points on elliptic curves associated with this problem.

Keywords algorithmic number theory, elliptic curves, concordant forms

AMS Subject Classification 11Y16, 11G05, 14H52

 |  |  |

## 1 Introduction

It is well known that the determination of the Mordell-Weil group of an elliptic curve is a difficult problem. Apart from the torsion subgroup, which can be calculated rather easily using the Lutz-Nagell-Theorem ([11], [16], cf. [20], [21]) and for which very good general information is given by Mazur’s Theorem (cf. [12]), obtaining information on the rational points of a rationally defined elliptic curve is hard. Even if the elliptic curve is explicitly given, both the calculation of the rank of the Mordell-Weil group and the determination of explicit solutions (generators of this group) are difficult problems. A famous example due to Zagier (cf. [25]; also see [9], p.5, Fig. 1.3), which illustrates the problems, is the task of explicitly showing that n = 157 n=157 is a congruent number by determining the sides of a rational triangle with area 157 157, which consist of fractions with more than 25 25 decimal places in both the numerator and the denominator. As a byproduct of these calculations one easily obtains nontrivial rational solutions of the equation y 2 = x ⁡ ( x − 157) ​ ( x + 157) y^{2}=x(x-157)(x+157), the smallest of which is given by

 | x \displaystyle x | = \displaystyle\hskip-4.2679pt=\hskip-4.2679pt | − 166136231668185267540804 / 2825630694251145858025, \displaystyle-166136231668185267540804/2825630694251145858025, |  |

 | y \displaystyle y | = \displaystyle\hskip-4.2679pt=\hskip-4.2679pt | 167661624456834335404812111469782006 / 150201095200135518108761470235125. \displaystyle 167661624456834335404812111469782006/150201095200135518108761470235125. |  |

An even more exciting example was discovered by Bremner and Cassels in [1] who considered the family of curves with equations y 2 = x ⁡ ( x 2 + p) y^{2}=x(x^{2}+p) with prime numbers p ≡ 5 p\equiv 5 (mod 8 8). In the introduction to this paper the authors mention an observation of S. Lang which asserts that in the tables of elliptic curves and generators of the Mordell-Weil group known at that time (around 1982) the numerator and the denominator of the x x -value of smallest nontrivial solutions to elliptic curve equations with integral coefficients are never much greater than the square of the discriminant. Note that the above example of Zagier exemplifies this observation, since the discriminant of the example is △ = 16 ⋅ 157 6 = 239617149303184 \triangle=16\cdot 157^{6}=239617149303184.

The most spectacular example calculated in [1] (see also [20], Chap. X, §6, Remark 6.3) is given by the prime number p = 877 p=877. The generator of the infinite part of the Mordell-Weil group in this example is given by

 | x = 375494528127162193105504069942092792346201 62159877768644257535639389356838044100 x=\frac{375494528127162193105504069942092792346201}{62159877768644257535639389356838044100} |  |

and

 | y = 256256267988926809388776834045513089648669153204356603464786949 490078023219787588959802933995928925096061616470779979261000 y=\frac{256256267988926809388776834045513089648669153204356603464786949}{490078023219787588959802933995928925096061616470779979261000} |  |

so that both the numerator and the denominator of x x are greater than Δ 4 \Delta^{4}, thus providing a clear counterexample to Lang’s observation.

In this paper we present an algorithm which enables us to calculate a large number of examples of smallest solutions to certain classes of elliptic curve equations. Many of the explicitly computed examples belonging to classes of elliptic curves other than those of the paper of Bremner and Cassels (namely those corresponding to Euler’s concordant forms) also contradict Lang’s assertion. We are not interested in general discussions on the determination of the rank of the Mordell-Weil group, but focus on finding explicit solutions. So in general we assume the given elliptic curves to have positive Mordell-Weil-rank. The method for finding solutions is a simple search loop of quadratic complexity, but the key point is the reduction of the equations to be considered to simpler ones by some technical tricks.

The first (and most important) reduction is a well-known descent procedure in which the original elliptic curve E E is substituted by a homogeneous space Q Q over E E. The equations defining this homogeneous space can be simplified by Newton’s method of parametrizing a quadric by means of a projection from a fixed point onto that quadric. These two concepts already enable us to formulate a simple algorithm, allowing us to find explicit solutions for a large class of curves.

The core of our approach is an improvement of the above algorithm which makes it possible to obtain solutions of twice the complexity as compared to the simpler algorithm. This improvement is achieved by invoking a technical condition which is satisfied in many situations.

The potential of this improved algorithm will be illustrated by some series of examples. For example, this algorithm can be used to find the smallest nontrivial integers A, B, C, D A,B,C,D satisfying the two equations A 2 − 373 ​ B 2 = C 2 A^{2}-373B^{2}=C^{2} and A 2 + 373 ​ B 2 = D 2 A^{2}+373B^{2}=D^{2}, which are found to be

 | A \displaystyle A | = \displaystyle\hskip 0.0pt=\hskip 0.0pt | 6464736286838262275566375140640125524476830394378258160144359151221846588162921 \displaystyle 6464736286838262275566375140640125524476830394378258160144359151221846588162921 |  |

 | B \displaystyle B | = \displaystyle\hskip 0.0pt=\hskip 0.0pt | 214402886988423616335778394508029972671920911384749815755228436417174376951980 \displaystyle 214402886988423616335778394508029972671920911384749815755228436417174376951980 |  |

 | C \displaystyle C | = \displaystyle\hskip 0.0pt=\hskip 0.0pt | 4964526988887992094202607668810309975770378526931158358479760499172740751760929 \displaystyle 4964526988887992094202607668810309975770378526931158358479760499172740751760929 |  |

 | D \displaystyle D | = \displaystyle\hskip 0.0pt=\hskip 0.0pt | 7677180621382399924131415436519959747090354653821331133153517438341892919535729 \displaystyle 7677180621382399924131415436519959747090354653821331133153517438341892919535729 |  |

and have up to 79 79 decimals. (The existence of such a solution shows explicitly that 373 373 is a congruent number.) Based on an analysis of the examples to be presented later in the paper, it may be possible to gain some insight into the behaviour of the solutions depending on the input parameters of the given elliptic curves, but many open questions remain. We see our contribution mainly in providing a tool which allows one to systematically find rational points on certain classes of elliptic curves.

The paper is organized as follows. After this introduction we present some preparatory material on elliptic curves and quadratic forms. The most important part of this section will be the description of the abstract descent procedure and its concrete realization for our purposes. In a subsequent section we illustrate this descent procedure by some examples, some of which will be taken up again in the series of examples discussed at the end of the paper. Subsequently, we describe our algorithm in detail. In particular, we point out the critical choices to be made during the execution of the algorithm and the conditions which are necessary to make it work. A further section contains some series of examples showing the power of the algorithm. Finally, we close with a critical discussion of the algorithm, examine consequences of the examples generated by the algorithm and give an outlook to further questions to be pursued.

## 2 General background

### 2.1 Elliptic curves

#### 2.1.1 General notions

Throughout this paper we consider most of our geometric objects to be defined over the field ℚ \mathbb{Q} of rational numbers. Sometimes we argue geometrically and regard the objects to be defined over an algebraic closure ℚ ¯ \overline{\mathbb{Q}} or over some number field.

An elliptic curve defined over ℚ \mathbb{Q} is a plane projective curve E E whose affine part is given by a Weierstraß equation of the form y 2 = P ⁡ ( x) y^{2}=P(x) where P ∈ ℚ ⁡ [x] P\in\mathbb{Q}[x] is a polynomial of degree 3 3 with nonzero discriminant. Note that such a curve always has a single smooth point at infinity which is defined over ℚ \mathbb{Q}. The geometric points of E E carry the structure of an algebraic group, the group law being given by Newton’s well-known secant and tangent construction. We fix the structure such that the point at infinity is the neutral element of this group law. The group law restricts to the set E ⁡ ( ℚ) E(\mathbb{Q}) of rational points on E E, the so-called Mordell-Weil group of the elliptic curve E E. By the important theorem of Mordell and Weil (cf. [13], [22]) this group is a finitely generated abelian group, hence is isomorphic (as an abstract group) to ℤ r × T \mathbb{Z}^{r}\times T where r = rank ​ ( E ​ ( ℚ)) r=\hbox{rank}(E(\mathbb{Q})) is the rank of E ⁡ ( ℚ) E(\mathbb{Q}) and T T is a torsion group, i. e., a finite abelian group.

If E E is explicitly given then it is relatively easy to compute the torsion part of the Mordell-Weil group by the theorem of Lutz-Nagell. Moreover, the famous theorem of Mazur tells us that there are only very few possibilities for a finite abelian group to occur as the torsion subgroup of the Mordell-Weil group of an elliptic curve. In fact, T T is either isomorphic to ℤ / n ​ ℤ \mathbb{Z}/n\mathbb{Z} where 1 ≤ n ≤ 12 1\leq n\leq 12, n ≠ 11 n\neq 11, or else is isomorphic to ℤ / 2 ​ ℤ × ℤ / 2 ​ n ​ ℤ \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2n\mathbb{Z} where 1 ≤ n ≤ 4 1\leq n\leq 4.

In contrast to the torsion part, the determination of the rank of the Mordell-Weil group is a much deeper problem. Moreover, it is very difficult to find non-torsion solutions even if one knows in advance that the rank is positive, i. e., that there exist infinitely many rational points on E E. This is due to the fact that even if the coefficients of the elliptic curve are small (measured for example in terms of a naive notion of height in projective space) the smallest non-torsion point on E E may be very large.

#### 2.1.2 Elliptic curves corresponding to concordant forms

In the sequel we will deal with elliptic curves E E defined over the rationals with torsion subgroup containing ℤ / 2 ​ ℤ × ℤ / 2 ​ ℤ \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}. This is equivalent to saying that E E is defined by an affine equation of the form y 2 = ( x − e 1) ​ ( x − e 2) ​ ( x − e 3) y^{2}=(x-e_{1})(x-e_{2})(x-e_{3}) with pairwise different rational numbers e 1, e 2, e 3 ∈ ℚ e_{1},e_{2},e_{3}\in\mathbb{Q}. We denote this elliptic curve by E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. By simple rational transformations we can clear denominators and translate the x x -coordinates such that the equation becomes y 2 = x ⁡ ( x + M) ​ ( x + N) y^{2}=x(x+M)(x+N) with different nonzero integers M, N ∈ ℤ M,N\in\mathbb{Z}; we denote this curve by E M, N E_{M,N}. (In projective notation we use homogeneous coordinates ( T, X, Y) (T,X,Y) and write the points of the affine part of E M, N E_{M,N} as ( x, y) = ( X / T, Y / T) (x,y)=(X/T,Y/T).) In this form the elliptic curve correponds to Euler’s concordant form problem (cf. [3], [17]), which is the problem of finding nontrivial integral solutions of the system of two quadratic equations X 0 2 + M ​ X 1 2 = X 2 2 X_{0}^{2}+MX_{1}^{2}=X_{2}^{2} and X 0 2 + N ​ X 1 2 = X 3 2 X_{0}^{2}+NX_{1}^{2}=X_{3}^{2}. (See [2], Ch. 8, for the representation of elliptic curves as intersections of quadrics.) The intersection of these two quadrics in projective three-space ℙ 3 ​ ( ℚ ¯) \mathbb{P}^{3}(\overline{\mathbb{Q}}) will be denoted by Q M, N Q_{M,N}. For future reference, let us fix the notations

(1)

 | E M, N \displaystyle E_{M,N} | = { ( T: X: Y) ∈ ℙ 2 ( ℚ ¯) ∣ T Y 2 = X ( X + T M) ( X + T N) }, \displaystyle=\{(T:X:Y)\in\mathbb{P}^{2}(\mathbb{\overline{Q}})\mid TY^{2}=X(X\!+\!TM)(X\!+\!TN)\}, |  |

 | Q M, N \displaystyle Q_{M,N} | = { ( X 0: X 1: X 2: X 3) ∈ ℙ 3 ( ℚ ¯) ∣ X 0 2 + M X 1 2 = X 2 2, X 0 2 + N X 1 2 = X 3 2 }. \displaystyle=\{(X_{0}:X_{1}:X_{2}:X_{3})\in\mathbb{P}^{3}(\mathbb{\overline{Q}})\mid X_{0}^{2}\!+\!MX_{1}^{2}=X_{2}^{2},\ X_{0}^{2}\!+\!NX_{1}^{2}=X_{3}^{2}\}. |  |

We note that Q M, N Q_{M,N} defines an abstract elliptic curve (i.e., a smooth projective curve of arithmetic genus one) which is isomorphic to the curve E M, N E_{M,N}. In fact, the mappings F: Q M, N → E M, N F:Q_{M,N}\rightarrow E_{M,N} given by

 | F ⁡ ( X 0 X 1 X 2 X 3) = ( N ​ X 2 − M ​ X 3 + ( M − N) ​ X 0 M ​ N ​ ( X 3 − X 2) M ​ N ​ ( M − N) ​ X 1) F\left(\begin{array}[]{c}X_{0}\\ X_{1}\\ X_{2}\\ X_{3}\end{array}\right)=\left(\begin{array}[]{c}NX_{2}-MX_{3}+(M-N)X_{0}\\ MN(X_{3}-X_{2})\\ MN(M-N)X_{1}\end{array}\right) |  | ( 2) |

and G: E M, N → Q M, N G:E_{M,N}\rightarrow Q_{M,N} given by

 | G ⁡ ( T X Y) = ( − ( X + M ​ T) ​ ( Y 2 − M ​ ( X + N ​ T) 2) 2 ​ Y ​ ( X + N ​ T) ​ ( X + M ​ T) − ( X + M ​ T) ​ ( Y 2 + M ​ ( X + N ​ T) 2) − ( X + N ​ T) ​ ( Y 2 + N ​ ( X + M ​ T) 2)) G\left(\begin{array}[]{c}T\\ X\\ Y\end{array}\right)=\left(\begin{array}[]{c}-(X+MT)(Y^{2}-M(X+NT)^{2})\\ 2Y(X+NT)(X+MT)\\ -(X+MT)(Y^{2}+M(X+NT)^{2})\\ -(X+NT)(Y^{2}+N(X+MT)^{2})\end{array}\right) |  | ( 3) |

extend to completely defined biregular mappings which are mutually inverse; cf. [19]. Note that for the equation of E M, N E_{M,N} we may assume that M > 0 M>0 and N < 0 N<0 after a trivial change of variables. Furthermore, we may write M = p ​ k M=pk and − N = q ​ k -N=qk with coprime natural numbers p, q ∈ ℕ p,q\in\mathbb{N} and a squarefree natural number k ∈ ℕ k\in\mathbb{N}. In this form the equation is closely related to the θ \theta -congruent number problem in the sense of Fujiwara (cf. [4]; see also [7], [24]).

Note that the two-torsion points ( 0,0) (0,0), ( − M ​,0) (-M,0), ( − N ​,0) (-N,0) together with the point at infinity on E M, N E_{M,N} correspond to the trivial solutions ( 1,0, ± 1, ± 1) (1,0,\pm 1,\pm 1) of the concordant form equations and to the trivial solution (the degenerated triangle) of the θ \theta -congruent number problem. Let us point out that by Mazur’s Theorem the only further torsion points could be either 4 4 - or 8 8 -torsion points or else 3 3 - or 6 6 -torsion points. Moreover, these additional torsion points can occur only in very rare cases. In fact, in the form E p ​ k, − q ​ k E_{pk,-qk} of the elliptic curve such torsion points can only occur when k = 1,2,3 k=1,2,3 or 6 6 (cf. [5], [19]). Since the torsion points can be calculated easily we will ignore them in the subsequent considerations in which we develop methods for finding non-torsion points on elliptic curves of the considered form.

### 2.2 Quadratic Forms

In the following sections we frequently consider ternary quadratic forms, in most cases of a rather special form. We will collect some facts about these forms needed later. The quadratic forms which occur in the following considerations are of the form F ⁡ ( X 0, X 1, X 2) = a 00 ​ X 0 2 + a 01 ​ X 0 ​ X 1 + a 11 ​ X 1 2 + a 22 ​ X 2 2 F(X_{0},X_{1},X_{2})=a_{00}X_{0}^{2}+a_{01}X_{0}X_{1}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2} with coprime integer coefficients a i ​ j ∈ ℤ a_{ij}\in\mathbb{Z}. In most cases the forms are already in diagonal form (i.e., a 01 = 0 a_{01}=0) or are transformed to diagonal form in the course of our investigations.

#### 2.2.1 Solvability criterion

Let F ⁡ ( X 0, X 1, X 2) = a 00 ​ X 0 2 + a 11 ​ X 1 2 + a 22 ​ X 2 2 F(X_{0},X_{1},X_{2})=a_{00}X_{0}^{2}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2} be a ternary diagonal form with integer coefficients. Then by standard techniques we can transform this equation into one for which the product a 00 ​ a 11 ​ a 22 a_{00}a_{11}a_{22} is squarefree (equivalently, such that the three coefficients are squarefree and pairwise coprime). The following criterion for the existence of a nonzero integer solution ( x 0, x 1, x 2) ∈ ℤ 3 (x_{0},x_{1},x_{2})\in\mathbb{Z}^{3} dates back to Legendre (cf. [10]).

Legendre Criterion: The equation a 00 ​ X 0 2 + a 11 ​ X 1 2 + a 22 ​ X 2 2 = 0 a_{00}X_{0}^{2}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2}=0 has a nonzero solution if and only if not all the coefficients have the same sign (which is equivalent to saying that there is a solution over the real numbers) and, in addition, for all permutations ( i, j, k) (i,j,k) of ( 0,1,2) (0,1,2) the number − a i ​ i ​ a j ​ j -a_{ii}a_{jj} is a quadratic residue modulo a k ​ k a_{kk}.

With this criterion one can easily check whether or not a given ternary quadratic form has a nontrivial solution. In addition, by the work of Holzer and his followers (cf. [6], [14], [23]) there are algorithms to find explicit solutions which terminate with a complexity which is known a priori depending on the coefficients. (Incidentally, Holzer’s Theorem occurs both as a tool within our algorithm and as a model for our overall approach, namely, to produce explicit solutions to certain types of equations in which the mere existence of solutions is known by other, more abstract, methods.)

Holzer’s Theorem: If F ⁡ ( X 0, X 1, X 2) = a 00 ​ X 0 2 + a 11 ​ X 1 2 + a 22 ​ X 2 2 F(X_{0},X_{1},X_{2})=a_{00}X_{0}^{2}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2} is a quadratic form with pairwise coprime and squarefree coefficients such that the equation F ⁡ ( X 0, X 1, X 2) = 0 F(X_{0},X_{1},X_{2})=0 has a nontrivial solution, then there exists such a solution ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) satisfying the inequalities | x 0 | < | a 11 ​ a 22 | |x_{0}|<\sqrt{|a_{11}a_{22}|}, | x 1 | < | a 00 ​ a 22 | |x_{1}|<\sqrt{|a_{00}a_{22}|} and | x 2 | < | a 00 ​ a 11 | |x_{2}|<\sqrt{|a_{00}a_{11}|}.

#### 2.2.2 Parametrization of quadratic forms

In the sequel we will make use of the fact that there is a systematic approach to finding all solutions of a quadratic form, provided one fixed solution is known. The technique is a well-known construction, dating back to Newton, which geometrically uses the fact that any line through the fixed point has a uniquely determined second point of intersection with the quadric, whose coordinates are rational expressions in the coefficients of the given quadric and the coordinates of the fixed point, where the slope of the line serves as a parameter. We summarize the calculations, writing down the parametrization using projective coordinates.

Lemma: Consider the projective quadric Q = { ( x 0, x 1, x 2) ∈ ℙ 2 | F ( X 0, X 1, X 2) Q=\{(x_{0},x_{1},x_{2})\in\mathbb{P}^{2}\,|\,F(X_{0},X_{1},X_{2}) = 0 } =0\} where F ⁡ ( X 0, X 1, X 2) = a 00 ​ X 0 2 + a 01 ​ X 0 ​ X 1 + a 11 ​ X 1 2 + a 22 ​ X 2 2 F(X_{0},X_{1},X_{2})=a_{00}X_{0}^{2}+a_{01}X_{0}X_{1}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2}. The set of all points ( x 0, x 1, x 2) ∈ Q (x_{0},x_{1},x_{2})\in Q with x 2 ≠ 0 x_{2}\not=0 can be parametrized by the rational mapping Φ: ℙ 1 → Q \varPhi:\mathbb{P}^{1}\rightarrow Q given by Φ ⁡ ( ξ 0, ξ 1) = ( φ 0 ​ ( ξ 0, ξ 1), φ 1 ​ ( ξ 0, ξ 1), φ 2 ​ ( ξ 0, ξ 1)) \varPhi(\xi_{0},\xi_{1})=(\varphi_{0}(\xi_{0},\xi_{1}),\varphi_{1}(\xi_{0},\xi_{1}),\varphi_{2}(\xi_{0},\xi_{1})) where

(4a)

 |  | X 0 \displaystyle X_{0}\  |  | = φ 0 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{0}(\xi_{0},\xi_{1})\  |  | = a 11 ​ x 0 ​ ξ 0 2 − 2 ​ a 11 ​ x 1 ​ ξ 0 ​ ξ 1 − ( a 01 ​ x 1 + a 00 ​ x 0) ​ ξ 1 2, \displaystyle=\ a_{11}x_{0}\xi_{0}^{2}-2a_{11}x_{1}\xi_{0}\xi_{1}-(a_{01}x_{1}+a_{00}x_{0})\xi_{1}^{2}, |  |

 |  | X 1 \displaystyle X_{1}\  |  | = φ 1 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{1}(\xi_{0},\xi_{1})\  |  | = ( − a 11 ​ x 1 − a 01 ​ x 0) ​ ξ 0 2 − 2 ​ a 00 ​ x 0 ​ ξ 0 ​ ξ 1 + a 00 ​ x 1 ​ ξ 1 2, \displaystyle=\ (-a_{11}x_{1}-a_{01}x_{0})\xi_{0}^{2}-2a_{00}x_{0}\xi_{0}\xi_{1}+a_{00}x_{1}\xi_{1}^{2}, |  |

 |  | X 2 \displaystyle X_{2}\  |  | = φ 2 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{2}(\xi_{0},\xi_{1})\  |  | = a 11 ​ x 2 ​ ξ 0 2 + a 01 ​ x 2 ​ ξ 0 ​ ξ 1 + a 00 ​ x 2 ​ ξ 1 2. \displaystyle=\ a_{11}x_{2}\xi_{0}^{2}+a_{01}x_{2}\xi_{0}\xi_{1}+a_{00}x_{2}\xi_{1}^{2}. |  |

whereas if x 2 = 0 x_{2}=0 and x 1 ≠ 0 x_{1}\not=0 the following parametrization can be used:

(4b)

 |  | X 0 \displaystyle X_{0}\  |  | = φ 0 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{0}(\xi_{0},\xi_{1})\  |  | = − ( a 01 ​ x 1 + a 00 ​ x 0) ​ ξ 0 2 + a 22 ​ x 0 ​ ξ 1 2, \displaystyle=\ -(a_{01}x_{1}+a_{00}x_{0})\xi_{0}^{2}+a_{22}x_{0}\xi_{1}^{2}, |  |

 |  | X 1 \displaystyle X_{1}\  |  | = φ 1 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{1}(\xi_{0},\xi_{1})\  |  | = a 00 ​ x 1 ​ ξ 0 2 + a 22 ​ x 1 ​ ξ 1 2, \displaystyle=\ a_{00}x_{1}\xi_{0}^{2}+a_{22}x_{1}\xi_{1}^{2}, |  |

 |  | X 2 \displaystyle X_{2}\  |  | = φ 2 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{2}(\xi_{0},\xi_{1})\  |  | = − ( a 01 ​ x 1 + 2 ​ a 00 ​ x 0) ​ ξ 0 ​ ξ 1. \displaystyle=\ -(a_{01}x_{1}+2a_{00}x_{0})\xi_{0}\xi_{1}. |  |

The proof is an elementary and simple calculation, which we omit.

Remark: We did not specify a base field over which the projective spaces and all the coordinates are defined, since the lemma is valid for any field. We will apply this lemma in the situation that the quadric is defined over the rational numbers; i.e., the coefficients a 00, a 01, a 11, a 22 a_{00},a_{01},a_{11},a_{22} as well as the coordinates of the fixed point ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) and the parameters ( ξ 0, ξ 1) (\xi_{0},\xi_{1}) are rational numbers. In this situation we can always assume that all these data are, in fact, integers such that the coefficients a 00, a 01, a 11, a 22 a_{00},a_{01},a_{11},a_{22} are coprime, the coordinates x 0, x 1, x 2 x_{0},x_{1},x_{2} are coprime and the parameters ξ 0, ξ 1 \xi_{0},\xi_{1} are coprime.

#### 2.2.3 Pairs of quadrics with separated variables

In the situation of the following discussion we will sometimes be given two quadrics in projective three-space of a special form in which the variables of the quadrics will be separated in some sense. More precisely, the quadrics Q 1 Q_{1} and Q 2 Q_{2} will have equations of the form

(5)

 |  | Q 1: \displaystyle Q_{1}: |  | a 00 ​ X 0 2 + a 01 ​ X 0 ​ X 1 + a 11 ​ X 1 2 + a 22 ​ X 2 2 \displaystyle\quad a_{00}X_{0}^{2}+a_{01}X_{0}X_{1}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2}\  |  | = 0, \displaystyle=\ 0, |  |

 |  | Q 2: \displaystyle Q_{2}: |  | b 00 ​ X 0 2 + b 01 ​ X 0 ​ X 1 + b 11 ​ X 1 2 + b 33 ​ X 3 2 \displaystyle\quad b_{00}X_{0}^{2}+b_{01}X_{0}X_{1}+b_{11}X_{1}^{2}+b_{33}X_{3}^{2}\  |  | = 0 \displaystyle=\ 0 |  |

so that the equations for the quadrics share two of the four variables such that the other two variables occur only as squares. We always assume the quadrics to have rational solutions, so by means of a fixed point ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) on Q 1 Q_{1} we can parametrize the points on the first quadric Q 1 Q_{1}, viewed as a quadric in the projective plane with coordinates ( X 0, X 1, X 2) (X_{0},X_{1},X_{2}), and we can substitute the parametrizations for the common variables X 0, X 1 X_{0},X_{1} into the second quadric, thus yielding a function of the variables ξ 0, ξ 1, X 3 \xi_{0},\xi_{1},X_{3} which is of degree 4 4 in the parameter variables ξ 0, ξ 1 \xi_{0},\xi_{1} and of pure degree 2 2 in the third variable X 3 X_{3}. Let us summarize the result of the calculations.

Lemma: Let Q 1, Q 2 Q_{1},Q_{2} be two quadratic forms as above, let ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) be a point on Q 1 Q_{1} and let

(6)

 |  | X 0 \displaystyle X_{0}\  |  | = φ 0 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{0}(\xi_{0},\xi_{1})\  |  | = α 00 ​ ξ 0 2 + α 01 ​ ξ 0 ​ ξ 1 + α 11 ​ ξ 1 2 \displaystyle=\ \alpha_{00}\xi_{0}^{2}+\alpha_{01}\xi_{0}\xi_{1}+\alpha_{11}\xi_{1}^{2} |  |

 |  | X 1 \displaystyle X_{1}\  |  | = φ 1 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{1}(\xi_{0},\xi_{1})\  |  | = β 00 ​ ξ 0 2 + β 01 ​ ξ 0 ​ ξ 1 + β 11 ​ ξ 1 2 \displaystyle=\ \beta_{00}\xi_{0}^{2}+\beta_{01}\xi_{0}\xi_{1}+\beta_{11}\xi_{1}^{2} |  |

 |  | X 2 \displaystyle X_{2}\  |  | = φ 2 ​ ( ξ 0, ξ 1) \displaystyle=\ \varphi_{2}(\xi_{0},\xi_{1})\  |  | = γ 00 ​ ξ 0 2 + γ 01 ​ ξ 0 ​ ξ 1 + γ 11 ​ ξ 1 2 \displaystyle=\ \gamma_{00}\xi_{0}^{2}+\gamma_{01}\xi_{0}\xi_{1}+\gamma_{11}\xi_{1}^{2} |  |

be the parametrization of Q 1 Q_{1} projecting from ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}). Then the substitution of φ 0 \varphi_{0} and φ 1 \varphi_{1} into the quadric Q 2 Q_{2} gives the equation

 | Q 2: B 40 ξ 0 4 + B 31 ξ 0 3 ξ 1 + B 22 ξ 0 2 ξ 1 2 + B 13 ξ 0 ξ 1 3 + B 04 ξ 1 4 + b 33 X 3 2 Q_{2}:\quad B_{40}\xi_{0}^{4}+B_{31}\xi_{0}^{3}\xi_{1}+B_{22}\xi_{0}^{2}\xi_{1}^{2}+B_{13}\xi_{0}\xi_{1}^{3}+B_{04}\xi_{1}^{4}+b_{33}X_{3}^{2} |  | ( 7) |

where

(8)

 |  | B 40 \displaystyle B_{40} |  | = b 00 ​ α 00 2 + b 01 ​ α 00 ​ β 00 + b 11 ​ β 00 2 \displaystyle=b_{00}\alpha_{00}^{2}+b_{01}\alpha_{00}\beta_{00}+b_{11}\beta_{00}^{2} |  |

 |  | B 31 \displaystyle B_{31} |  | = 2 ​ b 00 ​ α 00 ​ α 01 + b 01 ​ ( α 00 ​ β 01 + α 01 ​ β 00) + 2 ​ b 11 ​ β 00 ​ β 01 \displaystyle=2b_{00}\alpha_{00}\alpha_{01}+b_{01}(\alpha_{00}\beta_{01}\!+\!\alpha_{01}\beta_{00})+2b_{11}\beta_{00}\beta_{01} |  |

 |  | B 22 \displaystyle B_{22} |  | = b 00 ​ ( 2 ​ α 00 ​ α 11 + α 01 2) + b 01 ​ ( α 00 ​ β 11 + α 01 ​ β 01 + α 11 ​ β 00) + b 11 ​ ( 2 ​ β 00 ​ β 11 + β 01 2) \displaystyle=b_{00}(2\alpha_{00}\alpha_{11}\!+\!\alpha_{01}^{2})+b_{01}(\alpha_{00}\beta_{11}\!+\!\alpha_{01}\beta_{01}+\alpha_{11}\beta_{00})+b_{11}(2\beta_{00}\beta_{11}\!+\!\beta_{01}^{2}) |  |

 |  | B 13 \displaystyle B_{13} |  | = 2 ​ b 00 ​ α 01 ​ α 11 + b 01 ​ ( α 01 ​ β 11 + α 11 ​ β 01) + 2 ​ b 11 ​ β 01 ​ β 11 \displaystyle=2b_{00}\alpha_{01}\alpha_{11}+b_{01}(\alpha_{01}\beta_{11}\!+\!\alpha_{11}\beta_{01})+2b_{11}\beta_{01}\beta_{11} |  |

 |  | B 04 \displaystyle B_{04} |  | = b 00 ​ α 11 2 + b 01 ​ α 11 ​ β 11 + b 11 ​ β 11 2 \displaystyle=b_{00}\alpha_{11}^{2}+b_{01}\alpha_{11}\beta_{11}+b_{11}\beta_{11}^{2} |  |

Again, the proof is just an easy calculation and is omitted.

Corollary: If the two quadrics Q 1 Q_{1} and Q 2 Q_{2} are diagonal (i.e., if a 01 = b 01 = 0 a_{01}=b_{01}=0) and if one of the coordinates x 0 x_{0} or x 1 x_{1} of the fixed point is zero, then the substituted form of Q 2 Q_{2} is biquadratic in ( ξ 0, ξ 1) (\xi_{0},\xi_{1}).

In fact, in this situation we have α 00 = α 11 = β 01 = 0 \alpha_{00}=\alpha_{11}=\beta_{01}=0 if x 0 = 0 x_{0}=0 or else α 01 = β 00 = β 11 = 0 \alpha_{01}=\beta_{00}=\beta_{11}=0 if x 1 = 0 x_{1}=0. In both cases the two coefficients B 31 B_{31} and B 13 B_{13} vanish.

### 2.3 Two-descent

#### 2.3.1 General theory

We are interested in explicitly finding rational points on the elliptic curves E e 1, e 2, e 3 = { ( x, y) ∈ ℚ 2 ∣ y 2 = ( x − e 1) ​ ( x − e 2) ​ ( x − e 3) } E_{e_{1},e_{2},e_{3}}=\{(x,y)\in\mathbb{Q}^{2}\mid y^{2}=(x-e_{1})(x-e_{2})(x-e_{3})\} as defined in 2.1.2. We may restrict our considerations to the case that the numbers e i e_{i} are integers. According to Silverman (cf. [20], Chap. X, Remark 3.4) the *existence*of rational points may be checked by deciding whether certain homogeneous spaces over E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} are trivial in the sense of [20], Chap. X, §3, Prop. 3.3. But these homogeneous spaces are also useful for calculating rational points explicitly. Since for our purposes we do not make use of the important homological criteria for the existence of solutions (local-global principle, Selmer group, Tate-Shafarevich group etc.), we only recall the principal facts on the determination of homogeneous spaces belonging to rational points on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. Here we may restrict our attention to the isogeny given by the multiplication-by- 2 2 -map on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. We use the notations of [20] (see Chap. X, Section 1 and Example 4.5.1). The same calculations can be found in [8] (see Chap. IV, Section 3).

First we observe that any element of ℚ ∗ / ( ℚ ∗) 2 \mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2} can be uniquely represented by a squarefree integer. Any pair ( b 1, b 2) ∈ ℚ ∗ / ( ℚ ∗) 2 × ℚ ∗ / ( ℚ ∗) 2 (b_{1},b_{2})\in\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2}\times\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2} defines the intersection of two quadrics Q e 1, e 2, e 3, b 1, b 2 = Q 1 ∩ Q 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}}=Q_{1}\cap Q_{2} in projective three-space by

(9)

 |  | Q 1: \displaystyle Q_{1}: |  | b 1 ​ X 1 2 − b 2 ​ X 2 2 + ( e 1 − e 2) ​ X 0 2 \displaystyle\quad b_{1}X_{1}^{2}-b_{2}X_{2}^{2}+(e_{1}-e_{2})X_{0}^{2} |  | = 0, \displaystyle=\ 0, |  |

 |  | Q 2: \displaystyle Q_{2}: |  | b 1 ​ X 1 2 − b 1 ​ b 2 ​ X 3 2 + ( e 1 − e 3) ​ X 0 2 \displaystyle\quad b_{1}X_{1}^{2}-b_{1}b_{2}X_{3}^{2}+(e_{1}-e_{3})X_{0}^{2}\  |  | = 0. \displaystyle=\ 0. |  |

(Cf. [20], Chap. X, Section 1.) This intersection defines an abstract elliptic curve which in general does not have any rational point, but which is a twist of the given curve; i.e., it becomes isomorphic to E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} over an algebraic closure ℚ ¯ \overline{\mathbb{Q}}. This curve defines a homogeneous space over E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}, hence an element in the Weil-Chatelet group W ​ C ​ ( E e 1, e 2, e 3, ℚ) WC(E_{e_{1},e_{2},e_{3}},\mathbb{Q}). More precisely, since the above construction stems from the multiplication by 2 2 on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}, it defines an element of the 2-torsion part of W ​ C ​ ( E e 1, e 2, e 3, ℚ) WC(E_{e_{1},e_{2},e_{3}},\mathbb{Q}) (cf. [20], Ex. 4.5.1).

The assignment ( x 0, x 1, x 2, x 3) ↦ ( ( b 1 ​ x 1 2 / x 0 2) + e 1, b 1 ​ b 2 ​ x 1 ​ x 2 ​ x 3 / x 0 3) (x_{0},x_{1},x_{2},x_{3})\mapsto\bigl((b_{1}x_{1}^{2}/x_{0}^{2})+e_{1},\,b_{1}b_{2}x_{1}x_{2}x_{3}/x_{0}^{3}\bigr) extends to a well-defined regular mapping Q e 1, e 2, e 3, b 1, b 2 → E e 1, e 2, e 3 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}}\rightarrow E_{e_{1},e_{2},e_{3}} of degree 4. In particular, if ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}) is a rational point on the homogeneous space Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}}, one gets a rational point on the given curve. Note that the logarithmic height of the point ( b 1 ​ x 1 2 / x 0 2 + e 1, b 1 ​ b 2 ​ x 1 ​ x 2 ​ x 3 / x 0 3) (b_{1}x_{1}^{2}/x_{0}^{2}+e_{1},b_{1}b_{2}x_{1}x_{2}x_{3}/x_{0}^{3}) on E e 1 ​ e 2 ​ e 3 E_{e_{1}e_{2}e_{3}} is about three times the height of the point ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}) on Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}}. (Recall that the logarithmic height of a point P ∈ ℙ N ​ ( ℚ) P\in{\mathbb{P}}^{N}(\mathbb{Q}) is the logarithm of max ⁡ ( | x 0 |, …, | x N |) \max(|x_{0}|,\ldots,|x_{N}|) where P = ( x 0: x 1: ⋯: x N) P=(x_{0}:x_{1}:\cdots:x_{N}) is represented with coprime integers x i x_{i}.) This explains why it is reasonable to look for points on Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}} instead of finding rational points on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} directly. The problem is to determine the approriate homogeneous spaces which have rational points. The most important approach to this question is contained in the following two-descent procedure (cf. [20], Chap. X, Prop. 1.4; [8], Chap. IV, Section 3).

Let S S be the set of integers consisting of − 1 -1, 2 2 and all the divisors of the discriminant of E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. Let ℚ ⁡ ( S ​,2) \mathbb{Q}(S,2) be the subgroup of ℚ ∗ / ( ℚ ∗) 2 \mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2} generated by the elements of S S. Thus any element in ℚ ⁡ ( S ​,2) \mathbb{Q}(S,2) has a unique representation by an integer which is squarefree and which has prime factors only in S S. Let us consider the mappings φ i: E e 1, e 2, e 3 ​ ( ℚ) / 2 ​ E e 1, e 2, e 3 ​ ( ℚ) → ℚ ⁡ ( S ​,2) \varphi_{i}:E_{e_{1},e_{2},e_{3}}(\mathbb{Q})/2E_{e_{1},e_{2},e_{3}}(\mathbb{Q})\rightarrow\mathbb{Q}(S,2) defined by

 | φ i ​ ( P):= { x − e i if ​ P = ( x, y) ​ with ​ x ≠ e i; ( e i − e j) ​ ( e i − e k) if ​ P = ( e i ​,0) ​ where ​ { i, j, k } = { 1,2,3 }; 1 if ​ P = ∞. \varphi_{i}(P):=\begin{cases}x-e_{i}&\hbox{if}\ P=(x,y)\ \hbox{with}\ x\neq e_{i};\\ (e_{i}-e_{j})(e_{i}-e_{k})&\hbox{if}\ P=(e_{i},0)\ \hbox{where}\ \{i,j,k\}=\{1,2,3\};\\ 1&\hbox{if}\ P=\infty.\end{cases} |  | ( 10) |

Here the values are taken as representatives modulo ( ℚ ∗) 2 (\mathbb{Q}^{*})^{2}. Then φ i \varphi_{i} is well-defined and a homomorphism of groups. Furthermore, the homomorphism

 | φ: E e 1, e 2, e 3 ​ ( ℚ) / 2 ​ E e 1, e 2, e 3 ​ ( ℚ) → ℚ ⁡ ( S ​,2) × ℚ ⁡ ( S ​,2) P ↦ ( φ 1 ​ ( P), φ 2 ​ ( P)) \varphi:\begin{matrix}E_{e_{1},e_{2},e_{3}}(\mathbb{Q})/2E_{e_{1},e_{2},e_{3}}(\mathbb{Q})&\rightarrow&\mathbb{Q}(S,2)\times\mathbb{Q}(S,2)\\ P&\mapsto&\bigl(\varphi_{1}(P),\varphi_{2}(P)\bigr)\end{matrix} |  | ( 11) |

is injective (see [8], Prop. 4.8, or [20], Chap. X, Prop. 1.4).

Consequence: The homogeneous spaces Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}} which contain a rational point (and hence are trivial in the sense of [20], Chap. X, Section 3) are exactly those for which ( b 1, b 2) (b_{1},b_{2}) is contained in the image of the mapping φ \varphi. Since ℚ ⁡ ( S ​,2) × ℚ ⁡ ( S ​,2) \mathbb{Q}(S,2)\times\mathbb{Q}(S,2) is finite, we therefore have to check only a finite number of homogeneous spaces for the existence of a rational point.

Remark: If the curve is given in the Weierstraß form for E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}, the two-descent procedure (and thus the meaning of the mapping φ \varphi) can be explained in a very elementary way. The affine part of E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} is given by the equation y 2 = ( x − e 1) ​ ( x − e 2) ​ ( x − e 3) y^{2}=(x-e_{1})(x-e_{2})(x-e_{3}). If p = ( x, y) ∈ ℚ 2 p=(x,y)\in\mathbb{Q}^{2} is a point on E e 1, e 2, e 3 ​ ( ℚ) E_{e_{1},e_{2},e_{3}}(\mathbb{Q}) such that all three factors ( x − e i) (x-e_{i}) are rational squares, then p = [2] ⋅ q p=[2]\cdot q for some rational point q ∈ E e 1, e 2, e 3 ​ ( ℚ) q\in E_{e_{1},e_{2},e_{3}}(\mathbb{Q}), where [2] [2] denotes the multiplication-by-two map on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. This halving procedure stops after a finite number of steps (because E e 1, e 2, e 3 ​ ( ℚ) E_{e_{1},e_{2},e_{3}}(\mathbb{Q}) is finitely generated), yielding a point p ∈ E e 1, e 2, e 3 ​ ( ℚ) p\in E_{e_{1},e_{2},e_{3}}(\mathbb{Q}) which is not twice another rational point on E e 1, e 2, e 3 ​ ( ℚ) E_{e_{1},e_{2},e_{3}}(\mathbb{Q}). For this point p = ( x, y) p=(x,y) we know that not all the factors ( x − e i) (x-e_{i}) can be rational squares, whereas the product y 2 = ( x − e 1) ​ ( x − e 2) ​ ( x − e 3) y^{2}=(x-e_{1})(x-e_{2})(x-e_{3}) is a rational square. Writing

 | x − e 1 = A 1 ​ α 1 2, x − e 2 = A 2 ​ α 2 2, x − e 3 = A 3 ​ α 3 2 x-e_{1}=A_{1}\alpha_{1}^{2},\qquad x-e_{2}=A_{2}\alpha_{2}^{2},\qquad x-e_{3}=A_{3}\alpha_{3}^{2} |  | ( 12) |

with squarefree integers A i A_{i}, we can eliminate x = A 1 ​ α 1 2 + e 1 x=A_{1}\alpha_{1}^{2}+e_{1} to arrive at the equations

 | A 1 ​ α 1 2 − A 2 ​ α 2 2 = e 2 − e 1, A 1 ​ α 1 2 − A 3 ​ α 3 2 = e 3 − e 1. A_{1}\alpha_{1}^{2}-A_{2}\alpha_{2}^{2}=e_{2}-e_{1},\qquad A_{1}\alpha_{1}^{2}-A_{3}\alpha_{3}^{2}=e_{3}-e_{1}. |  | ( 13) |

Moreover, the product A 1 ​ A 2 ​ A 3 A_{1}A_{2}A_{3} is a perfect square, which implies that A 3 = A 1 ​ A 2 A_{3}=A_{1}A_{2} up to a square factor. In this way we obtain the equations of the homogeneous space in the above considerations.

#### 2.3.2 Reducing the number of possibilities

Let us first observe that, given a set P ⊆ E e 1, e 2, e 3 ​ ( ℚ) P\subseteq E_{e_{1},e_{2},e_{3}}(\mathbb{Q}) of known rational points on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}, and given a homogeneous space Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}} by coefficients ( b 1, b 2) ∈ ℚ ∗ / ( ℚ ∗) 2 × ℚ ∗ / ( ℚ ∗) 2 (b_{1},b_{2})\in\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2}\times\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2}, then Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}} contains a rational point (i.e., is trivial in the Weil-Chatelet group) if and only if for any point p ∈ P p\in P the homogeneous space Q e 1, e 2, e 3, c 1, c 2 Q_{e_{1},e_{2},e_{3},c_{1},c_{2}} with ( c 1, c 2) = ( b 1, b 2) ⋅ φ ⁡ ( p) (c_{1},c_{2})=(b_{1},b_{2})\cdot\varphi(p) has a rational point. So we may say that ( b 1, b 2), ( c 1, c 2) ∈ ℚ ∗ / ( ℚ ∗) 2 × ℚ ∗ / ( ℚ ∗) 2 (b_{1},b_{2}),(c_{1},c_{2})\in\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2}\times\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2} are P P -equivalent if and only if there is a point p ∈ P p\in P such that ( c 1, c 2) = ( b 1, b 2) ⋅ φ ⁡ ( p) (c_{1},c_{2})=(b_{1},b_{2})\cdot\varphi(p). Using this relation, we may restrict our considerations to special representatives of homogeneous spaces whenever we a priori know some rational points on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. Note that a well-known set of rational points on E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} is always given by the set of 2-torsion points.

Now we consider either a single curve E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} or else a family of curves E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} depending on some parameter(s) such that we know in advance that the curve(s) contain rational points other than the 2-torsion points. To find appropriate homogeneous spaces for E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}} possessing rational points, we may pursue the following strategy:

- •

determine the (finite) set ℚ ⁡ ( S ​,2) \mathbb{Q}(S,2);

- •

build equivalence classes of pairs ( b 1, b 2) ∈ ℚ ⁡ ( S ​,2) × ℚ ⁡ ( S ​,2) (b_{1},b_{2})\in\mathbb{Q}(S,2)\times\mathbb{Q}(S,2) which are P P -equivalent with respect to the set P P of 2-torsion points of E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}};

- •

exclude those classes of pairs ( b 1, b 2) ∈ ℚ ⁡ ( S ​,2) × ℚ ⁡ ( S ​,2) (b_{1},b_{2})\in\mathbb{Q}(S,2)\times\mathbb{Q}(S,2) for which a rational solution cannot exist for one of the following reasons:

  - –

the quadric intersection Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}} has no rational points because of obstructions due to properties of quadratic residues;

  - –

at least one of the quadratic equations defining Q e 1, e 2, e 3, b 1, b 2 Q_{e_{1},e_{2},e_{3},b_{1},b_{2}} has no solution (for example because of Legendre’s criterion).

Then the homogeneous spaces associated with the remaining classes are good candidates for having rational points and thus giving rational points on the original elliptic curve(s) E e 1, e 2, e 3 E_{e_{1},e_{2},e_{3}}. Examples for the application of this method will be presented in the next section.

#### 2.3.3 Notations

The notations used up to this point were chosen to be consistent with the ones used in [20] and [8]. For the use in later sections, it will be convenient to modify the notations slightly. As mentioned in 2.1, we always may assume that the elliptic curve under consideration is one of the curves E M, N E_{M,N} with different nonzero integers M, N ∈ ℤ ∖ { 0 } M,N\in\mathbb{Z}\setminus\{0\}, given in affine form by a Weierstraß equation of the special form y 2 = x ⁡ ( x + M) ​ ( x + N) y^{2}=x(x+M)(x+N). In addition, we may assume M = p ​ k > 0 M=pk>0 and N = − q ​ k < 0 N=-qk<0 with coprime natural numbers p, q ∈ ℕ p,q\in\mathbb{N} and a square-free natural number k k. We write the equations for the homogeneous spaces in the form

 | A ​ X 0 2 + M ​ X 1 2 − B ​ X 2 2 = 0, A ​ X 0 2 + N ​ X 1 2 − C ​ X 3 2 = 0 AX_{0}^{2}+MX_{1}^{2}-BX_{2}^{2}=0,\qquad AX_{0}^{2}+NX_{1}^{2}-CX_{3}^{2}=0 |  | ( 14) |

where A, B, C ∈ ℚ ⁡ ( S ​,2) A,B,C\in\mathbb{Q}(S,2) are represented by squarefree integers, with C C depending on A A and B B by the condition that A ​ B ​ C ABC is a perfect square. We call ( A, B, C) (A,B,C) a triplet defining a homogeneous space for E M, N E_{M,N}. The approach sketched in 2.3.2 provides us with means to reduce the number of potential triplets ( A, B, C) (A,B,C) by ruling out impossible ones and by identifying triplets with respect to 2-torsion equivalence. (In the next section some speficic examples are provided which explicitly show how this is done.)

Let us choose any of the possible 2-descent parameter sets ( A, B, C) (A,B,C). Then we know that finding the expected solution of E M, N E_{M,N} is equivalent to finding a solution of the system ( 12) (12), which in our situation reads

 | x = A ​ α 2, x + M = B ​ β 2, x + N = C ​ γ 2. x=A\alpha^{2},\qquad x+M=B\beta^{2},\qquad x+N=C\gamma^{2}. |  | ( 15) |

where x, α, β, γ ∈ ℚ x,\alpha,\beta,\gamma\in\mathbb{Q}. With such a solution we get a rational point ( x, y) (x,y) on E M, N E_{M,N} by setting y = A ​ B ​ C ​ α ​ β ​ γ y=\sqrt{ABC}\alpha\beta\gamma. The system (15) is equivalent to the system (14), and an integer solution ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}) of (14) yields a rational solution of (15) via

 | x = A ​ x 0 2 x 1 2, y = A ​ B ​ C ​ x 0 ​ x 2 ​ x 3 x 1 3, ( α, β, γ) = ( x 0 x 1, x 2 x 1, x 3 x 1). x=\frac{Ax_{0}^{2}}{x_{1}^{2}},\qquad y=\sqrt{ABC}\,\frac{x_{0}x_{2}x_{3}}{x_{1}^{3}},\qquad(\alpha,\beta,\gamma)=\left(\frac{x_{0}}{x_{1}},\frac{x_{2}}{x_{1}},\frac{x_{3}}{x_{1}}\right). |  | ( 16) |

In projective notation, the sought rational point ( x, y) (x,y) on E M, N E_{M,N} is given by the expression ( x 1 3: A x 0 2 x 1: A ​ B ​ C x 0 x 2 x 3) (x_{1}^{3}:Ax_{0}^{2}x_{1}:\sqrt{ABC}\,x_{0}x_{2}x_{3}). We see that the logarithmic height of this point is about 3 times the logarithmic height of the solution ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}).

In the sequel we thus may restrict our considerations to systems of quadratic equations of the form (14). We may also assume that this system has a solution at all, which in particular implies that each of the two individual quadratic equations has a solution.

## 3 Examples for the two-descent

As before we consider elliptic curves which are given by an affine equation of the form y 2 = x ⁡ ( x + M) ​ ( x + N) y^{2}=x(x+M)(x+N) where M = p ​ k M=pk and N = − q ​ k N=-qk with coprime natural numbers p, q p,q and a squarefree natural number k k. We denote the elliptic curve defined in this way by E p, q, k E_{p,q,k} and its Mordell-Weil group by E p, q, k ​ ( ℚ) E_{p,q,k}(\mathbb{Q}). As explained before, our aim is to determine the homogeneous spaces over E p, q, k E_{p,q,k} defined over the rationals which have a rational point. For this purpose we consider the homomorphism φ = ( φ − p ​ k, φ 0, φ q ​ k): E p, q, k ​ ( ℚ) / 2 ​ E p, q, k ​ ( ℚ) → ( ℚ ∗ / ( ℚ ∗) 2) 3 \varphi=(\varphi_{-pk},\varphi_{0},\varphi_{qk}):E_{p,q,k}(\mathbb{Q})/2E_{p,q,k}(\mathbb{Q})\rightarrow(\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2})^{3} where the components are defined as in (11). For the sake of simplicity we look at all three components even though the third one is already determined by the other two. From the considerations in 2.3.1 above we know that finding non-2-torsion points on E p, q, k E_{p,q,k} is equivalent to finding triplets in the image of the mapping φ \varphi (or, equivalently, homogeneous spaces having a rational point). In this section we give examples how to find candidates of triplets which potentially may lie in the image of φ \varphi. In other words, we try to find criteria which exclude many of these triplets from potentially lying in the image of φ \varphi.

### 3.1 General strategy

We proceed as follows:

1. 1.

Determine the discriminant of the equation for E p, q, k E_{p,q,k}. Determine all prime divisors of this discriminant and the set S p, q, k ​ ( 2, ℚ) S_{p,q,k}(2,\mathbb{Q}) of all squarefree integers which are candidates for components appearing in the image of φ \varphi.

2. 2.

Determine all the triplets ( A, B, C) ∈ ( S p, q, k ​ ( 2, ℚ)) 3 (A,B,C)\in(S_{p,q,k}(2,\mathbb{Q}))^{3} which cannot a priori be ruled out to lie in the image of φ \varphi. Note that with the conventions set up above, A A is positive and A ​ B ​ C ABC is a perfect square.

3. 3.

Generate equivalence classes of the remaining triplets with respect to 2-torsion equivalence; extract representatives of these equivalence classes.

4. 4.

Eliminate all those triplets which give rise to a homogeneous space over E p, q, k E_{p,q,k} which cannot have a rational point due to the quadratic residue behaviour of the quadratic equations defining the homogeneous space.

5. 5.

Eliminate all triplets leading to a system of quadratic equations of the form (14) of section 2 such that at least one of the quadratic equations is not solvable.

The remaining triplets are good candidates to start the algorithm to be developed in the sequel.

### 3.2 General data

Since the discriminant of the elliptic curve E p, q, k E_{p,q,k} is given by discr ​ ( E p, q, k) = 16 ​ p 2 ​ q 2 ​ ( p + q) 2 ​ k 6 \hbox{discr}(E_{p,q,k})=16p^{2}q^{2}(p+q)^{2}k^{6}, the elements of S p, q, k ​ ( 2, ℚ) S_{p,q,k}(2,\mathbb{Q}) are the squarefree integral numbers which are composed of − 1 -1, 2 2 and the prime divisors of p, q, p + q p,q,p+q and k k. For analyzing the 2-torsion-equivalent triplets, it is interesting to know the values of the mappings φ − p ​ k \varphi_{-pk}, φ 0 \varphi_{0}, φ q ​ k \varphi_{qk} at the 2-torsion points ( − p ​ k ​,0) (-pk,0), ( 0,0) (0,0), ( q ​ k ​,0) (qk,0). We collect the results in the following table, where the values always have to be regarded as representatives which should be replaced by their squarefree parts.

 |

 | ( − p ​ k ​,0) (-pk,0) | ( 0,0) (0,0) | ( q ​ k ​,0) (qk,0) |

φ − p ​ k \varphi_{-pk} | p ⁡ ( p + q) p(p+q) | p ​ k pk | ( p + q) ​ k (p+q)k |

φ 0 \varphi_{0} | − p ​ k -pk | − p ​ q -pq | q ​ k qk |

φ q ​ k \varphi_{qk} | − ( p + q) ​ k -(p+q)k | − q ​ k -qk | q ⁡ ( p + q) q(p+q) |

 |  |

For any triplet ( A, B, C) (A,B,C) defining a homogeneous space over E p, q, k E_{p,q,k} we consider the equations x + p ​ k = A ​ α 2 x+pk=A\alpha^{2}, x = B ​ β 2 x=B\beta^{2}, x − q ​ k = C ​ γ 2 x-qk=C\gamma^{2} and try to examine whether or not these equations are solvable in rational numbers x, α, β, γ x,\alpha,\beta,\gamma. Here we may restrict our attention to some representative ( A, B, C) (A,B,C) modulo 2-torsion equivalence.

### 3.3 Examples

#### 3.3.1 Congruent prime numbers

The case of congruent prime numbers corresponds to the case p = q = 1 p=q=1 with k k being a prime number. This case is discussed extensively in [8]. The results can be summarized as follows:

- •

If k ≡ 1 k\equiv 1 or 3 3 mod 8 8, then the rank of E 1,1, k ​ ( ℚ) E_{1,1,k}(\mathbb{Q}) is zero and there is no non-2-torsion point on E 1,1, k ​ ( ℚ) E_{1,1,k}(\mathbb{Q})

- •

If k ≡ 5 k\equiv 5 mod 8 8, then the triplets ( A, B, C) (A,B,C) yielding a homogeneous space with a rational point are given by the 2-torsion-equivalence class containing ( 1, − 1, − 1) (1,-1,-1), ( 2, k ​,2 ​ k) (2,k,2k), ( k ​,1, k) (k,1,k) and ( 2 ​ k, − k, − 2) (2k,-k,-2).

- •

If k ≡ 7 k\equiv 7 mod 8 8, then the triplets ( A, B, C) (A,B,C) yielding a homogeneous space with a rational point are given by the 2-torsion-equivalence class containing ( 2,1,2) (2,1,2), ( 1, − k, − k) (1,-k,-k), ( 2 ​ k, − 1, − 2 ​ k) (2k,-1,-2k) and ( k, k ​,1) (k,k,1).

#### 3.3.2 Congruent numbers which are twice a prime number

This case corresponds to p = q = 1 p=q=1 and k = 2 ​ ℓ k=2\ell where ℓ \ell is a prime number and can be discussed in a way similar to the above case. By different methods (see [18], p. 343) we a priori know that 2 ​ ℓ 2\ell is a congruent number if ℓ ≡ 3 \ell\equiv 3 or 7 7 mod 8 8. In this situation we have S 1,1,2 ​ ℓ = { − 1,2, ℓ } S_{1,1,2\ell}=\{-1,2,\ell\}, and the possibilities for the triplets defining homogeneous spaces over E 1,1,2 ​ ℓ E_{1,1,2\ell} are grouped into the following 2-torsion-equivalence classes:

1. { ( 1,1,1), ( 2, − 2 ​ l, − l), ( 2 ​ l, − 1, − 2 ​ l), ( l ​,2 ​ l ​,2) } \{(1,1,1),(2,-2l,-l),(2l,-1,-2l),(l,2l,2)\} 2. { ( 1, − 1, − 1), ( 2,2 ​ l, l), ( 2 ​ l ​,1,2 ​ l), ( l, − 2 ​ l ​,2) } \{(1,-1,-1),(2,2l,l),(2l,1,2l),(l,-2l,2)\} 3. { ( 1,2,2), ( 2, − l, − 2 ​ l), ( 2 ​ l, − 2, − l), ( l, l ​,1) } \{(1,2,2),(2,-l,-2l),(2l,-2,-l),(l,l,1)\} 4. { ( 1, − 2, − 2), ( 2, l ​,2 ​ l), ( 2 ​ l ​,2, l), ( l, − l, − 1) } \{(1,-2,-2),(2,l,2l),(2l,2,l),(l,-l,-1)\} 5. { ( 2,1,2), ( 1, − 2 ​ l, − 2 ​ l), ( l, − 1, − l), ( 2 ​ l ​,2 ​ l ​,1) } \{(2,1,2),(1,-2l,-2l),(l,-1,-l),(2l,2l,1)\} 6. { ( 2, − 1, − 2), ( 1,2 ​ l ​,2 ​ l), ( l ​,1, l), ( 2 ​ l, − 2 ​ l, − 1) } \{(2,-1,-2),(1,2l,2l),(l,1,l),(2l,-2l,-1)\} 7. { ( 2,2,1), ( 1, − l, − l), ( l, − 2, − 2 ​ l), ( 2 ​ l, l ​,2) } \{(2,2,1),(1,-l,-l),(l,-2,-2l),(2l,l,2)\} 8. { ( 2, − 2, − 1), ( 1, l, l), ( l ​,2,2 ​ l), ( 2 ​ l, − l, − 2) } \{(2,-2,-1),(1,l,l),(l,2,2l),(2l,-l,-2)\}

The first of these classes is given by the 2-torsion elements themselves. For the other ones it is sufficient to consider the equations corresponding to the first triplet.

2. If ( A, B, C) = ( 1, − 1, − 1) (A,B,C)=(1,-1,-1) then x + 2 ​ ℓ = α 2 x+2\ell=\alpha^{2}, x = − β 2 x=-\beta^{2} and x − 2 ​ ℓ = − γ 2 x-2\ell=-\gamma^{2}. Subtracting the third equation from the first yields 4 ​ ℓ = α 2 + γ 2 4\ell=\alpha^{2}+\gamma^{2}. Clearing denominators and reducing modulo the prime number ℓ \ell, we see that − 1 -1 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 mod 4 4. So ℓ ≡ 1 \ell\equiv 1 or 5 5 mod 8 8.

3. If ( A, B, C) = ( 1,2,2) (A,B,C)=(1,2,2) then x + 2 ​ ℓ = α 2 x+2\ell=\alpha^{2}, x = 2 ​ β 2 x=2\beta^{2} and x − 2 ​ ℓ = 2 ​ γ 2 x-2\ell=2\gamma^{2}. Subtracting the third equation from the first yields 4 ​ ℓ = α 2 − 2 ​ γ 2 4\ell=\alpha^{2}-2\gamma^{2}. Clearing denominators and reducing modulo ℓ \ell we see that 2 2 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 7 7 mod 8 8.

4. If ( A, B, C) = ( 1, − 2, − 2) (A,B,C)=(1,-2,-2) then x + 2 ​ ℓ = α 2 x+2\ell=\alpha^{2}, x = − 2 ​ β 2 x=-2\beta^{2} and x − 2 ​ ℓ = − 2 ​ γ 2 x-2\ell=-2\gamma^{2}. Subtracting the second equation from the first yields 2 ​ l ​ ℓ = α 2 + 2 ​ β 2 2l\ell=\alpha^{2}+2\beta^{2}. Clearing denominators and reducing modulo ℓ \ell we see that − 2 -2 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 3 3 mod 8 8.

5. If ( A, B, C) = ( 2,1,2) (A,B,C)=(2,1,2) then x + 2 ​ ℓ = 2 ​ α 2 x+2\ell=2\alpha^{2}, x = β 2 x=\beta^{2}, x − 2 ​ ℓ = 2 ​ γ 2 x-2\ell=2\gamma^{2}. Subtracting the second equation from the first yields 2 ​ ℓ = 2 ​ α 2 − γ 2 2\ell=2\alpha^{2}-\gamma^{2}. Clearing denominators and reducing modulo ℓ \ell we see that − 2 -2 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 7 7 mod 8 8.

6. If ( A, B, C) = ( 2, − 1, − 2) (A,B,C)=(2,-1,-2) then x + 2 ​ ℓ = 2 ​ α 2 x+2\ell=2\alpha^{2}, x = − β 2 x=-\beta^{2}, x − 2 ​ ℓ = − 2 ​ γ 2 x-2\ell=-2\gamma^{2}. On the one hand, subtracting the third equation from the first yields 4 ​ ℓ = 2 ​ α 2 + 2 ​ γ 2 4\ell=2\alpha^{2}+2\gamma^{2}. Clearing denominators, dividing by 2 2 and reducing modulo ℓ \ell we see that − 1 -1 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 mod 4 4 so that ℓ ≡ 1 \ell\equiv 1 or 5 5 mod 8 8. On the other hand, subtracting the second equation from the first yields 2 ​ ℓ = 2 ​ α 2 + β 2 2\ell=2\alpha^{2}+\beta^{2}. Clearing denominators and reducing modulo ℓ \ell we see that − 2 -2 is a quadratic residue mod ℓ \ell, which implies that ℓ ≡ 1 \ell\equiv 1 or 3 3 mod 8 8. Combining both results, we see that ℓ ≡ 1 \ell\equiv 1 mod 8 8.

7. If ( A, B, C) = ( 2,2,1) (A,B,C)=(2,2,1) then x + 2 ​ ℓ = 2 ​ α 2 x+2\ell=2\alpha^{2}, x = 2 ​ β 2 x=2\beta^{2}, x − 2 ​ ℓ = γ 2 x-2\ell=\gamma^{2}. Subtracting the third equation from the first yields 4 ​ ℓ = 2 ​ α 2 − γ 2 4\ell=2\alpha^{2}-\gamma^{2}. Clearing denominators and reducing modulo ℓ \ell we see that 2 2 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 7 7 mod 8 8.

8. If ( A, B, C) = ( 2, − 2, − 1) (A,B,C)=(2,-2,-1) then x + 2 ​ ℓ = 2 ​ α 2 x+2\ell=2\alpha^{2}, x = − 2 ​ β 2 x=-2\beta^{2}, x − 2 ​ ℓ = − γ 2 x-2\ell=-\gamma^{2}. On the one hand, subtracting the third equation from the first yields 4 ​ ℓ = 2 ​ α 2 + γ 2 4\ell=2\alpha^{2}+\gamma^{2}. Clearing denominators and reducing modulo ℓ \ell we see that − 2 -2 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 3 3 mod 8 8. On the other hand, subtracting the second equation from the first yields 2 ​ ℓ = 2 ​ α 2 + 2 ​ β 2 2\ell=2\alpha^{2}+2\beta^{2}. Clearing denominators, dividing by 2 and reducing modulo ℓ \ell we see that − 1 -1 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 5 5 mod 8 8. Combining both results we see that ℓ ≡ 1 \ell\equiv 1 mod 8 8.

Since we know beforehand (see [18], p. 343) that the number 2 ​ ℓ 2\ell is congruent if ℓ ≡ 3 \ell\equiv 3 or 7 7 mod 8 8, the above calculations give the following necessary conditions.

- •

If l ≡ 3 l\equiv 3 mod 8 8 then the only possibilities for solvable systems are given by the equivalence classes of the triplets ( 1, − 2, − 2) (1,-2,-2) and ( 2, − 2, − 1) (2,-2,-1).

- •

If l ≡ 7 l\equiv 7 mod 8 8 then the only possibilities for solvable systems are given by the equivalence classes of the triplets ( 1,2,2) (1,2,2), ( 2,1,2) (2,1,2) and ( 2,2,1) (2,2,1).

Explicit calculations show that in the first case the triplet ( 1, − 2, − 2) (1,-2,-2) yields solvable equations whereas the second one does not. Also by explicit calculations, in the second case the only triplet yielding solvable equations is ( 2,2,1) (2,2,1). For the rational points on the corresponding elliptic curves we refer to section 5 below.

#### 3.3.3 Examples with rank ( E p, q, k ​ ( ℚ)) = 2 \bigl(E_{p,q,k}(\mathbb{Q})\bigr)=2

The examples considered here correspond to the 2 ​ π / 3 2\pi/3 -congruent numbers 14 14, 206 206 and 398 398. These numbers are of the form 2 ​ ℓ 2\ell where ℓ \ell is a prime number satisfying ℓ ≡ 7 \ell\equiv 7 mod 96 96; hence the associated elliptic curve is given by p = 1 p=1, q = 3 q=3 and k = 2 ​ ℓ k=2\ell. We do not know whether all of these numbers ℓ \ell yield elliptic curves with rank ​ ( E 1,3,2 ​ ℓ ​ ( ℚ)) = 2 \hbox{rank}(E_{1,3,2\ell}(\mathbb{Q}))=2, but at least for the three explicit examples above we will show in section 5 that there are two independent solutions.

The discriminant of E 1,3,2 ​ ℓ E_{1,3,2\ell} is discr ​ ( E 1,3,2 ​ ℓ) = 2 14 ​ 3 2 ​ ℓ 6 \hbox{\rm discr}(E_{1,3,2\ell})=2^{14}3^{2}\ell^{6} so that S 1,3,2 ​ ℓ = { − 1,2,3, ℓ } S_{1,3,2\ell}=\{-1,2,3,\ell\}. In particular, we get 128 128 possibilities for the triplets ( A, B, C) (A,B,C) characterizing the homogeneous spaces associated with the 2-descent. The table for the mapping φ \varphi at the 2-torsion points looks as follows.

 |

 | ( − 2 ​ l ​,0) (-2l,0) | ( 0,0) (0,0) | ( 6 ​ l ​,0) (6l,0) |

φ − 2 ​ l \varphi_{-2l} | 1 1 | 2 ​ l 2l | 2 ​ l 2l |

φ 0 \varphi_{0} | − 2 ​ l -2l | − 3 -3 | 6 ​ l 6l |

φ 6 ​ l \varphi_{6l} | − 2 ​ l -2l | − 6 ​ l -6l | 3 3 |

 |  |

We see that any 2-torsion equivalence class contains a triplet which is independent of 2 ​ ℓ 2\ell. So the equivalence classes of these triplets are already determined by the 32 possible triplets composed of the factor set { − 1,2,3 } \{-1,2,3\}. (Note that − 1 -1 does not occur as a factor of A A since A A is positive.)

Let us discuss the explicit example of the triplet ( A, B, C) = ( 3,3,1) (A,B,C)=(3,3,1). The equations from 3.2 are x + 2 ​ ℓ = 3 ​ α 2 x+2\ell=3\alpha^{2}, x = 3 ​ β 2 x=3\beta^{2} and x − 6 ​ ℓ = γ 2 x-6\ell=\gamma^{2}. Subtracting the third equation from the first yields 8 ​ ℓ = 3 ​ α 2 − γ 2 8\ell=3\alpha^{2}-\gamma^{2}. Clearing denominators and reducing modulo the prime number ℓ \ell shows that 3 3 is a quadratic residue mod ℓ \ell, hence ℓ ≡ 1 \ell\equiv 1 or 11 11 mod 12 12. But this is not the case for l ≡ 7 l\equiv 7 mod 96 96. So this triplet does not belong to a homogeneous space having a rational point.

In the same way we may discuss all 32 possibilities. The only triplets which do not lead to a contradiction are ( 1,2,2) (1,2,2), ( 1, − 3, − 3) (1,-3,-3), ( 1, − 6, − 6) (1,-6,-6), ( 2,1,2) (2,1,2), ( 2,2,1) (2,2,1), ( 2, − 3, − 6) (2,-3,-6) and ( 2, − 6, − 3) (2,-6,-3). These triplets provide candidates for the search for rational solutions of the corresponding equations. In section 5 we will see that the triplets ( 1,2,2) (1,2,2), ( 2, − 3, − 6) (2,-3,-6) and ( 2, − 6, − 3) (2,-6,-3) indeed lead to solutions, as, of course, also do all triplets which are 2-torsion-equivalent to one of these. For the sake of completeness, let us explicitly write down the 2-torsion equivalence classes of these three triplets:

∙ \bullet { ( 1,2,2), ( 2 ​ l, − 6, − 3 ​ l), ( 1, − l, − l), ( 2 ​ l ​,3 ​ l ​,6) } \{(1,2,2),(2l,-6,-3l),(1,-l,-l),(2l,3l,6)\}; ∙ \bullet { ( 2, − 3, − 6), ( l ​,1, l), ( 2,6 ​ l ​,3 ​ l), ( l, − 2 ​ l, − 2) } \{(2,-3,-6),(l,1,l),(2,6l,3l),(l,-2l,-2)\}; ∙ \bullet { ( 2, − 6, − 3), ( l ​,2,2 ​ l), ( 2,3 ​ l ​,6 ​ l), ( l, − l, − 1) } \{(2,-6,-3),(l,2,2l),(2,3l,6l),(l,-l,-1)\}.

Note that in the group structure of ( ℚ ∗ / ( ℚ ∗) 2 × ( ℚ ∗ / ( ℚ ∗) 2 × ( ℚ ∗ / ( ℚ ∗) 2 (\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2}\times(\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2}\times(\mathbb{Q}^{*}/(\mathbb{Q}^{*})^{2} the third triplet is the product of the other two. So solutions corresponding to the third triplet correspond to sums of solutions of the other ones (the sum being calculated in terms of the elliptic curve structure of the given curve E 1,3,2 ​ ℓ E_{1,3,2\ell}). But the solutions belonging to the first and the second triplet are independent with respect to the elliptic curve addition, and since they are of infinite order we have shown that the Mordell-Weil rank of these groups is at least 2 2.

## 4 Algorithm

### 4.1 Weak form of the algorithm

The starting point of our algorithm is a system of quadratic equations of the form

(17)

 |  | Q 1 ​ ( X 0, X 1, X 2) \displaystyle Q_{1}(X_{0},X_{1},X_{2})\  |  | = a 00 ​ X 0 2 + a 11 ​ X 1 2 + a 22 ​ X 2 2 \displaystyle=\ a_{00}X_{0}^{2}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2}\  |  | = 0 \displaystyle=\ 0 |  |

 |  | Q 2 ​ ( X 0, X 1, X 3) \displaystyle Q_{2}(X_{0},X_{1},X_{3})\  |  | = b 00 ​ X 0 2 + b 11 ​ X 1 2 + b 33 ​ X 3 2 \displaystyle=\ b_{00}X_{0}^{2}+b_{11}X_{1}^{2}+b_{33}X_{3}^{2}\  |  | = 0 \displaystyle=\ 0 |  |

which we assume to be solvable in integers. Then in particular there is a point ( x 0, x 1, x 2) ∈ ℤ 3 ∖ { ( 0,0,0) } (x_{0},x_{1},x_{2})\in\mathbb{Z}^{3}\setminus\{(0,0,0)\} with Q 1 ​ ( x 0, x 1, x 2) = 0 Q_{1}(x_{0},x_{1},x_{2})=0. By Newton’s method, projecting from ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}), we may parametrize the solutions of Q 1 Q_{1} by quadratic polynomials

 | X 0 = Φ 0 ​ ( ξ 0, ξ 1), X 1 = Φ 1 ​ ( ξ 0, ξ 1), X 2 = Φ 2 ​ ( ξ 0, ξ 1), X_{0}=\Phi_{0}(\xi_{0},\xi_{1}),\qquad X_{1}=\Phi_{1}(\xi_{0},\xi_{1}),\qquad X_{2}=\Phi_{2}(\xi_{0},\xi_{1}), |  | ( 18) |

which means that the solutions ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) of the equation Q 1 = 0 Q_{1}=0 are exactly the points OPEN ( Φ 0 ​ ( ξ 0, ξ 1), Φ 1 ​ ( ξ 0, ξ 1), Φ 2 ​ ( ξ 0, ξ 1))) \bigl(\Phi_{0}(\xi_{0},\xi_{1}),\Phi_{1}(\xi_{0},\xi_{1}),\Phi_{2}(\xi_{0},\xi_{1})\bigr)) where ( ξ 0, ξ 1) ∈ ℙ 1 ​ ( ℚ) (\xi_{0},\xi_{1})\in\mathbb{P}^{1}(\mathbb{Q}). Substituting this parametrization for X 0 X_{0} and X 1 X_{1} into the equation for Q 2 Q_{2} yields an equation

(19)

 |  | Q 3 ​ ( ξ 0, ξ 1, X 3) = Q 2 ​ ( Φ 0 ​ ( ξ 0, ξ 1), Φ 0 ​ ( ξ 0, ξ 1), X 3) \displaystyle Q_{3}(\xi_{0},\xi_{1},X_{3})\ =\ Q_{2}\bigl(\Phi_{0}(\xi_{0},\xi_{1}),\Phi_{0}(\xi_{0},\xi_{1}),X_{3}\bigr) |  |

 |  | = b 00 ​ Φ 0 ​ ( ξ 0, ξ 1) 2 + b 11 ​ Φ 1 ​ ( ξ 0, ξ 1) 2 + b 33 ​ X 3 2 = 0 \displaystyle=\ b_{00}\Phi_{0}(\xi_{0},\xi_{1})^{2}+b_{11}\Phi_{1}(\xi_{0},\xi_{1})^{2}+b_{33}X_{3}^{2}\ =\ 0 |  |

which is of degree 4 4 in ( ξ 0, ξ 1) (\xi_{0},\xi_{1}) and of degree 2 2 in X 3 X_{3}. This equation is the basis of the weak form of the following algorithm for finding solutions of a system of the form (17).

eee /* weak algorithm */ eee INPUT: quadrics Q 1 Q_{1} and Q 2 Q_{2} eee BEGIN eee determine a solution ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) of Q 1 = 0 Q_{1}=0 eee calculate parametrizations X i = Φ i ​ ( ξ 0, ξ 1) X_{i}=\Phi_{i}(\xi_{0},\xi_{1}), i = 0,1,2 i=0,1,2 eee loop over ( ξ 0, ξ 1) (\xi_{0},\xi_{1}) eee eee BEGIN eee eee eee calculate value = − b 33 ​ ( b 00 ​ Φ 0 ​ ( ξ 0, ξ 1) 2 + b 11 ​ Φ 1 ​ ( ξ 0, ξ 1) 2) =-b_{33}(b_{00}\Phi_{0}(\xi_{0},\xi_{1})^{2}+b_{11}\Phi_{1}(\xi_{0},\xi_{1})^{2}) eee eee eee check whether value is a square number eee eee eee if yes eee eee eee BEGIN eee eee eee eee /* solution found */ eee eee eee eee x 0 = Φ 0 ​ ( ξ 0, ξ 1) x_{0}=\Phi_{0}(\xi_{0},\xi_{1}) eee eee eee eee x 1 = Φ 1 ​ ( ξ 0, ξ 1) x_{1}=\Phi_{1}(\xi_{0},\xi_{1}) eee eee eee eee x 2 = Φ 2 ​ ( ξ 0, ξ 1) x_{2}=\Phi_{2}(\xi_{0},\xi_{1}) eee eee eee eee x 3 = value / ( − b 33) x_{3}=\sqrt{\hbox{{v}alue}}/(-b_{33}) eee eee eee eee RETURN ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}) eee eee eee END eee eee END eee END
Remarks:

- •

The algorithm is not guaranteed to terminate. In fact, to the best of our knowledge no upper bound for the smallest solution of a system of the form (17) is known.

- •

The logarithmic height of a solution ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}) found by the algorithm is about twice the logarithmic height of the parameters ( ξ 0, ξ 1) (\xi_{0},\xi_{1}).

- •

Assuming that the algorithmic complexity of the calculations within the algorithm do not too strongly depend on the magnitude of the numbers involved, then the complexity of the algorithm depends quadratically on the height of the parameters ( ξ 0, ξ 1) (\xi_{0},\xi_{1}).

- •

Using a general purpose computer, it is possible to calculate the final loop for the parameters ξ 0, ξ 1 \xi_{0},\xi_{1} up to about 10 000 10\,000 within a few minutes, which yields results for the original quadratic equations with up to about 25 25 digits (in decimal representation).

### 4.2 Strong form of the algorithm

This section is devoted to an improved version of the weak form of the algorithm, provided a special property of the considered equations holds.

#### 4.2.1 Additional preparation and condition

We note that the starting point of our algorithm is the system ( 17) (17) which consists of two quadratic equations of a very special form. Namely, exactly two of the variables appear in both equations. We can, of course, eliminate from each of the equations one of the common variables, which yields four equations each of which contains exactly three of the four original variables, and each choice of two of these equations defines the same quadric intersection in projective 3-space. We now impose a condition which seems to be of a purely technical nature (not corresponding to any geometric or arithmetic property of the given elliptic curve), but seems to be satisfied in many particular cases. (See the examples in the subsequent sections.)

Condition: We suppose that at least one of the four equations has a solution with one coordinate being zero.

We choose the equation of the condition to be the first one and choose a second equation such that the variable whose coordinate in the distinguished solution is zero appears in both equations. After renaming the variables if necessary, we may suppose without loss of generality that the equations have the form ( 17) (17) and that ( 0, x 1, x 2) (0,x_{1},x_{2}) is an integer solution for Q 1 Q_{1}. As above, we parametrize the quadratic form Q 1 Q_{1} projecting from this point ( 0, x 1, x 2) (0,x_{1},x_{2}), which gives expressions X i = Φ i ​ ( ξ 0, ξ 1) X_{i}=\Phi_{i}(\xi_{0},\xi_{1}) as in ( 18) (18), and as above we substitute the parametrizations of X 0 X_{0} and X 1 X_{1} into the second equation. The crucial observation is that in our particular situation the polynomial Q 3 Q_{3} in equation ( 19) (19) is biquadratic in ( ξ 0, ξ 1) (\xi_{0},\xi_{1}); see 2.2.3. Hence substituting Y 0 = ξ 0 2 Y_{0}=\xi_{0}^{2}, Y 1 = ξ 1 2 Y_{1}=\xi_{1}^{2}, Y 2 = X 3 Y_{2}=X_{3} yields a quadratic form, which we denote (with a slight abuse of notation) by Q 3 ​ ( Y 0, Y 1, Y 2) Q_{3}(Y_{0},Y_{1},Y_{2}). Our task is then to find an integer solution of the equation Q 3 ​ ( y 0, y 1, y 2) = 0 Q_{3}(y_{0},y_{1},y_{2})=0 in such a way that both y 0 y_{0} and y 1 y_{1} are squares.

Remark: The property of being a square number is not invariant with respect to the change of representatives of projective coordinates. So the above problem can be stated equivalently by saying that we look for a coprime solution ( y 0, y 1, y 2) (y_{0},y_{1},y_{2}) for Q 3 Q_{3} and a factor μ \mu (which we may assume to be squarefree) such that y 0 = μ ​ σ 0 2 y_{0}=\mu\sigma_{0}^{2}, y 1 = μ ​ σ 1 2 y_{1}=\mu\sigma_{1}^{2}. This seems to be difficult. However, we can establish a strong condition for the possible factors μ \mu, as will be explained below.

Remark: The order of magnitude of ξ i \xi_{i} is about twice the order of magnitude of X i X_{i}, so Y i Y_{i} and X i X_{i} are nearly of the same order of magnitude.

#### 4.2.2 Parametrization of Q 3 Q_{3} and condition for μ \mu

As always we assume our problem to have a solution, hence Q 3 Q_{3} has a solution with the required property; in particular, Q 3 Q_{3} has a rational solution which, without loss of generality, we may assume to consist of coprime integers. Let p = ( p 0, p 1, p 2) p=(p_{0},p_{1},p_{2}) be such a solution. We parametrize Q 3 Q_{3} using p p as projection point according to Newton’s method to get representations

 | Y 0 = Ψ 0 ​ ( η 0, η 1), Y 1 = Ψ 1 ​ ( η 0, η 1), Y 2 = Ψ 2 ​ ( η 0, η 1) Y_{0}\ =\ \Psi_{0}(\eta_{0},\eta_{1}),\qquad Y_{1}\ =\ \Psi_{1}(\eta_{0},\eta_{1}),\qquad Y_{2}\ =\ \Psi_{2}(\eta_{0},\eta_{1}) |  | ( 20) |

with quadratic forms Ψ 0, Ψ 1, Ψ 2 \Psi_{0},\Psi_{1},\Psi_{2}. We observe that if μ \mu is a factor as considered in the last remark of 4.2.1, then μ \mu divides the numbers Ψ i ​ ( η 0, η 1) \Psi_{i}(\eta_{0},\eta_{1}) where i = 0,1,2 i=0,1,2 and hence also divides all ℤ {\mathbb{Z}} -linear combination of these three numbers. We write

(21)

 | Ψ 0 ​ ( η 0, η 1) \displaystyle\Psi_{0}(\eta_{0},\eta_{1}) | = \displaystyle= | ψ 00 ( 0) ​ η 0 2 + ψ 01 ( 0) ​ η 0 ​ η 1 + ψ 11 ( 0) ​ η 1 2 \displaystyle\psi_{00}^{(0)}\eta_{0}^{2}+\psi_{01}^{(0)}\eta_{0}\eta_{1}+\psi_{11}^{(0)}\eta_{1}^{2} |  |

 | Ψ 1 ​ ( η 0, η 1) \displaystyle\Psi_{1}(\eta_{0},\eta_{1}) | = \displaystyle= | ψ 00 ( 1) ​ η 0 2 + ψ 01 ( 1) ​ η 0 ​ η 1 + ψ 11 ( 1) ​ η 1 2 \displaystyle\psi_{00}^{(1)}\eta_{0}^{2}+\psi_{01}^{(1)}\eta_{0}\eta_{1}+\psi_{11}^{(1)}\eta_{1}^{2} |  |

 | Ψ 2 ​ ( η 0, η 1) \displaystyle\Psi_{2}(\eta_{0},\eta_{1}) | = \displaystyle= | ψ 00 ( 2) ​ η 0 2 + ψ 01 ( 2) ​ η 0 ​ η 1 + ψ 11 ( 2) ​ η 1 2 \displaystyle\psi_{00}^{(2)}\eta_{0}^{2}+\psi_{01}^{(2)}\eta_{0}\eta_{1}+\psi_{11}^{(2)}\eta_{1}^{2} |  |

and determine coprime integer coefficients c i c_{i} where i = 0,1,2 i=0,1,2 such that

(22)

 | c 0 ​ ψ 00 ( 0) + c 1 ​ ψ 00 ( 1) + c 2 ​ ψ 00 ( 2) \displaystyle c_{0}\psi_{00}^{(0)}+c_{1}\psi_{00}^{(1)}+c_{2}\psi_{00}^{(2)} | = \displaystyle= | 0, \displaystyle 0, |  |

 | c 0 ​ ψ 11 ( 0) + c 1 ​ ψ 11 ( 1) + c 2 ​ ψ 11 ( 2) \displaystyle c_{0}\psi_{11}^{(0)}+c_{1}\psi_{11}^{(1)}+c_{2}\psi_{11}^{(2)} | = \displaystyle= | 0. \displaystyle 0. |  |

so that

 | c 0 ​ Y 0 + c 1 ​ Y 1 + c 2 ​ Y 2 = ( c 0 ​ ψ 01 ( 0) + c 1 ​ ψ 01 ( 1) + c 2 ​ ψ 01 ( 2)) ⋅ η 0 ​ η 1. c_{0}Y_{0}+c_{1}Y_{1}+c_{2}Y_{2}\ =\ (c_{0}\psi_{01}^{(0)}+c_{1}\psi_{01}^{(1)}+c_{2}\psi_{01}^{(2)})\cdot\eta_{0}\eta_{1}. |  | ( 23) |

Since we are looking for coprime solutions ( y 0, y 1, y 2) (y_{0},y_{1},y_{2}) we may assume ( η 0, η 1) (\eta_{0},\eta_{1}) to be coprime and the factor μ \mu to be coprime with both η 0 \eta_{0} and η 1 \eta_{1}. So we have the following necessary condition for the possible factors μ \mu.

Condition: The factor μ \mu divides (the squarefree part of) D = c 0 ​ ψ 01 ( 0) + c 1 ​ ψ 01 ( 1) + c 2 ​ ψ 01 ( 2) D=c_{0}\psi_{01}^{(0)}+c_{1}\psi_{01}^{(1)}+c_{2}\psi_{01}^{(2)}.

A second (trivial) necessary condition for μ \mu is given by the property that the two quadratic equation

(24)

 |  | μ ​ σ 0 2 \displaystyle\mu\sigma_{0}^{2}\  |  | = Ψ 0 ​ ( η 0, η 1) \displaystyle=\ \Psi_{0}(\eta_{0},\eta_{1})\  |  | = ψ 00 ( 0) ​ η 0 2 + ψ 01 ( 0) ​ η 0 ​ η 1 + ψ 11 ( 0) ​ η 1 2, \displaystyle=\ \psi_{00}^{(0)}\eta_{0}^{2}+\psi_{01}^{(0)}\eta_{0}\eta_{1}+\psi_{11}^{(0)}\eta_{1}^{2}, |  |

 |  | μ ​ σ 1 2 \displaystyle\mu\sigma_{1}^{2}\  |  | = Ψ 1 ​ ( η 0, η 1) \displaystyle=\ \Psi_{1}(\eta_{0},\eta_{1})\  |  | = ψ 00 ( 1) ​ η 0 2 + ψ 01 ( 1) ​ η 0 ​ η 1 + ψ 11 ( 1) ​ η 1 2 \displaystyle=\ \psi_{00}^{(1)}\eta_{0}^{2}+\psi_{01}^{(1)}\eta_{0}\eta_{1}+\psi_{11}^{(1)}\eta_{1}^{2} |  |

are both (individually) solvable (in the variables η 0, η 1 \eta_{0},\eta_{1} and σ 0 \sigma_{0} or σ 1 \sigma_{1}, respectively. Apart from the above necessary conditions for the factor μ \mu, there seems to be no a priori criterion for selecting an appropriate factor μ \mu. We have to resort to a trial-and-error approach going through the possible candidates. We note in passing that the logarithmic height of ( Y 0, Y 1, Y 2) (Y_{0},Y_{1},Y_{2}) is about twice the logarithmic height of ( η 0, η 1) (\eta_{0},\eta_{1}).

#### 4.2.3 New quadratic form

Having chosen a suitable factor μ \mu according to 4.2.2, the original problem is transformed to solving the system ( 24) (24). (Note that the orders of magnitude of the parameters η 0 \eta_{0}, η 1 \eta_{1} and of σ 0 \sigma_{0}, σ 1 \sigma_{1} are approximately equal.)

Let us rename the variables ( η 0, η 1, σ 0) (\eta_{0},\eta_{1},\sigma_{0}) to ( Z 0, Z 1, Z 2) (Z_{0},Z_{1},Z_{2}) and let us denote the first of the quadratic equations in ( 24) (24) by Q 4 ​ ( Z 0, Z 1, Z 2) = 0 Q_{4}(Z_{0},Z_{1},Z_{2})=0. Again, let us determine a rational point ( z 0, z 1, z 2) (z_{0},z_{1},z_{2}) on this quadric and let us parametrize Q 4 Q_{4} by using this point as a projection point. Then we obtain a representation

 | Z 0 = Γ 0 ​ ( ρ 0, ρ 1), Z 1 = Γ 1 ​ ( ρ 0, ρ 1), Z 2 = Γ 2 ​ ( ρ 0, ρ 1) Z_{0}\ =\ \Gamma_{0}(\rho_{0},\rho_{1}),\qquad Z_{1}\ =\ \Gamma_{1}(\rho_{0},\rho_{1}),\qquad Z_{2}\ =\ \Gamma_{2}(\rho_{0},\rho_{1}) |  | ( 25) |

with quadratic forms Γ i \Gamma_{i}. Again, for any pair of parameters ( ρ 0, ρ 1) (\rho_{0},\rho_{1}) we get a solution for the first equation Q 4 ​ ( Z 0, Z 1, Z 2) = 0 Q_{4}(Z_{0},Z_{1},Z_{2})=0. Substituting the expressions for Z 0 Z_{0} and Z 1 Z_{1} into the right-hand side of the second equation yields

 | Ψ 1 ​ ( Γ 0 ​ ( ρ 0, ρ 1), Γ 1 ​ ( ρ 0, ρ 1)) = μ ​ σ 1 2. \Psi_{1}\bigl(\Gamma_{0}(\rho_{0},\rho_{1}),\Gamma_{1}(\rho_{0},\rho_{1})\bigr)\ =\ \mu\sigma_{1}^{2}. |  | ( 26) |

This equation (which is of degree 4 4 in the variables ρ 0, ρ 1 \rho_{0},\rho_{1}) is the base for a final search loop. We note that the logarithmic height of ( Z 0, Z 1, Z 2) (Z_{0},Z_{1},Z_{2}) is about twice the logarithmic height of ( ρ 0, ρ 1) (\rho_{0},\rho_{1}).

#### 4.2.4 Algorithm

The considerations above may be combined to the following strong form of the algorithm.

eee /* strong algorithm */ eee INPUT: quadrics Q 1 Q_{1} and Q 2 Q_{2} eee BEGIN eee calculate a representation of the quadric intersection as in 4.2.1 eee calculate a special point on Q 1 Q_{1} of the form x = ( 0, x 1, x 2) x=(0,x_{1},x_{2}) eee calculate the parametrization of Q 1 Q_{1} projecting from x x: eee eee X i = Φ i ​ ( ξ 0, ξ 1) X_{i}=\Phi_{i}(\xi_{0},\xi_{1}), i = 0,1,2 i=0,1,2; eee substitute X i = Φ i ​ ( ξ 0, ξ 1) X_{i}=\Phi_{i}(\xi_{0},\xi_{1}), i = 0,1 i=0,1, and plug into Q 2 Q_{2} eee calculate quadratic form Q 3 ​ ( Y 0, Y 1, Y 2) Q_{3}(Y_{0},Y_{1},Y_{2}) from this substitution eee determine point y = ( y 0, y 1, y 2) y=(y_{0},y_{1},y_{2}) on Q 3 Q_{3} eee calculate the parametrization of Q 3 Q_{3} projecting from y y: eee eee Y i = Ψ i ​ ( η 0, η 1) Y_{i}=\Psi_{i}(\eta_{0},\eta_{1}), i = 0,1,2 i=0,1,2 eee determine the system of linear equations (22) eee determine a solution of this system eee calculate the value D D from 4.2.2 eee determine the possible values for the coefficient μ \mu eee choose an appropriate value for μ \mu eee calculate the quadratic form Q 4 ​ ( Z 0, Z 1, Z 2) Q_{4}(Z_{0},Z_{1},Z_{2}) from 4.2.3 eee determine a point z = ( z 0, z 1, z 2) z=(z_{0},z_{1},z_{2}) on Q 4 Q_{4} eee calculate the parametrization of Q 4 Q_{4} projecting from z z: eee eee Z i = Γ i ​ ( ρ 0, ρ 1) Z_{i}=\Gamma_{i}(\rho_{0},\rho_{1}), i = 0,1,2 i=0,1,2 eee calculate the quartic form Ψ 1 ​ ( Γ 0 ​ ( ρ 0, ρ 1), Γ 1 ​ ( ρ 0, ρ 1)) \Psi_{1}(\Gamma_{0}(\rho_{0},\rho_{1}),\Gamma_{1}(\rho_{0},\rho_{1})) eee loop over ( ρ 0, ρ 1) (\rho_{0},\rho_{1}) eee eee BEGIN eee eee eee calculate the value val = Ψ 1 ​ ( Γ 0 ​ ( ρ 0, ρ 1), Γ 1 ​ ( ρ 0, ρ 1)) =\Psi_{1}\bigl(\Gamma_{0}(\rho_{0},\rho_{1}),\Gamma_{1}(\rho_{0},\rho_{1})\bigr) eee eee eee check whether μ ⋅ \mu\cdot val is a square eee eee eee if yes then eee eee eee BEGIN eee eee eee eee /* Solution found */ eee eee eee eee BREAK eee eee eee END eee eee END eee calculate values Z i = Γ i ​ ( ρ 0, ρ 1) Z_{i}=\Gamma_{i}(\rho_{0},\rho_{1}), i = 0,1,2 i=0,1,2 eee SET η i = Z i \eta_{i}=Z_{i}, i = 0,1 i=0,1 eee calculate values Y i = Ψ i ​ ( η 0, η 1) Y_{i}=\Psi_{i}(\eta_{0},\eta_{1}) eee calculate ξ i = μ ​ Y i \xi_{i}=\sqrt{\mu Y_{i}}, i = 0,1 i=0,1 eee calculate values X i = Φ i ​ ( ξ 0, ξ 1) X_{i}=\Phi_{i}(\xi_{0},\xi_{1}), i = 0,1,2 i=0,1,2 eee if necessary, rename the variables as explained in 4.2.1 eee RETURN ( X 0, X 1, X 2, X 3) (X_{0},X_{1},X_{2},X_{3}) eee END

Remarks:

- •

As was the case with its weak form, the algorithm is not guaranteed to terminate.

- •

The logarithmic height of a solution ( x 0, x 1, x 2, x 3) (x_{0},x_{1},x_{2},x_{3}) found by the algorithm is about four times the logarithmic height of the parameters ( ρ 0, ρ 1) (\rho_{0},\rho_{1}) of the final loop. Hence the number of digits in the solutions which can be found by a search up to a certain height for the parameters in the final search loop is about twice as large as compared to the weak form of the algorithm. This improvement is counteracted by the fact that the additional condition of 4.2.1 needs to be imposed on the given quadratic forms. Another disadvantage is the task of choosing a factor μ \mu according to 4.2.3, for which we are not aware of a guiding principle.

- •

As is the case with its weak form, the complexity of the algorithm depends quadratically on the height of the parameters ( ρ 0, ρ 1) (\rho_{0},\rho_{1}).

## 5 Examples

This section is devoted to the discussion and presentation of explicit examples to which the above algorithm is applied. In the first example we demonstrate the execution of the algorithm, exploiting the choices to be made for making the algorithm work and presenting the intermediate data produced within the algorithm. The second subsection collects some series of examples which are very similar in their behaviour, while the third part treats examples with rank larger than one.

### 5.1 An explicit example

Let us consider the case of the 2 ​ π / 3 2\pi/3 -congruent number n = 142 = 2 ⋅ 71 n=142=2\cdot 71. (Note that 71 71 is a prime number congruent to − 1 -1 mod 8 8 and hence is 2 ​ π / 3 2\pi/3 -congruent; cf. [24].) The elliptic curve associated with this problem is given by y 2 = x ⁡ ( x + 142) ​ ( x − 3 ⋅ 142) y^{2}=x(x+142)(x-3\cdot 142), and the equations for the corresponding concordant form problem are W 0 2 − 3 ⋅ 142 ​ W 1 2 = W 2 2 W_{0}^{2}-3\cdot 142\,W_{1}^{2}=W_{2}^{2} and W 0 2 + 142 ​ W 1 2 = W 3 2 W_{0}^{2}+142\,W_{1}^{2}=W_{3}^{2}. From the equivalence classes determined by the 2-descent we get the class belonging to the triplet ( A, B, C) = ( 1,2,2) (A,B,C)=(1,2,2), which is a good candidate for yielding a homogeneous space having a rational point. The corresponding equations are

 | x + 142 = α 2, x = 2 ​ β 2, x − 3 ⋅ 142 = 2 ​ γ 2. x+142=\alpha^{2},\qquad x=2\beta^{2},\qquad x-3\cdot 142=2\gamma^{2}. |  | ( 27) |

These equations are equivalent to the following system of quadratic equations

 | Q 1: 3 ​ X 0 2 − 8 ​ X 1 2 + 2 ​ X 2 2 = 0, Q 2: X 0 2 − 2 ​ X 1 2 − 142 ​ X 3 2 = 0. Q_{1}:\ 3X_{0}^{2}-8X_{1}^{2}+2X_{2}^{2}=0,\qquad Q_{2}:\ X_{0}^{2}-2X_{1}^{2}-142X_{3}^{2}=0. |  | ( 28) |

Each of these equations individually possesses rational solutions; so the corresponding homogeneous space has a chance to have a rational point. We see that Q 1 Q_{1} has the rational point ( 0,1,2) (0,1,2), so the critical condition of section 4.2 is fulfilled. Parametrizing Q 1 Q_{1} with this point gives

 | X 0 = 16 ​ ξ 0 ​ ξ 1, X 1 = 8 ​ ξ 0 2 + 3 ​ ξ 1 2, X 2 = − 16 ​ ξ 0 2 + 6 ​ ξ 1 2. X_{0}\ =\ 16\xi_{0}\xi_{1},\qquad X_{1}\ =\ 8\xi_{0}^{2}+3\xi_{1}^{2},\qquad X_{2}\ =\ -16\xi_{0}^{2}+6\xi_{1}^{2}. |  | ( 29) |

Substituting the expressions for X 0 X_{0} and X 1 X_{1} in Q 2 Q_{2} and setting Y 0 = ξ 0 2 Y_{0}=\xi_{0}^{2}, Y 1 = ξ 1 2 Y_{1}=\xi_{1}^{2}, Y 2 = X 3 Y_{2}=X_{3} gives the quadric

 | Q 3: − 64 ​ Y 0 2 + 80 ​ Y 0 ​ Y 1 − 9 ​ Y 1 2 − 71 ​ Y 2 2 = 0. Q_{3}:\ -64Y_{0}^{2}+80Y_{0}Y_{1}-9Y_{1}^{2}-71Y_{2}^{2}\ =\ 0. |  | ( 30) |

The next step is to find a point on Q 3 Q_{3}. We find the point ( y 0, y 1, y 2) = ( 10,9,1) (y_{0},y_{1},y_{2})=(10,9,1). Parametrizing Q 3 Q_{3} using this point gives the following representations:

(31)

 |  | Y 0 \displaystyle Y_{0}\  |  | = Ψ 0 ​ ( η 0, η 1) \displaystyle=\ \Psi_{0}(\eta_{0},\eta_{1})\  |  | = − 90 ​ η 0 2 + 81 ​ η 0 ​ η 1 − 20 ​ η 1 2, \displaystyle=\ -90\eta_{0}^{2}+81\eta_{0}\eta_{1}-20\eta_{1}^{2}, |  |

 |  | Y 1 \displaystyle Y_{1}\  |  | = Ψ 1 ​ ( η 0, η 1) \displaystyle=\ \Psi_{1}(\eta_{0},\eta_{1})\  |  | = − 719 ​ η 0 2 + 640 ​ η 0 ​ η 1 − 144 ​ η 1 2, \displaystyle=\ -719\eta_{0}^{2}+640\eta_{0}\eta_{1}-144\eta_{1}^{2}, |  |

 |  | Y 2 \displaystyle Y_{2}\  |  | = Ψ 2 ​ ( η 0, η 1) \displaystyle=\ \Psi_{2}(\eta_{0},\eta_{1})\  |  | = − 9 ​ η 0 2 + 40 ​ η 0 ​ η 1 − 16 ​ η 1 2. \displaystyle=\ -9\eta_{0}^{2}+40\eta_{0}\eta_{1}-16\eta_{1}^{2}. |  |

Now we have to find an appropriate coefficient μ \mu which, according to the necessary condition from the linear system in 4.2.2, must divide D = 142 D=142. The only candidates for μ \mu which result in (individually) solvable quadratic equations Ψ 0 ​ ( η 0, η 1) = μ ​ σ 0 2 \Psi_{0}(\eta_{0},\eta_{1})=\mu\sigma_{0}^{2} and Ψ 1 ​ ( η 0, η 1) = μ ​ σ 1 2 \Psi_{1}(\eta_{0},\eta_{1})=\mu\sigma_{1}^{2} are μ = − 1 \mu=-1 and μ = − 71 \mu=-71. We do not have an a priori criterion which of these values to use for the following search, but must use trial and error. It turns out that μ = − 1 \mu=-1 does not yield a solution, but μ = − 71 \mu=-71 does. So let us consider this choice. According to the notations of section 4, we denote by Q 4 Q_{4} and Q 5 Q_{5} the quadratic equations Ψ 0 ​ ( η 0, η 1) = μ ​ σ 0 2 \Psi_{0}(\eta_{0},\eta_{1})=\mu\sigma_{0}^{2} and Ψ 1 ​ ( η 0, η 1) = μ ​ σ 1 2 \Psi_{1}(\eta_{0},\eta_{1})=\mu\sigma_{1}^{2}, respectively, where we rename the variables as follows: Z 0 = η 0 Z_{0}=\eta_{0}, Z 1 = η 1 Z_{1}=\eta_{1}, Z 2 = σ 0 Z_{2}=\sigma_{0}, Z 3 = σ 1 Z_{3}=\sigma_{1}. Thus we arrive at the following equations:

(32)

 |  | Q 4: \displaystyle Q_{4}: |  | − 90 ​ Z 0 2 + 81 ​ Z 0 ​ Z 1 − 20 ​ Z 1 2 + 71 ​ Z 2 2 \displaystyle\quad-90Z_{0}^{2}+81Z_{0}Z_{1}-20Z_{1}^{2}+71Z_{2}^{2}\  |  | = 0, \displaystyle=\ 0, |  |

 |  | Q 5: \displaystyle Q_{5}: |  | − 719 ​ Z 0 2 + 640 ​ Z 0 ​ Z 1 − 144 ​ Z 1 2 + 71 ​ Z 3 2 \displaystyle\quad-719Z_{0}^{2}+640Z_{0}Z_{1}-144Z_{1}^{2}+71Z_{3}^{2}\  |  | = 0. \displaystyle=\ 0. |  |

Again, we have to look for a point on Q 4 Q_{4}. We find the point ( z 0, z 1, z 2) = ( 4,1,4) (z_{0},z_{1},z_{2})=(4,1,4) and use this point to parametrize Q 4 Q_{4}. This yields

(33)

 |  | Z 0 \displaystyle Z_{0}\  |  | = Γ 0 ​ ( ρ 0, ρ 1) \displaystyle=\ \Gamma_{0}(\rho_{0},\rho_{1})\  |  | = − 5 ​ ρ 0 2 + 10 ​ ρ 0 ​ ρ 1 + 279 ​ ρ 1 2, \displaystyle=\ -5\rho_{0}^{2}+10\rho_{0}\rho_{1}+279\rho_{1}^{2}, |  |

 |  | Z 1 \displaystyle Z_{1}\  |  | = Γ 1 ​ ( ρ 0, ρ 1) \displaystyle=\ \Gamma_{1}(\rho_{0},\rho_{1})\  |  | = − 19 ​ ρ 0 2 + 180 ​ ρ 0 ​ ρ 1 − 90 ​ ρ 1 2, \displaystyle=\ -19\rho_{0}^{2}+180\rho_{0}\rho_{1}-90\rho_{1}^{2}, |  |

 |  | Z 2 \displaystyle Z_{2}\  |  | = Γ 2 ​ ( ρ 0, ρ 1) \displaystyle=\ \Gamma_{2}(\rho_{0},\rho_{1})\  |  | = − 5 ​ ρ 0 2 + 81 ​ ρ 0 ​ ρ 1 − 360 ​ ρ 1 2. \displaystyle=\ -5\rho_{0}^{2}+81\rho_{0}\rho_{1}-360\rho_{1}^{2}. |  |

Finally, we substitute the expressions for Z 0 Z_{0} and Z 1 Z_{1} into Q 5 Q_{5}; this yields:

 | Q 5: Ψ 1 ​ ( Z 0, Z 1) + 71 ​ Z 3 2 = − 9 159 ​ ρ 0 4 + 359 260 ​ ρ 0 3 ​ ρ 1 − 5 176 610 ​ ρ 0 2 ​ ρ 1 2 + 32 218 380 ​ ρ 0 ​ ρ 1 3 − 73 204 479 ​ ρ 1 4 + 71 ​ Z 3 2 = 0 Q_{5}:\ \begin{matrix}\Psi_{1}(Z_{0},Z_{1})+71Z_{3}^{2}\ =\ &-9\,159\,\rho_{0}^{4}+359\,260\,\rho_{0}^{3}\rho_{1}-5\,176\,610\rho_{0}^{2}\rho_{1}^{2}\phantom{\ =\ 0}\\ &+32\,218\,380\,\rho_{0}\rho_{1}^{3}-73\,204\,479\,\rho_{1}^{4}+71\,Z_{3}^{2}\ =\ 0\end{matrix} |  | ( 34) |

This last expression is the starting point for the final search loop. We look for integers ( ρ 0, ρ 1) (\rho_{0},\rho_{1}) such that

 | − 71 ​ Ψ 1 ​ ( Γ 0 ​ ( ρ 0, ρ 1), Γ 1 ​ ( ρ 0, ρ 1)) = − 9 159 ​ ρ 0 4 + 359 260 ​ ρ 0 3 ​ ρ 1 − 5 176 610 ​ ρ 0 2 ​ ρ 1 2 + 32 218 380 ​ ρ 0 ​ ρ 1 3 − 73 204 479 ​ ρ 1 4 \begin{matrix}-71\,\Psi_{1}(\Gamma_{0}(\rho_{0},\rho_{1}),\Gamma_{1}(\rho_{0},\rho_{1}))\ =\ &-9\,159\,\rho_{0}^{4}+359\,260\,\rho_{0}^{3}\rho_{1}-5\,176\,610\,\rho_{0}^{2}\rho_{1}^{2}\\ &+32\,218\,380\,\rho_{0}\rho_{1}^{3}-73\,204\,479\,\rho_{1}^{4}\end{matrix} |  | ( 35) |

is a perfect square. Having found such a pair of integers we can recover a solution of the original equations. Using ( ρ 0, ρ 1) = ( 20,3) (\rho_{0},\rho_{1})=(20,3), the right-hand side of (35) takes the value − 10633599 = − 71 ⋅ 387 2 -10633599=-71\cdot 387^{2}, so we have found a solution. With these values we find that

(36)

 |  | ( Z 0, Z 1, Z 2, Z 3) \displaystyle(Z_{0},Z_{1},Z_{2},Z_{3})\  |  | = ( 1111,2390, − 380,387) \displaystyle=\ (1111,2390,-380,387) |  |

 |  | ( Y 0, Y 1, Y 2) \displaystyle(Y_{0},Y_{1},Y_{2})\  |  | = ( − 10252400, − 10633599,3709111) \displaystyle=\ (-10252400,-10633599,3709111) |  |

 |  | ( X 0, X 1, X 2, X 3) \displaystyle(X_{0},X_{1},X_{2},X_{3})\  |  | = ( 2352960,1604507, − 1411786, − 52241) \displaystyle=\ (2352960,1604507,-1411786,-52241) |  |

which results in the point

 | ( x, y) = ( 5148885426098 2729122081, 10659946547134851840 142572066633521) (x,y)\ =\ \left(\frac{5148885426098}{2729122081},\frac{10659946547134851840}{142572066633521}\right) |  | ( 37) |

on the curve y 2 = x ⁡ ( x + 142) ​ ( x − 426) y^{2}=x(x+142)(x-426). The corresponding solution ( W 0, W 1, W 2, W 3) (W_{0},W_{1},W_{2},W_{3}) of the concordant form problem is given by

 | [W 0 W 1 W 2 W 3] = [− 1685098252492020382767601 69610783446108974371680 − 880513748494434998396401 − 1878201269026558326761999] \left[\begin{matrix}W_{0}\\ W_{1}\\ W_{2}\\ W_{3}\end{matrix}\right]\ =\ \left[\begin{matrix}-1685098252492020382767601\\ \phantom{-}69610783446108974371680\\ -880513748494434998396401\\ -1878201269026558326761999\end{matrix}\right] |  | ( 38) |

We note that the signs in this solution are not important; they arise from the isomorphism used between the elliptic curve and the quadric intersection defining the concordant form problem. Other distributions of signs correspond to other points on the elliptic curve; these other points are determined by adding any of the 2-torsion points of E 1,3,142 ​ ( ℚ) E_{1,3,142}(\mathbb{Q}) to the above solution. They are given by the following three points, together with their negatives (in the sense of the elliptic curve addition), which are obtained by reversing the sign of the y y -component:

(39)

 | ( x 1, y 1) \displaystyle(x_{1},y_{1}) | = \displaystyle= | ( − 82545026461926 2574442713049, 5248834080776243516160 4130711354186111843), \displaystyle\left(\frac{-82545026461926}{2574442713049},\frac{5248834080776243516160}{4130711354186111843}\right), |  |

 | ( x 2, y 2) \displaystyle(x_{2},y_{2}) | = \displaystyle= | ( 294814405555200 498284927449, 2982672665844557232960 351735842291756957), \displaystyle\left(\frac{294814405555200}{498284927449},\frac{2982672665844557232960}{351735842291756957}\right), |  |

 | ( x 3, y 3) \displaystyle(x_{3},y_{3}) | = \displaystyle= | ( − 35378229848879 346026297600, 298269379294025686631 203546509300224000). \displaystyle\left(\frac{-35378229848879}{346026297600},\frac{298269379294025686631}{203546509300224000}\right). |  |

Remarks. During the execution of the algorithm one has to make some choices, most of which are not very critical and do not affect the working of the algorithm. Examples of such choices are those of the points on the quadrics Q 1 Q_{1}, Q 3 Q_{3} and Q 4 Q_{4}, which are used for the parametrizations of these quadrics. Also, it is irrelevant whether one uses the quadric Q 4 Q_{4} for parametrization and substitution into Q 5 Q_{5} or whether one exchanges the roles of Q 4 Q_{4} and Q 5 Q_{5}. A more delicate task is the choice of the parameter μ \mu, for which we have no good suggestions. Note that using different parametrizations of the intermediate quadrics may affect the possible choices for this parameter μ \mu.

### 5.2 Some series of examples with similar behaviour

#### 5.2.1 Congruent prime numbers k ≡ 5 k\equiv 5 mod 8 8

Let k ∈ ℕ k\in\mathbb{N} be a prime number satisfying k ≡ 5 k\equiv 5 mod 8 8. Then k k is a congruent number, i.e., it is the area of a right triangle with rational sides. This is tantamount to saying that there are nontrivial rational points on the elliptic curve y 2 = x ⁡ ( x + k) ​ ( x − k) y^{2}=x(x+k)(x-k), and the corresponding concordant form problem is given by the equations W 0 2 − k ​ W 1 2 = W 2 2 W_{0}^{2}-kW_{1}^{2}=W_{2}^{2} and W 0 2 + k ​ W 1 2 = W 3 2 W_{0}^{2}+kW_{1}^{2}=W_{3}^{2}. The Mordell-Weil-rank of these curves is one, and rational points on these curves can be found by examining the 2-descent with parameters ( A, B, C) = ( 1, − 1, − 1) (A,B,C)=(1,-1,-1). The initial quadrics for the algorithm are given by

 | Q 1: 2 ​ X 0 2 + X 1 2 − X 2 2 = 0, Q 2: X 0 2 + X 1 2 − k ​ X 3 2 = 0. Q_{1}:\ 2X_{0}^{2}+X_{1}^{2}-X_{2}^{2}=0,\qquad Q_{2}:\ X_{0}^{2}+X_{1}^{2}-kX_{3}^{2}=0. |  | ( 40) |

The point ( 0,1,1) (0,1,1) is on Q 1 Q_{1} and can be used for the first parametrization. Appendix 1 provides a table which contains the results found for all prime numbers k ≡ 5 k\equiv 5 mod 8 8 up to 613 613 in terms of the solutions ( W 0, W 1, W 2, W 3) (W_{0},W_{1},W_{2},W_{3}) to the concordant form problem (with all the components being positive). The table shows (in the last column) also the logarithmic heights of the solutions found (with respect to the logarithm with base 10 10, i.e., the maximum number of decimal places of the solution). The following diagram shows the logarithmic heights depending on the prime numbers k k.

[image: [Uncaptioned image]]

#### 5.2.2 Diagrams of some other series

(a) The following diagram shows the heights of the solutions (in terms of the solutions ( W 0, W 1, W 2, W 3) (W_{0},W_{1},W_{2},W_{3}) of the concordant form problem) depending on the coefficients k k, where k k is a prime number satisfying k ≡ 7 k\equiv 7 mod 8 8.

[image: [Uncaptioned image]]

(b) The following diagram shows the logarithmic heights of the solutions to the congruent number problem for the numbers k = 2 ​ ℓ k=2\ell where ℓ \ell is a prime number satisfying ℓ ≡ 7 \ell\equiv 7 mod 8 8.

[image: [Uncaptioned image]]

(c) Finally, let us consider the 2 ​ π / 3 2\pi/3 -congruent number problem. This corresponds to the elliptic curves E 1,3, k E_{1,3,k} given by y 2 = x ⁡ ( x + k) ​ ( x − 3 ​ k) y^{2}=x(x+k)(x-3k). From [24] we know that prime numbers k ≡ 5 k\equiv 5 mod 24 24 are 2 ​ π / 3 2\pi/3 -congruent. The following diagram shows again the logarithmic heights of solutions in terms of the solutions to the corresponding concordant form problem.

[image: [Uncaptioned image]]

### 5.3 Special examples

Let r = 2 ​ ℓ r=2\ell where ℓ ∈ ℕ \ell\in\mathbb{N} is a prime number satisfying ℓ ≡ 7 \ell\equiv 7 mod 96 96. As in section 3, we consider the 2 ​ π / 3 2\pi/3 -congruent number problem for these numbers. The solution to this problem corresponds to determining the rational points on the elliptic curve y 2 = x ⁡ ( x + 2 ​ ℓ) ​ ( x − 6 ​ ℓ) y^{2}=x(x+2\ell)(x-6\ell), and the corresponding concordant form problem is given by the equations W 0 2 + 2 ​ ℓ ​ W 1 2 = W 2 2 W_{0}^{2}+2\ell W_{1}^{2}=W_{2}^{2} and W 0 2 − 6 ​ ℓ ​ W 1 2 = W 3 2 W_{0}^{2}-6\ell W_{1}^{2}=W_{3}^{2}. According to the considerations in section 3, we have a good chance to find rational solutions to this problem by examining the homogeneous spaces belonging to the 2-descent parameter sets ( A, B, C) = ( 1,2,2) (A,B,C)=(1,2,2), ( 2, − 3, − 6) (2,-3,-6) and ( 2, − 6, − 3) (2,-6,-3), where the solutions to the third parameter set are obtained as the sums of the solutions of the first two parameter sets in terms of the group structure of the elliptic curve. Appendix 2 shows the results obtained for the three examples ℓ = 7 \ell=7, ℓ = 103 \ell=103 and ℓ = 199 \ell=199. For the concordant form we only exhibit the solution with positive coefficients; in addition, we list the four points on the elliptic curve with positive y y -coordinates which correspond to the concordant form solutions obtained by changing the signs of the coefficients (which means adding 2-torsion points on the elliptic curve).

## 6 Concluding remarks and open questions

The algorithm described in section 4 provides us with a tool to find explicit solutions to elliptic curve equations of a special form. This algorithm improves a simpler strategy which is probably well known to the experts and which is based on a classical 2-descent procedure together with a parametrization scheme for quadratic forms. As was shown by way of various examples, the algorithm works quite well in many situations. However, there are certain points which are not fully understood, and these open questions are addressed in this final section.

### 6.1 Choices within the algorithm

The algorithm applies to elliptic curves with full 2-torsion ℤ / 2 ​ ℤ × ℤ / 2 ​ ℤ \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}. It requires the validity of a certain condition which seems to be of a purely technical nature; namely, we assumed that the homogeneous space leading to a solution of the elliptic curve equation can be given by two diagonal quadrics with separated variables in the form

(41)

 |  | Q 1: \displaystyle Q_{1}: |  | a 00 ​ X 0 2 + a 11 ​ X 1 2 + a 22 ​ X 2 2 \displaystyle\quad a_{00}X_{0}^{2}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2}\  |  | = 0 \displaystyle=\ 0 |  |

 |  | Q 2: \displaystyle Q_{2}: |  | b 00 ​ X 0 2 + b 11 ​ X 1 2 + b 33 ​ X 3 2 \displaystyle\quad b_{00}X_{0}^{2}+b_{11}X_{1}^{2}+b_{33}X_{3}^{2}\  |  | = 0 \displaystyle=\ 0 |  |

such that at least one of the equations (without loss of generality the first one) has a solution of the form ( 0, x 1, x 2) (0,x_{1},x_{2}) or ( x 0 ​,0, x 2) (x_{0},0,x_{2}). However, this condition is not always fulfilled, as is shown by the following example.

Let k k be a prime number congruent to 23 23 modulo 24 24. Then, assuming the validity of the Birch-Swinnerton-Dyer Conjecture, the elliptic curve E 1,3, k E_{1,3,k} has positive rank ( \bigl( cf. [24], section 3, expectation (e1)) \bigr); in fact, we expect the rank of this curve to be one. Let us consider the special case k = 23 k=23. Then by the 2-descent procedure we find the triplet ( A, B, C) = ( 2,3,6) (A,B,C)=(2,3,6) to determine a homogeneous space having a rational solution. The four quadrics which are determined by this triplet according to 4.2.1 are given by

(42)

 |  | 0 \displaystyle 0\  |  | = X 0 2 − 2 ​ X 1 2 + X 2 2 \displaystyle=\ X_{0}^{2}-2X_{1}^{2}+X_{2}^{2} |  |

 |  | 0 \displaystyle 0\  |  | = 2 ​ X 0 2 − 3 ​ X 1 2 − 23 ​ X 3 2 \displaystyle=\ 2X_{0}^{2}-3X_{1}^{2}-23X_{3}^{2}\  |  | = 2 ​ X 0 2 − 3 ​ X 1 2 − k ​ X 3 2 \displaystyle=\ 2X_{0}^{2}-3X_{1}^{2}-kX_{3}^{2} |  |

 |  | 0 \displaystyle 0\  |  | = X 0 2 − 3 ​ X 2 2 − 46 ​ X 3 2 \displaystyle=\ X_{0}^{2}-3X_{2}^{2}-46X_{3}^{2}\  |  | = X 0 2 − 3 ​ X 2 2 − 2 ​ k ​ X 3 2 \displaystyle=\ X_{0}^{2}-3X_{2}^{2}-2kX_{3}^{2} |  |

 |  | 0 \displaystyle 0\  |  | = X 1 2 − 2 ​ X 2 2 − 23 ​ X 3 2 \displaystyle=\ X_{1}^{2}-2X_{2}^{2}-23X_{3}^{2}\  |  | = X 1 2 − 2 ​ X 2 2 − k ​ X 3 2 \displaystyle=\ X_{1}^{2}-2X_{2}^{2}-kX_{3}^{2} |  |

and it is easy to see that none of these equations has an integer solution with one component being 0 0. However, ( 7,5,1,1) (7,5,1,1) is a solution for this system of quadratic equations, and this solution determines for example the point ( 75,210) (75,210) on the elliptic curve E 1,3,23 E_{1,3,23}. The same equations yield solutions for other values of k k, for example k = 47,71,167,191,239,263,311,359,383,431,479,503,599 k=47,71,167,191,239,263,311,359,383,431,479,503,599.

Note that for any of the triplets ( A ′, B ′, C ′) (A^{\prime},B^{\prime},C^{\prime}) which are equivalent to ( 2,3,6) (2,3,6) with respect to the 2-torsion points, the critical condition is not satisfied either; hence we cannot apply the strong form of the algorithm to find rational points on the curves of the form E 1,3, k E_{1,3,k} with prime numbers k ≡ 23 k\equiv 23 modulo 24 24.

Question: Is there a geometric or arithmetic interpretation of the above condition?

During the execution of the algorithm we have to make some choices, some of which cause no problems at all whereas others need to be treated carefully.

1. We have to choose an appropriate homogeneous space leading to a solution. There are at least the homogeneous spaces being P P -equivalent in the sense of section 2, where P P is the set of 2-torsion points on the elliptic curve. The choice of different spaces should yield different solutions which are in the same residue class with respect to the 2-torsion subgroup.

2. In several situations we have to choose a point on a quadric for defining a parametrization of that quadric. Since the parametrizations always determine all rational points on that quadric, the choice of the point is irrelevant. However, the solutions found by choosing different points may arise in different succession.

3. At a sensitive point of the algorithm, we have to choose a factor μ \mu which determines the “right” representative of a point in projective space to have square coefficients. We have determined a finite set of possibilities for this choice, and we can exclude many of the potential candidates by simple arguments. However, for the remaining possibilities we have no guidelines which of the candidates may give rise to a solution, and hence resort to a trial-and-error approach.

Question: Is there a geometric or arithmetic interpretation of this factor which may lead to a better way of choosing this factor?

### 6.2 Qualities of the algorithm

Summarizing the observations made in section 4, we see that a search within the algorithm in which the parameters ρ 0 \rho_{0} and ρ 1 \rho_{1} of the central loop are considered up to logarithmic height n n, the solutions will have logarithmic height of about 12 ​ n 12n. Hence a search with parameters up to around 10 000 10\,000 is expected to find solutions with about 50 decimal places. Such a search can be performed with a usual personal computer in a few minutes. However, as mentioned in section 4, the complexity of the algorithm grows quadratically with the parameters ( ρ 0, ρ 1) (\rho_{0},\rho_{1}). Hence a search in a parameter range of up to 100 000 100\,000, which could provide solution with about 70 70 decimal places, would already take several hours.

In spite of this complexity defect, the examples of section 5 show that we can generate enough data to obtain interesting information on the behaviour of the smallest solutions found by the algorithm, depending on the coefficients of the original elliptic curves. Of course the data are too sparse to lead to serious conjectures. Nevertheless, the diagrams in section 5 suggest that for the families considered there may be a linear correlation between the parameters defining the curves and the logarithmic height of the smallest solutions. We are far from being able to formulate such a suspected correlation in more precise terms.

### 6.3 Structural questions

The central point in both the weak as well as the strong version of the algorithm is the consideration of a suitable homogeneous space Q Q over the given elliptic curve E E. Such a homogeneous space is geometrically (i.e. over an algebraic closure of ℚ \mathbb{Q}) isomorphic to E E. It is trivial (in the sense of the Weil-Chatelet group) if and only if it contains a rational point, and in this situation it is isomorphic over ℚ \mathbb{Q} to some rationally defined elliptic curve E Q E_{Q}. Via the well known construction of Nagell (cf. [15]) we can define a biregular mapping from Q Q to E Q E_{Q} given by a Weierstraß equation.

Question: What can be said about this elliptic curve?

We observe that if rank ( E Q ​ ( ℚ)) > 0 (E_{Q}(\mathbb{Q}))>0 we obtain an infinite series of rational points on E E by considering the composition of an isomorphism of Q Q to E Q E_{Q} and the mapping from Q Q to E E given in section 2. Obviously, independent rational points on E Q ​ ( ℚ) E_{Q}(\mathbb{Q}) will determine independent points on E ⁡ ( ℚ) E(\mathbb{Q}). So we certainly have rk ​ ( E Q ​ ( ℚ)) ≤ rk ​ ( E ⁡ ( ℚ)) \hbox{rk}(E_{Q}(\mathbb{Q}))\leq\hbox{rk}(E(\mathbb{Q})). In the examples of section 5 two cases occurred.

- •

There were examples with rk ​ ( E ​ ( ℚ)) = 1 \hbox{rk}(E(\mathbb{Q}))=1, and hence for the choosen homogeneous space to yield a solution of infinite order we also had necessarily rk ​ ( E Q ​ ( ℚ)) = 1 \hbox{rk}(E_{Q}(\mathbb{Q}))=1.

- •

There were examples with rk ​ ( E ​ ( ℚ)) = 2 \hbox{rk}(E(\mathbb{Q}))=2, and in these examples invariably all the homogeneous spaces Q Q considered for finding solutions on E ⁡ ( ℚ) E(\mathbb{Q}) were such that rk ​ ( E Q ​ ( ℚ)) = 1 \hbox{rk}(E_{Q}(\mathbb{Q}))=1. Hence to find independent solutions we had to look for two different (and non-equivalent with respect to 2-torsion points) homogeneous spaces.

Question: Are there examples in which rk ​ ( E Q ​ ( ℚ)) > 1 \hbox{rk}(E_{Q}(\mathbb{Q}))>1?

Let us again consider the case in which rk ​ ( E ​ ( ℚ)) ≥ 2 \hbox{rk}(E(\mathbb{Q}))\geq 2, and let Q Q and Q ′ Q^{\prime} be two independent homogeneous spaces yielding independent rational solutions on E ⁡ ( ℚ) E(\mathbb{Q}). Then the associated rationally defined elliptic curves E Q E_{Q} and E Q ′ E_{Q^{\prime}} are twists of one another (and twists of the original curve E E as well).

Question: What can be said about the connection between these two elliptic curves?

### 6.4 Further outlook

The algorithm above was developed for the class of elliptic curves E E with full 2-torsion, which means that the torsion subgroup of E E contains ℤ / 2 ​ ℤ × ℤ / 2 ​ ℤ \mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}. Equivalently, the curves considered can be given in affine form by a Weierstraß equation with split polynomial in the form y 2 = ( x − e 1) ​ ( x − e 2) ​ ( x − e 3) y^{2}=(x-e_{1})(x-e_{2})(x-e_{3}) where e 1, e 2, e 3 ∈ ℚ e_{1},e_{2},e_{3}\in\mathbb{Q} are pairwise different. It would be of interest to develop algorithms for other classes of elliptic curves with positive rank. Note that the 2-descent procedure may always be formulated in the same way as in section 2, but over some number field instead of ℚ \mathbb{Q}. One could try to develop an algorithm over such a number field and then, a fortiori, try to extract those solutions which are actually rational. Alternatively, one could try to reformulate the 2-descent procedure (at least in special cases) such that a rationally defined algorithm can be developed. Both strategies seem to be not entirely trivial.

Hagen Knaf, Karlheinz Spindler Hochschule RheinMain, Germany Applied Mathematics hagen.knaf@hs-rm.de, karlheinz.spindler@hs-rm.de

Erich Selder Frankfurt University of Applied Sciences, Germany Computer Science and Engineering e_selder@fb2.fra-uas.de

## 7 References

1. 1.

Andrew Bremner, John William Scott Cassels, *On the equation Y 2 = X ⁡ ( X 2 + p) Y^{2}=X(X^{2}+p)*, Mathematics of Computation, Vol. 42, No. 165, 1984, pp. 257–264.

2. 2.

John William Scott Cassels, *Lectures on Elliptic Curves*, London Mathematical Society Students Texts vol. 24, London 1991.

3. 3.

Leonhard Euler, *De binis formulis speciei xx+myy et xx+nyy inter se concordibus et discordibus*, Mem. Acad. Sci. St.-Petersbourg 1780 (Opera Omnia: Ser. 1, Vol. 5, pp. 406–413).

4. 4.

Masahiko Fujiwara, *θ \theta -congruent numbers*, in: K. Györy et al. (eds.), *Number theory*, de Gruyter, Berlin 1998, pp. 235–241.

5. 5.

Masahiko Fujiwara, *Some properties of θ \theta -congruent numbers*, Natural Science Report, Ochanomizu University, vol. 52, no. 2, 2001.

6. 6.

Ludwig Holzer, *Minimal solutions of diophantine equations*, Canad. J. Math. 2, 1950, pp. 238–244.

7. 7.

Makiko Kan, *θ \theta -congruent numbers and elliptic curves*, Acta Arithmetica 94 (2), 2000, pp. 153–160.

8. 8.

Anthony W. Knapp, *Elliptic Curves*, Mathematical Notes 40, Princeton University Press 1992.

9. 9.

Neal Koblitz, *Introduction to Elliptic Curves and Modular Forms*, Springer, New York/Berlin/Heidelberg 1993.

10. 10.

Adrien-Marie Le Gendre, *Recherches d’Analyse indéterminée*, Histoire de l’Académie Royale des Sciences 1785, pp. 465–559.

11. 11.

Elisabeth Lutz, *Sur l’équation y 2 = x 3 − A ​ x − B y^{2}=x^{3}-Ax-B dans les corps p p -adiques*, J. Reine Angew. Mathematik 177 (1937), pp. 237–247.

12. 12.

Barry Charles Mazur, *Modular curves and the Eisenstein ideal*, Publications mathématiques de l’I.H.E.S 47 (2), 1977, pp. 33–186.

13. 13.

Louis Joel Mordell, On the Rational Solutions of the Indeterminate Equations of the Third and Fourth Degrees, Proc. Cambridge Phil. Soc. XXI, 1922, pp. 179–192.

14. 14.

Louis Joel Mordell, *On the Magnitude of the Integer Solutions of the Equation a ​ x 2 + b ​ y 2 + c ​ z 2 = 0 ax^{2}+by^{2}+cz^{2}=0*, J. Number Theory 1, 1969, pp. 1–3.

15. 15.

Trygve Nagell, *Sur les propriétés arithmétiques des cubiques planes du premier genre*, Acta Mathematica 52 (1928), pp. 93–126.

16. 16.

Trygve Nagell, *Solution de quelques problèmes dans la théorie arithmétique des cubiques planes du premier genre*, Wid. Akad. Skrifter I, (1), 1935.

17. 17.

Ken Ono, *Euler’s Concordant Forms*, Acta arithmetica LXXVIII (2), 1996, pp. 101–123.

18. 18.

Takashi Ono, *Variations on a Theme of Euler*, Plenum Press, New York and London 1994.

19. 19.

Erich Selder, Karlheinz Spindler, *On θ \theta -congruent numbers, rational squares in arithmetic progressions, concordant forms and elliptic curves*, Mathematics 3(1), 2015, pp. 2–15.

20. 20.

Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, Springer 2009.

21. 21.

Joseph H. Silverman, J. Tate, *Rational Points on Elliptic Curves*, Springer, New York 1992.

22. 22.

André Weil: *Sur un théorème de Mordell*, Bull. Sci. Math. 2 (54), 1930, pp. 182–191.

23. 23.

Kenneth S. Williams, *On the Size of a Solution of Legendre’s Equation*, Utilitas Mathematica 34, 1988, pp. 65–72.

24. 24.

Shin-ichi Yoshida, *Some Variants of the Congruent Number Problem I*, Kyushu J. Math. 55 (2001), pp. 387–404.

25. 25.

Don Bernard Zagier, *Elliptische Kurven: Fortschritte und Anwendungen*, JBer. DMV 92 (1990), pp. 58–76.

Table 1: Solutions to the system W 0 2 − k ​ W 1 2 = W 2 2 W_{0}^{2}-kW_{1}^{2}=W_{2}^{2}, W 0 2 + k ​ W 1 2 = W 3 2 W_{0}^{2}+kW_{1}^{2}=W_{3}^{2}
where k k is prime with k ≡ 5 k\equiv 5 mod 8 8
k k W 0, W 1, W 2, W 3 W_{0},W_{1},W_{2},W_{3} log hgt 5 5 W 0 = 41 W_{0}=41 2 2 W 1 = 12 W_{1}=12 W 2 = 31 W_{2}=31 W 3 = 49 W_{3}=49 13 13 W 0 = 106921 W_{0}=106921 6 6 W 1 = 19380 W_{1}=19380 W 2 = 80929 W_{2}=80929 W 3 = 127729 W_{3}=127729 29 29 W 0 = 48029801 W_{0}=48029801 8 8 W 1 = 180180 W_{1}=180180 W 2 = 48019999 W_{2}=48019999 W 3 = 48039601 W_{3}=48039601 37 37 W 0 = 605170417321 W_{0}=605170417321 12 12 W 1 = 9475102140 W_{1}=9475102140 W 2 = 602419674529 W_{2}=602419674529 W 3 = 607908713329 W_{3}=607908713329 53 53 W 0 = 4850493897329785961 W_{0}=4850493897329785961 19 19 W 1 = 595711308569957580 W_{1}=595711308569957580 W 2 = 2172343665411286111 W_{2}=2172343665411286111 W 3 = 6506573990620136689 W_{3}=6506573990620136689 61 61 W 0 = 250510625883241 W_{0}=250510625883241 15 15 W 1 = 18295510698660 W_{1}=18295510698660 W 2 = 205760310228191 W_{2}=205760310228191 W 3 = 288398755364209 W_{3}=288398755364209 101 101 W 0 = 2015242462949760001961 W_{0}=2015242462949760001961 22 22 W 1 = 118171431852779451900 W_{1}=118171431852779451900 W 2 = 1628124370727269996961 W_{2}=1628124370727269996961 W 3 = 2339148435306225006961 W_{3}=2339148435306225006961 109 109 W 0 = 10537321 W_{0}=10537321 8 8 W 1 = 872340 W_{1}=872340 W 2 = 5299871 W_{2}=5299871 W 3 = 13927729 W_{3}=13927729 149 149 W 0 = 11880808361 W_{0}=11880808361 11 11 W 1 = 879612300 W_{1}=879612300 W 2 = 5086222111 W_{2}=5086222111 W 3 = 16013667889 W_{3}=16013667889 157 157 W 0 = 224403517704336969924557513090674863160948472041 W_{0}=224403517704336969924557513090674863160948472041 48 48 W 1 = 17824664537857719176051070357934327140032961660 W_{1}=17824664537857719176051070357934327140032961660 W 2 = 21796977171070247104112455266586147721935979809 W_{2}=21796977171070247104112455266586147721935979809 W 3 = 316605068345983991287469841722668300352741098609 W_{3}=316605068345983991287469841722668300352741098609

k k | W 0, W 1, W 2, W 3 W_{0},W_{1},W_{2},W_{3} | log |

 |  | hgt |

173 173 | W 0 = 11389552969201600543101928087171460571651881 W_{0}=11389552969201600543101928087171460571651881 | 44 44 |

 | W 1 = 151819892495256080406058239068697733204020 W_{1}=151819892495256080406058239068697733204020 |  |

 | W 2 = 11213134773123931932373766469330799882824031 W_{2}=11213134773123931932373766469330799882824031 |  |

 | W 3 = 11563279908237839493160911313667068050342769 W_{3}=11563279908237839493160911313667068050342769 |  |

181 181 | W 0 = 10940671490772286441 W_{0}=10940671490772286441 | 20 20 |

 | W 1 = 812534430489915900 W_{1}=812534430489915900 |  |

 | W 2 = 447084261166681441 W_{2}=447084261166681441 |  |

 | W 3 = 15465985290352891441 W_{3}=15465985290352891441 |  |

197 197 | W 0 = 3976155246560604347409241506281 W_{0}=3976155246560604347409241506281 | 31 31 |

 | W 1 = 128879379273797845692300739620 W_{1}=128879379273797845692300739620 |  |

 | W 2 = 3540856019037985665622394486369 W_{2}=3540856019037985665622394486369 |  |

 | W 3 = 4368290253857372604620867723569 W_{3}=4368290253857372604620867723569 |  |

229 229 | W 0 = 764646440211958998267241 W_{0}=764646440211958998267241 | 24 24 |

 | W 1 = 9404506457489780613180 W_{1}=9404506457489780613180 |  |

 | W 2 = 751285786287393798649441 W_{2}=751285786287393798649441 |  |

 | W 3 = 777777618847556210645041 W_{3}=777777618847556210645041 |  |

269 269 | W 0 = 3895373414239011964782976279255856376333539432681 W_{0}=3895373414239011964782976279255856376333539432681 | 49 49 |

 | W 1 = 27965347900755720997936131300398362642863770100 W_{1}=27965347900755720997936131300398362642863770100 |  |

 | W 2 = 3868276064680043715910003459047778706397631593569 W_{2}=3868276064680043715910003459047778706397631593569 |  |

 | W 3 = 3922283564474102177246930010978679686556478603569 W_{3}=3922283564474102177246930010978679686556478603569 |  |

277 277 | W 0 = 225651876701966818406248027783418906721100922839903398228891241 W_{0}=225651876701966818406248027783418906721100922839903398228891241 | 63 63 |

 | W 1 = 7177227596170451913324498105378376615737197106454374393982740 W_{1}=7177227596170451913324498105378376615737197106454374393982740 |  |

 | W 2 = 191441323585574742208871474928771109013368200999037188254008609 W_{2}=191441323585574742208871474928771109013368200999037188254008609 |  |

 | W 3 = 255318934946162061510445203213880843051935526236604388007831409 W_{3}=255318934946162061510445203213880843051935526236604388007831409 |  |

293 293 | W 0 = 464650359520278159096671986562151812257229902698281 W_{0}=464650359520278159096671986562151812257229902698281 | 51 51 |

 | W 1 = 9525532939264666216445930388515870770466775878580 W_{1}=9525532939264666216445930388515870770466775878580 |  |

 | W 2 = 435102716279337902002156546716850448714905366022431 W_{2}=435102716279337902002156546716850448714905366022431 |  |

 | W 3 = 492428207448547244972204796522699373235322337048369 W_{3}=492428207448547244972204796522699373235322337048369 |  |

317 317 | W 0 = 7704952068030240987029060443439470576691561 W_{0}=7704952068030240987029060443439470576691561 | 43 43 |

 | W 1 = 273033470936425799912142469450375693280340 W_{1}=273033470936425799912142469450375693280340 |  |

 | W 2 = 5977859131736779268748519442377486506296289 W_{2}=5977859131736779268748519442377486506296289 |  |

 | W 3 = 9110311352659588118420210652872068714343089 W_{3}=9110311352659588118420210652872068714343089 |  |

349 349 | W 0 = 543117687145297245481 W_{0}=543117687145297245481 | 21 21 |

 | W 1 = 24479594709742323420 W_{1}=24479594709742323420 |  |

 | W 2 = 292981872551143852319 W_{2}=292981872551143852319 |  |

 | W 3 = 710010751000672703281 W_{3}=710010751000672703281 |  |

373 373 | W 0 = 6464736286838262275566375140640125524476830394378258160144359151221846588162921 W_{0}=6464736286838262275566375140640125524476830394378258160144359151221846588162921 | 79 79 |

 | W 1 = 214402886988423616335778394508029972671920911384749815755228436417174376951980 W_{1}=214402886988423616335778394508029972671920911384749815755228436417174376951980 |  |

 | W 2 = 4964526988887992094202607668810309975770378526931158358479760499172740751760929 W_{2}=4964526988887992094202607668810309975770378526931158358479760499172740751760929 |  |

 | W 3 = 7677180621382399924131415436519959747090354653821331133153517438341892919535729 W_{3}=7677180621382399924131415436519959747090354653821331133153517438341892919535729 |  |

k k | W 0, W 1, W 2, W 3 W_{0},W_{1},W_{2},W_{3} | log |

 |  | hgt |

389 389 | W 0 = 7091795623967975164665712219283669343892955896357711001321 W_{0}=7091795623967975164665712219283669343892955896357711001321 | 58 58 |

 | W 1 = 178471843490509327250771615016308845953260187406885241100 W_{1}=178471843490509327250771615016308845953260187406885241100 |  |

 | W 2 = 6156546092792523632766658624365628021678212406860376224929 W_{2}=6156546092792523632766658624365628021678212406860376224929 |  |

 | W 3 = 7917327235348034759843187663340785352885655138147390834929 W_{3}=7917327235348034759843187663340785352885655138147390834929 |  |

397 397 | W 0 = 40610678141909645597145961 W_{0}=40610678141909645597145961 | 26 26 |

 | W 1 = 897770616925261772023980 W_{1}=897770616925261772023980 |  |

 | W 2 = 36458857951695016208049311 W_{2}=36458857951695016208049311 |  |

 | W 3 = 44375737009650677093379889 W_{3}=44375737009650677093379889 |  |

421 421 | W 0 = 206116218357279640098356283784343401 W_{0}=206116218357279640098356283784343401 | 36 36 |

 | W 1 = 5615337183197656507592648081062140 W_{1}=5615337183197656507592648081062140 |  |

 | W 2 = 170906168853566716230403514501943649 W_{2}=170906168853566716230403514501943649 |  |

 | W 3 = 236133166640367788597694235239072049 W_{3}=236133166640367788597694235239072049 |  |

461 461 | W 0 = 3891001511194439641326936071293799433960980792636201 W_{0}=3891001511194439641326936071293799433960980792636201 | 52 52 |

 | W 1 = 141603906393919705341026008387612184428936054638300 W_{1}=141603906393919705341026008387612184428936054638300 |  |

 | W 2 = 2428183393618185294158471720281132279464765769008799 W_{2}=2428183393618185294158471720281132279464765769008799 |  |

 | W 3 = 4937986525618685709148575673193534971677351329281201 W_{3}=4937986525618685709148575673193534971677351329281201 |  |

509 509 | W 0 = 8234822441 W_{0}=8234822441 | 11 11 |

 | W 1 = 358112820 W_{1}=358112820 |  |

 | W 2 = 1592388641 W_{2}=1592388641 |  |

 | W 3 = 11536416241 W_{3}=11536416241 |  |

541 541 | W 0 = 20712649137553815516771958538277092457342029080681 W_{0}=20712649137553815516771958538277092457342029080681 | 50 50 |

 | W 1 = 692383596502537714323160801078335881010146641980 W_{1}=692383596502537714323160801078335881010146641980 |  |

 | W 2 = 13025402685121753757242473560733781819142094311519 W_{2}=13025402685121753757242473560733781819142094311519 |  |

 | W 3 = 26236740527002218360424469656173951317763934832881 W_{3}=26236740527002218360424469656173951317763934832881 |  |

557 557 | W 0 = 5499709076648565793208509282424464890877481 W_{0}=5499709076648565793208509282424464890877481 | 43 43 |

 | W 1 = 73405451625480094969934137800528933306420 W_{1}=73405451625480094969934137800528933306420 |  |

 | W 2 = 5219720607933421868366276874910516409140831 W_{2}=5219720607933421868366276874910516409140831 |  |

 | W 3 = 5766117986189355551406701674738483083808369 W_{3}=5766117986189355551406701674738483083808369 |  |

613 613 | W 0 = 18030067140713632672003110416838548155838466663510382251241 W_{0}=18030067140713632672003110416838548155838466663510382251241 | 59 59 |

 | W 1 = 184995021722032435269683407294072813709395011761171749380 W_{1}=184995021722032435269683407294072813709395011761171749380 |  |

 | W 2 = 17438592982424790791434179315233932893903828538097188624609 W_{2}=17438592982424790791434179315233932893903828538097188624609 |  |

 | W 3 = 18602744877856272407302202226070441326874205450445721695409 W_{3}=18602744877856272407302202226070441326874205450445721695409 |  |

Table 2: Solutions to the system W 0 2 + 2 ​ ℓ ​ W 1 2 = W 2 2 W_{0}^{2}+2\ell W_{1}^{2}=W_{2}^{2}, W 0 2 − 6 ​ ℓ ​ W 1 2 = W 3 2 W_{0}^{2}-6\ell W_{1}^{2}=W_{3}^{2}
and to the equation y 2 = x ⁡ ( x + 2 ​ ℓ) ​ ( x − 6 ​ ℓ) y^{2}=x(x+2\ell)(x-6\ell) where ℓ ∈ { 7, 103, 199 } \ell\in\{7,\,103,\,199\}
l l ( A, B, C) (A,B,C) W 0, W 1, W 2, W 3 W_{0},W_{1},W_{2},W_{3} ( x, y) (x,y) 7 7 ( 1,2,2) (1,2,2) W 0 = 193 W_{0}=193 ( 50,160) (50,160) W 1 = 20 W_{1}=20 ( − 294 / 25, − 4705 / 125) (-294/25,-4705/125) W 2 = 207 W_{2}=207 ( 336,5880) (336,5880) W 3 = 143 W_{3}=143 ( − 7 / 4,245 / 8) (-7/4,245/8) 7 7 ( 2, − 3, − 6) (2,-3,-6) W 0 = 61 W_{0}=61 ( − 12,36) (-12,36) W 1 = 6 W_{1}=6 ( 49,147) (49,147) W 2 = 65 W_{2}=65 ( 378,7056) (378,7056) W 3 = 47 W_{3}=47 ( − 14 / 9,784 / 27) (-14/9,784/27) 7 7 ( 2, − 6, − 3) (2,-6,-3) W 0 = 13 W_{0}=13 ( − 6,48) (-6,48) W 1 = 2 W_{1}=2 ( 98,784) (98,784) W 2 = 15 W_{2}=15 ( 84,588) (84,588) W 3 = 1 W_{3}=1 ( − 7,49) (-7,49) 103 103 ( 1,2,2) (1,2,2) W 0 = 14497255873 W_{0}=14497255873 ( − 3757543 33124, 16707000155 6028568) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{-3757543}{33124},\frac{16707000155}{6028568}) W 1 = 573225380 W_{1}=573225380 ( 40941264 36481, 191037111720 6967871) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{40941264}{36481},\frac{191037111720}{6967871}) W 2 = 16669115727 W_{2}=16669115727 ( 470450 289, 269753120 4913) (\vphantom{\frac{\int^{b}}{\int_{a}}}\frac{470450}{289},\frac{269753120}{4913}) W 3 = 2665230577 W_{3}=2665230577 ( − 18396006 235225, 300932687328 114084125) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{-18396006}{235225},\frac{300932687328}{114084125}) 103 103 ( 2, − 3, − 6) (2,-3,-6) W 0 = 11581 W_{0}=11581 ( − 108,2772) (-108,2772) W 1 = 462 W_{1}=462 ( 10609 / 9,816893 / 27) (10609/9,816893/27) W 2 = 13345 W_{2}=13345 ( 74778 / 49,16804656 / 343) (74778/49,16804656/343) W 3 = 1487 W_{3}=1487 ( − 10094 / 121,3564624 / 1331) (-10094/121,3564624/1331) 103 103 ( 2, − 6, − 3) (2,-6,-3) W 0 = 8487373 W_{0}=8487373 ( − 103 / 841, − 3044783 / 24389) (-103/841,-3044783/24389) W 1 = 16646 W_{1}=16646 ( 1039476,1059584484) (1039476,1059584484) W 2 = 8490735 W_{2}=8490735 ( 1039682 / 1681,34458032 / 68921) (1039682/1681,34458032/68921) W 3 = 8477279 W_{3}=8477279 ( − 10086 / 49,57072 / 343) (-10086/49,57072/343) 198 198 ( 1,2,2) (1,2,2) W 0 = 58653195191109140161 W_{0}=58653195191109140161 ( 28710309938 15499969, 3196495762009760 61023377953) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{28710309938}{15499969},\frac{3196495762009760}{61023377953}) W 1 = 1573075476879053140 W_{1}=1573075476879053140 ( − 3682885634214 14355154969, 12478518082656282720 1719934182300797) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{-3682885634214}{14355154969},\frac{12478518082656282720}{1719934182300797}) W 2 = 66521235373358303439 W_{2}=66521235373358303439 ( − 253808255431 2179956100, 667116748338909653 101782150309000) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{-253808255431}{2179956100},\frac{667116748338909653}{101782150309000}) W 3 = 22035538516500689039 W_{3}=22035538516500689039 ( 5205735166800 1275418369, 10465997585174146680 45549016212097) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{5205735166800}{1275418369},\frac{10465997585174146680}{45549016212097}) 198 198 ( 2, − 3, − 6) (2,-3,-6) W 0 = 255711950171342941 W_{0}=255711950171342941 ( − 496910700 2436721, 28292464294380 3803721481) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{-496910700}{2436721},\frac{28292464294380}{3803721481}) W 1 = 7360756127254530 W_{1}=7360756127254530 ( 96496588321 41409225, 22649052322875419 266468362875) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{96496588321}{41409225},\frac{22649052322875419}{266468362875}) W 2 = 294877147817303041 W_{2}=294877147817303041 ( 677864759226 236452129, 454954755901005360 3635924387633) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{677864759226}{236452129},\frac{454954755901005360}{3635924387633}) W 3 = 26397138616197359 W_{3}=26397138616197359 ( − 94107947342 567725929, 97869913424403120 13527205710283) \vphantom{\frac{\int^{b}}{\int_{a}}}(\frac{-94107947342}{567725929},\frac{97869913424403120}{13527205710283}) 198 198 ( 2, − 6, − 3) (2,-6,-3) W 0 = 9901 W_{0}=9901 ( − 6,1680) (-6,1680) W 1 = 70 W_{1}=70 ( 79202,22176560) (79202,22176560) W 2 = 9999 W_{2}=9999 ( 59700 / 49,2376060 / 343) (59700/49,2376060/343) W 3 = 9601 W_{3}=9601 ( − 9751 / 25,277207 / 125) (-9751/25,277207/125)


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
