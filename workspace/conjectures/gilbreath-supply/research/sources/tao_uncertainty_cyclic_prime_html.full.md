<!-- source: https://arxiv.org/html/math/0308286v6 | converted from HTML -->

An uncertainty principle for cyclic groups of prime order

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0308286v6 [math.CA] 22 Jul 2004

# An uncertainty principle for cyclic groups of prime order

Terence Tao Address: Department of Mathematics, UCLA, Los Angeles CA 90095-1555 Email address: [tao@@math.ucla.edu][3]

###### Abstract.

Let G G be a finite abelian group, and let f: G → C f:G\to{\hbox{\bf C}} be a complex function on G G. The uncertainty principle asserts that the support supp ​ ( f):= { x ∈ G: f ⁡ ( x) ≠ 0 } {\hbox{\roman supp}}(f):=\{x\in G:f(x)\neq 0\} is related to the support of the Fourier transform f ^: G → C \hat{f}:G\to{\hbox{\bf C}} by the formula

 | | supp ​ ( f) | ​ | supp ​ ( f ^) | ≥ | G | |{\hbox{\roman supp}}(f)||{\hbox{\roman supp}}(\hat{f})|\geq|G| |  |

where | X | |X| denotes the cardinality of X X. In this note we show that when G G is the cyclic group Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} of prime order p p, then we may improve this to

 | | supp ​ ( f) | + | supp ​ ( f ^) | ≥ p + 1 |{\hbox{\roman supp}}(f)|+|{\hbox{\roman supp}}(\hat{f})|\geq p+1 |  |

and show that this is absolutely sharp. As one consequence, we see that a sparse polynomial in Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} consisting of k + 1 k+1 monomials can have at most k k zeroes. Another consequence is a short proof of the well-known Cauchy-Davenport inequality.

###### 1991 Mathematics Subject Classification

42A99

## 1. Introduction

Let G G be a finite abelian additive group, and let e: G × G → S 1:= { z ∈ C: | z | = 1 } e:G\times G\to S^{1}:=\{z\in{\hbox{\bf C}}:|z|=1\} be any non-degenerate bi-character of G G, by which we mean a function e ⁡ ( x, ξ) e(x,\xi) taking values on the unit circle obeying the multiplicativity properties

 | e ⁡ ( x + x ′, ξ) = e ⁡ ( x, ξ) ​ e ​ ( x ′, ξ); e ⁡ ( x, ξ + ξ ′) = e ⁡ ( x, ξ) ​ e ​ ( x, ξ ′) e(x+x^{\prime},\xi)=e(x,\xi)e(x^{\prime},\xi);\quad e(x,\xi+\xi^{\prime})=e(x,\xi)e(x,\xi^{\prime}) |  |

and is non-degenerate in the sense that for every x ≠ 0 x\neq 0 there exists a ξ ∈ G \xi\in G such that e ⁡ ( x, ξ) ≠ 1 e(x,\xi)\neq 1, and conversely for every ξ ≠ 0 \xi\neq 0 there exists an x ∈ G x\in G such that e ⁡ ( x, ξ) ≠ 1 e(x,\xi)\neq 1. For instance, if G G is the cyclic group G:= Z / N ​ Z G:={\hbox{\bf Z}}/N{\hbox{\bf Z}}, we may take e ⁡ ( x, ξ):= e 2 ​ π ​ i ​ x ​ ξ / N e(x,\xi):=e^{2\pi ix\xi/N}. If f: G → C f:G\to{\hbox{\bf C}} is any complex-valued function on G G, we may then define the Fourier transform f ^: G → C \hat{f}:G\to{\hbox{\bf C}} by the formula

 | f ^ ​ ( ξ):= 1 | G | ​ ∑ x ∈ G f ⁡ ( x) ​ e ⁡ ( x, ξ) ¯, \hat{f}(\xi):=\frac{1}{|G|}\sum_{x\in G}f(x)\overline{e(x,\xi)}, |  |

