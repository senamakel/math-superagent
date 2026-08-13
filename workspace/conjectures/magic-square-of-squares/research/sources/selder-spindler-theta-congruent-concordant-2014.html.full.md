<!-- source: https://arxiv.org/html/1408.1522v2 | converted from HTML -->

On θ -congruent numbers, rational squares in arithmetic progressions, concordant forms and elliptic curves

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1408.1522v2 [math.NT] 22 Aug 2014

# On θ \theta -congruent numbers, rational squares in arithmetic progressions, concordant forms and elliptic curves

Erich Selder Affiliation: Fachhochschule Frankfurt Affiliation: D - 60318 Frankfurt am Main, Germany Affiliation: E-mail: e ¯ \underline{\phantom{e}} selder@fb2.fh-frankfurt.de Karlheinz Spindler Affiliation: Hochschule RheinMain Affiliation: D - 65197 Wiesbaden, Germany Affiliation: E-mail: karlheinz.spindler@hs-rm.de

###### Abstract

The correspondence between right triangles with rational sides, triplets of rational squares in arithmetic succession and integral solutions of certain quadratic forms is well known. We show how this correspondence can be extended to the generalized notions of rational θ \theta -triangles, rational squares occurring in arithmetic progressions and concordant forms. In our approach we establish one-to-one mappings to rational points on certain elliptic curves and examine in detail the role of solutions of the θ \theta -congruent number problem and the concordant form problem associated with nontrivial torsion points on the corresponding elliptic curves. This approach allows us to combine and extend some disjoint results obtained by a number of authors, to clarify some statements in the literature and to answer some hitherto open questions.

† † 2010 *Mathematics Subject Classification*: Primary 11D25, 11G05; Secondary 14H52. † †*Key words and phrases*: Elliptic curves, concordant forms, θ \theta -congruent numbers.

## 1 Introduction

The following definition dates back to Euler ([E]; see also [O2]).

###### Definition 1.1.

Two quadratic forms X 2 + m ​ Y 2 X^{2}+mY^{2} and X 2 + n ​ Y 2 X^{2}+nY^{2} (where m, n ∈ ℤ ∖ { 0 } m,n\in{\mathbb{Z}}\setminus\{0\} with m ≠ n m\not=n) are called concordant if the system

 | X 2 + m ​ Y 2 = Z 2, X 2 + n ​ Y 2 = W 2 X^{2}+mY^{2}=Z^{2},\quad X^{2}+nY^{2}=W^{2} |  |

admits a nontrivial solution ( X, Y, Z, W) ∈ ℤ 4 (X,Y,Z,W)\in{\mathbb{Z}}^{4}, where nontriviality means that Y ≠ 0 Y\not=0. This is equivalent to saying that there are solutions ( X, Y, Z, W) (X,Y,Z,W) ∈ ℙ 3 ​ ( ℚ) \in{\mathbb{P}}_{3}({\mathbb{Q}}) other than ( 1, 0, ± 1, ± 1) (1,0,\pm 1,\pm 1). Thus ( X, Y, Z, W) (X,Y,Z,W) is a trivial solution if and only if it is a solution for any pair ( m, n) (m,n).

It is easily verified that every system of concordant forms is equivalent to one in which the coefficients m m and n n have different signs; hence we may always assume that m < 0 m<0 and n > 0 n>0. After factoring out the greatest common divisor of the coefficients, this leads us to consider quadratic forms X 2 − p ​ k ​ Y 2 X^{2}-pkY^{2} and X 2 + q ​ k ​ Y 2 X^{2}+qkY^{2} where k, p, q ∈ ℕ k,p,q\in{\mathbb{N}} with p p and q q coprime. Concordant forms in this form tie up nicely with rational squares occurring in arithmetic progressions. In fact, if α 2 < β 2 < γ 2 \alpha^{2}<\beta^{2}<\gamma^{2} are squares of rational numbers which occur in an arithmetic progression of (maximally chosen) step size k k, then there are coprime numbers p, q ∈ ℕ p,q\in{\mathbb{N}} such that α 2 = β 2 − p ​ k \alpha^{2}=\beta^{2}-pk and γ 2 = β 2 + q ​ k \gamma^{2}=\beta^{2}+qk, which means exactly that the forms X 2 − p ​ k ​ Y 2 X^{2}-pkY^{2} and X 2 + q ​ k ​ Y 2 X^{2}+qkY^{2} are concordant. To have a precise terminology available, let us give a formal definition.

###### Definition 1.2.

A triplet ( p, q, k) ∈ ℕ × ℕ × ℕ (p,q,k)\in{\mathbb{N}}\times{\mathbb{N}}\times{\mathbb{N}} where p, q p,q are coprime is called a solution of the concordant form problem if and only if the quadratic forms X 2 − p ​ k ​ Y 2 X^{2}-pkY^{2} and X 2 + q ​ k ​ Y 2 X^{2}+qkY^{2} are concordant; i.e., if and only if there is an arithmetic progression of (maximal) step size k k containing three rational squares, where the lowest and the highest are separated from the intermediate one by p p times resp. q q times the step size.

Obviously, a triplet ( p, q, k) (p,q,k) is a solution of the concordant form problem if and only if ( p, q, a 2 ​ k) (p,q,a^{2}k) is for any a ∈ ℕ a\in{\mathbb{N}} (since the factor a a can be subsumed into Y Y); hence it is sufficient to study solutions ( p, q, k) (p,q,k) where k k is squarefree. We note that arithmetic progressions of squares have been studied not just over the rationals, but over number fields (cf. [Co2], [GS], [GX], [X]). While in these approaches the goal was to find (maximal) uninterrupted arithmetic progressions of squares in the given base field, we focus on rational squares which occur in arithmetic progressions, but not necessarily in immediate succession. We now relate the concordant form problem to a different problem which is cast in geometric rather than arithmetic language. The concept of congruent numbers (see [Ko], [T]) has been extended to that of a t t -congruent number (cf. [TY]) and even more generally to that of a θ \theta -congruent number (cf. [F1], [Ka], [Y1], [Y2], [Y3]); for an overview see [TY]. Even though the concept of a t t -congruent number is more natural from a geometric point of view (arising from the search for triangles with rational sides and rational area), the more general concept of a θ \theta -congruent number is more relevant for the purposes of this paper.

###### Definition 1.3.

Given an angle θ ∈ ( 0, π) \theta\in(0,\pi) whose cosine is a rational number, a number k ∈ ℕ k\in{\mathbb{N}} is called θ \theta -congruent if there is a triangle with rational sides which has θ \theta as an angle and k ​ s 2 − r 2 k\sqrt{s^{2}-r^{2}} as its area, where r ∈ ℤ r\in{\mathbb{Z}} and s ∈ ℕ s\in{\mathbb{N}} are the unique coprime numbers such that cos ⁡ ( θ) = r / s \cos(\theta)=r/s. Somewhat more precisely we call a triplet ( r, s, k) ∈ ℤ × ℕ × ℕ (r,s,k)\in{\mathbb{Z}}\times{\mathbb{N}}\times{\mathbb{N}} a solution of the generalized congruent number problem if k k is θ \theta -congruent where cos ⁡ θ = r / s \cos\theta=r/s in lowest terms.

Scaling the sides of a triangle by a factor a a changes the area by the factor a 2 a^{2}; hence a natural number is θ \theta -congruent for some angle θ \theta if and only if its squarefree part is. In other words, ( r, s, k) (r,s,k) is a solution of the generalized congruent number problem if and only if ( r, s, a 2 ​ k) (r,s,a^{2}k) is for any number a ∈ ℕ a\in{\mathbb{N}}. Clearly, ( π / 2) (\pi/2) -congruence is just ordinary congruence of numbers; the only other angles θ \theta for which θ \theta -congruence has been studied somewhat systematically are θ = π / 3 \theta=\pi/3 and θ = 2 ​ π / 3 \theta=2\pi/3; see [Y1], [Y2], [Y3] and [JSDP].

The two problems are closely related, as is shown by the following theorem (whose elementary proof we omit).

###### Theorem 1.4.

Let 𝔑 \mathfrak{N} be the set of solutions of the generalized congruent number problem, and let 𝔉 \mathfrak{F} be the set of solutions of the concordant form problem. Then mutually inverse bijections f: 𝔑 → 𝔉 f:\mathfrak{N}\rightarrow\mathfrak{F} and g: 𝔉 → 𝔑 g:\mathfrak{F}\rightarrow\mathfrak{N} are given by

 | f ⁡ ( r, s, k):= { ( s − r, s + r, k) if r ≢ s mod 2, ( ( s − r) / 2, ( s + r) / 2, 2 ​ k) if r, s are both odd f(r,s,k):=\begin{cases}(s-r,s+r,k)&\hbox{if $r\not\equiv s$ mod $2$},\\ \bigl((s-r)/2,(s+r)/2,2k\bigr)&\hbox{if $r,s$ are both odd}\end{cases} |  |

and

 | g ⁡ ( p, q, k):= { ( ( q + p) / 2, ( q − p) / 2, k) if p, q are both odd, ( q + p, q − p, k / 2) if p ≢ q mod 2. g(p,q,k):=\begin{cases}\bigl((q+p)/2,(q-p)/2,k\bigr)&\hbox{if $p,q$ are both odd},\\ \bigl(q+p,q-p,k/2\bigr)&\hbox{if $p\not\equiv q$ mod $2$.}\end{cases} |  |

## 2 Connections to elliptic curves

In the introduction we exhibited a correspondence between θ \theta -congruent numbers, rational squares in arithmetic progressions and concordant forms written in a certain way. Now we establish a 1-1 correspondence between the intersection of quadrics given by concordant forms and elliptic curves in standard form.

###### Theorem 2.1.

Let m ≠ n m\not=n be nonzero integers. We denote by Q ⁡ ( m, n) Q(m,n) the set of all ( X 0, X 1, X 2, X 3) ∈ ℙ 3 ​ ( ℚ) (X_{0},X_{1},X_{2},X_{3})\in\mathbb{P}_{3}(\mathbb{Q}) such that

 | X 0 2 + m ​ X 1 2 = X 2 2 and X 0 2 + n ​ X 1 2 = X 3 2. X_{0}^{2}+mX_{1}^{2}=X_{2}^{2}\quad\hbox{and}\quad X_{0}^{2}+nX_{1}^{2}=X_{3}^{2}. |  |

Also, we denote by E ⁡ ( m, n) E(m,n) the set of all ( T, X, Y) ∈ ℙ 2 ​ ( ℚ) (T,X,Y)\in{\mathbb{P}}_{2}(\mathbb{Q}) such that

 | Y 2 ​ T = X ⁡ ( X + m ​ T) ​ ( X + n ​ T) Y^{2}T=X(X+mT)(X+nT) |  |

which, in affine notation, is just the elliptic curve y 2 = x ⁡ ( x + m) ​ ( x + n) y^{2}=x(x+m)(x+n). Then mutually inverse isomorphisms φ: Q ⁡ ( m, n) → E ⁡ ( m, n) \varphi:Q(m,n)\rightarrow E(m,n) and ψ: E ⁡ ( m, n) → Q ⁡ ( m, n) \psi:E(m,n)\rightarrow Q(m,n) are given by

 | φ: [X 0 X 1 X 2 X 3] ↦ [n ​ X 2 − m ​ X 3 + ( m − n) ​ X 0 m ​ n ​ ( X 3 − X 2) m ​ n ​ ( m − n) ​ X 1] \varphi:\left[\begin{matrix}X_{0}\\ X_{1}\\ X_{2}\\ X_{3}\end{matrix}\right]\mapsto\left[\begin{matrix}nX_{2}-mX_{3}+(m\!-\!n)X_{0}\\ mn(X_{3}-X_{2})\\ mn(m\!-\!n)X_{1}\end{matrix}\right] |  |

and

 | ψ: [T X Y] ↦ [− ( X + m ​ T) ​ ( Y 2 − m ​ ( X + n ​ T) 2) 2 ​ Y ​ ( X + n ​ T) ​ ( X + m ​ T) − ( X + m ​ T) ​ ( Y 2 + m ​ ( X + n ​ T) 2) − ( X + n ​ T) ​ ( Y 2 + n ​ ( X + m ​ T) 2)]. \psi:\left[\begin{matrix}T\\ X\\ Y\end{matrix}\right]\mapsto\left[\begin{matrix}-(X\!+\!mT)\bigl(Y^{2}-m(X\!+\!nT)^{2}\bigr)\\ 2Y(X\!+\!nT)(X\!+\!mT)\\ -(X\!+\!mT)\bigl(Y^{2}+m(X\!+\!nT)^{2}\bigr)\\ -(X\!+\!nT)\bigl(Y^{2}+n(X\!+\!mT)^{2}\bigr)\end{matrix}\right]\,. |  |

Note that φ \varphi needs to be redefined at ( 1, 0, 1, 1) (1,0,1,1) whereas ψ \psi needs to be redefined at ( 1, − m, 0) (1,-m,0), ( 1, − n, 0) (1,-n,0) and ( 0, 0, 1) (0,0,1) to obtain well-defined regular maps. We omit the proof that φ \varphi and ψ \psi are in fact well-defined and have the desired properties (which is obtained by straightforward calculations) and merely remark that this isomorphism is an instance of a general correspondence between elliptic curves and intersections of quadrics; see [Ca], p. 36, and [Co1], pp. 123-125.) We note that the isomorphism ψ \psi maps the point at infinity and the 2 2 -torsion points ( − m, 0) (-m,0), ( − n, 0) (-n,0) and ( 0, 0) (0,0) of E ⁡ ( m, n) E(m,n) exactly to the trivial solutions ( 1, 0, ± 1, ± 1) (1,0,\pm 1,\pm 1) of Q ⁡ ( m, n) Q(m,n). Consequently, all other rational points of E ⁡ ( m, n) E(m,n) correspond to nontrivial points on Q ⁡ ( m, n) Q(m,n). Thus the following is true (cf. [F1], Prop. 3; [Ka], Thm 1).

###### Theorem 2.2.

Let m ≠ n m\not=n be nonzero integers. Then the quadratic forms X 2 + m ​ Y 2 X^{2}+mY^{2} and X 2 + n ​ Y 2 X^{2}+nY^{2} are concordant if and only if E ⁡ ( m, n) E(m,n) possesses elements of (finite or infinite) order greater than two.

The fact that our mappings φ \varphi and ψ \psi are true isomorphisms make them more suitable than other correspondences studied in the literature. Let us explain this statement in some detail.

The book [Ko] deals with the classical congruent number problem. If n n is a natural number and ( X, Y, Z) (X,Y,Z) are rational sides of a right triangle with area n n (where X < Y < Z X<Y<Z), then the assignment ( X, Y, Z) ↦ ( Z 2 / 2, ( X 2 − Y 2) ​ Z / 8) = ( x, y) (X,Y,Z)\mapsto(Z^{2}/2,(X^{2}-Y^{2})Z/8)=(x,y) (see [Ko], Ch. I, §2, Prop. 2; Ch. I, §9, Prop. 19) maps the right triangles to rational points of the elliptic curve E ⁡ ( − n, n) E(-n,n) given by the affine equation y 2 = x 3 − n 2 ​ x y^{2}=x^{3}-n^{2}x. The assignment ( X 0, X 1, X 2, X 3) ↦ ( X 2 / X 1, X 0 / X 1, X 3 / X 1) (X_{0},X_{1},X_{2},X_{3})\mapsto(X_{2}/X_{1},X_{0}/X_{1},X_{3}/X_{1}) associates with any point ( X 0, X 1, X 2, X 3) (X_{0},X_{1},X_{2},X_{3}) on the intersection of the quadrics X 0 2 − n ​ X 1 2 = X 2 2 X_{0}^{2}-nX_{1}^{2}=X_{2}^{2} and X 0 2 + n ​ X 1 2 = X 3 2 X_{0}^{2}+nX_{1}^{2}=X_{3}^{2} with X i ≥ 0 X_{i}\geq 0 and X 1 > 0 X_{1}>0 such a triangle. The composite function τ \tau which is computed to be

 | ( X 0, X 1, X 2, X 3) ↦ ( X 0 2 X 1 2, − X 0 ​ X 2 ​ X 3 X 1 3) (X_{0},X_{1},X_{2},X_{3})\ \mapsto\ \left(\frac{X_{0}^{2}}{X_{1}^{2}},-\frac{X_{0}X_{2}X_{3}}{X_{1}^{3}}\right) |  |

obviously extends to a regular morphism Q ⁡ ( − n, n) → E ⁡ ( − n, n) Q(-n,n)\rightarrow E(-n,n). The trivial elements of Q ⁡ ( − n, n) Q(-n,n) are mapped to the point at infinity, i. e., to the neutral element of the elliptic curve E ⁡ ( − n, n) E(-n,n). This morphism, however, is not an isomorphism, but is a mapping of degree 4 whose image is exactly 2 ​ E ​ ( − n, n) 2E(-n,n), i.e., the set of all doubled points of E ⁡ ( − n, n) E(-n,n). If we denote by 𝔻 \mathbb{D} the doubling P ↦ 2 ​ P P\mapsto 2P on the elliptic curve E ⁡ ( − n, n) E(-n,n), then an easy computation shows that the diagram

 | Q ⁡ ( − n, n) \textstyle{Q(-n,n)\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces} τ \tau φ \varphi E ⁡ ( − n, n) \textstyle{E(-n,n)} E ⁡ ( − n, n) \textstyle{E(-n,n)\ignorespaces\ignorespaces\ignorespaces\ignorespaces} 𝔻 \mathbb{D} |  |

commutes in which φ \varphi is the mapping introduced at the beginning of this section. In other words, for any point S S in Q ⁡ ( − n, n) Q(-n,n) we have τ ⁡ ( S) = 2 ​ φ ​ ( S) \tau(S)=2\varphi(S). Since the only torsion points on E ⁡ ( − n, n) E(-n,n) are the points of order 2, these points are mapped to the neutral element of E ⁡ ( − n, n) E(-n,n). This diagram explains why, for example, the points ( 41 2 / 7 2, 29520 / 7 3) (41^{2}/7^{2},29520/7^{3}) on E ⁡ ( − 31, 31) E(-31,31) and ( 25 / 4, 75 / 8) (25/4,75/8) on E ⁡ ( − 5, 5) E(-5,5) (cf. [Ko], p. 7) are not in the image of τ \tau. However, they correspond to solutions of the associated concordant form problem via the mapping φ \varphi.

Note that the defect of the mapping τ \tau of not being an isomorphism does not affect any of the assertions in [Ko]. In particular, the statement that n n is a congruent number if and only if E ⁡ ( − n, n) E(-n,n) contains rational points of infinite order is true, since the only points of finite order (the 2-torsion points) are mapped to the neutral element of E ⁡ ( − n, n) E(-n,n) via the mapping τ \tau, and they correspond to the trivial solutions of the concordant form problem and the degenerate right triangle. However, the defect of τ \tau would make itself felt if one considered not only rational points on the elliptic curve in question, but also solutions over number fields.

The use of a correspondence which is not an isomorphism runs into problems when torsion points of order greater than 2 occur, which is the case in the general concordant form problem considered in [O1]. The mapping σ: Q ⁡ ( m, n) → E ⁡ ( m, n) \sigma:Q(m,n)\rightarrow E(m,n) used in [O1] is given by

 | ( X 0, X 1, X 2, X 3) ↦ ( X 0 2 X 1 2, X 0 ​ X 2 ​ X 3 X 1 3) (X_{0},X_{1},X_{2},X_{3})\ \mapsto\ \left(\frac{X_{0}^{2}}{X_{1}^{2}},\,\frac{X_{0}X_{2}X_{3}}{X_{1}^{3}}\right) |  |

and hence is the same as the one considered by Koblitz up to the sign in the second component. It turns out that σ \sigma is again the composition of the isomorphism φ \varphi with an algebraically defined endomorphism of E ⁡ ( m, n) E(m,n), namely the negative − 𝔻 -\mathbb{D} of the doubling mapping 𝔻 \mathbb{D}. Again, this mapping is of degree 4 and has 2 ​ E ​ ( m, n) 2E(m,n) as its image. But in this more general situation, the curve E ⁡ ( m, n) E(m,n) may have points of order 4, and these points are mapped to a 2-torsion point in the image of σ \sigma. Now such 2-torsion points correspond to nontrivial solutions of the associated concordant form problem. So for any pair of numbers ( m, n) (m,n) for which the torsion subgroup of the elliptic curve E ⁡ ( m, n) E(m,n) is isomorphic to ℤ 2 × ℤ 4 \mathbb{Z}_{2}\times\mathbb{Z}_{4} there exist nontrivial solutions of the concordant form problem in the sense of Definition 1.1 for the pair ( m, n) (m,n) even if the rank of E ⁡ ( m, n) E(m,n) is zero. Hence the statement in [O1] that if E ⁡ ( m, n) E(m,n) has rank zero then nontrivial solutions exist if and only if the torsion group is ℤ 2 × ℤ 8 {\mathbb{Z}}_{2}\times{\mathbb{Z}}_{8} or ℤ 2 × ℤ 6 {\mathbb{Z}}_{2}\times{\mathbb{Z}}_{6} ([O1], p. 101) needs qualification. For example, if ( m, n) = ( − 1, 3) (m,n)=(-1,3) then ( X, Y, Z, W) = ( ± 1, ± 1, 0, ± 2) (X,Y,Z,W)=(\pm 1,\pm 1,0,\pm 2) are solutions of the equations X 2 + m ​ Y 2 = Z 2 X^{2}+mY^{2}=Z^{2} and X 2 + n ​ Y 2 = W 2 X^{2}+nY^{2}=W^{2} corresponding to the 4-torsion points ( 3, ± 6) (3,\pm 6) and ( − 1, ± 2) (-1,\pm 2) of the elliptic curve y 2 = x ⁡ ( x − 1) ​ ( x + 3) y^{2}=x(x-1)(x+3); note that E ⁡ ( − 1, 3) E(-1,3) has rank zero (see [Y1]). These solutions are not covered by Main Corollary 1 (pp. 104/105) and Corollary 2 (p. 107) in [O1] where only solutions are considered for which all components are nonzero.

We note in passing that the curve y 2 = x ⁡ ( x − 1) ​ ( x + 3) y^{2}=x(x-1)(x+3) also provides a counterexample to Proposition 5.4 in [TY], which does not hold for n = 1 n=1. In fact, n = 1 n=1 is a π / 3 \pi/3 -congruent number (realized by the equilateral triangle with all sides equal to 2), which, in fact, corresponds to the 4-torsion points ( 3, ± 6) (3,\pm 6) and ( − 1, ± 2) (-1,\pm 2) of the elliptic curve E ⁡ ( − 1, 3) E(-1,3). Hence the additional assumption n > 1 n>1 is indispensible to make Proposition 5.4 in [TY] true.

In the recent paper [Im], again only solutions with nonzero components are considered, as becomes clear from Definition 2 in this paper (which should presumably state that a solution ( X, Y, Z, W) (X,Y,Z,W) is considered nontrivial only if X ​ Y ​ Z ​ W ≠ 0 XYZW\not=0). Thus, again, solutions associated with 4-torsion points on the corresponding curve are lost. For example, for m = 1 m=1 and n = k 2 n=k^{2} where k ∈ { 2, 3, 4, 5, 6, 8, 9, 13 } k\in\{2,3,4,5,6,8,9,13\} solutions exist (namely ( X, Y, Z, W) = ( 0, 1, 1, k) (X,Y,Z,W)=(0,1,1,k)) which are not covered in [Im]. The condition that the rank of E ⁡ ( 1, k 2) E(1,k^{2}) be zero is satisfied for the quoted values of k k (whereas the rank is one for k ∈ { 7, 10, 11, 12 } k\in\{7,10,11,12\}), as we verified with the SAGE software package.

While a thorough analysis of the mapping σ \sigma used in [O1] together with the two-descent on the elliptic curve E ⁡ ( m, n) E(m,n) may reveal all the interesting phenomena concerning solutions to the concordant form problem from the study of rational points on E ⁡ ( m, n) E(m,n) via σ \sigma, the approach via the isomorphism φ \varphi seems to be much more direct and natural. Also, the correspondence between solutions ( r, s, k) (r,s,k) of the congruent number problem and rational points of order > 2 >2 on the elliptic curve

 | y 2 = x ⁡ ( x − ( s − r) ​ k) ​ ( x + ( s + r) ​ k) y^{2}=x\bigl(x-(s\!-\!r)k\bigr)\bigl(x+(s\!+\!r)k\bigr) |  |

becomes, via the correspondence with rational squares in arithmetic progressions, more lucid than in [F1], [Ka] and [Y1]. It also becomes clear from our calculations that two rational points of order > 2 >2 on the curve yield the same triangle if and only if they differ by a 2-torsion element in the Mordell-Weil group of the curve. Moreover, our calculations clarify Theorem 1 and Proposition 4 in [F1]. More precisely, we will exactly determine those numbers n n occurring as θ \theta -congruent numbers corresponding to torsion elements of the associated elliptic curve, which was left open in [F1] and was clarified in the paper [F2], of which we were made aware only after finishing our paper.

## 3 Nontrivial torsion solutions

When we speak of the torsion subgroup of an elliptic curve E E over ℚ \mathbb{Q} we always mean the torsion subgroup of the Mordell-Weil group E ℚ E_{\mathbb{Q}} of rational points on E E. A deep theorem by Mazur (see [M]) states that the torsion subgroup of any elliptic curve over ℚ \mathbb{Q} must be one of the groups ℤ m {\mathbb{Z}}_{m} where 1 ≤ m ≤ 10 1\leq m\leq 10 or m = 12 m=12 or else of the groups ℤ 2 × ℤ 2 ​ n {\mathbb{Z}}_{2}\times{\mathbb{Z}}_{2n} where 1 ≤ n ≤ 4 1\leq n\leq 4. Since E ⁡ ( m, n) E(m,n) has three points of order 2 2, namely ( 0, 0) (0,0), ( − m, 0) (-m,0) and ( − n, 0) (-n,0), only the last four possibilities can occur for the curves studied here. We want to determine the exact conditions on m m and n n which determine the type of the torsion group. To do so, we compute all nontrivial torsion elements. This was essentially already done in [O1], and only a few additional calculations (omitted here) are needed to arrive at the following complete characterization of all torsion elements. (Also see [F2].)

###### Theorem 3.1.

We consider the elliptic curve E ⁡ ( m, n) E(m,n) over ℚ \mathbb{Q} where m = − p ​ k m=-pk and n = q ​ k n=qk such that p, q ∈ ℕ p,q\in{\mathbb{N}} are coprime and k ∈ ℕ k\in{\mathbb{N}} is squarefree.

1. (i)

There are points of order 4 4 if and only if − m -m and n − m n-m are squares, say − m = u 2 -m=u^{2} and n = v 2 − u 2 n=v^{2}-u^{2}. In this case, the 4 4 -torsion points are exactly the four points

 | ( u 2 − u ​ v, ± v ⁡ ( u 2 − u ​ v)) and ( u 2 + u ​ v, ± v ⁡ ( u 2 + u ​ v)). \bigl(u^{2}-uv,\,\pm v(u^{2}-uv)\bigr)\quad\hbox{and}\quad\bigl(u^{2}+uv,\,\pm v(u^{2}+uv)\bigr)\,. |  |

2. (ii)

There are points of order 8 8 if and only if there are numbers ξ, η ∈ ℕ \xi,\eta\in{\mathbb{N}} such that ξ 2 + η 2 \xi^{2}+\eta^{2} is a square, say ξ 2 + η 2 = ζ 2 \xi^{2}+\eta^{2}=\zeta^{2}, and the equations m = − ξ 4 m=-\xi^{4} and n = η 4 − ξ 4 = ζ 2 ​ ( η 2 − ξ 2) n=\eta^{4}-\xi^{4}=\zeta^{2}(\eta^{2}-\xi^{2}) hold. In this case, the 8 8 -torsion points are exactly the eight points

 | ( ξ ​ ζ ​ ( ξ + η) ​ ( ζ + η), ± ξ ​ η ​ ζ ​ ( ξ + η) ​ ( ζ + ξ) ​ ( ζ + η)), \displaystyle\bigl(\ \xi\zeta(\xi\!+\!\eta)(\zeta\!+\!\eta),\ \pm\xi\eta\zeta(\xi\!+\!\eta)(\zeta\!+\!\xi)(\zeta\!+\!\eta)\ \bigr), |  |

 | ( ξ ​ ζ ​ ( ξ + η) ​ ( ζ − η), ± ξ ​ η ​ ζ ​ ( ξ + η) ​ ( ζ − ξ) ​ ( ζ − η)), \displaystyle\bigl(\ \xi\zeta(\xi\!+\!\eta)(\zeta\!-\!\eta),\ \pm\xi\eta\zeta(\xi\!+\!\eta)(\zeta\!-\!\xi)(\zeta\!-\!\eta)\ \bigr), |  |

 | ( ξ ​ ζ ​ ( ξ − η) ​ ( ζ + η), ± ξ ​ η ​ ζ ​ ( ξ − η) ​ ( ζ − ξ) ​ ( ζ + η)), \displaystyle\bigl(\ \xi\zeta(\xi\!-\!\eta)(\zeta\!+\!\eta),\ \pm\xi\eta\zeta(\xi\!-\!\eta)(\zeta\!-\!\xi)(\zeta\!+\!\eta)\ \bigr), |  |

 | ( ξ ​ ζ ​ ( ξ − η) ​ ( ζ − η), ± ξ ​ η ​ ζ ​ ( ξ − η) ​ ( ζ − η) ​ ( ζ + ξ)). \displaystyle\bigl(\ \xi\zeta(\xi\!-\!\eta)(\zeta\!-\!\eta),\ \pm\xi\eta\zeta(\xi\!-\!\eta)(\zeta\!-\!\eta)(\zeta\!+\!\xi)\ \bigr). |  |

3. (iii)

There are points of order 3 3 (or, equivalently, points of order 6 6) if and only if there are coprime integers a, b ≠ 0 a,b\not=0 with a + 2 ​ b ≠ 0 a+2b\not=0, b + 2 ​ a ≠ 0 b+2a\not=0 and a ± b ≠ 0 a\pm b\not=0 such that m = a 3 ​ ( a + 2 ​ b) m=a^{3}(a+2b) and n = b 3 ​ ( b + 2 ​ a) n=b^{3}(b+2a). In this case the points of order 3 3 are the two points

 | ( a 2 ​ b 2, ± a 2 ​ b 2 ​ ( a + b) 2), (a^{2}b^{2},\,\pm a^{2}b^{2}(a+b)^{2}\bigr), |  |

and the points of order 6 6 are the six points

 | ( − a 2 ​ b ​ ( b + 2 ​ a), ± a 2 ​ b ​ ( b + 2 ​ a) ​ ( a 2 − b 2)), \displaystyle\bigl(\ -a^{2}b(b\!+\!2a),\ \pm a^{2}b(b\!+\!2a)(a^{2}\!-\!b^{2})\ \bigr), |  |

 | ( − a ​ b 2 ​ ( a + 2 ​ b), ± a ​ b 2 ​ ( a + 2 ​ b) ​ ( a 2 − b 2)), \displaystyle\bigl(\ -ab^{2}(a\!+\!2b),\ \pm ab^{2}(a\!+\!2b)(a^{2}\!-\!b^{2})\ \bigr), |  |

 | ( a ​ b ​ ( a + 2 ​ b) ​ ( b + 2 ​ a), ± a ​ b ​ ( a + 2 ​ b) ​ ( b + 2 ​ a) ​ ( a + b) 2). \displaystyle\bigl(ab(a\!+\!2b)(b\!+\!2a),\ \pm ab(a\!+\!2b)(b\!+\!2a)(a\!+\!b)^{2}\ \bigr). |  |

4. (iv)

In all other cases for m m and n n the only torsion points are the trivial points ( 0, 0) (0,0), ( − m, 0) (-m,0) and ( − n, 0) (-n,0).

###### Remark 3.2.

If k = d 2 ​ ℓ k=d^{2}\ell is not squarefree, then the elliptic curves E ⁡ ( − p ​ ℓ, q ​ ℓ) E(-p\ell,q\ell) and E ⁡ ( − p ​ k, q ​ k) E(-pk,qk) are isomorphic (as algebraic groups) via the isomorphism ( x, y) ↦ ( d 2 ​ x, d 3 ​ y) (x,y)\mapsto(d^{2}x,d^{3}y). So the torsion subgroups of the corresponding Mordell-Weil groups of rational points are also isomorphic. As a special case, we note that the curve E ⁡ ( − p ​ k, q ​ k) E(-pk,qk) contains points of order 4 4 if and only if − m = p ​ k -m=pk and n − m = q ​ k + p ​ k n-m=qk+pk are squares (irrespectively of whether or not k k is squarefree).

We are now ready to give a complete classification of all concordant forms and θ \theta -congruent triangles which correspond to torsion solutions of the associated elliptic curve. This classification is based on the following theorem. (Cf. [F2].)

###### Theorem 3.3.

We consider the elliptic curve E ⁡ ( m, n) E(m,n) where m = − p ​ k m=-pk and n = q ​ k n=qk such that p, q ∈ ℕ p,q\in{\mathbb{N}} are coprime and k ∈ ℕ k\in{\mathbb{N}} is squarefree. Let T T be the torsion subgroup of E ⁡ ( m, n) E(m,n).

1. (i)

If T ≅ ℤ 2 × ℤ 4 T\cong{\mathbb{Z}}_{2}\times{\mathbb{Z}}_{4} or T ≅ ℤ 2 × ℤ 8 T\cong{\mathbb{Z}}_{2}\times{\mathbb{Z}}_{8} then k = 1 k=1.

2. (ii)

If T ≅ ℤ 2 × ℤ 6 T\cong{\mathbb{Z}}_{2}\times{\mathbb{Z}}_{6} then k = 1 k=1 or k = 3 k=3.

( \bigl( The examples in the next section will show that each of the possible cases occurs for an infinite number of elliptic curves E ⁡ ( m, n) E(m,n).) \bigr)

###### Proof.

Let us first consider the case that that T ≅ ℤ 2 × ℤ 4 T\cong{\mathbb{Z}}_{2}\times{\mathbb{Z}}_{4} or T ≅ ℤ × ℤ 8 T\cong{\mathbb{Z}}\times{\mathbb{Z}}_{8}. Assume k ≠ 1 k\not=1; then there is a prime divisor t t of k k. The number t t then divides both − m = p ​ k -m=pk and n − m = ( p + q) ​ k n-m=(p+q)k which are squares according to Thm 3.1(i). Since k k is squarefree this implies that t t divides both p p and p + q p+q, which is impossible because p p and q q are coprime by assumption. Thus the assumption k ≠ 1 k\not=1 is wrong, and we must have k = 1 k=1 in this case.

Let us now consider the case that T ≅ ℤ 2 × ℤ 6 T\cong{\mathbb{Z}}_{2}\times{\mathbb{Z}}_{6}. By Thm 3.1(iii) there are coprime numbers a, b ∈ ℤ ∖ { 0 } a,b\in{\mathbb{Z}}\setminus\{0\} with a + 2 ​ b ≠ 0 a+2b\not=0, b + 2 ​ a ≠ 0 b+2a\not=0 and a ± b ≠ 0 a\pm b\not=0 such that m = a 4 + 2 ​ a 3 ​ b m=a^{4}+2a^{3}b and n = 2 ​ a ​ b 3 + b 4 n=2ab^{3}+b^{4}. Let t t be a prime divisor of k k. Then t t divides both − p ​ k = m = a 3 ​ ( a + 2 ​ b) -pk=m=a^{3}(a+2b) and q ​ k = n = b 3 ​ ( 2 ​ a + b) qk=n=b^{3}(2a+b). It is obvious that if the prime t t were a divisor of a a then it would also be a divisor of b b, and vice versa; this, however, is impossible because a a and b b are coprime. Thus t t divides neither a a nor b b, hence divides both a + 2 ​ b a+2b and 2 ​ a + b 2a+b, hence divides 2 ​ ( a + 2 ​ b) = ( 2 ​ a + b) + 3 ​ b 2(a+2b)=(2a+b)+3b, hence divides 3 ​ b 3b and consequently must be 3 3. We have shown that 3 3 is the only possible prime divisor of k k. This implies that k = 1 k=1 or k = 3 k=3. ∎

The implication of this theorem for concordant forms and θ \theta -congruent numbers will be elucidated in the next section.

## 4 Interpretation and conclusions

Theorem 3.3 may be interpreted in terms of the concordant form problem and of the generalized congruent number problem.

###### Theorem 4.1.

Let m = − p ​ k m=-pk and n = q ​ k n=qk such that p, q ∈ ℕ p,q\in{\mathbb{N}} are coprime and k ∈ ℕ k\in{\mathbb{N}} is squarefree.

1. (i)

If the quadratic forms X 2 + m ​ Y 2 X^{2}+mY^{2} and X 2 + n ​ Y 2 X^{2}+nY^{2} are concordant due to 4 4 - or 8 8 -torsion, then k = 1 k=1.

2. (ii)

If the quadratic forms X 2 + m ​ Y 2 X^{2}+mY^{2} and X 2 + n ​ Y 2 X^{2}+nY^{2} are concordant due to 3 3 - or 6 6 -torsion then k = 1 k=1 or k = 3 k=3.

###### Proof.

This is an immediate consequence of Thm 3.3. ∎

###### Theorem 4.2.

Let θ = arccos ⁡ ( r / s) \theta=\arccos(r/s) where r ∈ ℤ r\in{\mathbb{Z}} and s ∈ ℕ s\in{\mathbb{N}} are coprime numbers such that | r | < s |r|<s. Moreover, let k ∈ ℕ k\in{\mathbb{N}} be a squarefree number.

1. (i)

If k k is odd and is a θ \theta -congruent number due to 4 4 - or 8 8 -torsion then k = 1 k=1.

2. (ii)

If k k is even and is a θ \theta -congruent number due to 4 4 - or 8 8 -torsion then k = 2 k=2.

3. (iii)

If k k is odd and is a θ \theta -congruent number due to 3 3 - or 6 6 -torsion then k = 1 k=1 or k = 3 k=3.

4. (iv)

If k k is even and is a θ \theta -congruent number due to 3 3 - or 6 6 -torsion then k = 2 k=2 or k = 6 k=6.

###### Proof.

We remember that the associated elliptic curve is given by E ⁡ ( m, n) E(m,n) where m = − ( s − r) ​ k m=-(s-r)k and n = ( s + r) ​ k n=(s+r)k if r ≢ s r\not\equiv s mod 2 (first case) and where m = − ( s − r) k / 2 m=-(s-r)k/2 and n = ( s + r) ​ k / 2 n=(s+r)k/2 if r, s r,s are both odd (second case). In the first case, the coefficients satisfy the hypotheses of Thm 3.3 and we see that in the situation of (i) we have k = 1 k=1 and for (iii) we have k = 1 k=1 or k = 3 k=3. The same holds in the second case when k k is odd. It remains to consider the second case with k = 2 ​ ℓ k=2\ell being even (and ℓ \ell being odd since k k is assumed to be squarefree). In this situation the elliptic curve E ⁡ ( m ′, n ′) E(m^{\prime},n^{\prime}) associated with the triplet ( r, s, ℓ) (r,s,\ell) is given by m ′ = − ( s − r) ℓ / 2 m^{\prime}=-(s-r)\ell/2 and n ′ = ( s + r) ​ ℓ / 2 n^{\prime}=(s+r)\ell/2, and these coefficients satisfy the hypotheses of Thm 3.3. So we can conclude that ℓ = 1 \ell=1 (and hence k = 2 k=2) in the situation (ii) and ℓ = 1 \ell=1 or ℓ = 3 \ell=3 (and hence k = 2 k=2 or k = 6 k=6) in the situation (iv). ∎

Any of the above situations occurs for infinitely many elliptic curves. The characterization of the curves with a prescribed torsion subgroup, together with the arguments in the proof of Thm 3.3, gives rise to several series of examples which will illustrate this fact.

###### Example 4.3.

Torsion solutions of order 4. Let u, v u,v be any coprime numbers with u < v u<v and let m = − u 2 m=-u^{2} and n = v 2 − u 2 n=v^{2}-u^{2}. Then the torsion subgroup T ⊆ E ℚ ​ ( m, n) T\subseteq E_{\mathbb{Q}}(m,n) contains ℤ 2 × ℤ 4 \mathbb{Z}_{2}\times\mathbb{Z}_{4}. Hence any point of order 4 defines a solution of the concordant form problem given by the triplet ( p, q, k) = ( − m, n, 1) (p,q,k)=(-m,n,1). If m m and n n are both odd (which is equivalent to saying that v v is even) then this point defines a solution to the generalized congruent number problem given by the triplet ( r, s, k) = ( ( n − m) / 2, ( n + m) / 2, 1) (r,s,k)=((n-m)/2,\,(n+m)/2,\,1) as well. If m m and n n have different parities, then the elliptic curve E ⁡ ( 4 ​ m, 4 ​ n) E(4m,4n) also has a point of order 4, which defines a solution to the generalized congruent number problem given by the triplet ( n − m, n + m, 2) (n-m,\,n+m,\,2). Explicit instances are given by ( u, v) = ( 1, 2) (u,v)=(1,2), which corresponds to ( m, n) = ( − 1, 3) (m,n)=(-1,3) and represents the situation that v v is even, and by ( u, v) = ( 1, 3) (u,v)=(1,3), which corresponds to ( m, n) = ( − 1, 8) (m,n)=(-1,8) and represents the situation that v v is odd).

