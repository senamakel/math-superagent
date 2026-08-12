<!-- source: https://arxiv.org/pdf/2602.20043 | converted from PDF -->

COALESCING RANDOM WALKS
VIA THE COALESCENCE DETERMINANT

PIOTR ŚNIADY

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
many coalescing particles starting from fixed positions. All formulas hold for
arbitrary nearest-neighbor random walks and their Brownian scaling limits,
with no specific transition kernels required.

1. Introduction

1.1. Coalescing particles. When identical particles on a line collide, they merge
and continue as one (Figure 1). This coalescence rule appears in several areas
of probability and mathematical physics. In the voter model [HL75], boundaries
between opinion clusters perform coalescing random walks; their dynamics controls
the approach to consensus. In reaction-diffusion theory (A + A → A), diffusing
particles that merge on contact display anomalous kinetics: the density in one
dimension decays as n(t) ∼ t
−1/2, slower than the mean-field prediction, because
spatial correlations dominate at large times [DA88].
Arratia [Arr79] placed the infinite system on rigorous footing. Starting coalescing
Brownian motions from every point of R, he showed that the surviving population
is locally finite at any positive time: the system “comes down from infinity.”

1.2. The coalescence determinant. The Karlin–McGregor theorem [KM59] gives
exact determinantal formulas for particles that avoid collision. By contrast, exact
formulas for coalescing particles have been obtained only in specific settings and by
ad hoc methods. The difficulty is that collisions change the number of particles, so
the square matrices of Karlin–McGregor do not directly apply.

2020 Mathematics Subject Classification. Primary 60K35; Secondary 60J65, 15A15.
Key words and phrases. coalescing random walks, coalescing Brownian motions, coalescence
determinant, wall-particle system, skip-free process, basin boundaries, gap distribution, Rayleigh
distribution, determinantal formula.
 1arXiv:2602.20043v2  [math.PR]  9 Mar 2026
2 PIOTR ŚNIADYtime
Figure 1. Coalescing random walks starting from every site of a
lattice segment. Paths merge on contact; the surviving population
thins over time.

1.2.1. The formula. The companion paper [Śni26a, Section Integrating out the
ghosts] introduces the coalescing counterpart: the coalescence determinant. Given
a coalescence pattern—which of the n initial particles merge into each survivor—
the coalescence determinant gives the joint distribution of survivor positions as
the determinant of an n × n matrix built from transition probabilities and their
cumulative sums (Section 2 recalls the precise definition).
Much of the power of the original Karlin–McGregor theorem comes from the
weakness of its assumptions: the Markov property and skip-free trajectories (tran-
sitions only to neighboring states, so that particles cannot change order without
first meeting [KM59]). No symmetry and no specific transition kernels are needed.
The coalescence determinant operates under exactly the same assumptions, and
therefore applies wherever Karlin–McGregor does: we work with coalescing skip-free
random walks on Z and their Brownian scaling limits on R.
Concurrently and independently, Urbán [Urb25] proved the same formula for
binary coalescence of Pólya walks—a special case, since Pólya walks are birth-
and-death chains. His proof reaches the determinant from the opposite direction,
starting from Karlin–McGregor for non-colliding walks and handling coalescence
via a total-probability decomposition; see [Śni26a] for a detailed comparison.

1.2.2. This paper. This paper explores what the coalescence determinant yields
for general skip-free processes. A companion paper [Śni26b] proves that the wall
process carries a natural Pfaffian structure (for any skip-free process), derives
explicit cumulants and a central limit theorem for the wall count, and transfers
these results to surviving particles via checkerboard duality. Under the maximal
entrance law (every site initially occupied), we study the wall-particle system:
the joint system of survivors and the walls between their basins of attraction.
The coalescence determinant yields the finite-dimensional marginals of this system
in closed form (Theorem 1.1); gap distributions follow by marginalizing over wall

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 3

· · · · · ·

· · · · · ·time
t = 0

t > 0

0x−1/2 x1/2 x3/2

y−1 y0 y1 y2

basin of y−1 basin of y0 basin of y1 basin of y2

Figure 2. The (X, Y) system for coalescing random walks. Paths
coalesce on meeting; line weight increases with each merger. Bot-
tom: walls X = (. . . , x−1/2, x1/2, x3/2, . . .) (triangles) partition the
initial line, with x−1/2 < 0 ≤ x1/2. Top: survivor positions
Y = (. . . , y−1, y0, y1, y2, . . .) (circles), one per basin.

positions. Separately, for any finite initial configuration, the coalescence determinant
gives Warren’s determinantal CDF formula for survivor positions (Theorem 6.1).

1.3. The wall-particle system.

1.3.1. The construction. We work under the maximal entrance law: every site of Z
is initially occupied (for Brownian motion, every point of R). Each surviving particle
then owns a basin: the contiguous set of initial positions whose particles merged into
it. The basins partition the initial configuration, and their boundaries are the walls.
The joint system of wall positions X and survivor positions Y—the wall-particle
system (Section 3; see Figure 2)—pairs each survivor with its walls.
Previous work has studied the two marginals separately. Arratia [Arr79] identified
the walls (his “partition points”): the points separating groups of initial positions
that merge into the same survivor. For Brownian motion, he proved X d
= Y via a
time-reversal duality—but this distributional identity requires specific symmetry of
the underlying process. Fomichov [Fom16] computed the joint distribution of one
wall position and two cluster values for the Arratia flow, using Karlin–McGregor
determinants; he noted that this approach cannot recover the full joint distribution
for three or more clusters. The wall-particle correlation function (Theorem 1.1)
generalizes Fomichov’s computation from k = 2 clusters to arbitrary k, and from
the Arratia flow to any skip-free process.

1.3.2. Correlation function. The coalescence determinant gives the finite-dimensional
marginals of (X, Y) in closed form.

Theorem 1.1 (Wall-particle correlation function). Consider a coalescing skip-free
process on Z with every site initially occupied. The probability that (X, Y) contains

4 PIOTR ŚNIADY

the consecutive pattern
 y0 ↖ x1/2 ↗ y1 ↖ · · · ↖ xk−1/2 ↗ yk

(walls at x1/2, . . . , xk−1/2 flanked by survivors at y0, . . . , yk) equals det( ˜M ), where ˜M
is the 2k × 2k block matrix described in Section 3.2.

The formula holds for any skip-free process—no symmetry of the transition prob-
abilities and no specific kernels are needed. Despite the infinite initial configuration
(every site occupied), k consecutive wall-particle pairs depend only on a 2k × 2k
block matrix; the rest of the infinite system does not enter the formula.

1.4. Gap distributions. Marginalizing the correlation function over wall posi-
tions gives the joint distribution of consecutive gaps between survivors. Gap
distributions for coalescing Brownian motions were first studied by Doering and
ben-Avraham [DA88] via the inter-particle distribution function (IPDF) method:
the rescaled nearest-neighbor distance density converges to x e
−cx2, a Rayleigh
form. Ben-Avraham [Avr98] extended the method to derive the full hierarchy of
empty-interval probabilities; ben-Avraham and Brunet [AB05] extracted explicit
densities for two and three consecutive spacings. These formulas use the explicit
transition kernel of Brownian motion. In the asymptotic regime, FitzGerald, Tribe,
and Zaboronski [FTZ20; FTZ22] computed gap exponents and persistence expo-
nents via Fredholm Pfaffian methods, rigorously confirming predictions of Derrida
and Zeitak. For counting statistics, Glinyanaya and Fomichov [GF17] proved a
central limit theorem for the number of surviving clusters in the Arratia flow, with
Fano factor 3 − 2
√2 ≈ 0.172, reflecting the sub-Poissonian correlations induced by
coalescence.

