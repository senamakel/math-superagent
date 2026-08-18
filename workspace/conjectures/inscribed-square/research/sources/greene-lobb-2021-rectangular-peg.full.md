<!-- source: https://arxiv.org/pdf/2005.09193 | converted from PDF -->

arXiv:2005.09193v1  [math.GT]  19 May 2020
THE RECTANGULAR PEG PROBLEM

JOSHUA EVAN GREENE AND ANDREW LOBB

Abstract. For every smooth Jordan curve γ and rectangle R in the Euclidean plane, we show that
there exists a rectangle similar to R whose vertices lie on γ. The proof relies on Shevchishin’s theorem
that the Klein bottle does not admit a smooth Lagrangian embedding in C2.

The result of this paper is the solution of the Rectangular Peg Problem for smooth Jordan curves:

Theorem. For every smooth Jordan curve γ and rectangle R in the Euclidean plane, there exists a
rectangle similar to R whose vertices lie on γ.

Proof. We consider the Euclidean plane C with complex coordinate z = x + i · y and take another copy
with complex coordinate w = r · eiθ. In these coordinates, the standard symplectic structure on C2 is
given by ω = dx ∧ dy + r · dr ∧ dθ. Consider the maps l, g : C2 → C2 deﬁned in a mix of complex and
polar coordinates by

l : (z, w) ↦→ ( z + w
2 , z − w
2
 ) and g : (z, r, θ) ↦→ (z, r/√
2, 2θ).

The map l is a diﬀeomorphism and satisﬁes l∗(ω) = ω/2. Away from C × {0}, the map g is smooth and
satisﬁes g∗(ω) = ω. The Jordan curve γ is Lagrangian in C, so both the product γ × γ and its image
L = l(γ × γ) are smooth, Lagrangian tori in C2, noting that Lagrangians with respect to ω coincide
with those with respect to ω/2. For any φ ∈ R, the map

Rφ : C2 → C2 : (z, r, θ) ↦→ (z, r, θ + φ)

is a symplectomorphism. Fixing a choice 0 < φ ≤ π/2, Lφ = Rφ(L) is another smooth, Lagrangian
torus. By construction, g ◦ l(z, w) = g ◦ l(z′, w′) if and only if {z, w} = {z′, w′}. It follows that
M = g(L) and Mφ = g(Lφ) are both homeomorphic to a M¨obius band Sym
2(γ) and are smooth and
Lagrangian away from C × {0}.

The map Rπ preserves each of L and Lφ, and it ﬁxes γ × {0}, where these two tori intersect cleanly:
Tp(γ × {0}) = TpL ∩ TpLφ at each point p ∈ γ × {0}. We perform a Lagrangian smoothing of L ∪ Lφ
along γ × {0} according to Proposition 1.1 below. The result is a smoothly immersed Lagrangian torus
in C × C that coincides with L ∪ Lφ away from a neighborhood of γ × {0}, is disjoint from C × {0}, and
on which Rπ acts as a ﬁxed-point free involution. Its image under g is therefore a smoothly immersed,
Lagrangian Klein bottle K which coincides with M ∪ Mφ outside of a neighborhood of γ × {0} and
is embedded within this neighborhood. Shevchishin has shown that there is no smoothly embedded,
Lagrangian Klein bottle in C2 [16]. Therefore, M and Mφ must intersect at a point away from γ × {0},
so L and Lφ do as well, say at the point (z, rei(θ+φ)). It follows that the four points z ± reiθ and
z ± rei(θ+φ) all lie on the Jordan curve γ. These points form the vertices of a rectangle whose diagonals
meet at an angle of φ. As φ ∈ (0, π/2] was arbitrary, the proof is complete. □

AL thanks the Okinawa Institute of Science and Technology for hosting him as Excellence Chair while this work was
completed. JEG was supported on NSF CAREER Award DMS-1455132 and a Simons Fellowship.

1

2 JOSHUA EVAN GREENE AND ANDREW LOBB

The proof establishes somewhat more:

Porism. For every smooth Jordan curve γ and smooth map φ : [0, ∞) → (0, π), there exists r > 0 such
that γ contains the vertices of a rectangle of diameter r whose diagonals meet at angle φ(r). □

