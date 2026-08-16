<!-- source: https://ar5iv.labs.arxiv.org/html/2003.08456 | converted from HTML -->

[2003.08456] Convex Hulls of Random Order Types

# Convex Hulls of Random Order Types Thanks: This research started at the Banff Workshop “Helly and Tverberg Type Theorems”, October 6-11, 2019, at the Casa Matemática Oaxaca (CMO), Mexico.

Xavier Goaoc Note: Supported by grant ANR-17-CE40-0017 of the French National Research Agency (ANR project ASPAG) and Institut Universitaire de France. Affiliation: Université de Lorraine, CNRS, INRIA Affiliation: LORIA, F-54000 Nancy, France Email: [xavier.goaoc@loria.fr][1] Emo Welzl Note: Supported by the Swiss National Science Foundation within the collaborative DACH project Arrangements and Drawings as SNSF Project 200021E-171681 Affiliation: Dept. of Computer Science Affiliation: ETH Zürich, Switzerland Email: [emo@inf.ethz.ch][1]

###### Abstract

We establish the following two main results on order types of points in general position in the plane (realizable simple planar order types, realizable uniform acyclic oriented matroids of rank 3 3):

1. (a)

The number of extreme points in an n n -point order type, chosen uniformly at random from all such order types, is on average 4 + o ⁡ ( 1) 4+o(1). For labeled order types, this number has average 4 − 8 n 2 − n + 2 4-\mbox{$\frac{8}{n^{2}-n+2}$} and variance at most 3 3.

2. (b)

The (labeled) order types read off a set of n n points sampled independently from the uniform measure on a convex planar domain, smooth or polygonal, or from a Gaussian distribution are concentrated, i.e., such sampling typically encounters only a vanishingly small fraction of all order types of the given size.

Result (a) generalizes to arbitrary dimension d d for labeled order types with the average number of extreme points 2 ​ d + o ⁡ ( 1) 2d+o(1) and constant variance. We also discuss to what extent our methods generalize to the abstract setting of uniform acyclic oriented matroids. Moreover, our methods allow to show the following relative of the Erdős-Szekeres theorem: for any fixed k k, as n → ∞ n\to\infty, a proportion 1 − O ⁡ ( 1 / n) 1-O(1/n) of the n n -point simple order types contain a triangle enclosing a convex k k -chain over an edge.

For the unlabeled case in (a), we prove that for any antipodal, finite subset of the 2 2 -dimensional sphere, the group of orientation preserving bijections is cyclic, dihedral or one of A 4 A_{4}, S 4 S_{4} or A 5 A_{5} (and each case is possible). These are the finite subgroups of S ​ O ​ ( 3) SO(3) and our proof follows the lines of their characterization by Felix Klein.

##### keywords

order type; oriented matroid; Sylvester’s Four-Point Problem; random polytope; sampling random order types; projective plane; excluded pattern; Hadwiger’s transversal theorem; hairy ball theorem; finite subgroups of S ​ O ​ ( 3) SO(3).

##### Acknowledgements

The authors thank Boris Aronov for helpful discussions, Gernot Stroth for help on the group theoretic aspects of the paper, and Pierre Calka for help on probabilistic geometry. Moreover, the referees made many suggestions helping us to improve the presentation.

## 1 Introduction

Geometric algorithms are often designed *over the reals*, taking advantage of properties of continuity, closure under arithemic operations, and geometric figures of ℝ d \mathbb{R}^{d}, but implemented *in discrete floating point arithmetic*. As documented by, e.g., Kettner et al. [42], even mild numerical approximations suffice to provoke spectacular failures in basic geometric algorithms over simple, non-degenerate inputs. An established approach to address this issue, carried out for example in the CGAL library [60], is to design geometric algorithms that branch according to predicates of bounded complexity that depend solely and directly on the numbers in the input of the algorithm (rather than on numbers resulting from intermediate calculations of the algorithm); this encapsulates the handling of numerical issues in the correct evaluation of signs of functions, and since these functions are typically polynomials, their sign can be efficiently certified by computer algebra methods such as interval arithmetic and root isolation (e.g., Descartes’ rule of sign or Sturm sequences). As a result, such geometric algorithms effectively operate on a combinatorial abstraction of the geometric input, as their courses are determined not by the numerical values given in input, but by the output of the predicate functions.

One of the simplest geometric predicates is the planar orientation predicate. The *orientation*χ ⁡ ( p, q, r) {\chi}(p,q,r) of an ordered triple ( p, q, r) (p,q,r) of points in ℝ 2 \mathbb{R}^{2} is defined as 1 1 (resp. − 1 -1, 0 0) if r r is to the left of (resp. to the right of, on) the line through p p and q q, oriented from p p to q q. Note that χ ⁡ ( p, q, r) {\chi}(p,q,r) equals the sign of the determinant

 | | x p y p 1 x q y q 1 x r y r 1 | = | x p − x r y p − y r x q − x r y q − y r |, {\left|\begin{array}[]{ccc}x_{p}&y_{p}&1\\ x_{q}&y_{q}&1\\ x_{r}&y_{r}&1\end{array}\right|=}\left|\begin{array}[]{ccc}x_{p}-x_{r}&y_{p}-y_{r}\\ x_{q}-x_{r}&y_{q}-y_{r}\end{array}\right|~, |  | (1) |

so it evaluates like a polynomial in the coordinates of p p, q q and r r. An algorithm that relies solely on orientation predicates, for instance Knuth’s planar convex hull algorithms [43, § ​ 10 \mathsection 10 and § ​ 11 \mathsection 11], will behave identically on two input point *sequences*( p 1, p 2, …, p n) (p_{1},p_{2},\ldots,p_{n}) and ( q 1, q 2, …, q n) (q_{1},q_{2},\ldots,q_{n}) such that

 | ∀ 1 ≤ i, j, k ≤ n, χ ⁡ ( p i, p j, p k) = χ ⁡ ( q i, q j, q k). \forall 1\leq i,j,k\leq n,\quad{\chi}(p_{i},p_{j},p_{k})={\chi}(q_{i},q_{j},q_{k}). |  | (2) |

It is therefore natural to consider such point sequences to be equivalent; this is done by declaring that they *have the same labeled order type*. This is an equivalence relation, and a *labeled order type*is an equivalence class for that relation. An even coarser grouping is obtained when one identifies point *sets*P P and Q Q for which there exists a bijection f: P → Q f\!:P\to Q that preserves orientations; an equivalence class for this coarser relation is called an *order type*. The order type of a point set determines many of its properties. 1 1 1 To give a few examples: the face lattice of its convex hull, the graphs that can be straight-line embedded onto it, including the triangulations it supports, the maximum depth of a point from the set with respect to Tukey or simplicial depth, and the range space it defines over halfspaces.

Order types, labeled or not, were introduced by Goodman and Pollack [31] to study higher-dimensional analogues of sorting, just like *uniform oriented matroids*were devised, independently, by Bland in his PhD thesis [14] to study the simplex algorithm, by Folkman and Lawrence [28] to study face lattices of polytopes, and by Las Vergnas [44] to study questions in graphs and combinatorics, and later rediscovered by Knuth [43] to study convex hull algorithms. These two structures are actually closely related. The orientation predicate, and therefore the notion of (labeled) order type can be defined in any *topological affine plane*[54], that is, in any geometry defined by a system of simple, connected, unbounded curves (called *pseudolines*) satisfying the usual incidence axioms (any two points are on exactly one pseudoline, and any two pseudolines intersect in at most one point), and some continuity conditions [54, § ​ 1 \mathsection 1]. An order type is called *abstract*if it can be constructed in a topological affine plane, and *realizable*if it can be constructed in the usual, euclidean, affine plane. The Faulkman-Lawrence representation theorem [28] asserts that abstract order types coincide with the relabeling classes of acyclic uniform oriented matroids of rank 3 3. 2 2 2 More generally, abstract and realizable order types can be defined in dimension d d and the abstract ones coincide with the relabeling classes of acyclic uniform oriented matroids of rank d + 1 d+1. These two structures, abstract vs. realizable, do, however, behave very differently from a computational point of view: abstract order types can be characterized by a handful of axioms on up to five points, whereas deciding if a given abstract order type is realizable is ∃ ℝ \exists\mathbb{R} -complete [57, 55]. The reason for that is Mnëv’s universality theorem [47], which essentially states that for any semi-algebraic set S S, there is a planar order type whose space of realizations is homotopy equivalent to S S. This universality propagates to some structures determined by order types, for instance polytopes, even simplicial ones [1], or Delaunay triangulations [44].

A geometric algorithm or conjecture can sometimes be *tested*by trying it on a large number of (pseudorandomly generated) candidate point sets. If the algorithm/conjecture actually depends on the order type of the input point set, this is merely a way of trying it on candidate order types. 3 3 3 For example, the largest point set in general position with no empty convex hexagon is known to have size between 29 29 and 1716 1716 [50, 29]; it is tempting to try and improve the lower bound by testing order types of size 30 30 or so. The first result of this paper (Theorem 1.1) is that many standard models of random point sets explore very inefficiently the space of (labeled) order types. To our knowledge, this is the first theoretical result on the quality of *any*method for generating random (labeled) order types.

We establish this concentration result by proving, and this is our main result, some sharp bounds on the expected number of *extreme*points in a typical (labeled) order type; extreme points are points that appear as vertices of the convex hull of the point set. (Since the number of extreme points is the same for all representatives of an order type, we speak of the number of extreme points of the order type; we do the same for every notion independent of the choice of representative, e.g., the size.) Here we consider only *simple (labeled) order types*, i.e., with no three points on a line; by “typical” we mean chosen equiprobably among all simple (labeled) order types of a given size n n. As an illustration, for n = 4 n=4, the only two simple order types are the convex quadrilateral and the triangle with an interior point, so the quantity we are after is 4 + 3 2 = 7 2 \frac{4+3}{2}=\frac{7}{2}. For n = 5 n=5, it is 5 + 4 + 3 3 = 4 \frac{5+4+3}{3}=4, see Figure 1.

Figure 1: Left: The two simple 4-point order types. Right: The three simple 5-point order types.

### 1.1 Main results

Let 𝖮𝖳 aff n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} ( 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}) denote 4 4 4 We use ‘aff’ here in order to discriminate from the *projective*order types, which we will have to consider later in the course of our investigation. the set of simple (simple labeled, resp.) n n -point order types. For n ∈ ℕ n\in\mathbb{N}, let μ n \mu_{n} be a probability measure on ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}. We say that the family { μ n } n ∈ ℕ \{\mu_{n}\}_{n\in\mathbb{N}}*exhibits concentration*if there exist subsets A n ⊆ ( 𝖫) 𝖮𝖳 n aff A_{n}\subseteq{\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}, n ∈ ℕ n\in\mathbb{N}, such that μ n ​ ( A n) → 1 \mu_{n}(A_{n})\to 1 and | A n | / | ( 𝖫) 𝖮𝖳 n aff | → 0 |A_{n}|/|{\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|\to 0. In plain English, families of measures that exhibit concentration typically explore a vanishingly small fraction of the space of simple (labeled) order types. Devillers et al. [21] conjectured that the order types of points sampled uniformly and independently from a unit square exhibit concentration. We prove this conjecture and more:

###### Theorem 1.1.

Let μ \mu be a probability measure on ℝ 2 \mathbb{R}^{2} given by one of the following: (a) the uniform distribution on a smooth compact convex set, (b) the uniform distribution on a convex compact polygon, (c) a Gaussian distribution. The family of probabilities on ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} defined by the (labeled) order type of n n random points chosen independently from μ \mu exhibits concentration.

Another standard model of random point sets, called the Goodman-Pollack model, is the random 2 2 -dimensional projection of an n n -dimensional simplex; it is statistically equivalent to points chosen independently from a Gaussian distribution [10, Theorem 1], so the distribution on random order types it produces in the plane also exhibits concentration.

We establish Theorem 1.1 by comparing probability distributions on order types through one statistic: the number of extreme points. This statistic is already well understood for distributions induced by random point sets, as it corresponds to the typical number of vertices in models of random polytopes that are standard in stochastic geometry. We establish it here for the combinatorial model. For *labeled*order types, we prove:

###### Theorem 1.2.

For n ≥ 3 n\geq 3, the number of extreme points in a random simple labeled order type chosen uniformly among the simple, labeled order types of size n n in the plane has average 4 − 8 n 2 − n + 2 4-\mbox{$\frac{8}{n^{2}-n+2}$} and variance less than 3 3.

For non-labeled order types our statement is less precise:

###### Theorem 1.3.

For n ≥ 3 n\geq 3, the number of extreme points in a random simple order type chosen uniformly among the simple order types of size n n in the plane has average 4 + O ( n − 1 / 2 + ε) 4+O\left(n^{-1/2+\varepsilon}\right) for any ε > 0 \varepsilon>0.

Our proof of Theorem 1.2 extends to arbitrary dimension (Theorem 10.1), but not our proof of Theorem 1.3. A large part of our methods and results extend to abstract order types. In particular, Theorem 1.2 holds in the abstract setting with the same bound (Theorem 10.2), also in arbitrary dimension (Theorem 10.3). The proof of Theorem 1.3 does not completely carry over to the abstract setting, but our methods yield a similar statement (Theorem 10.4) with an upper bound of 10 + o ⁡ ( 1) 10+o(1).

Whether these methods generalize to order types with collinearities is a natural question; we see no easy answer, and consider this to be beyond the scope of this paper. Note, however, that for making the conclusion as in Theorem 1.1, the result for general position is more relevant. Actually, we conjecture that simple order types constitute only a (probably vanishingly) small proportion of all order types (potentially with collinearity), quite contrary to the situation for random order types sampled geometrically as described in Theorem 1.1.

### 1.2 Approach, terminology and further results

The gist of our method to establish Theorems 1.2 and 1.3 is to divide up the simple planar order types into classes, and average the number of extreme points inside each class.

#### 1.2.1 Setting and terminology

The division of order types into classes leverages a classical correspondence between points and lines in the plane ℝ 2 \mathbb{R}^{2}, and points and great circles on the origin-centered unit sphere 𝕊 2 \mathbb{S}^{2} in ℝ 3 \mathbb{R}^{3}. A *great circle*is the intersection of the sphere with a plane containing the origin 𝟎 \mathbf{0}, an *open hemisphere*is a connected component of the sphere in the complement of a great circle, and a *closed hemisphere*is the closure (in 𝕊 2 \mathbb{S}^{2}) of an open one. We call a finite set of points on the sphere an *affine set*if it is contained in an open hemisphere. The *sign*, χ ⁡ ( p, q, r) {\chi}(p,q,r), of a triple ( p, q, r) (p,q,r) of points on the sphere is the sign, − 1 -1, 0 0, or 1 1, of the determinant of the matrix ( p, q, r) ∈ ℝ 3 × 3 (p,q,r)\in\mathbb{R}^{3\times 3}. A bijection f: S → S ′ f:S\rightarrow S^{\prime} between finite subsets of the sphere is *orientation preserving*if χ ⁡ ( f ⁡ ( p), f ⁡ ( q), f ⁡ ( r)) = χ ⁡ ( p, q, r) {\chi}(f(p),f(q),f(r))={\chi}(p,q,r) for every triple of points in S S. Two affine sets have the *same affine order type*if there exists an orientation preserving bijection between them. An *affine**order type*is the equivalence class of all affine sets that have the same affine order type.

The plane ℝ 2 \mathbb{R}^{2} together with its orientation function can be mapped to any open hemisphere Γ \Gamma together with χ {\chi}, therefore relating order types (in ℝ 2 \mathbb{R}^{2}) to affine order types (in 𝕊 2 \mathbb{S}^{2}). Indeed, let t t denote the plane tangent to 𝕊 2 \mathbb{S}^{2} in the center of Γ \Gamma. Every affine transform from ℝ 2 \mathbb{R}^{2} to t t is of the form

 | ( x y) ↦ A ​ ( x y 1) \left(\begin{array}[]{c}x\\ y\end{array}\right)\mapsto A\left(\begin{array}[]{c}x\\ y\\ 1\end{array}\right) |  |

where A ∈ ℝ 3 × 3 A\in\mathbb{R}^{3\times 3} is non-singular. Let us fix such a transform with det A > 0 \det A>0, and compose it with a central projection of t t onto Γ \Gamma from 𝟎 \mathbf{0} (which amounts to normalizing the vector from t t). It is apparent from Equation ( 1) that the orientation χ ⁡ ( p, q, r) \chi(p,q,r) of three points in ℝ 2 \mathbb{R}^{2} coincides with the sign χ \chi of their images in Γ \Gamma. In particular, every such map sends every line to a semi-great circle, and a segment to a great-circle arc. Conversely, any open hemisphere can be mapped to ℝ 2 \mathbb{R}^{2} so that the sign χ \chi corresponds to the orientation function, semi-great circles are mapped to lines, and great-circle arcs are mapped to segments.

We divide up the affine order types into classes as follows. Two points p p and q q on the sphere are called *antipodal*if q = − p q=-p. A finite subset P P of the sphere is a *projective set*if p ∈ P ⇔ − p ∈ P p\in P\Leftrightarrow-p\in P. Starting from an affine n n -point set A A, we obtain the class of (the affine order type of) A A as the order types of all the affine n n -point sets that are contained in its *projective completion*A ∪ − A A\cup-A. 5 5 5 The reader familiar with projective geometry may check that two affine sets have the same projective completion if and only if there is a projective map that sends (a realization of) one to (a realization of) the other. In other words, each of our classes is the orbit of an order type under the action of projective maps. We illustrate this idea in Figure 2 and formalize it properly in Section 3.

Figure 2: A projective set of size 10 10 (left) containing the three simple affine order types of size 5 5.

This division into classes hints at yet another notion of order types, this time for projective point sets. Formally, two projective sets have *the same projective order type*if there exists an orientation preserving bijection between them. A *projective order type*is the equivalence class of all projective sets that have the same projective order type. We will represent the class of the affine order types of an affine set A A by the projective order type of A ∪ − A A\cup-A. The definitions of *labeled*affine and projective order types are similar: the ordering determines the bijection that is required to preserve orientations. It will sometimes be convenient to write a point sequence as A [λ] A_{[\lambda]}, where A A is the point set and λ: A → { 1, 2, …, n } \lambda:A\to\{1,2,\ldots,n\}, n = | A | n=|A|, the bijection specifying the ordering.

We take all our points on the origin-centered unit sphere 𝕊 2 \mathbb{S}^{2} in ℝ 3 \mathbb{R}^{3}, except for occasional mentions of the origin 𝟎 \mathbf{0}, and restrict our attention to affine and projective sets in general position. An affine set is in *general position*if no three points are coplanar with 𝟎 {\bf 0}; a projective set P P is in *general position*if whenever three points in P P are coplanar with 𝟎 \mathbf{0}, two of them are antipodal.

Let S S be a finite subset of the sphere. A *permutation*of S S is a bijection S → S S\to S and a *symmetry*of S S is an orientation preserving permutation of S S. The symmetries of S S form a group, which we call the *symmetry group*of S S. This group determines the relations between labeled and non-labeled order types: two orderings S [λ] S_{[\lambda]} and S [μ] S_{[\mu]} of a point set S S determine the same labeled order type if and only if μ − 1 ∘ λ \mu^{-1}\circ\lambda is a symmetry of S S.

#### 1.2.2 Further results

Given two order types ω \omega and τ \tau, we say that ω \omega*contains*τ \tau if any point set that realizes ω \omega contains a subset that realizes τ \tau. (Of course this needs only be checked for a single realization of ω \omega.) By the Erdös-Szekeres theorem [25], almost all order types contain the order type of k k points in convex position (since, for n n large enough, *all*order types have k k points in convex position). The relation between affine and projective order types reveals the following relative:

###### Theorem 1.4.

For any integer k ≥ 3 k\geq 3, the proportion of order types of size n n that contain k k points with 3 3 extreme points and the k − 3 k-3 inner points forming a convex chain together with one edge of the convex hull (see Figure 3) is 1 − O ⁡ ( 1 / n) 1-O(1/n).

Figure 3: Eight points with three extreme points and the five inner points forming a convex chain together with one edge of the convex hull.

A crucial ingredient in our proof of Theorem 1.3 is a classification of the symmetry groups of the affine and projective sets. Here it is for affine sets. (The definitions of layers, sometimes called onion layers, and lonely point are given in Section 2.3.)

###### Theorem 1.5.

The symmetry group of any affine set A A in general position is isomorphic to the cyclic group ℤ k \mathbb{Z}_{k} for some k ∈ ℕ k\in\mathbb{N} that divides the size of every layer of A A other than its lonely point (if A A has one). In particular, k k divides | A | |A| (if A A has no lonely point) or | A | − 1 |A|-1 (if A A has a lonely point); the latter can happen for k k odd only.

For all values of k k and n n satisfying k | n k\mid n, or k k odd and k | n − 1 k\mid n-1, with the exception of ( k, n) = ( 2, 4) (k,n)=(2,4), there exists an affine order type of size n n with ℤ k \mathbb{Z}_{k} as symmetry group (see Figure 4).

Figure 4: Left: For any even n ≥ 6 n\geq 6, there exists an affine set of n n points with symmetry group ℤ 2 \mathbb{Z}_{2}: take two sufficiently flat convex chains of n / 2 n/2 points each, facing each other (so-called double chain, [49]). Center and Right: For any 3 ≤ k ≤ n 3\leq k\leq n where k k divides n n or for any odd k k where k k divides n − 1 n-1, there exists an affine set of n n points with symmetry group ℤ k \mathbb{Z}_{k}: just pile up regular k k -gons inscribed in concentric circles.

We also prove that the symmetry groups of projective sets are finite subgroups of S ​ O ​ ( 3) SO(3).

###### Theorem 1.6.

The symmetry group of any projective set of 2 ​ n 2n points in general position is a finite subgroup of S ​ O ​ ( 3) SO(3). In particular, it is one of the following groups: ℤ 1 \mathbb{Z}_{1} (trivial group), ℤ m \mathbb{Z}_{m} (cyclic group), D m D_{m} (dihedral), with m | n m\mid n, or m | n − 1 m\mid n-1, S 4 S_{4} (octahedral = cubical), A 4 A_{4} (tetrahedral), and A 5 A_{5} (icosahedral).

We give examples of projective point sets with symmetry groups of each of the types identified in Theorem 1.6 (see Section 9.6).

### 1.3 Related work

We now briefly discuss previous works related to our results.

#### 1.3.1 Counting, enumerating and sampling order types

The space of order types is generally not well understood. To begin with, its size is not known, not even asymptotically. The most precise bounds are: there are n 4 ​ n ​ ϕ ​ ( n) n^{4n}\phi(n) labeled order types, where 2 − c ​ n ≤ ϕ ⁡ ( n) ≤ 2 c ′ ​ n 2^{-cn}\leq\phi(n)\leq 2^{c^{\prime}n} for some positive constants c, c ′ c,c^{\prime} [32, 4]. Factoring out the labeling requires to account for symmetries; we show that in the plane, every unlabeled order type corresponds to at least ( n − 1)! (n-1)! (and clearly at most n! n!) different labeled ones (Corollary 6.2). There is no known efficient algorithm for enumerating order types; in practice, they have been tabulated up to size 11 11 [2, 3], for which they are already counted in billions. 6 6 6 Recently, *abstract*order types have been counted up to size 13 13 by Rote and Scheucher, https://oeis.org/A006247.

Random sampling of order types is also quite unsatisfactory. First, the standard methods in discrete random generation such as Boltzmann samplers are unlikely to work here, as they require structural results (such as recursive decompositions) that usually make counting a routine task. It is of course easy to produce a random order type by merely reading off the order type of n n random points; standard models include points chosen independently from the uniform distribution in a square or a disk, from a Gaussian distribution, as well as points obtained as a random 2 2 -dimensional projection of a n n -dimensional simplex [15]. No random generation method is known to be both efficient (say, taking polynomial time per sample) and with controlled bias, and our Theorem 1.1 is the first negative result in this direction. This sad state of affairs can perhaps be explained by two fundamental issues: when working with order types symbolically (say as orientation maps to { − 1, 0, 1 } \{-1,0,1\}), one has to work around the NP-hardness (actually, ∃ ℝ \exists\mathbb{R} -completeness) of membership (i.e., realizability) testing [57, 47, 55]. When working with explicit point sets, one has to account for the exponential growth of the worst-case number of coordinate bits required to realize an order type of size n n [34]. It is an open question whether *most*order types can be realized using small (polynomial-size) coordinates (see Caraballo et al. [16] for recent progress).

#### 1.3.2 Random polytopes and Sylvester’s problem

Counting extreme points relates to the study of face vectors of random polytopes, a classical line of research in stochastic geometry initiated by Sylvester in 1865, who asked for “the probability that 4 4 points in the plane are in convex position”. A standard model of a random polytope K n K_{n} is the convex hull of n n random points chosen uniformly and independently in some fixed convex body K K. In this setting, the number of extreme points, i.e., of vertices of K n K_{n}, is well understood. Its average is asymptotically proportional to ( 1 + o ⁡ ( 1)) ​ n d − 1 d + 1 (1+o(1))n^{\frac{d-1}{d+1}} if K K is smooth and to ( 1 + o ⁡ ( 1)) ​ log d − 1 ​ n (1+o(1))\log^{d-1}n if K K is a polytope [52, 53] (see [51, § ​ 2.2.2 \mathsection 2.2.2]), and up to multiplicative constants these are the two extremes [8, Theorems 1–3]. There are also estimates on the variance, concentration inequalities, central limit theorems, and large deviation inequalities. We refer the interested reader to the survey of Reitzner [51].

This model of a random polytope naturally generalizes to arbitrary probability measures, or even to the convex hull of random dependent point sets such as determinantal point processes. Much less is known in this direction, aside from the occasional extensively-studied model such as Gaussian polytopes (see [51, § ​ 2.3 \mathsection 2.3]). In a sense, what we investigate is the average number of extreme points in a random polytope for a *combinatorially defined*probability distribution on point sets.

The study of random polytopes also relates to the ϵ \epsilon -net theory for halfspaces through the use of floating bodies [8] (see also [38] and [6, § ​ 3.2 \mathsection 3.2]). It also relates to graph drawing: Blaschke proved that the probability that 4 4 points chosen uniformly in a convex domain are in convex position is minimized when the domain is a triangle; for arbitrary planar probability measures, this merely asks for the limit as n → ∞ n\to\infty of the rectilinear crossing number of the complete graph.

#### 1.3.3 Symmetry groups of oriented matroids

The symmetry groups of oriented matroids of rank 2 2 and 3 3 were previously classified by Miyata [46]. Although phrased for realizable order types, our proof of Theorem 1.5 extends to abstract ones and offers an alternative to Miyata’s proof in the case of acyclic matroids [46, § ​ 6 \mathsection 6]. As we spell out in Section 10, some of our other proofs also extend to the abstract setting.

#### 1.3.4 Order types of random point sets

Several recent works have studied order types of random point sets [18, 21, 26, 37, 61], but they do not address the *equiprobable*distribution on n n -point order types. The recent work of Chiu et al. [20] comes closer, as they have looked at the average size of the j j th level in a random planar arrangement of n n lines, chosen by fixing a projective line arrangement of size n n and equiprobably choosing a random cell to contain the south-pole. This is similar to what we do, but let us stress that they do not take symmetries into account, so the actual distribution on planar arrangements they consider is not equiprobable (not even among those contained in the projective arrangement).

#### 1.3.5 Order types with forbidden patterns

Order types with forbidden patterns were previously investigated in several directions. The Erdős-Szekeres theorem was strengthened for order types with certain forbidden patterns [48, 40, 41]. Han et al. [37] studied the patterns contained in random samples. Eppstein [24] offers a beautiful small book about forbidden configurations, which concentrates on patterns in degenerate position (see Theorems 8.13, 8.16, 9.7, 11.22, and 12.3, and Lemma 15.14 in [24]). We are not aware of previous results on the number of order types with a forbidden pattern in general position such as Theorem 1.4.

### 1.4 Open problems

In our opinion, the most prominent open problem is the design of a method for generating pseudorandom order types that is both efficient (say, taking polynomial time per sample) and with controlled bias. Our methods reveal that this problem should perhaps be approached by sampling *projective order types*first, an idea that we discuss in Section 11. Here, let us say that one approach we believe *does not*work is the following (with the terminology of Theorem 1.1):

###### Conjecture 1.7.

Let μ \mu be a probability measure on ℝ 2 \mathbb{R}^{2} for which every line is negligible and such that the expected number of extreme points among n n random points chosen independently from μ \mu goes to infinity as n → ∞ n\to\infty. The family of probabilities on ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} defined by the (labeled) order type of n n random points chosen independently from μ \mu exhibits concentration.

We actually believe that a stronger conjecture holds.

###### Conjecture 1.8.

Let μ \mu be any probability measure on ℝ 2 \mathbb{R}^{2} for which every line is negligible. The family of probabilities on ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} defined by the (labeled) order type of n n random points chosen independently from μ \mu exhibits concentration.

We have only weak indicators for Conjecture 1.8. As it is easily seen, a distribution that exhibits perfect uniform distribution on all ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}, n ∈ ℕ n\in\mathbb{N}, for random points chosen independently from μ \mu is not possible, since random order types do not satisfy a “reducibility” condition which is true for any i.i.d. sampling, namely that removing random points from a random configuration gives a random configuration: For example, if we sample a random 5 5 -point order type, and then remove one of the five points at random, then we get the convex position 4 4 -point order type with probability 1 3 ​ ( 1 + 1 5 + 3 5) = 3 5 \frac{1}{3}\left(1+\frac{1}{5}+\frac{3}{5}\right)=\frac{3}{5} (check in Figure 1), and not 1 2 \frac{1}{2}, as we get it for a random 4 4 -point order type (see Figure 1). This irreducibility also implies, for instance, that for any distribution μ \mu on ℝ 2 \mathbb{R}^{2} there are two order types of size 6 6 whose probabilities differ by a factor of more than 1.8 1.8, see Goaoc et al. [30, Prop. 2]. Clearly, none of this implies concentration as n n grows.

One approach to bypass the ∃ ℝ \exists\mathbb{R} -completeness of testing realizability of order types is to work in a class of abstract order types that is not too large (having in mind that the number of abstract order types, e Ω ⁡ ( n 2) e^{\Omega(n^{2})}, grows much faster than the number of realizable ones, e O ⁡ ( n ​ log ⁡ n) e^{O(n\log n)}). A natural way to filter out abstract order types is to forbid them from containing patterns violating certain “affine theorems”.

###### Question 1.9.

Is it true that for any *fixed*(abstract) order type τ \tau, the number of (abstract) order types of size n n that *do not*contain τ \tau is vanishingly small as n → ∞ n\to\infty?

The answer is positive for τ \tau the order type of points in convex position (the Erdös-Szekeres theorem [25]), a triangle with one interior point (Carathéodory’s theorem) and a triangle with a convex chain over an edge (Figure 3, Theorem 1.4). The question may seem quite bold given the limited number of observations, but it is also motivated by an analogous phenomenon for permutations: the Marcus-Tardos theorem [45] asserts that for every fixed permutation π \pi, the number of size- n n permutations that *do not*contain π \pi is at most exponential in n n (see [45] for the definition of containment).

The paper by Aloupis et al. [5] addresses the complexity of order type isomorphism via so-called canonical labelings, improving bounds by Goodman and Pollack [31]. They describe an O ⁡ ( n d) O(n^{d}) time algorithm for computing the automorphisms of an order type (what we will call the symmetry group of orientation preserving permutations) for a set of n n points in ℝ d \mathbb{R}^{d} (or an acyclic oriented matroid of rank d + 1 d+1 given by an orientation oracle), [5, Theorem 4.1]. While in [5] evidence is given that O ⁡ ( n d) O(n^{d}) is optimal for deciding whether two point sets have the same order type, it is not excluded that the symmetry group of a point set can be computed faster, at least for small d d.

### 1.5 Paper organization

We recall some background material in Section 2. The paper is then organized in three parts:

- •

Sections 3 and 4 deal with labeled affine order types. Section 3 clarifies the relation between affine and projective order types, between their symmetry groups, and between the affine subsets of a projective sets and the cells of its dual arrangement. Section 4 proves Theorem 1.2 by relating the number of extreme points in a random affine order type to the number of edges in a random cell of an arrangement of great circles, and by analyzing such arrangements via double counting and the zone theorem.

