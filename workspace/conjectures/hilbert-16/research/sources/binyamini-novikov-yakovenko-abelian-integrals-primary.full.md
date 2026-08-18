<!-- source: https://arxiv.org/pdf/0903.5056 | converted from PDF -->

arXiv:0903.5056v1  [math.DG]  29 Mar 2009
LINEAR ESTIMATE FOR THE NUMBER OF ZEROS OF
ABELIAN INTEGRALS

SERGEY MALEV AND DMITRY NOVIKOV

Abstract. We prove a linear in deg ω upper bound on the number of real
zeros of the Abelian integral I(t) = R

δ(t) ω, where δ(t) ⊂ R2 is the real oval

x2y(1 − x − y) = t and ω is a one-form with polynomial coeﬃcients.

1. Introduction

For the polynomial H(x, y) = x
2y(1 − x − y) consider the continuous family
{δ(t), t ∈ (
0, 1
64 )
} of compact connected components of the level curves {H =
t} ⊂ R2. Let ω = p(x, y)dx + q(x, y)dy ∈ Λ1(R2) be a diﬀerential one-form with
polynomial coeﬃcients of degree n. Deﬁne the complete Abelian integral:

(1) I(t) = ∮

δ(t) ω, t ∈ (
0, 1
64
 ) .

We provide an explicit answer to the Inﬁnitesimal Hilbert 16th problem for this
particular Abelian integral.

Theorem 1.1. The number of isolated zeros of I(t) on (0, 1
64 ) does not exceed
7
4 n + 9, where n = deg ω.

It is well known that zeros of Abelian integrals correspond to limit cycles appear-
ing in non-conservative perturbations of Hamiltonian, or, more general, integrable
systems. Abelian integral (1) is related to perturbations of the integrable quadratic
vector ﬁeld which can be written in the Pfaﬃan form as follows:

(2) 1
x dH − εω = 0, H(x, y) = x
2y(1 − x − y).

Therefore Theorem 1.1 implies in a standard way the following claim:

Theorem 1.2. The number of limit cycles appearing in non-conservative perturba-
tion (2) and converging, as ǫ → 0, to a smooth cycle δ(t), does not exceed 1
4 (7n+43).

Indeed, these limit cycles correspond to the isolated zeros of ∫

δ(t) xω, so this
upper bound follows from Theorem 1.1 by replacing n by n + 1.
Our result should be considered in the general context of the Inﬁnitesimal Hilbert
16th problem. So far, the only known general explicit result about the number of
zeros of Abelian integrals is the recent result [1] providing double-exponential in
max(deg H, deg ω) upper bound for the number of zeros of Abelian integral. The
result of Petrov-Khovanskii, see [10] for an exposition of the result, provides an
upper bound which is a linear function of n = deg ω, but provides no information
about the coeﬃcients of this function. It seems reasonable to expect that these two
results can be combined together to provide an upper bound which would be linear

1

2 SERGEY MALEV AND DMITRY NOVIKOV

in n and double-exponential in deg H. However, even this upper bound will by far
exceed any known examples.
From the other side, for the cases of polynomials H of low degree the situation
seems to be better understood. More exact, for a generic polynomial H of third
degree Horozov and Iliev [6] were able to provide an explicit upper bound linear
in n which seems to be close to the best possible one. The key point was the
ellipticity of the level curves of H. This fact allowed to reduce the initial question
to the question about number of zeros of polynomial combinations of solutions of
some Riccati equation. This last question can be easily dealt with by essentially
fewnomials technique (i.e. Rolle lemma). Later, the same approach was applied to
the case of elliptic polynomial of fourth degree, see [5].
This result motivated consideration of integrable quadratic vector ﬁelds with
center whose trajectories are elliptic curves. Gautier in [2] lists all these ﬁelds.
Based on this list and results of [7], Gautier, Gavrilov and Iliev in [3] proposed
a program of studying cyclicity of open nests of cycles deﬁned by such foliations,
and, in particular, conjectured that one can provide an eﬀective upper bound for
the number of zeros of corresponding Abelian integrals, similar to [6]. Our case is
the case (rlv3) in notations of [3].

2. Decomposition in Petrov modules

Deﬁne the basic Abelian integrals as

(3) Ii,j (t) = 1
i + 1
 ∫
δ(t) x
i+1yjdy = ∫ ∫

∆(t) x
iyjdx ∧ dy,

where ∆(t) is the area bounded by the cycle δ(t). The integrals are well-deﬁned for
all (i.e. not only positive) i, j ∈ Z due to the following fact:

Remark 2.1. The curve δ(t) lies in {x, y > 0}.

