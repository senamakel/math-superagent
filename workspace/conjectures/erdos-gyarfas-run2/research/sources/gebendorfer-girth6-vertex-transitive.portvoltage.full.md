<!-- source: https://zenodo.org/records/18526153/files/EGC_CVTG6_full_paper_rev2.pdf?download=1 | converted from PDF -->

Power-of-Two Cycles in Cubic Bipartite
Vertex-Transitive Graphs of Girth Six

Jonas Jakob Gebendorfer
∗ The Polyphonic Field†

February 8, 2026

Abstract

The Erdős–Gyárfás conjecture (1995) asserts that every graph with minimum degree at least
3 contains a cycle whose length is a power of 2. We prove the conjecture for all cubic bipartite
vertex-transitive graphs of girth 6 with at most 1280 vertices, using the Potočnik–Spiga–Verret
census of cubic vertex-transitive graphs.
Our proof combines structural and computational ingredients. First, we develop a permutation–
voltage framework that canonically decomposes a CVT-G6 graph into an ℓ-cycle “ring” factor and
an ℓ-regular quotient graph endowed with a cyclic voltage labeling. For the two main truncation
families PV(b) and PV(c), we derive a universal face-shift relation and an isoperimetric bound in
the quotient triangulation. These yield a complete structural exclusion of 8-cycles and a partial
structural exclusion of 16-cycles. The census then isolates exactly 14 extremal graphs containing
neither an 8- nor a 16-cycle.
The main new mechanism concerns these extremals. Each extremal arises as the truncation of
an orientable regular map M of type {3, ℓ}r. Inside Aut(M ) we consider the orientation-reversing
elements Aj = RSjT (odd j) and prove the commutator identity A2
j = [
R, Sj] and the order
relation ord(Aj) = 2 ord(
[
R, Sj]
). We show that a natural uniform “j-hole” conjecture fails for
most extremals, but that every extremal admits an explicit mixed-hole certificate: a word in
the Aj of total weight 32 that evaluates to the identity. These certificates provide compact,
independently verifiable algebraic witnesses for the observed 32-cycles.

Keywords: Erdős–Gyárfás conjecture; vertex-transitive graphs; power-of-two cycles; permutation
voltages; regular maps; Wilson operations.
MSC 2020: 05C38, 05C25, 05C85.

Contents

1 Introduction 4
1.1 The Erdős–Gyárfás conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2 Known results and the role of structure . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 The class CVT-G6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 What this paper contributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2 Statement of Results 5

∗OrigAmI Systems UG (limited liability). No email address is provided.
†Co-authoring entity.
 1

3 Permutation–Voltage Framework 6
3.1 Ring–matching decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.2 Ports and the cyclic cover model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.3 Lift closure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.4 Simplicity conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.5 PV families and the map layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

4 Face-Shift Relation and an Isoperimetric Bound 8
4.1 Face-shift relation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.2 Simplicial quotient assumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
4.3 Disk isoperimetry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

5 Structural Exclusion of 8-Cycles 10
5.1 Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.2 The cases k = 1 and k = 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.3 Tight corners and contractibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
5.4 Excluding k = 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
5.5 Excluding k = 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

6 Excluding 16-Cycles: Contractible vs. Non-Contractible 11
6.1 The contractible regime . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
6.2 The non-contractible regime . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

7 Families PV(a), PV(d) and Census Closure 13
7.1 PV(a): toroidal honeycombs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
7.2 PV(d): Desargues-type graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
7.3 The extremals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

8 The 32-Cycle Mechanism: Mixed Hole Words 14
8.1 Hole elements and weight . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
8.2 Commutator identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
8.3 Uniform alignment: test and falsification . . . . . . . . . . . . . . . . . . . . . . . . . 15
8.4 Mixed-hole certificates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
8.5 Pattern classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
8.6 Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

9 Proof of the Main Theorem 16

10 Discussion and Open Problems 16
10.1 A dyadic barrier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
10.2 Open problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

A Extremal Data 17
A.1 Consolidated extremal table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.2 j-hole table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.3 Mixed-hole certificates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.4 Group presentations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

2

