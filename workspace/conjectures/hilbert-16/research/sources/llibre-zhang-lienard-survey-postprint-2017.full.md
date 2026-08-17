<!-- source: https://ddd.uab.cat/pub/artpub/2017/221320/expmat_a2017v35n3p286preprint.pdf | converted from PDF -->

LIMIT CYCLES OF THE CLASSICAL LI´ENARD
DIFFERENTIAL SYSTEMS: A SURVEY ON THE LINS
NETO, DE MELO AND PUGH’S CONJECTURE

JAUME LLIBRE
1 AND XIANG ZHANG
2

Abstract. In 1977 Lins Neto, de Melo and Pugh [Lectures Notes in
Math. 597, 335–357] conjectured that the classical Li´enard system

˙x = y − F (x), ˙y = −x,

with F (x) a real polynomial of degree n, has at most [(n − 1)/2] limit
cycles, where [·] denotes the integer part function. In this paper we
summarize what is known and what is still open on this conjecture. For
the known results on this conjecture we present a complete proof.

1. Introduction and statement of the main results

The classical Li´enard system

(1) ˙x = y − F (x), ˙y = −x,

with F (x) a real polynomial of degree n, has been extensively studied (see
for instance [2, 11, 20, 25, 31, 32, 39, 42, 43], and references therein). In
1977 Lins Neto, de Melo and Pugh [25] proved that there exist systems (1)
of degree n having [(n − 1)/2] limit cycles, and stated the following:

Conjecture System (1) has at most [(n − 1)/2] limit cycles, where n is the
degree of the real polynomial F (x).

Here [x] denotes the integer part function of x.

In this paper we summarize what is known and what is still open on this
conjecture. Moreover for the known results on this conjecture we present a
complete proof.

The conjecture was based in the following result of Lins Neto, de Melo
and Pugh [25]:

Theorem 1. If the real polynomial F (x) has degree n, then there are Li´enard
diﬀerential systems (1) having at least [(n − 1)/2] limit cycles.

2010 Mathematics Subject Classiﬁcation. Primary 34C05, 34C23; secondary 34C25,
34C29.
Key words and phrases. Li´enard system, limit cycle, conjecture of Lins Neto, de Melo
and Pugh. 1

This is a preprint of: “Limit cycles of the classical Li´enard diﬀerential systems: A survey on the
Lins Neto, de Melo and Pugh’s conjecture”, Jaume Llibre, Xiang Zhang, Exposition. Math., vol.
35, 386–299, 2017.
DOI: [10.1016/j.exmath.2016.12.001]

2 JAUME LLIBRE AND XIANG ZHANG

Here we shall present a shorter and diﬀerent proof of Theorem 1 from
the one given in [25], this new proof also provides information about the
stability of the limit cycles.

The known results on the conjecture are the following:

Theorem 2. For the Li´enard diﬀerential system (1) the following state-
ments hold.

(a) For n = 1, 2, system (1) has no limit cycles.
(b) For n = 3, 4, system (1) has at most one limit cycle, and there exist
systems (1) having one limit cycle.
(c) For any n ≥ 6, there exist systems (1) having at least n − 2 limit
cycles.

Theorem 2 says that for n = 1, 2, 3, 4 the conjecture holds, while for n ≥ 6
it does not hold. At this moment only remains to know if the conjecture
holds or not for n = 5.

The result that the conjecture holds for n = 1, 2, 3 already was proved by
Lins Neto, de Melo and Pugh [25]. Here, for n = 1, 2 we shall present the
orignal proofs, but for n = 3 we shall present two new diﬀerent and shorter
proofs. In 2012, thirty ﬁve years after the statement of the conjecture, it
was proved by Li and Llibre [23] that the conjecture also holds for n = 4,
but that proof is long and considers several cases, and the whole paper has
20 pages. We will not repeat this proof.

Statement (c) of Theorem 2 shows that the conjecture is not correct for
n ≥ 6. Through the conjecture remains unchanged for more than thirty
years in 2007 Dumortier, Panazzolo and Roussarie [11] shown that the con-
jecture is not true for n ≥ 7 providing one additional limit cycle to the
ones predicted by the conjecture. In 2011 De Maesschalck and Dumortier
[8] proved that the conjecture is not true for n ≥ 6 providing two additional
limit cycles to the ones predicted by the conjecture. Finally, in 2015 De
Maesschalck and Huzak [9] proved that the number of limit cycles is at least
n − 2 if n ≥ 6, i.e. showing that the Li´enard diﬀerential systems of degree
n ≥ 6 have essentially at least n/2 more limit cycles than the number con-
jectured by Lins Neto, de Melo and Pugh. Summarizing the above results
we state the following question:

Open problem. What is the maximum number of limit cycles for the
Li´enard diﬀerential systems (1) when n ≥ 5?

This paper is organized as follows. In section 2 we prove Theorem 1.
In section 3 statement (a) of Theorem 2 is proved. In section 4 we prove
statement (b) for n = 3 of Theorem 2. Finally, the proof of statement (c) is
presented in section 5.

LI´ENARD DIFFERENTIAL SYSTEMS 3

2. Proof of Theorem 1

The proof presented here of Theorem 1, is shorter, diﬀerent and provides
information about the kind of stability of the limit cycles, it comes from the
paper [26], see also [27].

