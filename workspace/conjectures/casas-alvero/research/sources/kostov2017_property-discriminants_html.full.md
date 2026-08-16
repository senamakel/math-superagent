<!-- source: https://arxiv.org/html/1701.02912v1 | converted from HTML -->

A property of discriminants

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1701.02912v1 [math.CA] 11 Jan 2017

# A property of discriminants

Vladimir Petrov Kostov Affiliation: Université Côte d’Azur, CNRS, LJAD, France Affiliation: e-mail: kostov@math.unice.fr

###### Abstract

For the family P:= x n + a 1 ​ x n − 1 + ⋯ + a n P:=x^{n}+a_{1}x^{n-1}+\cdots+a_{n} of complex polynomials in the variable x x we study its discriminant R:= R:= Res ( P, P ′, x) (P,P^{\prime},x), R ∈ ℂ ⁡ [a] R\in\mathbb{C}[a], a = ( a 1, …, a n) a=(a_{1},\ldots,a_{n}). When R R is regarded as a polynomial in a k a_{k}, one can consider its discriminant D ~ k:= \tilde{D}_{k}:= Res ( R, ∂ R / ∂ a k, a k) (R,\partial R/\partial a_{k},a_{k}). We show that D ~ k = c k ​ ( a n) d ⁡ ( n, k) ​ M k 2 ​ T k 3 \tilde{D}_{k}=c_{k}(a_{n})^{d(n,k)}M_{k}^{2}T_{k}^{3}, where c k ∈ ℚ ∗ c_{k}\in\mathbb{Q}^{*}, d ⁡ ( n, k):= min ⁡ ( 1, n − k) + max ⁡ ( 0, n − k − 2) d(n,k):=\min(1,n-k)+\max(0,n-k-2), the polynomials M k, T k ∈ ℂ ⁡ [a k] M_{k},T_{k}\in\mathbb{C}[a^{k}] have integer coefficients, a k = ( a 1, …, a k − 1, a k + 1, …, a n) a^{k}=(a_{1},\ldots,a_{k-1},a_{k+1},\ldots,a_{n}), the sets { M k = 0 } \{M_{k}=0\} and { T k = 0 } \{T_{k}=0\} are the projections in the space of the variables a k a^{k} of the closures of the strata of the variety { R = 0 } \{R=0\} on which P P has respectively two double roots or a triple root. Set P k:= P − x ​ P ′ / ( n − k) P_{k}:=P-xP^{\prime}/(n-k) for 1 ≤ k ≤ n − 1 1\leq k\leq n-1 and P n:= P ′ P_{n}:=P^{\prime}. One has T k = T_{k}= Res ( P k, P k ′, x) (P_{k},P_{k}^{\prime},x) for k ≠ n − 1 k\neq n-1 and T n − 1 = T_{n-1}= Res ( P n − 1, P n − 1 ′, x) / a n (P_{n-1},P_{n-1}^{\prime},x)/a_{n}.

AMS classification: 12E05; 12D05

Key words: polynomial in one variable; discriminant set; resultant; multiple root

## 1 Introduction

In the present paper we consider the general family of monic degree n n complex polynomials in one variable P:= x n + a 1 ​ x n − 1 + ⋯ + a n P:=x^{n}+a_{1}x^{n-1}+\cdots+a_{n}. (For a 1 = 0 a_{1}=0 this is the versal deformation of the A n − 1 A_{n-1} -singularity, see [2]). Its discriminant is the resultant R:= R:= Res ( P, P ′, x) (P,P^{\prime},x), i.e. the determinant of the Sylvester matrix S ⁡ ( P, P ′, x) S(P,P^{\prime},x). We remind that S ⁡ ( P, P ′, x) S(P,P^{\prime},x) is ( 2 ​ n − 1) × ( 2 ​ n − 1) (2n-1)\times(2n-1), its first (resp. n n th) row equals

 | ( 1, a 1, …, a n, 0, …, 0) ( resp. ( n, ( n − 1) a 1, …, a n − 1, 0, …, 0)), (1,a_{1},\ldots,a_{n},0,\ldots,0)~~~~\,\,\,\,{\rm(resp.}~~\,(n,(n-1)a_{1},\ldots,a_{n-1},0,\ldots,0)~~{\rm)}~, |  |

its second (resp. ( n + 1) (n+1) st) row is obtained by shifting the first (resp. the n n th) one to the right by one position while adding 0 0 to the left etc. Set a:= ( a 1, …, a n) a:=(a_{1},\ldots,a_{n}), a k:= ( a 1, …, a k − 1, a k + 1, …, a n) a^{k}:=(a_{1},\ldots,a_{k-1},a_{k+1},\ldots,a_{n}) and R a k:= ∂ R / ∂ a k R_{a_{k}}:=\partial R/\partial a_{k}. It is well-known that:

A) R R is a quasi-homogeneous polynomial in the coefficients a j a_{j}, where the quasi-homogeneous weight of a j a_{j} equals j j. It is a degree n n polynomial in each of the variables a j a_{j}, 1 ≤ j ≤ n − 1 1\leq j\leq n-1, and a degree n − 1 n-1 polynomial in a n a_{n}.

B) The set { R = 0 } \{R=0\} is the set of values of the coefficients a j a_{j} for which P P has a multiple root. It contains the subsets Σ \Sigma and M ~ \tilde{M} (the Maxwell stratum) such that for a ∈ Σ a\in\Sigma (resp. a ∈ M ~ a\in\tilde{M}) the polynomial P P has a root of multiplicity 3 3 (resp. has two different double roots). The semi-algebraic sets Σ \Sigma and M ~ \tilde{M} are irreducible. Indeed, the closure of Σ \Sigma is the image of the map ℂ n − 2 → ℂ n − 2 \mathbb{C}^{n-2}\rightarrow\mathbb{C}^{n-2}, ( z 1, z 4, z 5, …, z n) ↦ a (z_{1},z_{4},z_{5},\ldots,z_{n})\mapsto a, where in the computation of ( − 1) j ​ a j (-1)^{j}a_{j} as j j th elementary symmetric function of z 1 z_{1}, … \ldots, z n z_{n} one sets z 2 = z 3 = z 1 z_{2}=z_{3}=z_{1}; the closure of M ~ \tilde{M} is the image of the map ℂ n − 2 → ℂ n − 2 \mathbb{C}^{n-2}\rightarrow\mathbb{C}^{n-2}, ( z 1, z 3, z 5, z 6 ​ …, z n) ↦ a (z_{1},z_{3},z_{5},z_{6}\ldots,z_{n})\mapsto a, where in the computation of a a one sets z 2 = z 1 z_{2}=z_{1} and z 4 = z 3 z_{4}=z_{3}. It is easy to see that the intersections of the sets Σ \Sigma and M ~ \tilde{M} with each of the subspaces { a j = 0 } \{a_{j}=0\} are proper subsets of Σ \Sigma and M ~ \tilde{M}.

One can consider R R as a polynomial in a k a_{k}, with coefficients in ℂ ⁡ [a k] \mathbb{C}[a^{k}]. Thus one is led to consider the repeated resultants D ~ k:= \tilde{D}_{k}:= Res ( R, R a k, a k) (R,R_{a_{k}},a_{k}). The following result is proved in [5] (see Proposition 7 there):

###### Lemma 1.

