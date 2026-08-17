<!-- source: https://users.ugent.be/~stluca/Preprints/A1_2009_LUCA_Alien_Limit_Cycles.pdf | converted from PDF -->

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Detecting alien limit cycles near a Hamiltonian
2-saddle cycle

S. Luca1, M. Caubergh
2, F. Dumortier
1 and R. Roussarie
3

1stijn.luca@uhasselt.be, freddy.dumortier@uhasselt.be, Departement Wiskunde,

Universiteit Hasselt, Campus Diepenbeek, Agoralaan-Gebouw D, B-3590 Diepenbeek, Belgium
2magdalena.caubergh@uab.es, Departament de Matem`atiques, Ediﬁci C,

Universitat Aut`onoma de Barcelona, 08193 Cerdanyola de Vall`es, Barcelona, Spain
3roussari@haydn2002.ubourgogne.fr, Institut de Math´ematiques,

Universit´e de Bourgogne, BP47870, 21078 Dijon Cedex, France

Abstract

This paper aims at providing an example of a cubic Hamiltonian 2-
saddle cycle that after bifurcation can give rise to an alien limit cycle;
this is a limit cycle that is not controlled by a zero of the related Abelian
integral. To guarantee the existence of an alien limit cycle one can verify
generic conditions on the Abelian integral and on the transition map as-
sociated to the connections of the 2-saddle cycle. In this paper, a general
method is developed to compute the ﬁrst and second derivative of the
transition map along a connection between two saddles. Next, a concrete
generic Hamiltonian 2-saddle cycle is analyzed using these formula’s to
verify the generic relation between the second order derivative of both
transition maps, and a calculation of the Abelian integral.
Keywords: Planar vector ﬁeld, Hamiltonian perturbation, limit cycle,
Abelian integral, two-saddle cycle, alien limit cycle, transition map.
MSC2000: 34C23, 34C25, 34E10, 34C25, 34C20, 34C08

1 Introduction and settings

We deal with perturbations of Hamiltonian systems:

(X(µ,ε)) :
 



 ˙x = − ∂H
∂y + εf,

˙y = ∂H
∂x + εg, (1)

where H(x, y), f (x, y, µ, ε), g(x, y, µ, ε) are C ∞ functions, ε is considered to take
small positive values and µ varies in some compact subset K ⊂ Rp. Further we
abbreviate µ = (µ, ε).
We suppose that the ﬂow of X(µ,0) = XH contains a period annulus bounded
by a hyperbolic 2–saddle cycle L as in Figure 1. A period annulus is a subset of
the plane ﬁlled by closed orbits of XH . The hyperbolic 2–saddle cycle consists
of two saddle–connections Γ1 and Γ2 and two hyperbolic saddles s1 and s2 such
that s1 := α(Γ1) = ω(Γ2) and s2 := α(Γ2) = ω(Γ1). We choose H to be zero on
the 2–saddle cycle and strictly positive on the nearby closed orbits.

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

s1 s2

L Γ2

Γ1
 Figure 1: A 2–saddle cycle lying on the boundary of a period annulus.

In [9] it is proven that, for µ ∈ K and ε > 0 near zero, L can produce
limit cycles that are not controlled by zeros of the related Abelian integral (cfr.
(5)); these limit cycles are also called ‘alien limit cycles’ (cfr. [1]). In [9], one
found that exactly one alien limit cycle exists in a ‘generic’ unfolding (1) of
codimension 4, leaving one connection of the 2-saddle cycle unbroken. A precise
deﬁnition is given in Deﬁnition 2.
The principal result in this paper establishes the presence of this bifurca-
tion phenomenon of alien limit cycles in the unfolding (X(µ,ε)) of the quadratic
Hamiltonian system XH with two centers and two heteroclinic loops:
{ ˙x = 1 − 1
4 y2 − x2 + ε[µ3xy + µ4y2x + y(x2 + 1
12 y2 − 1)(x − √3π
8 xy)],

˙y = 2xy + εy(µ1 + µ2x). (2)
where the Hamiltonian H is given by

H(x, y) = y(x2 + 1
12 y2 − 1). (3)

Notice that this system was also studied in [6]. Veriﬁcation of the generic
conditions that guarantee the presence of an alien limit cycle that bifurcates
from the 2-saddle cycle lying in {y ≤ 0} , is quite involved.
For an unfolding to be ‘generic’, besides a genericity property on the re-
lated Abelian integral (cfr. (5) , (6) , (9) and (10)), a genericity property of the
second order derivative of the transition map along the saddle connections (cfr
(7) , (8) and (11)) have to be satisﬁed as well. Sections 4, 5 and 6, present useful
techniques to check the generic conditions in concrete examples.
In this paper we prove the following results. We obtain general formulas for
the second order derivative of the transition map near a saddle connection, that
remains unbroken in an smooth unfolding of a Hamiltonian vector ﬁeld; these
formulas are stated in section 6: Corollaries 18 and 19 respectively. Next, in
section 7, using the developed machinery, in Section 7 the generic conditions
are veriﬁed in the concrete system (2) ; we conclude that the generic properties
described in Deﬁnition 2 all are satisﬁed; in particular, from the result in [9],
we can conclude with:

Theorem 1 Let (X(µ,ε)) be the unfolding of the Hamiltonian vector ﬁeld XH
given in (2) with Hamiltonian H given in (3) ; let L be the 2-saddle cycle with
saddle points (−1, 0) and (1, 0) , lying in the half plane {y ≤ 0} . Then,

1. (X(µ,ε)) is a generic unfolding of codimension 4, leaving the connection
{y = 0} unbroken, in the sense of Deﬁnition 2.

2

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

2. Hence, the bifurcation diagram of limit cycles bifurcating from L with re-
spect to (µ, ε), for ∥(¯µ, ε)∥ suﬃciently small, ε > 0, exhibits a swallow tail
catastrophy.

3. In particular, there exists an alien limit cycle bifurcating from L for (¯µ, ε) =
(0, 0) ; i.e. there exist parameter values (¯µ, ε) arbitrarily close to (0, 0) such
that X(µ,ε) has 4 limit cycles tending to L when ∥(¯µ, ε)∥ → 0, while the
Abelian integral has at most 3 zeroes near h = 0.

In this paper, we only study the 2-saddle cycle in the half plane {y ≤ 0} ; one
can study the 2-saddle cycle in the half plane {y ≥ 0} with the same reasoning.
Notice that the results obtained in sections 4, 5 (and 6) are valid for arbitrary
analytic families of vector ﬁelds (perturbations of a Hamiltonian vector ﬁeld);
only in section 7, we work with the concrete Hamiltonian unfolding (2) .
The paper is organised as follows. In section 2, the generic conditions are
speciﬁed; in section 3, appropriate normal forms near the hyperbolic saddles
s1 and s2 are given, that are used to calculate the second order derivative of
the transition maps R1
µ and R2
µ in Sections 4, 5 and 6. In section 4, relying
on [2], general formulas for the second order derivative of the transition map
near a saddle connection, that remains unbroken in an smooth family of vector
ﬁelds. In section 5 (respectively 6), these formulas are translated for smooth
families of vector ﬁelds when expressed in normalizing coordinates (respectively
for smooth unfoldings of a Hamiltonian vector ﬁeld). Finally, using the devel-
oped machinery, in Section 7 the generic conditions are veriﬁed in the concrete
Hamiltonian system (2).

2 Generic conditions

Throughout this article we suppose that (Xµ) is a smooth unfolding of a Hamil-
tonian vector ﬁeld XH like in (1) such that XH admits a period annulus bounded
by a 2-saddle cycle L like in Figure 1 and where µ varies in some neighbour-
hood of (µ0, 0), µ0 ∈ K. After a translation in parameter space, one can always
suppose that µ0 = 0. Furthermore, we suppose that the connection Γ2 remains
unbroken by the unfolding.
In studying limit cycles bifurcating from such a 2-saddle cycle L for µ ∈ K
and ε > 0 near zero, it is convenient to consider the so-called diﬀerence map
∆ between two sections transverse to L (see [9]). We here brieﬂy recall its
deﬁnition. Take transverse sections Σ1 (respectively Σ2) and Σ3 (respectively
Σ4) near s1 and s2 respectively, transverse to Γ2 (respectively Γ1). Let u, v, z
and w be regular parameters that parametrize Σ1, Σ2, Σ3 and Σ4 respectively.
In the respective parametrizations, Γ2 ∩ Σ1 is represented by u = 0, Γ2 ∩ Σ3 by
z = 0, Γ1 ∩ Σ2 by v = 0, and Γ2 ∩ Σ4 by w = 0, see Figure 2.
Then, we consider the regular transition maps R2
µ from Σ1 to Σ3 along Γ2
deﬁned by the ﬂow of −X(¯µ,ε), and R1
µ from Σ2 to Σ4 along Γ1, deﬁned by the
ﬂow of X(¯µ,ε). Let D1
µ (respectively D2
µ) be the corner passages near the saddle
s1 (respectively s2) deﬁned by the ﬂow of X(¯µ,ε) (respectively −X(¯µ,ε)), see Fig-
ure 2. We suppose that all these transition maps are expressed in function of the
chosen regular parameter on the sections Σi, i = 1, . . . , 4. They are only locally
deﬁned: ε as well as the regular parameter u, v, z, w take on small positive values.

3

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

D 1
µ D 2
µ

R 2
µ
 Γ 3 ,z

Γ 4 ,wΓ 2,v

Γ 1,u
 R 1
µ
s1 s2
 Figure 2: Transition maps near a 2–saddle cycle.

Now the diﬀerence map ∆µ : Σ1 → Σ4 is locally deﬁned as:

∆µ(u) = ∆(u, µ) = ∆2(u, µ) − ∆1(u, µ),

for u > 0, with

∆1(u, µ) = ∆
1
µ(u) = R1
µ ◦ D1
µ (u) , ∆2(u, µ) = ∆
2
µ(u) = D2
µ ◦ R2
µ(u).

Clearly, for µ near (µ0, 0), µ0 ∈ K, limit cycles of Xµ near L, correspond to
positive zeroes u of ∆µ, for u near 0. In particular, we can write

∆ = ε∆, (4)

for a C ∞ map ¯∆.
As for the traditional displacement map (retour mapping minus identity),
the linear part of ∆ with respect to ε is related to the Abelian integral Iµ(h) for(X(¯µ,ε))
ε (cfr. [9]):

∆(u, µ, 0) = Iµ(h) ≡ I(h, µ) ≡ ∫

γh f dy − gdx, h > 0, (5)

where γh is the non-isolated periodic orbit of XH lying inside of {H = h} and
passing through the point u on Σ1. Furthermore, it is well-known that I(h, µ) ad-
mits an asymptotic expansion in the logarithmic scale 1, h, . . . , hi, h
i log h, . . . :
there exist smooth functions p, q, r, s in ¯µ such that

Iµ(h) = p(µ) + q(µ)h log h + r(µ)h + s(µ)h2 log h + O(h
2), h ↓ 0. (6)

The coeﬃcients p, q, r, s in this expansion can be calculated using Picard-Fuchs
equations (cfr. section 7 for an example).
The notion of a generic unfolding of codimension 4 also involves the asymp-
totics of the regular transition maps R1
µ and R2
µ. In Section 6, it will be shown
that, up to terms of order O (ε) , ε ↓ 0, the transition maps R1
µ and R2
µ are the
identity map, when expressed in appropriate normalizing coordinates near the
saddles:
 R1
µ(v) = v + ε(−β1(µ) + γ1(µ)v + η1(µ)v2 + O(v3)), u ↓ 0, (7)

for some smooth functions β1, γ1, η1 in the parameter µ = (µ, ε) and

R2
µ(u) = u + ε(−β2(µ) + γ2(µ)u + η2(µ)u
2 + O(u
3)), u ↓ 0,

4

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

for some smooth functions β2, γ2, η2 in the parameter µ = (µ, ε). Furthermore,
since Γ2 remains unbroken, we have that β2(µ) = 0, ∀µ, and after performing a
parameter dependent coordinate change in u, one can suppose that γ2(µ) = 0
yielding to: R2
µ(u) = u + ε(η2(µ)u
2 + O(u
3)), u ↓ 0, (8)

for some smooth function η2 in µ = (¯µ, ε) .

Deﬁnition 2 Let (X(¯µ,ε)) be a C ∞ unfolding of a Hamiltonian vector ﬁeld XH
like in (1) . Suppose that Γ is a 2-saddle cycle of XH , of which one connection,
say Γ2, remains unbroken by the perturbation. Let I¯µ be the related Abelian
integral of (X(¯µ,ε))
ε given in (5) with asymptotic expansion (6) . Let r1(µ) be
the hyperbolicity ratio of the saddle of Xµ lying near s1, then we deﬁne α1(µ) :=
α1(µ, 0) by r1(µ) = 1 + εα1(µ).

Let R1
µ (respectively R2
µ) be the regular transitions along the connection Γ1 (re-
spectively Γ2). Then, we say that (X(¯µ,ε)) is a generic unfolding of XH of codi-
mension 4, if

1. the Abelian integral is of codimension 3, i.e.,

p(0) = q(0) = r(0) = 0, s(0) ̸= 0. (9)

and the map
 (Rp, 0) → (R4, 0
) : µ ↦→ (p(µ), q(µ), r(µ), α1(µ)) (10)

is a local submersion at zero.

2. the functions η1 and η2, deﬁned by the asymptotic expansions of R2
µ and
R1
µ in (7) (respectively (8)), satisfy the following generic condition:

η2(0) ̸= 2η1(0). (11)

Remark 3 The main result in [9] implies that a 2-saddle cycle for such a
generic Hamiltonian unfolding (X(¯µ,e)) of codimension 4 can produce for limit
cycles, while it is clear that the related Abelian integral I¯µ can have at most 3
zeroes that bifurcate from h = 0, for ¯µ near 0. This is striking since in case that
L is a saddle-loop and the Abelian integral is generic, there is a 1-to-1 corre-
spondence between the bifurcation diagram of the limit cycles perturbing from
the Hamiltonian saddle loop and the zeroes of the related Abelian integral (cfr.
[14]).

Remark 4 Notice that

η1 (0) = 1
2 ∂2R1
ε
∂v2 (0) and η2 (0) = 1
2 ∂2R2
ε
∂u2 (0).

The map R1
µ describes the transition of the ﬂow of X(¯µ,ε) near a connection
that is not preserved by the perturbation (ε > 0), therefore the calculation of
η1 (0) is more complicated than the one of η2 (0) . However, if there exists some
i0 ∈ {1, . . . , p} such that, for p(µ) = Iµ(0),

p(0) = 0 and ∂p
∂µi0 (0) ̸= 0, (12)

5

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

which is guaranteed by conditions (9) and (10) , we can compute the quantity
η1 (0) using the formulas derived in section 6, that give expressions for the 1st
and 2nd order derivative of a transition map near a connection that is pre-
served by the perturbation. Indeed, under the conditions in (12) , there exists a
subfamily (Zε)ε , Zε = X(γ(ε),ε),

induced by a smooth curve µ = γ(ε), ε ↓ 0, in parameter space with γ(0) = 0
such that Zε has a 2-saddle cycle L (ε) for every ε > 0 suﬃciently small (see for
instance [11]). For ε = 0, L (0) = L and, if we denote the connections of L (ε)
by Γi (ε) such that α-limit of Γi (ε) for Zε is si, i = 1, 2, then Γi (0) = Γi, i =
1, 2. Denote the respective restrictions of the maps Ri
µ, ηi, i = 1, 2 to the curve
¯µ = γ (ε) by ̃Ri
ε, ̃ηi, i = 1, 2, we have

d
2 ˜R1
ε
dv2 (0) = 2ε˜η1(ε), and d
2 ˜R2
ε
du2 (0) = 2ε˜η2(ε);

in particular, since γ (0) = 0,

η1 (0) = ̃η1 (0) and η2 (0) = ̃η2 (0) .

3 Normal forms at hyperbolic saddles

In this section, we recall some useful normal forms for families of C ∞ vector ﬁelds
near a hyperbolic saddle, that will simplify the calculations of the quantities
η1 (0) and η2 (0) ; in particular, we give a speciﬁcation of the isochore Morse
lemma for a Hamiltonian unfolding in Theorem 10. Consider a C ∞ family of
planar vector ﬁelds (Xµ) with parameter values µ varying in some open set P
of Rp. Suppose that for some µ0 ∈ P, Xµ0 admits a hyperbolic saddle s, and
suppose that the Jordan normal form of DXµ0 (s) is given by
(
λ1 0
0 λ2
) ,

with λ2 < 0 < λ1. The ratio of hyperbolicity of Xµ0 at s is deﬁned by −λ2/λ1.
As an easy consequence of the implicit function theorem, one can suppose
that the saddle is persistant for all Xµ, µ ∈ P. By this we mean that there
exists a C ∞ function s : P ↦→ R2 such that each Xµ admits a hyperbolic saddle
at sµ := s(µ) with sµ0 = s.
The following theorem can be found in [15].

Theorem 5 Let (Xµ)µ∈P be a C ∞ family as above such that Xµ0 admits a
hyperbolic saddle s. Suppose that the ratio of hyperbolicity of Xµ0 at s is rational,
given by p/q with p, q ∈ N1, (p, q) = 1. Then for each N ∈ N, there exists a
neighbourhood PN of µ0 in parameter space such that the M –jet, M = N (p +
q) + 1, at sµ of each Xµ, µ ∈ PN , is locally C ∞-conjugate to:

˜X N
µ :
 



 ˙x = x(
λ1 + ∑N
i=0 ai(µ)(xpyq)i)
,

˙y = y(λ2 + ∑N
i=0 bi(µ)(xpyq)
i), (13)

6

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

where the coeﬃcients ai(µ) and bi(µ) are smooth in µ. In case the ratio of
hyperbolicity of Xµ0 at s is irrational, then for every N ∈ N, there exists a
neighbourhood PN of µ0 in parameter space such that the N –jet of Xµ, µ ∈ PN ,
is, locally near sµ, C ∞ linearisable.

Remark 6 1. The above theorem only applies to every ﬁnite jet of the family
of vector ﬁelds, while for an individual vector ﬁeld we have a normal form
for its inﬁnite jet at our disposal.

2. Using the theorem of Sternberg for families ([13]), it follows immediately
from the above theorem that, in case the ratio of hyperbolicity of Xµ0 at s
is rational, ∀k ∈ N, there exists some N (k) ≥ k such that the family (Xµ),
µ varying near µ0, is, locally near s, C k–conjugate to ˜X N (k)
µ .

In case of an individual integrable vector ﬁeld a further simpliﬁcation near
a hyperbolic saddle can be obtained by applying Morse’s lemma on the ﬁrst
integral H.

Proposition 7 Let X be an integrable vector ﬁeld with ﬁrst integral H and
admitting a hyperbolic saddle s. Denote by (u, v) the coordinates near s, given
by Morse’s lemma, in which H reads uv. Then, near s and expressed in the
coordinates (u, v), X reads: { ˙u = −u,

˙v = v, (14)

up to C ∞ equivalence and a possible coordinate change in (u, v).

Proof. Denote by Y , the vector ﬁeld, deﬁned locally near the origin, that
one obtains after expressing X in the coordinates (u, v). Because uv is a ﬁrst
integral of Y , it is clear that there exists a C ∞ function Y , with Y (0) ̸= 0, such
that Y1 = −uY and Y2 = vY . After a possible coordinate switch in (u, v), one
can always suppose that Y (0) > 0 implying the desired result.
We continue by describing another way to obtain the normal form (14), in
case X is a Hamiltonian vector ﬁeld. This method will ﬁrst reduce X to a formal
normal form (13) and can be useful when performing calculations in practice.
However, using this method, the normal form (14) is only obtained on each of
the half planes {u ≥ 0}, {u ≤ 0}, {v ≥ 0} or {v ≤ 0}, which will be suﬃcient
for our further practical use of it.
We notice that similar reductions of Morse functions are already obtained
in [12]. However these results were only valid near critical points that are not
saddle points. The method that we propose is based on the following proposi-
tion.

Proposition 8 Let X be an integrable vector ﬁeld with ﬁrst integral H : V ⊂
R2 → R that admits a hyperbolic saddle s. Suppose that there exist C ∞ coordi-
nates (u, v), near s, in which X reads:
{ ˙u = −u,

˙v = v, (15)

7

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

up to C ∞ equivalence. Then H, expressed in the coordinates (u, v), can be
written as a C ∞ function in uv, locally near the origin, on each of the half
planes {u ≥ 0}, {u ≤ 0}, {v ≥ 0} or {v ≤ 0}.

Proof. We prove the statement for H restricted to H = {u ≥ 0} ; in an anal-
ogous way the statement is obtained for the other half planes. The orbits of
system (15) are given by the curves {(0, 0)} ,

{(u, v) : uv = c, u > 0, v > 0} , {(u, v) : uv = c, u > 0, v < 0} , for c ̸= 0,

{(0, v) : v > 0} and {(0, v) : v < 0} .

Choose c0 such that (c0, 0) ∈ H ∩ V, then we deﬁne the map f as follows: for
c near zero, f (c) = H(c0, c
c0 ). By deﬁnition, the map f is C ∞. We now check

that f (uv) = H(u, v) on H and locally near the origin. As H is a ﬁrst integral
of system (15) on V, H stays constant on the orbits of (15) lying in H ∩ V .
Then for u > 0, this follows immediately from the deﬁnition of f. For u = 0,
we notice that the fact that f (0) = H(u1, 0), ∀u1 > 0, the continuity of H
implies H(0, 0) = f (0). Furthermore, because H stays constant on the positive
and negative v–axis, it follows that H(0, v) = H(0, 0), ∀v implying the required
result.

Proposition 9 For a Hamiltonian vector ﬁeld XH , with Hamiltonian H, given
by: 



 ˙x = − ∂H
∂y (x, y) ,

˙y = ∂H
∂x (x, y) , (16)

and admitting a hyperbolic saddle s, there exist C ∞ coordinates (u, v), near s,
in which the ∞–jet of XH reads:




 ˙u = −u
(λ + ∑

i≥1 ai(uv)i),

˙v = v(
λ + ∑
i≥1 ai(uv)
i), (17)

for some ai ∈ R, i ∈ N1.

Proof. Theorem 5 guarantees the existence of a C ∞ coordinate transformation
(x, y) = ϕ1(u, v) near s in which the ∞–jet of XH reads:




 ˙u = −u
(λ + ∑
i≥1 ai(uv)i),

˙v = v(
λ + ∑
i≥1 bi(uv)i), (18)

for some λ > 0, ai, bi ∈ R, i ∈ N1. We prove that the coeﬃcients ai and bi in (18)
coincide. It is easily veriﬁed that the coordinate transformation (x, y) = ϕ1(u, v)
transforms the Hamiltonian vector ﬁeld into:




 ˙u = − 1
det Dϕ1(u, v) ∂H ◦ ϕ1
∂v (u, v),

˙v = 1
det Dϕ1(u, v) ∂H ◦ ϕ1
∂u (u, v).
 (19)

8

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

On the other hand using Borel’s theorem on the realization of formal power
series, one ﬁnds smooth functions f and g such that

j∞f (0)(z) = ∑

i≥1 aizi, j∞g(0)(z) = ∑

i≥1 bizi.

In particular ϕ1 brings XH into




 ˙u = −u
(λ + f (uv)) + R(u, v),

˙v = v(λ + g(uv)
) + S(u, v), (20)

with j∞R(0) = j∞S(0) = 0. After a suitable near–identity transformation, one
can suppose that R = S = 0 [7]. Comparing (19) with (20), and abbreviating
det Dϕ1(u, v) as D(u, v) , one sees that

λ (u ∂D
∂u (u, v) − v ∂D
∂v (u, v)
) + u ∂D
∂u (u, v)f (uv) − v ∂D
∂v (u, v)g(uv)

+D(u, v)
(f (uv) − g(uv) + uv(f ′(uv) − g′(uv))) = 0.
 (21)

It is easily seen that ∀k ∈ N1, the 2k–jet at zero of the expression

u ∂D
∂u (u, v) − v ∂D
∂v (u, v) = 0,

does not contain terms in (uv)
i, i ≤ k. Therefore comparing terms in uv of the
2–jet at zero of (21), one sees immediately that a1 = b1. By comparing terms
in (uv)k in the 2k–jet at u = v = 0 of (21), one can proceed by induction on
k ≥ 1 to prove that ak = bk, ∀k ∈ N1.
The following theorem is a particular case of the ‘isochore Morse lemma’
proved by Colin de Verdi`eres (for C ∞ vector ﬁelds on Rn, n ∈ N) in [3]; however,
to keep the paper self-contained without being lengthy, we include here the
theorem and its proof for C ∞ vector ﬁelds on R2.

