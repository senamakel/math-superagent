<!-- source: https://yorkspace.library.yorku.ca/server/api/core/bitstreams/fc2121d3-1b87-4e03-bbae-5f01fe202378/content | converted from PDF -->

325
⁄
 0022-0396/02 $35.00
© 2002 Elsevier Science
All rights reserved.

Journal of Differential Equations 178, 325–436 (2002)
doi:10.1006/jdeq.2001.4017, available online at http://www.idealibrary.com on

Finite Cyclicity of Graphics with a Nilpotent Singularity
of Saddle or Elliptic Type 1

1 This work was supported by NSERC and FCAR in Canada.

Huaiping Zhu 2

2 E-mail: zhu@math.gatech.edu.

Department of Mathematics and Statistics, McMaster University, Hamilton,
Ontario, Canada, L8S 4K1

and

Christiane Rousseau 3

3 E-mail: rousseac@dms.umontreal.ca.

Department of Mathematics and Statistics, University of Montreal, Montreal,
Quebec, Canada, H3C 3J7

Received December 3, 1999; revised October 10, 2000

In this paper we prove finite cyclicity of several of the most generic graphics
through a nilpotent point of saddle or elliptic type of codimension 3 inside C .

families of planar vector fields. In some cases our results are independent of the
exact codimension of the point and depend only on the fact that the nilpotent point
has multiplicity 3. By blowing up the family of vector fields, we obtain all the limit
periodic sets. We calculate two different types of Dulac maps in the blown-up
family and develop a general method to prove that some regular transition maps
have a nonzero higher derivative at a point. The finite cyclicity theorems are
derived by a generalized derivation–division method introduced by Roussarie.

© 2002 Elsevier Science
 1. INTRODUCTION

A graphic (singular cycle, limit periodic set, polycycle) of a planar vector
field is an invariant set of the vector field involving regular orbits and sin-
gular points. We are interested in the graphics of generic families of vector
fields depending on a small number of parameters and their cyclicity, i.e.,
the maximum number of limit cycles that may appear by perturbation
inside the family. A simpler problem is to prove that the graphics have
finite cyclicity. The question of finding the number of limit cycles which

FIG. 1. Graphics through a nilpotent saddle. (a) convex, (b) concave.

appear by perturbation of a graphic in a generic family and the problem of
finite cyclicity is closely related to the Hilbert–Arnold problem [1, 21]:

Hilbert–Arnold problem. Prove that for any n, the bifurcation number
B(n) is finite, where B(n) is the maximum cyclicity of nontrivial polycycles
occurring in generic n-parameter families.

A graphic of planar vector field can be elementary or nonelementary in
the sense that its singular points are elementary (hyperbolic or semihyper-
bolic, i.e. at least one nonzero eigenvalue) or nonelementary. Some essen-
tial steps have been made toward the understanding of the bifurcation of
elementary graphics through the works of Roussarie [30], Mourtada
[27–29], Ilyashenko and Yakovenko [22], Dumortier et al. [12], Kotova
and Stanzo [24], Dumortier et al. [7], El Morsalani [15], etc.
The graphic with a nilpotent singular point of multiplicity 2 is the
cuspidal loop. Graphics through a point of multiplicity 3 are of two types:

• graphic through a nilpotent saddle (Fig. 1),
• graphic through a nilpotent elliptic point (Fig. 2).

In [14], by analytic and geometric methods based on the blowing up for
the unfoldings, Dumortier et al. studied the simplest case, the bifurcation

FIG. 2. Graphics through a nilpotent elliptic point. (a) Epp graphic, (b) Ehp graphic,
(c) Ehh graphic.

326 ZHU AND ROUSSEAU

diagram of a cuspidal loop of codimension 3. They give a complete answer
for the cyclicity and bifurcation diagram up to a conjecture. From this and
the complexity of the bifurcation diagram in the case of the cuspidal loop,
it seems hopeless without new methods to find a complete solution to solve
the similar question with triple nilpotent points. Fortunately we will show
that the question of proving the finite cyclicity of a graphic is much simpler
and that indeed we can give a complete answer to this question for several
graphics of codimension 3 and 4. This means in particular that we do not
consider the birth of small limit cycles from the singularities but only the
large limit cycles which coalesce with the graphic when the parameters
vanish.
In this paper, we study the finite cyclicity of graphics with a nilpotent
singularity of saddle or elliptic type, i.e., the existence of a bound for the
number of limit cycles which can bifurcate from such graphics. In some of
the finite cyclicity theorems, we will only use the multiplicity of the nilpo-
tent point and not its codimension, the finite cyclicity following from a
global genericity assumption. The precise definition of cyclicity for a limit
periodic set was given by Roussarie [30].

Definition 1.1. A limit periodic set C of a vector field Xm0 inside a
family Xm has finite cyclicity in Xm if there exist N ¥ N and e, d >0 such
that any Xm with |m − m0|< d has at most N limit cycles ci such that
distH(C, ci)< e. The minimum of such N when e and d tend to zero is
called the cyclicity of C in Xm, which we denote by Cycl(C).

Let X be a smooth vector field on R 2. A singular point p (i.e., X(p)=0)
is said to be a triple nilpotent point of saddle or elliptic type if there is a
local chart (x, y): (R 2,p) Q (R 2,0) in which the vector field has the form
(Takens [37])

X=y “
“x
+(e1x 3+dx 4+bxy+ax 2y+ex 3y) “
“y
+O(|(x, y)| 5),

where for the saddle case, e1=1; for the elliptic case e1=−1, b>2 `2.
Denoting the graphic with a nilpotent singularity by (X, p, C),we
are going to study the cyclicity of C by considering a three-parameter
unfolding Xm of X.
To describe the different types of graphics we use a weighted blow-up
(x, y)=(rx¯, r 2y¯) for the singular point. Following the convention of
Kotova and Stanzo [24], we use pp to denote a graphic going out of a
parabolic sector to a parabolic sector, hp to denote a graphic going out of
a hyperbolic sector to a parabolic sector, and hh to denote a graphic going
out of a hyperbolic sector to a hyperbolic sector. Then, a graphic through
an elliptic point can be of three different types (Fig. 3):

FINITE CYCLICITY 327

FIG. 3. Pp, hp, and hh graphics of elliptic type. (a) Epp upper, (b) Epp lower, (c) Ehp
upper, (d) Ehh upper.

• pp graphic: Epp (codimension 3),
• hp graphic: Ehp (this codimension 3 type of graphic was not
mentioned in [24]),
• hh graphic: Ehh (codimension 4).

Each graphic can occur in two versions: upper and lower (see one example
in Fig. 3b). Although the upper and lower graphics may have different
bifurcation diagrams, the proofs of their finite cyclicity are the same.
A graphic through a nilpotent saddle can be of two different types
(Fig. 4): hh graphic convex and Sxhh and hh graphic concave (Sahh).

FIG. 4. Convex and concave graphics of saddle type. (a) Sxhh, (b) Sahh.

328 ZHU AND ROUSSEAU

TABLE I

Main Results Concerning the Finite Cyclicity

Theorem Graphic Conditions Codimension Cyclicity

5.4 Sxhh
convex
 PŒ(0) ] 1
a ] − 1
2 in (2.5)
(b ] 0 in (2.1)) 4 Finite

6.3 Epp
 R (n)(0) ] 0(n \ 2)
a ] 1
2 in (2.5)

(b > 2 `2 in (2.1))
 n+1 n

6.6 Ehp a ] 1
2 in (2.5)

(b > 2 `2 in (2.1)) 3 Finite

6.9 Ehh
 PŒ(0) ] 1
a ] 1
2 and e¯2 ] 0 in (2.5)

(b > 2 `2 and e2 ] 0 in (2.3))
 4 Finite

Due to technical difficulties, we do not consider the concave graphic of
saddle type. For other graphics listed in Figs. 3 and 4, we have proved four
main theorems which we list in Table I.
To prove the finite cyclicity theorems listed above, one basic ingredient is
the blow-up of families developed in [10] and [14]. Around that we set up
a machinery which can be used for other similar graphics. Some of these
tools have been introduced for the study of the cuspidal loop [14]. These
tools include:

1. Normal form for a family with a nilpotent singularity: we develop
a special normal form different from the classical one and allowing:

• use of the special properties of quadratic systems:

— some transitions occur along straight lines,
— convexity of some trajectories,
— knowledge of the center conditions;

• easy application to graphics inside quadratic systems.

2. Blow-up of the family to allow the calculations of the passage
maps near the nilpotent singularity.
3. The list of limit periodic sets appearing in the blown-up family of
vector fields and which must be proved to have finite cyclicity.

FINITE CYCLICITY 329

4. The calculations of the different types of Dulac maps in the
neighborhood of the singular points of the blown-up sphere.
5. The structure theorems on the Dulac maps allow us to prove that
some compositions of a regular transition with two Dulac maps of first
type at opposite points on the blown up sphere behave exactly as an affine
map (Proposition 5.9). This reduces many proofs of finite cyclicity to
proofs identical to the proofs of finite cyclicity for graphics in the plane
with elementary singular points.
6. To derive finite cyclicity property, we consider systems whose
number of solutions bounds the number of fixed points of the return map
in the neighborhood of a limit periodic set under a small perturbation of
the blown-up vector field. We derive bounds for the number of solutions of
these systems by a generalized derivation–division method.
7. We introduce a general method to prove that some regular transi-
tions have a nonzero higher derivative at a given point.

In a second paper [33] we will apply these results to quadratic systems
and the finiteness part of Hilbert’s 16th problem [11].
The paper is organized as follows: In Section 2, we develop a new
general normal form unfolding the nilpotent singularity of saddle or elliptic
type of codimension 3. In Section 3, we make the global blow-up for the
family. In Section 4, we study two types of Dulac maps. We prove the main
finite cyclicity theorems for saddle and elliptic cases respectively in
Sections 5 and 6. Some details have been omitted for parts of the proof
which are identical to existing proofs in the literature, but full details are
written in [38].

2. NORMAL FORMS UNFOLDING THE SINGULARITY

In this section, we will first develop a new normal form unfolding the
codimension 3 nilpotent singularity of saddle or elliptic type different from
the standard unfolding used in [13].
We know by [36] that the germs of C . vector fields at 0 ¥ R 2 whose
1-jet is nilpotent and 2-jet is C .-conjugate to a vector field with a 2-jet
y “
“x+bxy “
“y is C .-conjugate to a vector field with 4-jet

y “
“x
+(e1x 3+dx 4+bxy+ax 2y+ex 3y) “
“x, (2.1)

where e1=0, ± 1 and a, b, c, d ¥ R, b \ 0.

330 ZHU AND ROUSSEAU

The codimension of the point is determined by looking at b and the
quantity
 Q(2.1) :=5e1a − 3bd (2.2)

associated with the 4-jet (2.1).
By [13], the vector field is C .-equivalent to a vector field with a 4-jet

y “
“x
+(e1x 3+bxy+e2x 2y+fx 3y) “
“x, (2.3)

where e1, 2=±1 and e2 is a multiple of Q(2.1).
The topological type falls into one of the following categories (Fig. 5):

(1) The saddle case: e1=1, any e2 and b (a topological saddle).

(2) The focus case: e1=−1 and 0<b<2 `2 (a topological focus).

(3) The elliptic case: e1=−1 and b \ 2 `2 (an elliptic point).

For e2=1 and e2=−1, the saddle points (resp. elliptic points) have the
same topological type.
For e1=1 (resp. e1=−1), the nilpotent singularity is of codimension 3 if
e2 ] 0, b ] 0 (resp. e2 ] 0b ] 2 `2); it is of codimension \ 4 if e2=0,
b=0,or b=2 `2.
We are interested only in the vector fields with a triple nilpotent singu-
larity of saddle or elliptic type with e1=±1 and b> `2 if e1=−1.A
family containing this singularity can be brought to [13]

x˙=y

y˙=e1x 3+l2x+l1+y(l3+bx+e2x 2+x 3h(x, l))+y 2Q(x, y, l), (2.4)

where l=(l1, l2, l3) are the parameters and Q(x, y, l) is C . in (x, y, l)
and of arbitrarily high order in (x, y, l). b is now a variable parameter
depending on l. For l=0, b(0) satisfies the condition described above.

FIG. 5. The different topological types. (a) Saddle case, (b) elliptic case.

FINITE CYCLICITY 331

Remark 2.1. Some of the work done here will also be useful for higher
codimension nilpotent saddle or elliptic singularities in the case e2=0
and/or b=0.

In this normal form (2.4), the principal part (the remaining part on the
blown-up sphere) will be cubic. We develop a new normal form for the
unfolding of the nilpotent singularity of the saddle and elliptic type, so that
the principal part becomes quadratic.

Theorem 2.2. The family (2.4) is C .-equivalent to

X˙ =Y+m2+aX 2

Y˙ =m1+Y(m3+X+e¯2X 2+X 3h1(X, m))+X 4h2(X, m)+Y 2Q(X, Y, m),
(2.5)

where e¯2=−ae1e2, and

• for the saddle case: a(0) ¥ (−1
2,0);
if a(0)=−1
2, the unfolding is of codimension 4 which corresponds to the case
b(0)=0.
• for the elliptic case: a(0) ¥ (0, 1
2);
if a(0)=
1
2, the unfolding is of codimension 4, type 1, which corresponds to the
case b(0)=2 `2 (the two characteristic trajectories coalesce into one).

m=(m1, m2, m3) is the parameter, h1(X, m), h2(X, m)=e¯2a+O(m)+O(X)
and Q(X, Y, m) are C . and Q(X, Y, m) is of arbitrary high order in
(X, Y, m).

Proof. In the family (2.4), we make the transformation

x=m1+X¯

y=m2+Y¯ +a2X¯ 2. (2.6)

To eliminate the terms X¯ , X¯ 2,X¯ 3 in the second equation for the new
system, we need to solve

F(m1,m2,a2, l):=R l2+(b − 2a2)m2+d1(m1,m2)
a2l3+(a2b+3e1)m1+e2m2+d2(m1,m2)
e1+a2b−2a 2
2+d3(m1,m2) S=0. (2.7)

For l=0 and m1=m2=0, by (2.7) we have a equation for a2(0):

2a 2
2(0) − b(0) a2(0) − e1=0. (2.8)

332 ZHU AND ROUSSEAU

Then
 a ±