- •

Sections 5 and 6 deal with affine order types. Section 5 proves that every symmetry of a projective set stabilizes exactly two subsets contained in a closed hemisphere – a combinatorial analogue of the property that any rotation in ℝ 3 \mathbb{R}^{3} fixes two points of the sphere. This allows us, in Section 6, to extract some information on projective symmetry groups by adapting the analysis of Klein leading to the classification of finite subgroups of S ​ O ​ ( 3) SO(3). We then analyze affine symmetries, proving Theorem 1.5, and establish Theorem 1.3.

- •

The last five sections are independent complements to Theorems 1.2 and 1.3. Section 7 relates concentration results on extreme points to concentration on the distribution of order types, and proves Theorem 1.1. Section 8 uses the projective setup to extend, in some sense, the Erdös-Szekeres theorem and prove Theorem 1.4. Section 9 completes the study of projective symmetries into the characterization of Theorem 1.6 and discusses some of its extensions. Section 10 presents generalizations of Theorems 1.2 and 1.3 to higher dimensions and to abstract order types (that is, acyclic uniform oriented matroids). Section 11 discusses how projective order types may help sampling (labeled) order types efficiently.

## 2 Background

We recall here some notions in finite group theory and in discrete geometry on 𝕊 2 \mathbb{S}^{2} (duality, arrangements, convexity).

### 2.1 Groups

The elements of group theory we use deal with a subgroup G G of the group of permutations of a finite set X X. The identity map, the neutral element in G G, is denoted by 𝗂𝖽 {\sf id} or 𝗂𝖽 X {\sf id}_{X}. We will study such a group G G through its action on X X or some set of subsets of X X. The *orbit*G ⁡ ( x) G(x) of x ∈ X x\in X is the image of x x under G G, i.e., G ⁡ ( x) = def { g ⁡ ( x) ∣ g ∈ G } G(x)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{g(x)\mid g\in G\}. Any two elements have disjoint or equal orbits, so the orbits partition X X. The *stabilizer*of an element x ∈ X x\in X is the set of permutations in G G having x x as a fixed point, i.e., G x = def { g ∈ G ∣ g ⁡ ( x) = x } G_{x}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{g\in G\mid g(x)=x\}. The *orbit-stabilizer theorem asserts that for any group G G acting on a set X X,*| G | = | G ⁡ ( x) | ⋅ | G x | |G|=|G(x)|\cdot|G_{x}| for every x ∈ X x\in X. We write ≃ \simeq for group isomorphism.

### 2.2 Duality and arrangements on 𝕊 2 \mathbb{S}^{2}

On the sphere, the *dual*of a point p p is the great circle p ∗ p^{*} contained in the plane through 𝟎 {\bf 0} and orthogonal to the line 𝟎 ​ p \mathbf{0}p. For any finite subset S S of the sphere, we write S ∗ S^{*} for the arrangement of the family of great circles { p ∗ ∣ p ∈ S } \{p^{*}\mid p\in S\}.

Let P P be a projective set of 2 ​ n 2n points in general position. Since antipodal points have the same dual great circle, P ∗ P^{*} is an arrangement of n n great circles. Observe that P P is in general position if and only if no three great circles in P ∗ P^{*} have a point in common. Any two great circles intersect in two points, so P ∗ P^{*} has 2 ​ ( n 2) 2{n\choose 2} vertices. Every vertex is incident to four edges; the total number of edges is therefore 4 ​ ( n 2) 4{n\choose 2}. By Euler’s formula, P ∗ P^{*} has 2 ​ ( n 2) + 2 2{n\choose 2}+2 faces of dimension 2 2, which we call *cells*.

Let us recall that many combinatorial quantities on arrangements of great circles on 𝕊 2 \mathbb{S}^{2} are essentially twice their analogues for arrangements of lines in ℝ 2 \mathbb{R}^{2}. Indeed, starting with an arrangement P ∗ P^{*} of n n great circles in general position, we can add another great circle C ∞ C_{\infty}, chosen so that P ∗ ∪ { C ∞ } P^{*}\cup\{C_{\infty}\} is also in general position, and consider the two open hemispheres bounded by C ∞ C_{\infty}. Each open hemisphere can be mapped to ℝ 2 \mathbb{R}^{2} by a central projection onto a plane parallel to C ∞ C_{\infty}, so that the half-circles of P ∗ P^{*} are turned into lines, and the two line arrangements are combinatorially equivalent by antipodality. In this way, we can for instance obtain the following version of the zone theorem from the bound given in [12] for the zone of a line in an arrangement of lines: 7 7 7 In [12] it is shown that the cells in the zone of a line h 0 h_{0} in an arrangement of n + 1 n+1 lines in the plane has edge-complexity at most ⌊ 19 ​ n / 2 ⌋ − 1 \lfloor 19n/2\rfloor-1. For translating this bound to the zone of a great circle in an arrangement of n n great circles on 𝕊 2 \mathbb{S}^{2}, (i) we replace n n by n − 1 n-1, (ii) we double for the two sides of C ∞ C_{\infty}, and (iii) we subtract 8 for the edges that get merged along C ∞ C_{\infty} (note that the infinite edges on h 0 h_{0} get merged and contribute 1 on each of their sides). Note that the unpublished manuscript http://www2.math.technion.ac.il/~room/ps_files/zonespl.pdf by Rom Pinchasi improves the bound in [12] by 2 to ⌊ 19 ​ n / 2 ⌋ − 3 \lfloor 19n/2\rfloor-3.

###### Theorem 2.1 (Zone Theorem).

Let P ∗ P^{*} be an arrangement of n n great circles on 𝕊 2 \mathbb{S}^{2} and let p ∗ ∈ P ∗ p^{*}\in P^{*}. Let Z ⁡ ( p ∗) Z(p^{*}) denote the *zone*of p ∗ p^{*}, i.e., the set of cells of the arrangement incident to p ∗ p^{*}. For a cell c c, let | c | |c| denote the number of edges incident to c c. Then ∑ c ∈ Z ⁡ ( p ∗) | c | ≤ 19 ​ ( n − 1) − 10 \sum_{c\in Z(p^{*})}|c|\leq 19(n-1)-{{10}}.

### 2.3 Convexity on the sphere

A point p ∈ A p\in A is *extreme*in an affine set A A if there exists a great circle C C that strictly separates p p from A ∖ { p } A\setminus\{p\}; that is, p p and A ∖ { p } A\setminus\{p\} lie in two different connected components of 𝕊 2 ∖ C \mathbb{S}^{2}\setminus C. An ordered pair ( p, q) ∈ A 2 (p,q)\in A^{2}, p ≠ q p\neq q, is a *positive extreme edge*of A A if for all r ∈ A ∖ { p, q } r\in A\setminus\{p,q\} we have χ ⁡ ( p, q, r) = + 1 {\chi}(p,q,r)=+1. Assuming general position and | A | ≥ 2 |A|\geq 2, a point p ∈ A p\in A is extreme in A A if and only if there exists q ∈ A q\in A such that ( p, q) (p,q) is a positive extreme edge; in that case, the point q q is unique.

A *CCW order*of the extreme points of A A is an order ( p 0, p 1, …, p h − 1) (p_{0},p_{1},\ldots,p_{h-1}) of its extreme points such that for all i = 0, 1, …, h − 1 i=0,1,\ldots,h-1, ( p i, p i + 1) (p_{i},p_{i+1}) is a positive extreme edge (indices mod h \bmod\,h). The *convex hull*of A A is

 | 𝖼𝗈𝗇𝗏 ⁡ ( A) = def ⋂ closed hemisphere ​ Σ ⊇ A Σ {\sf conv}(A)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\bigcap_{\text{closed hemisphere\,}{\Sigma}\supseteq A}{\Sigma} |  |

which equals, for A A in general position and | A | ≥ 3 |A|\geq 3,

 | { r ∈ 𝕊 2 ∣ ∀ positive extreme edges ( p, q), χ ( p, q, r) ≥ 0 }. \{r\in\mathbb{S}^{2}\mid\forall\hbox{ positive extreme edges }(p,q),{\chi}(p,q,r)\geq 0\}. |  |

An affine set A A is *in convex position*if every point is extreme in A A. The (onion) *layer sequence*of A A is a sequence ( A 0, A 1, …, A ℓ) (A_{0},A_{1},\ldots,A_{\ell}) of subsets of A A, partitioning A A, where A 0 A_{0} is the set of extreme points in A A, and ( A 1, A 2, …, A ℓ) (A_{1},A_{2},\ldots,A_{\ell}) is the layer sequence of A ∖ A 0 A\setminus A_{0} (if A = ∅ A=\emptyset, then the layer sequence is empty). The A i A_{i} ’s are called the *layers*of A A. If the innermost layer A ℓ A_{\ell} consists of a sole point, then that point is called *lonely*. There is one or no lonely point.

## 3 Hemisets: relating affine and projective order types

Any affine set A A naturally defines a projective set A ∪ − A A\cup-A, which we call its *projective completion*. Going in the other direction, we define a *hemiset*of a projective set P P as the intersection of P P with a *closed*hemisphere, and call a hemiset of P P an *affine hemiset*of P P if it is contained in an open hemisphere (or, equivalently for general position, a hemiset that contains no antipodal pair). With these definitions, we have:

###### Lemma 3.1.

A projective set P P is the projective completion of an affine set A A if and only if A A is an affine hemiset of P P.

*Proof.*Let P P be a projective set and let A A be an affine set. If P = A ∪ − A P=A\cup-A, then any open hemisphere Σ \Sigma that contains A A has no point of P P on its boundary, and the closure of Σ \Sigma intersects P P in A A. Conversely, if A = Σ ∩ P A=\Sigma\cap P for some closed hemisphere Σ \Sigma, then every point p ∈ P ∖ A p\in P\setminus A must be in interior of − Σ -\Sigma, so that − p ∈ P ∩ Σ = A -p\in P\cap\Sigma=A and P = A ∪ − A P=A\cup-A.

We note that an affine set is in general position if and only if its projective completion is. Although we are primarily interested in affine hemisets, it will be instrumental to consider also hemisets that are not affine. Note that for an open hemisphere to cut out an affine set that completes to P P, it must be bounded by a great circle that avoids P P. For instance, the set of vertices of the cross polytope P = def { ( ± 1, 0, 0), ( 0, ± 1, 0), ( 0, 0, ± 1) } P\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{(\pm 1,0,0),(0,\pm 1,0),(0,0,\pm 1)\} intersects some open hemispheres in a single point.

##### Notation.

Now seems a good time to introduce or recall our notation. For n ≥ 3 n\geq 3 we write 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} for the set of simple labeled affine order types of size n n, 𝖮𝖳 aff n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} for the set of simple affine order types of size n n, and 𝖮𝖳 proj n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n} for the set of simple projective order types of size 2 ​ n 2n. For an affine point set A A with affine order type ω \omega, we write 𝖫𝖮𝖳 aff A = 𝖫𝖮𝖳 aff ω {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!A}={\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\omega} for the set of the labeled affine order types of the orderings of A A. For a projective point set P P with projective order type π \pi, we write ( 𝖫) 𝖮𝖳 P aff = ( 𝖫) 𝖮𝖳 π aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}={\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi} for the set of affine (labeled) order types of the affine hemisets of P P.

### 3.1 Symmetries acting on hemisets

To understand how affine order types relate to projective order types, an important idea is that the symmetries of a projective point set P P act on the (affine) hemisets of P P. This action also carries the following structure. We define the *layer sequence*of a hemiset B B of a projective set P P as the sequence ( B − 1, B 0, B 1, …, B ℓ) (B_{-1},B_{0},B_{1},\ldots,B_{\ell}) of subsets of B B, where B − 1 = def B ∩ − B B_{-1}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}B\cap-B, and ( B 0, B 1, …, B ℓ) (B_{0},B_{1},\ldots,B_{\ell}) is the layer sequence of the affine set B ∖ B − 1 B\setminus B_{-1}. In particular, B − 1 = ∅ B_{-1}=\emptyset if and only if B B is an affine hemiset. 8 8 8 When the context makes it clear that we are dealing with affine sets, we may drop the term B − 1 B_{-1} for affine sets to fall back on the definition of layer sequence given in Section 2.3. If the innermost layer B ℓ B_{\ell} consists of a sole point, then that point is called *lonely*.

###### Proposition 3.2.

Let g: P → P ′ g:P\to P^{\prime} be an orientation preserving bijection between two projective sets in general position, | P | = | P ′ | ≥ 6 |P|=|P^{\prime}|\geq 6.

1. (i)

g g maps hemisets of P P to hemisets of P ′ P^{\prime} and affine hemisets of P P to affine hemisets of P ′ P^{\prime}.

2. (ii)

If a hemiset B B of P P has layer sequence ( B − 1, B 0, B 1, …, B ℓ) (B_{-1},B_{0},B_{1},\ldots,B_{\ell}), then its image g ⁡ ( B) g(B) has layer sequence ( g ⁡ ( B − 1), g ⁡ ( B 0), g ⁡ ( B 1), …, g ⁡ ( B ℓ)) \left(g(B_{-1}),g(B_{0}),g(B_{1}),\ldots,g(B_{\ell})\right).

The rest of this section is devoted to the proof of Proposition 3.2. We start with a basic lemma. 9 9 9 The lemma basically states that if the points on 𝕊 2 \mathbb{S}^{2} are considered as vectors in ℝ 3 \mathbb{R}^{3}, then orientation preserving bijections map sets of convexly dependent vectors to sets of convexly dependent vectors.

###### Lemma 3.3.

Let g: S → S ′ g:S\to S^{\prime} be an orientation preserving bijection between two subsets S S and S ′ S^{\prime} of the sphere, with S S not contained in a great circle.

1. (i)

If { p, − p } \{p,-p\} is a pair of antipodal points in S S, then g ⁡ ( − p) = − g ⁡ ( p) g(-p)=-g(p).

2. (ii)

If X X is a set of points in S S whose convex hull (in ℝ 3 \mathbb{R}^{3}) contains 𝟎 \mathbf{0} in its interior, then the convex hull of g ⁡ ( X) g(X) contains 𝟎 \mathbf{0} in its interior.

*Proof.*(i) We have g ⁡ ( − p) ≠ g ⁡ ( p) g(-p)\neq g(p) since g g is bijective. If g ⁡ ( − p) g(-p) and g ⁡ ( p) g(p) are not antipodal, then they span a unique great circle C {C}. For r ∈ S ′ r\in S^{\prime} we have 0 = χ ⁡ ( p, − p, g − 1 ​ ( r)) = χ ⁡ ( g ⁡ ( p), g ⁡ ( − p), r) 0={\chi}(p,-p,g^{-1}(r))={\chi}\left(g(p),g(-p),r\right), i.e., all points in S ′ S^{\prime} lie on C {C}, and therefore all points in S S lie on a great circle, contrary to our assumption.

(ii) The convex hull of X X contains 𝟎 \mathbf{0} in its interior if and only if there exists a pair of *non-antipodal*points in X X and for any two non-antipodal points p p and q q in X X, the plane spanned by p p, q q, and 𝟎 \mathbf{0} has points r ′ r^{\prime} and r ′′ r^{\prime\prime} in X X on opposite sides, i.e., 0 ≠ χ ⁡ ( p, q, r ′) = − χ ⁡ ( p, q, r ′′) 0\neq{\chi}(p,q,r^{\prime})=-{\chi}(p,q,r^{\prime\prime}). Clearly, also with (i), this property is preserved by an orientation preserving bijection.

This readily gives a more local characterization of (affine) hemisets:

###### Corollary 3.4.

Let P P be a projective set in general position with | P | ≥ 6 |P|\geq 6. A subset B ⊆ P B\subseteq P is a hemiset of P P if and only if (a) B B contains at least one point of every antipodal pair in P P, and (b) the convex hull of B B does not contain 𝟎 \mathbf{0} in its interior. Moreover, a hemiset B B of P P is affine if and only if (c) | B | = | P | / 2 |B|=|P|/2.

*Proof.*Conditions (a) and (b) are clearly necessary so let us argue they are sufficient. Condition (b) shows that B B is contained in a closed halfspace with 𝟎 \mathbf{0} on its boundary, i.e., there is a closed hemisphere Σ ⊇ B {\Sigma}\supseteq B. Suppose Σ ∩ P ≠ B {\Sigma}\cap P\neq B, i.e., there is a point p ∈ Σ ∩ P p\in{\Sigma}\cap P not in B B. Since − p ∈ B -p\in B by (a), p p and − p -p must lie on the boundary of Σ {\Sigma} and, therefore, by the general position assumption, there are at most two such points p p. An appropriate perturbation of Σ {\Sigma} yields a closed hemisphere Σ ′ {\Sigma}^{\prime} with Σ ′ ∩ P = B {\Sigma}^{\prime}\cap P=B and thus B B is indeed a hemiset. From (a) it follows that a hemiset B B of P P is affine if and only if | B | = | P | / 2 |B|=|P|/2.

The fact that symmetries of a projective point set P P act on its hemisets and on its affine hemisets is now apparent.

###### Proof of Proposition 3.2.

Statement (i) follows from the observation that Conditions (a), (b) and (c) from Corollary 3.4 are preserved under orientation preserving bijections.

Let us now consider a hemiset B B of P P with layer sequence ( B − 1, B 0, B 1, …, B ℓ) (B_{-1},B_{0},B_{1},\ldots,B_{\ell}). Let B ′ = def g ⁡ ( B) B^{\prime}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}g(B) and let ( B − 1 ′, B 0 ′, B 1 ′, …, B ℓ ′ ′) (B_{-1}^{\prime},B_{0}^{\prime},B_{1}^{\prime},\ldots,B_{\ell^{\prime}}^{\prime}) denote the layer sequence of the hemiset B ′ B^{\prime}. By Lemma 3.3 (i), for any p ∈ B ∩ − B p\in B\cap-B we have g ⁡ ( { − p, p }) = { − g ⁡ ( p), g ⁡ ( p) } g(\{-p,p\})=\{-g(p),g(p)\} so g ⁡ ( B ∩ − B) ⊆ B ′ ∩ − B ′ g(B\cap-B)\subseteq B^{\prime}\cap-B^{\prime}. In particular, | B ∩ − B | ≤ | B ′ ∩ − B ′ | |B\cap-B|\leq|B^{\prime}\cap-B^{\prime}|. By a similar argument we have g − 1 ​ ( B ′ ∩ − B ′) ⊆ B ∩ − B g^{-1}(B^{\prime}\cap-B^{\prime})\subseteq B\cap-B, therefore | B ∩ − B | = | B ′ ∩ − B ′ | |B\cap-B|=|B^{\prime}\cap-B^{\prime}| and B − 1 ′ = g ⁡ ( B − 1) B_{-1}^{\prime}=g(B_{-1}). Now, g g maps the affine set B ∖ B − 1 B\setminus B_{-1} to the affine set B ′ ∖ B − 1 ′ B^{\prime}\setminus B_{-1}^{\prime}. Since g g is order preserving, it must map every positive extreme edge to a positive extreme edge, and therefore g ⁡ ( B 0) = B 0 ′ g(B_{0})=B_{0}^{\prime} (here, again, we use g − 1 g^{-1} for one of the inclusions). By induction, for every i ≥ − 1 i\geq-1, g g maps B ∖ ∪ j = − 1 j = i B j B\setminus\cup_{j=-1}^{j=i}B_{j} to B ′ ∖ ∪ j = − 1 j = i B j ′ B^{\prime}\setminus\cup_{j=-1}^{j=i}B_{j}^{\prime}, and therefore maps B i + 1 B_{i+1}, the extreme points of the former, to B i + 1 ′ B_{i+1}^{\prime}, the extreme points of the latter. Statement (ii) follows. ∎

### 3.2 Orbit and stabilizer of a hemiset

Given a projective set P P with symmetry group 𝖦 {\sf G} and a subset S S of P P, we write 𝖦 S {\sf G}_{S} for the stabilizer of S S in the action of 𝖦 {\sf G} on subsets of P P. We also write 𝖦 ⁡ ( S) {\sf G}(S) for the orbit of S S in that action. (Note that in the following lemma, we do allow S S to contain antipodal pairs.)

###### Lemma 3.5.

Let P = def S ∪ − S P\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}S\cup-S for a finite S ⊆ 𝕊 2 S\subseteq\mathbb{S}^{2} not contained in a great circle and let 𝖦 {\sf G} denote the symmetry group of P P.

1. (a)

The symmetry group of S S is isomorphic to 𝖦 S {\sf G}_{S}.

2. (b)

Given S ′ ⊆ P S^{\prime}\subseteq P, there is an order preserving bijection from S S to S ′ S^{\prime} if and only if S ′ ∈ 𝖦 ⁡ ( S) S^{\prime}\in{\sf G}(S).

*Proof.*Let 𝖥 {\sf F} denote the symmetry group of S S. Note that since S S is not contained in a great circle, by Lemma 3.3 (i) any f ∈ 𝖥 f\in{\sf F} preserves antipodality for any antipodal pair occurring in S S. Since P = S ∪ − S P=S\cup-S, we can extend any f ∈ 𝖥 f\in{\sf F} to a permutation f ^ \hat{f} of P P by setting f ^ ​ ( p) = def f ​ ( p) \hat{f}(p)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}f(p) for p ∈ S p\in S and f ^ ​ ( p) = def − f ​ ( − p) \hat{f}(p)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}-f(-p) for p ∉ S p\notin S. Let 𝖥 ^ = def { f ^ ∣ f ∈ 𝖥 } \hat{{\sf F}}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{\hat{f}\mid f\in{\sf F}\}. We have that 𝖥 ^ \hat{{\sf F}} is isomorphic to 𝖥 {\sf F} since f 1 ∘ f 2 ^ = f 1 ^ ∘ f 2 ^ \widehat{f_{1}\circ f_{2}}=\widehat{f_{1}}\circ\widehat{f_{2}} for any two symmetries f 1, f 2 f_{1},f_{2} of S S. Moreover, any element g ∈ 𝖥 ^ g\in\hat{{\sf F}} fixes S S and, conversely, any symmetry g: P → P g:P\to P that fixes S S writes g = g | S ^ g=\widehat{g|_{S}} (by Lemma 3.3 (i)). Then, 𝖥 ^ = 𝖦 S \hat{{\sf F}}={\sf G}_{S} and statement (a) follows.

For statement (b), note that for any orientation preserving bijection f: S → S ′ f:S\to S^{\prime}, the extension f ^ \hat{f} of f f to P P also preserves orientations, and is therefore in 𝖦 {\sf G}. It follows that S ′ ∈ 𝖦 ⁡ ( S) S^{\prime}\in{\sf G}(S). The reverse inclusion is immediate since every symmetry of 𝖦 {\sf G} preserves orientations.

With Lemma 3.5, specialized to affine hemisets of a projective set P P, the orbit-stabilizer theorem readily implies:

###### Corollary 3.6.

Let P P be a projective set of 2 ​ n 2n points, n ≥ 3 n\geq 3, in general position and A A an affine hemiset of P P. Let 𝖥 {\sf F} and 𝖦 {\sf G} denote the symmetry groups of A A and P P, respectively. There are | 𝖦 | / | 𝖥 | |{\sf G}|/|{\sf F}| affine hemisets of P P with the same affine order type as A A.

### 3.3 How many points determine an order preserving bijection?

We conclude this section with a basic fact about order preserving bijections and symmetries (see, e.g., [5] for similar observations).

###### Claim 3.7.

For P P a projective set in general position and for S ⊆ P S\subseteq P not contained in a great circle, let f: S → S f\!:S\rightarrow S be a symmetry of S S with f ⁡ ( p) = p f(p)=p and f ⁡ ( q) = q f(q)=q for some p, q ∈ S p,q\in S, q ∉ { p, − p } q\notin\{p,-p\}. Then f = 𝗂𝖽 S f={\sf id}_{S}.

*Proof.*For r ∈ S ∖ { p, q } r\in S\setminus\{p,q\} we want to show f ⁡ ( r) = r f(r)=r. Suppose first that χ ⁡ ( p, q, r) = 0 {\chi}(p,q,r)=0, i.e., r ∈ { − p, − q } r\in\{-p,-q\}; r = − p r=-p, say. Then, by Lemma 3.3 (i), f ⁡ ( r) = f ⁡ ( − p) = − f ⁡ ( p) = − p = r f(r)=f(-p)=-f(p)=-p=r.

Suppose next that χ ⁡ ( p, q, r) ≠ 0 {\chi}(p,q,r)\neq 0; χ ⁡ ( p, q, r) = 1 {\chi}(p,q,r)=1, say. Let k k be the smallest positive integer with f k ​ ( r) = r f^{k}(r)=r. We need to show k = 1 k=1. Obviously, for R = def { p, q, r, f ⁡ ( r), … ​ f k − 1 ​ ( r) } R\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{p,q,r,f(r),\ldots f^{k-1}(r)\}, f | R f|_{R} is an orientation preserving bijection on R R. R R is an affine set with ( p, q) (p,q) a positive extreme edge of R R, thus p p is extreme in R R and there is a unique positive edge ( r ′, p) (r^{\prime},p) for some r ′ ∈ R r^{\prime}\in R. ( q, p) (q,p) cannot possibly be a positive extreme edge of R R since χ ⁡ ( q, p, r) = − 1 {\chi}(q,p,r)=-1. Hence, ( r ′, p) = ( f i ​ ( r), p) (r^{\prime},p)=(f^{i}(r),p) for some i i. f | R f|_{R} must map this edge to a positive extreme edge of R R, which, since f ⁡ ( p) = p f(p)=p, shows f i + 1 ​ ( r) = f i ​ ( r) f^{i+1}(r)=f^{i}(r), forcing k = 1 k=1.

###### Lemma 3.8.

Let P P and P ′ P^{\prime} be projective sets in general positions, with | P | = | P ′ | ≥ 6 |P|=|P^{\prime}|\geq 6. Let B B and B ′ B^{\prime} be hemisets of P P and P ′ P^{\prime}, resp., and let p ∈ B p\in B and p ′ ∈ B ′ p^{\prime}\in B^{\prime}. Unless p p is lonely in B B, there is at most one order preserving bijection B → B ′ B\rightarrow B^{\prime} that maps p p to p ′ p^{\prime}.

*Proof.*Let f 1 f_{1} and f 2 f_{2} be order preserving bijections B → B ′ B\rightarrow B^{\prime} with f 1 ​ ( p) = f 2 ​ ( p) = p ′ f_{1}(p)=f_{2}(p)=p^{\prime}. Then f = def f 1 ∘ f 2 − 1 f\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}f_{1}\circ f_{2}^{-1} is a symmetry of B B with f ⁡ ( p) = p f(p)=p. We have f 1 = f 2 f_{1}=f_{2} if and only if f = 𝗂𝖽 B f={\sf id}_{B}. Assuming that p p is not lonely, we want to show f = 𝗂𝖽 B f={\sf id}_{B}. Note right away that hemisets of projective sets P P in general position with | P | ≥ 6 |P|\geq 6 cannot be contained in a great circle.

For i = − 1, 0, 1, … i=-1,0,1,\ldots, we let B i B_{i} denote the i i th layer of B B. By Proposition 3.2, f f preserves layers (i.e., f ⁡ ( B i) = B i f(B_{i})=B_{i} for all i i).

Let us first deal with the case where p ∈ B i p\in B_{i} with i ≠ − 1 i\neq-1. Since p p is not lonely, there is a unique point q q such that ( p, q) (p,q) is a positive extreme edge of B i B_{i}. Clearly, its image ( f ⁡ ( p), f ⁡ ( q)) (f(p),f(q)) is a positive extreme edge of B i B_{i}. Since f ⁡ ( p) = p f(p)=p, we have f ⁡ ( q) = q f(q)=q. Since B B cannot be contained in a great circle, Claim 3.7 shows f = 𝗂𝖽 B f={\sf id}_{B}.

Next we assume p ∈ B − 1 p\in B_{-1}. Then − p ∈ B − 1 ⊆ B -p\in B_{-1}\subseteq B and f ⁡ ( − p) = − f ⁡ ( p) = − p f(-p)=-f(p)=-p (Lemma 3.3 (i)). Set B ′′ = def B ∖ { − p } B^{\prime\prime}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}B\setminus\{-p\}. Since − p ∉ B ′′ -p\not\in B^{\prime\prime}, p p is not in the layer − 1 -1 of B ′′ B^{\prime\prime}. Actually, p p has to be in layer 0 0. If p p is not lonely in B ′′ B^{\prime\prime}, the argument in the previous paragraph shows that f | B ′′ = 𝗂𝖽 B ′′ f|_{B^{\prime\prime}}={\sf id}_{B^{\prime\prime}} which entails f = 𝗂𝖽 B f={\sf id}_{B}. If p p is lonely in B ′′ B^{\prime\prime}, then B ′′ = { p } B^{\prime\prime}=\{p\} or B ′′ = { q, − q, p } B^{\prime\prime}=\{q,-q,p\} for some point q q. But then B = { p, − p } B=\{p,-p\} or B = { q, − q, p, − p } B=\{q,-q,p,-p\} which is not possible for hemisets as postulated in the assertion.

Lemma 3.8 implies that for any hemiset B B of a projective set of at least 6 6 points in general position, only 𝗂𝖽 B {\sf id}_{B} fixes a non-lonely point. Moreover, if B B is non-affine then it has at most 4 4 symmetries; see Lemma 9.1 for more.

## 4 Analysis of labeled affine order types

Perhaps surprisingly, Corollary 3.6 is all we need to prove Theorem 1.2. Once this is done, the reader interested in proving Theorem 1.1 for labeled order types only can skip Sections 5 and 6 and proceed to Section 7.

### 4.1 The two roles of affine symmetries

The number of symmetries of an affine order type determines both its number of labelings, and how often it occurs among the affine hemisets of a projective completion of one of its realizations. These two roles happen to balance each other out nicely:

###### Proposition 4.1.

Let P P be a projective set of 2 ​ n 2n points, n ≥ 3 n\geq 3, in general position. Let R R be a random affine hemiset chosen uniformly among all affine hemisets of P P. Let λ \lambda be a random permutation R → { 1, 2, …, n } R\to\{1,2,\ldots,n\} chosen uniformly among all such permutations. The labeled affine order type of R [λ] R_{[\lambda]} is uniformly distributed in 𝖫𝖮𝖳 aff P {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}.

*Proof.*Let N N denote the number of affine hemisets of P P. Let ω 1, ω 2, …, ω k \omega_{1},\omega_{2},\ldots,\omega_{k}, k ≤ N k\leq N, denote the order types of the affine hemisets of P P, without repetition (that is, the ω i \omega_{i} are pairwise distinct). Let 𝖦 {\sf G} denote the symmetry group of P P and let 𝖥 i {\sf F}_{i}, 1 ≤ i ≤ k 1\leq i\leq k, denote the symmetry group of ω i \omega_{i}. Let ρ \rho denote the affine order type of R R. By Corollary 3.6, we have

 | ℙ [ρ = ω i] = | 𝖦 | / | 𝖥 i | N. \mathbb{P}\left[\rho=\omega_{i}\right]=\frac{|{\sf G}|/|{\sf F}_{i}|}{N}. |  |

Next, the number of distinct labelings of the order type of an affine set A A is n! / | 𝖥 A | n!/|{\sf F}_{A}|, since two labelings A [λ] A_{[\lambda]} and A [μ] A_{[\mu]} of A A have the same labeled order type if and only if μ − 1 ∘ λ \mu^{-1}\circ\lambda is a symmetry of A A. Let ρ ¯ \overline{\rho} denote the labeled affine order type of R [λ] R_{[\lambda]}. For any σ ¯ ∈ 𝖫𝖮𝖳 aff ω i \overline{\sigma}\in{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\omega_{i}}, we have

 | ℙ ⁡ [ρ ¯ = σ ¯ ∣ ρ = ω i] = | 𝖥 i | n!. \mathbb{P}\left[\overline{\rho}=\overline{\sigma}\mid\rho=\omega_{i}\right]=\frac{|{\sf F}_{i}|}{n!}. |  |

Altogether, for any σ ¯ ∈ ⋃ i = 1 k 𝖫𝖮𝖳 aff ω i = 𝖫𝖮𝖳 aff P \overline{\sigma}\in\displaystyle\bigcup_{i=1}^{k}{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\omega_{i}}={\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}, we have

 | ℙ [ρ ¯ = σ ¯] = | 𝖦 | N ​ n! \mathbb{P}\left[\overline{\rho}=\overline{\sigma}\right]=\frac{|{\sf G}|}{Nn!} |  |

