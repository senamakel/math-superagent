<!-- source: https://yorkspace.library.yorku.ca/server/api/core/bitstreams/3526f30d-d900-4120-a7a6-8be8637c6841/content | converted from PDF -->

October 21, 2003 1:37 WSPC/Trim Size: 9in x 6in for Proceedings procs˙zhu

FROM THE PP-GRAPHICS TO THE FINITENESS PART OF
HILBERT’S 16T H PROBLEM FOR QUADRATIC SYSTEMS

HUAIPING ZHU∗

Department of Mathematics and Statistics
York University, Toronto, Ontario, Canada, M3J 1P3
E-mail: huaiping@mathstat.yorku.ca

This is part of the eﬀort, the program launched by Dumortier, Roussarie and
Rousseau, in proving the ﬁniteness part of Hilbert’s 16th problem. In this paper,
we highlight the ideas of proving the ﬁnite cyclicity of pp-graphics in quadratic
systems.

1. Introduction

In 1994, Dumortier, Roussarie and Rousseau 4 launched a program aiming
to prove the ﬁniteness part of Hilbert’s 16th problem for quadratic system:
The ﬁniteness part of Hilbert’s 16th problem for quadratic vector
ﬁelds: There exists a natural number N such that any quadratic system
P2(x, y) ∂
∂x +Q2(x, y) ∂
∂y , with P2(x, y) and Q2(x, y) are real quadratic poly-
nomials, has at most N limit cycles, or written as H(2) < ∞.
The program consists in proving the 121 graphics listed in 4 to have
ﬁnite cyclicity among quadratic systems. It has been progressing well since
the 1991 when the program ﬁrst started. Several papers have permitted to
prove the ﬁnite cyclicity of nearly all elementary graphics 1,2,5. The latest
development of the program is summarized by Rousseau in 10. Nilpotent
graphics are among the open cases.
There are two types of nilpotent graphics for quadratic systems: elliptic
and saddle type. The nilpotent graphics and related limit periodic sets were
left unknown in9. The ideas in 7 for dealing with the cuspital loop have been
reﬁned by Zhu and Rousseau 12 and extended to prove the ﬁnite cyclicity of
several graphics of codimension 3 or 4 passing through a nilpotent point of
saddle or elliptic type for any analytic vector ﬁelds. A machinery was built

∗Supported by NSERC in CANADA
 1

October 21, 2003 1:37 WSPC/Trim Size: 9in x 6in for Proceedings procs˙zhu

2
 (a) A pp-graphic
 R

(b) Blow-up

Figure 1. pp-graphics with a nilpotent elliptic point having ﬁnite cyclicity

which can be applied to study the cyclicity of other graphics. Typically,
there are three types of elliptic graphics: PP, HP and HH. The following
theorem was proved in 12.

Theorem 1.1. A pp-graphic with a triple nilpotent elliptic point (Epp)
of any codimension with 2 parabolic and 2 hyperbolic sectors (Fig. 1) has
cyclicity ≤ n (Cycl(Epp) ≤ n) if the regular transition map R calculated
using normalizing coordinates has its n−th derivative non-vanishing.

To apply the above theorem, one always needs to check the hypothesis
on nonlinearity. By using the theorem, for all the pp-graphics of quadratic
systems, the following theorem was proved in 11, (I 1
10a) was also proved in3:

Theorem 1.2. All the 16 pp-graphics of the quadratic systems have ﬁnite
cyclicity.this survey paper, we will use two typical examples of PP-graphics to
explore the ideas and techniques in proving the ﬁnite cyclicity of nilpotent
graphics for quadratic systems.

2. Normal forms of quadratic systems with PP-graphics
and Global blow-up

