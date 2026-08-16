<!-- source: https://www.renyi.hu/~barany/cikkek/72.pdf | converted from PDF -->

Discrete Comput Geom 19:335–342 (1998) Discrete & Computational
Geometry
© 1998 Springer-Verlag New York Inc.

A Positive Fraction Erd˝os–Szekeres Theorem¤

I. B´ar´any
1 and P. Valtr
2

1Mathematical Institute of the Hungarian Academy of Sciences,
P.O.B. 127, H-1364 Budapest, Hungary
barany@math-inst.hu

2Department of Applied Mathematics, Charles University,
Malostransk´en´am. 25, 118 00 Praha 1, Czech Republic
valtr@kam.ms.mff.cuni.cz

Communicated by J´anos Pach

Abstract. We prove a fractional version of the Erd˝os–Szekeres theorem: for any k there
is a constant ck > 0 such that any sufﬁciently large ﬁnite set X ½ R2 contains k subsets
Y1;:::; Yk, each of size ¸ ckjX j, such that every set fy1;:::; ykg with yi 2 Yi is in convex
position. The main tool is a lemma stating that any ﬁnite set X ½ R
d contains “large” subsets
Y1;:::; Yk such that all sets fy1;:::; ykg with yi 2 Yi have the same geometric (order) type.
We also prove several related results (e.g., the positive fraction Radon theorem, the positive
fraction Tverberg theorem).

1. Introduction

The Erd˝os–Szekeres theorem [ES1] says that among sufﬁciently many points in general
position in the plane one can ﬁnd k that are in convex position. It is a classical result in
combinatorial geometry with a number of generalizations and extensions (see, e.g., [S2]
and [EP]). This paper increases this number by one: we prove a fractional version of the
Erd˝os–Szekeres theorem.
A ﬁnite set in R
d is in general position if it contains no d C 1 points lying in a
hyperplane. A ﬁnite set Y ½ Rd is in convex position if every y 2 Y is a vertex of
conv Y .Given k sets Y1;:::; Yk, a set fy1;:::; ykg is called a transversal of the Yi ,if

¤ The research by I. B´ar´any was partially supported by Hungarian Science Foundation Grant T 016391. Part
of this research was done while this author was visiting the Mathematics Department at University College,
London, whom he thanks for their hospitality. The research by P. Valtr was supported by Czech Republic Grant
GA ˇCR 0194 and by Charles University Grants GAUK 193/1996 and 194/1996.

336 I. B´ar´any and P. Valtr

y1 2 Y1;:::; yk 2 Yk. We write [n] Df1;:::; ng. The fractional version of the Erd˝os–
Szekeres theorem follows:

Theorem 1. For every integer k ¸ 4 there is a constant ck > 0 with the following
property. Every sufﬁciently large ﬁnite set X ½ R
2 in general position contains k subsets
Y1;:::; Yk with jYi j¸ ckjX j .i 2 [k]/ such that every transversal of the Yi is in convex
position.

The proof is based on what we like to call the same type lemma. With further ap-
plications in mind we present it in colored version and in arbitrary dimension. Two
m-tuples .x1;:::; xm/ and .y1;:::; ym/.xi ; yi 2 Rd / are said to have the same .order/
type if the orientations of the simplices xi1 ¢¢¢ xidC1 and yi1 ¢¢¢ yidC1 are the same for every
1 · i1 < ¢¢¢ < idC1 · m. This is the same as saying that the signs of det
£¡xi1
1 ¢ ¢¢¢ ¡xidC1
1 ¢¤

and det
£¡yi1
1 ¢ ¢¢¢ ¡yidC1
1 ¢¤ are equal. Properties of order types have been intensively studied,
mainly in relation to computational geometry; a survey on these investigations can be
found in [GP1] or in [GP2].

Theorem 2 (Same Type Lemma). For every two natural numbers d and m there is a
constant c.d; m/> 0 with the following property. Given ﬁnite sets X 1;:::; X m ½ Rd

