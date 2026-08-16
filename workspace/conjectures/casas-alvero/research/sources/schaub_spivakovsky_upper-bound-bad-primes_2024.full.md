<!-- source: https://arxiv.org/pdf/2411.13967 | converted from PDF -->

arXiv:2411.13967v1  [math.AC]  21 Nov 2024
A description of and an upper bound on the set of bad primes in
the study of the Casas-Alvero Conjecture

Daniel Schaub, Univ Angers, CNRS, LAREMA, SFR MATHSTIC
F-49000 Angers, France
email: daniel.schaub@univ-angers.fr

Mark Spivakovsky, Univ Paul Sabatier, CNRS, IMT UMR 5219
F-31062 Toulouse, France and
CNRS, LaSol UMI 2001, UNAM.

November 22, 2024

Abstract

The Casas–Alvero conjecture predicts that every univariate polynomial over a ﬁeld of
characteristic zero having a common factor with each of its derivatives Hi(f ) is a power of a
linear polynomial. One approach to proving the conjecture is to ﬁrst prove it for polynomials
of some small degree n, compile a list of bad primes for that degree (namely, those primes p
for which the conjecture fails in degree n and characteristic p) and then deduce the conjecture
for all degrees of the form npℓ, ℓ ∈ N, where p is a good prime for n. In this paper we give
an explicit description of the set of bad primes in any given degree n. In particular, we show
that if the conjecture holds in degree n then the bad primes for n are bounded above by
( n2−n
2
n−2 )
! n−1∏

i=1
 (
i+n−2
n−2 )(
d−i+n−2
n−2 ).

1 Introduction

In the year 2001 Eduardo Casas–Alvero published a paper on higher order polar germs of plane
curve singularities [1]. His work on polar germs inspired him to make the following conjecture.
Let K be a ﬁeld, f ∈ K[x] a non-constant monic univariate polynomial, n := deg(f ):

f = xn + a1xn−1 + · · · + an.

Let
 Hi(f ) = (
n
i
 )xn−i + (n − 1
i
 )a1xn−i−1 + · · · + (i
i

)an−i

be the i-th Hasse derivative of f .

Deﬁnition 1.1 The polynomial f is said to be a Casas–Alvero polynomial if for each i ∈
{1, . . . , n − 1} it has a non-constant common factor with its i-th Hasse derivative Hi(f ).

Conjecture 1.2 (Casas–Alvero) Assume that char K = 0. If f ∈ K[x] is a Casas-Alvero
polynomial of degree n, then there exists b ∈ K such that f (x) = (x − b)n.

If char K = p > 0, the conjecture is false in general. The simplest counterexample is the
polynomial f (x) = xp+1 − xp.
 1

Remark 1.3 The following fact is known and easy to prove. If the Casas–Alvero conjecture
holds for the algebraic closure ¯K of K then it also holds for K (the converse is not established,
to our knowledge). Therefore, from now on we will assume that K is algebraically closed.

We will write CAn,p for the statement “The Casas–Alvero conjecture holds for polynomials
of degree n over algebraically closed ﬁelds of characteristic p”.
The following equivalences are known for each n ([4], [7]):
CAn,0 holds ⇐⇒ CAn,p holds for some prime n

Deﬁnition 1.4 A prime number p is said to be a bad prime for n if CAn,p is false. If p is
not a bad prime for n, we will say that p is a good prime for n.

Proposition 1.5 ([7], Propositions 2.2 and 2.6) Take a strictly positive integer n, a prime
number p and a non-negative integer ℓ. Assume that CAn,p holds. Then so do CAnpℓ,p and
CAnpℓ,0.

This result suggests the following general approach to the problem:
(1) prove the conjecture for a small number n;
(2) compile lists of good and bad primes for n;
(3) conclude that CAnpℓ,0 holds for all the primes p that are known to be good for n.

In particular, this shows the importance of knowing which primes are good or bad for a
given degree n.
The above approach has been carried out up to n ≤ 7 ([2], [3], [4], [5], [7]). Some integers
cannot be written in the form npℓ where p is a good prime for n, for example,

12 = 2
2 · 3, 20 = 2
2 · 5, 24 = 2
3 · 3, 28 = 2
2 · 7, 30 = 2 · 3 · 5, 36 = 2
2 · 3
2, 40 = 2
3 · 5, . . .

