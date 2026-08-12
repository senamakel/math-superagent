<!-- source: https://arxiv.org/pdf/2602.10782 | converted from PDF -->

EXACT DETERMINANT FORMULAS
FOR COALESCING PARTICLE SYSTEMS

PIOTR ŚNIADY AND ÁKOS URBÁN

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
so the results apply wherever the classical non-colliding theory does: discrete
lattice paths, birth-death chains, and continuous diffusions including Brownian
motion.

To Marek Bożejko, whose path crossed ours at just the right moments.

1. Introduction

1.1. The problem. Consider n particles performing independent random walks
on a one-dimensional universe for which a version of the ‘Darboux property’ holds
true: two particles cannot swap order without being at some intermediate moment
in the same state. (We postpone the formal definition to the crossing property of
Definition 2.5 and, for continuous time, to order preservation in Section 10.1; for now
a concrete example to keep in mind is a system of simple random walks, each taking
±1 steps and starting at even integers; see the non-dotted lines in Figure 1.) When
two particles meet, they coalesce into one. What is the probability that the particles
end up at specified positions, having undergone a specified pattern of coalescences?
This model appears throughout probability and statistical physics, notably in the
voter model [HL75]—where tracing ancestry backward in time produces coalescing
lineages.

2020 Mathematics Subject Classification. Primary 05A15; Secondary 05A19, 15A15, 60C05,
60J65, 82C22.
Key words and phrases. coalescing random walks, ghost particles, Lindström–Gessel–Viennot
lemma, Karlin–McGregor formula, determinant, interacting particle systems.
A 12-page extended abstract of this paper will be submitted to the proceedings of the conference
Formal Power Series and Algebraic Combinatorics (FPSAC) [ŚU26].

1

arXiv:2602.10782v3  [math.PR]  8 Jul 2026

2 PIOTR ŚNIADY AND ÁKOS URBÁN

x

t

T
 x1 x2 x3

c
 yH yH′ yg particle 1
particle 2
heir H
ghost g
particle 3 = heir H ′

Figure 1. Coalescence on the checkerboard lattice (pattern
2+1). Three particles start at x1 < x2 < x3. Particles 1 (solid)
and 2 (double) coalesce at c, producing heir H (ticked) and a
ghost (dotted). Particle 3 (zigzag) does not coalesce; it is heir H ′.
The ghost shares two edges with heir H ′ (shown offset)—ghosts
do not interact and may cross any path freely. Final positions:
yH < yH ′ < yg.

For non-colliding particles, exact probabilities are classical. The Karlin–McGregor
theorem [KM59] expresses the probability that n particles starting at positions
x1 ≤ · · · ≤ xn avoid collision as a determinant:

P(particles reach y1, . . . , yn without colliding) = det
(p(xi → yj)
)
1≤i,j≤n,

where p(xi → yj) is the transition probability from xi to yj for a single particle,
and the target positions y1 ≤ · · · ≤ yn are weakly increasing. The combinatorial
version is the Lindström–Gessel–Viennot (LGV) lemma [Lin73; GV85].

When particles coalesce, the count changes. After m coalescences, only k = n − m
particles remain. The determinant formula breaks down: the number of rows (initial
particles) exceeds the number of columns (final particles), leaving no square matrix.

1.2. The ghost method. Our solution is to keep the ‘discarded’ particles walking.
Whenever two particles meet, the collision produces one heir and one ghost: the
heir continues as a single particle—free to meet and merge again—while the ghost
walks off as an independent random walk that starts at the collision point and no
longer interacts with anything. Each later merger again splits off one fresh ghost,
so a single heir may absorb many particles by multiple collisions.
The total count—heirs plus ghosts—remains exactly n at every stage of the
dynamics. With n initial particles and n final entities, we can write a square matrix
and take its determinant. The ghosts are not physically real from the viewpoint
of coalescing random walks, but the enlarged system admits exact determinantal
formulas. We call this the ghost particle method.
Figure 1 illustrates this viewpoint for the coalescence pattern 2+1: particles 1
and 2 collide, producing one heir and one ghost, while particle 3 continues undis-
turbed. This is the simplest case, a single merger; in general an heir may merge
repeatedly, each collision producing another ghost.

COALESCING PARTICLE SYSTEMS 3

1.3. Main results.

