<!-- source: https://arxiv.org/pdf/math/9906132 | converted from PDF -->

arXiv:math/9906132v2  [math.MG]  14 Jan 2000
Diﬀraction from visible lattice points
and kth power free integers

Michael Baake1, Robert V. Moody
2 and Peter A. B. Pleasants3

1) Institut f¨ur Theoretische Physik, Universit¨at T¨ubingen,
Auf der Morgenstelle 14, D-72076 T¨ubingen, Germany
2) Department of Mathematical Sciences, University of Alberta,
Edmonton, Alberta T6G 2G1, Canada
3) Department of Mathematics and Computing Science,
University of the South Paciﬁc, Suva, Fiji

Dedicated to Ludwig Danzer on the occasion of his 70th birthday

Abstract

We prove that the set of visible points of any lattice of dimension n ≥ 2
has pure point diﬀraction spectrum, and we determine the diﬀraction spectrum
explicitly. This settles previous speculation on the exact nature of the diﬀrac-
tion in this situation. Using similar methods we show the same result for the
1-dimensional set of kth-power-free integers with k ≥ 2. Of special interest
is the fact that neither of these sets is a Delone set — each has holes of un-
bounded inradius. We provide a careful formulation of the mathematical ideas
underlying the study of diﬀraction from inﬁnite point sets.

1

Introduction

It has long been known that the diﬀraction spectrum of a crystal consists of pure
Bragg peaks only, being a pure point measure supported on the lattice dual to the
lattice of periods. Until about 15 years ago it was tacitly believed that crystals were
the only discrete point sets with this property. Now, however, we know that many
quasicrystals have pure point diﬀraction spectra (though in a signiﬁcantly diﬀerent
sense, since the locations of the peaks are no longer discrete). These quasicrystals are
all Meyer sets, that is, sets S that are both uniformly discrete and relatively dense
and whose diﬀerence sets ∆ = S − S also have these properties. (For a discussion of
Meyer sets, see [20]). There has consequently been a feeling that a perfectly diﬀracting
discrete point set, if not precisely a Meyer set, must be closely related to a Meyer set.
Indeed, the Meyer condition cannot possibly be strictly necessary since, as we shall see
later, adding or removing a set of density zero does not alter the diﬀraction spectrum
of a discrete point set, and one can clearly destroy the relative denseness of any
uniformly discrete point set by removing a set of density zero.
In this paper we give some simple examples of perfectly diﬀractive discrete point
sets that deviate much further from the Meyer properties than this; in fact we consider
sets which, for arbitrarily large D, have a lattice of holes of inner diameter at least D.
Such a set cannot diﬀer from a Meyer set (or from a model set, which is a particular
case of a Meyer set) only by a set of density zero. The sets comprising our examples
are well known in number theory: they are the sets of visible (or primitive) points of
a lattice in any dimension n ≥ 2, see [1, 14] and the front cover of [1] for a picture of
the case n = 2, and the 1-dimensional sets consisting of the kth-power-free integers
for k ≥ 2, see [14, §6.6].
As well as giving a rigorous derivation of the diﬀraction spectra that depends on
explicitly calculating the autocorrelation of the point set, we precede it by a shorter
derivation of the pure point parts of the spectra only, via the Fourier transform of the
point set. This takes a similar line to previous attempts and uses a general result of
A. Hof. It provides a quick, elegant way of calculating the discrete parts of the spectra
which gives the correct results but does not have a full mathematical justiﬁcation at
present.
The rigorous approach is a response to the history of the problem for the visible
lattice points, described in [3]. In particular, there is a clear disagreement between
earlier results in [29] and in [21] regarding the nature of the diﬀraction. This was
partially resolved in favour of [21] by a calculation of the point part of the diﬀraction
spectrum in terms of Dirichlet series and its comparison with a real optical experiment

2

[3]. The older numerical calculations in [29], using the fast Fourier transform, suﬀer
from an insuﬃcient resolution and are misleading. In this article, we give the deﬁnitive
description of the nature of the diﬀraction spectrum by making the previous formal
calculation of the pure point part [21, 3] rigorous and by proving that there is no
continuous part.
The paper is organized as follows. We start by describing the results from number
theory and related areas we need, then describe some basic properties of the set of
visible points. Next we discuss the background material of Fourier transforms and
autocorrelations needed for diﬀraction spectra. This is ﬁrst framed in the language
of tempered distributions and then connected to measure theoretical considerations
which are a basic part of the theory of diﬀraction. We then give the short intuitively
motivated method of computing the pure point part of the diﬀraction spectrum, both
for the visible points and the kth-power-free integers. The following two sections are
devoted to an explicit calculation of the autocorrelation of the set of visible points,
followed by a rigorous derivation of the diﬀraction spectrum. The ensuing section
treats the set of kth-power-free numbers in the same way, followed by an extensive
outlook and a summary.
Strictly speaking, neither the measure theoretical picture nor the intuitive ap-
proach to computing the diﬀraction are necessary for the logic of the paper, and they
could be omitted by the reader whose primary concern is verifying the mathematical
validity of the results. But we would like to stress that the additional information
provided in this article is needed to locate our results in the wider context of mathe-
matical diﬀraction theory.

Tools from number theory

Here we set out some results we need from number theory and related areas.

Notation

We use the notation (l, m) = gcd(l, m) to denote the greatest common divisor of two
integers l and m. For integers d and x, d | x means that d is a divisor of x. Summation
conditions like “d | x” are to be interpreted as meaning that d runs through positive
divisors of x only (even when x is negative). The divisor function σ(m) (deﬁned for
m ∈ Z
+) counts the number of positive divisors of m, so σ(m) = ∑

d|m 1.
Also, we will frequently use the O-notation for error estimates. For example, we
say that a function f (r) is O(1/r) if there is a constant c such that |f (r)| is bounded
by c/r for r ≥ 0, see [1, Sec. 3.2] for details.

3

Lattices

A lattice in Rn is a set Γ of the form

Γ = Zb1 ⊕ · · · ⊕ Zbn , (1)

where {b1, . . . , bn} is a set of n linearly independent vectors called a basis of Γ.
We deﬁne vol(Γ) to be the volume of a fundamental region of the lattice, e.g. of
{t1b1 + · · · + tnbn | 0 ≤ t1, . . . , tn < 1}. Consequently, vol(Γ) can be calculated as
vol(Γ) = | det(b1, . . . , bn)| which turns out to be independent of the basis chosen.
Every lattice is uniformly discrete and relatively dense in Rn and is a subgroup of Rn

under vector addition.

Proposition 1 Let Γ be a lattice and a an arbitrary vector (not necessarily in Γ).
Let N(R) be the number of points x in Γ + a with |x| < R. Then there are constants
c1 and c2, depending only on Γ, such that, for all R > 0,

|N(R)vol(Γ) − vnRn| ≤ c1Rn−1 + c2 , (2)

where vn is the volume of the unit ball in Rn, i.e. vn = πn/2/ Γ(1 + n
2 ).

Proof: The translates of the fundamental region of Γ by vectors in Γ + a tile Rn.
Let v be the total volume of those translates that meet the open ball BR(0) and v
the total volume of those translates that lie entirely inside this ball. Then the volume
vnRn of the ball and the number N(R)vol(Γ) are both bounded above by v and below
by v. So their diﬀerence is at most v−v, which is the total volume of the translates
of the fundamental region that meet the boundary of the ball. If D is the diameter1

of the fundamental region, then this volume is at most vn(R + D)n − vn(R − D)n ≤
2nvnDRn−1, when R ≥ D, and at most vn(R + D)n < 2nvnDn, when R < D. The
second of these estimates is obvious, while the ﬁrst (when R ≥ D) follows from

(R + D)n − (R − D)n =
 n∑

m=0
 ( n
m
)
Rn−m (Dm − (−D)m)

≤ 2 ∑

m odd
 ( n
m

)
Rn−1D (3)

= 2DRn−1 ∑

m odd
 ( n
m

) = 2nDRn−1 .

1The diameter of a bounded set S ⊂ Rn is the supremum of all distances between points of S.

4

This gives the result with c1 = 2nvnD and c2 = 2nvnDn. □
If Γ is a lattice and r is a nonzero real number then rΓ is also a lattice (a basis
of rΓ is {rb1, . . . , rbn}). When r is an integer rΓ ⊆ Γ and rΓ is a sublattice (and a
subgroup) of Γ, of index rn. For a nonzero integer m and two points a and b in Γ we
write a ≡ b (mod mΓ) to mean that a − b ∈ mΓ. With this notation we have the
following Chinese Remainder Theorem for a lattice Γ.

Proposition 2 Let Γ be a lattice and a1, a2, . . . , ar ∈ Γ. If m1, m2, . . . , mr ∈ Z
+

are chosen so that (mj, mk) = 1, for 1 ≤ j < k ≤ r, then there is a point a ∈ Γ such
that the solutions of the simultaneous congruences

x ≡ a1 (mod m1Γ), . . . , x ≡ ar (mod mrΓ) (4)

are precisely the points x ∈ Γ with

x ≡ a (mod (m1 · m2 · . . . · mr)Γ) . (5)

Proof: This follows by applying the Chinese Remainder Theorem for integers [14,
Thm. 2.7.1] to each coordinate with respect to a basis of Γ. □
We deﬁne the content of a nonzero lattice point x in a lattice Γ by

cont(x) := max{ l | x ∈ lΓ} . (6)

If x is expressed in terms of a basis of Γ, x = ∑ xjbj, then cont(x) = gcd(x1, . . . , xn)
(which is therefore independent of the particular basis chosen). For consistency and
convenience, we deﬁne cont(0) = ∞. For m ∈ Z
+ and x ∈ Γ, we have

cont(mx) = m · cont(x) . (7)

It is clear from (6) that for x ∈ Γ \ {0}

cont(x) ≤ |x|
L(Γ) , (8)

where |x| is the Euclidean length of x and L(Γ) is the length of the shortest nonzero
vector in Γ.
The set V = V (Γ) of visible points of a lattice Γ (also known as the primitive
points of Γ) is V := {x ∈ Γ | cont(x) = 1} . (9)

In terms of a lattice basis, V consists of all points whose coordinates have no common
divisor. These are precisely the lattice points that are visible from the origin, in the

5

sense that the line segment joining them to the origin contains no other lattice point.
When n = 1, V consists of two points, equidistant from 0, but otherwise V is inﬁnite
and, indeed, contains more than half the lattice points, as we shall see. For m ∈ Z
+

we have mV = {x ∈ Γ | cont(x) = m} . (10)

Density

Let S be a uniformly discrete set of points in Rn (i.e. there is a c > 0 so that x, y ∈ S
with x ̸= y implies |x − y| ≥ c). We say S has natural density D = dens(S) if

DR = DR(S) := |{x ∈ S | |x| < R}|
vnRn −→ D (11)

as R → ∞. The expression |D − DR| (a function of R) is called the error term for the
natural density. For example, by Proposition 1, D = dens(Γ) exists for every lattice
Γ and is equal to 1/vol(Γ) (with error term O(1/R)).
If dens(S) exists and if T is an orthogonal transformation then dens(T (S)) =
dens(S), but it is a failing of the natural density that it is not always true that
dens(T (S)) = dens(S)/| det(T )| when T is a general aﬃne transformation, see Ap-
pendix.
When we use the word “density” from now on we shall mean natural density.

Power-free numbers

For an integer exponent k ≥ 1 the set F = Fk of kth-power-free integers is

F := {n ∈ Z | n is not divisible by dk for any integer d > 1} . (12)

An equivalent characterization of the numbers n ∈ F is that in their prime power
factorization n = ±pa1
1 pa2
2 · · · par
r every exponent aj is less than k. In close analogy
with V , the case k = 1 is trivial, F1 consisting of just the two numbers ±1, but for
k ≥ 2, Fk is inﬁnite and contains more than half the integers. These numbers have
been studied for a long time, see [22, 19] for two sources relevant in our context.

