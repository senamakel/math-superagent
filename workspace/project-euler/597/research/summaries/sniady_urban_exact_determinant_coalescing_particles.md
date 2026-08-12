> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/sniady_urban_exact_determinant_coalescing_particles.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2602.10782 | converted from PDF -->

## What it claims

Abstract. When particles on a line collide, they may coalesce into one. Such
systems arise in the voter model, where boundaries between opinion clusters
perform coalescing random walks, and in reaction-diffusion theory, where
diffusing particles merge on contact. Computing exact coalescence probabilities
has been difficult because collisions reduce the particle count, while classical
determinantal methods require a fixed number of particles throughout. We
introduce ghost particles: when two particles collide, one survivor continues as
usual and one invisible ghost is created alongside it, preserving the total count.
This restores the square matrix structure needed for a determinantal formula.
We prove that the probability of any specified coalescence pattern—which initial
particles merge into which survivors—is given by a determinant whose entries
are transition probabilities. Integrating out ghost positions yields a closed-form
formula for the surviving particles alone: the coalescence determinant. The
only assumptions are the Markov property and nearest-neighbor transitions,
so…

T…

## Statements it makes

Theorem 1.1 (Coalescence formula, informal version of Theorem 3.2). The proba-
bility that the final outcome follows the prescribed coalescence pattern, with the final
entities at the positions above, is the determinant

Definition 2.1 (Spacetime graph). A spacetime graph is a directed acyclic graph
D = (V, E) equipped with an edge weight function w : E → R, where R is a
commutative ring (e.g., Z for combinatorial counting, R≥0 for probabilities, or
formal power series for generating functions). The directed acyclic graph structure
induces a time ordering: u ⋖ v if there is a directed path from u to v. This is a
partial order; for the sign-reversing involution (Section 8), we fix a linear extension
≤ of ⋖. The combinatorial proof works for any such extension. The phrase “first
crossing” means first in this order.

Definition 2.2 (Paths and weights). A path from x to y is a sequence of vertices
(v0, v1, . . . , vℓ) with v0 = x, vℓ = y, and each (vi, vi+1) ∈ E. We identify a path
with its set of vertices {v0, . . . , vℓ}, writing v ∈ P when v is a vertex of P ; thus for
paths A, C the intersection A ∩ C and union A ∪ C are sets of vertices. The weight
of a path is the product of its edge weights:

Definition 2.4 (Source and target sets). The source set X ⊆ V and target set
Y ⊆ V are each equipped with a linear order ≺.

Definition 2.5 (Planar configuration). The pair (X , Y) is planar if:

Definition 2.6 (Interval labeling). The initial particle (also called actor ) starting
at xj is labeled by the unit half-open interval Ij = [j, j + 1); we also write xIj or
xI for the starting position of actor I. The set of actors is A = {I1, . . . , In}. The
junction points are J = {2, 3, . . . , n}—the shared endpoints between consecutive

Definition 2.7 (Heir function). For ghost g ∈ G, we write heir(g) for the unique
heir interval containing junction g: heir(g) = [a, b) where a < g < b.

Definition 2.9 (Genealogy tree). A genealogy for an heir H ∈ H records which
initial particles merged to form H. It is an oriented tree T embedded in D with:

Definition 2.10 (Genealogy forest). A genealogy forest is a collection T = {TH :
H ∈ H} of genealogies satisfying:

Proposition 2.11 (Consecutivity). Under the planarity assumption (Definition 2.5),
the label Iv at each vertex is an interval: if particles A and C have both reached v,
then so has every particle B between them.

Definition 2.12 (Ghost paths). For each ghost g ∈ G, let cg be the internal vertex
where junction g was dissolved—the unique earliest vertex v of the genealogy forest
whose label Iv contains g in its interior, so that the particles on both sides of g have
merged by v; a simultaneous multi-way merger may serve as cg for several ghosts

Definition 2.13 (Performance). A performance P consists of:
• a genealogy forest T ;
• a ghost path Γg for each ghost g ∈ G.
The weight of the performance is the…

D…


*[further statements in the full text]*

*[digest of a 153910 character source; every section, statement, and proof in full at `research/sources/sniady_urban_exact_determinant_coalescing_particles.full.md`]*
