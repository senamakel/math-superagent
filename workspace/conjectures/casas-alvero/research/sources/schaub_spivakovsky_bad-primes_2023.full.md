<!-- source: https://arxiv.org/pdf/2307.05997 | converted from PDF -->

arXiv:2307.05997v2  [math.AC]  22 Aug 2023
On the set of bad primes in the study of the Casas–Alvero
conjecture

Daniel Schaub, Univ Angers, CNRS, LAREMA, SFR MATHSTIC
F-49000 Angers, France
email: daniel.schaub@univ-angers.fr

Mark Spivakovsky, Univ Paul Sabatier, CNRS, IMT UMR 5219
F-31062 Toulouse, France and
CNRS, LaSol UMI 2001, UNAM.
email: mark.spivakovsky@math.univ-toulouse.fr

August 23, 2023

Dedicated to Professor Osamu Saeki on the occasion of his sixtieth birthday

Abstract

The Casas–Alvero conjecture predicts that every univariate polynomial over a ﬁeld of
characteristic zero having a common factor with each of its derivatives Hi(f ) is a power of a
linear polynomial. One approach to proving the conjecture is to ﬁrst prove it for polynomials
of some small degree d, compile a list of bad primes for that degree (namely, those primes p for
which the conjecture fails in degree d and characteristic p) and then deduce the conjecture
for all degrees of the form dpℓ, ℓ ∈ N, where p is a good prime for d. In this paper we
calculate certain distinguished monomials appearing in the resultant R(f, Hi(f )) and obtain
a (non-exhaustive) list of bad primes for every degree d ∈ N \ {0}.

1 Introduction

In the year 2001 Eduardo Casas–Alvero published a paper on higher order polar germs of plane
curve singularities [1]. His work on polar germs inspired him to make the following conjecture
(according to the testimony of Jos´e Manuel Aroca, E. Casas communicated the problem orally
well before 2001).
Let K be a ﬁeld, d a strictly positive integer and f = xd + a1xd−1 + · · · + ad−1x + ad a
monic univariate polynomial of degree d over K. Let

Hi(f ) = (
d
i
)xd−i + (d − 1
i
 )a1xd−i−1 + · · · + (i
i

)ad−i

be the i-th Hasse derivative of f .

Deﬁnition 1 The polynomial f is said to be a Casas–Alvero polynomial if for each i ∈
{1, . . . , d − 1} it has a non-constant common factor with its i-th Hasse derivative Hi(f ).

1

Note that, by deﬁnition, a Casas-Alvero polynomial f has a common root with Hd−1(f ).
In particular, if char K = 0, it has at least one root b ∈ K, regardless of whether or not K
is algebraically closed. Making the change of variables x ⇝ x − b, we may assume that 0 is a
root of f , in other words, ad = 0. In the sequel, we will always make this assumption without
mentioning it explicitly.

Conjecture 1 (Casas–Alvero) Assume that char K = 0. If f ∈ K[x] is a Casas-Alvero
polynomial of degree d with ad = 0, then f (x) = xd.

For i ∈ {1, . . . , d − 1}, let Ri = R(f, Hi(f )) ∈ K[a1, . . . , ad−1] be the resultant of f and
Hi(f ). The polynomials f and Hi(f ) have a common factor if and only if Ri = 0. Thus f is
Casas–Alvero if and only if the point (a1, . . . , ad−1) ∈ V (R1, . . . , Rd−1) ⊂ K d−1. In those terms
the Conjecture can be reformulated as follows:

Conjecture 2 Let V = V (R1, . . . , Rd−1) ⊂ K d−1. Then V = {0}. In other words,
√(R1, . . . , Rd−1) = (a1, . . . , ad−1) (1)

or, equivalently,

a
N
i ∈ (R1, . . . , Rd−1) for all i ∈ {1, . . . , d − 1} and some N ∈ N. (2)

If char K = p > 0, the Conjecture is false in general. The simplest counterexample is the
polynomial f (x) = xp+1 − xp.

Remark 2 Let K ⊂ K ′ be a ﬁeld extension. The induced extension

K[a1, . . . , ad−1] ⊂ K ′[a1, . . . , ad−]

