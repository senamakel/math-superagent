<!-- source: https://personal.math.ubc.ca/~gerg/papers/downloads/PPRP.pdf | converted from PDF -->

Canad. Math. Bull. …¨…¨, pp. Ë–…Ë
http://dx.doi.org/Ë¨.Ëþq/S¨¨¨Çq™þ…¨¨¨¨¨™¨
© Canadian Mathematical Society …¨…¨

Primitive Points in Rational Polygons

Imre Bárány, Greg Martin, Eric Naslund, and Sinai Robins

Abstract. Let A be a star-shaped polygon in the plane, with rational vertices, containing the origin.
he number of primitive lattice points in the dilate tA is asymptotically B
π… Area(tA) as t → ∞.

We show that the error term is both Ω±(t»log log t) and O(t(log t)…~q(log log t)~q). Both bounds
extend (to the above class of polygons) known results for the isosceles right triangle, which appear in
the literature as bounds for the error term in the summatory function for Euler’s ´(n).

1 Introduction

One of the fundamental problems in discrete geometry is to estimate the number of
lattice points contained in a polygon. In this paper, we concern ourselves with the set
of primitive lattice points

(Ë.Ë) P = {(m, n) ∈ Z…∶ gcd(m, n) = Ë},

also known as lattice points visible from the origin. It is a classical result that the
number of primitive lattice points in a “reasonable” region in R… is approximately B
π…
times the area of the region. We are interested in the family {tA} of dilates of a ﬁxed
polygon A, for which we deﬁne the error term

(Ë.…) EA(t) = ¡(tA ∩ P) − B
π… Area(tA) = ¡(tA ∩ P) − B
π… t… Area(A).

he fact that ¡(tA ∩ P) ∼ B
π… t… Area(A), or equivalently, that EA(t) = o(t…), was
likely used as far back as Minkowski (see [ËB, p. ™™Ç] or [þ, heorem þ™]). Stronger
upper bounds than EA(t) = o(t…) are relatively easy to obtain; we state the following
result, which will be justiﬁed in the next section, as a benchmark for comparison.

Proposition Ë.Ë If A ⊂ R… is a polygon, then

EA(t) P t log t

for t ≥ …, where the implicit constant may depend on A.

Received by the editors July qË, …¨Ë™.
Published online on Cambridge Core January q¨, …¨…¨.
he ﬁrst author was partially supported by ERC Advanced Research Grant no. …B8ËBþ (DISCONV)
and by Hungarian National Science Grant K ËËËÇ…8. he second author was supported in part by a Natural
Sciences and Engineering Research Council of Canada Discovery Grant. he fourth author was partially
supported by ICERM, the Institute for Computational and Experimental Research in Mathematics, Brown
University, and would like to thank the warm hospitality of the ﬁrst author and the Alfréd Rényi Institute
of Mathematics, Hungarian Academy of Sciences.
AMS subject classiﬁcation: 11H06, ËËP…Ë, þ…C¨þ.
Keywords: Primitive points in polygons, visible points, Euler’s Totient function, Error term, rational
polygons.

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

… I. Bárány, G. Martin, E. Naslund, and S. Robins

he purpose of this paper is to improve this upper bound for any rational polygon (a
polygon all of whose vertices have both coordinates rational), and show that it cannot
be improved too much more by providing a strong Ω± result for the error term.
It is instructive to consider the speciﬁc example A = ∆, where ∆ is the isosceles
right triangle with vertices (¨, ¨), (Ë, ¨), and (Ë, Ë) and thus area Ë
… . hen ¡(t∆ ∩ P) is
the number of primitive points in the dilate t∆ = {(x, y) ∈ R…∶ ¨ ≤ y ≤ x ≤ t}; that is,

(Ë.q) ¡(t∆ ∩ P) = Q
¨≤m≤t Q
¨≤n≤m
gcd(m,n)=Ë
 Ë = Ë + Q
Ë≤m≤t ´(m)

(where the extra Ë comes from the fact that gcd(¨, Ë) = Ë). It is well known that this
summatory function of the Euler ´-function is asymptotic to q
π… t…, so we deﬁne

(Ë.) E∆(t) = Q
Ë≤m≤t ´(m) − q
π… t… + Ë = ¡(t∆ ∩ P) − q
π… t….

Proposition Ë.Ë implies the estimate E∆(t) P t log t, which (when phrased in terms
of the summatory function of the Euler ´-function) is a classical result of Mertens
[™]. he best known unconditional upper bound for this error term E∆(t) is due to
Walﬁsz [Ë8, p. Ë, eq. (q)]: using methods related to exponential sums, he showed
that

(Ë.þ) E∆(t) P t(log t)…~q(log log t)~q.

As a consequence of our work, we can extend this bound from the isosceles right
triangle ∆ to all rational polygons.

heorem Ë.… Let A ⊂ R… be a rational polygon. hen

EA(t) P t(log t)…~q(log log t)~q,

where the implicit constant may depend on A.

Prior to Walﬁsz’s result, Chowla and Pillai [Ë] showed that these upper bounds
cannot be signiﬁcantly improvedby establishing the lower bound

lim sup
t→∞
 SE∆(t)S
t log log log t > ¨,

that is, E∆(t) = Ω(t log log log t). Later, Erdős and Shapiro [] obtained a slightly
weaker quantitative lower bound but showed that E∆(t) oscillates in sign inﬁnitely
oen. Both results were improved by Montgomery [Ë¨].

Proposition Ë.q We have that E∆(t) = Ω±(t»log log t); in other words,

lim sup
t→∞
 E∆(t)

t»log log t > ¨ and lim inf
t→∞ E∆(t)

t»log log t < ¨.

We use the term origin-star-shaped (star-shaped with respect to the origin) to refer
to any domain B for which λB ⊂ B for all λ ∈ [¨, Ë]; note that in particular, any origin-
star-shaped domain contains the origin. he main result of this paper generalizes this
lower bound of Montgomery to this class of polygons.

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons q

heorem Ë. Let A ⊂ R… be a rational origin-star-shaped polygon. hen

EA(t) = Ω±(t»log log t),

where the implicit constant may depend on A.

In the process of applying an adaptation of Montgomery’s argument to the general
error term EA(t) for the primitive point counting function for the lattice polygon A,
we found that we needed to establish the following “error term independence” result
concerning the error term E∆ for the summatory function of ´(n), which was deﬁned
in equation (Ë.); this result may be of independent interest.

heorem Ë.þ For any positive rational numbers cË, . . . , ck , fË, . . . , fk,

cËE∆( fËx) + ⋅ ⋅ ⋅ + ck E∆( fk x) = Ω±›x»log log x”,

where the implied constant may depend upon the c j and f j.

