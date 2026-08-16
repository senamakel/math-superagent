<!-- source: https://arxiv.org/html/2506.00224v1 | converted from HTML -->

Automated Symmetric Constructionsin Discrete Geometry

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2506.00224v1 [cs.DM] 30 May 2025

# Automated Symmetric Constructions
in Discrete Geometry

Bernardo Subercaseaux [3], Ethan Mackey [4],
Long Qian [5] and Marijn J. H. Heule [6] Email address: [{bsuberca,ethanmac,longq,mheule}@andrew.cmu.edu][7] Address: Carnegie Mellon University, Pittsburgh, PA 15213, USA

###### Abstract.

We present a computational methodology for obtaining rotationally symmetric sets of points satisfying discrete geometric constraints, and demonstrate its applicability by discovering new solutions to some well-known problems in combinatorial geometry. Our approach takes the usage of SAT solvers in discrete geometry further by directly embedding rotational symmetry into the combinatorial encoding of geometric configurations. Then, to realize concrete point sets corresponding to abstract designs provided by a SAT solver, we introduce a novel local-search realizability solver, which shows excellent practical performance despite the intrinsic ∃ ℝ \exists\mathbb{R} -completeness of the problem. Leveraging this combined approach, we provide symmetric extremal solutions to the Erdős-Szekeres problem, as well as a minimal odd-sized solution with 21 points for the everywhere-unbalanced-points problem, improving on the previously known 23-point configuration. The imposed symmetries yield more aesthetically appealing solutions, enhancing human interpretability, and simultaneously offer computational benefits by significantly reducing the number of variables required to encode discrete geometric problems.

###### Key words and phrases:

Rotational Symmetry and SAT and Realizability and Computational Geometry

## 1. Introduction

Symmetric solutions to combinatorial problems present several benefits: they tend to be easier to grasp and generalize [6, 27], and can even be easier to compute since they have fewer degrees of freedom (i.e., optimization variables) [26, 7, 8]. In the words of Turing awardee Alan J. Perlis, *“Symmetry is a complexity-reducing concept; seek it everywhere”*[15].

Despite theese benefits, it can be hard to prove in advance that a given problem will have symmetric solutions. This is especially the case in Ramsey theory, where the existence of objects avoiding certain patterns is often proven by (pseudo)random constructions, or asymmetric inductive arguments. For example, Schur number k k, a classic Ramsey-theoretical problem, asks for the largest integer n n such that there exists a k k -coloring of { 1, …, n } \{1,\ldots,n\} with no monocromatic solution to x + y = z x+y=z, and the following *palindromic*3 3 -coloring is optimal since S ⁡ ( 3) = 13 S(3)=13:

 | 1 ​ 2 3 ​ 4 ​ 5 6 ​ 7 ​ 8 9 ​ 10 ​ 11 12 ​ 13. {\color[rgb]{1,0,0}1}\;{\color[rgb]{0,0.6,0}2}\;{\color[rgb]{0,0.6,0}3}\;{\color[rgb]{1,0,0}4}\;{\color[rgb]{0,0,1}5}\;{\color[rgb]{0,0,1}6}\;{\color[rgb]{0,0.6,0}7}\;{\color[rgb]{0,0,1}8}\;{\color[rgb]{0,0,1}9}\;{\color[rgb]{1,0,0}10}\;{\color[rgb]{0,0.6,0}11}\;{\color[rgb]{0,0.6,0}12}\;{\color[rgb]{1,0,0}13}. |  |

Interestingly, for all known Schur numbers S ⁡ ( k) S(k), there is an optimal coloring that is palindromic (symmetric w.r.t. i ↦ n − i + 1 i\mapsto n\!-\!i\!+\!1) [9]. However, this is not known to be true for all k k. A comparable phenomenon has been observed for van der Waerden numbers [8]. In this article we show that a similar situation seems to occur in certain discrete geometry problems, and that such symmetric solutions can be found *automatically*. We will consider two problems in discrete geometry described below.

[image: Refer to caption]

(a) Asymmetric construction of 16 16 points in general position without a convex 6 6 -gon [28].

[image: Refer to caption]

(b) 4-fold symmetric construction that minimizes the number of convex pentagons [21].

[image: Refer to caption]

(c) A 12-point 2-EU configuration with a 3-fold symmetry [2]. Lines connect collinear points.

Figure 1. Examples of geometric constructions with and without symmetry.

#### Erdős-Szekeres.

For each integer k ≥ 3 k\geq 3, the problem is to find g ⁡ ( k) g(k), the smallest integer such that any set of g ⁡ ( k) g(k) points in the plane, without three on a common line, contains k k points in convex position. This long-standing problem dates back to the 1930s, with Klein’s proof of g ⁡ ( 4) = 5 g(4)=5, popularly known as the *happy-ending theorem*. The only further values known are g ⁡ ( 5) = 9 g(5)=9 and g ⁡ ( 6) = 17 g(6)=17 [23]. Erdős and Szekeres conjectured that g ⁡ ( k) = 2 k − 2 + 1 g(k)=2^{k-2}+1 for every k k, which matches the three known datapoints, and proved this to be a lower bound [14]. The Erdős-Szekeres upper-bound construction is however asymmetric and hard to visualize even for small values of k k. For example, an asymmetric construction of showing g ⁡ ( 6) > 16 g(6)>16, currently in the Wikipedia page of the Happy Ending problem [28], is shown in Figure 1(a). In contrast, our symmetric constructions are presented in Section 6 ( Figure 4). Interestingly, Subercaseaux et al. [21] provided a symmetric construction for minimizing the number of convex pentagons amongst n n points, and both the work of Morris and Soltan [14] as well as Scheucher [18] exhibited symmetric (or almost symmetric) extremal constructions for variants of the Erdős-Szekeres problem. In this work, we present a much more systematic approach to symmetry in discrete geometry.

#### Everywhere-unbalanced-points.

Given a set S S of n n points in the plane, we denote by L ⁡ ( S) L(S) the set of lines that touch at least two points of S S. The “imbalance” Δ ⁡ ( ℓ) \Delta(\ell) of a line ℓ ∈ L ⁡ ( S) \ell\in L(S) is the difference between the number of points that are on one side of ℓ \ell and the number of points on the other side. We say that S S is k k -everywhere-unbalanced ( k k -EU, for short) if Δ ⁡ ( ℓ) ≥ k \Delta(\ell)\geq k for all lines ℓ ∈ L ⁡ ( S) \ell\in L(S). The main open problem is whether k k -EU sets exist for all k k. This question can be traced back to Kupitz, who asked whether a 2 2 -EU pointset exists [12]. Alon answered affirmatively (see Figure 1(c)), showing that 2 2 -EU sets with 4 ​ s 4s points exist for every odd value of s ≥ 3 s\geq 3, and his construction has an s s -fold rotational symmetry [2]. Pinchasi proved that k k -EU sets, if they exist, must have Ω ⁡ ( 2 2 k) \Omega(2^{2^{k}}) points [16], and recently Conlon and Lim showed an almost-matching upper bound when considering pseudolines instead of lines [4]. It is still open, however, whether a k k -EU set exists for any k ≥ 3 k\geq 3.

### 1.1. Our contributions and methodology

We present a computational methodology for obtaining rotationally symmetric constructions for discrete geometric problems, which we apply to the aforementioned problems as well as other variants, e.g., 9 9 points in general position without an empty convex 5 5 -gon. The methodology consists of two stages:

-

Symmetric combinatorial encoding: We first encode the geometric properties of the problems as instances of boolean satisfiability (SAT), following a recent line of work. We impose rotational symmetry in the encoding itself, which was initially explored by one of the authors [13]. To do this efficiently, we prove that the axioms of Knuth’s CC systems [11] can be encoded with O ⁡ ( n 4) O(n^{4}) many clauses without assuming a left-to-right ordering of the points as in previous work [10]. For the everywhere-unbalanced-points problem, we use SAT for the first time and prove, for instance, that Alon’s 12 12 -point construction uses the minimum number of points for a 2 2 -EU set.

-

Realizability: Going from the solutions to the SAT instances to actual pointsets turns out to be harder, both in theory and in practice. To tackle this we developed Localizer, a local-search solver for the ∃ ℝ \exists\mathbb{R} -complete realizability problem, and through an experimental evaluation show it is highly performant compared to the general-purpose local-search formulation used in previous work [21]. Our solver does not handle collinear points, and thus to realize solutions of the everywhere-unbalanced-points problem (which necessarily involves collinearity), we use a different ad-hoc approach.

We show symmetric solutions for the Erdős-Szekeres problem on 16 16 points without convex 6 6 -gons, and furthermore we enumerate and classify them, showing that s s -fold symmetric solutions exist for s = 4 s=4 and s = 5 s=5, but not for s = 3 s=3. For the everywhere-unbalanced-points problem, we exhibit a 21 21 -point symmetric construction ( Figure 6), which we prove to be the minimal odd-sized solution. In this case, the symmetry crucially allows us to find a realization.

Our code is publicly available at [github.com/bsubercaseaux/automatic-symmetries][8].

## 2. Background

