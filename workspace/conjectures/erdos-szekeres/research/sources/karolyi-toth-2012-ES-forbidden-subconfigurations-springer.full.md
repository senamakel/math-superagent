<!-- source: https://link.springer.com/article/10.1007/s00454-012-9424-6 | converted from HTML -->

Erdős–Szekeres Theorem for Point Sets with Forbidden Subconfigurations | Discrete & Computational Geometry | Springer Nature Link

Skip to main content

# Erdős–Szekeres Theorem for Point Sets with Forbidden Subconfigurations

- Published: 31 March 2012

- Volume 48, pages 441–452 ( 2012)
- Cite this article

[Download PDF][1]

[Save article][2]

[View saved research][3]

[Discrete & Computational Geometry][4] [Aims and scope][5] [Submit manuscript][6]

Erdős–Szekeres Theorem for Point Sets with Forbidden Subconfigurations

[Download PDF][1]

## Abstract

According to the Erdős–Szekeres theorem, every set of *n*points in the plane contains roughly log*n*points in convex position. We investigate how this bound changes if our point set does not contain a subset that belongs to a fixed order type.

### Similar content being viewed by others

### [Erdős–Szekeres Theorems for Families of Convex Sets][7]

Chapter © 2018

### [On Erdős–Szekeres-Type Problems for k-convex Point Sets][8]

Chapter © 2019

### [Point Sets with Small Integer Coordinates and No Large Convex Polygons][9]

Article 13 September 2017

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Combinatorial Geometry][10]
- [Convex and Discrete Geometry][11]
- [Discrete Mathematics][12]
- [Geometry][13]
- [Polytopes][14]
- [Set Theory][15]
- [Combinatorial Structures and Intersection Theorems][16]

## 1 Introduction

According to the Erdős–Szekeres theorem [[9][17]] for any integer *n*≥3, there is an *N*such that any set of *N*points in general position contains *n*in convex position. Denote the smallest number with this property by *F*(*n*). The best known bounds for *F*(*n*) are

$$2^{n-2}+1\le F(n)\le{2n-5\choose n-2}+1.$$

The lower bound is due to Erdős and Szekeres [[10][18]] and conjectured to be sharp. The upper bound is proved by Tóth and Valtr in [[20][19]]. One can formulate this the other way around. For any integer *N*, let *f*(*N*) be the largest number with the property that any set of *N*points in general position contains *f*(*N*) points in convex position. Then we have *f*(*N*)=*Θ*(log*N*).

A very closely related classical result is Ramsey’s theorem. Its best known version, for graphs, is the following. Any graph of *N*vertices contains a complete or empty subgraph of *Ω*(log*N*) vertices. This bound is sharp up to a multiplicative factor. The Erdős–Szekeres theorem can be deduced easily from Ramsey’s theorem [[14][20]]. Many other connections between the Erdős–Szekeres theorem and Ramsey’s theorem can be found in [[17][21]]. Although the *c*log*N*bound cannot be improved in general, Erdős and Hajnal [[8][22]] proved that a much better lower bound is available if one considers only graphs without a certain induced subgraph. More precisely, they proved that for any graph *H*there is a constant *c**H*such that any graph *G*of *N*vertices which does not contain *H*as an induced subgraph, contains a complete or empty subgraph of \(e^{c_{H}\sqrt{\log N}}\) vertices; see Fox and Sudakov [[11][23]] for a refinement. According to the Erdős–Hajnal conjecture, for any *H*, the statement holds with \(N^{\varepsilon_{H}}\) as well, but it has been verified for very few graphs *H*[[2][24], [6][25], [8][22]].

Kalai, Solymosi, and some others suggested the investigation of analogous problems related to the Erdős–Szekeres theorem. The general question is that how does the bound *Θ*(log*N*) change if some fixed configuration is *forbidden*in the original point set. To pose the problem precisely, we have to define exactly what do we mean by a forbidden configuration.

Throughout this paper we consider only point sets in general position in the plane, that is, we always assume that no three points are collinear. The *order type*of a point set is the list of orientations of its triples. See [[12][26]] for a survey on order types and applications. Two point configurations are said to be of the same order type, if there is a bijection between them which preserves the orientations of the triples. Thus, order types are equivalence classes of configurations. By the *size*of an order type we mean the common cardinality of all configurations that belong to that class.

We say that a point set *T*contains order type \(\mathcal{S}\) if a subset of *T*belongs to order type \(\mathcal{S}\). We denote this as \(\mathcal{S}\hookrightarrow T\). We say that an order type \({\mathcal{T}}\) contains order type \(\mathcal{S}\), that is, \(\mathcal{S}\hookrightarrow\mathcal{T}\), if for any set *T*of order type \(\mathcal{T}\), \(\mathcal{S}\hookrightarrow T\).

Ramsey-type properties of order types have been studied by Nešetřil and Valtr in [[18][27]]. Order types play an important role in canonical versions of the Erdős–Szekeres theorem [[19][28]], the main tool is the ‘same type lemma’ of Bárány and Valtr [[5][29]], see also [[4][30], [17][21]] for a survey.

For a fixed non-convex order type \({\mathcal{T}}\) and any integer *n*, define \(F_{\mathcal{T}}(n)\) as the smallest integer *N*such that any order type of size at least *N*that does not contain \({\mathcal{T}}\), contains *n*points in convex position. Or the other way around, for any *N*, let \(f_{\mathcal{T}}(N)\) be the largest integer *n*such that any set of *N*points that does not contain \({\mathcal{T}}\), contains *n*points in convex position. Note that \(F_{\mathcal{T}}\) and \(f_{\mathcal{T}}\) are non-decreasing functions, which are not defined for convex order types \({\mathcal{T}}\). Károlyi and Solymosi [[15][31]] proved, somewhat surprisingly, that the analogue with graph Ramsey theory breaks down here. They proved that there exists an order type \({\mathcal{T}}\) with \(F_{\mathcal{T}}(n)>2^{n-2}\), hence \(f_{\mathcal{T}}(N)=\varTheta (\log N)\). Roughly speaking, the fact that \({\mathcal{T}}\) is a forbidden order type does not help too much, we do not necessarily find much more points in convex position in point sets without \({\mathcal{T}}\) than in the general case. However, the proof applied a general result of Nešetřil and Valtr [[18][27]] from which it is not easy to extract a concrete order type \({\mathcal{T}}\) with the above property. One novelty in the present paper is the exhibition of explicit order types \({\mathcal{T}}\) for which \(F_{\mathcal{T}}(n)\) is exponentially large (Theorem [1][32]). One such order type is given by the vertex set of a regular pentagon together with its center.

**Fig. 1**

[image: Fig. 1]

[Full size image][33]

Order types \(\mathcal{A}\) and \(\mathcal{P}\)

We say that order type \(\mathcal{T}\) has the Erdős–Hajnal property, if \(F_{\mathcal{T}}\) is bounded from above by a polynomial. It was also shown in [[15][31]] that some families of order types \({\mathcal{T}}\) do satisfy the analogue of the Erdős–Hajnal conjecture, that is, they have the Erdős–Hajnal property. In Sect. [3][34] we exhibit some more general families of order types with the Erdős–Hajnal property (Theorems 4 and 5).

In Theorem 8 in Sect. [4][35] we determine for each order type \({\mathcal{T}}\), whose convex hull is a triangle, whether

1. (i)

\(F_{\mathcal{T}}(n)\) is bounded by a linear function in *n*;