and the distribution is uniform as we claimed. This also shows that | 𝖫𝖮𝖳 aff P | = N ​ n! | 𝖦 | |{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}|=\frac{Nn!}{|{\sf G}|} which will come handy later in the paper.

### 4.2 Hemisets and duality

The following dualization will make counting easy.

###### Lemma 4.2.

There is a bijection ϕ \phi between the affine hemisets of a projective point set P P and the cells of the dual arrangement P ∗ P^{*}, such that a point p p is extreme in an affine hemiset A A if and only if the great circle p ∗ p^{*} supports an edge of ϕ ⁡ ( A) \phi(A).

*Proof.*For any point p p we write p + p^{+} for the hemisphere centered in p p, that is, the closed hemisphere containing p p and bounded by p ∗ p^{*}. For any closed hemisphere Σ {\Sigma} we write Σ + {\Sigma}^{+} for its center, that is, the point q q with Σ = q + {\Sigma}=q^{+}. Now, a point p p is in a closed hemisphere Σ {\Sigma} if and only if the scalar product ⟨ p, Σ + ⟩ \langle p,{\Sigma}^{+}\rangle is nonnegative. Thus, p p lies in Σ {\Sigma} if and only if Σ + {\Sigma}^{+} lies in p + p^{+}. It follows that two hemispheres Σ 0 {\Sigma}_{0} and Σ 1 {\Sigma}_{1} intersect P P in the same hemiset if and only if Σ 0 + {\Sigma}_{0}^{+} and Σ 1 + {\Sigma}_{1}^{+} lie in the same cell of P ∗ P^{*}. Moreover, as Σ + {\Sigma}^{+} moves in the cell the hemisphere Σ {\Sigma} also moves while enclosing the same set of points; the boundary of Σ {\Sigma} touches a point p p if and only if Σ + {\Sigma}^{+} touches p ∗ p^{*}.

For example, we now see that a projective set of 2 ​ n 2n points, n ≥ 3 n\geq 3, in general position has 2 ​ ( n 2) + 2 2\binom{n}{2}+2 distinct affine hemisets (see Section 2.2). Also, it should be clear from the final computations of the proof of Proposition 4.1 that if that projective point set has symmetry group 𝖦 {\sf G}, then it supports ( 2 ​ ( n 2) + 2) ​ n! | 𝖦 | \left(2\binom{n}{2}+2\right)\frac{n!}{|{\sf G}|} distinct labeled affine order types.

### 4.3 Counting extreme points: expectation and variance

We can now prove Theorem 1.2 on the expectation and variance of the number of extreme points in a random labeled affine order type.

###### Lemma 4.3.

Let P P be a projective set of 2 ​ n 2n points, n ≥ 3 n\geq 3, in general position. If X P X_{P} denotes the number of extreme points in a labeled affine order type chosen uniformly among those supported by P P, then

 | 𝔼 ⁡ [X P] = 4 ​ n ​ ( n − 1) n ⁡ ( n − 1) + 2 = 4 − 8 n 2 − n + 2 and 𝔼 ⁡ [X P 2] ≤ 19 ​ n ​ ( n − 1) − 10 ​ n n ⁡ ( n − 1) + 2 < 19. \mathbb{E}\left[X_{P}\right]=\frac{4n(n-1)}{n(n-1)+2}=4-\mbox{$\frac{8}{n^{2}-n+2}$}\qquad\hbox{and}\qquad\mathbb{E}\left[{X_{P}}^{2}\right]\leq\frac{\displaystyle 19n(n-1)-{{10}}n}{\displaystyle n(n-1)+2}<19. |  |

*Proof.*By Proposition 4.1 and Lemma 4.2, X P X_{P} has the same distribution as the number of edges in a cell chosen uniformly at random in P ∗ P^{*}. The arrangement P ∗ P^{*} has 2 ​ ( n 2) + 2 2\binom{n}{2}+2 cells and 4 ​ ( n 2) 4\binom{n}{2} edges. Since every edge bounds exactly two cells, it follows that

 | 𝔼 ⁡ [X P] = 8 ​ ( n 2) 2 ​ ( n 2) + 2 = 4 ​ n ​ ( n − 1) n ⁡ ( n − 1) + 2 = 4 − 8 n 2 − n + 2. \mathbb{E}\left[X_{P}\right]=\frac{8\binom{n}{2}}{2\binom{n}{2}+2}={\frac{4n(n-1)}{n(n-1)+2}}=4-\mbox{$\frac{8}{n^{2}-n+2}$}. |  |

Moreover, the random variable X P 2 {X_{P}}^{2} has the same distribution as the square of the number of edges in a random cell chosen uniformly in P ∗ P^{*}. Let F 2 ​ ( P ∗) F_{2}(P^{*}) denote the set of cells of P ∗ P^{*} and for c ∈ F 2 ​ ( P ∗) c\in F_{2}(P^{*}) let | c | |c| denote its number of edges. We thus have

 | ( 2 ​ ( n 2) + 2) ​ 𝔼 ​ [X P 2] = ∑ c ∈ F 2 ​ ( P ∗) | c | 2. \left(2\binom{n}{2}+2\right)\mathbb{E}\left[{X_{P}}^{2}\right]=\sum_{c\in F_{2}(P^{*})}|c|^{2}. |  |

In the right-hand term, every edge e e of P ∗ P^{*} is counted | c 1 | + | c 2 | |c_{1}|+|c_{2}| times, where c 1 c_{1} and c 2 c_{2} are its two adjacent cells. For any point p ∈ P p\in P, the contribution of the edges supported by p ∗ p^{*} to that sum equals ∑ c ∈ Z ⁡ ( p ∗) | c | ≤ 19 ​ ( n − 1) − 10 \sum_{c\in Z(p^{*})}|c|\leq 19(n-1)-{{10}} (following notation and bound in Theorem 2.1). Altogether,

 | ( 2 ​ ( n 2) + 2) ​ 𝔼 ​ [X P 2] ≤ n ⁡ ( 19 ​ ( n − 1) − 10) \left(2\binom{n}{2}+2\right)\mathbb{E}\left[{X_{P}}^{2}\right]\leq n(19(n-1)-{{10}}) |  |

and 𝔼 ⁡ [X P 2] ≤ 19 ​ n ​ ( n − 1) − 10 ​ n n ⁡ ( n − 1) + 2 < 19 \mathbb{E}\left[{X_{P}}^{2}\right]\leq\frac{\displaystyle 19n(n-1)-{{10}}n}{\displaystyle n(n-1)+2}<19.

Here comes the announced proof.

*Proof of Theorem 1.2.*Let ρ ¯ \overline{\rho} be a simple labeled order type chosen uniformly at random in 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}. Let X n X_{n} denote the number of extreme points in ρ \rho, where ρ \rho denotes the unlabeling of ρ ¯ \overline{\rho} and let π \pi be the projective completion of ρ \rho. By Lemma 4.3, we have

 | ∀ π ′ ∈ 𝖮𝖳 n proj, 𝔼 [X n ∣ π = π ′] = 4 ​ n ​ ( n − 1) n ⁡ ( n − 1) + 2 and 𝔼 [X n 2 ∣ π = π ′] ≤ 19 ​ n ​ ( n − 1) − 10 ​ n n ⁡ ( n − 1) + 2. \forall\pi^{\prime}\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n},\quad\mathbb{E}\left[X_{n}\mid\pi=\pi^{\prime}\right]=\frac{4n(n-1)}{n(n-1)+2}\quad\hbox{and}\quad\mathbb{E}\left[{X_{n}}^{2}\mid\pi=\pi^{\prime}\right]\leq\frac{19n(n-1)-{{10}}n}{n(n-1)+2}. |  |

The formula of total probability therefore yields

 | 𝔼 ⁡ [X n] = 4 ​ n ​ ( n − 1) n ⁡ ( n − 1) + 2 and 𝔼 ⁡ [X n 2] ≤ 19 ​ n ​ ( n − 1) − 10 ​ n n ⁡ ( n − 1) + 2. \mathbb{E}\left[X_{n}\right]=\frac{4n(n-1)}{n(n-1)+2}\quad\hbox{and}\quad\mathbb{E}\left[{X_{n}}^{2}\right]\leq\frac{19n(n-1)-{{10}}n}{n(n-1)+2}. |  |

From there, Var ​ [X n] = 𝔼 ⁡ [X n 2] − 𝔼 ​ [X n] 2 < 3 \textrm{Var}\left[X_{n}\right]=\mathbb{E}\left[{X_{n}}^{2}\right]-\mathbb{E}\left[X_{n}\right]^{2}<3. (A bound of 3 + o ⁡ ( 1) 3+o(1) is readily seen from 𝔼 ⁡ [X n] = 4 + o ⁡ ( 1) \mathbb{E}\left[X_{n}\right]=4+o(1) and 𝔼 ⁡ [X n 2] < 19 \mathbb{E}\left[{X_{n}}^{2}\right]<19.)

As a consequence, we obtain for instance the following estimates.

###### Corollary 4.4.

For h ≥ 6 h\geq 6, the proportion of simple labeled affine n n -point order types with at least h h convex hull vertices is at most 3 / ( h − 4) 2 {3}/(h-4)^{2}.

*Proof.*By the Bienaymé-Chebyshev inequality, for any real t > 0 t>0 and any random variable X X with finite expected value and non-zero variance, we have

 | ℙ [| X − 𝔼 [X] | ≥ t Var ​ [X]] ≤ 1 t 2. \mathbb{P}\left[|X-\mathbb{E}\left[X\right]|\geq t\sqrt{\textrm{Var}\left[X\right]}\right]\leq\frac{1}{t^{2}}. |  |

Together with Theorem 1.2, this implies the statement.

Here is a more direct 10 10 10 The machinery we set up for our proof of Theorem 1.2 is needed in the analysis of the unlabeled setting, which was our initial goal. way to prove Theorem 1.2 which we learned from Arnau Padrol. We can define a labeled projective 2 ​ n 2n -point set P ¯ \bar{P} as a projective set where the antipodal pairs are labeled from 1 1 to n n (antipodal points receive the same label). Any affine hemiset of P ¯ \bar{P} determines a labeled affine order type. It turns out that for n ≥ 4 n\geq 4 these labeled affine order types are pairwise distinct: there is no multiplicity! 11 11 11 Indeed, consider two labeled affine order types A ¯ \bar{A} and A ¯ ′ \bar{A}^{\prime} of P ¯ \bar{P}. The map ϕ \phi that sends every point of A ¯ \bar{A} to the point in A ¯ ′ \bar{A}^{\prime} with the same label can be described as follows: for p ∈ A ¯ p\in\bar{A}, we have ϕ ⁡ ( p) = p \phi(p)=p if p ∈ A ¯ ′ p\in\bar{A}^{\prime} and ϕ ⁡ ( p) = − p \phi(p)=-p otherwise. Since A ¯ ≠ A ¯ ′ \bar{A}\neq\bar{A}^{\prime}, at least one point is antipodal to its image. Now, for n ≥ 4 n\geq 4, in any vector in { ± 1 } n \{\pm 1\}^{n} with at least one − 1 -1 entry, there exist three entries for which the number of − 1 -1 is odd. This fails for n = 3 n=3. Thus, the number of extreme points in a random labeled affine order type supported by P ¯ \bar{P} has the same distribution as the number of edges in a random 2 2 -cell chosen uniformly from P ¯ ∗ \bar{P}^{*}.

## 5 Poles of projective symmetries

To analyze non-labeled affine order types, we again relate, for a projective point set P P, the number of extreme points in a random order type of 𝖮𝖳 aff P {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P} to the average number of edges in a random cell of P ∗ P^{*}. The issue is, however, that we no longer have Proposition 4.1: to count every affine order type of 𝖮𝖳 aff P {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P} only once, and not as many times as there are hemisets of P P realizing it, will require some control over the structure of the symmetries of affine and projective sets.

We draw inspiration from Klein’s classical characterization of the finite subgroups of S ​ O ​ ( 3) SO(3). An easily accessible exposition of Klein’s proof can be found in [56], whose line we follow here. This proof analyzes how a finite subgroup of S ​ O ​ ( 3) SO(3) acts on the (finite) set of points fixed by at least one of its nontrivial members. The notion of *pole hemisets*that we now define plays the role of these fixed points.

Let P P be a projective point set and 𝖦 {\sf G} its symmetry group. Given a nontrivial symmetry g ∈ 𝖦 g\in{\sf G}, a *pole*of g g is a hemiset B B such that g ⁡ ( B) = B g(B)=B. A *pole*of P P is a pole of some nontrivial symmetry of P P. We say that two hemisets B 0 B_{0} and B 1 B_{1} of P P are *antipodal*if B 0 = − B 1 B_{0}=-B_{1}. The following will be instrumental to mimick Klein’s proof and to classify the structure of symmetry groups of projective sets.

###### Proposition 5.1.

Let P P be a projective set of 2 ​ n 2n points in general position, with n ≥ 3 n\geq 3. Every symmetry g ≠ 𝗂𝖽 g\neq{\sf id} of P P has exactly two poles and they are antipodal.

The rest of this section is devoted to the proof of Proposition 5.1. A first, at this point unmotivated step is to clarify some properties of order preserving and order reversing bijections of affine sets.

### 5.1 Preparation: reflections of affine sets

A bijection f: S → S ′ f:S\rightarrow S^{\prime} between sets on the sphere is *orientation reversing*if χ ⁡ ( f ⁡ ( p), f ⁡ ( q), f ⁡ ( r)) = − χ ⁡ ( p, q, r) {\chi}(f(p),f(q),f(r))=-{\chi}(p,q,r) for every triple in ( p, q, r) ∈ S 3 (p,q,r)\in S^{3}. A permutation f f of a set S S on the sphere *goes across*a great circle C {C} on the sphere, if, for all p ∈ S p\in S, either f ⁡ ( p) = p f(p)=p and p ∈ C p\in{C}, or p p and f ⁡ ( p) f(p) are strictly separated by C {C}. The first ingredient of the proof of Proposition 5.1 is:

###### Proposition 5.2.

Every orientation reversing permutation f f of an affine set A A in general position goes across some great circle C {C}.

It will be convenient to transport the affine set A A under consideration to the plane ℝ 2 \mathbb{R}^{2} as discussed in Section 1.2.1 and show the equivalent claim that every orientation reversing bijection f f goes across some line ℓ \ell, i.e., for all points p p we have either f ⁡ ( p) = p f(p)=p and p p lies on ℓ \ell, or ℓ \ell strictly separates f ⁡ ( p) f(p) from p p.

###### Lemma 5.3.

If f f is an orientation reversing permutation of a finite set A ⊆ ℝ 2 A\subseteq\mathbb{R}^{2} in general position, then f 2 = 𝗂𝖽 f^{2}={\sf id}.

*Proof.*Note that ( p, q) (p,q) is a positive extreme edge of A A if and only if ( f ⁡ ( q), f ⁡ ( p)) (f(q),f(p)) is a positive extreme edge of f ⁡ ( A) f(A). Hence, f f maps each layer of A A to itself and it suffices to prove the statement for A A in convex position. So let ( p 0, p 1, …, p n − 1) (p_{0},p_{1},\ldots,p_{n-1}) be a CCW extreme points order of A A and let t t be such that f ⁡ ( p 0) = p t f(p_{0})=p_{t}. Since f f reverses orientation, for all 0 ≤ i ≤ n − 1 0\leq i\leq n-1 we must have f ⁡ ( p i) = p t − i f(p_{i})=p_{t-i} (indices mod n \bmod\,n). It follows that f 2 ​ ( p i) = p i f^{2}(p_{i})=p_{i}.

Let f f be an orientation reversing permutation of A A. Since f 2 = 𝗂𝖽 A f^{2}={\sf id}_{A}, { 𝗂𝖽 A, f } \{{\sf id}_{A},f\} is a group and its action partitions A A into orbits of size 1 1 or 2 2, which we call *f f -orbits*. For p ∈ A p\in A we write [p] = def { p, f ⁡ ( p) } [p]\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{p,f(p)\} and p ¯ = def 𝖼𝗈𝗇𝗏 ⁡ ( [p]) \bar{p}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}{\sf conv}([p]), which is a segment or a single point; in the latter case we call [p] [p] a *point-orbit*. Let 𝒯 = 𝒯 ⁡ ( A, f) = def { p ¯ ∣ p ∈ A } \mathcal{T}=\mathcal{T}(A,f)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{\bar{p}\mid p\in A\}. Our task is to prove that there exists a line that intersects every element in 𝒯 \mathcal{T}. Note that if such a line transversal exists, then the general position ensures that one exists that is disjoint from the endpoints of segments in 𝒯 \mathcal{T}.

In order to prove Proposition 5.2 for a set A A in general position and an orientation reversing permutation f f of A A, we discriminate three cases depending on the number of point-orbits of f f.

##### Two point-orbits.

Suppose there are two point-orbits [p] [p] and [q] [q], i.e., f ⁡ ( p) = p f(p)=p and f ⁡ ( q) = q f(q)=q. Then the line ℓ p ​ q \ell_{pq} through p p and q q hits all segments r ¯ \bar{r} in 𝒯 \mathcal{T} since

 | χ ⁡ ( p, q, r) = − χ ⁡ ( f ⁡ ( p), f ⁡ ( q), f ⁡ ( r)) = − χ ⁡ ( p, q, f ⁡ ( r)) {\chi}(p,q,r)=-{\chi}(f(p),f(q),f(r))=-{\chi}(p,q,f(r)) |  |

and thus r r and f ⁡ ( r) f(r) have to lie on opposite sides of ℓ p ​ q \ell_{pq} (on ℓ p ​ q \ell_{pq} is outruled by general position).

##### One point-orbit.

Suppose [p] [p] is the only point-orbit and let [q] [q] and [r] [r] be two distinct f f -orbits different from [p] [p]. For the line ℓ p ​ q \ell_{pq} through p p and q q observe that the product χ ⁡ ( p, q, r) ⋅ χ ⁡ ( p, q, f ⁡ ( r)) {\chi}(p,q,r)\cdot{\chi}(p,q,f(r)) is − 1 -1 if and only if the line ℓ p ​ q \ell_{pq} hits r ¯ \bar{r}. We have that ℓ p ​ q \ell_{pq} hits r ¯ \bar{r} if and only if ℓ p ​ f ​ ( q) \ell_{pf(q)} hits r ¯ \bar{r} since

 | χ ⁡ ( p, f ⁡ ( q), r) ⋅ χ ⁡ ( p, f ⁡ ( q), f ⁡ ( r)) \displaystyle{\chi}(p,f(q),r)\cdot{\chi}(p,f(q),f(r)) | = \displaystyle= | − χ ( f ( p), f 2 ( q), f ( r)) ⋅ − χ ( f ( p), f 2 ( q), f 2 ( r)) \displaystyle-{\chi}(f(p),f^{2}(q),f(r))\cdot-{\chi}(f(p),f^{2}(q),f^{2}(r)) |  |

 |  | = \displaystyle= | χ ⁡ ( p, q, f ⁡ ( r)) ⋅ χ ⁡ ( p, q, r), \displaystyle{\chi}(p,q,f(r))\cdot{\chi}(p,q,r)~, |  |

and we have that ℓ p ​ q \ell_{pq} hits r ¯ \bar{r} if and only if ℓ p ​ r \ell_{pr} does *not*hit q ¯ \bar{q} since

 | χ ⁡ ( p, r, q) ⋅ χ ⁡ ( p, r, f ⁡ ( q)) = \displaystyle{\chi}(p,r,q)\cdot{\chi}(p,r,f(q))= | χ ( p, r, q) ⋅ − χ ( f ( p), f ( r), f 2 ( q)) \displaystyle{\chi}(p,r,q)\cdot-{\chi}(f(p),f(r),f^{2}(q)) |  |  |

 | = \displaystyle= | χ ( p, r, q) ⋅ − χ ( p, f ( r), q) \displaystyle{\chi}(p,r,q)\cdot-{\chi}(p,f(r),q) | = − χ ( p, q, r) ⋅ χ ( p, q, f ( r)). \displaystyle=-{\chi}(p,q,r)\cdot{\chi}(p,q,f(r))~. |  |

Hence, either ℓ p ​ q \ell_{pq} hits r ¯ \bar{r} or ℓ p ​ r \ell_{pr} hits q ¯ \bar{q} (but not both). W.l.o.g. let ℓ p ​ q \ell_{pq} hit r ¯ \bar{r} and thus ℓ p ​ f ​ ( q) \ell_{pf(q)} hits r ¯ \bar{r}. Then all lines through p p passing through q ¯ \bar{q} must hit r ¯ \bar{r}. This holds, since if we rotate the line through p p and q q to the line through p p and f ⁡ ( q) f(q) so that q ¯ \bar{q} is always hit, we can never encounter an endpoint of r ¯ \bar{r}, otherwise ℓ p ​ r \ell_{pr} or ℓ p ​ f ​ ( r) \ell_{pf(r)} hits q ¯ \bar{q}, which we excluded for ℓ p ​ q \ell_{pq} hitting r ¯ \bar{r}.

Consequently, the set of lines L p ​ q ¯ L_{p\bar{q}} through p p and q ¯ \bar{q} is a subset of the set L p ​ r ¯ L_{p\bar{r}} of lines through p p and r ¯ \bar{r}. It follows that the sets L p ​ s ¯ L_{p\bar{s}}, s ¯ ∈ 𝒯 ∖ { p ¯ } \bar{s}\in\mathcal{T}\setminus\{\bar{p}\}, are totally ordered by inclusion and the minimal set in this order exhibits a line hitting all elements in 𝒯 \mathcal{T}. This concludes the argument for Proposition 5.2 in the one point-orbit case.

##### No point-orbit.

Suppose there is no point-orbit of f f. We will employ Hadwiger’s *transversal theorem*[36]: *a finite family of pairwise disjoint, convex, subsets of the plane has a line transversal if and only if they can be ordered such that every three members can be intersected by a directed line in the given order.*

We start with a few observations about the relative position of segments in 𝒯 \mathcal{T}.

###### Claim 5.4.

1.

Let p ¯, q ¯ \bar{p},\bar{q}, and r ¯ \bar{r} be three distinct segments in 𝒯 \mathcal{T}.

2. (i)

The line supporting p ¯ \bar{p} is disjoint from q ¯ \bar{q}.

3. (ii)

Exactly two of the segments p ¯, q ¯ \bar{p},\bar{q}, and r ¯ \bar{r} are edges of 𝖼𝗈𝗇𝗏 ⁡ ( [p] ∪ [q] ∪ [r]) {\sf conv}([p]\cup[q]\cup[r]).

4. (iii)

The segments p ¯, q ¯ \bar{p},\bar{q}, and r ¯ \bar{r} have a line transversal.

*Proof.*(i) We have χ ⁡ ( p, f ⁡ ( p), q) = − χ ⁡ ( f ⁡ ( p), f 2 ​ ( p) ⏞ = p, f ⁡ ( q)) = χ ⁡ ( p, f ⁡ ( p), f ⁡ ( q)) {\chi}(p,f(p),q)=-{\chi}(f(p),\overbrace{f^{2}(p)}^{=p},f(q))={\chi}(p,f(p),f(q)), and therefore q q and f ⁡ ( q) f(q) are on the same side of the line through p p and f ⁡ ( p) f(p).

(ii) For each of the three f f -orbits of A ′ = def [p] ∪ [q] ∪ [r] A^{\prime}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}[p]\cup[q]\cup[r], either both of its points are extreme in A ′ A^{\prime} or none is. Hence, the orbits define a matching on the extreme points of A ′ A^{\prime}. Since, by (i), no two of the segments p ¯, q ¯ \bar{p},\bar{q}, and r ¯ \bar{r} cross, it follows that at least two segments are edges of 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}).

Now suppose all three segments are edges of 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}). Since, moreover, the segments are disjoint, all oriented triangles ( x, y, z) (x,y,z) with x ∈ p ¯ x\in\bar{p}, y ∈ q ¯ y\in\bar{q}, and z ∈ r ¯ z\in\bar{r} have the same orientation, i.e., they have the same sign χ ⁡ ( x, y, z) {\chi}(x,y,z). This contradicts χ ⁡ ( p, q, r) = − χ ⁡ ( f ⁡ ( p), f ⁡ ( q), f ⁡ ( r)) {\chi}(p,q,r)=-{\chi}(f(p),f(q),f(r)).

(iii) W.l.o.g. let p ¯ \bar{p} and q ¯ \bar{q} be edges of 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}). If 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}) is a quadrilateral, then r ¯ \bar{r} is in the interior of 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}). For every given pair of opposite edges of a convex quadrilateral, every interior point has a line passing through it and the given pair of edges. This establishes the claim.

The only case left is that of 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}) being a convex hexagon. Since r ¯ \bar{r} is not an edge of 𝖼𝗈𝗇𝗏 ⁡ ( A ′) {\sf conv}(A^{\prime}), it is a diagonal separating p ¯ \bar{p} and q ¯ \bar{q}. The claim is obvious in this case.

Let 𝒯 → \vec{\mathcal{T}} be the set 𝒯 \mathcal{T} where every segment is directed in some way; we denote the segment directed from p p to f ⁡ ( p) f(p) by p → \vec{p}. We say that q → ∈ 𝒯 → \vec{q}\in\vec{\mathcal{T}} is left of p → ∈ 𝒯 → \vec{p}\in\vec{\mathcal{T}} if [q] [q] lies to the *left of*p → \vec{p}, i.e., χ ⁡ ( p, f ⁡ ( p), q) = χ ⁡ ( p, f ⁡ ( p), f ⁡ ( q)) = + 1 {\chi}(p,f(p),q)={\chi}(p,f(p),f(q))=+1. If χ ⁡ ( p, f ⁡ ( p), q) = χ ⁡ ( p, f ⁡ ( p), f ⁡ ( q)) = − 1 {\chi}(p,f(p),q)={\chi}(p,f(p),f(q))=-1 we say that q → \vec{q} is *right of*p → \vec{p}. Claim 5.4 (i) ensures that q → \vec{q} is either left or right of p → \vec{p}. However, we cannot assume that q → \vec{q} left of p → \vec{p} implies p → \vec{p} right of q → \vec{q}.

We will proceed as follows. First, we show that we can indeed choose directed versions 𝒯 → \vec{\mathcal{T}} of the segments in 𝒯 \mathcal{T} such that q → \vec{q} is left of p → \vec{p} if and only if p → \vec{p} is right of q → \vec{q}, for all q →, p → ∈ 𝒯 → \vec{q},\vec{p}\in\vec{\mathcal{T}}. We call these *consistent directions*. Then we show that the relation “left of” is transitive. This induces a total order on 𝒯 → \vec{\mathcal{T}}, which will be the basis for the use of Hadwiger’s transversal theorem. Let us point out that even sets of segments satisfying Claim 5.4 (i) do not necessarily allow a consistent way of choosing directions, and moreover, even consistently directed segments do not necessarily imply transitivity as described above (see Figure 5 for examples).

Figure 5: Left: Three segments that cannot be directed in a consistent manner. Right: Three consistently directed segments with p → \vec{p} left of q → \vec{q} left of r → \vec{r} left of p → \vec{p}. Note that while these segments satisfy Claim 5.4 (i), they are in contradiction with Claim 5.4 (ii).

We now choose a set 𝒯 → \vec{\mathcal{T}} of directions for the segments in 𝒯 \mathcal{T}: Orient one of the segments arbitrarily, say orient p ¯ 0 ∈ 𝒯 {\bar{p}_{0}}\in\mathcal{T} as p → 0 {\vec{p}_{0}}. Then orient each other segment as q → \vec{q} so that the direction is consistent with p → 0 {\vec{p}_{0}}. Note here that q → \vec{q} is consistent with p → 0 {\vec{p}_{0}} if and only if χ ⁡ ( p 0, f ⁡ ( p 0), q) ⋅ χ ⁡ ( q, f ⁡ ( q), p 0) = − 1 {\chi}(p_{0},f(p_{0}),q)\cdot{\chi}(q,f(q),p_{0})=-1.

###### Claim 5.5.

Every pair q →, r → ∈ 𝒯 → ∖ { p → 0 } \vec{q},\vec{r}\in\vec{\mathcal{T}}\setminus\{\vec{p}_{0}\}, q → ≠ r → \vec{q}\neq\vec{r}, is consistently directed.

*Proof.*Suppose q → \vec{q} and r → \vec{r} are not consistent with each other. On the one hand, this means

 | χ ⁡ ( p 0, f ⁡ ( p 0), q) ⋅ χ ⁡ ( q, f ⁡ ( q), p 0) \displaystyle{\chi}(p_{0},f(p_{0}),q)\cdot{\chi}(q,f(q),p_{0}) | = \displaystyle= | − 1, \displaystyle-1~, |  |

 | χ ⁡ ( p 0, f ⁡ ( p 0), r) ⋅ χ ⁡ ( r, f ⁡ ( r), p 0) \displaystyle{\chi}(p_{0},f(p_{0}),r)\cdot{\chi}(r,f(r),p_{0}) | = \displaystyle= | − 1, and \displaystyle-1~,\mbox{~ and} |  | (3) |

 | χ ⁡ ( q, f ⁡ ( q), r) ⋅ χ ⁡ ( r, f ⁡ ( r), q) \displaystyle{\chi}(q,f(q),r)\cdot{\chi}(r,f(r),q) | = \displaystyle= | 1. \displaystyle~1~. |  |

On the other hand, by Claim 5.4 (ii), we know that two of p ¯ 0, q ¯, r ¯ \bar{p}_{0},\bar{q},\bar{r} are edges of 𝖼𝗈𝗇𝗏 ⁡ ( [p 0] ∪ [q] ∪ [r]) {\sf conv}([p_{0}]\cup[q]\cup[r]) and the third one is not. Again with Claim 5.4 (i) in mind, this fact can be expressed as

 | among ​ { χ ⁡ ( p 0, f ⁡ ( p 0), q) ⋅ χ ⁡ ( p 0, f ⁡ ( p 0), r) χ ⁡ ( q, f ⁡ ( q), r) ⋅ χ ⁡ ( q, f ⁡ ( q), p 0) χ ⁡ ( r, f ⁡ ( r), p 0) ⋅ χ ⁡ ( r, f ⁡ ( r), q) } ​ two are + 1, and one is − 1. \displaystyle\mbox{among}\left\{\begin{array}[]{c}{\chi}(p_{0},f(p_{0}),q)\cdot{\chi}(p_{0},f(p_{0}),r)\\ {\chi}(q,f(q),r)\cdot{\chi}(q,f(q),p_{0})\\ {\chi}(r,f(r),p_{0})\cdot{\chi}(r,f(r),q)\end{array}\right\}\mbox{two are $+1$, and one is $-1$.} |  |

The six χ {\chi} -terms in ( 5.1) are the same as the terms used in ( 3). According to ( 3), their overall product is + 1 +1, according to ( 5.1) it is − 1 -1, which gives the desired contradiction.

###### Claim 5.6.

Let p →, q →, r → ∈ 𝒯 → \vec{p},\vec{q},\vec{r}\in\vec{\mathcal{T}} be such that p → \vec{p} is left of q → \vec{q} and q → \vec{q} is left of r → \vec{r}. Then p → \vec{p} is left of r → \vec{r}, q ¯ \bar{q} is not an edge of 𝖼𝗈𝗇𝗏 ⁡ ( [p] ∪ [q] ∪ [r]) {\sf conv}([p]\cup[q]\cup[r]), and every transversal meets q ¯ \bar{q} in between p ¯ \bar{p} and r ¯ \bar{r}.

*Proof.*Since q → \vec{q} is left of r → \vec{r}, we have r → \vec{r} is right of q → \vec{q}, by consistency of directions. Since p → \vec{p} is left of q → \vec{q} and r → \vec{r} is right of q → \vec{q}, the segment q ¯ \bar{q} is not an edge of 𝖼𝗈𝗇𝗏 ⁡ ( [p] ∪ [q] ∪ [r]) {\sf conv}([p]\cup[q]\cup[r]). By Claim 5.4 (ii), r ¯ \bar{r} is an edge of this convex hull, and hence q → \vec{q} left of r → \vec{r} implies that also p → \vec{p} left of r → \vec{r}. Since p ¯ \bar{p} and r ¯ \bar{r} are disjoint edges of 𝖼𝗈𝗇𝗏 ⁡ ( [p] ∪ [q] ∪ [r]) {\sf conv}([p]\cup[q]\cup[r]), every transversal meets q ¯ \bar{q} in between p ¯ \bar{p} and r ¯ \bar{r}.