For doing the proof of Theorem 1 we need to recall some basic results
from the averaging theory of ﬁrst order, for a proof of these results see, for
instance, Theorems 11.5 and 11.6 of the book of Verhulst [37].

The averaging theory says: If the function

f (r) = 1
2π
 ∫ 2π

0 F1(θ, r) dθ

has k simple real roots, 0 < r1 < · · · < rk, then the diﬀerential equation in
polar coordinates (r, θ)

(2) dr
dθ = εF1(θ, r) + ε
2F2(θ, r, ε)

has k limit cycles tending to the circles r = ri for i = 1, . . . , k when ε →
0, where F1 and F2 are periodic of period 2π in θ and C 2 smoothness.
Moreover, the limit cycle tending to the circle r = ri is stable if f ′(ri) < 0,
and unstable if f ′(ri) > 0.

Proof of Theorem 1. We shall prove that [(n − 1)/2] is a lower bound for
the maximum number of limit cycles that Li´enard polynomial diﬀerential
systems (1) of degree n can have. More precisely, we shall show that there
are diﬀerential systems of the form

(3) ˙x = y + εF (x), ˙y = −x,

with F (x) = a0 + a1x + . . . + anxn and an ̸= 0 having [(n − 1)/2] limit cycles.

As usual polar coordinates (r, θ) are deﬁned as x = r cos θ and y = r sin θ.
In polar coordinates the diﬀerential system (3) is

(4) ˙r = ε cos θ F (r cos θ), ˙θ = −1 − ε 1
r sin θ F (r cos θ).

Choosing the variable θ as the new independent variable, system (4) becomes

(5) dr
dθ = −ε cos θ F (r cos θ) + O(ε
2) = εF1(θ, r) + ε
2F2(θ, r, ε).

4 JAUME LLIBRE AND XIANG ZHANG

Applying the averaging theory described for equation (2) to equation (5),
we obtain
 f (r) = 1
2π
 ∫ 2π

0 F1(θ, r)dθ

= − 1
2π
 ∫ 2π

0 cos θ F (r cos θ)dθ

= − 1
2π
 n∑

i=0 airi ∫ 2π

0 cosi+1 θdθ

= − 1
2π
 [(n−1)/2]∑

j=0 a2j+1r2j+1 ∫ 2π

0 cos2j+2 θdθ

=
 [(n−1)/2]∑

j=0 a2j+1b2j+1r2j+1

where
 b2j+1 = − 1
2π
 ∫ 2π

0 cos2j+2 θdθ ̸= 0,

for j = 0, 1, . . . , [(n − 1)/2].

Since the monomials of the polynomial f (r) are r, r3, . . . , r2[(n−1)/2]+1,
and the coeﬃcient a2j+1 in the monomial r2j+1 can be chosen arbitrarily,
we can obtain that the roots of the polynomial f (r) are 0 and ±r1, . . .,
±r[(n−1)/2] with 0 < r1 < . . . < r[(n−1)/2]. Note that all these roots are
simple, i.e. f ′(rk) ̸= 0 for k = 1, 2, . . . , [(n − 1)/2]. Therefore the averaging
theory says that for ε suﬃciently small the diﬀerential equation (5), and
consequently the diﬀerential system (3) have [(n − 1)/2] limit cycles near
the circles of radius rk for k = 1, 2, . . . , [(n − 1)/2]. This completes the proof
of the theorem. □

3. Proof of statement (a) of Theorem 2

The materials of this section follows from [25]. The ﬁrst one characterizes
the structure of system (1) at the inﬁnity in the so called Poincar´e disc, see
Theorem 1 of [25]. Since it is not a result properly on limit cycles we do not
prove it here.

Theorem 3. Let F = a1x+a2x2 +. . .+anxn. The topological phase portrait
of system (1) at inﬁnity is given in Fig. 1.

The second one is on the non–existence of periodic orbits and consequently
on limit cycles of system (1), see Proposition 1 of [25] for a proof. We
reproduce here that proof.

LI´ENARD DIFFERENTIAL SYSTEMS 5

p1p1
 p1p1
 p2p2
 p2p2
 q1q1
 q1q1
 q2q2
 q2q2
n odd, an > 0 n odd, an < 0

n even, an > 0 n even, an < 0

Figure 1. The topological phase portraits of the Li´enard diﬀer-
ential system (1) in a neighborhood of the inﬁnity.

Proposition 4. Let F (x) = E(x) + O(x) with E(x) an even polynomial and
O(x) an odd polynomial. If 0 is the unique root of O(x), then the Li´enard
diﬀerential system (1) has no periodic orbits.

Proof. Consider the diﬀerential system

(6) ˙x = y − E(x), ˙y = −x,

Let ak be the coeﬃcient of the highest order term of E(x). Since this system
is invariant under the symmetry (x, y, t) → (−x, y, −t) the origin of coor-
dinates is a center. Theorem 3 implies that system (6) has the two phase
portraits given in Fig. 2 for n = k even depending on ak > 0 and ak < 0,
respectively.