1.3.1. The coalescence formula. Consider n particles starting at positions x1 ≤ · · · ≤
xn. Suppose they coalesce into k heirs at positions yH1 < · · · < yHk , producing
m = n − k ghosts at positions yg1, . . . , ygm . The coalescence pattern is described by
a composition c1+ · · · +ck = n, where cj counts how many of the initial particles
merge into the heir Hj.
A ghost g comes to rest either to the left or to the right of its heir, and we record
which by a single bit, the ghost sign εg ∈ {−1, +1}: it is +1 when the ghost lies
to the left of its heir and −1 when it lies to the right. We will often use Iverson’s
bracket notation
 [εg = +1] =
 {1 if εg = +1,
0 otherwise,

[εg = −1] =
 {1 if εg = −1,
0 otherwise;

in figures, where space is tight, we abbreviate these as [ε
+
g ] and [ε−
g ].
Each ghost is created when two adjacent particles merge and the boundary
between them dissolves. We index the ghost by its junction index g ∈ {2, . . . , n},
which also indexes the ghost’s column in the matrix below.

Theorem 1.1 (Coalescence formula, informal version of Theorem 3.2). The proba-
bility that the final outcome follows the prescribed coalescence pattern, with the final
entities at the positions above, is the determinant

(1.1) P = det M

of the n × n matrix M whose rows are indexed by the initial particles and whose
columns are indexed by the final entities. The columns are arranged in groups of
c1, . . . , ck: the i-th group consists of the heir Hi followed by the ci − 1 ghosts created
on the way to Hi. An heir column holds the usual transition probabilities

Mi,H = p(xi → yH ),

while a ghost column g has a signed “staircase” structure of ± transition probabilities
and zeros, selected by the ghost sign:

Mi,g =
 {
−[εg = −1] · p(xi → yg) if i < g,

[εg = +1] · p(xi → yg) if i ≥ g.

See Figure 2 for the shape of M .

1.3.2. Example: coalescence pattern 2+1. Returning to Figure 1: three particles
start at x1 < x2 < x3. Particles 1 and 2 collide and merge into heir H; particle 3
does not collide and is the sole particle behind heir H ′. The result: two heirs at
positions yH < yH ′ and one ghost g. Heir H and its unique ghost g form the first
group of columns, the heir H ′ forms the second group. The 3 × 3 matrix is:

M =
 




p(x1 → yH ) −[εg = −1] · p(x1 → yg) p(x1 → yH ′)

p(x2 → yH ) [εg = +1] · p(x2 → yg) p(x2 → yH ′)

p(x3 → yH ) [εg = +1] · p(x3 → yg) p(x3 → yH ′)




 .

4 PIOTR ŚNIADY AND ÁKOS URBÁN

p(x1 → yH ) −[ε−
g ] p(x1 → yg) p(x1 → yH′ ) −[ε−
g′ ] p(x1 → yg′ )

p(x2 → yH ) [ε
+
g ] p(x2 → yg) p(x2 → yH′ ) −[ε−
g′ ] p(x2 → yg′ )

p(x3 → yH ) [ε
+
g ] p(x3 → yg) p(x3 → yH′ ) −[ε−
g′ ] p(x3 → yg′ )

p(x4 → yH ) [ε
+
g ] p(x4 → yg) p(x4 → yH′ ) [ε
+
g′ ] p(x4 → yg′ )

x1

x2

x3

x4
 H g H ′ g′

heir ghost heir ghost

heir column above step (i < g) below step (i ≥ g)

Figure 2. The coalescence matrix: staircase structure. Ma-
trix M for the 2+2 coalescence pattern: the initial particles 1
and 2 merge into heir H; the initial particles 3 and 4 merge into
heir H ′. Heir columns (yellow) contain plain transition probabili-
ties p(xi → yH ), p(xi → yH ′). Ghost columns show the staircase
pattern with the thick staircase line separating the two regions.
(With the notations of Sections 2.3 and 2.5, the heir H corresponds
to the interval [1, 3), and its ghost g corresponds to the junction 2;
similarly the heir H ′ corresponds to the interval [3, 5) and its ghost
g′ to the junction 4, so that the columns H, g, H ′, g′ correspond
to the final entities [1, 3), 2, [3, 5), 4 listed in min-order, with min-
values 1 < 2 < 3 < 4.)

More concretely, the scenario shown on Figure 1 corresponds to the case εg = −1
(i.e., yg ≥ yH ), so the matrix takes the form

(1.2) M =
 



p(x1 → yH ) −p(x1 → yg) p(x1 → yH ′)

p(x2 → yH ) 0 p(x2 → yH ′)

p(x3 → yH ) 0 p(x3 → yH ′)




 ;

COALESCING PARTICLE SYSTEMS 5

the determinant of (1.2) expands to a difference of two products of single-particle
transition probabilities.
In the other case εg = +1 (i.e., yg ≤ yH ) the matrix takes the form

(1.3) M =
 




p(x1 → yH ) 0 p(x1 → yH ′)

p(x2 → yH ) p(x2 → yg) p(x2 → yH ′)

p(x3 → yH ) p(x3 → yg) p(x3 → yH ′)




 ;

the determinant of (1.3) is a signed sum of four products.
This asymmetry—two terms versus four—reflects the staircase structure: the
ghost’s index and sign determine which rows contribute. Such asymmetry is a
general feature of the coalescence formula.

Several boundary configurations—weakly increasing heir positions, a ghost coin-
ciding with its heir, and coinciding initial positions—refine how the theorem should
be read; we treat them in Remark 3.3.

1.3.3. The coalescence determinant. For applications, one typically wants the prob-
ability of heir positions alone, summed over all ghost positions. Integrating out the
ghosts yields the coalescence determinant (Section 11): a ghost-free, closed-form
determinant whose heir columns contain transition probabilities and whose ghost
columns contain cumulative distribution functions in a staircase pattern.

1.4. Relation to classical determinantal formulas. The coalescence formula
(1.1) generalizes the Karlin–McGregor / Lindström–Gessel–Viennot (LGV) determi-
nant, and its proof adapts the classical segment-swap argument (Section 3.3), which
pairs the configurations where particles cross and cancels them in the signed sum
of the determinant. The argument originates with Karlin and McGregor [KM59];
Lindström [Lin73] independently discovered the same cancellation in the setting
of matroid theory, Gessel and Viennot [GV85] developed it into the LGV lemma
for lattice-path counting, and Stembridge [Ste90] extended it to acyclic digraphs,
introducing D-compatibility as the structural condition; see the survey of Kratten-
thaler [Kra15].
In our setting, crossings are not forbidden but prescribed: the ghost configuration
specifies which crossings must occur. The involution has the same structure—swap
at the first wrong crossing—but “wrong” now means “crossing that violates the
prescribed pattern.” The ghost signs (εg) encode which crossings are required, and
the Iverson brackets in the ghost columns retain exactly those terms where particles
cross at the right places. When no coalescences occur (no ghosts, every entity an
heir), the formula reduces to the classical LGV determinant.

1.5. Prior work. Coalescing Brownian motions were constructed by Arratia [Arr79].
Exact distributional results have since been obtained through several independent
lines of work.

1.5.1. Gap distributions and the IPDF method. Doering and ben-Avraham [DA88] in-
troduced the inter-particle distribution function (IPDF) method, computing nearest-
neighbor gap distributions for diffusion-limited coalescence; ben-Avraham [Avr98]
extended this to the full hierarchy of empty-interval probabilities; ben-Avraham and
Brunet [AB05] extracted explicit densities for consecutive spacings. See Section 1.8.1
for the ghost-based derivation.

6 PIOTR ŚNIADY AND ÁKOS URBÁN

1.5.2. Warren’s determinantal formula. Warren [War07] proved another n × n de-
terminantal formula for coalescing Brownian motions. His mechanism does not
use ghosts: after coalescence, merged particles simply follow the same trajectory.
Writing Zt(xi) for the position at time t of the survivor containing particle xi, the
joint cumulative distribution function P(Zt(xi) ≤ yi for all i) can be expressed as a
determinant. Since merged particles share a trajectory, the formula does not resolve
which particles have coalesced. Assiotis, O’Connell, and Warren [AOW19] extended
this via intertwining relations to general diffusions, and Assiotis [Ass18; Ass23] to
birth-death chains. The ghost formula provides a finer, pattern-level resolution of
Warren’s determinant (see Section 1.8.1).

1.5.3. Pfaffian point processes. A different question arises for infinitely many par-
ticles: what is the statistical structure of the surviving positions? Tribe and
Zaboronski [TZ11] proved that under the maximal entrance law for coalescing Brow-
nian motions (particles starting from every point of R), the surviving positions form
a Pfaffian point process with an explicit 2× 2 matrix kernel involving the complemen-
tary error function. Garrod, Poplavskyi, Tribe, and Zaboronski [GPTZ18] extended
this to continuous-time random walks on Z with spatially inhomogeneous rates and
arbitrary deterministic initial conditions. Their framework also covers annihilation
and mixed coalescence-annihilation and, as shown by Tribe and Zaboronski [TZ26],
all entrance laws—but it requires a time-homogeneous Markov generator with a
specific algebraic structure (the spin-pair identity). Using the Pfaffian structure,
Fomichov [Fom16] found the exact distribution of the number of surviving particles,
and Glinyanaya and Fomichov [GF17] proved a central limit theorem with explicit
variance.
The ghost formula and this Pfaffian approach have complementary strengths
(Section 1.6.1); see Section 1.8.3 for the ghost-based derivation.

1.5.4. The Pólya web. A key motivating example is the Pólya web, introduced by
the second-named author [Urb25]: coalescing chains on N2 whose steps follow a
Pólya urn rule. Each walk has a Beta-distributed limiting direction, and coalescence
corresponds to equality of limits. For pairwise coalescence, Urban shows that the
joint density of these limiting directions is a determinant whose entries alternate
between Beta density and cumulative distribution functions—a special case of our
coalescence determinant (Section 1.8.4).

1.6. Scope and structure of the method. Beyond the specific formulas, the
ghost method has several structural features—wide applicability, algebraic flexibility,
and exactness—that enable the results of the companion papers.

1.6.1. Wide scope. The ghost formula requires exactly the same assumptions as the
Karlin–McGregor theorem [KM59]—order preservation, identical and independent
dynamics, the strong Markov property, and meeting times being stopping times
(Section 10.1)—and therefore shares its broad scope: lattice random walks with
arbitrary inhomogeneous transition probabilities, birth-death chains, Brownian
motion, and more generally any skip-free Markov process (transitions only to
neighboring states, so that particles cannot change order without first meeting).
The analytic approaches surveyed in Section 1.5 have a different reach: the Pfaffian
point process method [TZ11; GPTZ18] requires access to the Markov generator

COALESCING PARTICLE SYSTEMS 7

and its spin-pair identity, and the IPDF method [DA88; Avr98] relies on Brownian-
motion-specific integrals; but they reach results the ghost method does not, such as
mixed coalescence-annihilation and all entrance laws [TZ26]. Neither framework
subsumes the other.

1.6.2. Algebraic flexibility and exactness. The ghost formula is a determinant, and
an exact one—not an asymptotic expansion or a scaling limit. The applications in
the companion papers rest on precisely this: determinants admit row and column
operations, and exactness permits algebraic rearrangement before any limit is
taken. Confluent limits of nearly coinciding boundary points produce the 2 × 2
block structure of the Tribe–Zaboronski Pfaffian kernel [TZ11; GPTZ18; Śni26e];
collapsing the determinant’s columns one by one recovers Warren’s formula [War07],
whose cumulative-distribution entries are revealed as the ghosts’ contribution; and
rearranging exact cumulant integrals yields a combinatorial central limit theorem
for basin boundaries [Śni26e].

At a structural level, the ghost method is a minimal extension of the Karlin–
McGregor theorem: the same sign-reversing involution applied to the same deter-
minantal language, with one new ingredient—the ghost particles that restore the
matrix to square form.

1.7. New viewpoint on the classic construction. The classic construction
of a finite coalescing system fixes a priority order on the particles, runs their
trajectories, and at each collision keeps the highest-priority particle while discarding
the rest [Arr79]. Our viewpoint reclaims this waste: the absorbed particles are
reclassified as ghosts, and the classic construction is thereby retrofitted to produce
the system of n particles and ghosts studied here (Section 10).

1.8. Companion papers. This paper is part of a series of five (Figure 3). The
left column develops exact combinatorial formulas (this paper for coalescence, a
companion for annihilation), while the right column applies them to probability (gap
distributions, Pfaffian point processes, and a detailed example). The top row is the
coalescence story (ghost particle method → wall-particle system), the bottom row
starts from annihilation (ghost pair method) and uses it to derive Pfaffian structure
for the coalescing system. The two rows are independent—neither relies on the
other. A fifth paper [BŚTU26] applies both lines of work to the Pólya web.

1.8.1. Gap distributions and Warren’s formula [Śni26c]. Under the maximal entrance
law (Section 1.5.3), coalescing particles come down from infinity: at any positive
time only finitely many survivors remain per bounded interval, each attracting a
basin of initial particles that eventually merge into it. The boundaries between
adjacent basins are the walls (Figure 4).
The companion paper [Śni26c] applies the coalescence determinant (Section 11)
to this wall-particle system—the joint process of survivors and walls—deriving gap
distributions and generalizing Warren’s formula (Section 1.5.2) to arbitrary skip-free
processes.

8 PIOTR ŚNIADY AND ÁKOS URBÁN

exact combinatorial
formulas probability
applications

this paper
ghost particle method [Śni26c]
wall-particle system

[Śni26d]
ghost pair method
 [BŚTU26]
example: Pólya web

[Śni26e]
Pfaffian structure
of walls

application

cancellative
labeling

parallel
constructions
 coalescence annihilation

Figure 3. This paper and its four companions. Two parallel
combinatorial constructions—the ghost particle method for coales-
cence developed here and the ghost pair method for annihilation—
yield exact determinant formulas. These are applied to probability,
giving gap distributions and Warren’s formula and the Pfaffian
structure of walls, and both lines converge on the Pólya web as a
worked example.

1.8.2. Annihilation [Śni26d]. The ghost method also applies to annihilation (A+A →
∅), where both particles are destroyed upon collision. Each collision now produces a
ghost pair —two independent random walks starting from the collision point—rather
than one heir and one ghost. The companion paper [Śni26d] uses this ghost pair
method to derive an annihilation formula with the same determinantal structure
and sign-reversing involution; when all n = 2k particles annihilate completely, the
determinant reduces to a Pfaffian. Applications include domain wall dynamics in
the Ising–Glauber model [AH00].

1.8.3. Pfaffian structure of walls [Śni26e]. The companion paper [Śni26e] proves a
Pfaffian empty-interval formula for the walls of any skip-free coalescing system: a de-
terministic cancellative labeling converts pairwise coalescence into total annihilation,
and the annihilation formula [Śni26d] then supplies the Pfaffian structure, yielding
explicit cumulants and a central limit theorem for the wall count. Checkerboard
duality identifies surviving particles with walls of a dual process, transferring the
Pfaffian structure to the survivors themselves; specializing to Brownian motion under
the maximal entrance law recovers the Tribe–Zaboronski kernel [TZ11; GPTZ18].

COALESCING PARTICLE SYSTEMS 9

· · · · · ·

· · · · · ·time
t = 0

t > 0

Figure 4. Coalescing random walks starting from every site. Paths
merge on contact; line weight increases with each merger. Walls
(triangles at the bottom) mark the boundaries between basins of
attraction at t = 0; survivors (large dots on top) are the particles
that remain at t > 0, one per basin.

1.8.4. The Pólya web [BŚTU26]. The companion paper [BŚTU26] applies both the
coalescence determinant and the Pfaffian machinery to the Pólya web [Urb25]. The
Pólya web is a natural testing ground for the general theory: it is genuinely non-
homogeneous (transition probabilities depend on position) yet exactly solvable, and
it mixes the discrete (finitely many survivors at each level) with the continuous (each
survivor acquires a Beta-distributed asymptotic direction). In suitable projective
coordinates the paper derives exact configuration probabilities, an arcsine law for
boundary positions, and Rayleigh spacing for gaps between adjacent survivors; the
Pfaffian kernel, built from Beta crossing probabilities, converges to the comple-
mentary error function kernel of coalescing Brownian motions, and the number
of survivors satisfies a central limit theorem with the Fano factor of coalescing
Brownian motions. Urban’s original proof [Urb25] reaches the same determinant
from a complementary direction—conditioning the Karlin–McGregor determinant
on successive coalescences—and derives the distribution of the number of survivors
and edge scaling to a Yule web.

1.9. Organization. Section 2 formalizes the coalescence model on weighted directed
acyclic graphs, defining performances (coalescence histories) and their weights.
Section 3 states precisely the main result, the coalescence formula, and gives an
outline of its proof; the proof itself occupies Sections 4 to 9, which develop, in
turn, the combinatorial framework, the attribution map, the rehearsal algorithm,
their mutual inversion, the sign-reversing involution, and the assembly of the proof.
Section 10 extends the formula to continuous time and space, covering Brownian
motion and birth-death chains, and Section 11 integrates out ghost positions, yielding
the closed-form ghost-free coalescence determinant used in the companion papers.

1.10. Companion code. Two software deposits accompany this paper, providing
two different kinds of evidence.
The first deposit [Śni26b] contains a machine-checked proof : the discrete results of
this paper are formalized and verified in the Lean 4 proof assistant, accompanied by

10 PIOTR ŚNIADY AND ÁKOS URBÁN

a Python reference implementation of the paper’s algorithms. An extended version
of this article, distributed with the formalization, adds a companion appendix
describing it and notes linking each result to its machine-checked counterpart.
The second deposit [Śni26a] contains exact numerical tests of the theorems: the
simulation and exact-enumeration code which was used to discover the formulas of
the present paper and of the companion paper on annihilation [Śni26d], and which
compares them, in exact arithmetic, against independent brute-force enumeration.

2. Setup

The coalescence formula holds for random walks on Z, Brownian motion on R,
and birth-death chains on arbitrary state spaces. Rather than prove each case
separately, we work with spacetime graphs—an abstraction that captures two
structural properties common to all settings:
(i) Planarity: paths with swapped endpoints must cross, and non-adjacent
particles cannot meet without an intermediate particle involved;
(ii) Weight-preserving segment swap: exchanging path segments at cross-
ings preserves total weight.
For discrete models (lattice walks), the spacetime graph is literal: vertices are
space-time points, edges are allowed transitions, and edge weights are transition
probabilities. For continuous processes (Brownian motion, continuous-time jump
processes), the graph is a conceptual tool—the actual proof uses measure-theoretic
arguments (Section 10), but the combinatorial structure is identical.

2.1. Spacetime graphs.

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

w(P ) =
 ℓ−1∏

i=0 w(vi → vi+1).

The weight from x to y is the total weight of all directed paths between them:

W (x → y) = ∑

P path
from x to y
 w(P ).

When the edge weights are the transition probabilities of a single particle, W (x → y)
is the probability that the particle, started at x, reaches y—the transition probability

COALESCING PARTICLE SYSTEMS 11

xI1
xI2
xI3xI4
 c3
 c2
y[1,4)
 y2 y3

y[4,5)
 Particles
I1 = [1, 2)
I2 = [2, 3)
I3 = [3, 4)
I4 = [4, 5) = H ′

[2, 4)
[1, 4) = H

Ghosts
2
3

Figure 5. Running example: coalescence pattern 3+1. A per-
formance records the collision structure on a spacetime graph—here
the lattice Z
2 with North/East steps. Four particles start at xI1,
xI2, xI3, xI4 (leaves, colored dots). Particles I2 and I3 meet at
c3, merging into [2, 4); then I1 and [2, 4) meet at c2, forming heir
H = [1, 4) which ends at the root y[1,4). Particle I4 does not coa-
lesce; it is heir H ′ = [4, 5). Ghost paths (dashed/dotted) emanate
from merger points: ghost 2 is born at c2, ghost 3 at c3. Note that
ghost 3 crosses through particle I1—ghosts are non-interacting. See
Figure 6 for the labeling scheme.

written p(x → y) in the introduction. The general theory below works with the
weight W ; the probabilistic reading is the special case.

Example 2.3 (Main examples).

• Product spacetime Z×Z≥0: vertices (x, t) with edges to (x′, t+1) for allowed
transitions.
• Checkerboard lattice: vertices where x + t is even, with edges to (x ± 1, t + 1)
(simple random walk, see Figure 1).

Figure 5 illustrates these concepts with a running example: four particles co-
alescing on the lattice Z
2 with North and East steps. We will use this example
throughout the paper.

2.2. Planarity. The classical LGV lemma counts non-intersecting paths, so it only
needs one geometric condition: paths with swapped endpoints must cross. For
interacting particles, we need a second condition controlling which particles can
collide.

Definition 2.4 (Source and target sets). The source set X ⊆ V and target set
Y ⊆ V are each equipped with a linear order ≺.

Definition 2.5 (Planar configuration). The pair (X , Y) is planar if:

(P1) Crossing property. For x ⪯ x′ in X and y′ ⪯ y in Y (targets swapped),
every path from x to y intersects every path from x′ to y′.

12 PIOTR ŚNIADY AND ÁKOS URBÁN

0 1 2 3 4 5

0 1 2 3 4 5

I1 I2 I3 I4

H H ′

2 3

Figure 6. Interval labeling and the final state. Initial parti-
cles (actors) are labeled by unit intervals; final entities (roles) by
intervals (heirs) or junction points (ghosts). This diagram shows
the same example as Figure 5. Here n = 4 (Example 2.8): initial
particles A = {I1, I2, I3, I4} and final entities R = {H, 2, 3, H ′}.
Heirs H = [1, 4) and H ′ = [4, 5); ghosts appear at junctions 2 and 3.
The min function is indicated by the small dots: each interval [a, b)
has a dot at position a (its left endpoint), so min reads off the
horizontal coordinate of the dot. Arrows show one bijection π:
I1 ↦→ H, I2 ↦→ 3, I3 ↦→ H ′, I4 ↦→ 2 between the initial particles
and the final entities. Under min, this becomes the permutation
1 ↦→ 1, 2 ↦→ 3, 3 ↦→ 4, 4 ↦→ 2—the 3-cycle (2 3 4) with sign +1.

(P2) Consecutive collision property. Let A, B, C be paths starting at x ⪯
x′ ⪯ x
′′ in X and ending in Y. If v ∈ A ∩ C, then there is a vertex w ≤ v
with w ∈ B ∩ (A ∪ C).

The crossing property (P1) is Stembridge’s D-compatibility [Ste90]: when paths
have swapped endpoints, they must meet somewhere (see Figure 7a). Stembridge’s
key insight was formulating this condition abstractly for general acyclic digraphs,
rather than relying on specific lattice geometry. This abstraction is what enables
generalizations to new settings—including ours.
The consecutive collision property (P2) is our addition for interacting particles.
It ensures that non-adjacent particles cannot collide without involving intermediate
particles—a physical constraint reflecting that particles on a line cannot jump over
each other. Classical LGV does not need this because it forbids all crossings; we
need it because collisions are allowed but must respect the spatial ordering (see
Figure 7b).

2.3. Interval labels.

2.3.1. Actors, heirs, and ghosts. Fix source vertices x1 ⪯ · · · ⪯ xn in X . The
coalescence structure is tracked using interval labels (see Figure 6).

Definition 2.6 (Interval labeling). The initial particle (also called actor ) starting
at xj is labeled by the unit half-open interval Ij = [j, j + 1); we also write xIj or
xI for the starting position of actor I. The set of actors is A = {I1, . . . , In}. The
junction points are J = {2, 3, . . . , n}—the shared endpoints between consecutive

COALESCING PARTICLE SYSTEMS 13

X

Y

A B

bridge
 (a)
 X

Y

A B C

v
 w
 bridge

(b)

Figure 7. The two planarity conditions (Definition 2.5), each
shown as a forbidden configuration; time runs upward, with sources
in X (bottom) and targets in Y (top). (a) Crossing prop-
erty (P1). Paths A and B have swapped endpoints—A runs
from the left source to the right target and B vice versa—yet reach
them without intersecting, one bridging over the other. Condi-
tion (P1) forbids this: paths with swapped endpoints must cross.
(b) Consecutive collision property (P2). Paths A and C
intersect at the shared vertex v ∈ A ∩ C. The intermediate path B
meets A ∪ C only at the vertex marked w, which lies above v. Con-
dition (P2) forbids this: B must share a vertex with A or C at or
before v.

intervals. Throughout, interval labels are half-open, so that the labels of distinct
active particles are disjoint.
When particles [a, b) and [b, c) collide, both disappear and two new entities are
born: an heir labeled [a, c) (the union), and a ghost labeled by the junction point b
(the dissolved boundary). In particular, particles that share a starting position
coalesce instantly: the coalescence occurs at time zero, and the heir and ghost
emerge from the shared vertex.

This labeling lets us trace origins: a particle labeled [a, c) arose from the merger
of all initial particles Ij with a ≤ j < c. Similarly, ghost b records which coalescence
created it: the one between the particles on either side of junction b.
Intuition: the heir [a, c) is “the owner of the interval [a, c),” and ghost b is
“attached to the boundary b that used to separate the particles on its left from those
on its right.”

2.3.2. Label order. The label order ◁ (read “label-less-than”) orders intervals and
junctions by position, by the following cases:

• interval before junction: [a, b) ◁ g iff b ≤ g;
• junction before interval: g ◁ [a, b) iff g ≤ a;
• interval before interval: [a, b) ◁ [a′, b
′) iff b ≤ a′;
• junction before junction: g ◁ g′ iff g < g′.

We write g ▷ I (read “label-greater”) for the reverse relation I ◁ g. For example,
I1 ◁ 2 ◁ I2 ◁ 3 ◁ I3. This is only a partial order: a junction g and an interval

14 PIOTR ŚNIADY AND ÁKOS URBÁN

[a, b) with a < g < b are ◁-incomparable, since neither b ≤ g nor g ≤ a holds. In
particular, a ghost is never comparable with its own heir.

2.3.3. min-labeling. The function min reads off the smallest element of an entity,
identifying intervals and junctions with [n] = {1, . . . , n}: an interval maps to its
left endpoint, [a, b) ↦→ a, and a junction is its own minimum, k ↦→ k. On the role
set R of final entities (the heirs and their ghosts, Section 2.5)—where each ghost
junction lies strictly inside its heir, so distinct entities have distinct minima—min is
injective, and the resulting total order, the min-order, is a linear extension of the
label order ◁: it places each heir immediately before the ghosts it contains, breaking
the incomparability noted above in favor of the heir.

2.4. Initial state. The initial state fixes the actors and where they start: the n
particles A = {I1, . . . , In} (Definition 2.6) begin at the source positions x1 ⪯ · · · ⪯
xn in X , with xi the starting position of actor Ii.

2.5. Final state. The final state F specifies:

• The ghost set G ⊆ J : junctions where coalescence occurred;
• The heir set H: maximal half-open intervals [a, b) ⊆ [1, n + 1) not containing
any junction from J \ G in their interior;
• The role set R = H ∪ G: the final entities;
• Final positions yf ∈ Y for each entity f ∈ R.

We assume heir positions respect label order: if H ◁ H ′, then yH ⪯ yH ′ . This is not
a restriction: by the crossing property (P1), any physically realizable coalescence
pattern must satisfy this ordering. Writing k = |H| for the number of heirs and
m = |G| for the number of ghosts, the cardinality is |R| = k + m = n.

Definition 2.7 (Heir function). For ghost g ∈ G, we write heir(g) for the unique
heir interval containing junction g: heir(g) = [a, b) where a < g < b.

Example 2.8 (Coalescence pattern 3+1). Consider n = 4 initial particles (Figures 5
and 6):
 A = {I1, I2, I3, I4}.

Suppose I2 and I3 coalesce (ghost at junction 3), then the merged particle [2, 4)
coalesces with I1 (ghost at junction 2), while I4 remains separate. The final state
has:
 G = {2, 3}, H = {[1, 4), [4, 5)}, R = {[1, 4), 2, 3, [4, 5)}.

Two heirs and two ghosts. Under the identification with [4]:

• A = {I1, I2, I3, I4} ←→ {1, 2, 3, 4} (particle Ij maps to j);
• R = {[1, 4), 2, 3, [4, 5)} ←→ {1, 2, 3, 4} (heir [1, 4) ↦→ 1, heir [4, 5) ↦→ 4,
ghosts map to themselves).

Any bijection π : A → R is thus a permutation of {1, 2, 3, 4}.

The ghost set G determines a composition c1+ · · · +ck = n, where cj counts the
initial particles that merge into the jth heir. In the example above, G = {2, 3} gives
composition 3+1; Figure 2 illustrates the 2+2 pattern.

COALESCING PARTICLE SYSTEMS 15

2.6. Performances. The classic Lindström–Gessel–Viennot lemma abstracts non-
colliding random walks into a graph-theoretic problem: counting tuples of vertex-
disjoint paths. We seek an analogous abstraction for coalescing particles. The
dynamics—particles moving, meeting, merging—is replaced by a static combinatorial
object: a forest of genealogy trees recording which particles merged, together with
ghost paths recording where each ghost traveled (Figure 5). This abstraction is the
performance.

Definition 2.9 (Genealogy tree). A genealogy for an heir H ∈ H records which
initial particles merged to form H. It is an oriented tree T embedded in D with:

• Leaves: starting positions xI for particles I that merge into H;
• Internal vertices: merger points where two or more particles merge and
continue as one;
• Root: the final position yH of the heir;
• Edges: directed paths in D—particle trajectories.

Each vertex v of T carries a label Iv: the union of the initial intervals of all particles
that have merged by v (an interval, by Proposition 2.11). When two initial particles
share a starting vertex, that vertex serves as both leaf and internal vertex; the
incoming paths have length zero.

Definition 2.10 (Genealogy forest). A genealogy forest is a collection T = {TH :
H ∈ H} of genealogies satisfying:

• Partition: Every initial particle belongs to exactly one tree;
• Non-intersection: Trees are vertex-disjoint.

Proposition 2.11 (Consecutivity). Under the planarity assumption (Definition 2.5),
the label Iv at each vertex is an interval: if particles A and C have both reached v,
then so has every particle B between them.

Proof. Suppose A and C both reach v, with starting positions xA ⪯ xC, and let B
be any particle with xA ⪯ xB ⪯ xC. By the partition property of the genealogy
forest, each of A, B, C lies on a full trajectory running from its leaf to the root of
its tree. We must show that B also reaches v.
Since A and C both pass through v, we have v ∈ A ∩ C; as the trees are
vertex-disjoint, A and C then lie in the same tree and have merged into a common
entity by v. The starting order xA ⪯ xB ⪯ xC places the three trajectories in the
configuration of the consecutive collision property (P2), which provides a vertex
w, no later than v, that lies on B and on A ∪ C. Vertex-disjointness again applies:
sharing the vertex w forces B into the same tree, merged with A or C by w; say
w ∈ A (the case w ∈ C is symmetric). Now w and v both lie on the directed path A,
hence are comparable in the time order ⋖; since ≤ extends ⋖, the relation w ≤ v
forces w ⋖ v or w = v. The portion of A from w onward therefore passes through v,
and B, having joined A at w, follows it to v.
Hence every particle between A and C reaches v, and the label Iv—the union of
the initial intervals of the particles merged by v—is an interval. □

Definition 2.12 (Ghost paths). For each ghost g ∈ G, let cg be the internal vertex
where junction g was dissolved—the unique earliest vertex v of the genealogy forest
whose label Iv contains g in its interior, so that the particles on both sides of g have
merged by v; a simultaneous multi-way merger may serve as cg for several ghosts

16 PIOTR ŚNIADY AND ÁKOS URBÁN

at once. The ghost path Γg is a directed path in D from cg to yg. Ghost paths are
non-interacting: they may pass through any vertices freely.

Definition 2.13 (Performance). A performance P consists of:
• a genealogy forest T ;
• a ghost path Γg for each ghost g ∈ G.
The weight of the performance is the product of all edge weights:

w(P) = ∏

tree edges e w(e) · ∏

g∈G w(Γg).

2.7. Ghost sign.

Definition 2.14 (Ghost sign). The ghost sign ε : G → {+1, −1} is:

εg =
 {+1 if yg ⪯ yheir(g) (ghost left of heir),
−1 if yheir(g) ⪯ yg (ghost right of heir).

In the special case yg = yheir(g), either sign may be chosen.

Two distinct orderings appear in our setup (Figure 6). Actors and final entities
carry labels—intervals and junctions ordered by ◁. But entities also have spatial
positions—vertices in the spacetime graph ordered by ≺.
In the classical LGV lemma, these two orderings coincide: the final entities admit
a single canonical left-to-right indexing, in which label order and spatial order agree.
The permutation π then has the same meaning whether interpreted as permuting
labels or as crossing paths.
With ghosts, this alignment breaks. Heirs keep a canonical order—they are sorted
by spatial position, matching their label order—but a ghost might end up to the left
or the right of its heir, regardless of their labels. The ghost sign ε captures precisely
this discrepancy.

2.8. Total weight. Given fixed initial and final state, the total weight

Z = ∑

P w(P)

is defined as the sum of weights over all performances with this prescribed initial
and final state. Our goal in this paper is to give a closed formula for Z.

3. The main result and an overview of its proof

3.1. The matrix. Fix the initial and the final state. Define the n × n matrix M
with: • rows indexed by particles I ∈ A (in label order);
• columns indexed by final entities f ∈ R (in min-order: each heir followed
by its attached ghosts);
• entries:

MI,f =
 



 W (xI → yH ) if f = H is an heir,

−[εg = −1] · W (xI → yg) if f = g is a ghost and I ◁ g,

[εg = +1] · W (xI → yg) if f = g is a ghost and I ▷ g;

see Figure 2 for an example.

COALESCING PARTICLE SYSTEMS 17

Remark 3.1 (Equivalence of notations). Under the min identification (Section 2.3),
the label order condition I ◁ g is equivalent to min I < min g. Since min I and
min g = g are the indexes of the row and column, respectively, this recovers the
coordinate formulation from the introduction (Section 1.3).

3.2. The theorem.

Theorem 3.2 (Coalescence formula with ghosts). Assume that the pair (X , Y)
is planar (Definition 2.5). The total weight of all coalescence performances with
prescribed initial and final state is the determinant

(3.1) Z = det M.

This generalizes Theorem 1.1.

Remark 3.3 (Edge cases of the boundary conditions). Three boundary configurations
refine the reading of Theorem 3.2. Weakly increasing heir positions: the ordering
assumption on heir positions (Section 2.5) is weak, so the theorem covers two heirs
sharing a final position. Such heirs would coalesce immediately, so the configuration
does not arise; on the matrix side their columns coincide, so both sides of (3.1) vanish.
A ghost coinciding with its heir: Definition 2.14 leaves εg free when yg = yheir(g), and
det M does not depend on the choice: passing from εg = −1 to εg = +1 amounts
to adding the heir column to the ghost column, a column operation. Coinciding
initial positions xi = xi+1: particles starting together coalesce immediately, so any
realizable pattern has a ghost at the junction between i and i+1. Unlike in the
non-colliding case, det M then need not vanish: the junction places the two particles
on opposite sides, so the two rows agree on every heir column but differ on that ghost
column, whose sign selects a different entry in each row; instantaneous coalescence
is a legitimate pattern of generally non-zero weight. (For a pattern without that
ghost the rows coincide and both sides vanish.)

3.3. Original proof of the non-colliding case. The proof which we provide for
Theorem 3.2 is adapted from the original papers [KM59; Lin73; GV85; Ste90] which
concerned the special case of calculating the probability (respectively, weight) of
n particles (respectively, paths) reaching specified final positions in a collision-free
way. We shall recall the original proof in a compressed form.
The key idea was to consider the Leibniz expansion of the determinant det M as
a sum over bijections π between the initial and the final positions. Any contributing
product of matrix M entries (each counting weights of single-particle trajectories)
can be interpreted as a sum over tuples of trajectories P = (P1, . . . , Pn) each
connecting specific initial and (permuted by π) final positions. In other words, the
determinant det M is expressed as a signed sum over pairs (π, P). Since such pairs
play a prominent role in this paper, we call them castings (Definition 4.1).
The goal of the classic proof is to evaluate this signed sum by cancellation. The
planarity assumption guarantees that a trajectory tuple P without crossings can
occur only for the identity permutation π = id, which the determinant expansion
counts with the positive sign sgn π = +1.
The crossing tuples are removed by a sign-reversing involution on the set of
castings: it pairs each crossing casting (π, P) with another crossing casting (π′, P
′)
of equal weight w(P) = w(P′) but opposite sign sgn π = − sgn π′, so that the
two contributions cancel. After all crossing castings cancel in such pairs, only the
non-crossing tuples survive, each carrying π = id and positive sign. The determinant

18 PIOTR ŚNIADY AND ÁKOS URBÁN

det M therefore equals the total weight of non-crossing trajectory tuples, which is
the desired count.

3.4. What goes wrong for coalescing particles. The overall strategy survives:
as in Section 3.3, we express the determinant det M as a signed sum over castings
and construct a sign-reversing involution which matches failed castings in pairs,
so that their contributions cancel. Two features of the coalescing setting, however,
force adaptations—one minor, one essential.

3.4.1. A minor difference: ε-candidate castings. The first difference concerns which
bijections π contribute. In the classical setting the matrix has no forced zeros, so
every permutation π can appear in the Leibniz expansion. Our matrix, by contrast,
has structural zeros: each ghost column vanishes except on the side selected by its
sign, so a bijection contributes only when it assigns every ghost an actor on the
correct side. We call a casting whose bijection meets this condition an ε-candidate
casting (Definition 4.2), and restrict attention to these; see Section 4.2.

3.4.2. The essential difference: performances are not castings. The two sides of
(3.1) count different kinds of objects. The left-hand side counts performances. A
performance is role-based: at each binary coalescence two particles arrive, meet,
and disappear, replaced by an heir and a ghost that emerge from the junction.
Nothing threads what enters the event to what leaves it. This description says
nothing about the identities behind the heir and the ghost—only that the coalescence
produced one of each. The discontinuity is reflected in Figure 1: the line styles
entering the coalescence differ from those leaving it, emphasizing that identities
do not persist across the event. In theatrical terms, the script fixes where each
character stands in the final scene, but not which actor plays which character.
The right-hand side, det M , counts a different kind of object. As in the classical
argument (Section 3.3), its Leibniz expansion is a signed sum over castings (π, P);
but a casting is actor-based, tracking each particle’s complete trajectory, so in
Figure 8 the line styles persist through the coalescence, recording who went where.
The proof bridges the two descriptions. It establishes a weight-preserving bijection
between performances and the successful castings—those that reproduce a valid
coalescence pattern (Definition 6.2)—while the remaining failed castings cancel in
signed pairs (Figure 9). The remainder of this overview describes the machinery
that realizes this bijection and cancellation.

3.5. Adapting the proof. Two maps bridge the two descriptions. Attribution
(Section 5) turns a performance into a casting by tracking which actor ends where;
it never fails, is injective, and its output is always an ε-candidate casting (Propo-
sition 5.9). Rehearsal (Section 6) tests the converse: scanning the crossings of an
ε-candidate casting in chronological order, it either processes every crossing as a
coalescence and reproduces a performance—the casting is successful —or halts at
a spurious crossing and reports its failure pair —the casting is failed. The failed
castings cancel in signed pairs: the segment swap (Section 8.1), applied at the
failure pair, yields the involution ι (Definition 8.4) whose fixed points are exactly
the successful castings (Theorem 8.5), and these are in weight-preserving bijection
with performances (Proposition 7.3). Sections 4 to 9 develop these components in
turn.
 COALESCING PARTICLE SYSTEMS 19

x

t

T
 c

x1 x2 x3

yH yH′ yg
 particle 1
→ ghost at yg

particle 2
→ heir 1 at yH

particle 3
→ heir 2 at yH′

Figure 8. Successful casting: actor-based view of a per-
formance. This is a casting—a bijection π from actors to roles
together with the paths realizing it—but it also displays a perfor-
mance: the same coalescence as Figure 1, now with each actor’s
identity tracked through the crossing. Here π sends particle 1
(solid) to the ghost at yg, particle 2 (double) to the heir at yH , and
particle 3 (zigzag) to the heir at yH ′; the line styles persist past c,
revealing who went where. The casting is successful : the crossing
at c is a valid coalescence—one of the two meeting paths is des-
tined for the ghost, so the crossing is not spurious—and rehearsal
reconstructs exactly the performance of Figure 1.

4. Expanding the determinant

Throughout the proof, we fix a final state F (Section 2.5): the ghost set G, the
heir set H, and final positions yf for each f ∈ R. The total weight Z = ZF counts
performances for F. From Section 5 onward we also assume, as in Theorem 3.2,
that the pair (X , Y) is planar (Definition 2.5); the present section is planarity-free.
Section 3 named the two sides of (3.1) as performances and castings; this section
makes the casting side precise and equips each casting with the right sign. The
Leibniz formula offers the usual permutation sign sgn π, but that sign is bound to
the arbitrary order we placed on the columns; we replace it by the ghost-adjusted
sign sgnε(π), read off the label order and the ghost signs alone—the intrinsic data
of the final state, blind to any left–right convention. The two constructions combine
in one clean identity, the restricted Leibniz expansion (Proposition 4.4): det M is
the sgnε-signed sum over ε-candidate castings.

4.1. The Leibniz expansion. The Leibniz formula expands the determinant as a
sum over bijections π : A → R from actors to roles:

det M = ∑

π sgn π ∏

I∈A MI,π(I).

Each matrix entry MI,f is either a weight W (xI → yf ) (for heir columns) or
±[εg = ±1] · W (xI → yg) (for ghost columns). Expanding:

det M = ∑

π sgn π ∑

P (sign factors) · w(P),

where P = {PI }I∈A is a family of paths with PI running from xI to yπ(I).

20 PIOTR ŚNIADY AND ÁKOS URBÁN

x

t

T
 !c

x1 x2 x3

yH yH′ yg particle 1
→ heir 1 at yH

particle 2
→ heir 2 at yH′

particle 3
→ ghost at yg

Figure 9. Failed casting: a spurious crossing. The same
endpoints as Figure 8, realized by different paths and a different
bijection: here π sends particle 1 to the heir at yH , particle 2
to the heir at yH ′, and particle 3 to the ghost at yg. Scanning
crossings in chronological order, rehearsal reaches c, where the
paths of particles 1 and 2 meet; but neither is destined for the ghost
role—both end at heir positions—so the crossing cannot be read as
a coalescence. It is spurious. Rehearsal therefore terminates and
produces no performance: its only output in this failed case is the
spurious crossing c together with the two actors that triggered it,
particles 1 and 2. Segment swap takes exactly this data, exchanging
the two actors’ path suffixes at c to pair the failed casting with a
sign-opposite partner (Section 8.1).

Definition 4.1 (Casting). A casting (π, P) consists of:

• A bijection π : A → R from actors (initial particles) to roles (final entities);
• A path family P = {PI }I∈A where PI goes from xI to yπ(I).

The weight is the product of the path weights,

w(P) = ∏

I w(PI ).

The sign a casting carries is the ghost-adjusted sign defined below (Equation (4.1)),
not the bare permutation sign.

Crucially, the path-family layer is pure geometry: the paths are non-interacting.
They may cross freely—a crossing is simply a point where two paths share a vertex,
with no physical consequence. There is no coalescence physics yet: the determinant
gives us n non-interacting walkers, not an interacting particle system.

4.2. ε-candidate bijections. Each ghost column carries forced zeros, and these
decide which bijections contribute. A ghost entry MI,g is non-zero only when two
conditions align. The first is geometric: through the bracket [εg = ±1], the ghost
sign selects one side of the junction g and zeros every entry on the other side. The
second is combinatorial : which side a given row lies on is fixed by the label relation
between the row’s interval I and the junction g. A term in the Leibniz expansion
therefore survives only if, for every ghost, the performer π−1(g)—the actor that π

COALESCING PARTICLE SYSTEMS 21

casts in the role g—lands on the side left non-zero by the sign. We record this as a
condition on π.

Definition 4.2 (ε-candidate bijection). A bijection π : A → R is an ε-candidate if,
for every ghost g ∈ G, the performer π−1(g) falls on the side of the junction dictated
by the ghost sign:

g ◁ π−1(g) if εg = +1, π−1(g) ◁ g if εg = −1

(equivalently, g ◁ π−1(g) ⇐⇒ εg = +1). We write ΠF for the set of ε-candidate
bijections.

The ghost sign εg compares the ghost’s final spatial position to its heir’s; ε-
candidacy is the matching condition on the performer’s interval label relative to the
junction.
The ghost-column brackets select exactly the ε-candidate bijections: each ghost
column vanishes off its sign-selected side, so only the terms with π ∈ ΠF survive.

4.3. The ghost-adjusted sign.

4.3.1. Factoring out the ghost signs. The ε-candidacy condition depends only on π,
not on the paths P, so the determinant expansion splits into a sign and a weight.
Fix an ε-candidate π. In each heir column the selected entry is W (xI → yH ); in
each ghost column ε-candidacy places the performer on the side left non-zero by
the bracket [εg = ±1], which contributes the factor εg, so the selected entry is
εg W (xI → yg). Hence

∏

I∈A MI,π(I) = (∏

g∈G εg) ∏

I∈A W (xI → yπ(I)),

and the Leibniz expansion gathers each casting’s permutation sign and these ghost
signs into a single sign—the one the determinant attaches to the casting. We define
that sign without reference to any order on the columns.

4.3.2. The tournament ◁ε. On the final entities, the label order ◁ is only partial:
by Section 2.3 its only incomparable pairs are an heir H and a ghost g lying in its
interior (so H = heir(g)). We extend it to a total relation ◁ε by deciding exactly
those incomparable pairs from the side on which the ghost comes to rest relative to
its heir,
 g ◁ε H if εg = −1, H ◁ε g if εg = +1,

while f ◁ε f ′ agrees with f ◁ f ′ on every comparable pair. This placement runs
against the spatial picture: a ghost coming to rest to the left of its heir (εg = +1)
is ordered after it in ◁ε, while a ghost resting to the right (εg = −1) is ordered
before it—each ghost sits, in ◁ε, on the side of its heir opposite to where it comes to
rest spatially. The ghost sign εg enters only as a name for “which side”; which side
one calls positive will not matter. Every pair of roles is now comparable, so ◁ε is
total; it need not, however, be transitive—◁ε is a tournament, not a linear order
(Remark 4.5).

22 PIOTR ŚNIADY AND ÁKOS URBÁN

4.3.3. The sign as an inversion count. Counting inversions needs only that every
pair is comparable, not transitivity. For a bijection π, an inversion is a pair of
actors I ◁ I ′ whose assigned roles ◁ε reverses, that is, with π(I ′) ◁ε π(I); write N (π)
for their number, N (π) = #{ I ◁ I ′ : π(I ′) ◁ε π(I) }.
Most are ordinary ◁-inversions between comparable roles. The rest come at most one
per ghost: g contributes an inversion exactly when its performer and resting place
fall on the same side—both left, or both right—of its heir’s performer and of the
heir. One may read such an inversion as a placement gone wrong; the inversion-free
placement is the far-side principle that attribution will follow (Section 5).
The ghost-adjusted sign of π is then

(4.1) sgnε(π) := (−1)
N (π).

Lemma 4.3 (Evaluating the ghost-adjusted sign). For every bijection π : A → R,

sgnε(π) = sgn π ∏

g∈G εg.

Proof. Let Nmin(π) = #{I ◁ I ′ : min π(I ′) < min π(I)} count the inversions of π
in the min-order, so that sgn π = (−1)Nmin(π). The min-order is a linear extension
of ◁, so ◁ε and the min-order agree on every comparable pair; they differ only
on the incomparable pairs, and there only for a ghost g with εg = −1, where
g ◁ε heir(g) while g > min heir(g) places g after its heir. Each such ghost flips
exactly one inversion, so N (π) ≡ Nmin(π) + #{g : εg = −1} (mod 2). Hence
sgnε(π) = (−1)N (π) = (−1)
Nmin(π) ∏
g εg = sgn π ∏
g εg. □

4.3.4. The restricted Leibniz expansion.

Proposition 4.4 (Restricted Leibniz expansion). For fixed initial and final state,
the determinant is a signed sum over ε-candidate castings, with the ghost-column
signs absorbed into the ghost-adjusted sign:

(4.2) det M = ∑

π∈ΠF sgnε(π) ∏

I∈A W (xI → yπ(I)) = ∑

(π,P)
π∈ΠF
 sgnε(π) · w(P).

Proof. The Leibniz formula sums over all bijections π, but each ghost column vanishes
off its sign-selected side, so only the ε-candidates survive (Definition 4.2). For an
ε-candidate the column product factors as ∏

I MI,π(I) = (∏

g εg) ∏

I W (xI → yπ(I)),
and sgn π · ∏

g εg = sgnε(π) by Lemma 4.3; expanding each weight W as a sum over
paths turns the product into ∑

P w(P). □

This identity is the starting point for the rest of the proof, which evaluates the
signed sum by cancellation.

Remark 4.5 (A tournament, not an order). The failure of transitivity is concrete. For
the heir H = [1, 4) carrying ghosts 2, 3 with ε2 = +1 and ε3 = −1, the comparisons
3 ◁ε H ◁ε 2 ◁ε 3 close a cycle, so ◁ε is a genuine tournament with no underlying
linear order. No linear order of the roles reproduces sgnε; what is well defined is
the inversion count N (π), which tallies pairs and needs no transitivity, and with
it the sign (4.1). This is why one cannot reorder the columns to remove the ghost
signs, and why the min-order of the introduction is only a device for writing the
determinant down. That device costs symmetry: min selects the left endpoint of

COALESCING PARTICLE SYSTEMS 23

each interval, a left–right choice, whereas ◁ε is built only from the label order and
the side each ghost rests on, which simply reverse when the line is reflected. The
restricted Leibniz expansion is in this sense even-handed—it privileges neither end
of the line, naming no positive side—where the determinant, to gain a compact
formula, had to.

Finally, sgnε inherits the one property of the permutation sign that the sign-
reversing involution of Section 8 relies on.

Corollary 4.6 (Transposition rule). Composing π with a transposition negates the
ghost-adjusted sign:
 sgnε((I J) ◦ π) = − sgnε(π).

Proof. Since ∏

g εg is a constant, Lemma 4.3 gives sgnε = sgn · ∏
g εg, and a trans-
position negates sgn. □

5. Attribution: performance to casting

A performance fixes the genealogy of the coalescences and the ghost paths, but
it does not record which initial actor ends up at which final entity. Attribution
supplies that missing correspondence—the casting underlying the performance.
Concretely, attribution follows each initial particle through the performance one
coalescence at a time. At each binary coalescence two incoming particles meet; the
rule below sends one onward as the heir and the other to the ghost just created.
Carrying out this rule at every coalescence both names the final entity each particle
reaches—the bijection π that the casting carries—and glues, in parallel, the path
each particle travels. We describe the rule at a single coalescence, iterate it to define
attribution and read off that it yields an ε-candidate bijection.

5.1. The two-particle case. We first describe what happens at a single coalescence
of two particles, then explain how to combine these local operations.
By consecutivity (Proposition 2.11), coalescing particles are always adjacent
intervals. Write I − and I + for the left and right incoming intervals at a coalescence,
H for the heir, and g for the ghost. (In interval notation: I − = [a, g), I + = [g, c),
H = [a, c).)
Four path segments meet at the coalescence vertex (Figures 10a and 11a): two
incoming and two outgoing (one to the ghost position yg, one continuing as the heir
toward further coalescences or the final position). The far-side principle connects
each incoming particle to the outgoing segment on the opposite side: a particle
arriving from the left interval I − leaves to the right, and one arriving from the right
interval I + leaves to the left.
The ghost sign εg encodes whether the ghost ends left or right of the heir,
determining the gluing (Figures 10b and 11b):

• εg = +1 (ghost left of heir): the right interval I + becomes the ghost;
• εg = −1 (ghost right of heir): the left interval I − becomes the ghost.

This defines a local bijection λ : {I −, I +} → {H, g} (Figures 10c and 11c). The two
cases look asymmetric, but each is the inversion-free choice for the tournament ◁ε:
the far-side principle draws the ghost from the side of its heir opposite where it
comes to rest, the placement that contributes no ◁ε-inversion at g. So the local

24 PIOTR ŚNIADY AND ÁKOS URBÁN

X

Y

I − I +

Hg
 (a)
 X

Y

I − I +

Hg
 (b)
 a g c

a g c

I − I +

H

g

(c)

Figure 10. Two-particle coalescence, case εg = +1: ghost
left of heir. (a) Schema: four distinct styles indicate entities do
not persist past coalescence; the dashed line shows the ghost path.
(b) Attribution via path gluing: the far-side principle routes the
particle from I − to yH (solid), while the particle from I + continues
as a ghost to yg (dashed). Following paths determines the bijection.
(c) Bijection λ+: I − ↦→ H, I + ↦→ g. The ghost is supplied from the
far side, so the bijection is inversion-free: sgnε λ+ = +1.

X

Y

I − I +

H g

(a)
 X

Y

I − I +

H g

(b)
 a g c

a g c

I − I +

H

g

(c)

Figure 11. Two-particle coalescence, case εg = −1: ghost
right of heir. (a) Schema: four distinct styles indicate entities do
not persist past coalescence; the dashed line shows the ghost path.
(b) Attribution via path gluing: the far-side principle routes the
particle from I + to yH (double line), while the particle from I −

continues as a ghost to yg (dashed). Following paths determines
the bijection. (c) Bijection λ−: I − ↦→ g, I + ↦→ H. Again the ghost
comes from the far side, so sgnε λ− = +1.

bijection counts zero inversions and, by (4.1), a single coalescence is ghost-adjusted-
sign-neutral either way: sgnε(λ) = +1.

Across all the coalescences these neutral factors multiply to sgnε(π) = +1 for the
whole casting (Proposition 5.10).

COALESCING PARTICLE SYSTEMS 25

5.2. From local to global.

5.2.1. The attribution map.

Definition 5.1 (Attribution). Attribution constructs a casting (π, P) from a per-
formance by applying the local gluing rule at each coalescence.

We describe attribution assuming every coalescence is binary; Section 5.2.2
reduces the general case to this one. For each initial particle I, follow its path
through the binary coalescences, applying the local gluing rule at each. The path
terminates either at an heir position or at a ghost position. This process produces:

• the endpoint π(I) (the final entity where I ends up);
• the glued path PI from xI to yπ(I).

Iterating over all initial particles yields the output of attribution: a casting
(π, (PI )I∈A).

Example 5.2 (Single coalescence: Figure 1). In Figure 1, particles I1 and I2 coalesce
at c. The ghost ends at yg > yH , so εg = −1 (ghost right of heir). By the far-
side principle, the left particle I1 becomes the ghost. The output is the casting
(π, (PI1, PI2, PI3 )) where:

• PI1: from x1 to c, then to yg; endpoint π(I1) = g;
• PI2: from x2 to c, then to yH ; endpoint π(I2) = H;
• PI3: from x3 to yH ′ (no coalescence); endpoint π(I3) = H ′.

See Figure 8.

5.2.2. High-indegree vertices. It remains to lift the binary assumption. When r > 2
intervals meet at one vertex they form a consecutive run J1, . . . , Jr (consecutivity);
process it by nested pairings in label order, ((J1 J2) J3) · · · Jr, each pairing producing
one ghost and a continuing heir, which completes the definition of attribution. This
left-to-right order is also the one rehearsal uses (Section 6.1), so attribution and
rehearsal agree.

Example 5.3 (Full coalescence: Figures 12 and 13). Three particles I1, I2, I3 all
coalesce into one heir H = [1, 4), with ghost signs ε2 = +1 (ghost 2 left of heir) and
ε3 = −1 (ghost 3 right of heir).
In Figure 12, junction 3 fires first: I2 and I3 meet. Since ε3 = −1, the left particle
I2 becomes the ghost. Next, junction 2 fires: I1 meets the merged interval (carried
by I3). Since ε2 = +1, the right particle (I3) becomes the ghost. The output is the
casting (π1, (PI1, PI2, PI3 )):

• PI1: from x1 to junction 2, then to yH ; endpoint π1(I1) = H;
• PI2: from x2 to junction 3, then to y3; endpoint π1(I2) = 3;
• PI3: from x3 to junction 3, to junction 2, then to y2; endpoint π1(I3) = 2.

In Figure 13, the same final state arises from a different coalescence order
(junction 2 fires first), producing a different casting (π2, (P ′
I1, P ′
I2, P ′
I3 )) with π2(I1) =
3, π2(I2) = 2, π2(I3) = H.

26 PIOTR ŚNIADY AND ÁKOS URBÁN

X

Y

I1 I2 I3

3

2

H2 3

(a)
 1 2 3 4

1 2 3 4

I1 I2 I3

H

2 3

(b)

Figure 12. Full coalescence, bijection π1: junction 3 fires
first. Three particles coalesce into one heir H = [1, 4), creating
ghosts at junctions 2 and 3. (a) Attribution: following each path
through all collisions determines the bijection. Junction 3 fires
first (I2 and I3 meet), then junction 2 (I1 meets the merged [2, 4)).
(b) Bijection π1: I1 ↦→ H, I2 ↦→ 3, I3 ↦→ 2. A successful casting
is positive; here sgnε π1 = +1. Line styles: I1 solid, I2 double,
I3 zigzag; dotted = ghost.
 X

Y

I1 I2 I3

2
 3

2 3H

(a)
 1 2 3 4

1 2 3 4

I1 I2 I3

H

2 3

(b)

Figure 13. Full coalescence, bijection π2: junction 2 fires
first. Same final state as Figure 12 (line styles as there), different
collision order. (a) Attribution: junction 2 fires first (I1 and I2
meet), then junction 3 (I3 joins). Following paths yields a different
bijection. (b) Bijection π2: I1 ↦→ 3, I2 ↦→ 2, I3 ↦→ H. Both π1 and
π2 are successful castings for the same final state, hence positive:
sgnε π2 = +1 as well.

5.3. Assignments: a bookkeeping device. To recast attribution—and, later, to
run rehearsal (Section 6)—we record one compact device. An assignment captures a
coalescence in progress: a partition of the initial particles into their current clusters,
paired with a bijection matching actors to the resulting entities. This is the actor-
to-entity language of a casting’s bijection π (Definition 4.1), with all spacetime and

COALESCING PARTICLE SYSTEMS 27

path weights forgotten. Attribution reaches, at the final state, an assignment whose
bijection is exactly that π; the construction below builds it one coalescence at a
time, starting from the identity assignment.

5.3.1. Partitions.

Definition 5.4 (Partition). A partition P records a coalescence pattern by:

• its active intervals Active(P )—a list of half-open intervals whose disjoint
union is [1, n + 1), recording the current clusters of initial particles;
• its ghost junctions G(P ) ⊆ J , recording which interior junctions have been
freed by past coalescences.

The entities of P are Active(P ) ∪ G(P ). (We reserve the names heir and H for
the final state; the active intervals of a general partition are transient clusters.)
Two extremal partitions appear repeatedly: the initial partition, whose active
intervals are the unit intervals I1, . . . , In and whose ghost set is empty; and the final-
state partition PF , whose active intervals are the heir intervals H from Section 2.5
and whose ghost set is G. The entities of PF are exactly the roles R, so the notations
Active(PF ) = H and G(PF ) = G are consistent.
A coalescence merges two adjacent active intervals into their union and adds the
junction between them to the ghost set; all other intervals and ghosts are unchanged.
Every partition in the proof arises this way, from the initial partition; in particular
every junction lying strictly inside an active interval is a ghost—a boundary dissolved
by an earlier merge.

5.3.2. Assignments and diagonality.

Definition 5.5 (Assignment). An assignment is a pair π = (P, π) where P is a
partition and π : A → Active(P ) ∪ G(P )

is a bijection from actors to entities of P . We write π both for the pair and for the
bijection; the underlying partition is recovered as Pπ when needed.

Definition 5.6 (Diagonal assignment). An assignment π = (P, π) is diagonal if,
for every active interval I = [a, b) of P , the bijection π restricts to a bijection

{ actors with label in [a, b) } ∼
−−→ {I} ∪ { g ∈ G(P ) : a < g < b }

from the b − a actors labelled in I onto I together with the ghost junctions interior
to I. The heir actor of I under π is the unique actor sent to I, namely π−1(I);
every other actor labelled in I performs an interior ghost.

The identity assignment pairs the initial partition with the bijection Ij ↦→ Ij.
It is trivially diagonal: each unit interval contains a single actor and no interior
junctions, so the required bijection sends that lone actor to its interval. A bijection
π : A → R pairs with the final-state partition PF to give an assignment π = (PF , π);
this is how the ε-candidate bijections of Definition 4.2 appear as assignments at PF .
Diagonality thus tiles each active interval: the b − a actors labelled in I = [a, b)
are partitioned into its heir actor and the performers π−1(g′) of its b − a − 1 interior
ghosts (every junction interior to an active interval is a ghost, by the partition
structure above). The rigidity argument of Section 6.3.2 uses this tiling directly.

28 PIOTR ŚNIADY AND ÁKOS URBÁN

5.3.3. The assignment poset.

Definition 5.7 (The assignment preorder). For assignments π and π′, write π ≤ π′

if: (i) the partition Pπ′ is coarser than Pπ (equivalently, G(Pπ) ⊆ G(Pπ′));
(ii) for every ghost g ∈ G(Pπ), π′−1(g) = π−1(g).

Reading: π′ extends π by further coalescences without revising the performer
π−1(g) of any ghost π already has. The identity assignment is the minimum element;
every assignment lies above it. Strictly, ≤ is a preorder—antisymmetry can fail for
assignments that differ only on their active-interval images—though on diagonal
assignments it is a genuine partial order. No argument below uses antisymmetry,
and we keep the customary shorthand assignment poset.

5.4. Attribution as a chain.

Proposition 5.8 (Attribution as a chain of diagonal assignments). Attribution
produces an increasing chain in the assignment poset, from the identity assignment
to the diagonal assignment (PF , π), advancing by one binary coalescence per step.
Every assignment in the chain is diagonal, and the bijection of the final assignment
is the bijection π that the casting carries (Definition 4.1).

Proof. This is immediate from the construction above. Each binary coalescence
merges two adjacent active intervals I − and I + into H and frees the junction g
between them; the far-side principle makes one of the two incoming actors the
performer of the new ghost g and lets the other carry the merged interval, so the
actors labelled in H are again in bijection with H and its interior ghosts—the
assignment stays diagonal. The step also moves up the poset (Definition 5.7): it only
coarsens the partition and adds the new ghost, while every actor already mapped to
a ghost keeps that image, so the performers already assigned are preserved. □

5.5. ε-candidacy emerges. The chain exposes two properties of the casting, one
read off each coalescence. The first is ε-candidacy. The right-hand side of the
formula is the restricted Leibniz expansion (Proposition 4.4), a sum over ε-candidate
castings; for the casting attribution produces to appear there at all—rather than be
silently absent—its bijection must be an ε-candidate. It is.

Proposition 5.9 (Attribution yields an ε-candidate). Let C = (π, P) be the casting
that attribution produces from a performance. Then π is an ε-candidate.

Proof. Fix a ghost g, created when the adjacent intervals I − = [a, g) and I + = [g, c)
merge. The interval [a, c) is assembled from the initial actors Ia, . . . , Ic−1, so the
particle arriving at this coalescence along I − traces back to an initial actor whose
label lies in [a, g), and the one arriving along I + to an initial actor whose label lies
in [g, c). The far-side principle hands the ghost role to one of the two incoming
intervals according to the ghost sign, and the ghost is performed by that interval’s
incoming particle.
If εg = −1 (ghost right of heir), the ghost comes from the left interval I − = [a, g),
so its performer π−1(g) has label in [a, g); thus π−1(g) ◁ g, the side Definition 4.2
requires when εg = −1. If εg = +1 (ghost left of heir), the ghost comes from the
right interval I + = [g, c), so π−1(g) has label in [g, c); thus g ◁ π−1(g), the side
required when εg = +1. In both cases the performer falls on the side the ghost sign
dictates, so π is an ε-candidate. □

COALESCING PARTICLE SYSTEMS 29

5.6. Positivity. The second property is the sign. ε-candidacy reads, off each
coalescence, which side the ghost is drawn from; the sign is the companion reading—
each coalescence moves the inversion count only by an even amount, so the count
stays even and the casting is positive.

Proposition 5.10 (Attribution yields a positive casting). The casting (π, P) that
attribution produces from a performance has ghost-adjusted sign sgnε(π) = +1.

We prove this at the end of the subsection, after isolating its one nontrivial step
(Lemma 5.11). The proof tracks the inversion count N of (4.1) along the chain,
defined for every assignment σ = (P, ρ), not only the final casting: ◁ε extends to
the entities of P by the same rule used on the final roles—active intervals play the
part of heirs, and an active interval and a ghost in its interior are ordered by the
ghost’s sign—and N (σ) = #{ I ◁ I ′ : ρ(I ′) ◁ε ρ(I) }.

Lemma 5.11 (A coalescence preserves inversion parity). Let σ → σ′ be one step of
the attribution chain—a coalescence merging adjacent active intervals L = [a, g) and
R = [g, c) into H = [a, c) and creating the ghost g. Then N (σ′) ≡ N (σ) (mod 2).

Proof. The actors are the fixed unit intervals, and the step changes only the images
of the two actors pL = σ−1(L) and pR = σ−1(R), sending them to the new entities
H and g; every other actor keeps its image, and the ◁ε-order among all surviving
entities is unchanged. So N can change only through pairs of actors meeting
{pL, pR}: the pair (pL, pR), and the two pairs each other actor forms with pL and
pR.
Write [ · ] ∈ {0, 1} for a truth value. A pair {x, p} is an inversion iff its label order
and the ◁ε-order of its images disagree, that is, iff [x ◁ p] + [σ(x) ◁ε σ(p)] is odd.

The pair (pL, pR). The far-side principle is the inversion-free choice for ◁ε (Section 5.1;
the bijections λ± are drawn in Figures 10c and 11c), so σ′(pL) ◁ε σ′(pR) holds just
as σ(pL) = L ◁ε R = σ(pR); with the label order of pL, pR fixed, the pair keeps its
inversion status.

The pairs through another actor x. Let e = σ(x) = σ′(x) be its unchanged image.
Write P (ρ) for the number of inversions among {x, pL} and {x, pR} under an
assignment ρ. By the rule above,

P (ρ) ≡ [x ◁ pL] + [x ◁ pR] + [e ◁ε ρ(pL)] + [e ◁ε ρ(pR)] (mod 2).

Here P (σ) is the count before the step, with {σ(pL), σ(pR)} = {L, R}, and P (σ′)
the count after, with {σ′(pL), σ′(pR)} = {H, g}; the label terms and the image
e = σ(x) = σ′(x) are common to both. So the change across the step is

P (σ′) − P (σ) ≡ [e ◁ε L] + [e ◁ε R] + [e ◁ε H] + [e ◁ε g] (mod 2),

which is zero: for every entity e,

(5.1) [e ◁ε L] + [e ◁ε R] ≡ [e ◁ε H] + [e ◁ε g] (mod 2).

Indeed, if e lies to one ◁ε-side of the block [a, c), then L, R, H, g are all on the
other side of e, and both sides of (5.1) count 0 or 2. Otherwise e is a ghost
inside L or R; then [e ◁ε H] = [e ◁ε (its container)], both settled by εe, and
[e ◁ε g] = [e ◁ε (the other interval)], both settled by position—so (5.1) holds term
by term.
Hence every actor x ̸= pL, pR contributes an even change to N , and (pL, pR)
contributes none: N (σ′) ≡ N (σ) (mod 2). □

30 PIOTR ŚNIADY AND ÁKOS URBÁN

Proof of Proposition 5.10. Attribution builds π as a chain of assignments from the
identity assignment up to (PF , π) (Proposition 5.8). At the identity assignment the
entities are the unit intervals, ◁ε restricts to the linear label order, and Ij ↦→ Ij has
no inversions, so N = 0. Each coalescence preserves the parity of N (Lemma 5.11),
so N (π) is even and sgnε(π) = (−1)N (π) = +1. □

ε-candidacy and positivity together fix attribution’s role in the proof: the re-
stricted Leibniz expansion counts each performance exactly once and with sign +1,
so every object we want is present, on the positive side. What they do not say is
that the expansion counts nothing else: its ε-candidate sum also carries castings that
attribution never produces. Sorting those out is the work that remains—rehearsal
(Section 6) and the sign-reversing involution it feeds (Section 8).

6. Rehearsal

Rehearsal reverses attribution: from a casting it tries to recover a performance that
attribution would turn into that casting. The casting’s bijection π is fixed in advance,
and rehearsal rebuilds the performance one coalescence at a time (Section 6.1). The
run succeeds when a performance is recovered and fails at a spurious crossing—a
coalescence the reconstruction cannot carry out. This success/failure split is what
the sign-reversing involution (Section 8) exploits: the failed castings cancel in signed
pairs, the successful ones survive.

6.1. The rehearsal algorithm.

6.1.1. Aspiration and reality. Rehearsal is read most easily as a climb in the assign-
ment poset (Definition 5.7). The input is an ε-candidate casting; its bijection π,
viewed as the assignment (PF , π) (Definition 5.5), sits at the top of the climb. We
call it the aspiration: it records, for each actor I, the entity π(I) that I should
reach. Starting from the identity assignment, rehearsal builds a second assignment
upward toward it, one binary coalescence at a time:
• σ: the reality, a running diagonal assignment (Definition 5.6) initialized
as the identity assignment and updated at each accepted coalescence; its
partition Pσ coarsens by one binary merge per step, and its bijection records
the performer of each ghost fired so far;
• P: the performance under construction (coalescence events and ghost paths
recorded so far).
This is the climb of Proposition 5.8 with the two sides exchanged. Attribution
built σ freely and let π emerge as its final value; rehearsal holds π fixed and asks
whether σ can reach it. Throughout the run the reality stays below the aspiration,
σ ≤ π (Lemma 6.4). So σ never overshoots π: the run either reaches π (success) or
halts earlier at a spurious crossing (failure). A third conceivable outcome—the run
completing without failure, no crossing left to process, yet with σ < π—is ruled out
under planarity (Section 6.3).

The representative (or survivor ) of an active interval J is the actor σ−1(J) flowing
as it—the one actor of J not yet consumed by a coalescence. Under the casting it
aspires to the entity π(σ−1(J)). The σ-active actors are the representatives of the
active intervals of Pσ.
 COALESCING PARTICLE SYSTEMS 31

A crossing of two adjacent active intervals I − ◁ I + at junction g forces their
merge; the only freedom is how σ updates its bijection, and the requirement
σ ≤ π pins it. The two gluings of the two-particle case are both available—λ−
drawing the ghost from I −, λ+ from I + (Figures 10 and 11)—but σ ≤ π admits
only the one whose ghost performer is π−1(g). Since π−1(g) is a single actor, at
most one of the two representatives can be it: there is one valid update when
π−1(g) ∈ {σ−1(I −), σ−1(I +)}, and none at all otherwise—the third outcome, absent
from attribution. Several intervals meeting at one vertex are processed as successive
binary crossings, in label order, matching attribution’s nested pairing (Section 5.2.2);
the binary description below loses no generality.

Definition 6.1 (Valid and spurious crossings). A crossing between adjacent active
intervals I − and I + at junction g is valid if one of them is destined for the ghost
role at g—that is, if π(σ−1(I −)) = g or π(σ−1(I +)) = g, so that one of the two
representatives aspires to become ghost g. Otherwise the crossing is spurious.

A valid crossing becomes a coalescence: one path exits as a ghost path, the other
represents the merged interval, and the system shrinks. A spurious crossing causes
rehearsal to halt: rehearsal terminates with failure, reporting the failure pair (I, J)
at the crossing vertex v. Rehearsal terminates successfully when no crossings remain.

6.1.2. The procedure. Rehearsal reads the casting one vertex at a time, in the linear
order ≤ (Definition 2.1): it passes through the vertices visited by at most one
σ-active representative and acts only at crossings, firing a coalescence at each valid
one and halting at the first spurious one.

Input: An ε-candidate casting (π, P), where π : A → R is an ε-candidate bijection
(fixed throughout).

Rehearsal.
(S1) Initialize: reality σ ← the identity assignment (the bottom of the poset), and
P ← the empty performance.
(S2) Visit the vertices v of the DAG in the linear order ≤ (Definition 2.1). At most
vertices fewer than two σ-active representatives meet, and nothing happens—
the sweep passes through. Otherwise, while two or more σ-active representa-
tives meet at v:
(a) Take the crossing pair: the active intervals of Pσ whose representatives
reach v form a contiguous block, by consecutivity (Section 6.2.2); let
I − ◁ I + be its leftmost adjacent pair, with junction g and representative
paths P = Pσ−1(I −) and Q = Pσ−1(I +) read from the casting. Let
I = σ−1(I −) and J = σ−1(I +) be the two representatives.
(b) Test: Is g ∈ {π(I), π(J)}? (Does one of the two representatives aspire to
ghost g?)
• If no, the crossing is spurious: rehearsal terminates (failure), re-
porting the failure pair (I, J) at vertex v.
• If yes (valid crossing)—record a coalescence. One of I, J aspires
to g (π(·) = g)—the ghost performer —and the other is the survivor.
– Ghost path: the suffix from v of the ghost performer’s casting
path becomes the ghost path Γg.
– Genealogy: Record v as an internal vertex (merger point) of
the genealogy tree; the segments of P and Q from their most

32 PIOTR ŚNIADY AND ÁKOS URBÁN

recent coalescence vertex (or starting point) to v become tree
edges.
– Form the merged interval H ← I − ∪ I + and extend σ by
this binary coalescence: the partition Pσ replaces {I −, I +}
by {H} and adds g to its ghost set, while the bijection sends
the survivor to the merged interval H as its heir actor and
the ghost performer to the new ghost g. Re-examine v, then
continue the sweep.
(S3) Success: the sweep (S2) runs to the end of the DAG without a spurious crossing.
The remaining representative paths (suffixes from the last coalescence to the
heir endpoints) become the final edges of the genealogy trees. Reality has
climbed all the way to aspiration: σ has reached (PF , π) (verified below in
Proposition 6.7). Return (π, P) (a fixed point) together with the performance P.
Rehearsal terminates (success).

6.1.3. Successful castings.

Definition 6.2 (Successful casting). An ε-candidate casting is successful if rehearsal
processes all crossings as valid coalescences without encountering a spurious one.

Remark 6.3 (A single obstruction). A priori, rehearsing a casting could break
down in several ways: a crossing selected by rehearsal might involve non-adjacent
intervals; a crossing might be spurious (neither representative aspires to the ghost);
or the run might terminate with reality failing to match aspiration on some ghost
or heir. The planarity assumptions collapse this list: consecutivity keeps every
selected crossing adjacent—at the start and after each merger (Section 6.2.2)—and
assignment rigidity rules out a mismatched termination (Corollary 6.6). The spurious
crossing is therefore the only genuine obstruction—and it is exactly the failure that
segment swap pairs off (Section 8).

6.2. Properties of the rehearsal algorithm. This subsection records two facts
about the reality σ that the involution argument (Section 8) uses downstream:
throughout the run σ stays below the aspiration in the poset, and the crossing
rehearsal selects is always between adjacent active intervals.

6.2.1. Reality stays below aspiration.

Lemma 6.4 (Reality stays below aspiration). While rehearsal has not crashed,
the running diagonal assignment σ satisfies σ ≤ π in the assignment poset (Defini-
tion 5.7): every ghost σ has fired is a ghost of π too, with the same performer.

This is immediate by induction on the accepted coalescences: each accepted step
fires a ghost g with σ−1(g) = π−1(g) (the validity test passed) and changes nothing
else, starting from the identity assignment.

6.2.2. Crossings are between consecutive intervals. At any vertex v, the active inter-
vals whose representatives reach v form a consecutive run: if the representatives of
two active intervals meet at v, so does the representative of every active interval
between them, whose path is ordered between theirs. This is consecutivity (Proposi-
tion 2.11). A crossing is therefore always between consecutive active intervals, and
a vertex where several meet carries a contiguous block, which rehearsal processes as
successive binary crossings of adjacent pairs—in label order, matching attribution’s

COALESCING PARTICLE SYSTEMS 33

nested pairing (Section 5.2.2). The property holds at every such vertex, not only
the one rehearsal reaches first, and is inherited after each merger.

6.3. The no-match obstruction and assignment rigidity. The properties above
describe what happens while rehearsal is running and at a spurious failure. There
is one further outcome we still have to rule out: a successful run that nevertheless
fails to reconstruct a performance, because the running assignment σ stops strictly
below the ε-candidate π. This subsection resolves that obstruction under planarity,
via a purely combinatorial rigidity lemma on assignments.

6.3.1. The obstruction. Fix an ε-candidate casting, with bijection π, and run re-
hearsal on it, producing the running assignment σ. Even a successful run—one
that did not crash on a spurious crossing—need not end with σ reaching π. It is
conceivable that rehearsal halts at σ < π: some ghost g ∈ G(Pπ) is not yet a ghost of
Pσ, yet no two σ-active actors’ paths cross in the casting (so rehearsal has nothing
further to process).
Such an outcome would break the proof. The casting would neither be in
attribution’s image (σ never reaches π) nor be spuriously failed (no rejection
occurred), so it would have no partner under the involution ι (Theorem 8.5) and
would survive in the signed sum.
The stall is ruled out in two steps. First, Section 6.3.2 isolates the combinato-
rial core, Lemma 6.5: a rigidity statement on the aspiration π and the running
assignment σ that makes no reference to paths or crossings. Then, in Section 6.3.3,
planarity (P1) supplies the lemma’s hypotheses at a successful termination of re-
hearsal; the conclusion is recorded as Corollary 6.6, the form in which the rest of
the proof uses this subsection.

6.3.2. The rigidity lemma.

Lemma 6.5 (Assignment rigidity). Let π be an assignment and let σ ≤ π be a
diagonal assignment. Suppose:
(i) π is heir-order-preserving: for active intervals I ◁ J of Pπ, π−1(I) ◁ π−1(J);
(ii) for every ghost g ∈ G(Pπ) \ G(Pσ), writing H = heirπ(g) for the unique
active interval of Pπ whose interior contains g, exactly one of the following
holds:
(G1) π−1(H) ◁ π−1(g) ◁ g, or
(G2) g ◁ π−1(g) ◁ π−1(H).
Then σ = π.

Two terms, defined relative to the pair σ ≤ π, run through the proof and through
Figure 14. A ghost of Pπ is pinned if it is also a ghost of Pσ: it then has the
same performer under both assignments, σ−1(g) = π−1(g) (Definition 5.7), so π
cannot reassign it. The remaining ghosts of Pπ, those in G(Pπ) \ G(Pσ), are unmet.
Hypothesis (ii) is a betweenness condition on the unmet ghosts: (G1) and (G2) are
the two mutually exclusive ways of saying that the performer π−1(g) of an unmet
ghost lies strictly between the ghost g itself and the performer π−1(H) of its heir.
The proof uses the hypothesis mostly through this reading.

Proof of Lemma 6.5. It suffices to prove that every ghost of Pπ is pinned, that is,
G(Pπ) = G(Pσ). Indeed, a partition is determined by its ghost junctions, so equal
ghost sets force Pπ = Pσ; the two assignments then have the same heirs, agree at

34 PIOTR ŚNIADY AND ÁKOS URBÁN

Pπ

Pσ

actors
 a c g b1 a−1
 H
 g

J
 c
 pinned

π determined on [a, g) except at c

Case (G1) at g: π−1(H) ◁ π−1(g) ◁ g — two claimants for the free label

H g

π−1(H) = c = π−1(g)

Case (G2) at g: g ◁ π−1(g) ◁ π−1(H) — no claimant for the free label

H g

?
 π−1(g) π−1(H)no one takes c

Figure 14. Assignment rigidity: the one-free-label pigeon-
hole. Top three rows: the entities of Pπ, of Pσ, and the actors over
a shared axis of labels, drawn as in Figure 11: an interval [x, y) is a
box with a filled circle at its minimum, ghosts are open circles below
their row, and arrows depict the assignment σ, from an actor to the
entity it performs. Left of a the two partitions agree and all ghosts
are pinned (grayed out). The minimal unmet ghost g is interior to
the π-heir H = [a, b) but is a boundary of Pσ, so J = [a, g) is an
heir of Pσ, and π is determined on the window [a, g) except at the
free actor c = σ−1(J) (brace; Steps 1–2 of the proof). Bottom two
rows: Step 3, each case played against its own copy of the actors’
row and a slim copy of the entities of Pπ. The arrows keep their
meaning, now for π: a filled dot performs H and the circled dot
performs the unmet ghost g, each placed in the cell of its performer;
the gray cells are taken by the performers of the pinned ghosts
of the window. In case (G1) both performers lie in the window,
whose only free cell is c: the dots collide, π−1(H) = c = π−1(g),
impossible for distinct labels. In case (G2) every performer avoids
the free cell (prefix entities perform left of a, everything else at or
beyond g): c goes unclaimed, contradicting bijectivity.

COALESCING PARTICLE SYSTEMS 35

every ghost (each being pinned), and hence use the same heir actors—the labels left
over for the heirs. On heirs, both assignments are order-preserving: σ by diagonality
(Definition 5.6; the heir actor of an active interval lies inside it, and the intervals
are disjoint), π by hypothesis (i). An order-preserving bijection from the heirs onto
the heir actors is unique—it must send the i-th heir in label order to the i-th heir
actor—so the assignments agree on heirs as well, and σ = π.

Suppose then, for contradiction, that unmet ghosts exist. Let g be the minimum
unmet ghost in label order, and let

H := heirπ(g) = [a, b)

be its heir, the unique active interval of Pπ whose interior contains g; thus a < g < b.
From now on we identify each actor with its integer label and compare labels and
junctions by the usual order on integers, reserving ◁ for quoting the hypotheses.
Two structural remarks will be used repeatedly. First, since G(Pσ) ⊆ G(Pπ), every
junction that is a boundary of Pπ—a non-ghost—is a boundary of Pσ as well; and
since a junction interior to an active interval is always a ghost, no active interval of
either partition straddles such a boundary. This applies in particular to a. Second,
by minimality of g, every ghost of Pπ with label < g is pinned.
The contradiction will be a pigeonhole on a single free label, traced in Figure 14.
Step 1 shows that π matches the labels below a with the entities lying below a;
in particular no heir has its performer in [a, π−1(H)). Step 2 shows that inside
the window [a, g) the pinned ghosts determine the value of π at every label except
one, the free actor c. Step 3 plays the two orders of betweenness at g against this
single free label: in case (G1) the performers of H and of g are both trapped in
the window—two claimants for one free label—while in case (G2) no entity at all
may claim c, though the bijection π must use that label. Either way we reach a
contradiction.

Step 1: π matches the prefix. Call an entity of Pπ a prefix entity if it lies entirely
below a: an heir with upper endpoint ≤ a, or a ghost with label < a. Since no heir
of Pπ straddles a, the prefix entities tile [1, a)—each prefix heir contributes itself and
its interior ghosts, one entity per label—so there are exactly a − 1 of them, as many
as there are labels below a. We claim that every non-prefix entity has performer ≥ a.
Since π is injective, the claim forces π to match the a − 1 labels below a with the
a − 1 prefix entities; in particular, every prefix heir then has performer < a. This
matching is the grayed-out region left of the cut at a in Figure 14. We verify the
claim one kind of entity at a time.

Pinned ghosts. The performer of a pinned ghost is its diagonal σ-performer, a label
inside the active interval of Pσ whose interior contains the ghost (Definition 5.6).
That interval does not straddle a. Hence a pinned ghost with label > a has
performer ≥ a; and—needed in a moment—every prefix ghost, being pinned (its
label is < a < g), has performer < a.

Heirs. First, π−1(H) ≥ a. Otherwise heir-order-preservation (i) would give every
prefix heir, each of which precedes H in interval order, a performer < π−1(H) < a as
well; the a − 1 prefix entities together with H would then have a distinct performers
among the a − 1 labels below a. Next, every non-prefix heir K either equals H or
lies entirely to the right of H (its lower endpoint is ≥ a, since it cannot straddle a),
so heir-order-preservation spreads the bound: π−1(K) ≥ π−1(H) ≥ a.

36 PIOTR ŚNIADY AND ÁKOS URBÁN

Unmet ghosts. An unmet ghost g′′ has label g′′ ≥ g > a by minimality of g, and
its heir H ′′ = heirπ(g′′) contains g′′ in its interior, so H ′′ is not a prefix heir and
π−1(H ′′) ≥ a by the previous paragraph. Betweenness places π−1(g′′) strictly
between g′′ and π−1(H ′′), neither of which lies left of a; hence π−1(g′′) ≥ a.
Heirs, pinned ghosts with label > a, and unmet ghosts exhaust the non-prefix
entities, so the claim and the matching hold. We record the resulting two-range
bound on heir-performers, the only form in which Step 3 will use it:

(6.1) π−1(K) < a when heir K has upper endpoint ≤ a,

π−1(K) ≥ π−1(H) ≥ a for every other heir K.

Step 2: one free label in the window [a, g). Every junction with label in (a, g)
is interior to H, hence a ghost of Pπ (a junction interior to an active interval is a
ghost), hence pinned—so in particular a ghost of Pσ. The junction g itself is unmet,
so it is a boundary of Pσ; and a is a boundary of Pσ by the first structural remark
above. Consequently J := [a, g)

is an active interval of Pσ, a strict sub-interval of H.
By σ-diagonality at J (Definition 5.6), the g − a labels of the window split
disjointly as

[a, g) = {c} ⊔ {σ−1(g′) : g′ ∈ G(Pσ) ∩ (a, g)
}
, c := σ−1(J),

the heir actor of J together with the performers of the pinned ghosts interior to J.
Pinning transfers the second set to π: under π as well, the ghosts in (a, g) consume
every label of the window except c. In other words, the value of π is already
determined at every label of the window but one—the free actor c singled out in
Figure 14—and an entity other than a pinned ghost in (a, g) can have its π-performer
in the window only by taking the one free label c.

Step 3: the free label gets two claimants or none. By hypothesis (ii), one of
the two orders of betweenness holds at g with heir H; we treat them in turn.

Case (G1): two claimants for the free label. Here π−1(H) ◁ π−1(g) ◁ g, that
is, π−1(g) ≤ g − 1 and π−1(H) ≤ g − 2. By (6.1) we also have π−1(H) ≥ a, so
π−1(H) and π−1(g) are two distinct labels in the window [a, g). But by Step 2, every
label of the window other than c performs, under π, a pinned ghost in (a, g)—and
neither the heir H nor the unmet ghost g is such an entity. Both labels would
therefore have to equal the single free label c: impossible, as they are distinct.

Case (G2): no claimant for the free label. Here g ◁ π−1(g) ◁ π−1(H), that is,
π−1(g) ≥ g and π−1(H) ≥ g + 1. The free actor c performs some entity π(c); we
rule out every candidate in turn.

• An heir. With π−1(H) ≥ g+1, the bound (6.1) confines every heir-performer
to [1, a) ∪ [g + 1, n + 1), and c ∈ [a, g) lies in neither range.
• A pinned ghost. If π(c) were a pinned ghost g′′, then c = π−1(g′′) = σ−1(g′′).
But σ sends c to the heir J, not to a ghost.
• The ghost g itself. Its performer satisfies π−1(g) ≥ g > c.
• Another unmet ghost g′. By minimality of g we have g′ > g. The heir
H ′ := heirπ(g′) contains g′ > a in its interior, so H ′ is not a prefix heir, and
(6.1) gives π−1(H ′) ≥ π−1(H) ≥ g + 1. Betweenness at g′ would place its

COALESCING PARTICLE SYSTEMS 37

performer c strictly between g′ and π−1(H ′), both of which lie right of g;
but c < g.
Heirs, pinned ghosts, and unmet ghosts exhaust the entities of Pπ: no candidate
for π(c) remains—the free label goes unclaimed, contradicting that π is a bijection
defined at c.

Both cases are impossible. Hence no unmet ghost exists, G(Pπ) = G(Pσ), and, as
shown at the outset, σ = π. □

6.3.3. From rehearsal success to the lemma’s hypotheses.

Corollary 6.6 (Successful rehearsal reaches the aspiration). Run rehearsal on an
ε-candidate casting with bijection π, producing the running assignment σ. Then the
run either fails on a spurious crossing or terminates with σ = π.

Proof. At a successful termination of rehearsal, the running assignment σ satisfies
σ ≤ π (Lemma 6.4) and is diagonal by construction; π is an ε-candidate by the
standing assumption. Successful termination also means that no two σ-active actors’
paths cross in the casting. The crossing property (P1) turns this non-crossing into
order preservation: two paths whose sources are in label order, xI ⪯ xK , but whose
endpoints are reversed, yπ(K) ⪯ yπ(I), are forced to intersect. So if such paths do
not cross, their endpoints keep the order of the sources: I ◁ K implies yπ(I) ≺ yπ(K).
This single observation supplies the two remaining hypotheses of Lemma 6.5.

Heir-order-preservation of π. For π-heirs H ◁ H ′, left-to-right order on the endpoints
yH , yH ′ (sorted by the heir-position assumption, Section 2.5) forces π−1(H) ◁
π−1(H ′).

The betweenness dichotomy (G1)/(G2). For an unmet ghost g of π—one not yet
fired in σ—with heir H = heirπ(g), both performers π−1(g) and π−1(H) are σ-
active: the ghost g has not fired, so π−1(g) is still active; and the performer of a
final heir is never consumed (by σ ≤ π, Lemma 6.4, a consumed actor performs a
ghost rather than reaching an heir). Their paths therefore do not cross, and the
order-preservation observation, applied in both label directions, gives the two-sided
equivalence π−1(g) ◁ π−1(H) ⇐⇒ yg ≺ yH ⇐⇒ εg = +1.
ε-candidacy (Definition 4.2) is exactly εg = +1 ⇐⇒ g ◁ π−1(g). Combining the
two equivalences, exactly one of (G1) or (G2) holds.

All hypotheses hold, so Lemma 6.5 yields σ = π. □

6.4. Successful castings yield valid performances.

Proposition 6.7 (Successful rehearsal recovers the prescribed final state). Let C
be a successful ε-candidate casting. The performance produced by rehearsal has the
prescribed final state F.

Proof. By Corollary 6.6, successful termination forces σ = π; in particular the
partitions agree at the end of the run, Pσ = PF .

Ghosts. Each coalescence adds its junction to G(Pσ), so the run fires exactly the
junctions of G(Pσ) = G. At the coalescence firing g, the consumed actor is the
aspirant π−1(g) (the validity test, Definition 6.1), so the ghost path Γg is a suffix of
the casting path Pπ−1(g)—which ends at yπ(π−1(g)) = yg by Definition 4.1.

38 PIOTR ŚNIADY AND ÁKOS URBÁN

Heirs. The final active intervals are Active(Pσ) = H, and the representative of
H ∈ H at termination is σ−1(H) = π−1(H), never consumed by a coalescence; its
casting path Pπ−1(H) therefore runs to its endpoint yπ(π−1(H)) = yH , closing the
genealogy tree of H.

The performance thus coalesces at exactly the prescribed ghosts, with ghost paths
ending at the prescribed positions, and its heirs are exactly H, with paths reaching
the prescribed endpoints: its final state is F. □

7. The performance–casting bijection

We prove that attribution and rehearsal are mutually inverse, weight-preserving
bijections between performances and successful castings. The key observation is that
the two constructions advance the same object: the running assignment σ, which
starts at the identity assignment and climbs the assignment poset by one binary
coalescence per step, in the linear order ≤ of Definition 2.1. The proof couples the
two runs and checks, by induction over the coalescences, that each step of one is
undone by the corresponding step of the other. Section 7.1 prepares the coupling and
the weight argument; Sections 7.2 and 7.3 then verify the two compositions—one
almost definitional, one substantive.

7.1. The running assignment as a dictionary. The two-particle rule (Sec-
tion 5.1) and its high-indegree extension (Section 5.2.2) assemble into a single
picture, in which attribution is neither a construction nor a calculation but a
relabeling—and the same picture, read backward, is rehearsal.

7.1.1. What each object records. A performance names what happens by entity: it
records which active intervals merge at each coalescence vertex and which ghost is
born there—the genealogy and the ghost paths—but never how the path-segments
meeting at such a vertex continue one another, a point that will matter in Section 7.3.
A casting names everything by actor : it consists of the actors’ paths, any number of
which may share an edge, together with the bijection π, and it records no coalescences
at all. Deciding which crossings are coalescences is rehearsal’s task, and only the
successful castings describe a performance.

7.1.2. The coupled induction. Attribution and rehearsal build the same kind of object:
an increasing chain of diagonal assignments in the assignment poset (Definition 5.7).
Each run starts at the identity assignment and advances by one binary coalescence
per step, taken in the linear order ≤ of Definition 2.1; we write σt for the running
assignment after the vertices up to t have been processed. At every moment σ−1
t
names, for each entity, the actor flowing as it: the running assignment is a dictionary
between the two languages above. Attribution uses it to translate a performance
into a casting; rehearsal, when it succeeds, uses it to translate back. The two lemmas
below show that the two runs share the same σt; the round trip therefore translates
every occurrence out and back with one dictionary, and returns the original. The
two runs differ in how a step is chosen. Attribution reads a coalescence of the
performance and lets the far-side principle pick which of the two incoming actors
performs the new ghost; the terminal value of the chain defines the output casting’s
bijection π (Proposition 5.8). Rehearsal reads a crossing of two representatives
in the casting and, when the validity test passes, extends σt by the coalescence
whose ghost performer is π−1(g) (Definition 6.1). To prove that the two runs agree,

COALESCING PARTICLE SYSTEMS 39

it suffices to consider a single step, assume the two assignments equal before it,
and check that the steps coincide—then induct. One point deserves care: π is
attribution’s terminal output, yet rehearsal needs it from the start. There is no
circularity, because rehearsal consults π only through the single value π−1(g) at the
coalescence firing g, and the chain settles that value at this very vertex and never
revises it.

7.1.3. Weight as a regrouped product. Read as a relabeling, attribution makes its
central property—that it preserves weight—a matter of bookkeeping rather than
calculation. The weight of a performance is a product over its edges grouped by the
genealogy, w(P) = ∏

tree edges e w(e) · ∏

g∈G w(Γg)

(Definition 2.13); the weight of a casting is the same product grouped instead by
actor, w(P) = ∏

I w(PI ). The two multiply the same multiset of edge weights—the
dictionary only re-sorts the factors, from grouped-by-entity to grouped-by-actor,
and the “at most one particle, any number of ghosts” tally ensures every factor is
claimed exactly once. Hence w(P) = w(P), the weight-preservation that underlies
the performance–casting bijection (Proposition 7.3).

7.2. The easy direction: rehearsal undoes attribution.

Lemma 7.1 (Coupling: attribution then rehearsal). Let P be a performance and σt
attribution’s running assignment along it (Proposition 5.8), indexed by the vertices t.
Then rehearsal on the casting A(P) holds the same σt at every t; in particular it
runs without a spurious crossing and returns P, so R ◦ A = id.

Proof. This direction is almost definitional: what attribution emits at a coalescence,
rehearsal reads straight back. We follow a single binary coalescence and induct over
the coalescences in the linear order ≤, both runs starting at the identity assignment.
First, rehearsal advances σt at exactly the coalescences of P. Between coalescences
the casting’s active representatives do not cross: an actor’s path runs along its
genealogy-tree trajectory; trajectories of one tree meet only at their mergers, and
distinct trees are vertex-disjoint (Definition 2.10); and a ghost path issues only from
the vertex that consumes its performer (Definition 2.12), an actor that is from then
on no longer a representative. So the only crossings are the merges themselves.
At such a merge two adjacent active intervals I −, I + meet at junction g, one heir
flowing on and the ghost g born. Attribution assigns the ghost role to the actor that
will follow the ghost path, namely π−1(g), placed on the side εg dictates (Figures 10
and 11); the casting it emits records which actors visit g, and how it stitches their
paths through the vertex plays no part here. Reading the casting, rehearsal recovers
the same coalescence: the merge of I −, I + at g is forced, and the ghost performer
it reconstructs is the actor π−1(g) attribution just named—fixed once g fires, as
the chain only grows (Proposition 5.8). No spurious crossing can arise, the casting
issuing from a genuine performance. The two updates of σt coincide, so the two
chains agree throughout.
It remains to check that the performance rehearsal assembles is P itself, paths
included. Attribution built each casting path by gluing segments of P—tree edges
and ghost paths—at the coalescence vertices (Definition 5.1); rehearsal cuts the
casting paths back at the same vertices, the two runs sharing their coalescences.

40 PIOTR ŚNIADY AND ÁKOS URBÁN

The suffix it records as the ghost path of g is therefore the ghost path Γg of P, and
the segments between consecutive mergers—with the final suffixes that close the
trees—are the tree edges of P. The genealogy trees and the ghost paths coincide,
and rehearsal returns P. □

7.3. The hard direction: attribution undoes rehearsal.

Lemma 7.2 (Coupling: rehearsal then attribution). Let C = (π, P) be a successful
casting, σt rehearsal’s running assignment on it, and P = R(C) (of final state F,
Proposition 6.7). Then attribution on P holds the same σt at every t; in particular
A(P) = C, so A ◦ R = id.

Proof. This is the substantive direction, because rehearsal discards information that
attribution must restore. As in the easy direction, both runs advance σt at the same
steps: the coalescences of P are exactly the valid crossings that rehearsal processed
(Definition 6.2), and attribution, reading P, meets them in the same order ≤. It
therefore suffices to follow a single such coalescence and induct.
At a junction g two active representatives cross. The four path-segments incident
to the vertex—two incoming, two outgoing—are paired in the casting, but rehearsal,
recording only the merge and the ghost it frees, disconnects them: the performance
it builds no longer says which incoming segment continued as which outgoing one.
This is no accident of the algorithm but of the representation: a performance names
what merges and what is freed, never the actor-paths themselves (Section 7.1). To
return the original casting, attribution must reconnect the four segments the way
rehearsal found them.
There are exactly two reconnections, the two gluings of the two-particle case: λ−
draws the ghost from I −, λ+ from I + (Figures 10 and 11). Rehearsal’s choice of
ghost performer—π−1(g), the only choice σ ≤ π admits (Lemma 6.4)—singles out
one of the two. Attribution chooses by the ghost sign, drawing the ghost from the
side εg dictates. The two choices agree because the casting is an ε-candidate, which
ties εg to the side of π−1(g): g ◁ π−1(g) ⇐⇒ εg = +1 (Definition 4.2). So the
side εg sends attribution to is the side π−1(g) sits on, and attribution reapplies the
very gluing rehearsal used. The lost pairing is recovered from εg, which the casting
carries—never stored as path data. The two updates of σt coincide, so σt agrees
throughout and attribution returns C. □

The two couplings compose to the identity in both orders, and the weight bill
has already been paid (Section 7.1.3):

Proposition 7.3 (Performance–casting bijection). For fixed final state F, attri-
bution and rehearsal are mutually inverse, weight-preserving bijections between
performances and successful castings: corresponding objects satisfy w(P) = w(P).

Proof. Immediate from Lemmas 7.1 and 7.2; weight is preserved because performance
and casting multiply the same multiset of edge weights (Section 7.1.3). □

8. The sign-reversing involution

Rehearsal (Section 6) sorts ε-candidate castings into successful and failed ones.
To prove the determinant formula we show that the failed castings cancel in signed
pairs, leaving only the successful ones. The pairing mechanism is segment swap, the
classical first-crossing exchange (Section 3.3); the one new ingredient is where to

COALESCING PARTICLE SYSTEMS 41

t = 0

t = T

x1 x2

y1 y2

c P1
P2

(a) Before swap:
paths cross at c
 t = 0

t = T

x1 x2

y1 y2

c P ′
1
P ′
2

(b) After swap:
endpoints exchanged

Figure 15. Segment swap: the sign-reversing involution.
(a) Paths P1 (solid) and P2 (double) cross at vertex c. (b) After the
swap, final segments are exchanged: P ′
1 follows P1 to c, then P2’s
tail to y2; P ′
2 follows P2 to c, then P1’s tail to y1. The bijection
updates to π′ = (1 2) ◦ π, reversing the sign. Failed castings cancel
in pairs via this operation.

apply it. As previewed in Section 1.4, the classical Karlin–McGregor / Lindström–
Gessel–Viennot proof forbids every crossing and swaps at the first one; here crossings
are prescribed by the coalescence pattern, and rehearsal locates the first spurious
crossing—a place where the aspiration π calls for a coalescence that the reality σ
cannot carry out. Segment swap edits π there by the transposition (I J), so the
involution pairs each failed casting with the one differing only in that single spurious
crossing; the ε-candidacy condition guarantees the swapped casting is again an
ε-candidate, and the surviving fixed points are exactly the castings whose aspiration
is realizable throughout. Section 8.1 establishes segment swap; Section 8.2 assembles
the involution ι, whose fixed points are the successful castings—already identified
with performances in Section 7.

8.1. Segment swap.

8.1.1. Definition and basic properties. Given a casting (π, P) and two actors I, J
whose paths cross, segment swap exchanges their suffixes at the first crossing v:
the new path P ′
I follows PI to v, then continues along PJ ; symmetrically for P ′
J .
The bijection updates accordingly: π′ = (I J) ◦ π, exchanging the destinations of I
and J. See Figure 15.

Lemma 8.1 (Segment swap is involutive, weight-preserving, and sign-reversing).
Segment swap is:
(i) An involution: swapping twice recovers the original.
(ii) Weight-preserving: same path segments, same total weight.
(iii) Sign-reversing: sgnε(π′) = − sgnε(π).

Proof. (i) Swapping at v twice restores the original paths and bijection. (ii) The
path segments are redistributed but the multiset of edges is unchanged, so total
weight is preserved. (iii) The updated bijection π′ = (I J) ◦ π differs from π by a
transposition, so sgnε(π′) = − sgnε(π) by the transposition rule (Corollary 4.6). □

42 PIOTR ŚNIADY AND ÁKOS URBÁN

8.1.2. The swap criterion. Segment swap of an arbitrary ε-candidate casting need
not itself be an ε-candidate. The next lemma pins down exactly when it is, at the
adjacent pair rehearsal crosses.

Lemma 8.2 (Swap criterion). At each iteration of rehearsal, let I − ◁ I + be the
adjacent active intervals at junction g, with representative actors I = σ−1(I −) and
J = σ−1(I +) whose paths cross. Then the segment swap of the casting at I, J is
again an ε-candidate if and only if

g /∈ {π(I), π(J)},

that is, unless one of the two crossing representatives aspires to ghost g.

Proof. Segment swap exchanges π at I and J and leaves π unchanged elsewhere;
the swapped casting fails ε-candidacy precisely when the swap moves some ghost’s
performer to the wrong side. We check each ghost.

The current junction h = g. The performer at g changes under the swap if and
only if g ∈ {π(I), π(J)}; in that case the new performer is the other actor of {I, J}.
Since I ∈ I − = [a, g) and J ∈ I + = [g, c) lie on opposite sides of g, the performer
of g switches sides, so ε-candidacy at g flips. If g /∈ {π(I), π(J)} the performer at g
is unchanged and ε-candidacy at g is preserved.

Ghosts h ̸= g outside I − ∪ I +. Both I and J lie inside the contiguous interval
I − ∪ I +, hence on the same side of h. Whether or not the performer at h changes,
it stays on the same side of h, so ε-candidacy at h is preserved.

Ghosts h ̸= g inside I − ∪ I +. Such an h lies interior to the active interval I − or
I +, so it is already a ghost of Pσ. By σ ≤ π (Lemma 6.4) its performer is pinned,
π−1(h) = σ−1(h)—the actor consumed when h fired, no longer a survivor. The
crossing representatives I and J are survivors, so π−1(h) /∈ {I, J}; the swap does
not affect the performer at h, and ε-candidacy at h is preserved.

Combining the three cases, the swapped casting fails ε-candidacy if and only
if g ∈ {π(I), π(J)}; equivalently, it remains an ε-candidate exactly when g /∈
{π(I), π(J)}. □

Corollary 8.3 (Segment swap at a failure pair lands in an ε-candidate). If rehearsal
on an ε-candidate casting C halts at the failure pair (I, J), then the segment swap
of C at (I, J) is itself an ε-candidate casting.

Proof. At a spurious crossing g /∈ {π(I), π(J)}, so the swap remains an ε-candidate
by Lemma 8.2. □

8.2. The involution. Combining rehearsal (the classifier) with segment swap (the
pairing mechanism) defines the involution on ε-candidate castings.

Definition 8.4 (The involution ι). For each ε-candidate casting C, set

ι(C) =
 



C if rehearsal on C succeeds,

segment swap of C at (I, J) if rehearsal on C
halts at the failure pair (I, J).

Theorem 8.5 (Successful castings are the fixed points of ι). The map ι is a weight-
preserving, sign-reversing involution on ε-candidate castings. Its fixed points are
exactly the successful castings.

COALESCING PARTICLE SYSTEMS 43

Proof. Well-defined on ε-candidates. If rehearsal succeeds on C then ι(C) = C is
ε-candidate. If rehearsal halts at (I, J), the segment swap at (I, J) lands in an
ε-candidate (Corollary 8.3).

Fixed points. By construction, ι(C) = C iff rehearsal succeeds on C, iff C is successful
(Definition 6.2).

Involution. We treat the two branches of ι’s definition separately. On a successful
casting, ι is the identity, so ι2 = id trivially.
On a failed casting C with failure pair (I, J) at vertex v and junction g, set C′ to
be the segment swap of C at (I, J). Here the failure vertex v is the first crossing
of PI and PJ , so the segment swap at (I, J) (Section 8.1) acts exactly at v: since
I and J are both σ-active when rehearsal reaches v, any earlier crossing of their
paths would—by consecutivity (Section 6.2.2) and rehearsal’s per-vertex processing—
already have fired a coalescence consuming one of I, J or halted rehearsal spuriously
before v, contradicting that both reach v active. We must show that ι(C′) = C.
We claim that rehearsal on C′ also halts at v with failure pair (I, J); then ι(C′)
is the segment swap of C′ at (I, J), which is C by involutivity of segment swap
(Lemma 8.1(i)).

Locality of the swap. Segment swap at (I, J) modifies only the suffixes of PI and PJ
after v; every walk prefix up to and including v, and every other walk, is identical
in C and C′. Rehearsal’s crossings strictly before v therefore appear in the same
chronological order on C and C′ with identical geometry. Through every valid
crossing before v, the same pair of active intervals merges at the same junction, the
same actor is consumed as a ghost performer, and reality σ advances identically, so
the reality σ and the partial performance built so far when rehearsal reaches v are
the same on C and C′. The same applies to any valid crossings processed at v itself
before the pair (I, J): their consumed performers are no longer active, hence are
neither I nor J, so the swap alters neither their tests nor their outcomes.

Invariance of the test at v. At v the paths of I and J still cross. The validity test
asks whether g ∈ {π(I), π(J)}. The swap transposes π at I and J, exchanging π(I)
and π(J); the unordered pair {π(I), π(J)} is unchanged. The test still fails, so
rehearsal on C′ halts at the same vertex v with failure pair (I, J).

Properties. Weight-preservation and sign-reversal follow from Lemma 8.1. □

9. Proof of the coalescence formula

With the bijection between performances and successful castings and the involu-
tion ι in place, two pieces remain: the sign identity, showing that every successful
casting is positive for the ghost-adjusted sign, and the final assembly, which reads
det M off the restricted Leibniz expansion (Proposition 4.4) and cancels the failed
castings against one another.

9.1. The sign identity.

Proposition 9.1 (Successful castings are positive). For any successful casting C,
the ghost-adjusted sign is

sgnε(π) = +1 (equivalently, sgn π = ∏

g∈G εg).

44 PIOTR ŚNIADY AND ÁKOS URBÁN

Proof. Every successful casting is the attribution of a performance—the surjectivity
of attribution, the A ◦ R = id direction of Proposition 7.3—so sgnε(π) = +1 by
Proposition 5.10. □

So attribution lands among the positive castings: each successful casting con-
tributes exactly +1 · w(P) to the determinant.

9.2. Completing the proof.

Proof of Theorem 3.2. The restricted Leibniz expansion (Proposition 4.4) writes
the determinant as a signed sum over ε-candidate castings,

det M = ∑

(π,P)
π∈ΠF
 sgnε(π) w(P).

The involution ι (Theorem 8.5) partitions the ε-candidate castings into its fixed
points—the successful castings—and two-element orbits of failed castings. Segment
swap preserves the weight and negates the ghost-adjusted sign (Lemma 8.1), so the
two castings of each failed orbit cancel. Every surviving fixed point is a successful
casting, which is positive by Proposition 9.1; hence

det M = ∑

successful castings sgnε(π) w(P) = ∑

successful castings w(P).

Finally, the weight-preserving bijection between successful castings and performances
(Proposition 7.3) identifies the right-hand side with the total weight Z. Therefore
Z = det M . □

9.3. Example: full coalescence of three particles. We return to Example 5.3:
three particles I1, I2, I3 coalesce into one heir H = [1, 4), with ε2 = +1 and ε3 = −1.
The ε-candidacy condition requires:
• π−1(2) ▷ 2, so π−1(2) ∈ {I2, I3};
• π−1(3) ◁ 3, so π−1(3) ∈ {I1, I2}.
Three bijections satisfy these constraints:

π1 : I1 ↦→ H, I2 ↦→ 3, I3 ↦→ 2,

π2 : I1 ↦→ 3, I2 ↦→ 2, I3 ↦→ H,

π3 : I1 ↦→ 3, I2 ↦→ H, I3 ↦→ 2.

9.3.1. Which candidates come from a performance. The bijections π1 and π2 each
arise from a coalescence order whose attribution produces it—the two orders worked
out in Example 5.3 (Figures 12 and 13), in which junction 3 fires first for π1 and
junction 2 first for π2. Both are positive, sgnε(π1) = sgnε(π2) = +1, as guaranteed
by Proposition 9.1: here sgn π1 = sgn π2 = −1 and ∏

g εg = ε2ε3 = −1 multiply to
+1.
The bijection π3, by contrast, arises from no coalescence order: it satisfies the
ε-candidacy constraint but admits no successful casting (Figure 16). The middle
particle I2 must coalesce with a neighbor before reaching the final time. If I2
coalesces first with I1, then ghost 2 is created—but the ghost must be I1 or I2, not
I3 as π3 requires. If I2 coalesces first with I3, then ghost 3 is created—but the ghost
must be I2 or I3, not I1 as π3 requires.

COALESCING PARTICLE SYSTEMS 45

X

Y

I1 I2 I3

2 H 3
 !

(a)
 1 2 3 4

1 2 3 4

I1 I2 I3

H

2 3 X

(b)

Figure 16. A candidate with no successful casting: π3. The
bijection π3: I1 ↦→ 3, I2 ↦→ H, I3 ↦→ 2 satisfies the candidacy
condition, yet every one of its castings fails. (a) Any path family
has a spurious crossing—the middle particle I2 must collide before
reaching H. (b) Bijection π3, with sgnε π3 = −1; its castings all fail
and cancel under the involution. Compare with Figures 12 and 13.

9.3.2. The involution pairs failed castings. Every π3-casting fails at its first crossing
(either P1 ∩ P2 or P2 ∩ P3). The segment swap at this crossing converts π3-castings
into π1- or π2-castings with wrong crossing order. Conversely, π1- and π2-castings
with wrong crossing order swap back to π3-castings. The pairings preserve weight
and flip sign, so all failed castings cancel. Only correctly-ordered π1- and π2-castings
survive—exactly those arising from performances.

10. Continuous processes

The discrete framework extends to continuous time and space. The determi-
nant identity of Theorem 3.2 was proved for discrete-time, discrete-space walks;
we now show that the same identity holds for any Markov process satisfying the
Karlin–McGregor assumptions—in particular Brownian motion—by reading the
discrete proof as a statement about measures rather than counts (Theorem 10.2).
The combinatorial core (ε-candidates, segment swap, the sign-reversing involu-
tion) is untouched; only the bookkeeping of outcomes changes from summation to
integration.
The dictionary with the discrete proof is direct. In the discrete proof a spacetime
point is a vertex (x, t)—space horizontal, time upward (Figure 1)—and the sign-
reversing involution runs along ≤, which on these vertices (x, t) we realize as the
lexicographic order (a linear extension of the time order of Definition 2.1), comparing
the time coordinate t first. Here the spacetime points are arbitrary (x, t) in space-
time, and the same order serves unchanged. The one combinatorial subtlety—several
particles meeting at a single spacetime point—is handled exactly as in the discrete
construction, by resolving the multiple meeting into a sequence of binary collisions
(the construction below).

46 PIOTR ŚNIADY AND ÁKOS URBÁN

10.1. Karlin–McGregor assumptions. Let Ω denote the probability space for n
non-interacting particles with initial positions x1 ≤ · · · ≤ xn. Each ω ∈ Ω specifies
trajectories up to time T , with XT (ω) = (X 1
T (ω), . . . , X n
T (ω)) denoting the final
positions.
The Karlin–McGregor assumptions [KM59] are:

(KM1) Strong Markov property: the n-particle system (X 1, . . . , X n) is strong
Markov—for any stopping time τ of its joint filtration, the post-τ system is
conditionally independent of the pre-τ system given the state at τ ;
(KM2) Identical, independent dynamics: the particles are independent (P is the
product law), each following the same Markov process (differing only in
initial position);
(KM3) Order preservation: adjacent particles cannot change their relative order
without first occupying the same state;
(KM4) Meeting times are stopping times: for particles I < J, the first meeting time
τI,J = inf{t : X I
t = X J
t } is a stopping time.

Identical, independent dynamics (KM2) ensures that when two particles meet, their
post-meeting trajectories are exchangeable (conditioned on the meeting state): this
is the measure-theoretic analog of weight-preserving segment swap. For independent
copies the joint strong Markov property (KM1) is not automatic; it holds under mild
regularity—continuous paths and a jointly continuous transition function [KM59,
Section 6, Theorem 2]. These hold for Brownian motion and other continuous-path
diffusions, as well as for skip-free birth-death chains. For discrete-time ±1 walks
on Z, order preservation requires that all particles share the same parity (as enforced
by the checkerboard lattice of Example 2.3).

10.2. The finite coalescing system. The formula below (Theorem 10.2) is an
identity for Pint, the law of the coalescing system. Before stating it we must say
what that system is: for particles moving in continuous space and time the very
meaning of coalescence calls for a construction, since there is no smallest time step
at which to resolve a collision. With finitely many particles this construction is
elementary, and the ghost method makes it transparent.

10.2.1. The construction. Fix a priority order on the n particles and run the n
trajectories of Ω, the non-interacting system of Section 10.1. At the first instant
at which two particles occupy a common state, an heir and a ghost emerge: the
higher-priority particle takes the heir role and carries the merged group forward
along its own trajectory, while the lower-priority particle takes the ghost role. Order
preservation (KM3) forces each collision to be between two particles currently
adjacent in the order, so every collision creates exactly one ghost and retires one
active particle; hence at most n − 1 collisions occur and the construction terminates.
Should three or more particles meet at a single instant, the meeting is resolved as a
sequence of binary collisions in priority order, exactly as a high-indegree vertex is in
the discrete construction (Section 5.2.2). Meeting times are stopping times (KM4)
and the strong Markov property (KM1) makes the evolution after each collision
a fresh instance of the same dynamics, so the recursion is well defined—it is the
very stopping-time bookkeeping used in Section 10.5.3 to make the casting space
measurable.
 COALESCING PARTICLE SYSTEMS 47

10.2.2. Retention makes existence immediate. The standard constructions truncate
the loser at each collision, as in Arratia’s construction for Brownian motion [Arr79];
the ghost method instead keeps the truncated tail as a ghost running on along its
own independent trajectory, so no path is ever stopped. All n trajectories of Ω
survive intact, and coalescence becomes a relabeling of which coordinate is read as
an heir. Consequently Pint is the pushforward of the non-interacting law P under
this deterministic relabeling, and its existence is immediate.

10.2.3. Generality. The construction invokes only the Karlin–McGregor assump-
tions (KM1–KM4), never any special feature of Brownian motion, so it covers the
whole class of Section 10.1. The law of the coalescing system does not depend
on the chosen priority order: identical, independent dynamics (KM2) makes the
post-collision trajectories exchangeable—for Brownian motion, exactly Arratia’s
observation that the coalescing flow does not depend on the precedence rule [Arr79].
Passing to infinitely many particles requires machinery—coming down from in-
finity, a topology on path families—that the finite systems of this paper do not
need [EMS13; TW98; FINR04].

10.3. The continuous-time ghost formula.

Definition 10.1 (ε-admissible sets). Fix a coalescence pattern, hence the role set
R, and a sign vector ε. An ε-admissible set is a measurable set A ⊆ RR of final
positions such that every (yf )f ∈R ∈ A satisfies:
• ghost–heir signs: for each ghost g we require yg ⪯ yheir(g) when εg = +1
and yheir(g) ≺ yg when εg = −1;
• heir order: yH ⪯ yH ′ whenever H ◁ H ′.
Here the weak inequality ⪯ for εg = +1 versus the strict ≺ for εg = −1 assigns a
tie yg = yheir(g) to εg = +1, as permitted by Definition 2.14.

The heir-order condition is no restriction: as in the discrete setting (Section 2.5),
order preservation (KM3) keeps the surviving particles in this order, so a configura-
tion violating it has probability zero under the coalescing system.

Theorem 10.2 (Continuous-time ghost formula). Let the underlying process satisfy
the Karlin–McGregor assumptions. For any ε-admissible set A:

Pint(final positions ∈ A) = ∑

π∈ΠA sgnε(π) P
(XT ∈ Aπ),

where Pint denotes the probability for the coalescing system, P denotes the probability
for non-interacting particles, and

Aπ = {
(yπ(1), . . . , yπ(n)) : (y1, . . . , yn) ∈ A}

is the set A with coordinates permuted by π.

The candidate set ΠA (Definition 4.2) depends only on the coalescence pattern
and ε, and the ghost-adjusted sign sgnε(π) (Equation (4.1)) only on π and ε; neither
depends on the positions in A, so the right-hand side is a well-defined finite signed
sum.

Remark 10.3 (Scope). The theorem is stated for a single ε-admissible set A—one
coalescence pattern together with one sign vector ε. An arbitrary event on the final
positions is recovered by partitioning it according to coalescence pattern and ε and

48 PIOTR ŚNIADY AND ÁKOS URBÁN

summing, so this one identity determines the entire law of the final state of the
coalescing system.

The formula is an identity between measures, making no reference to densities or
mass functions; it is the starting point for the Brownian specializations developed
in the companion papers [Śni26c; Śni26e].

10.4. Reduction to the discrete proof. The proof of Theorem 10.2 occupies the
rest of this section. The whole argument is one idea: the continuous identity is the
discrete determinant identity of Theorem 3.2 applied cell by cell, with the passage
between the two carried by a reformulation of rehearsal.

10.4.1. The lazy reformulation. As stated in Section 6.1, rehearsal is eager : it sweeps
through every spacetime vertex in the linear order, acting only at the rare crossings.
Nothing in the run depends on the inert steps, so rehearsal has an equivalent lazy
form: from the current state, jump straight to the first vertex at which two active
representatives meet, act there, and repeat. A continuum of spacetime offers no
next vertex to enumerate, but the first meeting of two active representatives is still a
well-defined instant—a stopping time, as verified below—so it is the lazy description
that survives the passage to continuous spacetime.

10.4.2. Finitely many cells. Read this way, rehearsal makes only finitely many
decisions: one at each coalescence of two active representatives (simultaneous
meetings of three or more reduce to binary collisions, as above). Each valid
coalescence retires one active representative, so the count of active particles strictly
decreases and at most n − 1 coalescences can occur before the run ends. The
potential continuity of the paths is deceptive but harmless here: two trajectories
may share a position infinitely often—near a meeting time, Brownian paths do
so almost surely—yet only the first meeting of two still-active representatives is
a decision, after which one of them is retired, so the remaining infinitely many
coincidences are invisible to rehearsal. What records the run is therefore not the
(possibly infinite) set of meetings but its combinatorial type: which adjacent pairs
coalesce, in what order, and with which valid/spurious verdicts, forgetting the actual
times and positions. Pairing the finite candidate set ΠA with Ω and grouping by
combinatorial type partitions the casting space into finitely many combinatorial
cells.
Their finiteness is structural: a combinatorial type is an increasing chain in
the assignment poset (Proposition 5.8)—the reality assignment σ climbs from the
identity at the bottom to (PF , π), one cover step per coalescence—and a finite poset
has only finitely many chains, however wildly the paths oscillate within each cell.
From the dual side the same finiteness is even more immediate: attribution reads a
coalescing performance produced with at most n − 1 coalescence points—the collision
instants where the ghosts emerge (Section 10.2)—so the finite skeleton sits in the
object itself, before any sweep reads it.

10.4.3. The discrete identity, cell by cell. On each combinatorial cell every combina-
torial object is constant: the candidate π, the time-evolution of the assignment σ up
to reparametrization, and the ghost-adjusted sign sgnε(π). The discrete proof uses
only these order-theoretic data, never the numerical positions, so it applies to each
cell verbatim and the determinant identity holds there unchanged. The only ingre-
dient genuinely new in continuous time is that segment swap is measure-preserving

COALESCING PARTICLE SYSTEMS 49

and so permutes the combinatorial cells; this is the single place where the strong
Markov property and the exchangeability of post-meeting trajectories enter.

10.4.4. What remains to verify. For the integrals it suffices to work with a coarser
partition: the first-spurious-crossing partition used below groups castings by which
pair of actors owns the first spurious crossing (or by success), and each of its blocks
is a union of combinatorial cells, so the two share the same measurability. The
remainder of the proof makes the reduction precise and verifies it against the discrete
argument of Sections 4 to 9: that those blocks are measurable, that the swap is
measure-preserving and sign-reversing, and that the successful castings account for
Pint(final positions ∈ A).

10.5. The casting space and its partition.

10.5.1. The casting space.

Definition 10.4 (Casting space). For an ε-admissible set A, the casting space is

CA = {(π, ω) ∈ ΠA × Ω : XT (ω) ∈ Aπ}.

A casting (π, ω) ∈ CA pairs an ε-candidate bijection with n trajectories (PI )I∈A;
its ghost-adjusted sign is sgnε(π) (Equation (4.1)). The casting space carries the
product measure µ: counting measure on ΠA times the probability measure P on Ω.

10.5.2. Partition into blocks. The involution ι : CA → CA acts by segment swap at
the first spurious crossing. Partition the casting space according to which pair of
actors has the first spurious crossing:

CA = C
succ
A ⊔ ⊔

I<J C(I,J)
A ,

where:
• Csucc
A consists of successful castings (no spurious crossing); the involution
acts as the identity;
• C(I,J)
A consists of castings whose first spurious crossing involves actors I
and J; the involution is the segment swap of paths PI , PJ .

10.5.3. Measurability. The blocks must be measurable for the integrals below to make
sense. Fix an ε-candidate π ∈ ΠA and run rehearsal on the casting (π, (PI (ω))I ); its
decisions are stopping times of the filtration (Ft) generated by the n trajectories.
By order preservation (KM3) two representatives reverse order only by first
meeting, so the first crossing is the earliest meeting of two active representatives; by
consecutivity (Section 6.2.2) this earliest meeting is automatically between adjacent
ones. At the start the adjacent pairs are fixed by the initial order and π, so ρ1 =
min τI,J , the minimum of the meeting times (KM4) over this finite, deterministic
set, is a stopping time. If two or more adjacent pairs meet at the same instant (at
distinct positions), the lexicographic order ≤—time first, then position—selects a
unique pair to process first; this keeps the first crossing well defined in every setting,
and for Brownian motion and non-degenerate diffusions the tie is moreover almost
surely vacuous.
The meeting pair at ρ1 is Fρ1-measurable, and whether the crossing is valid
or spurious—the condition g ∈ {π(σ−1(I −)), π(σ−1(I +))}—depends only on π
and that pair, hence is Fρ1-measurable. If the crossing is valid, rehearsal fires a
ghost and the surviving representative carries the merged interval onward along

50 PIOTR ŚNIADY AND ÁKOS URBÁN

its own trajectory, restricted to [ρ1, T ]. The record of which ghost fired is Fρ1-
measurable, so the new set of adjacent active pairs is Fρ1-measurable; and by the
strong Markov property (KM1) the surviving representatives form a post-ρ1 system
again satisfying (KM2) and (KM4). Hence ρ2, the earliest post-ρ1 meeting over this
random but Fρ1 -measurable finite family of adjacent pairs, is again a stopping time,
and likewise each subsequent ρi. Each valid crossing removes one active actor, so the
recursion halts after at most n − 1 steps, producing stopping times ρ1 ≤ · · · ≤ ρk.
The first spurious crossing occurs at the first ρi whose crossing is spurious—itself
a stopping time, being the first member of a finite chain of stopping times at which
an Fρi -measurable event holds; if none is spurious, the run is successful. Hence the
event {ω : (π, ω) ∈ C(I,J)
A } (first spurious crossing the pair (I, J)) and the event
{ω : (π, ω) ∈ Csucc
A } are FT -measurable; as ΠA is finite, the blocks of the partition
are measurable. The construction uses only the Karlin–McGregor assumptions, so
it covers every process in the theorem’s scope; for processes with jumps, where
two or more adjacent pairs may meet simultaneously with positive probability, the
lexicographic order ≤—not a null-set argument—keeps each ρi unambiguous.

10.6. The measure-preserving involution.

10.6.1. Measure-preservation of the swap. The segment swap is measure-preserving
on every block. On C(I,J)
A the swap acts at the first spurious crossing ρ⋆ (the first
spurious ρi above), at which the two representatives occupy the same position.
Because the underlying particles are independent—P is their product law on Ω,
by (KM2)—the post-ρ⋆ trajectories of the two representatives are conditionally inde-
pendent of each other given that common state; the strong Markov property (KM1)
lets each restart afresh from the meeting state, independently of the pre-ρ⋆ past,
and identical dynamics (KM2) makes them identically distributed. In particular,
the joint law of the pair (P post
I , P post
J ) is exchangeable: swapping the two post-
meeting segments produces a pair with the same distribution. It also maps CA
into itself: where it acts as the identity this is immediate, and on the block C(I,J)
A
the first spurious crossing is (I, J), so g /∈ {π(I), π(J)} and by the swap criterion
(Lemma 8.2 and Corollary 8.3) the swapped bijection π′ = (I J) ◦ π is again an
ε-candidate, with XT (ω′) ∈ Aπ′. Since the swap acts by exchanging exactly these
segments while leaving all other paths unchanged, exchangeability together with
this codomain-invariance shows that it preserves the product measure µ.

10.6.2. Cancellation of failed castings. On the failed part CA \ C
succ
A , the involution
ι is sign-reversing: sgnε(ι(π, ω)) = − sgnε(π). This holds because the segment swap
exchanges the roles of actors I and J, so the new bijection π′ = (I J) ◦ π differs
from π by a transposition (Lemma 8.1(iii)).
Since ι is also measure-preserving:
∫

CA\Csucc
A sgnε(π) dµ = ∫

CA\Csucc
A sgnε(ι(π, ω)) dµ = − ∫

CA\Csucc
A sgnε(π) dµ.

Therefore ∫

failed sgnε(π) dµ = 0, and
∫

CA sgnε(π) dµ = ∫

Csucc
A sgnε(π) dµ.

COALESCING PARTICLE SYSTEMS 51

10.7. Completing the proof.

10.7.1. Contribution from successful castings. For successful castings, the ghost-
adjusted sign is sgnε(π) = +1 (Proposition 9.1). Therefore
∫

Csucc
A sgnε(π) dµ = µ(C
succ
A ) = Pint(final positions ∈ A),

where the last equality uses the bijection between successful castings and perfor-
mances (Proposition 7.3). The bijection is purely combinatorial—it depends only on
the paths, not on the probability measure—so the discrete proof applies verbatim
to each outcome ω: the lexicographic tie-break makes rehearsal deterministic, so for
every ω ∈ Ω with final positions in A there is exactly one π ∈ ΠA such that (π, ω)
is a successful casting. No exceptional set is needed—the selection is deterministic
for every outcome, including those where two adjacent pairs meet simultaneously
(Section 10.5.3).

10.7.2. The determinant identity. The integral over the casting space equals
∫

CA sgnε(π) dµ = ∑

π∈ΠA sgnε(π) P
(XT ∈ Aπ).

Combining with the cancellation of failed castings and the positivity of successful
ones gives
 Pint(final positions ∈ A) = ∑

π∈ΠA sgnε(π) P
(XT ∈ Aπ),

which is Theorem 10.2.

11. Integrating out the ghosts

As previewed in Section 1.3, integrating out the ghost positions turns the coales-
cence formula (Theorem 3.2) into a determinant in the heir positions alone. The heirs
are the surviving particles, which we also call survivors. The result is a closed-form
determinantal formula—the coalescence determinant—that, like Theorem 10.2, is
an identity between measures, valid for both discrete and continuous state spaces.
Its matrix definition and theorem statement use only the coalescence pattern and
transition kernels; the ghost machinery enters only in the derivation.

11.1. Transition kernels. Let S denote the state space (R or Z), and fix a time
horizon T > 0. Write XT for the position of a single particle at time T , and let Px
denote the transition kernel: the distribution of XT when the particle starts at x.
For a measurable set B, write Px(B) = Px(XT ∈ B). Let ν denote the reference
measure (Lebesgue measure on R, counting measure on Z), and write px(y) for
the density of Px with respect to ν: the transition density (continuous case) or
transition probability (discrete case). Define the cumulative distribution

Fx(y) = Px((−∞, y]
) = Px(XT ≤ y).

52 PIOTR ŚNIADY AND ÁKOS URBÁN

11.2. The coalescence matrix. Fix a coalescence pattern: a composition
c1+ · · · +ck = n, where the first c1 particles merge into survivor 1 at position y1, the
next c2 into survivor 2 at y2, and so on. The lth block of the composition—the initial
particles merging into survivor l—has indices c1+ · · · +cl−1+1 through c1+ · · · +cl.

Definition 11.1 (Coalescence matrix). Both rows and columns of the n × n
coalescence matrix ˜M are indexed by {1, . . . , n}. The entry in row i, column j
(where j lies in the lth block, with survivor position yl) is

˜Mij =
 {
pxi(yl) if j is the first index in its block,
Fxi(yl) − [i < j] otherwise,

where [i < j] denotes the Iverson bracket. The first column of each block contains
transition densities (or probabilities); the remaining cl−1 columns contain cumulative
distributions with a “staircase” shift −[i < j]: entries with i < j are shifted by −1
(the staircase region is the same as in Figure 2, there shown for the ghost matrix M ).

11.3. The coalescence determinant.

Theorem 11.2 (Coalescence determinant). Label the survivors in increasing spatial
order, and let Wk = {(y1, . . . , yk) ∈ Sk : y1 ≺ · · · ≺ yk}

be the set of strictly ordered survivor positions. For a measurable set A ⊆ Wk,

Pint(survivor positions ∈ A) = ∫

A det
( ˜M (y1, . . . , yk)
) dν⊗k,

where Pint denotes the probability for the coalescing system (Section 10).

The restriction to Wk is the usual Karlin–McGregor caveat: the matrix ˜M is
built from the ordered positions y1 ≺ · · · ≺ yk, and off the ordered chamber the
determinant need not even be nonnegative. On Wk the formula is an identity
between measures: det ˜M is the Radon–Nikodym derivative of the survivor-position
distribution with respect to ν. For continuous state spaces, det ˜M is a probability
density on Wk; for discrete state spaces, it is a probability mass function. The
companion papers [Śni26c] and [Śni26e] develop applications of the coalescence
determinant.

Proof. Start from Theorem 3.2: the total weight of performances with a fixed sign
vector ε is Zε = det M , whose ghost columns are already specialized to ε through
the Iverson brackets [εg = ±1]. To marginalize over ghost positions, integrate each
ghost position yg over the half-line on the side of its heir selected by its sign—left,
yg ⪯ yheir(g), when εg = +1 and right, yheir(g) ≺ yg, when εg = −1 (the ε-admissible
region of Definition 10.1)—and sum over all sign vectors ε ∈ {+1, −1}
G. For
continuous state spaces this starting identity is the density form of Theorem 10.2,
with det M the joint density of the final positions; the marginalization below is then
integration against that density.
Using multilinearity of the determinant in columns—it is linear in each column
separately, and the marginalization touches one ghost column at a time—the sum-
mation and integration act column by column. Heir columns contain W (xi → yH )
with no ghost-sign dependence, so they pass through unchanged; under continuous
state spaces, W (xi → yH ) becomes the transition density pxi (yH ).

COALESCING PARTICLE SYSTEMS 53

For a ghost column g with heir H = heir(g), the junction index g separates the
rows by which side of the junction each particle starts on: those with i ≥ g start
at or to the right of the junction, those with i < g to its left. The matrix entry is
[εg = +1] · W (xi → yg) when i ≥ g and −[εg = −1] · W (xi → yg) when i < g. For
a fixed sign, the matching bracket equals 1 and the opposite bracket equals 0, so
each row keeps only its matching entry. Summing over both signs εg ∈ {+1, −1}
and integrating over yg, the ghost column entry in row i becomes:

• If i ≥ g: the entry [εg = +1] · W (xi → yg) contributes when εg = +1 (ghost
left of heir, yg ≤ yH ). Integrating:
∫

yg≤yH pxi(yg) dν(yg) = Fxi(yH ).

• If i < g: the entry −[εg = −1]·W (xi → yg) contributes when εg = −1 (ghost
right of heir, yg > yH ). The surviving entry is −W (xi → yg). Integrating:

−∫

yg>yH pxi(yg) dν(yg) = −(1 − Fxi(yH )) = Fxi(yH ) − 1.

This is precisely the staircase pattern in Definition 11.1. □

11.4. Example.

Example 11.3 (Pattern 2+1: three particles, first two coalesce). Continuing Sec-
tion 1.3.2: particles 1 and 2 coalesce (survivor at y1) while particle 3 survives alone
(y2). The composition is 2+1: the first block has columns 1 and 2, the second block
has column 3. The coalescence matrix is:

˜M =
 


px1 (y1) Fx1 (y1) − 1 px1(y2)
px2 (y1) Fx2 (y1) px2(y2)
px3 (y1) Fx3 (y1) px3(y2)



 .

The columns follow the same staircase logic as the intro example (Section 1.3.2),
with cumulative distributions replacing transition probabilities: column 2 carries
the shift −[i < j], so row 1 gives F − 1 and rows 2 and 3 give F .
For any measurable set A ⊆ W2 = {(y1, y2) : y1 ≺ y2} of ordered survivor
positions:
 Pint((y1, y2) ∈ A
) = ∫

A det ˜M dν⊗2.

For Brownian motion (S = R), dν⊗2 = dy1 dy2 and det ˜M is a joint density on W2.
For simple random walk (S = Z), ν is counting measure and det ˜M is the probability
mass at (y1, y2).
 Acknowledgments

We thank Theodoros Assiotis, Balázs Bárány, Maciej Dołęga, Sho Matsumoto,
Bálint Tóth, Oleg Zaboronski, and Karol Życzkowski for stimulating discussions
and helpful literature suggestions.
P. Śniady was supported by the National Science Centre, Poland, grant num-
ber 2025/59/B/ST1/01258.

54 PIOTR ŚNIADY AND ÁKOS URBÁN

Declaration of generative AI and AI-assisted technologies
in the manuscript preparation process

During the preparation of this work P. Śniady used Claude (Anthropic) in order to
draft and edit the text and to produce the figures (TikZ code). After using this tool,
the authors reviewed and edited the content as needed and take full responsibility
for the content of the published article.

References

[AB05] Daniel ben Avraham and Éric Brunet. “On the relation between one-
species diffusion-limited coalescence and annihilation in one dimension”.
In: J. Phys. A: Math. Gen. 38 (2005), pp. 3247–3252. doi: 10.1088/
0305-4470/38/15/001. arXiv: cond-mat/0412745.
[AH00] Daniel ben Avraham and Shlomo Havlin. Diffusion and Reactions in
Fractals and Disordered Systems. Cambridge University Press, 2000.
doi: 10.1017/CBO9780511605826.
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
[BŚTU26] Balázs Bárány, Piotr Śniady, Bálint Tóth, and Ákos Urbán. “The Pólya
Web”. In preparation. 2026.
[DA88] Charles R. Doering and Daniel ben Avraham. “Interparticle distribution
functions and rate equations for diffusion-limited reactions”. In: Phys.
Rev. A 38 (1988), pp. 3035–3042. doi: 10.1103/PhysRevA.38.3035.
[EMS13] Steven N. Evans, Ben Morris, and Arnab Sen. “Coalescing systems
of non-Brownian particles”. In: Probab. Theory Related Fields 156.1-
2 (2013), pp. 307–342. doi: 10 . 1007 / s00440 - 012 - 0429 - 0. arXiv:
0912.0017.
[FINR04] L. R. G. Fontes, M. Isopi, C. M. Newman, and K. Ravishankar. “The
Brownian web: characterization and convergence”. In: Ann. Probab. 32.4
(2004), pp. 2857–2883. doi: 10.1214/009117904000000568.
[Fom16] Vladimir Fomichov. “The distribution of the number of clusters in the
Arratia flow”. In: Communications on Stochastic Analysis 10.3 (2016),
pp. 257–270. doi: 10.31390/cosa.10.3.01.
[GF17] E. V. Glinyanaya and V. V. Fomichov. “The central limit theorem for
the number of clusters of the Arratia flow”. In: Theory of Stochastic
Processes 22(38).2 (2017), pp. 1–7. arXiv: 1712.05098.

REFERENCES 55

[GPTZ18] Barnaby Garrod, Mihail Poplavskyi, Roger Tribe, and Oleg Zaboronski.
“Examples of interacting particle systems on Z as Pfaffian point processes:
annihilating and coalescing random walks”. In: Ann. Henri Poincaré 19
(2018), pp. 3635–3662. doi: 10.1007/s00023-018-0719-x.
[GV85] Ira Gessel and Gérard Viennot. “Binomial determinants, paths, and
hook length formulae”. In: Adv. Math. 58.3 (1985), pp. 300–321. doi:
10.1016/0001-8708(85)90121-5.
[HL75] Richard A. Holley and Thomas M. Liggett. “Ergodic theorems for weakly
interacting infinite systems and the voter model”. In: Ann. Probab. 3.4
(1975), pp. 643–663. doi: 10.1214/aop/1176996306.
[KM59] Samuel Karlin and James McGregor. “Coincidence probabilities”. In:
Pacific J. Math. 9.4 (1959), pp. 1141–1164. doi: 10.2140/pjm.1959.9.
1141.
[Kra15] Christian Krattenthaler. “Lattice path enumeration”. In: Handbook of
Enumerative Combinatorics (2015), pp. 589–678. doi: 10.1201/b18255-
13. arXiv: 1503.05930.
[Lin73] Bernt Lindström. “On the vector representations of induced matroids”.
In: Bull. London Math. Soc. 5 (1973), pp. 85–90. doi: 10.1112/blms/
5.1.85.
[Śni26a] Piotr Śniady. Coalescing and annihilating particle systems — simulation
and verification code. Version 1.0.0. Zenodo software deposit. 2026. doi:
10.5281/zenodo.21218342.
[Śni26b] Piotr Śniady. Coalescing particle systems — Lean formalization and
Python prototype. Version 1.0.0. Zenodo software deposit. 2026. doi:
10.5281/zenodo.21037520.
[Śni26c] Piotr Śniady. “Coalescing random walks via the coalescence determi-
nant”. Preprint. 2026. arXiv: 2602.20043 [math.PR].
[Śni26d] Piotr Śniady. “Determinant and Pfaffian formulas for particle annihila-
tion”. Preprint. 2026. arXiv: 2602.13183 [math.PR].
[Śni26e] Piotr Śniady. “Pfaffian structure of basin walls for coalescing particles”.
Preprint. 2026. arXiv: 2602.22885 [math.PR].
[Ste90] John R. Stembridge. “Nonintersecting paths, Pfaffians, and plane par-
titions”. In: Adv. Math. 83 (1990), pp. 96–131. doi: 10.1016/0001-
8708(90)90070-4.
[ŚU26] Piotr Śniady and Ákos Urbán. “Exact coalescence formulas via ghost
particles”. Extended abstract, to be submitted to the proceedings of the
conference Formal Power Series and Algebraic Combinatorics (FPSAC).
2026.
[TW98] Bálint Tóth and Wendelin Werner. “The true self-repelling motion”. In:
Probab. Theory Related Fields 111.3 (1998), pp. 375–452. doi: 10.1007/
s004400050172.
[TZ11] Roger Tribe and Oleg Zaboronski. “Pfaffian formulae for one-dimensional
coalescing and annihilating systems”. In: Electron. J. Probab. 16 (2011),
pp. 2080–2103. doi: 10.1214/EJP.v16-942.
[TZ26] Roger Tribe and Oleg Zaboronski. “Entrance laws for coalescing and
annihilating Brownian motions”. Preprint. 2026. arXiv: 2602.16509
[math.PR].

56 REFERENCES

[Urb25] Ákos Urbán. “The Pólya Web”. MA thesis. Budapest University of
Technology and Economics, 2025. arXiv: 2601.12172 [math.PR].
[War07] Jon Warren. “Dyson’s Brownian motions, intertwining and interlacing”.
In: Electron. J. Probab. 12 (2007), pp. 573–590. doi: 10.1214/EJP.v12-
406.

(P. Śniady) Institute of Mathematics, Polish Academy of Sciences, ul. Śniadeckich
8, 00-656 Warszawa, Poland
Email address, P. Śniady: psniady@impan.pl

(Á. Urbán) Department of Stochastics, Budapest University of Technology and
Economics, Budapest, Hungary

(Á. Urbán) HUN-REN Alfréd Rényi Institute of Mathematics, Reáltanoda utca
13–15, 1053 Budapest, Hungary
Email address, Á. Urbán: urbana@math.bme.hu
Email address, Á. Urbán: urban.akos@renyi.hu