Our immediate goal is to construct explicit representation of the Abelian inte-
grals deﬁned in (1) as combinations with polynomial in t coeﬃcients of just three
Abelain integrals J1(t) = I0,0(t), J2(t) = I2,0(t) and J3(t) = I3,0(t). In other
words, we want to prove that Abelian integrals can be generated, as a C[t]-module,
by these 3 basic Abelian integrals.
Let H(x, y) = ∑
i,j∈Z2 hij x
iyj ∈ R[x, y] be a general Laurent polynomial in two
variables and assume that the family δ(t) ⊂ {H = t} of cycles lies in {x, y > 0}.

Lemma 2.2. Abelian integrals Ik,l(t) deﬁned by (3) satisfy the following relations:

t(k + 1) · Ik,l(t) = ∑

i,j hi,j(k + i + 1) · Ik+i,l+j (t),

t(l + 1) · Ik,l(t) = ∑

i,j hi,j(l + j + 1) · Ik+i,l+j (t),(4)
 (k + 1) · Ik,l(t) = ∑

i,j ihi,j · d
dt Ik+i,l+j (t),

(l + 1) · Ik,l(t) = ∑

i,j jhi,j · d
dt Ik+i,l+j (t),

where i, j ∈ Z.

LINEAR ESTIMATE FOR THE NUMBER OF ZEROS OF ABELIAN INTEGRALS 3

Proof. Since H(x, y) = t on the cycle δ(t) ⊂ R2 we have

t(k + 1) · Ik,l(t) = ∫

δ(t)
 H(x, y)x
k+1yldy = ∑

i,j hi,j(k + i + 1)Ik+i,l+j (t),

which is the ﬁrst equality of (4). The second identity is proved similarly.
By Gelfand-Leray formula we have

(5) d
dt (
∫ ∫

γ(t)
 dH ∧ x
k+1yldy) = ∮

δ(t)
 x
k+1yldy = (k + 1)Ik,l(t).

Replacing H by ∑

(i,j)∈Z2 hijx
iyj we get the third identity. The fourth equality is

proved similarly. □

For our particular choice H(x, y) = x
2y(1 − x − y) we can rewrite the relations
of Lemma 2.2 in more convenient form. We have

(6) ( t(k + 1) −k − 3 k + 4 k + 3
t(l + 1) −l − 2 l + 2 l + 3
 ) ·
 




 Ik,l
Ik+2,l+1
Ik+3,l+1
Ik+2,l+2
 



 = (
0
0

) .

Multiplying by ( l + 3 −k − 3
−l − 2 k + 4
 ) from the left we get an equivalent for k + l ̸=

−6 system of equations:

(7) ( −2t(l − k) −k − 3 k + l + 6 0
t(3l − k + 2) −l − 2 0 k + l + 6
 ) ·
 




 Ik,l
Ik+2,l+1
Ik+3,l+1
Ik+2,l+2
 



 = (
0
0
) .

In other words, Ik+3,l+1(t) and Ik+2,l+2(t) can be represented as µk,l
1 (t)Ik,l(t) +
µk,l
2 (t)Ik+2,l+1(t), where µk,l
1 is a polynomial of degree at most 1 and µk,l
2 is a
constant. We have such representation for any pair (k, l) such that k + l ̸= −6.
Another corollary of (6):

(8) ( −2l + k − 1 3l − k + 2 2l − 2k ) ·
 

 Ik+2,l+1
Ik+3,l+1
Ik+2,l+2
 

 = 0.

The equation (8) gives us linear dependence between Ik+2,l+1, Ik+3,l+1 and Ik+2,l+2
in all cases except k = l = −1. But in this case the equation (7) becomes:

(9) ( 0 −2 4 0
0 −1 0 4
 ) ·
 




 I−1,−1
I1,0
I2,0
I1,1
 



 = (
0
0

) .

Recall that J1(t) = I0,0(t), J2(t) = I2,0(t) and J3(t) = I3,0(t).

Lemma 2.3. For any polynomial 1-diﬀerential form ω the Abelian integral I(t) =∫

δ(t) ω can be represented as p1(t)J1(t)+p2(t)J2(t)+p3(t)J3(t) for some polynomials
pi(t) of degree less than or equal to n
4 , where n = deg ω.

4 SERGEY MALEV AND DMITRY NOVIKOV

Remark 2.4. The proof of this result below essentially provides the coeﬃcients
pi(t), i.e. provides an eﬀective decomposition in the Petrov module corresponding
to H. This result does not formally follow from the result of Gavrilov [4] since
x
2y(1 − x − y) is not a semi-weighted homogeneous polynomial. However, in this
simple situation it can be obtained by a straightforward computation.

