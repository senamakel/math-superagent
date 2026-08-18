<!-- source: https://arxiv.org/pdf/2112.08586 | converted from PDF -->

arXiv:2112.08586v1  [math.AG]  16 Dec 2021Removal of 5 Terms from a Degree 21
Polynomial

Curtis Heberle

December 17, 2021

Abstract

In 1683 Tschirnhaus claimed to have developed an algebraic method
to determine the roots of any degree n polynomial. His argument was
ﬂawed, but it spurred a great deal of work by mathematicians includ-
ing Bring, Jerrard, Hamilton, Sylvester, and Hilbert. Many of the
problems they considered can be framed in terms of the geometric
notion of resolvent degree, introduced by Farb and Wolfson. Roughly
speaking, we have RD(n) ≤ n − k if a general degree n polynomial
can be put into an (n − k)-parameter form. In the present note we
discuss a method introduced by Sylvester for solving systems of poly-
nomial equations, and apply it to ﬁnding bounds on resolvent degree.
In particular, we prove the bound RD(21) ≤ 15. This bound has been
independently established by Sutherland using the classical theory of
polarity.

Contents

1 Introduction 2

2 Some Background on Tschirnhaus Transformations 5
2.1 Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Some Results on Tschirnhaus Transformations from 1683 to
Present . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

3 Sylvester’s Obliteration Formula 11

1

4 Resolvent Degree 12
4.1 Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.2 Resolvent Degree of a Dominant Map . . . . . . . . . . . . . . 14
4.3 Resolvent Degree of the Quintic . . . . . . . . . . . . . . . . . 15

5 Linear subspaces of hypersurfaces 18
5.1 Linear subspace of cubic hypersurfaces . . . . . . . . . . . . . 20

6 Removing 5 Terms from a Polynomial 22

1 Introduction

Consider a degree n polynomial p(x) with roots x1, . . . , xn:

p(x) = x
n + a1x
n−1 + . . . + anx + an =
 n∏

i=1(x − xi).

A Tschirnhaus transformation is a polynomial transformation of the roots of
p. That is, given a polynomial

T (x) = bn−1x
n−1 + bn−2x
n−2 + . . . + b1x + b0,

and setting y = T (x)

we can form a new polynomial with roots T (x1), . . . , T (xn):

q(y) = yn + A1yn−1 + . . . + An−1y + An =
 n∏

i=1(y − T (xi)).

Tschirnhaus’s original idea was to transform p to a solvable form – speciﬁ-
cally, to choose T such that q(y) = yn + An – as part of a proposed method
for determining in radicals the roots of p. This method is not successful
because in general it is not possible to determine in radicals the coeﬃcients
of the necessary T . On the other hand, a number of interesting results have
since been proved involving the use of Tschirnhaus transformations to reduce
families of polynomials to certain canonical forms; in particular, the problem
of ﬁnding T such that q has the (n − k)-parameter form

q(y) = yn + Ak+1yn−k−1 + . . . + An−1y + An

2

with A1 = A2 = . . . = Ak = 0 has been widely considered. We provide a
partial review of the historical development of this theory in Section 2.
Recently progress has been made by casting the problem in terms of the
geometric notion of resolvent degree, as introduced by Farb and Wolfson. [7]
We review the precise deﬁnitions in Section 4, but roughly speaking the idea
is as follows. We say a generically ﬁnite dominant map X → Y has essential
dimension at most d if there is a pullback square

X W

Y Z

with dim(Z) ≤ d. We then say X → Y has resolvent degree at most d if
it factors as a composition of maps each of essential dimension at most d.
(This is somewhat stronger than what is required in the precise deﬁnition;
for instance, it is suﬃcient for X → Y to be birationally equivalent to such
a composition.)
In particular, we are interested in the resolvent degree of the root cover
of the family of degree n polynomials. That is, let Pn be the space of monic
degree n polynomials, and ̃Pn the space of pairs (p, λ) of polynomials p ∈ Pn
with a choice of root λ. Then there is a generically ﬁnite dominant map
̃Pn → Pn by “forgetting the root”, and we are interested in bounds on

RD(n) := RD(̃Pn → Pn).

Intuitively, we have RD(n) ≤ d if the roots of any p ∈ Pn can be determined
by solving algebraic functions of at most d variables. For example, for n = 2,
the quadratic formula implies that the root cover ̃P2 → P2 is a pullback of
the map
 P1 → P1z ↦→ z2.

Similarly, the existence of “formulas in radicals” for n = 3 and n = 4 implies
that ̃P3 → P3 and ̃P4 → P4 factor into towers of pullbacks of cyclic self-covers
of P1, so that RD(3) = RD(4) = 1.
Many classical results concerning Tschirnhaus transformations can be
translated into statements about resolvent degree: if any p ∈ Pn can be

3

reduced to an (n − k)-parameter form by means of a Tschirnhaus transfor-
mation T , we have RD(n) ≤ n − k,

provided that T can itself always be determined by solving algebraic func-
tions of at most n−k variables. For example, a result of Bring shows that any
degree 5 polynomial can be put into the one-parameter form y5 + A5y + 1. [4]
This is suﬃcient to imply RD(5) = 1; in Section 4 we treat this example in
detail. The bounds so-obtained are generally not sharp, as the improvements
obtained by Wolfson and Sutherland have demonstrated. [15, 19]
On the other hand, this formulation of the problem implies diﬀerent
constraints on which Tschirnhaus transformations T are permissible than
were generally assumed by classical authors. For example, in considering the
problem of transforming a general degree n polynomial p(x) into an (n − k)-
parameter form by means of a Tschirnhaus transformation T , Sylvester only
considers those transformations whose coeﬃcients can be determined without
solving any equation of degree higher than k. This is much more restrictive
than necessary if one’s goal is to show

RD(n) ≤ n − k.

For example, for k = 6, Sylvester obtains the following:

Proposition 1 (Sylvester). For n ≥ 44, a general polynomial of degree
n can be put into an (n − 6)-parameter form by means of a Tschirnhaus
transformation whose coeﬃcients can be determined without solving any
equation of degree higher than 5.