We can now conclude the proof of Proposition 5.2 for the case of no point-orbit. Define a relation ⪯ \preceq on 𝒯 → \vec{\mathcal{T}} by

 | p → ⪯ q → ⟺ def p → left of q → or p → = q →. \vec{p}\preceq\vec{q}~~\stackrel{{{}_{\text{\tiny{def}}}}}{{\Longleftrightarrow}}~~\mbox{$\vec{p}$ left of $\vec{q}$ ~or~ $\vec{p}=\vec{q}$}~. |  |

This is a total order: It is obviously reflexive; transitivity is shown in Claim 5.6; what we called consistency implies antisymmetry ( p → ⪯ q → \vec{p}\preceq\vec{q} and q → ⪯ p → \vec{q}\preceq\vec{p} implies p → = q → \vec{p}=\vec{q}) and connectedness ( p → ⪯ q → \vec{p}\preceq\vec{q} or q → ⪯ p → \vec{q}\preceq\vec{p}).

Whenever p → ⪯ q → ⪯ r → \vec{p}\preceq\vec{q}\preceq\vec{r} for three distinct elements in 𝒯 → \vec{\mathcal{T}}, there is a directed line meeting the segements p ¯ \bar{p}, q ¯ \bar{q}, and r ¯ \bar{r} in this order (Claims 5.4 (iii) and 5.6). Hadwiger’s transversal theorem entails a transversal of all segments in 𝒯 \mathcal{T}.

### 5.2 Uniqueness of poles

With reflections of affine sets under control with Proposition 5.2, we now turn to the proof of Proposition 5.1. We start with the uniqueness, which easily follows from the following remarkable property of hemisets. 12 12 12 In the affine case, the proposition basically states that no nontrivial symmetry can respect a nontrivial partition of the point set by a line.

###### Proposition 5.7.

Let P P be a projective set in general position, | P | ≥ 6 |P|\geq 6. Let B B be a hemiset of P P. Let g ≠ 𝗂𝖽 B g\neq{\sf id}_{B} be a symmetry of B B, and let Σ {\Sigma} be a closed hemisphere with g ⁡ ( B ∩ Σ) = B ∩ Σ g(B\cap{\Sigma})=B\cap{\Sigma}. Then B B is contained in Σ {\Sigma} or in − Σ -{\Sigma}.

It is perhaps worthwhile to mention that while many of the basic lemmas (e.g., Proposition 3.2 and Lemma 3.8) have appropriate generalizations to higher dimensions (along the lines of our proofs or also [5]), this proposition fails for higher dimensions: a set in ℝ 3 \mathbb{R}^{3}, or – in our terminology – an affine set A A on 𝕊 3 \mathbb{S}^{3} can have a nontrivial symmetry (rotation) which stabilizes a nontrivial intersection of A A with a hemisphere.

*Proof.*Let us first consider the case where B B is an affine set. If ∅ ≠ B ∩ Σ ≠ B \emptyset\neq B\cap{\Sigma}\neq B then there must be a unique positive extreme edge ( p 0, p 1) (p_{0},p_{1}) of B B with p 0 ∉ Σ p_{0}\not\in{\Sigma} and p 1 ∈ Σ p_{1}\in{\Sigma}. Since g g is a symmetry, ( g ⁡ ( p 0), g ⁡ ( p 1)) (g(p_{0}),g(p_{1})) is a positive extreme edge of B B. By the assumption g ⁡ ( B ∩ Σ) = B ∩ Σ g(B\cap{\Sigma})=B\cap{\Sigma}, we have g ⁡ ( p 0) ∉ Σ g(p_{0})\not\in{\Sigma} and g ⁡ ( p 1) ∈ Σ g(p_{1})\in{\Sigma}. It follows that ( g ⁡ ( p 0), g ⁡ ( p 1)) = ( p 0, p 1) (g(p_{0}),g(p_{1}))=(p_{0},p_{1}) and thus, with Claim 3.7, we conclude g = 𝗂𝖽 A g={\sf id}_{A}.

Now, consider a hemiset B B of P P and assume that E = def B ∩ − B ≠ ∅ E\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}B\cap-B\neq\emptyset. Let B ′ = def B ∖ E B^{\prime}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}B\setminus E (an affine set). By Proposition 3.2 (ii), g g maps E E to E E and B ′ B^{\prime} to B ′ B^{\prime}. Moreover, by Lemma 3.8, g ≠ 𝗂𝖽 B g\neq{\sf id}_{B} implies g | E ≠ 𝗂𝖽 E g|_{E}\neq{\sf id}_{E}.

Let us first argue (from g | E ≠ 𝗂𝖽 E g|_{E}\neq{\sf id}_{E}) that E ⊆ Σ E\subseteq{\Sigma} (which immediately shows that E E lies in the boundary of Σ {\Sigma} and thus also implies that E ⊆ − Σ E\subseteq-{\Sigma}). For every p ∈ E p\in E, Σ {\Sigma} must contain p p or − p -p, say p p. If − p -p is in the orbit of p p under g g, then − p ∈ Σ -p\in{\Sigma} as well because g ⁡ ( B ∩ Σ) = B ∩ Σ g(B\cap{\Sigma})=B\cap{\Sigma}. The alternative is that E = { p, − p, q, − q } E=\{p,-p,q,-q\} (remember that P P is in general position) and, up to exchanging q q and − q -q, that p ↦ g q ↦ g p p\stackrel{{\scriptstyle g}}{{\mapsto}}q\stackrel{{\scriptstyle g}}{{\mapsto}}p. But then, taking any r ∈ B ′ r\in B^{\prime},

 | χ ⁡ ( p, q, r) = χ ⁡ ( g ⁡ ( p), g ⁡ ( q), g ⁡ ( r)) = χ ⁡ ( q, p, g ⁡ ( r)) = − χ ⁡ ( p, q, g ⁡ ( r)), {\chi}(p,q,r)={\chi}(g(p),g(q),g(r))={\chi}(q,p,g(r))=-{\chi}(p,q,g(r)), |  |

which is impossible since g ⁡ ( B ′) = B ′ g(B^{\prime})=B^{\prime} and all points of B ′ B^{\prime} are on the same side of the great circle through p p and q q.

Given that we know that E ⊆ Σ E\subseteq{\Sigma} and E ⊆ − Σ E\subseteq-{\Sigma}, we then have two cases. If | B ′ | ≥ 2 |B^{\prime}|\geq 2, then g | B ′ g|_{B^{\prime}} is nontrivial by Lemma 3.8. We already know that the proposition holds in the affine case, so it applies to B ′ B^{\prime}, which must be contained in Σ {\Sigma} or in − Σ -{\Sigma}. If | B ′ | = 1 |B^{\prime}|=1, then Σ {\Sigma} or − Σ -{\Sigma} will always contain the given 1-element set B ′ B^{\prime}. Altogether, B = B ′ ∪ E B=B^{\prime}\cup E is also contained in Σ {\Sigma} or in − Σ -{\Sigma}.

###### Corollary 5.8.

If B 0 B_{0} and B 1 B_{1} are poles of g g, then B 1 = ± B 0 B_{1}=\pm B_{0}.

*Proof.*This follows from Proposition 5.7 with B = def B 0 B\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}B_{0} and Σ {\Sigma} a closed hemisphere with P ∩ Σ = B 1 P\cap{\Sigma}=B_{1}.

### 5.3 Existence of poles

Now, let us argue that g g has some pole. Since | P | ≥ 6 |P|\geq 6 and P P is in general position, g g preserves antipodality (Lemma 3.3 (i)) and acts on the hemisets of P P (Proposition 3.2 (i)); in particular, for any hemiset B B of P P, g ⁡ ( − B) = − g ⁡ ( B) g(-B)=-g(B). As spelled out in Lemma 4.2, for any projective set P P, the faces of the great circle arrangement P ∗ P^{*} are in correspondence with the hemisets of P P. In this correspondence, a hemiset with k k antipodal pairs corresponds to a face of dimension 2 − k 2-k. We therefore have:

###### Claim 5.9.

Any symmetry g g of a projective set P P induces a dimension preserving permutation g ¯ \bar{g} of the faces of the arrangement of P ∗ P^{*}, where also incidences are preserved: if face F F is incident to face F ′ F^{\prime}, then face g ¯ ​ ( F) \bar{g}(F) is incident to face g ¯ ​ ( F ′) \bar{g}(F^{\prime}).

This combinatorial map extents into a continuous map.

###### Claim 5.10.

There exists a continuous injective map γ: 𝕊 2 → 𝕊 2 \gamma\!:\mathbb{S}^{2}\to\mathbb{S}^{2} such that for any x ∈ 𝕊 2 x\in\mathbb{S}^{2} and any face F F of P ∗ P^{*}, x x is in F F if and only if γ ⁡ ( x) \gamma(x) is in g ¯ ​ ( F) \bar{g}(F).

*Proof.*We start by setting γ ​ ( v) = def g ¯ ​ ( v) \gamma(v)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\bar{g}(v) for every vertex v v of P ∗ P^{*}. Next, for every edge e e of P ∗ P^{*}, note that γ \gamma maps the vertices of e e to the vertices of g ¯ ​ ( e) \bar{g}(e); we extend it to a continuous (actually, “linear”) map from e e to g ¯ ​ ( e) \bar{g}(e). Last, for every cell c c of P ∗ P^{*}, γ \gamma already defines a continuous injective map from the boundary of c c to the boundary of g ¯ ​ ( c) \bar{g}(c) and can be extended into a continuous injective map c → g ¯ ​ ( c) c\to\bar{g}(c). Observe that γ \gamma agrees with g ¯ \bar{g} as stated.

Now enters the so-called hairy ball theorem 13 13 13 It is often formulated in terms of vector fields on 𝕊 2 \mathbb{S}^{2}, with the assertion at hand a simple corollary.: *If d d is even and ψ: 𝕊 d → 𝕊 d \psi:\mathbb{S}^{d}\rightarrow\mathbb{S}^{d} is a continuous function, then there exists at least one x 0 ∈ 𝕊 d x_{0}\in\mathbb{S}^{d} such that either ψ ⁡ ( x 0) = x 0 \psi(x_{0})=x_{0} or ψ ⁡ ( x 0) = − x 0 \psi(x_{0})=-x_{0}.*Hence, there exists x 0 ∈ 𝕊 2 x_{0}\in\mathbb{S}^{2} such that γ ⁡ ( x 0) ∈ { x 0, − x 0 } \gamma(x_{0})\in\{x_{0},-x_{0}\}. Let B B denote the hemiset corresponding, via Lemma 4.2, to the face containing x 0 x_{0} ( B B is the intersection of P P with the closed hemisphere centered in x 0 x_{0}). Since γ \gamma agrees with g ¯ \bar{g}, γ ⁡ ( x 0) \gamma(x_{0}) lies in the face corresponding to the hemiset g ⁡ ( B) g(B), that is, g ⁡ ( B) g(B) is the intersection of P P with the hemisphere centered in γ ⁡ ( x 0) \gamma(x_{0}).

When γ ⁡ ( x 0) = x 0 \gamma(x_{0})=x_{0} these faces coincide and g ⁡ ( B) = B g(B)=B is a pole of g g. Then also g ⁡ ( − B) = − B g(-B)=-B and we have our two poles.

Let us prove that poles exist also when γ ⁡ ( x 0) = − x 0 \gamma(x_{0})=-x_{0}. In that case, g ⁡ ( B) = − B g(B)=-B. Let g R: P → P g_{R}\!:P\rightarrow P be the auxiliary function g R ​ ( p) = def − g ​ ( p) g_{R}(p)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}-g(p). Observe that g R g_{R} is orientation *reversing*, that g R ​ ( B) = B g_{R}(B)=B, and that g R ≠ 𝗂𝖽 P g_{R}\neq{\sf id}_{P} (since P P contains three points p p, q q, r r with χ ⁡ ( p, q, r) ≠ 0 {\chi}(p,q,r)\neq 0). Our intention is to build our poles for g g from a great circle that g R g_{R} goes across. If B B is affine, we apply Proposition 5.2 to find a great circle C C such that the restriction g R | B {g_{R}}|_{B} goes across C C. The antipodality of g R g_{R} ensures that g R | − B {g_{R}}|_{-B} also goes across C C. The closed hemispheres bounded by C C determine two poles of g g.

When B B is not affine, a similar argument works once the points in B ∩ − B B\cap-B have been properly handled. Let E = B ∩ − B E=B\cap-B be the set of antipodal pairs of B B, all of which are on x 0 ∗ x_{0}^{*}. By general position of P P, | E | ≤ 4 |E|\leq 4. We cannot have E = { p, q, − p, − q } E=\{p,q,-p,-q\} with g g acting by p ↦ q ↦ − p ↦ − q ↦ p p\mapsto q\mapsto-p\mapsto-q\mapsto p. Indeed, this would imply that for any r ∈ B ∖ E r\in B\setminus E,

 | χ ⁡ ( p, q, r) = χ ⁡ ( g ⁡ ( p), g ⁡ ( q), g ⁡ ( r)) = χ ⁡ ( q, − p, g ⁡ ( r)) = χ ⁡ ( p, q, g ⁡ ( r)), {\chi}(p,q,r)={\chi}(g(p),g(q),g(r))={\chi}(q,-p,g(r))={\chi}(p,q,g(r))~, |  |

which is impossible because the great circle through p p and q q separates B B from g ⁡ ( B) = − B g(B)=-B. Next, if E = { p, q, − p, − q } E=\{p,q,-p,-q\} with g ⁡ ( p) = q g(p)=q and g ⁡ ( q) = p g(q)=p, then we can perturb x 0 x_{0} into a nearby position x 1 x_{1} whose corresponding hemiset B ′ B^{\prime} is either B ∪ { p, − q } B\cup\{p,-q\} or B ∪ { − p, q } B\cup\{-p,q\}. We may have γ ⁡ ( x 1) ≠ ± x 1 \gamma(x_{1})\neq\pm x_{1}, but we do not care as we still have g ⁡ ( B ′) = − B ′ g(B^{\prime})=-B^{\prime}. Since B ′ B^{\prime} is now affine, we can find our poles as we did above, using a circle that g R | B ′ {g_{R}}|_{B^{\prime}} goes across. Any pair { p, − p } \{p,-p\} in E E with g ⁡ ( p) = − p g(p)=-p can be pushed into B ′ B^{\prime} by a similar perturbation argument. We can therefore assume that we are left with some great circle x 1 ∗ x_{1}^{*} determining two hemisets B ′ B^{\prime} and − B ′ -B^{\prime} such that g ⁡ ( B ′) = − B ′ g(B^{\prime})=-B^{\prime} and such that E ′ = B ′ ∩ − B ′ E^{\prime}=B^{\prime}\cap-B^{\prime} consists of one or two pairs { p, − p } \{p,-p\} with g ⁡ ( p) = p g(p)=p. We compute B 0 B_{0} and B 1 B_{1} by applying, as above, Proposition 5.2 to the affine set B ′ ∖ E ′ B^{\prime}\setminus E^{\prime} to find two hemisets of P ∖ E ′ P\setminus E^{\prime} fixed by g g, say B 0 B_{0} and − B 0 -B_{0}. The hemisets B 0 B_{0} and − B 0 -B_{0} are affine so they can be defined by a great circle C C that contains no point of E E. For every pair { p, − p } ⊆ E ′ \{p,-p\}\subseteq E^{\prime}, we add p p to the set, B 0 B_{0} or − B 0 -B_{0}, on the same side as p p of C C and add − p -p to the other. The resulting sets B 0 B_{0} and − B 0 -B_{0} are poles of g g. This concludes the proof of Proposition 5.1.

## 6 Analysis of affine order types

With the notion of pole hemisets and Proposition 5.1 at our fingertips, we can now analyze the average number of extreme points of affine order types.

### 6.1 Orbit types

We start by gaining some insight on the projective symmetry groups through their action on poles (carrying over Felix Klein’s analysis of finite subgroups of S ​ O ​ ( 3) SO(3), as presented in [56]). Let 𝖦 {\sf G} be a group. We say that 𝖦 {\sf G} has *orbit type*14 14 14 As defined, a group 𝖦 {\sf G} could have more than one orbit type. As we will see later, in Proposition 9.2, it turns out that every projective symmetry group has a unique orbit type. [μ 1, μ 2, …, μ k] [\mu_{1},\mu_{2},\ldots,\mu_{k}], μ 1 ≤ μ 2 ≤ … ≤ μ k \mu_{1}\leq\mu_{2}\leq\ldots\leq\mu_{k}, if there exists a projective point set P P with symmetry group 𝖦 {\sf G} such that the action of 𝖦 {\sf G} on the poles of P P defines k k orbits of sizes μ i \mu_{i}, i = 1, 2, …, k i=1,2,\ldots,k.

###### Proposition 6.1.

Let 𝖦 {\sf G} be the symmetry group of a projective set of at least 6 6 points in general position. If 𝖦 {\sf G} is nontrivial, then its possible orbit types are [1, 1] [1,1], [4, 4, 6] [4,4,6], [6, 8, 12] [6,8,12], [12, 20, 30] [12,20,30] or [2, N / 2, N / 2] [2,N/2,N/2], where N = def | 𝖦 | N\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|{\sf G}|.

*Proof.*Let P P be a projective set of 2 ​ n 2n points in general position with symmetry group 𝖦 {\sf G}. We let N = def | 𝖦 | N\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|{\sf G}| and assume N ≥ 2 N\geq 2. We are going to count in two ways the pairs ( g, B) (g,B), with g ∈ 𝖦 ∖ { 𝗂𝖽 } g\in{\sf G}\setminus\{{\sf id}\} and B B a pole of g g. For the first count, note that every g ∈ 𝖦 ∖ { 𝗂𝖽 } g\in{\sf G}\setminus\{{\sf id}\} has exactly two poles by Proposition 5.1. Hence, the number of pairs is 2 ​ ( | 𝖦 | − 1) = 2 ​ N − 2. 2(|{\sf G}|-1)=2N-2.

The second count is less direct. Let 𝒫 \mathcal{P} denote the set of poles of P P. Recall that for every B ∈ 𝒫 B\in\mathcal{P}, 𝖦 ⁡ ( B) {\sf G}(B) denotes its orbit and 𝖦 B {\sf G}_{B} its stabilizer under 𝖦 {\sf G}. Note that by the definition of a pole, | 𝖦 B | ≥ 2 |{\sf G}_{B}|\geq 2. We number the orbits of 𝒫 \mathcal{P} from 1 1 to K K and let μ i \mu_{i} be the size of the i i th orbit. By the orbit-stabilizer theorem, for every B ∈ 𝒫 B\in\mathcal{P}, | 𝖦 | = | 𝖦 B | ⋅ | 𝖦 ⁡ ( B) | |{\sf G}|=|{\sf G}_{B}|\cdot|{\sf G}(B)|. It follows that every hemiset in the i i th orbit has a stabilizer of the same size; we let γ i \gamma_{i} denote that size (so μ i ​ γ i = N \mu_{i}\gamma_{i}=N). Now, a hemiset B ∈ 𝒫 B\in\mathcal{P} occurs in a pair ( g, B) (g,B) exactly for the nontrivial permutations in the stabilizer 𝖦 B {\sf G}_{B}, that is, | 𝖦 B | − 1 |{\sf G}_{B}|-1 times. The number of pairs is therefore ∑ i = 1 K μ i ​ ( γ i − 1) = K ​ N − ∑ i = 1 K μ i \sum_{i=1}^{K}\mu_{i}(\gamma_{i}-1)=KN-\sum_{i=1}^{K}\mu_{i}.

Equating the two counts, dividing by N N, and rearranging terms gives ∑ i = 1 K 1 γ i = K − 2 + 2 N. \sum_{i=1}^{K}\frac{1}{\gamma_{i}}=K-2+\frac{2}{N}~. This immediately restricts the range of possible values of K K. Since each γ i \gamma_{i} is at least 2 2 (by definition of a pole), K K must be less than 4 4. Since N ≥ 2 N\geq 2, K > 1 K>1. and the parameters thus satisfy

 | either ​ K = 2 and \displaystyle\hbox{either }K=2\qquad\hbox{and} | 1 γ 1 + 1 γ 2 = 2 N ⇔ μ 1 + μ 2 = 2, \displaystyle\qquad\qquad\frac{1}{\gamma_{1}}+\frac{1}{\gamma_{2}}=\frac{2}{N}~\Leftrightarrow~\mu_{1}+\mu_{2}=2, |  |  | (8) |

 | or ​ K = 3 and \displaystyle\hbox{or }K=3\qquad\hbox{and} | 1 γ 1 + 1 γ 2 + 1 γ 3 = 1 + 2 N ⇔ μ 1 + μ 2 + μ 3 = N + 2. \displaystyle\qquad\qquad\frac{1}{\gamma_{1}}+\frac{1}{\gamma_{2}}+\frac{1}{\gamma_{3}}=1+\frac{2}{N}~\Leftrightarrow~\mu_{1}+\mu_{2}+\mu_{3}=N+2. |  |  | (9) |

For K = 2 K=2 clearly, the only positive integer solution of μ 1 + μ 2 = 2 \mu_{1}+\mu_{2}=2 is μ 1 = μ 2 = 1 \mu_{1}=\mu_{2}=1, and the orbit type that P P allows for 𝖦 {\sf G} is [1, 1] [1,1].

For K = 3 K=3, let us recall that all μ i \mu_{i} are divisors of N N. Since all γ i \gamma_{i} are at least 2, all μ i \mu_{i} are at most N / 2 N/2. Let us assume they are ordered μ 1 ≤ μ 2 ≤ μ 3 ≤ N / 2 \mu_{1}\leq\mu_{2}\leq\mu_{3}\leq N/2. We have μ 3 > N / 3 \mu_{3}>N/3 (otherwise μ 1 + μ 2 + μ 3 ≤ N \mu_{1}+\mu_{2}+\mu_{3}\leq N, contradicting ( 9)), so μ 3 = N / 2 \mu_{3}=N/2 is determined and we are left with μ 1 + μ 2 = N / 2 + 2 \mu_{1}+\mu_{2}=N/2+2. We have μ 2 > N / 4 \mu_{2}>N/4 (otherwise μ 1 + μ 2 ≤ N / 2 \mu_{1}+\mu_{2}\leq N/2), so μ 2 ∈ { N / 2, N / 3 } \mu_{2}\in\{N/2,N/3\}. If μ 2 = N / 2 \mu_{2}=N/2, then the orbit type is [2, N / 2, N / 2] [2,N/2,N/2]. If μ 2 = N / 3 \mu_{2}=N/3 then we must have μ 1 = N / 6 + 2 \mu_{1}=N/6+2. Since μ 1 \mu_{1} divides N N, the only feasible choices are

 | μ 1 = N / 3 \displaystyle\mu_{1}=N/3 | ⇒ \displaystyle\Rightarrow | N = 12 ​ and ​ [μ 1, μ 2, μ 3] = [4, 4, 6] \displaystyle N=12\mbox{~~and~~}[\mu_{1},\mu_{2},\mu_{3}]=[4,4,6] |  |

 | μ 1 = N / 4 \displaystyle\mu_{1}=N/4 | ⇒ \displaystyle\Rightarrow | N = 24 ​ and ​ [μ 1, μ 2, μ 3] = [6, 8, 12] \displaystyle N=24\mbox{~~and~~}[\mu_{1},\mu_{2},\mu_{3}]=[6,8,12] |  |

 | μ 1 = N / 5 \displaystyle\mu_{1}=N/5 | ⇒ \displaystyle\Rightarrow | N = 60 ​ and ​ [μ 1, μ 2, μ 3] = [12, 20, 30] \displaystyle N=60\mbox{~~and~~}[\mu_{1},\mu_{2},\mu_{3}]=[12,20,30] |  |

This completes the proof.

### 6.2 More on affine symmetries

Next, we clarify the symmetries of affine sets.

*Proof of Theorem 1.5.*Let A A be an affine set with layer sequence ( A 0, A 1, …, A ℓ) (A_{0},A_{1},\ldots,A_{\ell}) and symmetry group 𝖥 {\sf F}. Note that by Proposition 3.2, any f ∈ 𝖥 f\in{\sf F} preserves the layer sequence, that is f ⁡ ( A i) = A i f(A_{i})=A_{i}. Moreover, for any non-lonely point p ∈ A p\in A, the stabilizer 𝖥 p {\sf F}_{p} is reduced to { 𝗂𝖽 } \{{\sf id}\} by Lemma 3.8, so | 𝖥 ⁡ ( p) | = | 𝖥 | |{\sf F}(p)|=|{\sf F}| by the orbit-stabilizer theorem. Now, consider a layer A i A_{i} not reduced to a single point. Any map f ∈ 𝖥 f\in{\sf F} maps a positive extreme edge of A i A_{i} to another one. The orbits under 𝖥 {\sf F} partition A i A_{i} into classes of equal sizes. Since | 𝖥 | = | 𝖥 ⁡ ( p) | |{\sf F}|=|{\sf F}(p)| for any p ∈ A i p\in A_{i}, | 𝖥 | |{\sf F}| divides | A i | |A_{i}|.

It is left to show that 𝖥 {\sf F} is cyclic. Fix p ∈ A 0 p\in A_{0}. The set 𝖥 ⁡ ( p) {\sf F}(p) is in convex position, in fact a subset of A 0 A_{0}, so let ( p 0 = p, p 1, p 2, …, p k − 1) (p_{0}=p,p_{1},p_{2},\ldots,p_{k-1}) be some CCW extreme points order of 𝖥 ⁡ ( p) {\sf F}(p). Let f ∈ 𝖥 f\in{\sf F} be the permutation with f ⁡ ( p) = p 1 f(p)=p_{1}. We then have f ⁡ ( p i) = p i + 1 f(p_{i})=p_{i+1} for i = 0, 1, …, k − 1 i=0,1,\ldots,k-1 (indices mod k \bmod\,k) since f f preserves positive extreme edges. From f i ​ ( p 0) = p i f^{i}(p_{0})=p_{i}, it follows that { f 0, f 1, …, f k − 1 } \{f^{0},f^{1},\ldots,f^{k-1}\} are all distinct. Since | 𝖥 | = | 𝖥 ⁡ ( p) | = k |{\sf F}|=|{\sf F}(p)|=k, 𝖥 {\sf F} is generated by f f.

Finally, assume that A A has a lonely point q q (hence f ⁡ ( q) = q f(q)=q) and that 𝖥 {\sf F} has even order. There is an element f ∈ 𝖥 f\in{\sf F} of order 2, i.e., f 2 = 𝗂𝖽 f^{2}={\sf id} (choose f = f 0 k / 2 f=f_{0}^{k/2} for a generator f 0 f_{0} of 𝖥 {\sf F}). For any other point p p, we have f ⁡ ( p) ≠ p f(p)\neq p by Lemma 3.8, so

 | χ ⁡ ( q, p, f ⁡ ( p)) = χ ⁡ ( f ⁡ ( q) ⏟ = q, f ⁡ ( p), p) = − χ ⁡ ( q, p, f ⁡ ( p)) {\chi}\left(q,p,f(p)\right)={\chi}(\underbrace{f(q)}_{=q},f(p),p)=-{\chi}\left(q,p,f(p)\right) |  |

implies that χ ⁡ ( q, p, f ⁡ ( p)) = 0 {\chi}(q,p,f(p))=0, contradicting the assumption that A A is in general position.

###### Corollary 6.2.

Let A A be an affine set of n n points with symmetry group 𝖥 {\sf F}. The orderings of A A realize exactly n! | 𝖥 | ≥ ( n − 1)! \frac{n!}{|{\sf F}|}\geq(n-1)! pairwise distinct labeled affine order types.

*Proof.*Let 𝖥 {\sf F} denote the symmetry group of A A. Recall that two labelings A [λ] A_{[\lambda]} and A [μ] A_{[\mu]} of A A determine the same labeled order type if and only if μ − 1 ∘ λ \mu^{-1}\circ\lambda is a symmetry of A A. The labelings of A A therefore determine n! / | 𝖥 | n!/|{\sf F}| labeled affine order types. Theorem 1.5 implies | 𝖥 | ≤ n |{\sf F}|\leq n, so this number is always at least ( n − 1)! (n-1)!.

We also refine the upper bound on the number of affine order types with many symmetries.

###### Proposition 6.3.

There is a constant c 0 c_{0}, such that for all 1 ≤ k ≤ n 1\leq k\leq n, there are at most ( c 0 ​ n k) 4 ​ n \left(c_{0}\frac{n}{\sqrt{k}}\right)^{4n} simple, affine order types of size n n with k k symmetries.

*Proof.*Let 𝖮𝖳 aff n, k {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k} denote the set of simple, affine order types of size n n with k k symmetries. By Theorem 1.5, either k k divides n n and none of the order types in 𝖮𝖳 aff n, k {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k} has a lonely point, or k k divides n − 1 n-1 and all do.

Let A A be an affine point set with order type in 𝖮𝖳 aff n, k {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k}. Again by Theorem 1.5, the symmetry group 𝖥 {\sf F} of A A is cyclic. We let f f be the generator of 𝖥 {\sf F} such that for every non-lonely point p ∈ A p\in A, the points p p, f ⁡ ( p) f(p), f 2 ​ ( p) f^{2}(p), …, f k − 1 ​ ( p) f^{k-1}(p) in its orbit appear in this order (counterclockwise) in the layer of A A that contains p p.

We call a labeling ( p 0, p 1, …, p n − 1) (p_{0},p_{1},\ldots,p_{n-1}) of A A a *standard labeling*if p i = f ⁡ ( p i − 1) p_{i}=f(p_{i-1}) for all 0 ≤ i ≤ n − 1 0\leq i\leq n-1 with i mod k ≠ 0 i\bmod k\neq 0. Note that this simply means that for each a a, 0 ≤ a ≤ ⌊ n k ⌋ − 1 0\leq a\leq\lfloor\frac{n}{k}\rfloor-1, we have

 | ( p a ​ k, p a ​ k + 1, p a ​ k + 2, …, p a ​ k + k − 1) = ( p a ​ k, f ⁡ ( p a ​ k), f 2 ​ ( p a ​ k), … ​ f k − 1 ​ ( p a ​ k)) (p_{ak},p_{ak+1},p_{ak+2},\ldots,p_{ak+k-1})=(p_{ak},f(p_{ak}),f^{2}(p_{ak}),\ldots f^{k-1}(p_{ak})) |  |

and if n n is not a multiple of k k, then p n − 1 p_{n-1} is the unique lonely point in A A. The points p a ​ k p_{ak}, a = 0, 1, …, ⌊ n / k ⌋ − 1 a=0,1,\ldots,\lfloor n/k\rfloor-1 are called *anchors*in the given standard labeling. Note that if a lonely point exists, it is not an anchor point. For every non-lonely point p p, there is an i p i_{p}, 0 ≤ i p ≤ k − 1 0\leq i_{p}\leq k-1, such that f i p ​ ( p) f^{i_{p}}(p) is an anchor.