In other words, there can be no “magic cancellation” among the terms E∆( f jx)
that makes the oscillation of the sum signiﬁcantly smaller than that of an individ-
ual term. Indeed, heorem Ë.þ holds more generally, when E∆ is replaced EA for
any rational origin-star-shaped polygon A (see the remark following the statement of
heorem ….Ë¨).
Furthermore, we conjecture that oscillations of the same size exist even when the
ci are allowed to be negative (where we require the fi to be distinct in order to avoid
trivial cancellations).

Conjecture Ë.B heorem Ë.þ holds for any rational numbers ci and any distinct posi-
tive rational numbers fi.

his conjectural generalization of heorem Ë.þ would imply a stronger version of
heorem Ë. that holds for any rational polygon A, not necessarily star-shaped or
containing the origin.

Conjecture Ë.8 Let A ⊂ R… be a rational polygon. hen

EA(t) = Ω±(t»log log t),

where the implicit constant may depend on A.

he rest of the paper is divided into two sections. In the next section, we show
(heorem ….Ë¨) that the error term EA(t) can be rewritten as a linear combination
of dilates of the totient error function E∆(t), thereby establishing heorem Ë.… and
reducing heorem Ë. to heorem Ë.þ. We then establish this latter theorem in the
ﬁnal section.

2 Decomposing the Error Term

We begin by giving a proof of Proposition Ë.Ë, not only for the sake of completeness,
but also because the structure of the argument foreshadows how we will approach the

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

 I. Bárány, G. Martin, E. Naslund, and S. Robins

main result of this section, namely, heorem ….Ë¨. We use the term pointed triangle to
mean a triangle that has the origin as a vertex.

Proof of Proposition 1.1 We begin by quoting a reasonably precise estimate [8, spe-
cial case of heorem ….Ë] for the number of primitive points inside a domain B: if B
is convex and contains the origin, then

(….Ë) ¡(B ∩ P) − B
π… Area(B) P max{Ë, ω log ω},

where ω is the diameter of B. In particular, if C is a convex polygon containing the
origin and B = tC is a dilate, then the diameter of B is a constant multiple of t, and
so

(….…) EC(t) P max{Ë, t log t},

with the implicit constant depending on C.
However, any polygon A can be partitioned into sums and diﬀerences of ﬁnitely
many pointed triangles (by which we mean that the indicator function of the set A
can be written as sums and diﬀerences of indicator functions of pointed triangles,
up to inaccuracies on the edges of these triangles), simply by triangulating A and
noting that any triangle T can be written as a sum and diﬀerence of three pointed
triangles deﬁned by the three edges of T. Let {T j}n
j=Ë denote the set of these pointed
triangles, and let
 j ∈ {Ë, −Ë} indicate whether (the indicator function of) T j is added
or subtracted, so that Area(A) = ∑n
j=Ë
 j Area(T j). Even though these triangles have
sides in common, the number of double-counted lattice points on the t-dilation of
each side is at most O(t). herefore, the bound (….…) is valid (since pointed triangles
are certainly convex polygons containing the origin), which implies

EA(t) = ¡(tA ∩ P) − B
π… Area(tA)

= − n
Q
j=Ë
 j¡(tT j ∩ P) + O(t)‘ − B
π… Area(tA)

= n
Q
j=Ë
 j− B
π… Area(tT j) + ET j (t)‘ + O(t) − B
π… Area(tA)

= n
Q
j=Ë
 jET j (t) + O(t) P t log t

for t ≥ …, as desired. Ì

Remark In [8], the bound (….Ë) is stated without the hypothesis that B contain the
origin; however, this hypothesis is actually necessary. One can easily construct, using
the Chinese remainder theorem, a square B of diameter ω containing no primitive
lattice points whatsoever. he area of such a square is a constant times ω…, and there-
fore
 U¡(B ∩ P) − B
π… Area(B)U Q ω…,

which is incompatible with the claimed bound ω log ω.

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons þ

he error in the proof of [8, heorem ….Ë] comes when applying [8, Lemma ….q],
which requires ω ≥ Ë, to a term of the form ∑(∆~k)Ë f (kx); when k > ω, the diameter
of ∆~k is less than Ë, and so Lemma ….q cannot be applied. However, if ∆ is a set con-
taining the origin, then these sets ∆~k are sets with diameter less than Ë that contain
the origin, and hence contain no primitive lattice points (indeed, no lattice points at
all other than the origin). herefore, the sums over k in the proof of [8, heorem ….Ë]
can be truncated at k ≤ ω, and the rest of the argument goes through thereaer.

he remainder of this section is dedicated to proving heorem ….Ë¨, which asserts
that the error term EA(t) for any rational polygon A can be rewritten in terms of
the totient error function E∆(t). We begin with a detailed investigation of this latter
function.

Deﬁnition ….Ë hroughout this section, we employ the notation
x for the greatest
integer not exceeding x and {x} = x −
x for the fractional part of x. We also employ
the sawtooth function deﬁned as
 B(x) = {x} − Ë
…
for all real numbers x. his function is equal to the ﬁrst periodic Bernoulli polynomial
BË(x) except when x is an integer; more precisely,

B(x) = BË(x) − Ë
… Ë (x),

where Ë is the indicator function of the integers.

Next we recall some well-known and useful estimates for sums involving the Möbius
µ-function, which satisﬁes the key identity

(….q) Q
dSn µ(d) = ¢¨¨
¦
¨¨¤

Ë, if n = Ë,
¨, otherwise.

For any real numbers … ≤ x ≤ y, we have

Q
d≤x
 µ(d)
d … = B
π… + O− Ë
x ‘;(….)
 Q
d≤y µ(d) x
d  = Ë;(….þ)
 U Q
d≤x
 µ(d)
d U P Ë.(….B)

he proofs of equations (….) and (….B) are in [B], and the identity (….þ) can be found
in [Ë], for instance. We are now ready to give a more precise formula for the totient
error term E∆(t).

Proposition ….… For any real numbers T ≥ t ≥ …,

E∆(t) = −t Q
d≤T
 µ(d)
d B− t
d ‘ + O(T).

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

B I. Bárány, G. Martin, E. Naslund, and S. Robins

Proof Starting from equation (Ë.q) and the key identity (….q), we have

¡(t∆ ∩ P) = Ë + Q
Ë≤m≤t Q
Ë≤n≤m
gcd(m,n)=Ë
 Ë = Q
m≤t Q
n≤m
gcd(m,n)=Ë Q
dSgcd(m,n) µ(d)

= Q
d≤t µ(d) Q
m≤t
dSm
 Q
n≤m
dSn
 Ë = Q
d≤t µ(d) Q
k≤t~d Q
K≤k Ë

= Q
d≤t µ(d) Q
k≤t~d k = Q
d≤t µ(d) Ë
… − t
d 
… +  t
d ‘

= Ë
… Q
d≤t µ(d) t
d 
… + Ë
…

by equation (….þ). he last sum does not change if we extend its range from d ≤ t to
d ≤ T. Expanding
 t
d … = ( t
d − { t
d })…, we obtain

¡(t∆ ∩ P) = t…

… Q
d≤T
 µ(d)
d … − t Q
d≤T
 µ(d)