While the domain of the aforementioned problems is continuous (i.e., ℝ 2 \mathbb{R}^{2}), it is possible to reason about geometric properties like convexity, or line balances, purely in terms of combinatorial relationships between points. A widely successful abstraction in discrete geometry is that of *triple orientations*[11] which consists of characterizing, for each ordered triples of points ( p, q, r) (p,q,r), whether it defines a curve that turns clockwise, counterclockwise, or whether they are collinear. Concretely, given points p, q, r p,q,r, their triple orientation is defined as

 | σ ⁡ ( p, q, r) = sign ​ det ( p x q x r x p y q y r y 1 1 1) = { − 1 if ​ p, q, r ​ are oriented clockwise, 0 if ​ p, q, r ​ are collinear, 1 if ​ p, q, r ​ are oriented counterclockwise. \sigma(p,q,r)=\text{sign}\det\begin{pmatrix}p_{x}&q_{x}&r_{x}\\ p_{y}&q_{y}&r_{y}\\ 1&1&1\end{pmatrix}=\begin{cases}-1&\text{if }p,q,r\text{ are oriented clockwise,}\\ \;\;\,0&\text{if }p,q,r\text{ are collinear},\\ \;\;\,1&\text{if }p,q,r\text{ are oriented counterclockwise}.\end{cases} |  |

This abstraction has been successfully used to encode and solve several problems in discrete geometry: Peters and Szekeres used it to settle g ⁡ ( 6) = 17 g(6)=17 [23], Heule and Scheucher for proving that 30 30 points in general position must contain an empty convex hexagon [10], among others [18, 21, 19]. Let us clarify how these orientations are enough to express the constraints of both the Erdős-Szekeres and the everywhere-unbalanced-points problems. We will start with some definitions. A set of points S S is in general position if no three points are collinear, that is, σ ⁡ ( p, q, r) ≠ 0 \sigma(p,q,r)\neq 0 for all ( p, q, r) ∈ ( S 3) (p,q,r)\in\binom{S}{3}. For a finite set of points S ⊂ ℝ 2 S\subset\mathbb{R}^{2}, we denote by conv ⁡ ( S) \conv(S) the *convex hull*of S S, which is the smallest convex set containing S S. Then, a set of points S S in general position is in *convex position*if removing any point a ∈ S a\in S would change its convex hull, i.e., conv ⁡ ( S ∖ { a }) ≠ conv ⁡ ( S) \conv\left(S\setminus\{a\}\right)\neq\conv(S) for all a ∈ S a\in S. As a consequence of Carathéodory’s theorem, a set of points S S in general position is in convex position if and only if every subset of 4 4 points of S S is also in convex position. This implies that, by using the triple orientations to express whether sets of 4 4 points are in convex position, we can express the presence of a convex k k -gon (from now on, we will use k k -gon to refer to a set of k k points in convex position). The precise formulation is in Section 4.3, and we remark that a Lean formalization of these basic discrete geometry notions has been carried out by Subercaseaux et al. [22]. For the everywhere-unbalanced-points problem, it will suffice to express the imbalance of a line ℓ \ell between points p p and q q of a pointset S S, as the absolute value of the difference between | { r ∈ S: σ ⁡ ( p, q, r) = 1 } | |\{r\in S:\sigma(p,q,r)=1\}| and | { r ∈ S: σ ⁡ ( p, q, r) = − 1 } |. |\{r\in S:\sigma(p,q,r)=-1\}|.

### 2.1. Geometric and combinatorial symmetries

We consider two different forms of symmetry. For a pointset P = { p 1, …, p n } P=\{p_{1},\ldots,p_{n}\}, a *combinatorial symmetry*is a bijection π: { 1, …, n } → { 1, …, n } \pi:\{1,\ldots,n\}\to\{1,\ldots,n\} such that σ ⁡ ( p i, p j, p k) = σ ⁡ ( p π ⁡ ( i), p π ⁡ ( j), p π ⁡ ( k)) \sigma(p_{i},p_{j},p_{k})=\sigma(p_{\pi(i)},p_{\pi(j)},p_{\pi(k)}) for all ( i, j, k) ∈ ( [n] 3) (i,j,k)\in\binom{[n]}{3}. On the other hand, a *geometric symmetry*is a bijection ρ: ℝ 2 → ℝ 2 \rho:\mathbb{R}^{2}\to\mathbb{R}^{2} such that ρ ⁡ ( p i) ∈ P \rho(p_{i})\in P for all i ∈ { 1, …, n } i\in\{1,\ldots,n\}. We say that a geometric symmetry ρ \rho is *orientation preserving*if σ ⁡ ( ρ ⁡ ( p), ρ ⁡ ( q), ρ ⁡ ( r)) = σ ⁡ ( p, q, r) \sigma(\rho(p),\rho(q),\rho(r))=\sigma(p,q,r) for every p, q, r ∈ ℝ 2 p,q,r\in\mathbb{R}^{2}. For example, any rotation of the plane is orientation preserving [22], but it might not be a geometric symmetry of a pointset, as illustrated in Figure 1(a) taking π / 4 \pi/4 as rotation angle. In this work, we focus on s s -fold rotational symmetries, which correspond to rotations of the plane by 2 ​ π s \frac{2\pi}{s}, for some integer s s. More formally, let ρ α: ℝ 2 → ℝ 2 \rho_{\alpha}:\mathbb{R}^{2}\to\mathbb{R}^{2} be the function defined by ρ α ​ ( x, y) = ( x ​ cos ⁡ ( α) − y ​ sin ⁡ ( α), x ​ sin ⁡ ( α) + y ​ cos ⁡ ( α)) \rho_{\alpha}(x,y)=(x\cos(\alpha)-y\sin(\alpha),x\sin(\alpha)+y\cos(\alpha)). Then, we say a set of points S S is *s s -fold symmetric*if ρ 2 ​ π / s \rho_{2\pi/{s}} is a geometric symmetry of S S (i.e., ρ 2 ​ π / s ​ ( S) = S \rho_{2\pi/{s}}(S)=S).

### 2.2. Orientation Variables

To obtain a propositional encoding for the aforementioned problems, we start by defining *orientation variables*a i, j, k \textsc{a}_{i,j,k}, b i, j, k \textsc{b}_{i,j,k}, and c i, j, k \textsc{c}_{i,j,k} for each triple of distinct indices i, j, k ∈ { 1, …, n } i,j,k\in\{1,\ldots,n\}, where n n is the number of points in the desired pointset. a i, j, k \textsc{a}_{i,j,k} will represent that σ ⁡ ( p i, p j, p k) = 1 \sigma(p_{i},p_{j},p_{k})=1, whereas b i, j, k \textsc{b}_{i,j,k} that σ ⁡ ( p i, p j, p k) = − 1 \sigma(p_{i},p_{j},p_{k})=-1, and c i, j, k \textsc{c}_{i,j,k} that σ ⁡ ( p i, p j, p k) = 0 \sigma(p_{i},p_{j},p_{k})=0. For the Erdős-Szekeres problem, given that we are interested in pointsets in general position, we will only need the variables a i, j, k \textsc{a}_{i,j,k}, since its truth value is enough to identify the orientation of the triple ( p i, p j, p k) (p_{i},p_{j},p_{k}). For the everywhere-unbalanced-points problem, we use the three kinds of variables, and naturally enforce that exactly one of them is true for each triple of points. From now on, we assume the number of points n n to be fixed.

### 2.3. CC Systems and Axioms

The study of axioms for combinatorial representations of pointsets was initiated by Knuth [11], who introduced the so-called *CC systems*, as an abstraction for pointsets in general position. Knuth’s axioms can be written as follows in our notation:

1. Axiom 1

(Cyclic Symmetry). a i, j, k → a j, k, i \textsc{a}_{i,j,k}\rightarrow\textsc{a}_{j,k,i},

2. Axiom 2

(Antisymmetry). a i, j, k → a i, k, j ¯ \textsc{a}_{i,j,k}\rightarrow\overline{\textsc{a}_{i,k,j}},

3. Axiom 3

(Nondegeneracy). a i, j, k ∨ a i, k, j \textsc{a}_{i,j,k}\lor\textsc{a}_{i,k,j},

4. Axiom 4

(Interiority). a i, j, k ∨ a i, k, l ∨ a k, j, ℓ ∨ a j, i, ℓ \textsc{a}_{i,j,k}\lor\textsc{a}_{i,k,l}\lor\textsc{a}_{k,j,\ell}\lor\textsc{a}_{j,i,\ell},

5. Axiom 5

(Transitivity). a ℓ, i, m ∨ a ℓ, j, m ∨ a ℓ, k, m ∨ a ℓ, j, i ∨ a ℓ, k, j ∨ a ℓ, i, k \textsc{a}_{\ell,i,m}\lor\textsc{a}_{\ell,j,m}\lor\textsc{a}_{\ell,k,m}\lor\textsc{a}_{\ell,j,i}\lor\textsc{a}_{\ell,k,j}\lor\textsc{a}_{\ell,i,k},

where each axiom is quantified over all distinct indices i, j, k, ℓ, m ∈ { 1, …, n } i,j,k,\ell,m\in\{1,\ldots,n\}. It turns out that Axioms (1-3) can be encoded implicitly, by only using variables a i, j, k \textsc{a}_{i,j,k} for indices i < j < k i<j<k, replacing each occurrence of a variable whose indices are not ordered with the corresponding variable with ordered indices, and a potential negation. Namely, for a tuple t t of three indices not necessarily sorted, we can consider t ′ t^{\prime} as the sorted version of t t. According to Axioms (1-3), we replace each occurrence of a t \textsc{a}_{t} with a t ′ \textsc{a}_{t^{\prime}} if t t has an even number of inversions (i.e., the number of swaps required to sort t t), and with a t ′ ¯ \overline{\textsc{a}_{t^{\prime}}} otherwise. Despite these optimizations, the number of clauses required to encode the axioms is still roughly 5! ⋅ ( n 5) ≈ n 5 5!\cdot\binom{n}{5}\approx n^{5}, which amounts to over 24 24 million clauses for n = 32 n=32.

### 2.4. Signotope Axioms

A more efficient alternative in terms of encoding size is to use the so-called *signotope axioms*[5, 18, 10], which assuming that points are sorted from left to right (i.e., x i < x i + 1 x_{i}<x_{i+1} for every i i, where x i x_{i} denotes the x x -coordinate of point p i p_{i}), allows to express an equivalent set of axioms with only 4 ​ ( n 4) 4\binom{n}{4} clauses. The signotope axioms can be written in clausal form as follows:

(1) |  | ( a i, j, k ¯ ∨ a i, k, ℓ ¯ ∨ a i, j, ℓ) ∧ ( a i, j, k ∨ a i, k, ℓ ∨ a i, j, ℓ ¯), (\overline{\textsc{a}_{i,j,k}}\lor\overline{\textsc{a}_{i,k,\ell}}\lor\textsc{a}_{i,j,\ell})\land(\textsc{a}_{i,j,k}\lor\textsc{a}_{i,k,\ell}\lor\overline{\textsc{a}_{i,j,\ell}}), |  |

(2) |  | ( a i, j, k ¯ ∨ a j, k, ℓ ¯ ∨ a i, k, ℓ) ∧ ( a i, j, k ∨ a j, k, ℓ ∨ a i, k, ℓ ¯), (\overline{\textsc{a}_{i,j,k}}\lor\overline{\textsc{a}_{j,k,\ell}}\lor\textsc{a}_{i,k,\ell})\land(\textsc{a}_{i,j,k}\lor\textsc{a}_{j,k,\ell}\lor\overline{\textsc{a}_{i,k,\ell}}), |  |

where the quantification here is only over indices 1 ≤ i < j < k < ℓ ≤ n 1\leq i<j<k<\ell\leq n. The main issue with these signotope axioms, which we will address in Section 4.1, is that they assume a left-to-right ordering of the points, which can often be assumed without loss of generality by simply relabeling points from left to right (cf. [22]), but in our case is incompatible with the rotational symmetries we want to impose. Note that the strictness of the ordering is not a restrictive condition since we can always rotate pointsets by an ε \varepsilon -angle while preserving all orientations to guarantee no points share the same x x -coordinate.

### 2.5. Realizability Problem

It is worth mentioning immediately that these combinatorial abstractions for pointsets are an *under-approximation*of the geometric properties of points in ℝ 2 \mathbb{R}^{2}, meaning that every set of points satisfies the axioms, but there are assignments of the orientation variables that satisfy the axioms and yet do not correspond to any planar pointset. Therefore, if after adding problem-specific constraints (e.g., convexity, imbalance, etc.) we obtain a satisfiable formula, we still need to check whether the solution to the orientation variables can be realized in ℝ 2 \mathbb{R}^{2}, the so-called *point realizability problem*for which we present a local-search solver in Section 5. On the other hand, if no assignment of the orientation variables satisfies the constraints of a problem in conjunction with the axioms, then we can safely conclude that no pointset exists satisfying the desired properties. This idea has been formalized in Lean by Subercaseaux et al. [22].

## 3. Symmetry Constraints

In this section, we present the symmetry constraints that we will use to enforce s s -fold rotational symmetry in our combinatorial encodings. In general, a combinatorial symmetry π: { 1, …, n } → { 1, …, n } \pi:\{1,\ldots,n\}\to\{1,\ldots,n\} can be enforced by adding clauses for the constraints a i, j, k ↔ a π ⁡ ( i), π ⁡ ( j), π ⁡ ( k), \textsc{a}_{i,j,k}\leftrightarrow\textsc{a}_{\pi(i),\pi(j),\pi(k)}, and similarly for the b i, j, k \textsc{b}_{i,j,k} and c i, j, k \textsc{c}_{i,j,k} variables when dealing with collinear points. As we will see next, however, it is possible to enforce the symmetry directly without those clauses by unifying equivalent variables as we did for Axioms (1-2) of Knuth’s CC systems. For example, if we want to enforce a 4 4 -fold rotational symmetry over 16 16 points, we can assume that the permutation π \pi can be factored as

(3) |  | π = ( 1, 2, 3, 4) ​ ( 5, 6, 7, 8) ​ ( 9, 10, 11, 12) ​ ( 13, 14, 15, 16), \pi=(1,2,3,4)\,(5,6,7,8)\,(9,10,11,12)\,(13,14,15,16), |  |

which can be succinctly coded by defining π ⁡ ( i) = ⌊ ( i − 1) / 4 ⌋ ⋅ 4 + ( i + 1) mod 4 \pi(i)=\lfloor(i-1)/4\rfloor\cdot 4+(i+1)\!\!\mod 4. Then, if we consider the triple of indices ( 1, 6, 8) (1,6,8), we have the equivalences:

 | a 1, 6, 8 ↔ a 2, 7, 5 ↔ a 3, 8, 6 ↔ a 4, 5, 7, \textsc{a}_{1,6,8}\leftrightarrow\textsc{a}_{2,7,5}\leftrightarrow\textsc{a}_{3,8,6}\leftrightarrow\textsc{a}_{4,5,7}, |  |

and by the equivalences of Section 2.3, this is the same as

 | a 1, 6, 8 ↔ a 2, 5, 7 ¯ ↔ a 3, 6, 8 ¯ ↔ a 4, 5, 7. \textsc{a}_{1,6,8}\leftrightarrow\overline{\textsc{a}_{2,5,7}}\leftrightarrow\overline{\textsc{a}_{3,6,8}}\leftrightarrow\textsc{a}_{4,5,7}. |  |

We can thus treat these literals as an equivalence class, and for each such equivalence class we can choose a representative (e.g., the lexicographically smallest one, a 1, 6, 8 \textsc{a}_{1,6,8}), and then replace all occurrences of the other literals in its class with the representative or its negation.

### 3.1. Filtering Isomorphic Constraints

Not only can we reduce the number of variables by the enforced symmetries, but also the number of constraints. For example, a constraint stating that indices { 1, 3, 6, 8, 10, 13 } \{1,3,6,8,10,13\} do not form a 6 6 -gon, already implies that the indices { 2, 4, 5, 7, 11, 14 } \{2,4,5,7,11,14\} do not form a 6 6 -gon when enforcing the symmetry of Equation 3. Therefore, the second constraint is redundant and can be removed. In general, for a constraint involving a tuple of indices t = ( i 1, …, i k) t=(i_{1},\ldots,i_{k}), we consider the *orbit*of t t under the symmetry π \pi, which is the set of all tuples of indices that can be obtained from t t by applying π \pi any number of times. We can then remove all but one constraint for each orbit, which we implement by only adding constraints that are lexicographically smallest in their orbits.

### 3.2. Symmetry Breaking

To limit the generation of isomorphic solutions, we add symmetry-breaking predicates, which depend on the parameters of the problem at hand. Let us consider, for example, the Erdős-Szekeres problem for 16 16 points without 6 6 -gons and a 4 4 -fold symmetry. The only possibility for the convex layers of these 16 16 points is that we have 4 4 layers with 4 4 points each. Then, as any rotational symmetry must map each point p p to a point q q in the same convex layer as p p (potentially p = q p=q), we can assume without loss of generality that the 4 4 -fold symmetry is precisely the one in Equation 3. Moreover, we can assume without loss of generality that the outermost convex layer is { 1, 2, 3, 4 } \{1,2,3,4\}, that the next one is { 5, 6, 7, 8 } \{5,6,7,8\}, and so on. To enforce that points 5, 6, 7, 8 5,6,7,8 are inside the convex hull of points 1, 2, 3, 4 1,2,3,4, and that 1 → 2 → 3 → 4 1\to 2\to 3\to 4 is a counterclockwise sequence, we can add *convex layer unit clauses*( CL -clauses) of the form a i, 1 + i mod 4, j \textsc{a}_{i,1+i\!\!\mod 4,j} for i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\} and j ∈ { 5, 6, 7, 8 } j\in\{5,6,7,8\}. Figure 2 illustrates how these CL -clauses enforece a *canonical*representative from a set of isomorphic solutions. We can then add analogous CL -clauses to enforce that points 9, 10, 11, 12 9,10,11,12 are inside the convex hull of points 5, 6, 7, 8 5,6,7,8, and so on. Furthermore, we can assume without loss of generality that all points whose index is mod 5 1\!\!\mod 5 are in the bottom-left quadrant. To see this, note that otherwise we could relabel the points assigning index 4 ​ i + 1 4i+1 to whichever point from the i i -th outermost convex layer is in the bottom left quadrant, noting that the 4 4 -fold symmetry enforces that at least one point per layer lies in that quadrant. Concretely, we add *quadrant clauses*( Q -clauses) of the form a 1, 3, i ¯ \overline{\textsc{a}_{1,3,i}} and a 2, 4, i \textsc{a}_{2,4,i} for every i > 1 i>1 that is 1 1 modulo 4 4. Note that, assuming without loss of generality that point 1 1 gets coordinates ( − C, 0) (-C,0), and that points 2, 3, 4 2,3,4 get the coordinates implied by the orbit 1 → 2 → 3 → 4 1\to 2\to 3\to 4, then these clauses directly correspond to the points 4 ​ i + 1 4i+1 for i ≥ 1 i\geq 1 being in the bottom-left quadrant. See Figures 2(d) and 2(e).

