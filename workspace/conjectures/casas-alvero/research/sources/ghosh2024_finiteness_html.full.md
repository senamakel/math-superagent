<!-- source: https://arxiv.org/html/2402.18717v3 | converted from HTML -->

A finiteness result towards the Casas-Alvero conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2402.18717v3 [math.AG] 14 Jan 2025

\DefineSimpleKey

bibprimaryclass \DefineSimpleKey bibarchiveprefix

# A finiteness result towards the Casas-Alvero conjecture

Soham Ghosh Address: Department of Mathematics, University of Washington, Seattle, WA 98195, USA Email address: [soham13@uw.edu][3]

Date: August 11, 2026

###### Abstract.

The Casas-Alvero conjecture predicts that every univariate polynomial over an algebraically closed field of characteristic zero sharing a common factor with each of its Hasse-Schmidt derivatives is a power of a linear polynomial. The conjecture for polynomials of a fixed degree is equivalent to the projective variety of such polynomials being one-dimensional. In this paper, we show that for any algebraically closed field of arbitrary characteristic, this variety is at most two-dimensional for all positive degrees. Consequently, we show that the associated arithmetic Casas-Alvero scheme in any positive degree has finitely many rational points over any field. Along the way, we prove several rigidity results towards the conjecture. We also introduce intermediate arithmetic Casas-Alvero schemes and show that their 𝕂 \mathbb{K} points form an almost complete intersection over any algebraically closed field 𝕂 \mathbb{K}. Furthermore, we consider the question of when they form a complete intersection.

###### Key words and phrases:

Casas-Alvero conjecture, complete intersection, Hasse-Schmidt derivations, higher discriminants

###### 2020 Mathematics Subject Classification

12E05, 13C15, 13N15, 14G05, 14M10

## 1. Introduction

### 1.1. Aim and main results of the paper

Let 𝕂 \mathbb{K} be a field and f ⁡ ( X) ∈ 𝕂 ⁡ [X] f(X)\in\mathbb{K}[X] be a monic polynomial of degree n > 1 n>1. Let f ( i) ​ ( X):= d i ​ f ​ ( X) / d ​ X i f^{(i)}(X):=d^{i}f(X)/dX^{i} be the i t ​ h i^{th} formal derivative of f ⁡ ( X) f(X) with respect to X X and let f i ​ ( X) f_{i}(X) be the i t ​ h i^{th} Hasse–Schmidt derivative of f ⁡ ( X) f(X). Over fields of characteristic 0 0, the two derivatives are related via f i ​ ( X) = f ( i) ​ ( X) / i! f_{i}(X)=f^{(i)}(X)/i!. This paper is concerned with the following question posed by E. Casas-Alvero in connection with his work [1] on higher-order polar germs:

###### Conjecture CA (Casas-Alvero, 2001).

Let f ⁡ ( X) f(X) be a monic univariate polynomial of degree n n over a field 𝕂 \mathbb{K}. Then gcd ⁡ ( f, f i) \gcd(f,f_{i}) is non-trivial for each i = 1, …, n − 1 i=1,\dots,n-1 if and only if f ⁡ ( X) = ( X − α) n f(X)=(X-\alpha)^{n} for some α ∈ 𝕂 \alpha\in\mathbb{K}.

In [7], the authors prove Conjecture CA (over characteristic 0 0) and in degrees n = p k n=p^{k} and 2 ​ p k 2p^{k} for any prime p p and k ∈ ℕ k\in\mathbb{N} by reformulating the problem over any field 𝕂 \mathbb{K} (irrespective of characteristic) as the absence of 𝕂 \mathbb{K} -rational points on a certain weighted projective ℤ \mathbb{Z} -scheme X n ⊆ ℙ ℤ ​ ( 1, 2, …, n − 1) X_{n}\subseteq\mathbb{P}_{\mathbb{Z}}(1,2,\dots,n-1). We refer to X n X_{n} as the n t ​ h n^{th} arithmetic Casas-Alvero scheme. As a consequence of the methods of [7], it follows that, for algebraically closed fields and a fixed degree n n, Conjecture CA depends only on the characteristic of the field 𝕂 \mathbb{K}, and if it is true over a certain characteristic, then it is true in all characteristics except finitely many primes. These results were improved in [5], where the authors used p p -adic valuation techniques to also prove Conjecture CA (over characteristic 0 0) in degrees 3 ​ p k 3p^{k} and 4 ​ p k 4p^{k} for primes p > 3 p>3, excepting degrees n = 4.5 k n=4.5^{k} and 4.7 k 4.7^{k}. The case of d = 5 ​ p k d=5p^{k} and corresponding bad primes were studied in [3]. Furthermore, the Conjecture in degrees d = 6 ​ p k d=6p^{k}, 7 ​ p k 7p^{k} (and 5 ​ p k 5p^{k} as well) has been verified in [2] with the aid of a computer, barring the bad primes in each case, which were also completely identified.

The main goal of this paper is to prove a finiteness result towards Conjecture CA for degree n ≥ 3 n\geq 3 over any field (of arbitrary characteristic).

We introduce the notion of (higher) D-subschemes of affine 𝕂 \mathbb{K} -schemes and various refinements (see Definitions 3.1, 3.7, 3.8) to encode derivations, along with characteristic maps (see Definition 4.2) for shift equivalence classes of monic polynomials f ⁡ ( X) ∈ 𝕂 ⁡ [X] f(X)\in\mathbb{K}[X]. These enable us to reformulate Conjecture CA (for 𝕂 \mathbb{K} algebraically closed) as a complete intersection problem for (higher) discriminant hypersurfaces Disc n i ⊆ 𝔸 𝕂 n \operatorname{Disc}^{i}_{n}\subseteq\mathbb{A}^{n}_{\mathbb{K}} ( 1 ≤ i ≤ n − 1 1\leq i\leq n-1). We relate these hypersurfaces to a union X n i X^{i}_{n} of certain involutions of D-subschemes of reduced principal monomial affine 𝕂 \mathbb{K} -schemes by the use of “Vieta’s map” ν n: 𝔸 𝕂 n → 𝔸 𝕂 n \nu_{n}:\mathbb{A}^{n}_{\mathbb{K}}\rightarrow\mathbb{A}^{n}_{\mathbb{K}}. Furthermore, Vieta’s map yields a regular map ν ¯ n: ℙ 𝕂 n − 1 → ℙ 𝕂 ​ ( 1, 2, …, n − 1) \overline{\nu}_{n}:\mathbb{P}^{n-1}_{\mathbb{K}}\rightarrow\mathbb{P}_{\mathbb{K}}(1,2,\dots,n-1) from straight projective space to a weighted one, using which we relate the projectivization of ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) in ℙ 𝕂 n − 1 ​ ( 𝕂) \mathbb{P}^{n-1}_{\mathbb{K}}(\mathbb{K}) and X n ​ ( 𝕂) ⊆ ℙ 𝕂 ​ ( 1, 2, …, n − 1) X_{n}(\mathbb{K})\subseteq\mathbb{P}_{\mathbb{K}}(1,2,\dots,n-1) (see Section 4.3). For any algebraically closed field 𝕂 \mathbb{K}, we prove the following dimension bound:

###### Theorem A (=Theorem 5.6).

For n ≥ 3 n\geq 3 and any algebraically closed field 𝕂 \mathbb{K}, dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) ≤ 2 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})\leq 2.

We prove Theorem A by decomposing dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) as a union ⋃ 1 ≤ j 1, …, j n − 1 ≤ n Z j 1, …, j n − 1 ​ ( 𝕂) \bigcup_{1\leq j_{1},\dots,j_{n-1}\leq n}Z_{j_{1},\dots,j_{n-1}}(\mathbb{K}) and encoding each Z j 1, …, j n − 1 ​ ( 𝕂) Z_{j_{1},\dots,j_{n-1}}(\mathbb{K}) as a deformation of a 1 1 -dimensional complete intersection via a family φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}_{\mathbb{K}}^{1}, for each choice of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. We show that each Z j 1, …, j n − 1 Z_{j_{1},\dots,j_{n-1}} is at most 2 2 -dimensional, from which Theorem A follows. This is done by showing that the family Y ⁡ ( j 1, …, j n − 1) Y(j_{1},\dots,j_{n-1}) is a 1 1 -dimensional Cohen-Macaulay scheme away from possibly one fiber (see Proposition 5.3). We then obtain the following result as an immediate corollary.

###### Theorem B (=Corollary 5.7).

For all n ≥ 3 n\geq 3, X n ​ ( 𝕂) X_{n}(\mathbb{K}) is finite for any field 𝕂 \mathbb{K}.

Concretely, Theorem B then says that for any n ≥ 2 n\geq 2, over any field 𝕂 \mathbb{K}, there are at most finitely many counterexamples to Conjecture CA in degree n n up to affine transformations (i.e., transformations of the form f ⁡ ( X) ↦ a − n ​ f ​ ( a ​ X + b) f(X)\mapsto a^{-n}f(aX+b), for a ∈ 𝕂 × a\in\mathbb{K}^{\times}, b ∈ 𝕂 b\in\mathbb{K}). Our method of proof also enables us to obtain a cohomological upper bound on the number of rational points | X n ​ ( 𝕂) | |X_{n}(\mathbb{K})| for any field 𝕂 \mathbb{K} (see Corollary 5.11). Consequently, we obtain:

###### Corollary C (=Corollary 5.8).

X n X_{n} is a finite ℤ \mathbb{Z} -scheme of dimension ≤ 1 \leq 1 for all n ≥ 3 n\geq 3. In particular, X n X_{n} is affine.

We also provide some rigidity implications of Theorem A for the structure of ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) in Section 5.2. By construction, the location of singular fibers of φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}_{\mathbb{K}}^{1} (for all 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n) is intimately related with Conjecture CA. We provide the following constraint for the singular fibers of these families using reduction mod p p methods, when 𝕂 \mathbb{K} is algebraically closed of characteristic 0 0 (see Theorem 5.16).

###### Theorem D (=Theorem 5.16).

Let 𝕂 \mathbb{K} be an algebraically closed field of characteristic 0 0. There are no singular ℚ \mathbb{Q} -rational fibers (i.e. fibers over 𝔸 𝕂 1 ​ ( ℚ) \mathbb{A}^{1}_{\mathbb{K}}(\mathbb{Q})) of φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}^{1}_{\mathbb{K}} outside { 1 m, m ∈ ℤ ∖ { 0 } } ⊆ ℚ \{\frac{1}{m},\ m\in\mathbb{Z}\setminus\{0\}\}\subseteq\mathbb{Q}. Furthermore, for all | m | ≥ 2 |m|\geq 2, there exists a finite set of primes 𝒫 ⁡ ( m) \mathcal{P}(m), such that the fibers ( φ ⋆) − 1 ​ ( 1 m p − 2) (\varphi^{\star})^{-1}(\frac{1}{m^{p-2}}) are non-singular for all p ∉ 𝒫 ⁡ ( m) p\notin\mathcal{P}(m).

Finally, we introduce intermediate arithmetic Casas-Alvero schemes X n ​ [j] X_{n}[j] for 1 ≤ j ≤ n − 1 1\leq j\leq n-1 (see Definition 6.1) such that X n ​ [n − 1] = X n X_{n}[n-1]=X_{n} is the n t ​ h n^{th} arithmetic Casas-Alvero scheme. Motivated from Conjecture CA, we consider the question of when X n ​ [j] ​ ( 𝕂) X_{n}[j](\mathbb{K}) form a complete intersection (Question 6.4), where 𝕂 \mathbb{K} is algebraically closed. As a measure of failure of Conjecture CA when it is not true, we consider the maximum value j C ​ ( n) j_{C}(n) of indices 1 ≤ j ≤ n − 1 1\leq j\leq n-1 for which X n ​ [j] ​ ( 𝕂) X_{n}[j](\mathbb{K}) is a complete intersection. Then Conjecture CA is equivalent to the claim that j C ​ ( n) = n − 1 j_{C}(n)=n-1 when 𝕂 \mathbb{K} has characteristic 0 0. The main technical result of this section is Proposition 6.5, using which we prove our final result provides a lower bound on j C ​ ( n) j_{C}(n) for n ≥ 3 n\geq 3.

###### Theorem E (=Corollary 6.8).

Let 𝕂 \mathbb{K} be algebraically closed of characteristic 0 0. Let q ⁡ ( n) q(n) be the largest number less than or equal to n n which is of the form p k p^{k} or 2 ​ p k 2p^{k} for some prime p p and k ∈ ℕ k\in\mathbb{N}. Then j C ​ ( n) ≥ q ⁡ ( n) − 1 j_{C}(n)\geq q(n)-1.

### 1.2. Existing results and methods

Conjecture CA was originally posed over characteristic 0 0 fields 𝕂 \mathbb{K}, and it is known that the conjecture holds over ℂ \mathbb{C} if and only if it holds over all such fields 𝕂 \mathbb{K}. The conjecture does not hold in general over positive characteristic (cf. [7] for counterexamples). Furthermore, they show that the truth of Conjecture CA over algebraically closed fields in a particular degree d d is independent of the choice of field, and only depends on its characteristic. The first progress over characteristic 0 0 was made for degree ≤ 7 \leq 7 polynomials via computational methods in [4]. Soon after, in [7] the authors related the conjecture for a general polynomial P ⁡ ( X) P(X) over any field 𝕂 \mathbb{K} to the absence of 𝕂 \mathbb{K} -rational points of a weighted projective ℤ \mathbb{Z} -subscheme of ℙ ℤ ​ ( 1, 2, …, n − 1) \mathbb{P}_{\mathbb{Z}}(1,2,\dots,n-1) defined by vanishing of resultants Res X ⁡ ( P, P i) \Res_{X}(P,P_{i}) for all 1 ≤ i < deg ⁡ P 1\leq i<\deg P. Their methods utilizing reduction modulo prime arguments, successfully proved the conjecture over fields of characteristic 0 0 for polynomials of degree p k p^{k}, 2 ​ p k 2p^{k} for any prime p p. Furthermore, by [7, Proposition 2.2], if Conjecture CA holds for all polynomials of degree n n over fields of characteristic p p, for some p = 0 p=0 or p p prime, then Conjecture CA holds true for degree n n polynomials over fields of any characteristic except finitely many primes. These methods were reformulated and extended in [5] using p p -adic valuations, where the authors proved Conjecture CA over characteristic 0 0 for polynomials of degrees 3 ​ p k 3p^{k} and 4 ​ p k 4p^{k} for primes p p greater than 3 3 and 4 4 respectively (except p = 5, 7 p=5,7 when n = 4 n=4). These results are particular instances of the following propositions.

###### Proposition.

(Proposition 2.6 2.6, [7]). For any positive integer d d and prime number p p, if Conjecture CA holds in degree d d and characteristic p p, then Conjecture CA also holds in degree d ​ p k dp^{k} for any integer k ≥ 0 k\geq 0 in characteristics p p and 0 0.

###### Proposition.

(Proposition 9 9, [5]). Let ν p \nu_{p} be an extension to ℂ \mathbb{C} of the p p -adic valuation on ℚ \mathbb{Q} for some prime p p. Consider the local ring R:= { z ∈ ℂ ∣ ν p ​ ( z) ≥ 0 } R:=\{z\in\mathbb{C}\mid\ \nu_{p}(z)\geq 0\} with maximal ideal M = { z ∈ ℂ ∣ ν p ​ ( z) > 0 } M=\{z\in\mathbb{C}\mid\ \nu_{p}(z)>0\} and let 𝕂 p = R / M \mathbb{K}_{p}=R/M be its residue field. Suppose that n = n ′ ​ p e n=n^{\prime}p^{e} with n ′ < p n^{\prime}<p and that Conjecture CA holds for all polynomials in 𝕂 p ​ [X] \mathbb{K}_{p}[X] of degree n ′ n^{\prime}. Then the conjecture holds for all polynomials of degree n n in ℂ ⁡ [X] \mathbb{C}[X].

In this spirit, further results for certain polynomials of degree 5 ​ p k 5p^{k} were shown in [3]. Recently, the authors of [15] have attempted to extend the results of [7] by providing a non-exhaustive list of bad primes p p for each n > 1 n>1, i.e., primes p p such that Conjecture CA does not hold in degree n n in characteristic p p. There have also been several computational studies, cf. [2], where the authors verified the conjecture for polynomials of degrees d = 5 ​ p k, 6 ​ p k d=5p^{k},\ 6p^{k} and 7 ​ p k 7p^{k} barring the bad primes in each case, which were also completely classified. They also studied obstructions to hypothetical counterexamples and have verified the conjecture for degree 12 12. (which is missed by the cases considered above). Computational approaches involving Gröbner bases, even though theoretically possible, get practically infeasible for large degrees due to the complexity of resultants. Alternate approaches to the conjecture have involved analytic tools via the Gauss–Lucas theorem. However, analytic approaches so far have been successful only in very low degrees as demonstrated in [5]. We refer the readers to the references of the cited articles for further literature on the conjecture.

### 1.3. Organization of the paper

In Section 3, we introduce (higher) D-subschemes of affine 𝕂 \mathbb{K} -schemes over algebraically closed fields 𝕂 \mathbb{K} of characteristic 0 0 and provide a characteristic p p generalization using Hasse-Schmidt like derivations. We, furthermore, characterize their 𝕂 \mathbb{K} -rational points for principal monomial schemes. In Section 4, we develop the geometry of Conjecture CA by introducing shift equivalence of monic univariate polynomials and their characteristic maps. We construct (higher) discriminant hypersurfaces and relate them to the arithmetic Casas-Alvero schemes X n X_{n} of [7]. Using this, we prove Theorem B in Section 5 as a consequence of a dimension-bound result (Theorem A). Both of these are established using the technical commutative algebraic result Proposition 5.3, which is also proved in this section. We also provide a couple of rigidity implications of Theorem A and provide a constraint on the ℚ \mathbb{Q} -rational singular fibers of the deformation family at the heart of the proof of Theorem A. We end by our discussion on intermediate arithmetic Casas-Alvero schemes in Section 6, where we prove Theorem E.

### Acknowledgement

The author would like to thank Mark Spivakovksy and Daniel Schaub for pointing out a gap in the proof of Theorem A in a previous version of the paper, and for several enlightening discussions in the process of fixing it. He would also like to thank Max Lieblich, Farbod Shokrieh, Sándor Kovács, Utsav Choudhury, and Apoorva Khare for useful discussion and feedback at various stages. The author was partially supported by NSF CAREER DMS-2044564 and NSF FRG DMS-2151718 grants.

## 2. Global notations and Definitions

We list a few notations and definitions that will be used throughout the paper.

1. (i)

For a univariate polynomial f ⁡ ( x) = a n ​ x n + a n − 1 ​ x n − 1 + ⋯ + a 0 ∈ 𝕂 ⁡ [x] f(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\dots+a_{0}\in\mathbb{K}[x] over any field 𝕂 \mathbb{K}, we will denote the i t ​ h i^{th} Hasse–Schmidt derivative (introduced in [16]) of f ⁡ ( x) f(x) by f i ​ ( x) f_{i}(x), which is defined as

 | f i ​ ( x) = ( n i) ​ a n ​ x n − i + ( n − 1 i) ​ a n − 1 ​ x n − i − 1 + ⋯ + ( i i) ​ a i. f_{i}(x)={n\choose i}a_{n}x^{n-i}+{n-1\choose i}a_{n-1}x^{n-i-1}+\dots+{i\choose i}a_{i}. |  |

2. (ii)

We will denote the i t ​ h i^{th} multivariate Hasse–Schmidt derivation on 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] by H ​ D k i HD^{i}_{k}, which is defined as follows: for a monomial x 1 α 1 ​ … ​ x k α k ∈ 𝕂 ⁡ [x 1, …, x k] x_{1}^{\alpha_{1}}\dots x_{k}^{\alpha_{k}}\in\mathbb{K}[x_{1},\dots,x_{k}] define

(2.1) |  | H ​ D k i ​ x 1 α 1 ​ … ​ x k α k:= ∑ j 1 + ⋯ + j k = i ( α 1 j 1) ​ ( α 2 j 2) ​ … ​ ( α k j k) ​ x 1 α 1 − j 1 ​ … ​ x k α k − j k. HD_{k}^{i}x_{1}^{\alpha_{1}}\dots x_{k}^{\alpha_{k}}:=\sum_{j_{1}+\dots+j_{k}=i}{\alpha_{1}\choose j_{1}}{\alpha_{2}\choose j_{2}}\dots{\alpha_{k}\choose j_{k}}x_{1}^{\alpha_{1}-j_{1}}\dots x_{k}^{\alpha_{k}-j_{k}}. |  |

The derivation H ​ D k i: 𝕂 ⁡ [x 1, …, x k] → 𝕂 ⁡ [x 1, …, x k] HD^{i}_{k}:\mathbb{K}[x_{1},\dots,x_{k}]\rightarrow\mathbb{K}[x_{1},\dots,x_{k}] is defined by extending ( 2.1) 𝕂 \mathbb{K} -linearly.

3. (iii)

For any two univariate polynomials f ⁡ ( x), g ⁡ ( x) ∈ 𝕂 ⁡ [x] f(x),g(x)\in\mathbb{K}[x], we will denote their classical resultant (see [6] *Chapter 12) by Res ⁡ ( f, g) \operatorname{Res}(f,g).

## 3. D-subschemes and monomial affine 𝕂 \mathbb{K} -schemes

### 3.1. Preliminaries on D-subschemes

Let 𝕂 \mathbb{K} be an algebraically closed field of characteristic 0 0 unless otherwise mentioned and Alg 𝕂 \algk be the category of finitely generated commutative unital 𝕂 \mathbb{K} -algebras. For a given polynomial ring 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] over 𝕂 \mathbb{K}, let D k: 𝕂 ⁡ [x 1, …, x k] → 𝕂 ⁡ [x 1, …, x k] D_{k}:\mathbb{K}[x_{1},\dots,x_{k}]\rightarrow\mathbb{K}[x_{1},\dots,x_{k}] be the 𝕂 \mathbb{K} -linear derivation D k = ∑ i = 1 k ∂ / ∂ x i D_{k}=\sum_{i=1}^{k}\partial/\partial x_{i}. Furthermore, for any integer i ≥ 1 i\geq 1, let

 | D k i:= ( D k ∘ D k ∘ ⋯ ∘ D k): 𝕂 [x 1, …, x k] → 𝕂 [x 1, …, x k] D^{i}_{k}:=(D_{k}\circ D_{k}\circ\cdots\circ D_{k}):\mathbb{K}[x_{1},\dots,x_{k}]\rightarrow\mathbb{K}[x_{1},\dots,x_{k}] |  |

be the map obtained by composing D k D_{k} with itself i i times.

###### Definition 3.1 (D-ideal and D-subscheme).

Let ( X, 𝔸 𝕂 k) (X,\mathbb{A}^{k}_{\mathbb{K}}) be a pair of an affine 𝕂 \mathbb{K} -scheme X = Spec ⁡ ( A) X=\spec(A) and an affine space 𝔸 𝕂 k \mathbb{A}^{k}_{\mathbb{K}} into which X X embeds as a closed subscheme. Any embedding X ↪ 𝔸 𝕂 k X\hookrightarrow\mathbb{A}^{k}_{\mathbb{K}} induces a surjective 𝕂 \mathbb{K} -algebra homomorphism 𝕂 ⁡ [x 1, …, x k] → A \mathbb{K}[x_{1},\dots,x_{k}]\rightarrow A, whereby A = 𝕂 ⁡ [x 1, …, x k] / I A=\mathbb{K}[x_{1},\dots,x_{k}]/I for some ideal I ⊆ 𝕂 ⁡ [x 1, …, x k] I\subseteq\mathbb{K}[x_{1},\dots,x_{k}].

1. (i)

Define the D-ideal of I I to be the ideal D k ​ ( I):= ( { D k ​ ( f) ∣ f ∈ I }) ⊆ 𝕂 ⁡ [X 1, …, X k] D_{k}(I):=(\{D_{k}(f)\mid\ f\in I\})\subseteq\mathbb{K}[X_{1},\dots,X_{k}] generated by the image of I I under the derivation D k D_{k}.

2. (ii)

Define the D-subscheme of ( X, 𝔸 𝕂 k) (X,\mathbb{A}^{k}_{\mathbb{K}}) as the pair ( 𝒟 ​ X, 𝔸 𝕂 k) (\mathscr{D}X,\mathbb{A}^{k}_{\mathbb{K}}), where 𝒟 ​ X \mathscr{D}X is the affine 𝕂 \mathbb{K} -scheme Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / D k ​ ( I)) \spec(\mathbb{K}[x_{1},\dots,x_{k}]/D_{k}(I)).

###### Remark 3.2.

1.
2. (i)

Note that for every ideal I I that I ⊆ D k ​ ( I) I\subseteq D_{k}(I), because if f ∈ I f\in I, then f = D k ​ ( x 1 ​ f) − x 1 ​ D k ​ ( f) ∈ D k ​ ( I) f=D_{k}(x_{1}f)-x_{1}D_{k}(f)\in D_{k}(I). It follows that 𝒟 ​ X \mathscr{D}X is indeed a closed subscheme of X X.

3. (ii)

If an ideal I ⊆ 𝕂 ⁡ [X 1, …, X k] I\subseteq\mathbb{K}[X_{1},\dots,X_{k}] is generated by f 1, f 2, …, f m f_{1},f_{2},\dots,f_{m}, then we claim that D k ​ ( I) = ( f 1, …, f m, D k ​ ( f 1), …, D k ​ ( f m)) D_{k}(I)=(f_{1},\dots,f_{m},D_{k}(f_{1}),\dots,D_{k}(f_{m})). Indeed, given any element g = h 1 ​ f 1 + h 2 ​ f 2 + ⋯ + h m ​ f m ∈ I g=h_{1}f_{1}+h_{2}f_{2}+\cdots+h_{m}f_{m}\in I, we have D k ​ ( g) = ∑ i = 1 m ( D k ​ ( h i) ​ f i + h i ​ D k ​ ( f i)) ∈ ( f 1, …, f m, D k ​ ( f 1), …, D k ​ ( f m)) D_{k}(g)=\sum_{i=1}^{m}(D_{k}(h_{i})f_{i}+h_{i}D_{k}(f_{i}))\in(f_{1},\dots,f_{m},D_{k}(f_{1}),\dots,D_{k}(f_{m})) by the Leibniz rule for derivations. The reverse inclusion follows by definition of D k ​ ( I) D_{k}(I) and since I ⊆ D k ​ ( I) I\subseteq D_{k}(I).

#### 3.1.1. Linear reduction of affine 𝕂 \mathbb{K} -schemes

Let X = Spec ⁡ ( A) X=\spec(A) be an affine 𝕂 \mathbb{K} -scheme, with A = 𝕂 ⁡ [x 1, …, x k] / I A=\mathbb{K}[x_{1},\dots,x_{k}]/I where I = ( f 1, …, f m) ⊆ 𝕂 ⁡ [x 1, …, x k] I=(f_{1},\dots,f_{m})\subseteq\mathbb{K}[x_{1},\dots,x_{k}]. Assume the generator f 1 ​ ( x 1, …, x k) = a 0 + a 1 ​ x 1 + a 2 ​ x 2 + ⋯ + a k ​ x k f_{1}(x_{1},\dots,x_{k})=a_{0}+a_{1}x_{1}+a_{2}x_{2}+\cdots+a_{k}x_{k} is a linear polynomial, in which case D k ​ ( f 1) = a 1 + a 2 + ⋯ + a k D_{k}(f_{1})=a_{1}+a_{2}+\cdots+a_{k} is a scalar. We call such f 1 f_{1} to be D-degenerate, and classify them into the following two categories:

1. (i)

Tame D-degeneracy: This corresponds to the case D k ​ ( f 1) = a 1 + ⋯ + a k = 0 D_{k}(f_{1})=a_{1}+\cdots+a_{k}=0. Letting I ′ = ( f 2, f 3, …, f m) ⊆ 𝕂 ⁡ [X 1, …, X k] I^{\prime}=(f_{2},f_{3},\dots,f_{m})\subseteq\mathbb{K}[X_{1},\dots,X_{k}], we have D k ​ ( I) = ( f 1, D k ​ ( I ′)) D_{k}(I)=(f_{1},D_{k}(I^{\prime})). Thus, 𝒟 ​ X \mathscr{D}X is the scheme-theoretic intersection of the hypersurface Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / ( f 1)) \spec(\mathbb{K}[x_{1},\dots,x_{k}]/(f_{1})) and the D-subscheme 𝒟 ​ X ′ \mathscr{D}X^{\prime} of the affine 𝕂 \mathbb{K} -scheme X ′ = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I ′) X^{\prime}=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I^{\prime}) in 𝔸 𝕂 k \mathbb{A}^{k}_{\mathbb{K}}.

2. (ii)

Wild D-degeneracy: This corresponds to the generic case when D k ​ ( f 1) = a 1 + ⋯ + a k ≠ 0 D_{k}(f_{1})=a_{1}+\cdots+a_{k}\neq 0, in which case D k ​ ( I) = 𝕂 ⁡ [x 1, …, x k] D_{k}(I)=\mathbb{K}[x_{1},\dots,x_{k}] and thus, 𝒟 ​ X \mathscr{D}X collapses to the empty subscheme.

Thus, generically, linear polynomials in the defining ideal of an affine 𝕂 \mathbb{K} -scheme X X collapse the D-subscheme 𝒟 ​ X \mathscr{D}X (wild case), or are redundant (tame case). This situation can be rectified by the process of linear reduction of X X, which we now describe:

Since f 1 = a 0 + a 1 ​ x 1 + ⋯ + a k ​ x k f_{1}=a_{0}+a_{1}x_{1}+\cdots+a_{k}x_{k} is non-constant, assume, without loss of generality, that a 1 ≠ 0 a_{1}\neq 0 and consider the 𝕂 \mathbb{K} -algebra homomorphism π f 1: 𝕂 ⁡ [x 1, …, x k] → 𝕂 ⁡ [x 2, …, x k] \pi_{f_{1}}:\mathbb{K}[x_{1},\dots,x_{k}]\rightarrow\mathbb{K}[x_{2},\dots,x_{k}] given by

 | x 1 ↦ − ( a 0 + a 2 x 2 + a 3 x 3 + ⋯ + a k x k) / a 1 and x i ↦ x i for all i ≥ 2. x_{1}\mapsto-(a_{0}+a_{2}x_{2}+a_{3}x_{3}+\cdots+a_{k}x_{k})/a_{1}\quad\text{and }x_{i}\mapsto x_{i}\text{ for all }i\geq 2. |  |

Geometrically, this map induces the inclusion of 𝔸 𝕂 k − 1 \mathbb{A}^{k-1}_{\mathbb{K}} into 𝔸 𝕂 k \mathbb{A}^{k}_{\mathbb{K}} by identifying it with the hyperplane V ⁡ ( f 1) ⊆ 𝔸 𝕂 k V(f_{1})\subseteq\mathbb{A}^{k}_{\mathbb{K}}. Furthermore, ker ⁡ π f 1 = ( f 1) \ker\pi_{f_{1}}=(f_{1}) and thus, we obtain the isomorphism of 𝕂 \mathbb{K} -algebras

 | A = 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f k) ≅ 𝕂 ⁡ [x 2, …, x k] / ( π f 1 ​ ( f 2), π f 1 ​ ( f 3), …, π f 1 ​ ( f k)) =: A 1. A=\mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{k})\cong\mathbb{K}[x_{2},\dots,x_{k}]/(\pi_{f_{1}}(f_{2}),\pi_{f_{1}}(f_{3}),\dots,\pi_{f_{1}}(f_{k}))=:A_{1}. |  |

It follows that, although X 1:= Spec ⁡ ( A 1) X_{1}:=\spec(A_{1}) is isomorphic to X:= Spec ⁡ ( A) X:=\spec(A) as affine 𝕂 \mathbb{K} -schemes, X 1 X_{1} comes with a natural embedding into 𝔸 𝕂 k − 1 \mathbb{A}^{k-1}_{\mathbb{K}}. We define the linear reduction of ( X, 𝔸 𝕂 k) (X,\mathbb{A}^{k}_{\mathbb{K}}) with respect to f 1 ∈ I f_{1}\in I as the pair ( X 1, 𝔸 𝕂 k − 1) (X_{1},\mathbb{A}^{k-1}_{\mathbb{K}}). Note that we can define the linear reduction of X = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I) X=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I) with respect to any linear polynomial f 1 ∈ I f_{1}\in I, by extending { f 1 } \{f_{1}\} to a generating set for I I. This process is well-defined, i.e., independent of the choice of generators of I I, since the linear reduction of X X with respect to f 1 ∈ I f_{1}\in I is the affine scheme Spec ⁡ ( 𝕂 ⁡ [x 2, …, x k] / π f 1 ​ ( I)) \spec(\mathbb{K}[x_{2},\dots,x_{k}]/\pi_{f_{1}}(I)) with its embedding in 𝔸 𝕂 k − 1 \mathbb{A}^{k-1}_{\mathbb{K}}.

The process of linear reduction can be iterated until one obtains an affine 𝕂 \mathbb{K} -scheme X lred = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x q] / I lred) X_{\lred}=\spec(\mathbb{K}[x_{1},\dots,x_{q}]/I_{\lred}) isomorphic to X X, such that I lred I_{\lred} does not contain any non-constant linear polynomials. This process terminates after finitely many steps since after each linear reduction we obtain an affine scheme isomorphic to X X embedding into an affine space of one lower dimension. The following definitions formalize this sequence of linear reductions algebraically.

###### Definition 3.3 (Linear sequences).

1. (i)

A sequence of polynomials f 1, …, f r f_{1},\dots,f_{r} in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] is said to form a linear sequence if f 1 f_{1} is a non-constant linear polynomial in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] and for each 2 ≤ i ≤ r 2\leq i\leq r, the residue of f i f_{i} in 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f i − 1) \mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{i-1}) is a non-constant linear polynomial.

2. (ii)

For an ideal I ⊆ 𝕂 ⁡ [x 1, …, x k] I\subseteq\mathbb{K}[x_{1},\dots,x_{k}], a sequence of polynomials f 1, f 2, …, f r ∈ 𝕂 ⁡ [x 1, …, x k] f_{1},f_{2},\dots,f_{r}\in\mathbb{K}[x_{1},\dots,x_{k}] is said to form an I I -linear sequence if the f i f_{i} form a linear sequence and each f i f_{i} belongs in I I.