d ı t
d   + Q
d≤T µ(d)ı t
d  
… + Ë
…

= t…

… − B
π… + O− Ë
T ‘‘ − t Q
d≤T
 µ(d)
d ı t
d   + O(T)

by equation (….) and a trivial bound. herefore,

E∆(t) = ¡(t∆ ∩ P) − B
π… t… Area(∆)

= q
π… t… − t Q
d≤T
 µ(d)
d ı t
d   + O(T) − q
π… t…

= −t Q
d≤T
 µ(d)
d −B− t
d ‘ + Ë
… ‘ + O(T)

= −t Q
d≤T
 µ(d)
d B− t
d ‘ + O(T)

by equation (….B). Ì

Counting lattice points in the simplest way (each with weight Ë) is problematic in
our present context. First, we will be decomposing polygons into unions of triangles
that share sides, and so double-counting lattice points on these shared boundaries
would become an issue; second, any error term as large as the perimeter for counting
lattice points in a triangle would result in an unacceptably large error term in the
inclusion-exclusion method we use to detect primitive lattice points. Consquently,
we employ a more convenient weighting in our lattice-point counting, namely the
solid angle sum of a polygon.

Deﬁnition ….q For a point p ∈ R…, let

D(p; r) = {q ∈ R…∶ d(p − q) < r}

denote the disk of radius r centered at p. Let λ denote Lebesgue measure on R…, and
deﬁne for any polygon A the solid angle at p:

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons 8

ωA(p) = lim
r→¨ λ(D(p; r) ∩ A)
λ(D(p; r)) .

It follows directly from the deﬁnition that

ωA(p) =
 ¢¨¨¨¨¨¨¨
¦
¨¨¨¨¨¨¨¤

¨, if p ∉ A,
Ë, if p is in the interior of A,
Ë~…, if p lies in the interior of an edge of A,
θ p~…π, if p is a vertex of A,

where θ p is the angle at the vertex p. Using this function, we deﬁne the solid angle
sum of the t-dilate of the rational polygon A to be

AA(t) = Q
p∈ … ωtA(p).

Note that trivially AcA(t) = AA(ct) for any constant c > ¨.
We also deﬁne the corresponding sum over primitive lattice points only:

PA(t) = Q
p∈ ωtA(p).

he beneﬁt of this solid angle weighting is that both of these functions are additive,
in the sense that AA∪B(t) = AA(t) + AB(t) and PA∪B(t) = PA(t) + PB(t) for any
polygons A and B with disjoint interiors.

Given positive rational numbers rË and r…, we let T(rË, r…) denote the right triangle
with vertices at (¨, ¨), (rË, ¨), and (¨, r…). An exact calculation of the solid angle sum
of dilates of T(rË, r…) is available for our use. Recall that Ë is the indicator function
of the integers.

Proposition …. For any positive rational numbers rË and r… and any positive real
number t,

(….8) AT(rË ,r…)(t) = rËr…
… t… − BË(qrËr…t) t
q + B…(qrËr…t)
…q…rËr… + r…
Ë + r…
…
Ë…rËr…
− s(qrË, qr…; rËt, ¨) − s(qr…, qrË; r…t, ¨)

− arctan(rË~r…)
…π Ë (rËt) − arctan(r…~rË)
…π Ë (r…t),

where q is the unique positive rational number such that qrË and qr… are coprime inte-
gers. Here, BË and B… are the ﬁrst and second periodic Bernoulli polynomials, respec-
tively, and
 s(h, k; y, x) = Q
r (mod k) BË„h r + x
k + y‚BË„ r + x
k ‚

is the Dedekind–Rademacher sum.

While its exact value is unimportant for us, we note that if rË = a
b and r… = c
d in low-
est terms, then the rational number q in the above statement is q = lcm[b, d]~gcd(a, c),
so that qrË = a~ gcd(a, c) ⋅ d~ gcd(b, d) and qr… = c~ gcd(a, c) ⋅ b~ gcd(b, d).

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Ç I. Bárány, G. Martin, E. Naslund, and S. Robins

Proof Le Quang and the fourth author [Ç, Main heorem] established this result for
the case of AT(h,k)(t) when h and k are positive coprime integers:

AT(h,k)(t) = hk
… t… − BË(hkt)t + B…(hkt)
…hk + h… + k…

Ë…hk − s(h, k; ht, ¨)

− s(k, h; kt, ¨) − arctan(h~k)
…π Ë (ht) − arctan(k~h)
…π Ë (kt).

Given positive rational numbers rË and r…, let q be the unique positive rational number
such that h = qrË and k = qr… are coprime integers. hen

AT(rË ,r…)(t) = AT(h~q,k~q)(t) = AT(h,k)~q(t) = AT(h,k)(t~q)

and therefore

AT(rË ,r…)(t) = qrËqr…
… „ t
q ‚

… − BË„qrËqr… t
q ‚ t
q

+ B…(qrËqr…t~q)
…qrËqr… + (qrË)… + (qr…)…

Ë…qrËqr…
− s(qrË, qr…; qrËt~q, ¨) − s(qr…, qrË; qr…t~q, ¨)

− arctan(qrË~qr…)
…π Ë (qrËt~q) − arctan(qr…~qrË)
…π Ë (qr…t~q),

which is equivalent to the statement of the proposition. Ì

While we include this exact statement in the hopes that it will be useful in the
future, for our present purposes we can use the following approximation.

Corollary ….þ For any positive rational numbers rË and r…, there exist constants c =
c(rË, r…) and f = f (rË, r…) such that

AT(rË ,r…)(t) = Area(T(rË, r…))t… − …cB( f t)t + cË ( f t)t + OrË ,r… (Ë).

Proof In the identity (….8), the leading coeﬃcient rËr…~… is indeed the area of T(rË, r…).
Deﬁnition ….Ë implies that −BË(qrËr…t) t
q = −…cB( f t)t + cË ( f t)t with c = Ë
…q . Finally,

B… is a bounded function, and the two arctangent terms in equation (….8) are bounded
in terms of rË and r…; and since SBË(z)S ≤ Ë
… we have Ss(h, k; y, x)S ≤ k
 uniformly in
h, y, and x, so that the two Dedekind–Rademacher sums in equation (….8) are also
bounded in terms of rË and r…. Ì

Deﬁnition ….B A ﬁtting angle is any angle of the form ∠POQ where O = (¨, ¨),
and where P = (k, K) and Q = (m, n) are lattice points such that det › k
m K
n ” = ±Ë,
or equivalently such that Area(△POQ) = Ë
… . A ﬁtting triangle is a rational pointed
triangle whose angle at the vertex O is a ﬁtting angle.

Corollary ….8 For any ﬁtting triangle T, there exist positive rational numbers c = c(T)
and f = f (T) such that

AT(t) = Area(T)t… − …cB( f t)t + cË ( f t)t + OT(Ë).

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons ™

