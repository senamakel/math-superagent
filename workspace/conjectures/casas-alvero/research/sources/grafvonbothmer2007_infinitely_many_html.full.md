<!-- source: https://arxiv.org/html/math/0605090v2 | converted from HTML -->

The Casas-Alvero conjecture for infinitely many degrees

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0605090v2 [math.AC] 25 Jun 2007

# The Casas-Alvero conjecture for infinitely many degrees Thanks: 1 Supported by the Schwerpunktprogramm “Global Methods in Complex Geometry” of the Deutsche Forschungs Gemeinschaft. Thanks: 2 Supported by the Radon Institute for Computational and Applied Mathematics (RICAM, Linz), Austrian Academy of Sciences. Thanks: 3 Supported by the Austrian Science Fund (FWF) in the frame of the projects “Solving Algebraic Equations”, P18992-N18, and SFB 013, subproject 03. Thanks: 4 Supported by the Special Semester on Gröbner Bases and Related Topics 2006, organised by RICAM Linz (in cooperation with RISC Hagenberg).

Hans-Christian Graf von Bothmer 1 Address: Institut für Mathematik
Universität Hannover
Welfengarten 1
30167 Hannnover, Germany URL: [www-ifm.math.uni-hannover.de/~bothmer][3] Email address: [bothmer m @ ath.uni-hannover.de][4], Oliver Labs 2 Address: Mathematik und Informatik
Gebäude E2.4
Universität des Saarlandes
66123 Saarbrücken, Germany URL: [www.OliverLabs.net][5] Email address: [Labs m @ ath.uni-sb.de, mail O @ liverLabs.net][6], Josef Schicho 3 Address: Radon Institut for Computational and Applied Mathematics
Austrian Academy of Sciences
4040 Linz, Austria URL: [www.ricam.oeaw.ac.at/research/symcomp][7] Email address: [josef.schicho o @ eaw.ac.at][8] and Christiaan van de Woestijne 4 Address: Institut für Mathematik B
Technische Universität Graz
8010 Graz, Austria URL: [www.opt.math.tugraz.at/~cvdwoest][9] Email address: [c.vandewoestijne t @ ugraz.at][10]

###### Abstract.

Over a field of characteristic zero, it is clear that a polynomial of the form ( X − α) d (X-\alpha)^{d} has a non-trivial common factor with each of its d − 1 d-1 first derivatives. The converse has been conjectured by Casas-Alvero. Up to now there have only been some computational verifications for small degrees d d. In this paper the conjecture is proved in the case where the degree of the polynomial is a power of a prime number, or twice such a power.

Moreover, for each positive characteristic p p, we give an example of a monic polynomial of degree d > p d>p which is not a d d th power but which has a common factor with each of its first d − 1 d-1 derivatives. This shows that the assumption of characteristic zero is essential for the converse statement to hold.

## 1. Introduction

Let 𝕂 {\mathbb{K}} be a field and let 𝕂 ⁡ [X] {\mathbb{K}}[X] be the ring of univariate polynomials over 𝕂 {\mathbb{K}}. For any polynomial P ∈ 𝕂 ⁡ [X] P\in{\mathbb{K}}[X] and for any nonnegative integer i i, we denote by P ( i) P^{(i)} the i i th derivative of P P, and by P i P_{i} the i i th Hasse derivative, which is P ( i) P^{(i)} divided by i! i\,! in characteristic zero.

This paper is concerned with the following question posed by E. Casas-Alvero in characteristic zero:

###### Conjecture (Casas-Alvero).

Let P P be a monic univariate polynomial of degree d d over a field 𝕂 {\mathbb{K}}. Then gcd ⁡ ( P, P i) \gcd(P,P_{i}) is nontrivial for i = 1, …, d − 1 i=1,\ldots,d-1 if and only if P = ( X − α) d P=(X-\alpha)^{d} for some α ∈ 𝕂 \alpha\in{\mathbb{K}}.

