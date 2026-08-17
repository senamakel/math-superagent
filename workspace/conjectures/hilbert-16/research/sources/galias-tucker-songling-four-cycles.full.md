<!-- source: http://www.zet.agh.edu.pl/~galias/ps/amc2022.pdf | converted from PDF -->

Applied Mathematics and Computation 415 (2022) 126691

Contents lists available at ScienceDirect

Applied  Mathematics  and  Computation

journal homepage: www.elsevier.com/locate/amc

The  Songling  system  has  exactly  four  limit  cycles

Zbigniew Galias
a , ∗, Warwick Tucker
b

a AGH University of Science and Technology, Department of Electrical Engineering, Poland
b Monash University, School of Mathematics, Australia

a r t i c l e  i n f o

Article history:
Received 6 May 2021
Revised 22 September 2021
Accepted 27 September 2021
Available online 14 October 2021

Keywords:
Hilbert 16th problem
Planar polynomial vector ﬁelds
Limit cycle
Interval arithmetic
 a b s t r a c t

Determining how many limit cycles a planar polynomial system of differential equations
can have is a remarkably hard problem. One of the main diﬃculties is that the limit cycles
can reside within areas of vastly different scales. This makes numerical explorations very
hard to perform, requiring high precision computations, where the necessary precision is
not known in advance. Using rigorous computations, we can dynamically determine the re-
quired precision, and localize all limit cycles of a given system. We prove that the Songling
system of planar, quadratic polynomial differential equations has exactly four limit cycles.
Furthermore, we give precise bounds for the positions of these limit cycles using rigorous
computational methods based on interval arithmetic. The techniques presented here are
applicable to the much wider class of real-analytic planar differential equations.

