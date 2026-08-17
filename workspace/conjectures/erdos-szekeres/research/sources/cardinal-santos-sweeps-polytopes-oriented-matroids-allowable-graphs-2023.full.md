<!-- source: https://link.springer.com/article/10.1007/s00493-023-00062-3 | converted from HTML -->

Sweeps, Polytopes, Oriented Matroids, and Allowable Graphs of Permutations | Combinatorica | Springer Nature Link

Skip to main content

# Sweeps, Polytopes, Oriented Matroids, and Allowable Graphs of Permutations

- Original Paper
- [Open access][1]
- Published: 23 October 2023

- Volume 44, pages 63–123 ( 2024)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Combinatorica][5] [Aims and scope][6] [Submit manuscript][7]

Sweeps, Polytopes, Oriented Matroids, and Allowable Graphs of Permutations

[Download PDF][2]

## Abstract

A sweep of a point configuration is any ordered partition induced by a linear functional. Posets of sweeps of planar point configurations were formalized and abstracted by Goodman and Pollack under the theory of allowable sequences of permutations. We introduce two generalizations that model posets of sweeps of higher dimensional configurations. Sweeps of a point configuration are in bijection with faces of an associated sweep polytope. Mimicking the fact that sweep polytopes are projections of permutahedra, we define sweep oriented matroids as strong maps of the braid oriented matroid. Allowable sequences are then the sweep oriented matroids of rank 2, and many of their properties extend to higher rank. We show strong ties between sweep oriented matroids and both modular hyperplanes and Dilworth truncations from (unoriented) matroid theory. Pseudo-sweeps are a generalization of sweeps in which the sweeping hyperplane is allowed to slightly change direction, and that can be extended to arbitrary oriented matroids in terms of cellular strings. We prove that for sweepable oriented matroids, sweep oriented matroids provide a sphere that is a deformation retract of the poset of pseudo-sweeps. This generalizes a property of sweep polytopes (which can be interpreted as monotone path polytopes of zonotopes), and solves a special case of the strong Generalized Baues Problem for cellular strings. A second generalization are allowable graphs of permutations: symmetric sets of permutations pairwise connected by allowable sequences. They have the structure of acycloids and include sweep oriented matroids.

### Similar content being viewed by others

### [The matroid stratification of the Hilbert scheme of points on \(\mathbb {P}^1\)][8]

Article 04 February 2021

### [Generalizations of Matroids][9]

Chapter © 2018

### [The Hypersimplex][10]

Chapter © 2023

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Combinatorics][11]
- [Combinatorial Geometry][12]
- [Discrete Mathematics][13]
- [Polytopes][14]
- [Set Theory][15]
- [Topology][16]
- [Geometric Combinatorics of Polytopes][17]

## 1 Introduction

It is very natural to order a point configuration by the values of a linear functional, and it is not surprising that applications abound in discrete and combinatorial geometry. For example, this is the core of sweep algorithms, a central paradigm in computational geometry (see [[27][18], Section 2.1]). The simplex methods for linear programming visit vertices of a convex polytope in such a linear order (see for example [[64][19]]). Moreover, these orderings are precisely those inducing the Bruggesser–Mani line shellings in the polar polytope [[18][20]] (see [[89][21], Lec. 8]).

**Fig. 1**

[image: Fig. 1]

[Full size image][22]

A segment of an allowable sequence. The sweeps between two consecutive permutations in the sequence correspond to ordered partitions

The set of all linear orderings of a planar point configuration was already studied by Perrin in 1882 [[68][23]]. This was a precursor to the theory of *allowable sequences*, introduced and developed by Goodman and Pollack [44, 45, 46, 47, [48][24]]. The idea is the following. Given a configuration \(\varvec{A}\) of *n*points in the plane, for each generic vector \(\varvec{u}\in {{\mathbb {R}}}^2\), we sweep the plane with a line orthogonal to \(\varvec{u}\). The order in which the points are hit by the line gives rise to a permutation \(\sigma \in \mathfrak {S}_{n}\) (see Fig. [1][25]). As \(\varvec{u}\) rotates \(180^{\circ }\) clockwise, we obtain a sequence of permutations in which:

1. (i)

the move from a permutation to the next one consists of reversing one or more disjoint substrings;

2. (ii)

each pair *i*, *j*with \(1\le i < j \le n\) is reversed in exactly one move along the sequence.

An *allowable sequence*is a sequence of permutations from the identity to its reverse ( \(\sigma ,{\overline{\sigma }}\in \mathfrak {S}_{n}\) are *reverse*if \(\sigma (t)=\overline{\sigma }(n-t+1)\) for all *t*) fulfilling these two conditions. Contrary to Perrin’s claim, Goodman and Pollack showed that there are unrealizable allowable sequences [[44][26], Fig. 3 and Thm. 3.1], that is, that do not arise from a point configuration with this construction (c.f. Fig. [10][27]).

Allowable sequences are hence purely combinatorial objects abstracting geometric properties of planar point configurations. They are closely related to pseudoline arrangements and oriented matroids (see [[17][28], Sects. 1.10 & 6.4]), although their combinatorial structure is in some senses easier to grasp and manipulate. In particular, in the *simple*case (where consecutive permutations differ by a transposition), allowable sequences are in correspondence with reduced decompositions of the reverse of the identity and maximal chains in the weak Bruhat order of \(\mathfrak {S}_{n}\), see [[17][28], Sec. 6.4], as well as with (minimal primitive) sorting networks [[59][29], Sec. 5.3.4]. This has allowed for their complete enumeration [[33][30], [79][31]], as well as the study of uniform random instances [[1][32], [4][33], [26][34]].

They turned out to be a very effective tool to study problems of geometric combinatorics in the plane, used for example to prove Ungar’s theorem (a configuration of 2*n*points not all on a same line determines at least 2*n*slopes) [[84][35]], to decide the stretchability of arrangements of at most eight pseudolines [[45][36]], or to estimate the number of *k*-sets and ( \(\le k\))-sets [[3][37], [60][38], [85][39]]. See [[48][24], Ch. V] and [[39][40], Ch. 6] for some of their applications.

The construction detailed above extends naturally to any higher dimensional point configuration \(\varvec{A}\in {{\mathbb {R}}}^{d\times [{n}]}\). Every vector \(\varvec{u}\in {{\mathbb {R}}}^d\) defines a *sweep*, which is the ordered partition of \([{n}]\) in which the points of \(\varvec{A}\) are met when sweeping with a hyperplane in direction \(\varvec{u}\). Goodman and Pollack already observed that sweeps induce a complex on the unit sphere \(\mathbb {S}^{d-1}\), *“which has not yet been fully investigated”*[[48][24], after Def. 2.3]. This was further explored by Edelman [[32][41]] and Stanley [[80][42]] who, in particular, presented a tight upper bound for the number of sweeping orders of a *d*-dimensional configuration of *n*points.

Ordered by refinement, the *poset of sweeps*\(\overline{\Pi }({\varvec{A}})\) is isomorphic to the face poset of a polyhedral fan generated by a hyperplane arrangement \(\mathcal{S}\mathcal{H}({\varvec{A}})\), called the *valid order arrangement*by Stanley in a polar formulation [[80][42]]. As we discuss in Sect. [2.3][43], this is the normal fan of a zonotope: the *sweep polytope*\(\varvec{SP}({\varvec{A}})\) (mentionned under the name of *shellotope*by Gritzmann and Sturmfels in [[50][44]]).

Posets of sweeps of point configurations are the high-dimensional analogue of realizable allowable sequences. However, there is no purely combinatorial description of these objects. Indeed, Hoffmann and Merckx recently adapted the classical Universality Theorem for oriented matroids by Mnëv [[65][45]] to give a Universality Theorem for allowable sequences [[54][46]]. This shows that already in the plane the problem of deciding whether an allowable sequence arises from a point configuration is very hard (equivalent to the “existential theory of the reals”, and in particular NP-hard).

Our main goal is to give a purely combinatorial high-dimensional generalization of allowable sequences that abstracts and encompasses the posets of sweeps of point configurations. We present two strongly related approaches with two levels of generality (*sweep oriented matroids*and *sweep acycloids*). As we will see, the objects that we introduce fill a gap connecting several topics studied by different communities, providing a new and unified point of view. We also hope that, beside their intrinsic interest, having a purely combinatorial framework without the rigid constraints of realizability will open the door to new approaches to problems on discrete and combinatorial geometry, as happened in the two-dimensional case.

Our starting point are sweep polytopes. We report alternative constructions that highlight different points of view. On the one hand, sweep polytopes are affine projections of permutahedra. The *n-permutahedron*\(\varvec{P}_{n}\subset {{\mathbb {R}}}^d\) is a classical polytope whose normal fan is the braid arrangement \(\mathcal {B}_{n}\). Up to translation, every affine projection of a permutahedron is a sweep polytope, which gives a natural combinatorial interpretation of permutahedral shadows. Moreover, sweep polytopes can be realized as fiber polytopes, and in particular as monotone path polytopes of zonotopes [[32][41], Sec. 5]. These are polytopes whose vertices encode the parametric simplex paths induced by a linear functional [[16][47], [23][48]]. Conversely, every monotone path polytope of a zonotope is a sweep polytope (under mild technical conditions, see Proposition [2.10][49]). This interpretation of sweep polytopes appears in the study of pivot rules in linear programming [[10][50]].

Moreover, this construction naturally reveals a decomposition of sweep polytopes as Minkowski sums of *k*-*set polytopes*[[6][51], [38][52]] (see Remark [2.9][53]). After the appearance of the first version of this article, most of these constructions have been generalized to *lineup polytopes*, which encode prefixes of sweeps and are relevant for the 1-body *N*-representability problem in quantum physics, see [[24][54]] and references therein.

Inspired by the characterization of sweep polytopes as permutahedral shadows, in Sect. [3][55] we define *sweep oriented matroids*as strong maps of the oriented matroid of the braid arrangement. The strong link between allowable sequences, oriented matroids of rank 3, and arrangements of pseudolines is well documented in [[17][28], Sects. 1.10 & 6.4] and explained in terms of *big*and *little oriented matroids*. These concepts extend to high dimensions too: each sweep oriented matroid of rank *r*determines a little and a big oriented matroid of rank \(r+1\) (Theorem [4.1][56] and Leema [4.4][57]). For sweep oriented matroids of rank 2, which are equivalent to allowable sequences, we recover the original definitions. In particular, in the realizable case, the little oriented matroid is the standard oriented matroid associated to the point configuration.

We show that, up to isomorphism, big oriented matroids are characterized by having a *tight modular hyperplane*(Theorem [4.9][58]). Modular flats of matroids were introduced by Stanley [[77][59]] and play a structural role for matroid constructions [[21][60]]. We call a modular hyperplane *tight*if it is no longer modular after the deletion of one of its elements. The operation that determines the big oriented matroid from its sweep oriented matroid extends to all oriented matroids equipped with certain decorations (Corollary [4.10][61]), and can be seen as an oriented matroid version of [[19][62], Thm. 2.1].

We extend the bounds from [[32][41], [80][42]] to the non-realizable case (Theorem [5.6][63]). For this, we show in Sect. [5][64] that, at the level of the underlying unoriented matroids, the lattice of flats of a sweep oriented matroid is (a weak map of) the first Dilworth truncation of the lattice of flats of the little oriented matroid (Theorem [5.2][65]). When one removes all the atoms from a geometric lattice, the resulting poset is no longer a geometric lattice. The first Dilworth truncation is a lattice obtained by adding the necessary joins in the most generic way to obtain a geometric lattice [[22][66], [29][67]]. We can therefore view sufficiently generic sweep oriented matroids as an oriented version of the first Dilworth truncation of the associated little oriented matroid. Unfortunately, in contrast to rank 3, not every (little) oriented matroid can be extended to a big oriented matroid (Theorem [4.13][68]). The question of characterizing oriented matroids admitting such an extension is open.

In Sect. [6][69], we discuss *pseudo-sweeps*, which correspond to sweeps in which the sweeping hyperplane is allowed to change direction (in a controlled monotonous way). Whereas sweeps of a point configuration correspond to the parametric (coherent) monotone paths on an associated zonotope, pseudo-sweeps take into account all monotone paths. They admit a polar formulation in terms of galleries and cellular strings of pseudo-hyperplane arrangements, which extends to oriented matroids [[13][70]]. This way, for every (little) oriented matroid, even those that cannot be extended to a big oriented matroid, one can define a poset of pseudo-sweeps. In general, an oriented matroid \(\mathcal {M}\) can be the little oriented matroid of several sweep oriented matroids; each with a different associated poset of sweeps. They are all subposets of the poset of pseudo-sweeps of \(\mathcal {M}\). A classification of the cases when all pseudo-sweeps are actual sweeps is given in [[35][71]].

There is a lot of literature concerning the graphs of pseudo-sweep permutations of oriented matroids. Cordovil and Moreira had shown that they are connected [[25][72]], extending to oriented matroids results that went back to Tits [[83][73]] (for reflection arrangements), Deligne [[28][74]] (for simplicial arrangements), and Salvetti [[75][75]] (for realizable oriented matroids). More results concerning graphs of pseudo-sweeps can be found in [[5][76], [73][77]].

The topology of the posets of pseudo-sweeps has been extensively studied as a special case of the *generalized Baues problem*[[23][48], [71][78]]. Without the trivial sweep, their order complexes have the homotopy type of, but in general are not homeomorphic to, a sphere. In the realizable case, Billera, Kapranov, and Sturmfels proved that the poset of sweeps is a strong deformation retract of the poset of pseudo-sweeps [[16][47]]. Their proof uses strongly the geometry of the fiber polytope construction. Björner [[13][70]] and Athanasiadis, Edelman, and Reiner [[2][79]] found combinatorial proofs that extend to general oriented matroids, but only give the homotopy type. Nevertheless, Björner claims that it is *“undoubtedly true”*that even for unrealizable oriented matroids there must be a sphere to which the poset of pseudo-sweeps retracts [[13][70], below Thm. 2]. However, there were no explicit candidates for these spheres. For oriented matroids that are little oriented matroids, we show in Theorem [6.6][80] that any of the associated sweep oriented matroids can play this role. That is, that the poset of non-trivial sweeps (which is a sphere) is a strong deformation retract of the poset of non-trivial pseudo-sweeps of the little oriented matroid. This highlights the fact that sweep oriented matroids should be seen as combinatorial analogues of monotone path polytopes of zonotopes; that is, sweep polytopes. Unfortunately, the existence of oriented matroids that are not little oriented matroids leaves some cases where Björner’s observation remains open.

In Sect. [7][81] we present a further generalization of sweep oriented matroids in terms of *allowable graphs of permutations*, which are closer to the original formulation of allowable sequences. Allowable graphs of permutations are graphs whose vertex sets are sets of permutations closed under taking reverses in which every pair of permutations is connected through a sequence of permutations fulfilling conditions (i) and (ii) above (plus some technical conditions when the moves are not simple). In the simple case, these are antipodal isometric subgraphs of the permutahedron. Translating back to sign-vectors, we obtain *sweep acycloids*(Theorem [7.12][82]), which have the structure of acycloids [[51][83]], also known as antipodal partial cubes [[41][84]]. Again, sweep acycloids (and thus allowable graphs of permutations) of rank 2 are equivalent to allowable sequences. Not every acycloid is an oriented matroid [[52][85], Sec. 7], but there are characterizations of those that are [[31][86], [52][85], [57][87]]. Since sweep acycloids that are oriented matroids are sweep oriented matroids (Corollary [7.18][88]), these give alternative characterizations of sweep oriented matroids in terms of allowable graphs of permutations (Corollary [7.20][89]). So far we could not find any example of a sweep acycloid that is not a sweep oriented matroid, and we leave this question as an open problem.

### 1.1 A Note Concerning the Terminology

The terms *sweep*and *sweeping*had already been used in the oriented matroids literature in the context of *topological sweepings*of affine oriented matroids and pseudo-hyperplane arrangements. These concepts should not be confused with the notions that we introduce in this paper.

The two colliding terminologies arise from the two classical dual geometric representations of realizable oriented matroids; namely, point configurations and hyperplane arrangements. Both give rise to a natural definition of *sweep*that generalizes to non-realizable matroids.

On the one hand, our definition of *sweep*is meant to model sweeps of point configurations by parallel hyperplanes. Such a sweep induces an ordering of the points, which are the elements of the underlying oriented matroid. When this picture is polarized, the point configuration gives rise to a hyperplane arrangement, but the collection of sweeping hyperplanes becomes a point that travels in a linear direction (the associated sweep permutation records the order in which the point crosses the hyperplanes). This is the formulation studied by Edelman [[32][41]] and Stanley [[80][42]].

On the other hand, one can consider sweeps of hyperplane arrangements by parallel hyperplanes. Such a sweep induces an ordering of the vertices of the arrangement, which are the cocircuits of the underlying oriented matroid. This is the point of view of the literature on *topological sweepings*of pseudo-hyperplane arrangements and oriented matroids (see, for example, [[17][28], [34][90], [37][91], [42][92], [55][93], p.172]), which concerns mostly the rank 3 case (pseudoline arrangements).

In rank 3, the two notions are strongly related. Indeed, the allowable sequence of a planar point configuration (which is a collection of sweeps in our terminology), can be interpreted as a topological sweep of the dual arrangement of lines. This correspondence exists in rank 3 but completely fails in higher rank, as it only works because in an oriented matroid of rank 3 the lines (flats of rank 2) coincide with the hyperplanes (flats of corank 1).

It is worth to note that in this second setup there exist other approaches to generalize allowable sequences to higher dimensions. For example, the *signotopes*described in [[42][92]] (see also [[39][40]]). These are strongly related to higher Bruhat orders [[66][94]] and single-element extensions of cyclic hyperplane arrangements [[43][95], [88][96]]. However, as these generalizations are meant to model (topological) sweeps of hyperplane arrangements with a (pseudo) hyperplane, they do not cover the spherical complexes that Goodman and Pollack alluded to in [[48][24]] as the natural way to generalize allowable sequences to higher dimensions.

### 1.2 Structure of this Document

This paper gravitates around the concept of sweep oriented matroid, which lies in the intersection of the theories of allowable sequences, valid order arrangements, and the generalized Baues problem for cellular strings. Our hope is to provide a unified reference that reflects all these connections. To this end, we give a broad overview of the topic, as we expect readers with diverse backgrounds and motivations to be interested in different aspects. In particular, most of the sections can be read independently.

Section [2][97] serves as an introduction and focuses in the realizable case. We present polytopal constructions that serve as motivation for the upcoming definitions. Sweep oriented matroids are defined in Sect. [3][55]. In Sect. [4][98] we show how the structural results on allowable sequences from [[17][28]] generalize to sweep oriented matroids of arbitrary rank. Section [5][64] demonstrates that the results in [[32][41], [80][42]] do not require realizability. Section [6][69] depicts sweep oriented matroids as highlighted spheres inside the poset of cellular strings of oriented matroids whose existence was conjectured by [[13][70]]. A presentation in terms of permutations, akin to Goodman and Pollack’s original formulation of allowable sequences [[48][24]], is given in Sect. [7][81] under the name of allowable graphs of permutations.

We end by discussing some open problems and further directions of research in Sect. [8][99].

## 2 Sweeps and Sweep Polytopes

### 2.1 Sweeps of Point Configurations

For any integer *n*, we use \([{n}]\) to denote the set \(\{1, \ldots , n\}\), \(\mathfrak {S}_n\) to denote the set of all permutations of \([{n}]\), and \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) =\left\{ (i,j) \;\big |\; 1\le i < j \le n \right\} \) to denote the set of non-repeating sorted pairs of elements of \([{n}]\). An *ordered partition*of \([{n}]\) is an ordered collection of non-empty disjoint subsets \((I_1, \ldots , I_l)\) whose union is \([{n}]\). Ordered partitions where all parts are singletons are identified with permutations. They are the maximal elements in the *refinement order*: we say that \(J=(J_1, \ldots , J_l)\) refines \(I=(I_1, \ldots , I_k)\), noted \(J\succeq I\), if each \(I_i\) is the union of some consecutive \(J_j\) ’s. In some proofs, it will be more comfortable to think of an ordered partition *I*as the surjection \(p_{I}\) from \([{n}]\) to [*l*] such that \(I_k=p_{I}^{-1}(\{k\})\) for all \(1\le k \le l\). Note that for a permutation \(\sigma \), the ordered partition \(I=(\{\sigma (1)\}, \ldots , \{\sigma (n)\})\) corresponds to the bijection \(p_{I}=\sigma ^{-1}\).