Note that the implication from right to left is trivial. The truth of the other implication depends on the characteristic of the base field 𝕂 {\mathbb{K}}. For d ≤ 7 d\leq 7 and assuming that char ⁡ 𝕂 = 0 \kar{\mathbb{K}}=0, the conjecture was proved in [DG05], using Gröbner basis computations. Since then the authors of [DG05] have settled the case of d = 8 d=8 as well (personal communication). It seems that no other cases are known.

In this paper, we prove the conjecture in characteristic 0 0 for infinitely many degrees d d. More precisely, in Section 2 we show

###### Theorem.

Let d d be of the form p k p^{k} or 2 ​ p k 2p^{k} for some prime number p p. Then the Casas-Alvero Conjecture holds in characteristic 0 0 for polynomials of degree d d.

Since we could not find a reference for the fact that the Casas-Alvero Conjecture does not always extend to characteristic p p, we include explicit counter-examples of degree d > p d>p for each p p in Section 3.

This work grew out of discussions in a meeting of the authors at RICAM in the frame of the special semester on Gröbner bases. The connection with Gröbner bases is made clear in Section 4, where we discuss the computational aspects of the problem.

### Notations and definitions.

We will write

 | P = a 0 ​ X d + a 1 ​ X d − 1 + … + a d P=a_{0}X^{d}+a_{1}X^{d-1}+\ldots+a_{d} |  |

throughout the paper. With this notation, we have

 | P i = ( d i) ​ a 0 ​ X d − i + … + ( i + 1 i) ​ a d − i + 1 ​ X + ( i i) ​ a d − i P_{i}=\binom{d}{i}a_{0}X^{d-i}+\ldots+\binom{i+1}{i}a_{d-i+1}X+\binom{i}{i}a_{d-i} |  |

for the i i th Hasse derivative of P P. In characteristic 0 0 one has P i = P ( i) / i! P_{i}=P^{(i)}/i\,!.

As ( i i) = 1 \binom{i}{i}=1, we see that none of the Hasse derivatives vanishes identically for all polynomials, regardless of the characteristic of the base field, whereas in characteristic p p, the n n th usual derivative of any polynomial is identically zero for all n ≥ p n\geq p. Thus, the conditions of the Conjecture are strengthened in positive characteristic by using the Hasse derivatives instead of the usual ones, whereas in characteristic 0 0 there is no difference.

## 2. Mixing characteristics, or There and Back Again

We now establish some results which will finally lead to a proof of our Theorem. Although the conjecture in general does not hold in positive characteristic, it turns out that, for degrees d d and a prime p p as in the Theorem, it is true in characteristic p p, and this fact is used in the proof.

First, we note that the condition gcd ⁡ ( P, P i) ≠ 1 \gcd(P,P_{i})\neq 1 is equivalent to the *resultant*Res X ⁡ ( P, P i) \Res_{X}(P,P_{i}) being zero (when a 0 ≠ 0 a_{0}\neq 0). Let us consider the “generic” polynomial

 | P = a 0 ​ X d + … + a d P=a_{0}X^{d}+\ldots+a_{d} |  |

as an element of the polynomial ring

 | ℤ ⁡ [a 0, …, a d] ​ [X]; {\mathbb{Z}}[a_{0},\ldots,a_{d}][X]; |  |

and let us assume that gcd ⁡ ( P, P i) ≠ 1 \gcd(P,P_{i})\neq 1 for 1 ≤ i ≤ d − 1 1\leq i\leq d-1. It follows that the vector of coefficients ( a 0, …, a d) (a_{0},\ldots,a_{d}) belongs to an algebraic variety, namely the set of common zeros of the equations { Res X ⁡ ( P, P i) ∣ 1 ≤ i ≤ d − 1 } \{\Res_{X}(P,P_{i})\mid 1\leq i\leq d-1\}. Therefore, we will study the set of points with coordinates in 𝕂 {\mathbb{K}} on this variety, for any field 𝕂 {\mathbb{K}}.