Although, for a linear sequence f 1, …, f r ∈ 𝕂 ⁡ [x 1, …, x k] f_{1},\dots,f_{r}\in\mathbb{K}[x_{1},\dots,x_{k}], we do not require f i f_{i} to be linear for 2 ≤ i ≤ r 2\leq i\leq r, one can assume them to be linear without loss of generality, by considering the residue of f i f_{i} modulo ( f 1, …, f i − 1) (f_{1},\dots,f_{i-1}) in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}]. Furthermore, it is clear that any non-constant linear polynomial in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] is a linear sequence of length 1 1.

###### Remark 3.4.

1.
2. (i)

For any linear sequence f 1, …, f r f_{1},\dots,f_{r} in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}], one contains the 𝕂 \mathbb{K} -algebra isomorphism 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f r) ≅ 𝕂 ⁡ [y 1, y 2, …, y k − r] \mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{r})\cong\mathbb{K}[y_{1},y_{2},\dots,y_{k-r}] by inducting on r r. In particular, the quotient of 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] by an ideal generated by a linear sequence is a global complete intersection. Furthermore, we also note that the length r r of any linear sequence f 1, …, f r f_{1},\dots,f_{r} in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] is at most k k.

3. (ii)

For an embedded affine scheme ( X, 𝔸 𝕂 k) (X,\mathbb{A}^{k}_{\mathbb{K}}) defined by X = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I) X=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I), the process of r r iterations of linear reduction is equivalent to taking an I I -linear sequence f 1, …, f r ∈ 𝕂 ⁡ [x 1, …, x k] f_{1},\dots,f_{r}\in\mathbb{K}[x_{1},\dots,x_{k}] and embedding X X in the closed subscheme Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f r)) ⊆ 𝔸 𝕂 n \spec(\mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{r}))\subseteq\mathbb{A}^{n}_{\mathbb{K}} as the closed subscheme Spec ⁡ 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f r) OPEN I / ( f 1, …, f r)) \displaystyle\spec\frac{\mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{r})}{I/(f_{1},\dots,f_{r}))}.

4. (iii)

By the embedding of X X in Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f r)) \spec(\mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{r})) from point ( 2) (2) above, we must have dim X ≤ dim 𝕂 ⁡ [x 1, …, x k] / ( f 1, …, f r) = k − r \dim X\leq\dim\mathbb{K}[x_{1},\dots,x_{k}]/(f_{1},\dots,f_{r})=k-r, where the last equality follows from point ( 1) (1) above. In particular, we note that for any proper ideal I ⊆ 𝕂 ⁡ [x 1, …, x k] I\subseteq\mathbb{K}[x_{1},\dots,x_{k}], the length r r of any I I -linear sequence is at most codim 𝕂 ⁡ [x 1, …, x k] ⁡ ( I) \cdim_{\mathbb{K}[x_{1},\dots,x_{k}]}(I).

We noted earlier that the process of linear reduction of an embedded affine scheme ( X, 𝔸 𝕂 k) (X,\mathbb{A}^{k}_{\mathbb{K}}) terminates after finitely many steps (in fact, after at most codim ⁡ ( X) \cdim(X) steps by Remark 3.4 (iii). The terminal linearly reduced affine scheme obtained from X = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I) X=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I), corresponds to a maximal I I -linear sequence of 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] by Remark 3.4 (ii). A priori, this process depends on the choice of the maximal I I -linear sequence polynomial. The following proposition shows that the terminal scheme obtained from X X is well-defined.

###### Proposition 3.5.

Let I ⊊ 𝕂 ⁡ [x 1, …, x k] I\subsetneq\mathbb{K}[x_{1},\dots,x_{k}] be a proper ideal, and I lin ⊆ I I_{\lin}\subseteq I be the sub-ideal generated by all the linear polynomials in I I. If f 1, …, f r f_{1},\dots,f_{r} in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] is any maximal I I -linear sequence, then I lin = ( f 1, …, f r) I_{\lin}=(f_{1},\dots,f_{r}) as ideals of 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}].

###### Proof.

Without loss of generality, we may assume that f 1, …, f r f_{1},\dots,f_{r} are all linear polynomials in I ⊆ 𝕂 ⁡ [x 1, …, x k] I\subseteq\mathbb{K}[x_{1},\dots,x_{k}]. Clearly, we have ( f 1, …, f r) ⊆ I lin (f_{1},\dots,f_{r})\subseteq I_{\lin}. Suppose the reverse inclusion fails to hold, i.e., there exists a linear polynomial g ∈ I lin ∖ ( f 1, …, f r) g\in I_{\lin}\setminus(f_{1},\dots,f_{r}), whereby its residue modulo ( f 1, …, f r) (f_{1},\dots,f_{r}) is also linear. If the residue is non-constant, then f 1, f 2, …, f r, g f_{1},f_{2},\dots,f_{r},g would be an I I -linear sequence, contradicting the maximality of f 1, f 2, …, f r f_{1},f_{2},\dots,f_{r}. If the residue of g g modulo ( f 1, …, f r) (f_{1},\dots,f_{r}) is a non-zero constant scalar, then since ( f 1, …, f r) ⊆ I lin (f_{1},\dots,f_{r})\subseteq I_{\lin}, we would contradict the properness of I I. Thus, the residue of g g modulo ( f 1, …, f r) (f_{1},\dots,f_{r}) must be 0 0, or equivalently, g ∈ ( f 1, …, f r) g\in(f_{1},\dots,f_{r}). This proves the reverse inclusion. ∎

By Remark 3.4 (ii) and Proposition 3.5, the terminal affine scheme obtained by a maximal sequence of iterations of linear reductions of X = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I) X=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I) corresponding to any maximal I I -linear sequence in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] is uniquely defined. We have the following two definitions.

###### Definition 3.6 (Complete linear reduction).

Given an affine 𝕂 \mathbb{K} -scheme X = Spec ⁡ ( A) X=\spec(A), with A = 𝕂 ⁡ [x 1, …, x k] / I A=\mathbb{K}[x_{1},\dots,x_{k}]/I, we define the complete linear reduction of X X to be the isomorphic affine 𝕂 \mathbb{K} -scheme X lred:= Spec ⁡ ( A lred) X_{\lred}:=\spec(A_{\lred}), where A lred:= 𝕂 ⁡ [x 1, …, x q] / I lred A_{\lred}:=\mathbb{K}[x_{1},\dots,x_{q}]/I_{\lred} is the 𝕂 \mathbb{K} -algebra obtained from A A by applying any maximal sequence of linear reductions.

###### Definition 3.7 (Linearly essential D-subscheme).

Let X = Spec ⁡ ( A) X=\spec(A) be an affine 𝕂 \mathbb{K} -scheme with A = 𝕂 ⁡ [x 1, …, x k] / I A=\mathbb{K}[x_{1},\dots,x_{k}]/I for some ideal I ⊆ 𝕂 ⁡ [x 1, …, x k] I\subseteq\mathbb{K}[x_{1},\dots,x_{k}] with complete linear reduction X lred:= Spec ⁡ ( A lred) X_{\lred}:=\spec(A_{\lred}), where A lred:= 𝕂 ⁡ [x 1, …, x q] / I lred A_{\lred}:=\mathbb{K}[x_{1},\dots,x_{q}]/I_{\lred}. Define the linearly essential D-subscheme 𝒟 less ​ X \mathscr{D}_{\leff}X of X X to be the closed affine subscheme 𝒟 ​ X lred:= Spec ⁡ ( 𝕂 ⁡ [x 1, …, x q] / D q ​ ( I lred)) \mathscr{D}X_{\lred}:=\spec(\mathbb{K}[x_{1},\dots,x_{q}]/D_{q}(I_{\lred})).

Since the linearly essential D-subscheme 𝒟 less ​ X \mathscr{D}_{\leff}X of an affine 𝕂 \mathbb{K} -scheme X X is also affine, we define higher order linearly essential D-subschemes of X X by defining the analogous subschemes of 𝒟 less ​ X \mathscr{D}_{\leff}X.

###### Definition 3.8 (Linearly essential i t ​ h i^{th} D-subscheme).

Let X = Spec ⁡ ( A) X=\spec(A) be an affine 𝕂 \mathbb{K} -scheme with A = 𝕂 ⁡ [x 1, …, x k] / I A=\mathbb{K}[x_{1},\dots,x_{k}]/I. We define the linearly essential i t ​ h i^{th} D-subscheme of X X to be the affine 𝕂 \mathbb{K} -scheme 𝒟 less i X:= 𝒟 less ( 𝒟 less ( ⋯ ( 𝒟 less X) ⋯)) \mathscr{D}^{i}_{\leff}X:=\mathscr{D}_{\leff}(\mathscr{D}_{\leff}(\cdots(\mathscr{D}_{\leff}X)\cdots)) obtained by iterating the construction of linearly essential D-subscheme i i times for i > 0 i>0. Also define 𝒟 less 0 ​ X:= X \mathscr{D}_{\leff}^{0}X:=X.

###### Remark 3.9.

Let X = Spec ⁡ ( A) X=\spec(A) be an affine 𝕂 \mathbb{K} -scheme for some 𝕂 \mathbb{K} -algebra A = 𝕂 ⁡ [x 1, …, x k] / I A=\mathbb{K}[x_{1},\dots,x_{k}]/I, where I I is a homogeneous ideal generated by homogeneous polynomials f 1, …, f m f_{1},\dots,f_{m} of degree n > 1 n>1. Then I I does not contain any linear polynomials, so X = X lred X=X_{\lred} is completely linearly reduced. Note that the derivation D k D_{k} sends monomials in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] of degree n n to homogeneous polynomials of degree n − 1 n-1. Hence for each j j, the homogeneous ideals D k j ​ ( I):= D k ​ ( D k j − 1 ​ ( I)) D^{j}_{k}(I):=D_{k}(D^{j-1}_{k}(I)) are generated by the homogeneous polynomials D k i ​ ( f l) D^{i}_{k}(f_{l}) ( 0 ≤ i ≤ j 0\leq i\leq j and 1 ≤ l ≤ m 1\leq l\leq m) of degree at least n − j n-j. Consequently, for all 1 ≤ j ≤ n − 2 1\leq j\leq n-2, D k j ​ ( I) D^{j}_{k}(I) do not contain linear polynomials implying that the affine 𝕂 \mathbb{K} -subschemes 𝒟 less j ​ X = 𝒟 j ​ X ⊂ X \mathscr{D}_{\leff}^{j}X=\mathscr{D}^{j}X\subset X are completely linearly reduced. Thus, the linearly essential j t ​ h j^{th} D-subscheme of X X is

 | 𝒟 less j ​ X = 𝒟 j ​ X:= Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / D k j ​ ( I)), ∀ 1 ≤ j ≤ n − 1. \mathscr{D}^{j}_{\leff}X=\mathscr{D}^{j}X:=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/D^{j}_{k}(I)),\ \forall 1\leq j\leq n-1. |  |

#### 3.1.2. D-subschemes of affine schemes over positive characteristic

The 𝕂 \mathbb{K} -linear derivation D k: 𝕂 ⁡ [x 1, …, x k] → 𝕂 ⁡ [x 1, …, x k] D_{k}:\mathbb{K}[x_{1},\dots,x_{k}]\rightarrow\mathbb{K}[x_{1},\dots,x_{k}] and its higher compositions can be packaged together into a Hasse–Schmidt derivation exp ⁡ ( t ​ D k): 𝕂 ⁡ [x 1, …, x k] → 𝕂 ⁡ [x 1, …, x k] ​ [[t]] \exp(tD_{k}):\mathbb{K}[x_{1},\dots,x_{k}]\rightarrow\mathbb{K}[x_{1},\dots,x_{k}][\![t]\!] given by exp ⁡ ( D k):= ∑ i ≥ 0 ( D k i / i!) ​ t i \exp(D_{k}):=\sum_{i\geq 0}(D_{k}^{i}/i!)t^{i}. In fact, the i t ​ h i^{th} multivariate Hasse–Schmidt derivation obtained from D k D_{k} (i.e., the coefficient of t i t^{i} in exp ⁡ ( t ​ D k) \exp(tD_{k})) can be defined alternatively by ( 2.1).

When 𝕂 \mathbb{K} is an algebraically closed field of characteristic p p, we will use the i t ​ h i^{th} derivation on 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}] defined by ( 2.1). For an affine scheme X = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I) X=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I) over a positive characteristic field, one can naively define the j t ​ h j^{th} Hasse–Schmidt D-subscheme of X X as the subscheme ℋ ​ 𝒟 j ​ X:= Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / ( HD k ​ ( I), HD k 2 ​ ( I), …, HD k j ​ ( I))) \mathcal{HD}^{j}X:=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/(HD_{k}(I),HD^{2}_{k}(I),\dots,HD^{j}_{k}(I))). For “nice” affine schemes X = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I) X=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/I), i.e., those for which the ideal ( H ​ D k ​ ( I), H ​ D k 2 ​ ( I), …, H ​ D k j ​ ( I)) ⊆ 𝕂 ⁡ [x 1, …, x k] (HD_{k}(I),HD^{2}_{k}(I),\dots,HD^{j}_{k}(I))\subseteq\mathbb{K}[x_{1},\dots,x_{k}] is a proper ideal, the naive definition of ℋ ​ 𝒟 k j ​ X \mathcal{HD}^{j}_{k}X provides the desired construction. In general, one can construct reductions analogous to Definition 3.6 to tackle degeneracies.

In this paper, we will be concerned with (higher) δ \delta -subschemes (primarily δ = D k \delta=D_{k} and H ​ D k HD_{k}) of principal monomial schemes (over algebraically closed fields 𝕂 \mathbb{K}) of degree n ≥ 2 n\geq 2, and certain deformations of these over 𝔸 𝕂 1 \mathbb{A}^{1}_{\mathbb{K}}. A principal monomial scheme is defined to be a monomial scheme determined by a single monomial of total degree n ≥ 2 n\geq 2 in the ring 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}]. In particular, over characteristic p p, the naive definition of ℋ ​ 𝒟 k j ​ X \mathcal{HD}^{j}_{k}X works for such X X for all 1 ≤ j < 1\leq j< degree of the defining monomial.

### 3.2. D-subschemes of prinicpal monomial affine 𝕂 \mathbb{K} -schemes

Let 𝕂 \mathbb{K} be an algebraically closed field of characteristic 0 0. For an integer n ≥ 2 n\geq 2, let 𝐫:= ( r 1, …, r k) \mathbf{r}:=(r_{1},\dots,r_{k}) corresponding to a fixed ordered partition r 1 + r 2 + ⋯ + r k = n r_{1}+r_{2}+\cdots+r_{k}=n into k ≥ 1 k\geq 1 positive integers. Let 𝐱 𝐫 ∈ 𝕂 ⁡ [x 1, …, x k] \mathbf{x}^{\mathbf{r}}\in\mathbb{K}[x_{1},\dots,x_{k}] be the monomial 𝐱 𝐫 = ∏ i = 1 k x i r i \mathbf{x}^{\mathbf{r}}=\prod_{i=1}^{k}x_{i}^{r_{i}}. Define 𝒮 n ​ ( 𝐫) \mathscr{S}_{n}(\mathbf{r}) to be the affine monomial 𝕂 \mathbb{K} -scheme Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / I ⁡ ( 𝐫)) \spec(\mathbb{K}[x_{1},\dots,x_{k}]/I(\mathbf{r})), where I ⁡ ( 𝐫) I(\mathbf{r}) is the ideal generated by 𝐱 𝐫 \mathbf{x}^{\mathbf{r}} in 𝕂 ⁡ [x 1, …, x k] \mathbb{K}[x_{1},\dots,x_{k}]. We will identify the set of 𝕂 \mathbb{K} -rational points 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) with the corresponding affine algebraic subset V ⁡ ( I ⁡ ( 𝐫)) = V ⁡ ( 𝐱 𝐫) ⊆ 𝔸 𝕂 k V(I(\mathbf{r}))=V(\mathbf{x}^{\mathbf{r}})\subseteq\mathbb{A}^{k}_{\mathbb{K}}.

###### Remark 3.10.

The set of 𝕂 \mathbb{K} -rational points 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) is reducible, with irreducible components V ⁡ ( x i) V(x_{i}) for each 1 ≤ i ≤ k 1\leq i\leq k. With the canonical 𝕂 \mathbb{K} -affine scheme structure induced by 𝒮 n ​ ( 𝐫) \mathscr{S}_{n}(\mathbf{r}), each irreducible component V ⁡ ( x i) V(x_{i}) occurs with multiplicity r i r_{i}.

Since 𝐱 𝐫 ∈ 𝕂 ⁡ [x 1, …, x k] \mathbf{x}^{\mathbf{r}}\in\mathbb{K}[x_{1},\dots,x_{k}] is a monomial of degree at least 2 2, by Remark 3.9, we know that 𝒟 j ​ 𝒮 n ​ ( 𝐫):= Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / D k j ​ I ​ ( 𝐫)) = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / ( 𝐱 𝐫, D k ​ 𝐱 𝐫, …, D k j ​ 𝐱 𝐫)) \mathscr{D}^{j}\mathscr{S}_{n}(\mathbf{r}):=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/D^{j}_{k}I(\mathbf{r}))=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/(\mathbf{x}^{\mathbf{r}},D_{k}\mathbf{x}^{\mathbf{r}},\dots,D_{k}^{j}\mathbf{x}^{\mathbf{r}})) is completely linearly reduced for all 0 ≤ j ≤ n − 2 0\leq j\leq n-2. Thus, the linearly essential j t ​ h j^{th} D-subschemes of 𝒮 n ​ ( 𝐫) \mathscr{S}_{n}(\mathbf{r}) are:

 | 𝒟 j ​ 𝒮 n ​ ( 𝐫) = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x k] / ( 𝐱 𝐫, D k ​ 𝐱 𝐫, …, D k j ​ 𝐱 𝐫)), ∀ 1 ≤ j ≤ n − 1. \mathscr{D}^{j}\mathscr{S}_{n}(\mathbf{r})=\spec(\mathbb{K}[x_{1},\dots,x_{k}]/(\mathbf{x}^{\mathbf{r}},D_{k}\mathbf{x}^{\mathbf{r}},\dots,D_{k}^{j}\mathbf{x}^{\mathbf{r}})),\ \forall\ 1\leq j\leq n-1. |  |

Henceforth we will refer to these closed subschemes of 𝒮 n ​ ( 𝐫) \mathscr{S}_{n}(\mathbf{r}) as the (higher) D-subschemes of 𝒮 \mathscr{S}.

The next result characterizes the set of 𝕂 \mathbb{K} -rational points 𝒟 j ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{D}^{j}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) for all 0 ≤ j ≤ n − 1 0\leq j\leq n-1 in terms of the irreducible components V ⁡ ( x i) V(x_{i}) of 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{S}_{n}(\mathbf{r})(\mathbb{K}). The set of 𝕂 \mathbb{K} -rational points 𝒟 j ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{D}^{j}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) is equal to V ⁡ ( 𝐱 𝐫, D k ​ 𝐱 𝐫, …, D k j ​ 𝐱 𝐫) = ⋂ i = 1 j V ⁡ ( 𝐱 𝐫, D k i ​ 𝐱 𝐫) ⊆ 𝔸 𝕂 k ​ ( 𝕂) V(\mathbf{x}^{\mathbf{r}},D_{k}\mathbf{x}^{\mathbf{r}},\dots,D_{k}^{j}\mathbf{x}^{\mathbf{r}})=\bigcap_{i=1}^{j}V(\mathbf{x}^{\mathbf{r}},D_{k}^{i}\mathbf{x}^{\mathbf{r}})\subseteq\mathbb{A}^{k}_{\mathbb{K}}(\mathbb{K}). The following proposition gives the set-theoretic description of 𝒟 j ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{D}^{j}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}).

###### Proposition 3.11.

For all 1 ≤ j ≤ n 1\leq j\leq n, the set 𝒟 j − 1 ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{D}^{j-1}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) of 𝕂 \mathbb{K} -rational points of the ( j − 1) t ​ h (j-1)^{th} D-subscheme of 𝒮 n ​ ( 𝐫) \mathscr{S}_{n}(\mathbf{r}) is the affine algebraic subset of 𝔸 𝕂 k ​ ( 𝕂) \mathbb{A}^{k}_{\mathbb{K}}(\mathbb{K}) given by

(3.1) |  | 𝒟 j − 1 ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) = ⋃ l = 1 j ⋃ i 1 < i 2 < ⋯ < i l r i 1 + r i 2 + ⋯ + r i l ≥ j V ⁡ ( x i 1) ∩ V ⁡ ( x i 2) ∩ ⋯ ∩ V ⁡ ( x i l). \mathscr{D}^{j-1}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K})=\bigcup_{l=1}^{j}\bigcup_{\begin{subarray}{c}i_{1}<i_{2}<\cdots<i_{l}\\ r_{i_{1}}+r_{i_{2}}+\cdots+r_{i_{l}}\geq j\end{subarray}}V(x_{i_{1}})\cap V(x_{i_{2}})\cap\cdots\cap V(x_{i_{l}}). |  |

###### Proof.

We induct on j j, with Remark 3.10 corresponding to the base case j = 1 j=1. Let us assume that the statement holds for some j = m < n j=m<n. Since

 | 𝒟 j − 1 ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) = V ⁡ ( 𝐱 𝐫, D k ​ 𝐱 𝐫, …, D k j − 1 ​ 𝐱 𝐫) ⊆ 𝔸 𝕂 k ​ ( 𝕂) ∀ j ≤ n, \mathscr{D}^{j-1}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K})=V(\mathbf{x}^{\mathbf{r}},D_{k}\mathbf{x}^{\mathbf{r}},\dots,D_{k}^{j-1}\mathbf{x}^{\mathbf{r}})\subseteq\mathbb{A}^{k}_{\mathbb{K}}(\mathbb{K})\quad\forall j\leq n, |  |

by the induction hypothesis we have

 | V ⁡ ( 𝐱 𝐫, D k ​ 𝐱 𝐫, …, D k m − 1 ​ 𝐱 𝐫) = ⋃ l = 1 m ⋃ i 1 < i 2 < ⋯ < i l r i 1 + r i 2 + ⋯ + r i l ≥ m V ⁡ ( x i 1) ∩ V ⁡ ( x i 2) ∩ ⋯ ∩ V ⁡ ( x i l). V(\mathbf{x}^{\mathbf{r}},D_{k}\mathbf{x}^{\mathbf{r}},\dots,D_{k}^{m-1}\mathbf{x}^{\mathbf{r}})=\bigcup_{l=1}^{m}\bigcup_{\begin{subarray}{c}i_{1}<i_{2}<\cdots<i_{l}\\ r_{i_{1}}+r_{i_{2}}+\cdots+r_{i_{l}}\geq m\end{subarray}}V(x_{i_{1}})\cap V(x_{i_{2}})\cap\cdots\cap V(x_{i_{l}}). |  |

The above union can be stratified along the levels r i 1 + r i 2 + ⋯ + r i l = μ r_{i_{1}}+r_{i_{2}}+\cdots+r_{i_{l}}=\mu, where μ ≥ m \mu\geq m. That is V ⁡ ( 𝐱 𝐫, D k ​ 𝐱 𝐫, …, D k m − 1 ​ 𝐱 𝐫) = ⋃ μ = m n 𝒟 j − 1 ​ 𝒮 n ​ ( 𝐫) ​ [μ] ​ ( 𝕂) V(\mathbf{x}^{\mathbf{r}},D_{k}\mathbf{x}^{\mathbf{r}},\dots,D_{k}^{m-1}\mathbf{x}^{\mathbf{r}})=\bigcup_{\mu=m}^{n}\mathscr{D}^{j-1}\mathscr{S}_{n}(\mathbf{r})[\mu](\mathbb{K}), where

 | 𝒟 j − 1 ​ 𝒮 n ​ ( 𝐫) ​ [μ] ​ ( 𝕂):= ⋃ l = 1 m ⋃ i 1 < i 2 < ⋯ < i l r i 1 + r i 2 + ⋯ + r i l = μ V ⁡ ( x i 1) ∩ V ⁡ ( x i 2) ∩ ⋯ ∩ V ⁡ ( x i l). \mathscr{D}^{j-1}\mathscr{S}_{n}(\mathbf{r})[\mu](\mathbb{K}):=\bigcup_{l=1}^{m}\bigcup_{\begin{subarray}{c}i_{1}<i_{2}<\cdots<i_{l}\\ r_{i_{1}}+r_{i_{2}}+\cdots+r_{i_{l}}=\mu\end{subarray}}V(x_{i_{1}})\cap V(x_{i_{2}})\cap\cdots\cap V(x_{i_{l}}). |  |

By definition, any 𝕂 \mathbb{K} -rational point P ∈ 𝒟 m − 1 ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) P\in\mathscr{D}^{m-1}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) satisfies 𝐱 𝐫 ​ ( P) = D k ​ 𝐱 𝐫 ​ ( P) = ⋯ = D k m − 1 ​ 𝐱 𝐫 ​ ( P) = 0 \mathbf{x}^{\mathbf{r}}(P)=D_{k}\mathbf{x}^{\mathbf{r}}(P)=\cdots=D_{k}^{m-1}\mathbf{x}^{\mathbf{r}}(P)=0, and thus P ∈ 𝒟 m ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) P\in\mathscr{D}^{m}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) if and only if D k m ​ 𝐱 𝐫 ​ ( P) = 0 D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P)=0 as well. Recall that 𝐱 𝐫 = ∏ i = 1 k x i r i \mathbf{x}^{\mathbf{r}}=\prod_{i=1}^{k}x_{i}^{r_{i}} and thus, by induction one can see that

(3.2) |  | D k j 𝐱 𝐫 = ∑ β 1 + ⋯ + β k = j 0 ≤ β i ≤ r i c β 1, ⋯, β k x 1 r 1 − β 1 ⋯ x k r k − β k (with appropriate coefficients c β 1, …, β k) D_{k}^{j}\mathbf{x}^{\mathbf{r}}=\sum_{\begin{subarray}{c}\beta_{1}+\cdots+\beta_{k}=j\\ 0\leq\beta_{i}\leq r_{i}\end{subarray}}c_{\beta_{1},\cdots,\beta_{k}}x_{1}^{r_{1}-\beta_{1}}\cdots x_{k}^{r_{k}-\beta_{k}}\ \ \text{(with appropriate coefficients }c_{\beta_{1},\dots,\beta_{k}}) |  |

is a homogeneous degree n − j n-j polynomial in x i x_{i} with integer coefficients. We first prove that 𝒟 m − 1 ​ 𝒮 n ​ ( 𝐫) ​ [μ] ​ ( 𝕂) ⊆ 𝒟 m ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{D}^{m-1}\mathscr{S}_{n}(\mathbf{r})[\mu](\mathbb{K})\subseteq\mathscr{D}^{m}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) for any μ ≥ m + 1 \mu\geq m+1. Let P ∈ 𝒟 m − 1 ​ 𝒮 n ​ ( 𝐫) ​ [μ] ​ ( 𝕂) P\in\mathscr{D}^{m-1}\mathscr{S}_{n}(\mathbf{r})[\mu](\mathbb{K}) for any μ ≥ m + 1 \mu\geq m+1, so that there exist i 1 < ⋯ < i l i_{1}<\cdots<i_{l} for some 1 ≤ l ≤ m 1\leq l\leq m, such that P ∈ V ⁡ ( x i 1) ∩ ⋯ ∩ V ⁡ ( x i l) P\in V(x_{i_{1}})\cap\cdots\cap V(x_{i_{l}}) with multiplicities of V ⁡ ( x i j) V(x_{i_{j}}) equal to r i j r_{i_{j}} such that r i 1 + ⋯ + r i l = μ ≥ m + 1 r_{i_{1}}+\cdots+r_{i_{l}}=\mu\geq m+1. For this point P P, we rewrite D k m ​ 𝐱 𝐫 ​ ( P) D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P) by grouping the terms x i ​ ( P) r i − β i x_{i}(P)^{r_{i}-\beta_{i}} in each monomial x 1 ( P) r 1 − β 1 ⋯ x k ( P) r k − β k x_{1}(P)^{r_{1}-\beta_{1}}\cdots x_{k}(P)^{r_{k}-\beta_{k}} in D k m ​ 𝐱 𝐫 ​ ( P) D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P) according to whether the index i i of x i ​ ( P) r i − β i x_{i}(P)^{r_{i}-\beta_{i}} is equal to i j i_{j} for some j = 1, …, l j=1,\dots,l or not:

(3.3) |  | D k m ​ 𝐱 𝐫 ​ ( P) = ∑ β 1 + ⋯ + β k = m 0 ≤ β i ≤ r i c β 1, …, β k ​ ( ∏ j = 1 l x i j ​ ( P) r i j − β i j) ​ ( ∏ i ≠ i j x i ​ ( P) r i − β i). D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P)=\sum_{\begin{subarray}{c}\beta_{1}+\cdots+\beta_{k}=m\\ 0\leq\beta_{i}\leq r_{i}\end{subarray}}c_{\beta_{1},\dots,\beta_{k}}(\prod_{j=1}^{l}x_{i_{j}}(P)^{r_{i_{j}}-\beta_{i_{j}}})(\prod_{i\neq i_{j}}x_{i}(P)^{r_{i}-\beta_{i}}). |  |

By choice of P P, we have r i 1 + ⋯ + r i l = μ ≥ m + 1 r_{i_{1}}+\cdots+r_{i_{l}}=\mu\geq m+1, while β i 1 + ⋯ + β i l ≤ m \beta_{i_{1}}+\cdots+\beta_{i_{l}}\leq m. Hence, for each monomial occurring in the sum in ( 3.3), there is some 1 ≤ j ≤ l 1\leq j\leq l such that r i j − β i j ≥ 1 r_{i_{j}}-\beta_{i_{j}}\geq 1. Since P ∈ V ⁡ ( x i 1) ∩ ⋯ ∩ V ⁡ ( x i l) P\in V(x_{i_{1}})\cap\cdots\cap V(x_{i_{l}}), all monomials in D k m ​ 𝐱 𝐫 ​ ( P) D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P) vanish and so D k m ​ 𝐱 𝐫 ​ ( P) = 0 D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P)=0.

Now, for any point P ∈ 𝒟 m ​ 𝒮 n ​ ( 𝐫) ​ [m] ​ ( 𝕂) P\in\mathscr{D}^{m}\mathscr{S}_{n}(\mathbf{r})[m](\mathbb{K}), any monomial in the sum in ( 3.3) with β i ≥ 1 \beta_{i}\geq 1 for some i ≠ i 1, …, i l i\neq i_{1},\dots,i_{l} has a factor of x i j x_{i_{j}} for some 1 ≤ j ≤ l 1\leq j\leq l, so it vanishes at P P. Thus, the only non-vanishing monomials can come from those for which β i = 0 \beta_{i}=0 for all i ≠ i 1, …, i l i\neq i_{1},\dots,i_{l}. Furthermore, since 0 ≤ β i j ≤ r i j 0\leq\beta_{i_{j}}\leq r_{i_{j}} and ∑ i = 1 k β i = ∑ j = 1 l β i j = m = ∑ j = 1 l r i j \sum_{i=1}^{k}\beta_{i}=\sum_{j=1}^{l}\beta_{i_{j}}=m=\sum_{j=1}^{l}r_{i_{j}}, it follows that β i j = r i j \beta_{i_{j}}=r_{i_{j}} for all 1 ≤ j ≤ l 1\leq j\leq l. Hence the only possible non-zero monomial (up to a non-zero coefficient) is ∏ i ≠ i j x i ​ ( P) r i \prod_{i\neq i_{j}}x_{i}(P)^{r_{i}} and it follows that D k m ​ 𝐱 𝐫 ​ ( P) = 0 D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P)=0 if and only if there exists i ≠ i j i\neq i_{j} for which x i ​ ( P) = 0 x_{i}(P)=0. Consequently, D k m ​ 𝐱 𝐫 ​ ( P) = 0 D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P)=0 if and only if P ∈ ⋂ j = 1 l V ⁡ ( x i j) ∩ V ⁡ ( x i) P\in\bigcap_{j=1}^{l}V(x_{i_{j}})\cap V(x_{i}) for some i ≠ i j i\neq i_{j}, and thus r i + ∑ j = 1 l r i j ≥ m + 1 r_{i}+\sum_{j=1}^{l}r_{i_{j}}\geq m+1. Thus, we have obtained that

 | 𝒟 m ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) = ⋃ l = 1 m + 1 ⋃ i 1 < i 2 < ⋯ < i l r i 1 + r i 2 + ⋯ + r i l ≥ m + 1 V ⁡ ( x i 1) ∩ V ⁡ ( x i 2) ∩ ⋯ ∩ V ⁡ ( x i l). \mathscr{D}^{m}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K})=\bigcup_{l=1}^{m+1}\bigcup_{\begin{subarray}{c}i_{1}<i_{2}<\cdots<i_{l}\\ r_{i_{1}}+r_{i_{2}}+\cdots+r_{i_{l}}\geq m+1\end{subarray}}V(x_{i_{1}})\cap V(x_{i_{2}})\cap\cdots\cap V(x_{i_{l}}). |  |

This completes the inductive step and hence the proof. ∎

Since 𝒟 m ​ 𝒮 n ​ ( 𝐫) ​ ( 𝕂) = ⋂ i = 1 m V ⁡ ( 𝐱 𝐫, D k i ​ 𝐱 𝐫) \mathscr{D}^{m}\mathscr{S}_{n}(\mathbf{r})(\mathbb{K})=\bigcap_{i=1}^{m}V(\mathbf{x}^{\mathbf{r}},D^{i}_{k}\mathbf{x}^{\mathbf{r}}), by Proposition 3.11, for any 1 ≤ m ≤ n − 1 1\leq m\leq n-1, the affine algebraic set V ⁡ ( 𝐱 𝐫, D k m ​ 𝐱 𝐫) V(\mathbf{x}^{\mathbf{r}},D_{k}^{m}\mathbf{x}^{\mathbf{r}}) contains an entire irreducible component V ⁡ ( x j) V(x_{j}) of 𝒮 n ​ ( 𝐫) ​ ( 𝕂) \mathscr{S}_{n}(\mathbf{r})(\mathbb{K}) if V ⁡ ( x j) V(x_{j}) has multiplicity r j ≥ m + 1 r_{j}\geq m+1. The following lemma shows that the converse is true as well.

###### Lemma 3.12.

V ⁡ ( x j) ⊆ V ⁡ ( 𝐱 𝐫, D k m ​ 𝐱 𝐫) V(x_{j})\subseteq V(\mathbf{x}^{\mathbf{r}},D_{k}^{m}\mathbf{x}^{\mathbf{r}}) if and only if r j ≥ m + 1 r_{j}\geq m+1, for any 0 ≤ m ≤ n − 1 0\leq m\leq n-1.

###### Proof.

