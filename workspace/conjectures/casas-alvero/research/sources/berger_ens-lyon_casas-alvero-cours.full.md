<!-- source: https://perso.ens-lyon.fr/laurent.berger/autrestextes/CApromys.pdf | converted from PDF -->

THE CASAS-ALVERO CONJECTURE

LAURENT BERGER

The goal of this project is to work on the following conjecture, which looks so simple that
you may be suprised to learn that it has not been proved yet! If P is a polynomial, let P (i)

denote its i-th derivative.

Conjecture 1. Let P (X) = X d + ad−1X d−1 + · · · + a0 be a monic polynomial of degree
d ≥ 1, with complex coeﬃcients. If for all 1 ≤ i ≤ d − 1, there exists xi ∈ C such that
P (xi) = P (i)(xi) = 0, then P (X) is of the form (X − λ)d for some λ ∈ C.

This conjecture has been proposed by Eduardo Casas-Alvero around 2000, following his
work [CA01] on plane curves. It is known for d ≤ 19 as well as for any d which is a prime
power or twice a prime power.
If P (X) ∈ C[X], we say that P is a CA polynomial if P and P (i) have a common root for
all 1 ≤ i ≤ deg(P ) − 1, so that the conjecture above says that CA polynomials have a very
special shape.

Exercise 1. Prove conjecture 1 for d = 2, 3, 4. If d ≥ 3, you can assume that P is of the
form P (X) = X 2 · (X − 1) · Q(X) where deg Q = d − 3: why? Can you do d = 5 as well?

1. Roots of polynomials

Before we go on, let us explore some properties of the roots of polynomials, using a bit of
real and complex analysis. The ﬁrst exercise is Rolle’s theorem for polynomials.