Before this, however, we apply some simplifications: it is enough to consider the conjecture for *monic*polynomials only, so we assume a 0 = 1 a_{0}=1; and, because we assume that P P has a common factor with its ( d − 1) (d-1) st derivative, which is linear, we know that P P has a zero in the base field. If we translate this zero to 0 0, we have a d = 0 a_{d}=0, and moreover, the property of P P of having a common factor with its derivatives is preserved under this translation.

The defining property is also invariant under scaling of the variable X X; from this, it follows that the equation Res X ⁡ ( P, P i) \Res_{X}(P,P_{i}) is *homogeneous*of weighted degree d ⁡ ( d − i) d(d-i), if we give weight j j to the variable a j a_{j}, for 1 ≤ j ≤ d − 1 1\leq j\leq d-1. (It is consistent to give a 0 a_{0} weight 0 0 and a d a_{d} weight d d, as well.)

Putting this all together, the object of interest is the weighted projective scheme

(1) |  | X d ⊆ ℙ ℤ ​ ( 1, 2, …, d − 1) X_{d}\subseteq{\mathbb{P}}_{{\mathbb{Z}}}(1,2,\ldots,d-1) |  |

over ℤ {\mathbb{Z}}, defined by the homogeneous ideal

 | I d = ⟨ Res X ( P, P i) ∣ i = 1, …, d − 1 ⟩ ⊆ R d = ℤ [a 1, …, a d − 1], I_{d}=\left<\Res_{X}(P,P_{i})\mid i=1,\ldots,d-1\right>\subseteq R_{d}={\mathbb{Z}}[a_{1},\ldots,a_{d-1}], |  |

where a j a_{j} has weight j j for 1 ≤ j ≤ d − 1 1\leq j\leq d-1. We will consider the set X d ​ ( 𝕂) X_{d}({\mathbb{K}}) of 𝕂 {\mathbb{K}} -rational points on X d X_{d} for any field 𝕂 {\mathbb{K}}.

Under the simplifications given above, if P P is a power of a linear polynomial, then we must have P = X d P=X^{d} and a 1 = … = a d − 1 = 0 a_{1}=\ldots=a_{d-1}=0. But this trivial rational point ( 0, …, 0) (0,\ldots,0) is excluded from X d X_{d}, as we consider X d X_{d} to be projective. Therefore, we have:

###### Proposition 2.1.

The Casas-Alvero Conjecture holds for polynomials of degree d d over a field 𝕂 {\mathbb{K}} if and only if X d ​ ( 𝕂) X_{d}({\mathbb{K}}) is empty.

The following result permits us to draw conclusions about the situation in characteristic 0 0 from results in characteristic p p. For any field 𝕂 {\mathbb{K}}, we write 𝕂 ¯ \overline{{\mathbb{K}}} for an algebraic closure of 𝕂 {\mathbb{K}}; also, we consider the *base extension*X d × Spec ⁡ 𝕂 X_{d}\times\Spec{\mathbb{K}} of X d X_{d} to a projective scheme over Spec ⁡ 𝕂 \Spec{\mathbb{K}}. The scheme X d × Spec ⁡ 𝕂 X_{d}\times\Spec{\mathbb{K}} is empty if and only if X d X_{d} has no points over 𝕂 ¯ \overline{{\mathbb{K}}}.

###### Proposition 2.2.

Let d ≥ 1 d\geq 1 be an integer. If X d ​ ( 𝔽 ¯ ℓ) X_{d}(\overline{{\mathbb{F}}}_{\ell}) is empty for some prime ℓ \ell, then the Casas-Alvero Conjecture holds, for degree d d, in characteristic 0 0 and in characteristic p p for all but finitely many primes p p.

###### Proof.

As X d X_{d} is weighted projective over ℤ {\mathbb{Z}}, the structure morphism

 | ϕ d: X d → Spec ⁡ ( ℤ) \phi_{d}:X_{d}\rightarrow\Spec({\mathbb{Z}}) |  |

