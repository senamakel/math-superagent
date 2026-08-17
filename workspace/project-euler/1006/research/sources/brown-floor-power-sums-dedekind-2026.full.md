<!-- source: https://nntdm.net/papers/nntdm-32/NNTDM-32-1-076-087.pdf | converted from PDF -->

Notes on Number Theory and Discrete Mathematics
Print ISSN 1310–5132, Online ISSN 2367–8275
2026, Volume 32, Number 1, 76–87
DOI: 10.7546/nntdm.2026.32.1.76-87

On a family of sums of powers of the floor function
and their links with generalized Dedekind sums

Steven Brown

48 rue Pottier, 78150 Le Chesnay Rocquencourt, France
e-mail: steven.brown.math@gmail.com

Received: 3 October 2025 Revised: 20 February 2026
Accepted: 23 February 2026 Online First: 23 February 2026

Abstract: In this paper we are concerned with a family of sums involving the floor function.
With r a nonnegative integer and n and m positive integers we consider the sums

Sr (n, m) :=
 n−1∑

k=1
 ⌊ km
n
 ⌋r.

While a formula for S1 is well known, we provide closed-form formulas for S2 and S3 as well
as the reciprocity laws they satisfy. Additionally, one can find a closed-form formula for the
classical Dedekind sum using the Euclidean algorithm. Finally, we provide a general formula for
Sr showing its dependency on generalized Dedekind sums.
Keywords: Sum of powers of the floor function, Dedekind sums, Faulhaber sums, Reciprocity
laws, Euclidean algorithm.
2020 Mathematics Subject Classification: 11F20, 11A05.

1 Introduction

The analysis of the sums Sr (n, m) defined below (see (1)) was motivated due to their links with
Dedekind sums (see Proposition 5.1) which have applications in many areas of mathematics.
A broad overview of the Dedekind sums and their applications can be found in the introduction
of [4], a reference monograph on the topic by Hans Rademacher and Emil Grosswald.

Copyright © 2026 by the Author. This is an Open Access paper distributed under the
terms and conditions of the Creative Commons Attribution 4.0 International License
(CC BY 4.0). https://creativecommons.org/licenses/by/4.0/

1.1 Notations

For any real number x we denote by ⌊x⌋ the floor function defined as the greatest integer less than
or equal to x. For an integer a and a positive integer b, we use a mod b to mean the remainder of
a when divided by b.
The sums of interest are noted as follows:

Sr (n, m) :=
 n−1∑

k=1
 ⌊ km
n
 ⌋r. (1)

We also use the following notation for the Faulhaber sums (see [5]):

Fr (n) :=
 n∑

i=0 i
r. (2)

For positive coprime integers a and b we use the notation s(b, a) as in Rademacher’s book [4]
to denote the classical Dedekind sum:

s(b, a) :=
 a∑

k=1
 (( kb
a
 )) ((k
a
 )) (3)

with the symbol ((x)) defined by