By the general Leibniz rule for self-composition of derivations, we have

 | D k m ​ 𝐱 𝐫 = D k m ​ ( ∏ i = 1 k x i r i) = ∑ l 1 + ⋯ + l k = m ( m l 1, …, l k) ​ ∏ 1 ≤ i ≤ k D k l i ​ ( x i r i) \displaystyle D_{k}^{m}\mathbf{x}^{\mathbf{r}}=D_{k}^{m}(\prod_{i=1}^{k}x_{i}^{r_{i}})=\sum_{l_{1}+\cdots+l_{k}=m}\binom{m}{l_{1},\dots,l_{k}}\prod_{1\leq i\leq k}D_{k}^{l_{i}}(x_{i}^{r_{i}}) |  |

 | = ∑ 0 ≤ l j ≤ m ( m l j) ​ D k l j ​ ( x j r j) ​ ∑ l 1 + ⋯ + l j ^ + ⋯ + l k = m − l j ( m − l j l 1, …, l j ^, …, l k) ​ ∏ i ≠ j D k l i ​ ( x i r i), \displaystyle=\sum_{0\leq l_{j}\leq m}\binom{m}{l_{j}}D_{k}^{l_{j}}(x_{j}^{r_{j}})\sum_{l_{1}+\cdots+\hat{l_{j}}+\cdots+l_{k}=m-l_{j}}\binom{m-l_{j}}{l_{1},\dots,\hat{l_{j}},\dots,l_{k}}\prod_{i\neq j}D_{k}^{l_{i}}(x_{i}^{r_{i}}), |  |

where l j ^ \hat{l_{j}} in the second line indicates that l j l_{j} is removed. Since V ⁡ ( x j) ⊆ V ⁡ ( 𝐱 𝐫) V(x_{j})\subseteq V(\mathbf{x}^{\mathbf{r}}), it suffices to show V ⁡ ( x j) ∩ V ⁡ ( D k m ​ 𝐱 𝐫) = V ⁡ ( x j) V(x_{j})\cap V(D^{m}_{k}\mathbf{x}^{\mathbf{r}})=V(x_{j}) if and only if r j ≥ m + 1 r_{j}\geq m+1. For P ∈ V ⁡ ( x j) ∩ V ⁡ ( D k m ​ 𝐱 𝐫) P\in V(x_{j})\cap V(D_{k}^{m}\mathbf{x}^{\mathbf{r}}), the terms with l j < r j l_{j}<r_{j} in the above expression for D k m ​ 𝐱 𝐫 D^{m}_{k}\mathbf{x}^{\mathbf{r}} vanish, when evaluated at P P. Furthermore, D k l j ​ ( x j r j) = 0 D^{l_{j}}_{k}(x_{j}^{r_{j}})=0 for all l j > r j l_{j}>r_{j}. Thus, the only remaining terms in D k m ​ 𝐱 𝐫 ​ ( P) D^{m}_{k}\mathbf{x}^{\mathbf{r}}(P) are exactly those with l j = r j l_{j}=r_{j}, so by the general Leibniz rule, D k m ​ 𝐱 𝐫 ​ ( P) = r j! ​ ( m r j) ​ D k m − r j ​ ( ∏ i ≠ j x i r i) ​ ( P) = 0 D_{k}^{m}\mathbf{x}^{\mathbf{r}}(P)=r_{j}!\binom{m}{r_{j}}D_{k}^{m-r_{j}}(\prod_{i\neq j}x_{i}^{r_{i}})(P)=0.

Note that V ⁡ ( x j) ⊆ V ⁡ ( D k m ​ 𝐱 𝐫) V(x_{j})\subseteq V(D_{k}^{m}\mathbf{x}^{\mathbf{r}}) if and only if the polynomial r j! ​ ( m r j) ​ D k m − r j ​ ( ∏ i ≠ j x i r i) r_{j}!\binom{m}{r_{j}}D_{k}^{m-r_{j}}(\prod_{i\neq j}x_{i}^{r_{i}}) in the k − 1 k-1 variables { x i ∣ i ≠ j } \{x_{i}\mid\ i\neq j\}, vanishes (identically) at all points of V ⁡ ( x j) ⊆ 𝔸 𝕂 k ​ ( 𝕂) V(x_{j})\subseteq\mathbb{A}^{k}_{\mathbb{K}}(\mathbb{K}), which is isomorphic to the affine k − 1 k-1 space 𝔸 𝕂 k − 1 ​ ( 𝕂) \mathbb{A}_{\mathbb{K}}^{k-1}(\mathbb{K}). It follows that the polynomial r j! ​ ( m r j) ​ D k m − r j ​ ( ∏ i ≠ j x i r i) r_{j}!\binom{m}{r_{j}}D_{k}^{m-r_{j}}(\prod_{i\neq j}x_{i}^{r_{i}}) in k − 1 k-1 variables must be identically 0 0. This is true if and only if r j ≥ m + 1 r_{j}\geq m+1, as D k m − r j ​ ( ∏ i ≠ j x i r i) D_{k}^{m-r_{j}}(\prod_{i\neq j}x_{i}^{r_{i}}) is a non-zero polynomial in k − 1 k-1 variables, because r 1 + ⋯ + r j ^ + ⋯ + r k = n − r j > m − r j r_{1}+\cdots+\hat{r_{j}}+\cdots+r_{k}=n-r_{j}>m-r_{j}. ∎

## 4. Geometry of higher discriminants

Throughout this section 𝕂 \mathbb{K} will denote an algebraically closed field of arbitrary characteristic.

### 4.1. Geometry of monic univariate polynomials of degree n n

For any positive integer n n, let 𝕂 ​ [X] n \mathbb{K}[X]_{n} be the set of degree n n monic univariate polynomials over 𝕂 \mathbb{K}. We introduce certain constructions on 𝕂 ⁡ [X] \mathbb{K}[X], and 𝕂 ​ [X] n \mathbb{K}[X]_{n} in particular, which will be useful in understanding Conjecture CA.

###### Definition 4.1 (Shift equivalence).

Define the equivalence relation ∼ \sim on the monic polynomials of the polynomial ring 𝕂 ⁡ [X] \mathbb{K}[X] as f ⁡ ( X) ∼ g ⁡ ( X) f(X)\sim g(X) in 𝕂 ⁡ [X] \mathbb{K}[X] if g ⁡ ( X) = f ⁡ ( X − β) g(X)=f(X-\beta) for some β ∈ 𝕂 \beta\in\mathbb{K}. We say f ⁡ ( X) f(X) and g ⁡ ( X) g(X) are shift equivalent if f ⁡ ( X) ∼ g ⁡ ( X) f(X)\sim g(X). We will denote the shift equivalence class of f ⁡ ( X) f(X) by [f ⁡ ( X)] [f(X)] and the set of shift equivalence classes of monic polynomials by [𝕂 ⁡ [X]] [\mathbb{K}[X]].

The shift equivalence class [f ⁡ ( X)] [f(X)] of the monic polynomial f ⁡ ( X) ∈ 𝕂 ⁡ [X] f(X)\in\mathbb{K}[X] consists of those monic polynomials g ⁡ ( X) g(X), whose roots are exactly the roots of f ⁡ ( X) f(X) up to translation – in other words, the relative location of the roots of g ⁡ ( X) g(X) are same as those of f ⁡ ( X) f(X). In particular, shift equivalence restricts to a well-defined equivalence relation on 𝕂 ​ [X] n \mathbb{K}[X]_{n}, whose equivalence classes will be denoted by [𝕂 ​ [X] n] [\mathbb{K}[X]_{n}]. Notice, if f ⁡ ( X) f(X) satisfies the hypothesis of Conjecture CA, then so does any g ⁡ ( X) ∈ [f ⁡ ( X)] g(X)\in[f(X)]. The following definition is crucial in lifting Conjecture CA, which is a problem in one variable, to a problem about linear algebraic subvarieties of higher dimensional affine spaces.

###### Definition 4.2 (Characteristic maps).

For any monic f ⁡ ( X) ∈ 𝕂 ⁡ [X] f(X)\in\mathbb{K}[X] of degree n n (i.e., f ⁡ ( X) ∈ 𝕂 ​ [X] n f(X)\in\mathbb{K}[X]_{n}) along with a fixed labelling α ¯ = ( α 1, …, α n) \overline{\alpha}=(\alpha_{1},\dots,\alpha_{n}) of roots, we define the α ¯ \overline{\alpha} -characteristic map of f ⁡ ( X) f(X) to be the 𝕂 \mathbb{K} -algebra map ℭ f, α ¯: 𝕂 ⁡ [x 1, …, x n] → 𝕂 ⁡ [X] \mathfrak{C}_{f,\overline{\alpha}}:\mathbb{K}[x_{1},\dots,x_{n}]\rightarrow\mathbb{K}[X] defined by x i ↦ X − α i x_{i}\mapsto X-\alpha_{i} for all 1 ≤ i ≤ n 1\leq i\leq n. Consequently, define the set of characteristic maps of f ⁡ ( X) f(X) to be the set ℭ ⁡ ( f):= { ℭ f, α ¯ ∣ α ¯ ∈ ℜ ⁡ ( f) } \mathfrak{C}(f):=\{\mathfrak{C}_{f,\overline{\alpha}}\mid\ \overline{\alpha}\in\mathfrak{R}(f)\}, where ℜ ⁡ ( f) \mathfrak{R}(f) is the set of all ordered tuples α ¯ = ( α 1, …, α n) \overline{\alpha}=(\alpha_{1},\dots,\alpha_{n}) obtained by permuting the roots of f f.

Note that for each 1 ≤ i ≤ n 1\leq i\leq n and α ¯ ∈ ℜ ⁡ ( f) \overline{\alpha}\in\mathfrak{R}(f), ker ⁡ ℭ f, α ¯ \ker\mathfrak{C}_{f,\overline{\alpha}} has a “base i i ” presentation, given by ker ⁡ ℭ f, α ¯ = ( { x j − x i + γ j ​ i ∣ 1 ≤ j ≤ n }) ⊆ 𝕂 ⁡ [x 1, …, x n] \ker\mathfrak{C}_{f,\overline{\alpha}}=(\{x_{j}-x_{i}+\gamma_{ji}\mid\ 1\leq j\leq n\})\subseteq\mathbb{K}[x_{1},\dots,x_{n}], where γ j ​ i = α j − α i \gamma_{ji}=\alpha_{j}-\alpha_{i}. Geometrically the α ¯ \overline{\alpha} -characteristic map ℭ f, α ¯ \mathfrak{C}_{f,\overline{\alpha}} induces a closed embedding ℭ f, α ¯ #: 𝔸 𝕂 1 ↪ 𝔸 𝕂 n \mathfrak{C}_{f,\overline{\alpha}}^{\#}:\mathbb{A}^{1}_{\mathbb{K}}\hookrightarrow\mathbb{A}^{n}_{\mathbb{K}} as the closed subscheme ℒ f, α ¯:= Spec ⁡ ( 𝕂 ⁡ [x 1, …, x n] / ker ⁡ ℭ f, α ¯) ⊆ 𝔸 𝕂 n \mathscr{L}_{f,\overline{\alpha}}:=\spec(\mathbb{K}[x_{1},\dots,x_{n}]/\ker\mathfrak{C}_{f,\overline{\alpha}})\subseteq\mathbb{A}^{n}_{\mathbb{K}}. Considering the “base 1 1 ” presentation of ker ⁡ ℭ f, α ¯ \ker\mathfrak{C}_{f,\overline{\alpha}}, the set of 𝕂 \mathbb{K} -rational points of ℒ f, α ¯ \mathscr{L}_{f,\overline{\alpha}} is

 | ℒ f, α ¯ ​ ( 𝕂) = V ⁡ ( ker ⁡ ℭ f, α ¯) = { ( β, β + γ 12, β + γ 13, …, β + γ 1 ​ n) ∣ β ∈ 𝕂 } ⊆ 𝔸 𝕂 n ​ ( 𝕂). \mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})=V(\ker\mathfrak{C}_{f,\overline{\alpha}})=\{(\beta,\beta+\gamma_{12},\beta+\gamma_{13},\dots,\beta+\gamma_{1n})\mid\ \beta\in\mathbb{K}\}\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}). |  |

Thus, we can identify ℒ f, α ¯ ​ ( 𝕂) \mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) with the shift equivalence class [f ⁡ ( X)] [f(X)] by the association

 | ( β, β + γ 12, β + γ 13, …, β + γ 1 ​ n) ↦ ∏ j = 1 n ( X + β + γ 1 ​ j) = f ⁡ ( X + β + α 1). (\beta,\beta+\gamma_{12},\beta+\gamma_{13},\dots,\beta+\gamma_{1n})\mapsto\prod_{j=1}^{n}(X+\beta+\gamma_{1j})=f(X+\beta+\alpha_{1}). |  |

Consequently, the subscheme ℒ f, α ¯ ⊆ 𝔸 𝕂 n \mathscr{L}_{f,\overline{\alpha}}\subseteq\mathbb{A}^{n}_{\mathbb{K}} depends only on the shift equivalence class [f ⁡ ( X)] [f(X)] of f ⁡ ( X) f(X). For each monic f ⁡ ( X) ∈ 𝕂 ⁡ [X] f(X)\in\mathbb{K}[X] of degree n n, we therefore obtain the set 𝔏 ⁡ ( f):= { ℒ f, α ¯, α ¯ ∈ ℜ ⁡ ( f) } \mathfrak{L}(f):=\{\mathscr{L}_{f,\overline{\alpha}},\ \overline{\alpha}\in\mathfrak{R}(f)\} of affine lines in 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}, which only depends on the shift equivalence class [f ⁡ ( X)] [f(X)]. Furthermore, the action of the symmetric group 𝔖 n \mathfrak{S}_{n} on 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}} via permuting the variables of 𝕂 ⁡ [x 1, …, x n] \mathbb{K}[x_{1},\dots,x_{n}], induces a transitive action on 𝔏 ⁡ ( f) \mathfrak{L}(f), so that the affine lines in 𝔏 ⁡ ( f) \mathfrak{L}(f) differ only by a permutation.

In what follows, let f ⁡ ( X) = ∏ i = 1 n ( X − α i) ∈ 𝕂 ⁡ [X] f(X)=\prod_{i=1}^{n}(X-\alpha_{i})\in\mathbb{K}[X] be a monic polynomial of degree n ≥ 2 n\geq 2 with a fixed ordering of roots α ¯ = ( α 1, …, α n) ∈ ℜ ⁡ ( f) \overline{\alpha}=(\alpha_{1},\dots,\alpha_{n})\in\mathfrak{R}(f). Let 𝐱 n:= ∏ i = 1 n x i ∈ 𝕂 ⁡ [x 1, …, x n] \mathbf{x}_{n}:=\prod_{i=1}^{n}x_{i}\in\mathbb{K}[x_{1},\dots,x_{n}] be the unique elementary symmetric monomial in n n variables. The following lemma will allow us to transfer conditions on the derivatives of f ⁡ ( X) f(X) in 𝕂 ⁡ [X] \mathbb{K}[X] to appropriate conditions on transformations of (Hasse-Schmidt) D-subschemes of the monomial affine 𝕂 \mathbb{K} -scheme Spec ⁡ ( 𝕂 ⁡ [x 1, …, x n] / ( 𝐱 n)) \spec(\mathbb{K}[x_{1},\dots,x_{n}]/(\mathbf{x}_{n})).

###### Lemma 4.3.

Let H ​ D n i: 𝕂 ⁡ [x 1, …, x n] → 𝕂 ⁡ [x 1, …, x n] HD^{i}_{n}:\mathbb{K}[x_{1},\dots,x_{n}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n}] be the i t ​ h i^{th} multivariate Hasse-Schmidt derivation defined by ( 2.1) and let H i: 𝕂 ⁡ [X] → 𝕂 ⁡ [X] H_{i}:\mathbb{K}[X]\rightarrow\mathbb{K}[X] be the i t ​ h i^{th} univariate Hasse-Schmidt derivation. Then, for all i ≥ 1 i\geq 1 and for any monic polynomial f ⁡ ( X) = ∏ i = 1 n ( X − α i) ∈ 𝕂 ⁡ [X] f(X)=\prod_{i=1}^{n}(X-\alpha_{i})\in\mathbb{K}[X] with a fixed ordering α ¯ = ( α 1, …, α n) \overline{\alpha}=(\alpha_{1},\dots,\alpha_{n}) of roots, the following diagram commutes:

 | 𝕂 ⁡ [x 1, …, x n] {\lx@inpgf@ignorespaces\mathbb{K}[x_{1},\dots,x_{n}]} 𝕂 ⁡ [x 1, …, x n] {\lx@inpgf@ignorespaces\mathbb{K}[x_{1},\dots,x_{n}]} 𝕂 ⁡ [X] {\lx@inpgf@ignorespaces\mathbb{K}[X]} 𝕂 ⁡ [X] {\lx@inpgf@ignorespaces\mathbb{K}[X]} ℭ f, α ¯ \scriptstyle{\lx@inpgf@ignorespaces\mathfrak{C}_{f,\overline{\alpha}}} H ​ D n i \scriptstyle{\lx@inpgf@ignorespaces HD^{i}_{n}} ℭ f, α ¯ \scriptstyle{\lx@inpgf@ignorespaces\mathfrak{C}_{f,\overline{\alpha}}} H i \scriptstyle{\lx@inpgf@ignorespaces H_{i}} |  |

###### Proof.

It suffices to check that the diagram commutes for any monomial in 𝕂 ⁡ [x 1, …, x n] \mathbb{K}[x_{1},\dots,x_{n}] as all the arrows are 𝕂 \mathbb{K} -linear. Let x 1 β 1 ​ x 2 β 2 ​ … ​ x n β n ∈ 𝕂 ⁡ [x 1, …, x n] x_{1}^{\beta_{1}}x_{2}^{\beta_{2}}\dots x_{n}^{\beta_{n}}\in\mathbb{K}[x_{1},\dots,x_{n}], whereby using ( 2.1) we have

 | ℭ f, α ¯ ​ ( H ​ D n i ​ ( x 1 β 1 ​ … ​ x n β n)) = ∑ j 1 + ⋯ + j n = i ( β 1 j 1) ​ … ​ ( β n j n) ​ ( X − α 1) β 1 − j 1 ​ … ​ ( X − α n) β n − j n. \mathfrak{C}_{f,\overline{\alpha}}(HD^{i}_{n}(x_{1}^{\beta_{1}}\dots x_{n}^{\beta_{n}}))=\sum_{j_{1}+\dots+j_{n}=i}{\beta_{1}\choose j_{1}}\dots{\beta_{n}\choose j_{n}}(X-\alpha_{1})^{\beta_{1}-j_{1}}\dots(X-\alpha_{n})^{\beta_{n}-j_{n}}. |  |

Similarly, using Leibniz rule for the univariate Hasse-Schmidt derivations, we have

 | H i ​ ( ℭ f, α ¯ ​ ( x 1 β 1 ​ … ​ x n β n)) = H i ​ ( ( X − α 1) β 1 ​ … ​ ( X − α n) β n) \displaystyle H_{i}(\mathfrak{C}_{f,\overline{\alpha}}(x_{1}^{\beta_{1}}\dots x_{n}^{\beta_{n}}))=H_{i}((X-\alpha_{1})^{\beta_{1}}\dots(X-\alpha_{n})^{\beta_{n}}) |  |

 | = ∑ j 1 + ⋯ + j n = i H j 1 ​ ( ( X − α 1) β 1) ​ … ​ H j n ​ ( ( X − α n) β n), \displaystyle=\sum_{j_{1}+\dots+j_{n}=i}H_{j_{1}}((X-\alpha_{1})^{\beta_{1}})\dots H_{j_{n}}((X-\alpha_{n})^{\beta_{n}}), |  |

which equals ℭ f, α ¯ ​ ( H ​ D n i ​ ( x 1 β 1 ​ … ​ x n β n)) \mathfrak{C}_{f,\overline{\alpha}}(HD^{i}_{n}(x_{1}^{\beta_{1}}\dots x_{n}^{\beta_{n}})) by using the fact that H i ​ ( ( X − α) n) = ( n i) ​ ( X − α) n − i H_{i}((X-\alpha)^{n})={n\choose i}(X-\alpha)^{n-i}. ∎

The set 𝕂 ​ [X] n \mathbb{K}[X]_{n} can be naturally identified with 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}} via a 0 + a 1 ​ X + ⋯ + a n − 1 ​ X n − 1 + X n ↦ ( a 0, a 1, …, a n − 1) a_{0}+a_{1}X+\dots+a_{n-1}X^{n-1}+X^{n}\mapsto(a_{0},a_{1},\dots,a_{n-1}). This equips 𝕂 ​ [X] n \mathbb{K}[X]_{n} with a variety structure. When n n is coprime to the characteristic of 𝕂 \mathbb{K}, the set 𝕂 ​ [X] n \mathbb{K}[X]_{n} can further be naturally identified with a GIT quotient. For this, we introduce the following map.

###### Definition 4.4 (Root map).

We define the degree n n root map to be the set map ρ n: 𝔸 𝕂 n ​ ( 𝕂) → 𝕂 ​ [X] n \rho_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow\mathbb{K}[X]_{n} sending ( α 1, α 2, …, α n) (\alpha_{1},\alpha_{2},\dots,\alpha_{n}) to the degree n n polynomial ∏ i = 1 n ( X + α i) \prod_{i=1}^{n}(X+\alpha_{i}).

###### Remark 4.5.

1.
2. (i)

Assume char ⁡ ( 𝕂) \operatorname{char}(\mathbb{K}) and n n are coprime. Let 𝔖 n \mathfrak{S}_{n} act on 𝔸 𝕂 n ​ ( 𝕂) \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) by permutation of coordinates. Then, by the definition of ρ n: 𝔸 𝕂 n ​ ( 𝕂) → 𝕂 ​ [X] n \rho_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow\mathbb{K}[X]_{n}, the fibers of ρ n \rho_{n} are the 𝔖 n \mathfrak{S}_{n} -orbits of 𝔸 𝕂 n ​ ( 𝕂) \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}). Thus, ρ n \rho_{n} induces a set bijection ρ n ¯: 𝔸 𝕂 n ​ ( 𝕂) ⫽ 𝔖 n → ∼ 𝕂 ​ [X] n \overline{\rho_{n}}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\sslash\mathfrak{S}_{n}\xrightarrow{\sim}\mathbb{K}[X]_{n}, where 𝔸 𝕂 n ​ ( 𝕂) ⫽ 𝔖 n \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\sslash\mathfrak{S}_{n} is the set of 𝕂 \mathbb{K} -rational points of the GIT quotient 𝔸 𝕂 n ⫽ 𝔖 n:= Spec ⁡ ( 𝕂 ​ [x 1, …, x n] 𝔖 n) \mathbb{A}^{n}_{\mathbb{K}}\sslash\mathfrak{S}_{n}:=\spec(\mathbb{K}[x_{1},\dots,x_{n}]^{\mathfrak{S}_{n}}). Furthermore, since ρ n \rho_{n} can be identified with the quotient map 𝔸 𝕂 n ​ ( 𝕂) → 𝔸 𝕂 n ​ ( 𝕂) ⫽ 𝔖 n \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\sslash\mathfrak{S}_{n}, it follows that ρ n \rho_{n} is a finite morphism.

3. (ii)

Let q S: 𝕂 ​ [X] n → [𝕂 ​ [X] n] q_{S}:\mathbb{K}[X]_{n}\rightarrow[\mathbb{K}[X]_{n}] be the map sending a degree n n monic polynomial f ⁡ ( X) ∈ 𝕂 ​ [X] n f(X)\in\mathbb{K}[X]_{n} to its shift equivalence class [f ⁡ ( X)] ∈ [𝕂 ​ [X] n] [f(X)]\in[\mathbb{K}[X]_{n}]. The fibers of the composite map 𝔸 𝕂 n ​ ( 𝕂) → ρ n 𝕂 ​ [X] n → q S [𝕂 ​ [X] n] \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\xrightarrow{\rho_{n}}\mathbb{K}[X]_{n}\xrightarrow{q_{S}}[\mathbb{K}[X]_{n}] are exactly ( q S ∘ ρ n) − 1 ​ ( [f]) = ⋃ α ¯ ∈ ℜ ⁡ ( f) ℒ f, α ¯ ​ ( 𝕂) (q_{S}\circ\rho_{n})^{-1}([f])=\bigcup_{\overline{\alpha}\in\mathfrak{R}(f)}\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}). Thus, ρ n \rho_{n} formalizes the correspondence between points of ℒ f, α ¯ ​ ( 𝕂) \mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) (for any α ¯ ∈ ℜ ⁡ ( f) \overline{\alpha}\in\mathfrak{R}(f)) and the elements of the shift equivalence class [f ⁡ ( X)] [f(X)] described previously.

### 4.2. Higher discriminant hypersurfaces

The goal of this subsection is to construct and describe higher discriminant hypersurfaces in 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}, motivating their relevance to Conjecture CA.

Let f ⁡ ( X) = ∏ i = 1 n ( X − α i) ∈ 𝕂 ​ [X] n f(X)=\prod_{i=1}^{n}(X-\alpha_{i})\in\mathbb{K}[X]_{n} be a generic monic univariate polynomial of degree n n with an ordering of roots α ¯ = ( α 1, …, α n) \overline{\alpha}=(\alpha_{1},\dots,\alpha_{n}) and let f i:= H i ​ ( f) f_{i}:=H_{i}(f) be its i t ​ h i^{th} Hasse-Schmidt derivative. For each 1 ≤ i ≤ n − 1 1\leq i\leq n-1, the hypothesis gcd ⁡ ( f, f i) ≠ 1 \gcd(f,f_{i})\neq 1 is equivalent to the existence of 1 ≤ j i ≤ n 1\leq j_{i}\leq n such that we have the ideal containment ( f, f i) ⊆ ( X − α j i) ⊆ 𝕂 ⁡ [X] (f,f_{i})\subseteq(X-\alpha_{j_{i}})\subseteq\mathbb{K}[X]. By Lemma 4.3, since ℭ f, α ¯ ​ ( 𝐱 n) = f ⁡ ( X) \mathfrak{C}_{f,\overline{\alpha}}(\mathbf{x}_{n})=f(X) and ℭ f, α ¯ ​ ( H ​ D n i ​ 𝐱 n) = f i ​ ( X) \mathfrak{C}_{f,\overline{\alpha}}(HD_{n}^{i}\mathbf{x}_{n})=f_{i}(X) for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1, by applying ℭ f, α ¯ − 1 \mathfrak{C}_{f,\overline{\alpha}}^{-1} to the above ideal containment in 𝕂 ⁡ [X] \mathbb{K}[X], we obtain

(4.1) |  | ( 𝐱 n, H ​ D n i ​ 𝐱 n, ker ⁡ ℭ f, α ¯) ⊆ ( x j i, ker ⁡ ℭ f, α ¯) ⊆ 𝕂 ⁡ [x 1, …, x n]. (\mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n},\ker\mathfrak{C}_{f,\overline{\alpha}})\subseteq(x_{j_{i}},\ker\mathfrak{C}_{f,\overline{\alpha}})\subseteq\mathbb{K}[x_{1},\dots,x_{n}]. |  |

Now we note that 𝕂 ⁡ [x 1, …, x n] / ( x i, ker ⁡ ℭ f, α ¯) ≅ 𝕂 ⁡ [X] / ( X − α i) ≅ 𝕂 \mathbb{K}[x_{1},\dots,x_{n}]/(x_{i},\ker\mathfrak{C}_{f,\overline{\alpha}})\cong\mathbb{K}[X]/(X-\alpha_{i})\cong\mathbb{K}, whence ( x i, ker ⁡ ℭ f, α ¯) ⊆ 𝕂 ⁡ [x 1, …, x n] (x_{i},\ker\mathfrak{C}_{f,\overline{\alpha}})\subseteq\mathbb{K}[x_{1},\dots,x_{n}] are maximal ideals for all 1 ≤ i ≤ n 1\leq i\leq n. Thus, ( 4.1) is equivalent to the containment V ⁡ ( x j i) ∩ ℒ f, α ¯ ​ ( 𝕂) ⊆ V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ∩ ℒ f, α ¯ ​ ( 𝕂) ⊆ 𝔸 𝕂 n ​ ( 𝕂) V(x_{j_{i}})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})\subseteq V(\mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) which is, furthermore, equivalent to the condition V ⁡ ( x j i) ∩ V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ∩ ℒ f, α ¯ ​ ( 𝕂) ≠ ∅ V(x_{j_{i}})\cap V(\mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})\neq\emptyset, since V ⁡ ( x j i) ∩ ℒ f, α ¯ ​ ( 𝕂) V(x_{j_{i}})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) is a singleton. Since gcd ⁡ ( f, f i) ≠ 1 \gcd(f,f_{i})\neq 1 is equivalent to the existence of an index 1 ≤ j i ≤ n 1\leq j_{i}\leq n for which the intersection V ⁡ ( x j i) ∩ V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ∩ ℒ f, α ¯ ​ ( 𝕂) V(x_{j_{i}})\cap V(\mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) is non-empty, by noting that V ⁡ ( 𝐱 n) = ⋃ j = 1 n V ⁡ ( x j) V(\mathbf{x}_{n})=\bigcup_{j=1}^{n}V(x_{j}), we obtain

(4.2) |  | gcd ⁡ ( f, f i) ≠ 1 ⇔ V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ∩ ℒ f, α ¯ ​ ( 𝕂) ≠ ∅. \gcd(f,f_{i})\neq 1\iff V(\mathbf{x}_{n},HD_{n}^{i}\mathbf{x}_{n})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})\neq\emptyset. |  |

Note that the non-emptiness of V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ∩ ℒ f, α ¯ ​ ( 𝕂) V(\mathbf{x}_{n},HD_{n}^{i}\mathbf{x}_{n})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) is independent of the choice of ordering of roots α ¯ ∈ ℜ ⁡ ( f) \overline{\alpha}\in\mathfrak{R}(f). This is because 𝔖 n \mathfrak{S}_{n} acts transitively on 𝔏 ⁡ ( f) = { ℒ f, α ¯, α ¯ ∈ ℜ ⁡ ( f) } \mathfrak{L}(f)=\{\mathscr{L}_{f,\overline{\alpha}},\ \overline{\alpha}\in\mathfrak{R}(f)\} and 𝐱 n, H ​ D n i ​ 𝐱 n ∈ 𝕂 ​ [x 1, …, x n] 𝔖 n \mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n}\in\mathbb{K}[x_{1},\dots,x_{n}]^{\mathfrak{S}_{n}}, making V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) V(\mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n}) 𝔖 n \mathfrak{S}_{n} -invariant for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1. In fact, note that for all 0 ≤ i ≤ n − 1 0\leq i\leq n-1, we have H ​ D n i ​ 𝐱 n = e n − i ​ ( x 1, …, x n) HD^{i}_{n}\mathbf{x}_{n}=e_{n-i}(x_{1},\dots,x_{n}), the degree n − i n-i elementary symmetric polynomial in n n variables.

###### Remark 4.6.

We describe the affine algebraic subsets V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ⊆ 𝔸 𝕂 n ​ ( 𝕂) V(\mathbf{x}_{n},HD_{n}^{i}\mathbf{x}_{n})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) appearing in ( 4.2). Let 𝐱 n − 1 j:= ∏ l ≠ j x l \mathbf{x}_{n-1}^{j}:=\prod_{l\neq j}x_{l} and note that V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) = ⋃ j = 1 n V ⁡ ( x j, H ​ D n i ​ 𝐱 n) V(\mathbf{x}_{n},HD_{n}^{i}\mathbf{x}_{n})=\bigcup_{j=1}^{n}V(x_{j},HD_{n}^{i}\mathbf{x}_{n}). Since 𝐱 n = x j ⋅ 𝐱 n − 1 j \mathbf{x}_{n}=x_{j}\cdot\mathbf{x}^{j}_{n-1}, it follows by the Leibniz rule for Hasse-Schmidt derivations, that

 | H ​ D n i ​ 𝐱 n = x j ​ H ​ D n i ​ 𝐱 n − 1 j + H ​ D n i − 1 ​ 𝐱 n − 1 j = x j ​ H ​ D n − 1, j i ​ 𝐱 n − 1 j + H ​ D n − 1, j i − 1 ​ 𝐱 n − 1 j, HD_{n}^{i}\mathbf{x}_{n}=x_{j}HD^{i}_{n}\mathbf{x}^{j}_{n-1}+HD_{n}^{i-1}\mathbf{x}^{j}_{n-1}=x_{j}HD^{i}_{n-1,j}\mathbf{x}^{j}_{n-1}+HD_{n-1,j}^{i-1}\mathbf{x}^{j}_{n-1}, |  |

where H ​ D n − 1, j i: 𝕂 ⁡ [x 1, …, x j ^, …, x n] → 𝕂 ⁡ [x 1, …, x j ^, …, x n] HD^{i}_{n-1,j}:\mathbb{K}[x_{1},\dots,\hat{x_{j}},\dots,x_{n}]\rightarrow\mathbb{K}[x_{1},\dots,\hat{x_{j}},\dots,x_{n}] is the natural Hasse-Schmidt derivation obtained by restricting H ​ D n i HD^{i}_{n} on 𝕂 ⁡ [x 1, …, x n] \mathbb{K}[x_{1},\dots,x_{n}] to 𝕂 ⁡ [x 1, …, x j ^, …, x n] \mathbb{K}[x_{1},\dots,\hat{x_{j}},\dots,x_{n}]. Consequently, we obtain V ⁡ ( x j, H ​ D n i ​ 𝐱 n) = V ⁡ ( x j, H ​ D n − 1, j i − 1 ​ 𝐱 n − 1 j) ⊆ 𝔸 𝕂 n ​ ( 𝕂) V(x_{j},HD^{i}_{n}\mathbf{x}_{n})=V(x_{j},HD^{i-1}_{n-1,j}\mathbf{x}_{n-1}^{j})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}). In other words, consider V ⁡ ( H ​ D n − 1, j i − 1 ​ 𝐱 n − 1 j) ⊆ Z n j ​ ( 𝕂) = 𝔸 𝕂 n − 1 ​ ( 𝕂) V(HD^{i-1}_{n-1,j}\mathbf{x}_{n-1}^{j})\subseteq Z^{j}_{n}(\mathbb{K})=\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}), where Z n j = Spec ⁡ ( 𝕂 ⁡ [x 1, …, x j, …, x n] / ( x j)) Z^{j}_{n}=\spec(\mathbb{K}[x_{1},\dots,x_{j},\dots,x_{n}]/(x_{j})). Then V ⁡ ( x j, H ​ D n i ​ 𝐱 n) V(x_{j},HD_{n}^{i}\mathbf{x}_{n}) is the image (henceforth denoted by V n − 1 j ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) V^{j}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})) of V ⁡ ( H ​ D n − 1, j i − 1 ​ 𝐱 n − 1 j) ⊆ Z n j ​ ( 𝕂) V(HD^{i-1}_{n-1,j}\mathbf{x}_{n-1}^{j})\subseteq Z^{j}_{n}(\mathbb{K}) in 𝔸 𝕂 n ​ ( 𝕂) \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) under the natural inclusion Z n j ↪ 𝔸 𝕂 n Z^{j}_{n}\hookrightarrow\mathbb{A}^{n}_{\mathbb{K}} as a closed subscheme. Thus,

