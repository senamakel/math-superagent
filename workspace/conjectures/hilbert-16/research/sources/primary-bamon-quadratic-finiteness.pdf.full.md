<!-- source: https://www.numdam.org/item/10.1007/BF02699193.pdf | converted from PDF -->

PUBLICATIONS MATHÉMATIQUES DE L’I.H.É.S.

RODRIGO BAMON
Quadratic vector ﬁelds in the plane have a ﬁnite number of limit cycles

Publications mathématiques de l’I.H.É.S., tome 64 (1986), p. 111-142

<http://www.numdam.org/item?id=PMIHES_1986__64__111_0>

© Publications mathématiques de l’I.H.É.S., 1986, tous droits réservés.

L’accès aux archives de la revue « Publications mathématiques de l’I.H.É.S. » (http://
www.ihes.fr/IHES/Publications/Publications.html) implique l’accord avec les conditions géné-
rales d’utilisation (http://www.numdam.org/conditions). Toute utilisation commerciale ou im-
pression systématique est constitutive d’une infraction pénale. Toute copie ou impression de
ce ﬁchier doit contenir la présente mention de copyright.

Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/

QUADRATIC VECTOR FIELDS IN THE PLANE HAVE
A FINITE NUMBER OF LIMIT CYCLES

by RODRIGO BAMON

INTRODUCTION

An isolated periodic orbit of a vector field in R2 is called a limit cycle. Part of
Hilbert's i6-th problem is to find an upper bound for the number of limit cycles of
polynomial vector fields of a given degree. Still today, very little is known about these
upper bounds. Moreover it is not known if an arbitrary polynomial vector field has
a finite number of limit cycles.
In 1923, Dulac [D] claimed that all graphs (see definitions in Chapter i) of analytic
vector fields in the plane are finite (i.e. they are not accumulated by limit cycles). From
this result follows the finitehess of limit cycles for polynomial vector fields. Recently,
IPyaSenko [I] gave a strikingly simple counterexample to one ofDulac's main assertions,
and gave a correct proof for the fact that all hyperbolic graphs (see Chapter i) of analytic
vector fields are finite. This represents a major step and is essential for the result in
this paper.
Around 1956 Petrovskii and Landis [P-L^, P-Lg] claimed that quadratic vector
fields in the plane have at most 3 limit cycles. In 1959 they withdrew their proof [P-Lg],
Later in 1979, the Chinese mathematician Shi Song Ling [Sh^, Shg] produced examples
of quadratic vector fields with 4 limit cycles, disproving the estimate of Petrovskii and
Landis.
For our work we start from the fact that a polynomial vector field with infinitely
many limit cycles must contain a graph (bounded or unbounded, see Chapter i) which is
accumulated by limit cycles. This follows from the Poincar^-Bendixon Theorem.
Taking into account very special qualitative properties of quadratic systems, all
of which are recalled in Chapter i, we prove the following theorem

The author acknowledges the very kind hospitality and a fine mathematical atmosphere provided by
IMPA/CNPq during the preparation of this paper. This work was partially supported by CNPq (Brasil),
CONIGYT (Chile) and PNUD-UNESCO.
 Ill

u s RODRIG O BAM6 N

Theorem B. — All graphs (bounded or unbounded) of quadratic vector fields in R 2 are finite.

From the fact we mentioned above follows immediately

Theorem A. — Every quadratic vector field in R 2 has a finite number of limit cycles.

In 1983, Chicone and Shafer [Ch-S] proved the finiteness of bounded graphs.
Here we give an alternative proof.
In Chapter i we give definitions and general information. We also recall pro-
perties of quadratic systems. In Chapter 2 we prove Theorem B.
We will denote by /2 the space of quadratic vector fields endowed with the topology
of the coefficients.

Acknowledgements. — I am indebted to a number of people for helping me in several
ways to achieve the results in this paper, among them A. Lins Neto, R. Moussu, J. Palis,
J. Sotomayor. I also acknowledge N. Yus for his earlier stimulus in the area of Dyna-
mical Systems.

i. Preliminaries

1.1 . General definitions

Let X be a differentiable vector field in R2.

Definition i. — An orbit <p(^) == {x(t)^y(t)) of X is called a separatrix of X if its
co-limit set (or its a-limit set) is a singular point p == (^o»^o) °^ ^  an(^

1) ^m  xw  ^  xo lor . um ,  xw  ^  x0} exists and belongs to Ru{±oo} ;

2) there exists e^> o and T >  o (T < o) with [(p(^) —p\<^  for all t^  T (^  T)
such that for all e > o there exist an orbit ^(t) of X and T >  T (T < T) such
that |  ^(t) — <p(^) |  < e for all t e [o, T] (t e [T, o]) and |  ^(T) — p |  >  e^.

Definition 2. — A closed curve F in R2 is called a graph ofX if it can be parametrized
by a : [o, i] ->R 2 of class C1 with a(o) =  a(i) satisfying:

1) if y!(t) == o then X(a(^)) =  o;
2) if v!(t) 4= o then a(^) belongs to a separatrix of X and there exists X > o such that
a'(f) == XX(a(f)).

We will say that a graph F of X has a return map if for all cross sections S of X
intersecting F, there exists p e S  such that (*)Q&) n S + 0  or aQ&) n S  4= 0.

i.  2. Poincarfs compactification

Let S2 == { (A-,^, z) e R3 [ x
2 +y 2 +  z
2 =  i} and let H4- and H- be the hemispheres
{{x,y, z) e S2 [ z >  o] and {(A?,J», z) e S2 [ z <  o}, respectively.

112
 QUADRATIC VECTOR FIELDS "3

To a differentiable vector field X in R2 we can associate vector fields X4' and X~
in H4' and H~ in the following way: first we define in {{x^, z) \  z == i} the vector
field X{x,jy, z) =  (X^j?), o) and then we project it by central projection onto H4'
and H". When X is a polynomial vector field of degree n, it happens that multiplying X
4"
and X~ by ^ n- l we obtain a vector field in H + u H~ that can be continuously extended
to S1 =  {{x,jy, z) e S2 |  z == 0} in such a way that the resulting vector field on S2 is
analytic.
This is the so-called Poincare compactification of X and is denoted by ^(X). This
construction allows us to study the flow of a polynomial vector field far away from the
origin. The equator S1 of S2 represents the "points at infinity 5? and it happens (by
construction) that points at infinity remain at infinity under the flow of ^(X) (i.e. S1 is
invariant for ^(X)).
A graph of X containing separatrices (and thus singularities) at infinity will be
called an unbounded graph.
To study a polynomial vector field at infinity we consider the following coordinates

u^=jylx

,^i == i/^" and ' ^2 = ^y
^2 ==
 I^-

Geometrically they can be represented as follows:

If X 6 /2 is given by

( x =  P(x,jy) == a +  mx +  ny +  ax
2 +  bxy +  cy
2

{ -—-_- _
U  == QX-^jO ==
 a +  mx +  n^ +  ^ x2 +  bxy +  cy
2
'
(i)

then in the coordinates u^ v^ it is expressed in the form

u !  == Pl(^l.  ^l)

v !  =  Q.l(^l.  ^l)
(2)

with
 x,:

^(^i?  ^i) =  a +  (b — a) u^ +  mv^ +  {c — b) M
2 +  (n — m) u^ v^
+  ao
2 — cu\ — nu^ v^ — a^  y
2

Q-i("i5 ^i) =  — ^i  — ^^i »i — wy
2
 — ^ 2 v^ — nu^v[— a^
 123

15

"4  RODRIG O BAMO N

and in the coordinates u^ v^ it is expressed in the form

(3) x  • [ u2  == P2(M2? V2)

2 [^ 2 =0.2(^2^2)

with Pg(^, ^) =  ^ +  (& -  ^  ^  +  ^2 +  (^ -  A) MJ +  (w -  n) ^  ^
+  az^ — fl^j — wz/j ^  — a«2 yj

0.2(^25 ^  == — ^2 — ^2  ^2 — ^j  — ^j  ^2 — ^ 2  ^  — az|.

Z^wwfl I.I.—  Every X  e ^2 AA? ow^, two or three pairs of symmetric singularities at
infinity or the whole infinity is filled up with singularities.

Proof. — If X e /2 is given by (i), using the expressions of X^ and X^ we have
that the singularities at infinity are obtained by solving
Pi(^i, o) =  a +  (b -  a) u^ +  (c -  b) u\ -  cu\ == o
an d  ^( ^  o) =  c +  {b -  c) u^ +  (a -  ~b) 4  -  ai4 =  o.

From these expressions the lemma follows immediately.
Note that ^  =)= o and ^  == "F1 represent the same point at infinity. D

Remark. — By a rotation of coordinates we can always carry one of the pairs
of symmetric singularities at infinity to the pair of points p =  (o, i, o) and
—^==(°3—i5o) - Hence we can always suppose that the origin in the (^, z/g) -plane
is a singularity of X^ or, in other words, we can always suppose c == o.
The following corollary is now clear.

Corollary i.ss. — Let X  e^ 2 be given by (i) with c =  o. Then:
I)  X  has one pair of symmetric singularities at infinity if  and only if  [(b — a)2 — 4:0(0 — b) <  o]
or [b — a ==c -— b == o and a +  o];
II)  X  has two pairs of symmetric singularities at infinity if  and only if

[(b — a)2 — 4^{c — b) =  o and c — b +  o]

<^ [c — b == o and 6 — a =(= o];
III)  X  has three pairs of symmetric singularities at infinity if  and only if  (b — a)2 — ^a{c — b) >  o
and c — b == o;
IV)  the whole infinity is filled with singularities of X if  and only if  c — b ==b — a == a == o.

The proof of Theorem B in the next chapter will consider separately each one
of the cases arising from this corollary.

1.3. General properties of quadratic vector field in R 2

Among the properties of planar quadratic vector fields there is a simple but basic
one that we will use throughout the paper. It will be refered to as the periodic orbit
property and says the following:

214
 QUADRATIC VECTOR FIELDS 115

If a planar quadratic vector field has a periodic orbit Y, then in the compact
region bounded by Y there is a unique singularity. Moreover, the linear part of the
vector field at this singularity has conjugate complex eigenvalues.
This property can be used to find simple expressions for the vector field. In
fact, if a quadratic vector field X has a periodic orbit, it is clear that there exists an
afine change of coordinates such that

f x =  mx -y  +  P^x,y)
'  [^  == x +  my +  Q^,j0 ,

where P^ and Q^ are homogeneous polynomial vector fields of degree two. In some
cases we will use the fact that this form of X is invariant under rotations.
Let us recall another basic property of planar quadratic vector fields.

Contact property. — Let X e ^2 be a quadratic vector field in R2. Then every
straight line t in R2 is either invariant or has at most two contacts with X (i.e. points
where t is not transversal to X).
This property enables us to find geometric properties for bounded or unbounded
graphs of quadratic systems. For example we can prove:

(i) all graphs with return map enclose a convex region;
(ii) a graph with return map and with at least two singularities must contain the straight
line segment joining two adjacent singularities. In this case the quadratic vector field
has an invariant line.

With these properties we obtain simple expressions for the vector field. In fact,
if a quadratic vector field X has an invariant line, then there exists an afine change of
coordinates such that

I
 x =  x{m +  ax +  by)
X : i-Q^j)
and if X has two transversal invariant lines then

[x==x{ m +ax +  by)

9 [^  ==J^+^+90 .

Whenever necessary we will use these forms of X.
Let us recall two more properties of quadratic systems.

Invariant line property. — If a quadratic system has an invariant line then it has
at most one limit cycle.

Two invariant lines property. — The quadratic system

f x == x(m +  ax +  by)

^y ==jy{n +~bx +cy)

has no limit cycle.
 115

116 RODRIGOBAM6 N

Although the invariant line property may substantially simplify the proofs, we
are not going to use it, because we do not know of a good reference for its proof.
However, we shall make use of the two invariant lines property, first proved by Bautin
(see [G]).

i.  4. Singularities and periodic orbits

Let p be a singular point of a vector field X in R2 (i.e. X(^) == o) and let X^, Xg
be the eigenvalues of DXQ&). We say that p is hyperbolic if Re \  + o, i =  i, 2, that
it is semi-hyperbolic if \  Xg == o but \  +  ^2 + °  an(! ^^  lt: ls a  degenerate singularity
if Xi == Xg == o. Moreover, we say tho.tp is a center type singularity \t\  and \  are complex
conjugate with zero real part.
For the moment we are interested in the description of the flow of X in a neigh-
borhood of p (the topological type of p).
First we define some types of singularities by their geometrical features:

saddle attractor repellor saddle-node

If the orbits of an attractor (repellor) spiral around the singularity we speak of
a focus; if not we speak of a node.
Let us now relate hyperbolicity with the above topological types.
Ifj&isa hyperbolic singularity of X and \,  X^ are the eigenvalues ofDX(^), then

p is a saddle if \  Xg < o, an attractor if Re \  <  o, i == i, 2, and a repellor if Re \  >  o,
i == 1,2. Moreover, p is a focus if and only if\  and X^ are complex conjugate numbers.
These are simple basic facts about dynamical systems and can be seen for example
in [P-M].
Ifp is a semi-hyperbolic singularity of X there are two local invariant differentiable
curves intersecting transversally at ?, such that the behavior of X along these curves
determines the topological type of p. The tangent lines to these curves at p are the
lines generated by the eigenvectors ofDX(^). The invariant curve whose tangent line
at p is generated by the eigenvector associated with the vanishing eigenvalue is called
the center manifold of p. The flow of X on the center manifold ofp is given by the first
nonzero derivative/^(o) of an associate one-dimensional differential equation x ==f{x)
for which f{o) ==y(o) =  o. The flow on the other invariant curve is determined by
the sign ofX, the nonzero eigenvalue. With this, the topological type of p is a saddle-
node if k is even, a saddle if k is odd and X./^o) < o and a node if k is odd and
X./^o) >  o (attractor if X < o and repellor if X > o).
The center manifold theory needed here can be found in [H-P-S] or [Ca],

116
 QUADRATIC VECTOR FIELDS 117

The topological type in the degenerate case can be obtained by means of the
blowing-up method. This method consists in <c opening "  (blowing-up) the singularity
into a circle using for example the map
9 : R x S1 -  R2

(r, 6) h> (r cos 6, r sin 6).

(We suppose that the vector field X is defined in an open set ofR 2 and has the degenerate
singularity p at the origin.) An important fact is that there exists a vector field X in
R X S1 (the blow-up of X) verifying

D(p^e)(X(r, 6)) == X(<p(r, 6)) for (r, 6) € U

and leaving {0} X S1 invariant. The set U is open in R X S1 and contains {0} X S
1.
If we know the flow of X in a neighborhood of {0} X S1 (for example if all the singu-
larities of X in {0} X S1 are hyperbolic or semi-hyperbolic), then 6C blowing down "
X we obtain the topological type of p. If X has degenerate singularities along {0} X S
1,
we blow-up again each one of these singularities and observe if we can determine the
corresponding flows. If not, we blow-up again and again. Fortunately this process
ends; in fact (X being analytic) we know that after a finite number of blowings-up we
only get hyperbolic and semi-hyperbolic singularities. This allows us to describe the
topological type of p.
In sections 2.1.1, 2. 2 (1.2) and 2.2 (11.2), we will give the topological types
of all degenerate singularities which will be needed.
The blowing-up method can be seen in detail in [A], [Du] and [T].
Finally, we recall that the topological type of a center type singularity p of an
analytic vector field is either a focus or a center (all orbits in a neighborhood of? are
periodic).
A periodic orbit y is called an attractor (repellor) if it is the co-limit set (a-limit set)
of all points in a neighborhood of y.
Let X be a vector field in R2 and let y be a periodic orbit of X of period T. The
number
 c =  f 7  div X^(t))  dt

is called the characteristic exponent of y-
It is a well known fact (see [A], [S]) that for c >  o the orbit y is a repellor and
for c < o it is an attractor.

1.5. Il^yaSenko's Theorem ([I])

Definition. — A graph F of a vector field X in R2 is called a hyperbolic graph of X
if all singularities of X contained in F are hyperbolic.

Theorem (IPyaSenko). — Every hyperbolic graph of an analytic vector field in R 2 is finite
(i.e. not accumulated by limit cycles).
 117

n8 RODRIG O BAMO N

This theorem is crucial for our result because it allows us to consider only the
non-hyperbolic graphs.

1. 6. Dulac's Proposition

Definition. — A semi-hyperbolic singularity p of a vector field X in R2 is called
contractive if div XQ&) < o and expansive if div X(^) > o. Notice that in this case
div X(j^) is the nonzero eigenvalue of DXQ&).

Proposition (Dulac [D]). — Every graph of an analytic vector field in R 2 which contains

only hyperbolic or contractive (expansive) semi-hyperbolic singularities is finite.

The proof of this fact is straightforward.

2. Proof of Theorem  B

2.1. We will first prove that all bounded graphs of quadratic vector fields are
finite. To do this we observe that a quadratic vector field has at most four singularities
in the plane. Since we are interested in periodic orbits we may suppose that one of
the singularities is a focus or a center (see i . 3 and 1.4). Hence bounded graphs contain
one, two or three singularities (this is true for every quadratic vector field; see Berlinskii's
Theorem in [C]).

2.1.1. Let us first consider graphs with one singularity. If the singularity is
either hyperbolic or semi-hyperbolic the graph is finite. This follows from IPyaSenko's
Theorem and Dulac's Proposition, respectively. Suppose now that the singularity is
at the origin and that both eigenvalues are zero. If the linear part of the vector field
at (o, o) is identically zero then the vector field is homogeneous and there is no limit
cycle. We may then suppose that after a linear change of coordinates the vector field
has the form
 x =y  4- ax
2 +  bxy +  9^
2

y == ax2 +  T^xy +  cy
2.

Following the blowing-up method we observe that if a + o the topological type
of the origin is
 •>x

a >  o a <  o

Since the line y == o is transversal except in (o, o) this singularity does not belong
to any graph. Thus, necessarily a == o.

118
 QUADRATIC VECTOR FIELDS "9

In this case [a == o) the line y =  o is invariant and the existence of a periodic
orbit implies both ~b =f= o and the existence of another singularity which must be a
focus or a center. Changing coordinates by (x,y) ^  (bx +  cy, 7^) with an appro-
priate X, we obtain the following form for X:

x =  ny +  ax2 +  bxy — ny2

-?v I .
y =  xy

with (o, o) and (o, i) as singularities. For (o, i) to be a focus or a center it is necessary
that b
2 <  4^. We also need a 4= o.
Suppose b =  o. Then the vector field verifies A^X == — X for A(x,y) == (—j/, x).
It follows that (o, i) is a center and that there is no limit cycle.
Now denote by X^ the vector field
x  == ny +  ax2 +  bxy — ny2

V == xy.
X•b '

Then, X, =  Xo +  b M  and det (XQ, X,) = -  bx2y2. It follows that the

orbits of X^ are topologically transverse to the ones of Xo and since Xo has a center
and is symmetric with respect to thej^-axis we see that X^, b 4= o, does not have any
periodic orbit. Moreover, calculating the topological type of (o, o) (by the blowing-up
method) we conclude that XQ has the following bounded graphs according to the values
of the coefficient a.
 a <  o o < a <  1/2

Also, the vector fields Xo for a ^ 1/2 and X^ for b + o do not have any bounded graph.
This settles the case of bounded graphs with one singularity.

a. i. a. Let us now consider bounded graphs with two singularities. Since we
are interested in graphs with return map we may suppose (by the contact property)
that both singularities are points of an invariant line for the vector field. By a linear
change of coordinates we can carry these points to (o, o) and (o, i). The vector field
then takes the form
 i x == x(m +  ax +  by)

\^y =  cy{y — i) +  mx +  ax
2 +  ^xy c ^  o.

The eigenvalues of the linear part of X are {m, — c} at (o, o) and {m +  b, c}
at (o, i). Since ^4= o each singularity is either hyperbolic or semi-hyperbolic. If

119

120 RODRIGOBAM6 N