We simply note that the map
 Sφ : C2 → C2 : (z, r, θ) ↦→ (z, r, θ + φ(2r))

is a symplectomorphism, so Lφ = Sφ(L) is a Lagrangian torus, invariant under Rπ and meeting L
cleanly along γ × {0}. The main result covers the case of a constant function φ.

1. Lagrangian smoothing.

We now turn to the smoothing used in the proof of the theorem:

Proposition 1.1. One may remove a neighborhood of γ ×{0} in L∪Lφ and replace it with two disjoint
Lagrangian annuli. The surgery may be performed so as to result in a smoothly immersed Lagrangian
torus T such that Rπ(T ) = T and T is disjoint from C × {0}.

Here Lφ may denote either Rφ(L) or Sφ(L) from the previous section. A posteriori we obtain a
Lagrangian smoothing of M ∪ Mφ nearby the common boundary ∂M = ∂Mφ = γ × {0} ⊂ C × {0},
but we found it more direct to work rather with L ∪ Lφ, due to the non-smoothness of g at C × {0}.

Proposition 1.1 will not come as a surprise to symplectic geometers, although we could not locate the
desired result in the literature. It can be phrased as a consequence of a simple case of the equivariant
Darboux-Weinstein theorem in the presence of a compatible clean intersection of Lagrangians. We
shall prove the proposition by establishing a linear local model for L ∪ Lφ near γ × {0}. The local
model is the 4-manifold X = S1 × (−ǫ, ǫ) × R × R with coordinates (θ, s, t1, t2), symplectic form
ωX = dθ ∧ dt1 + ds ∧ dt2, and symplectic involution

I : X → X : (θ, s, t1, t2) ↦→ (θ, −s, t1, −t2).

It contains Lagrangian submanifolds L0 = S1 × (−ǫ, ǫ) × {0} × {0} and L1 = S1 × {0} × {0} × R, which
intersect each other cleanly in Γ = S1 × {0} × {0} × {0}.

Proposition 1.2. There exists a symplectomorphism

Ψ : N (Γ) → N (γ)

from a neighborhood of Γ in X to a neighborhood of γ × {0} in C2 such that

(1) Ψ(Γ) = γ × {0},
(2) Ψ(L0 ∩ N (Γ)) = L ∩ N (γ),
(3) Rπ ◦ Ψ = Ψ ◦ I, and
(4) Ψ(L1 ∩ N (Γ)) = Lφ ∩ N (γ).

Proof of Proposition 1.1. Let A = {(s, t2) ∈ R2 : st2 = 0} denote the union of the usual axes in
Euclidean space. Under the map Ψ−1 of Proposition 1.2, the union of the Lagrangians L ∪ Lφ is
modelled near γ × {0} as S1 × A × {0}, where we have exchanged coordinates t1 and t2. We pick
a smoothing B of A ⊂ R2 near the origin whose components are exchanged by I (which acts as
rotation by π on this plane). Observe that S1 × B × {0} is Lagrangian with respect to ωX . Replacing
(L ∪ Lφ) ∩ N (γ) by Ψ((S1 × B × {0}) ∩ N (Γ)) gives the desired smoothing. □

THE RECTANGULAR PEG PROBLEM 3

The technical work of this section, then, is to derive Proposition 1.2. The next lemma is phrased
for our situation and is a case of the Equivariant Darboux-Weinstein Theorem [2, Theorem 3.2].

Lemma 1.3. Suppose that ω0 and ω1 are symplectic forms in a neighborhood of L0 ⊂ X for which L0
is Lagrangian and which satisfy I ∗(ωi) = ωi for i = 0, 1. Then there exist neighborhoods U0 and U1 of
Γ and a diﬀeomorphism σ : U0 → U1
such that σ commutes with I, σ∗ω1 = ω0, and σ restricts to the identity on L0 ∩ U0. □

Next we use Lemma 1.3 to obtain a local model for the Lagrangian L near γ × {0}. It establishes
Proposition 1.1 apart from the ﬁnal item.

Lemma 1.4. There exists a symplectomorphism

F : N (Γ) → N (γ)

from a neighborhood N (Γ) of Γ in X to a neighborhood N (γ) of γ × {0} in C2 such that