(4.3) |  | V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) = ⋃ j = 1 n V n − 1 j ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1). V(\mathbf{x}_{n},HD^{i}_{n}\mathbf{x}_{n})=\bigcup_{j=1}^{n}V^{j}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}). |  |

###### Definition 4.7 (Shift projection maps).

For all 1 ≤ j ≤ n 1\leq j\leq n, let Z n j ​ ( 𝕂) Z^{j}_{n}(\mathbb{K}) be the coordinate hyperplane of 𝔸 𝕂 n ​ ( 𝕂) \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) corresponding to x j = 0 x_{j}=0. Define the j t ​ h j^{th} shift projection map to be the map 𝔭 n j: 𝔸 𝕂 n ​ ( 𝕂) → Z n j ​ ( 𝕂) \mathfrak{p}^{j}_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow Z^{j}_{n}(\mathbb{K}) which sends ( x 1, …, x j, …, x n) (x_{1},\dots,x_{j},\dots,x_{n}) to ( x 1 − x j, …, x j − x j, …, x n − x j) (x_{1}-x_{j},\dots,x_{j}-x_{j},\dots,x_{n}-x_{j}).

The utility of shift projection maps is in the following observation. By ( 4.2), we are interested in the non-emptiness of V ⁡ ( 𝐱 n, H ​ D n i ​ 𝐱 n) ∩ ℒ f, α ¯ ​ ( 𝕂) V(\mathbf{x}_{n},HD_{n}^{i}\mathbf{x}_{n})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) which, by ( 4.3), is equivalent to the non-emptiness of V n − 1 j ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) ∩ ℒ f, α ¯ ​ ( 𝕂) V^{j}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) for some 1 ≤ j ≤ n 1\leq j\leq n. If 𝐲 = ( y 1, …, 0, …, y n) ∈ V n − 1 j ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) ∩ ℒ f, α ¯ ​ ( 𝕂) \mathbf{y}=(y_{1},\dots,0,\dots,y_{n})\in V^{j}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})\cap\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K}) (where 0 0 is at the j t ​ h j^{th} coordinate), then

 | ℒ f, α ¯ ​ ( 𝕂) = { ( β + y 1, …, β, …, β + y n) ∣ β ∈ 𝕂 } = ( 𝔭 n j) − 1 ​ ( 𝐲). \mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})=\{(\beta+y_{1},\dots,\beta,\dots,\beta+y_{n})\mid\ \beta\in\mathbb{K}\}=(\mathfrak{p}^{j}_{n})^{-1}(\mathbf{y}). |  |

Thus, ( 4.2) is equivalent to

(4.4) |  | gcd ( f, f i) ≠ 1 ⇔ ℒ f, α ¯ ( 𝕂) ⊆ X n i ( 𝕂):= ⋃ j = 1 n ( 𝔭 n j) − 1 ( V n − 1 j ( H D n − 1 i − 1 𝐱 n − 1)). \gcd(f,f_{i})\neq 1\quad\iff\quad\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})\subseteq X^{i}_{n}(\mathbb{K}):=\bigcup_{j=1}^{n}(\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})). |  |

The equivalence ( 4.4) can be formalized using the root map ρ n: 𝔸 𝕂 n ​ ( 𝕂) → 𝕂 ​ [X] n \rho_{n}:\mathbb{A}_{\mathbb{K}}^{n}(\mathbb{K})\rightarrow\mathbb{K}[X]_{n} as follows.

###### Lemma 4.8.

Let 𝔛 n i ​ ( 𝕂):= { f ⁡ ( X) ∈ 𝕂 ​ [X] n ∣ gcd ⁡ ( f, f i) ≠ 1 } ⊆ 𝕂 ​ [X] n \mathfrak{X}^{i}_{n}(\mathbb{K}):=\{f(X)\in\mathbb{K}[X]_{n}\mid\gcd(f,f_{i})\neq 1\}\subseteq\mathbb{K}[X]_{n} and let X n i ​ ( 𝕂) = ⋃ j = 1 n ( 𝔭 n j) − 1 ​ ( V n − 1 j ​ ( D n − 1 i − 1 ​ 𝐱 n − 1)) ⊆ 𝔸 𝕂 n ​ ( 𝕂) X^{i}_{n}(\mathbb{K})=\bigcup_{j=1}^{n}(\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(D^{i-1}_{n-1}\mathbf{x}_{n-1}))\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}). Then ρ n − 1 ​ ( 𝔛 n i ​ ( 𝕂)) = X n i ​ ( 𝕂) \rho_{n}^{-1}(\mathfrak{X}^{i}_{n}(\mathbb{K}))=X^{i}_{n}(\mathbb{K}).

###### Proof.

By ( 4.4), f ∈ 𝔛 n i ​ ( 𝕂) f\in\mathfrak{X}^{i}_{n}(\mathbb{K}) if and only if ⋃ α ¯ ∈ ℜ ⁡ ( f) ℒ f, α ¯ ​ ( 𝕂) ⊆ X n i ​ ( 𝕂) \bigcup_{\overline{\alpha}\in\mathfrak{R}(f)}\mathscr{L}_{f,\overline{\alpha}}(\mathbb{K})\subseteq X^{i}_{n}(\mathbb{K}). Equivalently, by Remark 4.5 (ii) we obtain that f ∈ 𝔛 n i ​ ( 𝕂) f\in\mathfrak{X}^{i}_{n}(\mathbb{K}) if and only if ρ n − 1 ​ ( q S − 1 ​ ( [f])) ⊆ X n i ​ ( 𝕂) \rho_{n}^{-1}(q_{S}^{-1}([f]))\subseteq X^{i}_{n}(\mathbb{K}). Since ρ n − 1 ​ ( f) ⊆ ρ n − 1 ​ ( q S − 1 ​ ( [f])) \rho_{n}^{-1}(f)\subseteq\rho_{n}^{-1}(q_{S}^{-1}([f])), it follows that ρ n − 1 ​ ( f) ⊆ ρ n − 1 ​ ( 𝔛 n i ​ ( 𝕂)) \rho_{n}^{-1}(f)\subseteq\rho_{n}^{-1}(\mathfrak{X}^{i}_{n}(\mathbb{K})) if and only if ρ n − 1 ​ ( f) ⊆ X n i ​ ( 𝕂) \rho_{n}^{-1}(f)\subseteq X^{i}_{n}(\mathbb{K}). ∎

###### Definition 4.9.

In light of Lemma 4.8, for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1, we define the i t ​ h i^{th} discriminant hypersurface of degree n n over an algebraically closed field 𝕂 \mathbb{K} to be X n i ​ ( 𝕂) ⊆ 𝔸 𝕂 n ​ ( 𝕂) X^{i}_{n}(\mathbb{K})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}).

###### Definition 4.10.

For a generic degree n n monic univariate polynomial f ⁡ ( X) = X n + y 1 ​ X n − 1 + y 2 ​ X n − 2 + ⋯ + y n − 1 ​ X + y n f(X)=X^{n}+y_{1}X^{n-1}+y_{2}X^{n-2}+\dots+y_{n-1}X+y_{n} and for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1, define the i t ​ h i^{th} discriminant polynomial Disc n i ⁡ ( y 1, …, y n) \disc_{n}^{i}(y_{1},\dots,y_{n}) to be the degree 2 ​ n − i 2n-i homogeneous polynomial given by the resultant Res ⁡ ( f, f i) \Res(f,f_{i}) in the ring ℤ ⁡ [y 1, …, y n] \mathbb{Z}[y_{1},\dots,y_{n}].

Let κ n: 𝔸 𝕂 n ​ ( 𝕂) → 𝕂 ​ [X] n \kappa_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow\mathbb{K}[X]_{n} be the “coefficient map” defined by ( y 1, …, y n) ↦ X n + y 1 ​ X n − 1 + ⋯ + y n − 1 ​ X + y n (y_{1},\dots,y_{n})\mapsto X^{n}+y_{1}X^{n-1}+\dots+y_{n-1}X+y_{n}, which is also a bijection. Then by definition of the resultant, we immediately see that the zero locus Δ n i ​ ( 𝕂):= V ⁡ ( Disc n i) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \Delta^{i}_{n}(\mathbb{K}):=V(\disc_{n}^{i})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) equals κ n − 1 ​ ( 𝔛 n i ​ ( 𝕂)) \kappa_{n}^{-1}(\mathfrak{X}^{i}_{n}(\mathbb{K})). Thus, we have

(4.5) |  | 𝔛 n i ​ ( 𝕂) = κ n ​ ( Δ n i ​ ( 𝕂)) = ρ n ​ ( X n i ​ ( 𝕂)) \mathfrak{X}^{i}_{n}(\mathbb{K})=\kappa_{n}(\Delta^{i}_{n}(\mathbb{K}))=\rho_{n}(X^{i}_{n}(\mathbb{K})) |  |

We note that in ( 4.5) above, we do not have an explicit understanding of the defining conditions/ polynomials for 𝔛 n i ​ ( 𝕂) \mathfrak{X}^{i}_{n}(\mathbb{K}) and Δ n i ​ ( 𝕂) \Delta^{i}_{n}(\mathbb{K}). However, by ( 4.4) we note that X n i ​ ( 𝕂) X^{i}_{n}(\mathbb{K}) have a very explicit description in terms of the shift projection maps and the zero sets of elementary symmetric polynomials. The following proposition will be useful in analyzing X n i ​ ( 𝕂) X^{i}_{n}(\mathbb{K}) further.

###### Proposition 4.11.

For each 1 ≤ i ≤ n 1\leq i\leq n and j ≠ i j\neq i, let Φ i ​ j: Z n i ​ ( 𝕂) → Z n i ​ ( 𝕂) \Phi_{ij}:Z^{i}_{n}(\mathbb{K})\rightarrow Z^{i}_{n}(\mathbb{K}) be the regular map ( x 1, …, x i − 1, 0, x i + 1, …, x n) ↦ ( y 1, …, y i − 1, 0, y i + 1, …, y n) (x_{1},\dots,x_{i-1},0,x_{i+1},\dots,x_{n})\mapsto(y_{1},\dots,y_{i-1},0,y_{i+1},\dots,y_{n}), where y j = − x j y_{j}=-x_{j} and y l = x l − x j y_{l}=x_{l}-x_{j} for all l ≠ j l\neq j. Then each Φ i ​ j \Phi_{ij} is an involution on Z n i ​ ( 𝕂) Z^{i}_{n}(\mathbb{K}) such that

(4.6) |  | ( 𝔭 n j) − 1 ​ ( V n − 1 j ​ ( H ​ D n − 1 k ​ 𝐱 n − 1)) = ( 𝔭 n i) − 1 ​ ( Φ i ​ j ​ ( V n − 1 i ​ ( H ​ D n − 1 k ​ 𝐱 n − 1))). (\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1}))=(\mathfrak{p}^{i}_{n})^{-1}(\Phi_{ij}(V^{i}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1}))). |  |

###### Proof.

Let ( x 1, …, x n) ∈ ( 𝔭 n j) − 1 ​ ( V n − 1 j ​ ( H ​ D n − 1 k ​ 𝐱 n − 1)) (x_{1},\dots,x_{n})\in(\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1})), whereby equivalently 𝔭 n j ​ ( x 1, …, x n) = ( x 1 − x j, …, x j − 1 − x j, 0, x j + 1 − x j, …, x n − x j) ∈ V n − 1 j ​ ( H ​ D n − 1 k ​ 𝐱 n − 1) ⊆ Z n j ​ ( 𝕂) \mathfrak{p}^{j}_{n}(x_{1},\dots,x_{n})=(x_{1}-x_{j},\dots,x_{j-1}-x_{j},0,x_{j+1}-x_{j},\dots,x_{n}-x_{j})\in V^{j}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1})\subseteq Z^{j}_{n}(\mathbb{K}), i.e.,

(4.7) |  | H ​ D n − 1 k ​ 𝐱 n − 1 ​ ( x 1 − x j, …, x j − 1 − x j, x j + 1 − x j, …, x n − x j) = 0. HD^{k}_{n-1}\mathbf{x}_{n-1}(x_{1}-x_{j},\dots,x_{j-1}-x_{j},x_{j+1}-x_{j},\dots,x_{n}-x_{j})=0. |  |

Let ( y 1, …, y i − 1, 0, y i + 1, …, y n):= 𝔭 n i ​ ( x 1, …, x n) = ( x 1 − x i, …, x i − 1 − x i, 0, x i + 1 − x i, …, x n − x i) (y_{1},\dots,y_{i-1},0,y_{i+1},\dots,y_{n}):=\mathfrak{p}^{i}_{n}(x_{1},\dots,x_{n})=(x_{1}-x_{i},\dots,x_{i-1}-x_{i},0,x_{i+1}-x_{i},\dots,x_{n}-x_{i}) and then note that y l − y j = x l − x j y_{l}-y_{j}=x_{l}-x_{j} for all l ≠ i l\neq i and − y j = x i − x j -y_{j}=x_{i}-x_{j}. Substituting these for x l − x j x_{l}-x_{j} in ( 4.7) for all l ≠ j l\neq j (assume i < j i<j without loss of generality):

 | H ​ D n − 1 k ​ 𝐱 n − 1 ​ ( y 1 − y j, …, y i − 1 − y j, − y j, y i + 1 − y j, …, y j − 1 − y j, y j + 1 − y j, …, y n − y j) = 0. \displaystyle HD^{k}_{n-1}\mathbf{x}_{n-1}(y_{1}-y_{j},\dots,y_{i-1}-y_{j},-y_{j},y_{i+1}-y_{j},\dots,y_{j-1}-y_{j},y_{j+1}-y_{j},\dots,y_{n}-y_{j})=0. |  |

Furthermore, since H ​ D n − 1 k ​ 𝐱 n − 1 ​ ( z 1, …, z n − 1) HD^{k}_{n-1}\mathbf{x}_{n-1}(z_{1},\dots,z_{n-1}) is a symmetric polynomial in the z i z_{i}, we equivalently obtain the following by shifting − y j -y_{j} from the i t ​ h i^{th} coordinate the ( j − 1) t ​ h (j-1)^{th} coordinate

(4.8) |  | H ​ D n − 1 k ​ 𝐱 n − 1 ​ ( y 1 − y j, …, y i − 1 − y j, y i + 1 − y j, …, y j − 1 − y j, − y j, y j + 1 − y j, …, y n − y j) = 0. HD^{k}_{n-1}\mathbf{x}_{n-1}(y_{1}-y_{j},\dots,y_{i-1}-y_{j},y_{i+1}-y_{j},\dots,y_{j-1}-y_{j},-y_{j},y_{j+1}-y_{j},\dots,y_{n}-y_{j})=0. |  |

By definition of the involution Φ i ​ j: Z n i ​ ( 𝕂) → Z n i ​ ( 𝕂) \Phi_{ij}:Z^{i}_{n}(\mathbb{K})\rightarrow Z^{i}_{n}(\mathbb{K}), we see that Φ i ​ j ​ ( y 1, …, y i − 1, 0, y i + 1, …, y n) = Φ i ​ j ​ ( 𝔭 n i ​ ( x 1, …, x n) ∈ V n − 1 i ​ ( H ​ D n − 1 k ​ 𝐱 n − 1) CLOSE \Phi_{ij}(y_{1},\dots,y_{i-1},0,y_{i+1},\dots,y_{n})=\Phi_{ij}(\mathfrak{p}^{i}_{n}(x_{1},\dots,x_{n})\in V^{i}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1}). Since each of the above steps is reversible, we see that ( x 1, …, x n) ∈ ( 𝔭 n j) − 1 ​ ( V n − 1 j ​ ( H ​ D n − 1 k ​ 𝐱 n − 1)) (x_{1},\dots,x_{n})\in(\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1})) if and only if Φ i ​ j ​ ( 𝔭 n i ​ ( x 1, …, x n) ∈ V n − 1 i ​ ( H ​ D n − 1 k ​ 𝐱 n − 1) CLOSE \Phi_{ij}(\mathfrak{p}^{i}_{n}(x_{1},\dots,x_{n})\in V^{i}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1}). Since Φ i ​ j \Phi_{ij} is an involution, we have ( 𝔭 n j) − 1 ​ ( V n − 1 j ​ ( H ​ D n − 1 k ​ 𝐱 n − 1)) = ( 𝔭 n i) − 1 ​ ( Φ i ​ j ​ ( V n − 1 i ​ ( H ​ D n − 1 k ​ 𝐱 n − 1))) (\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1}))=(\mathfrak{p}^{i}_{n})^{-1}(\Phi_{ij}(V^{i}_{n-1}(HD^{k}_{n-1}\mathbf{x}_{n-1}))). ∎

The following lemma describes the composition of the involutions Φ i ​ j: Z n i ​ ( 𝕂) → Z n i ​ ( 𝕂) \Phi_{ij}:Z^{i}_{n}(\mathbb{K})\rightarrow Z^{i}_{n}(\mathbb{K}), with each other and with transpositions, for a fixed 1 ≤ i ≤ n 1\leq i\leq n. We skip the proof, which is a straightforward computation.

###### Lemma 4.12.

Let 1 ≤ i ≤ n 1\leq i\leq n and 1 ≤ j 1, ≠ j 2 ≤ n 1\leq j_{1},\neq j_{2}\leq n, distinct from i i. Let τ j 1, j 2: Z n i ​ ( 𝕂) → Z n i ​ ( 𝕂) \tau_{j_{1},j_{2}}:Z^{i}_{n}(\mathbb{K})\rightarrow Z^{i}_{n}(\mathbb{K}) be the transposition of coordinates x j 1 x_{j_{1}} and x j 2 x_{j_{2}} for all ( x 1, …, x i − 1, 0, x i + 1, …, x n) ∈ Z n i ​ ( 𝕂) (x_{1},\dots,x_{i-1},0,x_{i+1},\dots,x_{n})\in Z^{i}_{n}(\mathbb{K}). Then we have Φ i ​ j 1 ∘ Φ i ​ j 2 = τ j 1 ​ j 2 ∘ Φ i ​ j 1 = Φ i ​ j 2 ∘ τ j 1 ​ j 2 \Phi_{ij_{1}}\circ\Phi_{ij_{2}}=\tau_{j_{1}j_{2}}\circ\Phi_{ij_{1}}=\Phi_{ij_{2}}\circ\tau_{j_{1}j_{2}}. Furthermore, for any 1 ≤ j, j 1, j 2 ≤ n 1\leq j,j_{1},j_{2}\leq n all mutually distinct and not equal to i i, we have Φ i ​ j ∘ τ j 1 ​ j 2 = τ j 1 ​ j 2 ∘ Φ i ​ j \Phi_{ij}\circ\tau_{j_{1}j_{2}}=\tau_{j_{1}j_{2}}\circ\Phi_{ij}.

###### Remark 4.13.

For brevity, let Φ j:= Φ n ​ j: Z n n ​ ( 𝕂) → Z n n ​ ( 𝕂) \Phi_{j}:=\Phi_{nj}:Z^{n}_{n}(\mathbb{K})\rightarrow Z^{n}_{n}(\mathbb{K}) be the involution described in Proposition 4.11 for i = n i=n, j ≠ i j\neq i and let 𝔭 n:= 𝔭 n n: 𝔸 𝕂 n ​ ( 𝕂) → Z n n ​ ( 𝕂) \mathfrak{p}_{n}:=\mathfrak{p}^{n}_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow Z^{n}_{n}(\mathbb{K}) be the n t ​ h n^{th} shift projection map. Furthermore, define Φ n: Z n n ​ ( 𝕂) → Z n n ​ ( 𝕂) \Phi_{n}:Z^{n}_{n}(\mathbb{K})\rightarrow Z^{n}_{n}(\mathbb{K}) to be the identity map. By Proposition 4.11, we have ( 𝔭 n j) − 1 ​ ( V n − 1 j ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) = 𝔭 n − 1 ​ ( Φ j ​ ( V n − 1 n ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1))) (\mathfrak{p}^{j}_{n})^{-1}(V^{j}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))=\mathfrak{p}_{n}^{-1}(\Phi_{j}(V^{n}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))) for all 1 ≤ j ≤ n 1\leq j\leq n. The involutions Φ j: Z n n ​ ( 𝕂) → Z n n ​ ( 𝕂) \Phi_{j}:Z^{n}_{n}(\mathbb{K})\rightarrow Z^{n}_{n}(\mathbb{K}) are regular for all 1 ≤ j ≤ n 1\leq j\leq n: for j ≠ n j\neq n, Φ j \Phi_{j} is induced by the corresponding algebra isomorphism

(4.9) |  | Φ j #: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1], Φ j #​ ( x l) = { x l − x j, l ≠ j, − x j, l = j. \Phi^{\#}_{j}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1}],\qquad\Phi^{\#}_{j}(x_{l})=\begin{cases}x_{l}-x_{j},\quad l\neq j,\\ -x_{j},\quad l=j.\end{cases} |  |

Letting Φ n #: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1] \Phi^{\#}_{n}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1}] be the identity map corresponding to Φ n \Phi_{n}, we have Φ j ​ ( V n − 1 n ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) = V n − 1 n ​ ( Φ j #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) ⊆ Z n n ​ ( 𝕂) \Phi_{j}(V^{n}_{n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))=V^{n}_{n-1}(\Phi^{\#}_{j}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))\subseteq Z^{n}_{n}(\mathbb{K}) for any 1 ≤ j ≤ n 1\leq j\leq n. Thus ( 4.4) yields:

(4.10) |  | X n i ​ ( 𝕂) = 𝔭 n − 1 ​ ( ⋃ j = 1 n V n − 1 n ​ ( Φ j #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1))), ∀ 1 ≤ i ≤ n − 1 X^{i}_{n}(\mathbb{K})=\mathfrak{p}_{n}^{-1}(\bigcup_{j=1}^{n}V^{n}_{n-1}(\Phi^{\#}_{j}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))),\ \ \forall 1\leq i\leq n-1 |  |

Note that ⋃ j = 1 n V n − 1 n ​ ( Φ j #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) \bigcup_{j=1}^{n}V^{n}_{n-1}(\Phi^{\#}_{j}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})) is an algebraic subset in Z n n ​ ( 𝕂) ≅ 𝔸 𝕂 n − 1 ​ ( 𝕂) Z^{n}_{n}(\mathbb{K})\cong\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}), i.e., affine space of one lower dimension.

### 4.3. Arithmetic Casas-Alvero scheme and higher discriminants

In this subsection, we provide an alternate description of the set X n ​ ( 𝕂) X_{n}(\mathbb{K}) of 𝕂 \mathbb{K} -rational points of the arithmetic Casas-Alvero schemes X n X_{n} considered in [7], for any algebraically closed field 𝕂 \mathbb{K}. This will be utilized in establishing Theorem B and in Section 6.

We briefly recall the construction of the weighted projective schemes X n X_{n}. For each n ≥ 2 n\geq 2, let ℤ w ​ [y 1, y 2, …, y n − 1, y n] \mathbb{Z}^{w}[y_{1},y_{2},\dots,y_{n-1},y_{n}] be the graded algebra of n n variables y 1, …, y n y_{1},\dots,y_{n}, where y i y_{i} has weight i i. Consider the reduced i t ​ h i^{th} discriminant polynomials Disc n i ⁡ ( y 1, …, y n − 1, 0) \disc^{i}_{n}(y_{1},\dots,y_{n-1},0) (by setting y n = 0 y_{n}=0) for 1 ≤ i ≤ n − 1 1\leq i\leq n-1, which are homogeneous polynomials in ℤ w ​ [y 1, y 2, …, y n − 1, y n] \mathbb{Z}^{w}[y_{1},y_{2},\dots,y_{n-1},y_{n}] of weighted degree n ⁡ ( n − i) n(n-i). The n t ​ h n^{th} arithmetic Casas-Alvero scheme is the weighted projective ℤ \mathbb{Z} -subscheme X n ⊆ ℙ ℤ ​ ( 1, 2, …, n − 1) X_{n}\subseteq\mathbb{P}_{\mathbb{Z}}(1,2,\dots,n-1) defined by the ideal ⟨ Disc n i ( y 1, …, y n − 1, 0), 1 ≤ i ≤ n − 1 ⟩ \langle\disc^{i}_{n}(y_{1},\dots,y_{n-1},0),\ 1\leq i\leq n-1\rangle.

For any algebraically closed field 𝕂 \mathbb{K}, it follows that the affine cone of ( X n) 𝕂:= X n × Spec ⁡ ( ℤ) Spec ⁡ ( 𝕂) (X_{n})_{\mathbb{K}}:=X_{n}\times_{\spec(\mathbb{Z})}\spec(\mathbb{K}) is equal to ⋂ i = 1 n − 1 Δ n i ​ ( 𝕂) ∩ V ⁡ ( y n) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \bigcap_{i=1}^{n-1}\Delta^{i}_{n}(\mathbb{K})\cap V(y_{n})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}), where Δ n i ​ ( 𝕂):= V ⁡ ( Disc n i ​ ( y 1, …, y n)) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \Delta^{i}_{n}(\mathbb{K}):=V(\disc^{i}_{n}(y_{1},\dots,y_{n}))\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) and 𝔸 𝕂 n = Spec ⁡ ( 𝕂 ⁡ [y 1, …, y n]) \mathbb{A}^{n}_{\mathbb{K}}=\spec(\mathbb{K}[y_{1},\dots,y_{n}]). Then we have (see [10, Definition 3.1.9]):

 | X n ​ ( 𝕂) = ( X ^ n ​ ( 𝕂) ∖ { 𝟎 }) / 𝔾 m w ​ ( 𝕂); X ^ n ​ ( 𝕂):= ⋂ i = 1 n − 1 Δ n i ​ ( 𝕂) ∩ V ⁡ ( y n), X_{n}(\mathbb{K})=(\widehat{X}_{n}(\mathbb{K})\setminus\{\mathbf{0}\})/\mathbb{G}^{w}_{m}(\mathbb{K});\ \ \widehat{X}_{n}(\mathbb{K}):=\bigcap_{i=1}^{n-1}\Delta^{i}_{n}(\mathbb{K})\cap V(y_{n}), |  |

where 𝔾 m w \mathbb{G}^{w}_{m} denotes the weighted action of 𝔾 m \mathbb{G}_{m} on 𝔸 n ∖ { 𝟎 } \mathbb{A}^{n}\setminus\{\mathbf{0}\} by λ. ( a 1, …, a n) = ( λ ​ a 1, λ 2 ​ a 2, …, λ n ​ a n) \lambda.(a_{1},\dots,a_{n})=(\lambda a_{1},\lambda^{2}a_{2},\dots,\lambda^{n}a_{n}).

Note that there is a graded ℤ \mathbb{Z} -algebra map ν n #: ℤ w ​ [y 1, …, y n] → ℤ ⁡ [x 1, …, x n] \nu^{\#}_{n}:\mathbb{Z}^{w}[y_{1},\dots,y_{n}]\rightarrow\mathbb{Z}[x_{1},\dots,x_{n}], where x i x_{i} ’s have weight 1 1, given by y i ↦ ( − 1) i ​ H ​ D n − i ​ 𝐱 n y_{i}\mapsto(-1)^{i}HD^{n-i}\mathbf{x}_{n}, for all 1 ≤ i ≤ n 1\leq i\leq n. That this map is weighted graded follows from the fact that H ​ D n i ​ 𝐱 n = e n − i ​ ( x 1, …, x n) HD^{i}_{n}\mathbf{x}_{n}=e_{n-i}(x_{1},\dots,x_{n}), i.e., the degree n − i n-i elementary symmetric polynomial in x 1, …, x n x_{1},\dots,x_{n}. Extending scalars, for any algebraically closed field 𝕂 \mathbb{K}, we obtain a weighted graded 𝕂 \mathbb{K} -algebra map 𝕂 w ​ [y 1, …, y n] → 𝕂 ⁡ [x 1, …, x n] \mathbb{K}^{w}[y_{1},\dots,y_{n}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n}], which we also denote by ν n #\nu^{\#}_{n}. This induces a regular map ν n: 𝔸 𝕂 n → 𝔸 𝕂 n \nu_{n}:\mathbb{A}^{n}_{\mathbb{K}}\rightarrow\mathbb{A}^{n}_{\mathbb{K}}, which we call Vieta’s map, since 𝐚:= ( a 1, …, a n) ↦ ( − e 1 ​ ( 𝐚), …, ( − 1) n ​ e n ​ ( 𝐚)) \mathbf{a}:=(a_{1},\dots,a_{n})\mapsto(-e_{1}(\mathbf{a}),\dots,(-1)^{n}e_{n}(\mathbf{a})). By Vieta’s formulae, it follows then ν n ​ ( X n i ​ ( 𝕂)) = Δ n i ​ ( 𝕂) \nu_{n}(X^{i}_{n}(\mathbb{K}))=\Delta^{i}_{n}(\mathbb{K}) for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1 and ν n ​ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂)) = ⋂ i = 1 n − 1 Δ n i ​ ( 𝕂) \nu_{n}(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}))=\bigcap_{i=1}^{n-1}\Delta^{i}_{n}(\mathbb{K}). Furthermore, since ν n #​ ( y n) = ( − 1) n ​ H ​ D 0 ​ 𝐱 n = ( − 1) n ​ x 1 ​ x 2 ​ … ​ x n \nu^{\#}_{n}(y_{n})=(-1)^{n}HD^{0}\mathbf{x}_{n}=(-1)^{n}x_{1}x_{2}\dots x_{n}, it follows that

 | ν n ​ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂)) ∩ ν n ​ ( V ⁡ ( x 1 ​ x 2 ​ … ​ x n)) = ⋂ i = 1 n − 1 Δ n i ​ ( 𝕂) ∩ V ⁡ ( y n) \displaystyle\nu_{n}(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}))\cap\nu_{n}(V(x_{1}x_{2}\dots x_{n}))=\bigcap_{i=1}^{n-1}\Delta^{i}_{n}(\mathbb{K})\cap V(y_{n}) |  |

 | ⟹ ν n ​ ( ⋃ j = 1 n V ⁡ ( x j) ∩ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂))) = ⋂ i = 1 n − 1 Δ n i ​ ( 𝕂) ∩ V ⁡ ( y n), \displaystyle\implies\nu_{n}(\bigcup_{j=1}^{n}V(x_{j})\cap(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})))=\bigcap_{i=1}^{n-1}\Delta^{i}_{n}(\mathbb{K})\cap V(y_{n}), |  |

where we again use Vieta’s relations to obtain the second equality. By Lemma 4.12, we observe that X n i ​ ( 𝕂) X^{i}_{n}(\mathbb{K}) is symmetric (i.e., invariant under 𝔖 n \mathfrak{S}_{n} -action on 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}) for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1. In particular, if τ j ​ n \tau_{jn} is the permutation which swaps the coordinates x j x_{j} and x n x_{n}, then τ j ​ n ​ ( V ⁡ ( x j) ∩ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂))) = V ⁡ ( x n) ∩ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂)) \tau_{jn}(V(x_{j})\cap(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})))=V(x_{n})\cap(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})). Since ν n ∘ σ = ν n \nu_{n}\circ\sigma=\nu_{n} for all σ ∈ 𝔖 n \sigma\in\mathfrak{S}_{n}, we conclude

(4.11) |  | ν n ​ ( V ⁡ ( x n) ∩ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂))) = ⋂ i = 1 n − 1 Δ n i ​ ( 𝕂) ∩ V ⁡ ( y n) = X ^ n ​ ( 𝕂) \nu_{n}(V(x_{n})\cap(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})))=\bigcap_{i=1}^{n-1}\Delta^{i}_{n}(\mathbb{K})\cap V(y_{n})=\widehat{X}_{n}(\mathbb{K}) |  |

Furthermore, ν n: 𝔸 𝕂 n → 𝔸 𝕂 n \nu_{n}:\mathbb{A}_{\mathbb{K}}^{n}\rightarrow\mathbb{A}_{\mathbb{K}}^{n} interchanges the weighted and unweighted actions of 𝔾 m \mathbb{G}_{m} on 𝔸 𝕂 n \mathbb{A}_{\mathbb{K}}^{n}, i.e., the following diagram commutes:

 | 𝔾 m × 𝔸 𝕂 n {\lx@inpgf@ignorespaces\mathbb{G}_{m}\times\mathbb{A}_{\mathbb{K}}^{n}} 𝔾 m w × 𝔸 𝕂 n {\lx@inpgf@ignorespaces\mathbb{G}^{w}_{m}\times\mathbb{A}_{\mathbb{K}}^{n}} 𝔸 𝕂 n {\lx@inpgf@ignorespaces\mathbb{A}_{\mathbb{K}}^{n}} 𝔸 𝕂 n {\lx@inpgf@ignorespaces\mathbb{A}_{\mathbb{K}}^{n}} id × ν n \scriptstyle{\lx@inpgf@ignorespaces\operatorname{id}\times\nu_{n}} ν n \scriptstyle{\lx@inpgf@ignorespaces\nu_{n}} |  |

The left vertical arrow in the diagram is the usual scaling action of 𝔾 m \mathbb{G}_{m} whereas the right arrow is the weighted scaling action of 𝔾 m \mathbb{G}_{m} on 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}. Since ν n − 1 ​ ( { 𝟎 }) = { 𝟎 } \nu_{n}^{-1}(\{\mathbf{0}\})=\{\mathbf{0}\}, the above commutative diagram yields a regular map ν n ¯: ℙ 𝕂 n − 1 → ℙ 𝕂 ​ ( 1, 2, …, n − 1) \overline{\nu_{n}}:\mathbb{P}^{n-1}_{\mathbb{K}}\rightarrow\mathbb{P}_{\mathbb{K}}(1,2,\dots,n-1). Utilizing the coefficient isomorphism κ n: 𝔸 𝕂 n ​ ( 𝕂) → 𝕂 ​ [X] n \kappa_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow\mathbb{K}[X]_{n}, we observe that the fibers of the Vieta map ν n \nu_{n} are precisely the orbits of the 𝔖 n \mathfrak{S}_{n} -action on 𝔸 𝕂 n ​ ( 𝕂) \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}). In particular, this implies that ν ¯ n: ℙ 𝕂 n − 1 → ℙ 𝕂 ​ ( 1, 2, …, n − 1) \overline{\nu}_{n}:\mathbb{P}^{n-1}_{\mathbb{K}}\rightarrow\mathbb{P}_{\mathbb{K}}(1,2,\dots,n-1) is a quasi-finite morphism. Thus, we obtain the following description of X n ​ ( 𝕂) X_{n}(\mathbb{K}).