is faithfully ﬂat. Since the polynomials R1, . . . , Rd−1 have coeﬃcients in Z, (2) holds in
K[a1, . . . , ad−1] if and only if it holds in K ′[a1, . . . , ad−1]. Hence the truth of the conjecture
depends only on the characteristic of K but not on the choice of the ﬁeld K itself.

Remark 3 Formulae (1) and (2) can be interpreted in terms of Gr¨obner bases. Namely, (1)
and (2) are equivalent to saying that for any choice of monomial ordering and Gr¨obner basis
(f1, . . . , fs) of (R1, . . . , Rd−1), after renumbering the fj, the leading monomial of fj is a power
of aj.
 We will write CAd,p for the statement “The Casas-Alvero conjecture holds for polynomials
of degree d over ﬁelds of characteristic p”.
The following equivalences are known for each d ([5], [6]) :
CAd,0 holds ⇐⇒ CAd,p holds for some prime number p ⇐⇒ CAd,p holds for all but
ﬁnitely many primes p.

Deﬁnition 4 A prime number p is said to be a bad prime for d if CAd,p is false. If p is not
a bad prime for d, we will say that p is a good prime for d.

Proposition 5 ([6], Propositions 2.2 and 2.6) Take a strictly positive integer d, a prime number
p and a non-negative integer ℓ. Assume that CAd,p holds. Then so do CAdpℓ,p and CAdpℓ,0.

2

This result suggests the following general approach to the problem :
(1) prove the conjecture for a small number d;
(2) compile lists of good and bad primes for d;
(3) conclude that CAdpℓ,0 holds for all the primes p that are known to be good for d.
In particular, this shows the importance of knowing which primes are good or bad for a
given degree d.
The above approach has been carried out up to d ≤ 7 ([2], [3], [4], [5], [6]). Some integers
cannot be written in the form dpℓ where p is a good prime for d. For example,

12 = 2
2 · 3, 20 = 2
2 · 5, 24 = 2
3 · 3, 28 = 2
2 · 7, 30 = 2 · 3 · 5, 36 = 2
2 · 3
2, 40 = 2
3 · 5, . . .

CA12,0 has been proved by [2] with the aid of a computer, by using a very clever strategy
to cut down the computation of resultants and Gr¨obner basis. Thus the smallest degree d for
which CAd,0 is not known is d = 20.

In this paper we show that for each i ∈ {1, . . . , d − 1}, the monomials (1 − (d
i))d−i ad
d−i and

(−1)(d−1)(d−i)(d
i)d−1a
d−i
d−1ad−i appear in the resultant Ri (unless i = 1 in which case the two
monomials are the same and the coeﬃcient is (1 − d)d−1). Moreover, the monomials ad
d−i are
the only pure powers appearing in any of the Ri. We then use these facts to compile a (non-
exhaustive) list of bad primes for each d ∈ N>0, namely all the primes p for which there exists
i ∈ {1, . . . , d − 1} such that p ∣
∣
∣ (d
i) − 1 .

Acknowledgement. The fact that the monomial (1 − (d
i))d−i ad
d−i appears in Ri and is the
only pure power appearing there was ﬁrst proved by Rosa de Frutos’ in her Ph.D. thesis [3],
Proposition 2.2.1, page 17.

2 A list of bad primes

Unless otherwise speciﬁed, from now till the end of this paper we shall regard the Ri as elements
of the polynomial ring Z[a1, . . . , ad−1].

Theorem 6 ([3], Proposition 2.2.1) For each i ∈ {1, . . . , d − 1}, the monomial

(−1)d−i ((d
i) − 1
)d−i ad
d−i appears in the resultant Ri. Moreover, the monomials ad
d−i are the
only pure powers appearing in any of the Ri.

Proof: The polynomial Ri is the resultant of

f = xd + ad−1xd−1 + · · · + ad−1x

and
 Hi(f ) = (d
i
)xd−i + (d − i − 1
i
 )a1xd−i−1 + · · · + (
i + 1
i
 )ad−i−1x + (i
i

)ad−i.

3

Notation. For i, j ∈ {1, . . . , d − 1}, we denote by ̃aij the element (d−j
i )aj.

Note that for all i ∈ {1, . . . , d − 1}, ̃ai,d−i = ad−i.