We study the case ak > 0. For ak < 0 the arguments are completely
same as those of ak > 0. Since each periodic orbit of system (6) intersects
the negative y–axis in a unique point, we deﬁne a function H : R2 → R
as follows: for each p ∈ R2 the value of H(p) is the y–coordinate of the
intersection point of the negative y–axis with the orbit passing through p.
Then H is an analytic function and H(0) = 0 is the unique maximum. By
deﬁnition H is a ﬁrst integral of system (6), so there exists an integrating

6 JAUME LLIBRE AND XIANG ZHANG
 p1p1 p2p2
 q1q1
 q2q2
ak > 0 ak < 0

Figure 2. The phase portrait of system (6).

factor R(x, y) such that

∂H
∂x = xR(x, y), ∂H
∂y = (y − E(x))R(x, y).

Furthermore we have R(x, y) < 0 for (x, y) ̸= (0, 0) because the origin is the
unique maximum and H monotonically decreases in x > 0.
Direct calculations on the orbits of the diﬀerential system (1) show that

dH
dt
 ∣
∣
∣
∣(1) = −O(x) ∂H
∂x = −xO(x)R(x, y).

By assumption we get that the derivative of H along an orbit of (1) vanishes
if and only if x = 0, and that for x ̸= 0 the derivative is either always positive
or always negative. This implies that system (1) has no periodic orbits. □

Proof of statement (a) of Theorem 2. When n = 1 the diﬀerential system
(1) is a linear diﬀerential system in R2, and consequently it has no limit
cycles, because when a linear diﬀerential system has a periodic orbit this
is not isolated in the set of all periodic orbits of the system. This proves
statement (a) of Theorem 2 for n = 1.
Assume n = 2. Then, applying Proposition 4 to system (1) we get that
O(x) = a1x. So the unique root of O(x) is x = 0, and by applying Proposi-
tion 4 the system has no limit cycles. This completes the proof of statement
(a) of Theorem 2. □

4. Proof of statement (b) of Theorem 2

We shall use the following well-known result, the Green’s theorem, for a
proof see for instance [29].

Theorem 5. Let γ be a piecewise smooth, simple closed curve in R2, and
let R be the open region bounded by γ. If P = P (x, y) and Q = Q(x, y)

LI´ENARD DIFFERENTIAL SYSTEMS 7

are functions deﬁned on an open region containing R and have continuous
partial derivatives there, then
∮

γ(P dx + Q dy) = ∫ ∫

R
 ( ∂Q
∂x − ∂P
∂y
 ) dx dy,

where the integration path along γ is in counterclockwise sense.

The divergence of a C1 diﬀerential system

(7) ˙x = P (x, y), ˙y = Q(x, y),

is the function
 div(x, y) = ∂P
∂x + ∂Q
∂y .

Proposition 6. Let γ = γ(t) = (x(t), y(t)) be a periodic orbit of a C1

diﬀerential system (7) of period T . Deﬁne

(8) σ = ∫

γ div(x, y) dt = ∫ T

0 div(x(t), y(t)) dt.

Then, if σ < 0 the periodic orbit γ is a stable limit cycle, and if σ > 0 the
periodic orbit γ is an unstable limit cycle.

For a proof of Proposition 6 see for instance Theorem 1.23 of [10].
The limit cycles for which the value σ deﬁned in (8) is non-zero are called
hyperbolic limit cycles.

First proof of statement (b) of Theorem 2 for n = 3. Set E(x) = a2x2 and
O(x) = a1x + a3x3. If a1a3 ≥ 0, we have either a1a3 > 0, or a1 = 0 and
a3 ̸= 0, or a1 ̸= 0 and a3 = 0, or a1 = a3 = 0. In the last case system (1)
is symmetric with respect to the y–axis, and the origin of coodinates is a
center, so it has no limit cycles. In the other three cases the odd function
O(x) has the unique root x = 0. Therefore, by Proposition 4, system (1) has
no periodic orbits, and consequently no limit cycles. Hence in what follows
we assume that a1a3 < 0.
For a1a3 < 0 we can assume without loss of generality that a1 > 0 and
a3 < 0, otherwise doing the change of variables (x, y, t) → (−x, y, −t) in
system (1) we obtain the wanted assumptions. Since a1 > 0 the singular
point at the origin of coordinates of the diﬀerential system (1) is a stable
focus or node.
Let γ be a periodic solution of the diﬀerential system (1), and −a1 −
2a2x − 3a3x2 is the divergence of that diﬀerential system. We consider the
integral of the divergence along the periodic orbit γ as in (8), i.e.

(9)
 I = − ∮

γ(a1 + 2a2x + 3a3x2)dt

= ∮

γ
 a1 + 2a2x + 3a3x2

x dy,

8 JAUME LLIBRE AND XIANG ZHANG

where we have used the second equation of the diﬀerential system (1). Since
the integral of the ﬁrst line of the expressions (9) is well deﬁned, also it is
well deﬁned the integral of the second line of (9).
In order to apply the Green’s theorem to the integral of the second line
of (9), we shall split such an integral as limit of two integrals as follows.
We add to the periodic orbit γ the segment S of the y-axis contained in
the region bounded by γ, now we split this segment as limit of two parallel
segments S−(ε) and S+(ε) contained in x < 0 and x > 0 and at a distance
ε > 0 of S, respectively, and such that a piece γ−(ε) of γ contained in x < 0
together with S−(ε) forms an oval O−(ε). Similarly, we consider a piece
γ+(ε) of γ contained in x > 0 such that together with S+(ε) forms another
oval O+(ε), in such a way that the union of these ovals tends to γ ∪ S when
ε ↦→ 0.
Since the orbit γ and consequently the ovals O±(ε) are run in clockwise,
and later on we want to apply the Green’s Theorem to these ovals, we orient
the orbit γ and both ovals in counterclockwise sense and denote them with
these new orientations by ̃γ and ̃O±(ε) respectively. Clearly the two integrals
∮
 ̃O−(ε)
 a1 + 2a2x + 3a3x2