###### Proposition 4.14.

Let 𝒱 ^ n ​ ( 𝕂):= V ⁡ ( x n) ∩ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂)) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \widehat{\mathcal{V}}_{n}(\mathbb{K}):=V(x_{n})\cap(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}))\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) and 𝒱 n ​ ( 𝕂):= ( 𝒱 ^ n ​ ( 𝕂) ∖ { 𝟎 }) / 𝔾 m ⊆ ℙ 𝕂 n − 1 ​ ( 𝕂) \mathcal{V}_{n}(\mathbb{K}):=(\widehat{\mathcal{V}}_{n}(\mathbb{K})\setminus\{\mathbf{0}\})/\mathbb{G}_{m}\subseteq\mathbb{P}^{n-1}_{\mathbb{K}}(\mathbb{K}). Then X n ​ ( 𝕂) = ν ¯ n ​ ( 𝒱 n ​ ( 𝕂)) X_{n}(\mathbb{K})=\overline{\nu}_{n}(\mathcal{V}_{n}(\mathbb{K})), where ν ¯ n: ℙ 𝕂 n − 1 → ℙ 𝕂 ​ ( 1, 2, …, n − 1) \overline{\nu}_{n}:\mathbb{P}^{n-1}_{\mathbb{K}}\rightarrow\mathbb{P}_{\mathbb{K}}(1,2,\dots,n-1) is the induced Vieta map.

###### Proof.

Follows immediately from ( 4.11). ∎

## 5. Proof of the main results

In this section, we provide various equivalent formulations of Conjecture CA using the higher discriminant hypersurfaces defined in Section 4. We also prove Theorems A, B and D. As usual, we let 𝕂 \mathbb{K} be algebraically closed. Unless otherwise specified, we let 𝕂 \mathbb{K} have arbitrary characteristic.

###### Proposition 5.1.

Conjecture CA is true for all monic degree n n polynomials over 𝕂 \mathbb{K} if and only if the intersection ⋂ i = 1 n − 1 X n i ​ ( 𝕂) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) has dimension 1 1.

###### Proof.

Note that a monic degree n n polynomial f ⁡ ( X) ∈ 𝕂 ​ [X] n f(X)\in\mathbb{K}[X]_{n} satisfies the hypothesis of Conjecture CA if and only if f ⁡ ( X) ∈ ⋂ i = 1 n − 1 𝔛 n i ​ ( 𝕂) f(X)\in\bigcap_{i=1}^{n-1}\mathfrak{X}^{i}_{n}(\mathbb{K}). Thus, Conjecture CA is equivalent to the equality ⋂ i = 1 n − 1 𝔛 n i ​ ( 𝕂) = { ( X − α) n ∣ α ∈ 𝕂 } \bigcap_{i=1}^{n-1}\mathfrak{X}^{i}_{n}(\mathbb{K})=\{(X-\alpha)^{n}\mid\ \alpha\in\mathbb{K}\} which, by Lemma 4.8, is equivalent to ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = Δ n ​ ( 𝕂):= { ( α, α, …, α) ∈ 𝔸 𝕂 n ​ ( 𝕂) ∣ α ∈ 𝕂 } \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=\Delta_{n}(\mathbb{K}):=\{(\alpha,\alpha,\dots,\alpha)\in\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\mid\ \alpha\in\mathbb{K}\}. Thus, it suffices to prove that dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = 1 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=1 is equivalent to ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = Δ n ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=\Delta_{n}(\mathbb{K}). We prove the forward implication as the reverse direction is obvious. Assume dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = 1 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=1, and let ( α 1, …, α n) ∈ ⋂ i = 1 n − 1 X n i ​ ( 𝕂) ∖ Δ n ​ ( 𝕂) (\alpha_{1},\dots,\alpha_{n})\in\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})\setminus\Delta_{n}(\mathbb{K}) for the sake of contradiction. By the definition of X n i ​ ( 𝕂) X^{i}_{n}(\mathbb{K}), we have f ⁡ ( X):= ∏ i = 1 n ( X − α i) ∈ ⋂ i = 1 n − 1 𝔛 n i ​ ( 𝕂) f(X):=\prod_{i=1}^{n}(X-\alpha_{i})\in\bigcap_{i=1}^{n-1}\mathfrak{X}^{i}_{n}(\mathbb{K}). Furthermore, by [5] *Lemma 2, we see that ∏ i = 1 n ( X − ( λ ​ α i + α)) ∈ ⋂ i = 1 n − 1 𝔛 n i ​ ( 𝕂) \prod_{i=1}^{n}(X-(\lambda\alpha_{i}+\alpha))\in\bigcap_{i=1}^{n-1}\mathfrak{X}^{i}_{n}(\mathbb{K}) for all λ, α ∈ 𝕂 \lambda,\alpha\in\mathbb{K}, whence

 | λ ⁡ ( α 1, α 2, …, α n) + α ⁡ ( 1, 1, …, 1) ∈ ⋂ i = 1 n − 1 X n i ​ ( 𝕂) ​ ∀ λ, α ∈ 𝕂. \lambda(\alpha_{1},\alpha_{2},\dots,\alpha_{n})+\alpha(1,1,\dots,1)\in\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})\ \forall\lambda,\alpha\in\mathbb{K}. |  |

This forms a 2 2 -dimensional linear subvariety of ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) by choice of ( α 1, …, α n) (\alpha_{1},\dots,\alpha_{n}), which contradicts the assumption dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = 1 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=1. This completes the proof. ∎

The higher discriminant hypersurfaces in 𝔸 𝕂 n ​ ( 𝕂) \mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) are determined by V ⁡ ( Φ j #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) ⊆ 𝔸 𝕂 n − 1 ​ ( 𝕂) V(\Phi^{\#}_{j}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))\subseteq\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}) for all 1 ≤ j ≤ n 1\leq j\leq n and 1 ≤ i ≤ n − 1 1\leq i\leq n-1, by ( 4.10). Thus, Proposition 5.1 has a purely commutative algebraic analogue in terms of the polynomials Φ j #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) ∈ 𝕂 ⁡ [x 1, …, x n − 1] \Phi^{\#}_{j}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})\in\mathbb{K}[x_{1},\dots,x_{n-1}].

###### Proposition 5.2.

Conjecture CA is true for all monic degree n n polynomials over 𝕂 \mathbb{K} if and only if for all choices of 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n, the sequence Φ j 1 #​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ j n − 1 #​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1) \Phi^{\#}_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\Phi^{\#}_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}) forms a regular sequence of homogeneous polynomials in 𝕂 ⁡ [x 1, …, x n − 1] \mathbb{K}[x_{1},\dots,x_{n-1}].

###### Proof.

By ( 4.10), we can write

(5.1) |  | ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = ⋃ 1 ≤ j 1, …, j n − 1 ≤ n 𝔭 n − 1 ​ ( ⋂ i = 1 n − 1 V n − 1 n ​ ( Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1))). \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=\bigcup_{1\leq j_{1},\dots,j_{n-1}\leq n}\mathfrak{p}_{n}^{-1}(\bigcap_{i=1}^{n-1}V^{n}_{n-1}(\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))). |  |

We note that for any 1 ≤ j i ≤ n 1\leq j_{i}\leq n, the polynomial Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) ∈ 𝕂 ⁡ [x 1, …, x n − 1] \Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})\in\mathbb{K}[x_{1},\dots,x_{n-1}] is homogeneous of degree n − i n-i for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1. Proposition 5.1 implies that Conjecture CA is true in degree n n if and only if ⋂ i = 1 n − 1 V n − 1 n ​ ( Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) = { ( 0, 0, …, 0) } ⊆ 𝔸 𝕂 n − 1 ​ ( 𝕂) \bigcap_{i=1}^{n-1}V^{n}_{n-1}(\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))=\{(0,0,\dots,0)\}\subseteq\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}) for any choice of 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. The proposition follows from the fact that for any r ≥ 1 r\geq 1, a sequence of r r homogeneous polynomials in r r variables is regular if and only if the reduced affine variety defined by them is the origin in 𝔸 𝕂 r \mathbb{A}^{r}_{\mathbb{K}}. ∎

### 5.1. Proofs of Theorem A and Theorem B

We will obtain Theorem B as an immediate corollary of Theorem A. We first prove Proposition 5.3, which is the main commutative algebraic result implying Theorem A. To prove Proposition 5.3, we need the following setup.

For any 1 ≤ j ≤ n − 1 1\leq j\leq n-1, let Φ #​ [T] j: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1, T] \Phi^{\#}[T]_{j}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1},T] be the 𝕂 \mathbb{K} -algebra homomorphism induced by Φ #​ [T] j ​ ( x i) = x i − T ​ x j \Phi^{\#}[T]_{j}(x_{i})=x_{i}-Tx_{j} for all i ≠ j i\neq j and Φ #​ [T] j ​ ( x j) = ( 1 − 2 ​ T) ​ x j \Phi^{\#}[T]_{j}(x_{j})=(1-2T)x_{j}. For j = n j=n, let Φ #​ [T] n: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1, T] \Phi^{\#}[T]_{n}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1},T] be the natural inclusion of 𝕂 \mathbb{K} -algebras. Our main technical result is the following.

###### Proposition 5.3.

Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1) \Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}) forms a regular sequence in 𝕂 ⁡ [x 1, …, x n − 1, T, 1 1 − 2 ​ T] \mathbb{K}[x_{1},\dots,x_{n-1},T,\frac{1}{1-2T}] for any choice of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. Here 𝕂 \mathbb{K} is any algebraically closed field.

###### Proof.

Fix a choice of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n, and for brevity, use the notation H l:= Φ #​ [T] j l ​ ( H ​ D n − 1 l − 1 ​ 𝐱 n − 1) H_{l}:=\Phi^{\#}[T]_{j_{l}}(HD^{l-1}_{n-1}\mathbf{x}_{n-1}), for all 1 ≤ l ≤ n − 1 1\leq l\leq n-1. Furthermore, for this proof, let R:= 𝕂 ⁡ [x 1, …, x n − 1, T] R:=\mathbb{K}[x_{1},\dots,x_{n-1},T]. We will prove the proposition by induction. Clearly H 1 H_{1} is regular in R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}]. Assume for some 1 < i < n − 1 1<i<n-1, H 1, …, H i − 1 H_{1},\dots,H_{i-1} form a regular sequence in R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}]. Then it suffices to show that H i H_{i} is a non-zero divisor in R ⁡ [1 1 − 2 ​ T] / ( H 1, …, H i − 1) R[\frac{1}{1-2T}]/(H_{1},\dots,H_{i-1}). Now note that for any 1 ≤ j ≤ n 1\leq j\leq n, the homomorphisms ϕ #​ [T] j \phi^{\#}[T]_{j} can be extended to an endomorphism of R R by defining ϕ #​ [T] j ​ ( T) = T \phi^{\#}[T]_{j}(T)=T. In fact, these can also be naturally extended to endomorphisms of R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}]. Then, we note that for all 1 ≤ j ≤ n 1\leq j\leq n, ϕ #​ [T] j: R ⁡ [1 1 − 2 ​ T] → R ⁡ [1 1 − 2 ​ T] \phi^{\#}[T]_{j}:R[\frac{1}{1-2T}]\rightarrow R[\frac{1}{1-2T}] are in fact 𝕂 \mathbb{K} -algebra automorphisms. This is obvious if j = n j=n. For j < n j<n, we see that ϕ #​ [T] j − 1 \phi^{\#}[T]_{j}^{-1} is defined by:

 | ϕ #​ [T] j − 1: { x i ↦ x i + T 1 − 2 ​ T ​ x j if ​ i ≠ j x j ↦ x j 1 − 2 ​ T T ↦ T \phi^{\#}[T]_{j}^{-1}:\begin{cases}x_{i}\mapsto x_{i}+\frac{T}{1-2T}x_{j}&\text{ if }i\neq j\\ x_{j}\mapsto\frac{x_{j}}{1-2T}\\ T\mapsto T\end{cases} |  |

Thus, H 1, …, H i − 1 H_{1},\dots,H_{i-1} is a regular sequence in R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}] if and only if ϕ #​ [T] j i − 1 ​ ( H 1), …, ϕ #​ [T] j i − 1 ​ ( H i − 1) \phi^{\#}[T]_{j_{i}}^{-1}(H_{1}),\dots,\phi^{\#}[T]_{j_{i}}^{-1}(H_{i-1}) is a regular sequence in R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}], where we are using the inverse of the automorphism used in defining H i = Φ #​ [T] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) H_{i}=\Phi^{\#}[T]_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}). If j i ≠ n j_{i}\neq n, then for all 1 ≤ l ≤ i − 1 1\leq l\leq i-1 define

(5.2) |  | G l = { ( 1 − 2 ​ T) n − l ​ ϕ #​ [T] j i − 1 ​ ( H l) if j l ≠ j i h l:= H ​ D n − 1 l − 1 ​ 𝐱 n − 1 = ϕ #​ [T] j i − 1 ​ ( H l) if j l = j i G_{l}=\begin{cases}(1-2T)^{n-l}\phi^{\#}[T]_{j_{i}}^{-1}(H_{l})&\text{if $j_{l}\neq j_{i}$}\\ h_{l}:=HD^{l-1}_{n-1}\mathbf{x}_{n-1}=\phi^{\#}[T]_{j_{i}}^{-1}(H_{l})&\text{if $j_{l}=j_{i}$}\end{cases} |  |

Note that if j i = n j_{i}=n, then ϕ #​ [T] j i − 1 = ϕ #​ [T] j i = id \phi^{\#}[T]_{j_{i}}^{-1}=\phi^{\#}[T]_{j_{i}}=\operatorname{id}. So if j i = n j_{i}=n, let G l = H l G_{l}=H_{l} for all 1 ≤ l ≤ i − 1 1\leq l\leq i-1. Consequently, for any 1 ≤ j i ≤ n 1\leq j_{i}\leq n, we see that G l ∈ R G_{l}\in R for all 1 ≤ l ≤ i − 1 1\leq l\leq i-1 and H 1, …, H i − 1 H_{1},\dots,H_{i-1} forms a regular sequence in R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}] if and only if G 1, …, G i − 1 G_{1},\dots,G_{i-1} does. The upshot of applying the automorphism Φ #​ [T] j i − 1 \Phi^{\#}[T]_{j_{i}}^{-1} to the sequence H 1, …, H i − 1 H_{1},\dots,H_{i-1} is that now it suffices to prove that h i:= H ​ D n − 1 i − 1 ​ 𝐱 n − 1 = Φ #​ [T] j i − 1 ​ ( H i) h_{i}:=HD^{i-1}_{n-1}\mathbf{x}_{n-1}=\Phi^{\#}[T]_{j_{i}}^{-1}(H_{i}) is a non-zero divisor in R ⁡ [1 1 − 2 ​ T] / ( G 1, …, G i − 1) R[\frac{1}{1-2T}]/(G_{1},\dots,G_{i-1}).

Furthermore, since G l mod T = h l:= H ​ D n − 1 l − 1 ​ 𝐱 n − 1 G_{l}\mod T=h_{l}:=HD^{l-1}_{n-1}\mathbf{x}_{n-1} for all 1 ≤ l ≤ n − 1 1\leq l\leq n-1, it follows that G 1, …, G i − 1, h i G_{1},\dots,G_{i-1},h_{i} forms a regular sequence in R ⁡ [1 1 − 2 ​ T] / ( T) R[\frac{1}{1-2T}]/(T). Thus, no minimal prime of the ideal ( G 1, …, G i − 1) ⊆ R ⁡ [1 1 − 2 ​ T] (G_{1},\dots,G_{i-1})\subseteq R[\frac{1}{1-2T}] can contain both h i h_{i} and T T. Hence, it suffices to prove that h i h_{i} is a non-zero divisor in R ⁡ [1 1 − 2 ​ T, 1 T] / ( G 1, …, G i − 1) R[\frac{1}{1-2T},\frac{1}{T}]/(G_{1},\dots,G_{i-1}). Furthermore, since R R is a domain, localization sends non-zero divisors to non-zero divisors, whence it suffices to prove that h i h_{i} is a non-zero divisor in R ⁡ [1 T] / ( G 1, …, G i − 1) R[\frac{1}{T}]/(G_{1},\dots,G_{i-1}). Now let Θ: R ⁡ [1 T] → R ⁡ [1 T] \Theta:R[\frac{1}{T}]\rightarrow R[\frac{1}{T}] be the 𝕂 \mathbb{K} -algebra automorphism defined by fixing the x i x_{i} ’s but swapping T T and 1 / T 1/T. Then it suffices to prove that h i = Θ ⁡ ( h i) h_{i}=\Theta(h_{i}) is a non-zero divisor in R ⁡ [1 T] / ( Θ ⁡ ( G 1), …, Θ ⁡ ( G i − 1)) R[\frac{1}{T}]/(\Theta(G_{1}),\dots,\Theta(G_{i-1})). If j i ≠ n j_{i}\neq n, then for all 1 ≤ l ≤ i − 1 1\leq l\leq i-1, define

 | F l = { T deg T ⁡ G l ​ Θ ​ ( G l) if H l ≠ h l T 2 ​ deg T ​ G l ​ Θ ​ ( G l) if H l = h l and l ≠ 1 T 2 ​ deg T ​ G 1 + 2 ​ Θ ​ ( G 1) if H 1 = h 1 F_{l}=\begin{cases}T^{\deg_{T}G_{l}}\Theta(G_{l})&\text{if $H_{l}\neq h_{l}$}\\ T^{2\deg_{T}G_{l}}\Theta(G_{l})&\text{if $H_{l}=h_{l}$ and $l\neq 1$}\\ T^{2\deg_{T}G_{1}+2}\Theta(G_{1})&\text{if $H_{1}=h_{1}$}\par\end{cases} |  |

If j i = n j_{i}=n, then define F l = T deg T ⁡ G l ​ Θ ​ ( G l) F_{l}=T^{\deg_{T}G_{l}}\Theta(G_{l}) for all 1 ≤ l ≤ i − 1 1\leq l\leq i-1. Then F l ∈ R F_{l}\in R for all 1 ≤ l ≤ i − 1 1\leq l\leq i-1 and it suffices to prove h i h_{i} is non-zero divisor in R ⁡ [1 T] / ( F 1, …, F i − 1) R[\frac{1}{T}]/(F_{1},\dots,F_{i-1}). Furthermore, if j i ≠ n j_{i}\neq n, then either F l = h l F_{l}=h_{l} or deg T ⁡ ( F l) = 2 ​ ( n − l) \deg_{T}(F_{l})=2(n-l) and if j i = n j_{i}=n, then either F l = h l F_{l}=h_{l} or deg T ⁡ ( F l) = n − l \deg_{T}(F_{l})=n-l. Again, since R R is a domain, it suffices for us to prove that h i h_{i} is a non-zero divisor in R / ( F 1, …, F i − 1) R/(F_{1},\dots,F_{i-1}). To prove this, we will need the following lemma.

###### Lemma 5.4.

Let ≺ T \prec_{T} be the monomial partial ordering on R = 𝕂 ⁡ [x 1, …, x n − 1, T] R=\mathbb{K}[x_{1},\dots,x_{n-1},T], defined by 𝐱 𝐚 T b ≺ T 𝐱 𝐚 ′ T b ′ \mathbf{x}^{\mathbf{a}}T^{b}\prec_{T}\mathbf{x}^{\mathbf{a}^{\prime}}T^{b^{\prime}} if and only if b ≤ b ′ b\leq b^{\prime}. For any f ∈ R f\in R, let Dom ⁡ ( f) \dom(f) be the sum of the maximal monomials in f f under the partial order ≺ T \prec_{T}. Then for any non-zero R R -linear combination of the form ∑ j ∈ S c j ​ F j \sum_{j\in S}c_{j}F_{j} for any subset S ⊆ { 1, …, i − 1 } S\subseteq\{1,\dots,i-1\}, there exist c ~ j ∈ R \tilde{c}_{j}\in R such that ∑ j ∈ S c j ​ F j = ∑ j ∈ S c ~ j ​ F j \sum_{j\in S}c_{j}F_{j}=\sum_{j\in S}\tilde{c}_{j}F_{j} and Dom ⁡ ( ∑ j ∈ S c j ​ F j) = Dom ⁡ ( ∑ j ∈ S Dom ⁡ ( c ~ j) ​ Dom ⁡ ( F j)) \dom(\sum_{j\in S}c_{j}F_{j})=\dom(\sum_{j\in S}\dom(\tilde{c}_{j})\dom(F_{j})).

###### Proof of Lemma.

Let n j:= deg T ⁡ F j n_{j}:=\deg_{T}F_{j}. Then note that Dom ⁡ ( F j) = T n j ​ h j \dom(F_{j})=T^{n_{j}}h_{j} for all 1 ≤ j ≤ i − 1 1\leq j\leq i-1. Let c j = ∑ p = 0 m j c j, p ​ T p c_{j}=\sum_{p=0}^{m_{j}}c_{j,p}T^{p} and F j = ∑ q = 1 n j F j, q ​ T q F_{j}=\sum_{q=1}^{n_{j}}F_{j,q}T^{q}, where F j, n j = h j F_{j,n_{j}}=h_{j}. By convention, for p < 0 p<0 or p > m j p>m_{j}, we set c j, p = 0 c_{j,p}=0 and similarly, for q < 0 q<0 or q > n j q>n_{j}, set F j, q = 0 F_{j,q}=0. Then if ∑ j ∈ S c j, m j ​ h j ​ T n j + m j ≠ 0 \sum_{j\in S}c_{j,m_{j}}h_{j}T^{n_{j}+m_{j}}\neq 0, then clearly Dom ⁡ ( ∑ j ∈ S c j ​ F j) = Dom ⁡ ( ∑ j ∈ S Dom ⁡ ( c j) ​ Dom 1 ⁡ ( F j)) \dom(\sum_{j\in S}c_{j}F_{j})=\dom(\sum_{j\in S}\dom(c_{j})\dom_{1}(F_{j})). Else, suppose ∑ j ∈ S c j, m j ​ h j ​ T n j + m j = 0 \sum_{j\in S}c_{j,m_{j}}h_{j}T^{n_{j}+m_{j}}=0. Now partition the set S S of indices j j as S = ⨆ d S d S=\bigsqcup_{d}S_{d}, based on the value of n j + m j n_{j}+m_{j}, i.e., let S 1 S_{1} be those j ∈ S j\in S, for which n j + m j n_{j}+m_{j} is maximum, S 2 S_{2} be those j ∈ S ∖ S 1 j\in S\setminus S_{1}, for which n j + m j n_{j}+m_{j} is maximum in S ∖ S 1 S\setminus S_{1}, and so on. In particular, for j ∈ S d j\in S_{d} for a fixed d d, the value n j + m j n_{j}+m_{j} is constant. Then we see ∑ j ∈ S d c j, m j ​ h j ​ T n j + m j = 0 \sum_{j\in S_{d}}c_{j,m_{j}}h_{j}T^{n_{j}+m_{j}}=0 for each d d. Since h j h_{j} form a regular sequence in R R for j ∈ S d j\in S_{d} for any d d, we therefore obtain:

(5.3) |  | For j ∈ S d: c j, m j T m j + n j = ∑ l ∈ S d r 1 j ​ l h l; such that r j ​ l 1 = − r l ​ j 1, ∀ j, l ∈ S d. \displaystyle\text{For $j\in S_{d}$: }\ c_{j,m_{j}}T^{m_{j}+n_{j}}=\sum_{l\in S_{d}}r^{1}_{jl}h_{l};\ \text{ such that $r^{1}_{jl}=-r^{1}_{lj}$, $\forall j,l\in S_{d}$.} |  |

Furthermore, T m j + n j | r j ​ l 1 T^{m_{j}+n_{j}}\mid r^{1}_{jl} for all l ∈ S d l\in S_{d} if j ∈ S d j\in S_{d}, whereby c j, m j = ∑ l ∈ S d q j ​ l 1 ​ h l c_{j,m_{j}}=\sum_{l\in S_{d}}q^{1}_{jl}h_{l}, by letting q j ​ l 1 = r 1 ​ j ​ l / T n j + m j q^{1}_{jl}=r^{1}{jl}/T^{n_{j}+m_{j}}. Then:

(5.4) |  | ∑ j ∈ S d ( c j, m j − 1 ​ h j + c j, m j ​ F j, n j − 1) ​ T m j + n j − 1 = ∑ j ∈ S d ( c j, m j − 1 + ∑ l ∈ S d q l ​ j 1 ​ F l, n l − 1) ​ h j ​ T m j + n j − 1 \displaystyle\sum_{j\in S_{d}}(c_{j,m_{j}-1}h_{j}+c_{j,m_{j}}F_{j,n_{j}-1})T^{m_{j}+n_{j}-1}=\sum_{j\in S_{d}}(c_{j,m_{j}-1}+\sum_{l\in S_{d}}q^{1}_{lj}F_{l,n_{l}-1})h_{j}T^{m_{j}+n_{j}-1} |  |

Thus, letting c ~ j, m j − 1:= c j, m j − 1 + ∑ l ∈ S d q l ​ j 1 ​ F l, n l − 1 \tilde{c}_{j,m_{j}-1}:=c_{j,m_{j}-1}+\sum_{l\in S_{d}}q^{1}_{lj}F_{l,n_{l}-1}, we see

 | ∑ j ∈ S d ( c j, m j − 1 ​ h j + c j, m j ​ F j, n j − 1) ​ T m j + n j − 1 = ∑ j ∈ S d c ~ j, m j − 1 ​ h j ​ T m j + n j − 1. \sum_{j\in S_{d}}(c_{j,m_{j}-1}h_{j}+c_{j,m_{j}}F_{j,n_{j}-1})T^{m_{j}+n_{j}-1}=\sum_{j\in S_{d}}\tilde{c}_{j,m_{j}-1}h_{j}T^{m_{j}+n_{j}-1}. |  |

In general, let c ~ j, m j − k:= c j, m j − k + ∑ l ∈ S d q l ​ j 1 ​ F l, n l − k \tilde{c}_{j,m_{j}-k}:=c_{j,m_{j}-k}+\sum_{l\in S_{d}}q^{1}_{lj}F_{l,n_{l}-k} for all 1 ≤ k ≤ m j 1\leq k\leq m_{j}. Then using the fact q j ​ l 1 = − q l ​ j 1 q^{1}_{jl}=-q^{1}_{lj}, ∀ j, l ∈ S d \forall j,l\in S_{d}, one can check for all 0 ≤ l ≤ m j + n j 0\leq l\leq m_{j}+n_{j}:

 | ∑ j ∈ S d ( ∑ k = 0 l c j, m j − k ​ F j, n j − l + k) ​ T m j + n j − l = ∑ j ∈ S d ( ∑ k = 1 l c ~ j, m j − k ​ F j, n j − l + k) ​ T m j + n j − l, \sum_{j\in S_{d}}(\sum_{k=0}^{l}c_{j,m_{j}-k}F_{j,n_{j}-l+k})T^{m_{j}+n_{j}-l}=\sum_{j\in S_{d}}(\sum_{k=1}^{l}\tilde{c}_{j,m_{j}-k}F_{j,n_{j}-l+k})T^{m_{j}+n_{j}-l}, |  |

when ∑ j ∈ S d c j, m j ​ h j ​ T n j + m j = 0 \sum_{j\in S_{d}}c_{j,m_{j}}h_{j}T^{n_{j}+m_{j}}=0. Doing this for each S d S_{d} in the partition of S S, we can define c j ~ = ∑ p = 0 m j − 1 c ~ j, p ​ T p \tilde{c_{j}}=\sum_{p=0}^{m_{j}-1}\tilde{c}_{j,p}T^{p} for each j ∈ S j\in S to obtain ∑ j ∈ S c j ​ F j = ∑ j ∈ S c ~ j ​ F j \sum_{j\in S}c_{j}F_{j}=\sum_{j\in S}\tilde{c}_{j}F_{j}. Then starting with ∑ j ∈ S c ~ j ​ F j \sum_{j\in S}\tilde{c}_{j}F_{j} instead of ∑ j ∈ S c j ​ F j \sum_{j\in S}c_{j}F_{j} (in particular, c ~ j \tilde{c}_{j} ’s instead of c j c_{j} ’s), we repeat the above process. Clearly this process must terminate after finitely many steps since at each step we are strictly reducing the T T -degree of c j c_{j} ’s. When this process terminates, we obtain Dom ⁡ ( ∑ j ∈ S c j ​ F j) = Dom ⁡ ( ∑ j ∈ S Dom ⁡ ( c j) ​ Dom ⁡ ( F j)) \dom(\sum_{j\in S}c_{j}F_{j})=\dom(\sum_{j\in S}\dom(c_{j})\dom(F_{j})). This proves the lemma. ∎

Now we return to our goal of proving that h i h_{i} is a non-zero divisor in R / ( F 1, …, F i − 1) R/(F_{1},\dots,F_{i-1}). For this, suppose given the following equation in R R:

(5.5) |  | c i ​ h i = ∑ j = 1 i − 1 c j ​ F j, c_{i}h_{i}=\sum_{j=1}^{i-1}c_{j}F_{j}, |  |

we have to show c i ∈ ( F 1, …, F i − 1) ⊆ R c_{i}\in(F_{1},\dots,F_{i-1})\subseteq R. Applying Lemma 5.4, we can assume Dom ⁡ ( ∑ j = 1 i − 1 c j ​ F j) = Dom ⁡ ( ∑ j = 1 i − 1 Dom ⁡ ( c j) ​ Dom ⁡ ( F j)) \dom(\sum_{j=1}^{i-1}c_{j}F_{j})=\dom(\sum_{j=1}^{i-1}\dom(c_{j})\dom(F_{j})). Then taking Dom \dom of ( 5.5), we have:

(5.6) |  | Dom ⁡ ( c i) ​ h i = Dom ⁡ ( ∑ j = 1 i − 1 Dom ⁡ ( c j) ​ Dom ⁡ ( F j)) \dom(c_{i})h_{i}=\dom(\sum_{j=1}^{i-1}\dom(c_{j})\dom(F_{j})) |  |

Let Z ⊆ { 1, 2, …, i − 1 } Z\subseteq\{1,2,\dots,i-1\} be the subset of indices l l for which F l = h l F_{l}=h_{l}, i.e., n l = deg T ⁡ ( F l) = 0 n_{l}=\deg_{T}(F_{l})=0. Recall that for l ∉ Z l\notin Z, Dom ⁡ ( F l) = T n l ​ h l \dom(F_{l})=T^{n_{l}}h_{l}, where either n l = deg T ⁡ ( F l) = 2 ​ ( n − l) n_{l}=\deg_{T}(F_{l})=2(n-l) for all l ∉ Z l\notin Z or n l = deg T ⁡ ( F l) = n − l n_{l}=\deg_{T}(F_{l})=n-l for all l ∉ Z l\notin Z (depending on whether j i j_{i} equals or not equals n n). In particular, for l ∉ Z l\notin Z, we can arrange the degrees n l n_{l} in strictly decreasing order, i.e., let { 1, 2, …, i − 1 } ∖ Z = { u 1, u 2, …, u k } \{1,2,\dots,i-1\}\setminus Z=\{u_{1},\ u_{2},\ \dots,\ u_{k}\} (where k = i − 1 − | Z | k=i-1-|Z|) such that n u 1 > n u 2 > ⋯ > n u k > 0 n_{u_{1}}>n_{u_{2}}>\dots>n_{u_{k}}>0. Let m i = deg T ⁡ ( c i) m_{i}=\deg_{T}(c_{i}). Then we can rewrite ( 5.6) as:

(5.7) |  | Dom ⁡ ( c i) ​ h i = Dom ⁡ ( ∑ j = 1 i − 1 Dom ⁡ ( c j) ​ T n j ​ h j), \dom(c_{i})h_{i}=\dom(\sum_{j=1}^{i-1}\dom(c_{j})T^{n_{j}}h_{j}), |  |

where deg T ⁡ ( Dom ⁡ ( c i)) = m i \deg_{T}(\dom(c_{i}))=m_{i}. Since h 1, …, h i h_{1},\dots,h_{i} form a regular sequence in R R, ( 5.7) implies that Dom ⁡ ( c i) = ∑ j = 1 i − 1 b j 1 ​ h j \dom(c_{i})=\sum_{j=1}^{i-1}b^{1}_{j}h_{j}, for b j 1 ∈ R b^{1}_{j}\in R such that T m i | b j 1 T^{m_{i}}\mid b^{1}_{j} for all 1 ≤ j ≤ i − 1 1\leq j\leq i-1. Now as long as 𝐦 𝐢 ≥ 𝐧 𝐮 𝟏 \mathbf{m_{i}\geq n_{u_{1}}}, let c i ′:= c i − ∑ j = 1 i − 1 b j 1 T n j ​ F j c_{i}^{\prime}:=c_{i}-\sum_{j=1}^{i-1}\frac{b^{1}_{j}}{T^{n_{j}}}F_{j}. Then either c i ′ = 0 c_{i}^{\prime}=0, in which case we are done, else c i ′ ≠ 0 c_{i}^{\prime}\neq 0 and

 | c i ′ ​ h i = ∑ j = 1 i − 1 ( c j − b j 1 ​ h i T n j) ​ F j, c_{i}^{\prime}h_{i}=\sum_{j=1}^{i-1}(c_{j}-\frac{b^{1}_{j}h_{i}}{T^{n_{j}}})F_{j}, |  |

which is an equation in R R of the form ( 5.5), but with Dom ⁡ ( c i ′) < Dom ⁡ ( c i) \dom(c_{i}^{\prime})<\dom(c_{i}). Iterating this process, we either reach c i ∈ ( F 1, …, F i − 1) ⊆ R c_{i}\in(F_{1},\dots,F_{i-1})\subseteq R, in which case we are done, or n u 2 ≤ deg T ⁡ ( c i) ≤ n u 1 − 1 n_{u_{2}}\leq\deg_{T}(c_{i})\leq n_{u_{1}}-1. Then taking Dom \dom of the new ( 5.5), we obtain ( 5.7), but with deg T ⁡ ( Dom ⁡ ( c i)) = m i ≤ n u 1 − 1 \deg_{T}(\dom(c_{i}))=m_{i}\leq n_{u_{1}}-1. Then from ( 5.7), we see that Dom ⁡ ( c u 1) ​ h u 1 ​ T n u 1 \dom(c_{u_{1}})h_{u_{1}}T^{n_{u_{1}}} gets cancelled, i.e., either Dom ⁡ ( c u 1) = 0 \dom(c_{u_{1}})=0 or there exists a subset S ⊆ { 1, 2, …, i − 1 } S\subseteq\{1,2,\dots,i-1\} such that u 1 ∈ S u_{1}\in S and ∑ j ∈ S Dom ⁡ ( c j) ​ h j ​ T n j = 0 \sum_{j\in S}\dom(c_{j})h_{j}T^{n_{j}}=0. Then applying Lemma 5.4 to this subset S S, we can reduce Dom ⁡ ( c u 1) \dom(c_{u_{1}}). Since m i < n u 1 m_{i}<n_{u_{1}}, we can iterate this process, until deg T ⁡ ( Dom ⁡ ( c u 1)) = 0 \deg_{T}(\dom(c_{u_{1}}))=0 or equivalently c u 1 ∈ 𝕂 ⁡ [x 1, …, x n − 1] c_{u_{1}}\in\mathbb{K}[x_{1},\dots,x_{n-1}]. Then we have

(5.8) |  |  | c u 1 h u 1 T n u 1 + ∑ j ∈ S ∖ { u 1 } Dom ( c j) h j T n j = 0 ⟹ c u 1 T n u 1 = − ∑ j ∈ S ∖ { u 1 } e j h j, \displaystyle c_{u_{1}}h_{u_{1}}T^{n_{u_{1}}}+\sum_{j\in S\setminus\{u_{1}\}}\dom(c_{j})h_{j}T^{n_{j}}=0\implies c_{u_{1}}T^{n_{u_{1}}}=-\sum_{j\in S\setminus\{u_{1}\}}e_{j}h_{j}, |  |

for some e j ∈ R e_{j}\in R such that e j = e j ′ ​ T n u 1 e_{j}=e_{j}^{\prime}T^{n_{u_{1}}} for e j ′ ∈ 𝕂 ⁡ [x 1, …, x n − 1] e_{j}^{\prime}\in\mathbb{K}[x_{1},\dots,x_{n-1}]. This is because { h j } j ∈ S \{h_{j}\}_{j\in S} forms a regular sequence in R R and c u 1 ∈ 𝕂 ⁡ [x 1, …, x n − 1] c_{u_{1}}\in\mathbb{K}[x_{1},\dots,x_{n-1}]. Then

 | c u 1 ​ h u 1 ​ T n u 1 + ∑ j ∈ S ∖ { u 1 } Dom ⁡ ( c j) ​ h j ​ T n j = ∑ j ∈ S ∖ { u 1 } ( Dom ⁡ ( c j) − e j ′ ​ h u 1 ​ T n u 1 − n j) ​ h j ​ T n j c_{u_{1}}h_{u_{1}}T^{n_{u_{1}}}+\sum_{j\in S\setminus\{u_{1}\}}\dom(c_{j})h_{j}T^{n_{j}}=\sum_{j\in S\setminus\{u_{1}\}}(\dom(c_{j})-e^{\prime}_{j}h_{u_{1}}T^{n_{u_{1}}-n_{j}})h_{j}T^{n_{j}} |  |

So ( 5.7) becomes

(5.9) |  |  | Dom ⁡ ( c i) ​ h i = Dom ⁡ ( ∑ j ∈ S ∖ { u 1 } ( Dom ⁡ ( c j) − e j ′ ​ h u 1 ​ T n u 1 − n j) ​ T n j ​ h j + ∑ j ∉ S Dom ⁡ ( c j) ​ T n j ​ h j) \displaystyle\dom(c_{i})h_{i}=\dom(\sum_{j\in S\setminus\{u_{1}\}}(\dom(c_{j})-e^{\prime}_{j}h_{u_{1}}T^{n_{u_{1}}-n_{j}})T^{n_{j}}h_{j}+\sum_{j\notin S}\dom(c_{j})T^{n_{j}}h_{j}) |  |

(5.10) |  |  | ⟹ Dom ⁡ ( c i) = ∑ j = 1 j ≠ u 1 i − 1 b j 2 ​ h j, \displaystyle\implies\dom(c_{i})=\sum_{\begin{subarray}{c}j=1\\ j\neq u_{1}\end{subarray}}^{i-1}b^{2}_{j}h_{j}, |  |

for b j 2 ∈ R b^{2}_{j}\in R such that T m i | b j 2 T^{m_{i}}\mid b^{2}_{j} for all j ≠ u 1 j\neq u_{1}, since { h j ∣ 1 ≤ j ≤ i − 1 ​ and ​ j ≠ u 1 } \{h_{j}\mid\ 1\leq j\leq i-1\ \text{and}\ j\neq u_{1}\} is a regular sequence in R R. Then as long as 𝐦 𝐢 ≥ 𝐧 𝐮 𝟐 \mathbf{m_{i}\geq n_{u_{2}}}, letting c i ′:= c i − ∑ j ≠ u 1 b j 2 T n j ​ F j c_{i}^{\prime}:=c_{i}-\sum_{j\neq u_{1}}\frac{b^{2}_{j}}{T^{n_{j}}}F_{j} we can repeat the above process. This same process can be iterated for all n u l ≤ m i ≤ m u l − 1 − 1 n_{u_{l}}\leq m_{i}\leq m_{u_{l-1}-1} (for 2 ≤ l ≤ k 2\leq l\leq k) and finally for m i ≥ n u k m_{i}\geq n_{u_{k}}, till we either have c i ∈ ( F 1, …, F i − 1) ⊆ R c_{i}\in(F_{1},\dots,F_{i-1})\subseteq R or obtain ( 5.5), i.e.,

 | c i ​ h i = ∑ j ∈ Z c j ​ F j + ∑ j ∉ Z c j ​ F j, c_{i}h_{i}=\sum_{j\in Z}c_{j}F_{j}+\sum_{j\notin Z}c_{j}F_{j}, |  |

with 0 < m i = deg T ⁡ ( c i) ≤ n u k − 1 0<m_{i}=\deg_{T}(c_{i})\leq n_{u_{k}}-1. Then by Lemma 5.4, there exist c ~ j \tilde{c}_{j} for all 1 ≤ j ≤ i − 1 1\leq j\leq i-1, such that c i ​ h i = ∑ j ∈ Z c ~ j ​ F j + ∑ j ∉ Z c ~ j ​ F j c_{i}h_{i}=\sum_{j\in Z}\tilde{c}_{j}F_{j}+\sum_{j\notin Z}\tilde{c}_{j}F_{j} and Dom ⁡ ( c i) ​ h i = Dom ⁡ ( ∑ j ∈ Z Dom ⁡ ( c ~ j) ​ h j + ∑ j ∉ Z Dom ⁡ ( c ~ j) ​ T n j ​ h j) \dom(c_{i})h_{i}=\dom(\sum_{j\in Z}\dom(\tilde{c}_{j})h_{j}+\sum_{j\notin Z}\dom(\tilde{c}_{j})T^{n_{j}}h_{j}). Then since n j > m i n_{j}>m_{i} for all j ∉ Z j\notin Z, there exists a subset S ⊆ { 1, 2 ​ …, i − 1 } S\subseteq\{1,2\dots,i-1\} such that { 1, 2, …, i − 1 } ∖ Z ⊆ S \{1,2,\dots,i-1\}\setminus Z\subseteq S and ∑ j ∈ S Dom ⁡ ( c ~ j) ​ Dom ⁡ ( F j) = 0 \sum_{j\in S}\dom(\tilde{c}_{j})\dom(F_{j})=0. Then applying Lemma 5.4 to this subset S S, we can reduce deg T ⁡ ( Dom ⁡ ( c j ~)) \deg_{T}(\dom(\tilde{c_{j}})) for all j ∉ Z j\notin Z. We can iterate this until we reach deg T ⁡ ( Dom ⁡ ( c ~ j)) = 0 \deg_{T}(\dom(\tilde{c}_{j}))=0 for all j ∉ Z j\notin Z, since m i < n j m_{i}<n_{j} for all j ∉ Z j\notin Z. Thus, we are reduced to the equation

(5.11) |  | c i ​ h i = ∑ j ∈ Z c j ​ F j + ∑ j ∉ Z c j ​ F j, c_{i}h_{i}=\sum_{j\in Z}c_{j}F_{j}+\sum_{j\notin Z}c_{j}F_{j}, |  |

where deg T ⁡ ( c i) = m i < n u k \deg_{T}(c_{i})=m_{i}<n_{u_{k}} and c j ∈ 𝕂 ⁡ [x 1, …, x n − 1] c_{j}\in\mathbb{K}[x_{1},\dots,x_{n-1}] for all j ∉ Z j\notin Z. Now we have two cases.

Case I: ( Z = ∅ Z=\emptyset) If Z = ∅ Z=\emptyset, then we have the equation c i ​ h i = ∑ j = 1 i − 1 c j ​ F j c_{i}h_{i}=\sum_{j=1}^{i-1}c_{j}F_{j}, where c j ∈ 𝕂 ⁡ [x 1, …, x n − 1] c_{j}\in\mathbb{K}[x_{1},\dots,x_{n-1}]. Furthermore, we have either of the following:

1. (1)

when j i ≠ n j_{i}\neq n: deg T ⁡ ( F j) = 2 ​ ( n − j) \deg_{T}(F_{j})=2(n-j) for all 1 ≤ j ≤ i − 1 1\leq j\leq i-1 and deg T ⁡ ( c i) < 2 ​ ( n − i + 1) = min 1 ≤ j ≤ i − 1 ⁡ deg T ⁡ ( F j) \deg_{T}(c_{i})<2(n-i+1)=\min_{1\leq j\leq i-1}\deg_{T}(F_{j}).

2. (2)

when j i = n j_{i}=n: deg T ⁡ ( F j) = n − j \deg_{T}(F_{j})=n-j for all 1 ≤ j ≤ i − 1 1\leq j\leq i-1 and deg T ⁡ ( c i) < n − i + 1 = min 1 ≤ j ≤ i − 1 ⁡ deg T ⁡ ( F j) \deg_{T}(c_{i})<n-i+1=\min_{1\leq j\leq i-1}\deg_{T}(F_{j}).

In any of the above cases ( 1) (1) or ( 2) (2), coefficient of T deg T ⁡ ( F 1) T^{\deg_{T}(F_{1})} in c i ​ h i c_{i}h_{i} is 0 0, while that in ∑ j = 1 i − 1 c j ​ F j \sum_{j=1}^{i-1}c_{j}F_{j} is c 1 ​ h 1 c_{1}h_{1}. Thus, we must have c 1 = 0 c_{1}=0. Now we are reduced to c i ​ h i = ∑ j = 2 i − 1 c j ​ F j c_{i}h_{i}=\sum_{j=2}^{i-1}c_{j}F_{j}, but then comparing the coefficients of T deg T ⁡ ( F 2) T^{\deg_{T}(F_{2})} on either side, we see c 2 = 0 c_{2}=0. Repeating this process, we see c j = 0 c_{j}=0 for all 1 ≤ j ≤ i − 1 1\leq j\leq i-1. Thus, we must have c i = 0 c_{i}=0, whence we are done by virtue of the previous reduction processes.

Case II: ( Z ≠ ∅ Z\neq\emptyset) Since F j = h j F_{j}=h_{j} for j ∈ Z j\in Z, we can rewrite ( 5.11) as c i ​ h i − ∑ j ∈ Z c j ​ h j = ∑ j ∉ Z c j ​ F j c_{i}h_{i}-\sum_{j\in Z}c_{j}h_{j}=\sum_{j\notin Z}c_{j}F_{j}. Now we take Dom \dom of this equation and note that since h j ∈ 𝕂 ⁡ [x 1, …, x n − 1] h_{j}\in\mathbb{K}[x_{1},\dots,x_{n-1}], we have Dom ⁡ ( c i ​ h i − ∑ j ∈ Z c j ​ h j) = Dom ⁡ ( Dom ⁡ ( c i) ​ h i − ∑ j ∈ Z Dom ⁡ ( c j) ​ h j) \dom(c_{i}h_{i}-\sum_{j\in Z}c_{j}h_{j})=\dom(\dom(c_{i})h_{i}-\sum_{j\in Z}\dom(c_{j})h_{j}). Furthermore, since c j ∈ 𝕂 ⁡ [x 1, …, x n − 1] c_{j}\in\mathbb{K}[x_{1},\dots,x_{n-1}] and deg T ⁡ ( F j) \deg_{T}(F_{j}) are all distinct for j ∉ Z j\notin Z, with max j ∉ Z ⁡ deg T ⁡ ( F j) = deg T ⁡ ( F u 1) \max_{j\notin Z}\deg_{T}(F_{j})=\deg_{T}(F_{u_{1}}), we see that Dom ⁡ ( ∑ j ∉ Z c j ​ F j) = c u 1 ​ Dom ⁡ ( F u 1) = c u 1 ​ T n u 1 ​ h u 1 \dom(\sum_{j\notin Z}c_{j}F_{j})=c_{u_{1}}\dom(F_{u_{1}})=c_{u_{1}}T^{n_{u_{1}}}h_{u_{1}}. So we obtain:

(5.12) |  | Dom ⁡ ( Dom ⁡ ( c i) ​ h i − ∑ j ∈ Z Dom ⁡ ( c j) ​ h j) = c u 1 ​ T n u 1 ​ h u 1 \dom(\dom(c_{i})h_{i}-\sum_{j\in Z}\dom(c_{j})h_{j})=c_{u_{1}}T^{n_{u_{1}}}h_{u_{1}} |  |

Since deg T ⁡ ( Dom ⁡ ( c i)) < n u k < n u 1 \deg_{T}(\dom(c_{i}))<n_{u_{k}}<n_{u_{1}}, we must have

(5.13) |  | Dom ( − ∑ j ∈ Z Dom ( c j) h j) = c u 1 T n u 1 h u 1 \dom(-\sum_{j\in Z}\dom(c_{j})h_{j})=c_{u_{1}}T^{n_{u_{1}}}h_{u_{1}} |  |

Then like before, we see that c u 1 ​ T n u 1 = ∑ j ∈ Z w j 1 ​ h j c_{u_{1}}T^{n_{u_{1}}}=\sum_{j\in Z}w^{1}_{j}h_{j}, where w j 1 = v j 1 ​ T n u 1 w^{1}_{j}=v^{1}_{j}T^{n_{u_{1}}} with v j 1 ∈ 𝕂 ⁡ [x 1, …, x n − 1] v^{1}_{j}\in\mathbb{K}[x_{1},\dots,x_{n-1}] for all j ∈ Z j\in Z. Then we see that c u 1 ​ F u 1 = ∑ j ∈ Z v j 1 ​ F u 1 ​ h j c_{u_{1}}F_{u_{1}}=\sum_{j\in Z}v^{1}_{j}F_{u_{1}}h_{j}. So we can rewrite ( 5.11) as

 | c i ​ h i − ∑ j ∈ Z ( c j + v j 1 ​ F u 1) ​ h j = ∑ j = 2 k c u j ​ F u j. c_{i}h_{i}-\sum_{j\in Z}(c_{j}+v^{1}_{j}F_{u_{1}})h_{j}=\sum_{j=2}^{k}c_{u_{j}}F_{u_{j}}. |  |

Since Dom ⁡ ( ∑ l = 2 k c u l ​ F u l) = c u 2 ​ T n u 2 ​ h u 2 \dom(\sum_{l=2}^{k}c_{u_{l}}F_{u_{l}})=c_{u_{2}}T^{n_{u_{2}}}h_{u_{2}} and deg T ⁡ ( c i) = m i < n u 2 \deg_{T}(c_{i})=m_{i}<n_{u_{2}}, we can repeat the above process again. Iterating this process, for all 1 ≤ l ≤ k 1\leq l\leq k, we obtain c u l ​ T n u l = ∑ j ∈ Z w j l ​ h j c_{u_{l}}T^{n_{u_{l}}}=\sum_{j\in Z}w^{l}_{j}h_{j}, where w j l = v j l ​ T n u 1 w^{l}_{j}=v^{l}_{j}T^{n_{u_{1}}} with v j l ∈ 𝕂 ⁡ [x 1, …, x n − 1] v^{l}_{j}\in\mathbb{K}[x_{1},\dots,x_{n-1}] for all j ∈ Z j\in Z. Thus, ( 5.11) reduces to:

(5.14) |  | c i ​ h i = ∑ j ∈ Z ( c j + ∑ l = 1 k v j l ​ F u l) ​ h j. c_{i}h_{i}=\sum_{j\in Z}(c_{j}+\sum_{l=1}^{k}v^{l}_{j}F_{u_{l}})h_{j}. |  |

Then since { h j ∣ j ∈ Z } ∪ { h i } \{h_{j}\mid\ j\in Z\}\cup\{h_{i}\} form a regular sequence in R R, it follows that c i ∈ ( h j ∣ j ∈ Z) = ( F j ∣ j ∈ Z) ⊆ R c_{i}\in(h_{j}\mid\ j\in Z)=(F_{j}\mid j\in Z)\subseteq R.

Thus, this completes the proof that if we have a relation in R R of the form ( 5.5), then c i ∈ ( F 1, …, F i − 1) ⊆ R c_{i}\in(F_{1},\dots,F_{i-1})\subseteq R, thereby proving that h i h_{i} is a non-zero divisor in R / ( F 1, …, F i − 1) R/(F_{1},\dots,F_{i-1}). As derived earlier, this implies H 1, …, H i H_{1},\dots,H_{i} is a regular sequence in R ⁡ [1 1 − 2 ​ T] R[\frac{1}{1-2T}], thereby proving the proposition by induction.

∎

###### Remark 5.5.

Since h 1, …, h n − 1 h_{1},\dots,h_{n-1} is a regular sequence of homogeneous polynomials in the ring R = 𝕂 ⁡ [x 1, …, x n − 1, T] R=\mathbb{K}[x_{1},\dots,x_{n-1},T], it follows that h 1 ​ y 1, …, h n − 1 ​ y n − 1 h_{1}y_{1},\dots,h_{n-1}y_{n-1} form a regular sequence in R ⁡ [y 1, …, y n − 1] R[y_{1},\dots,y_{n-1}] by [17] *Lemma 10.68.10. Then a similar argument as that in the proof of Proposition 5.3 yields that y 1 ​ Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, y n − 1 ​ Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1) y_{1}\Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ y_{n-1}\Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}) forms a regular sequence in R ⁡ [1 1 − 2 ​ T] ​ [y 1, …, y n − 1] R[\frac{1}{1-2T}][y_{1},\dots,y_{n-1}] for any choice of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. Again by [17] *Lemma 10.68.10 it follows that any subsequence of the sequence in Proposition 5.3 is a regular sequence.