###### Example 4.4.

Torsion solutions of order 8. Let ( ξ, η, ζ) (\xi,\eta,\zeta) be any primitive Pythagorean triplet so that ξ 2 + η 2 = ζ 2 \xi^{2}+\eta^{2}=\zeta^{2} and ξ < η \xi<\eta (note that ξ \xi and η \eta then automatically have unequal parities!) and let m = − ξ 4 m=-\xi^{4} and n = η 4 − ξ 4 n=\eta^{4}-\xi^{4}. Then the torsion subgroup T ⊆ E ℚ ​ ( m, n) T\subseteq E_{\mathbb{Q}}(m,n) is isomorphic to ℤ 2 × ℤ 8 \mathbb{Z}_{2}\times\mathbb{Z}_{8}. So any point of order 8 defines a solution of the concordant form problem given by the triplet ( p, q, k) = ( − m, n, 1) (p,q,k)=(-m,n,1). If m m and n n are both odd (which means ξ \xi is odd and η \eta is even), then this point also defines a solution of the generalized congruent number problem given by ( r, s, k) = ( ( n − m) / 2, ( n + m) / 2, 1) (r,s,k)=((n-m)/2,\,(n+m)/2,\,1). If m m is even (and a fortiori n n is odd), then the elliptic curve E ⁡ ( 4 ​ m, 4 ​ n) E(4m,4n) also has points of order 8 8, each of which defines a solution of the generalized congruent number problem given by the triplet ( n − m, n + m, 2) (n-m,\,n+m,\,2). Explicit instances are given by ( ξ, η, ζ) = ( 3, 4, 5) (\xi,\eta,\zeta)=(3,4,5), which corresponds to ( m, n) = ( − 81,175) (m,n)=(-81,175) and represents the situation of a primitive Pythagorean triplet with ξ \xi being odd), and by by ( ξ, η, ζ) = ( 8, 15, 17) (\xi,\eta,\zeta)=(8,15,17), which corresponds to ( m, n) = ( − 4096, 46 529) (m,n)=(-4096,\,46\,529) and represents the situation of a primitive Pythagorean triplet with ξ \xi being even).