1 1 3 3 2 2 4 4 5 5 6 6 7 7 8 8 (a) Canonical.

1 1 3 3 4 4 2 2 5 5 6 6 7 7 8 8 (b) Fails CL.

5 5 6 6 7 7 8 8 1 1 2 2 3 3 4 4 (c) Fails CL.

1 1 3 3 2 2 4 4 5 5 6 6 7 7 8 8 (d) Fails Q.

1 1 3 3 2 2 4 4 8 8 5 5 6 6 7 7 (e) Fails Q.

Figure 2. Symmetry breaking predicates for pointsets with a 4 4 -fold symmetry. Orientations in red are failing to satisfy the symmetry-breaking predicates.

## 4. Encodings

In this section, we detail the propositional encodings for the Erdős-Szekeres and everywhere-unbalanced-points problems.

### 4.1. Dynamic Point Ordering Axioms

While the signotope axioms are more efficient than the CC system axioms (an n 5 → n 4 n^{5}\to n^{4} advantage), they assume a left-to-right ordering of the points, which is not compatible with the rotational symmetries we want to impose — e.g., in the example symmetry of Equation 3 we can infer what the convex layers of the desired pointset are, but we cannot a priori say whether point 5 5 will be to the left of point 12 12 or to its right. A discovery of independent interest is that the left-to-right ordering can be replaced by any linear ordering ≺ \prec of the point indices, and only apply the signotope axioms for tuples of indices respecting a constraint similar to i ≺ j ≺ k ≺ ℓ i\prec j\prec k\prec\ell. That is, as opposed to a predefined ordering, we introduce variables ≺ i, j \prec_{i,j} for every pair of distinct indices, which the SAT solver will assign dynamically, and enforce axioms accordingly. Naturally, we need to add constraints stating that these variables induce a strict linear ordering:

1. Totality.

( ≺ i, j ∨ ≺ j, i) ({\prec_{i,j}}\lor{\prec_{j,i}}), for all 1 ≤ i ≠ j ≤ n 1\leq i\neq j\leq n.

2. Asymmetry.

( ≺ i, j ↔ ≺ j, i ¯) ({\prec_{i,j}}\leftrightarrow\overline{{\prec_{j,i}}}), for all 1 ≤ i ≠ j ≤ n 1\leq i\neq j\leq n.

3. Transitivity.

( ≺ i, j ∧ ≺ j, k → ≺ i, k) ({\prec_{i,j}}\land{\prec_{j,k}}\rightarrow{\prec_{i,k}}), for all 1 ≤ i ≠ j ≠ k ≤ n 1\leq i\neq j\neq k\leq n.

These linear-ordering axioms incur in Θ ⁡ ( n 3) \Theta(n^{3}) clauses, and thus are not a bottleneck. Then, it turns out that we can replace the signotope axioms for pointsets in general position with the following:

(4) |  | ( ≺ i, j ∧ ≺ i, k ∧ ≺ i, ℓ) → ( a i, j, k ∨ a i, j, ℓ ¯ ∨ a i, k, ℓ), ∀ i ≠ j ≠ k ≠ ℓ, \left(\prec_{i,j}\land\prec_{i,k}\land\prec_{i,\ell}\right)\rightarrow\left(\textsc{a}_{i,j,k}\lor\overline{\textsc{a}_{i,j,\ell}}\lor\textsc{a}_{i,k,\ell}\right),\quad\forall i\neq j\neq k\neq\ell, |  |

(5) |  | ( ≺ i, k ∧ ≺ j, k ∧ ≺ k, ℓ) → ( a i, j, k ∨ a i, k, ℓ ¯ ∨ a j, k, ℓ), ∀ i ≠ j ≠ k ≠ ℓ. \left(\prec_{i,k}\land\prec_{j,k}\land\prec_{k,\ell}\right)\rightarrow\left(\textsc{a}_{i,j,k}\lor\overline{\textsc{a}_{i,k,\ell}}\lor\textsc{a}_{j,k,\ell}\right),\quad\forall i\neq j\neq k\neq\ell. |  |

Moreover, Equation 4 is only needed when max ⁡ ( j, k) < ℓ \max(j,k)<\ell, which further reduces the number of clauses. In total, since the condition max ⁡ ( j, k) < ℓ \max(j,k)<\ell holds in exactly a third of the cases, these dynamic-ordering axioms incur in 4 3 ⋅ 4! ⋅ ( n 4) ≈ 4 3 ​ n 4 \frac{4}{3}\cdot 4!\cdot\binom{n}{4}\approx\frac{4}{3}n^{4} clauses. For n = 32 n=32, this is around 1.3 1.3 million clauses, a significant improvement over the 24 24 million clauses of the CC-system axioms (cf. Section 2.3). We now summarize correctness with the following two propositions.