where | G | |G| denotes the cardinality of G G. If we use supp ​ ( f):= { x ∈ G: f ⁡ ( x) ≠ 0 } {\hbox{\roman supp}}(f):=\{x\in G:f(x)\neq 0\} to denote the support of f f, we thus see from the triangle inequality, Cauchy-Schwarz and Plancherel that

 | sup ξ ∈ G | f ^ ​ ( ξ) | \displaystyle\sup_{\xi\in G}|\hat{f}(\xi)| | ≤ 1 | G | ​ ∑ x ∈ G | f ⁡ ( x) | \displaystyle\leq\frac{1}{|G|}\sum_{x\in G}|f(x)| |  |

 |  | ≤ | supp ​ ( f) | 1 / 2 | G | 1 / 2 ​ ( 1 | G | ​ ∑ x ∈ G | f ⁡ ( x) | 2) 1 / 2 \displaystyle\leq\frac{|{\hbox{\roman supp}}(f)|^{1/2}}{|G|^{1/2}}(\frac{1}{|G|}\sum_{x\in G}|f(x)|^{2})^{1/2} |  |

 |  | = | supp ​ ( f) | 1 / 2 | G | 1 / 2 ​ ( ∑ ξ ∈ G | f ^ ​ ( ξ) | 2) 1 / 2 \displaystyle=\frac{|{\hbox{\roman supp}}(f)|^{1/2}}{|G|^{1/2}}(\sum_{\xi\in G}|\hat{f}(\xi)|^{2})^{1/2} |  |

 |  | ≤ | supp ​ ( f) | 1 / 2 ​ | supp ​ ( f ^) | 1 / 2 | G | 1 / 2 ​ sup ξ ∈ G | f ^ ​ ( ξ) |. \displaystyle\leq\frac{|{\hbox{\roman supp}}(f)|^{1/2}|{\hbox{\roman supp}}(\hat{f})|^{1/2}}{|G|^{1/2}}\sup_{\xi\in G}|\hat{f}(\xi)|. |  |

Thus, if f f is non-zero, we thus obtain the well-known uncertainty principle [8], [16]

(1) |  | | supp ​ ( f) | ​ | supp ​ ( f ^) | ≥ | G |. |{\hbox{\roman supp}}(f)||{\hbox{\roman supp}}(\hat{f})|\geq|G|. |  |

This bound is of course sharp when f f is a Dirac mass, or when f ^ \hat{f} is a Dirac mass. More generally, if H H is any subgroup of G G, and we set f f to be the characteristic function χ H \chi_{H} of f f, it is easy to see that | supp ​ ( f) | = | H | |{\hbox{\roman supp}}(f)|=|H| and | supp ​ ( f ^) | = | G | / | H | |{\hbox{\roman supp}}(\hat{f})|=|G|/|H|, so again ( 1) is sharp. Indeed one can show that up to the symmetries of the Fourier transform (translation, modulation, and homogeneity) this is the only way in which ( 1) can be obeyed with equality (see e.g. [14]). For more background on the Fourier transform on finite abelian groups and the uncertainty principle we refer to [18].

Now consider the case where G G is a cyclic group of prime order, G = Z / p ​ Z G={\hbox{\bf Z}}/p{\hbox{\bf Z}}, with e ⁡ ( x, ξ):= e 2 ​ π ​ i ​ x ​ ξ / p e(x,\xi):=e^{2\pi ix\xi/p}. In this case G G has no subgroups other than the trivial ones { 0 } \{0\} and G G, and thus one expects to improve upon ( 1). Indeed we can get an absolutely sharp result as to the possible values of supp ​ ( f) {\hbox{\roman supp}}(f) and supp ​ ( f ^) {\hbox{\roman supp}}(\hat{f}):

###### Theorem 1.1.

Let p p be a prime number. If f: Z / p ​ Z → C f:{\hbox{\bf Z}}/p{\hbox{\bf Z}}\to{\hbox{\bf C}} is a non-zero function, then 1 1 1 This inequality was also discovered independently by András Biró [10] and Roy Meshulam (Vsevolod Lev, private communication). Given the number of times Lemma 1.3 appears to have been rediscovered in the literature it is in fact quite likely that this theorem has existed previously in some unpublished form.

 | | supp ​ ( f) | + | supp ​ ( f ^) | ≥ p + 1. |{\hbox{\roman supp}}(f)|+|{\hbox{\roman supp}}(\hat{f})|\geq p+1. |  |

Conversely, if A A and B B are two non-empty subsets of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} such that | A | + | B | ≥ p + 1 |A|+|B|\geq p+1, then there exists a function f f such that supp ​ ( f) = A {\hbox{\roman supp}}(f)=A and supp ​ ( f ^) = B {\hbox{\roman supp}}(\hat{f})=B.

