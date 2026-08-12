<!-- source: https://arxiv.org/html/2007.08965 | converted from HTML -->

Escaping a Polygon

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2007.08965v3 [cs.CG] 20 Oct 2025

# Escaping a Polygon

Zachary Abel Thanks: Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology, Cambridge, MA, USA, [zabel@mit.edu][3] Hugo Akitaya Thanks: Miner School of Computer and Information Sciences, University of Massachusetts, Lowell, MA, USA, [hugoakitaya@gmail.com][4] Erik D. Demaine Thanks: Computer Science and Artificial Intelligence Laboratory, Massachusetts Institute of Technology, Cambridge, MA, USA, [{edemaine,mdemaine,jaysonl}@mit.edu][5] Martin L. Demaine 3 3 footnotemark: 3 Adam Hesterberg Thanks: John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA, [achesterberg@gmail.com][6] Jason S. Ku Thanks: Department of Mechanical Engineering, National University of Singapore, Singapore, [jasonku@mit.edu][7] Jayson Lynch 3 3 footnotemark: 3

###### Abstract

Suppose an *escaping*player (“human”) moves continuously at maximum speed 1 1 in the interior of a region, while a *pursuing*player (“zombie”) moves continuously at maximum speed r r outside the region. For what r r can the first player escape the region, that is, reach the boundary a positive distance away from the pursuing player, assuming optimal play by both players? We formalize a model for this infinitesimally alternating 2-player game and prove that it has a unique winner in any locally rectifiable region. Our model thus avoids pathological behaviors (where both players can have “winning strategies”) previously identified for pursuit–evasion games such as the Lion and Man problem in certain metric spaces. For some specific regions, including both equilateral triangle and square, we give exact results for the *critical speed ratio*, above which the pursuing player can win and below which the escaping player can win (and at which the pursuing player can win). For simple polygons, we give a simple formula and polynomial-time algorithm that is guaranteed to give a 10.89898 10.89898 -approximation to the critical speed ratio, and we give a pseudopolynomial-time approximation scheme for approximating the critical speed ratio arbitrarily closely. On the negative side, we prove NP-hardness of the problem for polyhedral domains in 3D, and prove stronger results (PSPACE-hardness and NP-hardness even to approximate) for generalizations to multiple escaping and pursuing players.

## 1 Introduction

What would you do in a zombie apocalypse? Humans are fascinated by this question: zombies are the subject of over 1,300 films, 1 1 1 [https://www.imdb.com/search/keyword?keywords=zombie&title_type=movie][8] over 150 TV shows, 2 2 2 [https://www.imdb.com/search/keyword?keywords=zombie&title_type=tvSeries][9] over 1,000 books, 3 3 3 [https://www.goodreads.com/shelf/show/zombie-apocalypse][10] and over 900 video games. 4 4 4 [https://store.steampowered.com/tag/browse/#global_1659][11] A 2009 epidemiology study [MHIS09] launched an entire academic discipline of zombie mathematics, culminating in a collected works of fifteen papers on the topic [Smi14]. In this paper, we provide a computational geometric study of how and when humans can successfully escape zombies in a new type of game called “pursuit–escape”.

#### Related work: Pursuit–evasion.

One well-studied family of geometric problems relevant to the zombie apocalypse are pursuit–evasion games [Nah07], which arise in many military applications [Isa65]. In the most famous “Lion and Man” problem [Lit86], one evader (human/man) aims to eternally flee one pursuer (zombie/lion) while moving at unit speed in a shared domain. If the pursuer and evader are ever at the same point, then the pursuer captures the evader and the pursuer thereby wins the game. For example, in a Euclidean disk domain, an evader can evade capture from an equal-speed pursuer, but the pursuer can get arbitrarily close to the evader [Lit86, Cro64]. If the evader is a factor r > 1 r>1 faster, then there is a closed form for the minimum distance they can maintain from the pursuer [Lew86]. Two pursuers can capture one equal-speed evader in the disk, and similarly d d pursuers can win in a d d -dimensional ball [Cro64]; but there is a (rectifiable) 2D polygonal region with holes where the evader can evade two equal-speed pursuers [AHRWN17]. In the infinite plane, an evader can evade equal-speed pursuers if and only if the evader is outside the convex hull of pursuers [RR75, Jan78], but a ( 1 + ε) (1+\varepsilon) -faster evader can always evade countably many pursuers [AHRWN18]. In 3D with polyhedral evader, pursuer, and obstacles, it is (weakly) EXPTIME-hard to decide whether the evader can reach a goal point without being captured [RT93].

A discrete-time analog of the game, where the players take discrete steps of up to unit distance, has been analyzed in many domains, including polygons with holes [BKIS12], genus- g g polyhedral surfaces [KS15], unbounded convex Euclidean domains [ABG09], and compact cat ( 0) (0) (nonpositive-curvature) spaces [BC17]. A discrete-space discrete-time analog of the game is the *cops and robber game*[BN11], where k k cops/pursuers and one robber/evader alternate turns moving along edges on a graph; the smallest k k for which some cop can land on the robber is EXPTIME-complete [Kin15] and W[2]-hard [FGK08] to compute, but e.g. at most 3 3 in planar graphs [AM84]. Other discrete pursuit-evasion games include treewidth [ST93] and fire fighting [FM09] on graphs, and Conway’s Angel Problem [Klo07, Mát07] on grids.

#### Our problem: Pursuit–*escape*.

In this paper, we introduce and explore a variation called the pursuit–escape game, where the two players are the escaper (human/man) and pursuer (zombie/lion), and they move in *complementary domains*— for example, the interior and exterior of a simple polygon — and the escaper’s goal is to reach a common point on the boundaries of these domains where the pursuer is not. As “practical” motivation, the escaper/human/man may be inside a building or on its roof, while the pursuer/zombie/lion is restricted to remain outside; the escaper would like to reach an exit when the pursuer is a positive distance away. (Assume, for example, that the building is surrounded by a parking lot full of cars, enabling escape if the escaper has a brief head start.) The escaper and pursuer move continuously, at speeds bounded by respective maximum speeds, and each move optimally. When can the escaper escape, and when can the pursuer always prevent escape? Unlike pursuit–evasion, the escaper can easily evade *capture*, because of the complementary domains: just stand still. The challenge in pursuit–escape is to *escape*at a point where the escaper could not be captured.

One specific instance of this problem, where the pursuer and escaper regions are the interior and exterior of a unit disk, has been studied many times before in different guises. In 1961, Richard Guy [Guy61] posed this problem in the form of the following puzzle, reproduced in [O’B61]:

Some robbers have stolen the green eye of a little yellow god from a temple on a small island in the middle of a circular lake. As they embark in their boat, they are observed by a solitary guard on the shore, who can run four times as fast as they can row the boat. Can they be sure of reaching the shore and escaping with their loot? If so, how? And what if the guard could move four *and a half*times as fast as the robbers?

The same problem was rethemed by Martin Gardner [Gar65] to be about a maiden on a rowboat, and more recently, featured on Numberphile [Spa19]. The first explicit positive solution we know of is [O’B61]; see also e.g. [Nah07, Section 4.1]. We prove (for the first time) that this strategy is in fact optimal.

In this paper, we study this problem for more general domains than the unit disk. Specifically, suppose an escaper h h and a pursuer z z move simultaneously and continuously within respective geometric domains D h D_{h} and D z D_{z}, while each player has full knowledge of the movements of the other player. 5 5 5 Notationally, we use h h to denote the escaper and z z to denote the pursuer, as e e and p p are used for other concepts (notably, edge and point); for a mnemonic, think “human” and “zombie”. The pursuer moves at a maximum speed that is r r times faster than the escaper, who we can assume has maximum speed 1 1. To get started, the escaper chooses a starting position in D h D_{h}, and then the pursuer chooses a starting position in D z D_{z}. The escaper wins if they can reach an exit point among a specified set X X of exits, say D h ∩ D z D_{h}\cap D_{z}, that is a positive distance away from the pursuer; and the pursuer wins if they can prevent the escaper from winning for arbitrarily long. The goal of the pursuit–escape game is to determine who wins for given domains D h, D z D_{h},D_{z} for the escaper and the pursuer, an exit set X X, and a speed ratio r r.

#### Capture vs. no capture.

There are two possible models for what happens when the escaper and pursuer meet at the same geometric point. The Lion-and-Man game follows the capture model where the pursuer wins if they are ever at the same location as the escaper. For simplicity in both model and strategy descriptions, we assume the no-capture model: if the escaper and the pursuer are at a common point, then (instead of the pursuer immediately winning) the escaper is merely unable to escape at such an exit point, because they are not a positive distance from the pursuer. Intuitively, the pursuer *blocks*the escaper from exiting instead of *capturing*. Equivalently, we can think of there being two copies of the exit set X X — one for the escaper and one for the pursuer, where the distance between corresponding points is zero — and the escaper wins if they can reach a pursuer’s exit point without capture, while the pursuer must remain in their domain; by this perspective, the no-capture model is a special case of the capture model.

Our no-capture model makes it easier to specify strategies. For example, an escaper strategy can start at an exit point, which forces the pursuer to start at the same point; this exact forced placement then makes it easier to specify the rest of the escaper strategy. Figure 1 gives some simple examples of such strategies. For convex escaper domains, such behavior can be simulated in a capture model: the pursuer can instead start extremely close to an exit, forcing the escaper to be very close to that exit. For nonconvex domains like Figure 1(b), we need to modify strategies to avoid prematurely touching the boundary where the escaper might accidentally be captured by the pursuer, instead moving arbitrarily close to such reflex vertices. This is easy to do for the interior of a polygon or polyhedron, or more generally any escaper domain that has an ε > 0 \varepsilon>0 offset that metrically approximates the original: apply the strategy to the offset domain (which avoids touching the boundary) until it is time to exit, then walk ε \varepsilon to the boundary.

In most cases, we extend our results to the capture model. (In fact, it makes some of our hardness proofs easier.) But we focus on the no-capture model in particular because it makes it easier to relate a discrete game (as defined below) to the continuous game, which enables us to derive pseudopolynomial-time approximation schemes; we leave it open whether these can extend to the capture model.

(a) Disk (b) Nonconvex polygon

Figure 1: Simple (suboptimal) strategies for the escaper in two domains: start at p p, and run at full speed along the dotted shortest path to q q. The speed ratio r r must be at least d z ​ ( p, q) d h ​ ( p, q) d_{z}(p,q)\over d_{h}(p,q) for the pursuer to thwart this strategy, and thus the critical speed ratio is at least this large; see Theorem 3.1.

#### Our results: Well-behaved model.

It is not obvious that this game is well defined: how can two players decide their motion continuously and instantaneously on the past motion of each other? In contrast to most two-player games where the players take discrete turns, so each move can easily depend on all past moves, this game involves effectively infinitesimal alternation between the players’ moves. This difficulty was partially addressed by Bollobás et al. [BLW12] in the context of the Lion and Man problem, by giving a natural definition of “winning strategy” which can fully depend on the past (and in some sense the present) behavior of the opponent. Unfortunately, they also showed that this definition (without further restrictions, at least in some scenarios) actually allows *both*players to have a winning strategy, essentially because two strategies do not have a well-defined outcome of playing against each other.

We prove an analogous result for the no-capture pursuit–escape game: under definitions of winning strategy analogous to [BLW12], the escaper always wins (assuming the exit set is at least one-dimensional). But notably, under this strategy, when the escaper exits, their distance to the pursuer can be arbitrarily small, depending on how quickly the pursuer responds.

Thus we turn to an alternate definition of “winning” the pursuit–escape game: the escaper must exit at a distance of at least ε > 0 \varepsilon>0 from the pursuer, for a uniform constant ε \varepsilon that does not depend on the pursuer’s strategy (in particular, how quickly they respond). We prove that this definition guarantees that exactly one player wins, in very general scenarios. Indeed, we show that there is a critical speed ratio r ∗ ≥ 0 r^{*}\geq 0 (possibly ∞ \infty) such that the escaper wins if and only if r < r ∗ r<r^{*} and the pursuer wins if and only if r ≥ r ∗ r\geq r^{*} (for finite r ∗ r^{*}). The pursuit–escape problem thus asks to determine r ∗ r^{*}, given domains D h, D z D_{h},D_{z} and exit set X X.

In Section 2, we give a precise and general model for the pursuit–escape problem, presented concisely to enable reading of the algorithms in Sections 3 – 4. In Section 5, we further detail the model and prove that it satisfies the natural property that exactly one player wins the game, for arbitrary domains (in any dimension) that are finitely rectifiable in any bounded ball. (Because the full model details are complicated, we delay them until we need the techniques for developing additional algorithms in Section 6.) In particular, our model captures several natural settings for pursuit–escape:

- •

Escaper domains:

  - –

Polygon model: the escaper domain D h D_{h} consists of the interior and boundary of a simple polygon.

  - –

Jordan model: the escaper domain D h D_{h} consists of the interior and boundary of a Jordan curve of finite length, such as a circle in the original problem.

  - –

Polyhedron model: the escaper domain D h D_{h} consists of the interior and boundary of a polyhedron homeomorphic to a sphere.

- •

Pursuer domains:

  - –

Exterior model: the pursuer domain D z D_{z} consists of the exterior and boundary of D h D_{h}.

  - –

Moat model: the pursuer domain D z D_{z} consists of the boundary of D h D_{h} (as with a shark trapped in a moat surrounding a building).

  - –

Graph model: instead of Euclidean space, we have a graph with edge lengths (defining distance along the edges), and D h D_{h} and D z D_{z} consist of some vertices and/or edges (including their endpoints).

For the Lion-and-Man game, Bollobás et al. [BLW12] gave an alternate approach for guaranteeing a unique winner to the game, by restricting strategies to be “locally finite”. Our approach differs in that it redefines “winning” instead of directly restricting strategies, though we also show that our definition implies the existence of strategies satisfying a stronger (uniform) property than local finiteness which we call “obliviousness” (see Section 5.2). This stronger notion of obliviousness allows us to discretize the game in a new way that enables efficient approximation algorithms. Our results also apply more generally: we allow strategies to run for unbounded time (which is useful when the domains are unbounded), and we guarantee unique winners without needing the Axiom of Choice. (With the Axiom of Choice, we do obtain a simpler definition of the pursuer winning phrased in terms of a single pursuer strategy, but the rest of our results do not depend on this simpler definition.)

#### Our results: Algorithms.

We develop several algorithms and prove several complexity results for computing both exact and approximately optimal strategies for pursuit–escape. For the benefit of the reader, we present the most algorithmically interesting result first.

- •

In Section 3, we give a polynomial-time 2 ​ ( 3 + 6) < 10.89898 2(3+\sqrt{6})<10.89898 -approximation algorithm for the critical speed ratio r ∗ r^{*} when the escaper domain is a simple polygon P P and the pursuer domain is defined by either the exterior or moat model. The algorithm is based on a simple and natural formula max p, q ∈ ∂ P ⁡ d z ​ ( p, q) d h ​ ( p, q) \max_{p,q\in\partial P}\frac{d_{z}(p,q)}{d_{h}(p,q)}, which we show is within a constant factor of r ∗ r^{*} (in particular, a lower bound on r ∗ r^{*}) in both the polygon and polyhedron model. These results extend to the capture model.

- •

In Section 4, we solve the pursuit–escape problem exactly for several specific Jordan shapes in both the exterior and moat models: when D h D_{h} is an unbounded wedge, a halfplane, a disk (Guy’s problem), an equilateral triangle, and a square. We use the simple cases of wedge and halfplane to motivate a generalized escaper strategy called “APLO” (axially progressing laterally opposing), which moves the escaper forward in an axial direction, with a lateral component that linearly opposes the pursuer’s movement. We use APLO to define optimal escaper strategies for the disk, equilateral triangle, and square. The last two results are especially complicated, requiring intricate strategies for both escaper and pursuer. Table 1 summarizes the critical speed ratios we prove. These results extend to the capture model, as our optimal escaper strategies do not visit the boundary until the moment of escape.

 | 𝜽 \theta -Wedge | Disk | Equilateral Triangle | Square |

𝒓 ∗ r^{*} | 1 / sin ⁡ θ 1/\sin\theta | 1 / cos ⁡ θ ∗ ≈ 4.603 1/\cos\theta^{*}\approx 4.603 | ( 3 + 5) ​ 2 ≈ 7.405 (3+\sqrt{5})\sqrt{2}\approx 7.405 | 5 2 ​ ( 7 + 41) ≈ 5.789 \sqrt{\frac{5}{2}(7+\sqrt{41})}\approx 5.789 |

Table 1: Exact critical speed ratios for specific Jordan shapes, as proved in Section 4.
- •

In Section 6, we give a pseudopolynomial-time approximation scheme for the critical speed ratio r ∗ r^{*} when the escaper domain is a simple polygon P P and the pursuer domain is defined by either the exterior or moat model. This algorithm builds on the discrete model introduced in Section 5 as an approximation to the continuous game to prove the game has a unique winner. The main extra step for an algorithm is proving a *margin-of-victory*lemma (Lemma 6.3): if the escaper can win the continuous game at all, and the pursuer becomes slightly slower, then the escaper can win with a bit of time to spare. This seemingly innocuous claim is surprisingly involved to prove. It enables us to quantitatively decouple the interdependency of the escaper and pursuer strategies, and thereby bound the incurred discretization error.

- •

In Section 7, we prove that the pursuit–escape problem in 3D is weakly NP-hard, even for polyhedral domains. This result motivates our focus on approximation algorithms. Our proof builds on the famous result by Canny and Reif [CR87] that it is weakly NP-hard to find shortest paths in 3D amidst polyhedral obstacles.

- •

In Section 8, we generalize the problem to multiple escapers and multiple pursuers, where the escapers win if at least one of them can escape. On the positive side, our polynomial-time O ⁡ ( 1) O(1) -approximation and pseudopolynomial-time approximation scheme generalize to this scenario. We also give a partial analysis of the case where the escapers and pursuers move at the same speed. On the negative side, we prove computational complexity — both NP-hardness and PSPACE-hardness — of even approximating the critical speed ratio in several scenarios, as summarized in Table 2. Our reductions are from Nondeterministic Constraint Logic [HD09], Planar Vertex Cover [Lic82], and Vertex Cover [Kar72].

Escapers | Pursuers | Domain | Result |

Multiple | Multiple | Planar | PSPACE-hard [Theorem 8.9]; and NP-hard, even to approximate at all [Theorem 8.10] |

1 | Multiple | Connected | NP-hard, even to 2-approximate [Theorem 8.11] |

Table 2: Multi-pursuer hardness results, as proved in Section 8.

## 2 Brief Model (Abbreviated Version of Section 5)

As mentioned above, it takes some care to define a precise model of simultaneous play of two (or more) continuously moving players that can continuously adapt to each other’s motion. We generally follow the definitions from pursuit–evasion games in [BLW12], generalized to where the players have different speeds and different domains they traverse. Crucially, however, our game’s definition of “winning” is different, and we show that under it exactly one player wins in any game.

In this abbreviated version of Section 5, we define the key notions of our model and summarize the main results that are necessary for understanding the algorithms in Sections 3 – 4. For a more detailed description of why we use these particular definitions, how they differ from past work, and proofs of why exactly one player has a winning strategy, read instead the long form of the model in Section 5.

#### Domains.

A player domain is a closed subset D D of Euclidean space ℝ k \mathbb{R}^{k} that is locally finitely rectifiable, meaning that its intersection D ∩ B D\cap B with any bounded closed Euclidean ball B B is “finitely rectifiable”. Formally, R ⊆ ℝ k R\subseteq\mathbb{R}^{k} is finitely rectifiable if it is the union of the images of finitely many functions of the form S: [0, 1] k → R S:[0,1]^{k}\to R satisfying the Lipschitz condition d ⁡ ( S ⁡ ( u), S ⁡ ( v)) ≤ d ⁡ ( u, v) d(S(u),S(v))\leq d(u,v) for all u, v ∈ [0, 1] k u,v\in[0,1]^{k}.

The input to the pursuit–escape problem consists of both an escaper domain D h D_{h} and a pursuer domain D z D_{z}, and an exit set X X. The escaper and pursuer domains must be *player domains*as described above. The exit set X X must also be a player domain, and a subset of the player domains: X ⊆ D h ∩ D z X\subseteq D_{h}\cap D_{z}. The goal of the escaper will be to reach an exit — any point of the exit set X X — while being sufficiently away from the pursuer.

#### Motion paths.

A motion path with maximum speed s ≥ 0 s\geq 0 in metric domain D D is a function a: [0, ∞) → D a:[0,\infty)\to D satisfying the speed-limit constraint (Lipschitz condition)

 | d D ​ ( a ⁡ ( t 1), a ⁡ ( t 2)) ≤ s ⋅ | t 1 − t 2 | ​ for all ​ t 1, t 2 ≥ 0. d_{D}(a(t_{1}),a(t_{2}))\leq s\cdot|t_{1}-t_{2}|\text{ for all }t_{1},t_{2}\geq 0. |  |

We consider a model where the pursuer maximum speed is a factor of r r larger than the escaper maximum speed, which we assume is 1 1 for simplicity. Thus an escaper motion path is a motion path of maximum speed 1 1 in the escaper domain D h D_{h}, while a pursuer motion path is a motion path of maximum speed r r in the pursuer domain D z D_{z}.

#### Strategies.

For symmetry, the following definitions refer to a player (either escaper and pursuer) and their opponent (pursuer or escaper, respectively). A player strategy is a function A A mapping an opponent motion path b b to a player motion path A ⁡ ( b) A(b) satisfying the following nonbranching-lookahead constraint:

for any two opponent motion paths b 1, b 2 b_{1},b_{2} agreeing on [0, t] [0,t], the strategy’s player motion paths A ⁡ ( b 1), A ⁡ ( b 2) A(b_{1}),A(b_{2}) also agree on [0, t] [0,t].

An escaper strategy H H must satisfy one additional constraint, the escaper-start constraint:

all paths H ⁡ ( z) H(z) (over all pursuer motion paths z z) must start at a common point H ​ ( z) ​ ( 0) H(z)(0).

#### Win condition.

First we define an infinite family of games G ε G_{\varepsilon} for all ε > 0 \varepsilon>0. An escaper strategy H H wins 𝑮 𝜺 G_{\varepsilon} or wins 𝑮 G by 𝜺 \varepsilon if, for every pursuer motion path z z, there is a time t t at which H ​ ( z) ​ ( t) H(z)(t) is on an exit and at distance ≥ ε \geq\varepsilon from z ⁡ ( t) z(t) in the pursuer metric. A pursuer strategy Z Z wins 𝑮 𝜺 G_{\varepsilon} if, for every escaper motion path h h, and every time t t at which h ⁡ ( t) h(t) is on an exit, h ⁡ ( t) h(t) is at distance < ε <\varepsilon from Z ​ ( h) ​ ( t) Z(h)(t) in the pursuer metric: d z ​ ( h ⁡ ( t), Z ⁡ ( h) ​ ( t)) < ε d_{z}(h(t),Z(h)(t))<\varepsilon.

Now we can define the win condition for the pursuit–escape game G G. The escaper wins 𝑮 G if, for some ε > 0 \varepsilon>0, there is an escaper strategy that wins G G by ε \varepsilon, i.e., wins G ε G_{\varepsilon}. The pursuer wins 𝑮 G if, for all ε > 0 \varepsilon>0, there is a pursuer strategy that wins G ε G_{\varepsilon}.

The main result of Section 5 is the following:

{restatable*}

corollaryfinalmodelresult Any (continuous) pursuit–escape instance ( D h, D z, X) (D_{h},D_{z},X) has a critical speed ratio r ∗ ≥ 0 r^{*}\geq 0 (possibility ∞ \infty) such that the escaper wins G ⁡ ( r) G(r) for all speed ratios r < r ∗ r<r^{*} and the pursuer wins G ⁡ ( r) G(r) for all speed ratios r ≥ r ∗ r\geq r^{*}.

## 3 O ⁡ ( 1) O(1) -Approximation Algorithm

In this section, we show that the critical speed ratio for any simple polygon P P is lower bounded by max p, q ∈ ∂ P ⁡ d z ​ ( p, q) d h ​ ( p, q) \max_{p,q\in\partial P}\frac{d_{z}(p,q)}{d_{h}(p,q)} and upper bounded by 10.89898 ​ max p, q ∈ ∂ P ​ d z ​ ( p, q) d h ​ ( p, q) 10.89898\max_{p,q\in\partial P}\frac{d_{z}(p,q)}{d_{h}(p,q)}, where the escaper domain D h D_{h} is the interior and boundary of P P, the pursuer domain D z D_{z} is the boundary and optional exterior of P P (thus allowing either the exterior or moat models), and d h d_{h} and d z d_{z} are the intrinsic (shortest-path) metrics in the escaper and pursuer domains respectively (as defined in Section 2). Our results are constructive: in Section 3.1 we give a winning escaper strategy for speed ratio max p, q ∈ ∂ P ⁡ d z ​ ( p, q) d h ​ ( p, q) \max_{p,q\in\partial P}\frac{d_{z}(p,q)}{d_{h}(p,q)} and a winning pursuer strategy for speed ratio 10.89898 ​ max p, q ∈ ∂ P ​ d z ​ ( p, q) d h ​ ( p, q) 10.89898\max_{p,q\in\partial P}\frac{d_{z}(p,q)}{d_{h}(p,q)}. Furthermore, we give a polynomial-time algorithm in Section 3.2 to compute a maximizing point pair ( p, q) (p,q), resulting in a polynomial-time constant-factor approximation algorithm. As described in Section 1, the strategies can also be modified to work in the capture model by a small inset.

### 3.1 Strategies

The escaper strategy is simple: run from p p to q q for the pair p, q p,q achieving the maximum ratio. The main idea for our pursuer strategy is to decompose the polygon into its medial axis, and within each region corresponding to a polygon edge, try to follow a natural strategy for a halfplane, namely, following the projection of the escaper onto the edge (proved optimal for a halfplane in Section 4.2). The challenge is when the escaper crosses the medial axis from one region to the other, and possibly jumps back and forth between two regions. We only view the escaper as having changed regions once they have left a larger region called the “fringe”, meaning they are deeply in another region; see Figure 3. Then we argue that the pursuer has enough time to transition to the new region’s strategy before the escaper can escape or transition again.

###### Theorem 3.1 (lower bound).

For any escaper domain D h D_{h}, pursuer domain D z D_{z}, and exit set X X, the critical speed ratio r ∗ r^{*} is at least

 | max p, q ∈ X ⁡ d z ​ ( p, q) d h ​ ( p, q). \max_{p,q\in X}\frac{d_{z}(p,q)}{d_{h}(p,q)}. |  |

###### Proof.

Let p p and q q be points maximizing the expression above, and let r ε = d z ​ ( p, q) − ε d h ​ ( p, q) r_{\varepsilon}=\frac{d_{z}(p,q)-\varepsilon}{d_{h}(p,q)}. The escaper can start at p p (escaper-start constraint); we can assume that the pursuer is also at p p, or else the escaper escapes at p p. Then, the escaper can run toward q q at full speed (speed-limit constraint). This strategy does not depend on the pursuer’s position at all (nonbranching-lookahead constraint). The escaper’s distance to q q is d h ​ ( p, q) d_{h}(p,q) and the pursuer’s is d z ​ ( p, q) d_{z}(p,q), so when the escaper reaches q q, the pursuer is at least ε \varepsilon away in pursuer metric, and the escaper escapes. Therefore r ∗ ≥ r ε r^{*}\geq r_{\varepsilon} for all ε > 0 \varepsilon>0, and thus r ∗ ≥ r 0 r^{*}\geq r_{0}. ∎

For a polygonal escaper domain D h D_{h}, this escaper strategy can be extended to the capture model as described in Section 1 and Figure 1(b). For δ > 0 \delta>0, consider the modified strategy where we inset P P by a disk of radius δ \delta to produce a region P ′ P^{\prime}, which for sufficiently small δ \delta is connected and has approximately the same shortest-path metric; round the start point p p and end point q q to nearest points p ′ p^{\prime} and q ′ q^{\prime} respectively on ∂ P ′ \partial P^{\prime}; start at p ′ p^{\prime}; run along a shortest path from p ′ p^{\prime} to q ′ q^{\prime} within P ′ P^{\prime}; and then run along a shortest path from q ′ q^{\prime} to q q. This strategy only touches the boundary of P P at the final time when it reaches q q, but it starts at approximately the same point p ′ p^{\prime} and runs approximately the same distance. Now take the limit as δ → 0 \delta\to 0.

###### Theorem 3.2 (upper bound).

For any simple polygon P P or polyhedron P P homeomorphic to a sphere, define escaper domain D h D_{h} as P P ’s interior and boundary, pursuer domain D z D_{z} as P P ’s boundary and any subset of P P ’s exterior, and exit set X = ∂ P X=\partial P as P P ’s boundary. Then the critical speed ratio r ∗ r^{*} is at most

 | 2 ​ ( 3 + 6) ​ max p, q ∈ X ​ d z ​ ( p, q) d h ​ ( p, q) < 10.89898 ​ max p, q ∈ X ​ d z ​ ( p, q) d h ​ ( p, q). 2(3+\sqrt{6})\max_{p,q\in X}\frac{d_{z}(p,q)}{d_{h}(p,q)}<10.89898\max_{p,q\in X}\frac{d_{z}(p,q)}{d_{h}(p,q)}. |  |

###### Proof.

Divide P P into (open) medial-axis regions, as shown in Figure 2: each region is associated with a facet (edge or face) f f of P P and is the set of points inside P P closer to f f than to any other facet of P P. For each medial-axis region, also define its fringe to be the union, over points p p inside the region, of the ball of points within distance x ⋅ d ⁡ ( p, ∂ P) x\cdot d(p,\partial P) of p p, where d ⁡ ( p, ∂ P) d(p,\partial P) is the distance from p p to the nearest point on the boundary of P P and x = 6 − 2 ≈ 0.45 x=\sqrt{6}-2\approx 0.45 is a fringe size parameter. In particular, each fringe contains its medial-axis region. Because there is a bijection between medial-axis regions and facets of P P, we also refer to the fringe of a facet of P P.

Figure 2: A polygon and its medial axis.

Define the following pursuer strategy:

1. 1.

At all times, the pursuer has a target facet f f of P P such that it attempts to be at the closest point on f f to the escaper. Initially, f f is a facet of P P that is closest to the escaper.

2. 2.

When the escaper exits the fringe of f f, the pursuer runs to the closest point on the boundary ∂ P \partial P to the escaper. If that point is on facet f ′ f^{\prime} of P P, then the pursuer switches its target facet to f ′ f^{\prime}.

This strategy depends only on the current escaper position (nonbranching-lookahead constraint). We have to show that the strategy also satisfy the speed-limit constraint and that the pursuer is at the escaper’s position whenever the escaper is in ∂ P \partial P. We show that, when the escaper leaves the fringe of facet f f in the medial-axis region of a facet f ′ f^{\prime}, the pursuer can run into position (reaching the closest point in ∂ P \partial P to the escaper) before the escaper either reaches the boundary ∂ P \partial P (and escapes) or leaves the fringe of f ′ f^{\prime} (which would trigger another strategy change).

Next we define some points, as in Figure 3. Let h h be the point at which the escaper leaves the fringe (drawn in blue) of a medial-axis region R R (drawn in red) with corresponding facet f p f_{p}. Because h h is on the boundary of the fringe of R R, it is also on a sphere centered at a point o o on the boundary of R R (i.e., on the medial axis) of radius d ⁡ ( o, h) = x ⋅ d ⁡ ( o, ∂ P) = x ⋅ d ⁡ ( o, p) d(o,h)=x\cdot d(o,\partial P)=x\cdot d(o,p) where p p is the closest point to o o on f p f_{p}. Let z z be the closest point to h h on f p f_{p}, which is where the pursuer stands when the escaper is at h h. Note that z z is an endpoint of f p f_{p} if such endpoint is a reflex vertex of P P, i.e., it is not necessarily the projection of h h on the supporting line of f p f_{p}. Let q q be the closest point to h h on ∂ P \partial P, and let f q f_{q} be a facet containing q q.

Figure 3: The scenario when the escaper leaves the fridge (blue) of a medial-axis region R R (red), at a point h h now closest to facet f q f_{q}.

At h h, the escaper’s distance to the boundary is

 | d ⁡ ( h, q) ≥ d ( o, q) − d ( o, h) by triangle inequality = d ⁡ ( o, q) − x ⋅ d ⁡ ( o, p) ≥ ( 1 − x) d ( o, p) because d ⁡ ( o, q) ≥ d ⁡ ( o, p). \displaystyle\begin{aligned} d(h,q)&\geq d(o,q)-d(o,h)\quad\text{by triangle inequality}\\ &=d(o,q)-x\cdot d(o,p)\\ &\geq(1-x)\,d(o,p)\quad\text{because $d(o,q)\geq d(o,p)$}.\end{aligned} |  |

To leave the fringe of their new medial-axis region for facet f q f_{q}, the escaper must run a distance of at least x ⋅ d ⁡ ( h, q) x\cdot d(h,q). We arrange for the pursuer to be in position for the new region’s strategy before either event (reaching the boundary or leaving the new fringe), by bounding the motion of the pursuer during the next motion of the escaper by at most x ​ d ​ ( h, q) ≤ d ⁡ ( h, q) x\,d(h,q)\leq d(h,q) (assuming x ≤ 1 x\leq 1). To reach the new strategy, the pursuer must move at most the sum of three distances:

1. 1.

d ⁡ ( z, p) d(z,p) to return to p p. Because z z is the closest point on f p f_{p} to h h, it is at least as close to p p as the projection of h h onto the supporting line of f p f_{p} (possibly closer, if f p f_{p} is incident to a reflex vertex). The length of that projection is at most d ⁡ ( o, h) = x ⋅ d ⁡ ( o, p) ≤ x 1 − x ​ d ​ ( h, q) d(o,h)=x\cdot d(o,p)\leq\frac{x}{1-x}\,d(h,q) by ( 3.1), so that is an upper bound on the pursuer’s distance to return to p p.

2. 2.

d z ​ ( p, q) d_{z}(p,q) to reach q q.

3. 3.

≤ x ⋅ d ⁡ ( h, q) \leq x\cdot d(h,q) to match the escaper’s move (projected onto f q f_{q}).

So, if the pursuer’s speed is enough to travel these three distances in the time the escaper travels a distance of x ⋅ d ⁡ ( h, q) x\cdot d(h,q), then the pursuer can be in position in time for the escaper’s next region change or escape. That is, the critical speed ratio r ∗ r^{*} is at most

 | x 1 − x ​ d ​ ( h, q) + d z ​ ( p, q) + x ⋅ d ⁡ ( h, q) x ⋅ d ⁡ ( h, q) = 1 + 1 1 − x + d z ​ ( p, q) x ⋅ d ⁡ ( h, q). \frac{\frac{x}{1-x}\,d(h,q)+d_{z}(p,q)+x\cdot d(h,q)}{x\cdot d(h,q)}=1+\frac{1}{1-x}+\frac{d_{z}(p,q)}{x\cdot d(h,q)}. |  |

Because a closest point to o o on ∂ P \partial P is p p, the circle centered at o o with radius d ⁡ ( o, p) d(o,p) is contained in P P, so the line segment from p p to q q is also contained in P P. Thus d h ​ ( p, q) = d ⁡ ( p, q) d_{h}(p,q)=d(p,q), which by triangle inequality is at most 2 ​ d ​ ( o, p) ≤ 2 1 − x ​ d ​ ( h, q) 2\,d(o,p)\leq\frac{2}{1-x}\,d(h,q). Thus our upper bound on r ∗ r^{*} is at most

 | 1 + 1 1 − x + d z ​ ( p, q) x ​ 1 − x 2 ​ d h ​ ( p, q). 1+\frac{1}{1-x}+\frac{d_{z}(p,q)}{x\,\frac{1-x}{2}\,d_{h}(p,q)}. |  |

Because d h ​ ( p, q) d_{h}(p,q) follows the straight line segment between p p and q q, d z ​ ( p, q) d h ​ ( p, q) ≥ 1 \frac{d_{z}(p,q)}{d_{h}(p,q)}\geq 1. Therefore we can upper bound r ∗ r^{*} by

 | ( 1 + 1 1 − x + 2 x ⁡ ( 1 − x)) ​ d z ​ ( p, q) d h ​ ( p, q). \left(1+\frac{1}{1-x}+\frac{2}{x(1-x)}\right)\frac{d_{z}(p,q)}{d_{h}(p,q)}. |  |

This upper bound is minimized when x = 6 − 2 x=\sqrt{6}-2, so picking x = 6 − 2 x=\sqrt{6}-2, we obtain an upper bound of r ∗ ≤ 2 ​ ( 3 + 6) ​ d z ​ ( p, q) d h ​ ( p, q) r^{*}\leq 2\,(3+\sqrt{6})\frac{d_{z}(p,q)}{d_{h}(p,q)}. ∎

### 3.2 Algorithm

The upper bound of Theorem 3.2 combined with the lower bound of Theorem 3.1 suggest a polynomial-time constant-factor approximation algorithm for simple polygons and polyhedra homeomorphic to a sphere. However, it requires some work to actually find a pair of points p, q ∈ X p,q\in X maximizing d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,q)}{d_{h}(p,q)}. Here we show how to solve the polygon case, and leave the polyhedron case as an open problem.

###### Theorem 3.3.

Given a simple polygon P P with ≤ n \leq n vertices, and given exit set X ⊆ ∂ P X\subseteq\partial P as a set of ≤ n \leq n segments, we can compute the pair of points ( p ∗, q ∗) = arg ⁡ max p, q ∈ X ⁡ d z ​ ( p, q) d h ​ ( p, q) (p^{*},q^{*})=\arg\max_{p,q\in X}\frac{d_{z}(p,q)}{d_{h}(p,q)}, up to a 1 + ε 1+\varepsilon factor error, in O ⁡ ( n 4 ​ log ⁡ 1 ε) O(n^{4}\log{1\over\varepsilon}) time.

###### Proof.

Two shortest paths ( p 1, p 2, …, p k) (p_{1},p_{2},\ldots,p_{k}) and ( p 1 ′, p 2 ′, …, p l ′) (p^{\prime}_{1},p^{\prime}_{2},\ldots,p^{\prime}_{l}) between point pairs ( p 1, p k) (p_{1},p_{k}) and ( p 1 ′, p l ′) (p^{\prime}_{1},p^{\prime}_{l}) in ∂ P \partial P are combinatorially equivalent if p 1 p_{1} and p 1 ′ p_{1}^{\prime} are on the same edge, p k p_{k} and p l ′ p^{\prime}_{l} are on the same edge, k = l k=l, and p i = p i ′ p_{i}=p^{\prime}_{i} for i ∈ { 2, …, k − 1 } i\in\{2,\ldots,k-1\}.

Consider a point p ∈ ∂ P p\in\partial P and its (geodesic) shortest path within P P to every other point in ∂ P \partial P. Let 𝒮 ⁡ ( p) \mathcal{S}(p) be the set of combinatorial equivalence classes of these shortest paths from p p. By the shortest path map [Mit17], | 𝒮 ⁡ ( p) | = O ⁡ ( n) |\mathcal{S}(p)|=O(n) and 𝒮 ⁡ ( p) \mathcal{S}(p) can be computed in O ⁡ ( n) O(n) time.

We will partition the boundary of ∂ P \partial P into segments S S with the property that, for every p, p ′ ∈ S p,p^{\prime}\in S, 𝒮 ⁡ ( p) = 𝒮 ⁡ ( p ′) \mathcal{S}(p)=\mathcal{S}(p^{\prime}). Compute the arrangement of the lines going through every pair of vertices of P P. There are O ⁡ ( n 2) O(n^{2}) such lines, so we can compute the arrangement in O ⁡ ( ( n 2) 2) = O ⁡ ( n 4) O((n^{2})^{2})=O(n^{4}) time [HS17]. Partition each edge of P P into O ⁡ ( n 2) O(n^{2}) segments according to this arrangement, for a total of O ⁡ ( n 3) O(n^{3}) segments. We can then clip and/or remove the segments to lie within X X.

Let S S be such a segment of ∂ P \partial P. For k ≥ 4 k\geq 4, every shortest path ( p 1, p 2, …, p k) (p_{1},p_{2},\ldots,p_{k}) where p 1 = p p_{1}=p satisfies that S S is on the same side of the line through p 2 p_{2} and p 3 p_{3}. Hence, every shortest path from a point p 1 ′ ∈ S p^{\prime}_{1}\in S to p k p_{k} is ( p 1 ′, p 2, …, p k) (p_{1}^{\prime},p_{2},\ldots,p_{k}), and thus combinatorially equivalent to ( p 1, p 2, …, p k) (p_{1},p_{2},\ldots,p_{k}). For k = 3 k=3, let p 1 p_{1} be the leftmost point of S S and p 3 p_{3} be the point that minimizes the convex angle at p 2 p_{2} in the equivalence class of ( p 1, p 2, p 3) (p_{1},p_{2},p_{3}). Then consider moving a point p 1 ′ p^{\prime}_{1} starting at p 1 p_{1} toward the other endpoint of S S. If ( p 1, p 2, p 3) (p_{1},p_{2},p_{3}) ever becomes straight before reaching the endpoint, then S S would have been subdivided further, contradicting its definition. Thus ( p 1 ′, p 2, p 3) (p_{1}^{\prime},p_{2},p_{3}) remains a shortest path. We can use a similar argument to show that, for k = 2 k=2, given two visible points ( p 1, p 2) (p_{1},p_{2}) where p 1 ∈ S p_{1}\in S, every point in S S sees a point on the same edge as p 2 p_{2} (not necessarily p 2 p_{2} itself).

For each segment S S, we can compute a member in each equivalence class of shortest paths from S S in O ⁡ ( n) O(n) time. We map S × ( ∂ P ∖ S) S\times(\partial P\setminus S) to the square subset of the plane [0, 1] × [0, 1] [0,1]\times[0,1]. It is easy to partition the boundary ∂ P \partial P into shortest-path equivalence classes when k ≥ 4 k\geq 4 based on the last endpoint of the shortest path; for example, the set of points p 4 p_{4} on the same edge for which ( p 1, p 2, p 3, p 4) (p_{1},p_{2},p_{3},p_{4}) is a shortest path for all p 1 ∈ S p_{1}\in S and fixed p 2, p 3 p_{2},p_{3} can be computed from the line arrangement. Each equivalence class corresponds to a horizontal slab in the square. The intervals I I of the boundary ∂ P \partial P for which there are one-or-two-edge ( k ∈ { 2, 3 } k\in\{2,3\}) shortest paths from S S to I I, the distance function is more complicated. The set S × I S\times I corresponds to a horizontal slab of the square [0, 1] × [0, 1] [0,1]\times[0,1]. The boundary between points on this square corresponding to one-edge shortest paths and points corresponding to two-edge shortest paths are straight lines connecting the left and right edges of the square, because such points correspond to shortest paths ( p 1, p 2, p 3) (p_{1},p_{2},p_{3}) where the points are collinear for fixed p 2 p_{2}, and p 1 ∈ S p_{1}\in S. Moreover, the projection of such boundary line segments to the y y axis are interior-disjoint. Using these boundary lines, we can compute a partition of the square into regions and, for each region, compute d h ​ ( p, q) d_{h}(p,q) efficiently because either we know p p and q q are visible from each other or we know the points p 2, …, p k − 1 p_{2},\ldots,p_{k-1} through which the shortest path passes.

Figure 4: Two “hourglasses”, one inside and the other outside P P, representing a region S 1 × S 2 S_{1}\times S_{2} where shortest paths (inside or outside P P) between S 1 S_{1} and S 2 S_{2} are in the same equivalence class.

The computation of d z d_{z} can be done in a similar manner, but using (geodesic) shortest paths on the exterior of P P. The partition of ∂ P \partial P into regions S S with combinatorially equivalent shortest paths is exactly the same. For each S S, we obtain a new partition of O ⁡ ( n) O(n) regions in the square [0, 1] × [0, 1] [0,1]\times[0,1] corresponding to S × ( ∂ P ∖ S) S\times(\partial P\setminus S). Overlaying both escaper and pursuer partitions of the square, we obtain O ⁡ ( n) O(n) regions because of the horizontal separation between nonhorizontal boundaries. Figure 4 illustrates one such a region S 1 × S 2 S_{1}\times S_{2}. For each region, computing max p ∈ S 1, q ∈ S 2 ⁡ d z ​ ( p, q) d h ​ ( p, q) \max_{p\in S_{1},q\in S_{2}}\frac{d_{z}(p,q)}{d_{h}(p,q)} becomes a constant-size optimization problem of the form max x, y ∈ [0, 1] ⁡ f ⁡ ( x, y) g ⁡ ( x, y) \max_{x,y\in[0,1]}\frac{f(x,y)}{g(x,y)} where f, g f,g are functions on the segment parameters x, y x,y of the form x 2 + a + x 2 + b + y 2 + c + y 2 + d + e \sqrt{x^{2}+a}+\sqrt{x^{2}+b}+\sqrt{y^{2}+c}+\sqrt{y^{2}+d}+e. (The constant distances a, b, c, d, e a,b,c,d,e in each function f, g f,g can be computed exactly on a real RAM, or approximated using standard methods for computing square roots, such as Newton’s Method.) This optimization can be solved by computing the gradient of f ⁡ ( x, y) g ⁡ ( x, y) \frac{f(x,y)}{g(x,y)} and setting it to zero. We obtain two equations with two variables ( x x and y y). We argue that each equation is a polynomial of degree at most 48 48. The numerator of a partial derivative of f ⁡ ( x, y) g ⁡ ( x, y) \frac{f(x,y)}{g(x,y)} will contain 8 8 types of square roots w ⁡ ( x, y) \sqrt{w(x,y)} and we can eliminate each by multiplying by 1 − w ⁡ ( x, y) 1-\sqrt{w(x,y)}. Each such multiplication blows up the degree of our polynomial by a factor of 2 2, for a total of degree 48 48. The system has a constant number of variables and polynomials, and the polynomials have constant degree, so it can be solved using the Existential Theory of Reals in time linear in the bit complexity of the input and output [GV88], i.e., O ⁡ ( log ⁡ 1 ε) O(\log{1\over\varepsilon}) time. Then we take the maximum over all O ⁡ ( n) O(n) regions for the segment, and take the maximum over all O ⁡ ( n 3) O(n^{3}) segments S S of the boundary, for a total of O ⁡ ( n 4 ​ log ⁡ 1 ε) O(n^{4}\log{1\over\varepsilon}) time. ∎

In the case where the exit set X X is the entire boundary ∂ P \partial P, the following lemma allows us to simplify the analysis in Theorem 3.3 by limiting our attention to regions where the escaper shortest path (inside P P) has a single edge.

###### Lemma 3.4.

If D h D_{h} is a polygon, then there is a pair ( p, q) (p,q) of points on its boundary maximizing d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,q)}{d_{h}(p,q)} for which the shortest path inside D h D_{h} between p p and q q intersects D h D_{h} only at p p and q q.

###### Proof.

Suppose that ( p, q) (p,q) is a pair of points for which d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,q)}{d_{h}(p,q)} is maximized and, of such pairs, ( p, q) (p,q) minimizes the number of segments (possibly single vertices) of D h D_{h} ’s boundary that intersects with the shortest path inside D h D_{h} between p p and q q; see Figure 1(b) for an example. (Because D h D_{h} is a polygon, that number of segments is always finite—in particular, at most the number of sides of the polygon—so we can choose to minimize it. This is the only place we use the assumption that D h D_{h} is a polygon.) Suppose for contradiction that there is a segment on the boundary of D h D_{h}, that does not contain p p or q q, through which the shortest path from p p to q q passes, and let a a be an endpoint of it. Then d z ​ ( p, a) d h ​ ( p, a) ≤ d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,a)}{d_{h}(p,a)}\leq\frac{d_{z}(p,q)}{d_{h}(p,q)} and d z ​ ( a, q) d h ​ ( a, q) ≤ d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(a,q)}{d_{h}(a,q)}\leq\frac{d_{z}(p,q)}{d_{h}(p,q)}. Note that by algebra,

 | d z ​ ( p, a) + d z ​ ( a, q) d h ​ ( p, a) + d h ​ ( a, q) ≤ max ⁡ ( d z ​ ( p, a) d h ​ ( p, a), d z ​ ( a, q) d h ​ ( a, q)), \frac{d_{z}(p,a)+d_{z}(a,q)}{d_{h}(p,a)+d_{h}(a,q)}\leq\max\left(\frac{d_{z}(p,a)}{d_{h}(p,a)},\frac{d_{z}(a,q)}{d_{h}(a,q)}\right), |  |

with equality only if one of the distances is 0 (impossible by assumption) or d z ​ ( p, a) d h ​ ( p, a) = d z ​ ( a, q) d h ​ ( a, q) \frac{d_{z}(p,a)}{d_{h}(p,a)}=\frac{d_{z}(a,q)}{d_{h}(a,q)}. Also, by the triangle inequality, d z ​ ( p, q) ≤ d z ​ ( p, a) + d z ​ ( a, q) d_{z}(p,q)\leq d_{z}(p,a)+d_{z}(a,q), and by the assumption that a a is on the shortest interior path between p p and q q, d h ​ ( p, q) ≥ d h ​ ( p, a) + d h ​ ( a, q) d_{h}(p,q)\geq d_{h}(p,a)+d_{h}(a,q), so

 | d z ​ ( p, q) d h ​ ( p, q) ≤ d z ​ ( p, a) + d z ​ ( a, q) d h ​ ( p, a) + d h ​ ( a, q) ≤ max ⁡ ( d z ​ ( p, a) d h ​ ( p, a), d z ​ ( a, q) d h ​ ( a, q)) ≤ d z ​ ( p, q) d h ​ ( p, q), \frac{d_{z}(p,q)}{d_{h}(p,q)}\leq\frac{d_{z}(p,a)+d_{z}(a,q)}{d_{h}(p,a)+d_{h}(a,q)}\leq\max\left(\frac{d_{z}(p,a)}{d_{h}(p,a)},\frac{d_{z}(a,q)}{d_{h}(a,q)}\right)\leq\frac{d_{z}(p,q)}{d_{h}(p,q)}, |  |

so we must have equality at every step. In particular, d z ​ ( p, a) d h ​ ( p, a) = d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,a)}{d_{h}(p,a)}=\frac{d_{z}(p,q)}{d_{h}(p,q)}, so ( p, a) (p,a) is a pair of points for which d z ​ ( p, a) d h ​ ( p, a) \frac{d_{z}(p,a)}{d_{h}(p,a)} is maximized and the number of segments of D h D_{h} ’s boundary that the shortest path inside D h D_{h} between p p and a a intersects is less than the corresponding number for p p and q q, contradicting the choice of p p and q q. Hence the shortest path inside D h D_{h} between p p and q q intersects the polygon only at p p and q q, as claimed. ∎

## 4 Exact Solutions

In this section, we compute the precise critical speed ratio for a few specific escaper domains: a wedge (Section 4.1), a halfplane with specified starting positions (Section 4.2), the unit disk (Section 4.4), and two challenging cases — the equilateral triangle (Section 4.5) and the square (Section 4.6). Motivated by the winning escaper strategy for the wedge and halfplane, we also develop a generalized escaper strategy called APLO (Section 4.3), which we use to compute critical speed ratios in the later sections. Because the optimal pursuer strategies we prove never leave the convex boundary of the escaper domain, our results apply in both the moat and exterior models. The optimal escaper strategies we prove do not touch the boundary of the escaper domain until the moment of escape, so they trivially extend to the capture model described in Section 1.

### 4.1 Wedge

While the case of an infinite wedge is not particularly interesting by itself, a wedge models the local behavior around a vertex of a polygon, which will be useful later.

###### Theorem 4.1.

If the escaper domain is a wedge, i.e., an unbounded intersection of two halfplanes, having positive angle 2 ​ θ ≤ π 2\theta\leq\pi, the critical speed ratio is r ∗ = 1 / sin ⁡ θ r^{*}=1/\sin\theta.

###### Proof.

Let o = ( 0, 0) o=(0,0) be the apex of the wedge (or any point on the boundary if 2 ​ θ = π 2\theta=\pi); refer to Figure 5. Define right-handed coordinate frame ( x ^, y ^) (\hat{x},\hat{y}) such that x ^ \hat{x} is the unit vector parallel to the angle bisector of the wedge, where every point p = ( x, y) p=(x,y) in the wedge satisfies x ≥ 0 x\geq 0, and y ^ \hat{y} is the counterclockwise rotation of x ^ \hat{x} by 90 ∘ 90^{\circ}.

We first provide a winning pursuer strategy when r = r ∗ r=r^{*}: if the escaper is at point h = ( x, y) h=(x,y), the pursuer will be at boundary point z = ( | y | / tan ⁡ θ, y) z=(|y|/\tan\theta,y). This pursuer strategy satisfies the escaper-start constraint and the nonbranching-lookahead constraint (it only depends on the current position of the escaper) with paths that satisfy the speed-limit constraint: given points H ⁡ ( t) = ( x 1, y 1), H ⁡ ( t + τ) = ( x 2, y 2) H(t)=(x_{1},y_{1}),H(t+\tau)=(x_{2},y_{2}) on the escaper path, noting that ( | y 2 | − | y 1 |) 2 ≤ ( y 2 − y 1) 2 (|y_{2}|-|y_{1}|)^{2}\leq(y_{2}-y_{1})^{2},

 | ‖ z ⁡ ( t + τ) − z ⁡ ( t) ‖ ‖ H ⁡ ( t + τ) − H ⁡ ( t) ‖ ≤ ( | y 2 | − | y 1 |) 2 / tan 2 ⁡ θ + ( y 2 − y 1) 2 | y 2 − y 1 | ≤ r ∗ ​ ( 1 / tan 2 ⁡ θ + 1) ​ sin 2 ⁡ θ = r ∗, \frac{\|z(t+\tau)-z(t)\|}{\|H(t+\tau)-H(t)\|}\leq\frac{\sqrt{(|y_{2}|-|y_{1}|)^{2}/\tan^{2}\theta+(y_{2}-y_{1})^{2}}}{|y_{2}-y_{1}|}\leq r^{*}\sqrt{(1/\tan^{2}\theta+1)\sin^{2}\theta}=r^{*}, |  |

as desired. This strategy is winning for the pursuer, as whenever the escaper is at a boundary point p p the pursuer is also at p p.

Next, we provide a winning escaper strategy when r = r ∗ − ε r=r^{*}-\varepsilon for any ε > 0 \varepsilon>0. The escaper begins at point s h = ( cos ⁡ θ, 0) s_{h}=(\cos\theta,0) on the angle bisector, and the pursuer chooses a starting point s z = ( | d | ​ cos ⁡ θ, d ​ sin ⁡ θ) s_{z}=(|d|\cos\theta,d\sin\theta) on the boundary. Without loss of generality, assume the pursuer starts below the angle bisector with d ≤ 0 d\leq 0. If 2 ​ θ < π 2\theta<\pi the escaper runs at full speed to point p = ( cos ⁡ θ, sin ⁡ θ) p=(\cos\theta,\sin\theta); otherwise if 2 ​ θ = π 2\theta=\pi, the escaper runs to point ( 0, 1) (0,1). This escaper strategy satisfies the escaper-start constraint and the nonbranching-lookahead constraint (it only depends on the starting position of the pursuer) with paths that satisfy the speed-limit condition (escaper speed is always one). We claim this escaper strategy wins G δ G_{\delta} for 0 < δ < ε ​ sin ⁡ θ 0<\delta<\varepsilon\sin\theta when 2 ​ θ < π 2\theta<\pi, and wins for 0 < δ < ε 0<\delta<\varepsilon when 2 ​ θ = π 2\theta=\pi. In both cases, the distance between s z s_{z} and p p in the pursuer metric is 1 + | d | 1+|d|. When 2 ​ θ < π 2\theta<\pi, the escaper reaches p p in time t h = sin ⁡ θ t_{h}=\sin\theta, whereas the pursuer travels at most distance r ​ t h = ( r ∗ − ε) ​ sin ⁡ θ rt_{h}=(r^{*}-\varepsilon)\sin\theta; so when the escaper reaches p p, the pursuer is at least distance ( 1 + | d |) − ( r ∗ − ε) ​ sin ⁡ θ ≥ ε ​ sin ⁡ θ (1+|d|)-(r^{*}-\varepsilon)\sin\theta\geq\varepsilon\sin\theta from p p. Alternatively, when 2 ​ θ = π 2\theta=\pi, the escaper reaches p p in time 1 1, whereas the pursuer travels at most distance r = 1 − ε r=1-\varepsilon; so when the escaper reaches p p, the pursuer is at least distance ( 1 + | d |) − ( 1 − ε) = ε (1+|d|)-(1-\varepsilon)=\varepsilon from p p. ∎

Figure 5: Geometry of winning strategies in a wedge [Left] and halfplane [Right].

### 4.2 G ⁡ ( s h, s z) G(s_{h},s_{z}) in a Halfplane

A halfplane is a special case of a wedge, so Theorem 4.1 implies that the critical speed ratio of a halfplane is 1 1. We generalize this strategy to find the critical speed ratio for the game G ⁡ ( s h, s z) G(s_{h},s_{z}) with prescribed escaper and pursuer starting positions, s h s_{h} and s z s_{z} respectively (like the Lion and Man problem). The halfplane case models the local behavior around an edge of a polygon after running another partial strategy, which again will be useful later.

###### Theorem 4.2.

If the escaper domain is the halfplane, the critical speed ratio for the game G ⁡ ( s h, s z) G(s_{h},s_{z}) is r ∗ = 1 / sin ⁡ θ r^{*}=1/\sin\theta where angle θ = ∠ ​ s h ​ s z ​ h ′ ≤ π / 2 \theta=\angle s_{h}s_{z}h^{\prime}\leq\pi/2 and h ′ h^{\prime} the closest boundary point to s h s_{h} (or any other boundary point if the closest boundary point is s z s_{z}).

###### Proof.

If s h s_{h} is on the boundary, either s h = s z s_{h}=s_{z} and r ∗ = 1 r^{*}=1, or s h ≠ s z s_{h}\neq s_{z} and r ∗ = ∞ r^{*}=\infty. Otherwise, without loss of generality, let s z = ( 0, 0) s_{z}=(0,0) and s h = ( 1, 0) s_{h}=(1,0).

We first provide a winning pursuer strategy when r = r ∗ r=r^{*}: if the escaper is at point h = ( x, y) h=(x,y), the pursuer will be at boundary point z = ( y / tan ⁡ θ, y) z=(y/\tan\theta,y). This pursuer strategy satisfies the nonbranching-lookahead constraint (it only depends on the current position of the escaper) with paths that satisfy the speed-limit constraint: given points H ⁡ ( t) = ( x 1, y 1), H ⁡ ( t + τ) = ( x 2, y 2) H(t)=(x_{1},y_{1}),H(t+\tau)=(x_{2},y_{2}) on the escaper path,

 | ‖ z ⁡ ( t + τ) − z ⁡ ( t) ‖ ‖ H ⁡ ( t + τ) − H ⁡ ( t) ‖ ≤ ( y 2 − y 1) 2 / tan 2 ⁡ θ + ( y 2 − y 1) 2 | y 2 − y 1 | ≤ r ∗ ​ ( 1 / tan 2 ⁡ θ + 1) ​ sin 2 ⁡ θ = r ∗, \frac{\|z(t+\tau)-z(t)\|}{\|H(t+\tau)-H(t)\|}\leq\frac{\sqrt{(y_{2}-y_{1})^{2}/\tan^{2}\theta+(y_{2}-y_{1})^{2}}}{|y_{2}-y_{1}|}\leq r^{*}\sqrt{(1/\tan^{2}\theta+1)\sin^{2}\theta}=r^{*}, |  |

as desired. This strategy is winning for the pursuer, as whenever the escaper is at a boundary point p p the pursuer is also at p p.

Next, we provide a winning escaper strategy when r = r ∗ − ε r=r^{*}-\varepsilon for any ε > 0 \varepsilon>0: if θ < π / 2 \theta<\pi/2, the escaper runs straight to p = ( 1, tan ⁡ θ) p=(1,\tan\theta) at full speed; otherwise if θ = π / 2 \theta=\pi/2, the escaper runs to s z s_{z} at full speed, and then to p = ( 0, 1) p=(0,1). This escaper strategy satisfies the nonbranching-lookahead constraint (it only depends on the starting pursuer position) with paths that satisfy the speed-limit constraint (the escaper speed is always 1 1). We claim that this strategy wins G δ G_{\delta}, for 0 < δ < ε ​ tan ⁡ θ 0<\delta<\varepsilon\tan\theta when θ < π / 2 \theta<\pi/2, and for 0 < δ < ε / 2 0<\delta<\varepsilon/2 when θ = π / 2 \theta=\pi/2. When θ < π / 2 \theta<\pi/2, the escaper reaches p p in time t h = tan ⁡ θ t_{h}=\tan\theta, and the distance between s z s_{z} and p p is 1 + tan 2 ⁡ θ = 1 / cos ⁡ θ \sqrt{1+\tan^{2}\theta}=1/\cos\theta. However, the pursuer can travel at most distance r ​ t h = ( r ∗ − ε) ​ t h = 1 / cos ⁡ θ − ε ​ tan ⁡ θ rt_{h}=(r^{*}-\varepsilon)t_{h}=1/\cos\theta-\varepsilon\tan\theta in that time, at least distance ε ​ tan ⁡ θ \varepsilon\tan\theta from p p. Alternatively, 2 ​ θ = π 2\theta=\pi; when the escaper first reaches s z s_{z} the pursuer is within δ \delta of s z s_{z} or else the escaper has already won. Then escaper reaches p p in time 2 2, whereas the pursuer travels at most distance r = 1 − ε < 1 − 2 ​ δ r=1-\varepsilon<1-2\delta; so when the escaper reaches p p, the pursuer is at least distance ( 1 − δ) − ( 1 − ε) > δ (1-\delta)-(1-\varepsilon)>\delta from p p as desired. ∎

### 4.3 APLO Strategy

The strategy employed by the escaper in the previous section is quite simple: pick a point on the boundary and run to it at full speed. Motivated by this escaper strategy, we define a useful generalization which interpolates between two extreme straight-line strategies depending on the position of pursuer, which we will use to prove the critical speed ratio for the disk, equilateral triangle, and square.

###### Definition 1.

For games where the pursuer domain is a topological circle, let D ⁡ ( z, t) D(z,t) denote the net signed counterclockwise distance 6 6 6 For example, if the pursuer domain has length ℓ \ell and the pursuer starts at z ⁡ ( 0) z(0) and in time t t circles the boundary clockwise exactly three times back to z ⁡ ( 0) z(0) and then runs counterclockwise a distance ℓ / 3 \ell/3, then D ( z, t) = − 8 ℓ / 3 D(z,t)=-8\ell/3. Note that the net signed distance D ⁡ ( z, t) D(z,t) only depends on z ⁡ ( t) z(t) and the homotopy type of the pursuer’s path up to time t t. from z ⁡ ( 0) z(0) to z ⁡ ( t) z(t) counterclockwise along the pursuer domain, for any pursuer path z ⁡ ( t) z(t). Given:

- •

an escaper starting position h 0 h_{0},

- •

a preferred forward “axial” unit vector u ^ \hat{u} (referencing also the “lateral” unit vector v ^ \hat{v} which is u ^ \hat{u} rotated by a quarter-turn counterclockwise in the plane),

- •

speed ratio r ′ r^{\prime} (which must be an upper bound on pursuer speed), and

- •

positive axial and lateral speeds d u d_{u} and d v d_{v} (which must satisfy d u 2 + d v 2 ≤ 1 \sqrt{d_{u}^{2}+d_{v}^{2}}\leq 1),

we define the axially progressing laterally opposing (APLO) escaper strategy as follows (see Figure 6): for a pursuer at position z ⁡ ( t) z(t) at time t t, the escaper is at position:

 | H A ​ P ​ L ​ O ​ ( z, t, h 0, u ^, r ′, d u, d v) = h 0 + ( t ​ d u) ⋅ u ^ + ( D ⁡ ( z, t) r ′ ​ d v) ⋅ v ^. H_{APLO}(z,t;h_{0},\hat{u},r^{\prime},d_{u},d_{v})=h_{0}+(td_{u})\cdot\hat{u}+\left(\frac{D(z,t)}{r^{\prime}}d_{v}\right)\cdot\hat{v}. |  |

Figure 6: Geometry of APLO strategy H A ​ P ​ L ​ O ​ ( z, t, h 0, u ^, r ′, d u, d v) H_{APLO}(z,t;h_{0},\hat{u},r^{\prime},d_{u},d_{v}), where d v = sin ⁡ ( α) d_{v}=\sin(\alpha) (and hence d u = cos ⁡ ( α) d_{u}=\cos(\alpha)). The shaded wedge represent the possible escaper positions.

For example, if the pursuer runs clockwise at full speed r r then the escaper’s APLO response is to run in a straight line with velocity d u ​ u ^ + r r ′ ​ d v ​ v ^ d_{u}\hat{u}+\frac{r}{r^{\prime}}d_{v}\hat{v}, which by the assumptions placed on our inputs has magnitude at most 1 1. If the pursuer stays at z ⁡ ( 0) z(0) then the escaper runs forward along u ^ \hat{u} at speed d u d_{u}. In general, the escaper always progresses forward (in the u ^ \hat{u} direction) with constant speed d u d_{u}, while the pursuer’s position at time t t dictates the escaper’s lateral offset (in the v ^ \hat{v} direction) at time t t. Observe that this is done in a “memory-less” way: the escaper’s position at time t t depends only on t t and the pursuer’s position at time t t, not on the pursuer’s position at any earlier (or later!) time.

###### Lemma 4.3.

Any APLO escaper strategy H A ​ P ​ L ​ O ​ ( z, t, h 0, u ^, r ′, d u, d v) H_{APLO}(z,t;h_{0},\hat{u},r^{\prime},d_{u},d_{v}) satisfies the escaper-start and nonbranching-lookahead conditions with paths that satisfy the speed-limit condition. In other words, H A ​ P ​ L ​ O H_{APLO} is a valid strategy.

###### Proof.

H A ​ P ​ L ​ O H_{APLO} satisfies the escaper-start condition as at time t = 0 t=0, D ⁡ ( z, t) = 0 D(z,t)=0, so H A ​ P ​ L ​ O H_{APLO} places the escaper at position h 0 + 0 ⋅ u ^ + 0 ⋅ v ^ = h 0 h_{0}+0\cdot\hat{u}+0\cdot\hat{v}=h_{0}, as required.

H A ​ P ​ L ​ O H_{APLO} satisfies the nonbranching-lookahead condition as it does not depend on the pursuer’s position at any time except at time t t.

To show that H A ​ P ​ L ​ O H_{APLO} paths satisfy the speed-limit condition, we must show that after any positive time τ \tau from any time t ≥ 0 t\geq 0, the escaper travels at most distance τ \tau. The distance traveled by escaper between times t t and t + τ t+\tau is:

 | | H A ​ P ​ L ​ O ​ ( z, t) − H A ​ P ​ L ​ O ​ ( z, t + τ) | = τ 2 ​ d v 2 + ( D ⁡ ( z, t) − D ⁡ ( z, t + τ) r ′) 2 ​ d u 2. |H_{APLO}(z,t)-H_{APLO}(z,t+\tau)|=\sqrt{\tau^{2}d_{v}^{2}+\left(\frac{D(z,t)-D(z,t+\tau)}{r^{\prime}}\right)^{2}d_{u}^{2}}. |  |

This distance is maximized when D ⁡ ( z, t) − D ⁡ ( z, t + τ) D(z,t)-D(z,t+\tau) is maximized. Since the pursuer moves at rate at most r r, this distance is at most r ​ τ r\tau. And since r ′ ≥ r r^{\prime}\geq r and d u 2 + d v 2 ≤ 1 \sqrt{d_{u}^{2}+d_{v}^{2}}\leq 1 by assumption on the inputs, the distance the escaper travels is at most τ \tau, proving the claim. ∎

### 4.4 Disk

In this section, we solve for the first time the well-studied case of the disk. While an escaper strategy with this speed ratio was known before, we give an alternative escaper strategy based on our APLO technique. Furthermore, we are not aware of any previous presentation of a matching pursuer strategy.

###### Theorem 4.4.

Let φ ∗ \varphi^{*} be the angle such that tan ⁡ φ ∗ = π + φ ∗ \tan\varphi^{*}=\pi+\varphi^{*}, i.e., φ ∗ ≈ 0.430 ​ π \varphi^{*}\approx 0.430\pi. If the escaper domain is a unit disk, the critical speed ratio is r ∗ = 1 / cos ⁡ φ ∗ ≈ 4.603 r^{*}=1/\cos\varphi^{*}\approx 4.603.

Figure 7: Winning strategy geometries on a unit disk for both pursuer [Left] and escaper [Right].

###### Proof.

Let o o be the center of the unit disk. We first provide a winning pursuer strategy when r ≥ r ∗ r\geq r^{*}. The pursuer starts at the boundary point closest to the escaper start point. When the escaper is greater than distance 1 / r ∗ 1/r^{*} from o o and the pursuer is not at the boundary point h ′ h^{\prime} closest to the escaper, the pursuer moves at full speed along the shorter arc toward h ′ h^{\prime}, breaking ties arbitrarily, and otherwise stands still. This pursuer strategy satisfies the escaper-start constraint and the nonbranching-lookahead constraint (it only depends on the current position of the escaper) with paths that satisfy the speed-limit constraint (pursuer runs at speed at most r ∗ r^{*}). We claim this pursuer strategy is winning.

Suppose for contradiction there exists a winning escaper path H H ending at some boundary point p p. H H must contain at least one point at distance 1 / r ∗ = cos ⁡ φ ∗ 1/r^{*}=\cos\varphi^{*} from o o; otherwise, if H H is always outside the circle of radius 1 / r ∗ 1/r^{*}, the pursuer can at all times match the escaper’s angular velocity without exceeding speed r ∗ r^{*}, so will always exist at the closest boundary point to the escaper (in particular at p p at the end of H H). Then let s h s_{h} be the last point of H H at distance 1 / r ∗ 1/r^{*} from o o, and without loss of generality, assume s h = ( 1 / r ∗, 0) s_{h}=(1/r^{*},0) and p = ( cos ⁡ φ, sin ⁡ φ) p=(\cos\varphi,\sin\varphi) for some 0 ≤ φ < π 0\leq\varphi<\pi (see Figure 7 [Left]). Then the escaper cannot reach p p faster than time t h t_{h}, where:

- •

t h = ( cos ⁡ φ − cos ⁡ φ ∗) 2 + sin 2 ⁡ φ t_{h}=\sqrt{(\cos\varphi-\cos\varphi^{*})^{2}+\sin^{2}\varphi} when 0 ≤ φ ≤ φ ∗ 0\leq\varphi\leq\varphi^{*} (by straight line from s h s_{h} to p p), and

- •

t h > sin ⁡ φ ∗ + ( φ − φ ∗) / r ∗ t_{h}>\sin\varphi^{*}+(\varphi-\varphi^{*})/r^{*} when φ ∗ < φ < π \varphi^{*}<\varphi<\pi (by first running around the circle of radius 1 / r ∗ 1/r^{*}, then in a straight line to p p).

Since the subset of H H after s h s_{h} to p p lies strictly outside the circle of radius 1 / r ∗ 1/r^{*}, the pursuer’s angular velocity around o o is always greater than the escaper’s, meaning the arclength between the pursuer and the closest boundary point to the escaper only decreases, so the pursuer runs in a consistent direction. If this arclength reaches zero, the pursuer can track the closest boundary point to the escaper and the escaper will not win, so if H H wins, the pursuer always runs at full speed toward p p. Let s z = ( cos ⁡ θ, sin ⁡ θ) s_{z}=(\cos\theta,\sin\theta) be the pursuer position when the escaper is at s h s_{h}, and let t z t_{z} be the time the pursuer takes to reach p p. If 0 ≤ θ < π 0\leq\theta<\pi, then t z = | θ − φ | / r ∗ t_{z}=|\theta-\varphi|/r^{*}; otherwise if π ≤ θ < 2 ​ π \pi\leq\theta<2\pi, the pursuer reaches p p in time t z = ( 2 ​ π + φ − θ) / r ∗ t_{z}=(2\pi+\varphi-\theta)/r^{*}. t z t_{z} is maximized when θ = π \theta=\pi, so without loss of generality we can assume that s z = ( − 1, 0) s_{z}=(-1,0) and t z = ( π + φ) / r ∗ t_{z}=(\pi+\varphi)/r^{*}. The pursuer is at p p when the escaper reaches p p if t h − t z ≥ 0 t_{h}-t_{z}\geq 0. When φ > φ ∗ \varphi>\varphi^{*}, observe that

 | t h − t z > ( sin ⁡ φ ∗ + ( φ − φ ∗) / r ∗) − ( π + φ ∗ + ( φ − φ ∗)) / r ∗ = sin ⁡ φ ∗ − tan ⁡ φ ∗ / r ∗ = 0. t_{h}-t_{z}>(\sin\varphi^{*}+(\varphi-\varphi^{*})/r^{*})-(\pi+\varphi^{*}+(\varphi-\varphi^{*}))/r^{*}=\sin\varphi^{*}-\tan\varphi^{*}/r^{*}=0. |  |

Alternatively, when φ ≤ φ ∗ \varphi\leq\varphi^{*}, observe that t h − t z ≥ ( t h − t z) | φ = φ ∗ = 0 t_{h}-t_{z}\geq(t_{h}-t_{z})|_{\varphi=\varphi^{*}}=0, as the derivative of t h − t z t_{h}-t_{z} is never positive over the domain:

 | d d ​ φ ​ ( t h − t z) = − cos ⁡ φ ∗ ​ ( 1 − sin ⁡ φ sin 2 ⁡ φ + ( cos ⁡ φ − cos ⁡ φ ∗) 2) ≤ 0. \frac{d}{d\varphi}(t_{h}-t_{z})=-\cos\varphi^{*}\left(1-\frac{\sin\varphi}{\sqrt{\sin^{2}\varphi+(\cos\varphi-\cos\varphi^{*})^{2}}}\right)\leq 0. |  |

Thus the pursuer is at p p when the escaper reaches p p, a contradiction.

Next, we provide a winning escaper strategy when r = r ∗ − ε r=r^{*}-\varepsilon for any positive ε \varepsilon. The escaper begins on the circle C C of radius 1 / r ∗ 1/r^{*} concentric with the unit disk, and then runs at full speed around C C (with angular speed r ∗ r^{*} about o o) until the escaper and pursuer reach respective positions s h s_{h} and s z s_{z} where ∠ ​ s h ​ o ​ s z = π \angle s_{h}os_{z}=\pi. Without loss of generality, s h = ( cos ⁡ φ ∗, 0) s_{h}=(\cos\varphi^{*},0) and s z = ( − 1, 0) s_{z}=(-1,0). The escaper reaches such a state in finite time because the pursuer can run around the unit disk with angular speed at most r < r ∗ r<r^{*}. Then, the escaper executes APLO strategy H A ​ P ​ L ​ O ​ ( z, t, s h, x ^, r, d u, d v) H_{APLO}(z,t;s_{h},\hat{x},r,d_{u},d_{v}) where z ⁡ ( 0) = s z z(0)=s_{z}, x ^ \hat{x} is the unit direction from s z s_{z} to s h s_{h}, and d v = r / r ∗ < 1 d_{v}=r/r^{*}<1 and d u = 1 − d u 2 d_{u}=\sqrt{1-d_{u}^{2}} (see Figure 7 [Right]). At some finite time t f t_{f} while executing this strategy, the escaper reaches some boundary point p h = ( cos ⁡ φ, sin ⁡ φ) p_{h}=(\cos\varphi,\sin\varphi); without loss of generality assume 0 < φ 0<\varphi. Then at the same time, the pursuer is at point p z = ( cos ⁡ ( θ − π), sin ⁡ ( θ − π)) p_{z}=(\cos(\theta-\pi),\sin(\theta-\pi)) where θ = D ⁡ ( z, t f) = r ​ sin ⁡ φ / d v = r ∗ ​ sin ⁡ φ \theta=D(z,t_{f})=r\sin\varphi/d_{v}=r^{*}\sin\varphi by definition of APLO.

We claim this strategy wins G δ G_{\delta} for some δ > 0 \delta>0, i.e., p z ≠ p h p_{z}\neq p_{h}. It suffices to show that φ > θ − π \varphi>\theta-\pi. Since φ < φ ∗ \varphi<\varphi^{*} and function f ⁡ ( x) = ( sin ⁡ x) / ( π + x) f(x)=(\sin x)/(\pi+x) strictly increases over the domain 0 ≤ φ < φ ∗ 0\leq\varphi<\varphi^{*},

 | φ − ( θ − π) = ( π + φ) − r ∗ ​ sin ⁡ φ = ( π + φ) ​ ( 1 − π + φ ∗ sin ⁡ φ ∗ ​ sin ⁡ φ π + φ) > 0, \varphi-(\theta-\pi)=(\pi+\varphi)-r^{*}\sin\varphi=(\pi+\varphi)\left(1-\frac{\pi+\varphi^{*}}{\sin\varphi^{*}}\frac{\sin\varphi}{\pi+\varphi}\right)>0, |  |

proving the claim. ∎

### 4.5 Equilateral Triangle

The equilateral triangle is perhaps the simplest polygon, so serves as a natural starting point for exact bounds:

###### Theorem 4.5.

If the escaper domain is an equilateral triangle, the critical speed ratio is r ∗ = ( 3 + 5) ​ 2 ≈ 7.405 r^{*}=(3+\sqrt{5})\sqrt{2}\approx 7.405.

Figure 8: Geometry for computing the critical speed ratio r ∗ = 1 / sin ⁡ θ ∗ r^{*}=1/\sin\theta^{*} for a triangle.

Let θ ∗ < π / 2 \theta^{*}<\pi/2 be the positive angle such that r ∗ = 1 / sin ⁡ θ ∗ r^{*}=1/\sin\theta^{*}; see Figure 8. The speed ratio r ∗ r^{*} is chosen such that if the pursuer is at corner a a and the escaper is at point s a s_{a} at distance ( 3 − 3 tan θ ∗) / 2 = 3 ​ ( 7 − 3 ​ 5) / 2 ≈ 0.6616 (\sqrt{3}-3\tan\theta^{*})/2=\sqrt{3(7-3\sqrt{5})/2}\approx 0.6616 along the angle bisector of a a, then the escaper has four simultaneous threats to exit at p p, p ′ p^{\prime}, q q, and q ′ q^{\prime}. Specifically, the escaper distance from s a s_{a} to p p is exactly factor r ∗ r^{*} smaller than the pursuer distance counterclockwise from a a to b b to p p, i.e., r ∗ ​ ‖ s a − p ‖ = 1 + ‖ b − p ‖ r^{*}\|s_{a}-p\|=1+\|b-p\|, and the escaper distance from s a s_{a} to q q is exactly a factor r ∗ r^{*} smaller than the pursuer distance from a a to b b to c c to q q, i.e., r ∗ ​ ‖ s a − q ‖ = 2 + ‖ c − q ‖ r^{*}\|s_{a}-q\|=2+\|c-q\|; and similarly for p ′ p^{\prime} and q ′ q^{\prime} in the clockwise direction.

###### Proof.

We first provide a winning pursuer strategy when r ≥ r ∗ r\geq r^{*}. Our pursuer strategy transitions between six different strategies as the escaper move within the triangle. These six strategies z ⁡ ( h, i, j) z(h;i,j) are shown in Figure 9, where each strategy is associated with a corner i ∈ { a, b, c } i\in\{a,b,c\} and a sign j ∈ { − 1, 1 } j\in\{-1,1\}. Each of these strategies is identical up to rotations and reflections, so let us first focus on one of the strategies, z ⁡ ( h, a, 1) z(h;a,1).

Figure 9: Transitions between pursuer strategies.

The z ⁡ ( h, a, 1) z(h;a,1) strategy, depicted in Figure 10, maps each point of the colored subset of the triangle to a point on the boundary via a piecewise-linear map. Wherever the escaper is in the colored region of a strategy, the strategy will place the pursuer at the boundary point designated by the map. To make it easier to reference points on the boundary, we map each boundary point on edge a ​ b ab and edge a ​ c ac to a number, varying linearly from − 1 -1 at vertex b b (yellow), to 0 0 at vertex a a (blue), to 1 1 at vertex c c (red). The left drawing of Figure 10 depicts the geometry of the linear patches of this map:

Figure 10: Geometry of z ⁡ ( h, a, 1) z(h;a,1). This function is linear in each region a ​ b ​ b ′ abb^{\prime}, a ​ b ′ ​ s c ​ t ab^{\prime}s_{c}t, b ′ ​ s a ​ r ​ s c b^{\prime}s_{a}rs_{c}, r ​ s b ​ t ​ s c rs_{b}ts_{c}, a ​ t ​ s b ​ c ats_{b}c, and c ​ s b ​ r ​ s a cs_{b}rs_{a}, where points { a, b ′, s a, c ′ } \{a,b^{\prime},s_{a},c^{\prime}\} have value 0 0 (blue), points { b, s c, r, s b } \{b,s_{c},r,s_{b}\} have value − 1 -1 (yellow), and point c c has value 1 1 (red).

- •

point s i s_{i} for i ∈ { a, b, c } i\in\{a,b,c\} is distance 3 ​ ( 7 − 3 ​ 5) / 2 ≈ 0.6616 \sqrt{3(7-3\sqrt{5})/2}\approx 0.6616 along the angle bisector of corner i i;

- •

point b ′ b^{\prime} is the midpoint of segment b ​ s c bs_{c};

- •

point c ′ c^{\prime} is the midpoint of segment c ​ s b cs_{b};

- •

point t t is the intersection of the angle bisector of a a and the line though s c s_{c} parallel to segment a ​ b ′ ab^{\prime}; and

- •

point r r is the intersection of the angle bisector of a a and the line through b ′ b^{\prime} parallel to segment b ′ ​ s a b^{\prime}s_{a}.

We specify each linear patch by specifying the value at each vertex:

- •

points { a, b ′, s a, c ′ } \{a,b^{\prime},s_{a},c^{\prime}\} have value 0 0 (blue),

- •

points { b, s c, r, s b } \{b,s_{c},r,s_{b}\} have value − 1 -1 (yellow), and

- •

point c c has value 1 1 (red).

This map has the property that the gradient at every point within each linear patch has the same value, namely r ∗ r^{*}. Thus, as the escaper moves within the colored region, the pursuer’s speed will always stay below r ∗ ≤ r r^{*}\leq r, so the strategy will be valid. This map also has the property that the pursuer and the escaper will be collocated whenever the escaper is on edges a ​ b ab or a ​ c ac, so the escaper cannot win along those edges. If the escaper reaches edge b ​ s a bs_{a} or edge c ​ s a cs_{a}, the pursuer will switch strategies, respectively to either z ⁡ ( h, b, − 1) z(h;b,-1) or z ⁡ ( h, c, 1) z(h;c,1). These strategies exactly match strategy z ⁡ ( h, a, 1) z(h;a,1) along their respective transition edges. By transitioning between these strategies via the transition graph shown in Figure 9, the pursuer will always be collocated with the escaper whenever the escaper is at the boundary, as desired.

Next, we provide a winning escaper strategy when r = r ∗ − ε r=r^{*}-\varepsilon for any positive ε \varepsilon. Our escaper strategy follows a similar strategy as the circle escaper strategy: reach a state where the escaper can win via a single APLO strategy. In particular, when the escaper is on the boundary of triangle T = s a ​ s b ​ s c T=s_{a}s_{b}s_{c} (e.g., at some point p h p_{h} on s b ​ s c s_{b}s_{c}), and the pursuer is antipodal along the opposite edge boundary with the same ratio (e.g., at point p z p_{z} along segment b ​ c bc where ‖ b − p z ‖ / 1 = ‖ s b − p h ‖ / ‖ s b − s c ‖ \|b-p_{z}\|/1=\|s_{b}-p_{h}\|/\|s_{b}-s_{c}\|), then the escaper will be able to win via an APLO strategy to the boundary. We will reach such a configuration in two phases.

In the first phase, the escaper starts anywhere on T ′ = t a ​ t b ​ t c T^{\prime}=t_{a}t_{b}t_{c}, the triangle formed by connecting the midpoints of triangle T T. Let m a m_{a}, m b m_{b}, and m c m_{c} be the midpoints of b ​ c bc, c ​ a ca, and a ​ b ab respectively; see Figure 11. The perimeter of T ′ T^{\prime} has length 3 ​ ( 7 − 3 ​ 5) / 4 ≈ 0.2188 3(7-3\sqrt{5})/4\approx 0.2188 which is less than 3 / r ∗ ≈ 0.4051 3/r^{*}\approx 0.4051, so the escaper can run around T ′ T^{\prime} faster than the pursuer can run around the boundary. The escaper runs around T ′ T^{\prime} until the escaper reaches a position p h ​ 1 p_{h1} on T ′ T^{\prime} such that the pursuer’s position p z ​ 1 p_{z1} is antipodal. Without loss of generality, assume p h ​ 1 p_{h1} is on segment t a ​ t b t_{a}t_{b} and p z ​ 1 p_{z1} is antipodal on segment c ​ m a cm_{a} such that ‖ m a − p z ​ 1 ‖ / 1 = ‖ t a − p h ​ 1 ‖ / ‖ t a − t b ‖ \|m_{a}-p_{z1}\|/1=\|t_{a}-p_{h1}\|/\|t_{a}-t_{b}\|.

Figure 11: Geometry of the escaper strategy for a triangle.

Now that the escaper is antipodal to the pursuer on T ′ T^{\prime}, the escaper enters the second phase, executing an APLO strategy H A ​ P ​ L ​ O ​ ( z, t, p h ​ 1, c ^, r, d u, d v) H_{APLO}(z,t;p_{h1},\hat{c},r,d_{u},d_{v}) where c ^ \hat{c} is the unit direction from c c to m c m_{c}, d v = ‖ t a − t b ‖ ​ r < 1 d_{v}=\|t_{a}-t_{b}\|r<1, and d u = 1 − d v 2 < 1 d_{u}=\sqrt{1-d_{v}^{2}}<1, until the escaper reaches triangle T T at some point p h ​ 2 p_{h2}. By definition of APLO, during this process the escaper’s projection onto segment t a ​ t b t_{a}t_{b} remains antipodal to the pursuer, so when the escaper reaches p h ​ 2 p_{h2}, the pursuer is at a point p z ​ 2 p_{z2} antipodal to p h ​ 2 p_{h2} on T T. Without loss of generality, assume p h ​ 2 p_{h2} is on segment t a ​ s c t_{a}s_{c} and p z ​ 2 p_{z2} is antipodal on segment c ​ m a cm_{a} such that ‖ m a − p z ​ 1 ‖ / 1 = ‖ t a − p h ​ 2 ‖ / ‖ s b − s c ‖ \|m_{a}-p_{z1}\|/1=\|t_{a}-p_{h2}\|/\|s_{b}-s_{c}\|. Let x z ​ 2 = ‖ m a − p z ​ 1 ‖ x_{z2}=\|m_{a}-p_{z1}\|, let d s = ‖ s b − s c ‖ = ( 7 − 3 ​ 5) / 2 d_{s}=\|s_{b}-s_{c}\|=(7-3\sqrt{5})/2, and let x h ​ 2 = ‖ t a − p h ​ 2 ‖ = x z ​ 2 ​ d s x_{h2}=\|t_{a}-p_{h2}\|=x_{z2}d_{s}.

Now that the escaper is antipodal to the pursuer on T T, the escaper enters the third and final phase, executing an APLO strategy H A ​ P ​ L ​ O ​ ( z, t, p h ​ 2, a ^, r, d u, d v) H_{APLO}(z,t;p_{h2},\hat{a},r,d_{u},d_{v}), where a ^ \hat{a} is the unit direction from m a m_{a} to a a, d u = cos ⁡ ( π / 3 + θ ∗) d_{u}=\cos(\pi/3+\theta^{*}), and d v = sin ⁡ ( π / 3 + θ ∗) d_{v}=\sin(\pi/3+\theta^{*}), until the escaper reaches the boundary at some point p h ​ 3 p_{h3}, with the pursuer at some point p z ​ 3 p_{z3}. It remains to show that ‖ p h ​ 3 − p z ​ 3 ‖ \|p_{h3}-p_{z3}\| is bounded away from zero.

If the pursuer remains on b ​ c bc, the escaper wins easily as p h ​ 3 p_{h3} is above the line s c ​ s b s_{c}s_{b}. Otherwise, there are two cases: the pursuer leaves the segment b ​ c bc last through either b b or c c. It suffices to show that the separation of their projections onto segment b ​ c bc is bounded away from zero, specifically quantity | ( p h ​ 3 − t a) ⋅ v ^ − ( p z ​ 3 − t a) ⋅ v ^ | |(p_{h3}-t_{a})\cdot\hat{v}-(p_{z3}-t_{a})\cdot\hat{v}| where v ^ \hat{v} is the unit vector ( b − c) (b-c). Let x h ​ 3 = ( p h ​ 3 − t a) ⋅ v ^ x_{h3}=(p_{h3}-t_{a})\cdot\hat{v}. Note that x h ​ 3 x_{h3} is positive to the left of t a t_{a}.

1. 1.

(Pursuer leaves b ​ c bc through c c): pursuer leaves counter-clockwise from p z ​ 2 p_{z2}, so ( p h ​ 3 − p h ​ 2) ⋅ v ^ = x h ​ 3 − x h ​ 2 ≥ 0 (p_{h3}-p_{h2})\cdot\hat{v}=x_{h3}-x_{h2}\geq 0. Then by APLO, the pursuer travels counter-clockwise from p z ​ 2 p_{z2} by distance r ⁡ ( x h ​ 3 − x h ​ 2) / sin ⁡ ( π / 3 + θ ∗) r(x_{h3}-x_{h2})/\sin(\pi/3+\theta^{*}), for distance 1 / 2 − x z ​ 2 1/2-x_{z2} along edge b ​ c bc, and the remainder along edges a ​ b ab and a ​ c ac. The largest value of x h ​ 3 x_{h3} possible via this APLO strategy varies linearly with x z ​ 2 x_{z2}. When x z ​ 2 = 1 / 2 x_{z2}=1/2, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded above by

 | ( ‖ m c − s c ‖) ​ cos ⁡ ( π / 6 − θ ∗) cos ⁡ ( θ ∗) = 3 − 5 4; \left(\|m_{c}-s_{c}\|\right)\frac{\cos(\pi/6-\theta^{*})}{\cos(\theta^{*})}=\frac{3-\sqrt{5}}{4}; |  |

and when x z ​ 2 = 0 x_{z2}=0, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded above by

 | ( ‖ m c − s c ‖ + 3 2 ​ ‖ s c − t a ‖) ​ cos ⁡ ( π / 6 − θ ∗) cos ⁡ ( θ ∗) = 1 / 4; \left(\|m_{c}-s_{c}\|+\frac{\sqrt{3}}{2}\|s_{c}-t_{a}\|\right)\frac{\cos(\pi/6-\theta^{*})}{\cos(\theta^{*})}=1/4; |  |

so x h ​ 3 ≤ 1 4 + x z ​ 2 ​ ( 9 2 − 2 ​ 5) x_{h3}\leq\frac{1}{4}+x_{z2}\left(\frac{9}{2}-2\sqrt{5}\right). Using this relation and the fact that x h ​ 2 = x z ​ 2 ​ d s x_{h2}=x_{z2}d_{s}, yields:

 | ( p h ​ 3 − t a) ⋅ v ^ − ( p z ​ 3 − t a) ⋅ v ^ = x h ​ 3 − 1 2 ​ ( ( x h ​ 3 − x h ​ 2) ​ r sin ⁡ ( π / 3 + θ ∗) − ( 1 2 − x z ​ 2) − 1) ≥ ( 1 − r r ∗) ​ ( 1 − 2 ​ x z ​ 2 ​ ( 5 − 2)), \displaystyle\begin{aligned} (p_{h3}-t_{a})\cdot\hat{v}-(p_{z3}-t_{a})\cdot\hat{v}&=x_{h3}-\frac{1}{2}\left(\frac{(x_{h3}-x_{h2})r}{\sin(\pi/3+\theta^{*})}-\left(\frac{1}{2}-x_{z2}\right)-1\right)\\ &\geq\left(1-\frac{r}{r^{*}}\right)\left(1-2x_{z2}\left(\sqrt{5}-2\right)\right),\end{aligned} |  | (1) |

which is always strictly positive for r = r ∗ − ε < r ∗ r=r^{*}-\varepsilon<r^{*} and 0 ≤ x z ​ 2 ≤ 1 2 0\leq x_{z2}\leq\frac{1}{2}, as desired.

2. 2.

(Pursuer leaves b ​ c bc through b b): pursuer leaves clockwise from p z ​ 2 p_{z2}, so ( p h ​ 3 − p h ​ 2) ⋅ v ^ = x h ​ 3 − x h ​ 2 ≤ 0 (p_{h3}-p_{h2})\cdot\hat{v}=x_{h3}-x_{h2}\leq 0. Then by APLO, the pursuer travels clockwise from p z ​ 2 p_{z2} by distance r ⁡ ( x h ​ 2 − x h ​ 3) / sin ⁡ ( π / 3 + θ ∗) r(x_{h2}-x_{h3})/\sin(\pi/3+\theta^{*}), for distance 1 / 2 + x z ​ 2 1/2+x_{z2} along edge b ​ c bc, and the remainder along edges a ​ b ab and a ​ c ac. The smallest value of x h ​ 3 x_{h3} possible via this APLO strategy varies linearly with x z ​ 2 x_{z2}. When x z ​ 2 = 0 x_{z2}=0, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded below by

 | − ( ∥ m c − s c ∥ + 3 2 ∥ s c − t a ∥) cos ⁡ ( π / 6 − θ ∗) cos ⁡ ( θ ∗) = − 1 / 4; -\left(\|m_{c}-s_{c}\|+\frac{\sqrt{3}}{2}\|s_{c}-t_{a}\|\right)\frac{\cos(\pi/6-\theta^{*})}{\cos(\theta^{*})}=-1/4; |  |

and when x z ​ 2 = 1 / 2 x_{z2}=1/2, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded below by

 | − ( ‖ m c − s c ‖ + 3 ​ ‖ s c − t a ‖) ​ cos ⁡ ( π / 6 − θ ∗) cos ⁡ ( θ ∗) = − 5 − 1 4; -\left(\|m_{c}-s_{c}\|+\sqrt{3}\|s_{c}-t_{a}\|\right)\frac{\cos(\pi/6-\theta^{*})}{\cos(\theta^{*})}=-\frac{\sqrt{5}-1}{4}; |  |

so x h ​ 3 ≥ − 1 4 + x z ​ 2 ​ ( 9 2 − 2 ​ 5) x_{h3}\geq-\frac{1}{4}+x_{z2}\left(\frac{9}{2}-2\sqrt{5}\right). Using this relation and the fact that x h ​ 2 = x z ​ 2 ​ d s x_{h2}=x_{z2}d_{s}, yields

 | ( p h ​ 3 − t a) ⋅ v ^ − ( p z ​ 3 − t a) ⋅ v ^ = x h ​ 3 − 1 2 ​ ( − ( x h ​ 2 − x h ​ 3) ​ r sin ⁡ ( π / 3 + θ ∗) + ( 1 2 + x z ​ 2) + 1) ≤ − ( 1 − r r ∗) ​ ( 1 − 2 ​ x z ​ 2 ​ ( 5 − 2)), \displaystyle\begin{aligned} (p_{h3}-t_{a})\cdot\hat{v}-(p_{z3}-t_{a})\cdot\hat{v}&=x_{h3}-\frac{1}{2}\left(-\frac{(x_{h2}-x_{h3})r}{\sin(\pi/3+\theta^{*})}+\left(\frac{1}{2}+x_{z2}\right)+1\right)\\ &\leq-\left(1-\frac{r}{r^{*}}\right)\left(1-2x_{z2}\left(\sqrt{5}-2\right)\right),\end{aligned} |  | (2) |

which is always strictly negative for r = r ∗ − ε < r ∗ r=r^{*}-\varepsilon<r^{*} and 0 ≤ x z ​ 2 ≤ 1 2 0\leq x_{z2}\leq\frac{1}{2}, as desired. ∎

### 4.6 Square

The square is perhaps the next simplest polygon after the equilateral triangle. We show how to extend our exact techniques for this polygon as well:

###### Theorem 4.6.

If the escaper domain is a square, the critical speed ratio is
r ∗ = 5 2 ​ ( 7 + 41) ≈ 5.789 r^{*}=\sqrt{\frac{5}{2}(7+\sqrt{41})}\approx 5.789.

Similar to the triangle case, the speed ratio r ∗ r^{*} is chosen such that, if the pursuer is a particular position a a (in this case at the midpoint of a side) and the escaper is at point s a s_{a} at distance ( 9 − 41) / 4 ≈ 0.6492 (9-\sqrt{41})/4\approx 0.6492 along the perpendicular bisector at a a, then the escaper has four simultaneous threats to exit at p p, p ′ p^{\prime}, q q, and q ′ q^{\prime}; see Figure 12. Specifically, the escaper distance from s a s_{a} to p p is exactly factor r ∗ r^{*} smaller than the pursuer distance counterclockwise from a a to b b to c c to p p, i.e., r ∗ ​ ‖ s a − p ‖ = 2 + ‖ c − p ‖ r^{*}\|s_{a}-p\|=2+\|c-p\|; and the escaper distance from s a s_{a} to q q is exactly a factor r ∗ r^{*} smaller than the pursuer distance from a a to b b to c c to q q, i.e., r ∗ ​ ‖ s a − q ‖ = 3 − ‖ d − q ‖ r^{*}\|s_{a}-q\|=3-\|d-q\|; and similarly for p ′ p^{\prime} and q ′ q^{\prime} in the clockwise direction.

Figure 12: Geometry for computing the critical speed ratio r ∗ = 1 / sin ⁡ θ ∗ r^{*}=1/\sin\theta^{*} for a square.

###### Proof.

We first provide a winning pursuer strategy when r ≥ r ∗ r\geq r^{*}. Our pursuer strategy transitions between eight different strategies as the escaper move within the triangle. These six strategies z ⁡ ( h, i, j) z(h;i,j) are shown in Figure 13, where each strategy is associated with a corner i ∈ { a, b, c, d } i\in\{a,b,c,d\} and a sign j ∈ { − 1, 1 } j\in\{-1,1\}. Each of these strategies is identical up to rotations and reflections, so let us first focus on one of the strategies, z ⁡ ( h, a, 1) z(h;a,1).

Figure 13: Transitions between pursuer strategies.

The strategy z ⁡ ( h, a, 1) z(h;a,1), depicted in Figure 14, maps each point of the colored subset of the square to a point on the boundary via a piecewise-linear map. Wherever the escaper is in the colored region of a strategy, the strategy will place the pursuer at the boundary point designated by the map. To make it easier to reference points on the boundary, we map each boundary point on edges p a ​ b ​ p b ​ c p_{ab}p_{bc}, p c ​ d ​ p d ​ a p_{cd}p_{da}, and p d ​ a ​ p a ​ b p_{da}p_{ab} to a number, varying linearly from − 1.5 -1.5 at vertex p b ​ c p_{bc} (orange), to − 1 -1 at vertex b b (yellow), to − 0.5 -0.5 at vertex p a ​ b p_{ab} (green), to 0 0 at vertex b b (cyan), to 0.5 0.5 at vertex p d ​ a p_{da} (blue), to 1 1 at vertex c c (purple), to 1.5 1.5 at vertex p c ​ d p_{cd} (magenta). The left drawing of Figure 14 depicts the geometry of the linear patches of this map:

Figure 14: Geometry of z ⁡ ( h, a, 1) z(h;a,1). This function is linear in each region a ​ b ′ ​ p a ​ b ab^{\prime}p_{ab}, a ​ q ′ ​ b ′′ ​ b ′ aq^{\prime}b^{\prime\prime}b^{\prime}, p a ​ b ​ p b ​ c ​ b ′′′ ​ b ′ p_{ab}p_{bc}b^{\prime\prime\prime}b^{\prime}, b ′ ​ b ′′′ ​ s d ​ b ′′ b^{\prime}b^{\prime\prime\prime}s_{d}b^{\prime\prime}, p b ​ c ​ s a ​ b ′′′ p_{bc}s_{a}b^{\prime\prime\prime}, b ′′′ ​ s a ​ q ​ s d b^{\prime\prime\prime}s_{a}qs_{d}, q ′ ​ b ′′ ​ s d ​ q ​ s b ​ d ′′ q^{\prime}b^{\prime\prime}s_{d}qs_{b}d^{\prime\prime}, a ​ q ′ ​ d ′′ ​ p d ​ a aq^{\prime}d^{\prime\prime}p_{da}, d ′′ ​ s b ​ p c ​ d ​ p d ​ a d^{\prime\prime}s_{b}p_{cd}p_{da}, and q ​ s a ​ p c ​ d ​ s b qs_{a}p_{cd}s_{b}, where points { a, b ′, b ′′′, s a } \{a,b^{\prime},b^{\prime\prime\prime},s_{a}\} have value 0 0 (cyan), points { b, b ′′, s d, q, q ′, s b, d ′′ } \{b,b^{\prime\prime},s_{d},q,q^{\prime},s_{b},d^{\prime\prime}\} have value − 1 -1 (yellow), and points p a ​ b p_{ab}, p b ​ c p_{bc}, p c ​ d p_{cd}, d d, p d ​ a p_{da} have values − 0.5 -0.5 (green), − 1.5 -1.5 (orange), 1.5 1.5 (magenta), 1 1 (purple), and 0.5 0.5 (blue) respectively.

- •

point s i s_{i} for i ∈ { a, b, c, d } i\in\{a,b,c,d\} is distance ( 9 − 41) / 4 ≈ 0.06492 (9-\sqrt{41})/4\approx 0.06492 from midpoint i i toward the center;

- •

point b ′′′ b^{\prime\prime\prime} is the point on segment p b ​ c ​ s d p_{bc}s_{d} where 5 ​ ‖ b ′′′ − s d ‖ = 2 ​ ‖ s d − p b ​ c ‖ 5\|b^{\prime\prime\prime}-s_{d}\|=2\|s_{d}-p_{bc}\|;

- •

point q q is the intersection of the segment a ​ s a as_{a} and the line through s d s_{d} parallel to segment b ′′′ ​ s a b^{\prime\prime\prime}s_{a}.

- •

point q ′ q^{\prime} is on segment a ​ s a as_{a} such that ‖ a − q ′ ‖ = ‖ q − s a ‖ \|a-q^{\prime}\|=\|q-s_{a}\|;

- •

point b ′′ b^{\prime\prime} is the intersection of two lines: the line through t t parallel to segment b ′′′ ​ s a b^{\prime\prime\prime}s_{a} and the line through s d s_{d} perpendicular to segment b ′′′ ​ s a b^{\prime\prime\prime}s_{a};

- •

point d ′′ d^{\prime\prime} is the reflection of b ′′ b^{\prime\prime} about a ​ s a as_{a}; and

- •

point b ′ b^{\prime} is the point on segment p a ​ b ​ b ′′ p_{ab}b^{\prime\prime} where 3 ​ ‖ p a ​ b − b ′ ‖ = ‖ p a ​ b − b ′′ ‖ 3\|p_{ab}-b^{\prime}\|=\|p_{ab}-b^{\prime\prime}\|.

We specify each linear patch by specifying the value at each vertex:

- •

points { a, b ′, b ′′′, s a } \{a,b^{\prime},b^{\prime\prime\prime},s_{a}\} have value 0 0 (cyan),

- •

points { b, q, q ′, b ′′, d ′′, s d, s d } \{b,q,q^{\prime},b^{\prime\prime},d^{\prime\prime},s_{d},s_{d}\} have value − 1 -1 (yellow),

- •

point d d has value 1 1 (purple), and

- •

points p a ​ b p_{ab}, p b ​ c p_{bc}, p c ​ d p_{cd}, and p d ​ a p_{da} have values − 0.5 -0.5, − 1.5 -1.5, 1.5 1.5, and 0.5 0.5 respectively.

This map has the property that the gradient at every point within each linear patch has the same value, namely r ∗ r^{*}. Thus, as the escaper moves within the colored region, the pursuer’s speed will always stay below r ∗ ≤ r r^{*}\leq r, so the strategy will be valid. This map also has the property that the pursuer and the escaper will be collocated whenever the escaper is on edges p a ​ b ​ p b ​ c p_{ab}p_{bc}, p c ​ d ​ p d ​ a p_{cd}p_{da}, or p d ​ a ​ p a ​ b p_{da}p_{ab}, so the escaper cannot win along those edges. If the escaper reaches edge p b ​ c ​ s a p_{bc}s_{a} or edge p c ​ d ​ s a p_{cd}s_{a}, the pursuer will switch strategies, respectively to either z ⁡ ( h, b, − 1) z(h;b,-1) or z ⁡ ( h, d, 1) z(h;d,1). These strategies exactly match strategy z ⁡ ( h, a, 1) z(h;a,1) along their respective transition edges. By transitioning between these strategies via the transition graph shown in Figure 13, the pursuer will always be collocated with the escaper whenever the escaper is at the boundary, as desired.

Next, we provide a winning escaper strategy when r = r ∗ − ε r=r^{*}-\varepsilon for any positive ε \varepsilon; refer to Figure 15. Our escaper strategy follows a similar strategy as the triangle escaper strategy: reach a state where the escaper can win via a single APLO strategy. In particular, when the escaper is on the boundary of square S = s a ​ s b ​ s c ​ s d S=s_{a}s_{b}s_{c}s_{d}, e.g., at some point p h p_{h} on s b ​ s c s_{b}s_{c}, and the pursuer is antipodal, e.g., at point p z p_{z} on the boundary between c ​ d cd where d z ​ ( c, p z) / d z ​ ( d, p z) = ‖ s c − p h ‖ / ‖ s d − p h ‖ d_{z}(c,p_{z})/d_{z}(d,p_{z})=\|s_{c}-p_{h}\|/\|s_{d}-p_{h}\| (recall, d z ​ ( u, v) d_{z}(u,v) corresponds to the distance between u u and v v in the pursuer metric), then the escaper will be able to win via an APLO strategy to the boundary. We will reach such a configuration in two phases.

Figure 15: Geometry of the escaper strategy for a square.

In the first phase, the escaper starts anywhere on S ′ = t a ​ b ​ t b ​ c ​ t c ​ d ​ t d ​ a S^{\prime}=t_{ab}t_{bc}t_{cd}t_{da}, the square formed by connecting the midpoints of square S S. The perimeter of S ′ S^{\prime} has length 7 − 41 ≈ 0.5969 7-\sqrt{41}\approx 0.5969 which is less than 4 / r ∗ ≈ 0.6910 4/r^{*}\approx 0.6910, so the escaper can run around S ′ S^{\prime} faster than the pursuer can run around the boundary. The escaper runs around S ′ S^{\prime} until the escaper reaches a position p h ​ 1 p_{h1} on S ′ S^{\prime} such that the pursuer’s position p z ​ 1 p_{z1} is antipodal. Without loss of generality, assume p h ​ 1 p_{h1} is on edge t c ​ d ​ t b ​ c t_{cd}t_{bc} and p z ​ 1 p_{z1} is on edge p b ​ c ​ p c ​ d p_{bc}p_{cd} such that ‖ p b ​ c − p z ​ 1 ‖ = ‖ t b ​ c − p h ​ 1 ‖ / ‖ t b ​ c − t c ​ d ‖ \|p_{bc}-p_{z1}\|=\|t_{bc}-p_{h1}\|/\|t_{bc}-t_{cd}\|.

Now that the escaper is antipodal to the pursuer on S ′ S^{\prime}, the escaper enters the second phase, executing an APLO strategy H A ​ P ​ L ​ O ​ ( z, t, p h ​ 1, a ^, r, d u, d v) H_{APLO}(z,t;p_{h1},\hat{a},r,d_{u},d_{v}) where a ^ \hat{a} is the unit direction from c c to a a, d v = ‖ t b ​ c − t c ​ d ‖ ​ r < 1 d_{v}=\|t_{bc}-t_{cd}\|r<1, and d u = 1 − d v 2 < 1 d_{u}=\sqrt{1-d_{v}^{2}}<1, until the escaper reaches square S S at some point p h ​ 2 p_{h2} (without loss of generality, assume p h ​ 2 p_{h2} is on edge t b ​ c ​ s c t_{bc}s_{c}). By definition of APLO, during this process the escaper’s projection onto edge t b ​ c ​ t c ​ d t_{bc}t_{cd} remains antipodal to the pursuer, so when the escaper reaches p h ​ 2 p_{h2}, the pursuer is at the point p z ​ 2 p_{z2} on edge c ​ p c ​ d cp_{cd} that is also antipodal to p h ​ 2 p_{h2} on S S. Without loss of generality, assume p h ​ 2 p_{h2} is on segment t b ​ c ​ s c t_{bc}s_{c} and p z ​ 2 p_{z2} is antipodal on segment c ​ p b ​ c cp_{bc} such that ‖ p b ​ c − p z ​ 1 ‖ / 1 = ‖ t b ​ c − p h ​ 2 ‖ / ‖ s b − s c ‖ \|p_{bc}-p_{z1}\|/1=\|t_{bc}-p_{h2}\|/\|s_{b}-s_{c}\|. Let x z ​ 2 = ‖ t b ​ c − p z ​ 1 ‖ x_{z2}=\|t_{bc}-p_{z1}\|, let d s = ‖ s b − s c ‖ = 2 ​ ( 7 − 41) / 4 d_{s}=\|s_{b}-s_{c}\|=\sqrt{2}(7-\sqrt{41})/4, and let x h ​ 2 = ‖ t b ​ c − p h ​ 2 ‖ = x z ​ 2 ​ d s x_{h2}=\|t_{bc}-p_{h2}\|=x_{z2}d_{s}.

Now that the escaper is antipodal to the pursuer on S S, the escaper enters the third and final phase, executing an APLO strategy H A ​ P ​ L ​ O ​ ( z, t, p h ​ 2, u ^, r ∗, d u, d v) H_{APLO}(z,t;p_{h2},\hat{u},r^{*},d_{u},d_{v}), where u ^ \hat{u} is the unit direction from p b ​ c p_{bc} to p d ​ a p_{da}, d u = cos ⁡ ( π / 4 + θ ∗) d_{u}=\cos(\pi/4+\theta^{*}), and d v = sin ⁡ ( π / 4 + θ ∗) d_{v}=\sin(\pi/4+\theta^{*}), until the escaper reaches the boundary at some point p h ​ 3 p_{h3}.

If the pursuer remains in the halfplane H H bounded by p a ​ b ​ p c ​ d p_{ab}p_{cd} containing p b ​ c p_{bc}, the escaper wins easily as p h ​ 3 p_{h3} is in the other halfplane. Otherwise, there are two cases: the pursuer leaves H H last through either p a ​ b p_{ab} or p c ​ d p_{cd}. It suffices to show that the separation of their projections onto segment p a ​ b ​ p c ​ d p_{ab}p_{cd} is bounded away from zero, specifically quantity | ( p h ​ 3 − t b ​ c) ⋅ v ^ − ( p z ​ 3 − t b ​ c) ⋅ v ^ | |(p_{h3}-t_{bc})\cdot\hat{v}-(p_{z3}-t_{bc})\cdot\hat{v}| where v ^ \hat{v} is the unit vector ( p c ​ d − p a ​ b) (p_{cd}-p_{ab}). Let x h ​ 3 = ( p h ​ 3 − t b ​ c) ⋅ v ^ x_{h3}=(p_{h3}-t_{bc})\cdot\hat{v}. Note that x h ​ 3 x_{h3} is positive to the upper-left of t b ​ c t_{bc}.

1. 1.

(Pursuer leaves H H through p c ​ d p_{cd}): pursuer leaves counter-clockwise from p z ​ 2 p_{z2}, so ( p h ​ 3 − p h ​ 2) ⋅ v ^ = x h ​ 3 − x h ​ 2 ≥ 0 (p_{h3}-p_{h2})\cdot\hat{v}=x_{h3}-x_{h2}\geq 0. Then by APLO, the pursuer travels counter-clockwise from p z ​ 2 p_{z2} by distance r ⁡ ( x h ​ 3 − x h ​ 2) / sin ⁡ ( π / 4 + θ ∗) r(x_{h3}-x_{h2})/\sin(\pi/4+\theta^{*}), for distance 1 − x z ​ 2 1-x_{z2} along edge p b ​ c ​ p c ​ d p_{bc}p_{cd}, and the remainder along edges p c ​ d ​ p d ​ a p_{cd}p_{da} and p a ​ b ​ p d ​ a p_{ab}p_{da}. The largest value of x h ​ 3 x_{h3} possible via this APLO strategy varies linearly with x z ​ 2 x_{z2}. When x z ​ 2 = 1 / 2 x_{z2}=1/2, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded above by

 | ( ‖ s c − a ‖) ​ cos ⁡ ( π / 4 − θ ∗) cos ⁡ ( θ ∗) = 2 ​ ( 13 − 41) 32 (\|s_{c}-a\|)\frac{\cos(\pi/4-\theta^{*})}{\cos(\theta^{*})}=\frac{\sqrt{2}(13-\sqrt{41})}{32} |  |

and when x z ​ 2 = 0 x_{z2}=0, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded above by

 | ( ‖ s c − a ‖ + 1 2 ​ ‖ s c − t b ​ c ‖) ​ cos ⁡ ( π / 4 − θ ∗) cos ⁡ ( θ ∗) = 2 4 \left(\|s_{c}-a\|+\frac{1}{\sqrt{2}}\|s_{c}-t_{bc}\|\right)\frac{\cos(\pi/4-\theta^{*})}{\cos(\theta^{*})}=\frac{\sqrt{2}}{4} |  |

so x h ​ 3 ≤ 2 16 ​ ( 4 + x z ​ 2 ​ ( 33 − 5 ​ 41)) x_{h3}\leq\frac{\sqrt{2}}{16}\left(4+x_{z2}\left(33-5\sqrt{41}\right)\right). Using this relation and the fact that x h ​ 2 = x z ​ 2 ​ d s x_{h2}=x_{z2}d_{s}, yields

 | ( p h ​ 3 − t b ​ c) ⋅ v ^ − ( p z ​ 3 − t b ​ c) ⋅ v ^ = x h ​ 3 − 2 2 ​ ( ( x h ​ 3 − x h ​ 2) ​ r sin ⁡ ( π / 4 + θ ∗) − ( 1 − x z ​ 2) − 1) ≥ 5 ​ 2 16 ​ ( 1 − r r ∗) ​ ( 4 − x z ​ 2 ​ ( 41 − 5)) \displaystyle\begin{aligned} (p_{h3}-t_{bc})\cdot\hat{v}-(p_{z3}-t_{bc})\cdot\hat{v}&=x_{h3}-\frac{\sqrt{2}}{2}\left(\frac{(x_{h3}-x_{h2})r}{\sin(\pi/4+\theta^{*})}-\left(1-x_{z2}\right)-1\right)\\ &\geq\frac{5\sqrt{2}}{16}\left(1-\frac{r}{r^{*}}\right)(4-x_{z2}(\sqrt{41}-5))\end{aligned} |  | (3) |

which is always strictly positive for r = r ∗ − ε < r ∗ r=r^{*}-\varepsilon<r^{*} and 0 ≤ x z ​ 2 ≤ 1 2 0\leq x_{z2}\leq\frac{1}{2}, as desired.

2. 2.

(Pursuer leaves H H through p a ​ b p_{ab}): pursuer leaves clockwise from p z ​ 2 p_{z2}, so ( p h ​ 3 − p h ​ 2) ⋅ v ^ = x h ​ 3 − x h ​ 2 ≤ 0 (p_{h3}-p_{h2})\cdot\hat{v}=x_{h3}-x_{h2}\leq 0. Then by APLO, the pursuer travels clockwise from p z ​ 2 p_{z2} by distance r ⁡ ( x h ​ 2 − x h ​ 3) / sin ⁡ ( π / 4 + θ ∗) r(x_{h2}-x_{h3})/\sin(\pi/4+\theta^{*}), for distance 1 + x z ​ 2 1+x_{z2} along edges p b ​ c ​ p c ​ d p_{bc}p_{cd} and p a ​ b ​ p b ​ c p_{ab}p_{bc}, and the remainder along edges p a ​ b ​ p d ​ a p_{ab}p_{da} and p d ​ a ​ p c ​ d p_{da}p_{cd}. The smallest value of x h ​ 3 x_{h3} possible via this APLO strategy varies linearly with x z ​ 2 x_{z2}. When x z ​ 2 = 0 x_{z2}=0, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded below by

 | − ( ‖ s c − a ‖ + 1 2 ​ ‖ s c − t b ​ c ‖) ​ cos ⁡ ( π / 4 − θ ∗) cos ⁡ ( θ ∗) = − 2 4 -\left(\|s_{c}-a\|+\frac{1}{\sqrt{2}}\|s_{c}-t_{bc}\|\right)\frac{\cos(\pi/4-\theta^{*})}{\cos(\theta^{*})}=-\frac{\sqrt{2}}{4} |  |

and when x z ​ 2 = 1 / 2 x_{z2}=1/2, then ( x h ​ 3 − x h ​ 2) (x_{h3}-x_{h2}) is bounded below by

 | − ( ‖ s c − a ‖ + 2 2 ​ ‖ s c − t b ​ c ‖) ​ cos ⁡ ( π / 4 − θ ∗) cos ⁡ ( θ ∗) = − 2 ​ ( 3 + 41) 32 -\left(\|s_{c}-a\|+\frac{2}{\sqrt{2}}\|s_{c}-t_{bc}\|\right)\frac{\cos(\pi/4-\theta^{*})}{\cos(\theta^{*})}=-\frac{\sqrt{2}(3+\sqrt{41})}{32} |  |

so x h ​ 3 ≤ − 2 16 ​ ( 4 − x z ​ 2 ​ ( 33 − 5 ​ 41)) x_{h3}\leq-\frac{\sqrt{2}}{16}\left(4-x_{z2}\left(33-5\sqrt{41}\right)\right). Using this relation and the fact that x h ​ 2 = x z ​ 2 ​ d s x_{h2}=x_{z2}d_{s}, yields

 | ( p h ​ 3 − t b ​ c) ⋅ v ^ − ( p z ​ 3 − t b ​ c) ⋅ v ^ = x h ​ 3 − 2 2 ​ ( − ( x h ​ 2 − x h ​ 3) ​ r sin ⁡ ( π / 4 + θ ∗) + ( 1 + x z ​ 2) + 1) ≤ − 5 ​ 2 16 ​ ( 1 − r r ∗) ​ ( 4 − x z ​ 2 ​ ( 41 − 5)) \displaystyle\begin{aligned} (p_{h3}-t_{bc})\cdot\hat{v}-(p_{z3}-t_{bc})\cdot\hat{v}&=x_{h3}-\frac{\sqrt{2}}{2}\left(-\frac{(x_{h2}-x_{h3})r}{\sin(\pi/4+\theta^{*})}+\left(1+x_{z2}\right)+1\right)\\ &\leq-\frac{5\sqrt{2}}{16}\left(1-\frac{r}{r^{*}}\right)(4-x_{z2}(\sqrt{41}-5))\end{aligned} |  | (4) |

which is always strictly negative for r = r ∗ − ε < r ∗ r=r^{*}-\varepsilon<r^{*} and 0 ≤ x z ​ 2 ≤ 1 2 0\leq x_{z2}\leq\frac{1}{2}, as desired. ∎

## 5 Full Model (Full Version of Section 2)

In this section, we define our model (as in Section 2), as well as detail the motivation for the particular definitions and the differences from past work, in Section 5.1. Then we prove that at most one player can win in Section 5.2, and prove that at least one player can win in Section 5.4. Along the way, we introduce two important tools for analyzing these games: δ \delta -oblivious strategies (Section 5.2) and the ( δ, γ) (\delta,\gamma) -discretized game (Section 5.3). The latter will be useful in particular for our pseudopolynomial-time approximation scheme in Section 6.

### 5.1 Continuous Game

To define the pursuit–escape game G G, we need several ingredients: what type of domains (regions) the escaper and pursuer traverse, what type of motions are allowed within these domains, what strategies are and how they can adapt to the other player’s actions, and when exactly a player wins the game. We address each of these concepts in turn. The core definitions (the overlap with Section 2) are highlighted in yellow.

#### Domains.

First we define the notion of “player domain”, which is a play area that either the escaper or pursuer is restricted to move within. We choose to somewhat restrict the sets on which we analyze pursuer evasion games, to avoid cases where escaper or pursuer running distances (shortest-path metrics) are undefined or behave pathologically. Even so, we give a very general definition, both to show our framework applies very generally and so that it includes the many special cases of interest, including a disk (with smooth boundaries), a halfplane (with unbounded area), and the graph model (with one-dimensional features), in addition to our primary case of a polygon with the exterior or moat model. (Previous work on the Lion and Man game did not deal with the issue of defining allowable domains, focusing on specific cases, although the importance of rectifiability is mentioned in the context of two-lion games in [Bol06, p. 46] and [AHRWN17].)

Specifically, a player domain is a closed subset D D of Euclidean space ℝ k \mathbb{R}^{k} that is locally finitely rectifiable, meaning that its intersection D ∩ B D\cap B with any bounded closed Euclidean ball B B is “finitely rectifiable” (which intuitively means “finite total surface area”). Formally, R ⊆ ℝ k R\subseteq\mathbb{R}^{k} is finitely rectifiable if it is the union of the images of finitely many functions of the form S: [0, 1] k → R S:[0,1]^{k}\to R satisfying the Lipschitz condition d ⁡ ( S ⁡ ( u), S ⁡ ( v)) ≤ d ⁡ ( u, v) d(S(u),S(v))\leq d(u,v) for all u, v ∈ [0, 1] k u,v\in[0,1]^{k}. 7 7 7 Throughout this paper, we use Euclidean as the default metric unless otherwise specified, so d ⁡ ( u, v) d(u,v) denotes the Euclidean distance ‖ u − v ‖ 2 \|u-v\|_{2}. We use a subscript (such as d h d_{h} and d z d_{z} introduced soon) to denote a different metric. We call the functions S S constituting R R the patches of R R.

This definition forbids player domains with fractal boundary of nontrivial fractal dimension, and forbids the “Harmonic comb” — the union of line segments from the origin to ( 1 / i, 1) (1/i,1) for all i > 0 i>0, together with the segment from the origin to ( 0, 1) (0,1). 8 8 8 The Harmonic comb would have been allowed if we required the weaker property that D D is the union of the images of countably many Lipschitz functions (the countable analog of “finitely rectifiable”). Notably, this compact set has an infinite sequence of points ( 1 / i, 1) (1/i,1) that converge in the Euclidean metric but not when measured according to shortest paths within D D (contrary to Lemma A.1), so we choose to forbid it from being a valid domain. But the definition still allows a boundary of infinite total length/surface area so long as the infinity comes from being unbounded in ℝ k \mathbb{R}^{k}. For example, the following are valid domains:

- •

Polygons (interior plus boundary), possibly with holes, of finite total perimeter (but having possibly infinitely many edges).

- •

Unbounded polygons, where finitely many edges extend to infinite rays, while the finite-length edges have bounded total length. For example, 2D linear programs define convex unbounded polygons, including half-planes and wedges (which are studied in Section 4).

- •

The exterior (including the boundary) of one or more polygons, each of finite perimeter.

- •

Generalizations of the above to higher dimensions (polyhedra).

- •

Any closed semi-algebraic set, or more generally, closed semi-analytic or closed subanalytic set [BM88, Theorem 6.10].

- •

Any embedding (not necessarily straight-line) of a graph into ℝ k \mathbb{R}^{k} of finite total edge length. In particular, any graph can be embedded into ℝ 3 \mathbb{R}^{3}, even while matching specified edge lengths, so this lets us represent the pursuit–escape game on weighted graphs (the graph model). In this case, the entire domain is its own boundary.

The input to the pursuit–escape problem consists of an escaper domain D h D_{h} and a pursuer domain D z D_{z}, and an exit set X X. The escaper and pursuer domains must be *player domains*as described above. The exit set X X must also be a player domain, and a subset of the player domains: X ⊆ D h ∩ D z X\subseteq D_{h}\cap D_{z}. The goal of the escaper will be to reach an exit — any point of the exit set X X — while being sufficiently away from the pursuer. Typically, we imagine the entire escaper–pursuer domain intersection as the exit set ( X = D h ∩ D z X=D_{h}\cap D_{z}), but we allow the more general form to represent e.g. that the escaper must reach an escape vehicle which are only at certain points where the escaper and pursuer could meet.

Two natural cases captured by this framework are as follows:

- •

Exterior model: when D z = ℝ k − D h ¯ D_{z}=\overline{\mathbb{R}^{k}-D_{h}} (the closure of the complement of D h D_{h}), i.e., the pursuer can be anywhere the escaper cannot, plus the shared boundary ∂ D z = ∂ D h \partial D_{z}=\partial D_{h}. 9 9 9 Here ∂ D = D ∖ int ⁡ D \partial D=D\setminus\interior D is the boundary of D D, where int ⁡ D \interior D is the interior of D D, i.e., the set of all points of D D having an open neighborhood within D D.

- •

Moat model: when D z = ∂ D h D_{z}=\partial D_{h}, i.e., the pursuer can only walk around the boundary of the escaper domain.

For any domain D D, let d D d_{D} denote the intrinsic (shortest-path) metric of D D. This metric measures how someone restricted to the domain would travel. In particular, define the escaper metric d h = d D h d_{h}=d_{D_{h}} and pursuer metric d z = d D z d_{z}=d_{D_{z}}.

#### Motion paths.

A motion path with maximum speed s ≥ 0 s\geq 0 in metric domain D D is a function a: [0, ∞) → D a:[0,\infty)\to D satisfying the speed-limit constraint (Lipschitz condition)

 | d D ​ ( a ⁡ ( t 1), a ⁡ ( t 2)) ≤ s ⋅ | t 1 − t 2 | ​ for all ​ t 1, t 2 ≥ 0. \displaystyle d_{D}(a(t_{1}),a(t_{2}))\leq s\cdot|t_{1}-t_{2}|\text{ for all }t_{1},t_{2}\geq 0. |  |

(This definition matches the definitions of “lion path” and “man path” in [BLW12], generalized to arbitrary maximum speed and arbitrary domain.) The speed constraint implies that all motion paths are continuous. This definition can also represent finite motion paths by letting a ⁡ ( t) a(t) be constant for t ≥ T t\geq T for some T T.

We consider a model where the pursuer maximum speed is a factor of r r larger than the escaper maximum speed, which we assume is 1 1 for simplicity. Thus an escaper motion path is a motion path of maximum speed 1 1 in the escaper domain D h D_{h}, while a pursuer motion path is a motion path of maximum speed r r in the pursuer domain D z D_{z}.

#### Symmetric terminology for player vs. opponent.

For symmetry, the following definitions refer to a player (either escaper and pursuer) and their opponent (pursuer or escaper, respectively). For example, we use “player motion path” a a and “opponent motion path” b b to refer to two cases symmetrically: (1) an escaper motion path a a and a pursuer motion path b b; and (2) a pursuer motion path a a and an escaper motion path b b.

#### Strategies.

A player strategy is a function A A mapping an opponent motion path b b to a player motion path A ⁡ ( b) A(b) satisfying the following nonbranching-lookahead constraint:

for any two opponent motion paths b 1, b 2 b_{1},b_{2} agreeing on [0, t] [0,t], the strategy’s player motion paths A ⁡ ( b 1), A ⁡ ( b 2) A(b_{1}),A(b_{2}) also agree on [0, t] [0,t].

Effectively, this definition constrains A ​ ( b) ​ ( t) A(b)(t) to depend only on b ⁡ ( t ′) b(t^{\prime}) for earlier times t ′ ≤ t t^{\prime}\leq t, or equivalently by continuity of motion plans, for strictly earlier times t ′ < t t^{\prime}<t.

This definition matches the clever definition of “lion/man strategy” and “no lookahead” in [BLW12]. We use the term “nonbranching-lookahead” to more accurately reflect that the strategy can depend on the opponent motion path, including the future, so long as it does so in a nonbranching way. This is useful for defining strategies such as “move along a straight line to where the opponent will go”, but it can allow for certain kinds of “cheating”; see Lemma 5.1 below.

This definition correctly defines a pursuer strategy Z Z. An escaper strategy H H must satisfy one additional constraint, the escaper-start constraint:

all paths H ⁡ ( z) H(z) (over all pursuer motion paths z z) must start at a common point H ​ ( z) ​ ( 0) H(z)(0).

This constraint is necessary in our case because, if the escaper can choose their starting position depending on the pursuer’s start position, then the escaper can trivially win (by starting at a far-away exit). (In the man-and-lion problem, the man and lion’s starting positions are given, so [BLW12] did not have to deal with this asymmetry.)

Notationally, we use lower-case letters a, h, z a,h,z for motion paths and upper-case letters A, H, Z A,H,Z for strategies of the player, escaper, and pursuer, respectively.

#### Win condition.

It remains to define a win condition for the pursuit–escape game G G. We do so in terms of an infinity family of games G ε G_{\varepsilon} for all ε > 0 \varepsilon>0.

An escaper strategy H H wins 𝑮 𝜺 G_{\varepsilon} or wins 𝑮 G by 𝜺 \varepsilon if, for every pursuer motion path z z, there is a time t t at which H ​ ( z) ​ ( t) H(z)(t) is on an exit and at distance ≥ ε \geq\varepsilon from z ⁡ ( t) z(t) in the pursuer metric. Intuitively, the escaper needs a small amount of time to exit (e.g., to break into the getaway car), during which the pursuer can run ε \varepsilon distance and catch the escaper.

This no-capture definition allows the escaper and pursuer to collocate at time < t <t without the escaper being captured; in other words, the escaper has the ability to choose to exit, and only then must be away from the pursuer. As mentioned in Section 1, our no-capture model differs from the Lion and Man problem, where collocation implies immediate capture. Indeed, our no-capture model is a significant deviation because, if we used the Lion-and-Man notion of “escaper win” [BLW12], then the escaper would always win in many natural instances (e.g., polygon, Jordan, and polyhedron models):

###### Lemma 5.1.

Assuming the exit set X X contains a one-dimensional curve, there is an escaper strategy H H such that, for any pursuer motion path z z, H ⁡ ( z) H(z) wins G ε ⁡ ( z) G_{\varepsilon(z)} for some function ε ⁡ ( z) \varepsilon(z).

###### Proof.

Parameterize the curve as C ⁡ ( t) C(t) for 0 ≤ t ≤ T 0\leq t\leq T with unit speed in the escaper metric d h d_{h}. The escaper starts at C ⁡ ( 0) C(0), i.e., H ​ ( z) ​ ( 0) = C ​ ( 0) H(z)(0)=C(0). Thus H H satisfies the escaper-start constraint.

If z ⁡ ( 0) ≠ C ⁡ ( 0) z(0)\neq C(0), then the escaper wins immediately by d z ​ ( C ⁡ ( 0), z ⁡ ( 0)) > 0 d_{z}(C(0),z(0))>0. So assume z ⁡ ( 0) = C ⁡ ( 0) z(0)=C(0). (The escaper can still continue from this position because of the no-capture aspect of our model.) Either the pursuer stays at C ⁡ ( 0) C(0) for positive time, or they move away. We define the rest of the escaper strategy according to these two cases:

 | H ⁡ ( z) ​ ( t) = { C ⁡ ( t) if ​ z ​ ( t ′) = C ⁡ ( 0) ​ for all ​ t ′ ∈ [0, T ′] ​ for some ​ T ′ > 0, C ⁡ ( 0) if ​ z ​ ( t ′) ≠ C ⁡ ( 0) ​ for some ​ t ′ ∈ [0, 1]. H(z)(t)=\begin{cases}C(t)&\text{if }z(t^{\prime})=C(0)\text{ for all }t^{\prime}\in[0,T^{\prime}]\text{ for some }T^{\prime}>0,\\ C(0)&\text{if }z(t^{\prime})\neq C(0)\text{ for some }t^{\prime}\in[0,1].\end{cases} |  |

By the unit-speed parameterization of C C, H ⁡ ( z) H(z) is a valid escaper motion path. In the first case, the escaper wins by d z ​ ( C ⁡ ( 0), C ⁡ ( T ′)) > 0 d_{z}(C(0),C(T^{\prime}))>0. In the second case, the escaper wins by d z ​ ( C ⁡ ( 0), z ⁡ ( t ′)) > 0 d_{z}(C(0),z(t^{\prime}))>0.

Finally, we prove that H H satisfies the nonbranching-lookahead constraint. Consider two pursuer motion paths z 1, z 2 z_{1},z_{2} that agree on [0, t] [0,t] for some t ≥ 0 t\geq 0. If t = 0 t=0, then H ⁡ ( z 1) H(z_{1}) and H ⁡ ( z 2) H(z_{2}) also agree on [0, t] [0,t] (by the escaper-start constraint). If t > 0 t>0 and z i ​ ( t ′) = C ⁡ ( 0) z_{i}(t^{\prime})=C(0) for all t ′ ∈ [0, T ′] t^{\prime}\in[0,T^{\prime}] for some T ′ > 0 T^{\prime}>0, then z 3 − i ​ ( t ′) = C ⁡ ( 0) z_{3-i}(t^{\prime})=C(0) for all t ′ ∈ [0, min ⁡ { t, T ′ }] t^{\prime}\in[0,\min\{t,T^{\prime}\}]. Thus, if t > 0 t>0, then z 1 z_{1} and z 2 z_{2} are in the same case among the two cases, so H ⁡ ( z 1) H(z_{1}) and H ⁡ ( z 2) H(z_{2}) also agree on [0, t] [0,t]. ∎

To avoid this problem, we use the following notion of an escaper win for a pursuit–escape game G G. The escaper wins 𝑮 G if, for some ε > 0 \varepsilon>0, there is an escaper strategy that wins G G by ε \varepsilon, i.e., wins G ε G_{\varepsilon}. Notably, unlike Lemma 5.1, this condition requires a *uniform*ε \varepsilon for all pursuer motion paths. Equivalently, we are taking a uniform limit of winning strategies in the games G ε G_{\varepsilon} as ε → 0 \varepsilon\to 0. This is a key difference from the definitions for Lion and Man in [BLW12]; as we will show, it implies the existence of “oblivious” strategies, which are a stronger form of “locally finite” strategies from [BLW09], and perhaps a more natural notion of “no lookahead”. Note that, for the Lion-and-Man game, the locally finite property is already known to imply a unique winner [BLW09].

Next we define pursuer wins. A pursuer strategy Z Z wins 𝑮 𝜺 G_{\varepsilon} if, for every escaper motion path h h, and every time t t at which h ⁡ ( t) h(t) is on an exit, h ⁡ ( t) h(t) is at distance < ε <\varepsilon from Z ​ ( h) ​ ( t) Z(h)(t) in the pursuer metric: d z ​ ( h ⁡ ( t), Z ⁡ ( h) ​ ( t)) < ε d_{z}(h(t),Z(h)(t))<\varepsilon. Intuitively, such a pursuer strategy prevents the escaper from winning by ε \varepsilon. The pursuer wins 𝑮 G if, for all ε > 0 \varepsilon>0, there is a pursuer strategy that wins G ε G_{\varepsilon}. The latter definition allows the pursuer strategy to depend on ε \varepsilon, and our proofs will rely on this. Under the Axiom of Choice, however, it is equivalent to a simpler definition:

###### Lemma 5.2.

Assuming the Axiom of Choice, the pursuer wins G G if and only if there is a pursuer strategy that, for all ε > 0 \varepsilon>0, wins G ε G_{\varepsilon}.

To prove this lemma, we need a version of the Arzelà–Ascoli Theorem [Wik25]. This theorem is sometimes stated for bounded functions over bounded intervals and guaranteeing uniform convergence; we need a version over unbounded intervals and only local boundedness, at the cost of guaranteeing only pointwise instead of uniform convergence. Known generalizations [Kel55, p. 231], [Eng89, Theorems 3.4.20 and 8.2.10] imply this version, but for clarity and completeness, we translate the theorem and proof from topological language. Our proof is roughly a subset of the proof described in [Wik25] (skipping the finite-cover step needed for uniform convergence but which does not work for unbounded domains).

###### Lemma 5.3 (Arzelà–Ascoli Theorem).

For any metric domain D D, and for any sequence of functions f 1, f 2, …: [0, ∞) → D f_{1},f_{2},\ldots:[0,\infty)\to D that satisfies the following two properties, there is a subsequence f i 1, f i 2, … f_{i_{1}},f_{i_{2}},\dots that converges pointwise.

1. 1.

Uniformly locally bounded: there is an origin O O and a function M: [0, ∞) → [0, ∞) M:[0,\infty)\to[0,\infty) such that, for all i i and t t, we have d D ​ ( O, f i ​ ( t)) ≤ M ⁡ ( t) d_{D}(O,f_{i}(t))\leq M(t).

2. 2.

Uniformly equicontinuous: for every ε > 0 \varepsilon>0, there is a δ > 0 \delta>0 such that, for all i i, we have | s − t | ≤ δ |s-t|\leq\delta implies d D ​ ( f i ​ ( s), f i ​ ( t)) ≤ ε d_{D}(f_{i}(s),f_{i}(t))\leq\varepsilon.

###### Proof.

Fix an enumeration t 1, t 2, … t_{1},t_{2},\dots of the nonnegative rational numbers. Start by applying every function to t 1 t_{1}, forming the sequence f 1 ​ ( t 1), f 2 ​ ( t 1), … f_{1}(t_{1}),f_{2}(t_{1}),\dots. By uniform local boundedness, this sequence is bounded, so by the Bolzano–Weierstrass Theorem, it has a convergent subsequence f i 1, 1 ​ ( t 1), f i 1, 2 ​ ( t 1), … f_{i_{1,1}}(t_{1}),f_{i_{1,2}}(t_{1}),\dots. Now change the parameter from t 1 t_{1} to t 2 t_{2}, forming the sequence f i 1, 1 ​ ( t 2), f i 1, 2 ​ ( t 2), … f_{i_{1,1}}(t_{2}),f_{i_{1,2}}(t_{2}),\dots. This sequence is also bounded, so by the Bolzano–Weierstrass Theorem, it has a convergent subsequence f i 2, 1 ​ ( t 2), f i 2, 2 ​ ( t 2), … f_{i_{2,1}}(t_{2}),f_{i_{2,2}}(t_{2}),\dots. By induction, we obtain a sequence of progressively nested subsequences { i 1, 1, i 1, 2, … } ⊇ { i 2, 1, i 2, 2, … } ⊇ ⋯ \{i_{1,1},i_{1,2},\dots\}\supseteq\{i_{2,1},i_{2,2},\dots\}\supseteq\cdots such that f i k, 1 ​ ( t k), f i k, 2 ​ ( t k), … f_{i_{k,1}}(t_{k}),f_{i_{k,2}}(t_{k}),\dots converges for each k k.

Now diagonalize to form the subsequence f i 1, 1, f i 2, 2, f i 3, 3, … f_{i_{1,1}},f_{i_{2,2}},f_{i_{3,3}},\dots of the given functions f 1, f 2, … f_{1},f_{2},\dots. We claim that this subsequence converges pointwise. For any nonnegative rational t k t_{k}, the sequence f i 1, 1 ​ ( t k), f i 2, 2 ​ ( t k), … f_{i_{1,1}}(t_{k}),f_{i_{2,2}}(t_{k}),\dots converges because the suffix f i k, k ​ ( t k), f i k + 1, k + 1 ​ ( t k), … f_{i_{k,k}}(t_{k}),f_{i_{k+1,k+1}}(t_{k}),\dots is a subsequence of the convergent sequence f i k, 1 ​ ( t k), f i k, 2 ​ ( t k), … f_{i_{k,1}}(t_{k}),f_{i_{k,2}}(t_{k}),\dots. Thus, for any k k, any ε > 0 \varepsilon>0, and any sufficiently large p, q p,q, we have d D ​ ( f i p, p ​ ( t k), f i q, q ​ ( t k)) ≤ ε / 3 d_{D}(f_{i_{p,p}}(t_{k}),\allowbreak f_{i_{q,q}}(t_{k}))\leq\varepsilon/3. By uniform equicontinuity, there is a δ = δ ⁡ ( ε) > 0 \delta=\delta(\varepsilon)>0 such that, for all i i, we have | s − t | ≤ δ |s-t|\leq\delta implies d D ​ ( f i ​ ( s), f i ​ ( t)) ≤ ε / 3 d_{D}(f_{i}(s),f_{i}(t))\leq\varepsilon/3. For any t t, we can find a rational t k t_{k} such that | t − t k | ≤ δ |t-t_{k}|\leq\delta. By the triangle inequality, for any ε > 0 \varepsilon>0 and sufficiently large p, q p,q, we have

 | d D ​ ( f i p, p ​ ( t), f i q, q ​ ( t)) \displaystyle d_{D}\big(f_{i_{p,p}}(t),f_{i_{q,q}}(t)\big) | ≤ d D ​ ( f i p, p ​ ( t), f i p, p ​ ( t k)) + d D ​ ( f i p, p ​ ( t k), f i q, q ​ ( t k)) + d D ​ ( f i q, q ​ ( t k), f i q, q ​ ( t)) \displaystyle\leq d_{D}\big(f_{i_{p,p}}(t),f_{i_{p,p}}(t_{k})\big)+d_{D}\big(f_{i_{p,p}}(t_{k}),f_{i_{q,q}}(t_{k})\big)+d_{D}\big(f_{i_{q,q}}(t_{k}),f_{i_{q,q}}(t)\big) |  |

 |  | ≤ ε / 3 + ε / 3 + ε / 3 = ε. \displaystyle\leq\varepsilon/3+\varepsilon/3+\varepsilon/3=\varepsilon. |  |

Therefore, for any t t, the sequence f i 1, 1 ​ ( t), f i 2, 2 ​ ( t), … f_{i_{1,1}}(t),f_{i_{2,2}}(t),\dots is a Cauchy sequence, so it converges, as desired. ∎

###### Proof of Lemma 5.2.

One direction is obvious: if a single pursuer strategy wins G ε G_{\varepsilon} for all ε > 0 \varepsilon>0, then we satisfy the definition of winning G G. To prove the other direction, assume the pursuer wins G G, i.e., for every ε > 0 \varepsilon>0, there is a pursuer strategy Z ε Z_{\varepsilon} that wins G ε G_{\varepsilon}. To construct a single pursuer strategy Z 0 Z_{0} that wins all G ε G_{\varepsilon}, we roughly follow the proof of [BLW12, Lemma 3] which shows how to take limits of strategies in the Lion and Man game. (Our proof differs in a few ways: we need to check a different notion of winning; our result works for infinite time and unbounded domains; as in Lemma 5.3, we use pointwise instead of uniform convergence; and our proof is more detailed.) Specifically, we use Zorn’s Lemma (which is equivalent to the Axiom of Choice): for any partially ordered set, if every chain has a maximal element, then there is a global maximum element.

We define a partially ordered set of “good partial pursuer strategies”. A partial pursuer strategy is a *partial*function Z Z from escaper motion paths to pursuer motion paths satisfying the nonbranching-lookahead constraint where it is defined, i.e., for any two escaper motion paths h 1, h 2 ∈ dom ⁡ ( Z) h_{1},h_{2}\in\operatorname{dom}(Z) agreeing on [0, t] [0,t], the pursuer motion paths Z ⁡ ( h 1), Z ⁡ ( h 2) Z(h_{1}),Z(h_{2}) also agree on [0, t] [0,t]. A partial pursuer strategy Z Z is good if, for every escaper motion path h ∈ dom ⁡ ( Z) h\in\operatorname{dom}(Z), there is an infinite sequence ε 1, ε 2, … \varepsilon_{1},\varepsilon_{2},\dots converging to 0 0 such that Z ε 1 ​ ( h), Z ε 2 ​ ( h), … Z_{\varepsilon_{1}}(h),Z_{\varepsilon_{2}}(h),\dots converges pointwise to Z ⁡ ( h) Z(h) in the pursuer metric. As we show below, Z Z being good implies that Z Z wins G ε G_{\varepsilon} for all ε > 0 \varepsilon>0, if the escaper is restricted to motion paths in dom ⁡ ( Z) \operatorname{dom}(Z). The partial order ≤ \leq is defined as follows: for two good partial pursuer strategies Z 1, Z 2 Z^{1},Z^{2}, 𝒁 1 ≤ 𝒁 2 Z^{1}\leq Z^{2} if dom ⁡ ( Z 1) ⊆ dom ⁡ ( Z 2) \operatorname{dom}(Z^{1})\subseteq\operatorname{dom}(Z^{2}) and Z 1 Z^{1} and Z 2 Z^{2} agree on their common dom ⁡ ( Z 1) \operatorname{dom}(Z^{1}).

Zorn’s Lemma applies to this partial order because any chain Z 1, Z 2, … Z^{1},Z^{2},\dots of good partial strategies has a maximal element, namely, Z 1 ∪ Z 2 ∪ ⋯ Z^{1}\cup Z^{2}\cup\cdots. Thus we obtain a maximum good partial pursuer strategy Z 0 Z_{0}. We will show that Z 0 Z_{0} is in fact a (full) pursuer strategy, and by goodness, wins G ε G_{\varepsilon} for all ε > 0 \varepsilon>0 as desired.

Suppose for contradiction that Z 0 Z_{0} is not defined on some escaper motion path h ′ h^{\prime}. We will show how to extend Z 0 Z_{0} to a good partial pursuer strategy Z 0 ′ Z_{0}^{\prime} where dom ⁡ ( Z 0 ′) = dom ⁡ ( Z 0) ∪ { h ′ } \operatorname{dom}(Z_{0}^{\prime})=\operatorname{dom}(Z_{0})\cup\{h^{\prime}\}, contradicting maximality of Z 0 Z_{0}. To ensure preservation of the nonbranching-lookahead constraint, we look for an escaper motion path h ∈ dom ⁡ ( Z 0) h\in\operatorname{dom}(Z_{0}) that agrees with h ′ h^{\prime} for the longest interval [0, t ∗] [0,t^{*}]. To this end, define

 | t ∗ = sup { t ≥ 0 ∣ there exists h ∈ dom ( Z 0) such that h, h ′ agree on [0, t] }. t^{*}=\sup\{t\geq 0\mid\text{there exists }h\in\operatorname{dom}(Z_{0})\text{ such that }h,h^{\prime}\text{ agree on }[0,t]\}. |  |

Beyond time t ∗ t^{*}, we can define Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}) arbitrarily, while preserving the nonbranching-lookahead property. There are three cases according to whether the supremum t ∗ t^{*} is realized or undefined.

Case 0: t ∗ t^{*} is undefined.

This case happens when there is no h ∈ dom ⁡ ( Z 0) h\in\operatorname{dom}(Z_{0}) for which h ​ ( 0) = h ′ ​ ( 0) h(0)=h^{\prime}(0), so no matter how we define Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}), we will satisfy nonbranching lookahead.

Define ε i = 1 / i \varepsilon_{i}=1/i, and take the sequence Z ε 1 ​ ( h ′), Z ε 2 ​ ( h ′), … Z_{\varepsilon_{1}}(h^{\prime}),Z_{\varepsilon_{2}}(h^{\prime}),\dots. Now we apply Lemma 5.3 to this sequence of functions. Our functions Z ε i ​ ( h ′) Z_{\varepsilon_{i}}(h^{\prime}) are uniformly equicontinuous because they are Lipschitz with uniform constant r r. Our functions Z ε i ​ ( h ′) Z_{\varepsilon_{i}}(h^{\prime}) are uniformly locally bounded because they are uniformly Lipschitz and start at points Z ε 1 ​ ( h ′) ​ ( 0), Z ε 2 ​ ( h ′) ​ ( 0), … Z_{\varepsilon_{1}}(h^{\prime})(0),Z_{\varepsilon_{2}}(h^{\prime})(0),\allowbreak\dots which we know converge to a point, and thus are all within a bounded distance from that point. Thus Z ε 1 ​ ( h ′), Z ε 2 ​ ( h ′), … Z_{\varepsilon_{1}}(h^{\prime}),Z_{\varepsilon_{2}}(h^{\prime}),\dots has an infinite subsequence Z ε i 1 ​ ( h ′), Z ε i 2 ​ ( h ′), … Z_{\varepsilon_{i_{1}}}(h^{\prime}),Z_{\varepsilon_{i_{2}}}(h^{\prime}),\dots that converges pointwise to some function, which we define to be Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}).

It remains to check that Z 0 ′ Z_{0}^{\prime} is a (larger) good partial pursuer strategy. By construction, Z 0 ′ Z_{0}^{\prime} is good and satisfies the nonbranching-lookahead constraint. Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}) satisfies the speed constraint because the pointwise limit of r r -Lipschitz functions is r r -Lipschitz.

Case 1: t ∗ t^{*} is realized.

Then we have an escaper path h ∈ dom ⁡ ( Z 0) h\in\operatorname{dom}(Z_{0}) such that h, h ′ h,h^{\prime} agree on [0, t ∗] [0,t^{*}]. Because Z 0 Z_{0} is good, we have a sequence Z ε 1 ​ ( h), Z ε 2 ​ ( h), … Z_{\varepsilon_{1}}(h),Z_{\varepsilon_{2}}(h),\dots that converges pointwise to Z 0 ​ ( h) Z_{0}(h). The given strategies Z ε Z_{\varepsilon} are defined on all escaper paths, so we can form the corresponding sequence Z ε 1 ​ ( h ′), Z ε 2 ​ ( h ′), … Z_{\varepsilon_{1}}(h^{\prime}),Z_{\varepsilon_{2}}(h^{\prime}),\dots.

As in Case 0, we can apply Lemma 5.3 to this sequence of functions to get an infinite subsequence Z ε i 1 ​ ( h ′), Z ε i 2 ​ ( h ′), … Z_{\varepsilon_{i_{1}}}(h^{\prime}),Z_{\varepsilon_{i_{2}}}(h^{\prime}),\dots that converges pointwise to some function, which we define to be Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}). As in Case 0, Z 0 ′ Z_{0}^{\prime} is good and Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}) is a pursuer motion path.

To prove that Z 0 ′ Z_{0}^{\prime} satisfies the nonbranching-lookahead constraint, it suffices to check that Z 0 ′ ​ ( h ′), Z 0 ′ ​ ( h) = Z 0 ​ ( h) Z_{0}^{\prime}(h^{\prime}),Z_{0}^{\prime}(h)=Z_{0}(h) agree on [0, t ∗] [0,t^{*}] (because t ∗ t^{*} is maximum). The subsequence Z ε i 1 ​ ( h), Z ε i 1 ​ ( h), … Z_{\varepsilon_{i_{1}}}(h),\allowbreak Z_{\varepsilon_{i_{1}}}(h),\allowbreak\dots converges pointwise to Z 0 ​ ( h) Z_{0}(h) because it is a subsequence of the sequence Z ε 1 ​ ( h), Z ε 2 ​ ( h), … Z_{\varepsilon_{1}}(h),\allowbreak Z_{\varepsilon_{2}}(h),\allowbreak\dots which we assumed converged to Z 0 ​ ( h) Z_{0}(h), and the corresponding subsequence Z ε i 1 ​ ( h ′), Z ε i 1 ​ ( h ′), … Z_{\varepsilon_{i_{1}}}(h^{\prime}),\allowbreak Z_{\varepsilon_{i_{1}}}(h^{\prime}),\allowbreak\dots converges pointwise to Z 0 ′ ​ ( h ′) Z_{0}^{\prime}(h^{\prime}) by definition. For each j j, the given strategy Z ε i j Z_{\varepsilon_{i_{j}}} satisfies the nonbranching-lookahead constraint, so Z ε i j ​ ( h), Z ε i j ​ ( h ′) Z_{\varepsilon_{i_{j}}}(h),Z_{\varepsilon_{i_{j}}}(h^{\prime}) agree on [0, t ∗] [0,t^{*}]. Taking the two limits over the identical sequence ε i 1, ε i 2, … \varepsilon_{i_{1}},\varepsilon_{i_{2}},\dots, we obtain that Z 0 ​ ( h), Z 0 ′ ​ ( h ′) Z_{0}(h),Z_{0}^{\prime}(h^{\prime}) also agree on [0, t ∗] [0,t^{*}].

Case 2: t ∗ t^{*} is not realized.

By definition of sup \sup, we have an infinite sequence of escaper paths h 1, h 2, … ∈ dom ⁡ ( Z 0) h_{1},h_{2},\ldots\in\operatorname{dom}(Z_{0}) such that h ′, h i h^{\prime},h_{i} agree on [0, t i ∗] [0,t^{*}_{i}] where t i ∗ → t ∗ t^{*}_{i}\to t^{*} and t ∗ > 0 t^{*}>0. We can apply Lemma 5.3 to this sequence: uniform equicontinuity follows from escaper paths being Lipschitz with constant 1 1, and uniform local boundedness follows because all escaper motion paths h i h_{i} agree at time 0 0, so at time t t they remain within distance t t of that starting point. By Lemma 5.3, we obtain a subsequence h i 1, h i 2, … h_{i_{1}},h_{i_{2}},\ldots that converges pointwise to some h ∗ h^{*}. This h ∗ h^{*} is an escaper motion path because the pointwise limit of 1 1 -Lipschitz functions is 1 1 -Lipschitz. We claim that h ∗, h ′ h^{*},h^{\prime} agree on [0, t ∗] [0,t^{*}]: for any t < t ∗ t<t^{*}, for sufficiently large i i, h i ​ ( t) h_{i}(t) agrees with h ′ ​ ( t) h^{\prime}(t), and thus so does h ∗ ​ ( t) h^{*}(t); and for t ∗ t^{*}, for any ε > 0 \varepsilon>0, h ′ ​ ( t ∗) h^{\prime}(t^{*}) is within ε \varepsilon of h ′ ​ ( t ∗ − ε) h^{\prime}(t^{*}-\varepsilon) (by 1-Lipschitz of h ′ h^{\prime}), which is h ∗ ​ ( t ∗ − ε) h^{*}(t^{*}-\varepsilon) for sufficiently large i i, which is within ε \varepsilon of h ∗ ​ ( t ∗) h^{*}(t^{*}) (by 1-Lipschitz of h ∗ h^{*}), so h ′ ​ ( t ∗) h^{\prime}(t^{*}) is within 2 ​ ε 2\varepsilon of h ∗ ​ ( t ∗) h^{*}(t^{*}).

Because we are in Case 2, h ∗ ∉ dom ⁡ ( Z 0) h^{*}\notin\operatorname{dom}(Z_{0}). Because each h i ∈ dom ⁡ ( Z 0) h_{i}\in\operatorname{dom}(Z_{0}), we can construct the sequence Z 0 ​ ( h i 1), Z 0 ​ ( h i 2), … Z_{0}(h_{i_{1}}),Z_{0}(h_{i_{2}}),\dots. We can apply Lemma 5.3 to this sequence: uniform equicontinuity follows from pursuer paths being Lipschitz with constant r r, and uniform local boundedness follows because all escaper motion paths h i h_{i} agree at time 0 0, and Z 0 Z_{0} satisfies the nonbranching-lookahead constraint, so all pursuer motion paths Z 0 ​ ( h i) Z_{0}(h_{i}) agree at time 0 0, so at time t t they remain within distance t t of that starting point. By Lemma 5.3, we obtain a subsequence Z 0 ​ ( h i 1 ′), Z 0 ​ ( h i 2 ′), … Z_{0}(h_{i^{\prime}_{1}}),Z_{0}(h_{i^{\prime}_{2}}),\dots that converges pointwise to some function, which we define to be Z 0 ′ ​ ( h ∗) Z_{0}^{\prime}(h^{*}). As in Cases 0 and 1, Z 0 ′ Z_{0}^{\prime} is good and Z 0 ′ ​ ( h ∗) Z_{0}^{\prime}(h^{*}) is a pursuer motion path.

To prove that Z 0 ′ Z_{0}^{\prime} satisfies the nonbranching-lookahead constraint, consider an escaper motion path h ∈ dom ⁡ ( Z 0) h\in\operatorname{dom}(Z_{0}), and suppose that h, h ∗ h,h^{*} agree on [0, t] [0,t], where t t is necessarily less than the supremum t ∗ t^{*} (because we are in Case 2 and h ∗, h ′ h^{*},h^{\prime} agree on [0, t ∗] [0,t^{*}]). Take the infinite subsequence i 1 ′′, i 2 ′′, … i^{\prime\prime}_{1},i^{\prime\prime}_{2},\dots of i 1 ′, i 2 ′, … i^{\prime}_{1},i^{\prime}_{2},\dots where t i j ′′ ∗ ≥ t t^{*}_{i^{\prime\prime}_{j}}\geq t. Thus h, h ∗, h i 1 ′′, h i 2 ′′, … h,h^{*},h_{i^{\prime\prime}_{1}},h_{i^{\prime\prime}_{2}},\dots agree on [0, t] [0,t]. Because Z 0 Z_{0} satisfies the nonbranching-lookahead constraint, Z 0 ​ ( h), Z 0 ​ ( h i 1 ′′), Z 0 ​ ( h i 2 ′′), … Z_{0}(h),Z_{0}(h_{i^{\prime\prime}_{1}}),Z_{0}(h_{i^{\prime\prime}_{2}}),\dots agree on [0, t] [0,t]. Because Z 0 ​ ( h i 1 ′′), Z 0 ​ ( h i 2 ′′), … Z_{0}(h_{i^{\prime\prime}_{1}}),Z_{0}(h_{i^{\prime\prime}_{2}}),\dots converges pointwise to Z 0 ′ ​ ( h ∗) Z_{0}^{\prime}(h^{*}), we obtain that Z 0 ​ ( h), Z 0 ′ ​ ( h ∗) Z_{0}(h),Z_{0}^{\prime}(h^{*}) agree on [0, t] [0,t].

If h ′ = h ∗ h^{\prime}=h^{*}, we have achieved our goal. Otherwise, we are now in Case 1: the supremum t ∗ t^{*} is realized by h ∗ h^{*}. By Case 1, we can add h ′ h^{\prime} to dom ⁡ ( Z 0 ′) \operatorname{dom}(Z_{0}^{\prime}) as well.

Finally, we show that Z 0 Z_{0} wins G ε G_{\varepsilon} for all ε > 0 \varepsilon>0, or more generally, any good partial strategy Z Z wins all G ε G_{\varepsilon} if the escaper is restricted to motion paths in dom ⁡ ( Z) \operatorname{dom}(Z). Take any ε > 0 \varepsilon>0 and any escaper motion path h ∈ dom ⁡ ( Z) h\in\operatorname{dom}(Z). Because Z Z is good, Z ⁡ ( h) Z(h) is the limit of Z ε 1 ​ ( h), Z ε 2 ​ ( h), … Z_{\varepsilon_{1}}(h),Z_{\varepsilon_{2}}(h),\dots for some sequence ε 1, ε 2, … \varepsilon_{1},\varepsilon_{2},\dots converging to 0 0. For all ε i < ε / 2 \varepsilon_{i}<\varepsilon/2, Z ε i ​ ( h) Z_{\varepsilon_{i}}(h) prevents the escaper (following path h h) from exiting ε i < ε / 2 \varepsilon_{i}<\varepsilon/2 away from the pursuer (in the pursuer metric), i.e., for any time t ≥ 0 t\geq 0, h ⁡ ( t) ∈ X h(t)\in X implies d z ​ ( h ⁡ ( t), Z ε i ​ ( h) ​ ( t)) < ε i < ε / 2 d_{z}(h(t),Z_{\varepsilon_{i}}(h)(t))<\varepsilon_{i}<\varepsilon/2. By (pointwise) convergence, for any time t ≥ 0 t\geq 0, for sufficiently large i i, Z ε i ​ ( h) ​ ( t) Z_{\varepsilon_{i}}(h)(t) is within ε / 2 \varepsilon/2 of Z ​ ( h) ​ ( t) Z(h)(t) (in the pursuer metric). By triangle inequality, for any time t ≥ 0 t\geq 0, h ⁡ ( t) ∈ X h(t)\in X implies d z ​ ( h ⁡ ( t), Z ⁡ ( h) ​ ( t)) < ε / 2 + ε / 2 = ε d_{z}(h(t),Z(h)(t))<\varepsilon/2+\varepsilon/2=\varepsilon, i.e., Z ​ ( h) ​ ( t) Z(h)(t) prevents the escaper from exiting ε / 2 + ε / 2 = ε \varepsilon/2+\varepsilon/2=\varepsilon away from the pursuer (in the pursuer metric). Therefore, Z Z wins G ε G_{\varepsilon} when restricted to motion paths h ∈ dom ⁡ ( Z) h\in\operatorname{dom}(Z), for all ε > 0 \varepsilon>0. In particular, Z 0 Z_{0} wins G ε G_{\varepsilon} for all ε > 0 \varepsilon>0. ∎

Thus, under the Axiom of Choice, our definition of winning G G is equivalent to the existence of a single winning strategy for that player. An escaper strategy wins 𝑮 G if it wins by ε \varepsilon for some ε > 0 \varepsilon>0. A pursuer strategy wins 𝑮 G if it prevents the escaper from winning by ε \varepsilon for all ε > 0 \varepsilon>0. Henceforth, we will use the notions of winning G ε G_{\varepsilon} instead of G G, so as to not rely on the Axiom of Choice.

### 5.2 Both Players Cannot Win: Oblivious Strategies and Unique Playthroughs

In this section, we prove that our definitions prevent both players from having “winning strategies”, similar to stronger result about locally finite strategies for Lion and Man [BLW09]. Our main approach is to construct a valid playthrough that can result from a given pursuer strategy Z Z and escaper strategy H H, that is, an actual pursuer path z z and escaper path h h consistent with the strategies: z = Z ⁡ ( h) z=Z(h) and h = H ⁡ ( z) h=H(z). Any playthrough has a clear winner. We show that any winning player strategy can be modified to induce unique playthroughs, no matter what path/strategy the opponent chooses, while preserving the winning property.

#### Oblivious strategies.

Our main tool is the idea of “ δ \delta -oblivious” player strategies, where the player can only see and react to where the opponent was at times at least δ \delta ago. Formally, a player strategy A A is 𝜹 \delta -oblivious if it satisfies the following strengthening of the nonbranching-lookahead constraint:

for any two opponent motion paths b 1, b 2 b_{1},b_{2} agreeing on [0, t] [0,t], the strategy’s player motion paths A ⁡ ( b 1), A ⁡ ( b 2) A(b_{1}),A(b_{2}) agree on [0, t + δ] [0,t+\delta].

This definition is a stronger form of the nonbranching-lookahead constraint that guarantees a positive ( δ \delta) amount of no lookahead.

Oblivious strategies are a stronger notion than “locally finite strategies” introduced in [BLW09, Section 6], which effectively allow δ \delta to adapt (in particular, get smaller) as time advances. (For example, the classic Lion and Man solution is locally finite but not δ \delta -oblivious for any δ > 0 \delta>0, because the lion gets arbitrarily close to the man, so the man must react faster and faster.) If either player uses a locally finite strategy, then the game has a unique playthrough [BLW12, Proposition 14]. For completeness, we prove the weaker (and simpler) version we need: one oblivious strategy implies unique playthrough.

###### Lemma 5.4.

If one player uses a δ \delta -oblivious strategy A A for any δ > 0 \delta>0, then for any opponent strategy B B, the game has a unique playthrough.

###### Proof.

We will prove that strategies ( A, B) (A,B) have a unique playthrough ( a, b) (a,b) defined up until time k ​ δ k\delta, by induction on k k.

In the base case k = 0 k=0, the unique playthrough consists of trivial paths where neither player moves, but we need to define the starting point for both players. The escaper strategy defines a unique starting point for the escaper path (by the escaper start constraint), and thus the pursuer strategy defines a unique starting point for the pursuer path (by the nonbranching-lookahead constraint).

Now suppose we have determined a unique playthrough ( a, b) (a,b) up until time k ​ δ k\delta, i.e., we have determined a ⁡ ( [0, k ​ δ]) a([0,k\delta]) and b ⁡ ( [0, k ​ δ]) b([0,k\delta]). By the δ \delta -obliviousness of A A, A ​ ( b) ​ ( [0, ( k + 1) ​ δ]) A(b)([0,(k+1)\delta]) is a function just of the opponent path b ⁡ ( [0, k ​ δ]) b([0,k\delta]), and is therefore uniquely determined by the partial playthrough determined so far. Thus we can set a ⁡ ( [0, ( k + 1) ​ δ]) a([0,(k+1)\delta]) accordingly. Then the opponent’s strategy B ​ ( a) ​ ( [0, ( k + 1) ​ δ]) B(a)([0,(k+1)\delta]) is determined, being a function of a ⁡ ( [0, ( k + 1) ​ δ]) a([0,(k+1)\delta]) (by the nonbranching-lookahead constraint). Therefore we determine a a and b b uniquely and consistently by induction. ∎

Crucially, we do not require that strategies be δ \delta -oblivious. (Such a restriction is rightly rejected in [BLW09] because it forbids natural strategies such as “run in the direction of the escaper”.) But we can exploit the ε \varepsilon distance tolerance that we incorporated into the definition of the pursuer winning to show that any winning player strategy can be made oblivious, with some tweaking of the parameters:

###### Lemma 5.5 (Obliviate Lemma).

If a player has a winning strategy in G ε G_{\varepsilon} with speed ratio r r, then that player has a δ \delta -oblivious winning strategy in G ε ′ G_{\varepsilon^{\prime}}, where δ = ε 2 ​ r \delta={\varepsilon\over 2r}, and where ε ′ = 1 2 ​ ε \varepsilon^{\prime}={1\over 2}\varepsilon if the player is the escaper and ε ′ = 3 2 ​ ε \varepsilon^{\prime}={3\over 2}\varepsilon if the player is the pursuer.

###### Proof.

Given a player winning strategy A A for G ε G_{\varepsilon}, we construct a δ \delta -oblivious player winning strategy A δ A_{\delta}. Given an opponent motion path b b, we construct a player motion path A δ ​ ( b) A_{\delta}(b) that stands still for δ \delta time, then mimics strategy A A but with a shifted version of b b:

 | A δ ​ ( b) ​ ( [0, δ]) \displaystyle A_{\delta}(b)([0,\delta]) | = A ​ ( b) ​ ( 0), \displaystyle=A(b)(0), |  |

 | A δ ​ ( b) ​ ( t + δ) \displaystyle A_{\delta}(b)(t+\delta) | = A ​ ( b ​ ( [0, t])) ​ ( t). \displaystyle=A(b([0,t]))(t). |  |

This player strategy A δ A_{\delta} is clearly δ \delta -oblivious. We show that it wins G ε ′ G_{\varepsilon^{\prime}} in two cases.

First, if the player is the escaper, then for any pursuer motion path b b, the given winning strategy A A for G ε G_{\varepsilon} has a time t t such that A ​ ( b) ​ ( t) A(b)(t) is at an exit while b ⁡ ( t) b(t) is at least ε \varepsilon away in the pursuer metric. We obtain a similar time t + δ t+\delta for the constructed δ \delta -oblivious strategy A δ A_{\delta}: A δ ​ ( b) ​ ( t + δ) = A ⁡ ( b) ​ ( t) A_{\delta}(b)(t+\delta)=A(b)(t) is at an exit, and by the speed-limit constraint, b ⁡ ( t + δ) b(t+\delta) is at most δ ​ r = ε / 2 \delta r=\varepsilon/2 closer than b ⁡ ( t) b(t) was.

Second, if the player is the pursuer, then for any escaper motion path b b, and for any time t t where b ⁡ ( t) b(t) is on an exit, the given winning strategy A A for G ε G_{\varepsilon} guarantees that A ​ ( b) ​ ( t) A(b)(t) is < ε <\varepsilon distance from b ⁡ ( t) b(t). We prove the analogous result for A δ A_{\delta}: if b ⁡ ( t) b(t) is at an exit, then A δ ​ ( b) ​ ( t + δ) = A ⁡ ( b) ​ ( t) A_{\delta}(b)(t+\delta)=A(b)(t) is < ε <\varepsilon distance from b ⁡ ( t) b(t), and by the speed-limit constraint, A δ ​ ( b) ​ ( t) A_{\delta}(b)(t) is at most δ ​ r = ε / 2 \delta r=\varepsilon/2 away from A ​ ( b) ​ ( t) A(b)(t). The farthest it can be from b ⁡ ( t) b(t) is then 3 2 ​ ε {3\over 2}\varepsilon. ∎

###### Corollary 5.6.

If a player has a winning strategy A A for G ε G_{\varepsilon} with speed ratio r r, then that player has a winning strategy A ^ \hat{A} for G ε ′ G_{\varepsilon^{\prime}} (where ε ′ = 1 2 ​ ε \varepsilon^{\prime}={1\over 2}\varepsilon if the player is the escaper and ε ′ = 3 2 ​ ε \varepsilon^{\prime}={3\over 2}\varepsilon if the player is the pursuer) such that, for every opponent strategy B B, the game of A ^ \hat{A} against B B has a unique playthrough (where the player wins).

###### Proof.

By Lemma 5.5, the player has a δ \delta -oblivious winning strategy A ^ \hat{A} for G ε ′ G_{\varepsilon^{\prime}}. By Lemma 5.4, there is a unique playthrough ( a ^, b) (\hat{a},b) such that a ^ = A ^ ​ ( b) \hat{a}=\hat{A}(b) and B ⁡ ( a ^) = b B(\hat{a})=b. Because A ^ \hat{A} wins against all opponent paths, it wins against b b. ∎

Now it follows that both players cannot win in the pursuit–escape game G G, given that our definition of the escaper winning by a uniform ε > 0 \varepsilon>0. (Again, a stronger result for locally finite strategies in the Lion-and-Man game is mentioned in [BLW09, after Proposition 14].)

###### Corollary 5.7.

For no pursuit–escape game G G can both the escaper and pursuer win.

###### Proof.

Suppose the escaper wins G G. By definition, there is an escaper winning strategy H H for G ε G_{\varepsilon} for some ε > 0 \varepsilon>0. By Corollary 5.6, there is an escaper winning strategy H ^ \hat{H} for G ε ′ G_{\varepsilon^{\prime}}, for some ε ′ > 0 \varepsilon^{\prime}>0, that has unique playthroughs against all pursuer strategies where the escaper wins.

If the pursuer also wins G G, then for all ε > 0 \varepsilon>0, there is a pursuer winning strategy Z ε Z_{\varepsilon} for G ε G_{\varepsilon}; in particular, we obtain Z ε ′ Z_{\varepsilon^{\prime}} for G ε ′ G_{\varepsilon^{\prime}}. But H ^ \hat{H} and Z ε ′ Z_{\varepsilon^{\prime}} have a unique playthrough where the escaper wins, contradicting that Z ε ′ Z_{\varepsilon^{\prime}} is a pursuer winning strategy. ∎

#### Specified starting points.

Next we consider a variant G ⁡ ( s h, s z) G(s_{h},s_{z}) of the game G G where we are given the starting points s h s_{h} and s z s_{z} for the escaper and pursuer, respectively (like the Lion and Man problem). This game naturally arises when analyzing strategies in the middle of a game G G; in particular, we did so in Section 4.2. A similar proof technique to the Obliviate Lemma gives us another interesting result about robustness over starting points:

###### Lemma 5.8.

Suppose the escaper has a winning strategy for G ε ​ ( s h, s z) G_{\varepsilon}(s_{h},s_{z}), and that s z ′ s^{\prime}_{z} is another point in the pursuer domain with d z ​ ( s z, s z ′) = δ < ε d_{z}(s_{z},s^{\prime}_{z})=\delta<\varepsilon. Then the escaper has a winning strategy for G ε − δ ​ ( s h, s z ′) G_{\varepsilon-\delta}(s_{h},s^{\prime}_{z}).

###### Proof.

Let H H be the assumed escaper strategy that wins G ε ​ ( s h, s z) G_{\varepsilon}(s_{h},s_{z}). We define a new escaper strategy H ′ H^{\prime} that wins G ε − δ ​ ( s h, s z ′) G_{\varepsilon-\delta}(s_{h},s^{\prime}_{z}): for any pursuer path z ′ ​ ( t) z^{\prime}(t) starting at s z ′ s^{\prime}_{z}, the escaper strategy will return an escaper path H ′ ​ ( s z ′, t) H^{\prime}(s^{\prime}_{z},t) defined as follows. Let z s ​ ( t) z_{s}(t) be the pursuer path starting at s z s_{z} running at full speed along a shortest path in the pursuer metric to s z ′ s^{\prime}_{z} (in exactly δ / r \delta/r seconds), and then for t > δ / r t>\delta/r let z s ​ ( t) = z ′ ​ ( t − δ / r) z_{s}(t)=z^{\prime}(t-\delta/r). Define H ′ ​ ( z s ′, t) = H ⁡ ( z s, t) H^{\prime}(z^{\prime}_{s},t)=H(z_{s},t). Observe that strategy Z ′ Z^{\prime} satisfies:

- •

the nonbranching-lookahead constraint because H ′ ​ ( z b, t) H^{\prime}(z_{b},t) depends only on z s ′ z^{\prime}_{s} restricted to the closed interval [0, t − δ / r] [0,t-\delta/r] (unless t < δ / r t<\delta/r, in which case H ′ ​ ( z b, t) H^{\prime}(z_{b},t) is independent of z b z_{b}), and

- •

the speed-limit constraint because H H does and z s z_{s} obeys speed limit r r.

To see that strategy Z ′ Z^{\prime} wins G ε − δ ​ ( s h, s z ′) G_{\varepsilon-\delta}(s_{h},s^{\prime}_{z}), consider a particular pursuer path z ′ ​ ( t) z^{\prime}(t), and define z s ​ ( t) z_{s}(t) as above. Because Z Z is a winning strategy for G ε ​ ( s h, s z) G_{\varepsilon}(s_{h},s_{z}), there exists some time u u at which the escaper wins at boundary point h s = Z ⁡ ( z s, u) h_{s}=Z(z_{s},u) where d z ​ ( h s, z s ​ ( u)) ≥ ε d_{z}(h_{s},z_{s}(u))\geq\varepsilon. According to strategy Z ′ Z^{\prime}, the escaper at time u u reaches the same boundary point Z ′ ​ ( z ′, u) = Z ⁡ ( z s, u) = h s Z^{\prime}(z^{\prime},u)=Z(z_{s},u)=h_{s}, and the pursuer is at point z ′ ​ ( u) z^{\prime}(u). We claim that z ′ ​ ( u) z^{\prime}(u) has distance at least ε − δ \varepsilon-\delta from h s h_{s} in the pursuer metric, so the escaper wins at time u u.

Because pursuer has speed at most r r, d z ​ ( z s ​ ( u), z ′ ​ ( u)) = d z ​ ( z ′ ​ ( u − δ / r), z ′ ​ ( u)) ≤ δ d_{z}(z_{s}(u),z^{\prime}(u))=d_{z}(z^{\prime}(u-\delta/r),z^{\prime}(u))\leq\delta. And because d z ​ ( h s, z s ​ ( u)) ≥ ε d_{z}(h_{s},z_{s}(u))\geq\varepsilon, by the triangle inequality, d z ​ ( h s, z ′ ​ ( u)) ≥ ε − δ d_{z}(h_{s},z^{\prime}(u))\geq\varepsilon-\delta as desired. ∎

###### Corollary 5.9.

If the escaper can win G ⁡ ( s h, s z) G(s_{h},s_{z}), then the escaper can win G ⁡ ( s h, s z ′) G(s_{h},s^{\prime}_{z}) for all s z ′ s^{\prime}_{z} in some open d z d_{z} -neighborhood of s z s_{z}.

### 5.3 Discrete Game

In this section, we show how to discretize the (continuous) pursuit–escape game while closely approximating winning strategies. This tool will enable us to prove that some player always wins (in Section 5.4) and to obtain a pseudopolynomial-time approximation scheme (in Section 6). Bollobas et al. [BLW09] define a discrete pursuit–evasion game, which discretizes time into steps, but players still move in the original continuous domains. By contrast, we discretize both time and space. Combining this discretization with the stronger oblivious property that we obtained in Section 5.2 enables us to obtain finite approximation algorithms in Section 6. Our discrete game is similar in spirit to a discretization of pursuit–evasion games given by Reif and Tate [RT93, Section 4], but the difference in models means that we need to prove our own results about approximating the continuous game.

#### Discretization.

Given a pursuit–escape game consisting of an escaper domain D h D_{h}, pursuer domain D z D_{z}, exit set X X, and speed ratio r r, we define the ( 𝜹, 𝜸) (\delta,\gamma) -discretized game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) as follows. We write an explicit “ ( r) (r) ” for the intended speed ratio, as we will need to adjust it when relating to the continuous game G = G ⁡ ( r) G=G(r).

First we define a 𝜸 \gamma -sampling algorithm which, given a locally finitely rectifiable set Q Q (such as D h D_{h}, D z D_{z}, or X X), produces a countable set S Q, γ S_{Q,\gamma} of sample points such that every point q ∈ Q q\in Q has a γ \gamma -nearby sample point. In the special case that Q Q is finitely rectifiable, the sample set S Q, γ S_{Q,\gamma} is in fact finite. We define the 𝜸 \gamma -sample S Q, γ S_{Q,\gamma} of Q Q in two cases:

- •

For a finitely rectifiable set R R, the γ \gamma -sample of R R is the union, over every Lipschitz patch S: [0, 1] k → R S:[0,1]^{k}\to R constituting R R, of the finite point set { S ( i 1 / m, i 2 / m, …, i k / m) ∣ i 1, i 2, …, i k ∈ { 0, 1, …, m } } \big\{S(i_{1}/m,i_{2}/m,\dots,i_{k}/m)\mid i_{1},i_{2},\dots,i_{k}\in\{0,1,\dots,m\}\big\} where m = ⌈ 1 / ( k 2 ​ γ) ⌉ m=\left\lceil 1/\left({\sqrt{k}\over 2}{\gamma}\right)\right\rceil. Because R R is bounded, this sample set is finite.

- •

For a locally finitely rectifiable set Q Q, the γ \gamma -sample of Q Q is the union, over every positive integer ρ \rho, of the γ \gamma -sample of Q Q intersected with the radius- ρ \rho Euclidean ball centered at the origin. (Each such intersection is finitely rectifiable, so its γ \gamma -sample is defined above.) This γ \gamma -sample consists of countably many points.

###### Lemma 5.10.

Every point q ∈ Q q\in Q is within distance γ \gamma of a sample point in S Q, γ S_{Q,\gamma}, where distance is measured via the Euclidean shortest-path metric d Q d_{Q} in Q Q.

###### Proof.

First restrict to the integer-radius- ⌈ ‖ q ‖ + γ ⌉ \lceil\|q\|+\gamma\rceil ball A A centered at the origin, so that Q ∩ A Q\cap A is finitely rectifiable and has an associated sample set S Q ∩ A, γ ⊆ S Q, γ S_{Q\cap A,\gamma}\subseteq S_{Q,\gamma}. Let S S be a Lipschitz patch of Q ∩ A Q\cap A containing q ∈ Q q\in Q. Consider the closed radius- γ \gamma ball B B centered at q q which is intrinsic to surface S S (the ball’s distance is measured with respect to the metric on S S), which is contained in A A (by the construction of A A). By construction of the γ \gamma -sample S Q ∩ A, γ S_{Q\cap A,\gamma}, and by the Lipschitz property of S S, B B contains a point b b of S Q ∩ A, γ ⊆ S Q, γ S_{Q\cap A,\gamma}\subseteq S_{Q,\gamma}. By definition of the ball B B, d Q ​ ( q, b) ≤ γ d_{Q}(q,b)\leq\gamma as desired. ∎

Now we define a graph for the ( δ, γ) (\delta,\gamma) -discretized game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r):

- •

Define escaper vertex set V h = S D h, γ ∪ S X, γ V_{h}=S_{D_{h},\gamma}\cup S_{X,\gamma} and pursuer vertex set V z = S D z, γ ∪ S X, γ V_{z}=S_{D_{z},\gamma}\cup S_{X,\gamma}. Notably, both players share the exit sample S X, γ S_{X,\gamma}.

- •

The escaper edge set E h E_{h} contains edges between all pairs p, q ∈ V h p,q\in V_{h} such that d h ​ ( p, q) ≤ δ d_{h}(p,q)\leq\delta.

- •

The pursuer edge set E z E_{z} contains edges between all pairs p, q ∈ V z p,q\in V_{z} such that d z ​ ( p, q) ≤ r ​ δ d_{z}(p,q)\leq r\delta.

Finally we can define the game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) which has discrete alternation between the players. To start, the escaper chooses a point h 0 h_{0} from V h V_{h}; and then the pursuer chooses a point z 0 z_{0} from V z V_{z}. In turn i ∈ { 1, 2, … } i\in\{1,2,\dots\}, the escaper chooses a point h i h_{i} from V h V_{h} such that ( h i − 1, h i) ∈ E h (h_{i-1},h_{i})\in E_{h}; and then the pursuer chooses a point z i z_{i} from V z V_{z} such that ( z i − 1, z i) ∈ E z (z_{i-1},z_{i})\in E_{z}. The escaper wins if, in some turn j j, there is a discrete exit point x ∈ B x x\in B_{x} such that ( h j, x) ∈ E h (h_{j},x)\in E_{h} yet ( z j + 1, x) ∉ E z (z_{j+1},x)\notin E_{z}; and the pursuer wins if there is no such turn. In other words, in the discrete game, the pursuer gets two turns ( z j z_{j} and z j + 1 z_{j+1}) to respond to an escaper threat h j h_{j} to exit (analogous to the pursuer getting an extra reach of ε \varepsilon in the continuous game). It may seem strange that the escaper wins without ever actually reaching the boundary. This captures a moment when it is clear the escaper has a forced win. Using this definition, rather than when the escaper actually reaches a boundary vertex, will be useful in future proofs when we want to consider a moment when the escaper is ’close enough’ to just run to the boundary and win, or the pursuer always stays close enough to the escaper to prevent this.

#### Approximation.

Now we argue that winning strategies for the discrete game G ^ \hat{G} can be adapted to winning strategies for the continuous game G G with slightly different parameters.

###### Theorem 5.11.

If the discrete game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) has a player winning strategy where γ ≤ min ⁡ { 1 4, r 2 } ​ δ \gamma\leq\min\{{1\over 4},{r\over 2}\}\delta, then the continuous game G ε ​ ( r ′) G_{\varepsilon}(r^{\prime}) has a player winning strategy, where ε = 1 2 ​ r ​ δ \varepsilon={1\over 2}r\delta and r ′ = r − 2 ​ γ δ r^{\prime}=r-2{\gamma\over\delta} if the player is the escaper, and ε = 5 2 ​ r ​ δ \varepsilon={5\over 2}r\delta and r ′ = r / ( 1 − 2 ​ γ δ) r^{\prime}=r/(1-2{\gamma\over\delta}) if the player is the pursuer.

###### Proof.

For a ∈ { h, z } a\in\{h,z\} and for any point p ∈ D a p\in D_{a}, define

 | round a ⁡ p = { point ∈ S X, γ ​ nearest to ​ p ​ in ​ d X if ​ p ∈ X, point ∈ V a = S D a, γ ∪ S X, γ ​ nearest to ​ p ​ in ​ d a if ​ p ∉ X. \round_{a}p=\begin{cases}\text{point}\in S_{X,\gamma}\text{ nearest to }p\text{ in }d_{X}&\text{if }p\in X,\\ \text{point}\in V_{a}=S_{D_{a},\gamma}\cup S_{X,\gamma}\text{ nearest to }p\text{ in }d_{a}&\text{if }p\notin X.\\ \end{cases} |  |

By Lemma 5.10 and because X ⊆ D a X\subseteq D_{a}, d a ​ ( p, round a ⁡ p) ≤ γ d_{a}(p,\round_{a}p)\leq\gamma for any point p ∈ D a p\in D_{a}.

Case 1: The player is the escaper. We construct a continuous escaper winning strategy H ⁡ ( z) H(z) for G r ​ δ − γ ​ ( r − 2 ​ γ δ) G_{r\delta-\gamma}(r-2{\gamma\over\delta}), given a pursuer motion path z z. The continuous escaper starts at H ​ ( z) ​ ( 0) = h 0 H(z)(0)=h_{0}, the discrete point where the discrete escaper strategy starts. We give the discrete escaper strategy as input the pursuer move sequence z i = round z ⁡ z ⁡ ( i ​ δ) z_{i}=\round_{z}z(i\delta) for i ∈ { 0, 1, … } i\in\{0,1,\dots\}. To confirm that this sequence satisfies ( z i, z i + 1) ∈ E Z (z_{i},z_{i+1})\in E_{Z} for all i i, we can use the triangle inequality, the claim above, and that z z satisfies the r − 2 ​ γ δ r-2{\gamma\over\delta} speed-limit constraint:

 |  | d z ​ ( z i, z i + 1) \displaystyle d_{z}(z_{i},z_{i+1}) |  |

 |  | = d z ​ ( round z ⁡ z ⁡ ( i ​ δ), round z ⁡ z ⁡ ( ( i + 1) ​ δ)) \displaystyle=d_{z}\big(\round_{z}z(i\delta),\round_{z}z((i+1)\delta)\big) |  |

 |  | ≤ d z ​ ( round z ⁡ z ⁡ ( i ​ δ), z ⁡ ( i ​ δ)) + d z ​ ( z ⁡ ( i ​ δ), z ⁡ ( ( i + 1) ​ δ)) + d z ​ ( z ⁡ ( ( i + 1) ​ δ), round z ⁡ z ⁡ ( ( i + 1) ​ δ)) \displaystyle\leq d_{z}\big(\round_{z}z(i\delta),z(i\delta)\big)+d_{z}\big(z(i\delta),z((i+1)\delta)\big)+d_{z}\big(z((i+1)\delta),\round_{z}z((i+1)\delta)\big) |  |

 |  | ≤ 2 ​ γ + ( r − 2 ​ γ δ) ​ δ \displaystyle\leq 2\gamma+\big(r-2\textstyle{\gamma\over\delta}\big)\delta |  |

 |  | = r ​ δ. \displaystyle=r\delta. |  |

Suppose turn i i of the discrete escaper strategy tells us to move the escaper to h i h_{i} (dependent on only z 0, z 1, …, z i − 1 z_{0},z_{1},\dots,z_{i-1}). Then we extend the continuous escaper strategy by letting H ⁡ ( z) ​ ( [( i − 1) ​ δ, i ​ δ]) H(z)([(i-1)\delta,i\delta]) interpolate a shortest path in d h d_{h} between h i − 1 h_{i-1} and h i h_{i}. By construction of E h E_{h}, d h ​ ( h i − 1, h i) ≤ δ d_{h}(h_{i-1},h_{i})\leq\delta, so this interpolation satisfies the escaper speed-limit constraint. Because h i h_{i} depends on only z 0, z 1, …, z i − 1 z_{0},z_{1},\dots,z_{i-1}, H ⁡ ( z) ​ ( [( i − 1) ​ δ, i ​ δ]) H(z)([(i-1)\delta,i\delta]) depends on only z ⁡ ( [0, ( i − 1) ​ δ]) z([0,(i-1)\delta]), so H H satisfies the nonbranching-lookahead constraint. (Because we are in the no-capture model, we do not need to worry about the escaper being captured during this motion.)

In the final turn j j of the discrete game, there is an exit point x ∈ X x\in X such that ( h j, x) ∈ E h (h_{j},x)\in E_{h} yet ( x, z j + 1) ∉ E z (x,z_{j+1})\notin E_{z}. (Here we use that X ⊆ D h X\subseteq D_{h}, so that d h ​ ( h j, x) ≤ d X ​ ( h j, x) d_{h}(h_{j},x)\leq d_{X}(h_{j},x).) Thus d h ​ ( h j, x) ≤ δ d_{h}(h_{j},x)\leq\delta yet d z ​ ( z j + 1, x) > r ​ δ d_{z}(z_{j+1},x)>r\delta. We finish the continuous escaper winning strategy by letting H ⁡ ( z) ​ ( [j ​ δ, ( j + 1) ​ δ]) H(z)([j\delta,(j+1)\delta]) interpolate a shortest path in d h d_{h} from h j h_{j} to x x. As above, H H satisfies the escaper speed-limit constraint and nonbranching-lookahead constraint. Furthermore, H ⁡ ( z) H(z) is a continuous escaper winning strategy for G r ​ δ − γ G_{r\delta-\gamma} because, at time t = ( j + 1) ​ δ t=(j+1)\delta, H ​ ( z) ​ ( t) H(z)(t) is at an exit x x yet z j + 1 = round z ⁡ z ⁡ ( t) z_{j+1}=\round_{z}z(t) is at a distance > r ​ δ >r\delta away, so by the claim above, z ⁡ ( t) z(t) is at distance > r ​ δ − γ >r\delta-\gamma away. By our assumption that γ ≤ r 2 ​ δ \gamma\leq{r\over 2}\delta, r ​ δ − γ ≥ r 2 ​ δ r\delta-\gamma\geq{r\over 2}\delta.

Case 2: The player is the pursuer. We construct a continuous pursuer winning strategy Z ⁡ ( h) Z(h) for G 2 ​ r ​ δ + γ ​ ( r ′) G_{2r\delta+\gamma}(r^{\prime}), given an escaper motion path h h. Let δ ′ = δ ⁡ ( 1 − 2 ​ γ δ) \delta^{\prime}=\delta(1-2{\gamma\over\delta}). We give the discrete pursuer strategy as input the escaper move sequence h i = round h ⁡ h ~ ​ ( i ​ δ ′) h_{i}=\round_{h}\tilde{h}(i\delta^{\prime}) for i ∈ { 0, 1, … } i\in\{0,1,\dots\}. To confirm that this sequence satisfies ( h i, h i + 1) ∈ E H (h_{i},h_{i+1})\in E_{H} for all i i, we can use the triangle inequality, the claim above, and that h h satisfies the 1 1 speed-limit constraint:

 |  | d h ​ ( h i, h i + 1) \displaystyle d_{h}(h_{i},h_{i+1}) |  |

 |  | = d h ​ ( round h ⁡ h ⁡ ( i ​ δ ′), round h ⁡ h ⁡ ( ( i + 1) ​ δ ′)) \displaystyle=d_{h}\big(\round_{h}h(i\delta^{\prime}),\round_{h}h((i+1)\delta^{\prime})\big) |  |

 |  | ≤ d h ​ ( round h ⁡ h ⁡ ( i ​ δ ′), h ⁡ ( i ​ δ ′)) + d h ​ ( h ⁡ ( i ​ δ ′), h ⁡ ( ( i + 1) ​ δ ′)) + d h ​ ( h ⁡ ( ( i + 1) ​ δ ′), round h ⁡ h ⁡ ( ( i + 1) ​ δ ′)) \displaystyle\leq d_{h}\big(\round_{h}h(i\delta^{\prime}),h(i\delta^{\prime})\big)+d_{h}\big(h(i\delta^{\prime}),h((i+1)\delta^{\prime})\big)+d_{h}\big(h((i+1)\delta^{\prime}),\round_{h}h((i+1)\delta^{\prime})\big) |  |

 |  | ≤ 2 ​ γ + δ ′ \displaystyle\leq 2\gamma+\delta^{\prime} |  |

 |  | = 2 ​ γ + δ ⁡ ( 1 − 2 ​ γ δ) \displaystyle=2\gamma+\delta\big(1-2\textstyle{\gamma\over\delta}\big) |  |

 |  | = δ. \displaystyle=\delta. |  |

The continuous pursuer starts at Z ​ ( h) ​ ( 0) = z 0 Z(h)(0)=z_{0}, which depends on h 0 = round h ⁡ h ⁡ ( 0) h_{0}=\round_{h}h(0) (satisfying the nonbranching-lookahead constraint). Suppose turn i i of the discrete pursuer strategy tells us to move the pursuer to z i z_{i} (dependent on only h 0, h 1, …, h i − 1 h_{0},h_{1},\dots,h_{i-1}). Then we extend the continuous pursuer strategy by letting Z ⁡ ( h) ​ ( [( i − 1) ​ δ ′, i ​ δ ′]) Z(h)([(i-1)\delta^{\prime},i\delta^{\prime}]) interpolate a shortest path in d z d_{z} from z i − 1 z_{i-1} to z i z_{i}. By definition of E z E_{z}, d z ​ ( z i − 1, z i) ≤ r ​ δ = r ′ ​ δ ′ d_{z}(z_{i-1},z_{i})\leq r\delta=r^{\prime}\delta^{\prime}, so this interpolation satisfies the r ′ r^{\prime} pursuer speed-limit constraint. Because z i z_{i} depends on only h 0, h 1, …, h i − 1 h_{0},h_{1},\dots,h_{i-1}, Z ⁡ ( h) ​ ( [( i − 1) ​ δ ′, i ​ δ ′]) Z(h)([(i-1)\delta^{\prime},i\delta^{\prime}]) depends on only h ⁡ ( [0, ( i − 1) ​ δ ′]) h([0,(i-1)\delta^{\prime}]), so Z Z satisfies the nonbranching-lookahead constraint.

To see that Z Z is a continuous pursuer winning strategy for G 2 ​ r ​ δ + γ ​ ( r ′) G_{2r\delta+\gamma}(r^{\prime}), consider a time t t where h ⁡ ( t) = x ∈ X h(t)=x\in X. Let i ​ δ ′ i\delta^{\prime} be the integer multiple of δ ′ \delta^{\prime} nearest t t, so | t − i ​ δ ′ | ≤ 1 2 |t-i\delta^{\prime}|\leq{1\over 2}. By the escaper speed-limit constraint, d h ​ ( h ⁡ ( t), h ⁡ ( i ​ δ ′)) ≤ δ ′ 2 d_{h}(h(t),h(i\delta^{\prime}))\leq{\delta^{\prime}\over 2}. By the triangle inequality and the claim above, d h ​ ( h ⁡ ( t), round h ⁡ h ⁡ ( i ​ δ ′)) ≤ δ ′ 2 + γ d_{h}(h(t),\round_{h}h(i\delta^{\prime}))\leq{\delta^{\prime}\over 2}+\gamma, i.e., d h ​ ( x, h i) ≤ δ ′ 2 + γ d_{h}(x,h_{i})\leq{\delta^{\prime}\over 2}+\gamma. By the definition of round h \round_{h}, x ^ = round h ⁡ x ∈ S X, γ \hat{x}=\round_{h}x\in S_{X,\gamma}. By the triangle inequality and the claim above, d h ​ ( x ^, h i) ≤ δ ′ 2 + 2 ​ γ ≤ δ 2 + 2 ​ γ d_{h}(\hat{x},h_{i})\leq{\delta^{\prime}\over 2}+2\gamma\leq{\delta\over 2}+2\gamma. (Here we use that X ⊆ D z X\subseteq D_{z}, so that d z ​ ( x ^, h i) ≤ d X ​ ( x ^, h i) d_{z}(\hat{x},h_{i})\leq d_{X}(\hat{x},h_{i}).) By our assumption that γ ≤ δ 4 \gamma\leq{\delta\over 4}, d h ​ ( x ^, h i) ≤ δ d_{h}(\hat{x},h_{i})\leq\delta, so ( x ^, h i) ∈ E h (\hat{x},h_{i})\in E_{h}. By the discrete win condition, ( x ^, z i + 1) ∈ E z (\hat{x},z_{i+1})\in E_{z}, so d z ​ ( x ^, z i + 1) ≤ r ​ δ d_{z}(\hat{x},z_{i+1})\leq r\delta. Thus d z ​ ( x, z i + 1) ≤ r ​ δ + γ d_{z}(x,z_{i+1})\leq r\delta+\gamma, i.e., d z ​ ( h ⁡ ( t), Z ⁡ ( h) ​ ( ( i + 1) ​ δ)) ≤ r ​ δ + γ d_{z}(h(t),Z(h)((i+1)\delta))\leq r\delta+\gamma. By the pursuer speed-limit constraint, d z ​ ( h ⁡ ( t), Z ⁡ ( h) ​ ( t)) ≤ 2 ​ r ​ δ + γ d_{z}(h(t),Z(h)(t))\leq 2r\delta+\gamma. By our assumption that γ ≤ r 2 ​ δ \gamma\leq{r\over 2}\delta, 2 ​ r ​ δ + γ ≤ 5 2 ​ r ​ δ 2r\delta+\gamma\leq{5\over 2}r\delta. ∎

### 5.4 Some Player Wins

#### Discrete game.

We start by proving that the discrete game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) (defined in Section 5.3) always has a winner. This result follows from known results, but is nontrivial because the vertex set V V can have countably many vertices (when either domain is unbounded).

###### Lemma 5.12.

The discrete game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) always has a unique winner, i.e., either has an escaper winning strategy or a pursuer winning strategy but not both.

###### Proof.

We show that any G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) is an instance of an open Gale–Stewart game [GS53], where two players alternate moves (with perfect information about past moves), a move is an element of a discrete set M M, the first player wins if the sequence of moves has a prefix in a known set A A of finite prefixes, and the second player wins if they can prevent ever having a prefix in A A. (The prefix notion of winning is what makes the game “open” in the product topology of M ω M^{\omega}.)

We can represent G ^ \hat{G} by setting M = V M=V, 10 10 10 We could even make M M finite by mapping the finite number of choices available at any state to either player (by finite rectifiability) to bounded integers. and letting a finite prefix h 0, z 0, h 1, z 1, …, h k, z k h_{0},z_{0},h_{1},z_{1},\dots,h_{k},z_{k} represent the state of the game if the escaper starts at h 0 ∈ V h h_{0}\in V_{h}, the pursuer starts at z 0 ∈ V z z_{0}\in V_{z}, then the escaper moves along ( h 0, h 1) ∈ E h (h_{0},h_{1})\in E_{h}, then the pursuer moves along ( z 0, z 1) ∈ E z (z_{0},z_{1})\in E_{z}, etc. If any z i ∉ V z z_{i}\notin V_{z}, or any ( z i, z i + 1) ∉ E z (z_{i},z_{i+1})\notin E_{z}, then we declare the prefix winning for the escaper. Conversely, if any h i ∉ V h h_{i}\notin V_{h}, or any ( h i, h i + 1) ∉ E h (h_{i},h_{i+1})\notin E_{h}, then we forbid the prefix from being winning for the escaper. Otherwise, we define the prefix as winning if and only if there is an x ∈ B x x\in B_{x} such that ( h k − 1, x) ∈ E h (h_{k-1},x)\in E_{h} yet ( z k, x) ∉ E z (z_{k},x)\notin E_{z}.

Thus the discrete pursuit–escape game G ^ \hat{G} is an open Gale–Stewart game. By open determinacy theorem [GS53] this game is strictly determined, meaning that it has a unique winner. ∎

#### Continuous game.

Now we can combine Theorem 5.11 with Lemma 5.12 to derive results about the continuous pursuit–escape game:

###### Theorem 5.13.

For any escaper domain D h D_{h}, pursuer domain D z D_{z}, exit set X X, and speed ratio r r, either the escaper wins G ⁡ ( r ′) G(r^{\prime}) for all r ′ < r r^{\prime}<r or the pursuer wins G ⁡ ( r ′) G(r^{\prime}) for all r ′ > r r^{\prime}>r (or both).

###### Proof.

Construct an infinite sequence by, for each i = 1, 2, … i=1,2,\dots, taking the ( δ i, γ i) (\delta_{i},\gamma_{i}) -discretized game G ^ δ i, γ i ​ ( r) \hat{G}_{\delta_{i},\gamma_{i}}(r) induced by ( D h, D z, X, r) (D_{h},D_{z},X,r) and parameters δ i = 1 / i \delta_{i}=1/i and γ i = min ⁡ { 1 4, r 2 } ​ δ i / i \gamma_{i}=\min\{{1\over 4},{r\over 2}\}\delta_{i}/i. By Lemma 5.12, every discrete game G ^ δ i, γ i ​ ( r) \hat{G}_{\delta_{i},\gamma_{i}}(r) has a unique winner w i w_{i} (escaper or pursuer). We split into two cases, both of which could happen (and indeed will happen at the critical speed ratio):

Case 1: If infinitely many w i w_{i} are escaper, then by Theorem 5.11, we can convert each discrete escaper winning strategy for G ^ δ i, γ i ​ ( r) \hat{G}_{\delta_{i},\gamma_{i}}(r) into a continuous escaper winning strategy for G 1 2 ​ r ​ δ i ​ ( r − 2 ​ γ i δ i) = G 1 2 ​ r / i ​ ( r − min ⁡ { 1 2, r 2 } / i) G_{{1\over 2}r\delta_{i}}(r-2{\gamma_{i}\over\delta_{i}})=G_{{1\over 2}r/i}(r-\min\{{1\over 2},{r\over 2}\}/i). By definition, the escaper wins G ⁡ ( r − min ⁡ { 1 2, r 2 } / i) G(r-\min\{{1\over 2},{r\over 2}\}/i) (as well as at all smaller speed ratios). Because this holds for infinitely many i i, and min ⁡ { 1 2, r 2 } / i → 0 \min\{{1\over 2},{r\over 2}\}/i\to 0 as i → ∞ i\to\infty, we obtain that the escaper wins G ⁡ ( r − ε) G(r-\varepsilon) for all ε > 0 \varepsilon>0.

Case 2: If infinitely many w i w_{i} are pursuer, then by Theorem 5.11, we can convert the discrete pursuer winning strategy for G ^ δ i, γ i ​ ( r) \hat{G}_{\delta_{i},\gamma_{i}}(r) into a continuous pursuer winning strategy for G 5 2 ​ r ​ δ i ​ ( r / ( 1 − 2 ​ γ i δ i) = G 5 2 ​ r / i ​ ( r / ( 1 − min ⁡ { 1 2, r 2 } / i)) CLOSE G_{{5\over 2}r\delta_{i}}(r/(1-2{\gamma_{i}\over\delta_{i}})=G_{{5\over 2}r/i}(r/(1-\min\{{1\over 2},{r\over 2}\}/i)). Each such strategy also wins G ε ​ ( r / ( 1 − min ⁡ { 1 2, r 2 } / i) CLOSE G_{\varepsilon}(r/(1-\min\{{1\over 2},{r\over 2}\}/i) for all ε ≥ 5 2 ​ r / i \varepsilon\geq{5\over 2}r/i. (as well as at all larger speed ratios). Because this holds for infinitely many i i, and 5 2 ​ r / i → 0 {5\over 2}r/i\to 0 and min ⁡ { 1 2, r 2 } / i → 0 \min\{{1\over 2},{r\over 2}\}/i\to 0 as i → ∞ i\to\infty, we obtain that the pursuer wins G ε ​ ( r + ε) G_{\varepsilon}(r+\varepsilon) for all ε > 0 \varepsilon>0. Thus the pursuer wins G ⁡ ( r + ε) G(r+\varepsilon) for all ε > 0 \varepsilon>0. ∎

###### Corollary 5.14.

Any (continuous) pursuit–escape instance ( D h, D z, X) (D_{h},D_{z},X) has a critical speed ratio r ∗ ≥ 0 r^{*}\geq 0 (possibility ∞ \infty) such that the escaper wins G ⁡ ( r) G(r) for all speed ratios r < r ∗ r<r^{*} and the pursuer wins G ⁡ ( r) G(r) for all speed ratios r > r ∗ r>r^{*}.

The critical speed ratio r ∗ r^{*} can be ∞ \infty. For example, consider a cusp ≺ \prec where the escaper domain is (locally) on the right and the pursuer domain is (locally) on the left. No matter what speed r r the pursuer has, a unit-speed escaper can get sufficiently close to the cusp vertex, threaten to leave on the top side, and then run to the bottom side and escape. Thus the escaper always wins in such examples.

###### Theorem 5.15 (pursuer wins at critical speed ratio).

For any region R R and speed r ∗ r^{*}, if for all r > r ∗ r>r^{*} the pursuer wins the game at speed ratio r r, then the pursuer wins at r ∗ r^{*}.

Equivalently, the interval of speeds for which the pursuer wins is closed.

Equivalently, if the critical speed ratio r ∗ r^{*} is finite, the pursuer wins at speed r ∗ r^{*}.

###### Proof.

For every ε > 0 \varepsilon>0, we will construct an ε 4 ​ ( r ∗ + 1) \frac{\varepsilon}{4(r^{*}+1)} -oblivious winning strategy for the pursuer in the game G ε G_{\varepsilon} with speed ratio r ∗ r^{*}. By Lemma 5.5, since the pursuer has a winning strategy in G ε 3 G_{\frac{\varepsilon}{3}} with speed ratio r r, for every r > r ∗ r>r^{*} and every ε > 0 \varepsilon>0, the pursuer has an ε 6 ​ r \frac{\varepsilon}{6r} -oblivious winning strategy Z r, ε Z_{r,\varepsilon} for G ε 2 G_{\frac{\varepsilon}{2}} with speed ratio r r. So for every r ∈ ( r ∗, r ∗ + 1] r\in(r^{*},r^{*}+1] and every ε > 0 \varepsilon>0, the pursuer has an ε 6 ​ ( r ∗ + 1) \frac{\varepsilon}{6(r^{*}+1)} -oblivious winning strategy Z r, ε Z_{r,\varepsilon} for G ε 2 G_{\frac{\varepsilon}{2}} with speed ratio r r. We will simulate those games for every r r in the sequence ⟨ r ∗ + 1 k ∣ k = 1, 2, … ⟩ \langle r^{*}+{1\over k}\mid k=1,2,\dots\rangle, and in all of them we will have the escaper move as it does in the G ε G_{\varepsilon} game. 11 11 11 Note that here we take advantage of the asymmetry between the definitions of escaper and pursuer wins: for the escaper to win, it needs only be the case that there exists one ε > 0 \varepsilon>0 for which the escaper wins, so a similar strategy of simulating infinitely many games would not be possible for the escaper. We will define a winning strategy Z ⁡ ( h) Z(h) in G ε G_{\varepsilon} for every escaper strategy h h.

Consider the set of starting locations { Z r, ε ​ ( h) ​ ( 0) } r \{Z_{r,\varepsilon}(h)(0)\}_{r} chosen by pursuers in those simulated games. There are infinitely many of them, and they all lie within a pursuer-metric disk of radius ε 2 + ( ( r ∗ + 1)) ⋅ d h ​ ( h ⁡ ( 0), X) \frac{\varepsilon}{2}+((r^{*}+1))\cdot d_{h}(h(0),X) (or else the escaper could win the simulated games by running directly to X X). So, by Lemma A.1, they have a limit point p 0 p_{0} in the pursuer metric; the pursuer chooses to start at p 0 p_{0}. We will continue the simulations only of those simulated games for which the pursuer starts within ε 4 \frac{\varepsilon}{4} of p 0 p_{0}, of which there are infinitely many since p 0 p_{0} was a limit point.

We prove by induction on k k that at time k ​ ε 12 ​ ( r ∗ + 1) k\frac{\varepsilon}{12(r^{*}+1)}, we can guarantee that the pursuer is at distance at most ε 2 ​ ( 1 − 2 − 1 − k) \frac{\varepsilon}{2}(1-2^{-1-k}) from the positions of the pursuers in infinitely many of the simulated games. This is true for k = 0 k=0, as above.

At time k ​ ε 12 ​ ( r ∗ + 1) k\frac{\varepsilon}{12(r^{*}+1)}, the pursuer decides its movement for the next ε 12 ​ ( r ∗ + 1) \frac{\varepsilon}{12(r^{*}+1)} time as follows: simulate each game until time ( k + 1) ​ ε 12 ​ ( r ∗ + 1) (k+1)\frac{\varepsilon}{12(r^{*}+1)}. The pursuers in the simulated games follow ε 6 ​ ( r ∗ + 1) \frac{\varepsilon}{6(r^{*}+1)} -oblivious strategies, so their strategies until that time depend on the position of the escaper no later than ( k + 1) ​ ε 12 ​ ( r ∗ + 1) − ε 6 ​ ( r ∗ + 1) = ( k − 1) ​ ε 12 ​ ( r ∗ + 1) (k+1)\frac{\varepsilon}{12(r^{*}+1)}-\frac{\varepsilon}{6(r^{*}+1)}=(k-1)\frac{\varepsilon}{12(r^{*}+1)}. At time k ​ ε 12 ​ ( r ∗ + 1) k\frac{\varepsilon}{12(r^{*}+1)}, the pursuer (for whom we are constructing an ε 12 ​ ( r ∗ + 1) \frac{\varepsilon}{12(r^{*}+1)} -oblivious strategy) knows that much of the escaper’s motion, so it can in fact simulate all those games.

Consider the set of positions at which pursuers in those simulated games are at time ( k + 1) ​ ε 12 ​ ( r ∗ + 1) (k+1)\frac{\varepsilon}{12(r^{*}+1)}. There are infinitely many of them, and they all lie within a disk of radius ε 2 ​ ( 1 − 2 − 1 − k) + ( r ∗ + 1) ​ ε 12 ​ ( r ∗ + 1) \frac{\varepsilon}{2}(1-2^{-1-k})+(r^{*}+1)\frac{\varepsilon}{12(r^{*}+1)} centered at p k p_{k}, so by Lemma A.1, they have a limit point p k + 1 p_{k+1}. All the simulated pursuers are within distance ε 2 ​ ( 1 − 2 − 1 − k) \frac{\varepsilon}{2}(1-2^{-1-k}) of the actual pursuer at time k ​ ε 12 ​ ( r ∗ + 1) k\frac{\varepsilon}{12(r^{*}+1)}, and for any δ > ε 12 ​ ( r ∗ + 1) ​ r ∗ \delta>\frac{\varepsilon}{12(r^{*}+1)}r^{*}, only finitely many of the simulated pursuers are fast enough to travel a distance greater than δ \delta, so p k + 1 p_{k+1} is within ε 12 ​ ( r ∗ + 1) ​ r ∗ + ε 2 ​ ( 1 − 2 − 1 − k) \frac{\varepsilon}{12(r^{*}+1)}r^{*}+\frac{\varepsilon}{2}(1-2^{-1-k}) of the pursuer’s position at time k ​ ε 12 ​ ( r ∗ + 1) k\frac{\varepsilon}{12(r^{*}+1)}. The pursuer chooses to move toward p k + 1 p_{k+1}, so by time ( k + 1) ​ ε 12 ​ ( r ∗ + 1) (k+1)\frac{\varepsilon}{12(r^{*}+1)}, the pursuer is within ε 2 ​ ( 1 − 2 − 1 − k) \frac{\varepsilon}{2}(1-2^{-1-k}) of p k + 1 p_{k+1}. Continue the simulations only of those games in which the simulated pursuer is within ε 2 ​ ( 2 − 2 − k) \frac{\varepsilon}{2}(2^{-2-k}) of the limit point, of which there are infinitely many since p k + 1 p_{k+1} was a limit point. By the triangle inequality, the pursuer’s distance from the pursuer in each of those games at time ( k + 1) ​ ε 12 ​ ( r ∗ + 1) (k+1)\frac{\varepsilon}{12(r^{*}+1)} is at most ε 2 ​ ( 1 − 2 − 1 − k) + ε 2 ​ ( 2 − 2 − k) = ε 2 ​ ( 1 − 2 − 2 − k) \frac{\varepsilon}{2}(1-2^{-1-k})+\frac{\varepsilon}{2}(2^{-2-k})=\frac{\varepsilon}{2}(1-2^{-2-k}), completing the induction.

Whenever the escaper is at an exit, the pursuers in the simulated games are within distance ε 2 \frac{\varepsilon}{2}, since they are following winning strategies for G ε 2 G_{\frac{\varepsilon}{2}}. The (unsimulated) pursuer is within ε 2 \frac{\varepsilon}{2} of those (simulated) pursuers, so by the triangle inequality it is within ε \varepsilon of the escaper, so the pursuer wins G ε G_{\varepsilon}, as claimed. ∎

\finalmodelresult

## 6 Pseudopolynomial-Time Approximation Scheme

In this section, we give a pseudopolynomial-time approximation scheme for approximating the critical speed ratio r ∗ r^{*} when the escaper domain is the interior and boundary of a simple polygon P P with integer coordinates, the pursuer domain is the boundary and optional exterior of P P, and the exit set X = ∂ P X=\partial P. More precisely, given D h D_{h}, D z D_{z}, and ε > 0 \varepsilon>0, the scheme approximates r ∗ r^{*} to within a factor of 1 + ε 1+\varepsilon in time polynomial in 1 / ε 1/\varepsilon and the polygon coordinates. Our main tool is the ( δ, γ) (\delta,\gamma) -discretized game defined and analyzed in Section 5.3. (In fact, we initially developed the discretization idea in the context of this pseudopolynomial-time approximation scheme, and later realized it could be useful to prove that the continuous game always has a winner.) We showed in Section 5.3 that the discrete game approximates the continuous game in some sense, but we need substantially more effort to turn this into an efficient approximation algorithm.

### 6.1 Restricting to Convex Hull

One challenge with applying the discretization tool is that the vertex set V V has infinitely many points whenever D h D_{h} or D z D_{z} is unbounded. Even in very natural models (e.g., the exterior model), D z D_{z} is typically unbounded. Luckily, we can focus our attention to the convex hull of all boundaries:

###### Lemma 6.1.

If a player in domain D D has a winning strategy that leaves the convex hull of ∂ D \partial D, then they have a winning strategy that does not.

###### Proof.

Let C C be the convex hull of ∂ D \partial D (i.e., its interior and boundary), and let A A be a player winning strategy for G ε G_{\varepsilon}. For any opponent motion path b b and time t t, define A ^ ​ ( b) ​ ( t) \hat{A}(b)(t) to be the nearest point ∈ C \in C to A ​ ( b) ​ ( t) A(b)(t). Because this modification is a contraction, A ^ \hat{A} will still satisfy the speed-limit constraint. Because the modification is independent of b b, A ^ \hat{A} will still satisfy the nonbranching-lookahead constraint and (for the escaper player) the escaper-start constraint. Because A A won against every opponent strategy b b, so will A ^ \hat{A}. ∎

### 6.2 Margin of Victory

Another challenge with applying the discretization tool is that, while Theorem 5.11 relates discrete winning strategies to continuous winning strategies, it does so only for G ε G_{\varepsilon} for some ε > 0 \varepsilon>0. But we want an algorithm to compute the critical speed ratio for G G, not some G ε G_{\varepsilon}. To resolve this discrepancy, we develop a tool for trading off the pursuer winning distance ε \varepsilon with the speed ratio.

First we need a simpler lemma:

###### Lemma 6.2.

If the escaper has a winning strategy for G ε G_{\varepsilon}, then the escaper has a winning strategy for G ε / ( 2 ​ r + 3) G_{\varepsilon/(2r+3)} satisfying that the last ε / ( 2 ​ r + 3) \varepsilon/(2r+3) time of their motion (in response to any pursuer motion path) is along a shortest path.

If the escaper domain D h D_{h} is a polygon (interior and boundary) and X = ∂ D h X=\partial D_{h}, then the escaper can further restrict to a straight-line motion for the last ε / ( 2 ​ r + 3) \varepsilon/(2r+3) time of their motion.

###### Proof.

Suppose the escaper has a winning strategy H H for G ε G_{\varepsilon}, i.e., for any pursuer motion path z z, there is a time t z t_{z} such that H ​ ( z) ​ ( t z) H(z)(t_{z}) is an exit x z x_{z} and d z ​ ( H ⁡ ( z) ​ ( t z), z ⁡ ( t z)) ≥ ε d_{z}(H(z)(t_{z}),z(t_{z}))\geq\varepsilon. Define an escaper–pursuer distance by

 | d h ​ z ​ ( p h, p z) = min x ∈ X ⁡ d h ​ ( p h, x) + d z ​ ( p z, x). d_{hz}(p_{h},p_{z})=\min_{x\in X}d_{h}(p_{h},x)+d_{z}(p_{z},x). |  |

At any time t ≥ t z − ε ​ 1 2 ​ r + 3 t\geq t_{z}-\varepsilon\frac{1}{2r+3}, d h ​ ( H ⁡ ( z) ​ ( t), x z) ≤ ε ​ 1 2 ​ r + 3 d_{h}(H(z)(t),x_{z})\leq\varepsilon\frac{1}{2r+3} (by the escaper speed-limit constraint) and d h ​ z ​ ( H ⁡ ( z) ​ ( t), z ⁡ ( t)) ≥ ε ​ r + 2 2 ​ r + 3 d_{hz}(H(z)(t),z(t))\geq\varepsilon\frac{r+2}{2r+3} (because in time ≤ ε ​ 1 2 ​ r + 3 \leq\varepsilon\frac{1}{2r+3}, the pursuer and escaper travel a total distance of ≤ ε ​ r + 1 2 ​ r + 3 \leq\varepsilon\frac{r+1}{2r+3}, so d h ​ z ​ ( H ⁡ ( z) ​ ( t), z ⁡ ( t)) d_{hz}(H(z)(t),z(t)) can change by at most that much, yet it reaches at least ε ​ 2 ​ r + 3 2 ​ r + 3 \varepsilon\frac{2r+3}{2r+3} at the end). Thus, if we replace H ⁡ ( z) ​ ( [t z − ε ​ 1 2 ​ r + 3, t z]) H(z)([t_{z}-\varepsilon\frac{1}{2r+3},t_{z}]) with the escaper moving along a shortest path to x z x_{z}, then d h ​ z ​ ( H ⁡ ( z) ​ ( t), z ⁡ ( t)) d_{hz}(H(z)(t),z(t)) can decrease by ≤ ε ​ r + 1 2 ​ r + 3 \leq\varepsilon\frac{r+1}{2r+3} over that time from its initial value of ≥ ε ​ r + 2 2 ​ r + 3 \geq\varepsilon\frac{r+2}{2r+3}, leaving a distance of ≥ ε ​ 1 2 ​ r + 3 \geq\varepsilon\frac{1}{2r+3}. Thus we obtain an escaper winning strategy for G ε / ( 2 ​ r + 3) G_{\varepsilon/(2r+3)}.

If shortest paths in d h d_{h} are polygonal with vertices only at points of X X, as when D h D_{h} is a polygon and X = ∂ D h X=\partial D_{h}, then we can stop the shortest-path motion whenever it hits a point of X X and thereby guarantee a straight-line motion (which can be spread out over the final ε ​ 1 2 ​ r + 3 \varepsilon\frac{1}{2r+3} time interval). By the same argument, this strategy will still win. ∎

###### Lemma 6.3.

Suppose P P is a simple polygon and ε > 0 \varepsilon>0 satisfies

1. 1.

there is a point in P P at distance more than ε \varepsilon from the nearest boundary;

2. 2.

no disk of radius 2 ​ ε 2\sqrt{\varepsilon} intersects two edges not sharing a vertex; and

3. 3.

ε < 1 / ( 2 ​ ( r ∗) 2) \varepsilon<1/(2(r^{*})^{2}) where r ∗ r^{*} is the critical speed ratio for the game with escaper domain D h = P D_{h}=P, exit set X = ∂ P X=\partial P, and pursuer domain D z D_{z} either ∂ P \partial P or ℝ 2 − P ¯ \overline{\mathbb{R}^{2}-P}.

If the escaper wins the continuous game G G in a polygon P P (with D h D_{h}, X X, and D z D_{z} as above) at a speed ratio r r, then the escaper wins the game G ε 3 G_{\varepsilon^{3}} at speed ratio r / ( 1 + ε) r/(1+\varepsilon).

While it is easy to prove that such an ε \varepsilon*exists*via Lemma 5.5, the point is that we can efficiently compute a valid such ε \varepsilon. Specifically, we can compute an ε 0 \varepsilon_{0} such that all ε ∈ ( 0, ε 0] \varepsilon\in(0,\varepsilon_{0}] satisfy the three conditions of Lemma 6.3 by taking the minimum of the following three lower bounds:

1. 1.

We can compute a lower bound on Condition 1 by triangulating P P, choosing any of that triangulation’s triangles, and using the inradius of that triangle. The inradius is the area divided by half the perimeter, and both of those are polynomial functions of the input coordinates, so this bound on ε 0 \varepsilon_{0} is polynomial in the coordinates of P P.

2. 2.

We can compute a lower bound on Condition 2: the minimum distance between two edges not sharing a vertex is attained either by a pair of vertices (and we can compute the minimum distance between pairs of vertices) or by the perpendicular from a vertex v v to an edge ( u, w) (u,w). The length of that perpendicular is the area of the triangle with vertices u u, v v, and w w divided by the distance from u u to w w, and those are both polynomial in u u, v v, and w w, so this bound on ε 0 \varepsilon_{0} has length (in bits) polynomial in the length (in bits) of P P.

3. 3.

We can compute a lower bound on Condition 3 via an upper bound on r ∗ r^{*} depending only on P P: by Theorem 3.2, r ∗ ≤ 10.89898 ​ max p, q ∈ ∂ P ​ d z ​ ( p, q) d h ​ ( p, q) r^{*}\leq 10.89898\max_{p,q\in\partial P}\frac{d_{z}(p,q)}{d_{h}(p,q)}. Instead of computing d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,q)}{d_{h}(p,q)} directly, we can easily upper-bound it by the maximum of two easy-to-compute quantities:

  1. (a)

F / f F/f where F F is the perimeter of ∂ D h \partial D_{h} and f f is minimum distance between two nonincident edges (minimum feature size). This is an upper bound on d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,q)}{d_{h}(p,q)} for p, q p,q on any two nonincident edges.

  2. (b)

csc ⁡ θ min 2 \csc{\theta_{\min}\over 2} where θ min \theta_{\min} is the smallest interior angle of a vertex of D h D_{h}. This is an upper bound on d z ​ ( p, q) d h ​ ( p, q) \frac{d_{z}(p,q)}{d_{h}(p,q)} for p, q p,q along two edges sharing an endpoint. (When p p and q q are on the same edge, we get a ratio of 1 1, so we do not need to consider this case.)

###### Proof of Lemma 6.3.

The escaper should start at some point H H at distance more than ε \varepsilon from the nearest boundary (escaper-start constraint); ε 0 \varepsilon_{0} was chosen small enough that such a place exists. The escaper can still win G G: if they could win by some other starting position, the escaper can immediately run to that position; wherever the pursuer is after that run, the pursuer could have started there, so the escaper can simulate their winning strategy from that starting position to win.

If, from that starting position, there is a point T T on the boundary such that the escaper can win G G with speed ratio r r by committing to running straight to T T (that is, if there is a point T ∈ ∂ P T\in\partial P such that r ⋅ d h ​ ( H, T) < d z ​ ( Z, T) r\cdot d_{h}(H,T)<d_{z}(Z,T), where Z Z is the pursuer’s starting position), then the escaper can win G ε 3 G_{\varepsilon^{3}} with speed ratio r ​ 1 1 + ε r\frac{1}{1+\varepsilon} by running straight to that point. The escaper’s time to get there is d h ​ ( H, T) d_{h}(H,T), in which time the pursuer moves at most r ​ 1 1 + ε ⋅ d h ​ ( H, T) < 1 1 + ε ⋅ d z ​ ( Z, T) r\frac{1}{1+\varepsilon}\cdot d_{h}(H,T)<\frac{1}{1+\varepsilon}\cdot d_{z}(Z,T), leaving a distance of at least ε 1 + ε ⋅ d z ​ ( Z, T) > ε 2 ​ r ⋅ d h ​ ( H, T) > ε 2 2 ​ r > ε 3 \frac{\varepsilon}{1+\varepsilon}\cdot d_{z}(Z,T)>\frac{\varepsilon}{2r}\cdot d_{h}(H,T)>\frac{\varepsilon^{2}}{2r}>\varepsilon^{3}, as desired.

Otherwise, the escaper cannot immediately win G G with speed ratio r r by picking a point on ∂ P \partial P within ε \varepsilon of their location and running straight to it. However, the escaper can eventually win G G by using the strategy in Lemma 6.2. Consider the escaper’s position H H and pursuer’s position Z Z at a time t t such that for all later times, the escaper can win by picking a point on δ ​ P \delta P and running along a shortest path to it, and for all earlier times, the escaper cannot so win.

Let W = { W 1, W 2, … } W=\{W_{1},W_{2},\ldots\} be the set of points on ∂ P \partial P that the escaper can reach in the same time as the pursuer if both of them run on a shortest path.

If there is any point in W W at distance more than ε \varepsilon from h h, then by the same calculation as above, the escaper can win G ε 3 G_{\varepsilon^{3}} at speed ratio r ​ 1 1 + ε r\frac{1}{1+\varepsilon} by running straight to it. Otherwise, every such boundary point is within ε \varepsilon of h h. By the choice of ε \varepsilon, there are at most two edges within ε \varepsilon of h h, and if there are two such edges, they share a vertex, so all points in W W are on one or two adjacent edges.

When the escaper is at h h and the pursuer at z z, for every point x x on the boundary, the time it would take the pursuer to reach x x is at most the time it would take the escaper to reach x x. Suppose not, and suppose that the escaper’s shortest path to x x has length ℓ \ell and the pursuer’s shortest path to x x has length ℓ + r ​ ε x \ell+r\varepsilon_{x}. Then at time t − ε x 2 ​ r + 3 t-\frac{\varepsilon_{x}}{2r+3}, the length of the escaper’s shortest path to x x is at most ℓ + ε x 2 ​ r + 3 \ell+\frac{\varepsilon_{x}}{2r+3} and the length of the pursuer’s shortest path to x x is at least ℓ + r ​ ε x − r ​ ε x 2 ​ r + 3 > ℓ + ε x 2 ​ r + 3 + ε x 2 \ell+r\varepsilon_{x}-\frac{r\varepsilon_{x}}{2r+3}>\ell+\frac{\varepsilon_{x}}{2r+3}+\frac{\varepsilon_{x}}{2}, so at time t − ε x 2 ​ r + 3 t-\frac{\varepsilon_{x}}{2r+3}, the escaper can win G ε ′ G_{\varepsilon^{\prime}} for all ε ′ < ε x 2 \varepsilon^{\prime}<\frac{\varepsilon_{x}}{2} by picking the point x x and running along a shortest path to it. Hence the escaper wins G G by the same strategy, which contradicts the choice of t t.

If W W is empty, then consider, for each point on ∂ P \partial P, the time it takes the escaper to reach that point minus the time it takes the pursuer to reach that point. That’s function is always nonnegative, is nowhere 0 by assumption, and is a continuous function of a parameterization of the boundary, which is closed and bounded. Therefore, it attains a minimum ε x \varepsilon_{x}. At time t + ε x 2 ​ r + 3 t+\frac{\varepsilon_{x}}{2r+3}, that function is still everywhere at least ε x 2 \frac{\varepsilon_{x}}{2}, by the same calculation as above. So even at time t + ε x 2 ​ r + 3 t+\frac{\varepsilon_{x}}{2r+3}, there’s no point on the boundary such that the escaper can win G ε ′ G_{\varepsilon^{\prime}} for any ε ′ < ε x 2 \varepsilon^{\prime}<\frac{\varepsilon_{x}}{2} by running on a shortest path to it. So at time t + ε x 2 ​ r + 3 t+\frac{\varepsilon_{x}}{2r+3}, there’s no point on the boundary such that the escaper can win G G by running on a shortest path to it, contradicting the choice of t t.

If there are two points of W W on the same edge, let that edge be the x x -axis. The escaper’s shortest-path time to a point ( x, 0) (x,0) is a function of the form f ⁡ ( x) = x 2 + a ​ x + b f(x)=\sqrt{x^{2}+ax+b} for some a a and b b, and the pursuer’s shortest-path time is g ⁡ ( x) = x 2 + c ​ x + d / r g(x)=\sqrt{x^{2}+cx+d}/r. Since r > 1 r>1, if those two functions are equal at two points, then there’s some point such that the escaper’s shortest-path time to it is strictly less than the pursuer’s, say by ε x \varepsilon_{x}. At time t − ε x 2 ​ r + 3 t-\frac{\varepsilon_{x}}{2r+3}, that difference is still at least ε x 2 \frac{\varepsilon_{x}}{2}, by the same calculation as above. So even at time t − ε x 2 ​ r + 3 t-\frac{\varepsilon_{x}}{2r+3}, the escaper can win G G, contradicting the choice of t t.

Now, suppose that there’s at most one point of W W per edge, and W W is nonempty. We claim that the escaper cannot win at all with at most ε \varepsilon more movement, much less by committing to moving straight to one of those boundary points.

First, if there are points of W W on only one edge e e, the pursuer can use an APLO strategy until there’s a point of W W on another edge: the pursuer can match the escaper’s speed perpendicular to H ​ Z HZ and, conditioned on that, use as much of its speed as possible to move toward e e in the direction of H ​ Z HZ. If it’s the case that, for every direction θ \theta that the escaper runs, the escaper’s distance to e e decreases at most d ⁡ ( H, e) d ⁡ ( Z, e) \frac{d(H,e)}{d(Z,e)} times faster than the pursuer’s distance to e e does; then the pursuer reaches the boundary first and wins by Theorem 4.1. Otherwise, there’s some direction θ \theta such that the escaper’s distance to e e decreases more than d ⁡ ( H, e) d ⁡ ( Z, e) \frac{d(H,e)}{d(Z,e)} times faster than the pursuer’s distance to e e does. So, if the escaper runs straight in the direction θ \theta toward a point W 3 W_{3} on e e, the escaper reaches W 3 W_{3} before the pursuer reaches e e (since if the pursuer reaches e e, it wins by Theorem 4.1) following this strategy. But if the pursuer runs straight toward W 3 W_{3}, it gets there first by assumption; so if the pursuer runs straight toward W 3 W_{3} but slows down enough to keep the line between it and the escaper parallel to H ​ Z HZ, it still wins. If the pursuer does that, but uses any extra movement to move toward the boundary, that brings it strictly closer to W 3 W_{3}, so it still wins. But that’s exactly the pursuer strategy for which we claimed that the pursuer would lose, contradiction. So there are points of W W on at least two edges within ε \varepsilon of H H.

So, there are two edges e e and f f (there cannot be more, by the definition of ε \varepsilon) with one point of W W, within ε \varepsilon of H H, on each. To deal with this case, we prove three lemmas about the geometry of the situation.

###### Lemma 6.4.

The angle between the escaper’s shortest paths to the points in W W is at least the angle between the pursuer’s shortest paths to the points in W W, with equality only if both angles are π \pi.

###### Proof.

Let the points of W W be W 1 = ( x, y) W_{1}=(x,y) on edge e e and W 2 W_{2} on edge f f and the x x axis, which meet at P = ( 0, t) P=(0,t) with t > 0 t>0. The escaper and pursuer are on opposite sides of at least one of the supporting lines of e e and f f. We divide into two cases: either they are on opposite sides of both, or they are on opposite sides of just one.

If the escaper and pursuer are on opposite sides of both supporting lines of e e and f f, as in Figure 16, then Z ​ W 1 > H ​ W 1 ZW_{1}>HW_{1} because Z ​ W 1 ZW_{1} and H ​ W 1 HW_{1} are the shortest paths for the pursuer and escaper, respectively, to W 1 W_{1}, both players reach W 1 W_{1} in the same time, and the pursuer is faster, so the pursuer’s path is longer. Therefore, ∠ ​ W 1 ​ Z ​ H < ∠ ​ W 1 ​ H ​ Z \angle W_{1}ZH<\angle W_{1}HZ. Similarly, ∠ ​ W 2 ​ Z ​ H < ∠ ​ W 2 ​ H ​ Z \angle W_{2}ZH<\angle W_{2}HZ, so ∠ ​ W 1 ​ Z ​ W 2 < ∠ ​ W 1 ​ H ​ W 2 \angle W_{1}ZW_{2}<\angle W_{1}HW_{2}, as desired.

Figure 16: Coordinates and variables used in the easy case of the proof of Lemma 6.4.

If the escaper and pursuer are on opposite sides of just one of the edges e e and f f, then, without loss of generality, let them be on opposite sides of the supporting line of f f. Let the escaper’s shortest path to W 2 W_{2} be horizontal, let the pursuer’s position be Z = ( z, ζ) Z=(z,\zeta), and let the escaper’s position be H = ( h, 0) H=(h,0), so O = ( 0, 0) O=(0,0) is the foot of the perpendicular from P P to the escaper’s shortest path to W 2 W_{2}, as in Figure 17.

Figure 17: Coordinates and variables used in the hard case of the proof of Lemma 6.4.

#### Ramchundra’s intercept problem.

We first show that, when the pursuer is at P P, the escaper’s shortest-path time to some point on f f equals the pursuer’s shortest-path time if and only if the escaper is on P ​ O PO. (This is the “perpendicular to first sighting” rule for naval pursuit, also known as “Ramchundra’s intercept problem” [Nah07, Section 1.5].) When the escaper and pursuer both run by their shortest paths to W 2 W_{2}, and the pursuer is at P P, let the escaper be at a point O ′ O^{\prime}, and let W ′ W^{\prime} be any point on f f. By the law of sines, O ′ ​ W ′ ¯ P ​ W ′ ¯ = sin ⁡ ( ∠ ​ O ′ ​ P ​ W ′) sin ⁡ ( ∠ ​ P ​ O ′ ​ W ′) \frac{\overline{O^{\prime}W^{\prime}}}{\overline{PW^{\prime}}}=\frac{\sin(\angle O^{\prime}PW^{\prime})}{\sin(\angle PO^{\prime}W^{\prime})}, and ∠ ​ O ′ ​ P ​ W ′ \angle O^{\prime}PW^{\prime} is fixed, so O ′ ​ W ′ ¯ P ​ W ′ ¯ \frac{\overline{O^{\prime}W^{\prime}}}{\overline{PW^{\prime}}} is maximized over choices of W ′ W^{\prime} when ∠ ​ P ​ O ′ ​ W ′ = π 2 \angle PO^{\prime}W^{\prime}=\frac{\pi}{2}. But if O ′ O^{\prime} is the point where the escaper is when the pursuer’s at P P as both follow their shortest paths to W 2 W_{2}, then, by the choice of coordinate system, the escaper can tie only by running horizontally to W 2 W_{2}, so W ′ = W 2 W^{\prime}=W_{2} and O ′ O^{\prime} is the point on the escaper’s shortest path with P ​ O ′ ​ W 2 = π 2 PO^{\prime}W_{2}=\frac{\pi}{2}, that is, O ′ = O O^{\prime}=O.

By the perpendicular to first sighting rule, if the escaper can escape, they can escape by running perpendicular to the direction to the pursuer. So, when the pursuer is at P P, the escaper must be at the foot of the perpendicular from P P to the escaper path, that is, at O O, and that’s after the escaper has traveled a distance of H ​ O HO and the pursuer has traveled a distance of Z ​ P ZP, so Z ​ P ¯ H ​ O ¯ = r \frac{\overline{ZP}}{\overline{HO}}=r.

#### Tied time to W 1 W_{1}, in coordinates.

Writing ( Z ​ W 1 ¯) 2 = ( r ​ H ​ W 1 ¯) 2 (\overline{ZW_{1}})^{2}=(r\overline{HW_{1}})^{2} out in coordinates,

 | ( z − x) 2 + ( ζ − y) 2 = r 2 ​ [( x − h) 2 + y 2]. (z-x)^{2}+(\zeta-y)^{2}=r^{2}[(x-h)^{2}+y^{2}]. |  |

Consider the function from a point p p on e e to the difference between the escaper’s shortest-path time to p p and the pursuer’s shortest-path time to p p. At W 1 W_{1}, that difference is 0 0, and near W W, it’s nonnegative, so the derivative is 0 0 at W 1 W_{1}. In coordinates, the difference at a point near W 1 W_{1} is

 | ( z − x − x ​ d ​ ℓ) 2 + ( ζ − y − ( y − t) ​ d ​ ℓ) 2 = r 2 ​ [( x + x ​ d ​ ℓ − h) 2 + ( y + ( y − t) ​ d ​ ℓ) 2], (z-x-xd\ell)^{2}+(\zeta-y-(y-t)d\ell)^{2}=r^{2}[(x+xd\ell-h)^{2}+(y+(y-t)d\ell)^{2}], |  |

so the derivative gives us

 | ( z − x) ​ x + ( ζ − y) ​ ( y − t) = r 2 ​ [( h − x) ​ x + ( t − y) ​ ( y)]. (z-x)x+(\zeta-y)(y-t)=r^{2}[(h-x)x+(t-y)(y)]. |  |

Adding the equation ( Z ​ W 1 ¯) 2 = ( r ​ H ​ W 1 ¯) 2 (\overline{ZW_{1}})^{2}=(r\overline{HW_{1}})^{2} gives

 | ( z − x) ​ z + ( ζ − y) ​ ( ζ − t) = r 2 ​ [( h − x) ​ h + t ​ y], (z-x)z+(\zeta-y)(\zeta-t)=r^{2}[(h-x)h+ty], |  |

an equation that will be useful in two cases:

If y = 0 y=0, then the angle between the escaper’s shortest paths is π \pi, so the conclusion of Lemma 6.4 is satisfied.

If y > 0 y>0, then y ​ t > 0 yt>0, so h ⁡ ( h − x) < h ⁡ ( h − x) + y ​ t h(h-x)<h(h-x)+yt, so

 | h ⁡ ( h − x) H ​ W 1 ¯ ​ H ​ O ¯ < h ⁡ ( h − x) + y ​ t H ​ W 1 ¯ ​ H ​ O ¯. \frac{h(h-x)}{\overline{HW_{1}}\overline{HO}}<\frac{h(h-x)+yt}{\overline{HW_{1}}\overline{HO}}. |  |

By Ramchundra’s intercept problem, Z ​ P ¯ H ​ O ¯ = r \frac{\overline{ZP}}{\overline{HO}}=r, and by the definition of W W, Z ​ W 1 ¯ H ​ W 1 ¯ = r \frac{\overline{ZW_{1}}}{\overline{HW_{1}}}=r, so

 | h ⁡ ( h − x) H ​ W ¯ ​ H ​ O ¯ < r 2 ​ ( h ⁡ ( h − x) + y ​ t) Z ​ W 1 ¯ ​ Z ​ P ¯. \frac{h(h-x)}{\overline{HW}\overline{HO}}<\frac{r^{2}(h(h-x)+yt)}{\overline{ZW_{1}}\overline{ZP}}. |  |

By the tied time to W 1 W_{1} in coordinates, that’s

 | h ⁡ ( h − x) H ​ W 1 ¯ ​ H ​ O ¯ < ( z − x) ​ z + ( ζ − y) ​ ( ζ − t) Z ​ W 1 ¯ ​ Z ​ P ¯. \frac{h(h-x)}{\overline{HW_{1}}\overline{HO}}<\frac{(z-x)z+(\zeta-y)(\zeta-t)}{\overline{ZW_{1}}\overline{ZP}}. |  |

Each of those numerators is a dot product:

 | H ​ W 1 ⋅ H ​ O H ​ W 1 ¯ ​ H ​ O ¯ < Z ​ W 1 ⋅ Z ​ P Z ​ W 1 ¯ ​ Z ​ P ¯. \frac{HW_{1}\cdot HO}{\overline{HW_{1}}\overline{HO}}<\frac{ZW_{1}\cdot ZP}{\overline{ZW_{1}}\overline{ZP}}. |  |

That is, cos ⁡ ( ∠ ​ O ​ H ​ W 1) < cos ⁡ ( ∠ ​ W 1 ​ Z ​ P) \cos(\angle OHW_{1})<\cos(\angle W_{1}ZP), so ∠ ​ O ​ H ​ W 1 > ∠ ​ W 1 ​ Z ​ P \angle OHW_{1}>\angle W_{1}ZP, as claimed.

If y < 0 y<0, we again have, by the tied time to W 1 W_{1} in coordinates, that

 | ( z − x) ​ z + ( ζ − y) ​ ( ζ − t) = r 2 ​ [( h − x) ​ h + t ​ y]. (z-x)z+(\zeta-y)(\zeta-t)=r^{2}[(h-x)h+ty]. |  |

By the Cauchy-Schwarz inequality,

 | ( ( z − x) ​ z + ( ζ − y) ​ ( ζ − t)) 2 ≤ [( z − x) 2 + ( ζ − y) 2] ​ [z 2 + ( ζ − t) 2] = Z ​ W 1 ¯ 2 ​ Z ​ P ¯ 2. ((z-x)z+(\zeta-y)(\zeta-t))^{2}\leq[(z-x)^{2}+(\zeta-y)^{2}][z^{2}+(\zeta-t)^{2}]=\overline{ZW_{1}}^{2}\overline{ZP}^{2}. |  |

By Ramchundra’s intercept problem and the fact that Z ​ W 1 ¯ H ​ W 1 ¯ = r \frac{\overline{ZW_{1}}}{\overline{HW_{1}}}=r, that’s

 | r 4 ​ [( h − x) ​ h + t ​ y] 2 ≤ r 4 ​ h 2 ​ [( x − h) 2 + y 2], r^{4}[(h-x)h+ty]^{2}\leq r^{4}h^{2}[(x-h)^{2}+y^{2}], |  |

so

 | h 2 ​ y 2 ≥ 2 ​ ( h − x) ​ h ​ t ​ y + t 2 ​ y 2 ≥ 2 ​ ( h − x) ​ h ​ t ​ y. h^{2}y^{2}\geq 2(h-x)hty+t^{2}y^{2}\geq 2(h-x)hty. |  |

Since h > 0 h>0 and y < 0 y<0, h ​ y ≤ 2 ​ ( h − x) ​ t hy\leq 2(h-x)t. But ( h, 0) (h,0) is on the escaper side of edge e e, so h ​ y > ( h − x) ​ t hy>(h-x)t, contradiction.

Therefore, in every surviving case, the conclusion of Lemma 6.4 is satisfied. ∎

We know that, if the escaper moves straight toward a point W 1 W_{1}, there exists a pursuer strategy (a direction of pursuer movement) such that the pursuer does not fall behind in the race toward W 1 W_{1}. We now prove that that strategy is stable: if the escaper moves at an angle of θ \theta from W 1 W_{1}, and the pursuer moves at an angle less than θ \theta from its shortest path to W 1 W_{1}, then for a positive time, the invariant that the pursuer’s distance to *every*point on the edge containing W 1 W_{1} remains at most r r times the escaper’s distance.

###### Lemma 6.5.

Suppose the escaper and pursuer are on the same side of (the supporting line of) an edge f f containing a point W 2 W_{2} such that the the pursuer’s shortest path to W 2 W_{2} is r r times longer than the escaper’s shortest path to W 2 W_{2}. If the escaper moves a short distance d ​ t dt at an angle of θ \theta from its shortest path to W 2 W_{2}, and the pursuer moves a short distance r ​ d ​ t rdt at an angle at most θ \theta from its shortest path to W 2 W_{2}, then, for every point on f f, the pursuer’s shortest-path time to it remains at most the escaper’s shortest-path time to it.

###### Proof.

Let the end of f f to which the pursuer runs be ( 0, 0) (0,0); let the perpendicular ℓ \ell from ( 0, 0) (0,0) to the escaper’s shortest path be at an angle θ ℓ \theta_{\ell} (so points ( x, y) (x,y) on it have x sin θ ℓ − y cos θ ℓ = 0 x\sin\theta_{\ell}-y\cos\theta_{\ell}=0), let the pursuer’s position be ( a, b) (a,b), and let the escaper’s position be ( c, d) (c,d), all as in Figure 18. Then the escaper’s distance to ℓ \ell is c sin θ ℓ − d cos θ ℓ c\sin\theta_{\ell}-d\cos\theta_{\ell} and the pursuer’s distance to ( 0, 0) (0,0) is a 2 + b 2 \sqrt{a^{2}+b^{2}}. By Ramchundra’s intercept problem, if the escaper is on ℓ \ell at the same time as the pursuer reaches ( 0, 0) (0,0), the escaper cannot win a race to anywhere on f f. So, the pursuer’s distance to ( 0, 0) (0,0) is currently r r times the escaper’s distance to ℓ \ell, and it suffices for the pursuer to maintain that invariant.

Figure 18: Coordinates and variables used in the proof of Lemma 6.5.

Suppose the escaper moves in a direction θ ∂ H \theta_{\partial H}; that is, ( ∂ c, ∂ d) = ( cos ⁡ θ ∂ H, sin ⁡ θ ∂ H) (\partial c,\partial d)=(\cos\theta_{\partial H},\sin\theta_{\partial H}). (If the escaper moves at less than full speed, the pursuer can reduce its speed proportionally.) The direction directly toward ℓ \ell is ℓ + π 2 \ell+\frac{\pi}{2}, so the escaper’s angle from that direction is | π 2 + θ ℓ − θ ∂ H | |\frac{\pi}{2}+\theta_{\ell}-\theta_{\partial H}|. If the pursuer’s angle from ( 0, 0) (0,0) is θ Z \theta_{Z} (so ( a, b) = ( a 2 + b 2 cos θ Z, a 2 + b 2 sin θ Z) (a,b)=(\sqrt{a^{2}+b^{2}}\cos\theta_{Z},\sqrt{a^{2}+b^{2}}\sin\theta_{Z}) and the pursuer’s direction toward ( 0, 0) (0,0) is π + θ Z \pi+\theta_{Z}), we will have the pursuer move in any direction θ ∂ Z \theta_{\partial Z} (that is, ( ∂ a, ∂ b) = ( r cos θ ∂ Z, r sin θ ∂ Z) (\partial a,\partial b)=(r\cos\theta_{\partial Z},r\sin\theta_{\partial Z})) such that | θ ∂ Z − ( π + θ Z) | ≤ | π 2 + θ ℓ − θ ∂ H | |\theta_{\partial Z}-(\pi+\theta_{Z})|\leq|\frac{\pi}{2}+\theta_{\ell}-\theta_{\partial H}|. Then cos ⁡ ( π + θ Z − θ ∂ Z) ≥ cos ⁡ ( π 2 + θ ℓ − θ ∂ H) \cos(\pi+\theta_{Z}-\theta_{\partial Z})\geq\cos(\frac{\pi}{2}+\theta_{\ell}-\theta_{\partial H}), so cos θ Z cos θ ∂ Z + sin θ Z sin θ ∂ Z ≤ cos θ ∂ H sin θ ℓ − sin θ ∂ H cos θ ℓ \cos\theta_{Z}\cos\theta_{\partial Z}+\sin\theta_{Z}\sin\theta_{\partial Z}\leq\cos\theta_{\partial H}\sin\theta_{\ell}-\sin\theta_{\partial H}\cos\theta_{\ell}, or a ​ ∂ a + b ​ ∂ b ≤ r ​ a 2 + b 2 ​ ( sin ⁡ θ ℓ ​ ∂ c − cos ⁡ θ ℓ ​ ∂ d) a\partial a+b\partial b\leq r\sqrt{a^{2}+b^{2}}(\sin\theta_{\ell}\partial c-\cos\theta_{\ell}\partial d). The escaper’s distance to ℓ \ell is c sin θ ℓ − d cos θ ℓ c\sin\theta_{\ell}-d\cos\theta_{\ell} and the pursuer’s squared distance to ( 0, 0) (0,0) is a 2 + b 2 \sqrt{a^{2}+b^{2}}, so ( c sin θ ℓ − d cos θ ℓ) r = a 2 + b 2 (c\sin\theta_{\ell}-d\cos\theta_{\ell})r=\sqrt{a^{2}+b^{2}}, and a ∂ a + b ∂ b ≤ r 2 ( c sin θ ℓ − d cos θ ℓ) ( sin θ ℓ ∂ c − cos θ ℓ ∂ d) a\partial a+b\partial b\leq r^{2}(c\sin\theta_{\ell}-d\cos\theta_{\ell})(\sin\theta_{\ell}\partial c-\cos\theta_{\ell}\partial d). The left side is the derivative of the pursuer’s squared distance to ( 0, 0) (0,0) and the right side is r 2 r^{2} times the derivative of the escaper’s squared distance to ℓ \ell, so the pursuer’s shortest-path time to ( 0, 0) (0,0) decreases at least as fast as the escaper’s shortest-path time to ℓ \ell, as desired. ∎

###### Lemma 6.6.

Suppose the escaper and pursuer are on opposite sides of (the extensions of) an edge e e containing a point W 1 W_{1} such that the the pursuer’s shortest path to W 1 W_{1} is r r times longer than the escaper’s shortest path to W 1 W_{1}. If the escaper moves a short distance d ​ t dt at an angle of θ \theta from its shortest path to W 1 W_{1}, and the pursuer moves a short distance r ​ d ​ t rdt at an angle at most θ \theta from its shortest path to W 1 W_{1}, then, for every point on e e, the pursuer’s shortest-path time to it remains at most the escaper’s shortest-path time to it.

###### Proof.

Let edge e e be the x x -axis, let the pursuer’s position be ( a, b) (a,b), and let the escaper’s position be ( c, d) (c,d), as in Figure 19. Also, place the origin such that a = r 2 ​ c a=r^{2}c (which may be a translation from the coordinates used in the proof of the previous lemma); this is possible since r 2 ≠ 1 r^{2}\neq 1.

Figure 19: Coordinates and variables used in the proof of Lemma 6.6.

We first claim that the pursuer’s shortest-path distance to every point on e e is at most r r times the escaper’s shortest-path distance if and only if r 2 ​ d − b ≥ r ​ ( a − c) 2 + ( b − d) 2 r^{2}d-b\geq r\sqrt{(a-c)^{2}+(b-d)^{2}}, with equality if and only if there’s a point on e e for which the pursuer’s shortest-path distance equals r r times the escaper’s shortest-path distance. Indeed, a point ( x, y) (x,y) has the pursuer’s plane distance more than r r times the escaper’s plane distance if and only if ( x − a) 2 + ( y − b) 2 ≥ r 2 ​ [( x − c) 2 + ( y − d) 2] (x-a)^{2}+(y-b)^{2}\geq r^{2}\left[(x-c)^{2}+(y-d)^{2}\right], or ( x − r 2 ​ c − a r 2 − 1) 2 + ( y − r 2 ​ d − b r 2 − 1) 2 ≤ r 2 ( r 2 − 1) 2 ​ ( ( c − a) 2 + ( d − b) 2) \left(x-\frac{r^{2}c-a}{r^{2}-1}\right)^{2}+\left(y-\frac{r^{2}d-b}{r^{2}-1}\right)^{2}\leq\frac{r^{2}}{(r^{2}-1)^{2}}\left((c-a)^{2}+(d-b)^{2}\right). That describes a circle of radius r r 2 − 1 ​ ( c − a) 2 + ( d − b) 2 \frac{r}{r^{2}-1}\sqrt{(c-a)^{2}+(d-b)^{2}} centered at ( r 2 ​ c − a r 2 − 1, r 2 ​ d − b r 2 − 1) (\frac{r^{2}c-a}{r^{2}-1},\frac{r^{2}d-b}{r^{2}-1}), which is strictly above the x x -axis if r 2 ​ d − b > ( c − a) 2 + ( d − b) 2 r^{2}d-b>\sqrt{(c-a)^{2}+(d-b)^{2}} and is tangent to it at ( r 2 ​ c − a r 2 − 1, 0) (\frac{r^{2}c-a}{r^{2}-1},0) if they are equal, as claimed.

Since we chose r 2 ​ c = a r^{2}c=a, the point of tangency (that is, W 1 W_{1}) is ( 0, 0) (0,0). Let θ H \theta_{H} and θ Z \theta_{Z} be the angles from the origin to H H and Z Z, respectively, so the escaper’s direction to the origin is π + θ H \pi+\theta_{H} and the pursuer’s is π + θ Z \pi+\theta_{Z}. Suppose the escaper moves in a direction θ ∂ H \theta_{\partial H}; that is, ( ∂ c, ∂ d) = ( cos ⁡ θ ∂ H, sin ⁡ θ ∂ H) (\partial c,\partial d)=(\cos\theta_{\partial H},\sin\theta_{\partial H}). (If the escaper moves at less than full speed, the pursuer can reduce its speed proportionally.) The direction directly toward ( 0, 0) (0,0) is π + θ H \pi+\theta_{H}, so the escaper’s angle from that direction is | π + θ H − θ ∂ H | |\pi+\theta_{H}-\theta_{\partial H}|. We will have the pursuer move in any direction θ ∂ Z \theta_{\partial Z} (that is, ( ∂ a, ∂ b) = ( r cos θ ∂ Z, r sin θ ∂ Z) (\partial a,\partial b)=(r\cos\theta_{\partial Z},r\sin\theta_{\partial Z})) such that | π + θ Z − θ ∂ Z | ≤ | π + θ H − θ ∂ H | |\pi+\theta_{Z}-\theta_{\partial Z}|\leq|\pi+\theta_{H}-\theta_{\partial H}|. Then cos ⁡ ( θ ∂ Z − θ Z) ≤ cos ⁡ ( θ ∂ H − θ H) \cos(\theta_{\partial Z}-\theta_{Z})\leq\cos(\theta_{\partial H}-\theta_{H}). Also, a 2 + b 2 = r ​ c 2 + d 2 \sqrt{a^{2}+b^{2}}=r\sqrt{c^{2}+d^{2}}, so a 2 + b 2 ​ cos ⁡ ( θ ∂ Z − θ Z) ≤ r ​ c 2 + d 2 ​ cos ⁡ ( θ ∂ H − θ H) \sqrt{a^{2}+b^{2}}\cos(\theta_{\partial Z}-\theta_{Z})\leq r\sqrt{c^{2}+d^{2}}\cos(\theta_{\partial H}-\theta_{H}). Those are the coordinate expansions of dot products: a cos θ ∂ Z + b sin θ ∂ Z ≤ r 2 [c cos θ ∂ H + d sin θ ∂ H] a\cos\theta_{\partial Z}+b\sin\theta_{\partial Z}\leq r^{2}\left[c\cos\theta_{\partial H}+d\sin\theta_{\partial H}\right]. Plugging in ∂ a = r cos θ ∂ Z \partial a=r\cos\theta_{\partial Z} and so on gives a ​ ∂ a + b ​ ∂ b ≤ r 2 ​ [c ​ ∂ c + d ​ ∂ d] a\partial a+b\partial b\leq r^{2}\left[c\partial c+d\partial d\right]. Plugging in a = r 2 ​ c a=r^{2}c, multiplying by 1 − r 2 1-r^{2} (which is negative), and rearranging gives ( r 2 ​ d − b) ​ ( r 2 ​ ∂ d − ∂ b) ≥ r 2 ​ ( a − c) ​ ( ∂ a − ∂ c) + r 2 ​ ( b − d) ​ ( ∂ b − ∂ d) (r^{2}d-b)(r^{2}\partial d-\partial b)\geq r^{2}(a-c)(\partial a-\partial c)+r^{2}(b-d)(\partial b-\partial d). The left side is the derivative of ( r 2 ​ d − b) 2 (r^{2}d-b)^{2} and the right side is the derivative of ( r ​ ( a − c) 2 + ( b − d) 2) \left(r\sqrt{(a-c)^{2}+(b-d)^{2}}\right), so the chosen direction of pursuer movement maintains r 2 − d ≥ r ​ ( a − c) 2 + ( b − d) 2 r^{2}-d\geq r\sqrt{(a-c)^{2}+(b-d)^{2}}, as desired. ∎

Finally, we can complete the proof of Lemma 6.3, by describing an APLO-like strategy for the pursuer to win G ε G G_{\varepsilon_{G}} (for all ε G > 0 \varepsilon_{G}>0) as long as the escaper moves a distance at most ε \varepsilon, contradicting the assumption that the escaper could win G G with at most ε \varepsilon more movement. To win ε G \varepsilon_{G}, the pursuer will use an ε G \varepsilon_{G} -oblivious strategy, so it can respond to at least ε G \varepsilon_{G} ’s worth of escaper movement, and so define a direction of escaper movement for each time step. By the previous two lemmas, if the pursuer can, at all times, move in a direction closer to its shortest path to each of W 1 W_{1} and W 2 W_{2} than the escaper’s direction of movement is to its shortest path to each of W 1 W_{1} and W 2 W_{2}, the escaper cannot win a race to any point on either e e or f f. By Lemma 6.4, the pursuer can do so, so the pursuer wins G ε G G_{\varepsilon_{G}}.

So as long as the escaper and pursuer stay within that circle of radius 2 ​ ε 0 2\sqrt{\varepsilon_{0}}, the escaper cannot win, contradicting the assumption that, a moment later, the escaper could win by running straight a distance at most ε \varepsilon.

In every surviving case, the escaper can win G ε 3 G_{\varepsilon^{3}} with speed ratio r ​ 1 1 + ε r\frac{1}{1+\varepsilon}, as desired. ∎

### 6.3 Algorithm

###### Theorem 6.7 (pseudopolynomial-time approximation scheme).

Given a polygon with integer vertex coordinates ∈ [0, N] \in[0,N], defining the escaper domain D h D_{h} as its interior and boundary, the exit set X X as its boundary, and the pursuer domain D z D_{z} as its boundary and optionally its exterior, there is an ( N / ε) O ⁡ ( 1) (N/\varepsilon)^{O(1)} -time approximation algorithm for ε \varepsilon -approximating the critical speed ratio r ∗ r^{*} in G G: the algorithm computes a speed ratio r r such that ( 1 − ε) ​ r ≤ r ∗ ≤ ( 1 + ε) ​ r (1-\varepsilon)r\leq r^{*}\leq(1+\varepsilon)r.

###### Proof.

At the top level, our algorithm uses a binary search to evaluate r ∗ r^{*}. To this end, first we give easily computable bounds on the range of r ∗ r^{*}. As a lower bound, r ∗ ≥ 1 r^{*}\geq 1; otherwise, the escaper can win along a single edge, as in the halfplane analysis (Theorem 4.2). As an upper bound, r ∗ ≤ 10.89898 ​ max p, q ∈ X ​ d z ​ ( p, q) d h ​ ( p, q) r^{*}\leq 10.89898\max_{p,q\in X}\frac{d_{z}(p,q)}{d_{h}(p,q)} by Theorem 3.2. Instead of computing this quantity directly, we can easily compute an upper bound as described in Point 3 after Lemma 6.3. As both quantities are pseudopolynomial, we get an interval containing r ∗ r^{*} of pseudopolynomial length. The overhead for binary search will be a factor logarithmic in this interval length, which is even polynomial.

It thus remains to give an approximate binary decider for binary search: given a speed ratio r r (from binary search), decide in pseudopolynomial time whether r ∗ < ( 1 − ε) ​ r r^{*}<(1-\varepsilon)r or r ∗ > ( 1 + ε) ​ r r^{*}>(1+\varepsilon)r, with the freedom to return either answer if ( 1 − ε) ​ r ≤ r ∗ ≤ ( 1 + ε) ​ r (1-\varepsilon)r\leq r^{*}\leq(1+\varepsilon)r.

A key ingredient is that we can compute the winner for the discrete game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) for any δ, γ, r \delta,\gamma,r in pseudopolynomial time. First, in the exterior model, we restrict to the convex hull of R z R_{z} by Lemma 6.1. Then we compute the graph with vertices V V and edges E h ∪ E z E_{h}\cup E_{z}. This graph has pseudopolynomial size, as the area of the convex hull of R z R_{z} and the perimeter of R h R_{h} are both pseudopolynomial. Thus the number of states — consisting of the current escaper and pursuer positions, the previous escaper and pursuer positions to check the win condition, and whose move is next — is also pseudopolynomial. We can thus compute all winning positions in the discrete game by marking all game states for which the escaper immediately wins (being adjacent to a vertex x x of B x B_{x} for two moves such that the pursuer still is not adjacent to x x), then repeatedly, mark any game state as an escaper win if either it is the escaper’s turn and they can move to any game state already marked an escaper win, or it is the pursuer’s turn and every game state they can move to is already marked an escaper win. After at most as many rounds as the pseudopolynomial number of game states, every game state from which the escaper wins will be so marked because, at each round, either at least one game state not previously marked as an escaper win will be so marked or no new game states will be marked and every following round will be the same. (This is essentially the finite case of the open determinacy theorem [GS53] exploited in Lemma 5.12.) Then the escaper wins the discrete game if and only if there is an escaper starting position s h s_{h} such that, for every pursuer starting position s z s_{z}, the state with the escaper at s h s_{h}, the pursuer at s z s_{z}, and the pursuer to move is marked as an escaper win.

First suppose that the discrete game G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) has an escaper winning strategy, where γ < min ⁡ { 1 4, r 2, 1 2 ​ ε ​ r } ​ δ \gamma<\min\{{1\over 4},{r\over 2},{1\over 2}\varepsilon r\}\delta. By Theorem 5.11, the continuous game G ε ​ ( r ′) G_{\varepsilon}(r^{\prime}) and thus G ⁡ ( r ′) G(r^{\prime}) has an escaper winning strategy where r ′ = r − 2 ​ γ δ > r − ε ​ r = ( 1 − ε) ​ r r^{\prime}=r-2{\gamma\over\delta}>r-\varepsilon r=(1-\varepsilon)r, so r ∗ > ( 1 − ε) ​ r r^{*}>(1-\varepsilon)r.

On the other hand, if r ∗ > ( 1 + ε) ​ r r^{*}>(1+\varepsilon)r, then the escaper wins G ⁡ ( ( 1 + ε) ​ r) G((1+\varepsilon)r). By Lemma 6.3, there is an escaper winning strategy for G ε ^ 3 ​ ( 1 + ε 1 + ε ^ ​ r) G_{\hat{\varepsilon}^{3}}(\frac{1+\varepsilon}{1+\hat{\varepsilon}}r) for any ε ^ ≤ ε 0 \hat{\varepsilon}\leq\varepsilon_{0}, where ε 0 \varepsilon_{0} is computed according to the algorithm after Lemma 6.3. By Corollary 5.7, there is no pursuer winning strategy for the same game. Let δ = 2 ​ ε 0 3 / r \delta=2\varepsilon_{0}^{3}/r, so that ε ^ 3 ≤ 1 2 ​ r ​ δ \hat{\varepsilon}^{3}\leq{1\over 2}r\delta. By the contrapositive of Theorem 5.11, the discrete game G ^ δ, γ ​ ( 1 + ε 1 + ε ^ ​ ( 1 − 2 ​ γ δ) ​ r) \hat{G}_{\delta,\gamma}(\frac{1+\varepsilon}{1+\hat{\varepsilon}}(1-{2\gamma\over\delta})r) has no pursuer winning strategy. By Lemma 5.12, the same game has an escaper winning strategy. Because decreasing the speed ratio only removes pursuer moves, G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) has an escaper winning strategy provided 1 + ε 1 + ε ^ ​ ( 1 − 2 ​ γ δ) ≥ 1 \frac{1+\varepsilon}{1+\hat{\varepsilon}}(1-{2\gamma\over\delta})\geq 1. If we further constrain that γ ≤ δ ⁡ ( ε 4 ​ ( 1 + ε ^) − ε ^ 2) \gamma\leq\delta({\varepsilon\over 4}(1+\hat{\varepsilon})-{\hat{\varepsilon}\over 2}) (which we can make positive by setting ε ^ \hat{\varepsilon} small enough), then 2 ​ γ δ ≤ ε 2 ​ ( 1 + ε ^) − ε ^ {2\gamma\over\delta}\leq{\varepsilon\over 2}(1+\hat{\varepsilon})-\hat{\varepsilon}, so 1 − 2 ​ γ δ ≥ 1 − ε 2 ​ ( 1 + ε ^) + ε ^ = ( 1 + ε ^) ​ ( 1 − ε 2) 1-{2\gamma\over\delta}\geq 1-{\varepsilon\over 2}(1+\hat{\varepsilon})+\hat{\varepsilon}=(1+\hat{\varepsilon})(1-{\varepsilon\over 2}), so 1 + ε 1 + ε ^ ​ ( 1 − 2 ​ γ δ) ≥ ( 1 + ε) ​ ( 1 − ε 2) = 1 + ε 2 − ε 2 2 ≥ 1 \frac{1+\varepsilon}{1+\hat{\varepsilon}}(1-{2\gamma\over\delta})\geq(1+\varepsilon)(1-{\varepsilon\over 2})=1+{\varepsilon\over 2}-{\varepsilon^{2}\over 2}\geq 1 provided ε ≤ 1 \varepsilon\leq 1.

Therefore, assuming r ∗ r^{*} is not in ( ( 1 − ε) ​ r, ( 1 + ε) ​ r) ((1-\varepsilon)r,(1+\varepsilon)r), we have r ∗ > ( 1 + ε) ​ r r^{*}>(1+\varepsilon)r if and only if G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) has an escaper winning strategy. So we can compute the winner of G ^ δ, γ ​ ( r) \hat{G}_{\delta,\gamma}(r) to decide whether r ∗ > ( 1 + ε) ​ r r^{*}>(1+\varepsilon)r or r ∗ < ( 1 − ε) ​ r r^{*}<(1-\varepsilon)r, enabling the binary search. ∎

For a related pursuit–evasion problem (can a polyhedral evader reach a goal point while avoiding a polyhedral pursuer, given maximum speeds for each?), Reif and Tate [RT93] give what might seem like a pseudopolynomial-time approximation scheme. Specifically, they give an ( n / ε) O ⁡ ( 1) (n/\varepsilon)^{O(1)} -time algorithm to find an evasion strategy if there is an “ ε \varepsilon -safe” evasion strategy that stays ε \varepsilon away from the pursuer and all obstacles. They also prove this result with a similar approach to discretizing the continuous game. However, to turn such an algorithm into an approximation algorithm for computing the critical speed ratio requires a relation between tweaking the speed ratio and guaranteeing a safety distance. This relation is precisely the point of our margin-of-victory Lemma 6.3, which is the bulk of our proof.

## 7 NP-hardness for Two Players in 3D

In this section, we prove that the pursuit–escape problem is NP-hard for polyhedral domains in 3D. Our proof is an easy extension of the famous result by Canny and Reif [CR87] that it is weakly NP-hard to find shortest paths in 3D amidst polyhedral obstacles.

###### Theorem 7.1.

It is weakly NP-hard to calculate the critical speed ratio r ∗ r^{*} for a pursuit-escape problem with polyhedral domains in 3D, with or without specified starting positions, and even if D h D_{h} and D z D_{z} are disjoint except at X X which consists of at most two points.

###### Proof.

We begin by showing the problem hard with specified starting positions for the players, and with arbitrary intersections between D h D_{h} and D z D_{z}. Then we adapt the construction to work without specified starting positions, with minimal intersection between D h D_{h} and D z D_{z}, and to make both D h D_{h} and D z D_{z} proper polyhedra (without lower-dimensional degeneracy).

#### Specified starting positions.

Our reduction follows Canny and Reif’s reduction from 3SAT to finding a path of length ≤ ℓ \leq\ell from s s to t t in a 3D polyhedral environment under any L p L_{p} metric [CR87]. The escaper domain D h D_{h} is exactly the polyhedral environment in Canny and Reif’s construction. The escaper’s start location is the start location s s, and the exit set X X consists of a single point, namely, the target location t t. Next, the pursuer domain D z D_{z} is a straight line between t t and any point s z s_{z} at distance ℓ + ε \ell+\varepsilon (slightly more than the target path length) from t t. The pursuer’s start location is s z s_{z}.

The pursuer’s optimal strategy is to run directly from s z s_{z} to the unique exit location t t and staying there. If the pursuer arrives ε \varepsilon before the escaper, then the pursuer wins, and vice versa. Thus, if the escaper can find a path of length ≤ ℓ \leq\ell between s s and t t, then the escaper can win and the critical speed ratio is greater than 1 1. Conversely, if all paths have length ≥ ℓ + ε \geq\ell+\varepsilon, then any escaper strategy cannot arrive before the pursuer, so the pursuer wins with a speed ratio of 1 1. As argued in [CR87, Corollary 2.3.4], there is a gap of at least 2 − 2 ​ n ​ m − 3 ​ n − 3 2^{-2nm-3n-3} in path length between positive and negative instances (where n n is the number of variables in m m is the number of clauses in the 3SAT formula), so setting ε = 2 − 2 ​ n ​ m − 3 ​ n − 3 \varepsilon=2^{-2nm-3n-3} completes the reduction.

#### Unspecified starting positions.

The construction of the escaper domain D h D_{h} remains exactly the polyhedral environment in Canny and Reif’s construction. But now the exit set X = { s, t } X=\{s,t\} consists of both the start and target locations. The pursuer domain D z D_{z} is a Manhattan from s s to t t, so that its length ℓ z \ell_{z} is easy to compute as the sum of coordinate differences between s s and t t. We set r = ℓ z / ( ℓ + ε) r=\ell_{z}/(\ell+\varepsilon), at which an escaper path of length ℓ + ε \ell+\varepsilon takes the same time as the pursuer traversing the entire path of D z D_{z}, and ask whether the critical speed ratio r ∗ ≤ r r^{*}\leq r.

If there is a path in D h D_{h} from s s to t t of length ≤ ℓ \leq\ell, then we construct a winning escaper strategy with speed ratio r r. The strategy starts at s s which, because s ∈ X s\in X, forces the pursuer to also start at s s. Then the strategy runs to t t along the path of length ≤ ℓ \leq\ell, oblivious to movement by the pursuer. The pursuer will remain at least ε \varepsilon away from t t, so the escaper escapes.

If all paths in D h D_{h} from s s to t t have length ≥ ℓ + ε \geq\ell+\varepsilon, then we construct a winning pursuer strategy with speed ratio r r. For any escaper location h ∈ D h h\in D_{h}, the pursuer computes the shortest-path distances d h ​ ( s, h) d_{h}(s,h) and d h ​ ( h, t) d_{h}(h,t). (This strategy is expensive to compute, but all we need is that it exists.) By the triangle inequality,

 | d h ​ ( s, h) + d h ​ ( h, t) ≥ d h ​ ( s, t) ≥ ℓ + ε. d_{h}(s,h)+d_{h}(h,t)\geq d_{h}(s,t)\geq\ell+\varepsilon. |  |

We define the pursuer strategy Z ⁡ ( h) Z(h) to be the unique point along the path D z D_{z} that satisfies

 | d z ​ ( Z ​ ( h), s) d z ​ ( Z ⁡ ( h), s) + d z ​ ( Z ⁡ ( h), t) = d h ​ ( h, s) d h ​ ( h, s) + d h ​ ( h, t). \frac{d_{z}(Z(h),s)}{d_{z}(Z(h),s)+d_{z}(Z(h),t)}=\frac{d_{h}(h,s)}{d_{h}(h,s)+d_{h}(h,t)}. |  |

If h h varies with speed ≤ 1 \leq 1, then Z ⁡ ( h) Z(h) varies with speed ≤ r \leq r. The strategy is history-independent, so is a valid pursuer strategy. Because Z ⁡ ( s) = s Z(s)=s and Z ⁡ ( t) = t Z(t)=t, Z Z is in fact a winning pursuer strategy.

#### Disjoint regions.

Next we achieve the property that D h ∩ D z = X D_{h}\cap D_{z}=X, whereas currently the line segment D z D_{z} might intersect D h D_{h} at other intermediate points. In Canny and Reif’s construction, almost all of the polyhedral region D h D_{h} is “thin”, with a maximum width of w = 1 / 2 Θ ⁡ ( n ​ m) w=1/2^{\Theta(nm)}. They show that an additive change of O ⁡ ( w) O(w) to the path length does not affect the hardness reduction. Thus, we can safely move the exits in X X from s, t s,t to the nearest boundary faces of the polyhedral region D h D_{h}. Then we can modify D z D_{z} to a path between the two points of X X that avoids otherwise intersecting D h D_{h}. Again we set ℓ z \ell_{z} to the length of this path, and set r = ℓ z / ( ℓ + ε) r=\ell_{z}/(\ell+\varepsilon) as before. The rest of the argument works as above.

#### Polyhedral domains.

Finally, we show how to thicken the pursuer path so that the pursuer domains D z D_{z} is a proper polyhedron instead of a one-dimensional path. When we lay out Canny and Reif’s construction, we ensure that the first path splitter visited after the start location has no other gadget above it, and that the final clause filter visited has no other clause below it. These properties ensure that the start and end positions s, t s,t each has an orthogonal ray that does not intersect the rest of the construction. We set X X to the intersection of ∂ D h \partial D_{h} with these rays; these two points are still within O ⁡ ( w) O(w) of s s and t t respectively. Now we can route the path D z D_{z} orthogonality out and around the bounding box of D h D_{h}, keeping it at least O ⁡ ( w) O(w) distance away from any part of D h D_{h} and using at most six turns.

We now construct a polyhedral pursuer domain D z ′ D^{\prime}_{z} based on the orthogonal path D z D_{z}. For all parts of D z D_{z} more than w w away from the bounding box of D h D_{h}, we make D z ′ D^{\prime}_{z} an orthotube centered on D z D_{z} with orthogonal thickness w / 24 w/24. Then we connect the ends of these tubes to their respective closer point in X X via two pyramid caps that do not intersect D h D_{h}. The new pursuer shortest path has gotten smaller from the ability to shortcut corners in the orthotube, but the change in distance remains less than w w, and so still within the additive factor for which Canny and Reif’s construction works. ∎

## 8 Multiple Escapers and Pursuers

In this section, we prove stronger computational hardness of computing or approximating critical speed ratio in broader models of pursuit–escape problems. All of the hardness proofs require that there be multiple pursuers, not just one, such that any one of them can block the escaper’s escape. Some will also require that there be multiple escapers, who win if at least one escapes. First we generalize our model to allow multiple escapers and pursuers (Section 8.1). To make the hardness proofs more interesting, we discuss some positive results as well, in Sections 8.2 – 8.4. Then Section 8.5 describes the hardness results.

### 8.1 Model

First we describe the necessary extensions to the single-escaper single-pursuer model of Section 2 and Section 5 to handle multiple escapers and pursuers. Suppose there are n h n_{h} escapers and n z n_{z} pursuers. We define a two-player game where the escaper player controls all n h n_{h} escapers and the pursuer player controls all n z n_{z} pursuers. We refer to the n h + n z n_{h}+n_{z} escapers and pursuers as individuals.

#### Domains.

The definition of “domain” remains unchanged, but now instead of a single domain for each player, the input specifies a set of domains for each player and an integer capacity for each domain representing an upper bound on the number of individuals a player can place on the respective domain. We assume that every escaper domain and every pursuer domain intersect in a measure-zero set (possibly empty). We allow two domains of the same player to intersect, but still forbid individuals from jumping across domains at such intersections; they must remain in their originally assigned domain. We are also given a set of (escaper) exit locations, which must be a subset of the union of all pursuer domains. In this setting, the polygon model restricts the escaper domain set to contain a single simple polygon with infinite capacity. Similarly the external and moat models are defined with infinite capacity.

#### Strategies.

The definitions of “pursuer motion path” and “escaper motion path” remain unchanged, but now a player strategy involves multiple such paths. Suppose the player has n p n_{p} individuals (either n h n_{h} or n z n_{z}) and the opponent has n o n_{o} individuals (either n z n_{z} or n h n_{h}). A player strategy is a function A A mapping n o n_{o} opponent motion paths b 1, b 2, …, b n o b_{1},b_{2},\dots,b_{n_{o}} to n p n_{p} player motion paths A i ​ ( b 1, b 2, …, b n o) A_{i}(b_{1},b_{2},\dots,b_{n_{o}}) for i ∈ { 1, 2, …, n p } i\in\{1,2,\dots,n_{p}\} satisfying the following nonbranching-lookahead constraint:

for any opponent motion paths b 1, b 2, …, b n o, b ~ 1, b ~ 2, …, b ~ n o b_{1},b_{2},\dots,b_{n_{o}},\tilde{b}_{1},\tilde{b}_{2},\dots,\tilde{b}_{n_{o}} such that b j b_{j} and b ~ j \tilde{b}_{j} agree on [0, t] [0,t] for all j ∈ { 1, 2, …, n o } j\in\{1,2,\dots,n_{o}\}, the strategy’s player motion paths A i ​ ( b 1, b 2, …, b n o) A_{i}(b_{1},b_{2},\dots,b_{n_{o}}) and A ⁡ ( b ~ 1, b ~ 2, …, b ~ n o) A(\tilde{b}_{1},\tilde{b}_{2},\dots,\tilde{b}_{n_{o}}) also agree on [0, t] [0,t] for all i ∈ { 1, 2, …, n p } i\in\{1,2,\dots,n_{p}\}.

In addition, an escaper strategy must satisfy the escaper-start constraint:

for each i ∈ { 1, 2, …, n p } i\in\{1,2,\dots,n_{p}\}, all paths H i ​ ( z) H_{i}(z) (over all pursuer motion paths z z) must start at a common point H i ​ ( z) ​ ( 0) H_{i}(z)(0).

#### Win condition.

We model the escaper player’s natural goal of maximizing the number of escapers that escape, i.e., reach an exit sufficiently far from any pursuer. Thus we define winning relative to an integer goal g ∈ [1, n h] g\in[1,n_{h}] for the number of escapers that escape.

Given escaper motion paths h 1, h 2, …, h n h h_{1},h_{2},\dots,h_{n_{h}} and pursuer motion paths z 1, z 2, …, z n h z_{1},z_{2},\dots,z_{n_{h}}, we say that escaper i i escapes by 𝜺 \varepsilon if, for some time t t, h i ​ ( t) h_{i}(t) is on an exit and, for all j ∈ { 1, 2, …, n z } j\in\{1,2,\dots,n_{z}\}, z j ​ ( t) z_{j}(t) is at least ε \varepsilon away from h i ​ ( t) h_{i}(t) in the pursuer metric.

A pursuer strategy Z Z wins 𝑮 𝜺 G_{\varepsilon} if, for all escaper motion paths h 1, h 2, …, h n h h_{1},h_{2},\dots,h_{n_{h}}, the resulting pursuer motion paths Z 1 ​ ( ⋯), Z 2 ​ ( ⋯), …, Z n z ​ ( ⋯) Z_{1}(\cdots),Z_{2}(\cdots),\dots,Z_{n_{z}}(\cdots) let < g <g escapers to escape. An escaper strategy H H wins 𝑮 𝜺 G_{\varepsilon} if, for all pursuer motion paths z 1, z 2, …, z n z z_{1},z_{2},\dots,z_{n_{z}}, the resulting escaper motion paths H 1 ​ ( ⋯), H 2 ​ ( ⋯), …, H n h ​ ( ⋯) H_{1}(\cdots),H_{2}(\cdots),\dots,H_{n_{h}}(\cdots) let ≥ g \geq g escapers to escape. As before, a pursuer strategy wins 𝑮 G if it wins G ε G_{\varepsilon} for all ε > 0 \varepsilon>0, and an escaper strategy wins 𝑮 G if it wins G ε G_{\varepsilon} for some ε > 0 \varepsilon>0.

By straightforward extensions of the previous proofs, we can show that exactly one player wins any instance of game G G.

### 8.2 Multiple Escapers

In this section, we give simple strategies that narrow the interesting cases for multiple escapers. First we show that we can restrict to the goal of g = 1 g=1 escaper escaping (perhaps to call for help).

###### Proposition 8.1.

Every escaper can escape in a game with multiple escapers if and only if the single escaper could escape in the same game with only one escaper.

###### Proof.

If one escaper can escape in a game with only one escaper, all the escapers can stay together, moving as one escaper would to escape. If the pursuers can keep a lone escaper from escaping, they can ignore all but one of the escapers and keep that escaper from escaping. ∎

Next we identify some simple scenarios where multiple escapers can always win (with g = 1 g=1).

###### Proposition 8.2.

If there is only one escaper domain, the cardinality of the exit set is at least n h n_{h}, and if escapers outnumber pursuers, then one escaper can always escape.

###### Proof.

Each of the escapers can stand at a distinct point in the exit locations. At at least n h − n z n_{h}-n_{z} of those spots, there is no pursuer, so the escapers at those spots escape. ∎

### 8.3 Approximation Algorithms

In this section, we describe some simple extensions of our approximation algorithms to the case of multiple escapers and/or pursuers.

First, Theorem 6.7 still gives a pseudopolynomial approximation scheme if there are multiple (but O ⁡ ( 1) O(1)) escapers and/or pursuers. The proof is essentially the same: we can solve a discrete game with O ⁡ ( 1) O(1) pursuers, and the critical speed ratio is bounded above by the critical speed ratio for one pursuer.

Second, the O ⁡ ( 1) O(1) -approximation algorithm from Section 3 seems more difficult to generalize. One approach is to restrict to a pursuer strategy where the pursuers divide up regions to guard and then individually follow a strategy akin to the one used in Section 3. One side of Theorem 3.2 has an analogue:

###### Corollary 8.3.

Consider the game where a polygon P P is designated as the only escaper domain of capacity n h = 1 n_{h}=1, and there is a single pursuer domain of capacity n z n_{z} in the moat or exterior model. Consider partitions of the boundary of P P into n z n_{z} (not necessarily connected) regions ℛ = { R 1, R 2, …, R n z } \mathcal{R}=\{R_{1},R_{2},\dots,R_{n_{z}}\}. The pursuers win if their speed is at least

 | min partition ​ ℛ ⁡ ( 10.89898 ​ max p, q ​ in same region ​ R i ∈ ℛ ​ d z ​ ( p, q) d h ​ ( p, q)). \min_{\text{partition }\mathcal{R}}\left(10.89898~\max_{p,q\text{ in same region }R_{i}\in\mathcal{R}}~\frac{d_{z}(p,q)}{d_{h}(p,q)}\right). |  |

###### Proof.

Each pursuer can ignore all of the boundary but the part assigned to it and use the strategy of Theorem 3.2. ∎

However, for the other side we have no analogue. Does there exist c > 0 c>0 such that, for the game described in Corollary 8.3, the escaper wins if the pursuers’ speed is less than the minimum over partitions of the boundary into (not necessarily connected) regions of

 | c ⋅ max p, q ​ in same region ⁡ d z ​ ( p, q) d h ​ ( p, q) ​? c\cdot\max_{p,q\text{ in same region}}\frac{d_{z}(p,q)}{d_{h}(p,q)}? |  |

We leave this question as an open problem.

### 8.4 Slow Pursuers

In this section, we prove some simple results about pursuers running slower than or equal speed to the escapers, i.e., the speed ratio r ≤ 1 r\leq 1. Assume the polygon model (exterior or moat). First we show that the escaper always wins for r < 1 r<1:

###### Proposition 8.4.

For finitely many pursuers whose speed is strictly less than the escaper’s ( r < 1 r<1), the escaper wins in a polygonal domain P P.

###### Proof.

The intuition is as follows. When close to an edge, the escaper can outrun a single pursuer and escape. Thus there must be other pursuers nearby to catch the escaper. However, how close they need to be depends on how close the escaper is to the edge, and thus the escaper can force the pursuers to guard an arbitrarily small portion of an edge. Once clustered the escaper can outrun the whole group and escape. We now formalize such a strategy and show there is always a region of the polygon in which it can be executed.

First we describe the escaper strategy. Let R R be a δ × Δ \delta\times\Delta rectangle (i) contained in P P, and (ii) whose edge of length Δ \Delta is contained by the longest edge e e of P P. We determine Δ \Delta later as a function of δ \delta. We choose δ \delta to be small enough to satisfy properties (i) and (ii). Without loss of generality, e e is horizontal and the interior of P P is above e e. We define some points { u 1, …, u m + 1 } \{u_{1},\ldots,u_{m+1}\} of interest on the upper edge of R R called threat points. Make u 1 u_{1} (respectively, u m + 1 u_{m+1}) the upper left (respectively, upper right) corner of R R and place the remaining u i u_{i} so that the distance between consecutive points is the same. For each threat point u i u_{i}, we denote by u i ′ u_{i}^{\prime} its vertical projection on e e. The escaper starts at the upper left corner of R R and will move to the right at full speed. At each threat point u i u_{i}, the escaper checks whether they can win by running to u i ′ u_{i}^{\prime} at full speed. We show that this will be the case for at least one of the threat points, thus the escaper wins.

The main idea is that R R is chosen so that if a pursuer can guard the vertical projection of a threat point in time to prevent the victory of the escaper at that point, they cannot reach any of the subsequent projections of threat points in time. Then, each pursuer can only prevent the victory of the escaper at a single threat point. Because there are m + 1 m+1 threat points, the escaper wins. We proceed with the details. At a threat point u i u_{i}, the escaper can win by running at u i ′ u_{i}^{\prime} if there are no pursuers within r ​ δ r\delta distance from u i ′ u_{i}^{\prime}. We make the distance between consecutive threat point d = 2 ​ r ​ δ + ε 1 − r d=\frac{2r\delta+\varepsilon}{1-r} for some ε > 0 \varepsilon>0 determined later, so that, while the escaper travels d d, the distance traveled by pursuers is d − 2 ​ r ​ δ − ε d-2r\delta-\varepsilon. Then, if a pursuer is guarding u i ′ u_{i}^{\prime} when the escaper is at u i u_{i}, it will be at least ε \varepsilon away from the disk centered at u i + 1 ′ u_{i+1}^{\prime} with radius r ​ δ r\delta when the escaper is at u i + 1 u_{i+1}. Since the escaper runs to the right at full speed until they can win, such pursuer can never catch up. By definition, Δ = ( m + 1) ​ 2 ​ r ​ δ + ε 1 − r \Delta=(m+1)\frac{2r\delta+\varepsilon}{1-r}. We can choose ε = ‖ e ‖ 10 ​ m \varepsilon=\frac{\|e\|}{10m}, so that we can choose δ \delta small enough so that Δ < ‖ e ‖ / 2 \Delta<\|e\|/2 and properties (i) and (ii) are satisfied. ∎

Next we consider r = 1 r=1 where the pursuers and escaper have equal speeds. In the case of one pursuer, the escaper can always win by shortcutting across a convex vertex. But multiple pursuers can win in some cases:

###### Proposition 8.5.

If r = 1 r=1, and the exterior of the polygon can be divided into n z n_{z} convex regions that cover the boundary of the polygon, then the pursuers can win in the exterior model.

###### Proof.

Each pursuer can stay in one region, staying at the closest point in that region to the current escaper position (satisfying the nonbranching-lookahead constraint). The closest point in a convex region to the escaper cannot move faster than the escaper can, so the pursuers can keep up with this strategy (speed-limit constraint). If the escaper reaches the boundary, there is a pursuer region containing that boundary, and therefore a pursuer at the closest point in that region to the escaper, which is the escaper’s location itself. So, the escaper cannot escape. ∎

###### Corollary 8.6.

If r = 1 r=1, the escaper domain is a polygon P P with n n vertices, and n z = n n_{z}=n, then pursuers can win.

There is no lower bound analogous to Proposition 8.5 because 4 pursuers suffice to guard polygons like the one in Figure 20 with arbitrarily many vertices. Two pursuers can stay on the top and two on the bottom; each of those can be assigned to guard every other triangular region of the convex hull outside P P.

Figure 20: A polygon guardable by 4 pursuers with speed equal to the escaper’s in the exterior model. Colored regions denote the (disconnected) region assigned to each pursuer to guard.

For convex polygons, we can win with half as many pursuers:

###### Proposition 8.7.

If r = 1 r=1, the escaper domain is a convex n n -gon P P, and n z = ⌈ n 2 ⌉ n_{z}=\lceil\frac{n}{2}\rceil, then the escaper can win.

###### Proof.

The escaper should start at any vertex h h on the boundary (escaper-start constraint). Let h ′ h^{\prime} be the point opposite h h on ∂ P \partial P, that is, the point for which the pursuer distance from h h is maximal. The points h h and h ′ h^{\prime} split ∂ P \partial P into two sections, at least one of which must have at least ⌈ n 2 ⌉ \lceil\frac{n}{2}\rceil vertices (counting h h but not h ′ h^{\prime}). The escaper should run along that section of perimeter except at a small neighborhood of vertices. With this strategy, whenever the escaper is running along an edge there should always be a pursuer at the same position in order to prevent an escaper victory. Let θ \theta be the maximum internal angle, and α \alpha be the length of the shortest edge of P P. We first argue that there should be at least two pursuers in the α 4 \alpha\over 4 -neighborhood of h h at the start to prevent an escaper win. If not, the escaper can follow the same strategy as the wedge case (Theorem 4.1) with a small enough ε \varepsilon so that the length of the escaper path is at most α 16 \alpha\over 16 guaranteeing a separation of at least α 8 \alpha\over 8 from any pursuer not initially close to h h. We now describe the escaper strategy at an α 4 \alpha\over 4 -neighborhood of a vertex v v (along the chosen section of the perimeter) incident to edges e 1 e_{1} and e 2 e_{2}. Let p 1 p_{1} and p 2 p_{2} be the points obtained by the intersection of a circle centered at v v with radius α 4 \alpha\over 4 with e 1 e_{1} and e 2 e_{2} respectively. When the escaper reaches p 1 p_{1}, go directly to p 2 p_{2} and continue traversing e 2 e_{2}. At the moment the escaper is at p 1 p_{1}, if the only pursuers within α 2 \alpha\over 2 of p 2 p_{2} (in pursuer metrics) are at p 1 p_{1}, the escaper wins by reaching p 2 p_{2} while being at least 2 ​ α ​ ( 1 − sin ⁡ θ 2) > 0 2\alpha(1-\sin\frac{\theta}{2})>0 away from any pursuer. Otherwise, there is at least one new pursuer (one that was not at p 1 p_{1} with the escaper) that must follow the escaper in its traversal of e 2 e_{2}. Then the pursuers that were following the escaper in e 1 e_{1} will be behind the escaper and will not be able to be ahead of the escaper again because they do not have time to run around past h ′ h^{\prime} before the escaper gets there. For each of the ⌈ n 2 ⌉ − 1 \lceil\frac{n}{2}\rceil-1 vertices, there must be at least one new pursuer guard to prevent an escaper victory. With the initial 2 pursuers, ⌈ n 2 ⌉ + 1 \lceil\frac{n}{2}\rceil+1 pursuers are necessary to prevent an escaper win. At all moments the escaper speed is 1 (speed-limit constraint) and, apart from the application of Theorem 4.1, the escaper path does not depend on pursuer position at all (nonbranching-lookahead constraint). ∎

Although Proposition 8.7 is true for both the moat and exterior models, we can make a slightly stronger statement in the moat model using the same proof.

###### Corollary 8.8.

In the moat model, if P P is a polygon with c c*convex*vertices, then the escaper can escape from ⌈ c 2 ⌉ \lceil\frac{c}{2}\rceil pursuers of the same speed as theirs.

### 8.5 Hardness Results

In this section, we prove PSPACE-hardness and hardness of approximation results, as specified in Table 2, for problems of escaping from pursuers with various combinations of parameters. All results are for 1-dimensional domains (graph model). In Table 2, the “Domain” column describes whether there is an additional constraint to the domains:

- •

Planar: each domain is a tree, they pairwise intersect only at leaves, and the union of all domains is the embedding of a planar graph;

- •

Connected: there is a single escaper domain and a single pursuer domain.

###### Theorem 8.9.

Consider a multi-escaper/pursuer game with g = 1 g=1. It is PSPACE-hard to decide whether pursuers has a winning strategy even if each domain is a tree, they pairwise intersect only at leaves, all leaves are exits, and the union of all domains is the embedding of a planar graph.

###### Proof.

Our reduction is from Nondeterministic Constraint Logic (NCL) [HD09]. An instance of NCL is given by a planar cubic weighted graph G NCL G_{\mathrm{NCL}} (called a constraint graph) where each edge has either weight 1 (called red) or weight 2 (called blue). Each vertex is either incident to a single blue and two red edges (called an AND vertex), or incident to three blue edges (called an OR vertex). A configuration of the constraint graph is an orientation (specifying a direction for each edge) satisfying that every vertex has incoming edges of total weight at least 2 2 (the inflow constraint). Given a configuration, a move flips the orientation of one edge in such a way that results in another configuration (i.e., satisfying the inflow constraint). The reachable configurations remain the same in asynchronous NCL where we allow partial orientations (some undirected edges), where an undirected edge does not count as incoming at either endpoint, and allow a move to transform an oriented edge into an unoriented one or vice versa (while still satisfying the inflow constraint) [Vig13]. Given a planar constraint graph, a configuration of that graph, and an edge e out e_{\text{out}}, it is PSPACE-complete to decide whether there is a sequence of moves that flips e out e_{\text{out}} at the end [HD09]. The number of moves is less than 2 | E ⁡ ( G NCL) | 2^{|E(G_{\mathrm{NCL}})|} because this upper bounds the number of states ( 3 3 possible orientations for each edge).

The PSPACE-hardness reduction for NCL can be modified to have two degree- 1 1 vertices v in v_{\text{in}} and v out v_{\text{out}} with no constraint on their incoming weights, one blue edge e in e_{\text{in}} initially pointing toward v in v_{\text{in}} and another blue edge e out e_{\text{out}} initially pointing away from v out v_{\text{out}}. (In fact, a subset of the reduction given in [HD09, Section 5.2] works exactly this way, where e in e_{\text{in}} is the leftmost try in edge and e out e_{\text{out}} is the leftmost try out edge. The reduction then adds a free edge terminator gadget to each of these edges, and we can simply not add these gadgets.) Furthermore, it is PSPACE-complete to decide whether, for some configuration of the constraint graph with e in e_{\text{in}} directed toward v in v_{\text{in}}, there is a sequence of moves that flips e out e_{\text{out}} to point toward v out v_{\text{out}}. This claim follows from the same reduction, because [HD09, Lemma 5.8] tells us that edge e in e_{\text{in}} initially pointing out from the construction (toward v in v_{\text{in}}) forces the entire configuration to reset. Furthermore, v in v_{\text{in}} and v out v_{\text{out}} are on the same face of a planar embedding of G NCL G_{\mathrm{NCL}}.

(a) OR gadget (b) AND gadget (c) WIN gadget

Figure 21: Gadgets that simulate a local NCL picture (left) with red and blue pursuer domains and green escaper domains (right). An edge drawn with only one endpoint represents exactly one half of that edge. (The other half is represented by the gadget on the other end of the edge.)

We build a game with the goal of g = 1 g=1 escaper escaping and a speed ratio of r = 1 r=1. Refer to Figure 21. Given a planar constraint graph G NCL G_{\mathrm{NCL}} with distinguished edges e in, e out e_{\text{in}},e_{\text{out}} and vertices v in, v out v_{\text{in}},v_{\text{out}} as described above, we build domains as follows. Every vertex of the constraint graph will be represented by a tree escaper domain (colored green in the figures) of capacity 1 1. Every edge of the constraint graph will be represented by a tree pursuer domain (colored red or blue in the figures to match the G NCL G_{\mathrm{NCL}} edge) of capacity 1 1. We will describe each edge as the joining of two “half edges”, with one half defined by each endpoint.

- •

For each OR vertex (Figure 21 (a)), the pursuer domain corresponding to each half edge is a curve of length 1 / 2 1/2, all incident to a common point x x; and the corresponding escaper domain is the single point x x, which is also an exit location. This escaper forces some pursuer to block the exit x x at all times, implementing the OR constraint.

- •

For each AND vertex (Figure 21 (b)), the pursuer domain corresponding to each red half edge is a curve of length 1 / 2 1/2, with distinct endpoints x 1, x 2 x_{1},x_{2} respectively; the corresponding escaper domain is a curve of length 1 / 4 1/4 between those endpoints x 1, x 2 x_{1},x_{2}, which are exit locations; and the pursuer domain corresponding to the blue half edge is a Y with leaf curves of length 1 / 8 1/8 incident to x 1, x 2 x_{1},x_{2}, and a curve of length 3 / 8 3/8 connecting to the other half of the edge. Thus the distance between x 1 x_{1} and x 2 x_{2} is 1 / 4 1/4 in both the escaper domain and the blue pursuer domain, so one pursuer in the blue pursuer domain can successfully prevent escape (matching the motion of the escaper), as can one pursuer in each of the red pursuer domains (staying at x 1 x_{1} and x 2 x_{2}), implementing the AND constraint. Also, the pursuer has a distance of 1 / 2 1/2 from one endpoint to the other half edge, as with the curves implementing all other half edges.

Thus, the escapers can force the pursuers to satisfy the inflow constraint at every AND and OR vertex. Conversely, the pursuers can make a valid NCL move in unit time by moving a pursuer from one end of the edge’s pursuer domain to the other end.

- •

For the special vertices v in v_{\text{in}} and v out v_{\text{out}} (Figure 21 (c)), the pursuer domain corresponding to each incident half edge e in e_{\text{in}} and e out e_{\text{out}} is a curve of length 1 / 2 1/2, with endpoints x in x_{\text{in}} and x out x_{\text{out}} respectively, both of which are exit locations; and we create one escaper domain for both vertices, a curve of length 2 | E ⁡ ( G NCL) | 2^{|E(G_{\mathrm{NCL}})|} connecting x in x_{\text{in}} and x out x_{\text{out}}. Because v in v_{\text{in}} and v out v_{\text{out}} are on a common face of G NCL G_{\mathrm{NCL}}, this connection preserves planarity.

To realize this construction in the plane, we scale down the planar embedding of G NCL G_{\mathrm{NCL}} to the point where all edges have length at most 1 1, and then we wiggle the paths to have the specified lengths.

Set n h = | V ⁡ ( G NCL) | − 1 n_{h}=|V(G_{\mathrm{NCL}})|-1 (the number of escaper domains) and n z = | E ⁡ ( G NCL) | n_{z}=|E(G_{\mathrm{NCL}})| (the number of pursuer domains). By the Pigeonhole Principle, each domain contains exactly one individual.

Now suppose that the NCL instance has a solution: an initial configuration where e in e_{\text{in}} points toward v in v_{\text{in}}, and a sequence of less than 2 | E ⁡ ( G NCL) | 2^{|E(G_{\mathrm{NCL}})|} moves that ends with flipping edge e out e_{\text{out}} toward v out v_{\text{out}}. Then the pursuer has the following winning strategy, parameterized by the location t t of the escaper along the length- 2 | E ⁡ ( G NCL) | 2^{|E(G_{\mathrm{NCL}})|} curve from x in x_{\text{in}} to x out x_{\text{out}}. At t = 0 t=0, the pursuers are at the ends of their pursuer domains corresponding to the initial configuration. Between each integer t − 1 t-1 and t t, one pursuer moves from one end of its pursuer domain to the other in unit time, corresponding to the t t th move in the sequence. (Once t t is beyond the number of moves in the sequence, the pursuer does nothing.) Throughout, whenever an AND vertex has an inward-directed blue edge, the pursuer assigned to that end tracks the motion of the escaper. Because the sequence of configurations satisfies the inflow constraint, the escapers cannot win, including at t = 2 | E ⁡ ( G NCL) | t=2^{|E(G_{\mathrm{NCL}})|} when a pursuer from the pursuer domain corresponding to e out e_{\text{out}} has reached x out x_{\text{out}}.

Conversely, suppose that the NCL instance has no solution. Then the escaper has the following winning strategy. The escapers at AND and OR gadgets enforce the inflow constraints. The escaper along the length- 2 | E ⁡ ( G NCL) | 2^{|E(G_{\mathrm{NCL}})|} curve starts at x in x_{\text{in}} and runs at full speed to x out x_{\text{out}}. This forces the pursuing player to start with a pursuer at x in x_{\text{in}}. At all times, we can construct a corresponding configuration of G NCL G_{\mathrm{NCL}}, where an edge is directed toward a vertex if the corresponding pursuer is at the end of the domain corresponding to that vertex, and undirected if the pursuer is in the middle. Thus we start at a configuration where e in e_{\text{in}} is directed toward v in v_{\text{in}}, and follow moves according to asynchoronous NCL. By supposition, we cannot reach a configuration where e out e_{\text{out}} is directed toward v out v_{\text{out}}, so the corresponding pursuer cannot reach x out x_{\text{out}} (being pinned at the other end). Thus the escaper reaches exit x out x_{\text{out}} and wins. ∎

###### Theorem 8.10.

Consider a multi-escaper/pursuer game in the graph model with g = 1 g=1. It is NP-hard to distinguish a critical speed ratio of 0 0 from ∞ \infty, even if each domain is a tree, they pairwise intersect only at leaves, and the union of all domains is the embedding of a planar graph.

###### Proof.

We reduce from the Planar Vertex Cover problem of finding a set of at most k k vertices in a planar graph such that every edge contains at least one of them, which Lichtenstein [Lic82] shows to be NP-hard. Given an instance of Planar Vertex Cover consisting of a planar graph G V ​ C G_{VC} and a target number of vertices k k, we build a game with n h = k n_{h}=k and n z = | E ⁡ ( G V ​ C) | − 1 n_{z}=|E(G_{VC})|-1. Subdivide each edge with a point pursuer domain of capacity 1 marked as an exit. This splits G V ​ C G_{VC} into | V ⁡ ( G V ​ C) | |V(G_{VC})| components, each containing a vertex of G V ​ C G_{VC} and its incident half edges. Define each such component to be an escaper domain of capacity 1.

If there is a vertex cover of size at most k k, then the escapers can start at the corresponding k k vertices (escaper-start constraint). Then the pursuing player places the | E ⁡ ( G V ​ C) | − 1 |E(G_{VC})|-1 pursuers, so there is at least one edge that no pursuer starts on, and an escaper who starts at a vertex incident to that edge can escape by that edge. The escaper strategy depends only on the pursuer’s initial positions (nonbranching-lookahead constraint).

Now consider the pursuer strategy that initially checks whether there is an exit location/pursuer domain incident to escaper domains with no escapers, and if so, places a pursuer at all other locations. This pursuer strategy depends only on escaper’s initial positions (nonbranching-lookahead constraint). The escaping player loses if the initial escaper placement do not correspond to a vertex cover. Because r r is irrelevant to the proof, it is NP-hard to distinguish a critical speed ratio of 0 0 from ∞ \infty. ∎

###### Theorem 8.11.

Consider a multi-pursuer game in the graph model with n h = 1 n_{h}=1. It is NP-hard to approximate the critical speed ratio r r to within a factor of 2 2, even when there is a single escaper domain and a single pursuer domain.

###### Proof.

We reduce from the Vertex Cover problem of finding a set of at most k k vertices in a graph G G such that every edge contains at least one of them, which is one of Karp’s original 21 NP-hard problems (from [Kar72]). First we reduce to the special of Vertex Cover where the graph is guaranteed to be connected; refer to Figure 22. Given an instance ( G, k) (G,k) of vertex cover, where graph G G has connected components C 1, C 2, …, C k C_{1},C_{2},\dots,C_{k}, we add a new “apex” vertex a a with incident edges to one arbitrarily chosen vertex in each C i C_{i} as well as a new degree- 1 1 vertex ℓ \ell. Any vertex cover in the new graph G ′ G^{\prime} includes either a a or ℓ \ell, and if it includes ℓ \ell, we can replace it with a a, which covers the incident added edges. Thus G ′ G^{\prime} has a vertex cover of size k + 1 k+1 if and only if G G has a vertex cover of size k k.

Figure 22: Reduction from Vertex Cover to Vertex Cover on connected graphs.

Given an instance of Vertex Cover consisting of a connected graph G V ​ C G_{VC} and a target number of vertices k k, we make a multi-pursuer game with n h = 1 n_{h}=1, n z = k n_{z}=k, and domains as shown in Figure 23. The pursuer domain realizes the vertex–edge incident graph of G V ​ C G_{VC}, with a node x v x_{v} for each vertex v v of G V ​ C G_{VC}, a node x e x_{e} for each vertex e e of G V ​ C G_{VC}, and a length- 1 1 curve between two nodes x v, x e x_{v},x_{e} that correspond to an incident vertex v v and edge e e of G V ​ C G_{VC}. The escaper domain is a star centered at a point h h, with leaves at the nodes x e x_{e} corresponding to edges e e of G V ​ C G_{VC}, each connected by a curve of length 1 1 to h h. The exit points are the leaves of the star, i.e., the nodes x e x_{e} corresponding to edges e e of G V ​ C G_{VC}.

Figure 23: A graph with one escaper for which it is NP-hard to determine the critical speed ratio.

If there is a vertex cover, then the following is a winning pursuer strategy for r ≥ 1 r\geq 1. Assign each pursuer to a vertex in the cover set. Suppose that the escaper is currently on an edge x e ​ h x_{e}h of the star escaper domain. (If the escaper is at the center h h of the star, we consider it to be on the lexically first edge e 0 e_{0}.) Let t t be the distance of the escaper from x e x_{e}. Let w w be the lexically first vertex that covers e e. Then we place the pursuer assigned to w w on the edge x w ​ x e x_{w}x_{e}, at distance t t away from x e x_{e}, while all other pursuers remain at their assigned vertices. Thus, whenever the escaper reaches an exit x e x_{e} ( t = 0 t=0), a pursuer will be at the same exit. This strategy depends only on the current escaper position (nonbranching-lookahead constraint) and requires that pursuers run at most at unit speed (speed-limit constraint).

If there is no vertex cover, then the following is a winning escaper strategy for r < 2 r<2. The escaper starts at h h (escaper-start constraint). Wherever the pursuer player initially places the pursuers, there is an exit that no pursuer is within distance 2 of: to be within distance 2 of an exit x e x_{e}, a pursuer must be within distance 1 of a vertex node x v x_{v} where v v is incident to e e; and the regions within distance 1 of each vertex node x v x_{v} are disjoint; so if there were a pursuer within distance 2 of every exit x e x_{e}, that would give a vertex cover. The escaper then runs at full speed to that exit, and at the moment the exit is reached, the nearest pursuer is at least 2 − r 2-r away by the speed-limit constraint. This strategy depends only on the initial pursuer positions (nonbranching-lookahead constraint).

Therefore it is NP-hard to distinguish a critical speed ratio of at most 1 from one at least 2, as claimed. ∎

## 9 Open Problems

We conclude with several interesting open problems raised by this research:

1. 1.

Is the pursuit–escape game (with one pursuer and one evader) NP-hard for a 2D polygon?

2. 2.

We conjecture that our approximation algorithms of Section 3 and Section 6 generalize to apply in 3D as well, with a slightly worse constant in the case of Section 3. This would nicely complement our 3D NP-hardness result of Section 7.

3. 3.

Section 6 gives a pseudopolynomial-time approximation for the critical speed ratio for a polygon. Is this the best one can do, or is there an approximation scheme whose time depends polynomially only on the length of the description of P P, or also on log ⁡ 1 ε \log\frac{1}{\varepsilon}? Related, we conjecture we can generalize this approximation scheme to apply to nonpolygonal shapes, such as constant-degree splines (which would include the disk).

4. 4.

Can we determine the exact critical speed ratio for regular n n -gons for n > 4 n>4? Our pursuer strategies for equilateral triangle (Section 4.5) and square (Section 4.6) generalize naturally, but we have been unable to find matching escaper strategies, suggesting these may not be tight.

5. 5.

Is there an analogue of Theorem 3.2 describing the critical speed ratio to within a constant factor when there are *two*(or O ⁡ ( 1) O(1)) pursuers?

The most obvious analogue, using a 2nd-order Voronoi diagram, does not work: if P P is a long, thin rectangle with one long side subdivided, one pursuer should stay on each side, but a 2nd-order Voronoi diagram might put both pursuers on one side.

The other most obvious analogue would have one pursuer attempts to guard the edge the escaper is closest to, the second pursuer greedily guards whatever point the first pursuer would have the most trouble reaching, and both pursuers delay changing their strategies by the use of fringe regions as in Theorem 3.2, but the escaper might exit multiple fringes simultaneously, which seems hard for the pursuers to account for without paying an extra factor equal to the number of pursuers.

6. 6.

Can we characterize the exact number of pursuers required to win in a polygon, under the exterior or moat model, when the speed ratio r = 1 r=1? Section 8 gives a few sufficient conditions and an interesting example.

7. 7.

Our PSPACE-hardness result for multiple pursuers (Theorem 8.9) requires one edge of exponential length. Is the problem strongly PSPACE-hard, i.e., even when all edge lengths are polynomial integers? Is the problem in PSPACE?

8. 8.

Can we adapt our model to *capturing pursuers*, where an escaper loses if it is ever within ε \varepsilon of a pursuer (for arbitrarily small ε > 0 \varepsilon>0)? This more natural model should not affect our main domains of polygons or Jordan regions, where an escaper can walk near the boundary instead of on it. However, in the general setting considered in Section 5, it becomes more difficult to prove every game has a unique winner; in particular, our discrete model needs adaptation to avoid accidental captures. We conjecture that this is possible.

We believe we can prove many more hardness results in this model. In particular, we believe the 3D one-pursuer one-escaper problem becomes EXPTIME-hard by a modification to the proof of [RT93], which would strengthen our NP-hardness result (Theorem 7.1).

9. 9.

What happens if we restrict pursuer and escaper strategies to be continuous functions of their opponent’s movement? Does this change allow us to define escaper winning without needing a uniform ε \varepsilon by which they win? (See related results in [BLW09, Lemma 6 and Theorem 7].) Is this a reasonable model, or does it forbid natural strategies?

## Acknowledgments

We thank Greg Aloupis and Fae Charlton for helpful early discussions on this topic. We also thank anonymous referees for helpful comments, leading us to formulate precise definitions of the model, and for giving the proofs of Lemmas 5.1 and 5.2. Supported in part by the NSERC and NSF grant CCF-2348067.

## References

- [ABG09] S. Alexander, R. Bishop, and Robert Ghrist. Capture pursuit games on unbounded domains. L’Enseignement Mathématique, 55:103–125, 2009.
- [AHRWN17] Mikkel Abrahamsen, Jacob Holm, Eva Rotenberg, and Christian Wulff-Nilsen. Best laid plans of lions and men. In Boris Aronov and Matthew J. Katz, editors, Proceedings of the 33rd International Symposium on Computational Geometry, volume 77 of Leibniz International Proceedings in Informatics (LIPIcs), pages 6:1–6:16, 2017.
- [AHRWN18] Mikkel Abrahamsen, Jacob Holm, Eva Rotenberg, and Christian Wulff-Nilsen. Best laid plans of lions and men. arXiv:1703.03687, January 2018.
- [AM84] M. Aigner and M.Fromme. A game of cops and robbers. Discrete Applied Mathematics, 8(1):1–12, April 1984.
- [BC17] Andrew Beveridge and Yiqing Cai. Pursuit-evasion in a two-dimensional domain. Ars Mathematica Contemporanea, 13(1), 2017.
- [BKIS12] Deepak Bhadauria, Kyle Klein, Volkan Isler, and Subhash Suri. Capturing an evader in polygonal environments with obstacles: The full visibility case. The International Journal of Robotics Research, 31(10):1176–1189, 2012.
- [BLW09] B. Bollobás, I. Leader, and M. Walters. Lion and man – can both win? arXiv:0909.2524, 2009. [https://arXiv.org/abs/0909.2524][12]. Extended version of [BLW12].
- [BLW12] B. Bollobás, I. Leader, and M. Walters. Lion and man—can both win? Israel Journal of Mathematics, 189(1):267–286, June 2012.
- [BM88] Edward Bierstone and Pierre Milman. Semianalytic and subanalytic sets. Publications Mathématiques de l’IHÉS, 67:5–42, 1988.
- [BN11] Anthony Bonato and Richard J. Nowakowski. The Game of Cops and Robbers on Graphs. American Mathematical Society, 2011.
- [Bol06] Béla Bollobás. The Art of Mathematics: Coffee Time in Memphis. bridge University Press, 2006.
- [CR87] John Canny and John Reif. New lower bound techniques for robot motion planning problems. In Proceedings of the 28th Annual Symposium on Foundations of Computer Science, SFCS ’87, pages 49–60, Washington, DC, USA, 1987. IEEE Computer Society.
- [Cro64] Hallard T. Croft. “Lion and man”: A postscript. Journal of the London Mathematical Society, 39:385–390, 1964.
- [Eng89] Ryszard Engelking. General Topology. Heldermann, Berlin, 1989.
- [FGK08] Fedor V. Fomin, Petr A. Golovach, and Jan Kratochvíl. On tractability of Cops and Robbers game. In G. Ausiello, J. Karhumäki, G. Mauri, and L. Ong, editors, Proceedings of the 5th IFIP International Conference on Theoretical Computer Science, pages 171–185, Milano, Italy, 2008.
- [FM09] Stephen Finbow and Gary MacGillivray. The Firefighter Problem: A survey of results, directions and questions. Australasian Journal of Combinatorics, 43:57–77, 2009.
- [Gar65] Martin Gardner. Letters. Scientific American, 213(5):10–12, November 1965. Reproduced in [Gar90].
- [Gar90] Martin Gardner. Mathematical Carnival. Penguin Books, London, 1990.
- [GS53] David Gale and F. M. Stewart. Infinite games with perfect information. In Contributions to the Theory of Games, vol. 2, Annals of Mathematics Studies, no. 28, pages 245–266. Princeton University Press, 1953.
- [Guy61] Richard K. Guy. The jewel thief. NABLA, 8:149–150, September 1961.
- [GV88] D. Yu. Grigor’ev and N. N. Vorobjov. Solving systems of polynomial inequalities in subexponential time. Journal of Symbolic Computation, 5(1):37–64, 1988.
- [HD09] Robert A. Hearn and Erik D. Demaine. Games, Puzzles, and Computation. A K Peters/CRC Press, 2009.
- [HS17] Dan Halperin and Micha Sharir. Arrangements. In Jacob E. Goodman, Joseph O’Rourke, and Csaba D. Tóth, editors, Handbook of Discrete and Computational Geometry, chapter 28, pages 723–762. CRC Press, 3rd edition, 2017.
- [Isa65] Rufus Isaacs. Differential Games. Wiley Press, New York, 1965.
- [Jan78] Vladimir Janković. About a man and lions. Matematički Vesnik, 2:359–361, 1978.
- [Kar72] Richard Karp. Reducibility among combinatorial problems. In R. E. Miller, J. W. Thatcher, J. D., and Bohlinger, editors, Complexity of Computer Computations, pages 85–103. Springer, Boston, 1972.
- [Kel55] John L. Kelley. General Topology. D. Van Nostrand Company, Inc., Princeton, 1955.
- [Kin15] William B. Kinnersley. Cops and Robbers is EXPTIME-complete. Journal of Combinatorial Theory, Series B, 111:201–220, March 2015.
- [Klo07] Oddvar Kloster. A solution to the Angel Problem. Theoretical Computer Science, 389(1–2):152–161, December 2007.
- [KS15] Kyle Klein and Subhash Suri. Pursuit evasion on polyhedral surfaces. Algorithmica, 73(4):740–747, December 2015.
- [Lew86] J. Lewin. The lion and man problem revisited. Journal of Optimization Theory and Applications, 49(3):411–430, 1986.
- [Lic82] David Lichtenstein. Planar formulae and their uses. SIAM Journal on Computing, 11(2):329–343, 1982.
- [Lit86] John Edensor Littlewood. Littlewood’s miscellany: edited by Béla Bollobás. Cambridge University Press, 1986.
- [Mát07] András Máthé. The Angel of power 2 wins. Combinatorics, Probability and Computing, 16(3):363–374, 2007.
- [MHIS09] Philip Munz, Ioan Hudea, Joe Imad, and Robert J. Smith? When zombies attack!: Mathematical modelling of an outbreak of zombie infection. In J. M. Tchuenche and C. Chiyaka, editors, Infectious disease modelling research progress. Nova Science Publishers, 2009.
- [Mit17] Joseph S. B. Mitchell. Shortest paths and networks. In Jacob E. Goodman, Joseph O’Rourke, and Csaba D. Tóth, editors, Handbook of Discrete and Computational Geometry, chapter 31, pages 811–848. CRC Press, 3rd edition, 2017.
- [Nah07] Paul J. Nahin. Chases and Escapes: The Mathematics of Pursuit and Evasion. Princeton Press, 2007.
- [O’B61] Thomas H. O’Beirne. Christmas puzzles and paradoxes. The New Scientist, 266:753, December 1961.
- [RR75] Peter A. Rado and Richard Rado. More about lions and other animals. Mathematical Sprectrum, 7(3):89–93, 1974/75.
- [RT93] John H. Reif and Stephen R. Tate. Continuous alternation: The complexity of pursuit in continuous domains. Algorithmica, 10:156–181, October 1993.
- [Smi14] Robert Smith? Mathematical Modelling of Zombies. University of Ottawa Press, 2014.
- [Spa19] Ben Sparks. Game of cat and mouse. Numberphile video, May 2019. [https://www.numberphile.com/videos/cat-and-mouse][13].
- [ST93] P. D. Seymour and R. Thomas. Graph searching and a min-max theorem for tree-width. Journal of Combinatorial Theory, Series B, 58(1):22–33, May 1993.
- [Vig13] Giovanni Viglietta. Partial searchlight scheduling is strongly PSPACE-complete. August 2013.
- [Wik25] Wikipedia. Arzelà–Ascoli theorem, 2025. [https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem][14].

## Appendix A Intrinsic Metrics of Compact Regions with Finitely Rectifiable Boundaries are Compact

###### Lemma A.1.

If R R is a compact subset of ℝ k \mathbb{R}^{k} and R R is finitely rectifiable, then the intrinsic (shortest-path) metric space M M induced by R R is compact.

###### Proof.

A metric space is compact if and only if it is *sequentially compact*, i.e., every infinite sequence p 1, p 2, … p_{1},p_{2},\ldots has a *limit point*p ∗ p^{*}, i.e., a point p ∗ p^{*} such that, for every ε > 0 \varepsilon>0, there is a p i p_{i} within distance ε \varepsilon of p ∗ p^{*}. We will prove that M M is sequentially compact. Consider an infinite sequence p 1, p 2, … ∈ R p_{1},p_{2},\ldots\in R. Because R R is compact, we can restrict to an infinite subsequence of p i p_{i} ’s that converges (in the Euclidean metric) to a limit point p ∗ ∈ R p^{*}\in R. We will prove that p ∗ p^{*} is a limit point with respect to the intrinsic metric as well.

Each p i p_{i} lies on an associated Lipschitz patch of R R. Because there are finitely many Lipschitz patches associated with R R, we can restrict to an infinite subsequence q 1, q 2, … q_{1},q_{2},\dots of p 1, p 2, … p_{1},p_{2},\dots for which all q i q_{i} ’s lie on the same Lipschitz patch S S. Let r i r_{i} be a parameter vector for point p i p_{i} on S S. Because S S ’s domain is compact, the points r i r_{i} have a limit point r ∗ r^{*} in S S ’s domain, corresponding to a point q ∗ q^{*} on S S. Because p 1, p 2, … p_{1},p_{2},\dots converges to its limit p ∗ p^{*}, the subsequence q 1, q 2, … q_{1},q_{2},\dots converges to the same limit p ∗ = q ∗ p^{*}=q^{*}.

Because p i p_{i} and q i q_{i} both converge to p ∗ = q ∗ p^{*}=q^{*} in Euclidean metric, d ⁡ ( p i, q i) → 0 d(p_{i},q_{i})\to 0; likewise, because r i → r ∗ r_{i}\to r^{*}, | r i − r ∗ | → 0 |r_{i}-r^{*}|\to 0. Therefore, d R ​ ( p i, p ∗) ≤ d S ​ ( p i, p ∗) → 0 d_{R}(p_{i},p^{*})\leq d_{S}(p_{i},p^{*})\to 0, so p ∗ p^{*} is a limit point of the p i p_{i} ’s in the intrinsic metric. ∎

Gar90


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:zabel@mit.edu
[4]: mailto:hugoakitaya@gmail.com
[5]: mailto:%7Bedemaine,mdemaine,jaysonl%7D@mit.edu
[6]: mailto:achesterberg@gmail.com
[7]: mailto:jasonku@mit.edu
[8]: https://www.imdb.com/search/keyword?keywords=zombie&amp;title_type=movie
[9]: https://www.imdb.com/search/keyword?keywords=zombie&amp;title_type=tvSeries
[10]: https://www.goodreads.com/shelf/show/zombie-apocalypse
[11]: https://store.steampowered.com/tag/browse/#global_1659
[12]: https://arXiv.org/abs/0909.2524
[13]: https://www.numberphile.com/videos/cat-and-mouse
[14]: https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem
