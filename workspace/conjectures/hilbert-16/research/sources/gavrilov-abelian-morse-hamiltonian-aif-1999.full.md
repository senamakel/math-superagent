<!-- source: http://www.numdam.org/article/AIF_1999__49_2_611_0.pdf | converted from PDF -->

ANNALES DE L’INSTITUT FOURIER

LUBOMIR GAVRILOV
Abelian integrals related to Morse polynomials and
perturbations of plane hamiltonian vector ﬁelds

Annales de l’institut Fourier, tome 49, no 2 (1999), p. 611-652

<http://www.numdam.org/item?id=AIF_1999__49_2_611_0>

© Annales de l’institut Fourier, 1999, tous droits réservés.

L’accès aux archives de la revue « Annales de l’institut Fourier »
(http://annalif.ujf-grenoble.fr/) implique l’accord avec les conditions gé-
nérales d’utilisation (http://www.numdam.org/conditions). Toute utilisa-
tion commerciale ou impression systématique est constitutive d’une in-
fraction pénale. Toute copie ou impression de ce ﬁchier doit conte-
nir la présente mention de copyright.

Article numérisé dans le cadre du programme
Numérisation de documents anciens mathématiques
http://www.numdam.org/

Ann. Inst. Fourier, Grenoble
49, 2 (1999), 611-652

ABELIAN INTEGRALS RELATED TO
MORSE POLYNOMIALS AND
PERTURBATIONS OF PLANE
HAMILTONIAN VECTOR FIELDS

by Lubomir GAVRILOV

Contents.

1. Introduction
2. Modules of polynomial differential forms
3. Milnor bundles
4. Abelian integrals related to Morse polynomials
5. Polynomial perturbations of conservative vector fields
6. Abelian integrals which arise in polynomial perturbations of quadratic Hamil-
tonian vector fields with a center
6.1. Generic quadratic Hamiltonian vector fields with a center
6.2. Reversible quadratic Hamiltonian vector fields with a center
7. Polynomial deformations of a quadratic Hamiltonian vector field and non-
oscillation of Abelian integrals
Bibliography
 1. Introduction.

Let
 Y -H  9  H
 9
^-^Qx'^a y
be a polynomial Hamiltonian vector field. Consider a small polynomial
deformation
 X, =  XH + eY + o(e)

Keywords: Abelian integrals -  Limit cycles.
Math. classification: 35C05 -  34C10.

612 ABELIAN INTEGRALS AND VECTOR FIELDS

of XH , where y=p(.,^+Q(^

is a polynomial vector field of degree n, deg P <: n, deg Q < n. By abuse of
notations o(e) denotes a vector field, whose norm on any compact domain
K C R2 is of type o{e}. The present paper is a contribution in the study of
the number of the limit cycles (isolated periodic orbits) of the perturbed
vector field Xe for sufficiently small \e\.

Suppose that the vector field XH has a non-degenerate singular point
which is a center. Without loss of generality we assume that it is located at
the origin and
 H(x^y) = ^ 2 +2/ 2 )+.•. .

Consider the continuous family of ovals

^h)c{{x^)eR 2:H^y)=h}

which tend to the origin in R2 as h —> 0, and are defined on a maximal open
interval (0, h). Let £ be a closed arc, contained in the open period annulus
u ^w-
he{o,h)

and transversal to the family of ovals ^(h). For sufficiently small \e\ the arc
£ is still transversal to the vector field A^, and can be parameterized by
h = H{x^ y)^. Therefore we can define, on a suitable open subset of £, the
first return map h ^-> Pe{h) associated to the vector field Xg and the arc i,
as it is shown on Fig. 1. The limit cycles of the perturbed vector field X^
correspond to the fixed points of the analytic map Pe(h).

Figure L The first return map Pe(h) associated to
the vector field Xe and the arc ^

LUBOMIR GAVRILOV 613

As Po(h) = /i, then we have

P^K)-h=-eIy{K)^o{e),

where the Poincare-Pontryagin function Iy(K) [25] is given by

(1) Iy{h) = f  f  div(Y) dx A dy, div(V) = P^ 4- O,,.
J J{H<,h}

One may deduce that if k limit cycles of the perturbed vector field X^ tend
to an oval [H =  ho}^ ho € (0, h), then the function Iy(h) has a zero at ho
of multiplicity at least k (Corollary 4).

In contrast to the first return map Pe(h), the Poincare-Pontryagin
function Iy(h) does not depend on the choice of the arc £. It turns out that
if k limit cycles of the vector field X^ tend to the origin in K2 as e —^ 0,
then Iy(h) has a zero at h = 0 of multiplicity at least k + 1 (Corollary 5).
Suppose finally that the closure of the period annulus

LhW
h^(0,h)

is bounded by a homoclinic loop containing one non-degenerate saddle
point of the vector field Xs. Here once again the number of the limit cycles
of Xe which tend to the closed loop, as e —> 0, is less or equal to the
multiplicity (in a generalized sense) of the zero of Iy{h) at h = h, as it has
been proved by Roussarie [26].

The above provides a method to find the number and the location of
the limit cycles of Xs, which tend to the closure of the period annulus of the
non-perturbed Hamiltonian system, subject to the following restrictions:

• the Poincare-Pontryagin function Iy(h) does not vanish identically;

• the closure of the period annulus of the vector field XH is bounded
by a homoclinic loop with a non-degenerate saddle point.

A concrete application of this will be given in Section 7.

Consider the real vector space A (of infinite dimension) formed by all
Poincare-Pontryagin functions I{h) = Iy(H) of the form (1), where P(x, y),
Q{x, y) are real polynomials of arbitrary degree. The real functions I(h) are
most naturally studied in a complex domain, h € C. In this case the oval
{H =  h} C R2 represents a cycle ^(h) ^ ^(ff'^/^.Z ) on the complex
affine algebraic curve

H-\h) = {(x^y) e C2: H(x^y ) = h}

614  ABELIAN INTEGRALS AND VECTOR FIELDS