1.4.1. Discrete gap formula. In the discrete setting, no limiting procedure is needed.

Theorem 1.2 (Discrete gap intensity measure). Let Ps(n) denote the transition
probability of a translation-invariant skip-free process on Z (from 0 to n in time s),
and suppose the process is symmetric: Ps(n) = Ps(−n). Start with every site
occupied.
The gap intensity measure—the expected number of gaps of size g per unit length—
is
 µ({g}) = P2T (g − 1) − P2T (g + 1), g = 1, 2, 3, . . .

The total intensity ∑

g µ({g}) = P2T (0) + P2T (1)

is the survivor density per site; dividing by it recovers the gap probability mass
function (Theorem 5.1).

This formula holds for any symmetric skip-free process: simple random walk,
lazy random walk, or any birth-death chain with symmetric rates. The only inputs
are transition probabilities at doubled time—no PDEs, no passage to a continuous
limit. For non-symmetric processes, the gap intensity is a convolution of transition
probabilities at the original time (Section 5.1.1).

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 5

1.4.2. Brownian gaps: the Rayleigh distribution. Passing to Brownian motion, the
discrete formula becomes a continuous density.

Theorem 1.3 (Single gap intensity measure). Under the maximal entrance law,
the gap intensity measure in rescaled coordinates (G = gap/√T ) has density

µ(dG) = G
2√π e−G
2/4 dG, G > 0.

The total intensity ∫ ∞

0 µ(dG) = 1
√π

gives the rescaled survivor density; un-rescaling yields density n(T ) = 1/
√πT .
Normalizing to a probability distribution gives Rayleigh(
√2).

This recovers the Rayleigh law of Doering and ben-Avraham [DA88] by new
methods (Section 5.1). In Section 5.1.2 we sketch how the discrete formula from
Theorem 1.2 converges to this density under diffusive scaling.

1.4.3. Joint gap distribution. The single-gap Rayleigh law determines the marginal
distribution but says nothing about correlations between neighboring gaps.

Theorem 1.4 (Joint gap intensity). For two consecutive gaps G1 and G2, the joint
gap intensity h(G1, G2) is given by an explicit integral formula (Theorem 5.4). The
marginal intensities are each Rayleigh(√2), but the gaps are negatively correlated
(ρ ≈ −0.163).

The joint density of two consecutive spacings was previously obtained by ben-
Avraham and Brunet [AB05] from the IPDF hierarchy; we give an alternative
derivation via a 4 × 4 determinant.

1.5. Warren’s formula. Warren [War07] proved that for finitely many coalescing
Brownian motions, the joint CDF of survivor positions is a determinant of Gaussian
CDFs and their tails. Assiotis, O’Connell, and Warren [AOW19] extended this to
general one-dimensional diffusions, and Assiotis [Ass18; Ass23] to birth-death chains.
Unlike the wall-particle correlation function—which requires the maximal entrance
law (every site occupied)—Warren’s formula applies to any finite configuration
of particles at fixed starting positions. The coalescence determinant yields the
CDF formula for any skip-free process, including discrete-time random walks on Z
(Theorem 6.1): the proof uses only the coalescence determinant and a summation-
by-parts identity.

1.6. Scope. The coalescence determinant and the analytic approaches cover com-
plementary territory. Our formulas apply to any skip-free process with arbitrary
inhomogeneous transition probabilities, but the wall-particle results require the
maximal entrance law and treat only pure coalescence. The spin-pair duality
of [GPTZ18] handles mixed coalescence-annihilation and all deterministic initial
conditions (extended by Tribe and Zaboronski [TZ26] to all entrance laws), but
requires a time-homogeneous Markov generator. For coalescing Brownian motions,
FitzGerald, Tribe, and Zaboronski [FTZ20; FTZ22] derive sharp gap exponents via
Fredholm Pfaffian methods, and Glinyanaya and Fomichov [GF17] prove a CLT
with Berry–Esseen bound—results our approach does not yield.

6 PIOTR ŚNIADY

1.7. Organization. Section 2 recalls the coalescence determinant for arbitrary
patterns. Section 3 develops the wall-particle system and derives its correlation
function for skip-free processes on Z. Specializing to Brownian motion (Section 4),
each pair of flanking sites collapses to a density–derivative pair as the lattice spacing
vanishes, and the maximal entrance law provides translation invariance. Gap
distributions (Section 5) follow by marginalizing the correlation function over wall
positions for k = 1 and k = 2. Warren’s formula (Section 6) is a separate application
of the coalescence determinant: summing over all coalescence patterns converts
density columns to CDF columns.

2. The Coalescence Determinant

We recall the coalescence determinant from [Śni26a], which applies to any finite
collection of coalescing skip-free particles. We state the formula in the discrete
setting; the continuous extension is recalled in Section 4.
Write P (x, y) for the transition probability of the underlying skip-free process
from x to y in time T (with T fixed throughout), and

F (x, y) = ∑

z≤y P (x, z)

for the cumulative sum.
Start n particles at positions x1 < x2 < · · · < xn. A coalescence pattern is an
integer composition n1 + n2 + · · · + nk = n: the first n1 initial particles merge into
survivor 1, the next n2 into survivor 2, and so on. The lth block of the composition—
the initial particles merging into survivor l—has indices n1+ · · · +nl−1+1 through
n1+ · · · +nl. Write y1, . . . , yk for the survivor positions at time T .

Definition 2.1 (Coalescence matrix). Both rows and columns of the n×n coalescence
matrix ˜M are indexed by {1, . . . , n}. The entry in row i, column j (where j lies in
the lth block, with survivor position yl) is