The resultant Ri equals the determinant D(d, i) of the following matrix M (d, i):




























 d−i
︷ ︸︸ ︷
1 a1 a2 · · · ad−i−1
0 1 a1 · · · ad−i−2
... ...
0 · · · 0 · · · 1
 d
︷ ︸︸ ︷
ad−i · · · ad−1 0 · · · · · · 0
ad−i−1 ad−i · · · ad−1 0 · · · 0
... ...
a1 a2 · · · ad−i · · · ad−1 0
(d
i) ̃ai,1 ̃ai2 · · · ̃ai,d−i−1
0 (d
i) ̃ai,1 · · · ̃ai,d−i−2
... ... ...
... ... ...
... ... ...
... ... ...
0 0 · · · · · · 0
 ad−i · · · 0 0 · · · · · · 0
̃ai,d−i−1 ad−i 0 · · · · · · 0

̃ai,d−i−2 ... ... ...
... ... ...
... ... ...
... ... ...
· · · 0 (d
i) ̃ai,1 ̃ai,2 · · · ad−i
 



























By deﬁnition, the determinant D(d, i) of the (2d − i) × (2d − i) matrix M (d, i) = (mℓj) is

∆ = ∑

σ∈Σ2d−i(−1)
ǫ(σ)mσ(1),1mσ(2),2 · · · mσ(2d−i),2d−i, (3)

where Σ2d−i is the group of permutations of {1, . . . , 2d − i} and

ǫ(σ) = 0 if σ is even

= 1 if σ is odd.

First of all, note that the last column of M (d, i) has only one non-zero entry that equals
ad−i. Hence ad−i | D(d, i) . In particular no pure power of aj can appear in D(d, i) for j ̸= d − i.

Remark 7 The entry ad−i appears only in the last d columns of M (d, i): exactly once in each of
the last i columns and exactly twice in each of the columns numbered d−i+1, d−i+2, . . . , 2d−2i.

By inspection of the matrix M (d, i), we see that
(1) a monomial ω appearing in D(d, i) cannot be divisible by ad+1
d−i
(2) if ad
d−i ̸ | ω, then ω is not a pure power of ad−i
(3) if ad
d−i ∣
∣ ω, then in the notation of formula (3), ω = (−1)ǫ(σ)mσ(1),1 · · · mσ(2d−i),2d−i
with σ(j) = j for j ∈ {2d−2i+1, . . . , 2d−1} and σ(j) ∈ {j, j−d+i} for j ∈ {d−i+1, . . . , 2d−2i}.
The term in (3) corresponding to σ = Id is the product of the elements on the main
diagonal of M (d, i); this product is equal to ad
d−i. There are other choices of σ ∈ Σd for which
the corresponding summand in (3) is of the form cad
d−i, where c ∈ Z. Let us group all of these
terms together and calculate the total coeﬃcient of ad
d−i in (3)
Now, the coeﬃcient of ad
d−i in D(d, i) is given by the coeﬃcient of a
d−i
d−i in the expansion
of the determinant ˜D(d, i) of the (2d − 2i) × (2d − 2i)-matrix ˜M (d, i) obtained by deleting the
last i lines and the last i columns of M (d, i).
 4

The matrix ˜M (d, i) is


















 1 a1 a2 . . . ad−i−1 ad−i . . . ad−1 0
0 1 a1 . . . ad−i−2 ad−i−1 ad−i . . . ad−1
... ... ... ... ...
0 . . . 0 . . . 1 a1 a2 . . . ad−i(d
i) ̃ai,1 ̃ai,2 . . . ̃ai,d−i−1 ad−i 0 . . . 0
0 (d
i) ̃ai,1 . . . ̃ai,d−i−2 ̃ai,d−i−1 ad−i 0 . . .
... ... ... ... ...
0 . . . 0 (d
i) . . . . . . ̃ai,d−i−1 ad−i 0
0 0 . . . . . . (d
i) . . . . . . ̃ai,d−i+1 ad−i
 


















