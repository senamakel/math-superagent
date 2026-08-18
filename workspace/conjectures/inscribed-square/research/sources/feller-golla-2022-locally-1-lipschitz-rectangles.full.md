<!-- source: https://arxiv.org/pdf/2003.01590 | converted from PDF -->

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED
RECTANGLES

PETER FELLER AND MARCO GOLLA

Abstract. We discuss diﬀerences between genera of smooth and locally-ﬂat
non-orientable surfaces in the 4–ball with boundary a given torus knot or 2–
bridge knot. In particular, we establish that a result by Batson on the smooth
non-orientable 4–genus of torus knots does not hold in the locally-ﬂat category.
We further show that certain families of torus knots are not the boundary of
an embedded M¨obius band in the 4–ball and other 4–manifolds.
Our investigation of non-orientable surfaces with boundary a given torus
knot is motivated by our approach to unify the proof of the existence of in-
scribed squares and of inscribed rectangles with aspect ratio √3 in Jordan
curves with a regularity condition. This generalizes a result by Hugelmeyer
for smooth Jordan curves.
 1. Introduction

Let Γ ⊂ R2 be a Jordan curve; that is, Γ is the image of an injective continuous
function S1 → R2. We say that Γ is locally 1–Lipschitz if for each point p ∈ Γ there
is a neighbourhood U of p such that Γ ∩ U is the graph of a 1–Lipschitz function.
(See Deﬁnition 3.1 below.) A Euclidean rectangle in R2 is said to be inscribed in
Γ if its four corners belong to Γ. The aspect ratio of a rectangle whose sides have
lengths a and b is b/a; note that this is only deﬁned up to reciprocals.

Theorem 1.1. Let Γ ⊂ R2 be a locally 1–Lipschitz Jordan curve. Then, for all
integers n ≥ 2, there exists an integer 1 ≤ k ≤ n − 1 such that Γ has an inscribed
rectangle with aspect ratio tan ( kπ
2n ).
In particular, Γ has an inscribed square and an inscribed rectangle with aspect
ratio √3.

In fact, as we will see below, we will give a condition on the curve Γ (see Propo-
sition 2.5) for which the conclusion of Theorem 1.1 holds, and we will prove that
locally 1–Lipschitz Jordan curves satisfy this condition. At this point, we do not
know of any curve Γ for which our scheme of proof does not apply; see Remark 2.6.
For instance, while not all polygonal Jordan curves are locally 1–Lipschitz, they sat-
isfy the same condition, and therefore the statement can be extended to polygonal
curves.
The condition on Γ is chosen such that the proof of the theorem reduces to the
following result.

Theorem 1.2. Let K ⊂ S2 × S1 be the torus knot K1,2n in S2 × S1. If n is not a
square, then K does not bound a locally-ﬂat M¨obius band in D3 × S1.

Here, for coprime integers p and q, and identifying S2 = C ∪ {∞}, the torus knot
Kp,q in S2 × S1 is {(
e2πipt, e
2πiqt) ∣
∣ t ∈ R} ⊂ S2 × S1. Our proof of Theorem 1.2
combines a branched double cover construction and a very simple intersection form
obstruction. While our proof does not work when n is a square, we believe that the
result also holds without that assumption.
Theorem 1.1 is motivated by a question posed by Toeplitz in 1911, often referred
to as the square peg problem: does every Jordan curve contain an inscribed square?

1arXiv:2003.01590v2  [math.GT]  11 Apr 2021
2 PETER FELLER AND MARCO GOLLA

While the question remains open in full generality, it has been resolved in the
positive for many classes of curves. We refer to Matschke’s excellent survey on the
topic [Mat14]. See also Schwartz [Sch18] and Tao [Tao17] for further progress.
The starting point of the present article was a beautiful idea of Hugelmeyer [Hug18],
which is the ﬁrst article to address Toeplitz’s question for rectangles of a ﬁxed as-
pect ratio r > 1. In the paper, Hugelmeyer establishes Theorem 1.1 for n ≥ 3 (the
case n = 2 was previously known) and smooth Jordan curves, using an idea of proof
in line with Vaughan’s proof [Mey81, Mat14] of the following result. Every Jordan
curve has an inscribed rectangle. In his surprising proof, Vaughan elegantly reduces
this result to the statement that there is no proper embedding of the M¨obius band
into the upper-half space R2 × [0, ∞).
In more detail, in case Γ is smooth, Hugelmeyer gives a reduction of Theorem 1.1
to the smooth analog of Theorem 1.2. He then observes that, in the smooth setting
and for n ≥ 3, Theorem 1.2 follows from a result by Batson [Bat14]: for n ≥ 3, the
torus knot T2n−1,2n in the 3–sphere S3 = ∂B4 does not arise as the boundary of a
smoothly embedded M¨obius band in the 4–ball B4.
The need for locally-ﬂat statements in our approach, in contrast to Batson’s
smooth results, as well as the diﬀerences between the smooth and topological
orientable 4-genus [Rud84, BFLL18], motivated us to compare locally-ﬂatly and
smoothly embedded non-orientable surfaces in the 4–ball.
For a knot K in S3, let γ4(K) denote the smallest ﬁrst Betti number among
smooth non-orientable surfaces in B4 with boundary K ⊂ S3 = ∂B4. Similarly,
denote by γtop
4 (K) the smallest ﬁrst Betti number among locally-ﬂat non-orientable
surfaces in B4 with boundary K ⊂ S3 = ∂B4.

Theorem 1.3. For each integer n ≥ 5, we have γtop
4 (T2n−1,2n) < γ4(T2n−1,2n).

Batson proved in [Bat14] that γ4(T2n−1,2n) = n − 1 for all integers n > 1. We do
not determine γtop
4 (T2n−1,2n), but only show that it is at most n − 2. We believe
that the following two questions are open. Does T9,10 bound a locally-ﬂat punctured
Klein bottle? Are there torus knots that bound a locally-ﬂat M¨obius band in B4,
but not a smooth one?
In general we study which torus knots in S3 arise as the boundary of a locally-
ﬂat M¨obius band in B4. In particular in Section 5.2, we focus on the torus knots
T2n,2n+1: in contrast to T2n−1,2n, it is in general unknown which ones bound smooth
M¨obius bands in B4.
For example, we generalize the folklore result that neither T4,5 nor T5,6 ⊂ S3

bounds a locally-ﬂat M¨obius band in B4.

Proposition 1.4. Let p ≡ 5 (mod 8) be a positive integer. Then Tp,p±1 does not
bound a locally-ﬂat M¨obius band in B4.

Branched covers feature prominently in most topological proofs. We use them
in combination with correction terms in Heegaard Floer homology and with Don-
aldson’s diagonalisation theorem to close the paper with two results on torus knots
and 2-bridge knots which cannot bound smooth M¨obius bands in B4.

Addendum. Since the appearance of this manuscript, Greene and Lobb have used
symplectic topology to extend Hugelmeyer’s result from [Hug18] to cyclic quadri-
laterals inscribed in smooth curves [GL20b, GL20a]. Our main results on inscribed
quadrilaterals, Theorem 1.1 and Proposition 2.5, go in a diﬀerent direction, since
we aim at weakening the regularity assumption on the curve. Our results on non-
orientable surfaces in 4-manifolds are completely independent of their work.

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 3

Structure. In Section 2 we prove Proposition 2.5, which contains the key technical
property of curves that allows us to link metric geometry to topology. In Section 3,
we prove Theorem 1.1, assuming Theorem 1.2, which is proved in Section 4. In Sec-
tion 5 we prove Theorem 1.3, along with a number of obstructions to the existence
of smooth and locally-ﬂat M¨obius bands in B4 bounding torus knots and 2–bridge
knots in S3.

Acknowledgements. PF thanks Luca Studer for introducing him to Vaughan’s
beautiful proof that every Jordan curve has an inscribed square and the survey by
Matschke. We thank Andr´as Stipsicz for inquiring about locally-ﬂat non-orientable
surfaces ﬁlling torus knots. PF gratefully acknowledges support by the Swiss Na-
tional Science Foundation Grant 181199. This project started when PF visited the
University of Nantes, and was partially carried on while MG visited ETH and when
both authors stayed at MPIM. We thank all three institutions for their support.

2. From curves to M¨obius bands

In this section, we ﬁx a continuous injection α : S1 → C and denote the image
of α (by deﬁnition, a Jordan curve) as Γ ⊂ C.
Let M denote S1 × S1/(Z/2Z), that is, the quotient of S1 × S1 by the relation
(x, y) ∼ (y, x). Note that M is a M¨obius band. For each positive integer n, we
consider the map

Ψn : M → C2, {s, t} ↦→ ( α(s) + α(t)
2 , (α(s) − α(t))2n) .