2. (ii)

\(F_{\mathcal{T}}(n)\) is at least quadratic in *n*but bounded by a polynomial in *n*;

3. (iii)

\(F_{\mathcal{T}}(n)\) is exponentially large in *n*.

Moreover, we prove that there are no other possibilities.

## 2 Constructions

There are three different non-convex order types \(\mathcal{T}\) of size less than six. It was shown in [[15][31]] that for any of them \(F_{\mathcal{T}}(n)\) is bounded from above by a polynomial function in *n*. The following result shows that it is not the case for some order types of six points.

Let point set *A*be the three vertices of a regular triangle, and three further points inside the triangle, close to the midpoints of the sides. Let \(\mathcal{A}\) be the order type of *A*. Let point set *P*be the five vertices of a regular pentagon, and its center, and let \(\mathcal{P}\) be the order type of *P*. See Fig. [1][32].

### Theorem 1

*For the order types*\(\mathcal{A}\)*and*\(\mathcal{P}\)*we have*\(F_{\mathcal{A}}(n)> 2^{n/2-1}\)*and*\(F_{\mathcal{P}}(n)> 2^{n/2-1}\).

First we define a point set *T**k*of cardinality 2*k*for each nonnegative integer *k*. The sequence *T**k*of point sets is defined recursively and will be referred to as the *twin construction*.

Point set *T*0 is just one point. Suppose we have already defined *T**k*−1. Take a line *ℓ*which is not parallel to any line determined by the points of *T**k*−1. Replace each point *p*∈*T**k*−1 by two points, *p*′,*p*″, both very close to *p*, such that the line *p*′*p*″ is parallel to *ℓ*. If all line segments *pp*′ and *pp*″ are short enough, then no line connecting two points of the configuration *T**k*thus obtained will properly intersect any line segment of the form *p*′*p*″. The points *p*′ and *p*″ are called the *twins*of each other and *p*is the *parent*of them. Note that we can choose the direction of *ℓ*in each recursive step almost freely and different choices lead to several twin constructions of different order types.

### Lemma 2

*For any**n*≥1, *T**n**does not contain*2*n*+1 *points in convex position*.

### Proof

The statement clearly holds for *n*=1. Suppose it holds for *n*−1 and let *p*1,*p*2,…,*p**m*∈*T**k*be *m*points in convex position. If *p**i*and *p**j*are twins of each other, then they are consecutive on the convex hull. Therefore, there can be at most two pairs of twins among *p*1,*p*2,…,*p**m*. Replacing each point by its parent in *T**n*−1, we find at least *m*−2 points of *T**n*−1 in convex position. By the induction hypothesis, *m*−2≤2*n*−2, consequently *m*≤2*n*. □

A point set *S*or order type \(\mathcal{S}\) is said to have the *separation property*if any two of its points can be separated by a line determined by some other two points of it.

### Lemma 3

*Suppose that the order type*\(\mathcal{S}\)*has the separation property*. *Then*\(F_{\mathcal{S}}(2n+1)> 2^{n}\).

### Proof

Since |*T**n*|=2*n*, in view of the previous lemma it is sufficient to show that *T**n*does not contain \(\mathcal{S}\). We prove it by induction on *n*. It is obviously true for *n*=1. Suppose that the statement holds for *n*−1. Assume that {*p*1,*p*2,…,*p**m*}⊆*T**n*has order type \(\mathcal{S}\). Consider any two points, *p**i*and *p**j*. Since they are separated by some line *p**u**p**v*, they cannot be twins in *T**n*, so their parents \(\bar{p}_{i}\) and \(\bar{p}_{j}\) are different. The set of parents \(\bar{p}_{1}, \bar{p}_{2}, \ldots, \bar{p}_{m}\) thus form an *m*-element subset in *T**n*−1 whose order type is again \(\mathcal{S}\), which contradicts the induction hypothesis. This concludes the proof. □

### Proof of Theorem 1

Now observe that both \(\mathcal{A}\) and \(\mathcal{P}\) has the separation property, therefore, Theorem 1 follows from the previous lemma. □

## 3 Order Types with the Erdős–Hajnal Property

First we introduce three families of order types we will frequently refer to from now on. See Fig. [2][36] for a representative element of each family.

**Fig. 2**

[image: Fig. 2]

[Full size image][37]

Order types \(\mathcal{E}_{3}\), \(\mathcal{F}_{4}\), and \(\mathcal{G}_{6;3,2}\)

For any *k*≥1, let *E*={*a*,*b*,*c*,*p*1,…,*p**k*} be a point set such that points *p*1,…,*p**k*lie inside the triangle *abc*and points *b*,*p*1,…,*p**k*,*c*are in convex position. This defines the order type \(\mathcal{E}_{k}\) of *E*. It is easy to see that \(F_{\mathcal{E}_{1}}(n)=n\). In general \(F_{\mathcal{E}_{k}}\) is bounded from above by a linear function, see [[15][31]].

For any *k*≥3, let *F*={*a*,*b*,*c*,*p*1,…,*p**k*} be a point set such that points *p*1,…,*p**k*lie inside the triangle *abc*, points *p*2,…,*p**k*−1 lie inside the convex quadrilateral *bp*1*p**k**c*, the points *p*1,…,*p**k*are in convex position, and no line defined by two of them intersects the segment *bc*. The order type of *F*is denoted by \(\mathcal{F}_{k}\).

Finally, let *k*≥4, *l*,*m*≥0. Two point sets, *X*and *Y*are said to be *mutually avoiding*if any line determined by two points of *X*(resp. *Y*) has all points of *Y*(resp. *X*) on the same side. Consider a configuration *G*={*p*1,…,*p**k*, *q*1,…,*q**l*, *r*1,…,*r**m*} with the following properties. The points *p*1,…,*p**k*are in convex position, the points *q*1,…,*q**l*,*r*1,…,*r**m*lie inside the convex polygon *p*1*p*2 …*p**k*, the points *p*1,*q*1,…,*q**l*,*p*2 are in convex position such that *Q*={*p*1,*q*1,…,*q**l*,*p*2 } and *G*∖*Q*are mutually avoiding, and similarly, *p*3,*r*1,…,*r**m*,*p*4 are in convex position such that *R*={*p*3,*r*1,…,*r**m*,*p*4 } and *G*∖*R*are mutually avoiding. The order type of *G*is denoted by \(\mathcal{G}_{k;l,m}\). Order type \(\mathcal{G}_{k;l,l}\) is simply denoted by \(\mathcal{G}_{k;l}\).

### Theorem 4

*Every order type*\(\mathcal{F}_{k}\)*with**k*≥3 *has the Erdős–Hajnal property*.

### Theorem 5

*Every order type*\(\mathcal{G}_{k;l,m}\), *where**k*≥4, *l*,*m*≥0 *and not both**l**and**m**are zero*, *has the Erdős–Hajnal property*.

The points (*x*1,*y*1),…,(*x**n*,*y**n*)∈ℝ 2 with *x*1 <⋯<*x**n*form an *n-cap*if

$${y_2-y_1\over x_2-x_1}>{y_3-y_2\over x_3-x_2}>\cdots>{y_n-y_{n-1}\over x_n-x_{n-1}}.$$

Similarly, they form an *n-cup*if

$${y_2-y_1\over x_2-x_1}<{y_3-y_2\over x_3-x_2}<\cdots<{y_n-y_{n-1}\over x_n-x_{n-1}}.$$