at least one of them is hyperbolic then the graph is finite (by IPyaSenko's Theorem
or by Dulac's Proposition). If both singularities are semi-hyperbolic then m =  b == o.
But in this case x =  ax
2 and there is no bounded graph.

2.1.3. Finally, if there is a graph with three singularities and with return map
then, by the contact property, there are three invariant lines and by the two invariant
lines property we know that there is no limit cycle.
This conclude the proof for bounded graphs.

2.2. Now we prove that all unbounded graphs are finite. We proceed by consi-
dering separately each one of the relations in Corollary 1.2.

2.2 (I.I ) (~b -  a} 2 -4a(c-b) < 0

Let X e •y
2 be given by (i) with c === o and verify the relation above. In this
case p == (o, i, o) and — p are the unique singularities at infinity. Since X is expressed
in coordinates (u^,v^) (see 1.2) as

u^ =  {b — c) u^ +  nv^ +  .. .
Xg : . _
^2 == —  CZ/2 +  • .  .

the point p is hyperbolic for X restricted to infinity ((^-axis) and it is hyperbolic if and
only if ^4= o.

Lemma 2.i« — If  X  has an unbounded graph F, then:
(i) p and — p are saddles [and so b +  o) and they belong to T. An arc at infinity joining p

and — p must be contained in F.
(ii)  The line t :  x == — njb is invariant and contained in I\
(iii)  There exist coordinates in which we can write

{. x == xy
X : . with b
2 -  4^(c- i) <  o.
[y == Q.(^j0

Proof. — Part (i) is clear. To prove (ii) we notice that
<X( - n\b,y\ (i, o)> == a -  mn\b +  an^b2

proving that I is invariant or transversal to the flow. If it is transversal, the separatrices
of the saddles p and — p must be on different sides off (see the figure below). Therefore,
there is no unbounded graph

120
 QUADRATIC VECTOR FIELDS 121

We now prove (iii). By translating coordinates we carry t to the line x == o.
The vector field is now given by

1 x == x(m +  ax +  by)
\y
 =  Q^jO.

Since b =h o (p is a saddle), we obtain the desired form for X by changing
coordinates: [x^y) [-> (x, m +  ax +  by) D
Let X e ^2 be given by

x ==• xy

y == Q.(^)
X : b
2
 — 40(0 — i) < o.

Since in this case
 ^2 =  ^E 1  —  c  —  ^2  ~~ ^ 2  —  au ^  ~  mu 2  ^2 —  az^ ]
X«:
 ^2 =  Q.2("2> ^2) =  -  ^ 2  +  • • •
2 •

we conclude that the z^-axis is invariant and that the flow along this line is given by

^2 =  Q^ 0 ?  ^2) == —  ^2  —  n ^  —  a ^ -

Thus, the origin (^2, v^) == (o, o) (and hence p) is a saddle if and only if (i — c) c> o
(hyperbolic case) or c == n == o and a> o (non-hyperbolic case).
For X e ^2 as above we will prove the following scheme:

n2 — 4ac> o : there is no unbounded graph

( n 4= o : graph as in Fig. i
c{i — c) >  o < w
2 — 4ac =  o < b =f= o : graph as in Fig. 2

^ === o : graph as in Fig. 3
n == o

n2 — ^OLC < o : graph as in Fig. 4

1) =t= o : graph as in Fig. 5
c == n =  o and a > o ^ == o : graph as in Fig. 6

FIG. i. — The graph does not have a return map and so it is finite

FIG. 2. — Calculating the characteristic exponent it follows that three
is no periodic orbit
 121

16

122 RODRIG O BAM6 N

FIG. 3. — There is symmetry, therefore the graph is finite

FIG. 4. — By IFyasenko's theorem, the graph is finite

FIG. 5. — Same as in Fig. 2

FIG. 6. — Same as in Fig. 3

Let us consider the case c(l — c) >  0. We first look at the singularities of X
on the invariant line i : x =  o. These singularities are given by the roots of

Q(o,j/) == a +  ny +  cy
2 =  o.

If n2 — 4ac >  0, there are two singularities on t which are hyperbolic for X restricted
to t. In this case there is no unbounded graph. For n2 — 4ac =  0, there is a unique
singularity on/', namely ?Q == (o, — n/2c), which has eigenvalues — n^c and o. Thus,
for n 4= o, ?Q is a saddle-node and we obtain the graph of Figure i.
For n === o, we necessarily have a == o. Notice that if there is a periodic orbit
T == (Vi? T2). ^ "^ust be contained in {x >  0} or in {x <  o}. Also, from the expression
for X, we have y2 =  Yi/Yi • Calculating the characteristic exponent of a periodic orbit
of period T we obtain:

122
 QUADRATIC VECTOR FIELDS 125

f div X(y(^)) dt == f ~b^{t) dt +  F {20 +  i) ^(t) dt
J o J o J o

=~bS\i{t)dt+(2C+i) C^dt
Jo Jo YiW

==& !\^)dt.
Jo

So, if ~b + o, all possible periodic orbits in the same half-plane as well as the
singularities must be of the same type: all repellors or all attractors. Since this is.
impossible, there is no periodic orbit at all. Finally, for ~b == o, X has the form

f x =  xy
X =  . _  _
\^y =  mx +  ^  +  cy
2

and we easily show that A, X == — X for A{x,y) =  (A-, —y). The flow of X is then
given in Figure 3.
When n2 — 4dc< 0 there are no singularities on t and we get the graph of
Figure 4 with hyperbolic singularities. By IPyaSenko's Theorem we know that these
graphs are finite.
Let us now consider the case c =  n =  o and a >  o. In this case there are no
singularities on the invariant line I : x == o, and there are two singularities lying on
different sides of f. Both of them are center-type singularities. If there is a periodic
orbit Y == (vi, ^)  of period T we calculate its characteristic exponent and obtain the

number ~b j yi(^) dt. As before, we see that there is no periodic orbit if ~b 4= o. For

T) == o the vector field verifies A^ X =  — X for A : {x^y} -> (x, —y ) and so we
obtain the graph of Figure 6. This proves Theorem B in the case (I.i) .

2.2 (1.2) A — a ==c •— b •== 0 and a 4= 0.

Let X e /2 be given by (i) with c == o and verify the relations above. In this
case p =  (o, i, o) and — p are the unique singularities at infinity. Let X^ be the
expression of X in coordinates (^, v^) (see 1.2). Since

f" 2  == ^ 2  +  .  • •
-^2  :  ([  Z;2 =  —  ^2  +  • .  .,

the point p is not hyperbolic for X restricted to infinity (^-axis) and it is semi-hyperbolic
if and only if b 4= o.

Lemma 2.2. — Let b 4= o. If X has an unbounded graph F, then:

(i) p and — p are saddles and they belong to F. An arc at infinity joining p and — p is contained
in r.
 123

^  RODRIGOBAM6 N

(11) The line t : x == — nfb is invariant and contained in F.
(iii) There are coordinates in which

( x == xy
X : .  _ _
\y =  a +  mx +  ny +  ax
2 +jy 2.

Proo/. — Since p is semi-hyperbolic and is a node along the center manifold (the
infinite line), it is either a node or a saddle. If it is a node, no unbounded graph is
possible.
The rest of the proof goes as for Lemma 2.1. D

Lemma 2.3. — Let b == o. IfX  has a periodic orbit then there are coordinates in which

(
 x == mx — y +  ax
2
X : _ a +  o.
y == x +  my +  ax2 +  <yw

Proo/. — We first note that the conditions ~b — a == o, & == c == o and o 4= o
are invariant under affine change of coordinates that keep p == (o, i, o) fixed. The
lemma then follows by the periodic orbit property. D
Notice that we are only interested in quadratic vector fields which have periodic
orbits. Therefore, we will frequently use the coordinates given by Lemma 2.3.
If a + o, using {x,y) t-> (s^ x, Sgj), s, == ± i, i == i, 2 if necessary, we can
suppose a >  o and a >  o.

Lemma 2.4* —  Let X  6 y2 be given by

(
 x == mx — y 4- ax2 a >  o

y =  x +  my +  ax2 +  axy a >  o.

Then the singularity ^==(0,1,0 ) at infinity has the following topological type:

Proof. — By blowing-up the singularity at the origin for the vector field

f ^ 2 =  -  V2 -  ^ J  -  ^  V2
2 • 1 .
[ v^ =  — au^ ^  — wyj — ai4 ^  — ^2 ^

we recognize the above topological type. D

124
 QUADRATIC VECTOR FIELDS

We will now prove the following scheme:
 125

ah >  o : there is no unbounded graph
b 4= o n + o : graph as in Fig. 7
ab <  o (coordinates as in Lemma 2.2) n =  o : graph as in Fig. 8

m =  o : X is Hamiltonian

m 4= o : since div X^jy) == 2W, there is no
periodic orbitb == o (coordinates
as in Lemma 2.3)
 a == o
 ( 2am — a == o : graph as in Fig. 9

f 2am — a =(= o : there is no unbounded graph.
a >  o
 FIG. 7. — The characteristic exponent is nonzero,
therefore there is no periodic orbit

FIG. 8. — There is symmetry, hence graphs are finite

FIG. 9. — There is a Liapunov function inside the
graph. Thus, there is no periodic orbit

Let us consider the different cases:

When 64= 0 and db >  o, p is a node and therefore there is no unbounded graph.
For b 4= o and ab < o, p is a saddle. Let us consider coordinates as in Lemma 2.2.
If there exists a periodic orbit of period T, we calculate its characteristic exponent obtai-
ning nT. Thus, as before, there is no periodic orbit if n 4= o. When n =  o, the vector
field is symmetric with respect to {x,jy) \-> {x, —jy), and there are no limit cycles.
 125

126 RODRIGOBAMO N

We now suppose b =  o. Take coordinates as in Lemma 2.3 with a>  o and
a> o. Let y ==y{x) be the parabola

y =y{x) =  (a/2) r8 -  rnx -  (i +  w^/aa

and let a^ )  be its normal vector v.^{x) == {ax — m, — i).
Easy calculations show that

< ^{x,y{x}), acuM) == (aaOT -  a) A;
2
.

Fix a >  o, a >  o and consider m as a parameter. Let OT<. be given by 2am. -  a == o
and let j  =jpo(.<-) be the parabola

y =jfoW  =  (a/2) ^  -  OTQ x -  (i +  ^)/2a.

For m =  wo the parabola j> =j^)  is invariant under the flow of X. Let
b (x) •= -m^x — (i +m'
io)|a.

By straightforward calculation we obtain:

(i) ^)<j'o(;c) for all x eR

(ii) The function f(x,y) == (j, -^(^))/(j, -  ^))2  has the origin as a maximum and
in the region ^  ={{x,y)jy> y^x)} this is the only critical point. That is /ha s
the following level curves in Q.:
 y =.%(*)

(iii)  x/( ^  -  (I 1 '  +  1^)(^)  =  -  -(^|,«'<  o f.,  e.ch (,,^) ^  ^

X ~T~ 0 ,

In this way, if 2am -  a =  o^ the origin is a repellor and there are no periodic
orbits. For m + m, (i.e. 2am -  a + o), the parabola ;, =j^)  is transversal to X.
Since X.= X^ =.X^+  (m-  my) R where X^ is the vector field in Lemma 2.3
and R(^) =  (x,y) is the radial vector field, we observe that the separatrices at p
move to different sides of y == y,(x~) when m changes. Thus there is no unbounded
graph when m + CTQ. The proof of Theorem B in case (I) is complete.

2.2 (II. i) ft -  a}2 -  4a(c -b ) =0  and c -  b + 0.

In this case there are two pairs of singularities at infinity. The one different
from {p =  (o, i, o), —p } is a pair of saddle-nodes for X restricted to infinity. This
is clear from the equation of X restricted to infinity:

«i =  a +  (b -  a) Mi +  (c-b)  u^.

126
 QUADRATIC VECTOR FIELDS 127

By rotating coordinates we can carry this pair of singularities to {p, —p} , leading
us to the next case:

a.a (11.2) b — c == 0 and ~b — a 4= 0.

Besides {j&, — p} there is another pair of singularities at infinity. When we res-
trict X to infinity, p and — p are non-hyperbolic while the other pair is hyperbolic.
As before, let Xg be the expression of X in coordinates (^g, y^). The linear part

ofXg at the origin is ( , (. So p is semi-hyperbolic if and only if b 4= o. If b + o

and X has an unbounded graph F, then F must contain two adjacent singularities at
infinity and the corresponding arc between them.
Also, for b =(= o, if X has an unbounded graph without singularities in the plane,
it must be of one of the two following types:

By Dulac's Proposition these graphs are finite.
Now, if b =t= o and X has an unbounded graph which contains singularities in
the plane and which has a return map, then by the contact property it is proved that
the separatrices of the graph are contained in invariant lines. By changing coordinates
we put these invariant lines in the axes and so the vector field takes the form

x =  x{m -{- ax -}- by)

y ==y(n +  ~bx +  by).

By the two invariant lines property this graph is finite.
Suppose now b == o.

Lemma 2.5. — If  X  has a periodic orbit then there exist coordinates in which

x == mx — y +  ax
2 a — A >  o

Proof.
 ^y == x +  my +  <3W
2 +  bxy a ^ o.

The same as in Lemma 2.3 and the remark following it. D

Lemma 2.6. — Let X  be given as in the lemma above. Then the topological type of the
singularity ^==(0,1,0 ) at infinity is one of the following'.

(i) ^ if  o <  b <  a;
 127

128 RODRIG O BAM6 N

(ii)

(in)
 if  b'^ 2fl; & <  o;

if  20 <  6 <  a <  o;

(iv) if ~b == o then the topological types are as in (i), (ii) or as in the following figures
^Jr^

Proof. — As for Lemma 2.4. D
From the possible topological types for p, we obtain that unbounded graphs may
have i or 3 singularities at infinity. For example the following graphs can exist:

Unbounded graphs with two singularities at infinity cannot exist because graphs
with a return map must enclose a convex region.
Suppose that X e /2 as in Lemma 2.5 has a graph with a return map and with
three singularities at infinity. Then, one of them is p (or — p) and the others are the
adjacent ones which are themselves symmetric. This pair of symmetric singularities
are in the direction y\x == a/{a — A). Since they are contained in a graph they must
be saddles and, by the contact property, the separatrix in the plane must be an invariant
straight line I of the form

y=y(x } =— fl —^4-N .
a — b

From the equation a2
< X(AVW), {a, b -  a) > =  a{a -  ~b) x
2 +  ( ^  -  a) -  ——— +  ~b -  a) x
a — b

— aN +  mN(b — a) == o,

where (a, ~b — a) is a vector normal to ^, it follows that a == m == o and N == — i (b.

128
 QUADRATIC VECTOR FIELDS 129

Thus, X can be expressed in the form

(
 x =  — y +  ^ 2

y =  x +  ~bxy.
X :

Since this vector field has the symmetry A, X == — X for A(x,j) == (— A",^),
we see that the origin is a center, and so there is no limit cycle.
We will now prove the assertions in the following scheme for the case b =  o.

fa== o : graph as in Fig. 10
3<wi — bm — a =  o a >  o : graph as in Fig. n
ym  — ~bm — a 4= o : there is no unbounded graph
o <  ~b <  a

b < 2fl, b < o : there is no unbounded graph with return map

2fl <  A <  a <  o
 _ f a == o : graph as in Fig. 12
ym  — bm — a =  o { _
[a >  o : graph as in Fig. 13

3<wi — T>m — a + o : there is no unbounded graph

a =  o : graph as in Fig. 14
ym  — a == o [ a >  o : there is no unbounded graph
b = o ym  — a 4= o : there is no unbounded graph.

FIG. 10. — There is a first integral inside the graph, therefore it is finite

FIG. n . — There is a Liapunov function inside the graph. Thus, there
are no limit cycles

FIG. 12. — Same as in Fig. 10
 m

17

130 RODRIG O BAM6 N

FIG. 13. — Same as in Fig. i t

FIG. 14. — The graph is symmetric, therefore it is finite

To prove the above assertions, consider the parabola

2fl — ~b i +  m
2
y -=y{x) =  ———— x
2
 — mx — 20.

and its normal vector a^(^) == {{20, — A) x — m, — i).
Easy calculations give

< X{x,jy{x)), ^{x)  > == {ym -  bm -  a ) x2.

Let m^ be given by the relation ^amy — 'bm^ — o == o and let y ==J^o(^) be the
parabola
 2fl — b i+rn^
y ==^oW == x6 — my x M

Fix a, 6 and a satisfying 0 <  ~b <  a and a ^  0.
Notice that m^ =  o for a =  o. Let us consider m as a parameter.
If m ==- niQ the parabola jy ^^oW  ls invariant and forms an unbounded graph.
Take r =  ~b\a and let b{x} =  — WQ x — (i +  ^)/&. Then:

(i) ^ )  <^oW fo
1
*
 a11  A<eR -
(ii) The function f{x^y) =  (j/ —J/o(A:))r/(^ ~" ^(•v))2 has the origin as a maximum
and in the region Q =  {(.y,jQ^ ^J^oW} tllls ls t^le on^y critical point. The level
curves ofyin 0, are
 y -y^}

130
 QUADRATIC VECTOR FIELDS 131

(iii)  X/(^ )  =  (HP  +JQ)  (^ )  =  -  4(2. -  ^  ^^^1^<  o

for all (^,jQ e n  with  A* =)= o.

Therefore, for a =  o the origin is a center (Fig. 10) and if a>  o (so that m^ 4= o)
there are no periodic orbits inside the graph (Fig. n).
For m =f= mQ (i.e. ym  — 1)m — a 4= o), we have as before that the relation:
X == X , =  X,, +  (m -  mo) R

is satisfied, and so there is no unbounded graph. This ends the proof in case o < i < a.
Now fix a, ~b and a satisfying 2a <  & < a < 0 and a ^ 0.
Recall that if a =  o then m^ == o. Let us again consider m as a parameter.

First let m =  m^. In this case the parabola y =^o(^) ls invariant and forms
an unbounded graph. Take r and b{x) as before. Then:

(i) y^x) <  b{x) for all x eR .
(ii) The function f(x^y) == OoW -""jO^W  ~Y)2 h^ ^e  origin as a maximum
and in the region Q =  {{x,y}fy ^YeW} fhis is the only critical point. The level
curves of^i n f2 are

(iii) X/(^j) =  4(za -  b) m, ^ffJ ^  ^  < o

for all (x,jy) eii with X  4= o.

Therefore, if a =  o there is a first integral and the origin is a center (Fig. 12)
and if a >  o (so that m^ ==)= o) there is a Liapunov function and there is no periodic
orbit inside the graph (Fig. 13).
To conclude the case above, we now let m + m^ (i.e. ym  —1)m — a + o). The
same arguments as in the previous case prove that there is no unbounded graph.
If ~b < 2a and ~b < 0, then from the topological type of p we conclude that no
unbounded graph is possible.
Fix a, ~b and a satisfying & =  0 < a and a > 0. Consider m as a parameter. If
m == rriQ the parabola y =J/o(^) ls invariant and it is easily shown that there is a saddle
on the parabola. Hence there is no unbounded graph. When m 4= m^ the parabola
y =  y^x) is transversal to X. Suppose that the topological type of p is the one in (i)
of Lemma 2.6. (This is the only possibility when A =  o for the existence of an
unbounded graph.) Since the separatrices at infinity bound hyperbolic sectors, the

131

132 RODRIG O BAMO N

transversal parabola y ==j/o(^) must leave the separatrices at different sides. The
following picture illustrates the situation:

Thus, there is no unbounded graph.
Finally fix a, ~b and a satisfying T) == 0 <  a and a == 0, so that m^ == o. When
m =  niQ == o the vector field verifies A^ X == — X for A(x,jy) == (— x,jy), the origin
is a center and there are no limit cycles. If m + m^ as before there is no unbounded
graph.
Thus, all assertions concerning the case b =  o are proved and case (II) is settled.

2.2 (III) ft -  a)2 -  4d(c -  b) >  0 and c -  b + 0.

We now come to the most difficult part of the proof of our main result.
For X e^ 2 given by (i) (see Chapter i) with c == o and satisfying the relation
above, there are three pairs of symmetric singularities at infinity.

Lemma 2.7. — If  X  e ^2 has three pairs of symmetric singularities at infinity and if  two
of them are hyperbolic^ then X  has a finite number of limit cycles.

Proof. — When a quadratic vector field X has three pairs of symmetric singularities
at infinity, all of them are hyperbolic for the restriction ofX to infinity (see Lemma i . i).
So the only possible unbounded graphs with a return map are of the following types:

(double arrows indicate hyperbolicity)

The first one is finite by IPyaSenko's Theorem. The middle one is not accumulated
by periodic orbits (Dulac's Proposition). The last one, with singularities in the plane,
must have separatrices contained in invariant lines, and as explained before, in this
case there are no limit cycles. D

132
 QUADRATIC VECTOR FIELDS 133

Lemma a. 8. — If  X  e •y
2
 has three pairs of symmetric singularities at infinity and two
of them are not hyperbolic^ then
9
.

(i) the two pairs of non-hyperbolic singularities are semi-hyperbolic \
(ii)  the third pair of symmetric singularities consists of hyperbolic nodes \
(iii)  there exist coordinates in which the hyperbolic pair of singularities is

{r =  i/2-v/2(- i, 1,0), -r }

and the semi-hyperbolic pairs of singularities are

{p == (o, i, o) $ -  p} and {q == (i, o, o), -  q}.

In these coordinates the vector field has an expression as in (i) with a =  o, c =  o, a == o,

c == o, b +  ^ =  o and b 4= o.

Proof. — We first observe that given any order in the pairs of singularities, there
are coordinates in R2 such that the first pair is {p, — p}, the second pair is {q, — q}
and the third one is {r, — r}. In fact, with a rotation of coordinates we carry the first
pair to {?, — p}; with a linear change of coordinates of the form A{x,y) =  {x, T^x +j0
(which fixes p) the second pair is taken to {q, — q}\ and finally with a change of coor-
dinates (x^y) h> (x, Xy), X 4= o, the third one is taken to {r, — r}.
If X is expressed as in (i), then in the coordinates above the following relations
are true c == o, a == o, c — b +  a — 6= 0 and b — c =t= o (this follows from (2)
and (3) in 1.2, by imposing the conditions P2(o, o) == Pi(o, o) == P^(— i, o) =  o).
Moreover we have the following table

singularities eigenvalues

p =  (o, 1,0 )

q == (1,0,0 )
r =  1/2 V2(—  i, 1,0 )
 —  <?, b —  c =(= o
— a, b — a =  c — i  =)= o
A—c,^— b =t= o.

If we suppose that p and q are not hyperbolic then a == c =  o and A =  — 6 4= o.
The lemma now follows directly. D
By the two lemmas above we can restrict ourselves to quadratic vector fields X
with expression
 (
 x =  a +  mx +  ny +  bxy
X : _ _ _ b +  o.
^=a+w^+ ^  — bxy

Moreover, by translating the coordinates we can suppose n =  m == o. Also, if
necessary, the change of coordinates {x,y) \-> (jy, x) makes b > o.
 132

134 RODRIG O BAMO N

Lemma 2.9. — Le t X  £/ 2 Ac given by

I
 x =  a +  mx +  ^

ji» == a -(-yy? — bxy

with b >  o. TA^z:

(i) ^  == (o, i,  o) awrf y == (o, — i,  o) are semi-hyperbolic singularities of X  fl^ infinity
(hyperbolic/or the restriction of X  to infinity) and r =  1/2 '\/2(— i,  i,  o) t.y a hyperbolic

node;
(ii) I/' X  Aflj an unbounded graph then it must contain p and q (or — p and — q) and the cor-

responding arc between them; moreover p and q (— p and — q) must be saddles or saddles-

nodes^
(iii) ifX  has an unbounded graph that contains singularities in the plane and has a return map,

then the separatrices are contained in invariant lines. In this case the vector field does not

have limit cycles.

Proof. — Parts (i) and (ii) are clear from Lemmas 2.7 and 2.8. If X satisfies
the hypothesis in (iii) then by the contact property it follows that there exist two invariant
lines that must contain the separatrices. We know that in this case there is no limit
cycle. D
In what follows we will consider X e^ 2 to be given by

I
 x === a +  mx +  bxy
X : .  _ _
y == a +  ^y — bxy

with b >  o, and we will study, in terms of the coefficients, when X can have unbounded
graphs without singularities in the plane. We will prove the following assertions:

(i) if aa == o there is no graph without singularities in the plane;
(ii) if either a < o, a >  o or mn >  o there is no unbounded graph.

Notice that when m >  o and w < o, we can change coordinates {x,jy) h-> (—y , — x)
so that we may suppose m<  o and n>  o.
Let a>o , w^o , a< o and n ^ o. Then:
(iii) if a+a===m+w=== o the only possible graph is as follows

(iv) if (a +  a) (m +  ii) == o but a+a+m+w+o , there is no unbounded graph;
(v) if a +  a 4= o and m +  ^ =t= o, then any graph without singularities in the plane
is finite.

134
 QUADRATIC VECTOR FIELDS i35

To prove (i) suppose a =  o. The line y =  o is invariant and contains the
center manifold of q. So, there is no graph, as required. The same happens if a == o.

To prove the other assertions let us consider X expressed in the coordinates at
infinity:
 u-^ == — bu^ — bu^ +  (n — m) u^ v^ +  az^ — ai^ v\

z^ == — bu^ v^ — mv{ — az^,
Xi:
 rig === bu^ +  bu^ +  (w •— n) Mg i^ +  ay| — a^  yj
^  === bu^ v^ — n^ — az|.
X,:

In both systems, the origin is a semi-hyperbolic singularity.

The center manifold for X^ has the form

"i = W  =  (a/i) ^  +  e(^) ,

and the flow along it is given by

»i =  -  mv[ -  (a +  a) ^  +  6(0^).

Similarly, the center manifold for Xg has the form

"2  =  ^2 )  =  -  M  ^  +  O(^)

and the flow is given by

^=-n^-(a+a)^+e(^) .

We can now prove (ii). Suppose a < o. Since b >  o, the center manifold
of X^ is locally contained in the half plane t^< o. That is:

center manifold center manifold

From the contact property it follows that all graphs with return map must enclose
a convex region. On the other hand, by Lemma 2.9 any such graph must contain
the adjacent singularities p and q (or — p and — q). But this is impossible because
of the location of the center manifold (see figure above). The same happens when a >  o.

135

136 RODRIG O BAM6 N

If mn >  o then p or q is a node, and thus there is no unbounded graph.

Now suppose a >  o, w < o, a< o and n ^ o. Notice that from the expressions
for the center manifolds of p and q we have the following situations:

(double arrows indicate hyperbolicity)

Besides proving (iii) to (v) we will see that these are the only cases where we can
have unbounded graphs without singularities in the plane. In fact, consider the
hyperbola y ==y(x) =  — v.j(bx) and its normal vector oLy(x) == (— a, bx2). Easy
calculations show that

<X(^(A:)), a^(A:)> == x(b^ +  a) x -  a(m +  n)).

To prove (iii), observe that, since a+a=w+w==o , the hyperbola is invariant,
the vector field verifies A, X == — X for A{x,jy) == {jy, x) and we obtain the graph
indicated above.
To prove (iv), i.e. when (a +  a) [m -\- n) =  Q but a+a+^+^+o ? notice
that the hyperbola y =  y{x) is transversal to X and no unbounded graph can exist
(the separatrices of p and q must be on different sides of y ==J^)).
Let us now prove (v). We suppose a +  a  =t= o and m +  n =t= o. We recall
that a >  o, w^o , a< o and n ^ o. The relations m == o and a +  a >  o or
n =  o and a +  a ^  o imply respectively that q or p are nodes (see the expres-
sions for the center manifolds), and thus in these cases there are no unbounded
graphs.

Now we arrive at the hardest part of the proof of Theorem B. There are three
cases to consider: mn +0 ; m =  o, n>o , a +  a < o; and m < o, n =  o, a +  a >  o.
As shown in the figures above in the three cases there can exist an unbounded graph
without singularities in the plane. We will prove now that if such a graph exists, then
it is finite. For that purpose we will analyse return maps (Poincard maps) associated
to these graphs and show that these maps have isolated fixed points.
To help clarify our arguments let us consider the following figure and dia-
grams:

136
 QUADRATIC VECTOR FIELDS i37

"i "2

2i- /
 • ^

Si 2,

Let us explain the notation. For o < s < 8, let

Si -{(5,  v)l\v\ <  e}, S, ={(8, z)f\z\ <  e},

Si ={(«, 8)/|«| <  s}, S^ =={(», S)/|^l <  e),
"l = {(8^l)/l"ll<e},  02={(8,^)/|^|<e} ,

be transversal sections as indicated.
Let pi denote the change of coordinates from the (y^ v^ -plane to the (u^, v^) -plane.
Since v^ =  ifx and v^ =  ify we have v^v^ == x^y =  u^ and so pi(»2» °2)
 == (I/a2»
 v^lv•^•
Moreover, p,^)  =  {(1/8, Oi)/| »i |  < e/8}.
 137

18

138 R 0  D R I G 0  B AM 6  N

Let pg : pi^)- > ^i; <p : Sg-> S^ and ^S^-^S g be the Poincard maps
naturally defined by X.
Let ^ , jj, ^3 ^  ^ e l°cal changes of coordinates given as follows. First take

f ^i == ^  -  Ai(^) == ^  -  (a/^) ^  -  6(^)
(1) ^i ^ [^==^ .

In these new coordinates, X^ has the form

f ui == -  ^i -  bu[ +  u^ v^ g^  z/i)

[ ^  ==== ~  ^  ^  — mu^ — (a +  a) ^  +  ^fiW.

Now, to avoid the term -— ^^i z^ in the component of the z^-axis we take

f u == Mi

obtaining
 ^i: [v  == ^/(i +  ^),

(
 u == — AM — ^M
2 +  ^^i(^, y)
•X>^ \ ^  ^
v == — mv
2
 — (a +  a) v3 +  ^Vi(^  ^) +  ^ 2  ^i(^  ^)-

Now take ( ^  == ^  -  Aa(^) == z/a +  (a/A) ^  -  e(»j)
(ii) ^2 •• _
^2==^2 -

In these coordinates Xg is expressed as

( U2 == ^ 2  +  AZ/2
2 +  ^2 ^2 ^(^ ^  ^2)
[  v^ == ^2  ^2 — ^1  — ( a +  a) ^3 +  v^f^).

Again, to avoid the term bu^ v^ in the component of the z/g-axis we take

(w==u^
s^: \
[ z == v^l{i +  u^)

obtaining w =  &w +  iw2 4- ^^2(^5-2')

z == — ^ 2  — (a +  a) z
3 +  Z^MW, z) +  wz^Ti^w, z).
Xa l

Finally, let u == u{v) be the Poincar^ map from S^ ==={(8, v) e^Jv>  0} to Si
defined by Xi and let z == z(w) be the Poincare map from ^  == {(w, 8) eSjw  > 0}
to Sg defined by Xg.
To prove the finiteness of the graphs we will compare the Poincare maps above
to other ones defined by auxiliary vector fields.
To do this consider the following vector fields

( u == — bu ( w == bw
X[: and X,:
y =  -  m' y2 [ i  =  _  „' ^

138
 QUADRATIC VECTOR FIELDS 139

with m' <  o and «' >  o. Let V: S^ - ^  and ?  : 2^- -> £g be the Poineare maps
associated to X[ and Xg respectively. We will use the following expressions

det(Xi, Xi) == uv^\b{m' -  m} +  F^a, ^)],

det(Xs,, X^) == wz^\b(n -  n') +  ¥^w, z)],

where Fi(o, o) == o and Fg^, o) == o, to compare the flows of X, and X,', i =  i or 2.
Notice for example that if |m | > \m'\ then det(Xi, X^') >  o for u>  o, and so
S(o) <  u(s) for small enough v >  o.

Let us first calculate u == S'(o), z == ?(w) and show that 9'(o) =  i. We have

u=ff(v) =Se-^m'^el"(m'^ =k^e'>/^'v1

(4) z =  ?(») =  _ _____  ^  °
i  +  (n'8/A)ln8-(n'8/6)ma> Ag -  (n'8/A) In w

Now, to calculate <p'(o) we use the following lemma.

Lemma a.io. — We hose p^o) =  8.

Proof. — We calculate p^o) by the following formula (see [A])

^o)| r
7
P^^'^^exppdivX^))^

I ^l^ 6? 0) I ^0^T^Jo

where ^t) is the orbit of X^ that goes from (1/8, o) to (8, o) in time T. The vector
field X^, when restricted to ^  =  o, has the equation u^ == — bu^ — bu[. Integrating
we obtain
 / e-u \
^-(TT^T--" 0)-

From y(T) == 8 we obtain T == — ijb In 8. Since div Xi(^, o) == — b — 3*^
we calculate ^  fT ^-bt
divX,(^))A=-6T- 3  —————^^
Jo Jo i +  6 — e
 w

=ln8-3ln( i +  8 -  e-^) T

o
=  In 8
4.

Finally, since |  X^8, o) | =  bS(i +  8) and |  X^i/8, o) |  =  b{i +  8)/8
2 we obtain
P2(°)
 :=  S? proving the lemma. D
 139

140 RODRIG O BAMO N

Remark. — If t2i and ^  are cross sections for X^ with ^  tangent to Q^ at (8, o)

and ^2 tangent to pi.(Qa) at (1/8, o) and they are parametrized by the projection to
the z^-axis, 4 ^  fi. ^

ni' PiW

f"^  /K /
then the corresponding Poincar^ map % : Cg -> QI satisfies pa^o) =  p^o) == 8.
From the above remark and from the fact that p^(8, v^ == (1/8, v^S) we finally
obtain <p'(o) === i.
We can now give the expression of our modified Poincard map.

Lemma 2.13. — Let u == ff(v) and z == ?(w) A^ as in (4). Z^  o =  ^5{z) =  X<2?

a%rf w =  ^(^) === (AM. Then

{ffofo^o^W  ^ku^^

where k is a positive real number.

Proof. — The formula is obtained by composing the maps. D
Let us now compare the return map of X with the modified return map and prove
that if there exists a graph then it is finite (we will prove slightly more: they are not
accumulated by periodic orbits). Suppose o < (n/|m|)< i or else »===o. Chose
m', n\ X and (JL such that: m' <  o, \m /\<m, W >  n^ \<  i, (n'/l^'l ^)
 <-
 l  an(!
o <  [LU < ^(u) for all u >  o small enough. Then for ff^ ?, ip and ^defined in (4) and
in Lemma 2.13 we have
V(v) <  u(v) since, for u >  o, det(5^, X^) >  o near (o, o),
?(w) < z(w) since, for w >  o, det(Xa, Xg) < o near (o, o),

^{u) < ^(u) for M> o small enough,

^!(z) < 9(2') for z > o small enough.

Thus
 (^opo^o^)^ ) ^W 17 ^ 1 ^  (^o<po^o4/)(^) ,

and since (n'/l w' |  X) < i we conclude that u <  {u o <p o z o ^) (u) for all M small enough.
With this it is proved that if there is an unbounded graph then it is a repellor (i.e. it
is the a-limit set of some orbit).
In the same way if (n/| m |) >  i or m === o we prove that if there is an unbounded
graph it is an attractor (i.e. it is the co-limit set of some orbit). This ends the proof
of Case (III).

140
 QUADRATIC VECTOR FIELDS 141

a.a (IV) c-b='b-a==a==0 .

Let X e ^2 be given by (i) (see Section i) with c == c — i  == A — a == a == o.
In this case, X is transversal to infinity with the exception of two symmetric
points.
Since the relations above are invariant under any affine change of coordinates,
the periodic orbit property allows us to restrict ourselves to vector fields of the
form
 (
 x =  mx —y +  ax2 +  bxy

y == x +  my +  axy +  by
2.

For these vector fields it is not hard to prove that with a rotation of coordinates
we can make b =  o. We then obtain

(
 x =  mx — y +  ^x2

y == x +  my +  axy.

With this last expression we see that the origin is the only singularity and therefore,
there is a finite number of limit cycles.
The proof of Theorem B is now complete.

REFERENCES

[A] A. ANDRONOV et al., Qualitative Theory of Second Order Dynamical Systems, John Wiley &  Sons, New York,

1973-
[C] W. COPPEL, A survey of Quadratic Systems, Journal a/Differential Equations, 2 (1966), 293-304.
[Ca] J. CARR, Applications of Center Manifold  Theory, Applied Math. Sciences, 35, Springer-Verlag, 1981.
[Ch-S] C. CHICONE and S. SCHAFER, Separatrix and Limit Cycles of Quadratic Systems and Dulac's Theorem,

Transactions Amer. Math. Soc., 278 (1983), 585-612.
[D] M. H. DULAC, Sur les cycles limites. Bull. Soc. Math. France, 51 (1923), 45-188.
[Du] F. DUMORTIER, Singularities of Vector Fields, Journal of Differential Equations, 23, i  (1977), 53-io6.
[H-P-S] M. HIRSGH, C. PUGH and M. SHUB, Invariant Manifolds, Springer Lecture Notes in Math., 583 (1977).
[I]  Yu. S. IFyasenko, Limit cycles of polynomial vector fields with non degenerate singular points in  the
real plane (in  Russian), Functional Analysis and its applications, 18 (3) (1984), 32-34 (in  translation :  18 (3)

(i985)> 199-209).
[P-LJ I.  G. PETROVSKII and E. U. LANDIS, On the number of limit cycles of the equation dy\dx =  P(^,.y)/Q,(^,jO
where P and Q,are polynomials of the second degree, Amer. Math. Soc. Transl. (2), 16 (1958), 177-221.
[P-Lg] I.  G. PETROVSKII and E. U. LANDIS, On the number of limit cycles of the equation dy\dx == P(^,J»)/Q.(^,^)
where P and Q, are polynomials, Amer. Math. Soc. Transl. (2), 14 (1960), 181-200.
[P-L3] I.  G. PETROVSKII and E. U. LANDIS, Corrections to the articles :  €t On the number of limit cycles of the
equation dy\dx =  'P(x,y)IQ,(x,y) where P and Q, are polynomials ", Math. Sb.N.S., 48 (90) (1959).

253-255-
 241

i42 RODRIGOBAM6 N

[P-M] J. PALIS and W. de MELO, Geometric Theory of Dynamical Systems; An Introduction, New York, Springer-
Vcrlag, 1982.
[S] J. SOTOMAYOR, Curvas definidas por equacoes diferenciais no piano, 13° Coloquio Bras. de Mat., IMPA,
1981.
[Shi] SHI SONGLING, A concrete example of the existence of four limit cycles for plane quadratic systems, Sci.y
Sinica, Ser. A, 23 (1980), 153-158.
[Shg] SHI SONGLING, A method for constructing cycles without contact around a weak focus. Journal a/Differential
Equations, 41 (1981), 301-312.

Universidad de Chile
Departamento de Matematicas
Casilla 653
Santiago, Chile.
 Manuscrit refu Ie 16 septembre 1985.

U2