2 (0)=
1
4 [b(0) ± `b 2(0)+8e1].

We choose a(0)=a −(0). Note that

F(0, 0, a2(0), 0)=0,

det 1 “F(m1,m2,a2, l)
“(m1,m2,a2) :

(0, 0, a2(0), 0)2=
2e1(a 2(0)+e1)(2a 2(0)+e1)
a 2(0) ] 0.

So by the implicit function theorem, we solve F(m1,m2,a2, l)=0 in the
neighborhood of 0 ¥ R 6, and the solution of (2.7) can be written as

a2=a2(0)+O(|l|)

m1=− a2(0) e1
2(a 2
2(0)+e1) [e2l2+e1l3]+O(|l| 2)

m2=a2(0) e1l2+O(|l| 2).

The family has the form

X¯˙ =Y¯ +m2+a2X¯ 2

Y¯˙ =l1+m1l2+m2l3+O(|(m1,m2)| 2)

+Y¯ [l3+bm1+O(|(m1,m2)| 2)+b1(l)X¯ +b2(l)X¯ 2+X¯ 3h11(X¯ , l)]

+X¯ 4h12(X¯ , l)+Y¯ 2Q1(X¯ ,Y¯ , l), (2.9)

where h11(X¯ , l), h12(X¯ , l), and Q1(X¯ ,Y¯ , l) are C .. Also Q1 is of arbitrarily
high order in its variables and

b1(l)=b(0) − 2a2(0)+O(|l|)=− e1
a2(0)
+O(|l|)

b2(l)=e2+O(|l|)

h12(X, l)=e2a2+O(l)+O(X).

Rescaling in (2.9) by (X¯ ,Y¯ )=(X/b1(l), Y/b1(l)), then we get a new
normal form

X˙ =Y+m2+aX 2

Y˙ =m1+Y[m3+X+e¯2X 2+X 3h1(X, m)]+X 4h2(X, m)+Y 2Q(X, Y, m),
(2.10)

FINITE CYCLICITY 333

where
 a=−e1a 2
2+O(l)

e¯2=e2a 2
2+O(l)

h2(X¯ , l)=−e1e2a 4
2+O(l)+O(X¯ ).

Also m=(m1, m2, m3) is the new parameter with

m1= e1
a2(0) l1+O(|l| 2)

m2=−l2+O(|l| 2)

m3=−e1(2a2(0) − e1)
2(a2(0)+e1) [− e2l2+3l3]+O(|l| 2). L

Proposition 2.3. If instead of choosing a −
2 (0) of (2.8) we choose the
other root, we obtain a ¥ (−.,−1
2) (resp. a ¥ (
1
2, .)) for the saddle (resp.
elliptic case). For the saddle case, family (2.5) with a(0) ¥ (−.,−1
2) and
a(0) ¥ (−1
2,0) are C .-equivalent. But for the elliptic case, family (2.2) with
a(0) ¥ (0, 1
2) and a(0) ¥ (
1
2, .) are C .-equivalent except for a(0)=
1
4.

Proof. Let a(0)=a+
2 (0); then a(0) ¥ (−1
2,0). Consider family (2.5).
Under the transformation

X=Xˆ ,Y=Yˆ +(
1
2 −a) Xˆ 2 (2.11)

family (2.5) becomes

Xˆ˙ =m2+Yˆ +
1
2 Xˆ 2

Yˆ˙ =m1 − (1 − 2a) m2Xˆ +(
1
2 −a) m3Xˆ 2+Yˆ (m3+2aXˆ +e2Xˆ 2+Xˆ 3h12)

+Xˆ 4h22+Yˆ 2Q2(Xˆ ,Yˆ , m).
 (2.12)

To eliminate the terms Xˆ ,Xˆ 2 in the second equation of (2.12), there exists a
transformation of the form

Xˆ =X˜ +b1

Yˆ =Y˜ +b2+b3X˜ +b4X˜ 2, (2.13)

334 ZHU AND ROUSSEAU

where

b1= 1−2a
a(4a − 1) (e2m2+am3)+O(|m| 2)

b2=
1−2a
2a +O(|m|)

b3=− 1−2a
a(4a − 1) (e2m2+am3)+O(|m| 2)

b4= 1
2a(4a − 1) [(4a − 1) d1 −2e 2
2+8e2d2) m2+2a(4d2e2) m3]+O(|m| 2)

(2.14)

and by the transformation (2.13) and a rescaling in the variables X˜ and Y˜ ,
family (2.12) becomes

X˜˙ =Y˜ +m˜ 2+aŒX˜ 2

Y˜˙ =m˜ 1+
1
2 gX˜ 2+Y˜ [m˜ 3+X˜ +e˜2X˜ 2+X˜ 3h14(X˜ , m˜ )]

+X˜ 4h24(X˜ , m)+Y˜ 2Q4(X˜ ,Y˜ , m˜ ),
 (2.15)

where
 g=3 1 if a(0)=
1
4
0 if a(0) ] 1
4,

aŒ= 1
4a
+O(|m˜ |) and aŒ(0)= 1
4a(0) ¥1 − .,− 1
22;

also for the new parameter (m˜ 1, m˜ 2, m˜ 3) we have

det 1 “(m˜ 1, m˜ 2, m˜ 3
“(m1, m2, m3)2:

m=0=
4a(0)(1 − a(0))
4a(0) − 1 ] 0. (2.16)

So for the saddle case, family (2.5) with a(0) ¥ (−1
2,0) and a(0) ¥
(−.,−1
2) are C .-equivalent. For the elliptic case, family (2.2) with
a(0) ¥ (0, 1
2) and a(0) ¥ (
1
2, .) is C .-equivalent except for a(0)=
1
4. The
presence of the additional term for a(0)=
1
4 comes from the fact that the
eigenvalues at P3 and P4 are ± 1
2, + 1
2, + 1
2; hence the linear part can have a
Jordan block for the eigenvalue 1. L

FINITE CYCLICITY 335

3. GENERALITIES ON THE BLOW-UP OF THE FAMILY

3.1. Blow-up of the Family

Consider the normal form for the unfolding of the nilpotent singularity
of saddle or elliptic type

X:˛ x˙ =y+m2+ax 2

y˙=m1+y(m3+x+e2x 2+x 3h1(x, m))+x 4h2(x, m)+y 2Q(x, y, m), (3.1)

where a ¥ [− 1
2,0) is the saddle case, a ¥ (0, 1
2) is the elliptic case, m=
(m1, m2, m3, l) is the parameter, and h1(x, m), h2(x, m)=e1e2a+O(x) and
Q(x, y, m) are C . and also Q(x, y, m) has arbitrarily high order in (x, y, m).
From now on, we denote A=(0, 1
2) for the elliptic case and A=(−1
2,0)
for the saddle case.
We are interested in this family for a ¥ A and (x, y, m) ¥ U× L, a neigh-
borhood of (0, 0) in R 2 × R 3. L can be taken as S 2 × [0, n0). Making the
change of parameters
 m1=n 3m¯ 1

m2=n 2m¯ 2

m3=nm¯ 3,
 (3.2)

where (m¯ 1, m¯ 2, m¯ 3) ¥ S 2 and n ¥ (0, n0), we have a three-parameter family of
vector fields in (x, y, n) space with parameters (a, m¯) ¥ A× S 2:

Xˆ :˛

x˙=y+n 2m¯ 2+ax 2

y˙=n 3m¯ 1+y[nm¯ 3+x+e2x 2+x 3h1(x, nm¯)]

+x 4h2(x, nm¯)+y 2Q(x, y, nm¯)

n˙=0.
 (3.3)

We then make the (weighted) blow-up of the singular point of (3.3) at
the origin by
 x=rx¯

y=r 2y¯

n=rr,
 (3.4)

where r>0 and (x¯, y¯, r) ¥ S 2.
By the blow-up (3.4), we have a C .-family X¯ =
1
r Xˆ . For each (a, m¯) ¥
A× S 2, X¯ induces a 3-dimensional vector field X¯ (a, m¯) defined in the neigh-
borhood of S 2 ×{0} with parameters (a, m¯) ¥ A× S 2.

336 ZHU AND ROUSSEAU

FIG. 6. The stratified set {rr=0} in the blow-up. (a) Elliptic case, (b) saddle case.

A combination of (3.2) and (3.4), as in [14], for (3.1), at (x, y, m1, m2, m3)
=(0, 0, 0, 0, 0), yields a global blow-up

F: S 2 × R+× S 2 Q R 5

((x¯, y¯, r), r, (m¯ 1, m¯ 2, m¯ 3)) W (x, y, m1, m2, m3), (3.5)

where x¯ 2+y¯ 2+r 2=1.
Because of the symmetry, as in Fig. 6, we only need to study X¯ on
{r \ 0} to get complete information for ((x¯, y¯, r), r, (m¯ 1, m¯ 2, m¯ 3)) near
0 ¥ S 2 × [0, r0)× S 2. Note that for each m¯, the foliation given by
{n=rr=const} is preserved by X¯ (a, m¯):

• For {rr=n} with n >0, the leaf is a regular manifold of dimension 2.
• For {rr=0}, we get a stratified set in the critical locus. As shown in
Fig. 6, there are two strata of 2-dimensional manifolds:

— Fˆ m¯ 5 S 1 ×R+, the blow-up of the fiber m=0,
— Dm¯ ={x¯ 2+y¯ 2+r 2=1, r \ 0}.

On Fˆ m¯ ={r=0}, (3.5) is just the common blow-up of the nilpotent point

x=rx¯

y=r 2y¯ (3.6)

and by the blow-up (3.6), we get a vector field with four singular points Pi
(i=1, 2, 3, 4). P3 and P4 are hyperbolic saddles, while P1 and P2 are nodes
(resp. saddles) in the elliptic (resp. saddle) case (Fig. 7).

FIG. 7. Common blow-up of the nilpotent singularity. (a) Elliptic case, (b) saddle cases.

FINITE CYCLICITY 337

To study the objects on and near Fˆ m¯ , we use the ‘‘phase directional
rescaling.’’ We use charts

P.R.1 x¯=−1, (r1, r1,y¯ 1)

P.R.2 x¯=1, (r2, r2,y¯ 2)

which cover the boundary of the half 2-sphere. In the charts P.R.1 and
P.R.2, by transformation (i=1, 2)

x= + ri

y=r 2
i y¯ i

mj=(riri) 4−j m¯ j (j=1, 2, 3)
 (3.7)

and after division by ri, we get a vector field near Pi (i=1, 2)

X¯ Pi˛

r˙i= + (a+y¯ i+m¯ 2r 2
i )ri

r˙ i= ± (a+y¯ i+m¯ 2r 2
i ) ri

y¯˙ i= + (1 − 2a) y¯ i ±2y¯ 2
i +y¯ i[e2ri+m¯ 3ri ±2m¯ 2r 2
i + r 2
i h1(±ri,riri, m¯)]

+m¯ 1r 3
i +rih¯2(±ri,riri, m¯)+y¯ 2
i Q¯ 2(ri, ri,y¯ i, m¯), (3.8)

where h¯1 and h¯2=ae2+O(r) are C . in (ri, ri, m¯) and Q¯ (ri, ri,y¯ i, m¯) is C .

in (ri, ri,y¯ i, m¯) and of arbitrarily high order in (ri, ri,y¯ i).
Easily, we see that X¯ P1 has two singular points P1(0, 0, 0) and
P4(0, 0, 1−2a
2 ), X¯ P2 has two singular points P2(0, 0, 0) and P3(0, 0, 1−2a
2 ). Each
singularity has three real eigenvalues listed in Table II. In Fig. 8, we draw
the phase portraits in the chart P.R.1 for the elliptic and saddle case,
respectively.
 TABLE II

Eigenvalues at Pi (i=1, 2, 3, 4)

r r y

P1 − a a − (1 − 2a)
P2 a − a (1 − 2a)
P3 1/2 − 1/2 − (1 − 2a)
P4 − 1/2 1/2 (1 − 2a)

338 ZHU AND ROUSSEAU

FIG. 8. The phase portraits of X¯ P1 . (a) X¯ P1 , the elliptic case; (b) X¯ P1 , the saddle case.

To complete the phase portrait on the blown-up sphere Dm¯ , we use the
family rescaling and the chart F.R. r=1, (x¯, y¯, r), yielding

x¯˙ =m¯ 2+y¯+ax¯ 2

y¯˙ =m¯ 1+(x¯+m¯ 3)y¯+rh¯(x¯, y¯, r, m¯)

r˙=0,
 (3.9)

where h¯(x¯, y¯, r, m¯) is C . in (x¯, y¯, r, m¯). Especially, on {r=0}, we have

X¯ r=1 ˛ x¯˙ =m¯ 2+y¯+ax¯ 2

y¯˙ =m¯ 1+(m¯ 3+x¯) y¯. (3.10)

In order to list all the possible limit periodic sets for the family, we have
to study the bifurcation diagram of (3.10) for m¯ ¥ S 2.

3.2. Bifurcation Diagrams for the Family Rescaling and Limit Periodic Sets

Following the convention of Kotova and Stanzo [24], we use pp to
denote a graphic connecting two parabolic sectors, hp to denote the graphic
coming out of a hyperbolic sector and connecting to a parabolic sector,
and hh to denote the graphic connecting two hyperbolic sectors. We find
the limit periodic sets after the blow-up and note that they often occur in
families. The geometry of the boundary limit periodic sets is important. We
hence give the complete bifurcation diagrams of system (3.10). They corre-
spond via y¯+m¯ 2+ax¯ 2=Y to the bifurcation diagrams for the principal
rescalings studied in [13] and [9]. Complete bifurcation diagrams have
been given there except for the position of the separatrices at infinity which
are better studied in the quadratic model given here.

Proposition 3.1. For the system (3.10), there holds

(1) System (3.10) has an invariant line y¯=0 if and only if m¯ 1=0.

• In the elliptic case, the curve m¯ 1=0 is a bifurcation curve except
when there are two nodes on the line y¯=0.

FINITE CYCLICITY 339

• In the saddle case, the curve m¯ 1=0 is a bifurcation curve precisely
when there are two finite saddles on it.

(2) If a ] 1
4, the system (3.10) has an invariant parabola

y=1 1
2 −a2 x 2+m¯ 3 1−2a
1−4a x+
(1 − 2a)(2am¯ 2
3+(1 − 4a) 2 m¯ 2
a(1 − 4a) 2 (3.11)

if and only if
 m¯ 1=
2a(1 − 2a)
(1 − 4a) 3 m¯ 3
3+
2(1 − 2a)
1−4a m¯ 2m¯ 3. (3.12)

FIG. 9. The bifurcation diagram of the rescaled family: the elliptic case a(0) ] 1
2.

340 ZHU AND ROUSSEAU

(3) If a=
1
4, the system (3.10) has an invariant parabola if and only
if m¯ 3=0. For m¯ 3=0, the system (3.10) has one, two, or three invariant
parabolas
 y=
1
4 x 2+Bx+m¯ 2+2B 2 (3.13)

if 27m¯ 2
1+16m¯ 3
3 >0, =0,or <0, and B is the solution of the algebraic
equation
 2B 3+2m¯ 2B− m¯ 1=0.

Proof. Direct calculations. L

Theorem 3.2. The bifurcation diagram of (3.10) for the elliptic case
(0<a< 1
2) is in Fig. 9, the bifurcation diagram for the saddle case

FIG. 10. The bifurcation diagram of the rescaled family: the saddle case a(0) ] − 1
2.

FINITE CYCLICITY 341

TABLE III

Limit Periodic Sets of pp Type for the Elliptic Case

( − 1
2 <a<0) is in Fig. 10. In particular the limit periodic sets are listed in
Tables III–VII.

Note that when we study X¯ r=1 at infinity, we use the quasi-homoge-
neous compactification:
 x¯= ± 1
z y¯= u
z 2. (3.14)

TABLE IV

Limit Periodic Sets of hp Type for the Elliptic Case

342 ZHU AND ROUSSEAU

TABLE V

Limit Periodic Sets of hh Type for the Elliptic Case

These transformations are just the transformations we used in the charts
P.R.1 and P.R.2.
For the elliptic case, there are 22 limit periodic sets which fall into three
types: Epp, Ehp, and Ehh. We list the 22 limit periodic sets of elliptic type
in Tables III–V.
For the saddle case, there are two types of limit periodic sets: convex
graphics Sxhh and concave graphics Sahh. We list all the possible limit
periodic sets of saddle type in Tables VI and VII.

FINITE CYCLICITY 343

TABLE VI

Convex Limit Periodic Sets of hh Type for the Saddle Case

For all the families of limit periodic sets listed in the following tables, we
use a to denote the upper boundary graphic, b or d to denote the interme-
diate graphics, and c or e to denote the lower boundary graphic.

4. THE DULAC MAPS AT THE ENTRANCE POINTS
OF THE BLOWN-UP SPHERE

To study the cyclicity of the graphics after the global blow-up, we will
need some basic properties of the transition maps in the neighborhood of
an elementary singular point.

344 ZHU AND ROUSSEAU

TABLE VII

Concave Limit Periodic Sets of hh Type for the Saddle Case

4.1. Transition Maps near the Elementary Singular Points in the Plane

Definition 4.1. (1) A singular point is elementary if it has at least
one nonzero eigenvalue. It is hyperbolic (resp. semihyperbolic) if the two
eigenvalues are not on the imaginary axis (resp. exactly one eigenvalue is
zero).
(2) The hyperbolicity ratio at a hyperbolic saddle is the ratio r=
−l1/l2, where l1 <0< l2 are the two eigenvalues.

Let Xl, l ¥ L,bea C . family of vector fields defined in the neigh-
borhood of a hyperbolic saddle at the origin. We also assume that the
coordinate axes are the invariant manifolds near the saddle point.
By the normal form theory, for any fixed k ¥ N,upto C k-equivalence,
we can write the vector field Xl into some explicit expressions of the

FINITE CYCLICITY 345

normal form (cf. [20, 35]). Let rl be the hyperbolicity ratio of Xl at the
origin; then

•If r0 is irrational, then, -k ¥ N, the vector field Xl is C k-equivalent to

x˙=x

y˙=−r(l)y

for l in some neighborhood W of the origin in parameter space.
•If r0 ¥ Q, let r0=
p
q , (p, q)=1. Then -k ¥ N, Xl is C k-equivalent to

x˙=x

y˙=y 5 −r0+ C

N(k)

i=0 ai+1(l)(x py q) i6

for l in some neighborhood W of the origin in parameter space. In
particular, a1=r0 −r(l).

Let S˜ 1={y=y0} and S˜ 2={x=x0} be two sections transversal to the
vector field Xl (Fig. 11), where x0,y0 >0 constant. The flow of Xl induces
a transition map Dl(., l), also called the Dulac map

Dl: S˜ 1 0 S˜ 2

for all l ¥ W.
The Dulac map is C . for x>0. The following theorem of Mourtada
[27] describes its behavior near x=0.

FIG. 11. Dulac map near a hyperbolic saddle.

346 ZHU AND ROUSSEAU

Proposition 4.2 (Mourtada). The Dulac map Dl can be written as

Dl(x)=x r(l)[c(l)+k(x, l)], (4.1)

where c(l)=y0/x r(l)
0 and k(x, l) is C . for (x, l) ¥ (0, x0]×W. Further-
more, k satisfies the following property (I .
0 ):

(I .
0 ): -n ¥ N, lim
x Q 0 x n “ nk
“x n (x, l)=0 uniformly for l ¥ W. (4.2)

(1) If r0 ¥ Q, then k — 0;
(2) If r0=1, then the expression (4.1) is in general not fine enough for
proving the cyclicity.

Definition 4.3 [25, 31]. The Leontovich–Andronova–Ecalle–Roussarie
compensator of the vector field Xl is defined as

w(x, a1)=˛
x −a1 −1
a1 if a1 ] 0

− ln x if a1=0.
 (4.3)

By the definition of w, we can easily check w(x, a1) has the following
property:

Proposition 4.4.

w(ab, a1)=w(a, a1)(1+a1w(b, a1))+w(b, a1). (4.4)

Since the Dulac map in Proposition 4.2 is not fine enough to prove the
cyclicity for the case r0=1, in [30], by using the compensator, Roussarie
has an additional refinement:

Proposition 4.5. If r0=1, then the Dulac map Dl has a well-ordered
asymptotic expansion

Dl(x)=a1(l)[xw+···]+b1(l)[x+ · · · ]

+a2(l)[x 2w+···]+ak(l)[x kw+···]+kk(x, l), (4.5)

where a1(l)=r(l)−1, b1(0) ] 0, and k is a C k function, k-flat with respect
to x=0.

4.2. Normal Forms at the Entrance Points

To study the Dulac maps in the neighborhood of the entrance points, the
vector fields should be in the normal form.

FINITE CYCLICITY 347

For the saddle and elliptic cases, the family of vector fields at each point
Pi (i=1, 2, 3, 4) has the same form as (3.8), the three eigenvalues not all
having the same sign. Due to the special form of the family (3.8), after
dividing by a C . positive function, system (3.8) is linear in r and r. If nec-
essary we change the time (t W −t) so that we have two negative eigen-
values while the third is positive (Table II). So for the three eigenvalues at
each point, there are only two possibilities

−1, 1, − s(a)

or
 1, − 1, − s(a),

where
 s(a)=˛: 1−2a
a : at P1 and P2

2(1 − 2a) at P3 and P4.

By exchanging the roles of r and r, we only need to consider one case for
system (3.8) which we rewrite as

X(a, m¯)˛

r˙=−r

r˙ =r

y¯˙ =−s(a) y¯+f(a, m¯)(r, r,y¯),
 (4.6)

where

f(a, m¯)(r, r,y¯)

=s(a) y¯+
 −(1−2a) y¯+2y¯ 2+y¯[e2r+m¯ 3r+2m¯ 2r 2 −r 2h1(r, rr, m¯)]
+m¯ 1r 3+rh¯2(r, rr, m¯)+y¯ 2Q¯ 2(r, r,y¯, m¯)
a+y¯+m¯ 2r 2

and the parameters (a, m) ¥ A× S 2, where for the saddle case A=(−1
2,0)
and for the elliptic case A=(0, 1
2).

Proposition 4.6. Consider the family X(a, m¯) in the form of (4.6) with
parameters (a, m¯) ¥ A× S 2. Then -(a0, m¯) ¥ A× S 2 and -k ¥ N, there exists
A0 … A, a neighborhood of a0, N(k) ¥ N, and a C k-transformation

Y(a, m¯): (r, r,y¯) Q (r, r, k(a, m¯)(r, r,y¯)),

348 ZHU AND ROUSSEAU

where
 k(a, m¯)(r, r,y¯)=y¯+o(|(r, r,y¯)|) (4.7)

such that -(a, m¯) ¥ A0 × S 2, the map k(a, m¯) transforms X(a, m¯) into one of the
following normal forms:

•if s(a0) ¨ Q
 X˜ (a, m¯)˛

r˙= + r

r˙ =± r

y˙=−s¯(a, m¯, n)y.
 (4.8)

•If s(a0)=
p
q ¥ Q

X˜ (a, m¯)˛

r˙=−r

r˙ =r

y˙=or p+
1
q 5 −p+ C

N(k)

i=0 ai+1(a, m¯, n)(r py q) i6 y,
 (4.9)

where n=rr >0 and
 s¯(a, m¯, n)=s(a) − a0(a, m¯, n)

a0(a, m¯, n)= C

N(k)

i=1 cin i

a1(a, m¯, n)=p − s¯(a, m¯, n)q,
 (4.10)

where ci(a, m¯), ai, and o are smooth functions defined for (a, m¯) ¥ A0 × S 2.
Especially if q \ 2, o=0.

Proof. The proof is a straightforward application of normal form
theory (see for instance [16, 20]). L

In order to study the cyclicity of the graphics with a nilpotent singularity
of elliptic or saddle type, we only need to consider X˜ (a.m¯) with eigenvalues
−1, 1, −s(a) in the normal forms (4.8) and (4.9) and consider the follow-
ing two types of Dulac maps (Fig. 12):

D(a, m¯)=(d, D): S 0 P

G(a, m¯)=(t, X): y 0 P,

where S={r=r0}, P={r=r0}, and y={y=y0} are sections in the
normal form coordinates and r0, r0, and y0 are positive constants.

FINITE CYCLICITY 349

FIG. 12. Two types of Dulac map. (a) First type, (b) second type.

To simplify the notation, for all the maps and vector fields, we will drop
the index (a, m¯). For example, the Dulac map D(n,y˜ 1) means D(a, m¯)(n,y˜ 1).
In the next section, we give some preparation propositions for the proof
of the two main theorems about the Dulac maps.

4.3. Preliminaries

First we define a notation I(i1,i2,...,ij;m,n):

Definition 4.7. Let m, n, j ¥ N 2 {0}; we define

I(i1i2 ···ij; m, n)=3 ii,i2,...,ij ¥ N 2 {0} : i1+i2+···+ij=m
i1+2i2+ · · · +jij=n4.

Proposition 4.8. Let f(t, z) be a smooth function and consider the
initial value problem
 dz
dt=f(t, z0, z), z(0)=z0.

Denote the unique solution as z=z(t, z0). Then -n ¥ N, the nth derivative
(“ nz/“z n
0)(t, z0) satisfies the linear initial value problem

d
dt 1 “ nz
“z n
02=
“f
“z “ nz
“z n
0+fn 1 t, z0,z, “z
“z0 , “ 2z
“z 2
0 , ..., “ n−1z
“z n−1
0 2

“ nz
“z n
0 (0)=0,

350 ZHU AND ROUSSEAU

where
 fn 1 t, z0,z, “z
“z0 , “ 2z
“z 2
0 ,..., “ n−1z
“z n−1
0 2

=
“ nf
“z n
0 + C

n

i=2
 “ if
“z i C
I(i1i2 ···in−1;i,n) fD

n−1

l=1 1 “z
“z02 il

+ C

n−1

j=1 C

n−j

i=1
 “ i+jf
“z i
0“z j C
I(i1i2 ···in−1;j,n − j) fD

n−1

l=1 1 “z
“z0 2 il.

fn as well as all the partial derivatives are all evaluated at (t, z0, z(t, z0)) and
f denotes a positive integer.

Proof. By induction. L

Proposition 4.9. Let us consider the initial value problem

dz
dt=f(t, z)

z(0)=0

with t ¥ [0, T]. If there exist two continuous functions A(t), B(t) with

|f(t, z)| [ |A(t)| |z|+|B(t)|, (t, z) ¥ [0, T] × [0, Z0],

then for t ¥ [0, T], the solution of the initial value problem satisfies

|z(t)| [ e >t
0 |A(t)| dt F t

0 |B(t)| e −>t
0 |A(t)| dt dt.

Furthermore, if there exist constants M1,M2 >0 such that

|A(t)| [ M1

|B(t)| [ M2,

then there exists a constant K>0 such that for t ¥ [0, T], there holds

|z(t)| [ KM2t.

Proof. Calculations. L

4.4. Dulac Map of the First Type

We now study the first type of Dulac map D=(d, D). If we parameterize
the sections S and P by (n,y) with the obvious relation r=n/r0 on S and
r=n/r0 on P, then we have
FINITE CYCLICITY 351

Theorem 4.10. For any a0 ¥ A and m¯ ¥ S 2, consider the family X˜ =X˜ (a, m¯)
with eigenvalues −1, 1, s(a0) in normal form (4.8) or (4.9). Then -Y0 ¥ R,
there exist A0 … A, a neighborhood of a0, and n1 >0 such that -n ¥ (0, n1)
and (a, m¯,y) ¥ A0 × S 2 × [0, Y0], the Dulac map D(n, y)=(d(n, y), D(n, y))
has the form

d(n,y)=n

D(n,y)=g 1 n, w 1 n
n0 ,−a122+1 n
n02 s¯ 5y+f 1 n, w 1 n
n0 ,−a12,y26, (4.11)

where n0=r0r0 >0 a constant and

if s(a0) ¨ Q

g=f=0;

if s(a0) ¥ Q 0 N

g=0;

if s(a0)=p ¥ N

g 1 n, w 1 n
n0 ,−a122=or p
0 w 1 n
n0 ,−a121 n
n02 s¯;

if s(a0)=
p
q ¥ Q, p, q ¥ N and (p, q)=1, then f1n, w1 n
n0 ,−a12,y2 is C. and

f=O 1 n p¯w q+1 1 n
n0 ,−a12 ln n
n02

“f
“y
=O 1 n p¯w q 1 n
n0 ,−a12 ln n
n02

“ jf
“y j=O 1 n p¯ (1+[j−2
q ])w q − j+1+q [j−2
q ] 1 n
n0 ,−a12 ln n
n02,j \ 2
(4.12)

where
 p¯=˛ qs¯(a, n) a1 \ 0
p a1 <0. (4.13)

Also all the partial derivatives with respect to the parameters (a, m¯) are of
order
 O 1 n p¯w q 1 n
n0 ,−a12 ln n
n02.

352 ZHU AND ROUSSEAU

Proof. The proof is similar to the corresponding proof in [14].
Since we consider the Dulac map D(n,y) in the invariant leaf n=rr >0,
let n0=r0r0. Then the transition time from S to P is

t=ln r
r0=−ln n
n0 .

The first component d(n,y) is easily obtained:

d(n, y)=r0r0e −t=r0r0 n
n0=n.

Now let us consider the second component D(n,y).

(1) Case s(a0) ¨ Q. By the normal form (4.8), we directly have

D(n, y)=e −s¯ty=1 n
n02 s¯ y.

(2) Case s(a0)=
p
q ¥ Q, p, q ¥ N, (p, q)=1. Note that r(t)=r0e −t,
r(t)=(n/r0)e t, so by the third equation of (4.9), we can write the solution
of y as
 y(t)=e −s¯t[y0+or p
0 W(−a1, t)+U(t)]=e −s¯tW(t), (4.14)

where
 W(a1, t)=˛
e a1t −1
a1 a1 ] 0

t a1=0.

Note that if q \ 2, then o=0.
A straightforward calculation shows that U(t) satisfies

U˙ (t)=g(n, t, W(t))

U(0)=0, (4.15)

where g(n, t, W(t))=; N
i=1 (ai+1/r pi
0 ) n pie a1itW qi+1(t). First we are going to
prove that U(t) is bounded for t ¥ [0, |ln n/n0|].
By the definition of W(t) in (4.14), there exist constants K1,K2 >0 such
that
 |W(t)| [ K1+K2w 1 n
n0 ,−a12+|U(t)|, t ¥50, : ln n
n0:6, (4.16)

where K2=0 as long as q \ 2.

FINITE CYCLICITY 353

We want to show that U(t) is bounded, so we only need to consider the
region where |U(t)| \ 1. In such a region, by the definition of p¯ in (4.13),
there exists K3 >0 such that for t ¥ [0, |ln n/n0|] with n sufficiently small

|g(n,t,W)| [ K3n p¯w q+1 1 n
n0 ,−a12 |U| Nq+1. (4.17)

Indeed, for n sufficiently small and for t ¥ [0, |ln n/n0|],

|g(n,t,W)| [ C

N

i=1
 |ai+1|
r pi
0 n pie a1it |W(t)| qi+1

[ C

N

i=1
 |ai+1| n a1i
0
r pi
0 n p¯i |W(t)| qi+1

[ C

N

i=1
 |ai+1| n a1i
0
r pi
0 n p¯i 5K1+K2w 1 n
n0 ,−a12+|U(t)|6 qi+1

[ K3n p¯w q+1 1 n
n0 ,−a12 |U(t)| Nq+1.

Hence U(t) stays bounded by the solution of the initial value problem

Z˙ (t)=K3n p¯w q+1 1 n
n0 ,−a12 Z(t) Nq+1

Z(0)=1.

So for t ¥ [0, |ln n/n0|], there exist constants K4,K5 >0 such that

|U(t)| [ Z(t)= 1
1 1 − NqK3n p¯w q+1 1 n
n0 ,−a12 t2
 1
Nq

[51−K4n p¯w q+1 1 n
n0 ,−a12 ln n
n06 [ K5.

Since |U(t)| is bounded, by (4.15) and (4.17), there exists a constant
K6 >0 such that for t ¥ [0, |ln n/n0|]

|U˙ (t)| [ K6n p¯w q+1 1 n
n0 ,−a12.

So, -(a, m¯) ¥ A0 × S 2, -n ¥ (0, n0), and for t ¥ [0, |ln n/n0|], we have

|U(t)| [ K6n p¯w q+1 1 n
n0 ,−a12: ln n
n0:. (4.18)

354 ZHU AND ROUSSEAU

Substituting the transition time t=−ln n/n0 into (4.14) and letting

U(t)|t=−ln n
n0 =f 1 n, w 1 n
n0 ,−a12,y2,

then for the second component of the map D, we get

D(n,y)=1 n
n02 s¯ 5y+or p
0 w 1 n
n0 ,−a12+f 1 a, n, w 1 n
n0 ,−a12,y26

=g 1 n, w 1 n
n022+1 n
n02 s¯ 5y+f 1 a, n, w 1 n
n0 ,−a12,y26

where f is C . in (a, m¯, n, w(n/n0,−a1), y) and uniformly bounded; i.e., for
(a, m¯) ¥ A0 × S 2, n ¥ (0, n1), and y ¥ [0, Y0], we have

f 1 n, w 1 n
n0 ,−a12,y2=O 1 n p¯w q+1 1 n
n0 ,−a12 ln n
n02.

Now we consider the derivatives “ if/“y i for i \ 1.
For “f
“y, since “W
“y =1+
“U
“y ,so “W
“y satisfies

d
dt 1 “W
“y 2=g1(n, t, W(t)) “W
“y

“W
“y (0)=1,
 (4.19)

where g1(n, t, W(t))=; N
i=1 ((qi+1) ai+1/r pi
0 ) n pie a1itW qi(t).
For t ¥ [0, |ln n/n0|], by (4.16) and (4.18), and similar to the proof of
(4.17), there exists a K¯ 1 >0 such that

|g1(n, t, W(t))| [ K¯ 1n p¯w q 1 n
n0 ,−a12. (4.20)

Then, by (4.19) and (4.20) we have for t ¥ [0, |ln n/n0|]

e −K¯ 1n p¯wq ( n
n0 ,−a1)|ln n
n0| [ “W
“y [ e K¯ 1n p¯wq ( n
n0 ,−a1)|ln n
n0|.

Hence
 e −K¯ 1n p¯wq ( n
n0 ,−a1)|ln n
n0| −1 [ “U
“y [ e K¯ 1n p¯wq ( n
n0 ,−a1)|ln n
n0| −1.

FINITE CYCLICITY 355

So there exists Kˆ 1 >0 such that for (a, m¯) ¥ A0 × S 2 and n ¥ (0, n0), for
0 [ t [ |ln n/n0| : “U
“y: [ Kˆ 1n p¯w q 1 n
n0 ,−a12: ln n
n0:. (4.21)

Thus for f(n, w(n/n0,−a1), y), we have

“f
“y
=O 1 n p¯w q 1 n
n0 ,−a12 ln n
n02.

It is clear that the above properties on f also hold for all the partial
derivatives with respect to the parameters (a, m¯) ¥ A0 × S 2.
For “ iW/“y i(i \ 2), we will use induction on i. First show that for
2 [ i [ q+1, there holds

“ if
“y i=O 1 n p¯w q+1 − i 1 n
n0 ,−a12 ln n
n02.

Assume that for 2 [ i [ q, we have
: “ iW
“y i : [ Kˆ in p¯w q+1 − i 1 n
n0 ,−a12: ln n
n0:. (4.22)

Now we turn to “ i+1W/“y i+1. By Proposition 4.8, “ i+1W/“y i+1 satisfies
the following initial value problem

d
dt 1 “ i+1W
“y i+1 2=g1(n,t,W) “ i+1W
“y i+1 +gi+1 1 n,t,W, “W
“y , “ 2W
“y 2 ,..., “ iW
“y i 2

“ i+1W
“y i+1 (0)=0,
 (4.23)

where

gi+1 1 n,t,W, “W
“y , “ 2W
“y 2 ,..., “ iW
“y i 2= C

i+1

j=2
 “ jg
“W j C
I(j1j2 ···ji;j,i+1) fD

i

k=1 1 “W
“y02 jk.

We claim that there exists a constant K¯ i+1 >0 such that for t ¥
[0, |ln n/n0|]
: gi+1 1 n,t,W, “W
“y , “ 2W
“y 2 , ..., “ iW
“y i 2: [ K¯ i+1n p¯w q+1 − (i+1) 1 n
n0 ,−a12. (4.24)

356 ZHU AND ROUSSEAU

Indeed, for 2 [ j [ i+1, similar to the proof of (4.17), there exist
constants K¯ j1 >0 (j=2, 3, ..., i+1) such that
: “ jg
“W j:=: C

N(k)

i=1 j! 1 qi+1
j 2 ai+1
(n a1
0 r p
0 ) i n pie a1itW qi+1 − j(t):

[ K¯ j1n p¯w q+1 − j 1 n
n0 ,−a12. (4.25)

Note that by (4.21), we have |“W
“y | [ K¯ 0, so by (4.25) and by the induction
assumption (4.22), there exists a constant K¯ i+1 >0 such that
: gi+1 1 n, t, W(t), “W
“y , “ 2W
“y 2 ,..., “ iW
“y i 2:

[ C

i+1

j=2 K¯ j1n p¯w q+1 − j C
I(j1j2 ···ji;j,i+1) fD

i

l=2 1 n p¯w q − (l − 1) : ln n
n0:2 jl

= C

i+1

j=2 K¯ j1n p¯w q+1 − j C
I(j1j2 ···ji;j,i+1) f 1 n p¯w q : ln n
n0:2 j2+j3+···+ji w −j2 −2j3 − (i − 1) ji

= C

i+1

j=2 K¯ j1n p¯w q+1 − j C
I(j1j2 ···ji;j,i+1) f 1 n p¯w q : ln n
n0:2 j−j1 w j − (i+1)

[ K¯ i+1n p¯w q+1 − (i+1) 1 n
n0 ,−a12,

where in the final sum the dominant term is the term with j=j1=q+1.
By (4.20), (4.24), and Proposition 4.9, for the solution of (4.23), there
exists a constant Kˆ i+1 such that for t ¥ [0, |ln n/n0|]
: “ i+1W
“y i+1 : [ Kˆ i+1n p¯w q+1 − (i+1) 1 n
n0 ,−a12: ln n
n0:,2 [ i [ q. (4.26)

Therefore, for 2 [ i [ q+1, it follows from (4.22), (4.26), and by induction
that we have
 “ if
“y i
0=O 1 n p¯w q+1 − i 1 n
n0 ,−a12: ln n
n0:2.

Generally, -j \ 2, we can decompose j as j − 2=lq+i with 0 [ i [
q − 1, l \ 0. Then in the same way as for the case l=0, we can prove that

“ jf
“y j
0=O 1 n p¯ (1+[j−2
q ])w q − j+1+q [j−2
q ] 1 n
n0 ,−a12 ln n
n02. L

FINITE CYCLICITY 357

Remark 4.11. In Theorem 4.10, if q=1, then -j \ 2, we have

“ jf
“y j
0=O 1 n (j − 1) p¯ ln n
n02.

Remark 4.12. By Theorem 4.10, the properties of the Dulac map D
are valid on a compact set K1 of S. When we want to analyze a graphic
intersecting S at (r0,y g), we will of course choose K1 so that (r0,y g) ¥ K1.

The following lemma will be needed later to simplify the products of the
form 1 n
n02 s¯1 1 n
n02 −s¯2 1 resp. 1 n
n02 s¯3 1 n
n02 −s¯42

appearing when we compose the Dulac map at P1 (resp. P3) with the
inverse of the Dulac map at P2 (resp. P4).

Lemma 4.13. -a ¥ A,
1 n
n02 s¯=1 n
n02 s [1+N(n, ln n)], (4.27)

where
 N(n, ln n)=−c1(a, m¯, n) n ln n
n0+O(n 2(ln n) 2)

and c1(a, m¯, n) is defined in (4.10).

Proof. By the definition of s¯ in (4.10), we have
1 n
n02 s¯=1 n
n02 s 1 n
n02 −a0=1 n
n02 s exp 1 − a0 ln n
n02

=1 n
n02 s 51− c1n ln n
n0+O(n 2(ln n) 2)6. L

4.5. Dulac Map of the Second Type

Now we consider a Dulac map of the second type G=(t, X) (Fig. 12b).
If we parameterize y by (r, r), P by (n,y) with the relation rr=n, and
r=n/r0 on the two sections, respectively, then we have

Theorem 4.14. For any a0 ¥ A, consider X˜ l with eigenvalues −1, 1,
−s(a0) in the normal form (4.8) and (4.9). Then for r, r >0 sufficiently

358 ZHU AND ROUSSEAU

small, there exist A0 … A, a neighborhood of a0, and n1 >0 such that -(a, m¯) ¥
A0 × S 2 and n ¥ (0, n1), the Dulac map G(r, r) has the form

t(r, r)=n

X(r, r)=g 1 n, w 1 r
r0 , a122+1 r
r02 s¯ 5y0+h 1 r, r, w 1 r
r0 ,−a1226, (4.28)

where

•if s(a0) ¨ N, then g=0;if s(a0)=p ¥ N, then

g(n, w(r, a1))= o
r p
0 n pw 1 r
r0 , a12,

•if s(a0) ¨ Q, then h=0;if s(a0)=
p
q ¥ Q, then h(r, r, w(r/r0,−a1))
is C . in (a, m¯) and (r, r, w(r/r0,−a1)), and also satisfies

h=O 1 r pw 1 r
r0 , a1251+or pw 2 1 r
r0 ,−a1262

r j “ jh
“r j=O 1 r pw 1 r
r0 , a122 51+or pw 2 1 r
r0 ,−a1262,j \ 1.
 (4.29)

which are uniformly valid for (a, m¯) ¥ A0 × S 2 and r, r >0 sufficiently small.

Proof. t(r, r)=n follows from the invariance of rr=n.
For the second component X(r, r), the transition time from y to P is
t=|ln r/r0|. So for the case s(a0) ¨ Q by (4.8), we directly have

X(r, r)=y0e −st|t=|ln r
r0|=y0 1 r
r02 s
.

Now we consider the case s(a0)=
p
q ¥ Q. Note that r(t)=re −t and
r(t)=re t. Hence, by the third equation of (4.9), we have a first order
differential equation in y

y˙=−s¯y+or pe −pt+
1
q C

N(k)

i=1 ai+1(re t) pi y qi+1. (4.30)

Let the solution of (4.30) with the initial value y(0)=y0 be

y(t)=e −s¯t[y0+or pW(t, −a1)+V(t)]. (4.31)

FINITE CYCLICITY 359

Then V(t) satisfies the initial value problem

V˙ (t)=h(n,t, r, E(t))

V(0)=0, (4.32)

where
 E(t)=y0+or pW(t, −a1)+V(t),

h(n,t, r, E(t))= C

N

i=1 ai+1r pie ia1tE qi+1(t). (4.33)

So for X(r, r), substituting the transition time t=|ln r/r0| into (4.31)
and letting
 h 1 r, r, w 1 r
r0 ,−a122=V(t)|t=|ln r
r0|, (4.34)

then we have

X(r, r)=g 1 n, w 1 r
r0 , a122+1 r
r02 s¯ 5y0+h 1 r, r, w 1 r
r0 ,−a1226

where h(r, r, w(r/r0,−a1)) is C . and

g 1 n, w 1 r
r0 , a122=or p 1 r
r02 s¯ w 1 r
r0 ,−a12= o
r p
0 n pw 1 r
r0 , a12.

(1) Bound for h(r, r, w(r/r0,−a1)). First we prove that V(t) is
bounded for t ¥ [0, |ln r/r0|].
By (4.33), if we denote M0=|y0|, then

|E(t)| [ M0+|o|r pW(t, −a1)+|V(t)|. (4.35)

Note that for t ¥ [0, |ln r/r0|], W(t, −a1) [ w(r/r0,−a1), so, if we
restrict to the region V(t) \ 1, by (4.33) and (4.35), there exists a constant
M1 >0 such that

|h(n,t, r, E(t))|

[ r pe a1t C

N

i=1 |ai+1| r p(i − 1)e a1(i − 1) t 5M0+or pw 1 r
r0 ,−a12+|V(t)|6 qi+1

[ r pe a1t 5f w q+1 1 r
r0 ,−a12 |V(t)| q+1+f |V(t)| 2q+1+···+f |V(t)| Nq+16

[ M1r pe a1tw q+1 1 r
r0 ,−a12 |V(t)| Nq+1. (4.36)

360 ZHU AND ROUSSEAU

Hence by (4.32) and (4.36), V(t) stays bounded by the solution of the
initial value problem

Z˙ (t)=M1r pe a1tw q+1 1 r
r0 ,−a12 Z Nq+1

Z(0)=1.

So there exists a constant M2 >0 such that for t ¥ [0, |ln r/r0|],

|V(t)| [ Z(t)= 1
51 − qNM1r pw q+1 1 r
r0 ,−a12 W(t, a1)6
 1
Nq [ M2. (4.37)

Again by (4.35) and (4.37), there exists a constant M3 >0 such that for
t ¥ [0, |ln r/r0|],
 |E(t)| [ M3+or pw(t, −a1). (4.38)

We will prove that there exist constants M4,M5 >0 such that

|h(n,t, r, E(t))| [ r pe a1t 5M4+M5or pw 2 1 r
r0 ,−a126. (4.39)

Indeed, for the case q=1, there exist M4,M5, and M5i >0
(i=3, 4, ..., N+1) such that

|h(n,t, r, E(t))|

[ C

N

i=1 |ai+1| r pie ia1t |E i+1(t)|

[ r pe a1t 5|a2| 1 M 2
3+2oM3r pw 1 r
r0 ,−a12+o 2r 2pw 2 1 r
r0 ,−a122

+|a3|M53+···+|aN+1|M5(N+1)6

[ r pe a1t 5M4+M5or pw 2 1 r
r0 ,−a126.

The case q \ 2 is similar with o=0.

FINITE CYCLICITY 361

So for the solution of Eq. (4.32), for t ¥ [0, |ln r/r0|], by (4.39) we have

|V(t)| [ F t

0 |h(s, r, E(s))| ds

[ F t

0 r pe a1s 5M4+M5or pw 2 1 r
r0 ,−a126 ds

=r pW(t, a1) 5M4+oM5r pw 2 1 r
r0 ,−a126

[ r pw 1 r
r0 , a125M4+oM5r pw 2 1 r
r0 ,−a126. (4.40)

Hence for h(r, r, w(r/r0,−a1)) given in (4.34), for (a, m¯) ¥ A0 × S 2 and
r, r >0, rr=n sufficiently small, we have

h 1 r, r, w 1 r
r0 ,−a122=O 1 r pw 1 r
r0 , a1251+or pw 2 1 r
r0 ,−a1262.

We will use induction on i (i \ 1) to study “ ih/“r i.
(2) Bound for “h
“r. By the first equation of (4.33), we have “V
“r=
“E
“r ,so
“E
“r satisfies the following linear equation

d
dt 1 “E
“r2=h0(t, r,E) “E
“r+h1(t, r,E)

“E
“r (0)=0,
 (4.41)

where
 h0(t, r,E)= “h
“E (t, r, E)= C

N(k)

i=1 (qi+1) ai+1r pie a1itE qi(t),

h1(t, r,E)=“h
“r (t, r, E)= C

N(k)

i=1 piai+1r pi − 1e a1itE qi+1(t).

By (4.38) and similar to the proof of (4.39), we can prove that there exist
constants M¯ 1i >0 (i=1, 2, 3, 4) such that

|h0(t, r,E)| [ r pe a1t 5M¯ 11+oM¯ 12r pw 1 r
r0 ,−a126

=e a1tA¯(r, r)=A(t, r, r)

362 ZHU AND ROUSSEAU

|h1(t, r,E)| [ r p−1e a1t 5M¯ 13+oM¯ 14r pw 2 1 r
r0 ,−a126

=e a1tB¯ (r, r)=B(t, r, r). (4.42)

Then by (4.42) and Proposition 4.9, there exist constants Mˆ 11,Mˆ 12 >0
such that for t ¥ [0, |ln r/r0|], there holds
: “E
“r: [ r p−1w 1 r
r0 , a125Mˆ 11+oMˆ 12r pw 2 1 r
r0 ,−a126. (4.43)

So by Proposition 4.9, for t ¥ [0, |r/r0|], there exist a constant
M¯ 1,Mˆ 11,Mˆ 12 >0 such that
: “E
“r: [ e >t
0 A(s, r, r)ds F t

0 B(u, r, r)e −>u
0 A(s, r, r)ds du

=e >t
0 A¯(r, r)ea1s ds 5 − B¯ (r, r)
A¯(r, r) F t

0 d(e −>u
0 A¯(r, r)ea1s ds)6

=B¯ (r, r)
A¯(r, r) (e >t
0 A¯(r, r)ea1s ds −1)

[ B¯ (r, r)
A¯(r, r) [e A¯(r, r) w ( r
r0 , a1) −1]

=B¯ (r, r)
A¯(r, r) 5e t1A¯(r, r) w 1 r
r0 , a126

[ r p−1w 1 r
r0 , a125Mˆ 11+oMˆ 12r pw 2 1 r
r0 ,−a126 (4.44)

where t1 ¥ (0, A¯(r, r) w(r/r0, a1)), M¯ 1=e A¯(r, r) w(r/r0, a1), and Mˆ 11=M¯ 1M¯ 13,
Mˆ 12=M¯ 1M¯ 14.
So for (a, m¯) ¥ A0 × S 2 and r, r >0 sufficiently small, we have uniformly

r “h
“r
=O 1 r pw 1 r
r0 , a121 1+or pw 2 1 r
r0 ,−a122.

(3) Bound for “ ih/“r i, (i \ 2). Assume that there exist constants
Mˆ j1,Mˆ j2 >0 such that for 2 [ j [ i, there holds
: “ jE
“r j: [ r p−jw 1 r
r0 , a12 Lˆ j 1 r, w 1 r
r0 ,−a122 (4.45)

FINITE CYCLICITY 363

where
 Lˆ j 1 r, w 1 r
r0 ,−a122=Mˆ j1+oMˆ j2r pw 2 1 r
r0 ,−a12.

Now let us consider “ j+1E/“r j+1. By Proposition 4.8, it satisfies

d
dt 1 “ i+1E
“r i+12=h0(t, r,E) “ i+1E
“r i+1+hi+1 1 t, r,E, “E
“r , “ 2E
“r 2 ,..., “ iE
“r i2

“ i+1E
“r i+1 (0)=0,
 (4.46)

where
 hi+1=“ i+1h
“r i+1+ C

i

j=2
 “ jh
“E j C
I(j1j2 ···ji;j,i+1) fD

i

k=1 1 “ kE
“r k2 jk

+ C

i

l=1 C

i+1 − l

j=1
 “ j+lh
“r j“E l C
I(l1l2 ···li;l,i+1 − j) fD

i

k=1 1 “ kE
“r k2 lk. (4.47)

Lemma 4.15. There exist constants M¯ i+1, 1,M¯ i+1, 2 >0 such that for
-(a, m¯) ¥ A0 × S 2 and for r, r >0 sufficiently small, there holds

|hi+1(t, r,E)| [ r p − (i+1)e a1tw 1 r
r0 , a125M¯ i+1, 1+oM¯ i+1, 2w 1 r
r0 ,−a126.

(4.48)

Proof. Let us denote the first and the second sum in (4.47) by hI and
hII; i.e.,
 hi+1=“ i+1h
“r i+1+hI+hII. (4.49)

For “ i+1h/“r i+1, by (4.38) and the definition of h in (4.33), there exist
constants Mi+1, 1, Mi+1, 2 >0 such that
: “ i+1h
“r i+1: [ r p − (i+1)e a1t 5Mi+1, 1+oMi+1, 2r pw 2 1 r
r0 , a126. (4.50)

Similarly, there exist constants M˜ j1,M˜ j2,M˜ jl1, and M˜ jl2 >0 such that
: “ jh
“E j: [ r pe a1tL¯ j 1 r, w 1 r
r0 ,−a122 (4.51)
: “ j+lh
“r j“E l: [ r p−je a1tL˜ jl 1 r, w 1 r
r0 ,−a122 (4.52)

364 ZHU AND ROUSSEAU

where
 L¯ j 1 r, w 1 r
r0 ,−a122=M˜ j1+oM˜ j2r pw 1 r
r0 ,−a12

L˜ jl 1 r, w 1 r
r0 ,−a122=M˜ jl1+oM˜ jl2r pw 1 r
r0 ,−a12.

So for hI, by (4.51), (4.44), and assumption (4.45), for t ¥ [0, |ln r/r0|]
we have
: hI 1 t, r,E, “E
“r , “ 2E
“r 2 ,..., “ iE
“r i2:

[ C

i

j=2 : “ jh
“E j: C
I(j1j2 ···ji;j,i+1) f : “E
“r: j1 : “ 2E
“r 2: j2 ···: “ iE
“r i: ji

[ C

i

j=2 r pe a1tL¯ j(r, w) C
I(j1j2 ···ji;j,i+1) fD

i

k=1 |r p−kwLˆ k(r, w)| jk

[ C

i

j=2 r pe a1tL¯ j(r, w) C
I(j1j2 ···ji;j,i+1) f r p ; i
k=1 jk − ; i
k=1 kjkw ; i
k=1 jk D

i

k=1 Lˆ jk
k (r, w)

[ C

i

j=2 r pe a1tL¯ j(r, w) C
I(j1j2 ···ji;j,i+1) f r pj − (i+1)w j D

i

k=1 Lˆ jk
k (r, w)

[ r p − (i+1)e a1t C

i

j=2 r pjw jL¯ j(r, w) C
I(j1j2 ···ji;j,i+1) fD

i

k=1 Lˆ jk
k (r, w)

[ o(r 2p − 1) r p − (i+1)e a1t. (4.53)

Similarly, for hII, by (4.52), (4.44), and (4.45), we have
: hII 1 t, r,E, “E
“r , “ 2E
“r 2 ,..., “ iE
“r i2:

[ C

i

l=1 C

i+1 − l

j=1 : “ j+lh
“r j“E l: C
I(l1l2 ···li;l,i+1 − j) fD

i

k=1 : “E
“r: lk

[ C

i

l=1 C

i+1 − l

j=1 r p−je a1tL˜ jl(r, w) C
I(l1l2 ···li;l,i+1 − j) fD

i

k=1 [r p−kwLˆ k(r, w)] lk

[ C

i

l=1 C

i+1 − l

j=1 r p − j+pl − (i+1 − j)e a1tw lL˜ jl(r, w) C
I(l1l2 ···li;l,i+1 − j) fD

i

k=1 Lˆ lk
k (r, w)

[ r p − (i+1)e a1t C

i

l=1 r plw l C

i+1 − l

j=1 L˜ jl(r, w) C
I(l1l2 ···li;l,i+1 − j) fD

i

k=1 Lˆ lk
k (r, w)

[ O 1 r pw 1 r
r0 , a122 r p − (i+1)e a1t. (4.54)

FINITE CYCLICITY 365

Then by (4.49), (4.50), (4.53), and (4.54), there exist positive constants
M¯ i+1, 1 and M¯ i+1, 2 such that

|hi+1| [: “ i+1h
“r i+1:+|hI|+|hII|

[ r p − (i+1)e a1t 5Mi+1, 1+oMi+1, 2r pw 2 1 r
r0 , a126+o(r 2p − 1) r p − (i+1)e a1t

+O 1 r pw 1 r
r0 , a122 r p − (i+1)e a1t

[ r p − (i+1)e a1tw 1 r
r0 , a125M¯ i+1, 1+oM¯ i+1, 2w 2 1 r
r0 ,−a126. L

End of proof of Theorem 4.14. Then for the initial value problem (4.46)
with the estimations (4.42) and (4.48), similar to the proof (4.44), again by
Proposition 4.9, for t ¥ [0, |r/r0|], there exist constants Mˆ i+1, 1,Mˆ i+1, 2 >0
such that for t ¥ [0, |r/r0|] we have
: “ i+1E
“r i+1: [ r p − (i+1)w 1 r
r0 , a125Mˆ i+1, 1+oMˆ i+1, 2r pw 2 1 r
r0 ,−a126. (4.55)

Hence for (a, m¯) ¥ A0 × S 2 and r, r >0 sufficiently small, we have

r i+1 “ i+1h
“r i+1=O 1 r pw 1 r
r0 , a121 1+or pw 2 1 r
r0 ,−a122. L

Remark 4.16. Although for a0 ¥ Q, the inverse of the map G(r, r) has
no nice expression, it has a nice expression inside either the invariant sub-
space r=0 or the invariant subspace r=0. This expression is the usual
expression of the Dulac map in the neighborhood of a 2-dimensional
saddle [27, 30].

5. FINITE CYCLICITY OF CONVEX GRAPHICS WITH
A NILPOTENT SINGULARITY OF SADDLE TYPE

5.1. Preliminaries on the Derivatives of Regular Transition Maps

In proving the finite cyclicity of graphics of saddle or elliptic type, we
will need to calculate the derivatives of a regular transition map. First we
recall briefly the formula of [2].

366 ZHU AND ROUSSEAU

Proposition 5.1 (ALGM). Consider the vector field

X=P(x, y) “
“x
+Q(x, y) “
“y. (5.1)

Let S={(x, y)=(f1(s), g1(s))} and S˜ ={(x, y)=(f2(s), g2(s))} be two
arcs transverse to the same orbit. Let R(s) be the transition map from S to
S˜ . Then
 RŒ(s)= D(s)
D˜ (R(s)) exp 1 F T(s)

0 div X(c(t)) dt2, (5.2)

where T(s) is the transition time from (f1(s), g1(s)) to (f2(R(s)), g2(R(s)))
along the orbit c(t) starting at (f1(s), g1(s)) for t=0 and

D(s)=: P(f1(s), g1(s)) f −
1(s)
Q(f1(s), g1(s)) g −
1(s):

D˜ (s˜)=:P(f2(s˜), g2(s˜)) f −
2(s˜)
Q(f1(s˜), g2(s˜)) g −
2(s˜):.

It is not easy to use Proposition 5.1 to calculate the higher order deriva-
tives of a regular transition map. The following proposition will be very
useful.

Proposition 5.2. Consider the transition map R(x) of the vector field
X=P(x, y) “
“x+Q(x, y) “
“y between two arcs without contact, S={(x, y)=
(x, f1(x))} and S˜ ={(x, y)=(x, f2(x))}, in a region where Q(x, y) ] 0. Let
x=x(x0,y0,y) be the solution with initial condition x(x0,y0,y0)=x0. Then

dR
dx0 (x0)=exp 1 F f2(R(x0))

f1(x0) 1 P −
xQ−PQ −
x
Q 2 2:

x=x(x0,f1(x0), y) dy2

1−1 P
Q2 (x0,f1(x0)) f −
1(x0)

1−1 P
Q2 (x0,f2(R(x0))) f −
2(R(x0)). (5.3)

Formulas for the first and second derivatives are given in the particular case
where x0=0 and P(0, y) — 0. Let yi=fi(0).

RŒ(0)=exp 1 F y2

y1
 P −
x
Q (0, y) dy2. (5.4)

FINITE CYCLICITY 367

Rœ(0)=RŒ(0) 52 1 f −
2(0) RŒ(0) 1 Px
Q2 (0, y2)−f −
1(0) 1 Px
Q2 (0, y1)2

+F y2

y1 1 P '
x
Q (0, y) − 2 P −
xQ −
x
Q 2 (0, y)2 exp 1 F y

y1
 P −
x
Q (0, z) dz2 dy6.

(5.5)

Proof. We rewrite the vector field into the equivalent differential
equation
 dx
dy
=P
Q. (5.6)

The solution is x=x(x0,f1(x0), y) with initial condition x(x0,f1(x0), f1(x0))
=x0. We have that R(x0)=x(x0,f1(x0), f2(R(x0))). Moreover

“
“y “x
“x0= “
“x0
 “x
“y
= “
“x0
 P(x(x0,f1(x0), y), y)
Q(x(x0,f1(x0), y), y)
=
P −
xQ−PQ −
x
Q 2 “x
“x0 (5.7)

from which
 “x
“x0=exp 1 F y

f1(x0) P −
xQ−PQ −
x
Q 2 dy2 (5.8)

follows. Hence we can rewrite

dR
dx0 (x0)=exp 1 F f2(R(x0))

f1(x0) 1 P −
xQ−PQ −
x
Q 2 2:

x=x(x0,f1(x0), y) dy2

1−1 P
Q2 (x0,f1(x0)) f −
1(x0)

1−1 P
Q2 (x0,f2(R(x0))) f −
2(R(x0)). (5.9)

The second derivative of R is most easily calculated from this formula.
However, the general formula is very long. In the particular case x0=0 we
get (5.4) and (5.5) for RŒ(0) and Rœ(0). L

5.2. Generic Property of the hh Graphic of Saddle or Elliptic Type

Graphics through a nilpotent saddle point can be of two types: convex or
concave. We only consider the convex graphics. Let C be the convex hh
graphic of saddle type (see Fig. 13a). Let SŒ be a section transverse to the

368 ZHU AND ROUSSEAU

FIG. 13. The Poincaré first return map for the hh graphic of saddle or elliptic type.
(a) Return map (saddle type), (b) blow-up of the graphic, (c) return map (elliptic type),
(d) blow-up of the graphic.

connection C and parameterized by a regular C . coordinate. We will con-
sider the Poincaré first return map P: S Q SŒ with S … SŒ, a neighborhood
of C 5 SŒ.

Proposition 5.3. For the convex graphic of saddle or elliptic type and
-a ¥ A, the Poincaré first return map P(z) is at least C 1 for z \ 0 and

PŒ(0)=c g=exp 1 F .

−. div X(C(t)) dt2. (5.10)

Proof. We give the proof for the saddle case. For the elliptic case, the
proof is almost the same.
Consider the system

x˙ =y+ax 2

y˙ =y(x+e2x 2+x 3h(x))+y 2Q(x, y), (5.11)

FINITE CYCLICITY 369

where h(x) and Q(x, y) are C . and Q(x, y)=O(|(x, y)| N) for N suffi-
ciently large. To study the dynamics near the singularity at (0, 0), we make
the blow-up (3.6). Let y¯=1 in (3.6); we have

r˙=
1
2 r(x¯+rO(|(r, x¯)|)) :=P¯ (r, x¯)

x¯˙ =1 − (
1
2 −a) x¯ 2+rO(|(r, x¯)|) :=Q¯ (r, x). (5.12)

The system (5.12) has two singular points P3 and P4 and both are hyper-
bolic saddles (see Fig. 13b). The eigenvalues at P3 are (`2(1 − 2a)/(2(1 − 2a)),
−`2(1 − 2a)); the eigenvalues at P4 are (−`2(1 − 2a)/(2(1 − 2a)),
`2(1 − 2a)). Hence the hyperbolicity ratio at P3 (resp. P4)is s3(a)=
2(1 − 2a) (resp. 1/(s3(a))).
Take sections S¯ i={ri=r0}(i=3, 4), y¯3={x˜ 3=−x0}, and y¯4={x˜ 4=x0}
in the normal form coordinates in the neighborhood of P3 and P4, respec-
tively. For the Dulac maps near P3 and P4, we have

D¯ 4(x˜ 4)=x˜
 1
s3(a)
4 [c4+h4(x˜ 4)]

D¯ 3(r3)=r s3
3 [c3+h3(r˜3)], (5.13)

where c3, c4 are positive constants, c4c 1/s3
3 =1, and h3, h4 ¥ (I .
0 ).
Then we can decompose the Poincaré first return map P as

P=R p D¯ 3 p T¯ p D¯ 4, (5.14)

where T¯ : y¯4 Q y¯3 and R: S¯ 3 Q S¯ 4 are two regular transition maps in the
normal form coordinates.
For the transition map T¯ along r=0, the two sections become

y¯4=31 r, − 2

`1−2a
+x0+O(|(r, x0)| 224

y¯3=31 r, 2

`1−2a −x0+O(|(r, x0)| 224.

Note that for the system (5.12), along r=0, div X|r=0=−(1 − 2a) x¯ and
P¯ (0, x¯)=0, so by Proposition 5.1 we have T¯ Œ(0)=1. Thus we have

T¯ (r4)=r4+O(r 2
4). (5.15)

Therefore, by (5.13) and (5.15), if letting x˜ 4=D¯ 3 p T˜ p D¯ 4(x˜ 3), then

x˜ 4=x˜ 3+o(x˜ 3). (5.16)

370 ZHU AND ROUSSEAU

To calculate the map R, as in [7, 34, 14], we introduce two auxiliary
sections S˜ i={ri=r00} (i=3, 4) in the normal form coordinates. Then the
map R can be calculated by the decomposition

R=R40 p R¯ p R30, (5.17)

where R30: S¯ 3 Q S˜ 3 and R40: S˜ 4 Q S¯ 4 are regular transition maps. Similar
to T¯ Œ(0), for R30 and R40 we have

R −
30(0)=1 r00
r0 2 1− s3(a)

R −
40(0)=1 r0
r002 1− s3(a)
.
 (5.18)

For the transition map R¯ : S˜ 3 Q S˜ 4, using the original coordinates (r, x¯),
the two sections are

S˜ 3=31 r00, 2

`1−2a
+x¯+O(x¯ 2)+r00O(|(r, x0)|)24

S˜ 4=31 r00,− 2

`1−2a −x¯+O(x¯ 2)+r00O(|(r, x0)|)24.

So again by (5.2) in Proposition 5.1, we have

R¯ Œ(0)=exp 1 F T2

−T1 div X(C(t)) dt2.

Note that R is independent of r00,so

RŒ(0)= lim
r00 Q 0 R −
40(0) R¯ Œ(0) R −
30(0)= lim
r00 Q 0 exp 1 F T2

−T1 div X(C(t)) dt2

=exp 1 F .

−. div X(C(t)) dt2. (5.19)

Thus, by (5.17), (5.18), and (5.19), we have

R(x˜ 4)=exp 1 F .

−. div X(C(t)) dt2 x˜ 4+O(x˜ 2
4). (5.20)

It follows from (5.14), (5.16), and (5.20) that there holds

P(x˜ 3)=exp 1 F .

−. div X(C(t)) dt2 x˜ 3+o(x˜ 3);

thus we proved (5.10). L
 FINITE CYCLICITY 371

5.3. Main Theorem on the Convex Graphic of Saddle Type

For the convex graphic of saddle type, we have

Theorem 5.4. A convex hh graphic through a triple nilpotent saddle of
codimension 3 has finite cyclicity if the generic hypothesis PŒ(0) ] 1 is
satisfied.

For the proof, by changing the vector field X to −X if necessary, we
impose

Hypothesis 5.5. The convex hh graphic with a nilpotent saddle is
attracting:
 [H]:PŒ(0)=c g <1. (5.21)

After the global blow-up in Section 3.1, for the convex graphic through a
triple nilpotent saddle, we get a total of 10 families of convex graphics:
Sxhh1, Sxhh2, ..., Sxhh10 (see Table VI). For each family Sxhhi
(i=1, 2, ..., 10), the graphics fall into three groups:

• the upper boundary graphic: Sxhhia(i=1, 2, ..., 10);
• the intermediate graphics: Sxhhib(i=1, 2, ..., 10), Sxhh9d, and
Sxhh10d;
• the lower boundary graphics: Sxhhic(i=1, 2, ..., 10), Sxhh9e, and
Sxhh10e.

To prove the finite cyclicity of the convex graphic with a nilpotent saddle,
we have to prove that all the graphics listed above have finite cyclicity.

Notation 5.6. For convenience in the notation, in the remainder of
Section 5 and in Section 6, let r0, r0, and y0 be positive constants. We will
always use
 Si={ri=r0}, i=1, 2, 3, 4

Pi={ri=r0}, i=1, 2, 3, 4

yi={y˜ i=y0}, i=1, 2

yi={y˜ i=−y0}, i=3, 4
 (5.22)

to denote the sections in normal form coordinates (ri, ri,y˜ i) in the neigh-
borhood of the four singular points Pi (i=1, 2, 3, 4).

We begin with the upper boundary graphics.

372 ZHU AND ROUSSEAU

5.4. The Upper Boundary Graphics have Finite Cyclicity

Proposition 5.7. For the convex hh graphics of saddle type or hh
graphics of elliptic type, under the generic assumption, all the upper boundary
graphics have cyclicity one.
Proof. As shown in Fig. 14a, to prove the upper boundary graphic of
saddle type, we study the Poincaré first return map defined on the section
S4:
 P: S4 0 S4.

We can factorize it as
 P=R p G3 p T¯
43 p G −1
4 , (5.23)

where G4 and G3 are the second type of Dulac maps in the neighborhood
of P4 and P3, respectively; T¯
43 and R are the regular transition maps.
At P3, the eigenvalues are (1, −1, s3(a)), where for a ¥ (−.,0), s3(a)=
2(1 − 2a) > 0. By the normal form discussion in Proposition 4.6, depending
on whether a0 ¨ Q or a0 ¥ Q, the vector field near P3 has the normal form
of (4.8) or (4.9) with s=s3. Correspondingly, we use bi (i=1, 2, ..., N(k))
instead of using ai to make the distinction. In particular, b1=p3 − s¯ 3(a) q3.
By Theorem 4.14, the second type Dulac map G3=(t3, X3): y3 Q S3 has
the expression

t3(r3, r3)=n

X3(r3, r3)=g3 1 n, w 1 r3
r0 , b122+1 r3
r02 s¯3 5y0+h3(r3, r3, w 1 r3
r0 ,−b1)26,

(5.24)

FIG. 14. Upper boundary graphics of (a) saddle and (b) elliptic type.

FINITE CYCLICITY 373

where g3(n, w(r3/r0, b1))=(o3/r p3
0 ) n p3w(r3/r0, b1) and h3(r3, r3, w(r3/r0,
−b1)) satisfies the property (4.29). Due to the symmetry, the Dulac map
G4: y4 Q S4 has the same form as G3 in (5.24). Note that both s¯ 3 and s¯ 4
satisfy Lemma 4.13.
We calculate the transition T¯
43: y4 Q y3 using the polar coordinates
(x¯, y¯)=(r cos h,r 2 sin h) in the chart F.R.. Then we have

(1+sin 2 h)r˙=r cos h(a cos 2 h+sin 2 h+sin h)+O(r 2)

(1+sin 2 h) h˙=sin h((1 − 2a) cos 2 h −2 sin h)+O(r)

or
 dr
dh
=−r cos h(a cos 2 h+sin 2 h+sin h)
sin h((1 − 2a) cos 2 h −2 sin h)
+O(r 2).

Making the translation h=h¯+
p
2 , then

dr
dh¯=r sin h¯(a sin 2 h¯+cos 2 h¯+cos h¯)
cos h¯((1 − 2a) sin 2 h¯ −2 cos h¯)
+O(r 2)=f(h¯) r+O(r 2). (5.25)

Note that f(−h¯)=−f(h¯) and the two symmetric sections y3 and y4 corre-
spond to the two symmetric positions h¯=h¯0 and h¯=−h¯0. So integrating
(5.25) from h¯0 to − h¯0 gives that for n=0

r3=r4 exp 1 F h0

−h0 f(h¯)dh¯2+O(r 2
4)=r4+O(r 2
4). (5.26)

Let
 Tˆ =G3 p T¯
43 p G −1
4 . (5.27)

Easily we have Tˆ
1(n,y˜ 4)=n. Now we calculate the first derivative of Tˆ
2.
Note that by (5.24), we have

“
“r3 X3(r3, r3)=1 r3
r02 s¯3 −1 5y0+b1o3
r s¯3 −1
0 r p3
3 +hˆ 3 1 r3, r3, w 1 r3
r0 ,−b1226.

(5.28)

For X −1
4 (n,y˜ 4), we have

“
“y˜ 4 X −1
4 (n,y˜ 4)= 1
1 r4
r02 s¯4 −1 5y0+b1o4
r s¯3 −1
0 r p3
4 +hˆ 4 1 r4, r4, w 1 r4
r0 ,−b1226.

(5.29)

374 ZHU AND ROUSSEAU

Hence by (5.27), (5.28), (5.26), (5.29), and Lemma 4.13, we have that Tˆ
2
is at least C 1 and
 Tˆ −
2(0, 0)=1. (5.30)

We calculate the transition map R in the chart P.R.3. We have
R1(n,y˜ 3)=n. For the second component R2, as in Proposition 5.3, by using
the auxiliary sections and formula of [ALGM] in Proposition 5.2, we
obtain
 R −
2(0, 0)=c g. (5.31)

It follows from (5.23), (5.30), and (5.31) that we have

det P(0, 0)=c g.

By Hypothesis 5.5, c g <1. Hence the first return map P has at most one
fixed point; i.e., Cycl(Shhia) [ 1, i=1, 2, ..., 10.
In the above proof for the saddle case, we only use the fact that
1 − 2a>0. For the elliptic case with a ¥ (0, 1
2), the same proof gives that the
upper boundary hh graphic of elliptic type has finite cyclicity 1. L

5.5. Intermediate and Lower Boundary Graphics
Let C be any intermediate or lower boundary graphic of the 10 families.
To study its cyclicity, as shown in Fig. 15, take sections P3 and P4 (as
defined in (5.22)) in the normal form coordinates (ri, ri,y˜ i) (i=3, 4). We
are going to study the displacement map

L=R −1 −T: P4 Q P3 (5.32)

FIG. 15. Transition map for the intermediate hh graphics of saddle type.

FINITE CYCLICITY 375

or the displacement map
 L=R − T −1: P3 Q P4 (5.33)

where R: P3 Q P4 is the transition map along the regular orbit in the
normal form coordinates and T: P4 Q P3 is the transition map passing
through the blown-up singularity. Then by the derivation–division method
introduced by Roussarie in [30], we study the number of small roots of
L=0 or L=0. The maximum number of roots bounds the cyclicity.

Remark 5.8. Unless otherwise stated, due to the existence of an
invariant foliation, we focus our attention only on the second component.

We begin with the transition map R. Obviously R1(n,y¯ 3)=n. The second
component R2(n,y¯ 3) is almost affine (the two passages near P3 and P4 have
a ‘‘funneling effect’’ [14]).

Proposition 5.9. For any k ¥ N and -a0 ¥ A=(−1
2,0), there exist
A0 … A, a neighborhood of a0, and n1 >0 such that -(a, m¯) ¥ A0 × S 2 and
-n ¥ (0, n1), R2(n,y˜ 1) is C k and

(1) If a0 ¨ Q

R2(n,y˜ 3)=m340(n)1 n
n02 −s3+(c g+O(n ln n)) y˜ 3+ C

k

j=2 O(n j−1)y˜ j
3+O(n ky˜ k+1
3 ).

(2) If a0 ¥ Q

R2(n,y˜ 3)=c340 1 n, w 1 n
n0 ,−b122+ C

k

i=1 c34i 1 n, w 1 n
n0 ,−b122 y˜ i
3+O(y˜ k+1
3 ),

(5.34)

where m340(0)=0, and

c340=m340(n) 1 n
n02 −s¯4+o3r0(c g −1) w 1 n
n0 ,−b12+o3O 1 n s¯3w 2 1 n
n0 ,−b122

c341=c g+O 1 n ln n
n02+O 1 n p¯3w q3 1 n
n0 ,−b12 ln n
n02

c34j=O 1 n ln n
n02+O 1 n p¯3 (1+[j−2
q3 ])w q3+1 −j−q3 [j−2
q3 ] 1 n
n0 ,−b12 ln n
n02,

j \ 2.

Also R −1
2 (n,y˜ 4) is C k and has precisely the same form as R2.

376 ZHU AND ROUSSEAU

Proof. We limit ourselves to the second case: a0 ¥ Q. Decompose the
transition map R as
 R:=D −1
4 p R34 p D3,

where Dj: Pj Q Sj (j=3, 4) are the two Dulac maps of the first type in the
normal form coordinates near P3 and P4, respectively, and R34: S3 Q S4 is
the regular transition map with second component

R342(n,y˜ 3)=m340(n)+ C

k

i=1 m34i(n)y˜ i
3+O(y˜ k+1
3 ), (5.35)

where m340(0)=0 and m341(0)=c g+O(n).
The system near P3 (resp. P4) has the form (4.8) or (4.9) with s=s3(a)
(resp. s=s4(a)). By Theorem 4.10, the Dulac maps Di (i=3, 4) have
second components

Di(n,y˜ i)=gi 1 n, w 1 n
n0 , b122+1 n
n02 s¯i 5y˜ i+ki 1 n,y˜ i, w 1 n
n0 , b1226,

(5.36)

where gi and ki have the same property as in (4.12).
Let
 yˆ 4=1 n
n02 −s¯4 5D4 (n,y˜ 4)− g4 1 n, w 1 n
n0 , b1226. (5.37)

Then by (5.36) and (5.37), we have

yˆ 4=y˜ 4+k4 1 n, w 1 n
n0 ,−b12,y˜ 42. (5.38)

Let
 y˜ 4=yˆ 4+f¯4 1 n, w 1 n
n0 ,−b12,yˆ 42

be the inverse of (5.38). Then f¯4 has the same property as k4.
If we use yˆ 4 as the variable, we can express the y− component of D −1
4 as

D −1
4 (n,y˜ 4)=yˆ 4+f¯4 1 n, w 1 n
n0 ,−b12,yˆ 42. (5.39)

FINITE CYCLICITY 377

Hence, for the second component of transition map R¯ , by (5.36), (5.35),
(5.39), and Lemma 4.13, a straightforward calculation gives the result. L

The following proposition will serve to treat the intermediate graphics
while the lower boundary graphics will require ad hoc methods in each
case.

Proposition 5.10. Assume that we have a convex hh graphic C of saddle
or elliptic type shown in Fig. 15. Let

T: P4 Q P3

be the transition map along the connection in the chart F.R. Then if T
satisfies one of the following conditions:

• T is the identity while the graphic is generic (i.e., c g <1);
• T −
2(0, 0) is sufficiently small or T −
2(0, 0) is sufficiently large;
• T2(0, y˜ 4) is nonlinear of order n,

then C has finite cyclicity.

Proof. We consider the displacement map L or its inverse defined in
(5.32). By Proposition 5.9, the second component R2(n,y˜ 3) of R is almost
affine, yielding the results. C has cyclicity [ 1 in the first two cases and
cyclicity [ n in the third. L

It seems a priori difficult to show that a transition map is nonlinear. For
all the cases, we will deal with families of graphics. This allows an interest-
ing observation which we state in the following proposition.

Proposition 5.11. It is possible to choose normalizing coordinates near
P3 and P4 such that y˜ i(0, ri,yi) (i=3, 4) is analytic.

Proof. We modify the normalization process. For both the saddle or
elliptic cases, the vector field near P3 can be written as

r˙=r

r˙ =−r

y˙=−s3(a) y+h(a, m¯,r, r, y),
 (5.40)

where h(a, m¯,r, r, y)=o(|r, r,y|) and for both the saddle A=(−1
2,0) or
the elliptic A=(0, 1
2) case, we have s3(a)=2(1 − 2a) > 0.
Let us consider (5.40) for r=0. Then we get

r˙ =−r

y˙=−s3(a) y+h(a, m¯,0, r, y). (5.41)

378 ZHU AND ROUSSEAU

For the subfamily (5.41), the tuple of eigenvalues (−1, −s3(a)) is in the
Poincaré domain, the subfamily has no (resp. one) resonant monomial
when s3(a0) ¨ N (resp. s3(a0) ¥ N). Hence there exists an analytic map

Y=y+fˆ (r,y) (5.42)

which brings the family (5.41) into the normal form

r˙ =−r

Y˙ =−s3(a) Y+o3r p3, (5.43)

where p3=s3(a0), and, if s3(a0) ¨ N, then o3=0.
Applying the map (5.42) to the original family (5.40) brings the system to
the form
 r˙=r

r˙ =−r

Y˙ =−s3(a) Y+o3r p3+rH(a, m¯,r, r, Y).
 (5.44)

For the system (5.44), by Proposition 4.6, -(a, m¯) ¥ A×V, there exists a C k

map of the form
 y˜ =Y+rf¯(r, r,Y) (5.45)

which brings system (5.44) into the normal form (4.8) or (4.9). L

Corollary 5.12. Analytic extension principle. Assume that -a0 ¥ A
and m¯ 0 ¥ V(V … S 2), we have a family of graphics of the saddle (convex) or
elliptic type which only differ by a segment joining two nodes (Fig. 15). Let
C be any intermediate graphic in the family. Then -(a, m¯) ¥ A×V, the
normal form coordinates y˜ 3,y˜ 4 can be taken so that y˜ i(0, r,yi) is analytic.
Take sections P3 and P4 in the normal form coordinates in the neighborhood
of P3 and P4, respectively. Let C 5 P4=(0, y˜ g
4 ). Consider the transition map
associated with the graphic C

T: P4 Q P3

(n,y˜ 4) W (n,T2(n,y˜ 4)).

If -(a, m¯) ¥ A×V, T2(0, y˜ 4) is nonlinear in the neighborhood of y˜ g
4 , then its
analytic extension in its extension domain I in R is nonlinear at any particu-
lar value of y˜ 4 ¥ I for (a, m¯) ¥ A×V.

Proof of Theorem 5.4. There are 10 families of convex graphics of
saddle type (Table VI). We have proved in Proposition 5.7 that all the

FINITE CYCLICITY 379

upper boundary graphics have finite cyclicity, so we need to prove that in
each family all the intermediate and lower boundary graphics have finite
cyclicity.
For each lower boundary graphic, we will study the number of roots for
the corresponding displacement map L=R −1 −T or L: R−T −1 defined in
(5.32) or (5.33). Let C be any intermediate graphic of the corresponding
family and let T: P4 Q P3 be the transition map associated with the
graphic C in the chart F.R. We will apply Proposition 5.10 to the graphic
C. Usually if the criterion that T is nonlinear is used, the starting point is
chosen near the lower boundary graphic.
The map R satisfies Proposition 5.9 and R2 is almost affine. For
the transition map T, since r=0 is invariant in the chart F.R., then
T1(0, y˜ 3)=0. We will go over all 10 families of graphics by considering the
second component T2(0, y˜ 3) or its inverse.
For each family of the graphic Sxhhi (i=1, 2, ..., 10), we use Vi … S 2 to
denote the set of m¯ in which the family Sxhhi exists.
(1) Family Sxhh1. As shown in Fig. 16a, family Sxhh1 has a lower
boundary graphic Sxhh1c which passes through a hyperbolic saddle point
in the chart F.R. Using the good properties of R2 the proof is almost the
same as for the finite cyclicity of a homoclinic loop except for the following
points.
Let l0(m¯ 0) be the hyperbolicity ratio at the saddle point. If l(m¯ 0) ] 1,we
find Cycl(Sxhh1c) [ 1.If l(m¯ 0)=1 and a ] − 1
2, we need to calculate the
first saddle quantity of the saddle point of system (3.10). Using the formula
in [7], we find it is
 a02= 2a(a − 1)(1+2a) 2

a(4a − 1) m¯ 2
30 − (1+2a) 2 m¯ 20 m¯ 30. (5.46)

FIG. 16. Transition map T for the family (a) Sxhh1 and (b) Sxhh2.

380 ZHU AND ROUSSEAU

Then we have two cases

•If m¯ 30 ] 0: The lower boundary graphic Sxhh1c is studied as a
homoclinic loop for which the first saddle quantity is nonzero. Then
Cycl(Sxhh1c) [ 3. Moreover, near the lower boundary graphic T '
2 (0, y˜ 4)
] 0, T2 is nonlinear in y˜ 4. By Proposition 5.10, we have that Cycl(Sxhh1b)
is finite.
•If m¯ 30=0: In this case l(m¯ 0)=1 implies that the system (3.10) is
symmetric with respect to the y-axis. The lower boundary graphic is treated
as a homoclinic loop for which the first derivative is nonzero. Hence
Cycl(Sxhh1c) [ 2.

(2) Families Sxhh2 and Sxhh3. For the family Sxhh2, system (3.10)
has a semihyperbolic saddle on Sxhh2c (Fig. 16b). Consider the map D¯=
(d¯,D¯ ): S¯ 1 Q S¯ 2. In this case for n=0, D¯ is the stable center transition near
the semihyperbolic saddle. Then by [12], -i1,i2 ¥ N, -(a, m¯) ¥ A0 ×V20, and
n >0 sufficiently small, we have

“ i1D¯

“xˆ i1 (n,xˆ )=O(xˆ i2). (5.47)

So for T2, by (5.47) we have T −
2(0, y˜ 4) Q 0 which gives Cycl(Sxhh2c) [ 1
and the nonlinearity of T2, hence the finite cyclicity of Cycl(Sxhh2b).
By changing (x, t) W (−x, −t), similar to family Sxhh2, the result holds
for the family Sxhh3.
(3) Families Sxhh4, Sxhh5, and Sxhh6. For the families Sxhh4,
Sxhh5, and Sxhh6, the corresponding lower boundary graphic has a saddle
connection S1S2.At S1 and S2, the hyperbolicity ratios are

S1: l1=
m¯ 3 −= − m¯ 2
a

2a = − m¯ 2
a
 ; S2: l2= −2a = − m¯ 2
a

m¯ 3+= − m¯ 2
a
 .

Families Sxhh4 and Sxhh6 correspond to m¯ 30 ] 0; i.e., l1l2 ] 1. The proof
is exactly the same as for a polycycle with two hyperbolic saddles [28];
yielding their cyclicity is at most 2.
The family Sxhh5 exists if and only if m¯=(0, 1, 0). Then system (3.10) in
the chart F.R. is symmetric with a center (Fig. 17). For the intermediate
graphics, we easily see that, for n=0, the transition map T is the identity,
yielding by Proposition 5.10 that the graphic Sxhh5b has finite cyclicity.

FINITE CYCLICITY 381

FIG. 17. Transition map T for the family Sxhh5.

Now we consider the graphic Sxhh5c. The hyperbolicity ratios l1 and l2
satisfy l1=− 1
2a >1, l2=−2a < 1 and l1l2=1. By Proposition 4.2, the
Dulac maps defined in the neighborhood of the two saddles can be written
as
 D¯ 1(n,x1)=x l1
1 (1+f¯1(n,x1)

D¯ −1
2 (n,x2)=x
 1
l2
2 (1+f¯2(n,x2), (5.48)

where f¯i(n,xi) (i=1, 2) satisfies (I .
0 ) for (a, m¯) ¥ A0 ×V51, n ¥ (0, n1), and
xi sufficiently small.
Consider the displacement map

L: S¯ 1 0 S¯ 20

L=T¯
12 p D¯1 − D¯ −1
2 p T¯
32 p R −1 p T¯
14, (5.49)

where
 • T¯
12: S¯ 10 Q S¯ 20, T¯
122(n,y1)=m120(n)+(1+O(n)) y1+O(y 2
1);
• T¯
14: S¯ 1 Q P4, T¯
14(n,x1)=m140(n)+m141(n)x1+O(x 2
1);
• R −1: P4 Q P3, By Proposition 5.9 we have R −1
2 (n,y˜ 4)=
m340(n)+( 1
cg+O(n)) y˜ 4+O(y˜ 2
4);
• T¯
32: P3 Q S¯ 2, T¯
322(n,y˜ 3)=m320(n)+m321(n)y˜ 3+O(y˜ 2
3) and m321(0)
m141(0)=1 because of the symmetry of the system (3.10).

382 ZHU AND ROUSSEAU

Then a straightforward calculation gives

L2(n,x1)=e¯1(n)+x l1
1 (1+f¯11(n,x1))

−[e¯2(n)+c¯ g(n)x1+O(x 2
1)] 1
l2 (1+f¯21(n,x1)) (5.50)

where c¯ g(n)=(m321(n)m141(n)/c g)+O(n) ] 1 and f¯11, f¯21 ¥ (I .
0 ).
By (5.50),

L −
2(n,x1)=l1x l1 −1
1 (1+f¯12(n,x1))

− 1
l2 [e¯2(n)+c¯ g(n)x1+O(x 2
1)] 1
l2 −1 (c¯ g(n)+f¯22(n,x1)),

where f¯12, f¯22 ¥ (I .
0 ). L −
2(n,x1) has the same number of small roots x1 >0
as

L21(n,x1)=(l1l2)
 l2
1− l2 x
 (l1 −1) l2
1− l2
1 (1+f¯13(n,x1))

−[e¯2(n)− c¯ g(n)x1+O(x 2
1)](c¯ g l2
1− l2(n)+f¯23(n,x1)). (5.51)

Let b¯ 1=(1 − l1l2)/(1 − l2). For the term x (l1 −1) l2/(1 − l2)
1 , we make the
following development

x
 (l1 −1) l2
1− l2
1 =x 1− b¯ 1
1 =x1(1+b¯ 1w¯ ),

where w¯ =w(x1, b¯ 1).
By (5.51), we then have

L −
21(n,x1)=(l1l2)
 l2
1− l2 (1 − b¯ 1+b¯ 1(1 − b¯ 1) w¯ )(1+f¯14(n,x1))

−[c¯ g1+ l2
1− l2+O(x1)](1+f¯24(n,x1)) (5.52)

which has the same number of zeroes as

L22(n,x1)=1 − b¯ 1 − cˆ g(n)+O(n)+b¯ 1(1 − b¯ 1) w¯ +O(x1), (5.53)

where cˆ g(n)=c¯ g1/(1 − l2)/(l1l2) l2/(1 − l2) and cˆ g(0)=c g.
Let L23=L22/w¯ ; then

L23=
1− b¯ 1 − cˆ g(n)+O(n)
w¯ +b¯ 1(1 − b¯ 1)− O(x1)
w¯ .

If we differentiate L23 and let L24=w¯ 2x 1+b¯ 1
1 L −
23, then

L24=[ − 1+b¯ 1+cˆ g(n)+O(n)]+O(x1).

FINITE CYCLICITY 383

FIG. 18. Transition map T for the families (a) Sxhh9 and (b) Sxhh10.

Since cˆ g(0)=c g ] 1, then -(a, m¯) ¥ A0 ×V51 and for n >0 sufficiently small,
we have that L24 does not vanish. So L=0 has at most three roots which
gives Cycl(Sxhh5c) [ 3.
(4) Families Sxhh7 and Sxhh8. The proof is exactly the same as for
the finite cyclicity of a graphic through a saddle node and a hyperbolic
saddle of the same attracticity. As in [12], the cyclicity is [ 1.
(5) Families Sxhh9 and Sxhh10. As shown in Fig. 18a, the family
Sxhh9 has two subfamilies of graphics: intermediate graphics Sxhh9b and
Sxhh9d and two boundary graphics Sxhh9c and Sxhh9e.
First note that the graphic Sxhh9c that passes by an attracting saddle
node has the same structure as the graphic Sxhh2c, so we only need to
consider the lower boundary graphic Sxhh9e. The proof of its finite cycli-
city is the same as that of a graphic through a hyperbolic saddle and a
saddle node with central transition (see [12]).
For the intermediate graphics Sxhh9d, the transition map T along the
graphic can be factorized as two regular transition maps and a central
transition map. Obviously, T2(n,y˜ 4) has a first derivative which is small;
thus Cycl(Sxhh9d) is finite.
For family Sxhh10 we change (x, t) W (−x, −t). L

6. FINITE CYCLICITY OF GRAPHICS WITH A NILPOTENT
SINGULARITY OF ELLIPTIC TYPE

6.1. Finite Cyclicity of pp Graphics of Elliptic Type.

In Table III, we have three families of pp graphics of elliptic type: Epp1,
Epp2, and Epp3. All the pp-graphics have no return map. For the passage

384 ZHU AND ROUSSEAU

near the blown-up sphere r=0 we have system (3.10) in the chart F.R. Let
Vi (i=1, 2, 3) be the set of parameters in which Eppi exists.
The following proposition will be important in proving the finite cyclicity
of pp and hh graphics of elliptic type.

Proposition 6.1. Let S2 be the second component of the transition map
S: P1 Q P2 in the normal form coordinates. Then -(a, m¯) ¥ A×VI1 and n >0
sufficiently small, we have

“S2
“y˜ 1 (0, 0)=exp 1 pm¯ 3
`am¯ 22+O(r0)

“ 2S2
“y˜ 2
1 (0, 0)= 1
a(1 − 2a) e
 pm¯3
`am¯2[1−e
 pm¯3
`am¯2]+O(r0).
 (6.1)

Proof. The transition map S can be factorized as

S=Y2|P2 p F02|P2 p S¯ p F10|P1 p Y −1
1 |P1 , (6.2)

where
(1) Y1 and Y2 are the C k-coordinate changes normalizing the vector
fields (3.8) at P1 and P2 respectively,

Y −1
1 |P1 :˛
r1= n
r0

y¯ 1=b11y˜ 1+b12y˜ 2
1+O(y˜ 3
1)

Y2|P2 :˛
r2= n
r0

y˜ 2=b21y¯ 2+b22y¯ 2
2+O(y¯ 3
2)

where b1i and b2i(i=1, 2) are functions of ri, ri, respectively. On the
sections P1 and P2, we have r1=r2=r0,soon r=0, we have

b11=1+
m¯ 3
a r0+O(r 2
0)

b12=− 1
a(1 − 2a)
+O(r0)

b21=1+
m¯ 3
a r0+O(r 2
0)

b22= 1
a(1 − 2a)
+O(r0).

FINITE CYCLICITY 385

(2) F10 and F02 are coordinate changes between charts P.R.1 and
F.R. and F.R. and P.R.2, respectively. On the corresponding sections, they
are linear:
 F10|P1 :˛
x¯=− 1
r0

y¯=y˜ 1
r 2
0 ,
 F02|P1 :˛
r2= n
r0

y˜ 2=r 2
0y¯.

(3) S¯:{x¯=−x0} Q {x¯=x0} is the transition map in the original
coordinates (x¯, y¯) in the chart F.R., where x0=1/r0.
For m¯ ¥ VI1 , system (3.10) has no singular points on the invariant line
y¯=0,so S¯2 is a C k regular transition map

S¯2(n,y¯)=m0(n)+m1(n)y¯+m2(n)y¯ 2+O(y¯ 3), (6.3)

where m0(0)=0. For the coefficients m1(n) and m2(n), by Proposition 5.2,
we have

m1(0)=exp 1 F x¯0

−x¯0
 x¯+m¯ 3
ax¯ 2+m¯ 2 dx¯2=exp 1 2m¯ 3
`am¯ 2 arc tan ax¯0
`am¯ 22,

m2(0)=m1(0) F x¯0

−x¯0 − 2(x¯+m¯ 3)
(ax¯ 2+m¯ 2) 2 exp 1 F x¯

−x¯0
 x¯+m¯ 3
ax¯ 2+m¯ 2 dx¯2 dx¯=m1(0) I12(x¯0),

where
 I12(x¯0)=
e
 m¯3
`am¯2 arc tan ax¯0
`am¯2
(ax¯ 2
0+m¯ 2) 1
2a F x¯0

−x¯0
 −2(x¯+m¯ 3)e
 m¯3
`am¯2 arc tan ax¯

`am¯2
(ax¯ 2+m¯ 2) 2− 1
2a dx¯.

By L’Hospital’s rule,

lim
x¯0 Q . I12(x¯0)(ax¯ 2
0+m¯ 3)= 2
1−2a (1−e
 pm¯3
`am¯2).

So
 I12(x¯0)= 2
a(1 − 2a) (1−e
 pm¯3
`am¯2) 1
x¯ 2
0+o 1 1
x¯ 2
02.

Therefore, for x¯0= 1
r0 and r0 >0 small, we have

m1(0)=e
 pm¯3
`am¯2+O(r0)

m2(0)= 2
a(1 − 2a) e
 pm¯3
`am¯2(1−e
 pm¯3
`am¯2) r 2
0+o(r 2
0)}.

386 ZHU AND ROUSSEAU

Then by (1), (2), (3), and (6.2), we have

“ 2S2
“y˜ 2
1 (0, 0)= 1
a(1 − 2a) e
 pm¯3
`am¯2[1−e
 pm¯3
`am¯2]+O(r0). L

Let C be any pp graphic in the family. To prove its finite cyclicity, as
shown in Fig. 19, we take sections S1 and S2 in normal form coordinates
in the neighborhood of P1 and P2, respectively. We study the displacement
maps
 L=R −1 −T or L=R − T −1, (6.4)

where R: S2 Q S1 is the regular transition map along the regular orbit and
T: S1 Q S2 is the transition passing through the blown-up nilpotent elliptic
singularity.
For the transition map T, similar to Proposition 5.9, the passage from P1
to P2 has a funneling effect, i.e., its second component T2 is almost affine.

Proposition 6.2. There exists e0 >0 such that for any k ¥ N, a0 ¥ (0, 1
2),
there exist A0 … (0, 1
2), a neighborhood of a0 such that for -(a, m¯) ¥ A0 ×VI3 ,
T −
2(0, 0) is sufficiently small, while for (a, m¯) ¥ A×VI2 , T −1
2 (0, 0) is suffi-
ciently small. For any (a, m¯) ¥ A0 ×VI1 and n >0 sufficiently small, the second
component T2(n,y¯) of T is C k and

T2(n,y˜ 1)=c120 1 n, w 1 n
n0 ,−a022+ C

k

i=1 c12i 1 n, w 1 n
n0 ,−a022 y˜ i
1

+O 1 n p¯1 (1+[k−2
q1 ])w q1+1 −k−q1[k−2
q1 ]) 1 n
n0 ,−a02 ln n
n0 y˜ k+1
1 2 (6.5)

FIG. 19. Displacement maps for pp graphics. (a) Epp1, (b) Epp2, (c) Epp3.

FINITE CYCLICITY 387

where

c120=m120(n) 1 n
n02 −s¯2+o1r p1
0 (1 − m121(n)) w 1 n
n0 , a12

+O 11 n
n02 s¯1 w 2 1 n
n0 ,−a022

c121=m121(n)+O 1 n ln n
n02+O 11 n
n02 p¯1 w q1 1 n
n0 ,−a02 ln n
n02

c12i=O 1 n ln n
n02+O 1 n p¯1(1+[i−2
q1 ])w q1+1 − i − q1[i−2
q1 ]) 1 n
n0 ,−a02 ln n
n02,

i \ 2

and m120(0)=0, m121(0)=exp(pm¯ 3/`am¯ 2).

Theorem 6.3. We consider a pp graphic with a triple nilpotent elliptic
point of any codimension. If the second component R2 of the regular transi-
tion map R has its nth derivative nonvanishing, then Cycl(Epp) [ n.

Proof. There are three types of pp limit periodic sets through a nilpo-
tent elliptic point. We write

R2(n,y˜ 1)= C

k

i=0 c˜i(n)y˜ i
1+o(y˜ k
1), (6.6)

where c˜0(0)=0 and c˜1(0), c˜n(0) ] 0.
So for the displacement map L in (6.4), we have L1(n,y˜ 1)=0 and

L2(n,y˜ 1)= C

k

i=0 5c12i 1 n, w 1 n
n0 ,−a022 − c˜i(n)6 y˜ i
1+O(y˜ k+1
1 ). (6.7)

For the graphic Epp3, c121(n, w) sufficiently small, so we have

“L2
“y˜ 1 (n,y˜ 1)=c121 1 n, w 1 n
n0 ,−a022 − c˜1(n)+O(y˜ 1) ] 0,

which gives Cycl(Epp3) [ 1. Similarly Cycl(Epp2) [ 1.

388 ZHU AND ROUSSEAU

For the graphic Epp1, if we choose k \ n, then by (6.5) and (6.7),
-(a, m¯) ¥ A0 ×VI1 and -n ¥ (0, n1), there holds

“ nL2
“y˜ n
1 (n,y˜ 1)

=−n! c˜n(n)+1 n n
n02+O 1 n p¯1 (1+[n−2
q1 ]w q11+1 − n+q1[n−2
q1 ] 1 n
n0 ,−a02 ln n
n02

+O(y˜ 1)

] 0.

So by Rolle’s theorem, for any (a, m¯) ¥ A0 ×VI1 and -n ¥ (0, n1), L2(n,y˜ 1)
=0 has at most n small roots in the neighborhood of y˜ 1=0; i.e.,
Cycl(Epp1) [ n. L

Proposition 6.4. In Theorem 6.3, for the transition map R we assumed
that for n \ 2, R (n)
2 (0, 0) ] 0. This assumption is intrinsic.

Proof. The ideas come from [17]. By saying that the assumption
R (n)
2 (0, 0) ] 0 (n \ 2) is intrinsic we mean that this property depends neither
on the choices of coordinate changes which bring the system near P1 and P2
to normal forms nor on the choice of the sections parallel to the coordinate
axes in the normal form coordinates.
In the coordinates (r1, r1,y˜ 1), the system near P1 has the normal form
(4.8) or (4.9). The Dulac map D1: S1 Q P1 has the form (4.11). Assume
that by an another ‘‘nearly-identity’’ change of coordinates, we bring the
system near P1 into the same normal form with coordinates (r1, r1,y˜˜ 1). Let
S˜ 1={r1=r10} and P˜ 1={r1=r10} be two sections parametrized by the
new normal form coordinates y˜˜ 1 and let D˜˜ 1=(d˜˜,D˜˜ 1) be the Dulac map
S˜ 1 Q P˜ 1 in the new normal form coordinates. Then D˜˜ 1 has the same form
as D1 in (4.11), and we should have

D˜˜ 1(n,y˜˜ 1)=Fˆ 11 p D1 p F˜ 11(n,y˜˜ 1) or

D˜˜ 1 p F˜ −1
11 (n,y˜ 1)=Fˆ 11 p D1(n,y˜ 1), (6.8)

where
 F˜ −1
11 (n,y˜ 1)=(n, f˜ −1
11 ): S˜ 1 Q S1

Fˆ 11(n,y˜ 1)=(n, fˆ 11): P1 Q P˜ 1

FINITE CYCLICITY 389

are the compositions of coordinate changes and C k regular transitions,
respectively. Let
 f˜ −1
11 (n,y˜ 1)= C

k

j=0 m˜ 11j(n)y˜ j
1+O(y˜ k+1
1 )

fˆ 11(n,y˜ 1)= C

k

j=0 mˆ 11j(n)y˜ j
1+O(y˜ k+1
1 ),
 (6.9)

where m˜ 111(0) > 0 and mˆ 111(0) > 0.
We only consider the most difficult case a0 ¥ Q 5 A. Substituting (6.9)
and the expressions for D1, D˜˜ 1 into the second equation of (6.8), we have

g1 1 n, w 1 n
n0 ,−a122+1 n
n02 s¯1 5f˜ −1
11 (n,y˜ 1)+f1 1 n, w 1 n
n02, f˜ −1
11 (n,y˜ 1)26

=g¯1 1 n, w 1 n
n0 ,−a122

+ C

k

j=0 mˆ 11j(n) 5g¯1 1 n, w 1 n
n0 ,−a122

+1 n
n02 s¯1 1 y˜ 1+f¯1(n, w 1 n
n0 − a12,y˜ 1226 j

+O(y˜ k+1
1 ). (6.10)

Equating the coefficient of monomial y˜ j
1 on both sides of (6.10), we get a
series of equations about mˆ 11j and m˜ 11j. Then for j=2, 3, ..., k, we have
1 n
n02 s¯1 5m˜ 11j(n)+o 11 n
n02 s¯126=mˆ 11j(n) 1 n
n02 js¯1+o 11 n
n02 (j − 1) s¯12. (6.11)

Then by (6.11), for 2 [ j [ k, we have

m˜ 11j(n)=1 n
n02 s¯1 mˆ 11j(n)+o 11 n
n02 s¯12.

Therefore we get
 m˜ 11j(0)=0, j=2, 3, ..., k. (6.12)

Let
 F˜ 22(n,y˜ 2)=(n, f˜ 22): S˜ 2 Q S2

390 ZHU AND ROUSSEAU

be the corresponding composition of coordinate change and a C k regular
transition map. If we denote

f˜ −1
22 (n,y˜ 2)=y˜ 2+ C

k

j=2 m˜ 22j(n)y˜ j
2+O(y˜ k+1
2 ),

then similar to (6.12), we get

m˜ 22j(0)=0, j=2, 3, ..., k. (6.13)

Let R˜˜ : S˜ 1 Q S˜ 2 be the transition map in the new normal form coordi-
nates; then we have
 R˜˜ =F˜ −1
22 p R p F˜ −1
11 . (6.14)

It follows from (6.12), (6.13), and (6.14) that one finds a constant C¯ >0
such that R˜˜ (n)
2 (0, 0)=C¯ R (n)
2 (0, 0) by which we finish the proof. L

Remark 6.5. In the new normal form coordinates (ri, ri,y˜˜ 1) (i=1, 2),
the second component of the transition map T is still almost affine.

6.2. Finite Cyclicity of hp Graphics of Elliptic Type

Theorem 6.6. A hp graphic with a triple nilpotent singularity for which
a ] 1
2 has finite cyclicity.

Proof. We consider the concave hp graphic. We will study the cyclicity
of all the graphics listed in Table IV.
(1) Graphics Ehp1, Ehp2c, and Ehp3. As shown in Fig. 20, take
sections y2 and P2 (Notation 5.6). We study the displacement map defined
on y2,
 L: y2 Q P2

L=T˜ −Tˆ , (6.15)

FIG. 20. Displacement maps for graphics (a) Ehp1, (b) Ehp2c, and (c) Ehp3.

FINITE CYCLICITY 391

where T˜ is the transition map along the graphic and Tˆ =G2 is the second
type of Dulac map near P2.
On y2, the coordinates are (r2, r2) with r2r2=n, n >0 small and
invariant. We want to cover a domain |r2|< e,|r2|< e, where e >0 small.
Then n [ e 2.So -u ¥ (0, 1), on the curve n=ue 2, we have r2r2=ue 2.
Therefore r2, r2 ¥ (ue, e). Let

r2=n 1−d, r2=n d. (6.16)

We then parameterize the section y2 using the coordinates (n,d) ¥
(0, e 2)× In, where In=(ln e
ln n, ln ue
ln n ) … (0, 1) and n=ue 2.
To prove the finite cyclicity of the graphics, we are going to prove that
the two functions T˜
2(n,d) and Tˆ
2(n,d) have different convexity, i.e.,
T˜ '
2 (n, d)<0 and Tˆ '
2 (n, d)>0, which will yield Cycl(Ehp1, Ehp3) [ 2.
We calculate Tˆ '
2 (n,d) first. Using coordinates (n,d) on section y2, for
Tˆ =G2=(t2, X2), by Theorem 4.14, we have

X2(n, d)=g2 1 n, w 1 n d

r0 , a122+n s¯2d 5l1+h2 1 n, n d, w 1 n d

r0 ,−a1226

(6.17)

where l1=y0/r s¯1
0 >0, g2(n, w(n d/r0, a1)) =(o3/r p1
0 n p1) w(n d/r0, a1), and
h2(n, n d, w(n d/r0,−a1)) is C .. Also -(a, m¯) ¥ A0 × S 2, for d ¥ (0, 1) and
n >0 sufficiently small, we have uniformly

“ ih2
“d i 1 n, n d, w 1 n d

r0 ,−a122=O 1 n p1dw 1 n d

r0 , a12 (ln n) i2,i \ 0. (6.18)

We also have

“
“d g2 1 n, w 1 n d

r0 , a12=− o1
r p1 − a1
0 n p1n −a1d ln n=− o1
r s¯1
0 n s¯1dn p1(1 − d) ln n. (6.19)

Note that -d ¥ (ln e
ln n , ln ue
ln n ), n 1−d ¥ (ue, e) and n p1(1 − d) ¥ (0, e p1), so if we dif-
ferentiate Tˆ
2(n,d) twice with respect to d, then we have

Tˆ '
2 (n, d)=n s¯2d(ln n) 2 5s¯ 2
2l1+a1 o1
r s¯2
0 n p1(1 − d)+hˆ 21 1 n, n d, w 1 n d

r0 ,−a1226,

(6.20)

yielding -(n,d) ¥ (0, e 2)× In with e >0 sufficiently small, Tˆ '
2 (n, d)>0.
Now, for T˜
2(n,d), we make the decomposition

T˜ =S p D1 p R p G3 p V, (6.21)

392 ZHU AND ROUSSEAU

where
 • D1 is the first type of Dulac map near P1. It satisfies Theorem 4.10
with s=s1(a),
• G3 is the second type of Dulac map near P3. It satisfies
Theorem 4.14 with s=s3(a): Using coordinates (n,r3) on the section y3
defined in normal form coordinates by {y˜ 3=−y0}, the second component
of G3 is

X3(n,r3)=g3 1 n, w 1 r3
r0 , b122+r s¯3
3 5 −l3+h3 1 n,r3, w 1 r3
r0 ,−b1226,

(6.22)

where l3=y0/r s¯3
0 >0 and h3(n,r3, w(r3/r0,−b1)) satisfies a similar
property as h2 in (6.18).
• S: P1 Q P2 is the transition map defined in Proposition 6.1 with
S2 in (6.3),
• R: S3 Q S1 is a C k regular transition map

R2(n,y˜ 3)=m310(n)+m311(n)y˜ 3+O(y˜ 2
3), (6.23)

where m310(0)=0 and m311(0) > 0,
• V: y2 0 y3 is a C k regular transition map which can be written as

V1(r2, r2)=r2[m231+O(|(r2, r2)|)]

V2(r2, r2)=r2[mˆ 231+O(|(r2, r2)|)], (6.24)

where m231(0), mˆ 231(0) > 0 are constants.

Let
 r3=n 1−d[m231+O(|(n d, n 1−d)|)]. (6.25)

Then for the transition map T˜ , by (6.21) and using coordinates (n,d) on
the section y2, a straightforward calculation gives

T˜
2(n, d)=d00(n)+d01(n) n s¯1+p3w(r3,−b1)(1+O(n p3w(r3,−b1)))

+d11(n) n s¯1r s¯3
3 [1+h31(n,r3, w(r3,−b1))], (6.26)

FINITE CYCLICITY 393

where
 d00(n)=m0(0)+m310(n) 1 n
n02 s¯1+O 11 n
n02 s¯1w 1 n
n0 ,−a122

d01(n)=m1(n)m311(n)

d11(n)=−l3m1(n)m311(n)
n s¯1
0 <0,
 (6.27)

m1(n) is large for Ehp2c and small for Ehp3.
Note that if q3=1, p3 − b1=s¯ 3 and n 1−dn p3n −(1 − d)(1+b1)=n p3dn s¯3(1 − d). A
first derivative of T˜
2(n,d) gives

T˜ −
2(n, d)=−n s¯3(1 − d)d11(n) n s¯1 ln n(1+O(n d, n 1−d))
5s¯ 3m s¯3
231+O(n p3d)+h33 1 n, n d, w 1 m231 n 1−d

r0 ,−b1226. (6.28)

where h33 has the same property as h31.
Therefore for T˜ '
2 (n,d), we have

T˜ '
2 (n, d)=n s¯1n s¯3(1 − d)d11(n)(ln n) 2 (1+O(n d, n 1−d))
5s¯ 3m s¯3
231+O(n p3d)+h34 1 n, n d, w 1 m231 n 1−d

r0 ,−b1226 (6.29)

where d11(n)<0.So -(n,d) ¥ (0, e 2)× In with e >0 sufficiently small,
T˜ '
2 (n, d)<0.

Remark 6.7. For the hp graphics Ehp1, Ehp3, and Ehp2c considered
above, we studied the displacement maps defined on the section y2 which is
transverse to the passage from P2 to P3 along the equator. Since n=r2r2 is
invariant, on y2 we have r2=n/r2. So it is the passage from P2 to P3 along
the equator which forces the two functions T˜
2 and Tˆ
2 to have different
convexity. Similar phenomenon happens on the passage from P1 to P4.
Therefore, if a graphic contains exactly one of these two passages and has a
structure similar to that of Ehp1, then it has finite cyclicity 2.

(2) Cyclicity of graphic Ehp2a. As shown in Fig. 21a, Ehp2a is a hp
graphic through a repelling saddle node. The composition of T31 with the
two Dulac maps of type one is similar to the passage near an attracting
saddle node. Hence the proof is exactly the same as for a graphic through
two saddle nodes, one with central transition and one with center-unstable
transition and uses the Khovanskii procedure [15, 38].

394 ZHU AND ROUSSEAU

FIG. 21. Displacement maps for graphics (a) Ehp2a, (b) Ehp2b, and (c) map T.

(3) Cyclicity of graphic Ehp2b. As in Fig. 21b, let S¯ 1={x˜=−x0}
and S¯ 2={x˜=x0} be two sections transversal to the graphic Ehp2b, and
consider the displacement map
 L: S¯ 2 Q S¯ 1

L:=D¯0 −T¯
31, (6.30)

where D¯0(n,x˜ )=(d¯
0,D¯ 0): S¯ 2 0 S¯ 1 is the central transition near the saddle
node in the normal form coordinates (x˜, y˜), and

D¯ 0(n,y˜ )=m(mˆ 2)y˜, lim
mˆ 2 Q 0 m(mˆ 2)=0. (6.31)

T¯
31 is the transition along the flow of the graphic which can be factorized as

T¯
31: S¯ 2 Q S¯ 1

(n,x˜) Q (n,T¯
312)

T¯
31=T¯
10 p D1 p R p D3 p T¯
03,
 (6.32)

where especially T¯
03: S¯ 2 Q P3 is a regular transition map in normal form
coordinates which can be written as

T¯
031(n,y˜)= n
r0

T¯
032(n,y˜)=m030(n)+ C

n

i=1 m03i(n)y˜ i+O(y˜ n+1),

where m030(0)=0.

Lemma 6.8. We consider the vector field

x˙ =y+ax 2

y˙ =y(x+1) (6.33)

FINITE CYCLICITY 395

with a saddle node at the origin and a singular point P at infinity given by
(u, z)=(
1−2a
2 ,0), where (u, z)=(y/x 2, 1
x) (Fig. 21c). Let (x˜, y˜) be normal
coordinates near the origin and (u˜, z˜) be normal coordinates near P. Then the
transition map
 T: {x˜=x0} Q {z˜=z0}

is nonlinear at any point y˜ 0 of {x˜=x0}; i.e., -y˜ 0, there exists n \ 2 such that

d nT
dy˜ n (y˜ 0) ] 0. (6.34)

Proof. The proof is very similar to that in Proposition 5.11. The argu-
ment lies essentially in the fact that it is possible to choose normalizing
coordinates near the saddle node so that the intersection of the section S¯ 2
with n=0 is an analytic section in the original coordinates. This highly
nontrivial fact was explained to us by Y. Ilyashenko. The proof will appear
in [8]. The Appendix contains a statement of the results. Also as in Prop-
osition 5.11 we can suppose that the section P3 is analytic. Then it suf-
fices to prove that the transition map T: S¯ 0 Q p3 is nonlinear at one point,
where S¯ 0={x˜=x0}. This will be done by considering the asymptotic
expansion of T near y˜=0 on the lower boundary graphic (Fig. 21c). Then

T=S3 p V¯ p G¯ −1
2 p S¯, (6.35)

where S¯ and V¯ are regular. Since we are in the invariant subspace r=0,
then by Remark 4.16 we have

G¯ −1
2 (y˜ 2)=˛
y˜
 1
s1
2 if s1(a0) ¨ Q

y˜
 1
s1
2 51+ C

k

i=1 aiy˜ ip
2 w(y˜ 2, a1)+o(y˜ kp
2 )6 if 1
s1(a0)
=
p
q ¥ Q,

(6.36)

where a1=p/q − 1/s1. A direct calculation yields that

S3(r3)= 1
r s3
3 (−C1+C2o3 ln r3), (6.37)

where C1, C2 are positive constants and o3=0 if s3(a0) ¨ N.
By (6.35)–(6.37), it is then clear that T sends a neighborhood of y˜=0 to
a neighborhood of .. No affine maps can have this property. Hence T is
nonlinear at each point in a neighborhood of y˜=0. By analytic extension,
it is nonlinear at every point of S¯ 0. L

396 ZHU AND ROUSSEAU

End of proof of Theorem 6.6. By Lemma 6.8, there exists n \ 2 such
that “ nT032/“y˜ n(0, 0)=m˜ 03n ] 0. Then for the transition map T¯
31, we have

T¯
312(n,y˜)

=c310 1 n, w 1 n
n0 ,−a12, w 1 n
n0 ,−b122

+1 n
n02 s¯1+s¯3 5 C

n

i=1 c31i 1 n, w 1 n
n0 ,−a12, w 1 n
n0 ,−b122 y˜ i+O(y˜ n+1)6.

(6.38)

where for n >0 sufficiently small, c31n(0)=f m˜ 03n ] 0.
Now consider the displacement map L:=T¯
31 − D0. Obviously L1(n,y˜)
=0; for L2, it follows from (6.30), (6.31), and (6.32) that we have

L2(n,y˜)

=−m(mˆ 2)y˜+c310 1 n, w 1 n
n0 ,−a12, w 1 n
n0 ,−b12

+1 n
n02 s¯1+s¯3 5 C

n

i=1 c31i 1 n, w 1 n
n0 ,−a12, w 1 n
n0 ,−b122 y˜ i+O(y˜ n+1)6.

Derivating L2 with respect to y˜n times, we have

L˜ n(n,y˜)=1 n
n02 −(s¯1+s¯3) L (n)
2 (n,y˜)=f m˜ 03n(0)+O(n)+O(y˜) ] 0. (6.39)

So L=0 has at most n small roots; i.e., Cycl(Ehp2b) [ n.
(4) Cyclicity of Ehp4, Ehp5, Ehp6, and Ehp7. Note that passing
from P3 to P1 is like passing an attracting saddle node. So for Ehp4, the
proof is the same as that of the finite cyclicity of a graphic with a saddle
and a saddle node [38].

FIG. 22. Displacement maps for graphics (a) Ehp4, (b) Ehp6, and (c) Ehp7.

FINITE CYCLICITY 397

For the limit periodic sets Ehp5, Ehp6, and Ehp7, as shown in Fig. 22b
and 22c, since the return map can be written as a composition of regular
transition maps and maps with derivatives sufficiently small, we get
Cycl(Ehp5, Ehp6, Ehp7) [ 1. L

6.3. Finite Cyclicity of hh Graphics of Elliptic Type

In this section, we study the 12 families of hh graphics listed in Table V.
We state the main result in Section 6.3.1 and give a generalized Rolle’s
theorem in Section 6.3.2. The main theorem is proved in Sections 6.3.3 and
6.3.4.

6.3.1. Main theorem on the hh graphics of elliptic type.

Theorem 6.9. An hh graphic through a triple nilpotent elliptic point of
codimension 3 has finite cyclicity if the generic hypothesis PŒ(0) ] 1 is
satisfied.

For the proof, by changing the family X to −X if necessary, we impose

Hypothesis 6.10. The hh graphic with a nilpotent elliptic point is
attracting:
 [H]: PŒ(0)=c g <1. (6.40)

In Table V, there are 12 families of hh graphics of elliptic type: Ehhi
(i=1, ..., 12).
By Proposition 5.7, all the upper boundary graphics in the 12 families
have finite cyclicity 1. We are going to prove that all the lower boundary
and intermediate graphics have finite cyclicity. The proof is long and split
into several subsections.

6.3.2. Generalized Rolle’s theorem and a transition map. We will have to
study the number of intersection points of two planar curves, hence the
following generalization of Rolle’s theorem (in the spirit of Khovanskii’s
method) is useful.

Theorem 6.11 (Generalized Rolle’s theorem). Let D=(x1,x2)×(y1,y2).
Let F(x, y), G(x, y) be two functions continuous on Da and smooth in D.
Assume that in D, F −
x(x, y), F −
y(x, y) ] 0. Denote the number of intersections
of F(x, y)=0 and G(x, y)=0 in the region D by #(F, G) and let

J[F, G](x, y)=F −
y(x, y) G −
x(x, y) − F −
x(x, y) G −
y(x, y).

Then
 #(F, G) [ 1+#(F, J[F, G]).

398 ZHU AND ROUSSEAU

Proof. First note that if -(x, y) ¥ D, F(x, y) ] 0, then #(F, G)=0, and
the conclusion holds.
Assume that there exists a point (x0,y0) ¥ D such that F(x0,y0)=0.
Since F(x, y) is smooth and Fy(x, y) ] 0, by the implicit function theorem,
there exists eˆ0 >0 such that F(x, y)=0 defines a unique smooth curve:
y=f(x),in (x0 − eˆ0,x0+eˆ0).As F −
y(x, y) ] 0, the function y=f(x) can be
extended both ways to the boundaries of the region. Let [x3,x4] be the
maximum interval in which y=f(x) is defined. Then x1 [ x3 [ x4 [ x2.
The curve y=f(x), x ¥ [x3,x4] is the unique branch defined by
F(x, y)=0 in the region D. Indeed, if x4 <x2, since F −
x(x, y), F −
y(x, y) ] 0,
so either F −
x(x, y) F −
y(x, y) > 0 or F −
x(x, y) F −
y(x, y) < 0. In the first case,
then for x ¥ [x3,x4], fŒ(x)=−F −
x(x, f(x))/F −
y(x, f(x)) < 0, yielding f(x4)
=y1. Therefore, -(x, y) ¥ (x4,x2]×[y1,y2] there holds

F(x, y)=F(x, y) − F(x4,y1)

=[F(x, y) − F(x, y1)]+[F(x, y1) − F(x4,y1)]

=F −
y(x, y¯)(y−y1)+F −
x(x¯, y1)(x − x4) ] 0,

where x¯ and y¯ are between x, x4 and y, y1, respectively. The case
F −
x(x, y) F −
y(x, y) < 0 is similar. So -(x, y) ¥ ([x1,x3) 2 (x4,x2])×[y1,y2],
F(x, y) ] 0.
Let g(x)=G(x, f(x)). Then we turn to study the number of roots of
g(x)=0 for x ¥ [x3,x4]. Since