Proof First, let Γ be any element of SL…(Z). Such elements act on the plane, acting
as a bijection on the lattice Z…, sending lines and triangles to lines and triangles, and
preserving whether lattice points lie on line segments or inside triangles. herefore
the only disparity between the solid angle sums of tT and tΓ(T) is that the solid angles
at the three vertices might be diﬀerent. Consequently, we certanly have

AT(t) = AΓ(T)(t) + O(Ë)

uniformly for all triangles T, all Γ ∈ SL…(Z), and all t > ¨.
Given a ﬁtting triangle △RËOR…, we can ﬁnd lattice points P = (k, K) and Q =
(m, n), on the rays ÐÐ→
ORË and ÐÐ→
OR…, respectively, such that det › k
m K
n ” = ±Ë. It follows

that Γ = › k
m K
n ”
−Ë is an element of SL…(Z) that sends P to (Ë, ¨) and Q to (¨, Ë), and
hence sends RË and R… to rational points (rË, ¨) and (¨, r…), respectively. herefore
AT(t) = AΓ(T)(t) + O(Ë) = AT(rË ,r…)(t) + O(Ë), and so this corollary follows directly
from Corollary ….þ (since the areas of T and Γ(T) = T(rË, r…) are equal). Ì

We say that a polygon A can be written as a sum, or written as a signed sum, of
ﬁnitely many other polygons B j if the indicator function of A can be written as sums,
or sums and diﬀerences (respectively), of indicator functions of the indicator func-
tions of the B j, up to inaccuracies on the edges of these polygons.

Lemma ….Ç Any rational polygon can be written as a signed sum of ﬁtting triangles.
If the rational polygon is origin-star-shaped, then it can be written as a sum of ﬁtting
triangles.

Proof First, any rational polygon P can be written as the signed sum of rational
pointed triangles: every edge of P deﬁnes a rational pointed triangle, which is taken
with sign +Ë if the ray from the origin hits that edge from the interior of the polygon
and sign −Ë if the ray from the origin hits that edge from the exterior of the polygon.
Note that if P is origin-star-shaped, then all the signs that occur in this decomposition
are +Ë. All that remains is to prove that every rational pointed triangle can be written
as a sum of ﬁtting triangles.
Given a rational pointed triangle △AOB, consider the convex hull of all the lattice
points in the cone bounded by Ð→
OA and Ð→
OB other than the origin. he vertices of this
convex hull can be written in order as V¨, . . . , Vk for some k ≥ Ë, where V¨ ∈ Ð→
OA
and Vk ∈ Ð→
OB. Note that each △VjOVj+Ë contains no lattice points other than its
three vertices, by the deﬁnition of convex hull. By Pick’s theorem, the area of this
triangle equals Ë
… , and thus each angle ∠VjOVj+Ë is a ﬁtting angle. Let Wj be the

intersection of ÐÐ→
OVj and AB, so that W¨ = A and Wk = B. hen △AOB is the sum
of the ﬁtting triangles △W¨OWË, . . . , △Wk−ËOWk. (We remark that V¨, . . . , Vk is a
“Hilbert basis” for the lattice points in the cone deﬁned by ∠AOB; in that context it is
a standard fact that the triangles △VjOVj+Ë are “empty” and “unimodular” and thus,
in our terminology, have ﬁtting angles ∠VjOVj+Ë.) Ì

Proposition ….™ Let A be a rational polygon. here exist a positive integer k, rational
numbers cË, . . . , ck, and positive rational numbers fË, . . . , fk (all depending on A) such

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Ë¨ I. Bárány, G. Martin, E. Naslund, and S. Robins

that

(….Ç) AT(t) = Area(A)t… − …t k
Q
j=Ë c jB( f j t) + t k
Q
j=Ë c jË ( f j t) + OA(Ë).

Furthermore, when A is an origin-star-shaped polygon, the c j can be taken to all be
positive.

Proof he proposition follows immediately by using Lemma ….Ç to decompose A
as a signed sum of ﬁtting triangles, and then applying Corollary ….8 to each of those
ﬁtting triangles T (taking c j = ±c(T) from Corollary ….8, depending on the sign at-
tached to T in the decomposition of A). Ì

he following theorem results from a careful examination of PA(t), which can be
related to the solid angle sum AA(t) using the Möbius function as in the proof of
Proposition ….….

heorem ….Ë¨ Let A be a rational polygon. here exist a positive integer k, rational
numbers rË, . . . , rk, and positive rational numbers fË, . . . , fk (all depending on A) such
that

(….™) EA(t) = k
Q
j=Ë r jE∆( f j t) + O(t),

where the implicit constant may depend upon A. Furthermore, if A is an origin-star-
shaped polygon, then the r j can all be taken to be positive as well.

Remark heorem Ë.… follows immediately from heorem ….Ë¨ in light of the known
upper bound (Ë.þ). In addition, heorem Ë. follows immediately from the combi-
nation of heorem ….Ë¨ and heorem Ë.þ; the latter theorem is proved in the next
section. Finally, we note that heorem ….Ë¨ automatically implies the generalization
of heorem Ë.þ where the isosceles right triangle ∆ is replaced by any rational origin-
star-shaped polygon A.

Proof We commence by excluding the (non-primitive) origin and using the Möbius
identity (….q) to write

PA(t) = Q
(m,n)∈ …(¨,¨) ωtA›(m, n)” Q
dSgcd(m,n) µ(d).

Interchanging the order of summation (valid since in reality there are only ﬁnitely
many nonzero terms) and rescaling (which preserves solid angles),

PA(t) = ∞
Q
d=Ë µ(d) Q

(m,n)∈ …(¨,¨)
dSm, dSn
 ωtA›(m, n)”

= ∞
Q
d=Ë µ(d) Q
(x , y)∈ …(¨,¨) ω t
d A›(x, y)”

= ∞
Q
d=Ë µ(d)−AA− t
d ‘ − ω t
d A›(¨, ¨)”‘

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons ËË

by the deﬁnition of AA. We can truncate the outer sum at any real number T ≥
t diam(A), since for larger values of d, the diameter of t
d A is less than Ë, and hence t
d A
(which contains the origin) cannot contain any other lattice points. Proposition ….™
now implies

PA(t) = Q
d≤T µ(d)œ Area(A) t…

d … − … t
d
 k
Q
j=Ë c jB„ f j t
d ‚

+ t
d
 k
Q
j=Ë c jË „ f j t
d ‚ + OA(Ë)¡

= Area(A)t… Q
d≤T
 µ(d)
d … − …t k
Q
j=Ë c j Q
d≤T
 µ(d)
d B„ f j t
d ‚

+ t k
Q
j=Ë c j Q
d≤T
 µ(d)
d Ë „ f j t
d ‚ + OA„ Q
d≤T Sµ(d)S‚

= Area(A)t…„ B
π… + O„ Ë
T ‚‚ − …t k
Q
j=Ë c j Q
d≤T
 µ(d)
d B„ f j t
d ‚