Set d ⁡ ( n, k):= min ⁡ ( 1, n − k) + max ⁡ ( 0, n − k − 2) d(n,k):=\min(1,n-k)+\max(0,n-k-2). The polynomial D ~ k \tilde{D}_{k} equals ( a n) d ⁡ ( n, k) ​ D k 0 ~ (a_{n})^{d(n,k)}\tilde{D^{0}_{k}}, where D k 0 ~ ∈ ℂ ⁡ [a] \tilde{D^{0}_{k}}\in\mathbb{C}[a] is not divisible by any of the variables a i a_{i}, 1 ≤ i ≤ n 1\leq i\leq n.

###### Example 2.

For n = 3 n=3 one has P:= x 3 + a ​ x 2 + b ​ x + c P:=x^{3}+ax^{2}+bx+c, P ′ = 3 ​ x 2 + 2 ​ a ​ x + b P^{\prime}=3x^{2}+2ax+b and

 | R:= Res ⁡ ( P, P ′, x) = 4 ​ a 3 ​ c − a 2 ​ b 2 − 18 ​ a ​ b ​ c + 4 ​ b 3 + 27 ​ c 2. R:={\rm Res}(P,P^{\prime},x)=4a^{3}c-a^{2}b^{2}-18abc+4b^{3}+27c^{2}~. |  |

Set D ~ a:= \tilde{D}_{a}:= Res ( R, ∂ R / ∂ a, a) (R,\partial R/\partial a,a) and similarly for D ~ b \tilde{D}_{b} and D ~ c \tilde{D}_{c}. Hence

 | D ~ a = − 64 ​ c ​ ( b 3 − 27 ​ c 2) 3, D ~ b = − 64 ​ c ​ ( a 3 − 27 ​ c) 3 ​ and ​ D ~ c = − 432 ​ ( − 3 ​ b + a 2) 3. \tilde{D}_{a}=-64c(b^{3}-27c^{2})^{3}~~,~~\tilde{D}_{b}=-64c(a^{3}-27c)^{3}~~{\rm and}~~\tilde{D}_{c}=-432(-3b+a^{2})^{3}~. |  |

###### Example 3.

For n = 4 n=4 one has P:= x 4 + a ​ x 3 + b ​ x 2 + c ​ x + d P:=x^{4}+ax^{3}+bx^{2}+cx+d, P ′ = 4 ​ x 3 + 3 ​ a ​ x 2 + 2 ​ b ​ x + c P^{\prime}=4x^{3}+3ax^{2}+2bx+c and

 | R: ⁣ = Res ⁡ ( P, P ′, x) = − 27 ​ a 4 ​ d 2 + 18 ​ a 3 ​ b ​ c ​ d − 4 ​ a 3 ​ c 3 + a 2 ​ b 2 ​ c 2 + 144 ​ a 2 ​ b ​ d 2 − 4 ​ a 2 ​ b 3 ​ d − 6 ​ a 2 ​ c 2 ​ d − 80 ​ a ​ b 2 ​ c ​ d + 18 ​ a ​ b ​ c 3 − 192 ​ a ​ c ​ d 2 + 16 ​ b 4 ​ d − 4 ​ b 3 ​ c 2 − 128 ​ b 2 ​ d 2 + 144 ​ b ​ c 2 ​ d − 27 ​ c 4 + 256 ​ d 3. \begin{array}[]{ccccl}R&:=&{\rm Res}(P,P^{\prime},x)&=&-27a^{4}d^{2}+18a^{3}bcd-4a^{3}c^{3}+a^{2}b^{2}c^{2}+144a^{2}bd^{2}-4a^{2}b^{3}d\\ &&&&-6a^{2}c^{2}d-80ab^{2}cd+18abc^{3}-192acd^{2}+16b^{4}d\\ &&&&-4b^{3}c^{2}-128b^{2}d^{2}+144bc^{2}d-27c^{4}+256d^{3}~.\end{array} |  |

One finds that

 | D ~ a = 6912 ​ d 2 ​ M a 2 ​ T a 3, D ~ b = − 4096 ​ d ​ M b 2 ​ T b 3, D ~ c = 6912 ​ d ​ M c 2 ​ T c 3 ​ and ​ D ~ d = 4096 ​ M d 2 ​ T d 3, \tilde{D}_{a}=6912d^{2}M_{a}^{2}T_{a}^{3}~~,~~\tilde{D}_{b}=-4096dM_{b}^{2}T_{b}^{3}~~,~~\tilde{D}_{c}=6912dM_{c}^{2}T_{c}^{3}~~{\rm and}~~\tilde{D}_{d}=4096M_{d}^{2}T_{d}^{3}~~, |  |

where the factors M a M_{a}, T a T_{a}, M b M_{b}, … \ldots, T d T_{d} are irreducible:

 | M a = 16 ​ b 2 ​ d 2 − 8 ​ b ​ c 2 ​ d + c 4 − 64 ​ d 3, T a = 3 ​ b 4 ​ d − b 3 ​ c 2 + 72 ​ b 2 ​ d 2 − 108 ​ b ​ c 2 ​ d + 27 ​ c 4 + 432 ​ d 3 M b = a 2 ​ d − c 2, T b = 27 ​ a 4 ​ d 2 − a 3 ​ c 3 − 6 ​ a 2 ​ c 2 ​ d − 768 ​ a ​ c ​ d 2 + 27 ​ c 4 + 4096 ​ d 3 M c = a 4 − 8 ​ a 2 ​ b + 16 ​ b 2 − 64 ​ d, T c = 27 ​ a 4 ​ d − a 2 ​ b 3 − 108 ​ a 2 ​ b ​ d + 3 ​ b 4 + 72 ​ b 2 ​ d + 432 ​ d 2 M d = a 3 − 4 ​ a ​ b + 8 ​ c, T d = 27 ​ a 3 ​ c − 9 ​ a 2 ​ b 2 − 108 ​ a ​ b ​ c + 32 ​ b 3 + 108 ​ c 2. \begin{array}[]{lcl}M_{a}=16b^{2}d^{2}-8bc^{2}d+c^{4}-64d^{3}&,&T_{a}=3b^{4}d-b^{3}c^{2}+72b^{2}d^{2}-108bc^{2}d+27c^{4}+432d^{3}\\ \\ M_{b}=a^{2}d-c^{2}&,&T_{b}=27a^{4}d^{2}-a^{3}c^{3}-6a^{2}c^{2}d-768acd^{2}+27c^{4}+4096d^{3}\\ \\ M_{c}=a^{4}-8a^{2}b+16b^{2}-64d&,&T_{c}=27a^{4}d-a^{2}b^{3}-108a^{2}bd+3b^{4}+72b^{2}d+432d^{2}\\ \\ M_{d}=a^{3}-4ab+8c&,&T_{d}=27a^{3}c-9a^{2}b^{2}-108abc+32b^{3}+108c^{2}~.\end{array} |  |

One can notice that the equation M b = 0 M_{b}=0 defines the Whitney umbrella.

We prove the following theorem:

###### Theorem 4.

For n ≥ 4 n\geq 4 the polynomial D ~ k \tilde{D}_{k} is of the form c k ​ ( a n) d ⁡ ( n, k) ​ M k 2 ​ T k 3 c_{k}(a_{n})^{d(n,k)}M_{k}^{2}T_{k}^{3}, where c k ∈ ℚ ∗ c_{k}\in\mathbb{Q}^{*}, the degree d ⁡ ( n, k) d(n,k) is defined in Lemma 1 and the polynomials M k, T k ∈ ℂ ⁡ [a k] M_{k},T_{k}\in\mathbb{C}[a^{k}] are with integer coefficients and irreducible. The zero sets of these polynomials are the closures of the projections in the space of the variables a k a^{k} of the sets M ~ \tilde{M} and Σ \Sigma.

