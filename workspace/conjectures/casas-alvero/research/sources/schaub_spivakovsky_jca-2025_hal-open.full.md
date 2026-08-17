<!-- source: https://hal.science/hal-04341794/document | converted from PDF -->

HAL Id: hal-04341794

https://hal.science/hal-04341794v3

Submitted on 5 Feb 2025

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

On the Casas-Alvero Conjecture

Daniel Schaub, Mark Spivakovsky

To cite this version:

Daniel Schaub, Mark Spivakovsky. On the Casas-Alvero Conjecture. Journal of Commutative Algebra, 2025,
17 (2), pp.199-202. ⟨10.1216/jca.2025.17.199⟩. ⟨hal-04341794v3⟩

A note on the Casas-Alvero Conjecture

Daniel Schaub, Univ Angers, CNRS, LAREMA, SFR MATHSTIC
F-49000 Angers, France
email: daniel.schaub@univ-angers.fr

Mark Spivakovsky, Univ Paul Sabatier, CNRS, IMT UMR 5219
F-31062 Toulouse, France and
CNRS, LaSol UMI 2001, UNAM.
email: mark.spivakovsky@math.univ-toulouse.fr

February 5, 2025

Abstract

The Casas–Alvero conjecture predicts that every univariate polynomial f over a field
K of characteristic zero having a common factor with each of its derivatives Hi(f ) is a
power of a linear polynomial. Let f = xd + a1xd−1 + · · · + a1x ∈ K[a1, . . . , ad−1][x] and let
Ri = Res(f, Hi(f )) ∈ K[a1, . . . , ad−1] be the resultant of f and Hi(f ), i ∈ {1, . . . , d − 1}.
The Casas-Alvero Conjecture is equivalent to saying that R1, . . . , Rd−1 are “independent”
in a certain sense, namely that the height ht(R1, . . . , Rd−1) = d − 1 in K[a1, . . . , ad−1].
In this paper we prove a partial result in this direction: if i ∈ {d − 3, d − 2, d − 1} then

Ri∈/
√(R1, . . . , ˘Ri, . . . , Rd−1).

1 Introduction

In the year 2001 Eduardo Casas–Alvero published a paper on higher order polar germs of plane
curve singularities [1]. His work on polar germs inspired him to make the following conjecture
(according to the testimony of Jos´e Manuel Aroca, E. Casas communicated the problem orally
well before 2001).
Let K be a field, d a strictly positive integer and f = xd + a1xd−1 + · · · + ad−1x + ad a
monic univariate polynomial of degree d over K. Let

Hi(f ) = (
d
i
)xd−i + (
d − 1
i
 )a1xd−i−1 + · · · + (
i
i

)ad−i

be the i-th Hasse derivative of f .

Definition 1 The polynomial f is said to be a Casas–Alvero polynomial if for each i ∈
{1, . . . , d − 1} it has a non-constant common factor with its i-th Hasse derivative Hi(f ).

Note that, by definition, a Casas-Alvero polynomial f has a common root with Hd−1(f ).
In particular, if char K = 0, it has at least one root b ∈ K, regardless of whether or not K
is algebraically closed. Making the change of variables x ⇝ x − b, we may assume that 0 is a
root of f , in other words, ad = 0. In the sequel, we will always make this assumption without
mentioning it explicitly.
 1

Conjecture 1 (Casas–Alvero) Assume that char K = 0. If f ∈ K[x] is a Casas-Alvero
polynomial of degree d with ad = 0, then f (x) = xd.

For i ∈ {1, . . . , d − 1}, let Ri = Res(f, Hi(f )) ∈ K[a1, . . . , ad−1] be the resultant of f and
Hi(f ). The polynomials f and Hi(f ) have a common factor if and only if Ri = 0. Thus f
is Casas–Alvero if and only if the point (a1, . . . , ad−1) ∈ Kd−1 belongs to the algebraic variety
V (R1, . . . , Rd−1) ⊂ Kd−1. In those terms the Conjecture can be reformulated as follows:

Conjecture 2 Let V = V (R1, . . . , Rd−1) ⊂ Kd−1. Then V = {0}.

If the field K is algebraically closed then Conjecture 2 is also eqiuvalent to

Conjecture 3 We have √(R1, . . . , Rd−1) = (a1, . . . , ad−1) (1)

or, equivalently,

a
N
i ∈ (R1, . . . , Rd−1) for all i ∈ {1, . . . , d − 1} and some N ∈ N. (2)

For non-algebraically closed fields Conjecture 3 is a priori stronger than Conjecture 2.

Remark 2 Let K ⊂ K′ be a field extension. The induced extension