gŒ(x)=
J[F(x, y), G(x, y)]
F −
y(x, y) :

y=f(x),

FIG. 23. The transition map U: y1 Q y4.

FINITE CYCLICITY 399

by Rolle’s theorem,

#(F, G) [ 1+#(gŒ(x), 0)

=1+#(J[F, G](x, y), F(x, y))

=1+#(F, J[F, G]). L

We will use Theorem 6.11 for a pair of functions F, G in a region
depending on n.
To study the cyclicity of the family Ehh1, we use Proposition 6.1, and we
also need the transition map U in Fig. 23 to be nonlinear.

Proposition 6.12. Let U=(U1,U2): y1 Q y4 be the transition map along
r1=r1=0 in the normal form coordinates (see Fig. 23). If a ] 1
3, 1
4, then

U1(r1, r1)=r1[m141+m142r1+m143r1+O(|(r1, r1)| 2)]

U2(r1, r1)=r1[mˆ 141+mˆ 142r1+mˆ 143r1+O(|(r1, r1)| 2)]. (6.41)

Also -(a, m¯) ¥ A× S 2,
 “ 2U1
“r 2
1 (0, 0)=2m142=f e2

“ 2U2
“r 2
1 (0, 0)=2mˆ 143=f m¯ 3.
 (6.42)