(1) F (Γ) = γ × {0},
(2) F (L0 ∩ N (Γ)) = L ∩ N (γ), and
(3) Rπ ◦ F = F ◦ I.

Proof. Parametrize the Jordan curve γ ⊂ C as γ(θ), where θ ∈ S1. Now, γ × {0} is a submanifold of
L, so using the restriction of the standard metric on C2 to L, the exponential map

(θ, s) ↦→ exp(γ(θ),0)(s)

identiﬁes a neighborhood S1 × (−ǫ, ǫ) of the normal bundle of γ × {0} inside L with a tubular neigh-
borhood of γ × {0} in L. Since the standard metric is invariant under Rπ, we have that Rπ preserves
geodesics in L. It follows that we have

(θ, −s) ↦→ Rπ(exp(γ(θ),0)(s)).

Next we take a smooth choice of orthonormal basis {v1
θ , v2
θ } for (T L)
⊥|(γ(θ),0) (the orthogonal comple-
ment to T L along γ) such that v1
θ ∈ T(γ(θ),0)C × {0}. Note that (Rπ)∗(v1
θ ) = v1
θ and (Rπ)∗(v2
θ ) = −v2
θ .

Decreasing ǫ and N (γ) if necessary, we have a diﬀeomorphism

F ′ : S1 × (−ǫ, ǫ) × (−ǫ, ǫ) × (−ǫ, ǫ) → N (γ) : (θ, s, t1, t2) ↦→ exp(γ(θ),0)(s) + t1v1
θ + t2v2
θ .

Since Rπ is a linear map, we have

F ′ : (θ, −s, t1, −t2) ↦→ Rπ(exp(γ(θ),0)(s) + t1v1
θ + t2v2
θ ).

Hence we observe that F ′ satisﬁes all the required properties except possibly being a symplec-
tomorphism. We now apply Lemma 1.3 to ωX and to F ′∗(ω). Composing F ′ with the resulting
diﬀeomorphism σ between neighborhoods of Γ gives the required map F . □

It only remains to take account of the second Lagrangian Lφ; we write L2 = F −1(Lφ).

Lemma 1.5. There exists a symplectomorphism

G : U → V

deﬁned on neighborhoods U and V of Γ such that

(1) G restricts to the identity on L0,
(2) G ◦ I = I ◦ G, and

4 JOSHUA EVAN GREENE AND ANDREW LOBB

(3) G(L2 ∩ U ) = L1 ∩ V .

Proof. Observe that L2 is a Lagrangian within a neighborhood of Γ that satisﬁes I(L2) = L2 and that
intersects L0 cleanly in Γ. Po´zniak argues that there exist neighborhoods U and V of Γ within which
L2 ∩ U is the graph of a function deﬁned over L1 [13, Proposition 3.4.1 and Lemma 3.4.2]. Based on
this feature he deﬁnes a map, which in our framework takes the form

G : U → V : (θ, s, t1, t2) ↦→ (θ, s′, t′
1, t2),

by the requirement that (θ, s − s′, t1 − t′
1, t2) ∈ L2.
Such a map automatically satisﬁes properties (1) and (3), and Po´zniak shows that G is a symplecto-
morphism (this follows from L2 being Lagrangian). To verify property (2) we directly compute

I ◦ G(θ, s, t1, t2) = I(θ, s′, t′
1, t2) = (θ, −s′, t′
1, −t2) = G(θ, −s, t1, −t2) = G ◦ I(θ, s, t1, t2),

where the third equality follows because

(θ, −(s − s′), t1 − t′
1, −t2) = I(θ, s − s′, t1 − t′
1, t2) ∈ I(L2) = L2. □

Proof of Proposition 1.2. Set Ψ = F ◦ (G
−1) with the maps F and G of Lemmas 1.4 and 1.5. □

2. Discussion.

In 1911, Toeplitz posed the Square Peg Problem, which asks whether every continuous Jordan curve
in the Euclidean plane inscribes (contains the vertices of) a square [18]. It remains open to this day. The
Rectangular Peg Problem (for smooth Jordan curves) grew out of it [10, Conjecture 8]. Our solution
ﬁts into a long line of attack on these problems which involves identifying the inscribed feature with
the (self-)intersection of an associated geometric-topological object. The arguments tend to be quite
short, once the appropriate outlook and auxiliary result is identiﬁed.