It follows that the orientations χ ⁡ ( p ∗, q, r) {\chi}(p^{*},q,r) for ( p ∗, q, r) ∈ A 3 (p^{*},q,r)\in A^{3}, | { p ∗, q, r } | = 3 |\{p^{*},q,r\}|=3, p ∗ p^{*} an anchor, determine all orientations of all triples ( p, q, r) ∈ A 3 (p,q,r)\in A^{3}, | { p, q, r } | = 3 |\{p,q,r\}|=3, since

 | χ ⁡ ( p, q, r) = { χ ⁡ ( f i p ​ ( p), f i p ​ ( q), f i p ​ ( r)) if p is not a lonely point, and − χ ⁡ ( f i q ​ ( q), p, f i q ​ ( r)) if p is a lonely point (hence f i q ​ ( p) = p). {\chi}(p,q,r)=\left\{\begin{array}[]{ll}{\chi}(f^{i_{p}}(p),f^{i_{p}}(q),f^{i_{p}}(r))&\mbox{if $p$ is not a lonely point, and}\\ -{\chi}(f^{i_{q}}(q),p,f^{i_{q}}(r))&\mbox{if $p$ is a lonely point (hence $f^{i_{q}}(p)=p$).}\end{array}\right. |  |

We represent the space of all n n -point affine sets by ℝ 2 ​ n \mathbb{R}^{2n}, equipped with the coordinate system ( x 0, y 0, x 1, y 1 CLOSE, (x_{0},y_{0},x_{1},y_{1}, …, OPEN x n − 1, y n − 1) x_{n-1},y_{n-1}), where p i = ( x i, y i) p_{i}=(x_{i},y_{i}). Let 𝒫 n, k \mathcal{P}_{n,k} be the family of polynomials

 | 𝒫 n, k = def { | x a ​ k x i x j y a ​ k y i y j 1 1 1 | ∣ 0 ≤ a ≤ ⌊ n k ⌋ − 1, 0 ≤ i, j ≤ n − 1, | { a k, i, j } | = 3 }. \displaystyle\mathcal{P}_{n,k}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\left\{\left|\begin{matrix}x_{ak}&x_{i}&x_{j}\\ y_{ak}&y_{i}&y_{j}\\ 1&1&1\end{matrix}\right|\mid 0\leq a\leq\lfloor\frac{n}{k}\rfloor-1,0\leq i,j\leq n-1,|\{ak,i,j\}|=3\right\}. |  |

We let m = def | 𝒫 n, k | = ⌊ n k ⌋ ​ ( n − 1) ​ ( n − 2) < n 3 k m\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|\mathcal{P}_{n,k}|=\lfloor\frac{n}{k}\rfloor(n-1)(n-2)<\frac{n^{3}}{k} and order the polynomials in 𝒫 n, k \mathcal{P}_{n,k} as P 1, P 2, …, P m P_{1},P_{2},\ldots,P_{m}. The number of standard labelings of order types in 𝖮𝖳 aff n, k {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k} (and thus | 𝖮𝖳 aff n, k | |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k}|) is at most the number of sign vectors

 | { ( sign ​ ( P 1 ​ ( x)), sign ​ ( P 2 ​ ( x)), …, sign ​ ( P m ​ ( x))) ∈ { − 1, + 1 } m ∣ x ∈ ℝ 2 ​ n } \{\left(\textrm{sign}\left(P_{1}(x)\right),\textrm{sign}\left(P_{2}(x)\right),\ldots,\textrm{sign}\left(P_{m}(x)\right)\right)\in\{-1,+1\}^{m}\mid x\in\mathbb{R}^{2n}\} |  |

of the polynomials in 𝒫 n, k \mathcal{P}_{n,k}. By Warren’s theorem [63, Theorem 3], m ≤ m ′ m\leq m^{\prime} real polynomials in v ≤ m ′ v\leq m^{\prime} variables, each of degree at most 2 2, determine at most ( 8 ​ e ​ m ′ v) v \left(\frac{8em^{\prime}}{v}\right)^{v} sign vectors. Here v = 2 ​ n v=2n and we can choose m ′ = n 3 k m^{\prime}=\frac{n^{3}}{k}, so

 | | 𝖮𝖳 n, k aff | ≤ ( 4 ​ e ​ n 2 k) 2 ​ n |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k}|\leq\left(\frac{4e\,n^{2}}{k}\right)^{2n} |  |

and the condition v ≤ m ′ v\leq m^{\prime} holds for all n ≥ 2 n\geq 2 and k ≤ n k\leq n. The claimed bound on | 𝖮𝖳 aff n, k | |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k}| follows with c 0 = 2 ​ e c_{0}=2\sqrt{e}.

Remark. We mention that the proof above carries many redundancies which can be exploited. Improvements we see, however, would not be relevant when we apply it in the proof of Theorem 1.3 in Section 6.4 below. Let us still briefly sketch an improvement by a factor of 1 ⌊ n / k ⌋! ​ k ⌊ n / k ⌋ − 1 \frac{1}{\lfloor n/k\rfloor!k^{\lfloor n/k\rfloor-1}}. For that, note that the upper bound we derived is actually for the number of standard labelings of order types with k k symmetries. How many *distinct*such *standard-*labeled order types does a given element in 𝖮𝖳 aff n, k {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k} have? There are ⌊ n / k ⌋! \lfloor n/k\rfloor! ways to order the non-lonely orbits, and there are k ⌊ n / k ⌋ k^{\lfloor n/k\rfloor} choices for the anchors (the first elements of the respective orbits). Note, however, that for a standard labeling ( p 0, p 1, …, p n − 1) (p_{0},p_{1},\ldots,p_{n-1}), all labelings ( f i ​ ( p 0), f i ​ ( p 1), …, f i ​ ( p n − 1)) (f^{i}(p_{0}),f^{i}(p_{1}),\ldots,f^{i}(p_{n-1})), i = 0, 1, …, k − 1 i=0,1,\ldots,k-1, yield the same labeled order type, all standard labelings. Hence we get exactly ⌊ n / k ⌋! ​ k ⌊ n / k ⌋ / k \lfloor n/k\rfloor!k^{\lfloor n/k\rfloor}/k standard labelings for each order type in 𝖮𝖳 aff n, k {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k}.

Let us take a step back here and review, why did we have to divide by k k here? If we have a *point set*, then, for a standard labeling ( p 0, p 1, …, p n − 1) (p_{0},p_{1},\ldots,p_{n-1}), all labelings ( f i ​ ( p 0), f i ​ ( p 1), …, f i ​ ( p n − 1)) (f^{i}(p_{0}),f^{i}(p_{1}),\ldots,f^{i}(p_{n-1})), i = 0, 1, …, k − 1 i=0,1,\ldots,k-1, are distinct orderings (in standard form) of this given point set. However, as a labeled order type, they are clearly all the same, since f f is a symmetry ( χ ⁡ ( p a, p b, p c) = χ ⁡ ( f i ​ ( p a), f i ​ ( p b), f i ​ ( p c)) {\chi}(p_{a},p_{b},p_{c})={\chi}(f^{i}(p_{a}),f^{i}(p_{b}),f^{i}(p_{c})).

With N! > 2 ​ π ​ N ​ ( N e) N N!>\sqrt{2\pi N}\left(\frac{N}{e}\right)^{N} we have

 | ⌊ n / k ⌋! ​ k ⌊ n / k ⌋ − 1 > 2 ​ π ​ ⌊ n / k ⌋ ​ ( ⌊ n / k ⌋ e) ⌊ n / k ⌋ ​ k ⌊ n / k ⌋ − 1 ≥ ( c 1 ​ n) n / k + O ⁡ ( 1). \lfloor n/k\rfloor!k^{\lfloor n/k\rfloor-1}>\sqrt{2\pi\lfloor n/k\rfloor}\left(\frac{\lfloor n/k\rfloor}{e}\right)^{\lfloor n/k\rfloor}k^{\lfloor n/k\rfloor-1}\geq(c_{1}n)^{n/k+O(1)}~. |  |

for 15 15 15 “ + O ⁡ ( 1) +O(1) ” in the exponent stands for a negative constant. a constant c 1 > 0 c_{1}>0 sufficiently small. The resulting bound of | 𝖮𝖳 n, k aff | ≤ n − n / k + O ( 1) ( c 2 n k) 4 ​ n |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,k}|\leq n^{-n/k+O(1)}\left(c_{2}\frac{n}{\sqrt{k}}\right)^{4n} is now in line with the known bound of ( c ​ n) 3 ​ n + o ⁡ ( 1) (cn)^{3n+o(1)} for | 𝖮𝖳 aff n, 1 | |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n,1}|. For the other extreme case of k = Θ ⁡ ( n) k=\Theta(n), the bound is ( c ′ ​ n) 4 ​ n + o ⁡ ( 1) = ( c ′′ ​ n) 2 ​ n + o ⁡ ( 1) (c^{\prime}\sqrt{n})^{\,4n+o(1)}=(c^{\prime\prime}n)^{2n+o(1)} and we do not know how close that is to the truth.

### 6.3 Counting extreme points in one projective class

For any affine order type ω \omega we write h ⁡ ( ω) h(\omega) for its number of extreme points. For any projective set P P, we define h ( P) = def 1 | 𝖮𝖳 aff P | ∑ ω ∈ 𝖮𝖳 aff P h ( ω) h(P)\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\frac{1}{|{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!P}|}\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!P}}h(\omega).

###### Proposition 6.4.

If P P is a projective set of 2 ​ n 2n points in general position with N N symmetries, then 4 − ε n ≤ h ⁡ ( P) ≤ 4 + 3 ​ N / n 4-\varepsilon_{n}\leq h(P)\leq 4+3N/n with 0 ≤ ε n = O ⁡ ( 1 n 2) 0\leq\varepsilon_{n}=O\left(\frac{1}{n^{2}}\right). Moreover, if N = 1 N=1 then h ⁡ ( P) = 4 − 8 n 2 − n + 2 h(P)=4-\mbox{$\frac{8}{n^{2}-n+2}$}.

*Proof.*Let 𝖦 {\sf G} denote the symmetry group of P P (so N = | 𝖦 | N=|{\sf G}|). Let us put M = def | 𝖮𝖳 aff P | M\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}|, 𝖮𝖳 P aff = { ω 1, ω 2, …, ω M } {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}=\{\omega_{1},\omega_{2},\ldots,\omega_{M}\} and H = def h ⁡ ( P) = 1 M ​ ∑ i = 1 M h ⁡ ( ω i) H\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}h(P)=\frac{1}{M}\sum_{i=1}^{M}h(\omega_{i}). Let μ i = def | 𝖦 ⁡ ( ω i) | \mu_{i}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|{\sf G}(\omega_{i})|; by Corollary 3.6, μ i \mu_{i} is the number of affine hemisets of P P with order type ω i \omega_{i}.

By Lemma 4.2, affine hemisets of P P are in bijection with cells of P ∗ P^{*}, of which there are 2 ​ ( n 2) + 2 2{n\choose 2}+2. Also, a point p p is extreme in an affine hemiset of P P if and only if p ∗ p^{*} supports an edge of the corresponding cell; there are 4 ​ ( n 2) 4{n\choose 2} edges, and each edge is adjacent to two cells. Altogether we obtain

 | ∑ i = 1 M μ i = 2 ​ ( n 2) + 2 and ∑ i = 1 M μ i ​ h ​ ( ω i) = 8 ​ ( n 2). \sum_{i=1}^{M}\mu_{i}=2{n\choose 2}+2\qquad\mbox{and}\qquad\sum_{i=1}^{M}\mu_{i}h(\omega_{i})=8{n\choose 2}~. |  | (10) |

Let K ′ K^{\prime} be the number of order types in 𝖮𝖳 aff P {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P} with nontrivial symmetry group. We claim that K ′ ≤ 3 K^{\prime}\leq 3. Indeed, by Lemma 3.5 the order types of 𝖮𝖳 aff P {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P} correspond to the orbits of affine hemisets of P P under 𝖦 {\sf G}. Moreover, for every affine hemiset A A in the orbit of ω i \omega_{i}, the stabilizer 𝖦 A {\sf G}_{A} is isomorphic to the symmetry group of ω i \omega_{i}. Hence, when this group is nontrivial, the orbit consists of poles of P P; there are at most three such orbits by Proposition 6.1. Let us stress that K ′ K^{\prime} counts only affine pole orbits, whereas Proposition 6.1 also accounts for non-affine pole orbits.

When K ′ = 0 K^{\prime}=0, which holds, in particular, for 𝖦 {\sf G} the trivial group, we have M = 2 ​ ( n 2) + 2 M=2{n\choose 2}+2 and μ i = 1 \mu_{i}=1 for all i = 1, 2, …, M i=1,2,\ldots,M, and we obtain

 | H = 1 M ​ ∑ i = 1 M h ⁡ ( ω i) = 8 ​ ( n 2) 2 ​ ( n 2) + 2 = 4 − 8 n 2 − n + 2, H=\frac{1}{M}{\sum_{i=1}^{M}h(\omega_{i})}=\frac{8{n\choose 2}}{2{n\choose 2}+2}=4-\mbox{$\frac{8}{n^{2}-n+2}$}~, |  | (11) |

as for labeled order types. This gives us the last statement.

So assume that 1 ≤ K ′ ≤ 3 1\leq K^{\prime}\leq 3 and that we have ordered 𝖮𝖳 aff P {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P} so that the K ′ K^{\prime} order types with nontrivial symmetry group are ω 1, …, ω K ′ \omega_{1},\ldots,\omega_{K^{\prime}}. We therefore have μ i < N \mu_{i}<N for i ≤ K ′ i\leq K^{\prime} and, by Corollary 3.6, μ i = N \mu_{i}=N for i > K ′ i>K^{\prime}. Equation ( 10)-right can be rewritten as

 | 8 ​ ( n 2) = \displaystyle 8{n\choose 2}= | ∑ i = 1 M μ i ​ h ​ ( ω i) = N ​ ∑ i = 1 M h ⁡ ( ω i) − ∑ i ≤ K ′ ( N − μ i) ​ h ​ ( ω i) \displaystyle\sum_{i=1}^{M}\mu_{i}h(\omega_{i})=N\sum_{i=1}^{M}h(\omega_{i})-\sum_{i\leq K^{\prime}}(N-\mu_{i})h(\omega_{i}) |  |

 |  | ⇒ M ​ H = 1 N ​ ( 8 ​ ( n 2) + ∑ i ≤ K ′ ( N − μ i) ​ h ​ ( ω i)). \displaystyle\Rightarrow\qquad MH=\frac{1}{N}\left(8{n\choose 2}+\sum_{i\leq K^{\prime}}(N-\mu_{i})h(\omega_{i})\right). |  |

For the same reason, Equation ( 10)-left can be rewritten as

 | 2 ​ ( n 2) + 2 = \displaystyle 2{n\choose 2}+2= | ∑ i = 1 M μ i = N ​ M − ∑ i ≤ K ′ ( N − μ i) \displaystyle\sum_{i=1}^{M}\mu_{i}=NM-\sum_{i\leq K^{\prime}}(N-\mu_{i}) |  |

 |  | ⇒ M = 1 N ​ ( 2 ​ ( n 2) + 2 + ∑ i ≤ K ′ ( N − μ i)) \displaystyle\Rightarrow\qquad M=\frac{1}{N}\left(2{n\choose 2}+2+\sum_{i\leq K^{\prime}}(N-\mu_{i})\right) |  |

Together, this gives H = 4 + Δ H=4+\Delta where Δ = def − 8 + ∑ i ≤ K ′ ( N − μ i) ​ ( h ⁡ ( ω i) − 4) 2 ​ ( n 2) + 2 + ∑ i ≤ K ′ ( N − μ i) \Delta\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\frac{\displaystyle-8+\sum_{i\leq K^{\prime}}(N-\mu_{i})(h(\omega_{i})-4)}{\displaystyle 2{n\choose 2}+2+\sum_{i\leq K^{\prime}}(N-\mu_{i})}.

On the one hand,

 | Δ ≤ ∑ i ≤ K ′ N ⁡ ( h ⁡ ( ω i) − 1) 2 ​ ( n 2) ≤ K ′ ​ N ​ ( n − 1) n ⁡ ( n − 1) ≤ 3 ​ N n, \Delta\leq\frac{\displaystyle\sum_{i\leq K^{\prime}}N(h(\omega_{i})-1)}{\displaystyle 2{n\choose 2}}\leq\frac{K^{\prime}N(n-1)}{n(n-1)}\leq 3\frac{N}{n}, |  |

which proves the upper bound. For the lower bound, recall that the order of the symmetry group of ω i \omega_{i} equals N / μ i N/\mu_{i} and must divide h ⁡ ( ω i) h(\omega_{i}). Now, if the numerator of Δ \Delta is less than − 8 -8, there must exist some i i, 1 ≤ i ≤ K ′ 1\leq i\leq K^{\prime}, with h ⁡ ( ω i) = 3 h(\omega_{i})=3. By Proposition 6.1, this can happen only for ( N, μ i) ∈ { ( 3, 1), ( 6, 2), ( 12, 4), ( 24, 8), ( 60, 20) } (N,\mu_{i})\in\{(3,1),(6,2),(12,4),(24,8),(60,20)\}. Hence

 | Δ ≥ − 8 − 3 ⋅ 40 2 ​ ( n 2) = − 128 n ⁡ ( n − 1), \Delta\geq\frac{\displaystyle-8-3\cdot 40}{\displaystyle 2{n\choose 2}}=-\frac{128}{n(n-1)}, |  |

which proves the lower bound.

### 6.4 Counting extreme points in affine order types

We now build on Proposition 6.4 to prove Theorem 1.3. The main issue is the factor N / n N/n: projective order types with Ω ⁡ ( n) \Omega(n) symmetries may contribute substantially more than 4 4 to the average. We keep them in check using Proposition 6.3 and the following consequence of Proposition 6.1.

###### Corollary 6.5.

Any projective order type with N > 60 N>60 symmetries contains an affine hemiset with at least N / 2 N/2 symmetries.

*Proof of Theorem 1.3.*The lower bound of Proposition 6.4 immediately implies that the average number of extreme points is at least 4 − O ⁡ ( n − 2) 4-O(n^{-2}). We therefore focus on the upper bound.

If two affine sets A 1 A_{1}, A 2 A_{2} have the same affine order type, then their projective completions A 1 ∪ − A 1 A_{1}\cup-A_{1} and A 2 ∪ − A 2 A_{2}\cup-A_{2} have the same projective order type. Thus, the family { 𝖮𝖳 π aff ∣ π ∈ 𝖮𝖳 n proj } \{{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi}\mid\pi\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n}\} partitions 𝖮𝖳 aff n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}. It follows that | 𝖮𝖳 aff n | = ∑ π ∈ 𝖮𝖳 proj n | 𝖮𝖳 aff π | |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|=\sum_{\pi\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{proj}}}_{\!n}}|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi}|, and

 | ∑ ω ∈ 𝖮𝖳 aff n h ( ω) = ∑ π ∈ 𝖮𝖳 proj n ∑ ω ∈ 𝖮𝖳 aff π h ( ω). \sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!n}}h(\omega)=\sum_{\pi\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{proj}}}_{\!n}}\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!\pi}}h(\omega). |  | (12) |

For n ∈ ℕ n\in\mathbb{N} and N 0 ∈ ℝ N_{0}\in\mathbb{R}, let 𝖮𝖳 proj n, ≥ N 0 {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n,\geq N_{0}} (resp. 𝖮𝖳 proj n, < N 0 {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n,<N_{0}}) denote the number of projective order types π \pi with | π | = 2 ​ n |\pi|=2n and | 𝖦 π | ≥ N 0 |{\sf G}_{\pi}|\geq N_{0} (resp. | 𝖦 π | < N 0 |{\sf G}_{\pi}|<N_{0}). For any N 0 N_{0}, 1 ≤ N 0 ≤ n 1\leq N_{0}\leq n, we can inject the bounds of Proposition 6.4 in Equation ( 12) and obtain (we use N ≤ min ⁡ { 2 ​ n, 60 } N\leq\min\{2n,60\} and therefore N / n = O ⁡ ( 1) N/n=O(1)):

 | ∑ ω ∈ 𝖮𝖳 aff n h ( ω) \displaystyle\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!n}}h(\omega) | = ∑ π ∈ 𝖮𝖳 proj n, < N 0 ∑ ω ∈ 𝖮𝖳 aff π h ( ω) + ∑ π ∈ 𝖮𝖳 proj n, ≥ N 0 ∑ ω ∈ 𝖮𝖳 aff π h ( ω) \displaystyle=\sum_{\pi\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{proj}}}_{\!n,<N_{0}}}\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!\pi}}h(\omega)+\sum_{\pi\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{proj}}}_{\!n,\geq N_{0}}}\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!\pi}}h(\omega) |  |

 |  | ≤ 4 | 𝖮𝖳 aff n | + ∑ π ∈ 𝖮𝖳 proj n, < N 0 3 N 0 n | 𝖮𝖳 aff π | + ∑ π ∈ 𝖮𝖳 proj n, ≥ N 0 O ( 1) | 𝖮𝖳 aff π | \displaystyle\leq\ 4\,|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|+\sum_{\pi\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{proj}}}_{\!n,<N_{0}}}3\,\frac{N_{0}}{n}|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi}|+\sum_{\pi\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{proj}}}_{\!n,\geq N_{0}}}O(1)\ |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi}| |  |

 |  | ≤ ( 4 + 3 N 0 / n) | 𝖮𝖳 aff n | + O ( n 2) | 𝖮𝖳 proj n, ≥ N 0 |. \displaystyle\leq\ \left(4+3N_{0}/n\right)|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|+O(n^{2})|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n,\geq N_{0}}|. |  |

We cut off at N 0 = 2 ​ n 2 ​ c N_{0}=2n^{2c}, with 0 < c < 1 2 0<c<\frac{1}{2} to be specified shortly. By Corollary 6.5, the number of projective order types with at least N 0 N_{0} symmetries is at most the number of affine order types with at least N 0 2 \frac{N_{0}}{2} symmetries. By Proposition 6.3, the latter is at most

 | ∑ k = N 0 2 n ( c 0 ​ n k) 4 ​ n ≤ n ​ ( c 0 ​ n N 0 / 2) 4 ​ n = c 0 4 ​ n ​ n 4 ​ ( 1 − c) ​ n + 1. \sum_{k=\frac{N_{0}}{2}}^{n}\left(c_{0}\frac{n}{\sqrt{k}}\right)^{4n}\leq n\left(c_{0}\frac{n}{\sqrt{N_{0}/2}}\right)^{4n}={c_{0}}^{4n}n^{4(1-c)n+1}. |  |

Crudely factoring out symmetries – by dividing by n! n! – in the Goodman-Pollack lower bound of ( n!) 4 / 2 3 ​ n (n!)^{4}/2^{3n} on the number of labeled order types [32, § ​ 5 \mathsection 5], we get | 𝖮𝖳 n aff | ≥ ( c 2 n) 3 ​ n + O ⁡ ( 1) |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|\geq(c_{2}n)^{3n+O(1)} for some constant c 2 c_{2}. The bound therefore becomes

 | 1 | 𝖮𝖳 aff n | ∑ ω ∈ 𝖮𝖳 aff n h ( ω) ≤ 4 + 3 n 2 ​ c − 1 + O ( n 2) c 0 4 ​ n ​ n 4 ​ ( 1 − c) ​ n + 1 c 2 3 ​ n ​ n 3 ​ n + O ⁡ ( 1) = 4 + 3 n 2 ​ c − 1 + n O ⁡ ( 1) c 3 n n ( 1 − 4 ​ c) ​ n \frac{1}{|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|}\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!n}}h(\omega)\leq 4+3n^{2c-1}+O(n^{2})\frac{{c_{0}}^{4n}n^{4(1-c)n+1}}{{c_{2}}^{3n}n^{3n+O(1)}}=4+3n^{2c-1}+n^{O(1)}{c_{3}}^{n}n^{(1-4c)n} |  |

for some constant c 3 c_{3}. Taking c = def 1 4 + log ⁡ c 4 log ⁡ n c\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\frac{1}{4}+\frac{\log c_{4}}{\log n}, for some c 4 > c 3 4 c_{4}>\sqrt[4]{c_{3}}, we get

 | 1 | 𝖮𝖳 aff n | ∑ ω ∈ 𝖮𝖳 aff n h ( ω) ≤ 4 + 3 n − 1 2 + 2 ​ log ⁡ c 4 log ⁡ n + n O ⁡ ( 1) c 3 n n − 4 ​ log ⁡ c 4 log ⁡ n ​ n ⏟ c 4 − 4 ​ n ≤ 4 + O ( n − 1 2 + O ⁡ ( 1 log ⁡ n)) \frac{1}{|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|}\sum_{\omega\in{\sf O\hskip-0.70004ptT}^{{}_{\mathrm{aff}}}_{\!n}}h(\omega)\leq 4+3n^{-\frac{1}{2}+\frac{2\log c_{4}}{\log n}}+n^{O(1)}c_{3}^{n}\,\underbrace{n^{-\frac{4\log c_{4}}{\log n}n}}_{c_{4}^{-4n}}\leq 4+O\left(n^{-\frac{1}{2}+O(\frac{1}{\log n})}\right) |  |

as announced.

## 7 Concentration of (labeled) order types of random point sets

Let us now turn our attention to the efficiency of random sampling methods for order types based on sampling point sets. We start by a sufficient condition for a family of distributions on ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} to exhibit concentration.

###### Proposition 7.1.

Let μ n \mu_{n} be a probability distribution on ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} and let Z n Z_{n} denote the number of extreme points in a (labeled) order type chosen from μ n \mu_{n}. If 𝔼 [Z n] → n → ∞ ∞ \mathbb{E}\left[Z_{n}\right]\to_{n\to\infty}\infty and Var ​ [Z n] = o ⁡ ( 𝔼 ​ [Z n] 2) \textrm{Var}\left[Z_{n}\right]=o\left(\mathbb{E}\left[Z_{n}\right]^{2}\right), then { μ n } n ≥ 3 \{\mu_{n}\}_{n\geq 3} exhibits concentration.

*Proof.*We let ℒ n \mathcal{L}_{n} denote the set of (labeled) planar, simple order types of size n n with at least 𝔼 ⁡ [Z n] / 2 \mathbb{E}\left[Z_{n}\right]/2 extreme points. On one hand, by Markov’s inequality and Theorem 1.3 (Theorem 1.2, resp.), we have

 | | ℒ n | | ( 𝖫) 𝖮𝖳 aff n | ≤ 4 + o ⁡ ( 1) 𝔼 ⁡ [Z n] / 2 → n → ∞ 0, \frac{|\mathcal{L}_{n}|}{|{\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|}\leq\frac{4+o(1)}{{\mathbb{E}\left[Z_{n}\right]/2}}\to_{n\to\infty}0, |  |

so ℒ n \mathcal{L}_{n} is a vanishingly small part of ( 𝖫) 𝖮𝖳 n aff {\sf(\hskip-0.80002ptL\hskip-0.80002pt)O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}. On the other hand, the Bienaymé-Chebyshev inequality ensures that for any real t > 0 t>0,

 | ℙ [| Z n − 𝔼 [Z n] | ≥ t Var ​ [Z n]] ≤ 1 t 2. \mathbb{P}\left[|Z_{n}-\mathbb{E}\left[Z_{n}\right]|\geq t\sqrt{\textrm{Var}\left[Z_{n}\right]}\right]\leq\frac{1}{t^{2}}. |  |

Let us take t = 𝔼 ⁡ [Z n] 2 ​ Var ​ [Z n] t=\frac{\mathbb{E}\left[Z_{n}\right]}{2\sqrt{\textrm{Var}\left[Z_{n}\right]}}, so that

 | ℙ [Z n ≤ 𝔼 ⁡ [Z n] 2] ≤ ℙ [| Z n − 𝔼 [Z n] | ≥ 𝔼 ⁡ [Z n] 2] ≤ 4 ​ Var ​ [Z n] 𝔼 ​ [Z n] 2, \mathbb{P}\left[Z_{n}\leq{\frac{\mathbb{E}\left[Z_{n}\right]}{2}}\right]\leq\mathbb{P}\left[|Z_{n}-\mathbb{E}\left[Z_{n}\right]|\geq{\frac{\mathbb{E}\left[Z_{n}\right]}{2}}\right]\leq{\frac{4\textrm{Var}\left[Z_{n}\right]}{\mathbb{E}\left[Z_{n}\right]^{2}}}, |  |

which goes to 0 0. This ensures that the probability that a (labeled) order type chosen from μ n \mu_{n} lies in ℒ n \mathcal{L}_{n} goes to 1 1.

Theorem 1.1 follows from Proposition 7.1 and previous work in stochastic geometry.

*Proof of Theorem 1.1.*Let μ \mu be a probability distribution on ℝ 2 \mathbb{R}^{2} and let Z n Z_{n} denote the random variable counting the extreme points in a set (or sequence) of n n random points chosen independently from μ \mu.

When μ \mu is the uniform probability distribution in a compact convex set K K, 𝔼 ⁡ [Z n] \mathbb{E}\left[Z_{n}\right] is Ω ⁡ ( log ⁡ n) \Omega(\log n) [8, Theorems 1–2]. For K K smooth, Vu [62, Corollary 2.12] proved that Var ​ [Z n] = Θ ⁡ ( 𝔼 ⁡ [Z n]) \textrm{Var}\left[Z_{n}\right]=\Theta\left(\mathbb{E}\left[Z_{n}\right]\right). For K K a polygon, Bárány and Reitzner [9] proved that Var ​ [Z n] = Θ ⁡ ( 𝔼 ⁡ [Z n]) \textrm{Var}\left[Z_{n}\right]=\Theta\left(\mathbb{E}\left[Z_{n}\right]\right). Proposition 7.1 therefore applies.

When μ \mu is a Gaussian distribution on ℝ 2 \mathbb{R}^{2}, 𝔼 ⁡ [Z n] \mathbb{E}\left[Z_{n}\right] is Ω ⁡ ( log ⁡ n) \Omega(\sqrt{\log n}) and Var ​ [Z n] = Θ ⁡ ( 𝔼 ⁡ [Z n]) \textrm{Var}\left[Z_{n}\right]=\Theta\left(\mathbb{E}\left[Z_{n}\right]\right), see [51, § ​ 2.3 \mathsection 2.3].

## 8 Order types with excluded patterns

Building on the affine-projective relation (Section 3), the correspondence between affine hemisets and dual cells (Lemma 4.2), and the classification of affine symmetries, we can now prove that certain order types are hard to avoid.

*Proof of Theorem 1.4.*Fix k k and let τ \tau be the k k -point order type with three extreme points, and whose k − 3 k-3 interior points form a convex chain together with two of the extreme points. 16 16 16 For the reader familiar with this terminology, this is equivalent to saying that τ \tau is the order type obtained from k k points in convex position by sending a line cutting off one point to infinity.

Let n n be large enough such that any n / 2 n/2 points in general position in the plane contain a convex 2 ​ k 2k -gon (see Suk [58] for the most recent bounds). Let P P be a projective set of 2 ​ n 2n points in general position. We claim that for every projective set P P of size 2 ​ n 2n, there are at most two affine hemisets of P P (an affine hemiset and its antipodal set) whose order types do not contain τ \tau. This shows that at most two of the affine order types in 𝖮𝖳 aff P {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P} avoid τ \tau. Since | 𝖮𝖳 P aff | = Ω ( n) |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}|=\Omega(n) we obtain that the number of n n -point affine order types that do not contain τ \tau is at most O ( n − 1) | 𝖮𝖳 n aff | O(n^{-1})|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}|. The fact that | 𝖮𝖳 P aff | = Ω ( n) |{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!P}|=\Omega(n) follows from (i) that the number of affine hemisets of P P equals the number of cells of P ∗ P^{*}, that is, 2 ​ ( n 2) + 2 2{n\choose 2}+2 (Lemma 4.2), (ii) an order type ω \omega appears with multiplicity | 𝖦 | / | 𝖥 | |{\sf G}|/|{\sf F}| ( 𝖦 {\sf G} and 𝖥 {\sf F} the symmetry groups of P P and A A, resp., Corollary 3.6), and (iii) | 𝖦 | ≤ max ⁡ { 60, 2 ​ n } |{\sf G}|\leq\max\{60,2n\} (Corollary 6.5 and Theorem 1.5).