The informal explanation of this principle is that the class of functions f f from Z / p ​ Z → C {\hbox{\bf Z}}/p{\hbox{\bf Z}}\to{\hbox{\bf C}} has exactly p p degrees of freedom. Requiring that supp ​ ( f) = A {\hbox{\roman supp}}(f)=A takes away p − | A | p-|A| of these degrees, while requiring that supp ​ ( f ^) = B {\hbox{\roman supp}}(\hat{f})=B takes away another p − | B | p-|B|. The uncertainty principle is then a statement that the Fourier basis (of exponentials) and the physical space basis (of Dirac deltas) are “totally skew” (or more precisely, that all the minors of the exponential basis matrix ( e 2 ​ π ​ i ​ j ​ k / p) 0 ≤ j, k < p (e^{2\pi ijk/p})_{0\leq j,k<p} are non-zero). The idea that the prime cyclic group Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} has this “maximally skew” structure (in some sense, it is as far as possible from containing subgroups) is consistent with some other recent work on the arithmetic structure of prime cyclic groups, see for instance [2], [3].

The proof of Theorem 1.1 requires a number of preliminary lemmas. We first need a lemma from the Galois theory of the cyclotomic integers.

###### Lemma 1.2.

Let p p be a prime, n n be a positive integer, and let P ⁡ ( z 1, …, z n) P(z_{1},\ldots,z_{n}) be a polynomial with integer co-efficients. Suppose that we have n n p t ​ h p^{th} roots of unity ω 1, …, ω n \omega_{1},\ldots,\omega_{n} (not necessarily distinct) such that P ⁡ ( ω 1, …, ω n) = 0 P(\omega_{1},\ldots,\omega_{n})=0. Then P ⁡ ( 1, …, 1) P(1,\ldots,1) is a multiple of p p.

Proof Write ω:= e 2 ​ π ​ i / p \omega:=e^{2\pi i/p}, then for every 1 ≤ j ≤ n 1\leq j\leq n we have ω j = ω k j \omega_{j}=\omega^{k_{j}} for some integers 0 ≤ k j < p 0\leq k_{j}<p. If we then define the single-variable polynomial Q ⁡ ( z) Q(z) by

 | Q ⁡ ( z):= P ⁡ ( z k 1, …, z k n) mod z p − 1, Q(z):=P(z^{k_{1}},\ldots,z^{k_{n}})\mod z^{p}-1, |  |

where R ⁡ ( z) mod z p − 1 R(z)\mod z^{p}-1 is the remainder when dividing R ⁡ ( z) R(z) by z p − 1 z^{p}-1 (or equivalently, taking the polynomial R ⁡ ( z) R(z) and replacing z q ​ p + r z^{qp+r} with z r z^{r} for all q ≥ 1 q\geq 1 and 0 ≤ r < p 0\leq r<p), then we have Q ⁡ ( ω) = 0 Q(\omega)=0 and Q ⁡ ( 1) = P ⁡ ( 1, …, 1) Q(1)=P(1,\ldots,1). But Q ⁡ ( z) Q(z) is a polynomial of degree at most p − 1 p-1 with integer coefficients, and thus must be an integer multiple of the minimal polynomial 1 + z + … + z p − 1 1+z+\ldots+z^{p-1} of ω \omega. The claim follows.

Using this lemma, we can show that all the minors of the Fourier matrix are non-zero.

###### Lemma 1.3.

Let p p be a prime and 1 ≤ n ≤ p 1\leq n\leq p. Let x 1, …, x n x_{1},\ldots,x_{n} be distinct elements of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}}, and let ξ 1, …, ξ n \xi_{1},\ldots,\xi_{n} also be distinct elements of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}}. Then the matrix ( e 2 ​ π ​ i ​ x j ​ ξ k / p) 1 ≤ j, k ≤ n (e^{2\pi ix_{j}\xi_{k}/p})_{1\leq j,k\leq n} has non-zero determinant.