is proper [Har77, Theorem II.4.9]. In particular, the image ϕ d ​ ( X d) \phi_{d}(X_{d}) is closed. The complement U U of ϕ d ​ ( X d) \phi_{d}(X_{d}) is exactly the set of points in Spec ⁡ ( ℤ) \Spec({\mathbb{Z}}) where the fiber under ϕ d \phi_{d} is empty. By assumption, U U is non-empty, because it contains the prime ℓ \ell. It follows that U U is dense in Spec ⁡ ( ℤ) \Spec({\mathbb{Z}}), and hence contains the generic point, as well as all but finitely many primes. But the fiber of the generic point is X d × Spec ⁡ ℚ X_{d}\times\Spec{\mathbb{Q}}, while the fiber of a prime p p is X d × Spec ⁡ 𝔽 p X_{d}\times\Spec{\mathbb{F}}_{p}, so that all these fibers are empty by definition of U U.

By base extension, one sees easily that if X d × Spec ⁡ ℚ X_{d}\times\Spec{\mathbb{Q}} is empty, then so is X d ​ ( 𝕂) X_{d}({\mathbb{K}}) for any field 𝕂 {\mathbb{K}} of characteristic 0 0, and the analogon holds for characteristic p p. ∎

We now come to some concrete statements about the problem.

###### Proposition 2.3.

The Casas-Alvero Conjecture holds over any field in degrees 1 1 and 2 2.

###### Proof.

The linear case is trivial. Suppose P = X 2 + a 1 ​ X P=X^{2}+a_{1}X shares a factor with its derivative 2 ​ X + a 1 2X+a_{1}; then it follows easily that a 1 = 0 a_{1}=0, whether 2 2 is equal to 0 0 or not. ∎

We use a number-theoretical lemma. For an integer a a and a prime number p p, let v p ​ ( a) v_{p}(a) be the number of factors p p in a a; we have v p ​ ( 0) = ∞ v_{p}(0)=\infty.

###### Lemma 2.4.

Let d d be a positive integer, let p p be a prime number dividing d d, and let i i be an integer with 0 ≤ i ≤ d 0\leq i\leq d. If v p ​ ( i) < v p ​ ( d) v_{p}(i)<v_{p}(d), then the binomial coefficient ( d i) \binom{d}{i} is 0 0 modulo p p.

###### Proof.

It is an old result of Kummer [Kum52, p. 116], which is easily proved, that the highest power of p p that divides ( d i) \binom{d}{i} is equal to the number of ‘carries’ that occur when i i and d − i d-i are added in p p -adic notation. If v p ​ ( d) = e v_{p}(d)=e, then the p p -adic expansion of d d ends in e e zeros, whereas by our assumption, the expansions of i i and d − i d-i end in less than e e zeros. Therefore, if we add them, we must incur at least one carry, and the binomial coefficient will be divisible by p p. ∎

###### Proposition 2.5.

Let d ≥ 1 d\geq 1 be an integer. If d d is a power of some prime number p p, then X d ​ ( 𝔽 ¯ p) X_{d}(\overline{{\mathbb{F}}}_{p}) is empty.

###### Proof.

Assume that P ∈ 𝔽 ¯ p ​ [x] = x d + … + a d − 1 ​ x P\in\overline{{\mathbb{F}}}_{p}[x]=x^{d}+\ldots+a_{d-1}x is a polynomial having a common factor with all its Hasse derivatives up to order d − 1 d-1. Note that by the Lemma, ( d i) = 0 \binom{d}{i}=0 in 𝔽 p {\mathbb{F}}_{p}, for i = 1, …, d − 1 i=1,\ldots,d-1. In particular ( d d − 1) = 0 \binom{d}{d-1}=0, hence P d − 1 = a 1 P_{d-1}=a_{1}. The existence of a common factor with P P implies that a 1 = 0 a_{1}=0. But then P d − 2 = a 2 P_{d-2}=a_{2}, hence a 2 = 0 a_{2}=0, and so on. Hence a 1 = … = a d − 1 = 0 a_{1}=\ldots=a_{d-1}=0, and because the origin is not contained in the weighted projective space, it follows X d ​ ( 𝔽 ¯ p) X_{d}(\overline{{\mathbb{F}}}_{p}) is empty. ∎