It remains to prove the claim. So suppose P P has an affine hemiset A A with no subset of order type τ \tau. Let Σ {\Sigma} be a closed hemisphere such that A ′ = def P ∩ Σ A^{\prime}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}P\cap{\Sigma} is an affine hemiset of P P distinct from A A and − A -A. We want to show that A ′ A^{\prime} has a subset of order type τ \tau. Let C {C} be the great circle bounding Σ {\Sigma}. Since A ≠ A ′ ≠ − A A\neq A^{\prime}\neq-A, there are points of A A on both sides of C {C}. We fix a point p ∈ A p\in A such that the side of C {C} not containing p p has at least as many points in A A as the side containing p p. That is, the other side of C {C} has at least n / 2 n/2 points of A A, so it must contain a subset D D of 2 ​ k 2k points in convex position. W.l.o.g. let us assume that p ∉ A ′ p\not\in A^{\prime}, so that D ∪ { − p } ⊆ A ′ D\cup\{-p\}\subseteq A^{\prime} (otherwise, switch from A ′ A^{\prime} to − A ′ -A^{\prime} and observe that τ \tau appears in A ′ A^{\prime} if and only if it appears in − A ′ -A^{\prime}). Let q 1 q_{1} and q 2 q_{2} denote the neighbors of p p on the convex hull of the affine set D ∪ { p } ⊆ A D\cup\{p\}\subseteq A. Note that q 1 q_{1} and q 2 q_{2} are also the neighbors of − p -p on the convex hull of D ∪ { − p } ⊆ − A ′ D\cup\{-p\}\subseteq{\color[rgb]{0.6,0.6,0.6}-}A^{\prime}. Since A A has no subset of order type τ \tau, the interior of the triangle p ​ q 1 ​ q 2 pq_{1}q_{2} must contain less than k − 3 k-3 points of D D. Then, p ∪ D p\cup D has at least k + 5 k+5 extreme points, and { − p } ∪ D ⊆ − A ′ \{-p\}\cup D\subseteq{\color[rgb]{0.6,0.6,0.6}-}A^{\prime} contains a subset of order type τ \tau.

## 9 Classification of projective symmetries and their pole orbits

This section analyzes further the symmetry groups of projective sets, and their orbit structure. While this is not essential for the targeted results of this paper, we consider this of independent interest. It should be made clear that the orbit type per se, as we considered it so far, does not say much about the underlying group. Still, together with the special properties of the groups we have at hand, we can derive properties of the cyclic subgroups that can occur in the symmetry groups. Building on this, we will derive the classification.

Given two groups H, G H,G, let us write H ≤ G H\leq G to mean that H H is a subgroup of G G. For a group G G and an element g ∈ G g\in G, we write ⟨ g ⟩ \langle g\rangle for the subgroup of G G generated by g g. Note that if G G is finite then ⟨ g ⟩ \langle g\rangle is cyclic.

### 9.1 From pole stabilizers to maximal cyclic subgroups

A *maximal cyclic subgroup*of a group G G is a cyclic subgroup of G G that is not properly contained in another cyclic subgroup of G G. We next relate the maximal cyclic subgroups of the symmetry group of a projective point set to the stabilizers of its hemisets. Before that, we should get some hold on the symmetry groups of *non-affine*hemisets.

###### Lemma 9.1.

Let B B be a non-affine hemiset of a projective set P P of at least 6 6 points in general position, with 𝖦 {\sf G} the symmetry group of P P. The symmetry group of B B (and thus the stabilizer 𝖦 B {\sf G}_{B} of B B) is either trivial, or cyclic of order 2 2 or 4 4.

*Proof.*Proposition 3.2 (ii) and Lemma 3.8 show that the symmetry group 𝖥 {\sf F} of a non-affine hemiset B B has order at most | B ∩ − B | ∈ { 2, 4 } |B\cap-B|\in\{2,4\}. That is, we are done if | B ∩ − B | = 2 |B\cap-B|=2, since the only group of order 2 2 is cyclic. So let us assume that B ∩ − B = { p, − p, q, − q } B\cap-B=\{p,-p,q,-q\}. Consider first a symmetry g g with g ⁡ ( p) = q g(p)=q. Every point of B B is on the same side of the great circle through p p and q q, so we cannot have g ⁡ ( q) = p g(q)=p: indeed, for any r ∈ B ∖ { p, − p, q, − q } r\in B\setminus\{p,-p,q,-q\} we would have χ ⁡ ( p, q, r) = χ ⁡ ( g ⁡ ( p), g ⁡ ( q), g ⁡ ( r)) = χ ⁡ ( q, p, g ⁡ ( r)) = − χ ⁡ ( p, q, g ⁡ ( r)) {\chi}(p,q,r)={\chi}(g(p),g(q),g(r))={\chi}(q,p,g(r))=-{\chi}(p,q,g(r)), a contradiction. This implies g ⁡ ( q) = − p g(q)=-p, and thus the symmetry g g is determined by Lemma 3.3 (i) as p ↦ q ↦ − p ↦ − q ↦ p p\mapsto q\mapsto-p\mapsto-q\mapsto p. This mapping generates a cyclic group of order 4 4. Similarly, if p ↦ − q p\mapsto-q. Otherwise, if p p maps neither to q q nor to − q -q, the symmetry group is either trivial or of order 2 2, thus cyclic. By Lemma 3.5 (a), 𝖦 B {\sf G}_{B} is isomorphic to 𝖥 {\sf F}.

We now have the following correspondence.

###### Proposition 9.2.

Let P P be a projective set, | P | ≥ 6 |P|\geq 6, in general position, with symmetry group 𝖦 {\sf G}.

1. (i)

For every hemiset B B of P P, the stabilizer 𝖦 B {\sf G}_{B} is trivial or a maximal cyclic subgroup of 𝖦 {\sf G}.

2. (ii)

For every maximal cyclic subgroup C ≤ 𝖦 C\leq{\sf G}, if nontrivial, there are exactly two hemisets B 0 B_{0}, B 1 B_{1} of P P such that C = 𝖦 B 0 = 𝖦 B 1 C={\sf G}_{B_{0}}={\sf G}_{B_{1}}; moreover, B 0 = − B 1 B_{0}=-B_{1}.

*Proof.*Let B B be a hemiset of P P with 𝖦 B ≠ { 𝗂𝖽 } {\sf G}_{B}\neq\{{\sf id}\}. First, note that 𝖦 B {\sf G}_{B} is cyclic (if B B is an affine hemiset, by Lemma 3.5 (i) and Theorem 1.5, and if B B is a not affine, by Lemma 9.1). We now argue that 𝖦 B {\sf G}_{B}, when nontrivial, is a maximal cyclic subgroup of 𝖦 {\sf G}. Suppose that 𝖦 B ≤ C ≤ 𝖦 {\sf G}_{B}\leq C\leq{\sf G}, for C = ⟨ g 0 ⟩ C=\langle g_{0}\rangle a cyclic group. By Proposition 5.1, g 0 g_{0} has two poles, which we denote by B ′ B^{\prime} and − B ′ -B^{\prime}. Any g ∈ G B ∖ { 𝗂𝖽 } g\in G_{B}\setminus\{{\sf id}\} is in C C and therefore writes g = g 0 i g=g_{0}^{i} for some integer i i. This implies that B ′ B^{\prime} is a pole of g g, since g ⁡ ( B ′) = g 0 i ​ ( B ′) = B ′ g(B^{\prime})=g_{0}^{i}(B^{\prime})=B^{\prime}, and by Proposition 5.1 we must have B ′ = B B^{\prime}=B or B ′ = − B B^{\prime}=-B. In either case g 0 ∈ G B g_{0}\in G_{B} and thus G B = C G_{B}=C. This proves statement (i).

Now, let C = ⟨ g 0 ⟩ C=\langle g_{0}\rangle be a maximal cyclic subgroup of 𝖦 {\sf G}. Let ± B \pm B be the poles of g 0 g_{0}, as per Proposition 5.1. For every g ∈ C g\in C, we have g ⁡ ( B) = B g(B)=B, so C ≤ 𝖦 B C\leq{\sf G}_{B}. Since 𝖦 B {\sf G}_{B} is cyclic, it follows that C = 𝖦 B C={\sf G}_{B}. The same argument gives C = 𝖦 − B C={\sf G}_{-B}. Finally, for every hemiset B ′ B^{\prime} of P P distinct from ± B \pm B, we must have g 0 ​ ( B ′) ≠ B ′ g_{0}(B^{\prime})\neq B^{\prime} by Proposition 5.1, and C ≠ 𝖦 B ′ C\neq{\sf G}_{B^{\prime}}. This proves statement (ii).

A first structural consequence is that projective symmetry groups are what is called *completely decomposable*[59], that is, they have the following property:

###### Corollary 9.3.

For any two maximal cyclic subgroups C C, C ′ C^{\prime} of a projective symmetry group 𝖦 {\sf G} we have C ∩ C ′ = { 𝗂𝖽 } C\cap C^{\prime}=\{{\sf id}\}.

*Proof.*Any nontrivial element in 𝖦 {\sf G} has exactly two poles by Proposition 5.1 and therefore belongs to exactly one maximally cyclic subgroup of 𝖦 {\sf G} by Proposition 9.2 (ii).

Another consequence is that the action of a projective symmetry group on the poles of a projective point set completely reveals its number of maximal cyclic subgroups. Given a group G G, let 𝗆𝖼𝗌 i ​ ( G) {\sf mcs}_{i}(G) denote the number of maximal cyclic subgroups of cardinality i i of G G.

###### Corollary 9.4.

Let P P be a projective set, | P | ≥ 6 |P|\geq 6, in general position, with symmetry group 𝖦 {\sf G}. For any i ≥ 1 i\geq 1, the action of 𝖦 {\sf G} on the poles of P P has exactly 2 ​ i | 𝖦 | ​ 𝗆𝖼𝗌 i ​ ( 𝖦) \frac{2i}{|{\sf G}|}{\sf mcs}_{i}({\sf G}) orbits of size | 𝖦 | / i |{\sf G}|/i.

*Proof.*Let 𝒫 i \mathcal{P}_{i} be the set of poles of P P with stabilizer of cardinality i i. By Proposition 9.2, | 𝒫 i | = 2 ​ 𝗆𝖼𝗌 i ​ ( 𝖦) |\mathcal{P}_{i}|=2\,{\sf mcs}_{i}({\sf G}). The action of 𝖦 {\sf G} on the poles of P P partitions 𝒫 i \mathcal{P}_{i} into orbits, since two poles in the same orbit have isomorphic stabilizers. Each orbit in 𝒫 i \mathcal{P}_{i} has size | 𝖦 | / i |{\sf G}|/i by the orbit-stabilizer theorem, so there must be 2 ​ i | 𝖦 | ​ 𝗆𝖼𝗌 i ​ ( 𝖦) \frac{2i}{|{\sf G}|}{\sf mcs}_{i}({\sf G}) orbits in 𝒫 i \mathcal{P}_{i}.

By Corollary 9.4, the orbit type determines the number of maximal cyclic subgroups of each size, and vice-versa. In particular, a projective symmetry group has a single orbit type (a fact that is not obvious otherwise). Proposition 6.1 therefore yields the information summarized in Table 1.

 | | 𝖦 | orbit type maximal cyclic subgroup statistics 𝖦 N [1, 1] ⇔ 𝗆𝖼𝗌 N = 1 ℤ N 4 [2, 2, 2] ⇔ 𝗆𝖼𝗌 2 = 3 D 2 N > 4 [2, N / 2, N / 2] ⇔ 𝗆𝖼𝗌 2 = N / 2, 𝗆𝖼𝗌 N / 2 = 1 D N / 2 12 [4, 4, 6] ⇔ 𝗆𝖼𝗌 2 = 3, 𝗆𝖼𝗌 3 = 4 A 4 24 [6, 8, 12] ⇔ 𝗆𝖼𝗌 2 = 6, 𝗆𝖼𝗌 3 = 4, 𝗆𝖼𝗌 4 = 3 S 4 60 [12, 20, 30] ⇔ 𝗆𝖼𝗌 2 = 15, 𝗆𝖼𝗌 3 = 10, 𝗆𝖼𝗌 5 = 6 A 5 \begin{array}[]{c|ccccc|c}|{\sf G}|&&\mbox{orbit type}&&\mbox{maximal cyclic subgroup statistics}&&{\sf G}\\ \hline\cr N&&[1,1]&\Leftrightarrow&{\sf mcs}_{N}=1&&\mathbb{Z}_{N}\\ 4&&[2,2,2]&\Leftrightarrow&{\sf mcs}_{2}=3&&D_{2}\\ N>4&&[2,N/2,N/2]&\Leftrightarrow&{\sf mcs}_{2}=N/2,\ {\sf mcs}_{N/2}=1&&D_{N/2}\\ 12&&[4,4,6]&\Leftrightarrow&{\sf mcs}_{2}=3,\ {\sf mcs}_{3}=4&&A_{4}\\ 24&&[6,8,12]&\Leftrightarrow&{\sf mcs}_{2}=6,\ {\sf mcs}_{3}=4,\ {\sf mcs}_{4}=3&&S_{4}\\ 60&&[12,20,30]&\Leftrightarrow&{\sf mcs}_{2}=15,\ {\sf mcs}_{3}=10,\ {\sf mcs}_{5}=6&&A_{5}\par\end{array} |  |

Table 1: Orbit types of symmetry groups with maximal cyclic subgroup statistics. The last column anticipates the implied classification to follow below in Section 9.2.

### 9.2 Group classification

We now analyze the possible group structure of 𝖦 {\sf G}, proving Theorem 1.6 on the way.

#### 9.2.1 Infinite cases: cyclic and dihedral

Let us first dispose of the cases where the order may be arbitrarily large. Let 𝖦 {\sf G} be a projective symmetry group and let N = def | 𝖦 | N\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|{\sf G}|. Recall that every element g ∈ 𝖦 g\in{\sf G} generates a cyclic subgroup { 𝗂𝖽, g, g 2, … } ≤ 𝖦 \{{\sf id},g,g^{2},\ldots\}\leq{\sf G} and is therefore contained in some maximal cyclic subgroup.

If 𝖦 {\sf G} has orbit type [1, 1] [1,1], then it has a single maximal cyclic subgroup, with | 𝖦 | |{\sf G}| elements. Hence, 𝖦 ≃ ℤ N {\sf G}\simeq\mathbb{Z}_{N}.

Now assume that 𝖦 {\sf G} has orbit type [2, N / 2, N / 2] [2,N/2,N/2]. For N = 4 N=4, we have 𝗆𝖼𝗌 2 ​ ( 𝖦) = 3 {\sf mcs}_{2}({\sf G})=3 so 𝖦 {\sf G} is a group with 4 4 elements that is not cyclic. The only possibility is the dihedral group D 2 D_{2}. For N > 4 N>4, we have 𝗆𝖼𝗌 2 ​ ( 𝖦) = N / 2 {\sf mcs}_{2}({\sf G})=N/2 and 𝗆𝖼𝗌 N / 2 ​ ( 𝖦) = 1 {\sf mcs}_{N/2}({\sf G})=1. Let g 0 g_{0} be a generator of the maximal cyclic subgroup of order N / 2 N/2. Let g 1 ∈ 𝖦 ∖ ⟨ g 0 ⟩ g_{1}\in{\sf G}\setminus\langle g_{0}\rangle. Note that Corollary 9.3 implies that both g 1 g_{1} and g 0 ​ g 1 g_{0}g_{1} are of order 2 2. Thus, the subgroup generated by g 0 g_{0} and g 1 g_{1} is the dihedral group D N / 2 = ⟨ g 0, g 1 ∣ g 0 N / 2 = g 1 2 = ( g 0 g 1) 2 = 𝗂𝖽 ⟩ D_{N/2}=\langle g_{0},g_{1}\mid g_{0}^{N/2}=g_{1}^{2}=(g_{0}g_{1})^{2}={\sf id}\rangle. Since 𝖦 {\sf G} and D N / 2 D_{N/2} have equal cardinalities, it must be that 𝖦 ≃ D N / 2 {\sf G}\simeq D_{N/2}.

#### 9.2.2 Finite cases: shortcuts

For the remaining three cases, a natural approach is to compare the information of Table 1 to the classification of finite groups. For instance, for orbit type [4, 4, 6] [4,4,6], the group has 12 12 elements, none of which has order more than 3 3. From the 17 17 17 Here we used [https://groupprops.subwiki.org/wiki/Groups_of_order_12][2]. five groups of size 12 12, this readily rules out the cyclic group ℤ 12 \mathbb{Z}_{12}, the dihedral group D 12 D_{12}, the direct product ℤ 6 × ℤ 2 \mathbb{Z}_{6}\times\mathbb{Z}_{2}, as well as the dicyclic group Dic 12 {\rm Dic}_{12} which has an element of order 4 4. This leaves A 4 A_{4} as the only possibility.

For a geometer, this does not provide much insight. We thus provide an alternative proof that trades specific knowledge of groups of size 12 12, 24 24 and 60 60 for some analysis of the orbits. We let 𝖦 {\sf G} be a projective symmetry group, let N = def | 𝖦 | N\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}|{\sf G}|, and let 𝒫 \mathcal{P} denote the set of poles of some projective point set in general position with symmetry group 𝖦 {\sf G}.

#### 9.2.3 Finite case: [4, 4, 6] ⇒ A 4 [4,4,6]\Rightarrow A_{4}

Let P P be some projective point set with symmetry group 𝖦 {\sf G} of orbit type [4, 4, 6] [4,4,6] and size 12 12 and let O O denote an orbit of size 4 4 in the action of 𝖦 {\sf G} on the pole hemisets of P P. By Proposition 5.1, every g ∈ 𝖦 g\in{\sf G} fixes exactly two poles of P P. The group 𝖦 {\sf G} therefore acts faithfully 18 18 18 The action of a group G G on a set X X is *faithful*if for every g ∈ G ∖ { 𝗂𝖽 } g\in G\setminus\{{\sf id}\}, there is some x ∈ X x\in X such that g ⁡ ( x) ≠ x g(x)\neq x. Given two distinct elements f, g ∈ G f,g\in G, we have f ⁡ ( x) ≠ g ⁡ ( x) ⇔ ( g − 1 ∘ f) ​ ( x) ≠ x f(x)\neq g(x)\Leftrightarrow(g^{-1}\circ f)(x)\neq x. It follows that G G acts faithfully on X X if and only if every element of G G determines a distinct permutation of X X, that is, G G is isomorphic to a subgroup of 𝖲𝗒𝗆 ⁡ ( X) {\sf Sym}(X). on O O, and must be a subgroup of 𝖲𝗒𝗆 ⁡ ( O) ≃ S 4 {\sf Sym}(O)\simeq S_{4}. There is only one subgroup of size 12 12 in S 4 S_{4}: A 4 A_{4}.

#### 9.2.4 Preparation: action on pairs of antipodal orbits

We will classify the remaining two cases by examining the action of 𝖦 {\sf G} not on pole hemisets, but on pairs of pole hemisets. We prepare this by laying out a few basic facts.

Let H H be a nontrivial subgroup H ≤ 𝖦 H\leq{\sf G}, and let B ∈ 𝒫 B\in\mathcal{P}. First, B ′ ↦ − B ′ B^{\prime}\mapsto-B^{\prime} defines a bijection between H ⁡ ( B) H(B) and H ⁡ ( − B) H(-B).

###### Claim 9.5.

For any B ∈ 𝒫 B\in\mathcal{P}, | H ⁡ ( B) | = | H ⁡ ( − B) | |H(B)|=|H(-B)|.

Let us say that g g*reverses*B B if g ⁡ ( B) = − B g(B)=-B. If g g reverses B B, then g ∉ 𝖦 B g\notin{\sf G}_{B} and g 2 ∈ 𝖦 B g^{2}\in{\sf G}_{B}. By Proposition 9.2, g 2 g^{2} is in two distinct maximal cyclic subgroups of 𝖦 {\sf G}, and is therefore the identity by Corollary 9.3.

###### Claim 9.6.

Any symmetry that reverses some pole is of order 2 2.

Any two orbits are either equal or disjoint, in particular, either H ⁡ ( − B) = H ⁡ ( B) H(-B)=H(B) or H ⁡ ( − B) ∩ H ⁡ ( B) = ∅ H(-B)\cap H(B)=\emptyset.

###### Claim 9.7.

If − B ∈ H ⁡ ( B) -B\in H(B) then − B ′ ∈ H ⁡ ( B) -B^{\prime}\in H(B) for all B ′ ∈ H ⁡ ( B) B^{\prime}\in H(B) and | H ⁡ ( B) | |H(B)| is even.

We can in fact consider the action ⊲ \triangleleft of H H on the set 𝒫 ± = def { { − B, B } ∣ B ∈ 𝒫 } \mathcal{P}^{\pm}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{\{-B,B\}\mid B\in\mathcal{P}\} of pairs of antipodal hemisets. When − B ∈ H ⁡ ( B) -B\in H(B), the orbit of { − B, B } \{-B,B\} under ⊲ \triangleleft has | H ⁡ ( B) | / 2 |H(B)|/2 elements. The orbit-stabilizer theorem therefore implies:

###### Claim 9.8.

If − B ∈ H ⁡ ( B) -B\in H(B) then there are exactly 2 ​ | H | / | H ⁡ ( B) | 2|H|/|H(B)| symmetries g ∈ H g\in H that fix or reverse B B.

#### 9.2.5 Finite case: [6, 8, 12] ⇒ S 4 [6,8,12]\Rightarrow S_{4}

Consider the next case, when 𝖦 {\sf G} has orbit type [6, 8, 12] [6,8,12] and size 24 24. Let P P be some projective point set with symmetry group 𝖦 {\sf G} and let O O denote the orbit of size 8 8 in the action of 𝖦 {\sf G} on the pole hemisets of P P. There is a single orbit of size 8 8, so by Claim 9.5, O O writes O = { B 1, − B 1, B 2, − B 2, …, − B 4 } O=\{B_{1},-B_{1},B_{2},-B_{2},\ldots,-B_{4}\}. We let O ± = def { { B i, − B i } ∣ 1 ≤ i ≤ 4 } O^{\pm}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{\{B_{i},-B_{i}\}\mid 1\leq i\leq 4\} and argue that 𝖦 {\sf G} acts faithfully on O ± O^{\pm}.

Assume that 𝖦 {\sf G} acts unfaithfully on O ± O^{\pm}, i.e., that some g 0 ∈ 𝖦 g_{0}\in{\sf G} fixes or reverses every B i B_{i}. Let us make the following observations:

1. (a)

g 0 g_{0} must reverse all B i B_{i}. Indeed, Proposition 5.1 ensures that g 0 g_{0} cannot fix all B i B_{i} (it can fix at most one), so it must reverse some and is therefore of order 2 2. Then, we cannot have g 0 ∈ 𝖦 B i ≃ ℤ 3 g_{0}\in{\sf G}_{B_{i}}\simeq\mathbb{Z}_{3} for order reason.

2. (b)

Each B i B_{i} is reversed by three symmetries. Indeed, 𝖦 B i ≃ ℤ 3 {\sf G}_{B_{i}}\simeq\mathbb{Z}_{3} and each B i B_{i} is fixed or reversed by six symmetries by Claim 9.8.

3. (c)

𝖦 {\sf G} has 9 9 elements of order 2 2, 3 3 of which are in maximal cyclic subgroups of order 4 4, as revealed by Table 1.

We claim that there exists a symmetry in 𝖦 ∖ { g 0 } {\sf G}\setminus\{g_{0}\} and i ≠ j i\neq j such that g g reverses B i B_{i} and B j B_{j}. This follows from the pigeonhole principle if no B i B_{i} is reversed by an element of a maximal cyclic subgroup of order 4 4 (if an element reverses B i B_{i}, it is of order 2 2 by Claim 9.6; there are 6 6 such elements not in a maximal cyclic subgroup of order 4 4; if each of them reverses at most one B i B_{i}, then, together with g 0 g_{0}, we get at most 6 + 4 = 10 6+4=10 reversals; but by (b) above, we need 4 × 3 = 12 4\times 3=12 such reversals). If say B 1 B_{1} is reversed by g 2 g^{2} with g ∈ 𝖦 g\in{\sf G}, then g g (of order 4 4) neither fixes (which would require order 3 3) nor reverses B 1 B_{1} (which would require order 2 2), so w.l.o.g. we have g ⁡ ( B 1) = B 2 g(B_{1})=B_{2}. Then, − B 1 = g 2 ​ ( B 1) = g ⁡ ( B 2) -B_{1}=g^{2}(B_{1})=g(B_{2}), and thus g 2 ​ ( B 2) = − g ⁡ ( B 1) = − B 2 g^{2}(B_{2})=-g(B_{1})=-B_{2}; the symmetry g 2 g^{2} thus reverses B 1 B_{1} and also B 2 B_{2}.

We can now obtain our contradiction: the symmetry g 0 ∘ g g_{0}\circ g fixes both B 1 B_{1} and B 2 B_{2}, but is not the identity as g 0 2 = 𝗂𝖽 g_{0}^{2}={\sf id} and g ≠ g 0 g\neq g_{0}. Thus, g 0 g_{0} cannot exist and 𝖦 {\sf G} acts faithfully on O ± O^{\pm}. It follows that 𝖦 ≤ S 4 {\sf G}\leq S_{4} and, since | 𝖦 | = | S 4 | |{\sf G}|=|S_{4}|, 𝖦 ≃ S 4 {\sf G}\simeq S_{4}.

#### 9.2.6 Finite case: [12, 20, 30] ⇒ A 5 [12,20,30]\Rightarrow A_{5}

Consider the next case, when 𝖦 {\sf G} has orbit type [12, 20, 30] [12,20,30] and size 60 60. Let P P be some projective point set with symmetry group 𝖦 {\sf G} and let O O denote the orbit of size 30 30 in the action of 𝖦 {\sf G} on the pole hemisets of P P. There is a single orbit of size 30 30, so by Claim 9.5, we have O = { B 1, − B 1, B 2, − B 2, …, − B 15 } O=\{B_{1},-B_{1},B_{2},-B_{2},\ldots,-B_{15}\}. Also, each B ∈ O B\in O has a stabilizer of size 2 2. Let g i g_{i} denote the common generator of the stabilizers of B i B_{i} and − B i -B_{i}. Proposition 5.1 ensures that g i ≠ g j g_{i}\neq g_{j} whenever i ≠ j i\neq j, and by Table 1, 𝖦 {\sf G} has 15 15 elements of order 2 2. They are thus all accounted for.

We will use the subgroups D 2 ≤ 𝖦 D_{2}\leq{\sf G}, so let us first clarify how they act on P P.

###### Lemma 9.9.

Let P P be a projective point set with symmetry group 𝖦 {\sf G}. Let H ≤ 𝖦 H\leq{\sf G} with H ≃ D 2 H\simeq D_{2}. Let 𝒫 H \mathcal{P}_{H} be the set of poles of the elements of H H. The action of H H on 𝒫 H \mathcal{P}_{H} has three orbits, each consisting of two antipodal hemisets.

*Proof.*We have | H | = 4 |H|=4, with all elements, except for 𝗂𝖽 {\sf id}, of order 2 2. There are six poles (three antipodal pairs), grouped in three orbits of size two. Suppose, for some B ∈ 𝒫 H B\in\mathcal{P}_{H}, H ⁡ ( B) = { B, B 1 } H(B)=\{B,B_{1}\} with B 1 ≠ − B B_{1}\neq-B. Let 𝗂𝖽 ≠ g 0 ∈ H {\sf id}\neq g_{0}\in H and 𝗂𝖽 ≠ g 1 ∈ H {\sf id}\neq g_{1}\in H be such that g 0 ​ ( B) = B g_{0}(B)=B and g 1 ​ ( B 1) = B 1 g_{1}(B_{1})=B_{1}; both g 0 g_{0} and g 1 g_{1} are of order 2 and g 0 ≠ g 1 g_{0}\neq g_{1}. We must have g 1 ​ ( B) = B 1 g_{1}(B)=B_{1}, since g 1 ​ ( B) ∈ H ​ ( B) g_{1}(B)\in H(B) and the stabilizer H B H_{B} is of order 2 and has no elements other than g 0 g_{0} and 𝗂𝖽 {\sf id}. On the one hand, this shows g 1 ​ ( g 1 ​ ( B)) = g 1 ​ ( B 1) = B 1 g_{1}(g_{1}(B))=g_{1}(B_{1})=B_{1}. On the other hand, g 1 2 = 𝗂𝖽 g_{1}^{2}={\sf id} and therefore g 1 ​ ( g 1 ​ ( B)) = B g_{1}(g_{1}(B))=B; contradiction. Therefore, H ⁡ ( B) H(B) has to be { B, − B } \{B,-B\} as announced.

Now, let H i H_{i} denote the subgroup of 𝖦 {\sf G} that fixes or reverses B i B_{i}. We have | H i | = 4 |H_{i}|=4 by Claim 9.8. Since H B i = { 𝗂𝖽, g i } H_{B_{i}}=\{{\sf id},g_{i}\}, every element in H i ∖ { 𝗂𝖽, g i } H_{i}\setminus\{{\sf id},g_{i}\} reverses B i B_{i}, and must be of order 2 2 by Claim 9.6. Thus, H i ≃ D 2 H_{i}\simeq D_{2}.

###### Claim 9.10.

If g j ​ ( B i) = − B i g_{j}(B_{i})=-B_{i}, then g i ​ ( B j) = − B j g_{i}(B_{j})=-B_{j}.

*Proof.*Assume that g j ​ ( B i) = − B i g_{j}(B_{i})=-B_{i}, so that g j ∈ H i g_{j}\in H_{i}. By Lemma 9.9, the action of H i H_{i} on the poles of its elements has { B j, − B j } \{B_{j},-B_{j}\} as an orbit. Thus, g i ​ ( B j) g_{i}(B_{j}) must be B j B_{j} or − B j -B_{j}, and it cannot be the former since the only poles of g i g_{i} are ± B i \pm B_{i}.

It follows that if g j ∈ H i g_{j}\in H_{i}, then g i ∈ H j g_{i}\in H_{j}. In other words, if H i = { 𝗂𝖽, g i, g j, g k } H_{i}=\{{\sf id},g_{i},g_{j},g_{k}\}, then H j = H i = H k H_{j}=H_{i}=H_{k} and each of the 15 15 elements of 𝖦 {\sf G} of order 2 2 belongs to exactly one subgroup H i H_{i}. The set X = def { H i ∣ 1 ≤ i ≤ 15 } X\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{H_{i}\mid 1\leq i\leq 15\} is therefore of size 5 5.

Now, for any f, g ∈ 𝖦 f,g\in{\sf G} we write f ⊲ g = def f ∘ g ∘ f − 1 f\triangleleft g\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}f\circ g\circ f^{-1}. Observe that for every H ∈ X H\in X and f ∈ 𝖦 f\in{\sf G}, the set f ⊲ H = def { f ⊲ g ∣ g ∈ H } f\triangleleft H\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{f\triangleleft g\mid g\in H\} is also an element of X X. Indeed, f ⊲ g f\triangleleft g has same order as g g, and ( f ⊲ g) ∘ ( f ⊲ g ′) = f ⊲ ( g ∘ g ′) (f\triangleleft g)\circ(f\triangleleft g^{\prime})=f\triangleleft(g\circ g^{\prime}). So 𝖦 {\sf G} acts on X X by ⊲ \triangleleft.

###### Claim 9.11.

f ⊲ g i = g j f\triangleleft g_{i}=g_{j} if and only if f ⁡ ( B i) ∈ { B j, − B j } f(B_{i})\in\{B_{j},-B_{j}\}.

*Proof.*On the one hand, if f ⊲ g i = g j f\triangleleft g_{i}=g_{j} then f ∘ g i = g j ∘ f f\circ g_{i}=g_{j}\circ f, so that f ⁡ ( B i) = g j ​ ( f ⁡ ( B i)) f(B_{i})=g_{j}\left(f(B_{i})\right), forcing f ⁡ ( B i) ∈ { − B j, B j } f(B_{i})\in\{-B_{j},B_{j}\} since g j g_{j} fixes only two poles (Proposition 5.1). On the other hand, if f ⁡ ( B i) = ϵ ​ B j f(B_{i})=\epsilon B_{j} with ϵ ∈ { +, − } \epsilon\in\{+,-\}, then f ⊲ g i ​ ( ϵ ​ B j) = f ∘ g i ∘ f − 1 ​ ( ϵ ​ B j) = f ∘ g i ​ ( B i) = f ⁡ ( B i) = ϵ ​ B j f\triangleleft g_{i}(\epsilon B_{j})=f\circ g_{i}\circ f^{-1}(\epsilon B_{j})=f\circ g_{i}(B_{i})=f(B_{i})=\epsilon B_{j}, revealing that f ⊲ g i f\triangleleft g_{i} is the symmetry of order 2 2 that fixes ϵ ​ B j \epsilon B_{j}, that is g j g_{j}.

For any i, j i,j there exists f ∈ 𝖦 f\in{\sf G} such that f ⁡ ( B i) = B j f(B_{i})=B_{j}, so f ⊲ H i = H j f\triangleleft H_{i}=H_{j}. Claim 9.11 therefore implies that the action ⊲ \triangleleft of 𝖦 {\sf G} on X X is transitive.

