<!-- source: https://msp.org/pjm/1994/166-2/pjm-v166-n2-p04-s.pdf | converted from PDF -->

Paciﬁc
Journal of
Mathematics

THE NUMBER OF LATTICE POINTS WITHIN A CONTOUR
AND VISIBLE FROM THE ORIGIN

DOUGLAS AUSTIN HENSLEY

Volume 166 No. 2 December 1994

PACIFIC JOURNAL OF MATHEMATICS
Vol. 166, No. 2, 1994

TH E NUMBER OF LATTIC E POINT S WITHIN A
CONTOU R AND VISIBLE FROM TH E ORIGIN

DOUG HENSLEY

The main result is an estimate for the number P(r) of
relatively prime pairs (α, b) of integers within a contour.
When specialized to the contour x2 + y2 = r this estimate
gives

P{r) = (6/π)r
 + ( without the RH, O ((rV 2 exp(-(logr)W +e))

or with the RH 0

A similar estimate, with the same sort of error, is ob-
tained for the number of relatively prime pairs (α, b) of
positive integers so that ab < r. The error term for a gen-
eral contour depends on the maximal value of the radius
of curvature of the bounding contour.

1. Introduction . The number R(r) of integer pairs (α, b) for
which a2 + b2 < r is known to satisfy

R(r) = π r + 0 e(rΘ+€)

where 1/4 < θ < 7/22. The main result here is an estimate of the
number P(r) of relatively prime integer pairs (α, 6) within a contour.
When specialized to the contour x\ + x\ = r, it gives

P(r) = (6/π)r + 0e (r1'2 exp

If the Riemann Hypothesis (RH) holds, this improves to

If we assume further that the correct value of θ in the circle prob-
lem is 1/4, then the exponent 51/110 becomes 9/10. We give a

295

296 DOUG HENSLEY

comparable estimate for the divisor problem (lattice points under a
hyperbola) in section 3.
The first estimate, which does not depend on any unproven hy-
potheses, holds uniformly over a wide range of convex contours en-
closing the origin. The key parameter is the maximum radius of cur-
vature p. The number of lattice points inside a square with sides of
length r parallel to the coordinate axes is r2 + O(r). The error term
cannot be improved because a whole rank of lattice points is lined
up along the boundary of the square, and the slightest change in r
can move the boundary line to the other side of this rank of lattice
points. The same phenomenon obstructs the estimation of lattice
point count inside arbitrary regions whenever the region contains a
particularly straight segment at any slope. The basic theorem on
lattice points in ϋft
2 within a region A is due to van der Corput, and
with explicit constants and an elementary proof, to Chaix [3]. It
takes this difficulty into account by framing the estimate in terms of
the maximum straightness of the bounding curve, that is, in terms
of the maximal radius of curvature p = p(A):

THEORE M (VAN DER CORPUT , CHAIX) . There exists an explic-
itly computable constant C > 0 such that if A is a convex region in
!R
2 with maximal radius of curvature ρ(A) > 0, then

I Lattice Count (A) - Area (A)\ < C(l + p(A))2/*.

The exponent is best possible, although in special cases such as
that of a circle with center at a lattice point the exponent can be
improved some. For the circle, the best known constant, due to
Iwaniec and Mozzochi [2], is 7/11+e. It is known that this exponent
cannot be less than 1/2. There is no real consensus, nor is there
strong numerical evidence, on whether or not the true value is 1/2 +

The results given here for the number of visible lattice points
(points with relatively prime integer coordinates) improve on an
unpublished result of Biagiolli, in which one had (6/τr2) Area (A) +
O(ρ) for reasonable contours. The general idea is, in both cases,
inclusion and exclusion using the Mobius function μ(d), but this
time with a trick to take advantage of the smooth contour. While it
is not standard notation, we shall for technical convenience exclude

NUMBER OF LATTICE POINTS WITHIN A CONTOUR 297

0 from all lattice point counts from now on. This will not affect the
conclusions. (The trouble with counting the origin is that inclusion
and exclusion fails. A domain far from the origin poses a related
problem, which applies to all the lattice points in the domain. Large
divisors can sift the set of visible points down to an empty remnant.)
Let A be a domain in 3£
2, including 0, with area \A\ and maxi-
mal radius of curvature p — p(A) on its (smooth) boundary. More
precisely, the boundary of A should at all points have a unique unit
tangent vector when traced counterclockwise , and for any arc of
length s along this boundary, the cumulative change in direction for
this vector should be at least s/ρ(A).
Let N(A) — sup{|(xi,^2)| •' (^i?^2) £ ^4} be the maximum dis-
tance from the origin to the boundary of A. Clearly A lies within
any circle of radius ρ(A) tangent to A and convex in the same di-
rection, so that N(A) < 2ρ(A). We may as well assume p large
(details later), and we do. Let R(A) denote the number of lattice
points exclusive of the origin, or integer pairs (α, b) φ 0 in Λ, and
let P(A) denote the number of relatively prime pairs among these.
Then with tA := {^(^1,^2) : (^1^2) £ A}, we have by inclusion
and exclusion
 N(A)
(1) P(A) = Σ μ(d)R(d-ιA).

For an arbitrary domain J3, let E(B) := R(B) — \B\. (Later, we
will have occasion to use a different definition of E in connection
with the divisor problem. The idea is that E denotes the difference
between the actual number of nonzero lattice points enclosed and
the expected number, which is in most cases the area.)
Let (*I,*2J - -*Λ) = {tι{A),t2{A),.. Λk(A)(A)) be the increasing
sequence of real numbers t G (0,1] for which the boundary of tA
contains a lattice point. Let Tj = 1/tj. Let Ij(A) denote the interval

(TJ+I..TJ]. Then for any y, 1 < y < N(A), and with the convention
that if Tj+ι <y < Tj then Ij is truncated at the lower end by y, we

298 DOUG HENSLEY

have

(2) P(A) = \A\ Σ d-2μ(d) + Σ μ{d)E{dΓιA)
d<N(A) d<y Σ

= (Main + Eo) + EX + E2 + ES say.

This is the trick. Different methods suit different terms.
The first term here is

Main + Eo = ±\A\ + Oe (j£L exp (-

from the well known estimate [5] for the Mobius sum

M(x) := Σ A*(«Q = Oe (xexp ( -
d<x

To estimate the second term one simply uses the van der Corput-
Chaix [3] estimate

(3) E(A) = 0(1 + p(Af3)

which holds uniformly over all domains A. In this second term,
d < N(A) ^C p(^4)? the radius of curvature of d~ιA will be at
least comparable to 1, and the "1 " can be omitted in the estimate
above. For the last two terms we can take advantage of the hard-core
number theoretic bounds on M(x): M(x) <ζi xexp(—\og3'5~ex), or
on the Riemann Hypothesis, M(x) <S χΐ+e. This latter estimate,
if true, is roughly best possible. Odlyzko and teRiele [6] have even
shown that Merten's conjecture, to the effect that | Σ3rf<χ M(^) I ^
x1/2 is false.
In the next section we discuss the various error terms and prove
a theorem for general, reasonably rounded, convex contours enclos-
ing the origin. In section three, as mentioned previously, we count
relatively prime pairs for which the product is bounded by r 2.

2. The general case. For the routine text of this section, we
abbreviate p(A) to p. There are several error terms to control. We

NUMBER OF LATTICE POINTS WITHIN A  CONTOUR 299

have an estimate for E o from section 1. For E\ we have the simple
estimate
 ^1 = ^ I 2-frf P  \  =v\y P  )
\d<y J
from (3). Now again with the convention that replaces Tj+ι with y
ifr j+1 <y<r i ,

E 2=Σ E(^lA)(M(rj)-M(τj+ι))
Tj>y

(4) =0

or on the RH,

(4') E 2 =  O,

Finally, integrating by parts gives

E3 = 2\A\ £  Γ  s-3(M(s) - M(τj+1))ds
Tj>y Jτi+ι

(5) =  O e (\A\y~1 exp ( -

On the RH, the same approach gives

(5') E z =  O e (\A

Now fix e >  0, put aside the RH, and take

y =  pexp(-(l/2)log (3/5)- £p)

Then for p  sufficiently large,

(6) logy >  (11/12) log(3/5)"€ p.

This condition specifies "sufficiently large" p  from the introduction.
Now it will be convenient to  set δ  := | — e.
Continuing with the analysis of E2, from (4) and (6) we have

(7) E 2 =  O e (p 2/ 3 exp(-(ll/12) log* p) Tj>y

300 DOUG HENSLEY

If, in this last sum, we count the terms by multiplicity according to
the number of lattice points on the boundary of tjA, this can only
serve to increase the sum. With this convention, though, we have
the sum in (7) is

(8) £ ί
p-
1 exp( | log5 p)} XeZ2np~l exp( | log5 p)A

and on replacing the scaled copy of A with a disk D about the origin
of radius 4 exp(| log
5 p), this sum increases to <C p1^ Σ\eD \M~l^S ^
p1/3 exp(| log
5 p)and it follows immediately that

(9) £ 2 = O

With our choice of y, the bound (5) on £3 reduces to

(10)
 = Oe (exp (-^log a p ) p- χ μi ) = OeE 3

which is less than the tolerance allowed for in other error term esti-
mates. With this same choice of y, E\ = Oe (ρexp(—(l/6)log5p)J.
In view of the stronger bound on Eo, this establishes

THEOREM 1. There exists a constant C > 0 such that for all
fixed e > 0; uniformly over A containing the origin and for which
p(A) > C,

P(A) = ^-2\A\ + Oe (p(A)exp ( -

Assuming the Riemann Hypothesis gave us

(11)
 E
Ά = O€ (\A\y<-*'2) , and E2 = Oe (V 3 Σ ^'
V
 τ
i>y

Proceeding as before with E2 we get, this time on taking y
that
 NUMBER OF LATTICE POINTS WITHIN A CONTOUR 301

(9')

This now gives

THEORE M 2. If the Riemann hypothesis is correct, then with the
same hypotheses and uniformity as in theorem 1,

REMARK . Any upper bound θ < 1 for the real part of a zero of
ζ(s) leads to a similar bound on the error in P(A) with an exponent
less than one on p(A). Stronger bounds for E(A) for particular
contours likewise yield improved estimates , but only in conjunction
with the Riemann hypothesis.

3. The circle and divisor problems. Although the region un-
der a hyperbola does not fit the premises of theorems 1 and 2, a
similar result holds. We give details only for the case of the di-
visor problem, but the same Riemann-hypothesis-conditional esti-
mate for the number of points in a circle about the origin of ra-
dius p holds with virtually the same proof. We begin with the
recent sharp estimate [2] for the number of lattice points in the
region Ap := {{xux2) : \ < Xux2,xχx2 < p 2}. They give (with
C = 2 7 - 1)

R(A
P) = 2p2 log(p2) + Cp2 + O€ (p^/ 11 ) .

Though this estimate does not have the exact form of "pointcount=
=area+small error", the ideas of section 2 go th rough. The ana-
logue to (1) is

d<p

(12) = £ μ(d) (F(p/d) + E{p/d)) say
d<p

302 DOUG HENSLEY

where now R(z) := R({(xι,x2) : 1/2 < x\,x2,x\x2 < z2}) and
E{z) := Λ(z) - 4z 2 logz- Cz2. By[2], £(z) = Oe (z<7+e>/n) . As in
(2), with P(p) := P(Λ p) etc., this gives

d<p
(13) = £ μ(d)F(p/d) - Σ μ(d)F(p/d) + ^ μ(d)E(p/d).
d>p d<p

Now put £ 0 = -Σd>Pμ(d)F(p/d). Put E = Σd<Pμ(d)E(p/d).
Then for arbitrary y,l <y < pv/e have

(14) E = Σ
d<y y<d<p

Let (ίi,Ϊ2? *fc ^ 1) be the successive values at which R(tjp)
increases. Let Tj = l/tj. This time, ί^p runs through the integers
from 1 to [p
2], so that tά = j
1/2
ρ~
λ and TJ = pj~1/2. Put Ij(p) :=
(τj+i,Tj], except that in the least interval which meets (y, oo) we
replace r^+i with y. As before we now discuss separately the cases
in which Tj < y, > y. For the case Tj > y we take note of the fact
that R(ρ/d) = R(ρ/τj) whenever Tj+i < d <Tj. As in (2), we break
down E further with

Έ = Σ μ(d)E(p/d) +ΣΈ
d<y
+ Σ Σ

so that P(ρ) = Σd>i β(d)F(ρ/d) + E0 + E1 + E2 + EΆ say. Now

(16) E 0 =

From [2],

(17) ^ « Σ (l)
d<V 5  VCt /

NUMBER OF LATTICE POINTS WITHIN A CONTOUR 303

Again the estimation of E2 is the main issue. We have

(18) £ 2 « £ \E{plτi)\ \M(τj+ι) -
τj>y

Taking y =  p 4/ 5, this gives

E2 « P1/2+e

(19) <p 1/2+ e Σ / /22 " 1/4+ e

Now
 Γ (F(pfr)-F(p/s))dM(s)
Tj>y Jτ3+ι

= - Σ Γ  s"
2i?'(^/
s) (M
(s) -  M( ri)) d s

j<p 2/ 5  ^Tj + l

« Σ Γ s^2F'(p/s)ds

(20)

We now  have th e bounds £ 0 <P £+1/2 , £i<p 51/55+£ , E 2 <p 51 / 55+2£ ,

and E 3 <p 2 / 5+e . Thus Ej<^p51/55+2e for all four error terms E^, so
that (since e is arbitrary)

(21)

An elementary calculation now gives

Σ μ(d)F(p/d) =  ^p 2 logp + -i(27 -

7Γ π

which gives our final result:

THEORE M 3. If the Riemann hypothesis is true, then the number
of pairs P(p) of relatively prime positive integers with product no
larger than p 2 as p —>• 00 is given by

P(p) =  ^p 2 logp + ^(2 7 - l)p 2 - i^C'(2) + O

304 DOUG HENSLEY

REMARKS . If we assume further that the correct exponent in
the divisor or circle problem is (1/4) + 6, then 51/55 in theorem
3 can be reduced to 9/10. Even moderately convincing numerical
evidence for the true rate of growth in max p< x P(AP), say for the
circle, is not easily amassed. The best published studies depend on
an algorithm that requires O (p 1//2) evaluations of the integer part
of a square root. Vinogradov, and later in a sharper form Chaix [3]
gave an elementary proof that R(AP) — \AP\ + 0 (p 1//3). Their ideas

can be adapted to give an algorithm which requires O (ρ1// 3 log p)
evaluations of the integer part of a square root. (The log factor
can be eliminated but at the cost of an impractically large implicit
constant.) Even so, finding P(AP) requires O (p 1^ 2) evaluations of
the integer part of a square root. Small scale computation fails to
indicate a dramatic difference in the behaviors of the error term for
R and P.
 REFERENCE S

[1] A. Biagiolli, private communication.
[2] H. Iwaniec and C.J. Mozzochi, On the divisor and circle problem, (to
appear) (39 pp).
[3] H. Chaix, Demonstration elementaire d'un theoreme de Van der Corput,
C.R. Acad. Sc. Paris, 275 (1972) Series A, 883-885.
[4] W. Fraser and C. C. Gotlieb, A calculation of the number of lattice points
in the circle and sphere, Math. Comp., 16 (1962), 282-290.
[5] A. Ivic, The Theory of the Riemann Zeta Function with Applications,
Wiley & Sons, New York 1985.

[6] A. Odlyzko and H. te Riele, Disproof of the Mertens conjecture, J. Reine
u. Angew. Math., 357 (1985), 138-160.

Received September 28, 1992, revised December 21, 1993, and accepted for
publication October 17, 1994.

TEXA S A & M UNIVERSITY

COLLEGE STATION, T X 77843-3368

PACIFIC JOURNAL OF MATHEMATICS

Volume 166 No. 2 December 1994
 213Geometric aspects of Bäcklund transformations of Weingarten
submanifolds
STEVEN BUYSKE
 225Multipliers between invariant subspaces of the backward shift
ROBERT BRUCE CROFOOT
 247The Cauchy integral, analytic capacity and subsets of quasicircles
XIANG FANG
 295The number of lattice points within a contour and visible from the origin
DOUGLAS AUSTIN HENSLEY
 305On ﬂatness of the Coxeter graph E8
MASAKI IZUMI
 329Immersions up to joint-bordism
GUI SONG LI
 339Generalization of the Hilbert metric to the space of positive deﬁnite
matrices
CARLANGELO LIVERANI and MACIEJ WOJTKOWSKI
 357Periodicity, genera and Alexander polynomials of knots
SWATEE NAIK
 373On divisors of sums of integers. V
ANDRÁS SÁRKÖZY and CAMERON LEIGH STEWART
 385Approximately inner automorphisms on inclusions of type IIIλ-factors
CARL WINSLØW
 401Correction to: “A convexity theorem for semisimple symmetric spaces”
KARL-HERMANN NEEB
 403Correction to: “Periodic points on nilmanifolds and solvmanifolds”
EDWARD KEPPELMANN
 405Correction to: “Partially measurable sets in measure spaces”
MAX SHIFFMANPaciﬁcJournalofMathematics1994Vol.166,No.2