The proofs of Theorem 4, Lemma 7 and Lemma 8 are to be found in Section 3.

Acknowledgement. The author is grateful to B.Z. Shapiro from the University of Stockholm for the formulation of the problem and its subsequent discussions.

## 2 Comments and lemmas

Theorem 4 is formulated for n ≥ 4 n\geq 4 because for n < 4 n<4 the set M ~ \tilde{M} does not exist. In Example 2 only the cubes of the factors T k T_{k} and the powers of a n a_{n} (i.e. of c c) are present.

It is well-known that R = ∏ 1 ≤ i < j ≤ n ( z i − z j) 2 R=\prod_{1\leq i<j\leq n}(z_{i}-z_{j})^{2}. Denote by Δ \Delta the union of hyperplanes { z i = z j } \{z_{i}=z_{j}\} in the space ℂ n \mathbb{C}^{n} of the roots of the polynomial P P. In the last presentation of R R as a product it is necessary to have the differences of roots z i − z j z_{i}-z_{j} squared because when the roots change continuously along a loop avoiding the set Δ \Delta so that in the end two of them are exchanged, then such an exchange should not change the value of R R.

By analogy, the fact that the power of the factor T k T_{k} in the formula for D ~ k \tilde{D}_{k} in Theorem 4) is a multiple of 3 3 can be explained like this. At a point a = a ∗ ∈ Σ a=a^{*}\in\Sigma (we assume that a ∗ ∉ Σ ¯ \ Σ a^{*}\not\in\bar{\Sigma}\backslash\Sigma) three roots z 1 z_{1}, z 2 z_{2}, z 3 z_{3} of P P coalesce. For fixed nearby values of a k a^{k} the polynomial R R (when considered as a polynomial in a k a_{k}) has two roots ζ 1 \zeta_{1} and ζ 2 \zeta_{2} that coalesce for a k = a ∗ k a^{k}={a^{*}}^{k} (the projection of a ∗ a^{*} in the space of the variables a k a^{k}). These roots correspond to equalities and inequalities between the roots of P P of the form z 1 = z 2 ≠ z 3 z_{1}=z_{2}\neq z_{3} and z 1 ≠ z 2 = z 3 z_{1}\neq z_{2}=z_{3} for a k ≠ a ∗ k a^{k}\neq{a^{*}}^{k}, and to z 1 = z 2 = z 3 z_{1}=z_{2}=z_{3} for a k = a ∗ k a^{k}={a^{*}}^{k}. When the ( n − 1) (n-1) -tuple of coefficients a k a^{k} circumvents the projection Σ k \Sigma_{k} of Σ \Sigma in the space of the variables a k a^{k} along a generic loop, the three roots z i z_{i} of P P undergo a cyclic permutation of order 3 3 and now the roots ζ 1 \zeta_{1} and ζ 2 \zeta_{2} of R R correspond to other equalities and inequalities between the roots z i z_{i}, namely, to z 3 = z 1 ≠ z 2 z_{3}=z_{1}\neq z_{2} and z 3 ≠ z 1 = z 2 z_{3}\neq z_{1}=z_{2}. In order D ~ k \tilde{D}_{k} to be invariant w.r.t. such permutations the power of T k T_{k} dividing the resultant D ~ k \tilde{D}_{k} must be a multiple of 3 3.

For the power of M k M_{k} being even a similar explanation exists. To this end we remind first some facts about R R for n = 4 n=4. The formula for R R was obtained in Example 3. On Fig. 1 we show for real values of c c and d d the sets { R = 0 } | a = 0, b = − 1 \{R=0\}|_{a=0,b=-1}, { R = 0 } | a = b = 0 \{R=0\}|_{a=b=0} and { R = 0 } | a = 0, b = 1 \{R=0\}|_{a=0,b=1} (from left to right) which are symmetric w.r.t. the d d -axis. This figure can be compared with the well-known picture of the swallowtail catastrophe, see [7]. Fig. 1 gives a sufficient idea about the set { R = 0 } | a = 0 \{R=0\}|_{a=0} because the set { R = 0 } \{R=0\} is invariant under the quasi-homogeneous dilatations a ↦ t ​ a a\mapsto ta, b ↦ t 2 ​ b b\mapsto t^{2}b, c ↦ t 3 ​ c c\mapsto t^{3}c, d ↦ t 4 ​ d d\mapsto t^{4}d, t ≠ 0 t\neq 0.

At the points U U and V V the polynomial P P has a triple real and a simple real root ( U U and V V are ordinary 2 / 3 2/3 -cusp points for the real curve { R = 0 } | a = 0, b = − 1 \{R=0\}|_{a=0,b=-1}). One has

 | Σ ∩ { a = 0, b = − 1 } = { U, V }, M ~ ∩ { a = 0, b = − 1 } = { S }. \Sigma\cap\{a=0,b=-1\}=\{U,V\}~~~,~~~\tilde{M}\cap\{a=0,b=-1\}=\{S\}~. |  |

At the point S S (with d d -coordinate equal to 1 / 4 1/4) the curve { R = 0 } | a = 0, b = − 1 \{R=0\}|_{a=0,b=-1} has transversal self-intersection and the polynomial P P has two double real roots. At the point T T (which is an isolated double point of the real curve { R = 0 } | a = 0, b = 1 \{R=0\}|_{a=0,b=1}, with d d -coordinate equal to 1 / 4 1/4) the polynomial P P has a double complex conjugate pair. At the points I I, J J and K K one has c = d = 0 c=d=0. The real curves { R = 0 } | a = 0, b = − 1 \{R=0\}|_{a=0,b=-1} and { R = 0 } | a = 0, b = 1 \{R=0\}|_{a=0,b=1} are smooth at I I and K K respectively while { R = 0 } | a = b = 0 \{R=0\}|_{a=b=0} has a 4 / 3 4/3 -type singularity at J J.

[image: Refer to caption]

Figure 1: The sets { R = 0 } | a = 0, b = − 1 \{R=0\}|_{a=0,b=-1}, { R = 0 } | a = b = 0 \{R=0\}|_{a=b=0} and { R = 0 } | a = 0, b = 1 \{R=0\}|_{a=0,b=1} for n = 4 n=4.

From now on we keep in mind that the set { R = 0 } \{R=0\} can be defined in both contexts – the ones of real or of complex variables x x, a a, b b, c c and d d. In this sense we make use of Fig. 1 as an illustration of the real case and as a hint for the complex one. Why for n = 4 n=4 the powers of the factors M k M_{k} should be even is suggested by the following lemma. For n > 4 n>4 the analogs of the loops γ ¯ \bar{\gamma} and Γ \Gamma of the lemma exist in a neighbourhood of any value of the parameters a j a_{j} for which the polynomial P P has a quadruple root, but their explicit construction is harder to describe.

###### Lemma 5.