+ t k
Q
j=Ë c j Q
d≤T
dS f j t
 µ(d)
d + OA(T).

As long as T ≥ f j t, the inner sum on the last line equals ¨ if f j t ∉ Z and ´( f j t)~( f j t) ≤
Ë if f j t ∈ Z, and therefore this simpliﬁes to

PA(t) = B
π… Area(A)t… − …t k
Q
j=Ë c j Q
d≤T
 µ(d)
d B„ f j t
d ‚ + OA(T)

when t ≤ T. Using Proposition ….…, we can rewrite the above in terms of E∆(t) to
obtain

(….Ë¨) PA(t) = Area(A) B
π… t… + k
Q
j=Ë
 …c j
f j E∆( f j t) + OA(T)

for any T ≥ t max{Ë, diam(A), fË, . . . , fk}.
he number of integer points on the boundary of tA is OA(t), since tA has ﬁnitely
many sides each of which has length OA(t). Consequently, the diﬀerence between the
solid angle sum and the ordinary count of lattice points satisﬁes PA(t)−¡(tA∩P) PA
t, and therefore equation (….Ë¨) implies

EA(t) = ¡(tA ∩ P) − Area(A) B
π… t…

= PA(t) + OA(t) − Area(A) B
π… t… = k
Q
j=Ë
 …c j
f j E∆( f j t) + O(T).

Upon setting T = t max{Ë, diam(A), fË, . . . , fk} and r j = …c j~ f j for each Ë ≤ j ≤ k,
the theorem follows. Ì

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Ë… I. Bárány, G. Martin, E. Naslund, and S. Robins

3 Linear Combinations of E∆

In this section, we prove heorem Ë.þ, showing that positive rational linear combina-
tions of scaled copies of the totient error function E∆ have oscillations as large as those
known for E∆ itself. We begin by recalling some of the components of Montgomery’s
argument [Ë¨] establishing the oscillations of E∆, aer which we describe the strategy
that leads to our modiﬁcations.

Deﬁnition q.Ë Deﬁne
 R¨(x) = Q
n≤x
 ´(n)
n − B
π… x.

Montgomery [Ë¨, heorem Ë] showed that the totient error function is closely con-
nected to the above weighted error.

Lemma q.… (Montgomery) E∆(x) = xR¨(x) + O›x exp(−c»log x)”.

Deﬁnition q.q Deﬁne
 K(q, α) = − Q
dSq
 µ(d)
d B− α
d ‘,

where the sawtooth function B(x) was deﬁned in Deﬁnition ….Ë, and

C(q, α) = K(q, α) B
π… M
pSq −Ë − Ë
p… ‘
−Ë.

Lemma q. If b is relatively prime to q, then

K(qb, αb) = Q
dË d…=b
 µ(dË)
dË K(q, αd…).

Proof Since every divisor of qb can be written uniquely as a divisor of b times a
divisor of q,

K(qb, αb) = − Q
dSqb
 µ(d)
d B− αb
d ‘ = − Q
aSb
 µ(a)
a Q
cSq
 µ(c)
c B− αb
ac ‘

= Q
aSb
 µ(a)
a K−q, αb
a ‘,

which is equivalent to the statement of the lemma. Ì

he above quantities appear [Ë¨, Lemma ] in a key part of Montgomery’s argu-
ment, which displays a bias in the values of R¨ sampled on an arithmetic progression.

Lemma q.þ (Montgomery) here exists a positive real number c such that if α is a
non-integral real number with ¨ < α < q, then

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons Ëq

N
Q
n=Ë R¨(nq + α) = C(q, α)N + O›N exp(−c»log N)”

uniformly for q ≤ e c»log N .

he proof of Lemma q.þ is based on the following ancient identity due to Raabe [Ëþ]
for a sum of B(x) over an arithmetic progression of points: for all real numbers x,

J
Q
j=Ë B−x + j
J ‘ = B(Jx).

he relevance to the problem at hand is due to the fact [Ë¨, Lemma Ë] that

R¨(x) = − Q
d≤x
 µ(d)
d B− x
d ‘ + O(Ë).

To exploit Lemma q.þ, Montgomery chose α = q~, so that for all divisors d of q
the quantity B(α~d) equals ± Ë
 , with the sign depending only upon the residue class
of d modulo . On the other hand, he chose q to be the product of many primes
congruent to q modulo ; for any divisor d of this q, the residue class of d (mod )
depends only on the number of prime factors of d. With these choices, the sign of
B(α~d) correlates exactly with the sign of µ(d), making the quantity K(q, α) large
in absolute value. Choosing α = qq~ instead again makes K(q, α) large but with the
opposite sign.
One of our key observations is that we can work modulo a suitably chosen prime
P rather than working modulo . Instead of choosing q to be the product of many
primes congruent to q (mod ), we instead choose q to be the product of many primes
that are quadratic nonresidues modulo P. he sign of B(α~d) will not be perfectly cor-
related with µ(d), but there will be enough of a systematic bias in the signs of B(α~d)
(due to the imperfect distribution of quadratic residues and nonresidues modulo P)
that we can still force K(q, α) to be large in absolute value. If we choose the prime
P carefully, we can even force all of the diﬀerent K(qbi , αbi) to be large in absolute
value and have the same sign.
We introduce the following function, whose oscillations we will want to establish.
For the rest of this section, we use boldface variables such as a to indicate the depen-
dence of various quantities on k-tuples (aË, . . . , ak) of variables.

Deﬁnition q.B Given real numbers aË, . . . , ak and bË, . . . , bk, deﬁne

Ga,b(x) = aËR¨(bËx) + ⋅ ⋅ ⋅ + ak R¨(bk x).

he starting point of our modiﬁcation of Montgomery’s method is the following
easy consequence of Lemma q.þ.

Lemma q.8 Let aË, . . . , ak and bË, . . . , bk > ¨ be real numbers. here exists a positive
real number c such that if α ∈ (¨, q) is a real number such that none of the αb j is an

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Ë I. Bárány, G. Martin, E. Naslund, and S. Robins

integer, then

N
Q
n=Ë Ga,b(nq + α) = N k
Q
j=Ë a jC(qb j, αb j) + Oa,b›N exp(−c»log N)”

uniformly for max{bË, . . . , bk} < q ≤ e c»log N .

We now state our oscillation result for Ga,b, aer which we show how heorem Ë.þ
is implied by it. hereaer, our only remaining goal will be to establish this proposi-
tion.

Proposition q.Ç Let aË, . . . , ak and bË, . . . , bk be ﬁxed positive integers. here exists
a constant κa,b > ¨, and sequences QN ,b ≤ e»log N and ¨ < α+
N , α−
N < QN ,b deﬁned for
positive integers N, for which QN ,b tends to inﬁnity with N and

N
Q
n=Ë Ga,b(nQN ,b + α+
N ) = κa,bN»log log N + Oa,b(N),

N
Q
n=Ë Ga,b(nQN ,b + α−
N ) = −κa,bN»log log N + Oa,b(N).