As a corollary, one obtains the resolvent degree bound RD(n) ≤ n − 6 for
n ≥ 44; on the other hand, ﬁnding the necessary Tschirnhaus transformation
is a resolvent degree RD(5) = 1 problem, since only equations of degree at
most 5 are involved. Sylvester’s was nonetheless the best known bound for
k = 6 prior to Wolfson’s 2020 proof that RD(n) ≤ n − 6 for n ≥ 41. [19]
In Wolfson’s argument, ﬁnding the necessary Tschirnhaus transformation is
shown to be at worst a resolvent degree 35 problem. It has been conjectured
by Wiman and (separately) Chebotarev that RD(n) ≤ 15 for n ≥ 21, though
their proposed arguments contain gaps. [3, 18] Recently, Sutherland has pro-
vided a rigorous proof of this bound using the classical theory of polarity. [15]
In the current note we use ideas from Sylvester to provide an alternative
proof of the RD(n) ≤ n − 6 for n ≥ 21 bound. In particular, we show

4

Theorem (Main Theorem). For n ≥ 21, a general polynomial of degree n
can be put into an (n − 6)-parameter form by means of a Tschirnhaus trans-
formation whose coeﬃcients can be determined without solving an equation
of degree higher than 20.

This implies RD(n) ≤ n − 6 for n ≤ 21.
We now give an outline of the remaining sections of the paper. In Section
2 we give a brief historical overview of the classical theory of Tschirnhaus
transformations and some of the important results therein. In Section 3 we
turn to Sylvester’s work in particular and give a description of his “method
of obliteration”: a technique for ﬁnding solutions of systems of polynomial
equations when the number of variables is large relative to the number of
equations, which lies at the heart of his work on Tschirnhaus transformations.
In Section 4 we discuss resolvent degree and consider the n = 5 case in detail
as an illustration of the relation between resolvent degree and the classical
theory of Tschirnhaus transformations. Section 5 describes a key ingredient
of our main result: the use of the “method of obliteration” to determine
linear subspaces of hypersurfaces. Finally, in Section 6 we give the proof of
our main theorem.

2 Some Background on Tschirnhaus Trans-
formations

2.1 Preliminaries

Let p(x) be a polynomial over a (not necessarily closed) ﬁeld K. Then we
have
 p(x) = x
n + a1x
n−1 + . . . + an−1x + an =
 n∏

i=1(x − xi)

for some coeﬃcients a1, . . . , an ∈ k and roots x1, . . . , xn ∈ K. Fixing some
algebraic extension L of K, a Tschirnhaus transformation is a polynomial
T ∈ L[x], T (x) = b0 + b1x + . . . + bn−1x
n−1

which we apply to the roots of p to obtain a new polynomial

q(y) =
 n∏

i=1(y − T (xi)) = yn + A1yn−1 + . . . + A1y + A0.

5

Note that the coeﬃcients A0, . . . , An are symmetric functions of the trans-
formed roots T (x1), . . . , T (xn), and hence are symmetric in x1, . . . , xn. The
coeﬃcients a0, . . . , an generate the algebra of symmetric polynomials in x1, . . . , xn,
so we can determine the Ai polynomially in terms of a0, . . . , an and b0, . . . , bn−1.
In particular, this implies q ∈ L[y]. The precise constraints on the ﬁeld L
from which the coeﬃcients of T may be taken vary from author to author
but generally one considers towers of extensions of bounded degree. Tschirn-
haus’s original goal was to ﬁnd a formula in radicals for the roots of p. More
precisely, taking L to be the solvable closure of K, his strategy was to de-
termine a Tschirnhaus transformation T ∈ L[x] which transforms p into the
solvable form q(y) = yn+An. If yi is a root of q, we can ﬁnd the corresponding
root(s) of p (i.e., those xj such that T (xj) = yi) as the roots of

GCD(p(x), T (x) − yi).

If there are d roots of p which map to yi, this will be a degree d polynomial.
In particular, if q has distinct roots, then the roots of p can be recovered
rationally from the roots of q. Thus if q is solvable and T has coeﬃcients in
a solvable extension of K, then p will in general be solvable. (And at worst
recovering the roots of p will require the solution of an equation of degree
n − 1.) This strategy fails because it is not generally possible to determine
T solvably such that all the intermediate terms A1, A2, . . . , An−1 of q vanish.
On the other hand, there are weaker versions of Tschirnhaus’s problem which
are tractable. More precisely, we can ask: what conditions on n and L are
suﬃcient for there to exist T in L[x] transforming the degree n polynomial
p ∈ K[x] to a polynomial q ∈ L[y] with A1 = . . . = Ak = 0? That is, we
consider the problem of setting some (rather than all) of the intermediate
coeﬃcients to zero (thus reducing the number of parameters of the family of
polynomials), and we relax the requirement that L necessarily be a solvable
extension.
We now consider in more detail what is necessary to determine T such
that A1 = . . . = Ak = 0. As we remarked above, Ai is a polynomial function
of a1, . . . , an and b0, . . . , bn−1. Treating the bi’s as unknowns to be deter-
mined, we further observe that Ai is homogeneous of degree i in the variables

6

b0, . . . , bn−1. For example,

A1 = −
 n∑

i=1 T (xi)

= −
 n∑

i=1 (bn−1x
n−1
i + bn−2x
n−2
i + . . . + b1xi + b0)

=
 (
−
 n∑

i=1 x
n−1
i
 )
 bn−1 +
 (
−
 n∑

i=1 x
n−2
i
 )
 bn−2 + . . . +
 (
−
 n∑

i=1 xi
)
 b1 − nb0

we can ensure A1 = 0 as long as the coeﬃcients b0, . . . , bn−1 of T are chosen
to satisfy a single homogeneous linear equation. (The coeﬃcients of this
equation are symmetric in the xi, so again can be expressed in terms of
the coeﬃcients a1, . . . , an of p; it is not necessary to know the roots xi.)
More generally, Ai vanishes if and only if the ith symmetric function of
T (x1), . . . , T (xn) vanishes, so to ﬁnd a Tschirnhaus transformation T such
that Ai = 0 in the transformed polynomial we need to solve a degree i
polynomial in b0, . . . , bn−1 whose coeﬃcients are polynomials in a1, . . . , an.
Thus, to determine T we must ﬁnd a point in Pn−1
b on the intersection of
the hypersurfaces V (A1), V (A2), . . . , V (Ak), which are of degree 1, 2, . . . , k,
respectively.

2.2 Some Results on Tschirnhaus Transformations from
1683 to Present