In the complex case there exists a loop γ ¯ \bar{\gamma} belonging to the space of variables ( b, c) (b,c) which can be lifted to a loop Γ ⊂ { R = 0 } | a = 0 \Gamma\subset\{R=0\}|_{a=0} circumventing the set Σ ∪ M ~ ¯ \overline{\Sigma\cup\tilde{M}} such that any fibre of the projection Γ → γ ¯ \Gamma\rightarrow\bar{\gamma} consists of two points and the monodromy defined on the fibre after one turn along γ ¯ \bar{\gamma} is nontrivial.

###### Proof.

In what follows an additional index d d denotes the projection of a given set in the space of variables ( b, c, d) (b,c,d) ( a a is presumed equal to 0 0) into the space of variables ( b, c) (b,c). Consider the point A A on Fig. 1. We are going to construct a continuous path γ ⊂ { R = 0 } | a = 0 \gamma\subset\{R=0\}|_{a=0} leading from A A to G G, one of the two points of { R = 0 } | a = 0 \{R=0\}|_{a=0} which share with A A the same b b - and c c -coordinates as shown on Fig. 1. As b b increases from − 1 -1 to 1 1, the point A A becomes the point B B for b = 0 b=0 and then C C for b = 1 b=1. Then we decrease c c by keeping the same value of b b – this gives the arc C ​ K ​ D CKD. Then we fix c c and decrese b b – this gives the arc D ​ E ​ F DEF. Finally we add the arc F ​ G FG. The thus constructed path is real. Three remarks will be needed for what follows:

1) The path γ \gamma, in its part between the points A A and F F, can be constructed as symmetric w.r.t. the plane { c = 0 } \{c=0\}.

2) The projection Σ d \Sigma_{d} of Σ \Sigma is defined by 32 ​ b 3 + 108 ​ c 2 = 0 32b^{3}+108c^{2}=0, i.e. 8 ​ b 3 + 27 ​ c 2 = 0 8b^{3}+27c^{2}=0; the equation of this semi-cubic parabola is obtained from the equation T d = 0 T_{d}=0 by setting a = 0 a=0, see Example 3. There exists a unique number b 0 ∈ ( − 1, 0) b_{0}\in(-1,0) such that for b = b 0 b=b_{0} the projection γ d \gamma_{d} of γ \gamma intersects Σ d \Sigma_{d} at two points ( b 0, ± c 0) (b_{0},\pm c_{0}).

3) In the real case the path γ \gamma has to pass through the point S ∈ M ~ S\in\tilde{M}, but in the complex one γ \gamma can be modified so that it circumvent S S. The points of the modified path γ \gamma which are close to S S do not have all their coordinates real.

Now we construct (in the complex case) a path γ 1 ⊂ { R = 0 } | a = 0 \gamma^{1}\subset\{R=0\}|_{a=0} leading from G G to A A and satisfying the condition γ d 1 = γ d \gamma^{1}_{d}=\gamma_{d}. At the same time we modify the path γ \gamma in order to have this condition. If the path γ 1 \gamma_{1} is defined such that γ d 1 = γ d \gamma^{1}_{d}=\gamma_{d}, then for b = b 0 b=b_{0}, γ 1 \gamma_{1} will intersect the set Σ \Sigma. Therefore for b b close to b 0 b_{0} we modify γ 1 \gamma_{1} and γ \gamma so that γ 1 \gamma^{1} avoid the set Σ \Sigma. (We make two such modifications, corresponding to points of γ d \gamma_{d} and γ d 1 \gamma^{1}_{d} close to ( b 0, c 0) (b_{0},c_{0}) and to ( b 0, − c 0) (b_{0},-c_{0}). The modifications can be made symmetrically w.r.t. the plane { c = 0 } \{c=0\}.)

For the values of b b close to b 0 b_{0} the points of γ \gamma do not have all their coordinates real. As for γ 1 \gamma^{1}, its points do not have all coordinates real not only for b b close to b 0 b_{0}, but also for b ∈ [b 0, 1] b\in[b_{0},1] (recall the construction of the arcs A ​ B ​ C ABC and D ​ E ​ F DEF of γ \gamma) and for b = 1 b=1, c ≠ 0 c\neq 0 (recall the construction of its arc C ​ K ​ D CKD). Indeed, as R R is a degree 3 3 polynomial in d d, then in the real case it has either three real roots (see for instance the vertical line on the left part of Fig. 1 which intersects the set { R = 0 } \{R=0\} at three points two of which are A A and G G) or one real and two complex conjugate ones; this is, in particular, the case of any vertical line different from the d d -axis for b = 1 b=1, see the right part of Fig. 1. (The d d -axis on the right part of the figure corresponds to one simple root at 0 0 and a double one at 1 / 4 1/4. One simple and one double real root is also the situation observed on the vertical lines passing through the points U U and V V.)

To obtain the proof of the lemma one sets γ ¯ = γ d = γ d 1 \bar{\gamma}=\gamma_{d}=\gamma^{1}_{d} and one defines the loop Γ \Gamma as the concatenation of γ \gamma and γ 1 \gamma^{1}. For points of γ \gamma and γ 1 \gamma^{1} close to the point S S one has γ d = γ d 1 \gamma_{d}=\gamma^{1}_{d} and no self-intersection of Γ \Gamma takes place. ∎

###### Remarks 6.

(1) To prove Theorem 4 we need to recall some notation and results from [5]. Suppose that G 1 G_{1} and G 2 G_{2} are polynomials in several variables one of which is denoted by y y. By S ⁡ ( G 1, G 2, y) S(G_{1},G_{2},y) we denote the Sylvester matrix of G 1 G_{1} and G 2 G_{2} when considered as polynomials in y y. We set P k:= P − x ​ P ′ / ( n − k) P_{k}:=P-xP^{\prime}/(n-k) for 1 ≤ k ≤ n − 1 1\leq k\leq n-1 and P n:= P ′ P_{n}:=P^{\prime}.

(2) It is shown in [5] that for k ≠ n − 1 k\neq n-1 the polynomial V k:= V_{k}:= Res ( P k, P k ′, x) (P_{k},P_{k}^{\prime},x) is irreducible and that the polynomial Res ( P n − 1, P n − 1 ′, x) (P_{n-1},P_{n-1}^{\prime},x) is the product of a n a_{n} and an irreducible polynomial in a n − 1 a^{n-1}. We set V n − 1:= V_{n-1}:= Res ( P n − 1, P n − 1 ′, x) / a n (P_{n-1},P_{n-1}^{\prime},x)/a_{n}. It follows from Theorem 12 of [5] that V k = T k V_{k}=T_{k}, k = 1, …, n k=1,\ldots,n. Theorem 4 allows to find the polynomials M k M_{k} and T k T_{k}; however the definition of T k T_{k} as T k = V k T_{k}=V_{k} is an easier way to find T k T_{k}.

(3) We denote by QHD ( U) (U) the quasi-homogeneous degree of a quasi-homogeneous polynomial U ∈ ℂ ⁡ [a] U\in\mathbb{C}[a], where the quasi-homogeneous weight of a k a_{k} is k k.