Exercise 2. If P (X) ∈ R[X], and if a < b are two real roots of P (X), then P ′(X) has a
root in the open interval ]a, b[.

The following asks you to prove the Gauss-Lucas theorem.

Exercise 3. If P (X) ∈ C[X], then the roots of P ′ are in the convex hull of the roots of P .

Can you use the Gauss-Lucas theorem to study the cases d = 3, 4? Can you say something
about the minimal number of distinct roots of a CA polynomial? Unfortunately, it does not
seem possible to prove conjecture 1 using these ideas if d ≥ 5. We ﬁnish this section with a
much harder exercise.

Exercise 4. If d ≥ 2 and 1 ≤ n ≤ d − 1, then there exists a monic polynomial P (X) ∈ C[X]
of degree d, such that P and P (i) have a common root for all 1 ≤ i ≤ d − 1 with i ̸= n.
1

2 LAURENT BERGER

2. Resultants

Since analysis does not seem to be of much help, we turn to algebra. There is a nice
algebraic way of ﬁguring out if two polynomials have a common root. Let K be a ﬁeld
and let P (X) = adX d + · · · + a0 and Q(X) = beX e + · · · + b0 be two polynomials with
coeﬃcients in K. Let K[X]n denote the space of polynomials of degree ≤ n − 1. Let M be
the matrix of the map K[X]e × K[X]d → K[X]d+e given by (A, B) ↦→ AP + QB, in the basis
{X e−1, . . . , X, 1} of K[X]e, {X d−1, . . . , X, 1} of K[X]d and {X d+e−1, . . . , X, 1} of K[X]d+e.
We then have
 M =
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

 ad 0 · · · 0 be 0 · · · 0

ad−1 ad . . . ... ... be . . . ...
... ad−1 . . . 0 ... . . . 0
... ... . . . ad b1 be
a0 ad−1 b0 . . . ... ...

0 . . . ... 0 . . . b1 ...
... . . . a0 ... ... . . . b0 b1
0 . . . 0 a0 0 . . . 0 b0
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

 .

The resultant res(P, Q) of P and Q is res(P, Q) = det(M ).

Exercise 5. Compute res(P, P ′) when P (X) = X 2 + aX + b and when P (X) = X 3 + pX + q.
Do you recognize the results?

Exercise 6. Show that if ad ̸= 0 and be ̸= 0, then res(P, Q) = 0 if and only if P and Q have
a common root. Show that res(P, Q) = ae
d · ∏
P (x)=0 Q(x) = (−1)
de · bd
e · ∏
Q(x)=0 P (x).

If K = C, a polynomial P of degree d is therefore a CA polynomial if and only if

res(P, P ′) = res(P, P ′′) = · · · = res(P, P (d−1)) = 0.

This way, we have reduced the CA conjecture to showing that certain sets of equations have
no solution. We’ll see how to prove this in the next section.

3. The Nullstellensatz

Let A = C[X1, . . . , Xn] be the set of polynomials in n variables, with coeﬃcients in C.
Let I be an ideal of A, that is a subset of A such that i + j ∈ I if i, j ∈ I and a · i ∈ I if
a ∈ A and i ∈ I. The Nullstellensatz (the “zero locus theorem”) is the following theorem.

Theorem 1. If I is an ideal of A and I ̸= A, then there exists x = (x1, . . . , xn) ∈ C
n such
that f (x) = 0 for all f ∈ I.

Exercise 7. What does theorem 1 say when n = 1?

THE CASAS-ALVERO CONJECTURE 3

Exercise 8. Show that theorem 1 implies the following: if f1, . . . , fm ∈ A, then either some
A-linear combination of the fi’s is equal to 1, or there exists x ∈ Cn such that fi(x) = 0 for
all i.

You should look up the Nullstellensatz; there are several diﬀerent proofs, see for example
§1 of Chapter IX of [Lan02], or the proof that is explained in [May03].

Exercise 9. Show that the Casas-Alvero conjecture is equivalent to the following statement:
if P (X) = X(X − 1)(X d−2 + ad−3X d−3 + · · · + a0), and A = C[a0, . . . , ad−3], then some
A-linear combination of the {res(P, P (i))}1≤i≤d−1 is equal to 1.
Use a computer algebra system to verify the conjecture for small values of d.

This is how conjecture 1 has been proved for some values of d up to d = 12 (see for instance
[DG06] and [CLO14]). For larger values of d, some additional theoretical input is needed as
the computations become too diﬃcult, even for a computer.

4. Polynomials in characteristic p

In this section, we consider polynomials with coeﬃcients in a ﬁeld K of characteristic p,
for example K = Fp. In this case, we can have P ′(X) = 0 for some non constant P , for
example if P (X) = X p. In addition P (k)(X) = 0 for all P as soon as k ≥ p (why?). Instead
of working with derivatives, we work with the Hasse derivative. The k-th Hasse derivative
of P (X) = adX d + · · · + a0 is

H kP (X) = (d
k
)
adX d−k + (
d − 1
k
 )
ad−1X d−1−k + · · · + (k
k
)ak.

Note that P (k)(X) = k! · H kP (X). If P (X) ∈ K[X], we say that P is a CA polynomial if
P and H iP have a common root for all 1 ≤ i ≤ deg(P ) − 1. The characteristic p version of
the Casas-Alvero conjecture for polynomials of degree d is then the following.

Question 1. If P is a monic CA polynomial, then do we necessarily have P (X) = (X − λ)d

for some λ ∈ K alg?

Exercise 10. Show that if (X − λ)d ∈ Fp[X], then λ ∈ Fp. For what ﬁelds other than Fp
does an analogous statement hold?

Exercise 11. Show that the answer to question 1 is yes for d = 1, 2, for d = 3 if p ̸= 2, and
no if d = p + 1.

Exercise 12. What about P (X) = X(X − 1)
4(X − 8)(X − 18) in F23[X]?

The following is the main theorem of [BLSW].

4 LAURENT BERGER

Theorem 2. Let K be algebraically closed. If p ∤ n and question 1 has a positive answer in
degree n, then it also has a positive answer in degree d = npe for all e ≥ 1.

In the rest of this section, we (meaning: you) prove theorem 2. If n ≥ 0, write n in base
p as = nkpk + nk−1pk−1 + · · · + n0.

Exercise 13. If m, n ≥ 1, then
( n
m

) ≡ ( nk
mk
) · · · ( n1
m1
) · ( n0
m0
) mod p

Exercise 14. Let the notation be as in theorem 2. Prove that if P is a CA polynomial of
degree d, then there is a CA polynomial Q of degree n such that P = Q
pe. Prove theorem 2.

5. Reduction modulo p

It is possible to use the results of the previous section to prove conjecture 1 when the
degree of P is a power of a prime number or twice a power of a prime number. In order
to do this, you need to know a little bit of valuation theory, see for instance §4 of Chapter
XII of [Lan02] (but beware that what Lang calls a valuation is what we’d call an absolute
value; how do you relate the two deﬁnitions?). For us, a valuation on a ﬁeld K is a function
v : K × → R such that v(xy) = v(x) + v(y) and v(x + y) ≥ min(v(x), v(y)). It is customary
to extend v to K by setting v(0) = +∞. The trivial valuation is given by v(x) = 0 for all
x ∈ K ×. Let p be a prime number. The p-adic valuation on Q is the function valp : Q× → Z
deﬁned as follows. If x ∈ Q×, we can write it as x = pn · a/b where p divides neither a nor b
and then we let valp(x) = n.

Exercise 15. Check that valp is a valuation on Q. Conversely, show that if v is a non-trivial
valuation on Q, then there exists a prime number p such that v is a multiple of valp.

We use the following fact (see §4 of Chapter XII of [Lan02]).

Theorem 3. If v is a valuation on K, and L/K is a ﬁeld extension, then v extends to L.

Exercise 16. By (possibly inﬁnite) induction, it is enough to prove theorem 3 for extensions
of the form L = K(x). How do you extend a valuation v on K to K(x)? Treat separately
the cases where x is algebraic over K and where x is transcendental over K.

The p-adic valuation valp can therefore be extended (in many diﬀerent ways) from Q to
C. We choose one such extension. Let R denote the set of elements of C of valuation ≥ 0
and let mR denote the set of elements of C of valuation > 0.

Exercise 17. Show that R is a ring, that mR is a maximal ideal of R, and that the quotient
ﬁeld R/mR is a ﬁeld of characteristic p.

THE CASAS-ALVERO CONJECTURE 5

Exercise 18. Prove the Casas-Alvero conjecture for polynomials P (X) ∈ C[X] whose degree
is a power of a prime or twice a power of a prime.

The same idea can be used to prove the conjecture for polynomials of degree 3pe, 4pe or
5pe for primes p, but you have to start excluding some primes (see [DdJ11] and [CS12]).

6. Going further

Now your work really begins. Look up the literature on the subject, for example the
references below. There are also various papers on the arxiv that claim to give a complete
proof: can you make sense of them? What is the smallest degree d for which the conjecture
is currently open? Can you prove the conjecture using some totally diﬀerent ideas?

References

[CA01] E. Casas-Alvero – “Higher order polar germs”, J. Algebra 240 (2001), no. 1, p. 326–337.
[Cas13] W. Castryck – “La conjecture de Casas-Alvero”, 2013, http://images.math.cnrs.fr/
La-conjecture-de-Casas-Alvero.html.
[CLO14] W. Castryck, R. Laterveer & M. Ouna¨ıes – “Constraints on counterexamples to the Casas-
Alvero conjecture, and a veriﬁcation in degree 12”, Math. Comp., to appear, 2014.
[CS12] M. Chellali & A. Salinier – “La conjecture de Casas Alvero pour les degr´es 5pe”, An. Univ.
Dun˘area de Jos Galat¸i Fasc. II Mat. Fiz. Mec. Teor. 4(35) (2012), no. 1-2, p. 54–62.
[DdJ11] J. Draisma & J. P. de Jong – “On the Casas-Alvero conjecture”, Eur. Math. Soc.
Newsl. (2011), no. 80, p. 29–33. Erratum: http://www.win.tue.nl/~jdraisma/publications/
erratumcasasalvero.pdf.
[DG06] G. M. Diaz-Toca & L. Gonzalez-Vega – “On analyzing a conjecture about univariate poly-
nomials and their roots by using Maple.”, in Maple conference 2006. Proceedings of the conference,
Waterloo, Ontario, Canada, July 23–26, 2006., Waterloo: Maplesoft, 2006, p. 81–98.
[BLSW] H.-C. Graf von Bothmer, O. Labs, J. Schicho & C. van de Woestijne – “The Casas-
Alvero conjecture for inﬁnitely many degrees”, J. Algebra 316 (2007), no. 1, p. 224–230.
[Lan02] S. Lang – Algebra, third ed., Graduate Texts in Mathematics, vol. 211, Springer-Verlag, New
York, 2002.
[May03] J. P. May – “Munshi’s proof of the Nullstellensatz”, Amer. Math. Monthly 110 (2003), no. 2,
p. 133–140.

UMPA de l’ENS de Lyon, UMR 5669 du CNRS, IUF
E-mail address: laurent.berger@ens-lyon.fr
URL: perso.ens-lyon.fr/laurent.berger/