Note that the image of Ψn does not depend on the parametrization α of Γ.

Remark 2.1. The maps Ψn were studied by Hugelmeyer [Hug18], extending an idea
of Vaughan; compare [Mey81, Mat14]. A crucial observation is the following. For
n ≥ 2, the map Ψn is injective if and only if there exists an integer 1 ≤ k ≤ n − 1
such that Γ has an inscribed rectangle with aspect ratio tan ( kπ
2n ).

2.1. The image of Ψ1 is topologically locally ﬂat. Denote with Ok the origin
of Rk.

Deﬁnition 2.2. Fix integers m > n > 0. A subset F of an m–manifold M is called
locally-ﬂat (of dimension n) at x ∈ F if there exist an open neighbourhood U ⊂ M
of x such that (U, U ∩ F ) is homeomorphic to an open subset of (Rm, R≥0 × Rn−1 ×
{Om−n}). The subset F is called locally-ﬂat if it is locally-ﬂat for all x ∈ F .
Two locally-ﬂat submanifolds F, F ′ without boundary, of dimension n and n′

respectively, are said to intersect transversely in M if: either F ∩ F ′ is empty, or
n+n′ ≥ m and every point x ∈ F ∩F ′ has a neighbourhood U ⊂ M such that (U, U ∩
F, U ∩F ′) is homeomorphic to an open subset of (Rm, Rn×{Om−n}, {Om−n′}×Rn′).

Lemma 2.3. Ψ1 is injective and its image M := Ψ1 (M) ⊂ C2 is a locally-ﬂat
M¨obius band. Furthermore, there is a regular neighbourhood N of C × {0} such that
∂N intersects M transversely and the pair (N, N ∩ M ) is homeomorphic to
(C × D1, {(x, y) ∈ S1 × D | |y|x2 = y}) = (C × D1, {(s, r(s
2)) | r ∈ [0, 1], s ∈ S1}) .

In particular, (∂N, M ∩ ∂N ) is homeomorphic to (C × S1, K1,2).

Here, Dr := {z ∈ C | |z| ≤ r} is the unite disc of radius r, and a closed
regular neighborhood is understood to be a subset N ⊂ C2 such that there exist a
homeomorphism Ψ : C2 → C2 with Ψ(N ) = C × Dr and Ψ restricts to the identity
on C × {0}.

4 PETER FELLER AND MARCO GOLLA

Proof. Clearly, Ψ1 is injective. The rest of the statement is easy to check when Γ
is the unit circle Γstd = S1 ⊂ C. Indeed, the image Mstd := Im(Ψ1) is a smooth
2-submanifold of C2; in particular, the M¨obius band Mstd is locally-ﬂat. And, for
N = C × D1, ∂N = C × S1 intersects Mstd transversely in
{( √3
2 e2πit, −e2πi2t) ∣
∣
∣ t ∈ R} ⊂
 √3
2 S1 × S1 ⊂ C × S1.

For the general case, let φ : C → C be a compactly supported homeomorphism
such that Γ = φ(Γstd), which exists by the Jordan–Sch¨onﬂies theorem. The state-
ment follows by identifying C2 with the space of unordered pairs C2/(Z/2Z) =
{{x, y} | x, y ∈ C} and observing that the self-homeomorphism of C2/(Z/2Z) given
by Φ({x, y}) = {φ(x), φ(y)} induces a homeomorphisms of topological pairs between
(C2, Mstd) and (C2, M ). To be explicit, (C2, Mstd) and (C2, M ) are homeomorphic
as pairs via

Ψ : C2 → C2

(z, w) ↦→
 

 φ (z ± √w
2 ) + φ (z ∓ √w
2 )

2 , (φ (z ± √w
2 ) − φ (z ∓ √w
2 ))2

 . □

2.2. The image of Ψ1 under taking powers in the second coordinate. Note
that Ψn = pn ◦ Ψ1, where pn : C2 → C2, (z, w) ↦→ (z, wn).

Lemma 2.4. Fix an n ≥ 2. If Ψn is an injection on an open subsurface S of
M \ ∂M, then Ψn(S) ⊂ C2 is a locally-ﬂat surface.

Proof. This is immediate from Lemma 2.3. For (z, w) ∈ Ψn(S), we have w ̸= 0.
Let (z, u) be a preimage of (z, w) under pn that lies in M ⊂ C2. Let U be an
open neighborhood of (z, u) that witnesses the local ﬂatness of M at (z, u) and
that maps injectively under pn. Furthermore, we choose U suﬃciently small such
that pn(U ∩ M ) = p(U ) ∩ Ψn(S). Thus, p(U ) is an open neighborhood of (z, w)
that establishes the local ﬂatness of Mn at (z, w). □

Using Lemma 2.4 and Theorem 1.2, we can obtain the following.

Proposition 2.5. Fix a Jordan curve Γ ⊂ C, an integer n ≥ 2, and a positive
real number d. Suppose that N is a regular closed neighborhood of C × {0} in C2

containing C × Dd2n such that:
• the map Ψn and ∂N are transverse;
• the pair (∂N, Im(Ψn) ∩ ∂N ) is homeomorphic to (C × S1, K1,±2n).
Then, the there exists a, b ∈ M such that Ψn(a) = Ψn(b) ∈ C × (C \ D◦
d2n ); in other
words, there exists an integer 1 ≤ k ≤ n − 1 such that Γ has an inscribed rectangle
with aspect ratio tan ( kπ
2n ) and diameter larger than d.

Here, Ψn and ∂N being transverse is deﬁned to mean that every point x ∈
Ψ−1
n (∂N ) has an open neighbourhood Ux such that Ψn restricts to an injection on
Ux with image Ψn(Ux) a locally-ﬂat surface that intersects ∂N transversely.

Proof. It suﬃces to establish the theorem for n prime. Indeed, if p is a prime
factor of n, then the non-injectivity of Ψp implies that of Ψn, since Ψn arises as the
concatenation of a map with Ψp. So, from here on, we only consider n prime.
Set X := C2 \ N ◦. Assume towards a contradiction that Γ has no inscribed
rectangle with aspect ratio tan ( kπ
2n ) of diameter larger than d. Equivalently, as in
Remark 2.1, Ψn is injective restricted to Ψ
−1
n (C×(C\D◦
d2n )). Thus, by Lemma 2.4,
Mn := Im(Ψn) ∩ X is locally-ﬂat in its interior and, by transversality of Ψn and

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 5

∂N , also at its boundary. Hence, Mn is a locally-ﬂat properly embedded surface.
It is either a closed disc or a M¨obius band, since it is homeomorphic to a closed
subsurface of M with connected boundary. Since ∂Mn = ∂N ∩ Im(Ψn) is a circle
that is not null-homotopic in ∂X = ∂N , Mn must be a M¨obius band. In conclusion,
Mn is a locally-ﬂat M¨obius band, properly embedded in X, such that the pair
(∂X, ∂Mn) is homeomorphic to (C × S1, K1,2n), which yields a contradiction since
the image of Mn under an embedding (X, ∂X) ↪→ (D3 ×S1, S2 ×S1) is a locally-ﬂat
M¨obius band in D3 × S1 that cannot exist by Theorem 1.2. □

Remark 2.6. We observe (as in Remark 2.1) that, for a Jordan curve Γ ⊂ C the
following are equivalent:

• Ψn is an injection in a neighborhood of the boundary of the M¨obius band
M;
• there exists an ε > 0 such that Γ has no inscribed rectangles with the aspect
ratios tan ( kπ
2n ) and diameter less than ε.

Now, if Γ is a Jordan curve with no ‘small’ rectangles with the aspect ratios
tan ( kπ
2n ) as above and A a neighbourhood on which Ψn is injective, then Ψn(A \
∂A) is a locally-ﬂat surface by Lemma 2.4. Any small regular neighborhood of
N of C2 × {0} can be made to have its boundary transversal to Ψn(A \ ∂A) by
a small compactly supported ambient isotopy; see [FQ90, Section 9.5]. Thus, the
ﬁrst condition in Proposition 2.5 above is automatically satisﬁed for such Γ. The
interesting question is thus the following:

Question 2.7. Can N be found so that the 1–manifold A ∩ ∂N is connected of knot
type K1,±2n?

If the answer to the question were positive, by Proposition 2.5, Γ has inscribed
rectangles with the aspect ratios tan ( kπ
n ). It seems conceivable that the answer is
always yes. We take this as an indication that at least in principle, the general case
of Γ is in the realm of being treated using this approach, and the diﬃculty lies in
under standing the knot (or link) type of A ∩ ∂N as a knot (link) in ∂N ∼= C × S1.
And so, we understand that application to 1–Lipschitz curves given in the next
section as proof of concept for this method, rather than its optimal use.

