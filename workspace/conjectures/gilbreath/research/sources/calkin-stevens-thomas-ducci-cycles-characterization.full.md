<!-- source: https://www.fq.math.ca/Papers1/43-1/paper43-1-7.pdf | converted from PDF -->

A CHARACTERIZATION FOR THE LENGTH OF CYCLES
OF THE N - NUMBER DUCCI GAME

Neil J. Calkin
Department of Mathematical Sciences, Clemson University, Clemson, SC 29634-1907

John G. Stevens
Department of Mathematical Sciences, Montclair State University, Upper Montclair, NJ 07043

Diana M. Thomas
Department of Mathematical Sciences, Montclair State University, Upper Montclair, NJ 07043

(Submitted June 2002-Final Revision September 2002)

1. INTRODUCTION

In the late 1800’s, E. Ducci made a series of observations on iterations of the map D :
Z
n → Z
n, D(x) = (|x1 − x2|, |x2 − x3|, . . . , |xn − x1|) (1)

where x = (x1, x2, . . . , xn) [12].
The dynamics of the Ducci map have been examined for special cases of n in [7, 17, 27].
In addition, many interesting results have been developed for arbitrary n in [1, 2, 8].
One of the main results, which has been proved several times in the literature, states
that for n = 2k for some positive integer k, all initial vectors converge to the zero vector [1,
5]. For the case n ̸= 2k, it has been proved that every initial vector converges to a periodic
cycle [8]. Speciﬁc properties on the lengths of the period have been examined by Ehrlich in
[8]. Ehrlich proved some divisibility conditions relating odd vector length to maximal period
length. Using these relationships, he generated maximal period lengths for odd n. Due to
computing limitations, the lengths were calculated only to n = 165.
This article will develop new insights into the period lengths for any positive integer n by
considering the Ducci game as a map on the vector space Z
n
2 .

2. THE n NUMBER DUCCI AS A MAP ON THE VECTOR SPACE Z
n
2

In order to understand the dynamics of the Ducci map on Z, we need only understand
how the map behaves on binary vectors. This observation is due to an early result that states
every initial vector converges in a ﬁnite number of iterations to a periodic solution of the form
k(x1, x2, . . . , xn) where xi ∈ {0, 1} and k is a positive constant [3].
Ehrlich noticed that the Ducci map on binary vectors can be written as

Dx = ((x1 + x2) mod 2, (x2 + x3) mod 2, . . . , (xn + x1) mod 2),

which is clearly a linear map on Z
n
2 . The matrix representation of D in the standard basis is
given by,
 A =
 








 1 1 0 . . . 0
0 1 1 0 . . . 0
. . .

0 . . . 0 1 1
1 0 . . . 0 1
 








 = I + SL (2)

53

A CHARACTERIZATION FOR THE LENGTH OF CYCLES OF THE N - NUMBER DUCCI GAME

where SL is the left shift map on Z
n
2 . Using the formulation (2), Ehrlich proves that all vectors
converge to the zero vector for n = 2k. One simply expands (I + SL)
2
k using the binomial
theorem. Since all the inner binomial coeﬃcients are multiples of two,
(I + SL)
2
k = I + Sn
L = I + I = 0.

Ehrlich attempted to ﬁnd a formula for the maximal period length for odd n. He was
unable to discover a concise general formula but he was able to prove some valuable divisibility
relationships between vector length and the size of the maximal period. We will reprove his
divisibility conditions by using the algebraic structure of the Ducci map on Z2. The following
deﬁnitions will be used extensively in our analysis.

Deﬁnition 2.1: The minimal annihilating polynomial of a vector v ∈ Z
n
2 is the monic poly-
nomial µv(λ) of least degree such that µv(A)v = 0.
The existence of such a polynomial is guaranteed by the Cayley-Hamilton theorem which
states that the characteristic polynomial of A will annihilate A.