The argument of the Proposition can be generalised as follows.

###### Proposition 2.6.

Let d ≥ 1 d\geq 1 and k ≥ 0 k\geq 0 be integers. If d = n ​ p k d=np^{k} for some prime p p, and if X n ​ ( 𝔽 ¯ p) X_{n}(\overline{{\mathbb{F}}}_{p}) is empty, then X d ​ ( 𝔽 ¯ p) X_{d}(\overline{{\mathbb{F}}}_{p}) is empty.

###### Proof.

The proof of the previous Proposition shows that a 1 = … = a p k − 1 = 0 a_{1}=\ldots=a_{p^{k}-1}=0. Now we have P d − p k = ( d d − p k) ​ X p k + a p k P_{d-p^{k}}=\binom{d}{d-p^{k}}X^{p^{k}}+a_{p^{k}}, where this time, the leading coefficient does not necessarily vanish in 𝔽 p {\mathbb{F}}_{p}. Continuing, we see that again in P d − p k − 1 P_{d-p^{k}-1}, the leading coefficient vanishes, as well as the coefficient of a p k a_{p^{k}}, and we obtain a p k + 1 = 0 a_{p^{k}+1}=0. This process eventually shows that a i = 0 a_{i}=0 unless p k | i p^{k}\mid i. We obtain

 | P = X d + a p k ​ X d − p k + … + a d − p k ​ X p k, P=X^{d}+a_{p^{k}}X^{d-p^{k}}+\ldots+a_{d-p^{k}}X^{p^{k}}, |  |

which in characteristic p p is equal to Q p k Q^{p^{k}} for some polynomial Q ∈ 𝔽 ¯ p ​ [X] Q\in\overline{{\mathbb{F}}}_{p}[X] of degree n n, because the field 𝔽 ¯ p \overline{{\mathbb{F}}}_{p} is perfect. This polynomial Q Q again must have a common factor with all its Hasse derivatives up to order n − 1 n-1, which is impossible if no such polynomials (except the trivial one X n X^{n}) exist in degree n n. ∎

We can now prove the main result of this paper.

###### Theorem.

Let d d be of the form p k p^{k} or 2 ​ p k 2p^{k} for some prime number p p. Then the Casas-Alvero Conjecture holds in characteristic 0 0 for polynomials of degree d d.

###### Proof.

If d d is a prime power p k p^{k}, then by Proposition 2.5, we see that X d ​ ( 𝔽 ¯ p) X_{d}(\overline{{\mathbb{F}}}_{p}) is empty. If d = 2 ​ p k d=2p^{k}, then we first invoke Proposition 2.3 to show that no nontrivial quadratic examples exist in characteristic p p, and then use Proposition 2.6 to prove that X d ​ ( 𝔽 ¯ p) X_{d}(\overline{{\mathbb{F}}}_{p}) is empty in this case as well.

We can now finish the proof by using Proposition 2.2, which allows us to conclude that X d ​ ( 𝕂) X_{d}({\mathbb{K}}) is also empty for any field 𝕂 {\mathbb{K}} of characteristic 0 0. ∎

## 3. Counter-Examples in Positive Characteristic

For each prime field 𝔽 p {\mathbb{F}}_{p}, we construct a monic polynomial P P of degree d > p d>p that violates the Casas-Alvero Conjecture.

###### Proposition 3.1.

Let p p be a prime number, let P = X p + 1 − X p ∈ 𝔽 p ​ [X] P=X^{p+1}-X^{p}\in{\mathbb{F}}_{p}[X], and let d = deg ⁡ P = p + 1 d=\deg P=p+1. Then P P is not a d d th power, but it has a non-trivial common factor with its Hasse derivatives P i P_{i}, i = 1, 2, …, d − 1 i=1,2,\ldots,d-1.

###### Proof.

We have

 | P = X p + 1 − X p = X p ​ ( X − 1) ∈ 𝔽 p ​ [X]. P=X^{p+1}-X^{p}=X^{p}(X-1)\in{\mathbb{F}}_{p}[X]. |  |