and I(h) is called an Abelian integral. The vector space ofAbelian integrals
A is a module over the ring R[h] of real polynomials in one variable h:
if I(h) (E A, then hl(h) € A. It was proved in [7] that for a fixed generic
polynomial H the R[h] module A is free and has p, generators, where fi is the
number of the critical points of H. In the present paper we consider the case
when H is a Morse polynomial. This means that all its critical points are of
Morse type (but it can have multiple critical values). We also suppose that
for suitable weights the highest order weight-homogeneous part of H has
an isolated critical point at the origin. Under these assumptions we prove
that A is a free R[h] module of rank Jl < ^. The rank Jl of A is computed
in the following way. The cycle 7(/i) C ^(ff'^/^.Z ) represents a locally
constant section of the global homology Milnor bundle £', associated to
the global Milnor bundle C2 —> C of the polynomial H(x^y) . For a fixed
regular value ho, denote by £^(/io) c  ^ho the minimal complex vector
space which contains the orbit of the cycle 7(^0) under the action of the
monodromy group of H. Then (Corollary 2)

Jl=dimE^o)'

The paper is organized as follows. In Section 2 we recall the definition
of the Petrov module PH associated to a polynomial H and its main
properties. In Section 3 we define the global homology Milnor bundle E of
a semiweighted homogeneous polynomial, and prove some properties of the
subbundle E^ C E associated to the locally constant section ^{h) € E^.
This is used in Section 4, where we establish our main result (Theorem 2).
The rest of the paper is devoted to applications.

Let H be a real cubic polynomial, such that XH has a center at
the origin. The corresponding R[h] modules PH, A and its generators
are computed in Section 6. We compute then the dimension of the
real vector space An C A, formed by Abelian integrals (1) such that
deg(P),deg(Q) ^ n. Part of these results are already known to the
specialists [12], others were used without justification or were erroneously
stated (see Remark 5 after Theorem 4 in Section 7). They can be used
either as an illustration of Theorem 2, or as a reference in further study of
the following Hilbert-Arnold problem.

For a fixed real polynomial H{x^y ) denote by Z(H,n) the exact
upper bound for the number of the zeros of degree n Poincare-Pontryagin
functions (1), degP,degQ <: n, on a maximal interval on which the oval
{H = h} exists. The Hilbert-Arnold problem (called "weakened 16th

LUBOMIR GAVRILOV 615

Hilbert problem" in [4], p. 313, and [17]) is

Find the numbers Z(m^n) =  sup ^Z(H^n)^.
deg H<^m

According to Varchenko-Khovanskii Theorem Z(m,n) < oo. On the other
hand we have obviously
 Z(H,n) > dim An -  1.

It was proved recently [12] that

Z(3,n) <5n+1 5

but the exact value of Z(3, n) is still unknown (even for n =  2!). For special
Hamiltonians H the numbers Z(H,n) are computed in [22], [23], [24], [8]
and [9].

In the last section we compute Z(H^n) and then study the number
of the limit cycles of Xg for a new class of cubic Hamiltonians H. Namely,
suppose that XH is a quadratic vector field with a center, such that

• XH is reversible (it has an axis of symmetry);

• XH has exactly one center and one saddle equilibrium point.

In this case the Hamiltonian function can be put (after a M-linear
change of the variables) in the following normal form:

H{x,y) =  ^{x2 -\-y2) -  ^x 3 -{-axy2, where -  ^ < a < 0.

We show first that
 Z(H,n) = dimAn -  1 = n -  1

(Theorem 4), that is to say the real vector space An has the so called
Chebishev property [3]. In the case a =  0 this result is due to Bogdanov,
IPyashenko (n =  2,3) and Petrov [22], [23] (for arbitrary n). The main
difficulty to study the case —^ < a < 0 is that while for a •== 0 the
rank of the module A is equal to two, in the case — ^ < a < 0 it equals
to three. To prove our result we count zeros of Abelian integrals in a
complex domain by making use of the argument principle. We use the
reciprocity law for differential forms of first and third kind. It should be
noted that the Chebishev property does not hold true in general even for

616  ABELIAN INTEGRALS AND VECTOR FIELDS

cubic reversible polynomials [12]. It depends on the monodromy group
of the global homology Milnor bundle of the polynomial H (compare for
example the Dynkin diagrams shown on Fig. 3).

Suppose at last that, in addition, the Poincare-Pontryagin function
Iy(h) associated to the perturbed vector field Xe is not identically zero.
We prove that the exact upper bound for the number of the limit cycles
of the perturbed vector field Xe^ in any compact domain K C IR
2 is n  — 1.
For a = 0 this was proved by Mardesic [19].

Acknowledgments. — We thank E. Horozov and I. Iliev for the stimu-
lating discussions and critical remarks.

2. Modules of polynomial differential forms.

The results of this section hold over C or R. Therefore we denote by
K either the field of complex numbers C, or the field of real numbers R.
Let /  C US [re, y] be a polynomial and consider the quotient vector space Pf
of polynomial one-forms
 uj == Pdx+Qdy,

modulo one-forms dA + B df where A, B are polynomials. The quotient
space Pf is a module over the ring of polynomials SC[^], under the multi-
plication
 R(t)'uj=R{f)uj, R^K[t\.

Recall that a function f:C 2 —> C is called weighted homogeneous
(wh) of weighted degree d and type

W  =  (Wx.Wy),

w^ = weight (a;) G R, Wy = weight (y) € R if

f(z wxx^^y)=z df^y)^  V^GC* .

We shall also suppose that w^^Wy > 0. By analogy to the case of an isolated
singularity of a germ of an analytic function [2], we give the following

LUBOMIR GAVRILOV 617

DEFINITION 1. — A polynomial f  € K[a;^] is called semiweighted
homogeneous (swh) of weighted degree wdeg(f) = d and type w if it can
be written as
 f=Ef-

where fi are wh-polynomials of weighted degree i and type w, and the
polynomial fd{x^y) has an isolated critical point at the origin.

Note that according to this definition a wh-polynomial with non-
isolated critical point is not semiweighted homogeneous. We define the
weighted degree of a one-form uj =  P dx + Q dy as

wdeg(o;) = max{wdeg(P) + Wa;,wdeg(Q) + Wy}.

The main feature of a swh polynomial is that its global behavior is exactly
as the local behavior of its highest order weight-homogeneous part [6].
Using this the following theorem can be proved

THEOREM 1 (see [7]). — Let f  G K[x,y] be a swh-polynomial of
weighted degree wdeg(/) = d and type w =  {w^.Wy). The K[t\ module
Pf is free and finitely generated by p, polynomial one-forms o;i ^^, ... ,c<;^,
where ^ == {d — Wx){d — Wy)/WxWy. Each one-form uji can be defined by the
condition

(2) duji =  gi da; dy

where g\ ,g^,... ,g^, is a monomial basis of the quotient ring K[x,y}/{fx ,fy).
For every polynomial one-form uj there exist unique polynomials o,k(t} of
degree at most (wdeg(c<;) — wdeg(c<;fc))/wdeg(/) such that in Pf holds

^

LJ =  ^dk(t)(jJk'
k=l

Remark 1. — In [7] the above theorem was proved for K. =  C. In the
case K == R the proof is the same.

Remark 2. — The number p, = (d -  w^)(d -  Wy)/WxWy is the global
Milnor number of the polynomial f(x^y): every regular fiber f~ l(t) C C2

has the homotopy type of a bouquet of fi circles [6]. It is equal, on another

618  ABELIAN INTEGRALS AND VECTOR FIELDS

hand, to the global Milnor number of the highest order weight-homogeneous
part f d  of the polynomial /. Let g\^ g^^... , g^ be a monomial basis of the
quotient ring K.[.r, y]/(f ^ / d). Then one can show that

^
• ^  wdeg(^) = ^;
%=i
• wdeg(^) < 2(d -Wx -  Wy);

• ^i, g-z, ... , ^  form a basis of the quotient ring K[x, y]/{fx , fy)'

Remark 3. — Denote by f^* the complex of polynomial differential
forms on C2 and let ^^/ r  De the complex of relative polynomial forms,
where
 ofc ___"_ _
"c./c- ^-iAd/ '

Let /  G ^° = C[a;,y] be a polynomial with isolated critical points and
suppose that W,TT C O1 represent equivalence classes in the first relative
cohomology group of /

I / _  ^(»^2/c)  _  -^(^2/c)
"  ("C2/C} -  d^/c  -  ^ "  + ^df

and in the Petrov module
 = ^
/ ~ d^2
0 4- ^°d/
respectively. It is easy to check that the identity

d7r =  uj A d/

defines a K-linear mapM^M^j—^^^/c )
which is a bijection. Similarly the map uj ^—> TT, where dc<; == TT establishes a
K-linear bijection ^^^-d^d/ -

The local results of Brieskorn [5] and Sebastian! [28] combined with
Theorem 1 suggest the following

CONJECTURE. — Let f(x,y) € K[.r,^/] be a polynomial with isolated
critical points^ and such that every fiber /~ l(^), t C C is regular at
infinity (see [21]). Then the K[t] module Pf is free and its rank equals the
global Milnor number of f.

LUBOMIR GAVRILOV 619

3. Milnor bundles.

In this section we suppose that /  G lR[rr,?/] is a semiweighted
homogeneous polynomial. It is well known that the global Milnor fibration

(3) C2 -/-^  C

is locally trivial on the complement to the set of critical values

Ac = {ti,t^,... ,ty}

of /  (there are no critical points "at infinity" in this case [6]). To the global
Milnor fibration C2 —> C we associate the homology (resp. cohomology)
Milnor bundle E (resp. £'*). This is a holomorphic vector bundle with
base C -  Ac and fibers Et = H^f- 1 ^^)  (resp. E^ == ^(/-^C)) .
Any two "close" fibers of the global Milnor fibration (3) are isotopic,
which shows that any two "close" fibers of the homology Milnor bundle
are canonically isomorphic. This isomorphism is called the Gauss-Manin
connection of the (co)homology Milnor bundle.

Choose a disc D C C containing Ac and let Ui C D be paths
connecting a fixed point to G QD to iz. To each path Ui we associate a loop
£i € TI-I (D — Ac, to) and each loop ^  defines an automorphism (monodromy)
^^(r^o)^) —^(r^o)^)

Denote by
 H,cH,(f-\to)^C)

the vector space formed by cycles which vanish at the critical value ii
as t —»ti along the path Ui (see the beginning of the section).

DEFINITION 2. — The set of planes H^,H'z,...,H^i s called a weekly
distinguished basis of vanishing planes^ provided that the fundamental
group Ti-i {D — Ac ,^o) is freely generated by the loops i\ ^ ,...  ,iv

DEFINITION 3. — The image of the fundamental group 7Ti(D — Ac^o)
in Aut(H^(f~l{to)) is called the monodromy group of the global homology
Milnor bundle of the polynomial f(x^y) and it will be denoted by M.

620 ABELIAN INTEGRALS AND VECTOR FIELDS

It is well known that the vanishing cycles form a basis of the middle
homology group of an isolated singularity [2]. Combining this with the
results of [6] implies the following direct sum decomposition

(4) ^(r^c)^^,
1=1

The global Milnor bundle E is equipped with the following structures:

1) Each fiber Et = H^f- 1^)^)  of the homology Milnor bundle E
contains a real vector space J:fl(/~'l(^),R) and a lattice -fl^l(/~l(^),Z).

2) On each fiber Ef = H-i(f~l(t),C) we have an integer skew-
symmetric bi-linear form (. ,.): the intersection index of cycles on the
affine curve / -l(^ ) C C2. The intersection form (. , .)|^ is invariant under
parallel transport, and in particular (. ,.)|^ is invariant under the action
of the monodromy group M.

3) The complex conjugation (x^y^t ) —> (x^y^t ) induces an involution
on H^(f~l(t)^C) for t € R, and an anti-holomorphic involution of the
Milnor bundle E

(5) Et—^Et:7(t)——^).

In particular, Ef =  Ef for t € M and (5) is an automorphism.

The intersection form (. ,.) in the fibers Et is degenerate in
general. Let r\ be the compactified and normalized affine algebraic curve
/ -1^)  C C2. We have a natural inclusion
,:/-i(^)_rv

The kernel of the intersection form (. ,.} on H^(f~l(t)^C) coincides with
the kernel of the induced map

i^H^f^W^—.H^C).

PROPOSITION 1. — The cycle 6(to) is a fixed point of the monodromy
group M, if and only if 6 (to) belongs to the kernel of the intersection
form (. ,.).

Indeed, if 6 (to) belongs to the kernel of the intersection form, then
the Picard-Lefschetz formula implies that

M'6(to)=6(to).

LUBOMIR GAVRILOV 621

If M  • 6(to) = 6(to) then we may choose a loop C. € ^\{D — Ac.to) which
makes one turn about all critical values of /. Then ^  is the operator of
classical monodromy of the weighted homogeneous singularity fd (where f d

is the highest order weight homogeneous part of /). In this case we have
^  — id = Varyd o^

and as Var^d \Hi(Tt,c}
 ls injective, then the kernel of ^  — id is the set of
cycles which are homologous to zero on 1^ (equivalently, whose relative
homology class is zero) [2]. Therefore 6(to) belongs to the kernel of the
intersection form (.,.) . D

For any locally constant section 6(t) C H^(f~l(t)^ Z) of the homology
Milnor bundle E denote by
E^cEt^H^r1^)^)

the minimal complex vector space containing the orbit M  • 6 (to). This gives
rise to a flat complex sub-bundle Es of the homology Milnor bundle jEJ,
whose fibers E^t) are obtained from -E'6(to)
 Dv parallel transport. The
holomorphic bundle Eg carries the structures 1) and 2) above. By analogy
to (5) we give the following

DEFINITION 4. — The bundle Es is said to be compatible with the
real structure (the antiholomorphic involution) ofE^ provided that