Tschirnhaus, in his 1683 paper introducing these transformations, claimed
to be able to solve any degree n polynomial by removing all intermediate
terms. [17] That is, he claimed one could ﬁnd a transformation T such that

A1 = A2 = . . . = An−1 = 0

and the transformed polynomial has the solvable form

yn + An = 0.

The problem with this strategy is that ﬁnding the necessary T requires the
solution of a system of polynomial equations of degrees 1, 2, . . . , n − 1. In
general this leads to an equation of degree (n − 1)!, so for n > 3 ﬁnding

7

T is a priori more complicated than ﬁnding the roots of the original degree
n polynomial. Tschirnhaus did show explicitly how to ﬁnd T in the n = 3
case, and his proof readily generalizes to removing the ﬁrst two intermediate
terms from any degree n polynomial.
Finding a Tschirnhaus transformation T yielding A1 = A2 = . . . =
Ak = 0 requires solving a system of k equations in n variables, of degree
1, 2, 3, . . . , k. In the worst case this leads to an equation of degree k!, but
when the system is suﬃciently undetermined (i.e., n much larger than k), a
solution can be found without solving any polynomial of degree greater than
k. The ﬁrst result of this kind was given in 1786 by Bring, who showed that
when n ≥ 5, we can ﬁnd T such that A1 = A2 = A3 = 0 without solving any
equation of degree higher than three. [4]
In 1834, Jerrard recovered independently Bring’s result that removal of
three terms from a degree 5 polynomial was possible by means of a Tschirn-
haus transformation. [10] In fact, Jerrard went on to claim that his methods
could yield a reduction of a general quintic to a solvable form. [11] (Jerrard
was aware of, but did not accept, Abel’s 1824 work on the insolvability of
the quintic.)
Shortly thereafter Hamilton was commissioned by the British Associa-
tion for the Advancement of Science to investigate the validity of Jerrard’s
methods, issuing his report in 1837. [8] He showed that Jerrard’s reductions
were in many cases “illusory”. Jerrard allowed Tschirnhaus transformations
of degree potentially as high or higher than the original polynomial p, and
Hamilton demonstrated that in the “illusory” cases the transformation T
found by Jerrard was a multiple of p. In this case the transformed polynomial
is always q(y) = yn (the same as if the “transformation” y = T (x) = 0 were
permitted) for any degree n polynomial p, so there is no hope of determining
the roots of p by studying q. On the other hand, Hamilton showed that
Jerrard’s methods can be a made to work –and the “illusory” cases avoided
– in higher degrees. More precisely, for any ﬁxed k, one can ﬁnd a (nonzero,
degree ≤ n−1) Tschirnhaus transformation T yielding A1 = A2 . . . = Ak = 0
without solving any equation of degree higher than k, provided the degree n
of the original polynomial p is large enough relative to k. In particular, for
k = 4, Hamilton showed n ≥ 11 suﬃces, and for k = 5, n ≥ 47.
In 1886, Sylvester published a geometric explanation of the Hamilton/Jerrard
method, sharpened some of the bounds (ﬁnding, in particular, n ≥ 10 suﬃces
for k = 4, and n ≥ 44 for k = 5). [16] Sylvester claimed that these sharpened
bounds are optimal if no “elevation of degree” is allowed – that is, if no equa-

8

tions of degree higher than k are to be solved. This claim requires careful
interpretation – Sylvester does not consider the possibility of higher degree
polynomials arising but factoring into lower degree terms. This is known to
happen for k = 3: if one attempts to remove three terms from a degree n
polynomial, the system of equations of degree 1, 2, and 3 leads in general to
an equation for degree 6. Sylvester’s method is able to avoid this elevation of
degree only when n ≥ 5. For n = 4, Sylvester’s method is inapplicable, but
Lagrange had shown (in 1771, more than 100 years prior) that the degree 6
equation that arises in this case always factors into a pair of cubics, so that
the necessary Tschirnhaus transformation can in fact be determined without
solving any equation of degree higher than 3. [12]
Further reductions have been achieved, but all loosen or ignore the “el-
evation of degree” restriction in one way or another. Viewing the degree 9
polynomial p(x) = a0x
9 + a1x
8 + . . . + a8x + a9

as a multi-valued “algebraic function” sending (a0, . . . , a9) to the set of roots
of p, Hilbert asked whether this could be written as a composition of algebraic
functions of at most 4 variables. [9] As part of his investigation, Hilbert
sketched a method for ﬁnding a Tschirnhaus transformation such that A1 =
A2 = A3 = A4 = 0 when n ≥ 9. Hilbert’s method requires ﬁnding a line on a
cubic surface. This in turn requires the solution of an equation of degree 27.
However, by putting the equation of the cubic surface into a four-parameter
canonical form (the “pentahedral form”, originally suggested by Sylvester),
Hilbert was able to show that the coeﬃcients of the necessary line were
themselves algebraic functions of four variables, so this was suﬃcient for his
purposes.
In 1945, B. Segre strengthened Hilbert’s result, describing an algorithm
for ﬁnding a Tschirnhaus transformation removing 4 terms from a degree
n ≥ 9 polynomial, without solving any equation of degree higher than 5. [13]
The same result was later proven by Dixmier using diﬀerent methods. [6] Also
building on Hilbert’s work were Wiman, who sketched an alternative proof of
the n = 9 bound for k = 4, and G. Chebotarev, who extended Wiman’s ideas
to sketch a proof that n = 21 for k = 5. [3, 14, 18] In 1975, Brauer showed
that, when n > k!, a degree n polynomial can be written as a composition of
algebraic functions of (n−k −1) variables; in this framing of the problem it is
permissible to simply solve the degree k! to ﬁnd a Tschirnhaus transformation
removing k terms, since this will be an algebraic function of fewer variables

9