This result was first proved by Chebotarëv in 1926 (see [17]), and with additional proofs given by Resetnyak [15], Dieudonné [7], Newman [13], Evans and Stark [9], and more recently Frenkel [10] and Goldstein, Guralnick, and Isaacs [11]. Recently, some more quantitative measure of the non-degeneracy of (randomly selected) minors was obtained in [4]. All proofs of Lemma 1.3 require a certain amount of algebraic information about the cyclotomic integers, but our proof requires relatively little in that regard (all we need is Lemma 1.2).

Proof Write ω j:= e 2 ​ π ​ i ​ x j / p \omega_{j}:=e^{2\pi ix_{j}/p}. Then each ω j \omega_{j} is a distinct root of unity, and our task is to show that

 | det ( ω j ξ k) 1 ≤ j, k ≤ n \det(\omega_{j}^{\xi_{k}})_{1\leq j,k\leq n} |  |

is non-zero. Motivated by the previous lemma, we define the polynomial D ⁡ ( z 1, …, z n) D(z_{1},\ldots,z_{n}) of n n variables by

 | D ⁡ ( z 1, …, z n):= det ( z j ξ k) 1 ≤ j, k ≤ n; D(z_{1},\ldots,z_{n}):=\det(z_{j}^{\xi_{k}})_{1\leq j,k\leq n}; |  |

here we identify the frequencies ξ k ∈ Z / p ​ Z \xi_{k}\in{\hbox{\bf Z}}/p{\hbox{\bf Z}} with elements of { 0, 1, …, p − 1 } \{0,1,\ldots,p-1\} in the obvious manner. This is clearly a polynomial with integer co-efficients. Unfortunately D ⁡ ( 1, …, 1) D(1,\ldots,1) degenerates to zero and so Lemma 1.2 does not directly tell us that D ⁡ ( ω 1, …, ω n) D(\omega_{1},\ldots,\omega_{n}) is non-zero. Indeed, D D clearly vanishes when z j = z j ′ z_{j}=z_{j^{\prime}} for any 1 ≤ j < j ′ ≤ n 1\leq j<j^{\prime}\leq n, and so we can factor

(2) |  | D ⁡ ( z 1, …, z n) = P ⁡ ( z 1, …, z n) ​ ∏ 1 ≤ j < j ′ ≤ n ( z j − z j ′) D(z_{1},\ldots,z_{n})=P(z_{1},\ldots,z_{n})\prod_{1\leq j<j^{\prime}\leq n}(z_{j}-z_{j^{\prime}}) |  |

for some other polynomial P P with integer coefficients. We will show that P ⁡ ( 1, …, 1) P(1,\ldots,1) is not a multiple of p p, which by Lemma 1.2 shows that P ⁡ ( ω 1, …, ω n) P(\omega_{1},\ldots,\omega_{n}) is non-zero, which proves the claim since the ω j \omega_{j} are all distinct.

To compute P ⁡ ( 1, …, 1) P(1,\ldots,1), we differentiate D D repeatedly. In particular, we consider the expression

(3) |  | ( z 1 ​ d d ​ z 1) 0 ​ ( z 2 ​ d d ​ z 2) 1 ​ … ​ ( z n ​ d d ​ z n) n − 1 ​ D ​ ( z 1, …, z n) | z 1 = … = z n = 1. (z_{1}\frac{d}{dz_{1}})^{0}(z_{2}\frac{d}{dz_{2}})^{1}\ldots(z_{n}\frac{d}{dz_{n}})^{n-1}D(z_{1},\ldots,z_{n})|_{z_{1}=\ldots=z_{n}=1}. |  |

Note that we are applying 0 + 1 + … + n − 1 = n ⁡ ( n − 1) 2 0+1+\ldots+n-1=\frac{n(n-1)}{2} differentiation operators, which is exactly the same number as the number of linear factors ( z j − z j ′) (z_{j}-z_{j^{\prime}}) in ( 2). By the Leibnitz rule, each differentiation operator z j ​ d d ​ z j z_{j}\frac{d}{dz_{j}} may eliminate one of these linear factors (and replace it with z j z_{j}), or it may differentiate some other term (e.g. it may differentiate P P). But the only terms from the Leibnitz expansion which do not vanish when z 1 = … = z n = 1 z_{1}=\ldots=z_{n}=1 are those in which every differentiation operator eliminates one of the linear factors (so in particular we never need to differentiate P P). The n − 1 n-1 copies of the differentiation operators z n ​ d d ​ z n z_{n}\frac{d}{dz_{n}} can only eliminate the n − 1 n-1 linear factors ( z j − z n) (z_{j}-z_{n}), and so every one of those linear factors must be eliminated by one of these differentiation operators, and there are ( n − 1)! (n-1)! ways in which this can occur. We then argue similarly with the n − 2 n-2 copies of z n − 1 ​ d d ​ z n − 1 z_{n-1}\frac{d}{dz_{n-1}}, which must eliminate the n − 2 n-2 linear factors ( z j − z n − 1) (z_{j}-z_{n-1}) (and there are ( n − 2)! (n-2)! ways of doing so). Continuing in this fashion we thus see that

 | ( 3) = ( n − 1)! ​ ( n − 2)! ​ … ​ 0! ​ P ​ ( 1, …, 1). \eqref{big-mess}=(n-1)!(n-2)!\ldots 0!P(1,\ldots,1). |  |

