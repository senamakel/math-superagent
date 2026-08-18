<!-- source: https://doi.org/10.1007/s00010-026-01307-4 | converted from HTML -->

Inscribed rhombi having diagonals collinear with specified points | Aequationes mathematicae | Springer Nature Link

Skip to main content

# Inscribed rhombi having diagonals collinear with specified points

- [Open access][1]
- Published: 03 June 2026

- Volume 100, article number 58 ( 2026)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Aequationes mathematicae][5] [Aims and scope][6] [Submit manuscript][7]

Inscribed rhombi having diagonals collinear with specified points

[Download PDF][2]

## Abstract

We investigate the question of whether a simple closed curve in the plane must contain all four vertices of some rhombus having one diagonal collinear with a specified point. This complements previous research on whether there is a rhombus with a diagonal or side parallel to a given line. We obtain a new proof that a simple closed curve contains the vertices of uncountably many rhombi. We also explore conditions guaranteeing that all points in some region are collinear with diagonals of such rhombi.

### Similar content being viewed by others

### [On integral points on degree four del Pezzo surfaces][8]

Article 01 October 2017

### [Some remarks on the simplicial volume of nonpositively curved manifolds][9]

Article 13 April 2020

### [A Discrete Collocation Method for a Hypersingular Integral Equation on Curves with Corners][10]

Chapter © 2018

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algebraic Geometry][11]
- [Combinatorial Geometry][12]
- [Differential Geometry][13]
- [Geometry][14]
- [Polytopes][15]
- [Projective Geometry][16]
- [Combinatorial Structures and Intersection Theorems][17]

## 1 Introduction

Otto Toeplitz [[10][18]] famously asked whether every Jordan curve contains the vertices of some square. Such a square is said to be *inscribed*in the curve, even though the curve may not circumscribe the square. Matschke ( [[4][19], [5][20]]) provides detailed surveys of the literature seeking to resolve the conjecture.

For some special classes of curves, the existence of an inscribed square has been proved by focusing on families of inscribed rhombi ( [[1][21], [2][22], [9][23]]). Motivated by such work, Nielsen [[6][24]] proved that for every Jordan curve and every given line, the curve admits an inscribed rhombus with *one side parallel to that line*. More recently, Fung [[3][25]] considered whether a Jordan curve must have an inscribed rhombus with *a diagonal parallel to a given line*and was able to show there is always an uncountable family of non-parallel lines for which this happens.

In the present work, we focus on finding a rhombus with a *diagonal passing through a given point*outside the convex hull of the Jordan curve. We prove that this is always possible under suitable assumptions on the relative positions of the point and curve. Among these are the following cases: the curve admits a differentiable parametrization with non-vanishing derivative; each point on the boundary of the convex hull has a unique supporting line; the curve is convex with no acute interior angles; or the curve is polygonal in some neighborhood of each extreme point of its convex hull. Under mild assumptions on the curve, every point outside some compact set is collinear with the diagonal of an inscribed rhombus. Moreover, our approach suffices to prove once again that there are uncountably many rhombi inscribed in a general Jordan curve.

The next section introduces our general notation. Section [3][26] defines and illustrates our framework for seeking inscribed rhombi when given a specific curve and point. We present basic existence criteria in § [4][27] and then use those criteria in § [5][28] to prove uncountability. Sections [6][29] and [7][30] develop, respectively, intuitive regularity and geometric conditions guaranteeing that every point outside some compact set is collinear with the diagonal of at least one inscribed rhombus. An appendix provides additional details about the regularity condition.

## 2 Notation

We work mainly in the Cartesian plane \(\mathbb {R}^2\), where we parametrize unit vectors in two ways by

$$ {{\,\mathrm{\textbf{x}}\,}}(\theta ) := \begin{bmatrix}\cos \theta \\ \sin \theta \end{bmatrix}, \qquad {{\,\mathrm{\textbf{y}}\,}}(\theta ) := {{\,\mathrm{\textbf{x}}\,}}(\theta -\pi /2) = \begin{bmatrix}-\sin \theta \\ \cos \theta \end{bmatrix}. $$

Observe that \({{\,\mathrm{\textbf{x}}\,}}(\theta )\perp {{\,\mathrm{\textbf{y}}\,}}(\theta )\). We use the identities

$$ {{\,\mathrm{\textbf{x}}\,}}(\theta )\cdot {{\,\mathrm{\textbf{x}}\,}}(\hat{\theta }) = {{\,\mathrm{\textbf{y}}\,}}(\theta )\cdot {{\,\mathrm{\textbf{y}}\,}}(\hat{\theta }) = \cos (\theta -\hat{\theta }), \qquad {{\,\mathrm{\textbf{x}}\,}}(\theta )\cdot {{\,\mathrm{\textbf{y}}\,}}(\hat{\theta }) = \sin (\theta -\hat{\theta }) $$

without explicit mention in later sections. Writing \({{\,\textrm{mid}\,}}(u,v):= (u+v)/2\), we note that

$$\begin{aligned} {{\,\textrm{mid}\,}}({{\,\mathrm{\textbf{x}}\,}}(\theta ),{{\,\mathrm{\textbf{x}}\,}}(\hat{\theta })) = \cos ([\theta - \hat{\theta }]/2) \;{{\,\mathrm{\textbf{x}}\,}}([\theta + \hat{\theta }]/2), \end{aligned}$$

(1)

$$\begin{aligned} {{\,\textrm{mid}\,}}(\varrho {{\,\mathrm{\textbf{x}}\,}}(\theta ),\hat{\varrho }{{\,\mathrm{\textbf{x}}\,}}(\theta )) = [(\varrho + \hat{\varrho })/2] {{\,\mathrm{\textbf{x}}\,}}(\theta ). \end{aligned}$$

(2)

We let \({{\,\textrm{mid}\,}}[M]\) denote the image of a set \(M \subseteq \mathbb {R}^2 \times \mathbb {R}^2\) under \({{\,\textrm{mid}\,}}(\cdot )\). More generally, *g*[*S*] is the image of a set *S*under a function *g*, whereas \(g|_S\) is the restriction of *g*to *S*.

The Euclidean norm on \(\mathbb {R}^2\) is denoted \(\Vert \cdot \Vert \). We denote the interior and boundary of *Q*by \({{\,\textrm{Int}\,}}Q\) and \(\partial Q\), respectively. To each nonempty set \(Q\subseteq \mathbb {R}^2\) we associate a function \(\mathbb {R}^2 \rightarrow [0,\pi ]\) defined by

$$ u \mapsto {{\,\textrm{sweep}\,}}(u\,|\,Q) := \sup \left\{ \!\left. \arccos \left( \frac{(v-u)\cdot (w-u)}{\Vert v-u\Vert \Vert w-u\Vert } \right) \right| \, v,w\in Q\setminus \{u\} \right\} . $$

For a convex polygon *Q*and \(u \in \partial Q\), the value of \({{\,\textrm{sweep}\,}}(u\,|\,Q)\) is the interior angle at *u*. Notice that \({{\,\textrm{sweep}\,}}(u\,|\,Q)\) is unchanged if we replace *Q*with its convex hull \({{\,\textrm{Conv}\,}}Q\).

If \(Q \subseteq \mathbb {R}^2\) is compact and convex, then the *face of Q containing u*is denoted

$$ {{\,\textrm{Face}\,}}(u\,|\, Q) := \{ u_0 \in Q \mid \exists u_1 \in Q, \lambda \in (0,1) : u = (1-\lambda )u_0 +\lambda u_1 \}. $$

If \(u \in \partial Q\) then either *u*is an extreme point of *Q*with \({{\,\textrm{Face}\,}}(u\,|\, Q) = \{u\}\) or *u*is not an extreme point and \({{\,\textrm{Face}\,}}(u\,|\, Q)\) is a closed line segment with endpoints at distinct extreme points of \(Q \setminus \{u\}\). The other cases (namely, \(u\not \in Q\) or \(u \in {{\,\textrm{Int}\,}}Q\)) will not be of interest here.

Our arguments involve angles of rotation about a given point that varies by context, so we introduce polar-coordinate notation to provide suitable flexibility. Consider a non-collinear set \(Q \subset \mathbb {R}^2\) and a point *z*outside the (nonempty) interior of \({{\,\textrm{Conv}\,}}Q\). There exist unique scalars \(\varrho _z^-(Q)\), \(\varrho _z^+(Q)\), \(\theta _z^-(Q)\), \(\theta _z^+(Q)\) with

$$ 0 \le \varrho _z^-(Q)< \varrho _z^+(Q), \qquad -\pi \le \theta _z^-(Q) \le \theta _z^+(Q) \le \theta _z^-(Q)+\pi < 2\pi $$

such that each \(u \in {{\,\textrm{Conv}\,}}(Q\cup \{z\})\setminus \{z\}\) may be written as \(u = z+\varrho _z(u) {{\,\mathrm{\textbf{x}}\,}}(\theta _z(u))\) for unique choices of radius \(\varrho _z(u):= \Vert u-z\Vert \in [0,\varrho _z^+(Q)]\) and angle

$$\begin{aligned} \theta _z(u) := \theta _z^-(Q)&+ \arccos ({{\,\mathrm{\textbf{x}}\,}}(\theta _z^-(Q))\cdot (u-z) / \varrho _z(u)) \\ = \theta _z^+(Q)&- \arccos ({{\,\mathrm{\textbf{x}}\,}}(\theta _z^+(Q))\cdot (u-z) / \varrho _z(u)) \in [\theta _z^-(Q),\theta _z^+(Q)]. \end{aligned}$$

In particular, *Q*lies in the annular (or circular) section

$$ {{\,\textrm{Ann}\,}}_z Q := \{ u \mid \varrho _z^-(Q) \le \varrho _z(u) \le \varrho _z^+(Q), \; \theta _z^-(Q) \le \theta _z(u) \le \theta _z^+(Q) \} $$

because \(\varrho _z(u) \in [\varrho _z^-(Q),\varrho _z^+(Q)]\) for all \(u \in {{\,\textrm{Conv}\,}}Q\). For each \(u \in {{\,\textrm{Ann}\,}}_z Q\) and \(\psi >0\) we define a closed neighborhood of \(u \not =z\) by

$$ {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) := \{ z+\varrho {{\,\mathrm{\textbf{x}}\,}}(\theta ) \mid 0\le \varrho ,\; |\theta -\theta _z(u)| \le \psi \}. $$

Finally, we let \({{\,\textrm{Ann}\,}}_z^*Q := \{ u \in {{\,\textrm{Ann}\,}}_z Q \mid {{\,\textrm{sweep}\,}}(u\,|\,Q) < \pi \}\) comprise the four ‘corners’ of \({{\,\textrm{Ann}\,}}_z Q\) at which \(\varrho _z(\cdot )\) and \(\theta _z(\cdot )\) together attain extremes over *Q*. Observe that members of \(Q \cap {{\,\textrm{Ann}\,}}_z^*Q\) are extreme points of \({{\,\textrm{Conv}\,}}Q\).

## 3 Families of chords

We now describe our framework for finding a rhombus. Throughout this section, we fix a Jordan curve *J*and a point \(z \not \in {{\,\textrm{Conv}\,}}J\). An inscribed rhombus in *J*corresponds to an orthogonal pair of chords in *J*sharing a midpoint. Such a rhombus has a diagonal collinear with *z*if and only if one chord is collinear with *z*and the other chord’s endpoints are equidistant from *z*. Our rhombus-existence proofs amount to constructing connected families of both types of chords in *J*and then finding a pair where their midpoints agree.

By the correspondence of chords to endpoint pairs, we consider sets of the form

$$\begin{aligned} D&:= \{ (d_\textrm{n},d_\textrm{f}) \in G_\textrm{n}\times G_\textrm{f} \mid \theta _z(d_\textrm{n}) = \theta _z(d_\textrm{f}) \} , \end{aligned}$$

(3)

$$\begin{aligned} E&:= \{ (e_\textrm{c},e_\textrm{a}) \in G_\textrm{c}\times G_\textrm{a} \mid \varrho _z(e_\textrm{c}) = \varrho _z(e_\textrm{a}) \} \end{aligned}$$

(4)

for selected arcs \(G_\textrm{n}, G_\textrm{f}, G_\textrm{c}, G_\textrm{a}\) in *J*. In the notation of our framework, use of the letters ‘c’ and ‘a’ (upper or lower case, any font) is intended to suggest objects that are further in the clockwise and anti-clockwise orientation, respectively, about *z*. The letters ‘f’ and ‘n’ indicate objects that are respectively farther from *z*and nearer to *z*. We associate the letter ‘d’ with chords in *J*that could be diagonals collinear with *z*; the letter ‘e’ refers to chords whose endpoints are equidistant from *z*.

Note that true chords require \(d_\textrm{n} \not = d_\textrm{f}\) and \(e_\textrm{c} \not = e_\textrm{a}\) in the definitions of *D*and *E*in ( [3][31])–( [4][32]). We allow equality to ensure compactness for existence arguments, opting instead to handle degenerate pairs (*d*, *d*) or (*e*, *e*) as they arise. Our specific choice of arcs \(G_\textrm{n}, G_\textrm{f}, G_\textrm{c}, G_\textrm{a}\) will assist with both considerations. First we label four sub-arcs in the boundary of the enclosing annular section \({{\,\textrm{Ann}\,}}_z J\):

$$\begin{aligned} N := \{ n \in \partial \!{{\,\textrm{Ann}\,}}_z J \mid \varrho _z(n) = \varrho _z^-(J) \}, \quad F := \{ f \in \partial \!{{\,\textrm{Ann}\,}}_z J \mid \varrho _z(f) = \varrho _z^+(J) \},\\ C := \{ c \in \partial \!{{\,\textrm{Ann}\,}}_z J \mid \theta _z(c) = \theta _z^-(J) \},\quad A := \{ a \in \partial \!{{\,\textrm{Ann}\,}}_z J \mid \theta _z(a) = \theta _z^+(J) \}. \end{aligned}$$

Next, we label the extremes of *J*within those boundary arcs:

-

\(n_\textrm{c}\) and \(n_\textrm{a}\) minimize and maximize \(\theta _z(n)\) over \(n \in J\cap N\);

-

\(f_\textrm{c}\) and \(f_\textrm{a}\) minimize and maximize \(\theta _z(f)\) over \(f \in J\cap F\);

-

\(c_\textrm{n}\) and \(c_\textrm{f}\) minimize and maximize \(\varrho _z(c)\) over \(c \in J\cap C\);

-

\(a_\textrm{n}\) and \(a_\textrm{f}\) minimize and maximize \(\varrho _z(a)\) over \(a \in J\cap A\).

Those points are identified in Figure [1][33] for an example of *J*and *z*.

**Fig. 1**

[image: Fig. 1]

[Full size image][34]

A Jordan curve and circumscribing annular section relative to a point

Finally, we define the sub-arcs of *J*:

-

\(G_\textrm{n}\) is the arc in *J*from \(c_\textrm{n}\) to \(a_\textrm{n}\) having the property that for every \(u \in J \setminus G_\textrm{n}\) there exists \(v \in G_\textrm{n}\) with \(\varrho _z(v) < \varrho _z(u)\);

-

\(G_\textrm{f}\) is the arc in *J*from \(c_\textrm{f}\) to \(a_\textrm{f}\) having the property that for every \(u \in J \setminus G_\textrm{f}\) there exists \(v \in G_\textrm{f}\) with \(\varrho _z(v) > \varrho _z(u)\);

-

\(G_\textrm{c}\) is the arc in *J*from \(n_\textrm{c}\) to \(f_\textrm{a}\) having the property that for every \(u \in J \setminus G_\textrm{c}\) there exists \(v \in G_\textrm{c}\) with \(\theta _z(v) < \theta _z(u)\);