Deﬁnition 2.2: Suppose that µv(0) ̸= 0. Then the order of µv(λ), ord(µv(λ)), is deﬁned to
be the smallest natural number, c, such that µv(λ)|λc − 1. If µv(0) = 0, then µv(λ) can be
written as λk ˜µv(λ), for some positive integer k, where the polynomial, ˜µv(λ), has the property,
˜µv(0) ̸= 0. In this case, the order of µv(λ) is deﬁned to be the order of ˜µv(λ).
A characterization of period lengths by Richman for odd n based on orders of polynomials
was quoted in [16]. To the best of our knowledge, the paper containing the proof of this result
never appeared. We now provide a general characterization for any positive integer n, and any
linear map. This result was initially proved in [25] to study a similar linear map on Z
n
2 .

Theorem 2.1: Let v ∈ Z
n
2 . Let µv(λ) be the minimal annihilating polynomial of v. Assume
that µv(λ) = λk ˜µv(λ) where k ≥ 0 and ˜µv(λ) is a monic polynomial with ˜µv(0) ̸= 0. Then the
kth iterate of v belongs to a periodic cycle with period length c = ord(µv).
Proof: Let A
jv be the ﬁrst iterate that belongs to the periodic cycle. Denote the length
of the cycle by c. Then by deﬁnition of periodicity,

Ac(A
jv) = A
jv
⇒Ac(A
jv) − Ajv = 0

⇒Aj(A
c − I)v = 0.

Therefore, the polynomial p(λ) = λj(λc − 1) has the property that p(A)v = 0. Since the
minimal polynomial divides any other annihilating polynomial, it follows that

µv(λ)|λj(λc − 1). (3)

Using the assumption that µv(λ) = λk ˜µv(λ), yields that λk|λj and ˜µv(λ)|λc − 1.
We will now show that ord( ˜µv(λ)) must equal c. To see this, assume on the contrary that
ord( ˜µv(λ)) = l for some natural number l < c. This means that ˜µv(λ)|λl − 1 which yields,
λk(λl − 1) = µv(λ)q(λ) for some polynomial q. Therefore,

A
k(A
l − I)v = µv(A)q(A)v = q(A)µv(A)v = 0.

It follows that A
l(Akv) = A
kv and so A
kv is in a periodic cycle of length l, giving a contra-
diction since the period of the cycle that v converges to is c. Thus, c = ordµv(λ).

54

A CHARACTERIZATION FOR THE LENGTH OF CYCLES OF THE N - NUMBER DUCCI GAME

Next we will prove that k = j. Since λk|λj, k ≤ j. We will show that k cannot be strictly
less than j. To see this assume on the contrary that k < j. Now ˜µv(λ)|λc − 1 by the deﬁnition
of order. Therefore, µv(λ)|λk(λc − 1) and so

λk(λc − 1) = µv(λ)¯q(λ),

for some polynomial, ¯q(λ). From the deﬁnition of minimal annihilating polynomial,

A
k(A
c − 1)v = ¯q(A)µv(A)v = 0.

Therefore, A
c(A
kv) = A
kv and so A
kv is in the periodic cycle. But A
jv is the ﬁrst iterate on
the cycle. Hence our assumption that k < j is false and k cannot be strictly less than j. This
shows that k must equal j.
Since there always exists a vector whose minimal annihilating polynomial is the minimal
polynomial, the period of the maximal cycle is equal to the order of the minimal polynomial.
Therefore, it will be useful to obtain the exact formulation of the minimal polynomial of A,
µn(λ). We do so by ﬁrst computing the characteristic polynomial of A.
The structure of the matrix A − λI provides some important observations:

A − λI =
 








 1 − λ 1 0 . . . 0
0 1 − λ 1 0 . . . 0
. . .

0 0 . . . 0 1 − λ 1

1 0 . . . 0 1 − λ
 








 (4)

The n−1st minor determinant of A−λI is equal to one. Therefore, the characteristic polynomial
is pn(λ) = (1 − λ)
n + 1.