Proof of Theorem 1.5 assuming Proposition 3.8 By Lemma q.…,

k
Q
j=Ë r jE∆(s jx) = x k
Q
j=Ë r js jR¨(s jx) + Or,s›x exp(−c»log x)”.

Let Ds be the least common denominator of the rational numbers sË, . . . , sk, and set
a j = Dsr js j and b j = Dss j. Replacing x by Dsx, we obtain

(q.Ë) k
Q
j=Ë r jE∆(s j Dsx) = xGa,b(x) + Or,s›x exp(−c»log x)”.

Let ¨ < ε < κa,b. If there were to exist a real number x¨ such that Ga,b(x) < (κa,b −
ε)»log log(Dsx) for all x > x¨, then we would have

N
Q
n=Ë Ga,b(nQN + α+
N )

< (κa,b − ε)N¼
log log(Ds(NQN + α+
N )) + O(x¨ max
Ë≤t≤x¨ Ga,b(t))

= (κa,b − ε)N−
»log log N + Os− Ë
»log N ‘‘ + Oε,a,b(Ë)

by the bounds ¨ < α+
N < QN ,b; for large N (and hence for large QN ,b), this would con-
tradict Proposition q.Ç. herefore, no such x¨ can exist, in which case equation (q.Ë)
implies that there are arbitrarily large values of x for which

k
Q
j=Ë r jE∆(s j Dsx) ≥ x(κa,b − ε)»log log(Dsx) + Or,s›x exp(−c»log x)”.

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons Ëþ

In other words,
 lim sup
x→∞
 rËE∆(sËx) + ⋅ ⋅ ⋅ + rk E∆(sk x)

x»log log x ≥ κa,b
Ds ,

and the analogous argument using the values G(nQN + α−
N ) gives

lim inf
x→∞ rËE∆(sËx) + ⋅ ⋅ ⋅ + rk E∆(sk x)

x»log log x ≤ − κa,b
Ds ,

completing the derivation of heorem Ë.þ from Proposition q.Ç. Ì

Before addressing Proposition q.Ç directly, we record some preliminary facts about
the distribution of primes in residue classes and the associated L-values.

Lemma q.™ Let P ≡ q (mod ) be a prime exceeding q, and let χË(⋅) = › ⋅
P” denote
the quadratic character modulo P. hen the class number h(−P) of the ﬁeld Q(√−P)
equals
 h(−P) =
 √P
π L(Ë, χË) = − Ë
P
 P−Ë
Q
a=Ë a χË(a).

Proof hese results are classical; see, for example, [q, Chapter B, equations (Ëþ) and
(Ë™)]. Ì

Lemma q.Ë¨ Let P ≡ q (mod ) be a prime exceeding q. If χ¨ denotes the principal
character (mod P), then

M
p≤y
› p
P”=−Ë
 −Ë + χ¨(p)
p ‘ = cP»log y + OP(Ë),

where

(q.…) cP = − eγ

π P − Ë

h(−P)√P M
› p
P”=−Ë ›Ë − p−…”‘
Ë~….

On the other hand, for any nonprincipal character χ (mod P),

M
p≤y
› p
P”=−Ë
 −Ë + χ(p)
p ‘ PP Ë.

Proof Again, let χË(⋅) = › ⋅
P” denote the quadratic character (mod P). For any char-
acter χ (mod P), we can write

(q.q) − M
p≤y
› p
P”=−Ë
 −Ë + χ(p)
p ‘‘
… =

M
p≤y −Ë − χ(p)
p ‘
−Ë M
p≤y −Ë − χ(p)χË(p)
p ‘ M
p≤y
› p
P”=−Ë
 −Ë − χ…(p)
p… ‘.

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

ËB I. Bárány, G. Martin, E. Naslund, and S. Robins

he last product is absolutely convergent uniformly in P; indeed,

U M
p>y
› p
P”=−Ë
 −Ë − χ…(p)
p… ‘U ≤ M
p>y
› p
P”=−Ë
 −Ë + Ë
p… ‘

< M
n>y −Ë + Ë
n… ‘ < M
n>y −Ë − Ë
n… ‘
−Ë = Ë + Ë
yˇ ,

and so the last product equals ∏› p
P”=−Ë(Ë − χ…(p)p−…)(Ë + O( Ë
y )) and, in particular, is
uniformly bounded. When χ is nonprincipal, we know [ËË, heorem .ËË(d)] that

M
p≤y −Ë − χ(p)
p ‘
−Ë = L(Ë, χ) + O χ− Ë
log y ‘ = L(Ë, χ)−Ë + OP− Ë
log y ‘‘,

since L(Ë, χ) ≠ ¨ [ËË, heorem .™]. (Better error terms are available but are not rele-
vant for us.) In particular, when neither χ nor χ χË is principal, the ﬁrst two products
on the right-hand side of equation (q.q) are L(Ë, χ)(Ë + OP( Ë
log y )) and L(Ë, χ χË)−Ë(Ë +
OP( Ë
log y )), respectively; in particular, both are PP Ë. his estimate establishes the
lemma when χ is neither principal nor equal to χË.
When χ = χË, the ﬁrst and third factors are still bounded, while the second fac-
tor now actually diverges to ¨, and hence, in particular, is still bounded. Finally,
when χ = χ¨ is principal, the second factor converges to Ë~L(Ë, χË) = √P~πh(−P)
by Lemma q.™, while the ﬁrst factor on the le-hand side of equation (q.q) is

M
p≤y −Ë − χ¨(p)
p ‘
−Ë = M
p≤y
p≠P
 −Ë − Ë
p ‘
−Ë

= P − Ë
P (eγ log y)−Ë + O− Ë
log y ‘‘

by Mertens’s formula [ËË, heorem ….8(e)]. his asymptotic evaluation of the right-
hand side of equation (q.q) establishes the lemma when χ is principal, indeed with
the stronger error term OP( Ë»log y ). Ì

We can now deﬁne the modulus QN ,b appearing in the statement of Proposition q.Ç,
in terms of a companion prime Pb.

Deﬁnition q.ËË Let Pb be the smallest prime in the residue class Pb ≡ −Ë (mod ÇbË . . . bk).
Note that Pb ≡ 8 (mod Ç), and so −Ë is a quadratic nonresidue (mod Pb), while … is a
quadratic residue (mod Pb). Furthermore, if p is any odd prime dividing one of the
b j, then by quadratic reciprocity [Ë…, heorem q.Ë], we have, since Pb ≡ q (mod ) and
Pb ≡ −Ë (mod p),
 ‰ p
Pb’ = (−Ë)
(p−Ë)~…‰Pb
p ’ = (−Ë)(p−Ë)~…‰
−Ë
p ’ = Ë.

herefore each prime dividing every b j is a quadratic residue (mod Pb).

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons Ë8

Now deﬁne, for any integer N ≥ Ë,

QN ,b = M

p≤c»log N
› p
Pb”=−Ë
 p,