such that X 1 [ X 2 [ ¢¢¢ [ X m is in general position, there are subsets Yi ½ Xi with
jYi j¸ c.d; m/jXi j such that all transversals of the Yi have the same type.

We mention without elaborating that the sets X; X 1;:::; X m in the above theorems
could be replaced by probability measures. Then the subsets Yi would be of measure at
least ck or c.d; m/, respectively.
Recently, Theorem 1 was proved for k D 4 by Nielsen (personal communication).
Solymosi (unpublished) found the following weaker version of Theorem 1: given n
points in general position in the plane, one can always choose a sequence of length ckn
from among them such that any k consecutive members of this sequence are in convex
position.
The proofs of the above two theorems, followed by a discussion on direct conse-
quences, are given in the next two sections. Related results (e.g., the positive fraction
Radon theorem, the positive fraction Tverberg theorem) are described in Section 4.

2. Proof of Theorem 2

It is enough to work with the case m D d C1, the theorem would then follow by applying
the case m D d C 1toevery .d C 1/-tuple Xi1 ;:::; XidC1 .1 · i1 < ¢¢¢ < idC1 · m/.
So assume m D d C 1.
Partition [d C 1] into all possible unordered pairs of (nonempty) subsets:
.I1; J1/;:::;.I2d ¡1; J2d ¡1/. For any i 2 [d C 1], we will ﬁnd a chain of subsets Xi D
X 0
i ¾ X 1
i ¾ ¢¢¢ ¾ X 2
d ¡1
i D Yi such that, for all ® 2 [2
d ¡ 1],

jX ®
i j¸ 1
d C 1 jX ®¡1
i j: (1)

A Positive Fraction Erd˝os–Szekeres Theorem 337

We proceed in 2
d ¡ 1 steps. In step ® we ﬁnd the subsets X ®
i in the following way. Let
zi be the center of X ®¡1
i in the sense of [DGK], i.e., every open half-space containing
zi contains at least [1=.d C 1/]jX ®¡1
i j points of X ®¡1
i . We may assume that the set
fz1;:::; zdC1g is in general position, since otherwise we may achieve it by a small
perturbation of the sets X ®¡1
i . Consider the hyperplane H® parallel with afffzi : i 2 I®g
and with afffzi : i 2 J®g and positioned half-way between them. Write H I
® and H J
® for the
two half-spaces bounded by H® so that H I
® ¾ afffzi : i 2 I®g and H J
® ¾ afffzi : i 2 J®g.
Take H I
® closed and H J
® open, say. Deﬁne

X ®
i D ½H I
® \ X ®¡1
i for i 2 I®;
H J
® \ X ®¡1
i for i 2 J®:

Inequality (1) follows now from the property of the centers zi . So at the end we have
Yi D X 2
d ¡1
i ½ Xi with
 jYi j¸ .d C 1/
¡.2
d ¡1/jXi j: (2)

We claim now that every simplex with vertices y1 2 Y1;:::; ydC1 2 YdC1 has the
same orientation. Suppose the contrary and let y0
1 y0
2 ¢¢¢ y0
dC1 be another simplex with a
different orientation. Then, for a suitable t 2 .0; 1/, the points ui D tyi C .1 ¡ t/y0
i
(i 2 [d C 1]) all lie on a hyperplane H . By Radon’s theorem [R], applied in H to the
points u1;:::; udC1, there is a partition .I; J / of [d C 1] with

convfui : i 2 I g\ convfui : i 2 J g6D;: (3)

Now .I; J / D .I®; J®/ for some ®. We have convfui : i 2 I g½ conv S
fYi : i 2 I g½
conv S
fX ®
i : i 2 I g½ H I
® and similarly convfu j : j 2 J g½ H J
® , a contradiction with
(3).
The argument in the last paragraph was used for a different purpose by Goodman
et al. [GPW].

Remark 1. Denote by c.d; m/ the inﬁmum of the constants for which Theorem 2 is
true. The above proof gives

c.d; m/ ¸ .d C 1/
¡.2
d ¡1/.m¡1
d /: (4)

A slight improvement on (1) and consequently on (2) and (4) comes from using the
ham–sandwich theorem instead of the center point theorem.

Remark 2. In the plane, (4) can be improved to

c.2; m/ ¸ 1
m 2
¡.
m¡1
2 /: (5)

To see this observe ﬁrst that the sets X 1;:::; X m may be reordered so that there are
vertical (say) lines l0; l1;:::; lm (in this order from left to right) such that Xi has at least
.1=m/jXi j elements between li¡1 and li . Write X 0
i for the set of points of Xi between

338 I. B´ar´any and P. Valtr

li¡1 and li . Now, for any triple 1 · p < q < r · m, only X 0
q has to be separated from
X 0
p and X 0
r (lp separates X 0
p from the other two, and lq separates X 0
r from the other two).
This can be reached by a line l that halves X 0
p and X 0
r simultaneously. l cuts X 0
q into two
parts. Keep the larger part and half of X 0
p and of X 0
r on the other side of l.

Remark 3. There is a cone version to the same type lemma. This states, under the
same conditions, the existence of Yi ½ Xi , jYi j¸ c0.d; m/jXi j such that

det.yi1 ;:::; yid /

has the same sign for all choices yi1 2 Yi1 ;:::; yid 2 Yid . The proof is essentially the
same, starting with the case m D d. However, as a ﬁrst step, halve Y1;:::; Yd by a
hyperplane and keep those halves that are on the other side to the origin. Then use two
partitions of [d] and separating hyperplanes that pass through the origin.

Remark 4. It is clear from the proof that the statement of Theorem 2 is also valid for
transversals of the conv Yi . The same is true in the case of Theorem 1.

Remark 5. With some effort, Theorem 2 can also be proved when X 1 [ X 2 [ ¢¢¢ [ X m
is not in general position.

Remark 6. It follows from Theorem 2 that for any k and any ﬁnite point set X in
general position in Rd there exist k positive fraction subsets X 1;:::; X k so that the
convex hull of every choice is combinatorially the cyclic polytope on k vertices.

3. Proof of Theorem 1

Let m D m.k/ be the Erd˝os–Szekeres number for k. Choose vertical lines l0; l1;:::; lm
(listed from left to right) so that at least b.1=m/jX jc points of X lie between li¡1 and li
.i 2 [m]/; denote by Xi the set of these points. Apply the same type lemma to obtain
subsets Yi µ Xi such that all transversals of the Yi are of the same type and, of course,
jYi j¸ c.2; m/jXi j (i 2 [m]).
For every i 2 [m], ﬁx yi 2 Yi . The Erd˝os–Szekeres theorem implies that some
yi1 ;:::; yik are in convex position. Then, by the same type lemma, every transversal of
the Yi j is in convex position.

Remark. Again, write ck for the inﬁmum of the constants for which Theorem 1 is true.
The above proof gives
 ck ¸ 1
m.k/ 2
¡.
m.k/¡1
2 /

which is doubly exponential in k: it is known that 2
k C 1 · m.k/ · ¡
2k¡4
k¡2 ¢ C 1 (see [ES1]

A Positive Fraction Erd˝os–Szekeres Theorem 339

Fig. 1. The regions A01, A02, C01, C02.

and [ES2]). For k D 4 and 5 we can do better. We give the proof of c4 ¸ 1
22 and invite
the reader to prove or improve c5 ¸ 1
352 .

Proof of c4 ¸ 1
22 . Assume jX j is divisible by 22 and set jX jD 22n. Choose vertical
lines l0; l1; l2; l3 (listed from left to right) so that writing A, B, C for the set of points
between l0 and l1, l1 and l2, and l2 and l3, respectively, we have jAjD 10n, jBjD 2n,
jCjD 10n. The halving line, l4,of A and C bisects B. Assume at least half of B is above
l4, and denote this subset of B by B0. Let A0, C0 be the half of A, C below l4, respectively.
Take the line l5 that bisects A0 into two subsets A01, A02, jA01jD n, jA02jD 4n, and
C0 into two subsets C01, C02, jC01jD 3n, jC02jD 2n, as in Fig. 1. Now push the line l3
toward l2 and stop when it passed either n points of C01 or n points of C02 (whichever
comes ﬁrst). Further, halve the set A02 by a vertical line. Denote the obtained regions as
in Fig. 2. We know that jA01jD n, jA1jDjA2jD 2n, jB0j¸ n, jC1j¸ 2n, jC3j¸ n,
and maxfjC2j; jC4jg D n. We now distinguish two possible cases.

Case 1: jC2jD n. The sets A01, B0, C2, and C3 are “convexly independent” sets of
size ¸ n in this case.

Case 2: jC4jD n. Take the halving line of A1 and C1. It bisects A1, A2, and C1 into
upper and lower parts to be denoted by Au
1, Au
2, C u
1 , and Al
1, Al
2, C l
1. Now either jAu
2j¸ n,
in which case Al
1, Au
2, C l
1, C4 are “convexly independent” of size ¸ n,or jAl
2j > n,in
which case Au
1, Al
2, C u
1 , B0 are “convexly independent” of size ¸ n.

Fig. 2. The regions Ai ; Ci .

340 I. B´ar´any and P. Valtr

4. Further Consequences

4.1. Positive Fraction Radon Theorem

A simple consequence of the same type lemma is a positive fraction Radon theorem
saying that the sets Y1;:::; Ym obtained have the following property as well. Any .d C2/-
set D ½ [m] has a two-partition D D I [ J such that the Radon partition of every set
fyi 2 Yi : i 2 Dg is fyi : i 2 I g[fyi : i 2 J g.
The proof is straightforward. The Radon partition is induced by the signs of the
coefﬁcients in the afﬁne dependence
X

i2D ®i yi D 0; X

i2D ®i D 0:

The sign of ®i is just the sign of det[¡yj
1 ¢
: j 2 Dnfig] which depends only on Dnfig (and
not on the choice).

4.2. Positive Fraction Tverberg Theorem

With a little effort, one can get a positive fraction Tverberg theorem as well. For simplicity,
we state it when m D .d C 1/.r ¡ 1/ C 1. A partition Z D Z1 [ ¢¢¢ [ Zr of a ﬁnite set
Z ½ Rd is called a Tverberg partition if

r\

iD1 conv Zi 6D ;:

Theorem 3. Assume d; r ¸ 2, and let m D .d C 1/.r ¡ 1/ C 1 and X1;:::; X m ½ R
d .
Then there are positive fraction subsets Yi ½ Xi .i 2 [m]/ and r -partitions I ®
1 [ ¢¢¢ [ I ®
r ,
® 2 [a], of [m] .with a ¸ 1/ such that all Tverberg r -partitions of any set of the form
fyi : i 2 [m]g where yi 2 Yi are Sr
jD1fyi : i 2 I ®
j g, ® 2 [a].

Proof. Let v1;:::;vr 2 R
r ¡1 be r vectors such that their only linear dependence is

v1 C ¢¢¢ C vr D 0: (6)

For x 2 Rd , write x D ¡x
1¢ 2 R
dC1. The tensor product vj   x is an r ¡ 1by .d C 1/
matrix and is regarded as an element of Rm¡1. Further, let x1; x2;:::; xm 2 Rd and
g:[m] ! [r ].
We make use of the following observation [BO] and [S1]: Tverberg partitions of
fx1;:::; xmg are in one-to-one correspondence with linear dependences of the form

mX

iD1 ®i vg.i/   xi D 0;®i ¸ 0: (7)

To see this assume (7) holds. Then the sets Ij Dfi: g.i/ D jg partition [m]. We claim
that Tj2[r ] convfxi : i 2 Ij g6D;, i.e., the sets fxi : i 2 Ij g form a Tverberg partition.

A Positive Fraction Erd˝os–Szekeres Theorem 341

Equation (7) can be written as
 0 D
 rX

jD1 vj   X

i2Ij ®i xi :

Multiplying from the left by vectors u> 2 R
r ¡1 orthogonal to r ¡ 2 of the vectors
v1;:::;vr shows, using (6), the existence of x 2 R
dC1 with

x D X

i2I1 ®i xi D ¢¢¢ D X

i2Ir ®i xi :

Checking the last components gives xdC1 D P
i2I1 ®i D ¢¢¢ D P
i2Ir ®i so that, indeed,

r\

jD1 convfxi : i 2 Ij g6D;:

The argument can be reversed showing that a Tverberg partition gives rise to a linear
dependency of the form (7).
Returning to the proof of Theorem 3, consider the rm sets fvj   xi : xi 2 Xi g,to
be denoted by vj   Xi . Choose k 2 [m] and a map g:[m]nfkg! [r ] and apply the
proof of the same type lemma (cone version) to the sets vg.i/   Xi .i 2 [m]nfkg/ with the
following extra requirement. When vg.i/   X ®¡1
i is to be replaced by the subset vg.i/   X ®
i ,
replace vj   X ®¡1
i by vj   X ®
i for every j 2 [r ]. Do this for every k 2 [m] and every
g:[m]nfkg! [r ]. The outcome is positive fraction subsets Yi ½ Xi .i 2 [m]/ such that
for every k 2 [m] and every g:[m]nfkg! [r ] the sign of

det[vg.i/   yi : i 2 [m]nfkg]

(where yi 2 Yi ) depends only on k and g (and not on the choice of yi ). To ﬁnish the
proof observe that solutions to (7) are determined by the above determinants.

4.3. Tverberg-Type Result on Multicolored Simplices

Pach [P] used a modiﬁcation of the same type lemma to prove the following. Given sets
X 1;:::; X dC1 ½ Rd there are subsets Yi µ Xi with jYi j¸ C.d/jXi j .i 2 [d C 1]/ and
a point p 2 R
d such that for every choice yi 2 Yi .i 2 [d C 1]/ the point p lies in
convfy1;:::; ydC1g. This was proved in the plane by [BFL] with C.2/ D 1
12 but was not
known for d > 2.
Here is a sketch of a modiﬁed version of Pach’s neat argument. (It differs from
Pach’s proof by applying a different point selection theorem and by applying the same
type lemma instead of a weaker separation argument.) Consider the complete .d C 1/-
partite hypergraph H D .V; E/ with vertex set V D X1 [ ¢¢¢ [ X dC1. The “point
selection” theorem of [ABFK] implies the existence of a point z 2 Rd and an edge
set E 0 ½ E, jE 0j¸ pjEj, where p D p.d/> 0, such that z 2 conv e for each
e 2 E 0. By a weak form of the hypergraph version of Szemer´edi’s regularity lemma (see
[KS] or [P] for this particular case), for every ´> 0 there are subsets Zi ½ Xi with
jZi j¸ b. p;´/jXi j for all i 2 [d C 1] (where b. p;´/ > 0 is a constant) such that for

342 I. B´ar´any and P. Valtr

every choice of subsets Yi ½ Zi with jYi j¸ ´jZi j, there is an edge fy1;:::; ydC1g2 E 0

with yi 2 Yi . Choose ´ D c.d; d C 2/ from Theorem 2, and apply Theorem 2 to the sets
Z0; Z1;:::; ZdC1 where Z0 consists of “many” copies of the point z.Weget Yi ½ Zi ,
jYi j¸ ´jZi j (i D 0; 1;:::; d C 1), such that all transversals of the Yi have the same type.
There is an edge fy¤
1 ;:::; y¤
dC1g2 E 0 with y¤
i 2 Yi .Wehave z 2 convfy¤
1 ;:::; y¤
dC1g,
and consequently z 2 convfy1;:::; ydC1g for each choice yi 2 Yi .

Acknowledgment

We thank J´anos Pach for pointing out several references and explaining his proof
(sketched in Section 4.3) to us. We also thank the referees for helpful comments.

References

[ABFK] N. Alon, I. B´ar´any, Z. F¨uredi, and D. Kleitman. Point selections and weak "-nets for convex hulls.
Combin. Probab. Comput. 1 (1992), 189–200.
[BFL] I. B´ar´any, Z. F¨uredi, and L. Lov´asz. On the number of halving planes. Combinatorica 10 (1990),
175–183.
[BO] I. B´ar´any and S. Onn. Colourful linear algebra. 7th IPCO, 1996, Vancouver (to appear in Math. Oper.
Res.).
[DGK] L. Danzer, B. Gr¨unbaum, and V. Klee. Helly’s theorem and its relatives. Proc. Symp. Pure Math.,
Vol. 7. AMS, Providence, RI, 1963, pp. 101–138.
[EP] P. Erd˝os and G. Purdy. Extremal problems in combinatorial geometry. In: Handbook of Combina-
torics, Chapter 17 (R. Graham, M. Gr¨otschel, and L. Lov´asz, eds.). Elsevier, New York, pp. 809–874,
1995.
[ES1] P. Erd˝os and G. Szekeres. A combinatorial problem in geometry. Compositio Math. 2 (1935), 463–
470.
[ES2] P. Erd˝os and G. Szekeres. On some extremum problems in elementary geometry. Ann. Univ. Sci.
Budapest 3/4 (1960/61), 53–62.
[GP1] J. E. Goodman and R. Pollack. The complexity of point conﬁgurations. Discrete Appl. Math. 31
(1991), 167–180.
[GP2] J. E. Goodman and R. Pollack. Allowable sequences and order types in discrete and computational
geometry. In: New Trends in Discrete and Computational Geometry (J. Pach, ed.). Springer-Verlag,
New York, 1993.
[GPW] J. E. Goodman, R. Pollack, and R. Wenger. Geometric transversal theory. In: New Trends in Discrete
and Computational Geometry (J. Pach, ed.). Springer-Verlag, New York, 1991.
[KS] J. Koml´os and M. Simonovits. Szemer´edi’s regularity lemma and its applications in graph theory. In:
Paul Erd˝os Is Eighty, Vol. 2 (Keozshely, 1993), pp. 295–352. Bolyai Society Mathematical Studies,
Vol. 2, Budapest, 1996.
[P] J. Pach. A Tverberg-type result on multicolored simplices. To appear in Comput. Geom. Theory Appl.
[R] J. Radon. Mengen konvexer K¨orper, die einen gemeinsamen Punkt enthalten. Math. Ann. 83 (1921),
113–115.
[S1] K. S. Sarkaria. Tverberg’s theorem via number ﬁelds. Israel J. Math. 79 (1992), 317–320.
[S2] P. Schmitt. Problems in discrete and combinatorial geometry. In: Handbook of Convex Geometry,
Chapter 2.2 (P. M. Gruber and J. M. Wills, eds.). Elsevier, New York, pp. 449–483, 1993.
[T] H. Tverberg. A generalization of Radon’s theorem. J. London Math. Soc. 41 (1966), 123–128.

Received March 8, 1996, and in revised form June 24, 1996.

Note added in proof: J. Solymosi found a new and nice proof of Theorem 1 that gives
a better constant for ck as well. His constant is roughly 2
¡16k2 .