In the next section, we will study a family of Jordan curves for which we are
able to establish the conditions from Proposition 2.5.

3. Proof of Theorem 1.1

Deﬁnition 3.1. A Jordan curve Γ ⊂ C is said to be locally 1–Lipschitz if, for each
p ∈ Γ, there exist ε > 0 and an isometry (−ε, ε) × (−ε, ε) → U ⊂ C centered at p
such that, in these coordinates, Γ ∩ U is the graph of a 1–Lipschitz function.

Being locally 1–Lipschitz is a condition on Jordan curves Γ that implies that, for
suﬃciently small r, the neighborhood N := C × Dr2n is a neighborhood as required
for Proposition 2.5. For this N , the projection of Ψn(M) ∩ ∂N ⊂ C × C to the ﬁrst
coordinate corresponds to the set Γr ⊂ C of all midpoints of pairs (γ1, γ2) ∈ Γ × Γ
that are distance r apart. A key step of the proof below is the claim that Γr is a
Jordan curve in case Γ is locally 1–Lipschitz. The point is that this implies that
K := Ψn(M) ∩ ∂N is a subset of the torus Γr × S1
r2n , so, given we know K is a
connected 1–manifold in ∂N = C × S1
r2n, K must be a torus knot. We start with
the following elementary lemma.

6 PETER FELLER AND MARCO GOLLA

Lemma 3.2. Let g : R → R be 1–Lipschitz. For every t ∈ R and r ≥ 0, there exists
a unique ηr(t) ∈ [0, r/2] such that |t+ηr(t)+ig(t+ηr(t))−(t−ηr(t)+ig(t−ηr(t)))| =
r. Moreover, the map (r, t) ↦→ ηr(t) is continuous.

Proof. For existence and uniqueness, it is enough to prove the statement for t = 0.
The function |x + ig(x)) − (−x + ig(−x))|
2 = (g(x) − g(−x))2 + (2x)
2 is strictly
increasing on [0, ∞). Hence, there exists a unique η with (g(η)−g(−η))
2+(2η)
2 = r2

for every r ∈ [0, ∞). Continuity in (r, t) is easy to note. □

Proof of Theorem 1.1. Fix a parametrization α : S1 → C of a locally 1–Lipschitz
curve Γ. We aim to show that, for all n, the map Ψn is not injective. By Proposi-
tion 2.5, it suﬃces to show the following.
(1) Ψn is an injection restricted to an open neighborhood A of the boundary
of M and no m ∈ M \ A gets mapped to Ψn(A),
(2) there exists a regular neighborhood N of C × {0} such that ∂N intersects
Im(Ψn) only in Ψn(A), which is locally-ﬂat by Lemma 2.4, and the in-
tersection is transverse for all elements of Im(Ψn) ∩ ∂N = Ψn(A) ∩ ∂N ,
and
(3) the pair (∂N, ∂N ∩ Im(Ψn)) is homeomorphic to (C × S1, K1,2n).
Indeed, choosing d such that C×Dd2n ⊂ N gives the assumptions of Proposition 2.5.
The remainder of this proof is concerned with establishing (1), (2), and (3). We
use the following.
Let (x, y) be a point on Γ. By assumption, we have that in a small neighborhood
U of (x, y), Γ is given as the image of {L(t, f (t)) | t ∈ (− 3
2 ε, 3
2 ε)}, where L is an
isometry of R2 (with the Euclidean metric), ε > 0, and f : (− 3
2 ε, 3
2 ε) → R, 0 ↦→ 0
is 1–Lipschitz. In fact, we arrange that L satisﬁes L(Ustd) = U , where Ustd =
(− 3
2 ε, 3
2 ε) × i(− 3
2 ε, 3
2 ε) ⊂ C.
We choose an ε > 0 such that Γ is covered by a ﬁnite collection { 2
3 Uj}, where
each Uj is a neighborhood as described above. Furthermore, we may arrange that
for any two points on Γ of Euclidean distance less than ε there exists an index j
such that they both lie in 2
3 Uj.
Given this, we deﬁne V := C × D◦
ε2n, where D◦
ε2n ⊂ C denotes the disc centered
at 0 of radius ε2n. One checks that Vj := 2
3 Uj × D◦
ε2n yields a ﬁnite set of open
subsets of V such that Im(Ψn) ∩ V ⊂ ⋃
j Vj.
We consider one Uj. Let f and L be the 1–Lipschitz function and the isometry as
described above. Without loss of generality, we take L to be the identity. Finally,
we let ̃f : (− 3
2 ε, 3
2 ε) → S1 be the factorization of f through α; that is, we have
f = α ◦ ̃f .
For t ∈ (−ε, ε) and r ∈ [0, ε), we let ηr(t) be the unique element in [0, ε/2) such
that |(t + ηr(t) + if (t + ηr(t)) − (t − ηr(t) + if (t − ηr(t)))| = r.
(Existence and uniqueness of ηr(t) follows by applying Lemma 3.2, which also gives
continuity of (r, t) → ηr(t).) With this we can continuously parametrize Im(Ψn)∩Vj
via:
 P : (−ε, ε) × [0, ε) → C × C, (t, r) ↦→ Ψn ({ ̃f (t + ηr(t)), ̃f (t − ηr(t))}) .

In particular, P factors through

̃P : (−ε, ε) × [0, ε) → M, (t, r) ↦→ { ̃f (t + ηr(t)), ̃f (t − ηr(t))} .

With this setup one now readily veriﬁes (1), (2), and (3). We provide details.

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 7

(1). We claim that Ψn is injective on Aε := {{s, t} ∈ M ∣
∣ |α(s) − α(t)| < ε
} =
Ψ−1
n (C × D◦
ε2n ). Indeed, for {s, t} and {s
′, t
′} in Aε with Ψn({s, t}) = Ψn({s
′, t
′}),
let j be such that α(s) and α(t) are in 2
3 Uj. Note that then also α(s
′) and α(t′)
are in Uj and since they have the same midpoint as α(s) and α(t). Since L is the
identity,
 {s, t} = ̃P (Re ( α(s) + α(t)
2
 ) , |α(s) − α(t)|
)

= ̃P (Re ( α(s
′) + α(t′)
2
 ) , |α(s
′) − α(t′)|
) = {s
′, t
′}.

(2). For r ∈ (0, ε), we set N := C × Dr2n . One swiftly checks that ∂N intersects
the locally ﬂat-surface Ψn(M) ∩ V transversally. Indeed, identifying

Vj \ (C × {0}) = (−ε, ε) × i(−ε, ε) × (0, ε) × S1,

we see that ∂N ∩ (Vj \ (C × {0})) is given as (−ε, ε) × i(−ε, ε) × {r} × S1, while
Ψn(M) ∩ (Vj \ (C × {0})) is the graph of a continuous function on the ﬁrst and third
coordinate to the second and forth coordinate. In particular, every point ∂N ∩
Ψn(M) has a neighborhood W ⊂ C2 such that the triple (W, W ∩ ∂N, W ∩ Ψn(M))
is homeomorphic to (R4, R × R × {0} × R, R × {0} × R × {0}).

(3). Fix r ∈ [0, ε). Im(Ψn) ∩ C × S1
r2n projects to the ﬁrst factor C = C × {0} as
a Jordan curve. For r = 0, the projection is of course just Γ. For r > 0, using the
parametrizations P for each 2
3 Uj one sees that Ψn concatenated with the projection
to the ﬁrst factor maps

γr := {
{s, t} ∈ M ∣
∣ |α(s) − α(t)| = r} = Ψ
−1
1 (C × S1
r ) = Ψ−1
n (C × S1
r2n )

homeomorphically onto its image Γr (by point (1) above, it is injective), and Γr
is homeomorphic to S1 since it is a 1–submanifold (check in a chart 2
3 Ui) and it
is connected (since it is the image of S1 via a continuous map). Hence, K :=
Im(Ψn) ∩ C × S1
r2n is a torus knot since it is parametrized by Ψn restricted to
the simple closed curve γr and sits on the torus Γr × S1
r2n . Given that γr maps
homeomorphically to the ﬁrst factor of Γr × S1
r2n, it is clear that K is a K1,ℓ torus
knot. Finally, Ψn restricted to γr and projected to the second factor has degree
(±2n); that is, ℓ = ±2n as desired. This can for example be seen as follows.
Let φ from S1 to S1
r be deﬁned by s ↦→ α(s) − α(t(s)), where t(s) is the unique
element with |α(s) − α(t(s))| = r and t(s) lies before s on S1 (assuming ε is
suﬃciently small, we have |s − t| < 2, whenever |α(t) − α(s)| = r; hence, lying
before is well-deﬁned as the unique shortest path from t(s) to s on S1 having the
same orientation as the orientation induced by S1). The map φ is a degree-(±1)
map from S1 to S1
r . To see this, we view φ as a map to C\{0} (rather than S1
r ). The
map φ is homotopic to α(t)−p, where p ∈ C is any point in the bounded component
B of the complement of Γ, and, of course, α(t) − p has degree ±1 (that is, it induces
an isomorphism on H1(·, Z)) as desired). Indeed, one may continuously deform φ(s)
into α(s) − p via α(s) − αR(t(s)), where [0, 1] × S1 ∋ (R, t) ↦→ αR(t) is continuous,
p for R = 0 and injective on (0, 1] × S1 (in other words, it is a parametrization of
the closed disc Γ ∪ B in polar coordinates, which exists by the Jordan Schoenﬂies
theorem). Since φ has degree ±1, its 2nth power has degree ±2n. □

