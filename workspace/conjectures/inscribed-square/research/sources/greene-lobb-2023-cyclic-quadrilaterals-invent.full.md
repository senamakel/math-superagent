<!-- source: https://arxiv.org/pdf/2011.05216 | converted from PDF -->

CYCLIC QUADRILATERALS AND SMOOTH JORDAN CURVES

JOSHUA EVAN GREENE AND ANDREW LOBB

Abstract. For every smooth Jordan curve γ and cyclic quadrilateral Q in the Euclidean plane,
we show that there exists an orientation-preserving similarity taking the vertices of Q to γ. The
proof relies on the theorem of Polterovich and Viterbo that an embedded Lagrangian torus in C2 has
minimum Maslov number 2.

A quadrilateral Q inscribes in a smooth Jordan curve γ in the Euclidean plane if there exists an
orientation-preserving similarity of the plane taking the vertices of Q to γ; it is cyclic if it inscribes in a
circle. The result of this paper is the solution of the cyclic quadrilateral peg problem [3, Conjecture 9]:

Theorem. Every cyclic quadrilateral inscribes in every smooth Jordan curve in the Euclidean plane.

The result is best possible, by considering the case in which the smooth Jordan curve is itself a circle.
Moreover, some regularity hypothesis on the Jordan curve is necessary in order for the Theorem to
hold, as the only cyclic quadrilaterals that inscribe in all triangles are the isosceles trapezoids [6, § 3.6].

Proof. For a ﬁxed cyclic quadrilateral Q and smooth Jordan curve γ, we construct a pair of Lagrangian
tori T1 and T2 in standard symplectic C2. They intersect cleanly along γ × {0} and in a disjoint set of
points P which parametrize the inscriptions of Q in γ. By smoothing the intersection along γ × {0},
we obtain an immersed Lagrangian torus T whose set of self-intersections is P . As we show, T has
minimum Maslov number 4. On the other hand, a theorem independently due to Polterovich and
Viterbo asserts that an embedded Lagrangian torus in C2 has minimum Maslov number 2 [7, 10].
Therefore P is non-empty, so Q inscribes in γ. □

The strategy of proof of the Theorem resembles that of our earlier result, which treated the case
in which Q is a rectangle [2]. In that case, we additionally arranged that T is invariant under a
symplectic involution τ of C2. Passing to the quotient by τ , we obtained an immersed Lagrangian
Klein bottle K = T /τ in C2 whose self-intersections P/τ parametrize inscriptions of Q in γ up to
rotation by π. A theorem independently due to Shevchishin and Nemirovski asserts that there is no
embedded Lagrangian Klein bottle in C2 [5, 9], thereby ensuring that P is non-empty, so Q inscribes in
γ. In the more general case of a cyclic quadrilateral, T does not admit any apparent symmetry, which
impedes reusing the same approach. Our revised approach produces a stronger result and somewhat
more directly.

Cyclic quadrilaterals. We begin by characterizing the set of cyclic quadrilaterals. Let Q denote
a convex quadrilateral in the plane whose vertices are labeled ABCD in counterclockwise order. Its
diagonals AC and BD intersect in a point X. Euclid’s chord theorem asserts that Q is cyclic if and
only if |AX| · |CX| = |BX| · |DX| [1, Theorem III.35].1

JEG was supported on NSF Award DMS-2005619.
1Euclid proves the forward direction, which can be used to prove the reverse.

1arXiv:2011.05216v1  [math.GT]  10 Nov 2020
2 JOSHUA EVAN GREENE AND ANDREW LOBB

By a cyclic permutation of the vertex labels, we may assume that |AX| ≤ |CX| and |BX| ≤ |DX|.
We thereby obtain real values s = |AX|/|AC| and t = |BX|/|BD| in (0, 1/2] and an angle φ = ∠AXB
in (0, π). The triple of values (s, t, φ) uniquely determines the oriented similarity class of Q, unless one
of s and t equals 1/2, in which case (s, t, φ) and (t, s, π − φ) determine the same oriented similarity
class.

We reformulate the preceding description for our present purposes. Identify the Euclidean plane
with the complex numbers C. Deﬁne C-linear automorphisms of C2 by the matrices

Fr = ( r 1 − r√r(1 − r) −√
r(1 − r)

) and Rφ = (
1 0
0 eiφ
)