^)=^(,-) ,  Vt€C .

PROPOSITION 2. — Suppose that the cycle 6(to) is obtained from some
real cycle 6(t) (that is to say 6(t) = 6(t), t e R) by parallel transport.
Then Ef is compatible with the real structure of the complex bundle E.

Proof. — Suppose that 6 (to) is obtained from the real cycle 6(t), t € K
by parallel transport, and let 7(1) be another cycle obtained by parallel
transport along some path u (the ends of u coincide with t, u C C — Ac).
The identity -/
J^{t) «/7(
/ UJ =  I UJ
J^t) J^(f}
implies that the cycle 7(1) is obtained from 6(1) by parallel transport along
the path u, and hence 7(1), 7(1) 6 Et^t € M. As a set of generators of Ef
can be obtained in such a way, we conclude that E^t) = ^6{t) • I
11 a  similar
way we prove that E^(t) = ^6(t} ^
OI an t € C. D

622 ABELIAN INTEGRALS AND VECTOR FIELDS

DEFINITION 5. — We shall say that the bundle Eg satisfies the
condition (^) provided that the following direct sum decomposition holds:

v
M  ^-Q^n^o)}.-Q) ~  VJ^l"^  ' ' ^0{to)
i=l

The condition (^) is motivated by the direct sum decomposition (4).
Of course the decomposition (4) holds for any choice of the paths Ui.
Similarly, the condition (*) does not depend on the choice of the paths ui
(and hence on the choice of vanishing planes Hi), as it follows from the
following simple

PROPOSITION 3. — The bundle E^ satisfies the condition (^), if and
only if
 6{to) =  ^  <^o), where 6i(to) C H, H E^y

COROLLARY 1. — If 6(t) is a vanishing cycle (along an appropriate
path connecting t to a singular value ti) then the bundle E(, satisfies the
condition (-A-).

Proof of Proposition 3. — It suffices to prove that if 7(^0) G E^to),
then
 i/
(6) 7(^0) = ]^7z(^o) where 7^0) € H, H E^y
i=l

If^-* € Aut(I:fl(/-l(^o)) is the monodromy transformation induced by the
loop £j then the Picard-Lefschetz formula [2] shows that

Wto)  =  6(to) + a(^o), a(to) e [H, n E^)}.

and hence 7(^0) = ^^(^o) satisfies (6). The identity (6) follows from the
fact that M  • 6(to) generates Eg^y Q

To check that the condition (-*-) does not depend on the choice of
paths u^ we have to prove that if we replace the plane Hi by i^Hi, then
the identity of Proposition 3 still holds true. Indeed, as

^*^o) = ^o)+a^o) ,

LUBOMIR GAVRILOV 623

where aj(to) € {Hi n E^)}, then

6(to) = ^  <^o) 4- ^(to)  -  a,{to) +  <^o)
k^ij

where ^(to)  G ^-^  0 E^a) and -^(to ) + ^o)  € { ^  H E^,,).

Another important case in which the condition (-*-) is satisfied is given
by the following

PROPOSITION 4. — JfM acts on E^^o) without fixed points then the
bundle Eg satisfies the condition (^).

Proof. — We have

Im(^ -  id)|^^  C Hj n E^to)

and hence

(7) ^dim{lm( ^ -  id)|^J  ^ dimE,^).
j
On the other hand

dim{lm(^ -  id)|^^ J = dimEg^) -  dim{Ker(^-, -  id)|^J,

dim{lm(^.+i),-id)|^^ J

> dim{lm(^+i), -  id)|Ker(^-id)|^J

=dim{Ker(^,-id)|^^ J
-  dim[{Ker(^.+i), -  id)|^J  H {Ker(^., -  id),^^j]

and hence

(8) ^dim{lm(^-id)i^ J

^ dim£^) -  dim{r|Ker(^ -  id)|^^J .
i
As M acts on E^^o) without fixed points, then

nKer(^.-id)|^=0,
i
which combined with (7), (8) gives

i/
^-^{Im^-id)!^ }
j=i
and hence (-*-). Q

624 ABELIAN INTEGRALS AND VECTOR FIELDS

4. Abelian integrals related to Morse polynomials.

Denote by As the vector space of Abelian integrals

(9) I(t) = { ^
Js(t)
over all polynomial one-forms

uj = P(x, y) dx + Q(x, y) dy, P, Q € R[x, y].

This is a R[t] module with multiplication

t' ^ =  / f^^y)^'
UJ =
/<5(t) J<$(t)J6(t} J6(t)
The map

(10) Pf —> As : ^ ^  /' a;
J<5(<)

is a homomorphism of R[t] modules. In the case when /  is a polynomial
with Morse critical points and distinct critical values, the map (10) is an
isomorphism [7], Prop. 3.2, and E^t) = £'t = J^l(/~ l(^C). In the case
of multiple critical values, however, Es may be a proper subbundle of the
homology Milnor bundle E.

In the sequel we shall call 6(to) € H^(f~^(to)^) a vanishing cycle
provided that it vanishes along some path ui as t —>• ti. Note that
this is less restrictive than the usual definition [2] (as we do not use
"morsification" of /). Recall that a cycle 6(t)^ t € R is said to be real,
provided that 6(t) = 6(t).

The central result of the present paper is the following

THEOREM 2. — Suppose that the semiweighted homogeneous
polynomial f  € R[a*,2/] has only Morse critical points. If the vector bundle
Es is compatible with the real structure of the Milnor bundle E, and satisfies
the condition (*), then the R[t] module As is free, finitely generated, and
its rank is equal to the rank ofEs.

COROLLARY 2. — Suppose that the semiweighted homogeneous
polynomial f  C IK[^,2/] has only Morse critical points. If 6(t) is a real
vanishing cycle, then the R[t] module As is free, finitely generated, and its
rank is equal to the rank of the complex vector bundle Es.

LUBOMIR GAVRILOV 625

Remark 4. — As the map (10) is surjective, the generators of As may
be chosen among the integrals over monomial one-forms

^W-  / ^  3= 1,2,...,/,,
^i(t)

where o;j is the basis of Pf defined in Theorem 1.

Proof of Corollary 2. — If the cycle 6(t), t € R is real, then by
Proposition 2 the bundle Es is compatible with the real structure of E.
If the cycle 6(t) vanishes along some path connecting t to a critical value
of /, then by Corollary 1 the bundle satisfies the condition (^). The result
follows from Theorem 2. Q

The proof of Theorem 2 is based on the following

LEMMA 1. — Let 6[ ^2,.. . ,<^, be a basis of locally constant sections
ofEs. There exists a permutation a' = (o-[,a^ .. . ,cr^,), such that

det( [ V^)
v ^)  l/

is a non-zero constant in t, where V is the covariant derivative with respect
to the Gauss-Manin connection of E, and

^  wdeg c^  = // wdeg(/).
1=1

Proof of Theorem 2 assuming the above lemma. — As /  is a swh-
polynomial (Def. 1) then we may deduce that for sufficiently big \t\, such
that the argument of t is bounded, holds

J.'.s',W^[

tS6'.(t)^ u}^ =0(1)

(see the proof of Lemma 2.2 in [7]). This implies that for sufficiently big \t\

^(^'(t)^ ) =0(1)
^'^(^'(t)^)

626 ABELIAN INTEGRALS AND VECTOR FIELDS

and hence
 po(t) -=det( f  ^\
'^(t)  l/

is a polynomial of degree exactly // = ra.nk.Es. By (*), we have

^(to)=(B{^«o)n^}
i

and hence
 ^gpo{t) =^dim{E^to) H H,}.

As /  has only Morse critical points, then po(t) has a zero of order
dim{Es[to) H Hi} at t = ^, and hence

/-
t/

po(^) = C^ J^(t -  ^^^o)^}.
1=1

In particular po(t) does not vanish for ^^^.Ifo;is a polynomial one-form,
then the Cramer's formulae imply that there exist polynomials pi(t), such
that
 r ^ r^
^- Z
/6(t) ^i  J6(t)
(11) po{t) uj=^p,(t) ^ ,  V^)GE^) .
^6rt) ,_-, Jw  ^

Each polynomial p^(^) has a zero of order dim{£'^(^) H ^ }  at ^ = ^, and
hence the polynomial po(t) divides pz{t). It remains to check that pz{t)/pQ{t}
is a real polynomial. As Es is compatible with the real structure of the
Milnor bundle JEJ, then the complex conjugation ^y(t) ^—> ^(t) induces an
automorphism a € Aut(£^)) for t e R. It follows that

pi(t) = det(a)p,(^)

and hence pz(t)/po(t) € R[t\. D

Proof of Lemma 1 in the case when the intersection form (. ,.) is
non-degenerate. — Let Ej- be the vector sub-bundle of E with fibers

E^  =  {-fW e Et: (7(t),^)) =  0, V<^) G ^(,)}.

As the intersection form on Et is non-degenerate, then by Proposition 1
and Proposition 4 the bundles Es and Ej- satisfy the condition (^). We

LUBOMIR GAVRILOV 627

claim further that (. , .)|^^ is non-degenerate. Indeed, if we suppose that
7(^0) € ^6{to)^ 7(^0) 7^ 0, then there exists a vanishing cycle 7/(to) G ^,
such that (^(to),Y{to)) ^  0. The Picard-Lefschetz formula gives

^*7(^o) =  7(^o) -  E^o)^o))7^o )
j

where 7^(to) form a basis of Hi. As