We always consider \({{\mathbb {R}}}^d\) as an Euclidean space, equipped with the usual orthogonal scalar product \(\left\langle \cdot \, , \, \cdot \right\rangle \). A *point configuration*is an ordered sequence \(\varvec{A}=(\varvec{a}_1,\dots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) of points in \({{\mathbb {R}}}^d\) indexed by \([{n}]\). We do not require the points to be distinct, although it will be often convenient to make this simplification. For \(\varvec{u}\in {{\mathbb {R}}}^d\), consider the linear form \(\left\langle \varvec{u} \, , \, \cdot \ \right\rangle :{{\mathbb {R}}}^d\rightarrow {{\mathbb {R}}}\) sending \(\varvec{x}\) to \(\left\langle \varvec{u} \, , \, \varvec{x} \right\rangle \). The *sweep*of \(\varvec{A}\) associated to \(\varvec{u}\) is the ordered partition \(I^{\varvec{u}}=(I_1, \ldots , I_l)\) of \([{n}]\) that verifies \(\left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle =\left\langle \varvec{u} \, , \, \varvec{a}_j \right\rangle \) for all *i*, *j*in a same part \(I_k\), and \(\left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle < \left\langle \varvec{u} \, , \, \varvec{a}_j \right\rangle \) if \(i\in I_r,\, j\in I_s\) with \(r<s\). In particular, \(\left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle \le \left\langle \varvec{u} \, , \, \varvec{a}_j \right\rangle \) if and only if \(p_{{I^{\varvec{u}}}}(i) \le p_{{I^{\varvec{u}} }}(j)\). Note that the partition associated to the linear form \(\varvec{0}\) is the *trivial sweep*\(([{n}])\).

The *poset of sweeps*of \(\varvec{A}\), denoted \(\overline{\Pi }({\varvec{A}})\), is the set of all sweeps ordered by refinement. Its maximal elements are permutations whenever \(\varvec{A}\) does not contain repeated points. We will often assume that this is the case, as we can always identify repeated points. Under this assumption, we denote by \(\Pi ({\varvec{A}})\) \(\subseteq \mathfrak {S}_{n}\) the set of its maximal elements, the *sweep permutations*of \(\varvec{A}\). If there are repeated points, we will still call the maximal elements *sweep permutations*for brevity.

Sweeps induce an equivalence relation on \({{\mathbb {R}}}^d\), where \(\varvec{u}\sim \varvec{v}\) if they give the same sweep. Its equivalence classes are the cells of the polyhedral fan induced by the *sweep hyperplane arrangement*\(\mathcal{S}\mathcal{H}({\varvec{A}})\); the arrangement of the linear hyperplanes \(\left\{ \varvec{u} \in ~{{\mathbb {R}}}^d \;\big |\; \left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle =\left\langle \varvec{u} \, , \, \varvec{a}_j \right\rangle \right\} \) for all \((i, j) \in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). Note that the face poset of \(\mathcal{S}\mathcal{H}({\varvec{A}})\) is isomorphic to the poset \(\overline{\Pi }({\varvec{A}})\), with a bijection that sends each cell \(\mathcal {C}\) of \(\mathcal{S}\mathcal{H}({\varvec{A}})\) to the sweep *I*in \(\overline{\Pi }({\varvec{A}})\) that verifies that the relative interior of \(\mathcal {C}\) is \(\left\{ \varvec{u} \in {{\mathbb {R}}}^d \;\big |\; I^{\varvec{u}}=I \right\} \). In particular, the cones of dimension *d*of \(\mathcal{S}\mathcal{H}({\varvec{A}})\) are indexed by the sweep permutations in \(\Pi ({\varvec{A}})\).

We will see in Sect. [2.3][43] that \(\mathcal{S}\mathcal{H}({\varvec{A}})\) is the normal fan of a polytope: the *sweep polytope*of \(\varvec{A}\), denoted by \(\varvec{SP}({\varvec{A}})\). Thus, the poset of sweeps \(\overline{\Pi }({\varvec{A}})\) enlarged with a top element is isomorphic to the poset opposite to the face lattice of \(\varvec{SP}({\varvec{A}})\), and is in particular a lattice. This provides a natural labeling of the faces of \(\varvec{SP}({\varvec{A}})\) by sweeps. In particular, the vertices of \(\varvec{SP}({\varvec{A}})\) are labeled by the sweep permutations in \(\Pi ({\varvec{A}})\).

The identification of sweeps with faces of \(\varvec{SP}({\varvec{A}})\) reflects the inherent topological structure of the poset of sweeps. This can be made precise in terms of its order complex. The *order complex*\(\Delta \left( P\right) \) of a poset *P*is the simplicial complex whose simplices are the chains of *P*, see [[14][100]] or [[17][28], Sec. 4.7] for some background. In our case, the order complex of \(\overline{\Pi }({\varvec{A}})\smallsetminus ([{n}])\), the poset of sweeps without the trivial sweep, is just the barycentric subdivision of the boundary of \(\varvec{SP}({\varvec{A}})\). We will implicitly identify \(\overline{\Pi }({\varvec{A}})\) with \(\Delta \left( {\overline{\Pi }({\varvec{A}})\smallsetminus ([{n}])}\right) \) whenever we make topological statements about posets of sweeps.

### 2.2 Examples

Before providing constructions for this polytope, we will present two particular examples.

#### 2.2.1 The Simplex and the Permutahedron

If \(\varvec{A}_n\) is the set of vertices of a standard \((n-1)\) -simplex \(\varvec{\triangle }_{n-1}\), i.e. the points \(\varvec{a}_i\) are the canonical basis vectors \(\varvec{e}_i\) in \({{\mathbb {R}}}^n\), then \(\mathcal{S}\mathcal{H}({\varvec{A}_n})\) is the *braid arrangement*\(\mathcal {B}_{n}\) consisting of the hyperplanes \(\left\{ \varvec{u} \;\big |\; \varvec{u}_j-\varvec{u}_i=0 \right\} \) for all \(1\le i < j \le n\), the set of sweep permutations is the whole symmetric group \(\Pi ({\varvec{A}_n})=\mathfrak {S}_{n}\), and the poset of sweeps \(\overline{\Pi }({\varvec{A}_n})\) is the poset of all ordered partitions of \([{n}]\). Likewise for any set \(\varvec{A}\) of affinely independent points, up to affine transformation of the braid arrangement.

The braid arrangement \(\mathcal {B}_{n}\) is the normal fan of a polytope, the *n*-*permutahedron*\(\varvec{P}_{n}\). It is usually defined as the convex hull of the points \((\sigma (1), \ldots , \sigma (n))\in {{\mathbb {R}}}^n\) for all \(\sigma \in \mathfrak {S}_{n}\) (see [[89][21], Ex 0.10] or [[17][28], Ex. 2.2.5]). Thus, it lives in the \((n-1)\) -dimensional affine subspace of the sum of coordinates constant equal to \(\tfrac{n(n+1)}{2}\). It can be described as the zonotope:

$$\begin{aligned} \varvec{P}_{n}= \tfrac{n+1}{2} \varvec{1}_{n}+ \sum _{1 \le i < j \le n} \left[ -\frac{\varvec{e}_i-\varvec{e}_j}{2}, \frac{\varvec{e}_i-\varvec{e}_j}{2}\right] , \end{aligned}$$

(1)

where \(\varvec{1}_{n}=\sum _{i=1}^n \varvec{e}_i\) is the all-ones vector and \([\varvec{p},\varvec{q}]\subset {{\mathbb {R}}}^d\) denotes the segment between the points \(\varvec{p}\) and \(\varvec{q}\), see [[89][21], Ex. 7.15].

**Fig. 2**

[image: Fig. 2]

[Full size image][101]

\(\varvec{A}_3\), its sweep hyperplane arrangement \(\mathcal{S}\mathcal{H}({\varvec{A}_3})=\mathcal {B}_{3}\) (modulo linearity), and its sweep polytope \(\varvec{SP}({{\varvec{A}_3}})=\varvec{P}_{3}'\), the 3-permutahedron, where each vertex is labeled by the corresponding sweep permutation of \(\varvec{A}_3\)

**Fig. 3**

[image: Fig. 3]

[Full size image][102]

\(\varvec{A}_4\) and its sweep polytope \(\varvec{SP}({{\varvec{A}_4}})=\varvec{P}_{4}'\), the 4-permutahedron

The sweep polytope \(\varvec{SP}({\varvec{A}})\) associated to the standard simplex is the translation of \(\varvec{P}_{n}\) centered at the origin. We will denote this translated permutahedron by \(\varvec{P}_{n}'\)

$$\begin{aligned} \varvec{P}_{n}'=\sum _{1 \le i < j \le n} \left[ -\frac{\varvec{e}_i-\varvec{e}_j}{2}, \frac{\varvec{e}_i-\varvec{e}_j}{2}\right] \end{aligned}$$

(2)

to distinguish it from the standard realization. See Figs. [2][103] and [3][104] for the cases \(n=3,4\).

#### 2.2.2 The Cross-Polytope and the Permutahedron of type *B*

Let \(\varvec{A}[B]_n\) be the set of vertices of the cross-polytope \(\varvec{\lozenge }_{n}\), that is, the set of standard basis vectors of \({{\mathbb {R}}}^n\) and their opposites. It is convenient to index the points by \([\pm n]=\{-n,\dots ,-1,1,\dots ,n\}\): \(\varvec{B}_n=\{ \varvec{b}_{-n}=-\varvec{e}_n, \ldots , \varvec{b}_{- 1}=-\varvec{e}_1, \varvec{b}_1=\varvec{e}_1, \ldots , \varvec{b}_n=\varvec{e}_n\}\). Then the sweep permutations of \(\varvec{B}_n\) are the centrally symmetric permutations of \(\mathfrak {S}_{{[\pm n]}}\), which satisfy \(\sigma (-i)=-\sigma (i)\) for all \(i\in [\pm n]\). By symmetry, the first half determines the whole permutation. This way, they can be represented by signed permutations of \([{n}]\), where \(-k\) is denoted by \(\overline{k}\). We use this notation in Figs. [4][105] and [5][106].

**Fig. 4**

[image: Fig. 4]

[Full size image][107]

\(\varvec{B}_2\), its sweep hyperplane arrangement \(\mathcal{S}\mathcal{H}({{\varvec{B}_2}})\), and its sweep polytope \(\varvec{SP}({{\varvec{B}_2}})\)

**Fig. 5**

[image: Fig. 5]

[Full size image][108]

\(\varvec{B}_3\) and its sweep polytope \(\varvec{SP}({{\varvec{B}_3}})\), the 3-permutahedron of type *B*

They are the elements of the Coxeter group of type *B*, also called hyperoctahedral group. See [[8][109], Section 8.1] for more details on the combinatorics of this group. The sweep hyperplane arrangement \(\mathcal{S}\mathcal{H}({{\varvec{B}_n}})\) is the Coxeter arrangement of type *B*, which consists of the hyperplanes \(\left\{ \varvec{u}\in {{\mathbb {R}}}^n \;\big |\; \varvec{u}_i\pm \varvec{u}_j=0 \right\} \) for all \(1\le i < j\le n\) and \(\left\{ \varvec{u}\in {{\mathbb {R}}}^n \;\big |\; \varvec{u}_i=0 \right\} \) for all \(1\le i \le n\). The sweeps are the centrally symmetric ordered partitions of \([\pm n]\). This complex is known as the Coxeter complex of type *B*, see [[17][28], Sec. 2.3(c)]. See Fig. [4][105] for an example.

The associated sweep polytope is the Coxeter permutahedron of type *B*, also known as the Coxeterhedron of type *B*[[74][110]]. See Figs. [4][105] and [5][106] for pictures in dimensions 2 and 3.

#### 2.2.3 Sweeping with Polynomial Functions

Sweep polytopes can also be used to model sweeps of a point configuration \(\varvec{A}=(\varvec{a}_1, \ldots , \varvec{a}_n) \in {{\mathbb {R}}}^{d\times [{n}]}\) by polynomial functions \(p\in {{\mathbb {R}}}[x_1, \ldots , x_d]\) of bounded degree. The *polynomial sweep*of \(\varvec{A}\) associated to \(p\) is the ordered partition of \([{n}]\) induced by the ordered level sets of \(p\) on \(\varvec{A}\).

Let \(\mathcal {M}\) be the set of monomials of degree at most *D*on variables \(x_1,\dots ,x_d\). There are \(|\mathcal {M}|=\left( {\begin{array}{c}D+d\\ D\end{array}}\right) \) elements in \(\mathcal {M}\). For a point \(\varvec{v}=(v_1, \ldots , v_d) \in {{\mathbb {R}}}^d\) and a monomial \(M\in \mathcal {M}\), denote by \(M(\varvec{v}) \in {{\mathbb {R}}}\) the evaluation of *M*on the values \(x_1=v_1, \ldots , x_d=v_d\). The *Veronese mapping*is defined by the map

$$\begin{aligned} \chi : {\left\{ \begin{array}{ll} {{\mathbb {R}}}^d &{}\rightarrow {{\mathbb {R}}}^{\mathcal {M}} \\ \varvec{v} &{}\mapsto \left( M(\varvec{v}) \right) _{M\in \mathcal {M}}. \end{array}\right. } \end{aligned}$$

Then, the polynomial sweep of \(\varvec{A}\) induced by the polynomial \(p=\sum _{M\in \mathcal {M}} c_M M\) exactly corresponds to the sweep of \(\chi (\varvec{A})\) induced by the linear functional \(\left\langle \varvec{c} \, , \, \cdot \right\rangle \) for \(\varvec{c}=(c_M)_{M\in \mathcal {M}} \in {{\mathbb {R}}}^{\mathcal {M}}\). In particular, the poset of sweeps of \(\chi (\varvec{A})\) coincides with the poset of polynomial sweeps of \(\varvec{A}\) induced by polynomials of degre at most *D*. Note that if \(d=1\), the image \(\chi (\varvec{A})\) is a standard cyclic polytope of dimension *D*with *n*vertices.

Variants of the Veronese mapping can be used for particular families of polynomial sweeps. For example, the embedding

$$\begin{aligned} (v_1,\dots ,v_d)\mapsto (v_1,\dots ,v_d, v_1^2+\cdots +v_d^2) \end{aligned}$$

onto the paraboloid models sweeps by families of concentric spheres.

### 2.3 Constructions for Sweep Polytopes

In what follows, we describe three approaches to construct the sweep polytope \(\varvec{SP}({\varvec{A}})\). Recall that \(\varvec{SP}({\varvec{A}})\) is a polytope whose normal fan coincides with the sweep hyperplane arrangement \(\mathcal{S}\mathcal{H}({\varvec{A}})\), and whose face poset is opposite to the poset of sweeps \(\overline{\Pi }({\varvec{A}})\).

#### 2.3.1 As a Zonotope

The most direct realization is as the Minkowski sum of the segments with directions the differences between the points of the configuration, which is (a translation of) the presentation of sweep polytopes given in [[50][44]] (under the name of *shellotopes*).

### Definition 2.1

The *sweep polytope*\(\varvec{SP}({\varvec{A}})\) associated to the configuration \(\varvec{A}=(\varvec{a}_1,\dots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) is the zonotope:

$$\begin{aligned} \varvec{SP}({\varvec{A}})= \sum _{1\le i < j \le n}\left[ -\frac{\varvec{a}_i-\varvec{a}_j}{2},\frac{\varvec{a}_i-\varvec{a}_j}{2}\right] \subset {{\mathbb {R}}}^d. \end{aligned}$$

The normal fan of a zonotope is the arrangement of the hyperplanes orthogonal to its generators, see for example [[87][111], Sec. 2] and [[89][21], Thm. 7.16]. Applied to sweep polytopes, we directly get:

### Proposition 2.2

The normal fan of \(\varvec{SP}({\varvec{A}})\) is the hyperplane arrangement \(\mathcal{S}\mathcal{H}({\varvec{A}})\).

#### 2.3.2 As a Projection of the Permutahedron

Our second incarnation is as a projection of the (centered) permutahedron \(\varvec{P}_{n}'\). For a configuration \(\varvec{A}\) of *n*points \(\varvec{a}_1, \ldots , \varvec{a}_n\) in \({{\mathbb {R}}}^d\), let \({M_{\varvec{A}}}\) be the linear map

$$\begin{aligned} {M_{\varvec{A}}}: {{\mathbb {R}}}^n&\rightarrow {{\mathbb {R}}}^d \\ \varvec{e}_i&\mapsto \varvec{a}_i.\nonumber \end{aligned}$$

(3)

Then it follows from Definition [2.1][112] and the description of \(\varvec{P}_{n}'\) in ( [2][113]) that:

### Proposition 2.3

\(\varvec{SP}({\varvec{A}})= {M_{\varvec{A}}}(\varvec{P}_{n}').\)

Conversely, all affine images of permutahedra are sweep polytopes, up to translation. This provides a combinatorial interpretation, in terms of sweeps, of the face lattice of any affine projection of a permutahedron (a *permutahedral shadow*).

### Corollary 2.4

Let \(M_{}:{{\mathbb {R}}}^n\rightarrow {{\mathbb {R}}}^d\) be a linear map, then \(M_{}(\varvec{P}_{n}')\) is the sweep polytope of the point configuration \(M_{}(\varvec{e}_1),\dots ,M_{}(\varvec{e}_n)\).

Note that, given a linear map from \(\varvec{P}_{n}'\) to \({{\mathbb {R}}}^d\), there is a *d*-dimensional family of ways to extend it to a linear map from \({{\mathbb {R}}}^n\) to \({{\mathbb {R}}}^d\). This amounts to the fact that point configurations related by a translation give rise to the same sweep polytope.

### Remark 2.5

Proposition [2.3][114] follows from the fact that Minkowski sums and linear projections commute. This can be exploited also with other decompositions of the permutahedron. For example, the permutahedron \(\varvec{P}_{n}\) can be written as the Minkowski sum of the hypersimplices \(\varvec{\triangle }_{n,k}=\left\{ \varvec{x}\in [0,1]^n \;\big |\; \sum \varvec{x}_i=k \right\} \) with *k*ranging from 1 to \(n-1\) (see for example [[69][115]]). Therefore, any sweep polytope can be expressed as a Minkowski sum of projections of hypersimplices. Projections of hypersimplices are studied under the name of *k*-*set polytopes*[[6][51], [38][52]], which (up to homothety) can be described as the convex hull of the barycenters of all *k*-subsets of \(\varvec{A}\), see [[67][116]]. The sweep polytope of \(\varvec{A}\) is thus the Minkowski sum of its *k*-set polytopes, up to translation and homothety. In particular, because \({{\,\textrm{conv}\,}}(\varvec{A})={M_{\varvec{A}}}(\varvec{\triangle }_{n,1})\), this shows that \({{\,\textrm{conv}\,}}(\varvec{A})\) is a Minkowski summand of \(\varvec{SP}({\varvec{A}})\). See Fig. [6][117] for an example. Another point of view on this Minkowski decomposition will be discussed in Remark [2.9][53].

**Fig. 6**

[image: Fig. 6]

[Full size image][118]

The sweep polytope \(\varvec{SP}({{\varvec{B}_3}})=\varvec{P}_{3}'\) as a Minkowski sum of the *k*-set polytopes of \(\varvec{B}_3\) for \(k=1,\dots ,5\)

#### 2.3.3 As a Monotone Path Polytope

Fiber polytopes are certain polytopes associated to polytope projections. This construction was introduced by Billera and Sturmfels in [[23][48]], generalizing the theory of secondary polytopes in a unified way that encompasses concepts such as monotone path polytopes, zonotopal tiling polytopes and secondary polytopes. We refer to [[89][21], Lec. 9] and [[30][119], Sec. 9.1] for gentle introductions to the topic.

Consider polytopes \(\varvec{P}\) and \(\varvec{Q}\) related by a linear surjection \(\pi : \varvec{P} \rightarrow \varvec{Q}\). The fibers of \(\pi \) over \(\varvec{Q}\) form a *polytope bundle*\(\varvec{y}\in \varvec{Q}\mapsto \pi ^{-1}(\{\varvec{y}\})\) whose *Minkowski integral*, after some normalization, is the *fiber polytope*\(\Sigma \left( \varvec{P},\pi \right) \):

$$\begin{aligned} \Sigma \left( \varvec{P},\pi \right) = \frac{1}{{{\,\textrm{vol}\,}}(\varvec{Q})}\int _{\varvec{Q}}\pi ^{-1}(\{\varvec{y}\}) d\varvec{y}. \end{aligned}$$

Fiber polytopes can also be described as a finite Minkowski sum. Namely,

$$\begin{aligned} \Sigma \left( \varvec{P},\pi \right) = \frac{1}{{{\,\textrm{vol}\,}}(\varvec{Q})}\sum _{\varvec{C} \in \Gamma (\varvec{P}, \pi )} {{\,\textrm{vol}\,}}(\varvec{C})\ \pi ^{-1}(\{\varvec{b}_{\varvec{C}}\}), \end{aligned}$$

where \(\Gamma (\varvec{P}, \pi )\) is the set of *chambers*: the subsets of \(\varvec{Q}\) of the form

$$\begin{aligned} \varvec{C}_{\varvec{y}}~=~\bigcap \limits _{\underset{\varvec{y} \in \pi (\varvec{F})}{\varvec{F}\text { face of }\varvec{P}}} \pi (\varvec{F}) \end{aligned}$$

for \(\varvec{y}\in \varvec{Q}\); and \(\varvec{b}_{\varvec{C}}\) is the barycenter of the chamber \(\varvec{C}\).

Note that \(\Sigma \left( \varvec{P},\pi \right) \) lies in the fiber over the barycenter of \(\varvec{Q}\): \(\Sigma \left( \varvec{P},\pi \right) \subset \pi ^{-1}\left( \frac{1}{{{\,\textrm{vol}\,}}(\varvec{Q})}\int _{\varvec{Q}}\varvec{y}\ d\varvec{y} \right) \).

An important feature of fiber polytopes is that their face lattice is isomorphic to the poset of \(\pi \) -coherent subdivisions of *Q*(ordered by refinement), which are subdivisions of \(\varvec{Q}\) composed of images of faces of \(\varvec{P}\) that are *coherently induced*by the map \(\pi \). We refer to the aforementioned sources for the details in the definitions. We are particularly interested in a special case of fiber polytopes: monotone path polytopes. They will give a new interpretation of sweep polytopes and provide motivation for the definition of pseudo-sweeps, that will be further explored in Sect. [6][69].

If \(\varvec{Q}\) is one dimensional and \(\varvec{P}\subset {{\mathbb {R}}}^n\), then \(\pi :\varvec{P}\rightarrow \varvec{Q}\) is a linear form defined by a vector \(\varvec{u}\in {{\mathbb {R}}}^n\) via \(\pi (\varvec{x})=\left\langle \varvec{u} \, , \, \varvec{x} \right\rangle \). For simplicity, assume that \(\pi \) is generic in the sense that it is not constant along any edge of \(\varvec{P}\), and let \(\varvec{p}_m\) and \(\varvec{p}_M\) be the minimal and maximal vertices of \(\varvec{P}\) with respect to \(\pi \). A \(\pi \) -*monotone path*is a path from \(\varvec{p}_m\) to \(\varvec{p}_M\) composed of edges of \(\varvec{P}\) along which \(\pi \) is always increasing. One way to obtain \(\pi \) -monotone paths is to consider some generic vector \(\varvec{w}\) orthogonal to \(\varvec{u}\) and consider the sequence of vertices of \(\varvec{P}\) that are extreme in the direction \(\varvec{w}+\lambda \varvec{u}\) as \(\lambda \) ranges from \(-\infty \) to \(\infty \) (see Fig. [7][120]). These paths induce the finest \(\pi \) -coherent subdivisions of \(\varvec{Q}\), and are known as *parametric simplex paths*in linear programming, where they play an important role as they are the paths followed by the shadow-vertex simplex method [[20][121], [49][122]].

More generally, a *cellular string*on \(\varvec{P}\) with respect to \(\pi \) is a sequence of faces \(\varvec{F}_1,\dots ,\varvec{F}_k\) of \(\varvec{P}\) of dimension at least 1 such that \(\varvec{p}_m\in \varvec{F}_1\), \(\varvec{p}_M\in \varvec{F}_k\), and every two adjacent faces \(\varvec{F}_i,\varvec{F}_{i+1}\) meet at a vertex \(\varvec{p}_i\) such that \(\pi (\varvec{x})\le \pi (\varvec{p}_i)\le \pi (\varvec{y})\) for each \(\varvec{x}\in \varvec{F}_i\) and \(\varvec{y}\in \varvec{F}_{i+1}\). Such a cellular string is \(\pi \) -coherent if there is some (not-necessarily generic) vector \(\varvec{w}\) orthogonal to \(\varvec{u}\) such that these are the maximal faces of \(\varvec{P}\) maximized in a direction of the form \(\varvec{w}+\lambda \varvec{u}\). The fiber polytope \(\Sigma \left( \varvec{P},\pi \right) \) is called the *monotone path polytope*of \(\varvec{P}\) and \(\pi \). Its vertices are in one-to-one correspondence with the parametric \(\pi \) -monotone paths of \(\varvec{P}\), and its faces are in correspondence with the \(\pi \) -coherent cellular strings.

### Example 2.6

([[23][48], Ex. 5.4], see also [[89][21], Ex. 9.8]) Let \(\varvec{\square }_{n}= [-1, 1]^n\) be the *n*-dimensional \(\pm 1\) -hypercube, and let \(s: {{\mathbb {R}}}^n\rightarrow {{\mathbb {R}}}\) be the linear form that sums the coordinates, i.e. the form \(s=\left\langle \varvec{1}_{n} \, , \, \cdot \ \right\rangle \) induced by the all-ones vector. Then the fiber polytope \(\Sigma \left( \varvec{\square }_{n},s\right) =\frac{2}{n} \varvec{P}_{n}'\) is (homothetic to) the (centered) permutahedron \(\varvec{P}_{n}'\), and \(\Sigma \left( \frac{n}{2}\varvec{\square }_{n},s\right) =\varvec{P}_{n}'\).

**Fig. 7**

[image: Fig. 7]

[Full size image][123]

The zonotope \(\varvec{Z}({\bar{\varvec{B}_2}})\). Three fibers of the height function \(h\) are highlighted, representing a copy of the convex hull of \(\varvec{B}_2\), and of its 2-set and 3-set polytopes. The lower (red) path represents the coherent monotone path associated to the permutation \(({\bar{2}}, {\bar{1}}, 1, 2)\) (which can be read off the directions of the steps in the path). The upper (blue) path is a monotone path that is not coherent. It is associated to the permutation \(({\bar{1}},2,1,{\bar{2}})\), which is not a sweep permutation, but a pseudo-sweep permutation, see Sect. [6][69]

The following central property of fiber polytopes will be key for our purposes.

### Lemma 2.7

([[23][48], Lem. 2.3]) Let \({{\mathbb {R}}}^n\xrightarrow {\theta }{{\mathbb {R}}}^m\xrightarrow {\pi }{{\mathbb {R}}}^d\) be linear maps, and \(\varvec{P}\subset {{\mathbb {R}}}^n\) a polytope. Then \(\Sigma \left( \theta (\varvec{P}),\pi \right) =\theta (\Sigma \left( \varvec{P},\pi \circ \theta \right) )\).

We need some extra notation. Let \(\varvec{A}=(\varvec{a}_1,\dots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) be a point configuration, and consider its *homogenization*\(\bar{\varvec{A}}=(\bar{\varvec{a}}_1,\dots ,\bar{\varvec{a}}_n)\in {{\mathbb {R}}}^{(d+1)\times [{n}]}\) consisting of the vectors \(\bar{\varvec{a}}_i=(\varvec{a}_i,1)\). We define the zonotope \(\varvec{Z}({\bar{\varvec{A}}})\) associated to \(\varvec{A}\) as the following Minkowski sum of centrally symmetric segments:

$$\begin{aligned} \varvec{Z}({\bar{\varvec{A}}})= \sum _{i=1}^n [-\bar{\varvec{a}}_i, \bar{\varvec{a}}_i]. \end{aligned}$$

Let \( h :{{\mathbb {R}}}^{d+1} \rightarrow {{\mathbb {R}}}\) denote the map that returns the last coordinate of a point, that we call its *height*.

This gives us another point of view on sweep polytopes.

### Proposition 2.8

For any point configuration \(\varvec{A}\) we have

$$\begin{aligned} \Sigma \left( \tfrac{n}{2}\varvec{Z}({\bar{\varvec{A}}}),h\right) =\varvec{SP}({\varvec{A}})\times \{0\}, \end{aligned}$$

and hence \(\varvec{SP}({\varvec{A}})\) is affinely isomorphic to the monotone path polytope \(\Sigma \left( \varvec{Z}({\bar{\varvec{A}}}),h\right) \).

### Proof

The projection \(M_{\bar{\varvec{A}}}:\mathbb {R}^n \rightarrow \mathbb {R}^{d+1}\) that maps \(\varvec{e}_i\) to \(\bar{\varvec{a}}_i=(\varvec{a}_i, 1)\) is such that \(\varvec{Z}({\bar{\varvec{A}}})=M_{\bar{\varvec{A}}}(\varvec{\square }_{n})\) and \(s=h\circ M_{\bar{\varvec{A}}}\), where *s*is the linear form that sums the coordinates defined in Example [2.6][124]. Hence, by Lemma [2.7][125] and Example [2.6][124] we have \(\Sigma \left( \varvec{Z}({\bar{\varvec{A}}}),h\right) =M_{\bar{\varvec{A}}}(\Sigma \left( \varvec{\square }_{n},s\right) )=M_{\bar{\varvec{A}}}(\frac{2}{n} \varvec{P}_{n}')\). Now, \(\varvec{P}_{n}'\) lies in \(s^{-1}\left( \frac{1}{{{\,\textrm{vol}\,}}(\varvec{\square }_{n})}\int _{\varvec{\square }_{n}} {\varvec{y}} d\varvec{y}\right) =s^{-1}(\varvec{0}_{n})\), and thus \(M_{\bar{\varvec{A}}}(\frac{2}{n} \varvec{P}_{n}')\) lies in the kernel of \(h\), which means that \(\Sigma \left( \varvec{Z}({\bar{\varvec{A}}}),h\right) =\frac{2}{n}{M_{\varvec{A}}}(\varvec{P}_{n}')\times \{0\}\). Finally, by Proposition [2.3][114], we have \({M_{\varvec{A}}}(\varvec{P}_{n}') = \varvec{SP}({\varvec{A}})\), and therefore \(\Sigma \left( \varvec{Z}({\bar{\varvec{A}}}),h\right) =\frac{2}{n}\varvec{SP}({\varvec{A}})\times \{0\}\). \(\square \)

### Remark 2.9

If we intersect \(\varvec{Z}({\bar{\varvec{A}}})\) with the hyperplane of height equal to \(-n+2\), we obtain

$$\begin{aligned} {{\,\textrm{conv}\,}}(-\sum _{i=1}^n \bar{\varvec{a}_i} +2\bar{\varvec{a}_j}, j\in [n])={{\,\textrm{conv}\,}}(-\sum _{i=1}^n {\varvec{a}_i} + 2\varvec{A})\times \{-n+2\}, \end{aligned}$$

which is an embedding of a dilation of the convex hull of \(\varvec{A}\) in \({{\mathbb {R}}}^{d+1}\). Similarly, for any \(k\in [n]\) the slice at height \(-n+2k\) is an embedding of a dilation of the projection of the hypersimplex \(\varvec{\triangle }_{n,k}\) under the map \(M_{\varvec{A}}\). This is the *k*-set polytope of \(\varvec{A}\), see Remark [2.5][126]. The fiber polytope realization reflects the decomposition of the sweep polytope as a sum of *k*-set polytopes.

Conversely, monotone path polytopes of zonotopes for nondegenerate functionals are sweep polytopes, up to normal equivalence. Two polytopes are called *normally equivalent*if they have the same normal fan, and normal equivalence obviously implies combinatorial equivalence.

### Proposition 2.10

Let \(\varvec{Z}\subset {{\mathbb {R}}}^d\) be a zonotope, \(\pi :{{\mathbb {R}}}^d\rightarrow {{\mathbb {R}}}\) a linear map, and \(\varvec{Z}^\pi \) the face of \(\varvec{Z}\) minimizing \(\pi \). Then the monotone path polytope \(\Sigma \left( {\varvec{Z}},\pi \right) \) is normally equivalent to the Minkowski sum of \(\varvec{Z}^\pi \) with the sweep polytope \(\varvec{SP}({\varvec{A}})\), where \(\varvec{A}\) consists of the points \( \frac{1}{\pi (\varvec{z}_i)} \varvec{z}_i\) for the generators \(\varvec{z}_i\) of \(\varvec{Z}\) such that \(\pi (\varvec{z}_i)\ne 0\).

### Proof

Let \(\varvec{c}, \varvec{z}_1 \ldots , \varvec{z}_m\in {{\mathbb {R}}}^d\) be such that

$$\begin{aligned} \varvec{Z}= \varvec{c} + \sum _{i=1}^m \left[ -\varvec{z}_i,\varvec{z}_i\right] \subset {{\mathbb {R}}}^d. \end{aligned}$$

Then \(\varvec{Z}\) is normally equivalent to any zonotope \(\varvec{Z}'= \varvec{c}' + \sum _{i=1}^m \left[ -\lambda _i \varvec{z}_i,\lambda _i \varvec{z}_i\right] \), where \(\varvec{c}'\) is a vector in \({{\mathbb {R}}}^d\) and the \(\lambda _i\) are non-zero scalars.

Up to relabeling the \(\varvec{z}_i\), one can suppose that \(\left\{ i \;\big |\; \pi (\varvec{z}_i)=0 \right\} =\{n+1, \ldots , m\}\) for a certain \(n \in \{0, \ldots , m\}\). Let \(\varvec{Z}_1\) and \(\varvec{Z}_2\) be the zonotopes:

$$\begin{aligned} \varvec{Z}_1&= \sum _{i=1}^n \left[ -\frac{1}{\pi (\varvec{z}_i)} \varvec{z}_i, \frac{1}{\pi (\varvec{z}_i)} \varvec{z}_i\right] ,&\varvec{Z}_2&= \sum _{i=n+1}^m \left[ -\varvec{z}_i ,\varvec{z}_i\right] . \end{aligned}$$

Note that the face \(\varvec{Z}^{\pi }\) is a translation of \(\varvec{Z}_2\).

Since \(\varvec{Z}\) is normally equivalent to the Minkowski sum \(\varvec{Z}_1 + \varvec{Z}_2\), we have that its monotone path polytope \(\Sigma \left( {\varvec{Z}},\pi \right) \) is normally equivalent to the monotone path polytope \(\Sigma \left( {\varvec{Z}_1 + \varvec{Z}_2},\pi \right) \) by [[63][127], Cor. 4.4].

Moreover, \(\Sigma \left( {\varvec{Z}_1 + \varvec{Z}_2},\pi \right) =\Sigma \left( {\varvec{Z}_1},\pi \right) +\varvec{Z}_2\) because \(\pi (\varvec{Z}_2)=\{0\}\), thus \((\varvec{Z}_1 + \varvec{Z}_2)\cap \pi ^{-1}(\{y\}) = \varvec{Z}_1 \cap \pi ^{-1}(\{y\}) + \varvec{Z}_2\) for any \(y\in {{\mathbb {R}}}\). If we denote the configuration of points \(\varvec{a}_1 = \frac{1}{\pi (\varvec{z}_1)}\varvec{z}_1, \ldots , \varvec{a}_n = \frac{1}{\pi (\varvec{z}_n)} \varvec{z}_n\) in \({{\mathbb {R}}}^d\) by \(\varvec{A}\), we have exactly \(s=\pi \circ {M_{\varvec{A}}}\) and \(\varvec{Z}_1={M_{\varvec{A}}}(\varvec{\square }_{n})\), with the same notations as in Proposition [2.3][114] and Example [2.6][124]. Hence, Lemma [2.7][125] and Example [2.6][124] give \(\Sigma \left( {\varvec{Z}_1},\pi \right) = {M_{\varvec{A}}}(\Sigma \left( \varvec{\square }_{n},s\right) )={M_{\varvec{A}}}(\frac{2}{n}\varvec{P}_{n}') = \frac{2}{n}\varvec{SP}({\varvec{A}})\).

Hence \(\Sigma \left( {\varvec{Z}},\pi \right) \) is normally equivalent to the Minkowski sum \(\varvec{SP}({\varvec{A}})+ \varvec{Z}^{\pi }\). \(\square \)

There is an alternative (but strongly related) way to construct sweep polytopes as fiber polytopes. It is not directly used in the sequel, but we present it in Appendix [A][128] for completeness.

## 3 Sweep Oriented Matroids

The goal of this section is to provide a purely combinatorial definition of posets of sweeps generalizing allowable sequences to higher dimensions. Since already in the plane not all allowable sequences arise from point configurations, it is clear that our definition has to go beyond the realizable case. We will do it in terms of oriented matroids, which do have enough expressive power to completely describe allowable sequences. However, to motivate our definition, we will start by discussing some oriented matroids associated to point configurations, inspired by [[17][28], Sects. 1.10 & 6.4]. While we will introduce the basic definitions in oriented matroid theory, we refer the reader not familiar with the topic to the introduction in [[89][21], Lec. 6], and to the classical book [[17][28]] for a comprehensive source.

### 3.1 Basic Notions and Notation

There are several cryptomorphic approaches to oriented matroids. We will use the presentation in terms of the *covector axioms*, which describe oriented matroids in terms of collections of sign-vectors \( \mathcal {M}\subseteq \{+,-,0\}^E\), called *covectors*, labeled by a finite ground set *E*.

For \(X\in \mathcal {M}\) and \(e\in E\), \(X_e\) denotes the value of *X*at the coordinate *e*. The *opposite*\(-X\) of \(X\in \mathcal {M}\) is the sign-vector obtained by switching \(+\) and - in *X*; that is, \((-X)_e=-(X_e)\). For \(X,Y \in \mathcal {M}\), the *composition*of *X*and *Y*is the sign-vector \(X\circ Y \in \{ +, -,0\}^E\) such that \((X\circ Y)_e=X_e\) if \(X_e\ne 0\); and \((X\circ Y)_e=Y_e\) otherwise. The *separation set*of *X*and *Y*, denoted \(S({X},{Y})\), is the set of elements \(e\in E\) such that \((X_e, Y_e) \in \{(+,-),(-,+)\}\).

### Definition 3.1

(cf. [[17][28], Def. 4.1.1]) A collection of sign-vectors \(\mathcal {M}\subseteq \{+,-,0\}^E\) is the set of covectors of an *oriented matroid*if it satisfies the following axioms:

1. (V0)

\(\varvec{0}\in \mathcal {M}\),

2. (V1)

\(X\in \mathcal {M}\) implies \(-X\in \mathcal {M}\),

3. (V2)

\(X,Y \in \mathcal {M}\) implies \(X\circ Y \in \mathcal {M}\),

4. (V3)

if \(X,Y\in \mathcal {M}\) and \(e\in S({X},{Y})\) then there exists \(Z \in \mathcal {M}\) such that \(Z_e=0\) and \(Z_f=(X\circ Y)_f\) for all \(f\notin S(X,Y)\).

The set of covectors of an oriented matroid, with the product partial order induced by \(0\prec +,-\) componentwise, forms a poset. It has the structure of a lattice, called the *big face lattice*of the oriented matroid, if a top element \(\hat{\varvec{1}}\) is adjoined. The *rank*of the oriented matroid is the length of the maximal chains in the poset of covectors. The minimal non-zero covectors are called *cocircuits*, and they determine the oriented matroid as every non-zero covector is a composition of cocircuits. The maximal covectors for this partial order are called the *topes*of the oriented matroid. They also determine the oriented matroid, as *X*is a covector of \(\mathcal {M}\) if and only if \(X\circ T\) is a tope for every tope *T*. In fact, the *tope-graph*of \(\mathcal {M}\), whose vertices are the topes and whose edges are given by the covectors covered by exactly two topes, already determines the oriented matroid up to FL-isomorphism, see [[11][129], Theorem 6.14] and [[17][28], Theorem 4.2.14].

There are several standard notions of oriented matroid isomorphism. By *FL-isomorphism*, we mean the coarsest, induced by isomorphism of the big face lattices. FL-isomorphism, called just isomorphism in [[40][130]], is the equivalence relation induced by reorientation, relabeling, and introduction/deletion of loops and parallel elements.

To understand the concepts used in the definition of FL-isomorphism, we need some extra notation. For \(X\in \{+,-,0\}^E\) and \(F\subseteq E\), we denote by \(_{-F}{X}\) the signed vector *Z*such that: \(Z_f = -X_f\) for \(f\in F\) and \(Z_e = X_e\) for \(e\in E{\setminus } F\), which we call the *reorientation*of *X*on *F*. If \(\mathcal {M}\) is an oriented matroid on the ground set *E*, its *reorientation*on *F*is the oriented matroid \(_{-F}{\mathcal {M}}\) with covectors \(_{-F}{X}\) for \(X\in \mathcal {M}\). The *support*of a sign-vector *X*is \(\underline{X}=\left\{ e\in E \;\big |\; X_e\ne 0 \right\} \). A *loop*is an element \(e\in E\) that does not belong to the support of any covector. Two elements \(e,f\in E\) are said to be *parallel*if \(X_f = X_e\) for all \(X\in \mathcal {M}\) or \(X_f=-X_e\) for all \(X \in \mathcal {M}\). This defines an equivalence relation on *E*, whose equivalence classes are called *parallelism classes*. The parallelism class of \(e\in E\) is denoted \(\overline{\overline{e}}\). An oriented matroid is called *simple*if it does not contain loops or distinct parallel elements.

For \(X\in \{+,-,0\}^E\) and \(F\subseteq E\), *the restriction of X to F*, denoted \({ \hspace{0.0pt}X \big |_{F} }\) is the covector \(Z \in \{+,-,0\}^F\) such that \(Z_f=X_f\) for all \(f\in F\). If \(\mathcal {M}\) is an oriented matroid on the ground set *E*, the set \(\left\{ { \hspace{0.0pt}X \big |_{F} } \;\big |\; X\in \mathcal {M} \right\} \) forms an oriented matroid, denoted \({ \hspace{0.0pt}\mathcal {M} \big |_{F} }\) and called the *restriction of*\(\mathcal {M}\)*to**F*. The set \(\left\{ { \hspace{0.0pt}X \big |_{E\setminus F} } \;\big |\; X\in \mathcal {M}, X_f=0\, \forall f\in F \right\} \) also forms an oriented matroid, denoted \(\mathcal {M} / _{F}\) and called the *contraction of*\(\mathcal {M}\)*along**F*.

An oriented matroid is called *acyclic*if the all-positive sign-vector \(\varvec{+}_{n}\) is a tope.

The standard way to associate an oriented matroid to a real vector configuration \({\varvec{{V}}}=(\varvec{v}_1,\dots ,\varvec{v}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) is to consider the set of covectors on the ground set \([{n}]\) induced by the signs of the evaluations of linear functionals on the elements of \({\varvec{{V}}}\):

$$\begin{aligned} \mathcal {M}({{\varvec{{V}}}})=\left\{ ({{\,\textrm{sign}\,}}(\left\langle \varvec{u} \, , \, \varvec{v}_1 \right\rangle ,\dots ,{{\,\textrm{sign}\,}}(\left\langle \varvec{u} \, , \, \varvec{v}_n \right\rangle ) \;\big |\; \varvec{u}\in {{\mathbb {R}}}^n \right\} \subseteq \{+,-,0\}^n, \end{aligned}$$

(4)

where \({{\,\textrm{sign}\,}}(x)={\left\{ \begin{array}{ll} + &{}\text { if } x>0\\ - &{}\text { if } x<0\\ 0 &{}\text { if } x=0. \end{array}\right. }\)

That is, to each linear oriented hyperplane, we record which vectors of the configuration lie on the hyperplane, and which lie at the positive and negative sides, respectively. The covectors \(\mathcal {M}({{\varvec{{V}}}})\) label the regions of the hyperplane arrangement \(\mathcal {H}_{{\varvec{{V}}}}\) consisting of the hyperplanes orthogonal to the vectors of \({\varvec{{V}}}\). Under this labeling, the big face lattice is consistent with the inclusion order of the regions, the topes labeling the maximal cells of the arrangement. Thus, the big face lattice on \(\mathcal {M}({{\varvec{{V}}}})\) is isomorphic to (the opposite of) the face lattice of the zonotope \(\sum _{i\in [{n}]} [\varvec{0},\varvec{v}_i]\). The rank of \(\mathcal {M}({{\varvec{{V}}}})\) coincides with the dimension of the linear hull of \({\varvec{{V}}}\). We will call this oriented matroid the *oriented matroid associated to*\({\varvec{{V}}}\). Oriented matroids that arise this way are called *realizable*. Note that even non-realizable oriented matroids can be geometrically realized by *arrangements of pseudo-spheres*, see [[17][28], Sec. 1.4.1 & 5.2].

### 3.2 Three Realizable Oriented Matroids Associated to a Point Configuration

The construction above extends directly to affine point configurations, by considering evaluations of affine functionals instead. (Or, equivalently, linear functionals on the homogenization \(\bar{\varvec{A}}\).) Although this is the standard way to associate an oriented matroid to a point configuration \(\varvec{A}\), we will call it the *little oriented matroid*of \(\varvec{A}\), which is consistent with the notation in [[17][28], Sect. 1.10] for planar configurations. This is to avoid confusion with the other alternative notions of oriented matroid associated to a point configuration that we will introduce. The *big oriented matroid*, which contains more information than the little oriented matroid, is also inspired by [[17][28], Sect. 1.10]. We will prefer a more compact presentation, the *sweep oriented matroid*, which was not explicitly introduced there.

### Definition 3.2

Let \(\varvec{A}=(\varvec{a}_1, \ldots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) be a full-dimensional point configuration (i.e. its affine span is the whole space \({{\mathbb {R}}}^d\)):

1. (i)

The *little oriented matroid*of \(\varvec{A}\), denoted \(\mathcal {M}^{lit} (\bar{\varvec{A}})\), is the oriented matroid of rank \(d+1\) with ground set \([{n}]\) associated to the \((d+1)\) -dimensional homogenized vector configuration \(\bar{\varvec{A}}= (\bar{\varvec{a}}_1, \dots , \bar{\varvec{a}}_n)\in {{\mathbb {R}}}^{(d+1)\times [{n}]}\), where \(\bar{\varvec{a}}_i=(\varvec{a}_i,1)\in {{\mathbb {R}}}^{d+1}\). This is always an acyclic oriented matroid.

2. (ii)

The *sweep oriented matroid*of \(\varvec{A}\), denoted \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\), is the oriented matroid of rank *d*with ground set \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) =\left\{ (i,j) \;\big |\; 1\le i < j \le n \right\} \) associated to the *d*-dimensional vector configuration

$$\begin{aligned} \textstyle \left\{ \varvec{a}_{(i,j)}=\varvec{a}_j-\varvec{a}_i \;\big |\; (i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \right\} \in {{\mathbb {R}}}^{d\times \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }. \end{aligned}$$

3. (iii)

The *big oriented matroid*Footnote 1 of \(\varvec{A}\), denoted \({\mathcal {M}}^{\textsf {big}}({\bar{\varvec{A}}})\), is the oriented matroid of rank \(d+1\) on the ground set \([{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) associated to the \((d+1)\) -dimensional vector configuration

$$\begin{aligned} \textstyle \bar{\varvec{A}}\cup \left\{ (\varvec{a}_{(i,j)},0) \;\big |\; (i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \right\} \in {{\mathbb {R}}}^{\left( d+1\right) \times \left( [{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \right) }. \end{aligned}$$

**Fig. 8**

[image: Fig. 8]

[Full size image][131]

A big oriented matroid (with collinearities indicated). The points in the upper line, which represents the line at infinity, give rise to a sweep oriented matroid, whereas the points below give rise to the associated little oriented matroid

Little, sweep and big oriented matroids obtained this way from a point configuration will be called *realizable*. In Sects. [3.3][132] and [4.1][133], we give definitions for abstract sweep, little and big oriented matroids not necessarily arising from point configurations. We explain below how these structures are related to each other and to the poset of sweeps and the set of sweep permutations.

For a sweep \(I=(I_1, \ldots , I_l)\in \overline{\Pi }({\varvec{A}})\), corresponding to the surjection \(p_{I}: [n] \rightarrow [l]\), we define the sign-vector \(X^{I}\in \{+,-,0\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) such that

$$\begin{aligned} X_{(i,j)}^I={\left\{ \begin{array}{ll} + &{}\text { if } p_{I}(i)<p_{I}(j),\\ - &{}\text { if } p_{I}(i)>p_{I}(j),\\ 0 &{}\text { if } p_{I}(i)=p_{I}(j); \end{array}\right. } \end{aligned}$$

(5)

for \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \).

For example, if *I*is the sweep \((\{1, 3\}, \{2\})\), we have \(p_{I}(1)=p_{I}(3)=1\), \(p_{I}(2)=2\), and the corresponding covector on the ground set \(\{(1,2), (1,3), (2,3)\}\) is \(X^{I}=(+, 0, -)\). Compare Figs. [2][103] and [9][134] to see other examples. As the figures illustrate, this map induces an isomorphism at the level of posets.

**Fig. 9**

[image: Fig. 9]

[Full size image][135]

The vector configuration \(\left\{ \varvec{a}_{(1,2)},\varvec{a}_{(1,3)},\varvec{a}_{(2,3)}\right\} \) associated to the point configuration \(\varvec{A}_3\) from Fig. [2][103]. The covectors associated to the regions of the sweep hyperplane are indicated by sign-vectors of length 3 containing the sign of the scalar product of a vector in the region with \(\varvec{a}_{(1,2)}\), \(\varvec{a}_{(1,3)}\), and \(\varvec{a}_{(2,3)}\), respectively. This should be compared with the labeling of the regions of the sweep hyperplane arrangement in terms of partitions in Fig. [2][103]

### Lemma 3.3

The map \(I \mapsto X^{I}\) induces a poset isomorphism between the poset of sweeps \(\overline{\Pi }({\varvec{A}})\) and the poset of covectors of the sweep oriented matroid \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\).

In particular, \(\overline{\Pi }({\varvec{A}})\cup \hat{\varvec{1}}\), where \(\hat{\varvec{1}}\) is an additional top element, is isomorphic to the big face lattice of \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\), which is the opposite of the face lattice of the zonotope \(\varvec{SP}({\varvec{A}})\) (cf. [[89][21], Cor. 7.17]).

### Proof

Let *I*be an ordered partition in \(\overline{\Pi }({\varvec{A}})\), with corresponding surjection \(p_I\), and associated to the linear form \(u\in {{\mathbb {R}}}^d\). This linear form *u*is also associated to a covector *X*of \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) that is exactly the image of *I*by the above bijection:

$$\begin{aligned} X_{(i,j)} = 0&\Leftrightarrow \left\langle u \, , \, a_j-a_i \right\rangle =0&\Leftrightarrow p_I(i)=p_I(j), \\ X_{(i,j)} = +&\Leftrightarrow \left\langle u \, , \, a_j-a_i \right\rangle>0&\Leftrightarrow p_I(i)<p_I(j), \\ X_{(i,j)} = -&\Leftrightarrow \left\langle u \, , \, a_j-a_i \right\rangle <0&\Leftrightarrow p_I(i)>p_I(j). \end{aligned}$$

Hence both the sweeps of \(\overline{\Pi }({\varvec{A}})\) and the covectors of \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) are in bijection with the cells of the hyperplane arrangement \(\mathcal{S}\mathcal{H}({\varvec{A}})\) and the bijections induce poset isomorphisms. \(\square \)

It follows from the previous lemma that the set of sweep permutations \(\Pi ({\varvec{A}})\) is in bijection with the topes of the sweep oriented matroid \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\). Since the topes of an oriented matroid completely determine it (cf. [[17][28], Proposition 3.8.2]), this implies:

### Corollary 3.4

The set of sweep permutations \(\Pi ({\varvec{A}})\) determines the whole poset of sweeps \(\overline{\Pi }({\varvec{A}})\).

The structures we have introduced are related by the following hierarchy (whose proof depends on the upcoming Proposition [4.3][136]):

### Theorem 3.5

Let \(\varvec{A}\in {{\mathbb {R}}}^{d\times [{n}]}\) be a point configuration. Then the set of sweep permutations \(\Pi ({\varvec{A}})\), the poset of sweeps \(\overline{\Pi }({\varvec{A}})\), the sweep oriented matroid \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) and the big oriented matroid \({\mathcal {M}}^{\textsf {big}}({\bar{\varvec{A}}})\) (cryptomorphically) determine each other. They determine the little oriented matroid \({\mathcal {M}}^{\textsf {lit}}({\bar{\varvec{A}}})\), which does not always determine them.

In particular, the sweep oriented matroid is a combinatorial invariant of a point configuration that is finer than the order type (given by the little oriented matroid).

### Proof

The fact that \(\Pi ({\varvec{A}})\) and \(\overline{\Pi }({\varvec{A}})\) determine each other follows from Corollary [3.4][137]. The equivalence between \(\overline{\Pi }({\varvec{A}})\) and \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) follows from Lemma [3.3][138]. The equivalence between \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) and \({\mathcal {M}}^{\textsf {big}}({\bar{\varvec{A}}})\) will be proved later, as a consequence of Definition [4.2][139] and Proposition [4.3][136].

Finally, \({\mathcal {M}}^{\textsf {big}}({\bar{\varvec{A}}})\) determines \({\mathcal {M}}^{\textsf {lit}}({\bar{\varvec{A}}})\) by restriction to the ground set [*n*] but this operation is not injective. Examples of planar configurations with different sets of sweep permutations but the same little oriented matroid can be found in [[17][28], Section 1.10]. \(\square \)

### 3.3 Sweep Oriented Matroids

The main insight for expanding the notion of sweep oriented matroids from Definition [3.2][140] beyond the realizable case is to note that a configuration of vectors of the form \(\varvec{a}_j-\varvec{a}_i\) for \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) is just the projection of the *braid configuration*\(\{ \varvec{e}_j-\varvec{e}_i \;\big |\; (i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \} \in {{\mathbb {R}}}^{n\times \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) (the set of positive roots of the Coxeter root system \(A_{n-1}\)) under the linear map \({M_{\varvec{A}}}\) defined in ( [3][141]).

Consider the oriented matroid \(\mathcal {B}_{{n}}\) associated to the braid configuration, that is, the graphic oriented matroid of the complete graph \(K_n\) with the acyclic orientation induced by the usual order on \([{n}]\). We will use the same notation \(\mathcal {B}_{{n}}\) as with the hyperplane arrangement, as it will be always clear from the context whether we are considering the hyperplane arrangement or the associated oriented matroid. Note that, since the configuration of the \(\varvec{a}_j-\varvec{a}_i\) is a linear projection of the braid configuration, every covector of \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) is a covector of the braid oriented matroid, as we can pull back linear forms with \({M_{\varvec{A}}}^*\).

The oriented matroid analogues of linear projections are *strong maps*. For two oriented matroids \(\mathcal {M}_1\) and \(\mathcal {M}_2\) on the same ground set, we say that there is a *strong map*from \(\mathcal {M}_1\) to \(\mathcal {M}_2\), denoted \(\mathcal {M}_1\rightarrow \mathcal {M}_2\), if every covector of \(\mathcal {M}_2\) is a covector of \(\mathcal {M}_1\) (see [[17][28], Sec. 7.7]). This will be the starting point for our definition.

### Definition 3.6

An oriented matroid \(\mathcal {M}\) on the ground set \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) is a *sweep oriented matroid*if there is a strong map \(\mathcal {B}_{{n}}\rightarrow \mathcal {M}\) from \(\mathcal {B}_{{n}}\) to \(\mathcal {M}\), i.e. if all covectors of \(\mathcal {M}\) are covectors of \(\mathcal {B}_{{n}}\).

### Remark 3.7

Note that, if \(\mathcal {M}\) is a sweep oriented matroid, then we can interpret its covectors as covectors of the braid arrangement, and hence each covector can be uniquely identified with an ordered partition via the bijection inverse to ( [5][142]). For a covector \(X\in \mathcal {M}\) of a sweep oriented matroid, we will denote by \(I_{X}\) the associated ordered partition.

Our next result characterizes sweep oriented matroids via a 3-term orthogonality condition on covectors (c.f. [[17][28], Sec. 3.4]) that provides an explicit test for deciding whether an oriented matroid is a sweep oriented matroid. It will be relevant later in the context of sweep acycloids in Sect. [7][81].

Recall that the *support*of a sign-vector \(X\in \{+,-,0\}^E\) is \(\underline{X}=\left\{ e\in E \;\big |\; X_e\ne 0 \right\} \). Two sign-vectors \(X,Y\in \{+,-,0\}^E\) are said to be *orthogonal*if either \(\underline{X}\cap \underline{Y}=\emptyset \), or the restrictions of *X*and *Y*to \(\underline{X}\cap \underline{Y}\) are neither equal nor opposite (i.e., there are *i*, *j*with \(X_i=Y_i\ne 0\) and \(X_j=-Y_j\ne 0\)).

### Lemma 3.8

An oriented matroid \(\mathcal {M}\) on \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) is a sweep oriented matroid if and only if for every covector *X*and every choice of \(1\le i< j < k \le n\), the triple \((X_{(i,j)},X_{(j,k)},X_{(i,k)})\) is orthogonal to the sign vector \((+,+,-)\).

Equivalently, \(\mathcal {M}\) is a sweep oriented matroid if and only if for any covector *X*, and for \(1\le i< j < k \le n\), the triple \((X_{(i,j)},X_{(j,k)},X_{(i,k)})\) does not belong to the following list of forbidden patterns:

$$\begin{aligned} \left\{ \begin{array}{ccccccc} (+,+,-),&{}(-,-,+),&{}(0,+,-),&{}(0,-,+),&{}(+,0,-),&{}(-,0,+),&{}(+,+,0),\\ (-,-,0),&{}(0,0,-),&{}(0,0,+),&{}(0,+,0),&{}(0,-,0),&{}(+,0,0),&{}(-,0,0) \end{array} \right\} . \end{aligned}$$

### Proof

There is a strong map \(\mathcal {B}_{{n}}\rightarrow \mathcal {M}\) if and only if all the covectors of \(\mathcal {M}\) are covectors of \(\mathcal {B}_{{n}}\), which is equivalent to the condition that all the covectors of \(\mathcal {M}\) are orthogonal to all circuits of \(\mathcal {B}_{{n}}\) (see [[17][28], Prop. 7.7.1]).

The circuits of \(\mathcal {B}_{{n}}\) are induced by cycles of \(K_n\). They are of the form \(C^{i_1, \ldots , i_r}\) for any collection \(i_1, \ldots , i_r\) of at least 3 distinct elements of \([{n}]\), with \(C^{i_1, \ldots , i_r}_{(i_k, i_{k+1})}=+\) if \(i_k<i_{k+1}\) and \(C^{i_1, \ldots , i_r}_{(i_{k+1}, i_{k})}=-\) if \(i_k>i_{k+1}\) for all \(1\le k \le r\) (with the convention \(i_{r+1}=i_1\)), and \(C^{i_1, \ldots , i_r}_{(h,l)}=0\) for any other pair.

An easy induction shows that the orthogonality to the circuit \(C^{i_1, \ldots , i_r}\) is implied by the orthogonality to all circuits \(C^{i_1, i_k, i_{k+1}}\) for \(2\le k \le r-1\), which is equivalent to our statement. \(\square \)

This condition is actually a reformulation of the transitivity of the partial order induced by an ordered partition *I*(namely \(i \preceq j\) if and only if \(p_I(i)\le p_I(j)\)). For example, forbidding the patterns \((+,+, -)\) and \((+, +, 0)\) is equivalent to stating that \(i\prec j \prec k\) implies \(i\prec k\), and so on. This is why we refer to it as the *transitivity condition*on sweep oriented matroids.

The *poset of sweeps*of a sweep oriented matroid \(\mathcal {M}\) is the partially ordered set \(\overline{\Pi }({\mathcal {M}})\) of the ordered partitions \(I_{X}\) for the covectors \(X\in \mathcal {M}\), ordered by refinement. Enlarged with a top element \(\hat{\varvec{1}}\), this poset is isomorphic to the big face lattice of \(\mathcal {M}\). The topology of such complexes is well known [[17][28], Thm. 4.3.3]. We describe it in the following proposition. Note that there is some ambiguity in the literature concerning the definition of the poset of faces of cell complexes, in particular whether it should be augmented by a bottom element or not (compare [[12][143], Fig. 2] and [[14][100], Fig. 2]). We follow [[14][100]] and [[17][28]] and do not include an additional bottom element in the definition of the *face poset*of a cell complex.

### Proposition 3.9

[[17][28], Thm. 4.3.3] The poset of sweeps \(\overline{\Pi }({\mathcal {M}})\smallsetminus ([{n}])\) of a sweep oriented matroid \(\mathcal {M}\) of rank *r*without the trivial sweep is isomorphic to the face poset of a shellable regular cell decomposition of the \((r-1)\) -sphere. In particular, the order complex \(\Delta \left( {\overline{\Pi }({\mathcal {M}})\smallsetminus ([{n}])}\right) \) triangulates the \((r-1)\) -sphere.

## 4 Big and Little Oriented Matroids

In this section we show how the big and little oriented matroids of a point configuration (Definition [3.2][140]) are completely determined by its sweep oriented matroid. Actually, the construction of these matroids can be extended to any abstract sweep oriented matroid, providing definitions beyond the realizable case. This generalizes the results for rank 3 proved in [[17][28], Sec. 1.10].

### 4.1 Big and Little Oriented Matroids Associated to Sweep Oriented Matroids

First, we will show how to extend any sweep oriented matroid to what will be called a big oriented matroid. For a covector *X*of a sweep oriented matroid, let \(p_{X}:[{n}]\rightarrow [l_X]\) be the surjection associated to the corresponding ordered partition. For each \(1\le k \le 2l_X+1\), let \(X^k\in \{+,-,0\}^{[{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) be the sign-vector:

$$\begin{aligned} {X}^k_i&= {\left\{ \begin{array}{ll} - &{}\text { if } p_X(i)\le \lfloor \frac{k-1}{2} \rfloor , \\ + &{}\text { if } p_X(i)>\lfloor \frac{k}{2} \rfloor , \\ 0 &{}\text { if } k \text { is even and } p_X(i)=\frac{k}{2}. \end{array}\right. }{} & {} \text { for }1\le i\le n;\\ {X}^k_{(i,j)}&= X_{(i,j)}{} & {} \text { for all } 1\le i < j \le n. \end{aligned}$$

We defer the details of checking that the transitivity condition from Lemma [3.8][144] implies the oriented matroid axioms for these covectors to Appendix [B][145]. They are easy, but tedious.

### Theorem 4.1

If \(\mathcal {M}\) is the set of covectors of a sweep oriented matroid, then

$$\begin{aligned} {\mathcal {M}}^{\textsf {big}} = \left\{ {X}^k \;\big |\; X\in \mathcal {M}, \, 1\le k\le 2l_X+1 \right\} \end{aligned}$$

is the set of covectors of an oriented matroid.

### Definition 4.2

Let \(\mathcal {M}\) be a sweep oriented matroid. The oriented matroid \({\mathcal {M}}^{\textsf {big}}\) is the *big oriented matroid*of \(\mathcal {M}\); and the oriented matroid \({\mathcal {M}}^{\textsf {lit}}\) obtained by deleting all pairs (*i*, *j*) from \({\mathcal {M}}^{\textsf {big}}\) is the *little oriented matroid*of \(\mathcal {M}\).

These definitions are indeed coherent with the realizable case, as the following proposition shows. This proves that the sweep oriented matroid of a point configuration determines its big and little oriented matroids, concluding the proof of Theorem [3.5][146].

### Proposition 4.3

The big and little oriented matroids of a point configuration are the big and little oriented matroids associated to its sweep oriented matroid.

### Proof

Let \(\varvec{A}=(\varvec{a}_1,\dots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) be a *d*-dimensional point configuration. Every vector \(\varvec{u}\in {{\mathbb {R}}}^d\) induces an ordering of \(\varvec{A}\), which is encoded in a covector *X*of \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\). For \(c\in {{\mathbb {R}}}\), the partition

$$\begin{aligned} \left\{ i \;\big |\; \left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle <c \right\} , \left\{ i \;\big |\; \left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle =c \right\} , \left\{ i \;\big |\; \left\langle \varvec{u} \, , \, \varvec{a}_i \right\rangle >c \right\} \end{aligned}$$

only depends on which, or between which pair, of the \(l_X\) values attained by \(\left\langle \varvec{u} \, , \, \cdot \ \right\rangle \) on \(\varvec{A}\) does *c*lie. These \(2l_X+1\) distinct partitions are precisely those encoded by the covectors \(X^k\) defining the big oriented matroid of \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\). \(\square \)

Note that, by the definition of the big oriented matroid of \(\mathcal {M}\), the zero covector \(\varvec{0}\) of \(\mathcal {M}\) induces the all-positive tope \(\varvec{+}_{n}\) in \({\mathcal {M}}^{\textsf {lit}}\), which is hence an acyclic oriented matroid.

The following lemma concerning the ranks of the big and little oriented matroids will be needed later.

### Lemma 4.4

If the sweep oriented matroid \(\mathcal {M}\) is of rank *r*, then \({\mathcal {M}}^{\textsf {big}}\) and \({\mathcal {M}}^{\textsf {lit}}\) are of rank \(r+1\).

### Proof

To justify that \({\mathcal {M}}^{\textsf {big}}\) has rank \(r+1\), it is sufficient to notice that if \(\varvec{0}_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }=Y^0\prec Y^1\prec \cdots \prec Y^{r}\) is a maximal chain of covectors of \(\mathcal {M}\), then \(\varvec{0}_{[{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }=Z^{-1}\prec Z^0\prec Z^1\prec \cdots \prec Z^{r}\) is a maximal chain of covectors of \({\mathcal {M}}^{\textsf {big}}\), where for any \(k\in \{0, \ldots , r\}\), we define \(Z^k\) by \({ \hspace{0.0pt}Z^k \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }=Y^k\) and \({ \hspace{0.0pt}Z^k \big |_{[{n}]} }=\varvec{+}_{n}\). Indeed, we cannot add a covector *Z*in the big oriented matroid between \(Z^{-1}\) and \(Z^0\) because if \(Z_i=0\) and \(Z_j=+\) we necessarily have \(Z_{(i,j)}\ne 0\) since *i*and *j*are not in the same part of the ordered partition \(l_Z\). We cannot add a covector strictly between \(Z^k\) and \(Z^{k+1}\) either because its restriction to \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) would give a covector of \(\mathcal {M}\) strictly between \(Y^k\) and \(Y^{k+1}\).

We prove that \({\mathcal {M}}^{\textsf {lit}}\) also has rank \(r+1\) by induction on *r*. If \(\mathcal {M}\) is of rank \(r=0\), then \(\varvec{0}_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) is its only covector. It induces the little oriented matroid of rank 1 consisting of the covectors \(\varvec{-}_{n}\), \(\varvec{0}_{n}\), and \(\varvec{+}_{n}\).

Now, suppose that \(\mathcal {M}\) is a sweep oriented matroid on ground set \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) that has rank \(r\ge 1\). Up to relabelling, we can suppose that \((n-1,n)\) is not a loop. Then the contraction of \(\mathcal {M}\) along \(\{(n-1,n)\}\) has rank \(r-1\). Under the bijection ( [5][142]), the covectors of this contraction \(\mathcal {M} / _{\{(n-1,n)\}}\) correspond to the partitions associated to covectors of \(\mathcal {M}\) such that \(n-1\) and *n*are in the same part. This implies that for all \(i\le n-2\), the pairs \((i,n-1)\) and (*i*, *n*) are parallel. By deleting all the pairs (*i*, *n*) we obtain an oriented matroid \(\mathcal {M}'\) on \(\left( {\begin{array}{c}{[n-1]}\\ 2\end{array}}\right) \) isomorphic to \(\mathcal {M} / _{\{(n-1,n)\}}\). The transitivity condition from Lemma [3.8][144] is preserved, and hence \(\mathcal {M}'\) is a sweep oriented matroid of rank \(r-1\) and \({\mathcal {M}'}^{\textsf {lit}}\) has rank *r*, by induction. A maximal chain of the contraction \({\mathcal {M}'}^{\textsf {lit}}/(n-1)\) induces a chain \(\varvec{0}_{n}=X^0 \prec \cdots \prec X^{r-1}\) of \({\mathcal {M}}^{\textsf {lit}}\) in which \((X^i)_{n-1}=(X^i)_n=0\) for all \(0\le i\le r-1\) and that is maximal with this property. Since \(n-1\) and *n*are not parallel (because \((n-1,n)\) is not a loop), there is a covector *Y*of \({\mathcal {M}}^{\textsf {lit}}\) such that \(Y_{n-1}=+\) and \(Y_n=0\). Setting \(X^{r}=X^{r-1}\circ Y\), and \(X^{r+1}=X^{r}\circ \varvec{+}_{n}\), we obtain a chain

$$\begin{aligned} \varvec{0}_{n}=X^0 \prec \cdots \prec X^{r-1}\prec X^{r}\prec X^{r+1} \end{aligned}$$

of lenght \(r+1\) of covectors of \({\mathcal {M}}^{\textsf {lit}}\). Moreover, the restriction operation on oriented matroids cannot increase the rank, thus the rank of \({\mathcal {M}}^{\textsf {lit}}\) cannot be bigger than the rank of \({\mathcal {M}}^{\textsf {big}}\). Hence \({\mathcal {M}}^{\textsf {lit}}\) also has rank \(r+1\). \(\square \)

### Example 4.5

(The braid oriented matroids in types *A*and *B*) The study of big oriented matroids of Coxeter hyperplane arrangements in types *A*and *B*unveils a recursive decomposition that, in view of the upcoming Sect. [4.2][147], explains the existence of a maximal chain of modular flats. This important property was first studied by Stanley under the name of *supersolvability*[[78][148]].

**Type**\(\textbf{A}\). The big oriented matroid of the braid oriented matroid \(\mathcal {B}_{{n}}\) is the braid oriented matroid \(\mathcal {B}_{{n+1}}\). More precisely, if we relabel the elements \(i\in [{n}]\) by \((1,i+1)\) and the elements \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) by \((i+1,j+1)\), then we recover the braid oriented matroid \(\mathcal {B}_{{n+1}}\). Indeed, the topes of \({\mathcal {B}_{{n}}}^{\textsf {big}}\) are of the form \(X^{2k+1}\) where *X*is a tope of \(\mathcal {B}_{{n}}\) and \(0\le k\le n\). If *X*corresponds to the permutation \((\sigma (1),\dots ,\sigma (n))\in \mathfrak {S}_{n}\), then \(X^{2k+1}\) corresponds to the permutation in \(\mathfrak {S}_{n+1}\):

$$\begin{aligned} (\sigma (1)+1,\dots ,\sigma (k)+1,1,\sigma (k+1)+1,\dots ,\sigma (n)+1). \end{aligned}$$

**Type**\(\textbf{B}\). Consider the type *B*braid oriented matroid \(\mathcal {B}_{{n}}^{B}\) from Sect. [2.2.2][149], indexed by the elements in \(\left( {\begin{array}{c}{[\pm n]}\\ 2\end{array}}\right) \). That is, \(\mathcal {B}_{{n}}^{B}\) is the sweep oriented matroid of the vertex set of the cross-polytope. Then its big oriented matroid \({{(\mathcal {B}_{{n}}^{B})}}^{\textsf {big}}\) is FL-isomorphic to \(\mathcal {B}_{{n+1}}^{B}\) without one element (of those of the form \((-i,i)\)).

To see it, it is easier to consider first an enlarged version, with base elements

$$\begin{aligned}{}[-n,n]=\{-n,\dots ,-1,0,1,\dots ,n\} \end{aligned}$$

corresponding to the point configuration

$$\begin{aligned} \widetilde{\varvec{B}}_n=(- \varvec{e}_{n}, \ldots , - \varvec{e}_1, \varvec{0}, \varvec{e}_1, \ldots , \varvec{e}_n) \end{aligned}$$

that contains the vertices of the cross-polytope together with the origin. The FL-isomorphism class of the sweep oriented matroid does not change, but we get some new parallel elements. Namely, the elements labeled \((-i,i)\), \((-i,0)\), and (0, *i*) become parallel (with the same orientation) in the enlarged sweep oriented matroid \(\widetilde{\mathcal {B}}_{{n}}^{B}={\mathcal {M}}^{\textsf {sw}}({\widetilde{\varvec{B}}_n})\). Now, relabel the elements \([-n,n]\cup \left( {\begin{array}{c}{[{-n,n}]}\\ 2\end{array}}\right) \) to \(\left( {\begin{array}{c}{[{-n-1,n+1}]}\\ 2\end{array}}\right) \) by sending each \(i\in [{\pm n}]\) to the pair of parallel elements \((-n-1,-i), (i,n+1)\); 0 to the triple of parallel elements \((-n-1,n+1),(-n-1,0),(0,n+1)\); and leaving the pairs in \(\left( {\begin{array}{c}{[-n,n]}\\ 2\end{array}}\right) \) unchanged. Each tope *X*of the sweep oriented matroid \(\widetilde{\mathcal {B}}_{{n}}^{B}\) is represented by a centrally symmetric permutation \(\sigma \) of \([{-n,n}]\):

$$\begin{aligned} (-\sigma (n), \dots , -\sigma (1),0,\sigma (1),\dots ,\sigma (n)). \end{aligned}$$

Under the relabeling we can read the topes \(X^{2k+1}\) of the big oriented matroid \({{(\widetilde{\mathcal {B}}_{{n}}^{B})}}^{\textsf {big}}\) as centrally symmetric permutations of \([{-n-1,n+1}]\) representing topes of \(\widetilde{\mathcal {B}}_{{n+1}}^{B}\). Namely, for \(0\le k\le n+1\), the tope \(X^{2k+1}\) corresponds to the centrally symmetric permutation:

$$\begin{aligned}{} & {} (-\sigma (n), \dots , -\sigma ({n-k+1}), -n-1, -\sigma ({n-k}), \dots ,\\{} & {} \sigma ({n-k}),n+1,\sigma ({n+1-k}),\dots \sigma ({n})). \end{aligned}$$

whereas for \(n+2\le k\le 2n+2\) it corresponds to:

$$\begin{aligned}{} & {} (-\sigma (n), \dots , -\sigma ({n-k+1}), n+1, -\sigma ({n-k}), \dots ,\\{} & {} \sigma ({n-k}),-n-1,\sigma ({n+1-k}),\dots \sigma ({n})). \end{aligned}$$

This shows that \({{(\widetilde{\mathcal {B}}_{{n}}^{B})}}^{\textsf {big}}\) is FL-isomorphic to \(\widetilde{\mathcal {B}}_{{n+1}}^{B}\), and hence to \(\mathcal {B}_{{n+1}}^{B}\).

If we want to consider the original configuration without the origin, we simply need to remove all the elements of the big oriented matroid that involve a label using 0. Every parallelism class conserves at least one representative except for the singleton 0, which was sent to the triple \((-n-1,n+1),(-n-1,0),(0,n+1)\) with our relabeling. This shows that \({{(\mathcal {B}_{{n}}^{B})}}^{\textsf {big}}\) is FL-isomorphic to \(\mathcal {B}_{{n+1}}^{B}\smallsetminus (-n-1,n+1)\).

### Remark 4.6

(On labeling and isomorphism) The labeling plays an important role in the definition of a sweep oriented matroid and in Theorem [3.5][146]. Indeed, non-isomorphic big oriented matroids might arise from isomorphic sweep oriented matroids. (Here, we mean FL-isomorphism, but the statement is also true for the other standard notions of oriented matroid isomorphism.) For example, all sufficiently generic planar *n*-point configurations give rise to FL-isomorphic sweep oriented matroids but their big oriented matroids are not FL-isomorphic.

### Remark 4.7

(On realizability) Note that, for a big oriented matroid \(\mathcal {M}\), realizability as an oriented matroid (i.e. in the sense of ( [4][150])) is equivalent to realizability as a big oriented matroid (i.e. in the sense of Definition [3.2][140]). Indeed, any point configuration \(\varvec{A}\) such that \({\mathcal {M}}^{\textsf {big}}({\bar{\varvec{A}}})=\mathcal {M}\) can be extended (with the corresponding points at infinity) to an oriented matroid realization of \(\mathcal {M}\). And reciprocally, the restriction of any oriented matroid realization of \(\mathcal {M}\) to the elements indexed by \([{n}]\) can be sent, after a suitable projective transformation and dehomogenization, to a point configuration \(\varvec{A}\) such that \({\mathcal {M}}^{\textsf {big}}({\bar{\varvec{A}}})=\mathcal {M}\).

**Fig. 10**

[image: Fig. 10]

[Full size image][151]

The allowable sequence \((1,2,3,4,5) \rightarrow (1,2,4,3,5)\rightarrow (2,1,4,3,5) \rightarrow (2,1,4,5,3) \rightarrow (2,4,1,5,3) \rightarrow (2,4,5,1,3) \rightarrow (4,2,5,1,3) \rightarrow (4,5,2,1,3) \rightarrow (4,5,2,3,1) \rightarrow (4,5,3,2,1) \rightarrow (5,4,3,2,1) \) cannot be realized by a point configuration, because it would necessarily be a pentagon whose sides and “parallel diagonals” meet as in the above picture, which is geometrically impossible [[44][26]]

In contrast, there are sweep oriented matroids that are realizable as an oriented matroid but that are not of the form \({\mathcal {M}}^{\textsf {sw}}({\bar{\varvec{A}}})\) for any point configuration \(\varvec{A}\). Indeed, the non-realizable pentagon of [[44][26]] (see Fig. [10][27]) gives rise to a non-realizable allowable sequence; that is, to a non-realizable big oriented oriented matroid of rank 3. The associated sweep oriented matroid is an oriented matroid of rank 2, and thus realizable (as an oriented matroid) [[17][28], Cor. 8.2.3]. However, it is not the sweep oriented matroid of a point configuration, because the corresponding big oriented matroid is not realizable.

We end this remark by noting that the Universality Theorem for allowable sequences of Hoffmann and Merckx [[54][46]] implies that it is \((\exists {{\mathbb {R}}})\) -hard to decide whether a big oriented matroid is realizable.

### 4.2 Big Oriented Matroids and Tight Modular Hyperplanes

In this section we provide an alternative characterization of the FL-isomorphism classes of big oriented matroids, and hence of sweep oriented matroids. It is purely structural, without relying on the labeling of the elements. We show that they are closely related to the concept of modular hyperplanes.

According to our definition, every big oriented matroid \({\mathcal {M}}^{\textsf {big}}\) on \([{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) contains the cocircuit \(Z=(\varvec{+}_{n},\varvec{0}_{\left( {\begin{array}{c}n\\ 2\end{array}}\right) })\). Moreover, \(X_{(i,j)}=0\) for any covector *X*such that \(X_i=X_j=0\); which is equivalent to the fact that for any *i*, *j*not in the same parallelism class, the restriction of \({\mathcal {M}}^{\textsf {big}}\) to the set \(\{i,j,(i,j)\}\subset E\) has rank 2. These two properties show that the set of indices \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) form a *modular hyperplane*.

The *flats*of an oriented matroid \(\mathcal {M}\) of rank *r*on *E*are the flats of its underlying (unoriented) matroid \(\underline{\mathcal {M}}\); that is, the zero-sets of its covectors. The poset of flats ordered by inclusion forms a geometric lattice [[17][28], 4.1.13]. The *hyperplanes*are the flats of rank \(r-1\), and they arise as zero-sets of cocircuits. A flat *F*is called *modular*if \({{\,\textrm{rk}\,}}_{}(F)+{{\,\textrm{rk}\,}}_{}(G)={{\,\textrm{rk}\,}}_{}(F\wedge G)+{{\,\textrm{rk}\,}}_{}(F\vee G)\) for any other flat *G*, where \({{\,\textrm{rk}\,}}_{}(\cdot )\) is the rank function of the geometric lattice (for a flat *F*, \({{\,\textrm{rk}\,}}_{}(F)\) coincides with the rank of the oriented matroid \({ \hspace{0.0pt}\mathcal {M} \big |_{F} }\)). Modular flats have many interesting properties, and play an important role in the theory of matroids, see [[21][60], [77][59]].

Hence, a *modular hyperplane*is a hyperplane \(F\subset E\) such that \({{\,\textrm{rk}\,}}_{}(F\wedge G)={{\,\textrm{rk}\,}}_{}(F\cap G)={{\,\textrm{rk}\,}}_{}(G)-1\) for any flat *G*not contained in *F*. Said differently, \(F\cap G\) is a hyperplane in \({ \hspace{0.0pt}\mathcal {M} \big |_{G} }\). In [[21][60], Cor. 3.4] it is shown that a hyperplane is modular if and only if it intersects every line (flat *G*with \({{\,\textrm{rk}\,}}_{}(G)=2\)). Equivalently, if for every pair of elements \(x,y\in E\smallsetminus F\) that are not parallel nor a loop, there is some element \(z\in F\) such that for every covector *X*with \(X_x=X_y=0\) we have \(X_z=0\). We will say that a modular hyperplane *F*is *tight*if there is no \(z\in F\) such that \(F\smallsetminus z\) is a modular hyperplane of \({ \hspace{0.0pt}\mathcal {M} \big |_{E\smallsetminus z} }\).

The following result gives a characterization of big oriented matroids similar to the one given in [[17][28], Sect. 6.4] for the rank 3 case.

### Proposition 4.8

Let \(\mathcal {M}\) be an oriented matroid on ground set \(E=[{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) such that:

1. (1)

there exists a cocircuit *Z*of \(\mathcal {M}\) such that \(\{e\in E \, |\, Z_e=0\}=\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) (i.e. \(\underline{Z}=[n]\)),

2. (2)

for any \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), for any covector *X*of \(\mathcal {M}\), if two coordinates among \(X_i\), \(X_j\), \(X_{(i,j)}\) are zero, then the third one is zero too.

Then, up to reorientation, \(\mathcal {M}\) is the big oriented matroid of the sweep oriented matroid \({ \hspace{0.0pt}\mathcal {M} \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\).

In a realizable setting, and without parallel elements and loops, the conditions on \(\mathcal {M}\) amount to asking that the real vector representing (*i*, *j*) is in the intersection of the 2-plane spanned by the real vectors representing *i*and *j*and the hyperplane given by the cocircuit *Z*(which contains all the vectors corresponding to elements in \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \)). One can check that the example depicted in Fig. [8][152] satisfies this condition.

### Proof

We need to prove that, after the reorientation of some elements of the ground set, the restriction \({ \hspace{0.0pt}\mathcal {M} \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\) is a sweep oriented matroid, i.e. it satisfies Lemma [3.8][144], and the covectors of \(\mathcal {M}\) are exactly those obtained from the covectors of \({ \hspace{0.0pt}\mathcal {M} \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\) as in Theorem [4.1][56].

We can assume that, after a suitable reorientation of \(\mathcal {M}\) we have that \(Z=(\varvec{+}_{n},\varvec{0}_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) })\). Note that \({ \hspace{0.0pt}\mathcal {M} \big |_{[{n}]} }\) cannot have loops, as witnessed by *Z*; and that if *i*and *j*are parallel, then (*i*, *j*) must be a loop. We will from now on assume that \(\mathcal {M}\) does not have parallel elements, as it simplifies the exposition.

Let us show that for any two covectors \(X, Y\in \mathcal {M}\) such that \(X_i=Y_i=-\), \(X_j=Y_j=+\) we have \(X_{(i,j)}=Y_{(i,j)}\ne 0\). Assume the contrary. Then the axiom Definition [3.1][153] on oriented matroids would imply the existence of a covector \(T\in \mathcal {M}\) such that \(T_i=-\), \(T_j=+\) and \(T_{(i,j)}=0\). A second application of the axiom Definition [3.1][153] between *T*and *Z*would give the existence of a covector \(T'\in \mathcal {M}\) such that \(T'_i=T'_{(i,j)}=0\) and \(T'_j=+\), which contradicts the second assumption on \(\mathcal {M}\). Hence, we can reorient (*i*, *j*) so that for any covector *X*of \(\mathcal {M}\) with \(X_i = -\) and \(X_j = +\), we have \(X_{(i,j)} = +\).

To check that \({ \hspace{0.0pt}\mathcal {M} \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\) is a sweep oriented matroid, it suffices to look at all restrictions of the form

$$\begin{aligned} { \hspace{0.0pt}\mathcal {M} \big |_{\{i, j, k, (i,j), (j,k), (i,k)\}} } \end{aligned}$$

for \(1\le i< j < k \le n\). This gives an oriented matroid of rank at most 3. One can easily check that with our conditions there are only three possible configurations, none of which violates the condition from Lemma [3.8][144].

Moreover, it is clear that any covector *X*of \(\mathcal {M}\) can be obtained from the covector \({ \hspace{0.0pt}X \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\) of \({ \hspace{0.0pt}\mathcal {M} \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\) by the method described at the beginning of Sect. [4.1][133]. Indeed, our reorientation on \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) implies that the ordered partition of \([{n}]\) given by \((I_-=\{i \, |\, X_i=-\}, \, I_0=\{i \, |\, X_i=0\}, I_+=\{i \, |\, X_i=+\})\) is refined by the ordered partition *J*induced by \({ \hspace{0.0pt}X \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\), in such a way that either \(I_0=\emptyset \) or \(I_0\) is an entire part of *J*. Thus *X*is of the form \(({ \hspace{0.0pt}X \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } })^k\) for some *k*.

It remains to check that, for every covector \(Y\in { \hspace{0.0pt}\mathcal {M} \big |_{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\), all covectors \(Y^k\) obtained by the method described in Sect. [4.1][133] are indeed covectors of \(\mathcal {M}\). We do it by induction on *k*. Observe first that \(Y^1=Z\circ \tilde{Y}\), where \(\tilde{Y}\) is any covector in \(\mathcal {M}\) whose restriction to \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) gives *Y*. Thus, we have \(Y^1\in \mathcal {M}\).

Now, for an odd \(k_0\in [{2 l_Y}]\), we apply the Elimination Axiom (V3) to the covectors \(Y^{k_0}\) and \((-Z)\circ Y^{k_0}\), and the smallest element \(i_0\in p_{Y}^{-1}(\{\frac{k_0 + 1}{2}\})\) to obtain a covector *T*. We claim that \(T=Y^{k_0+1}\). Indeed, for all *i*where \(p_{Y}(i)<\frac{k_0 + 1}{2}\) we have \(T_i=Y^{k_0}_i=(-Z)_i=-\). For all \(i\in p_{Y}^{-1}(\{\frac{k_0 + 1}{2}\})\), we have \(T_{i_0}=0\) and \(T_{(i_0,i)}=Y^{k_0}_{(i_0,i)}=(-Z)_{(i_0,i)}=0\), so the second hypothesis on \(\mathcal {M}\) implies that \(T_{i}=0\). Let *i*where \(p_{Y}(i)>\frac{k_0 + 1}{2}\). We assume that \(i>i_0\), the other case is analogous. We have that \(T_{(i_0,i)}=Y^{k_0}_{(i_0,i)}\ne 0\) and \(T_{i_0}=0\), so \(T_{i}\ne 0\) by the second hypothesis. This forces that \(T_i=+\) as otherwise \(T\circ Z\) would satisfy \((T\circ Z)_{i_0}=-(T\circ Z)_{i}=(T\circ Z)_{(i_0,i)}\), which contradicts our assumption on the reorientation.

To conclude, if \(k_0\) is even, then \(Y^{k_0+1} = Y^{k_0}\circ (-Z)\). \(\square \)

We get the following characterization as a direct corollary.

### Theorem 4.9

A simple oriented matroid \(\mathcal {M}\) is FL-isomorphic to a big oriented matroid if and only if it has a tight modular hyperplane.

### Proof

It is straightforward to check that in a big oriented matroid the elements indexed by \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) form a modular hyperplane that is tight up to the simplification of parallel elements.

For the converse, let *E*be the ground set of \(\mathcal {M}\), and \(F\subseteq E\) a tight modular hyperplane. We will relabel the elements of \(E\smallsetminus F\) by \([{n}]\), where \(n=|E\smallsetminus F|\). Now, for each \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) there is an element \(z\in F\) in the line spanned by *i*and *j*by the modularity of *F*. We add to \(\mathcal {M}\) an element parallel to *z*labeled by \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). We obtain this way an isomorphic oriented matroid \(\mathcal {M}'\). Note that, since the modular hyperplane \(F\subseteq E\) is tight, for each \(z\in F\) there are some \(i,j\in E\smallsetminus F\) such that *i*, *j*, *z*are collinear. Hence, *z*is parallel to (*i*, *j*) and \(\mathcal {M}'\smallsetminus z\) is isomorphic to \(\mathcal {M}\). We conclude that \({ \hspace{0.0pt}\mathcal {M}' \big |_{[{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) } }\) is isomorphic to \(\mathcal {M}\). It satisfies the conditions of Proposition [4.8][154] and is hence isomorphic to a big oriented matroid. \(\square \)

A consequence of this observation is that we can extend the process to determine the big oriented matroid from the sweep oriented matroid to any oriented matroid with a modular hyperplane (not necessarily tight). For sweep oriented matroids, this relies on the labeling of the elements (see Remark [4.6][155]). Arbitrary modular hyperplanes also need a similar extra information. Let \(\mathcal {M}\) be an oriented matroid on a ground set *E*with a modular hyperplane *F*. To simplify the exposition, we will assume that \(\mathcal {M}\) is simple (no loops or parallel elements), that \(E\smallsetminus F=[{n}]\), that \(F\cap \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) =\emptyset \), and that all the elements of \(E\smallsetminus F\) lie in a common halfspace defined by *F*. (We could omit this simplification by adding information to the decoration, but it unnecessarily complicates the notation.)

We will *decorate*the elements in *F*by constructing maps \(\delta : F\rightarrow 2^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) and \(\epsilon :\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \rightarrow \{+,-\}\) that associate a subset of elements of \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) to each \(f\in F\) and a sign to each pair in \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). This is done with the following algorithm. We start decorating each element in *F*with an empty set. For every \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), let \(f\in F\) be the element of *F*in the flat spanned by *i*and *j*. We add to the decoration \(\delta (f)\) of *f*the ordered pair (*i*, *j*); and we set \(\epsilon (i,j)=+\) if there is a covector \(X\in \mathcal {M}\) such that \(X_i=0\) and \(X_j=X_f\ne 0\), or \(\epsilon (i,j)=-\) otherwise. We will call this information the *decoration of**F**induced by*\(\mathcal {M}\).

We will show that we can recover \(\mathcal {M}\) from \(\mathcal {M}'={ \hspace{0.0pt}\mathcal {M} \big |_{F} }\), its restriction to *F*, and the decoration. To state our result, we introduce *valid decorations*, which are those that can be obtained with the procedure above. For any simple oriented matroid \(\mathcal {M}'\) on the ground set *F*, we call a *valid decoration*a couple of maps \(\delta :F\rightarrow 2^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) and \(\epsilon :\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \rightarrow \{+,-\}\) for a certain *n*, such that:

-

the decorations form a partition of \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), with empty parts accepted: \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) = \bigcup _{f\in F} \delta (f)\) with \( \delta (f)\cap \delta (f')=\emptyset \) whenever \(f\ne f'\); and

-

the covectors \(X\in \mathcal {M}\), seen as elements of \(\{+,-,0\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) by considering \(X_{(i,j)}=\epsilon (i,j)X_f\) if \((i,j)\in \delta (f)\), satisfy the transitivity condition from Lemma [3.8][144].

The following result should be seen as the oriented version of [[19][62], Thm. 2.1], which similarly characterizes when an (unoriented) matroid can be extended so that its ground set is a modular hyperplane of the larger matroid. We have deferred its proof to Appendix [B][145], since it relies on the proof of Theorem [4.1][56].

### Corollary 4.10

If \(\mathcal {M}'\) is a simple oriented matroid on *F*with a valid decoration \((\delta ,\epsilon )\), then \(\mathcal {M}'\) can be extended to a unique oriented matroid \(\mathcal {M}\) for which *F*is a modular hyperplane and \((\delta ,\epsilon )\) is the decoration of *F*induced by \(\mathcal {M}\).

In particular, an oriented matroid \(\mathcal {M}\) with a modular hyperplane *F*is completely determined by \({ \hspace{0.0pt}\mathcal {M} \big |_{F} }\) together with the decoration of *F*induced by \(\mathcal {M}\).

### 4.3 Not Every Oriented Matroid is a Little Oriented Matroid

Little oriented matroids are always acyclic, meaning that \(\varvec{+}_{n}\) is a tope. A first guess could be that all acyclic oriented matroids can be extended to a big oriented matroid. After all, this is trivially the case for realizable oriented matroids. Moreover, it is also true for rank 3 oriented matroids. Although stated in a different language, this follows directly from [[17][28], Thm. 6.3.3] and [[42][92], Lemma 1] Footnote 2, which was first proved in the uniform case in [[76][156]]. (Actually, their result is stronger, as the sweep oriented matroid they construct is Dilworth in the sense of the upcoming Sect. [5.1][157].)

### Theorem 4.11

[[17][28], Thm. 6.3.3] Every loopless acyclic oriented matroid \(\mathcal {M}\) of rank 3 is the little oriented matroid of a sweep oriented matroid.

However, contrary to the rank 3 case, starting at rank 4 there exist acyclic oriented matroids that cannot be extended to big oriented matroids. The proof of Theorem [4.11][158] in [[17][28]] uses Levi’s extension lemma, that states that every arrangement of pseudolines can be extended with an extra pseudoline through two given points. We use a famous counterexample to the analogous statement in rank 4 by Richter-Gebert [[72][159]] to present an acyclic oriented matroid that cannot be extended to a big oriented matroid.

### Theorem 4.12

[[72][159], Cor. 3.4] There is an oriented matroid \(\mathcal {R}\mathcal {G}\) of rank 4 with ground set \([{12}]\) with two topes *U*and *T*such that no extending pseudoplane intersects *U*and *T*simultaneously.

This means that if \(\mathcal {R}\mathcal {G}'\) is an oriented matroid on \([{12}]\cup \{f\}\) such that \({ \hspace{0.0pt}\mathcal {R}\mathcal {G}' \big |_{[{12}]} }=\mathcal {R}\mathcal {G}\), then it cannot contain covectors \(U', T'\in \mathcal {R}\mathcal {G}'\) such that \({ \hspace{0.0pt}U' \big |_{[{12}]} }\preceq U\) and \({ \hspace{0.0pt}T' \big |_{[{12}]} }\preceq T\) but \(U'_f=T'_f=0\).

### Theorem 4.13

The reorientation of \(\mathcal {R}\mathcal {G}\) sending *U*to \(\varvec{+}_{12}\) is acyclic, but it is not the little oriented matroid of any sweep oriented matroid.

### Proof

After a suitable reorientation, assume that \(U=\varvec{+}_{12}\). Suppose that there is a big oriented matroid \(\mathcal {M}\) on \([{12}]\cup \left( {\begin{array}{c}{[{12}]}\\ 2\end{array}}\right) \) such that \({ \hspace{0.0pt}\mathcal {M} \big |_{[{12}]} }=\mathcal {R}\mathcal {G}\). It contains a cocircuit \(U'\in \mathcal {M}\) with \(U'_i=U_i=+\) for all \(i\in [{12}]\) and \(U'_{(i,j)}=0\) for all \((i,j)\in \left( {\begin{array}{c}{[{12}]}\\ 2\end{array}}\right) \).

Let *X*be a covector in \(\mathcal {R}\mathcal {G}\) such that [*X*, *T*] forms an interval of length 2 in the face lattice of \(\mathcal {R}\mathcal {G}\). This means that there are \(1\le i_0 < j_0 \le 12\) such that \(X_{i_0}=X_{j_0}=0\) and \(X_i\preceq T_i\) for all \(i\in [{12}]{\setminus }\{i_0, j_0\}\). Let \(X'\) be a covector in \(\mathcal {M}\) such that \({ \hspace{0.0pt}X' \big |_{[{12}]} }=X\). Hence, we have \(X'_{(i_0,j_0)}=0\) and \({ \hspace{0.0pt}X' \big |_{[{12}]} }\preceq T\). Hence \(\mathcal {R}\mathcal {G}'={ \hspace{0.0pt}\mathcal {M} \big |_{[{12}]\cup \{(i_0,j_0)\}} }\) is an extension of \(\mathcal {R}\mathcal {G}\) whose covectors \({ \hspace{0.0pt}U' \big |_{[{12}]\cup \{(i_0,j_0)\}} }\) and \({ \hspace{0.0pt}X' \big |_{[{12}]\cup \{(i_0,j_0)\}} }\) contradict the special property of \(\mathcal {R}\mathcal {G}\). \(\square \)

## 5 Lattices of Flats of Sweep Oriented Matroids

### 5.1 Dilworth Sweep Oriented Matroids

It is also interesting to understand the underlying (unoriented) matroid \(\underline{{\mathcal {M}}^{\textsf {sw}}}\) associated to a sweep oriented matroid \({\mathcal {M}}^{\textsf {sw}}\). In particular, because it plays an essential role in the enumeration of sweeps [[17][28], Sec. 4.6]. In the realizable case, this was done by Edelman [[32][41]] and Stanley [[80][42]], who showed that, under certain genericity constraint, \(\underline{{\mathcal {M}}^{\textsf {sw}}}\) can be obtained from \(\underline{{\mathcal {M}}^{\textsf {lit}}}\) via the operation of *Dilworth truncation*.

We will work directly with the axiomatic of (unoriented) matroids in terms of *geometric lattices*of flats, which was already mentioned in Sect. [4.2][147]. We refer to [[86][160]] for a comprehensive reference on (unoriented) matroids.

Recall that if \(\mathcal {M}\) is an oriented matroid on ground set *E*, a *flat*of \(\mathcal {M}\) is a subset \(F\subseteq E\) that is the zero-set of a covector of \(\mathcal {M}\) (there is \(X\in \mathcal {M}\) such that \(F=\{e\in E \, |\, X_e=0\}\)). The set \(\mathcal {F}_{\mathcal {M}}\) of all flats of \(\mathcal {M}\), ordered by inclusion, has the special structure of a *geometric lattice*; that is, a finite atomistic semimodular lattice. If \(\mathcal {M}\) has no loop, its minimal element is \(\emptyset \). (Note that this order is reversed from the order on the covectors in the face lattice of \(\mathcal {M}\).) Conversely, any geometric lattice can be seen as the lattice of flats of a matroid. Let \(S \subseteq E\). There is only one minimal flat *F*that contains *S*. The *rank*of *S*is the length of any maximal chain from \(\emptyset \) to *F*in \(\mathcal {F}_{\mathcal {M}}\). It is denoted \({{\,\textrm{rk}\,}}_{\mathcal {M}}(S)\), or \({{\,\textrm{rk}\,}}_{\underline{\mathcal {M}}}(S)\). The rank function satisfies the *submodular inequality*:

$$\begin{aligned} {{\,\textrm{rk}\,}}_{\mathcal {M}}(A)+{{\,\textrm{rk}\,}}_{\mathcal {M}}(B)\ge {{\,\textrm{rk}\,}}_{\mathcal {M}}(A\cap B)+{{\,\textrm{rk}\,}}_{\mathcal {M}}(A\cup B). \end{aligned}$$

The flats and the rank function give two cryptomorphic ways to define the underlying (unoriented) matroid \(\underline{\mathcal {M}}\) of the oriented matroid \(\mathcal {M}\). If \(\underline{\mathcal {M}}({{\varvec{{V}}}})\) is the matroid associated to a real vector configuration \({\varvec{{V}}}=(\varvec{v}_1, \ldots , \varvec{v}_n)\), the flats correspond to the sets of vectors in a same linear subspace and the rank of \(S\subseteq E\) is the dimension of the linear subspace generated by \(\{\varvec{v}_i \, |\, i\in S\}\).

The flats of the braid arrangement \(\mathcal {B}_{{n}}\) are in correspondence with the (unordered) partitions of \([{n}]\), and the lattice of flats of \(\mathcal {B}_{{n}}\) is just the lattice of partitions of \([{n}]\). Similarly, each flat of a sweep oriented matroid can be associated to a partition, and the sweeps corresponding to orderings of this partition correspond to the covectors with this zero-pattern.

We will need the oriented and unoriented notions of weak maps, which are the matroidal version of perturbing a configuration to a more special position. If \(\mathcal {M}\) and \(\mathcal {M}'\) are two oriented matroids on the same ground set *E*, we say that there is a *weak map*from \(\mathcal {M}\) to \(\mathcal {M}'\) if for every covector \(X \in \mathcal {M}'\), there is a covector \(Y \in \mathcal {M}\) such that \(X \preceq Y\). Note that every strong map is also a weak map, but not the other way round (the definition of strong maps is given in Sect. [3.3][132]). If \(\underline{\mathcal {M}}\) and \(\underline{\mathcal {M}}'\) are two unoriented matroids on the same ground set *E*, we say that there is a *weak map*from \(\underline{\mathcal {M}}\) to \(\underline{\mathcal {M}}'\) if for any subset \(F\subseteq E\) we have \({{\,\textrm{rk}\,}}_{\underline{\mathcal {M}}'}(F)\le {{\,\textrm{rk}\,}}_{\underline{\mathcal {M}}}(F)\). Note that a weak map between oriented matroids induces a weak map on the underlying unoriented matroids (cf. [[17][28], Cor. 7.7.7]).

The idea behind the Dilworth truncation is the following: if \(\mathcal {F}\) is a geometric lattice and we remove the elements of rank 1, we obtain a poset \(\mathcal {F}'\) that is not necessarily a geometric lattice. The most generic way to augment it with all the joins needed to fulfill the semimodularity condition gives rise to a matroid called the *first Dilworth truncation*of \(\mathcal {F}\). The construction works in more generality when the elements of rank \(\le k\) are removed, giving rise to the *k*th Dilworth truncation, but we will not need it in such generality ([[29][67]], see also [[22][66]]).

### Definition 5.1

[[22][66], Prop. 7.7.5] Let \(\underline{\mathcal {M}}\) be a matroid on ground set *E*. The *first Dilworth truncation*of \(\underline{\mathcal {M}}\), denoted \(D_1(\underline{\mathcal {M}})\), is defined on the ground set \(\left( {\begin{array}{c}E\\ 2\end{array}}\right) \) and its rank function is given by:

$$\begin{aligned} {{\,\textrm{rk}\,}}_{D_1(\underline{\mathcal {M}})}(\emptyset )&=0,\\ {{\,\textrm{rk}\,}}_{D_1(\underline{\mathcal {M}})}(F)&= \min _{S\in \mathcal {S}\left( F\right) } r_{S}(F)&\text {for } \emptyset \ne F \subseteq \left( {\begin{array}{c}E\\ 2\end{array}}\right) , \end{aligned}$$

where \(\mathcal {S}\left( F\right) \) is the set of (unordered) partitions \(S=\{F_1, \ldots , F_l\}\) of *F*( \(F=F_1\cup \cdots \cup F_l\), \(F_k\ne \emptyset \) for all \(k\in [l]\), and \(F_k\cap F_h=\emptyset \) for all \(k\ne h\)) and \(r_{S}(F)=\big (\sum _{k=1}^l {{\,\textrm{rk}\,}}_{\underline{\mathcal {M}}}(\bigcup \{i, j\, |\, (i,j)\in F_k\})\big ) -l\).

The flats of rank 1 of \(D_1(\underline{\mathcal {M}})\) are exactly the flats of rank 2 (i.e. the lines) of \(\underline{\mathcal {M}}\). As noted by Brylawski [[22][66]] and Mason [[61][161], Sec. 2.1], in the realizable case the Dilworth truncation can be geometrically realized by intersecting all the lines of \(\underline{\mathcal {M}}\) with a generic affine hyperplane. If \(\varvec{A}\) is generic enough (in the sense that incomparable flats spanned by its subsets are never parallel), then the hyperplane at infinity fulfills this genericity condition and \(\underline{{\mathcal {M}}^{\textsf {sw}}}({\bar{\varvec{A}}})\) is the first Dilworth truncation of \(\underline{{\mathcal {M}}^{\textsf {lit}}}({\bar{\varvec{A}}})\). Otherwise, we only get a weak map of \(D_1(\underline{{\mathcal {M}}^{\textsf {lit}}}({\bar{\varvec{A}}}))\), as \(\underline{{\mathcal {M}}^{\textsf {sw}}}({\bar{\varvec{A}}})\) will be in less general position. This result extends to (not necessary realizable) sweep oriented matroids.

### Theorem 5.2

Let \(\mathcal {M}\) be a sweep oriented matroid on \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). Then there is a weak map from \(D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})\) to \(\underline{\mathcal {M}}\).

The proof needs an auxiliary lemma.

### Lemma 5.3

Let \({\mathcal {M}}^{\textsf {lit}}\) be the little oriented matroid of the sweep oriented matroid \(\mathcal {M}\). If *I*is a flat of \({\mathcal {M}}^{\textsf {lit}}\) of rank at least two, and *J*is the minimal flat in \(\mathcal {M}\) that contains \(\left\{ (i,j) \;\big |\; i,j\in I \right\} \), then \({{\,\textrm{rk}\,}}_{\mathcal {M}}(J)= {{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I)-1\).

### Proof

Let \(I'= \{ (i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \;\big |\; i,j\in I \}\). Then \({ \hspace{0.0pt}\mathcal {M} \big |_{I'} }\) is a sweep oriented matroid with little oriented matroid \({ \hspace{0.0pt}{\mathcal {M}}^{\textsf {lit}} \big |_{I} }\), and their respective ranks are \({{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I)-1\) and \({{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I)\) by Lemma [4.4][57]. Therefore, \({{\,\textrm{rk}\,}}_{\mathcal {M}}(J)={{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I)-1\), because the rank function of a restriction is just the restriction of the rank function, see [[22][66], Prop 7.3.1]. \(\square \)

### Proof of Theorem5.2

We want to show that \({{\,\textrm{rk}\,}}_{\mathcal {M}}(G) \le {{\,\textrm{rk}\,}}_{D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})}(G)\) for every \(G\subseteq \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). Let *F*be a minimal flat of \(D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})\) that contains *G*, so that \({{\,\textrm{rk}\,}}_{D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})}(F)={{\,\textrm{rk}\,}}_{D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})}(G)\). Then there exists an unordered partition \(\{I_1, \ldots , I_l\}\) of a subset of \([{n}]\) into flats of \({\mathcal {M}}^{\textsf {lit}}\) of rank at least two such that \(F=\bigsqcup _{k=1}^l \left\{ (i,j) \;\big |\; i,j\in I_k \right\} \) and \({{\,\textrm{rk}\,}}_{D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})}(F)=\sum _{k=1}^l ({{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_k) -1)\).

Indeed, let \(S=\{F_1,\dots ,F_l\}\) be a partition of *F*that minimizes \(r_{S}(F)\), and let \(I_k=\bigcup \left\{ i,j \;\big |\; (i,j)\in F_k \right\} \). The submodular inequality shows that \({{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_1\cup I_2) -1\le {{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_1) + {{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_1) -2\) whenever \(I_1\cap I_2\ne \emptyset \). We can therefore assume that the \(I_k\) ’s are disjoint. Moreover, these parts \(I_k\) have to be flats of \({\mathcal {M}}^{\textsf {lit}}\). Otherwise, if there was some \(e\notin I_k\) such that \({{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_k)={{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_k\cup \{e\})\), then we could add to *F*all the pairs (*i*, *e*) and (*e*, *i*) with \(i\in I_k\) without augmenting its rank, but *F*was taken to be a flat.

Let \(J_k\) be the minimal flat in \(\mathcal {M}\) that contains \(\left\{ (i,j) \;\big |\; i,j\in I_k \right\} \); and let *J*be the join of all the \(J_k\) in the lattice of flats of \(\mathcal {M}\). The submodularity of geometric lattices implies that \({{\,\textrm{rk}\,}}_{\mathcal {M}}(J)\le \sum _{k=1}^l {{\,\textrm{rk}\,}}_{\mathcal {M}}(J_k)\). Moreover, such a *J*contains all the \(J_k\), hence it contains *F*, which contains *G*; and therefore \({{\,\textrm{rk}\,}}_{\mathcal {M}}(G) \le {{\,\textrm{rk}\,}}_{\mathcal {M}}(J)\). We conclude by Lemma [5.3][162], that implies that for any *k*, \({{\,\textrm{rk}\,}}_{\mathcal {M}}(J_k)={{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_k)-1\). \(\square \)

In view of this result, we will say that a sweep oriented matroid \(\mathcal {M}\) is *Dilworth*if the weak map predicted by Theorem [5.2][65] is actually an equality and we have \(\underline{\mathcal {M}}=D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})\).

This is the case if for any flat *F*of \(\mathcal {M}\) associated to a partition \(I=(I_1, \ldots , I_l)\) we have

$$\begin{aligned} {{\,\textrm{rk}\,}}_{\mathcal {M}}(F) =\left( \sum _{k=1}^l {{\,\textrm{rk}\,}}_{{\mathcal {M}}^{\textsf {lit}}}(I_k)\right) -l. \end{aligned}$$

(6)

In other words, coplanarities in \(\mathcal {M}\) are induced by coplanarities in \({\mathcal {M}}^{\textsf {lit}}\). For sweep oriented matroids that come from a point configuration, it prevents the case where some subspaces spanned by disjoint subsets of points are parallel.

Note that Dilworth sweep oriented matroids provide an oriented version of the matroid operation of Dilworth truncation. However, contrary to the unoriented case, such a truncation is often not unique and may even not exist, as shown by Theorem [4.13][68].

Even if Theorem [5.2][65] only works at the level of unoriented matroids, we expect that a stronger statement holds at the level of oriented matroids. The following conjecture is true for sweep oriented matroids of rank 2 (by [[17][28], Thm. 6.3.3]), and for sweep oriented matroids arising from point configurations (it suffices to make a generic projective perturbation that removes unwanted parallelisms).

### Conjecture 5.4

For any sweep oriented matroid \(\mathcal {M}\) there is a Dilworth sweep oriented matroid \(\mathcal {M}'\) such that there is a weak map from \(\mathcal {M}'\) to \(\mathcal {M}\), and \(\mathcal {M}\) and \(\mathcal {M}'\) have the same little oriented matroid.

### 5.2 Bounds on the Number of Sweep Permutations

One motivation for studying the lattice of flats of an oriented matroid is that it completely determines its *f*-vector, as shown by the celebrated Las Vergnas-Zaslavsky Theorem [[17][28], Thm 4.6.4].

### Theorem 5.5

The number of topes of an oriented matroid \(\mathcal {M}\) only depends on its lattice of flats \(\mathcal {F}\). More precisely, this number is:

$$\begin{aligned}(-1)^r\chi _{\mathcal {F}}(-1),\end{aligned}$$

where *r*is the rank of \(\mathcal {M}\), and \(\chi _{\mathcal {F}}\) is the characteristic polynomial of \(\mathcal {F}\).

We can therefore adapt [[32][41], Thm. 3.4], Footnote 3 and [[80][42], Thm. 7] to oriented matroids. As noted by Stanley in [[80][42]], for fixed *r*the bound is a polynomial in *n*of degree \(2(r-1)\).

### Theorem 5.6

Let \(\mathcal {M}\) be a sweep oriented matroid on \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) of rank *r*. Then its number of sweep permutations is bounded from above by:

$$\begin{aligned} \left| \Pi ({\mathcal {M}})\right| \le \sum _{i=0}^{\lfloor \frac{r-1}{2}\rfloor } 2 c(n, n-r+1+2i), \end{aligned}$$

where the \(c(n,n-i)\) are the unsigned Stirling numbers of the first kind.

The equality is obtained for example for realizable sweep oriented matroids that come from generic configurations of *n*points in \({{\mathbb {R}}}^{r-1}\).

### Proof

We demonstrate how the proof of [[32][41], Thm. 3.4] and [[80][42], Thm. 7] extends to our set-up. We repeat the main ideas for the reader’s convenience and refer to these references for more details. We denote by \({\mathcal {G}^{r}_{n}}\) the geometric lattice obtained by removing all elements of rank greater than *r*from the Boolean lattice on \([{n}]\) and adding a top element. This is the lattice of flats of any generic point configuration of *n*points in \({{\mathbb {R}}}^{r-1}\). The computation and evaluation of the characteristic polynomial of \(D_1({\mathcal {G}^{r}_{n}})\) gives the right hand side of the inequality (see [[32][41], Co. 3.2]), which is the number of topes of any oriented matroid whose lattice of flats is \(D_1({\mathcal {G}^{r}_{n}})\) via Theorem [5.5][163]. This is the case for the sweep oriented matroids arising from generic configurations.

By [[58][164], Cor. 9.3.7], it suffices to show that there is a weak map from \(D_1({\mathcal {G}^{r}_{n}})\) to \(\underline{\mathcal {M}}\), because this implies that the coefficients of the characteristic polynomial of \(\underline{\mathcal {M}}\) are bounded by those of the characteristic polynomial of \(D_1({\mathcal {G}^{r}_{n}})\). Note that for any subset \(F\subseteq [{n}]\), we have \({{\,\textrm{rk}\,}}_{{\mathcal {G}^{r}_{n}}}(F)=\min (|F|, r)\). Like in any matroid, \(\underline{{\mathcal {M}}^{\textsf {lit}}}\) satisfies \({{\,\textrm{rk}\,}}_{\underline{{\mathcal {M}}^{\textsf {lit}}}}(F)\le |F|\), and hence there is a weak map from \({\mathcal {G}^{r}_{n}}\) to \(\underline{{\mathcal {M}}^{\textsf {lit}}}\). It follows from Definition [5.1][165] of the Dilworth truncation by its rank function that this induces a weak map from \(D_1({\mathcal {G}^{r}_{n}})\) to \(D_1(\underline{{\mathcal {M}}^{\textsf {lit}}})\). It follows from Theorem [5.2][65] that there is a weak map from \(D_1({\mathcal {G}^{r}_{n}})\) to \(\underline{\mathcal {M}}\). \(\square \)

## 6 Pseudo-sweeps

Even if the little oriented matroid does not change, the poset of sweeps of a point configuration is not invariant under admissible projective transformations (in the sense of [[89][21], App. 2.6]). In this section we describe a larger poset, the *poset of pseudo-sweeps*, that contains the sweeps with respect to all possible choices of “hyperplane at infinity”. It is a poset of cellular strings, and as such it can be defined at the level of oriented matroids. Thus it exists even for those oriented matroids that are not little oriented matroids of any sweep oriented matroid.

### 6.1 Pseudo-sweeps

With the presentation of \(\varvec{SP}({\varvec{A}})\) as a monotone path polytope introduced in Sect. [2.3.3][166], we know that sweep permutations of a point configuration \(\varvec{A}\) can be interpreted as coherent monotone paths of the zonotope \(\varvec{Z}({\bar{\varvec{A}}})\) with respect to a linear form (which we called the height). Non-coherent monotone paths also give rise to permutations of the elements of \(\varvec{A}\), which we will call *pseudo-sweep permutations*. They can be read in terms of *k*-sets. A *k*-*set*of \(\varvec{A}\) is a *k*-element subset \(\varvec{S}\subseteq \varvec{A}\) for which there is an affine hyperplane strictly separating \(\varvec{S}\) from \(\varvec{A}\smallsetminus \varvec{S}\). See [[62][167], Ch. 11] for background.

For simplicity, assume that \(\varvec{A}=(\varvec{a}_1,\dots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) does not contain repeated points. A *pseudo-sweep permutation*of \(\varvec{A}\) is a permutation \(\sigma \in \mathfrak {S}_{n}\) such that \(\left\{ \varvec{a}_{\sigma (i)} \;\big |\; 1\le i \le k \right\} \) is a *k*-set for all \(1\le k\le n\). Note that we are still sweeping with a hyperplane, although we are allowed to slightly change its direction every time the hyperplane hits a point, as long as the new hyperplane does not cross one of the already visited points.

This point of view can be extended to obtain ordered partitions (and lift the constraint of not having repeated points). Consider a sequence of affine functionals \(\gamma _r(\varvec{x})=\left\langle \varvec{u}_r \, , \, \varvec{x} \right\rangle -c_r\) for \(1\le r \le m\) such that for each point \(\varvec{a}_i\in \varvec{A}\) there is an *r*with \(\gamma _r(\varvec{a}_i)= 0\), \(\gamma _s(\varvec{a}_i)> 0\) for all \(s<r\), and \(\gamma _s(\varvec{a}_i)< 0\) for all \(r<s\); and such that for each \(1\le r\le m\) there is some *i*such that \(\gamma _r(\varvec{a}_i)= 0\). The sets \(I_r=\left\{ i \;\big |\; \gamma _r(\varvec{a}_i)=0 \right\} \) with \(1\le r\le m\) form an ordered partition of \([{n}]\), which we call a *pseudo-sweep*of \(\varvec{A}\).

There is another way to interpret pseudo-sweeps of \(\varvec{A}\) and monotone paths/cellular strings of \(\varvec{Z}({\bar{\varvec{A}}})\) in terms of hyperplane arrangements, which extends to oriented matroids.

A *gallery*of a hyperplane arrangement (without parallels) is a sequence of chambers (topes) such that adjacent chambers are separated by exactly one hyperplane. More generally, a *gallery*of an oriented matroid is a collection of topes \(T^0,\dots ,T^{m+1}\) such that \(S({T^i},{T^{i+1}})\) is a parallelism class for all *i*. A gallery is *minimal*if no parallelism class is crossed twice. We will work with acyclic oriented matroids and we will be interested in their minimal galleries from \(\varvec{+}_{n}\) to its opposite \(\varvec{-}_{n}\).

This definition can be relaxed to accept paths that go accross some covectors (other than subtopes). A *cellular string*of \(\mathcal {M}\) with respect to \(\varvec{+}_{n}\) is a sequence of non-tope covectors \((X^1,\dots , X^m)\) that are such that \(X^1\circ \varvec{+}_{n}=\varvec{+}_{n}\), \(X^m\circ \varvec{-}_{n}=\varvec{-}_{n}\), and \(X^i\circ \varvec{-}_{n}=X^{i+1}\circ \varvec{+}_{n}\) for all *i*. This notation is consistent with the notion of cellular string for a polytope with respect to a linear functional given in Sect. [2.3.3][166]. Indeed, for a hyperplane arrangement which is the normal fan of a zonotope \(\varvec{Z}\), its cellular strings are equivalent to the cellular strings of \(\varvec{Z}\) with respect to a linear functional that is minimized at the vertex corresponding to \(\varvec{+}_{n}\). (Minimal galleries are in correspondence with monotone paths.)

Note that an allowable sequence is just a cellular string on the braid arrangement based at the tope indexed by the permutation \({{\,\textrm{id}\,}}=(1,2,\dots ,n)\), and that its galleries correspond to simple allowable sequences.

**Fig. 11**

[image: Fig. 11]

[Full size image][168]

The hyperplane arrangement \(\mathcal {H}_{\bar{\varvec{B}_2}}\). To depict the arrangement, it is intersected with the unit sphere and stereographically projected from the south pole \((0,0,-1)\). We obtain an arrangement of circles, oriented so that the positive side is the interior. Two sweeps, corresponding to the permutation \(\bar{2},{\bar{1}}, 1,2\) and the ordered partition \({\bar{2}}1,{\bar{1}}2\) are depicted; and also the pseudo-sweep that is not a sweep corresponding to the permutation \({\bar{1}},2,1,{\bar{2}}\). (This resumes the example of Fig. [7][120], where the monotone paths corresponding to these two permutations were depicted.) To represent these pseudo-sweeps, an oriented ray from the all-positive tope (containing the origin) to its opposite (at infinity) is depicted. The order in which the circles are crossed gives the corresponding permutation. If the ray meets more than one circle at the same time, then one recovers an ordered partition. Note that this gives an alternative method to construct the sweep hyperplane arrangement \(\mathcal{S}\mathcal{H}({{\varvec{B}_2}})\). Indeed, it is not hard to see that when one does this procedure (intersection of \(\mathcal {H}_{\bar{\varvec{A}}}\) with the unit sphere plus stereographic projection), the hyperplanes spanned by the origin and the intersections of all possible pairs of spheres are precisely those of \(\mathcal{S}\mathcal{H}({\varvec{A}})\). This is why, under this representation, sweeps correspond to straight rays emanating from the origin

The following lemma sums up the relations between these objects in the realizable case. It is illustrated in Fig. [11][169], where the example of \(\varvec{B}_2\) from Figs. [4][105] and [7][120] is revisited.

### Lemma 6.1

Let \(\varvec{A}=(\varvec{a}_1,\dots ,\varvec{a}_n)\in {{\mathbb {R}}}^{d\times [{n}]}\) be a point configuration; let \(\mathcal {H}_{\bar{\varvec{A}}}\) be the hyperplane arrangement in \({{\mathbb {R}}}^{d+1}\) composed of the linear hyperplanes \({\varvec{H}}_{i}=\left\{ \varvec{x}\in {{\mathbb {R}}}^{d+1} \;\big |\; \left\langle \varvec{x} \, , \, \bar{\varvec{a}}_i \right\rangle =0 \right\} \) (oriented towards \(\bar{\varvec{a}}_i\)) for \(\varvec{a}_i\in \varvec{A}\), where \(\bar{\varvec{a}}=(\varvec{a},1)\); and let \(\varvec{Z}({\bar{\varvec{A}}})= \sum _{i=1}^n [-\bar{\varvec{a}}_i, \bar{\varvec{a}}_i]\) be the associated zonotope.

There is a bijection between:

1. (i)

pseudo-sweeps of \(\varvec{A}\),

2. (ii)

cellular strings of \(\mathcal {H}_{\bar{\varvec{A}}}\) with respect to the all-positive tope \(\varvec{+}_{n}\), and

3. (iii)

\(h\) -monotone cellular strings of \(\varvec{Z}({\bar{\varvec{A}}})\) ( \(h\) -coherent subdivisions of \(h(\varvec{Z}({\bar{\varvec{A}}}))\));

and if moreover \(\varvec{A}\) does not have repeated points, then there is a bijection between:

1. (i)

pseudo-sweep permutations of \(\varvec{A}\),

2. (ii)

minimal galleries of \(\mathcal {H}_{\bar{\varvec{A}}}\) from the tope \(\varvec{+}_{n}\) to its opposite \(\varvec{-}_{n}\), and

3. (iii)

\(h\) -monotone paths of \(\varvec{Z}({\bar{\varvec{A}}})\).

### Proof

The proof amounts simply to translate between definitions (the definition of cellular strings induced by a projection was given in Sect. [2.3.3][166]). We omit the details and only give some indications.

To a sequence of affine functionals \(\gamma _r(\varvec{x})=\left\langle \varvec{u}_r \, , \, \varvec{x} \right\rangle -c_r\) for \(1\le r \le m\) such that for each point \(\varvec{a}_i\in \varvec{A}\) there is an *r*with \(\gamma _r(\varvec{a}_i)= 0\), \(\gamma _s(\varvec{a}_i)> 0\) for all \(s<r\), and \(\gamma _s(\varvec{a}_i)< 0\) for all \(r<s\); we can associate

1. (i)

the ordered partition \(I_1,\dots ,I_m\) of \([{n}]\) given by \(I_r=\left\{ i \;\big |\; \gamma _r(\varvec{a}_i)=0 \right\} \),

2. (ii)

the sequence of non-tope covectors \(X^1,\dots ,X^m\) obtained by considering the sign of evaluating \(\gamma _r\) on each of the points of \(\varvec{A}\), and

3. (iii)

the sequence \(\varvec{F}_1,\dots ,\varvec{F}_m\) of faces of \(\varvec{Z}({\bar{\varvec{A}}})\), where \(\varvec{F}_r\) is the face of \(\varvec{Z}({\bar{\varvec{A}}})\) minimized by the linear functional \(\ell _r:{{\mathbb {R}}}^{d+1}\rightarrow {{\mathbb {R}}}\) given by \((\varvec{x},x_{d+1})\mapsto \left\langle \varvec{u}_r \, , \, \varvec{x} \right\rangle -c_rx_{d+1}\).

One can easily check that the conditions imposed on \(\gamma _1,\dots ,\gamma _m\) imply that these sequences are a pseudo-sweep of \(\varvec{A}\), a cellular string of \(\mathcal {H}_{\bar{\varvec{A}}}\) with respect to the all-positive tope \(\varvec{+}_{n}\), and a \(h\) -monotone cellular string of \(\varvec{Z}({\bar{\varvec{A}}})\), respectively. And conversely, for any pseudo-sweep or cellular string of \(\mathcal {H}_{\bar{\varvec{A}}}\) or \(\varvec{Z}({\bar{\varvec{A}}})\), one can find such a sequence of affine functionals. This is direct for pseudo-sweeps and cellular strings of \(\mathcal {H}_{\bar{\varvec{A}}}\). For cellular strings \(\varvec{F}_1,\dots ,\varvec{F}_m\) of \(\varvec{Z}({\bar{\varvec{A}}})\), we associate to each face \(\varvec{F}_r\) an affine map \(\gamma _r\) obtained by restricting the linear functional minimized by \(\varvec{F}_r\) in \(\varvec{Z}({\bar{\varvec{A}}})\) to the hyperplane \(x_{d+1}=1\).

The map that associates the partition \(I_1,\dots ,I_m\) to the sequence \(X^1,\dots ,X^m\) with \((X^r)_i=0\) if \(i\in I_r\), \((X^r)_i=-\) if \(i\in I_s\) with \(s<r\) and \((X^r)_i=+\) if \(i\in I_s\) with \(s>r\), is hence a bijection between pseudo-sweeps and cellular strings of \(\mathcal {H}_{\bar{\varvec{A}}}\). And similarly the map that sends a cellular string \(X^1,\dots ,X^m\) of \(\mathcal {H}_{\bar{\varvec{A}}}\) to the cellular string \(\varvec{F}_1,\dots ,\varvec{F}_m\) of \(\varvec{Z}({\bar{\varvec{A}}})\) given by

$$\begin{aligned} \varvec{F}_r=\sum _{(X^r)_i=+}\{-\bar{\varvec{a}}_i\}+\sum _{(X^r)_i=-}\{\bar{\varvec{a}}_i\}+\sum _{(X^r)_i=0}[-\bar{\varvec{a}}_i, \bar{\varvec{a}}_i] \end{aligned}$$

is also a bijection.

The second part of the statement arises from the observation that these bijections are order-preserving. \(\square \)

In particular, we can define pseudo-sweeps of a realizable oriented matroid in terms of its cellular strings. We extend this definition to abstract oriented matroids.

### Definition 6.2

A *pseudo-sweep*of an acyclic oriented matroid \(\mathcal {M}\) is an ordered partition \((I_1,\dots , I_m)\) arising from a cellular string \((X^1,\dots ,X^m)\) of \(\mathcal {M}\) via \(I_i=S({X^i\circ \varvec{+}_{n}},{X^i\circ \varvec{-}_{n}})\), that is, \(I_i\) is the set of zeros of \(X^i\).

**Fig. 12**

[image: Fig. 12]

[Full size image][170]

The pseudo-sweeps of the point configuration \(\varvec{B}_2\). Without the trivial sweep, they index a non-pure cellular complex that retracts to the boundary of the sweep polytope \(\varvec{SP}({{\varvec{B}_2}})\) from Fig. [4][105], a 1-sphere

### Remark 6.3

If \(\varvec{A}'\) is a (full-dimensional) admissible projective transformation of \(\varvec{A}\), then any sweep of \(\varvec{A}'\) gives rise to a pseudo-sweep of \(\varvec{A}\). Indeed, under an admissible projective transformation a pencil of parallel hyperplanes is mapped into a pencil of hyperplanes containing a codimension 2 flat that does not intersect \({{\,\textrm{conv}\,}}(\varvec{A})\). The *k*-sets defined by these hyperplanes clearly give rise to a pseudo-sweep. However, not all pseudo-sweeps arise this way. For example, if \(\{\varvec{a}_1,\dots , \varvec{a}_6\}\) are the vertices of a regular hexagon in cyclic order, then [1, 2, 3, 6, 5, 4] is a pseudo-sweep permutation that is not a sweep of any of its projective transformations. (Because in every realization the vector \(\varvec{a}_6-\varvec{a}_3\) is a positive linear combination of the vectors \(\varvec{a}_1-\varvec{a}_2\) and \(\varvec{a}_5-\varvec{a}_4\).)

### Remark 6.4

(Pseudo-sweeps and shellings) One of Stanley’s motivations for studying sweep permutations in [[80][42]] is that they are in correspondence with Bruggesser–Mani line-shelling orders of polytopes [[18][20]]. For a convex polytope \(\varvec{P}\) and a line \(\ell \) through its interior, this is the order in which the facets of \(\varvec{P}\) become visible to a point following \(\ell \) from the interior of \(\varvec{P}\) to infinity, plus the order in which the remaining facets lose visibility when the point returns from the opposite side to the interior of \(\varvec{P}\) along \(\ell \). Now, let \({\varvec{P}}^\circ \) be the polar of \(\varvec{P}\) with respect to an interior point \(\varvec{p}\) of \(\varvec{P}\), and let \(\ell \) be a line through \(\varvec{p}\). (Here, we are considering the usual projective polarity, as in [[62][167], Sec. 5.1], but after a translation by \(-\varvec{p}\).) Since \(\ell \) contains \(\varvec{p}\), which is mapped to the hyperplane at infinity by polarity, the set of points in \(\ell \) corresponds to a family of parallel affine hyperplanes orthogonal to a common direction. The shelling order given by \(\ell \) coincides with the sweep permutation of the vertices of \({\varvec{P}}^\circ \) with respect to this direction. Thus, sweep permutations of a point configuration in convex position are in bijection with line shelling orders of the polar polyhedron for lines that go through the center of polarity (here, the origin, which is the image of the hyperplane at infinity).

Actually, not only sweeps, but all pseudo-sweeps, give rise to shelling orders. And this is true in the more general level of oriented matroids. Indeed, every pseudo-sweep of \(\mathcal {M}\) induces a shelling order of the (Edmonds-Mandel) face lattice of the tope \(\varvec{+}_{n}\) [[36][171], Sec. 3.VI], see also [[17][28], Sec. 4.3]. (To the best of our knowledge, it is still an open problem whether the opposite of this lattice, called the Las Vergnas face lattice, is shellable.) Pseudo-sweep shellings have been recently rediscovered by Heaton and Samper in the special case of matroid polytopes under the name of *broken line shellings*[[56][172]].

### 6.2 The Poset of Pseudo-sweeps and the Generalized Baues Problem

Just like sweeps, pseudo-sweeps can be naturally ordered by refinement. We denote by \(\widetilde{\Pi }({\mathcal {M},T})\) the poset of pseudo-sweeps of \(\mathcal {M}\). Topological properties of this poset have been studied in the context of a special case of the *generalized Baues problem*(GBP) of Billera and Sturmfels [[23][48]] concerning the homotopy of the poset of subdivisions induced by a projection of polytopes; see [[71][78]] for a nice survey. We recall that by the topology of a poset *P*we mean the topology of its *order complex*\(\Delta \left( P\right) \): the simplicial complex whose simplices are the chains of *P*(see [[14][100]] or [[17][28], Sec. 4.7]).

Billera, Kapranov and Sturmfels [[16][47], Thm. 2.3] showed that the strong version of the GBP, as considered in [[71][78], Q. 2.3], holds for monotone paths of polytopes. This implies that, in the realizable case, the poset of sweeps of a point configuration is a deformation retract of the poset of pseudo-sweeps. For the case of zonotopes, Björner [[13][70], Thm. 2] gave an alternative combinatorial proof for the weak version of the GBP (in the sense of [[71][78], Q. 2.2]) that extends to oriented matroids. Namely, he proved that the poset of pseudo-sweeps of an oriented matroid is homotopy equivalent to a sphere (once the trivial sweep \(([{n}])\) is removed). A further generalization to shellable CW-spheres, for an appropriate definition of cellular strings induced by shellings, was proven in [[2][79]].

### Theorem 6.5

([[13][70], Thm. 2]) The poset of pseudo-sweeps of an oriented matroid \(\mathcal {M}\) of rank *r*with respect to a tope *T*without the trivial sweep has the homotopy type of an \((r-2)\) -sphere.

Note that, by Corollary [3.9][173], for oriented matroids that admit a sweep oriented matroid (in the sense that they are the little oriented matroid of some sweep oriented matroid) the poset of sweeps is an explicit \((r-2)\) -sphere embedded in the poset of pseudo-sweeps. We will show that it is in fact a deformation retract; thus proving the strong GBP for cellular strings of little oriented matroids. In the realizable case, this holds by [[16][47], Thm. 2.3]. In the more general case, Björner also remarks that he expects the poset of pseudo-sweeps to retract to a subcomplex homeomorphic to a \((r-2)\) -sphere [[13][70], below Thm. 2], but does not provide a candidate subcomplex.

### Theorem 6.6

Let \({\mathcal {M}}^{\textsf {lit}}\) be the little oriented matroid of a sweep oriented matroid \({\mathcal {M}}^{\textsf {sw}}\). Then the poset of sweeps of \({\mathcal {M}}^{\textsf {sw}}\) is a strong deformation retract of the poset of pseudo-sweeps of \({\mathcal {M}}^{\textsf {lit}}\); and the poset of non-trivial sweeps is a strong deformation retract of the poset of non-trivial pseudo-sweeps.

The proof of Theorem [6.6][80] needs some auxiliary results concerning (combinatorial) homotopy theorems. We refer to [[14][100]] for a very good introduction to the topic. First, we present a result that allows us to weaken the statement to prove, as a consequence of the fact that the *homotopy extension property*holds for order complexes of subposets (c.f. [[53][174], Ch. 0]). Then we recall three results on the homotopy type of posets: the Carrier Lemma, Quillen’s Fiber Theorem and Babson’s Lemma (the last two being corollaries of the first one). Next, inspired by [[2][79]], we use the function that returns the first part of an ordered partition to show the contractibility of some subsets of pseudo-sweeps and sweeps, thanks to Babson’s Lemma. Finally, we combine all these results to prove that the inclusion induces a homotopy equivalence.

The first result that we need shows that it suffices to prove a weaker statement, namely that the inclusion is a homotopy equivalence. A *CW pair*of a cell complex (such as a simplicial complex) is a pair (*X*, *A*) consisting of a cell complex *X*and a subcomplex *A*. In particular, if *S*is a subposet of *P*, then \((\Delta \left( P\right) ,\Delta \left( S\right) )\) is a CW pair.

### Lemma 6.7

([[53][174], Prop. 0.16 and Cor. 0.20]) If (*X*, *A*) is a CW pair and the inclusion \(A\hookrightarrow X\) is a homotopy equivalence, then *A*is a strong deformation retract of *X*.

We will use the following version of the Carrier Lemma, from [[14][100]]. For a simplicial complex \(\Delta \) and a space *T*, let \(C:\Delta \rightarrow 2^T\) be an order-preserving map ( \(C(\sigma )\subseteq C(\tau )\) for all \(\sigma \subseteq \tau \)). A mapping \(f:\left\Vert \Delta \right\Vert \rightarrow T\) is *carried*by *C*if \(f(\left\Vert \sigma \right\Vert )\subseteq C(\sigma )\) for all \(\sigma \in \Delta \), where \(\left\Vert \cdot \right\Vert \) denotes the associated geometric realization of the simplicial complex.

### Lemma 6.8

(Carrier Lemma [[14][100], Lem. 10.1]) Let \(C:\Delta \rightarrow 2^T\) be an order-preserving map such that \(C(\sigma )\) is contractible for all \(\sigma \in \Delta \). If \(f,g:\left\Vert \Delta \right\Vert \rightarrow T\) are both carried by *C*, then *f*and *g*are homotopy equivalent, \(f\sim g\).

We will also need Quillen’s Fiber Theorem [[70][175]]. For a poset *Q*and \(x\in Q\), let \(Q_{\ge x}=\left\{ y\in Q \;\big |\; y\ge x \right\} \). For the claim about the carrier, see the proof in [[14][100], Thm. 10.5].

### Theorem 6.9

(Quillen’s Fiber Theorem [[70][175]]) Let \(f:P\rightarrow Q\) be an order-preserving map of posets. If \(f^{-1}(Q_{\ge x})\) is contractible for all \(x\in Q\), then *f*induces a homotopy equivalence between \(\Delta \left( P\right) \) and \(\Delta \left( Q\right) \) whose homotopy inverse is carried by \(C(\sigma )=f^{-1}(Q_{\ge \min \sigma })\).

For this variant of Quillen’s Fiber Theorem, known as Babson’s Lemma [[7][176], Lem. 1 in Sec. 0.4.3], see also [[82][177], Lem. 3.2].

### Lemma 6.10

(Babson’s Lemma [[7][176]]) If an order-preserving map of posets \(f: P \rightarrow Q\) fulfills

1. (i)

\(f^{-1}(x)\) is contractible for all \(x \in Q\), and

2. (ii)

\(f^{-1}(x) \cap P_{\ge y}\) is contractible for all \(x \in Q\) and \(y \in P\) with \(f(y) \le x\),

then *f*induces a homotopy equivalence between \(\Delta \left( P\right) \) and \(\Delta \left( Q\right) \).

Moreover, we will need the following lemmas certifying the contractibility of certain subsets of pseudo-sweeps and sweeps. If \(F\subseteq [{n}]\) is the zero-set of a non-negative covector *Z*of \({\mathcal {M}}^{\textsf {lit}}\), we denote by \(\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F}\) the sets of sweeps \((I_1,\dots ,I_m)\) with \(I_1\subseteq F\). Similarly, we denote by \(\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}},\varvec{+}_{n}})_{\subseteq F}\) the sets of pseudo-sweeps \((I_1,\dots ,I_m)\) with \(I_1\subseteq F\).

### Lemma 6.11

Let \(F\subseteq [{n}]\) be the zero-set of a non-negative covector *Z*of \({\mathcal {M}}^{\textsf {lit}}\), then \(\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}},\varvec{+}_{n}})_{\subseteq F}\) is contractible.

### Proof

The proof of [[2][79], Lem. 5.5] can be adapted to prove that \(\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}},\varvec{+}_{n}})_{\subseteq F}\) is contractible. First, we note that with the same proof we can make a slightly stronger statement. Namely, they define a map \(f:\omega (P, \mathcal {O}, a)\rightarrow D(P, \mathcal {O},a)\), between certain posets \(\omega (P, \mathcal {O}, a)\) and \(D(P, \mathcal {O},a)\) that we describe below, and show that it induces a homotopy equivalence. However, the exact same proof also shows that \(f:\omega (P, \mathcal {O}, a)\cap f^{-1}(I)\rightarrow I\) induces a homotopy equivalence for any order ideal (lower set) *I*of \(D(P, \mathcal {O},a)\).

To match their notations, we call *P*the poset opposite to the big face lattice of \({\mathcal {M}}^{\textsf {lit}}\) (the atoms of *P*are the topes of \({\mathcal {M}}^{\textsf {lit}}\) and its 1-skeleton is the tope graph) and \(\mathcal {O}\) the orientation of the tope graph that goes from \(\varvec{-}_{n}\) to \(\varvec{+}_{n}\). For a tope *a*, the poset \(\omega (P, \mathcal {O}, a)\) is the poset of partial cellular strings ending at *a*(i.e. sequences of non-tope covectors \((X^1,\dots , X^m)\) such that \(X^1\circ \varvec{-}_{n}=\varvec{-}_{n}\), \(X^m\circ \varvec{+}_{n}=a\), and \(X^i\circ \varvec{+}_{n}=X^{i+1}\circ \varvec{-}_{n}\) for all *i*). Therefore taking \(a=a_{max}=\varvec{+}_{n}\) we have that \(\omega (P,\mathcal {O}, a_{max})=\omega (P,\mathcal {O})\) is exactly the poset of cellular strings of \({\mathcal {M}}^{\textsf {lit}}\) with respect to \(\varvec{-}_{n}\), which is in bijection with \(\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}}, \varvec{+}_{n}})\). However, their partial order is the opposite of our refinement order and the cellular strings have to be read in reverse order. The poset \(D(P, \mathcal {O}, a)\) is the poset of the non-tope covectors *X*such that \(X\circ \varvec{+}_{n}= a\). Therefore, \(D(P, \mathcal {O}, a_{max})\) corresponds to the half-interval \([\varvec{0},\varvec{+}_{n})\) in the face lattice of \({\mathcal {M}}^{\textsf {lit}}\).