In 1913, Emch solved the Square Peg Problem for smooth convex curves [3]; and in 1929, Schnirelman
solved it for smooth Jordan curves [14]. In fact, both required weaker hypotheses than smoothness.
They laid the groundwork for later approaches, introducing the idea of conﬁguration spaces and argu-
ments involving homology and bordism.

In 1981, Vaughan gave a simple proof of the result that every continuous Jordan curve γ inscribes a
rectangle [11]. Vaughan’s argument was to deﬁne a continuous map v : Sym2(γ) → C × R≥0 by sending
an unordered pair of points on γ to the ordered pair consisting of their midpoint and the length of the
line segment they span. The points of self-intersection of v thus parametrize inscribed rectangles in γ.
By ﬁlling γ × {0} with a disk D ⊂ C× {0}, we extend v to a continuous map from RP2 to C× R≥0 ⊂ R3

with the same set of self-intersections as v. Such a map contains a point of self-intersection (in fact,
a triple point), which corresponds to an inscribed rectangle in γ. The fact that v contains so much
self-intersection indicates that a large family of inscribed rectangles should exist in γ, but extracting
more information is a challenge.

In 1991, Griﬃths claimed a solution of the smooth Rectangular Peg Problem based on elementary
intersection theory, in the spirit of Schnirelman’s work [5]. However, in 2008, Matschke identiﬁed an
irreparable error in its proof, casting doubt on the eﬃcacy of this approach [10]. Following the discovery
of this error, the status of the Rectangular Peg Problem reverted to the cases already reported.

In 2018, Hugelmeyer salvaged some new cases of the smooth Rectangular Peg Problem [6]. He did
so by resolving Vaughan’s map into a four-dimensional version that enables the detection of rectangles’
aspect angles (the angle between the two diagonals). Deﬁne a map hn : Sym
2(γ) → C × C by sending

THE RECTANGULAR PEG PROBLEM 5

each unordered pair of points on γ to their midpoint and the (2n)-th power of their diﬀerence. For
n ≥ 2, the points of self-intersection of hn parametrize inscribed rectangles in γ of aspect angle equal
to an integer multiple of π/n. Hugelmeyer showed how to identify im(hn) with the image of a surface
mapped into the 4-ball with boundary on a (2n, 2n − 1) torus knot in the 3-sphere. However, for n ≥ 3,
this knot does not bound a smoothly embedded M¨obius band in the 4-ball: this is a result of Batson
proven using Heegaard Floer homology [1]. Hence hn contains a point of self-intersection for n ≥ 3
when γ is smooth. In particular, taking n = 3 leads to the novel case of the smooth Rectangular Peg
Problem for a rectangle of aspect angle π/3.

In 2019, Hugelmeyer sharpened this approach and recovered 1/3 of the smooth Rectangular Peg
Problem [7]. More precisely, he showed that for any smooth Jordan curve γ, the set of values φ ∈ (0, π/2]
for which γ contains an inscribed rectangle of aspect angle φ has Lebesgue measure at least π/6. The
map h1 above is a smooth embedding when γ is a smooth Jordan curve, giving rise to a smooth M¨obius
band im(h1) = M ⊂ C×C. The inscribed rectangles in γ of aspect angle φ are parametrized by interior
points of intersection between M and R2φ(M ). Hugelmeyer argued that this intersection is non-empty
for ≥ 1/3 of the angles φ by ﬁrst introducing a novel ordering on a set of embedded M¨obius bands in
C × R≥0 × S1 based on how they link and then applying a result from additive combinatorics. In fact,
this ordering may be applied to recover his earlier result, as well as the case of a square.