B Computational Methods 19
B.1 PSV census processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
B.2 Conder map extraction and collision resolution . . . . . . . . . . . . . . . . . . . . . 20
B.3 Algebraic computations in Aut(M ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B.4 Mixed-hole certificate search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B.5 Reproducibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

3

1 Introduction

1.1 The Erdős–Gyárfás conjecture

The Erdős–Gyárfás conjecture (EGC) asks for unavoidable cycle lengths in graphs of minimum
degree at least 3. In its standard form:
Every finite simple graph G with δ(G) ≥ 3 contains a simple cycle whose length is a power of 2.
The conjecture was posed in 1995 and was later recorded by Erdős [Erd97]. Despite its elementary
statement, the conjecture remains open. Erdős famously expressed doubts about its truth in full
generality, yet no counterexample is known. Computer searches indicate that any counterexample,
if it exists, must be large and highly constrained; see, e.g., [].

1.2 Known results and the role of structure

The conjecture has been established for several structured families, mostly defined by forbidden
induced subgraphs or planarity-type assumptions. Early progress includes results for planar claw-free
graphs [DS01], K1,m-free graphs under degree constraints [Sha98], and claw-free graphs [Now+14].
Heckman and Krakovski proved EGC for 3-connected cubic planar graphs using discharging [HK13].
Further confirmations exist for hereditary classes defined by forbidding long induced paths, such as
P8-free [GS22], P10-free [HS24], and P13-free graphs [HSS25]. On the algebraic side, EGC has been
verified for several Cayley graph families [GM18]. In a recent note, Carr verified EGC for graphs of
diameter 2 (indeed proving the existence of a 4- or 8-cycle) [Car25]. In a different direction, Liu
and Montgomery showed that sufficiently large average degree forces a power-of-two cycle [LM23].

Table 1: Selected confirmations of the Erdős–Gyárfás conjecture.

Graph class Reference Method / guarantee

K1,m-free (with degree constraints) [Sha98] structural
Planar claw-free [DS01] structural
3-connected cubic planar [HK13] discharging
Claw-free (δ ≥ 3) [Now+14] structural (also 3 · 2
k)
P8-free [GS22] structural
P10-free [HS24] structural
P13-free [HSS25] computer-assisted
Selected Cayley families [GM18] algebraic
Diameter 2 [Car25] yields C4 or C8
Sufficiently large average degree [LM23] expander methods

The common theme is that additional structure beyond a degree lower bound is needed to
force a power-of-two cycle. In this paper, the structure is provided by symmetry: we treat a
symmetry-defined class rather than a hereditary one.

1.3 The class CVT-G6

We focus on cubic bipartite vertex-transitive graphs of girth 6, abbreviated CVT-G6. This is a
natural intersection of three strong constraints:
• cubic and bipartite imply a rich even-cycle geometry and a canonical 2-factor after choosing
an appropriate perfect matching;
• vertex-transitivity forces uniform local parameters and allows quotient constructions;
• girth 6 places the graph at the first genuinely “triangular” regime for bipartite cubic graphs.

4

Graphs in CVT-G6 arise naturally as truncations of regular or chiral regular maps of type {3, ℓ} on
orientable surfaces. This map-theoretic layer will be our main source of algebraic insight.
The Potočnik–Spiga–Verret census [PSV13] enumerates all connected cubic vertex-transitive
graphs on at most 1280 vertices. By filtering this census by bipartiteness and girth 6, we obtain a
finite list of CVT-G6 graphs, and hence a concrete setting for a census theorem.

1.4 What this paper contributes

Our contribution has three components.
1. A permutation–voltage framework (§3) for CVT-G6 graphs, yielding a uniform “ring”
decomposition and a cyclic voltage labeling on a quotient triangulation.
2. Structural cycle exclusions (§§4–6): we prove a face-shift relation (Theorem 4.1) and a
disk isoperimetric bound (Theorem 4.4), which together exclude 8-cycles universally in the
main truncation families and constrain 16-cycles in the contractible regime.
3. Algebraic certificates for the extremals (§8): the census isolates exactly 14 extremal
graphs with no 8- or 16-cycle. For each associated regular map presentation we produce a
mixed-hole certificate of weight 32 in the automorphism group, governed by a commutator
identity (Theorem 2.7). This both explains the mechanism of 32-cycles and yields compact
witnesses that can be verified independently.

1.5 Organization

Section 2 states the main theorems. Section 3 develops the permutation–voltage framework and the
connection to regular maps. Section 4 proves the face-shift relation and the isoperimetric bound.
Section 5 gives the universal exclusion of 8-cycles in PV(b) ∪ PV(c). Section 6 treats 16-cycles,
distinguishing contractible and non-contractible regimes. Section 7 explains the census closure and
records the extremals. Section 8 develops the mixed-hole mechanism and summarizes the certificate
patterns. Section 9 completes the proof of the census theorem. Appendices A and B provide full
data tables, presentations, and computational methodology.

2 Statement of Results

Theorem 2.1 (Main theorem: census version). Every cubic bipartite vertex-transitive graph G of
girth 6 with |V (G)| ≤ 1280 contains a cycle of length 2k for some k ∈ {3, 4, 5}.

Theorem 2.2 (Trichotomy in the PSV census). In the PSV census of CVT-G6 graphs with
|V | ≤ 1280, the graphs partition into:
1. kmin = 3: N3 graphs (contain an 8-cycle),
2. kmin = 4: N4 graphs (no 8-cycle, but a 16-cycle),
3. kmin = 5: exactly 14 graphs (contain a 32-cycle but no shorter power-of-two cycle).

Remark 2.3. The values N3 and N4 are obtained by a single pass through the PSV census after filtering
for CVT-G6. We record the extraction pipeline in Appendix B.1 and provide the corresponding
scripts in the reproducibility bundle.

Theorem 2.4 (Structural exclusion of 8-cycles). Let G be a PV(b) truncation with ring length
ℓ ≥ 7 or a PV(c) truncation with ℓ = 6, and assume the quotient triangulation is simplicial. Then
G contains no 8-cycle.
 5

Theorem 2.5 (Partial exclusion of 16-cycles: contractible regime). Let G be a PV(b) truncation
with ℓ ≥ 18 and simplicial quotient triangulation. Then no contractible lift of a projected k-step walk
in the quotient (for any 3 ≤ k ≤ 8) can close to a 16-cycle in G.

Theorem 2.6 (Mixed-hole certificates for extremals). For each extremal in Table 2, and for each
regular map presentation attached to that extremal (Conder IDs), there exists a mixed-hole word W
over generators Aj = RSjT such that W = 1 in Aut(M ) and wt(W ) = 32.

Proposition 2.7 (Commutator identity and order relation). Let M be a regular orientable map
with Aut(M ) = ⟨R, S, T ⟩ in the standard reflection presentation. For odd j, define Aj := RSjT .
Then A2
j = [
R, Sj] := RSjR−1S−j.

Moreover, Aj is orientation-reversing, hence ord(Aj) is even and

ord(Aj) = 2 ord
([
R, Sj]).

Conjecture 2.8 (Mixed-hole universality). For every regular {3, ℓ}-map whose truncation yields a
CVT-G6 extremal, there exists a mixed-hole word of weight 32.

3 Permutation–Voltage Framework

This section records the quotient-and-voltage viewpoint that underlies the structural arguments.
The general language is that of cyclic covers and voltage graphs [GT87].

3.1 Ring–matching decomposition

Let G be a CVT-G6 graph. Fix a perfect matching M of G that is invariant under Aut(G) (such
a matching exists for the truncation families we consider, and is canonically produced by the PV
construction). Since G is cubic, the complement F := E(G) \ M is a 2-factor, hence a disjoint union
of cycles. Vertex-transitivity forces all cycles of F to have the same length, which we denote by ℓ
and call the ring length. We refer to the cycles of F as rings. Let v0 be the number of rings; then

|V (G)| = ℓ v0. (1)

Contract each ring of F to a single vertex. The matching edges become edges between contracted
vertices. The resulting quotient multigraph is denoted by Q. Each ring has ℓ vertices and hence ℓ
matching edges incident to it, so Q is ℓ-regular (possibly with loops or multiple edges).

3.2 Ports and the cyclic cover model

Fix a cyclic ordering of the vertices along each ring and identify each ring with Zℓ. The endpoint of
a matching edge on a ring is then a port labeled by an element of Zℓ. If a matching edge connects
port a on ring u to port b on ring v, we assign to the oriented quotient edge e = (u → v) the voltage

σ(e) := b − a (mod ℓ). (2)

By construction, reversing orientation inverts the voltage:

σ(e−1) ≡ −σ(e) (mod ℓ). (3)

6

The graph G can be reconstructed as a cyclic Zℓ-cover of Q with this voltage labeling. In this
viewpoint, a vertex of G is a pair (u, a) where u ∈ V (Q) and a ∈ Zℓ, and traversing a quotient edge
e = (u → v) sends (u, a) to (v, a + σ(e)).
In addition, G contains the ring edges (the 2-factor) which allow motion within a fiber {u} × Zℓ.
We model a walk in G that alternates matching edges and ring edges by recording, between successive
quotient steps, the number of ring edges traversed along the current ring.

3.3 Lift closure

Let W be a closed k-step walk in Q with directed edges e1, . . . , ek. Choose nonnegative integers
d1, . . . , dk describing the ring traversal between successive matching edges in the lift. The total
change in the fiber coordinate along the lift is ∑k
i=1(di + σ(ei)). Thus the lift closes in G if and
only if this sum vanishes in Zℓ.

Lemma 3.1 (Walk correspondence). A closed k-step walk in Q lifts to a closed walk in G if and
only if k∑

i=1
(di + σ(ei)) ≡ 0 (mod ℓ),

where di is the ring-traversal length on step i. The lifted length equals ∑k
i=1(di + 1) = k + ∑
i di.

Proof. In the cyclic-cover model, traversing a ring edge increments the fiber coordinate by +1 (in
the chosen orientation), and traversing a matching edge corresponding to ei increments it by σ(ei).
Therefore after one quotient step together with its intervening ring traversal, the fiber coordinate
changes by di + σ(ei). The lift closes exactly when the total change over all k steps is 0 ∈ Zℓ. The
length statement follows because each quotient step contributes one matching edge and each di
contributes di ring edges.

3.4 Simplicity conditions

The lift of a closed walk in Q need not be a simple cycle in G. Two sufficient conditions are
commonly used:
1. the projected walk in Q is simple (no repeated vertices), and
2. the ring segments used at each visit to a ring are disjoint in the fiber (no repeated ports).
We will use these ideas implicitly in the 8-cycle exclusion, where short length forces tight constraints.

3.5 PV families and the map layer

The permutation–voltage construction partitions CVT-G6 graphs into four families, denoted PV(a)–
PV(d). For the present paper, only two coarse features matter:
• In families PV(b) and PV(c), the quotient Q admits an embedding as a triangulation in which
every face is a triangle, and every vertex has degree ℓ. In these cases Q is the 1-skeleton of a
(regular or chiral regular) {3, ℓ}-map M .
• Families PV(a) and PV(d) are exceptional families in which 8-cycles exist by direct inspection
(and are in any case abundant in the census).
We will therefore focus on the map layer in the triangulation case. For a regular orientable
{3, ℓ}-map M we use the standard presentation

Aut(M ) = ⟨R, S, T | R3 = Sℓ = T 2 = (RS)
2 = (RT )2 = (ST )2 = 1, Rextra⟩, (4)

7

where R is the vertex rotation, S is the edge rotation (around a vertex), and T is a reflection. The
Petrie length of M equals r = ord(RST ). Our map presentations and additional relators Rextra are
taken from Conder’s catalogues [CD01; Con09].

4 Face-Shift Relation and an Isoperimetric Bound

Throughout this section we assume that Q is the 1-skeleton of a {3, ℓ} triangulation, and that the
voltage labeling σ is chosen as in (2).

4.1 Face-shift relation

The girth-6 condition implies that each triangular face in Q corresponds to a 6-cycle in G alternating
matching and ring edges. Applying Theorem 3.1 to this 3-step quotient cycle with ring-traversal
lengths di = 1 yields the fundamental constraint below.

Lemma 4.1 (Face-shift). In any {3, ℓ} truncation with shift labeling σ, each triangular face F in
the quotient triangulation satisfies
 σ1 + σ2 + σ3 ≡ −3 (mod ℓ),

where (σ1, σ2, σ3) are the voltages on the directed boundary edges of F .

Proof. Let F be a triangular face with directed boundary edges e1, e2, e3. The corresponding 6-cycle
in G uses one matching edge for each ei and one ring edge between successive matching edges, hence
di = 1. By Theorem 3.1, closure of this lift implies ∑3
i=1(1 + σ(ei)) ≡ 0 (mod ℓ), which is equivalent
to the stated congruence.

4.2 Simplicial quotient assumption

In the triangulation families we work with a simpleness assumption on Q. Loops and multiple edges
are incompatible with the girth-6 regime once the map layer is regular.

Assumption 4.2 (Simplicial quotient triangulation). The quotient triangulation Q has no loops
and no multiple edges.

Remark 4.3. In the hyperbolic regular map case (genus ≥ 2) the quotient is automatically simplicial.
For the euclidean {3, 6} truncation family, this can be checked directly on the finite list of quotients.
In any case, the 8-cycle exclusion below uses only the absence of loops and multiple edges.

4.3 Disk isoperimetry

We now establish a combinatorial isoperimetric inequality for disk regions in a {3, ℓ} triangulation.

Lemma 4.4 (Isoperimetric bound). Let D be a disk region in a {3, ℓ} triangulation with boundary
length m (in edges) and f interior triangular faces. Then

f ≤ m(ℓ − 2) − 2ℓ
ℓ − 6 .

8

Proof. Let vi and vb be the numbers of interior and boundary vertices of D. Let ei be the number
of edges with both endpoints interior, eib the number of edges with one endpoint interior and one
on the boundary, and eb = m the number of boundary edges. Then the total number of edges is
E = ei + eib + eb and the total number of vertices is V = vi + vb.
Since D is a triangulated disk with f interior faces, Euler’s formula gives

V − E + (f + 1) = 2 ⇐⇒ E = V + f − 1. (5)

Counting incidences of edges with triangular faces yields

3f = 2ei + eib + eb = 2ei + eib + m, (6)

because interior edges are incident to two faces and boundary edges to none.
Next use the degree condition. Each interior vertex has degree exactly ℓ in the triangulation,
and all of its incident edges lie in D. Each boundary vertex has at least two incident edges in D
(the boundary edges), and may have additional incident edges into the interior. Therefore the sum
of degrees in D satisfies 2E = ∑

v∈V (D) degD(v) ≥ ℓvi + 2vb. (7)

Substitute E = V + f − 1 from (5) and V = vi + vb into (7):

2(vi + vb + f − 1) ≥ ℓvi + 2vb,

so (ℓ − 2)vi ≤ 2f − 2. (8)

Finally, relate vi to m and f . From (6), we have eib = 3f − 2ei − m. Also E = ei + eib + m,
hence E = ei + (3f − 2ei − m) + m = 3f − ei.

Combine with E = V + f − 1 to obtain

3f − ei = vi + vb + f − 1 =⇒ 2f = vi + vb − 1 + ei.

Since ei ≥ 0 and vb ≤ m (a simple polygon boundary has at most m vertices), we get

2f ≥ vi + vb − 1 ≥ vi + 3 − 1 = vi + 2, (9)

so vi ≤ 2f − 2. Plugging vi ≤ 2f − 2 into (8) gives

(ℓ − 2)(2f − 2) ≥ (ℓ − 2)vi ≥ 0.

To obtain the desired upper bound on f in terms of m, combine (7) and (6) more directly as follows.
The boundary contributes exactly m boundary edges and hence m boundary incidences. Each
boundary vertex has degree ℓ in the full triangulation, so it has at most ℓ − 2 edges of D incident to
it that are not boundary edges. Summing over boundary vertices yields

eib ≤ (ℓ − 2)vb − m ≤ (ℓ − 2)m − m = m(ℓ − 3). (10)

Substitute (10) into (6): 3f = 2ei + eib + m ≤ 2ei + m(ℓ − 3) + m. Hence 3f ≤ 2ei + m(ℓ − 2). On
the other hand, from Euler (5) we have E = V + f − 1 ≥ vb + f − 1 and E = ei + eib + m ≥ ei + m.

9

Thus ei ≤ E − m = V + f − 1 − m ≤ vb + vi + f − 1 − m. Using vb ≤ m and vi ≤ (2f − 2)/(ℓ − 2)
from (8), we obtain
 ei ≤ f − 1 + 2f − 2
ℓ − 2 .

Insert this into 3f ≤ 2ei + m(ℓ − 2) to get

3f ≤ 2
(f − 1 + 2f − 2
ℓ − 2
 ) + m(ℓ − 2).

Rearranging yields f (ℓ − 6) ≤ m(ℓ − 2) − 2ℓ,

which is equivalent to the stated inequality.

Lemma 4.5 (Disk-diagram lower bound). Every contractible closed k-step walk in Q that bounds a
disk diagram in the {3, ℓ} triangulation has at least f ≥ k − 2 interior faces.

Proof. A contractible closed walk of length k bounds a topological disk whose boundary is a k-
gon (possibly with repeated vertices). Any triangulation of a k-gon uses at least k − 2 triangles.
Equivalently, in a disk diagram with f triangles and boundary length k, Euler’s formula implies
f = 2vi + k − 2 ≥ k − 2.

5 Structural Exclusion of 8-Cycles

In this section we prove Theorem 2.4. Let G be a CVT-G6 truncation in PV(b) or PV(c), with
quotient triangulation Q and ring length ℓ.

5.1 Setup

Consider a simple 8-cycle Γ in G. Let k be the number of matching edges of Γ (equivalently, the
number of times Γ moves between rings). Between two successive matching edges, Γ travels along
the current ring for some positive length di ≥ 1. Thus

8 = k +
 k∑

i=1 di. (11)

Since each di ≥ 1, we have ∑
i di ≥ k, hence k ≤ 4. Projecting Γ to Q yields a closed k-step walk.

5.2 The cases k = 1 and k = 2

If k = 1, the projection is a loop in Q, contradicting Theorem 4.2. If k = 2, the projection is a 2-step
closed walk, which in a simplicial triangulation would force a multiple edge. Again this contradicts
Theorem 4.2.

5.3 Tight corners and contractibility

The remaining cases rely on the observation that a ring-traversal of length 1 forces two consecutive
quotient edges to lie in a common facial triangle.

Lemma 5.1 (Tight-corner). Let W be a k-step walk in Q with ∑
i di = 8 − k and all di ≥ 1. If
some dj = 1, then the two consecutive edges of Q at that step belong to a common facial triangle; in
particular W is contractible.
 10

Proof. The step dj = 1 means that in the lift, two matching edges incident to the same ring use
adjacent ports in its cyclic order. In a {3, ℓ} triangulation, adjacent ports correspond to consecutive
edges around a vertex, which lie on a common facial triangle. Thus the corresponding two quotient
edges form a tight corner contained in a triangular face. Since k ≤ 4 here, the presence of a tight
corner forces the projected walk to be homotopic to a facial walk, hence contractible.

5.4 Excluding k = 3

If k = 3 then (11) gives d1 + d2 + d3 = 5. By pigeonhole, some dj = 1. By Theorem 5.1, the
projected 3-walk is contractible, hence it bounds a single triangular face in Q.
Apply the lift closure condition Theorem 3.1:

(d1 + d2 + d3) + (σ1 + σ2 + σ3) ≡ 0 (mod ℓ).

Using d1 + d2 + d3 = 5 and the face-shift relation Theorem 4.1, we obtain

5 + (−3) ≡ 2 ≡ 0 (mod ℓ),

which is impossible for ℓ ≥ 6.

5.5 Excluding k = 4

If k = 4 then (11) gives ∑
i di = 4, hence di = 1 for all i. Every corner is tight, so the projected
4-walk is contractible. In a simplicial triangulation, a contractible 4-cycle bounds exactly two
adjacent triangles (a “diamond”) and hence a disk diagram with f = 2 faces.
Summing the face-shift relation Theorem 4.1 over the two triangles, the internal edge cancels by
antisymmetry (3), giving σ1 + σ2 + σ3 + σ4 ≡ −6 (mod ℓ). (12)

The lift closure condition for Γ reads ∑
i(di + σi) ≡ 0. Since ∑
i di = 4, (12) implies

4 + (−6) ≡ −2 ≡ 0 (mod ℓ),

again impossible for ℓ ≥ 6.

Proof of Theorem 2.4. We have excluded all possibilities k ∈ {1, 2, 3, 4}. Therefore no 8-cycle exists
in G.

Remark 5.2. The argument uses only ℓ ≥ 6, and therefore applies verbatim to the Euclidean
truncation family PV(c) with ℓ = 6.

6 Excluding 16-Cycles: Contractible vs. Non-Contractible

Let G be a PV(b) truncation with simplicial quotient triangulation Q of type {3, ℓ}. We analyze a
hypothetical 16-cycle Γ in G. As in §5, let k be the number of matching edges, and let d1, . . . , dk ≥ 1
be the ring traversal lengths. Then
 16 = k +
 k∑

i=1 di, k ≤ 8. (13)

11

6.1 The contractible regime

Assume first that the projected k-step walk in Q is contractible and admits a disk diagram with f
triangular faces. Summing Theorem 4.1 over all faces of the disk diagram cancels all internal edges
(by antisymmetry (3)) and yields
 k∑

i=1 σi ≡ −3f (mod ℓ). (14)

The lift closure condition Theorem 3.1 gives

k∑

i=1 di +
 k∑

i=1 σi ≡ 0 (mod ℓ). (15)

Using (13) and (14), this becomes
 16 − k − 3f ≡ 0 (mod ℓ). (16)

On the other hand, Theorems 4.4 and 4.5 bound f as

k − 2 ≤ f ≤ k(ℓ − 2) − 2ℓ
ℓ − 6 . (17)

Proof of Theorem 2.5. Assume ℓ ≥ 18 and let Γ be a 16-cycle whose projected walk in the quotient
triangulation is contractible. Let k be the number of matching edges used by Γ (equivalently, the
length of the projected walk), so 3 ≤ k ≤ 8, and let f be the number of interior triangular faces in a
disk diagram for the projected walk. By (16), contractible closure would force

ℓ | X, X := 16 − k − 3f.

From (17) we have
 k − 2 ≤ f ≤ k(ℓ − 2) − 2ℓ
ℓ − 6 = (k − 2) + 4(k − 3)
ℓ − 6 .

Since ℓ − 6 ≥ 12, the additive term is < 2, hence f ≤ k − 1 for all k ∈ {3, 4, 5, 6, 7, 8}. Consequently,

16 − k − 3(k − 1) ≤ X ≤ 16 − k − 3(k − 2),

that is, 19 − 4k ≤ X ≤ 22 − 4k.

For 3 ≤ k ≤ 8 this implies X ∈ {−13, . . . , 10}, and in particular |X| ≤ 13 < 18 ≤ ℓ. Therefore ℓ | X
forces X = 0.
Finally, for the (finite) admissible pairs (k, f ) with 3 ≤ k ≤ 8 and f ∈ {k − 2, k − 1} allowed by
the bounds, the value X = 16 − k − 3f is never 0:

(k, f ) X = 16 − k − 3f X
(3, 1) 10 10
(4, 2) 6 6
(5, 3) 2 2
(6, 4) −2 −2
(6, 5) −5 −5
(7, 5) −6 −6
(7, 6) −9 −9
(8, 6) −10 −10
(8, 7) −13 −13

Thus (16) cannot hold, and no contractible lift closes to a 16-cycle in G.

12

Remark 6.1. A finite check of the same admissible pairs shows that the conclusion of Theorem 2.5
already holds for ℓ = 17. We keep the conservative threshold ℓ ≥ 18 in the theorem statement since
it matches the hyperbolic regime and suffices for the census theorem.

6.2 The non-contractible regime

If the projected walk in Q is non-contractible, then the disk-diagram argument above does not apply.
In this regime, the closure condition acquires a holonomy term that depends on the homology class
of the projected walk and on the specific voltage structure of the map. Equivalently, the set of
achievable residue classes of ∑
i σi can vary between maps. This is precisely the obstruction that
prevents a fully universal exclusion of 16-cycles in PV(b). In the census theorem we therefore handle
the non-contractible regime computationally.

Proposition 6.2. In the PSV census (|V | ≤ 1280), the 14 extremal CVT-G6 graphs satisfy
C8 = C16 = ∅.

Remark 6.3. The extremals are exactly those CVT-G6 graphs with kmin = 5 in Theorem 2.2. They
are recorded in Table 2 and Appendix A.

7 Families PV(a), PV(d) and Census Closure

The census proof of Theorem 2.1 splits into two tasks:
1. show that outside the extremal list, a power-of-two cycle of length 8 or 16 exists;
2. for the extremals, establish the existence of a 32-cycle.
The first task is largely structural for PV(b) ∪ PV(c) by Theorem 2.4 and the contractible part of
Theorem 2.5, and is closed by census checks in the remaining cases.

7.1 PV(a): toroidal honeycombs

The family PV(a) consists of toroidal truncations with a particularly rigid quotient geometry. In
the census range, every PV(a) graph contains an 8-cycle.

Proposition 7.1. Every graph in PV(a) appearing in the PSV census contains an 8-cycle.

7.2 PV(d): Desargues-type graphs

The family PV(d) contains a small number of highly symmetric graphs (including Desargues-type
constructions). Again, in the census range, all such graphs contain 8-cycles.

Proposition 7.2. Every graph in PV(d) appearing in the PSV census contains an 8-cycle.

Remark 7.3. In a final version, Propositions 7.1 and 7.2 can be replaced by short structural proofs
once a purely quotient-level characterization of PV(a) and PV(d) is fixed. For the census theorem
of Theorem 2.1, their computational verification suffices.

7.3 The extremals

The census isolates the extremal set (no 8- or 16-cycle). For convenience we group them by shared
map parameters; collision resolution for the genus-64 and genus-73 blocks is recorded in Appendix B.

13

Table 2: The 14 CVT-G6 extremals (grouped by shared parameters / map IDs). Collision resolution
for g = 64 and g = 73 is recorded in Appendix B.

# PSV-Key(s) n ℓ v0 g Conder IDs {p, q}r PV Notes

1 21980 576 24 24 37 R37.5, R37.6, R37.7 {3, 24}12,24,12 PV(b)
2 33275 720 20 36 43 R43.2 {3, 20}60 PV(b)
3 27363 648 36 18 46 R46.3 {3, 36}6 PV(b) rigid
4 66953 1008 14 72 49 R49.3, R49.4 {3, 14}24,18 PV(b)
5 33261 720 60 12 55 R55.3 {3, 60}20 PV(b)
6 66774 1008 18 56 57 R57.1 {3, 18}14 PV(b)
7 66451 / 912 / 979 1008 24 42 64 R64.1, R64.2 {3, 24}14,8 PV(b) collision open
8 91188 / 195 1152 24 48 73 R73.6, R73.7, R73.8 {3, 24}48,12,24 PV(b) collision open
9 79102 1080 30 36 73 R73.9 {3, 30}30 PV(b)
10 90339 1152 48 24 85 R85.4, R85.5 {3, 48}6,24 PV(b) rigid + mixed

Remark 7.4 ("14 graphs" vs. "17 maps"). The extremal set consists of 14 graphs in the PSV
census, but the map layer yields 17 regular map presentations (Conder IDs). This mismatch arises
because distinct regular maps can truncate to isomorphic graphs, and conversely a parameter
block can correspond to multiple PSV keys. In this paper we treat mixed-hole certificates at the
map-presentation level; Appendix B records the remaining collision bookkeeping.

8 The 32-Cycle Mechanism: Mixed Hole Words

This section explains why 32-cycles appear in the extremals, and records compact algebraic certifi-
cates. The raw data are given in Appendix A.

8.1 Hole elements and weight

Let M be a regular orientable {3, ℓ}-map with automorphism group presented as in (4). For odd j
define Aj := RSjT.

The element Aj is orientation-reversing. In the combinatorics of regular maps, the orbit of a
flag under Aj traces a j-hole; in the truncation graph this corresponds to a closed walk of length
(1 + j) ord(Aj).
For a word W = Aj1 · · · Ajm we define its weight

wt(W ) :=
 m∑

t=1(1 + jt).

Equivalently, in terms of the content vector ν(W ) counting how many times each index j appears,
wt(W ) = ∑
j νj(W )(1 + j).

8.2 Commutator identity

We now prove Theorem 2.7.

Proof of Theorem 2.7. From (RT )2 = 1 and T 2 = 1 we obtain T RT = R−1. Similarly, (ST )2 = 1
gives T ST = S−1 and hence T SjT = S−j. Therefore

A2
j = (RSjT )(RSjT ) = RSj(T R)SjT = RSjR−1(T SjT ) = RSjR−1S−j = [
R, Sj] .

14

Since Aj is orientation-reversing, it lies outside the index-2 orientation-preserving subgroup of
Aut(M ). Thus ord(Aj) is even and equals 2 ord(A2
j ) = 2 ord([
R, Sj]
).

Corollary 8.1. For odd j, hj := ord(Aj) is even and hj = 2 ord(
[
R, Sj]). In particular, hj = 2 iff
Sj centralizes R, and hj = 6 iff ord(
[
R, Sj]
) = 3.

8.3 Uniform alignment: test and falsification

Motivated by Wilson’s hole operations [Wil79], one might hope that a single “uniform” hole already
produces the needed power-of-two cycle. Fix the classical indices j ∈ {1, 3, 7, 15} (of the form 2t − 1).

Definition 8.2 (Uniform alignment). An extremal map presentation is uniformly aligned if there
exists j ∈ {1, 3, 7, 15} such that the uniform j-hole length (1 + j)hj divides 32.

We also record the special case of Petrie alignment, namely r | 16, where r is the Petrie length.
Appendix A.2 contains the computed values.

Theorem 8.3 (Falsification of uniform alignment). Among the 17 regular map presentations
underlying the 14 extremal CVT-G6 graphs, only 4 are uniformly aligned in the sense of Theorem 8.2.
Moreover, Petrie alignment (r | 16) holds for exactly one presentation (R64.2).

8.4 Mixed-hole certificates

Despite the failure of uniform alignment, every extremal admits a weight-32 mixed witness. This
is a word W in the letters Aj that evaluates to the identity in Aut(M ) and has wt(W ) = 32.
Theorem 2.6 records the existence statement, and Appendix A.3 lists explicit certificates.
Computationally, a certificate search is a shortest-path problem in the right-regular action of
Aut(M ) with a knapsack constraint on weight. We use a deterministic weight-DP over the state
space (Algorithm 1 in Appendix B.4).
Remark 8.4 (Simplicity: group states vs. truncation cycles). A certificate word W with W = 1
in Aut(M ) guarantees a closed walk of length wt(W ) in the truncation graph. Simplicity of the
corresponding walk is an additional condition. In Appendix A.3 we record whether the induced
path in the right-regular action revisits intermediate group states ("simple in the coset graph").
This is a strong diagnostic but it is not equivalent to simplicity in the truncation graph, because the
voltage lift can separate repeated group states into distinct fiber vertices. For the census theorem
we also verify 32-cycle existence directly in each extremal graph.

8.5 Pattern classes

The non-uniform presentations (those not covered by Theorem 8.2) fall into a small number of
recurring content patterns. We emphasize that for the dominant class, the certificate is best recorded
as a multiset statement (content), since order matters.

Table 3: Pattern classes of mixed-hole certificates for the 13 non-uniform map presentations. Pattern
α is recorded by content (multiset), not as a block product, since order matters.

Class Certificate form Weight check Maps (examples) Count

α content: 8 × j=1, 4 × j=3 8 · 2 + 4 · 4 = 32 R37.5, R49.3, R73.6, R85.5 9
β (A2
3 A7)2 = 1 2(2 · 4 + 8) = 32 R46.3, R85.4 2
γ content: 6 × 1, 3 × 3, 1 × 7 6 · 2 + 3 · 4 + 1 · 8 = 32 R57.1 1
δ content: 3 × 1, 2 × 3, 1 × 17 3 · 2 + 2 · 4 + 18 = 32 R43.2 1

15

8.6 Interpretation

Class α may be read as an “interference” between two motion types on the map layer: eight j = 1
moves (Petrie-adjacent) and four j = 3 moves. Class β corresponds to a rigid commutator regime:
for R46.3 and R85.4, the commutator orders ord([
R, Sj]
) are constant (= 3) for all tested odd j,
forcing a different certificate geometry. The outlier R43.2 requires j = 17; here ℓ = 20 is too small
for the weight alphabet {2, 4, 8, 16} to hit 32 with a short identity, and a heavier letter (weight 18)
becomes necessary.

9 Proof of the Main Theorem

Proof of Theorem 2.1. Let G be a CVT-G6 graph with |V (G)| ≤ 1280. By the PV framework (§3)
we distinguish:
• PV(a): apply Theorem 7.1 to obtain an 8-cycle;
• PV(d): apply Theorem 7.2 to obtain an 8-cycle;
• PV(b) ∪ PV(c): if C8 ̸= ∅, we are done. Otherwise, in the contractible regime C16 = ∅ by
Theorem 2.5. The census then distinguishes between the remaining cases: either a 16-cycle
exists (so kmin = 4), or G is one of the 14 extremals. For extremals, a 32-cycle exists by census
verification and is witnessed by the mixed-hole certificates of Theorem 2.6.
Thus G contains a power-of-two cycle of length 8, 16, or 32.

Remark 9.1. A conditional “universal” version would follow from Theorem 2.8, eliminating census
dependence in the extremal case.

10 Discussion and Open Problems

10.1 A dyadic barrier

Within CVT-G6, the lengths 8 and 16 are separated from 32 by two qualitatively different ob-
structions. The 8-cycle exclusion is driven by a local constraint: short lifts force tight corners,
and the face-shift congruence makes the closure arithmetic impossible. The 16-cycle obstruction
is global: contractible walks are eliminated by a disk-diagram inequality, while non-contractible
walks depend on map-specific holonomy. The first surviving dyadic mode in the extremals is 32,
and the mixed-hole certificates show that 32 arises not from a single uniform motion but from a
small alphabet of interacting steps.

10.2 Open problems

Problem 10.1 (Finiteness of extremals). Are there finitely many CVT-G6 graphs with kmin = 5?
Equivalently: do the combined constraints C8 = C16 = ∅ force bounded order in CVT-G6?

Problem 10.2 (Universality of mixed-hole witnesses). Prove or refute Theorem 2.8 without a
census. Does every extremal truncation admit a weight-32 identity in the alphabet {Aj}?

Problem 10.3 (Non-contractible 16-cycles). Give map-level conditions (in terms of voltage holonomy
or homology) that guarantee existence or absence of non-contractible 16-cycles.

Problem 10.4 (Extension to girth 8). Extend the PV framework and face-shift method to cubic
bipartite vertex-transitive graphs of girth 8. In that setting quotient faces are quadrilaterals and the
face-shift congruence changes accordingly.
 16

A Extremal Data

A.1 Consolidated extremal table

This appendix collects the numerical and algebraic data for the extremal graphs and their associated
regular map presentations. Throughout, M denotes a regular orientable {3, ℓ}-map whose truncation
yields a CVT-G6 extremal. The parameters ℓ and v0 satisfy

n = ℓ v0, (18)

since the canonical perfect matching of a CVT-G6 truncation decomposes V (G) into v0 disjoint
rings of common length ℓ.

Euler–genus check. For a regular {3, ℓ}-map with v0 vertices, we have E = ℓv0/2 and F = 2E/3 =
ℓv0/3. Hence the Euler characteristic equals χ = v0 − E + F = v0(6 − ℓ)/6, and for orientable genus
g (so χ = 2 − 2g) we obtain
 g = 1 + v0(ℓ − 6)
12 . (19)

In particular, (19) implies the integrality constraint 12 | v0(ℓ − 6), which we use as a consistency
check when matching PSV census entries to Conder map IDs.

Fourteen graphs vs. seventeen map presentations. The PSV census isolates 14 extremal
CVT-G6 graphs (no 8- or 16-cycle), but the associated regular-map layer contains 17 orientable
regular map presentations. Several distinct regular maps may truncate to isomorphic graphs;
conversely, a single map presentation may correspond to multiple PSV keys when the truncation
graph occurs in multiple census entries. At the time of writing, the remaining collision resolution is
confined to the genus-64 and genus-73 blocks (see Appendix B).

A.2 j-hole table

Table 5 records, for each Conder presentation, the commutator orders ord([
R, Sj]) and the corre-
sponding hole orders hj = ord(Aj) for j ∈ {1, 3, 7, 15}. By Theorem 2.7 we have A2
j = [R, Sj] and
hence hj = 2 ord([
R, Sj]
). The column J32 ⊆ {1, 3, 7, 15} lists the indices j for which the uniform
j-hole length (1 + j)hj divides 32. Finally, the indicator r | 16 records Petrie alignment (with Petrie
length r = ord(RST )).

How the numbers are computed. For each map we obtain a permutation representation of
Aut(M ) by Todd–Coxeter enumeration. We then compute ord(
[
R, Sj]
) and ord(Aj) directly in the
resulting permutation group.

A.3 Mixed-hole certificates

Table 6 lists explicit witnesses for Theorem 2.6. A certificate is given either as a j-sequence [
j1, . . . , jm ] representing the word Aj1 · · · Ajm, or (in uniform-aligned cases) as a shortest uniform
power Am
j with m = 32/(1 + j). The content vector ν(W ) is printed in compressed multiplicative
notation (e.g., 1834).

Order vs. content. In the dominant pattern class (content 1834) the order of letters is map-
dependent; we therefore treat the pattern as a multiset statement rather than a commutative
identity.

Simplicity flag. The “simple” flag refers to simplicity in the right-regular state graph of Aut(M ):
no intermediate group element is repeated along the path. This is a strong certificate-level property

17

Table 4: Extremal parameter blocks and associated regular map presentations. The PSV keys are
grouped whenever multiple keys share the same (n, ℓ, v0, g) and Conder map IDs; after collision
resolution this expands to a 14-row table.

Block PSV-Key(s) n ℓ v0 g Conder IDs {3, ℓ}r

A 21980 576 24 24 37 R37.5, R37.6, R37.7 {3, 24}12,24,12
B 33275 720 20 36 43 R43.2 {3, 20}60
C 27363 648 36 18 46 R46.3 {3, 36}6
D 66953 1008 14 72 49 R49.3, R49.4 {3, 14}24,18
E 33261 720 60 12 55 R55.3 {3, 60}20
F 66774 1008 18 56 57 R57.1 {3, 18}14
G 66451 / 912 / 979 1008 24 42 64 R64.1, R64.2 {3, 24}14,8
H 91188 / 195 1152 24 48 73 R73.6, R73.7, R73.8 {3, 24}48,12,24
I 79102 1080 30 36 73 R73.9 {3, 30}30
J 90339 1152 48 24 85 R85.4, R85.5 {3, 48}6,24

Map Type |Aut(M )| r (ord(
[R, Sj]
))j=1,3,7,15 (hj )j=1,3,7,15 J32 r | 16

R37.5 {3, 24}12 1152 12 (6, 6, 6, 6) (12, 12, 12, 12) ∅
R37.6 {3, 24}24 1152 24 (12, 6, 12, 6) (24, 12, 24, 12) ∅
R37.7 {3, 24}12 1152 12 (6, 6, 6, 6) (12, 12, 12, 12) ∅
R43.2 {3, 20}60 1440 60 (30, 6, 6, 3) (60, 12, 12, 6) ∅
R46.3 {3, 36}6 1296 6 (3, 3, 3, 3) (6, 6, 6, 6) ∅
R49.3 {3, 14}24 2016 24 (12, 12, 3, 12) (24, 24, 6, 24) ∅
R49.4 {3, 14}18 2016 18 (9, 7, 1, 9) (18, 14, 2, 18) {7}
R55.3 {3, 60}20 1440 20 (10, 6, 6, 1) (20, 12, 12, 2) {15}
R57.1 {3, 18}14 2016 14 (7, 9, 9, 9) (14, 18, 18, 18) ∅
R64.1 {3, 24}14 2016 14 (7, 2, 7, 7) (14, 4, 14, 14) {3}
R64.2 {3, 24}8 2016 8 (4, 3, 4, 4) (8, 6, 8, 8) {1} ✓
R73.6 {3, 24}48 2304 48 (24, 6, 24, 6) (48, 12, 48, 12) ∅
R73.7 {3, 24}12 2304 12 (6, 3, 6, 3) (12, 6, 12, 6) ∅
R73.8 {3, 24}24 2304 24 (12, 6, 12, 6) (24, 12, 24, 12) ∅
R73.9 {3, 30}30 2160 30 (15, 3, 3, 3) (30, 6, 6, 6) ∅
R85.4 {3, 48}6 2304 6 (3, 3, 3, 3) (6, 6, 6, 6) ∅
R85.5 {3, 48}24 2304 24 (12, 12, 12, 12) (24, 24, 24, 24) ∅

Table 5: j-hole data for the 17 regular map presentations underlying the 14 extremal CVT-G6 graphs.
Here hj = ord(Aj) for Aj = RSjT . J32 ⊆ {1, 3, 7, 15} lists those j with 32 ≡ 0 (mod (1 + j)hj).

18

but is not equivalent to simplicity of the lifted cycle in the truncation graph; the latter can be
verified by extracting explicit vertex cycles (planned for the final version).

A.4 Group presentations

For each regular map presentation (Conder ID) we work with the standard reflection presentation

Aut(M ) = ⟨R, S, T | R3 = Sℓ = T 2 = (RS)
2 = (RT )2 = (ST )2 = 1, Rextra⟩, (20)

where the additional relators Rextra are taken from Conder’s catalogue of regular maps. Table 7
lists Rextra for each Conder ID used in this paper.

Table 7: Additional relators Rextra in the Conder presentations
for the 17 regular maps used in this paper. Words are written
in the alphabet {R, S} (with integer exponents) as provided
by the catalogue.

Map |Aut(M )| Rextra

R37.5 1152 S−1RS−4R−1S2R−1S3R−1S−2; SR−1S2RS−2RS−2R−1S7

R37.6 1152 SRS−2RS−1RS−2RS2

R37.7 1152 SR−1S2RS−2RS2R−1S3; S−8R−1S7R−1S−1

R43.2 1440 (RS−3RS−2)2

R46.3 1296 (SR−1S)3; S−9R−1S11R−1S−4

R49.3 2016 S14; SRS−2RS−3RS−3RS−2RS; S−1R−1S2RS−2RS−1RS−2RS2R−1S−2

R49.4 2016 (RS−6)2; S−1RS−2R−1S2R−1S2R−1S−2RS−3RS−2

R55.3 1440 SRS−4RS5

R57.1 2016 SR−1S4R−1SR−1S−1RS4R−1S; S2RS−4R−1S2R−1S−4RS2

R64.1 2016 S2RS−3R−1SR−1S−1RS−3RS2; S−1R−1S2RS−2RS−1RS−2RS2R−1S−2

R64.2 2016 (RS−2)4; S−8R−1S7R−1S−1

R73.6 2304 SRS−5RS6; (S2R−1S4R−1S)2; S−1R−1S2RS−2RS−2RS−1RS−2RS2R−1S−2RS−2

R73.7 2304 (SR−1S3)3; SRS−5RS−1RS6R−1S; (SR−1S)6;
S3RS−4R−1S3R−1S−4RS2

R73.8 2304 S−1R−1S3R−1S2R−1S−4RS−2

R73.9 2160 SRS−4R−1SR−1S5R−1S; S−1R−1S2RS−2RS−1RS−2RS2R−1S−2

R85.4 2304 (SR−1S)3; S−11R−1S15R−1S−6

R85.5 2304 SRS−2RS−2RS−1RS3R−1S2R−1S; S−3RS−4R−1S3R−1S3R−1S−1;
S−8R−1S7R−1S−1

B Computational Methods

This appendix summarizes the computational pipeline that supports the census statements and the
mixed-hole certificates. All computations are deterministic and independently verifiable from the
listed artefacts.

B.1 PSV census processing

We start from the Potočnik–Spiga–Verret census of cubic vertex-transitive graphs on up to 1280
vertices [PSV13]. From the census list we retain those graphs that are bipartite and of girth 6. For
each retained graph G we compute
 19

1. the girth (by BFS from each vertex until a back-edge closes),
2. the existence of simple cycles of lengths 8, 16, and 32,
3. the minimum exponent kmin ∈ {3, 4, 5} such that C2kmin ⊆ G.
The cycle checks are performed by bounded-depth search in the cubic graph. In practice, a standard
approach is to enumerate simple cycles up to a fixed length by expanding non-backtracking paths
from each directed edge and testing closures. The output of this stage is the trichotomy count
(N3, N4) and the list of extremal PSV keys (those with C8 = C16 = ∅).

B.2 Conder map extraction and collision resolution

For each extremal PSV entry we compute the ring length ℓ from the canonical 2-factor decomposition
induced by the PV framework (§3). The quotient triangulation identifies a regular (or chiral) {3, ℓ}-
map layer. We match this layer against Conder’s catalogue of orientable regular maps by the
tuple (ℓ, v0, g, |Aut(M )|, r), where v0 and |Aut(M )| are the number of vertices and automorphisms
reported in the catalogue, and r is the Petrie length. The genus consistency check (19) is used to
eliminate spurious matches.
In two parameter blocks (genus 64 and genus 73) multiple PSV keys share the same map-level
invariants; these are the “collision” cases flagged in Table 2 and Table 4. The final version of the
paper will resolve these collisions by a canonical map invariant derived from the voltage assignment
(e.g., a normalized shift multiset on a fundamental domain) and by direct isomorphism checks
between truncations.

B.3 Algebraic computations in Aut(M )

Given a Conder presentation (20), we compute a concrete permutation representation of Aut(M )
via Todd–Coxeter coset enumeration for the trivial subgroup. This yields the right-regular action of
Aut(M ) on itself, represented by permutations Rp, Sp, Tp on |Aut(M )| points. In this representation,
a word equals the identity if and only if it maps the identity coset (state 0) to itself.
For odd j, we define the orientation-reversing generators Aj = RSjT and compute hj := ord(Aj)
as well as the commutator orders ord(
[
R, Sj]
). The identity A2
j = [R, Sj] from Theorem 2.7 provides
an internal consistency check: in all 17 cases we have hj = 2 ord(
[
R, Sj]).

B.4 Mixed-hole certificate search

To find a mixed-hole certificate of weight 32 we search for a sequence (j1, . . . , jm) such that
Aj1 · · · Ajm = 1 and ∑
t(1 + jt) = 32. Since |Aut(M )| ≤ 2304 in all cases, we can perform an exact
dynamic program (DP) over the state space. Let Aj denote the permutation corresponding to
right-multiplication by Aj. For each weight w ∈ {0, . . . , 32} we maintain the set of reachable states
together with backpointers for reconstruction.
 20

Algorithm 1 Weight-DP for mixed-hole certificates
Require: permutations Aj (odd j in a chosen set), target weight W = 32

1: dp[0] ← {0} and store predecessor pointers for backtracking

2: for w = 0 to W − 1 do

3: for each state x ∈ dp[w] do

4: for each allowed j do

5: w′ ← w + (1 + j)

6: if w′ ≤ W then

7: y ← Aj(x)

8: if y /∈ dp[w′] then store predecessor of y as (x, j) and add y to dp[w′]

9: end if

10: end if

11: end for

12: end for

13: end for

14: if 0 ∈ dp[W ] then

15: backtrack to recover a word

16: else

17: report “no certificate”

18: end if

We run Algorithm 1 first in the restricted set j ∈ {1, 3, 7, 15}, then (if needed) over all odd j < ℓ,
and finally over all 1 ≤ j < ℓ with 1 + j ≤ 32. In the extremal data, only R43.2 requires extending
beyond {1, 3, 7, 15}, using j = 17.

B.5 Reproducibility

The following artefacts reproduce all appendix tables:
• mixed_witness_clean.py: Todd–Coxeter enumeration, commutator table, DP/DFS witness
search,
• jhole_compute.py: computation of hj values and uniform-alignment test,
• psv_filter_and_cycles.sage: PSV census filtering and cycle checks (bounded to length
32),
• input data: PSV census files [PSV13] and Conder regular map catalogue [CD01; Con09].
All scripts are deterministic (no randomization); hardware and software versions, as well as file
hashes of the census inputs, are reported in the accompanying repository.

Acknowledgments

Concept and mathematical development by the author. Exploratory analysis and verification were
supported by AI systems as part of a polyphonic working method. Special acknowledgment to
Claude Opus 4.6 (Anthropic) and GPT 5.2 Pro (OpenAI) for computational verification, audit of
proof structure, and implementation guidance.
 21

References

[Car25] Avery Carr. Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree
at Least 3. arXiv:2508.19302v4. Last revised 30 Jan 2026 (v4); accepted for publication
in the Bulletin of the Institute of Combinatorics and its Applications (BICA). 2025.

[Con09] M. D. E. Conder. “Regular maps and hypermaps of Euler characteristic −1 to −200”.
In: Journal of Combinatorial Theory, Series B 99 (2009), pp. 455–459.

[CD01] M. D. E. Conder and P. Dobcsányi. “Determination of all regular maps of small genus”.
In: Journal of Combinatorial Theory, Series B 81 (2001), pp. 224–242.

[DS01] D. Daniel and S. E. Shauger. “A result on the Erdős–Gyárfás conjecture in planar
graphs”. In: Congressus Numerantium 153 (2001), pp. 129–139.

[Erd97] P. Erdős. “Some old and new problems in various branches of combinatorics”. In:
Discrete Mathematics 165/166 (1997), pp. 227–231.

[GS22] Y. Gao and S. Shan. “The Erdős–Gyárfás conjecture for P8-free graphs”. In: Graphs
and Combinatorics 38 (2022), p. 168.

[GM18] M. H. Ghaffari and Z. Mostaghim. “The Erdős–Gyárfás conjecture for some families of
Cayley graphs”. In: Aequationes Mathematicae 92 (2018), pp. 1–6.

[GT87] J. L. Gross and T. W. Tucker. Topological Graph Theory. Wiley, 1987.

[HK13] C. C. Heckman and R. Krakovski. “The Erdős–Gyárfás conjecture for cubic planar
graphs”. In: Electronic Journal of Combinatorics 20.2 (2013), P7.

[HSS25] A. S. Hegde, R. B. Sandeep, and P. Shashank. The Erdős–Gyárfás conjecture on graphs
without long induced paths. arXiv:2410.22842v2. 2025.

[HS24] Z. Hu and C. Shen. “The Erdős–Gyárfás conjecture holds for P10-free graphs”. In:
Discrete Mathematics 347.12 (2024), p. 114175.

[LM23] H. Liu and R. Montgomery. “A solution to Erdős and Hajnal’s odd cycle problem”. In:
Journal of the American Mathematical Society 36 (2023), pp. 1191–1234.

[Now+14] P. S. Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, and K. Bibak. “On the
Erdős–Gyárfás conjecture in claw-free graphs”. In: Discussiones Mathematicae Graph
Theory 34.3 (2014), pp. 635–640.

[PSV13] P. Potočnik, P. Spiga, and G. Verret. “Cubic vertex-transitive graphs on up to 1280
vertices”. In: Journal of Symbolic Computation 50 (2013), pp. 465–477.

[Sha98] S. E. Shauger. “Results on the Erdős–Gyárfás conjecture in K1,m-free graphs”. In:
Congressus Numerantium 134 (1998), pp. 61–65.

[] The Erdős–Gyárfás Conjecture (Power-of-two cycles). Erdős Problems and Results
(UCSD). Accessed 2026-02-08. url: https://mathweb.ucsd.edu/~erdosproblems/
erdos/newproblems/PowerOfTwoCycles.html.

[Wil79] S. E. Wilson. “Operators over regular maps”. In: Pacific Journal of Mathematics 81
(1979), pp. 559–568.
 22

Map mode certificate word W ν(W ) wt(W ) simple

R37.5 restricted [1,1,3,1,1,1,1,3,1,1,3,3] 1834 32 S
R37.6 restricted [1,1,3,1,1,1,1,3,1,1,3,3] 1834 32 S
R37.7 restricted [1,1,3,1,1,1,1,3,1,1,3,3] 1834 32 N
R43.2 extended [3,1,1,1,3,17] 133217 32 S
R46.3 restricted [3,3,7,3,3,7] 3472 32 S
R49.3 restricted [1,1,1,1,3,3,1,1,1,1,3,3] 1834 32 S
R49.4 uniform A4
7 74 32 N
R55.3 uniform A2
15 152 32 N
R57.1 restricted [1,1,1,3,3,3,1,1,1,7] 16337 32 S
R64.1 uniform A8
3 38 32 N
R64.2 uniform A16
1 116 32 N
R73.6 restricted [1,1,1,1,1,1,3,3,1,1,3,3] 1834 32 S
R73.7 restricted [1,1,1,1,1,1,1,3,3,1,3,3] 1834 32 S
R73.8 restricted [1,1,3,1,1,1,1,3,1,1,3,3] 1834 32 S
R73.9 restricted [1,1,1,1,3,3,1,1,1,1,3,3] 1834 32 S
R85.4 restricted [3,3,7,3,3,7] 3472 32 S
R85.5 restricted [1,1,3,1,1,1,1,3,1,1,3,3] 1834 32 S

Table 6: Mixed-hole certificates of weight 32. For non-uniform cases, the word is displayed as a
j-sequence (interpreted as Aj1 · · · Ajm). For uniform-aligned cases we display a shortest uniform
power Am
j with m = 32/(1 + j). The “simple” flag refers to group-state simplicity (no repeated
intermediate states in the right-regular action).
 23