In the above proof we in particular noted that, for locally 1–Lipschitz Γ, there
exists an ε > 0 such that, for all r < ε, Γ has no inscribed rectangle with diameter
r. It would be interesting to compare the condition Γ has no inscribed rectangles

8 PETER FELLER AND MARCO GOLLA

of diameter r with the condition of non-existence of special trapezoids considered
by Matschke in [Mat11, Chapter 2, Theorem 2.5] (see also [Mat14, Theorem 4]).

4. M¨obius bands in D3 × S1

The goal of this section is to prove Theorem 1.2, which states that, for n ∈ Z>0
not a square, the torus knot K1,2n ⊂ S2 × S1 does not bound a locally-ﬂat M¨obius
band in D3 × S1.
Unless explicitly stated, homology will be taken with integer coeﬃcients. We
will keep the notation throughout the section.
We will argue by contradiction. To this extent, suppose that j : M ↪→ D3 × S1

is a locally ﬂat M¨obius band whose boundary is K; since K has algebraic winding
number 2n, it is easy to see that the map j∗ : H1(M ) → H1(D3 ×S1), after choosing
a generator for H1(M ; Z) ∼= Z and H1(D3 × S1; Z) ∼= Z, is multiplication by n. We
call EK the exterior of K in S2 × S1, and EM the exterior of M in D3 × S1.

Lemma 4.1. We have H1(EK) ∼= Z ⊕ Z/2nZ and H1(EM ) ∼= Z ⊕ Z/2Z. In both
cases, the torsion subgroup is generated by the meridian µ of K and the free part
can be chosen to be generated by a curve φ = {⋆} × S1 ⊂ S2 × S1 ⊂ D3 × S1.

It follows that we can consider double covers of D3 × S1, branched over M ,
whose boundaries are double covers of S2 × S1, branched over K. Such covers are
identiﬁed with homomorphisms π1(EM ) → Z/2Z that map [µ] to 1; since Z/2Z is
abelian, these homomorphisms factor through H1(EM ) = ⟨[φ], [µ]⟩.
We will refer to a speciﬁc double cover, denoted with Σ(M ), namely the one
associated to the map H1(EM ) → Z/2Z that sends [φ] to 0. It is now easy to
see that this induces a unique surjective homomorphism π1(EK) → Z/2Z. We
denote with Σ(K) associated double cover, i.e. ∂Σ(M ). We also denote with ˜EM
the double cover of EM associated to the homomorphism above.

Proof. Let N be a tubular neighbourhood of M (for uniqueness and existence of
such, also called normal vector bundles, see [FQ90, Section 9.3]). We know that N
retracts onto M , and that its boundary is the union of a neighbourhood of K in
S2 × S1 and the ‘vertical’ boundary V , which is the non-orientable circle bundle
over M . In particular, V retracts onto a Klein bottle, and H1(V ) = Z ⊕ Z/2Z.
More precisely, the torsion subgroup in H1(V ) is generated by the ﬁbre of the circle
bundle; since a meridian of K gives a ﬁbre, we see that the meridian of K generates
the torsion of H1(V ).
From the Mayer-Vietoris exact sequence for D3 × S1 = N ∪V (EM ) we extract

H2(D3 × S1) = 0 −→ H1(V ) −→ H1(N ) ⊕ H1(EM ) −→ Z = H1(D3 × S1) −→ 0.

Since the last group in the sequence is free, the sequence splits, and the inclusion
V ↪→ EM induces an isomorphism of the torsion part of H1(V ) onto the torsion of
H1(EM ).
Now observe that one ﬁbre φ = {⋆} × S1 of S2 × S1 is disjoint from K by
construction; it is easy to see (e.g. since the map H1(EK) → H1(S2 × S1) is
onto) that [φ] generates the free part of H1(EK). Composing with the inclusions
EK ↪→ EM and S2 × S1 ↪→ D3 × S1 also shows that [φ] generates (a choice of) the
free part of H1(EM ). □

Lemma 4.2. The 3–manifold Σ(K) is obtained by doing (−n)–surgery on the com-
ponents of the T2,2n torus link in S3; in particular, b1(Σ(K)) = 1.

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 9

Proof. We refer to Figure 1. The knot K is presented as the closure of the 2n–
braid σ1 · · · σ2n−1, after doing 0–surgery on the axis A. Since the link comprising
A and K (viewed as a link in S3) is symmetric, Σ(K) is presented as surgery on
the closure of the braid (σ1 · · · σ2n−1)2, i.e. the T2,2n torus link. Determining the
surgery coeﬃcient is an easy calculation (see [Rol76, Section 10.C]).
Now, this gives a presentation of H1(Σ(K)) by the matrix
( −n n
n −n
 ) ,

hence H1(Σ(K)) = Z ⊕ Z/nZ. □

Let C be the 4–manifold with boundary Σ(K) given by the surgery presentation
of Lemma 4.2 above (also called the trace of that surgery).

Lemma 4.3. The 4–manifold C has homology groups H0(C) ∼= Z, H2(C) ∼= Z
⊕2,
and all its other homology groups vanish. The inclusion of Σ(K) into C induces
an injection H2(Σ(K)) → H2(C). Moreover, C contains a surface S of self-
intersection −n; that is [S] · [S] = −n, where · denotes the intersection form on
H2(C).

Proof. This is immediate from the fact that C has a handle decomposition with no
1–, 3–, or 4–handles, and with two 2–handles. The surface of self-intersection −n is
obtained by capping oﬀ a Seifert surface of either attaching circle (see Figure 1(C))
with the core of the corresponding 2–handle. □

Lemma 4.4. The group H3( ˜EM ; Z/2Z) is trivial.

Proof. We look at the Gysin sequence associated to the double cover ˜EM → EM :

H3(EM ; Z/2Z) −→ H3( ˜EM ; Z/2Z) −→ H3(EM ; Z/2Z);

thus, it suﬃces to know that H3(EM ; Z/2Z) = 0. In fact, from the Mayer–Vietoris
long exact sequence of D3 × S1 = N ∪ EM , we extract

0 = H3(V ; Z/2Z) −→ H3(N ; Z/2Z) ⊕ H3(EM ; Z/2Z) −→ H3(D3 × S1; Z/2Z) = 0,

which implies the claim. □

Lemma 4.5. We claim the following facts about the homology of Σ(M ).
(1) The third homology group H3(Σ(M )) is torsion, and has odd order. It
follows that also H 3(Σ(M )) and H1(Σ(M ), Σ(K)) are torsion.
(2) The second homology group H2(Σ(M )) is torsion, and b1(Σ(M )) = 1.

Proof of Lemma 4.5. To prove point (1), we consider the Mayer–Vietoris long exact
sequence associated to Σ(M ) = ˜N ∪ ˜V ˜EM , where ˜N is a neighbourhood of the
branching set ˜M of Σ(M ) → D3 × S1. Like above, the neighborhood ˜N retracts
onto ˜M , and ˜V retracts onto a Klein bottle. We then have

H3( ˜EM ) ⊕ H3( ˜N ) −→ H3(Σ(M )) −→ H2( ˜V ) = 0;

the claim follows since H3( ˜EM ) is torsion of odd order (H3( ˜EM ; Z/2Z) = 0) and
H3(N ) = 0. The second part of the claim follows from the universal coeﬃcient
theorem and Poincar´e–Lefschetz duality.
We now claim he map H1(Σ(K); Q) → H1(Σ(M ); Q) induced by the inclu-
sion is onto: this follows immediately from the long exact sequence for the pair
(Σ(M ), Σ(K)) and point (1):

H1(Σ(K); Q) −→ H1(Σ(M ); Q) −→ H1(Σ(M ), Σ(K); Q) = 0.

10 PETER FELLER AND MARCO GOLLA

± 1
2n ...
 f
(a) A surgery presen-
tation of T2n,2n±1 ⊂
S3 (if f = 1) and of
K1,2n ⊂ S2 × S1 (if
f = 0).
 ± 1
