<!-- source: https://ddd.uab.cat/pub/pubmat/pubmat_a1995v39n2/pubmat_a1995v39n2p355.pdf | converted from PDF -->

Publicacions Matem`atiques, Vol 39 (1995), 355–366.

ABELIAN INTEGRALS OF
QUADRATIC HAMILTONIAN VECTOR FIELDS
WITH AN INVARIANT STRAIGHT LINE*

Chengzhi Li, Jaume Llibre and Zhifen Zhang

Abstract
 We prove that the lowest upper bound for the number of isolated
zeros of the Abelian integrals associated to quadratic Hamiltonian
vector ﬁelds having a center and an invariant straight line after
quadratic perturbations is one.

1. Introduction

Let H(x, y) be a real polynomial of degree n + 1, and let P (x, y) and
Q(x, y) be real polynomials of degree at most m. The problem of ﬁnding
an upper bound N (n, m) for the number of isolated zeros of the Abelian
integrals

(1.1) I(h)= ∫

Γh Q(x, y) dx − P (x, y) dy,

where Γh varies in the compact components of H −1(h) is called the
weakened 16th Hilbert problem. It was posed by Arnold in [1].
The weakened 16th Hilbert problem is closely related to the problem
of determinating an upper bound for the number of limit cycles of the
perturbed Hamiltonian system

(1.2)ε
 dx
dt = ∂H
∂y + εP (x, y),

dy
dt = − ∂H
∂x + εQ(x, y),

*The authors are partially supported by DGICYT grants, the ﬁrst and third au-
thors are also partically supported by NSF of China, the second one is also partially
supported by a CIRIT grant.

356 C. Li, J. Llibre, Z. Zhang

where 0 < |ε| << 1. The relationship between both problems comes from
the following two facts:

(1) If I(h∗)=0 and I ∗(h∗) ̸= 0, then there exists a hyperbolic limit
cycle Lh∗ of system (1.2)ε such that Lh∗ → Γh∗ as ε → 0; and conversely,
if there exists a hyperbolic limit cycle Lh∗ of system (1.2)ε such that
Lh∗ → Γh∗ as ε → 0, then I(h∗)=0.

(2) The total number of isolated zeros of (1.1) (taking into account
their multiplicity) is an upper bound for the number of limit cycles of
system (1.2)ε tending to some periodic orbit Γh of system (1.2)ε=0 when
ε → 0.

Khovansky [16] and Varchenko [24] proved independently that
N (n, m) is ﬁnite, but an explicit expression for N (n, m) is unknown.
Many authors have contributed to estimate the number N (n, m) for some
values of n and m, and for some classes of polynomial functions H(x, y),
see for instance Bogdanov [3] and [4], Petrov [20] and [21], Cushman
and Sanders [10], Dumortier, Roussarie and Sotomayor [13], Drachman,
van Gils and Zhang [12], Li and Rousseau [18], Gavrilov and Horozov
[14], Li, Llibre and Zhang [17], ...

A quadratic Hamiltonian vector ﬁeld is a vector ﬁeld of the form
(∂H/∂y, −∂H/∂x) where H = H(x, y) is a real polynomial of degree 3.

Our main result is to showthat N (2, 2) = 1 for the quadratic pertur-
bations of the quadratic Hamiltonian vector ﬁelds having an invariant
straight line under the ﬂowdeﬁned by the vector ﬁeld. This result is
proved in Section 2. In Section 3 we characterize the phase portraits of
the quadratic Hamiltonian vector ﬁelds having an invariant straight line,
we will see that there are six of such phase portaits.

We want to thank to Armengol Gasull his comments on a preliminary
version of this paper.

2. Statement of the main results

Let (∂H/∂y, −∂H/∂x) be a quadratic Hamiltonian vector ﬁeld, as
usual we say that
 dx
dy = ∂H
∂y , dy
dt = − ∂H
∂x ,

Abelian integrals of quadratic hamiltonian v. f. 357

is its associated quadratic Hamiltonian system, and vice versa. For ab-
breviation we denote by QH the class of quadratic Hamiltonian systems
having a center and an invariant straight line.

Lemma 1. Every system in QH can be reduced to another system in
QH of the form

(2.1)
 dx
dt = ∂H
∂y =2xy,

dy
dt = − ∂H
∂x = −y2 + f (x),

where f (x) is a polynomial of degree 2.

Proof: Let

(2.2) dx
dt = ∂H1
∂y , dy
dt = − ∂H1
∂x ,

be a system in QH. By a translation we can put the origin of coordinates
on the invariant straight line of system (2.2). Then by a rotation we
can transform the invariant straight line of system (2.2) in the y-axis.
Since both transformations are canonical, they preserve the Hamiltonian
structure of the system, and clearly they do not increase the degree of
the Hamiltonian function. Thus system (2.2) can be written in the form

(2.3)
 dx
dt = ∂H2
∂y = x(ax + by + c),

dy
dt = − ∂H2
∂x .

Notice that b ̸= 0; otherwise ˙x = x(ax+c), and consequently system (2.3)
would not have periodic orbits.
Nowconsider the change of variables

(2.4) x = x, by = ax + by + c.

Clearly
 det ( ∂(x, y)
∂(x, y)
 ) =1,

358 C. Li, J. Llibre, Z. Zhang

and the transformation (2.4) is canonical. For simplicity rewriting (x, y)
instead of (x, y) in system (2.3) after doing the change of variables (2.4),
we get

(2.5)
 dx
dt = ∂H3
∂y = bxy,

dy
dt = − ∂H3
∂x .

Since system (2.5) belongs to QH, it follows that

dx
dt = ∂H3
∂y = bxy,

dy
dt = − ∂H3
∂x = − b
2 y2 + g(x),

where g(x) is a polynomial of degree 2. Nowrescaling the variable y
from y to 2y/b, the lemma follows.

Notice that system (2.1) is invariant under the symmetry (x, y, t) ↦→
(x, −y, −t) and that it has x = 0 as an invariant straight line.
Nowwe present two preliminary results on the Abelian integrals I(h)
(see Section 1). These results will allow us to simplify the quadratic
perturbation of a system in QH. They are well-known but since we
cannot ﬁnd any reference for them, we prove them here.

Proposition 2. The following equality holds

I(h)= ∫

Γh
 (Q(x, y)+ ∫ ∂P (x, y)
∂x dy) dx.

Proof: From Stokes theorem we get
∫

Γh
 [
P (x, y) dy + (∫ ∂P (x, y)
∂x dy) dx]

= ∫

lnt(Γh)
 [ ∂P (x, y)
∂x dx ∧ dy + ∂
∂y
 (∫ ∂P (x, y)
∂x dy) dy ∧ dx]

= ∫

lnt(Γh)
 ( ∂P (x, y)
∂x − ∂P (x, y)
∂x
 ) dx ∧ dy

=0.

Then from (1.1) the propesition follows.

From Proposition 2 it follows immediately.

Abelian integrals of quadratic hamiltonian v. f. 359

Corollary 3. The Abelian integral I(h) associated to the system

dx
dt = ∂H
∂y ,

dy
dt = − ∂H
∂x + ε (Q(x, y)+ ∫ ∂P (x, y)
∂x dy) ,

is identical to the Abelian integral associated to system (1.2).

From Proposition 2 and Corollary 3 we get easily the following result.

Corollary 4. Assume that the perturbation (P, Q) of system (1.2)ε=0
is of degree 2. Then the Abelian integral I(h) associated to system (1.2)ε
is identical to the Abelian integral associated to the following system

dx
dt = ∂H
∂y ,

dy
dt = − ∂H
∂x + ε(µ1y + µ2xy + µ3y2).

Nowwe will apply Corollary 4 to a system in QH.

Lemma 5. Every system in QH after a quadratic perturbation has
the same Abelian integral that the following perturbed system of QH:

(2.6)
 dx
dt = ∂H
∂y =2xy,

dy
dt = − ∂H
∂x = −y2 + f (x)+ µ1y + µ2xy,

where f (x) is a polynomial of degree 2.

Proof: By Lemma 1 every system in QH can be transformed in the
form (2.1) with Hamiltonian function

(2.7) H(x, y)= x(y2 + F (x)),

where F (x) is a polynomial of degree 2 such that minus the derivative
of xF (x) is equal to f (x). From Corollary 4 the Abelian integral of a
Hamiltonian system (2.1) with an arbitrary quadratic perturbation is
the same that the Abelian integral of the system:

(2.8)
 dx
dt =2xy,

dy
dt = −y2 + f (x)+ µ1y + µ2xy + µ3y2.

360 C. Li, J. Llibre, Z. Zhang

Since for a periodic orbit Γh of the Hamiltonian system we have Γh ∩
{x =0} = ∅, it follows from (2.7) that

∫

Γh y2 dx = ∫

Γh
 ( h
x − F (x)
) dx =0.

So the Abelian integral of system (2.8) is the same that the Abelian
integral of system (2.6).

Notice that system (2.6) only depends on two parameters.

Nowwe state our main result.

Theorem 6. We have that N (2, 2) = 1 for the quadratic perturbation
of quadratic Hamiltonian vector ﬁelds having an invariant straight line.

Proof: We denote by
 Ii(h)= ∫

Γh x
iydx

for i =0, 1. Then, from Lemma 5, the Abelian integral for the quadratic
perturbation of a system in QH is

I(h)= µ1I0(h)+ µ2I1(h),

where h ∈ (h0,h1), and h0 and h1 corespond to some equilibrium point
and some homoclinic or heteroclinic loop of the phase partrait of the
Hamiltonian system
 dx
dt = ∂H
∂y =2xy,

dx
dt = − ∂H
∂x = −y2 + f (x),

in the Poincar´e disc.

Since (2.6) is a quadratic system having an invariant straight line, by
the properties of quadratic systems (see [5], [6], [15], [25], [21], [8] and
[9]), system (2.6) has at most one limit cycle, and if it exists then it is
hyperbolic. So I(h) can have at most one zero. Hence, N (2, 2) = 1.

Abelian integrals of quadratic hamiltonian v. f. 361

The number of isolated zeros of the Abelian integral (1.1) associated
to quadratic perturbations of a system in QH, and the number of limit
cycles of the perturbed system in general is not the same. It may ex-
ist limit cycles of the perturbed system such that when the quadratic
perturbation goes to zero they tend to the equilibrium point (the center
for the system in QH) or to the homoclinic or heteroclinic loop forming
the boundary of the center in the Poincar´e disc. Both possibilities has
been conﬁrmed by Zoladek in [26] and [27]. Hence, in order to obtain
all the limit cycles which can be bifurcated from a center it is necessary
to study simultaneously three cases. The ﬁrst one is to control the num-
ber of limit cycles which can be bifurcated from the equilibrium point,
secondly those which can be bifurcated from periodic orbits of the center
(for instance, through Abelian integrals), and ﬁnally those which can be
bifurcated from the homoclinic or heteroclinic loop at the boundary of
the center. For more details see [4], [19], [18] and [22].

3. Classiﬁcation of the System in QH

We shall use the classiﬁcation of all the phase portraits of quadratic
Hamiltonian vector ﬁelds given by Artes and Llibre in [2] to characterize
the phase portraits of the systems in QH, i.e. the phase portraits of the
quadratic Hamiltonian vector ﬁelds having an invariant straight line and
at least one center.
By Lemma 1 every system in QH can be transformed to a system

(3.1) dx
dt = ∂H
∂y , dy
dt = − ∂H
∂x ,

with H(x, y)= x(y2 + ax
2 + bx + c). In order to classify the phase
portrarits of system (3.1) in QH we distinguish three main cases.

Case 1. a =0. If b = 0 then system (3.1) has no center. So we assume
that b ̸= 0. After rescaling the variable x the parameter b can be reduced
to 1. Therefore H(x, y)= x(y2+x+c) = 0 has two branches, the straight
line x = 0 and the parabola y2 + x + c =0. If c ≥ 0 then system (3.1) has
no centers. So we assume c< 0. Then the two branches of H(x, y)=0
intersect at two saddle points of system (3.1). The other singular point
(−c/2, 0) of system (3.1) is a center. Hence, from [2], system (3.1) has
the phase portrait of type Vulpe 5 (see Figure 1).

Case 2: a> 0. After rescaling the variable x the parameter a can be
taken equal to 1. So H(x, y)= x[y2 +(x + b/2)
2 + c − b2/4].
Subcase 1. c − b2/4 < 0 . Then H(x, y) = 0 has two branches, the
straight line x = 0 and the circle centered at the point (−b/2, 0) with

362 C. Li, J. Llibre, Z. Zhang

radius equal to √b2/4 − c.If c< 0 then both branches intersect at two
saddles of system (3.1). Therefore, from [2], system (3.1) has the phase
portrait of type Valpe 3 (see Figure 1). If c = 0 the straight line x =0
is tangent to the cercle y2 +(x + b/2)
2 = b2/4, and from [2] system (3.1)
has the phare partrait of type Vulpe 2 (see Figure 1). If c> 0 the two
branches of H(x, y) = 0 do not intersect, then from [2] system (3.1) has
the phase portrait of type Vulpe 2 (see Figure 1).

Subcase 2. c − b2/4 ≥ 0. Then H(x, y) = 0 has a unique branch,
the straight line x =0. If b2 − 3c ≤ 0 then system (3.1) has no centers.
Therefore we assume b2 − 3c> 0. Nowsystem (3.1) has exactly two
singular points of coordinates ((−b ± √b2 − 3c)/3, 0), a center and a
saddle. Therefore, from [2] the phase portrait of system (3.1) is of type
Vulpe 2 (see Figure 1).

Case 3. a< 0. After rescaling the variable x the parameter a can be
taken equal to −1. So H(x, y)= x[y2 − (x − b/2)
2 + c + b2/4].

Subcase 1. c + b2/4=0. Then H(x, y) = 0 has three branches, the
straight lines x =0,y = x − b/2 and y = x + b/2. Each two of them
intersects at a saddle. Therefore, from [2], system (3.1) has the phase
portrait of type Vulpe 10 (see Figure 1).

Subcase 2. c + b2/4 ̸= 0. Then H(x, y) = 0 has three branches, the
straight line x = 0 and the two branches of the hyperbola y2−(x−b/2)
2 =
−(c+b2/4). If b2+3c ≤ 0 then system (3.1) has no centers. So we assume
that b2 +3c> 0. If c + b2/4 < 0 then x = 0 intersects the two branches
of the hyperbola, at two saddles. Therefore, from [2] it follows that
system (3.1) has the phase portrait of type Vulpe 9 (see Figure 1). If
c + b2/4 > 0 then x = 0 intersects only one branch of the hyperbola, at
two saddles. Hence, from [2], system (3.1) has the phase portrait of type
Vulpe 8 (see Figure 1).

Thus we have obtained six diﬀerent topological phase portraits for the
systems in QH. We remark that the unique of these six phase portraits
which can be realized for a quadratic Hamiltonian system without having
an invariant straight line is the phase portrait of Vulpe 2. This is due
to the property that if a quadratic system has an orbit with α-limit
one saddle and ω-limit another saddle, then this orbit is contained in
an invariant straight line. This result is due to Dong [11], see also Ye
Yanqian and others [25]. An improvement of this result is due to Chicone
and Shafer, see Theorem 2.8 of [7].

We also remark that Vulpe 2 without invariant straight line is re-
lated with the Bogdanov-Takens bifurcation restricted to quadratic vec-
tor ﬁelds.

Abelian integrals of quadratic hamiltonian v. f. 363

a =0
 Vulpe 5

c − b2/4 < 0, c< 0

Vulpe 3
 c − b2/4 < 0, c =0

Vulpe 2
 c − b2/4 < 0, c> 0

Vulpe 2

a> 0

c + b2/4=0

Vulpe 10
 c + b2/4 < 0

Vulpe 9
 c + b2/4 > 0

Vulpe 8

a< 0
 Figure 1: The six diﬀerent topological phase portraits of
the quadratic Hamiltonian vector ﬁelds having
an invariant straight line and at least one center.

364 C. Li, J. Llibre, Z. Zhang

References

1. V. I. Arnold, Loss of stability of self-oscillation close to resonance
and versal deformations of equivariant vector ﬁelds, Funct. Anal.
Appl. 11 (1977), 1–10.
2. J. C. Art´es and J. Llibre, Quadratic Hamiltonian vector ﬁelds,
J. Diﬀ. Equations 107 (1994), 80–95.
3. R. I. Bogdanov, Bifurcation of the limit cycle of a family of a
planar vector ﬁelds, Selecta Math. Soviet 1 (1981), 373–387.
4. R. I. Bogdanov, Versal deformation of a singularity of a vector
ﬁeld on the plane in the case of zero eigenvalues, Selecta Math.
Soviet 1 (1981), 389–421.
5. L. A. Cherkas and L. I. Zhilevich, Some criteria for the absence
of limit cycles and for the existence of a single limit cycle, Diﬀ.
Equations 6 (1970), 891–897.
6. L. A. Cherkas and L. I. Zhilevich, Limit cycles of some diﬀer-
ential equations, Diﬀ. Equations 8 (1972), 924–929.
7. C. Chicone and D. S. Shafer, Separatrix and limit cycles of
quadratic systems and Dulac’s theorem, Trans. Amer. Math. Soc.
278 (1983), 585–612.
8. B. Coll and J. Llibre, Limit cycles for a quadratic system with
an invariant straight line and some evolution of phase portraits, Col-
loquia Mathematica Societatis J´anos Bolyai 53, Qualitative Theory
of Diﬀerential Equations, Bolyai Institut, Szeged, Hungary (1988),
111–123.
9. W. A. Coppel, Some quadratic systems with at most one limit
cycle, Dynamics Reported 2 (1989), 61–88.
10. R. Cushman and J. A. Sanders, A codimension two bifurcation
with a third order Picard-Fuchs equation, J. Diﬀ. Equations 59
(1985), 243–256.
11. D. Jinzhu, The structure of the separatrix cycles of the system
˙x = ∑

0≤i+k≤2 aikx
i yk,˙y = ∑

0≤i+k≤2 bikx
iyk (in Chinese), Acta Math.

Sinica 12 (1962), 251–257.
12. B. Drachman, S. A. van Gils and Z. F. Zhang, Abelian inte-
grals for quadratic vector ﬁelds, J. Reine Angew. Math. 382 (1987),
165–180.
13. F. Dumortier, R. Roussarie and J. Sotomayor, Generic 3-pa-
rameter families of vector ﬁelds on the plane, unfolding a singularity

Abelian integrals of quadratic hamiltonian v. f. 365

with nilpotent linear part, The cusp case, Ergod. Th. & Dyn. Sys.
7 (1987), 375–413.

14. L. Gavrilov and E. Horozov,“Limit cycles and zero of Abelian
integrals satisfying third order Picand-Fuchs equations,” Lect. Notes
in Math. 1455, Springer-Verlag, 1990, pp. 160–196.

15. G. Naidan and C. Lansun,“Theory of limit cycles,” by Ye Yan-
qian and others, Transl. of Math. Monographs 66, Amer. Math.
Soc., 1984, pp. 336, 359–360.

16. A. G. Khovansky, Real analytic manifolds with ﬁniteness proper-
ties and complex Abelian integrals, Funct. Anal. Appl. 18 (1984),
119–128.

17. C. Li, J. Llibre and Z. F. Zhang, Weak focus, limit cycles and
bifurcations for bounded quadratic systems, J. Diﬀ. Equations 115
(1995), 193–223.

18. C. Li and C. Rousseau, A system with three limit cycles appear-
ing in a Hopf bifurcation and dying in a homoclinic bifurcation: The
cusp of order 4, J. Diﬀ. Equations 79 (1989), 132–161.

19. P. Mardesic, The number of limit cycles of polynomial deforma-
tions of a Hamiltonian vector ﬁeld, Ergod. Th. & Dynam. Sys. 10
(1990), 523–529.

20. G. S. Petrov, Number of zeros of complete elliptic integrals, Funct.
Anal. Appl. 18 (1984), 148–150.

21. G. S. Petrov, Elliptic integrals and their nonoscillations, Funct.
Anal. Appl. 20 (1986), 37–40.

22. G. S. Petrov, The Chebyshev property of elliptic integrals, Funct.
Anal. Appl. 22 (1988), 72–73.

23. G. S. Rychkov, Limit cycles of the equation u(x +1) du =
(−x+ax
2 +bxu +cu +du2) dx, Diﬀ. Equations 8 (1972), 1748–1750.

24. A. N. Varchenko, Estimate of the number of zeros of an Abelian
integral depending on a parameter and limit cycles, Funct. Anal.
Appl. 18 (1984), 98–108.

25. Y. Yanqian and others,“Theory of Limit cycle,” Tranl. of Math.
Monographs 66, Amer. Math. Soc., 1984.

366 C. Li, J. Llibre, Z. Zhang

26. H. Zoladek, Quadratic systems with center and their perturba-
tions, preprint (1992).
27. H. Zoladek, The cyclicity of triangles in quadratic systems,
preprint (1992).

Chengzhi Li:
Department of Mathematics
Beijing University
Beijing 100871
PEOPLES REPUBLIC OF CHINA
 Jaume Llibre:
Departament de Matem`atiques
Universitat Aut`onoma de Barcelona
08193 Bellaterra (Barcelona)
SPAIN

Zhi-fen Zhang:
Department of Mathematics
Beijing University
Beijing 100871
PEOPLES REPUBLIC OF CHINA

Rebut el 24 de Mar¸c de 1995