where c is the constant from Lemma q.8. Since

log QN ,b = Q
Ë≤a≤Pb
› a
Pb”=−Ë
 Q

p≤c»log N
p≡a (mod Pb)
 log p = Q
Ë≤a≤Pb
› a
Pb”=−Ë
 θ›c»log N; Pb, a”,

where the sum on the right-hand side is over ´(Pb)~… reduced residue classes mod-
ulo Pb, the prime number theorem for arithmetic progressions to a ﬁxed modulus
(see [ËË, Corollary ËË.…Ë]) implies that

log QN ,b ∼ Ë
… c»log N .

In particular, QN ,b tends to inﬁnity with N, and QN ,b < e c»log N when N is large
enough.
Note also that QN ,b is squarefree and relatively prime to Pb and to each b j, since
every prime p S b j satisﬁes › p
Pb” = Ë. Finally, note that any divisor d of QN ,b has
the convenient (and, for us, crucial) property that › d
Pb” = µ(d), since both quantities
equal (−Ë)¡{pSd}.

Lemma q.Ë… For any Ë ≤ b ≤ P − Ë, we have

Q
dSQ N ,b
d≡b (mod Pb)
 Ë
d = cPb√…(Pb − Ë)
 »log log N + Ob(Ë),

where cP was deﬁned in equation (q.…).

Proof From the orthogonality of the characters modulo Pb,

Q
dSQ N ,b
d≡b (mod Pb)
 Ë
d = Ë
Pb − Ë Q
χ (mod Pb) ¯χ(b) Q
dSQ N ,b
 χ(d)
d

= Ë
Pb − Ë Q
χ (mod Pb) ¯χ(b) M
pSQ N ,b −Ë + χ(p)
p ‘

= Ë
Pb − Ë Q
χ (mod Pb) ¯χ(b) M

p≤c»log N
› p
Pb”=−Ë
 −Ë + χ(p)
p ‘

= Ë
Pb − Ë cPb ¼log(c»log N) + OPb (Ë)

by Lemma q.Ë¨. he statement of the lemma follows upon noting that log(c»log N) =
Ë
… log log N + O(Ë). Ì

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

ËÇ I. Bárány, G. Martin, E. Naslund, and S. Robins

Lemma q.Ëq For any integer m that is not a multiple of Pb and for any integer N ≥ q,

K−QN ,b, mQN ,b
Pb ‘ = ‰m
Pb’‰QN ,b
Pb ’ cPb h(−Pb)
√…(Pb − Ë)
 »log log N + Ob(Ë).

Remark he exact value of the leading constant is not as important for us as the
fact that its dependence on m is only in the term › m
Pb”, so that the sign of the leading
constant depends on whether m is a quadratic residue or nonresidue modulo Pb.

Proof By Deﬁnition q.q and the coincidence between the Legendre symbol and the
Möbius function on divisors of QN ,b (as noted at the end of Deﬁnition q.ËË), we have

−K−QN ,b, mQN ,b
Pb ‘ = Q
dSQ N ,b
 µ(d)
d B− mQN ,b
dPb ‘

= Q
dSQ N ,b ‰ d
Pb’ Ë
d B− mQN ,b
dPb ‘

= Q
dSQ N ,b ‰mQN ,b
Pb ’‰mQN ,b~d
Pb ’ Ë
d B− mQN ,b
dPb ‘

= ‰mQN ,b
Pb ’
 Pb−Ë
Q
a=Ë ‰ a
Pb’B− a
Pb ‘ Q
dSQ N ,b
mQ N ,b d −Ë≡a (mod Pb)

Ë
d .

he last congruence is equivalent to d being in the reduced residue class mQN ,ba−Ë (mod Pb),
and so Lemma q.Ë… applies:

− K−QN ,b, mQN ,b
Pb ‘

= ‰mQN ,b
Pb ’
 Pb−Ë
Q
a=Ë ‰ a
Pb’B− a
Pb ‘− cPb√…(Pb − Ë)
 »log log N + Ob(Ë)‘

= ‰mQN ,b
Pb ’ cPb√…(Pb − Ë)
 »log log N
 Pb−Ë
Q
a=Ë ‰ a
Pb’B− a
Pb ‘ + Ob(Ë).

By the deﬁnition of the Bernoulli polynomial B, this sum equals

Pb−Ë
Q
a=Ë ‰ a
Pb’B− a
Pb ‘ = Ë
Pb
 Pb−Ë
Q
a=Ë a‰ a
Pb’ − Ë
…
 Pb−Ë
Q
a=Ë ‰ a
Pb’ = −h(−Pb) − ¨

by Lemma q.™, which completes the proof of the lemma. Ì

We now have all the tools we need to establish Proposition q.Ç and hence our main
theorems.

Proof of Proposition 3.8 Given a suﬃciently large integer N, deﬁne two numbers

α±
N = m±QN ,b
Pb ,

where the integers Ë ≤ m± ≤ Pb −Ë satisfy m± ≡ ±QN ,b (mod Pb); note that none of the
numbers α±
N b j is an integer, since neither QN ,b nor any of the b j is a multiple of the

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons Ë™

prime Pb. Since we conﬁrmed in Deﬁnition q.ËË that QN ,b < e c»log N , we can invoke
Lemma q.8:

N
Q
n=Ë Ga,b(nQN ,b + α+
N )

= N k
Q
j=Ë a jC(QN ,bb j, α+
N b j) + O›N exp(−c»log N)”

= N k
Q
j=Ë a jK(QN ,bb j, α+
N b j) B
π… M
pSQ N ,b b j −Ë − Ë
p… ‘
−Ë + O(N).

As noted in Deﬁnition q.ËË, each b j is relatively prime to QN ,b. hus, by Lemma q.
with our choice of α±
N ,

N
Q
n=Ë Ga,b(nQN ,b + α±
N ) = O(N) + B
π… N M
pSQ N ,b −Ë − Ë
p… ‘
−Ë k
Q
j=Ë a j

× M
pSb j −Ë − Ë
p… ‘
−Ë Q
dË d…=b j
 µ(dË)
dË K−QN ,b, m±d…QN ,b
Pb ‘.

By Lemma q.Ëq,

N
Q
n=Ë Ga,b(nQN ,b + α±
N )

= O(N) + B
π… N M
pSQ N ,b −Ë − Ë
p… ‘
−Ë k
Q
j=Ë a j M
pSb j −Ë − Ë
p… ‘
−Ë

× Q
dË d…=b j
 µ(dË)
dË −‰m±d…
Pb ’‰QN ,b
Pb ’ cPb h(−Pb)
√…(Pb − Ë)
 »log log N + Ob(Ë)‘.

As noted in Deﬁnition q.ËË, every prime dividing b j is a quadratic residue modulo Pb,
which implies that ›d…
Pb” = Ë always. Moreover, m+ ≡ QN ,b (mod Pb), so the product

of Legendre symbols ›m+