2n ...

f

(b) The same surgery
presentations of
T2n,2n±1 and K1,2n,
after an isotopy.
 ± 2
2n ...
 f ∓n

f ∓n

(c) A surgery presen-
tation of Σ(T2n,2n±1)
(if f = −1) and
Σ(T1,2n) (if f = 0).
(The thin curve is aux-
iliary.)

Figure 1. The 4–manifold C from Lemma 4.3 (f = 0) and the
4–manifold W from Lemma 5.3 (f = 1) as traces of surgery pre-
sentations. The picture represents closures of 2n–braids, and each
box represents a fraction of a full twist.

As a consequence, b1(Σ(M )) ≤ 1.
Finally, to prove (2), observe that bk(Σ(M )) = 0 for each k ≥ 3 (the case
k = 3 is point (1) above), b1(Σ(M )) ≤ 1, and b0(Σ(M )) = 1 (Σ(M ) is connected).
Since Σ(M ) is the double cover of D3 × S1 branched over M , and that all three
of χ(D3 × S1), χ(M ), and χ(V ) vanish. In particular, χ(Σ(M )) = 0, too, and
therefore b2(Σ(M )) = b1(Σ(M )) − 1; however

0 ≤ b2(Σ(M )) = b1(Σ(M )) − 1 ≤ 1 − 1 = 0;

Therefore b1(Σ(M )) = 1 and b2(Σ(M )) = 0. □

Let us call X the 4–manifold obtained by gluing Σ(M ) and −C (the manifold
given by C with reversed orientation) along Σ(K).

Lemma 4.6. The second homology group H2(X; Q) is 1–dimensional.

Proof. We look at the Mayer–Vietoris long exact sequence; keeping in mind that
H∗(C) = H∗(−C), that H1(C) = 0, and that H2(Σ(M ); Q) = 0 (Lemma 2), we
obtain:

H2(Σ(K); Q) −→ H2(C; Q) −→ H2(X; Q) −→ H1(Σ(K); Q) −→ H1(Σ(M ); Q).

The ﬁrst map and the last map are injections by Lemma 4.3 and Lemma 2, respec-
tively. We therefore have a short exact sequence

H2(Σ(K); Q) −→ H2(C; Q) −→ H2(X; Q),

where the second vector space has dimension 2 by Lemma 4.3, hence b2(X) = 1. □

Proof of Theorem 1.2. Since −C ⊂ X, X contains a surface of self-intersection +n,
by Lemma 4.3. However, b2(X) = 1, so the intersection form is unimodular of rank
1, and it contains a vector of positive square, so it is ⟨+1⟩. This contradicts the
existence of a vector of square +n, since n is not a square. □

We note that Proposition 5.6, given below, provides another proof of Theo-
rem 1.2, for n a prime, while Proposition 1.4 implies Theorem 1.2 for n ≡ 1, 2
(mod 4).
 NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 11

5. Non-orientable 4–genus for torus knots in S3

In this section we discuss non-orientable 4–genus for torus knots in S3. In Sub-
section 5.1, we show that for torus knots the notion of non-orientable 4–genus
depends on the choice of category by establishing the existence of locally-ﬂat sur-
faces in B4 with boundary certain torus knots. In contrast, in Subsection 5.2, we
discuss obstructions (in both categories) for the existence of M¨obius bands in B4

with boundary a given knot.

5.1. Proof of Theorem 1.3. The following proposition is a strengthening of The-
orem 1.3.

Proposition 5.1. For integers n ≥ 5, we have γtop
4 (T2n−1,2n) ≤ n − 2 < n − 1 =
γ4(T2n−1,2n). In fact, there exists a non-orientable connected locally-ﬂat surface
Σ ⊂ B4 with b1(Σ) = n − 2 such that ∂Σ = T2n−1,2n and π1(B4 \ Σ) ∼= Z/2Z.

Remark 5.2. Recently, Lobb observed in [Lob19] that γ4 is smaller on torus knots
than previously conjectured by Batson in [Bat14]. However, one may ask whether
the conjecture holds when restricting to surfaces with complements that have cyclic
fundamental group. (Note that, by the Mayer–Vietoris sequence, the ﬁrst homology
of the complement of such a surface is always Z/2Z.) The second assertion of the
above proposition, implies that even in this more restrictive setup, the topologically
locally-ﬂat quantity is strictly smaller than the corresponding smooth one. Note
that Proposition 1.4 at least says that if 2n − 1 ≡ 5 (mod 8), then we cannot hope
to decrease the locally-ﬂat non-orientable genus all the way down to 1.

Proof of Proposition 5.1. The equality n − 1 = γ4(T2n−1,2n) is due to Batson. For
the upper bound on the topological cross cap number, we ﬁnd a non-orientable
spanning surface S ⊂ S3 for T2n−1,2n with b1(S) = n with the following property:
there is a separating simple closed curve γ ⊂ S ⊂ S3 with trivial Alexander poly-
nomial, such that one of the two connected components of S \ γ is a once-punctured
torus.
We modify S by replacing the once-punctured torus in S3 with the locally-ﬂat
disc in B4 with boundary γ. By doing so, we ﬁnd a locally-ﬂat non-oriented surface
Σ ⊂ B4 with b1(Σ) = n − 2 that ﬁlls T2n−1,2n. The existence of such a disc
is guaranteed by a consequence Freedman’s celebrated disk theorem: knots with
Alexander polynomial one are topologically slice. In fact, a knot K has Alexander
polynomial 1 if and only if, there exists a locally-ﬂat disc D ⊂ B4 with boundary
K such that π1(B4 \ D) ∼= Z; see [Fre82, Theorem 1.13]. A Seifert–van Kampen
calculation allows to check that the complement of Σ (pushed into B4 to be properly
embedded) has cyclic fundamental group; this follows from the fact that π1(B4 \
D) ∼= Z. In the rest of the proof we implement this in detail.
We ﬁrst describe a (non-orientable) spanning surface S for T2nk−1,2n for k ≥ 0.
While we are interested in the case k = 1, it is instructive to see that all of these
are built from the case k = 0. For this, we view T2nk−1,2n as the closure of the 2n–
stranded braid (σ1σ2 · · · σ2n−1)
2kn−1. For k = 0, we take S to be the checkerboard
surface for the standard diagram of the braid closure of (σ1σ2 · · · σ2n−1)−1 that
misses the braid axis. For k ≥ 1, we take S to be the surface obtained from the one
for k = 0 by k–surgery along the braid axis; i.e. by adding k positive full twists as
depicted in Figure 2. Note that b1(S) = n.
Next, we deﬁne an orientable, incompressible subsurface F of S with b1(F ) =
n − 1. Let α1, α2, . . . , αn−1 be the simple closed curves depicted in Figure 2, and
take F to be a neighborhood of their union; in particular, the homology classes of
the αi constitute a basis for H1(F ; Z). We focus on F and try to ﬁnd a separating

12 PETER FELLER AND MARCO GOLLA

k full twists

(a) The spanning surface S (gray).
 α1
 α2

(b) The curves αi: αi+1 is a copy
of αi shifted down by two strands.

Figure 2. The surface S and the curves αi on S. The curves αi
and αi+1 intersect in one point. The box represents k positive full
twists on 2p strands.

curve in F with Alexander polynomial one that cuts out a once-punctured torus.
The boundary of a once-punctured torus T is a knot with Alexander polynomial 1
if and only if one (and thus all) matrix A representing the Seifert form on T satisﬁes

(1) det(t
1/2A − t−1/2AT ) = 1.

Therefore, ﬁnding such a once punctured torus amounts to ﬁnding a pair of once-
intersecting curves β1 and β2 in F such that, if A is the matrix representing the
restriction of the Seifert form on F to span{[β1], [β2]} ⊂ H1(F, Z), then A satis-
ﬁes (1). In fact, it suﬃces to ﬁnd a rank-two subgroup H of H1(F ; Z) on which
the Seifert form is given by a bilinear form that satisﬁes (1) since any pair of
such homology classes can be represented by once intersecting simple closed curve;
see [FL18, Proposition 9] or [FM16, last paragraph of the proof of Proposition 6]
for details. Consequently, for the rest of the proof, we only concern ourselves with
the Seifert form on F and subgroups H as described above.
The Seifert form of H1(F ; Z) with respect to the basis ([α1], . . . , [αn−1]) is

Mk = M0 + Mtwist =
 





 −1 −1 0 0
0 −1 −1 0
0 0 −1 −1 . . .
 




 + k
 





 4 4 4
4 4 4 · · ·
4 4 4
... . . .
 




 ;

in particular, for n = 5

(2) Mk =
 




 4k − 1 4k − 1 4k 4k
4k 4k − 1 4k − 1 4k
4k 4k 4k − 1 4k − 1
4k 4k 4k 4k − 1
 



 .