Let us argue that 𝖦 {\sf G} acts faithfully on X X. Let H ∈ X H\in X and let us write H = { 𝗂𝖽, g i, g j, g k } H=\{{\sf id},g_{i},g_{j},g_{k}\} and introduce O H = def { B i, − B i, B j, − B j, B k, − B k } O_{H}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{B_{i},-B_{i},B_{j},-B_{j},B_{k},-B_{k}\}. Claim 9.11 implies:

###### Claim 9.12.

f ⊲ H = H f\triangleleft H=H if and only if f ⁡ ( O H) = O H f(O_{H})=O_{H}.

Thus, the action of ⟨ f ⟩ \langle f\rangle partitions O H O_{H} into classes of size 1 1, 2 2, 3 3 or 6 6. These sizes must divide the order of f f, which is 2 2, 3 3 or 5 5 by Table 1.

###### Claim 9.13.

If f f has order 5 5 then f ⊲ H ≠ H f\triangleleft H\neq H. If f f has order 2 2 then f ⊲ H = H f\triangleleft H=H if and only if f ∈ H f\in H.

*Proof.*If f f has order 5 5 and f ⊲ H = H f\triangleleft H=H, then ⟨ f ⟩ \langle f\rangle must partition O H O_{H} in orbits of size 1 1, forcing f ∈ H f\in H to be of order at most 2 2, a contradiction. If f f has order 2 2 and f ⊲ H = H f\triangleleft H=H, then the action of ⟨ f ⟩ \langle f\rangle partitions O H O_{H} in singletons and pairs. There must exist a ∈ { i, j, k } a\in\{i,j,k\} such that f ⁡ ( B a) ∈ { B a, − B a } f(B_{a})\in\{B_{a},-B_{a}\}, implying that f ∈ H a = H f\in H_{a}=H. The reverse direction is immediate.

We already have that for every element f ∈ 𝖦 f\in{\sf G} of order 2 2 or 5 5, there exists H ∈ X H\in X such that f ⊲ H ≠ H f\triangleleft H\neq H. It remains to handle elements of order 3 3. Let S H S_{H} denote the stabilizer of H H for ⊲ \triangleleft. Since ⊲ \triangleleft is transitive, | S H | = 60 / 5 = 12 |S_{H}|=60/5=12 and Claim 9.13 implies that S H S_{H} has 12 − 4 = 8 12-4=8 elements of order 3 3. Let α \alpha be the number of pairs ( H, f) (H,f) where H ∈ X H\in X, f ∈ S H f\in S_{H}, and f f is of order 3 3; we thus have α = 5 × 8 = 40 \alpha=5\times 8=40.

Now, let O X = def { O H ∣ H ∈ X } O_{X}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{O_{H}\mid H\in X\}. Like 𝖦 {\sf G} acts on X X, 𝖦 {\sf G} must act on O X O_{X}. For every f f of order 3 3, the action of ⟨ f ⟩ \langle f\rangle on O X O_{X} creates orbits of size 1 1 or 3 3. Thus, each f f of order 3 3 fixes globally either two or five elements of O X O_{X}. There are 20 20 elements of order 3 3 in 𝖦 {\sf G} by Table 1, so α = 40 \alpha=40 implies that each element of order 3 3 fixes *exactly*2 2 elements of O X O_{X}. It follows that for every element f ∈ 𝖦 f\in{\sf G} of order 3 3 there also exists H ∈ X H\in X such that f ⊲ H ≠ H f\triangleleft H\neq H.

Altogether, 𝖦 {\sf G} acts faithfully on X X, and is therefore a subgroup of S 5 S_{5}. It follows that 𝖦 ≃ A 5 {\sf G}\simeq A_{5}, the only subgroup of S 5 S_{5} of size 60 60.

### 9.3 More on orbits

To analyze the symmetry group of a given projective point set (as in Section 9.6 below), it is convenient to have a better grasp on the possible orbits of poles. The next lemma clarifies the conditions under which a pole B B may have an orientation reversing symmetry, that is, − B ∈ 𝖦 ⁡ ( B) -B\in{\sf G}(B) or, equivalently, 𝖦 ⁡ ( B) = 𝖦 ⁡ ( − B) {\sf G}(B)={\sf G}(-B).

###### Lemma 9.14.

Let P P be a projective set in general position with nontrivial symmetry group 𝖦 {\sf G}, and B B a pole of P P. We have 𝖦 ⁡ ( B) ≠ 𝖦 ⁡ ( − B) {\sf G}(B)\neq{\sf G}(-B) if and only if

1. (i)

𝖦 {\sf G} has orbit type [1, 1] [1,1], or

2. (ii)

𝖦 {\sf G} has orbit type [2, N / 2, N / 2] [2,N/2,N/2], N / 2 N/2 is odd, and | 𝖦 ⁡ ( B) | = N / 2 |{\sf G}(B)|=N/2, or

3. (iii)

𝖦 {\sf G} has orbit type [4, 4, 6] [4,4,6] and | 𝖦 ⁡ ( B) | = 4 |{\sf G}(B)|=4.

*Proof.*Let us go through the possible orbit types of 𝖦 {\sf G}. An important point is that, by Corollary 9.4, 𝖦 {\sf G} has at most one orbit type. Hence, the orbit type of 𝖦 {\sf G} describes the orbits of the poles of P P under the action of 𝖦 {\sf G}. Also, | 𝖦 ⁡ ( B) | = | 𝖦 ⁡ ( − B) | |{\sf G}(B)|=|{\sf G}(-B)| by Claim 9.5, so 𝖦 ⁡ ( B) = 𝖦 ⁡ ( − B) {\sf G}(B)={\sf G}(-B) holds for any pole B B in an orbit that have a unique size. This takes care of all poles for orbit types [6, 8, 12] [6,8,12] and [12, 20, 30] [12,20,30], and of the poles in the orbit of size 2 2 for [2, N / 2, N / 2] [2,N/2,N/2] with N / 2 > 2 N/2>2, and for the the poles in the orbit of size 6 6 for [4, 4, 6] [4,4,6]. We are left only with the following cases to be clarified.

If 𝖦 {\sf G} has orbit type [1, 1] [1,1], then the action of 𝖦 {\sf G} on the poles of P P has two orbits, both of size 1 1. It follows that 𝖦 ⁡ ( B) ≠ 𝖦 ⁡ ( − B) {\sf G}(B)\neq{\sf G}(-B) for every pole B B of P P.

If 𝖦 {\sf G} has orbit type [2, 2, 2] [2,2,2] (that is, [2, N / 2, N / 2] [2,N/2,N/2] with N = 4 N=4), then | 𝖦 | = 4 |{\sf G}|=4 with all elements other than 𝗂𝖽 {\sf id} of order 2 2. Hence, 𝖦 ≃ D 2 {\sf G}\simeq D_{2} and Lemma 9.9 implies that every orbit is of the form { B, − B } \{B,-B\}. It follows that 𝖦 ⁡ ( B) = 𝖦 ⁡ ( − B) {\sf G}(B)={\sf G}(-B) for any pole of P P.

Assume that 𝖦 {\sf G} has orbit type [2, N / 2, N / 2] [2,N/2,N/2] with N / 2 > 2 N/2>2 and | 𝖦 ⁡ ( B) | = N / 2 |{\sf G}(B)|=N/2. If N / 2 N/2 is odd, then 𝖦 ⁡ ( B) ≠ 𝖦 ⁡ ( − B) {\sf G}(B)\neq{\sf G}(-B) by Claim 9.7. So assume N / 2 N/2 is even and let g 1 g_{1} be the unique element of order 2 2 in the cyclic subgroup of 𝖦 {\sf G} of order N / 2 N/2 (cf. Corollary 9.4). We claim that g 1 ​ ( B) = − B g_{1}(B)=-B. In order to verify this, note that 𝖦 B ≃ ℤ 2 {\sf G}_{B}\simeq\mathbb{Z}_{2} since | 𝖦 B | = | 𝖦 | / | 𝖦 ⁡ ( B) | = N / ( N / 2) = 2 |{\sf G}_{B}|=|{\sf G}|/|{\sf G}(B)|=N/(N/2)=2, so let us write 𝖦 B = { 𝗂𝖽, g 0 } {\sf G}_{B}=\{{\sf id},g_{0}\}. Hence, g 0 g_{0} is of order 2 2, and g 0 ≠ g 1 g_{0}\neq g_{1} because they belong to different maximal cyclic subgroups of 𝖦 {\sf G} (by Proposition 9.2). Now g 2 = def g 0 ∘ g 1 g_{2}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}g_{0}\circ g_{1} has to be some element not in the maximal cyclic subgroup of order N / 2 N/2 of 𝖦 {\sf G}, hence g 2 g_{2} is of order 2 as well. From

 | g 1 ∘ g 0 = g 2 − 1 = g 2, g 0 ∘ g 2 = g 1, g 2 ∘ g 0 = g 1 − 1 = g 1, g 2 ∘ g 1 = g 0, g 1 ∘ g 2 = g 0 − 1 = g 0, g_{1}\circ g_{0}={g_{2}}^{-1}=g_{2},\quad g_{0}\circ g_{2}=g_{1},\quad g_{2}\circ g_{0}={g_{1}}^{-1}=g_{1},\quad g_{2}\circ g_{1}=g_{0},\quad g_{1}\circ g_{2}={g_{0}}^{-1}=g_{0}, |  |

we get that H = def { 𝗂𝖽, g 0, g 1, g 2 } H\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{{\sf id},g_{0},g_{1},g_{2}\} is a subgroup of 𝖦 {\sf G} of order 4 4, each of which element has order 2 2. It follows that H ≃ D 2 H\simeq D_{2} and Lemma 9.9 ensures that H ⁡ ( B) = { B, − B } H(B)=\{B,-B\} and g 1 ​ ( B) = − B g_{1}(B)=-B. In this case (orbit type [2, N / 2, N / 2] [2,N/2,N/2] with N / 2 > 2 N/2>2 even and | 𝖦 ⁡ ( B) | = N / 2 |{\sf G}(B)|=N/2), we therefore have 𝖦 ⁡ ( B) = 𝖦 ⁡ ( − B) {\sf G}(B)={\sf G}(-B).

The last case is when 𝖦 {\sf G} has orbit type [4, 4, 6] [4,4,6] and | 𝖦 ⁡ ( B) | = 4 |{\sf G}(B)|=4. In preparation of the argument, let us first have a look at a pole A A with | 𝖦 ⁡ ( A) | = 6 |{\sf G}(A)|=6. Let H H be the subgroup of 𝖦 {\sf G} consisting of symmetries that map A A to A A or − A -A. We have | H | = 4 |H|=4 by Claim 9.8. Any symmetry that maps A A to − A -A has order 2 2 by Claim 9.6. Since | 𝖦 A | = 12 / 6 = 2 |{\sf G}_{A}|=12/6=2, there is exactly one nontrivial symmetry that fixes A A, and it also has order 2 2. There are exactly 3 3 elements of order 2 2 in 𝖦 {\sf G} (cf. Table 1), so together with 𝗂𝖽 {\sf id} they form the group H H.

We return to orbit 𝖦 ⁡ ( B) {\sf G}(B) of size 4 4 with the goal of showing that − B ∉ 𝖦 ⁡ ( B) -B\not\in{\sf G}(B). If − B ∈ 𝖦 ⁡ ( B) -B\in{\sf G}(B), then by Claim 9.8 there is a group H ′ H^{\prime} of 6 6 symmetries in 𝖦 {\sf G} that fix or reverse B B. The three symmetries in H ′ H^{\prime} reversing B B are of order 2 2 by Claim 9.6; again, they are exactly the elements of order 2 2 of 𝖦 {\sf G}. It follows that H ≤ H ′ H\leq H^{\prime}, a contradiction, since H H is of order 4 4, H ′ H^{\prime} is of order 6 6, and 4 4 does not divide 6 6.

### 9.4 Adding reflections

It is natural to ask what happens if we include orientation reversing permutations (see Section 5.1) in symmetries. Given a projective set P P, let 𝖦 {\sf G} be the set of orientation preserving symmetries, and let 𝖦 𝗋 {\sf G^{r}} be the set of orientation preserving or reversing symmetries. Clearly, 𝖦 ≤ 𝖦 𝗋 {\sf G}\leq{\sf G^{r}} and 𝖦 ≠ 𝖦 𝗋 {\sf G}\neq{\sf G^{r}}, since the permutation g 𝗂𝗇𝗏: p ↦ − p g^{\sf inv}\,:p\mapsto-p is an orientation reversing permutation (hence not in 𝖦 {\sf G}, provided | P | ≥ 6 |P|\geq 6). Moreover, if g g and g ′ g^{\prime} are orientation reversing permutations, then g ∘ g ′ g\circ g^{\prime} is an orientation preserving permutation. Any symmetry preserves antipodality by Lemma 3.3 (i), so g 𝗂𝗇𝗏 g^{\sf inv} commutes with every g ∈ 𝖦 g\in{\sf G} and we have 𝖦 𝗋 = { 𝗂𝖽, g 𝗂𝗇𝗏 } × 𝖦 ≃ ℤ 2 × 𝖦 {\sf G^{r}}=\{{\sf id},g^{\sf inv}\}\times{\sf G}\simeq\mathbb{Z}_{2}\times{\sf G}.

For example, if | 𝖦 𝗋 | = 24 |{\sf G^{r}}|=24, then this group is isomorphic to A 4 × ℤ 2 A_{4}\times\mathbb{Z}_{2}, ℤ 12 × ℤ 2 \mathbb{Z}_{12}\times\mathbb{Z}_{2}, or D 6 × ℤ 2 D_{6}\times\mathbb{Z}_{2} (not S 4 S_{4} which is not isomorphic to any of the three groups mentioned).

### 9.5 Symmetries on the Sphere

We have characterized the symmetries of affine and projective sets in general position on the sphere 𝕊 2 \mathbb{S}^{2}. What about general finite subsets Q Q in general position of 𝕊 2 \mathbb{S}^{2}? This can be easily derived as follows. Given such a set Q Q, let P = def Q ∪ − Q P\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}Q\cup-Q be the completion of Q Q to a projective set, which is – as a projective set – in general position, with 𝖦 {\sf G} the group of symmetries of P P.

Similar to the situation for affine sets, we can let 𝖦 {\sf G} act on the *semisets*of P P, i.e., the subsets of P P which contain exactly one point from every antipodal pair in P P (the fact that this is indeed an action follows from g ⁡ ( − p) = − g ⁡ ( p) g(-p)=-g(p), see Lemma 3.3 (i)). Consider the stabilizer 𝖦 Q {\sf G}_{Q} of Q Q. Similar to Lemma 3.5, we can derive that 𝖦 Q {\sf G}_{Q} is isomorphic to the group of orientation preserving symmetries of Q Q, and thus this group is a subgroup of 𝖦 {\sf G}. This shows that 𝖦 Q {\sf G}_{Q} is among the groups we identified for the projective sets, as they are closed under taking subgroups (being the finite subgroups of S ​ O ​ ( 3) SO(3)).

### 9.6 Gallery

#### 9.6.1 Small Sets

Table 2 gives a summary of all projective order types with 2 ​ n 2n points, 3 ≤ n ≤ 6 3\leq n\leq 6, their symmetry groups and their induced affine order types. We see that for each n ≤ 5 n\leq 5 there is exactly one projective order type. For n = 6 n=6, we have four projective order types, the completions of convex position and the three order types with 5 extreme points. These partition the twenty 6-point affine order types (note that this is 20, since we consider symmetries without reflection; with reflection it is 16).

icon | | π | 2 \frac{|\pi|}{2} | 𝖮𝖳 aff π {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi} | | 𝖮𝖳 aff π | |{\sf O\hskip-0.92505ptT}^{{}_{\mathrm{aff}}}_{\!\pi}| | 𝖦 {\sf G} | | 𝖦 | |{\sf G}| | 2 ​ ( n 2) + 2 2\binom{n}{2}+2 |

 | 3 3 | 8 3 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{3}_{8} | 1 1 | S 4 S_{4} | 24 24 | 8 8 |

 | 4 4 | 6 4 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{4}_{6}, 8 3 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{3}_{8} | 2 2 | S 4 S_{4} | 24 24 | 14 = 6 + 8 14=6+8 |

 | 5 5 | 2 5 {\includegraphics[page,width]{./figures-revision.pdf}}^{5}_{2}, 10 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{10}, 10 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{10} | 3 3 | D 5 D_{5} | 10 10 | 22 = 2 + 2 × 10 22=2+2\times 10 |

 | 6 6 | 2 6 {\includegraphics[page,width]{./figures-revision.pdf}}^{6}_{2}, 12 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{12}, 12 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{12}, 6 2 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{2}_{6} | 4 4 | D 6 D_{6} | 12 12 | 32 = 2 + 2 × 12 + 6 32=2+2\times 12+6 |

 | 6 6 | 12 5 {\includegraphics[page,width]{./figures-revision.pdf}}^{5}_{12}, 20 3 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{3}_{20} | 2 2 | A 5 A_{5} | 60 60 | 32 = 12 + 20 32=12+20 |

 | 6 6 | 6 1 {\includegraphics[page,width]{./figures-revision.pdf}}^{1}_{6}, 2 3 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{3}_{2}, 6 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{6}, 6 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{6}, … | 6 6 | D 3 D_{3} | 6 6 | 32 = 2 + 5 × 6 32=2+5\times 6 |

 | 6 6 | 4 1 {\includegraphics[page,width]{./figures-revision.pdf}}^{1}_{4}, 4 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{4}, 4 1 {\includegraphics[page,width]{./figures-revision.pdf}\,}^{1}_{4}, … | 8 8 | ℤ 4 \mathbb{Z}_{4} | 4 4 | 32 = 8 × 4 32=8\times 4 |

Table 2: The affine order types and symmetries of projective order types π \pi with 2 ​ n 2n points, n = 3, 4, 5, 6 n=3,4,5,6. For an affine order type ω \omega, we write ω μ γ \omega^{\gamma}_{\mu}, with γ \gamma the size of its symmetry group, and μ \mu the size of its orbit among the affine hemisets. The last column indicates, how the 2 ​ ( n 2) + 2 2\binom{n}{2}+2 affine hemisets distribute among the affine order types induced by the projective set.

Let us recall that poles are hemisets, not necessarily affine hemisets. This explains, e.g., that the projective set with 𝖦 = S 4 {\sf G}_{\includegraphics[page,width]{./figures-revision.pdf}}=S_{4} exhibits in the table only 8 affine poles, all in the same orbit; the missing poles are hemisets with one or two antipodal pairs, with symmetry of size 4 or 2, resp., and thus orbits of size 6 and 12, resp., see Figure 6 (left). Similarly, the projective set with 𝖦 = S 4 {\sf G}_{\includegraphics[page,width]{./figures-revision.pdf}}=S_{4} has 12 12 non-affine poles that form a single orbit under 𝖦 {\sf G}_{\includegraphics[page,width]{./figures-revision.pdf}}, see Figure 6 (center).

The projective set is the only one up to n = 6 n=6 which has no affine hemiset with nontrivial symmetry (see Figure 7), but there is still a non-affine hemiset (see Figure 6 (right)) with symmetry group ℤ 4 \mathbb{Z}_{4}.

6 4 {\includegraphics[page,width]{./figures-revision.pdf}\!}^{4}_{6} 12 2 {\includegraphics[page,width]{./figures-revision.pdf}\,\,}^{2}_{12} 12 2 {\includegraphics[page,width]{./figures-revision.pdf}\,\,}^{2}_{12} 1 4 {\includegraphics[page,width]{./figures-revision.pdf}\,\,}^{4}_{1}

Figure 6: Non-affine poles of projective sets. Rays indicate the connections to the antipodal pairs on the boundary of the defining closed hemispheres (points in infinity).

Figure 7: A “hemisphere” of affine hemisets of the projective set . Each order type in 𝖮𝖳 aff {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\mbox{\includegraphics[page,width]{./figures-revision.pdf}}} occurs with multiplicity four as affine hemiset. We see five order types, with three order types missing, the reflections of the three inner order types. Pairs of affine hemisets whose dual cells share an edge, or equivalently, which can be obtained by projectively swapping a point to the other side are connected by an edge, hinged at the points swapped.

#### 9.6.2 Small groups, cyclic groups

We see that all symmetry groups have size at least 4 in Table 2, in particular, we have not yet encountered a projective set with trivial symmetry group. So let us describe examples with smaller symmetry groups. For that we need the following lemma:

###### Lemma 9.15.

For any two affine hemisets A A and A ′ ∉ { A, − A } A^{\prime}\not\in\{A,-A\} of a projective set P P in general position with | P | = 2 ​ n |P|=2n, we have h ⁡ ( A) + h ⁡ ( A ′) ≤ n + 4 h(A)+h(A^{\prime})\leq n+4.

*Proof.*We recall here the duality from Section 2.2 and denote by p ∗ p^{*} the great circle dual to point p p on 𝕊 2 \mathbb{S}^{2}. Recall that p ∗ = ( − p) ∗ p^{*}=(-p)^{*}, i.e., P ∗ = def { p ∗ ∣ p ∈ P } P^{*}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{p^{*}\mid p\in P\} is an arrangement of n n great circles in general position. Every affine hemiset A A of P P corresponds to a cell in this arrangement (see Lemma 4.2), which we denote by A ∗ A^{*}. We have that cell A ∗ A^{*} is incident to h ⁡ ( A) h(A) of the great circles in P ∗ P^{*}.

For affine hemisets A A and A ′ A^{\prime} the cells A ∗ A^{*} and A ′ ⁣ ∗ A^{\prime*} share at most four out of the n n great circles in P ∗ P^{*} to which they are both incident, unless A ′ ∈ { A, − A } A^{\prime}\in\{A,-A\}. This is easy to prove directly and follows from a basic fact on line arrangements which is called Gunderson’s Theorem in [19, Theorem VII]. Going back to the primal, this yields h ⁡ ( A) + h ⁡ ( A ′) ≤ n + 4 h(A)+h(A^{\prime})\leq n+4.

It follows that if h ⁡ ( A) > n / 2 + 2 h(A)>n/2+2 then no other affine hemiset except for − A -A has the same number of extreme points as A A, and therefore 𝖦 ⁡ ( A) ⊆ { A, − A } {\sf G}(A)\subseteq\{A,-A\}. If, in addition, A A has symmetry group 𝖥 {\sf F} and no orientation reversing symmetry, then 𝖦 ⁡ ( A) = { A } {\sf G}(A)=\{A\} and | 𝖦 | = | 𝖦 ⁡ ( A) | ⋅ | 𝖦 A | = | 𝖦 ⁡ ( A) | ⋅ | 𝖥 | = | 𝖥 | |{\sf G}|=|{\sf G}(A)|\cdot|{\sf G}_{A}|=|{\sf G}(A)|\cdot|{\sf F}|=|{\sf F}|, that is, 𝖦 ≃ 𝖥 {\sf G}\simeq{\sf F}. We summarize:

###### Claim 9.16.

Let A A be an affine subset of 𝕊 2 \mathbb{S}^{2}, with h ⁡ ( A) > | A | / 2 + 2 h(A)>|A|/2+2 and symmetry 𝖥 {\sf F}. If A A has no orientation reversing symmetry, then the completion of A A is a projective set with symmetry group isomorphic to ℤ | 𝖥 | \mathbb{Z}_{|{\sf F}|}. If A A has an orientation reversing symmetry, then the completion of A A is a projective set with symmetry group isomorphic to D | 𝖥 | D_{|{\sf F}|}.

This provides us immediately with many examples of projective sets with symmetry groups of size 1 or 2. 19 19 19 We also see why this fails for n = 6 n=6: we have n / 2 + 2 = 5 n/2+2=5 and more than 5 extreme points force convex position. For example, suppose a 7-point set has six extreme points (note 6 > 7 / 2 + 2 6>7/2+2), and the inner point placed barely inside an edge of the convex hull, see Figure 8 (left). Then its symmetry group is trivial, but it exhibits an orientation reversing symmetry. Hence, the projective completion has symmetry D 1 ≃ ℤ 2 D_{1}\simeq\mathbb{Z}_{2}. If we have a 9-point set with seven extreme points (note 7 > 9 / 2 + 2 7>9/2+2), then the inner two points can be easily placed so that we have no orientation reversing symmetry, see Figure 8 (center). The projective completion of such a set has trivial symmetry.

Figure 8: Sets with projective completion with symmetry ℤ 2 \mathbb{Z}_{2} (left), ℤ 1 \mathbb{Z}_{1} (center), and ℤ 5 \mathbb{Z}_{5} (right).

Here is a claim that provides projective sets with symmetry ℤ k \mathbb{Z}_{k}, k k odd, see Figure 8 (right).

###### Claim 9.17.

Let P P be a projective set in general position, with an affine pole A A with symmetry 𝖥 ≃ ℤ k {\sf F}\simeq\mathbb{Z}_{k}, k > 1 k>1. If k k is odd and A A has at least three layers of odd size, then A A has no orientation reversing symmetry and, for the symmetry group 𝖦 {\sf G} of P P, 𝖦 ≃ ℤ k {\sf G}\simeq\mathbb{Z}_{k} or 𝖦 ≃ A 4 {\sf G}\simeq A_{4} (the latter can occur only for k = 3 k=3).

*Proof.*Every orientation reversing permutation of A A has to fix exactly one element in each odd layer, i.e., it has to fix at least three elements. Obvioulsy, a permutation fixing three elements cannot be orientation reversing. The fact that A A has no orientation reversing symmetry implies − A ∉ 𝖦 ⁡ ( A) -A\not\in{\sf G}(A). By Lemma 9.14, this cannot happen if 𝖦 {\sf G} has orbit type [6, 8, 12] [6,8,12] or [12, 20, 30] [12,20,30]. Also, if 𝖦 ≃ D k {\sf G}\simeq D_{k}, then − A ∈ 𝖦 ⁡ ( A) -A\in{\sf G}(A), so this must be ruled out. This leaves ℤ k \mathbb{Z}_{k} or A 4 A_{4}, and the latter only for k = 3 k=3.

#### 9.6.3 Tetrahedral group

Let Δ = { p 1, p 2, p 3, p 4 } \Delta=\{p_{1},p_{2},p_{3},p_{4}\} be the vertices of a regular tetrahedron inscribed in 𝕊 2 \mathbb{S}^{2}, and let G ¯ \overline{G} denote the set of rotations of 𝕊 2 \mathbb{S}^{2} that map Δ \Delta to itself; true to its name, G ¯ ≃ A 4 \overline{G}\simeq A_{4} is the tetrahedral group. For any point q ∈ 𝕊 2 q\in\mathbb{S}^{2} not fixed by any element of G ¯ \overline{G}, we have | G ¯ ​ ( q) | = | G ¯ | = 12 |\overline{G}(q)|=|\overline{G}|=12. We fix a generic point p 1 ′ p_{1}^{\prime} close to p 1 p_{1}, and close to the geodesic arc p 1 ​ p 2 p_{1}p_{2}, but not on this arc. Let g 1 g_{1} denote the element of order 3 3 in G ¯ \overline{G} that fixes p 1 p_{1} and note that the orbit of p 1 ′ p_{1}^{\prime} under ⟨ g 1 ⟩ \langle g_{1}\rangle consists of three points close to p 1 p_{1}. Let S 1 = def { p 1 } ∪ ⟨ g 1 ⟩ ​ ( p 1 ′) S_{1}\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\{p_{1}\}\cup\langle g_{1}\rangle(p_{1}^{\prime}).

Now, let P = def Δ ∪ − Δ ∪ G ¯ ​ ( p 1 ′) ∪ − G ¯ ​ ( p 1 ′) P\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}\Delta\cup-\Delta\cup\overline{G}(p_{1}^{\prime})\cup-\overline{G}(p_{1}^{\prime}) and let 𝖦 {\sf G} be the symmetry group of P P. Observe that P P is a projective set in general position with 32 32 points.

###### Claim 9.18.

If p 0 ′ p_{0}^{\prime} is chosen sufficiently close to both p 0 p_{0} and the arc p 0 ​ p 1 p_{0}p_{1}, then 𝖦 ≃ A 4 {\sf G}\simeq A_{4}.

*Proof.*We already know that A 4 ≃ G ¯ ≤ 𝖦 A_{4}\simeq\overline{G}\leq{\sf G}, so 𝖦 {\sf G} cannot be cyclic nor dihedral. The only candidates are therefore A 4 A_{4}, S 4 S_{4} and A 5 A_{5}. Observe that the orbit type of S 4 S_{4} and A 5 A_{5}, and Claim 9.5, force every hemiset A A to lie in the same orbit as − A -A. To prove the claim, it thus suffices to exhibit an affine hemiset of P P with no orientation reversing symmetry.

Note that P P consists of 8 8 groups of 4 4 close-by points, each group being isometric to either S 1 S_{1} of − S 1 -S_{1}. We write S i S_{i} for the group containing p i p_{i}, and S − i S_{-i} for the group containing − p i -p_{i}. Let H H be the open hemisphere centered at p 1 p_{1}, and let A = def P ∩ H A\stackrel{{{}_{\text{\tiny{def}}}}}{{=}}P\cap H. The set A A is an affine hemiset of P P and A = S 1 ∪ S − 2 ∪ S − 3 ∪ S − 4 A=S_{1}\cup S_{-2}\cup S_{-3}\cup S_{-4}, see Figure 9. The set A A has four convex layer of odd size and therefore, by Claim 9.17, no orientation reversing symmetry. The statement follows.

Figure 9: An 16-point set with projective completion with symmetry A 4 A_{4}. The five layers of size 1,3,3,6, and 3, resp., are indicated by dashed polygons.

## 10 Generalizations: higher dimension and abstract order types

We now examine to what extent the previous analysis generalizes to higher dimension and to related structures.

### 10.1 Arbitrary dimension

Our methods for labeled affine order types generalize to finite subsets of 𝕊 d \mathbb{S}^{d}, the unit sphere in ℝ d + 1 \mathbb{R}^{d+1}.

Let us clarify how the notions generalize (without surprise) to higher dimensions. We call a subset of 𝕊 d \mathbb{S}^{d}*affine*if it is contained in an open hemisphere; a point of an affine subset is *extreme*if it can be cut out from the rest of the set by a great hypersphere, that is, the intersection of 𝕊 d \mathbb{S}^{d} with a hyperplane through the origin 𝟎 \mathbf{0}. A subset P P of 𝕊 d \mathbb{S}^{d} is *projective*if − p ∈ P -p\in P for every p ∈ P p\in P. An affine set is *in general position*if no d + 1 d+1 points are coplanar with 𝟎 \mathbf{0}; a projective set is *in general position*if whenever d + 1 d+1 points are coplanar with 𝟎 \mathbf{0}, two of them are antipodal. The *orientation*, χ ⁡ ( p 1, p 2, …, p d + 1) {\chi}(p_{1},p_{2},\ldots,p_{d+1}), of a ( d + 1) (d+1) -tuple ( p 1, p 2, …, p d + 1) (p_{1},p_{2},\ldots,p_{d+1}) of points in 𝕊 d \mathbb{S}^{d} is the sign, − 1 -1, 0 0, or 1 1, of the determinant of the matrix ( p 1, p 2, …, p d + 1) ∈ ℝ ( d + 1) × ( d + 1) (p_{1},p_{2},\ldots,p_{d+1})\in\mathbb{R}^{(d+1)\times(d+1)}. Two affine (projective, resp.) sets have the same *affine*(*projective*, resp.) *order type*if there exists an orientation preserving bijection between them. Two affine point sequences ( p 1, p 2, …, p n) (p_{1},p_{2},\ldots,p_{n}) and ( q 1, q 2, …, q n) (q_{1},q_{2},\ldots,q_{n}) are defined to be of the same *labeled affine order type*if the map p i ↦ q i p_{i}\mapsto q_{i} preserves orientations.

As for d = 2 d=2, the *projective completion*of an affine set A A is the projective set A ∪ − A A\cup-A. A *hemiset*of a projective set is its intersection with a closed hemisphere, and a hemiset is *affine*if it is contained in an open hemisphere, that is, if it does not contain any antipodal pair. We again have that a projective set P P is the projective completion of an affine set A A if and only if A A is an affine hemiset of P P.

In the arguments for the following theorem we only outline the differences w.r.t. the 2-dimensional setting.

###### Theorem 10.1.