Since ( n − 1)! ​ ( n − 2)! ​ … ​ 0! (n-1)!(n-2)!\ldots 0! is not a multiple of p p, it thus suffices to show that the integer ( 3) is not a multiple of p p. But by the definition of D ⁡ ( z 1, …, z n) D(z_{1},\ldots,z_{n}) and the multilinearity of the determinant, and the trivial observation that ( z j ​ d d ​ z j) ​ z j ξ = ξ ​ z j ξ (z_{j}\frac{d}{dz_{j}})z_{j}^{\xi}=\xi z_{j}^{\xi}, we see that

 | ( 3) = det ( ξ k j − 1) 1 ≤ j, k ≤ n. \eqref{big-mess}=\det(\xi_{k}^{j-1})_{1\leq j,k\leq n}. |  |

This is a Vandermonde determinant which (as is well-known) is equal to

 | ± ∏ 1 ≤ k < k ′ ≤ n ( ξ k − ξ k ′). \pm\prod_{1\leq k<k^{\prime}\leq n}(\xi_{k}-\xi_{k^{\prime}}). |  |

But since the ξ k \xi_{k} are all distinct modulo p p, this is not a multiple of p p, and the claim follows.

From the above Lemma we immediately obtain

###### Corollary 1.4.

If p p is a prime, and A, A ~ A,\tilde{A} are non-empty subsets of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} such that | A | = | A ~ | |A|=|\tilde{A}|, then the linear transformation T: l 2 ​ ( A) → l 2 ​ ( A ~) T:l^{2}(A)\to l^{2}(\tilde{A}) defined by T ​ f = f ^ | A ~ Tf=\hat{f}|_{\tilde{A}} (i.e. we restrict the Fourier transform of f f to A ~ \tilde{A}) is invertible. Here we use l 2 ​ ( A) l^{2}(A) to denote those functions f: G → C f:G\to{\hbox{\bf C}} which are equal to zero outside of A A.

Indeed, the coefficient matrix of T T is of the form considered in Lemma 1.3. From this Corollary we can now easily prove the uncertainty principle.

Proof [of Theorem 1.1.] Suppose for contradiction that we had a non-zero function f f such that | supp ​ ( f) | + | supp ​ ( f ^) | ≤ p |{\hbox{\roman supp}}(f)|+|{\hbox{\roman supp}}(\hat{f})|\leq p. Then if we write A:= supp ​ ( f) A:={\hbox{\roman supp}}(f), then we can find a set A ~ \tilde{A} in Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} which is disjoint from supp ​ ( f ^) {\hbox{\roman supp}}(\hat{f}) and has cardinality equal to | A | |A|. But this contradicts Corollary 1.4 since T ​ f = 0 Tf=0 but f ≠ 0 f\neq 0.

Now we prove the converse. It will suffice to prove the claim when | A | + | B | = p + 1 |A|+|B|=p+1, since the claim for | A | + | B | > p + 1 |A|+|B|>p+1 then follows by applying the claim to subsets A ′ A^{\prime}, B ′ B^{\prime} of A A, B B respectively for which | A ′ | + | B ′ | = p + 1 |A^{\prime}|+|B^{\prime}|=p+1, and then taking generic linear combinations as A ′ A^{\prime}, B ′ B^{\prime} vary.