Furthermore, if m142 ] 0, then mˆ 142 ] 0;if mˆ 143 ] 0, then m143 ] 0.

Proof. The map U is a regular transition map along the invariant line
{r1=0} 5 {r1=0}. Since r1=0 and r1=0 are invariant, we can write
U=(U1,U2) in the form of (6.41) and calculate the derivatives “ iU1/
“r i
1(0, 0), in the plane r1=0 (resp. “ iU2/“r i
1(0, 0), in the plane r1=0).
We begin with the derivatives with respect to r1. In the plane r1=0, the
system (4.6) becomes

dr1
dy¯ 1= − (a+y¯ 1)r1
−(1−2a) y¯ 1+2y¯ 2
1 −y¯ 1r1(e2+r1h¯1)+r1h¯2=P¯1(r1,y¯ 1)
Q¯ 1(r1,y¯ 1), (6.43)

where h¯1 and h¯2 are C . functions and h¯2=e2a+O(r1).
We are going to do the calculations using the system (4.6) in the original
coordinates (r1, r1,y¯ 1).
In the neighborhood of P1, the system has the form (4.6). By the normal
form change (4.7), the system (4.6) is in the normal form (4.9) or (4.8). In
the plane r1=0,if a ] 1
4, 1
3 , the section y1={y˜ 1=y0} becomes