###### Example 4.5.

Torsion solutions of order 3 or 6. Let a, b a,b be any coprime numbers with a < 0 a<0, b > 0 b>0, a + 2 ​ b > 0 a+2b>0, 2 ​ a + b > 0 2a+b>0 and a + b ≠ 0 a+b\neq 0, and let m = a 3 ​ ( a + 2 ​ b) m=a^{3}(a+2b) and n = b 3 ​ ( 2 ​ a + b) n=b^{3}(2a+b). Then the torsion subgroup T ⊆ E ℚ ​ ( m, n) T\subseteq E_{\mathbb{Q}}(m,n) is isomorphic to ℤ 2 × ℤ 6 \mathbb{Z}_{2}\times\mathbb{Z}_{6}. From the proof of Thm 3.3 we know that the only possible common divisors of m m and n n are 1 or 3.

- •

First case: gcd ⁡ ( a + 2 ​ b, 2 ​ a + b) = 1 \gcd(a+2b,2a+b)=1. In this case any point of order 3 or 6 defines a solution of the concordant form problem given by the triplet ( p, q, k) = ( − m, n, 1) (p,q,k)=(-m,n,1). If m m and n n are both odd then this point also defines a solution of the generalized congruent number problem given by ( r, s, k) = ( ( n − m) / 2, ( n + m) / 2, 1) (r,s,k)=((n-m)/2,\,(n+m)/2,\,1). If m ≢ n m\not\equiv n mod 2 then the elliptic curve E ⁡ ( 4 ​ m, 4 ​ n) E(4m,4n) also has points of order 3 and 6, which define solutions of the generalized congruent number problem given by the triplet ( n − m, n + m, 2) (n-m,\,n+m,\,2).

