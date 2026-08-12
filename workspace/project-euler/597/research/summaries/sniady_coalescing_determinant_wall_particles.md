> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/sniady_coalescing_determinant_wall_particles.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2602.20043 | converted from PDF -->

## What it claims

Abstract. When identical particles on a line collide, they merge and continue
as one. Exact determinantal formulas have long been available for particles
conditioned never to collide, but collisions change the number of particles, and
exact distributions for the survivors have been obtained only in specific settings
and by ad hoc methods. Building on the coalescence determinant introduced in a
companion paper, we study the wall-particle system: when every site is initially
occupied, this is the joint system of survivors and the boundaries between their
basins of attraction. Its finite-dimensional distributions are determinants of
block matrices built from transition probabilities and their cumulative sums; a
finite block matrix suffices even when the initial configuration is infinite. As
applications, we recover the Rayleigh spacing density and the joint distribution
of consecutive gaps—which are negatively correlated—by new methods, and
give a new derivation of the determinantal formula for the joint CDF of finitely
many coalescing particles starting from fixed positions. All…

1.…

## Statements it makes

Theorem 1.1 (Wall-particle correlation function). Consider a coalescing skip-free
process on Z with every site initially occupied. The probability that (X, Y) contains

Theorem 1.2 (Discrete gap intensity measure). Let Ps(n) denote the transition
probability of a translation-invariant skip-free process on Z (from 0 to n in time s),
and suppose the process is symmetric: Ps(n) = Ps(−n). Start with every site
occupied.
The gap intensity measure—the expected number of gaps of size g per unit length—
is
 µ({g}) = P2T (g − 1) − P2T (g + 1), g = 1, 2, 3, . . .

Theorem 1.3 (Single gap intensity measure). Under the maximal entrance law,
the gap intensity measure in rescaled coordinates (G = gap/√T ) has density

Theorem 1.4 (Joint gap intensity). For two consecutive gaps G1 and G2, the joint
gap intensity h(G1, G2) is given by an explicit integral formula (Theorem 5.4). The
marginal intensities are each Rayleigh(√2), but the gaps are negatively correlated
(ρ ≈ −0.163).

Definition 2.1 (Coalescence matrix). Both rows and columns of the n×n coalescence
matrix ˜M are indexed by {1, . . . , n}. The entry in row i, column j (where j lies in
the lth block, with survivor position yl) is

Theorem 2.2 (Coalescence determinant [Śni26a]). Under the coalescence pattern
n1 + · · · + nk = n, the joint probability of survivor positions at y1 < · · · < yk is
det( ˜M ).

Theorem 3.2 (Wall-particle correlation function). Consider a coalescing skip-free
process on Z with every site initially occupied. For positions x1/2 < · · · < xk−1/2 and
y0 < · · · < yk, the probability that (X, Y) contains the consecutive pattern

Corollary 3.4 (Block structure of ˜M ). The matrix ˜M from Theorem 3.2 for
a pattern with k walls has a column structure 1+2+ · · · +2+1: the first and last
columns are single P columns (one for each boundary survivor), and each interior
survivor contributes a 2 × 2 block Bi,j. See Figure 4 for the k = 3 case, where the
block structure and the staircase pattern are fully apparent.

Theorem 3.9 (Multi-pattern correlation function). Consider m separated consecu-
tive patterns in the wall-particle system. Pattern α (α = 1, . . . , m) consists of kα
walls and kα + 1 survivors:

Proposition 4.1 (Grid refinement). For coalescing Brownian motions starting
from a grid with spacing ε, the wall-particle correlation function for k walls near
x1/2, . . . , xk−1/2 and k + 1 survivors near y0, . . . , yk equals ε
k det(M0) + O(εk+1),
where M0 is the 2k × 2k matrix with alternating density and derivative rows and
the column structure of ˜M . Each wall contributes one factor of ε.

Theorem 4.3 (Wall-particle intensity). Under the maximal entrance law for coa-
lescing Brownian motions at time T > 0, the consecutive pattern

Theorem 4.4 (Half-line intensity). Under the maximal entrance law for reflected
Brownian motion on [0, ∞) at time T > 0, the pattern

Theorem 5.1 (Discrete…


*[further statements in the full text]*

*[digest of a 56811 character source; every section, statement, and proof in full at `research/sources/sniady_coalescing_determinant_wall_particles.full.md`]*