If we take *I*the lower set of \(D(P, \mathcal {O}, a_{max})\) corresponding to the interval \([Z, \varvec{+}_{n})\), their function \(f:\omega (P, \mathcal {O}, a_{max})\cap f^{-1}(I)\rightarrow I\) corresponds to the function that sends the pseudo-sweep \((I_1, \ldots , I_m) \in \widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}}, \varvec{+}_{n}})_{\subseteq F}\) to the non-negative covector \(Y\in [Z, \varvec{+}_{n})\) with zero-set \(I_1\). Hence it induces a homotopy equivalence from \(\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}},\varvec{+}_{n}})_{\subseteq F}\) to \([Z,\varvec{+}_{n})\), which has a contractible order poset because it has a unique minimal element. \(\square \)

We wish to prove the same when restricted to sweeps. For this, we use an auxiliary result from [[9][178]]. Let \(\mathcal {M}\subseteq \{+,-, 0\}^E\) be the set of covectors of an oriented matroid on *E*. Then, each element \(e\in E\) defines two *halfspaces*\(\left\{ X\in \mathcal {M} \;\big |\; X_e=+ \right\} \) and \(\left\{ X\in \mathcal {M} \;\big |\; X_e=- \right\} \), and a *hyperplane*\(\left\{ X\in \mathcal {M} \;\big |\; X_e=0 \right\} \).