- •

Second case: gcd ⁡ ( a + 2 ​ b, 2 ​ a + b) = 3 \gcd(a+2b,2a+b)=3. (Note that this situation occurs when a ≡ b a\equiv b mod 3.) Let p = − m / 3 p=-m/3 and q = n / 3 q=n/3. Then any point of order 3 or 6 defines a solution of the concordant form problem given by the triplet ( p, q, k) = ( − m / 3, n / 3, 3) (p,q,k)=(-m/3,\,n/3,\,3). If m m and n n are both odd, then this point also defines a solution of the generalized congruent number problem given by ( r, s, k) = ( ( n − m) / 6, ( n + m) / 6, 3) (r,s,k)=((n-m)/6,\,(n+m)/6,\,3). If m ≢ n m\not\equiv n mod 2 then the elliptic curve E ⁡ ( 4 ​ m, 4 ​ n) E(4m,4n) also has points of order 3 and 6, which define solutions to the generalized congruent number problem given by the triplet ( ( n − m) / 3, ( n + m) / 3, 6) ((n-m)/3,\,(n+m)/3,\,6).

Explicit instances are given as follows:

- •

the example ( a, b) = ( − 1, 3) (a,b)=(-1,3) corresponds to ( m, n) = ( − 5, 27) (m,n)=(-5,27) and represents the situation that a, b a,b are odd coprime numbers with different signs satisfying the congruence condition a ≢ b a\not\equiv b mod 3 3 and the inequalities a + 2 ​ b > 0 a+2b>0 and 2 ​ a + b > 0 2a+b>0;