y −
1:y¯ 1 :=g11(r1)=d10(y0)+d11(y0)r1+O(r 2
1), (6.44)

400 ZHU AND ROUSSEAU

where
 d10(y0)=y0+O(y 2
0), d11(y0)=e2 5 a
1−3a
+O(y0)6.

Similarly, in the coordinates (r1, r1,y¯ 1), the section y4={y˜ 4=−y0}
becomes
 y −
4:y¯ 1 :=g14(r1)=d40(y0)+d41(y0)r1+O(r 2
1), (6.45)

where

d40(y0)=
1−2a
2 −y0+O(y 2
0), d41(y0)=e2 58a(1+4a)
3−4a +O(y0)6.

Then by Proposition 5.2, we have

“U1
“r1 (0, 0)=exp 1 F g14(0)

g11(0) a+y¯ 1
y¯ 1(1−2a−2y¯ 1) dy¯ 12=
1 1−2a
2 2
 1+2a
2(1 − 2a)

y
 1+2a
2(1 − 2a)
0
 (1+O(y0)).

(6.46)

Now we calculate “ 2U1/“r 2
1(0, 0). Since P¯1(0, y¯ 1)=0, by Proposition 5.2
we have
 “ 2U1
“r 2
1 (0, 0)=
“U1
“r1 (0, 0)[PI1+PI2+PI3], (6.47)