We note that M0 + M T
0 is negative deﬁnite. In fact, for k = 0, F is the minimal
Seifert surface of the T2,−n+1 torus link.
We have now reduced the problem to the following linear algebra question: for
n ≥ 5 and k = 1, do there exist vectors a and b in Z
n−1 such that a
T Mka = 0,
a
T Mkb = 0, and b
T Mka = ±1? And, once we have such an H for n = 5, we have
it for all n ≥ 5 since Mk for n = 5 is the top-left 4 × 4 sub-matrix of Mk for n ≥ 5.

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 13

Hence, we conclude the proof by noting that the following pair of vectors has the
desired property: (a = (−1, −1, 0, 1)T , b = (4, 1, 2, −4)
T ). □

5.2. Torus knots that do not bound M¨obius bands. Recall that Batson [Bat14]
proved that γ4(T2n−1,2n) = n − 1 for each n ≥ 2; however, neither his result nor
subsequent related developments [OSSz17, GM18] say anything about γ4(T2n,2n+1).
For this reason, for most of this section we focus on ﬁnding values of n for which
we can prove that γtop
4 (T2n,2n+1) > 1.
We begin with a statement about double covers of torus knots T2n,2n±1. Recall
that, if p is even and q is odd and coprime with p, then |det Tp,q| = |q|. Recall also
that the double cover of S3 branched over Tp,q is the manifold Σ(2, p, q), i.e. the
link of the singularity of {x
2 + yp + zq = 0} ⊂ C3 at the origin.

Lemma 5.3. Let n ≥ 1 be an integer. The 3–manifold Σ(2, 2n, 2n ± 1) is the
boundary of a 4–manifold W with H1(W ) = H3(W ) = 0 and whose intersection
form is represented by the matrix ( ∓n − 1 n
n ∓n − 1 ). In particular, H1(Σ(2, 2n, 2n±
1)) is cyclic of order 2n ± 1.

Proof. The 4–manifold W is given as the trace of the surgery in Figure 1. We ﬁrst
unknot T2n,2n±1 with an axial surgery (left); the corresponding link is symmetric,
so we swap its components (center); ﬁnally, we branch double cover over the axis
(right). The framings are easily computed (see, for example, [Rol76, Section 10.C])
to be ∓n−1 for each of the two 2–handles, and their linking number is ±n (the signs
are coherent with the sign determining the knot). Up to changing the orientation
of one of the two components, we can always change the signs oﬀ the diagonal, so
the intersection form is presented by the matrix V = ( ∓n − 1 n
n ∓n − 1 ).
Adding the second row of V ±1-times to the ﬁrst and then adding the ﬁrst row
n-times to the second yields V ∼ ( −1 ∓1
0 ∓2n − 1 ). Hence H1(Σ(2, 2n, 2n ± 1)) ∼=
Z/(2n ± 1)Z as claimed. □

In what follows, given a rational number q, we denote with ⟨q⟩ the bilinear form
x ⊗ y ↦→ xqy; we use the same notation for bilinear forms that take values in Z (like
the intersection form of a 4–manifold with b2 = 1) and for those that take values in
Q/Z (like the linking form λY of a rational homology 3–sphere Y with cyclic H1).
We denote with ( p
q ) the Jacobi symbol. We say that a linking form λY represents s
as a square if there exists a torsion element x ∈ H1(Y ) such that λY (x, x) = s. For
any integer p > 0 dividing the order |G| of a ﬁnite Abelian group G with a bilinear
form λ to Q/Z, we take its reduction modulo p to be the Q/Z–valued bilinear form
λp on G ⊗ Z/pZ given by (x ⊗ 1) ⊗ (y ⊗ 1) ↦→ λ(x, y) |G|
p . Note that, by deﬁnition,
if λ represents k
|G| as a square, then λp represents k
p as a square.
The following statement is a special case of a result of Murakami and Ya-
suhara [MY00].

Proposition 5.4 ([MY00, Corollary 2.7]). Let K ⊂ S3 be a knot that bounds a
locally-ﬂat M¨obius band in B4. Then there is a λΣ(K)–orthogonal decomposition
H1(Σ(K)) = G ⊕ H where H has square order and λΣ(K)|G represents 1
|G| or − 1
|G|
as a square.
In particular, if det K is square-free, then the linking form on Σ(K) represents
1
|det K| or − 1
|det K| as a square.

We will need the following elementary number theory calculation.

Lemma 5.5. Let p be a prime and λ be a linking form on Z/pZ that represents
− 1
p as a square.

14 PETER FELLER AND MARCO GOLLA

(1) If p ≡ 3 (mod 8), then λ represents 2
p as a square, but not − 2
p .
(2) If p ≡ 5 (mod 8), then λ represents neither 2
p nor − 2
p as squares.
(3) If p ≡ 7 (mod 8), then λ represents − 2
p as a square, but not 2
p .

Proof. Since λ represents − 1
p , λ is isomorphic to ⟨− 1
p ⟩; that is, λ(x, x) = − x2
p for
every x ∈ Z/pZ, and 2
p (respectively, − 2
p ) is represented as a square if and only if
( −2
p ) = 1 (resp. ( 2
p ) = 1).
It is well-known that ( −1
p ) = 1 if and only if p ≡ 1 (mod 4), and that ( 2
p ) = 1 if
and only if p ≡ ±1 (mod 8) (see, for instance, [HW08, Theorems 82 and 95]). Using
multiplicativity of Legendre symbols, we quickly derive all three statements. □

We can now prove Proposition 1.4 from the introduction; that is, we show that
Tp,p±1 does not bound a M¨obius band if p ≡ 5 (mod 8).

Proof of Proposition 1.4. Call Σ = Σ(2, p, p ± 1) and λ = λΣ its linking form. By
Lemma 5.3, H1(Σ) is cyclic of order p. Suppose towards a contradiction that Tp,p±1
is the boundary of a locally ﬂat M¨obius band. By Proposition 5.4, there is a λ–
orthogonal decomposition H1(Σ) = G ⊕ H, where H has square order and λ|G
represents 1
|G| or − 1
|G| . Since p ≡ 5 (mod 8) and all odd squares are congruent to
1 modulo 8, G is not the trivial group. In fact, |G| ≡ 5 (mod 8). This implies that
either:

(i) |G| is divisible by a prime q ≡ 5 (mod 8), or
(ii) |G| is divisible by two primes q1 ≡ 3 (mod 8) and q2 ≡ 7 (mod 8).

We claim that, λ|G represent neither 2
|G| nor − 2
|G| as a square. We treat cases (i)
and (ii) separately using reduction modulo q and q1 and q2, respectively.
In case (i), we reduce λ modulo q. Since λ|G represents 1
|G| or − 1
|G| as a square,
its reduction modulo q is a quadratic form on Z/qZ that represents 1
q or − 1
q (and
hence both, since −1 is a square mod q) as a square, therefore by Lemma 5.5(2), it
represent neither 2
q nor − 2
q as a square. Hence, λ|G represent neither 2
|G| nor − 2
|G|
as a square.
In case (ii), we reduce λ modulo q1 and modulo q2. If λ|G represents − 1
|G| as a
square, its reduction modulo q1 cannot represent − 2
q1 as a square by Lemma 5.5(1)
and its reduction modulo q2 cannot represent 2
q2 as a square by Lemma 5.5(3).
Similarly, if λ|G represents 1
|G| as a square, its reduction modulo q2 cannot represent
− 2
q2 as a square and its reduction modulo q1 cannot represent 2
q1 as a square. Hence,
λ|G represents neither 2
|G| nor − 2
|G| as a square.
Next we derive from Lemma 5.3 that λΣ does represent 2
|G| or − 2
|G| as a square,
which leads to the desired contradiction.
We begin with the case of Tp,p+1. Call n = p+1
2 . In this case, Σ(2, 2n − 1, 2n)
bounds a 4–manifold W with H1(W ) = 0 and intersection form presented by( n − 1 n
n n − 1 ), and therefore the linking form of Σ(2, 2n − 1, 2n) is presented by

1
p ( n − 1 n
n n − 1 ). In particular, it represents n−1
p as a square. Since 2(n − 1) =
2n − 2 ≡ −1 (mod p), the linking form represents n−1
p if and only if it represents
− 2
p as a square. By restricting to G, we see that λ|G represents − 2
|G| as a square,
which is a contradiction.
Let us now look at the case of Tp,p−1. Call n = p−1
2 . Σ(T2n,2n+1) now bounds a
4–manifold with intersection form presented by ( −n − 1 n
n −n − 1 ), and therefore the

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 15

linking form represents n+1
p as a square. The inverse of n+1 modulo p is 2, so it also
represents 2
p as a square. As above, restricting to G we reach a contradiction. □

