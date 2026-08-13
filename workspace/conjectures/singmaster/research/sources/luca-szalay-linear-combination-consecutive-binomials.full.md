<!-- source: https://ami.uni-eszterhazy.hu/uploads/papers/finalpdf/AAPASM_31_from53to60.pdf | converted from PDF -->

Acta Academiae Paedagogicae Agriensis, Sectio Mathematicae 31 (2004) 53–60

LINEAR DIOPHANTINE EQUATION WITH
THREE CONSECUTIVE BINOMIAL COEFFICIENTS

Florian Luca
⋆ (UNAM, Mexico)
László Szalay (Sopron, Hungary)

Abstract. In this note, we study the diophantine equation A(
n
k)+B( n
k+1)+C( n
k+2)=0 in

positive integers (n,k), where A, B and C are ﬁxed integers.

AMS Classiﬁcation Number: 11D04, 11D09

1. Introduction

D. Singmaster (see [3]) found inﬁnitely many positive integer solutions (n, k)
to the diophantine equation

(1) (
n
k
) = (
n − 1
k + 1
).

All such solutions arise in a natural way from the sequence of Fibonacci
numbers (Fm)m≥0 given by F0 = 0, F1 = 1 and Fm+2 = Fm+1 + Fm for m ≥ 0.
Goetgheluck (see [1]) extended the above result and found inﬁnitely many positive
integer solutions (n, k) for the diophantine equation

2(
n
k
) = (
n − 1
k + 1
)
.

These solutions arise in a natural way from the positive integer solutions of the Pell
equation x
2 − 3y2 = −2. Several other diophantine equations involving binomial
coeﬃcients have been considered in [2], [4] and [5].

In this note, we ﬁx three integers A, B, C, not all zero, and look at the
positive integer solutions (n, k) of the equation A
(
n
k) + B( n
k+1) + C( n
k+2
) = 0. To
avoid degenerate cases, we shall assume that 1 ≤ k < k + 2 ≤ n − 1. We shall also
assume that AC ̸= 0. Indeed, say if A = 0, then the above equation simpliﬁes to

⋆ This research was partially sponsored by grants SEP-CONACYT 37259-E and 37260-E.

54 F. Luca, L. Szalay

(2) B( n
k + 1
) + C( n
k + 2

) = 0.

Obviously, equation (2) has no solution if BC > 0. Suppose that BC < 0 (say,
up to changing signs, that B < 0 and C > 0) and that gcd(B, C) = 1. Then
equation (2) implies B(k + 2) + C(n − k − 1) = 0, which can be rewritten as
n = ((C − B)k + C − 2B)/C = k + 1 − B(k + 2)/C. Thus, n is an integer if and
only if k ≡ −2 (mod C). Moreover, the conditions 1 ≤ k < k + 2 ≤ n − 1 are
always fulﬁlled if k > 1 and k ≥ −2(1 + C/B), and therefore (2) has inﬁnitely many
solutions.
The case when C = 0 can be reduced to the case when A = 0 by using the
symmetry of the binomial coeﬃcients and the substitution (A, C, k) ↦−→ (C, A, n −
k − 2).

Acknowledgements. This paper was written during a very enjoyable visit
by the ﬁrst author to University of West Hungary in Sopron; he wishes to express
his thanks to that institution for the hospitality and support.

2. Main Result

It is clear that we may assume that gcd(A, B, C) = 1 and that A > 0. Our
main result is the following.

Theorem. Let A, B and C be integers with A > 0, C ̸= 0 and gcd(A, B, C) = 1.
If the diophantine equation

(3) A
(
n
k
) + B( n
k + 1
) + C( n
k + 2

) = 0.

admits inﬁnitely many integer solutions 1 ≤ k < k + 2 ≤ n − 1, then one of the
following holds:
(i) B = A + C and C < 0, case in which all the solutions (n, k) are on the line

A(k + 2) + C(n − k) = 0,

(ii) A = A
2
0, B = −2A0C0, C = C2
0 hold with some positive coprime integers A0
and C0, case in which all solutions (n, k) with 1 ≤ k < k + 2 ≤ n − 1 of (3) are of
the form

(4) k + 2 = t(t + C0)
A0(A0 + C0) and n − k = t(t − A0)
C0(A0 + C0)

Linear diophantine equations with three consecutive binomial coeﬃcients 55

for some positive integer t.
(iii) B ̸= A + C, D = B2 − 4AC > 0 is not a perfect square, and

(5) X 2 − DY 2 = E

holds, where X = (B2 − 4AC)(n − k) − A(B − 2C), Y = 2A(k + 2) + B(n − k) − A,
E = 4A
2C(A−B +C), case in which all positive integer solutions (n, k) of equation
(3) can be found by solving the Pell like equation (5).

Proof. After simpliﬁcations, equation (3) becomes

A(k + 1)(k + 2) + B(k + 2)(n − k) + C(n − k)(n − k − 1) = 0.

Writing k + 2 = x, n − k = y we get

Ax(x − 1) + Bxy + Cy(y − 1) = 0,

or, equivalently,