- •

the example ( a, b) = ( − 2, 5) (a,b)=(-2,5) corresponds to ( m, n) = ( − 64, 125) (m,n)=(-64,\,125) and represents the situation that a, b a,b are coprime numbers with different signs and different parities satisfying the congruence condition a ≢ b a\not\equiv b mod 3 3 and the inequalities a + 2 ​ b > 0 a+2b>0 and 2 ​ a + b > 0 2a+b>0;

- •

the example ( a, b) = ( − 5, 13) (a,b)=(-5,\,13) corresponds to ( m, n) = ( − 875 ⋅ 3, 2197 ⋅ 3) (m,n)=(-875\cdot 3,\,2197\cdot 3) and represents the situation that a, b a,b are odd coprime numbers with different signs satisfying the congruence condition a ≡ b a\equiv b mod 3 3 and the inequalities a + 2 ​ b > 0 a+2b>0 and 2 ​ a + b > 0 2a+b>0;

- •

the example ( a, b) = ( − 2, 7) (a,b)=(-2,7) corresponds to ( m, n) = ( − 32 ⋅ 3, 343 ⋅ 3) (m,n)=(-32\cdot 3,\,343\cdot 3) and represents the situation that a, b a,b are coprime numbers with different signs and different parities satisfying the congruence condition a ≡ b a\equiv b mod 3 3 and the inequalities a + 2 ​ b > 0 a+2b>0 and 2 ​ a + b > 0 2a+b>0.