The next proposition implies Theorem 1.2 when n is a prime.

Proposition 5.6. For each odd prime p there are inﬁnitely many positive integers
k such that the knot T2p,2kp±1 does not bound a locally-ﬂat M¨obius band in B4.

The statement means that for each choice of a sign there are inﬁnitely many
values of k such that the statement is true; i.e. we do not claim that there are
values of k such that the statements holds with both signs. We prefer to leave the
ambiguity in order to keep the notation lighter.

Proof. Let q be a prime number with q ≡ 1 (mod 4) and such that p is not a
square residue modulo q. We claim that we can always construct such a number.
Indeed, by quadratic reciprocity, ( p
q ) = ( q
p ); so it suﬃces to choose q such that
( q
p ) = −1. There are inﬁnitely many such primes: it suﬃces to pick an integer r
such that ( r
p ) = −1 and look at the arithmetic progression r + sp, which contains
inﬁnitely many primes by Dirichlet’s theorem. Since q ≡ 1 (mod 4), ( −1
q ) = 1, so
that ( −p
q ) = −1, too. In particular, for any positive integer r, neither −p nor p is
a square modulo qr.
Let h0 be any positive integer such that 2h0p ± 1 ≡ q (mod q2). Let us look at
the arithmetic progression 2h0p±1+hpq2, with h > 0. Since gcd(2h0p±1, pq2) = q,
we can re-write 2h0p ± 1 + hpq2 = q(a + hpq),
where gcd(a, pq) = 1; in particular, by Dirichlet’s theorem there are inﬁnitely many
primes in the arithmetic progression a + hpq. Choose h such that r = a + hpq is a
prime, and let k = h0 + q2h. In particular, we have 2kp ± 1 = qr.
We claim that T2p,2kp±1 does not bound a locally-ﬂat M¨obius band, and more
precisely that T2p,2kp±1 violates the Murakami–Yasuhara criterion.
Since qr = 2kp ± 1, qr = det T2p,2kp±1; since q and r are distinct primes,
H1(Σ(2, 2p, qr)) ∼= Z/qrZ. By tweaking the proof of Lemma 5.3, we see that
Σ(2, 2p, qr) has a surgery presentation for which the linking matrix is given by
the following tridiagonal 2k × 2k matrix:

Q =
 











 −2 1
1 −2
 . . . −2 1 0 0
1 ±p − 1 ±p 0
0 ±p ±p − 1 1
0 0 1 −2
 . . . −2 1
1 −2
 











 .

Since H1(Σ(2, 2p, qr)) is cyclic, it suﬃces to compute one non-trivial square in the
linking form λ; by an explicit inductive computation, the ﬁrst entry of the matrix
−Q
−1, which is the matrix that represents the linking form, is qr∓p
qr .
Since ( p
q ) = ( −p
q ) = −1 by choice, and since λ represents ∓ p
qr as a square by
the previous computation, λ does not represent 1
qr nor − 1
qr as a square. Thus, by
Proposition 5.4, T2p,2kp±1 is not the boundary of a locally-ﬂat M¨obius band. □

We want to highlight the limitations of the techniques we used above. There
are shortcomings to applying Proposition 5.4 even when |det K| =: q is a prime:
if −1 is not a square residue modulo q (equivalently, if q ≡ 3 (mod 4)), then for

16 PETER FELLER AND MARCO GOLLA

algebraic reasons either 1
q or − 1
q is always represented by a square. So, for instance,
we cannot directly conclude anything about the existence of a M¨obius band in B4

whose boundary is T6,7. However, we can ﬁnd an alternative to Proposition 1.4.

Proposition 5.7. Let n ≡ 3 (mod 4) be a positive integer such that 2n + 1 is
square-free and n + 1 is not a square. Then T2n,2n+1 does not bound a smooth
M¨obius band in B4. In particular, T14,15 and T22,23 do not bound smooth M¨obius
bands in B4.

Note that there are inﬁnitely many integers satisfying the three conditions in
the statement: for instance, n + 1 is never a square if n ≡ 7 (mod 16), and by
Dirichlet’s theorem on primes in arithmetic progressions there are inﬁnitely many
primes (and in particular square-free integers) congruent to 15 modulo 32.

Proof. We know from Lemma 5.3 that Y := Σ(2, 2n, 2n + 1) = Σ(T2n,2n+1) bounds
a spin negative deﬁnite 4–manifold W with second Betti number 2. By successively
blowing up W , we obtain the canonical negative plumbing P whose boundary is
Y , according to Neumann [Neu81]; call Γ the associated weighted graph (which
is a three-legged star-shaped graph, in this case). Ozsv´ath and Szab´o computed
correction terms of Y starting from the plumbing graph Γ [OSz03b] as follows.
Let L be the intersection lattice of P , and ﬁx a coset in Char(L)/2L (recall that
the set Char(L) of characteristic covectors of L is a 2L–torsor). Since cosets in
Char(L)/2L are in bijection with spinc structures on Y , we will denote the coset
by the spin
c structure t it corresponds to. Then:

(3) d(Y, t) = d(L, t) := max
ξ∈t ξ2 + rank L
4 .

We make an easy observation here: if L = ⟨−1⟩ ⊕ L
′, then the inclusion L
′ →
L induces a bijection j : Char(L)/2L → Char(L′)/2L
′, and it is easy to verify
that d(L, t) = d(L
′, j(t)). This implies that, since P is a blow-up of W and the
intersection from changes by taking the direct sum with ⟨−1⟩ under blow-ups, we
can do the maximisation on the intersection lattice of W (which has rank 2), rather
than on the intersection lattice of P .
To unravel (3), let Q be the 2 × 2 matrix ( −n − 1 n
n −n − 1 ). Since the entries on
the diagonal are both even, characteristic covectors are of the form 2Q
−1ηT , where
η = (η1, η2) is an integer vector. The maximisation then reads:

(4) d(Y, t) = max
ξ∈t ξ2 + rank L
4 = max
2Q−1ηT ∈t η Q
−1ηT + 1
2 = 1
2 −(η1 +η2)
2 − η2
1 + η2
2
2n + 1 .

Note that the quantity on the right-hand side is negative as soon as η1 + η2 ̸= 0.
Suppose that T2n,2n+1 bounds a (locally-ﬂat) M¨obius band M in B4. Then Y
bounds a 4–manifold Z with b2(Z) = 1, namely the double cover of B4 branched
over M . If M is smoothly embedded, then Z is a smooth 4–manifold.
Since 2n + 1 is a square-free, the intersection form of Z is ⟨±(2n + 1)⟩. Suppose
that Z were positive deﬁnite. Then we could glue Z and −W along their boundary
to get a closed, positive deﬁnite 4–manifold X with b2(X) = 3. Its intersection
form, since it is unimodular and negative deﬁnite, has to be diagonal. But this
implies that the self-intersection of the generator of H2(Z), which is 2n + 1, is a
sum of three squares. But this contradicts the fact that 2n + 1 ≡ 7 (mod 8).
So Z is negative deﬁnite, with intersection form ⟨−2n − 1⟩. However, Ozsv´ath
and Szab´o [OSz03a, Theorem 9.6] proved, under these assumptions, for each spinc

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 17

structure s on Z which restricts to t on Y , that

(5) c1(s)
2 + 1
4 ≤ d(Y, t),

and that the two sides are congruent modulo 2.
Let us focus on the case where ⟨c1(s), H2(Z)⟩ = Z (this is possible since the
intersection form of Z is odd, and therefore there is such a spinc structure; in fact
there are exactly two, which are conjugate). Then c1(s)
2 = − 1
2n+1 , and therefore

c1(s)
2+1
4 = n
4n+2 > 0.
It follows from (5) that d(Y, t) > 0, and therefore, from (4), that t corresponds
to Q
−1ηT with η1 + η2 = 0. In particular, d(Y, t) = 1
2 − 2x2
2n+1 for the integer x = η1.
We now use the congruence condition in (5). We have (the reduction modulo 1
2
of) the congruence condition (modulo 2) telling us that −1 ≡ −8x2 (mod 2n + 1).
However, if n+1
4 is not a square, then the smallest positive integer solution x of this

congruence has x > √ n+1
4 , and therefore

d(Y, t) = 1
2 − 2x2

2n + 1 < 1
2 − n + 1
4n + 2 = n
4n + 2 = c1(s)2 + 1
4 ,

which contradicts (5). □

Recall that 2–bridge links are links L ⊂ R3 ⊂ S3 such that the restriction of
the z–function is Morse with two minima and two maxima. The double cover of
S3 branched over a two 2–bridge link is a lens space, and two 2–bridge links are
isotopic if and only if their branched covers are homeomorphic. We refer to Kp/q
as the unique 2–bridge link whose double cover is the lens space L(p, q); note that
Kp/q is a knot if and only if p is odd, and that p = |det Kp/q|.