(4) Set Q k:= ( n − k) ​ P k = ( n − k) ​ P − x ​ P ′ Q_{k}:=(n-k)P_{k}=(n-k)P-xP^{\prime}, k ≤ n − 1 k\leq n-1, Q n:= P ′ Q_{n}:=P^{\prime}. When we compare polynomials P k P_{k}, Q k Q_{k}, R R or V k V_{k} for two consecutive values of n n (i.e. for n n and n + 1 n+1) we write P k n P_{k}^{n}, P k n + 1 P_{k}^{n+1}, Q k n Q_{k}^{n}, Q k n + 1 Q_{k}^{n+1}, R n R^{n}, R n + 1 R^{n+1} or V k n V_{k}^{n}, V k n + 1 V_{k}^{n+1}. Notice that as Q k = − k ​ x n + ∑ j = 1 n ( j − k) ​ a j ​ x n − j Q_{k}=-kx^{n}+\sum_{j=1}^{n}(j-k)a_{j}x^{n-j}, one has

 | Q k n + 1 = x ​ Q k n + ( n + 1 − k) ​ a n + 1 ​ and ​ ( Q k n + 1) ′ = x ​ ( Q k n) ′ + Q k n. Q_{k}^{n+1}=xQ_{k}^{n}+(n+1-k)a_{n+1}~~{\rm and}~~(Q_{k}^{n+1})^{\prime}=x(Q_{k}^{n})^{\prime}+Q_{k}^{n}~. |  | (1) |

In the following lemma and its proof Ω \Omega denotes nonspecified nonzero rational numbers.

###### Lemma 7.

(1) One has V ∗:= V k n + 1 | a n + 1 = 0 = Ω ​ ( a n) 2 ​ V k n V_{*}:=V_{k}^{n+1}|_{a_{n+1}=0}=\Omega(a_{n})^{2}V_{k}^{n} for 1 ≤ k ≤ n − 2 1\leq k\leq n-2, V ∗ = Ω ​ ( a n) 3 ​ V k n V_{*}=\Omega(a_{n})^{3}V_{k}^{n} for k = n − 1 k=n-1 and V ∗ = Ω ​ ( a n − 1) 3 ​ V k n V_{*}=\Omega(a_{n-1})^{3}V_{k}^{n} for k = n k=n.

(2) One has R n + 1 | a n + 1 = 0 = ± a n 2 ​ R n R^{n+1}|_{a_{n+1}=0}=\pm a_{n}^{2}R^{n}.

The following lemma announces the quasi-homogeneous degrees of certain polynomials that appear in this text:

###### Lemma 8.

For n ≥ 4 n\geq 4 one has the following quasi-homogeneous degrees of polynomials:

(1) QHD ( R) = (R)= QHD ( V k) = n ⁡ ( n − 1) (V_{k})=n(n-1), 1 ≤ k ≤ n − 2 1\leq k\leq n-2.

(2) QHD ( V n − 1) = n ⁡ ( n − 2) (V_{n-1})=n(n-2).

(3) QHD ( V n) = ( n − 1) ​ ( n − 2) (V_{n})=(n-1)(n-2).

(4) QHD ( R a k) = n ⁡ ( n − 1) − k (R_{a_{k}})=n(n-1)-k, 1 ≤ k ≤ n − 2 1\leq k\leq n-2, QHD ( R a n − 1) = n 2 − 3 ​ n + 1 (R_{a_{n-1}})=n^{2}-3n+1, QHD ( R a n) = n 2 − 4 ​ n + 2 (R_{a_{n}})=n^{2}-4n+2.

(5) QHD ( D ~ k) = n ​ ( n − 1) 2 + n 2 ​ ( n − k − 1) (\tilde{D}_{k})=n(n-1)^{2}+n^{2}(n-k-1), 1 ≤ k ≤ n − 1 1\leq k\leq n-1, QHD ( D ~ n) = n ⁡ ( n − 1) ​ ( n − 2) (\tilde{D}_{n})=n(n-1)(n-2).

(6) QHD ( M k) = n 3 − 3 ​ n 2 + 2 ​ n − ( n 2 − n) ​ ( k + 1) / 2 (M_{k})=n^{3}-3n^{2}+2n-(n^{2}-n)(k+1)/2, 1 ≤ k ≤ n − 2 1\leq k\leq n-2, QHD ( M n − 1) = n ⁡ ( n − 2) ​ ( n − 3) / 2 (M_{n-1})=n(n-2)(n-3)/2, QHD ( M n) = ( n − 1) ​ ( n − 2) ​ ( n − 3) / 2 (M_{n})=(n-1)(n-2)(n-3)/2.

## 3 Proofs

###### Proof of Lemma 7.

The equality A = [B] ℓ, r A=[B]_{\ell,r} means that the matrix A A is obtained from the matrix B B by deleting its ℓ \ell th row and r r th column. Prove part (1). In the proof of the lemma we use the polynomials Q k Q_{k} instead of P k P_{k}. For 1 ≤ k ≤ n − 2 1\leq k\leq n-2 set Q ∗:= Q k n + 1 | a n + 1 = 0 = x ​ Q k n Q_{*}:=Q_{k}^{n+1}|_{a_{n+1}=0}=xQ_{k}^{n}. Consider the ( 2 ​ n + 1, 2 ​ n + 1) (2n+1,2n+1) -Sylvester matrix S ∗:= S ⁡ ( Q ∗, Q ∗ ′, x) S_{*}:=S(Q_{*},Q_{*}^{\prime},x). The only nonzero entry in its last column is Ω ​ a n \Omega a_{n} in position ( 2 ​ n + 1, 2 ​ n + 1) (2n+1,2n+1). Hence when finding its determinant Ω ​ V ∗ \Omega V_{*} one can develop it w.r.t. the last column to obtain V ∗ = Ω ​ a n ​ V ∗ ⁣ ∗ V_{*}=\Omega a_{n}V_{**}, where V ∗ ⁣ ∗ = det S ∗ ⁣ ∗ V_{**}=\det S_{**}, S ∗ ⁣ ∗ = [S ∗] 2 ​ n + 1, 2 ​ n + 1 S_{**}=[S_{*}]_{2n+1,2n+1}.

Subtract for j = 1, …, n j=1,\ldots,n the j j th row of S ∗ ⁣ ∗ S_{**} from its ( n + j) (n+j) th row. This doesn’t change V ∗ ⁣ ∗ V_{**}. Hence the terms Ω ​ a n \Omega a_{n} disappear in the ( n + 1) (n+1) st, … \ldots, ( 2 ​ n) (2n) th rows of S ∗ ⁣ ∗ S_{**}, see ( 1). The only nonzero entry of the new matrix (denoted by S ∗ ∗ ∗ S_{***}) in its last column is Ω ​ a n \Omega a_{n} in position ( n, 2 ​ n) (n,2n). It is easy to see that [S ∗ ∗ ∗] n, 2 ​ n = S ( Q k n, ( Q k n) ′, x) [S_{***}]_{n,2n}=S(Q_{k}^{n},(Q_{k}^{n})^{\prime},x) (this can be deduced from ( 1)). Hence V ∗ ⁣ ∗ = det S ∗ ∗ ∗ = Ω a n V k n V_{**}=\det S_{***}=\Omega a_{n}V_{k}^{n} and V ∗ = Ω ​ ( a n) 2 ​ V k n V_{*}=\Omega(a_{n})^{2}V_{k}^{n}.

For k = n − 1 k=n-1 the above reasoning differs only in the end – one defines V n − 1 n V_{n-1}^{n} not as det ( [S ∗ ∗ ∗] n, 2 ​ n) \det([S_{***}]_{n,2n}) (the latter is divisible by a n a_{n}), but as det ( [S ∗ ∗ ∗] n, 2 ​ n) / a n \det([S_{***}]_{n,2n})/a_{n}. Hence V ∗ = Ω ​ ( a n) 3 ​ V n − 1 n V_{*}=\Omega(a_{n})^{3}V_{n-1}^{n}.