for values r ∈ (0, 1/2] and φ ∈ (0, π).

Lemma 1. Points A, B, C, D ∈ C correspond as above to vertices of a cyclic quadrilateral with param-
eters (s, t, φ) if and only if

(1) Rφ ◦ Fs(A, C) = Ft(B, D) and A ̸= C (equivalently B ̸= D).

Proof. Equality in the ﬁrst coordinate of (1) is equivalent to the assertion that segments AC and BD
intersect at a point X so that |AX| = s · |AC| and |BX| = t · |BD|. Equality in the second coordinate
given the ﬁrst then ensures that ∠AXB = φ and that |AX| · |CX| = s(1 − s) · |AC|2 = t(1 − t) · |BD|
2 =
|BX| · |DX|. Insisting that A ̸= C or B ̸= D ensures that Q does not degenerate to a point. □

Two embedded Lagrangian tori. Suppose that Q is a cyclic quadrilateral with parameters (s, t, φ)
as above and that γ is a smooth Jordan curve in C. Note that γ × γ is a smoothly embedded torus in
C2. Deﬁne tori T1 = Rφ ◦ Fs(γ × γ) and T2 = Ft(γ × γ).

Note that both Rφ ◦ Fs and Ft map the point (z, z) to (z, 0) for all z ∈ C. From Lemma 1 we see that
the set of inscriptions of Q in γ is parametrized by the set of points

P = T1 ∩ T2 − γ × {0}.

Let ω = dz ∧ dz + dw ∧ dw denote the standard symplectic form on C2, up to scale.

Lemma 2. The tori T1 and T2 are Lagrangian with respect to ω and intersect cleanly along γ × {0}:

T(p,0)T1 ∩ T(p,0)T2 = T(p,0)(γ × {0}), for all p ∈ γ.

Proof. A direct calculation shows that

ωr := F ∗
r ω = r · dz ∧ dz + (1 − r) · dw ∧ dw

for r ∈ (0, 1/2]. Note that γ × γ is Lagrangian with respect to ωr and R∗
φ ω = ω. It follows that T1
and T2 are Lagrangian with respect to ω.

If p ∈ γ is a point on the Jordan curve, then Tpγ ⊂ C is a 1-dimensional real subspace. A direct
calculation shows that

T(p,0)T1 = Tpγ × {0} ⊕ {0} × eiφTpγ and T(p,0)T2 = Tpγ × {0} ⊕ {0} × Tpγ,

so T(p,0)T1 ∩ T(p,0)T2 = Tpγ × {0} = T(p,0)(γ × {0}),

and the intersection along γ × {0} is clean, as required. □

CYCLIC QUADRILATERALS AND SMOOTH JORDAN CURVES 3

x2

y2

T1

T2

T

Figure 1. Cross-section of smoothing in the x1 = constant, y1 = 0 plane.

A surgered immersed Lagrangian torus. Because T1 and T2 intersect cleanly along γ × {0}, a
version of the Weinstein neighborhood theorem due to Po´zniak [8, Proposition 3.4.1] implies that we
can select coordinates (x1, y1, x2, y2) in a neighborhood N ≈ (R/Z) × R3 of γ × {0} such that

• ω = dx1 ∧ dy1 + dx2 ∧ dy2,
• T1 ∩ N = {y1 = y2 = 0}, and
• T2 ∩ N = {y1 = x2 = 0}.

We smooth the intersection of T1 and T2 in N as suggested by Figure 1 and let T denote the result. The
tangent plane to T at a point in N is spanned by ∂/∂x1 and a vector of the form a · ∂/∂x2 + b · ∂/∂y2,
which are ω-orthogonal. Thus, T is an immersed Lagrangian torus in (C2, ω), and its set of self-
intersections equals P , which parametrizes the set of inscriptions of Q in γ.

The minimum Maslov number. Equip Cn with a product symplectic form ω0 = ∑n
i=1 ci · dzi ∧ dzi.
An immersed Lagrangian submanifold i : L → (Cn, ω0) has a Maslov class µ ∈ H 1(L; Z), given as
follows (cf. [4, pp.117-118]). The tangent planes to i(L) along the image of an embedded loop α ⊂ L
determine a loop α♯ in L(ω0), the Grassmannian of Lagrangian n-planes in (Cn, ω0). The Maslov index
of α is the value µ([α]) := [α♯] ∈ H1(L(ω0); Z) ≈ Z, and the minimum Maslov number of L is the
non-negative integer m(L) such that µ(H1(L; Z)) = m(L) · Z.