K[a1, . . . , ad−1] ⊂ K′[a1, . . . , ad−1]

is faithfully flat. Since the polynomials R1, . . . , Rd−1 have coefficients in Z, (2) holds in
K[a1, . . . , ad−1] if and only if it holds in K′[a1, . . . , ad−1]. Hence the truth of Conjecture 3
for any given d depends only on the characteristic of K but not on the choice of the field K
itself. Because of this, we will take K = C in the sequel.

Remark 3 Formulae (1) and (2) can be interpreted in terms of Gr¨obner bases. Namely, (1)
and (2) are equivalent to saying that for any choice of monomial ordering and Gr¨obner basis
(f1, . . . , fs) of (R1, . . . , Rd−1), after renumbering the fj, the leading monomial of fj is a power
of aj for j ∈ {1, . . . , d − 1}.

Remark 4 Conjecture 3 and Remark 3 say that, as polynomials in K[a1, . . . , ad−1], the resul-
tants R1, . . . , Rd−1 are “independent” in a certain sense.
Each of the following statements is also equivalent to Conjecture 3.

(a) For each i ∈ {1, . . . , d − 2}, the element Ri+1 is not a zero divisor modulo (R1, . . . , Ri) (in
other words, R1, . . . , Rd−1 form a regular sequence in K[a1, . . . , ad−1]).

(b) For each i ∈ {1, . . . , d − 2}, Ri+1∈/ ⋃

p∈Ass((R1,...,Ri)) p.

where Ass((R1, . . . , Ri)) is the set of associated primes of the ideal (R1, . . . , Ri).

Moreover, the above statements (a) and (b) are independent of the numbering of the Ri; a
permutation of the Ri yields equivalent statements.

2

Notation. We will denote by (R1, R2, . . . , ˘Ri, . . . , Rd−1) the ideal of K[a1, . . . , ad−1] generated
by the set {R1, R2, . . . , Rd−1} \ {Ri}.

The main theorem of this paper is the following partial result in the direction of Conjecture
3 and statements (a) and (b) of Remark 4.

Theorem 5 Take an element i ∈ {d − 3, d − 2, d − 1}. We have

Ri∈/√
(R1, R2, . . . , ˘Ri, . . . , Rd−1).

Added in press: In two recent preprints [6] and [7] Soham Ghosh gave a complete proof of
the Casas–Alvero conjecture.

2 Ideals generated by all the resultants but one

In this section we prove Theorem 5 after recalling some preliminary results.