(6) Ax
2 + Bxy + Cy2 − Ax − Cy = 0.

We shall assume that D := B2 − 4AC ̸= 0, and we shall return to the case
when D = 0 later.

With the substitution x = u + α, y = v + β, we get that the above relation
becomes

(7) (Au2 + Buv + Cv2) + (2Aα + Bβ − A)u + (Bα + 2Cβ − C)v

= −(Aα
2 + Bαβ + Cβ2) + Aα + Cβ.

We choose α and β such that the coeﬃcients of the linear terms in u and v in
equation (7) vanish. These lead to the system of equations

2Aα + Bβ = A,

Bα + 2Cβ = C,

whose rational solution is
 α = C(B − 2A)
B2 − 4AC ,

β = A(B − 2C)
B2 − 4AC .

56 F. Luca, L. Szalay

Note that we may divide by D = B2 − 4AC, because D ̸= 0. With the above
formulas for α and β, we get that

−(Aα
2 + Bαβ + Cβ2) + Aα + Cβ = −AC(A − B + C)
B2 − 4AC ,

and so equation (7) becomes

Au2 + Buv + Cv2 = −AC(A − B + C)
B2 − 4AC .

This last equation implies that

(2Au + Bv)
2 − (B2 − 4AC)v2 = −4A
2C(A − B + C)
B2 − 4AC ,

and since
 2Au + Bv = (2Ax + By) − (2Aα + Bβ)

= (2Ax + By) − 2AC(B − 2A) + AB(B − 2C)
B2 − 4AC = 2Ax + By − A,

while
 v = y − β = (B2 − 4AC)y − A(B − 2C)
B2 − 4AC ,

it follows that if we write
X := (B2 − 4AC)y − A(B − 2C),
Y := 2Ax + By − A,
E := 4A
2C(A − B + C),
we get that X, Y ∈ ZZ and

(8) X 2 − DY 2 = E.

We thus see that if D < 0, then the diophantine equation (3) has at most
ﬁnitely integer solutions 1 ≤ k < k + 2 ≤ n − 1. We now assume that D > 0. If
E = 0, then since AC ̸= 0, it follows that B = A+C. In this case, D = B2 −4AC =
(A − C)
2, and so pairs of integers X, Y satisfying equation (8) satisfy either

X = (C − A)Y or X = (A − C)Y.

In terms of the variables x and y, the above lines become

x + y = 1 or Ax + Cy = 0.

Linear diophantine equations with three consecutive binomial coeﬃcients 57

It is clear that the ﬁrst one admits no integer solutions x = k + 2 and y = n − k
for 1 ≤ k < k + 2 ≤ n − 1, while the second one admits inﬁnitely many such
solutions if and only if C < 0 (whereas if C > 0, then the second one does not
admit any such solutions either). Finally, if E ̸= 0, then equation (8) admits only
ﬁnitely many solutions (or none) if D is a perfect square, while if D is not a perfect
square, the above equation (8) is a Pell like equation, which either has no solutions,
or it has inﬁnitely many, and in this later case all integer solutions (X, Y ) of such
equation belong to ﬁnitely many binary recurrent sequences whose roots are the
fundamental unit ζ of norm 1 in the quadratic order IK = IQ[
√
D] and its conjugate
ζ1, respectively.

Finally, we deal with the case D = 0. In this case, B2 = 4AC, so B = 2B0, and
B2
0 = AC. Since gcd(A, B, C) = 1, and A > 0, it follows that gcd(A, C) = 1, and
then that A = A
2
0 and C = C2
0 hold with some positive integers A0 and C0. Hence,
B0 = ±A0C0. When B0 = A0C0, it is clear that the left hand side of equation (3)
is positive whenever 1 ≤ k < k + 2 ≤ n − 1. Thus, B0 = −A0C0, and therefore
B = −2A0C0. Equation (6) becomes

A
2
0x
2 − 2A0C0xy + C2
0 y2 = A
2
0x + C2
0 y,

which can be rewritten as

(A0x − C0y)
2 = A
2
0x + C2
0 y = A0(A0x − C0y) + C0(A0 + C0)y.

Setting t := A0x − C0y, we get that

C0(A0 + C0)y = t2 − A0t,

leading to
 y = t(t − A0)
C0(A0 + C0) ,

and since A0x = C0y + t, we get that

x = t(t + C0)
A0(A0 + C0) ,

which lead to formulae (4) via the fact that x = k + 2, and y = n − k. Note that
since x, t, and y are integers, it follows that t is in certain arithmetical progressions
modulo A0C0(A0 + C0), and from the fact that x ≥ 3 and y ≥ 3, it follows that
either t > G1 := G1(A0, C0), or t < G2 := G1(A0, C0), where G1 and G2 are two
constants which depend on A0 and C0 and which can be easily computed by solving
the coresponding quadratic inequalities.

This completes the proof of the Theorem.

58 F. Luca, L. Szalay

3. Examples

Example 1. The equation

(9) (
n
k
) − ( n
k + 1

) − 2( n
k + 2

) = 0