where
 PI1=2g −
14(0) “U1
“r1 (0, 0) 1 P¯1r1
Q¯ 1 2 (0, g14(0))

=
4e2a(1+4a)
3−4a 1 1−2a
2 2
 6a − 1
2(1 − 2a) 1+O(y0)

y
 3−2a
2(1 − 2a)
0 =f 1+O(y0)

y
 3−2a
2(1 − 2a)
0

PI2=−2g −
11(0) 1 P¯1r1
Q¯ 1 2 (0, g11(0))

=− e2a 2(1+O(y0))
(1 − 3a)(1 − 2a) y0=f sign(1 − 3a) e2 1+O(y0)
y0
 (6.48)

FINITE CYCLICITY 401

and

PI3=F g14(0)

g11(0) 5P¯ '
1r1
Q¯ 1 (0, y¯ 1)−2 P¯ −
1r1 Q¯ −
1r1
Q¯ 2
1 (0, y¯ 1)6 exp 1 F u

g11(0) P¯ −
1r1
Q¯ 1 (0, u) du2 dy¯ 1

=−f e2(1+O(y0))

y
 a
1−2a
0 F d40(y0)

d10(y0) (a+y¯ 1)(y¯ 1 −a)

y¯
 2−5a
1−2a
1 1 1−2a
2 −y¯ 12
 5−8a
2(1 − 2a) dy¯ 1. (6.49)

Since

lim
y0 Q 0
 F d40(y0)

d10(y0) (a+y¯ 1)(y¯ 1 −a)

y¯
 2−5a
1−2a
1 1 1−2a
2 −y¯ 12
 5−8a
2(1 − 2a) dy¯ 1

1

y
 3−4a
2(1 − 2a)
0
 =−8a(1+4a)
3−4a 1 1−2a
2 2
 3a − 1
1−2a
,

then
 F d40(y0)

d10(y0) (a+y¯ 1)(y¯ 1 −a)

y¯
 2−5a
1−2a
1 1 1−2a
2 −y¯ 12
 5−8a
2(1 − 2a) dy¯ 1=−f 1+O(y
 1+2a
2(1 − 2a)
0 )

y
 3−4a
2(1 − 2a)
0 , (6.50)

so, by (6.49) and (6.50), for PI3, we have

PI3=f e2 1+O(y
 1+2a
2(1 − 2a)
0 )

y
 3−2a
2(1 − 2a)
0 . (6.51)

Therefore, it follows from (6.47), (6.46), (6.48), and (6.51) that we have

“ 2U1
“r 2
1 (0, 0)=f e2 1+O(y0)+O (y
 1+2a
2(1 − 2a)
0 )

y
 2
1−2a
0 . (6.52)

So, if we take y0 >0 small, then by (6.52), “ 2U1/“r 2
1(0, 0)=f e2.
Now we prove that “ 2U2/“r 2
1(0, 0) ] 0. In the plane r1=0, the system
(4.6) becomes

dr1
dy¯ 1= (a+y¯ 1+m¯ 2r 2
1) r1
−(1−2a) y¯ 1+2y¯ 2
1+m¯ 3r1y¯ 1+2m¯ 2r 2
2y¯ 1+m¯ 1r 3
1=Pˆ 1(r1,y¯ 1)
Qˆ 1(r1,y¯ 1). (6.53)

We still use the system (4.6) in the original coordinates (r1, r1,y¯ 1) to do the
calculations.

402 ZHU AND ROUSSEAU

In the plane r1=0,if a ] 1
4, 1
3, the section y1={y˜ 1=y0} becomes

yˆ1:y¯ 1 :=gˆ 11(r1)=dˆ10(y0)+dˆ11(y0) r1+O(r 2
1), (6.54)

where
 dˆ10(y0)=y0+O(y 2
0), dˆ11(y0)=
m¯ 3
a +O(y0).

Similarly, in the coordinates (r1, r1,y¯ 1),on r1=0 the section y4=
{y˜ 4=−y0} becomes

yˆ −
4:y¯ 1=gˆ 14(r1)=dˆ40(y0)+dˆ41(y0) r1+O(r 2
1), (6.55)

where

dˆ40(y0)=
1−2a
2 −y0+O(y 2
0), dˆ41(y0)=−1−2a
1−4a m3+O(y0).

Then, for “U2/“r1(0, 0), by Proposition 5.2, we have

“U2
“r1 (0, 0)=
y
 1+2a
2(1 − 2a)
0 (1+O(y0))
1 1−2a
2 2
 1+2a
2(1 − 2a) . (6.56)

Now we calculate “ 2U2/“r 2
1(0, 0). By Proposition 5.2, since Pˆ 1(0, y¯ 1)=0,
we have
 “ 2U2
“r 2
1 (0, 0)=
“U2
“r1 (0, 0)[PI5 1+PI5 2+PI5 3], (6.57)

where

PI5 1=2gˆ −
14(0) “U2
“r1 (0, 0) 1 Pˆ 1r1
Qˆ 1 2 (0, gˆ 14(0))= m¯ 3 y
 6a − 1
2(1 − 2a)
0 (1+O(y0))

(1 − 4a) 1 1−2a
2 2
 6a − 1
2(1 − 2a)

PI5 2=−2gˆ −
11(0) 1 Pˆ 1r1
Qˆ 1 2 (0, gˆ 11(0))=
2m¯ 3(1+O(y0))
(1 − 2a) y0
 (6.58)

FINITE CYCLICITY 403

and

PI5 3=F gˆ 14(0)

gˆ 11(0) 5Pˆ '
1r1
Qˆ 1 (0, y¯1)−2 Pˆ −
1r1 Qˆ −
1r1
Qˆ 2
1 (0, y¯1)6 exp1F u

gˆ 11(0) Pˆ −
1r1
Qˆ 1 (0, u) du2 dy¯1

=−m¯ 3 y
 a
1−2a
0 (1+O(y0))

2 1 1−2a
2 2
 1
2(1 − 2a) F dˆ40(y0)

dˆ10(y0) a+y¯ 1

y¯
 2−3a
1−2a
1 1 1−2a
2 −y¯ 12
 3−8a
2(1 − 2a) dy¯ 1. (6.59)

Since
 lim
y0 Q 0
 F dˆ40(y0)

dˆ10(y0) a+y¯ 1

y¯
 2−3a
1−2a
1 1 1−2a
2 −y¯ 12
 3−8a
2(1 − 2a) dy¯ 1

1

y
 1−a
1−2a
0
 = a(1 − 2a)

(1−a) 1 1−2a
2 2
 3−8a
2(1 − 2a),

thus

F dˆ40(y0)

dˆ10(y0) a+y¯ 1

y¯
 2−3a
1−2a
1 1 1−2a
2 −y¯ 12
 3−8a
2(1 − 2a) dy¯ 1= 2a [1+O (y
 1+2a
2(1 − 2a)
0 )]

(1 − a) 1 1−2a
2 2
 1−4a
2(1 − 2a) y
 1−a
1−2a
0
 . (6.60)

By (6.59) and (6.60), we have

PI5 3= 2am¯ 3
(1 − 2a) y0 [1+O(y0)+O(y
 1+2a
2(1 − 2a)
0 )]. (6.61)

It follows from (6.57), (6.58), and (6.61) that we have

“ 2U2
“r 2
1 (0, 0)=
“U2
“r1 (0, 0)r m¯ 3 y
 6a − 1
2(1 − 2a)
0 (1+O(y0))

(1 − 4a) 1 1−2a
2 2
 6a − 1
2(1 − 2a)
+
2m¯ 3(1+O(y0))
(1 − 2a) y0

+
2am¯ 3[1+O(y0)+O(y
 1+2a
2(1 − 2a)
0 )]
(1 − 2a) y0 s

=
(1+2a) m¯ 3
(1 − 2a) y0 [1+O(y0)+O (y
 1+2a
2(1 − 2a)
0 )]. (6.62)

404 ZHU AND ROUSSEAU

By the invariance of n=r1r1=r2r2 and (6.41), we have

r2r2=r1r1[m141+m142r1+m143r1+O(|(r1, r1)| 2)]

[mˆ 141+mˆ 142r1+mˆ 143r1+O(|(r1, r1)| 2)]. (6.63)

Equating the coefficients of terms of r1 and r1 respectively on both sides
of (6.63), we have
 m141mˆ 142+mˆ 141m142=0

m141mˆ 143+mˆ 141m143=0. (6.64)

Since m141mˆ 141=1,if m142 ] 0, then mˆ 142 ] 0;if mˆ 143 ] 0, then m143 ] 0. L

Corollary 6.13. For the transition map V: y2 Q y3 in the normal form
coordinates, if a ] 1
3, 1
4, then

“V1
“r2 (0, 0)=
“U1
“r1 (0, 0)

“ 2V1
“r 2
2 (0, 0)=
“ 2U1
“r 2
1 (0, 0)

“V2
“r2 (0, 0)=
“U2
“r1 (0, 0)

“ 2V2
“r 2
2 (0, 0)=
“ 2U2
“r 2
1 (0, 0).
 (6.65)

Proof. Just note that in the plane r2=0, the system is the same as
system (6.43) except for the sign of the term r2h¯1 which does not influence
the first and second derivatives. L

6.3.3. Lower boundary hh graphics of elliptic type. Among the 12 lower
boundary graphics, Ehh1c, Ehh2e, and Ehh3e pass through both passages
P2P3 and P1P4 along the equator (Remark 6.7) and require a special treat-
ment. Indeed in general an explicit formula does not exist for the inverse of
the second type of Dulac map. We will replace the study of zeroes of the
displacement map by the study of the zeroes of a system of two variables
using generalized Rolle’s theorem.
To prove the finite cyclicity of the graphic Ehh1, we give the following
lemma.

Lemma 6.14. For the system in the neighborhood of P3,if s3=
1
n, n ¥ N,
then the first saddle quantity is nonzero for the 2-dimensional system on r=0
as soon as e2 ] 0.
 FINITE CYCLICITY 405

For the system in the neighborhood of P1,if s1=1 (a0=
1
3 )or s1=2
(a0=
1
4), then for the 2-dimensional system on r=0, the first saddle quantity
is a2=f m¯ 30.

Proof. The proof relies on the fact that the system in the neighborhood
of P3 is simple, allowing a control on the normalizing process up to the
determination of the first saddle quantity. See Appendix A.2 for the
calculations. L

Theorem 6.15. The generic graphic Ehh1c through a nilpotent elliptic
point of codimension 3 has finite cyclicity. For the generic graphics Ehh2e
and Ehh3e, Cycl(Ehh2e, Ehh3e) [ 2.

Proof. As shown in Fig. 24, take transversal sections Pi, Si+2(i=1, 2),
and yj(j=1, 2, 3, 4) in the charts P.R. 1, 2, 3 and P.R.4 respectively (sec-
tions were defined in 5.6). Similar to what we have done in Theorem 6.6 for
the graphic Ehp1 in (6.16), we take

r1=n 1−c, r1=n c

on the section y1 and
 r2=n 1−d, r2=n d

on the section y2 with (n,c) ¥ (0, e 2)× In and (n,d) ¥ (0, e 2)× In, where
In=(ln e
ln n, ln ue
ln n ) … (0, 1) and u ¥ (0, 1), and n=ue 2.

FIG. 24. The displacement maps defined on y1 and y2.

406 ZHU AND ROUSSEAU

To study the cyclicity of the lower boundary graphics, we are going to
study the displacement maps defined on the sections y1 and y2 respectively
with images in P1 and S4. Limit cycles are given by roots of the system

T1(n, c)=T2(n,d)

T4(n, c)=T3(n, d). (6.66)

To study their number, we use Theorem 6.11 in a region (c, d) ¥ In × In
depending on n with n >0 sufficiently small.
The proof will go in several steps.

(1) Developing the transition maps Ti (i=1, 2, 3, 4).

(1.1) Transition map T1. The map T1: y1 Q P1 is the second type
of Dulac map near P1. By Theorem 4.14, for r=n c and r=n 1−c, it has an
expression similar to (6.17) with s¯ 3=s¯ 1. Hence

T12(n, c)=g1 1 n, w 1 n c

r0 , a122+n s¯1c 5l1+h1 1 n, n c, w 1 n c

r0 ,−a1226

(6.67)

where l1=y0/r s¯1
0 >0; g1(n, w(n c/r0, a1)) =(o1/r p1
0 ) n p1 w(n c/r0, a1) and
h1(n, n c, w(n c/r0,−a1)) is C . and satisfies the same properties as h2 in
(6.18). (1.2) Transition map T4. The transition map T4: y1 Q S4 can be
factored as
 T4=G4 p U,

where
 • U: y1 Q y4 is the regular transition map defined in Proposi-
tion 6.12. In the coordinate c on y1, the first component U1 of the map U
can be written as

U1(n 1−c, n c)=n 1−c[m141+m142(n) n 1−c+m143(n) n c+O(n 2(1 − c), n 2c)], (6.68)

where by Proposition 6.12, m141(0) ] 0, m142(0)=f e2 and m143(0)=f m¯ 30.
• G4: y4 Q S4 is the second type of Dulac map near P4 which
satisfies Theorem 4.14 with s¯=s¯ 4. By (6.68), we have

r4=n 1−c(m141+O(n c, n 1−c)). (6.69)

FINITE CYCLICITY 407

Let m4=m141/r0. Using (6.69) we have

w 1 r4
r0 , b12=w 1 m14
r0 n 1−c(1+O(n c, n 1−c)), b12

=w(m4n 1−c, b1)+O(n c − (1 − c) b1, n (1 − c)(1 − b1)). (6.70)

So by (6.68), (4.28), and (6.70) and by Lemma 4.13 for s¯ 4, we have

T42(n, c)=g4(n, w(r4, b1))

+n s¯3(1 − c)[m41(n)+m42n 1−c+m43n c+O(n 2(1 − c), n 2c)

+h41(n, n 1−c, w(m4n 1−c,−b1))], (6.71)

where m41=(y0/r s¯3
0 )(m141(n)) s¯3=l4m141(n), m42(0)=f m142(0)=K142e2,
and m43(0)=f m143(0)=K143m¯ 30 and K142,K143 are nonzero constants; in
g4(n, w(r4/r0, b1)) we still keep r4 as a function of c in (6.68); also
h41(n, n 1−c, w(m4n 1−c,−b1)) is C k and satisfies

“ ih41
“c i =O(n p3(1 − c)w(m4n 1−c, b1)(ln n) i)i \ 0. (6.72)

(1.3) Transition map T2. The transition map T2: y2 Q P1 can be
factored as
 T2=S −1 p G2(r2, r2),

where
 • G2: y2 Q P2 is the second type of Dulac map near P2. Using the
coordinates (n,d) on the section y2 is given in (6.17). g2(n, w(n d/r0, a1))
=(o1/r p1
0 ) n p1w(n d/r0, a1). Also h2(n,d, w(n d/r0,−a1)) is C . and satisfies
the same properties as h1 in (6.18).
• S −1: P2 Q P1 is a C k regular transition map defined in
Proposition 6.1. We can write its second component as

S −1
2 (n,y˜ 2)=m210(n)+m211(n)y˜ 2+m212(n)y˜ 2+O(y˜ 3
2), (6.73)

where m210(0)=0 and m211(0) ] 0 and by Proposition 6.1, for Ehh1c,
m212(0)=f m¯ 30, while for Ehh2e (resp. Ehh3e) m211(0) is small (resp. large) .

408 ZHU AND ROUSSEAU

By (6.73) and Lemma 4.13 for s¯ 2 in G2, for the transition map T2,we
have
 T22(n, d)=m20 1 n, w 1 n d

r0 , a122

+n s¯1d 5m21 1 n, w 1 n d

r0 , a122+m22 1 n, w 1 n d

r0 , a122 n s¯1d

+h211 1 n, n d, w 1 n d

r0 ,−a1226 (6.74)

where
 m20 1 n, w 1 n d

r0 , a122=m210(n)+o1 5m211(n)
r s¯1
0 n p1w 1 n d

r0 , a122

+O 1 n 2p1w 2 1 n d

r0 , a1226

m21 1 n, w 1 n d

r0 , a122=m211(n)l1+o1O 1 n p1w 1 n d

r0 , a122

m22 1 n, w 1 n d

r0 , a122=m212(n)l 2
1+o1O 1 n p1w 1 n d

r0 , a122,

and h211 is C k and has the same properties as h1 in (6.18).
(1.4) The transition map T3. Transition map T3: y2 Q S4 can be
factored as
 T3=R p G3 p V,

where
 • V: y2 Q y3 is the regular transition map defined in
Corollary 6.13. Using the coordinates (n,d) on section y3, we have

V1(n 1−d, n d)=n 1−d[m¯ 141+m¯ 142(n) n 1−d+m¯ 143(n) n d+O(n 2(1 − d), n 2d)], (6.75)

where by Corollary 6.13 we have m¯ 14i(0)=m14i(0) (i=1, 2, 3);
• G3: y3 Q s3 is the second type of Dulac map near P3 which
satisfies Theorem 4.14 with s3(a0)=2(1 − 2a0);
• the regular transition map R: S3 Q S4 is C k and can be written as

R2(n,y˜ 3)=m340(n)+ C

N2

j=1 m34j(n)y˜ j
3+O(y˜ N2+1
3 ), (6.76)

where by Hypothesis 6.10, we have m341(0) < 1.

FINITE CYCLICITY 409

So it follows from (6.75), (4.28), and (6.76) that the transition map T3
satisfies

T32(n, d)=m30(n, w(r3, b1))+n s¯3(1 − d) 5m31(n, w(m4n 1−d, b1))

+m32(n) n 1−d+m33n d+O(n 2(1 − d), n 2d)

+ C

N1

j=1 m¯ 34jns¯3(1 − d) j+O(n(N1+1) s¯3(1 − d))+h31(n, n1−d, w(m4n1−d, b1))6,

(6.77)

where h31 is C k and satisfies the properties of h41 in (6.72) and

m30=m340(n)+o3 5m341(n)
r p3
0 n p3w 1 r3
r0 , b12+O 1 n 2p3w 2 1 r3
r0 , b1226

m31=
m¯ s¯3
141m341 y0
r s¯3
0 +o3O(n p3w(m4n 1−d, b1)), m31(0) ] 0

m32=
s¯ 3m¯ 142(n)y0
r s¯3
0 m¯ 1− s¯3
141 +o3O(n p3w(m4n 1−d, b1)), m32(0)=f K142e2

m33=
s¯ 3m¯ 143(n)y0
r s¯3
0 m¯ 1− s¯3
141 +o3O(n p3w(m4n 1−d, b1)), m33(0)=f K143m¯ 30

m¯ 341=
m¯ 2s¯3
141 y 2
0m342
r 2s¯3
0 +o3O(n p3w(m4n 1−d, b1)), m¯ 341(0)=f m342(0)

and in m30(n, w(r3/r0, b1)) we still keep r3 as the function of d in the
expression (6.75).
To get the cyclicity of Ehh1c and Ehh3e, we are going to apply
Theorem 6.11 to study #(F, G) of the following system

Fn(c, d) :=T12(n,c) − T22(n, d)=0

Gn(c, d) :=T42(n,c) − T32(n, d)=0 (6.78)

for (a, m¯) ¥ A0 × S 2 and (c, d) ¥ Dn, where Dn is a square whose size
depends on n. With n=ue 2 and u ¥ (0, 1), then Dn=In × In.
(2) Functions Fn(c, d) and Gn(c, d) satisfy the conditions of Theorem
5.3.2. For 0< n < e 2, Fn(c, d) and Gn(c, d) are continuous on Da n and
smooth in Dn. Note that -c ¥ (ln e
ln n, ln ue
ln n ), we have n 1−c ¥ (ue, e), hence
n p1(1 − c) ¥ (0, e p1). So for 0< n < e 2 and -(c, d) ¥ Dn with e >0 sufficiently
small, by (6.19), a first derivation gives

410 ZHU AND ROUSSEAU

“
“c Fn(c, d)=− o1
r s¯1
0 n s¯1cn p1(1 − c) ln n+n s¯1c ln n 5s¯ 1l1+h1 1 n, n c, w 1 n c

r0 ,−a122

+ 1
ln n “
“c h1 1 n, n c, w 1 n c

r0 ,−a1226

=n s¯1c ln n 5s¯ 1l1+l11n p1(1 − c)+h11 1 n, n c, w 1 n c

r0 , a1226

] 0 (6.79)

where l11=−o1/r s¯1
0 , h11(n, n c, w(n c/r0, a1)) is C k and satisfies the pro-
perties (6.18). Since for x>0 sufficiently small, (x p1w(x, a1))Œ=
x p1 −1[s¯ 1w(x, a1) − 1]>0, for h11 with c ¥ In, we have the estimation
h11(n, n c, w(n c/r0, a1))=O(e p1w(e, a1)).
Similar for 0< n < e 2 and -(c, d) ¥ Dn with e >0 sufficiently small, we
have

“
“d Fn(c, d)

=−n s¯1d ln n 5s¯ 1l2+l21n p1(1 − d)+l22(n) n s¯1d+h23 1 n, n d, w 1 n d

r0 ,−a1226

] 0 (6.80)

where l2(0)=l1m211(0) ] 0, l21=−o1m211/r s1
0 , and l22=2s¯ 1l 2
1m212. Also
for Ehh1c, l22(0)=f m212(0)=f m¯ 30. For h23,itis C k and satisfies the
properties (6.18).
By (6.79) and (6.80), for 0< n < e 2 and -(c, d) ¥ Dn with e >0 sufficiently
small, Fn(c, d) and Gn(c, d) satisfy the conditions of Theorem 6.11. So we
have
 #(F, G) [ 1+#(F, J[F, G]). (6.81)

(3) Calculation of #(F, J[F, G]). To calculate #(F, J[F, G]),we
have to calculate J[F, G]=
“F
“c “G
“d − “F
“d “G
“c .
Note that for the case q3=1, s¯ 3+b1=p3=1,so

nn −b1(1 − c)=n 1− b1(1 − c)=n (1 − b1)(1 − c)n 1 − (1 − c)=n cn s¯3(1 − c).

FINITE CYCLICITY 411

Therefore, for g4(n, w(r4/r0, b1)), by (6.68) and similar to (6.19) we have

“g4
“c 1 n, w 1 r4
r0 , b122

=
o3
r0 n “
“c w 1 r4
r0 , b12=
o3
r0 n 5 −1 r4
r02 −1 − b16 “r4
“c

= o3
m s¯1
4 n s¯3(1 − c)n c ln n[1+m¯ˆ 142(n) n 1−c+m¯ˆ 143(n) n c+O(n 2(1 − c), n 2c)].

(6.82)

So by (6.71), (6.77), and (6.82) and direct derivation, we have

“
“c Gn(c, d)

=n s¯3(1 − c) ln n[s¯ 3l4+l¯
411n p3c+l¯
422(n) n 1−c+l¯
423(n) n c

+O(n 2(1 − c), n 2c)+h42(n, n 1−c, w(m4n 1−c, b1))]

“
“d Gn(c, d)

=−n s¯3(1 − d) ln n 5s¯ 3l3+l¯
311n p3d+l¯
322(n) n 1−d+l¯
323(n) n d+O(n 2(1 − d), n 2d)

+ C

N1

j=1 l¯
33jn s¯3(1 − d) j+O(n (N1+1) s¯3(1 − d))+h32(n, n 1−d, w(m4n 1−d,−b1))6

(6.83)