Proposition. The minimum Maslov number of T is 4.

Proof. Orienting γ ⊂ C counterclockwise, its Maslov index equals 2 with respect to c · dz ∧ dz. Hence
γ × {pt.} and {pt.} × γ both have Maslov index 2 in γ × γ with respect to the product form ωr. Since
their homology classes generate H1(γ ×γ; Z), we obtain m(γ ×γ) = 2. The diagonal loop {(z, z) : z ∈ γ}
is homologous to their sum, so it has Maslov index 4 in γ × γ with respect to ωr. Applying Rφ ◦ Fs
and Ft, we deduce that γ × {0} has Maslov index 4 in both T1 and T2 with respect to ω and that
m(T1) = m(T2) = 2. Let δ denote a push-oﬀ of γ × {0} in T1 away from the site of surgery. A
neighborhood of δ survives the surgery, so the Maslov index of [δ] in T is 4 with respect to ω.

Next, select oriented loops λ1 ⊂ T1, λ2 ⊂ T2, and λ ⊂ T such that λ1 ∪ λ2 and λ coincide outside
the neighborhood N above and meet it in a single slice x1 = constant, y1 = 0, as displayed in Figure
1. The tangent planes to T ∪ T1 ∪ T2 along the diﬀerence 1-cycle λ − λ1 − λ2 describe a nullhomotopic
loop in L(ω). Consequently, [λ
♯] = [λ♯
1] + [λ
♯
2] ∈ H1(L(ω); Z) ≈ Z. The class [λj] completes to a basis
of H1(Tj; Z) with [γ × {0}] for j = 1, 2. Since m(Tj) = 2 and [γ × {0}] has Maslov index 4 in Tj,
j = 1, 2, it follows that [λj] has Maslov index 2 (mod 4), j = 1, 2. Therefore, the Maslov index of [λ]
in T is a multiple of 4.

Since [δ] and [λ] form a basis for H1(T ; Z), it follows that m(T ) = 4. □

4 JOSHUA EVAN GREENE AND ANDREW LOBB

Acknowledgements. We thank Mohammed Abouzaid, Lev Buhovsky, Joe Johns, and Leonid Polterovich
for useful discussions and Lenny Ng for drawing our attention to a key result from [1].

References

1. Euclid, The elements, c. 300 B.C.E.
2. Joshua Evan Greene and Andrew Lobb, The rectangular peg problem, arXiv:2005.09193 (2020).
3. Benjamin Matschke, A survey on the square peg problem, Notices Amer. Math. Soc. 61 (2014), no. 4, 346–352.
4. Dusa McDuﬀ and Dietmar Salamon, Introduction to symplectic topology, third ed., Oxford Graduate Texts in Math-
ematics, Oxford University Press, Oxford, 2017.
5. S. Nemirovski, The homology class of a Lagrangian Klein bottle, Izv. Ross. Akad. Nauk Ser. Mat. 73 (2009), no. 4,
37–48.
6. Igor Pak, The discrete square peg problem, arXiv:0804.0657 (2008).
7. L. V. Polterovich, The Maslov class of the Lagrange surfaces and Gromov’s pseudo-holomorphic curves, Trans.
Amer. Math. Soc. 325 (1991), no. 1, 241–248.
8. Marcin Po´zniak, Floer homology, Novikov rings and clean intersections, Ph.D. thesis, University of Warwick, 1994.
9. V. V. Shevchishin, Lagrangian embeddings of the Klein bottle and the combinatorial properties of mapping class
groups, Izv. Ross. Akad. Nauk Ser. Mat. 73 (2009), no. 4, 153–224.
10. C. Viterbo, A new obstruction to embedding Lagrangian tori, Invent. Math. 100 (1990), no. 2, 301–320.

Department of Mathematics, Boston College, USA

Email address: joshua.greene@bc.edu

URL: https://sites.google.com/bc.edu/joshua-e-greene

Mathematical Sciences, Durham University, UK

Email address: andrew.lobb@durham.ac.uk

URL: http://www.maths.dur.ac.uk/users/andrew.lobb/