We now prove Theorem A using Proposition 5.3.

###### Theorem 5.6.

Let 𝕂 \mathbb{K} be any algebraically closed field. For n ≥ 3 n\geq 3, we have dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) ≤ 2 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})\leq 2.

###### Proof.

Recall the 𝕂 \mathbb{K} -algebra homomorphisms Φ #​ [T] j: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1, T] \Phi^{\#}[T]_{j}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1},T] induced by Φ #​ [T] j ​ ( x i) = x i − T ​ x j \Phi^{\#}[T]_{j}(x_{i})=x_{i}-Tx_{j} for all i ≠ j i\neq j and Φ #​ [T] j ​ ( x j) = ( 1 − 2 ​ T) ​ x j \Phi^{\#}[T]_{j}(x_{j})=(1-2T)x_{j}. For j = n j=n, recall that Φ #​ [T] n: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1, T] \Phi^{\#}[T]_{n}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1},T] is the natural inclusion of 𝕂 \mathbb{K} -algebras. Now note the following natural 𝕂 \mathbb{K} -algebra homomorphism, generated by sending T T to its image in the quotient:

(5.15) |  | 𝕂 ⁡ [T] → 𝜑 𝒪 ⁡ ( j 1, …, j n − 1):= 𝕂 ⁡ [x 1, …, x n − 1, T] ( Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)). \mathbb{K}[T]\xlongrightarrow{\varphi}\mathcal{O}(j_{1},\dots,j_{n-1}):=\frac{\mathbb{K}[x_{1},\dots,x_{n-1},T]}{(\Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}))}. |  |

Let Y ⁡ ( j 1, …, j n − 1):= Spec ⁡ ( 𝒪 ⁡ ( j 1, …, j n − 1)) Y(j_{1},\dots,j_{n-1}):=\spec(\mathcal{O}(j_{1},\dots,j_{n-1})), whereby we obtain the induced morphism φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}^{1}_{\mathbb{K}} of 1 1 -dimensional affine 𝕂 \mathbb{K} -schemes. We first note that φ ⋆ \varphi^{\star} is surjective since for each α ∈ 𝔸 𝕂 1 ​ ( 𝕂) \alpha\in\mathbb{A}^{1}_{\mathbb{K}}(\mathbb{K}), the fiber Y ​ ( j 1, …, j n − 1) α:= Y ⁡ ( j 1, …, j n − 1) × 𝔸 𝕂 1 Spec ⁡ ( 𝕂 ⁡ [T] / ( T − α)) Y(j_{1},\dots,j_{n-1})_{\alpha}:=Y(j_{1},\dots,j_{n-1})\times_{\mathbb{A}^{1}_{\mathbb{K}}}\spec(\mathbb{K}[T]/(T-\alpha)) equals

 | Y ​ ( j 1, …, j n − 1) α = Spec ⁡ 𝕂 ⁡ [x 1, …, x n − 1] ( Φ #​ [α] j 1 ​ ( HD n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [α] j n − 1 ​ ( HD n − 1 n − 2 ​ 𝐱 n − 1)), Y(j_{1},\dots,j_{n-1})_{\alpha}=\spec\frac{\mathbb{K}[x_{1},\dots,x_{n-1}]}{(\Phi^{\#}[\alpha]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[\alpha]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}))}, |  |

which is non-empty since, for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1, each Φ #​ [α] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) \Phi^{\#}[\alpha]_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}) obtained by substituting T = α T=\alpha is a homogeneous polynomial in x 1, …, x n − 1 x_{1},\dots,x_{n-1}. Note that Φ #​ [1] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) = Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) \Phi^{\#}[1]_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})=\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}) for 0 < i < n 0<i<n, whence ⋂ i = 1 n − 1 V ⁡ ( Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) CLOSE \bigcap_{i=1}^{n-1}V(\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}) is the set of 𝕂 \mathbb{K} -rational points of the fiber Y ​ ( j 1, …, j n − 1) 1 Y(j_{1},\dots,j_{n-1})_{1} over 1 1. Now let

(5.16) |  | 𝒪 ​ ( j 1, …, j n − 1) 1 = 𝕂 ⁡ [x 1, …, x n − 1, T] ( Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1), T − 1), \displaystyle\mathcal{O}(j_{1},\dots,j_{n-1})_{1}=\frac{\mathbb{K}[x_{1},\dots,x_{n-1},T]}{(\Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}),T-1)}, |  |

whereby Y ​ ( j 1, …, j n − 1) 1 = Spec ⁡ 𝒪 ​ ( j 1, …, j n − 1) 1 Y(j_{1},\dots,j_{n-1})_{1}=\spec\mathcal{O}(j_{1},\dots,j_{n-1})_{1}. But now note that

(5.17) |  | dim 𝒪 ​ ( j 1, …, j n − 1) 1 = dim 𝕂 ⁡ [x 1, …, x n − 1, T, 1 1 − 2 ​ T] ( Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1), T − 1), \displaystyle\dim\mathcal{O}(j_{1},\dots,j_{n-1})_{1}=\dim\frac{\mathbb{K}[x_{1},\dots,x_{n-1},T,\frac{1}{1-2T}]}{(\Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}),T-1)}, |  |

since no prime ideal ideal of 𝕂 ⁡ [x 1, …, x n − 1, T] \mathbb{K}[x_{1},\dots,x_{n-1},T] can contain T − 1 T-1 and 1 − 2 ​ T 1-2T together. But by Proposition 5.3, the ring

 | 𝕂 ⁡ [x 1, …, x n − 1, T, 1 1 − 2 ​ T] ( Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)) \frac{\mathbb{K}[x_{1},\dots,x_{n-1},T,\frac{1}{1-2T}]}{(\Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}))} |  |

is a 1 1 -dimensional Cohen-Macaulay ring. This along with ( 5.16) implies that Y ​ ( j 1, …, j n − 1) 1 Y(j_{1},\dots,j_{n-1})_{1} is at most 1 1 -dimensional, and thus so is ⋂ i = 1 n − 1 V ⁡ ( Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) CLOSE \bigcap_{i=1}^{n-1}V(\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}) for any choice of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. Thus dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) ≤ 2 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})\leq 2 by ( 5.1), since all fibers of the shift projection map 𝔭 n: 𝔸 𝕂 n ​ ( 𝕂) → Z n n ​ ( 𝕂) \mathfrak{p}_{n}:\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K})\rightarrow Z^{n}_{n}(\mathbb{K}) are 1 1 -dimensional. ∎

###### Corollary 5.7.

X n ​ ( 𝕂) X_{n}(\mathbb{K}) is finite for all fields 𝕂 \mathbb{K} and n ≥ 3 n\geq 3, where X n X_{n} is the arithmetic Casas-Alvero scheme.

###### Proof.

It suffices to assume 𝕂 \mathbb{K} to be algebraically closed. Recalling the definition of the shift projection map 𝔭 n: 𝔸 n ​ ( 𝕂) → Z n n ​ ( 𝕂) \mathfrak{p}_{n}:\mathbb{A}^{n}(\mathbb{K})\rightarrow Z^{n}_{n}(\mathbb{K}), we see by( 5.1):

(5.18) |  | 𝒱 ^ n ​ ( 𝕂) = V ⁡ ( x n) ∩ ( ⋂ i = 1 n − 1 X n i ​ ( 𝕂)) = ⋃ 1 ≤ j 1, …, j n − 1 ≤ n ⋂ i = 1 n − 1 V n − 1 n ​ ( Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)). \widehat{\mathcal{V}}_{n}(\mathbb{K})=V(x_{n})\cap(\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}))=\bigcup_{1\leq j_{1},\dots,j_{n-1}\leq n}\bigcap_{i=1}^{n-1}V^{n}_{n-1}(\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})). |  |

Thus, by Theorem 5.6, 𝒱 ^ n ​ ( 𝕂) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \widehat{\mathcal{V}}_{n}(\mathbb{K})\subseteq\mathbb{A}_{\mathbb{K}}^{n}(\mathbb{K}) is 1 1 -dimensional. This is equivalent to 𝒱 n ​ ( 𝕂) ⊆ ℙ 𝕂 n − 1 ​ ( 𝕂) \mathcal{V}_{n}(\mathbb{K})\subseteq\mathbb{P}^{n-1}_{\mathbb{K}}(\mathbb{K}) being a finite set of points. By Proposition 4.14, X n ​ ( 𝕂) = ν ¯ n ​ ( 𝒱 n ​ ( 𝕂)) X_{n}(\mathbb{K})=\overline{\nu}_{n}(\mathcal{V}_{n}(\mathbb{K})), implying X n ​ ( 𝕂) X_{n}(\mathbb{K}) is finite. ∎

###### Corollary 5.8.

X n X_{n} is a finite ℤ \mathbb{Z} -scheme of dimension ≤ 1 \leq 1 for all n ≥ 3 n\geq 3. In particular, X n X_{n} is affine.

###### Proof.

Corollary 5.7 implies that X n × Spec ⁡ ℤ Spec ⁡ 𝕂 X_{n}\times_{\spec\mathbb{Z}}\spec\mathbb{K} is a finite 𝕂 \mathbb{K} -scheme for all fields 𝕂 \mathbb{K}. In particular, we note that the fibers ϕ n − 1 ​ ( p) \phi_{n}^{-1}(p) of the structure morphism ϕ n: X n → Spec ⁡ ℤ \phi_{n}:X_{n}\rightarrow\spec\mathbb{Z} are finite ℤ / p ​ ℤ \mathbb{Z}/p\mathbb{Z} -schemes for all p ∈ Spec ⁡ ℤ p\in\spec\mathbb{Z}. Thus, ϕ n \phi_{n} is a quasi-finite proper morphism of schemes. By [17] *Lemma 37.44.1 (or [8]), ϕ n \phi_{n} is a finite morphism. For quasi-compactness of X n X_{n}, note that ϕ n \phi_{n} is an affine morphism by [9] *Ex II.5.17 and therefore, X n = ϕ n − 1 ​ ( Spec ⁡ ℤ) X_{n}=\phi_{n}^{-1}(\spec\mathbb{Z}) is affine. The dimension bound follows from [17] *Lemma 29.44.9. ∎

###### Remark 5.9.

If ϕ n: X n → Spec ⁡ ℤ \phi_{n}:X_{n}\rightarrow\spec\mathbb{Z} is surjective, then dim X n = 1 \dim X_{n}=1 by [17] *Lemma 29.44.9. Conversely, if ϕ n \phi_{n} is not surjective, then since Im ⁡ ϕ n \operatorname{Im}\phi_{n} is a finite subset of Spec ⁡ ℤ \spec\mathbb{Z}, it follows that dim X n = 0 \dim X_{n}=0. Thus, Conjecture CA is true in degree n n if and only if dim X n = 0 \dim X_{n}=0.

###### Remark 5.10.

Let A n:= Γ ⁡ ( X n, 𝒪 X n) A_{n}:=\Gamma(X_{n},\mathcal{O}_{X_{n}}). Then by Corollary 5.8 X n = Spec ⁡ ( A n) X_{n}=\spec(A_{n}) and A n A_{n} is finitely generated as a ℤ \mathbb{Z} -module. Thus, A n = ℤ r n ⊕ T A_{n}=\mathbb{Z}^{r_{n}}\oplus T as ℤ \mathbb{Z} -modules, where T T is the torsion part of A n A_{n}. Thus, conjecture CA over characteristic 0 0 in degree n n is equivalent to A n A_{n} being torsion as a ℤ \mathbb{Z} -module. In that case, the set of bad primes for the conjecture in degree n n (as defined in [15]) is equal to the set of primes occurring in the primary decomposition of A n A_{n} as a ℤ \mathbb{Z} -module.

We can further strengthen Corollary 5.7 to give a cohomological upper bound on the size of X n ​ ( 𝕂) X_{n}(\mathbb{K}) for any field 𝕂 \mathbb{K}.

###### Corollary 5.11.

Let X n ​ ( j 1, …, j n − 1):= Y ​ ( j 1, …, j n − 1) 1 X_{n}(j_{1},\dots,j_{n-1}):=Y(j_{1},\dots,j_{n-1})_{1} for all 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. Let h c i ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ):= dim ℚ ℓ H c i ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ) h^{i}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell}):=\dim_{\mathbb{Q}_{\ell}}H^{i}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell}), where H c i ​ ( −, ℚ ℓ) H^{i}_{c}(-,\mathbb{Q}_{\ell}) denotes ℓ \ell -adic cohomology with compact support. Then for any field 𝕂 \mathbb{K} such that ℓ \ell is coprime to the characteristic of 𝕂 \mathbb{K}, we have:

 | | X n ​ ( 𝕂) | ≤ ∑ 1 ≤ j 1, …, j n − 1 ≤ n h c 2 ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ). |X_{n}(\mathbb{K})|\leq\sum_{1\leq j_{1},\dots,j_{n-1}\leq n}h^{2}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell}). |  |

###### Proof.

We assume 𝕂 \mathbb{K} is algebraically closed. Let ℓ \ell be a prime coprime to characteristic of 𝕂 \mathbb{K}. Let X n ​ ( j 1, …, j n − 1):= ⋂ i = 1 n − 1 V n − 1 n ​ ( Φ j i #​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) ⊂ 𝔸 𝕂 n X_{n}(j_{1},\dots,j_{n-1}):=\bigcap_{i=1}^{n-1}V^{n}_{n-1}(\Phi^{\#}_{j_{i}}(HD^{i-1}_{n-1}\mathbf{x}_{n-1}))\subset\mathbb{A}^{n}_{\mathbb{K}} for any 1 ≤ j 1, j 2, …, j n − 1 ≤ n 1\leq j_{1},\ j_{2},\dots,\ j_{n-1}\leq n. By Proposition 5.3, X n ​ ( j 1, …, j n − 1) X_{n}(j_{1},\dots,j_{n-1}) is at most 1 1 -dimensional. If dim X n ​ ( j 1, …, j n − 1) = 1 \dim X_{n}(j_{1},\dots,j_{n-1})=1, then by [14] *Corollary 7.5.21, the number of irreducible components of X n ​ ( j 1, …, j n − 1) X_{n}(j_{1},\dots,j_{n-1}) is equal to h c 2 ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ) h^{2}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell}). Similarly, if dim X n ​ ( j 1, …, j n − 1) = 0 \dim X_{n}(j_{1},\dots,j_{n-1})=0, then X n ​ ( j 1, …, j n − 1) r ​ e ​ d ≅ Spec ⁡ 𝕂 X_{n}(j_{1},\dots,j_{n-1})_{red}\cong\spec\mathbb{K}, and one can see that H c 2 ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ) = 0 H^{2}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell})=0, which has ℚ ℓ \mathbb{Q}_{\ell} -dimension 0 0. From ( 5.18) we see that the number N N of irreducible components of 𝒱 ^ n ​ ( 𝕂) \widehat{\mathcal{V}}_{n}(\mathbb{K}) is upper bounded by:

(5.19) |  | N ≤ ∑ 1 ≤ j 1, …, j n − 1 ≤ n h c 2 ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ). N\leq\sum_{1\leq j_{1},\dots,j_{n-1}\leq n}h^{2}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell}). |  |

From the definition of 𝒱 n ​ ( 𝕂) \mathcal{V}_{n}(\mathbb{K}) (see Proposition 4.14, it follows that | 𝒱 n ​ ( 𝕂) | = N |\mathcal{V}_{n}(\mathbb{K})|=N. Furthermore, X n ​ ( 𝕂) = ν n ¯ ​ ( 𝒱 n ​ ( 𝕂)) X_{n}(\mathbb{K})=\overline{\nu_{n}}(\mathcal{V}_{n}(\mathbb{K})) by the same Proposition, whereby we see that | X n ​ ( 𝕂) | ≤ | 𝒱 n ​ ( 𝕂) | = N |X_{n}(\mathbb{K})|\leq|\mathcal{V}_{n}(\mathbb{K})|=N. Combined with ( 5.19), we are done. ∎

###### Remark 5.12.

One can provide a much weaker bound on | X n ​ ( 𝕂) | |X_{n}(\mathbb{K})| depending only on n n, and independent of characteristic of 𝕂 \mathbb{K}. This can be done by bounding h c 2 ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ) ≤ ∑ i h c i ​ ( X n ​ ( j 1, …, j n − 1), ℚ ℓ) h^{2}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell})\leq\sum_{i}h^{i}_{c}(X_{n}(j_{1},\dots,j_{n-1}),\mathbb{Q}_{\ell}) and using [12] *Theorem A.