We can then choose an A ~ \tilde{A} in Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} of cardinality | A ~ | = | A | |\tilde{A}|=|A| such that A ~ \tilde{A} intersects B B in only one point, say A ~ ∩ B = { ξ } \tilde{A}\cap B=\{\xi\}. But by Corollary 1.4 the map T T is invertible, and in particular we can find a non-zero f ∈ l 2 ​ ( A) f\in l^{2}(A) such that f ^ \hat{f} vanishes on A ~ \ { ξ } \tilde{A}\backslash\{\xi\} and is non-zero on ξ \xi. Such a function must then be non-zero on all of A A and non-zero on all of B B since this would violate the first part of the uncertainty principle proven in the previous paragraph. Thus supp ​ ( f) = A {\hbox{\roman supp}}(f)=A and supp ​ ( f ^) = B {\hbox{\roman supp}}(\hat{f})=B as desired.

Observe that an immediate consequence of Theorem 1.1 is that any sparse polynomial ∑ j = 0 k c j ​ z n j \sum_{j=0}^{k}c_{j}z^{n_{j}} with k + 1 k+1 non-zero coefficients and 0 ≤ n 0 < … < n k < p 0\leq n_{0}<\ldots<n_{k}<p, when restricted to the p t ​ h p^{th} roots of unity { z: z p = 1 } \{z:z^{p}=1\}, can have at most k k zeroes. Indeed, such a polynomial is essentially the Fourier transform in Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} of a function whose support has cardinality k + 1 k+1, and so the support of the polynomial must contain at least p − k p-k p t ​ h p^{th} roots of unity by Theorem 1.1, and the claim follows.

Another immediate consequence is the Cauchy-Davenport inequality [5], [6], which asserts that for any two finite non-empty subsets A A and B B of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}}, the sumset A + B:= { a + b: a ∈ A, b ∈ B } A+B:=\{a+b:a\in A,b\in B\} obeys the bounds

 | | A + B | ≥ min ⁡ ( | A | + | B | − 1, p). |A+B|\geq\min(|A|+|B|-1,p). |  |

Proof 2 2 2 We thank Robin Chapman for this proof, which is slightly shorter than the original proof of the author. Fix A A, B B. Since A A and B B are non-empty, we may find two subsets X X and Y Y of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}} such that | X | = p + 1 − | A | |X|=p+1-|A|, | Y | = p + 1 − | B | |Y|=p+1-|B|, and | X ∩ Y | = max ⁡ ( | X | + | Y | − p, 1) |X\cap Y|=\max(|X|+|Y|-p,1). By Theorem 1.1 we may find a function f f such that supp ​ ( f) = A {\hbox{\roman supp}}(f)=A and supp ​ ( f ^) = X {\hbox{\roman supp}}(\hat{f})=X, and a function g g such that supp ​ ( g) = B {\hbox{\roman supp}}(g)=B and supp ​ ( g ^) = Y {\hbox{\roman supp}}(\hat{g})=Y. Then f ∗ g f*g has support contained in A + B A+B and has Fourier support equal to X ∩ Y X\cap Y (in particular, f ∗ g f*g is non-zero), and hence by Theorem 1.1 again we have | A + B | + | X ∩ Y | ≥ p + 1 |A+B|+|X\cap Y|\geq p+1, which gives | A + B | ≥ max ⁡ ( | A | + | B | − 1, p) |A+B|\geq\max(|A|+|B|-1,p) as desired.

It is interesting to compare this proof with the polynomial method proof of [1], which uses the basis of polynomials rather than the basis of exponentials but is otherwise rather similar in spirit.

Based on this result for groups of prime order, it seems natural to conjecture that one can improve ( 1) substantially for all finite abelian groups G G, provided that the cardinality of | supp ​ ( f) | |{\hbox{\roman supp}}(f)| and | supp ​ ( f ^) | |{\hbox{\roman supp}}(\hat{f})| stays well away from any factor of | G | |G|. For instance, Roy Meschulam (private communication) has used Theorem 1.1 and an iteration argument to show that p j ​ | supp ​ ( f) | + p n − j − 1 ​ | supp ​ ( f ^) | ≥ p n + p n − 1 p^{j}|{\hbox{\roman supp}}(f)|+p^{n-j-1}|{\hbox{\roman supp}}(\hat{f})|\geq p^{n}+p^{n-1} for all non-zero functions f f supported on ( Z / p ​ Z) n ({\hbox{\bf Z}}/p{\hbox{\bf Z}})^{n} and all 0 ≤ j ≤ n − 1 0\leq j\leq n-1. To put this another way, the point ( | supp ​ ( f) |, | supp ​ ( f ^) |) (|{\hbox{\roman supp}}(f)|,|{\hbox{\roman supp}}(\hat{f})|) in Z × Z {\hbox{\bf Z}}\times{\hbox{\bf Z}} lies on or above the convex hull of the points ( p j, p n − j) (p^{j},p^{n-j}) for 0 ≤ j ≤ n 0\leq j\leq n, which correspond to the cases where f f is the characteristic function of a subgroup of ( Z / p ​ Z) n ({\hbox{\bf Z}}/p{\hbox{\bf Z}})^{n}. This has immediate application to the number of zeroes of a sparse polynomial of several variables in Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}}, which may be of interest for cryptographic applications.