Theorem 10 Let XH be a Hamiltonian vector ﬁeld that admits a hyperbolic
saddle s at which the eigenvalues of DXH (s) are given by ±λ, λ > 0. Then
there exist C ∞ coordinate coordinates ϕ : C1 ⊂ R2 → R2, (x, y) = ϕ (n, m),
where C1 is a neighbourhood of s in R2 and a C ∞ function d : C2 ⊂ R → R,
where C2 is an open interval containing 0 ∈ R d (0) = 0, such that XH is
transformed, up to the C ∞–equivalence factor λ + d(nm), into




 ˙n = −n,

˙m = m, (22)

In particular, if H is one of the half planes {n ≥ 0}, {n ≤ 0}, {m ≥ 0} or {m ≤
0}, then ϕ can be chosen such that the Hamiltonian H (ϕ (n, m)) = nm on H and
the equivalence factor equals 1/ det Dϕ(n, m) = λ + d(nm) on H. Furthermore,
we can suppose that {n = 1} is contained inside of C1.

9

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Proof. From Proposition 9 and using Borel’s theorem on the realization of
formal power series, one ﬁnds a C ∞ coordinate change (x, y) = ϕ1(u, v) bringing
XH , near s, into: 



 ˙u = −u(λ + f (uv)) + R(u, v),