### 5.2. Some rigidity implications of Theorem A

The dimension bound provided by Theorem 5.6 also enables us to obtain a description of the structure of ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) for any algebraically closed field 𝕂 \mathbb{K}. This can be interpreted as a general rigidity result towards Conjecture CA.

###### Corollary 5.13.

If dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = 2 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=2, then ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) is a finite union of 2 2 -dimensional linear subspaces of 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}} invariant under the action of 𝔖 n \mathfrak{S}_{n} on 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}.

###### Proof.

If dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = 2 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=2, there exist points α = ( α 1, …, α n) \mathbf{\alpha}=(\alpha_{1},\dots,\alpha_{n}) in the intersection, but not in the diagonal Δ n ​ ( 𝕂) ⊆ 𝔸 𝕂 n \Delta_{n}(\mathbb{K})\subseteq\mathbb{A}^{n}_{\mathbb{K}}. By [5, Lemma 2], for any such point α ∈ ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \mathbf{\alpha}\in\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}), the 2 2 -dimensional linear space ⟨ α, Δ n ​ ( 𝕂) ⟩ \langle\mathbf{\alpha},\Delta_{n}(\mathbb{K})\rangle spanned by α \mathbf{\alpha} and Δ n ​ ( 𝕂) \Delta_{n}(\mathbb{K}) is also contained in ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}). By dimension constraint, ⟨ α, Δ n ​ ( 𝕂) ⟩ \langle\mathbf{\alpha},\Delta_{n}(\mathbb{K})\rangle must be the irreducible component of ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}), containing α \mathbf{\alpha}. This proves that ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) is a finite union of 2 2 -dimensional linear subspaces of 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}. By ( 5.1) and Lemma 4.12, it follows that ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) is fixed under the action of transpositions of coordinates. Thus, it follows that it is fixed under the 𝔖 n \mathfrak{S}_{n} action on 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}. ∎

As a consequence of Corollary 5.13, we obtain a topological description of Conjecture CA over an algebraically closed field 𝕂 \mathbb{K}.

###### Corollary 5.14.

Conjecture CA is true in degree n n if and only if ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) is irreducible in 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}.

###### Proof.

The “only if” implication is clear. If ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) is irreducible, assume dim ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = 2 \dim\bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=2, as else we are done. Then by Corollary 5.13, it is a single 2 2 -dimensional linear subspace of 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}, fixed under the action of 𝔖 n \mathfrak{S}_{n} on 𝔸 𝕂 n \mathbb{A}^{n}_{\mathbb{K}}. Furthermore, ⋂ i = 1 n − 1 X n i ​ ( 𝕂) = ⟨ α, Δ n ​ ( 𝕂) ⟩ \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K})=\langle\alpha,\Delta_{n}(\mathbb{K})\rangle for any non-diagonal α = ( α 1, …, α n) \alpha=(\alpha_{1},\dots,\alpha_{n}) in ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}). Fix such an α \alpha. Then, for all σ ∈ 𝔖 n \sigma\in\mathfrak{S}_{n}, there exist λ σ, β σ ∈ 𝕂 \lambda_{\sigma},\beta_{\sigma}\in\mathbb{K}, such that

(5.20) |  | ( α σ ⁡ ( 1), α σ ⁡ ( 2), …, α σ ⁡ ( n)) = ( β σ ​ α 1 + λ σ, β σ ​ α 2 + λ σ, …, β σ ​ α n + λ σ) (\alpha_{\sigma(1)},\alpha_{\sigma(2)},\dots,\alpha_{\sigma(n)})=(\beta_{\sigma}\alpha_{1}+\lambda_{\sigma},\beta_{\sigma}\alpha_{2}+\lambda_{\sigma},\dots,\beta_{\sigma}\alpha_{n}+\lambda_{\sigma}) |  |

In particular, letting σ = τ 12 \sigma=\tau_{12} be the transposition of 1 1 and 2 2, we obtain α 2 = β 12 ​ α 1 + λ 12 \alpha_{2}=\beta_{12}\alpha_{1}+\lambda_{12} and α 1 = β 12 ​ α 2 + λ 12 \alpha_{1}=\beta_{12}\alpha_{2}+\lambda_{12} forcing λ 12 = α 1 + α 2 \lambda_{12}=\alpha_{1}+\alpha_{2} and β 12 = − 1 \beta_{12}=-1. Furthermore for all i ≥ 3 i\geq 3, we have α i = β 12 ​ α i + λ 12 \alpha_{i}=\beta_{12}\alpha_{i}+\lambda_{12}, yielding α i = ( α 1 + α 2) / 2 \alpha_{i}=(\alpha_{1}+\alpha_{2})/2. Thus, using the transposition τ 12 \tau_{12} on ( 5.20) forces α i \alpha_{i} ’s to be equal for all i ≠ 1, 2 i\neq 1,2. Using the same argument with transposition τ i ​ j \tau_{ij} for other 1 ≤ i ≠ j ≤ n 1\leq i\neq j\leq n, we see that α i \alpha_{i} ’s must all be equal, contradicting the choice of non-diagonal α \alpha. Thus, ⋂ i = 1 n − 1 X n i ​ ( 𝕂) \bigcap_{i=1}^{n-1}X^{i}_{n}(\mathbb{K}) must be 1 1 -dimensional. ∎

#### 5.2.1. Conjecture CA as a complete intersection problem

Let I j 1, …, j n − 1 ⊆ 𝕂 ⁡ [x 1, …, x n − 1] I_{j_{1},\dots,j_{n-1}}\subseteq\mathbb{K}[x_{1},\dots,x_{n-1}] be the ideal ⟨ Φ j 1 #​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ j n − 1 #​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1) ⟩ \langle\Phi^{\#}_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\Phi^{\#}_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1})\rangle for any set of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. Then since I j 1, …, j n − 1 ⊆ ( x 1, …, x n − 1) I_{j_{1},\dots,j_{n-1}}\subseteq(x_{1},\dots,x_{n-1}) is a homogeneous ideal, we can think of I j 1, …, j n − 1 I_{j_{1},\dots,j_{n-1}} as an ideal in the local ring 𝕂 ​ [x 1, …, x n − 1] ( x 1, …, x n − 1) \mathbb{K}[x_{1},\dots,x_{n-1}]_{(x_{1},\dots,x_{n-1})}. Then, if μ ⁡ ( −) \mu(-) denotes the minimal number of generators of an ideal, we have μ ⁡ ( I j 1, …, j n − 1) = μ ⁡ ( I j 1, …, j n − 1 / I j 1, …, j n − 1 2) \mu(I_{j_{1},\dots,j_{n-1}})=\mu(I_{j_{1},\dots,j_{n-1}}/I_{j_{1},\dots,j_{n-1}}^{2}) (see [11, Section 10.2]). In Theorem 5.6, we prove n − 2 ≤ ht ⁡ ( I j 1, …, j n − 1) n-2\leq\operatorname{ht}(I_{j_{1},\dots,j_{n-1}}), the height of the ideal I j 1, …, j n − 1 I_{j_{1},\dots,j_{n-1}} in 𝕂 ⁡ [x 1, …, x n − 1] \mathbb{K}[x_{1},\dots,x_{n-1}]. Thus, we have:

 | n − 2 ≤ ht ⁡ ( I j 1, …, j n − 1) ≤ μ ⁡ ( I j 1, …, j n − 1) ≤ n − 1 n-2\leq\operatorname{ht}(I_{j_{1},\dots,j_{n-1}})\leq\mu(I_{j_{1},\dots,j_{n-1}})\leq n-1 |  |

This yields three possible scenarios:

1. (1)

ht ⁡ ( I j 1, …, j n − 1) = μ ⁡ ( I j 1, …, j n − 1) = n − 2 \operatorname{ht}(I_{j_{1},\dots,j_{n-1}})=\mu(I_{j_{1},\dots,j_{n-1}})=n-2.

2. (2)

ht ⁡ ( I j 1, …, j n − 1) = μ ⁡ ( I j 1, …, j n − 1) = n − 1 \operatorname{ht}(I_{j_{1},\dots,j_{n-1}})=\mu(I_{j_{1},\dots,j_{n-1}})=n-1.

3. (3)

ht ⁡ ( I j 1, …, j n − 1) = n − 2 \operatorname{ht}(I_{j_{1},\dots,j_{n-1}})=n-2, μ ⁡ ( I j 1, …, j n − 1) = n − 1 \mu(I_{j_{1},\dots,j_{n-1}})=n-1.

Cases ( 1) (1) and ( 2) (2) are equivalent to I j 1, …, j n − 1 I_{j_{1},\dots,j_{n-1}} being complete intersection ideals, while ( 3) (3) is the almost complete intersection case. By Proposition 5.2, Conjecture CA is equivalent to I j 1, …, j n − 1 I_{j_{1},\dots,j_{n-1}} being a complete intersection ideal of height n − 1 n-1 for all 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n, i.e., case ( 2) (2). Furthermore, in light of Proposition 5.3, we see that Conjecture CA is equivalent to T − 1 T-1 being a non-zero divisor in 𝕂 ⁡ [x 1, …, x n − 1, T, 1 1 − 2 ​ T] / ( Φ #​ [T] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)) \mathbb{K}[x_{1},\dots,x_{n-1},T,\frac{1}{1-2T}]/(\Phi^{\#}[T]_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1}}(HD^{n-2}_{n-1}\mathbf{x}_{n-1})), which is a 1 1 -dimensional Cohen-Macaulay ring.

### 5.3. Proof of Theorem D

We end by proving Theorem D which provides a constraint for the singular ℚ \mathbb{Q} -rational fibers of the surjective morphism φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}^{1}_{\mathbb{K}} (obtained from ( 5.15)) considered in the proof of Theorem 5.6 when 𝕂 \mathbb{K} is an algebraically closed field of characteristic 0 0. We define the ℚ \mathbb{Q} -rational fibers of φ ⋆ \varphi^{\star} to be Y ​ ( j 1, …, j n − 1) α:= ( φ ⋆) − 1 ​ ( α) Y(j_{1},\dots,j_{n-1})_{\alpha}:=(\varphi^{\star})^{-1}(\alpha) for α ∈ 𝔸 𝕂 1 ​ ( ℚ) \alpha\in\mathbb{A}^{1}_{\mathbb{K}}(\mathbb{Q}). Since φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}^{1}_{\mathbb{K}} is a surjective family over a 1 1 -dimensional base such that ( φ ⋆) − 1 ​ ( 𝔸 𝕂 1 ​ ( 𝕂) ∖ { 1 / 2 }) (\varphi^{\star})^{-1}(\mathbb{A}^{1}_{\mathbb{K}}(\mathbb{K})\setminus\{1/2\}) is 1 1 -dimensional, it follows that the generic (and hence the general) fiber is 0 0 -dimensional (in fact, a single point) by [17, Lemma 37.30.1]. In particular, there are only finitely many singular fibers of φ ⋆ \varphi^{\star} i .e., 1 1 -dimensional fibers over 𝔸 𝕂 1 ​ ( 𝕂) ∖ { 1 / 2 } \mathbb{A}^{1}_{\mathbb{K}}(\mathbb{K})\setminus\{1/2\}. Note that Conjecture CA is equivalent to the fiber Y ​ ( j 1, …, j n − 1) 1 Y(j_{1},\dots,j_{n-1})_{1} of φ ⋆ \varphi^{\star} over 1 1 being non-singular.

###### Remark 5.15.

Note that φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}^{1}_{\mathbb{K}} is not flat in general and there exist singular ℚ \mathbb{Q} -rational fibers of φ ⋆ \varphi^{\star}. For example, if j 1 ≠ n j_{1}\neq n, then one can check that the fiber ( φ ⋆) − 1 ​ ( 1 / 2) (\varphi^{\star})^{-1}(1/2) is singular since Φ j 1 #​ [1 / 2] ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1) = 0 \Phi^{\#}_{j_{1}}[1/2](HD^{0}_{n-1}\mathbf{x}_{n-1})=0 when j 1 ≠ n j_{1}\neq n. It then follows that dim ( φ ⋆) − 1 ​ ( 1 / 2) = dim Y ​ ( j 1, …, j n − 1) 1 2 ≥ 1 \dim(\varphi^{\star})^{-1}(1/2)=\dim Y(j_{1},\dots,j_{n-1})_{\frac{1}{2}}\geq 1.

###### Theorem 5.16.

Let 𝕂 \mathbb{K} be an algebraically closed field of characteristic 0 0. There are no singular ℚ \mathbb{Q} -rational fibers of φ ⋆: Y ⁡ ( j 1, …, j n − 1) → 𝔸 𝕂 1 \varphi^{\star}:Y(j_{1},\dots,j_{n-1})\rightarrow\mathbb{A}^{1}_{\mathbb{K}} outside { 1 m, m ∈ ℤ ∖ { 0 } } ⊆ ℚ \{\frac{1}{m},\ m\in\mathbb{Z}\setminus\{0\}\}\subseteq\mathbb{Q}. Furthermore, for all integers | m | ≥ 2 |m|\geq 2, there exists a finite set of primes 𝒫 ⁡ ( m) \mathcal{P}(m), such that the fibers ( φ ⋆) − 1 ​ ( 1 m p − 2) (\varphi^{\star})^{-1}(\frac{1}{m^{p-2}}) are non-singular for all p ∉ 𝒫 ⁡ ( m) p\notin\mathcal{P}(m).

###### Proof.

First let r / s ∈ ℚ ∖ { 1 m, m ∈ ℤ ∖ { 0 } } r/s\in\mathbb{Q}\setminus\{\frac{1}{m},\ m\in\mathbb{Z}\setminus\{0\}\}, in its reduced form (i.e., r r and s s are coprime). Then the 𝕂 \mathbb{K} -rational points of the fiber Y ​ ( j 1, …, j n − 1) r s Y(j_{1},\dots,j_{n-1})_{\frac{r}{s}} form the affine algebraic set

 | ⋂ i = 1 n − 1 V ⁡ ( Φ #​ [r / s] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) ⊆ 𝔸 𝕂 n − 1 ​ ( 𝕂). \bigcap_{i=1}^{n-1}V(\Phi^{\#}[r/s]_{j_{i}}(HD_{n-1}^{i-1}\mathbf{x}_{n-1}))\subseteq\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}). |  |

Note that this also equals ⋂ i = 1 n − 1 V ⁡ ( s n − i ​ Φ #​ [r / s] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) \bigcap_{i=1}^{n-1}V(s^{n-i}\Phi^{\#}[r/s]_{j_{i}}(HD_{n-1}^{i-1}\mathbf{x}_{n-1})), but for each 1 ≤ i ≤ n − 1 1\leq i\leq n-1, s n − i ​ Φ #​ [r / s] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) ∈ ℤ ⁡ [x 1, …, x n − 1] s^{n-i}\Phi^{\#}[r/s]_{j_{i}}(HD_{n-1}^{i-1}\mathbf{x}_{n-1})\in\mathbb{Z}[x_{1},\dots,x_{n-1}], since Φ #​ [r / s] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) \Phi^{\#}[r/s]_{j_{i}}(HD_{n-1}^{i-1}\mathbf{x}_{n-1}) is a homogeneous polynomial of degree n − i n-i in the x i x_{i} ’s and s ​ Φ #​ [r / s] j i ​ ( x l) = s ​ x l − r ​ x j i s\Phi^{\#}[r/s]_{j_{i}}(x_{l})=sx_{l}-rx_{j_{i}} if l ≠ j i l\neq j_{i} and s ​ Φ #​ [r / s] j i ​ ( x j i) = ( s − 2 ​ r) ​ x j i s\Phi^{\#}[r/s]_{j_{i}}(x_{j_{i}})=(s-2r)x_{j_{i}}, all of which are polynomials with integer coefficients. Thus, consider

 | Y r / s ​ ( j 1, …, j n − 1):= Proj ⁡ ℤ ⁡ [x 1, …, x n − 1] ( s n − 1 ​ Φ #​ [r / s] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, s ​ Φ #​ [r / s] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)), Y_{r/s}(j_{1},\dots,j_{n-1}):=\operatorname{Proj}\frac{\mathbb{Z}[x_{1},\dots,x_{n-1}]}{(s^{n-1}\Phi^{\#}[r/s]_{j_{1}}(HD_{n-1}^{0}\mathbf{x}_{n-1}),\dots,s\Phi^{\#}[r/s]_{j_{n-1}}(HD_{n-1}^{n-2}\mathbf{x}_{n-1}))}, |  |

which is a projective subscheme of ℙ ℤ n − 1 \mathbb{P}^{n-1}_{\mathbb{Z}}. By [9, Proposition II.4.9], the structure morphism Y r / s ​ ( j 1, …, j n − 1) → Spec ⁡ ( ℤ) Y_{r/s}(j_{1},\dots,j_{n-1})\rightarrow\spec(\mathbb{Z}) is proper and, thus, its image is closed. Let p ∈ Spec ⁡ ( ℤ) p\in\spec(\mathbb{Z}) be a prime which divides r r, and is therefore coprime to s s. Then the fiber of the structure morphism over p p is Y r / s ​ ( j 1, …, j n − 1) p:= Y r / s ​ ( j 1, …, j n − 1) × Spec ⁡ ( ℤ) Spec ⁡ ( 𝔽 p) Y_{r/s}(j_{1},\dots,j_{n-1})_{p}:=Y_{r/s}(j_{1},\dots,j_{n-1})\times_{\spec(\mathbb{Z})}\spec(\mathbb{F}_{p}), which equals (by [13, Proposition 3.1.9])

 | Y r / s ​ ( j 1, …, j n − 1) p = Proj ⁡ 𝔽 p ​ [x 1, …, x n − 1] ( s n − 1 ​ Φ #​ [r / s] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, s ​ Φ #​ [r / s] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)). Y_{r/s}(j_{1},\dots,j_{n-1})_{p}=\operatorname{Proj}\frac{\mathbb{F}_{p}[x_{1},\dots,x_{n-1}]}{(s^{n-1}\Phi^{\#}[r/s]_{j_{1}}(HD_{n-1}^{0}\mathbf{x}_{n-1}),\dots,s\Phi^{\#}[r/s]_{j_{n-1}}(HD_{n-1}^{n-2}\mathbf{x}_{n-1}))}. |  |

But there exists x ∈ ℤ x\in\mathbb{Z} such that since s ​ x ≡ 1 mod p sx\equiv 1\mod p and r ​ x ≡ 0 mod p rx\equiv 0\mod p. Replacing r / s r/s by r ′ / s ′ r^{\prime}/s^{\prime}, where r ′ = r ​ x r^{\prime}=rx and s ′ = s ​ x s^{\prime}=sx we have s ′ ≡ 1 mod p s^{\prime}\equiv 1\mod p and r ′ ≡ 0 mod p r^{\prime}\equiv 0\mod p, and thus,

 | Y r / s ​ ( j 1, …, j n − 1) p = Y r ′ / s ′ ​ ( j 1, …, j n − 1) p = Proj ⁡ 𝔽 p ​ [x 1, …, x n − 1] ( H ​ D n − 1 0 ​ 𝐱 n − 1, …, H ​ D n − 1 n − 2 ​ 𝐱 n − 1) = ∅, Y_{r/s}(j_{1},\dots,j_{n-1})_{p}=Y_{r^{\prime}/s^{\prime}}(j_{1},\dots,j_{n-1})_{p}=\operatorname{Proj}\frac{\mathbb{F}_{p}[x_{1},\dots,x_{n-1}]}{(HD_{n-1}^{0}\mathbf{x}_{n-1},\dots,HD_{n-1}^{n-2}\mathbf{x}_{n-1})}=\emptyset, |  |

since the radical ( H ​ D n − 1 0 ​ 𝐱 n − 1, …, H ​ D n − 1 n − 2 ​ 𝐱 n − 1) \sqrt{(HD_{n-1}^{0}\mathbf{x}_{n-1},\dots,HD^{n-2}_{n-1}\mathbf{x}_{n-1})} is the irrelevant maximal ideal ( x 1, …, x n − 1) ⊆ 𝔽 p ​ [x 1, …, x n − 1] (x_{1},\dots,x_{n-1})\subseteq\mathbb{F}_{p}[x_{1},\dots,x_{n-1}]. Thus, the structure morphism Y r / s ​ ( j 1, …, j n − 1) → Spec ⁡ ( ℤ) Y_{r/s}(j_{1},\dots,j_{n-1})\rightarrow\spec(\mathbb{Z}) is not surjective, whereby it follows that the generic fiber over 0 ∈ Spec ⁡ ( ℤ) 0\in\spec(\mathbb{Z}) is empty as well. By base change, it follows that for any algebraically closed field 𝕂 \mathbb{K} of characteristic 0 0,

 | Proj ⁡ 𝕂 ⁡ [x 1, …, x n − 1] ( s n − 1 ​ Φ #​ [r / s] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, s ​ Φ #​ [r / s] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)) = ∅, \operatorname{Proj}\frac{\mathbb{K}[x_{1},\dots,x_{n-1}]}{(s^{n-1}\Phi^{\#}[r/s]_{j_{1}}(HD_{n-1}^{0}\mathbf{x}_{n-1}),\dots,s\Phi^{\#}[r/s]_{j_{n-1}}(HD_{n-1}^{n-2}\mathbf{x}_{n-1}))}=\emptyset, |  |

or equivalently ⋂ i = 1 n − 1 V ⁡ ( Φ #​ [r / s] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) ⊆ 𝔸 𝕂 n − 1 ​ ( 𝕂) \bigcap_{i=1}^{n-1}V(\Phi^{\#}[r/s]_{j_{i}}(HD_{n-1}^{i-1}\mathbf{x}_{n-1}))\subseteq\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}) is just the origin { 𝟎 } \{\mathbf{0}\}, and thus, 0 0 -dimensional. Thus, the fiber Y ​ ( j 1, …, j n − 1) r s Y(j_{1},\dots,j_{n-1})_{\frac{r}{s}} is not singular for any r / s ∈ ℚ ∖ { 1 n, n ∈ ℕ } r/s\in\mathbb{Q}\setminus\{\frac{1}{n},\ n\in\mathbb{N}\}.

Now consider any integer m m such that | m | ≥ 2 |m|\geq 2. Then for all but finitely many primes p ∈ Spec ⁡ ( ℤ) p\in\spec(\mathbb{Z}), the fiber Y m ​ ( j 1, …, j n − 1) p = ∅ Y_{m}(j_{1},\dots,j_{n-1})_{p}=\emptyset. Let 𝒫 ⁡ ( m) \mathcal{P}(m) be the union of the set of the finitely many primes over which the fiber of Y m ​ ( j 1, …, j n − 1) Y_{m}(j_{1},\dots,j_{n-1}) is non-empty and the set of prime divisors of m m. Then for all p ∉ 𝒫 ⁡ ( m) p\notin\mathcal{P}(m), since m p − 1 ≡ 1 mod p m^{p-1}\equiv 1\mod p, we have

 | Y m ​ ( j 1, …, j n − 1) p = Proj ⁡ 𝔽 p ​ [x 1, …, x n − 1] ( Φ #​ [m] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [m] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)) \displaystyle Y_{m}(j_{1},\dots,j_{n-1})_{p}=\operatorname{Proj}\frac{\mathbb{F}_{p}[x_{1},\dots,x_{n-1}]}{(\Phi^{\#}[m]_{j_{1}}(HD_{n-1}^{0}\mathbf{x}_{n-1}),\dots,\Phi^{\#}[m]_{j_{n-1}}(HD_{n-1}^{n-2}\mathbf{x}_{n-1}))} |  |

 | = Proj ⁡ 𝔽 p ​ [x 1, …, x n − 1] ( Φ #​ [1 m p − 2] j 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [1 m p − 2] j n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1)) = ∅. \displaystyle=\operatorname{Proj}\frac{\mathbb{F}_{p}[x_{1},\dots,x_{n-1}]}{(\Phi^{\#}[\frac{1}{m^{p-2}}]_{j_{1}}(HD_{n-1}^{0}\mathbf{x}_{n-1}),\dots,\Phi^{\#}[\frac{1}{m^{p-2}}]_{j_{n-1}}(HD_{n-1}^{n-2}\mathbf{x}_{n-1}))}=\emptyset. |  |

Thus, Y m ​ ( j 1, …, j n − 1) p = Y 1 m p − 2 ​ ( j 1, …, j n − 1) p = ∅ Y_{m}(j_{1},\dots,j_{n-1})_{p}=Y_{\frac{1}{m^{p-2}}}(j_{1},\dots,j_{n-1})_{p}=\emptyset, whereby the image of the structure morphism Y 1 m p − 2 ​ ( j 1, …, j n − 1) → Spec ⁡ ( ℤ) Y_{\frac{1}{m^{p-2}}}(j_{1},\dots,j_{n-1})\rightarrow\spec(\mathbb{Z}) is a proper closed subset of Spec ⁡ ( ℤ) \spec(\mathbb{Z}). This implies that the generic fiber over 0 ∈ Spec ⁡ ( ℤ) 0\in\spec(\mathbb{Z}) is empty as well. Thus, like the preceding argument for r / s ∈ ℚ ∖ { 1 n, n ∈ ℕ } r/s\in\mathbb{Q}\setminus\{\frac{1}{n},n\in\mathbb{N}\}, for any algebraically closed characteristic 0 0 field 𝕂 \mathbb{K}, ⋂ i = 1 n − 1 V ⁡ ( Φ #​ [1 m p − 2] j i ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1)) ⊆ 𝔸 𝕂 n − 1 ​ ( 𝕂) \bigcap_{i=1}^{n-1}V(\Phi^{\#}[\frac{1}{m^{p-2}}]_{j_{i}}(HD_{n-1}^{i-1}\mathbf{x}_{n-1}))\subseteq\mathbb{A}^{n-1}_{\mathbb{K}}(\mathbb{K}) is just the origin { 𝟎 } \{\mathbf{0}\}, and hence the fiber Y ​ ( j 1, …, j n − 1) 1 m p − 2 Y(j_{1},\dots,j_{n-1})_{\frac{1}{m^{p-2}}} is non-singular for all p ∉ 𝒫 ⁡ ( m) p\notin\mathcal{P}(m). ∎

## 6. Intermediate arithmetic Casas-Alvero schemes

Throughout this section 𝕂 \mathbb{K} is an algebraically closed field unless otherwise mentioned.

###### Definition 6.1.

For 1 ≤ j ≤ n − 1 1\leq j\leq n-1, define the j t ​ h j^{th} intermediate arithmetic Casas-Alvero scheme of degree n n to be the weighted projective ℤ \mathbb{Z} -scheme X n ​ [j] ⊆ ℙ ℤ ​ ( 1, 2, …, n − 1) X_{n}[j]\subseteq\mathbb{P}_{\mathbb{Z}}(1,2,\dots,n-1) defined by the ideal ⟨ Disc n i ( y 1, …, y n − 1, 0), 1 ≤ i ≤ j ⟩ \langle\disc^{i}_{n}(y_{1},\dots,y_{n-1},0),\ 1\leq i\leq j\rangle, where Disc n i ​ ( y 1, …, y n − 1, 0) ∈ ℤ w ​ [y 1, …, y n − 1] \disc^{i}_{n}(y_{1},\dots,y_{n-1},0)\in\mathbb{Z}^{w}[y_{1},\dots,y_{n-1}] is the reduced i t ​ h i^{th} discriminant polynomial (see Section 4.3).

Thus, the ordinary n t ​ h n^{th} arithmetic Casas-Alvero scheme X n X_{n} is X n ​ [n − 1] X_{n}[n-1] in terms of the above definition. Using the notations of Section 4.3, recall that ν n ​ ( X n i ​ ( 𝕂)) = Δ n i ​ ( 𝕂) = V ⁡ ( Disc n i ​ ( y 1, …, y n)) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \nu_{n}(X^{i}_{n}(\mathbb{K}))=\Delta^{i}_{n}(\mathbb{K})=V(\disc^{i}_{n}(y_{1},\dots,y_{n}))\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1. Then it follows that Proposition 4.14 can be generalised as follows.

###### Proposition 6.2.

For any 1 ≤ j ≤ n − 1 1\leq j\leq n-1, let 𝒱 ^ n ​ [j] ​ ( 𝕂):= V ⁡ ( x n) ∩ ( ⋂ i = 1 j X n i ​ ( 𝕂)) ⊆ 𝔸 𝕂 n ​ ( 𝕂) \widehat{\mathcal{V}}_{n}[j](\mathbb{K}):=V(x_{n})\cap(\bigcap_{i=1}^{j}X^{i}_{n}(\mathbb{K}))\subseteq\mathbb{A}^{n}_{\mathbb{K}}(\mathbb{K}) and 𝒱 n ​ [j] ​ ( 𝕂):= ( 𝒱 ^ n ​ [j] ​ ( 𝕂) ∖ { 𝟎 }) / 𝔾 m ⊆ ℙ 𝕂 n − 1 ​ ( 𝕂) \mathcal{V}_{n}[j](\mathbb{K}):=(\widehat{\mathcal{V}}_{n}[j](\mathbb{K})\setminus\{\mathbf{0}\})/\mathbb{G}_{m}\subseteq\mathbb{P}^{n-1}_{\mathbb{K}}(\mathbb{K}). Then X n ​ [j] ​ ( 𝕂) = ν ¯ n ​ ( 𝒱 n ​ [j] ​ ( 𝕂)) X_{n}[j](\mathbb{K})=\overline{\nu}_{n}(\mathcal{V}_{n}[j](\mathbb{K})), where ν ¯ n: ℙ 𝕂 n − 1 → ℙ 𝕂 ​ ( 1, 2, …, n − 1) \overline{\nu}_{n}:\mathbb{P}^{n-1}_{\mathbb{K}}\rightarrow\mathbb{P}_{\mathbb{K}}(1,2,\dots,n-1) is the induced Vieta map.

By Remark 5.9, Conjecture CA in degree n n is equivalent to dim X n ​ [n − 1] = dim X n = 0 \dim X_{n}[n-1]=\dim X_{n}=0. Note that Corollary 5.7 provides the dimension bound dim X n ​ [n − 1] ​ ( 𝕂) ≤ 0 \dim X_{n}[n-1](\mathbb{K})\leq 0 for all fields 𝕂 \mathbb{K} (with the convention that dim X n ​ [n − 1] < 0 \dim X_{n}[n-1]<0 if empty). Using Proposition 6.2 and Proposition 5.3 we can obtain a similar dimension bound for X n ​ [j] ​ ( 𝕂) X_{n}[j](\mathbb{K}) for all 1 ≤ j ≤ n − 1 1\leq j\leq n-1 and 𝕂 \mathbb{K} algebraically closed.

###### Corollary 6.3.

Let 𝕂 \mathbb{K} be any algebraically closed field. Then for any n ≥ 2 n\geq 2 and 1 ≤ j ≤ n − 1 1\leq j\leq n-1, we have n − j − 2 ≤ dim X n ​ [j] ​ ( 𝕂) ≤ n − j − 1 n-j-2\leq\dim X_{n}[j](\mathbb{K})\leq n-j-1.

###### Proof.

By Proposition 5.3, for any 1 ≤ j ≤ n − 1 1\leq j\leq n-1, Φ #​ [T] l 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] l j ​ ( H ​ D n − 1 j − 1 ​ 𝐱 n − 1) \Phi^{\#}[T]_{l_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{l_{j}}(HD^{j-1}_{n-1}\mathbf{x}_{n-1}) is a regular sequence in 𝕂 ⁡ [x 1, …, x n − 1, T, 1 1 − 2 ​ T] \mathbb{K}[x_{1},\dots,x_{n-1},T,\frac{1}{1-2T}] for any choice of indices 1 ≤ l 1, …, l j ≤ n 1\leq l_{1},\dots,l_{j}\leq n. This, along with Krull’s height theorem gives us

 | n − j − 1 ≤ dim 𝕂 ⁡ [x 1, …, x n − 1, T] / ( Φ #​ [T] l 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] l j ​ ( H ​ D n − 1 j − 1 ​ 𝐱 n − 1), T − 1) ≤ n − j, n-j-1\leq\dim\mathbb{K}[x_{1},\dots,x_{n-1},T]/(\Phi^{\#}[T]_{l_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{l_{j}}(HD^{j-1}_{n-1}\mathbf{x}_{n-1}),T-1)\leq n-j, |  |

for any choice of indices 1 ≤ l 1, …, l j ≤ n 1\leq l_{1},\dots,l_{j}\leq n. This along with Equation ( 4.10) and Proposition 6.2 implies the result. ∎

Note that if dim X n ​ [j] ​ ( 𝕂) = n − j − 2 \dim X_{n}[j](\mathbb{K})=n-j-2, then it is a complete intersection. For any n ≥ 3 n\geq 3 and algebraically closed field 𝕂 \mathbb{K}, it is easy to see that X n ​ [1] ​ ( 𝕂) X_{n}[1](\mathbb{K}) and X n ​ [2] ​ ( 𝕂) X_{n}[2](\mathbb{K}) are complete intersections. From Proposition 5.2 we see that if we have X n ​ ( 𝕂) = X n ​ [n − 1] ​ ( 𝕂) = ∅ X_{n}(\mathbb{K})=X_{n}[n-1](\mathbb{K})=\emptyset, then dim X n ​ [j] ​ ( 𝕂) = n − j − 2 \dim X_{n}[j](\mathbb{K})=n-j-2 for all 1 ≤ j ≤ n − 2 1\leq j\leq n-2, i.e., X n ​ [j] ​ ( 𝕂) X_{n}[j](\mathbb{K}) is a complete intersection for all 1 ≤ j ≤ n − 2 1\leq j\leq n-2. In general, we see that if X n ​ [j 0] ​ ( 𝕂) X_{n}[j_{0}](\mathbb{K}) is a complete intersection, then so is X n ​ [j] ​ ( 𝕂) X_{n}[j](\mathbb{K}) for all 1 ≤ j ≤ j 0 1\leq j\leq j_{0}. This motivates one to ask the following question.

###### Question 6.4.

For a given n ≥ 3 n\geq 3 and algebraically closed field 𝕂 \mathbb{K}, what is the maximum value j C ​ ( n) j_{C}(n) of 1 ≤ j ≤ n − 1 1\leq j\leq n-1 such that X n ​ [j] ​ ( 𝕂) X_{n}[j](\mathbb{K}) is a complete intersection?

It is clear that Question 6.4 depends only on the characteristic of 𝕂 \mathbb{K}. Conjecture CA is then equivalent to saying that when 𝕂 \mathbb{K} has characteristic 0 0, then j C ​ ( n) = n − 1 j_{C}(n)=n-1 for all n ≥ 3 n\geq 3. Thus, j C ​ ( n) j_{C}(n) provides a way to measure the failure of Conjecture CA, when it is not true. We will now try to understand how intermediate arithmetic Casas-Alvero schemes across various degrees control each other’s complete intersection behaviour. First we need a technical result.

###### Proposition 6.5.

Let 𝕂 \mathbb{K} be an algebraically closed field. If for some 1 ≤ l ≤ n − 1 1\leq l\leq n-1 the sequence

 | Φ j 1 #​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ j l #​ ( H ​ D n − 1 l − 1 ​ 𝐱 n − 1) \Phi^{\#}_{j_{1}}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\ \dots,\ \Phi^{\#}_{j_{l}}(HD^{l-1}_{n-1}\mathbf{x}_{n-1}) |  |

forms a regular sequence in 𝕂 ⁡ [x 1, …, x n − 1] \mathbb{K}[x_{1},\dots,x_{n-1}] for all choices of indices 1 ≤ j 1, …, j l ≤ n 1\leq j_{1},\dots,j_{l}\leq n, then the sequence

 | Φ j 1 #​ ( H ​ D n 0 ​ 𝐱 n), …, Φ j l #​ ( H ​ D n l − 1 ​ 𝐱 n) \Phi^{\#}_{j_{1}}(HD^{0}_{n}\mathbf{x}_{n}),\ \dots,\ \Phi^{\#}_{j_{l}}(HD^{l-1}_{n}\mathbf{x}_{n}) |  |

forms a regular sequence in 𝕂 ⁡ [x 1, …, x n − 1, x n] \mathbb{K}[x_{1},\dots,x_{n-1},x_{n}] for all choices of indices 1 ≤ j 1, …, j l ≤ n + 1 1\leq j_{1},\dots,j_{l}\leq n+1.

###### Proof.

For the purpose of this proof, we will denote the endomorphisms Φ j #: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1] \Phi^{\#}_{j}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1}] defined in Remark 4.13 by Φ j, n − 1 #\Phi^{\#}_{j,n-1} for all 1 ≤ j ≤ n 1\leq j\leq n. Similarly, we will denote the homomorphisms Φ #​ [T] j: 𝕂 ⁡ [x 1, …, x n − 1] → 𝕂 ⁡ [x 1, …, x n − 1, T] \Phi^{\#}[T]_{j}:\mathbb{K}[x_{1},\dots,x_{n-1}]\rightarrow\mathbb{K}[x_{1},\dots,x_{n-1},T] defined in Section 5.1 by Φ #​ [T] j, n − 1 \Phi^{\#}[T]_{j,n-1} for all 1 ≤ j ≤ n 1\leq j\leq n. For ease of notation, we also add the convention that Φ j, n − 1 #= Φ n, n − 1 #\Phi^{\#}_{j,n-1}=\Phi^{\#}_{n,n-1} for all j ≥ n j\geq n.

For ease of notation, we will only prove the Proposition for the case l = n − 1 l=n-1, as the proof of a general 1 ≤ l ≤ n − 1 1\leq l\leq n-1 is akin to that for l = n − 1 l=n-1. By Proposition 5.3, the hypothesis is equivalent to Φ #​ [T] j 1, n − 1 ​ ( H ​ D n − 1 0 ​ 𝐱 n − 1), …, Φ #​ [T] j n − 1, n − 1 ​ ( H ​ D n − 1 n − 2 ​ 𝐱 n − 1), T − 1 \Phi^{\#}[T]_{j_{1},n-1}(HD^{0}_{n-1}\mathbf{x}_{n-1}),\dots,\ \Phi^{\#}[T]_{j_{n-1},n-1}(HD^{n-2}_{n-1}\mathbf{x}_{n-1}),\ T-1 being a regular sequence in 𝕂 ⁡ [x 1, …, x n − 1, T, 1 1 − 2 ​ T] \mathbb{K}[x_{1},\dots,x_{n-1},T,\frac{1}{1-2T}] for any choice of indices 1 ≤ j 1, …, j n − 1 ≤ n 1\leq j_{1},\dots,j_{n-1}\leq n. Similarly, we see that our conclusion is equivalent to Φ #​ [T] j 1, n ​ ( H ​ D n 0 ​ 𝐱 n), …, Φ #​ [T] j n − 1, n ​ ( H ​ D n n − 2 ​ 𝐱 n), T − 1 \Phi^{\#}[T]_{j_{1},n}(HD^{0}_{n}\mathbf{x}_{n}),\dots,\Phi^{\#}[T]_{j_{n-1},n}(HD^{n-2}_{n}\mathbf{x}_{n}),\ T-1 being a regular sequence in 𝕂 ⁡ [x 1, …, x n, T, 1 1 − 2 ​ T] \mathbb{K}[x_{1},\dots,x_{n},T,\frac{1}{1-2T}] for all choices of 1 ≤ j 1, …, j n − 1 ≤ n + 1 1\leq j_{1},\dots,j_{n-1}\leq n+1. Now since j 1, …, j n − 1 j_{1},\dots,j_{n-1} are some integers between 1 1 and n + 1 n+1, there exists some 1 ≤ l ≤ n 1\leq l\leq n such that j i ≠ l j_{i}\neq l for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1. Let τ l ​ n: 𝕂 ⁡ [x 1, …, x n, T] → 𝕂 ⁡ [x 1, …, x n, T] \tau_{ln}:\mathbb{K}[x_{1},\dots,x_{n},T]\rightarrow\mathbb{K}[x_{1},\dots,x_{n},T] be the 𝕂 \mathbb{K} -algebra automorphism that swaps x l x_{l} and x n x_{n}. Then

(6.1) |  | τ l ​ n ​ ( Φ #​ [T] j i, n ​ ( H ​ D n i − 1 ​ 𝐱 n)) = { Φ #​ [T] j i, n ​ ( H ​ D n i − 1 ​ 𝐱 n) if ​ j i ≠ n Φ #​ [T] l, n ​ ( H ​ D n i − 1 ​ 𝐱 n) if ​ j i = n. \displaystyle\tau_{ln}(\Phi^{\#}[T]_{j_{i},n}(HD^{i-1}_{n}\mathbf{x}_{n}))=\begin{cases}\Phi^{\#}[T]_{j_{i},n}(HD^{i-1}_{n}\mathbf{x}_{n})&\text{if }j_{i}\neq n\\ \Phi^{\#}[T]_{l,n}(HD^{i-1}_{n}\mathbf{x}_{n})&\text{if }j_{i}=n.\end{cases} |  |

Thus, without loss of generality, we can assume that j i ≠ n j_{i}\neq n for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1 in the sequence Φ #​ [T] j 1, n ​ ( H ​ D n 0 ​ 𝐱 n), …, Φ #​ [T] j n − 1, n ​ ( H ​ D n n − 2 ​ 𝐱 n) \Phi^{\#}[T]_{j_{1},n}(HD^{0}_{n}\mathbf{x}_{n}),\dots,\Phi^{\#}[T]_{j_{n-1},n}(HD^{n-2}_{n}\mathbf{x}_{n}). Then we see that

(6.2) |  | Φ #​ [T] j i, n ​ ( H ​ D n i − 1 ​ 𝐱 n) = ( x n − T ​ x j i) ​ Φ #​ [T] j i, n − 1 ​ ( H ​ D n − 1 i − 1 ​ 𝐱 n − 1) + Φ #​ [T] j i, n − 1 ​ ( H ​ D n − 1 i − 2 ​ 𝐱 n − 1) \Phi^{\#}[T]_{j_{i},n}(HD^{i-1}_{n}\mathbf{x}_{n})=(x_{n}-Tx_{j_{i}})\Phi^{\#}[T]_{j_{i},n-1}(HD^{i-1}_{n-1}\mathbf{x}_{n-1})+\Phi^{\#}[T]_{j_{i},n-1}(HD^{i-2}_{n-1}\mathbf{x}_{n-1}) |  |

For brevity, let H i, n:= Φ #​ [T] j i, n ​ ( H ​ D n i − 1 ​ 𝐱 n) H_{i,n}:=\Phi^{\#}[T]_{j_{i},n}(HD^{i-1}_{n}\mathbf{x}_{n}) for all 1 ≤ i ≤ n − 1 1\leq i\leq n-1, and j i ∈ { 1, …, n + 1 } ∖ { n } j_{i}\in\{1,\dots,n+1\}\setminus\{n\}. Consider the monomial partial ordering ≺ \prec on 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n] \mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n}] given by x 1 α 1 ​ … ​ x n α n ≺ x 1 α 1 ′ ​ … ​ x n α n ′ x_{1}^{\alpha_{1}}\dots x_{n}^{\alpha_{n}}\prec x_{1}^{\alpha^{\prime}_{1}}\dots x_{n}^{\alpha^{\prime}_{n}} if and only if α n ≤ α n ′ \alpha_{n}\leq\alpha^{\prime}_{n}. Let Dom ⁡ ( f) \dom(f) denote the sum of the dominant terms of f ∈ 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n] f\in\mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n}]. Then by Equation ( 6.2), we see that Dom ⁡ ( H i, n) = x n ​ H i, n − 1 \dom(H_{i,n})=x_{n}H_{i,n-1}. We want to show that H 1, n, H 2, n, …, H n − 1, n, T − 1 H_{1,n},H_{2,n},\dots,H_{n-1,n},\ T-1, or equivalently by [17] *Lemma 10.68.9, H 1, n n − 1, H 2, n n − 2, …, H n − 1, n, T − 1 H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n},\ T-1 is a regular sequence in 𝕂 ⁡ [x 1, …, x n, T, 1 1 − 2 ​ T] \mathbb{K}[x_{1},\dots,x_{n},T,\frac{1}{1-2T}]. By Proposition 5.3 and [17] *Lemma 10.68.9, we already know that H 1, n n − 1, H 2, n n − 2, …, H n − 1, n H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n} forms a regular sequence and thus, it suffices to show that T − 1 T-1 is a non-zero divisor modulo the ideal ( H 1, n n − 1, H 2, n n − 2, …, H n − 1, n) (H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n}) in 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n] \mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n}]. Note that Dom ⁡ ( H i, n n − i) = x n n − i ​ H i, n − 1 n − i \dom(H_{i,n}^{n-i})=x_{n}^{n-i}H_{i,n-1}^{n-i} and by Remark 5.5 and our assumption, it follows that any subsequence of H 1, n − 1 n − 1, H 2, n − 1 n − 2, …, H n − 1, n − 1 H_{1,n-1}^{n-1},H_{2,n-1}^{n-2},\dots,H_{n-1,n-1} forms a regular sequence as well. Then we obtain the following Lemma analogous to Lemma 5.4.

###### Lemma 6.6.

Let ≺ \prec be the monomial partial ordering on A:= 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n] A:=\mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n}] given by x 1 α 1 ​ … ​ x n α n ≺ x 1 α 1 ′ ​ … ​ x n α n ′ x_{1}^{\alpha_{1}}\dots x_{n}^{\alpha_{n}}\prec x_{1}^{\alpha^{\prime}_{1}}\dots x_{n}^{\alpha^{\prime}_{n}} if and only if α n ≤ α n ′ \alpha_{n}\leq\alpha^{\prime}_{n}. Then for any non-zero A A -linear combination of the form ∑ j ∈ S c j ​ H j, n n − j \sum_{j\in S}c_{j}H_{j,n}^{n-j} for any subset S ⊆ { 1, …, n − 1 } S\subseteq\{1,\dots,n-1\}, there exist c ~ j ∈ A \tilde{c}_{j}\in A such that ∑ j ∈ S c j ​ H j, n n − j = ∑ j ∈ S c ~ j ​ H j, n n − j \sum_{j\in S}c_{j}H_{j,n}^{n-j}=\sum_{j\in S}\tilde{c}_{j}H_{j,n}^{n-j} and Dom ⁡ ( ∑ j ∈ S c j ​ H j, n n − j) = Dom ⁡ ( ∑ j ∈ S Dom ⁡ ( c ~ j) ​ Dom ⁡ ( H j, n n − j)) \dom(\sum_{j\in S}c_{j}H_{j,n}^{n-j})=\dom(\sum_{j\in S}\dom(\tilde{c}_{j})\dom(H_{j,n}^{n-j})).

We skip the proof of Lemma 6.6 as it is essentially similar to the proof of Lemma 5.4. Now we return to our goal of proving that T − 1 T-1 is a non-zero divisor in A / ( H 1, n n − 1, H 2, n n − 2, …, H n − 1, n) A/(H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n}). Our strategy will be similar to the proof of Proposition 5.3. For this, suppose given the following equation in A A:

(6.3) |  | c ⁡ ( T − 1) = ∑ j = 1 n − 1 c j ​ H j, n n − j, c(T-1)=\sum_{j=1}^{n-1}c_{j}H_{j,n}^{n-j}, |  |

we have to show c ∈ ( H 1, n n − 1, H 2, n n − 2, …, H n − 1, n) ⊆ A c\in(H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n})\subseteq A. Applying Lemma 6.6, we can assume Dom ⁡ ( ∑ j = 1 n − 1 c j ​ H j, n n − j) = Dom ⁡ ( ∑ j = 1 n − 1 Dom ⁡ ( c j) ​ Dom ⁡ ( H j, n n − 1)) \dom(\sum_{j=1}^{n-1}c_{j}H_{j,n}^{n-j})=\dom(\sum_{j=1}^{n-1}\dom(c_{j})\dom(H_{j,n}^{n-1})). Then taking Dom \dom of ( 6.3), we have:

(6.4) |  | Dom ⁡ ( c) ​ ( T − 1) = Dom ⁡ ( ∑ j = 1 n − 1 Dom ⁡ ( c j) ​ Dom ⁡ ( H j, n n − j)) = Dom ⁡ ( ∑ j = 1 n − 1 Dom ⁡ ( c j) ​ H j, n − 1 n − j ​ x n n − j), \dom(c)(T-1)=\dom(\sum_{j=1}^{n-1}\dom(c_{j})\dom(H_{j,n}^{n-j}))=\dom(\sum_{j=1}^{n-1}\dom(c_{j})H_{j,n-1}^{n-j}x_{n}^{n-j}), |  |

where deg x n ⁡ ( Dom ⁡ ( c)) = m \deg_{x_{n}}(\dom(c))=m. Since H 1, n − 1 n − 1, H 2, n − 1 n − 2, …, H n − 1, n − 1, T − 1 H_{1,n-1}^{n-1},H_{2,n-1}^{n-2},\dots,H_{n-1,n-1},T-1 form a regular sequence in A A, ( 6.4) implies that Dom ⁡ ( c) = ∑ j = 1 n − 1 b j 1 ​ H j, n − 1 n − j \dom(c)=\sum_{j=1}^{n-1}b^{1}_{j}H_{j,n-1}^{n-j}, for b j 1 ∈ A b^{1}_{j}\in A such that x n m | b j 1 x_{n}^{m}\mid b^{1}_{j} for all 1 ≤ j ≤ n − 1 1\leq j\leq n-1. Now as long as 𝐦 ≥ 𝐧 − 𝟏 \mathbf{m\geq n-1}, let c ′:= c − ∑ j = 1 n − 1 b j 1 x n n − j ​ H j, n n − j c^{\prime}:=c-\sum_{j=1}^{n-1}\frac{b^{1}_{j}}{x_{n}^{n-j}}H_{j,n}^{n-j}. Then either c ′ = 0 c^{\prime}=0, in which case we are done, else c ′ ≠ 0 c^{\prime}\neq 0 and

 | c ′ ​ ( T − 1) = ∑ j = 1 n − 1 ( c j − b j 1 ​ ( T − 1) x n n − j) ​ H j, n n − j, c^{\prime}(T-1)=\sum_{j=1}^{n-1}(c_{j}-\frac{b^{1}_{j}(T-1)}{x_{n}^{n-j}})H_{j,n}^{n-j}, |  |

which is an equation in A A of the form ( 6.3), but with Dom ⁡ ( c ′) < Dom ⁡ ( c) \dom(c^{\prime})<\dom(c). Iterating this process, we either reach c ∈ ( H 1, n n − 1, H 2, n n − 2, …, H n − 1, n) ⊆ A c\in(H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n})\subseteq A, in which case we are done, or deg x n ⁡ ( c) ≤ n − 2 \deg_{x_{n}}(c)\leq n-2. Then taking Dom \dom of the new ( 6.3), we obtain ( 6.4), but with deg x n ⁡ ( Dom ⁡ ( c)) = m ≤ n − 2 \deg_{x_{n}}(\dom(c))=m\leq n-2. Then from ( 6.4), we see that Dom ⁡ ( c 1) ​ H 1, n − 1 n − 1 ​ x n n − 1 \dom(c_{1})H_{1,n-1}^{n-1}x_{n}^{n-1} gets cancelled, i.e., either Dom ⁡ ( c 1) = 0 \dom(c_{1})=0 or there exists a subset S ⊆ { 1, 2, …, n − 1 } S\subseteq\{1,2,\dots,n-1\} such that 1 ∈ S 1\in S and ∑ j ∈ S Dom ⁡ ( c j) ​ H j, n − 1 n − j ​ x n n − j = 0 \sum_{j\in S}\dom(c_{j})H_{j,n-1}^{n-j}x_{n}^{n-j}=0. Then applying Lemma 6.6 to this subset S S, we can reduce Dom ⁡ ( c 1) \dom(c_{1}). Since m < n − 1 m<n-1, we can iterate this process, until deg x n ⁡ ( Dom ⁡ ( c 1)) = 0 \deg_{x_{n}}(\dom(c_{1}))=0 or equivalently c 1 ∈ 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n − 1] c_{1}\in\mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n-1}]. Then we have

(6.5) |  |  | c 1 H 1, n − 1 n − 1 x n n − 1 + ∑ j ∈ S ∖ { 1 } Dom ( c j) H j, n − 1 n − j x n n − j = 0 ⟹ c 1 x n n − 1 = − ∑ j ∈ S ∖ { 1 } e j H j, n − 1 n − j, \displaystyle c_{1}H_{1,n-1}^{n-1}x_{n}^{n-1}+\sum_{j\in S\setminus\{1\}}\dom(c_{j})H_{j,n-1}^{n-j}x_{n}^{n-j}=0\implies c_{1}x_{n}^{n-1}=-\sum_{j\in S\setminus\{1\}}e_{j}H_{j,n-1}^{n-j}, |  |

for some e j ∈ A e_{j}\in A such that e j = e j ′ ​ x n n − 1 e_{j}=e_{j}^{\prime}x_{n}^{n-1} for e j ′ ∈ 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n − 1] e_{j}^{\prime}\in\mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n-1}]. This is because { H j, n − 1 n − j } j ∈ S \{H_{j,n-1}^{n-j}\}_{j\in S} forms a regular sequence in A A and c 1 ∈ 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n − 1] c_{1}\in\mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n-1}]. Then

 | c 1 ​ H 1, n − 1 n − 1 ​ x n n − 1 + ∑ j ∈ S ∖ { 1 } Dom ⁡ ( c j) ​ H j, n − 1 n − j ​ x n n − j = ∑ j ∈ S ∖ { 1 } ( Dom ⁡ ( c j) − e j ′ ​ H 1, n − 1 n − 1 ​ x n j − 1) ​ H j, n − 1 n − j ​ x n n − j c_{1}H_{1,n-1}^{n-1}x_{n}^{n-1}+\sum_{j\in S\setminus\{1\}}\dom(c_{j})H_{j,n-1}^{n-j}x_{n}^{n-j}=\sum_{j\in S\setminus\{1\}}(\dom(c_{j})-e^{\prime}_{j}H_{1,n-1}^{n-1}x_{n}^{j-1})H_{j,n-1}^{n-j}x_{n}^{n-j} |  |