˜Mij =
 {P (xi, yl) if j is the first index in its block,
F (xi, yl) − [i < j] otherwise.

The first column of each block contains transition probabilities P ; the remaining
nl − 1 columns contain cumulative sums F with a staircase shift.

Theorem 2.2 (Coalescence determinant [Śni26a]). Under the coalescence pattern
n1 + · · · + nk = n, the joint probability of survivor positions at y1 < · · · < yk is
det( ˜M ).

The formula above is stated for discrete state spaces. For continuous processes
satisfying the Karlin–McGregor assumptions (such as Brownian motion), transition
probabilities P become densities and cumulative sums F become CDFs; the deter-
minant then gives a probability density rather than a probability mass. See [Śni26a]
for the general statement covering both cases.

Example 2.3 (Pattern 2 + 1). Three particles; the first two merge (survivor y1), the
third survives alone (y2):

˜M =
 


P (x1, y1) F (x1, y1) − 1 P (x1, y2)
P (x2, y1) F (x2, y1) P (x2, y2)
P (x3, y1) F (x3, y1) P (x3, y2)


 .

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 7

3. The Wall-Particle System

3.1. Two coupled sequences. Consider a coalescing skip-free process on Z with
every site initially occupied. When two particles meet, they coalesce and continue
as one. Fix a time T > 0. We call each surviving particle a survivor and write
Y = (yj)j∈Z for the increasing sequence of survivor positions (time-T coordinates),
indexed by the integers.
Each survivor owns a basin: the contiguous set of initial positions whose particles
merged into it. The basins partition Z. Between consecutive basins lies a wall :
the half-integer separating the last initial position in one basin from the first
in the next. Write X = (xi)i∈Z′ for the increasing sequence of walls (time-0
coordinates), where Z
′ = Z + 1
2 . The basin of yj is the set of initial integers in the
interval (xj−1/2, xj+1/2). Throughout, X and Y denote the random sequences, with
components xi and yj. When xi and yj appear without boldface in formulas, they
denote specific (deterministic) positions. See Figure 2 for an illustration.
Because walls live at time 0 and survivors at time T , there is no interlacing
constraint on their values—a survivor need not lie inside its basin. The two
sequences have interleaved indices—half-integers for walls, integers for survivors:

· · · ↖ x1/2 ↗ y1 ↖ x3/2 ↗ y2 ↖ x5 /2 ↗ · · ·

We use this zigzag notation throughout: each arrow connects a wall to an adjacent
survivor in the index order.

Remark 3.1 (Labeling convention). The labeling of walls and survivors is determined
only up to a global shift of the index set. When needed, we fix a reference by
requiring x−1/2 < 0 ≤ x1/2, placing the origin in the basin of y0. This convention
plays no role in the distributional results.

Each wall xi (i ∈ Z
′) is flanked by two initial integer positions:

ai = xi − 1
2 , bi = xi + 1
2 .

Position ai (to the left of the wall) belongs to the basin of survivor yi−1/2, and bi
(to the right) to the basin of survivor yi+1/2.

3.2. Correlation function.

Theorem 3.2 (Wall-particle correlation function). Consider a coalescing skip-free
process on Z with every site initially occupied. For positions x1/2 < · · · < xk−1/2 and
y0 < · · · < yk, the probability that (X, Y) contains the consecutive pattern

y0 ↖ x1/2 ↗ y1 ↖ x3/2 ↗ · · · ↖ xk−1/2 ↗ yk

equals det( ˜M ), where ˜M is the coalescence matrix (Definition 2.1) for 2k particles
started at a1, b1, . . . , ak, bk with coalescence pattern 1+2+ · · · +2+1: particle a1
survives alone at y0; each pair (bl, al+1) merges into survivor yl; and bk survives
alone at yk.

Proof. Consider first only the 2k flanking particles a1, b1, . . . , ak, bk (no other sites
occupied; see Figure 3 for k = 2). The coalescence determinant (Theorem 2.2) gives
the probability of the stated coalescence event as det( ˜M ).
Now populate every remaining integer site. In Arratia’s construction of coalescing
processes [Arr79], additional particles do not alter the trajectories of existing ones:
they follow the same underlying paths and merge into whatever they meet. Because

8 PIOTR ŚNIADY

t = 0

t > 0time
a1 b1 a2 b2

x 1/2 x 3/2

y0 y1 y2
 pair 1 (solid)

pair 2 (zigzag)

survivor (double)

intermediate

Figure 3. Proof of Theorem 3.2 for k = 2. The coalescence determi-
nant applies to the four flanking particles a1, b1, a2, b2 (bold paths:
solid for pair 1, zigzag for pair 2). Particles b1 and a2 coalesce
into survivor y1 (double line); particles a1 and b2 survive as y0
and y2. The intermediate particles (thin gray) cannot cross the
flanking paths—the skip-free property traps them in the closing
funnel between b1 and a2—so they are absorbed into the same
survivors. Adding them does not change the coalescence outcome
for the flanking particles.

the process is skip-free, every intermediate particle (at a site between bl and al+1) is
trapped between the converging paths of bl and al+1 and must coalesce into the same
survivor yl (see Figure 3). The wall-particle event in the full system therefore has
the same probability as the coalescence event for the 2k flanking particles alone. □

3.3. Block structure. We now examine the matrix ˜M from Theorem 3.2 more
closely. The pattern 1+2+ · · · +2+1 gives ˜M a 2 × 2 block structure: each wall
contributes a row-pair and each interior survivor a column-pair (P and F ), while
the two boundary survivors contribute single P columns. Write Bi,j (i ∈ Z′, j ∈ Z)
for the 2 × 2 block at row-pair i (wall) and column-pair j (survivor):

Bi,j =
 (
P (ai, yj) F (ai, yj) − [i < j]
P (bi, yj) F (bi, yj) − [i < j]
)
 ,

where [i < j] is the Iverson bracket.

Example 3.3 (Pattern 1+2+1). For k = 2 (two walls, three survivors), the pattern
y0 ↖ x1/2 ↗ y1 ↖ x3/2 ↗ y2 gives a 4 × 4 matrix with column structure 1+2+1.
The interior survivor y1 contributes a block Bi,j—a P column and an F column
carrying a staircase step—while the boundary survivors y0 and y2 each contribute a
single P column:

˜M =
 





P (a1, y0) P (a1, y1) F (a1, y1) − 1 P (a1, y2)
P (b1, y0) P (b1, y1) F (b1, y1) − 1 P (b1, y2)
P (a2, y0) P (a2, y1) F (a2, y1) P (a2, y2)
P (b2, y0) P (b2, y1) F (b2, y1) P (b2, y2)




 .

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 9

pa1 (y0 ) pa1 (y1) Fa1 (y1)−1 pa1 (y2) Fa1 (y2)−1 pa1 (y3)

pb1 (y0 ) pb1 (y1) Fb1 (y1)−1 pb1 (y2) Fb1 (y2)−1 pb1 (y3)

pa2 (y0 ) pa2 (y1) Fa2 (y1) pa2 (y2) Fa2 (y2)−1 pa2 (y3)

pb2 (y0 ) pb2 (y1) Fb2 (y1) pb2 (y2) Fb2 (y2)−1 pb2 (y3)

pa3 (y0 ) pa3 (y1) Fa3 (y1) pa3 (y2) Fa3 (y2) pa3 (y3)

pb3 (y0 ) pb3 (y1) Fb3 (y1) pb3 (y2) Fb3 (y2) pb3 (y3)

a1

b1

a2

b2

a3

b3

pair 1

pair 2

pair 3
 y0 y1 y2 y3

2×1 2×2 2×2 2×1

transition prob. p cumul. sum F cumul. sum F −1

Figure 4. Block structure of ˜M for the 1+2+2+1 pattern (k = 3
walls). Rows come in pairs; columns are grouped by survivor:
2 × 1 boundary blocks for y0 and y3, and 2 × 2 interior blocks
for y1 and y2, each containing a P column and an F column. The
thick red staircase separates F −1 blocks (dark blue, solid hatching)
from F blocks (orange, dashed hatching); unhatched yellow blocks
contain only P entries.

For the boundary case k = 1 (one wall, no interior survivors, no coalescence at
all), there are no blocks Bi,j and the matrix reduces to the 2 × 2 Karlin–McGregor
determinant [KM59].

Corollary 3.4 (Block structure of ˜M ). The matrix ˜M from Theorem 3.2 for
a pattern with k walls has a column structure 1+2+ · · · +2+1: the first and last
columns are single P columns (one for each boundary survivor), and each interior
survivor contributes a 2 × 2 block Bi,j. See Figure 4 for the k = 3 case, where the
block structure and the staircase pattern are fully apparent.

Remark 3.5 (Staircase and block structure). The block formula for Bi,j uses the
Iverson bracket [i < j], which steps at block boundaries. The coalescence matrix
(Definition 2.1), however, defines the staircase at the level of individual rows. For

10 PIOTR ŚNIADY

the wall-particle patterns 1+2+ · · · +2+1, each staircase step falls between the
two rows of a single block, so the two conventions agree on all F columns (where
the distinction matters) and may differ only on P columns—but P entries do not
depend on the staircase. Warren’s formula (Section 6), however, sums over all 2
n−1

coalescence patterns and requires the original row-level staircase.

Remark 3.6 (Asymmetry between walls and survivors). The block matrix ˜M treats
walls and survivors asymmetrically: the pattern has k walls but k + 1 survivors, and
the two boundary survivors each contribute only one column (rather than two), so
walls and survivors cannot simply be interchanged. When the underlying process has
a checkerboard structure—such as discrete-time ±1 random walk—this asymmetry
can be resolved: a decomposition of the lattice gives a duality between walls and
survivors, connecting the wall-particle system to Pfaffian point processes. This is
developed in [Śni26b].

3.4. Examples. We describe two classes of processes satisfying the skip-free as-
sumption of Theorem 3.2.

Example 3.7 (Simple symmetric random walk). Consider the ±1 simple random walk:
at each discrete time step, every particle moves left or right with equal probability.
Space-time splits into two checkerboard sublattices: a particle at position x at
time t satisfies either x + t ≡ 0 or x + t ≡ 1 (mod 2), and each particle stays on
one sublattice forever. If we start particles at every site of Z, the Karlin–McGregor
assumptions fail: a particle starting at an even site and a particle starting at an
odd site live on complementary sublattices and can exchange order without ever
sharing a site, so the non-crossing property does not hold.
The remedy is to occupy a single sublattice—say all even sites 2Z at time 0.
Particles on the same sublattice cannot cross without meeting (they share the
same parity at every time step), so the skip-free assumption holds. Applying the
framework to the initial sublattice 2Z (with spacing 2 playing the role of the unit
lattice), walls sit at the odd integers 2Z + 1. At time T , all survivors share the same
parity, so all gaps between consecutive survivors are even (see Theorem 5.1 for the
gap distribution).

Example 3.8 (Birth-death chains). Continuous-time birth-death chains on the non-
negative integers are skip-free by construction (only ±1 transitions), and every
integer is a valid state at every time—no parity constraint. The wall-particle
framework applies directly, with walls at { 1
2 , 3
2 , . . .}. For instance, the M/M/1 queue
has transition probabilities expressible via modified Bessel functions [KM59].

3.5. Multi-pattern correlations. Theorem 3.2 extends to several separated consec-
utive patterns observed simultaneously, with an unspecified number of intermediate
survivors between them. We state this for completeness; it is not used in the present
paper.

Theorem 3.9 (Multi-pattern correlation function). Consider m separated consecu-
tive patterns in the wall-particle system. Pattern α (α = 1, . . . , m) consists of kα
walls and kα + 1 survivors:

y(α)
0 ↖ x
(α)
1/2 ↗ y(α)
1 ↖ · · · ↖ x
(α)
kα −1/2 ↗ y(α)
kα ,

with walls and survivors each globally increasing. Between consecutive patterns, the
number of intermediate survivors is unspecified.

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 11

The probability that (X, Y) contains all m patterns simultaneously equals det( ˜M ),
where ˜M is the coalescence matrix (Definition 2.1) for the 2K flanking particles
(K = ∑
α kα). Within each pattern, the coalescence is as in Theorem 3.2; between
consecutive patterns, the boundary particles survive alone.

Proof. Apply the coalescence determinant (Theorem 2.2) to the 2K flanking po-
sitions. Within each pattern, the argument is identical to Theorem 3.2. Between
patterns, intermediate particles are trapped between the last flanking particle of
one pattern and the first of the next, so populating them does not change the
probability. □

Example 3.10 (Two separated patterns). Consider m = 2 patterns: pattern 1 with
k1 = 2 (walls x1/2, x3/2, flanking positions a1, b1, a2, b2, survivors y0, y1, y2) and
pattern 2 with k2 = 1 (wall x5 /2, flanking positions a3, b3, survivors y3, y4), with an
unspecified number of intermediate survivors between y2 and y3. The 6 × 6 matrix
is:
 ˜M =
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




 y0 y1 y2 y3 y4

a1 P P F −1 P P P

b1 P P F −1 P P P

a2 P P F P P P

b2 P P F P P P

a3 P P F P P P
b3 P P F P P P
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




 .

Here P denotes a transition probability entry P (al, yj) or P (bl, yj), and F , F −1
denote cumulative sum entries F (·, y1) or F (·, y1) − 1.
The double lines mark the pattern boundary. Within pattern 1 (upper-left 4 × 4
block), the structure is the familiar 1+2+1 from Example 3.3: the interior survivor y1
has an F column, with the staircase separating F −1 (wall 1, above) from F (walls 2
and 3, below). Pattern 2 (lower-right 2 × 2 block) is pure Karlin–McGregor.
The off-diagonal blocks couple the two patterns; their entries are all P . No
F column appears between y2 and y3: this absence is what allows an arbitrary
number of unspecified intermediate survivors between the two patterns. Compare
Figure 4, where the single pattern 1+2+2+1 has F columns for every interior
survivor.
 4. Brownian Motion Setting

We specialize the block matrix ˜M (Corollary 3.4) to Brownian motion. In the con-
tinuous limit, each flanking pair (al, bl) collapses to a single wall position; subtracting
the two rows of each block and dividing by the grid spacing turns the row pair into
a Gaussian density and its spatial derivative. The resulting 2k × 2k matrix M0 is
explicit. We then pass to the maximal entrance law—coalescing Brownian motions
starting from all of R, a classical construction due to Arratia [Arr79]—and obtain a
determinantal formula for the intensity of the wall-particle system.

12 PIOTR ŚNIADY

4.1. Transition densities. Write px(y) for the Gaussian transition density at
time T (fixed throughout):

px(y) = 1
√2πT exp
(− (y − x)2

2T
 ) ,

and Fx(y) for the Gaussian CDF:

Fx(y) = ∫ y

−∞ px(z) dz = Φ
( y − x
√T
 ) ,

where Φ is the standard normal CDF.
Start coalescing Brownian motions from a grid with spacing ε. Each wall is
flanked by starting positions al and bl = al + ε. The coalescence determinant
(Theorem 2.2) gives a 2k × 2k matrix as in Section 3.2, with Brownian densities
px(y) and CDFs Fx(y) in place of P (x, y) and F (x, y).
Subtracting the al row from the bl row within each pair (which preserves the
determinant) and dividing by ε replaces the second row by the derivative ∂x, up to
O(ε) error. Each 2 × 2 interior block becomes:
( px(y) Fx(y) − [·]
∂xpx(y) ∂xFx(y)
 )
 + O(ε),

where [·] stands for the Iverson bracket as in Bi,j (Section 3.3). The boundary
columns (containing only p entries) undergo the same row operation, becoming
(px(y), ∂xpx(y))
T . Each row-pair contributes one factor of ε.

Proposition 4.1 (Grid refinement). For coalescing Brownian motions starting
from a grid with spacing ε, the wall-particle correlation function for k walls near
x1/2, . . . , xk−1/2 and k + 1 survivors near y0, . . . , yk equals ε
k det(M0) + O(εk+1),
where M0 is the 2k × 2k matrix with alternating density and derivative rows and
the column structure of ˜M . Each wall contributes one factor of ε.

Proof. The row operations above give det( ˜M ) = ε
k det(M0) + O(εk+1). □

Remark 4.2 (Wronskian structure). For translation-invariant kernels px(y) = p(y −
x), ∂xpx(y) = −∂ypx(y), ∂xFx(y) = −px(y).
Thus the derivative row of each block in M0 is −∂y applied to the density row, giving
a generalized Wronskian in the CDF Fx evaluated at y. This structure matches
the Tribe–Zaboronski kernel for coalescing Brownian motions [TZ11; GPTZ18]; the
connection is explored in [Śni26b].

4.2. Maximal entrance law. Arratia [Arr79] constructs coalescing Brownian
motions starting from all of R via dyadic approximation and proves that the set of
survivors is locally finite. We use the same construction to build the joint (X, Y)
system.
Fix a time T > 0. At step n = 0, 1, 2, . . ., start independent Brownian motions
from every point of 2
−nZ at time 0, and run them until time T with the coalescing
rule: when two trajectories meet, they merge and continue as one.
The construction is incremental. Going from step n to step n+1, the new starting
points 2
−n−1(2Z + 1) interleave the existing ones from 2
−nZ. Each newly launched
Brownian motion either hits an existing trajectory before time T and is absorbed,
or survives to time T without hitting any existing trajectory. The set of survivors

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 13

grows monotonically with n: existing survivors are never removed. The limiting set
is locally finite: two Brownian motions distance ε apart fail to coalesce by time T
with probability ε/√πT + O(ε2) (this is Arratia’s estimate [Arr79]; it also follows
from Proposition 4.1 with k = 1), so the expected number of survivors per unit
length remains bounded as the grid refines.
The construction produces the (X, Y) system from Section 3: the wall sequence
X = (xi) and the survivor sequence Y = (yj) (positions at time T ), with basins
partitioning R. The maximal entrance law inherits translation invariance from the
dyadic grid: the shifts by 2−n become dense as n → ∞, so the joint law of (X, Y)
is invariant under all translations of R.

4.3. Wall-particle intensity. A consecutive pattern with k walls and k+1 survivors
lives in R2k+1 (k wall coordinates plus k + 1 survivor coordinates), and the wall-
particle system under the maximal entrance law forms a point process on this space.
Its intensity is the density of the point process with respect to Lebesgue measure:
integrating over a region gives the expected number of patterns in that region.
Combining the grid-refinement limit (Proposition 4.1) with the dyadic construction
gives this intensity in closed form.

Theorem 4.3 (Wall-particle intensity). Under the maximal entrance law for coa-
lescing Brownian motions at time T > 0, the consecutive pattern

y0 ↖ x1/2 ↗ y1 ↖ · · · ↖ xk−1/2 ↗ yk

has intensity det
(M0(x1/2, . . . , xk−1/2; y0, . . . , yk)
)

with respect to Lebesgue measure on R2k+1, where M0 is the 2k × 2k matrix from
Proposition 4.1.

Proof. At dyadic step n, the starting grid has spacing ε = 2
−n. By Proposition 4.1,
the wall-particle correlation function for k walls near x1/2, . . . , xk−1/2 and survivors
near y0, . . . , yk is εk det(M0) + O(εk+1). Each factor of ε matches the grid spacing
per wall, so det(M0) is the density per unit length in each wall coordinate. Since
the survivor set is locally finite [Arr79] and grows monotonically with each dyadic
refinement, it almost surely stabilizes on any bounded interval after finitely many
steps. Passing to n → ∞ gives the result. □

4.4. Example: reflected Brownian motion. The grid-refinement technique of
Section 4.1 extends naturally to any process with continuous paths and a smooth
transition density. As an illustration beyond standard Brownian motion, we treat
coalescing Brownian motions on the half-line [0, ∞) with reflection at 0. Translation
invariance is lost, and the reflecting boundary introduces a leftmost survivor with a
special role.
Reflected Brownian motion on [0, ∞) has transition density

px(y) = 1
√2πT
 [
e−(y−x)
2/(2T ) + e−(y+x)
2/(2T )] , x, y ≥ 0.

This is skip-free (continuous paths), so the coalescence determinant applies. The
maximal entrance law occupies all of [0, ∞); translation invariance is broken by the
boundary at 0.

14 PIOTR ŚNIADY

The set of survivors is half-infinite: there is a leftmost survivor y0, with basin
[0, x1/2) bounded on the left by the reflecting boundary. We write

y0 ↖ x1/2 ↗ y1 ↖ x3/2 ↗ y2 ↖ · · ·

for the wall-particle system, with walls 0 < x1/2 < x3/2 < · · · and survivors
0 < y0 < y1 < y2 < · · · .

Theorem 4.4 (Half-line intensity). Under the maximal entrance law for reflected
Brownian motion on [0, ∞) at time T > 0, the pattern

y0 ↖ x1/2 ↗ y1 ↖ · · · ↖ xk−1/2 ↗ yk

with y0 the leftmost survivor has intensity

det
(M0(x1/2, . . . , xk−1/2; y0, . . . , yk)
)

with respect to Lebesgue measure on (0, ∞)2k+1. Here M0 is a (2k+1) × (2k+1)
matrix: its first row comes from a particle at the boundary 0, and its remaining
k row-pairs are the density and ∂x-derivative rows from the k walls. Columns are
organized as in the coalescence pattern 2+2+ · · · +2+1: a P -and-F column-pair for
each group of size 2, and a single P column for the final group of size 1.

Proof. Construct the maximal entrance law on [0, ∞) by dyadic approximation,
as in Section 4.2: at step n, start reflected Brownian motions from every point of
{0, 2
−n, 2 · 2−n, . . .}.
At grid spacing ε = 2−n, the particle at 0 and the 2k flanking particles
a1, b1, . . . , ak, bk form a system of 2k + 1 particles. The coalescence determinant
(Theorem 2.2) gives their joint distribution under the pattern 2+2+ · · · +2+1: the
particle at 0 and a1 merge into y0; each pair (bl, al+1) merges into yl; and bk survives
alone at yk. Intermediate particles are trapped by the skip-free property (as in
Theorem 3.2): between 0 and a1, the reflecting boundary prevents leftward escape;
between bl and al+1, the closing funnel absorbs all intermediate particles.
The grid-refinement procedure (Proposition 4.1) carries over: each (al, bl) pair
collapses to a density row and a ∂x-derivative row, contributing one factor of ε; the
particle at 0 contributes a single row. Thus

det( ˜M ) = ε
k det(M0) + O(εk+1).

Since the survivor set is locally finite [Arr79] and grows monotonically, it stabilizes
on any bounded interval after finitely many steps. Passing to n → ∞ gives the
intensity det(M0). □

Example 4.5 (One wall on the half-line). For k = 1 (one wall, two survivors, leftmost
survivor at y0), the pattern 2+1 gives the 3 × 3 matrix

M0 =
 



 p0(y0) F0(y0) − 1 p0(y1)
px1/2 (y0) Fx1/2 (y0) px1/2 (y1)
∂xpx1/2 (y0) ∂xFx1/2 (y0) ∂xpx1/2 (y1)




 ,

where px(y) and Fx(y) use the reflected Brownian motion transition density.

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 15

5. Gap Distributions

We compute gap distributions in the discrete setting (where no limiting procedure
is needed) and for Brownian motion under the maximal entrance law. All results
are stated in terms of the gap intensity measure: µ({g}) is the expected number
of gaps of size g per unit length. Dividing by the total intensity ∑

g µ({g}) (the
survivor density) recovers the gap probability distribution.

5.1. Single gap. We derive the single-gap intensity measure, first in the discrete
setting (where the formula is exact) and then for Brownian motion under the maximal
entrance law. The Brownian result recovers the Rayleigh law (see Section 1.4 for
prior work); we give a new proof through the wall-particle system.

5.1.1. Discrete single-gap distribution. Apply the wall-particle system with k = 1: a
single wall at half-integer x separates two basins, with flanking sites a = x − 1
2 and
b = x + 1
2 (so b = a + 1). The two survivors y0 < y1 satisfy the Karlin–McGregor
non-intersection condition, and the coalescence determinant gives:

det( ˜M ) = P (a, y0) P (b, y1) − P (a, y1) P (b, y0).

Summing the wall-particle intensity over all wall positions gives the probability that
y0 and y1 are consecutive survivors:
(5.1)
P(y0, y1 consecutive survivors) = ∑

a∈Z
[
P (a, y0) P (a+1, y1) − P (a, y1) P (a+1, y0)
]
.

This formula is valid for any skip-free process with every site initially occupied: no
translation invariance or symmetry is needed.

Translation-invariant case. Assume P (x, y) = P (0, y − x) for all x, y ∈ Z; we
write P (n) = P (0, n) when the time T is understood. Writing g = y1 − y0 for the
gap, translation invariance gives P (a, y0) = P (y0 − a), P (a+1, y1) = P (y1 − a − 1),
and so on; each summand in (5.1) depends only on g and a − y0, so the sum is
independent of y0. Define the autocorrelation

R(m) = ∑

s∈Z PT (s) PT (s + m).

Then the two sums in (5.1) are R(g − 1) and R(g + 1) respectively, giving

(5.2) µ({g}) = R(g − 1) − R(g + 1).

Symmetric case. When the walk is symmetric (P (n) = P (−n) for all n), the
autocorrelation reduces to a convolution: R(m) = ∑
s P (s) P (m − s) = P2T (m)
by the Chapman–Kolmogorov identity, so µ({g}) = P2T (g − 1) − P2T (g + 1). The
continuous-time simple random walk (±1 jumps, each at rate 1) is the main example:
every integer is reachable from every integer, so there is no parity constraint.

Theorem 5.1 (Discrete gap intensity measure). For a symmetric translation-
invariant coalescing skip-free process on Z with every site initially occupied, the gap
intensity measure is

µ({g}) = P2T (g − 1) − P2T (g + 1), g = 1, 2, 3, . . .

16 PIOTR ŚNIADY

The total intensity is a telescoping sum:

∞∑

g=1 µ({g}) = P2T (0) + P2T (1),

since P2T (g) → 0 as g → ∞; this gives the survivor density per site. Dividing by the
total intensity recovers the probability mass function P(G = g) = µ({g})/[P2T (0) +
P2T (1)].

Proof. Equation (5.2) gives µ({g}). For the total intensity, the partial sum

N∑

g=1
[P2T (g − 1) − P2T (g + 1)] = P2T (0) + P2T (1) − P2T (N ) − P2T (N + 1)

telescopes (reindex: the first sum runs over m = 0, . . . , N − 1 and the second over
m = 2, . . . , N + 1). Letting N → ∞ gives total intensity P2T (0) + P2T (1). □

5.1.2. Scaling limit preview. Under diffusive scaling, the discrete gap distribution
from Theorem 5.1 recovers the Brownian motion Rayleigh density from Theorem 1.3.
The scaling sends:
• lattice spacing ε → 0;
• discrete gap g ∈ Z to continuous gap G = g · ε (measured in the rescaled
coordinates);
• discrete time t to continuous time with ε
2t held fixed.
In this regime, the transition probability P2t(n) at the integer n = (g ± 1) is well
approximated by the Gaussian density p(nε, 2ε2t) times the lattice spacing ε. The
difference at unit spacing becomes a derivative:

P2t(g − 1) − P2t(g + 1) ≈ −2ε
2 ∂G p(G, 2T )∣
∣
∣
∣G=gε, T =ε2t,

and since ∂G p(G, 2T ) = − G
2T p(G, 2T ), this gives

µ(dG) ∝ G e−G
2/(4T ) dG,

the gap intensity measure, identifying the Rayleigh(
√2) family.
This argument is a scaling heuristic, not a rigorous proof: a complete deriva-
tion requires controlling the error terms in the Gaussian approximation and the
convergence of the normalizing constants. The rigorous Brownian motion proof
follows.

5.2. Brownian motion single gap. We prove Theorem 1.3 by applying the (X, Y)
framework from Section 3 (with the Brownian motion specialization from Section 4.1)
with k = 1 and passing to the maximal entrance law (Section 4.2).
We recall the Rayleigh distribution with scale parameter σ > 0:

Rayleigh(σ) : fσ(G) = G
σ2 e−G
2/(2σ2), G > 0.

The mean is σ√π/2 and the variance is (4 − π)σ2/2.

Theorem 5.2 (Gap intensity measure under the maximal entrance law). Under the
maximal entrance law, the gap intensity measure in rescaled coordinates has density

µ(dG) = G
2
√π e−G
2/4 dG, G > 0.

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 17

Normalizing to a probability distribution gives the Rayleigh(√2) density f (G) =
G
2 e−G
2/4.

Corollary 5.3 (Density of surviving particles). The total intensity is ∫ ∞
0 µ(dG) =
1/
√π, giving the rescaled survivor density. Since the rescaled mean gap is E[G] = √π,
the mean gap between consecutive survivors at time T is √πT , and the density of
survivors per unit length is 1/√πT .

Proof of Theorem 5.2. By Theorem 4.3 with k = 1, the intensity of the pattern
y0 ↖ x ↗ y1 is det(M0), where

M0 = ( px(y0) px(y1)
∂xpx(y0) ∂xpx(y1)
) .

Using ∂xpx(y) = px(y) · (y − x)/T , the determinant is:

det(M0) = px(y0) px(y1) · y1 − y0
T .

Change coordinates: let u = y0 − x (displacement of left survivor from wall
position) and G = y1 − y0 (gap). Then px(y0) = (2πT )−1/2e−u
2/(2T ) and px(y1) =
(2πT )
−1/2e−(u+G)2/(2T ), so

det(M0) = G
2πT 2 exp(− u
2 + (u + G)
2

2T
 ) .

Completing the square: u2 + (u + G)
2 = 2(u + G/2)2 + G2/2. Integrating over u:
∫ ∞

−∞ det(M0) du = G
2πT 2 e−G
2/(4T )√πT = G
2√π T 3/2 e−G
2/(4T ).

By translation invariance, this is independent of the location y0, so it gives the
gap intensity per unit (unrescaled) length. Changing to rescaled coordinates G =
(y1 − y0)/√T , the gap intensity per unit rescaled length becomes

µ(dG) = G
2
√π e−G2/4 dG,

which is 1/
√π times the Rayleigh(
√2) density. □

5.3. Joint distribution of consecutive gaps. We derive the joint intensity of
two consecutive gaps, first in the discrete setting and then for Brownian motion,
proving Theorem 1.4. The Brownian joint density was previously obtained by
ben-Avraham and Brunet [AB05] from the IPDF hierarchy; our derivation via the
wall-particle system applies to any skip-free process, including discrete random walks
and birth-death chains.

5.3.1. Discrete joint gaps. For k = 2 consecutive gaps, the 1+2+1 pattern from
Example 3.3 gives a 4 × 4 determinant. As in the single-gap case (Section 5.1.1),
summing the wall-particle intensity over all wall positions gives the probability that
y0, y1, y2 are consecutive survivors:

P(y0, y1, y2 consecutive survivors) = ∑

a1,a2∈Z det( ˜M ),

18 PIOTR ŚNIADY

where al, bl = al + 1 are the flanking sites of wall l, and ˜M is the 4 × 4 matrix

˜M =
 




 P (a1, y0) P (a1, y1) F (a1, y1) − 1 P (a1, y2)
P (b1, y0) P (b1, y1) F (b1, y1) − 1 P (b1, y2)
P (a2, y0) P (a2, y1) F (a2, y1) P (a2, y2)
P (b2, y0) P (b2, y1) F (b2, y1) P (b2, y2)
 



 .

By translation invariance, the sum depends only on the gaps g1 = y1 − y0 and
g2 = y2 − y1; in the Brownian limit the sums over wall positions become the integrals
over u and v in Theorem 5.4 below.

5.3.2. Brownian motion joint gaps. We apply the (X, Y) framework from Section 3
with k = 2: two walls produce three survivors at positions y0 < y1 < y2, with
consecutive gaps G1 = y1 − y0 and G2 = y2 − y1.

Theorem 5.4 (Joint gap intensity and negative correlation). The joint gap intensity
for (G1, G2) is
 h(G1, G2) = ∫ ∫

u<v det M0(u, v; G1, G2) du dv,

where u, v are the rescaled positions of the two walls (the constraint u < v is the
wall ordering). The three survivors are placed at rescaled positions 0, G1, G1 + G2
(translation invariance fixes the leftmost survivor at the origin). Write S = G1 + G2
for the total gap. The 4 × 4 matrix M0 is:

M0 =
 





 ϕ(u) ϕ(G1−u) Φ(G1−u) − 1 ϕ(S−u)

−u ϕ(u) (G1−u) ϕ(G1−u) −ϕ(G1−u) (S−u) ϕ(S−u)

ϕ(v) ϕ(G1−v) Φ(G1−v) ϕ(S−v)

−v ϕ(v) (G1−v) ϕ(G1−v) −ϕ(G1−v) (S−v) ϕ(S−v)
 




 ,

where ϕ is the standard normal density and Φ its CDF. The block structure is
(2+2)×(1+2+1) (Example 3.3 and Figure 4); the even rows are the source derivatives
from the grid refinement of Proposition 4.1.
The marginal gap distributions are each Rayleigh(√2), but the joint intensity
does not factorize. The gaps are negatively correlated, with ρ ≈ −0.163.

General structure for k gaps. The joint intensity h(G1, . . . , Gk) of k consecutive
gaps is obtained by integrating a 2k × 2k determinant with the same block structure
as in Section 3.2 and Figure 4: k row-pairs (density and derivative) and k+1 density
columns plus k−1 CDF columns. The case k = 2 above has 3 density columns and
1 CDF column. See Remark 5.5 for the general case.

Proof. By Theorem 4.3, the intensity of the consecutive pattern y0 ↖ x1 ↗ y1 ↖
x2 ↗ y2 is det(M0). Fix rescaled coordinates: place the three survivors at 0, G1,
G1 + G2 (translation invariance removes the location variable), and let u, v be the
rescaled wall positions. The Gaussian density ϕ(y − x) and CDF Φ(y − x) give the
matrix entries directly; the source derivative ∂xϕ(y − x) = (y − x) ϕ(y − x) and
∂xΦ(y − x) = −ϕ(y − x) supply the even rows (Remark 4.2). Integrating det(M0)
over the wall positions with the ordering constraint u < v yields the joint gap
intensity. □

The determinant does not factorize as f (G1)·g(G2) because the wall variables u, v
couple the two gaps: each wall position interacts with all three survivors. Numerical

COALESCING RANDOM WALKS VIA THE COALESCENCE DETERMINANT 19

0 0.5 1 1.5 2 2.5
0

0.5

1

1.5

2

2.5
 0 . 50.40.30.30.2
0 .2

0.1

0 . 10.1
G1G2
Figure 5. Joint gap intensity h(G1, G2) from Theorem 5.4, com-
puted by numerical integration. The tilted elliptical contours reflect
negative correlation (ρ ≈ −0.163).

integration gives ρ ≈ −0.163 (to three decimal places). An analytical proof that
ρ < 0 remains open, as does a closed-form expression for ρ.
See Figure 5.

Remark 5.5 (Higher-order gap distributions). The joint intensity of k consecutive
gaps (G1, . . . , Gk) follows from the 1+2+ · · · +2+1 pattern (Section 3) with 2k
particles in k pairs. By Proposition 4.1, the 2k ×2k determinant scales as εk det(M0),
where M0 has alternating rows of transition densities and spatial derivatives. This
determines the joint intensity h(G1, . . . , Gk).
Preliminary numerical computations suggest that non-adjacent gaps also have
negative correlations, though weaker than for adjacent gaps.

6. Warren’s Formula

We now derive the determinantal CDF formula described in Section 1.2 for all
skip-free processes from the coalescence determinant.
The setting is the following. Start n particles at fixed positions x1 < · · · < xn;
each performs an independent skip-free process until it meets another particle, at
which point the two coalesce and continue as one. At time T , some of the original n
particles have merged, so the number of distinct positions is at most n. Warren’s
formula gives the joint CDF of these positions.
We use the notation P (x, y) and F (x, y) from Section 2. We write ∑

z for
summation over the state space S; in the continuous case, all sums become integrals.

Theorem 6.1 (Warren’s formula for skip-free processes). Let X (1), . . . , X (n) be
coalescing skip-free processes on a linearly ordered state space S, starting at positions

20 PIOTR ŚNIADY

x1 < x2 < · · · < xn. Let ZT (xi) denote the position at time T of the particle that
started at xi (after possible coalescence).
For y1 ≤ y2 ≤ · · · ≤ yn in S:

P(ZT (xi) ≤ yi for all i = 1, . . . , n) = det(M W ),

where the n × n matrix M W has entries:

M W
ij = F (xi, yj) − [i < j].

Proof. The plan is: sum over all coalescence patterns n = n1 + · · · + nk, and for each
pattern sum the survivor positions z1, . . . , zk over the region compatible with the
CDF thresholds y1, . . . , yn. We then show that the resulting sum of determinants
collapses to det(M W ).
By Theorem 2.2, composition n1 + · · · + nk = n produces an n × n coalescence
matrix ˜M whose determinant gives the joint density of the k survivor positions. All
particles in block l share the same survivor zl, so the constraint zl ≤ yi for every i
in the block reduces to zl ≤ yjl , where jl = n1 + · · · + nl−1 + 1 is the first index in
the block (giving the smallest threshold). The CDF decomposes as

P
(ZT (xi) ≤ yi ∀ i
) = ∑

n1+···+nk =n
 ∑

z1<···<zk
zl ≤yj l
 det ˜M (z1, . . . , zk),

a sum over all 2
n−1 compositions of n.
We evaluate this sum by collapsing one column at a time, from right to left.

Summing out the rightmost survivor. We sum out the survivor variable that
feeds into column n, grouping patterns in pairs. For each composition m1+· · ·+mr =
n−1, define two compositions of n:
• Pattern A: m1 + · · · + mr + 1 (particle n in a new block);
• Pattern B: m1 + · · · + (mr+1) (particle n appended to the last block).
This pairs the 2n−1 compositions of n into 2n−2 pairs.
Columns 1, . . . , n−1 of the coalescence matrix are identical for paired patterns A
and B (same block sizes, same survivors): extending the last block adds column n
but does not alter the existing columns.
In Pattern A, the survivor zr+1 of the new block {n} appears only in column n
(P -type). Summing over zr+1 ∈ (zr, yn] replaces this column by the vector
(F (xi, yn) − F (xi, zr))
i.

By multilinearity of the determinant in column n, Pattern A contributes

det
(· · · , F·(yn)
) − det(· · · , F·(zr)
),

where · · · denotes columns 1, . . . , n−1 and F·(y) is the column (F (xi, y))
n
i=1.
In Pattern B, column n is F (xi, zr) − [i < n] (an F -column with staircase, since n
is not the first index in its block). By multilinearity:

det
(· · · , F·(zr)) − det(· · · , [i < n]
).

Adding: the F·(zr) terms cancel, leaving

det
(· · · , F·(yn) − [i < n]
).

Column n is now M W
·,n = F (xi, yn) − [i < n], independent of all survivor variables.

REFERENCES 21

The rightmost survivor has been summed out: column n is in its final Warren
form, and the remaining sum runs over the 2n−2 compositions of n−1 and their
survivors.

Iteration. Repeating the pairing at boundary (n−2, n−1) collapses column n−1
to F (xi, yn−1) − [i < n−1], reducing to 2n−3 compositions of n−2. After n − 1
iterations every column is in Warren form. The final step sums the sole remaining
survivor z1 over (−∞, y1], giving column 1 = F·(y1) (with [i < 1] = 0). The result
is det(M W ). □

Theorem 6.1 applies to all the skip-free processes discussed in earlier sections,
including birth-death chains (Example 3.8) and reflected Brownian motion (Sec-
tion 4.4).
 Acknowledgments

We thank Theodoros Assiotis, Balázs Bárány, Maciej Dołęga, Sho Matsumoto,
Bálint Tóth, Ákos Urbán, Oleg Zaboronski, and Karol Życzkowski for stimulating
discussions and helpful literature suggestions.
We thank Richard Arratia for generously providing access to his PhD the-
sis [Arr79].
We are grateful to Folkmar Bornemann for sharing his MATLAB toolbox for
computing distributions in random matrix theory [Bor10]. This software was
instrumental in our preliminary numerical experiments.
Claude Code (Anthropic) was used as an assistant during formula discovery and
manuscript preparation.
 References

[AB05] Daniel ben Avraham and Éric Brunet. “On the relation between one-
species diffusion-limited coalescence and annihilation in one dimension”.
In: J. Phys. A: Math. Gen. 38 (2005), pp. 3247–3252. doi: 10.1088/
0305-4470/38/15/001. arXiv: cond-mat/0412745.
[AOW19] Theodoros Assiotis, Neil O’Connell, and Jon Warren. “Interlacing Dif-
fusions”. In: Séminaire de Probabilités L. Vol. 2252. Lecture Notes in
Mathematics. Cham: Springer, 2019, pp. 301–380. doi: 10.1007/978-
3-030-28535-7_13. arXiv: 1607.07182.
[Arr79] Richard Arratia. “Coalescing Brownian motions on the line”. PhD thesis.
University of Wisconsin–Madison, 1979.
[Ass18] Theodoros Assiotis. “Random surface growth and Karlin–McGregor
polynomials”. In: Electron. J. Probab. 23 (2018), Paper no. 106, 81 pp.
doi: 10.1214/18-EJP236. arXiv: 1709.10444.
[Ass23] Theodoros Assiotis. On some integrable models in inhomogeneous space.
2023. arXiv: 2310.18055 [math.PR].
[Avr98] Daniel ben Avraham. “Complete exact solution of diffusion-limited
coalescence, A + A → A”. In: Phys. Rev. Lett. 81 (1998), pp. 4756–4759.
doi: 10.1103/PhysRevLett.81.4756. arXiv: cond-mat/9803281.
[Bor10] Folkmar Bornemann. “On the Numerical Evaluation of Distributions in
Random Matrix Theory: A Review”. In: Markov Processes and Related
Fields 16.4 (2010), pp. 803–866.

22 REFERENCES

[DA88] Charles R. Doering and Daniel ben Avraham. “Interparticle distribution
functions and rate equations for diffusion-limited reactions”. In: Phys.
Rev. A 38 (1988), pp. 3035–3042. doi: 10.1103/PhysRevA.38.3035.
[Fom16] Vladimir Fomichov. “The distribution of the number of clusters in the
Arratia flow”. In: Communications on Stochastic Analysis 10.3 (2016),
pp. 257–270. doi: 10.31390/cosa.10.3.01.
[FTZ20] Will FitzGerald, Roger Tribe, and Oleg Zaboronski. “Sharp asymptotics
for Fredholm Pfaffians related to interacting particle systems and ran-
dom matrices”. In: Electron. J. Probab. 25 (2020), Paper no. 49, 1–15.
doi: 10.1214/20-EJP512. arXiv: 1905.03754.
[FTZ22] Will FitzGerald, Roger Tribe, and Oleg Zaboronski. “Asymptotic expan-
sions for a class of Fredholm Pfaffians and interacting particle systems”.
In: Ann. Probab. 50.6 (2022), pp. 2409–2474. doi: 10.1214/22-AOP1586.
arXiv: 2107.14504.
[GF17] E. V. Glinyanaya and V. V. Fomichov. “The central limit theorem for
the number of clusters of the Arratia flow”. In: Theory of Stochastic
Processes 22(38).2 (2017), pp. 1–7. arXiv: 1712.05098.
[GPTZ18] Barnaby Garrod, Mihail Poplavskyi, Roger Tribe, and Oleg Zaboronski.
“Examples of interacting particle systems on Z as Pfaffian point processes:
annihilating and coalescing random walks”. In: Ann. Henri Poincaré 19
(2018), pp. 3635–3662. doi: 10.1007/s00023-018-0719-x.
[HL75] Richard A. Holley and Thomas M. Liggett. “Ergodic theorems for weakly
interacting infinite systems and the voter model”. In: Ann. Probab. 3.4
(1975), pp. 643–663. doi: 10.1214/aop/1176996306.
[KM59] Samuel Karlin and James McGregor. “Coincidence probabilities”. In:
Pacific J. Math. 9.4 (1959), pp. 1141–1164. doi: 10.2140/pjm.1959.9.
1141.
[Śni26a] Piotr Śniady. Exact determinant formulas for coalescing particle systems.
2026. arXiv: 2602.10782 [math.PR].
[Śni26b] Piotr Śniady. Pfaffian structure of basin walls for coalescing particles.
2026. arXiv: 2602.22885 [math.PR].
[TZ11] Roger Tribe and Oleg Zaboronski. “Pfaffian formulae for one-dimensional
coalescing and annihilating systems”. In: Electron. J. Probab. 16 (2011),
pp. 2080–2103. doi: 10.1214/EJP.v16-942.
[TZ26] Roger Tribe and Oleg Zaboronski. “Entrance laws for coalescing and
annihilating Brownian motions”. In: (2026). arXiv: 2602.16509.
[Urb25] Ákos Urbán. “The Pólya Web”. MA thesis. Budapest University of
Technology and Economics, 2025. arXiv: 2601.12172 [math.PR].
[War07] Jon Warren. “Dyson’s Brownian motions, intertwining and interlacing”.
In: Electron. J. Probab. 12 (2007), pp. 573–590. doi: 10.1214/EJP.v12-
406.

Institute of Mathematics, Polish Academy of Sciences, ul. Śniadeckich 8,
00-656 Warszawa, Poland
Email address: psniady@impan.pl