where h42(n, n 1−c, w(m4n 1−c,−b1)) and h32(n, n 1−d, w(m4n 1−d,−b1)) are
C k and satisfy the properties (6.72); l4=(y0/r s¯1
0 )m s¯3
141, l3=m341l4, and
l3(0) l4(0) ] 0. Also

l¯
311(0)=f o3

l¯
411(0)=f o3

l¯
331(0)=f m342(0)

l¯
422(0)=f m142(0)=f K142e2

l¯
423(0)=f m143(0)=f K143m¯ 30

l¯
322(0)=f m341(0) l¯
422(0)=f m341K142e2

l¯
323(0)=f m341(0) l¯
423(0)=f m341K143m¯ 30.

412 ZHU AND ROUSSEAU

Let
 G1(n,c,d) :=
s¯ 3n s¯3

s¯ 1
 J[F, G](n,c,d)
“G
“c “G
“d
 .

It follows from (6.79), (6.80), and (6.83) that

G1(n, c, d)=n (s¯1+s¯3)c[1+h¯1(n, c)] − n (s¯1+s¯3)d 5m211(n)
m341(n)
+h¯2(n,d)6.

Then for 0< n < e 2 and -(c, d) ¥ Dn with e >0 sufficiently small, the
equation G1(n, c, d)=0 is equivalent to equation G2(n, c, d)=0, where

G2(n,c,d) :=n c[1+h1(n, c)] − n d[c1(n)+h2(n, d)], (6.84)

where c1(n)=(m211(n)/m341(n)) 1/(s¯1+s¯3), and

h1(n, c)=c¯111n p1(1 − c)+c¯311n p3c

c¯142n 1−c+c¯143n c+O(n 2(1 − c), n 2c)

+H1 1 n, n c, n 1−c, w 1 n c

r0 ,−a12, w(m4n 1−c,−b1)2

h2(n, d)=c¯211n p1(1 − d)+c¯411n p3d

+c¯232n 1−d+c¯233n d+O(n 2(1 − d), n 2d)

+ C

N1

j=1 c¯34jn s¯3(1 − d) j+O(n (N1+1)(1 − d) s¯3)+c22(n) n s¯1d

+H2 1 n, n d, n 1−d, w 1 n d

r0 ,−a12, w(m4n 1−d,−b1)2

where
 c¯111(0)=f o1, c¯211(0)=f o1

c¯311(0)=f o3, c¯411(0)=f o3

c¯22(0)=f m212(0)

c¯341(0)=f m342(0)

c¯232(0)=f c¯142(0)=f K142e2

c¯233(0)=f c¯143(0)=f K143m¯ 30.

FINITE CYCLICITY 413

Also H1 and H2 are C k and

H1=O 1 n p1cw 1 n c

r0 , a12, n p3(1 − c)w(m4n 1−c, b1)2

H2=O 1 n p1dw 1 n d

r0 , a12, n p3(1 − d)w(m4n 1−d, b1)2.

Similar to what we did in (2) with the functions Fn(c, d) and Gn(c, d), one
can check that for 0< n < e 2 and -(c, d) ¥ Dn with e >0 sufficiently small,
G2(n,c,d) and Fn(c, d) satisfy the conditions of Theorem 6.11. Hence we
have
 #(F, G) [ #(G2, J[F, G2])+2. (6.85)

(4) Calculation of #(G2, J[F, G2]). Let

G3(n,c,d) := − s¯ 1l1 J[F, G2](n,c,d)
G −
2cG −
2d .

Then a straightforward calculation gives

G3(n, c, d)=n (s¯1 −1) c[1+h31(n, c)] − n (s¯1 −1) d[c2(n)+h32(n, d)], (6.86)

where c2(n)=m211(n)(m341(n)/m211(n)) 1/s¯1+s¯3.
By (6.84), if for 0< n < e 2 and -(c, d) ¥ Dn with e >0 sufficiently small,
G2(n,c,d) ] 0, then #(G2, J[F, G2])=0 and we already finish the proof.
Otherwise, similar to the proof in the Theorem 6.11, G2(n, c, d)=0 defines
a unique connected curve which satisfies

n c=n d c1(n)+h2(n,d)
1+h1(n,c) . (6.87)

By iterating the relation (6.87), the unique curve defined by
G2(n, c, d)=0 can be written as

n c=n d[c1(n)+h0(n, d)], (6.88)

where

h0(n, d)=c¯001n p1(1 − d)+c¯003n p3d

+c¯012n 1−d+c¯013n d+O(n 2(1 − d), n 2d)

+ C

N1

j=1 c¯03jn s¯3(1 − d) j+O(n (N1+1)(1 − d) s¯3)

+c¯02(n) n s¯1d+H0 1 n, n d, n 1−d, w 1 n d

r0 ,−a12, w(m4n 1−d,−b1)2

414 ZHU AND ROUSSEAU

where
 c¯001(0)=f o1, c¯003(0)=f o3

c¯02(0)=f m212(0)

c¯031(0)=f m342(0)

c¯012(0)=f m142(0)(m211(0) − m341(0))=f K142e2

c¯013(0)=f m143(0)(m211(0) m341(0))=f K143m¯ 30.

Also H0 is C k and

H0=O 1 n p1dw 1 n d

r0 , a12, n p3(1 − d)w(m4n 1−d, b1)2. (6.89)

If we substitute (6.88) into G3(n,c,d) and let

g(n, d)=c 1− s¯1
1 n 1− s¯1G3(n,c,d)|(6.88),

then a straightforward calculation gives

g(n, d)=c(n)+d01n p1(1 − d)+d03n p3d

+d2n 1−d+d3n d+O(n 2(1 − d), n 2d)

+ C

N1

j=1 d4jn s¯3(1 − d) j+O(n (N3+1)(1 − d) s¯3)

+d1(n) n s¯1d+H 1 n, n d, n 1−d, w 1 n d

r0 ,−a12, w(m4n 1−d,−b1)2,

(6.90)

where
 c(n)=1 − (m s¯3
211(n)m s¯1
341(n)) 1
s¯1+s¯3, (6.91)

and
 d01(0)=f o1, d03(0)=f o3

d1(0)=f m212(0)=f m¯ 30

d2(0)=f m142(0)(m211(0) − m341(0))=f K142e2

d3(0)=f m143(0)(m211(0) − m341(0))=f K143m¯ 30

d41(0)=f m342(0).

Also H is C k and satisfies (6.89).

FINITE CYCLICITY 415

In order to get the cyclicity of Ehh2e, Ehh3e, and Ehh1c, we will study
the number of roots of the equation g(n, d)=0 for d ¥ (0, 1) and n >0
sufficiently small.
(5) Cycl(Ehh2e, Ehh3e) [ 2. For the graphic Ehh2e (resp. Ehh3e),
since m211(0) can be sufficiently small (resp. large), so c(0) Q 1 (resp. is
sufficiently large). Hence for (a, m¯) ¥ A0 ×VI2 (resp. (a, m¯) ¥ A0 ×VI3 ), and
-n ¥ (0, n0) and d ¥ (0, 1), we have g(n,d) ] 0. Therefore, #(G2, J[F, G2])
=0 and by (6.85), we have #(F, G) [ 2, i.e., Cycl(Ehh2e, Ehh3e) [ 2.
(6) Cyclicity of Ehh1c when m211(0) [ 1 (this contains the case
m¯ 30=0). For the graphic Ehh1c, by (6.91), we have

c(0)=1 − (m s¯3
211(0) m s¯1
341(0)) 1
s¯1+s¯3. (6.92)

By Hypothesis 6.10 we have m341(0) < 1,soif m211(0) [ 1, then by (6.92) we
have c(0) ] 0; i.e., Cycl(Ehh1c) [ 2.
For the graphic Ehh1c with m211(0) > 1 (which implies m¯ 30 ] 0), we will
study the equation g(n, d)=0 with 0< n < e 2 and d ¥ In for a0 ¥ (0, 1
2) 0 Q
and a0 ¥ (0, 1
2) 5 Q in (7) and (8), respectively.
We have
 d2(0)=f m142(0)[m211(0) − m341(0)]=f K142e2 ] 0

d3(0)=f m143(0)[m211(0) − m341(0)]=f K143m¯ 30 ] 0. (6.93)

(7) Cyclicity of Ehh1c when m211(0) > 1 (m¯ 30 >0): Case a0 ¥ (0, 1
2) 0 Q.
For a0 ¥ (0, 1
2) 0 Q, the function g(n,d) in (6.90) can be simplified to

g(n, d)=c(n)+d1(n) n s¯1d+o(n s¯1d)

+d2(n) n 1−d+d3(n) n d+O(n 2(1 − d), n 2d)

+ C
[ 1
s¯3]

j=1 d4jn s¯3(1 − d) j+O(n([ 1
s¯3]+1) s¯3(1 − d)). (6.94)

Let

DD:˛
g0(n, d)= 1
ln n “
“d g(n,d)

gj(n, d)=
n s¯3(1 − d) j

ln n “
“d (gj−1(n,d) n −s¯3(1 − d) j), j=1, ..., 5 1
s¯ 36.

(6.95)

416 ZHU AND ROUSSEAU

Then after [1/s¯ 3]+1 steps of successive derivation and division in
(6.95), we get

g[ 1
s¯3](n, d)=d¯1(n) n s¯1d+o(n s¯1d)+d¯2(n) n 1−d+d¯3(n) n d+o(n 2(1 − d), n 2d),
(6.96)

where d¯1(0)=f m212(0)=f m¯ 30 ] 0, and by (6.93), d¯2(0)=f d2(0) ] 0.
We introduce a lemma.

Lemma 6.16. Consider the equation

L(n, d)=l¯
1(n) n s¯1d+o(n s¯1d)+l¯
2(n) n 1−d+o(n 1−d)+l¯
3(n) n d+o(n d)

for n ¥ (0, e 2) and d ¥ (ln e
ln n, ln ue
ln n ) with u ¥ (0, 1), n=ue 2, and e >0 sufficiently
small. If s¯ 1 >1 and l¯
2(0) l¯
3(0) ] 0 or s¯ 1 <1 and l¯
1(0) l¯
2(0) ] 0, then
L(n, d)=0 has at most 1 solution.

Proof. For the case s¯ 1 >1, L(n,d) can be simplified to

L(n, d)=l¯
2(n) n 1−d+o(n 1−d)+l¯
3(n) n d+o(n d).

Note that l¯
2(0) l¯
3(0) ] 0, so we have two possibilities:

•if l¯
2(0) l¯
3(0) > 0, then L(n,d) ] 0;
•if l¯
2(0) l¯
3(0) < 0, then L −
d(n,d) ] 0, thus L(n, d)=0 has at most one
solution.

The case s¯ 1 <1 is similar. L

End of proof of Theorem 6.15. In this case, note that we have
d¯1(0) d¯2(0) d¯3(0) ] 0 and s¯ 1 ] 1, so applying Lemma 6.16 to the function in
(6.96), we conclude that g[1/s¯3](n,d) has at most one root. Hence
g(n, d)=0 has at most [1/s¯ 3]+2 roots, yielding Cycl(Ehh1c) [ [1/s¯ 3]+4.
(8) Cyclicity of Ehh1c when m211(0) > 1 (m¯ 30 >0): Case a0 ¥ (0, 1
2)
5 Q. Then s1(a0), s3(a0) ¥ Q. For i=1, 3, let si(a0)=pi/qi,pi,qi ¥ N
and (pi,qi)=1; thus we have three subcases:
(8.1) Case a0 ¥ (0, 1
2) 5 Q 0 {
1
3, 2n − 1
4n ,n ¥ N}. Note that in this case
1/s3 ¨ N and s1 ] 1; therefore Eq. (6.90) can be reduced to

g(n, d)=c(n)+d1(n) n s¯1d+o(n s¯1d)+d3(n) n d+o(n d)

+ C

q3

j=1 d4jn s¯3(1 − d) j+d2(n) n 1−d+o(n 1−d). (6.97)

FINITE CYCLICITY 417

Applying the DD process (6.95) [1/s3]+1 steps to the function g(n,d)
in (6.97), we get

gp1,q3 (n, d)=˛ ldˆ 1(n) n s¯1d+o(n s¯1d)+dˆ 2(n) n 1−d+o(n 1−d) if s1 <1
dˆ 3(n) n d+o(n d)+dˆ 2(n) n 1−d+o(n 1−d) if s1 >1,

where dˆ i(0) ] 0 (i=1, 2, 3).
Then by Lemma 6.16 we obtain that gp1,q3 (n, d)=0 has at most one
solution. Hence g(n, d)=0 has at most [1/s¯ 3]+4 solutions; i.e., Ehh1c
has finite cyclicity.
(8.2) Case a0=
1
4. In this case, we have s1(
1
4)=2 and s3(
1
4)=1.By
Lemma 6.14, the first saddle quantity at P1 is a2=f m¯ 30 ] 0, the first saddle
quantity at P3 is b2 ] 0.
For the second type of Dulac map near P3, by Theorem 4.14, we have

h4 1 r4, r4, w 1 r4
r0 ,−b122

=b2K3r3w 1 r3
r0 , b12+O 1 nw 2 1 r4
r0 ,−b12 w1 r4
r0 , b122. (6.98)

Then the function in (6.90) has the form

g(n, d)=c(n)+d11(n) n d+d12(n) n 2d

+d1(n) n 2dw 1 n d

r0 , a12+O 1 n 2w 2 1 n d

r0 ,−a12 w 1 n d

r0 , a122

+d21n 1−d+d2(n) n 1−dw(m4n 1−d, b1)

+O(nw 2(m4n 1−d,−b1) w(m4n 1−d, b1)) (6.99)

where d11(n) can vanish, d1(0)=f a2(
1
4)=f m¯ 30 ] 0, and d2(0)=f b2 ] 0.
By applying the standard division–derivation method to the function
g(n,d) in (6.99), we can kill the terms c(n) and n d. Then g(n, d)=0 has at
most four roots plus the number of roots of

g1(n, d)=dˆ 12n 2d+dˆ 1(n) n 2dw 1 n d

r0 , a12+O 1 n 2w 2 1 n d

r0 ,−a12 w 1 n d

r0 , a122

+dˆ 21(n) n 1−d+dˆ 2(n) n 1−dw(m4n 1−d, b1)

+O(nw 2(m4n 1−d,−b1) w(m4n 1−d, b1))

where dˆ i(0)=f di(0) ] 0 (i=1, 2).

418 ZHU AND ROUSSEAU

Let g2(n, d)=n 2d/ln n “
“d (n −2dg1(n, d)); then

g2(n, d)=−r a1
0 d˜ 1n s¯1d+O 1 n 2w 2 1 n d

r0 ,−a12 w 1 n d

r0 , a122

− [(3+b1) w(m14n 1−d, b1)+1] d˜ 2(n) n 1−d

+O(nw 2(m4n 1−d,−b1) w(m4n 1−d, b1)).

Let g3(n, d)=n 1−d/ln n “
“d (n −(1 − d)g2(n, d)); then

g3(n, d)=d¯1n s¯1d+O 1 n 2w 2 1 n d

r0 ,−a12 w 1 n d

r0 , a122

+d¯2(n) n s¯3d+O(nw 2(m4n 1−d,−b1) w(m4n 1−d, b1)),

where d¯1(0)=−r a1
0 d˜ 1(0) ] 0, d¯2(0)=(3+b1)m −b1
4 d˜ 2(0) ] 0.
Again applying Lemma 6.16 to the function g3(n,d) we conclude that
g3(n, d)=0 has at most one root, so for a0=
1
4, Cycl(Ehh1c) [ 9.
(8.3) Case a0=
2n − 1
4n , n ¥ N, n ] 1. In this case, we have s1(a0)=
2
2n − 1 <1 and s3(a0)=
1
n.
Since s1 <1, this case is similar to the case (8.2), but simpler. The
function in (6.90) has the form

g(n, d)=c(n)+d1(n) n s¯1d+o(n s¯1d)+ C

n−1

j=1 d2jn s¯3(1 − d) j+d22(n) n 1−d

+d2(n) n 1−dw(m4n 1−d, b1)+O(nw 2(m4n 1−d,−b1) w(m4n 1−d, b1)),
(6.100)

where d1(0)=f m212(0)=f m¯ 30 ] 0, and by Lemma 6.14, d2(0)=f b2 ] 0.
After killing the terms c(n) and n s¯3(1 − d) j (j=1, 2, ..., n − 1) by the
derivation–division process, then similar to the process in (8.2), we obtain
that Cycl(Ehh1c) [ n+3.
(8.4) Case a0=
1
3. Note that in this case, s1(
1
3)=1, s3(1
3)=
2
3. Then
the function in (6.90) has the form

g(n, d)=c(n)+d11(n) n d+d1(n) n dw 1 n d

r0 , a12

+O 1 nw 2 1 n d

r0 ,−a12 w 1 n d

r0 , a122

+d21n s¯3(1 − d)+d2(n) n 1−d+o(n 1−d)

FINITE CYCLICITY 419

where d1(0)=f a2, a2 is the saddle quantity for the 2-dimensional system
near P1 on r=0. By Lemma 6.14,a2=−f m¯ 30 ] 0. Then, similar to the case
(8.3), we get the finite cyclicity of Ehh1c. L

Next we study the rest of the lower boundary graphics of Ehh families
using the following remark:

Remark 6.17. The system (3.10) is invariant under the transformation

(−t, −x, −m¯ 1,−m¯ 3) W (t, x, m¯ 1, m¯ 3) (6.101)

so the families Ehh7 and Ehh8 can be obtained from the families Ehh5 and
Ehh6 and the families Ehh11 and Ehh12 can be obtained from the families
Ehh9 and Ehh10. We will only need to deal with families Ehh5, Ehh6,
Ehh9 and Ehh10 as long as we do not use Hypothesis 6.10: c g <1.

Theorem 6.18. For the families Ehh4, ..., Ehh12, all the lower boundary
graphics have finite cyclicity.

Proof. For the family Ehh4, the proof is the same as for the family
Sxhh1 in the saddle case, so by Theorem 5.4, Ehh4c has finite cyclicity.
To prove the finite cyclicity of graphics Ehh5c, Ehh6c, Ehh9c, and
Ehh10e, take sections y1 and S3 as defined in Notation 5.6. We are going
to study the displacement map defined on the section y1,

L=Tˆ −T˜ : y1 Q S3, (6.102)

where Tˆ is the transition map through the blown-up singularity and T˜ is
the transition map along the regular orbit. Similar to the graphic Ehp1c, on
the section y1, we will use coordinates (n,c) with c ¥ In.

(1) Lower boundary graphics Ehh9c and Ehh10e. The lower bound-
ary graphics Ehh9c and Ehh10e are treated exactly as graphics Ehp1,
Ehp2c and Ehp3 in Section 6.2 (see also Remark 6.7).
(2) Lower boundary graphics Ehh5c and Ehh6c. Taking sections y4,
S4, and S3 in the normal form coordinates (Notation 5.6 and Fig. 25), the
transition map T˜ can be calculated by the decomposition

T˜ =R −1 p h4 p U,

where U: y1 Q y4 is the regular transition map defined in Proposition 6.12
with expression (6.41), G4: y4 Q S4 is the second type of Dulac map near

420 ZHU AND ROUSSEAU

FIG. 25. Lower boundary graphics (a) Ehh5c and (b) Ehh6c: Displacement maps.

P4, and R −1: S4 Q S3 is the inverse of the transition map R defined in
(6.76). Then a straightforward calculation gives

T˜
2(n, c)=m˜ 130(n)+m˜ 131(n) g4(n, w(r4, b1))+O(n 2p3(1 − c)w 2(m4n 1−c, b1))

−m13(n) n s¯3(1 − c)[1+h4(n, n 1−c, w 2(m4n 1−c, b1)], (6.103)

where r4=n 1−c[m141+O(n c, n 1−c)], m4=m141/r0, and m13(0) > 0.
Since the graphics Ehh5c and Ehh6c pass through a saddle and a saddle
node, respectively, the transition map Tˆ may not be C 2, and the graphics
need a special treatment.
Let us see Ehh5c first. As shown in Fig 25, in the normal form coordi-
nates in the neighborhood of the saddle point, take sections S¯ 1=
{x˜=−x0} and S¯ 3={y˜=y0} and let l(m¯ 0) be the hyperbolicity ratio of the
saddle point. Then for the transition map

D¯0=(d¯
0,D¯ 0): S¯ 1 Q S3

its second component D¯ 0(n,y˜) can be written in the form of Mourtada
(Proposition 4.2).
Take sections P1 and P3 as defined in Notation 5.6 in the normal form
coordinates; then the transition map Tˆ has the decomposition

Tˆ =D3 p T¯
03 p D¯0 p T¯
10 p G1, (6.104)

where

• G1: y1 Q P1 is the second type of Dulac map near P1 which satisfies
Theorem 4.14 with s=s1,
 FINITE CYCLICITY 421

• T¯
10: P1 Q S¯ 1 and T¯
03: S¯ 3 Q P3 are C k regular transition maps with

T¯
102=m100(n)+m101(n)y˜+m102(n)y˜ 2+O(y˜ 3)

T¯
032=m030(n)+m031(n)x˜+m032(n)x˜ 2+O(x˜ 3),

• D3: P3 Q S3 is the first type of Dulac map near P3 which satisfies
Theorem 4.10 with s=s3.

(2.1) Case l(m¯ 0)>1. Let

y˜ 1= o1
r p1
0 n p1w 1 n c

r0 , a12+n s¯1c 5l1+h1 1 n, n c, w 1 n c

r0 ,−a1226

y˜ 3=m030(n)+m031y˜ l
1[b0+f0(n,y˜ 1)],
 (6.105)

where l1=y0/r s¯1
0 >0, m030(0)=0, m031(0) ] 0, and f0(n,y˜ 1) ¥ (I .
0 ). Then
the second component Tˆ
2(n,c) can be written as

Tˆ
2(n, c)=o3rp3
0 w1 n
n0 ,−b321 n
n02s¯3+1 n
n02s¯3 5y˜ 3+f3 1n,y˜ 3, w1 n
n0 ,−b3226

(6.106)

where m˜ 031(0) > 0 and f˜ 031 is C k and satisfies the property (6.18).
Consider the displacement defined in (6.102). By (6.103) and (6.106), a
first derivation of L2(n,c) gives

L −
2(n, c)=Tˆ −
2(n, c)−T˜ −
2(n,d)

=1 n
n02 s¯3 51+“f3
“y˜ 3 1 n,y˜ 3, w 1 n
n0 ,−b3226

[m031(n) ly˜ l −1
1 (1+f01(n,y˜ 1))]

n s¯1c ln n 5s¯ 1l1+O(n p1(1 − c))+h11 1 n, n c, w 1 n c

r0 ,−a1226

− n s¯3(1 − c) ln n[m13(n) s¯ 3+O(n p3c)

+h41(n, n 1−c, w(m4n 1−c, b3))], (6.107)

where f01 ¥ (I .
0 ), and h11, h41 satisfy (6.18), and also “f3/“y˜ 3=
O(n p3w q3( n
n0 ,−b3) ln n
n0 ). L −
2(n,c) has the same number of roots as

L21(n,c)=
n −s¯3(1 − c)

ln n L −
2(n,c)

=−m13(n) s¯ 3+O(n p3c)+h41(n, n 1−c, w(m4n 1−c, b3))+O(y˜ l −1
1 ).
(6.108)

422 ZHU AND ROUSSEAU

Since m13(0) ] 0,so L21(n,c) ] 0. Thus L2(n, c)=0 has at most one root;
i.e., Cycl(Ehh5c) [ 1.
(2.2) Case l(m¯ 0)<1. In this case, L −
2(n,c) has the same number of
roots as

L¯ 21(n,c)

=n
 (s¯1+s¯3)c
1− l 51+
“f31
“y˜ 3 1 n,y˜ 3, w 1 n
n0 ,−b3226
5(s¯ 1l1) 1
1− l+O(n p1(1 − c))+h12 1 n, n c, w 1 n c

r0 ,−a1226

−y˜ 1(1+f11(n,y˜ 1))[(m13s¯ 3) 1
1− l+O(n p3c)+h41(n, n 1−c, w(m4n 1−c, b3))].
(6.109)

Then

L¯ −
21(n, c)=n
 (s¯1+s¯3)c
1− l ln n 51+O 1 n p3w q3 1 n
n0 ,−b32 ln n
n026
5(s¯ 1+s¯ 3)(s¯ 1l1) 1
1− l

1− l +O(n p1(1 − c))+h13 1 n, n c, w 1 n c

r0 ,−a1226

− n s¯1c ln n 5l1s¯ 1+O(n p1(1 − c))+h14 1 n, n c, w 1 n c

r0 ,−a1226

(1+f03(n,y˜ 1))

[(m13(n) s¯ 3) 1
1− l+O(n p3c)+h43(n, n 1−c, w(m4n 1−c, b3))], (6.110)

which has the same number of roots as L22(n, c)=−(n s¯1c/ln n)L¯ −
21(n, c).
Note that

L22(n, c)=l1s¯ 1(m13(n) s¯ 3) 1
1− l [1+f03(n,y˜ 1)]
51+O(n p1(1 − c))+h14 1 n, n c, w 1 n c

r0 ,−a1226

[1+O(n p3c)++h43(n, n 1−c, w(m4n 1−c, b3))]+O(n
 (s¯1l+s¯3)c
1− l )

] 0; (6.111)

hence, L2(n, c)=0 has at most two roots, yielding Cycl(Ehh5c) [ 2.
(2.3) Case l(m¯ 0)=1. In this case, for the second component Tˆ
2 of
Tˆ defined in (6.104), letting

y˜=m100(n)+m101n p1w 1 n c

r0 , a12+m11(n) n s¯1c 51+h11 1 n, n c, w 1 n c

r0 , a1226

(6.112)

FINITE CYCLICITY 423

and using the refinement of Roussarie [30] for T¯
03 p D¯0, then a straight-
forward calculation gives

Tˆ
2(n,c)=a00(n)+O 1 n s¯3w 1 n
n0 ,−b322

+n s¯3[a11(n)y˜ w(y˜, a11)+a22(n)y˜ +O(n s¯3y˜ 2w(y˜, a11))] (6.113)

where a00(0)=0, a22(0) ] 0.
Then the first derivation of L2(n,c) gives

L −
2(n, c)=n s¯3[a¯11(n) w(y˜, a11)+a¯22(n)+O(n s¯3y˜ w(y˜, a11))]
5m11(n) n s¯1c ln n 1 1+O(n p1(1 − c))+h11 1 n, n c, w 1 n c

r0 ,−a12226

− n s¯3(1 − c) ln n[m13(n) s¯ 3+O(n p3c)+h41(n, n 1−c, w(m4n 1−c, b3))],
(6.114)

where a¯11(n)=a11(1 − a11) and a¯22=a22 − a11 with a¯22(0) ] 0.
Denote

L0j(n, c)=1+O(n p1(1 − c), n p3c)

+h¯1j 1 n, n c, w 1 n c

r0 ,−a122+h¯4j(n, n 1−c, w(m4n 1−c,−b3))>0,

j \ 1.

where the h1j and h4j will have similar properties to those of h11 and h41,
respectively.
Then the equation L −
2(n, c)=0 has the same number of roots as

L22(n,c)

= n −(s¯1+s¯3)cL −
2(n,c)

w(y˜, a11) ln n 1 1+O(n p1(1 − c))+h11 1 n, n c, w 1 n c