CA12,0 has been proved in [2] with the aid of a computer, by using a very clever strategy to cut
down the computation of resultants and Gr¨obner bases. Thus the smallest degree n for which
CAn,0 is not known is n = 20.

The purpose of this paper is to give an explicit description of the set of bad primes in any
given degree n. In particular, we obtain an explicit upper bound on bad primes for n, assuming
that Cn,0 holds. These results are based on recent work of Soham Ghosh [6].

Notation: For j ∈ {1, . . . , n − 1}, let the involution

Φj : K[x1, . . . , xn−1] → K[x1, . . . , xn−1], (1)

be deﬁned by Φj(xi) = xi − xj for i ̸= j and Φj(xj) = −xj. (2)

Let Φn : K[x1, . . . , xn−1] → K[x1, . . . , xn−1], (3)

denote the identity map.
Let σi(x1, . . . , xn−1) denote the i-th elementary symmetric function of x1, . . . , xn−1.
Let T = {1, . . . , n}n−1; the set T is the collection of all the (n − 1)-tuples of the form
(j1, . . . , jn−1), where j1, . . . , jn−1 ∈ {1, . . . , n}.

Notation. Given a ﬁxed choice of T = (j1, . . . jn−1), for i ∈ {1, . . . , n − 1} we will denote by
GT,i the homogeneous polynomial Φji(σi(x1, . . . , xn−1)).

In his fundamental preprint [6], Soham Ghosh showed that the Casas–Alvero conjecture
in degree n (over any ﬁeld, regardless of characteristic) is equivalent to the following statement.

2

Conjecture 1.6 ([6], Proposition 5.2) For every choice of T = (j1, . . . , jn−1) ∈ T , the sequence
of homogeneous polynomials (GT,1, . . . , GT,n−1) (4)

forms a regular sequence in K[x1, . . . , xn−1].

Since the polynomial ring K[x1, . . . , xn−1] is Cohen–Macaulay, Conjecture 1.6 is equivalent
to saying that ht(GT,1, . . . , GT,n−1) = n − 1 and thus also to

Conjecture 1.7 We have √GT,1, . . . , GT,n−1 = (x1, . . . xn−1). (5)

2 Macaulay’s Theorem

We recall (a part of) Macaulay’s celebrated theorem from 1916.
Let x1, . . . , xn be independent variables, f1, . . . , fn ∈ K[x1, . . . , xn] homogeneous polyno-
mials and let di = deg fi denote the total degree of fi. Let m := (x1, . . . , xn). Finally, put

d = n∑

k=1 dk − n + 1.

Theorem 2.1 [8] The following statements are equivalent:

(1) √(f1, . . . , fn) = m

(2) md ⊂ (f1, . . . , fn).

3 A description of and an upper bound on the set of bad primes

In this section we state and prove our main results.

Let x = (x1, . . . , xn−1). We will use multi-index notation: xα will stand for n−1∏

k=1 xαk
k and

|α| for n−1∑

k=1 αk.

We apply Macaulay’s Theorem to the polynomials GT,, . . . , GT,n−1 ∈ K[x].
We have deg GT,i = i for i ∈ {1, . . . , n − 1}.

Let d = n−1∑

i=1 deg GT,i − (n − 2) = 1 + 2 + · · · + (n − 1) − (n − 2) = n2−3n+4
2 .

Let C denote the binomial coeﬃcient ( n2−n
2
n−2 )
; it is the number of monomials of degree

d = n2−3n+4
2 in n − 1 variables.
Let ST,i = { GT,ixα | |α| = d − i}, i ∈ {1, . . . , n − 1} and

ST :=
 n−1⋃

i=1 ST,i.

We have |ST,i| = (
d−i+n−2
n−2 )
.

Let D := |ST | = n−1∑

i=1 |ST,i| = n−1∑

i=1
 (d−i+n−2
n−2 ); we have D ≥ C (in fact, this inequality is

strict whenever n > 2).
 3

Consider the C-dimensional K-vector space V , generated by all the monomials in x of
degree d; we have ST ⊂ V .
Let MT denote the D × C matrix formed by the row vectors (v)v∈ST . Let JT be the
greatest common divisor of all the C × C minors of MT .