Theorem 2.1. Any quadratic system with a graphic of the form (H1),
(F1a), (H3) and (I2 a) (Fig. 2) is aﬃne equivalent to
{ ˙x = y + ax2 + cxy − y2

˙y = xy. , a ∈ (0, 1

2 ) (1)

with 0 < c < 2√1 − a for the ﬁrst two cases and c = 2√1 − a for the last
two cases.

October 21, 2003 1:37 WSPC/Trim Size: 9in x 6in for Proceedings procs˙zhu
 3

(a) (H1)(F1a)(F 1
6b)
 (b) (H3)(I2 a)(I 2
17b)

Figure 2. 4 pp-graphics in quadratic vector ﬁelds

Table 1. Limit periodic sets of pp-type for elliptic graphics

graphic Epp1 graphic Epp2 graphic Epp3

By using the classical normal form in6 for a family containing a triple
nilpotent singularity of elliptic type with two parabolic sectors, a new nor-
mal form was developed in12. Applying the reﬁned global blow-up tech-
niques to the new normal form, we get the list of all limit periodic sets
for which ﬁnite cyclicity must be proved. For any pp-graphic, there three
possible passages in the blown-up neighborhood of the elliptic point, Ta-
ble. 1. To verify theorem 1.1 is true for any of the three limit periodic sets,
as shown in Fig. 3, the ingredient is that the transition map from Σ1 to
Σ2 is “almost linear”, so some nonlinearity is needed to conclude the ﬁnite
cyclicity.
 P  P
Σ1 Σ2
T

1 2
λ

Figure 3. The transition map along the pp-passage:“funnelling eﬀect”.

October 21, 2003 1:37 WSPC/Trim Size: 9in x 6in for Proceedings procs˙zhu

4
 Denote Tλ the map along the passage from P1 to P2 (in fact its second
component). Let Vi be the subset of parameters in which the pp limit
periodic set Eppi exists (i = 1, 2, 3). Then if λ ∈ V3 (resp. λ ∈ V2) all the
derivatives of Tλ (resp. T −1
λ ) are suﬃciently small, while for EPP1 with
λ ∈ V1, Tλ(y1) is C k and moderate, has the funnelling eﬀect:

Theorem 2.2. 12 There exists ε0 > 0 such that ∀k ∈ N, a0 ∈ (0, 1
2 ), ∃
A0 ⊂ (0, 1
2 ), a neighborhood of a0 such that ∀(a, ¯µ) ∈ A0 × V1 and ∥λ∥
suﬃciently small, Tλ is C k, and

Tλ(y) = γ0(λ) + γ1(λ)y + hλ(y) (2)

with hλ(y) = o(y) and hλ(y) = O(ν)

3. Finite cyclicity of the hemicycles (H 1
6 ) and (H 3
7 )
Analytic extension principle and its application

The hemicycle (H 1
6 ), Fig. 2(a), is a graphic with a typical pp-connection
and two extra saddle points at inﬁnity, .

Theorem 3.1. The hemicycle (H 1
6 ) has ﬁnite cyclicity.

Proof. The (H 1
6 ) occurs in (1) with a ∈ (0, 1
2 ) and 0 < c < 2√1 − a.
Take sections Σ1 and Σ2 in the normal form coordinates at the entrance
and exit parabolic sectors in the neighborhood of P1 and P2 respectively,
Fig. 4(a). Let Rλ : Σ2 −→ Σ1 be the transition map shown in Fig. 4(a).
Then the cyclicity of (H 1
6 ) is determined by the number of roots of the map
Lλ := Rλ − Tλ(y). By Theorem 2.2, Tλ(y) is almost a aﬃne map, hence we
expect the nonlinearity of R will give the ﬁnite cyclicity.
As shown in Fig. 4(a), discompose Rλ as Rλ = R1 ◦ Dl ◦ R0 ◦ Dr ◦ R2,
here Dl andDr are the Dulac maps in the normal form coordinates in the
neighborhood of the saddle in the inﬁnity, R1 and R2 are regular maps
along x-axis, and R0 : Πr −→ Πl is regular along the equator in the normal
form coordinates on Πr and Πl. It follows from a long and very technical
calculation (details in 11), that

Rλ(y) = β1y + β2y1+σr + o(y1+σr ) (3)

where σr = a
1−a < 1, the hyperbolicity of the saddle point at positive
inﬁnity, β1 > 0 β2 ̸= 0.
The comparison of Rλ and Tλ(y) gives that ∂2
∂y2 Lλ(0) ̸= 0, by which we
get Cycl(H 1
6 ) ≤ 2.

October 21, 2003 1:37 WSPC/Trim Size: 9in x 6in for Proceedings procs˙zhu
 5

Σ Σ Σ Σ
 Π

l

Πl
 r
 r

2
Pl Pr

R

1

(a) The hemicycle (H 1
6 )
 2

0Π

RD
 R
 R D
1 1 2 2

3

D4 0

Sλ
Σ1 Σ2

R
 Π

(b) The hemicycle (H 3
7 )

Figure 4. The transition maps of hemicycle in proving their ﬁnite cyclicity

The proof of the cyclicity of (H 1
6 ) not only relays on the understanding
of the transition near the elliptic point, but depends in particular on the
fact that the equator is invariant which leads to the calculation of R. While
for any graphic in the family (H 1
6a), this becomes impossible since we do
not have the invariance and the expression of the regular orbit. As such,
the following analytic extension principle becomes crucial.

Theorem 3.2. Analytic extension principle Using Poincar´e theorem
stating that it is possible to bring a node to normal form via an analytic
change of coordinates, it is possible to choose normalizing coordinates which
are analytic in the coordinate plane where the singular point has a node
behavior. The section is then analytic and parameterized by an analytic
coordinate inside that plane.
Using the sectorial normalizing theorem for a saddle-node it is possi-
ble to show that there exist a normalizing change of coordinates which is
analytic in the node sector for the zero value of the parameters. Then the
section parallel to the stable (unstable) manifold in the node sector is ana-
lytic for the zero value of the parameters and parameterized by an analytic
coordinate (details in 3).
The transition map must be calculated in normalizing coordinates on
sections parallel to the axes. If a regular transition appears for a graphic
in a family of graphics and if the two sections on which it is deﬁned are
analytic and parameterized by analytic coordinates, then, if the transition
is nonlinear in one point, it is nonlinear everywhere.

It is usually easy to prove the nonlinearity of the transition near one of the
boundary graphics of the family. It follows immediately from Theorem 3.1
and the analytic extension principle that (F 1
6a) has ﬁnite cyclicity.

October 21, 2003 1:37 WSPC/Trim Size: 9in x 6in for Proceedings procs˙zhu

6 3.3. The hemicycle (H 3
7 ) has ﬁnite cyclicity.

Proof. Compare to (H 1
6 ), (H 3
7 ) has an extra saddle-node on the equator
which changes the“balance” of the displacement map used for (H 1
6 ). The
presence of an additional saddle-node allows to conclude that Epp1 and
Epp3 have cyclicity 1.
In case Epp3 some nonlinearity is needed to be able to conclude to
cyclicity 3. As shown in Fig. 4(b), we consider Vλ(y) = Rλ(y) − R−1
1 ◦ Sλ ◦
R−1
2 (y), where Sλ is the inverse of Tλ deﬁned in (2), and Rλ(y) = D1 ◦ R4 ◦
D0 ◦ R3 ◦ D2. It turns out that as one component of R, R3 : Π2 −→ Π0
in the normalizing coordinates contributes to the nonlinearity of Rλ(y).
One can verify through the standard diﬀerentiation-division technique that
the number of roots of Vλ is at most one plus the number of roots of
Wλ(y) = a0(λ) + a1(λ)yσr(λ) + O(y) where a1(λ) = ∗R′′
3 (0) and σr(0) < 1.
Similar to the proof of the nonlinearity of Rλ in (3) 12, one can prove that
R′′
3 (0) ̸= 0. Hence W ′
λ(y) is large for small y and ∥λ∥, yielding that (H 3
7 )
has cyclicity at most 2.

For (I 2
17a), the nonlinearity follows again from the nonlinearity of R3
since the hyperbolic saddle on the right has a hyperbolicity ratio σr(0) < 1,
then the analytic extension principle ensures that (I 2
17a) has ﬁnite cyclicity.

Acknowledgments

The author thanks Y. Ilyashenko, R. Roussarie, F. Dumortier for invita-
tion to Equadiﬀ03, and thanks C. Rousseau, his Ph.D. supervisor, for her
encouragement and help in writing this manuscript.

ReferencesF. Dumortier, M. El. Morsalani and C. Rousseau, Nonli. 9 , no. 5, (1996).
2. F. Dumortier, A. Guzm´an and C. Rousseau, Qual.Th.Dynam.Syst., 3(2002).
3. F. Dumortier, Y. Ilyashenko and C. Rousseau, Erg.Th.Dynam.Syst. 22(2002).
4. F. Dumortier, R. Roussarie and C. Rousseau, J. Diﬀ. Eq. 110 , no. 1 (1994).
5. F. Dumortier, R. Roussarie and C. Rousseau, Nonli. 7 , no. 3(1994).
6. F. Dumortier, R. Roussarie and S. Sotomayor, Lect.NotesinMath., 1480(1991).
7. F. Dumortier, R. Roussarie and S. Sotomayor, Nonli. 10 , no. 6 (1997).
8. A. Guzman, C. Rousseau, J. Diﬀ. Eq., 155, no. 1(1999).
9. A. Kotova and V. Stanzo, Amer. Math. Soc. Transl. Ser. 2, 165, (1995). (1995).
10. C. Rousseau, Lecture Notes for NATO Workshop, Montreal, Oct. (2002).
11. C. Rousseau and H. Zhu, to appear in J. Diﬀ. Eq..
12. H. Zhu and C. Rousseau, J. Diﬀ. Eq., Vol. 178, No.2, 325-436 (2002).