Proof. First of all we will give such a representation for all Ik,l(t) if k + l ≤ 3,
k, l ≥ 0. By (9) we have I1,0 = 2J2 and I1,1 = 1
2 J2. Using (8) one can calculate
the required representation for I0,1 and I2,1. This implies similar representation for
I0,2 and I1,2 and then for I0,3. Note that for these integrals the coeﬃcients pi are
polynomials of degree 0, i.e. scalar.
For n = i + j ≥ 4 the proof goes by induction on n. Using (7), we see that the
required representation of Ik,n−k for 2 ≤ k ≤ n − 1, together with bounds on the
degrees of pi, follows from the same for Ik,l with smaller k + l. Using (8) one can
obtain that I1,n−1 is a linear combination of I1,n−2 and I2,n−2 (for k = −1 and
l = n − 3) because 2l − 2k = 2n − 4 > 0. Thus we obtain a required representation
for I1,n−1 and similarly for I0,n. Now we use (8) for k = n − 3 and l = −1 to obtain
representation of In,0 as a linear combination of In−1,0 and In−1,1. One can easily
check that the degrees of pi are bounded by n/4 in all these cases. □

3. Construction of the Picard-Fuchs system.

It is well known that the eﬀective decomposition in Petrov modules allows to ex-
plicitly construct the Picard-Fuchs system for the generators of the Petrov module,
see e.g. [9]. Here we follow this classical path.

Lemma 3.1. The column J =
 

J1(t)
J2(t)
J3(t)


 satisﬁes the system

(10) J = d
dt ((A + tB)J),

where A =
 

0 − 1
12 1
12
0 − 1
56 1
56
0 − 5
504 5
504
 

 and B =
 


 2
3 0 0
0 4
7 0
0 2
21 4
9
 

 .

Proof. of the lemma 3.1:
By Lemma 2.2 for any k and l (and in particular for l = 0 and k = 0, 1, 3) we
have (l + 1) · Ik,l(t) = ∑
i,j jhi,j · d
dt Ik+i,l+j (t).
It implies

(11) Ik,0 = d
dt (Ik+2,1 − Ik+3,1 − 2Ik+2,2).

LINEAR ESTIMATE FOR THE NUMBER OF ZEROS OF ABELIAN INTEGRALS 5

Using Lemma 2.3 we represent Ik,1 for 2 ≤ k ≤ 6 and Ik,2 for k = 2, 4 and 5 in
terms of Ji. After calculation we obtain the result:

I2,1 = 1
2 J2 − 1
2 J3,

I3,1 = 1
4 J2 − 1
4 J3,

I4,1 = 1
7 J2 − 1
7 J3 − 4
7 tJ2,

I5,1 = 5
56 J2 − 5
56 J3 − 6
7 tJ2,(12)
 I6,1 = 5
84 J2 − 5
84 J3 − 4
7 tJ2 − 2
3 tJ3,

I2,2 = 1
6 J2 − 1
6 J3 − 1
3 tJ1,

I4,2 = 1
28 J2 − 1
28 J3 − 1
7 tJ2,

I5,2 = 5
252 J2 − 5
252 J3 − 4
21 tJ2 + 1
9 tJ3,

The formulas (11) and system (12) together immediately imply the system (10).
□

The system (10) can be rewritten as

(13) (A + tB) · J ′ = (I3×3 − B) · J,

where I3×3 is the 3-dimensional identity operator.
This equation can be rewritten as

(14) D(t) · J ′(t) = Q(t) · J(t),

where
 Q(t) =
 

− 1
2 + 32t 9 −10
0 3
2 + 48t − 5
2
0 3
2 − 24t − 5
2 + 80t



 and D(t) = 64t2 − t.

Introducing new variables X = t− 1
2 J1, Y = J2, Z = J3 we have

(15)
 



D(t)
√tX ′ = 9Y − 10Z
D(t)Y ′ = ( 3
2 + 48t)Y − 5
2 Z
D(t)Z ′ = ( 3
2 − 24t)Y + (− 5
2 + 80t)Z

4. Proof of Theorem 1.1

Take any Abelian integral I(t). By Lemma 2.3 I(t) = p1(t)J1(t) + p2(t)J2(t) +
p3(t)J3(t) where deg pi ≤ n
4 . Thus I(t) = √
tp1X + p2Y + p3Z.
Using (15), we obtain

(16) ( I
p1√
t
 )′ = 1
Dp2
1t√t · (˜p1Y + ˜p2Z),

where ˜pi are some polynomials of degree less than or equal to n
2 + 2.

6 SERGEY MALEV AND DMITRY NOVIKOV

Recall that Z = J3 = I0,3(t) = ∫∫

γ(t) y3dx ∧ dy, so Z is positive for t ∈ (0, 1
64 ) by

Remark 2.1. Hence the function w = Y
Z is well-deﬁned and by (15) satisﬁes the
Riccati equation

(17) Dw′ = (
− 3
2 + 24t) w2 + (4 − 32t) w − 5
2 .

So for the function S(t) = ˜p1w + ˜p2 we have