### Lemma 6.12

Let \(\mathcal {M}\) be the set of covectors of an oriented matroid. Then, any non-empty intersection of one or more halfspaces and hyperplanes, seen as a subposet of the face lattice, is contractible.

### Proof

This is a consequence of [[9][178], Prop. 15]. Indeed, an intersection of halfspaces and hyperplanes is a COM, because it satisfies Face symmetry and Strong elimination, see [[9][178], Def. 1]. \(\square \)

### Lemma 6.13

Let \(F\subseteq [{n}]\) be the zero-set of a non-negative covector *Z*of \({\mathcal {M}}^{\textsf {lit}}\), then \(\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F}\) is contractible.

### Proof

Inspired by the proof of [[2][79], Lem. 5.5], we apply Babson’s Lemma [6.10][179] with the function *f*from the subposet of sweeps \(\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F}\) to the half-open interval of the face lattice \([Z,\varvec{+}_{n})\) that sends a sweep \((I_1, \ldots , I_m)\) to the non-negative covector with zero-set \(I_1\).

Let *Y*be a covector in \([Z, \varvec{+}_{n})\), with zero-set \(G\subseteq F\).

1. (i)

\(f^{-1}(Y)\) is the set of sweeps whose first part is *G*. It is not empty because *Y*must be of the form \(\tilde{Y}^1\) for a covector \(\tilde{Y}\in {\mathcal {M}}^{\textsf {sw}}\) (in the sense of Definition [4.2][139]), and such \(\tilde{Y}\) corresponds to a sweep with first part *G*. Moreover, \(f^{-1}(Y)\) is the intersection of halfspaces \(\left\{ X\in {\mathcal {M}}^{\textsf {sw}} \;\big |\; X_{(i,j)}=+ \right\} \) for all \(i\in G\), \(j\notin G\) and \(i<j\), and \(\left\{ X\in {\mathcal {M}}^{\textsf {sw}} \;\big |\; X_{(i,j)}=- \right\} \) for all \(i\in G\), \(j\notin G\) and \(i>j\). By Lemma [6.12][180] it is contractible.