For k = n k=n consider the ( 2 ​ n + 1) × ( 2 ​ n + 1) (2n+1)\times(2n+1) -matrix S 0:= S ⁡ ( Q n n + 1, ( Q n n + 1) ′, x) S^{0}:=S(Q_{n}^{n+1},(Q_{n}^{n+1})^{\prime},x). Its last column contains a single nonzero entry ( Ω ​ a n + 1 \Omega a_{n+1} in position ( n, 2 ​ n + 1) (n,2n+1)). By definition det S 0 = Ω ​ a n + 1 ​ V n n + 1 \det S^{0}=\Omega a_{n+1}V_{n}^{n+1}. Hence V ∗ = Ω ​ det S † V_{*}=\Omega\det S^{\dagger}, where S † = ( [S 0] n, 2 ​ n + 1) | a n + 1 = 0 S^{\dagger}=([S^{0}]_{n,2n+1})|_{a_{n+1}=0}.

The last column of S † S^{\dagger} contains a single nonzero entry ( Ω ​ a n − 1 \Omega a_{n-1} in position ( 2 ​ n, 2 ​ n) (2n,2n)), so to find det S † \det S^{\dagger} one can develop it w.r.t. the last column. This gives V ∗ = Ω ​ a n − 1 ​ det S † 0 V_{*}=\Omega a_{n-1}\det S^{\dagger 0}, where S † 0 = [S †] 2 ​ n, 2 ​ n S^{\dagger 0}=[S^{\dagger}]_{2n,2n}.

Subtract the j j th row of S † 0 S^{\dagger 0} from its ( n − 1 + j) (n-1+j) th one, j = 1, …, n − 1 j=1,\ldots,n-1; hence the terms Ω ​ a n − 1 \Omega a_{n-1} disappear in the n n th, … \ldots, ( 2 ​ n − 2) (2n-2) nd rows (see ( 1)). This gives the matrix S † ⁣ ∗ S^{\dagger*} such that det S † ⁣ ∗ = det S † 0 \det S^{\dagger*}=\det S^{\dagger 0}.

The only nonzero entry in the last column of S † ⁣ ∗ S^{\dagger*} is Ω ​ a n − 1 \Omega a_{n-1} in position ( 2 ​ n − 1, 2 ​ n − 1) (2n-1,2n-1). Hence det S † ⁣ ∗ = Ω ​ a n − 1 ​ det S † ⁣ † \det S^{\dagger*}=\Omega a_{n-1}\det S^{\dagger\dagger}, where S † ⁣ † = [S † ⁣ ∗] 2 ​ n − 1, 2 ​ n − 1 S^{\dagger\dagger}=[S^{\dagger*}]_{2n-1,2n-1}. The only nonzero entry of S † ⁣ † S^{\dagger\dagger} in its last column is in position ( n − 1, 2 ​ n − 2) (n-1,2n-2) and equals Ω ​ a n − 1 \Omega a_{n-1}. Thus V ∗ = Ω ( a n − 1) 3 det S † † 0 V_{*}=\Omega(a_{n-1})^{3}\det S^{\dagger\dagger 0}, where S † † 0 = [S † ⁣ †] n − 1, 2 ​ n − 2 S^{\dagger\dagger 0}=[S^{\dagger\dagger}]_{n-1,2n-2}. The ( 2 ​ n − 3) × ( 2 ​ n − 3) (2n-3)\times(2n-3) -matrix S † † 0 S^{\dagger\dagger 0} equals S ⁡ ( Q n n / x, ( Q n n / x) ′, x) S(Q_{n}^{n}/x,(Q_{n}^{n}/x)^{\prime},x), i.e. Ω ​ S ​ ( ( P n) ′, ( P n) ′′, x) \Omega S((P^{n})^{\prime},(P^{n})^{\prime\prime},x).

To prove part (2) one notices that for a n + 1 = 0 a_{n+1}=0 one has P n + 1 = x ​ P n P^{n+1}=xP^{n} and the Sylvester matrix S 1:= S ⁡ ( x ​ P n, ( x ​ P n) ′, x) S^{1}:=S(xP^{n},(xP^{n})^{\prime},x) contains a single nonzero entry in its last column, namely a n a_{n} in position ( 2 ​ n + 1, 2 ​ n + 1) (2n+1,2n+1). Set S 2:= [S 1] 2 ​ n + 1, 2 ​ n + 1 S^{2}:=[S^{1}]_{2n+1,2n+1}. Hence R n + 1 | a n + 1 = 0 = det S 1 = a n ​ det S 2 R^{n+1}|_{a_{n+1}=0}=\det S^{1}=a_{n}\det S^{2}. For j = 1 j=1, … \ldots, n n subtract the j j th row of S 2 S^{2} from its ( n + j) (n+j) th one. The newly obtained matrix (denoted by S 3 S^{3}) has a single nonzero entry in its last column. This is a n a_{n} in position ( n, 2 ​ n) (n,2n). Set S 3:= [S 2] n, 2 ​ n S^{3}:=[S^{2}]_{n,2n}. Hence det S 2 = ± a n det S 3 \det S^{2}=\pm a_{n}\det S^{3}, i.e. R n + 1 | a n + 1 = 0 = ± a n 2 det S 3 R^{n+1}|_{a_{n+1}=0}=\pm a_{n}^{2}\det S^{3}. On the other hand S 3 = S ⁡ ( P n, ( P n) ′, x) S^{3}=S(P^{n},(P^{n})^{\prime},x) from which part (2) follows.

∎

###### Proof of Lemma 8.

We denote by W W any of the polynomials R R, V k V_{k}, k ≤ n − 2 k\leq n-2, or a n ​ V n − 1 a_{n}V_{n-1} and we remind that T k = V k T_{k}=V_{k}, see Remarks 6. Any polynomial W W contains a monomial β ​ a n n − 1 \beta a_{n}^{n-1}, β ≠ 0 \beta\neq 0. Indeed, the only positions in which the matrix S ⁡ ( W, W ′, x) S(W,W^{\prime},x) contains the variable a n a_{n} are ( i, n + i) (i,n+i), i = 1, …, n − 1 i=1,\ldots,n-1; in these positions the matrix has terms of the form η ​ a n \eta a_{n}, η ≠ 0 \eta\neq 0. When det ( S ⁡ ( W, W ′, x)) \det(S(W,W^{\prime},x)) is computed, these terms are multiplied by the constant nonzero terms in positions ( n − 1 + j, j) (n-1+j,j), j = 1, …, n j=1,\ldots,n to give the only monomial of the form β ​ a n n − 1 \beta a_{n}^{n-1} in det ( S ⁡ ( W, W ′, x)) \det(S(W,W^{\prime},x)). Hence QHD ( R) = (R)= QHD ( V k) = (V_{k})= QHD ( a n ​ V n − 1) = n ⁡ ( n − 1) (a_{n}V_{n-1})=n(n-1) which proves parts (1) and (2). The proof of part (3) is analogous (one considers polynomials W W of degree n − 1 n-1 instead of n n and a n − 1 a_{n-1} plays the role of a n a_{n}).

Part (4) follows from parts (1), (2) and (3) – when R R is differentiated w.r.t. a k a_{k}, its quasi-homogeneous degree decreases by k k.