than the original degree n polynomial. [1] For k ≥ 7, this n > k! bound
is lower than the corresponding bounds for removal of k terms found by
Sylvester, though it should again be emphasized that this ignores the “no
elevation of degree“ constraint which is explicit in Sylvester, and implicit in
pre-Sylvester work on the problem.
In 2020, Wolfson described a function F (k) such that a degree n poly-
nomial can be put in an (n − k − 1)-parameter form whenever n ≥ F (k),
and which improved signiﬁcantly on Brauer’s bounds. [19] Wolfson frames
the problem in terms of the theory resolvent degree, which allows bounds on
the number of necessary parameters for a family of algebraic functions to be
computed based on the dimensions of certain spaces. For k = 5, Wolfson
shows n ≥ 41, which also improves on Sylvester’s bound of n ≥ 44. To ﬁnd
the Tschirnhaus transformation accomplishing the reduction in this case re-
quires, among other things, ﬁnding a 2-plane inside of a cubic hypersurface
in P6. Informally, since the dimension of the moduli space of cubic hyper-
surfaces in P6 is 35, ﬁnding a 2-plane inside such a hypersurface is at worst
a 35-parameter problem, so is permissible when putting a degree 41 polyno-
mial into 35-parameter form. This approach does not produce the degrees of
the equations which must be solved to ﬁnd the Tschirnhaus transformation
(which may be higher than n, as in Hilbert’s proof that n = 9 suﬃces for
k = 4, where it was necessary to solve a degree 27 equation to ﬁnd a line on
a cubic surface).
Most recently, Sutherland used a combination of ideas from the classi-
cal theory of polarity together with optimizations to the moduli-dimension-
counting method to improve on the F (k) bound for k = 5, . . . , 15 and all
k ≥ 18. [15] In particular, for k = 5, Sutherland shows that n = 21 suﬃces,
giving the ﬁrst rigorous proof of the bound ﬁrst claimed by Chebotarev.
In the current note, we show that the n = 21 result can be recovered from
Sylvester’s method if partial elevation of degree is allowed. More precisely,
one can ﬁnd a Tschirnhaus transformation removing 5 terms (i.e., such that
the coeﬃcients of the transformed polynomial satisfy A1 = A2 = A3 = A4 =
A5 = 0) from a degree n polynomial whenever n ≥ 21, by solving no equation
of degree higher than 20. A key ingredient is that there exists an explicit
algorithm to ﬁnd a 2-plane on a cubic hypersurface in P9, without solving
any equation of degree higher than 5.

10

3 Sylvester’s Obliteration Formula

Though motivated by the problem of ﬁnding Tschirnhaus transformations,
the procedure Sylvester describes in [16] is remarkably general, allowing for
a solution to be found to any suﬃciently underdetermined system, without
elevation of degree. More precisely, given a system of equations S of poly-
nomial equations in N variables of degree at most k, with ni the number of
equations of degree i, Sylvester shows there is a function l(n1, . . . , nk) such
that, if N > l(n1, . . . , nk), then a solution to S can be found without solving
any equation of degree greater than k.
The method is as follows: Pick any f of maximal degree k from the
system S. We can ﬁnd a solution to S by ﬁrst ﬁnding a line L contained in
the solution set of the subsystem S′ = S \{f }, then intersecting this line with
the vanishing locus of f . To ﬁnd L, ﬁrst ﬁnd a solution Q = (q0, . . . , qN ) to
S′. Then to get the required line it suﬃces to ﬁnd a point P = (p0, . . . , pN )
such that P + λQ is a solution to S′ for all λ ∈ C. For any equation g ∈ S′,
then, view g(P + λQ) as a polynomial in λ; if deg(g) = d, the coeﬃcients of
1, λ, . . . , λd−1, λd must vanish identically. In fact the coeﬃcient of λd is just
g(Q), so vanishes since we chose Q to be a solution of S′. The vanishing of
the remaining coeﬃcients imposes polynomial conditions on the p0, . . . , pN of
degrees 1, 2, . . . , d. Ranging over all g ∈ S′, we see that P must be a solution
to a system S′′ with mi equations of degree i, where

mk = nk − 1
mk−1 = nk + nk−1
mk−2 = nk + nk−1 + nk−2
.
m1 = nk + nk−1 + . . . + n1.

Now to ﬁnd this needed point solution, we proceed inductively: again hold
aside some polynomial of highest degree (say h), and ﬁnd a linear solution
to the subsystem S′′ \ {h}, then intersect that line with h, and so on. The
number of equations of maximal degree decreases by 1 with each step, so
eventually we are left with a (possibly very large) system of linear equations;
a line in the solution set to this system can be found provided the number
of variables is (at least) one greater than the number of equations. Then
to backtrack to a linear solution to the original system requires only for
equations of degree ≤ k to be solved one at a time.

11

The core reduction is succinctly summarized by Sylvester’s formula of
obliteration, which we will refer to repeatedly:

Proposition 2 (Sylvester). Given n1, . . . , nk ∈ N, let

[nk, nk−1, . . . , n2, n1]

denote the minimum number of variables such that a linear solution to any
system of equations with exactly ni equations of degree i can be found with-
out elevation of degree. Then

[nk, nk−1, . . . , n2, n1] ≤ 1 + [mk, mk−1, . . . , m2, m1]