-

\(G_\textrm{a}\) is the arc in *J*from \(n_\textrm{a}\) to \(f_\textrm{c}\) having the property that for every \(u \in J \setminus G_\textrm{a}\) there exists \(v \in G_\textrm{a}\) with \(\theta _z(v) > \theta _z(u)\).

The arcs \(G_\textrm{n}\) and \(G_\textrm{f}\) connect the two flat sides *C*and *A*of \({{\,\textrm{Ann}\,}}_z J\), with \(G_\textrm{n}\) nearer to *z*than \(G_\textrm{f}\). The closures of \(G_\textrm{c} \setminus (G_\textrm{c} \cap G_\textrm{a})\) and \(G_\textrm{a} \setminus (G_\textrm{c} \cap G_\textrm{a})\) connect the inner circle of the annulus to the outer circle, with the former arc further clockwise than the latter rotationally about *z*. These arcs are illustrated in Figure [2][35]. Notice that \(G_\textrm{c} \cap G_\textrm{a}\) is the sub-arc of *J*from \(f_\textrm{c}\) to \(f_\textrm{a}\) that misses *N*.

**Fig. 2**

[image: Fig. 2]

[Full size image][36]

Sub-arcs selected from the Jordan curve of Figure [1][33]

**Fig. 3**

[image: Fig. 3]

[Full size image][37]

Illustration of *D*showing some chords with endpoints at the same angle of rotation about *z*and a path of such midpoints

The definition ( [3][31]) of *D*in terms of \(G_\textrm{f}\) and \(G_\textrm{n}\) is illustrated in Figure [3][38], which shows a small sample of chords in *D*. It highlights the midpoints of those specific chords and presents a path of such chordal midpoints in \({{\,\textrm{mid}\,}}[D]\). The points defined as \(\bar{c} := {{\,\textrm{mid}\,}}(c_\textrm{n},c_\textrm{f}) \in C\) and \(\bar{a} := {{\,\textrm{mid}\,}}(a_\textrm{n},a_\textrm{f}) \in A\) are also shown in Figure [3][38]. Notice that \(\bar{c},\bar{a} \in \partial {{\,\textrm{Conv}\,}}J \cap {{\,\textrm{mid}\,}}[D]\) and that the path in \({{\,\textrm{mid}\,}}[D]\) spans the annular section \({{\,\textrm{Ann}\,}}_z J\), reaching from \(\bar{c}\) to \(\bar{a}\). Those two points will be of special interest below.

**Fig. 4**

[image: Fig. 4]

[Full size image][39]

Illustration of *E*showing some chords with endpoints equidistant from *z*and a path of such midpoints

Similarly, Figure [4][40] shows a sample of chords in *E*and a path in \({{\,\textrm{mid}\,}}[E]\). By the curvature of the circular arcs, the points \({{\,\textrm{mid}\,}}(n_\textrm{a},n_\textrm{c})\) and \({{\,\textrm{mid}\,}}(f_\textrm{a},f_\textrm{c})\) are closer to *z*than their respective endpoints unless the chords degenerate to a point.

Elements of \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\) are potential centers of rhombi inscribed in *J*having diagonals collinear with *z*, as shown in Figure [5][41].

**Fig. 5**

[image: Fig. 5]

[Full size image][42]

Intersections of the chordal-midpoint paths from Figures [3][38] – [4][40] and three inscribed rhombi with centers at such intersections

But in general, members of \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\) are merely candidates for inscribed rhombi and may instead yield points (degenerate rhombi) at the corners of \({{\,\textrm{Ann}\,}}_z J\). However, the specific construction above of the chord families *D*and *E*constrains the ways in which \({{\,\textrm{mid}\,}}[D]\) and \({{\,\textrm{mid}\,}}[E]\) can meet at the boundary of the annular section \({{\,\textrm{Ann}\,}}_z J\). Our first result records the essential facts about degeneracy.

### Lemma 3.1

Define \(U^* := \{\bar{c},\bar{a}\} \cap (N \cup F) \cap {{\,\textrm{mid}\,}}[E] \subsetneq {{\,\textrm{Ann}\,}}_z^* J\). The following are always true:

1. (a)

If \(\bar{c} \in N \cup F\), then \(J \cap C = \{\bar{c}\}\). If \(\bar{a} \in N \cup F\), then \(J \cap A = \{\bar{a}\}\). If \({{\,\textrm{mid}\,}}[E] \cap N\) meets \(C \cup A\), then \({{\,\textrm{mid}\,}}[E] \cap N = J \cap N\) and it is a singleton.

2. (b)

Each element of \(U^*\) has one of these four forms: \(\bar{a} = f_\textrm{a} = a_\textrm{f} = a_\textrm{n}\), \(\bar{c} = f_\textrm{c} = c_\textrm{f} = c_\textrm{n}\), \(\bar{a} = \bar{n} = n_\textrm{a} = n_\textrm{c} = a_\textrm{f} = a_\textrm{n}\), or \(\bar{c} = \bar{c} = n_\textrm{a} = n_\textrm{c} = c_\textrm{f} = c_\textrm{n}\).

3. (c)

The set \(U^*\) has 0, 1 or 2 elements, whereas \(U^* \cap F\) has 2 elements if and only if \(\bar{c}, \bar{a} \in F\).

4. (d)

If \((d,d) \in D\), then \(d \in \{\bar{a}, \bar{c}\}\). If \((e,e) \in E\), then \(e \in N \cup F\).

5. (e)

If \(s \in {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\) and \((s,s) \in D \cup E\) then \((s,s) \in D \cap E\) and \(s \in U^*\).

### Proof

The definitions lead immediately to conclusions (a)–(d). For (e), we may write \(s = {{\,\textrm{mid}\,}}(d_\textrm{n},d_\textrm{f}) = {{\,\textrm{mid}\,}}(e_\textrm{c},e_\textrm{a})\) for some choice of \((d_\textrm{n},d_\textrm{f}) \in D\) and \((e_\textrm{c},e_\textrm{a}) \in E \). Equations ( [1][43])–( [2][44]) imply

$$\begin{aligned} \theta _z({{\,\textrm{mid}\,}}(d_\textrm{n},d_\textrm{f}))&= \theta _z(d_\textrm{n}), \end{aligned}$$

(5)

$$\begin{aligned} \varrho _z({{\,\textrm{mid}\,}}(d_\textrm{n},d_\textrm{f}))&= [\varrho _z(d_\textrm{n})+\varrho _z(d_\textrm{f})]/2, \end{aligned}$$

(6)

$$\begin{aligned} \theta _z({{\,\textrm{mid}\,}}(e_\textrm{c},e_\textrm{a}))&= [\theta _z(e_\textrm{c}) + \theta _z(e_\textrm{a})]/2, \end{aligned}$$

(7)

$$\begin{aligned} \varrho _z({{\,\textrm{mid}\,}}(e_\textrm{c},e_\textrm{a}))&= \varrho _z(e_\textrm{a})\cos ([\theta _z(e_\textrm{c})- \theta _z(e_\textrm{a})]/2) \end{aligned}$$

(8)

First suppose \((s,s) \in D\). Conclusion (d) tells us that \(s \in \{\bar{a},\bar{c}\}\), so ( [7][45]) implies \(\theta _z(s) = \theta _z(e_\textrm{c}) = \theta _z(e_\textrm{a})\). But then ( [8][46]) gives us \(\varrho _z(s) = \varrho _z(e_\textrm{c}) = \varrho _z(e_\textrm{a})\), proving that \(s = e_\textrm{c} = e_\textrm{a} \in (J \cap F) \cup ({{\,\textrm{mid}\,}}[E] \cap N)\) and \((s,s) \in E\). Now ( [6][47]) implies \(\varrho _z(s) = \varrho _z(d_\textrm{n}) = \varrho _z(d_\textrm{f})\) and therefore \(s = d_\textrm{n} = d_\textrm{f}\), as claimed. A similar argument applies when \((s,s) \in E\): \(s \in (J \cap F) \cup ({{\,\textrm{mid}\,}}[E] \cap N)\) by conclusion (d), so ( [5][48])–( [6][47]) lead to \(s = d_\textrm{f} = d_\textrm{n} \in \{\bar{a}, \bar{c}\}\) and then also to \(s = e_\textrm{c} = e_\textrm{a}\). \(\square \)

We now summarize the framework above. Elements \((s,\hat{s}) \in D \cup E\) with \(s \not = \hat{s}\) give endpoints for chords of *J*. If chords from *D*and *E*share a midpoint, then they are orthogonal and give diagonals of a rhombus inscribed in *J*having one diagonal collinear with *z*. If no such rhombus exists, then \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E] \subseteq U^*\). Therefore our overarching goals for the rest of the paper are threefold: show that \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\) is always nonempty; find criteria ensuring that \(U^*\) is empty; and address situations where \(U^*\) is nonempty.

## 4 Basic existence results

The graphical evidence in the previous section suggests that \({{\,\textrm{mid}\,}}[D]\) and \({{\,\textrm{mid}\,}}[E]\) are likely to meet. In this section we verify that intuition by topological arguments similar to those used by Wright [[11][49]] when proving the theorems of Nielsen [[6][24]] and Fung [[3][25]].

Here is the fundamental concept behind our proof of existence. We say that planar sets *Q*and \(\widehat{Q}\) are *cyclically co-circumscribed*if there exists a Jordan curve \(J_0\) and a 4-tuple \((u,v;\hat{u},\hat{v}) \in Q^2 \times \widehat{Q}^2\) such that the following conditions are satisfied:

1. 1.

*Q*and \(\widehat{Q}\) are contained in the union of \(J_0\) with the bounded component of the complement of \(J_0\);

2. 2.

\(u \not = v\) and \(\hat{u} \not = \hat{v}\), with \(u, \hat{u}, v, \hat{v}\) appearing in that cyclic order (clockwise or anti-clockwise) on \(J_0\).

We say that *Q*and \(\widehat{Q}\) are cyclically co-circumscribed at \((u,v;\hat{u},\hat{v})\) if there exists such \(J_0\), and we say that *Q*and \(\widehat{Q}\) are cyclically co-circumscribed by \(J_0\) if there exists such \((u,v;\hat{u},\hat{v})\).

That concept sets the stage for the following well-known consequence of the Jordan curve theorem. Recall that a *continuum*(plural: *continua*) is a nonempty compact connected metric space.

### Lemma 4.1

If plane continua *K*and \(\widehat{K}\) are cyclically co-circumscribed, then they have nonempty intersection.

We shall see below that at least one such an arrangement is always present in the framework of § [3][26]. To construct cyclically co-circumscribed continua in that context, we rely on the next two lemmas. The first is an immediate consequence of Corollary 2.3 of [[7][50]] or Observation (i) of [[8][51]].

### Lemma 4.2

For \(i=1,2\) consider arcs \(H_i \subseteq \mathbb {R}^n\) with endpoints \(u_i\) and \(v_i\). If \(\zeta _i: H_i \rightarrow [\alpha ,\beta ]\) is a continuous function with \(\zeta _i(u_i)=\alpha \) and \(\zeta _i(v_i)=\beta \), then \((u_1,u_2)\) and \((v_1,v_2)\) lie in the same connected component of

$$ \left\{ \left. \! (w_1,w_2) \in H_1 \times H_2 \,\right| \, \zeta _1(w_1) = \zeta _2(w_2) \right\} . $$

Note that a connected component of a compact metric space is a continuum.

### Lemma 4.3

(Corollary 3.2 of [[7][50]]) Consider closed subsets \(Q_1\) and \(Q_2\) of a continuum \(\widehat{K}\). If \(Q_1\) and \(Q_2\) are disjoint, then some sub-continuum *K*of \(\widehat{K}\) meets both \(Q_1\) and \(Q_2\) but misses the interiors of \(Q_1\) and \(Q_2\).

We are now ready for our core existence result, which is stated in terms of the notation introduced in § [3][26]

### Theorem 4.4

Given any \(f \in F \cap J\), there exist \(\bar{n} \in N \cap {{\,\textrm{mid}\,}}[E]\) along with continua \(\widehat{D} \subseteq D\) and \(\widehat{E} \subseteq E\) for which

-

\((c_\textrm{n},c_\textrm{f}), (a_\textrm{n},a_\textrm{f}) \in \widehat{D}\) and \((f,f) \in \widehat{E}\);

-

(*f*, *f*) is the only point of the form \((e,e) \in \widehat{E} \cap (F\times F)\);

-

\({{\,\textrm{mid}\,}}[\widehat{D}],{{\,\textrm{mid}\,}}[\widehat{E}]\) are cyclically co-circumscribed by \(\partial \! {{\,\textrm{Ann}\,}}_z J\) at \((\bar{c}, \bar{a}; f, \bar{n})\).

In particular, \({{\,\textrm{mid}\,}}[\widehat{D}] \cap {{\,\textrm{mid}\,}}[\widehat{E}]\) is nonempty.

### Proof

First we obtain a connected component \(\widehat{D}\) of *D*by applying Lemma [4.2][52] with the choices \((H_1,H_2) = (G_\textrm{n},G_\textrm{f})\), \((u_1,u_2) = (c_\textrm{n},c_\textrm{f})\), \((v_1,v_2) = (a_\textrm{n},a_\textrm{f})\), \(\zeta _i = \theta _z(\cdot )\), \(\alpha = \theta _z^-(J)\) and \(\beta = \theta _z^+(J)\). We see that \({{\,\textrm{mid}\,}}[\widehat{D}]\) is a continuum because it is the continuous image of a continuum.

Our construction of \(\widehat{E}\) is somewhat more complicated by the nonconvexity of \({{\,\textrm{Ann}\,}}_z J\) exhibited at its boundary arc *N*. Define \(\widetilde{G}_\textrm{c}\) to be the sub-arc of \(G_\textrm{c}\) from \(n_\textrm{c}\) to *f*; similarly, let \(\widetilde{G}_\textrm{a}\) be the sub-arc of \(G_\textrm{a}\) from \(n_\textrm{c}\) to *f*. Clearly, (*f*, *f*) is the only point of the form \((e,e) \in (\widetilde{G}_\textrm{c} \times \widetilde{G}_\textrm{a})\cap ( F \times F)\). We obtain a connected component \(\widetilde{E}\) of *E*by applying Lemma [4.2][52] with the choices \((H_1,H_2) = (\widetilde{G}_\textrm{c},\widetilde{G}_\textrm{a})\), \((u_1,u_2) = (n_\textrm{c},n_\textrm{a})\), \((v_1,v_2) = (f,f)\), \(\zeta _i = \varrho _z(\cdot )\), \(\alpha = \varrho _z^-(J)\) and \(\beta = \varrho _z^+(J)\). Lemma [4.3][53] then yields a sub-continuum \(\widehat{E} \subseteq \widetilde{E}\) satisfying \(\varrho _z^-(J) \le \varrho _z({{\,\textrm{mid}\,}}(e_\textrm{c},e_\textrm{a})) \le \varrho _z^+(J)\) for all \((e_\textrm{c},e_\textrm{a}) \in \widehat{E}\); we may choose \(\widehat{E}\) so it contains (*f*, *f*) and a point \((\hat{e}_\textrm{c},\hat{e}_\textrm{a})\) with \(\varrho _z^-(J) = \varrho _z({{\,\textrm{mid}\,}}(\hat{e}_\textrm{c},\hat{e}_\textrm{a}))\). Again, \({{\,\textrm{mid}\,}}[\widehat{E}]\) is continuum. Take \(\bar{n} = {{\,\textrm{mid}\,}}(\hat{e}_\textrm{c},\hat{e}_\textrm{a})\).