(^7(^7(^o)) =  E<^o)^o)) 2  >  (7(^7^o)> 2 ^  0

3

and ^7(^0) ^ ^<5(to)? th611 we conclude that (. , •)|^^ is non-degenerate.
On its hand this implies that

(12) E=EseE^ .

Let a =  ((T', a" ) be a permutation of the set {1,2,... , p} such that

a 1 =  (a^cr^...^/) , a" == (a'/,^,... ,cr^,,),

^i < (7w>  ^i <  ^Vi

and // = dim-K^^^Q),/^" = dim£1 y Let c<;i,a;25... ,cc;^ be a "monomial"
base of the Petrov module Pf denned by (2), 6' =  (6[,6^... ,^,),

S" =  (6^,6^... ,6^,) be fixed bases of Eg^o) and E^ .  respectively,
6=  {6',6") . Denote by

(/vc A {(y^\  ( ( v^)
^j^
 / ^j^.
 v ^.A^)
 /

the matrices of dimension [L x /^, /^
/ x //, and /^
// x //' respectively. The
Picard-Lefschetz formula implies that the functions

A(t) =  del (  /l Vo;,), A,/(t) =  del (  /V^ )

and
 A^(t)=det ( ( V^// )
'^(t)  t /

are single-valued on C, and hence they are rational functions. On the other
hand each integral J^ V^ can have only logarithmic singularities (as the

628 ABELIAN INTEGRALS AND VECTOR FIELDS

critical points of /  are of Morse type) so the above determinants are in fact
polynomials. We have

(13) A(<)=]^A^)A^ )
a
where the sum is over all the permutations a = (cr',07') as above. It is
proved in [7] that A(t) is a non-zero constant, and

p- [t' p."
^wdego;, = ^wdega;^ + ^wdegc^/ = jLAwdeg(/).
1=1 i=i l %=i
As ^ ^
Y, wdeg o^/ ^  wdeg c^/
deg
 ^o
<
- '^ssjr - "'• ^  ^"o ^ ^^/r  - ""•
then
 deg A^(t) + deg A^(t) ^ 0.
This implies that for any permutation a = (a', a") the polynomial
A^/(t)A^(t) is either a non-zero constant, or it is identically zero. We
conclude that there exists a permutation a = (a', a"), such that the
polynomial Acr/(^)A^(t) is a non-zero constant.

Proof of Lemma 1 in the case when the intersection form {. ,.} is
degenerate. — Let Ft be the compacified and normalized affine curve
/~ 1^). We have ^(r^q^ia-^c)/-
where 6(t) ~ 0 if and only if 6(t) is in the kernel of the intersection form on
H^f- 1^)^). Denote

E = E / ~, E, = J%/ ~, ^  = J^-/ ~, ^  = H,/ ~ .

As the intersection form is non-degenerate on ^(F^C ) then as above we
obtain
 v
ffi(r(,c) = ^(o 0)^), ^ )  = ^{ff. n ^)} ,
z=l
^-QWn^}.
1=1
We already know that
 ^(t)  =  det ( ( Vo;,,.)
'^(t)  /

LUBOMIR GAVRILOV 629

is a non-zero constant [7]. On the other hand if the cycle 6(t) is homologous
to zero on the compactified and normalized fibre .f"1^), then

/  V^-
J6{t)

is a polynomial in t which is a linear combination of the residues of Vo;j. By
Remark 2 the weighted degree of Vci^ is less than d and hence | L(.^ Vci;j |
grows at infinity no faster than a constant. By making use ofR-linear change
of the base (o;i, o;2? -' ' i ^)  and C-linear change of the base (^i, 62,... , <5^)
we may partially diagonalize the /x x fi matrix (J. Vo;o-J:

(14) (/V^) ^  * \  ^-2,=diag(l,l,...,l) ,
^j  / v u lp•-^g/

where g is the genus of the compact Riemann surface 1^, and A is a 2g x 2g
matrix. The first 2g lines of the matrix (14) correspond to integrals over
cycles which form a base of ^(F^C), and the last ji — 2g lines of the
matrix (14) correspond to integrals over cycles homologous to zero on I\.
Respectively the one-forms ci;i, ^25 • • . -> ^2g have no residues on I\, and each
of the remaining p, — 2g one-forms is a normalized differential of third kind.
This new base of one-forms is no-more monomial but each one-form can
still be still chosen weighted homogeneous.

We notice now that del A = A^(t), and hence del A is a non-zero
constant. As in the case of a non-degenerate intersection form, we can
find weighted homogeneous (and hence also monomial) one-forms without
residues, such that the determinant of the corresponding rank Eg x Ef is a
non-zero constant. Complete at last the basis of sections of Es to a basis
of sections of Es by adding zero-homology cycles, as well the basis of first
kind forms by adding normalized third kind forms. The determinant of the
obtained in this way rank Es x rank Es matrix is a non-zero constant, which
completes the proof of Lemma 1. D

5. Polynomial perturbations of conservative vector
fields.

Consider the differential equation

(15) dH +£€<;+ o(e) = 0, \e\ <  1

where H(x^ y) = ^ (a;2-^!/2)^-- • • is a real polynomial, cj, o(e) are polynomial

63 0  ABELIAN INTEGRALS AND VECTOR FIELDS

one-forms on R 2, and the norm of o(e)/e tends to zero on any compact
domain K c  M2, as e -^ 0. Let £ be a closed arc transversal to a continuous
family {H =  h} of closed integral curves of the equation dH =  0 and
parameterized by h = H(x^,. Denote by P^h) be the corresponding
first return map associated to (15) and to the arc £ (see Fig. 1). The limit
cycles of (15) intersecting i  are in one-to-one correspondence with the zeros
of P^(h) -  h. The basic tool in their study is the following

LEMMA 2. — One has

Pe(h) = h-  el(h) + o(e), where I(h) =  ( uj.
J{H=h}

For a proof see [25] or [4], p. 318. Lemma 2 implies immediately the
following

COROLLARY 3 (Poincare-Pontryagin criterion). — If a limit cycle
of (15) tends to the closed integral curve {H =  ho}, as e -^ 0
then I(ho) =  0. If I(ho) =  0 and in addition r(ho) ^  0, then for all
sufficiently small \e\ ^  0 the equation (15) has an unique limit cycle which
tends to {H = ho} as e -> 0.

For every fixed sufficiently small \e\ the first return map P^h) is an
analytic function in a neighborhood of h =  ho ^  0, and hence it can be
analytically continued in a complex domain, h € C. As the complex zeros
of (P^(/i) -  h)/ e in a neighborhood of h =  ho depend continuously on e
then we get

COROLLARY 4. — Suppose that k limit cycles of (15) tend to {H == ho}
ase -^ 0. Then the Abelian integral I(h) has a zero at h =  ho of multiplicity
at least k.

Finally we note that the Poincare-Pontryagin function I(h) contains
an information for the limit cycles which tend to the origin

COROLLARY 5. — Suppose that k limit cycles of (15) tend to the
non-degenerate center 0 e M
2 ase -^ 0. Then I(h) has a zero at h =  0 of
multiplicity at least k + 1.

LUBOMIR GAVRILOV 631

Proof. — Without loss of generality we assume that 0 G R2 is a
non-degenerate singular point of (15) for all sufficiently small \e\. Indeed, if
the coordinates of the singular point are (a(^), b(e))^ where a(0) = &(0) = 0,
then we substitute
 x —> x + a(^), y -^ y + b(e)

in (15). The Poincare-Pontryagin function of the new differential equation
coincides with the Poincare-Pontryagin function of (15). Let £ be a smooth
closed arc through the origin in R2, and transversal to the periodic solutions
{H =  h} in a small neighborhood of the center. It is parameterized by the
analytic function p =  ^/H(x^y)\^. It is classically known that the associate
first return map Pe(p) is an analytic function. Each limit cycle of (15)
which is close to the origin, intersects twice i. As Pe(0) = 0 then it follows
that if k limit cycles of the equation (15) tend to the origin in R2 as e —> 0,
then Pe(p) — p has at least 2k + 1 real zeros in a neighborhood of the origin

p =  0 on £. As before we may continue analytically the function Pe(p) — p in
a complex domain p € C. The zeros of (-Pe(p) — p)/ £ depend continuously
on e and hence the Poinacre-Pontryagin function
w-^^

has a zero of multiplicity at least 2A;+latp=0 . We note at last that

dH +  £LJ +  o(e) =  0 4=^ dp +  e^- + ^  =  0, p2 =  H.
2p Zp

Repeating the arguments from the proof of Lemma 2 in a punctured
neighborhood of the origin in R2 we obtain
^(p)-^ m= ( ^
^P J{H=h}

As the Abelian integral I(h) is analytic in h =  p2, then I(p ) is an odd
function and I(h) has a zero at the origin of multiplicity at least k + 1 in h.
D

^2  ABELIAN INTEGRALS AND VECTOR FIELDS

6. Abelian integrals which arise in polynomial
perturbations of quadratic Hamiltonian vector fields
with a center.

The quadratic polynomial vector fields with a center can be divided
in four dosses: Q^ , Qf, Q§ and Q^ (Zoladek [30]), called Lotka-Volterra
case, Hamiltonian case, reversible case and codimension 4 case respectively.
In this section we shall study the Poincare-Pontryagin functions

I(h)=  [ P(x,y)dy-Q(x,y)d x
J{H=h}

= / /  (^ ,  u) +  Qy{x, y)) dx A dz/, P, Q e R[^, y]
J  u \H<_h}

associate to small polynomial perturbations of quadratic polynomial
Hamiltonian vector fields with a center

(16) ^^4-.P+o(.),  y=-^^eQ^o(e).

If we place the center at the origin and a saddle point at (1,0), the
Hamiltonian function H(x,y) can be written in the following form [13]:

(17) H(x^ y) = \  (x2 + y2) -  ^x 3 + axy2 + ^ by3.

The critical values of H are fti = 0, ^  = j , and the roots of the
polynomial

A(/i)=3 6 (-^+ 4  a 3) 2/,2
-  (144 a4 -  48 a3 -  72 aV  -  36 ab2 -  12 b2 -  6 64)/^

+9a 2 +6a+6 2 +l .

The discriminant of A(/i) is

36(8a 2+4a+6 2) 36 2

and we have also

A(|) = (2a + l) 3^! + 2a)(l -  a)2 -  &
2), A(0) = (3a + I)2 + b2.

LUBOMIR GAVRILOV 633

The Hamiltonian vector field (16) (resp. the Hamiltonian function H (17)),
is said to be reversible, or belongs to Q§, if it has an axis of symmetry. The
Hamiltonian H(x,y) (17) is reversible if and only if

b{(l+2a)(l-a) 2-b 2) = 0

(see [13], Fig. 1, where the non-reversible Hamiltonians with a center were
called "generic"). To state our results we shall use the following standard
notations introduced in [13], [12]

X(h) =f ( x dx A dy, Y(h) =  [ f y dx A dy,
JJH<, h JJH< h

M(h) =1 1 dx/\ dy, L(h) = f[ x2 dx A dy,
JJH< h JJH<, h

K(h) =  1 1 xydx/\dy,
J JH<h

^x =  -xy dx, ujy =  -  j  y2 dx, UJM =  -y dx,

UJL = -^y  dx, UJK == -  i xy2 dx.

Denote by
 6(h)c{{x,y)€R 2: H(x,y)=h}

the continuous family of ovals surrounding the origin in R2, by As the real
vector space of Abelian integrals of the form

/  P(x,y)dy-Q(x,y)dx , P,Q € R[x,y], he^.h^}
J6(h)
and by An C As its subspace formed by Abelian integrals of degree n,
where deg P, deg Q <: n.

6.1. Generic quadratic Hamiltonian vector fields with a center.

In this section we suppose that the real polynomial H(x,y) defined
by (17) is not reversible (equivalently b{(l + 2a)(l -  a)2 -  b2) ^  0).

PROPOSITION 5.

(i) The R[h] modules PH and As are free. The map

(18) PH —^ As : a; •—> I uj
Js{h)

is an isomorphism of modules.

634 ABELIAN INTEGRALS AND VECTOR FIELDS

(ii) Ifb2 — 4a3 ^  0, then the module PH is freely generated by u^x, ^Y,
^Mi ^K- Ifb'2 — 4a3 == 0 the module PH is freely generated byujx^ ^Y-> ^M-

(iii) The real vector space An is of dimension [j(4n + 1)].

Proof. — lib 2 — 4a3 ^  0 the polynomial

H°(x, y ) = -  ^ x3 + axy2 + ^ by3

has an isolated critical point. It follows that

C[^ y]/(H ^ Hy) =  C[x^ y]/(H ^ H^) =  Vect{l, x, y , xy}

and Theorem 1 implies that PH is freely generated by ujx, ^y, ^M-, ^K-
In the case b2 — 4a3 = 0 the polynomial — j x3 + axy2 + j 6?/
3 has non-
isolated critical points and after a real linear change of the variables we
may put the Hamiltonian in the form

(19) c-iX
2 + c-^xy + c^y2 + xy2, c| -  4ciC3 < 0.

As ci 7^ O then this polynomial is semiweighted homogeneous (in
the sense of Section 2), with 2wdeg(^/) =  wdeg(a;) and highest weighted
homogeneous part equal to c^x2 + xy2. Using Theorem 1 we conclude
that PH is free of rank p, =  dimC[x,y]/{Hx^Hy). An easy computation
shows that the global Milnor number of H is equal to three, and moreover

C[x^y]/(H^Hy ) =C[x^y]/(H^H^ = Vect{l^}

which implies Proposition 5, (ii).

To compute the module of Abelian integrals As we note that

(20) H,{H-\ho)^C)=V^

which, combined with Theorem 2 implies that the map (18) is an
isomorphism. Indeed, if H has distinct critical values (8a2 + 4a + b2 ^  0 in
this case) then (20) follows from the fact that the Dynkin diagram of any
(and hence of H) swh polynomial is connected (see for example the proof
of [7], Prop. 3.2). If8a 2+4a+6 2 =  0 the polynomial H has two Morse critical
points and one cusp. The identity (20) follows from an explicit computation
of the orbit of 6 (ho) under the action of the monodromy group. To do this
we need the Dynkin diagram of H which will be computed in the next
section.
 LUBOMIR GAVRILOV 635

It remains to compute the dimension of the vector space An' In the
case when H is a weighted homogeneous (b
2
 — 4a3 -^ 0) polynomial we have

I(h) C An <=^ I(h) =pX+qY+rK+sM

where p, g, r, 5 are real polynomials in h of degree [j(n-2)] , [j(n-2)] ,
[j(n-3)] , [j(n - 1)] respectively. It follows that

dim^=[j(n-2)]+[j(n-2)]+[j(n-3)]+[j(n-l)]+ 4
=[j(4n+l)] .

The above does not work if b2 -  4a3 =  0 but we may compute dim An
in the following way. As As is isomorphic to PH then An is isomorphic (as a
vector space) to the space of degree n polynomial one-forms Pn dx + Qn dy,
modulo polynomial one-forms dA + B dH. Using the isomorphism of the
vector spaces
 PH —> ^/dQ 0 A dH : uj i—> duj

we conclude that An is isomorphic to the vector space of two-forms

Rn-i{x,y)dx /\dy , degRn-i ^ n -  1

modulo two-forms
 dA A dH, deg A{x, y) < n -  2

(see Section 2). Indeed, if g(x,y ) is a homogeneous polynomial, then

dg^d(xy 2)=0  <==^ g(x,y ) = (xy 2^.

Using this and (19) we conclude that if Rn-i(x,y) dx A dy =  dA A dH
where degRn-i <: n  — 1, then there always exists a polynomial An-2 of
degree less or equal to n -  2, such that Rn-i(x, y) dx A dy =  dAn-2 A dH.
Similarly

dAAd^=0 , A^R[x,y] ^  3f e R[/i], A(^) = f(H(x^y)) .

Finally we have

dim An = dim{7?n_i e M[a:,?/]; degJ?n_i < n -  1}
-  dim{A^-2 € R[^^]; degA^-2 ^ n -  2}
+ dim{/ G M[/i]; deg /(^(a:, y)) < n -  2}

=  jn(n+l) -  j(n-l)n+[j(n-2)]+ l

=[j(4n+l)] .

This completes the proof of Proposition 5. D

636 ABELIAN INTEGRALS AND VECTOR FIELDS

6.2. Reversible quadratic Hamiltonian vector fields with a center.

In this section we suppose that the real polynomial H(x, y) defined
by (17) is reversible (equivalently &((! + 2a)(l -  a)2 -  b2) = 0). As a matter
of fact it suffices to study the Hamiltonians (24) below, that is to say 6=0 .
Indeed, any reversible vector field XQ e Q§ can be written in the form [30]

(21) x = y(\ + dx), y = —x — ay2 + ex2.

It has an axis of symmetry {y = 0} and an invariant line {1 + dx = 0}.
If we suppose in addition that (21) is Hamiltonian then we have d = 2a and

(22) H(x,y) = ^(x 2 +y2) -  jx^+axy 2.

The cubic Hamiltonian H(x, y), a ^  0, has a reducible level set

/oo\ ET/ \ 3a-j-c / lV 2  c  2 3a+ c 3a+c \
(23) H(x,y)- -^  =  (.+  ^){ay 2 -  ^ 2  +  -^x-  -^)

and vice versa: any real cubic polynomial with an elliptic critical point and
at least one reducible level set is equivalent, under a real linear change of
the variables, to the Hamiltonian (22). A real homothetic transformation of
x, y shows that the family (22) is naturally parameterized by the projective
line PR1 3 [a: c]. If we put c = 1, then we obtain the following normal form
of cubic reversible Hamiltonians with a center:

(24) ' H(x,y) = ^(x 2+y 2)- j x3 -h axy2, a ^  oo

H(x,y)= ^(x2-{-y2)+xy2, oo.

• For a ^  0, oo the critical points of H(x, y) (24) are (x\,y\) = (0,0),
(^2,2/2) = (1,0), and

/I I /l+2a \
(^3,2/3) =  ( -  n-' +  o- V ——— ).\ 2a 2a V a /

with corresponding critical values
 ( ^ 4)= (-2a 5 -

.  , 1 , , 3a+ l
=0 , ri2 = ^ , hs = h4=
6 24a
3

• For a == 0 we have only two critical points (a;i,^/i) == (0,0),
(^2 ? Vi) = (I? 0), with corresponding critical values h\ = 0 and h^ = -.

LUBOMIR GAVRILOV 637

• For a =  oo the Hamiltonian function (24) has three critical points

(^i)==(0,0) , (x^y,)=  (-!'—) , (^4) =  (-^-— )
2\/2 ^

with corresponding critical values /ii = 0, h^ = /i4 = 1 2 y ^

0
In the case when the critical point (a^,^) is a saddle (center) of
the vector field (16), we shall denote (a^,^) = {x^yf) ((rc^)). Similar
notations will be used for the critical values hi.

The topology of the real fibration

2 HR

is one and the same when a belongs to one of the open intervals ] — oo, —
 1
- [,
] -  j , 0[, ]0,1[, or ]1, oo[. Selected level curves of H are shown on Fig. 2.

Figure 2. Selected level curves of the polynomial (24)
H(x^)=^x 2+y 2)-^x 3+axy 2.

We are going to study now the topology of the global Milnor fibration

2 H
C'

Note that the Hamiltonians (24) are semiweighted homogeneous so
the results of [6], Section 2, apply. In particular we have that for regular
values h e C the complex affine curve H'1^)  C C2 is an elliptic curve
with • one removed point (a = 0),
• two removed points (a = oo),
• three removed points (a ^  0, oo).

638 ABELIAN INTEGRALS AND VECTOR FIELDS

Suppose that ^3,4 ^h\,h^, that is to say a ^  — j , — j , 0,1. Let h =  ho
be a fixed regular value with Im(/io) > 0 and let fi\, £^, ^4  be three mutually
non-intersecting paths, connecting ho to /^, and contained in the upper
half-plane Im(/i) > 0 (except their ends which coincide with hi). Denote
by 6i(h) C ^(^^(/i^Z ) the continuous families of cycles which vanish
at (xi.yi) as h tends to hi along the path ^. For all regular h the cycles
6i(h) form a basis of the first integer homology group of the affine algebraic
curve H^^h) C C2. The families 6i(h) define locally constant sections of
the global homology Milnor bundle of H(x,y ) with base C\{h]_,h-^ ,^3,4}
and fibre H^(H~1 {h), Z). Note that although h^ = ^4, the sections ^3, 6^
are well defined, due to the fact that 6^(h) and 6^(h) vanish in the same
level set of JY, and hence their intersection index is equal to zero.

DEFINITION 6. — The Dynkin diagram of H(x^y} is the graph with
vertices the cycles 61. Two cycles 6z, 6j , hi <  hj, are connected by an edge
(dotted edge) if  the intersection index 6i o 6j is equal to +1 (—1)'

The Dynkin diagram of H describes the intersection indices 61 o 6j,
and hence the monodromy group M. It depends, however, on the homotopy
class of the non-intersecting paths £1.

PROPOSITION 6. — The Dynkin diagram of the polynomial H (24) is
shown on Fig. 3.
 ^  ^ 6
s
, ^  6
s
,

a= 0
 ^

a >  0 j  <a< 0 a<--,

Figure 3. Dynkin diagram of the polynomial (24).

LUBOMIR GAVRILOV 639

Proof. — The critical values of H are easily computed (Table 1).

a <

a =
-,<a

a =  -
- j  <a< 0

a =

0 < a

a >

a =
 i
2
i
2
< 4
i
3

0
< 1

1

00
 h\ < /i|  4 < ^

^L  <  ^3,4 =  ^2

^L  <  ^3,4 <  ^2

^  =  ^3,4 <  ^2

^3.4 <h (i<h^

h^ <h^

h ([<h^< /i|  4

h^ <  /i|  4 <  h^

hc! <  ^1,4

Table 1. The critical values, for a € RP
1, of
H(x^)=^x 2+y 2)-^x 3+axy 2.

In the Hamiltonian triangle case a == 1 the polynomial H has only
real Morse critical points, and all saddle points are contained in the same
level set {H = j}. The Dynkin diagram in this case (as well for a close
to 1) follows from the results ofA'Campo and Husein-Zade [I], [14], [2]. For
a e ]0,1[ or a e ]l,oo[ the polynomial H defines topologically equivalent
global Milnor fibrations (see for example [6], Thm 2.5) and hence its Dynkin
diagram is one and the same.

If a <  — ^ the polynomial H has only real Morse critical points, and
all the saddle points are contained in the level set {H =  (3a + l)/24a3}. As
before we may use the method of A'Campo and Husein-Zade. In the same
way we obtain the Dynkin diagram of the parabolic case a == oo and the
case a=0 .

Note finally that

^,,)=ff(l-..^T^)=|-[J(^+^)-J.3+a^ ]

where a = —a/(l + 2a) is a real polynomial. If a € ] — -  0[ then a > 0 and
hence the Dynkin diagram of H is obtained from the Dynkin diagram of H
(after exchanging 6^ and ^|). D

640  ABELIAN INTEGRALS AND VECTOR FIELDS

Denote the compactified and normalized fibre H'^^h) C C2 by I\.
For every h the affine elliptic curve Jf" 1^) C C2 has an elliptic involution

i : (x,y) •—> (x,-y).

This defines an elliptic involution on I\  which permutes its "infinite"
points. We have

• r\  =J :^- l(/l)UPoUP+UP-, a^0,oo ;

• I\  =  H- 1^)  U P+ U P-, a =  oo;
• r^ji-^upo, a=o

and without loss of generality,

z(Po)=Po, z(P±)=P^ .

If 2; is an uniformizing parameter on the elliptic curve r\, such that z = 0
is a fixed point of %, then z(z) = —2;. It follows that i acts on fZi(I\,Z)
as — id.

PROPOSITION 7. — The Petrov R[h] module Pn associated to the
Hamiltonian (24), is freely generated by the one-forms

•  ^X^Y^M^L,  0^0,00 ;
• UJX^Y^M, a = oo;

• (^X^M, a = 0.

The proof follows from Theorem 1. Indeed, for a 7^ 0,oo the vector
space C[x, y]/(Hx ^ Hy) is generated by 1, re, y , x2, for a = oo by 1, cC, ?/, and
for a= 0 by 1, x. D

Denote by 6(h) C T^"1^) the real oval of H surrounding the origin
in R2, and defined for small positive h and consider the associated R[/i]
module A (9) of Abelian integrals.

PROPOSITION 8. — The R[h] module As associated to the Hamilto-
nian (24) is freely generated by the Abelian integrals

• X(h),L(h),M(h) in the case a ^  0,1,oo;

• L(/i),M(/i) in  the case a =  1;

• X(h)^M(h) in the case a =  0,oo.

LUBOMIR GAVRILOV 641

Proof. — We have i*ujy = o;y, i^6 = —6, and hence Y{h) =. 0.
On the other hand using the Dynkin diagram Fig. 3, Table 1, and the
Picard-Lefschetz formula we get
• if a > 0, a ^  1, then

£^«o) = Span{^(to),^(to),^(to) +W)}, rank£^ = 3;

• if a < 0, then

^(*o) = Span{^(to),^(to)^3(to) + W)}, rankle  == 3;

• ifa=l , then

Es^  = Span{^(to),^(to) + ^(to) + ^o)}, rankle  == 2;

• if a = 0, then

^«o )  =  Span{6^(^o),^(to)}, rankE^ =  2;

• if a == oo, then

^(<o) =  Span{^(to), ^(^o) +  ^(to)}, rankE^ =  2.

If a ^  — -  Proposition 8 follows from Theorem 2. In the case a = — j
the decomposition (12) still holds true which implies Lemma 1 and hence
Theorem 2. Thus Proposition 8 holds also in the case when the cubic
polynomial H is not of Morse type. D

Consider the real vector subspace An C As of Abelian integrals

/  P(x, y) dx + Q(x, y) dy, P, Q € R[x, y], deg(P), deg(Q) < n.
J6

PROPOSITION 9. — The dimension of the real vector space An is n
if  a -^ 1, and [- (2n 4-1)] in  the Hamiltonian triangle case, a =  1.

Proof. — Suppose first that a ^  0,1, oo. In this case the polyno-
mial (24) is semi-homogeneous. An Abelian integral I(h) belongs to the
space An it and only if

I(h) = p{h)X{h) 4- q(h)L(h) 4- r(h)M(h)

where p, g, r are real polynomials of degree at most [ j (n — 2)], [ j (n — 3)],

642 ABELIAN INTEGRALS AND VECTOR FIELDS

and [1. (n — 1)] respectively. As the module Ag is free then

dimAn = [ j (n -  2)] + [^ (n -  3)] + [^ (n -  1)] + 3 = n.

In a similar way in the case case a = 1 we have

I(h)=.q(h)L{h)+r(h)M(h)

where g, r are real polynomials of degree at most [^ (n — 3) and ^ [(n — 1)]
respectively, so

dimAn =  [^(n-3)]+[^(n-l)]+2 =  [^(2n+l)] .

The case a = 0 follows from [23].

Suppose at last that a = oo. We shall modify the proof of Proposition 5
in the case b
2
 — 4a3 =  0. Note first that if a polynomial differential one-form
uj is even in y , Z*LJ = u, i(x,y) = (x, —y), then the corresponding Abelian
integral fgc(^ ^ is identically zero. So it is enough to consider only integrals
of the form t
 UJ^ Z UJ =  UJ.
)6W

If such an integral is identically zero, then we have also

I -/
J6 c(h} J6 3
u =  i uj =  0.
16^ Js^w^m

On the other hand I\ = H~1 U P+ U P- where i permutes P+ and P-. It
follows that uj has no residues, so
i
\  o;=0 .
J6^h)-6W

Thus the restriction of uj on the fibre jy" 1^) represents the zero co-
homology class in ^(^^(/^C) , and its "relative cohomology class"
[uj\ G PH is zero too [7],Thml.2. As in the proof of Proposition 5 we
conclude that the vector space An is isomorphic to the vector space of
two-forms
 uj =  R^_^(x^y) dx A d2/, deg-Rn-i <  n  — 1, i*uj =  uj

LUBOMIR GAVRILOV 643

modulo two-forms dA A dH, where the real polynomial A{x^y) is even in y^
and deg A < n  — 2. Thus we get

dim  An =  dim{Rn-i G ^[x,y] : degRn-i ^  n -  1,
^n-i(;z:,-^) =^_i(a:,?/)}
-  dim{A^_2 G R[.r, ^/] : deg An-2 <: n -  2,

An-2(x,-y) =  -An-2{x,y)}
=  n +  (n -  2) +  (n -  4) +  • • • -  (n -  2) -  (n -  4) -  • • •
=  n. D

7. Polynomial deformations of a quadratic Hamiltonian
vector field and non-oscillation ofAbelian integrals.

Let
 Y  Tf °  T-f
 Q
A ^  — ^y ~^~ ~  li^  ~^~y
 Qx 9y
be a reversible quadratic polynomial Hamiltonian vector field with one
center and one saddle point. It follows from the preceding section that by a
linear change of the variables x, y and t we can assume that

H{x,y) = ^(x 2 +^/ 2) -  1 ^ 3 -\-axy2, where -  z  < a <, 0.

Consider a polynomial deformation of XH of the form

X, =  XH + eY + o(e)

where
 Y=P^y)^Q^y^

is a polynomial vector field of degree n, degP <_ n, degQ ^ n. The first
approximation of the return map associated to Xe is given by the Abelian
integral
 IvW  =  ( ( div(V) dx A dy, div(V) =  P^ +  Qy
J J{H^h}

where h C [0, |  [.

THEOREM 3. — Let Xg be a polynomial deformation of degree n of
the Hamiltonian vector field XH, and assume that Iy{h) is not identically
zero. Let K C R2 be any compact domain. For all sufficiently small e the
vector field Xe has at most n — 1 limit cycles in K. This bound is exact.

644 ABELIAN INTEGRALS AND VECTOR FIELDS

The difficult part of the proof is the study of the Abelian integral Jy.
If a = 0 this is done in a well known paper by Petrov [23], [3]. Based on
this and on Roussarie's theorem [26] Mardesic [19] deduced Theorem 3 in
the case a = 0. Therefore further we suppose that — j < a < 0. Theorem 3
will be proved at the end of this section. We shall find first the exact upper
bound for the number of the zeros of an Abelian integral I(h) € As (we keep
the notations of the preceding sections). Using the method of Petrov, we
shall compute this number in the larger complex domain T> = C\[h^, oo[, in
which I{h) is a holomorphic function. The determination of the domain P
is crucial for the proof, and it amounts to compute the Dynkin diagram
of the polynomial H{x^y) (Proposition 12). The second new observation is
that the imaginary part of the holomorphic function F(h) = r^/M'^h)
on [^,oo[ is an expression involving the "relative" complete Abelian
integral of first kind
 />p+
/  ^M
JP,

(see (27), (25)). This can be used to obtain a more transparent proof of
results in [10], [24].

Recall that, according to the classical terminology a meromorphic
differential one-form on the Riemann surface I\  is said to be of first kind if
it is holomorphic, of second kind if it has no residues, and it is of third kind
if it has only simple poles. Introduce the following notation:

Z(H) =  (3a -  l)X(h) -  4aL(^), ujz =  (3a -  l)^x -  4a^L,
,  __ x dx . _  x dx , _  dx
^X  =  V^X  =  -  -„—  . ^L  =  V^  =  -  -rr—  . ^M  =  V^M  =  -  „ -
Hy  Hy  My

where the one-forms a;x? ^Mi ^L-> and the Abelian integrals X(h), M(K),
L(h) were defined in Section 6.

PROPOSITION 10. — Let a ^  0,oo. The one-form uj^ is of first kind,
a;^ is of second Jcind, and uj'x is of third kind. The only residues of uj'^
are at P±.

Proof. — It is easily checked that u'^ is holomorphic, uj^
 nas ^ly
simple poles, and ^  has at most double poles. As i*^x =  ~UJx anc^
z(Po) = P(0), then Resp^'x = 0. The fact that a;^ has no residues follows
from [12], Remark 3.4.

LUBOMIR GAVRILOV 645

Proposition 10 suggests to replace the Abelian integral I{h) by its
derivative. As the Abelian integral I(h) e As always vanishes at h = 0 then
on any real interval containing h =  0 the number of the zeros of I(h) is less
or equal to the number of the zeros of I'(h ) on the same interval. The next
proposition follows from Proposition 8 (and is in fact equivalent to it).

PROPOSITION 11. — For every Abelian integral I(K) e An, a ^  0,
holds
 I'(h ) =  p{h)X'(h) + qWZ'W  + r(K)M'{K)

wherep.q^r are suitable unique real polynomials of degree at most [^ (n—2)],
[j(n - 3)] and [j(n-l) ] respectively.

Proof. — We use Proposition 8 to express I{h) as a polynomial linear
combination in X(h), Z(/i), M(h) and then derive with respect to h. It
remains to express X(h), Z(h), M(h) as a linear combination in their
derivatives. This is a general fact, but in our particular case we can be
completely explicit. It follows from [12], Remark 3.4, that
-X' + (a + 1)I/ -  Ga/iM' + 4aM = 0,

(-12a2^ + a + \)X' + (2a2 -  a -  1)L' + lIc^X  4- a(l -  o)M =  0,

(6/i -  1)X' + (12ah -  2a)L/ + (3a -  7)X -  16aL + (a + 1)M = 0.

Figure 4. The vanishing cycles on the elliptic curve I\,  — ^ < a < 0?
 2

Let 6i, i = 1,2,3,4 be a basis of vanishing cycles of H^H^ih), Z) as
on Fig. 4. We have
^)=-^  W^-6^  W=-6^  W^-6 8,.

646 ABELIAN INTEGRALS AND VECTOR FIELDS

Consider the vector space An of Abelian integrals

I P{x, y) dx 4- Q(x, y) dy, P, Q G R[x, y], deg(P), deg(Q) <  n
J^

and the vector space A^ == {I^h):!^) € An}' The following observation
is crucial in the proof of the non-oscillation property

PROPOSITION 12. — Every Abelian integral I(h) € An is analytically
continued to a holomorphic function in the complex domain T> =  C\[h^ ,oo[.

Indeed, according to the Dynkin diagram of H , the intersection index
of the cycles 6^ and ^3, 64 is zero. The Picard-Lefschetz formula implies
that I(K) is a holomorphic function in the complex domain P  == C\[h^ oo[.

THEOREM 4. — The space A^ is Chebishev in the complex domain V.

Remark 5.—I n the particular case a =  — j the polynomial (24) can
be put, after a suitable translation, rotation of the axes, and rescaling, in
the form
 H(x,y) =xy+x 3 -}-y3.

In this case Theorem 4 is usually attributed to Petrov (see [3], p. Ill, [17])
who announced it without proof [23], Thm 5. Apparently Petrov believed
that the module of Abelian integrals along the ovals of H has only two
generators, while in fact it has three. This was noted by Rousseau and
Zoladek [27], p. 41, and Zoladek [29], p. 169, who claimed (also without
proof) that the Petrov's result "turns to be not true". A rigorous proof of
Petrov's theorem, based on [8], is first given in [9].

The dimension of A^ is equal to dim An =  ri. To find a bound
for the number of the zeros of I'(h ) € An in V we shall evaluate the
increment of the argument of F(h) =  I'(h)IM'{h ) along the boundary
of P. We recall that uj^ is a holomorphic form and hence M'(/i) does not
vanish [11]. Denote by F^{h) (resp. F~(h)) the analytic continuation of
F(h) on [h^, oo[, along a path contained in the half-plane Im(/i) > 0 (resp.
lm(h) < 0). The Picard-Lefschetz formula implies

^  TmF± ^  . ^ )  J  ^W  ^  ~  kw  ^  ^W  ^
(25) Im F  {h)=±————————^^p—————————.

LUBOMIR GAVRILOV 647

Denote the numerator of the above expression by W^^(uj1,^). By
Proposition 11 we have

^^(^^M) = PW^^(^X^M)+^)^l^(^,^).

As ^'Z^'M nave  no residues (Proposition 10) then the function
^I^O^Z^M ) is single valued in h on the complex plain C and has
no poles. Moreover for \h\ ^  oo the asymptotic estimates

\M\K)\ ^  \h\-^\ \Z\K)\^\h\^

imply that Wg^^ (.^Z^M) ls bounded in h. It follows that it is a (non-zero)
constant. Further the reciprocity law for meromorphic differentials of first
and third kind uj'^ and o/^ [11] imply

(26) HW^M )  =  I ^X  t ^M  -  I ^M  I ^X
«/ 6^ i/ 0)2 v 6-^ J <$^
rP+
=  27^V ::iResp^^ \  uj'^
JP_

where the path of integration from P_ to P+ in the integral above is
contained in r\ cut along the loops 6\{h) and 6^{h) as it is shown on
Fig. 4. Note that Resp^uj^ is an imaginary constant in h, and fp^ uj'^ is
imaginary too. We obtain finally that on the interval [h^ oo[ holds

(27) H^(o/,c^ )  =  p(^)27rv^l [ p+ ^  +  q(h)
JP_

where p(h}, q{h) are real polynomials of degree at most [-(n — 2)] and
[j(n — 3)] respectively. Denote by by Bn the vector space of functions (27),
continued analytically to holomorphic functions in the larger domain
C\] — oo,/i3^4[. Obviously

dim ^  =  [ i  (n -  2)] +  [^ (n -  3)] +  2.

LEMMA 3. — The space of functions Bn is Chebishev in the complex
domain C\] — oo,/i3^[.

Proof. — For \h\ ^  oo we have that \p{h) fp^ uj'^ + q(h)\ grows no
faster than IfajK
72-3)/3] and its imaginary part on ] — oo, h^^[ equals to

±q(h) [ ^,  6(h) € ^(^-^.Z).
J6{h)

648  ABELIAN INTEGRALS AND VECTOR FIELDS

As the one-form uj^ is holomorphic on the elliptic curve I\  (Prop. 10) then
the integral L/^ ^'M can not vanish. The argument principle implies that
^W  fp^ ^M + QW nas  a t "^st deg(p) 4- deg(g) + 1 = dimBn — 1 zeros
in the domain C\] — oo, ^3,4 [. D

Proof of Theorem 4. — Let R be a big enough constant and r a small
enough constant. Denote by T>' the set obtained by removing the small disc
{|/i — h^\ < r} from P  D {[/i[ < J?}. To estimate the number of the zeros
of the Abelian integral I'(h ) in V  (and hence in P) we shall evaluate the
increment of the argument of the function F(h) along the boundary of T>'.

Along the circle {\h\ = R} we have

IF^I^I/^ 71- 1)/ 3

and on the interval }h^ oo[ the imaginary part of F{h) has at most dim Bn — 1
zeros (Lemma 3). At last if h ^  h^ then using the Picard-Lefschetz formula
we have either

(28) IF^I^C^ O

(which is the generic case), or

(29) \F(h)\ ^ ^

or
 \h\k
(30) 1^)1 -TT-^llogWI

In the first case the change of the argument of F(h), when h makes one
turn along the circle {\h — h^\ = r} is close to zero. This yields that the
increment of the argument of F(K) along the boundary of V  is less than

27r(l+ ^(n-l)+dim6n-l ) ^  27r(n -  1)

and hence F(h) can have at most n — 1 zeros in P'. Finally we note that in
the case (29) the argument of F(h) decreases by at least 27rk. This yields
an even sharper estimate for the number of the zeros of F(h). The third
case (30) is similar: we note that the argument of 1/[ log(ft)| decreases along
the circle {\h — h^\ = r}, and this decrease is close to zero. D

LUBOMIR GAVRILOV 649

The above reasonings indicate that it is possible to control the zeros
which "accumulate" at the point h^ on the boundary of V. This will be
used when studying limit cycles in a neighborhood of the separatrix loop of
the unperturbed Hamiltonian system (16).

Recall that in a neighborhood of h^ holds

I^h) = (holomorphic function) log(/i -  h^) + holomorphic function.

Thus we have either

(31) \I\h)\ ^  \(h -  h^ 2  \og(h -  ^)|, where k is even

or

(32) \r(K)\ w\h- ^l^'^ 2 , where k is odd.

It may be shown (Roussarie [26]) then, that any function of the form

I\h) = (holomorphic function) \og(h — h^) 4- holomorphic function,

sufficiently close to I'(h)^ can have at most k zeros in {\h — h^\ < r} D P.
This justifies the following

DEFINITION 7. — We shall say that I'(h ) e An, h € V has a zero of
multiplicity k at h^ € 9V, provided that either the estimate (31), or the
estimate (32) holds.

THEOREM 5. — If the Abelian integral I'(K) e An has a zero of
multiplicity k at h = h^ then it has at most n  — k — 1 zeros in V. This
bound is exact.

Proof. — Consider first the case k even, and the estimate (31) holds.
Then | /  a/ ^\h-h^ 2

• Js^h}^w

and hence ^^'^M^h-h^ 2 .

Thus W^^ (^  ^M) nas  a  zero °^ order at least j k at /^, and by Lemma 3
the number of the zeros of the imaginary part of F(h) on the interval }h^ oo[

650  ABELIAN INTEGRALS AND VECTOR FIELDS

is less or equal to dimBn — 1 — ^k. On the other hand for h ^  h^ holds
|F(/i)| ^  \h\k^. As in the proof of Theorem 4 we compute now the increment
of the argument of F(h) when h makes one turn along the boundary of V
in a positive direction. Taking into account that when h makes one turn
along the small circle {\h — h^\ =  r}, the decrease of the argument of F(h)
is close to Trk we conclude that F(h) has at most n  — k — 1 zeros in V.

The case k odd and the estimate (32) holds is studied in a similar
way. We have
 | ( a/ ^|/i-/ilP+ 1 )/ 2

' Js^h}/6^h)

and hence l^^^^)!^^-^!^- 1 )/ 2 .

It follows that ^i^sO^^M ) nas  a  zero °^
 oraer a t ^ ^  ^{k — 1) at /i|,
and by Lemma 3 the number of the zeros of the imaginary part of F(h)
on the interval ]h^ oo[ is less or equal to dimBn — 1— ^(k — 1). Along the
circle {\h — h^ =  r} holds
 |/J(A-1)/ 2i^^ r

The factor /z^"1)/2 corresponds to a decrease of the argument of F(h) close
to 7r(A: — 1). The factor I/ \og(h} corresponds to a decrease of the argument
of F(h) close to zero. The point is that when h makes one turn along the
circle {\h— h^\ == r}, then the imaginary part of the function F(h)/h^k~l^'2

has exactly one zero (at h =  h^ — r). Using the argument principle we
conclude that F(h) has at most n  — k — 1 zeros in T>. D

Proof of Theorem 3. — Ife is sufficiently small the compact domain K
contains only two critical points of the vector field X^. When e —> 0 a limit
cycle of Xe tends either to a periodic solution of XH, to the origin (0,0), or
to the homoclinic loop {H = -}.

According to the Poincare-Pontryagin criterion the number of limit
cycles of X^ which tend to a periodic solution of XH is less or equal to the
number of the zeros of the Abelian integral Iy(h) on the open interval ]0, -  [,
which on its hand equals the number of the zeros of Iy(h) (as Iy(ft) =  0).
The number of limit cycles which tend to the origin is less or equal to the
order of 7y(/i) at h =  0 minus one, and hence equals to the order of Iy(h)

LUBOMIR GAVRILOV 651

at h =  0. Finally, to evaluate the number of the limit cycles which tend
to the homoclinic loop {H == -}  we shall use Roussarie's theorem [26].
In our case it can be stated in the following form (see [19]): "Suppose that
k limit cycles tend to a homoclinic loop with a non-degenerate saddle point,
as e —f 0. Then the Abelian integral Iy(h) has a zero of multiplicity at least k
at h = /i2." Theorem 5 implies Theorem 3. D

BIBLIOGRAPHY

[I] N. A'CAMPO, Le groupe de monodromie du deploiment des singularites isolees de
courbes planes, I, Math. Ann., 213 (1975), 1-32.

[2] V.I. ARNOLD, S.M. GUSEIN-ZADE, A.N. VARCHENKO, Singularities of Differen-
tiable Maps, vols. 1 and 2, Monographs in mathematics, Birkhauser, Boston, 1985
and 1988.

[3] V.I. ARNOLD, Yu. S. IL'YASHENKO, Ordinary Differential Equations, in 'Dyna-
mical Systems, I', Encyclopaedia of Math. Sci., vol. 1, Springer, Berlin, 1988.

[4] V.I. ARNOLD, Geometrical Methods in the Theory of Ordinary Differential
Equations, Springer, New York, 1988.

[5] E. BRIESKORN, Die Monodromie der isolierten Singularitaten von Hyperflaschen,
Manuscripta Math., 2 (1970), 103-161.

[6] L. GAVRILOV, Isochronicity of plane polynomial Hamiltonian systems, Nonlinea-
rity, 10 (1997), 433-448.

[7] L. GAVRILOV, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math.,
122 (1998), 571-584.

[8] L. GAVRILOV, Nonoscillation of elliptic integrals related to cubic polynomials of
order three, Bull. London Math. Soc., 30 (1998), 267-273.

[9] L. GAVRILOV, Modules of Abelian integrals, Proc. of the IVth Catalan days of
applied mathematics, p. 35—45, Tarragona, Spain, 1998.

[10] L. GAVRILOV, E. HOROZOV, Limit cycles of perturbations of quadratic vector
fields, J. Math. Pures AppL, 72 (1993), 213-238.

[II] P.A. GRIFFITHS, J. HARRIS, Principles of Algebraic Geometry, John Wiley and
Sons, 1978.

[12] E. HOROZOV, I. ILIEV, Linear estimate for the number of zeros of Abelian
integrals with cubic Hamiltonians, Nonlinearity, 11 (1998), 1521-1537.

[13] E. HOROZOV, I.D. ILIEV, On the number of limit cycles in perturbations of
quadratic Hamiltonian systems, Proc. London Math. Soc., 69 (1994), 198-224.

[14] S.M. HUSEIN—ZADE, Dynkin digrams of singularities of functions of two variables,
Functional Anal. AppL, 8 (1974), 10-13, 295-300.

[15] I.D. ILIEV, Perturbations of quadratic centers, Bull. Sci. Math., 122 (1998),
107-161.

[16] I.D. ILIEV, Higher-order Melnikov functions for degenerate cubic Hamiltonians,
Adv. Diff. Equations, 1 (1996), 689-708.

[17] Yu. IL'YASHENKO, Dulac's memoir "On Limit Cycles" and related problems of
the local theory of differential equations, Russian Math. Surveys, 40 (1985), 1—49.

652 ABELIAN INTEGRALS AND VECTOR FIELDS

[18] B. MALGRANGE, Integrales asymptotiques et monodromie, Ann. scient. EC.
Norm. Sup., 7 (1974), 405-430.

[19] P. MARDESIC, The number of limit cycles of polynomial deformations of a
Hamiltonian vector field, Ergod. Th. and Dynam. Sys., 10 (1990), 523-529.

[20] P. MARDESIC, Chebishev systems and the versal unfolding of the cusp of order n,
Hermann, collection Travaux en Cours, 1998.

[21] W.D. NEUMANN, Complex algebraic curves via their links at infinity, Inv. Math.,
98 (1989), 445-489.

[22] G.S. PETROV, Number of zeros of complete elliptic integrals, Funct. Anal. Appl.,
18 (1984), 73-74.

[23] G.S. PETROV, Elliptic integrals and their nonoscillation, Funct. Anal. Appl., 20
(1986), 37-40.

[24] G.S. PETROV, Nonoscillation of elliptic integrals, Funct. Anal. Appl., 24 (1990),
45-50.

[25] L.S. PONTRYAGIN, On dynamic systems close to Hamiltonian systems, Zh. Eksp.
Teor. Fiz., 4 (1934), 234-238, in russian.

[26] R. ROUSSARIE, On the number of limit cycles which appear by perturbation of
separatrix loop of planar vector fields, Bol. Soc. Bras. Math., (2), vol.17 (1986),
67-101.

[27] C. ROUSSEAU, H. ZOLADEK, Zeros of complete elliptic integrals for 1: 2
resonance, J. Diff. Equations, 94 (1991), 41-54.

[28] M. SEBASTIANI, Preuve d'une conjecture de Brieskorn, Manuscripta Math., 2
(1970), 301-308.

[29] H. ZOLADEK, Abelian integrals in unfolding of codimension 3 singular planar
vector firlds, in 'Bifurcations of Planar Vector Fields', Lecture Notes in Math.,
vol. 1480, Springer (1991).

[30] H. ZOLADEK, Quadratic systems with center and their perturbations, J. Diff.
Equations, 109 (1994), 223-273.
 Manuscrit recu Ie 15 juillet 1998,
accepte Ie 8 octobre 1998.

Lubomir GAVRILOV,
Universite Paul Sabatier
Laboratoire Emile Picard, UMR 5580
118, route de Narbonne
31062 Toulouse Cedex (Prance).
gavrilov@picard.ups-tlse.fr