A result in [13] states that µn(λ) = pn(λ) [qn−1(λ)]−1 where qn−1(λ) is the greatest common
factor of the n − 1 rowed minor determinants of A − λI. Since we already know that one of
the n − 1 minor determinants is equal to one,

µn(λ) = pn(λ) = (1 − λ)n + 1.

Since we are working over a ﬁeld of characteristic 2, combining these observations with Theorem
2.1 yields the following corollary,
Corollary 2.2: Let n be a positive integer. Then the period of the maximal cycle under A is
equal to the order of the minimal polynomial of A,

µn(λ) = (1 + λ)n + 1.

Moreover, for n odd, µn(λ) = λ ˜µv(λ) and so any v that converges to the maximal cycle does
so in at most one iteration.
 55

A CHARACTERIZATION FOR THE LENGTH OF CYCLES OF THE N - NUMBER DUCCI GAME

Deﬁne c1 = 2j − 1 where j is the order of 2 modulo n. If n|2
l + 1, for some l, then let
m = min{l : n|2l + 1} and deﬁne c2 = n(2m − 1). Note that the existence of c1 is always
guaranteed by Euler’s Theorem. Ehrlich proved that c|c1 and c|c2 if c2 exists. We now provide
alternate algebraic proofs of this divisibility condition. The structure of these arguments give
insight into the connection between Ehrlich’s results and the minimal polynomial of A.
Proposition 2.3: Let c be the period length for the maximal cycle and deﬁne c1 = 2
j − 1
where j is the order of 2 modulo n. For odd n, c divides c1.
Proof: Since the roots of the minimal polynomial, µn(λ) are simple, a result from [14]
states that c = ord(µn(λ)) = min{s|zs
i = 1},

where zi is a root of µn(λ). Now if zi is a root of µn(λ) then

(1 + zi)n = 1.

Let xi = 1 + zi. Then x
n
i = 1 and zi = 1 + xi. Therefore, we seek,

min
s (1 + xi)s = 1

where xi is an nth root of unity.
We will show that (1 + xi)c1 = 1 which will prove that c|c1. To see this, observe that

(1 + xi)c1 = (1 + xi)
2j −1

= 1 + xi + . . . + x2
j −1
i

= 1 + x
2j
i
1 + xi .

We know x
2j −1
i = 1, since n|2j − 1. Therefore, x
2
j
i = xi and so

1 + x
2
j
i
1 + xi = 1.

Proposition 2.4: Let n be odd and suppose that n|2l +1, for some l. Let m = min{l : n|2
l +1}
and deﬁne c2 = n(2
m − 1). If c is the length of the maximal cycle, then c|c2.
Proof: Similar to Proposition 2.3, we compute (1 + xi)
c2 ,

(1 + xi)
c2 = [(1 + xi)2
m−1]n

= [1 + xi + . . . + x2
m−1
i ]n

= [ 1 + x
2
m
i
1 + xi
 ]n

56

A CHARACTERIZATION FOR THE LENGTH OF CYCLES OF THE N - NUMBER DUCCI GAME

Since x2
m+1
i = 1, x2
m
i = x−1
i so

[ 1 + x
2
m
i
1 + xi
 ]n = x−n
i
 [ xi + 1
1 + xi
 ]n = 1.

This proves c|c2.
The next lemma relates c2 to c1 when c2 exists.
Proposition 2.5: Let n be odd and suppose that c2 exists. Then c2|c1.
Proof: We will ﬁrst show that j = 2m. Since 2
m ≡ −1 (mod n), 2
2m ≡ 1 (mod n),
which implies that j ≤ 2m. Now, if j < m, then 2m−j ≡ −1 (mod n), contradicting the
minimality of m. Moreover, by deﬁnition, m ̸= j, and if m < j < 2m, then 2j−m ≡ −1
(mod n), again contradicting the minimality of m. Hence j = 2m as claimed.
It follows that, c1 = (2
m + 1)(2m − 1) is divisible by c2.
Ehrlich provided four examples to show that c does not necessarily have to equal c1 or c2,
namely n = 37, 95, 101 and 111. Obviously, the maximal period in these cases was a proper
common divisor of c1 and c2 and is also a multiple of n.
The next section provides data for cycles of the Ducci map up to n = 40, obtained using
Theorem 2.1.
 3. PERIODS OF THE n-NUMBER DUCCI GAME