Theorem 3.1 A prime number p is a bad prime for n if and only if p | JT for some T ∈ T
(equivalently, if and only if p | lcm(JT )T ∈T ).

Proof. Fix a T ∈ T . By Theorem 2.1, (5) is equivalent to (x)d ⊂ (GT 1, . . . , GT,n−1). And this
is true if and only if V ⊂ (GT 1, . . . , GT,n−1). This inclusion is true if and only if the rank of the
matrix MT is maximal, ie. rk MT = C. or in other words, if and only MT has a non-degenerate
C × C minor.
Therefore Conjecture 1.6 fails in degree n and characteristic p if and only if p | JT for
some T ∈ T . By [6], Proposition 5.2, the failure of Conjecture 1.6 in degree n and characteristic
p is equivalent to p being a bad prime for n. □

Corollary 3.2 If Cn,0 holds but p is a bad prime for n then

p < C!
 n−1∏

i=1
 (i + n − 2
n − 2
 )(
d−i+n−2
n−2 ). (6)

Proof. The corollary follows from Theorem 3.1 and the following lemma.

Lemma 3.3 Fix a T ∈ T and let A be a C × C minor of MT . Then

|A| ≤ C!
 n−1∏

i=1
 (i + n − 2
n − 2
 )(
d−i+n−2
n−2 ).

Proof of the lemma. Write GT,i as a sum of (possibly repeated) monomials, each with coeﬃcient
1. The monomial xi
ji is repeated (i+n−2
n−2 ) times, more than any other monomial. Therefore, once
we group the like terms together, the greatest absolute value of a coeﬃcient of a monomial in
GT i is (
i+n−2
n−2 ).
When we write the minor A as a sum of C! terms, each term divides an integer of the

form n−1∏

i=1
 (
i+n−2
n−2 )∏

j=1 aij, where for all the pairs (i, j) we have |aij| ≤ (i+n−2
n−2 )
. This proves the lemma

and, with it, the corollary. □

Remark 3.4 The upper bound (6) can be vastly improved as follows. Let the notation be as

above. The product n−1∏

i=1
 (i+n−2
n−2 )(
d−i+n−2
n−2 ) has a total of D (not necessarily distinct) terms of the

form (i+n−2
n−2 ). We have (i+n−2
n−2 ) < (i′+n−2
n−2 ) whenever i < i′. Write n−1∏

i=1
 (i+n−2
n−2 )(
d−i+n−2
n−2 ) = D∏

k=1 bk

with the sequence bk non-strictly increasing. Then

p < C!
 D∏

D−C+1 bk (7)

The proof is the same as in the corollary. The reason we did not state the corollary in this form
in the ﬁrst place is that we could not ﬁnd an explicit, closed form for the integers bk appearing
in (7). For example, what is the value of i such that bD−C+1 = (i+n−2
n−2 ) ?

4

References

[1] Eduardo Casas–Alvero, Higher Order Polar Germs, Journal of Algebra, Volume 240, Issue
1, 1 June 2001, pages 326–337

[2] W. Castryck, R. Laterveer, M. Ouna¨ıes, Constraints on counterexamples to the Casas-
Alvero conjecture and a veriﬁcation in degree 12, arXiv:1208.5404v1, 27/08/2018.

[3] M. Chellali, A. Salinier, La conjecture de Casas-Alvero pour les degr´es 5pe, hal-00748843,
2012.

[4] J. Draisma and J. P. de Jong, On the Casas-Alvero conjecture, Newsletter of the EMS 80
(June 2011) 29–33

[5] R. M. de Frutos Mar´ın, Perspectivas Aritm´eticas para la Conjectura de Casas–Alvero, PhD
thesis, Universidad de Valladolid, 2012.

[6] S. Ghosh, A ﬁniteness result towards the Casas-Alvero Conjecture, arXiv:2402.18717
[math.AG].

[7] H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. Van de Woestline, The Casas-Alvero
conjecture for inﬁnitely many degrees Journal of Algebra, Vol. 316(1),224-230, 2007.

[8] F. S. Macaulay, The algebraic theory of modular systems, Cambridge University Press, 2016.

5