x dy and ∮
 ̃O+(ε)
 a1 + 2a2x + 3a3x2

x dy

are well deﬁned, and the integral
∮
̃γ
 a1 + 2a2x + 3a3x2

x dy

is the limit when ε ↦→ 0 of

(10) Iε = ∮
 ̃O−(ε)
 a1 + 2a2x + 3a3x2

x dy + ∮
 ̃O+(ε)
 a1 + 2a2x + 3a3x2

x dy.

Applying the Green’s theorem (Theorem 5) to both integrals of (10) we
obtain that

(11) Iε = ∮
R−(ε)
 (
− a1
x2 + 3a3) dx dy + ∮
R+(ε)
 (
− a1
x2 + 3a3) dx dy,

where R±(ε) are the open regions bounded by the ovals ̃O±(ε). Now, from
(9), (10), (11), taking into account the change of orientation from γ to ̃γ,
and taking the limit of Iε given in (11) when ε ↦→ 0 we obtain that

I = − ∫ ∫
R
 (
− a1
x2 + 3a3) dx dy > 0,

because a1 > 0 > a3, where R is the open region bounded by γ.
By Proposition 6, this implies that all the periodic orbits γ surrounding
the origin of the diﬀerential system (1) are hyperbolic and unstable, con-
sequently at most there is one periodic orbit surrounding the origin, and
when it exists is hyperbolic. This completes the proof of statement (b) of
Theorem 2 for n = 3. □

LI´ENARD DIFFERENTIAL SYSTEMS 9

Our second proof on the uniqueness of limit cycles when n = 3 is again
diﬀerent from the original one and more simple.

Second proof of statement (b) of Theorem 2 for n = 3. In a similar way to
the ﬁrst proof we can assume that a1 > 0 and a3 < 0. Under this assumption
the origin of coordinates is stable, and the inﬁnity is also stable, see Fig.
1. Hence it follows from the Poincar´e–Bendixson Theorem (see for instance
Corollary 1.30 of [10]) that system (1) has at least one periodic orbit.

First we claim that any periodic orbit of system (1) intersects the straight
lines x = ±√−a1/a3. Take