###### Proposition 1.

For every set of n n points S = { p 1, …, p n } S=\{p_{1},\ldots,p_{n}\} in general position with distinct x x -coordinates, the assignment of the a i, j, k \textsc{a}_{i,j,k} and ≺ i, j {\prec_{i,j}} variables τ \tau defined as:

 | τ ( a i, j, k) = { true if ​ σ ​ ( p i, p j, p k) = 1 false otherwise, τ ( ≺ i, j) = { true if ​ x i < x j false otherwise, \tau(\textsc{a}_{i,j,k})=\begin{cases}\text{true}&\text{if }\sigma(p_{i},p_{j},p_{k})=1\\ \text{false}&\text{otherwise},\end{cases}\quad\tau(\prec_{i,j})=\begin{cases}\text{true}&\text{if }x_{i}<x_{j}\\ \text{false}&\text{otherwise},\end{cases} |  |

satisfies the dynamic-ordering axioms from Equations 4 and 5.

###### Proposition 2.

For every assignment τ \tau of the a i, j, k \textsc{a}_{i,j,k} variables, with i, j, k ∈ { 1, …, n } i,j,k\in\{1,\ldots,n\}, if there is an assignment θ \theta to the ≺ i, j {\prec_{i,j}} variables ( 1 ≤ i ≠ j ≤ n 1\leq i\neq j\leq n) such that τ ∪ θ \tau\cup\theta satisfies the dynamic-ordering axioms from Equations 4 and 5, and CC-Axioms (1-3) (see Section 2.3), then τ \tau satisfies the CC-Axioms (4-5).

Proposition 1 is stating that the dynamic-ordering axioms are respected by actual pointsets, and Proposition 2 is Intuitively stating that these axioms are no more permisive than the CC axioms. In other words, an empty set of axioms would trivially satisfy Proposition 1 but not Proposition 2, and on the other hand, an inconsistent set of axioms would trivially satisfy Proposition 2 but not Proposition 1. Both proofs are included in Appendix D. The first proof is algebraic, and similar to the proof of the signotope axioms in [22], whereas the second proof is computational, since it reduces to the case n = 5 n=5.

### 4.2. Axioms for Collinear Point Sets

In addition to the axioms in Section 4.1, additional care is needed to handle potentially collinear points. Intuitively, such axioms capture the property that for any collection of 4 points p i, p j, p k, p ℓ p_{i},p_{j},p_{k},p_{\ell} where the first 3 are collinear (i.e. c i, j, k \textsc{c}_{i,j,k} is true), then the orientation of any triple that includes the point p ℓ p_{\ell} uniquely determines the orientation of all triples. As the points are not necessarily ordered, we leverage the dynamic point orderings and case on all possibilities. That is, we add the following clauses for every set of four distinct indices i, j, k, ℓ ∈ { 1, …, n } i,j,k,\ell\in\{1,\ldots,n\}:

1. (1)

( c i, j, k) → ( c 𝐭 𝟏 ↔ c 𝐭 𝟐) (\textsc{c}_{i,j,k})\rightarrow(\textsc{c}_{\mathbf{t_{1}}}\leftrightarrow\textsc{c}_{\mathbf{t_{2}}}), for distinct triples 𝐭 𝟏, 𝐭 𝟐 ≠ { i, j, k } \mathbf{t_{1}},\mathbf{t_{2}}\neq\{i,j,k\},

2. (2)

( ≺ i, j ∧ ≺ j, k ∧ c i, j, k) → ( a 𝐭 𝟏 ↔ a 𝐭 𝟐) ({\prec_{i,j}}\land{\prec_{j,k}}\land\textsc{c}_{i,j,k})\rightarrow(\textsc{a}_{\mathbf{t_{1}}}\leftrightarrow\textsc{a}_{\mathbf{t_{2}}}), for distinct triples 𝐭 𝟏, 𝐭 𝟐 ≠ { i, j, k } \mathbf{t_{1}},\mathbf{t_{2}}\neq\{i,j,k\},

3. (3)

( ≺ i, k ∧ ≺ k, j ∧ c i, j, k) → ( ( a i, j, ℓ ↔ a i, k, ℓ) ∧ ( a i, j, ℓ ↔ b j, k, ℓ)) ({\prec_{i,k}}\land{\prec_{k,j}}\land\textsc{c}_{i,j,k})\rightarrow\left((\textsc{a}_{i,j,\ell}\leftrightarrow\textsc{a}_{i,k,\ell})\land(\textsc{a}_{i,j,\ell}\leftrightarrow\textsc{b}_{j,k,\ell})\right),

4. (4)

( ≺ k, i ∧ ≺ i, j ∧ c i, j, k) → ( ( a i, j, ℓ ↔ b i, k, ℓ) ∧ ( a i, j, ℓ ↔ b j, k, ℓ)) ({\prec_{k,i}}\land{\prec_{i,j}}\land\textsc{c}_{i,j,k})\rightarrow\left((\textsc{a}_{i,j,\ell}\leftrightarrow\textsc{b}_{i,k,\ell})\land(\textsc{a}_{i,j,\ell}\leftrightarrow\textsc{b}_{j,k,\ell})\right).

Moreover, for Axioms (2-4), we also add an analogous version with each ≺ \prec variable negated, to consider the opposite ordering. Axiom (1) enforces the transitivity of collinearity: if there exist two distinct triples of { p i, p j, p k, p l } \{p_{i},p_{j},p_{k},p_{l}\} that are collinear, then all points are collinear. Axioms (2-4) handle the case where { p i, p j, p k } \{p_{i},p_{j},p_{k}\} are collinear yet p ℓ p_{\ell} does not lie on the same line. In Axiom (2), either i ≺ j ≺ k i\prec j\prec k or i ≻ j ≻ k i\succ j\succ k hold, thus the points are ordered monotonically. As such, their relative orientations with respect to p ℓ p_{\ell} are necessarily equivalent, hence the bi-implication clauses. In contrast, consider the scenario where i ≺ k ≺ j i\prec k\prec j, which falls under Axiom (3). In this case, the orientations σ ⁡ ( p i, p j, p ℓ) = σ ⁡ ( p i, p k, p ℓ) \sigma(p_{i},p_{j},p_{\ell})=\sigma(p_{i},p_{k},p_{\ell}) are still equivalent, as the lines p i → p j, p i → p k p_{i}\to p_{j},p_{i}\to p_{k} have the same direction, resulting in the clauses a i, j, ℓ ↔ a i, k, ℓ \textsc{a}_{i,j,\ell}\leftrightarrow\textsc{a}_{i,k,\ell}. On the contrary, the lines p i → p j, p j → p k p_{i}\to p_{j},p_{j}\to p_{k} are now in opposing directions, thus the orientations σ ⁡ ( p i, p j, p ℓ) = − σ ⁡ ( p j, p k, p ℓ) \sigma(p_{i},p_{j},p_{\ell})=-\sigma(p_{j},p_{k},p_{\ell}) are opposites, yielding the clauses a i, j, ℓ ↔ b j, k, ℓ \textsc{a}_{i,j,\ell}\leftrightarrow\textsc{b}_{j,k,\ell}. Axiom (4) is identical and considers the remaining cases. Note that it suffices to add these clauses only for i < j < k i<j<k, and ℓ ∈ [n] ∖ { i, j, k } \ell\in[n]\setminus\{i,j,k\}. Therefore, the total number of clauses is 28 ​ ( n − 3) ⋅ ( n 3) = 112 ​ ( n 4) 28(n-3)\cdot\binom{n}{3}=112\binom{n}{4}.

### 4.3. Constraints for k k -Gons

Similarly to the work of Scheucher [18, 19], we create auxiliary variables conv i, j, k, ℓ \textsc{conv}_{i,j,k,\ell} for each set of four indices i, j, k, ℓ ∈ { 1, …, n } i,j,k,\ell\in\{1,\ldots,n\} (note that these are unordered), representing whether the points p i, p j, p k, p ℓ p_{i},p_{j},p_{k},p_{\ell} are in convex position. Our encoding is slightly different from Scheucher’s in that we define these variables only in terms of the base orientation variables:

 | conv i, j, k, ℓ ↔ ( ( a i, j, k ↔ a i, k, ℓ) ↔ ( a i, k, ℓ ↔ a j, k, ℓ)), \textsc{conv}_{i,j,k,\ell}\leftrightarrow((\textsc{a}_{i,j,k}\leftrightarrow\textsc{a}_{i,k,\ell})\leftrightarrow(\textsc{a}_{i,k,\ell}\leftrightarrow\textsc{a}_{j,k,\ell})), |  |

which we can express in 12 ​ ( n 4) 12\binom{n}{4} clauses using Tseitin variables. The correctness of this encoding can be seen by a tedious case analysis of the 16 16 possible orientations for the four points p i, p j, p k, p ℓ p_{i},p_{j},p_{k},p_{\ell}. Then, as described in Section 2, a set of points S S is in convex position if and only if every subset of 4 4 points of S S is also in convex position. Thus, to express the absence of a convex k k -gon, we enforce for every set X ⊆ { 1, …, n } X\subseteq\{1,\ldots,n\} with | X | = k |X|=k, the clause ⋁ i, j, k, ℓ ∈ X conv i, j, k, ℓ ¯. \bigvee_{i,j,k,\ell\in X}\overline{\textsc{conv}_{i,j,k,\ell}}.

### 4.4. Constraints for Imbalance

Recall that for a set of n n points S S in the plane, L ⁡ ( S) L(S) denotes the set of all lines touching at least two points of S S. For a pair of points p i, p j ∈ S p_{i},p_{j}\in S, let l i, j ∈ L ⁡ ( S) l_{i,j}\in L(S) be the unique line passing through p i p_{i} and p j p_{j}. The set of points above/below l i, j l_{i,j} are defined as l i, j + = { p k ∈ S ∣ σ ⁡ ( p i, p j, p k) > 0 } l^{+}_{i,j}=\{p_{k}\in S\mid\sigma(p_{i},p_{j},p_{k})>0\} and l i, j − = { p k ∈ S ∣ σ ⁡ ( p i, p j, p k) < 0 } l^{-}_{i,j}=\{p_{k}\in S\mid\sigma(p_{i},p_{j},p_{k})<0\}, respectively. and the imbalance of p i, p j p_{i},p_{j}, denoted Δ ⁡ ( i, j) \Delta(i,j), is defined as Δ ⁡ ( i, j) = | | l i, j + | − | l i, j − | |. \Delta(i,j)=||l^{+}_{i,j}|-|l^{-}_{i,j}||. Finally, the imbalance of S S is the minimum of all such imbalances Δ ⁡ ( S) = min i, j ∈ ( [n] 2) ⁡ Δ ⁡ ( i, j). \Delta(S)=\min_{i,j\in{[n]\choose{2}}}\Delta(i,j). Therefore, to encode Δ ⁡ ( S) ≥ c \Delta(S)\geq c, it suffices to encode Δ ⁡ ( i, j) ≥ c \Delta(i,j)\geq c for all pairs i, j i,j. Thus, the problem reduces to encoding that

 | ∑ k ∉ { i, j } a i, j, k ≥ ∑ k ∉ { i, j } b i, j, k + c or ∑ k ∉ { i, j } a i, j, k ≤ ∑ k ∉ { i, j } b i, j, k − c. \sum_{k\not\in\{i,j\}}\textsc{a}_{i,j,k}\geq\sum_{k\not\in\{i,j\}}\textsc{b}_{i,j,k}+c\qquad\text{or}\qquad\sum_{k\not\in\{i,j\}}\textsc{a}_{i,j,k}\leq\sum_{k\not\in\{i,j\}}\textsc{b}_{i,j,k}-c. |  |

To achieve this, we use the standard Sinz encoding [20] to define for every pair i, j i,j the *counting variables*s m s_{m} and t m t_{m}, for each 0 ≤ m ≤ n − 2 0\leq m\leq n-2, which represent ∑ k ∉ { i, j } a i, j, k = m \sum_{k\not\in\{i,j\}}\textsc{a}_{i,j,k}=m and ∑ k ∉ { i, j } b i, j, k = m \sum_{k\not\in\{i,j\}}\textsc{b}_{i,j,k}=m respectively. Then, to encode that Δ ⁡ ( i, j) ≥ c \Delta(i,j)\geq c it suffices to add clauses of the form s ¯ x ∨ t ¯ y \overline{s}_{x}\lor\overline{t}_{y} for each x, y ∈ { 0, …, n − 2 } x,y\in\{0,\ldots,n-2\} such that | x − y | < c |x-y|<c.

## 5. Realizability

In the realizability problem, we are given an orientation assignment τ: ( n 3) → { − 1, 0, 1 } \tau:\binom{n}{3}\to\{-1,0,1\}, and the goal is to construct a set of points S = { p 1, …, p n } ⊂ ℝ 2 S=\{p_{1},\ldots,p_{n}\}\subset\mathbb{R}^{2} such that τ ⁡ ( i, j, k) = σ ⁡ ( p i, p j, p k) \tau(i,j,k)=\sigma(p_{i},p_{j},p_{k}) for all i < j < k i<j<k. This problem is known to be ∃ ℝ \exists\mathbb{R} -complete [24], and thus at least NP-hard (recall that NP ⊆ ∃ ℝ ⊆ PSPACE \textrm{NP}\subseteq\exists\mathbb{R}\subseteq\textrm{PSPACE} [17]). We first describe our efficient general-purpose realizability solver for pointsets in general position, and then the ad-hoc method we followed to realize pointsets with collinearities for the everywhere-unbalanced-points problem.

### 5.1. Localizer: a Realizability Solver for Points in General Position

Our solver (called Localizer) is written in C and it implements a local-search algorithm that starts with a random initialization of point coordinates ( x 1, y 1), …, ( x n, y n) (x_{1},y_{1}),\ldots,(x_{n},y_{n}), and iteratively moves the points trying to minimize the number of orientation constraints that are not satisfied by their current positions. The solver is multithreaded, and uses a parallelism model in which a global table of top- K K solutions is maintained, and threads independently select a random solution from this table (with probability proportional to the solution quality) and attempt to improve upon it. If a thread manages to find a strictly better solution, then it updates the global table in case the found solution is better-or-equal than some solution on the top- K K table. Within a thread, the algorithm uses a form of *simulated annealing*, where in each iteration a point is selected, with probabilities proportional to the number of unsatisfied constraints they participate in, and then the point is moved to a random position within a ball of radius r r centered at its previous position. The radius r r is exponentially decreasing. The pseudocode of the algorithm is presented in Appendix E. Moreover, Localizer can receive the description of a rotational symmetry and find solutions that respect it.

#### Evaluation.

We evaluate our algorithm on two families of realizable instances. On the one hand, we use the database of realizable order types for n ≤ 10 n\leq 10 points built by Aichholzer et al. [1], where our algorithm solves every instance in less than 50 50 milliseconds. On the other hand, we evaluate on randomly generated instances of n n points in general position, where we sample the points uniformly at random from the unit square (we tested other distributions and obtained similar results). We conducted the experiments on a personal computer (MacBook Pro M1 2020, 16GB RAM, 8 CPU cores) using 8 8 threads, and present the results in Figure 3. In terms of performance, Localizer is roughly 6 6 orders of magnitude faster than the local-search procedure described in our previous work [21], which could not solve any instance with n = 30 n=30 points in less than a minute. We validated each solution through an independent Python program, which converts the floating-point coordinates to exact rational coordinates, and checks that all orientations are satisfied exactly.

30 30 40 40 50 50 60 60 70 70 80 80 0 0 20 20 40 40 60 60 Figure 3. Experimental evaluation of the Localizer realizability solver, over orientations obtained from random realizable sets of points (independently uniform in [0, 1] 2 [0,1]^{2}). Previous approaches took up to 100s for 16 points [21].

### 5.2. Realizing Collinear Configurations for Everywhere-Unbalanced

As collinearity is an *exact*condition where arbitrarily small perturbations will result in non-collinear points, it is not clear how purely numerical methods over the variables { x 1, y 1, …, x n, y n } \{x_{1},y_{1},\ldots,x_{n},y_{n}\} can be used to satisfy the desired orientation constraints exactly. In fact, instead of trying to directly realize the orientation assignment τ \tau obtained through SAT solving, we take τ \tau as partial information to construct a set of points with the same imbalance, but not necessarily respecting the same orientations. In particular, we start by extracting from τ \tau a family of abstract lines ℒ \mathcal{L} where each L ∈ ℒ L\in\mathcal{L} is a maximal set of indices (so L ⊆ { 1, …, n } L\subseteq\{1,\ldots,n\}) such that τ ⁡ ( i, j, k) = 0 \tau(i,j,k)=0 for all i, j, k ∈ ( L 3) i,j,k\in\binom{L}{3}. Then, we note that if there are lines L 1, L 2 ∈ ℒ L_{1},L_{2}\in\mathcal{L} such that L 1 ∩ L 2 = { i } L_{1}\cap L_{2}=\{i\} for some i ∈ { 1, …, n } i\in\{1,\ldots,n\}, then the point p i p_{i} is fully determined by the remaining points (as two lines in Euclidean space have a unique intersection point), and we will say it is *dependent*. After this, we aim to realize the remaining independent variables by maximizing the resulting unbalancedness using a numerical global optimization algorithm. That is, we write the imbalance of each pair of points as a function of the independent variables, and then maximize the minimum imbalance over all pairs of points, using the differential_evolution algorithm implemented in SciPy [25].

## 6. Results

For all our experiments, we used a version of the solver CaDiCaL 1 1 1 Available at [https://github.com:jreeves3/allsat-cadical][9]. [3] that is extended to support efficient enumeration of all solutions.

[image: Refer to caption]

(a) 4-fold symmetric.

[image: Refer to caption]

(b) 5-fold symmetric.

Figure 4. Constructions of 16 16 points in general position without a convex 6 6 -gon.

### 6.1. Avoiding Hexagons

We searched for symmetric configurations with 16 points that avoid hexagons (the maximum number where this can occur). We constructed the formulas for s ∈ { 3, 4, 5 } s\in\{3,4,5\}. The formula enforcing a 3 3 -fold symmetry is unsatisfiable, while the formulas with a 4 4 -fold and 5 5 -fold symmetry are satisfiable. After symmetry breaking, they have 66 and 948 satisfying assignments, respectively. Computing all satisfying assignments can be achieved in a couple of seconds using a single core on a personal computer (MackBook Pro M1 2020).

Not all these 16-point satisfying assignments are realizable. In fact, most of them are (likely) unrealizable 2 2 2 The realizer tool can only determine realizability, not unrealizability. However, for several of the configurations for which the tool was unable to find a realization, we were able to find a subset 10-point configuration that is known to be unrealizable.. Out of the 66 solutions of the 4 4 -fold symmetry, 18 are realizable, while out of the 932 solutions of the 5 5 -fold symmetry 92 are realizable. Figure 4 shows a 4 4 -fold and a 5 5 -fold realization.

We also examined the number of 4 4 -gons and 5 5 -gons in the solutions. All 66 solutions of the 4 4 -fold symmetry have 924 4 4 -gons, while the number of 5 5 -gons ranges between 208 and 320. For the 5 5 -fold symmetry solutions, the number of 4 4 -gons ranges from 800 to 1185, while the number of 5 5 -gons range from 263 to 1038. Figure 5 illustrates the data. Note that assignments are more likely to be realizable if they have a relatively high number of 4 4 -gons and a relatively low number of 5 5 -gons.

[image: Refer to caption] Figure 5. The number of 4-gons and 5-gons in realizable and (likely) unrealizable configurations with a 4-fold symmetry (left) and a 5-fold symmetry (right).

### 6.2. Avoiding 7 7 -Gons

We also sought a symmetric solution for 32 points without a 7 7 -gon. On 32 points, only 7 7 -gon-free s s -fold rotational symmetries could exist with s ∈ { 1, 2, 4 } s\in\{1,2,4\}. We focused our experiments on s = 4 s=4 as that symmetry reduces the search space the most. The resulting formula is easy to satisfy, but the initial solutions that we obtained were hard to realize. We therefore decided to enumerate all solutions on a supercomputer, which took about 1 CPU year. The number of non-isomorphic configurations is staggering: 310 187 713. We attempted to realize several of them using heuristics to determine which ones would be more likely to be realizable. During those experiments, we observed that the outer 28 points can frequently be realized (so only the inner 4 points not), while the inner 12 points were never realizable. Afterwards we observed that all 310 million solutions have only 6 different configurations to the inner 12 points and none of those are realizable. Thus, there does not exist a realizable 4-fold symmetry on 32 points without a 7 7 -gon.

### 6.3. Avoiding Balance

It is known from prior constructions [2, 4] that there exist infinitely many point sets with an even number of points having imbalance 2, as well as a set of 23 points having imbalance 2. However, it was unknown if these constructions were minimal. So we explored the question: What is the smallest even (odd) number of points needed to achieve an imbalance of 2? Utilizing our encoding, we were first able to show that the 12-point construction in [2] is indeed minimal, as a smaller number of points produces encodings that are UNSAT. Similarly, in the odd case, we were able to refute the existence of such point sets having ≤ 19 \leq 19 points. Furthermore, by searching for solutions with a 3 3 -fold (combinatorial) rotational symmetry, we were able to find *satisfying and realizable*solutions with 21 points ( Figure 6), thereby completely answering the minimality questions.

[image: Refer to caption] Figure 6. A 2 2 -everywhere-unbalanced construction on 21 21 points.

## 7. Conclusion

We have presented a systematic approach to obtain symmetric constructions for discrete geometric problems, and along the way, a highly performant local-search solver for the realizability problem. Our results show further evidence of an interesting pattern highlighted in the introduction: while general constructions for problems in Ramsey theory are often asymmetric, it turns out that there are symmetric solutions for small values of the parameters. A natural direction of research, both for computer scientists and mathematicians, is to try to uncover general constructions from the symmetric solutions that we can find for small instances. In particular, for the Erdős-Szekeres problem, we suspect that there are symmetric constructions for all k ≥ 7 k\geq 7, and proving this could represent progress toward the conjectured bound g ⁡ ( k) = 2 k − 2 + 1 g(k)=2^{k-2}+1, since it might be easier to prove optimality for more structured solutions. In the case of the everywhere-unbalanced-points problem, our future research will focus on finding a 3 3 -EU set, for which we aim to leverage the reduction in the number of variables achieved by forcing an ansatz symmetry. Further problems in this line of work include finding a realization of a 2 2 -fold symmetric construction of 32 32 points without a convex 7 7 -gon, and designing an efficient solver that can handle collinearity constraints for the realizability problem.

## References

- [1] Oswin Aichholzer, Franz Aurenhammer, and Hannes Krasser. Enumerating Order Types for Small Point Sets with Applications. Order, 19(3):265–281, September 2002.
- [2] Noga Alon. Research problems. Kleitman and Combinatorics: A Celebration, 257(2):599–624, November 2002.
- [3] Armin Biere, Tobias Faller, Katalin Fazekas, Mathias Fleury, Nils Froleyks, and Florian Pollitt. CaDiCaL 2.0. In Arie Gurfinkel and Vijay Ganesh, editors, Computer Aided Verification - 36th International Conference, CAV 2024, Montreal, QC, Canada, July 24-27, 2024, Proceedings, Part I, volume 14681 of Lecture Notes in Computer Science, pages 133–152. Springer, 2024.
- [4] David Conlon and Jeck Lim. Everywhere unbalanced configurations, 2025.
- [5] Stefan Felsner and Helmut Weil. Sweeps, arrangements and signotopes. Discrete Applied Mathematics, 109(1):67–94, April 2001.
- [6] Giora and Bernard R Goldstein. From summetria to symmetry: The making of a revolutionary scientific concept. Archimedes: New Studies in the History and Philosophy of Science and Technology. Springer, New York, NY, 2008 edition, July 2008.
- [7] Marijn Heule and Toby Walsh. Symmetry in Solutions. Proceedings of the AAAI Conference on Artificial Intelligence, 24(1):77–82, July 2010.
- [8] Marijn J. H. Heule. Avoiding triples in arithmetic progression. Journal of Combinatorics, 8(3):391–422, June 2017.
- [9] Marijn J. H. Heule. Schur number five. In Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelligence, AAAI’18/IAAI’18/EAAI’18, pages 6598–6606, New Orleans, Louisiana, USA, February 2018. AAAI Press.
- [10] Marijn J. H. Heule and Manfred Scheucher. Happy Ending: An Empty Hexagon in Every Set of 30 Points. In Bernd Finkbeiner and Laura Kovács, editors, Tools and Algorithms for the Construction and Analysis of Systems, pages 61–80, Cham, 2024. Springer Nature Switzerland.
- [11] Donald E. Knuth. Axioms and Hulls. In Donald E. Knuth, editor, Axioms and Hulls, Lecture Notes in Computer Science, pages 1–98. Springer, Berlin, Heidelberg, 1992.
- [12] Yakov Shimeon Kupitz. Extremal problems in combinatorial geometry. Lecture notes series. Aarhus Universitet, Matematisk Institut, 1979.
- [13] Ethan Mackey. Pinwheels and polygons: Symmetric realizations of polygon-free point placements via sat. Master’s thesis, Carnegie Mellon University, 2025.
- [14] W. Morris and V. Soltan. The Erdos-Szekeres problem on points in convex position – a survey. Bulletin of the American Mathematical Society, 37(4):437–458, 2000.
- [15] Alan J. Perlis. Special feature: Epigrams on programming. SIGPLAN Not., 17(9):7–13, September 1982.
- [16] Rom Pinchasi. Lines With Many Points On Both Sides. Discrete & Computational Geometry, 30(3):415–435, September 2003.
- [17] Marcus Schaefer. Complexity of Some Geometric and Topological Problems. In David Eppstein and Emden R. Gansner, editors, Graph Drawing, pages 334–344, Berlin, Heidelberg, 2010. Springer.
- [18] Manfred Scheucher. Two disjoint 5-holes in point sets. Computational Geometry, 91:101670, 2020.
- [19] Manfred Scheucher. A SAT Attack on Erdős-Szekeres Numbers in R^d and the Empty Hexagon Theorem. Computing in Geometry and Topology, 2(1):2:1–2:13, March 2023.
- [20] Carsten Sinz. Towards an optimal CNF encoding of boolean cardinality constraints. In Peter van Beek, editor, Principles and Practice of Constraint Programming - CP 2005, 11th International Conference, CP 2005, Sitges, Spain, October 1-5, 2005, Proceedings, volume 3709 of Lecture Notes in Computer Science, pages 827–831. Springer, 2005.
- [21] Bernardo Subercaseaux, John Mackey, Marijn J. H. Heule, and Ruben Martins. Automated mathematical discovery and verification: Minimizing pentagons in the plane, 2024.
- [22] Bernardo Subercaseaux, Wojciech Nawrocki, James Gallicchio, Cayden Codel, Mario Carneiro, and Marijn J. H. Heule. Formal Verification of the Empty Hexagon Number. In Yves Bertot, Temur Kutsia, and Michael Norrish, editors, 15th International Conference on Interactive Theorem Proving (ITP 2024), volume 309 of Leibniz International Proceedings in Informatics (LIPIcs), pages 35:1–35:19, Dagstuhl, Germany, 2024. Schloss Dagstuhl – Leibniz-Zentrum für Informatik.
- [23] George Szekeres and Lindsay Peters. Computer solution to the 17-point Erdős-Szekeres problem. The ANZIAM Journal, 48(2):151–164, 2006.
- [24] Csaba D. Toth, Joseph O’Rourke, and Jacob E. Goodman, editors. Handbook of Discrete and Computational Geometry. Chapman and Hall/CRC, New York, 3 edition, November 2017.
- [25] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, C J Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17:261–272, 2020.
- [26] Toby Walsh. Symmetry within and between Solutions. In Byoung-Tak Zhang and Mehmet A. Orgun, editors, PRICAI 2010: Trends in Artificial Intelligence, pages 11–13, Berlin, Heidelberg, 2010. Springer.
- [27] Hermann Weyl. Symmetry. Princeton Science Library. Princeton University Press, Princeton, NJ, December 2016.
- [28] Wikipedia. Happy ending problem — Wikipedia, the free encyclopedia. [http://en.wikipedia.org/w/index.php?title=Happy%20ending%20problem&oldid=1282669476][10], 2025. [Online; accessed 12-May-2025].

## Appendix A Realizations of 4-Fold Symmetric Configurations

Below are the nine non-isomorphic realizable configurations on 16 points with a 4-fold rotational symmetry. The lines are added to make the symmetry more clearly visible and to facilitate comparison of the different configurations. Note that in the top three plots, the two outer layers are very close to each other, thereby resulting in overlapping points.

## Appendix B Realizations of 5-Fold Symmetric Configurations

Below are the 46 non-isomorphic realizable configurations on 16 points with a 5-fold rotational symmetry. The lines are added to make the symmetry more clearly visible and help compare the different configurations.

## Appendix C Explicit coordinates

We present, for verification purposes, the coordinates of the points in the 4-fold and 5-fold symmetric configurations presented in Figures 4(a) and 4(b). The coordinates for Figure 4(a) are presented explicitly in Table 1, whereas the coordinates for Figure 4(b) are better described by specifying some rational points and leaving the rest implicit. Concretely, if we denote again ρ 2 ​ π / 5 ​ ( x, y) = ( x ​ cos ⁡ ( 2 ​ π / 5) − y ​ sin ⁡ ( 2 ​ π / 5), x ​ sin ⁡ ( 2 ​ π / 5) + y ​ cos ⁡ ( 2 ​ π / 5)) \rho_{2\pi/5}(x,y)=(x\cos(2\pi/5)-y\sin(2\pi/5),x\sin(2\pi/5)+y\cos(2\pi/5)), and denote by ρ 2 ​ π / 5 ( k) \rho_{2\pi/5}^{(}k) the k k -fold application of ρ 2 ​ π / 5 \rho_{2\pi/5}, then Table 2 describes the coordinates of the points in Figure 4(b).

Table 1. The coordinates of the points in Figure 4(a).

1: | ( − 30, 0) (-30,0) |

2: | ( 0, − 30) (0,-30) |

3: | ( 30, 0) (30,0) |

4: | ( 0, 30) (0,30) |

5: | ( − 20, − 7 2) \left(-20,-\frac{7}{2}\right) |

6: | ( 7 2, − 20) \left(\frac{7}{2},-20\right) |

7: | ( 20, 7 2) \left(20,\frac{7}{2}\right) |

8: | ( − 7 2, 20) \left(-\frac{7}{2},20\right) |

9: | ( − 13, − 6) (-13,-6) |

10: | ( 6, − 13) (6,-13) |

11: | ( 13, 6) (13,6) |

12: | ( − 6, 13) (-6,13) |

13: | ( − 19 10, − 6 5) \left(-\frac{19}{10},-\frac{6}{5}\right) |

14: | ( 6 5, − 19 10) \left(\frac{6}{5},-\frac{19}{10}\right) |

15: | ( 19 10, 6 5) \left(\frac{19}{10},\frac{6}{5}\right) |

16: | ( − 6 5, 19 10) \left(-\frac{6}{5},\frac{19}{10}\right) |

Table 2. The coordinates of the points in Figure 4(b).

1: | ρ 2 ​ π / 5 ( 4) ​ ( − 12, − 17) \rho_{2\pi/5}^{(4)}(-12,-17) |

2: | ( − 12, − 17) (-12,-17) |

3: | ρ 2 ​ π / 5 ( 1) ​ ( − 12, − 17) \rho_{2\pi/5}^{(1)}(-12,-17) |

4: | ρ 2 ​ π / 5 ( 2) ​ ( − 12, − 17) \rho_{2\pi/5}^{(2)}(-12,-17) |

5: | ρ 2 ​ π / 5 ( 3) ​ ( − 12, − 17) \rho_{2\pi/5}^{(3)}(-12,-17) |

6: | ( − 15, 2) (-15,2) |

7: | ρ 2 ​ π / 5 ( 1) ​ ( − 15, 2) \rho_{2\pi/5}^{(1)}(-15,2) |

8: | ρ 2 ​ π / 5 ( 2) ​ ( − 15, 2) \rho_{2\pi/5}^{(2)}(-15,2) |

9: | ρ 2 ​ π / 5 ( 3) ​ ( − 15, 2) \rho_{2\pi/5}^{(3)}(-15,2) |

10: | ρ 2 ​ π / 5 ( 4) ​ ( − 15, 2) \rho_{2\pi/5}^{(4)}(-15,2) |

11: | ( − 13, 0) (-13,0) |

12: | ρ 2 ​ π / 5 ( 1) ​ ( − 13, 0) \rho_{2\pi/5}^{(1)}(-13,0) |

13: | ρ 2 ​ π / 5 ( 2) ​ ( − 13, 0) \rho_{2\pi/5}^{(2)}(-13,0) |

14: | ρ 2 ​ π / 5 ( 3) ​ ( − 13, 0) \rho_{2\pi/5}^{(3)}(-13,0) |

15: | ρ 2 ​ π / 5 ( 4) ​ ( − 13, 0) \rho_{2\pi/5}^{(4)}(-13,0) |

16: | ( 0, 0) (0,0) |

[image: Refer to caption] Figure 22. A 21 21 -point 2 2 -everywhere-unbalanced configuration with simple coordinates. Table 3. The coordinates of the points in Figure 22.

1: | ( − 3 ​ 3, − 1) (-3\sqrt{3},-1) |

2: | ( 36 / 11 3, − 20 / 11) (36/11\sqrt{3},-20/11) |

3: | ( 3 / 2 3, − 5 / 2) (3/2\sqrt{3},-5/2) |

4: | ( 3, − 1) (\sqrt{3},-1) |

5: | ( 1 / 2 ​ 3, 1 / 2) (1/2\sqrt{3},1/2) |

6: | ( 961 / 520 3, − 961 / 520) (961/520\sqrt{3},-961/520) |

7: | ( − 7 / 8 3, − 13 / 40) (-7/8\sqrt{3},-13/40) |

8: | ( 3, 5) (\sqrt{3},5) |

9: | ( − 28 / 11 3, − 4) (-28/11\sqrt{3},-4) |

10: | ( − 2 ​ 3, − 1) (-2\sqrt{3},-1) |

11: | ( − 3, − 1) (-\sqrt{3},-1) |

12: | ( 0, − 1) (0,-1) |

13: | ( − 961 / 520 3, − 961 / 520) (-961/520\sqrt{3},-961/520) |

14: | ( 11 / 40 ​ 3, 59 / 40) (11/40\sqrt{3},59/40) |

15: | ( 2 ​ 3, − 4) (2\sqrt{3},-4) |

16: | ( − 8 / 11 3, 64 / 11) (-8/11\sqrt{3},64/11) |

17: | ( 1 / 2 ​ 3, 7 / 2) (1/2\sqrt{3},7/2) |

18: | ( 0, 2) (0,2) |

19: | ( − 1 / 2 3, 1 / 2) (-1/2\sqrt{3},1/2) |

20: | ( 0,961 / 260) (0,961/260) |

21: | ( 3 / 5 3, − 23 / 20) (3/5\sqrt{3},-23/20) |

## Appendix D Proofs for the dynamic-ordering axioms

###### Proof of Proposition 1.

We first prove that Equation 4 is satisfied. Up to relabeling, let { p 1, p 2, p 3, p 4 } \{p_{1},p_{2},p_{3},p_{4}\} be 4 4 points from S S such that the ordering requirements ≺ 1, 2 ∧ ≺ 1, 3 ∧ ≺ 1, 4 \prec_{1,2}\land\prec_{1,3}\land\prec_{1,4} are satisfied. By translating if necessary, we may further assume that p 1 = ( 0, 0) p_{1}=(0,0) is the origin (note that this does not affect the relative ordering of the x x -coordinates nor the orientations). Then, we will think of the condition a 1, 2, 3 ∨ a 1, 2, 4 ¯ ∨ a 1, 3, 4 \textsc{a}_{1,2,3}\lor\overline{\textsc{a}_{1,2,4}}\lor\textsc{a}_{1,3,4} as ( a 1, 2, 3 ¯ ∧ a 1, 3, 4 ¯) → a 1, 2, 4 ¯ (\overline{\textsc{a}_{1,2,3}}\land\overline{\textsc{a}_{1,3,4}})\rightarrow\overline{\textsc{a}_{1,2,4}}. Thus, we assume that a 1, 2, 3 ¯, a 1, 3, 4 ¯ \overline{\textsc{a}_{1,2,3}},\overline{\textsc{a}_{1,3,4}} hold, and it remains to prove that a 1, 2, 4 ¯ \overline{\textsc{a}_{1,2,4}} holds as well. By the construction of the assignment τ \tau, we have that σ ⁡ ( p 1, p 2, p 3) = − 1 \sigma(p_{1},p_{2},p_{3})=-1 and σ ⁡ ( p 1, p 3, p 4) = − 1 \sigma(p_{1},p_{3},p_{4})=-1. Recall that the orientation σ ⁡ ( p, q, r) \sigma(p,q,r) is defined according to the sign of the determinant (or cross-product) relating the points:

 | sign ​ det ( p x q x r x p y q y r y 1 1 1) = { − 1 if ​ ( p x − q x) ​ ( p y − r y) < ( p y − q y) ​ ( p x − r x), 0 if ​ ( p x − q x) ​ ( p y − r y) = ( p y − q y) ​ ( p x − r x), 1 if ​ ( p x − q x) ​ ( p y − r y) > ( p y − q y) ​ ( p x − r x). \text{sign}\det\begin{pmatrix}p_{x}&q_{x}&r_{x}\\ p_{y}&q_{y}&r_{y}\\ 1&1&1\end{pmatrix}=\begin{cases}-1&\text{if }(p_{x}-q_{x})(p_{y}-r_{y})<(p_{y}-q_{y})(p_{x}-r_{x}),\\ 0&\text{if }(p_{x}-q_{x})(p_{y}-r_{y})=(p_{y}-q_{y})(p_{x}-r_{x}),\\ 1&\text{if }(p_{x}-q_{x})(p_{y}-r_{y})>(p_{y}-q_{y})(p_{x}-r_{x}).\end{cases} |  |

Therefore, from σ ⁡ ( p 1, p 2, p 3) = − 1 \sigma(p_{1},p_{2},p_{3})=-1 we have

(6) |  | x 2 ​ y 3 < x 3 ​ y 2, x_{2}y_{3}<x_{3}y_{2}, |  |

and from σ ⁡ ( p 1, p 3, p 4) = − 1 \sigma(p_{1},p_{3},p_{4})=-1 we have

(7) |  | x 3 ​ y 4 < x 4 ​ y 3. x_{3}y_{4}<x_{4}y_{3}. |  |

Since ≺ 1, 2 \prec_{1,2} holds, we have x 1 < x 2 x_{1}<x_{2} and thus we can multiply Equation 7 by x 2 x_{2} without flipping the inequality, obtaining

 | x 2 ​ x 3 ​ y 4 \displaystyle x_{2}x_{3}y_{4} | < x 2 ​ x 4 ​ y 3 = x 4 ​ ( x 2 ​ y 3) < x 4 ​ ( x 3 ​ y 2). \displaystyle<x_{2}x_{4}y_{3}=x_{4}(x_{2}y_{3})<x_{4}(x_{3}y_{2}). |  |

By dividing the left- and right-most terms by x 3 x_{3}, which is positive since ≺ 1, 3 \prec_{1,3} holds, we have x 2 ​ y 4 < x 4 ​ y 2 x_{2}y_{4}<x_{4}y_{2}. This directly implies that σ ⁡ ( p 1, p 2, p 4) = − 1 \sigma(p_{1},p_{2},p_{4})=-1, and thus a 1, 2, 4 ¯ \overline{\textsc{a}_{1,2,4}} holds, satisfying Equation 4.

The proof for Equation 5 is similar, but this time setting p 3 = ( 0, 0) p_{3}=(0,0) for convenience. Here we assume a 1, 2, 3 ¯ \overline{\textsc{a}_{1,2,3}} and a 2, 3, 4 ¯ \overline{\textsc{a}_{2,3,4}}, from where we have

(8) |  | x 4 ​ y 2 \displaystyle x_{4}y_{2} | < x 2 ​ y 4, \displaystyle<x_{2}y_{4}, |  |

(9) |  | x 1 ​ y 2 \displaystyle x_{1}y_{2} | < x 2 ​ y 1. \displaystyle<x_{2}y_{1}. |  |

We moreover have, due to the ordering assumption, that x 1, x 2 < 0 x_{1},x_{2}<0 and x 4 > 0 x_{4}>0, and we want to show that a 1, 3, 4 ¯ \overline{\textsc{a}_{1,3,4}} holds. By the equivalence discussed in Section 2.3, this is the same as proving that a 3, 4, 1 ¯ \overline{\textsc{a}_{3,4,1}} holds, which we do next. Indeed, since x 1 < 0 x_{1}<0, multiplying Equation 8 by x 1 x_{1} gives

(10) |  | x 1 ​ x 4 ​ y 2 > x 1 ​ x 2 ​ y 4, x_{1}x_{4}y_{2}>x_{1}x_{2}y_{4}, |  |

and as x 4 > 0 x_{4}>0, multiplying Equation 9 by x 4 x_{4} gives

(11) |  | x 4 ​ x 1 ​ y 2 < x 4 ​ x 2 ​ y 1. x_{4}x_{1}y_{2}<x_{4}x_{2}y_{1}. |  |

Then, transitivity over Equations 10 and 11 gives

 | x 1 ​ x 2 ​ y 4 < x 4 ​ x 2 ​ y 1, x_{1}x_{2}y_{4}<x_{4}x_{2}y_{1}, |  |

which dividing by x 2 x_{2} (recalling that x 2 < 0 x_{2}<0) gives x 1 ​ y 4 > x 4 ​ y 1 x_{1}y_{4}>x_{4}y_{1}, which is equivalent to a 3, 4, 1 ¯ \overline{\textsc{a}_{3,4,1}}, as desired.

∎

###### Proof of Proposition 2.

We first prove that it suffices to show it for n = 5 n=5. Indeed, suppose that for some n > 5 n>5 there is an assignment τ \tau of the a i, j, k \textsc{a}_{i,j,k} variables, and θ \theta for the ≺ i, j \prec_{i,j} variables, that satisfies the dynamic-ordering axioms but not the CC axioms. Then, in particular, there is a CC-axiom clause C C that is not satisfied by τ \tau, which involves a set S S of at most 5 5 indices (see Section 2.3). Thus, the restriction of θ ∪ τ \theta\cup\tau to variables whose indices are contained in S S, which we denote by ( θ ∪ τ) | S (\theta\cup\tau)_{|S}, holds ( θ ∪ τ) | S ⊭ C (\theta\cup\tau)_{|S}\nvDash C. On the other hand, if we denote by D S D_{S} the set of clauses of the dynamic-ordering axioms that involve only variables whose indices are in S S, we have ( θ ∪ τ) | S ⊨ D S (\theta\cup\tau)_{|S}\vDash D_{S}. By considering the mapping f: S → { 1, …, | S | } f:S\to\{1,\ldots,|S|\} that maps the i i -th largest index in S S to i i, and letting C f C^{f} (resp. D S f {D^{f}_{S}}) be clauses obtained by replacing each index j j appearing in some variable in C C (resp. D S D_{S}) with its image f ⁡ ( j) f(j), then we have that ( θ ∪ τ) | f ( S) ⊨ D S f (\theta\cup\tau)_{|f(S)}\vDash{D^{f}_{S}} and ( θ ∪ τ) | f ( S) ⊭ C f (\theta\cup\tau)_{|f(S)}\nvDash C^{f}, which would consitute a counterexample with n ≤ 5 n\leq 5. For n = 5 n=5 (which trivially implies the cases with n < 5 n<5), the question reduces to a finite computation, which we carry out as a SAT problem. We start by we creating a formula DOA ​ ( 5) \textsf{DOA}(5), consisting of the dynamic-ordering axioms for n = 5 n=5, and a formula CCA ​ ( 5) \textsf{CCA}(5), consisting of the CC axioms for n = 5 n=5. We then use a Tseitin transformation to negate the CC axioms: for each clause C ∈ CCA ​ ( 5) C\in\textsf{CCA}(5), we introduce a new variable y C y_{C} and add a clause ℓ ¯ ∨ y C ¯ \overline{\ell}\lor\overline{y_{C}} for each literal ℓ \ell in C C, thus ensuring that if clause C C is satisfied by any of its literals, then y C y_{C} is false. Therefore, given that DOA ​ ( 5) \textsf{DOA}(5) is clearly satisfiable, the formula

 | Ψ:= DOA ​ ( 5) ∧ ⋀ C ∈ CCA ​ ( 5) ⋀ ℓ ∈ C ( ℓ ¯ ∨ y C ¯) ∧ ( ⋁ C ∈ CCA ​ ( 5) y C) \Psi:=\textsf{DOA}(5)\land\bigwedge_{C\in\textsf{CCA}(5)}\bigwedge_{\ell\in C}\left(\overline{\ell}\lor\overline{y_{C}}\right)\land\left(\bigvee_{C\in\textsf{CCA}(5)}y_{C}\right) |  |

is satisfiable if and only if there is an assignment τ \tau of the a i, j, k \textsc{a}_{i,j,k} variables and θ \theta for the ≺ i, j \prec_{i,j} variables for which ( τ ∪ θ) (\tau\cup\theta) satisfies the dynamic-ordering axioms, but not the CC axioms. We conclude by running a SAT solver on Ψ \Psi, and finding that Ψ \Psi is unsatisfiable, which proves that no such assignment exists. The code for generating the formulas is available in the repository [github.com/bsubercaseaux/automatic-symmetries][8]. ∎

## Appendix E Pseudocode for Localizer

Some auxiliary functions used by Localizer are presented in Algorithm 1. The main loop of each thread is presented in Algorithm 2. About Algorithm 1, it is worth clarifying that an important point is that when moving a given point p i p_{i}, only the orientation constraints involving p i p_{i} can change whether they are satisfied or not, and thus we can do an O ⁡ ( n 2) O(n^{2}) evaluation, instead of the general O ⁡ ( n 3) O(n^{3}) evaluation.

Algorithm 1 Auxiliary functions for Localizer.

1: An orientation assignment τ: ( n 3) → { − 1, 1 } \tau:\binom{n}{3}\to\{-1,1\}.

2: function Eval ( P, τ P,\tau)

3: u ← 0 u\leftarrow 0 ⊳ \triangleright Number of unsat constraints

4: F ← [0, 0, …, 0] F\leftarrow[0,0,\ldots,0] ⊳ \triangleright Number of unsat constraints per point

5: for all triple of indices 1 ≤ i < j < k ≤ | P | 1\leq i<j<k\leq|P| do

6: if τ ⁡ ( i, j, k) ≠ σ ⁡ ( p i, p j, p k) \tau(i,j,k)\neq\sigma(p_{i},p_{j},p_{k}) then

7: u ← u + 1 u\leftarrow u+1

8: F ⁡ [i], F ⁡ [j], F ⁡ [k] ← F ⁡ [i] + 1, F ⁡ [j] + 1, F ⁡ [k] + 1 F[i],F[j],F[k]\leftarrow F[i]+1,F[j]+1,F[k]+1

9: return u, F u,F

10:

11: function LocalEval ( P, τ, i P,\tau,i)

12: F i ← [0, 0, …, 0] F_{i}\leftarrow[0,0,\ldots,0] ⊳ \triangleright Number of unsat constraints involving p i p_{i} per point

13: for all triple of indices 1 ≤ a < b < c ≤ | P | 1\leq a<b<c\leq|P| with i ∈ { a, b, c } i\in\{a,b,c\} do

14: if τ ⁡ ( a, b, c) ≠ σ ⁡ ( p a, p b, p c) \tau(a,b,c)\neq\sigma(p_{a},p_{b},p_{c}) then

15: F i ​ [a], F i ​ [b], F i ​ [c] ← F i ​ [a] + 1, F i ​ [b] + 1, F i ​ [c] + 1 F_{i}[a],F_{i}[b],F_{i}[c]\leftarrow F_{i}[a]+1,F_{i}[b]+1,F_{i}[c]+1

16: return F i F_{i}

17:

18: function WeightedSample ( A, W A,W)

19: randomly sample i ∈ { 1, …, | A | } i\in\{1,\ldots,|A|\} with probability proportional to W ⁡ [i] + 1 W[i]+1. ⊳ \triangleright The + 1 +1 ensures that all elements can be chosen.

20: return A ⁡ [i] A[i]

Algorithm 2 Localizer Thread

1: An orientation assignment τ: ( n 3) → { − 1, 1 } \tau:\binom{n}{3}\to\{-1,1\}.

2: P ∼ 𝒰 ​ ( [0, 1] 2) n P\sim\mathcal{U}([0,1]^{2})^{n} ⊳ \triangleright Start with n n uniformly random points in [0, 1] 2 [0,1]^{2}.

3: u, F ← Eval ​ ( P, τ) u,F\leftarrow\textsc{Eval}(P,\tau) ⊳ \triangleright u u is the total number of unsat constraints, F F is an array with the number of unsat constraints per point

4: itsSinceCheck ← 0 \textsf{itsSinceCheck}\leftarrow 0 ⊳ \triangleright Number of iterations since last improvement

5: while u > 0 u>0 do

6: ⊳ \triangleright Choose the index of a point to move proportionally to unsat constraints ⊲ \triangleleft

7: i ← WeightedSample ​ ( { 1, …, n }, F) i\leftarrow\textsc{WeightedSample}(\{1,\ldots,n\},F)

8: p ← P ⁡ [i] p\leftarrow P[i]

9: F i ← LocalEval ​ ( P, τ, i) F_{i}\leftarrow\textsc{LocalEval}(P,\tau,i) ⊳ \triangleright Evaluate w.r.t. point p p

10: ⊳ \triangleright Move chosen point with exponentially decreasing radius ⊲ \triangleleft

11: for s ∈ { 0, …, ptMovements } s\in\{0,\ldots,\textsf{ptMovements}\} do

12: r ← max ⁡ { minRadius, maxRadius / 2 s } r\leftarrow\max\{\textsf{minRadius},\textsf{maxRadius}/2^{s}\}

13: p ′ ∼ 𝒰 ⁡ ( B ⁡ ( p, r)) p^{\prime}\sim\mathcal{U}(B(p,r)) ⊳ \triangleright sample from radius- r r ball around p p

14: P ′ ← P ∖ { p } ∪ { p ′ } P^{\prime}\leftarrow P\setminus\{p\}\cup\{p^{\prime}\}

15: F i ′ ← localEval ​ ( P ′, τ, i) F_{i}^{\prime}\leftarrow\textsc{localEval}(P^{\prime},\tau,i)

16: if F i ′ ​ [i] ≤ F i ​ [i] F_{i}^{\prime}[i]\leq F_{i}[i] then

17: P ← P ′ P\leftarrow P^{\prime} ⊳ \triangleright Accept new point even if no strict improvement

18: for all j ∈ { 1, …, n } j\in\{1,\ldots,n\} do ⊳ \triangleright Update unsat per point

19: F ⁡ [j] ← F ⁡ [j] + ( F i ′ ​ [j] − F i ​ [j]) F[j]\leftarrow F[j]+(F_{i}^{\prime}[j]-F_{i}[j])

20: if F i ′ ​ [i] < F i ​ [i] F_{i}^{\prime}[i]<F_{i}[i] then ⊳ \triangleright Strict improvement case

21: u ← u − ( u i − u i ′) u\leftarrow u-(u_{i}-u_{i}^{\prime}) ⊳ \triangleright Update total number of unsat constraints

22: BroadcastToLeaderboard ​ ( P, u) \textsc{BroadcastToLeaderboard}(P,u)

23: itsSinceCheck ← 0 \textsf{itsSinceCheck}\leftarrow 0

24: if u = 0 u=0 then

25: break

26:

27: itsSinceCheck ← itsSinceCheck + 1 \textsf{itsSinceCheck}\leftarrow\textsf{itsSinceCheck}+1

28: ⊳ \triangleright If no improvement in a while, restart from a good solution. ⊲ \triangleleft

29: if itsSinceCheck > restartThreshold \textsf{itsSinceCheck}>\textsf{restartThreshold} then

30: newStart ← WeightedSample ​ ( leaderboardSols, leaderboardScores) \textsf{newStart}\leftarrow\textsc{WeightedSample}(\textsf{leaderboardSols},\textsf{leaderboardScores})

31: ⊳ \triangleright Perturb solution to increase diversity ⊲ \triangleleft

32: for all i ∈ { 1, …, n } i\in\{1,\ldots,n\} do

33: P ⁡ [i] ∼ 𝒰 ⁡ ( B ⁡ ( newStart ​ [i], resetRadius)) P[i]\sim\mathcal{U}(B(\textsf{newStart}[i],\textsf{resetRadius}))

34: u, F ← Eval ​ ( P, τ) u,F\leftarrow\textsc{Eval}(P,\tau)

35: return P P


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: http://orcid.org/0000-0003-2295-1299
[4]: http://orcid.org/0009-0005-9130-6797
[5]: http://orcid.org/0000-0003-1567-3948
[6]: http://orcid.org/0000-0002-5587-8801
[7]: mailto:%7Bbsuberca,ethanmac,longq,mheule%7D@andrew.cmu.edu
[8]: https://github.com/bsubercaseaux/automatic-symmetries
[9]: https://github.com:jreeves3/allsat-cadical
[10]: http://en.wikipedia.org/w/index.php?title=Happy%20ending%20problem&amp;oldid=1282669476