is a particular case of equation (3) for A = 1, B = −1 and C = −2. Since
B = A + C, all solutions of equation (9) satisfy

(k + 2) − 2(n − k) = 0,

which is equivalent to 2n − 3k = 2. The integer solutions of the above equation are
given by n = 1 + 3t and k = 2t with some integer t, and since n and k must be
positive, we must have t > 1. Conversely, one veriﬁes easily that

(
3t + 1
2t
 ) − (
3t + 1
2t + 1
) − 2(
3t + 1
2t + 2

) = 0

holds for all positive integers t.

Example 2. The equation

(10) ( n
k + 2
) − 2( n
k + 1
) + (
n
k
) = 0

has A = C = 1 and B = 2, therefore D = 0. Moreover, A0 = C0 = 1, so all
solutions (n, k) of the above diophantine equation (10) have

k + 2 = t(t + 1)
2 and n − k = t(t − 1)
2 ,

which gives
 k = t2 + t − 4
2 and n = t2 − 2.

Since n > k > 0, it follows that either t ≥ 3, or t ≤ −3. Conversely, one may check
that if t is any integer which is ≤ −3, or ≥ 3, then

( t2 − 2
t2+t−4
2
 ) − 2( t2 − 2
t2+t−2
2
 ) + (
t2 − 2
t2+t
2
 ) = 0.

Linear diophantine equations with three consecutive binomial coeﬃcients 59

Example 3. The equation

(11) ( n
k + 2
) = ( n
k + 1
) + (
n
k
)

reduces to equation (3) for A = 1, B = 1, and C = −1. In this case, D =
B2 − 4AC = 5, E = 4A
2C(A − B + C) = 4, X = (B2 − 4AC)(n − k) − A(B − 2C) =
5(n − k) − 3, and Y = 2A(k + 2) + B(n − k) − A = 2(k + 2) + (n − k) − 1. Since
X 2 − 5Y 2 = 4, it follows that X = Lm and Y = Fm hold with some even positive
integer m, where (Lℓ)ℓ≥0 is the Lucas sequence given by L0 = 2, L1 = 1, and
Lℓ+2 = Lℓ+1 + Lℓ for all ℓ ≥ 0, and (Fℓ)ℓ≥0 is the Fibonacci sequence. We now get
that n − k = (X + 3)/5 = (Lm + 3)/5, and that k + 2 = (Y − (n − k) + 1)/2 =
(5Fm − Lm + 2)/10. Hence, k = (5Fm − Lm − 18)/10, and n = (5Fm + Lm − 12)/10.
Since n and k are integers, we need that 5|Lm + 3, and that 10|5Fm − Lm + 2.
Thus, 5|Lm + 3 and 2|Fm + Lm. The second relation is always fulﬁlled, while the
ﬁrst one is fulﬁlled precisely if m ≡ 0 (mod 4). Thus, n = (5F4t + L4t − 12)/10,
and k = (5F4t − L4t − 18)/10. Since k > 0, we also need that 5F4t > L4t + 18,
which forces t ≥ 2. One can now easily verify that

( 5F4t+L4t−12
10
5F4t−L4t+2
10
 ) = ( 5F4t+L4t−12
10
5F4t−L4t−8
10
 ) + ( 5F4t+L4t−12
10
5F4t−L4t−18
10
 )

holds for all integers t ≥ 2. Note also that since

( n
k + 1

) + (
n
k
) = (
n + 1
k + 1
)
,

it follows that the diophantine equation (11) reduces to the diophantine equation
(11), which in turn is a consequence of our Theorem.

Remark. We remark that at instance (iii) of our Theorem, it could be possible
that the Pell equation (5) has integer solutions (X, Y ), and yet none such that the
additional congruence X ≡ −A(B − 2C) (mod B2 − 4AC) (necessary in order for
n − k to be an integer) is satisﬁed.

References

[1] Goetgheluck, P., Inﬁnite families of solutions of the equation (
n
k) = 2(
a
b)
,
Math. Comp. 67 (1998), 1727–1733.
[2] Luca, F. Consecutive binomial coeﬃcients in Pythagorian triples, The Fi-
bonacci Quart. 40 No. 2 (2002), 76–78.
[3] Singmaster, D., Repeated binomial coeﬃcients and Fibonacci numbers, The
Fibonaci Quart. 13 (1975), 295–298.

60 F. Luca, L. Szalay

[4] Stroeker, R., and de Weger, B. M. M., Elliptic binomial diophantine
equations, Math. Comp. 68 (1999), 1257–1281.
[5] Szalay, L., A note on binomial coeﬃcients and equations of Pythagorean
type, Acta Acad. Paed. Agriensis, Sect. Math. 30 (2003), 173–177.

Florian Luca
Instituto de Matemáticas
Universidad Nacional Autonoma de México
C.P. 58180, Morelia, Michoacán, México
E-mail: ﬂuca@matmor.unam.mx

László Szalay
Institute of Mathematics and Statistics
University of West Hungary
H-9400, Sopron, Bajcsy-Zs. út 4, Hungary
E-mail: laszalay@ktk.nyme.hu