For n ≥ d + 1 n\geq d+1, the number of faces of dimension k − 1 k-1 in the convex hull of a random simple labeled order type chosen uniformly among the simple, labeled order types of size n n in ℝ d \mathbb{R}^{d} has average 2 k ​ ( d k) + o ⁡ ( 1) 2^{k}\binom{d}{k}+o(1); for k = 1 k=1, this random variable has variance O ⁡ ( 1) O(1). In particular, the number of extreme points ( 0 0 -faces of the convex hull) has average 2 ​ d + o ⁡ ( 1) 2d+o(1), with constant variance, and the number of facets ( ( d − 1) (d-1) -faces) of the convex hull has average 2 d + o ⁡ ( 1) 2^{d}+o(1).

*Proof outline.*Let n ≥ d + 1 n\geq d+1. Let P P be a projective set of 2 ​ n 2n points. As for d = 2 d=2, the projective symmetries of P P act on its (affine) hemisets, the affine hemisets of P P of given order type form an orbit in this action, and the stabilizer of an affine hemiset is isomorphic to its (affine) symmetry group.

Let ω \omega be the order type of an affine hemiset of P P. Again, the number of (affine) symmetries of ω \omega affects both how frequently ω \omega occurs among the affine hemisets of P P, and how many distinct *labeled*affine order types are supported by ω \omega. As for d = 2 d=2, these two effects balance each other out and Proposition 4.1 generalizes: picking uniformly a random affine hemiset of P P, then picking uniformly a random ordering of the points of that hemiset produces a random labeled affine order type distributed *uniformly*among all those that can be obtained from P P.

In 𝕊 d \mathbb{S}^{d}, the dual p ∗ p^{*} of a point p p is the great hypersphere cut out by the hyperplane perpendicular to the line 𝟎 ​ p \mathbf{0}p in 𝟎 \mathbf{0}. Any projective set of 2 ​ n 2n points, n ≥ d + 1 n\geq d+1, therefore has an associated dual arrangement P ∗ P^{*} of n n great hyperspheres. Lemma 4.2 readily generalizes: there is a bijection ϕ \phi between the affine hemisets of a projective point set P P and the cells (i.e., full-dimensional faces) of the dual arrangement P ∗ P^{*}, such that a nonempty subset S ⊆ A S\subseteq A forms a face (which has to be a ( k − 1) (k-1) -face, k = | S | k=|S|) in the convex hull of an affine hemiset A A if and only if the intersection of the k k great hyperspheres { p ∗ ∣ p ∈ S } \{p^{*}\mid p\in S\} supports a ( d − k) (d-k) -face of ϕ ⁡ ( A) \phi(A).

Let f d, k ​ ( n) f_{d,k}\left(n\right) denote the number of faces of codimension k k (i.e., dimension d − k d-k) in P ∗ P^{*}. Every face of codimension k k of P ∗ P^{*} is contained in the intersection of a unique subset of k k of the hyperspheres, in which it is a cell of the induced ( d − k) (d-k) -dimensional arrangement. Hence,

 | f d, k ​ ( n) = ( n k) ​ f d − k, 0 ​ ( n − k). f_{d,k}\left(n\right)=\binom{n}{k}f_{d-k,0}\left(n-k\right). |  |

An arrangement of n n hyperplanes in general position in ℝ d \mathbb{R}^{d} has ∑ i = 0 d ( n i) \sum_{i=0}^{d}{n\choose i} cells [22, Lemma 1.2]. As explained in Section 2, P ∗ P^{*} can be decomposed into 2 2 inverted copies of an arrangement of n − 1 n-1 hyperplanes in ℝ d \mathbb{R}^{d}, so we have

 | f d, 0 ​ ( n) = 2 ​ ∑ i = 0 d ( n − 1 i) and, more generally, f d, k ​ ( n) = 2 ​ ( n k) ​ ∑ i = 0 d − k ( n − k − 1 i). f_{d,0}\left(n\right)=2\sum_{i=0}^{d}{n-1\choose i}\quad\text{and, more generally,}\quad f_{d,k}\left(n\right)=2\binom{n}{k}\sum_{i=0}^{d-k}{n-k-1\choose i}. |  |

The number of cells of P ∗ P^{*} that contain a given j j -face is 2 d − j 2^{d-j}; see [22, Lemma 1.1] (remark that by projecting along the affine span of the j j -face, this is the same as counting the number of cells that contain a given vertex in an arrangement of hyperplanes in general position in ℝ d − j \mathbb{R}^{d-j}). The average number of faces of codimension k k of a cell of P ∗ P^{*} is therefore

 | 2 k ​ f d, k ​ ( n) f d, 0 ​ ( n) = 2 k ​ ( n k) ​ ∑ i = 0 d − k ( n − k − 1 i) ∑ i = 0 d ( n − 1 i) = 2 k ​ ( n k) ​ ( n − k − 1 d − k) ( n − 1 d) + o ⁡ ( 1), \frac{2^{k}f_{d,k}\left(n\right)}{f_{d,0}\left(n\right)}=\frac{\displaystyle 2^{k}\binom{n}{k}\sum_{i=0}^{d-k}{n-k-1\choose i}}{\displaystyle\sum_{i=0}^{d}{n-1\choose i}}=2^{k}\frac{\displaystyle\binom{n}{k}{n-k-1\choose d-k}}{\displaystyle\binom{n-1}{d}}+o(1), |  |

that is, 2 k ​ ( d k) + o ⁡ ( 1) 2^{k}\binom{d}{k}+o(1). This is also the average number of ( k − 1) (k-1) -faces in the convex hull of an affine hemiset, as announced.

To bound the variance, we can use the general version of the zone theorem [23]. For p ∈ P p\in P, let Z ⁡ ( p ∗) Z(p^{*}) denote the zone of p ∗ p^{*}, i.e., the set of cells of P ∗ P^{*} incident to p ∗ p^{*}. For a cell c c, let | c | |c| denote the number of facets (faces of codimension 1 1) that are incident to c c. Then ∑ c ∈ Z ⁡ ( p ∗) | c | = O ⁡ ( n d − 1) \sum_{c\in Z(p^{*})}|c|=O\left(n^{d-1}\right) and the average squared number of facets in a random full-dimensional cell of P ∗ P^{*} is O ⁡ ( 1) O(1).

As for *unlabeled*affine order types, we do not see that any of our results in the plane generalizes. The information we extract on orbit types depends on the fact that every projective symmetry has exactly two poles (Proposition 5.1); our proof of that fact relies on the hairy ball theorem, which only holds in even dimension. The analysis of reflections may be another difficulty: the transversal theorem of Hadwiger that we used was generalized to hyperplane transversals [33] but with the ordering condition rephrased (interestingly, in terms of order types). Also, our analysis of symmetries of affine sets is specific to the planar setting.

### 10.2 Abstract order types (acyclic uniform oriented matroids)

The order type records the orientation of every triple of points, that is, the position of each point with respect to the line through the other two. This can also be carried out in a more general setting where the usual (straight) lines of the affine setting are replaced by curves forming a pseudoline arrangement. Starting with a *topological projective plane*[35] and distinguishing a pseudoline as being “at infinity”, one obtains a *topological affine plane*, in which orientations are well-defined: through any two points there is a unique pseudoline, and together with the pseudoline at infinity it cuts out two connected components (just like a line in the affine plane). The equivalence classes of finite subsets of topological affine planes modulo orientation preserving bijections are called *abstract order types*. Since the affine plane is a topological affine plane, any order type is an abstract order type. The converse is not true, and we refer to the survey of Goodman and Felsner [27] for a discussion of some of the differences. Unlike order types, abstract order types are amenable to combinatorial methods, and are characterized by a few simple axioms [43]; they are, in fact, equivalent to *relabeling classes of rank 3 3 acyclic oriented matroids*, a classical combinatorial structure [13]. More generally, order types of point sets in ℝ d \mathbb{R}^{d} enjoy a similar abstract generalization, which turns out to be equivalent to relabeling classes of rank d + 1 d+1 acyclic oriented matroids.

Our approach generalizes to abstract order types as follows. We work again on 𝕊 2 \mathbb{S}^{2}, but now equipped with a system of pseudocircles, each symmetric with respect to the origin 𝟎 \mathbf{0}. An open pseudo-hemisphere is a connected component in the complement of a pseudocircle, and a closed pseudo-hemisphere is the closure of an open one. The abstract order types are read off intersections of projective sets with closed pseudo-hemispheres with no point on the boundary, and the notions of extreme point, extreme edge, convex hull, …carry through. The content of Sections 3 and 4 generalizes readily (in particular, the combinatorics of the dual arrangement and the bound used for the zone theorem [12] holds also for pseudolines), and we obtain:

###### Theorem 10.2.

For n ≥ 3 n\geq 3, the number of extreme points in a random simple labeled abstract order type chosen uniformly among the simple, labeled order types of size n n has average 4 − 8 n 2 − n + 2 4-\mbox{$\frac{8}{n^{2}-n+2}$} and variance at most 3 3.

The extension to higher dimension for labeled order types also generalizes to the abstract setting:

###### Theorem 10.3.

For n ≥ d + 1 n\geq d+1, the number of faces of dimension k − 1 k-1 in the convex hull of a random simple labeled abstract order type chosen uniformly among the simple, labeled, d d -dimensional abstract order types of size n n has average 2 k ​ ( d k) + o ⁡ ( 1) 2^{k}\binom{d}{k}+o(1); for k = 1 k=1, this random variable has variance O ⁡ ( 1) O(1).

In the *unlabeled*setting, most of the proof of Theorem 1.3 goes through, with the notable exception of the proof of Proposition 6.3 (specific to the realizable setting since it reformulates orientations as signs of polynomials). We expect that an analogue of Proposition 6.3 holds for abstract order types and that Theorem 1.3 generalizes, but settle here for a slightly weaker version.

###### Theorem 10.4.

For n ≥ 3 n\geq 3, the number of extreme points in a random simple abstract order type chosen uniformly among the simple abstract order types of size n n in the plane has average O ⁡ ( 1) O(1).

*Proof outline.*From the beginning of Section 5 to Corollary 6.2, everything generalizes readily. The only nontrivial step is the use of Hadwiger’s transversal theorem, but Basu et al. [11, Theorem 5] provides the required generalization. In particular, in the abstract setting we do have that

1. (a)

projective symmetries have exactly two, opposite, poles,

2. (b)

the possible orbit types are the same in the realizable and abstract settings,

3. (c)

abstract order types have the same symmetry groups as the realizable ones (that is, Theorem 1.5 holds also for abstract order types), and

4. (d)

every abstract order type of size n n corresponds to at least ( n − 1)! (n-1)! and at most n! n! labeled abstract order types.

We cannot control the number of abstract order types with many symmetries as in the affine setting by counting sign vectors of polynomials. Still, the proof of Proposition 6.4 does not require it, and readily goes through. In other words, the average number of extreme points in an abstract order type of size n n, chosen uniformly conditioned on a given projective completion, is at most 4 + 3 ​ N / n 4+3N/n where N N is the number of projective symmetries.

Then, all of Section 9 readily extends to the abstract setting. This include the correspondence between orbit types and maximal cyclic subgroups (Proposition 9.2), which ensures that any abstract projective order type with 2 ​ n 2n points and N > 60 N>60 symmetries has a cyclic subgroup of size N N or N / 2 N/2, so that n ≥ N / 2 n\geq N/2. Altogether, for every sufficiently large abstract projective order type, the average number of extreme points in the abstract order types it contains is at most 10 10. The statement follows.

As noted in the proof outline of Theorem 10.4, the classifications of symmetry groups (Theorems 1.5 and 1.6) also hold in the abstract setting.

## 11 Outlook: random sampling via projective order types

We wrap up by continuing the discussion about sampling random order types from Section 1.4, now with the extra insights from the results of this paper and its approach.

Let us clarify the algorithmic problems we consider here. We take as input an integer n ≥ 3 n\geq 3 and want to output an element chosen uniformly at random in 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}, 𝖮𝖳 aff n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} or 𝖮𝖳 proj n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n}, depending on the variant of the problem. The algorithm has access to a sequence of uniform random bits. For simplicity, we represent an element of 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} as the orientation map χ {\chi} from the ordered triples from { 1, 2, …, n } \{1,2,\ldots,n\} to { − 1, 1 } \{-1,1\}, but note that more compact representations are possible (for instance the λ \lambda -matrices of Goodman and Pollack [31, Def. 1.3,Cor. 1.9] or the encoding based on hierarchical cuttings of Cardinal et al. [17]). We represent an element of 𝖮𝖳 aff n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} or 𝖮𝖳 proj n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n} as any labeled order type it contains. To be clear, ω ∈ 𝖮𝖳 aff n \omega\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}*contains*ω ¯ ∈ 𝖫𝖮𝖳 aff n \overline{\omega}\in{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} if the latter can be obtained by ordering the vertices of the former; π ∈ 𝖮𝖳 proj n \pi\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n}*contains*ω ∈ 𝖮𝖳 aff n \omega\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} if the latter is the order type of some affine hemiset of the former; π ∈ 𝖮𝖳 proj n \pi\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n} contains ω ¯ ∈ 𝖫𝖮𝖳 aff n \overline{\omega}\in{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} if there exists ω ∈ 𝖮𝖳 aff n \omega\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} that is contained in the former and contains the latter. Let us stress that given two orientation maps, one can decide in O ⁡ ( n 2) O(n^{2}) time whether the labeled affine order types they represent are contained in the same affine order type, i.e., isomorphic, see Aloupis et al. [5].

### 11.1 Polynomial-time equivalence

Let us first argue that any of the variants of the problem reduces to any other variant in time polynomial in n n.

##### From projective to labeled affine.

Assume given an algorithm 𝒜 \mathcal{A} that outputs a random projective order type π \pi chosen uniformly in 𝖮𝖳 proj n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n}. We first describe a preliminary procedure for a uniform sampling of 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n} which allows failure, i.e., the procedure may decide to output a failure symbol ⟂ \perp instead of a labeled affine order type: For π ∈ 𝖮𝖳 proj n \pi\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n} generated by 𝒜 \mathcal{A}, we first determine the symmetry group 𝖦 π {\sf G}_{\pi} of π \pi. With probability 1 | 𝖦 π | \frac{1}{|{\sf G}_{\pi}|}, we pick an affine hemiset of π \pi uniformly at random, then an ordering of its vertices uniformly at random, and then we output this labeled affine order type ρ ¯ \overline{\rho} (note that ρ ¯ \overline{\rho} is uniformly chosen in 𝖫𝖮𝖳 aff π {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi} by Proposition 4.1). With probability 1 − 1 | 𝖦 π | 1-\frac{1}{|{\sf G}_{\pi}|}, we output ⟂ \perp. The necessary operations can be performed in time polynomial in n n, in particular, computing the symmetry group can be done in O ⁡ ( n 2) O(n^{2}) time, along the lines of Aloupis et al. [5].

Since | 𝖦 π | ≤ max ⁡ { 60, 2 ​ n } |{\sf G}_{\pi}|\leq\max\{60,2n\}, the procedure succeeds in producing an order type with probability Ω ⁡ ( n − 1) \Omega\left(n^{-1}\right). Hence, if we repeat the procedure until success, O ⁡ ( n) O(n) iterations will suffice on average. It remains to ensure that the procedure generates every ω ¯ \overline{\omega} with the same probability. Let π ω \pi_{\omega} be the completion of ω \omega (the unlabeled affine order type underlying ω ¯ \overline{\omega}). Then the probability of the procedure to output ω ¯ \overline{\omega} is given by

 | 1 | 𝖮𝖳 proj n | ⋅ 1 | 𝖦 π ω | ⋅ 1 | 𝖫𝖮𝖳 aff π ω | = 1 | 𝖮𝖳 proj n | ⋅ 1 ( 2 ​ ( n 2) + 2) ​ n! \frac{1}{|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n}|}\cdot\frac{1}{|{\sf G}_{\pi_{\omega}}|}\cdot\frac{1}{|{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi_{\omega}}|}=\frac{1}{|{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n}|}\cdot\frac{1}{\left(2\binom{n}{2}+2\right)n!} |  |

where we use | 𝖫𝖮𝖳 π aff | = ( 2 ( n 2) + 2) n! | 𝖦 π | |{\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!\pi}|=\left(2\binom{n}{2}+2\right)\frac{n!}{|{\sf G}_{\pi}|} (see end of proof of Proposition 4.1).

##### From labeled affine to affine.

Now, assume given an algorithm 𝒜 \mathcal{A} that outputs a random labeled affine order type ρ ¯ \overline{\rho} chosen uniformly in 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}. Simply outputting the affine order type that contains ρ ¯ \overline{\rho} gives us a random generator of affine order types, but it has some bias: indeed, an affine order type ω \omega with symmetry group 𝖥 ω {\sf F}_{\omega} contains exactly n! | 𝖥 ω | \frac{n!}{|{\sf F}_{\omega}|} distinct labeled affine order types. Since 1 ≤ | 𝖥 ω | ≤ n 1\leq|{\sf F}_{\omega}|\leq n, we can correct this bias using rejection, by accepting the output ω ¯ \overline{\omega} of algorithm 𝒜 \mathcal{A} with probability | 𝖥 ω | n \frac{|{\sf F}_{\omega}|}{n}. Clearly, at most n n iterations are needed in expectation. Computing the symmetry group of an affine order type can be done in O ⁡ ( n 2) O(n^{2}) time, as shown by Aloupis et al. [5].

##### From affine to projective.

Finally, assume given an algorithm 𝒜 \mathcal{A} that outputs a random affine order type ρ \rho chosen uniformly in 𝖮𝖳 aff n {\sf O\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}. Again, we output the projective order type containing ρ \rho (i.e., the completion of ρ \rho) after correcting for bias via rejection: a projective order type contains between 1 1 and 2 ​ ( n 2) + 2 2\binom{n}{2}+2 affine order types. The number of affine order types contained in a given π ∈ 𝖮𝖳 proj n \pi\in{\sf O\hskip-1.00006ptT}^{{}_{\mathrm{proj}}}_{\!n} can be computed in polynomial time by examining each affine hemiset in turn, and counting how many distinct affine order types occur. The number of rejections is O ⁡ ( n 2) O(n^{2}) on average.

##### About concentration.

The transforms listed above can turn any algorithm 𝒜 \mathcal{A} simulating a distribution on one sort of order types into an algorithm 𝒜 ′ \mathcal{A}^{\prime} simulating a distribution on another sort of order types. Let us remark, however, that when 𝒜 \mathcal{A} is not uniform, our transforms may no longer compensate exactly the imbalance due to the fact that an n n -point order type (affine or projective, labeled or not) may have from 1 1 to Θ ⁡ ( n) \Theta(n) symmetries. We cannot exclude that (the distribution simulated by) 𝒜 ′ \mathcal{A}^{\prime} exhibits concentration, altough (the one simulated by) 𝒜 \mathcal{A} does not. However, if 𝒜 ′ \mathcal{A}^{\prime} is *sufficiently*concentrated, in the sense that a subset A n A_{n} of the order type gets hit with probability going to 1 1 but represents a fraction o ⁡ ( n 2) o(n^{2}) of all order types, then it must be that 𝒜 \mathcal{A} already exhibits concentration.

### 11.2 Models from projective order types

Starting from *any*distribution on projective order types, the (polynomial-time) transform “projective to labeled affine” presented above produces a distribution on labeled affine order types with average number of extreme points equal to 4 − 8 n 2 − n + 2 4-\mbox{$\frac{8}{n^{2}-n+2}$}, *just like the equiprobable distribution on 𝖫𝖮𝖳 aff n {\sf L\hskip-1.00006ptO\hskip-1.00006ptT}^{{}_{\mathrm{aff}}}_{\!n}*. In particular, the selection of an affine hemiset equiprobably (whether or not we account for symmetries) seems effective at breaking the “reducibility” barrier pointed out right after Conjecture 1.8.

A natural distribution on projective order types is given by the projective order type of the projective completion of n n points chosen independently and uniformly on 𝕊 2 \mathbb{S}^{2}. This leads to two natural distributions on labeled affine order types:

Geometric projection:

pick a hemisphere uniformly at random among all hemispheres, read off the order type of the affine hemiset that it determines almost surely, and conclude by ordering the points uniformly at random.

Combinatorial projection:

pick an affine hemiset equiprobably, read off its order type and order uniformly at random.

In other words, the geometric projection selects an affine hemiset with probability proportional to the area of its dual cell (rather than with equiprobability).

###### Question 11.1.

Does the distribution on affine order types given by the geometric or combinatorial projection of the uniform measure on 𝕊 2 \mathbb{S}^{2} exhibit concentration?

For the geometric projection, concentration would follow from our Conjecture 1.8. Note that order types obtained from the geometric projection already have a constant number of extreme points on average [7, 39], so Conjecture 1.7 would not suffice.

## References

- [1] Adiprasito, K. A., and Padrol, A. The universality theorem for neighborly polytopes. Combinatorica 37, 2 (2017), 129–136.
- [2] Aichholzer, O., Aurenhammer, F., and Krasser, H. Enumerating order types for small point sets with applications. Order 19, 3 (2002), 265–281.
- [3] Aichholzer, O., and Krasser, H. Abstract order type extension and new results on the rectilinear crossing number. Computational Geometry 36, 1 (2007), 2 – 15. Special Issue on the 21st European Workshop on Computational Geometry.
- [4] Alon, N. The number of polytopes, configurations and real matroids. Mathematika 33, 1 (1986), 62–71.
- [5] Aloupis, G., Iacono, J., Langerman, S., Özkan, Ö., and Wuhrer, S. The complexity of order type isomorphism. In Proceedings of the Twenty-Fifth Annual ACM-SIAM Symposium on Discrete Algorithms, SODA 2014, Portland, Oregon, USA, January 5-7, 2014 (2014), C. Chekuri, Ed., SIAM, pp. 405–415.
- [6] Bárány, I., Fradelizi, M., Goaoc, X., Hubard, A., and Rote, G. Random polytopes and the wet part for arbitrary probability distributions. Annales Henri Lebesgue 3 (2020), 701–715.
- [7] Bárány, I., Hug, D., Reitzner, M., and Schneider, R. Random points in halfspheres. Random Structures & Algorithms 50, 1 (2017), 3–22.
- [8] Bárány, I., and Larman, D. G. Convex bodies, economic cap coverings, random polytopes. Mathematika 35, 2 (1988), 274–291.
- [9] Bárány, I., and Reitzner, M. On the variance of random polytopes. Advances in Mathematics 225, 4 (2010), 1986–2001.
- [10] Baryshnikov, Y. M., and Vitale, R. A. Regular simplices and Gaussian samples. Discrete & Computational Geometry 11, 2 (1994), 141–147.
- [11] Basu, S., Goodman, J. E., Holmsen, A., and Pollack, R. The Hadwiger transversal theorem for pseudolines. Combinatorial and Computational Geometry, Math. Sci. Res. Inst. Publ 52 (2004), 79–85.
- [12] Bern, M. W., Eppstein, D., Plassmann, P. E., and Yao, F. F. Horizon theorems for lines and polygons. In Discrete and Computational Geometry: Papers from the DIMACS Special Year (1990), J. E. Goodman, R. Pollack, and W. Steiger, Eds., vol. 6 of DIMACS Series in Discrete Mathematics and Theoretical Computer Science, DIMACS/AMS, pp. 45–66.
- [13] Björner, A., Las Vergnas, M., Sturmfels, B., White, N., and Ziegler, G. M. Oriented matroids. No. 46 in Encyclopedia of Mathematics and its Applications. Cambridge University Press, 1999.
- [14] Bland, R. G. Complementary orthogonal subspaces of n-dimensional Euclidean space and orientability of matroids. PhD thesis, Cornell University, 1974.
- [15] Bokowski, J., Richter-Gebert, J., and Schindler, W. On the distribution of order types. Computational Geometry 1, 3 (1992), 127–142.
- [16] Caraballo, L. E., Díaz-Báñez, J.-M., Fabila-Monroy, R., Hidalgo-Toscano, C., Leaños, J., and Montejano, A. On the number of order types in integer grids of small size. Computational Geometry 95 (2021), 101730.
- [17] Cardinal, J., Chan, T. M., Iacono, J., Langerman, S., and Ooms, A. Subquadratic encodings for point configurations. Journal of Computational Geometry 10, 2 (2019), 99–126.
- [18] Cardinal, J., Fabila-Monroy, R., and Hidalgo-Toscano, C. Chirotopes of random points in space are realizable on a small integer grid, 2020. arXiv:2001.08062.
- [19] Carver, W. The polygonal regions into which a plane is divided by n n straight lines. The American Mathematical Monthly 48, 10 (1941), 667–675.
- [20] Chiu, M., Felsner, S., Scheucher, M., Schnider, P., and Valtr, P. On the average complexity of the k-level. Journal of Computational Geometry 11, 1 (2020), 493–506.
- [21] Devillers, O., Duchon, P., Glisse, M., and Goaoc, X. On order types of random point sets, 2020. arXiv:1812.08525.
- [22] Edelsbrunner, H. Algorithms in combinatorial geometry, vol. 10 of Monographs in Theoretical Computer Science. Springer Science & Business Media, 1987.
- [23] Edelsbrunner, H., Seidel, R., and Sharir, M. On the zone theorem for hyperplane arrangements. SIAM Journal on Computing 22, 2 (1993), 418–429.
- [24] Eppstein, D. Forbidden configurations in discrete geometry. Cambridge University Press, 2018.
- [25] Erdős, P., and Szekeres, G. A combinatorial problem in geometry. Compositio mathematica 2 (1935), 463–470.
- [26] Fabila-Monroy, R., and Huemer, C. Order types of random point sets can be realized with small integer coordinates. In XVII Spanish Meeting on Computational Geometry: book of abstracts, Alicante, June 26-28 (2017), pp. 73–76.
- [27] Felsner, S., and Goodman, J. E. Pseudoline arrangements. In Handbook of Discrete and Computational Geometry. Chapman and Hall/CRC, 2017, pp. 125–157.
- [28] Folkman, J., and Lawrence, J. Oriented matroids. Journal of Combinatorial Theory, Series B 25, 2 (1978), 199–236.
- [29] Gerken, T. Empty convex hexagons in planar point sets. Discrete & Computational Geometry 39, 1-3 (2008), 239–272.
- [30] Goaoc, X., Hubard, A., de Verclos, R. d. J., Sereni, J.-S., and Volec, J. Limits of order types, 2018. arXiv:1811.02236.
- [31] Goodman, J. E., and Pollack, R. Multidimensional sorting. SIAM Journal on Computing 12, 3 (1983), 484–507.
- [32] Goodman, J. E., and Pollack, R. Upper bounds for configurations and polytopes in ℝ d {\mathbb{R}}^{d}. Discrete & Computational Geometry 1, 3 (1986), 219–227.
- [33] Goodman, J. E., and Pollack, R. Hadwiger’s transversal theorem in higher dimensions. Journal of the American Mathematical Society 1, 2 (1988), 301–309.
- [34] Goodman, J. E., Pollack, R., and Sturmfels, B. The intrinsic spread of a configuration in ℝ d \mathbb{R}^{d}. Journal of the American Mathematical Society (1990), 639–651.
- [35] Goodman, J. E., Pollack, R., Wenger, R., and Zamfirescu, T. Arrangements and topological planes. The American Mathematical Monthly 101, 9 (1994), 866–878.
- [36] Hadwiger, H. Über Eibereiche mit gemeinsamer Treffgeraden. Portugalia Mathematica 16, 1 (1957), 23–57.
- [37] Han, J., Kohayakawa, Y., Sales, M. T., and Stagni, H. Extremal and probabilistic results for order types. In Proceedings of the Thirtieth Annual ACM-SIAM Symposium on Discrete Algorithms (2019), SIAM, pp. 426–435.
- [38] Har-Peled, S. On the expected complexity of random convex hulls, 2011. arXiv:1111.5340.
- [39] Kabluchko, Z., Marynych, A., Temesvari, D., and Thäle, C. Cones generated by random points on half-spheres and convex hulls of poisson point processes. Probability Theory and Related Fields 175, 3 (2019), 1021–1061.
- [40] Károlyi, G., and Solymosi, J. Erdős–Szekeres theorem with forbidden order types. Journal of Combinatorial Theory, Series A 113, 3 (2006), 455–465.
- [41] Károlyi, G., and Tóth, G. Erdős–Szekeres theorem for point sets with forbidden subconfigurations. Discrete & Computational Geometry 48, 2 (2012), 441–452.
- [42] Kettner, L., Mehlhorn, K., Pion, S., Schirra, S., and Yap, C. Classroom examples of robustness problems in geometric computations. Computational Geometry 40, 1 (2008), 61–78.
- [43] Knuth, D. E. Axioms and hulls, vol. 606 of Lecture Notes in Computer Science. Springer, 1992.
- [44] Las Vergnas, M. Matroides orientables. CR Acad. Sci. Paris (1975).
- [45] Marcus, A., and Tardos, G. Excluded permutation matrices and the Stanley–Wilf conjecture. Journal of Combinatorial Theory, Series A 107, 1 (2004), 153–160.
- [46] Miyata, H. On symmetry groups of oriented matroids, 2013. arXiv:1301.6451.
- [47] Mnëv, N. E. The universality theorem on the oriented matroid stratification of the space of real matrices. In Discrete and Computational Geometry: Papers from the DIMACS Special Year (1990), J. E. Goodman, R. Pollack, and W. Steiger, Eds., vol. 6 of DIMACS Series in Discrete Mathematics and Theoretical Computer Science, DIMACS/AMS, pp. 237–244.
- [48] Nešetřil, J., and Valtr, P. A Ramsey property of order types. Journal of Combinatorial Theory, Series A 81, 1 (1998), 88–107.
- [49] Olaverri, A. G., Noy, M., and Tejel, J. Lower bounds on the number of crossing-free subgraphs of K N {K}_{N}. Comput. Geom. 16, 4 (2000), 211–221.
- [50] Overmars, M. Finding sets of points without empty convex 6-gons. Discrete & Computational Geometry 29, 1 (2002), 153–158.
- [51] Reitzner, M. Random polytopes. In New Perspectives in Stochastic Geometry, W. S. Kendall and I. Molchanov, Eds. Oxford University Press, 2009, ch. 2, pp. 45–75.
- [52] Rényi, A., and Sulanke, R. Über die konvexe Hülle von n n zufällig gewählten Punkten. Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete 2, 1 (1963), 75–84.
- [53] Rényi, A., and Sulanke, R. Über die konvexe Hülle von n n zufällig gewählten Punkten. II. Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete 3, 2 (1964), 138–147.
- [54] Salzmann, H. R. Topological planes. Advances in mathematics 2, 1 (1967), 1–60.
- [55] Schaefer, M. Complexity of some geometric and topological problems. In Graph Drawing, 17th International Symposium, GD 2009, Chicago, IL, USA, September 22-25, 2009. Revised Papers (2009), D. Eppstein and E. R. Gansner, Eds., vol. 5849 of Lecture Notes in Computer Science, Springer, pp. 334–344.
- [56] Senechal, M. Finding the finite groups of symmetries of the sphere. The American Mathematical Monthly 97, 4 (1990), 329–335.
- [57] Shor, P. Stretchability of pseudolines is NP-hard. Applied Geometry and Discrete Mathematics-The Victor Klee Festschrift (1991).
- [58] Suk, A. On the Erdős-Szekeres convex polygon problem. Journal of the American Mathematical Society 30, 4 (2017), 1047–1053.
- [59] Suzuki, M. On the finite group with a complete partition. J. Math. Soc. Japan 2, 1-2 (09 1950), 165–185.
- [60] The CGAL Project. CGAL User and Reference Manual, 4.14 ed. CGAL Editorial Board, 2019.
- [61] van der Hoog, I., Miltzow, T., and van Schaik, M. Smoothed analysis of order types, 2019. arXiv:1907.04645.
- [62] Vu, V. Sharp concentration of random polytopes. Geometric & Functional Analysis GAFA 15, 6 (2005), 1284–1318.
- [63] Warren, H. E. Lower bounds for approximation by nonlinear manifolds. Transactions of the American Mathematical Society 133, 1 (1968), 167–178.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:
[2]: https://groupprops.subwiki.org/wiki/Groups_of_order_12
[3]: /html/2003.08455
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/2003.08456
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2003.08456
[9]: https://arxiv.org/pdf/2003.08456
[10]: /html/2003.08457