In this determinant, the ﬁrst d − i columns do not contain any ad−i and in the last d − i
columns, each ad−i appears two times, once in the ﬁrst d − i rows, once in the last d − i rows.
In each of the last d−i columns we have to choose one of the two ad−i and delete the rest of
the line and the rest of the column to which it belongs. Fix one such choice. The corresponding
monomial (−1)ǫ(σ)mσ(1),1mσ(2),2 · · · mσ(2d−2i),2d−2i, σ ∈ Σ2d−2i, satisﬁes σ(j) ∈ {j, j − d + i} for
all j ∈ {d − i + 1, . . . , 2d − 2i}.
Let J = { σ(j) | j ∈ {d − i + 1, . . . , 2d − 2i}} (4)

and J c = {1, . . . , 2d − 2i} \ J. Write J = {j1, . . . , jd−i} ⊂ {1, . . . , 2(d − i)}.

For all q, ℓ ∈ {1, . . . d − i} we have jq − jℓ ̸= d − i. (5)

The set J c has the same property. Note that, conversely, every set

J = {j1, . . . , jd−i} ⊂ {1, . . . , 2(d − i)}

satisfying (5) has the form (4) for a suitable σ ∈ Σ2d−2i.
The coeﬃcient of the term ad−i
d−i in the expansion of ˜D(d, i) corresponding to a given choice
of J is the determinant of the matrix N (d, i, J) obtained from the ﬁrst (d − i) columns of ˜M (d, i)
by deleting the rows numbered j1, . . . jd−i−1, jd−i.
Let k = # (J c ∩ {d − i + 1, d − i + 2, . . . 2(d − i)}) . (6)

There exists a permutation of the rows of N (d, i, J) such that the resulting matrix is an upper
triangular matrix with only 1 and (d
i) on the main diagonal, where 1 appears (d − i − k)
times and (d
i) appears k times. Thus the permutation σ ∈ Σ2d−2i is uniquely determined by
J ∩ {d − i + 1, . . . , 2d − 2i}.
We have
 det N (d, i, J) = ±(
d
i
)k. (7)

Now, σ is the composition of k transpositions (j, j − d + i) for j ∈ J c ∩ {d − i + 1, . . . , 2d − 2i}.
Thus ǫ(σ) ≡ k mod 2. (8)

Example To illustrate the process, let us take

J = {d − i + 1, d − i + 2, . . . , 2(d − i) − 3, d − i − 2, 2(d − i) − 1, 2(d − i)},

5

which means that we chose all the occurrences of ad−i lying on the main diagonal in the last
(d − i) rows of ˜M (d, i) except in the column number 2(d − i) − 2 in which case we chose the
occurrence of ad−i at the place (d − i − 2, 2d − 2i − 2). We have k = 1.
The resulting matrix N (d, i, J) looks like












 1 a1 a2 . . . . . . . . . ad−i−1
0 1 a1 . . . . . . . . . ad−i−2
... ... ... ...
0 . . . 0 1 a1 a2 a3
0 . . . . . . 0 0 1 a1
0 . . . . . . . . . 0 0 1
0 . . . . . . 0 (
d
i) ̃ai,1 ̃ai,2
 












To obtain an upper triangular matrix, we have to apply a cyclic permutation to the rows d − i,
d − i − 1 and d − i − 2 and we obtain that the desired determinant is ±(d
i).

Coming back to the proof of the Theorem, for each k ∈ {0, . . . , d−i}, there are (d−i
k ) choices
of J satisfying (6). Combining this with (7) and (8) and summing over all k ∈ {0, . . . , d − i}, we
get that the coeﬃcient of ad
d−i in Ri is

d−i∑

k=0(−1)
k(d − i
k
 )(d
i
)k = (−1)
d−i ((d
i
) − 1
)d−i (9)

□

Corollary 8 Take a prime number p such that there exists i ∈ {1, . . . , d−1} for which p ∣
∣
∣ (d
i) − 1 .
Then CAd,p is false.

Proof. Assume that char(K) = p. By Theorem 6, no pure power of any of the ai appears in any
of the Rj mod p. Hence the point of K d−1 whose i-th coordinate is 1 and all of whose other
coordinates are zero belongs to V (R1, . . . , Rd−1). □

Using similar arguments, we obtain the following Theorem.

Theorem 9 For i ∈ {2, . . . , d − 1}, the monomial (−1)(d−1)(d−i)(d
i)d−1ad−i
d−1ad−i appears in the