Prove part (5). For a i = 0 a_{i}=0, k ≠ i ≠ n k\neq i\neq n, k < n k<n, one has R = Ω 1 ​ a k n ​ a n n − k − 1 + Ω 2 ​ a n n − 1 R=\Omega_{1}a_{k}^{n}a_{n}^{n-k-1}+\Omega_{2}a_{n}^{n-1}, Ω 1 ≠ 0 ≠ Ω 2 \Omega_{1}\neq 0\neq\Omega_{2}, see Statement 8 in [5]. Therefore the Sylvester matrix S ⁡ ( R, R a k, a k) S(R,R_{a_{k}},a_{k}) has only the following nonzero entries, in the following positions:

 | Ω 1 ​ a n n − k − 1 at ⁡ ( i, i), Ω 2 ​ a n n − 1 at ⁡ ( i, n + i), i = 1, …, n − 1 and n ​ Ω 1 ​ a n n − k − 1 at ⁡ ( n − 1 + j, j), j = 1, …, n. \begin{array}[]{clcclcl}\Omega_{1}a_{n}^{n-k-1}&{\rm at}~~(i,i)&,&\Omega_{2}a_{n}^{n-1}&{\rm at}~~(i,n+i)&,&i=1,\ldots,n-1\\ &&{\rm and}&n\Omega_{1}a_{n}^{n-k-1}&{\rm at}~~(n-1+j,j)&,&j=1,\ldots,n~.\end{array} |  |

Hence its determinant equals Ω ​ a n ( n − 1) 2 + n ⁡ ( n − k − 1) \Omega a_{n}^{(n-1)^{2}+n(n-k-1)}, Ω ≠ 0 \Omega\neq 0 which proves part (5) for k < n k<n.

If k = n k=n and a i = 0 a_{i}=0 for i ≤ n − 2 i\leq n-2, then R = Ω 3 ​ a n n − 1 + Ω 4 ​ a n − 1 n R=\Omega_{3}a_{n}^{n-1}+\Omega_{4}a_{n-1}^{n}, Ω 3 ≠ 0 ≠ Ω 4 \Omega_{3}\neq 0\neq\Omega_{4}. Indeed, the presence of the monomials Ω 3 ​ a n n − 1 \Omega_{3}a_{n}^{n-1} and Ω 4 ​ a n − 1 n \Omega_{4}a_{n-1}^{n} in R R is easy to deduce from the form of the matrix S ⁡ ( P, P ′, x) S(P,P^{\prime},x), and for a i = 0 a_{i}=0 ( i ≤ n − 2 i\leq n-2) there exist no other monomials of quasi-homogeneous weight n ⁡ ( n − 1) n(n-1) in Res ( P, P ′, x) (P,P^{\prime},x). Hence the Sylvester matrix S ⁡ ( R, R a n, a n) S(R,R_{a_{n}},a_{n}) (of size ( 2 ​ n − 3) × ( 2 ​ n − 3) (2n-3)\times(2n-3)) has only the following nonzero entries, in the following positions:

 | Ω 3 at ⁡ ( i, i), Ω 4 ​ a n − 1 n at ⁡ ( i, n − 1 + i), i = 1, …, n − 2 and ( n − 1) ​ Ω 3 at ⁡ ( n − 2 + j, j), j = 1, …, n − 1. \begin{array}[]{clcclcl}\Omega_{3}&{\rm at}~~(i,i)&,&\Omega_{4}a_{n-1}^{n}&{\rm at}~~(i,n-1+i)&,&i=1,\ldots,n-2\\ &&{\rm and}&(n-1)\Omega_{3}&{\rm at}~~(n-2+j,j)&,&j=1,\ldots,n-1~.\end{array} |  |

Hence its determinant equals Ω ~ ​ a n − 1 n ⁡ ( n − 2) \tilde{\Omega}a_{n-1}^{n(n-2)}, Ω ~ ≠ 0 \tilde{\Omega}\neq 0. Part (5) is proved.

Part (6) follows from the previous parts, from Lemma 1 and from Theorem 4. Indeed, for k ≤ n − 2 k\leq n-2 one has

 | QHD ⁡ ( M k) = ( QHD ⁡ ( D ~ k) − 3 ​ Q ​ H ​ D ​ ( V k) − n ⁡ ( n − k − 1)) / 2 = ( n ​ ( n − 1) 2 + n 2 ​ ( n − k − 1) − 3 ​ n ​ ( n − 1) − n ⁡ ( n − k − 1)) / 2 = n 3 − 3 ​ n 2 + 2 ​ n − ( n 2 − n) ​ ( k + 1) / 2. \begin{array}[]{ccl}{\rm QHD}(M_{k})&=&({\rm QHD}(\tilde{D}_{k})-3{\rm QHD}(V_{k})-n(n-k-1))/2\\ &=&(n(n-1)^{2}+n^{2}(n-k-1)-3n(n-1)-n(n-k-1))/2\\ &=&n^{3}-3n^{2}+2n-(n^{2}-n)(k+1)/2~.\end{array} |  |

For k = n − 1 k=n-1 one obtains

 | QHD ⁡ ( M n − 1) = ( QHD ⁡ ( D ~ n − 1) − 3 ​ Q ​ H ​ D ​ ( V n − 1) − n) / 2 = ( n ​ ( n − 1) 2 − 3 ​ n ​ ( n − 2) − n) / 2 = n ​ ( n − 2) ​ ( n − 3) / 2. \begin{array}[]{cclcl}{\rm QHD}(M_{n-1})&=&({\rm QHD}(\tilde{D}_{n-1})-3{\rm QHD}(V_{n-1})-n)/2&&\\ &=&(n(n-1)^{2}-3n(n-2)-n)/2&=&n(n-2)(n-3)/2~.\end{array} |  |

Finally for k = n k=n one gets

 | QHD ⁡ ( M n) = ( QHD ⁡ ( D ~ n) − 3 ​ QHD ​ ( V n)) / 2 = ( n − 1) ​ ( n − 2) ​ ( n − 3) / 2. {\rm QHD}(M_{n})=({\rm QHD}(\tilde{D}_{n})-3{\rm QHD}(V_{n}))/2=(n-1)(n-2)(n-3)/2~. |  |

∎

###### Proof of Theorem 4.

At a point of the set { R = 0 } \{R=0\}, where P P has one double nonzero root and n − 2 n-2 simple roots, this set is locally the graph of a function analytic in the variables a k a^{k}, for any 1 ≤ k ≤ n 1\leq k\leq n; if the double root is at 0 0, then this property holds for k = n k=n and fails for 1 ≤ k ≤ n − 1 1\leq k\leq n-1; at a point of this set for which P P has a root of multiplicity ≥ 3 \geq 3 the set is not smooth (see Theorem 4 in [5]). It is not smooth also at points for which P P has m ≥ 2 m\geq 2 double roots and n − 2 ​ m n-2m simple ones; at such points the set { R = 0 } \{R=0\} is locally the transversal intersection of m m smooth hypersurfaces (see part (1) of Remarks 6 in [5]).

Hence a priori the polynomial D ~ k \tilde{D}_{k} is of the form ( a n) s k ​ M k α k ​ T k β k (a_{n})^{s_{k}}M_{k}^{\alpha_{k}}T_{k}^{\beta_{k}}, where s k ∈ ℕ ∪ 0 s_{k}\in\mathbb{N}\cup 0, α k, β k ∈ ℕ \alpha_{k},\beta_{k}\in\mathbb{N}, { M k = 0 } \{M_{k}=0\} (resp. { T k = 0 } \{T_{k}=0\}) is the projection of the set M ~ \tilde{M} (resp. of Σ \Sigma) in the space of the variables a k a^{k}. The equality s k = d ⁡ ( n, k) s_{k}=d(n,k) follows from Lemma 1.

