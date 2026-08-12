> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/hesterberg-escaping-polygons-thesis.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://erikdemaine.org/theses/ahesterberg.pdf | converted from PDF -->

## What it claims

Closed quasigeodesics

A closed quasigeodesic on the surface of a polyhedron is a loop which can everywhere locally be
unfolded to a straight line: thus, it’s straight on faces, uniquely determined on edges, and has as
much ﬂexibility at a vertex as that vertex’s curvature. On any polyhedron, at least three closed
quasigeodesics are known to exist, by a nonconstructive topological proof. We present an algorithm
to ﬁnd one on any convex polyhedron in time O(n2ε−2Lℓ−1), where ε is the minimum curvature of
a vertex, L is the length of the longest side, and ℓ is the smallest distance within a face between a
vertex and an edge not containing it.

Escaping from polygons

You move continuously at speed 1 in the interior of a polygon P , trying to reach the boundary.
A zombie moves continuously at speed r outside P , trying to be at the boundary when you reach
it. For what r can you escape and for what r can the zombie catch you? We give exact results
for some P . For general P , we give a simple approximation to within a factor of roughly 9.2504.
We also give a pseudopolynomial-time…

Conﬂi…

## Statements it makes

Lemma 1.2.1. If R1 = R(X, ϕ1, ∞) and R2 = R(X, ϕ2, ∞) are two geodesic rays from a common
starting point X with an angle between them of θ ∈ (0, π), the face sequences F (R1) and F (R2) are
distinct, and the ﬁrst diﬀerence between them occurs at most one face after a geodesic distance of
O(θ−1L).

Lemma 1.2.2. Let R = (X, ϕ, d) be a geodesic segment with d < ℓ. In O(n) time, we can calculate
F (R), expressed as a sequence S1 of O(n) faces, followed by another sequence S2 of O(n) faces and
a distance over which R visits the faces of S2 periodically2. Also, we can calculate the face, location
in the face, and direction of R at its endpoint other than X.

Corollary 1.2.3. In O(ndℓ−1) time, we can calculate R(X, ϕ, d).

Theorem 1.2.4. Let P be a convex polyhedron with n vertices all of curvature at least ε, let L be
the length of the longest side, and let ℓ be the least distance between points on edges sharing a face
but not a vertex. Then in O(n2ε−2Lℓ−1) time, we can ﬁnd a closed quasigeodesic on P . We can
express such a closed quasigeodesic as a sequence of O(n3ε−2Lℓ−1) subsequences of faces, where for
each subsequence we give a distance for which the closed quasigeodesic visits that subsequence of
faces periodically.

Theorem 2.2.1. Let ϕ ≈ 0.43π be the angle such that tan ϕ = π + ϕ. Then the critical speed ratio
r∗ for a circle is sec ϕ ≈ 4.60.

Theorem 2.2.2. If P is an unbounded intersection of halfplanes and the angle between the two
extreme halfplanes is 2θ ∈ (0, π], then the critical speed ratio r∗ is csc θ.

Theorem 2.3.1. Let P be any polygon. Then the critical speed ratio r∗ is at least maxp,q∈δP dz(p,q)
dh(p,q)
(where dz and dh are the geodesic distances in the zombie and human play areas, respectively).

Theorem 2.3.2. Let P be any polygon. Then the critical speed ratio r∗ is at most 9.2504 maxp,q∈δP dz(p,q)
dh(p,q)
(where dz and dh are the geodesic distances in the zombie and human play areas, respectively).

Theorem 2.3.3. For every polygon P there exists an ε0 > 0, such that ε−1
0 is polynomial in the
coordinates of P and if r∗ is the critical speed ratio for P , then for all ε ∈ (0, ε0) and for all integers
z, h ∈ (0, ε−1), the human wins the (P, ε5, z, h) game if z/h ∈ [1, r∗ 1
(1+ε)3 ) and the zombie wins if
z/h > r∗(1 + ε)3.

Lemma 2.3.4. If the human wins the continuous game, then there exists ε > 0 (not necessarily
bounded by a function of ε0) such that the zombie is at distance at least ε when the human wins.

Lemma 2.3.5. If the human wins the continuous game at a speed ratio r, then there exists ε > 0
(not necessarily bounded by a function of ε0) such that the human can commit to moving in a
straight line for the last ε of their movement, and still win.

Lemma 2.3.6. If the zombie has a winning strategy that leaves the convex hull of P , then it has a
winning strategy that doesn’t.

Lemma 2.3.7. If P is a polygon, then…

Lem…


*[further statements in the full text]*

*[digest of a 147661 character source; every section, statement, and proof in full at `research/sources/hesterberg-escaping-polygons-thesis.full.md`]*