Both *n*-caps and *n*-cups are convex *n*-gons. They were used by Erdős and Szekeres in the original proof of the Erdős–Szekeres theorem.

### Lemma 6

[[9][17]] *Let**f*(*a*,*b*) *denote the smallest integer such that any set of**f*(*a*,*b*) *points in general position in the plane*, *no two on a vertical line*, *contains either an**a*-*cap or a**b*-*cup*. *Then*

$$f(a,b)={a+b-4\choose a-2}+1.$$

Note that for any fixed *a*, *f*(*a*,*b*) is a polynomial of *b*of degree *a*−2. Similarly, since \({a+b-4\choose a-2}={a+b-4\choose b-2}\), for any fixed *b*, *f*(*a*,*b*) is a polynomial of *a*of degree *b*−2.

### Proof of Theorem 4

We prove that for \(\mathcal{T}=\mathcal{F}_{k}\), the function \(F_{\mathcal{T}}\) is bounded from above by a polynomial of degree 3*k*−5. Let *X*be a set of \(n{n+k-4\choose k-2}^{3}\) points and assume that *X*does not contain *n*points in convex position. Then its convex hull contains at most *n*−1 vertices. Triangulate it, one of the triangles, say *abc*, contains more than \({n+k-4\choose k-2}^{3}\) points of *X*. Let *P*denote the set of these points. Define a partial order ≺*ab*on *P*as follows: For *p*,*q*∈*P*, let *p*≺*ab**q*if and only if the ray *pq*intersects side *bc*and the ray *qp*intersects side *ac*of the triangle. It is easy to check that the relation ≺*ab*is indeed a partial order. Partial orders ≺*ac*and ≺*bc*can be introduced in a similar way. Note that any two points of *P*are related by exactly one of these three relations. Thus, a repeated application of Dilworth’s theorem [[7][38]] gives that there is a subset *P*′ of *P*of size \(|P'|>{n+k-4\choose k-2}\), which is linearly ordered with respect to one of the three partial orders, say ≺*bc*. Translate and rotate the triangle so that vertex *a*is at the origin, and the negative *y*-axis is the angular bisector at *a*. Then for point set *P*′, the linear order ≺*bc*is identical to the linear order according to the *x*-coordinates of the points. By the assumption *P*′ does not contain an *n*-cap, therefore, by Lemma 6, it contains a *k*-cup. This, together with *a*, *b*, and *c*, is a point set of order type \(\mathcal{F}_{k}\). □

Given a family of sets *Y*1,*Y*2,…,*Y**m*, a *transversal*of this family is an *m*-element set {*y*1,*y*2,…,*y**m*} such that *y**i*∈*Y**i*for *i*=1,2,…,*m*. One key to the proof of Theorem 5 is the following ‘same type lemma’ due to Bárány and Valtr.

### Lemma 7

([[5][29]]) *For every integer**t*≥1 *there is a positive**c**t**with the following property*. *Assume that**X*1,*X*2,…,*X**t**are not necessarily disjoint planar point sets such that**X*1 ∪*X*2 ∪⋯∪*X**t**is in general position*. *Then there are subsets**Y**i*⊂*X**i**with*|*Y**i*|≥*c**t*|*X**i*|, *such that all transversals of**Y*1,*Y*2,…,*Y**t**belong to the same order type*.

### Proof of Theorem 5

Let *X*be a point set, |*X*|>*c*0*n**α*, which does not contain *n*points in convex position. We prove that if *c*0 =*c*0 (*k*,*l*) and *α*=*α*(*k*,*l*) are sufficiently large, then \({\mathcal{G}_{k;l}}\hookrightarrow X\). Then we also have \({\mathcal{G}_{k;l,m}}\hookrightarrow X\) and \({\mathcal{G}_{k;m,l}}\hookrightarrow X\) for any *m*≤*l*, which implies the theorem.

Assume that no two points of *X*lie on a vertical line. Choose a large enough integer *t*=*t*(*k*,*l*) whose value will be specified later. According to a result of Aronov et al. [[3][39]], every configuration of *N*points contains two mutually avoiding subsets of size at least \(\sqrt{N}/10\). By a repeated application of this result we can obtain pairwise mutually avoiding subsets *X*1,*X*2,…,*X**t*, such that |*X**i*|>*c*1*n**β*holds for every 1≤*i*≤*t*with *β*>*α*/2*t*. Using Lemma 7, we can find subsets \(X'_{i}\subset X_{i}\), \(|X'_{i}|>c_{2}n^{\beta}\) such that any transversal of \(X'_{1}, X'_{2}, \ldots, X'_{t}\) is of the same order type. In view of the Erdős–Szekeres theorem (Lemma 6), there is a sequence *i*1,*i*2,…,*i**s*such that *s*≥log 4*t*, and any transversal of \(X'_{i_{1}}, X'_{i_{2}}, \ldots, X'_{i_{s}}\) is in convex position. For simplicity, we denote \(X'_{i_{j}}\) by *Y**j*.

Consider now any ordered pair (*Y**i*,*Y**j*), 1≤*i*≠*j*≤*s*. Define a binary relation on the points of *Y**i*. For *p*,*q*∈*Y**i*, let *p*≺*q*if and only if *p*has smaller *x*-coordinate than *q*, and all points of *Y**j*lie *above*the line *pq*. It is not hard to see that ≺ is a partial ordering. According to Dilworth’s theorem, there is either a chain or an antichain of size \(\sqrt{|Y_{i}|}>c_{3}n^{\beta/2}\). Suppose that *C*⊂*Y**i*is such a chain (resp. antichain). Then all points of *Y**j*are *above*(resp. *below*) every line determined by *C*. Delete all points of *Y**i*which are not in that chain (resp. antichain).

Proceed analogously for each ordered pair (*Y**i*,*Y**j*). Note that during the process each set *Y**i*is reduced *s*−1 times. Denote the resulting sets by *Z**i*⊂*Y**i*, *i*=1,2,…,*s*. Now we have the family *Z*1,*Z*2,…,*Z**s*, such that any transversal of *Z*1,*Z*2,…,*Z**s*is in convex position, in this counterclockwise order, for any pair (*Z**i*,*Z**j*), *Z**j*is either above, or below *every*line determined by *Z**i*, and |*Z**i*|>*c*4*n**γ*holds for every 1≤*i*≤*s*with *γ*=*β*/2*s*−1 ≥*β*/2*t*−1.

Define now a four-colored complete graph on the vertex set {1,…,*s*} as follows. For any *i*<*j*, we know that *Z**j*is either above, or below every line determined by *Z**i*, and *Z**i*is either above, or below every line determined by *Z**j*. So we have four possibilities for the pair (*Z**i*,*Z**j*) that determines the color of the edge *ij*. Call the corresponding colors *aa*, *ab*, *ba*, and *bb*, respectively. By Ramsey’s theorem, there is a complete monochromatic subgraph of size *r*≥log 256*s*. Suppose without loss of generality that its vertices are 1,…,*r*.

Now we should distinguish four cases. Since reflection about the *x*-axis interchanges the “above” and “below” relations, it will be enough to consider two cases; see Fig. [3][40].

*Case 1:*:

All edges are colored with color *aa*.

*Case 2:*:

All edges are colored with color *ab*.

Now we assume that *t*is big enough so that *r*≥*k*−2. We choose the value of *c*0 and *α*so that

$$c_4n^\gamma>{n+l-2\choose l}.$$

*X*does not contain *n*points in convex position, therefore *Z*1 does not contain an *n*-cup. It follows from Lemma 6 that in either case *Z*1 contains an (*l*+2)-cap *C*1 ={*p*3,*r*1,…,*r**l*,*p*4 }. For *i*=2,…,*k*−3, choose a point *p**i*+3 ∈*Z**i*.

**Fig. 3**

[image: Fig. 3]

[Full size image][41]

Cases 1 and 2

In Case 1, we use the fact that *Z**k*−2 does not contain an *n*-cup, therefore it must contain an (*l*+2)-cap *C**k*−2 ={*p*1,*q*1,…,*q**l*,*p*2 }. In Case 2, we use the fact that *Z**k*−2 does not contain an *n*-cap, therefore it must contain an (*l*+2)-cup *C**k*−2 ={*p*2,*q**l*,…,*q*1,*p*1 }.

In either case, the set *C**k*−2 ∪*C*1 ∪{*p*5,…,*p**k*} is a configuration whose order type is \(\mathcal{G}_{k;l}\); see Fig. [4][42]. It is proved that \(\mathcal{G}_{k;l}\hookrightarrow X\).

**Fig. 4**

[image: Fig. 4]

[Full size image][43]

Finding \(\mathcal{G}_{k;l}\)

□

## 4 Order Types with Triangular Convex Hull

The following result estimates the function \(F_{\mathcal{T}}(n)\) for order types \({\mathcal{T}}\) of at least four points whose convex hull has three vertices.

### Theorem 8

*Let*\({\mathcal{T}}\)*be an order type of at least*4 *points*, *whose convex hull has three vertices*.

1. (i)

*If*\({\mathcal{T}}={\mathcal{E}}_{k}\)*for some**k*≥1, *then*\(F_{\mathcal{T}}(n)\)*is bounded from above by a linear function of**n*.

2. (ii)

*If*\({\mathcal{T}}={\mathcal{F}}_{k}\)*for some**k*≥3, *then*\(F_{\mathcal{T}}(n)\)*is bounded from below by a quadratic function*, *and bounded from above by a polynomial in**n*.

3. (iii)

*If*\({\mathcal{T}}\ne{\mathcal{E}}_{k}, {\mathcal{F}}_{k}\), *then*\(F_{\mathcal{T}}(n)\)*grows exponentially in**n*.

Part (i) and the lower bound in (ii) are proved in [[15][31]]. The upper bound in (ii) is proved in Theorem 4. In the rest of the section we prove (iii).

We need the following special cases of the twin construction. For any nonnegative integer *m*let \(m=\sum_{i=0}^{\infty}a_{i}2^{i}\) (*a**i*∈{0,1}) be its binary representation and let \(\overline{m}=\sum_{i=0}^{\infty}a_{i}2^{4^{i}}\). Define \(\mathit{RH}_{k}=\{ (m, \overline{m}) \mid0\le m<2^{k}\}\) and let \(\mathcal{RH}_{k}\) denote its order type. Similarly, \(\mathit{LH}_{k}=\{ (-m, \overline{m}) \mid0\le m<2^{k}\}\) and let \(\mathcal{LH}_{k}\) denote its order type. It is not hard to check the following properties:

1. (i)

*RH**k*is a twin construction;

2. (ii)

each set *RH**k*is centrally symmetric;

3. (iii)

for any *k*<*n*, *RH**n*is the disjoint union of 2*n*−*k*translated copies *RH**k*(1),…,*RH**k*(2*n*−*k*) of *RH**k*=*RH**k*(1) and for every *i*<*j*, *RH**k*(*j*) is to the right of *RH**k*(*i*);

4. (iv)

for every *i*<*j*, *RH**k*(*j*) is above every line determined by the points of *RH**k*(*i*), and *RH**k*(*i*) is below every line determined by the points of *RH**k*(*j*).

Obviously, similar statements hold for *LH**k*.

### Lemma 9

*Let**n**be a positive integer and let*\({\mathcal{T}}\)*be an order type of six points whose convex hull is a triangle*. *If*\({\mathcal{T}}\)*is contained in both*\({\mathcal{L}H}_{n}\)*and*\({\mathcal{R}H}_{n}\), *then*\({\mathcal{T}}={\mathcal{E}}_{3}\), *or*\({\mathcal{T}}={\mathcal{F}}_{3}\).

We prove Lemma 9 at the end of the section.

### Proof of Theorem 8 (iii)

Since both *RH**n*and *LH**n*are twin constructions, by Lemma 2 they do not contain 2*n*+1 points in convex position. Therefore, it suffices to prove that if \({\mathcal{T}}\ne{\mathcal{E}}_{k}, {\mathcal{F}}_{k}\), then for every *n*we have \(T\not\hookrightarrow \mathit{RH}_{n}\) or \(T\not\hookrightarrow \mathit{LH}_{n}\).

Let *T*be a configuration of at least 4 points such that its convex hull is a triangle *abc*, and suppose that for some *n*we have *T*↪*RH**n*and *T*↪*LH**n*. If |*T*|≤5, then \(T\in\mathcal{E}_{1}=\mathcal{F}_{1}\), or \(T\in\mathcal{E}_{2}=\mathcal{F}_{2}\). Suppose that 6≤|*T*|=*k*+3. Let *S*⊆*T*such that *a*,*b*,*c*∈*S*and |*S*|=6. Then by Lemma 9, the order type of *S*is either \(\mathcal{E}_{3}\) or \(\mathcal{F}_{3}\). Therefore, for any three points *p*,*q*,*r*of *T*∖{*a*,*b*,*c*}, the three lines determined by *p*,*q*,*r*intersect the same two sides of triangle *abc*. It follows that *every*line determined by the points of *T*∖{*a*,*b*,*c*}, intersect the same two sides of triangle *abc*, say, *ac*and *bc*. Introduce again the partial order used in the proof of Theorem 4. For *p*,*q*∈*T*∖{*a*,*b*,*c*}, let *p*≺*ab**q*if and only if the ray *pq*intersects side *bc*and the ray *qp*intersects side *ac*of the triangle *abc*. In this case any two points of *T*∖{*a*,*b*,*c*} are comparable, therefore, it defines a linear order. That is, the elements of *T*∖{*a*,*b*,*c*} can be ordered as *p*1,…,*p**k*so that for any *i*<*j*, rays *p**i**p**j*and *p**j**p**i*intersect sides *bc*and *ac*, respectively. Assume that \(T_{i}=\{ a,b,c,p_{i},p_{i+1},p_{i+2}\}\in\mathcal{F}_{3}\) and \(T_{i+1}=\{ a,b,c,p_{i+1},p_{i+2},p_{i+3}\}\in\mathcal{E}_{3}\) for some 1≤*i*≤*k*−3. Then points *p**i*+1,*p**i*+2,*p**i*+3 lie inside triangle *p**i**bc*so that line *p**i*+1*p**i*+2 intersects sides *p**i**b*and *bc*, while line *p**i*+2*p**i*+3 intersects sides *p**i**c*and *bc*of the triangle (see Fig. [5][44]), contradicting Lemma 9. By symmetry, it is not possible that \(T_{i}\in\mathcal{E}_{3}\) and \(T_{i+1}\in\mathcal{F}_{3}\). Therefore *T**i*must belong to the same order type, either \(\mathcal{E}_{3}\) or \(\mathcal{F}_{3}\), for every 1≤*i*≤*k*−3. Therefore, \(T\in\mathcal{E}_{k}\) or \(T \in\mathcal{F}_{k}\). This concludes the proof of Theorem 8. It remains to prove Lemma 9.

**Fig. 5**

[image: Fig. 5]

[Full size image][45]

\(S=\{ b,c,p_{i},p_{i+1},p_{i+2},p_{i+3}\}\not\in\mathcal{E}_{3}\cup\mathcal{F}_{3}\)

□

### Proof of Lemma 9

If \({\mathcal{T}}\ne {\mathcal{E}}_{3}, {\mathcal{F}}_{3}\), then \({\mathcal{T}}\) is either one of the four order types depicted on Fig. [6][46], or one of the mirror images \({\mathcal{C}}^{\top}\), \({\mathcal{D}}^{\top}\).

**Fig. 6**

[image: Fig. 6]

[Full size image][47]

Order types of six points

We must prove that neither of these six order types is contained in both \({\mathcal{L}H}_{n}\) and \({\mathcal{R}H}_{n}\). Since \(\mathcal{A}\) has the separation property, it is not contained in any twin construction. Therefore neither \({\mathcal{L}H}_{n}\) nor \({\mathcal{R}H}_{n}\) does contain \(\mathcal{A}\).

Now we show that \(\mathcal{B}\) is not contained in \({\mathcal{R}H}_{n}\). Assume that on the contrary, *a*,*b*,*c*,*x*,*y*,*z*∈*RH**n*and \(\{a,b,c,x,y,z\}\in\mathcal{B}\). Consider the smallest *k*such that {*x*,*y*,*z*} is contained in *RH**k*(*i*) for some 1≤*i*≤2*n*−*k*. Both *RH**k*−1 (2*i*−1) and *RH**k*−1 (2*i*) must contain at least one of *x*,*y*,*z*. By symmetry, we can assume without loss of generality that *x*,*y*∈*RH**k*−1 (2*i*−1) and *z*∈*RH**k*−1 (2*i*). Note that *z*is inside triangle *xyc*. Now *c*∈*RH**k*−1 (*j*) for some 1≤*j*≤2*n*−*k*+1. If *j*<2*i*, then any vertical line that separates *RH**k*−1 (2*i*−1) and *RH**k*−1 (2*i*) would separate {*x*,*y*,*c*} from *z*which is impossible. If *j*=2*i*, then both *x*and *y*would lie below the line *cz*, so *cz*would not separate *x*and *y*. Finally, if *j*>2*i*, then both *x*and *y*would lie left to the line *cz*, again a contradiction.

To see that \(\mathcal{C}\) is not contained in \({\mathcal{L}H}_{n}\), assume that *a*,*b*,*c*,*x*,*y*,*z*∈*LH**n*and \(\{a,b,c,x,y,z\}\in\mathcal{C}\). Let *k*be the smallest integer such that {*x*,*y*,*z*}⊂*LH**k*(*i*) for some 1≤*i*≤2*n*−*k*. Again, by symmetry we may assume that exactly one of the three points *x*,*y*, and *z*lies in *LH**k*−1 (2*i*−1). We distinguish three subcases.

*Case 1:**z*∈*LH**k*−1 (2*i*−1) and *x*,*y*∈*LH**k*−1 (2*i*). Since *z*is inside triangle *xyc*, by the previous argument we find that *c*cannot be in any subset *LH**k*−1 (*j*).

*Case 2:**y*∈*LH**k*−1 (2*i*−1) and *x*,*z*∈*LH**k*−1 (2*i*). Now we use the fact that *y*is inside triangle *zxb*. We arrive at a contradiction as before: there is no place for the point *b*.

*Case 3:**x*∈*LH**k*−1 (2*i*−1) and *y*,*z*∈*LH**k*−1 (2*i*). Because of the orientation of triangle *xyz*, the points *x*,*y*,*z*follow each other from left to right in this order. Since the orientation of both triangles *yzb*and *yzc*is clockwise, both *b*and *c*must lie under any horizontal line *ℓ*that separates *LH**k*−1 (2*i*−1) and *LH**k*−1 (2*i*). Point *x*sees *y*,*z*, and *c*in this order, therefore *c*must lie in *LH**k*−1 (2*i*). For triangle *abc*to contain *x*, point *a*must lie above *ℓ*. But then line *ax*cannot separate *z*and *c*, a contradiction.

Thus we have proved that \(\mathcal{C}\) is indeed not contained in \({\mathcal{L}H}_{n}\). By symmetry, \(\mathcal{C}^{\top}\) is not contained in \({\mathcal{R}H}_{n}\). A similar argument shows that \({\mathcal{R}H}_{n}\) does not contain \(\mathcal{D}\) and \({\mathcal{L}H}_{n}\) does not contain \(\mathcal{D}^{\top}\). We omit the technical details. □

### Remarks

Erdős and Szekeres conjectured that the following stronger version of their theorem holds. For every *n*there is an *N*with the property that any set of *N*points in general position contains an *empty*convex *n*-gon, that is, *n*points in convex position such that their convex hull does not contain any other point of the point set in its interior. But as a great surprise, Horton proved that the conjecture does not hold for *n*≥7 [[13][48]]. He constructed arbitrarily large point sets with no empty convex heptagons. His construction is a very special, and probably the most famous twin construction. The notations *LH**k*and *RH**k*are abbreviations of “Left Horton Set” and “Right Horton Set”, respectively. The idea of the twin construction is quite similar to that of a construction introduced in [[16][49]] in order to obtain lower bounds to the Erdős–Szekeres function in higher dimensions.

### Open Problems

For each non-convex order type \({\mathcal{T}}\) of four or five points, it is easy to see that \(F_{\mathcal{T}}(n)\le2n-3\). There are 15 non-convex order types of six points [[1][50]]. By our results, for five of them \(F_{\mathcal{T}}(n)\) is bounded from above by a polynomial, for five of them \(F_{\mathcal{T}}(n)\) grows exponentially, and for five of them, shown on Fig. [7][51], the order of magnitude of \(F_{\mathcal{T}}(n)\) is not known. Probably it is not too hard to give the answer for some of these order types.

**Fig. 7**

[image: Fig. 7]

[Full size image][52]

The smallest remaining order types

Another interesting question is, whether the answer is always either “polynomial” or “exponential”. More precisely, is there an order type \({\mathcal{T}}\) for which \(F_{\mathcal{T}}(n)\) is bounded from above by the exponential function *c**n*for every *c*>1, if *n*is large enough, and bounded from below the polynomial *n**k*for every *k*>0, if *n*is large enough?

## References

1.

Aichholzer, O., Aurenhammer, F., Krasser, H.: Enumerating order types for small point sets with applications. Order **19**, 265–281 (2002)

[Article][53] [MathSciNet][54] [MATH][55] [Google Scholar][56]

2.

Alon, N., Pach, J., Solymosi, J.: Ramsey-type theorems with forbidden subgraphs. Combinatorica **21**, 155–170 (2001)

[Article][57] [MathSciNet][58] [MATH][59] [Google Scholar][60]

3.

Aronov, B., Erdős, P., Goddard, W., Kleitman, D.J., Klugerman, M., Pach, J., Schulman, L.J.: Crossing families. Combinatorica **14**, 127–134 (1994)

[Article][61] [MathSciNet][62] [MATH][63] [Google Scholar][64]

4.

Bárány, I., Károlyi, Gy.: Problems and results around the Erdős–Szekeres convex polygon theorem. In: Akiyama, J., et al. (eds.) Discrete and Computational Geometry. Lecture Notes in Computer Science, vol. 2098, pp. 91–105. Springer Berlin (2001)

[Chapter][65] [Google Scholar][66]

5.

Bárány, I., Valtr, P.: A positive fraction Erdős–Szekeres theorem. Discrete Comput. Geom. **19**, 335–342 (1998)

[Article][67] [MathSciNet][68] [MATH][69] [Google Scholar][70]

6.

Chudnovsky, M., Safra, S.: The Erdős–Hajnal conjecture for bull-free graphs. J. Comb. Theory, Ser. B **98**, 1301–1310 (2008)

[Article][71] [MathSciNet][72] [MATH][73] [Google Scholar][74]

7.

Dilworth, R.P.: A decomposition theorem for partially ordered sets. Ann. Math. **51**, 161–166 (1950)

[Article][75] [MathSciNet][76] [MATH][77] [Google Scholar][78]

8.

Erdős, P., Hajnal, A.: Ramsey-type theorems. Discrete Appl. Math. **25**, 37–52 (1989)

[Article][79] [MathSciNet][80] [Google Scholar][81]

9.

Erdős, P., Szekeres, G.: A combinatorial problem in geometry. Compos. Math. **2**, 463–470 (1935)

[Google Scholar][82]

10.

Erdős, P., Szekeres, G.: On some extremum problems in elementary geometry. Ann. Univ. Sci. Bp. Rolando Eötvös Nomin., Sect. Math. **3/4**, 53–62 (1960–1961)

[Google Scholar][83]

11.

Fox, J., Sudakov, B.: Induced Ramsey-type theorems. Adv. Math. **219**, 1771–1800 (2008)

[Article][84] [MathSciNet][85] [MATH][86] [Google Scholar][87]

12.

Goodman, J.E., Pollack, R.: Allowable sequences and order types in discrete and computational geometry. In: Pach, J. (ed.) New Trends In Discrete and Computational Geometry. Algorithms and Combinatorics, vol. 10, pp. 103–134. Springer, Berlin (1993)

[Chapter][88] [Google Scholar][89]

13.

Horton, J.D.: Sets with no empty convex 7-gons. Can. Math. Bull. **26**, 482–484 (1983)

[Article][90] [MathSciNet][91] [MATH][92] [Google Scholar][93]

14.

Johnson, S.C.: A new proof of the Erdős–Szekeres convex *k*-gon result. J. Comb. Theory, Ser. A **42**, 318–319 (1986)

[Article][94] [MATH][95] [Google Scholar][96]

15.

Károlyi, Gy., Solymosi, J.: Erdős–Szekeres theorem with forbidden order types. J. Comb. Theory, Ser. A **13**, 455–465 (2006)

[Article][97] [Google Scholar][98]

16.

Károlyi, Gy., Valtr, P.: Point configurations in *d*-space without large subsets in convex position. Discrete Comput. Geom. **30**, 277–286 (2003)

[Article][99] [MathSciNet][100] [MATH][101] [Google Scholar][102]

17.

Morris, W., Soltan, V.: The Erdős–Szekeres problem on points in convex position – a survey. Bull. Am. Math. Soc. **37**, 437–458 (2000)

[Article][103] [MathSciNet][104] [MATH][105] [Google Scholar][106]

18.

Nešetřil, J., Valtr, P.: A Ramsey property of order types. J. Comb. Theory, Ser. A **81**, 88–107 (1998)

[Article][107] [MATH][108] [Google Scholar][109]

19.

Pór, A., Valtr, P.: The partitioned version of the Erdős–Szekeres theorem. Discrete Comput. Geom. **28**, 625–637 (2002)

[Article][110] [MathSciNet][111] [MATH][112] [Google Scholar][113]

20.

Tóth, G, Valtr, P.: The Erdős–Szekeres theorem: upper bounds and related results. In: Goodman, J.E., et al. (eds.) Combinatorial and Computational Geometry. Publ. M.S.R.I., vol. 52, pp. 557–568 (2005)

[Google Scholar][114]

[Download references][115]

## Acknowledgements

This paper was completed during the special semester on Discrete and Computational Geometry held at the EPFL Lausanne, sponsored by the Centre Interfacultaire Bernoulli and the Swiss National Science Foundation. The first author was supported by Bolyai Research Fellowship and OTKA Grant NK67867. The second author was supported by OTKA Grants K83767 and NN102029.

## Author information

### Authors and Affiliations

1.

Institute of Mathematics, Eötvös University, Pázmány P. sétány 1/C, Budapest, 1117, Hungary

Gyula Károlyi

2.

Alfréd Rényi Institute of Mathematics, Reáltanoda u. 15, Budapest, 1053, Hungary

Géza Tóth

Authors

1. Gyula Károlyi

[View author publications][116]

Search author on: [PubMed][117] [Google Scholar][118]

2. Géza Tóth

[View author publications][119]

Search author on: [PubMed][120] [Google Scholar][121]

### Corresponding author

Correspondence to [Géza Tóth][122].

## Rights and permissions

[Reprints and permissions][123]

## About this article

### Cite this article

Károlyi, G., Tóth, G. Erdős–Szekeres Theorem for Point Sets with Forbidden Subconfigurations. *Discrete Comput Geom***48**, 441–452 (2012). https://doi.org/10.1007/s00454-012-9424-6

[Download citation][124]

-

Received: 19 April 2011

-

Revised: 14 March 2012

-

Accepted: 14 March 2012

-

Published: 31 March 2012

-

Issue date: September 2012

-

DOI: https://doi.org/10.1007/s00454-012-9424-6

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Order type][125]
- [Erdős–Szekeres theorem][126]
- [Combinatorial convexity][127]


## Links

[1]: /content/pdf/10.1007/s00454-012-9424-6.pdf
[2]: /article/10.1007/s00454-012-9424-6/save-research?_csrf=dpQ0bxM3IDSM08MI65ow0lgf4ONm4oXj
[3]: /saved-research
[4]: /journal/454
[5]: /journal/454/aims-and-scope
[6]: https://www.editorialmanager.com/dcge
[7]: https://link.springer.com/10.1007/978-3-662-57413-3_9?fromPaywallRec=false
[8]: https://link.springer.com/10.1007/978-3-030-25005-8_4?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s00454-017-9931-6?fromPaywallRec=false
[10]: /subjects/combinatorial-geometry
[11]: /subjects/convex-and-discrete-geometry
[12]: /subjects/discrete-mathematics
[13]: /subjects/geometry
[14]: /subjects/polytopes
[15]: /subjects/set-theory
[16]: /subjects/combinatorial-structures-and-intersection-theorems
[17]: /article/10.1007/s00454-012-9424-6#ref-CR9
[18]: /article/10.1007/s00454-012-9424-6#ref-CR10
[19]: /article/10.1007/s00454-012-9424-6#ref-CR20
[20]: /article/10.1007/s00454-012-9424-6#ref-CR14
[21]: /article/10.1007/s00454-012-9424-6#ref-CR17
[22]: /article/10.1007/s00454-012-9424-6#ref-CR8
[23]: /article/10.1007/s00454-012-9424-6#ref-CR11
[24]: /article/10.1007/s00454-012-9424-6#ref-CR2
[25]: /article/10.1007/s00454-012-9424-6#ref-CR6
[26]: /article/10.1007/s00454-012-9424-6#ref-CR12
[27]: /article/10.1007/s00454-012-9424-6#ref-CR18
[28]: /article/10.1007/s00454-012-9424-6#ref-CR19
[29]: /article/10.1007/s00454-012-9424-6#ref-CR5
[30]: /article/10.1007/s00454-012-9424-6#ref-CR4
[31]: /article/10.1007/s00454-012-9424-6#ref-CR15
[32]: /article/10.1007/s00454-012-9424-6#Fig1
[33]: /article/10.1007/s00454-012-9424-6/figures/1
[34]: /article/10.1007/s00454-012-9424-6#Sec3
[35]: /article/10.1007/s00454-012-9424-6#Sec4
[36]: /article/10.1007/s00454-012-9424-6#Fig2
[37]: /article/10.1007/s00454-012-9424-6/figures/2
[38]: /article/10.1007/s00454-012-9424-6#ref-CR7
[39]: /article/10.1007/s00454-012-9424-6#ref-CR3
[40]: /article/10.1007/s00454-012-9424-6#Fig3
[41]: /article/10.1007/s00454-012-9424-6/figures/3
[42]: /article/10.1007/s00454-012-9424-6#Fig4
[43]: /article/10.1007/s00454-012-9424-6/figures/4
[44]: /article/10.1007/s00454-012-9424-6#Fig5
[45]: /article/10.1007/s00454-012-9424-6/figures/5
[46]: /article/10.1007/s00454-012-9424-6#Fig6
[47]: /article/10.1007/s00454-012-9424-6/figures/6
[48]: /article/10.1007/s00454-012-9424-6#ref-CR13
[49]: /article/10.1007/s00454-012-9424-6#ref-CR16
[50]: /article/10.1007/s00454-012-9424-6#ref-CR1
[51]: /article/10.1007/s00454-012-9424-6#Fig7
[52]: /article/10.1007/s00454-012-9424-6/figures/7
[53]: https://doi.org/10.1023%2FA%3A1021231927255
[54]: http://www.ams.org/mathscinet-getitem?mr=1942187
[55]: http://www.emis.de/MATH-item?1027.68127
[56]: http://scholar.google.com/scholar_lookup?amp;title=Enumerating%20order%20types%20for%20small%20point%20sets%20with%20applications&amp;journal=Order&amp;doi=10.1023%2FA%3A1021231927255&amp;volume=19&amp;pages=265-281&amp;publication_year=2002&amp;author=Aichholzer%2CO.&amp;author=Aurenhammer%2CF.&amp;author=Krasser%2CH.
[57]: https://link.springer.com/doi/10.1007/s004930100016
[58]: http://www.ams.org/mathscinet-getitem?mr=1832443
[59]: http://www.emis.de/MATH-item?0989.05124
[60]: http://scholar.google.com/scholar_lookup?amp;title=Ramsey-type%20theorems%20with%20forbidden%20subgraphs&amp;journal=Combinatorica&amp;doi=10.1007%2Fs004930100016&amp;volume=21&amp;pages=155-170&amp;publication_year=2001&amp;author=Alon%2CN.&amp;author=Pach%2CJ.&amp;author=Solymosi%2CJ.
[61]: https://link.springer.com/doi/10.1007/BF01215345
[62]: http://www.ams.org/mathscinet-getitem?mr=1289067
[63]: http://www.emis.de/MATH-item?0804.52010
[64]: http://scholar.google.com/scholar_lookup?amp;title=Crossing%20families&amp;journal=Combinatorica&amp;doi=10.1007%2FBF01215345&amp;volume=14&amp;pages=127-134&amp;publication_year=1994&amp;author=Aronov%2CB.&amp;author=Erd%C5%91s%2CP.&amp;author=Goddard%2CW.&amp;author=Kleitman%2CD.J.&amp;author=Klugerman%2CM.&amp;author=Pach%2CJ.&amp;author=Schulman%2CL.J.
[65]: https://link.springer.com/doi/10.1007/3-540-47738-1_7
[66]: http://scholar.google.com/scholar_lookup?amp;title=Problems%20and%20results%20around%20the%20Erd%C5%91s%E2%80%93Szekeres%20convex%20polygon%20theorem&amp;doi=10.1007%2F3-540-47738-1_7&amp;pages=91-105&amp;publication_year=2001&amp;author=B%C3%A1r%C3%A1ny%2CI.&amp;author=K%C3%A1rolyi%2CGy.
[67]: https://link.springer.com/doi/10.1007/PL00009350
[68]: http://www.ams.org/mathscinet-getitem?mr=1608874
[69]: http://www.emis.de/MATH-item?0914.52007
[70]: http://scholar.google.com/scholar_lookup?amp;title=A%20positive%20fraction%20Erd%C5%91s%E2%80%93Szekeres%20theorem&amp;journal=Discrete%20Comput.%20Geom.&amp;doi=10.1007%2FPL00009350&amp;volume=19&amp;pages=335-342&amp;publication_year=1998&amp;author=B%C3%A1r%C3%A1ny%2CI.&amp;author=Valtr%2CP.
[71]: https://doi.org/10.1016%2Fj.jctb.2008.02.005
[72]: http://www.ams.org/mathscinet-getitem?mr=2462320
[73]: http://www.emis.de/MATH-item?1168.05317
[74]: http://scholar.google.com/scholar_lookup?amp;title=The%20Erd%C5%91s%E2%80%93Hajnal%20conjecture%20for%20bull-free%20graphs&amp;journal=J.%20Comb.%20Theory%2C%20Ser.%20B&amp;doi=10.1016%2Fj.jctb.2008.02.005&amp;volume=98&amp;pages=1301-1310&amp;publication_year=2008&amp;author=Chudnovsky%2CM.&amp;author=Safra%2CS.
[75]: https://doi.org/10.2307%2F1969503
[76]: http://www.ams.org/mathscinet-getitem?mr=32578
[77]: http://www.emis.de/MATH-item?0038.02003
[78]: http://scholar.google.com/scholar_lookup?amp;title=A%20decomposition%20theorem%20for%20partially%20ordered%20sets&amp;journal=Ann.%20Math.&amp;doi=10.2307%2F1969503&amp;volume=51&amp;pages=161-166&amp;publication_year=1950&amp;author=Dilworth%2CR.P.
[79]: https://doi.org/10.1016%2F0166-218X%2889%2990045-0
[80]: http://www.ams.org/mathscinet-getitem?mr=1031262
[81]: http://scholar.google.com/scholar_lookup?amp;title=Ramsey-type%20theorems&amp;journal=Discrete%20Appl.%20Math.&amp;doi=10.1016%2F0166-218X%2889%2990045-0&amp;volume=25&amp;pages=37-52&amp;publication_year=1989&amp;author=Erd%C5%91s%2CP.&amp;author=Hajnal%2CA.
[82]: http://scholar.google.com/scholar_lookup?amp;title=A%20combinatorial%20problem%20in%20geometry&amp;journal=Compos.%20Math.&amp;volume=2&amp;pages=463-470&amp;publication_year=1935&amp;author=Erd%C5%91s%2CP.&amp;author=Szekeres%2CG.
[83]: http://scholar.google.com/scholar_lookup?amp;title=On%20some%20extremum%20problems%20in%20elementary%20geometry&amp;journal=Ann.%20Univ.%20Sci.%20Bp.%20Rolando%20E%C3%B6tv%C3%B6s%20Nomin.%2C%20Sect.%20Math.&amp;volume=3%2F4&amp;pages=53-62&amp;publication_year=1960%E2%80%931961&amp;author=Erd%C5%91s%2CP.&amp;author=Szekeres%2CG.
[84]: https://doi.org/10.1016%2Fj.aim.2008.07.009
[85]: http://www.ams.org/mathscinet-getitem?mr=2455625
[86]: http://www.emis.de/MATH-item?1152.05054
[87]: http://scholar.google.com/scholar_lookup?amp;title=Induced%20Ramsey-type%20theorems&amp;journal=Adv.%20Math.&amp;doi=10.1016%2Fj.aim.2008.07.009&amp;volume=219&amp;pages=1771-1800&amp;publication_year=2008&amp;author=Fox%2CJ.&amp;author=Sudakov%2CB.
[88]: https://link.springer.com/doi/10.1007/978-3-642-58043-7_6
[89]: http://scholar.google.com/scholar_lookup?amp;title=Allowable%20sequences%20and%20order%20types%20in%20discrete%20and%20computational%20geometry&amp;doi=10.1007%2F978-3-642-58043-7_6&amp;pages=103-134&amp;publication_year=1993&amp;author=Goodman%2CJ.E.&amp;author=Pollack%2CR.
[90]: https://doi.org/10.4153%2FCMB-1983-077-8
[91]: http://www.ams.org/mathscinet-getitem?mr=716589
[92]: http://www.emis.de/MATH-item?0521.52010
[93]: http://scholar.google.com/scholar_lookup?amp;title=Sets%20with%20no%20empty%20convex%207-gons&amp;journal=Can.%20Math.%20Bull.&amp;doi=10.4153%2FCMB-1983-077-8&amp;volume=26&amp;pages=482-484&amp;publication_year=1983&amp;author=Horton%2CJ.D.
[94]: https://doi.org/10.1016%2F0097-3165%2886%2990106-8
[95]: http://www.emis.de/MATH-item?0591.52005
[96]: http://scholar.google.com/scholar_lookup?amp;title=A%20new%20proof%20of%20the%20Erd%C5%91s%E2%80%93Szekeres%20convex%20k-gon%20result&amp;journal=J.%20Comb.%20Theory%2C%20Ser.%20A&amp;doi=10.1016%2F0097-3165%2886%2990106-8&amp;volume=42&amp;pages=318-319&amp;publication_year=1986&amp;author=Johnson%2CS.C.
[97]: https://doi.org/10.1016%2Fj.jcta.2005.04.006
[98]: http://scholar.google.com/scholar_lookup?amp;title=Erd%C5%91s%E2%80%93Szekeres%20theorem%20with%20forbidden%20order%20types&amp;journal=J.%20Comb.%20Theory%2C%20Ser.%20A&amp;doi=10.1016%2Fj.jcta.2005.04.006&amp;volume=13&amp;pages=455-465&amp;publication_year=2006&amp;author=K%C3%A1rolyi%2CGy.&amp;author=Solymosi%2CJ.
[99]: https://link.springer.com/doi/10.1007/s00454-003-0009-4
[100]: http://www.ams.org/mathscinet-getitem?mr=2007965
[101]: http://www.emis.de/MATH-item?1051.52012
[102]: http://scholar.google.com/scholar_lookup?amp;title=Point%20configurations%20in%20d-space%20without%20large%20subsets%20in%20convex%20position&amp;journal=Discrete%20Comput.%20Geom.&amp;doi=10.1007%2Fs00454-003-0009-4&amp;volume=30&amp;pages=277-286&amp;publication_year=2003&amp;author=K%C3%A1rolyi%2CGy.&amp;author=Valtr%2CP.
[103]: https://doi.org/10.1090%2FS0273-0979-00-00877-6
[104]: http://www.ams.org/mathscinet-getitem?mr=1779413
[105]: http://www.emis.de/MATH-item?0958.52018
[106]: http://scholar.google.com/scholar_lookup?amp;title=The%20Erd%C5%91s%E2%80%93Szekeres%20problem%20on%20points%20in%20convex%20position%20%E2%80%93%20a%20survey&amp;journal=Bull.%20Am.%20Math.%20Soc.&amp;doi=10.1090%2FS0273-0979-00-00877-6&amp;volume=37&amp;pages=437-458&amp;publication_year=2000&amp;author=Morris%2CW.&amp;author=Soltan%2CV.
[107]: https://doi.org/10.1006%2Fjcta.1997.2820
[108]: http://www.emis.de/MATH-item?0902.52006
[109]: http://scholar.google.com/scholar_lookup?amp;title=A%20Ramsey%20property%20of%20order%20types&amp;journal=J.%20Comb.%20Theory%2C%20Ser.%20A&amp;doi=10.1006%2Fjcta.1997.2820&amp;volume=81&amp;pages=88-107&amp;publication_year=1998&amp;author=Ne%C5%A1et%C5%99il%2CJ.&amp;author=Valtr%2CP.
[110]: https://link.springer.com/doi/10.1007/s00454-002-2894-1
[111]: http://www.ams.org/mathscinet-getitem?mr=1949905
[112]: http://www.emis.de/MATH-item?1019.52011
[113]: http://scholar.google.com/scholar_lookup?amp;title=The%20partitioned%20version%20of%20the%20Erd%C5%91s%E2%80%93Szekeres%20theorem&amp;journal=Discrete%20Comput.%20Geom.&amp;doi=10.1007%2Fs00454-002-2894-1&amp;volume=28&amp;pages=625-637&amp;publication_year=2002&amp;author=P%C3%B3r%2CA.&amp;author=Valtr%2CP.
[114]: http://scholar.google.com/scholar_lookup?amp;title=The%20Erd%C5%91s%E2%80%93Szekeres%20theorem%3A%20upper%20bounds%20and%20related%20results&amp;pages=557-568&amp;publication_year=2005&amp;author=T%C3%B3th%2CG&amp;author=Valtr%2CP.
[115]: https://citation-needed.springer.com/v2/references/10.1007/s00454-012-9424-6?format=refman&amp;flavour=references
[116]: /search?sortBy=newestFirst&amp;contributor=Gyula%20K%C3%A1rolyi
[117]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Gyula%20K%C3%A1rolyi
[118]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Gyula%20K%C3%A1rolyi%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[119]: /search?sortBy=newestFirst&amp;contributor=G%C3%A9za%20T%C3%B3th
[120]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=G%C3%A9za%20T%C3%B3th
[121]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22G%C3%A9za%20T%C3%B3th%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[122]: mailto:geza@renyi.hu
[123]: https://s100.copyright.com/AppDispatchServlet?title=Erd%C5%91s%E2%80%93Szekeres%20Theorem%20for%20Point%20Sets%20with%20Forbidden%20Subconfigurations&amp;author=Gyula%20K%C3%A1rolyi%20et%20al&amp;contentID=10.1007%2Fs00454-012-9424-6&amp;copyright=Springer%20Science%2BBusiness%20Media%2C%20LLC&amp;publication=0179-5376&amp;publicationDate=2012-03-31&amp;publisherName=SpringerNature&amp;orderBeanReset=true
[124]: https://citation-needed.springer.com/v2/references/10.1007/s00454-012-9424-6?format=refman&amp;flavour=citation
[125]: /search?query=Order%20type&amp;facet-discipline=#34;Mathematics&#34;
[126]: /search?query=Erd%C5%91s%E2%80%93Szekeres%20theorem&amp;facet-discipline=#34;Mathematics&#34;
[127]: /search?query=Combinatorial%20convexity&amp;facet-discipline=#34;Mathematics&#34;