(12) V (x, y) =
 { e−2a2y (
y − a2x2 + 1
2a2
 ) if a2 ̸= 0,
x2 + y2 if a2 = 0,

which is the ﬁrst integral of system (1) with a1 = a3 = 0, i.e. of the
diﬀerential system

(13) ˙x = y − a2x2, ˙y = −x.

Then the derivative of V along an orbit of the diﬀerential system (1) is

(14) ˙V = dV
dt
 ∣
∣
∣
∣
(1) = Lx2 (a1 + a3x2) ,

where L = −2 if a2 = 0 or L = 2a2e−2a2y if a2 ̸= 0. This shows that ˙V does
not change its sign inside the vertical strip −√
−a1/a3 ≤ x ≤ √−a1/a3. On
the other hand V (x, y) is a ﬁrst integral of system (13), so near the origin
the level curves are closed. Moreover, we get from Fig. 2 and the invariance
of V under the symmetry (x, y) → (−x, y) that there exists a closed level
curve of V which contains the origin in its interior and is tangent to both
straight lines x = ±√−a1/a3. Let D be the region enclosed by this closed
level curve of V . Then a periodic orbit cannot intersect D, otherwise there
is a contradiction with the fact that ˙V does not change its sign inside D.
This proves the claim.

Next we prove that system (1) has at most one periodic orbit. By contra-
diction, we assume that ̃Γ and Γ are two diﬀerent periodic orbits of system
(1) with ̃Γ in the interior of Γ and the origin of coordinates in the interior
of ̃Γ. From the last claim we have Fig. 3 which shows the separation of the
two periodic orbits ̃Γ and Γ by the straight lines x = ±√
−a1/a3.

For the function V (x, y) deﬁned in (12) we have that

̃I = ∫

̃Γ
 dV (x, y) = 0, I = ∫

Γ
 dV (x, y) = 0.

On the other hand we will prove that ̃I ̸= I. This contradiction implies that
system (1) cannot have more than one periodic orbit.

10 JAUME LLIBRE AND XIANG ZHANG
 x

y

x = −√
− a1
a3 x = √− a1
a3

p1

p2p3

p4
 ̃p1

̃p2̃p3

̃p4
 Γ
 ̃Γ

q1

q2q3

q4

Figure 3. The graph of the two periodic orbits ̃Γ and Γ separated
by the vertical straight lines x = ±√
− a1
a3 .

From (14) we have

̃I = ∫

̃Γ
 x2 (a1 + a3x2) L(y)dt, I = ∫

Γ
 x2 (a1 + a3x2) L(y)dt,

where L(y) = −2 if a2 = 0 or L(y) = 2a2e−2a2y if a2 ̸= 0. We claim that
̃I < I for a2 > 0, and ̃I > I for a2 ≤ 0.
We only prove the claim for a2 > 0, the proof for the other case follows
using the same arguments than for the case a2 > 0. From Fig. 3 we have

̃Γ = ̂̃p1̃p2 ∪ ̂̃p2 ̃p3 ∪ ̂̃p3̃p4 ∪ ̂̃p4̃p1,
Γ = ̂p1q1 ∪ ̂q1q2 ∪ ̂q2p2 ∪ ̂p2p3 ∪ ̂p3q3 ∪ ̂q3q4 ∪ ̂q4p4 ∪ ̂p4p1.

On γ = ̂p1q1 ∪ ̂q2p2 ∪ ̂p3q3 ∪ ̂q4p4, we have a1 + a3x2 ≥ 0 with the equality
only at the points p1, p2, p3 and p4. Since L(x, y) > 0, it follows that

I0 = ∫

γ x2 (a1 + a3x2) L(x, y)dt > 0.

For convenience to express the integrals, we denote qi = (xi, yi) and ̃pi =
(̃xi, ̃yi) for i = 1, . . . , 4.

For comparing the integrals on ̂q1q2 ⊂ Γ and ̂̃p1̃p2 ⊂ ̃Γ we parameterize
the two orbit arcs as (x1(y), y) and (̃x1(y), y) for y ∈ [y2, y1], respectively.

LI´ENARD DIFFERENTIAL SYSTEMS 11

Then we have

I1 = ∫

̂q1q2
 x2 (a1 + a3x2) L(y)dt =
 y2∫

y1
 x2 (a1 + a3x2) L(y)
−x
 ∣
∣
∣
∣
∣
x=x1(y) dy

>
 y2∫

y1
 x2 (a1 + a3x2) L(y)
−x
 ∣
∣
∣
∣
∣
x=̃x1(y) dy = ∫

̂̃p1 ̃p2
 x2 (a1 + a3x2) L(y)dt = ̃I1,

where we have used y1 > y2, L(y) > 0 and x1(y)(a1 +a3x1(y)2) > ̃x1(y)(a1 +
a3̃x1(y)2) > 0 for y ∈ [y2, y1].

Parameterizing the orbit arcs ̂p2p3 and ̂̃p2̃p3 by (x, y2(x)) and (x, ̃y2(x))
for x ∈ [̃x3, ̃x2] respectively, then we have

I2 = ∫

̂p2p3
 x2 (a1 + a3x2) L(y)dt =
 ̃x3∫

̃x2
 x2 (
a1 + a3x2) L(y)
y − F (x)
 ∣
∣
∣
∣
∣
y=y2(x) dx

>
 ̃x3∫

̃x2
 x2 (a1 + a3x2) L(y)
y − F (x)
 ∣
∣
∣
∣
∣
y=̃y2(x) dx = ∫

̂̃p2 ̃p3
 x2 (
a1 + a3x2) L(y)dt = ̃I2,

where we have used a1 + a3x2 ≤ 0 with equality only at x = ̃x2 and x = ̃x3,
and y2(x) < ̃y2(x) and L(y2(x)) > L(̃y2(x)) for x ∈ [̃x3, ̃x2].

Similarly we have I3 > ̃I3 on the orbit arcs ̂q3q4 and ̂̃p3 ̃p4, and I4 > ̃I4
on the orbit arcs ̂p4p1 and ̂̃p4 ̃p1. Summarizing the above proof we have
I = I0 + I1 + I2 + I3 + I4 > ̃I1 + ̃I2 + ̃I3 + ̃I4 = ̃I. This proves the claim,
and consequently statement (b) of Theorem 2 for n = 3. □

The proof of statement (b) of Theorem 2 for n = 4 was given in [23]. This
proof considers several cases and contains 20 pages, and since we cannot
provide a new and shorter proof of this statement we do not prove it here.

5. Proof of statement (c) of Theorem 2

Here the proof mainly follows from that of [9] by De Maesschalck and
Huzak, who proved the result using slow divergence integrals.
Consider the slow fast Li´enard diﬀerential system

(15) ˙x = y − F (x), ˙y = −εx,

with F (x) polynomial and satisfying

(16) F (0) = F ′(0) = 0, F ′(x)
x > 0 for x ∈ R.

Under the assumption (16) the function y = F (x) has the graph shown in
Fig. 4. For each x > 0 there exists a unique L(x) < 0 such that F (x) =

12 JAUME LLIBRE AND XIANG ZHANG
 x

y
 y = F (x)
Γ
f
x

Γ
s
x

L(x) x

Figure 4. Slow fast cycle Γx.

F (L(x)). The piecewise smooth closed curve

Γx = Γs
x∪Γf
x, Γs
x = {(s, F (s)) : s ∈ [L(x), x]}, Γf
x = {(s, F (x)) : s ∈ (L(x), x)},

is called a slow–fast cycle, which is formed by the fast orbit Γf
x of the layer
equation ˙x = y − F (x), ˙y = 0,
and the slow orbit Γs
x of the reduced equation

0 = y − F (x), y′ = −x with y′ = dy
dτ and τ = εt.

Deﬁne the slow divergence integral associated to Γx

(17) I(x) =
 L(x)∫

x
 f (s)2

x ds, x ∈ (0, ∞),

where f (x) = F ′(x) with prime the derivative with respect to x.
The next result, due to De Maesschalck and Huzak [9, Theorem 2], charac-
terizes the number of limit cycles of the classical Li´enard diﬀerential system
(15) via slow divergence integral.

Theorem 7. Under the condition (16), if the slow divergence integral I(x)
has exactly k simple zeros, then there exists a smooth function λ = λ(ε) with
λ(0) = 0 such that the perturbed system

(18) ˙x = y − F (x), ˙y = ε(λ(ε) − x),

has exactly k + 1 limit cycles provided that ε > 0 suﬃciently small, which
are all hyperbolic.

For computing the slow divergence integral I(x), set

(19) F (x) = Fe(x) + δFo(x),

where Fe is even and Fo is odd, and δ is a small parameter. In [9] there
obtained an asymptotic expression of I as follows.

LI´ENARD DIFFERENTIAL SYSTEMS 13

Proposition 8. The slow divergence integral I(x) associated to the slow–
fast cycle Γx with F (x) of the form (19) has the asymptotic expression

(20) I(x) = 2δI1(x) + O(δ2), I1(x) = ∫ x

0
 (
f ′
e(s)Fo(s) − fe(s)F ′
o(s)
) ds,

with fe(x) = F ′
e(x)/x.

Now we apply Theorem 7 and Proposition 8 to prove statement (c) of
Theorem 2. The proof will be manipulated by induction.
Step 1: n = 6. Choose

Fe(x) = ∫ x

0 sfe(s)ds, fe(x) = 1 + a1x2 + a2x4,

Fo(x) = b1x3 + b2x5,

with (a1, a2) = (−3.1, 2.7) and (b1, b2) = (−0.4, 1). Then

I1(x) = 0.4x3 − 1.248x5 + 1.17429x7 − 0.3x9.

It has exactly 3 positive zeros x1 = 0.824803, x2 = 0.898793, x3 = 1.55761.
So for suﬃciently small δ > 0 I(x) will also have exactly 3 positive zeros.
It follows from Theorem 7 that the classical Li´enard diﬀerential system of
degree 6 could have at least 4 limit cycles.
Step 2: n > 6 even. For any integer k ≥ 3, we write the Li´enard diﬀerential
system (15) of degree 2k in the form

F (x) = F (k)
e (x) + δF (k)
o (x),

with F (k)
o odd of degree 2k − 1 and F (k)
e even of degree 2k and F (k)
e (x) =
∫ x
0 sf k
e (s)ds, where f (k)
e is a polynomial of degree 2k − 2. Correspondingly
we have

I1(x) := I (k)
1 (x) = ∫ x

0
 (
f (k)
e ′(s)F (k)
o (s) − f (k)
e (s)F (k)
o ′(s)
) ds.

For applying induction through perturbation and using Step 1, we assume
that I (k)
1 (x) has 2k − 3 simple zeros and f (k)
e (x) > 0 for x ∈ R, and so the
classical Li´enard diﬀerential system (15) of degree n = 2k has at least n − 2
hyperbolic limit cycles.
Set

F (k+1)
e (x) = ∫ x

0 sf (k+1)
e (s)ds, f (k+1)
e (x) = f (k)
e (x) + 10akx2kµ2,

F (k+1)
o (x) = F (k)
o (x) + bkx2k+1µ2,

where ak is the coeﬃcient of x2k−2 in f (k)
e and bk is the coeﬃcient of x2k−1

in f (k)
o . We have

I (k+1)
1 (x) = ∫ x

0
 (
f (k+1)
e ′(s)F (k+1)
o (s) − f (k+1)
e (s)F (k+1)
o ′(s)
) ds,

14 JAUME LLIBRE AND XIANG ZHANG

which has 2k − 3 simple zeros when µ = 0 by the inductive assumption.
Consequently I (k+1)
1 (x) has 2k−3 simple zeroes near the 2k−3 simple zeroes
of I (k)
1 (x) for µ > 0 suﬃciently small. In addition, I (k+1)
1 (x) has other two
simple zeros appearing in O(1/µ) range. Indeed, some calculations show
that
 I (k+1)
1 (x/µ) = ∫ x/µ

0
 (
f (k+1)
e ′(s)F (k+1)
o (s) − f (k+1)
e (s)F (k+1)
o ′(s)
) ds

= µ−4k+3akbk (
J (k+1)
1 (x) + O(µ2)
) ,

where
 J (k+1)
1 (x) = ∫ x

0 (A
′
k+1(s)Bk+1(s) − Ak+1(s)B′
k+1(s))ds,

with Ak+1(x) = x2k−2 + 10x2k, Bk+1(x) = x2k−1 + x2k+1.

It is easy to check that J (k+1)
1 (x) has exactly 2 positive zeroes, which are
simple. Consequently J (k+1)
1 (x)+O(µ2) has two simple positive zeroes. This
proves that I (k+1)
1 (x) has two simple zeroes in the range O(1/µ), and so has
(2k − 3) + 2 = 2k − 1 positive simple zeroes. By Theorem 7 system (15) of
degree n = 2k + 2 with

F (x) = F (k+1)
e (x) + δF (k+1)
o (x),

has 2k hyperbolic limit cycles.
By induction we complete the proof of statement (c) of Theorem 2 for
any even degree n ≥ 6.
Step 3: n > 6 odd. Set n = 2k + 1 with k > 3. By the proof of Step 2 there
exists a polynomial Li´enard diﬀerential system of degree 2k of the form

(21) ˙x = y − F (x), ˙y = ε0(λ0 − x),

which has 2k − 2 hyperbolic limit cycles. Since these limit cycles are nested
and hyperbolic, the largest one should be either stable or unstable, which
can be assumed without loss of generality to be unstable. We consider the
perturbation of system (21)

(22) ˙x = y − (F (x) + ρx2k+1), ˙y = ε0(λ0 − x),

with ρ ≥ 0 small. Note that the 2k − 2 hyperbolic limit cycles of system
(22) when ρ = 0 persist for ρ > 0 suﬃciently small. In addition, the inﬁnity
of system (22) is a repeller when ρ > 0, and system (22) has a unique ﬁnite
singularity. By the Poincar´e–Bendixson annulus theorem system (22) has
an extra limit cycle beside the 2k − 2 limit cycles. Hence there exist classical
Li´enard diﬀerential systems (15) of degree n which have n − 2 limit cycles.
This proves statement (c) of Theorem 2 for any odd degree n ≥ 6, and
consequently statement (c) of Theorem 2. □

LI´ENARD DIFFERENTIAL SYSTEMS 15

Acknowledgements

The ﬁrst author is partially supported by a MINECO grant MTM2013-
40998-P, an AGAUR grant number 2014SGR-568, and the grants FP7-
PEOPLE-2012-IRSES 318999 and 316338, and from the recruitment pro-
gram of high–end foreign experts of China.
The second author is partially supported by NNSF of China grant num-
bers 11271252 and 11671254, by FP7-PEOPLE-2012-IRSES-316338 of Eu-
rope, and by innovation program of Shanghai municipal education commis-
sion grant 15ZZ012.
 References

[1] A. Andronov, E. Leontovich, I. Gordon and A. Maier, Theory of Bifurcations
of Dynamical Systems on a Plane, I.P.S.T., Jerusalem, 1971.
[2] T.R. Blows and N.G. Lloyd, The number of small-amplitude limit cycles of
Li´enard equations, Math. Proc. Cambrigge Philos. Soc. 95 (1984) 359–366.
[3] P. Bonckaert, Partially hyperbolic ﬁxed points with constraints, Trans. Amer. Math.
Soc. 348 (1996) 997–1011.
[4] T. Carletti and G. Villari, A note on existence and uniqueness of limit cycles
for Li´enard systems, J. Math. Anal. Appl. 307 (2005) 763–773.
[5] M. Caubergh and F. Dumortier, Hilberts 16th problem for classical Li´enard equa-
tions of even degree, J. Diﬀerential Equations 244 (2008) 1359–1394.
[6] W. A. Coppel, Some Analytical Systems with at most one Limit Cycle, Dynamics
Reported, Vol. 2, Edited by U. Kirchgraber & H.O.Walther, John Wiley Sons Ltd,
1989.
[7] P. De Maesschalck and F. Dumortier, Time analysis and entry-exit relation
near planar turning points, J. Diﬀerential Equations 215 (2005) 225–267.
[8] P. De Maesschalck and F. Dumortier, Classical Li´enard equation of degree n ≥ 6
can have [ n−1
2 ] + 2 limit cycles, J. Diﬀerential Equations 250 (2011) 2162–2176.
[9] P. De Maesschalck and R. Huzak, Slow divergence integrals in classical Li´enard
equations near centers, J. Dyn. Diﬀ. Equat. 27 (2015) 117–185.
[10] F. Dumortier, J. Llibre and J.C. Art´es, Qualitative theory of planar diﬀerential
systems, UniversiText, Springer–Verlag, New York, 2006.
[11] F. Dumortier, D. Panazzolo and R. Roussarie, More limit cycles than expected
in Li´enard equations, Proc. Amer. Math. Soc. 135 (2007) 1895–1904.
[12] F. Dumortier and R. Roussarie, Bifurcation of relaxation oscillations in dimen-
sion two, Discrete Contin. Dyn. Syst. 19 (2007) 631–674.
[13] F. Dumortier and R. Roussarie, Multiple canard cycles in generalized Li´enard
equations, J. Diﬀerential Equations 174 (2001) 1–29.
[14] F. Dumortier and R. Roussarie, Canard cycles and center manifolds, Mem. Amer.
Math. Soc. 121 (1996).
[15] J. ´Ecalle, Introduction aux fonctions analysables et preuve constructive de la con-
jecture de Dulac, Hermann, 1992.
[16] A. Gasull, H. Giacomini and J. Llibre, New criteria for the existence and non–
existence of limit cycles in Li´enard diﬀerential systems, Dynamical Systems: An
International Journal 24 (2009) 171–185.
[17] M. Grau, F. Ma˜nosas and J. Villadelprat, A Chebyshev criterion for Abelian
integrals, Trans. Amer. Math. Soc. 363 (2011) 109–129.
[18] M. Hirsch, C. Pugh and M. Shub, Invariant Manifolds, Lecture Notes in Math.
583, Springer–Verlag, 1977.

16 JAUME LLIBRE AND XIANG ZHANG

[19] Yu. Ilyashenko, Finiteness Theorems for Limit Cycles, Translations of Math. Mono-
graphs 94, Amer. Math. Soc., 1991.
[20] Yu. Ilyashenko and A. Panov, Some upper estimates of the number of limit cycles
of planar vector ﬁelds with applications to Li´enard equations, Moscow Math. J. 1
(2001) 583–599.
[21] S. Karlin and W. Studden, Tchebycheﬀ Systems: With Applications in Analysis
and Statistics, Pure and Applied Mathematics, XV, Interscience Publishers John
Wiley & Sons, New York, 1966.
[22] A. Kelley, The stable, center–stable, center, center–unstable and unstable manifolds,
Appendix C in R. Abraham, J. Robbin: Transveral mappings and ﬂows, Benjamin,
New York, 1967.
[23] C. Li and J. Llibre, Uniqueness of limit cycle for Li´enard equations of degree four,
J. Diﬀerential Equations 252 (2012) 3142–3162.
[24] A. Li´enard, ´Etude des oscillations entretenues, Revue G´enerale de l’´Electricit´e 23
(1928) 946–954.
[25] A. Lins Neto, W. de Melo and C.C. Pugh, On Li´enard Equations, Proc. Symp.
Geom. and Topol., Lectures Notes in Math. 597, Springer–Verlag, 1977 pp. 335–357.
[26] J. Llibre, A.C. Mereu and M.A. Teixeira, Limit cycles of the generalized poly-
nomial Li´enard diﬀerential equations, Math. Proceed. Camb. Phyl. Soc. 148 (2009)
363–383.
[27] J. Llibre and M.A. Teixeira, Limit cycles for m–piecewise discontinuous polyno-
mial Li´enard diﬀerential equations, Z. angew. Math. Phys. 66 (2015) 51–66.
[28] P. Mardeˇsi´c, Chebyshev Systems and the Versal Unfolding of the Cusps of Order n,
Travaux en Cours, 57, Hermann, Paris, 1998.
[29] J.E. Marsden and A. Tromba, Vector Calculus, 5th edition, W. H. Freeman, New
York, 2003.
[30] J.L. Massera, Sur un th´eor`eme de G. Sansone sur l’´equation di Li´enard (French),
Boll. Un. Mat. Ital. (3) 9 (1954) 367–369.
[31] J. Pan, Limit cycles of polynomial Li´enard system of degree 4, Nanjing Daxue Xuebao
Shuxue Bannian Kan 17(2000) 211–217.
[32] G.S. Rychkov, The maximum number of limit cycles of the system ˙y = −x, ˙x =

y − 2∑

i=0 aix2i+1 is equal to two, (Russian) Diﬀerential Equations 11(1975) 390–391.

[33] M. Sabatini and G. Villari, Limit cycle uniqueness for a class of planar dynamical
systems, Appl. Math. Lett. 19 (2006) 1180–1184.
[34] G. Sansone, Soluzioni periodiche dell’equazione di Li´enard. Calcolo del periodo (I-
talian), Univ. e Politecnico Torino. Rend. Sem. Mat. 10 (1951) 155–171.
[35] U. Staude, Uniqueness of periodic solutions of the Li´enard equation, in: Recent
Advances in Diﬀerential Equations, Academic Press, 1981, pp. 421–429.
[36] S. Sternberg, On the structure of local homeomorphisms of euclidean n-space II,
Amer. J. Math. 80 (1958) 623–631.
[37] F. Verhulst, Nonlinear diﬀerential equations and dynamical systems, Universitext,
Springer, 1996.
[38] D. Xiao and Z. Zhang, On the uniqueness and nonexistence of limit cycles for
predator–prey systems, Nonlinearity 16 (2003) 1185–1201.
[39] Ye Yanqian et al, Theory of Limit Cycles, Transl. Math. Monographs, 66, Amer.
Math. Soc. Providence, RI, 1986.
[40] X. Zeng, On the uniqueness of limit cycle of Li´enard’s equation, Sci. Sinica Ser. A ,
Chinese Version: 1982, No. 1, 14–20; English Version: 25 (1982) 583–592.
[41] X. Zeng, Remarks on the uniqueness of limit cycles, Kexeu Tongbao (English Ed.)
28(1983) 452–455.
[42] Z. Zhang, D. Ding, W. Huang and Z. Dong, Qualitative Theory of Diﬀerential
Equations, Transl. Math. Monographs, 101, Amer. Math. Soc. Providence, RI, 1992.

LI´ENARD DIFFERENTIAL SYSTEMS 17

[43] C. Zuppa, Order of cyclicity of the singular point of Li´enard’s polynomial vector
ﬁelds, Bol. Soc. Brasil Mat. 12(1981) 105–111.

1 Departament de Matem`atiques, Universitat Aut`onoma de Barcelona, 08193
Bellaterra, Barcelona, Catalonia, Spain
E-mail address: jllibre@mat.uab.cat

2 School of Mathematical Sciences, MOE–LSC, Shanghai Jiao Tong Univer-
sity, Shanghai, 200240, P. R. China
E-mail address: xzhang@sjtu.edu.cn