The inspiration behind our solution was to recast the problem within the framework of symplectic
geometry, which oﬀers greater rigidity for controlling intersections. Following Hugelmeyer’s second
approach, we wished to endow C × C with a symplectic form with respect to which M is Lagrangian
and R2φ is a Hamiltonian symplectomorphism. Then an optimistic version of the Arnold-Givental
conjecture predicts that M and Mφ = R2φ(M ) should contain at least dim H∗(M ; Z/2Z) = 2 points
of intersection in their interiors. Ultimately, we were able to arrange the framework by adjusting the
map h1 into the form g ◦ l given in the proof of the theorem. We were able to circumvent proving the
required version of the Arnold-Givental conjecture by noting that M ∪ Mφ is a Lagrangian Klein bottle
away from the common boundary of M and Mφ. By smoothing it and appealing to Shevchishin’s
theorem, we obtained an intersection point that corresponds with the desired inscribed rectangle in γ
of aspect angle φ.

Enjoyable accounts of the history of these problems and their relatives appear in [8, 10, 12]. Addi-
tional notable progress appears in the work of Feller and Golla, Schwartz, and Tao [4, 15, 17].

Acknowledgements. We thank Peter Feller and Patrick Orson for stimulating discussions on a
subtropical island at the outset of this work. We thank Yasha Eliashberg, Joe Johns, and Leonid
Polterovich for reassurances about Lagrangian smoothing, and Leonid in particular for steering us to
the references [9, 13].
 References

1. J. Batson, Nonorientable slice genus can be arbitrarily large, Math. Res. Lett. 21 (2014), no. 3, 423–436.
2. Shubham Dwivedi, Jonathan Herman, Lisa C. Jeﬀrey, and Theo van den Hurk, Hamiltonian Group Actions and
Equivariant Cohomology, SpringerBriefs in Mathematics, Springer-Verlag, 2019.
3. Arnold Emch, Some properties of closed convex curves in a plane, Amer. J. Math. 35 (1913), no. 4, 407–412.
4. Peter Feller and Marco Golla, Non-orientable slice surfaces and inscribed rectangles, arxiv.org/2003.01590 (2020).
5. H. B. Griﬃths, The topology of square pegs in round holes, Proc. London Math. Soc. (3) 62 (1991), no. 3, 647–672.
6. Cole Hugelmeyer, Every smooth Jordan curve has an inscribed rectangle with aspect ratio equal to √3,
arxiv:1803.07417 (2018).
7. , Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios, arxiv:1911.07336
(2019).

6 JOSHUA EVAN GREENE AND ANDREW LOBB

8. Victor Klee and Stan Wagon, Old and new unsolved problems in plane geometry and number theory, The Dolciani
Mathematical Expositions, vol. 11, Mathematical Association of America, Washington, DC, 1991.
9. Cheng Yu Mak and Weiwei Wu, Dehn twist exact sequences through Lagrangian cobordism, Compos. Math. 154
(2018), 2485–2533.
10. Benjamin Matschke, A survey on the square peg problem, Notices Amer. Math. Soc. 61 (2014), no. 4, 346–352.
11. Mark D. Meyerson, Balancing acts, Topology Proc. 6 (1981), no. 1, 59–75 (1982).
12. Igor Pak, The discrete square peg problem, arxiv.org/0804.0657 (2008).
13. Marcin Po´zniak, Floer homology, Novikov rings and clean intersections, Ph.D. thesis, University of Warwick, 1994.
14. Lev Schnirleman, On some geometric properties of closed curves (in Russian), Usp. Mat. Nauk 10, 34–44.
15. Richard Schwartz, A trichotomy for rectangles inscribed in Jordan loops, Geom. Dedicata (2020).
16. V. V. Shevchishin, Lagrangian embeddings of the Klein bottle and the combinatorial properties of mapping class
groups, Izv. Ross. Akad. Nauk Ser. Mat. 73 (2009), no. 4, 153–224.
17. Terence Tao, An integration approach to the Toeplitz square peg problem, Forum Math. Sigma 5 (2017), no. e30.
18. Otto Toeplitz, Ueber einige Aufgaben der Analysis situs, Verhandlungen der Schweizerischen Naturforschenden
Gesellschaft (1911), no. 4, 197.

Department of Mathematics, Boston College, USA

E-mail address: joshua.greene@bc.edu

URL: https://sites.google.com/bc.edu/joshua-e-greene

Mathematical Sciences, Durham University, UK

E-mail address: andrew.lobb@durham.ac.uk

URL: http://www.maths.dur.ac.uk/users/andrew.lobb/