Proposition 6 Let f be a polynomial of degree d with real roots β1 ≤ β2 ≤ . . . ≤ βd, counted
with multiplicity. Then H1(f ) has real roots γ1 ≤ γ2 ≤ . . . ≤ γd−1, counted with multiplicity,
where γi ∈]βi, βi+1[ if βi < βi+1 and γi = βi if βi = βi+1.

Proof: Assume that f has s distincts roots δ1 < δ2 < · · · < δs of multiplicities m1, . . . , ms,
respectively. Then δj is a root of H1(f ) of multiplicity mj − 1, where we say that δj is a root of
multiplicity 0 if it is not a root of H1(f ).
By Rolle’s theorem, there is at least one root of H1(f ) in each of the s − 1 open intervals
]δ1, δ2[, . . . , ]δs−1, δs[.

Notation. Let Int(βi, βi+1) :=]βi, βi+1[ if βi < βi+1 and Int(βi, βi+1) := {βi} if βi = βi+1.

According to the above, there is at least one real root of H1(f ) in each of Int(βi, βi+1),
i ∈ {1, . . . , d − 1}, where γ1 ∈ Int(β1, β2), . . . , γm1−1 ∈ Int(βm1−1, βm1) are the first m1 − 1 roots
of H1(f ) (in fact, the same root counted with multiplicity m1 − 1) and similarly for the other
multiple roots of f .
We have accounted for a total of s−1+(m1 −1)+· · ·+(ms −1) = m1 +· · ·+ms −1 = d−1
real roots of H1(f ) counted with multiplicities. Hence H1(f ) has no roots, real or complex, other
than the ones listed above, and the result follows. □

Corollary 7 Let f be a polynomial of degree d with d real roots, counted with multipliciites.
Then each of the Hi(f ), i ∈ {1, . . . , d − 1}, has d − i real roots, counted with multiplicity. In
other words, all the roots of Hi(f ) are real.

Next, we recall a result from [5] on almost counterexamples to the Casas-Alvero conjecture.

Definition 8 Fix an i ∈ {1, . . . , d − 1}. An almost counterexample to the Casas-Alvero
conjecture of level i is a polynomial f that has a common root with Hj(f ) for all j ∈ {1, . . . , d−
1} \ {i} but is not a power of a linear polynomial.

Notation. Given a polynomial f of degree d with d real roots, for a pair (k, m) of integers with
1 ≤ k ≤ d − 1 and 1 ≤ m ≤ d − k we write αk,m(f ) for the m-th root of Hk(f ), where the roots
of Hk(f ) are ordered (weakly) increasingly.

We state the next theorem in a somewhat stronger form than in [5]: the extra information
about the recycled roots αkj ,mj (f ) does not appear explicitly in the statement of the result in
[5], but is shown in the course of its proof.
 3

Theorem 9 (J. Draisma–J. P. de Jong [5], Theorem 5) Fix d − 2 pairs of integers

(kj, mj), j ∈ {1, . . . , d − 2},

with 1 ≤ k1 < k2 < · · · < kd−2 ≤ d − 1

and 1 ≤ mj ≤ d − kj. There exists a polynomial f ∈ R[x] with f (0) = f (1) = 0, all of whose
roots are real and lie in [0, 1], such that αkj ,mj (f ) is a root of f for all j ∈ {1, . . . , d − 2} (in
particular, f is an almost counterexample to the Casas-Alvero conjecture of level i, where i is
the unique element of the set {1, . . . , d − 1} \ {k1, . . . , kd−2}).

We also recall the following result, Theorem 13 of [2]:

Theorem 10 Assume that f is a counterexample to the Casas-Alvero Conjecture. Then f has
at least five distinct roots.

Proof of Theorem 5: We argue by contradiction. Assume that

Ri ∈ √
(R1, . . . , ˘Ri, . . . , Rd−1). (3)

Let f be an almost counterexample of level i to the Casas-Alvero conjecture with mj = 1 for
all j ∈ {1, . . . , d − 2}, given by Theorem 9. By (3), f is a Casas-Alvero polynomial that is a
counterexample to the Casas-Alvero conjecture. By definition of f , αkj 1(f ) is the first root of
Hkj (f ) and also a root of f , for all j ∈ {1, . . . , d − 2}. In particular, since i ∈ {d − 3, d − 2, d − 1},
αℓ1(f ) is the first root of Hℓ(f ) and a root of f for all ℓ ∈ {1, . . . , d − 4}.
By Proposition 6, α11(f ) is also the first root of f (so α11(f ) = 0). Let m denote the
multiplicity of this root of f . Since 0 is a root of f of multiplicity m, it is also the first root
of Hℓ(f ) for all 1 ≤ ℓ ≤ m − 1 (again by Proposition 6). In other words, αℓ1(f ) = 0 for all
1 ≤ ℓ ≤ m − 1. By Theorem 10, f has at least 5 distinct roots, hence m ≤ d − 4. Let β denote
the first strictly positive root of f .
By Proposition 6, there is a unique root β(1) of H1(f ) with β(1) ∈]0, β[. If m > 2, again
by Proposition 6, there is a unique root β(2) of H2(f ) with β(2) ∈]0, β(1)[⊂]0, β[. We continue
like this recursively until Hm−1(f ), to show that there is a unique root β(m−1) of Hm−1(f ) with
β(m−1) ∈]0, β(m−2)[⊂]0, β[. Now, Hm(f ) has no root at 0, hence its first root αm1(f ) belongs to
the open interval ]0, β(m−1)[⊂]0, β[.
This contradicts the fact that αm1(f ) is a root of f . □

References

[1] Eduardo Casas–Alvero, Higher Order Polar Germs, Journal of Algebra, Volume 240, Issue
1, 1 June 2001, pages 326–337

[2] W. Castryck, R. Laterveer, M. Ouna¨ıes, Constraints on counterexamples to the Casa-Alvero
conjecture and a verification in degree 12, arXiv:1208.5404v1, 27/08/2018.

[3] R.M. de Frutos Mar´ın, Perspectivas Aritm´eticas para la Conjectura de Casas–Alvero, PhD
thesis, Universidad de Valladolid, 2012.

[4] A. Salinier, M. Chellali, La conjecture de Casas-Alvero pour les degr´es 5pe, hal-00748843,
2012.
 4

[5] J. Draisma and J.P. de Jong, On the Casas-Alvero conjecture, Newsletter of the EMS 80
(June 2011) 29–33

[6] Soham Ghosh, A finiteness result towards the Casas-Alvero Conjecture, arXiv:2402.18717,
2024

[7] Soham Ghosh, Proof of the Casas-Alvero conjecture, arXiv:2501.09272, January 2025

[8] H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. Van de Woestline, The Casas-Alvero
conjecture for infinitely many degrees Journal of Algebra, Vol. 316(1), 224-230, 2007.

5