((x)) :=
 { {x} − 1
2, if x /∈ Z,
0, if x ∈ Z. (4)

We use as well a definition of generalized Dedekind sums suggested by Don Zagier in the
article [6, Eq. 40, p. 157]. In this definition, b and n are positive integers and the coefficients ai
for i from 1 to n are positive integers coprime with b:

δ(b; a1, . . . , an) := 2nbn−1 b−1∑

k=1
 n∏

i=1
 (( kai
b
 )) . (5)

1.2 General considerations

Proposition 1.1. Let a, b and r be positive coprime integers. If a and b are coprime, then

Sr (b, a) +
 r∑

i=0 (−1)i+1(
r
i
)
(a − 1)
r−iSi (b, a) = 0. (6)

Proof. Let k be an integer satisfying 0 < k < b. Let uk := ⌊ ka
b ⌋ and vk := ⌊ −ka
b ⌋. The ratio ka
b
is not in Z and therefore, as a property of the floor function
1, we have uk + vk = −1:

—————-

1 ∀x ∈ R, ⌊x⌋ + ⌊−x⌋ =
 { 0, if x ∈ Z,
−1, if x /∈ Z.
 77

⌊ ka
b
 ⌋r − ⌊ (b − k)a
b
 ⌋r = ukr − (a + vk)
r

= ukr − (a − 1 − uk)r

= ukr −
 r∑

i=0
 (
r
i
)(−uk)
i(a − 1)r−i

= ukr +
 r∑

i=0 (−1)
i+1(r
i
)
(a − 1)
r−iuki.

We can take the sum of the last equation for k from 1 to b − 1. The left-hand side sums to zero
as the difference of two equal sums (the two sums index are in reverse order). On the right-hand
side we recognize the sums Si (b, a) for i from 0 to r.

Proposition 1.2. Let m, n and r be positive integers. Let d = gcd(n, m) such that there exist two
positive coprime integers b and a such that n = db and m = da. We have

Sr (n, m) = arFr (d − 1) +
 r∑

k=0
 (r
k
)
akFk (d − 1) Sr−k (b, a) . (7)
Proof.
 Sr (n, m) =
 n−1∑

k=0
 ⌊ ka
b
 ⌋r

=
 d−1∑

i=0
 b−1∑

j=0
 ⌊ (ib + j)a
b
 ⌋r

=
 d−1∑

i=0
 b−1∑

j=0
 r∑

k=0
 (r
k
)
ikak ⌊ ja
b
 ⌋r−k .

The case k = r needs attention since ∑b−1
j=0 ⌊ ja
b ⌋r−r = 1 + S0 (b, a):

Sr (n, m) = arFr (d − 1) (1 + S0 (b, a)) +
 r−1∑

k=0
 (r
k
)
akFk (d − 1) Sr−k (b, a)

= arFr (d − 1) +
 r∑

k=0
 (r
k
)
akFk (d − 1) Sr−k (b, a) .

Equation (7) shows that in general (whether m and n are coprime or not) the formula of
Sr (n, m) only depends on Si (b, a) for 0 ≤ i ≤ r and some known Faulhaber sums. Therefore it
is enough to focus on studying Sr (b, a) with b and a positive coprime integers.

2 Formulas for Si for 0 ≤ i ≤ 3

2.1 A formula for S1 (n, m)

A formula for S1 (n, m) is provided and proved in [3] and also in [2, p. 94]. If m and n are
positive integers and if d = gcd(m, n), then

S1 (n, m) = (m − 1)(n − 1)
2 + d − 1
2 . (8)

78

We give here a first2 alternative proof of Equation (8). Let a and b be the positive coprime
integers defined by m = da and n = db. From Proposition 1.1 with r = 1 we have

2S1 (b, a) − (a − 1)S0 (b, a) = 0.

It is clear that S0 (b, a) = b − 1 (9)

and therefore
 S1 (b, a) = (a − 1)(b − 1)
2 . (10)

We write now Equation (7) from Proposition 1.1 with r = 1:

S1 (n, m) = aF1 (d − 1) + F0 (d − 1) S1 (b, a) + aF1 (d − 1) S0 (b, a) .

This equation gives Equation (8) knowing that F0 (d − 1) = d and F1 (d − 1) = (d − 1)d
2 .

2.2 A formula for S2 (n, m)

In this section we carry out a direct calculation of S2 (n, m) and establish an equation involving
another sum of interest that will be studied separately. We have the positive integers m, n, a, b,
d and k such that m = da, n = db and a and b are coprime. We write now Equation (7) from
Proposition 1.2 with r = 2:

S2 (n, m) = a2F2 (d − 1) +

F0 (d − 1) S2 (b, a) + 2aF1 (d − 1) S1 (b, a) + a2F2 (d − 1) S0 (b, a) .

Since all is known apart from S2 (b, a), we have

S2 (n, m) = (d − 1)m
6 ((2d − 1)ab + 3(a − 1)(b − 1)) + dS2 (b, a) .

Since we have ⌊ ka
b
 ⌋ = ka
b − { ka
b
 } , (11)

summing the square of Equation (11) for k from 1 to b − 1 leads to

S2 (b, a) =
 b−1∑

k=1
 ( ka
b
 )2 +
 b−1∑

k=1
 { ka
b
 }2 − 2
 b−1∑

k=1
 ka
b
 { ka
b
 }

= 1 + a2

b2 F2 (b − 1) − 2 a
b2
 b−1∑

k=1 k(ka mod b).

Let us define the function Wn (a, b) by the following sum:

Wn (a, b) :=
 n−1∑

k=1(ak mod n)(bk mod n). (12)

—————

2 A second proof is given in Section 5.
 79

We also give a sense to this function when at least one of its arguments is equal to one through
this definition Wn (a) := Wn (a, 1) . (13)

With this definition we get to

S2 (b, a) = (1 + a2)(b − 1)(2b − 1)
6b − 2 a
b2 Wb (a) , (14)

and therefore

S2 (n, m) = d
6b (
(b − 1)(2b − 1) + a2(n − 1)(2n − 1)
) − m
2 (d − 1)(b − 1) − 2 m
b2 Wb (a) . (15)

This formula together with Equation (22) from Section 3.3 provides a closed-form formula
for S2 (n, m).

2.3 A formula for S3 (n, m)

Let us write Equation (6) from Proposition 1.1 with r = 3:

2S3 (b, a) − (a − 1)
3S0 (b, a) + 3(a − 1)
2S1 (b, a) − 3(a − 1)S2 (b, a) = 0.

By means of Equations (9), (10) and (14), the above equation gives:

S3 (b, a) = 1
4b (b − 1)(a − 1) ((b − 1)(1 + a2) + 2ab) − 3
b2 a(a − 1)Wb (a) . (16)

We now write Equation (7) from Proposition 1.2 with r = 3. There is

S3 (n, m) = a3F3 (d − 1) + F0 (d − 1) S3 (b, a) +

3aF1 (d − 1) S2 (b, a) + 3a2F2 (d − 1) S1 (b, a) + a3F3 (d − 1) S0 (b, a) .

Using known formulas for Faulhaber sums, as well as Equations (9), (10), (14) and (16), we
get to

S3 (n, m) = 1
4 (d − 1)am ((d − 1)bm + (2d − 1)(a − 1)(b − 1))

+ 1
4bd(1 + a2)(b − 1) ((d − 1)a(2b − 1) + (b − 1)(a − 1))

+ 1
2m(b − 1)(a − 1) − 3
b2 m(m − 1)Wb (a) . (17)

This formula together with Equation (22) from Section 3.3 provides a closed-form formula
for S3 (n, m).

3 Analysis of W

The objective of this section is to give a closed-form formula for Wn (m) in order to finalize the
calculation of S2 (n, m) in Equation (15) and of S3 (n, m) in Equation (17). The analysis of W
provides an elementary proof
3 of the simplest form of Dedekind’s reciprocity law.

—————-

3 Although it is not fundamentally a new proof, one can see it in Section 4.1.

80

3.1 Basic properties of W

In the previous section we introduced the function W in Equations (12) and (13). The objective
of this section is to provide some of its properties.

Proposition 3.1. Let n, a, b and c be any positive integers, then we have the following:

(i) Wn (a, b) = Wn (a mod n, b mod n),

(ii) If gcd(c, n) = 1, we have Wn (ac, bc) = Wn (a, b),

(iii) If ab mod n = 1, we have Wn (a) = Wn (b),

(iv) Wn (a) + Wn (n − a) = 1
2n2(n − 1).

Proof. (i) comes from ak mod n = ((a mod n)k) mod n.

(ii) Whenever the positive integer c is coprime with n, the application x ↦→ cx mod n is a
bijection of {1, . . . , n − 1}. In that case, we have Wn (ac, bc) = Wn (a, b).

(iii)
 Wn (a) =
 n−1∑

k=1(bk mod n)(a(bk mod n) mod n)

=
 n−1∑

k=1(bk mod n)((ab mod n)k mod n)

= Wn (b) .

For the second equality we use the fact that ab mod n = 1 implies that gcd(b, n) = 1 and
therefore k ↦→ bk mod n is a bijection of An.

(iv) Wn (a) + Wn (n − a) =
 n−1∑

k=1 k {(ak mod n) + (−ak mod n)} .

Proposition 3.2. Let d = gcd(m, n), where m = da and n = db with a and b coprime. We have
the following equation
 Wn (m) = d2Wb (a) + 1
4 n
2(d − 1)(b − 1). (18)

Proof. Wn (m) =
 db−1∑

k=1 k(dak mod db)

= d
 d−1∑

j=0
 b−1∑

k=0(k + jb)(a(k + jb) mod b)

= d2Wb(a) + db
 d−1∑

j=0 j
 b−1∑

k=0(ak mod b)

= d2Wb(a) + 1
4n2(d − 1)(b − 1).

Note that when m and n are coprime, then d = 1 and the equation is obviously satisfied. We
can now focus on calculating Wb (a) when b and a are coprime.
81

3.2 Calculation of Wb (a) when a and b are coprime

Given that from property (ii) Wb (a) = Wb (a mod b) and that gcd(a, b) = 1 implies
gcd(a mod b, b) = 1, we can work under the assumption that 0 < a < b even if it means
considering a mod b instead of a. According to Definition (12),

Wb (a) =
 b−1∑

k=1 k(ak mod b).

Note that the term k(ak mod b) inside the sum is zero for k = b. In particular, we can write
Wb (a) in a slightly different way:

Wb (a) =
 a−1∑

j=0
 ⌊ (j+1)b
a ⌋∑

k=⌊ jb
a ⌋+1 k(ak mod b).

The integer variable k of the inner sum satisfies

jb
a < ⌊ jb
a
 ⌋ + 1 ≤ k ≤ ⌊ (j + 1)b
a
 ⌋ ≤ (j + 1)b
a ,

which implies 0 < ka − jb ≤ b.

It should be noted that the right-hand side inequality is always a strict inequality apart from
the case when j = a − 1 and k = b. Indeed, when 0 ≤ j < a − 1, the ratio (j + 1)b
a is never an
integer. If that was the case, knowing that a and b are coprime, the Gauss lemma would imply
that a divides j + 1 which is not possible since 0 < j + 1 < a. That means that apart from the
case j = a − 1 and k = b we have
 ka mod b = ka − jb.

Now we can write
 Wb (a) =
 



 a−1∑

j=0
 ⌊ (j+1)b
a ⌋∑

k=⌊ jb
a ⌋+1 k(ka − jb)




 − b2.

Note that when j = a − 1 and k = b, the expressions k(ka − jb) = b2 and k(ka mod b) = 0
are not equal, the reason why we need to substract b2.
The first part of the sum is easily simplified

a−1∑

j=0
 ⌊ (j+1)b
a ⌋∑

k=⌊ jb
a ⌋+1 ak2 = a
 b∑

k=1 k2

= ab(b + 1)(2b + 1)
6 .

82

We are now left with the calculation of the second term of the sum:

A := −b
 a−1∑

j=0 j ⌊ (j+1)b
a ⌋∑

k=⌊ jb
a ⌋+1 k.

We have
 A = − b
2
 a−1∑

j=0 j (⌊ (j + 1)b
a
 ⌋ (⌊(j + 1)b
a
 ⌋ + 1) − ⌊ jb
a
 ⌋ (⌊jb
a
 ⌋ + 1))

= − b
2
 a∑

j=1 (j − 1) ⌊ jb
a
 ⌋ (⌊jb
a
 ⌋ + 1) + b
2
 a−1∑

j=0 j ⌊ jb
a
 ⌋ (⌊jb
a
 ⌋ + 1)

= b
2S2 (a, b) + b
2 S1 (a, b) − b
2(a − 1)b(b + 1).

Using Equation (10), after some simplifications we get to

Wb (a) = b
2 S2 (a, b) + b
12(b − 1)(2b − 1)(3 − a). (19)

3.3 Formula for Wa (b) using the Euclidean algorithm

The purpose of this section is to provide a closed-form formula for Wa (b) for two positive
coprime integers a and b with a < b. From Equation (24) and using property (ii) we can write

Wa (b) = f (a, b) − (a
b
 )2 Wb (a mod b) (20)

with f being the following function

f (x, y) := x
12y ((1 + x2)(1 + y2) − xy(x − 3)(y − 3)) . (21)

Let (un)n∈N be the sequence defined by the first two terms, u0 = a, u1 = b, and the following
induction equation ui+2 = ui mod ui+1 for i ≥ 0. This sequence is the sequence of remainders
of Euclid’s algorithm (see [1]). We know that (un)n∈N is strictly decreasing until it reaches
uN = 1 = gcd(a, b) for a specific index N ≥ 1. Then for any i > N we have ui = 0. For
i from 0 to N − 1 we have gcd(ui, ui+1) = 1 and we can write N times Equation (20) for
Wui (ui+1). Compounding these N equations leads to

Wu0 (u1) =
 (N −1∑

k=0 (−1)
k( u0
uk
 )2f (uk, uk+1)
)
 + (−1)
N ( u0
uN
 )2WuN (uN +1) .

Given that uN +1 = 0, we have WuN (uN +1) = 0 and we are left with

Wa (b) = a2

12
 N −1∑

k=0 (−1)
k ( (1 + uk2)(1 + uk+12)
ukuk+1 − (uk − 3)(uk+1 − 3)
) . (22)

As a consequence, we have closed-form formulas
4 for S2 (b, a), S2 (n, m), S3 (b, a), S3 (n, m),
Wn (m) and the classical Dedekind sum s(b, a) respectively from Equations (14), (15), (16), (17),
(18) and (26).
——————–

4 Don Zagier in [6, p. 166] had already noticed that the classical Dedekind sum was fully determined from their
properties and the use of the Euclidean algorithm.83

4 Reciprocity laws

With positive and coprime integers a and b, the consideration of Equations (19) and (14) yields
easily to the following symetrical equations that could be considered as reciprocity laws:

Theorem 4.1 (Reciprocity law for S2). If a and b are positive coprime integers, then

aS2 (a, b) + bS2 (b, a) = 1
6(a − 1)(2a − 1)(b − 1)(2b − 1). (23)

Proof. In Equation (14), we replace Wb (a) by its expression from Equation (19).

Theorem 4.2 (Reciprocity law for W). If a and b are positive coprime integers, then

a2Wb (a) + b2Wa (b) = ab
12 ((1 + a2)(1 + b2) − ab(a − 3)(b − 3)) . (24)

Proof. In Equation (14), we swap a and b and inject the expression of S2 (a, b) in Equation
(19).

Theorem 4.3 (Reciprocity law for S3). If a and b are positive coprime integers, then

a(a − 1)S3 (a, b) + b(b − 1)S3 (b, a) = 1
4 (a − 1)
2(b − 1)
2 ((a − 1)(b − 1) + ab) . (25)

Proof. In Equation (6) for r = 3, we replace S0 and S1 according to their formulas in Equations
(9) and (10) and get an Equation between S2 and S3. With this equation and the reciprocity law
for S2 in (23) we easily get Equation (25).

4.1 A proof of Dedekind’s reciprocity law

The proof of Dedekind’s reciprocity law
5 that we give here is in essence the same as the one given
in [6, p. 153] although it is presented differently.
In the definition Equation (3) of the classical Dedekind sum, the summand for k = a is equal
to 0. For 0 < k < a both kb
a and k
a are not in Z:

s(b, a) =
 a−1∑

k=1
 ( kb mod a
a − 1
2
 ) (k
a − 1
2
)

= 1
a2 Wa (b) − 1
4 (a − 1),

that is
 Wa (b) = a2 (s(b, a) + a − 1
4
 ) . (26)

This reciprocity law satisfied by the classical Dedekind sum results from the reciprocity law
satisfied by W (Equation (24)) and the relation between W and the classical Dedekind sum
(Equation (26)). Combining these two equations yields:

a2b2 (s(b, a) + a − 1
4
 ) + a2b2 (
s(a, b) + b − 1
4
 ) =

ab
12 ((1 + a2)(1 + b2) − ab(a − 3)(b − 3)) ,

—————–

5 Not to be mistaken with the Quadratic reciprocity law.

84

from where we get the reciprocity law for Dedekind sums:

s(b, a) + s(a, b) = −1
4 + 1
12
 ( a
b + 1
ab + b
a
 ) .

4.2 A formula for the classical Dedekind sum

From Equation (26) we have
 s(b, a) = Wa (b)
a2 − a − 1
4 .

This equation together with Equation (22) gives a closed-form formula for s(b, a) as a function
of the remainders obtained with the Euclidean algorithm applied to u0 = b and u1 = a (see
Section 3.3).

5 Expression of Sr (b, a) as a function
of generalized Dedekind sums

Proposition 5.1. For positive coprime integers a and b and for a positve integer r we have the
following expression for Sr (b, a)

Sr (b, a) = b
2r ∑

u+v+w=r
u,v,w≥0
 ( r
u, v, w
) ( a
b
 )u (−1
b
 )v (a − 1)
wδ(b; 1, . . . , 1
︸ ︷︷ ︸
u times , a, . . . , a
︸ ︷︷ ︸
v times ). (27)

Proof. We transform Sr (b, a) using the trinomial expansion and recognize generalized Dedekind
sums (Equation (5)) in the expression:

Sr (b, a) =
 b−1∑

k=1
 ( ka
b − a
2 − ({ka
b
 } − 1
2
) + a − 1
2
 )r

=
 b−1∑

k=1
 ∑

u+v+w=r
u,v,w≥0
 ( r
u, v, w
)
au (k
b − 1
2
)u (−1)
v ({ ka
b
 } − 1
2
 )v ( a − 1
2
 )w

= ∑

u+v+w=r
u,v,w≥0
 ( r
u, v, w
)
au(−1)
v ( a − 1
2
 )w 2
u+vbu+v−1

2u+vbu+v−1
 b−1∑

k=1
 (( k
b
 ))u (( ka
b
 ))v .

5.1 Application of Equation (27)

In this section, we use Equation (27) to prove Equations (10), (14) and (16). In the following
proofs, we use the fact that the generalized Dedekind sum (5) is zero when n is odd. The sum in
(27) is on all nonnegative integers u, v and w such that u + v + w = r. The previous argument
means that we can discard the triplets (u, v, w) where u + v is even since they contribute to zero
to the formula because of the factor δ(b; 1, . . . , 1
︸ ︷︷ ︸
u times , a, . . . , a
︸ ︷︷ ︸
v times ) which is equal to zero in that case.

85

5.1.1 Another proof of Equation (10)

To calculate S1 (b, a) with (27) the only possibility is (u, v, w) = (0, 0, 1) hence

S1 (b, a) = b
2 (a − 1)δ(b; ∅).

But
 δ(b; ∅) = 2
0b−1 b−1∑

k=1
 ∏

a∈∅
 (( ka
b
 ))

= (b − 1)
b . (28)

Hence
 S1 (b, a) = (a − 1)(b − 1)
2 ,

which is Equation (10).

5.1.2 Another proof of Equation (14)

To calculate S2 (b, a) with (27) the only possibilities for (u, v, w) are (0, 0, 2), (2, 0, 0), (1, 1, 0),
and (0, 2, 0), therefore,

S2 (b, a) = (a − 1)
2b
4 δ(b; ∅) + a2

4b δ(b; 1, 1) − a
2b δ(b; 1, a) + 1
4b δ(b; a, a). (29)

From Equations (9) in [6, p. 151], we have

δ(b; a, a) = δ(b; 1, 1). (30)

A straightforward calculation leads to

δ(b; 1, 1) = 1
3 (b − 1)(b − 2). (31)

We now calculate δ(b; 1, a) by means of Equation (26).

δ(b; 1, a) = 4bs(a, b)

= 4
b Wb (a) − b(b − 1). (32)

Finally, we get Equation (14) after using Equations (28), (30), (31) and (32) in Equation (29).

5.1.3 Another proof of Equation (16)

Similarly, in order to calculate S3 (b, a) with (27) the only possibilities for (u, v, w) are (0, 0, 3),
(2, 0, 1), (1, 1, 1), and (0, 2, 1), which leads to

S3 (b, a) = (a − 1)
3b
8 δ(b; ∅) + 3a2(a − 1)
8b δ(b; 1, 1)

− 3a(a − 1)
4b δ(b; 1, a) + 3(a − 1)
8b δ(b; a, a). (33)

We get Equation (16) after using Equations (28), (30), (31) and (32) in Equation (33).

86

6 Conclusion

In this paper, we have given closed-form formulas for S2, S3, W and the classical Dedekind
sums. In addition, we have shown the reciprocity laws that these expressions satisfy. In the last
section, we have shown how Sr depend on generalized Dedekind sums through Equation (27).
For r ≥ 4 there is more than one Dedekind sum involved in the formula of Sr making the analysis
more difficult than it is for S2 and S3 where only one Dedekind sum is involved, however that
could probably be investigated further.

Acknowledgements

I would like to thank William Gasarch for kindly accepting to peer review this paper and for
providing insightful comments. I also thank my wife Natallia for her continuous support.

References

[1] Damphousse, P. (2000). Opuscules. D´ecouvrir l’Arithm´etique. Ellipses.

[2] Graham, R. L., Knuth, D. E., & Patashnik, O. (1994). Concrete Mathematics: A Foundation
for Computer Science. Addison-Wesley Professional.

[3] Polezzi, M. (1997). A geometrical method for finding an explicit formula for the greatest
common divisor. The American Mathematical Monthly, 104(5), 445–446.

[4] Rademacher, H., & Grosswald, E. (1972). Dedekind Sums (Vol. 16). American
Mathematical Society.

[5] Schumacher, R. (2016). An extended version of Faulhaber’s formula. Journal of Integer
Sequences, 19(4), Article 16.4.

[6] Zagier, D. (1973). Higher dimensional Dedekind sums. Mathematische Annalen, 202,
149–172.
 87