˙v = v(λ + f (uv)) + S(u, v), (23)

with f being smooth such that j∞f (0)(z) = ∑

i≥1 aizi and R and S being
ﬂat at zero, i.e. j∞R(0) = j∞S(0) = 0. Applying a suitable near–identity
transformation, one can suppose that the ﬂat terms R and S are zero [7], such
that the normal form of XH for C ∞ equivalence reads −u ∂
∂u + v ∂
∂v .
From Proposition 8, one knows that H, expressed in the new coordinates
(u, v), is a function in uv locally near the origin on each of the half planes
{u ≥ 0}, {u ≤ 0}, {v ≥ 0} or {v ≤ 0}. Suppose H(u, v) = uvH0(uv) on {u ≥ 0}
with H0(0) ̸= 0. After a reﬂection with respect to the u–axis, one can suppose
that H0(0) > 0. One performs the local transformation (n, m) = ϕ2(u, v), with

n = uG0(uv), m = vG0(uv), (24)

where G0(uv) = √
H0(uv). This transformation will leave the linear normal
form, up to C ∞ equivalence, invariant but will bring the Hamiltonian into nm
on the half plane {n ≥ 0}. In the new coordinates (n, m), XH reads:




 ˙n = − 1
det Dϕ(n, m) ∂H ◦ ϕ
∂m (n, m),

˙m = 1
det Dϕ(n, m) ∂H ◦ ϕ
∂n (n, m),

where ϕ = ϕ1 ◦ ϕ
−1
2 . On the other hand it is a straightforward calculation
to verify, using Proposition 8, that f (uv) can be written as a function d in
nm locally near the origin on the half plane {n ≥ 0}. Therefore applying the
transformation (24) on (23) (with R = S = 0), one ﬁnds:




 ˙n = −n(λ + d(nm)),

˙m = m(λ + d(nm)),

for some C ∞ function d with d(0) = 0 implying the result on {n ≥ 0}. The
same arguments can be used for obtaining the result on the half planes {n ≤ 0},
{m ≥ 0} or {m ≤ 0}. Furthermore, by performing a dilatation, we can obtain
that {n = 1} is contained inside of C1.

4 Transition maps

In this section we give formulas for the ﬁrst and second derivative of the tran-
sition map, based on Diliberto’s theorem.
Denote by X a C ∞ planar vector ﬁeld with ﬂow φ(t, v) := φt(v), v ∈ R2.
Take two sections Σ1 and Σ2 transverse to some regular orbit of X. Suppose
that ψi = (fi, gi) : Ii ⊂ R ↦→ Σi is a regular parametrization of Σi, for i = 1, 2.
Denote by T (s) the transition map of X from Σ1 to Σ2 expressed in the chosen

10

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

parameters s and s
′. In particular the orbit φt(ψ1(s)) crosses the section Σ2 at
the point ψ2(T (s)). Let the function τ (s) be the transition time function of X
from Σ1 to Σ2 expressed in the chosen parameter s; τ (s) is the time needed to
go from ψ1(s) to ψ2(T (s)).
Derivatives of the transition map and the transition time function can be
found by means of implicit diﬀerentiation of the expression:

θ(s, ˜s, τ (s)) = φτ (s)(ψ1(s)) − ψ2(˜s) = 0. (25)

Denoting for ﬁxed t, D2φ(t, v) as the diﬀerential of φ(t, v) with respect to v, we
ﬁnd

D2φ(τ (s), ψ1(s)) ψ′
1(s) + X(φτ (s)(ψ1(s)))τ ′(s) − ψ′
2(T (s))T ′(s) = 0. (26)

To ﬁnd the desired derivatives, we use Diliberto’s theorem [4] to decompose the
vectorial equation (26) with respect to an appropriate orthogonal basis. See also
[2], where formulas for T ′(s) and τ ′(s) are already obtained using Diliberto’s
theorem.
The scalar and wedge product between a vector ﬁeld X with Euclidean
coordinates (P, Q) and a vector ﬁeld X with Euclidean coordinates (P , Q) are
denoted as
 X · X = P P + QQ, and X ∧ X := P Q − QP .

Deﬁne the vector ﬁeld N := 1
∥ X ∥2 X ⊥,

multiple of the orthogonal vector ﬁeld:

X ⊥ = −Q ∂
∂x + P ∂
∂y ,

such that X ⊥ · N = 1. The following C ∞ functions are referred to as the curl,
the divergence and the curvature of X at p respectively:

curl X(p) = ∂Q
∂x (p) − ∂P
∂y (p), div X(p) = ∂P
∂x (p) + ∂Q
∂y (p),

and:
 κ(p) = 1
∥ X(p) ∥
 (N (p) · d
dt X(φt(p)) |t=0
). (27)

Theorem 11 (Diliberto [4]). Let X be a C ∞ planar vector ﬁeld with ﬂow
φt(v), v ∈ R2. Let p ∈ R2 with X(p) ̸= 0. For

w = αX(p) + βN (p)