## 2. Acknowledgements

This work was conducted at Australian National University. The author is a Clay Prize Fellow and is supported by a grant from the Packard Foundation. The author is also indebted to Robin Chapman for pointing out the provenance of Lemma 1.3 and simplifying the proof of the Cauchy-Davenport inequality, to Michael Cowling and Gerd Mockenhaupt for pointing out the provenance of ( 1), and to Roy Meshulam to pointing out extensions of Theorem 1.1 to higher powers of Z / p ​ Z {\hbox{\bf Z}}/p{\hbox{\bf Z}}. We also thank Gergely Harcos, Melvyn Nathanson and Vselvolod Lev for some corrections and comments.

## References

- [1] N. Alon, M. Nathanson, I. Ruzsa, The polynomial method and restricted sums of congruence classes, J. Number Theory 56 (1996), 404–417.
- [2] J. Bourgain, N. Katz, T. Tao, A sum-product estimate in finite fields, and applications, to appear, GAFA. math.CO/0301343
- [3] J. Bourgain, S. Konyagin, Estimates for the number of sums and products and for exponential sums over subgroups in fields of prime order, C. R. Acad. Sci. Paris, Ser. I 337 (2003), 75–80.
- [4] E. Candes, J. Romberg, T. Tao, Robust uncertainty principles: Exact signal reconstruction from highly incomplete frequency information, preprint.
- [5] A.L. Cauchy, Recherches sur les nombres, J. École Polytech. 9 (1813), 99-116.
- [6] H. Davenport, On the addition of residue classes, J. London Math. Soc. 10 (1935), 30–32.
- [7] J. Dieudonné, Une propriété des racines de l’unité, Collection of articles dedicated to Alberto González Domínguez on his sixty-fifth birthday. Rev. Un. Mat. Argentina 25 (1970/71), 1–3.
- [8] D.L. Donoho, P.B. Stark, Uncertainty principles and signal recovery, SIAM J. Appl. Math. 49 (1989), 906–931.
- [9] R.J. Evans, I.M. Stark, Generalized Vandermonde determinants and roots of unity of prime order, Proc. Amer. Math. Soc. 58 (1977), 51–54.
- [10] P. Frenkel, Simple proof of Chebotarev’s theorem on roots of unity, preprint. math.AC/0312398
- [11] D. Goldstein, R. Guralnick, I. Isaacs, Inequalities for finite group permutation modules, preprint. math.GR/0310169
- [12] R. Meshulam, An uncertainty inequality for finite abelian groups, preprint. math.CO/0312407
- [13] M. Newman, On a theorem of Cebotarev, Linear and Multilinear Algebra 3 (1975/76), no. 4, 259–262.
- [14] T. Przebinda, Three uncertainty principles for a locally compact abelian group, preprint.
- [15] Yu. G. Rešetnyak, Yu., New proof of a theorem of N. G. Cebotarev (Russian), Uspehi Mat. Nauk (N.S.) 10 (1955), no. 3(65), 155–157.
- [16] K.T. Smith, The uncertainty principle on groups, SIAM J. APpl. Math. 50 (1990), 876–882.
- [17] P. Stevenhagen, H.W. Lenstra Jr., Chebotarëv and his density theorem, Math. Intelligencer 18 (1996), no. 2, 26–37.
- [18] A. Terras, Fourier analysis on finite groups and applications. London Mathematical Society Student Texts, 43. Cambridge University Press, Cambridge, 1999.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:tao@@math.ucla.edu