2. (ii)

Let \(J=(J_1, \ldots , J_r)\) be a sweep in \(\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F}\) such that \(f(J)\le Y\), i.e. \(G\subseteq J_1\). The intersection \(f^{-1}(Y)\cap (\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F})_{\ge J}\) is the set of sweeps that refine *J*and whose first part is *G*. As for \(f^{-1}(Y)\), this set is an intersection of halfspaces. It is not empty because it contains the sweep corresponding to \(J\circ \tilde{Y}\). Hence it is contractible.

It follows from Babson’s Lemma that \(\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F}\) is homotopy equivalent to \([Z, \varvec{+}_{n})\), which has a contractible order poset because it has a unique minimal element. \(\square \)

### Proof of Theorem 6.6

To simplify the exposition, we denote by \(P=\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}},\varvec{+}_{n}})\) the poset of pseudo-sweeps of \({\mathcal {M}}^{\textsf {lit}}\) with respect to \(\varvec{+}_{n}\), by \(S=\overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})\) the poset of sweeps of \({\mathcal {M}}^{\textsf {sw}}\), and by \(Q=[\varvec{0},\varvec{+}_{n})\) the half-open interval between \(\varvec{0}\) and \(\varvec{+}_{n}\) in the face lattice of \({\mathcal {M}}^{\textsf {lit}}\) (this is its Edmonds-Mandel lattice without the top element).

By Lemma [6.7][181] it suffices to show that the inclusion map \(\iota : S\hookrightarrow P\) induces a homotopy equivalence. As in the proof of Lemmas [6.11][182] and [6.13][183], let \(f:P\rightarrow Q\) be the map that sends a pseudo-sweep \((I_1,\dots , I_m)\) to the non-negative covector with zero-set \(I_1\).

[image: figure a]

For any covector \(Z\in Q\) with zero-set *F*, we have that \((f\circ \iota )^{-1}(Q_{\ge Z})= \overline{\Pi }({{\mathcal {M}}^{\textsf {sw}}})_{\subseteq F}\), which is contractible by Lemma [6.13][183].

We conclude by Quillen’s Theorem [6.9][184] that \(f\circ \iota :S \rightarrow Q\) induces a homotopy equivalence with a homotopy inverse \(g: Q \rightarrow S\) carried by \(C(\sigma )=(f\circ \iota )^{-1}(Q_{\ge \min \sigma })\).

We will show that \(g\circ f: P \rightarrow S\) is a homotopy inverse of the inclusion map \(\iota : S \hookrightarrow P\). We trivially have that \(g\circ f \circ \iota \sim {{\,\textrm{id}\,}}_{S}\) from the fact that \((f\circ \iota )\) and *g*are homotopy inverses.