DS′ = (− 3
2 + 24t) ˜p1w2 + (D ˜p′
1 + (4 − 32t)˜p1)w + D ˜p′
2 − 5
2 ˜p1.

One can obtain

D ˜p1S′ = (
− 3
2 + 24t) (S − ˜p2)
2 + (D ˜p′
1 + (4 − 32t)˜p1)(S − ˜p2) + (
D ˜p′
2 − 5
2 ˜p1
) ˜p1.

Thus the Riccati equation for the function S(t) reads as

(18) D ˜p1S′ = AS2 + BS + C,

where A, B and C are polynomials and deg C ≤ n + 5. Now one can introduce new
time τ and rewrite (18) as a system

(19)
 { ˙t = D ˜p1
˙S = AS2 + BS + C,

where ˙ϕ denotes dϕ
dτ . Denote by ∆j, j = 1, . . . , k (k ≤ deg ˜p1 + 1) the open intervals
into which (0, 1
64 ) is split by the zeros of ˜p1. It is clear that in ∆j between any two
zeros of S there is a zero of C. Let λj be the number of zeros of C on ∆j. Thus
the number of zeros of S in ∆j is less than or equal to λj + 1. So the number of

zeros of S in (0, 1
64 ) is less than or equal to k∑

j=1(λj + 1) ≤ deg C + deg ˜p1 + 1. Thus

it does not exceed n + 5 + n
2 + 2 + 1 = 3
2 n + 8. By (16) we obtain that on (0, 1
64 )

the number of zeros of ( I
p1√t
 )′ does not exceed 3
2 n + 8.

Denote by Ξj, j = 1, . . . , l (l ≤ deg p1 + 1) the open intervals into which (0, 1
64 )
is split by the zeros of p1. It is clear that in Ξj between any two zeros of I

(i.e. zeros of I
p1√t ) there is a zero of ( I
p1√t
 )′. Let lj be the number of zeros

of ( I
p1√
t
 )′ on Ξj. Thus the number of zeros of I in Ξj is less than or equal to

lj + 1. So the number of zeros of I in (0, 1
64 ) is less than or equal to l∑

j=1
(lj + 1) and

l∑

j=1 lj ≤ 3
2 n + 8. Thus the number of zeros of I in (0, 1
64 ) is less than or equal to

3
2 n + 8 + l ≤ 3
2 n + 8 + n
4 + 1 = 7
4 n + 9. This proves Theorem 1.1.

References

[1] G. Binyamini, D. Novikov, S. Yakovenko, On the number of zeros of Abelian integrals (2008).
[2] S. Gautier, Quadratic centers deﬁning elliptic surfaces, J. of Diﬀ. Eq., 245 (2008), no 12, p.
3545-3569.
[3] S. Gautier, L. Gavrilov, ID. Iliev, Perturbations of quadratic centers of genus one (2007).

LINEAR ESTIMATE FOR THE NUMBER OF ZEROS OF ABELIAN INTEGRALS 7

[4] L. Gavrilov, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math. 122 (1998), no. 8,
571–584.
[5] F. Girard, M.-A. Jebrane, Majorations aﬃnes du nombre de zeros d’integrales abeliennes
pour les hamiltoniens quartiques elliptiques, Annales de la faculte des sciences de Toulouse,
Ser. 6, 7 no. 4 (1998), p. 671-685.
[6] E. Horozov, I. D. Iliev, Linear estimate for the numbers of zeros of Abelian integrals with
cubic Hamiltonians (1998).
[7] I. D. Iliev, Perturbations of quadratic centers, Bull. Sci. Math. 122 (1998), no. 2, 107161.
[8] Yu. Ilyashenko, Centenial History of Hilbert’s 16th problem Bull. Amer. Math. Soc. (N.S.)
39 (2002), no. 3, 301–354 (electronic).
[9] S. YakovenkoBounded decomposition in the Brieskorn lattice and Pfaﬃan Picard–Fuchs sys-
tems for Abelian integrals, Bull. Sci. Math 126 (2002), no. 7, 535–554.
[10] H. ˙Zol¸adek, The monodromy group, Instytut Matematyczny Polskiej Akademii Nauk. Mono-
graﬁe Matematyczne (New Series) [Mathematics Institute of the Polish Academy of Sciences.
Mathematical Monographs (New Series)], vol. 67, Birkh¨auser Verlag, Basel, 2006.

Faculty of Mathematics and Computer Science, The Weizmann Institute of Science
POB 26, Rehovot 76100, ISRAEL
E-mail address: sergey.malev@weizmann.ac.il

Faculty of Mathematics and Computer Science, The Weizmann Institute of Science
POB 26, Rehovot 76100, ISRAEL
E-mail address: dmitry.novikov@weizmann.ac.il
