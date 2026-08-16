<!-- source: https://arxiv.org/html/2312.08742v7 | converted from HTML -->

A note on the Casas-Alvero Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2312.08742v7 [math.AC] 11 Feb 2025

# A note on the Casas-Alvero Conjecture

Daniel Schaub Univ Angers CNRS LAREMA SFR MATHSTIC Affiliation: F-49000 Angers, France Affiliation: email: daniel.schaub@univ-angers.fr Mark Spivakovsky Univ Paul Sabatier CNRS IMT UMR 5219 Affiliation: F-31062 Toulouse, France and Affiliation: CNRS, LaSol UMI 2001, UNAM. Affiliation: email: mark.spivakovsky@math.univ-toulouse.fr

###### Abstract

The Casas–Alvero conjecture predicts that every univariate polynomial f f over a field K K of characteristic zero having a common factor with each of its derivatives H i ​ ( f) H_{i}(f) is a power of a linear polynomial. Let f = x d + a 1 ​ x d − 1 + ⋯ + a 1 ​ x ∈ K ⁡ [a 1, …, a d − 1] ​ [x] f=x^{d}+a_{1}x^{d-1}+\cdots+a_{1}x\in K[a_{1},\ldots,a_{d-1}][x] and let R i = R ​ e ​ s ​ ( f, H i ​ ( f)) ∈ K ⁡ [a 1, …, a d − 1] R_{i}=Res(f,H_{i}(f))\in K[a_{1},\ldots,a_{d-1}] be the resultant of f f and H i ​ ( f) H_{i}(f), i ∈ { 1, …, d − 1 } i\in\{1,\ldots,d-1\}. The Casas-Alvero Conjecture is equivalent to saying that R 1, …, R d − 1 R_{1},\ldots,R_{d-1} are “independent” in a certain sense, namely that the height h ​ t ​ ( R 1, …, R d − 1) = d − 1 ht(R_{1},\ldots,R_{d-1})=d-1 in K ⁡ [a 1, …, a d − 1] K[a_{1},\ldots,a_{d-1}]. In this paper we prove a partial result in this direction: if i ∈ { d − 3, d − 2, d − 1 } i\in\{d-3,d-2,d-1\} then R i ​ ∈ / ​ ( R 1, …, R i ˘, …, R d − 1) R_{i}\mbox{$\in$ \hskip-8.00003pt/}\sqrt{(R_{1},\ldots,\breve{R_{i}},\ldots,R_{d-1})}.

## 1 Introduction

In the year 2001 Eduardo Casas–Alvero published a paper on higher order polar germs of plane curve singularities [1]. His work on polar germs inspired him to make the following conjecture (according to the testimony of José Manuel Aroca, E. Casas communicated the problem orally well before 2001).

Let K K be a field, d d a strictly positive integer and f = x d + a 1 ​ x d − 1 + ⋯ + a d − 1 ​ x + a d f=x^{d}+a_{1}x^{d-1}+\cdots+a_{d-1}x+a_{d} a monic univariate polynomial of degree d d over K K. Let

 | H i ​ ( f) = ( d i) ​ x d − i + ( d − 1 i) ​ a 1 ​ x d − i − 1 + ⋯ + ( i i) ​ a d − i H_{i}(f)=\binom{d}{i}x^{d-i}+\binom{d-1}{i}a_{1}x^{d-i-1}+\cdots+\binom{i}{i}a_{d-i} |  |

be the i i -th Hasse derivative of f f.

###### Definition 1

The polynomial f f is said to be a Casas–Alvero polynomial if for each i ∈ { 1, …, d − 1 } i\in\{1,\ldots,d-1\} it has a non-constant common factor with its i i -th Hasse derivative H i ​ ( f) H_{i}(f).

Note that, by definition, a Casas-Alvero polynomial f f has a common root with H d − 1 ​ ( f) H_{d-1}(f). In particular, if char ​ K = 0 \text{char}\ K=0, it has at least one root b ∈ K b\in K, regardless of whether or not K K is algebraically closed. Making the change of variables x ↝ x − b x\rightsquigarrow x-b, we may assume that 0 0 is a root of f f, in other words, a d = 0 a_{d}=0. In the sequel, we will always make this assumption without mentioning it explicitly.

###### Conjecture 1

(Casas–Alvero) Assume that char ​ K = 0 \text{char}\ K=0. If f ∈ K ⁡ [x] f\in K[x] is a Casas-Alvero polynomial of degree d d with a d = 0 a_{d}=0, then f ⁡ ( x) = x d f(x)=x^{d}.

