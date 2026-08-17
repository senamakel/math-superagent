<!-- source: https://www.ams.org/journals/mcom/1998-67-224/S0025-5718-98-01002-3/S0025-5718-98-01002-3.pdf | converted from PDF -->

MATHEMATICS OF COMPUTATION
Volume 67, Number 224, October 1998, Pages 1727–1733
S 0025-5718(98)01002-3
 INFINITE FAMILIES
OF SOLUTIONS OF THE EQUATION (
n
k =2(
a
b

P. GOETGHELUCK

Abstract. We give explicit formulas providing two new inﬁnite families of
couples of binomial coeﬃcients whose ratio is 2.

1. Introduction

For every positive integer r we have (2r
r  =2(
2r−1
r−1 ,so (n, k, a, b)=
(2r, r, 2r − 1,r − 1) (r =1, 2, 3,... ) is a family of solutions of the equation

n
k
 =2
a
b

,(1)

where n, k, a, b are unknown integers (we can assume, without loss of generality,
that k  n/2and b  a/2).
Are there any other solutions or family of solutions of equation (1)? Partial
answers to this question can be found in [1], [4], [9] and [11].
It should be noted that a simple application of Siegel’s theorem [7, Th. 22,
p. 278], implies that for any ﬁxed k  2and b  2 with k + b> 4, there are only
ﬁnitely many solutions n, a to equation (1).
D. Singmaster [10] found an inﬁnite family of solutions of the equation (
n
k = (
a
b

in terms of Fibonacci numbers, and more recently B. M. M. de Weger [12] gave
some complementary results, in particular on rational solutions of (n
3 = (
a
4.
In the present note the search for solutions of (1) is made using the same method
as Singmaster in [10]:
1) A computer search is made, producing a list of solutions.
2) Computer solutions are examined. Some of them are proved to belong to
inﬁnite families by solving Pell’s equations.
Singmaster performed his computer search for solutions of (
n
k = (a
b with the
exact value of binomial coeﬃcients. So he was limited by the size (2
48) of integers
implemented on the computer. In the present work the computations involving bi-
nomial coeﬃcients use only the factorization of the number instead of its numerical
representation:

if 
n
k
 =2α1 3α25α3 ... (there are no primes p> n in the factorization),

then 
n
k
 is represented by the ﬁnite sequence (α1,α2,α3,... ).

Received by the editor May 29, 1996 and, in revised form, October 7, 1996.
1991 Mathematics Subject Classication. Primary 11B65, 11Y50, 11B37.

c⃝1998 American Mathematical Society

1727

1728 P. GOETGHELUCK

Using this process, computer searches were made in the following domains, where
binomial coeﬃcients can be very big:
 n  100,a  10000,
 n  1000,a < n + 1000,
 for particular values of k and b.
In the next section we give the main results: examining ﬁrst a list of computer
solutions of (1), we ﬁnd three obvious inﬁnite families of solutions, and we are led
to solve Pell’s equations providing two nonobvious inﬁnite families of solutions. In
Section 3, we exhibit another inﬁnite family of solutions, which is easily deduced
from the results of Section 2. Section 4 is devoted to explaining the process of
factorization of binomial coeﬃcients. In Section 5 we present and discuss some
ﬁnite families of solutions.
Let us note that for any given integer λ the equation (
n
k = λ
(a
b can be investi-
gated by the same method.

2. Infinite families of solutions

In this section a list of computer solutions of equation (1) is examined. Some of
them clearly belong to obvious inﬁnite families of solutions. Others are solutions
of (n
2 =2(
a
2 and (
n−1
k+1 =2(
n
k. Solving completely these two equations produces
two new nontrivial inﬁnite families of solutions.

2.1. Obvious solutions. The computer search gave many numerical solutions,
such as

2
1

 =2
1
0


, 4
2

 =2
3
1


, 
6
3

 =2
5
2


, 
8
4

 =2
7
3


,...

4
1

 =2
2
1


, 6
3

 =2
10
1
 
, 
8
2

 =2
14
1
 
, 
8
3

 =2
28
1
 
,...

2
1

 =2
2
0


, 5
2

 =2
5
1


, 
8
3

 =2
8
2


, 
11
4
  =2
11
3
 
,...

belonging to the three obvious inﬁnite families of solutions described by the follow-
ing formulas: 
2r
r
  =2
2r − 1
r − 1
  (r =1, 2,... ),

n
k
 =2r =2
r
1

 (r =1, 2,... ),

3r − 1
r
  =2
3r − 1
r − 1
  (r =1, 2,... ).

2.2. Inﬁnite family of solutions of (
n
2 =2(
a
2. By computer search we have
found the following three numerical solutions:

21
2
  =2
15
2
 
, 
120
2
  =2
85
2
 
, 
697
2
  =2
493
2
 
.

Thus, we are led to wonder if the equation (
n
2 =2(
a
2 has any other solution.
We put a = n − c (0 <c <n). The equation (
n
2 =2(n−c
2  is equivalent to
n2 − n(4c +1) + 2(c2 + c) = 0, giving n =(4c +1 + p
8c2 +1)/2(since n>c).

INFINITE FAMILIES OF SOLUTIONS OF THE EQUATION (n
k =2
(a
b 1729

Thus n is an integer if and only if 8c2 + 1 is a square, and we must solve the
Pell’s equation
 x
2 − 8c2 =1.(2)

The least positive integers satisfying (2) are (x, c)= (3, 1), and then (see [8, Th.
4.4, p. 118]) all positive solutions (xi,ci) of (2) are given by

xi + cip
8= (3 + p
8)
i (i =1, 2, 3,... )

or equivalently

x1 =3,c1 =1,xi+1 =3xi +8ci,ci+1 = xi +3ci (i =1, 2, 3 ... ).

By a straightforward calculation, the following induction formulas provide all solu-
tions (ni,ai) of the equation (
n
2 =2(
a
2:

(n1,a1)= (4, 3), (n2,a2)= (21, 15),

(ni+2,ai+2)= 6(ni+1,ai+1) − (ni,ai) − (2, 2) (i =1, 2, 3,... ).

The computer search found the ﬁrst four solutions (4, 3), (21, 15), (120, 85),
(697, 493); the next are (4060, 2871), (23661, 16731),... .

2.3. Inﬁnite family of solutions of (
n−1
k+1 =2(n
k. The computer search also
gave the following two numerical solutions:

43
12

 =2
44
11


, 614
165

 =2
615
164


,

leading to the study of the equation (
n−1
k+1 =2(
n
k.
This equation is equivalent to n2 − n(4k +3) + (k2 + k) = 0, whose solution
satisfying n> k is n =(4k +3+ p
12k2 +20k +9)/2.
Thus n is an integer if and only if 12k2 +20k + 9 is a square, and we are led to
solve
 12k2 +20k +9 = x
2.

The positive solution of the last equation is k =(−5+ p
3x2 − 2)/6, and k is an
integer if and only if
 3x
2 − 2= y2,y  5(mod 6).(3)

Since (2, 1) and (1, 1) are the least positive solutions of the equations z2 − 3t
2 =1
and z2−3t2 = −2, respectively, an inﬁnite family of solutions (zi,ti)of z2−3t2 = −2
(see [6, Th. 8.8, p. 148]) is given by

zi + tip
3= (1 + p
3)(2 + p
3)
i (i =0, 1, 2,... )

or equivalently
 (z0,t0)= (1, 1), (z1,t1)= (5, 3),

(zi+2,ti+2)= 4(zi+1,ti+1) − (zi,ti)(i =0, 1, 2,... ).

These induction formulas show that zi  (−1)
i (mod 6). Then an inﬁnite family of
solutions of (3) is (yi,xi)= (z2i−1,t2i−1)(i =1, 2, 3,... ), which can be described
by
 (y1,x1)= (5, 3), (y2,x2)= (71, 41),

(yi+2,xi+2) = 14(yi+1,xi+1) − (yi,xi)(i =1, 2, 3,... ).

1730 P. GOETGHELUCK

The corresponding solutions (ni,ki)of (
n−1
k+1 =2(
n
k satisfy ki =(yi − 5)/6and
ni =(4ki +3+ xi)/2, and then are given by

(n1,k1)= (3, 0), (n2,k2)= (44, 11),

(ni+2,ki+2) = 14(ni+1,ki+1) − (ni,ki)+(2, 10) (i =1, 2, 3,... ).

The computer search found (n1,k1)=(3, 0), (n2,k2)=(44, 11), and (n3,k3)=
(615, 164). The next two solutions are (8568, 2295) and (119339, 31976).

3. Another infinite family of solutions

3.1. Equivalent solutions. If for some n, a and k we have (
n
k =2(
a
k,then
multiplying both sides by k!(n−k)!
a!(n−a)! yields
 n
n − a
 =2
n − k
n − a

.

We say that corresponding solutions (n, k, a, k)and (n, n − a, n − k, n − a) are
equivalent.

3.2. Application. We have found the following three numerical solutions
21
6
  =2
19
6
 
, 
120
35
  =2
118
35
 
, 
697
204

 =2
695
204


,

which are clearly equivalent to the solutions

21
2
  =2
15
2
 
, 
120
2
  =2
85
2
 , 
697
2
  =2
493
2
 

of subsection 2.2.
More generally, if (n, k, a, b)=(n, 2,a, 2) is a solution of (
n
k =2(
a
b,then
(n, n − a, n − 2,n − a) is another solution of this equation. So the inﬁnite family of
solutions found in subsection 2.2 provides a new inﬁnite family (ni,ui,ni − 2,ui)of
equivalent solutions given by the following induction formulas:

(n1,u1)= (4, 1), (n2,u2)= (21, 6),

(ni+2,ui+2)= 6(ni+1,ui+1) − (ni,ui) − (2, 0) (i =1, 2, 3,... ).

The computer search found the ﬁrst four solutions (4, 1), (21, 6), (120, 35), (697, 204);
the next are (4060, 1189), (23661, 6930),... .

4. Expansion of a binomial coefficient into primes

We denote by Ep(n, k) the power of the prime p in the expansion of (
n
k into
primes. The basic result is the following:

Theorem (Kummer, 1852 [5, p. 115]). For any prime p and any integers n and k
(0  k  n), Ep(n, k) is equal to the number of borrow (s) in the subtraction n − k
in base p.

Some immediate consequences make Kummer’s theorem easy to apply:
 If p>n,then Ep(n, k)= 0.
 If 2k  n and n − k< p  n,then Ep(n, k)= 1.
 If 2k  n and n
2 <p  n − k,then Ep(n, k)= 0.
 If 2k  n and p
n< p  n
2 ,then Ep(n, k)=0 or 1, and Ep(n, k)=1 if and
only if n mod p< k mod p.

INFINITE FAMILIES OF SOLUTIONS OF THE EQUATION (n
k =2
(a
b 1731

Figure 1. The set of all (p, k) such that p is prime and divides (
400
k 

To get the expansion of (n
k into primes we need a table of primes up to n. Then,
under the assumption n  4and 2k  n, the computation is made according to the
following scheme:

if 2 <p  p
n, Ep(n, k) = number of borrow(s)

in the subtraction n − k in base p;

if p
n<p  n/2,Ep(n, k)= 0 if k mod p  n mod p and

Ep(n, k)= 1 if k mod p> n mod p;

if n/2 <p  n − k, Ep(n, k)= 0;

if n − k< p  n, Ep(n, k)= 1;

if n< p, Ep(n, k)= 0.

A detailed algorithm for computing the factorization of (n
k into primes can be
found in [2].
Using a PC with a 66mhz 486 CPU, the computation of the factorization of(n
k spends less than 3  10−4 second if n  1000 and less than 2  10−3 second if
n  10000.

Application. 1) Obviously, in the computer search, instead of comparing values,
we compare the factorizations of (n
k and 2(
a
b.
2) Suppose that for given n and k, we search for a solution of (1) with a  n.
If there are primes in the interval (n − k, n], let p be the greatest of them. By the
second consequence of Kummer’s theorem, p divides (
n
k, and therefore, p divides(a
b.Then p  a  n. If we now search for a solution of (1) with a> n,an
analogous proof shows that for any prime q satisfying n<q  a we must have
b  a − q.
Then the computer search is restricted to very few binomial coeﬃcients.
Figure 1 gives a geometric illustration of these results. For a given n (here
n = 400), the ﬁgure is drawn by plotting every (p, k) such that p is prime and
divides (
n
k. (The structure of the pattern, which is the same for any n, is explained
in [3]). So, to get the list of primes p dividing (
n
k we need only to draw a horizontal
line at ordinate k and collect abscissas where it meets vertical segments.
These remarks explain why we ﬁnd only very few solutions to equation (1).

1732 P. GOETGHELUCK

5. Finite families of solutions

5.1. A list of solutions. Besides the members of inﬁnite families of solutions of
Sections 2 and 3, the numerical computation also found that:

a) 
36
3
  =2
85
2
 
, 
10
4
  =2
15
2
 
, 
11
5
  =2
22
2
 
,

25
5
  =2
231
2
 
, 
30
5
  =2
378
2
 
, 
34
5
  =2
528
2
 
,

38
7
  =2
3553
2
 
, 
18
9
  =2
221
2
 ;

b) 
85
34

 =2
83
35


;

c) 
45
2
  =2
12
4
 
, 
273
2
  =2
18
6
 
.

These solutions are listed here according to the following classiﬁcation:
Type a. Solutions (
n
k =2(
a
2.
Type b. Solutions (
n
k =2(
n−2
k+1.
Type c. Solutions (
n
2 =2(
6b
2b.
Special programs have been written to exhibit other results of these three types.
None of them gave any new solution.

5.2. Remarks.

5.2.1. We have no explanation of the fact that there are so many solutions of
type a. However we remark that for these solutions (
a
2 and n have “many” prime
factors.

5.2.2. If we take u = n − k − 1and v = k +1, then (
n
k =2(
n−2
k+1 is equivalent to
the equation 2u3 − vu2 − (2v2 − v +2)u − (v3 − v2)= 0 or 2u3 − vu2 − 2v2u − v3 =
2u − uv − v2. The fact that the polynomial 2x
3 − x
2 − 2x − 1 has no rational roots
implies that there are only ﬁnitely many solutions of type b (this is an application
of the following result [7, p. 278] established by Schinzel: let f and g be two
polynomials with integer coeﬃcients satisfying deg(f ) > 2, deg(g) < deg(f )and f
irreducible in the rational ﬁeld; then the equation f (u, v)= g(u, v) has only a ﬁnite
number of integer solutions).
The computation shows that (85
34
 =2(
83
35 is the only solution of type b for
n  106.

5.2.3. Since (
n
2 =2(
a
2 gave many solutions, we have investigated the equation(n
k =2(
a
k (k> 2). This equation has only a ﬁnite number (possibly zero) of
solutions, and, as seen in subsection 3.1, is equivalent to the equation
 n
n − a
 =2
n − k
n − a

.

Then, when seeking solutions, we can assume that n − a<k.
A computer search shows that there are no solutions in the domains
 3  k  40,n  106,n − a<k;
 n  30000,n − a  k.

INFINITE FAMILIES OF SOLUTIONS OF THE EQUATION (n
k =2
(a
b 1733

References

1. A. D. Barry, L'equation diophantienne x(x +1) = ky(y + 1), Enseign. Math. (2) 25 (1979),
23–31. MR 81b:10006
2. P. Goetgheluck, Computing binomial coecients, Amer. Math. Monthly 94 (1987), 360–365.
3. , On prime divisors of binomial coecients,Math. Comp., 51 (1988), 325–329. MR
89f:11033
4. C. G. Khatri and A. M. Vaidya, On integers which are ratios of two triangular numbers,J.
Indian Math. Soc. (N.S.) 35 (1971), 205–215. MR 46:7157
5. E. E. Kummer, Uber die Erganzumgssatze zu den allgemeinen Reciprocit¨at gesetzen,J. Reine
Angew. Math. 44 (1852), 93–164.
6. W. J. Le Veque, Topics in Number Theory, Vol. 1, Addison-Wesley, Reading, MA, 1956. MR
18:283d
7. L. J. Mordell, Diophantine Equations, Academic Press, London, 1969. MR 40:2600
8. C. D. Olds, Continued Fractions, Random House, New York, 1963. MR 26:3672
9. T. N. Shorey, On the ratio of values of a polynomial, Proc. Indian Acad. Sci. (Math. Sci.) 93
(1984), 109–116. MR 87c:11037
10. D. Singmaster, Repeated binomial coecients and Fibonacci numbers, Fibonacci Quarterly
13 (1975), 295–298. MR 54:224
11. S. Thouvenot, Resolution en nombres entiers de l'equation diophantienne n(n +1) =
2n0(n0 + 1), Enseign. Math. (2) 16 (1970), 203–217. MR 45:3319
12. B. M. M. de Weger, Equal binomial coecients: Some elementary considerations,J. Number
Theory, 63 (1997), 373–386. MR 98b:11027

Universit´e de Paris-Sud, Math´ematiques, Bat 425, 91405 Orsay Cedex, France
E-mail address: goetghe@iut-orsay.fr