In addition to cycles with the maximal period c, there can exist cycles with shorter periods
that are proper divisors of c. If g(λ) is a proper divisor of ˜µ(λ), then there exists a vector
with g(λ) as its minimal annihilating polynomial. As Theorem 2.1 states, the vector is in a
cycle with period equal to the order of g(λ). In fact, all possible periods can be obtained by
examining ˜µ and all of its divisors.
For example, for n = 17, ˜µ(λ) = g1(λ)g2(λ) where,

g1(λ) = λ8 + λ7 + λ5 + λ4 + λ3 + λ2 + 1

and g2(λ) = λ8 + λ5 + λ3 + λ2 + 1.

The order of g1 is 85 and the order of g2 is 255. Although the majority of cycles are of length
255, there do exist three cycles of length 85. The algorithm to obtain the complete cyclic
structure (state diagram) for a linear map on Zn
p based on this approach is given in [25].
The output of this procedure applied to the Ducci map for vector lengths up to n = 40
are provided in Table 1. In addition to the information in Table 1, the program also generates
the number of vectors in each cycle, the maximum number of iterations needed to arrive in
the cycle, and the irreducible factors of the minimal polynomial. We note that ﬁxed points
are considered a cycle of length one.
Many interesting questions remain on the Ducci map. For example, is there a way to
predict when c = c1 or c2? If so, is there a method of determining the period for the cases
when c ̸= c1, c2? The even case has been looked at but not as extensively as the odd case. Are
there similar divisibility conditions connected to the minimal polynomial in the even case? We
believe that the algebraic structure may provide some answers to these questions.

57

A CHARACTERIZATION FOR THE LENGTH OF CYCLES OF THE N - NUMBER DUCCI GAME

Vector Length Number of Cycle Lengths Vector Length Number of Cycle Lengths

Cycles of Cycles of

Diﬀerent Lengths Diﬀerent Lengths

n=3 2 1,3 n=22 3 1,341,682

n=4 1 1 n=23 2 1,2047

n=5 2 1,15 n=24 5 1,3,6,12,24

n=6 3 1,3,6 n=25 3 1,15,25575

n=7 2 1,7 n=26 3 1,819,1638

n=8 1 1 n=27 4 1,3,63,13797

n=9 3 1,3,63 n=28 4 1,7,14,28

n=10 3 1,15,30 n=29 2 1,475107

n=11 2 1,341 n=30 7 1,3,5,6,10,15,30

n=12 4 1,3,6,12 n=31 2 1,31

n=13 2 1,819 n=32 1 1

n=14 3 1,7,14 n=33 4 1,3,341,1023

n=15 4 1,3,5,15 n=34 5 1,85,170,255,510

n=16 1 1 n=35 6 1,7,15,105,819,4095

n=17 3 1,85,255 n=36 7 1,3,6,12,63,126,252

n=18 5 1,3,6,63,126 n=37 2 1,3233097

n=19 2 1,9709 n=38 3 1,9709,19418

n=20 4 1,15,30,60 n=39 6 1,3,455,819,1365,4095

n=21 5 1,3,7,21,63 n=40 5 1,15,30,60,120

Table 1. Period lengths under iterations of the Ducci map.

ACKNOWLEDGMENTS

The authors would like to thank Marc Chamberland for generating interest in the problem
and providing us with literature.
 REFERENCES