###### Remark 4.6.

From the above considerations it is clear that each of the possible situations occurs for an infinite number of cases. Furthermore, with these examples we answer a question left open in [F1] (Remark 1 after Proposition 4). Namely, in [F1] it is shown that if n ∉ { 1, 2, 3, 6 } n\not\in\{1,2,3,6\} then n n is a θ \theta -congruent number if and only if the rank of the associated elliptic curve is positive; i.e., it is not possible to obtain a corresponding θ \theta -triangle from torsion points on this elliptic curve. In [F1] it was shown that the condition n ∉ { 1, 2 } n\not\in\{1,2\} is indispensible in this statement; i.e., there are torsion solutions for n = 1 n=1 and n = 2 n=2. For n = 3 n=3 and n = 6 n=6 this was left as an open problem, which is now answered affirmatively by the above considerations.

The following result yields a nice geometric characterization of the 4-torsion solutions.

###### Theorem 4.7.

Let p, q ∈ ℕ p,q\in{\mathbb{N}} be coprime, let k ∈ ℕ k\in{\mathbb{N}} be squarefree, and let m = − p ​ k m=-pk and n = q ​ k n=qk. Consider a rational point P P on the curve E ⁡ ( m, n) E(m,n), the associated θ \theta -congruent triangle Δ \Delta and the associated triplet T T of rational squares in an arithmetic progression. Then the following statements are equivalent:

1. (i)

P P has order four;

2. (ii)

T T contains the number zero;

3. (iii)

Δ \Delta is isosceles, i.e., has two equal sides.

###### Proof.

Under the correspondences in Thm 1.4 we have a = b a=b for the sides of Δ \Delta if and only if α = 0 \alpha=0 for the smallest element in the progression α 2 < β 2 < γ 2 \alpha^{2}<\beta^{2}<\gamma^{2}, which is the case if and only if X 2 = 0 X_{2}=0 for a corresponding point ( X 0, X 1, X 2, X 3) (X_{0},X_{1},X_{2},X_{3}) on Q ⁡ ( m, n) Q(m,n) as defined in Thm 2.1 (since α = X 2 / X 1 \alpha=X_{2}/X_{1}, β = X 0 / X 1 \beta=X_{0}/X_{1} and γ = X 3 / X 1 \gamma=X_{3}/X_{1} under the correspondence between points on this curve and rational squares in arithmetic progression). Now the condition X 2 = 0 X_{2}=0 corresponds to the equation ( x + m) ​ ( y 2 + m ​ ( x + n) 2) = 0 (x+m)(y^{2}+m(x+n)^{2})=0 via the biregular mapping in Thm 2.1. This equation yields either x = − m x=-m (which is one of the 2-torsion points) or else y 2 + m ​ ( x + n) 2 = 0 y^{2}+m(x+n)^{2}=0. In the latter case − m -m must clearly be a square. Since both y 2 = − m ​ ( x + n) 2 y^{2}=-m(x+n)^{2} and y 2 = x ⁡ ( x + m) ​ ( x + n) y^{2}=x(x+m)(x+n), we have

 | 0 = x ⁡ ( x + m) ​ ( x + n) + m ​ ( x + n) 2 = ( x + n) ​ ( x 2 + 2 ​ m ​ x + m ​ n) = ( x + n) ​ ( ( x + m) 2 + m ⁡ ( n − m)) \begin{array}[]{ll}0&=x(x+m)(x+n)+m(x+n)^{2}\\ &=(x+n)(x^{2}+2mx+mn)\\ &=(x+n)\bigl((x+m)^{2}+m(n-m)\bigr)\end{array} |  |

and hence ( x + m) 2 = − m ⁡ ( n − m) (x+m)^{2}=-m(n-m). Hence not only − m -m, but also n − m n-m must be a square. This is exactly the condition that E ⁡ ( m, n) E(m,n) contains points with 4 4 -torsion. Writing − m = u 2 -m=u^{2}, the equation y 2 = − m ​ ( x + n) 2 = u 2 ​ ( x + n) 2 y^{2}=-m(x+n)^{2}=u^{2}(x+n)^{2} yields y = ± u ⁡ ( x + n) y=\pm u(x+n), which shows that the points ( x, y) (x,y) on E ⁡ ( m, n) E(m,n) associated with isosceles triangles are exactly the points of order 4 4. ∎

The isosceles triangles occurring as solutions of the generalized congruent number problem can be characterized in terms of intrinsic geometrical properties, as we now show. (Note that when we speak of an isosceles θ \theta -triangle we always assume the angle θ \theta to be between the two equal sides.)

###### Theorem 4.8.

There is an isosceles rational θ \theta -triangle if and only if sin ⁡ ( θ / 2) \sin(\theta/2) is rational. If sin ⁡ ( θ / 2) = ϱ / σ \sin(\theta/2)=\varrho/\sigma where ϱ, σ ∈ ℕ \varrho,\sigma\in\mathbb{N} are coprime, then the sides of the unique rational θ \theta -triangle with squarefree k k are given by a, a, c a,a,c with a = k ​ σ a=k\sigma and c = 2 ​ a ​ k ​ sin ⁡ ( θ / 2) = 2 ​ k ​ ϱ c=2ak\sin(\theta/2)=2k\varrho.

###### Proof.