Further we prove the theorem by induction on n n. For n = 4 n=4 its proof follows from Example 3. Suppose that for some a ∈ ℂ n + 1 a\in\mathbb{C}^{n+1} the polynomial P n + 1 P^{n+1} has a simple root h ∈ ℂ h\in\mathbb{C}. Set x ↦ x + h x\mapsto x+h. The new polynomial P n + 1 P^{n+1} has a simple root at 0 0 hence a n + 1 = 0 a_{n+1}=0. The discriminant R n + 1 R^{n+1} depends only on the differences between the roots of P n + 1 P^{n+1} hence it remains invariant under shifts of the variable x x. For a n + 1 = 0 a_{n+1}=0 one can apply Lemma 7. The lemma implies that for k ≤ n − 1 k\leq n-1 the discriminant Res ( R n + 1, ∂ R n + 1 / ∂ a k, a k) (R^{n+1},\partial R^{n+1}/\partial a_{k},a_{k}) is of the form a n t k ​ M k 2 ​ T k 3 a_{n}^{t_{k}}M_{k}^{2}T_{k}^{3}, t k ∈ ℕ t_{k}\in\mathbb{N}, i.e. one has α k = 2 \alpha_{k}=2 and β k = 3 \beta_{k}=3 for k ≤ n − 1 k\leq n-1, a n ≠ 0 a_{n}\neq 0 and a n − 1 ≠ 0 a_{n-1}\neq 0. The sets M ~ \tilde{M} and Σ \Sigma are irreducible and their intersections with each of the subspaces { a j = 0 } \{a_{j}=0\} are their proper subsets. Therefore the restriction a n ≠ 0 a_{n}\neq 0 and a n − 1 ≠ 0 a_{n-1}\neq 0 can be lifted and one concludes that α k = 2 \alpha_{k}=2 and β k = 3 \beta_{k}=3 for k ≤ n − 1 k\leq n-1. The number h ∈ ℂ h\in\mathbb{C} is arbitrary and for n > 4 n>4 the set of polynomials P n P^{n} without simple roots is a variety in the space of variables a a of codimension ≥ 3 \geq 3. Hence the above reasoning is the proof that for n + 1 n+1 the claim of the theorem is true if k ≤ n − 1 k\leq n-1.

To perform the induction also for k = n k=n and k = n + 1 k=n+1 we consider the discriminant of the family of polynomials P ∗ n + 1:= a 0 ​ x n + 1 + a 1 ​ x n + ⋯ + a n + 1 P_{*}^{n+1}:=a_{0}x^{n+1}+a_{1}x^{n}+\cdots+a_{n+1}. For its discriminant (denoted also by R n + 1 R^{n+1}) one has R n + 1 = ( a 0) 2 ​ n ​ ∏ 1 ≤ i < j ≤ n + 1 ( z i − z j) 2 R^{n+1}=(a_{0})^{2n}\prod_{1\leq i<j\leq n+1}(z_{i}-z_{j})^{2} ( z i z_{i} being the roots of P ∗ n + 1 P_{*}^{n+1}, see [8]). Consider the polynomial P r n + 1:= x n + 1 ​ P ∗ n + 1 ​ ( 1 / x) P^{n+1}_{r}:=x^{n+1}P_{*}^{n+1}(1/x) (the index r r stands for “reverted”). Its roots equal 1 / z i 1/z_{i}. Hence its discriminant R r n + 1 R^{n+1}_{r} equals

 | ( a n + 1) 2 ​ n ​ ∏ 1 ≤ i < j ≤ n + 1 ( 1 / z i − 1 / z j) 2 = ( a 0) 2 ​ n ​ ∏ 1 ≤ i < j ≤ n + 1 ( z i − z j) 2 = R n + 1. (a_{n+1})^{2n}\prod_{1\leq i<j\leq n+1}(1/z_{i}-1/z_{j})^{2}=(a_{0})^{2n}\prod_{1\leq i<j\leq n+1}(z_{i}-z_{j})^{2}=R^{n+1}~. |  |

For P r n + 1 P^{n+1}_{r} the coefficient a 0 a_{0} plays the same role as a n + 1 a_{n+1} plays for P n + 1 P^{n+1}. Denote by α ~ k \tilde{\alpha}_{k}, β ~ k \tilde{\beta}_{k} the quantities α k \alpha_{k}, β k \beta_{k} when defined for the polynomial P r n + 1 P^{n+1}_{r} instead of P n + 1 P^{n+1}. Hence one can make a shift x ↦ x + h ~ x\mapsto x+\tilde{h}, where h ~ \tilde{h} is a simple root of P r n + 1 P^{n+1}_{r}, and in the same way as above conclude that α ~ k = 2 \tilde{\alpha}_{k}=2 and β ~ k = 3 \tilde{\beta}_{k}=3 for k ≤ n − 1 k\leq n-1. This is tantamount to α k = 2 \alpha_{k}=2 and β k = 3 \beta_{k}=3 for k ≥ 2 k\geq 2. As n ≥ 4 n\geq 4, this means in particular that α n = α n + 1 = 2 \alpha_{n}=\alpha_{n+1}=2 and β n = β n + 1 = 3 \beta_{n}=\beta_{n+1}=3.

The polynomials D ~ k \tilde{D}_{k} and V k V_{k} are determinants of Sylvester matrices defined after polynomials with integer coefficients. Hence D ~ k \tilde{D}_{k} and V k V_{k} have also integer coefficients. Hence the polynomials M k M_{k} can also be chosen with integer coefficients which implies c k ∈ ℚ ∗ c_{k}\in\mathbb{Q}^{*}.

∎

## References

- [1] A. Albouy and Y. Fu, Some Remarks About Descartes’ Rule of Signs, Elemente der Mathematik 69 (2014), 186–194.
- [2] V.I. Arnold, S.M. Gusein-Zade and A.N. Varchenko, Singularities of differentiable maps. Volume 1. Classification of critical points, caustics and wave fronts. Translated from the Russian by Ian Porteous based on a previous translation by Mark Reynolds. Reprint of the 1985 edition. Modern Birkhäuser Classics. Birkhäuser/Springer, New York, 2012. xii+382 pp.
- [3] J. Forsgård, V.P. Kostov and B.Z. Shapiro, Could René Descartes have known this?, Experimental Mathematics vol. 24, issue 4 (2015) 438-448.
- [4] V.P. Kostov, Topics on hyperbolic polynomials in one variable. Panoramas et Synthèses 33 (2011), vi + 141 p. SMF.
- [5] V.P. Kostov, Some facts about discriminants, Comptes Rendus Acad. Bulg. Sci. (to appear).
- [6] I. Méguerditchian, Géométrie du Discriminant Réel et des Polynômes Hyperboliques, Thèse de Doctorat (soutenue le 24 janvier 1991 à Rennes).
- [7] T. Poston and I. Stewart, Catastrophe theory and its applications. With an appendix by D. R. Olsen, S. R. Carter and A. Rockwood. Reprint of the 1978 original. Dover Publications, Inc., Mineola, NY, 1996. xviii+491 pp.
- [8] Wikipedia. Discriminant.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