For i ∈ { 1, …, d − 1 } i\in\{1,\ldots,d-1\}, let R i = Res ​ ( f, H i ​ ( f)) ∈ K ⁡ [a 1, …, a d − 1] R_{i}=\text{Res}(f,H_{i}(f))\in K[a_{1},\ldots,a_{d-1}] be the resultant of f f and H i ​ ( f) H_{i}(f). The polynomials f f and H i ​ ( f) H_{i}(f) have a common factor if and only if R i = 0 R_{i}=0. Thus f f is Casas–Alvero if and only if the point ( a 1, …, a d − 1) ∈ K d − 1 (a_{1},\ldots,a_{d-1})\in K^{d-1} belongs to the algebraic variety V ⁡ ( R 1, …, R d − 1) ⊂ K d − 1 V(R_{1},\dots,R_{d-1})\subset K^{d-1}. In those terms the Conjecture can be reformulated as follows:

###### Conjecture 2

Let V = V ⁡ ( R 1, …, R d − 1) ⊂ K d − 1 V=V(R_{1},\ldots,R_{d-1})\subset K^{d-1}. Then V = { 0 } V=\{0\}.

If the field K K is algebraically closed then Conjecture 2 is also eqiuvalent to

###### Conjecture 3

We have

 | ( R 1, …, R d − 1) = ( a 1, …, a d − 1) \sqrt{(R_{1},\ldots,R_{d-1})}=(a_{1},\ldots,a_{d-1}) |  | (1) |

or, equivalently,

 | a i N ∈ ( R 1, …, R d − 1) ​ for all ​ i ∈ { 1, …, d − 1 } ​ and some ​ N ∈ ℕ. a_{i}^{N}\in(R_{1},\ldots,R_{d-1})\text{ for all }i\in\{1,\ldots,d-1\}\text{ and some }N\in\mathbb{N}. |  | (2) |

For non-algebraically closed fields Conjecture 3 is a priori stronger than Conjecture 2.

###### Remark 2

Let K ⊂ K ′ K\subset K^{\prime} be a field extension. The induced extension

 | K ⁡ [a 1, …, a d − 1] ⊂ K ′ ​ [a 1, …, a d − 1] K[a_{1},\ldots,a_{d-1}]\subset K^{\prime}[a_{1},\ldots,a_{d-1}] |  |

is faithfully flat. Since the polynomials R 1, …, R d − 1 R_{1},\ldots,R_{d-1} have coefficients in ℤ \mathbb{Z}, ( 2) holds in K ⁡ [a 1, …, a d − 1] K[a_{1},\ldots,a_{d-1}] if and only if it holds in K ′ ​ [a 1, …, a d − 1] K^{\prime}[a_{1},\ldots,a_{d-1}]. Hence the truth of Conjecture 3 for any given d d depends only on the characteristic of K K but not on the choice of the field K K itself. Because of this, we will take K = ℂ K=\mathbb{C} in the sequel.

###### Remark 3

Formulae ( 1) and ( 2) can be interpreted in terms of Gröbner bases. Namely, ( 1) and ( 2) are equivalent to saying that for any choice of monomial ordering and Gröbner basis ( f 1, …, f s) (f_{1},\ldots,f_{s}) of ( R 1, …, R d − 1) (R_{1},\ldots,R_{d-1}), after renumbering the f j f_{j}, the leading monomial of f j f_{j} is a power of a j a_{j} for j ∈ { 1, …, d − 1 } j\in\{1,\dots,d-1\}.

###### Remark 4

Conjecture 3 and Remark 3 say that, as polynomials in K ⁡ [a 1, …, a d − 1] K[a_{1},\dots,a_{d-1}], the resultants R 1, …, R d − 1 R_{1},\dots,R_{d-1} are “independent” in a certain sense.

Each of the following statements is also equivalent to Conjecture 3.

1. (a)

For each i ∈ { 1, …, d − 2 } i\in\{1,\ldots,d-2\}, the element R i + 1 R_{i+1} is not a zero divisor modulo ( R 1, …, R i) (R_{1},\ldots,R_{i}) (in other words, R 1, …, R d − 1 R_{1},\dots,R_{d-1} form a regular sequence in K ⁡ [a 1, …, a d − 1] K[a_{1},\dots,a_{d-1}]).

2. (b)