Inclusion-exclusion

The M¨obius function µ(m) is deﬁned for m ∈ Z
+ by

µ(m) :=
 



 1, when m = 1,
(−1)r, when m is a product of r distinct primes,
0, when m is divisible by the square of a prime. (13)

6

It is multiplicative in the sense that µ(lm) = µ(l)µ(m) when (l, m) = 1 (and clearly
µ(lm) = 0 when (l, m) ̸= 1).
A number of inversion formulæ and variants of the inclusion-exclusion principle
can be expressed in terms of this function. The result we need in this paper is

∑

d|m µ(d) = { 1, if m = 1,
0, if m > 1, (14)

see [14, Thm. 6.3.1]. For a point x in a lattice Γ this shows that

χV (x) := ∑

d|cont(x) µ(d) (15)

is the characteristic function of the visible points V of Γ (except that it is undeﬁned
when x = 0).
Similarly, since dk | x if and only if d divides the largest integer whose kth-power
divides x, χF (x) := ∑

dk|x µ(d) (16)

is the characteristic function of the kth-power-free integers (except for being undeﬁned
when x = 0).

Dirichlet series

The well-known Riemann zeta-function (see, for example, [1, Ch. 12] or [14, §9.2]) is
deﬁned for complex numbers s with Re(s) > 1 by

ζ(s) :=
 ∞∑

m=1
 1
ms = ∏

p
 (1 − 1
ps
 )−1 , (17)

where the sum is called a Dirichlet series and the product (in which p runs through
all positive prime numbers) is called an Euler product. The sum and product are ab-
solutely convergent for s in the half-plane Re(s) > 1, but ζ(s) can be meromorphically
continued to the whole of C, for example ζ(0) = −1/2. The only singularity of ζ(s)
is a simple pole at s = 1 with residue 1. Using the Euler product, we see that the
Dirichlet series of 1/ζ(s) is given by

1
ζ(s) = ∏

p
 (1 − 1
ps
 ) =
 ∞∑

m=1
 µ(m)
ms . (18)

7

This function has inﬁnitely many poles (all in the half-plane Re(s) < 1). Its value at
1 is 0 and its value at 0 is −2.
Another Dirichlet series we shall encounter is

ξ(s) :=
 ∞∑

m=1
 µ(m)σ(m)
ms = ∏

p
 (1 − 2
ps
 ) . (19)

Again, both the Dirichlet series and Euler product are absolutely convergent in the
half-plane Re(s) > 1. It can also be seen from the Euler product that ξ(1) = 0.

Visible points of a lattice

Here we summarize some elementary and well-known properties of the set of visible
points V of a lattice Γ, together with complete proofs.
Since Γ is a free Abelian group of rank n, its automorphism group, Aut(Γ), is
isomorphic to the matrix group GL(n, Z). Explicit isomorphisms can be found by
taking coordinates with respect to any lattice basis.

Proposition 3 The orbits of the action of GL(n, Z) on Γ are the sets mV , m ∈ N0.
In particular, GL(n, Z) acts transitively on V .

Proof: Since the elements of GL(n, Z) cannot decrease content and are invertible,
they preserve content. Hence each set mV is invariant under GL(n, Z). The transi-
tivity of GL(n, Z) on V can be seen from the facts that every visible point belongs to
some basis of Γ [10, §3,Thm. 5] and that any two bases of Γ are related by a trans-
formation in GL(n, Z). For m ∈ Z
+ the transitivity of GL(n, Z) on mV follows from
its transitivity on V . Transitivity on the singleton orbit 0 · V = {0} is trivial. □

Proposition 4 V is uniformly discrete, but has arbitrarily large holes. Moreover,
for any r > 0, there is a set of holes in V of inradius at least r whose centres have
positive density.

Proof: The uniform discreteness is trivial, as V is a subset of a lattice. Now let
C = {a1, . . . , as} be any ﬁnite conﬁguration of points in Γ (e.g. all points in a ball or
a cube). Choose s integer moduli m1, . . . , ms that are > 1 and coprime in pairs (for
example, they could be the ﬁrst s primes). By Proposition 2 there is a point a ∈ Γ
with a ≡ −a1 (mod m1Γ) , . . . , a ≡ −as (mod msΓ) . (20)

8

Now for any x ≡ a (mod m1m2 . . . msΓ) the conﬁguration C+x = {a1+x, . . . , as+x}
is congruent, in the geometric sense, to C but no point in C + x is visible, since
aj + x ∈ mjΓ. The points x have density dens(Γ)/(m1m2 . . . ms) > 0. □
For n = 2, and with the density of holes not mentioned, this is Thm. 5.29 of [1].
We note that the hole nearest the origin provided by this argument can be expected to
be at a distance of the order ss and that the density guaranteed for holes of inradius
r is of the order r−n2rn, so large holes, while having positive density, are probably
extremely sparse.
This proposition shows that V , though uniformly discrete, is not relatively dense,
and hence not a Delone set. Consequently it is not a Meyer set either. (Recall that
Λ is a Meyer set if and only if both Λ and Λ − Λ := {x − y | x, y ∈ Λ} are Delone
sets [17].) Also, V cannot be transformed into a Delone set by adding a set of zero
density. However, we do have:

Proposition 5 If n ≥ 2 then V − V = Γ.

Proof: Clearly, V − V ⊆ Γ. Now let x = ∑n
j=1 xjbj ∈ Γ, where n ≥ 2. Then,
(x1, x2, . . . , xn) = (x1 + 1, 1, x3, . . . , xn) − (1, 1 − x2, 0, . . . , 0), and x is the diﬀerence
of two visible points. □
The existence of arbitrarily large holes also implies that the set of visible points
cannot have a uniform density (not, at least, when its density is positive in some
sense, as is the case for n ≥ 2). It does have a natural density, however:

Proposition 6 The visible points V of a lattice Γ ∈ Rn have a natural density given
by
 dens(V ) = dens(Γ)
ζ(n) , (21)

with error term O(1/R) when n ̸= 2 and O(log R/R) when n = 2.

This is a standard example of the use of M¨obius inversion given (at least for the case
Γ = Z
2) in most introductory number theory books (for example, [14, Thm. 6.6.3]
and [1, Thm. 3.9]). In these particular references the averages are taken over triangles
and squares, respectively, instead of balls. Indeed the density is independent of the
shape of the region averaged over. We say more about this in the Appendix.
Proof: The proposition is trivially true for n = 1, when the pole of ζ(s) at 1
gives a density of 0, so we assume from now on that n ≥ 2.
The density of V , if it exists, is the limit as R → ∞ of
1
vnRn ∑

|x|<R
x∈V
 1 , (22)

9

which by (15) is
1
vnRn ∑

x∈Γ\{0}
|x|<R
 ∑

m|cont(x)
µ(m) = 1
vnRn ∑

1≤m<cR µ(m) ∑

x∈mΓ\{0}
|x|<R
1 , (23)

where c = 1/L(Γ) (using (8)). The inner sum is equal to the number of nonzero points
y ∈ Γ with |y| < R/m, which by Proposition 1 is

vn
vol(Γ)
 ( R
m
)n + O
 (( R
m
)n−1)
 + O(1) . (24)

Substituting this into the right hand side of (23) gives

dens(Γ) ∑

1≤m<cR
 µ(m)
mn + O( 1
R
 ∑

1≤m<cR
 1
mn−1
 ) + O ( 1
Rn−1
 ) (25)

which tends to dens(Γ)/ζ(n) as R → ∞ when n ≥ 2 by (18). The total error is
O(1/Rn−1), from the last term and the tail of the sum in the main term, and O(1/R)
(or O(log R/R) when n = 2 and the series diverges logarithmically), from the middle
term. □
Calculations of densities by M¨obius inversion form the core of this paper. This is
the ﬁrst of many.

Diﬀraction spectra

In this section we assemble the facts we need about distributions, Fourier transforms
and diﬀraction spectra. The mathematics underlying diﬀraction is quite subtle and
needs to be spelt out carefully. Although the discussion in this section does not contain
much that is new, it is nonetheless diﬃcult to extract it all from any convenient source.
We shall use a formulation based upon tempered distributions. For an essentially
parallel approach which starts with measures, we refer to [12]. We shall link the two
approaches later in this section.

Autocorrelations

In dealing with diﬀraction, and therefore Fourier transforms, it is appropriate to
use tempered distributions, whose test space S consists of the Schwartz functions
(also known as “rapidly decreasing functions”). We refer to ([30, 25]) for this and

10

the details on the standard topology which is used to describe convergence in S. A
tempered distribution T is a continuous (in the sense of this topology) linear functional
on S. The space of tempered distributions is denoted by S ′ and is equipped with the
weak*-topology. A simple example is δx, Dirac’s delta-distribution2 at the point x,
deﬁned by (δx, ψ) := ψ(x) for all ψ ∈ S. We prefer this notation to δx(ψ) because it
emphasizes the duality between S ′ and S.
If S is a uniformly discrete subset of Rn, we call

ωS := ∑

x∈S δx (26)

its Dirac comb. It is also a tempered distribution, and in fact the sum (26) is conver-
gent (with any ordering) in the weak*-topology.
To describe the diﬀraction from a Dirac comb ω = ωS we need its natural auto-
correlation distribution (also called its generalized Patterson function) deﬁned by

γω := lim
R→∞ 1
vnRn ∑

x,y∈SR δx−y , (27)

where SR = S ∩ BR(0) and BR(0) is the ball of radius R centre 0. We shall simply
call γω the “autocorrelation” of S from now on. The existence of this limit in the
weak*-topology is a prerequisite for the diﬀraction spectrum to be well deﬁned. (The
word “natural” refers to the use of the expanding ball BR(0) in the averaging process.
Replacing it by an expanding region of some other shape might lead to a diﬀerent
limit.) It is clear from the deﬁnition that enlarging or diminishing S by a set of
density 0 does not change its autocorrelation γω. In particular, adding or removing
any ﬁnite number of points does not change γω, as for natural density.
We say that S has ﬁnite local complexity if ∆ = S − S is discrete and closed in
Rn (as is clearly the case for all sets whose diﬀraction spectra we seek in this paper).
Such an S is uniformly discrete because 0 ∈ ∆ is isolated. The existence of the limit
(27) in the weak*-topology is now controlled by the following result.

Lemma 1 Let S be a set of ﬁnite local complexity and ω = ωS its Dirac comb. Then
S has a natural autocorrelation γω if and only if the coeﬃcients w(a)

w(a) := lim
R→∞ 1
vnRn ∑

|x|,|x−a|<R
x,x−a∈S

1 (28)

2Nowadays it is usually called Dirac’s point measure for reasons that will become clear shortly.

11

exist, i.e. the right hand side is convergent for all a ∈ ∆. In this case, w(a) ≥ 0 for
all a ∈ ∆ and γω is the tempered distribution of positive type3 given by the weak*-
convergent sum γω = ∑

a∈∆ w(a)δa . (29)

Proof: The existence of γω clearly implies the existence of w(a) for all a ∈ ∆ because
∆ is discrete by assumption and the Schwartz space S contains all C ∞-functions of
compact support, whence we can focus on any individual a.
Conversely, assume that the w(a) exist (they are then clearly ≥ 0). Since ∆
is closed and discrete, its intersection with any compact subset of Rn contains only
ﬁnitely many points. Consequently, the w(a) are locally summable and the right hand
side of (29) deﬁnes a distribution over the space D of all C ∞-functions of compact
support. We have to show that it is actually also a tempered distribution. This follows
from the translation boundedness
4 of ω which is then inherited by γω, see [12, Prop.
2.2]. Finally, γω can also be written as a certain volume-normalized convolution (see
below) which implies that it is a distribution of positive type. □

Fourier transforms

The Fourier transform ˆT of a tempered distribution T ∈ S ′ is deﬁned by ( ˆT , ψ) :=
(T, ˆψ), where we use the deﬁnition

ˆψ(y) := ∫
Rn e
−2πiy·x ψ(x)dx (30)

for the Fourier transform of functions ψ ∈ S. The Fourier transform maps the space S
onto itself and is continuous on S in the standard topology for Schwartz functions [25,
Thm. 7.7], hence it maps S ′ onto itself and is continuous on S ′ in the weak*-topology
[25, Thm. 7.15].
As special cases, we mention ˆδ0 = 1 and the well-known Poisson summation
formula for lattice Dirac combs
 ˆωΓ = dens(Γ) · ωΓ∗ (31)

where Γ∗ is the dual or reciprocal lattice deﬁned by

Γ∗ := {y | y · x ∈ Z , for all x ∈ Γ} . (32)

3See next section for a deﬁnition.
4We will explain this below in the context of measures.

12

(Eq. (31) can easily be derived from Poisson’s summation formula for Schwartz func-
tions [30, p. 254].)
For a set S of ﬁnite local complexity with autocorrelation γω, its diﬀraction pattern
(also called its diﬀraction distribution or diﬀraction spectrum) is the Fourier transform
ˆγω. In view of the remarks above, ˆγω is a tempered distribution. It is also a positive
measure, as we shall see.
The autocorrelation of a lattice Γ, for example, is supported on Γ itself (since
∆ = Γ − Γ = Γ) and each peak has equal amplitude dens(Γ). So the autocorrelation
is γω = dens(Γ)ωΓ and the corresponding diﬀraction spectrum is ˆγω = dens(Γ)2ωΓ∗,
a constant multiple of the Fourier transform of ωΓ itself. However, as we shall see,
the Fourier transform of a general point set (even of ﬁnite local complexity) does not
describe its diﬀraction in such a simple way.

Pure point distributions

Our principal concern is with showing that the visible points and kth-power-free points
have a pure point spectrum. In this section we consider a special class of point
measures which we will use in the sequel. We already borrow from the terminology
of measures here, although we will establish the precise connection only in the next
section.
Consider an arbitrary complex point measure. It can be expressed in the form

ν = ∑

x∈S w(x)δx , (33)

where the point set S is countable, but not necessarily uniformly discrete, and the
coeﬃcients or weights w(x) ∈ C are not necessarily constant. Note that the weights
may be complex numbers. Let us assume in addition that the measure is translation
bounded. This can be expressed as the condition that for every compact set K ⊂ Rn

the sum ∑

x∈S∩(K+a) |w(x)| (34)

is convergent and bounded uniformly in a. We denote the space of all translation
bounded point measures by T . All these measures are tempered, and we identify ν
with Tν, the corresponding tempered distribution.
As a subset of S ′, T is not closed in the weak*-topology. For example, the sequence
of pure point distributions {j−nωZn/j} (35)

13

tends to the constant function 1 as j → ∞. (For a test function ψ the numbers
j−nωZn/j(ψ) are approximating sums to the integral
5 of ψ.) A similar argument shows
that every bounded continuous function is a limit of pure point distributions, compare
the more detailed discussion in [24, Sec. IV.5]. Unfortunately, as this example shows,
the weak*-limit of such a sequence is not, in general, the same as its pointwise limit.
However, taking pointwise limits in T is justiﬁable under certain circumstances,
and fortunately these apply in the cases of interest to us here. We introduce a “locally
deﬁned” norm on T by

∥ν∥loc := sup
K
 ∫

K d|ν| = sup
K
 ∑

x∈S∩K |w(x)| , (36)

where the supremum is taken over all compact sets K of diameter < 1. This norm
deﬁnes a topology on T stronger than the weak*-topology and it provides a simulta-
neous “M-test” for pointwise and weak*-convergence of inﬁnite sums of translation
bounded point measures:

Lemma 2 If νj ∈ T for j ∈ Z
+ and ∑∞
j=1 ∥νj∥loc is convergent then ∑∞
j=1 νj is
pointwise and weak*-convergent to the same sum ν ∈ T .

Proof: Let νj = ∑

x∈Sj wj(x)δx and choose a ﬁxed covering of {Km}m∈Z+ of Rn

by compact sets of diameter < 1. For any ψ ∈ S we have

|(νj, ψ)| = ∣
∣
∣ ∑

x∈Sj wj(x)ψ(x)∣
∣
∣ ≤
 ∞∑

m=1
 ∑

x∈Sj ∩Km |wj(x)ψ(x)|

≤ ∥νj∥loc
 ∞∑

m=1 ∥ψKm∥ = Cψ · ∥νj∥loc , (37)

where ψKm is the restriction of ψ to Km and Cψ < ∞ is a constant that depends
only on ψ and the covering chosen. Hence ∑∞
j=1(νj, ψ) is absolutely convergent (by
comparison with ∑ ∥νj∥loc) and so ∑ νj is weak*-convergent to a distribution ν.
Also

(ν, ψ) =
 ∞∑

j=1(νj, ψ) =
 ∞∑

j=1
 ∑

x∈Sj wj(x)ψ(x) = ∑

x∈
⋃ Sj
 ∞∑

j=1 wj(x)ψ(x) , (38)

the reversal of the order of summation (with wj(x) := 0 whenever x ̸∈ Sj) being
justiﬁed by the fact that the double sum is absolutely convergent, in view of (37).

5Seen as a sequence of measures, (35) weak*-converges to Lebesgue measure.

14

Hence
 ν = ∑

x∈
⋃ Sj
 ∞∑

j=1 wj(x)δx (39)

is the pointwise sum of the νj’s.
Finally, if K ⊆ Rn is any compact set with diameter < 1 and we write S := ⋃ Sj
and w(x) := ∑∞
j=1 wj(x) then

∑

x∈S∩(K+a) |w(x)| ≤
 ∞∑

j=1
 ∑

x∈Sj ∩(K+a) |wj(x)| ≤
 ∞∑

j=1 ∥νj∥loc . (40)

Hence ν is translation bounded, and therefore tempered. □
Note that if µj is the distribution in (35) then µj+1 − µj is translation bounded
but ∥µj+1 − µj∥loc ≥ vn
2n−1 − 1
j(j + 1) , (41)

where vn is the volume of the n-dimensional unit ball. (The supports of µj and µj+1
intersect in the integer points only and there is almost no cancellation in calculating
the norm.) So the norms of the diﬀerences are bounded below by a positive constant
for large j and their sum diverges to inﬁnity, thus failing to satisfy the hypothesis of
the lemma. (An easier calculation along the same lines is ∥µ2k+1 − µ2k∥ ≥ vn/2n.)

Distributions and measures

The diﬀraction pattern ˆγω is a tempered distribution. However, it is also a positive
measure. This remarkable fact is indispensible for the general theory of diﬀraction,
making available to it a vast array of concepts and tools. For example, it makes it
immediately evident that the diﬀraction pattern may be viewed as having a pure point
part and a continuous part, a fact of considerable physical signiﬁcance.
The next two subsections sketch out this distribution theory – measure theory con-
nection in the context of diﬀraction. The proofs of the main theorems of this paper in
no way depend on this background material, which can therefore be ignored as far as
verifying the results is concerned. Nevertheless, it is desirable to realize the natural
connection to measure theory, both to see our results in their proper setting and be-
cause it is this picture that has a generalization to the diﬀraction theory of translation
bounded measures on locally compact Abelian groups which is an appropriate setting
for more general questions, compare [11, 2].
A distribution T is positive if for all positive test functions ψ, (T, ψ) ≥ 0. A
distribution T is of positive type or is positive deﬁnite if for all test functions ψ,

15

(T, ψ∗ψ∗) ≥ 0, where ψ∗(x) := ψ(−x). These two concepts are related by the Bochner-
Schwarz theorem (see [30, Thm. VII.XVIII] or [24, Thm. IX.10]) which asserts that a
tempered distribution is positive if and only if it is the Fourier transform of a tempered
distribution of positive type.
Let C denote the space of complex-valued continuous functions of compact support
on Rn and let ∥ · ∥ denote the supremum norm on C. A (complex) measure ν on Rn

is deﬁned as a linear functional on C such that for every compact set K ⊂ Rn there
is a constant aK such that |ν(φ)| ≤ aK∥φ∥ (42)

for all φ ∈ C with support in K. Such measures are in one-to-one correspondence
with regular Borel measures through the Riesz-Markov representation theorem, see
[8, Ch. XIII] and [4, Ch. 8, Sec. 69] for background material, and we thus identify
these two pictures. We deal only with regular Borel measures in this paper. If for
each φ ∈ C inequality (42) holds uniformly for all translates of φ, we say that ν is
translation bounded. This turns out to be a very useful concept because the Fourier
transform of a tempered measure, though a tempered distribution, need not be a
measure, but the Fourier transform of the autocorrelation of a translation bounded
tempered distribution, if it exists, is always a measure. Let us explain how to control
this subtle point in the context of diﬀraction theory.
Distributions and measures act on diﬀerent spaces of functions and are equipped
with diﬀerent topologies. Nonetheless, there is an important connection between them
which comes through the fact that the space D of C ∞-functions of compact support
is dense both in C and in S.
If a measure ν deﬁnes a tempered distribution Tν by

(Tν, ψ) = ν(ψ) = ∫ ψ dν (43)

for all ψ ∈ S, the measure ν is called tempered. A suﬃcient condition for a measure to
be tempered is that it is slowly increasing in the sense that ∫ (1 + |x|)−k|ν|(dx) < ∞
for some k ∈ Z
+, see [30, Thm. VII.VII] or [25, Ex. 7.12 b]. Here, |ν| is the unique
absolute value of ν, i.e. the smallest positive measure ρ such that |ν(φ)| ≤ ρ(|φ|) for all
φ ∈ C. It is also called the variational measure of ν. As a partial converse, any positive
tempered distribution is a positive tempered measure. Thus, under the assumption
of positiveness, tempered measures and tempered distributions can be viewed as the
same thing, and the Bochner-Schwartz theorem can be restated as follows: ν is a
positive tempered measure if and only if it is the Fourier transform of a tempered
distribution of positive type.
 16

Now, let ν be a translation bounded measure. Clearly ν is tempered. Our pre-
vious deﬁnition of the autocorrelation of a Dirac comb has a natural extension to
the autocorrelation γν of ν by means of a volume-normalized convolution of ν with
ν∗, where ν∗ is deﬁned by ν∗(φ) := ν(φ∗), see [12] for details
6. This construction of
γν guarantees that, when it exists, it is a positive deﬁnite tempered measure (and
distribution), so combining the previous arguments we see that the corresponding
diﬀraction pattern ˆγν is a tempered positive measure.
This is important because it is this object that describes what one actually sees
on the screen in a diﬀraction experiment: each (measurable) volume is assigned a
non-negative number, namely the total intensity of radiation scattered into this vol-
ume. In this article, we will only meet the simple case that ν is a Dirac comb ωS.
However, already the convolution with a function of compact support (a “proﬁle” of
the scatterer) shows why the more general setting is useful. Let us summarize this by
the following result, which is a combination of [12, Prop. 2.2] and [12, Prop. 3.3].

Proposition 7 Let ν be a translation bounded measure. If its natural autocorrela-
tion γν exists, it is a translation bounded (hence tempered) positive deﬁnite measure.
Furthermore, ˆγν is then a positive measure and also translation bounded.

Decomposition of measures

A pure point of a measure ν is a point x ∈ Rn with ν({x}) ̸= 0. Since ν is a regular
Borel measure, it has at most countably many pure points and the sum of |ν({x})|
over the pure points in any compact set K is convergent, and the pure points alone
serve to deﬁne a measure νpp called the pure point part of ν. Thus ν has a unique
decomposition as ν = νpp + νc , (44)

where νc := ν − νpp is the so-called continuous part
7 of ν, and is characterized by
having no pure points. A pure point measure is a measure whose continuous part is 0.
When a tempered measure ν is decomposed in this way the components νpp and
νc are, of course, measures, but not necessarily tempered. For a translation bounded

6Note, however, that the deﬁnition of the analogous operation to ∗ in [12] is slightly incorrect in
that it omits the extra complex conjugation.
7The word “continuous” here does not refer to being continuous as a function, since a line measure
in the plane, for example, is continuous. It refers to the intermediate value property that if there
are sets A ⊂ C with νc(A) < b < νc(C) then there is a set B with A ⊂ B ⊂ C and νc(B) = b. Some
authors use the word diﬀuse instead of continuous and the words atomic or purely discrete instead
of pure point.
 17

measure ν, however, the components are both translation bounded and hence tem-
pered. If ν is a positive tempered measure, the decomposition is automatically into
tempered components.
Returning now to diﬀraction patterns, we meet the special situation that ˆγω is a
positive measure. Consequently, it decomposes into a pure point part and a continuous
part, both of which are positive measures. The pure point part is called the Bragg
spectrum (of the point set S that created it). We say that the diﬀraction pattern is
pure point or that S has a pure point diﬀraction spectrum if its diﬀraction pattern is
a pure point measure, i.e. if it is equal to its Bragg spectrum.
Let us ﬁnally mention that, relative to Lebesgue measure, the continuous part νc
can be further decomposed into an absolutely continuous and a singular continuous
part, νc = νac + νsc, see [4, 24] for details. In our examples, we show that νc vanishes,
which means that there is neither an absolutely continuous nor a singular continuous
component present.

An intuitive derivation of the point spectra

This section describes a short, intuitive way of calculating the pure point part of the
diﬀraction spectrum of the visible points V of a lattice Γ and also of the kth-power-free
numbers F = Fk. Its purpose is to give a taste of our later number theoretic methods
in a simpler setting and also to contrast this intuitively clear calculation with the
more circuitous route via autocorrelations we take later in rigorously establishing the
complete diﬀraction spectra. It seems almost miraculous when the longer method
eventually reduces to the same simple result. The intuitive method depends on the
fact that since the autocorrelation γω is a volume-normalized convolution of ω = ωV
with itself, its Fourier transform, the diﬀraction pattern ˆγω, should be a normalized
square of ˆω.
In this context, the coeﬃcients of ˆω are usually called amplitudes, even if they
only exist formally, while those of ˆγω are called intensities which relates to the fact
that they are real and non-negative. The appropriate operation now is to determine
the intensities as the absolute squares of the corresponding amplitudes of peaks, as
indicated in the commutative Wiener diagram in Figure 1 where the vertical arrows
represent the Fourier transform, the upper horizontal arrow the volume-normalized
convolution, and the lower horizontal arrow taking the absolute squares of amplitudes.
This observation dates back at least 100 years in optics and is the standard proce-
dure in diﬀraction theory [7]. In the context of diﬀraction from inﬁnite arrangements,
it has been made rigorous (at least for the pure point part of the spectrum) by Hof

18

ˆω

ω
 ˆγω

γω

| · |2

∗

ft ft

✲

✲

❄ ❄

Figure 1: Wiener diagram

[12, 13]. The intuitive approach to the visible points runs through the Wiener diagram
along the “low road”, via the diﬃcult to interpret ˆω.

Visible points

We start from
 ωV =
 ∞∑

m=1 µ(m)ωmΓ\{0} , (45)

which follows from (15) since the sum on the right is supported on Γ \ {0} and the
amplitude of the peak at x ∈ Γ \ {0} is

χV (x) = ∑

m|cont(x) µ(m) . (46)

Although the sum on the right of (46) is ﬁnite for each x, these pointwise sums are
not uniformly convergent, so the sum on the right of (45) does not pass the M-test
of Proposition 2 as a sum of pure point distributions. Nevertheless, it is clear that
the sum does converge to ωV in the weak*-topology (though not in the local norm
topology). Taking the Fourier transform of (45) term-by-term we obtain

ˆωV =
 ∞∑

m=1 µ(m) ( 1
mn ωΓ∗/m − 1) , (47)

where here and in the remainder of this subsection we assume Γ to have unit density,
i.e. vol(Γ) = 1. Since ωV is a tempered distribution it has a Fourier transform ˆωV
which is also a tempered distribution, and since the Fourier transform is a continuous
operator on the space of tempered distributions with the weak*-topology [24] the sum
on the right of (47) converges to ˆωV in the weak*-topology (though again it does not
pass the M-test). This time the sums of the amplitudes at individual points of QΓ∗

are inﬁnite sums but uniformly convergent, when n ≥ 2.

19

It is diﬃcult to interpret (47) as a distribution and we suspect that it is not a
measure. Nevertheless, we can identify the pure points and their amplitudes formally
(even though they may not be real peaks).
Deﬁne the denominator of a non-zero point x ∈ QΓ∗ by

den(x) := gcd{m ∈ Z | mx ∈ Γ∗} (48)

(it is the smallest positive integer such that mx ∈ Γ∗). Then the sum of the amplitudes
in (47) at a point x ∈ QΓ∗\{0} with denominator d is

∞∑

l=1
 µ(ld)
(ld)n = µ(d)
dn
 ∞∑

l=1
(l,d)=1

µ(l)
ln = µ(d)
dn ∏

p̸ |d
 (1 − 1
pn
 )

= µ(d)
ζ(n)dn ∏

p|d
 (1 − 1
pn
 )−1 = µ(d)
ζ(n)
 ∏

p|d
 1
pn − 1 . (49)

When n ≥ 2, the pointwise sum of the pure point parts is thus nonzero at all points
of QΓ∗ with squarefree denominator but is not absolutely locally summable. It is,
however, locally square summable. The squaring operation gives, for the diﬀraction
spectrum ˆγω of V , the distribution with a pure point at each point of QΓ∗ with
squarefree denominator, the peak at such a point with denominator d having intensity

1
ζ 2(n)
 ∏

p|d
 1
(pn − 1)2 . (50)

These coeﬃcients are uniformly absolutely locally summable and in fact are the correct
intensities of the diﬀraction pattern. This will be proved below in Theorem 3. They
were ﬁrst derived, based on similar arguments, in [3]. However, one may well ask why
this works. How can we justify the squaring operation as the appropriate mechanism
for obtaining the intensities? The intuition is supported as follows.

Hof’s results

Two results of Hof [12, 13] are

Proposition 8 Let ν be a translation bounded measure on Rn such that ˆν is also a
translation bounded measure. Then

ˆν({x}) = lim
R→∞ 1
vnRn
 ∫

BR(a) e
−2πix·y ν(dy) (51)

for every x ∈ Rn and the limit exists uniformly in a.

20

Proposition 9 Let ν be a translation bounded measure with natural autocorrelation
γ and suppose that for all x ∈ Rn,

mx := lim
R→∞ 1
vnRn
 ∫
BR(a) e
−2πix·y ν(dy) , (52)

exists uniformly in a. Then, for all x, we have

ˆγ({x}) = |mx|2 . (53)

Taken together, these show that if the Fourier transform ˆν of a translation bounded
tempered distribution ν is also translation bounded (and hence can be decomposed
as a pure point part and a continuous part) then the pure points of the diﬀraction
spectrum ˆγν are the same as the pure points of the Fourier transform ˆν, but their
intensities are the absolute squares of the amplitudes of ˆν. Proposition 9 alone says
that this continues to be true even when ˆν is not translation bounded, at least as
long as the formal expressions for the pure point amplitudes, also called Fourier-Bohr
coeﬃcients, of ˆν (which may now not represent peaks of ˆν in the accepted sense)
converge uniformly with respect to translation of physical space. We shall say more
about the status of the method after giving the analogous intuitive derivation for the
kth-power-free integers.

kth-power-free integers

The parallel intuitive calculation for the pure point part of the diﬀraction spectrum
of the set F = Fk of kth-power-free integers in R goes like this. We have

ωF =
 ∞∑

m=1 µ(m)ωmkZ\{0}, (54)

hence
 ˆωF =
 ∞∑

m=1 µ(m) ( 1
mk ωZ/mk − 1) . (55)

Let dk be the smallest positive integer such that dk
k is divisible by d. We note that
dk is a divisor of d but is divisible by every prime factor of d and that d | m
k if and
only if dk | m. Then the formal sum of the amplitudes of the peaks of (55) at a point
x ∈ Q with denominator d is

∞∑

l=1
 µ(ldk)
(ldk)k = µ(dk)
dk
k
 ∞∑

l=1
(l,d)=1

µ(l)
lk = µ(dk)
ζ(k)dk
k
 ∏

p|d
 (
1 − 1
pk
 )−1 = µ(d∗)
ζ(k)
 ∏

p|d
 1
pk − 1 , (56)

21

since, when dk is squarefree, we have dk = d∗ = ∏

p|d p (the squarefree kernel of d)
and dk
k = ∏
p|d pk. Consequently, the pure point part of the diﬀraction spectrum of F
has peaks at the points of Q with (k + 1)th-power-free denominator, and its intensity
at a such a point, with denominator d, is

1
ζ 2(k)
 ∏

p|d
 1
(pk − 1)2 . (57)

This is a pure point distribution and also agrees with the result of Theorem 5 below.

Status of the method

In the remaining sections of this paper, which contain the heart of the proofs, we
completely avoid Hof’s formula (52) (which in any case could only determine the pure
point part of the spectrum without any assurance that there is no continuous part).
What prevents us from making our derivation of the pure point part of the spectrum
rigorous by citing Proposition 9 is that for our examples the limit in (52) is not
uniform in a. This is most easily seen by noting that our point sets have arbitrarily
large holes, so that no matter how large R is there will be an a such that BR(0) + a
lies entirely within a hole. However, large holes are very sparse, so the limit is, in
a sense, “nearly uniform”. For x ̸∈ QΓ∗ the limit (52) can be shown to be 0 (as it
should be) but again is almost certainly not uniform in a.
The fact that our examples are outside the domain where Hof’s result applies
underscores the fact that we are in new territory not only for calculating the continuous
part of the diﬀraction spectrum but even for calculating the diﬀraction peaks. In other
words: the answer to the question which distributions of matter diﬀract is still largely
unknown.

Autocorrelation of the visible points

The remainder of this paper consists of a rigorous derivation of the results of the
previous section via the “high road” of the autocorrelation. So we begin by using an
elaboration of the kind of M¨obius inversion argument used in proving Proposition 6
to calculate the autocorrelation of the visible points V of a lattice Γ.

Theorem 1 For n ≥ 3, the natural autocorrelation γ of the set V of visible points
of a lattice Γ exists and is supported on Γ, the weight of a point a ∈ Γ in the auto-

22

correlation of V being given by

w(a) = dens(Γ) ξ(n) ∏

p|cont(a)
 (
1 + 1
pn − 2
) , (58)

with error term (as deﬁned just after (11)) equal to O(1/R), where the implied constant
depends on a as well as on Γ.

Proof: By Prop. 5, V − V = Γ, so the autocorrelation of V (if it exists) is supported
on Γ. The weight of a point a ∈ Γ in the autocorrelation of V is the limit as R → ∞
of 1
vnRn ∑

|x|,|x−a|<R
x,x−a∈V

1 (59)

and by Lemma 1 the existence of this limit for each a ∈ Γ is suﬃcient to ensure the
existence of the autocorrelation.
It is convenient to drop the condition |x − a| < R in (59), which then becomes
1
vnRn ∑

|x|<R
x,x−a∈V

1 . (60)

The diﬀerence between these sums is O(1/R), due to the extra lattice points x within
a constant distance |a| of the boundary of BR(0) that are included in the latter. We
note that the latter sum has a natural geometric interpretation as the proportion
of integer points in a large ball that are visible both from the origin and from the
viewpoint a. By (15) and (8), (60) can be expressed as
1
vnRn ∑

x∈Γ\{0,a}
|x|<R
 ∑

l|cont(x) µ(l) ∑

m|cont(x−a)
µ(m) = 1
vnRn ∑

1≤l<S
 ∑

1≤m<S µ(l)µ(m) ∑

x∈Γ\{0,a}
x≡0 (mod lΓ)
x≡a (mod mΓ)
|x|<R
1 , (61)

where S = (R+|a|)/L(Γ). Collecting together terms with the same value of d = (l, m),
noting that all solutions x of the congruences belong to dΓ and that the congruences
have no solution at all unless a ∈ dΓ, and putting l′ = l/d, m
′ = m/d, x′ = x/d,
a′ = a/d, we obtain
1
vnRn ∑

d|cont(a)
 ∑

1≤l′<S/d
 ∑

1≤m′<S/d
(l′,m′)=1
 µ(l′d)µ(m
′d) ∑

x′∈Γ\{0,a′}
x′≡0 (mod l′Γ)
x′≡a′ (mod m′Γ)
|x′|<R/d

1 . (62)

23

Since l′ and m
′ are bound variables of summation and x′ and a′ will not be referred
to again, we can drop the dashes: from now on l and m are the new l′ and m
′ but a
is the original a.
By Propositions 2 and 1 (with lmΓ in place of Γ) the inmost sum is

dens(Γ) vn
 ( R
dlm
)n + O ( R
dlm
)n−1 + O(1) (63)

These three terms give a main term and two error terms in (62).
The ﬁrst error term is majorized by

O
 ( 1
R
 ∑

1≤l<S
 1
l(n−1) ∑

1≤m<S
 1
m(n−1)
 )
 = { O(1/R), if n ≥ 3,
O((log S)2/R), if n = 2, (64)

since the sums are convergent when n − 1 ≥ 2 and increase logarithmically when
n − 1 = 1.
The second error term is majorized by O(S2/Rn) = O(1/Rn−2). So when n ≥ 3
both error terms are O(1/R) (since S = O(R)) and tend to 0 as R → ∞.
The main term is (with D = dens(Γ))

D ∑

d|cont(a)
 ∑

1≤l<S/d
 ∑

1≤m<S/d
(l,m)=1
 µ(ld)µ(md)
(dlm)n = D ∑

d|cont(a)
 ∑

1≤l<S/d
(l,d)=1
 ∑

1≤m<S/d
(m,d)=1
(l,m)=1
 µ2(d)µ(l)µ(m)
(dlm)n (65)

since µ(ld) is µ(l)µ(d) when (l, d) = 1 and 0 otherwise, and similarly for µ(md),

= D ∑

d|cont(a)
 µ2(d)
dn ∑

1≤l<S/d
(l,d)=1
 ∑

1≤m<S/d
(m,d)=1
 µ(lm)
(lm)n (66)

since µ(l)µ(m) is µ(lm) when (l, m) = 1 and 0 otherwise

−→ D ∑

d|cont(a)
 µ2(d)
dn
 ∞∑

r=1
(r,d)=1

µ(r)σ(r)
rn as R → ∞ (67)

since the double sum is absolutely convergent. The diﬀerence between this limit and
the partial sum (66) is O(1/Rn−1), so falls within the error term estimate O(1/R).

24

Using (19), the expression for the limit (67) can be rearranged as

D ∑

d|cont(a)
d squarefree
1
dn ∏

p̸ |d
 (
1 − 2
pn
 ) = D ξ(n) ∑

d|cont(a)
d squarefree

1
dn ∏

p|d
 (1 − 2
pn
 )−1 (68)

= D ξ(n) ∏

p|cont(a)
 (
1 + 1
pn
 (
1 − 2
pn
 )−1)
 = D ξ(n) ∏

p|cont(a)
 (
1 + 1
pn − 2
) .

This completes the proof. □
To establish the existence of the autocorrelation function for the visible points
when n = 2, we need to reduce the second error term in the above proof. This we
do by modifying the argument slightly, ﬁrst using the characteristic function (15) to
replace the constraint on x − a only, then discarding large values of m from the sum
before using (15) again to replace the constraint on x.

Theorem 2 Theorem 1 holds for n = 2 with the error term increased to O(1/√
R).

Proof: Using (15) to replace the constraint on x − a, (60) becomes

1
πR2 ∑

x∈V
x̸=a
|x|<R
 ∑

m|cont(x−a) µ(m) = 1
πR2 ∑

1≤m<S µ(m) ∑

x∈V
x̸=a
x≡a (mod mΓ)
|x|<R
 1 , (69)

where S is as before. The inner sum is trivially O(R2/m
2) (since m < S = O(R)) so
the contribution to (60) from the terms with m ≥ √R is

O( ∑

m≥√R
 1
m2
 ) = O(1/√
R) . (70)

For the terms in (69) with m < √R we use the characteristic function (15) to replace
the constraint on x, obtaining

1
πR2 ∑

1≤m<√R µ(m) ∑

x∈Γ\{0,a}
x≡a (mod mΓ)
|x|<R
 ∑

l|cont(x)
µ(l) = 1
πR2 ∑

1≤l<S
 ∑

1≤m<√R µ(l)µ(m) ∑

x∈Γ\{0,a}
x≡0 (mod lΓ)
x≡a (mod mΓ)
|x|<R

1 . (71)

25

This is now identical to (61), except that the second S is replaced by √R, and as
before contributes to (60) a main term that tends to

D ξ(2) ∏

p|cont(a)
 (1 + 1
p2 − 2
) (72)

as R → ∞ and two error terms O((log R)2/R) and O(1/√
R). The diﬀerence between
the main term and its limit is also O(1/√
R). So the total error term is majorized by
O(1/√
R). □
Note that this modiﬁed argument does not reduce the error term when n ≥ 3,
which contains a term O(1/R) arising from the boundary of the ball when l = m = 1.
For n = 2, a similar but more complicated argument gives an improved error term
O(R−3/4(log R)c) for some constant c, but we do not need this here.
Remark Theorems 1 and 2 show that the weight w(a) in the autocorrelation of
V (also called the autocorrelation coeﬃcient8) depends only on the content of a and
the density of Γ. This enables us to calculate how the application of a non-singular
linear transformation T to V aﬀects the autocorrelation of V . Clearly T preserves
content, in the sense that, for any lattice Γ and x ∈ Γ, the content of T x as a vector
of T Γ is equal to the content of x as a vector of Γ. In particular, T V is the set of
visible points of T Γ. The autocorrelation of T V is supported on T Γ and (58) shows
that
 wT V (T a) = dens(T Γ)
dens(Γ) wV (a) = 1
| det T | wV (a) , (73)

where the suﬃx on w indicates which autocorrelation it is associated with. Thus the
autocorrelation of T V is | det T |−1 times the T -image of the autocorrelation of V .
The direct way of calculating wT V (T a) from (59) is

wT V (T a) = lim
R→∞ 1
vnRn ∑

x,x−T a∈RB∩T V
1 , (74)

where B = B1(0) is the unit ball in Rn, and substituting this in (73) gives

wV (a) = lim
R→∞ | det T |
vnRn ∑

y,y−a∈RT −1B∩V
1 = lim
R→∞ 1
vol(E)Rn ∑

y,y−a∈RE∩V
1 , (75)

8Note that w(a) can also be interpreted as the density of lattice points that are simultaneously
visible both from the origin and from the lattice point a. Extending this to the condition of simul-
taneous visibility from an arbitrary (but ﬁnite) set of points of Γ results in higher order correlation
coeﬃcients, see [5] for some recent results.
 26

where E = T −1B is an ellipsoid. Hence averaging over the expanding ellipsoid RE
gives the same value for the autocorrelation of V as using the natural density and
averaging over an expanding ball. The choice of ellipsoid here is completely arbitrary,
since for any E there is a linear transformation T with T E = B. In the Appendix
this is generalized further and we show how to replace E by any bounded measurable
region (not necessarily centred at 0) with ﬁnite (n − 1)-dimensional surface area.

Diﬀraction spectrum of the visible points

The ﬁnal step in obtaining the diﬀraction spectrum of the visible points V is to take
the Fourier transform of the autocorrelation of V .

Theorem 3 The diﬀraction spectrum of the set of visible points of an n-dimensional
lattice Γ (with n ≥ 2) exists and is a pure point measure which is concentrated on the
set of points in QΓ∗ with squarefree denominator and whose intensity at a point with
such a denominator q is given by

dens(Γ)2

ζ 2(n)
 ∏

p|q
 1
(pn − 1)2 . (76)

This measure can also be represented as

dens(Γ)2 ξ(n)
 ∞∑

d=1
d squarefree

(∏

p|d
 1
p2n − 2pn
 )ωΓ∗/d , (77)

a weak*-convergent sum of Dirac combs.

Proof: Let γ be the autocorrelation of V . The right hand side of (68) can be
expressed in the form (again, with D = dens(Γ))

w(a) = D ξ(n)
 ∞∑

d=1
d squarefree
a∈dΓ
 1
dn ∏

p|d
 (
1 − 2
pn
 )−1 . (78)

So by Theorems 1 and 2 and Lemma 1

γ = D ξ(n)
 ∞∑

d=1
d squarefree

1
dn ∏

p|d
 (1 − 2
pn
 )−1 ωdΓ . (79)

27

Since ∥ωdΓ∥loc = O(1) and the coeﬃcient of ωdΓ is O(1/dn) when n ≥ 2, this
sum of tempered distributions is convergent in the weak*-topology by Lemma 2 (and
this is easy to see by other means in this case, where the resulting sum is uniformly
discrete). Its term-by-term Fourier transform is

D2 ξ(n)
 ∞∑

d=1
d squarefree

1
d2n ∏

p|d
 (
1 − 2
pn
 )−1 ωΓ∗/d, (80)

which weak*-converges to the diﬀraction spectrum of V , since the Fourier transform
operator is weak*-continuous. Since ∥ωΓ∗/d∥loc = O(dn) and the coeﬃcient of ωΓ∗/d is
O(1/d2n), Lemma 2 tells us that the weak*-sum is a translation bounded pure point
measure equal to the pointwise sum of its terms.
This establishes the series form (77) for the diﬀraction spectrum. The explicit
values of the intensities can now be evaluated quite simply. Let p be a point in QΓ∗

with denominator q. We can suppose that q is square-free, since otherwise there is no
contribution to (77) at all. The terms in (77) that contribute to the intensity at p are
those with d = mq (m squarefree in Z
+ and prime to q), so the intensity at p is

D2 ξ(n) ∏

p|q
 1
p2n − 2pn
 ∞∑

m=1
m squarefree
(m,q)=1

∏

p|m
 1
p2n − 2pn . (81)

This simpliﬁes to

D2 ξ(n) ∏

p|q
 1
p2n − 2pn ∏

p̸ |q
 (
1 + 1
p2n − 2pn
 )

= D2 ξ(n) ∏

p|q
 1
p2n
 (1 − 2
pn
 )−1 ∏

p̸ |q
 (1 − 1
pn
 )2(
1 − 2
pn
 )−1

= D2

ζ 2(n)
 ∏

p|q
 1
p2n
 (
1 − 1
pn
 )−2 (82)

(using the Euler products in (18) and (19)) which agrees with (76). □
An explicit example of the diﬀraction (for Γ = Z
2) is shown in [3], and compared
with an optical experiment. The diﬀraction image in this case is both D4-symmetric
and GL(2, Z) invariant which results in a beautiful image with a rather unusual sym-
metry structure, reminiscent of self-similar patterns common in fractals.

28

kth-power-free numbers

In this section we derive the diﬀraction spectrum of the 1-dimensional set F consisting
of the kth-power-free numbers in Z. Again, this has arbitrarily long gaps but it
nevertheless has a pure point diﬀraction spectrum. The proof of the second assertion
closely parallels the corresponding proof for the visible points V in the previous two
sections, with the parameter k for F playing the rˆole of the dimension n of V in the
formalism. There are some diﬀerences of detail, however, particularly with the error
terms.
Let us note here that the results on the autocorrelation derived below also follow
from [22] (k = 2) and from [19, Thm. 1], where also more general correlation functions
have been derived. The error term given in [19] is O(R−1+2/(k+1)), which is slightly
better than the error term we derive in Theorem 4. We include our proof to make this
paper self-contained and to show up the close parallel between visible lattice points
and k-free numbers.

Proposition 10 F is uniformly discrete, but has gaps of arbitrary length. Moreover,
for any L > 0 the set of gaps of length at least L has positive density.

Proof: The uniform discreteness is trivial since F ⊂ Z. Choose L integer moduli
m1, . . . , mL that are > 1 and coprime in pairs (for example, the ﬁrst L primes). By
the Chinese Remainder Theorem there is an integer N with

N ≡ −j + 1 (mod m
k
j ) for j = 1, . . . , L. (83)

Now for x ≡ N (mod m
k
1m
k
2 . . . m
k
L) we have m
k
1 | x, m
k
2 | (x + 1),. . . , m
k
L | (x + L − 1),
so none of the numbers x, x + 1, . . . , x + L − 1 is kth-power-free. The numbers x have
density (m1m2 . . . mL)−k. □
This argument gives a distance of the order L
kL between gaps of length L, so again
long gaps can be expected to be extremely sparse. Nevertheless, gaps of length L have
a deﬁnite frequency (its expression in terms of Dirichlet series can be extracted from
[19]). It is interesting to note that the corresponding distribution is not Poissonian,
but that these frequencies decline faster than exponentially in L [15, 9].

Proposition 11 For k ≥ 2, the kth-power-free integers F have a natural density
given by
 dens(F ) = 1
ζ(k) , (84)

with error term O(R−1+(1/k)).
 29

At least for the squarefree numbers, this is again a standard example of M¨obius
inversion, see [14, Thm. 6.6.1].
Proof: The natural density of F is the limit as R → ∞ of

1
2R
 ∑

|x|<R
x∈F
 1 , (85)

which by (16) is
 1
2R
 ∑

|x|<R
x̸=0
 ∑

mk|x
µ(m) = 1
2R
 ∑

1≤m<R1/k µ(m) ∑

|x|<R
x≡0 (mod mk)
x̸=0
 1 (86)

= ∑

1≤m<R1/k
 µ(m)
mk + O (R1/k

R
 ) ,

since the inner sum on the right of (86) is 2R/m
k + O(1). This last expression tends
to 1/ζ(k) as R → ∞ when n ≥ 2, with the errors due to the tail of the sum and to
the explicit error term both O(R−1+(1/k)). □

Theorem 4 For k ≥ 2, the natural autocorrelation of the set F of kth-power-free
integers exists and is supported on Z, the weight of an integer a in the autocorrelation
of V being given by
 w(a) = ξ(k) ∏

pk|a
 (1 + 1
pk − 2
 ) , (87)

with error term O(R−(1−(1/k))2), where the implied constant depends on a.

Proof: Clearly the autocorrelation is supported on Z. The weight of an integer a in
the autocorrelation of F is the limit as R → ∞ of
1
2R
 ∑

|x|,|x−a|<R
x,x−a k-free

1 (88)

and, as in the proof of Theorem 1, to show the existence of the autocorrelation it is
enough to show that this limit exists for every a. Again as in the proof of Theorem 1,
we can drop the condition |x − a| < R from the sum to obtain

1
2R
 ∑

|x|<R
x,x−a k-free

1 (89)

30

with error O(1/R).
This can be evaluated by an argument exactly parallel to that for the visible points,
using the characteristic function (16) in place of (15). We use the argument in the
modiﬁed form we used in the proof of Theorem 2 since, in the context of kth-power-
free numbers, it gives an improved error term in all cases owing to the fact that, for a
1-dimensional set, errors due to the boundary of a large region are trivial. (Using the
unmodiﬁed form would give error term O(R−1+(2/k)) instead of the O(R−1+(2/k)−(1/k)2)
we obtain here. As with the visible points, this would not be small enough to establish
the existence of the limit for the squarefree numbers k = 2 — the paradigm case.)
Using the characteristic function (16) to replace the constraint on x − a, (89)
becomes 1
2R
 ∑

|x|<R
x k-free
x̸=a
 ∑

mk|(x−a) µ(m) = 1
2R
 ∑

1≤m<S1/k µ(m) ∑

|x|<R
x k-free
x̸=a
x≡a (mod mk)

1 , (90)

where S = R + |a|. The inner sum is trivially O(R/m
k) (since m
k < S) so the
contribution to (89) from the terms with m ≥ T , where T is a parameter tending to
inﬁnity with R to be chosen later, is

O( ∑

m≥T
 1
mk
 ) = O(T 1−k) . (91)

For the terms in (90) with m < T we use the characteristic function (16) to replace
the constraint on x, obtaining

1
2R
 ∑

1≤m<T µ(m) ∑

|x|<R
x̸=0,a
x≡a (mod mk)

∑

lk|x µ(l) = 1
2R
 ∑

1≤l<R1/k
 ∑

1≤m<T µ(l)µ(m) ∑

|x|<R
x̸=0,a
x≡0 (mod lk)
x≡a (mod mk)

1 . (92)

Collecting together terms with the same value of d = (l, m), noting that all solutions
x of the congruences are divisible by dk and that the congruences have no solution
unless dk | a, and putting l′ = l/d, m
′ = m/d, x
′ = x/dk, a
′ = a/dk, we obtain

1
2R
 ∑

dk|a
 ∑

1≤l′<R1/k/d
 ∑

1≤m′<T /d
(l′,m′)=1
 µ(l′d)µ(m
′d) ∑

|x′|<R/dk

x′̸=0,a′

x′≡0 (mod l′k)
x′≡a′ (mod m′k)

1 . (93)

31

As in the proof of Theorem 1, we can drop the dashes from now on.
By the Chinese Remainder Theorem the inner sum is

2R
(dlm)k + O(1) , (94)

giving a main term and another error term in (89).
The error term is majorized by O(R−1+(1/k)T ).
The main term is
∑

dk|a
 ∑

1≤l<R1/k/d
 ∑

1≤m<T /d
(l,m)=1
 µ(ld)µ(md)
(dlm)k

= ∑

dk|a
 ∑

1≤l<R1/k/d
(l,d)=1
 ∑

1≤m<T /d
(m,d)=1
(l,m)=1
 µ2(d)µ(l)µ(m)
(dlm)k (95)

since µ(ld) is µ(l)µ(d) when (l, d) = 1 and 0 otherwise, and similarly for µ(md),

= ∑

dk|a
 µ2(d)
dk ∑

1≤l<R1/k/d
(l,d)=1
 ∑

1≤m<T /d
(m,d)=1
 µ(lm)
(lm)k (96)

since µ(l)µ(m) is µ(lm) when (l, m) = 1 and 0 otherwise

−→ ∑

dk|a
 µ2(d)
dk
 ∞∑

r=1
(r,d)=1

µ(r)σ(r)
rk as R → ∞ (97)

since the double sum is absolutely convergent. The diﬀerence between this limit
and the partial sum (96) is O(1/R−(k−1)/k) + O(T −(k−1)) and each of these terms is
subsumed by one of the error estimates we already have.
This last expression is

∑

dk|a
d squarefree

1
dk ∏

p̸ |d
 (
1 − 2
pk
 ) = ξ(k) ∑

dk|a
d squarefree

1
dk ∏

p|d
 (
1 − 2
pk
 )−1 (98)

= ξ(k) ∏

pk|a
 (
1 + 1
pk
 (
1 − 2
pk
 )−1)
 = ξ(k) ∏

pk|a
 (1 + 1
pk − 2
 ) .

32

Finally, we choose T = R(1/k)−(1/k)2 , making both error terms O(R−1+(2/k)−(1/k)2). □
We can now ﬁll a small gap in our analogy by the following result.

Corollary 1 For k ≥ 2, we have F − F = Z.

Proof: Since F − F ⊂ Z, γω is clearly supported on Z. From Theorem 4, we get
w(a) > 0 for all a ∈ Z, hence also Z ⊂ F − F . □
Let us ﬁnally describe the diﬀraction of kth-power-free integers.

Theorem 5 The diﬀraction spectrum of the set F of kth-power-free integers exists
and is a pure point measure. It is supported on the set of numbers a/q ∈ Q with q
being (k + 1)-power-free. The diﬀraction intensity at a point with such a denominator
q is 1
ζ 2(k)
 ∏

p|q
 1
(pk − 1)2 . (99)

This measure can also be represented as

ξ(k)
 ∞∑

d=1
d squarefree

(∏

p|d
 1
p2k − 2pk
 )ωZ/dk , (100)

a weak*-convergent sum of Dirac combs.

Proof: As in the proof of Theorem 3, it follows from (98) that

γ = ξ(k)
 ∞∑

d=1
d squarefree

1
dk ∏

p|d
 (
1 − 2
pk
 )−1 ωdkZ , (101)

where γ is the autocorrelation of F and this sum of tempered distributions is conver-
gent in the ∥ · ∥loc-topology for k ≥ 2. Its term-by-term Fourier transform is

ξ(k)
 ∞∑

d=1
d squarefree

1
d2k ∏

p|d
 (
1 − 2
pk
 )−1 ωZ/dk , (102)

where the sum of the local norms of the terms is convergent, so by Lemma 2 (102)
weak*-converges to a translation bounded pure point measure equal to the pointwise
sum of its terms. Since the Fourier transform operator is weak*-continuous this pure
point distribution is the diﬀraction spectrum of F .

33

This establishes (100). To obtain (99) we note that the terms in (100) that con-
tribute to the intensity at a/q (where q has to be (k + 1)-free) are those with d = mq∗,
where q∗ is the square-free kernel of q and m ∈ Z
+ is square-free and prime to q. Thus
the intensity at a/q is
 ξ(k) ∏

p|q
 1
p2k − 2pk
 ∞∑

m=1
m squarefree
(m,q)=1

∏

p|m
 1
p2k − 2pk . (103)

This is (81) without the factor D2 and with n replaced by k, so reduces to (99). □

Further connections and directions

Above, we have emphasized that the sets of visible lattice points VΓ and the set of
k-th-power-free numbers Fk diﬀer from any regular model set (see [18, 20, 27, 28] for
deﬁnitions and properties) by a set of positive density, suggesting that they cannot be
obtained from the cut-and-project construction in any natural way. However, there is
a way of obtaining these sets by cut-and-project using the rational adeles instead of
Euclidean space as the hyperspace (or embedding space) and using windows which,
although they have empty interior, are quite natural sets in this context. From this
point of view, VΓ and Fk are “super-singular” model sets. This comes about because
these sets are the result of sieving over primes: Fk, for example, is what remains of Z
after removing the zero residue class mod pk for each p.
The cut-and-project construction can be pictured like this.

B π
←− A πint−→ C
∪
L (104)

Usually the hyperspace A is Rn+m, with the physical space B = Rn and the internal
space C = Rm being complementary subspaces having π and πint as the associated
projections with kernels C and B respectively, and L being a lattice in A whose images
in B and C are dense. A bounded acceptance domain or window Ω ⊂ C is chosen
and the model set in B is

Λ = Λ(Ω) := {π(x) | x ∈ L , πint(x) ∈ Ω} . (105)

Then Λ is a uniformly discrete set, and also relatively dense if Ω has non-empty
interior. When B and C are orthogonal and Ω is a simple region we have

dens(Λ) = vol(Ω)dens(L) = vol(Ω)/vol(FL), (106)

34

where FL is a fundamental region of L. This construction admits the generalization
where A is allowed to be an arbitrary locally compact Abelian group and L a discrete
subgroup with A/L compact (so that L plays the rˆole of a lattice), see [20] and refer-
ences therein. It is well known [18, 20, 27] that, even in this more general situation,
Λ(Ω) is relatively dense if Ω has non-empty interior and possesses a uniform density
if, in addition, ∂Ω has Haar measure 0, see [13, 27] for details.
To obtain the kth-power-free numbers, we take A to be the ring of rational adeles
AQ. Let us explain what this is. (For the technical details and background to p-adic
numbers and adeles see [6], which deals with the case of a general algebraic number
ﬁeld in place of Q.) Given a prime p ∈ Z
+ the p-adic valuation on Q is deﬁned,
for q ̸= 0, by |q|p = p−r, where q = pra/b with r ∈ Z and a, b not divisible by p.
This satisﬁes not only the triangle inequality but the stronger inequality |q1 + q2|p ≤
max{|q1|p, |q2|p}. (Such valuations are called non-Archimedean.) The ﬁeld Qp of p-
adic numbers is the completion of Q with respect to | · |p (analogous to R being the
completion of Q with respect to the ordinary absolute value) and is locally compact
in the p-adic topology. In view of the strong triangle inequality, the p-adic numbers a
with |a|p ≤ 1 form a ring Zp, called the p-adic integers. (It is the closure of Z in Qp.)
For any p-adic number b ̸∈ Zp the p-adic open ball {a | |a − b|p < 1} is disjoint from
Zp. Hence Zp is closed in Qp and, since it is bounded, also compact. But Zp is the
disjoint union of the p open balls {a | |a−i|p < 1} with i = 1, . . . , p, hence is also open
in Qp. As a locally compact Abelian group under addition, Qp has a Haar measure,
unique up to a multiplicative constant, which can be normalized so that vol(Zp) = 1.
Any ﬁxed power of a non-Archimedean valuation is also a valuation, and topolog-
ically equivalent; but up to this equivalence the p-adic valuations and the ordinary
absolute value are the only valuations on Q. The rational adele ring AQ is the re-
stricted direct product with respect to the Zp’s of the completions of Q with respect
to these valuations, i.e.

AQ = {
α = (α∞, (αp)) | α∞ ∈ R, αp ∈ Qp, and αp ∈ Zp
for all except ﬁnitely many p.
 } (107)

and has the restricted product topology for which the sets O∞ × ∏
p Op, with O∞
open in R, Op open in Qp and Op = Zp for all except ﬁnitely many p, form a base of
open sets. As a restricted product of locally compact sets with respect to compact
sets, AQ is locally compact.
Now Q embeds in AQ diagonally (i.e. each q ∈ Q can be identiﬁed with the adele
all of whose components are q), and with this identiﬁcation Q is discrete in AQ and
AQ/Q is compact. A fundamental region for Q in AQ is [0, 1] × ∏

p Zp, which has

35

volume 1 in the normalized Haar measure on AQ. This gives rise to the interesting
and natural cut-and-project scheme

R π
←− AQ πint−→ ∏

p (Zp) Qp
∪
Q (108)

with componentwise projections and ∏
(Zp) denoting the restricted product. The image
π(Q) is, of course, dense in R and the denseness of πint(Q) in ∏ Qp is equivalent to
the Strong Approximation Theorem [6, §15]. If we choose for the window the closed
and open set Ω := ∏

p Zp we obtain the model set Λ(Ω) = Z ∈ R. Since vol(Ω) = 1 in
the normalized Haar measure on ∏ Qp and dens(Z) = 1 we notice that this satisﬁes
(106). If instead we choose Ω := ∏

p(Zp \ pkZp) with k ≥ 2 we obtain the “thin”
model set Λ(Ω) = Fk. We say “thin” because, being not relatively dense, Fk is not a
regular model set. The reason that Schlottmann’s result does not apply here is that
Ω has empty interior: Ω contains no basic open set because it projects to a proper
subset of Zp in every non-Archimedean component, whereas basic open sets project
to Zp in all except ﬁnitely many components. Nevertheless, Ω has a positive volume
in the normalized Haar measure on ∏ Qp given by

vol(Ω) = ∏

p vol(Zp \ pkZp) = ∏

p
 (1 − 1
pk
 ) = 1
ζ(k) , (109)

which, in view of Proposition 11, agrees with (106). This is astonishing and we have
no explanation for it at present, since merely by translating Ω we can not only reduce
the density of Λ to 0 but can cause Λ to vanish altogether. Let i : P → Z, where
P is the set of positive primes, be any one-one correspondence, and for each p ∈ P
choose αp ∈ Zp with αp ≡ i(p) (mod pk). Then the window Ω + α ⊆ ∏ Zp, where
α = (αp) ∈ ∏ Qp, leads to the empty set under the cut-and-project construction
because each i ∈ Z is excluded mod pk for the corresponding p.
The visible points VΓ of a lattice Γ ⊂ Rn, for n ≥ 2, can be obtained by a similar
construction, using (AQ)n, which is topologically isomorphic to the restricted product
with respect to Z
n
p A := Rn × ∏

p (Zn
p ) Q
n
p . (110)

Choose a basis {b1, . . . , bn} of Γ and embed QΓ in A by

x = q1x1 + · · · + qnxn ↦→ (x, ((q1, . . . , qn)p)) , (111)

36

where (q1, . . . , qn)p = (q1, . . . , qn) for each p. (In the terminology of commutative
algebra, this establishes that A is isomorphic to Γ ⊗Z AQ, the AQ-iﬁcation of the
Z-module Γ, see [16] under the index entry “iﬁcation”). Then the image of QΓ is a
discrete subgroup of A and A/QΓ is compact with F = FΓ × ∏ Z
n
p as a fundamental
region, where FΓ is a fundamental region of Γ in Rn. The volume of this fundamental
region in the normalized Haar measure on A is 1/dens(Γ). This gives the cut-and-
project scheme Rn π
←− (AQ)n πint−→ ∏

p (Zn
p ) Q
n
p
∪
QΓ (112)

with the images of QΓ under π and πint being dense. If we choose for the window the
closed and open set Ω := ∏

p Z
n
p we obtain the model set Λ(Ω) = Γ ⊂ Rn which has
vol(Ω) = 1 and satisﬁes (106). If we choose Ω := ∏

p(Z
n
p \ pZ
n
p ) we obtain Λ(Ω) = VΓ.
Again, Ω has empty interior but positive volume, given by

vol(Ω) = ∏

p
 (
1 − 1
pn
 ) = 1
ζ(n) (113)

so that (106) holds by Proposition 6. Again, translating Ω can cause the model set
to vanish. A translation α ∈ ∏ Q
n
p that does this can be constructed as follows: let
i : P → Z
n be any one-one correspondence and for each p choose αp ≡ i(p) (mod p);
then take α = (αp).
These adelic constructions are nothing more than number theoretic sieves which
exclude certain residue classes modulo a power of each prime. The choice of window
determines the residue classes to be retained and translating the window changes the
set of residue classes without changing their number. Clearly, many other examples
of the same type can be constructed.
If VΓ and Fk were regular model sets, we would be able to use standard results
on model sets to derive their diﬀractiveness [28], but the constructions just described
are outside the range of current diﬀraction results. To the best of our knowledge, the
diﬀraction of adelic model sets has not been studied, which is why we have had to
derive our diﬀraction results from scratch.
Obviously, one further question is how relevant the examples are. Is the set of
visible lattice points an isolated example, or more of a paradigm case of a family
of examples with pure point diﬀraction? We believe the latter is true, and there is
one immediate class of examples that springs to mind. If we view the visible points
of Z
2 as the orbit of (1, 0) under the group SL(2, Z), it is clear that this orbit, in
general, will split into several pieces when SL(2, Z) is replaced by one of the standard

37

congruence subgroups. However, our methods are robust under further congruence
constraints, and so it is clear that there is a large class of congruence subsets of the
visible points which will have interesting diﬀraction spectra.
We hope to report on some examples soon.

Summary

We have demonstrated that the set of visible lattice points in dimensions n ≥ 2 and
the set of kth-power-free integers with k ≥ 2 both possess well-deﬁned autocorrela-
tions and pure point diﬀraction spectra. We have shown how to replace the intuitive
but incomplete derivation of the spectra by a rigorous number theoretical argument
based on explicit computation of the autocorrelation followed by Fourier inversion
and repeated application of the Poisson summation formula.

Acknowledgements

It is our pleasure to thank Martin N. Huxley for several useful hints on the literature
of k-free integers and Martin Schlottmann for a number of clarifying discussions. This
work was supported by the German Research Council (DFG) and the Natural Sciences
and Engineering Council of Canada (NSERC).

38

Appendix

This paper has required several calculations of densities of discrete point sets, for
which we have used natural density. The natural density is in fact nowhere near as
natural as one would expect from its name. Here we brieﬂy examine the drawbacks
of the natural density and also the uniform density, and suggest a simply stated
deﬁnition of density, intermediate between natural density and uniform density, that
is applicable to sets of the kind we encounter here. A fuller exposition will appear
elsewhere [23].
As an aid to describing the behaviour of densities we begin by introducing some
standard measurements of measurable sets in Rn.

Measurements of measurable sets

For a bounded, measurable set R in Rn we denote by V (R) the volume of R (that
is, its n-dimensional measure). Given ǫ > 0 we denote by ∂ǫR the set of points in
Rn whose distance from the boundary of R is less than ǫ. Then ∂ǫR is open, hence
measurable, so also has a volume. We temporarily call a set R good if

(a) R is bounded and measurable, and

(b) V (∂ǫR)/ǫ is bounded as ǫ → 0.

For good sets we can deﬁne the functions

V = V (R), (114)

M = M(R) = sup
x∈R |x|, (115)

R = R(R) = inf
c∈Rn sup
x∈R |x − c|, (116)

S = S(R) = sup
0<ǫ≤R
{V (∂ǫR)/2ǫ}. (117)

The following relations are immediate from these deﬁnitions:

R ≤ M, V ≤ vnRn, RS ≥ 2n−1V, S ≥ vnRn−1/2, (118)

where vn is the volume of the unit ball in Rn.
Each of these functions is invariant under Euclidean transformations and scales
homogeneously with dilation of R: M and R proportionally to the dilation factor λ,

39

V proportionally to λn and S proportionally to λn−1. They are aﬀected by a non-
singular aﬃne transformation A = T + t (where T is linear and t is a translation) as
follows:
 V (A(R)) = | det T | V (R), (119)

M(A(R)) ≤ ∥T ∥ M(R) + |t|, (120)

R(A(R)) ≤ ∥T ∥ R(R), (121)

S(A(R)) ≤ 2n| det T | ∥T ∥n−1∥T −1∥nS(R). (122)

Of these functions, V , M and R are straightforward, representing the volume,
the maximum distance from the origin and the circumradius of R, respectively. The
function S is a substitute for the surface area of R and in fact is always greater than
or equal to the (n−1)-dimensional measure of the boundary ∂R. The condition ǫ ≤ R
in its deﬁnition is arbitrary, but ensures the scaling of S under dilations mentioned
above. (Using any ﬁxed multiple of R would have the same eﬀect.)
These functions extend to arbitrary measurable sets if we deﬁne M = R = ∞
when R is unbounded (in which case V may or may not be inﬁnite) and S = ∞ when
(b) fails. We note that V (∂ǫR) is inﬁnite for every ǫ when R is an unbounded set of
ﬁnite volume, so S = ∞ for every set of ﬁnite volume that is not good.

Densities of discrete sets

Let X be a locally ﬁnite set of points in Rn, that is, every bounded region of Rn

contains only ﬁnitely many points of X. Here we compare ways of deﬁning a density
for such a set X.

Uniform density

X has uniform density D = D(X) if

|{x ∈ X | |x − c| < R}| = DvnRn + o(Rn) as R → ∞ (123)

uniformly in c.
It is immediate from this deﬁnition that
(i) uniform density is invariant under Euclidean transformations.
A less immediate consequence is that if R is an arbitrary measurable set in Rn and
f (V ) is any function of V (no matter how slowly increasing) that tends to inﬁnity
with V then

|R ∩ X| = DV (R) + o(
V (R)) + O(
f (V (R))S(R)) as V (R) → ∞. (124)

40

A consequence of (124) is
(ii) uniform density is independent of shape;
that is, if X has uniform density D then (123) continues to hold, with the same value
of D, when the sphere |x − c| < R is replaced by an expanding set of any other shape
and vn is replaced by the volume of the set in the family that has R = 1.
Another consequence of (124) (using (119) and (122) to control the error terms)
is
(iii) uniform density varies as the reciprocal of the determinant under non-singular
aﬃne transformations.
All crystals and most quasicrystals possess a uniform density. However, the set
V of the visible points of a lattice Γ does not. In fact Proposition 6 shows that the
number of points of V in a ball of radius R with centre 0 is (dens(Γ)/ζ(n))vnRn+o(Rn),
whereas Proposition 5 shows that there are arbitrarily large balls that contain no
points of V . Similarly, the set Fk of kth-power-free integers in R does not possess a
uniform density either. Consequently uniform density is of no use for the questions
considered in this paper—in fact none of the sets whose densities we require possesses
a uniform density.
A deﬁnition of density known as van Hove density is implicit in Ch. 2 of [26], if the
identical formulæ (3.3) and (3.8) of [26, Ch. 2] are regarded as deﬁning the density
of a general potential operator Φ. This is equivalent to uniform density. The fact
that uniform density implies van Hove density follows from (124) and the converse
implication results from choosing the van Hove sets to be balls.

Natural density

As deﬁned in (10) for uniformly discrete sets, X has natural density D = D(X) if

|{x ∈ X | |x| < R}| = DvnRn + o(Rn) as R → ∞. (125)

This is often called asymptotic density in the context of number theory.
Like uniform density, natural density is
(i) invariant under Euclidean transformations.
(Tranlation invariance is easy to derive, though not quite as immediate as for uniform
density.) However, natural density is not independent of shape and does not transform
naturally under linear transformations. For example, let X = {(x, y) | x, y ∈ Z, |y| <
2|x|} be the set of points in Z
2 that lie in the double wedge with angle 2 tan
−1 2. The
natural density of X is (2/π) tan
−1 2 = 0.7048 . . . , but the proportion of the integer
points in the square {(x, y) | |x|, |y| < R} that belong to X is 3/4 and the proportion

41

of the integer points in the square {(x, y) | |x| + |y| < R} that belong to X is 2/3.
So for this set, counting points according to the L
2, L
∞ or L
1 norm in R2 gives three
distinct answers. The linear map T (x, y) = (2x, y) transforms X into the set of integer
points with x-coordinate even in the double wedge {(x, y) | x, y ∈ Z, |y| < |x|} with
angle π/2. This set has density 1/4, which is not a half of (2/π) tan
−1 2, showing that
natural density does not transform naturally under linear maps.
For the sets we deal with in this paper natural density does not exhibit such
pathological behaviour. For example, Proposition 6, Theorem 1 and Theorem 2, which
establish the densities of certain subsets of a lattice Γ in Rn, all give a factor dens(Γ)
as the only dependency of the density on the lattice, conﬁrming that the density
varies as the reciprocal of the determinant under linear transformations. However,
rather than having to verify this in each individual case, as in eﬀect we have done
here, it would be preferable to have a deﬁnition of density with strength intermediate
between uniform density and natural density for which non-pathological behaviour is
guaranteed.

Tied density

It is possible to deﬁne an alternative form of density, intermediate between uniform
density and natural density, that overcomes these diﬃculties. This depends on the
idea of making uniform density less free of the origin by replacing R by M in the error
term of (123). We say that X has tied density D = D(X) if for all c ∈ Rn

|{x ∈ X | |x − c| < R}| = DvnRn + o(M n) as R → ∞, (126)

where M = R + |c|.
Again it is easy to see that
(i) tied density is invariant under Euclidean transformations.
In a similar way to (124) it can also be shown that if X has tied density D and R is
an arbitrary measurable set in Rn then

|R ∩ X| = DV (R) + o(
M(R)n) + o(
M(R)S(R)) as V (R) → ∞. (127)

This is suﬃcient to establish that
(ii) tied density is independent of shape,
and, with the help of (119) and (120), that
(iii) tied density varies as the reciprocal of the determinant under non-singular aﬃne
transformations.
 42

The error term o(M n) in the deﬁnition of tied density has the eﬀect that, while
balls centred away from the origin are not excluded from consideration, those distant
from the origin by more than a few radii have little inﬂuence. It can be regarded as
a reminder to experimentalists that, as the radius of a probe is increased, the next
position of the probe should not be more than a few radii from the previous position.
There is, nevertheless, a great deal of arbitrariness in the deﬁnition of tied density.
The core idea is to make the error term in (126) depend on c as well as on R, but any
kind of dependency on c (provided that for every R the error term tends to inﬁnity
with c) would have a similar eﬀect. The faster the rate of increase of the error term
with c the more widely applicable the density deﬁnition becomes. In an eﬀort to
conceal this arbitrariness we have chosen a very simple dependency on c.
It is clear from these deﬁnitions that the existence of uniform density for a set
X implies the existence of tied density for X, which in turn implies the existence of
natural density for X, and that each of these densities has a unique value when it is
deﬁned.
To establish the existence of tied density for the sets studied in this paper we
would need to count points x with |x − c| < R instead of |x| < R. As a result,
though the x and y variables in sums still have range R (but no longer centred at the
origin), the l and m variables have range R + |c| = M. The eﬀect is that main terms
remain the same but some R’s are replaced by M’s in error terms. The new error
terms for the results of this paper when the ball of radius R is centred away from the
origin are as follows:

Proposition 6 (n ≥ 3) O(1/R) + O(M/Rn),
Proposition 6 (n = 2) O(log M/R) + O(M/R2),
Theorem 1 (n ≥ 3) O(1/R) + O(M 2/Rn),
Theorem 2 (n = 2) O(√M/R) + O(M/R2),
Proposition 11 (n = 1) O(M 1/k/R),
Theorem 4 (n = 1) O(R1/kM 1/k/RM 1/k2) + O(M 1/k/R).

Each of these error terms, when multiplied by Rn, is well within the error estimate
o(M n) required by the deﬁnition (126) of tied density. Consequently we could have
worked with tied densities instead of natural densities throughout. One concrete
advantage of such an approach would have been that we could then have worked with
the visible points of cubic lattices only, then used property (iii) of tied density to
transfer the results to other lattices.
 43

References

[1] T. M. Apostol, Introduction to Analytic Number Theory, Springer, New York (1976).

[2] L. Argabright and J. Gil de Lamadrid, Fourier analysis of unbounded measures on
locally compact Abelian groups, Memoirs of the American Mathematical Society, vol.
145, AMS, Providence (1974).

[3] M. Baake, U. Grimm and D. H. Warrington, “Some remarks on the visible points of a
lattice”, J. Phys. A27 (1994) 2669–74 and 5041 (Erratum); see also math-ph/9903046.

[4] S. K. Berberian, Measure and Integration, Macmillan, New York (1965), reprint:
Chelsea, New York (1970).

[5] D. Berend, in preparation.

[6] J. W. S. Cassels, “Global Fields”, in: Algebraic Number Theory, eds. J. W. S. Cassels
and A. Fr¨ohlich, Academic Press, London (1967), pp. 42–84.

[7] J. M. Cowley, Diﬀraction Physics, 3rd ed., North Holland, Amsterdam (1995).

[8] J. Dieudonn´e, Treatise on Analysis, vol. II, Academic Press, New York (1970).

[9] G. Grimmett, “Large deviations in the random sieve”, Math. Proc. Cambridge Phil.
Soc. 121 (1997) 519–30.

[10] P. M. Gruber and C. G. Lekkerkerker, Geometry of Numbers, 2nd ed., North Holland,
Amsterdam (1987).

[11] E. Hewitt and K. A. Ross, Abstract Harmonic Analysis I, 2nd ed., Springer, New York
(1979).

[12] A. Hof, “On diﬀraction by aperiodic structures”, Commun. Math. Phys. 169 (1995)
25–43.

[13] A. Hof, “Diﬀraction by aperiodic structures”, in: The Mathematics of Long-Range
Aperiodic Order, ed. R. V. Moody, NATO ASI Series C 489, Kluwer, Dordrecht (1997),
pp. 239–68.

[14] L. K. Hua, Introduction to Number Theory, Springer, Berlin (1982).

[15] M. N. Huxley, “Moments of diﬀerences between square-free numbers”, in: Sieve Meth-
ods, Exponential Sums, and their Applications in Number Theory, eds. G. R. H.
Greaves, G. Harman and M. N. Huxley, LMS 237, Cambridge University Press, Cam-
bridge (1997), pp. 187–204.
 44

[16] J. T. Knight, Commutative Algebra, Cambridge University Press, Cambridge (1971).

[17] J. C. Lagarias, “Meyer’s concept of quasicrystal and quasiregular sets”, Commun.
Math. Phys. 179 (1996) 365–76.

[18] Y. Meyer, Algebraic Numbers and Harmonic Analysis, North-Holland, Amsterdam
(1972).

[19] L. Mirsky, “Arithmetical pattern problem relating to divisibility by rth powers”, Proc.
London Math. Soc. 50 (1949) 497–508.

[20] R. V. Moody, “Meyer sets and their duals”, in: The Mathematics of Long-Range Ape-
riodic Order, ed. R. V. Moody, NATO ASI Series C 489, Kluwer, Dordrecht (1997),
pp. 403–41.

[21] R. Mosseri, “Visible points in a lattice”, J. Phys. A25 (1992) L25–9.

[22] S. S. Pillai, “On sets of square-free numbers”, J. Indian Math. Soc. (New Series) 2
(1936) 116–8.

[23] P. A. B. Pleasants, in preparation.

[24] M. Reed and B. Simon, Methods of Modern Mathematical Physics. I: Functional Anal-
ysis, 2nd ed., Academic Press, San Diego (1980).

[25] W. Rudin, Functional Analysis, 2nd ed., McGraw-Hill, New York (1991).

[26] D. Ruelle, Statistical Mechanics: Rigorous Results, Benjamin, Reading (1969); reprint:
Addison-Wesley, Redwood City (1989).

[27] M. Schlottmann, “Cut-and-project sets in locally compact Abelian groups”, in: Qua-
sicrystals and Discrete Geometry, ed. J. Patera, Fields Institute Monographs, vol. 10,
AMS, Providence (1998), pp. 247–64.

[28] M. Schlottmann, “Generalized model sets and dynamical systems”, to appear in: Direc-
tions in Mathematical Quasicrystals, eds. M. Baake and R. V. Moody, CRM Monograph
Series, AMS, Providence (2000), in press.

[29] M. R. Schroeder, “A simple function and its Fourier transform”, Mathem. Intelli-
gencer 4 (1982) 158–61, and: Number Theory in Science and Communication, 3rd ed.,
Springer, Berlin (1997).

[30] L. Schwartz, Th´eorie des Distributions, 3rd ed., Hermann, Paris (1998).

45