the system: { ˙v = DX(φt(p))v,

v(0) = w (28)

has solution D2φ(t, p)w = A(t)X(φt(p)) + B(t)N (φt(p)),

11

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

where A(t) := A(t, X, p, w) and B(t) := B(t, X, p, w) are given by:

A(t) = α + ∫ t

0
 { 1
∥ X ∥2 [2κ ∥ X ∥ − curl X]} (φr(p)) B(r) dr, (29)

B(t) = β · exp (∫ t

0 div X(φr(p)) dr).

Theorem 12 Let X be a C ∞ vector ﬁeld. Consider the transition map T (s)
between two sections Σ1 and Σ2 transverse to the ﬂow of X. Suppose ψ1 and
ψ2 are regular parametrisations of these sections and Γs is the orbit starting at
ψ1(s) and ending in ψ2(T (s)). Let the quantities ∆i (s) , i = 1, 2, be deﬁned as:

∆i(s) := ∆(s, X, ψi) = X(ψi(s)) ∧ ψ′
i(s),

and
 σi(s) := σ(s, X, ψi) = ∆′
i(s)
∆i(s) − X(ψi(s)) · ψ′
i(s)
∥ X(ψi(s)) ∥2 div X(ψi(s)),

with i = 1, 2, the derivatives of ﬁrst and second order of T are given by:

T ′(s) = ∆1(s)
∆2(T (s)) exp ∫

Γs
 div X
∥ X ∥ ds , (30)

T ′′(s) = T ′(s)
(σ1(s) − T ′(s)σ2(T (s)) + ∆1(s) ∫

Γs
 A B
∥ X ∥3 ds )

where ds represents the arc length element of Γs and where A(z) := A(z, X)
and B(z) := B(z, X), z = (x, y) ∈ R2, are given by:

A(z) = D(div X)z(X ⊥(z)) − {(2κ ∥ X ∥ − curl X) div X}(z),

B(z) = exp ∫

Γs(z)
 div X
∥ X ∥ ds,
 (31)

with Γs(z) the orbit starting at ψ1(s) and ending in z.

Proof. To shorten notation during the proof let us denote ˜s = T (s). We
will decompose the vectorial equation (26) with respect to the orthogonal basis
{X, N } introduced in Theorem 11 to obtain formulas for T ′(s) and τ ′(s).
Decomposing ψ′
i(s) as

ψ′
i(s) = αi(s)X(ψi(s)) + βi(s)N (ψi(s)) (32)

with
 αi(s) = X(ψi(s)) · ψ′
i(s)
∥ X(ψi(s)) ∥2 , βi(s) = X(ψi(s)) ∧ ψ′
i(s),

it follows from Theorem 11 that

D2φ(t, ψ1(s))(ψ′
1(s)) = A(t)X(φt(ψ1(s)) + B(t)N (φt(ψ1(s))), (33)

12

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

where A(t) = A(t, X, ψ1(s), ψ′
1(s) and B(t) = B(t, X, ψ2(˜s), ψ′
1(s)) are deﬁned
as in Theorem 11. This leads to the following decomposition of formula (26):
(α2(˜s)T ′(s) − τ ′(s) − A(τ (s)))
X(ψ2(˜s))

+(β2(˜s)T ′(s) − B(τ (s)))N (ψ2(˜s)) = 0. (34)

In particular β2(˜s)T ′(s) − B(τ (s)) = 0 such that

T ′(s) = β1(s)
β2(˜s) exp ∫ τ (s)

0 div X(γs(t)) dt (35)

with γs(t) = φ(t, ψ1(s)). The ﬁrst formula in (30) follows.
Derivation of (35) gives

T ′′(s) = T ′(s)( β2(˜s)
β1(s) d
ds
 ( β1(s)
β2(˜s)
 ) + τ ′(s) div X(ψ2(˜s))

+ ∫ τ (s)

0
 d
ds
 ( div X(γs(t))
) dt)
.
 (36)

This formula can be simpliﬁed. To this end, we ﬁrst search for an expression
for d
ds div X(γs(t)). Because:

d
ds
 ( div X(γs(t))
) = D(div X)γs(t)(D2φ(t, ψ1(s))ψ′
1(s))

one ﬁnds, after substituting formula (33),

d
ds
 ( div X(γs(t))
) = A(t)D(div X)γs(t)(X(γs(t)))

+B(t)D(div X)γs(t)(N (γs(t))).
 (37)

Since D(div X)γs(t)(X(γs(t))) = d
dt div X(γs(t)) one can use the technique of
partial integration on the integral

∫ τ (s)

0 A(t)D(div X)γs(t)(X(γs(t))) dt.

Using (37) this yields

∫ τ (s)

0
 d
ds
 ( div X(γs(t))
)dt = [
A(t) div X(γs(t))]τ (s)

0 + I, (38)

where I is given by

∫ τ (s)

0 B(t) A(γs(t))
∥ X(γs(t)) ∥2 dt = β1(s) ∫

Γs
 A B
∥ X ∥3 ds,

13

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

with A and B deﬁned as in (31). Substituting (38) and τ ′(s) = α2(˜s)T ′(s) −
A(τ (s)) (that follows from (34)) into (36) and using:

β2(˜s)
β1(s) d
ds
 ( β1(s)
β2(˜s)
 ) = β′
1(s)
β1(s) − T ′(s) β′
2(˜s)
β2(˜s) ,

the formula of T ′′(s) follows.
The formulas in the following corollary can already be found in [5]. One
easily veriﬁes that they are a special case of the formulas stated in Theorem 12.

Corollary 13 Let X = P ∂
∂x + Q ∂
∂y be a C ∞ vector ﬁeld. Suppose Γ is an orbit
lying on the x-axis and Σi = {x = xi} are sections locally transverse to the ﬂow
of X at (xi, 0), i = 1, 2 and parametrised by y ↦→ (xi, y). Then the ﬁrst two
derivatives of the transition map T along Γ from Σ1 to Σ2 read:

T ′(0) = exp (∫ x2

x1
 Qy
P (x, 0)dx
),

T ′′(0) = T ′(0) ∫ x2

x1
 P Qyy − 2PyQy
P 2 (x, 0) exp (∫ x

x1
 Qy
P (u, 0)du
)dx.

5 Transition along a saddle–connection

In this section, using the general formulas obtained in section 4, we derive
formulas for the ﬁrst and second derivative of the transition map along a 2-
saddle connection, using normalizing coordinates near the saddles. In particular
we don’t restrict to individual vector ﬁelds but consider the transition near the
2-saddle connection in a family that leaves the saddle-connection unbroken.
We consider a C ∞ family of vector ﬁelds (Xµ)µ∈P with parameter values
µ varying in some subset P ⊂ Rp. We suppose that for µ0 ∈ P, the vector
ﬁeld Xµ0 admits a saddle-connection Γ, with α(Γ) = s1 and ω(Γ) = s2, s1
and s2 hyperbolic saddles of Xµ0. Let the vector ﬁeld (Xµ) be expressed in the
coordinates (x, y).
In particular we suppose that for µ near µ0, Xµ has two hyperbolic saddles
s1(µ) and s2(µ) lying in a neigbourhood of s1 respectively s2 such that si (µ0) =
si, i = 1, 2 and that there exists a saddle-connection Γµ between them that
coincides with Γ for µ = µ0.
Let i = 1, 2. Denote the eigenvalues of the linear part DXµ0 (si) at the
saddle si as λi and νi with νi < 0 < λi. Denote the ratio of hyperbolicity
by ri = − νi
λi . Denote the eigenvalues of DXµ(si(µ)) as λi(µ) and νi(µ) with
λi(µ0) = λi and νi(µ0) = νi. The corresponding ratio of hyperbolicity of si(µ)
is denoted as ri(µ) and ri(µ) = − νi(µ)
λi(µ) = ri + ˜ri(µ), for some C ∞ function ˜ri(µ)
with ˜ri(µ0) = 0.
Furthermore, we suppose that for µ near µ0, the connection stays unbroken.
This asumption is not restrictive by Remark 4.

Normalizing coordinates near the saddles. We suppose that (Xµ)µ∈P0
can be brought into a normal form at both saddles s1 and s2. The normal form
at si depends on the ratio of hyperbolicity ri (see Theorem 5). From now on,

14

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

(n, m) will denote the normalizing coordinates near s1 or s2 depending on which
saddle, s1 or s2, we are dealing with.
In case ri is given by pi/qi, pi, qi ∈ N1, (pi, qi) = 1, there exist some C k

(k ≥ 2) coordinates, near the saddle si, in which the family (Xµ)µ∈P0 reads:




 ˙n = n(λi(µ) + ai(µ)npimqi + Pi(npimqi, µ)),

˙m = m(νi(µ) + bi(µ)npim
qi + Qi(npim
qi, µ)), (39)

where Pi(z, µ) and Qi(z, µ) are polynomials in z = npim
qi of degree N (k) ≥ k
and of order O(z2). The functions λi, νi, ai and bi (respectively the polynomials
Pi and Qi) in (39) depend in a C ∞- (respectively C k-) way on the parameter µ.
On the other hand if the ratio of hyperbolicity ri of DXµ0(si) is irrational,
then (Xµ)µ∈P0 is C k linearisable near the saddle si. In particular there exists
some C k coordinates near the saddle si in which (Xµ)µ∈P0 reads:
{ ˙n = λi(µ) n,

˙m = νi(µ) m. (40)

The coordinate transformations expressing the coordinates (x, y) in function
of (n, m) are denoted as ϕ
1
µ and ϕ
2
µ near s1 and s2 respectively. We choose
normalizing coordinates near s1 (resp. s2) such that points on the positive n–
axis correspond to points on the unstable (resp. stable) separatrix of s1 (resp.
s2), lying on Γ for µ = µ0. This can always be achieved by performing a suitable
linear transformation in (n, m).
Let us denote the determinants of the corresponding jacobians of these trans-
formations as Ai
µ(n, m) := det Dϕ
i
µ(n, m), i = 1, 2. Further we also deﬁne

θi
µ(n, m) =
 ∂ϕi
µ
∂n (n, m). ∂ϕi
µ
∂m (n, m)

∥ ∂ϕi
µ
∂n (n, m) ∥2 . (41)

Remark that geometrically Ai
µ(n, m) represents the area of the paralellogram

spanned by the vectors ∂ϕ
i
µ
∂n (n, m) and ∂ϕi
µ
∂m (n, m). The angle between these two
vectors is strongly related to the function θi
µ(n, m).
Let us state the following lemma, which will be of use later on. It can be
applied near both saddles s1 and s2 inside the family (Xµ)µ∈P0.

Lemma 14 Suppose (Xµ) is a family of vector ﬁelds such that Xµ0 admits
a hyperbolic saddle s persisting as s(µ) for µ near µ0. Denote by (n, m) the
normalizing coordinates in which the family is, near s, expressed as the normal
form N µ = N 1
µ ∂
∂n + N 2
µ ∂
∂m in (39) or (40). Let (x, y) = ϕµ(n, m) be the
corresponding C k coordinate change. Denote by λ(µ) and ν(µ) the eigenvalues
of DXµ(s(µ)) with ν(µ) < 0 < λ(µ). Then

Xµ(ϕµ(n, m)) ∧ ∂ϕµ
∂m (n, m) = det Dϕµ(n, m)N 1
µ(n, m), (42)

and
 λ(µ) n Xµ(ϕµ(n, 0)). ∂ϕµ
∂m (n, 0)
∥ Xµ(ϕµ(n, 0)) ∥2 =
 ∂ϕµ
∂n (n, 0). ∂ϕµ
∂m (n, 0)

∥ ∂ϕµ
∂n (n, 0) ∥2 . (43)

15

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Proof. The identities (42) and (43) can easily be deduced from the identity

Xµ(ϕµ(n, m)) = Dϕµ(n, m)N µ(n, m). (44)

Expressing the transition using normalizing coordinates. Take a C k

normalizing coordinate transformation (x, y) = ϕ
i
µ(n, m) near s1 and s2 such
that the normalizing coordinates transform the family (Xµ) into (N i
µ) given by
(22) , and satisfy the properties of theorem 10. In these normalizing coordinates
(n, m) we choose sections Σ1
µ = {n = 1} and Σ
2
µ = {n = 1} near s1 and s2
respectively that are transverse to the ﬂow of the normal form (22) for (Xµ)µ∈P0 .
In a natural way we use the normalizing coordinate m to parametrise the section.
The transition map from Σ1
µ to Σ
2
µ expressed in the normalizing coordinate
m is denoted as Rµ(m). Remark that Rµ(m) is only deﬁned for m near zero
and µ near µ0. Calculating the derivatives of Rµ directly using Theorem 12 is
not possible. Indeed only a ﬁnite jet of ϕ
1
µ and ϕ
2
µ at (0, 0) can be calculated
implying that one is not able to calculate the derivatives of the parametrisations
of the sections Σ
i
µ, i = 1, 2. However this can be dealt with by using a limiting
process (see also [8]).
Take K0 > 0 and ε0 > 0 such that {(x, y) | 0 ≤ n < K0, −ε0 < m < ε0}
lies in the domains of ϕ
1
µ and ϕ
2
µ. For some 0 < K < K0 ﬁxed, consider the
section C i
µ,K = ϕ
i
µ({(K, m) | −ε0 < m < ε0}), parametrised by ϕi
µ |{n=K} :
m ↦→ ϕ
i
µ(K, m), i = 1, 2.
Consider the part of Γµ lying between the sections C 1
µ,K and C 2
µ,K, denoted
as Γµ,K, and write Z = T µ,K(Y ) as the transition map along Γµ,K from C 1
µ,K to
C 2
µ,K expressed in the parameter m. Further let Fµ,K (respectively Gµ,K) be the
transition maps from {n = 1} to {n = K} near s1 (respectively {n = K} to {n =
1} near s2), expressed using as parameter the normalizing coordinate m. Then
the transition map Rµ can be seen as the composition Rµ = Gµ,K ◦ T µ,K ◦ Fµ,K.
The ﬁrst two derivatives of Rµ at zero are now given by

R′
µ(0) = G
′
µ,K(0)T ′
µ,K(0)F ′
µ,K(0), (45)

and

R′′
µ(0) = G
′′
µ,K(0) (T ′
µ,K(0)
)2 (F ′
µ,K (0)
)2 + G
′
µ,K(0) T ′′
µ,K(0) (F ′
µ,K (0)
)2

+G
′
µ,K(0) T ′
µ,K(0) F ′′
µ,K(0). (46)
Because these equalities hold for every 0 < K < K0, one can switch over to the
limit for K → 0 causing the chosen sections C 1
µ,K and C 2
µ,K to tend arbitrarily
close to the saddles. This process will enable us to calculate the derivatives as
stated in the following theorem.

Theorem 15 Let (Xµ) be a C ∞ family admitting for each parameter two hy-
perbolic saddles s1(µ) and s2(µ) with a saddle–connection Γµ between them. Let
Rµ be the transition map from Σ1
µ to Σ2
µ along Γµ expressed using normalizing
coordinates. Consider the normal form at si, (39) or (40), and the correspond-
ing coordinate transformation ϕi
µ, i = 1, 2. Let Γµ,K be the part of Γµ starting

16

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

at ϕ
1
µ(K, 0) and ending in ϕ
2
µ(K, 0). Then one has

R′
µ(0) = A1
µ(0, 0) λ1(µ)
A2
µ(0, 0) λ2(µ) lim
K→0
 [
K r2(µ)−r1(µ) exp
 (∫

Γµ,K
 div Xµ
∥ Xµ ∥ d¯s

)]
 , (47)

where d¯s represents the arc length element of Γµ. Suppose that R′
µ(0) = 1, then

R′′
µ(0) = lim
K→0
 [ Uµ(K) + Iµ(K) + λ1(µ)K 1−r1(µ)A1
µ(K, 0) ∫

Γµ,K
 Aµ Bµ
∥ Xµ ∥3 d¯s
]
,

(48)
where Aµ(p) := A(p, Xµ), Bµ(p) := B(p, Xµ) are deﬁned as in Theorem 12 and
where Uµ(K) is the diﬀerence U 1
µ(K) − U 2
µ(K) with

U i
µ(K) := K −ri(µ)( ∂A
i
µ
∂y (K, 0)

Ai
µ(K, 0) − θi
µ(K, 0)
λi(µ)K div Xµ(ϕ
i
µ(K, 0))
), i = 1, 2.

The function Iµ(K) disappears for ri /∈ N. When ri ∈ N it is given by the
diﬀerence I 1
µ(K) − I 2
µ(K) with

I i
µ(K) := ai(µ)
λi(µ) K −˜ri(µ)−2 bi(µ) + ai(µ)ri(µ)
λi(µ) ω (K, ˜ri(µ)) , i = 1, 2,

where ω is the traditional compensator deﬁned by

ω (K, α) =
 



 K −α − 1
α for α ̸= 0

ln K for α = 0 . (49)

Remark 16 In expressions (47) , (48) as well as in (60) , some terms tend to
inﬁnity, but the limit value of the expression in the right-hand side exists and
is ﬁnite, since the limit of the left-hand term is well-deﬁned for K → 0 by deﬁ-
nition. In fact, in (47) for instance, the logarithm of the expression in between
the brackets [. . .] is given by

(r2(µ) − r1(µ)) ln K +
 (∫

Γµ,K
 div Xµ
∥ Xµ ∥ d¯s

)
 ;

since its limit for K → 0 is ﬁnite, the integral is divergent and its principal part
is given by − (r2(µ) − r1(µ)) ln K + o (1) , K → 0.

In fact, we are not interested in these principal parts but just in the ﬁnite quan-
tities which remain after subtracting these (non-interesting) principal terms. In
some sense, it is a question of method: we want to compute quantities which
are trivially known to be ﬁnite (R′
µ(0), R′′
µ(0), and next η1 (0) , η2 (0)) and the
method is to apply expressions which diverge in terms of a parameter K and to
retain some ﬁnite residue.

Proof. We will successively calculate all derivatives appearing in the right-hand
side of formula (45). Because the equality holds for all 0 < K < K0, one can
take the limit as K → 0 to ﬁnd the desired derivative R′
µ(0).

17

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

For calculating the derivatives F ′
µ,K(0) and G
′
µ,K(0), one can use the formu-
las of Corollary 13. One computes F ′
µ,K (0) = K −r1(µ) and G
′
µ,K (0) = K r2(µ)

such that R′
µ (0) = K r2(µ)−r1(µ) T ′
µ,K(0). (50)

The derivative T ′
µ,K(0) can be calculated using formula (30) in Theorem 12.
From Lemma 14, it easily follows that

T ′
µ,K(0) = A1
µ(K, 0) λ1(µ)
A2
µ(K, 0) λ2(µ) exp
 (∫

Γµ,K
 div Xµ
∥ Xµ ∥ d¯s

)

. (51)

One now substitutes (51) into (50) and takes the limit as K → 0. Because the
coordinate transformations ϕ1
µ and ϕ
2
µ are locally diﬀeomorphisms, Ai
µ, i = 1, 2
stays away from zero for K near 0 implying (47).
Assuming that R′
µ(0) = 1, i.e. G′
µ,K(0) T ′
µ,K(0) F ′
µ,K(0) = 1, equation (46)
simpliﬁes to
 R′′
µ(0) = G
′′
µ,K(0)
G′2
µ,K (0) + T ′′
µ,K(0)

T ′
µ,K(0) F ′
µ,K(0) + F ′′
µ,K(0)
F ′
µ,K(0) . (52)

Again we calculate all ingredients of the right-hand side in this identity after
which we let K tend to zero.
The term F ′
µ,K(0) (T ′′
µ,K(0)/T ′
µ,K(0)) in (52) can be computed by use of The-
orem 12. We deﬁne σ1
µ(K) := σ1(0, Xµ, ϕµ |v=K) and σ2
µ(K) := σ2(0, Xµ, ψµ |w=K
), where σ1 and σ2 are deﬁned as in Theorem 12. From equation (50) and the
assumptation that R′
µ(0) = 1, it follows that T ′
µ,K (0) = K r1(µ)−r2(µ). Because
F ′
µ,K (0) = K −r1(µ), one ﬁnds, using Lemma 14:

F ′
µ,K(0) T ′′
µ,K(0)

T ′
µ,K(0) = (
K −r1(µ)σ1
µ(K) − K −r2(µ))σ2
µ(K)+

+λ1(µ)K 1−r1(µ)A1
µ(K, 0)∫

Γµ,K
 Aµ Bµ
∥ Xµ ∥3 ds
).

The expressions for the functions σi
µ(K) can be simpliﬁed by applying Lemma
14. When r1 /∈ N, in particular when q1 > 1, we ﬁnd

σ1
µ(K) =
 ∂A1
µ
∂y (K, 0)

A1
µ(K, 0) − θ1
µ(K, 0)
λ1(µ)K div Xµ(ϕ1
µ(K, 0),

while in the case where r1 ∈ N, we ﬁnd

σ1
µ(K) =
 ∂A1
µ
∂y (K, 0)

A1
µ(K, 0) − θ1
µ(K, 0)
λ1(µ)K div Xµ(ϕ
1
µ(0, K) + a1(µ)
λ1(µ) K r1 .

Totally similar expressions are obtained for σ2
µ(K).
For the expression F ′′
µ,K(0)/F ′
µ,K(0) we use Corollary 13. One calculates
that for r1 /∈ N this quantity vanishes and that for r1 ∈ N:

F ′′
µ,K(0)
F ′
µ,K(0) = 2 b1(µ) + a1(µ)r1(µ)
λ1(µ)
 ∫ K

1 x−(1+˜r1(µ))dx. (53)

18

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Computations of the same sort also reveal an expression for G
′′
µ,K(0)/G′
µ,K(0)
when r2 ∈ N :
 G
′′
µ,K(0)
G′2
µ,K = −2 b2(µ) + a2(µ)r2(µ)
λ2(µ)
 ∫ K

1 x−(1+˜r2(µ)dx (54)

By (49) , the integrals in (53) and (54) are the compensators ω (K, 1 + ˜r1 (µ))
and ω (K, 1 + ˜r2 (µ)) respectively. Doing the obvious substitutions into (52) and
taking the limit as K → 0 yields the formula for R′′
µ(0) in (48).
Notice that in practice Theorem 15 can only be used when R′
µ(0) = 1,
which is true after a coordinate transformation ˜m = R′
µ(0)m in normalizing
coordinates near s1.

6 Regular transition maps near a Hamiltonian
2–saddle cycle

In this section, we apply the formulas obtained in the previous section on an
unfolding of a Hamiltonian vector ﬁeld.
Consider a family (Xµ) like in (1), µ varying near µ0 = (µ0, 0) with µ0 ∈ Rp,
and where XH has a saddle–connection Γ on which the Hamiltonian takes con-
stant value 0. Denote s1 and s2 as the hyperbolic saddles that are respectively
given by the α–limit and ω–limit of Γ. Assume that Γ persists in the family
(Xµ).

Appropriate normalizing coordinates near the saddles. Consider ﬁrst
the Hamiltonian vector ﬁeld XH near the saddles s1 and s2. Let i = 1 or i = 2.
Denote the eigenvalues of DXH (si) as ±λi, λi > 0. Theorem 10 guarantees the
existence of coordinates (n, m) in which XH , near si, reads:
{ ˙n = n,

˙m = −m, (55)

up to a non–zero factor E0
i (n, m) that equals −λi for n m = 0. Denote by ψi
0
the coordinate transformation expressing the old coordinates (x, y) in function
of the new ones (n, m). Let Hi denote a half plane that contains, in its interior,
the separatrices corresponding to the separatrices of si, that lie on L for ε = 0.
One can choose ψi
0 such that H expressed in the new coordinates reads n m on
Hi and such that E0
i (n, m) = −1/ det Dψi
0(n, m) on Hi.
Peforming, if necessary a coordinate switch or a reﬂection with respect to
the origin, one can suppose that points on the positive n–axes correspond to
points on Γ1 lying near s1 and s2 respectively; similar, This choice of coor-
dinates implies an orientation on the normalizing coordinate axes such that
det Dψ1
0(0, 0) = 1/λ1 and det Dψ2
0(0, 0) = −1/λ2. The half plane Hi can be
chosen such that in the new coordinates it will correspond to {n ≥ 0}.
We continue by peforming the transformation (x, y) = ψi
0(n, m) on the family
(Xµ) yielding: { ˙n = n + ε ˜fi(n, m, µ),

˙m = −m + ε˜gi(n, m, µ), (56)

19

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

up to the factor E0
i (n, m). Applying Theorem 5 yields C k transformations
(n, m) = (I + εφi
µ)(n, m) (i = 1, 2), near si and for µ near µ0, transforming (56)
into the normal form:




 ˙n = n(1 + ε(˜λi(µ) + ˜ai(µ)nm + Pi(nm, µ)
)),

˙m = −m
(1 + ε(˜νi(µ) − ˜bi(µ)nm − Qi(nm, µ)
)), (57)

where Pi(z, µ) and Qi(z, µ) are polynomials in z = nm of ﬁnite degree N (k) ≥ k
and of order O(z2).
Composing all the above performed transformations, one obtains C k trans-
formations (x, y) = ϕ1
µ(n, m) and (x, y) = ϕ
2
µ(n, m) near the saddles s1 and s2
respectively and for µ near µ0 bringing the family (Xµ) in (57) up to the factor
Ei(n, m, µ) = (E0
i ◦ (I + εφ
i
µ)
)(n, m), i = 1, 2.

Derivation of the transition along a Hamiltonian saddle–connection,
expressed using appropriate normalizing coordinates. As before, choose
transverse sections Σ
1
µ and Σ2
µ corresponding to {n = 1} in normalizing coordi-
nates near s1 and s2 respectively. Similar choose transverse sections Σ
2
µ and Σ4
µ
corresponding to {m = 1} in normalizing coordinates near s1 and s2 respectively.
The sections Σ
1
µ and Σ3
µ are parametrised using the normalizing coordinate m
while the normalizing coordinate n is used in order to parametrize the sections
Σ2
µ and Σ4
µ.
Consider the transition maps R1
µ(m) and R2
µ(n) from Σ1 to Σ3 and Σ2 to
Σ4 respectively, see Figure 2. We will derive formulas for the ﬁrst and second
derivative of Rµ := R1
µ at zero. Similar formulas for R2
µ can be deduced by
applying a coordinate switch in normalizing coordinates.
Because we have chosen the normalizing coordinates in such way that for
ε = 0 the Hamiltonian H reads nm in the normalizing coordinates near the
saddles on {n ≥ 0}, it is easily veriﬁed that Rµ = I + O(ε).
On the half plane {n ≥ 0}, one can deﬁne for i = 1, 2:

−Ei(n, m, µ) det (Dϕ
i
µ(n, m)) = 1 + εAi
µ(n, m) + O(ε2),

θi
0(n, m) =
 ∂ψi
0
∂n (n, m) · ∂ψi
0
∂m (n, m)

∥ ∂ψi
0
∂n (n, m) ∥2 .
 (58)

Further, we let ˜a
0
i (µ) = ˜ai(µ) |ε=0 and ˜b
0
i (µ) = ˜bi(µ) |ε=0. We can now state
the following proposition.

Proposition 17 Suppose (Xµ) is a perturbation of a Hamiltonian vector ﬁeld
as in (1), with µ varying in a neighbourhood of some (µ0, 0), µ0 ∈ Rp, such
that XH admits a saddle–connection Γ : H = 0, between two hyperbolic saddles
s1 and s2, that persists in the family (Xµ). Choose appropriate normalizing
coordinates (n, m) near the saddles in which (Xµ) reads as in (57) and consider
the functions θi
0 and Ai
µ deﬁned in (58) together with the coeﬃcients ˜a
0
i (µ) and
˜b0
i (µ).
Consider the transition map from Σ1
µ to Σ3
µ expressed in the appropriate
normalizing coordinates. Then we have

R′
µ(0) = 1 + O(ε). (59)

20

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Denoting ΓK as the part of Γ lying between ψ1
0(K, 0) and ψ2
0(K, 0) and fµ, gµ
as the restrictions of f and g to ε = 0, we have

R′′
µ(0) = ε lim
K→0
 [
α(µ) + δ(µ) ln K + U µ(K) − ∫

ΓK
 A
∥ XH ∥3 ds
] + O(ε2), (60)

where A(z) is deﬁned as

A(z) := D(div (fµ, gµ))z(X ⊥
H (z)) − {(2κ0 ∥ XH ∥ − curl XH ) div (f, g)
}(z),

with κ0(z) the curvature of XH at z, as deﬁned in (27), and where U µ(K) is
given by the diﬀerence U 1
µ(K) − U 2
µ(K) with

U i
µ(K) := 1
K
 ( ∂Ai
µ
∂m (K, 0) + θi
0(K, 0)
λi K div (f, g)(ψi
0(K, 0))
), i = 1, 2.

The coeﬃcient α(µ) is given by ˜a
0
1(µ) − ˜a
0
2(µ) and δ(µ) is given by δ1(µ) − δ2(µ)
with δi(µ) = 2(˜b0
i (µ) + ˜a
0
i (µ)).

Proof. We choose appropriate normalizing coordinates (n, m) near the saddles
as before and apply Theorem 15. In the normalizing coordinates, all transitions
occur in the half plane {n ≥ 0}, even in {n ≥ 0} ∩ {m ≥ 0}. So all calculations
in normalizing coordinates can be restricted to the half plane {n ≥ 0}.
Formula (59) is just the consequence of the fact that Rµ = I +O(ε). However
it can also be seen by applying the formula (47). Let us explain how formula
(60) follows from Theorem 15.
In the formulas of Lemma 14, we have to take the equivalence factors
Ei(n, m, µ) into account, i = 1, 2. Equation (42) stays valid up to this equiva-
lence factor:

Xµ(ϕi
µ(n, m)) ∧ ∂ϕ
i
µ
∂m (n, m) = Ei(n, m, µ) det Dϕ
i
µ(n, m)N 1
µ(n, m), (61)

for i = 1, 2 and where Nµ = N 1
µ ∂
∂n + N 2
µ ∂
∂m denotes the normal form (57) at
s1 or s2 depending near which saddle we apply the identity. Equation (43) is
translated into:

(1 + ε˜λi(µ)) nEi(n, 0, µ) Xµ(ϕ
i
µ(n, 0)). ∂ϕi
µ
∂m (n, 0)
∥ Xµ(ϕi
µ(n, 0)) ∥2 =
 ∂ϕi
µ
∂n (n, 0). ∂ϕi
µ
∂m (n, 0)

∥ ∂ϕi
µ
∂u (n, 0) ∥2 . (62)

Formula (61) implies that the area Ai
µ, in the proof of Theorem 15 is now
replaced by:
 Ai
µ = Ei(n, m, µ) det {Dϕ
i
µ(n, m)
}

= −(1 + εAi
µ(n, m) + O(ε2)), i = 1, 2.

Further, for ε = 0, formula (62) leads to

−λi n XH (ψi
0(n, 0)). ∂ψ0
∂m (n, 0)
∥ XH (ψi
0(n, 0)) ∥2 =
 ∂ψi
0
∂n (n, 0). ∂ψi
0
∂m (n, 0)

∥ ∂ψi
0
∂n (n, 0) ∥2 = θi
0(n, 0), (63)

21

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

such that θi
µ(n, 0) appearing in the formulas of Theorem 15 now equals θi
0(n, 0)+
O(ε), ε → 0.
Noticing that the divergence of Xµ reads div Xµ = ε div (f, g) + O(ε
2) and
referring to the normal form in (57), it should be clear for the reader that
formula (48) in Theorem 15 reduces to

R′′
µ(0) = εr1(K, µ) + ε
2r2(K, µ), (64)

where r1(K, µ) is the function given by

r1(K, µ) = α(µ) + δ(µ) ln K + Uµ(K) − ∫

ΓK
 A
∥ XH ∥3 ds,

with all appearing functions deﬁned as above.
Notice that the transformation ˜m = R′
µ(0)m in normalizing coordinates
leaves the equality (64) invariant up to order O(ε
2). Therefore, one can always
assume that the condition R′
µ(0) = 1 is satisﬁed such that it is justiﬁed to apply
formula (48) for obtaining a formula for R′′
µ(0) up to order O(ε2).
Because Rµ = I + O(ε), we can write:

R′′
µ(0) = εη(µ) + O(ε2), (65)

for some function η(µ), C ∞ dependent on µ. In particular comparing (64) with
(65), one sees r1(K, µ) = η(µ), for all 0 < K < K0, K0 near zero. This implies
η(µ) = limK→0 r1(K, µ), resulting in formula (60).

Formulas for calculating η1 and η2. Consider a family (Xµ) like in (1)
containing a period annulus bounded by a hyperbolic 2–saddle cycle L, see
Figure 1, that leaves the connection Γ2 unbroken. We choose H to be zero
on the 2–saddle cycle and strictly positive on the nearby closed orbits. In the
following corollaries, we obtain formulas for η1(µ, 0) (resp. η2(µ, 0)), deﬁned in
(7) (resp. (8)) in the case where one can ﬁnd a curve in parameter space passing
through (µ, 0) along which Γ1 persists.

Corollary 18 Suppose (Xµ) is a perturbation of a Hamiltonian vector ﬁeld
XH = X(µ0,0), containing a hyperbolic 2–saddle cycle L, that leaves the con-
nection Γ2 unbroken. Suppose there exists a curve µ = γ(ε) in parameter space
passing through (µ0, 0) along which the connection Γ1 stays unbroken. Choose
appropriate normalizing coordinates (n, m) near the saddles in which (Xµ) reads
as in (57) and consider the functions θi
0 and Ai
µ deﬁned in (58) together with
the coeﬃcients ˜a
0
i (µ) and ˜b0
i (µ). Let Γ
K
1 be the part of Γ1 lying between ψ1
0(K, 0)
and ψ2
0(K, 0). Denote fµ0 and gµ0 as the restrictions of f and g to µ = (µ0, 0)
respectively. Then the coeﬃcient η1(µ0, 0) as deﬁned in (7) reads

η1(µ0, 0) = lim
K→0
 [ α(µ0) + δ(µ0) ln K + V µ0 (K) − ∫

Γ1
K
 A
∥ XH ∥3 ds
]
, (66)

where A(z) is deﬁned as

A(z) := D(div (fµ0 , gµ0 ))z(X ⊥
H (z))−{(2κ0 ∥ XH ∥ − curl XH ) div (fµ0 , gµ0 )
}(z)

22

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

with κ0(z) the curvature of XH at z, deﬁned as in (27), and V µ0 (K) is given

by the diﬀerence V 1
µ0(K) − V 2
µ0(K) with:

V 1
µ0(K) := 1
K
 ( ∂A2
µ0
∂m (K, 0) − ∂A1
µ0
∂m (K, 0))
,

V 2
µ0(K) := 1
K
 ( θ1
0(K, 0)
λ1K div1 + θ2
0(K, 0)
λ2K div2
),

where divi := div (fµ0 , gµ0 )(ψi
0(K, 0)). The coeﬃcient α(µ0) is given by ˜a0
2(µ0)−
˜a
0
1(µ0) and δ(µ0) is given by δ2(µ0) − δ1(µ0) with δ0
i (µ0) = 2(˜b0
i (µ0) + ˜a
0
i (µ0)).

Proof. Applying Proposition 17 on the family (Zε) = (X(γ(ε),ε)), one easily
obtains formula (66).

Corollary 19 Suppose the same notations and considerations as in Corollary
18, and let Γ
K
2 be the part of Γ2 lying between ψ1
0(0, K) and ψ2
0(0, K). Then,
the coeﬃcient η2(µ0, 0) as deﬁned in (8) reads:

η2(µ0, 0) = lim
K→0
 [
β(µ0) + δ(µ0) ln K + ˜Vµ0(K) − ∫

Γ2
K
 A
∥ XH ∥3 ds]
, (67)

where A(z) is deﬁned as in Corollary 18 and ˜Vµ0(K) is given by the diﬀerence
˜V 2
µ0(K) − ˜V 1
µ0(K), with:

˜V 1
µ0 (K) := 1
K
 ( ∂A2
µ0
∂n (0, K) − ∂A1
µ0
∂n (0, K))
,

˜V 2
µ0 (K) := 1
K
 ( θ1
0(0, K)
λ1K div1 + θ2
0(0, K)
λ2K div2
)
,

where divi := div (fµ0, gµ0)(ψi
0(0, K)). The coeﬃcient β(µ0) is given by ˜b0
2(µ) −
˜b0
1(µ) and δ(µ0) is given by δ2(µ) − δ1(µ) with δ0
i (µ0) = 2(˜b
0
i (µ0) + ˜a
0
i (µ0)).

Proof. After a coordinate switch (n, m) ↦→ (m, n), we can apply Corrollary
18. The coeﬃcients in the normal form (57) switch roles and change sign, if we
want to keep the expression of (57) as it is. Because Γ2 runs from s1 to s2, the
roles of the saddles are interchanged compared with Corollary 18.

7 Unfolding a Hamiltonian 2–saddle cycle

In this section we verify that the unfolding (X(µ,ε)), (¯µ, ε) ∼ (0, 0) , of the Hamil-
tonian vector ﬁeld XH , deﬁned in (2) and (3) , satisﬁes the generic conditions
in the sense of Deﬁnition 2.
The phase portrait of XH contains four singularities: two centers at (0, ±2)
and two saddles given by s1 = (−1, 0) and s2 = (1, 0) where both saddles
have eigenvalues ±2 (cfr. Figure 3.). The singularities as well as the saddle-
connection between them lying on the x–axis, remain ﬁxed after perturbation.
The saddles and the saddle-connection on the x-axis are part of two 2–saddle
cycles, one lying in the half plane {y ≥ 0} and one lying in the half plane {y ≤ 0}.

23

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Both 2–saddle cycles lie inside {H = 0} ; as in the announcement of theorem 1,
we will only focus on the 2-saddle cycle that is contained in {H = 0} ∩ {y ≤ 0} ,
and call it by L. The non-isolated periodic orbits inside L, lie inside {H > 0} .

s1 s2
 Figure 3: Phase portrait of XH = X(µ,0).

The conditions concerning the Abelian integral. Suppose h ≥ 0 and
denote γh as one of the closed curves inside the annulus of which L is the
boundary. The Abelian integral is deﬁned as:

I (h, ¯µ) = ∫

γh f dy − gdx, (68)

with f (x, y, ¯µ, ε) and g(x, y, ¯µ, ε) the functions that appear after the parameter
ε in the expression of (Xµ), (2). We now check the conditions (9) and (10).
In what follows, we calculate the coeﬃcients in the expansion of I using
Picard-Fuchs equations; write

I(h, µ) = p(µ) + q(µ)h log h + r(µ)h + s(µ)h2 log h + O(h
2). (69)

The Abelian integral related to (2) is given by:

I(h, µ) = ∫

γh µ3xydy − (µ1 + µ2x)ydx

+ ∫

γh µ4y2xdy + y(x2 + 1
12 y2 − 1)
︸ ︷︷ ︸
=H(x,y)
 (x − √3π
8 yx)dy

= µ4 ∫
γh y2xdy + (µ3 − √3π
8 h
) ∫
γh xydy
+h ∫

γh xdy − µ1 ∫

γh ydx − µ2 ∫

γh xydx

or I(h, µ) = µ4I2(h) + (µ3 −
 √3π
8 h)I1(h) + (µ1 + h)I0(h), (70)

with Ik(h) = ∫
γh ykxdy. Now by direct computation, one easily veriﬁes that:

lim
h→0 I0(h) = −
√3π, lim
h→0 I1(h) = 8, lim
h→0 I2(h) = −3
√3π.

In particular the condition to have a 2–saddle cycle is given by:

I(0, µ) = −3√3πµ4 + 8µ3 − √3πµ1 = 0.

24

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

Referring to [6], the Picard–Fuchs equation is given by:

D(h) d
dh
 


I0
I1
I2


 =
 


 3
4 h
2 − 2 − 3
4 h 2
3
h 9
8 h
2 −h
− 3
2 h
2 −3h 3
2 h
2



 


I0
I1
I2


 , (71)

with D(h) = 9
8 h(h
2 − ( 4
3 )2). Writing:

I0(h) = −√3π + a1h + a2h log h + a3h2 log h + O(h
2),

I1(h) = 8 + b1h + b2h log h + b3h2 log h + O(h
2),

I2(h) = −3
√3π + c1h + c2h log h + c3h
2 log h + O(h
2),

and substituting in (71) gives:

a2 = −1, b1 = −√3π, b2 = 0, c1 = 12, c2 = 0.

We conclude that:

I0(h) = −√3π + a1h − h log h + a3h
2 + a4h
2 log h + O(h
2),
I1(h) = 8 − √3πh + b3h
2 + b4h
2 log h + O(h
2),
I2(h) = −3
√3π + 12h + c3h
2 + c4h
2 log h + O(h
2).

Using (70), the coeﬃcients in (69) are given by:

p(µ) = −3
√3πµ4 + 8µ3 − √3πµ1,

q(µ) = −µ1,

r(µ) = 12µ4 − √3πµ3 + a1µ1,

s(µ) = c4µ4 + b4µ3 + a4µ1 − 1,

So p(0) = q(0) = r(0) = 0, but s(0) ̸= 0. Moreover, since α1(µ) = 1
2 (µ1 − µ2),
it is easily seen that the map

µ ↦→ (p(µ), q(µ), r(µ), α1(µ)),

is a local diﬀeomorphism at zero.

Calculation of appropriate normalizing coordinates. By the calcula-
tions of the Abelian integral and the observations in remark 4, we can use for-
mulas (66) and (67) in order to calculate η2(0) as well as η1(0). Along {µ = 0}
the perturbation is zero on both connections of L, implying that the 2-saddle
cycle persist in the subfamily (Zε)ε , where

Zε = X(γ(ε),ε), where γ (ε) = 0, ∀ε ↓ 0.

In what follows, notations are kept the same as in Corollaries 18 and 19.
We calculate the appropriate normalizing coordinates near the saddles of the
subfamily (Xε) = (X(0,ε)). The unfolding (Xε) reads:

(Xε) :
 { ˙x = 1 − 1
4 y2 − x2 + εy(x2 + 1
12 y2 − 1)(x − √3π
8 xy),

˙y = 2xy
 25

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

with X0 = XH and H deﬁned in (3). It will appear to be suﬃcient to perform
normal form calculations up to order 4.
The Hamiltonian vector ﬁeld XH has two hyperbolic saddles, one at (−1, 0)
and one at (1, 0). Near (1, 0), we proceed as follows. We start with calculating
the 3–jet of (x, y) = ψ2
0(n, m), the coordinate change transforming XH into the
normal form (55) up to C ∞ equivalence. First, we translate the singularity to
the origin, yielding: { ˙x = −2x − 1
4 y2 − x2,

˙y = 2y + 2xy.

The linear part at the origin is already in its Jordan form. The transformation

(x, y) = (x + 1
4 x3 + 7
48 xy2, y + 1
4 x2y − 1
48 y3), (72)

will remove all terms of order less than 4. One concludes that the 3–jet of
X is C ω linearisable by the transformation given by the composition of the
translation (x, y) = (x + 1, y) with (72).
The Hamiltonian expressed in the new coordinates already reads 2xy up to
order 5. Therefore the transformation that brings the Hamiltonian in xy is up
to order 4 given by a dilatation that one can choose to be (x, y) = (x, y
2 ). After
a switch of the normalizing coordinates and a reﬂection (x, y) ↦→ (−x, −y), the
positive x and y–axis in normalizing coordinates correspond respectively to the
unstable and the stable separatrix of s2 lying on L. One obtains the following
3–jet of the transformation (x, y) = ψ2
0(n, m):

(x, y) = (1 − m + 1
2 m
2 − 1
96 n2 − 1
4 m3 − 7
192 n2m,

− 1
2 n − 1
2 n m − 1
8 n m
2 + 1
384 n3). (73)

The 3–jet of (Xε) is transformed into:
{ ˙n = n + 1
2 εn
2m,

˙m = −m − 1
2 εn m − ε √3
32 πn2m, (74)

up to a factor 2 + O(|n m|2).
Near s1 = (−1, 0), one can make use of the symmetry of XH with respect to
the y–axis. The Hamiltonian vector ﬁeld is invariant under the transformation

(x, y, t) ↦→ (−x, y, −t),

such that the behaviour of XH in the region {(x, y) | −1 < x < −1 + ε0} is
exactly given by the behaviour of −XH in the region {(x, y) | 1 − ε0 < x < 1}.
Choosing ψ1
0 := S ◦ ψ2
0, where S(x, y) = (−x, y), the 3–jet of (Xε) is near s1
transformed into: { ˙n = n − 1
2 εn
2m,

˙m = −m + 1
2 εn m + ε √3
32 πn2m, (75)

up to a factor −2 + O(|n m|
2). Moreover the Hamiltonian expressed in new
coordinates reads n m, up to order 5.
 26

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

One continues by performing a transformation of the form I + εϕ
i
ε, i = 1, 2
near s1 and s2 respectively, keeping the unperturbed vector ﬁeld unchanged but
removing non–resonant terms of order less than 4, appearing after the parameter
ε in expressions (74) and (75).
Performing the transformation

(n, m) = (n, m − ε( 1
2 nm +
 ( 1
8 ε −
 √3π
64
 )
 n2m)
),

one comes to the following normal form at s2 for the 3–jet of (Xε):
{ ˙n = n + 1
2 εn
2m,

˙m = −m, (76)

up to a factor 2 + O(|n m|2).
Analogously, performing the transformation

(n, m) = (n, m + ε( 1
2 nm +
 ( 1
8 ε +
 √3π
64
 )
 n2m)
),

the 3–jet of (75) will, locally near s1, be transformed into:
{ ˙n = n − 1
2 εn
2m,

˙m = −m, (77)

up to a factor −2 + O(|n m|2).

Calculation of η1(0) and η2(0). We use formulas (66) and (67) to calculate
η1(0) and η2(0). Using the above normal form calculations, one computes the
functions θi
0 and ¯Ai
0, i = 1, 2, deﬁned in (58) :

θ1
0(n, m) = θ2
0(n, m) = 13
12 x − 11
24 xy + O(∥ (x, y) ∥
3),

where x and y depend on (n, m) and:




 A1
0(n, m) = 1
2 n + 1
64 √3πn2 + O(∥ (n, m) ∥
3),

A2
0(n, m) = − 1
2 n − 1
64 √3πn
2 + O(∥ (n, m) ∥3),

together with:

div (f0, g0)(x, y) = 2xy(x −
 √3π
8 xy) + H(x, y)(1 −
 √3π
8 y), (78)

where f0 and g0 are the functions appearing after the parameter ε in the ex-
pression of (Xε). In particular, one gets:

div (f0, g0)(ψi
0(0, K)) = 0, i = 1, 2, ∀0 < K < K0,

27

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

such that ˜V 2
0 (K) = 0, for each K near zero, in formula (67). On the other hand,
the asymptotic behaviour of ˜V 1
0 (K) as K → 0 is given by:

˜V 1
0 (K) = − 1
K + O(K), K → 0.

One concludes that the function ˜V0(K) in (67) has the following asymptotic
behaviour as K → 0:
 ˜V0(K) = 1
K + O(K), K → 0. (79)

Furthermore, from (41), we have:

θ1
0(K, 0) = θ2
0(K, 0) = 13
12 K + O(K 3), K → 0

and, from (78),

div (f0, g0)(ψ1
0(K, 0)) = div (f0, g0)(ψ2
0(K, 0)) = −K + O(K 2), K → 0

such that the function V 2
0(K) in formula (66) is given by:

V 2
0(K) = − 13
24 + O(K), K → 0.

Furthermore, one easily gets

V 1
0(K) = O(K), K → 0

implying that V 0(K) in formula (66) is given by:

V 0(K) = 13
24 + O(K), K → 0. (80)

We are left with the calculations of the integrals appearing in the formulas (66)
and (67) of η1(0) and η2(0) respectively.
Consider the integral in formula (67), along the orbit Γ2 lying on the x–
axis. Parametrizing the orbit using the x–coordinate leads to an integral over
x ∈ [r1
1(0, K), r2
1(0, K)] with ψi
0 = (ri
1, ri
2) and K varying in ]0, K0[, K0 near
zero. A direct calculation yields the following primitive of the integrand:

F (x) := ln ( 1 − x
1 + x
 ) − x
x2 − 1 .

Because r1
1(0, K) = −r2
1(0, K) the integral equals:

∫

Γ2
K
 A
∥ XH ∥3 ds = −2 r2
1(0, K)
r2
1(0, K)2 − 1 + 2 ln ( 1 − r2
1(0, K)
1 + r2
1(0, K)
 ).

Using (73), one easily ﬁnds that

r2
1(0, K) = 1 − K + 1
2 K 2 + O(K 3), K → 0

28

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

yielding in ∫

Γ2
K
 A
∥ XH ∥3 ds = 1
K − 2 ln 2 + 2 ln K + O(K), K → 0. (81)

Consider now the integral along the connection Γ1 in formula (66),

Γ1 : x2 + 1
12 y2 − 1 = 0,

which can be parametrized by the x–coordinate yielding an integral over x ∈
[r2
1(K, 0), r1
1(K, 0)]. A direct calculation shows that

G(x) := x (√3π√3 − 3x2 − 4)

8 (1 + 11x2) − 3
4 π arcsin x + 1
2 ln ( 1 + x
1 − x
 ) .

is a primitive of the integrandum, where

g (x) = x (√3π√3 − 3x2 − 4)

8 (1 + 11x2) − 3
4 π arcsin x.

Thus, the integral equals G(−r2
1(K, 0)) − G(r2
1(K, 0)). Using (73), one sees

r2
1(K, 0) = 1 − K 2

96 + O(K 3), K → 0

such that the integral equals
∫

Γ1
K
 A
∥ XH ∥3 ds = 1
12 + 3
4 π2 + 2 ln K − ln 192 + o(1), K → 0. (82)

Substituting the obtained data (80) , (82) , (79) and (81) in the formulas (66)
and (67), one gets:

η1(0) = 13
12 + ln 192 + 3
4 π2 and η2(0) = 2 ln 2.

Clearly, these values fulﬁlled the necessary condition η2 (0) ̸= 2η1 (0) in (11) ,
we wanted to verify (see page 5).

Acknowledgement 20 M. Caubergh would like to thank the research group
‘Dynamical Systems’ of Hasselt University, of which she was part as postdoc-
toral fellow, when this work was initiated, for the research collaboration and the
ﬁnancial support by the tUL-impuls programme.

References

[1] M. Caubergh, F. Dumortier and R. Roussarie, Alien limit cycles
near a Hamiltonian 2-saddle cycle, Comptes Rendus Math´ematiques de
l’Acad´emie des Sciences, Vol. 340, no.8, 587–592, 2005.

[2] C. Chicone, Bifurcations of nonlinear oscillations and frequency entrain-
ment near resonance, Journal on Mathematical Analysis, Vol. 23, no.6,
1577–1608, 1992.
 29

Preprint submitted at DISCRETE AND CONTINUOUS DYNAMICAL SYSTEMS. The
ﬁnal publication is available at
http://www.aimsciences.org/journals/redirecting.jsp?paperID=4488

[3] Y. Colin de Verdi`ere and J. Vey, Le lemme de Morse Isochore, Topology,
no.4, 283–293, 1979.

[4] S.P. Diliberto, On Systems of ordinary diﬀerential equations, in contribu-
tions to the theory of nonlinear oscillations, Princeton University Press,
1950.

[5] F. Dumortier, A. Guzm´an and C. Rousseau, Finite Cyclicity of elementary
graphics surrounding a focus or center in quadratic systems, Qualitative
Theory of Dynamical Systems, Vol. 3, no.34, 123–154, 2002.

[6] F. Dumortier, C. Li and Z. Zhang, Unfolding of a quadratic integrable
system with two centers and two unbounded heteroclinic loops, Journal of
Diﬀerential Equations, Vol.139, no.1, 1–29, 1979.

[7] F. Dumortier, J. Llibre and J.C. Art´es, Qualitative Theory of Planar Dif-
ferential Systems, Springer-Verlag, 2006.

[8] F. Dumortier, M. El Morsalani and C. Rousseau, Hilbert’s 16th Problem
for Quadratic Systems and Cyclicity of Elementary Graphics, Nonlinearity,
Vol. 9, no.5, 1209–1261, 1996.

[9] F. Dumortier and R. Roussarie, Abelian Integrals and limit cycles, Journal
of Diﬀerential Equations, 116–165, 2004.

[10] J.P. Fran¸coise, Singularit´es de champs isochores, Duke Math. Journal, Vol.
47, no.3, 465–485, 1980.

[11] J. Guckenheimer and P. Holmes, Nonlinear oscillations, dynamical systems
and bifurcations of vector ﬁelds, Springer-Verlag, 1983.

[12] V. Guillemin, Band asymptotics in two dimensions, Advances in Mathe-
matics, Vol. 42, 248–282, 1981.

[13] Yu. S. Il’yashenko and S. Yu. Yakovenko, Finitely smooth normal forms of
local families of diﬀeomorphisms and vector ﬁelds, Russian Math. Surveys,
Vol. 46, no.1, 1–43, 1991.

[14] P. Mardesic, Chebychev systems and the versal unfolding of the cusps of
order n, Travaux en cours, no. 57, Hermann, Paris, 1998.

[15] R. Roussarie, On the number of limit cycles which appear by perturbation
of separatrix loop of planar vector ﬁelds, Bol. Soc. Brasil. Mat., Vol. 17,
No. 2, 67–101, 1986.
 30