where
 mi =
 {∑k
j=i nj i ̸= k
nk − 1 i = k.

Note that applying the obliteration formula nk times yields a system
with no equations of degree k, so all equations of the highest degree can be
removed. This can be repeated until only (a large number of) linear equations
remain, in which case the minimum number of variables needed is easy to
determine. For example, consider the problem of ﬁnding a line on a cubic
hypersurface. We have a system of equations with 1 equation of degree 3,
0 equations of degree 2, and 0 of degree 1. By repeated application of the
obliteration formula,

[1, 0, 0] ≤ 1 + [1, 1] ≤ 2 + [2] = 2 + 3 = 5,

so it is possible to ﬁnd a line solvably (in fact, by solving no equation of
degree greater than 3) on a cubic hypersurface in P5.

4 Resolvent Degree

4.1 Deﬁnitions

Let k be an algebraically closed ﬁeld and let X → Y be a generically ﬁnite
dominant map of k-varieties. Following Buhler and Reichstein [2], we deﬁne

12

the essential dimension of this map, ed(X → Y ), to be the minimal d such
that there exists a pullback square

X W

Y Z

with dim Z ≤ d. The idea of resolvent degree is to extend this notion to
allow towers of pullbacks; essentially, a map is of resolvent degree at most d
if it can be written as a composition of maps each of essential dimension at
most d. More precisely, following Farb and Wolfson [7], the resolvent degree,
RD(X → Y ), is deﬁned to be the minimal d such that there exists a tower

Er → · · · → E1 → E0 = U,

where U is an open subset of Y , Er → U factors through a dominant map
Er → X, and ed(Ei → Ei−1) ≤ d for each i. It follows from these deﬁnitions
that RD(X → Y ) ≤ ed(X → Y ) ≤ dim Y.

It is convenient, in proving results on resolvent degree, to construct towers of
maps of bounded resolvent degree (rather than essential dimension). Lemma
2.7 in Farb and Wolfson [7] shows that this is suﬃcient.
The connection to polynomials and their roots is as follows. Let Pn denote
the space of monic degree n polynomials with coeﬃcients in k and let

̃Pn = {(p, r) ∈ Pn × A1
k | p(r) = 0},

the space of monic polynomials together with a choice of root. We then
deﬁne RD(n) := RD(̃Pn → Pn)

where the map is “forgetting the root”. RD(n) captures the complexity of
the root cover in the sense that if there is a formula in terms of algebraic
functions of at most d variables for ﬁnding the roots of a degree n polynomial
in terms of its coeﬃcients, then RD(n) ≤ d.

13

4.2 Resolvent Degree of a Dominant Map

It is necessary to extend the deﬁnition of resolvent degree to dominant maps
of k-varieties which are not necessarily generically ﬁnite. Although we are
principally interested in RD(n) = ̃Pn → Pn, which is generically ﬁnite, a
number of maps which arise naturally in the study of Tschirnhaus transfor-
mations are not. For example, a key step in Bring’s proof that a general
quintic can be reduced to a one-parameter form involves ﬁnding a line on a
quadric surface in P3. Thus we would like to study

H1
2,3 → H2,3

where H2,3 is the parameter space of quadric surfaces in P3 and H1
2,3 is the
space of such quadrics together with a choice of line on the surface, and the
map is “forgetting the line”. Since any quadric surface contains an inﬁnite
family of lines, this map is not generically ﬁnite. We would like to extend the
notion of resolvent degree so that RD(H1
2,3 → H2,3) captures the complexity
of ﬁnding lines on quadric surfaces in the same way that RD(̃Pn → Pn)
captures the complexity of ﬁnding roots.
This is done in [19] in the following way: given a dominant map π : X →
Y , deﬁne the resolvent degree RD(X → Y ) to be the minimum d for which
there exists a dense collection of subvarieties {Uα ⊂ X} with

π|Uα : Uα → Y

a generically ﬁnite dominant map and RD(Uα → Y ) ≤ d for all α. (Such a
subvariety Uα is called a rational multi-section for π.)
Requiring the collection of multisections to be dense in X is necessary
to ensure that resolvent degree behaves well with respect to composition of
dominant maps: given X → Y and Y → Z dominant, for the composition
X → Z we have RD(X → Z) ≤ max{RD(X → Y ), RD(Y → Z)} by [19,
Lemma 4.10]. Having multi-sections V → Y for X → Y and U → Z for
Y → Z is not generally enough to product a multisection for X → Z (the
range of V → Y could entirely miss U). On the other hand, if V → Y is
surjective, then we do obtain a multi-section of X → Z.
Returning to the example of lines on quadrics, an algorithm for de-
termining a line (or ﬁnite set of lines) on each quadric surface in terms
of algebraic functions of degree d gives a multi-section U → H2,3 with
RD(U → H2,3) ≤ RD(d), but this is somewhat less than what is required to

14

show that RD(H1
2,3 → H2,3) ≤ RD(d). On the other hand, as we shall see
in the next section, determining any one line is suﬃcient to yield a Tschirn-
haus transformation reducing the quintic to a one-parameter form, so that
RD(5) = 1.

4.3 Resolvent Degree of the Quintic

As an illustrative example, we now give a detailed proof that (as observed
in [7]) Bring’s work on Tschirnhaus transformations of quintic polynomials
implies RD(5) = 1. (Recall that by deﬁnition, RD(5) = RD(̃P5 → P5),
where P5 is the parameter space of monic degree 5 polynomials and ̃P5 is the
space of such polynomials together with a choice of root.)
Recall that given a polynomial p(x) = x
5 + a1x
4 + a2x
3 + a3x
2 + a4x + a5
in P5 and a Tschirnhaus transformation of the form T (x) = b0x
4 + b1x
3 +
b2x
2 + b3x + b4, we can set y = T (x) and eliminate x to obtain a polynomial

q(y) = y5 + A1y4 + A2y3 + A3y2 + A4y + A5,

where the coeﬃcient Ai is a degree i homogeneous polynomial in b0, b1, b2, b3, b4,
whose coeﬃcients are integral functions of a0, a1, a2, a3, a4, a5.
Our strategy will be to construct a tower of maps

X5 → X4 → X3 → X2 → X1 → P5

such that the resolvent degree of each map is 1 and there is a dominant
rational map X5 → ̃P5. Informally, in X1 there will be associated to each
quintic polynomial p the equation of a hyperplane determining the set of
Tschirnhaus transformations such that A1 = 0. In X2, we will further have
the information of a quadric Q contained in this hyperplane, corresponding
to A1 = A2 = 0, and the equation of a line l contained in Q. In X3 we
will further have a choice of Tschirnhaus transformation T which lies on l
while also satisfying A3 = 0. Using this information we can construct a map
from X3 to the one-dimensional space of quintic polynomials of the form
z5 + Az + 1, and we will take X4 to be the pullback of the root cover of
this space, so that X4 associates to p a root of the polynomial obtained by
applying T to p. Finally, in constructing X5, we recover the roots of p itself
from the roots of the transformed polynomial. Each step of this process is of
bounded resolvent degree.
 15

More precisely: viewing the bi as homogeneous coordinates on P4, there
is associated to each polynomial p ∈ P5 a hyperplane H ⊂ P4
b consisting
of all Tschirnhaus transformations that send p to a polynomial q(y) with
A1 = 0. Let X1 denote the space of ordered pairs (p, H) with p and H as
just described. Then the map X1 → P5 is birational, hence has resolvent
degree 1.
Next, we consider the set of all Tschirnhaus transformations such that
A1 = 0 and A2 = 0 in the transformed polynomial. The latter is a degree
2 homogeneous polynomial in b0, b1, b2, b3, b4, so to each polynomial p there
is associated a quadric surface Q ⊂ H ∼= P3 whose points are Tschirnhaus
transformations satisfying both conditions. This deﬁnes a map

X1 → H2,3

where H2,3 is the parameter space of quadric surfaces in P3. Letting H1
2,3
denote the space of such surfaces together with a choice of line, we consider
the map H1
2,3 → H2,3.

An algorithm exists for ﬁnding a line on a quadric surface that requires
solving only a single quadratic equation, so there is a rational multi-section
U → H2,3 with RD(U → H2,3) ≤ RD(2) = 1.

(In fact there is a dense collection of such multi-sections, so RD(H1
2,3 →
H2,3) = 1, but this is stronger than we require.)
We deﬁne X2 via the pullback square

X2 X1

U H2,3

so that RD(X2 → X1) ≤ RD(U → H2,3) = 1. Points of X2 are ordered
tuples (p, H, Q, l), where p is a quintic polynomial, H is the space of all
Tschirnhaus transformations that send p to a polynomial with A1 = 0, Q ⊂
H is the quadric surface whose points are Tschirnhaus transformations such
that A1 = 0 and A2 = 0, and l is a line contained in Q.
Finally, to ﬁnd a Tschirnhaus transformation T satisfying A1 = 0, A2 = 0,
and A3 = 0 requires intersecting the cubic hypersurface deﬁned by A3 = 0

16

with the line l. To ﬁnd the three points of intersection requires only the solu-
tion of a cubic equation. Deﬁning X3 to be the space of tuples (p, H, Q, l, T ),
with p, H, Q, l as above and T a Tschirnhaus transformation yielding A1 =
A2 = A3 = 0, the projection map
X3 → X2

has resolvent degree RD(3) = 1.
Now let P ′
5 denote the space of quintic polynomials of the form z5+Az+1.
Given a point (p, H, Q, l, T ) in X3, we can apply the transformation T to p
to obtain a polynomial
 q(y) = y5 + A4y + A5.

Applying a change of variables y = 5√A5z and dividing by A5 yields

z5 + A4 5√A5
A5 z + 1

so this procedure deﬁnes a map X3 → P ′
5. Now, the root cover

̃P ′
5 → P ′
5

has resolvent degree
 RD(̃P ′
5 → P ′
5) ≤ dim (P ′
5) = 1,

so deﬁning X4 via the pullback square

X4 X3

̃P ′
5 P ′
5

we have RD(X4 → X3) = 1. Points of X4 are of the form (p, H, Q, l, T, λ),
where (p, H, Q, l, T ) ∈ X3 and λ is a root of the transformed polynomial
z5 + A4 5√
A5
A5 z +1. Let X5 be the space whose points are tuples (p, H, Q, l, T, µ),
where µ is a root of p. There is a map

X5 → X4

17

deﬁned by
 (p, H, Q, l, T, µ) ↦→ (
p, H, Q, l, T, T (µ)

5√A5
 ) .

On the other hand, given a root λ of the transformed polynomial, we
can ﬁnd the corresponding roots of p by solving the (at worst degree 4)
polynomial equation
 GCD(p(x), 5√A5T (x) − λ) = 0

so RD(X5 → X4) = RD(4) = 1.
In all, we have constructed a tower of maps

X5 → X4 → X3 → X2 → X1 → P5

each of which has resolvent degree 1. Since the root cover ̃P5 → P5 factors
through the projection X5 → ̃P5, (p, H, Q, l, T, µ) ↦→ (p, µ), we have

RD(5) = RD(̃P5 → P5) = 1.

5 Linear subspaces of hypersurfaces

To prove RD(5) = 1 we needed to show one can always ﬁnd a Tschirnhaus
transformation which eliminates the ﬁrst three intermediate terms of a quintic
polynomial. This required ﬁnding a solution of a system of three equations
of degree 1, 2, and 3, respectively. A key geometric fact which made this
tractable was that any quadric surface in P3 contains a line, and that an
equation for such a line can be found by solving a quadratic equation; this
allows the degree 2 equation (which determines the quadric surface) to be
replaced by a degree 1 equation (which determines the line), so that to ﬁnd
a solution of the system requires only the solution of a cubic equation.
Similarly, in Hilbert’s proof that RD(9) = 4, a Tschirnhaus transforma-
tion removing four intermediate terms is required, so a system of equations
of degrees 1, 2, 3, and 4 must be solved. Informally, Hilbert’s idea is to ﬁrst
ﬁnd a 3-plane inside the hypersurface determined by the equation of degree 2
(which is possible as long as the ambient dimension is high enough), then to
ﬁnd a line on the cubic surface determined inside this 3-plane by the equation
of degree 3. If this can be done, all that remains is to intersect the line with
the remaining equation of degree 4 and a solution can be found.
In general, one can consider the problem of ﬁnding a k-plane inside a
degree d hypersurface in PN . We can ask several questions:

18

Q1: In terms of d and k, how large must the ambient dimension N be to
guarantee that any degree d hypersurface contains a k-plane?

Q2: What is the “resolvent degree of ﬁnding the k-plane”? That is, if
Md,N is a moduli space of degree d hypersurfaces in PN and Mk
d,N is
the space of such hypersurfaces together with a choice of k-plane, what
is the resolvent degree of the map

Mk
d,N → Md,N

which forgets the choice of plane?

Q3: When is there a constructive algorithm to determine the k-plane? What
are the degrees of the equations that must be solved? How large must
N be if no equation of degree higher than some given bound is to be
permitted?

As the RD(5) = 1 and RD(9) = 4 examples above illustrate, the answers
to these questions have implications for the problem of ﬁnding Tschirnhaus
transformations, since replacing a hypersurface with a linear subspace of
that hypersurface allows us to replace a degree d equation with one or more
equations of degree 1, reducing the total degree of the system to be solved.
An answer to Q1 is given in Debarre and Manivel [5]: for d > 3, any
degree d hypersurface in PN contains a k-plane if

N ≥
 (d+k
k )

k + 1 + k.

In this case, the map Mk
d,N → Md,N is surjective, and an upper bound on
its resolvent degree is given by the dimension of the codomain:

RD (Mk
d,N → Md,N ) ≤ dim (Md,N ) .

For example, RD (
M1
3,3 → M3,3) ≤ dim (M3,3) = 4,

corresponding to Hilbert’s observation that ﬁnding a line on a cubic surface
requires the solution of at most an algebraic function of four variables.
These dimension-counting arguments do not provide enough information
to address Q3. For this we return to Sylvester’s ideas. First, for the problem
of ﬁnding a line on a degree d hypersurface, repeated application of the

19

obliteration formula suﬃces to compute an ambient dimension N such that
the desired line may be found without solving any equation of degree higher
than d. Sylvester’s methods can be readily adapted to the problem of ﬁnding
a k-plane on a degree d hypersurface without solving any equation of degree
higher than d. Note that, when N is large enough for this to be possible,

RD (Mk
d,N → Md,N ) ≤ RD(d)

giving a bound on resolvent degree which is often sharper than what one ob-
tains from dimension-counting alone (though at the price of requiring a larger
ambient dimension N than that given by Waldron’s theorem), so Sylvester’s
ideas are of interest even if one is only concerned with ﬁnding bounds on
resolvent degree. In the remainder of this section we look at the d = 3 case
in detail.

5.1 Linear subspace of cubic hypersurfaces

Let M3,N be the moduli space of smooth cubic hypersurfaces in PN and
let Mr
3,N be the moduli space of pairs (C, P ) where C is a smooth cubic
hypersurface and P is an r-plane contained in C. We can then consider the
“resolvent degree of ﬁnding an r-plane”, i.e.,

RD(Mr
3,N → M3,N ),

where the map forgets the choice of plane. For example, for the problem of
ﬁnding a line on a cubic surface, we have

RD(M1
3,3 → M3,3) ≤ dim(M3,3) = 4,

so that ﬁnding a line on a cubic surface in P3 requires the solution of alge-
braic equations of no more than 4 variables. Farb and Wolfson [7], using an
argument due to Klein, show this bound can be improved to

RD(M1
3,3 → M3,3.) ≤ 3.

In higher dimensions it is easier to ﬁnd a line. In particular, by Sylvester’s
obliteration method, as discussed in section 3, ﬁnding a line on a cubic surface
in P5 requires the solution of no equation of degree higher than 3, and so is
a resolvent degree 1 problem.
 20

Proposition 3 (Sylvester). Given a cubic hypersurface V in Pn, we can
ﬁnd a line contained in V by solving equations of degree no higher than 3
provided n ≥ 5. Hence

RD(M1
3,5 → M3,5) ≤ RD(3) = 1.

Proof. We wish to ﬁnd a linear solution to a system of equations consisting
of 1 equation of degree 3 and no equations of lower degree. By Sylvester’s
obliteration formula, the ambient dimension required is

[1, 0, 0] ≤ 1 + [1, 1] ≤ 2 + [2] = 2 + 3 = 5.

Sylvester’s method also extends to ﬁnding higher-dimensional linear sub-
spaces of hypersurfaces, when the dimension of the ambient space is large
enough. For example, for cubic hypersurfaces in P9, ﬁnding a 2-plane can
also be done solvably.

Proposition 4 (Sylvester). Given a cubic hypersurface V = V (f ) in Pn, we
can ﬁnd a 2-plane contained in V by solving equations of degree no higher
than 3, provided n ≥ 11. Hence

RD(M2
3,11 → M3,11) ≤ RD(3) = 1.

Proof. Since n ≥ 5, we can ﬁnd a line l contained in V ⊂ Pn solvably. Let q
and r be distinct points of l such that q + λr ∈ V for all λ ∈ V. To ﬁnd a
plane contained in V , we look for a point

p = Pn−2 ⊂ Pn \ l

such that f (p + µq + λr) = 0 for all µ, λ ∈ V. Expanding this as a polynomial
in µ and λ, the coeﬃcients of 1, λ, µ, λµ, λ2, and µ2, must vanish identically.
This gives a system of equations in n − 2 variables with 1 equation of
degree 3, 2 equations of degree 2, and 3 equations of degree 1. To solve it, we
look for a linear solution to the subsystem of equations of degree < 3, then
intersect this line with the remaining degree 3 equation. Using Sylvester’s
formula of obliteration, we have

[2, 3] ≤ 1 + [1, 5] ≤ 2 + [6] = 2 + 7 = 9,

so we can ﬁnd the needed linear solution when n − 2 ≥ 9. Thus we can ﬁnd
a line on a cubic hypersurface in Pn when n ≥ 11.

21

The ambient dimension can be reduced slightly if some elevation of degree
is allowed. From Segre [1945, pg 295, Sec 12], it is possible to determine a
line on the intersection of two given quadrics by solving equations of degree
no higher than 5, provided the ambient dimension is at least 4. Thus to ﬁnd
a linear solution of a system with 2 equations of degree 2, and 3 equations
of degree 1, an ambient dimension of 7 is suﬃcient. Comparing to the last
paragraph in the proof above we have

Proposition 5. Given a cubic hypersurface V = V (f ) in Pn, we can ﬁnd
a 2-plane contained in V by solving equations of degree no higher than 5,
provided n ≥ 9. Hence

RD(M2
3,9 → M3,9) ≤ RD(5) = 1.

6 Removing 5 Terms from a Polynomial

Given a degree n polynomial

x
n + a1x
n−1 + . . . + anx + an

we wish to ﬁnd a Tschirnhaus transformation

T (x) = bn−1x
n−1 + bn−2x
n−2 + . . . + b1x + b0

such that after setting y = T (x) the transformed polynomial

yn + A1yn−1 + . . . + An−1y + An

satisﬁes A1 = A2 = A3 = A4 = A5 = 0. To determine the coeﬃcients
b0, . . . , bn−1 of T then requires the solution of a system of equations with
degrees 1, 2, 3, 4, 5, in Pn−1. In general, to ﬁnd a solution to such a system
requires solving a polynomial of degree 5! = 120, but when n is large enough
this elevation of degree can be partially avoided.
We ﬁrst informally sketch the geometry underlying Wolfson’s bound of
n = 41. The general idea is that by ﬁnding linear subspaces of the hyper-
surfaces corresponding to the polynomials of our system, the total degree of
the system can be reduced. In this case, to ﬁnd the necessary Tschirnhaus
transformation one ﬁrst ﬁnds a 6-plane inside a quadric surface in P13 (this
only requires solving degree 2 equations, so is resolvent degree 1). Then, in-
tersecting the degree 3 equation with the 6-plane yields a cubic hypersurface

22

in P6. If we can then ﬁnd a 2-plane inside this cubic hypersurface, then by
intersecting the degree 4 and 5 equations with this plane, we are left with a
system of total degree 20 to solve. In summary, we have the chain

V4 ∩ V5 ⊂ P2 ⊂ V3 ⊂ P6 ⊂ V2 ⊂ P13 = V1 ⊂ P14.

This gives an algorithm for ﬁnding the desired Tschirnhaus transforma-
tion provided one is able to ﬁnd the necessary 2-plane inside the cubic hy-
persurface in P6. Wolfson uses a dimension count to show that

RD(M2
3,6 → M3,6) ≤ dim(M3,6) = 35,

and so is able to use this Tschirnhaus transformation to show RD(n) ≤ n − 6
whenever n − 6 ≥ 35.
By increasing the ambient dimension in which the the cubic hypersurface
lives, we can use Sylvester’s ideas to ﬁnd a plane inside a cubic hypersurface
in P9 by solving only equations of degree 5 or less. (i.e., in a resolvent degree
1 way). This allows the n = 41 bound for removing 5 terms from a degree n
polynomial to be reduced to n = 21, with simpler irrationalities involved in
ﬁnding the necesary Tschirnhaus transformation.

Theorem (Main Theorem). Let n ≥ 21. Given a degree n polynomial

x
n + a1x
n−1 + . . . + anx + an

we can ﬁnd a Tschirnhaus transformation

T (x) = bn−1x
n−1 + bn−2x
n−2 + . . . + b1x + b0

such that after setting y = T (x) the transformed polynomial

yn + A1yn−1 + . . . + An−1y + An

satisﬁes A1 = A2 = A3 = A4 = A5 = 0. The coeﬃcients b0, . . . bn−1 of T can
be determined by solving equations of degree at most 20.

Proof. The equations A1 = 0, A2 = 0, A3 = 0, A4 = 0, A5 = 0 impose
polynomial conditions of degree 1, 2, 3, 4, and 5, respectively, on the point
(b0, . . . , bn−1) ∈ Pn−1 to be determined. Using the degree 1 equation we can
eliminate one variable. The degree 2 equation then determines a quadric

23

hypersurface in Pn−2. By the classical theory of linear subspaces of quadrics,
we can ﬁnd a P9 contained in this hypersurface provided n − 2 ≥ 19.
Next, we consider the cubic hypersurface determined by this P9 and the
degree 3 equation. By Proposition 5 of the previous section, we can ﬁnd a
P2 contained in this hypersurface by solving equations of degree at worst 5.
Finally, intersecting the remaining equations of degree 4 and 5 determine two
curves in this P2, whose points of intersection are governed by an equation of
degree at most 20. Each such point then satisﬁes all 5 polynomial conditions,
by construction, and so yields a Tschirnhaus transformation of the desired
form.

In the same way that the reduction of the quintic to one-parameter form
can be translated into the language of resolvent degree to yield RD(5) = 1,
this theorem implies RD(n) ≤ n − k for n ≥ 21.

References

[1] Richard Brauer. On the resolvent problem. Annali di Matematica Pura
ed Applicata, 102(1):45–55, 1975.

[2] Joe Buhler and Zinovy Reichstein. On tschirnhaus transformations. In
Topics in Number theory, pages 127–142. Springer, 1999.

[3] Grigorii Nikolaevich Chebotarev. On the problem of resolvents. Uchenye
Zapiski Kazanskogo Universiteta. Seriya Fiziko-Matematicheskie Nauki,
114(2):189–193, 1954.

[4] Alexander Chen, Yang-Hui He, and John McKay. Erland Samuel
Bring’s “transformation of algebraic equations”. arXiv preprint
arXiv:1711.09253, 2017.

[5] Olivier Debarre and Laurent Manivel. Sur la vari et e des espaces lin
eaires contenus dans une intersection compl ete. Math. Ann, 312:549–
574, 1998.

[6] Jacques Dixmier. Histoire du 13e probleme de hilbert. Cahiers du
s´eminaire d’histoire des math´ematiques, 3:85–94, 1993.

[7] Benson Farb and Jesse Wolfson. Resolvent degree, hilbert’s 13th prob-
lem and geometry. L’Enseignement Math´ematique, 65(3):303–376, 2020.

24

[8] Sir William Rowan Hamilton. Inquiry Into the Validity of a Method
Recently Proposed by George B. Jerrard, Esq. for Transforming and Re-
solving Equations of Elevated Degrees Undertaken at the Request of the
Association. Richard and John E. Taylor, 1836.

[9] David Hilbert. ¨Uber die gleichung neunten grades. Mathematische An-
nalen, 97(1):243–250, 1927.

[10] George Birch Jerrard. Mathematical Researches. Longman, Bristol and
London, 1834.

[11] George Birch Jerrard. Xxiv. on certain transformations connected with
the ﬁnite solution of equations of the ﬁfth degree: To the editors of
the philosophical magazine and journal. The London, Edinburgh, and
Dublin Philosophical Magazine and Journal of Science, 7(39):202–203,
1835.

[12] Joseph Lagrange. R´eﬂexions sur la r´esolution alg´ebrique des ´equations.
Nouveaux M´emoires de l’Acad´emie Royale des Sciences et Belles-Lettres
de Berlin, 1771.

[13] Beniamino Segre. The algebraic equations of degrees 5, 9, 157,..., and
the arithmetic upon an algebraic variety. Annals of Mathematics, pages
287–301, 1945.

[14] Alexander J. Sutherland. GN Chebotarev’s “on the problem of resol-
vents”. arXiv preprint arXiv:2107.01006, 2021.

[15] Alexander J Sutherland. Upper bounds on resolvent degree and its
growth rate. arXiv preprint arXiv:2107.08139, 2021.

[16] James Joseph Sylvester. On the so-called tschirnhausen transformation.
1887.

[17] Ehrenfried Walther von Tschirnhaus. Methodus auferendi omnes ter-
minos intermedios ex data aeqvatione (method of eliminating all inter-
mediate terms from a given equation). Acta Eruditorum (1683), pages
204–207.

[18] Anders Wiman. ¨Uber die Anwendung der Tschirnhausentransforma-
tion auf die Reduktion algebraischer Gleichungen. Almquist & Wiksells
Boktr., 1927.
 25

[19] Jesse Wolfson. Tschirnhaus transformations after hilbert.
L’Enseignement Math´ematique, 66(3):489–540, 2021.

26