Pb ”›Q N ,b
Pb ” equals Ë; on the other hand, since −Ë is a quadratic

nonresidue modulo Pb, the product of Legendre symbols ›m−

Pb ”›Q N ,b
Pb ” equals −Ë. Con-
sequently,
 N
Q
n=Ë Ga,b(nQN ,b + α±
N )

= ± B
π… cPb h(−Pb)
√
…(Pb − Ë) N»log log N M
pSQ N ,b −Ë − Ë
p… ‘
−Ë k
Q
j=Ë a j

× M
pSb j −Ë − Ë
p… ‘
−Ë Q
dË d…=b j
 µ(dË)
dË + O(N).

he last sum equals ∑dSb j µ(d)
d = ´(b j)
b j , which when multiplied by the preceding prod-

uct becomes ∏pSb j (Ë + Ë
p )−Ë. In addition, by the same argument as in the proof of

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

…¨ I. Bárány, G. Martin, E. Naslund, and S. Robins

Lemma q.Ë¨,
 M
pSQ N ,b −Ë − Ë
p… ‘
−Ë = M
› p
Pp”=−Ë −Ë − Ë
p… ‘
−Ë + O− Ë
»log N ‘.

We therefore see that we have established the proposition with

κa,b = B
π… cPb h(−Pb)
√…(Pb − Ë) M
› p
Pp”=−Ë −Ë − Ë
p… ‘
−Ë k
Q
j=Ë a j M
pSb j −Ë + Ë
p ‘
−Ë

= eγ~…q
√…
πþ~… h(−Pb)Ë~…

PË~√Pb − Ë M
› p
Pp”=−Ë −Ë − Ë
p… ‘
−Ë~… k
Q
j=Ë a j M
pSb j −Ë + Ë
p ‘
−Ë

(q.)

by the deﬁnition (q.…) of cP. Ì

Remark he condition that all of the a j are positive is used here only to ensure that
this last line is non-zero. In the case where the a j may be arbitrary, and thus where
the innermost sum in equation (q.) may equal ¨, it is possible that modifying QN ,b
and the above argument could prove the totient independence for any coeﬃcients;
however, we succeeded in getting this to work only when k ≤ q.
It is interesting to note that the methods of […], which handle primitive points in
planar convex regions that have nowhere-vanishing Gaussian curvature, involve the
analysis of zeta functions and thus are quite diﬀerent from the present methods.

References

[Ë] T. M. Apostol, Introduction to analytic number theory. Undergraduate Texts in Mathematics,
Springer-Verlag, New York–Heidelberg, Ë™8B.
[…] R. C. Baker, Primitive lattice points in planar domains. Acta Arith. Ë…(…¨Ë¨), q, …B8–q¨….
https://doi.org/10.4064/aa142-3-4
[q] H. Davenport, Multiplicative number theory, hird Ed., Graduate Texts in Mathematics, 8,
Springer-Verlag, New York, …¨¨¨.
[] P. Erdős and H. N. Shapiro, On the changes of sign of a certain error function. Canad. J. Math.
q(Ë™þË), q8þ–qÇþ. https://doi.org/10.4153/cjm-1951-043-3
[þ] G. H. Hardy and E. M. Wright, An introduction to the theory of numbers, Fih ed., he Clarendon
Press, Oxford University Press, Ë™8™.
[B] G. J. O. Jameson, he prime number theorem. London Mathematical Society Student Texts, þq,
Cambridge University Press, Cambridge, …¨¨q. https://doi.org/10.1017/CBO9781139164986
[8] E. Kranakis and M. Pocchiola, Counting problems relating to a theorem of Dirichlet. Comput. Geom.
(Ë™™), q¨™–q…þ. https://doi.org/10.1016/0925-7721(94)00013-1
[Ç] N. Le Quang and S. Robins, Macdonald’s solid-angle sum for real dilations of rational polygons.
Preprint. arxiv:1602.02681v1.
[™] F. Mertens, Über einige asymptotische Gesetze der Zahlentheorie. J. Reine Angew. Math. 88(ËÇ8),
…Ç™–qqÇ. https://doi.org/10.1515/crll.1874.77.289
[Ë¨] H. L. Montgomery, Fluctuations in the mean of Euler’s phi function. Proc. Indian Acad. Sci. Math.
Sci. ™8(Ë™Ç8), Ë–q, …q™–…þ. https://doi.org/10.1007/BF02837826
[ËË] H. L. Montgomery and R. C. Vaughan, Multiplicative number theory. I. Classical theory. Cambridge
Studies in Advanced Mathematics, ™8, Cambridge University Press, Cambridge, …¨¨8.
[Ë…] I. Niven, H. S. Zuckerman, and H. L. Montgomery, An introduction to the theory of numbers, Fih
ed., John Wiley & Sons, Inc., New York, Ë™™Ë.
[Ëq] M. Nosarzewska, Évaluation de la diﬀérence entre l’aire d’une r´gion plane convexe et le nombre des
points aux coordonnées entières couverts par elle. Colloq. Math. Ë(Ë™Ç), q¨þ–qËË.
https://doi.org/10.4064/cm-1-4-305-311

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.

Primitive Points in Rational Polygons …Ë

[Ë] S. S. Pillai and S. D. Chowla, On the error terms in some asymptotic formulae in the theory of
numbers (Ë). J. Lond. Math. Soc. þ(Ë™q¨), …, ™þ–Ë¨Ë. https://doi.org/10.1112/jlms/s1-5.2.95
[Ëþ] J. L. Raabe, Zurückführung einiger Summen und bestimmten Integrale auf die Jacob Bernoullische
Function. J. Reine Angew. Math. …(ËÇþË), qÇ–q8B. https://doi.org/10.1515/crll.1851.42.348
[ËB] C. A. Rogers, Existence theorems in the geometry of numbers. Ann. of Math. Ç(Ë™8), ™™–Ë¨¨….
https://doi.org/10.2307/1969390
[Ë8] A. Walﬁsz, Weylsche Exponentialsummen in der neueren Zahlentheorie. Mathematische
Forschungsberichte, XV, VEB Deutscher Verlag der Wissenschaen, Berlin, Ë™Bq.

Rényi Institute of Mathematics, Hungarian Academy of Sciences, H-ËqB Budapest, Pf. Ë…8, Hungary

Department of Mathematics, University College London, Gower Street, London, WCËE BBT, England
e-mail : barany@renyi.hu

Department of Mathematics, University of British Columbia, Room Ë…Ë, Ë™Ç Mathematics Road, Vancouver,
BC VBT ËZ…, Canada
e-mail : gerg@math.ubc.ca naslund.eric@gmail.com

Instituto de Mathematica e Estatistica, Universidade de São Paulo, ¨þþ¨Ç-¨™¨ São Paulo, Brazil
e-mail : srobins@ime.usp.br

Downloaded from https://www.cambridge.org/core. 09 Jun 2020 at 17:13:04, subject to the Cambridge Core terms of use.