It remains to show that \(\iota \circ g \circ f\sim {{\,\textrm{id}\,}}_{P}\). Now, for \(\sigma \) in the order complex of *P*, let \(C'(\sigma )=\left\Vert f^{-1}(Q_{\ge \min f(\sigma )}) \right\Vert \). Note that \(f^{-1}(Q_{\ge \min f(\sigma )})\) is of the form \(\widetilde{\Pi }({{\mathcal {M}}^{\textsf {lit}},\varvec{+}_{n}})_{\subseteq F}\) where *F*is the first part of the smallest ordered partition in \(\sigma \). It is therefore contractible by Lemma [6.11][182]. We claim that \({{\,\textrm{id}\,}}_p\) and \(\iota \circ g \circ f\) are both carried by \(C'\), and thus that they must be homotopy equivalent by Lemma [6.8][185]. Indeed, \({{\,\textrm{id}\,}}_P\) is trivially carried by \(C'\); and so is \(\iota \circ g \circ f\) because *g*is carried by *C*.

The same proof works if we restrict to non-trivial sweeps in *S*and *P*. \(\square \)

## 7 Allowable Graphs of Permutations and Sweep Acycloids

In this section we present an alternative generalization of allowable sequences to high dimensions that is closer to the original formulation, in terms of moves between permutations. As we will see, the resulting objects naturally have the structure of acycloids, and we recover sweep oriented matroids as a special case.

### 7.1 Allowable Graphs of Permutations

In this setting it is useful to see a permutation \(\sigma \in \mathfrak {S}_{n}\) as the word \([\sigma (1), \ldots , \sigma (n)]\) on the alphabet [*n*]. A *substring*of \(\sigma \) is then a contiguous sequence of characters, of the form \([\sigma (j), \sigma (j+1), \ldots , \sigma (k)]\) for certain \(1\le j<k\le n\). Such a substring is said to be *increasing*if \(\sigma (j)< \sigma (j+1)< \ldots < \sigma (k)\).

### Definition 7.1

Let \(\Pi \subseteq \mathfrak {S}_{n}\) be a set of permutations, and \(\sigma , \sigma ' \in \Pi \). We define an *allowable sequence*in \(\Pi \) from \(\sigma \) to \(\sigma '\) as a sequence of permutations of \(\Pi \): \(\sigma = \sigma _0, \ldots , \sigma _l=\sigma '\) such that

1. (M1)

for each \(1 \le k \le l\) the *move*from \(\sigma _{k-1}\) to \(\sigma _k\) consists of reversing a set \(m_k\) of one or more disjoint substrings of \(\sigma _{k-1}\);

2. (M2)

each pair *i*, *j*is reversed at most once along the path. In other words, there is at most one move \(m_k\) such that *i*and *j*are in the same substring of \(m_k\).

A move is *simple*if it consists of a single substring of two elements; and an allowable sequence is *simple*if all its moves are.

For example, and are valid moves, the second being moreover simple. The sequence

is an allowable sequence from (1, 2, 3, 4, 5) to (3, 4, 2, 5, 1) in \(\mathfrak {S}_{5}\); whereas

is not an allowable sequence in \(\mathfrak {S}_{5}\), because the pair \(\{2, 3\}\) is reversed twice. In fact, in an allowable sequence from the identity permutation, only increasing substrings can be reversed. Note that if there is a move *m*from \(\sigma \) to \(\gamma \), then from \(\gamma \) to \(\sigma \) there is the *reverse move*\(\overline{m}\) whose substrings are \(\overline{s}=[s_k, \ldots , s_0]\) for each substring \(s=[s_0, \ldots , s_k]\) of *m*. This way, every allowable sequence can be reversed.

Another way to describe allowable sequences is by looking at the set of pairs that are reversed at each move. For a permutation \(\sigma \), we denote by \({{\,\textrm{inv}\,}}(\sigma )\) its set of inversions; that is, the set of pairs \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) such that \(i<j\) and \(\sigma (i)>\sigma (j)\). We denote by \(\,\triangle \,\) the symmetric difference operation on sets.

### Definition 7.2

If there is a move *m*from a permutation \(\sigma \) to a permutation \(\gamma \), we define the *set of inversions*of the move *m*by \({{\,\textrm{inv}\,}}_{m}\) \(={{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\gamma )\).

For example, for the move we obtain the set of inversions \(\left\{ (2,3), (4,5), (4,6), (5,6) \right\} \).

The conditions defining allowable sequences become:

1. (M1’):

if (*a*, *b*) or (*b*, *a*) is in \({{\,\textrm{inv}\,}}_{m_k}\) and (*b*, *c*) or (*c*, *b*) is in \({{\,\textrm{inv}\,}}_{m_k}\), then (*a*, *c*) or (*c*, *a*) is in \({{\,\textrm{inv}\,}}_{m_k}\);

2. (M2’):

the inversion sets \({{\,\textrm{inv}\,}}_{m_k}\) are pairwise disjoint.

Note also that \({{\,\textrm{inv}\,}}_{m}={{\,\textrm{inv}\,}}_{\overline{m}}\).

### Remark 7.3

An *allowable sequence*in the sense of Goodman and Pollack in [[44][26], 46, 47, [48][24]] is exactly what we call an allowable sequence from \({{\,\textrm{id}\,}}=(1, 2, \ldots , n)\) to \({\overline{{{\,\textrm{id}\,}}}} = (n, n-1, \ldots , 1)\) in \(\mathfrak {S}_{n}\).

We need to introduce another concept before our main definition.

### Definition 7.4

A set of permutations \(\Pi \subseteq \mathfrak {S}_{n}\) is *symmetric*if \(\overline{\sigma } \in \Pi \) for all \(\sigma \in \Pi \), where \(\overline{\sigma }\) is the *reverse*of \(\sigma \), defined by \(\sigma (t)=\overline{\sigma }(n-t+1)\) for all \(t\in [{n}]\).

### Definition 7.5

Consider a set of permutations \(\Pi \subseteq \mathfrak {S}_{n}\) and a set \(\mathcal {L}\) of moves such that:

1. (P1)

\(\Pi \) is symmetric,

2. (P2)

for any \(\sigma , \sigma ' \in \Pi \), there is an allowable sequence from \(\sigma \) to \(\sigma '\) whose moves belong to \(\mathcal {L}\),

3. (P3)

for \(m,s\in \mathcal {L}\), either \({{\,\textrm{inv}\,}}_m={{\,\textrm{inv}\,}}_s\) or \({{\,\textrm{inv}\,}}_m\cap {{\,\textrm{inv}\,}}_s=\emptyset \).

The graph with vertex set \(\Pi \) and whose edges are the pairs of permutations differing by a move in \(\mathcal {L}\) is an *allowable graph of permutations*.

An allowable graph of permutations is *simple*if \(\mathcal {L}\) consists only of simple moves.

### Lemma 7.6

The graph is completely determined by \(\Pi \) and does not depend on \(\mathcal {L}\). More precisely, \(\sigma , \sigma '\in \Pi \) form an edge if and only if there is no \(\sigma ''\in \Pi \setminus \{\sigma \}\) such that \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma '')\subsetneq {{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')\).

### Proof

Suppose that \(\sigma , \sigma '\in \Pi \) form an edge. It means that there is a move *m*in \(\mathcal {L}\) with inversion set \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')\). Suppose that \(\sigma ''\in \mathcal {L}\) satisfies \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma '')\subseteq {{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')\). For any move \(m'\) in \(\mathcal {L}\) along an allowable sequence from \(\sigma \) to \(\sigma ''\) we have \({{\,\textrm{inv}\,}}_{m'}\subseteq {{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma '')\), thus \({{\,\textrm{inv}\,}}_{m'}\cap {{\,\textrm{inv}\,}}_m\ne \emptyset \). We deduce from (P3) that \({{\,\textrm{inv}\,}}_{m'}={{\,\textrm{inv}\,}}_m\), thus \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma '')= {{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')\).

Reciprocally, suppose that \(\sigma , \sigma ' \in \Pi \) do not form an edge and let \(\sigma ''\in \Pi \setminus \{\sigma \}\) be the neighbor of \(\sigma \) on an allowable sequence from \(\sigma \) to \(\sigma '\). By (M2), we have \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma '')\subseteq {{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')\), as if there was a pair in \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ''){\setminus }{{{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')}\), then it would be reversed twice in the allowable sequence: first between \(\sigma \) and \(\sigma ''\) and later between \(\sigma ''\) and \(\sigma '\). Moreover, \(\sigma '\ne \sigma ''\) because \(\sigma \) and \(\sigma ''\) form an edge, and thus \({{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma '')\ne {{\,\textrm{inv}\,}}(\sigma )\,\triangle \,{{\,\textrm{inv}\,}}(\sigma ')\). \(\square \)

We will therefore usually identify \(\Pi \) with the corresponding allowable graph, and directly call \(\Pi \) an *allowable graph of permutations*.

### Remark 7.7

The set of moves can be recovered from the graph by gathering all moves between adjacent permutations in the graph.

### Remark 7.8

If \(\Pi \) forms an allowable graph of permutations and \(\omega \in \mathfrak {S}_{n}\), then \(\omega \circ \Pi = \left\{ \omega \circ \sigma \;\big |\; \sigma \in \Pi \right\} \) is still an allowable graph of permutations. Sometimes it is convenient to suppose that the identity permutation \({{\,\textrm{id}\,}}\) belongs to \(\Pi \), as Goodman and Pollack did, which can always be obtained by multiplying by an \(\omega \) that is the inverse of a permutation in \(\Pi \).

### Remark 7.9

Note that in the case of a simple allowable graph of permutations Condition (P3) is redundant. However, the example of Fig. [13][186] shows that it is necessary in the general case and this is why we needed to fix a set of moves in Definition [7.5][187].

In this example, a valid set of moves \(\mathcal {L}\) would necessarily contain all the moves represented with the arrows (and their reverse), which are all the singletons \(\{[i,j]\}\) for \((i,j)\in \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). However, in order to satisfy Condition (P2), \(\mathcal {L}\) also has to contain the move \(\{[1, 2], [3, 4]\}\) represented by the dashed segment joining permutations (3, 4, 5, 2, 1) and (4, 3, 5, 1, 2), since there is no other allowable sequence between these two permutations. Indeed, we can see that the edges adjacent to (3, 4, 5, 2, 1) are labeled [2, 5] and [4, 5] but those pairs should not be reversed on an allowable sequence to (4, 3, 5, 1, 2). Thus, both conditions (P3) and (P2) cannot be satisfied simultaneously.

We need to have both conditions in order to have the structure of acycloids, as stated in Theorem [7.12][82].

**Fig. 13**

[image: Fig. 13]

[Full size image][188]

Example of a set of permutations that do not satisfy the definition of allowable graph of permutations. Neither graphs with or without the dashed segment are partial cubes

### 7.2 Sweep Acycloids

Acycloids are combinatorial objects widely studied in connection with the characterization of tope sets of oriented matroids, c.f. [[41][84], [51][83]]. They are equivalent to *antipodal partial cubes*(see [[57][87]]), a concept well-studied in metric graph theory. A graph is a *partial cube*if it is (isomorphic to) an isometric subgraph of a hypercube graph, and it is *antipodal*(also called *symmetric even*[[15][189]]) if for every vertex *v*there exists exactly one vertex \({\tilde{v}}\), called the antipode of *v*, such that the distance from *v*to \({\tilde{v}}\) is larger than the distance from *v*to any neighbor of \({\tilde{v}}\).

Following [[51][83]], we introduce *acycloids*in terms of its topes, which are subsets of sign-vectors. We use the same notation for the notions of reorientation, support and parallelism classes of oriented matroids from Sect. [3.1][190], which carry on verbatim to arbitrary subsets of sign vectors.

### Definition 7.10

A collection of sign-vectors \(\mathcal {T}\subseteq \{+,-,0\}^E\) is the set of topes of an *acycloid*if and only if it satisfies the following axioms Footnote 4:

1. (T1)

\(X, Y \in \mathcal {T}\) implies \(\underline{X}=\underline{Y}\) (this set is called the *support*of the acycloid),

2. (T2)

\(X\in \mathcal {T}\) implies \(-X\in \mathcal {T}\),

3. (T3)

if \(X\ne Y \in \mathcal {T}\) then there exists \(f\in S({X},{Y})\) such that \(_{-\overline{\overline{f}}}{X}\in \mathcal {T}\).

These three axioms are satisfied by the topes of an oriented matroid but they are not sufficient; there are examples of acycloids that are not oriented matroids, see [[52][85], Sec. 7].

To describe the link between allowable graphs of permutations and acycloids, we associate a sign-vector \(X^{\sigma }\) in \(\{+,-\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) to each permutation \(\sigma \in \mathfrak {S}_{n}\) via the map ( [5][142]). For simplicity, we will sometimes implicitly identify permutations and sign-vectors when it is clear from the context. For a set of permutations \(\Pi \subseteq \mathfrak {S}_{n}\), we denote \(\mathcal {T}_\Pi =\left\{ X^{\sigma } \;\big |\; \sigma \in \Pi \right\} \subseteq \{+,-\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\).

### Lemma 7.11

Let \(\Pi \subseteq \mathfrak {S}_{n}\) form an allowable graph of permutations, and let \(\mathcal {T}_\Pi \subseteq \{+,-\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) be the set of sign-vectors associated to its permutations. Then the inversion sets of the moves in \(\mathcal {L}\) coincide with the parallelism classes of \(\mathcal {T}_\Pi \).

### Proof

First, the fact that \(\Pi \) is symmetric and the existence of a valid path between \(\sigma \) and \(\overline{\sigma }\) for any \(\sigma \in \Pi \) implies that any pair \(\{i, j\}\) is in the inversion set of at least one move in \(\mathcal {L}\), which is necessarily unique by the disjointness condition (P3). Hence, the inversion sets of the moves in \(\mathcal {L}\) define equivalence classes on the pairs \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). It is straightforward to check that these coincide with the parallelism classes of \(\mathcal {T}_\Pi \). \(\square \)

### Theorem 7.12

Let \(\Pi \subseteq \mathfrak {S}_{n}\) form an allowable graph of permutations. Then \(\mathcal {T}_\Pi \subset \{+,-,0\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) is the set of topes of an acycloid.

### Proof

The support of all the covectors is \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), and we have symmetry by definition. Hence, it suffices to verify that \(\mathcal {T}_\Pi \) satisfies the reorientation property (T3). Let \(X, Y \in \mathcal {T}_\Pi \) and \(\sigma , \gamma \in \Pi \) be the associated permutations. Let \(\sigma =\gamma _0, \ldots , \gamma _l=\gamma \) be an allowable sequence from \(\sigma \) to \(\gamma \). \(S({X},{Y})\) corresponds to the pairs reversed along this path. Let *Z*be the sign-vector associated to \(\gamma _1\) by the map ( [5][142]). Then *Z*is in \(\mathcal {T}_\Pi \) and \(Z=_{-{{\,\textrm{inv}\,}}_m}{X}\) where *m*is the move from \(\sigma \) to \(\gamma _1\). Lemma [7.11][191] shows that \({{\,\textrm{inv}\,}}_m\) is the parallelism class of any pair \(\{i,j\}\) reversed by *m*. \(\square \)

We can characterize which acycloids arise from allowable graphs of permutations. We do it in a slightly more general context.

### Definition 7.13

A *sweep acycloid*is an acycloid on the ground set \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) such that

1. (i)

its topes fulfill the transitivity condition from Lemma [3.8][144]; namely for every covector *X*and every choice of \(1\le i< j < k \le n\), the triple \((X_{(i,j)},X_{(j,k)},X_{(i,k)})\) is orthogonal to the sign vector \((+,+,-)\), and

2. (ii)

its parallelism classes verify the transitivity condition Definition [7.2][192]; namely, if \(\overline{\overline{(i,j)}}\) or \(\overline{\overline{(j,i)}}\) coincides with \(\overline{\overline{(j,k)}}\) or \(\overline{\overline{(k,j)}}\), then it also coincides with \(\overline{\overline{(i,k)}}\) or \(\overline{\overline{(k,i)}}\).

As we show in Proposition [7.15][193] below, sweep acycloids are essentially equivalent to allowable graphs of permutations. The only nuance is that sweep acycloids might have some elements outside its support, which under the map ( [5][142]) would give rise to some partitions that are not permutations. In this case, there would be pairs of elements that belong to the same part in all the partitions. However, up to merging non-singleton parts and relabeling, one can suppose that these maximal ordered partitions are permutations. We recover then an allowable graph of permutations.

These operations of merging and relabeling do not affect the tope-graphs.

### Lemma 7.14

Let \(\mathcal {T}\subseteq \{+,-,0\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) be a sweep acycloid with support \(S\subseteq \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). For \(1\le i<j\le n\), if \((i,j)\notin S\), then the restriction of \(\mathcal {T}\) to \(\left( {\begin{array}{c}{[{n}]\smallsetminus \{j\}}\\ 2\end{array}}\right) \) is a sweep acycloid with isomorphic tope-graph.

### Proof

That this restriction is a sweep acycloid is straigthforward from the definition. Moreover, from the characterization in Lemma [3.8][144] one sees that for \(X\in \mathcal {T}\) and \(k\ne i,j\), the values of *X*on the pairs (*i*, *k*) (resp. (*k*, *i*)) and (*j*, *k*) (resp. (*k*, *j*)) determine each other uniquely (the sign depending on the relative order of *i*, *j*, *k*), because \(X_{(i,j)}=0\). Therefore, there is a bijection between topes (resp. parallelism classes) of \(\mathcal {T}\) and topes (resp. parallelism classes) of the restriction. \(\square \)

If \(\mathcal {T}\) is the tope set of a sweep acycloid, we denote by \(\Pi _\mathcal {T}=\left\{ I_{X} \;\big |\; X\in \mathcal {T} \right\} \) the set of associated ordered partitions.

### Theorem 7.15

If \(\Pi \subseteq \mathfrak {S}_{n}\) forms an allowable graph of permutations, then \(\mathcal {T}_\Pi \) is the set of topes of a sweep acycloid. Conversely, if \(\mathcal {T}\) is the tope set of a sweep acycloid of full support \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), then \(\Pi _\mathcal {T}\) forms an allowable graph of permutations.

### Proof

The first claim follows directly from Theorem [7.12][82]. Indeed, the topes of the form \(X^{\sigma }\) for a permutation \(\sigma \in \mathfrak {S}_{n}\) fulfill the transitivity condition from Lemma [3.8][144] by construction. Moreover, the parallelism classes of \(\mathcal {T}_\Pi \) are the moves of \(\Pi \) by Lemma [7.11][191], and they fulfill condition Definition [7.2][192] by definition.

For the second claim, note first that \(\Pi _\mathcal {T}\) is clearly symmetric by (T2). Following Lemma [7.11][191], we set \(\mathcal {L}\) to be the moves whose inversion sets are parallelism classes of the topes. By construction, two distinct moves in this family are either disjoint, or they are reverse to each other and have the same set of inversions.

Finally, let \(\sigma _X, \sigma _Y\in \Pi _\mathcal {T}\) be the permutations associated to the topes \(X,Y\in \mathcal {T}\). We will prove that they are joined by an allowable sequence by induction on the cardinality of the symmetric difference of their inversion sets. By the reorientation property (T3), there is an element \(f\in S({X},{Y})\) such that \(Z=_{-\overline{\overline{f}}}{X}\in \mathcal {T}\). The parallelism class \(\overline{\overline{f}}\) corresponds to a move \(m\in \mathcal {L}\) such that \({{\,\textrm{inv}\,}}_{m}\subseteq {{\,\textrm{inv}\,}}_{\sigma _X}\,\triangle \,{{\,\textrm{inv}\,}}_{\sigma _Y}\). Hence, *Z*is associated to a permutation \(\sigma _Z\) such that \({{\,\textrm{inv}\,}}_{\sigma _Z}\,\triangle \,{{\,\textrm{inv}\,}}_{\sigma _Y} = ({{\,\textrm{inv}\,}}_{\sigma _X}\,\triangle \,{{\,\textrm{inv}\,}}_{\sigma _Y}) {\setminus } {{\,\textrm{inv}\,}}_{m}\). By induction there is an allowable sequence \(\sigma _Z\rightarrow \cdots \rightarrow \sigma _Y\) with labels in \(\mathcal {L}\). Note that *m*is not a label of this path because its inversion set is disjoint from \({{\,\textrm{inv}\,}}_{\sigma _Z}\,\triangle \,{{\,\textrm{inv}\,}}_{\sigma _Y}\). Then, \(\sigma _X\xrightarrow {m}\sigma _Z\rightarrow \cdots \rightarrow \sigma _Y\) is an allowable sequence from \(\sigma _X\) to \(\sigma _Y\). \(\square \)

### 7.3 Sweeps and Potential Sweeps of Sweep Acycloids

With Handa’s notation from [[52][85]], a *face*of an acycloid \(\mathcal {T}\subseteq \{+,-,0\}^E\) is a sign-vector \(X\in \{+,-,0\}^E\) such that \(X\circ T\in \mathcal {T}\) for all \(T\in \mathcal {T}\); and a *coboundary*of \(\mathcal {T}\) is a sign-vector \(X\in \{+,-,0\}^E\) that conforms to a tope (which means that there is a tope that refines it) and such that, for every \(T\in \mathcal {T}\) with \(X\circ T= T\) we have \(X\circ (-T)\in \mathcal {T}\). In the language of partial cubes, faces correspond to gated subgraphs, and coboundaries are antipodal subgraphs. In an acycloid, every gated subgraph is antipodal, which shows that every face is a coboundary (see [[57][87]] for definitions and details). In general, the converse is not true. However, if \(\mathcal {T}\) is the set of topes of an oriented matroid, then faces and coboundaries coincide, and correspond to the covectors of the oriented matroid.

Augmented with a top element, the set of faces of an acycloid forms a lattice, the *big face lattice *of the acycloid [[52][85]]. Face lattices of acycloids lack many nice properties of those of oriented matroids. In particular, they are not always graded.

We can translate these concepts to sweeps. To this end, define the *composition*\(I\circ J\) of two ordered partitions \(I=(I_1, \ldots , I_l)\) and \(J=(J_1, \ldots , J_{l'})\) of \([{n}]\) as

$$\begin{aligned} I\circ J = (I_{1, 1}, \ldots , I_{1, r_1}, \ldots , I_{l,1}, I_{l, r_l}), \end{aligned}$$

where for any \(k \in \{1, \ldots , l\}\), \((I_{k,1}, \ldots , I_{k,r_k})\) is the sequence \((I_k\cap J_1, I_k\cap J_2, \ldots , I_k\cap J_{l'})\) where the empty parts are removed. That is, the ordered partition of the elements of \(I_k\) induced by *J*.

### Definition 7.16

Let \(\Pi \subseteq \mathfrak {S}_{n}\) be an allowable graph of permutations.

-

A *sweep*of \(\Pi \) is an ordered partition *I*such that \(I\circ \sigma \in \Pi \) for all \(\sigma \in \Pi \).

-

A *potential sweep*of \(\Pi \) is an ordered partition *I*of \([{n}]\) refined by some permutation in \(\Pi \) and such that any sweep permutation \(\sigma \in \Pi \) that refines *I*satisfies \(I\circ \overline{\sigma } \in \Pi \).

### Lemma 7.17

Let \(\Pi \subseteq \mathfrak {S}_{n}\) form an allowable graph of permutations and let \(\mathcal {T}_\Pi \) be its associated sweep acycloid. Then the sweeps of \(\Pi \) are in bijection with the faces of \(\mathcal {T}_\Pi \) and the potential sweeps of \(\Pi \) are in bijection with the coboundaries of \(\mathcal {T}_\Pi \).

### Proof

We prove first the equivalence between potential sweeps and coboundaries. It is clear that \(X^{I}\) is a coboundary of \(\mathcal {T}_\Pi \) for any potential sweep *I*of \(\Pi \). Indeed, if \(\sigma \) refines *I*, it implies that \(X^{I}\) conforms to \(X^{\sigma }\), i.e. \(X^{I}\circ X^{\sigma }=X^{\sigma }\). Moreover, \(I\circ \overline{\sigma }\in \Pi \) implies that \(X^{I}\circ (-X^{\sigma })=X^{I}\circ X^{\overline{\sigma }}=X^{I\circ \overline{\sigma }}\) is in \(\mathcal {T}_\Pi \).

For the converse statement, let *Y*be a coboundary of \(\mathcal {T}_\Pi \). We need to show that it is of the form \(X^{I}\) for an ordered partition *I*of \([{n}]\). Then it is clear from the definitions that *I*is a potential sweep of \(\Pi \). Suppose that there are \(1\le i< j < k\le n\) such that \((Y_{(i,j)}, Y_{(j,k)}, Y_{(i,k)})\) is one of the forbidden patterns in Lemma [3.8][144]. Let \(\sigma \in \Pi \) be a sweep permutation such that \(Z:=Y\circ X^{\sigma }=X^{\sigma }\). We denote \(\tilde{\sigma }\) the permutation in \(\Pi \) such that \(\tilde{Z}:= Y\circ (-X^{\sigma }) = X^{\tilde{\sigma }}\). The fact that *Z*and \(\tilde{Z}\) satisfy the transitivity condition implies that the forbidden pattern of *Y*must be one of the last six ones (with two zeroes). We consider the case \((Y_{(i,j)}, Y_{(j,k)}, Y_{(i,k)})=(0,0,-)\), the other ones are similar. Then we must have \(\{(Z_{(i,j)}, Z_{(j,k)}, Z_{(i,k)}), \, (\tilde{Z}_{(i,j)}, \tilde{Z}_{(j,k)}, \tilde{Z}_{(i,k)})\} = \{(+,-,-), (-,+,-)\}\), i.e. the elements *i*, *j*, *k*are ordered *k*, *i*, *j*and *j*, *k*, *i*in \(\sigma \) and \(\tilde{\sigma }\). As a consequence of condition Definition [7.2][192], in any allowable sequence in \(\Pi \) from \(\sigma \) to \(\tilde{\sigma }\), there must be a permutation where the elements *i*, *j*, *k*are ordered *k*, *j*, *i*. Such \(\tau \) satisfies \(Y\circ X^{\tau }=X^{\tau }\). Indeed, any pair (*k*, *l*) with \(Y_{(k,l)}\ne 0\) satisfies \(Z_{(k,l)}=\tilde{Z}_{(k,l)}\), thus it cannot be reversed in an allowable sequence from \(\sigma \) to \(\tilde{\sigma }\). But then the covector \(Y\circ (-X^{\tau })\) should belong to \(\mathcal {T}_\Pi \) while it has the forbidden pattern \((+,+,-)\). We conclude that any coboundary satisfies the transitivity condition from Lemma [3.8][144].

To finish, it is clear that any sweep *I*of \(\Pi \) gives a covector \(X^{I}\in \{+,-,0\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) such that for any \(\sigma \in \Pi \), \(X^{I}\circ X^{\sigma }=X^{I\circ \sigma }\in \mathcal {T}_\Pi \), thus \(X^{I}\) is a face of \(\mathcal {T}_\Pi \). For the converse, note that any face *Y*of \(\mathcal {T}_\Pi \) is a coboundary, and hence it must be of the form \(X^{I}\) associated to a potential sweep *I*. The condition of being a face shows that this potential sweep is indeed a sweep. \(\square \)

Note in particular that the *poset of sweeps*of an allowable graph of permutations, augmented with a top element, is always a lattice, as it is isomorphic to the big face lattice of an acycloid.

### 7.4 Sweep Oriented Matroids from Sweep Acycloids and Allowable Graphs of Permutations

The set of topes of an oriented matroid is always an acycloid, but the converse statement is not true. However, the conditions in the definition of sweep acycloid guarantee that, whenever they correspond to an oriented matroid, it is a sweep oriented matroid.

Note that, for this, the transitivity condition Definition [7.2][192] on the parallelism classes of sweep acycloids is necessary. Indeed, \((+,+,+), (-,-,-), (-,+,+), (+,-,-)\) satisfy the conditions of Lemma [3.8][144] (they are orthogonal to \((+,+,-)\)) and they are the topes of an oriented matroid, but not a sweep oriented matroid. This gives an acycloid whose topes fulfill the transitivity condition from Lemma [3.8][144] and that arises from an oriented matroid, but that is not a sweep oriented matroid. However, thanks to Lemma [7.17][194], we know that the conditions on topes and subtopes in the definition of sweep acycloids extend to the whole set of covectors.

### Corollary 7.18

The set of topes of a sweep oriented matroid is a sweep acycloid. Conversely, if a sweep acycloid is the set of topes of an oriented matroid, then it is a sweep oriented matroid.

The following hierarchy summarizes our current knowledge:

### Theorem 7.19

[image: figure b]

Goodman and Pollack’s unrealizable pentagon proves that the first inclusion is strict. For the second inclusion, it is known that there are acycloids that are not oriented matroids, but we do not know of any example that has the additional structure given by the transitivity condition from Lemma [3.8][144].

Corollary [7.18][88] allows us to use characterizations of acycloids arising from oriented matroids to characterize which allowable graphs of permutations arise from sweep oriented matroids. We know three families of such characterizations, summarized in [[57][87], Cor. 7.2]. In the language of permutations, da Silva’s characterization [[31][86], Thm. 4.1] concerns sweeps and potential sweeps. Handa’s characterization is stated in terms of contractions. If \(\Pi \) is an allowable graph of permutations, and \(m\in \mathcal {L}\) is one of its moves, the *elementary contraction*\(\Pi /m\) is obtained by taking all permutations \(\gamma \in \Pi \) that are separated from another permutation of \(\Pi \) by *m*, and replacing the substring *m*by its minimal element. One obtains this way a new set of permutations on the ground set \([{n}]\smallsetminus m\cup \{\min (m)\}\). For a collection of moves \(M=\{m_1, \ldots , m_l\}\), the *contraction*\(\Pi /M\), is defined inductively by \(\Pi /M=(((\Pi /m _1)/m_2)\cdots )/m_l\). The characterization by Knauer and Marc [[57][87], Cor. 7.2] is in terms of excluded partial cube minors. This operation goes outside the scope of allowable graphs of permutations. We will hence not present its details and refer the reader to the source [[57][87]].

### Corollary 7.20

Let \(\Pi \) form an allowable graph of permutations. The following conditions are equivalent:

1. (i)

\(\Pi \) arises from a sweep oriented matroid,

2. (ii)

every potential sweep of \(\Pi \) is a sweep,

3. (iii)

all its contractions are allowable graphs of permutations,

4. (iv)

the graph is in \(\mathcal {F}(\mathcal {Q}^-)\) in the sense of [[57][87]].

These characterizations might be useful to answer the question whether all sweep acycloids are sweep oriented matroids. We have not been able to construct any counterexample, but we do not have any evidence on why the properties defining sweep acycloids should force these conditions to be satisfied.

### Question 7.21

Is every sweep acycloid an oriented matroid?

## 8 Further Directions

### 8.1 Elementary Homotopies Between Sweep Oriented Matroids

In [[39][40], [42][92]] it is proven that if an allowable sequence has two consecutive moves with disjoint support, then these can be merged into a single move and the result is still an allowable sequence; and that conversely, if a move consists of more than one disjoint substrings, these can be split into two disjoint moves. These operations induce an equivalence relation among sweep oriented matroids of rank 2 whose equivalence classes are in correspondence with the associated little oriented matroids.

Extending this result to higher rank is closely related to some of the open questions indicated in the paper. First of all, the higher analogue of the operation of merging would consist in collapsing some flats of a sweep oriented matroid to get a flat whose rank is lower than the one expected by ( [6][195]). The reverse operation would break a flat with unexpected low rank into pieces fulfilling ( [6][195]). Understanding this procedure would provide a method to prove Conjecture [5.4][196].

Even if the operations were well described, it is not clear that one could find a connectivity result analogous to that by Felsner and Weil in rank 2 [[42][92]]. Note that, even if Theorem [6.6][80] goes in this direction, as it shows that all sweep oriented matroids are homotopy equivalent in the complex of pseudo-sweeps, it is not clear that there is a way to do this where all the intermediate steps are also sweep oriented matroids.

#### 8.1.1 Are All Sweep Acycloids Oriented Matroids?

Another natural problem that is left open is Question [7.21][197], which asks whether every sweep acycloid is an oriented matroid. The answer would be very interesting in either direction. If it is affirmative, then the two categories of sweep acycloids and sweep oriented matroids would collapse into a single concept. This would make allowable graphs of permutations a useful alternative characterization of sweep oriented matroids. If, on the contrary, the answer is negative, then it would be interesting to understand the gap between the two categories.

We do not have any good reason to conjecture that every sweep acycloid is an oriented matroid, beyond the fact that we could not find any. This does not tell much, because the naive approaches to computationally generate all allowable graphs of permutations of a certain size fail badly very soon because of the rapid growth of these objects.

#### 8.1.2 Allowable Graphs in Coxeter Groups

We already saw the hyperoctahedral group \(B_n\) naturally appear before. First, in Sect. [2.2.2][149], because the permutahedron of type *B*is the sweep polytope of the crosspolytope. Then also in Example [4.5][198] to explain the supersolvability of the associated matroid. In fact, the definition of allowable graph extends naturally to any Coxeter group, specially in the simple case; namely, a *simple allowable graph of Coxeter permutations*is a symmetric set \(\Pi \) of elements of the Coxeter group, in which for every pair of elements \(w,w'\in \Pi \) there is a path from *w*to \(w'\) following a reduced decomposition of \(w^{-1} w'\). For the non-simple case one has to partition the generators into a collection of disjoint subsets to define the allowable moves.

**Fig. 14**

[image: Fig. 14]

[Full size image][199]

The first row shows a generic and a degenerate 2nd higher 5-permutahedra. The second row depicts two combinatorially different generic 3rd higher 6-permutahedra

#### 8.1.3 Higher Sweep Oriented Matroids and Permutahedra

As we saw in Sect. [5.1][157], sweep oriented matroids are closely related to the first Dilworth truncation. What about higher truncations? In the realizable case, instead of studying the intersection of the lines spanned by the points of \(\varvec{A}\) with a hyperplane (at infinity), we would study the intersection of a flat *F*of codimension *k*(playing the role of hyperplane at infinity) with every flat spanned by \(k+1\) points of \(\varvec{A}\). In [[80][42], Thm. 8], Stanley states (in the polar formulation) that for a sufficiently generic choice of the flat, this gives rise to an arrangement whose lattice of flats is the *k*th Dilworth truncation of the original arrangement. Let’s call this operation the *k*th Dilworth truncation of \(\varvec{A}\) with respect to *F*. Doing the *k*th Dilworth truncation of an standard \((n-1)\) -simplex gives rise to “higher” analogues of braid arrangements, which are the normal fans of the *k*th higher *n*-*permutahedra*. However, in comparison with the \(k=1\) case, there is no \(\mathfrak {S}_{n}\) -invariant subspace that gives a canonical choice for *F*. Indeed, different choices for *F*can give rise to different combinatorial types of hyperplane arrangements and zonotopes, even if the flats are sufficiently generic in the sense of Stanley. See Fig. [14][200] for some examples. Nevertheless, every zonotope associated to a *k*th Dilworth truncation of a point configuration still arises as the projection of some *k*th higher permutahedron.

#### 8.1.4 Which Matroids are Little Oriented Matroids?

In Sect. [4.3][201] we proved that not every oriented matroid is a little oriented matroid. This begs the question of which are the oriented matroids that are sweepable, in the sense that they can be extended to a big oriented matroid. Or, at least, to find sufficient conditions. For example, we know that realizable oriented matroids are sweepable, and also all oriented matroids of rank 3, by Theorem [4.11][158].

As shown in [[55][93]], Euclidean oriented matroids (see [[17][28], Section 10.5]) always admit topological sweepings (see Sect. [1.1][202]). Is there a relation between being Euclidean and being sweepable? Our example of non-sweepable oriented matroid in Sect. [4.3][201] is based on a well-known example of non-Euclidean oriented matroid.

## Data Availability

Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

## Notes

1.

Our definition differs slightly from that in [[17][28], Sect. 1.10] We admit parallel vectors when the configuration is not generic, whereas in [[17][28], Sect. 1.10] all parallel vectors of the form \(\varvec{a}_j-\varvec{a}_i\) are merged into a single element of the oriented matroid.

2.

This is usually presented in the context of “topological sweepings” of arrangements of pseudolines, for example in [[39][40], [42][92]]. Note that the notation in these references collides slightly with ours, see Sect. [1.1][202].

3.

There is a small typo in the statement of [[32][41], Thm. 3.4] but the correct statement can be recovered from [[32][41], Cor. 3.2] with \(d=n-k-1\).

4.

Recall that the parallelism class \(\overline{\overline{f}}\) of *f*is the set of elements \(e\in E\) such that \(X_f=X_e\) for all covectors *X*or \(X_f=-X_e\) for all covectors *X*. The reorientation \(_{-F}{X}\) is the signed vector *Z*such that \(Z_f=-X_f\) for all \(f\in F\) and \(Z_f=X_f\) otherwise. The separation set *S*(*X*, *Y*) of covectors *X*, *Y*are the elements \(e\in E\) such that \((X_e, Y_e)\in \{(+, -), (-, +)\}\).

## References

1.

Angel, O., Dauvergne, D., Holroyd, A.E., Virág, B.: The local limit of random sorting networks. Ann. Inst. Henri Poincaré Probab. Stat. **55**(1), 412–440 (2019)

[MathSciNet][203] [Google Scholar][204]

2.

Athanasiadis, C.A., Edelman, P.H., Reiner, V.: Monotone paths on polytopes. Math. Z. **235**(2), 315–334 (2000)

[MathSciNet][205] [Google Scholar][206]

3.

Alon, N., Györi, E.: The number of small semispaces of a finite set of points in the plane. J. Comb. Theory Ser. A **41**(1), 154–157 (1986)

[MathSciNet][207] [Google Scholar][208]

4.

Angel, O., Holroyd, A.E., Romik, D., Virág, B.: Random sorting networks. Adv. Math. **215**(2), 839–868 (2007)

[MathSciNet][209] [Google Scholar][210]

5.

Athanasiadis, C.A., Santos, F.: Monotone paths on zonotopes and oriented matroids. Can. J. Math. **53**(6), 1121–1140 (2001)

[MathSciNet][211] [Google Scholar][212]

6.

Andrzejak, A., Welzl, E.: In between \(k\) -sets, \(j\) -facets, and \(i\) -faces: \((i, j)\) -partitions. Discret. Comput. Geom. **29**(1), 105–131 (2003)

[MathSciNet][213] [Google Scholar][214]

7.

Babson, E.K.: A combinatorial flag space, Ph.D. thesis, Massachusetts Institute of Technology (1994)

8.

Björner, A., Brenti, F.: Combinatorics of Coxeter Groups, Graduate Texts in Mathematics, vol. 231. Springer, New York (2005)

[Google Scholar][215]

9.

Bandelt, H.-J., Chepoi, V., Knauer, K.: COMs: complexes of oriented matroids. J. Comb. Theory Ser. A **156**, 195–237 (2018)

[MathSciNet][216] [Google Scholar][217]

10.

Black, A.E., De Loera, J.A., Lütjeharms, N., Sanyal, R.: The polyhedral geometry of pivot rules and monotone paths. SIAM J. Appl. Algebra Geom. **7**(3), 623–650 (2023)

[MathSciNet][218] [Google Scholar][219]

11.

Björner, A., Edelman, P.H., Ziegler, G.M.: Hyperplane arrangements with a lattice of regions. Discret. Comput. Geom. **5**(3), 263–288 (1990)

[MathSciNet][220] [Google Scholar][221]

12.

Björner, A.: Posets, regular CW complexes and Bruhat order. Eur. J. Comb. **5**(1), 7–16 (1984)

[MathSciNet][222] [Google Scholar][223]

13.

Björner, A.: Essential chains and homotopy type of posets. Proc. Am. Math. Soc. **116**(4), 1179–1181 (1992)

[ADS][224] [MathSciNet][225] [Google Scholar][226]

14.

Björner, A.: Topological Methods, Handbook of Combinatorics, vol. 1, 2, pp. 819–1872. Elsevier Sci. B. V., Amsterdam (1995)

15.

Berman, A., Kotzig, A.: Cross-cloning and antipodal graphs. Discret. Math. **69**(2), 107–114 (1988)

[MathSciNet][227] [Google Scholar][228]

16.

Billera, L.J., Kapranov, M.M., Sturmfels, B.: Cellular strings on polytopes. Proc. Am. Math. Soc. **122**(2), 549–555 (1994)

[MathSciNet][229] [Google Scholar][230]

17.

Björner, A., Vergnas, M.L., Sturmfels, B., White, N., Ziegler, G.M.: Oriented Matroids, Encyclopedia of Mathematics and its Applications, vol. 46, 2nd edn., Cambridge University Press, Cambridge (1999)

18.

Bruggesser, H., Mani, P.: Shellable decompositions of cells and spheres. Math. Scand. **29**(2), 197–205 (1971)

[MathSciNet][231] [Google Scholar][232]

19.

Bonin, J.E.: Extending a matroid by a cocircuit. Discret. Math. **306**(8–9), 812–819 (2006)

[MathSciNet][233] [Google Scholar][234]

20.

Borgwardt, K.-H.: The simplex method, Algorithms and Combinatorics: Study and Research Texts. A Probabilistic Analysis, vol. 1. Springer, Berlin (1987)

21.

Brylawski, T.: Modular constructions for combinatorial geometries. Trans. Am. Math. Soc. **203**, 1–44 (1975)

[MathSciNet][235] [Google Scholar][236]

22.

Brylawski, T.: Constructions, Theory of Matroids, Encyclopedia Math. Appl., vol. 26, pp. 127–223. Cambridge Univ. Press, Cambridge (1986)

23.

Billera, L.J., Sturmfels, B.: Fiber polytopes. Ann. Math. **135**, 527–549 (1992)

[MathSciNet][237] [Google Scholar][238]

24.

Castillo, F., Labbé, J.-P., Liebert, J., Padrol, A., Philippe, E., Schilling, C.: An effective solution to convex 1-body \(N\) -representability (2023)

25.

Cordovil, R., Moreira, M.L.: A homotopy theorem on oriented matroids. Discret. Math. **111**(1–3), 131–136 (1993) Graph theory and combinatorics (Marseille-Luminy, 1990)

26.

Dauvergne, D.: The Archimedean limit of random sorting networks (2022)

27.

de Berg, M., Cheong, O., van Kreveld, M., Overmars, M.: Computational Geometry, Algorithms and Applications, 3rd edn. Springer, Berlin (2008)

[Google Scholar][239]

28.

Deligne, P.: Les immeubles des groupes de tresses généralisés. Invent. Math. **17**, 273–302 (1972)

[ADS][240] [MathSciNet][241] [Google Scholar][242]

29.

Dilworth, R.P.: Dependence relations in a semi-modular lattice. Duke Math. J. **11**, 575–587 (1944)

[MathSciNet][243] [Google Scholar][244]

30.

De Loera, J.A., Rambau, J., Santos, F.: Triangulations: structures for algorithms and applications. In: Algorithms and Computation in Mathematics, vol. 25, Springer, (2010)

31.

da Silva, I.P.F.: Axioms for maximal vectors of an oriented matroid: a combinatorial characterization of the regions determined by an arrangement of pseudohyperplanes. Eur. J. Comb. **16**(2), 125–145 (1995)

[MathSciNet][245] [Google Scholar][246]

32.

Edelman, P.H.: Ordering points by linear functionals, Eur. J. Comb.. **21**(1), 145–152 (2000) Combinatorics of polytopes

33.

Edelman, P., Greene, C.: Balanced tableaux. Adv. Math. **63**(1), 42–99 (1987)

[MathSciNet][247] [Google Scholar][248]

34.

Edelsbrunner, H., Guibas, L.J.: Topologically sweeping an arrangement. J. Comput. Syst. Sci. **38**(1), 165–194 (1989)

[MathSciNet][249] [Google Scholar][250]

35.

Edman, R., Jiradilok, P., Liu, G., McConville, T.: Zonotopes whose cellular strings are all coherent (2021)

36.

Edmonds, J., Mandel, A.: Topology of oriented matroids, Ph.D. Thesis of A. Mandel, Ph.D. thesis, University of Waterloo (1982)

37.

Edelsbrunner, H., O’Rourke, J., Seidel, R.: Constructing arrangements of lines and hyperplanes with applications. SIAM J. Comput. **15**(2), 341–363 (1986)

[MathSciNet][251] [Google Scholar][252]

38.

Edelsbrunner, H., Valtr, P., Welzl, E.: Cutting dense point sets in half. Discret. Comput. Geom. **17**(3), 243–255 (1997)

[MathSciNet][253] [Google Scholar][254]

39.

Felsner, S.: Geometric graphs and arrangements, Some chapters from combinatorial geometry. In: Advanced Lectures in Mathematics, Friedr. Vieweg & Sohn, Wiesbaden, (2004)

40.

Finschi, L., Fukuda, K.: Generation of oriented matroids–a graph theoretical approach. Discret. Comput. Geom. **27**(1), 117–136 (2002) (Geometric combinatorics (San Francisco, CA, 2000)

41.

Fukuda, K., Handa, K.: Antipodal graphs and oriented matroids. Discret. Math. **111**(1–3), 245–256 (1993), Graph theory and combinatorics (Marseille-Luminy, 1990)

42.

Felsner, S., Weil, H.: Sweeps, arrangements and signotopes. Discret. Appl. Math. **109**(1–2), 67–94 (2001), 14th European Workshop on Computational Geometry CG’98 (Barcelona)

43.

Felsner, S., Ziegler, G.M.: Zonotopes associated with higher Bruhat orders. Discret. Math. **241**(1–3) (2001), 301–312, Selected papers in honor of Helge Tverberg

44.

Goodman, J.E., Pollack, R.: On the combinatorial classification of nondegenerate configurations in the plane. J. Comb. Theory Ser. A **29**(2), 220–235 (1980)

[MathSciNet][255] [Google Scholar][256]

45.

Goodman, J.E., Pollack, R.: Proof of Grünbaum’s conjecture on the stretchability of certain arrangements of pseudolines. J. Comb. Theory Ser. A **29**(3), 385–390 (1980)

[Google Scholar][257]

46.

Goodman, J.E., Pollack, R.: A theorem of ordered duality. Geom. Dedicata **12**(1), 63–74 (1982)

[MathSciNet][258] [Google Scholar][259]

47.

Goodman, J.E., Pollack, R.: Semispaces of configurations, cell complexes of arrangements. J. Comb. Theory Ser. A **37**(3), 257–293 (1984)

[MathSciNet][260] [Google Scholar][261]

48.

Goodman, J.E., Pollack, R.: Allowable sequences and order types in discrete and computational geometry. In: New Trends in Discrete and Computational Geometry, Algorithms Combin., vol. 10, pp. 103–134. Springer, Berlin (1993)

49.

Gass, S., Saaty, T.: The computational algorithm for the parametric objective function. Naval Res. Logist. Quart. **2**, 39–45 (1955)

[MathSciNet][262] [Google Scholar][263]

50.

Gritzmann, P., Sturmfels, B.: Minkowski addition of polytopes: computational complexity and applications to Gröbner bases. SIAM J. Discret Math. **6**(2), 246–269 (1993)

[Google Scholar][264]

51.

Handa, K.: A characterization of oriented matroids in terms of topes. Eur. J. Comb. **11**(1), 41–45 (1990)

[MathSciNet][265] [Google Scholar][266]

52.

Handa, K.: Topes of oriented matroids and related structures. Publ. Res. Inst. Math. Sci. **29**(2), 235–266 (1993)

[MathSciNet][267] [Google Scholar][268]

53.

Hatcher, A.: Algebraic Topology. Cambridge University Press, Cambridge (2002)

[Google Scholar][269]

54.

Hoffmann, U., Merckx, K.: A universality theorem for allowable sequences with applications, Preprint, [arXiv:1801.05992][270], (2018)

55.

Hochstättler, W.: Topological sweeping in oriented matroids, Technical report [https://www.fernuni-hagen.de/MATHEMATIK/DMO/pubs/feu-dmo042-16.pdf][271] (2016)

56.

Heaton, A., Samper, J.A.: Dual matroid polytopes and internal activity of independence complexes, Preprint, [arXiv:2005.04252][272], (2020)

57.

Knauer, K., Marc, T.: On tope graphs of complexes of oriented matroids. Discret. Comput. Geom. **63**(2), 377–417 (2020)

[MathSciNet][273] [Google Scholar][274]

58.

Kung, J.P.S., Nguyen, H.Q.: Weak maps. In: Theory of Matroids, Encyclopedia Math. Appl., vol. 26, pp. 254–271. Cambridge Univ. Press, Cambridge (1986)

59.

Knuth, D.E.: The Art of Computer Programming. Sorting and Searching, vol. 3, 2nd ed., Addison-Wesley, Reading, MA (1998)

60.

Lovász, L., Vesztergombi, K., Wagner, U., Welzl, E.: Convex quadrilaterals and \(k\) -sets. In: Towards a Theory of Geometric Graphs, Contemp. Math., vol. 342, pp. 139–148. Am. Math. Soc., Providence, RI (2004)

61.

Mason, J.H.: Matroids as the study of geometrical configurations. In: Higher Combinatorics (Proc. NATO Advanced Study Inst., Berlin, 1976), NATO Adv. Study Inst. Ser., Ser. C: Math. Phys. Sci., vol. 31, pp. 133–176. Reidel, Dordrecht-Boston, MA (1977)

62.

Matoušek, J.: Lectures on Discrete Geometry, Graduate Texts in Mathematics, vol. 212. Springer, New York (2002)

[Google Scholar][275]

63.

McMullen, P.: Fibre tilings. Mathematika **50**(1-2) (2003), 1–33 (2005)

64.

Matoušek, J., Gärtner, B.: Understanding and using linear programming (universitext). Springer, Berlin (2006)

[Google Scholar][276]

65.

Mnëv, N.E.: The universality theorems on the classification problem of configuration varieties and convex polytopes varieties. In: Topology and Geometry—Rohlin Seminar, Lecture Notes in Math., vol. 1346, pp. 527–543. Springer, Berlin (1988)

66.

Manin, Y.I., Schechtman, V.V.: Arrangements of hyperplanes, higher braid groups and higher Bruhat orders. In: Algebraic Number Theory, Adv. Stud. Pure Math., vol. 17, pp. 289–308. Academic Press, Boston, MA (1989)

67.

Martínez-Sandoval, L., Padrol, A.: The convex dimension of hypergraphs and the hypersimplicial Van Kampen-Flores theorem. J. Comb. Theory Ser. B **149**, 23–51 (2021)

[MathSciNet][277] [Google Scholar][278]

68.

Perrin, R.: Sur le problème des aspects. Bull. Soc. Math. France **10**, 103–127 (1882)

[MathSciNet][279] [Google Scholar][280]

69.

Postnikov, A.: Permutohedra, associahedra, and beyond. Int. Math. Res. Not. IMRN **6**, 1026–1106 (2009)

[MathSciNet][281] [Google Scholar][282]

70.

Quillen, D.: Homotopy properties of the poset of nontrivial \(p\) -subgroups of a group. Adv. Math. **28**(2), 101–128 (1978)

[MathSciNet][283] [Google Scholar][284]

71.

Reiner, V.: The generalized Baues problem, New perspectives in algebraic combinatorics (Berkeley, CA, 1996–97), Math. Sci. Res. Inst. Publ., vol. 38, pp. 293–336. Cambridge Univ. Press, Cambridge (1999)

72.

Richter-Gebert, J.: Oriented matroids with few mutations. Discret. Comput. Geom. **10**(3), 251–269 (1993)

[MathSciNet][285] [Google Scholar][286]

73.

Reiner, V., Roichman, Y.: Diameter of graphs of reduced words and galleries. Trans. Am. Math. Soc. **365**(5), 2779–2802 (2013)

[MathSciNet][287] [Google Scholar][288]

74.

Reiner, V., Ziegler, G.M.: Coxeter-associahedra. Mathematika **41**(2), 364–393 (1994)

[Google Scholar][289]

75.

Salvetti, M.: Topology of the complement of real hyperplanes in \({ {C}}^N\). Invent. Math. **88**(3), 603–618 (1987)

[ADS][290] [MathSciNet][291] [Google Scholar][292]

76.

Snoeyink, J., Hershberger, J.: Sweeping arrangements of curves. In: Discrete and Computational Geometry (New Brunswick, NJ, 1989/1990), DIMACS Ser. Discrete Math. Theoret. Comput. Sci., vol. 6, pp. 309–349. Am. Math. Soc., Providence, RI (1991)

77.

Stanley, R.P.: Modular elements of geometric lattices. Algebra Universalis **1**, 214–217 (1971)

[MathSciNet][293] [Google Scholar][294]

78.

Stanley, R.P.: Supersolvable lattices. Algebra Universalis **2**, 197–217 (1972)

[MathSciNet][295] [Google Scholar][296]

79.

Stanley, R.P.: On the number of reduced decompositions of elements of Coxeter groups. Eur. J. Comb. **5**(4), 359–372 (1984)

[MathSciNet][297] [Google Scholar][298]

80.

Stanley, R.P.: Valid orderings of real hyperplane arrangements. Discret. Comput. Geom. **53**(4), 951–964 (2015)

[MathSciNet][299] [Google Scholar][300]

81.

Sturmfels, B.: On the Newton polytope of the resultant. J. Algebraic Comb. **3**(2), 207–236 (1994)

[MathSciNet][301] [Google Scholar][302]

82.

Sturmfels, B., Ziegler, G.M.: Extension spaces of oriented matroids. Discret. Comput. Geom. **10**(1), 23–45 (1993)

[MathSciNet][303] [Google Scholar][304]

83.

Tits, J.: Le problème des mots dans les groupes de Coxeter. In: Symposia Mathematica (INDAM. Rome, 1967/68), vol. 1, pp. 175–185. Academic Press, London (1969)

84.

Ungar, P.: \(2N\) noncollinear points determine at least \(2N\) directions. J. Comb. Theory Ser. A **33**(3), 343–347 (1982)

[MathSciNet][305] [Google Scholar][306]

85.

Welzl, E.: More on \(k\) -sets of finite sets in the plane. Discret. Comput. Geom. **1**(1), 95–100 (1986)

[MathSciNet][307] [Google Scholar][308]

86.

White, N. (ed.): Theory of Matroids, Encyclopedia of Mathematics and Its Applications, vol. 26. Cambridge University Press, Cambridge (1986)

[Google Scholar][309]

87.

Ziegler, G.M.: The face lattice of hyperplane arrangements. In: Proceedings of the Oberwolfach Meeting “Kombinatorik” (1986), vol. 73, pp. 223–238 (1989)

88.

Ziegler, G.M.: Higher Bruhat orders and cyclic hyperplane arrangements. Topology **32**(2), 259–279 (1993)

[MathSciNet][310] [Google Scholar][311]

89.

Ziegler, G.M.: Lectures on Polytopes, Graduate Texts in Mathematics, vol. 152. Springer, New York (1995)

[Google Scholar][312]

[Download references][313]

## Acknowledgements

We are very grateful to Keiichi Handa, who sent us a copy of his Ph.D. thesis manuscript. We also want to thank Raul Cordovil, Kolja Knauer, Jean-Philippe Labbé, Germain Poullot, Francisco Santos, and Raman Sanyal for their helpful comments on previous versions of this manuscript. Finally, we would like to thank the anonymous reviewers for their detailed comments and suggestions to improve our presentation.

## Funding

Open Access funding provided thanks to the CRUE-CSIC agreement with Springer Nature.

## Author information

### Authors and Affiliations

1.

Departament de Matemàtiques i Informàtica, Universitat de Barcelona, Gran Via de les Corts Catalanes 585, 08007, Barcelona, Spain

Arnau Padrol

2.

Sorbonne Université and Université de Paris, CNRS, IMJ-PRG, 75005, Paris, France

Eva Philippe

Authors

1. Arnau Padrol

[View author publications][314]

Search author on: [PubMed][315] [Google Scholar][316]

2. Eva Philippe

[View author publications][317]

Search author on: [PubMed][318] [Google Scholar][319]

### Corresponding author

Correspondence to [Arnau Padrol][320].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Supported by the project CAPPS (ANR-17-CE40-0018) of the French National Research Agency ANR, the French – Austrian project PAGCAP (ANR 21 CE48 0020 and FWF I 5788), the project PID2019-106188GB-I00 of MCIN/AEI/10.13039/501100011033, and the project CLaPPo (21.SI03.64658) of Universidad de Cantabria and Banco Santander.

## Appendices

### Appendix A. Another Fiber Polytope Construction

In this section we present another way to construct sweep polytopes as fiber polytopes. As we will see, it is strongly related to the monotone path construction we gave in Sect. [2.3.3][166].

Define the *Lawrence polytope*of a point configuration \(\varvec{A}\in {{\mathbb {R}}}^{d\times [{n}]}\) as

$$\begin{aligned} {\varvec{\Lambda }(\bar{\varvec{A}})}={{\,\textrm{conv}\,}}\left\{ \varvec{e}_i\times (-\bar{\varvec{a}}_i),\varvec{e}_i\times \bar{\varvec{a}}_i \;\big |\; i\in [{n}] \right\} \subset {{\mathbb {R}}}^{n+d+1}. \end{aligned}$$

Then the intersection of \({\varvec{\Lambda }(\bar{\varvec{A}})}\) with the subspace \(\varvec{x}_{1}=\cdots =\varvec{x}_{n}\) is a homothety of the zonotope \(\varvec{Z}({\bar{\varvec{A}}})\), and the *Cayley trick*provides a bijection between (regular) subdivisions of \({\varvec{\Lambda }(\bar{\varvec{A}})}\) and (coherent) zonotopal tilings of \(\varvec{Z}({\bar{\varvec{A}}})\), see [[30][119], Sec. 9.2]. In fact, the fiber polytopes associated to the canonical projections \(\varvec{\triangle }_{2n-1}\rightarrow {\varvec{\Lambda }(\bar{\varvec{A}})}\) and \(\varvec{\square }_{n}\rightarrow \varvec{Z}({\bar{\varvec{A}}})\) are normally equivalent [[81][321], Thm. 5.1].

Consider (the vertex set of) the standard \((n-1)\) -simplex \(\varvec{\triangle }_{n-1}\) and the 0-dimensional configuration \(\varvec{O}\in {{\mathbb {R}}}^{0\times [{n}]}\) consisting of *n*copies of a point. The chain of linear maps

[image: figure c]

Note that \(\varvec{Z}({{\varvec{\triangle }_{n-1}}})\) is just the cube \(\varvec{\square }_{n}\), and \(\varvec{Z}({{\bar{\varvec{O}}}})\) a segment, and hence \(\Sigma \left( {\varvec{Z}({{\varvec{\triangle }_{n-1}}})}, s \right) \) and \(\Sigma \left( \varvec{Z}({\bar{\varvec{A}}}),h\right) \) are the *n*-permutahedron and the sweep polytope \(\varvec{SP}({\varvec{A}})\) by Example [2.6][124] and Proposition [2.8][322], respectively.

Moreover, \({\varvec{\Lambda }({{\varvec{\triangle }_{n-1}}})}\) and \({\varvec{\Lambda }({{\bar{\varvec{O}}}})}\) are the (non-standard) \((2n-1)\) -simplex \({{\,\textrm{conv}\,}} \left\{ \varvec{e}_i\pm \varvec{e}_{i+n} \;\big |\; i\in [{n}] \right\} \) and a prism over \(\varvec{\triangle }_{n-1}\), respectively. The same proof as in [[30][119], Thm. 6.2.6] shows that \(\Sigma \left( {{\varvec{\Lambda }({{\varvec{\triangle }_{n-1}}})}},{{\,\textrm{id}\,}}\times s \right) \) is a homothety of the *n*-permutahedron embedded into \({{\mathbb {R}}}^{2n}\). By Lemma [2.7][125] we obtain that:

### Corollary A.1

The fiber polytope \(\Sigma \left( {\varvec{\Lambda }(\bar{\varvec{A}})},{{\,\textrm{id}\,}}\times h\right) \) is a homothety of the sweep polytope \(\varvec{SP}({\varvec{A}})\) embedded into \({{\mathbb {R}}}^{n+d+1}\).

### Appendix B. Proofs of Theorem [4.1][56] and Corollary [4.10][61]

We include below the technical details of the proof of Theorem [4.1][56]. We first recall the notations and the statement of the theorem.

For a covector *X*of a sweep oriented matroid, let \(p_{X}:[{n}]\rightarrow [l_X]\) be the surjection associated to the corresponding ordered partition. For each \(1\le k \le 2l_X+1\), let \(X^k\in \{+,-,0\}^{[{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) be the sign-vector:

$$\begin{aligned} {X}^k_i&= {\left\{ \begin{array}{ll} - &{}\text { if } p_X(i)\le \lfloor \frac{k-1}{2} \rfloor , \\ + &{}\text { if } p_X(i)>\lfloor \frac{k}{2} \rfloor , \\ 0 &{}\text { if } k \text { is even and } p_X(i)=\frac{k}{2}. \end{array}\right. }{} & {} \text { for }1\le i\le n;\\ {X}^k_{(i,j)}&= X_{(i,j)}{} & {} \text { for all } 1\le i < j \le n. \end{aligned}$$

### Theorem

( [4.1][56]) If \(\mathcal {M}\) is the set of covectors of a sweep oriented matroid, then

$$\begin{aligned} {\mathcal {M}}^{\textsf {big}} = \left\{ {X}^k \;\big |\; X\in \mathcal {M}, \, 1\le k\le 2l_X+1 \right\} \end{aligned}$$

is the set of covectors of an oriented matroid.

### Proof

We have to check that \(\mathcal {M}\) satisfies the axioms of Definition [3.1][153], namely:

1. (V0)

\(\varvec{0}\in {\mathcal {M}}^{\textsf {big}}\),

2. (V1)

\(X\in {\mathcal {M}}^{\textsf {big}}\) implies \(-X\in {\mathcal {M}}^{\textsf {big}}\),

3. (V2)

\(X,Y \in {\mathcal {M}}^{\textsf {big}}\) implies \(X\circ Y \in {\mathcal {M}}^{\textsf {big}}\),

4. (V3)

if \(X,Y\in {\mathcal {M}}^{\textsf {big}}\) and \(e\in S({X},{Y})\) then there exists \(Z \in {\mathcal {M}}^{\textsf {big}}\) such that \(Z_e=0\) and \(Z_f=(X\circ Y)_f\) for all \(f\notin S(X,Y)\).

(*V*0) \(\varvec{0}_{n}\in \mathcal {M}\), associated to the one part ordered partition \((\{1, 2, \ldots , n\})\). Then \((\varvec{0}_{n})^2\) is the zero vector and it is in \({\mathcal {M}}^{\textsf {big}}\).

(*V*1) Let \(X^k\) be an element of \({\mathcal {M}}^{\textsf {big}}\). Then, \(-X^k= (-X)^{2l_X+2-k}\), so it is still in \({\mathcal {M}}^{\textsf {big}}\).

(*V*2) Let \(X^k, Y^h\) be two elements of \({\mathcal {M}}^{\textsf {big}}\). Then \(X^k \circ Y^h = (X\circ Y)^t\), where \(t= 2(r_1 + \ldots + r_{\frac{k-1}{2}-1})+1\) if *k*is odd (with the same notations as in the definition of the composition between two ordered partitions), \(t=2(r_1 + \ldots + r_{\frac{k}{2}-1})+ j\) if *k*is even and *j*is the index corresponding to *h*when the elements of \(I_k\) are ordered according to *Y*(that is to say, for all \(i \in I_k\), \(p_{X\circ Y}(i)\le \lfloor \frac{t-1}{2} \rfloor \Leftrightarrow p_Y(i)\le \lfloor \frac{h-1}{2} \rfloor \) and \(p_{X\circ Y}(i)> \lfloor \frac{t}{2} \rfloor \Leftrightarrow \lfloor p_Y(i) \rfloor > \lfloor \frac{h}{2} \rfloor \)).

(*V*3) Let \(X^k, Y^h\) be two elements of \({\mathcal {M}}^{\textsf {big}}\), and \(e \in S({X^k},{Y^h})\). It remains to find \(Z\in \mathcal {M}\) and \(r \in \{1, \ldots , 2l_Z+1\}\) such that \((Z^r)_e=0\) and \((Z^r)_f=(X^k \circ Y^h)_f\) for any \(f \notin S({X^k},{Y^h})\). *e*can be of two types: \(e=(i,j)\) or \(e=i\).

In both cases, it will be convenient to define

$$\begin{aligned} E_-&=\Big \{ p \mid 1\le p \le n\text { and } \{(X^k)_p, (Y^h)_p\} \in \{ \{-,-\}, \{0,-\}\} \Big \} \\&=\Big \{p \in \{1, \ldots , n\} \setminus S({X^k},{Y^h}) \mid (X^k \circ Y^h)_p=-\Big \},\\ E_+&= \Big \{p\mid 1\le p \le n\text { and } \{(X^k)_p, (Y^h)_p\} \in \{ \{+,+\}, \{0,+\}\Big \},\\ E_0&= \Big \{p\mid 1\le p \le n\text { and } \{(X^k)_p, (Y^h)_p\} =\{0,0\}\Big \}. \end{aligned}$$

Then \(E_-\cup E_+ \cup E_0 = \{1, \ldots , n\}{\setminus } S({X^k},{Y^h})\) and part of the condition is that \((Z^r)_p=\varepsilon \) for all \(p \in E_{\varepsilon }\), \(\varepsilon \in \{-, +, 0\}\).

1. (1)

If \(e=(i,j)\), up to exchanging \(X^k\) and \(Y^h\), one can suppose that \(X_{(i,j)} = -\) and \(Y_{(i,j)}=+\). Let \(Z\in \mathcal {M}\) be given by (*V*3) on \(\mathcal {M}\). For any *r*we will have that \((Z^r)_e=0\) and \((Z^r)_f=(X^k \circ Y^h)_f\) for any \(f \notin S({X^k},{Y^h})\) of the form \(f=(p,q)\), because in that case, *f*is an index for *X*and *Y*that is not in \(S({X},{Y})\). Can we find *r*such that \((Z^r)_p=(X^k \circ Y^h)_p\) for any \( 1\le p \le n\) such that \(p \notin S({X^k},{Y^h})\)? It is sufficient to check that \(p_Z(p)<p_Z(q)\) for all \((p,q) \in E_-\times E_+\cup E_-\times E_0 \cup E_0\times E_+\) and \(p_Z(p)=p_Z(q)\) for all \((p,q) \in E_0\times E_0\). \((p,q) \in E_0\times E_0\) and \(p<q\) implies that \(X_{(p,q)}=Y_{(p,q)}=0\), hence \(Z_{(p,q)}=0\) and \(p_Z(p)=p_Z(q)\). If \(E_0\ne \emptyset \), we take \(r = 2 p_Z(q)\) for any \(q \in E_0\). Then, we treat the case \((p,q) \in E_-\times E_0\), since the case \((p,q) \in E_0\times E_+\) is similar. If \(p<q\), then \(\{(X^k)_{(p,q)}, (Y^h)_{(p,q)}\} \in \{\{+,+\}, \{+,0\}\}\) and \(Z_{(p,q)}=+\). If \(p>q\), then \(\{(X^k)_{(q,p)}, (Y^h)_{(q,p)}\} \in \{\{-,-\}, \{-,0\}\}\) and \(Z_{(q,p)}=-\). In any case, \(p_Z(p)<p_Z(q)\), thus \((Z^r)_p=-\). If \(E_0 = \emptyset \), there may be several possibilities for *r*. The same reasoning as precedently shows that for any \((p,q) \in E_-\times E_+\), \(p_Z(p)<p_Z(q)\). Hence there is at least one appropriate *r*which separates the parts that contain elements in \(E_-\) from parts that contain elements in \(E_+\).

2. (2)

If \(e=i\) for some \(1\le i \le n\), up to exchanging \(X^k\) and \(Y^h\), one can suppose that \((X^k)_{i} = -\) and \((Y^h)_{i}=+\). First, we consider the case where \(E_0=\emptyset \). We take \(Z=X\circ Y\) and \(r=2p_{X\circ Y}(i)\) (corresponding to the part of *i*in *Z*). It only remains to check that if \(p\in E_{-}\) (resp. \(E_+\)), than \((Z^r)_p=-\) (resp. \(+\)). \(p \in E_- \Rightarrow p_Y(p)<p_Y(i) \Rightarrow p_Z(p)<p_Z(i) \Rightarrow (Z^r)_p=-\), \(p \in E_+ \Rightarrow p_X(p)>p_X(i) \Rightarrow p_Z(p)>p_Z(i) \Rightarrow (Z^r)_p=+\).

If \(E_0\ne \emptyset \), let *j*be the smallest element of \(E_0\). Than \(p_X(i)<p_X(j)\) and \(p_Y(i)>p_Y(j)\), thus \((i,j) \in S({X},{Y})\). Let \(Z \in \mathcal {M}\) be given by axiom (*V*3) applied to \(\mathcal {M}\) with *X*, *Y*and (*i*, *j*). Than, for any \(k \in E_0\) other than *j*, \(Z_{(j,k)}=0\) because \(X_{(j,k)}=0\) and \(Y_{(j,k)}=0\) (resp. \(Z_{(k,j)}=0\) because \(X_{(k,j)}=0\) and \(Y_{(k,j)}=0\)), and thus \(Z_{(i,k)}=0\) (resp. \(Z_{(k,i)}=0\)), because \(Z_{(i,j)}=0\) and \(\mathcal {M}\) satisfies the transitivity condition from Lemma [3.8][144]. We choose \(r=2p_{Z}(i)\) (corresponding to the part of *Z*that contains *i*and all \(k\in E_0\)). Then:

$$\begin{aligned} p \in E_-{} & {} {\Rightarrow }{} & {} {\left\{ \begin{array}{ll} p_X(p)<p_X(j) \\ p_Y(p)\le p_Y(j) \end{array}\right. } \text {or } {\left\{ \begin{array}{ll} p_X(p)= p_X(j) \\ p_Y(p)< p_Y(j) \end{array}\right. }{} & {} {\Rightarrow }{} & {} p_Z(p)<p_Z(j){} & {} {\Rightarrow }{} & {} (Z^r)_p=-,\\ p \in E_+{} & {} {\Rightarrow }{} & {} {\left\{ \begin{array}{ll} p_X(p)>p_X(i) \\ p_Y(p)\ge p_Y(j) \end{array}\right. } \text {or } {\left\{ \begin{array}{ll} p_X(p)=p_X(i) \\ p_Y(p)>p_Y(j) \end{array}\right. }{} & {} {\Rightarrow }{} & {} p_Z(p)>p_Z(j){} & {} {\Rightarrow }{} & {} (Z^r)_p=+. \end{aligned}$$

\(\square \)

For the proof of Corollary [4.10][61], recall that for any simple oriented matroid \(\mathcal {M}'\) on the ground set *F*, we call a *valid decoration*a couple of maps \(\delta :F\rightarrow 2^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) and \(\epsilon :\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \rightarrow \{+,-\}\) for a certain *n*, such that:

-

the decorations form a partition of \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), with empty parts accepted: \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) = \bigcup _{f\in F} \delta (f)\) with \( \delta (f)\cap \delta (f')=\emptyset \) whenever \(f\ne f'\); and

-

the covectors \(X\in \mathcal {M}\), seen as elements of \(\{+,-,0\}^{\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) }\) by considering \(X_{(i,j)}=\epsilon (i,j)X_f\) if \((i,j)\in \delta (f)\), satisfy the transitivity condition from Lemma [3.8][144].

### Corollary

( [4.10][61]) If \(\mathcal {M}'\) is a simple oriented matroid on *F*with a valid decoration \((\delta ,\epsilon )\), then \(\mathcal {M}'\) can be extended to a unique oriented matroid \(\mathcal {M}\) for which *F*is a modular hyperplane and \((\delta ,\epsilon )\) is the decoration of *F*induced by \(\mathcal {M}\).

In particular, an oriented matroid \(\mathcal {M}\) with a modular hyperplane *F*is completely determined by \({ \hspace{0.0pt}\mathcal {M} \big |_{F} }\) together with the decoration of *F*induced by \(\mathcal {M}\).

### Proof

The proof is very simple, as it relies entirely on Theorem [4.1][56], but it involves some auxiliary oriented matroids and some cumbersome notation to identify them.

With the help of the decoration, we will first add to \(\mathcal {M}'\) the elements of \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) to get a new oriented matroid \({\tilde{\mathcal {M}}}'\) on \(F\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). We do this by adding for each \(f\in F\) the parallel elements \((i,j)= \epsilon (i,j) f\) for \((i,j)\in \delta (f)\). The restriction of \({\tilde{\mathcal {M}}}'\) to \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) is a sweep oriented matroid, as it fulfills the transitivity condition from Lemma [3.8][144] by hypothesis. We want to apply Theorem [4.1][56] to find the associated big oriented matroid. While Theorem [4.1][56] is only stated to extend a matroid from \(\left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) to \([{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \), the same proof carries on almost verbatim to extend a matroid from \(F\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) to \(F\cup [{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \). We associate a family of covectors \(X^k\) on \(F\cup [{n}]\cup \left( {\begin{array}{c}[{n}]\\ 2\end{array}}\right) \) to every covector *X*of \({\tilde{\mathcal {M}}}'\) in the very same way, just ignoring the entries in *F*when generating the values for \([{n}]\) in \(X^k\). These are the covectors of an oriented matroid \({\tilde{\mathcal {M}}}\) (by the same argument as in Theorem [4.1][56]), and its restriction to \([{n}]\cup F\) is the desired oriented matroid \(\mathcal {M}\). \(\square \)

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][323].

[Reprints and permissions][324]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [325]

### Cite this article

Padrol, A., Philippe, E. Sweeps, Polytopes, Oriented Matroids, and Allowable Graphs of Permutations. *Combinatorica***44**, 63–123 (2024). https://doi.org/10.1007/s00493-023-00062-3

[Download citation][326]

-

Received: 05 January 2022

-

Revised: 13 July 2023

-

Accepted: 17 August 2023

-

Published: 23 October 2023

-

Version of record: 23 October 2023

-

Issue date: February 2024

-

DOI: https://doi.org/10.1007/s00493-023-00062-3

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Allowable sequences of permutations][327]
- [oriented matroids][328]
- [polytopes][329]
- [sweep algorithms][330]
- [monotone path polytopes][331]
- [generalized Baues problem][332]
- [permutahedra][333]

### Mathematics Subject Classification

- [52B05][334]
- [52B11][335]
- [52B12][336]
- [52B22][337]
- [52B40][338]
- [52C35][339]
- [52C40][340]
- [05B35][341]
- [06B99][342]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s00493-023-00062-3.pdf
[3]: /article/10.1007/s00493-023-00062-3/save-research?_csrf=vr3w1JzslnFOIfBvGxYXZBeMn5COsqQu
[4]: /saved-research
[5]: /journal/493
[6]: /journal/493/aims-and-scope
[7]: https://ef.msp.org/submit/combinatorica
[8]: https://link.springer.com/10.1007/s00229-021-01280-z?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/978-3-662-56039-6_14?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/978-3-031-41069-7_3?fromPaywallRec=false
[11]: /subjects/combinatorics
[12]: /subjects/combinatorial-geometry
[13]: /subjects/discrete-mathematics
[14]: /subjects/polytopes
[15]: /subjects/set-theory
[16]: /subjects/topology
[17]: /subjects/geometric-combinatorics-of-polytopes
[18]: /article/10.1007/s00493-023-00062-3#ref-CR27
[19]: /article/10.1007/s00493-023-00062-3#ref-CR64
[20]: /article/10.1007/s00493-023-00062-3#ref-CR18
[21]: /article/10.1007/s00493-023-00062-3#ref-CR89
[22]: /article/10.1007/s00493-023-00062-3/figures/1
[23]: /article/10.1007/s00493-023-00062-3#ref-CR68
[24]: /article/10.1007/s00493-023-00062-3#ref-CR48
[25]: /article/10.1007/s00493-023-00062-3#Fig1
[26]: /article/10.1007/s00493-023-00062-3#ref-CR44
[27]: /article/10.1007/s00493-023-00062-3#Fig10
[28]: /article/10.1007/s00493-023-00062-3#ref-CR17
[29]: /article/10.1007/s00493-023-00062-3#ref-CR59
[30]: /article/10.1007/s00493-023-00062-3#ref-CR33
[31]: /article/10.1007/s00493-023-00062-3#ref-CR79
[32]: /article/10.1007/s00493-023-00062-3#ref-CR1
[33]: /article/10.1007/s00493-023-00062-3#ref-CR4
[34]: /article/10.1007/s00493-023-00062-3#ref-CR26
[35]: /article/10.1007/s00493-023-00062-3#ref-CR84
[36]: /article/10.1007/s00493-023-00062-3#ref-CR45
[37]: /article/10.1007/s00493-023-00062-3#ref-CR3
[38]: /article/10.1007/s00493-023-00062-3#ref-CR60
[39]: /article/10.1007/s00493-023-00062-3#ref-CR85
[40]: /article/10.1007/s00493-023-00062-3#ref-CR39
[41]: /article/10.1007/s00493-023-00062-3#ref-CR32
[42]: /article/10.1007/s00493-023-00062-3#ref-CR80
[43]: /article/10.1007/s00493-023-00062-3#Sec10
[44]: /article/10.1007/s00493-023-00062-3#ref-CR50
[45]: /article/10.1007/s00493-023-00062-3#ref-CR65
[46]: /article/10.1007/s00493-023-00062-3#ref-CR54
[47]: /article/10.1007/s00493-023-00062-3#ref-CR16
[48]: /article/10.1007/s00493-023-00062-3#ref-CR23
[49]: /article/10.1007/s00493-023-00062-3#FPar11
[50]: /article/10.1007/s00493-023-00062-3#ref-CR10
[51]: /article/10.1007/s00493-023-00062-3#ref-CR6
[52]: /article/10.1007/s00493-023-00062-3#ref-CR38
[53]: /article/10.1007/s00493-023-00062-3#FPar10
[54]: /article/10.1007/s00493-023-00062-3#ref-CR24
[55]: /article/10.1007/s00493-023-00062-3#Sec14
[56]: /article/10.1007/s00493-023-00062-3#FPar25
[57]: /article/10.1007/s00493-023-00062-3#FPar29
[58]: /article/10.1007/s00493-023-00062-3#FPar36
[59]: /article/10.1007/s00493-023-00062-3#ref-CR77
[60]: /article/10.1007/s00493-023-00062-3#ref-CR21
[61]: /article/10.1007/s00493-023-00062-3#FPar38
[62]: /article/10.1007/s00493-023-00062-3#ref-CR19
[63]: /article/10.1007/s00493-023-00062-3#FPar50
[64]: /article/10.1007/s00493-023-00062-3#Sec22
[65]: /article/10.1007/s00493-023-00062-3#FPar44
[66]: /article/10.1007/s00493-023-00062-3#ref-CR22
[67]: /article/10.1007/s00493-023-00062-3#ref-CR29
[68]: /article/10.1007/s00493-023-00062-3#FPar41
[69]: /article/10.1007/s00493-023-00062-3#Sec25
[70]: /article/10.1007/s00493-023-00062-3#ref-CR13
[71]: /article/10.1007/s00493-023-00062-3#ref-CR35
[72]: /article/10.1007/s00493-023-00062-3#ref-CR25
[73]: /article/10.1007/s00493-023-00062-3#ref-CR83
[74]: /article/10.1007/s00493-023-00062-3#ref-CR28
[75]: /article/10.1007/s00493-023-00062-3#ref-CR75
[76]: /article/10.1007/s00493-023-00062-3#ref-CR5
[77]: /article/10.1007/s00493-023-00062-3#ref-CR73
[78]: /article/10.1007/s00493-023-00062-3#ref-CR71
[79]: /article/10.1007/s00493-023-00062-3#ref-CR2
[80]: /article/10.1007/s00493-023-00062-3#FPar58
[81]: /article/10.1007/s00493-023-00062-3#Sec28
[82]: /article/10.1007/s00493-023-00062-3#FPar83
[83]: /article/10.1007/s00493-023-00062-3#ref-CR51
[84]: /article/10.1007/s00493-023-00062-3#ref-CR41
[85]: /article/10.1007/s00493-023-00062-3#ref-CR52
[86]: /article/10.1007/s00493-023-00062-3#ref-CR31
[87]: /article/10.1007/s00493-023-00062-3#ref-CR57
[88]: /article/10.1007/s00493-023-00062-3#FPar93
[89]: /article/10.1007/s00493-023-00062-3#FPar95
[90]: /article/10.1007/s00493-023-00062-3#ref-CR34
[91]: /article/10.1007/s00493-023-00062-3#ref-CR37
[92]: /article/10.1007/s00493-023-00062-3#ref-CR42
[93]: /article/10.1007/s00493-023-00062-3#ref-CR55
[94]: /article/10.1007/s00493-023-00062-3#ref-CR66
[95]: /article/10.1007/s00493-023-00062-3#ref-CR43
[96]: /article/10.1007/s00493-023-00062-3#ref-CR88
[97]: /article/10.1007/s00493-023-00062-3#Sec4
[98]: /article/10.1007/s00493-023-00062-3#Sec18
[99]: /article/10.1007/s00493-023-00062-3#Sec33
[100]: /article/10.1007/s00493-023-00062-3#ref-CR14
[101]: /article/10.1007/s00493-023-00062-3/figures/2
[102]: /article/10.1007/s00493-023-00062-3/figures/3
[103]: /article/10.1007/s00493-023-00062-3#Fig2
[104]: /article/10.1007/s00493-023-00062-3#Fig3
[105]: /article/10.1007/s00493-023-00062-3#Fig4
[106]: /article/10.1007/s00493-023-00062-3#Fig5
[107]: /article/10.1007/s00493-023-00062-3/figures/4
[108]: /article/10.1007/s00493-023-00062-3/figures/5
[109]: /article/10.1007/s00493-023-00062-3#ref-CR8
[110]: /article/10.1007/s00493-023-00062-3#ref-CR74
[111]: /article/10.1007/s00493-023-00062-3#ref-CR87
[112]: /article/10.1007/s00493-023-00062-3#FPar1
[113]: /article/10.1007/s00493-023-00062-3#Equ2
[114]: /article/10.1007/s00493-023-00062-3#FPar3
[115]: /article/10.1007/s00493-023-00062-3#ref-CR69
[116]: /article/10.1007/s00493-023-00062-3#ref-CR67
[117]: /article/10.1007/s00493-023-00062-3#Fig6
[118]: /article/10.1007/s00493-023-00062-3/figures/6
[119]: /article/10.1007/s00493-023-00062-3#ref-CR30
[120]: /article/10.1007/s00493-023-00062-3#Fig7
[121]: /article/10.1007/s00493-023-00062-3#ref-CR20
[122]: /article/10.1007/s00493-023-00062-3#ref-CR49
[123]: /article/10.1007/s00493-023-00062-3/figures/7
[124]: /article/10.1007/s00493-023-00062-3#FPar6
[125]: /article/10.1007/s00493-023-00062-3#FPar7
[126]: /article/10.1007/s00493-023-00062-3#FPar5
[127]: /article/10.1007/s00493-023-00062-3#ref-CR63
[128]: /article/10.1007/s00493-023-00062-3#Sec39
[129]: /article/10.1007/s00493-023-00062-3#ref-CR11
[130]: /article/10.1007/s00493-023-00062-3#ref-CR40
[131]: /article/10.1007/s00493-023-00062-3/figures/8
[132]: /article/10.1007/s00493-023-00062-3#Sec17
[133]: /article/10.1007/s00493-023-00062-3#Sec19
[134]: /article/10.1007/s00493-023-00062-3#Fig9
[135]: /article/10.1007/s00493-023-00062-3/figures/9
[136]: /article/10.1007/s00493-023-00062-3#FPar27
[137]: /article/10.1007/s00493-023-00062-3#FPar17
[138]: /article/10.1007/s00493-023-00062-3#FPar15
[139]: /article/10.1007/s00493-023-00062-3#FPar26
[140]: /article/10.1007/s00493-023-00062-3#FPar14
[141]: /article/10.1007/s00493-023-00062-3#Equ3
[142]: /article/10.1007/s00493-023-00062-3#Equ5
[143]: /article/10.1007/s00493-023-00062-3#ref-CR12
[144]: /article/10.1007/s00493-023-00062-3#FPar22
[145]: /article/10.1007/s00493-023-00062-3#Sec40
[146]: /article/10.1007/s00493-023-00062-3#FPar18
[147]: /article/10.1007/s00493-023-00062-3#Sec20
[148]: /article/10.1007/s00493-023-00062-3#ref-CR78
[149]: /article/10.1007/s00493-023-00062-3#Sec8
[150]: /article/10.1007/s00493-023-00062-3#Equ4
[151]: /article/10.1007/s00493-023-00062-3/figures/10
[152]: /article/10.1007/s00493-023-00062-3#Fig8
[153]: /article/10.1007/s00493-023-00062-3#FPar13
[154]: /article/10.1007/s00493-023-00062-3#FPar34
[155]: /article/10.1007/s00493-023-00062-3#FPar32
[156]: /article/10.1007/s00493-023-00062-3#ref-CR76
[157]: /article/10.1007/s00493-023-00062-3#Sec23
[158]: /article/10.1007/s00493-023-00062-3#FPar39
[159]: /article/10.1007/s00493-023-00062-3#ref-CR72
[160]: /article/10.1007/s00493-023-00062-3#ref-CR86
[161]: /article/10.1007/s00493-023-00062-3#ref-CR61
[162]: /article/10.1007/s00493-023-00062-3#FPar45
[163]: /article/10.1007/s00493-023-00062-3#FPar49
[164]: /article/10.1007/s00493-023-00062-3#ref-CR58
[165]: /article/10.1007/s00493-023-00062-3#FPar43
[166]: /article/10.1007/s00493-023-00062-3#Sec13
[167]: /article/10.1007/s00493-023-00062-3#ref-CR62
[168]: /article/10.1007/s00493-023-00062-3/figures/11
[169]: /article/10.1007/s00493-023-00062-3#Fig11
[170]: /article/10.1007/s00493-023-00062-3/figures/12
[171]: /article/10.1007/s00493-023-00062-3#ref-CR36
[172]: /article/10.1007/s00493-023-00062-3#ref-CR56
[173]: /article/10.1007/s00493-023-00062-3#FPar24
[174]: /article/10.1007/s00493-023-00062-3#ref-CR53
[175]: /article/10.1007/s00493-023-00062-3#ref-CR70
[176]: /article/10.1007/s00493-023-00062-3#ref-CR7
[177]: /article/10.1007/s00493-023-00062-3#ref-CR82
[178]: /article/10.1007/s00493-023-00062-3#ref-CR9
[179]: /article/10.1007/s00493-023-00062-3#FPar62
[180]: /article/10.1007/s00493-023-00062-3#FPar65
[181]: /article/10.1007/s00493-023-00062-3#FPar59
[182]: /article/10.1007/s00493-023-00062-3#FPar63
[183]: /article/10.1007/s00493-023-00062-3#FPar67
[184]: /article/10.1007/s00493-023-00062-3#FPar61
[185]: /article/10.1007/s00493-023-00062-3#FPar60
[186]: /article/10.1007/s00493-023-00062-3#Fig13
[187]: /article/10.1007/s00493-023-00062-3#FPar74
[188]: /article/10.1007/s00493-023-00062-3/figures/13
[189]: /article/10.1007/s00493-023-00062-3#ref-CR15
[190]: /article/10.1007/s00493-023-00062-3#Sec15
[191]: /article/10.1007/s00493-023-00062-3#FPar81
[192]: /article/10.1007/s00493-023-00062-3#FPar71
[193]: /article/10.1007/s00493-023-00062-3#FPar88
[194]: /article/10.1007/s00493-023-00062-3#FPar91
[195]: /article/10.1007/s00493-023-00062-3#Equ6
[196]: /article/10.1007/s00493-023-00062-3#FPar48
[197]: /article/10.1007/s00493-023-00062-3#FPar96
[198]: /article/10.1007/s00493-023-00062-3#FPar31
[199]: /article/10.1007/s00493-023-00062-3/figures/14
[200]: /article/10.1007/s00493-023-00062-3#Fig14
[201]: /article/10.1007/s00493-023-00062-3#Sec21
[202]: /article/10.1007/s00493-023-00062-3#Sec2
[203]: http://www.ams.org/mathscinet-getitem?mr=3901651
[204]: http://scholar.google.com/scholar_lookup?amp;title=The%20local%20limit%20of%20random%20sorting%20networks&amp;journal=Ann.%20Inst.%20Henri%20Poincar%C3%A9%20Probab.%20Stat.&amp;volume=55&amp;issue=1&amp;pages=412-440&amp;publication_year=2019&amp;author=Angel%2CO&amp;author=Dauvergne%2CD&amp;author=Holroyd%2CAE&amp;author=Vir%C3%A1g%2CB
[205]: http://www.ams.org/mathscinet-getitem?mr=1795510
[206]: http://scholar.google.com/scholar_lookup?amp;title=Monotone%20paths%20on%20polytopes&amp;journal=Math.%20Z.&amp;volume=235&amp;issue=2&amp;pages=315-334&amp;publication_year=2000&amp;author=Athanasiadis%2CCA&amp;author=Edelman%2CPH&amp;author=Reiner%2CV
[207]: http://www.ams.org/mathscinet-getitem?mr=826945
[208]: http://scholar.google.com/scholar_lookup?amp;title=The%20number%20of%20small%20semispaces%20of%20a%20finite%20set%20of%20points%20in%20the%20plane&amp;journal=J.%20Comb.%20Theory%20Ser.%20A&amp;volume=41&amp;issue=1&amp;pages=154-157&amp;publication_year=1986&amp;author=Alon%2CN&amp;author=Gy%C3%B6ri%2CE
[209]: http://www.ams.org/mathscinet-getitem?mr=2355610
[210]: http://scholar.google.com/scholar_lookup?amp;title=Random%20sorting%20networks&amp;journal=Adv.%20Math.&amp;volume=215&amp;issue=2&amp;pages=839-868&amp;publication_year=2007&amp;author=Angel%2CO&amp;author=Holroyd%2CAE&amp;author=Romik%2CD&amp;author=Vir%C3%A1g%2CB
[211]: http://www.ams.org/mathscinet-getitem?mr=1863845
[212]: http://scholar.google.com/scholar_lookup?amp;title=Monotone%20paths%20on%20zonotopes%20and%20oriented%20matroids&amp;journal=Can.%20J.%20Math.&amp;volume=53&amp;issue=6&amp;pages=1121-1140&amp;publication_year=2001&amp;author=Athanasiadis%2CCA&amp;author=Santos%2CF
[213]: http://www.ams.org/mathscinet-getitem?mr=1946797
[214]: http://scholar.google.com/scholar_lookup?amp;title=In%20between%20%24%24k%24%24%20k%20-sets%2C%20%24%24j%24%24%20j%20-facets%2C%20and%20%24%24i%24%24%20i%20-faces%3A%20%24%24%28i%2C%20j%29%24%24%20%28%20i%20%2C%20j%20%29%20-partitions&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=29&amp;issue=1&amp;pages=105-131&amp;publication_year=2003&amp;author=Andrzejak%2CA&amp;author=Welzl%2CE
[215]: http://scholar.google.com/scholar_lookup?amp;title=Combinatorics%20of%20Coxeter%20Groups%2C%20Graduate%20Texts%20in%20Mathematics&amp;publication_year=2005&amp;author=Bj%C3%B6rner%2CA&amp;author=Brenti%2CF
[216]: http://www.ams.org/mathscinet-getitem?mr=3762108
[217]: http://scholar.google.com/scholar_lookup?amp;title=COMs%3A%20complexes%20of%20oriented%20matroids&amp;journal=J.%20Comb.%20Theory%20Ser.%20A&amp;volume=156&amp;pages=195-237&amp;publication_year=2018&amp;author=Bandelt%2CH-J&amp;author=Chepoi%2CV&amp;author=Knauer%2CK
[218]: http://www.ams.org/mathscinet-getitem?mr=4628425
[219]: http://scholar.google.com/scholar_lookup?amp;title=The%20polyhedral%20geometry%20of%20pivot%20rules%20and%20monotone%20paths&amp;journal=SIAM%20J.%20Appl.%20Algebra%20Geom.&amp;volume=7&amp;issue=3&amp;pages=623-650&amp;publication_year=2023&amp;author=Black%2CAE&amp;author=Loera%2CJA&amp;author=L%C3%BCtjeharms%2CN&amp;author=Sanyal%2CR
[220]: http://www.ams.org/mathscinet-getitem?mr=1036875
[221]: http://scholar.google.com/scholar_lookup?amp;title=Hyperplane%20arrangements%20with%20a%20lattice%20of%20regions&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=5&amp;issue=3&amp;pages=263-288&amp;publication_year=1990&amp;author=Bj%C3%B6rner%2CA&amp;author=Edelman%2CPH&amp;author=Ziegler%2CGM
[222]: http://www.ams.org/mathscinet-getitem?mr=746039
[223]: http://scholar.google.com/scholar_lookup?amp;title=Posets%2C%20regular%20CW%20complexes%20and%20Bruhat%20order&amp;journal=Eur.%20J.%20Comb.&amp;volume=5&amp;issue=1&amp;pages=7-16&amp;publication_year=1984&amp;author=Bj%C3%B6rner%2CA
[224]: http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&amp;bibcode=1992euff.book.....B
[225]: http://www.ams.org/mathscinet-getitem?mr=1140664
[226]: http://scholar.google.com/scholar_lookup?amp;title=Essential%20chains%20and%20homotopy%20type%20of%20posets&amp;journal=Proc.%20Am.%20Math.%20Soc.&amp;volume=116&amp;issue=4&amp;pages=1179-1181&amp;publication_year=1992&amp;author=Bj%C3%B6rner%2CA
[227]: http://www.ams.org/mathscinet-getitem?mr=937775
[228]: http://scholar.google.com/scholar_lookup?amp;title=Cross-cloning%20and%20antipodal%20graphs&amp;journal=Discret.%20Math.&amp;volume=69&amp;issue=2&amp;pages=107-114&amp;publication_year=1988&amp;author=Berman%2CA&amp;author=Kotzig%2CA
[229]: http://www.ams.org/mathscinet-getitem?mr=1205482
[230]: http://scholar.google.com/scholar_lookup?amp;title=Cellular%20strings%20on%20polytopes&amp;journal=Proc.%20Am.%20Math.%20Soc.&amp;volume=122&amp;issue=2&amp;pages=549-555&amp;publication_year=1994&amp;author=Billera%2CLJ&amp;author=Kapranov%2CMM&amp;author=Sturmfels%2CB
[231]: http://www.ams.org/mathscinet-getitem?mr=328944
[232]: http://scholar.google.com/scholar_lookup?amp;title=Shellable%20decompositions%20of%20cells%20and%20spheres&amp;journal=Math.%20Scand.&amp;volume=29&amp;issue=2&amp;pages=197-205&amp;publication_year=1971&amp;author=Bruggesser%2CH&amp;author=Mani%2CP
[233]: http://www.ams.org/mathscinet-getitem?mr=2234987
[234]: http://scholar.google.com/scholar_lookup?amp;title=Extending%20a%20matroid%20by%20a%20cocircuit&amp;journal=Discret.%20Math.&amp;volume=306&amp;issue=8%E2%80%939&amp;pages=812-819&amp;publication_year=2006&amp;author=Bonin%2CJE
[235]: http://www.ams.org/mathscinet-getitem?mr=357163
[236]: http://scholar.google.com/scholar_lookup?amp;title=Modular%20constructions%20for%20combinatorial%20geometries&amp;journal=Trans.%20Am.%20Math.%20Soc.&amp;volume=203&amp;pages=1-44&amp;publication_year=1975&amp;author=Brylawski%2CT
[237]: http://www.ams.org/mathscinet-getitem?mr=1166643
[238]: http://scholar.google.com/scholar_lookup?amp;title=Fiber%20polytopes&amp;journal=Ann.%20Math.&amp;volume=135&amp;pages=527-549&amp;publication_year=1992&amp;author=Billera%2CLJ&amp;author=Sturmfels%2CB
[239]: http://scholar.google.com/scholar_lookup?amp;title=Computational%20Geometry%2C%20Algorithms%20and%20Applications&amp;publication_year=2008&amp;author=Berg%2CM&amp;author=Cheong%2CO&amp;author=Kreveld%2CM&amp;author=Overmars%2CM
[240]: http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&amp;bibcode=1972InMat..17..273D
[241]: http://www.ams.org/mathscinet-getitem?mr=422673
[242]: http://scholar.google.com/scholar_lookup?amp;title=Les%20immeubles%20des%20groupes%20de%20tresses%20g%C3%A9n%C3%A9ralis%C3%A9s&amp;journal=Invent.%20Math.&amp;volume=17&amp;pages=273-302&amp;publication_year=1972&amp;author=Deligne%2CP
[243]: http://www.ams.org/mathscinet-getitem?mr=11287
[244]: http://scholar.google.com/scholar_lookup?amp;title=Dependence%20relations%20in%20a%20semi-modular%20lattice&amp;journal=Duke%20Math.%20J.&amp;volume=11&amp;pages=575-587&amp;publication_year=1944&amp;author=Dilworth%2CRP
[245]: http://www.ams.org/mathscinet-getitem?mr=1324423
[246]: http://scholar.google.com/scholar_lookup?amp;title=Axioms%20for%20maximal%20vectors%20of%20an%20oriented%20matroid%3A%20a%20combinatorial%20characterization%20of%20the%20regions%20determined%20by%20an%20arrangement%20of%20pseudohyperplanes&amp;journal=Eur.%20J.%20Comb.&amp;volume=16&amp;issue=2&amp;pages=125-145&amp;publication_year=1995&amp;author=Silva%2CIPF
[247]: http://www.ams.org/mathscinet-getitem?mr=871081
[248]: http://scholar.google.com/scholar_lookup?amp;title=Balanced%20tableaux&amp;journal=Adv.%20Math.&amp;volume=63&amp;issue=1&amp;pages=42-99&amp;publication_year=1987&amp;author=Edelman%2CP&amp;author=Greene%2CC
[249]: http://www.ams.org/mathscinet-getitem?mr=990055
[250]: http://scholar.google.com/scholar_lookup?amp;title=Topologically%20sweeping%20an%20arrangement&amp;journal=J.%20Comput.%20Syst.%20Sci.&amp;volume=38&amp;issue=1&amp;pages=165-194&amp;publication_year=1989&amp;author=Edelsbrunner%2CH&amp;author=Guibas%2CLJ
[251]: http://www.ams.org/mathscinet-getitem?mr=837588
[252]: http://scholar.google.com/scholar_lookup?amp;title=Constructing%20arrangements%20of%20lines%20and%20hyperplanes%20with%20applications&amp;journal=SIAM%20J.%20Comput.&amp;volume=15&amp;issue=2&amp;pages=341-363&amp;publication_year=1986&amp;author=Edelsbrunner%2CH&amp;author=O%E2%80%99Rourke%2CJ&amp;author=Seidel%2CR
[253]: http://www.ams.org/mathscinet-getitem?mr=1432062
[254]: http://scholar.google.com/scholar_lookup?amp;title=Cutting%20dense%20point%20sets%20in%20half&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=17&amp;issue=3&amp;pages=243-255&amp;publication_year=1997&amp;author=Edelsbrunner%2CH&amp;author=Valtr%2CP&amp;author=Welzl%2CE
[255]: http://www.ams.org/mathscinet-getitem?mr=583961
[256]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20combinatorial%20classification%20of%20nondegenerate%20configurations%20in%20the%20plane&amp;journal=J.%20Comb.%20Theory%20Ser.%20A&amp;volume=29&amp;issue=2&amp;pages=220-235&amp;publication_year=1980&amp;author=Goodman%2CJE&amp;author=Pollack%2CR
[257]: http://scholar.google.com/scholar_lookup?amp;title=Proof%20of%20Gr%C3%BCnbaum%E2%80%99s%20conjecture%20on%20the%20stretchability%20of%20certain%20arrangements%20of%20pseudolines&amp;journal=J.%20Comb.%20Theory%20Ser.%20A&amp;volume=29&amp;issue=3&amp;pages=385-390&amp;publication_year=1980&amp;author=Goodman%2CJE&amp;author=Pollack%2CR
[258]: http://www.ams.org/mathscinet-getitem?mr=645039
[259]: http://scholar.google.com/scholar_lookup?amp;title=A%20theorem%20of%20ordered%20duality&amp;journal=Geom.%20Dedicata&amp;volume=12&amp;issue=1&amp;pages=63-74&amp;publication_year=1982&amp;author=Goodman%2CJE&amp;author=Pollack%2CR
[260]: http://www.ams.org/mathscinet-getitem?mr=769218
[261]: http://scholar.google.com/scholar_lookup?amp;title=Semispaces%20of%20configurations%2C%20cell%20complexes%20of%20arrangements&amp;journal=J.%20Comb.%20Theory%20Ser.%20A&amp;volume=37&amp;issue=3&amp;pages=257-293&amp;publication_year=1984&amp;author=Goodman%2CJE&amp;author=Pollack%2CR
[262]: http://www.ams.org/mathscinet-getitem?mr=127431
[263]: http://scholar.google.com/scholar_lookup?amp;title=The%20computational%20algorithm%20for%20the%20parametric%20objective%20function&amp;journal=Naval%20Res.%20Logist.%20Quart.&amp;volume=2&amp;pages=39-45&amp;publication_year=1955&amp;author=Gass%2CS&amp;author=Saaty%2CT
[264]: http://scholar.google.com/scholar_lookup?amp;title=Minkowski%20addition%20of%20polytopes%3A%20computational%20complexity%20and%20applications%20to%20Gr%C3%B6bner%20bases&amp;journal=SIAM%20J.%20Discret%20Math.&amp;volume=6&amp;issue=2&amp;pages=246-269&amp;publication_year=1993&amp;author=Gritzmann%2CP&amp;author=Sturmfels%2CB
[265]: http://www.ams.org/mathscinet-getitem?mr=1034143
[266]: http://scholar.google.com/scholar_lookup?amp;title=A%20characterization%20of%20oriented%20matroids%20in%20terms%20of%20topes&amp;journal=Eur.%20J.%20Comb.&amp;volume=11&amp;issue=1&amp;pages=41-45&amp;publication_year=1990&amp;author=Handa%2CK
[267]: http://www.ams.org/mathscinet-getitem?mr=1211779
[268]: http://scholar.google.com/scholar_lookup?amp;title=Topes%20of%20oriented%20matroids%20and%20related%20structures&amp;journal=Publ.%20Res.%20Inst.%20Math.%20Sci.&amp;volume=29&amp;issue=2&amp;pages=235-266&amp;publication_year=1993&amp;author=Handa%2CK
[269]: http://scholar.google.com/scholar_lookup?amp;title=Algebraic%20Topology&amp;publication_year=2002&amp;author=Hatcher%2CA
[270]: https://arxiv.org/pdf/1801.05992
[271]: https://www.fernuni-hagen.de/MATHEMATIK/DMO/pubs/feu-dmo042-16.pdf
[272]: https://arxiv.org/pdf/2005.04252
[273]: http://www.ams.org/mathscinet-getitem?mr=4057443
[274]: http://scholar.google.com/scholar_lookup?amp;title=On%20tope%20graphs%20of%20complexes%20of%20oriented%20matroids&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=63&amp;issue=2&amp;pages=377-417&amp;publication_year=2020&amp;author=Knauer%2CK&amp;author=Marc%2CT
[275]: http://scholar.google.com/scholar_lookup?amp;title=Lectures%20on%20Discrete%20Geometry%2C%20Graduate%20Texts%20in%20Mathematics&amp;publication_year=2002&amp;author=Matou%C5%A1ek%2CJ
[276]: http://scholar.google.com/scholar_lookup?amp;title=Understanding%20and%20using%20linear%20programming%20%28universitext%29&amp;publication_year=2006&amp;author=Matou%C5%A1ek%2CJ&amp;author=G%C3%A4rtner%2CB
[277]: http://www.ams.org/mathscinet-getitem?mr=4203550
[278]: http://scholar.google.com/scholar_lookup?amp;title=The%20convex%20dimension%20of%20hypergraphs%20and%20the%20hypersimplicial%20Van%20Kampen-Flores%20theorem&amp;journal=J.%20Comb.%20Theory%20Ser.%20B&amp;volume=149&amp;pages=23-51&amp;publication_year=2021&amp;author=Mart%C3%ADnez-Sandoval%2CL&amp;author=Padrol%2CA
[279]: http://www.ams.org/mathscinet-getitem?mr=1503890
[280]: http://scholar.google.com/scholar_lookup?amp;title=Sur%20le%20probl%C3%A8me%20des%20aspects&amp;journal=Bull.%20Soc.%20Math.%20France&amp;volume=10&amp;pages=103-127&amp;publication_year=1882&amp;author=Perrin%2CR
[281]: http://www.ams.org/mathscinet-getitem?mr=2487491
[282]: http://scholar.google.com/scholar_lookup?amp;title=Permutohedra%2C%20associahedra%2C%20and%20beyond&amp;journal=Int.%20Math.%20Res.%20Not.%20IMRN&amp;volume=6&amp;pages=1026-1106&amp;publication_year=2009&amp;author=Postnikov%2CA
[283]: http://www.ams.org/mathscinet-getitem?mr=493916
[284]: http://scholar.google.com/scholar_lookup?amp;title=Homotopy%20properties%20of%20the%20poset%20of%20nontrivial%20%24%24p%24%24%20p%20-subgroups%20of%20a%20group&amp;journal=Adv.%20Math.&amp;volume=28&amp;issue=2&amp;pages=101-128&amp;publication_year=1978&amp;author=Quillen%2CD
[285]: http://www.ams.org/mathscinet-getitem?mr=1226979
[286]: http://scholar.google.com/scholar_lookup?amp;title=Oriented%20matroids%20with%20few%20mutations&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=10&amp;issue=3&amp;pages=251-269&amp;publication_year=1993&amp;author=Richter-Gebert%2CJ
[287]: http://www.ams.org/mathscinet-getitem?mr=3020115
[288]: http://scholar.google.com/scholar_lookup?amp;title=Diameter%20of%20graphs%20of%20reduced%20words%20and%20galleries&amp;journal=Trans.%20Am.%20Math.%20Soc.&amp;volume=365&amp;issue=5&amp;pages=2779-2802&amp;publication_year=2013&amp;author=Reiner%2CV&amp;author=Roichman%2CY
[289]: http://scholar.google.com/scholar_lookup?amp;title=&amp;journal=Coxeter-associahedra.%20Mathematika&amp;volume=41&amp;issue=2&amp;pages=364-393&amp;publication_year=1994&amp;author=Reiner%2CV&amp;author=Ziegler%2CGM
[290]: http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&amp;bibcode=1987InMat..88..603S
[291]: http://www.ams.org/mathscinet-getitem?mr=884802
[292]: http://scholar.google.com/scholar_lookup?amp;title=Topology%20of%20the%20complement%20of%20real%20hyperplanes%20in%20%24%24%7B%20%7BC%7D%7D%5EN%24%24%20C%20N&amp;journal=Invent.%20Math.&amp;volume=88&amp;issue=3&amp;pages=603-618&amp;publication_year=1987&amp;author=Salvetti%2CM
[293]: http://www.ams.org/mathscinet-getitem?mr=295976
[294]: http://scholar.google.com/scholar_lookup?amp;title=Modular%20elements%20of%20geometric%20lattices&amp;journal=Algebra%20Universalis&amp;volume=1&amp;pages=214-217&amp;publication_year=1971&amp;author=Stanley%2CRP
[295]: http://www.ams.org/mathscinet-getitem?mr=309815
[296]: http://scholar.google.com/scholar_lookup?amp;title=Supersolvable%20lattices&amp;journal=Algebra%20Universalis&amp;volume=2&amp;pages=197-217&amp;publication_year=1972&amp;author=Stanley%2CRP
[297]: http://www.ams.org/mathscinet-getitem?mr=782057
[298]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20reduced%20decompositions%20of%20elements%20of%20Coxeter%20groups&amp;journal=Eur.%20J.%20Comb.&amp;volume=5&amp;issue=4&amp;pages=359-372&amp;publication_year=1984&amp;author=Stanley%2CRP
[299]: http://www.ams.org/mathscinet-getitem?mr=3341587
[300]: http://scholar.google.com/scholar_lookup?amp;title=Valid%20orderings%20of%20real%20hyperplane%20arrangements&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=53&amp;issue=4&amp;pages=951-964&amp;publication_year=2015&amp;author=Stanley%2CRP
[301]: http://www.ams.org/mathscinet-getitem?mr=1268576
[302]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20Newton%20polytope%20of%20the%20resultant&amp;journal=J.%20Algebraic%20Comb.&amp;volume=3&amp;issue=2&amp;pages=207-236&amp;publication_year=1994&amp;author=Sturmfels%2CB
[303]: http://www.ams.org/mathscinet-getitem?mr=1215321
[304]: http://scholar.google.com/scholar_lookup?amp;title=Extension%20spaces%20of%20oriented%20matroids&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=10&amp;issue=1&amp;pages=23-45&amp;publication_year=1993&amp;author=Sturmfels%2CB&amp;author=Ziegler%2CGM
[305]: http://www.ams.org/mathscinet-getitem?mr=676751
[306]: http://scholar.google.com/scholar_lookup?amp;title=%24%242N%24%24%202%20N%20noncollinear%20points%20determine%20at%20least%20%24%242N%24%24%202%20N%20directions&amp;journal=J.%20Comb.%20Theory%20Ser.%20A&amp;volume=33&amp;issue=3&amp;pages=343-347&amp;publication_year=1982&amp;author=Ungar%2CP
[307]: http://www.ams.org/mathscinet-getitem?mr=824111
[308]: http://scholar.google.com/scholar_lookup?amp;title=More%20on%20%24%24k%24%24%20k%20-sets%20of%20finite%20sets%20in%20the%20plane&amp;journal=Discret.%20Comput.%20Geom.&amp;volume=1&amp;issue=1&amp;pages=95-100&amp;publication_year=1986&amp;author=Welzl%2CE
[309]: http://scholar.google.com/scholar_lookup?amp;title=Theory%20of%20Matroids%2C%20Encyclopedia%20of%20Mathematics%20and%20Its%20Applications&amp;publication_year=1986
[310]: http://www.ams.org/mathscinet-getitem?mr=1217068
[311]: http://scholar.google.com/scholar_lookup?amp;title=Higher%20Bruhat%20orders%20and%20cyclic%20hyperplane%20arrangements&amp;journal=Topology&amp;volume=32&amp;issue=2&amp;pages=259-279&amp;publication_year=1993&amp;author=Ziegler%2CGM
[312]: http://scholar.google.com/scholar_lookup?amp;title=Lectures%20on%20Polytopes%2C%20Graduate%20Texts%20in%20Mathematics&amp;publication_year=1995&amp;author=Ziegler%2CGM
[313]: https://citation-needed.springer.com/v2/references/10.1007/s00493-023-00062-3?format=refman&amp;flavour=references
[314]: /search?sortBy=newestFirst&amp;contributor=Arnau%20Padrol
[315]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Arnau%20Padrol
[316]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Arnau%20Padrol%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[317]: /search?sortBy=newestFirst&amp;contributor=Eva%20Philippe
[318]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Eva%20Philippe
[319]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Eva%20Philippe%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[320]: mailto:arnau.padrol@ub.edu
[321]: /article/10.1007/s00493-023-00062-3#ref-CR81
[322]: /article/10.1007/s00493-023-00062-3#FPar8
[323]: http://creativecommons.org/licenses/by/4.0/
[324]: https://s100.copyright.com/AppDispatchServlet?title=Sweeps%2C%20Polytopes%2C%20Oriented%20Matroids%2C%20and%20Allowable%20Graphs%20of%20Permutations&amp;author=Arnau%20Padrol%20et%20al&amp;contentID=10.1007%2Fs00493-023-00062-3&amp;copyright=The%20Author%28s%29&amp;publication=0209-9683&amp;publicationDate=2023-10-23&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[325]: https://crossmark.crossref.org/dialog/?doi=10.1007/s00493-023-00062-3
[326]: https://citation-needed.springer.com/v2/references/10.1007/s00493-023-00062-3?format=refman&amp;flavour=citation
[327]: /search?query=Allowable%20sequences%20of%20permutations&amp;facet-discipline=#34;Mathematics&#34;
[328]: /search?query=oriented%20matroids&amp;facet-discipline=#34;Mathematics&#34;
[329]: /search?query=polytopes&amp;facet-discipline=#34;Mathematics&#34;
[330]: /search?query=sweep%20algorithms&amp;facet-discipline=#34;Mathematics&#34;
[331]: /search?query=monotone%20path%20polytopes&amp;facet-discipline=#34;Mathematics&#34;
[332]: /search?query=generalized%20Baues%20problem&amp;facet-discipline=#34;Mathematics&#34;
[333]: /search?query=permutahedra&amp;facet-discipline=#34;Mathematics&#34;
[334]: /search?query=52B05&amp;facet-discipline=#34;Mathematics&#34;
[335]: /search?query=52B11&amp;facet-discipline=#34;Mathematics&#34;
[336]: /search?query=52B12&amp;facet-discipline=#34;Mathematics&#34;
[337]: /search?query=52B22&amp;facet-discipline=#34;Mathematics&#34;
[338]: /search?query=52B40&amp;facet-discipline=#34;Mathematics&#34;
[339]: /search?query=52C35&amp;facet-discipline=#34;Mathematics&#34;
[340]: /search?query=52C40&amp;facet-discipline=#34;Mathematics&#34;
[341]: /search?query=05B35&amp;facet-discipline=#34;Mathematics&#34;
[342]: /search?query=06B99&amp;facet-discipline=#34;Mathematics&#34;