r0 ,−a1222

=m11(n) a¯11(n)+m11(n) a¯22(n)
w(y˜, a11) − s¯ 3m13(n) n −(s¯1+s¯3)cL01(n,c)
w(y˜, a11) .

(6.115)

424 ZHU AND ROUSSEAU

The number of roots of the equation L22(n, c)=0 is at most one plus the
number of roots of

L23(n,c)=
n (s¯1+s¯3)cy˜ 1+a11w 2(y˜, a11)L −
22(n,c)
(s¯ 1+s¯ 3)m13(n)L02(n,c) ln n

=y˜ 1+a11w(y˜, a11)+m11(n) n s¯1cL02(n, c)+O(n (2s¯1+s¯3)c). (6.116)

Let
 L24(n, c)= L −
23(n,c)

s¯ 1n s¯1c ln n 51+O(n p1(1 − c))+h11 1 n, n c, w 1 n c

r0 ,−a1226.

Then

L24(n, c)=m11(n)[1+(1+a¯11)y˜ a¯11w(y˜, a11)]+s¯1L03(n, c)+O(n(2s¯1+s¯3)c)>0,
(6.117)

where the term y˜ a¯11w(y˜, a11) is positive and sufficiently large. Therefore,
L2(n, c)=0 has at most three roots which gives Cycl(Ehh5c) [ 3.
Now let us study the graphic Ehh6c. In the decomposition of Tˆ , the
second component of the transition map d¯0=(d¯
0,D¯ 0) satisfies (5.47).
Still letting y˜ be defined as in (6.112), and also letting

y˜ 3=m030(n)+O(y˜ i2), i2 \ 2,

then a first derivation of L2(n,c) gives

L −
2(n, c)=1 n
n02 s¯3 O(y˜ i2 −1) 51+“f3
“y˜ 3 1 n,y˜ 3, w 1 n
n0 ,−b3226

n s¯1c ln n 5s¯ 1l1+O(n p1(1 − c))+h11 1 n, n c, w 1 n c

r0 ,−a1226

− n s¯3(1 − c) ln n[m13(n) s¯ 3+O(n p3c)+h41(n, n 1−c, w(m4n 1−c, b3))],

which has the same number of roots as

L21(n,c)=
L −
2(n,c) n s¯3(c − 1)

ln n

=−m13(n) s¯ 3+O(n p3c)+h41(n, n 1−c, w(m4n 1−c, b3))+O(y˜ i2 −1) ] 0.

Therefore, L(n, c)=0 has at most one small root, i.e., Cycl(Ehh6c) [ 1. L

FINITE CYCLICITY 425

6.3.4. Intermediate graphics of the Ehh families.

Theorem 6.19. Under the generic assumption, all the intermediate hh
graphics of elliptic type of the 12 families Ehh1, Ehh2, ..., Ehh12 have finite
cyclicity.

Proof. Let C be any of the intermediate hh graphics of elliptic type of
the 12 families. Similar to the intermediate concave graphics of saddle type,
take sections P3 and P4 as defined in (5.22) in the normal form coordi-
nates in the neighborhood of P3 and P4, respectively. Consider the map

T: P3 Q P4

defined in Proposition 5.10. We are going to discuss the transition map
T2(0, y˜ 3) in the chart F.R. on r=0. By taking r3=0 and r4=0 in the
normal forms in the neighborhood of P3 and P4 in Proposition 4.6, we
obtain the normal forms in the neighborhoods of P3 and P4 in the chart
F.R. on r=0,
 r˙ i=(−1) i ri

y˜˙ i=(−1) i s3(a) y˜ i+(−1) i+1 o3r p3
i , (6.118)

where i=3, 4 and if a ] 1
4 then o3=0.
Let pi={ri=r0} (i=3, 4) be the two sections in the chart F.R. on r=0
parametrized by the normal form coordinate y˜ i. Then we are reduced to
study the 1-dimensional transition map

T2(0, y˜ 4): p4 Q p3

or its inverse. We will verify that for each family, the corresponding map
T2(0, y˜ 4) or its inverse satisfies one of the sufficient conditions listed in
Proposition 5.10.

(1) Family Ehh1. Let C be any intermediate graphic of the family
Ehh1. Since the systems (6.118) (i=3, 4) exist globally, so the map T2 exists
globally on p4 and not only in the neighborhood of p4 5 C. We are going
to prove that T2(0, y˜ 4) is either the identity or nonlinear. By Proposi-
tion 5.11, to prove the nonlinearity of T2, it suffices to prove that it is non-
linear at one point on p3. To do this, as shown in Fig. 26, we take line sec-
tions y4={y˜ 4=−y0} and y3={y˜ 3=−y0} in the normal form coordinates,
chosen such that any intermediate graphic of the family intersects either yi
or pi inside the neighborhood of Pi (i=3, 4) respectively. Then over some
subinterval of p4 the map T2 can be factorized as

T2=S3 p Tˆ
2 p S −1
4 , (6.119)

426 ZHU AND ROUSSEAU

FIG. 26. Transition map T for the intermediate graphic of family Ehh1. (a) Regular
transition, (b) T2.

where as shown in Fig. 26a, Si: yi Q pi (i=3, 4) are the regular transition
maps in the normal form coordinates in the neighborhood of P3 and P4,
respectively, and Tˆ
2: y4 Q y3 is the transition map which is in particular
defined near the lower boundary graphic Ehh1c.
We first calculate S3 and S −1
4 . Due to the easy form of system (6.118), the
transition S3 can be directly calculated by integration and

S3(0, r3)= 1
r s3
3 [−C1+C2o3 ln r3], (6.120)

where C1 and C2 are positive constants. Let vi=1/y˜ i (i=3, 4). If we
parameterize the section pi by vi, then by (6.120), we have

Si:vi= r s3
i
−C1+C2oi ln ri . (6.121)

In particular, the transition map S4 sends the points on section y4 in the
positive neighborhood of 0 to the points on the section p4 at infinity.

Remark 6.20. Although the normal form is only valid in the neigh-
borhood of P3 and P4, the systems (6.118) (i=3, 4) exist globally.

Note that if m¯ 30=0, then Tˆ
2 is the identity since the system is symmetric.
In the case m¯ 30 ] 0 we now turn to the calculation of Tˆ
2. As shown in
Fig. 26b, there are two saddles P1 and P2 at infinity in the chart F.R. on
r=0,so Tˆ
2 can be calculated by the following decomposition

Tˆ
2=V2 p D¯ 2 p S2 p D¯ 1 p U −1
2 . (6.122)

FINITE CYCLICITY 427

For the components of Tˆ
2 in (6.122), we have

• U2 and V2 are the regular transition maps defined in Proposition 6.12
and Corollary 6.13. By (6.41) and (6.65), we have

U −1
2 (0, r4)=m41r4+m42r 2
4+O(r 3
4)

V2(0, r2)= 1
m41 5r2 − m42
m 2
41 r 2
2+O(r 3
2)6. (6.123)

Also by Proposition 6.12 and Corollary 6.13, we have m42 ] 0 since m¯ 30 ] 0.
• D¯ 1 and D¯ 2 are Dulac maps in the neighborhood of the infinite
singular points P1 and P2
 D¯ 1: y1 Q p1

D¯ 2: p2 Q y2

and

D¯ 1(0, r1)=˛ r s1
1 (b10+f11(0, r1)) if s1 ] 1
b10r1+a1r1w1[1+ · · · ]+a2r 2
1w1[1+ ···]+··· if s1=1

D¯ 2(0, y˜ 2)=˛ y˜
 1
s1
2 (b¯ 10+f¯11(0, y˜ 2)) if s1 ] 1
b¯ 10y˜ 2+a1y˜ 2w2[1+ · · · ]+a2y˜ 2
2w2[1+ ···]+··· if s1=1,
(6.124)

where w1=w(r1, a1) and w2=w(y˜ 2, a1), f11, f¯11 satisfy (I .
0 ).
• S2 is the second component of the transition map S defined in
Proposition 6.1 and satisfies (6.1).

It follows from (6.122), (6.123), (6.124), and (6.1) that we have

• Case s1 ] 1.

Tˆ
2(0, r4)=m1r4+mˆ 42r 2
4+mˆ 2r 1+s1
4 +fˆ 1(r4, w(r4, a1)), (6.125)

where mˆ 2=f S '
2 (0)=f m¯ 30 ] 0 and mˆ 42=f m42 ] 0; also fˆ 1(r4, w(r4, a1)) is
C . and satisfies I .
0 .
• Case s1=1.

Tˆ
2(0, r4)=m1r4+a1m˜ 2r4w(r4, a1)[1+ ···]

+a2m˜ 1r 2
4w(r4, a1)[1+ ···]+···, (6.126)

where m˜ 1 ] 0. For the case s1=1 (a=
1
3), by the formula in [7], we have
the first saddle quantity a2=f m¯ 3 ] 0 (see (8.4) in the proof of
Theorem 6.15).

428 ZHU AND ROUSSEAU

So for both cases s1 ] 1 and s1=1,if m¯ 3 ] 0, Tˆ
2(0, r4) is nonlinear in r4.
Now we show that the map T2(0, y˜ 4) is nonlinear if m¯ 30 ] 0. Indeed, by
(6.119), we have
 S4=T −1
2 p S3 p Tˆ
2. (6.127)

If T2(0, y˜ 4) were linear in y˜ 4, i.e., T2(0, y˜ 4)=bˆy˜ 4 (bˆ ] 0), then by (6.127)
and (6.121), we should have

S4(0, r4)= (Tˆ
2(0, r4)) s3

bˆ[−C1+C2o3 ln Tˆ
2(0, r4)]
,

which is a contradiction to (6.121) for all the cases of s3, o3, and o4.
Thus all the intermediate graphics of the family Ehh1 have finite
cyclicity.
(2) Family Ehh3. As in Fig. 27a, we have a family of intermediate
graphics Ehh3b, Ehh3c, and Ehh3d. Note that Ehh3d is similar to the
graphic Ehh6c while Ehh2d is similar to the graphic Ehh10e. As in
Theorem 6.18, we conclude that Cycl(Ehh3c) [ 1 and Cycl(Ehh3d) [ 2.To
study the cyclicity of the graphic Ehh3b, we study the transition map T2
defined on p4 in the neighborhood of the graphic Ehh3c.
From the form of T2, we have limy˜ 4 Q 0 T2(0, y˜ 4)=−.. Hence T2 maps
(0, .) to (−., .). Since T2(0, y˜ 4) is analytic and bijective, it has to be
nonlinear in y˜ 4, thus any intermediate graphic Ehh3b has finite cyclicity.
(3) Family Ehh2. Its finite cyclicity follows from Remark 6.17.
(4) Family Ehh4. The proof is exactly the same as for the family
Sxhh1 of saddle type.

FIG. 27. Transition map T for the intermediate graphics of (a) Ehh3 and (b) Ehh2.

FINITE CYCLICITY 429

FIG. 28. Transition map T for the families (a) Ehh9b and (b) Ehh10d.

(5) Families Ehh9, Ehh10, Ehh11, and Ehh12. By Remark 6.17, we
only need to consider the intermediate graphics for the family Ehh9 and
Ehh10. We could have proved directly that Ehh10d has cyclicity [ 1, but
the proof given here will work simultaneously for Ehh9b and Ehh10d.
As shown in Fig. 28b, the corresponding transition map T2 can be
factored as
 T2=Tˆ
2 p S −1
4

Tˆ
2=W p D¯ 1 p U2, (6.128)

where U2,S4 are are given in (6.121) and (6.123), respectively, D¯ 1: y1 Q p1 is
given in (6.124), and the map W: p1 Q p3 is a C k map

W(n, y)=m¯ 0(n) y+o(y),

where m¯ 0(n)>0 and m¯ 0(n) small for Ehh10d.
Then a straightforward calculation gives

• Case s1 ] 1.
 Tˆ
2(0, r4)=m˜ 0(m¯) r s1
4 +o(r s1
4 ), (6.129)

where m˜ 0=f m¯ 0.
• Case s1=1 (a=
1
3).

Tˆ
2(0, r4)=m¯ 0(m¯)[c1r4+a1r4w(r4, a1)[1+ · · · ]

+a2r 2
4w(r4, a1)[1+ · · · ]+ ···], (6.130)

where we have the saddle quantity a2=f m¯ 30 ] 0 since m¯ 30 ] 0 for these
graphics.

430 ZHU AND ROUSSEAU

Let v4=1/y˜ 4, we parameterize section p4 by v4 and denote
T˜
2(0, v4)=T2(0, y˜ 4). We claim that the map T˜
2(0, v4) is nonlinear in v4 in
the neighborhood of v4=0. Indeed, if T˜
2(0, v4)=bˆv4 (bˆ ] 0), by (6.128) we
have T˜
2 p S4=Tˆ
2:

• Case s1 ] 1.

b r s3
4
−C1+C2 ln r4=m¯ 0(m¯) c1(n) r s1
4 +o(r s1
4 ).

• Case s1=1.

b r s3
4
−C1+C2 ln r4=c0(n)+m¯ 0(m¯)[c1(n) r4+a1r4w(r4, a1)[1+ ···]

+a2r 2
4w(r4, a1)[1+ · · · ]+ · · · ].

Since s1=
1−2a
a , s3=2(1 − 2a), and -a ¥ (0, 1
2), s1 ] s3, the above equations
are impossible, whether m¯ 0(n) is small (Ehh10d) or moderate (Ehh9b).
Ehh10b and Ehh10c are treated exactly as Sxhh2b and Sxhh2c in the
saddle case.
(6) Families Ehh5, Ehh6, Ehh7, and Ehh8. By Remark 6.17, we only
need to study families Ehh5 and Ehh6. The family Ehh6 is similar to Ehh2.
As shown in Fig. 29, the lower boundary graphic Ehh5c passes through
two saddle points. Similar to the case of Ehh 2 limy˜ 4 Q − . T2(0, y˜ 4)=0.
Hence T2 maps (−., .) to (0, .), yielding that T2 is nonlinear.
Altogether, we have proved that all the intermediate graphics of the Ehh
type have finite cyclicity. L

FIG. 29. Transition map T for the families (a) Ehh5b and (b) Ehh6b.

FINITE CYCLICITY 431

APPENDIX

A.1. Normal Form for a Saddle Node [8]

Theorem A.1. Consider a real analytic germ of a saddle node vector
field on (R 2,0) with one zero and one negative eigenvalue. Then it is C .

orbitally equivalent to its normal form

v0=z m+1(1+az m) −1 “
“z −w “
“w.

The equivalence may be taken analytic outside the stable manifold.

Theorem A.2. For any C . unfolding of a germ from Theorem 1 there
exists a finitely smooth orbital equivalence with the polynomial normal form

ve=P(e,z) “
“z
+z m+1(1+a(e)z m) −1 “
“z −w “
“w,

with P(e, z)=; m −1
i=0 bi(e)z i where bi(0)=0. For the critical parameter value
this equivalence is analytic outside the stable manifold of the saddle node
germ.

The proof uses the sectorial normalization theorem [19, 26]).

A.2. Proof of Lemma 6.14

Proof. By (3.8) with i=2, after a translation y=y2 − 1−2a
2 , the system
on r=0 in the neighborhood of P4 can be written as

r˙=r

y˙=−s3 y− 8ay 2

1+2y +e2r+O(r 2), (6.131)

where s3=2(1 − 2a). In the case s3=
1
n, n ¥ N, we have a=
2n − 1
4n .
By the linear transformation y=z+(e2/(3 − 4a)) r, system (6.131)
becomes
 r˙=r

z˙=−1
n z− 8az 2

1+2z
+
e¯2z(1+z)
(1+2z) 2 r+O(r 2), (6.132)

where e¯2=16ae2/(4a − 3). For convenience, instead of expressing a in
terms of n, we still keep a in the higher order terms.

432 ZHU AND ROUSSEAU

By normal form theory (see for instance [16, 20]), we will obtain the
normal form of (6.131):
 r˙=r

Z˙ =−1
n Z+ C

k

i=1 bi+1(rZ n) i Z, (6.133)

where b2, the coefficient of the term rZ n+1, is the first saddle quantity.
In order to obtain the normal form (6.133) from system (6.132), we
rewrite system (6.132) as

r˙=r

z˙=−1
n z−8a C

.

i=0 (−2) i z i+2+e¯2 5z− C

.

i=0 (−2) i (i+3) z i+26 r+O(r 2).

(6.134)

To prove b2 ] 0, we are going to apply the normal form theory to system
(6.134). The proof goes in two steps. For any n ¥ N, we will first kill the
terms rz, rz 2, ..., rz n. In the second step, we get rid of the nonresonant part
8a ; .
i=0 (−2) i z i+2.

(1) Kill the terms rz, rz 2,...,rz n successively.

(1.1) Kill the term rz first. Let z=z1+re¯2z1. Then by (6.134), we
obtain the equation of z1,

z˙1=−1
n z1 −8a C

.

j=0 (−2) j z j+2
1 −r C

.

j=0 (−2) j c1jz j+2
1 +O(r 2),

where c1j=e¯2[8a(j+1)+(j+3)] ] 0 and all the coefficients c1j have the
same sign as e¯2.
Note that if n=1, the coefficient of the resonant term rz 2
1 is c10 ] 0.
Then the first step stops here.
(1.2) Let n \ 2. Assume that by n−2 steps of near-identity trans-
formation of the form zk−1=zk+bkrz k
k, k=2, ..., n − 1, we get rid of the
terms rz 2
1,rz 3
1, ..., rz n−1
1 and obtain the equations of zn

r˙=r

z˙n=−1
n zn −8a C

.

j=0 (−2) j z j+2
n −r C

.

j=n − 2 (−2) j cnjz j+2
n +O(r 2), (6.135)

where for j \ n−2, cnj ] 0 and they have the same sign as e2.

FINITE CYCLICITY 433

(1.3) Kill the nonresonant term rz n
n in (6.135). Let zn=w+bnrw n,
where bn=−ncn, n − 2(−2) n−2; then

w˙=−1
n w−8a C

.

j=0 (−2) j w j+2 −cn+1, nrw n+1+rO(w n+2)+O(r 2), (6.136)

where
 cn+1, n=−[16abn+(−2) n−1 cn, n − 1]

=(−2) n−2 [16ancn, n − 2+2cn, n − 1] ] 0.

Therefore, we bring system (6.134) into the form

r˙=r

w˙=−1
n w− 8w 2

1+2w −cn+1, nrw n+1+rO(w n+2)+O(r 2). (6.137)

(2) Remove the nonresonant part −8w 2/1+2w.
By
 dw

− w
n − 8aw 2

1+2w

= dZ

− Z
n

we can solve for Z:
 Z=w(1+4nw)
 1−2n
2n . (6.138)

So if we make the change of coordinate (6.138), we bring the system (6.137)
into
 r˙=r

Z˙ =−1
n Z−cn+1, nrZ n+1+rO(Z n+2)+O(r 2). (6.139)

Hence we get that the first saddle quantity b2=−cn+1, n ] 0. L

ACKNOWLEDGMENTS

The authors thank Freddy Dumortier, Yulij Ilyashenko, Robert Roussarie, Dana
Schlomiuk, and Sergei Yakovenko for their valuable suggestions and comments. The first
author also thanks the Institut des Sciences Mathématiques for the financial support during
his Ph.D. studies in Université de Montréal.

434 ZHU AND ROUSSEAU

REFERENCES

1. V. I. Arnold and Yu. S. Ilyashenko, ‘‘Ordinary Differential Equations,’’ Encyclopedia
Math. Sci., 1, Dynamical systems, Vol. I, pp. 1–148, Springer-Verlag, Heidelberg, 1988.
[Current Problems in Mathematics: Fundamental Directions, Vol. 1, Akad. Nauk SSSR,
Vsesoyuz. Inst. Nauchn. i Tekhn. Inform., Moscow, 1985]
2. A. Andronov, E. Leontovich, I. Gordon, and A. Maier, ‘‘Theory of Bifurcations of
Dynamical Systems on a Plane,’’ Israel Program for Scientific Translations, Jerusalem,
1971.
3. P. Bonckaert, Conjugacy of vector fields respecting additional properties, J. Dynam.
Control Systems 3 (1997), 419–432.
4. F. Dumortier, Singularities of vector fields on the plane, J. Differential Equations 23
(1977), 53–106.
5. F. Dumortier, ‘‘Singularities of Vector Fields,’’ Monografias de Matematica [Mathema-
tical Monographs], Vol. 32, Instituto de Matematica Pura e Aplicada, Rio de Janeiro,
1978.
6. F. Dumortier, Techniques in the theory of local bifurcations: blow-up, normal forms,
nilpotent bifurcations, singular perturbations, in ‘‘Bifurcations and Periodic Orbits of
Vector Fields, Montreal, 1992’’ (D. Schlomiuk, Ed.), pp. 19–73, NATO Adv. Sci. Inst.
Ser. C Math. Phys. Sci., Vol. 408, Kluwer Academic, Dordrecht, 1993.
7. F. Dumortier, M. El. Morsalani, and C. Rousseau, Hilbert’s 16th problem for quadratic
systems and cyclicity of elementary graphics, Nonlinearity 9 (1996), 1209–1261.
8. F. Dumortier, Y. Ilyashenko, and C. Rousseau, Normal forms near a saddle node and
applications to finite cyclicity of graphics, preprint CRM, Université de Montréal, 2000.
9. F. Dumortier and C. Rousseau, Cubic Liénard equations with linear damping,
Nonlinearity 3 (1990), 1015–1039.
10. F. Dumortier and R. Roussarie, Canard cycles and center manifolds (with an appendix by
Chengzhi Li), Mem. Amer. Math. Soc. 121 (1996), no. 577.
11. F. Dumortier, R. Roussarie, and C. Rousseau, Hilbert’s 16th problem for quadratic
vector fields, J. Differential Equations 110 (1994), 86–133.
12. F. Dumortier, R. Roussarie, and C. Rousseau, Elementary graphics of cyclicity 1 and 2,
Nonlinearity 7 (1994), 1001–1043.
13. F. Dumortier, R. Roussarie, and S. Sotomayor, ‘‘Generic 3-parameter Families of Vector
Fields in the Plane, Unfoldings of Saddle, Focus and Elliptic Singularities with Nilpotent
Linear Parts,’’ Lecture Notes in Mathematics, Vol. 1480, pp. 1–164, Springer-Verlag,
Berlin/New York, 1991.
14. F. Dumortier, R. Roussarie, and S. Sotomayor, Bifurcations of cuspidal loops,
Nonlinearity 10 (1997), 1369–1408.
15. M. El Morsalani, Perturbations of graphics with semihyperbolic singularities, Bull. Sci.
Math. 120 (1996), 337–366.
16. J. Guckenheimer and P. Holmes, ‘‘Non-linear Oscillations, Dynamical Systems and
Bifurcation of Vector fields,’’ Appl. Math. Sci., Vol. 42, Springer-Verlag, Berlin/New
York, 1983.
17. A. Guzmán and C. Rousseau, Genericity conditions for finite cyclicity of elementary
graphics, J. Differential Equations 155 (1999), 44–72.
18. Y. Ilyashenko, Finiteness theorems for limit cycles, Russian Math. Surveys 45 (1990),
129–203.
19. Y. Ilyashenko, ‘‘Nonlinear Stokes Phenomena,’’ Advances in Soviet Mathematics,
Vol. 14, pp. 1–55, American Mathematical Society, Providence, RI, 1993.
20. Y. Ilyashenko and S. Yakovenko, Finite-smooth normal forms of local families of
diffeomorphisms and vector fields, Russian Math. Surveys 46 (1991), 1–43.

FINITE CYCLICITY 435

21. Y. Ilyashenko and S. Yakovenko, Concerning the Hilbert sixteenth Problem, in
‘‘Concerning the Hilbert 16th Problem,’’ Amer. Math. Soc. Transl. Ser. 2, Vol. 165,
pp. 1–19, Amer. Math. Soc., Providence, RI, 1995.
22. Y. Ilyashenko and S. Yakovenko, Finite cyclicity of elementary polycycles in generic
families, in ‘‘Concerning the Hilbert 16th Problem,’’ Amer. Math. Soc. Transl. Ser. 2,
Vol. 165, Amer. Math. Soc., Providence, RI, 1995.
23. P. Joyal and C. Rousseau, Saddle quantities and applications, J. Differential Equations 78,
(1989), 374–389.
24. A. Kotova and V. Stanzo, On few-parameter generic families of vector fields on the
two-dimensional sphere, in ‘‘Concerning the Hilbert 16th Problem,’’ Amer. Math. Soc.
Transl. Ser. 2, Vol. 165, pp. 155–201, Amer. Math. Soc., Providence, RI, 1995.
25. E. Leontovich-Andronova, On the generation of limit cycle from separatrice, Dokl. Acad.
Nauka 78 (1951), 641–644.
26. J. Martinet and J.-P. Ramis, Problèmes de modules pour des équations différentielles non
linéaires du premier ordre, Publ. Math. Inst. Hautes Étud. Sci. 55 (1982), 63–164.
27. A. Mourtada, Cyclicité finie des polycycles hyperboliques de champs de vecteurs du plan:
mise sous forme normale, in ‘‘Bifurcations of Planar Vector Fields, Luminy, 1989,’’
Lecture Notes in Mathematics, Vol. 1455, pp. 272–314, Springer-Verlag, Berlin, 1990.
28. A. Mourtada, Degenerate and non-trivial hyperbolic polycycles with two vertices,
J. Differential Equations 113 (1994), 68–83.
29. A. Mourtada, ‘‘Projection de sous-ensembles quasi-réguliers de Dulac-Hilbert. Un cas
noethérien,’’ Prépublication ou Rapport de Recherche, 124, Laboratoire de Topologie,
1997.
30. R. Roussarie, A note on finite cyclicity property and Hilbert’s 16th problem, in
‘‘Dynamical Systems, Valparaiso, 1986,’’ Lecture Notes in Mathematics, Vol. 1331,
pp. 161–168, Springer-Verlag, Berlin/New York, 1988.
31. R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix
loop of planar vector fields, Bol. Soc. Brasil. Mat. 17 (1986), 67–101.
32. R. Roussarie, ‘‘Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem,’’
Progress in Mathematics, Vol. 164, Birkhäuser, Basel, 1998.
33. C. Rousseau and H. Zhu, Hilbert’s 16th problem for quadratic systems and finite cyclicity
of graphics with a nilpotent singularity of saddle or elliptic type, in preparation.
34. J. Sotomayor and R. Paterlini, Bifurcations of polynomial vector fields in the plane, in
‘‘Oscillations, Bifurcation and Chaos, Toronto, Ontario, 1986,’’ CMS Conf. Proc., Vol. 8,
pp. 665–685, Amer. Math. Soc., Providence, RI, 1987.
35. S. Sternberg, On the structure of local homeomorphisms of euclidean n-space, II, Amer.
J. Math. 80 (1958), 623–631.
36. F. Takens, Unfoldings of certain singularities of vector fields: generalized Hopf bifurca-
tions, J. Differential Equations 14 (1973), 476–493.
37. F. Takens, Singularities of vector fields, Publ. Math. l’IHES 43 (1974), 47–100.
38. H. Zhu, ‘‘Finite Cyclicity of Graphics with a Nilpotent Singularity of Saddle or Elliptic
Type,’’ Ph.D. thesis, University of Montreal, September 1999.

436 ZHU AND ROUSSEAU