©2021 The Authors. Published by Elsevier Inc.
This is an open access article under the CC BY license
( http://creativecommons.org/licenses/by/4.0/ )

1. Introduction

In 1900, at the International Congress of Mathematics held in Paris, David Hilbert presented ten open problems in math-
ematics, and later published a more comprehensive list of 23 problems [1] aimed to challenge the mathematical community.
Throughout the 20th century, these problems have received great attention, and still do. Today, most of the Hilbert problems
have been resolved (two of them were deemed to be unresolvable), but a few ones still remain unsolved: one of these is
Hilbert’s 16th problem.
Hilbert’s 16th problem has two distinct parts: one in real algebraic geometry, and one in dynamical systems. We will
address the latter which asks for H(n ) –the maximal number of limit cycles (isolated periodic orbits) the family of two-
dimensional polynomial vector ﬁelds of degree n can display. This problem has been highlighted in Steven Smale’s list of
challenging problems for the 21st century [2] (it appears as number 13 there), and is phrased roughly as follows:
Consider the differential equation in R 2 :

(⋆ )
{ ˙ x = P n (x, y ) ,
˙ y = Q n (x, y ) .

where P n and Q n are polynomials of degree at most n . Is there a bound H(n ) on the number of limit cycles the system ( ⋆ ) can
have, that only depends on the degree n ?

∗ Corresponding author.
E-mail addresses: galias@agh.edu.pl (Z. Galias), warwick.tucker@monash.edu (W. Tucker).

https://doi.org/10.1016/j.amc.2021.126691
0 096-30 03/© 2021 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license
( http://creativecommons.org/licenses/by/4.0/ )

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

Note that the bound H(n ) should be uniform, that is, it should not depend on the particular polynomial vector ﬁeld,
only on its degree n . Hilbert’s 16 problem has a remarkable history, and ﬁnding upper bounds for H(n ) in the general case
appears to be extremely hard. Indeed, very little progress has been made since Hilbert’s seminal talk. As of today, this
question is not resolved even in the simplest, quadratic, case ( n = 2 ). What is known, is that any given single polynomial
vector ﬁeld can have only a ﬁnite number of limit cycles; this was (independently) proved in [3] and [4] . Partial results
for the quadratic case, and a general introduction to the bifurcation theory of planar polynomial vector ﬁelds can be found
in [5] . See also [6] for an overview of the problem. In terms of rigorous numerical studies of limit cycles of planar vector
ﬁelds, an early paper is [7] . It uses a rotated vector ﬁeld to form an annulus containing a given (approximate) limit cycle.
The existence of a true limit cycle follows by verifying that the original vector ﬁeld is transverse to the boundary of the
annulus—this can be achieved by local (rigorous) computations, rather than by integrating the system. Note that the method
presented in [7] cannot be used to prove the uniquness of a limit cycle in a speciﬁed region.
Even  ﬁnding  realistic  lower  bounds  for  H(n )  appears  to  be  very  hard;  for  some  of  the  best  known  lower  bounds,
see [8,9] ( n = 2 ),  [10] ( n = 3 ), and [11] ( n ≥ 4 ).
In this paper, we will focus on the Songling system; the three-parameter family of quadratic planar vector ﬁelds discussed
in [8] . The system is deﬁned by

˙ x = λx − y − 10 x
2 + ( 5 + δ) xy + y
2 ,
˙ y = x + x
2 + ( −25 + 8 ε − 9 δ) xy ,  (1)

where δ = −10 −13 , ε = −10 −52 , and λ = −10 −200 . In [8] , it is proved that this system has at least four limit cycles. Normal
form theory is applied in [12] to prove the uniqueness of periodic orbits in a neighborhood of the singular point (0,0).
The main goal of this work is to conﬁrm that the system (1) supports exactly four limit cycles and to give precise bounds
for positions of initial points of these limit cycles. Additionally, we would like to show that rigorous computational methods
based on interval arithmetic [13] can be useful in studies related to the 16th Hilbert problem [4,6,14,15] .

Theorem 1. The Songling system (1) has exactly four limit cycles.

Proof. From [12] it follows that we only have to prove that no limit cycles of (1) intersect the line segment (x, y ) ∈ { 0 } ×
[0 . 004 , 0 . 04] . This is achieved by combining Lemma 8 with the enclosure of the largest limit cycle, given in Lemma 2 .  □

Computations reported in this work are carried out using the CAPD library [16] . The MPFR library [17] is used for the
multiple-precision support. Computation times are reported for a single core 3.5 GHz processor.
Following the convention in the literature on interval arithmetic, we denote intervals by bold letters. For example the
closed interval with the endpoints x l ≤ x r is denoted by x = [ x l , x r ] . For the sake of brevity, we use a short notation to deﬁne
intervals. For example 9 . 80749 8
6 denotes the interval [9.807496,9.807498].

2. Preliminaries

The system (1) has two equilibria (0,0) and (0,1). Let us consider the line  = { (x, y ) : x = 0 } containing both equilibria.
For (x, y ) ∈  we have

˙ x = −y + y
2 ,
˙ y = 0 .  (2)

From (2) it follows that within  the derivative  ˙ x is negative for y ∈ I = (0 , 1) and positive for y ̸∈ [0 , 1] . It is known (by
index theory) that each limit cycle has to surround a singular point. It follows that each periodic orbit of (1) has to intersect
the interval (0 , I) ⊂ , where (0 , I) denotes a two-dimensional interval vector, with an equivalent notation { 0 } × I.
Let  us  consider  the  return  map  P : I ↦→ I deﬁned  as  follows.  For  y ∈ I the  image  P (y )  is  deﬁned  by  (0 , P (y )) =
φ(τ (0 , y ) , (0 , y )) , where φ(t, (x, y )) is a trajectory of (1) starting at (x, y ) and τ (x, y ) is the smallest positive number t
such that φ(t, (x, y )) ∈ (0 , I) . If the trajectory φ(t, (0 , y )) does not return to (0 , I) then P is not deﬁned on y .

3. The existence of limit cycles

In this section we show that there exist at least four ﬁxed points of P , and we provide very tight enclosures of their
positions.

3.1. Non-rigorous computations

First, let us study the dynamics of P  using non-rigorous computations. During these computations a non-rigorous Tay-
lor  integration  method  with  the  order  100  and  the  absolute  tolerance  10 −300  is  used.  We  select  points  y k = 10 −k/ 3  for
k = 1 , 2 , . . . , 300 , evaluate P (y k ) and compute the difference  f (y k ) = y k − P (y k ) . The results are plotted in Fig. 1 in the log-
arithmic scale. One can see that  f changes the sign four times in the interval y ∈ [10 −100 , 10 −1 / 3 ] . The sign changes are
observed in the intervals [4 . 64 · 10 −75 , 10 −74 ] , [2 . 15 · 10 −21 , 4 . 65 · 10 −21 ] , [4 . 64 · 10 −8 , 10 −7 ] , [2 . 15 · 10 −2 , 4 . 64 · 10 −2 ] . The ﬁrst
three sign changes are continuous and the jumps seen in the picture are caused by computing  f (y ) = y − P (y ) only at dis-
crete values and using the logarithmic scale.
 2

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

Fig. 1.  Plot of the difference f (y ) = y − P(y ) for y ∈ [10
−100 , 10
−1 / 3 ] in the logarithmic scale. Note that f (y ) changes sign four times.

In the interval [2 . 15 · 10 −2 , 4 . 64 · 10 −2 ] the return map is discontinuous. This interval contains a point y ≈ 0 . 03689 whose
trajectory escapes to inﬁnity. However, the map  f changes sign within a smaller interval [4 · 10 −2 , 4 . 64 · 10 −2 ] where  f is
continuous. Therefore, one may expect that  f (y ) has four zeros in the interval y ∈ [10 −100 , 10 −1 / 3 ] which means that P  has
four ﬁxed points in this interval. The results presented in Fig. 1 provide approximate positions of the ﬁxed points which
may be used as starting points for the Newton method to obtain better approximations.

3.2. Topological approach

The existence of a ﬁxed point can be proved using the following topological lemma.

Lemma 1. Let gbe a continuous map deﬁned on an interval x . If either g(x ) ⊂ x or x ⊂ g(x ) , then ghas a ﬁxed point in x .

In order to carry out the proof of existence of a ﬁxed point of P in y = [ y l , y r ] , one has to ﬁnd enclosures of P (y l ) , P (y r ) ,
and show that certain inequalities regarding these enclosures and the endpoints of y are satisﬁed. Additionally, one has to
prove that P  is well deﬁned on [ y l , y r ] . This can be done by ﬁnding an enclosure of P ([ y l , y r ]) . All these computations can
be carried out using interval arithmetic tools for the rigorous integration of nonlinear vector ﬁelds.
The existence of four ﬁxed points of P is formulated in the following lemma.

Lemma 2. Each of the intervals
[ y 1 l , y 1 r ] = 0 . 0426896038820 85
75 ,
[ y 2 l , y 2 r ] = 6 . 6 6 6 6 60148 2
1 · 10 −8 ,
[ y 3 l , y 3 r ] = 2 . 24780594 8
7 · 10 −21 , and
[ y 4 l , y 4 r ] = 7 . 07106781186547524 5
4 · 10 −75

contains a ﬁxed point of P .

Proof. The following inequalities are veriﬁed:
P (y 1 l ) − y 1 l < −5 . 06 · 10 −15 , P (y 1 r ) − y 1 r > 4 . 93 · 10 −15 ,
P (y 2 l ) − y 2 l > 2 . 58 · 10 −57 , P (y 2 r ) − y 2 r < −2 . 32 · 10 −57 ,
P (y 3 l ) − y 3 l < −5 . 05 · 10 −123 , P (y 3 r ) − y 3 r > 1 . 29 · 10 −123 ,
P (y 4 l ) − y 4 l > 5 . 03 · 10 −295 , and P (y 4 r ) − y 4 r < −6 . 23 · 10 −293 .
For each i = 1 , 2 , 3 , 4 an enclosure of P ([ y il , y ir ]) is found which proves that P  is well deﬁned on [ y il , y ir ] . The assertion
follows.  □

The computations are carried out using the CAPD library. Multiple-precision interval computations with the precision of
up to 1024 bits are used. The total computation time per ﬁxed point varies from 4 s to 14 s. We illustrate the associated
limit cycles in Fig. 2 .

3.3. The interval Newton method approach

In  this  section,  we  present results  on  the  existence  and  uniqueness of  ﬁxed  points of  P  obtained using  the  interval
Newton operator.
 3

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

Fig. 2.  Polar plot of the four limit cycles of Lemma 2 . The radius is in logarithmic scale. The two equilibria are plotted as red dots. Note that three of the
four limit cycles surround the equilibrium at the origin. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to the
web version of this article.)

The interval Newton operator for the (continuously differentiable) map  f : R ↦→ R and the interval y is deﬁned as

N(y ) = y − f (y ) / f ′ (y ) ,  (3)

where y ∈ y . The most important property of the interval Newton operation states that if N(y ) is enclosed in the interior of y
then the interval y contains exactly one zero of f . To prove the existence of ﬁxed points of P one applies the interval Newton
operator to the map  f (y ) = y − P (y ) and veriﬁes that the condition N(y ) ⊂ int (y ) holds. In this case the interval Newton
operator has the form N(y ) = y − (y − P (y )) / (1 − P ′ (y )) . Let us note that in this approach one needs rigorous enclosures of
both P (y ) and P ′ (y ) . Based on an enclosure of P ′ (y ) one may state what is the stability type of the ﬁxed point. If | P ′ (y ) | < 1
( | P ′ (y ) | > 1 ) then the ﬁxed point is stable (unstable). Once the existence of a ﬁxed point is proved one may iterate the
interval Newton operator to obtain very accurate enclosures for the position of this ﬁxed point.
The following lemma presents results on stability types and bounds for positions of four ﬁxed points of P .

Lemma 3. The interval
y 1 = 0 . 042689603882080 0619842959753055429655870 0142980749 8
6
contains a single (stable) ﬁxed point of P . P ′ (y 1 ) ⊂ 9 . 11 9
8 · 10 −5 .
The interval
y 2 = 6 . 6 6 6 6 60148152650573950 698517996479316281685290427336417127406 91
88 · 10 −8  contains a single (unstable) ﬁxed
point of P .
P ′ (y 2 ) ⊂ 1 . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 049 2
1 .
The interval
y 3 = 2 . 2478059477961305860583886189574201301744379417437915330332524455975299877707946920093780
3
1 · 10
−21

contains a single (stable) ﬁxed point of P .
P ’ (y 3 ) ⊂ 0 . 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
9936 6
5
The interval
y 4 = 7 . 07106781186547524 40084 4362104 84 9039284 8359376 8847403658833986 8995366239157720186091861933830487
4530341735932808282429248647985062424748296 62807287186790 612435
6
4 · 10
−75  contains  a  single  (unstable)  ﬁxed  point
of P .
P ’ (y 4 ) ⊂ 1 . 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 062 9
8 .

One can see that for ﬁxed points in y 2 , 3 , 4  the derivative of P  is very close to one. As a consequence a very accurate
integration method has to be used. For the numerical integration the rigorous Taylor integration method with the order 100
is used. During the proof the computations are carried out using multiple-precision arithmetic with up to 2048 bits. The
computation time for a single ﬁxed point varies from 45 s to 40 min.

4

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

4. The uniqueness of limit cycles

In [12] , it is shown that there are exactly four ﬁxed points of P outside the segment [0.004,0.04]. The existence of exactly
3 ﬁxed points of P  in the segment (0,0.004) is proved using the normal form theory. The existence of a single ﬁxed point
in the segment (0.04,1) follows from the fact that the line 1 + x − 25 y = 0 which intersects the y axis at the point (0,0.04)
is transversal to the vector ﬁeld and the property of the Songling system that it has at most one limit cycle around one of
the equilibria (for more details see [12] ).
In order to prove that the Songling system has exactly four limit cycles it remains to show that P  has no ﬁxed points
in the segment [0.004,0.04]. In the following, using interval arithmetic tools we show that P  has a single ﬁxed point in the
segment [0.001,1). From Lemma 3 we know that this ﬁxed point is not in [0.004,0.04].
During the computer assisted proof we will use the following technical lemmas.

Lemma 4. If  ¯y < P ( ¯y ) then there are no ﬁxed points of P in the segment [ ¯y , P ( ¯y )] . If  ¯y > P ( ¯y ) then there are no ﬁxed points of P
in the segment [ P ( ¯y ) , ¯y ] .

Proof. Let us consider the case  ¯y < P ( ¯y ) . Let us assume that P (y ) = y for y ∈ [ ¯y , P ( ¯y )] . It follows that y ̸ = ¯y and trajectories
φ(t, (0 , y )) and φ(t, (0 , ¯y )) intersect for t ∈ [0 , τ (0 , y )] , which contradicts the uniqueness of solutions of (1) .  □

A similar result can be formulated for the inverse of P .

Lemma 5. If  ¯y < P −1 ( ¯y ) then there are no ﬁxed points of P  in the segment [ ¯y , P −1 ( ¯y )] . If  ¯y > P −1 ( ¯y ) then there are no ﬁxed
points of P in the segment [ P −1 ( ¯y ) , ¯y ] .

Using Lemma 4 one may construct a sequence of points y 0 < y 1 < y 2 < . . . < y n such that the segment [ y 0 , y n ] does not
contain ﬁxed points of P  or a sequence of points y 0 > y 1 > y 2 > . . . > y n  such that the segment [ y n , y 0 ] does not contain
ﬁxed points of P . This is achieved by selecting a point y 0 ∈ (0 , 1) and computing rigorous bounds for its images under P .
To illustrate this procedure let us assume that P (y 0 ) > y 0 . In the k th step of the procedure using rigorous computations we
obtain an enclosure [ y k +1 ,l , y k +1 ,r ] of P (y k ) and we select y k +1 = y k +1 ,l . After n steps we obtain the point y n . It follows from
Lemma 4 that the interval [ y 0 , y n ] does not contain ﬁxed points of P . For the case P (y 0 ) < y 0 we select y k +1 = y k +1 ,r . After
n steps we obtain the interval [ y n , y 0 ] with no ﬁxed points of P . A similar approach may be used to construct intervals not
containing ﬁxed points using Lemma 5 . We will refer to the approach to exclude the existence of ﬁxed points of P based on
Lemmas 4 and 5 as the iteration based method .
Let  us  note  that  using  Lemmas  4  and  5  one  can  exclude  the  existence  of  ﬁxed  points  of  P  also  in  in-
tervals  containing  points  where  P  is  not  deﬁned.  For  the  Songling  system  one  can  show  that  the  trajectories
φ(t, (0 , 0 . 03689093)) and φ(t, (0 , 0 . 03689096)) intersect the line  at y < 0 and y > 1 , respectively. It follows that the
interval [0 . 036 89093 , 0 . 036 89096] contains a point y ∗ such that the trajectory φ(t, (0 , y ∗)) escapes to inﬁnity ( P  is not de-
ﬁned at y ∗). On the other hand, computing the trajectory starting at (0,0.364) one may show that P (0 . 0364) > 0 . 3766 . From
Lemma 4 it follows that there are no ﬁxed points of P in [0 . 0364 , 0 . 3766] ⊃ [0 . 036 89093 , 0 . 036 89096] ∋ y ∗.
It will be shown that the iteration based method is not eﬃcient for small y . An alternative approach which will be called
the derivative based method is based on the evaluation of P ′ . In this approach we will use the following lemma.

Lemma 6. Let us assume that 1 ̸∈ P ′ (y ) where  y = [ y l , y r ] ⊂ (0 , 1) . If (y l − P (y l ))(y r − P (y r )) > 0 then P (y ) ̸ = y for y ∈ y . If
(y l − P (y l ))(y r − P (y r )) < 0 then y contains a single ﬁxed point of P .

Proof. From the assumption 1 ̸∈ P ′ (y ) it follows that the function  f (y ) = y − P (y ) is strictly monotonic in y . If  f (y l ) = y l −
P (y l ) and  f (y r ) = y r − P (y r ) are of the same sign then  f has no zeros in y , which means that P  has no ﬁxed points in this
interval. If f (y l ) and f (y r ) are of opposite signs then from the monotonicity of f it follows that  f has a single zero in y and
hence that P has a single ﬁxed point in y .  □

To prove that P  has no ﬁxed points in the interval y = [ y l , y r ] two conditions have to be veriﬁed. The ﬁrst condition
(P (y l ) − y l )(P (y r ) − y r ) > 0 requires evaluation of P  over y l  and y r  and is usually easy to verify. The second condition re-
quires evaluation of the derivative P ′ over the whole interval y and verifying that the result does not contain 1. This can be
done in a single evaluation of P ′ only for small intervals. For larger intervals one may split the interval y into several smaller
intervals and verify the condition P ′ (y ) ̸ = 1 separately for each of them.
For the proof that the interval [0.001,1) contains a single ﬁxed point of P  we use the combination of the iteration based
method, the derivative based method and the Lyapunov function method. First, using the Lyapunov function method, we
show that there are no ﬁxed points in the segment [0.98,1). More speciﬁcally, we show that P −1 is increasing in the segment
[0.98,1).

Lemma 7. P −1 (y ) > y for y ∈ [0 . 98 , 1) .

Proof. The change of variables z = y − 1 shifts the equilibrium (0,1) to the origin. In these variables the Songling system has
the form:

˙ x = cx + z − 10 x
2 + axz + z
2 ,
˙ z = −dx + x
2 + bxz ,
 5

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

where a = 5 + δ, b = −25 + 8 ε − 9 δ, c = 5 + δ + λ, d = 24 − 8 ε + 9 δ. Let us deﬁne the Lyapunov function

V ( x, z ) = 0 . 5 d ( ( d + 1 ) x + cz )
2
+ 0 . 5
(
c
2 + ( d + 1 )
2 )
z
2 .

The Lyapunov function is nonnegative and vanishes only at the origin. The derivative of V  with respect to t is

d V
d t  = cd (d + 1)(x
2 + z
2 ) + d(d + 1)(c − 10(d + 1)) x
3 + cd (d + 1) z
3

+((b + d) (d + 1)
2
+ (bc
2 + acd )(d +1)) xz
2 + (d(d + 1)( bc + (a + c
2 − 10 cd )(d + 1)) + (d + 1)
2 ) x
2 z.

Let us assume that x 2 + z 2 = r 2 . The ﬁrst term is equal to cd(d + 1) r 2 . The absolute value of the remaining terms can be
bounded by er 3 , where e = 1 . 482 · 10 5 . It follows that if r < cd(d + 1) /e ≈ 0 . 02026 then  d V
d t  is positive and the Lyapunov
function V (x, z) is increasing along trajectories.
Let us come back to the Songling system. It can be veriﬁed that P −1 (0 . 98) > 0 . 995 and that during the evaluation of
P −1 (0 . 98) the trajectory does not leave the circle centered at (0,1) with the radius 0.02026. It follows that V (x, y − 1) de-
creases during the evaluation of P −1 (y ) for each y ∈ [0 . 98 , 1) and hence V (0 , y − 1) > V (0 , P −1 (y ) − 1) , i.e.,

(y − 1)
2 > (P
−1 (y ) − 1)
2 .  (4)

It follows that P −1 (y ) > y for y ∈ [0 . 98 , 1) .  □

Lemma 8. The segment [0 . 027 , 0 . 99] contains a single ﬁxed point of P .

Proof. Applying the iteration based method for the map P  with y 1 = 0 . 98 and n = 4 we obtain y 4 < 0 . 042689603882 . It
follows from Lemma 4 that the interval [0.042689603882,0.99] does not contain ﬁxed points of P .
Applying the iteration based method for the map P  with y 1 = 0 . 027 and n = 351 we obtain y 351 > 0 . 042689603881 . It
follows that the interval [0.027,0.042689603881] does not contain ﬁxed points of P .
It remains to show that the segment 0 . 04268960388 2
1 contains a single ﬁxed point of P . Let us consider the segment
0 . 0426 90
89 . One can show that P (0 . 042689) > 4 . 26896038 and that P (0 . 042690) > 4 . 26896039 . It follows that the segment
0 . 0426 90
89 contains at least one ﬁxed point of P . One can also show that 1 ̸∈ P ′ (0 . 0426 90
89 ) . From Lemma 6 it follows that the
segment 0 . 0426 90
89 contains a single ﬁxed point of P .  □

Let us note that the iteration based method can be used to handle regions very close to y = 1 . For example apply-
ing this procedure for the map P −1  with y 1 = 0 . 99 and n = 10 we obtain y 10 > 0 . 9999999999999999993 . It follows from
Lemma 5 that the interval [0.99,0.9999999999999999993] does not contain ﬁxed points of P .
The iteration based method is not eﬃcient for y < 0 . 027 due to the fact that the distance | y − P (y ) | decreases fast when
y is decreased. For example to carry out the proof for the segment [0.020,0.021] one needs 3210 evaluations of P  and the
computation time is 15 min. For the segment [0.010,0.011] the number of evaluations exceeds 1 . 4 · 10 6 and the computation
time is 65 h.
As it has been mentioned before an alternative approach is based on the evaluation of P ′ (see Lemma 6 and the following
discussion). This method allows to reduce the number of evaluations when compared with the iteration based method. For
example for the segment [0.01,0.011] the number of evaluations is two times smaller. However the computation time is
longer because the evaluation of P ′ takes longer than the evaluation of P .
A better approach is to use Lemma 6 after a change of coordinates. We will use the polar coordinates: x = r cos ϕ, y =
r sin ϕ (compare also [12] ). From r ˙ r = x ˙ x + y ˙ y one obtains

˙ r =  ˙ x cos ϕ +  ˙ y sin ϕ = λr cos
2 ϕ + r
2 cos ϕ
(( 6 + d ) cos ϕ sin ϕ − ( 14 + 9 δ − 8 ε ) sin
2 ϕ − 10 )
)
.

From  ˙ x = ˙ r cos ϕ − r sin ϕ ˙ ϕ and  ˙ y = ˙ r sin ϕ + r cos ϕ ˙ ϕ one obtains

˙ ϕ =  ˙ y cos ϕ − ˙ x sin ϕ = 1 − λ cos ϕ sin ϕ + r ( 6 + δ) cos
3 ϕ + r
(( 8 ε − 9 δ − 14 ) cos
2 ϕ sin ϕ − sin ϕ − ( 5 + δ) cos ϕ
)
.

It follows that the Songling system in the polar coordinates is deﬁned as

˙ r = r
1 ( ϕ ) + r
2 R ( ϕ ) ,
˙ ϕ = 1 −
2 ( ϕ ) + r( ϕ ) ,  (5)

where

1 ( ϕ ) = λcos
2 ϕ ,
2 ( ϕ ) = λ cos ϕ sin ϕ ,  R ( ϕ ) = cos ϕ
(( 6 + d ) cos ϕ sin ϕ −( 14 + 9 δ −8 ε ) sin
2 ϕ −10
)
,
( ϕ ) = ( 8 ε − 9 δ − 14 ) cos
2 ϕ sin ϕ − sin ϕ − ( 5 + δ) cos ϕ + ( 6 + δ) cos
3 ϕ.

Lemma 9. P (y ) > y for y ∈ [0 . 001 , 0 . 027] .

Proof. In the proof we use Lemma 6 . First, it is veriﬁed that P (0 . 027) > 0 . 027 and P (0 . 001) > 0 . 001 . It remains to show
that 1 ̸∈ P ′ ([0 . 001 , 0 . 027]) . The evaluation of P ′ (y ) is carried out in the polar coordinates. From (5) it follows that ϕ grows
as long as

r < 1 − max ϕ
2 (ϕ)
max ϕ | (ϕ) |  .
 6

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

One can see that |
2 (ϕ) | < 0 . 5 λ. Using interval arithmetic tools we show that | (ϕ) | < c = 7 . 1 . Using the bisection method
the interval t ∈ [0 , 2 π ] is divided into 1288 subintervals t i . Enclosures z i of (t i ) are computed and it is veriﬁed that | z i | < c.
It follows that  ˙ ϕ is positive (i.e. ϕ grows) when

r ≤ 0 . 14 < 1 − 0 . 5 λ
c  .

Next, we verify that during the evaluation of P (0 . 027) the trajectory does not leave the circle centered at the origin with
the radius 0.14. It follows that for y ∈ (0 , 0 . 027] the return map P (y ) can be computed by integrating the one-dimensional
vector ﬁeld
d r
d ϕ =  r
1 (ϕ) + r
2 R (ϕ)
1 −
2 (ϕ) + r(ϕ)  (6)

for ϕ ∈ [0 . 5 π , 2 . 5 π ] with the initial condition r(ϕ = 0 . 5 π ) = y .
The bisection method is used to split the interval [0.001,0.027] into 20809 subintervals. For each subinterval the map P
and its derivative are computed by integrating the vector ﬁeld (6) for ϕ ∈ [0 . 5 π , 2 . 5 π ] and it is proved that P ′ (y ) ̸ = 1 for
y ∈ [0 . 001 , 0 . 027] . The total computation time is 40 h. The assertion follows from Lemma 6 .  □

Let us note that the method to evaluate P ′  which is used in the proof of Lemma 9 is much faster than the standard
approach in which the vector ﬁeld (1) is integrated. For example in the case of the interval y = [0 . 010 , 0 . 011] the number
of evaluations needed to prove that 1 ̸∈ P ′ (y ) is 181 and the computation time is 8 min compared to more than 1 . 4 · 10 6

evaluations and 65 h of computations for the standard approach. The most ﬁne splitting of the interval [0.001,0.027] is
necessary  close  to  the  endpoint  0.001.  For  example  the  calculations  involving  the  interval  [0.0 01,0.0 02]  with  the  width
being less than 4% of the total width took 70% of the computation time.
From Lemmas 7, 8 , and 9 it follows that the segment [0.001,1) contains a single ﬁxed points of P .
Additionally, we prove that there are no ﬁxed points of P in a neighborhood of the origin.

Lemma 10. P (y ) < y for y ∈ (0 , 2 · 10
−202 ] .

Proof. The Songling system can be written as:

˙ x = λx − y − 10 x
2 + axy + y
2 ,
˙ y = x + x
2 + bxy ,

where a = 5 + δ, b = −25 + 8 ε − 9 δ. Let us deﬁne the Lyapunov function

V (x, y ) = (1 + 0 . 25 λ
2 ) y
2 + (x − 0 . 5 λy )
2 .

The Lyapunov function is nonnegative and V (x, y ) = 0 only at the origin. The derivative of V  with respect to t is

d V
d t  =  λ
(x
2 + y
2 ) − ( 20 + λ) x
3 − λy
3 +
(2 + 2 b + bλ
2 − aλ
)
xy
2 +
(2 + 2 a + λ
2 − bλ + 10 λ
)
x
2 y.

Let r =
√
x 2 + y 2 . The ﬁrst term is equal to λr 2 (recall that λ is negative). The absolute value of the remaining terms can be
bounded by 40 r 3 . It follows that for r < | λ| / 40 = 2 . 5 · 10 −202 the Lyapunov function V (x, y ) is decreasing along trajectories.
In the next step, we verify that P (2 · 10 −202 ) < 2 · 10 −202 and that during the evaluation of P (2 · 10 −202 ) the trajectory
does not leave the circle centered at the origin with the radius 2 . 5 · 10 −202 . It follows that for y ∈ (0 , 2 · 10
−202 ] the Lya-
punov function V (x, y ) decreases during the evaluation of P (y ) and hence V (0 , y ) > V (0 , P (y )) , i.e. y 2 > P (y ) 2 . The assertion
follows.  □

5. Conclusions

As mentioned in the introduction, this paper has two main goals: (1) to prove that the Songling system has exactly four
limit cycles, and (2) to illustrate the powers (and potential future use) of rigorous computations based on interval arithmetic.
For the problem we are considering here, the rigorous computations show their strength in producing coarse and tight
enclosures of limit cycles, as illustrated in Lemma 2 and Lemma 3 , respectively. The same lemmas also give local unique-
ness results within each enclosure, leading to an exact count of the limit cycles. The weakness of the same computational
techniques lies in proving non -existence of limit cycles. This is a global problem, and as such requires much more computa-
tional effort. Small neighbourhoods of 0 and 1 are handled analytically by Lyapunov function methods, as in Lemma 10 and
Lemma 7 , respectively. But for the remaining sectors, our methods were not practical. As an illustration, Lemma 8 (clear-
ing  the  interval  [2 . 7 · 10 −2 , 9 . 9 · 10 −1 ]  from  ﬁxed  points  of  P )  required  15  min  to  compute,  whereas  Lemma  9  (clearing
[10 −3 , 2 . 7 · 10 −2 ] ) took 40 h.
Although we could (in principle) exhaust the remaining interval [2 · 10 −202 , 10 −3 ] , it would have required an enormous
amount of computing power. Instead, we used the analytical normal form result of [12] , which clears the larger interval
[0 . 0 , 4 · 10 −3 ] from ﬁxed points of P .

Acknowledgements

This work was supported in part by the AGH University of Science and Technology.

7

Z. Galias and W. Tucker  Applied Mathematics and Computation 415 (2022) 126691

References

[1] D. Hilbert , Mathematical problems, Bull. Amer. Math. Soc. 8 (10) (1902) 437–479 .
[2] S. Smale , Mathematical problems for the next century, Math. Intelligencer 20 (20 0 0) .
[3] J. Écalle , Introduction Aux Fonctions Analysables Et Preuve Constructive De La Conjecture De Dulac, Actualités Mathématiques, Hermann, Paris, 1992 .
[4] Y.S. Ilyashenko , Finiteness theorems for limit cycles, Translations of Mathematical Monographs, vol. 94, American Mathematical Society, Providence,
1991 .
[5] R. Roussarie , Bifurcation of planar vector ﬁelds and Hilbert’s sixteenth problem, Progress in Mathematics, vol. 164, Birkhäuser Verlag, Basel, 1998 .
[6] Y.S. Ilyashenko , Centennial history of Hilbert’s 16th problem, Bull. Am. Math. Soc. 39 (2002) 301–355 .
[7] J. Guckenheimer , Phase portraits of planar vector ﬁelds: computer proofs, Exp. Math. 4 (2) (1995) 153–165 .
[8] S. Songling , A concrete example of the existence of four limit cycles for plane quadratic systems, Sci. Sin. 23 (2) (1980) 153–158 .
[9] P. Yu , M. Han , Four limit cycles from perturbing quadratic integrable systems by quadratic polynomials, Int. J. Bifur. Chaos Appl. Sci. Eng. 22 (10) (2012)
1250254,28 .
[10] C. Li , C. Liu , J. Yang , A cubic system with thirteen limit cycles, J. Differ. Equ. 246 (9) (2009) 3609–3619 .
[11] R. Prohens , J. Torregrosa , New lower bounds for the Hilbert numbers using reversible centers, Nonlinearity 32 (1) (2018) 331–355 .
[12] D.A. Filimonov , Normal forms of quadratic vector ﬁelds and the Shi Songling equation, Differ. Equ. 46 (5) (2010) 649–659 .
[13] R. Moore , Methods and Applications of Interval Analysis, SIAM, Philadelphia, 1979 .
[14] C.J. Christopher , N.G. Lloyd , Polynomial systems: a lower bound for the Hilbert numbers, Proc. Math. Phys. Sci. 450 (1938) (1995) 219–224 .
[15] C. Li , C. Liu , J. Yang , A cubic system with thirteen limit cycles, J Differ Equ 246 (9) (2009) 3609–3619 .
[16] T. Kapela , M. Mrozek , D. Wilczak , P. Zgliczy ´nski , CAPD::DynSys: a ﬂexible C++ toolbox for rigorous numerical analysis of dynamical systems, Commun.
Nonlinear Sci. Numer. Simul. (2020) 105578 .
[17] GNU MPFR library, 2021, URL http://www.mpfr.org ,
 8