For each i ∈ { 1, …, d − 2 } i\in\{1,\ldots,d-2\},

 | R i + 1 ​ ∈ / ​ ⋃ 𝔭 ∈ Ass ​ ( (,,,,,)) 𝔭. R_{i+1}\mbox{$\in$ \hskip-8.17776pt/}\bigcup\limits_{\mathfrak{p}\in\text{Ass}((R_{1},\ldots,R_{i}))}\mathfrak{p}. |  |

where Ass ​ ( (,,,,,)) \text{Ass}((R_{1},\ldots,R_{i})) is the set of associated primes of the ideal ( R 1, …, R i) (R_{1},\ldots,R_{i}).

Moreover, the above statements (a) and (b) are independent of the numbering of the R i R_{i}; a permutation of the R i R_{i} yields equivalent statements.

Notation. We will denote by ( R 1, R 2, …, R i ˘, …, R d − 1) (R_{1},R_{2},\ldots,\breve{R_{i}},\ldots,R_{d-1}) the ideal of K ⁡ [a 1, …, a d − 1] K[a_{1},\dots,a_{d-1}] generated by the set { R 1, R 2, …, R d − 1 } ∖ { R i } \{R_{1},R_{2},\ldots,R_{d-1}\}\setminus\{R_{i}\}.

The main theorem of this paper is the following partial result in the direction of Conjecture 3 and statements (a) and (b) of Remark 4.

###### Theorem 5

Take an element i ∈ { d − 3, d − 2, d − 1 } i\in\{d-3,d-2,d-1\}. We have

 | R i ​ ∈ / ​ ( R 1, R 2, …, R i ˘, …, R d − 1). R_{i}\mbox{$\in$ \hskip-8.17776pt/}\sqrt{(R_{1},R_{2},\ldots,\breve{R_{i}},\ldots,R_{d-1})}. |  |

Added in press: In two recent preprints [6] and [7] Soham Ghosh gave a complete proof of the Casas–Alvero conjecture.

## 2 Ideals generated by all the resultants but one

In this section we prove Theorem 5 after recalling some preliminary results.

###### Proposition 6