resultant Ri. The term (−1)(d−1)(d−i)(d
i)d−1ad−i
d−1ad−i is the unique monomial in (3) of degree
d − i + 1; all the other monomials appearing in (3) have degree strictly greater than d − i + 1.

Proof. By inspection of the matrix M (d, i), we see that the monomial (−1)(d−1)(d−i)(
d
i)d−1a
d−i
d−1ad−i
appears in the resultant Ri: it is the monomial with

σ(j) = d − i + j for {1, . . . , d − i}

= j − (d − i) for j ∈ {d − i + 1, . . . , 2d − i − 1}

= 2d − i for j = 2d − i.

Moreover, it is the unique monomial ω of Ri such that ad−i
d−1 ∣
∣
∣ ω.
Let us prove the second statement of the Theorem. Let M •(d, i) be the matrix obtained
by deleting the last row and the last column of M (d, i). Let D•(d, i) = det M •(d, i). We need
to show that all the monomials appearing in D•(d, i) have order at least d − i and a
d−i
d−1 is the
only one of order exactly d − i.
 6

Remark 10 For ℓ, j ∈ {1, . . . , 2d − i − 1}, we have mℓj ∈ N \ {0} if and only if one of the
following conditions holds:
(1) j ∈ {d − i + 1, . . . , d − 1} and ℓ = j + d − i
(2) j ∈ {1, . . . , d − i} and ℓ ∈ {j, j + d − i}.

By Remark 10, the last d − i columns of M •(d, i) do not involve any non-zero constant entries.
Hence every monomial ω = (−1)ǫ(σ)mσ(1),1 · · · mσ(2d−i−1),2d−i−1 appearing in D•(d, i) has degree
at least d − i. Moreover, assume that deg ω = d − i. Moreover, for j ∈ {1, . . . , d − 1} one of the
conditions (1) or (2) of Remark 10 holds with ℓ = σ(j). Let

j(ω) = min{j ∈ {1, . . . , d − 1} | σ(j) = j + d − i}.

Lemma 11 We have j(ω) = 1.

Proof of Lemma. Assume that j(ω) > 1, aiming for contradiction. By Remark 10,

if j ∈ {d − i + 1, . . . , d − 1}, then σ(j) = j + d − i. (10)

Hence j(ω) ≤ d − i + 1.
Take a j ∈ {j(ω) + d − 2, . . . , 2d − i − 1}. Then j > d − 1. From (10) we obtain
σ(j)∈/{2d − i − 1, . . . , 2d − i − 1}. By inspection of the matrix M •(d, i), it follows that

σ(j) ∈ {j(ω) − 1, . . . , d − i}.

By descending induction on j, we obtain

σ(j) = j − d + 1 whenever j ∈ {j(ω) + d − 2, . . . , 2d − i − 1}. (11)

By equation (11), we have σ(j(ω) + d − 2) = j(ω) − 1, so σ(j(ω) − 1) ̸= j(ω) − 1. By
Remark 10, σ(j(ω) − 1) = j(ω) − 1 + d − i. contradicting the deﬁnition of j(ω). The Lemma is
proved. □

The Theorem follows from the Lemma by inspection of the matrix M •(d, i). □

References

[1] Eduardo Casas–Alvero, Higher Order Polar Germs, Journal of Algebra, Volume 240, Issue
1, 1 June 2001, pages 326–337

[2] W. Castryck, R. Laterveer, M. Ouna¨ıes, Constraints on counterexamples to the Casa-Alvero
conjecture and a veriﬁcation in degree 12, arXiv:1208.5404v1, 27/08/2018.

[3] R.M. de Frutos Mar´ın, Perspectivas Aritm´eticas para la Conjectura de Casas–Alvero, PhD
thesis, Universidad de Valladolid, 2012.

[4] A. Salinier, M. Chellali, La conjecture de Casas-Alvero pour les degr´es 5pe, hal-00748843,
2012.

[5] J. Draisma and J.P. de Jong, On the Casas-Alvero conjecture, Newsletter of the EMS 80
(June 2011) 29–33

[6] H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. Van de Woestline, The Casas-Alvero
conjecture for inﬁnitely many degrees Journal of Algebra, Vol. 316(1),224-230, 2007.

7