[1] O. Andriychenko and M. Chamberland. “Iterated Strings and Cellular Automata.” Math-
ematical Intelligencer 22.4 (2000): 33-36.
[2] F. Breuer. “A Note on a Paper by Glaser and Sch¨oﬀ.” Fibonacci Quarterly 36.5 (1998):
463-466.
[3] M. Burmester, R. Forcade and E. Jacobs. “Circles of Numbers.” Glasgow Math. J. 19
(1978): 115-19.
[4] L. Carlitz and R. Scoville. In “Solutions.” SIAM Review 12 (1970): 247-300.
[5] M. Chamberland. “Unbounded Ducci Sequences.” Journal of Diﬀerence Equations , to
appear.
[6] C. Ciamberlini and A. Marengoni. “Su una interessante curiosit.” it `a numerica Peri-
odiche di Matematiche 17 (1937): 25-30.
[7] J. Creely. “The Length of a Three-Number Game.” Fibonacci Quarterly 26 (1988):
141-143.
 58

A CHARACTERIZATION FOR THE LENGTH OF CYCLES OF THE N - NUMBER DUCCI GAME

[8] A. Ehrlich. “Periods in Ducci’s n-Number Game of Diﬀerences.” Fibonacci Quarterly 28
(1990): 302-305.
[9] B. Freedman. “The Four Number Game.” Scripta Math 14 (1948): 35-47.
[10] H. Glaser and G. Sch¨oﬄ. “Ducci-Sequences and Pascal’s Triangle.” Fibonacci Quarterly
33 (1995): 313-324.
[11] J.M. Hammersley. In “Problems.” SIAM Review 11 (1969): 73-74.
[12] R. Honsberger. Ingenuity in Mathematics, Yale University, (1970).
[13] N. Jacobson. Lectures in Abstract Algebra, VII, (1953).
[14] R. Lidl and H. Niederreiter. Finite Fields, Encyclopedia of Mathematics and its Applica-
tions, 20 (1983).
[15] M. Lotan. “A Problem in Diﬀerence Sets.” American Mathematical Monthly 56 (1949):
535-541.
[16] A. Ludington Furno. “Cycles of Diﬀerences of Integers.” Journal of Number Theory 13
(1981): 255-261.
[17] A. Ludington. “Length of the 7-Number Game.” Fibonacci Quarterly 26 (1988): 195-204.
[18] A. Ludington-Young. “Length of the n-Number Game.” Fibonacci Quarterly 28 (1990):
259-265.
[19] A. Ludington-Young. “Ducci-Processes of 5-tuples.” Fibonacci Quarterly 36.5 (1998):
419-434.
[20] A. Ludington-Young. “Even Ducci-Sequences.” Fibonacci Quarterly 37.2 (1999): 145-
153.
[21] K.R. McLean. “Playing Diﬀy With Real Sequences.” Mathematical Gazette 83 (1999):
58-68.
[22] R. Miller. “A Game With n Numbers.” American Mathematical Monthly 85 (1978):
183-185.
[23] F. Pompili. “Evolution of Finite Sequences of Integers . . . .” Mathematical Gazette 80
(1996): 322-332.
[24] I.R. Sprague. Recreation in Mathematics, Dover, (1963).
[25] J.G. Stevens. “On the Construction of State Diagrams for Cellular Automata With Ad-
ditive Rules.” Information Sciences 115 (1999): 43-59.
[26] B. Thwaites. “Two Conjectures or How to Win L1100.” Mathematical Gazette 80 (1996):
35-36.
[27] W. Webb. “The Length of the Four-Number Game.” Fibonacci Quarterly 20 (1982):
33-35.
[28] F.-B. Wong. “Ducci Processes.” Fibonacci Quarterly 20 (1982): 97-105.
[29] P. Zvengrowski. “Iterated Absolute Diﬀerences.” Mathematics Magazine 52.1 (1979):
36-37.

AMS Classiﬁcation Numbers: 11T99, 12E20, 39A11

✠ ✠ ✠

59