Thus P P is not a d d th power, and it has a common factor X X with P i P_{i} for i = 1, 2, …, d − 2 i=1,2,\ldots,d~-~2. Moreover,

 | P d − 1 = d ​ X − 1 ≡ X − 1 mod p, P_{d-1}=dX-1\equiv X-1\mod p, |  |

and X − 1 X-1 divides P P. ∎

###### Remark 3.2.

If we fix d d, and assume that the Casas-Alvero Conjecture is true for degree d d in characteristic 0 0, then it follows from Proposition 2.2 that the primes p p for which counter-examples to the Casas-Alvero Conjecture exist over 𝔽 p {\mathbb{F}}_{p} are bounded. For example, for d = 3 d=3 the Conjecture is true for a field of any characteristic, except 2 2. By Proposition 2.6, this implies that the Conjecture holds in characteristic 0 0 for all degrees under 30 30, except possibly 12 12, 20 20, 24 24, and 28 28.

However, the bound on the bad primes for a given degree d d may be quite large. For example, considering all quadrinomials of the form X 6 + a ​ X 4 + X 3 + b ​ X 2 X^{6}+aX^{4}+X^{3}+bX^{2} that possibly violate the conjecture, we find the counter-example

 | P = X 6 + 3144481702696843 ​ X 4 + X 3 + 2707944513497181 ​ X 2 P=X^{6}+3144481702696843X^{4}+X^{3}+2707944513497181X^{2} |  |

in characteristic 7390044713023799 7390044713023799, even though the conjecture holds for d = 6 d=6 over ℚ {\mathbb{Q}}.

## 4. Computational aspects

As was already said in the Introduction, the Casas-Alvero Conjecture may in principle be verified computationally for any degree d d. One way to do this is to let a computer algebra package compute the polynomials Res X ⁡ ( P, P i) \Res_{X}(P,P_{i}), for i = 1, …, d − 1 i=1,\ldots,d-1, and then compute a Gröbner basis of the ideal I d I_{d} generated by these resultants in ℚ ⁡ [a 1, …, a d − 1] {\mathbb{Q}}[a_{1},\ldots,a_{d-1}]. The Conjecture is true for degree d d in characteristic 0 0 if and only if the Gröbner basis for I d I_{d} (in any term ordering) contains, for each i i, an element whose leading term is a power of a i a_{i} (see [AL94] for more on these concepts).

We have done several such computations, using the packages Singular [GPS05], Magma [BCP97], Macaulay 2 [GS], and Maple [MG+07], all of which offer Gröbner basis computations for ideals in multivariate polynomial rings.

However, the cost of these computations becomes prohibitive already for small degrees d d. Taking the smallest open case, d = 12 d=12, one will find that even computing the resultants is impossible, let alone computing a Gröbner basis. The main problem here is that these are polynomials in many variables, which tend to have exponentially many nonzero terms, whereas a Gröbner basis may again contain exponentially many such polynomials.

Another approach, used by the authors of [DG05], is to take the zeros of P P as parameters instead of the coefficients. Here one obtains an explicit decomposition of I d I_{d} into ideals that are “more primary” than I d I_{d}, and one proceeds with these. Unfortunately, the number of these components grows exponentially with d d, and the largest case that was solved using this technique is d = 8 d=8 (personal communication).

It may be expected that the computations become easier if we reduce the ideal I d I_{d} modulo a prime, because many terms may become zero. This is in fact the case, and allows quick verification of the Conjecture for some small degrees.

Pushing the argument of Proposition 2.5 a little further, one can even show that if d = p k d=p^{k}, then the polynomials Res X ⁡ ( P, P i) \Res_{X}(P,P_{i}), for i = 1, …, d − 1 i=1,\ldots,d-1, *already form a Gröbner basis*of the reduction of the ideal I d I_{d} modulo p p, for the weighted degree reverse lexicographic monomial order with a 1 < a 2 < … < a d − 1 a_{1}<a_{2}<\ldots<a_{d-1}. The leading monomial of Res X ⁡ ( P, P i) \Res_{X}(P,P_{i}) under this order is a d − i d a_{d-i}^{d}. This provides an alternative proof that the projective variety of the ideal over 𝔽 ¯ p \overline{{\mathbb{F}}}_{p} is empty.