Let f f be a polynomial of degree d d with real roots β 1 ≤ β 2 ≤ … ≤ β d \beta_{1}\leq\beta_{2}\leq\ldots\leq\beta_{d}, counted with multiplicity. Then H 1 ​ ( f) H_{1}(f) has real roots γ 1 ≤ γ 2 ≤ … ≤ γ d − 1 \gamma_{1}\leq\gamma_{2}\leq\ldots\leq\gamma_{d-1}, counted with multiplicity, where γ i ∈] β i, β i + 1 [\gamma_{i}\in]\beta_{i},\beta_{i+1}[if β i < β i + 1 \beta_{i}<\beta_{i+1} and γ i = β i \gamma_{i}=\beta_{i} if β i = β i + 1 \beta_{i}=\beta_{i+1}.

Proof: Assume that f f has s s distincts roots δ 1 < δ 2 < ⋯ < δ s \delta_{1}<\delta_{2}<\cdots<\delta_{s} of multiplicities m 1, …, m s m_{1},\ldots,m_{s}, respectively. Then δ j \delta_{j} is a root of H 1 ​ ( f) H_{1}(f) of multiplicity m j − 1 m_{j}-1, where we say that δ j \delta_{j} is a root of multiplicity 0 if it is not a root of H 1 ​ ( f) H_{1}(f).

By Rolle’s theorem, there is at least one root of H 1 ​ ( f) H_{1}(f) in each of the s − 1 s-1 open intervals ] δ 1, δ 2 [, …,] δ s − 1, δ s []\delta_{1},\delta_{2}[,\ldots,]\delta_{s-1},\delta_{s}[.

Notation. Let Int ( β i, β i + 1):=] β i, β i + 1 [(\beta_{i},\beta_{i+1}):=]\beta_{i},\beta_{i+1}[if β i < β i + 1 \beta_{i}<\beta_{i+1} and Int ( β i, β i + 1):= { β i } (\beta_{i},\beta_{i+1}):=\{\beta_{i}\} if β i = β i + 1 \beta_{i}=\beta_{i+1}.

According to the above, there is at least one real root of H 1 ​ ( f) H_{1}(f) in each of Int ( β i, β i + 1) (\beta_{i},\beta_{i+1}), i ∈ { 1, …, d − 1 } i\in\{1,\ldots,d-1\}, where γ 1 ∈ Int ​ ( β 1, β 2) \gamma_{1}\in\text{Int}(\beta_{1},\beta_{2}), …, γ m 1 − 1 ∈ Int ​ ( β m 1 − 1, β m 1) \gamma_{m_{1}-1}\in\text{Int}(\beta_{m_{1}-1},\beta_{m_{1}}) are the first m 1 − 1 m_{1}-1 roots of H 1 ​ ( f) H_{1}(f) (in fact, the same root counted with multiplicity m 1 − 1 m_{1}-1) and similarly for the other multiple roots of f f.

We have accounted for a total of s − 1 + ( m 1 − 1) + ⋯ + ( m s − 1) = m 1 + ⋯ + m s − 1 = d − 1 s-1+(m_{1}-1)+\cdots+(m_{s}-1)=m_{1}+\cdots+m_{s}-1=d-1 real roots of H 1 ​ ( f) H_{1}(f) counted with multiplicities. Hence H 1 ​ ( f) H_{1}(f) has no roots, real or complex, other than the ones listed above, and the result follows. □ \Box

###### Corollary 7

Let f f be a polynomial of degree d d with d d real roots, counted with multipliciites. Then each of the H i ​ ( f) H_{i}(f), i ∈ { 1, …, d − 1 } i\in\{1,\ldots,d-1\}, has d − i d-i real roots, counted with multiplicity. In other words, all the roots of H i ​ ( f) H_{i}(f) are real.

Next, we recall a result from [5] on almost counterexamples to the Casas-Alvero conjecture.

###### Definition 8

Fix an i ∈ { 1, …, d − 1 } i\in\{1,\ldots,d-1\}. An almost counterexample to the Casas-Alvero conjecture of level i i is a polynomial f f that has a common root with H j ​ ( f) H_{j}(f) for all j ∈ { 1, …, d − 1 } ∖ { i } j\in\{1,\ldots,d-1\}\setminus\{i\} but is not a power of a linear polynomial.

Notation. Given a polynomial f f of degree d d with d d real roots, for a pair ( k, m) (k,m) of integers with 1 ≤ k ≤ d − 1 1\leq k\leq d-1 and 1 ≤ m ≤ d − k 1\leq m\leq d-k we write α k, m ​ ( f) \alpha_{k,m}(f) for the m m -th root of H k ​ ( f) H_{k}(f), where the roots of H k ​ ( f) H_{k}(f) are ordered (weakly) increasingly.

We state the next theorem in a somewhat stronger form than in [5]: the extra information about the recycled roots α k j, m j ​ ( f) \alpha_{k_{j},m_{j}}(f) does not appear explicitly in the statement of the result in [5], but is shown in the course of its proof.

###### Theorem 9 (J. Draisma–J. P. de Jong [5], Theorem 5)

Fix d − 2 d-2 pairs of integers

 | ( k j, m j), j ∈ { 1, …, d − 2 }, (k_{j},m_{j}),\quad j\in\{1,\ldots,d-2\}, |  |

with

 | 1 ≤ k 1 < k 2 < ⋯ < k d − 2 ≤ d − 1 1\leq k_{1}<k_{2}<\dots<k_{d-2}\leq d-1 |  |

and 1 ≤ m j ≤ d − k j 1\leq m_{j}\leq d-k_{j}. There exists a polynomial f ∈ ℝ ⁡ [x] f\in\mathbb{R}[x] with f ⁡ ( 0) = f ⁡ ( 1) = 0 f(0)=f(1)=0, all of whose roots are real and lie in [0, 1] [0,1], such that α k j, m j ​ ( f) \alpha_{k_{j},m_{j}}(f) is a root of f f for all j ∈ { 1, …, d − 2 } j\in\{1,\ldots,d-2\} (in particular, f f is an almost counterexample to the Casas-Alvero conjecture of level i i, where i i is the unique element of the set { 1, …, d − 1 } ∖ { k 1, …, k d − 2 } \{1,\dots,d-1\}\setminus\{k_{1},\dots,k_{d-2}\}).

We also recall the following result, Theorem 13 of [2]:

###### Theorem 10

Assume that f f is a counterexample to the Casas-Alvero Conjecture. Then f f has at least five distinct roots.

Proof of Theorem 5: We argue by contradiction. Assume that

 | R i ∈ ( R 1, …, R i ˘, …, R d − 1). R_{i}\in\sqrt{(R_{1},\ldots,\breve{R_{i}},\ldots,R_{d-1})}. |  | (3) |

Let f f be an almost counterexample of level i i to the Casas-Alvero conjecture with m j = 1 m_{j}=1 for all j ∈ { 1, …, d − 2 } j\in\{1,\ldots,d-2\}, given by Theorem 9. By ( 3), f f is a Casas-Alvero polynomial that is a counterexample to the Casas-Alvero conjecture. By definition of f f, α k j ​ 1 ​ ( f) \alpha_{k_{j}1}(f) is the first root of H k j ​ ( f) H_{k_{j}}(f) and also a root of f f, for all j ∈ { 1, …, d − 2 } j\in\{1,\ldots,d-2\}. In particular, since i ∈ { d − 3, d − 2, d − 1 } i\in\{d-3,d-2,d-1\}, α ℓ ​ 1 ​ ( f) \alpha_{\ell 1}(f) is the first root of H ℓ ​ ( f) H_{\ell}(f) and a root of f f for all ℓ ∈ { 1, …, d − 4 } \ell\in\{1,\ldots,d-4\}.

By Proposition 6, α 11 ​ ( f) \alpha_{11}(f) is also the first root of f f (so α 11 ​ ( f) = 0 \alpha_{11}(f)=0). Let m m denote the multiplicity of this root of f f. Since 0 is a root of f f of multiplicity m m, it is also the first root of H ℓ ​ ( f) H_{\ell}(f) for all 1 ≤ ℓ ≤ m − 1 1\leq\ell\leq m-1 (again by Proposition 6). In other words, α ℓ ​ 1 ​ ( f) = 0 \alpha_{\ell 1}(f)=0 for all 1 ≤ ℓ ≤ m − 1 1\leq\ell\leq m-1. By Theorem 10, f f has at least 5 distinct roots, hence m ≤ d − 4 m\leq d-4. Let β \beta denote the first strictly positive root of f f.

By Proposition 6, there is a unique root β ( 1) \beta^{(1)} of H 1 ​ ( f) H_{1}(f) with β ( 1) ∈] 0, β [\beta^{(1)}\in]0,\beta[. If m > 2 m>2, again by Proposition 6, there is a unique root β ( 2) \beta^{(2)} of H 2 ​ ( f) H_{2}(f) with β ( 2) ∈] 0, β ( 1) [⊂] 0, β [\beta^{(2)}\in]0,\beta^{(1)}[\subset]0,\beta[. We continue like this recursively until H m − 1 ​ ( f) H_{m-1}(f), to show that there is a unique root β ( m − 1) \beta^{(m-1)} of H m − 1 ​ ( f) H_{m-1}(f) with β ( m − 1) ∈] 0, β ( m − 2) [⊂] 0, β [\beta^{(m-1)}\in]0,\beta^{(m-2)}[\subset]0,\beta[. Now, H m ​ ( f) H_{m}(f) has no root at 0, hence its first root α m ​ 1 ​ ( f) \alpha_{m1}(f) belongs to the open interval ] 0, β ( m − 1) [⊂] 0, β []0,\beta^{(m-1)}[\subset]0,\beta[.

This contradicts the fact that α m ​ 1 ​ ( f) \alpha_{m1}(f) is a root of f f. □ \Box

## References

- [1] Eduardo Casas–Alvero, Higher Order Polar Germs, Journal of Algebra, Volume 240, Issue 1, 1 June 2001, pages 326–337
- [2] W. Castryck, R. Laterveer, M. Ounaïes, Constraints on counterexamples to the Casa-Alvero conjecture and a verification in degree 12, arXiv:1208.5404v1, 27/08/2018.
- [3] R.M. de Frutos Marín, Perspectivas Aritméticas para la Conjectura de Casas–Alvero, PhD thesis, Universidad de Valladolid, 2012.
- [4] A. Salinier, M. Chellali, La conjecture de Casas-Alvero pour les degrés 5 ​ p e 5p^{e}, hal-00748843, 2012.
- [5] J. Draisma and J.P. de Jong, On the Casas-Alvero conjecture, Newsletter of the EMS 80 (June 2011) 29–33
- [6] Soham Ghosh, A finiteness result towards the Casas-Alvero Conjecture, arXiv:2402.18717, 2024
- [7] Soham Ghosh, Proof of the Casas-Alvero conjecture, arXiv:2501.09272, January 2025
- [8] H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. Van de Woestline, The Casas-Alvero conjecture for infinitely many degrees Journal of Algebra, Vol. 316(1), 224-230, 2007.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