Proposition 5.8. Let p a positive integer. If p ≡ 5 (mod 8), the 2–bridge knot
Kp/(p−2) does not bound a locally-ﬂat M¨obius band in B4. If p ≡ 7 (mod 8) and
p > 7, the 2–bridge knot Kp/(p−2) does not bound a smooth M¨obius band in B4.

Proof. Suppose that Kp/(p−2) bounds a locally-ﬂat M¨obius band M in B4; then
the double cover of B4 branched over M is a 4–manifold Z with b2(Z) = 1 whose
boundary is a lens space, namely Σ(Kp/(p−2)) = L(p, p − 2). The intersection form
on Z gives a presentation of the restriction of the linking form on L(p, p − 2) to a
subgroup G, where G is as in Proposition 5.4; see e.g. [GL11, Lemma E.1]. More
precisely, if the intersection form of Z is isomorphic to ⟨±r⟩ for some positive integer
r, then the linking form of L(p, p − 2) restricted to G is isomorphic to ⟨∓ 1
r ⟩. Recall
that the linking form λ of L(p, p − 2) is isomorphic to ⟨ p−2
p ⟩ = ⟨ −2
p ⟩. Thus, λ|G
presents −2
r as a square, in addition to presenting 1
r or −1
r as a square.
Note that, since all odd squares are congruent to 1 modulo 8, r ≡ p (mod 8). If
p ≡ 7 (mod 8), r is not a square and it is either divisible by a prime congruent to
7 modulo 8, or by a prime congruent 5 modulo 8. If p ≡ 5 (mod 8), again r is not
a square and it is either divisible by a prime congruent to 5 modulo 8 or by both a
prime congruent 3 modulo 8 and 7 modulo 8.
We can exclude the case where r = |G| is divisible by a prime congruent to 5
modulo 8 or by both a prime congruent 3 modulo 8 and one congruent 7 modulo
8 since otherwise, arguing as in the proof of Proposition 1.4, we ﬁnd that λ|G does
not present −2
r as square, which yields a contradiction. In particular, this concludes
the proof if p ≡ 5 (mod 8).
It remains to treat the case where p ≡ 7 (mod 8) with p > 7 and r = |G| is
divisible by a prime s ≡ 7 (mod 8) but not by a prime congruent to 3 modulo 8.

18 PETER FELLER AND MARCO GOLLA

Since s ≡ 7 (mod 8), Lemma 5.5(3) implies that the reduction of λ|G modulo s
cannot present 1
s as a square, as this would contradict the reduction of λ|G modulo
s representing − 2
s as a square. Hence λ|G cannot present 1
r as a square. Therefore,
the linking form restricted to G is isomorphic to ⟨− 1
r ⟩ (and not ⟨ 1
r ⟩). It follows
that Z is positive deﬁnite, i.e. that its intersection form is isomorphic to ⟨r⟩.
At this point, we further assume that M is smooth, hence Z is smooth. Gluing
−Z and the negative deﬁnite plumbing P whose boundary is L(p, p − 2), we obtain
a smooth, negative deﬁnite 4–manifold X. In particular, the intersection form
of P embeds with co-rank 1 in a diagonal lattice, by Donaldson’s diagonalisation
theorem [Don83].
Recall that the negative deﬁnite plumbing of L(p, p − 2) is determined by the
negative continued fraction expansion of p/(p − 2) = [2, . . . , 2, 3], where the string
of 2s has length N − 2 = (p − 3)/2. However, if p > 7 the string of 2s has a unique
embedding, namely (in some basis e1, . . . , eN of Z
N ) e1 − e2, . . . , eN −2 − eN −1.
Since N ≥ 2 by assumption, there is no vector in Z
N of self-intersection −3 that
intersects the chain (algebraically) once in the last vector, which contradicts our
assumption. □

References

[Bat14] Joshua Batson. Nonorientable slice genus can be arbitrarily large. Math. Res. Lett.,
21(3):423–436, 2014.
[BFLL18] S. Baader, P. Feller, L. Lewark, and L. Liechti. On the topological 4-genus of torus knots.
Trans. Amer. Math. Soc., 370(4):2639–2656, 2018. ArXiv:1509.07634 [math.GT].
[Don83] Simon K. Donaldson. An application of gauge theory to four-dimensional topology. J.
Diﬀerential Geom., 18(2):279–315, 1983.
[FL18] Peter Feller and Lukas Lewark. On classical upper bounds for slice genera. Selecta
Math. (N.S.), 24(5):4885–4916, 2018. ArXiv:1611.02679 [math.GT].
[FM16] Peter Feller and Duncan McCoy. On 2-bridge knots with diﬀering smooth and topolog-
ical slice genera. Proc. Amer. Math. Soc., 144(12):5435–5442, 2016. ArXiv:1508.01431
[math.GT].
[FQ90] Michael H. Freedman and Frank Quinn. Topology of 4-manifolds, volume 39 of Prince-
ton Mathematical Series. Princeton University Press, Princeton, NJ, 1990.
[Fre82] Michael H. Freedman. The topology of four-dimensional manifolds. J. Diﬀerential
Geom., 17(3):357–453, 1982.
[GL11] Patrick M. Gilmer and Charles Livingston. The nonorientable 4-genus of knots. J. Lond.
Math. Soc. (2), 84(3):559–577, 2011.
[GL20a] Joshua E. Greene and Andrew Lobb. Cyclic quadrilaterals and smooth jordan curves.
ArXiv:2011.05216, 2020.
[GL20b] Joshua E. Greene and Andrew Lobb. The rectangular peg problem. ArXiv:2005.09193,
2020.
[GM18] Marco Golla and Marco Marengon. Correction terms and the nonorientable slice genus.
Mich. Math. J., 67(1):59–82, 2018.
[Hug18] Cole Hugelmeyer. Every smooth Jordan curve has an inscribed rectangle with aspect
ratio equal to √3. Arxiv e-print, 2018. ArXiv:1806.07417 [math.GT].
[HW08] G. H. Hardy and E. M. Wright. An introduction to the theory of numbers. Oxford
University Press, Oxford, sixth edition, 2008. Revised by D. R. Heath-Brown and J. H.
Silverman, With a foreword by Andrew Wiles.
[Lob19] Andrew Lobb. A counterexample to Batson’s conjecture. Math. Res. Lett., 26(6):1789,
2019.
[Mat11] Benjamin Matschke. Equivariant topology methods in discrete geometry. PhD thesis,
Freie Universit¨at Berlin, 2011.
[Mat14] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc.,
61(4):346–352, 2014.
[Mey81] Mark D. Meyerson. Balancing acts. Topology Proc., 6(1):59–75 (1982), 1981.
[MY00] Hitoshi Murakami and Akira Yasuhara. Four-genus and four-dimensional clasp number
of a knot. Proc. Amer. Math. Soc., 128(12):3693–3699, 2000.

NON-ORIENTABLE SLICE SURFACES AND INSCRIBED RECTANGLES 19

[Neu81] Walter D. Neumann. A calculus for plumbing applied to the topology of complex surface
singularities and degenerating complex curves. Trans. Amer. Math. Soc., 268(2):299–
344, 1981.
[OSSz17] Peter S. Ozsv´ath, Andr´as I. Stipsicz, and Zolt´an Szab´o. Unoriented knot Floer ho-
mology and the unoriented four-ball genus. Int. Math. Res. Not., 2017(17):5137–5181,
2017.
[OSz03a] Peter S. Ozsv´ath and Zolt´an Szab´o. Absolutely graded Floer homologies and intersec-
tion forms for four-manifolds with boundary. Adv. Math., 173(2):179–261, 2003.
[OSz03b] Peter S. Ozsv´ath and Zolt´an Szab´o. On the Floer homology of plumbed three-manifolds.
Geom. Topol., 7:185–224, 2003.
[Rol76] Dale Rolfsen. Knots and links. AMS Chelsea Publishing, 1976.
[Rud84] Lee Rudolph. Some topologically locally-ﬂat surfaces in the complex projective plane.
Comment. Math. Helv., 59(4):592–599, 1984.
[Sch18] Richard E. Schwartz. A trichotomy for rectangles inscribed in Jordan loops. to appear
in Geom. Dedicata, 2018.
[Tao17] Terence Tao. An integration approach to the Toeplitz square peg problem. Forum Math.
Sigma, 5:e30, 63, 2017.

Email address: peter.feller@math.ethz.ch

ETH Zurich, Department of Mathematics, Zurich, Switzerland

Email address: marco.golla@univ-nantes.fr

CNRS, Laboratoire de Math´ematiques Jean Leray, Nantes, France