Finally, the construction in § [3][26] ensures that \(\bar{a} \not = \bar{c}\) and \(f \not = \bar{n}\). It also implies that \(\bar{c},\bar{n},\bar{a}, f\) appear in that cyclic order around the boundary of \({{\,\textrm{Ann}\,}}_z J\). In particular, Lemma [4.1][54] now applies. \(\square \)

Recall that members of \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\) are merely *candidates*for the centers of inscribed rhombi: they might instead give points at the corners of \({{\,\textrm{Ann}\,}}_z J\). That suggests our first concrete criterion ensuring non-degeneracy.

### Corollary 4.5

If *J*misses \({{\,\textrm{Ann}\,}}_z^* J\) then *J*admits an inscribed rhombus having one diagonal collinear with *z*.

### Proof

Recall that \(U^* \subseteq {{\,\textrm{Ann}\,}}_z^* J\) by definition of the former in § [3][26], so the hypothesis implies \(U^*\) is empty. By Theorem [4.4][55] there is a point \(s \in {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\). By Lemma [3.1][56] (e), we have \((s,s) \not \in D\cup E\). Hence, *s*corresponds to a rhombus rather than merely a point or line segment. \(\square \)

On the other hand, if *J*does not miss \({{\,\textrm{Ann}\,}}_z^* J\) then we must consider the behavior of *J*near points in \({{\,\textrm{Ann}\,}}_z^* J\). For that purpose we make the following observation, which underpins the regularity assumption explored in § [6][29].

### Lemma 4.6

If \(H_\textrm{n} \subset G_\textrm{n}\), \(H_\textrm{f} \subset G_\textrm{f}\), \(H_\textrm{c} \subset G_\textrm{c}\) and \(H_\textrm{a} \subset G_\textrm{a}\) are arcs satisfying with \(H_\textrm{n} \cap H_\textrm{f} = H_\textrm{c} \cap H_\textrm{a} = \{u\} \subseteq U^*\), then there exists \(\psi > 0\) so that

$$\begin{aligned} {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) \subseteq {{\,\textrm{mid}\,}}[ D\cap (H_\textrm{n}\times H_\textrm{f}) ],\\ {{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) \subseteq {{\,\textrm{mid}\,}}[ E\cap (H_\textrm{c}\times H_\textrm{a}) ]. \end{aligned}$$

### Proof

For \(H:= H_\textrm{n} \cup H_\textrm{f} \cup H_\textrm{c} \cup H_\textrm{a}\), define \(\phi := \inf \big \{ |\theta _z(v)-\theta _z(u)| \,\big |\, v \in J \setminus H \big \}\). Then the closure of \(J \setminus H\) misses \(\{ v= z+\varrho {{\,\mathrm{\textbf{x}}\,}}(\theta ) \mid \varrho _z^-(J) \le \varrho ,\; \theta _z(v) = \theta _z(u) \}\) because the latter is closed and meets *J*only at *u*. Therefore \(w \in H\) whenever \(w \in J\) and \(|\theta _z(w) - \theta _z(u)| < \phi \). Also, \(\phi >0\). Choose \(\psi \in (0,\phi /2)\). Now consider \(v \in {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\). Writing \(v = (d_\textrm{n}+d_\textrm{f})/2\) for \((d_\textrm{n},d_\textrm{f}) \in D\), we have \(\theta _z(v) = \theta _z(d_\textrm{n}) = \theta _z(d_\textrm{f})\) by ( [5][48]). Thus \(|\theta _z(w) - \theta _z(u)| < \phi \) for \(w \in \{d_\textrm{n},d_\textrm{f}\} \subset J\), implying that \((d_\textrm{n},d_\textrm{f}) \in H_\textrm{n}\times H_\textrm{f}\). Hence \(v \in {{\,\textrm{mid}\,}}[H_\textrm{n}\times H_\textrm{f}]\). Next consider \(v \in {{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\). If we write \(v = (e_\textrm{c}+e_\textrm{a})/2\) with \((e_\textrm{c},e_\textrm{a}) \in E\), then \(\theta _z(v) = (\theta _z(e_\textrm{c})+\theta _z(e_\textrm{a}))/2\) by ( [7][45]). Observe that \(|\theta _z(e_\textrm{c})-\theta _z(v)| = |\theta _z(e_\textrm{a})-\theta _z(v)| < |\theta _z(v)-\theta _z(u)|\) implies

$$\begin{aligned} |\theta _z(e_\textrm{c})-\theta _z(v)|< 2|\theta _z(v)-\theta _z(u)|< \phi ,\\ |\theta _z(e_\textrm{a})-\theta _z(u)|< 2|\theta _z(v)-\theta _z(u)| < \phi . \end{aligned}$$

Thus \(|\theta _z(w) - \theta _z(u)| < \phi \) for \(w \in \{e_\textrm{c}, e_\textrm{a}\} \subset J\), so that \((e_\textrm{c},e_\textrm{a}) \in H_\textrm{c}\times H_\textrm{a}\). Therefore \(v \in {{\,\textrm{mid}\,}}[H_\textrm{c}\times H_\textrm{a}]\). \(\square \)

We end this section with two simple scenarios that will be instrumental in the sequel.

### Proposition 4.7

Consider points \(a,f,c,n \in J\) satisfying

$$\begin{aligned} \theta _z(c) = \theta _z^-(J), \quad \theta _z(a) = \theta _z^+(J), \quad \varrho _z(n) = \varrho _z^-(J), \quad \varrho _z(f) = \varrho _z^+(J). \end{aligned}$$

(9)

There exists a rhombus inscribed in *J*having a diagonal collinear with *z*if either of the following conditions holds: (a) the points *c*, *n*, *a*, *f*are distinct; or (b) the point *n*lies on the line through *f*and *z*.

### Proof

Assume no rhombus inscribed in *J*has a diagonal collinear with *z*; we shall show that neither (a) nor (b) may hold. Obtain \(\bar{n}\), \(\widehat{D}\), and \(\widehat{E}\) from Theorem [4.4][55] and choose a point \(s \in {{\,\textrm{mid}\,}}[\widehat{D}] \cap {{\,\textrm{mid}\,}}[\widehat{E}] \subseteq {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\). Because *s*is not the center of a rhombus having a diagonal collinear with *z*, we have \((s,s) \in D \cup E\). By Lemma [3.1][56] (e), \(s \in U^* \subseteq \{\bar{c},\bar{a}\} \cap (N \cup F)\) whereas Lemma [3.1][56] (a) implies that \(s = c = \bar{c}\) or \(s = a = \bar{a}\).

Suppose that \(s \in N\). Lemma [3.1][56] (a) tells us that \(N = \{n\}\), which implies that \(c = s = n\) or \(a = s = n\). In particular, assumption (a) cannot hold. On the other hand, assumption (b) would imply \(c = \bar{c} = {{\,\textrm{mid}\,}}(f,n) \not = n\) or \(a = \bar{a} = {{\,\textrm{mid}\,}}(f,n) \not = n\). This completes the proof if \(U^*\) meets *N*.

Now suppose instead that \(U^* \subseteq F\). The choice of \(\widehat{D}\) and \(\widehat{E}\) ensures that (*f*, *f*) is the only point of the form \((e,e) \in \widehat{E} \cap (F\times F)\). Hence \(s = f\), so either \(s = c = \bar{c}\) or \(s = a = \bar{a}\) and assumption (a) cannot hold. But assumption (b) would then imply \(\bar{c} = {{\,\textrm{mid}\,}}(f,n) \not = f\) or \(\bar{a} = {{\,\textrm{mid}\,}}(f,n) \not = f\), so (b) likewise cannot hold. \(\square \)

Although the assumptions in Proposition [4.7][57] are not comprehensive, they suffice for proving uncountability as we show next.

## 5 Uncountably many inscribed rhombi

This section is devoted to proving the following result.

### Theorem 5.1

Every Jordan curve admits uncountably many inscribed rhombi.

We begin with a partial step toward the general case.

### Proposition 5.2

Consider a Jordan curve *J*and a point *z*in the plane that lies outside the convex hull \({{\,\textrm{Conv}\,}}J\) of *J*. Select points \(c,n,a,f \in J\) satisfying ( [9][58]). If *n*is also the (unique) nearest point in \({{\,\textrm{Conv}\,}}J\) to *z*, then for every \(\tau \ge 0\) there is a rhombus inscribed in *J*having a diagonal collinear with \(z+\tau (z-n)\). Moreover, if either *a*or *c*lies on the line through *f*and *n*, then no such rhombus corresponds to two different values of \(\tau \ge 0\).

### Proof

Assume that *a*lies on the line through *f*and *n*. Given \(z_\tau := z+\tau (z-n)\), select points \(c_\tau \), \(n_\tau \), \(a_\tau \) and \(f_\tau \) in analogy with the points *c*, *n*, *a*and *f*selected relative to *z*. Clearly, we may choose \(a_\tau \equiv a\). The collinearity of *f*, *n*and *z*ensures that we may choose \(f_\tau \equiv f\), whereas the nearest-point hypothesis implies \(n_\tau \equiv n\) as well as the final statement of the corollary. Because \(c_\tau \) cannot lie on the line through \(f_\tau \) and \(n_\tau \), assumption (b) of Proposition [4.7][57] is met if we replace *z*with \(z_\tau \) and *c*with \(c_\tau \) in that context. \(\square \)

We now return to the general case. Choose diametric points *l*and *r*for *J*, in the sense that they maximize the distance between points in *J*. Note that *l*and *r*are extreme points of \({{\,\textrm{Conv}\,}}J\). Defining \(x := (r-l) / \Vert r-l\Vert \), we see that *l*and *r*are the unique minimizer and maximizer (respectively) of \(u \mapsto x \cdot u\) over *J*. Next choose a unit vector \(y\perp x\) so that \(y \cdot u > y \cdot r\) for some \(u \in J\). Select points \(t,b\in J\) that maximize and minimize (respectively) \(u \mapsto y \cdot u\), so that \(l \not = b\). The choice of letters ‘l’, ‘t’, ‘r’ and ‘b’ is intended to suggest points on the left, top, right and bottom sides of the rectangle *R*circumscribed about *J*with sides parallel to *x*and *y*. See Figure [6][59].

**Fig. 6**

[image: Fig. 6]

[Full size image][60]

A Jordan curve with diametric points, arcs of the circles centered at those points, and a circumscribed rectangle

We shall show that there is a rhombus inscribed in *J*having a diagonal collinear with the point \(z_\tau := \tau x + b + [x\cdot (r-b)]x\) for each sufficiently large \(\tau >0\), as illustrated in Figure [7][61].

**Fig. 7**

[image: Fig. 7]

[Full size image][62]

Inscribed rhombi having diagonals collinear with three vectors \(z_\tau \)

Because \(x\cdot (z_\tau -r) = \tau \), we see that \(z_\tau \) lies outside \({{\,\textrm{Conv}\,}}J\). Moreover, because \(z_\tau \) is collinear with the side of *R*containing *b*, no two values of \(\tau >0\) can yield the same rhombus. In this way, we obtain an uncountable family of rhombi.

Choose \(f_\tau , n_\tau \in J\) to maximize and minimize (respectively) the Euclidean distance between \(z_\tau \) and points in *J*. Also, select \(a_\tau \) and \(c_\tau \) from *J*giving the maximum of the angle \(|\theta _{z_\tau }(u)-\theta _{z_\tau }(v)|\) over \(u,v\in J\). If \(y\cdot b = y\cdot r\) then \(f_\tau \equiv l\) and \(n_\tau \equiv r\), in which case we may choose \(a_\tau \equiv r\) and apply Proposition [5.2][63] to obtain an uncountable family of rhombi. So we assume instead that \(y\cdot b < y\cdot r\) and choose \(a_\tau \equiv b\). To apply Proposition [4.7][57] (a), we must prove that the points \(a_\tau \), \(f_\tau \), \(c_\tau \) and \(n_\tau \) are distinct for sufficiently large \(\tau \). Clearly, \(a_\tau \not = c_\tau \) and \(f _\tau \not = n_\tau \) for all \(\tau >0\). So it remains to show that \(a_\tau , c_\tau \not \in \{f _\tau ,n_\tau \}\) for large \(\tau \). The following lemma therefore suffices to complete the proof of Theorem [5.1][64].

### Lemma 5.3

If \(y\cdot b < y\cdot r\) then

$$\begin{aligned} \varrho _{z_\tau }(n_\tau )< \varrho _{z_\tau }(a_\tau ) < \varrho _{z_\tau }(f_\tau ), \end{aligned}$$

(10)

$$\begin{aligned} \theta _{z_\tau }(c_\tau )< \theta _{z_\tau }(n_\tau ) < \theta _{z_\tau }(f_\tau ) \end{aligned}$$

(11)

for all sufficiently large \(\tau \).

### Proof

Observing that \(x = -{{\,\mathrm{\textbf{x}}\,}}(\theta _z(b))\) in the notation introduced in § [2][65], we may reformulate ( [11][66]) equivalently as

$$\begin{aligned} \xi _{z_\tau }(c_\tau )< \xi _{z_\tau }(n_\tau ) < \xi _{z_\tau }(f_\tau ), \end{aligned}$$

(12)

where \(\xi _z(u) := \cos (\theta _z(b)-\theta _z(u)) = {{\,\mathrm{\textbf{x}}\,}}(\theta _z(b)) \cdot {{\,\mathrm{\textbf{x}}\,}}((\theta _z(u)) = x\cdot (z-u) / \Vert z-u\Vert \). For each vector *u*we define scalars \(u_x := x\cdot u\) and \(u_y := y\cdot u\) allowing us to express \(u = u_xx + u_yy\) in terms of its orthogonal projections onto (the lines through) *x*and *y*. Observing that \(\Vert u\Vert ^2 = u_x^2 + u_y^2\) and \(v\cdot u = v_xu_x+v_yu_y\), we may write \(z_\tau = (\tau + r_x)x + b_yy\) to obtain

$$\begin{aligned} u-z_\tau = - (\tau +r_x-u_x)x + (u_y-b_y)y, \end{aligned}$$

(13)

$$\begin{aligned} \varrho _{z_\tau }^2(u) = \Vert u-z_\tau \Vert ^2 = (\tau +r_x-u_x)^2 + (u_y-b_y)^2, \end{aligned}$$

(14)

$$\begin{aligned} \varrho _{z_\tau }^2(u)-\varrho _{z_\tau }^2(u) = 2(v_x-u_x)\tau + \zeta (u,v), \end{aligned}$$

(15)

$$\begin{aligned} \xi _{z_\tau }(u) = \frac{\tau +r_x-u_x}{\sqrt{(\tau +r_x-u_x)^2 + (u_y-b_y)^2}}, \end{aligned}$$

(16)

where we define \(\zeta (u,v) := (u_x-v_x) (u_x+v_x-2r_x) + (u_y-v_y) (u_y+v_y-2b_y)\). Combining ( [15][67]) with

$$\begin{aligned} \varrho _{z_\tau }^2(a_\tau )-\varrho _{z_\tau }^2(n_\tau ) = \varrho _{z_\tau }^2(b)-\varrho _{z_\tau }^2(n_\tau ) \ge \varrho _{z_\tau }^2(b)-\varrho _{z_\tau }^2(r),\\ \varrho _{z_\tau }^2(f_\tau )-\varrho _{z_\tau }^2(a_\tau ) = \varrho _{z_\tau }^2(f_\tau )-\varrho _{z_\tau }^2(b) \ge \varrho _{z_\tau }^2(l)-\varrho _{z_\tau }^2(b) \end{aligned}$$

yields \(\varrho _{z_\tau }^2(n_\tau ) + 2\tau (r_x-b_x) + \zeta (b,r) \le \varrho _{z_\tau }^2(a_\tau ) \le \varrho _{z_\tau }^2(f_\tau ) - 2\tau (b_x-l_x) - \zeta (l,b)\). Together with \(l_x<b_x<r_x\), this implies ( [10][68]) for all sufficiently large \(\tau > 0\). Next, we use equation ( [16][69]) to obtain

$$ \xi _{z_\tau }(t) = \frac{\tau +r_x-t_x}{\sqrt{(\tau +r_x-t_x)^2+(t_y-b_y)^2}}, \qquad \xi _{z_\tau }(r) = \frac{\tau }{\sqrt{\tau ^2+(r_y-b_y)^2}}. $$

Hence \(\xi _{z_\tau }(t) < \xi _{z_\tau }(r)\) if and only if \(\tau > (r_x-t_x)(r_y-b_y)/(t_y-r_y)\). By \(\varrho _{z_\tau }(n_\tau ) \le \varrho _{z_\tau }(r)\) and \(x\cdot n_\tau \le x\cdot r \le x\cdot z_\tau \), we also have

$$\begin{aligned} \xi _{z_\tau }(r) = \frac{x\cdot (z_\tau -r)}{\Vert z_\tau -r\Vert } \le \frac{x\cdot (z_\tau -r)}{\Vert z_\tau -n_\tau \Vert } \le \frac{x\cdot (z_\tau -n_\tau )}{\Vert z_\tau -n_\tau \Vert } = \xi _{z_\tau }(n_\tau ) \end{aligned}$$

(17)

for \(\tau >0\). Thus, \(\xi _{z_\tau }(c_\tau ) \le \xi _{z_\tau }(t) < \xi _{z_\tau }(r) \le \xi _{z_\tau }(n_\tau )\), proving that the left inequality in ( [12][70]) holds for sufficiently large \(\tau \). Because \(\varrho _{z_\tau }(n_\tau ) < \varrho _{z_\tau }(f_\tau )\), the right inequality in ( [12][70]) holds by the same reasoning as ( [17][71]) if we can verify that \(x\cdot f_\tau \le x\cdot n_\tau \) for sufficiently large \(\tau \). In fact, \(x\cdot f_\tau \rightarrow l_x\) and \(x\cdot n_\tau \rightarrow r_x\) as \(\tau \rightarrow \infty \). To see this, note that ( [15][67]) implies

$$\begin{aligned} 0 \le \varrho _{z_\tau }^2(f_\tau )-\varrho _{z_\tau }^2(l) = 2(l_x-x\cdot f_\tau )\tau + \zeta (f_\tau ,l),\\ 0 \le \varrho _{z_\tau }^2(r)-\varrho _{z_\tau }^2(n_\tau ) = 2(x\cdot n_\tau -r_x)\tau + \zeta (r,n_\tau ). \end{aligned}$$

Thus, \(0\le x\cdot f_\tau - l_x \le \zeta (f_\tau ,l)/(2\tau )\) and \(0\le x\cdot f_\tau -r_x \le \zeta (r,n_\tau )/(2\tau )\). Because \(\zeta \) is bounded on *J*, these prove that \(x\cdot f_\tau \rightarrow l_x\) and \(x\cdot n_\tau \rightarrow r_x\) as \(\tau \rightarrow \infty \). This completes the proof of the lemma. \(\square \)

The argument above finds a half line of points corresponding to diagonals of distinct inscribed rhombi. The rest of the paper explores when there is a more substantial set of such points filling an entire region surrounding *J*. With that goal in mind, the next section proposes a regularity condition.

## 6 Local polygonality

Recall that Corollary [4.5][72] ensures existence of an inscribed rhombus having one diagonal collinear with \(z \not \in {{\,\textrm{Conv}\,}}J\) if we know that *J*misses \({{\,\textrm{Ann}\,}}_z^*J\). When *J*meets \({{\,\textrm{Ann}\,}}_z^*J\) instead, we seek assumptions to impose on *J*near points in \({{\,\textrm{Ann}\,}}_z^* J\). Roughly speaking, it suffices for *J*to have well-defined one-sided tangents at such points.

We shall limit our discussion here to the simplest such case: we say that *J*is *locally polygonal*at \(u \in J\) if there exist scalars \(\gamma >0\), \(\eta \ge 0\) and \(\omega \) such that the image of \([-\gamma ,\gamma ]\) under \(h(\tau ):= u + \tau {{\,\mathrm{\textbf{x}}\,}}(\omega ) + \eta |\tau | {{\,\mathrm{\textbf{y}}\,}}(\omega )\) lies in *J*. Clearly, *h*is continuous and bijective. Some facts about local polygonality are provided in Appendix A. Here is how we use this concept.

### Proposition 6.1

If *J*is locally polygonal at each \(u \in J \cap {{\,\textrm{Ann}\,}}_z^* J\), then *J*admits an inscribed rhombus having a diagonal collinear with *z*.

### Proof

Recall the notation of § [3][26]. We consider two cases, according to whether \(U^*\) is empty or nonempty. In the former case, Theorem [4.4][55] tells us there is a point \(s \in {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{mid}\,}}[E]\) which by Lemma [3.1][56] (e) satisfies \((s,s) \not \in D\cup E\). Hence, *s*corresponds to a rhombus rather than merely a point or line segment.

We now assume instead that \(U^*\) is nonempty. If \(U^*\cap (F \cap J)\) is nonempty then choose \(f \in U^*\cap (F \cap J)\); otherwise, choose \(f \in F \cap J\). By Theorem [4.4][55] there exists \(\bar{n} \in {{\,\textrm{mid}\,}}[E] \cap N\) along with continua \(\widetilde{D} \subseteq D\) and \(\widetilde{E} \subseteq E\) that are cyclically co-circumscribed at \((\bar{c}, \bar{a}; f, \bar{n})\) and satisfy \({{\,\textrm{mid}\,}}[\widetilde{D}] \cap {{\,\textrm{mid}\,}}[\widetilde{E}] \not = \emptyset \). We shall construct continua \(\widehat{D} \subseteq \widetilde{D}\) and \(\widehat{E} \subseteq \widetilde{E}\) that are cyclically co-circumscribed at a 4-tuple \((\hat{c},\hat{a};\hat{n},\hat{f})\) with the additional property that the nonempty set \({{\,\textrm{mid}\,}}[\widehat{D}] \cap {{\,\textrm{mid}\,}}[\widehat{E}]\) misses \(U^*\). We rely on the following fact, which is proved in the appendix:

-

Lemma [A.2][73]. If *J*is locally polygonal at \(u \in U^*\), then there exist \(\psi > 0\), an interval \(I \subseteq \varrho _z[J]\) containing \(\varrho _z(u)\), and continuous functions \(\bar{d} : I \rightarrow {{\,\textrm{mid}\,}}[D]\) and \(\bar{e}: I \rightarrow {{\,\textrm{mid}\,}}[E]\) satisfying \(\theta _z \circ \bar{d} = \theta _z \circ \bar{e}\),

$$ {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u|\psi ) \subseteq \bar{d}[I],\qquad {{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u|\psi ) \subseteq \bar{e}[I], $$

and \(|\varrho _z(\bar{d}(\varrho )) - \varrho _z(u)| > |\varrho _z(\bar{e}(\varrho )) - \varrho _z(u)|\) for all \(\varrho \in I \setminus \{\varrho _z(u)\}\).

For each \(u \in U^*\) let \((\psi _u,I_u, \bar{d}_u, \bar{e}_u)\) be the *u*-specific \((\psi , I, \bar{d}, \bar{d})\) guaranteed by the fact above and define \(\hat{\psi }: = \min \{\psi _u \mid u \in U^*\}\). Note that \(\theta _z(\bar{a}) \not = \theta _z(\bar{c})\) and \(\theta _z(\bar{n}) \not = \theta _z(f)\), where the latter is implied by \(U^* \not = \emptyset \). Thus \({{\,\textrm{Nbhd}\,}}_z(\bar{a}\,|\,\psi ) \cap {{\,\textrm{Nbhd}\,}}_z(\bar{c}\,|\,\psi ) = \emptyset = {{\,\textrm{Nbhd}\,}}_z(\bar{n}\,|\,\psi ) \cap {{\,\textrm{Nbhd}\,}}_z(f\,|\,\psi )\) for all sufficiently small \(\psi \in (0,\hat{\psi }]\). Fix such a value of \(\psi \) and use it to define nonempty closed sets

$$\begin{aligned} M(u \,|\, K) := {\left\{ \begin{array}{ll} \big \{(v,w) \in K \,\big |\, {{\,\textrm{mid}\,}}(v,w) \in {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\}, & u \in U^*,\\ \{(v,w) \in K \mid {{\,\textrm{mid}\,}}(v,w) = u\}, & u \not \in U^*, \end{array}\right. } \end{aligned}$$

for \(K = \widetilde{D}\) or \(\widetilde{E}\). Then

$$\begin{aligned} M(\bar{a} \,|\, \widetilde{D}) \cap M(\bar{c} \,|\, \widetilde{D}) = \emptyset = M(\bar{n} \,|\, \widetilde{E}) \cap M(f \,|\, \widetilde{E}). \end{aligned}$$

(18)

Now we apply Lemma [4.3][53] to obtain a sub-continuum \(\widehat{D}\) of \(\widetilde{D}\) meeting both \(M(\bar{a} \,|\, \widetilde{D})\) and \(M(\bar{c} \,|\, \widetilde{D})\) but missing \({{\,\textrm{Int}\,}}M(\bar{a} \,|\, \widetilde{D})\) and \({{\,\textrm{Int}\,}}M(\bar{c} \,|\, \widetilde{D})\). Likewise, there is a sub-continuum \(\widehat{E}\) of \(\widetilde{E}\) meeting \(M(\bar{n} \,|\, \widetilde{E})\) and \(M(f \,|\, \widetilde{E})\) but not their interiors. Select points \(\hat{c},\hat{n},\hat{a},\hat{f}\) so that

$$\begin{aligned} \hat{c} \in {{\,\textrm{mid}\,}}[M(\bar{c} \,|\, \widetilde{D}) \cap \widehat{D}], \qquad \hat{n} \in {{\,\textrm{mid}\,}}[M(\bar{n} \,|\, \widetilde{E}) \cap \widehat{E}],\\ \hat{a} \in {{\,\textrm{mid}\,}}[M(\bar{a} \,|\, \widetilde{D}) \cap \widehat{D}], \qquad \hat{f} \in {{\,\textrm{mid}\,}}[M(f \,|\, \widetilde{E}) \cap \widehat{E}]. \end{aligned}$$

Let \(\partial J_0:= {{\,\textrm{Conv}\,}}({{\,\textrm{mid}\,}}[\widehat{D}] \cup {{\,\textrm{mid}\,}}[\widehat{E}])\). Clearly, \(\theta _z(\hat{c}) = \theta _z^-(J_0)\) and \(\theta _z(\hat{a}) = \theta _z^+(J_0)\).

By \(\theta _z \circ \bar{d}_u = \theta _z \circ \bar{e}_u\) in Lemma [A.2][73], equation ( [18][74]), and the definitions of \(M(\cdot |\cdot )\) and \({{\,\textrm{Nbhd}\,}}_z(\cdot |\cdot )\), we see that \(\theta _z(\hat{a}) \not = \theta _z(\hat{c})\) and \(\theta _z(\hat{n}) \not = \theta _z(\hat{f})\). Hence \(\hat{a} \not = \hat{c}\) and \(\hat{n} \not = \hat{f}\). Without loss of generality, we may assume \(\theta _z(\bar{n}) > \theta _z(f)\) and consider these three cases separately:

-

If \(f \not \in U^*\) then \(\bar{n} = \bar{a} \in U^*\) and \(f \not = \bar{c}\). By construction we have \((\hat{f},\hat{c}) = (f,\bar{c})\) with \(\theta _z(\hat{c}) \le \theta _z(\hat{f}) < \theta _z(\hat{n}) = \theta _z(\hat{a})\) and \(\varrho _z(\hat{c}) < \varrho _z(\hat{f})\). For \(u = \bar{n} = \bar{a}\), Lemma [A.2][73] yields \(\varrho \in I_u\) with \(\varrho _z(\hat{n}) = \varrho _z(\bar{e}_u(\varrho )) < \varrho _z(\bar{d}_u(\varrho )) = \varrho _z(\hat{a})\).

-

If \(\bar{n} \not \in U^*\) then \(f = \bar{c} \in U^*\) and \(\bar{n} \not = \bar{a}\). By construction we have \((\hat{n},\hat{a}) = (\bar{n}, \bar{a})\) with \(\theta _z(\hat{c}) = \theta _z(\hat{f}) < \theta _z(\hat{n}) \le \theta _z(\hat{a})\) and \(\varrho _z(\hat{n}) < \varrho _z(\hat{a})\). For \(u = f = \bar{c}\), Lemma [A.2][73] yields \(\varrho \in I_u\) with \(\varrho _z(\hat{f}) = \varrho _z(\bar{e}_u(\varrho )) > \varrho _z(\bar{d}_u(\varrho )) = \varrho _z(\hat{c})\).

-

If \(U^* = \{f,\bar{n}\}\) then \(\bar{n} = \bar{a}\) and \(f = \bar{c}\). By construction we have \((\hat{f},\hat{c},\hat{n},\hat{a}) = (f,\bar{c},\bar{n}, \bar{a})\) with \(\theta _z(\hat{c}) = \theta _z(\hat{f}) < \theta _z(\hat{n}) = \theta _z(\hat{a})\). For \(u_1 = \bar{n} = \bar{a}\) and \(u_2 = f = \bar{c}\), Lemma [A.2][73] yields \(\varrho _i \in I_{u_i}\) with \(\varrho _z(\hat{n}) = \varrho _z(\bar{e}_{u_1}(\varrho _1)) < \varrho _z(\bar{d}_{u_1}(\varrho _1)) = \varrho _z(\hat{a})\) and \(\varrho _z(\hat{f}) = \varrho _z(\bar{e}_{u_2}((\varrho _2)) > \varrho _z(\bar{d}_{u_2}((\varrho _2)) = \varrho _z(\hat{c})\).

Each case has \(\theta _z(\hat{c}) \le \theta _z(\hat{f}) < \theta _z(\hat{n}) \le \theta _z(\hat{a})\), \(\varrho _z(\hat{n}) \le \varrho _z(\hat{a})\), and \(\varrho _z(\hat{c} ) \le \varrho _z(\hat{f})\). So \(\hat{c},\hat{n},\hat{a},\hat{f}\) appear in that cyclic order on the boundary of \(J_0\).

Finally, notice that each ordered pair (*u*, *u*) with \(u \in U^*\) lies in \({{\,\textrm{Int}\,}}M(u \,|\, \widetilde{D}) \cap {{\,\textrm{Int}\,}}M(u \,|\, \widetilde{E})\). Hence, no such ordered pair lies in \(\widehat{D} \cup \widehat{E}\). Because *u*is an extreme point of \({{\,\textrm{Ann}\,}}_z(J)\), we have \(u \not \in {{\,\textrm{mid}\,}}[\widehat{D}] \cup {{\,\textrm{mid}\,}}[\widehat{E}]\). Lemma [4.1][54] ensures that \({{\,\textrm{mid}\,}}[\widehat{D}] \cap {{\,\textrm{mid}\,}}[\widehat{E}]\) is nonempty, whereas Lemma [3.1][56] (e) tells us each member of that intersection corresponds to an inscribed rhombus having a diagonal collinear with *z*. \(\square \)

Notice that the proof of Proposition [6.1][75] does not directly use the hypothesis of local polygonality, but instead uses the conclusion of Lemma [A.2][73] cited from the appendix. It is perhaps possible to ensure that lemma’s conclusion by hypotheses much weaker than local polygonality.

Proposition [6.1][75] leads to natural geometric assumptions which may be imposed on *J*independent of the choice of *z*.

### Corollary 6.2

If a Jordan curve in the plane is locally polygonal at all extreme points of its convex hull, then for every point outside the convex hull there is a rhombus inscribed in the curve having a diagonal collinear with that point.

### Proof

All elements of \(J \cap {{\,\textrm{Ann}\,}}_z^*J\) are extreme points of \({{\,\textrm{Conv}\,}}J\), so this result follows from Proposition [6.1][75]. \(\square \)

### Corollary 6.3

For every point outside the convex hull of a polygonal Jordan curve, there is a rhombus inscribed in the curve having a diagonal collinear with that point.

### Proof

This follows from Corollary [6.2][76]. \(\square \)

In the next section, we tighten up the argument so that *J*need only be well behaved at a very small number of points.

## 7 Diagonals collinear with all points in a region

We now present properties of a curve ensuring that every point outside some compact set is collinear with the diagonal of an inscribed rhombus. Ideally, such properties might be phrased simply and intuitively in terms of *J*or \({{\,\textrm{Conv}\,}}J\). Here is the main result in this section.

### Theorem 7.1

Let *Z*be the set of points collinear with at least one inscribed rhombus of a given Jordan curve *J*. The complement of *Z*is bounded if *J*is locally polygonal at each \(u \in \partial {{\,\textrm{Conv}\,}}J\) with \({{\,\textrm{sweep}\,}}(u\,|\,J) \le \pi /2\).

The hypothesis concerning \({{\,\textrm{sweep}\,}}(\cdot )\) amounts to a condition on only those extreme points of \({{\,\textrm{Conv}\,}}J\) with non-obtuse interior angles. Clearly, *J*may have at most four such exceptional points. Theorem [7.1][77] therefore significantly strengthens Corollary [6.2][76]. The rest of the section is devoted to proving the theorem above. We begin with some observations about points on the annulus about *J*.

### Lemma 7.2

Consider a Jordan curve *J*, a point \(z \not \in {{\,\textrm{Conv}\,}}J\), and points \(c,n,a,f \in J\) satisfying

$$\begin{aligned} \theta _z(c) = \theta _z^-(J), \quad \theta _z(a) = \theta _z^+(J), \quad \varrho _z(n) = \varrho _z^-(J), \quad \varrho _z(f) = \varrho _z^+(J). \end{aligned}$$

(19)

If *p*is the unique nearest point in \({{\,\textrm{Conv}\,}}J\) to *z*, then:

1. (a)

\(|\theta _z(p) - \theta _z(u)| < \pi /2\) for all \(u \in {{\,\textrm{Conv}\,}}J\);

2. (b)

\({{\,\textrm{sweep}\,}}(u\,|\,J) \le \pi /2\) for each \(u \in \{a,c\} \cap \{f,p\}\);

3. (c)

if \(n \in \{a,c\}\) then \({{\,\textrm{sweep}\,}}(n\,| \, J) \le \pi /2 + |\theta _z(p) - \theta _z(n)| < \pi \), \((n-p)\perp (z-p)\), and *n*is an extreme point of \({{\,\textrm{Face}\,}}(p\,| {{\,\textrm{Conv}\,}}J)\).

In particular, all members of \(\{a,c\} \cap \{f,n,p\}\) are extreme points of \({{\,\textrm{Conv}\,}}J\).

### Proof

First, we note that the final statement of the lemma follows from conclusions (b) and (c): if \(u \in {{\,\textrm{Conv}\,}}J\) is not an extreme point then *u*lies in the relative interior of a line segment in \({{\,\textrm{Conv}\,}}J\) and therefore \({{\,\textrm{sweep}\,}}(u\,|\, J) = \pi \).

Next, we observe that every \(u \in {{\,\textrm{Conv}\,}}J\) satisfies these linear inequalities:

$$\begin{aligned} {{\,\mathrm{\textbf{y}}\,}}(\theta _z(a)) \cdot u&\le {{\,\mathrm{\textbf{y}}\,}}(\theta _z(a)) \cdot a,&{{\,\mathrm{\textbf{y}}\,}}(\theta _z(c)) \cdot u&\ge {{\,\mathrm{\textbf{y}}\,}}(\theta _z(c)) \cdot c, \end{aligned}$$

(20)

$$\begin{aligned} {{\,\mathrm{\textbf{x}}\,}}(\theta _z(f)) \cdot u&\le {{\,\mathrm{\textbf{x}}\,}}(\theta _z(f)) \cdot f,&{{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot u&\ge {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot p. \end{aligned}$$

(21)

Specifically, the coefficient vectors \({{\,\mathrm{\textbf{y}}\,}}(\theta _z(a))\) and \(-{{\,\mathrm{\textbf{y}}\,}}(\theta _z(c))\) for inequalities ( [20][78]) are the unique outward-pointing normal unit vectors to the lines containing the two flat sides of the annular section \({{\,\textrm{Ann}\,}}_z J\) circumscribed around *J*by the points *a*, *f*, *c*, *n*. Similarly, the coefficient vector \({{\,\mathrm{\textbf{x}}\,}}(\theta _z(f))\) in ( [21][79]) is the unique outward-pointing normal unit vector to the circle about *z*through *f*. Also, the coefficient vector \(-{{\,\mathrm{\textbf{x}}\,}}(\theta _z(p))\) in ( [21][79]) is the unit vector pointing from *p*in the direction of *z*. We see by the latter that conclusion (a) of the lemma holds because

$$ 0 \le {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot (u-p) = \varrho _z(u) \cos (\theta _z(u)-\theta _z(p)) - \varrho _z(p) $$

implies \(\cos (\theta _z(u)-\theta _z(p)) \ge \varrho _z(p)/\varrho _z(u) > 0\).

Defining \({{\,\textrm{NCone}\,}}(u) := \{ v \mid \forall \hat{u}\in {{\,\textrm{Conv}\,}}J:\, v\cdot (\hat{u}-u)\le 0 \}\) for \(u \in \partial {{\,\textrm{Conv}\,}}J\), we see that the inequalities ( [20][78])–( [21][79]) are equivalent to

$$\begin{aligned} {{\,\mathrm{\textbf{y}}\,}}(\theta _z(a)) \in {{\,\textrm{NCone}\,}}(a),\quad -{{\,\mathrm{\textbf{y}}\,}}(\theta _z(c)) \in {{\,\textrm{NCone}\,}}(c), \end{aligned}$$

(22)

$$\begin{aligned} {{\,\mathrm{\textbf{x}}\,}}(\theta _z(f)) \in {{\,\textrm{NCone}\,}}(f),\quad -{{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \in {{\,\textrm{NCone}\,}}(p). \end{aligned}$$

(23)

Moreover, \({{\,\textrm{sweep}\,}}(0\,|{{\,\textrm{NCone}\,}}(u)) + {{\,\textrm{sweep}\,}}(u\,|\, J) = \pi \) for any \(u \in \partial {{\,\textrm{Conv}\,}}J\). Thus, conclusions (b)–(c) of the lemma can be reformulated equivalently in terms of exterior angles:

1. (b)

\({{\,\textrm{sweep}\,}}(0\,|{{\,\textrm{NCone}\,}}(u)) \ge \pi /2\) for each \(u \in \{a,c\} \cap \{f,p\}\);

2. (c)

if \(n \in \{a,c\}\) then \({{\,\textrm{sweep}\,}}(0\,|{{\,\textrm{NCone}\,}}(n)) \ge \pi /2 - |\theta _z(p) - \theta _z(n)|\), \((n-p)\perp (z-p)\), and *n*is an extreme point of \({{\,\textrm{Face}\,}}(p\,| {{\,\textrm{Conv}\,}}J)\).

In particular, conclusion (b) follows from ( [22][80])–( [23][81]) because \({{\,\mathrm{\textbf{x}}\,}}(\theta ) \perp {{\,\mathrm{\textbf{y}}\,}}(\theta )\).

We now turn to conclusion (c) in which \(n \in \{a,c\}\). Suppose \({{\,\textrm{Conv}\,}}\{p_0,p_1\!\} = {{\,\textrm{Face}\,}}(p\,| {{\,\textrm{Conv}\,}}J)\). We may assume that \(\theta _z(p_0) \le \theta _z(p_1)\) and \(p = (1-\lambda )p_0 + \lambda p_1\) for some \(\lambda \in (0,1)\). By convexity, \((1-\sigma )p_0 + \sigma p_1 \in {{\,\textrm{Conv}\,}}J\) for all \(\sigma \in [0,1]\) and so the second inequality in ( [21][79]) leads to

$$ 0 \le {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot \big ([(1-\sigma )p_0 + \sigma p_1]-p\big ) = (\sigma -\lambda )[{{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot (p_1-p_0)]. $$

The choices \(\sigma \in \{0,1\}\) yield \(0 = {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot (p_0-p_1)\), implying that

$$\begin{aligned} {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot p_1 = {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot p = {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot p_0. \end{aligned}$$

(24)

Next, by ( [21][79]) we have

$$\begin{aligned} 0 \le {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p))\cdot (n-p)&= {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p))\cdot (n-p_i) \\&= \varrho _z(n)\cos (\theta _z(p)-\theta _z(n)) - \varrho _z(p_i)\cos (\theta _z(p)-\theta _z(p_i)). \end{aligned}$$

Rewriting this as

$$ \cos (\theta _z(p)-\theta _z(n)) \ge \frac{\varrho _z(p_i)}{\varrho _z(n)}\cos (\theta _z(p)-\theta _z(p_i)) \ge \cos (\theta _z(p)-\theta _z(p_i)) $$

leads to \(|\theta _z(p)-\theta _z(n)| \le |\theta _z(p)-\theta _z(p_i)|\). Combining this with the observation that \(\theta _z(p_0) \le \theta _z(p) \le \theta _z(p_1)\), we obtain \(\theta _z(p_0) \le \theta _z(n) \le \theta _z(p_1)\). By \(n \in \{a,c\}\), this implies that either \(\theta _z(p_0) = \theta _z(c) = \theta _z(n)\) or \(\theta _z(p_1) = \theta _z(a) = \theta _z(n)\). Hence, for a specific choice of \(j \in \{0,1\}\), we have \(\theta _z(p_j) = \theta _z(n)\) and therefore \(n = z + \beta (p_j - z)\) for some \(\beta \in (0,1]\). Now ( [21][79]) and ( [24][82]) tell us that

$$\begin{aligned} 0&\le {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p))\cdot [z + \beta (p_j - z) -p] \\&= {{\,\mathrm{\textbf{x}}\,}}(\theta _z(p))\cdot [(1-\beta )(z-p) + \beta (p_j - p)] = (1-\beta )\varrho _z(p), \end{aligned}$$

and so \(\beta \ge 1\). Hence \(\beta =1\), so \(n=p_j\) as claimed in conclusion (c). Also, ( [24][82]) yields \((n-p)\perp (z-p)\), as desired. To finish the proof, suppose that \(n = c\); the case of \(n=a\) is similar. Observe that \(-{{\,\mathrm{\textbf{y}}\,}}(\theta _z(n)) \in {{\,\textrm{NCone}\,}}(n)\) by \(n = c\) and ( [22][80]). At the same time, \(-{{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \in {{\,\textrm{NCone}\,}}(n)\) by \((n-p)\perp (z-p)\) and ( [23][81]). Hence the calculation \({{\,\mathrm{\textbf{x}}\,}}(\theta _z(p)) \cdot {{\,\mathrm{\textbf{y}}\,}}(\theta _z(n)) = \sin (\theta _z(p)-\theta _z(n)) = \cos (\pi /2-\theta _z(p)+\theta _z(n))\) yields \({{\,\textrm{sweep}\,}}(0\,|{{\,\textrm{NCone}\,}}(n)) \ge \pi /2 - \theta _z(p) + \theta _z(n) = \pi /2 - |\theta _z(p) - \theta _z(n)|\) because \(n=c\) implies \(|\theta _z(p) - \theta _z(n)| = \theta _z(p) - \theta _z(n)\). This completes the proof of the reformulated conclusion (c). \(\square \)

On its own, Lemma [7.2][83] paves the way for existence criteria stated in terms of overall properties of a Jordan curve. Here are some intuitively appealing examples.

### Corollary 7.3

Consider a Jordan curve *J*in the plane and suppose one of the following conditions holds:

1. (a)

\(J = g[\mathbb {R}]\) for some differentiable \(g : \mathbb {R} \rightarrow \mathbb {R}^2\) with \(g'\not =0\) everywhere;

2. (b)

each point of \(\partial {{\,\textrm{Conv}\,}}J\) has a unique supporting line;

3. (c)

\(J = \partial {{\,\textrm{Conv}\,}}J\) and \(\pi /2 < {{\,\textrm{sweep}\,}}(u\,|\, J)\) for all \(u \in J\).

Then for each \(z \not \in {{\,\textrm{Conv}\,}}J\) there is a rhombus inscribed in *J*having a diagonal collinear with *z*.

### Proof

Let *c*, *n*, *a*, *f*, *p*be as in Lemma [7.2][83]. We shall show that \(\{a,c\}\cap \{f,n\} = \emptyset \) in all three cases, so that we may apply Proposition [4.7][57] (a) to obtain existence. First, assumption (a) of the corollary implies assumption (b) because the extreme points of \({{\,\textrm{Conv}\,}}J\) lie on *J*. Next, assumption (b) is equivalent to saying that \({{\,\textrm{sweep}\,}}(u\,| \, J) = \pi \) for all \(u \in {{\,\textrm{Conv}\,}}J\). Lemma [7.2][83] (b) then implies that \(f \not \in \{a,c\}\), while conclusions (a) and (c) of that lemma combine to show that \(n \not \in \{a,c\}\). Finally, for assumption (c) we see that Lemma [7.2][83] (b) and \(p = n\) imply \(\{a,c\}\cap \{f,n\} = \emptyset \). \(\square \)

We now turn our focus to points in \(\partial \!{{\,\textrm{Conv}\,}}J\) with acute or right interior angles. As noted earlier, there are at most four such points.

### Proposition 7.4

Consider a Jordan curve *J*that is locally polygonal at each \(u \in \partial {{\,\textrm{Conv}\,}}J\) for which \({{\,\textrm{sweep}\,}}(u\,|\,J) \le \pi /2\). Suppose \(z \not \in {{\,\textrm{Conv}\,}}J\), let *p*be the nearest point in \({{\,\textrm{Conv}\,}}J\) to *z*, and let *n*be a nearest point in *J*to *z*. Then *J*admits an inscribed rhombus having a diagonal collinear with *z*if at least one of the following holds:

1. (a)

*J*is locally polygonal at *n*;

2. (b)

*n*is not an extreme point of \({{\,\textrm{Conv}\,}}J\);

3. (c)

*n*is not the *unique*nearest point in *J*to *z*;

4. (d)

\(n = p\) (equivalently, \(p \in J\));

5. (e)

\(n \not \in {{\,\textrm{Face}\,}}(p\,|{{\,\textrm{Conv}\,}}J)\);

6. (f)

\({{\,\textrm{sweep}\,}}(n\,|\,J) > \pi /2 + |\theta _z(p) - \theta _z(n)|\); or

7. (g)

\({{\,\textrm{sweep}\,}}(n\,|\,J) > \pi /2 + \arctan (\Vert n-p\Vert /\Vert z-p\Vert )\).

### Proof

Assume *J*is locally polygonal at every \(u \in \partial {{\,\textrm{Conv}\,}}J\) with \({{\,\textrm{sweep}\,}}(u\,|\,J) \le \pi /2\), and that no rhombus inscribed in *J*has a diagonal collinear with *z*. We shall show that assumptions (a)–(g) of the proposition cannot hold. Let the points \(\bar{c},\bar{a}\) and sets \(N, F, U^*\) be as in § [3][26]; also, choose points \(c,a \in J\) satisfying ( [19][84]). In view of Proposition [6.1][75], there is a point \(u \in U^*\) at which *J*is not locally polygonal and hence \({{\,\textrm{sweep}\,}}(u\,|\, J) > \pi /2\). By Lemma [7.2][83] (b), \(u \not \in (F \cap J) \cup \{p\}\) and so \(u = \bar{n} \in [\{\bar{a}, \bar{c}\} \cap N] \setminus \{p\}\); also *u*is an extreme point of \({{\,\textrm{Conv}\,}}J\). By Lemma [3.1][56] (a,b), we see that \(p \not = \bar{n} = n \in \{a,c\}\) for the unique choice of \(n \in J\) satisfying ( [19][84]). Thus, assumptions (a)–(d) of the proposition cannot hold. Next, Lemma [7.2][83] (c) implies that assumptions (e) and (f) do not hold. Finally, the orthogonality of \(z-p\) and \(n-p\) in Lemma [7.2][83] (c) implies that the angle \(\angle nzp = \theta _z(n) - \theta _z(p)\) about *z*satisfies \(\tan |\theta _z(p) - \theta _z(n)| = \Vert n-p\Vert / \Vert z-p\Vert \). Hence, assumptions (f) and (g) of the proposition are equivalent in the current context. \(\square \)

We end by using the foregoing results to prove Theorem [7.1][77].

### Proof (Proof of Theorem 7.1)

Define \(\lambda \) to be the length of the longest line segment in \(\partial {{\,\textrm{Conv}\,}}J\), or zero if \(\partial {{\,\textrm{Conv}\,}}J\) contains no line segments. Let \(\phi > \pi /2\) be the infimum of \({{\,\textrm{sweep}\,}}(\cdot \,|\,J)\) over \(\{ u \in \partial {{\,\textrm{Conv}\,}}J \mid {{\,\textrm{sweep}\,}}(u\,|\,J) > \pi /2 \}\). We claim that *Z*contains every \(z \in \mathbb {R}^2\) satisfying

$$\begin{aligned} \Vert z-u\Vert > -\lambda \tan \phi \end{aligned}$$

(25)

for all \(u\in {{\,\textrm{Conv}\,}}J\). This would imply that the complement of *Z*lies entirely within distance \(-\lambda \tan \phi \) of \({{\,\textrm{Conv}\,}}J\).

Consider a point \(z \not \in {{\,\textrm{Conv}\,}}J\). Let *p*and *n*be as in Proposition [7.4][85]. We prove that one of the assumptions (a), (d), (e) or (g) of Proposition [7.4][85] must hold. If assumption (a) fails, then \({{\,\textrm{sweep}\,}}(n\,|\,J) > \pi /2\) and thus \({{\,\textrm{sweep}\,}}(n\,|\,J) \ge \phi \). This implies \(0 > \tan ({{\,\textrm{sweep}\,}}(n\,|\,J)) \ge \tan \phi \). If (d) and (e) also fail, then \(n \in {{\,\textrm{Face}\,}}(p\,|{{\,\textrm{Conv}\,}}J) \setminus \{p\} \subseteq \partial {{\,\textrm{Conv}\,}}J\) and so \(0< \Vert n-p\Vert < \lambda \). Combining these with ( [25][86]) at \(u=p\), we obtain \(\Vert z-p\Vert \ge \lambda (-\tan \phi ) > \Vert n-p\Vert [-\tan ({{\,\textrm{sweep}\,}}(n\,|\,J))]\). Rearranging this as

$$\begin{aligned} \tan ({{\,\textrm{sweep}\,}}(n\,|\,J))&> -\Vert z-p\Vert /\Vert n-p\Vert = -\cot (\arctan (\Vert n-p\Vert /\Vert z-p\Vert )) \\&= \tan (\pi /2 + \arctan (\Vert n-p\Vert /\Vert z-p\Vert )), \end{aligned}$$

we observe that the inequality between the left and right sides is equivalent to assumption (g) of Proposition [7.4][85]. \(\square \)

## Data availability

No datasets were generated or analysed during the current study.

## References

1.

Emch, A.: Some properties of closed convex curves in a plane. Am. J. Math. **35**(4), 401–412 (1913)

[Article][87] [MathSciNet][88] [Google Scholar][89]

2.

Emch, A.: On some properties of the medians of closed continuous curves formed by analytic arcs. Am. J. Math. 38(1), (1916). (6–18)

3.

Fung, A.T.H.: Every Jordan curve inscribes uncountably many rhombi, Geom. Dedicata 215, 421–441 (2021)

4.

Matschke, B.: A survey on the square peg problem. Notices Amer. Math. Soc. **61**, 346–352 (2014)

[Article][90] [MathSciNet][91] [Google Scholar][92]

5.

Matschke, B.: On the square peg problem and its relatives. Trans. Amer. Math. Soc 375(9), (2022). (6255–6280)

6.

Nielsen, M.J.: Rhombi inscribed in simple closed curves. Geom. Dedicata. **54**, 245–254 (1995)

[Article][93] [MathSciNet][94] [Google Scholar][95]

7.

Nielsen, M.J., Wright, S.E.: Rectangles inscribed in symmetric continua. Geom. Dedicata. **56**, 287–297 (1995)

[Article][96] [MathSciNet][97] [Google Scholar][98]

8.

Sikorski, R., Zarankiewicz, K.: On uniformization of functions (I). Fund. Math. **41**, 339–344 (1954)

[Article][99] [MathSciNet][100] [Google Scholar][101]

9.

Stromquist, W.: Inscribed squares and square-lie quadrilaterals in closed curves. Mathematika **36**, 187–197 (1989)

[Article][102] [MathSciNet][103] [Google Scholar][104]

10.

Toeplitz, O.: Ueber einige Aufgaben der Analysis situs. Verhandlungen der Schweizerischen Naturforschenden Gesellschaft **4**, 197 (1911)

[Google Scholar][105]

11.

Wright, S.E.: Every Jordan curve contains all vertices of uncountably many rhombi—a short proof, American Mathematical Monthly (to appear)

[Download references][106]

## Author information

### Authors and Affiliations

1.

Department of Statistics, Miami University, Oxford, OH, 45056, USA

Stephen E. Wright

Authors

1. Stephen E. Wright

[View author publications][107]

Search author on: [PubMed][108] [Google Scholar][109]

### Contributions

The paper is entirely the work of the sole author S.W.

### Corresponding author

Correspondence to [Stephen E. Wright][110].

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## A. Appendix

### A. Appendix

We now provide details about local polygonality (as defined in § [6][29]) needed in the proof of Proposition [6.1][75]. We work in the framework of § [3][26]. Assume throughout this appendix that *J*is a given Jordan curve in the plane, *z*is a specific point outside \({{\,\textrm{Conv}\,}}J\), and \(u \in U^*\) is a point at which *J*is locally polygonal. By the latter, there exist scalars \(\gamma >0\), \(\eta \ge 0\) and \(\omega \) such that the image of \([-\gamma ,\gamma ]\) under \(h(\tau ) := u + \tau {{\,\mathrm{\textbf{x}}\,}}(\omega ) + \eta |\tau | {{\,\mathrm{\textbf{y}}\,}}(\omega )\) lies in *J*. Clearly, *h*is continuous and bijective. We begin by writing *h*in a form suited to the polar-coordinate representation of the main article.

### Lemma A.1

If we write \(h(\tau ) = u + \alpha (\tau ) {{\,\mathrm{\textbf{x}}\,}}(\theta _z(u)) + \beta (\tau ) {{\,\mathrm{\textbf{y}}\,}}(\theta _z(u))\) using

$$\begin{aligned} \alpha (\tau )&:= \tau \cos (\theta _z(u)-\omega ) + \eta |\tau | \sin (\theta _z(u)-\omega ) = {{\,\mathrm{\textbf{x}}\,}}(\theta _z(u))\cdot [h(\tau )-u], \\ \beta (\tau )&:= -\tau \sin (\theta _z(u)-\omega ) + \eta |\tau | \cos (\theta _z(u)-\omega ) = {{\,\mathrm{\textbf{y}}\,}}(\theta _z(u))\cdot [h(\tau )-u], \end{aligned}$$

then the following hold:

1. (a)

\(\alpha (\tau ) = |\tau | \alpha ({{\,\textrm{sgn}\,}}(\tau ))\) and \(\beta (\tau ) = |\tau | \beta ({{\,\textrm{sgn}\,}}(\tau ))\) for all \(\tau \);

2. (b)

\(\alpha '(\tau ) = {{\,\textrm{sgn}\,}}(\tau ) \alpha ({{\,\textrm{sgn}\,}}(\tau ))\) and \(\beta '(\tau ) = {{\,\textrm{sgn}\,}}(\tau ) \beta ({{\,\textrm{sgn}\,}}(\tau ))\) for all nonzero \(\tau \);

3. (c)

the functions \(\varrho _z\circ h\) and \(\theta _z\circ h\) satisfy

$$\begin{aligned} \varrho _z^2(h(\tau ))&= [\varrho _z(u) + \alpha (\tau )]^2 + \beta ^2(\tau ) \end{aligned}$$

(26)

$$\begin{aligned}&= \tau ^2(1 + \eta ^2) + 2\varrho _z(u) \alpha (\tau ) + \varrho _z^2(u), \end{aligned}$$

(27)

$$\begin{aligned} \theta _z(h(\tau ))&= \arctan (\beta (\tau )/[\varrho _z(u)+\alpha (\tau )]) + \theta _z(u); \end{aligned}$$

(28)

4. (d)

\(\sin (\theta _z(u)-\omega )\) and \(\cos (\theta _z(u)-\omega )\) are nonzero;

5. (e)

\(\sin (\theta _z(u)-\omega ) > 0\) if and only if \(\varrho _z(u) = \varrho _z^-(J)\), which holds if and only if \(\alpha (\tau ) \ge 0\) for all \(\tau \);

6. (f)

\(\cos (\theta _z(u)-\omega ) > 0\) if and only if \(\theta _z(u) = \theta _z^-(J)\), which holds if and only if \(\beta (\tau ) > 0\) for all \(\tau \);

7. (g)

\(|\!\tan (\theta _z(u)-\omega )| < \eta \), \(|\!\cot (\theta _z(u)-\omega )| \le \eta \), and \(\eta > 1\);

8. (h)

\(|\!\cot (\theta _z(u)-\omega )| = \eta \) if and only if \(\alpha (\tau ) = 0\) for some nonzero \(\tau \), in which case \(\varrho _z(u) = \varrho _z^-(J)\) and \(\alpha (-\tau ) > 0\);

9. (i)

the functions \(\alpha \) and \(\beta \) do not change sign.

### Proof

Statements (a)–(b) follow immediately from the definitions of \(\alpha \) and \(\beta \). To verify ( [26][111])–( [27][112]) we simply observe that \(\alpha ^2(\tau ) + \beta ^2(\tau ) = \tau ^2(1 + \eta ^2)\) and

$$\begin{aligned} \varrho _z^2(h(\tau ))&= \Vert h(\tau )-z\Vert ^2 = \Vert [h(\tau )-u]+(u-z)\Vert ^2 \\&= \Vert [\varrho _z(u)+\alpha (\tau )]{{\,\mathrm{\textbf{x}}\,}}(\theta _z(u)) + \beta (\tau ){{\,\mathrm{\textbf{y}}\,}}(\theta _z(u))\Vert ^2 \\&= [\varrho _z(u)+\alpha (\tau )]^2 + \beta ^2(\tau ). \end{aligned}$$

To confirm ( [28][113]) we first expand \(0 = {{\,\mathrm{\textbf{y}}\,}}(\theta _z(h(\tau ))) \cdot {{\,\mathrm{\textbf{x}}\,}}(\theta _z(h(\tau )))\) to obtain

$$\begin{aligned} 0&= {{\,\mathrm{\textbf{y}}\,}}(\theta _z(h(\tau ))) \cdot {{\,\mathrm{\textbf{x}}\,}}(\theta _z(h(\tau ))) \varrho _z(h(\tau )) \\&= {{\,\mathrm{\textbf{y}}\,}}(\theta _z(h(\tau ))) \cdot [h(\tau )-z] = {{\,\mathrm{\textbf{y}}\,}}(\theta _z(h(\tau ))) \cdot [(h(\tau )-u])-(z-u)] \\&= {{\,\mathrm{\textbf{y}}\,}}(\theta _z(h(\tau ))) \cdot [\tau {{\,\mathrm{\textbf{x}}\,}}(\omega ) + \eta |\tau | {{\,\mathrm{\textbf{y}}\,}}(\omega ) + \varrho _z(u){{\,\mathrm{\textbf{x}}\,}}(\theta _z(u))] \\&= \tau \sin (\omega -\theta _z(h(\tau ))) + \eta |\tau | \cos (\omega -\theta _z(h(\tau ))) + \varrho _z(u) \sin (\theta _z(u)-\theta _z(h(\tau ))). \end{aligned}$$

Writing \(\omega -\theta _z(h(\tau )) = [\omega -\theta _z(u)] + [\theta _z(u)-\theta _z(h(\tau ))]\) and using the identities

$$\begin{aligned} \sin (\omega -\phi _1) = \sin (\omega -\phi _2)\cos (\phi _2-\phi _1) + \cos (\omega -\phi _2)\sin (\phi _2-\phi _1),\\ \cos (\omega -\phi _1) = \cos (\omega -\phi _2)\cos (\phi _2-\phi _1) - \sin (\omega -\phi _2)\sin (\phi _2-\phi _1) \end{aligned}$$

with \(\phi _1 = \theta _z(h(\tau ))\) and \(\phi _2 = \theta _z(u)\) yields

$$ 0= \beta (\tau )\cos (\theta _z(u)-\theta _z(h(\tau ))) + [\alpha (\tau ) + \varrho _z(u)]\sin (\theta _z(u)-\theta _z(h(\tau ))). $$

This now leads to ( [28][113]), proving statement (c) of the lemma.

The proofs of statements (d)–(i) are intertwined. We use the notation \(\zeta _{\sigma _1}^{\sigma _2} = \zeta (\sigma _2) - \zeta (\sigma _1)\) when \(\zeta \) is a given function on some interval. By \(u \in U^*\), the functions \([\varrho _z\circ h]|_0^\tau = \) and \([\theta \circ h]|_0^\tau \) do not change sign and are zero only at \(\tau = 0\). For \(\tau \not = 0\), we write \(|\beta (\tau )| > 0\) as \({{\,\textrm{sgn}\,}}(\beta (\gamma )) \beta (\tau ) >0\). Substituting the definition of \(\beta (\tau )\) into this and dividing by \(|\tau |\) gives

$$ {{\,\textrm{sgn}\,}}(\beta (\gamma )) \left[ \pm \sin (\theta _z(u)-\omega )+ \eta \cos (\theta _z(u)-\omega ) \right] > 0, $$

which is the same as \({{\,\textrm{sgn}\,}}(\beta (\gamma )) \,\eta \, \cos (\theta _z(u)-\omega ) > \mp \sin (\theta _z(u)-\omega )\). Hence \(\eta > |\tan (\theta _z(u)-\omega )|\) and \({{\,\textrm{sgn}\,}}(\beta (\tau )) = {{\,\textrm{sgn}\,}}(\cos (\theta _z(u)-\omega ))\). These confirm statement (f), the claim in statement (d) about \(\cos (\theta _z(u)-\omega )\), and the tangent inequality in statement (g). For \(\tau \not = 0\), we write \(\big |[\varrho ^2\circ h]|_0^\tau \big | > 0\) as

$$ {{\,\textrm{sgn}\,}}([\varrho ^2\circ h]|_0^\gamma ) \{\tau ^2+\eta ^2\tau ^2 + 2\varrho _z(u) [\tau \cos (\theta _z(u)-\omega ) + \eta |\tau | \sin (\theta _z(u)-\omega )] \} >0. $$

Divide by \(2\varrho _z(u)|\tau |\) and take the limit as \(\tau \rightarrow 0^\pm \) to get

$$ {{\,\textrm{sgn}\,}}([\varrho ^2\circ h]|_0^\gamma ) [\pm \cos (\theta _z(u)-\omega ) + \eta \sin (\theta _z(u)-\omega )] \ge 0 $$

or, equivalently,

$$ {{\,\textrm{sgn}\,}}([\varrho ^2\circ h]|_0^\gamma )\sin (\theta _z(u)-\omega )\eta \ge \mp {{\,\textrm{sgn}\,}}([\varrho ^2\circ h]|_0^\gamma )\cos (\theta _z(u)-\omega ). $$

This implies that \(\sin (\theta _z(u)-\omega ) \not = 0\), \({{\,\textrm{sgn}\,}}([\varrho ^2\circ h]|_0^\gamma ) = {{\,\textrm{sgn}\,}}(\sin (\theta _z(u)-\omega ))\) and \(\eta \ge |\cot (\theta _z(u)-\omega )|\). These confirm statement (e), the claim in statement (d) that \(\sin (\theta _z(u)-\omega )\) is nonzero, and the cotangent inequality in statement (g). We see that \(\eta >1\) because the tangent and cotangent are reciprocals. Statement (h) now follows from ( [27][112]), whereas statement (i) follows from (e)–(f). \(\square \)

Here is the key property used in the proof of Proposition [6.1][75].

### Lemma A.2

If *J*is locally polygonal at \(u \in U^*\), then there exist \(\psi > 0\), an interval \(I \subseteq \varrho _z[J]\) containing \(\varrho _z(u)\), and continuous functions \(\bar{d} : I \rightarrow {{\,\textrm{mid}\,}}[D]\) and \(\bar{e}: I \rightarrow {{\,\textrm{mid}\,}}[E]\) satisfying \(\theta _z \circ \bar{d} = \theta _z \circ \bar{e}\),

$$ {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u|\psi ) \subseteq \bar{d}[I],\qquad {{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u|\psi ) \subseteq \bar{e}[I], $$

and \(|\varrho _z(\bar{d}(\varrho )) - \varrho _z(u)| > |\varrho _z(\bar{e}(\varrho )) - \varrho _z(u)|\) for all \(\varrho \in I \setminus \{\varrho _z(u)\}\).

### Proof

We begin by showing that there exist \(\gamma _1,\gamma _2 \in (0,\gamma )\) for which the restrictions \(\varrho _z \circ h|_{\Gamma _i}\) and \(\theta _z \circ h|_{\Gamma _i}\) to the intervals \(\Gamma _1 := [-\gamma _1,0]\) and \(\Gamma _2 := [0,\gamma _2]\) are injective. From Lemma [A.1][114] (a,b,c) we obtain

$$\begin{aligned} {[}\varrho _z^2 \circ h]'(\tau ) = 2\tau (1+\eta ^2) + 2\varrho _z(u){{\,\textrm{sgn}\,}}(\tau ) \alpha ({{\,\textrm{sgn}\,}}(\tau )), \end{aligned}$$

(29)

$$\begin{aligned} [\theta _z\circ h]'(\tau ) = \frac{\varrho _z(u){{\,\textrm{sgn}\,}}(\tau ) \beta ({{\,\textrm{sgn}\,}}(\tau ))}{[\varrho _z(u)+\alpha (\tau )]^2 + \beta ^2(\tau )} \end{aligned}$$

(30)

for \(\tau \not =0\), along with the one-sided derivatives

$$\begin{aligned} [\varrho _z \circ h]'_\pm (0) = [\alpha ]_\pm '(0) = \alpha (\pm 1), \qquad [\theta _z \circ h]'_\pm (0) = \frac{[\beta ]_\pm '(0)}{\varrho _z(u)} = \frac{\beta (\pm 1)}{\varrho _z(u)}. \end{aligned}$$

(31)

By ( [29][115]), \([\varrho _z^2 \circ h]'(\tau )\) does not change sign on \((-\gamma _1,0)\) or on \((0,\gamma _2)\) if the \(\gamma _i>0\) are sufficiently small. Specifically, we may take \(\gamma _i = \gamma \) if \(\alpha ((-1)^i)\ge 0\) and we may take \(\gamma _i\) to be the lesser of \(\gamma \) and \(-2\varrho _z(u)\alpha ((-1)^i) / [2(1+\eta ^2)]\) if \(\alpha ((-1)^i)<0\). By ( [30][116]), \([\theta _z\circ h]'(\tau )\) never changes sign on \((-\infty ,0)\) nor on \((0,\infty )\). Hence, \(\varrho _z\circ h\) and \(\theta _z\circ h\) are strictly monotone on each of the intervals \(\Gamma _1\) and \(\Gamma _2\), proving the claimed injectivity.

We define injective functions \(e_i := h \circ [\varrho _z \circ h|_{\Gamma _i}]^{-1}\) and \(d_i := h \circ [\theta _z \circ h|_{\Gamma _i}]^{-1}\). Clearly, \(\theta _z(d_i(\theta )) = \theta \) for all \(\theta \in (\theta _z \circ h)[\Gamma _i]\) and \(\varrho _z(e_i(\varrho )) = \varrho \) for all \(\varrho \in (\varrho _z \circ h)[\Gamma _i]\). Next, we define \(\bar{e}(\varrho ):= {{\,\textrm{mid}\,}}(e_1(\varrho ), e_2(\varrho ))\) and let \(I_1 \subseteq \varrho _z[J]\) be a subinterval containing \(\varrho _z(u)\) for which \((\theta _z \circ \bar{e})[I_1] \subseteq (\theta _z \circ h)[\Gamma _1] \cap (\theta _z \circ h)[\Gamma _2]\). Then \(\hat{d}_i := d_i \circ \theta _z \circ \bar{e}\) and \(\bar{d}(\varrho ) := {{\,\textrm{mid}\,}}(\hat{d}_1(\varrho ), \hat{d}_2(\varrho ))\) are defined on \(I_1\) and satisfy \(\theta _z \circ \bar{d} = \theta _z \circ \hat{d}_i = \theta _z \circ \bar{e}\) on \(I_1\).

We shall show that \(\bar{d}\) and \(\bar{e}\) parametrize \({{\,\textrm{mid}\,}}[D]\) and \({{\,\textrm{mid}\,}}[E]\) as curves near *u*in the following sense:

-

Claim 1. There exist \(\psi >0\) and an interval \(I_2 \subseteq \varrho _z[J]\) containing \(\varrho _z(u)\) such that \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) \subseteq \bar{d}[I_2]\) and \({{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) \subseteq \bar{e}[I_2]\).

Without loss of generality, we may assume that \(\theta _z(u) = \theta _z^+\). Take \(H_\textrm{a} = H_\textrm{f} = e_1[I_1]\) with \(H_\textrm{c} = H_\textrm{n} = e_2[I_1]\) in Lemma [4.6][117]. The images of the injective functions \(d_i\) and \(e_i\) each give arcs within \(e_i[I_1] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\) containing *u*. Consequently, the image of \(\hat{d}_i\) is also an arc within \(e_i[I_1]\). If \(v \in {{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) \subseteq {{\,\textrm{mid}\,}}\!\big [ D \cap (e_2[I_1]\times e_1[I_1]) \big ]\) then \(v = {{\,\textrm{mid}\,}}(d_1(\theta ), d_2(\theta ))\) for the unique choice \(\theta = \theta _z(v)\). Hence, \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\) is the image of some interval \(I_D\) under \(\theta \mapsto {{\,\textrm{mid}\,}}(d_1(\theta ), d_2(\theta ))\), and so \({{\,\textrm{mid}\,}}[D] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\) is an arc that also lies in the image of \(\bar{d}\). Similarly, if \(v \in {{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi ) \subseteq {{\,\textrm{mid}\,}}\!\big [ E \cap (e_2[I_1]\times e_1[I_1]) \big ]\) then \(v = {{\,\textrm{mid}\,}}(e_1(\varrho ), e_2(\varrho ))\) for some \(\varrho \). Hence, \({{\,\textrm{mid}\,}}[E] \cap {{\,\textrm{Nbhd}\,}}_z(u\,|\,\psi )\) lies in the image of some interval \(I_E\) under \(\bar{e}\). Take \(I_2 = I_D \cap I_E\). This completes the verification of Claim 1.

To finish the proof, we show there exists an interval \(I_3 \subseteq \varrho _z[J]\) containing \(\varrho _z(u)\) such that \(\theta _z(\bar{d}(\varrho )) = \theta _z(\bar{e}(\varrho ))\) and \(|\varrho _z(\bar{d}(\varrho ))-\varrho _z(u)| > |\varrho _z(\bar{e}(\varrho )) - \varrho _z(u)|\) for all \(\varrho \in I_3 \setminus \{\varrho _z(u)\}\). Then we may take \(I = I_1 \cap I_2 \cap I_3\). We begin by observing that the values \(\varrho \in I_1\) and \(\delta _i,\epsilon _i>0\) satisfy

$$\begin{aligned} \delta _i = \left| [\theta _z \circ h|_{\Gamma _i}]^{-1} (\theta _z(\bar{e}(\varrho )))\right| , \qquad \epsilon _i = \left| [\varrho _z \circ h|_{\Gamma _i}]^{-1}(\varrho )\right| \end{aligned}$$

(32)

if and only if \(h((-1)^i\delta _i) = \hat{d}_i(\varrho )\) and \(h((-1)^i\epsilon _i) = e_i(\varrho )\). Moreover, the mappings \(\varrho \mapsto \epsilon _i\) in ( [32][118]) are injective. In addition, notice that the inequality in the statement of the lemma amounts to \(\varrho _z(\bar{d}(\varrho )) > \varrho _z(\bar{e}(\varrho ))\) if \(\varrho _z(u) = \varrho _z^-(J)\) and to \(\varrho _z(\bar{d}(\varrho )) < \varrho _z(\bar{e}(\varrho ))\) if \(\varrho _z(u) = \varrho _z^+(J)\). By ( [6][47]), it therefore suffices to prove the following:

-

Claim 2. For all sufficiently small \(\epsilon _i > 0\) with \(\varrho _z(h(-\epsilon _1)) = \varrho _z(h(\epsilon _2))\), there exist \(\delta _i, \lambda _i>0\) satisfying

$$\begin{aligned} h((-1)^i\delta _i) - z = \lambda _i \{[h(-\epsilon _1) - z] + [h(\epsilon _2) - z]\} \end{aligned}$$

(33)

and \(\lambda _1+\lambda _2 > 1\) if \(\varrho _z(u) = \varrho _z^-(J)\) and \(\lambda _1+\lambda _2 < 1\) if \(\varrho _z(u) = \varrho _z^+(J)\).

If Claim 2 holds for all \(\epsilon _1 \in (0,\epsilon _1^+]\) then we take \(I_3 = (\varrho _z \circ h)\big [[0,\epsilon _1^+]\big ]\). By Lemma [A.1][114], the final condition in Claim 2 is equivalent to \({{\,\textrm{sgn}\,}}(\lambda _1 + \lambda _2 - 1) = {{\,\textrm{sgn}\,}}(\alpha (-1)+\alpha (1))\).

Next we introduce \(\hat{\alpha }(\epsilon _1,\epsilon _2) := \alpha (-\epsilon _1) + \alpha (\epsilon _2)\) and \(\hat{\beta }(\epsilon _1,\epsilon _2) := \beta (-\epsilon _1) + \beta (\epsilon _2)\) along with \(\alpha _i := \alpha ((-1)^i)\) and \(\beta _i := \beta ((-1)^i)\). By Lemma [A.1][114] (a,d,e,f,i), \(\epsilon _i > 0\) implies \({{\,\textrm{sgn}\,}}(\hat{\alpha }(\epsilon _1,\epsilon _2)) = {{\,\textrm{sgn}\,}}(\max _i \alpha _i) \not =0\) and \({{\,\textrm{sgn}\,}}(\hat{\beta }(\epsilon _1,\epsilon _2)) = {{\,\textrm{sgn}\,}}(\beta _i) \not = 0\). Thus, the final condition in Claim 2 becomes \({{\,\textrm{sgn}\,}}(\lambda _1 + \lambda _2 - 1) = {{\,\textrm{sgn}\,}}(\hat{\alpha }(\epsilon _1,\epsilon _2))\). Taking \(\phi = \theta _z(u)-\omega \), we see that

$$ (\cos \phi +\eta \sin \phi )(\sin \phi +\eta \cos \phi ) -({-}\cos \phi +\eta \sin \phi )({-}\sin \phi +\eta \cos \phi ) = 2\eta . $$

In other words, \(\alpha _2\beta _1 - \alpha _1\beta _2 = 2\eta \). Rewriting ( [33][119]) using the form \(h(\tau ) - z = [\varrho _z(u) + \alpha (\tau )] {{\,\mathrm{\textbf{x}}\,}}(\theta _z(u)) + \beta (\tau ) {{\,\mathrm{\textbf{y}}\,}}(\theta _z(u))\) and then equating coefficients of \({{\,\mathrm{\textbf{x}}\,}}(\theta _z(u))\) (and likewise of \({{\,\mathrm{\textbf{y}}\,}}(\theta _z(u))\)) on both sides, we see that ( [33][119]) is equivalent to the system

$$\begin{aligned}&{{\,\mathrm{\textbf{x}}\,}}(\theta _z(u)):&\varrho _z(u) + \delta _i \alpha _i&= \lambda _i[2\varrho _z(u) + \hat{\alpha }(\epsilon _1,\epsilon _2)], \\&{{\,\mathrm{\textbf{y}}\,}}(\theta _z(u)):&\delta _i \beta _i&= \lambda _i\hat{\beta }(\epsilon _1,\epsilon _2). \end{aligned}$$

These are uniquely satisfied by \(\lambda _i = \varrho _z(u) / [2\varrho _z(u) + \hat{\alpha }(\epsilon _1,\epsilon _2) - \hat{\beta }(\epsilon _1,\epsilon _2) \alpha _i / \beta _i]\) and \(\delta _i = \lambda _i \hat{\beta }(\epsilon _1,\epsilon _2) / \beta _i\). Notice that \(\lambda _i\) and \(\delta _i\) depend continuously on \((\epsilon _1, \epsilon _2)\), and also that \(\lambda _i = 1/2\) when \(\epsilon _1 = \epsilon _2 = 0\). Therefore \(\lambda _i, \delta _i > 0\) for sufficiently small \((\epsilon _1, \epsilon _2)\). Observe that \(\lambda _1 + \lambda _2 - 1\) has the same sign as \(\zeta (\epsilon _1,\epsilon _2) := \varrho _z^2(u)(\lambda _1+ \lambda _2 - 1)/(\lambda _1\lambda _2)\), which can be rewritten as

$$\begin{aligned} \zeta (\epsilon _1,\epsilon _2)&= \varrho _z(u) [4\varrho _z(u) + 2\hat{\alpha }(\epsilon _1,\epsilon _2) - \hat{\beta }(\epsilon _1,\epsilon _2) (\alpha _1/\beta _1 + \alpha _2/\beta _2)]\\&\qquad - [2\varrho _z(u) + \hat{\alpha }(\epsilon _1,\epsilon _2) - \hat{\beta }(\epsilon _1,\epsilon _2)\alpha _1/\beta _1]\\&\qquad \qquad [2\varrho _z(u) + \hat{\alpha }(\epsilon _1,\epsilon _2) - \hat{\beta }(\epsilon _1,\epsilon _2)\alpha _2/\beta _2] \\&= \varrho _z(u) (\epsilon _1\beta _1-\epsilon _2\beta _2) (\alpha _2\beta _1-\alpha _1\beta _2) + \epsilon _1 \epsilon _2 (\alpha _2\beta _1-\alpha _1\beta _2)^2 \\&= 2\eta \varrho _z(u)(\epsilon _1 \beta _1 - \epsilon _2 \beta _2) + 4\eta ^2 \epsilon _1 \epsilon _2. \end{aligned}$$

We must verify that \({{\,\textrm{sgn}\,}}(\zeta (\epsilon _1,\epsilon _2)) = {{\,\textrm{sgn}\,}}(\hat{\alpha }(\epsilon _1,\epsilon _2))\) whenever the \(\epsilon _i > 0\) are sufficiently small and satisfy \(\varrho _z^2(h(-\epsilon _1)) = \varrho _z^2(h(\epsilon _2))\). We rearrange the latter via ( [26][111]) in two forms:

$$\begin{aligned} [\varrho _z(u) + \epsilon _1\alpha _1]^2 + (\epsilon _1\beta _1)^2 = [\varrho _z(u) + \epsilon _2\alpha _2]^2 + (\epsilon _2\beta _2)^2, \end{aligned}$$

(34)

$$\begin{aligned} (\epsilon _1\beta _1-\epsilon _2\beta _2) \hat{\beta }(\epsilon _1,\epsilon _2) = (\epsilon _2 \alpha _2 - \epsilon _1 \alpha _1) [2\varrho _z(u) + \hat{\alpha }(\epsilon _1,\epsilon _2)]. \end{aligned}$$

(35)

By ( [34][120]) we see that \(\epsilon _2 \ge 0\) can be expressed as a continuous function of \(\epsilon _1 \ge 0\). Lemma [A.1][114] (d,h,i) tells us there are three cases: \(\alpha _1 = 0 < \alpha _2\), \(\alpha _1 > 0 = \alpha _2\), and \(\alpha _1 \alpha _2 > 0\). Notice that in the first two cases, we have \(\hat{\alpha }(\epsilon _1,\epsilon _2) > 0\) when \(\epsilon _i > 0\) and it suffices to show that \(\epsilon _1 \beta _1 - \epsilon _2 \beta _2\). If \(\alpha _1 = 0 < \alpha _2\) then \(2\eta = \alpha _2\beta _1 - \alpha _1\beta _2 = \alpha _2\beta _1\), so \(\beta _i > 0\). Hence for \(\epsilon _i > 0\), ( [35][121]) becomes \(\epsilon _1 \beta _1 - \epsilon _2 \beta _2 = \epsilon _2 \alpha _2 [2\varrho _z(u) + \epsilon _2 \alpha _2] / \hat{\beta }(\epsilon _1,\epsilon _2) > 0\) as required. Similarly, if \(\alpha _1 > 0 = \alpha _2\) then \(\beta _i < 0\) and \(\epsilon _1 \beta _1 - \epsilon _2 \beta _2 = -\epsilon _1 \alpha _1 [2\varrho _z(u) + \epsilon _1 \alpha _1] / \hat{\beta }(\epsilon _1,\epsilon _2) > 0\). Finally, if \(\alpha _1 \alpha _2 > 0\) then we differentiate ( [34][120]) implicitly with respect to \(\epsilon _1\) to obtain

$$ \varrho _z(u) \alpha _1 + \epsilon _1(\alpha _1^2 + \beta _1^2) = \big [\varrho _z(u) \alpha _2 + \epsilon _2(\alpha _2^2 + \beta _2^2)\big ] \frac{\textrm{d}\epsilon _2}{\textrm{d}\epsilon _1}. $$

When \(\epsilon _i =0\) this yields \(\textrm{d}\epsilon _2 / \textrm{d}\epsilon _1 = \alpha _1/\alpha _2\) and thus

$$ \frac{\textrm{d}\zeta (\epsilon _1,\epsilon _2)}{\textrm{d}\epsilon _1}(0,0) = 2\eta \varrho _z(u)(\beta _1-\beta _2\alpha _1/\alpha _2) = 4\eta ^2\varrho _z(u)/\alpha _2. $$

For \(\epsilon _1 \approx 0^+\) this implies \({{\,\textrm{sgn}\,}}(\zeta (\epsilon _1, \epsilon _2)) = {{\,\textrm{sgn}\,}}(\alpha _2) = {{\,\textrm{sgn}\,}}(\hat{\alpha }(\epsilon _1,\epsilon _2))\). \(\square \)

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][122].

[Reprints and permissions][123]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [124]

### Cite this article

Wright, S.E. Inscribed rhombi having diagonals collinear with specified points. *Aequat. Math.***100**, 58 (2026). https://doi.org/10.1007/s00010-026-01307-4

[Download citation][125]

-

Received: 12 December 2025

-

Accepted: 24 May 2026

-

Published: 03 June 2026

-

Version of record: 03 June 2026

-

DOI: https://doi.org/10.1007/s00010-026-01307-4

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Mathematics Subject Classification

- [51M04 . 53A04 . 54D05][126]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s00010-026-01307-4.pdf
[3]: /article/10.1007/s00010-026-01307-4/save-research?_csrf=dCymTeT8VC0i-v_auLsTbZ56BiFf9zRl
[4]: /saved-research
[5]: /journal/10
[6]: /journal/10/aims-and-scope
[7]: https://submission.nature.com/new-submission/10/3
[8]: https://link.springer.com/10.1007/s11856-017-1581-0?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s00208-020-01987-6?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/978-3-319-72456-0_25?fromPaywallRec=false
[11]: /subjects/algebraic-geometry
[12]: /subjects/combinatorial-geometry
[13]: /subjects/differential-geometry
[14]: /subjects/geometry
[15]: /subjects/polytopes
[16]: /subjects/projective-geometry
[17]: /subjects/combinatorial-structures-and-intersection-theorems
[18]: /article/10.1007/s00010-026-01307-4#ref-CR10
[19]: /article/10.1007/s00010-026-01307-4#ref-CR4
[20]: /article/10.1007/s00010-026-01307-4#ref-CR5
[21]: /article/10.1007/s00010-026-01307-4#ref-CR1
[22]: /article/10.1007/s00010-026-01307-4#ref-CR2
[23]: /article/10.1007/s00010-026-01307-4#ref-CR9
[24]: /article/10.1007/s00010-026-01307-4#ref-CR6
[25]: /article/10.1007/s00010-026-01307-4#ref-CR3
[26]: /article/10.1007/s00010-026-01307-4#Sec3
[27]: /article/10.1007/s00010-026-01307-4#Sec4
[28]: /article/10.1007/s00010-026-01307-4#Sec5
[29]: /article/10.1007/s00010-026-01307-4#Sec6
[30]: /article/10.1007/s00010-026-01307-4#Sec7
[31]: /article/10.1007/s00010-026-01307-4#Equ3
[32]: /article/10.1007/s00010-026-01307-4#Equ4
[33]: /article/10.1007/s00010-026-01307-4#Fig1
[34]: /article/10.1007/s00010-026-01307-4/figures/1
[35]: /article/10.1007/s00010-026-01307-4#Fig2
[36]: /article/10.1007/s00010-026-01307-4/figures/2
[37]: /article/10.1007/s00010-026-01307-4/figures/3
[38]: /article/10.1007/s00010-026-01307-4#Fig3
[39]: /article/10.1007/s00010-026-01307-4/figures/4
[40]: /article/10.1007/s00010-026-01307-4#Fig4
[41]: /article/10.1007/s00010-026-01307-4#Fig5
[42]: /article/10.1007/s00010-026-01307-4/figures/5
[43]: /article/10.1007/s00010-026-01307-4#Equ1
[44]: /article/10.1007/s00010-026-01307-4#Equ2
[45]: /article/10.1007/s00010-026-01307-4#Equ7
[46]: /article/10.1007/s00010-026-01307-4#Equ8
[47]: /article/10.1007/s00010-026-01307-4#Equ6
[48]: /article/10.1007/s00010-026-01307-4#Equ5
[49]: /article/10.1007/s00010-026-01307-4#ref-CR11
[50]: /article/10.1007/s00010-026-01307-4#ref-CR7
[51]: /article/10.1007/s00010-026-01307-4#ref-CR8
[52]: /article/10.1007/s00010-026-01307-4#FPar4
[53]: /article/10.1007/s00010-026-01307-4#FPar5
[54]: /article/10.1007/s00010-026-01307-4#FPar3
[55]: /article/10.1007/s00010-026-01307-4#FPar6
[56]: /article/10.1007/s00010-026-01307-4#FPar1
[57]: /article/10.1007/s00010-026-01307-4#FPar12
[58]: /article/10.1007/s00010-026-01307-4#Equ9
[59]: /article/10.1007/s00010-026-01307-4#Fig6
[60]: /article/10.1007/s00010-026-01307-4/figures/6
[61]: /article/10.1007/s00010-026-01307-4#Fig7
[62]: /article/10.1007/s00010-026-01307-4/figures/7
[63]: /article/10.1007/s00010-026-01307-4#FPar15
[64]: /article/10.1007/s00010-026-01307-4#FPar14
[65]: /article/10.1007/s00010-026-01307-4#Sec2
[66]: /article/10.1007/s00010-026-01307-4#Equ11
[67]: /article/10.1007/s00010-026-01307-4#Equ15
[68]: /article/10.1007/s00010-026-01307-4#Equ10
[69]: /article/10.1007/s00010-026-01307-4#Equ16
[70]: /article/10.1007/s00010-026-01307-4#Equ12
[71]: /article/10.1007/s00010-026-01307-4#Equ17
[72]: /article/10.1007/s00010-026-01307-4#FPar8
[73]: /article/10.1007/s00010-026-01307-4#FPar35
[74]: /article/10.1007/s00010-026-01307-4#Equ18
[75]: /article/10.1007/s00010-026-01307-4#FPar19
[76]: /article/10.1007/s00010-026-01307-4#FPar21
[77]: /article/10.1007/s00010-026-01307-4#FPar25
[78]: /article/10.1007/s00010-026-01307-4#Equ20
[79]: /article/10.1007/s00010-026-01307-4#Equ21
[80]: /article/10.1007/s00010-026-01307-4#Equ22
[81]: /article/10.1007/s00010-026-01307-4#Equ23
[82]: /article/10.1007/s00010-026-01307-4#Equ24
[83]: /article/10.1007/s00010-026-01307-4#FPar26
[84]: /article/10.1007/s00010-026-01307-4#Equ19
[85]: /article/10.1007/s00010-026-01307-4#FPar30
[86]: /article/10.1007/s00010-026-01307-4#Equ25
[87]: https://doi.org/10.2307%2F2370404
[88]: http://www.ams.org/mathscinet-getitem?mr=1506193
[89]: http://scholar.google.com/scholar_lookup?amp;title=Some%20properties%20of%20closed%20convex%20curves%20in%20a%20plane&amp;journal=Am.%20J.%20Math.&amp;doi=10.2307%2F2370404&amp;volume=35&amp;issue=4&amp;pages=401-412&amp;publication_year=1913&amp;author=Emch%2CA
[90]: https://doi.org/10.1090%2Fnoti1100
[91]: http://www.ams.org/mathscinet-getitem?mr=3184501
[92]: http://scholar.google.com/scholar_lookup?amp;title=A%20survey%20on%20the%20square%20peg%20problem&amp;journal=Notices%20Amer.%20Math.%20Soc.&amp;doi=10.1090%2Fnoti1100&amp;volume=61&amp;pages=346-352&amp;publication_year=2014&amp;author=Matschke%2CB
[93]: https://link.springer.com/doi/10.1007/BF01265340
[94]: http://www.ams.org/mathscinet-getitem?mr=1326729
[95]: http://scholar.google.com/scholar_lookup?amp;title=Rhombi%20inscribed%20in%20simple%20closed%20curves&amp;journal=Geom.%20Dedicata.&amp;doi=10.1007%2FBF01265340&amp;volume=54&amp;pages=245-254&amp;publication_year=1995&amp;author=Nielsen%2CMJ
[96]: https://link.springer.com/doi/10.1007/BF01263570
[97]: http://www.ams.org/mathscinet-getitem?mr=1340790
[98]: http://scholar.google.com/scholar_lookup?amp;title=Rectangles%20inscribed%20in%20symmetric%20continua&amp;journal=Geom.%20Dedicata.&amp;doi=10.1007%2FBF01263570&amp;volume=56&amp;pages=287-297&amp;publication_year=1995&amp;author=Nielsen%2CMJ&amp;author=Wright%2CSE
[99]: https://doi.org/10.4064%2Ffm-41-2-339-344
[100]: http://www.ams.org/mathscinet-getitem?mr=72465
[101]: http://scholar.google.com/scholar_lookup?amp;title=On%20uniformization%20of%20functions%20%28I%29&amp;journal=Fund.%20Math.&amp;doi=10.4064%2Ffm-41-2-339-344&amp;volume=41&amp;pages=339-344&amp;publication_year=1954&amp;author=Sikorski%2CR&amp;author=Zarankiewicz%2CK
[102]: https://doi.org/10.1112%2FS0025579300013061
[103]: http://www.ams.org/mathscinet-getitem?mr=1045781
[104]: http://scholar.google.com/scholar_lookup?amp;title=Inscribed%20squares%20and%20square-lie%20quadrilaterals%20in%20closed%20curves&amp;journal=Mathematika&amp;doi=10.1112%2FS0025579300013061&amp;volume=36&amp;pages=187-197&amp;publication_year=1989&amp;author=Stromquist%2CW
[105]: http://scholar.google.com/scholar_lookup?amp;title=Ueber%20einige%20Aufgaben%20der%20Analysis%20situs&amp;journal=Verhandlungen%20der%20Schweizerischen%20Naturforschenden%20Gesellschaft&amp;volume=4&amp;publication_year=1911&amp;author=Toeplitz%2CO
[106]: https://citation-needed.springer.com/v2/references/10.1007/s00010-026-01307-4?format=refman&amp;flavour=references
[107]: /search?sortBy=newestFirst&amp;contributor=Stephen%20E.%20Wright
[108]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Stephen%20E.%20Wright
[109]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Stephen%20E.%20Wright%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[110]: mailto:wrightse@miamioh.edu
[111]: /article/10.1007/s00010-026-01307-4#Equ26
[112]: /article/10.1007/s00010-026-01307-4#Equ27
[113]: /article/10.1007/s00010-026-01307-4#Equ28
[114]: /article/10.1007/s00010-026-01307-4#FPar33
[115]: /article/10.1007/s00010-026-01307-4#Equ29
[116]: /article/10.1007/s00010-026-01307-4#Equ30
[117]: /article/10.1007/s00010-026-01307-4#FPar10
[118]: /article/10.1007/s00010-026-01307-4#Equ32
[119]: /article/10.1007/s00010-026-01307-4#Equ33
[120]: /article/10.1007/s00010-026-01307-4#Equ34
[121]: /article/10.1007/s00010-026-01307-4#Equ35
[122]: http://creativecommons.org/licenses/by/4.0/
[123]: https://s100.copyright.com/AppDispatchServlet?title=Inscribed%20rhombi%20having%20diagonals%20collinear%20with%20specified%20points&amp;author=Stephen%20E.%20Wright&amp;contentID=10.1007%2Fs00010-026-01307-4&amp;copyright=The%20Author%28s%29&amp;publication=0001-9054&amp;publicationDate=2026-06-03&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[124]: https://crossmark.crossref.org/dialog/?doi=10.1007/s00010-026-01307-4
[125]: https://citation-needed.springer.com/v2/references/10.1007/s00010-026-01307-4?format=refman&amp;flavour=citation
[126]: /search?query=51M04%20.%2053A04%20.%2054D05&amp;facet-discipline=#34;Mathematics&#34;