First, if a, a, c a,a,c are the rational sides of an isosceles rational θ \theta -triangle with a rational cosine cos ⁡ ( θ) = r / s \cos(\theta)=r/s, then c = 2 ​ a ​ sin ⁡ ( θ / 2) c=2a\sin(\theta/2) so that sin ⁡ ( θ / 2) \sin(\theta/2) is also rational. Conversely, if sin ⁡ ( θ / 2) \sin(\theta/2) is rational, say sin ⁡ ( θ / 2) = ϱ / σ \sin(\theta/2)=\varrho/\sigma with ϱ, σ ∈ ℕ \varrho,\sigma\in\mathbb{N} coprime, then cos ⁡ ( θ) = 1 − 2 ​ sin 2 ⁡ ( θ / 2) \cos(\theta)=1-2\sin^{2}(\theta/2) is rational. If σ \sigma is odd, then cos ⁡ ( θ) = ( σ 2 − 2 ​ ϱ 2) / σ 2 = r / s \cos(\theta)=(\sigma^{2}-2\varrho^{2})/\sigma^{2}=r/s is a coprime representation with r, s r,s both odd. Let a = 2 ​ σ a=2\sigma and c = 2 ​ a ​ sin ⁡ ( θ / 2) = 4 ​ ϱ c=2a\sin(\theta/2)=4\varrho. Then the isosceles rational θ \theta -triangle with sides a, a, c a,a,c has the area ( a 2 / 2) ​ sin ⁡ ( θ) = 2 ​ σ 2 ​ 1 − cos 2 ⁡ ( θ) = 2 ​ σ 2 ​ ( s 2 − r 2) / s 2 = ( 2 ​ σ 2 / s) ​ s 2 − r 2 = 2 ​ s 2 − r 2 (a^{2}/2)\sin(\theta)=2\sigma^{2}\sqrt{1-\cos^{2}(\theta)}=2\sigma^{2}\sqrt{(s^{2}-r^{2})/s^{2}}=(2\sigma^{2}/s)\sqrt{s^{2}-r^{2}}=2\sqrt{s^{2}-r^{2}}, so that this triangle is the unique solution with k = 2 k=2.

If σ = 2 ​ τ \sigma=2\tau is even, then cos ⁡ ( θ) = ( 4 ​ τ 2 − 2 ​ ϱ 2) / ( 4 ​ τ 2) = ( 2 ​ τ 2 − ϱ 2) / ( 2 ​ τ 2) = r / s \cos(\theta)=(4\tau^{2}-2\varrho^{2})/(4\tau^{2})=(2\tau^{2}-\varrho^{2})/(2\tau^{2})=r/s is a coprime representation with s s even and r r odd. Let a = σ a=\sigma and c = 2 ​ a ​ sin ⁡ ( θ / 2) = 2 ​ ϱ c=2a\sin(\theta/2)=2\varrho. Then the isosceles rational θ \theta -triangle with sides a, a, c a,a,c has the area ( a 2 / 2) ​ sin ⁡ ( θ) = ( σ 2 / 2) ​ 1 − cos 2 ⁡ ( θ) = ( σ 2 / 2) ​ ( s 2 − r 2) / s 2 = ( σ 2 / ( 2 ​ s)) ​ s 2 − r ​ 2 = ( σ 2 / ( 4 ​ τ 2)) ​ s 2 − r 2 = s 2 − r 2 (a^{2}/2)\sin(\theta)=(\sigma^{2}/2)\sqrt{1-\cos^{2}(\theta)}=(\sigma^{2}/2)\sqrt{(s^{2}-r^{2})/s^{2}}=\bigl(\sigma^{2}/(2s)\bigr)\sqrt{s^{2}-r2}=\bigl(\sigma^{2}/(4\tau^{2})\bigr)\sqrt{s^{2}-r^{2}}=\sqrt{s^{2}-r^{2}}, so that this triangle is the unique solution with k = 1 k=1. □ \square. ∎

###### Remark 4.9.

The equilateral triangle with all three sides of length 2 2 plays a somewhat special role. First, it is the unique isosceles rational π / 3 \pi/3 -triangle with area k ​ 3 k\sqrt{3} and squarefree k ∈ ℕ k\in\mathbb{N}; in fact, k = 1 k=1. Furthermore, there is no other rational π / 3 \pi/3 -triangle with area 3 \sqrt{3}, since the rank of the Mordell-Weil group E ℚ ​ ( − 1, 3) E_{\mathbb{Q}}(-1,3) is zero (cf. [O1] or [Y1]). For any squarefree k > 1 k>1 there are either no rational π / 3 \pi/3 -triangles with area k ​ 3 k\sqrt{3} at all, or else there are infinitely many such triangles. The only case in which there is a single solution is the case k = 1 k=1 with the above-mentioned equilateral triangle.

The possibility of freely moving between the concordant form problem and the generalized congruent number problem provides a way of translating solutions found for one of these problems to solutions of the other problem. For example, various interesting examples of concordant forms and of triplets of rational squares in arithmetic progressions can be obtained from the examples for rational 2 ​ π / 3 2\pi/3 -triangles found in [Ka]. Conversely, examples for concordant forms given in [O1] can be used to construct rational θ \theta -triangles.

## References

- [1]
- [Ca] J. W. S. Cassels, *Lectures on Elliptic Curves*, Cambridge University Press 1991.
- [Co1] I. Connell, *Elliptic Curve Handbook*, available on the internet via http://www.math.mcgill.ca/connell/.
- [Co2] K. Conrad, *Arithmetic Progression of Four Squares*, arXiv:0909.1642v1, 2009.
- [E] L. Euler, *De binis formulis speciei xx+myy et xx+nyy inter se concordibus et discordibus*, Mem. Acad. Sci. St.-Petersbourg 1780 (Opera Omnia: Ser. 1, Vol. 5, pp. 406–413).
- [F1] M. Fujiwara, *θ \theta -congruent numbers*, in: K. Györy et al. (eds.), *Number theory*, de Gruyter, Berlin 1998, 235–241.
- [F2] M. Fujiwara, *Some properties of θ \theta -congruent numbers*, Natural Science Report, Ochanomizu Univeristy, vol. 52, no. 2, 2001.
- [GS] E. Gonzàles-Jiménez and J. Steuding, *Arithmetic progressions of four squares over quadratic fields*, Publ. Math. Debrecen 77 (1-2), 2010, 125–138.
- [GX] E. Gonzàles-Jiménez and X. Xarles, *Five Squares in Arithmetic Progression over Quadratic Fields*, arXiv:0909.1663v3[math.NT].
- [H] D. Husemöller, *Elliptic Curves*, Springer, New York 2004.
- [I] B.-H. Im, *Concordant Numbers within Arithmetic Progressions and Elliptic Curves*, Proc. Amer. Math. Soc. 141 (3), 2013, 791–800.
- [JSDP] A. S. Janfada, S. Salami, A. Dujella, J. C. Peral, *On the high rank π / 3 \pi/3 - and 2 ​ π / 3 2\pi/3 -congruent number elliptic curves*, Rocky Mountain Journal of Mathematics (1), 2014.
- [Ka] M. Kan, *θ \theta -congruent numbers and elliptic curves*, Acta Arithmetica 94 (2), 2000, 153–160.
- [Ko] N. Koblitz, *Introduction to Elliptic Curves and Modular Forms*, Springer, New York/Berlin/Heidelberg 1993.
- [M] B. Mazur, *Modular curves and the Eisenstein ideal*, Publications mathématiques de l’I.H.E.S 47 (2), 1977, 33–186.
- [O1] K. Ono, *Euler’s Concordant Forms*, Acta arithmetica LXXVIII (2), 1996, 101–123.
- [O2] T. Ono, *Variations on a Theme of Euler*, Plenum Press, New York and London 1994.
- [ST] J. H. Silverman, J. Tate, *Rational Points on Elliptic Curves*, Springer, New York 1992.
- [TY] J. Top and N. Yui, *Congruent number problems and their variants*, Algorithmic Number Theory 44 (2008), 613–639.
- [T] J. B. Tunnell, *A classical Diophantine problem and modular forms of weight 3/2*, Invent. Math. 72 (2), (1983), 323–334.
- [X] X. Xarles, *Squares in Arithmetic Progression over Number Fields*, Journal of Number Theory 132 (3), March 2012, 379–389.
- [Y1] S. Yoshida, *Some Variants of the Congruent Number Problem I*, Kyushu J. Math. 55 (2001), 387–404.
- [Y2] S. Yoshida, *Some Variants of the Congruent Number Problem II*, Kyushu J. Math. 56 (2002), 147–165.
- [Y3] S. Yoshida, *Some Variants of the Congruent Number Problem III*, Technical Report, Chiba University.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