However, when trying to solve the case d = 12 d=12 by reducing modulo p p, one finds that there are counterexamples in characteristic p = 2, 3, 5, 7, 11, 13 p=2,3,5,7,11,13, while for p = 17 p=17 and larger we face the same complexity problems as in characteristic 0 0.

Another way to obtain partial information is to fix several coefficients a priori. For example, when we put P = X 6 + a ​ X 4 + X 3 + b ​ X 2 P=X^{6}+aX^{4}+X^{3}+bX^{2}, as in the last section, we can readily compute a Gröbner basis of I 6 I_{6}, even when we take ℤ {\mathbb{Z}} as the base ring instead of ℚ {\mathbb{Q}}. The ideal I 6 I_{6} is here generated by three inhomogeneous equations in two variables (two resultants are zero), and its Gröbner basis contains the integer

 | M = 13 3 ⋅ 19 7 ⋅ 67 2 ⋅ 20771 2 ⋅ 21379 ⋅ 23993 3 ⋅ 7783207 ⋅ 40362599 ⋅ 7390044713023799. M=13^{3}\cdot 19^{7}\cdot 67^{2}\cdot 20771^{2}\cdot 21379\cdot 23993^{3}\cdot 7783207\cdot 40362599\cdot 7390044713023799. |  |

It follows that some quadrinomial of the cited form violates the Conjecture in characteristic p p if and only if p p is a prime factor of M M.

## References

- [AL94] W. Adams and P. Loustaunau. An introduction to Gröbner bases. Graduate Studies in Mathematics, 3. American Mathematical Society, 1994.
- [BCP97] W. Bosma, J. Cannon, and C. Playoust. The Magma algebra system. I. The user language. J. Symbolic Comput., 24(3-4):235–265, 1997. Computational algebra and number theory (London, 1993). To be ordered via [http://magma.maths.usyd.edu.au][11].
- [DG05] G. Diaz-Toca and L. Gonzalez-Vega. On a conjecture about univariate polynomials and their roots. In A. Dolzmann, A. Seidl, and T. Sturm, editors, Algorithmic Algebra and Logic 2005, pages 83–90, Norderstedt, Germany, 2005. Books on Demand.
- [GPS05] G.-M. Greuel, G. Pfister, and H. Schönemann. Singular 3.0. A Computer Algebra System for Polynomial Computations. Centre for Computer Algebra, University of Kaiserslautern (2005). Available at [http://www.singular.uni-kl.de][12].
- [GS] D. R. Grayson and M. E. Stillman. Macaulay 2, a software system for research in algebraic geometry. Available at [http://www.math.uiuc.edu/Macaulay2/][13].
- [Har77] R. Hartshorne. Algebraic Geometry. Springer Verlag, 1977.
- [Kum52] E. E. Kummer. Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen. J. Reine Angew. Math., 44:65–74, 1852.
- [MG+07] M. Monagan, K. Geddes, K. Heal, G. Labahn, S. Vorkoetter, J. McCarron, and P. DeMarco. Maple 11 Programming Guide. Maplesoft, 2007. To be ordered via [http://www.maplesoft.com][14].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: http://www-ifm.math.uni-hannover.de/~bothmer
[4]: mailto:%0Abothmer%0A
[5]: http://www.OliverLabs.net
[6]: mailto:%0ALabs%0A
[7]: http://www.ricam.oeaw.ac.at/research/symcomp
[8]: mailto:%0Ajosef.schicho%0A
[9]: http://www.opt.math.tugraz.at/~cvdwoest
[10]: mailto:%0Ac.vandewoestijne%0A
[11]: http://magma.maths.usyd.edu.au
[12]: http://www.singular.uni-kl.de
[13]: http://www.math.uiuc.edu/Macaulay2/
[14]: http://www.maplesoft.com