So ( 6.4) becomes

(6.6) |  |  | Dom ⁡ ( c) ​ ( T − 1) = Dom ⁡ ( ∑ j ∈ S ∖ { 1 } ( Dom ⁡ ( c j) − e j ′ ​ H 1, n − 1 n − 1 ​ x n j − 1) ​ H j, n − 1 n − j ​ x n n − j + ∑ j ∉ S Dom ⁡ ( c j) ​ H j, n − 1 n − j ​ x n n − j) \displaystyle\dom(c)(T-1)=\dom(\sum_{j\in S\setminus\{1\}}(\dom(c_{j})-e^{\prime}_{j}H_{1,n-1}^{n-1}x_{n}^{j-1})H_{j,n-1}^{n-j}x_{n}^{n-j}+\sum_{j\notin S}\dom(c_{j})H_{j,n-1}^{n-j}x_{n}^{n-j}) |  |

(6.7) |  |  | ⟹ Dom ⁡ ( c) = ∑ j = 2 n − 1 b j 2 ​ H j, n − 1 n − j, \displaystyle\implies\dom(c)=\sum_{\begin{subarray}{c}j=2\end{subarray}}^{n-1}b^{2}_{j}H_{j,n-1}^{n-j}, |  |

for b j 2 ∈ A b^{2}_{j}\in A such that x n m | b j 2 x_{n}^{m}\mid b^{2}_{j} for all 2 ≤ j ≤ n − 1 2\leq j\leq n-1, since { H j, n − 1 n − j ∣ 2 ≤ j ≤ n − 1 } \{H_{j,n-1}^{n-j}\mid\ 2\leq j\leq n-1\} is a regular sequence in A A. Then as long as 𝐦 ≥ 𝐧 − 𝟐 \mathbf{m\geq n-2}, letting c ′:= c − ∑ j = 2 n − 1 b j 2 x n n − j ​ H j, n n − j c^{\prime}:=c-\sum_{j=2}^{n-1}\frac{b^{2}_{j}}{x_{n}^{n-j}}H_{j,n}^{n-j} we can repeat the above process. This same process can be iterated for all H j, n − 1 n − j H_{j,n-1}^{n-j} for 2 ≤ j ≤ n − 1 2\leq j\leq n-1, till we either have c ∈ ( H 1, n n − 1, H 2, n n − 2, …, H n − 1, n) ⊆ A c\in(H_{1,n}^{n-1},H_{2,n}^{n-2},\dots,H_{n-1,n})\subseteq A or obtain ( 6.3), i.e.,

 | c ⁡ ( T − 1) = ∑ j = 1 n − 1 c j ​ H j, n n − j, c(T-1)=\sum_{j=1}^{n-1}c_{j}H_{j,n}^{n-j}, |  |

with m = deg x n ⁡ ( c) = 0 m=\deg_{x_{n}}(c)=0. Then by Lemma 6.6, there exist c ~ j \tilde{c}_{j} for all 1 ≤ j ≤ n − 1 1\leq j\leq n-1, such that c ⁡ ( T − 1) = ∑ j = 1 n − 1 c j ~ ​ H j, n n − j c(T-1)=\sum_{j=1}^{n-1}\tilde{c_{j}}H_{j,n}^{n-j} and Dom ⁡ ( c) ​ ( T − 1) = Dom ⁡ ( ∑ j = 1 n − 1 Dom ⁡ ( c j ~) ​ H j, n − 1 n − j ​ x n n − j) \dom(c)(T-1)=\dom(\sum_{j=1}^{n-1}\dom(\tilde{c_{j}})H_{j,n-1}^{n-j}x_{n}^{n-j}). Then since n − j > 0 = deg x n ⁡ ( Dom ⁡ ( c)) n-j>0=\deg_{x_{n}}(\dom(c)) for all 1 ≤ j ≤ n − 1 1\leq j\leq n-1, there exists a subset S ⊆ { 1, 2 ​ …, n − 1 } S\subseteq\{1,2\dots,n-1\} such that ∑ j ∈ S Dom ⁡ ( c ~ j) ​ Dom ⁡ ( H j, n n − j) = 0 \sum_{j\in S}\dom(\tilde{c}_{j})\dom(H_{j,n}^{n-j})=0. Then applying Lemma 6.6 to this subset S S, we can reduce deg x n ⁡ ( Dom ⁡ ( c j ~)) \deg_{x_{n}}(\dom(\tilde{c_{j}})) for all j ∈ S j\in S. We can iterate this until we reach deg x n ⁡ ( Dom ⁡ ( c ~ j)) = 0 \deg_{x_{n}}(\dom(\tilde{c}_{j}))=0 for all j ∈ S j\in S and subsequently for all 1 ≤ j ≤ n − 1 1\leq j\leq n-1. Thus, we are reduced to the case where we have c, c i ∈ 𝕂 ⁡ [T, 1 1 − 2 ​ T] ​ [x 1, …, x n − 1] c,c_{i}\in\mathbb{K}[T,\frac{1}{1-2T}][x_{1},\dots,x_{n-1}] in ( 6.3). Then comparing coefficients of x n n − 1 x_{n}^{n-1} we see that 0 = c 1 ​ H 1, n − 1 n − 1 ​ x n n − 1 0=c_{1}H_{1,n-1}^{n-1}x_{n}^{n-1}, which implies c 1 = 0 c_{1}=0. This reduces us to the equation c ⁡ ( T − 1) = ∑ j = 2 n − 1 c j ​ H j, n n − j c(T-1)=\sum_{j=2}^{n-1}c_{j}H_{j,n}^{n-j}, but then comparing coefficients of x n n − 2 x_{n}^{n-2} on either side, we see c 2 = 0 c_{2}=0. Repeating this process we see c j = 0 c_{j}=0 for all 1 ≤ j ≤ n − 1 1\leq j\leq n-1. Thus, we must have c = 0 c=0, which completes the proof in account of the previous reduction processes. ∎

As an immediate corollary of Proposition 6.5, we obtain the following.

###### Corollary 6.7.

Let 𝕂 \mathbb{K} be an algebraically closed field. If dim X N ​ [l] ​ ( 𝕂) = N − l − 2 \dim X_{N}[l](\mathbb{K})=N-l-2 for some N ≥ 2 N\geq 2 and 1 ≤ l ≤ N − 1 1\leq l\leq N-1, then for all n ≥ N n\geq N, we have dim X n ​ [l] ​ ( 𝕂) = n − l − 2 \dim X_{n}[l](\mathbb{K})=n-l-2. In particular, if X N ​ ( 𝕂) = X N ​ [N − 1] ​ ( 𝕂) = ∅ X_{N}(\mathbb{K})=X_{N}[N-1](\mathbb{K})=\emptyset, then X N + 1 ​ [N − 1] ​ ( 𝕂) X_{N+1}[N-1](\mathbb{K}) is finite.

###### Proof.

This follows from Equation ( 4.10), Proposition 6.2 and Proposition 6.5. ∎

###### Corollary 6.8.

Let 𝕂 \mathbb{K} be algebraically closed of characteristic 0 0. Let q ⁡ ( n) q(n) be the largest number less than or equal to n n which is of the form p k p^{k} or 2 ​ p k 2p^{k} for some prime p p and k ∈ ℕ k\in\mathbb{N}. Then j C ​ ( n) ≥ q ⁡ ( n) − 1 j_{C}(n)\geq q(n)-1.

###### Proof.

This follows from Corollary 6.7 and [7] *Theorem. ∎

###### Remark 6.9.

The implication X N ​ ( 𝕂) = X N ​ [N − 1] ​ ( 𝕂) = ∅ ⟹ | X N + 1 ​ [N − 1] ​ ( 𝕂) | < ∞ X_{N}(\mathbb{K})=X_{N}[N-1](\mathbb{K})=\emptyset\implies|X_{N+1}[N-1](\mathbb{K})|<\infty, strengthens the unconditional result Corollary 5.7. Concretely, the implication says that if Conjecture CA is true in degree N N over a field 𝕂 \mathbb{K}, then there are only finitely many (up to affine transformations) monic univariate degree N + 1 N+1 polynomials f f over 𝕂 \mathbb{K} satisfying the (weaker) condition gcd ⁡ ( f, f i) ≠ 1 \gcd(f,f_{i})\neq 1 for each i = 1, …, N − 1 i=1,\dots,N-1.

## References

- [1] E. Casas-Alvero (2001) Higher order polar germs. J. Algebra 240 ( 1), pp. 326–337. External Links: ISSN 0021-8693, [Link][4], Review [MathReviews][5] Cited by: §1.1.
- [2] W. Castryck, R. Laterveer, and M. Ounaïes (2014) Constraints on counterexamples to the Casas-Alvero conjecture and a verification in degree 12. Math. Comp. 83 ( 290), pp. 3017–3037. External Links: ISSN 0025-5718, [Link][6], Review [MathReviews][7] Cited by: §1.1, §1.2.
- [3] M. Chellali and A. Salinier (2012) La conjecture de Casas Alvero pour les degrés 5 ​ p e 5p^{e}. An. Univ. Dunărea de Jos Galaţi Fasc. II Mat. Fiz. Mec. Teor. 4(35) ( 1-2), pp. 54–62. External Links: ISSN 2067-2071, Review [MathReviews][8] Cited by: §1.1, §1.2.
- [4] G. M. Diaz-Toca and L. Gonzalez-Vega (2006) On analyzing a conjecture about univariate polynomials and their roots by using Maple. In Proceedings of the Maple Conference 2006, Waterloo (Canada), July 23-26, 2006, pp. 81–98. Cited by: §1.2.
- [5] J. Draisma and J. P. de Jong (2011) On the Casas-Alvero conjecture. Eur. Math. Soc. Newsl. ( 80), pp. 29–33. External Links: ISSN 1027-488X, Review [MathReviews][9] Cited by: §1.1, §1.2, §1.2, §5.2, §5, Proposition.
- [6] I. M. Gelfand, M. M. Kapranov, and A. V. Zelevinsky (2008) Discriminants, resultants and multidimensional determinants. Modern Birkhäuser Classics, Birkhäuser Boston, Inc., Boston, MA. Note: Reprint of the 1994 edition External Links: ISBN 978-0-8176-4770-4, Review [MathReviews][10] Cited by: item iii.
- [7] H. Graf von Bothmer, O. Labs, J. Schicho, and C. van de Woestijne (2007) The Casas-Alvero conjecture for infinitely many degrees. J. Algebra 316 ( 1), pp. 224–230. External Links: ISSN 0021-8693, [Link][11], Review [MathReviews][12] Cited by: §1.1, §1.2, §1.2, §1.3, §4.3, §6, Proposition.
- [8] A. Grothendieck (1966) Éléments de géométrie algébrique. iv. Étude locale des schémas et des morphismes de schémas. iii (rédigés avec la collaboration de j. dieudonné). Inst. Hautes Études Sci. Publ. Math. ( 28), pp. 255. External Links: ISSN 0073-8301, Review [MathReviews][13] Cited by: §5.1.
- [9] R. Hartshorne (1977) Algebraic geometry. , Vol. No. 52., Springer-Verlag, New York-Heidelberg. External Links: ISBN 0-387-90244-9, Review [MathReviews][14] Cited by: §5.1, §5.3.
- [10] T. Hosgood (2020) An introduction to varieties in weighted projective space. External Links: math.AG/1604.02441 Cited by: §4.3.
- [11] F. Ischebeck and R. A. Rao (2005) Ideals and reality. Springer Monographs in Mathematics, Springer-Verlag, Berlin. Note: Projective modules and number of generators of ideals External Links: ISBN 3-540-23032-7, Review [MathReviews][15] Cited by: §5.2.1.
- [12] N. M. Katz (2001) Sums of betti numbers in arbitrary characteristic. Finite Fields Appl. 7 ( 1), pp. 29–44. Note: Dedicated to Professor Chao Ko on the occasion of his 90th birthday External Links: ISSN 1071-5797, Review [MathReviews][16], [Document][17] Cited by: Remark 5.12.
- [13] Q. Liu (2002) Algebraic geometry and arithmetic curves. Oxford Graduate Texts in Mathematics, Vol. 6, Oxford University Press, Oxford. Note: Translated from the French by Reinie Erné; Oxford Science Publications External Links: ISBN 0-19-850284-2, Review [MathReviews][18] Cited by: §5.3.
- [14] B. Poonen (2017) Rational points on varieties. Graduate Studies in Mathematics, Vol. 186, American Mathematical Society, Providence, RI. External Links: ISBN 978-1-4704-3773-2, Review [MathReviews][19], [Document][20] Cited by: §5.1.
- [15] D. Schaub and M. Spivakovsky (2024) On the set of bad primes in the study of the casas–alvero conjecture. Res. Math. Sci. 11 ( 2), pp. Paper No. 31. External Links: ISSN 2522-0144, Review [MathReviews][21], [Document][22] Cited by: §1.2, Remark 5.10.
- [16] F. K. Schmidt and H. Hasse (1937) Noch eine begründung der theorie der höheren differentialquotienten in einem algebraischen funktionenkörper einer unbestimmten. (nach einer brieflichen mitteilung von f.k. schmidt in jena). J. Reine Angew. Math. 177, pp. 215–237 ( German). External Links: ISSN 0075-4102, Review [MathReviews][23], [Document][24] Cited by: item i.
- [17] T. Stacks project authors (2023) The stacks project. External Links: [Link][25] Cited by: §5.1, §5.3, Remark 5.5, Remark 5.9, §6.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
[4]: https://doi.org/10.1006/jabr.2000.8727
[5]: http://www.ams.org/mathscinet-getitem?mr=1830556
[6]: https://doi.org/10.1090/S0025-5718-2014-02809-3
[7]: http://www.ams.org/mathscinet-getitem?mr=3246822
[8]: http://www.ams.org/mathscinet-getitem?mr=3136558
[9]: http://www.ams.org/mathscinet-getitem?mr=2848893
[10]: http://www.ams.org/mathscinet-getitem?mr=2394437
[11]: https://doi.org/10.1016/j.jalgebra.2007.06.017
[12]: http://www.ams.org/mathscinet-getitem?mr=2354861
[13]: http://www.ams.org/mathscinet-getitem?mr=0217086
[14]: http://www.ams.org/mathscinet-getitem?mr=0463157
[15]: http://www.ams.org/mathscinet-getitem?mr=2114392
[16]: http://www.ams.org/mathscinet-getitem?mr=1803934
[17]: https://dx.doi.org/10.1006/ffta.2000.0303
[18]: http://www.ams.org/mathscinet-getitem?mr=1917232
[19]: http://www.ams.org/mathscinet-getitem?mr=3729254
[20]: https://dx.doi.org/10.1090/gsm/186
[21]: http://www.ams.org/mathscinet-getitem?mr=4729911
[22]: https://dx.doi.org/10.1007/s40687-024-00444-z
[23]: http://www.ams.org/mathscinet-getitem?mr=1581557
[24]: https://dx.doi.org/10.1515/crll.1937.177.215
[25]: https://stacks.math.columbia.edu
