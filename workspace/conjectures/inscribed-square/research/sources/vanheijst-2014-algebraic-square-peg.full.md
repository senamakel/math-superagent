<!-- source: https://ar5iv.labs.arxiv.org/html/1403.5979 | converted from HTML -->

[1403.5979] The algebraic square peg problem Master’s thesis in mathematics, Aalto University, March 2014.

# The algebraic square peg problem
Master’s thesis in mathematics, Aalto University, March 2014.

Wouter van Heijst

## 1 Introduction

Toeplitz conjectured in 1911 that every continuous closed curve in the plane that does not self-intersect, also known as a Jordan curve, contains all four corners of some square. More than a hundred years have passed since the statement of Toeplitz’s conjecture; various partial results assuming the curve satisfies additional smoothness properties have been proven, but in full generality the problem remains unsolved.

Why look at squares? The conjecture does not hold if squares are replaced with regular polygons with more than four vertices; Eggleston [5] gave an example of a convex curve, a curve that is the boundary of a convex region of the plane, that does not inscribe any regular polygon with more than four vertices. On the other hand, the conjecture does hold if squares are replaced by triangles or rectangles; Nielsen [16] showed that any Jordan curve inscribes a triangle and Vaughan, by way of Meyerson [15], proved that every Jordan curve inscribes some rectangle. Vaughan’s proof has no control over the aspect ratio of the inscribed rectangle. Both these cases are discussed in Igor Pak’s online book “Lectures on Discrete and Polyhedral Geometry” [17, Section 5, “Inscribed and circumscribed polgons”]. We shall concern ourselves in this thesis with the special case of inscribing a rectangle with prescribed equal aspect ratio, otherwise known as a square. See Matschke’s survey paper [14, Section 4] for further problems related to the square peg problem.

Initial publications on the square peg problem, as Toeplitz’s conjecture has become known, were made by Emch; who proved the existence of an inscribed square on convex curves [7] in 1913 and three years later for piecewise analytic curves with a finite number of singularieties [8]. According to Matschke [14, Emch’s proof], implicit in Emch’s work is the understanding that a generic curve inscribes an odd number of squares. Since zero is not an odd number, such a parity argument implies the existence of at least one inscribed square, thereby proving Toeplitz’s conjecture for these restricted classes of curves. The sense of genericity is important; Popvassilev showed that for any natural number n n, there exists a continuous curve that inscribes exactly n n squares [19].

Further work on the square peg problem came from, among others, the hands of Jerrard [13], and Stromquist [26]. Jerrard’s proof for analytic curves and Stromquist’s proof for locally monotone curves both show show that generically the number of squares inscribed on a smooth enough curve is odd. Stromquist’s locally monotone curves is one of the largest classes for which Toeplitz’s conjecture is known to hold. In more recent years Pak [18] has given an elementary proof for piecewise linear curves while Matschke [14, Theorem 3.3] has generalized the square peg problem to arbitrary metric spaces.

We refer readers interested in the history of the square peg problem to Matschke’s survey paper [14] or the papers of Sagols and Marín [22, Section 1] and Pak [18, Section 3].

In this thesis we shall employ algebra, rather than the analytical and topological methods of the above approaches, to count the number of squares that may be inscribed on a curve. Thus the class of curves we consider is that of the algebraic plane curves, which are curves defined by the vanishing of a polynomial in two variables. These are no longer neccessarily Jordan curves, but exhibit interesting behaviour nonetheless. The main result of this thesis, Theorem 4.8, states that an algebraic plane curve of degree m m inscribes at most ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 isolated squares. Section 5 \@vpageref []sec:experimental provides some evidence for the claim that a generic complex algebraic plane curve inscribes exactly ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 squares. The behaviour of real algebraic plane curves is less clear, examples of real algebraic plane curves of different topological types inscribing various numbers of squares are listed in Section 6 \@vpageref []sec:illustrative. Those examples form the basis for three conjectures in Section 7 \@vpageref []sec:conclusions, similar to the results from Emch, Jerrard, and Stromquist that a generic Jordan curve inscribes an odd number of squares. The most striking of these, to the author’s eyes at least, is the conjecture that an algebraic plane curve homeomorphic to the real line inscribes an even number of squares.

The outline of this thesis is as follows: In Section 2 \@vpageref []sec:background we recall some algebra, polytope theory, and algebraic geometry to support understanding of the statement of Bernshtein’s Theorem, Theorem 4.1. In Section 3 \@vpageref []sec:formulation we formulate the algebraic square peg problem; we parametrize a complex square in Definition 2 as a 4 4 -tuple ( a, b, c, d) (a,b,c,d) where ( a, b) (a,b) is the center of the square and the four corners are offset from the center by ( c, d) (c,d), ( − d, c) (-d,c), ( − c, − d) (-c,-d) and ( d, − c) (d,-c). Evaluating a polynomial f f at these four corners gives the four generators of the corner ideal that describes all squares inscribed on the algebraic plane curve defined by f f. Bernshtein’s Theorem provides an estimate on the number of isolated solutions to this system of four polynomials. While the immediate estimate is no better than Bézout’s bound, in Section 4 \@vpageref []sec:upper-bound we show that a different choice of generators yields Newton polytopes whose mixed volume gives exactly the bound ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 on the number of inscribed isolated squares. That this bound is tight, at least for low degrees, is exhibited by experimental data in section 5 \@vpageref []sec:experimental. In Section 6 \@vpageref []sec:illustrative we picture simple real algebraic plane curves of degrees three to eight inscribing varying numbers of squares. Finally we discuss some directions for future work in Section 7 \@vpageref []sec:conclusions.

## 2 Background

The square peg problem is inherently a geometric problem: Whether a curve inscribes a square depends on the lengths of and angles between line segments connecting pairs of points on the curve. Considering squares inscribed on algebraic curves allows us to view the square peg problem as an an algebraic problem as well. The gain of this approach is that we can use algebraic tools, such as Bernshtein’s Theorem, to make definite statements about the set of inscribed squares.

The main result of this thesis, Theorem 4.8, states that the number of isolated squares inscribed on an algebraic curve of degree m m is at most ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4. The proof of this result depends on Bernshtein’s Theorem, Theorem 4.1, which bounds the number of solutions to a polynomial system of equations by the mixed volume of the Newton polytopes of the generators of that polynomial system. The purpose of this background section is to present enough knowledge about these concepts such that readers who were not previously familiar with them can understand the statement of Bernshtein’s Theorem.

In Section 2.1 \@vpageref []sec:background-algebra we will recall some basic facts about polynomials and ideals of polynomial rings. The fact that each ideal is finitely generated is known as Hilbert’s Basis Theorem (Lemma 2.1).

We discuss convexity, polytopes, simplices, Minkowski sums, Schlegel diagrams, normal fans, Newton polytopes and the definition of the mixed volume in Section 2.2 \@vpageref []sec:background-polytopes.

In Section 2.3 \@vpageref []sec:background-varieties we mention the Nullstellensatz, which states that over an algebraically closed field, the radical of any ideal defining a variety is exactly the ideal of polynomials vanishing on that variety. We also show that varieties consist of a finite number of irreducible components (Lemma 2.7), and the fact that the saturation of an ideal I I with respect to an ideal J J corresponds to the difference in varieties of I I and J J (Lemma 2.8). These two results will be used in Section 4 \@vpageref []sec:upper-bound and Section 5 \@vpageref []sec:experimental to ensure that we are counting all the non-degenerate squares inscribed on an algebraic plane curve.

The algebra and results on varieties follow the expositions of Cox [4] and Eisenbud [6]. The polytope theory derives from Ziegler’s book on polytopes [27, Chapters 0, 1, 2, 5 and 7]. Definition 1 of the mixed volume is taken from Schneider’s book on convex bodies [23].

Readers familiar with these topics can safely skip this background section and proceed immediately to Section 3 \@vpageref []sec:formulation.

### 2.1 Algebra

Algebraic plane curves are a special case of geometric objects called varieties. Varieties are defined by the vanishing of a set of polynomials; in the case of plane curves these are polynomials in two variables. Before we discuss these algebraic geometric objects in Section 2.3 \@vpageref []sec:background-varieties, we define some basic notions concerning polynomials and their natural environments, polynomial rings.

Let x 1, …, x n x_{1},\dots,x_{n} be n n independent variables and α ∈ ℕ n \alpha\in\mathbb{N}^{n} a tuple of nonnegative integers. A *monomial*x α = x 1 α 1 ​ … ​ x n α n x^{\alpha}=x_{1}^{\alpha_{1}}\dots x_{n}^{\alpha_{n}} is a product of powers of the variables x i x_{i}. The degree of a monomial x α x^{\alpha} is the sum α 1 + ⋯ + α n \alpha_{1}+\dots+\alpha_{n} of the entries of its exponent. A *polynomial*over a field 𝕜 \mathds{k} in x 1, …, x n x_{1},\dots,x_{n} is a finite sum ∑ α ∈ ℕ n c α ​ x α \sum_{\alpha\in\mathbb{N}^{n}}c_{\alpha}x^{\alpha} of monomials where the coefficients c α c_{\alpha} are elements of the field 𝕜 \mathds{k}. The *total degree*(or simply degree) deg ⁡ f \deg f of a polynomial is the maximal degree of its monomials; the degree of 3 ​ x ​ y 2 − x ​ y 3xy^{2}-xy is three due to the exponent ( 1, 2) (1,2) of the monomial x ​ y 2 xy^{2}.

The collection of all polynomials in x 1, …, x n x_{1},\dots,x_{n} over 𝕜 \mathds{k}, denoted 𝕜 ⁡ [x 1, …, x n] \mathds{k}[x_{1},\dots,x_{n}], is called a *polynomial ring*. This terminology is justified, as multiplication and addition of polynomials equip 𝕜 ⁡ [x 1, …, x n] \mathds{k}[x_{1},\dots,x_{n}] with the structure of a ring. A *monomial ordering*< < on a polynomial ring is a binary relation with the following properties for any distinct exponents α, β ∈ ℕ n \alpha,\beta\in\mathbb{N}^{n},

1. 1.

either x α < x β x^{\alpha}<x^{\beta} or x β < x α x^{\beta}<x^{\alpha} (linear ordering)

2. 2.

x α < x β x^{\alpha}<x^{\beta} implies x α + γ < x β + γ x^{\alpha+\gamma}<x^{\beta+\gamma} for any γ ∈ ℕ n \gamma\in\mathbb{N}^{n}.

3. 3.

1 < x γ 1<x^{\gamma} for any nonzero γ ∈ ℕ n \gamma\in\mathbb{N}^{n} (well-ordering).

As usual with orderings we write x α ≤ x β x^{\alpha}\leq x^{\beta} if either x α = x β x^{\alpha}=x^{\beta} or x α < x β x^{\alpha}<x^{\beta}. The leading monomial 𝐋𝐌 < ​ ( f) \mathbf{LM}_{<}(f) of a polynomial f f compares greater than any other monomial of f f with respect to the ordering < <. The coefficient of the leading monomial is denoted 𝐋𝐂 < ​ ( f) \mathbf{LC}_{<}(f). The explicit dependence on the particular ordering < < is suppressed if no confusion is likely to arise. There is only one monomial ordering on univariate polynomials, x d < x e x^{d}<x^{e} if d < e d<e, but multivariate polynomials admit many different monomial orderings.

Certain subsets of 𝕜 ⁡ [x 1, …, x n] \mathds{k}[x_{1},\dots,x_{n}] hold special interest for us. A subset I ⊂ 𝕜 ⁡ [x 1, …, x n] I\subset\mathds{k}[x_{1},\dots,x_{n}] is called an *ideal*if it is closed under multiplication by elements of the polynomial ring and closed under addition by elements of I I. These conditions can be compactly stated with set-wise addition and multiplication notation, respectively 𝕜 ⁡ [x 1, …, x n] ​ I ⊂ I \mathds{k}[x_{1},\dots,x_{n}]I\subset I and I + I ⊂ I I+I\subset I.

The set { 0 } \{0\} is an ideal as 0 + 0 = 0 0+0=0 and f ⋅ 0 = 0 f\cdot 0=0 for any polynomial f ∈ 𝕜 ⁡ [x 1, …, x n] f\in\mathds{k}[x_{1},\dots,x_{n}]. The set { x, y } ⊂ 𝕜 ⁡ [x, y, z] \{x,y\}\subset\mathds{k}[x,y,z] on the other hand is not an ideal; neither x + y x+y nor x ​ z xz are contained in { x, y } \{x,y\}, so { x, y } \{x,y\} violates both closedness properties of an ideal. The set { x ​ f ∣ f ∈ 𝕜 ⁡ [x, y] } \{xf\mid f\in\mathds{k}[x,y]\} of “polynomial consequences of x x ” is again an ideal of 𝕜 ⁡ [x, y] \mathds{k}[x,y]; both the addition of elements x ​ g + x ​ g ′ = x ⁡ ( g + g ′) xg+xg^{\prime}=x(g+g^{\prime}) and the multiplication of an element x ​ g xg with an arbitrary polynomial g ′ g^{\prime} are of the form x ​ f xf required to be an element of the set.

Any ideal I I can be expressed as the consequence of an, a priori possibily infinite, set of generators B I B_{I} called a *basis*for I I,

 | I = ⟨ B I ⟩ = { ∑ i = 1 r h i g i ∣ r ∈ ℕ, g i ∈ B I, h i ∈ 𝕜 [x 1, …, x n] }. I=\langle B_{I}\rangle=\left\{\sum_{i=1}^{r}h_{i}g_{i}\mid r\in\mathbb{N},g_{i}\in B_{I},h_{i}\in\mathds{k}[x_{1},\dots,x_{n}]\right\}. |  |

The ideals { 0 } \{0\} and { x ​ f ∣ f ∈ 𝕜 ⁡ [x, y] } \{xf\mid f\in\mathds{k}[x,y]\} are generated by single polynomials, 0 0 and x x respectively. Bases are not unique, as the examples ⟨ x, y ⟩ = ⟨ x + y, x − y ⟩ \langle x,y\rangle=\langle x+y,x-y\rangle and ⟨ x, x ​ y, y ⟩ = ⟨ x, y ⟩ \langle x,xy,y\rangle=\langle x,y\rangle show. If I I has a finite, basis I I is *finitely generated*.

A ring with the property that every ideal is finitely generated is called *Noetherian*. It is easy to see that all fields are Noetherian; any ideal I ⊂ 𝕜 I\subset\mathds{k} other than ⟨ 0 ⟩ \langle 0\rangle contains some nonzero element u u. Since all nonzero elements of 𝕜 \mathds{k} are invertible and I I is closed under multiplication by field elements, r = r ​ u − 1 ​ u ∈ I r=ru^{-1}u\in I for all r ∈ 𝕜 r\in\mathds{k}. But then I I is the entire field itself, I = ⟨ 1 ⟩ I=\langle 1\rangle. As all ideals of a field are generated by a single element, any field is clearly Noetherian.

As a consequence of the next lemma, polynomial rings over a field are Noetherian as well.

###### Lemma 2.1 (Hilbert’s Basis Theorem [6, Theorem 1.2]).

Let R R be a Noetherian ring. Then R ⁡ [x] R[x] is Noetherian.

###### Proof.

Let I ⊂ R ⁡ [x] I\subset R[x] be an ideal. Select elements f i ∈ I f_{i}\in I as follows. If I = ⟨ f 1, …, f i ⟩ I=\langle f_{1},\dots,f_{i}\rangle, stop. Otherwise choose f i + 1 ∈ I ∖ ⟨ f 1, …, f i ⟩ f_{i+1}\in I\setminus\langle f_{1},\dots,f_{i}\rangle of minimal degree.

The leading coefficients of the f i f_{i} generate an ideal ⟨ 𝐋𝐂 ⁡ ( f 1), 𝐋𝐂 ⁡ ( f 2), … ⟩ \langle\mathbf{LC}(f_{1}),\mathbf{LC}(f_{2}),\dots\rangle of R R. This ideal is finitely generated since R R is Noetherian. Let m m be the smallest index such that the first m m leading coefficients generate the entire ideal of leading coefficients, ⟨ 𝐋𝐂 ⁡ ( f 1), …, 𝐋𝐂 ⁡ ( f m) ⟩ = ⟨ 𝐋𝐂 ⁡ ( f 1), … ⟩ \langle\mathbf{LC}(f_{1}),\dots,\mathbf{LC}(f_{m})\rangle=\langle\mathbf{LC}(f_{1}),\dots\rangle. We claim that our process must have stopped at f m f_{m}, that is, I = ⟨ f 1, …, f m ⟩ I=\langle f_{1},\dots,f_{m}\rangle.

Suppose we had picked an f m + 1 f_{m+1}. By assumption on m m the leading coefficient 𝐋𝐂 ⁡ ( f m + 1) \mathbf{LC}(f_{m+1}) can be expressed as a linear combination ∑ j = 1 m u j ​ 𝐋𝐂 ​ ( f j) \sum_{j=1}^{m}u_{j}\mathbf{LC}(f_{j}) of the earlier leading coefficients. The polynomial g = ∑ j = 1 m u j ​ f j ​ x deg ⁡ f m + 1 − deg ⁡ f j g=\sum_{j=1}^{m}u_{j}f_{j}x^{\deg f_{m+1}-\deg f_{j}} has the same degree and leading term as f m + 1 f_{m+1} by construction. Their difference, f m + 1 − g f_{m+1}-g, is of strictly smaller degree than f m + 1 f_{m+1}. By minimality of f m + 1 f_{m+1}, the difference f m + 1 − g f_{m+1}-g must be an element of ⟨ f 1, …, f m ⟩ \langle f_{1},\dots,f_{m}\rangle. As f m + 1 f_{m+1} is the sum of two elements of ⟨ f 1, …, f m ⟩ \langle f_{1},\dots,f_{m}\rangle, it must itself be an element of this ideal, which contradicts the choice of f m + 1 f_{m+1}. ∎

Hilbert’s Basis Theorem is stated for univariate polynomials with coefficients in a Noetherian ring; as we can rewrite a polynomial ∑ c γ ​ x 1 γ 1 ​ … ​ x n γ n \sum c_{\gamma}x_{1}^{\gamma_{1}}\dots x_{n}^{\gamma_{n}} as a sum ∑ i = 0 r ( ∑ γ n = i c γ ​ x γ 1 ​ … ​ x n − 1 γ n − 1) ​ x n i \sum_{i=0}^{r}(\sum_{\gamma_{n}=i}c_{\gamma}x^{\gamma_{1}}\dots x_{n-1}^{\gamma_{n-1}})x_{n}^{i} of monomials in x n x_{n} with coefficients in 𝕜 ⁡ [x 1, …, x n − 1] \mathds{k}[x_{1},\dots,x_{n-1}], the polynomial ring 𝕜 ⁡ [x 1, …, x n] = 𝕜 ⁡ [x 1, …, x n − 1] ​ [x n] \mathds{k}[x_{1},\dots,x_{n}]=\mathds{k}[x_{1},\dots,x_{n-1}][x_{n}] is Noetherian as well.

A sequence ( A 1, A 2, …) (A_{1},A_{2},\dots) of nested sets is called *ascending*if A i ⊂ A i + 1 A_{i}\subset A_{i+1} and *descending*if A i ⊃ A i + 1 A_{i}\supset A_{i+1}. Such a sequence terminates, or stabilizes, if the tail of the sequence is constant, that is, A n = A N A_{n}=A_{N} for some N ∈ ℕ N\in\mathbb{N} and all n ≥ N n\geq N. If every ascending chain of ideals of a ring R R terminates, R R is said to satisfy the *Ascending Chain Condition*(ACC). The Ascending Chain Condition on a ring and a ring being Noetherian are two different ways of looking at the same property.

###### Lemma 2.2.

The Ascending Chain Condition and being Noetherian are equivalent.

###### Proof.

Let R R be a Noetherian ring and let I 1 ⊂ I 2 ⊂ … I_{1}\subset I_{2}\subset\dots be an ascending chain of ideals. The union I = ∪ 1 ∞ I i I=\cup_{1}^{\infty}I_{i} is again an ideal, since f, g ∈ I f,g\in I implies that f, g ∈ I r f,g\in I_{r} for some r r large enough. By assumption I I is finitely generated, say I = ⟨ f 1, …, f m ⟩ I=\langle f_{1},\dots,f_{m}\rangle. The chain terminates at the smallest index j j such that f 1, …, f m ∈ I j f_{1},\dots,f_{m}\in I_{j}.

Assume that a ring R R has the Ascending Chain Condition and let I I be an ideal of R R. Pick f 1 ∈ I f_{1}\in I and f i + 1 ∈ I ∖ ⟨ f 1, …, f i ⟩ f_{i+1}\in I\setminus\langle f_{1},\dots,f_{i}\rangle. The ideals I i = ⟨ f 1, …, f i ⟩ I_{i}=\langle f_{1},\dots,f_{i}\rangle so constructed form an ascending chain. By the ACC the chain terminates, providing a finite set of generators for I I. ∎

In the sequel we separate non-degenerate squares from degenerate squares inscribed on a curve by taking the difference of varieties. The corresponding algebraic operation is called saturation, which is phrased in terms of colon ideals. Let I, J ⊂ 𝕜 ⁡ [x 1, …, x n] = R I,J\subset\mathds{k}[x_{1},\dots,x_{n}]=R be ideals. The *colon ideal*I: J I:J is the set { f ∈ R: f ​ J ⊂ I } \{f\in R:fJ\subset I\}. The colon ideal ⟨ x ​ y ⟩: ⟨ y ⟩ \langle xy\rangle:\langle y\rangle contains all polynomials f f such that f ​ y ∈ ⟨ x ​ y ⟩ fy\in\langle xy\rangle. It does not contain the polynomial 1 1, as y y is not an element of ⟨ x ​ y ⟩ \langle xy\rangle. It does contain x x, and it is not hard to show that ⟨ x ​ y ⟩: ⟨ y ⟩ = ⟨ x ⟩ \langle xy\rangle:\langle y\rangle=\langle x\rangle.

Recall that the notation J m J^{m} denotes the set of all products ∏ i = 1 m j i \prod_{i=1}^{m}j_{i} with m m factors from J J. The *saturation*I: J ∞ I:J^{\infty} of I I with respect to J J is the ideal ⋃ m = 0 ∞ I: J m \bigcup_{m=0}^{\infty}I:J^{m}. The colon ideals I: J m I:J^{m} form an ascending chain; as I I is an ideal and thus closed under multiplication by the ring, the condition f ​ J ⊂ I fJ\subset I implies that f ​ J 2 ⊂ I fJ^{2}\subset I. The ascending chain I ⊂ I: J ⊂ I: J 2 ⊂ … I\subset I:J\subset I:J^{2}\subset\dots terminates because polynomial rings are Noetherian, and thus the saturation I: J ∞ = I: J M I:J^{\infty}=I:J^{M} for some M ∈ ℕ M\in\mathbb{N}.

For multivariate polynomials it is often convenient to think about all the monomials of a certain degree separately. The monomials of a fixed degree form a basis for the vector space of all homogenenous polynomials of that degree. A general approach for grouping objects with the same properties together is to work with a grading. A *grading*of a ring R R is a decomposition of R R as a direct sum R 0 ⊕ R 1 ⊕ … R_{0}\oplus R_{1}\oplus\dots into abelian groups R i R_{i} with the property that R i ​ R j ⊂ R i + j R_{i}R_{j}\subset R_{i+j}. An element f ∈ R k f\in R_{k} is called a *homogeneous*element, or a *form*, of degree k k. A polynomial ring has a grading by total degree where the homogeneous polynomials of degree k k are sums of monomials of total degree k k. The homogeneous parts of a polynomial f f are homogeneous elements f i ∈ R i f_{i}\in R_{i} such that f 1 + ⋯ + f deg ⁡ f = f f_{1}+\dots+f_{\deg f}=f. The three homogeneous parts of f = 3 ​ x 3 ​ y 3 + x ​ y + 2 ​ x 2 + 1 f=3x^{3}y^{3}+xy+2x^{2}+1 are the forms 3 ​ x 3 ​ y 3 3x^{3}y^{3}, x ​ y + 2 ​ x 2 xy+2x^{2} and 1 1.

### 2.2 Polytopes

Bernshtein’s Theorem is stated in terms of polynomials, varieties, Newton polytopes and mixed volumes. We discussed polynomials in the previous section and will discuss varieties in the next section. The current section contains the definition of mixed volume and enough polytope theory to understand the statement of Bernshtein’s Theorem, as well as the proofs in Section 4 \@vpageref []sec:upper-bound.

Throughout this section V V denotes the ambient vector space containing the geometric objects of interest. Its dual space V ∗ V^{*} consists of all linear functionals α: V → 𝕜 \alpha\colon V\to\mathds{k}. The notation ⟨ α, v ⟩ \langle\alpha,v\rangle denotes the functional pairing ⟨ α, v ⟩ = α ⁡ ( v) \langle\alpha,v\rangle=\alpha(v) as well as the inner product on V V by identifying the functional α ∈ V ∗ \alpha\in V^{*} with a suitable vector α ∈ V \alpha\in V. As V V will always be finite-dimensional in this thesis, no confusion is likely to arise. The standard basis vectors e i e_{i} of V V are unit vectors whose i i -th coordinate is one. The standard basis vectors of the plane are e 1 = ( 1, 0) e_{1}=(1,0) and e 2 = ( 0, 1) e_{2}=(0,1).

Polytopes are a particular nice class of convex geometric objects. A set S S is *convex*if it contains all line segments between its constituent points. Equivalently, convexity of S S can be expressed as the property that S S contains all the convex combinations of its elements. A finite sum ∑ i = 1 r t i ​ s i \sum_{i=1}^{r}t_{i}s_{i} is a *convex combination*of elements s i s_{i} of S S if all the t i t_{i} are non-negative and sum to one. This leads us to the definition of the *convex hull*of S S, the set of all convex combinations of elements of S S,

 | conv S = { ∑ i = 1 r t i s i ∣ r ∈ ℕ, s i ∈ S, t i ≥ 0, ∑ 1 r t i = 1 }. \mathrm{conv}S=\left\{\sum_{i=1}^{r}t_{i}s_{i}\mid r\in\mathbb{N},s_{i}\in S,t_{i}\geq 0,\sum_{1}^{r}t_{i}=1\right\}. |  |

If we do not require that the t i t_{i} are non-negative, a finite sum ∑ i = 1 r t i ​ s i \sum_{i=1}^{r}t_{i}s_{i} such that the t i t_{i} sum to one is an *affine combination*of the elements s i s_{i}. The *affine hull*is defined analogously to the convex hull. The affine hull of a subset S S of V V is the smallest *affine*subspace of V V that contains S S. If the affine subspace contains the element 0 0 it is also a linear subspace of V V. If 0 0 is not contained in an affine subspace A A, then A A is the translation of some linear subspace of V V. The dimension of an affine subspace is the dimension of the linear subspace it is a translate of. Consider affine space a linear space where we have forgotten how to distinguish the zero element.

[image: Refer to caption] Figure 1: The teardrop is convex because it contains every line segment between two of its points. The crescent is not convex.

The line y = x + 1 y=x+1 is not a linear subspace of ℝ 2 \mathbb{R}^{2} since it does not contain the origin, but it is an affine subspace. For linear subspaces we are used to the concept of linear independence, affine subspaces have a similar concept of affine independence. A set { p 1, …, p r } ⊂ V \{p_{1},\dots,p_{r}\}\subset V of points is *affinely independent*if no p i p_{i} is contained in affine hull spanned by the other p j p_{j}. Linear independence implies affine independence, but not vice versa. The set { ( 1, 0), ( 0, 1), ( 1, 1) } \{(1,0),(0,1),(1,1)\} is affinely independent since a line through two of the points does not contain the third. The set { ( 1, 0), ( 0, 1), ( 1 / 2, 1 / 2) } \{(1,0),(0,1),(1/2,1/2)\} is affinely dependent as the three points are collinear. These affine hulls are depicted in Figure 2.

[image: Refer to caption] Figure 2: The affine hull of a pairs of points, or collinear points, is a line.

Points, edges, triangles, tetrahedra and their higher-dimensional generalizations have the property that their vertices are affinely independent; an n n -*simplex*is the convex hull of n + 1 n+1 affinely independent points. The convex hull of the origin and the n n standard basis vectors e i e_{i} of an n n -dimensional vector space is an n n -simplex. In one, two and three dimensions the volumes of such simplices are 1 1, 1 / 2 1/2 and 1 / 6 1/6. Volume is invariant under translation, so the volume of an n n -simplex with vertices v 0 v_{0}, v 1 v_{1}, …, v n v_{n} is the same as that of the n n -simplex with vertices 0 0, v 1 − v 0 v_{1}-v_{0}, …, v n − v 0 v_{n}-v_{0}. The matrix with colum vectors v i − v 0 v_{i}-v_{0} maps the vertices of conv ⁡ ( 0, e 1, …, e n) \mathrm{conv}(0,e_{1},\dots,e_{n}) to the vertices conv ⁡ ( 0, v 1 − v 0, …, v n − v 0) \mathrm{conv}(0,v_{1}-v_{0},\dots,v_{n}-v_{0}). The volume of the second simplex is proportional to the volume of the first simplex, as the determinant of a matrix can be interpreted as a scaling factor in volume. According to Stein [25], the volume of a general n n -simplex with vertices v 0 v_{0}, v 1 v_{1}, …, v n v_{n} is

 | 1 n! ​ | det ( v 1 − v 0 v 2 − v 0 … v n − v 0) |. \frac{1}{n!}\left|\det\begin{pmatrix}v_{1}-v_{0}&v_{2}-v_{0}&\dots&v_{n}-v_{0}\end{pmatrix}\right|. |  |

A *polytope*is the convex hull of a *finite*set of points, not necessarily affinely independent. Figure 3 \@vpageref []fig:(non)-polytopes depicts some examples and non-examples of polytopes.

→ convex hull \xrightarrow{\text{convex hull}} → convex hull \xrightarrow{\text{convex hull}} → convex hull \xrightarrow{\text{convex hull}} Figure 3: Subsets of the plane and their convex hulls. The disc is not a polytope, the other two convex hulls are polytopes.

The *Minkowski (or vector) sum*of two sets S S and T T is the set S + T = { s + t: s ∈ S, t ∈ T } S+T=\{s+t:s\in S,t\in T\} of sums of their elements. The Minkowski sum is a well-defined binary operation on the space of convex objects as well as the space of polytopes. Let S S and T T be two convex sets. The cartesian product S × T S\times T is again convex and the map ( s, t) ↦ s + t (s,t)\mapsto s+t is linear so in particular it preserves convex combinations. Assume furthermore that S S and T T are the convex hulls of finite sets of points { s 1, …, s p } \{s_{1},\dots,s_{p}\} and { t 1, …, t q } \{t_{1},\dots,t_{q}\}. An arbitrary point s + t = ∑ 1 p λ i ​ s i + ∑ 1 q μ j ​ s j s+t=\sum_{1}^{p}\lambda_{i}s_{i}+\sum_{1}^{q}\mu_{j}s_{j} is the convex combination ∑ i, j λ i ​ μ j ​ ( s i + t j) \sum_{i,j}\lambda_{i}\mu_{j}(s_{i}+t_{j}) so S + T S+T is the convex hull of the finite set { s 1, …, s p } + { t 1, …, t q } \{s_{1},\dots,s_{p}\}+\{t_{1},\dots,t_{q}\} and hence a polytope.

A different viewpoint defines a polytope as the bounded intersection of a finite number of halfspaces. The equivalence between these two viewpoints is a fundamental result in polytope theory, see Ziegler [27, Theorem 1.1]. Obtaining a vertex description from a halfspaces description and vice-versa is a hard problem in general. For the specific polytopes occurring in this thesis both descriptions are at hand.

A hyperplane H α, c = { x ∈ V: ⟨ α, x ⟩ = c } ⊂ V H_{\alpha,c}=\{x\in V:\langle\alpha,x\rangle=c\}\subset V is an affine subspace of codimension one with normal vector α \alpha. The closed halfspaces H α, c − = { x ∈ V: ⟨ α, x ⟩ ≤ c } H_{\alpha,c}^{-}=\{x\in V:\langle\alpha,x\rangle\leq c\} and H α, c + = { x ∈ V: ⟨ α, x ⟩ ≥ c } H_{\alpha,c}^{+}=\{x\in V:\langle\alpha,x\rangle\geq c\} contain all the points to one side of H α, c H_{\alpha,c} in addition to the hyperplane itself.

A hyperplane H H*supports*a convex set S S at the point v v if H H touches S S at the point v v and S S lies on one side of H H, that is, v ∈ H ∩ S v\in H\cap S and either S ⊂ H − S\subset H^{-} or S ⊂ H + S\subset H^{+}. It is allowed for S S to lie within H H, the line segment { ( x, y) ∣ x ≥ 0, y ≥ 0, x + y = 1 } \{(x,y)\mid x\geq 0,y\geq 0,x+y=1\} is supported by the hyperplane x + y = 1 x+y=1 at any of its points.

If H α, c H_{\alpha,c} supports S S and S ⊂ H α, c − S\subset H_{\alpha,c}^{-} then H α, c − H_{\alpha,c}^{-} is a supporting halfspace of S S with outward normal vector α \alpha. If the convex set S S is also closed, then for any x x outside of S S there is a unique point y ∈ S y\in S that is closest to x x. The hyperplane through y y that is perpendicular to the line segment between x x and y y supports S S at y y. This construction, depicted in Figure 4 \@vpageref []fig:supporting-halfspace, shows that for each point x x outside of S S there is a halfspace H − H^{-} that contains S S but not x x, and thus every nonempty closed convex set is the intersection of its supporting halfspaces [23, Corollary 1.3.5].

y y S S x x H H Figure 4: The supporting hyperplane H H separates the closed convex set S S from any point x x outside of S S.

Let P = H 1 − ∩ ⋯ ∩ H r − P=H_{1}^{-}\cap\dots\cap H_{r}^{-} be a polytope defined as the intersection of r r halfspaces, where r r is minimal. An intersection of P P with multiple halfplanes H i H_{i} yields a subset of P P called a *face*. A face of dimension i i is called an i i -face. Every polytope trivially has itself as a face. Faces that are strict subsets of the polytope are *proper*faces. Special terminology is used for 0 0 -faces (*vertices*), 1 1 -faces (*edges*) and the proper faces of largest dimension (*facets*). An n n -dimensional polytope is *simple*if all its vertices are contained in the minimum of n n facets. A three-dimensional cube is simple, since each vertex is contained in three facets, but a pyramid with a square base is not simple as the apex is contained in four facets.

There is a dual way of thinking of the faces of a polytope, for a functional α ∈ V ∗ \alpha\in V^{*} let M P ​ ( α) = max v ∈ P ⁡ ⟨ α, v ⟩ M_{P}(\alpha)=\max_{v\in P}\langle\alpha,v\rangle denote the maximum value that α \alpha attains on P P. The *maximizer*F P ​ ( α) F_{P}(\alpha) of P P with respect to α \alpha is the subset of P P where α \alpha attains the maximal value M P ​ ( α) M_{P}(\alpha),

 | F P ​ ( α) = { v ∈ P ∣ ⟨ α, v ⟩ = max w ∈ P ⁡ ⟨ α, w ⟩ }. F_{P}(\alpha)=\left\{v\in P\mid\langle\alpha,v\rangle=\max_{w\in P}\langle\alpha,w\rangle\right\}. |  |

One way to envision the maximizer of P P with respect to α \alpha is to picture sliding the halfplane perpendicular to α \alpha along its normal in the positive direction, see Figure 5 \@vpageref []fig:maximizer. As the hyperplane progresses along α \alpha there is a critical point where the intersection with P P becomes empty. The last non-empty intersection is the set F P ​ ( α) F_{P}(\alpha).

1 1 2 2 3 3 4 4 5 5 6 6 1 1 2 2 3 3 4 4 0 0 v v α \alpha P \displaystyle P Figure 5: The face v v of the triangle P P is the maxmizer F P ​ ( α) F_{P}(\alpha) of P P with respect to α \alpha.

###### Lemma 2.3.

The faces of a full-dimensional polytope P P are exactly the sets of maximizers { v ∈ P ∣ ⟨ v, α ⟩ = max w ∈ P ⁡ ⟨ w, α ⟩ } \{v\in P\mid\langle v,\alpha\rangle=\max_{w\in P}\langle w,\alpha\rangle\} where α \alpha ranges over all functionals on the ambient vector space containing the polytope.

###### Proof.

Let H 1, …, H r H_{1},\dots,H_{r} be a set of facet-defining hyperplanes of P P with outward normals n 1, …, n r n_{1},\dots,n_{r}. The polytope itself maximizes the zero functional. Facets are the maximizers with respect to their facet normals. Any lower dimensional faces are intersections of multiple facets.

Assume that the intersection H 1 ∩ ⋯ ∩ H n H_{1}\cap\dots\cap H_{n} is a face F F of P P. Then for α ∈ cone ⁡ { n 1, …, n r } = { ∑ t i ​ n i ∣ t i ≥ 0 } \alpha\in\mathrm{cone}\{n_{1},\dots,n_{r}\}=\{\sum t_{i}n_{i}\mid t_{i}\geq 0\} the face F F is a subset of the maximizer F P ​ ( α) F_{P}(\alpha). If one of the t i t_{i} is zero, the containment is strict, but if all t i t_{i} are positive then any point x x outside of any of the H i H_{i} is not an element of the maximizer F P ​ ( α) F_{P}(\alpha). Hence the face F F is equal to F P ​ ( α) F_{P}(\alpha). ∎

The *normal cone*of a face F F is the set of functionals { α ∈ V ∗ ∣ F P ​ ( α) = F } \{\alpha\in V^{*}\mid F_{P}(\alpha)=F\} that attain their maximal value precisely on F F. Identifying the functionals α ∈ V ∗ \alpha\in V^{*} with vectors α ∈ V \alpha\in V such that α ⁡ ( v) = ⟨ α, v ⟩ \alpha(v)=\langle\alpha,v\rangle for every v ∈ V v\in V, these normal cones can be thought of as geometric objects living in the same space as F F.

The *normal fan*of the polytope P P is the collection of the normal cones of all faces of P P; it partitions V ∗ V^{*} into cones, see Figure 6 \@vpageref []fig:normal-fan.

P P

Figure 6: The normal fan of P P partitions the plane into normal cones of all the faces of P P.

Scaling a polytope by a positive scalar does not change the normal fans, as is clear from the equality λ ​ P = { λ ​ x: A ​ x ≤ b } = { x: A ​ x ≤ λ ​ b } \lambda P=\{\lambda x:Ax\leq b\}=\{x:Ax\leq\lambda b\}.

Let P P be an n n -dimensional polytope. A *triangulation*S S of P P is a decomposition of P P into simplices of dimension n n with mutually disjoint interiors, Figure 7 \@vpageref []fig:polytope-triangulation shows triangulations for a square and a triangular prism.

[image: Refer to caption] Figure 7: Triangulations of a square and a triangular prism.

###### Lemma 2.4.

Let v v be a vertex of a polytope P P and for F F a facet of P P not containing v v let S F S_{F} be a triangulation of F F. Then the union

 | ⋃ F { conv ⁡ ( v, S) ∣ S ∈ S F } \bigcup_{F}\{\mathrm{conv}(v,S)\mid S\in S_{F}\} |  |

of the convex hulls of v v with each simplex in a triangulation of a face of F F not containing v v, is a triangulation of P P.

###### Proof.

Let x ∈ P x\in P be distinct from v v. The ray from v v to x x exits P P in some face F F not containing v v and thus intersects some simplex σ ∈ S F \sigma\in S_{F}. The convex hull conv ⁡ ( v, σ) \mathrm{conv}(v,\sigma) of v v and σ \sigma contains x x by convexity. As v v is affinely independent from σ \sigma, the simplex conv ⁡ ( v, σ) \mathrm{conv}(v,\sigma) is full-dimensional.

Suppose the ray through x x intersects two distinct simplices σ \sigma and τ \tau. Then x x is contained in conv ⁡ ( v, σ ∩ τ) \mathrm{conv}(v,\sigma\cap\tau). Since σ \sigma and τ \tau share no interior points, the dimension of the intersection σ ∩ τ \sigma\cap\tau is at most n − 2 n-2. The dimension of conv ⁡ ( v, σ ∩ τ) \mathrm{conv}(v,\sigma\cap\tau) is then at most n − 1 n-1, so conv ⁡ ( v, σ) \mathrm{conv}(v,\sigma) and conv ⁡ ( v, τ) \mathrm{conv}(v,\tau) have disjoint interiors. ∎

Lemma 2.4 suggests an algorithm for triangulating a polytope. Starting out with a pair ( P, v) (P,v), recursively triangulate the facets of P P not containing v v to obtain the triangulations S F S_{F}. This algorithm is known as the Cohen & Hickey algorithm [2, Section 3.1] and will be used in Corollary 4.7 to calculate the volume of a Minkowski sum.

So far we have pictured polytopes of dimension zero, one, two and three. The polytopes playing a main role in this thesis are four-dimensional. One way to visualize four-dimensional polytopes is by using Schlegel diagrams. The idea is to project a polytope onto one of its facets, see Figure 8 \@vpageref []fig:schlegel-projection.

[image: Refer to caption] Figure 8: A Schlegel diagram of a polytope P P is obtained by projecting P P onto a facet F F using the projection p y p_{y}.

Let y y lie beyond a facet F F of a polytope P P. The projection p y ​ ( x) p_{y}(x) of x ∈ P x\in P onto F F is the intersection of the line segment between x x and y y with F F. The *Schlegel diagram*𝒟 ⁡ ( P, F) \mathcal{D}(P,F) of P P based at the facet F F is the image of all the proper faces of P P, other than F F, under the projection map p p. Its usefulness comes from the fact [27, Proposition 5.6] that although 𝒟 ⁡ ( P, F) \mathcal{D}(P,F) is of smaller dimension than the original polytope, the combinatorial structures of P P and the Schlegel diagram are equivalent. This allows one to read off the face structure of a four-dimensional polytope from a three-dimensional picture. The Schlegel diagrams in this thesis are Figure 16 \@vpageref []fig:schlegel1 and Figure 17 \@vpageref []fig:schlegel2.

The concept of mixed volume was introduced by Minkowski in the early 1900s. For our purposes the mixed volume serves only as a computational tool. In the literature various definitions of the mixed volume abound. The following definition as used by Schneider [23], Bernshtein [1] and Huber and Sturmfels [12] is convenient for root counting.

###### Definition 1 (Mixed volume [23, Theorem 5.1.6]).

Let P 1, …, P n ⊂ ℝ n P_{1},\dots,P_{n}\subset\mathbb{R}^{n} be n n polytopes. Their *mixed volume*M ​ V ​ ( P 1, …, P n) MV(P_{1},\dots,P_{n}) is the coefficient of the monomial λ 1 ​ … ​ λ n \lambda_{1}\dots\lambda_{n} appearing in the expression for the n n -dimensional Euclidean volume Vol n ​ ( λ 1 ​ P 1 + ⋯ + λ n ​ P n) \mathrm{Vol}_{n}(\lambda_{1}P_{1}+\dots+\lambda_{n}P_{n}) of the Minkowski sum of the P i P_{i} scaled by factors λ i \lambda_{i}.

The process of calculating the mixed volume of two rectangles is depicted in Figure 9 \@vpageref []fig:mixed-volume.

[image: Refer to caption] Figure 9: The mixed volume M ​ V ​ ( P 1, P 2) MV(P_{1},P_{2}) of the polytopes P 1 P_{1} and P 2 P_{2} is the coefficient of λ 1 ​ λ 2 \lambda_{1}\lambda_{2} in the expression λ 1 2 ​ Vol ​ ( P 1) + λ 2 2 ​ Vol 2 ​ ( P 2) + λ 1 ​ λ 2 ​ ( a 1 ​ b 2 + a 2 ​ b 1) \lambda_{1}^{2}\mathrm{Vol}(P_{1})+\lambda_{2}^{2}\mathrm{Vol}_{2}(P_{2})+\lambda_{1}\lambda_{2}(a_{1}b_{2}+a_{2}b_{1}) for the volume of the Minkowski sum P 1 + P 2 P_{1}+P_{2}.

Before we move on to varieties, the last polytopal concept occuring in the statement of Bernshtein’s Theorem is the concept of a Newton polytope. Let f = ∑ γ c γ ​ x γ ∈ 𝕜 ⁡ [x 1, …, x n] f=\sum_{\gamma}c_{\gamma}x^{\gamma}\in\mathds{k}[x_{1},\dots,x_{n}] be a polynomial. The *Newton polytope*𝒩 ⁡ ( f) \mathcal{N}(f) of f f is the convex hull of the exponents of the monomials of f f, 𝒩 ⁡ ( f) = conv ⁡ { γ ∈ ℕ n ∣ c γ ≠ 0 } \mathcal{N}(f)=\mathrm{conv}\{\gamma\in\mathbb{N}^{n}\mid c_{\gamma}\neq 0\}.

###### Example 2.5.

The Newton polytopes of λ 00 + λ 10 ​ x + λ 12 ​ x ​ y 2 \lambda_{00}+\lambda_{10}x+\lambda_{12}xy^{2} and μ 10 ​ x + μ 30 ​ x 3 + μ 01 ​ y + μ 03 ​ y 3 + μ 11 ​ x ​ y \mu_{10}x+\mu_{30}x^{3}+\mu_{01}y+\mu_{03}y^{3}+\mu_{11}xy are depicted in Figure 10 \@vpageref []fig:newton-polytopes. The points ( i, j) (i,j) in the Newton polytopes that are an exponent of a monomial x i ​ y j x^{i}y^{j} are labeled with the corresponding term.

[image: Refer to caption]

[image: Refer to caption]

Figure 10: Newton polytopes of the polynomials λ 00 + λ 10 ​ x + λ 12 ​ x ​ y 2 \lambda_{00}+\lambda_{10}x+\lambda_{12}xy^{2} and μ 10 ​ x + μ 30 ​ x 3 + μ 01 ​ y + μ 03 ​ y 3 + μ 11 ​ x ​ y \mu_{10}x+\mu_{30}x^{3}+\mu_{01}y+\mu_{03}y^{3}+\mu_{11}xy.

### 2.3 Varieties

An algebraic curve and the set of squares inscribed on such a curve are both examples of varieties. Varieties are geometric objects we can describe well by ideals of polynomials vanishing on the variety. This connection enables the use of algebraic tools from the Algebra background section to answer questions of geometry. The Ascending Chain Condition allows us to show that varieties consist of a finite number of irreducible components; the difference of varieties defined by ideals I I and J J corresponds to the variety defined by the saturation I: J ∞ I:J^{\infty}.

Algebraic geometry is pursued over any field, be it finite or infinite, a subfield of ℂ \mathbb{C} or something more exotic. The concrete fields used in the applications in this thesis are the rationals ℚ \mathbb{Q}, the reals ℝ \mathbb{R} and the complex numbers ℂ \mathbb{C}. All of them are infinite fields, which makes some reasoning easier. The complex numbers additionally have the property that they are *algebraically closed*, any nonconstant polynomial with complex coefficients has a complex root. Many proofs that work for the complex numbers, such as the Strong Nullstellensatz, only depend on the fact that the field of complex numbers is algebraically closed. We shall state such results for an arbitrary algebraically closed field.

Let f 1, …, f r ∈ 𝕜 ⁡ [x 1, …, x n] f_{1},\dots,f_{r}\in\mathds{k}[x_{1},\dots,x_{n}] be a set of polynomials. The set of points ( x 1, …, x n) (x_{1},\dots,x_{n}) ∈ 𝕜 n \in\mathds{k}^{n} simultaneously satisfying the system of equations

 | f 1 ​ ( x 1, …, x n) = 0, …, f r ​ ( x 1, …, x n) = 0, f_{1}(x_{1},\dots,x_{n})=0,\dots,f_{r}(x_{1},\dots,x_{n})=0, |  |

is called the *variety*defined by { f 1, …, f r } \{f_{1},\dots,f_{r}\}, denoted 𝐕 ⁡ ( f 1, …, f r) \mathbf{V}(f_{1},\dots,f_{r}). Linear and affine subspaces are familiar examples, both defined by collections of linear polynomials. Conics, finite sets of points, and graphs y = f ⁡ ( x 1, …, x n) y=f(x_{1},\dots,x_{n}) of polynomials are other examples the reader may have seen before. Some varieties and non-varieties are depicted in Figure 11 \@vpageref []fig:non-varieties. An algebraic plane curve is a variety defined by the vanishing of a single polynomial in two variables. The line through the origin with slope one is an algebraic curve defined by the vanishing of the polynomial x − y x-y. The unit circle is defined by the vanishing of the polynomial x 2 + y 2 − 1 x^{2}+y^{2}-1.

The smallest variety V V that contains a set S S is called the *Zariski closure*S ¯ \overline{S} of S S. The Zariski closure of a point is just the point, as it is already a variety. The Zariski closure of the integers is all of ℝ \mathbb{R}, as any polynomial that vanishes on all integers will vanish on all real numbers.

[image: Refer to caption] (a) 𝐕 ⁡ ( y 4 − x 2) \mathbf{V}(\frac{y}{4}-x^{2})

[image: Refer to caption] (b) The positive half-line

[image: Refer to caption] (c) 𝐕 ⁡ ( y, x 2 − 1) \mathbf{V}(y,x^{2}-1)

[image: Refer to caption] (d) A square

[image: Refer to caption] (e) 𝐕 ⁡ ( x + y) \mathbf{V}(x+y)

[image: Refer to caption] (f) The sequence ( 1 n) n = 1 ∞ \left(\frac{1}{n}\right)_{n=1}^{\infty}.

Figure 11: Three varieties on the left and three non-varieties on the right.

The polynomials f 1, …, f r f_{1},\dots,f_{r} have the property that they vanish on the variety 𝐕 ⁡ ( f 1, …, f r) \mathbf{V}(f_{1},\dots,f_{r}) by construction. The collection 𝐈 ⁡ ( V) \mathbf{I}(V) of all polynomials vanishing on a variety V V is called the *ideal of V V*. One checks that 𝐈 ⁡ ( V) \mathbf{I}(V) indeed has the structure of an ideal as defined in Section 2.1 \@vpageref []sec:background-algebra. Any 𝕜 ⁡ [x 1, …, x n] \mathds{k}[x_{1},\dots,x_{n}] -linear combination of f 1, …, f r f_{1},\dots,f_{r} vanishes on 𝐕 ⁡ ( f 1, …, f r) \mathbf{V}(f_{1},\dots,f_{r}) so we see that ⟨ f 1, …, f r ⟩ ⊂ 𝐈 ⁡ ( 𝐕 ⁡ ( f 1, …, f r)) \langle f_{1},\dots,f_{r}\rangle\subset\mathbf{I}(\mathbf{V}(f_{1},\dots,f_{r})). That the containment can be strict is illustrated by the ideal ⟨ x 2 ⟩ ⊂ 𝕜 ⁡ [x] \langle x^{2}\rangle\subset\mathds{k}[x]; the only point where x 2 x^{2} is zero is the origin, so 𝐕 ⁡ ( x 2) = { 0 } \mathbf{V}(x^{2})=\{0\}. The two monomials of 𝕜 ⁡ [x] \mathds{k}[x] not contained in ⟨ x 2 ⟩ \langle x^{2}\rangle are x x and 1 1. The constant monomial 1 1 does not vanish anywhere, but x x also vanishes at the origin, so 𝐈 ⁡ ( { 0 }) = ⟨ x ⟩ \mathbf{I}(\{0\})=\langle x\rangle. There is another relation between the previous two ideals: ⟨ x ⟩ \langle x\rangle is the radical of ⟨ x 2 ⟩ \langle x^{2}\rangle. The *radical*I \sqrt{I} of an ideal I I is the ideal { f ∣ f m ∈ I, m ∈ ℕ } \{f\mid f^{m}\in I,m\in\mathbb{N}\} of all polynomials that occur in I I to some non-negative power. It is always true that I ⊂ 𝐈 ⁡ ( 𝐕 ⁡ ( I)) \sqrt{I}\subset\mathbf{I}(\mathbf{V}(I)), but when 𝕜 \mathds{k} is not algebraically closed equality is not guaranteed. If 𝕜 \mathds{k} is algebraically closed, it *is*true that the radical of an ideal I I contains all polynomials that vanish on 𝐕 ⁡ ( I) \mathbf{V}(I).

###### Theorem 2.6 (Strong Nullstellensatz [4, Theorem 4.2.6]).

Let 𝕜 \mathds{k} be an algebraically closed field. If I I is an ideal in 𝕜 ⁡ [x 1, …, x n] \mathds{k}[x_{1},\dots,x_{n}] then

 | 𝐈 ⁡ ( 𝐕 ⁡ ( I)) = I. \mathbf{I}(\mathbf{V}(I))=\sqrt{I}. |  |

As a result there is a one-to-one correspondence between radical ideals and varieties, the maps 𝐕: radical ideals → varieties \mathbf{V}\colon\text{radical ideals}\to\text{varieties} and 𝐈: varieties → radical ideals \mathbf{I}\colon\text{varieties}\to\text{radical ideals} are inclusion-reversing inverses to each other.

The Nullstellensatz is one reason to pass to ℂ \mathbb{C} rather than working over ℝ \mathbb{R}; when we start out with an ideal I I it may be hard to determine the ideal 𝐈 ⁡ ( 𝐕 ⁡ ( I)) \mathbf{I}(\mathbf{V}(I)) of polynomials vanishing on the variety 𝐕 ⁡ ( I) \mathbf{V}(I) defined by I I. Knowing that all such polynomials lie in the radical I \sqrt{I} can make proofs easier, as happens in the proof of Lemma 2.8 that 𝐕 ⁡ ( I: J ∞) = 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) ¯ \mathbf{V}(I:J^{\infty})=\overline{\mathbf{V}(I)\setminus\mathbf{V}(J)}. Another benefit is that there are algorithms available to compute the radical of an ideal.

[image: Refer to caption] Figure 12: The variety 𝐕 ⁡ ( x ​ z, y ​ z) \mathbf{V}(xz,yz) consists of two irreducible components.

Some varieties are simpler than others. Let f f and g g define two distinct varieties 𝐕 ⁡ ( f) \mathbf{V}(f) and 𝐕 ⁡ ( g) \mathbf{V}(g). As the product f ​ g fg vanishes there where at least one of the polynomials f f or g g vanish, the variety 𝐕 ⁡ ( f ​ g) \mathbf{V}(fg) is the union of the two subvarieties 𝐕 ⁡ ( f) \mathbf{V}(f) and 𝐕 ⁡ ( g) \mathbf{V}(g).

Whenever a variety V V admits a decomposition V = W ∪ Z V=W\cup Z into two proper subvarieties, V V is said to be reducible. Otherwise V V is *irreducible*. The reducible variety 𝐕 ⁡ ( x ​ z, y ​ z) ⊂ 𝕜 3 \mathbf{V}(xz,yz)\subset\mathds{k}^{3}, depicted in Figure 12 \@vpageref []fig:plane-and-axis, is the union of two irreducible components: the z z -axis and the x ​ y xy -planes.

As each point is itself a variety, any non-finite variety has an infinite amount of subvarieties. However, we can decompose a variety into a finite number of irreducible components. The following proof is a mixture of several results from Cox [4, Section 4.6]. It can be cast in the theory of primary decompositions, see Eisenbud [6, Theorem 3.1a]) for a more comprehensive treatment.

###### Lemma 2.7.

Any variety V ⊂ 𝕜 n V\subset\mathds{k}^{n} can be written as a finite union V = V 1 ∪ ⋯ ∪ V r V=V_{1}\cup\dots\cup V_{r} of irreducible components such that V i ⊄ V j V_{i}\not\subset V_{j} for any pair i i and j j.

###### Proof.

Suppose V V can not be written as a finite union of irreducible varieties. In particular V V is reducible, so there exist distinct proper subvarieties Z 1 Z_{1} and W 1 W_{1} such that V = Z 1 ∪ W 1 V=Z_{1}\cup W_{1}. We can assume that Z 1 Z_{1} can not be written as a finite union of irreducible varieties either, so then Z 1 = Z 2 ∪ W 2 Z_{1}=Z_{2}\cup W_{2} is reducible. Repeating this process we get a chain V ⊋ Z 1 ⊋ Z 2 ⊋ … V\supsetneq Z_{1}\supsetneq Z_{2}\supsetneq\dots of strictly decreasing varieties. By passing to the ideals of these varieties we get an increasing chain of ideals 𝐈 ⁡ ( V) ⊂ 𝐈 ⁡ ( Z 1) ⊂ 𝐈 ⁡ ( Z 2) ⊂ … \mathbf{I}(V)\subset\mathbf{I}(Z_{1})\subset\mathbf{I}(Z_{2})\subset\dots, as all polynomials that vanish on Z i Z_{i} certainly vanish on Z i + 1 Z_{i+1}. As 𝕜 ⁡ [x 1, …, x n] \mathds{k}[x_{1},\dots,x_{n}] is Noetherian, these ideals stabilize, and since 𝐕 ⁡ ( 𝐈 ⁡ ( Z i)) = Z i \mathbf{V}(\mathbf{I}(Z_{i}))=Z_{i} we observe that the chain V ⊃ Z 1 ⊃ Z 2 ⊃ … V\supset Z_{1}\supset Z_{2}\supset\dots stabilizes as well. This contradicts the assumption that V V can not be written as a finite union of irreducible varieties.

We conlude that V V is a finite union V = V 1 ∪ ⋯ ∪ V r V=V_{1}\cup\dots\cup V_{r} of irreducible subvarieties. If V i ⊂ V j V_{i}\subset V_{j} we can drop V i V_{i} from the union, proving the statement of the lemma. ∎

The difference of two varieties in general is no longer a variety. Consider the case of a line L L in the plane and a point p p contained in L L. Suppose a polynomial f f vanishes on L ∖ { p } L\setminus\{p\}, the restriction of f f to L L defines a univariate polynomial with an infinite amount of zeros. By the fundamental theorem of algebra a nonzero polynomial of degree m m has at most m m roots, so the restriction of f f to L L must be the zero polynomial. But then it also vanishes on p p, so the smallest variety containing L ∖ { p } L\setminus\{p\} is L L.

There is a relation between the smallest variety that contains the difference of two varieties defined by ideals I I and J J, and the variety of the colon ideal I: J I:J. Over any field it is true that 𝐕 ⁡ ( I: J) ⊃ 𝐕 ⁡ ( I) ∖ V ⁡ ( J) ¯ \mathbf{V}(I:J)\supset\overline{\mathbf{V}(I)\setminus V(J)}. Equality holds if in addition the field is algebraically closed and I I is radical [4, Theorem 4.4.7]. If 𝕜 \mathds{k} is algebraically closed but we can not guarantee that I I is radical, the following lemma shows we can instead pass to the saturation I: J ∞ I:J^{\infty}.

###### Lemma 2.8.

Let 𝕜 \mathds{k} be an algebraically closed field and let I, J ⊂ 𝕜 ⁡ [x 1, …, x n] I,J\subset\mathds{k}[x_{1},\dots,x_{n}] be ideals. Then

 | 𝐕 ⁡ ( I: J ∞) = 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) ¯. \mathbf{V}(I:J^{\infty})=\overline{\mathbf{V}(I)\setminus\mathbf{V}(J)}. |  |

###### Proof.

Let f ∈ I: J ∞ f\in I:J^{\infty}, that is, for every j ∈ J j\in J the product f ​ j k fj^{k} is an element of I I, for some k ∈ ℕ k\in\mathbb{N}. Since for every x ∈ 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) x\in\mathbf{V}(I)\setminus\mathbf{V}(J) there is a j ∈ J j\in J that is nonzero at x x, the condition f ​ j k ∈ I fj^{k}\in I implies that f ⁡ ( x) = 0 f(x)=0, as 𝐕 ⁡ ( I) \mathbf{V}(I) is per definition the set of points where *all*elements of I I vanish. Thus every element of I: J ∞ I:J^{\infty} vanishes on 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) \mathbf{V}(I)\setminus\mathbf{V}(J). Since 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) ¯ \overline{\mathbf{V}(I)\setminus\mathbf{V}(J)} is the smallest variety containing 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) \mathbf{V}(I)\setminus\mathbf{V}(J), we have shown the inclusion 𝐕 ⁡ ( I: J ∞) ⊃ 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) ¯ \mathbf{V}(I:J^{\infty})\supset\overline{\mathbf{V}(I)\setminus\mathbf{V}(J)}.

For the reverse inclusion, let f ∈ 𝐈 ⁡ ( 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J)) f\in\mathbf{I}(\mathbf{V}(I)\setminus\mathbf{V}(J)). For any j ∈ J j\in J the product f ​ j fj vanishes on the entirety of 𝐕 ⁡ ( I) \mathbf{V}(I) as j j vanishes on 𝐕 ⁡ ( J) \mathbf{V}(J) and f f vanishes on the complement of 𝐕 ⁡ ( J) \mathbf{V}(J) in 𝐕 ⁡ ( I) \mathbf{V}(I). Since we assumed that 𝕜 \mathds{k} is algebraically closed, it follows that f ​ j ∈ I fj\in\sqrt{I} and thus ( f ​ j) k ∈ I (fj)^{k}\in I for some integer k k. If f k ​ j k ∈ I f^{k}j^{k}\in I for all j j we can conclude that f k ∈ I: J ∞ f^{k}\in I:J^{\infty}. We will use the fact that J J is finitely generated to argue that there is indeed an integer k k such that f k ​ j k ∈ I f^{k}j^{k}\in I for all j ∈ J j\in J.

Let j 1, …, j s j_{1},\dots,j_{s} be a finite set of generators for J J. By the reasoning in the previous paragraph, ( f ​ j i) k i ∈ I (fj_{i})^{k_{i}}\in I for some k i ∈ ℕ k_{i}\in\mathbb{N}. Let k k be the minimal integer such that ( f ​ j i) k ∈ I (fj_{i})^{k}\in I for all i ∈ { 1, …, s } i\in\{1,\dots,s\}. Let j = ∑ i = 1 s h i ​ j i j=\sum_{i=1}^{s}h_{i}j_{i} be an arbitrary element of J J, then

 | ( f ​ j) k ​ s = ∑ | α | = k ​ s g α ​ f k ​ s ​ j 1 α 1 ​ … ​ j s α s, (fj)^{ks}=\sum_{|\alpha|=ks}g_{\alpha}f^{ks}j_{1}^{\alpha_{1}}\dots j_{s}^{\alpha_{s}}, |  |

where the g α g_{\alpha} are products of the h i h_{i} and multinomial coefficients. For each term g α ​ f k ​ s ​ j 1 α 1 ​ … ​ j s α s g_{\alpha}f^{ks}j_{1}^{\alpha_{1}}\dots j_{s}^{\alpha_{s}} at least one of the α i ≥ k \alpha_{i}\geq k, otherwise | α | < k ​ s |\alpha|<ks. As f k ​ s ​ j 1 α 1 ​ … ​ j s α s f^{ks}j_{1}^{\alpha_{1}}\dots j_{s}^{\alpha_{s}} is a multiple of f k ​ j i α i f^{k}j_{i}^{\alpha_{i}}, which is an element of I I by construction, the product ( f ​ j) k ​ s (fj)^{ks} is a sum of elements of I I and thus an element of I I itself.

Thus f k ​ s ∈ I: J ∞ f^{ks}\in I:J^{\infty} as j j was arbitrary. We have shown that every polynomial f f that vanishes on 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) \mathbf{V}(I)\setminus\mathbf{V}(J) is present to some power in I: J ∞ I:J^{\infty}, thus the radical I: J ∞ \sqrt{I:J^{\infty}} contains 𝐈 ⁡ ( 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J)) \mathbf{I}(\mathbf{V}(I)\setminus\mathbf{V}(J)) and we get the reverse inclusion 𝐕 ⁡ ( I: J ∞) ⊂ 𝐕 ⁡ ( I) ∖ 𝐕 ⁡ ( J) ¯ \mathbf{V}(I:J^{\infty})\subset\overline{\mathbf{V}(I)\setminus\mathbf{V}(J)}. ∎

A formal definition of dimension of a variety requires some work, see Chapter 9 “The Dimension of a Variety” of Cox [4]. For this thesis our intuition that points, curves and surfaces are respectively of dimensions zero, one and two will suffice to reason about dimensionality. Experimental computations of dimensions will rely on the dim command provided by Macaulay2.

## 3 Problem formulation

Toeplitz’s conjecture asks whether every Jordan curve inscribes a square. This existence question has eluded a complete answer for over a hundred years; the class of continuous curves contains rather pathological specimens.

In the algebraic square peg problem we consider algebraic plane curves rather than Jordan curves; what can we say about the set of squares inscribed on an algebraic plane curve? A straight line does not inscribe any squares, whereas a circle inscribes an uncountable amount of squares. In this thesis our aim is to count the number of inscribed squares that do not come in infinite families, a circle inscribes zero “finite” squares.

With a suitable concept of a square, the set of inscribed squares has the structure of a variety. We will see in Section 4 \@vpageref []sec:upper-bound that we can use Bernshtein’s Theorem to bound the size of the finite part of this variety. Before we state how many squares one can maximally inscribe, let us consider the variety of inscribed squares in some more detail. The first issue we should address is settling on a notion of a square that is compatible with our algebraic worldview. Figure 13 \@vpageref []fig:square-param is the picture to keep in mind.

Let f ∈ ℝ ⁡ [x, y] f\in\mathbb{R}[x,y] define an algebraic plane curve 𝐕 ℝ ​ ( f) = { ( x, y) ∈ ℝ 2 ∣ f ⁡ ( x, y) = 0 } \mathbf{V}_{\mathbb{R}}(f)=\{(x,y)\in\mathbb{R}^{2}\mid f(x,y)=0\}. If we parametrize a square by a center ( a, b) (a,b) and an offset ( c, d) (c,d) to a distinguished corner, then the variety 𝐕 ℝ ​ ( f ⁡ ( a + c, b + d), f ⁡ ( a − c, b − d), f ⁡ ( a + d, b − c), f ⁡ ( a − d, b + d)) ⊂ ℝ 4 \mathbf{V}_{\mathbb{R}}(f(a+c,b+d),f(a-c,b-d),f(a+d,b-c),f(a-d,b+d))\subset\mathbb{R}^{4} captures all the squares inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f). We consider this variety as the real part of a complex variety defined by the same algebraic relations. These relations motivate our definition of a complex square.

###### Definition 2 (Parametrization of a complex square).

A 4 4 -tuple ( a, b, c, d) ∈ ℂ 4 (a,b,c,d)\in\mathbb{C}^{4} parametrizes a *complex square*with center ( a, b) (a,b) and corners ( a + c, b + d), ( a + d, b − c), ( a − c, b − d), ( a − d, b + c) (a+c,b+d),(a+d,b-c),(a-c,b-d),(a-d,b+c), depicted in Figure 13 \@vpageref []fig:square-param. As there are four choices of ( c, d) (c,d) corresponding to distinguishing a particular corner, there is a four-to-one correspondence between 4 4 -tuples and complex squares with distinct corners.

[image: Refer to caption] Figure 13: Center ( a, b) (a,b) and offset ( c, d) (c,d) to a distinguished corner ( a + c, b + d) (a+c,b+d) parametrize a complex square.

When constrained to ℝ 2 ⊂ ℂ 2 \mathbb{R}^{2}\subset\mathbb{C}^{2} this definition reduces to the familiar definition of a square: the diagonals are two perpendicular line segments of equal length intersecting each other in their midpoints. The four corners of a square are distinct as long as ( c, d) ≠ ( 0, 0) (c,d)\neq(0,0). If ( c, d) = ( 0, 0) (c,d)=(0,0) the resulting square is *degenerate*, it has collapsed to a single point. We combine the definition of a complex square with a polynomial definining a plane curve to investigate the set of squares inscribed on that curve.

Let f ∈ ℂ ⁡ [x, y] f\in\mathbb{C}[x,y] define an algebraic plane curve 𝐕 ⁡ ( f) ⊂ ℂ 2 \mathbf{V}(f)\subset\mathbb{C}^{2}. The *corner ideal*I f I_{f} of f f is the ideal generated by the four polynomials that result from evaluating f f at the four corners of a complex square,

 | I f = ⟨ f ⁡ ( a + c, b + d), f ⁡ ( a + d, b − c), f ⁡ ( a − c, b − d), f ⁡ ( a − d, b + c) ⟩ ⊂ ℂ ⁡ [a, b, c, d]. I_{f}=\langle f(a+c,b+d),f(a+d,b-c),f(a-c,b-d),f(a-d,b+c)\rangle\subset\mathbb{C}[a,b,c,d]. |  |

The variety 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) encodes all the squares inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f), both degenerate and non-degenerate squares. All of the degenerate squares are contained in the part of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) where the c c and d d coordinates are both zero. There is one degenerate square ( a, b, 0, 0) ∈ 𝐕 ⁡ ( I f) (a,b,0,0)\in\mathbf{V}(I_{f}) for every point ( a, b) ∈ 𝐕 ⁡ ( f) (a,b)\in\mathbf{V}(f). Thus we identify the degenerate squares 𝐕 ( I f) ∩ { c = d = 0 } \mathbf{V}(I_{f})\cap\{c=d=0\} with the original plane curve 𝐕 ⁡ ( f) \mathbf{V}(f). In the complement 𝐕 ⁡ ( I f) ∖ 𝐕 ⁡ ( f) \mathbf{V}(I_{f})\setminus\mathbf{V}(f) all squares are non-degenerate.

There might be positive-dimensional components of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) other than the one containing 𝐕 ⁡ ( f) \mathbf{V}(f); consider a plane curve consisting of two parallel lines. The non-degenerate squares inscribed on such a curve have two vertices on each component of the curve and are centered on a third line parallel to these two components. The sidelengths of the squares equal the distance between the two parallel lines.

In this thesis we are mainly interested in counting the number of inscribed squares that lie in the zero-dimensional parts of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}). Such squares are *isolated*as they lie in a neighbourhood that contains no other squares inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f). Our main result is the following theorem, proven in the next section.

###### Theorem 4.8.

Let f ∈ ℂ ⁡ [x, y] f\in\mathbb{C}[x,y] of degree m m define an algebraic plane curve 𝐕 ⁡ ( f) ⊂ ℂ 2 \mathbf{V}(f)\subset\mathbb{C}^{2}. The number of isolated squares inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f) is at most ( m 4 − 5 ​ m 2 − 4 ​ m) / 4 (m^{4}-5m^{2}-4m)/4.

## 4 An upper bound on the number of isolated squares

The variety 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) of squares inscribed on an algebraic plane curve 𝐕 ⁡ ( f) \mathbf{V}(f) consists of a finite number of irreducible components and hence contains a finite number of isolated points by Lemma 2.7. How do we count or estimate the number of these isolated points? We will state and use a theorem by Bernshtein to provide an upper bound on the isolated squares inscribed on an algebraic plane curve.

A classical result from algebraic geometry, called Bézout’s Theorem, supplies a bound on the cardinality of a variety in terms of the degrees of the defining polynomials: If 𝐕 ⁡ ( f 1, …, f s) \mathbf{V}(f_{1},\dots,f_{s}) is finite, then its cardinality is at most the product ∏ deg ⁡ f i \prod\deg f_{i} of the degrees of the defining polynomials. The four generators of I f = ⟨ f ⁡ ( a + c, b + d), f ⁡ ( a + d, b − c), f ⁡ ( a − c, b − d), f ⁡ ( a − d, b + c) ⟩ I_{f}=\langle f(a+c,b+d),f(a+d,b-c),f(a-c,b-d),f(a-d,b+c)\rangle all have the same degree as f f, say m m. Ignoring for a moment the technicality that 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) is not finite, from Bézout we would expect that 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) contains at most m 4 m^{4} points.

Bézout’s Theorem is best stated in the context of projective space, and considering intersection multiplicities, see Cox [4, Section 8.7]. Apart from being a very useful theoretical tool, Bézout’s bound acts as a baseline against which we can judge other root counting methods.

A more refined estimate than Bézout’s bound makes use of more structure of the polynomials defining a variety than just their degrees. Bernshtein in his paper “The number of roots of a system of equations” [1], and Kushnirenko and Khovanskii in related papers, developed theorems to count the number of isolated roots of a polynomial system by exploiting the sparsity structure of the monomials appearing in the defining polynomials. In deference to all three mathematicians, the resulting bound is often called the BKK-bound.

###### Theorem 4.1 (Bernshtein [1, 3, 12, 20]).

Let f 1, …, f n ∈ ℂ ⁡ [x 1, …, x n] f_{1},\dots,f_{n}\in\mathbb{C}[x_{1},\dots,x_{n}]. Then the number of isolated zeros in 𝐕 ⁡ ( f 1, …, f n) ∩ ( ℂ ∖ { 0 }) n \mathbf{V}(f_{1},\dots,f_{n})\cap(\mathbb{C}\setminus\{0\})^{n} is bounded from above by the mixed volume M ​ V ​ ( 𝒩 ⁡ ( f 1), …, 𝒩 ⁡ ( f n)) MV(\mathcal{N}(f_{1}),\dots,\mathcal{N}(f_{n})) of the Newton polytopes of the generators f i f_{i}.

A priori Bernshtein’s Theorem has two drawbacks: it provides no information about positive-dimensional components of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}), and it may miss isolated solutions that lie in a coordinate hyperplane, a linear subspace where one or more coordinates are zero. We relegate the study of the positive-dimensional components to future work.

We will argue that the interference of the coordinate hyperplanes turns out to not be a restriction for counting the zero-dimensional part of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}); let f f be a plane curve and suppose one of the isolated points p p of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) lies in a coordinate hyperplane. Two phenomena can cause p p to lie in a coordinate hyperplane: the square inscribed by 𝐕 ⁡ ( f) \mathbf{V}(f) corresponding to p p either has

1. 1.

a center located on the union of the x x - and y y -axes 𝐕 ⁡ ( x ​ y) \mathbf{V}(xy), or

2. 2.

corners lying on the translate 𝐕 ​ ( ( x − a) ​ ( y − b)) \mathbf{V}((x-a)(y-b)) of the coordinate-axes to its center.

Note that both phenomena can occur at the same time, Figure 14 \@vpageref []fig:square-in-hyperplane depicts the square ( 0, 0, 0, 1) (0,0,0,1) inscribed by 𝐕 ⁡ ( x ​ y) \mathbf{V}(xy).

[image: Refer to caption] Figure 14: The square ( 0, 0, 0, 1) (0,0,0,1) lies in three coordinate hyperplanes.

Both these situations are an artifact of choosing coordinates for the geometric object that is the curve. By translating the curve we can ensure the center of the square corresponding to p p no longer lies on 𝐕 ⁡ ( x ​ y) \mathbf{V}(xy). A rotation suffices to ensure the corners and the center do not lie on the same translate of 𝐕 ⁡ ( x ​ y) \mathbf{V}(xy).

As 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) has a finite number of irreducible components, there exists a curve f ′ f^{\prime} obtainable from f f by translations and rotations so that none of the zero-dimensional components of 𝐕 ⁡ ( I f ′) \mathbf{V}(I_{f^{\prime}}) lie in a coordinate hyperplane. For the purpose of counting the number of isolated squares inscribed on a curve we can safely assume Bernshtein’s Theorem acounts for all of them.

We want to bound the number of isolated squares in 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) using Bernshtein’s Theorem; What are the concrete objects appearing in the expression for the mixed volume M ​ V ​ ( 𝒩 ⁡ ( f 1), 𝒩 ⁡ ( f 2), 𝒩 ⁡ ( f 3), 𝒩 ⁡ ( f 4)) MV(\mathcal{N}(f_{1}),\mathcal{N}(f_{2}),\mathcal{N}(f_{3}),\mathcal{N}(f_{4})) for the algebraic square peg problem? It is straightforward to calculate the mixed volume for the polynomials of the form f ⁡ ( a + c, b + d) f(a+c,b+d) that generate I f = ⟨ f ⁡ ( a + c, b + d), f ⁡ ( a + d, b − c), f ⁡ ( a − c, b − d), f ⁡ ( a − d, b + c) ⟩ I_{f}=\langle f(a+c,b+d),f(a+d,b-c),f(a-c,b-d),f(a-d,b+c)\rangle, but we show in Section 4.1 \@vpageref []sec:us that these generators do not provide a useful BKK bound in general.

We pursue a five step program to obtain the bound ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 on the number of isolated squares inscribed on an algebraic plane curve of degree m m. The first step is a better choice of generators g i g_{i} of I f I_{f} in Section 4.2 \@vpageref []sec:ideal-rewrite. In Section 4.3 \@vpageref []sec:monomial-presence we will see that this choice will allow for more control on the monomials present in the generators. That control translates into smaller Newton polytopes in the third step discussed in Section 4.4 \@vpageref []sec:newton-polytope-shapes. The Minkowski sum of these smaller Newton polytopes is described in Section 4.5 \@vpageref []sec:minkowski-sum-shape. In the fifth and final step of our program we calculate the volume of the Minkowski sum ∑ λ i ​ 𝒩 ​ ( g i) \sum\lambda_{i}\mathcal{N}(g_{i}) and extract the mixed volume of the 𝒩 ⁡ ( g i) \mathcal{N}(g_{i}).

The fact that an algebraic plane curve of degree m m inscribes at most ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 isolated squares is then an immediate consequence of invoking Bernshtein’s Theorem, Theorem 4.1, with the data M ​ V ​ ( 𝒩 ⁡ ( g 1), 𝒩 ⁡ ( g 2), 𝒩 ⁡ ( g 3), 𝒩 ⁡ ( g 4)) MV(\mathcal{N}(g_{1}),\mathcal{N}(g_{2}),\mathcal{N}(g_{3}),\mathcal{N}(g_{4})) as calculated by the five step program.

### 4.1 The effect of naive generators

Let f = ∑ c i, j ​ x i ​ y j f=\sum c_{i,j}x^{i}y^{j} of degree m m define a plane curve. We saw that an application of Bézout’s Theorem to I f = ⟨ f ⁡ ( a + c, b + d), f ⁡ ( a + d, b − c), f ⁡ ( a − c, b − d), f ⁡ ( a − d, b + c) ⟩ I_{f}=\langle f(a+c,b+d),f(a+d,b-c),f(a-c,b-d),f(a-d,b+c)\rangle only tells us that the finite part of 𝐕 ⁡ ( I f) \mathbf{V}(I_{f}) is at most of size m 4 m^{4}. An application of Bernshtein’s Theorem will bound the number of isolated squares inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f), up to the squares that lie in a coordinate hyperplane. Can we do better than Bézout’s bound by applying Bernshtein’s Theorem? Unfortunately, not immediately.

Suppose that the monomials 1 1, x m x^{m} and y m y^{m} appear in f f with nonzero coefficients, that is, the Newton polytope of f f is as large as it can be for a curve of degree m m. To calculate the BKK bound we first determine what the Newton polytopes of f ⁡ ( a + c, b + d) f(a+c,b+d), f ⁡ ( a − c, b − d) f(a-c,b-d), f ⁡ ( a + d, b − c) f(a+d,b-c), and f ⁡ ( a − d, b + c) f(a-d,b+c) are by looking at the monomials occuring in them.

Substituting the corner ( a − c, b − d) (a-c,b-d) into f f and expanding f ⁡ ( a − c, b − d) f(a-c,b-d), the monomial x m x^{m} gets mapped to ∑ j = 0 m ( m j) ​ a j ​ ( − 1) m − j ​ c m − j \sum_{j=0}^{m}{m\choose j}a^{j}(-1)^{m-j}c^{m-j}, which establishes that a m a^{m} and c m c^{m} appear with nonzero coefficients in f ⁡ ( a − c, b − d) f(a-c,b-d). Similar reasoning applied to y m y^{m} guarantees the presence of the monomials b m b^{m} and d m d^{m}. As presence of the monomial 1 1 is unaffected by the substitution, we see that the Newton polytope 𝒩 ⁡ ( f ⁡ ( a − c, b − d)) \mathcal{N}(f(a-c,b-d)) contains at least conv ⁡ { a m, b m, c m, d m, 1 } = m ​ conv ​ { 0, e 1, e 2, e 3, e 4 } = m ​ Δ \mathrm{conv}\{a^{m},b^{m},c^{m},d^{m},1\}=m\mathrm{conv}\{0,e_{1},e_{2},e_{3},e_{4}\}=m\Delta. All monomials of degree at most m m are contained in m ​ Δ m\Delta, so we conclude that 𝒩 ⁡ ( f ⁡ ( a − c, b − d)) = m ​ Δ \mathcal{N}(f(a-c,b-d))=m\Delta. The same argument goes through for the other Newton polytopes. Calculating the volume of the Minkowski sum ∑ 1 4 λ i ​ m ​ Δ \sum_{1}^{4}\lambda_{i}m\Delta we see that

 | Vol 4 ​ ( ∑ 1 4 λ i ​ m ​ Δ) = ( ∑ 1 4 λ i) n ​ Vol 4 ​ ( m ​ Δ), \mathrm{Vol}_{4}\left(\sum_{1}^{4}\lambda_{i}m\Delta\right)=\left(\sum_{1}^{4}\lambda_{i}\right)^{n}\!\!\!\!\mathrm{Vol}_{4}(m\Delta), |  |

so the mixed volume of the Newton polytopes is 4! 4! times the volume of m ​ Δ m\Delta. That is, 4! ​ m 4 / 4! = m 4 4!m^{4}/4!=m^{4}.

The resulting estimate is the same as the one supplied by Bézout. To overcome this problem it is necessary that we pick a set of generators for I f I_{f} whose Newton polytopes are smaller than m ​ Δ m\Delta. This is the first step of our five step program, which we undertake in Section 4.2 \@vpageref []sec:ideal-rewrite.

### 4.2 A better choice of generators

The issue with the naive generators of I f = ⟨ f ⁡ ( a + c, b + d), f ⁡ ( a + d, b − c), f ⁡ ( a − c, b − d), f ⁡ ( a − d, b + c) ⟩ I_{f}=\langle f(a+c,b+d),f(a+d,b-c),f(a-c,b-d),f(a-d,b+c)\rangle not providing a BKK bound different from Bézout’s bound is that they contain a lot of redundant information. By reducing the redundancy in the generators of I f I_{f} we get a set of generators for which we will be able to show in the next two sections that their Newton polytopes are smaller than those of the original generators.

Define polynomials g 1, g 2, g 3, g 4 g_{1},g_{2},g_{3},g_{4} by

 | g 1 = f ⁡ ( a + c, b + d) + f ⁡ ( a − c, b − d) − f ⁡ ( a − d, b + c) − f ⁡ ( a + d, b − c), g 2 = f ⁡ ( a + c, b + d) − f ⁡ ( a − c, b − d), g 3 = f ( a − d, b + c) − f ( a + d, b − c), g 4 = f ( a + d, b − c). \begin{array}[]{l}g_{1}=f(a+c,b+d)+f(a-c,b-d)-f(a-d,b+c)-f(a+d,b-c),\\ g_{2}=f(a+c,b+d)-f(a-c,b-d),\\ g_{3}=\phantom{f(a+c,b+d)+f(a-c,b-d)-~}f(a-d,b+c)-f(a+d,b-c),\\ g_{4}=\phantom{f(a+c,b+d)+f(a-c,b-d)-f(a-d,b+c)-~}f(a+d,b-c).\end{array} |  | (1) |

As the g i g_{i} are linear combinations of the generators of I f I_{f}, it is clear that they generate a subideal of I f I_{f}. It is easily checked that the original generators are contained in this subideal as well, so ⟨ g 1, g 2, g 3, g 4 ⟩ = ⟨ f ⁡ ( a + c, b + d), f ⁡ ( a + d, b − c), f ⁡ ( a − c, b − d), f ⁡ ( a − d, b + c) ⟩ \langle g_{1},g_{2},g_{3},g_{4}\rangle=\langle f(a+c,b+d),f(a+d,b-c),f(a-c,b-d),f(a-d,b+c)\rangle. It may not be immediately clear that we have gained anything by this different choice of generators. Over the course of Section 4.3 \@vpageref []sec:monomial-presence, Section 4.4 \@vpageref []sec:newton-polytope-shapes, Section 4.5 \@vpageref []sec:minkowski-sum-shape and Section 4.6 \@vpageref []sec:minkowski-sum-volumes we will show that M ​ V ​ ( 𝒩 ⁡ ( g 1), 𝒩 ⁡ ( g 2), 𝒩 ⁡ ( g 3), 𝒩 ⁡ ( g 4)) = m 4 − 5 ​ m 2 + 4 ​ m MV(\mathcal{N}(g_{1}),\mathcal{N}(g_{2}),\mathcal{N}(g_{3}),\mathcal{N}(g_{4}))=m^{4}-5m^{2}+4m, a definite improvement over the previous estimate m 4 m^{4}.

### 4.3 Monomials present in g i g_{i}

We have shown that the Newton polytopes 𝒩 ⁡ ( f ⁡ ( a + c, b + d)) \mathcal{N}(f(a+c,b+d)) of the generators of I f I_{f} all equal the simplex m ​ Δ m\Delta by showing that they contain the vertices ( 0, 0, 0, 0) (0,0,0,0) and m ​ e i me_{i} for i = 1, 2, 3, 4 i=1,2,3,4. Since g 4 = f ⁡ ( a + d, b − c) g_{4}=f(a+d,b-c) we know that 𝒩 ⁡ ( g 4) = m ​ Δ \mathcal{N}(g_{4})=m\Delta.

The construction of the generators g 1 g_{1}, g 2 g_{2}, and g 3 g_{3} causes the constant term to disappear, but it is less clear which monomials of the g i g_{i} then will be vertices of the Newton polytopes. Which monomials are even present in the generators g i g_{i}?

Since our five step program has the aim of proving the bound ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 for all curves of degree m m, we can assume that the coefficients of f = ∑ i + j ≤ m C i, j ​ x i ​ y j f=\sum_{i+j\leq m}C_{i,j}x^{i}y^{j} are not related in such a way that they cause cancellation in the g i g_{i}. After some algebraic manipulation we will see that the presence of a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} in g i g_{i} then only depends on i i and the parity of γ 3 + γ 4 \gamma_{3}+\gamma_{4}, barring the exceptional case for g 1 g_{1} whenever γ 3 = γ 4 \gamma_{3}=\gamma_{4} is an even number. The presence of the monomial a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} in g i g_{i} can be read off from Equation ( 2) \@vpageref []eq:presence and is summarized in Table 1 \@vpageref []tab:monomial-presence. An example of the monomials present in a fourth degree curve is displayed in Section 4.3.1 \@vpageref []sec:fourth-example.

 | γ 3 + γ 4 \gamma_{3}+\gamma_{4} odd | γ 3 + γ 4 \gamma_{3}+\gamma_{4} even |

 |  | γ 3 = γ 4 \gamma_{3}=\gamma_{4}, even | otherwise |

g 1 g_{1} | absent | absent | present |

g 2 g_{2} and g 3 g_{3} | present | absent | absent |

g 4 g_{4} | present | present | present |

Table 1: Presence of monomials a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} in g i g_{i} depends on the parity of γ 3 + γ 4 \gamma_{3}+\gamma_{4}.

Substituting the expressions for the corners into the variables x x and y y transforms monomials x i ​ y j x^{i}y^{j} of degree k k to monomials a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} of the same degree k k, as seen from the binomial expansion

 | ( a + c) i ​ ( b + d) j = ∑ p = 0 i ( i p) ​ a p ​ c i − p ​ ∑ q = 0 j ( j q) ​ b q ​ d j − q. (a+c)^{i}(b+d)^{j}=\sum_{p=0}^{i}{i\choose p}a^{p}c^{i-p}\sum_{q=0}^{j}{j\choose q}b^{q}d^{j-q}. |  |

To establish the presence or absence of monomials in g i g_{i} of degree k k it thus suffices to consider the k k -th homogeneous part of f f. We consider ( g i) k = h i ​ 1 ​ f ​ ( a + c, b + d) k + h i ​ 2 ​ f ​ ( a − c, b − d) k + h i ​ 3 ​ f ​ ( a − d, b + c) k + h i ​ 4 ​ f ​ ( a + d, b − c) k (g_{i})_{k}=h_{i1}f(a+c,b+d)_{k}+h_{i2}f(a-c,b-d)_{k}+h_{i3}f(a-d,b+c)_{k}+h_{i4}f(a+d,b-c)_{k}, where h i ​ j ∈ { − 1, 0, 1 } h_{ij}\in\{-1,0,1\} according to the choices in Equation ( 1) \@vpageref []eq:gi. Expanding the definitions results in the equations

 | f ​ ( a ± c, b ± d) k = ∑ j = 0 k C k − j, j ​ ( a ± c) k − j ​ ( b ± d) j, f ​ ( a ± d, b ∓ c) k = ∑ j = 0 k C k − j, j ​ ( a ± d) k − j ​ ( b ∓ c) j. \begin{array}[]{lr}f(a\pm c,b\pm d)_{k}=\sum_{j=0}^{k}C_{k-j,j}(a\pm c)^{k-j}(b\pm d)^{j},\\ f(a\pm d,b\mp c)_{k}=\sum_{j=0}^{k}C_{k-j,j}(a\pm d)^{k-j}(b\mp c)^{j}.\end{array} |  |

In addition to expanding the binomial terms ( a ± d) k − j (a\pm d)^{k-j} and ( b ∓ c) j (b\mp c)^{j} in f ​ ( a ± d, b ∓ c) k f(a\pm d,b\mp c)_{k} as before, we keep track of the coefficients C k − j, j C_{k-j,j} and minus signs. Gathering monomials we get

 | f ​ ( a ± d, b ∓ c) k \displaystyle f(a\pm d,b\mp c)_{k} | = ∑ j = 0 k C k − j, j ​ ∑ i = 0 k − j ( k − j i) ​ a i ​ d k − j − i ​ ( ±) k − j − i ​ ∑ l = 0 j ( j l) ​ b l ​ c j − l ​ ( ∓) j − l \displaystyle=\sum_{j=0}^{k}C_{k-j,j}\sum_{i=0}^{k-j}{k-j\choose i}a^{i}d^{k-j-i}(\pm)^{k-j-i}\sum_{l=0}^{j}{j\choose l}b^{l}c^{j-l}(\mp)^{j-l} |  |

 |  | = ∑ j = 0 k ∑ i = 0 k − j ∑ l = 0 j C k − j, j ​ ( k − j i) ​ ( j l) ​ ( ±) k − j − i ​ ( ∓) j − l ​ a i ​ b l ​ c j − l ​ d k − j − i. \displaystyle=\sum_{j=0}^{k}\sum_{i=0}^{k-j}\sum_{l=0}^{j}C_{k-j,j}{k-j\choose i}{j\choose l}(\pm)^{k-j-i}(\mp)^{j-l}a^{i}b^{l}c^{j-l}d^{k-j-i}. |  |

Summing up h i ​ 3 ​ f ​ ( a − d, b + c) + h i ​ 4 ​ f ​ ( a + d, b − c) h_{i3}f(a-d,b+c)+h_{i4}f(a+d,b-c) we can read off the coefficient of the monomial with exponent γ = ( i, l, j − l, k − j − i) \gamma=(i,l,j-l,k-j-i) as

 | C γ 1 + γ 4, γ 2 + γ 3 ​ ( γ 1 + γ 4 γ 1) ​ ( γ 2 + γ 3 γ 2) ​ ( h i ​ 3 ​ ( − 1) γ 4 + h i ​ 4 ​ ( − 1) γ 3). C_{\gamma_{1}+\gamma_{4},\gamma_{2}+\gamma_{3}}{\gamma_{1}+\gamma_{4}\choose\gamma_{1}}{\gamma_{2}+\gamma_{3}\choose\gamma_{2}}(h_{i3}(-1)^{\gamma_{4}}+h_{i4}(-1)^{\gamma_{3}}). |  |

The derivation for h i ​ 1 ​ f ​ ( a + c, b + d) + h i ​ 2 ​ f ​ ( a − c, b − d) h_{i1}f(a+c,b+d)+h_{i2}f(a-c,b-d) is analogous. The constant term C 0, 0 C_{0,0} disappears from g i g_{i} as long as the sum h i ​ 1 + h i ​ 2 + h i ​ 3 + h i ​ 4 h_{i1}+h_{i2}+h_{i3}+h_{i4} vanishes. With our choice of generators this is the case. For k > 0 k>0 the degree k k monomial a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} occurs in g i g_{i} in the term

 |  | [( γ 1 + γ 3 γ 1) ( γ 2 + γ 4 γ 2) C γ 1 + γ 3, γ 2 + γ 4 ( h i ​ 1 + h i ​ 2 ( − 1) γ 3 + γ 4) + \displaystyle\left[{\gamma_{1}+\gamma_{3}\choose\gamma_{1}}{\gamma_{2}+\gamma_{4}\choose\gamma_{2}}C_{\gamma_{1}+\gamma_{3},\gamma_{2}+\gamma_{4}}\left(h_{i1}+h_{i2}(-1)^{\gamma_{3}+\gamma_{4}}\right)\right.+ |  | (2) |

 |  | ( γ 1 + γ 4 γ 1) ( γ 2 + γ 3 γ 2) C γ 1 + γ 4, γ 2 + γ 3 ( h i ​ 3 ( − 1) γ 4 + h i ​ 4 ( − 1) γ 3)] a γ 1 b γ 2 c γ 3 d γ 4. \displaystyle\left.{\gamma_{1}+\gamma_{4}\choose\gamma_{1}}{\gamma_{2}+\gamma_{3}\choose\gamma_{2}}C_{\gamma_{1}+\gamma_{4},\gamma_{2}+\gamma_{3}}\left(h_{i3}(-1)^{\gamma_{4}}+h_{i4}(-1)^{\gamma_{3}}\right)\right]a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}}. |  |

Here we see that for particular values of the coefficients C α C_{\alpha} some extra cancellation may occur that does not happen in the general case. However, for a generic choice of coefficients, if γ 3 ≠ γ 4 \gamma_{3}\neq\gamma_{4} the two summands between brackets in Equation ( 2) \@vpageref []eq:presence are independent. Both g 2 g_{2} and g 3 g_{3} have two of the h i ​ j h_{ij} set to zero, so then the bracketed term is zero if, respectively,

 | 1 + ( − 1) ​ ( − 1) γ 3 + γ 4 = 0, or ( − 1) γ 4 + ( − 1) ​ ( − 1) γ 3 = 0. 1+(-1)(-1)^{\gamma_{3}+\gamma_{4}}=0,\quad\text{or}\quad(-1)^{\gamma_{4}}+(-1)(-1)^{\gamma_{3}}=0. |  |

Multiplying the second equation with ( − 1) γ 3 (-1)^{\gamma_{3}} we obtain the equation ( − 1) γ 3 + γ 4 − 1 = 0 (-1)^{\gamma_{3}+\gamma_{4}}-1=0. Thus for both g 2 g_{2} and g 3 g_{3} if γ 3 + γ 4 \gamma_{3}+\gamma_{4} is even the monomial a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} is absent, otherwise it is present.

A similar argument for g 1 g_{1} shows that a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}} is absent from g 1 g_{1} if γ 3 + γ 4 \gamma_{3}+\gamma_{4} is odd, since h 11 = h 12 h_{11}=h_{12} and h 13 = h 14 h_{13}=h_{14}. When γ 3 + γ 4 \gamma_{3}+\gamma_{4} is even there are two further cases to distinguish; when γ 3 = γ 4 \gamma_{3}=\gamma_{4} is an even number, Equation ( 2) \@vpageref []eq:presence collapses to

 | ( γ 1 + γ 3 γ 1) ​ ( γ 2 + γ 4 γ 2) ​ C γ 1 + γ 3, γ 2 + γ 4 ​ ( 1 + 1 − 1 − 1) ​ a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4 = 0. {\gamma_{1}+\gamma_{3}\choose\gamma_{1}}{\gamma_{2}+\gamma_{4}\choose\gamma_{2}}C_{\gamma_{1}+\gamma_{3},\gamma_{2}+\gamma_{4}}\left(1+1-1-1\right)a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}}=0. |  |

Otherwise, either γ 3 = γ 4 \gamma_{3}=\gamma_{4} is odd and Equation ( 2) \@vpageref []eq:presence evaluates to

 | 4 ​ ( γ 1 + γ 3 γ 1) ​ ( γ 2 + γ 4 γ 2) ​ C γ 1 + γ 3, γ 2 + γ 4 ​ a γ 1 ​ b γ 2 ​ c γ 3 ​ d γ 4, 4{\gamma_{1}+\gamma_{3}\choose\gamma_{1}}{\gamma_{2}+\gamma_{4}\choose\gamma_{2}}C_{\gamma_{1}+\gamma_{3},\gamma_{2}+\gamma_{4}}a^{\gamma_{1}}b^{\gamma_{2}}c^{\gamma_{3}}d^{\gamma_{4}}, |  |

or γ 3 ≠ γ 4 \gamma_{3}\neq\gamma_{4} and the two equations 1 + ( − 1) γ 3 + γ 4 = 1 1+(-1)^{\gamma_{3}+\gamma_{4}}=1 and ( − 1) ​ ( − 1) γ 4 + ( − 1) ​ ( − 1) γ 3 (-1)(-1)^{\gamma_{4}}+(-1)(-1)^{\gamma_{3}} need to be simultaneously zero.

In conclusion: monomials of odd c, d c,d -degree are present in g 2 g_{2} and g 3 g_{3} but absent in g 1 g_{1}. Monomials of even c, d c,d -degree are absent in g 2 g_{2} and g 3 g_{3} but present in g 1 g_{1} when the degrees of c c and d d are not both even. These relations are tabulated in Table 1 \@vpageref []tab:monomial-presence.

#### 4.3.1 Example for a fourth degree curve

The presence of monomials in the g i g_{i} so far is a little abstract. Let us look at a somewhat more concrete example by considering a generic fourth degree curve f = C 4, 0 ​ x 4 + C 3, 1 ​ x 3 ​ y + C 2, 2 ​ x 2 ​ y 2 + C 1, 3 ​ x ​ y 3 + C 0, 4 ​ y 4 + C 3, 0 ​ x 3 + C 2, 1 ​ x 2 ​ y + C 1, 2 ​ x ​ y 2 + C 0, 3 ​ y 3 + C 2, 0 ​ x 2 + C 1, 1 ​ x ​ y + C 0, 2 ​ y 2 + C 1, 0 ​ x + C 0, 1 ​ y + C 0, 0 f={C}_{4,0}x^{4}+{C}_{3,1}x^{3}y+{C}_{{2,2}}x^{2}y^{2}+{C}_{{1,3}}xy^{3}+{C}_{{0,4}}y^{4}+{C}_{{3,0}}x^{3}+{C}_{{2,1}}x^{2}y+{C}_{{1,2}}xy^{2}+{C}_{{0,3}}y^{3}+{C}_{{2,0}}x^{2}+{C}_{{1,1}}xy+{C}_{{0,2}}y^{2}+{C}_{{1,0}}x+{C}_{{0,1}}y+{C}_{{0,0}}. According to Table 1, the monomials in g 1 g_{1} should be all even c, d c,d -degree monomials of total degree at most four, excluding the monomials 1 1 and c 2 ​ d 2 c^{2}d^{2}, which is indeed the case:

 | g 1 \displaystyle g_{1} | = ( − 2 ​ C 2, 2 + 12 ​ C 4, 0) ​ a 2 ​ c 2 + ( − 6 ​ C 1, 3 + 6 ​ C 3, 1) ​ a ​ b ​ c 2 + ( − 12 ​ C 0, 4 + 2 ​ C 2, 2) ​ b 2 ​ c 2 \displaystyle=(-2{C}_{{2,2}}+12{C}_{{4,0}})a^{2}c^{2}+(-6{C}_{{1,3}}+6{C}_{{3,1}})abc^{2}+(-12{C}_{{0,4}}+2{C}_{{2,2}})b^{2}c^{2} |  |

 |  | + ( − 2 ​ C 0, 4 + 2 ​ C 4, 0) ​ c 4 + 12 ​ C 3, 1 ​ a 2 ​ c ​ d + 16 ​ C 2, 2 ​ a ​ b ​ c ​ d + 12 ​ C 1, 3 ​ b 2 ​ c ​ d \displaystyle+(-2{C}_{{0,4}}+2{C}_{{4,0}})c^{4}+12{C}_{{3,1}}a^{2}cd+16{C}_{{2,2}}abcd+12{C}_{{1,3}}b^{2}cd |  |

 |  | + ( 2 ​ C 1, 3 + 2 ​ C 3, 1) ​ c 3 ​ d + ( 2 ​ C 2, 2 − 12 ​ C 4, 0) ​ a 2 ​ d 2 + ( 6 ​ C 1, 3 − 6 ​ C 3, 1) ​ a ​ b ​ d 2 \displaystyle+(2{C}_{{1,3}}+2{C}_{{3,1}})c^{3}d+(2{C}_{{2,2}}-12{C}_{{4,0}})a^{2}d^{2}+(6{C}_{{1,3}}-6{C}_{{3,1}})abd^{2} |  |

 |  | + ( 12 ​ C 0, 4 − 2 ​ C 2, 2) ​ b 2 ​ d 2 + ( 2 ​ C 1, 3 + 2 ​ C 3, 1) ​ c ​ d 3 + ( 2 ​ C 0, 4 − 2 ​ C 4, 0) ​ d 4 \displaystyle+(12{C}_{{0,4}}-2{C}_{{2,2}})b^{2}d^{2}+(2{C}_{{1,3}}+2{C}_{{3,1}})cd^{3}+(2{C}_{{0,4}}-2{C}_{{4,0}})d^{4} |  |

 |  | + ( − 2 ​ C 1, 2 + 6 ​ C 3, 0) ​ a ​ c 2 + ( 2 ​ C 2, 1 − 6 ​ C 0, 3) ​ b ​ c 2 + 8 ​ C 2, 1 ​ a ​ c ​ d + 8 ​ C 1, 2 ​ b ​ c ​ d \displaystyle+(-2{C}_{{1,2}}+6{C}_{{3,0}})ac^{2}+(2{C}_{{2,1}}-6{C}_{{0,3}})bc^{2}+8{C}_{{2,1}}acd+8{C}_{{1,2}}bcd |  |

 |  | + ( 2 ​ C 1, 2 − 6 ​ C 3, 0) ​ a ​ d 2 + ( − 2 ​ C 2, 1 + 6 ​ C 0, 3) ​ b ​ d 2 + ( 2 ​ C 2, 0 − 2 ​ C 0, 2) ​ c 2 \displaystyle+(2{C}_{{1,2}}-6{C}_{{3,0}})ad^{2}+(-2{C}_{{2,1}}+6{C}_{{0,3}})bd^{2}+(2{C}_{{2,0}}-2{C}_{{0,2}})c^{2} |  |

 |  | + 4 ​ C 1, 1 ​ c ​ d + ( − 2 ​ C 2, 0 + 2 ​ C 0, 2) ​ d 2. \displaystyle+4{C}_{{1,1}}cd+(-2{C}_{{2,0}}+2{C}_{{0,2}})d^{2}. |  |

Of the list of monomials { a 2 c 2, a b c 2, b 2 c 2, c 4, a 2 c d, a b c d, b 2 c d, c 3 d, a 2 d 2, a b d 2, b 2 d 2 \{a^{2}c^{2},abc^{2},b^{2}c^{2},c^{4},a^{2}cd,abcd,b^{2}cd,c^{3}d,a^{2}d^{2},abd^{2},b^{2}d^{2}, c ​ d 3 cd^{3}, d 4 d^{4}, a ​ c 2 ac^{2}, b ​ c 2 bc^{2}, a ​ c ​ d acd, b ​ c ​ d bcd, a ​ d 2 ad^{2}, b ​ d 2 bd^{2}, c 2 c^{2}, c ​ d cd, d 2 } d^{2}\} occuring in g 1 g_{1}, those with only the variables c c and d d are depicted in Figure 15 \@vpageref []fig:squares.

[image: Refer to caption] (a) Monomials c γ 3 ​ d γ 4 c^{\gamma_{3}}d^{\gamma_{4}} present in g 1 g_{1} are represented by blue circles.

[image: Refer to caption] (b) Monomials c γ 3 ​ d γ 4 c^{\gamma_{3}}d^{\gamma_{4}} present in g 2 g_{2} are represented by blue circles.

Figure 15: The parity of γ 3 + γ 4 \gamma_{3}+\gamma_{4} determines whether monomials c γ 3 ​ d γ 4 c^{\gamma_{3}}d^{\gamma_{4}} are present in the generators g 1 g_{1} and g 2 g_{2}.

### 4.4 Newton polytope shapes

In the previous two sections we have shown which monomials are present in the g i g_{i}. In the third step of our five step program to prove that the mixed volume M ​ V ​ ( 𝒩 ⁡ ( g 1), 𝒩 ⁡ ( g 2), 𝒩 ⁡ ( g 3), 𝒩 ⁡ ( g 4)) = m 4 − 5 ​ m 2 + 4 ​ m MV(\mathcal{N}(g_{1}),\mathcal{N}(g_{2}),\mathcal{N}(g_{3}),\mathcal{N}(g_{4}))=m^{4}-5m^{2}+4m we describe the Newton polytopes 𝒩 ⁡ ( g i) \mathcal{N}(g_{i}). We already know that 𝒩 ⁡ ( g 4) = m ​ Δ \mathcal{N}(g_{4})=m\Delta and 𝒩 ⁡ ( g i) ⊂ m ​ Δ \mathcal{N}(g_{i})\subset m\Delta since the g i g_{i} are of degree m m. We also saw from Table 1 \@vpageref []tab:monomial-presence that 𝒩 ⁡ ( g 2) = 𝒩 ⁡ ( g 3) \mathcal{N}(g_{2})=\mathcal{N}(g_{3}).

In this section we prove that the Newton polytopes 𝒩 ⁡ ( g 1) \mathcal{N}(g_{1}) and 𝒩 ⁡ ( g 2) \mathcal{N}(g_{2}) alternate between the two types of simple polytopes P 1 P_{1} and P 2 P_{2} from Definition 3, according to the parity of m m. This dependence is summarized in Table 2. Their Schlegel diagrams are depicted in Figure 16 \@vpageref []fig:schlegel1 and Figure 17 \@vpageref []fig:schlegel2; the vertex descriptions of P 1 P_{1} and P 2 P_{2} as well as expressions of the vertices as intersections of facets are given in Lemma 4.2 and Lemma 4.3.

The Newton polytopes 𝒩 ⁡ ( g i) \mathcal{N}(g_{i}) are the convex hulls of the monomials appearing in the g i g_{i}; the pertinent information about g 1 g_{1}, g 2 g_{2} and g 3 g_{3} is shown in Table 1 \@vpageref []tab:monomial-presence. Let us rewrite this information in a form convenient for thinking about polytopes as intersections of halfspaces,

 | { exponents of ​ g 1 } \displaystyle\{\text{exponents of }g_{1}\} | = m Δ ∩ ⋃ n = 0 ∞ { x 3 + x 4 = 2 n + 2 } ∖ { x 3 = x 4 even }, \displaystyle=m\Delta\cap\bigcup_{n=0}^{\infty}\ \{x_{3}+x_{4}=2n+2\}\setminus\{x_{3}=x_{4}\text{ even}\}, |  |

 | { exponents of ​ g 2 } \displaystyle\{\text{exponents of }g_{2}\} | = m Δ ∩ ⋃ n = 0 ∞ { x 3 + x 4 = 2 n + 1 }. \displaystyle=m\Delta\cap\bigcup_{n=0}^{\infty}\ \{x_{3}+x_{4}=2n+1\}. |  |

The extreme monomials determine the convex hull, so we can express 𝒩 ⁡ ( g 1) \mathcal{N}(g_{1}) and 𝒩 ⁡ ( g 2) \mathcal{N}(g_{2}) as the following intersections of halfspaces:

 | 𝒩 ⁡ ( g 1) = m ​ Δ ∩ H x 3 + x 4 ≥ 2 ∩ H x 3 + x 4 ≤ 2 ​ n 1 + 2, 𝒩 ⁡ ( g 2) = m ​ Δ ∩ H x 3 + x 4 ≥ 1 ∩ H x 3 + x 4 ≤ 2 ​ n 2 + 1, \begin{array}[]{l}\mathcal{N}(g_{1})=m\Delta\cap H_{x_{3}+x_{4}\geq 2}\cap H_{x_{3}+x_{4}\leq 2n_{1}+2},\\ \mathcal{N}(g_{2})=m\Delta\cap H_{x_{3}+x_{4}\geq 1}\cap H_{x_{3}+x_{4}\leq 2n_{2}+1},\end{array} |  |

where n 1 n_{1} and n 2 n_{2} are the largest integers n 1 n_{1} and n 2 n_{2} such that 2 ​ n 1 + 2 2n_{1}+2 and 2 ​ n 2 + 1 2n_{2}+1 are both smaller than or equal to m m. If m m is even, then the halfspace H x 3 + x 4 ≤ 2 ​ n 1 + 2 H_{x_{3}+x_{4}\leq 2n_{1}+2} is redundant as the hyperplane H x 3 + x 4 = 2 ​ n 1 + 2 H_{x_{3}+x_{4}=2n_{1}+2} intersects m ​ Δ m\Delta in the facet defined by the hyperplane H ∑ x i = m H_{\sum x_{i}=m}. When m m is odd, H x 3 + x 4 ≤ 2 ​ n 2 + 1 H_{x_{3}+x_{4}\leq 2n_{2}+1} is redundant. These polytopes are central to the rest of this section, so let us fix some notation.

###### Definition 3.

The three types of polytopes P 0 P_{0}, P 1 P_{1} and P 2 P_{2} are obtained from m ​ Δ m\Delta by successively adding a facet-defining hyperplane parallel to H ( 0, 0, 1, 1) H_{(0,0,1,1)} so that

 | P 0 = P 0 ​ ( m) = m ​ Δ, P 1 = P 1 ​ ( m, l) = P 0 ∩ H x 3 + x 4 ≥ l, P 2 = P 2 ​ ( m, l, k) = P 1 ​ ( m, l) ∩ H x 3 + x 4 ≤ k. \begin{array}[]{l}P_{0}=P_{0}(m)=m\Delta,\\ P_{1}=P_{1}(m,l)=P_{0}\cap H_{x_{3}+x_{4}\geq l},\\ P_{2}=P_{2}(m,l,k)=P_{1}(m,l)\cap H_{x_{3}+x_{4}\leq k}.\end{array} |  |

The polytopes P 1 P_{1} and P 2 P_{2} are both four-dimensional when m ≥ 4 m\geq 4 but not for m ∈ { 2, 3 } m\in\{2,3\}. Schlegel diagrams for m = 4 m=4 are depicted in Figure 16 \@vpageref []fig:schlegel1 and Figure 17 \@vpageref []fig:schlegel2. With the notation from Definition 3 we can summarize the Newton polytopes of g 1 g_{1} and g 2 g_{2} for even and odd m m as

 | m = 2 ​ n + 2 m = 2 ​ n + 1 𝒩 ⁡ ( g 1) P 1 ​ ( m, 2) P 2 ​ ( m, 2, m − 1) 𝒩 ⁡ ( g 2) P 2 ​ ( m, 1, m − 1) P 1 ​ ( m, 1). \begin{array}[]{lll}&m=2n+2&\phantom{ugly}m=2n+1\\ \mathcal{N}(g_{1})&P_{1}(m,2)&\phantom{ugly}P_{2}(m,2,m-1)\\ \mathcal{N}(g_{2})&P_{2}(m,1,m-1)&\phantom{ugly}P_{1}(m,1).\\ \end{array} |  |

Table 2: 𝒩 ⁡ ( g 1) \mathcal{N}(g_{1}) and 𝒩 ⁡ ( g 2) \mathcal{N}(g_{2}) alternate between the polytopes P 1 P_{1} and P 2 P_{2}[image: Refer to caption] Figure 16: Schlegel diagram of P 1 P_{1} projected onto its facet where x 4 = 0 x_{4}=0.[image: Refer to caption] Figure 17: Schlegel diagram of P 2 P_{2} projected onto its facet where ∑ x i = m \sum x_{i}=m.

The combinatorial structure of the polytopes P 1 P_{1} and P 2 P_{2}, that is, which vertices are included in which faces, can be read off from the Schlegel diagrams. For those unconvinced that the Schlegel diagrams are correct, the next two lemmas establish vertex descriptions and the facet-vertex incidences of P 1 ​ ( m, l) P_{1}(m,l) and P 2 ​ ( m, l, k) P_{2}(m,l,k), without the visual aid.

###### Lemma 4.2.

Let m ≥ 4 m\geq 4 and 0 < l < m 0<l<m. Then P 1 = P 1 ​ ( m, l) P_{1}=P_{1}(m,l), as defined in Definition 3, is a simple polytope with eight labeled vertices given by the columns of the matrix

 | 1 2 3 4 5 6 7 8 ( 0 m − l 0 0 0 m − l 0 0) 0 0 m − l 0 0 0 m − l 0 l l l m 0 0 0 0 0 0 0 0 l l l m. \bordermatrix{&1&2&3&4&5&6&7&8\cr&0&m-l&0&0&0&m-l&0&0\cr&0&0&m-l&0&0&0&m-l&0\cr&l&l&l&m&0&0&0&0\cr&0&0&0&0&l&l&l&m\cr}. |  |

The vertices are expressed as intersections of hyperplanes in the following way,

 | H − e 1, 0 ∩ H − e 2, 0 ∩ H − e i, 0 ∩ H ∑ e k, m = { m ​ e j }, H − e 1, 0 ∩ H − e 2, 0 ∩ H − e i, 0 ∩ H − e 3 − e 4, l = { l ​ e j }, H − e 1 + j 1, 0 ∩ H − e 3 + j 2, 0 ∩ H ∑ e i, m ∩ H − e 3 − e 4, l = { ( m − l) ​ e 2 − j 1 + l ​ e 4 − j 2 }, \displaystyle\begin{array}[]{l}H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{-e_{i},0}\cap H_{\sum e_{k},m}=\{me_{j}\},\\ H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{-e_{i},0}\cap H_{-e_{3}-e_{4},l}=\{le_{j}\},\\ H_{-e_{1+j_{1}},0}\cap H_{-e_{3+j_{2}},0}\cap H_{\sum e_{i},m}\cap H_{-e_{3}-e_{4},l}=\{(m-l)e_{2-j_{1}}+le_{4-j_{2}}\},\end{array} |  |

where i, j ∈ { 3, 4 } i,j\in\{3,4\}, i ≠ j i\neq j and j 1, j 2 ∈ { 0, 1 } j_{1},j_{2}\in\{0,1\}.

###### Proof.

The polytope P 1 ​ ( m, l) P_{1}(m,l) has six facet-defining hyperplanes. There are ( 6 4) {6\choose 4} ways to form intersections of four of these hyperplanes. Due to the constraint x 3 + x 4 ≥ l x_{3}+x_{4}\geq l the intersection H − e 3, 0 ∩ H − e 4, 0 H_{-e_{3},0}\cap H_{-e_{4},0} does not contain any part of P 1 P_{1}. The intersection H − e 1, 0 ∩ H − e 2, 0 ∩ H − e 3 − e 4, l ∩ H ∑ e i, m H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{-e_{3}-e_{4},l}\cap H_{\sum e_{i},m} is empty due to conflicting constraints. Thus any intersection of five hyperplanes is either empty or lies outside P 1 P_{1}, as a five-fold intersection of the hyperplanes defining P 1 P_{1} involves at least one of these two intersections. Hence any vertex of P 1 P_{1} is contained in at most four facets.

This leaves 2 ​ ( 4 3) = 8 2{4\choose 3}=8 combinations of intersecting four hyperplanes to check, each involving exactly one of H − e 3, 0 H_{-e_{3},0} or H − e 4, 0 H_{-e_{4},0}. These eight intersections are listed above and result in eight distinct vertices, each of which is contained in precisely four facets. ∎

We obtain P 2 P_{2} from P 1 P_{1} by intersecting it with the halfspace H x 3 + x 4 ≤ k H_{x_{3}+x_{4}\leq k}. The facet of P 2 P_{2} defined by this halfspace is parallel to the hyperplane H x 3 + x 4 ≥ l H_{x_{3}+x_{4}\geq l} that cuts out P 1 P_{1} from P 0 P_{0}, and thus the derivation of P 2 P_{2} follows the same kind of reasoning as Lemma 4.2.

###### Lemma 4.3.

Let 0 < l < k < m 0<l<k<m and m ≥ 4 m\geq 4. Then P 2 = P 2 ​ ( m, l, k) P_{2}=P_{2}(m,l,k) is a simple polytope with twelve labeled vertices given by the colums of the matrix

 | 1 2 3 4 5 6 7 8 9 10 11 12 ( 0 m − l 0 0 m − k 0 0 m − l 0 0 m − k 0) 0 0 m − l 0 0 m − k 0 0 m − l 0 0 m − k l l l k k k 0 0 0 0 0 0 0 0 0 0 0 0 l l l k k k. \scriptscriptstyle\hskip-3.6806pt\bordermatrix{&1&2&3&4&5&6&7&8&9&10&11&12\cr&0&m-l&0&0&m-k&0&0&m-l&0&0&m-k&0\cr&0&0&m-l&0&0&m-k&0&0&m-l&0&0&m-k\cr&l&l&l&k&k&k&0&0&0&0&0&0\cr&0&0&0&0&0&0&l&l&l&k&k&k\cr}\displaystyle. |  |

The vertices are expressed as intersections of hyperplanes in the following way,

 | H − e 1, 0 ∩ H − e 2, 0 ∩ H e i, 0 ∩ H e 3 + e 4, k = { k ​ e j }, H − e 1, 0 ∩ H − e 2, 0 ∩ H e i, 0 ∩ H − e 3 − e 4, l = { l ​ e j }, H − e 1 + j 1, 0 ∩ H − e 3 + j 2, 0 ∩ H e 3 + e 4, k ∩ H ∑ e i, m = { ( m − k) ​ e 2 − j 1 + k ​ e 4 − j 2 }, H − e 1 + j 1, 0 ∩ H − e 3 + j 2, 0 ∩ H − e 3 − e 4, l ∩ H ∑ e i, m = { ( m − l) ​ e 2 − j 1 + l ​ e 4 − j 2 }, \begin{array}[]{l}H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{e_{i},0}\cap H_{e_{3}+e_{4},k}=\{ke_{j}\},\\ H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{e_{i},0}\cap H_{-e_{3}-e_{4},l}=\{le_{j}\},\\ H_{-e_{1+j_{1}},0}\cap H_{-e_{3+j_{2}},0}\cap H_{e_{3}+e_{4},k}\cap H_{\sum e_{i},m}=\{(m-k)e_{2-j_{1}}+ke_{4-j_{2}}\},\\ H_{-e_{1+j_{1}},0}\cap H_{-e_{3+j_{2}},0}\cap H_{-e_{3}-e_{4},l}\cap H_{\sum e_{i},m}=\{(m-l)e_{2-j_{1}}+le_{4-j_{2}}\},\end{array} |  |

where i, j ∈ { 3, 4 } i,j\in\{3,4\}, i ≠ j i\neq j and j 1, j 2 ∈ { 0, 1 } j_{1},j_{2}\in\{0,1\}.

###### Proof.

As in the previous lemma, the intersection H − e 3, 0 ∩ H − e 4, 0 H_{-e_{3},0}\cap H_{-e_{4},0} contains no part of P 2 P_{2}. Likewise, the intersection H − e 1, 0 ∩ H − e 2, 0 ∩ H ∑ e i, m H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{\sum e_{i},m} contains no vertices due to the conflicting constraint x 3 + x 4 ≤ k x_{3}+x_{4}\leq k. Again the implication is that no intersection of five hyperplanes contains a vertex of P 2 P_{2}.

Of the four-fold intersections those involving neither of H − e 3, 0 H_{-e_{3},0} nor H − e 4, 0 H_{-e_{4},0} are either contained in H e 3 + e 4, k ∩ H − e 3 − e 4, l H_{e_{3}+e_{4},k}\cap H_{-e_{3}-e_{4},l} or in H − e 1, 0 ∩ H − e 2, 0 ∩ H ∑ e i, m H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{\sum e_{i},m}, and thus contribute nothing. The remaining 4 ​ ( 3 2) = 12 4{3\choose 2}=12 options involving exactly one of { H − e 3, 0, H − e 4, 0 } \{H_{-e_{3},0},H_{-e_{4},0}\} and exactly one of { H e 3 + e 4, k, H − e 3 − e 4, l } \{H_{e_{3}+e_{4},k},H_{-e_{3}-e_{4},l}\} all contribute a vertex of P 2 P_{2}.

∎

### 4.5 Minkowski sum shapes

We are over halfway in our five step program to proving that there are at most ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 squares inscribed on an algebraic plane curve of degree m m. In the previous section we showed that the Newton polytopes 𝒩 ⁡ ( g 1) \mathcal{N}(g_{1}) are of the types P 0 P_{0}, P 1 P_{1} and P 2 P_{2} defined in Definition 3. In the fourth step of our program we show that the Minkowski sum λ 1 ​ 𝒩 ​ ( g 1) + λ 2 ​ 𝒩 ​ ( g 2) + λ 3 ​ 𝒩 ​ ( g 3) + λ 4 ​ 𝒩 ​ ( g 4) \lambda_{1}\mathcal{N}(g_{1})+\lambda_{2}\mathcal{N}(g_{2})+\lambda_{3}\mathcal{N}(g_{3})+\lambda_{4}\mathcal{N}(g_{4}) is itself a P 2 P_{2} type polytope. This result, Lemma 4.5, is due to the combination of two facts: the common refinement of the normal fans of P 0 P_{0}, P 1 P_{1} and P 2 P_{2} is the normal fan of P 2 P_{2}, and Lemma 4.4, which states that the normal fan of a Minkowski sum is the common refinement of the normal fans of the summands. Knowing the form of the Minkowski sum enables us to calculate its volume to finally determine the mixed volume of the 𝒩 ⁡ ( g i) \mathcal{N}(g_{i}).

As the polytopes 𝒩 ⁡ ( g i) \mathcal{N}(g_{i}) are of different shape depending on the parity of m m, as summarized in Table 2 \@vpageref []tab:shape-alternation, we rewrite the Minkowski sum ∑ λ i ​ 𝒩 ​ ( g i) \sum\lambda_{i}\mathcal{N}(g_{i}) as μ 1 ​ P 1 + μ 2 ​ P 2 + λ 4 ​ 𝒩 ​ ( g 4) \mu_{1}P_{1}+\mu_{2}P_{2}+\lambda_{4}\mathcal{N}(g_{4}). Since 𝒩 ⁡ ( g 2) = 𝒩 ⁡ ( g 3) \mathcal{N}(g_{2})=\mathcal{N}(g_{3}) one of μ 1 \mu_{1} or μ 2 \mu_{2} equals λ 2 + λ 3 \lambda_{2}+\lambda_{3}, while the other coefficient μ i \mu_{i} is set to λ 1 \lambda_{1}. Table 3 \@vpageref []tab:mu summarizes the values of μ 1 \mu_{1} and μ 2 \mu_{2}.

 | m ​ even m ​ odd μ 1 λ 1 λ 2 + λ 3 μ 2 λ 2 + λ 3 λ 1 \begin{array}[]{ccc}&m\text{ even}&m\text{ odd}\\ \mu_{1}&\lambda_{1}&\lambda_{2}+\lambda_{3}\\ \mu_{2}&\lambda_{2}+\lambda_{3}&\lambda_{1}\end{array} |  |

Table 3: The values of the coefficients μ 1 \mu_{1} and μ 2 \mu_{2} in
the expression of ∑ i = 1 4 λ i ​ 𝒩 ​ ( g i) = μ 1 ​ P 1 + μ 2 ​ P 2 + λ 4 ​ 𝒩 ​ ( g 4) \sum_{i=1}^{4}\lambda_{i}\mathcal{N}(g_{i})=\mu_{1}P_{1}+\mu_{2}P_{2}+\lambda_{4}\mathcal{N}(g_{4}).

The following lemma from Ziegler’s Lectures on Polytopes tells us that we should look at the normal fans of the Newton polytopes to determine the normal fan of the Minkowski sum.

###### Lemma 4.4 ( [27, Proposition 7.12, p198]).

The normal fan of a Minkowski sum is the common refinement of normal fans of the summands.

###### Proof.

Let P = P 1 + ⋯ + P n P=P_{1}+\dots+P_{n} and let Γ \Gamma be a face of P P. Fix a functional α \alpha in the normal cone of Γ \Gamma, that is, Γ \Gamma is precisely the subset of P P that is maximal under α \alpha. Let Γ ∋ v = v 1 + ⋯ + v n \Gamma\ni v=v_{1}+\dots+v_{n}. Suppose that some v j v_{j} does not maximize α \alpha in P i P_{i}. Then there exists a w j ∈ P j w_{j}\in P_{j} such that

 | α ⁡ ( v) = ∑ α ⁡ ( v i) < ∑ i ≠ j α ⁡ ( v i) + α ⁡ ( w j) = α ⁡ ( v − v j + w j). \alpha(v)=\sum\alpha(v_{i})<\sum_{i\neq j}\alpha(v_{i})+\alpha(w_{j})=\alpha(v-v_{j}+w_{j}). |  |

The vector v − v j + w j v-v_{j}+w_{j} is an element of P P by definition of the Minkowski sum, but this contradicts Γ \Gamma being the maximizer of α \alpha. Thus the faces of the P i P_{i} that are the summands in Γ = Γ 1 + ⋯ + Γ n \Gamma=\Gamma_{1}+\dots+\Gamma_{n} are themselves maximizers of P i P_{i} with respect to α \alpha. The normal cone of Γ \Gamma is then the intersection of the normal cones of the Γ i \Gamma_{i}. ∎

The normal cone of any face of a polytope is spanned by the facet normals of the facets said face is contained in. Thus, the normal fan of a polytope is completely determined by the normal cones of the vertices of a polytope. The descriptions of the vertices as intersections of hyperplanes in Lemma 4.2 and Lemma 4.3 directly tell us what the normal cones of the vertices of P 1 P_{1} and P 2 P_{2} are. To show that μ 1 ​ P 1 ​ ( m, l 1) + μ 2 ​ P 2 ​ ( m, l 2, k) + m ​ Δ \mu_{1}P_{1}(m,l_{1})+\mu_{2}P_{2}(m,l_{2},k)+m\Delta is of type P 2 P_{2} we first show that P 0 P_{0}, P 1 P_{1} and P 2 P_{2} have normal fans that successively refine each other.

###### Lemma 4.5.

The Minkowski sum μ 1 ​ P 1 ​ ( m, l 1) + μ 2 ​ P 2 ​ ( m, l 2, k) + m ​ Δ = P 2 ​ ( m ′, l ′, k ′) \mu_{1}P_{1}(m,l_{1})+\mu_{2}P_{2}(m,l_{2},k)+m\Delta=P_{2}(m^{\prime},l^{\prime},k^{\prime}) where

 | m ′ = ( μ 1 + μ 2 + λ 4) ​ m, l ′ = μ 1 ​ l 1 + μ 2 ​ l 2, k ′ = ( μ 1 + λ 4) ​ m + μ 2 ​ k. \begin{array}[]{lcr}m^{\prime}=(\mu_{1}+\mu_{2}+\lambda_{4})m,&l^{\prime}=\mu_{1}l_{1}+\mu_{2}l_{2},&k^{\prime}=(\mu_{1}+\lambda_{4})m+\mu_{2}k\\ \end{array}. |  |

###### Proof.

We obtain P i + 1 P_{i+1} from P i P_{i} by introducing an additional facet-defining hyperplane H i H^{i}. As P i P_{i} and P i + 1 P_{i+1} are both simple, any vertices contained in H i H^{i} are contained in three other hyperplanes. The normal cone of a vertex in H i H^{i} lies within the normal cone of a vertex of P i P_{i} cut off from P i + 1 P_{i+1} by H i H^{i}; each vertex cut off lies in an intersection H 1 i ∩ ⋯ ∩ H r i i H_{1}^{i}\cap\dots\cap H_{r_{i}}^{i} of hyperplanes whose facet-normals generate a cone containing the facet-normal of H i H^{i}.

We see from the vertex-facet incidences of Lemma 4.2 and Lemma 4.3 that the vertices of P 0 P_{0} that are cut off from P 1 P_{1} by H − e 3 − e 4, l H_{-e_{3}-e_{4},l} lie in the intersection H − e 3, 0 ∩ H − e 4, 0 H_{-e_{3},0}\cap H_{-e_{4},0} and the facet-normal − e 3 − e 4 -e_{3}-e_{4} of H − e 3 − e 4, l H_{-e_{3}-e_{4},l} is the sum of the facet-normals of H − e 3, 0 H_{-e_{3},0} and H − e 4, 0 H_{-e_{4},0}.

Likewise, the vertices of P 2 P_{2} that are cut off from P 1 P_{1} by H e 3 + e 4, k H_{e_{3}+e_{4},k} lie in the intersection H − e 1, 0 ∩ H − e 2, 0 ∩ H ∑ e i, m H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{\sum e_{i},m} and again the facet-normal of H e 3 + e 4, k H_{e_{3}+e_{4},k} is the sum of the facet normals e 1 + e 2 + e 3 + e 4 e_{1}+e_{2}+e_{3}+e_{4}, − e 1 -e_{1} and − e 2 -e_{2}.

Thus the normal fan of P 2 P_{2} is a refinement of the normal fan of P 1 P_{1} which is a refinement of the normal fan of P 0 P_{0}; the common refinement of the normal fans of P 0 P_{0}, P 1 P_{1} and P 2 P_{2} then is the normal fan of P 2 P_{2}. By Lemma 4.4 this is also the normal fan of the Minkowski sum ∑ 1 4 λ i ​ 𝒩 ​ ( g i) \sum_{1}^{4}\lambda_{i}\mathcal{N}(g_{i}).

In particular the Minkowski sum is itself a P 2 ​ ( m ′, l ′, k ′) P_{2}(m^{\prime},l^{\prime},k^{\prime}) polytope for appropriate constants m ′ m^{\prime}, l ′ l^{\prime} and k ′ k^{\prime}. We can read off the values of m ′ m^{\prime} and k ′ k^{\prime} from the vertices of P 2 ​ ( m ′, l ′, k ′) P_{2}(m^{\prime},l^{\prime},k^{\prime}) contained in the intersection of hyperplanes with normals ( 0, 0, 1, 1) (0,0,1,1) and ( 1, 1, 1, 1) (1,1,1,1), for example the vertex ( m ′ − k ′, 0, k ′, 0) (m^{\prime}-k^{\prime},0,k^{\prime},0). This vertex is the sum of vertices v i v_{i} of the summands of μ 1 ​ P 1 + μ 2 ​ P 2 + P 0 \mu_{1}P_{1}+\mu_{2}P_{2}+P_{0} that have a normal cone containing its normal cone.

As the normal cone of H − e 1, 0 ∩ H − e 2, 0 ∩ H − e 3, 0 ∩ H ∑ e i, m H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{-e_{3},0}\cap H_{\sum e_{i},m} contains the normal cone of H − e 1 + j, 0 ∩ H − e 3, 0 ∩ H ∑ e i, m ∩ H e 3 + e 4, k H_{-e_{1+j},0}\cap H_{-e_{3},0}\cap H_{\sum e_{i},m}\cap H_{e_{3}+e_{4},k}, we get the vertex ( μ 1 + λ 4) ​ m ​ e 4 + μ 2 ​ ( ( m − k) ​ e 2 − j + k ​ e 4) (\mu_{1}+\lambda_{4})me_{4}+\mu_{2}\left((m-k)e_{2-j}+ke_{4}\right). Summing up the coefficients gives m ′ = ( μ 1 + μ 2 + λ 4) ​ m m^{\prime}=(\mu_{1}+\mu_{2}+\lambda_{4})m. The coefficient of e 4 e_{4} is k ′ = ( μ 1 + λ 4) ​ m + μ 2 ​ k k^{\prime}=(\mu_{1}+\lambda_{4})m+\mu_{2}k.

The value of l ′ l^{\prime} can be recovered from a vertex contained in H − e 3 − e 4, l H_{-e_{3}-e_{4},l}. As the normal cone of H − e 1, 0 ∩ H − e 2, 0 ∩ H − e 3, 0 ∩ H − e 4, 0 H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{-e_{3},0}\cap H_{-e_{4},0} contains the normal cone of H − e 1, 0 ∩ H − e 2, 0 ∩ H − e 3, 0 ∩ H − e 3 − e 4, l H_{-e_{1},0}\cap H_{-e_{2},0}\cap H_{-e_{3},0}\cap H_{-e_{3}-e_{4},l}, we get the vertex ( μ 1 ​ l 1 + μ 2 ​ l 2) ​ e 4 (\mu_{1}l_{1}+\mu_{2}l_{2})e_{4} of the Minkowski sum, so l ′ = μ 1 ​ l 1 + μ 2 ​ l 2 l^{\prime}=\mu_{1}l_{1}+\mu_{2}l_{2}. ∎

### 4.6 Minkowski sum volumes

We have one step left of our program towards proving Theorem 4.8. Recall that Bernshtein’s Theorem uses the mixed volume M ​ V ​ ( 𝒩 ⁡ ( g 1), 𝒩 ⁡ ( g 2), 𝒩 ⁡ ( g 3), 𝒩 ⁡ ( g 4)) MV(\mathcal{N}(g_{1}),\mathcal{N}(g_{2}),\mathcal{N}(g_{3}),\mathcal{N}(g_{4})) to bound the number of isolated solutions in 𝐕 ⁡ ( g 1, g 2, g 3, g 4) ∩ ( ℂ ∖ { 0 }) 4 \mathbf{V}(g_{1},g_{2},g_{3},g_{4})\cap(\mathbb{C}\setminus\{0\})^{4}. The mixed volume, defined in Definition 1, is the coefficient of the monomial λ 1 ​ λ 2 ​ λ 3 ​ λ 4 \lambda_{1}\lambda_{2}\lambda_{3}\lambda_{4} as it appears in the expression for the volume of the Minkowski sum ∑ i = 1 4 λ i ​ 𝒩 ​ ( g i) \sum_{i=1}^{4}\lambda_{i}\mathcal{N}(g_{i}). In Lemma 4.5 we showed that this Minkowski sum can be expressed as the polytope P 2 ​ ( ( μ 1 + μ 2 + λ 4) ​ m, μ 1 ​ l 1 + μ 2 ​ l 2, ( μ 1 + λ 4) ​ m + μ 2 ​ k) P_{2}((\mu_{1}+\mu_{2}+\lambda_{4})m,\mu_{1}l_{1}+\mu_{2}l_{2},(\mu_{1}+\lambda_{4})m+\mu_{2}k). To complete the final step of our program, we should calculate the volume of a P 2 P_{2} type polytope.

From the halfspace definition in Definition 3 we see that P 2 ​ ( m ′, l ′, k ′) P_{2}(m^{\prime},l^{\prime},k^{\prime}) is the closure of the set difference P 1 ​ ( m ′, l ′) ∖ P 1 ​ ( m ′, k ′) {P_{1}(m^{\prime},l^{\prime})\setminus P_{1}(m^{\prime},k^{\prime})}. Thus the volume of P 2 ​ ( m ′, l ′, k ′) P_{2}(m^{\prime},l^{\prime},k^{\prime}) can be calculated as the difference in volumes of P 1 ​ ( m ′, l ′) P_{1}(m^{\prime},l^{\prime}) and P 1 ​ ( m ′, k ′) P_{1}(m^{\prime},k^{\prime}). In turn we can calculate the volume of P 1 P_{1} as the sum of four simplices that triangulate P 1 P_{1}. The volume of a simplex is straightforward to calculate by taking the determinant of a matrix whose columnvectors are the offsets from a distinguished vertex of the simplex to the other vertices. For the triangulation of P 1 P_{1} it is convenient to express its facets in a more combinatorial way.

###### Corollary 4.6.

Labeling the vertices of P 1 P_{1} by the numbers from one to eight, in the same way as in Lemma 4.2, the combinatorial facet description of P 1 P_{1} is

 | F 1 = H − e 1, 0 ∩ P 1 = { 1, 3, 4, 5, 7, 8 } F m = H ∑ e i, m ∩ P 1 = { 2, 3, 4, 6, 7, 8 } F 2 = H − e 2, 0 ∩ P 1 = { 1, 2, 4, 5, 6, 8 } F l = H − e 3 − e 4, l ∩ P 1 = { 1, 2, 3, 5, 6, 7 } F 3 = H − e 3, 0 ∩ P 1 = { 5, 6, 7, 8 } F 4 = H − e 4, 0 ∩ P 1 = { 1, 2, 3, 4 } \begin{array}[]{ll}F_{1}=H_{-e_{1},0}\cap P_{1}=\{1,3,4,5,7,8\}&F_{m}=H_{\sum e_{i},m}\cap P_{1}=\{2,3,4,6,7,8\}\\ F_{2}=H_{-e_{2},0}\cap P_{1}=\{1,2,4,5,6,8\}&F_{l}=H_{-e_{3}-e_{4},l}\cap P_{1}=\{1,2,3,5,6,7\}\\ F_{3}=H_{-e_{3},0}\cap P_{1}=\{5,6,7,8\}&F_{4}=H_{-e_{4},0}\cap P_{1}=\{1,2,3,4\}\end{array} |  |

###### Proof.

The statements of Lemma 4.2 and Lemma 4.3 express the vertices as intersections of hyperplanes. Inverting the relationship and expressing the facets as the set of vertices they contain ends up with the statement above. ∎

We triangulate P 1 P_{1} by writing it as the union of four simplices, each of which is defined by a set of five affinely independent vertices of P 1 P_{1}. As long as these simplices intersect in lower-dimensional faces we obtain a triangulation of P 1 P_{1}.

###### Corollary 4.7.

The volume of P 1 ​ ( m, l) P_{1}(m,l) is ( m − l) 3 ​ ( m + 3 ​ l) ​ 4! (m-l)^{3}(m+3l)4!.

###### Proof.

We shall first triangulate P 1 P_{1}, calculating its volume is then a matter of summing the volumes of the triangulating simplices.

Let v v be a vertex of P 1 P_{1}. An *opposing facet*of v v is facet of P 1 P_{1} that does not contain v v. Assume that we have a triangulation of every opposing facet of v v. The convex hull of v v and a simplex in a triangulation of an opposing facet is again a simplex. By Lemma 2.4 the simplices thus obtained triangulate P 1 P_{1}. The Cohen-Hickey algorithm [2, Section 3.1] triangulates a polytope by picking a vertex and recursively triangulating its opposing facets.

From the combinatorial description of P 1 P_{1} given in Corollary 4.6 it is easy to read off what the facets opposing a vertex are. In that notation the vertices of P 1 P_{1} are labeled 1, …, 8 1,\dots,8. We start the Cohen-Hickey algorithm by selecting as the first vertex v 1 = 1 v_{1}=1. Its opposing facets are F 3 F_{3} and F m F_{m}, the former of which is already a simplex (it is three-dimensional on four vertices).

The next step of the recursion triangulates F m F_{m} by picking v 2 = 2 v_{2}=2. The facets of F m F_{m} that oppose v 2 v_{2} are intersections of F m F_{m} with facets of P 1 P_{1} that oppose v 2 v_{2}, that is, F m ∩ F 3 = { 6, 7, 8 } F_{m}\cap F_{3}=\{6,7,8\}, a simplex, and F m ∩ F 1 = { 3, 4, 7, 8 } F_{m}\cap F_{1}=\{3,4,7,8\}. At the deepest level of the recursion we triangulate F m ∩ F 1 F_{m}\cap F_{1} by picking v 3 = 3 v_{3}=3 and we find the one-dimensional simplices F m ∩ F 1 ∩ F 2 = { 4, 8 } F_{m}\cap F_{1}\cap F_{2}=\{4,8\} and F m ∩ F 1 ∩ F 3 = { 7, 8 } F_{m}\cap F_{1}\cap F_{3}=\{7,8\}. The triangulation of F m ∩ F 1 F_{m}\cap F_{1} is depicted in Figure 18 \@vpageref []fig:P1-triangulation.

Our application of the Cohen-Hickey algorithm results in the following triangulation of P 1 P_{1}: { { 1, 5, 6, 7, 8 } \{\{1,5,6,7,8\}, { 1, 2, 6, 7, 8 } \{1,2,6,7,8\}, { 1, 2, 3, 4, 8 } \{1,2,3,4,8\}, { 1, 2, 3, 7, 8 } } \{1,2,3,7,8\}\}. The volume of P 1 ​ ( m, l) P_{1}(m,l) is the sum of the volumes of the simplices in this triangulation,

 | Vol 4 ​ ( P 1 ​ ( m, l)) \displaystyle\mathrm{Vol}_{4}(P_{1}(m,l)) | = | 0 m − l 0 0 0 0 m − l 0 l 0 0 0 − l 0 0 m − l | ​ 4! + | m − l m − l 0 0 0 0 m − l 0 0 − l − l − l 0 l l m | ​ 4! \displaystyle=\begin{vmatrix}[r]0&m-l&0&0\cr 0&0&m-l&0\cr l&0&0&0\cr-l&0&0&m-l\cr\end{vmatrix}4!+\begin{vmatrix}[r]m-l&m-l&0&0\cr 0&0&m-l&0\cr 0&-l&-l&-l\cr 0&l&l&m\cr\end{vmatrix}4! |  |

 |  | + | m − l 0 0 0 0 m − l m − l 0 0 0 − l − l 0 0 l m | ​ 4! + | m − l 0 0 0 0 m − l 0 0 0 0 m − l − l 0 0 0 m | ​ 4! \displaystyle+\begin{vmatrix}[r]m-l&0&0&0\cr 0&m-l&m-l&0\cr 0&0&-l&-l\cr 0&0&l&m\cr\end{vmatrix}4!+\begin{vmatrix}[r]m-l&0&0&0\cr 0&m-l&0&0\cr 0&0&m-l&-l\cr 0&0&0&m\cr\end{vmatrix}4! |  |

 |  | = ( m − l) 3 ​ l ​ 4! + ( m − l) 3 ​ l ​ 4! + ( m − l) 3 ​ l ​ 4! + ( m − l) 3 ​ m ​ 4! \displaystyle=(m-l)^{3}l4!+(m-l)^{3}l4!+(m-l)^{3}l4!+(m-l)^{3}m4! |  |

 |  | = ( m − l) 3 ​ ( m + 3 ​ l) ​ 4!. \displaystyle=(m-l)^{3}(m+3l)4!. |  |

∎

[image: Refer to caption] Figure 18: Triangulation of the face F m ∩ F 3 F_{m}\cap F_{3} of P 1 P_{1}, as in the proof of Corollary 4.7.

To calculate the volume of the Minkowski sum ∑ λ i ​ 𝒩 ​ ( g 1) = P 1 ​ ( m ′, l ′) ∖ P 1 ​ ( m ′, k ′) ¯ \sum\lambda_{i}\mathcal{N}(g_{1})=\overline{P_{1}(m^{\prime},l^{\prime})\setminus P_{1}(m^{\prime},k^{\prime})} we apply Corollary 4.7 and subtract the volume of P 1 ​ ( m ′, k ′) P_{1}(m^{\prime},k^{\prime}) from that of P 1 ​ ( m ′, l ′) P_{1}(m^{\prime},l^{\prime}). The expression for the volume we obtain is ( m ′ − l ′) 3 ​ ( m ′ + 3 ​ l ′) ​ 4! − ( m ′ − k ′) 3 ​ ( m ′ + 3 ​ k ′) ​ 4! (m^{\prime}-l^{\prime})^{3}(m^{\prime}+3l^{\prime})4!-(m^{\prime}-k^{\prime})^{3}(m^{\prime}+3k^{\prime})4!.

The mixed volume of 𝒩 ⁡ ( g 1) \mathcal{N}(g_{1}), 𝒩 ⁡ ( g 2) \mathcal{N}(g_{2}), 𝒩 ⁡ ( g 3) \mathcal{N}(g_{3}), 𝒩 ⁡ ( g 4) \mathcal{N}(g_{4}) can be extracted from the above volume as the coefficient of the monomial λ 1 ​ λ 2 ​ λ 3 ​ λ 4 \lambda_{1}\lambda_{2}\lambda_{3}\lambda_{4}. Extracting this coefficient by hand is somewhat tedious; Macaulay2 code that performs the necessary algebraic manipulations is included in the appendix, see Listing Code on page Code. Recall from Section 4.4 \@vpageref []sec:newton-polytope-shapes that for degrees two and three the polytopes P 1 P_{1} and P 2 P_{2} are not both four-dimensional. For these two boundary cases the code in Listing Code on page Code uses the PHCpack [10] interface from Macaulay2 to calculate the mixed volumes, which conform to the same formula as the m ≥ 4 m\geq 4 case.

At last we see that for all m ∈ ℕ m\in\mathbb{N} the mixed volume of the Newton polytopes 𝒩 ⁡ ( g 1) \mathcal{N}(g_{1}), 𝒩 ⁡ ( g 2) \mathcal{N}(g_{2}), 𝒩 ⁡ ( g 3) \mathcal{N}(g_{3}), 𝒩 ⁡ ( g 4) \mathcal{N}(g_{4}) is m 4 − 5 ​ m 2 + 4 ​ m m^{4}-5m^{2}+4m.

### 4.7 Applied BKK bound

We set out to prove that the number of isolated squares inscribed on an algebraic plane curve of degree m m is bounded by ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4. In the last five sections we have shown that the variety of complex squares inscribed on a plane curve 𝐕 ⁡ ( f) \mathbf{V}(f) is defined by four polynomials g i g_{i} with the property that the mixed volume of their Newton polytopes is ( m 4 − 5 ​ m 2 + 4 ​ m) (m^{4}-5m^{2}+4m). An immediate consequence of Bernshtein’s Theorem applied to these data is that the number of isolated squares of 𝐕 ⁡ ( g 1, g 2, g 3, g 4) \mathbf{V}(g_{1},g_{2},g_{3},g_{4}) that do not lie in a coordinate hyperplane is bounded by ( m 4 − 5 ​ m 2 + 4 ​ m) (m^{4}-5m^{2}+4m). By passing to a different choice of coordinates we can assume no isolated squares lie in any coordinate hyperplane. Finally, as there are four parametrizations of every square inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f) we divide the mixed volume by four and have proven Theorem 4.8.

###### Theorem 4.8.

Let f ∈ ℂ ⁡ [x, y] f\in\mathbb{C}[x,y] of degree m m define an algebraic plane curve 𝐕 ⁡ ( f) ⊂ ℂ 2 \mathbf{V}(f)\subset\mathbb{C}^{2}. The number of isolated squares inscribed on 𝐕 ⁡ ( f) \mathbf{V}(f) is at most ( m 4 − 5 ​ m 2 − 4 ​ m) / 4 (m^{4}-5m^{2}-4m)/4.

## 5 Experimental evidence for the number of complex squares

How many squares can be inscribed on an algebraic plane curve? Theorem 4.8 states that at most ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 isolated squares are inscribed on a plane curve of degree m m. Is this bound sharp, and if so, how often?

Table 4 \@vpageref []tab:experiments tabulates, for degrees three to ten, the number of squares (possibly with multiplicities) inscribed on the majority of plane curves from a sample of randomly chosen curves. The experiments were carried out using the computer algebra system Macaulay2 [9], the code used is listed in Listing Code on page Code. In all the cases the varieties turned out to be zero-dimensional, in which case all the squares inscribed on a curve are isolated. Note that the number of squares found on the curves of the sample, entered in the third column of Table 4 \@vpageref []tab:experiments, agrees exactly with the maximum ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 provided by Theorem 4.8. Not only is the bound sharp, these experiments suggest that the bound is attained for *all*squares inscribed on a generic curve. Proving this stronger result is out of scope for the current thesis.

Degree m m | # solutions | squares | fraction | field |

3 | 48 | 12 | 4991/5000 | ℚ \mathbb{Q} |

4 | 192 | 48 | 4998/5000 | ℚ \mathbb{Q} |

5 | 520 | 130 | 100/100 | ℚ \mathbb{Q} |

6 | 1140 | 285 | 50/50 | ℤ / 32479 \mathbb{Z}/32479 |

7 | 2184 | 546 | 1/1 | ℤ / 32479 \mathbb{Z}/32479 |

8 | 3808 | 952 | 1/1 | ℤ / 32479 \mathbb{Z}/32479 |

9 | 6192 | 1548 | 1/1 | ℤ / 32479 \mathbb{Z}/32479 |

10 | 9540 | 2385 | 1/1 | ℤ / 32479 \mathbb{Z}/32479 |

Table 4: Experimental results for number of complex squares calculated using Listing Code on page Code. The fraction column harbors the fraction of the sample of curves that attain the maximal number of squares.

The curves featuring in Table 4 \@vpageref []tab:experiments were generated by having Macaulay2 randomly pick the coefficients c γ c_{\gamma} of f = ∑ | γ | ≤ m c γ ​ x γ 1 ​ y γ 2 f=\sum_{|\gamma|\leq m}c_{\gamma}x^{\gamma_{1}}y^{\gamma_{2}} for a fixed degree m m. As the degree goes up the memory usage grows. Even a degree six curve already used more than fourteen gigabytes of memory when working with the rationals as a base field. Computations for degree seven ran out of memory after using more than fifty gigabytes. For this reason finite fields were used in the calculations with higher degrees.

## 6 Illustrative examples of real squares

The previous section argues that there is not much of interest going on in the complex case, almost all complex algebraic plane curves inscribe the maximum number of squares. For real plane curves, however, we have no evidence as to what the generic case is.

This section contains selected real plane curves of low degree that inscribe varying numbers of squares. The pictures have been plotted in Maple, using the code from Listing Code on page Code, based on numerical data for the locations of the squares computed by PHCpack [10]. The topology of the curves has been determined by a manual process: the RAGlib [21] Maple package provides at least one point on each connected component of a plane curve, by inspecting the plot and intersecting the curves with suitably chosen lines we can determine which visible components connect outside of the plotted range. The “realroots.m2” functionality written by Dan Grayson and Frank Sottile [24] was used for determining how many real intersections these lines and the curves have. The polynomials that define the curves in the plots are listed in Table 7 \@vpageref []tab:long-polys.

The maximal number of squares inscribed on a third degree curve is twelve, according to Theorem 4.8; the examples in this section show that a third degree real curve can inscribe any number of squares from zero to twelve, see Table 6(a) \@vpageref []tab:three-topologies. Two topological types attaining the maximum number are shown in Figure 22 \@vpageref []fig:twelve-clear and Figure 29 \@vpageref []fig:twelve-awesome. Curves of these types look like perturbations of either a) an oval times a line, or b) the product of three lines. The perturbation approach of constructing curves is called the “marking method” by Gudkov [11, Section 2.10].

The proofs of Emch, Jerrard and Stromquist establish that, generically, on a smooth enough Jordan curve the number of inscribed squares will be odd. It is no surprise then that we see the same behaviour for algebraic plane curves that topologically speaking are circles. Figure 19 \@vpageref []fig:inscribed-zeroOne shows algebraic Jordan curves inscribing one, three, five and seven squares.

[image: Refer to caption] (a) One square inscribed on f 30 f_{30} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Three squares inscribed on f 31 f_{31} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Five squares inscribed on f 32 f_{32} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (d) Seven squares inscribed on f 33 f_{33} in Table 7 \@vpageref []tab:long-polys

Figure 19: Algebraic Jordan curves inscribing an odd number of squares.

Recall that a Jordan curve starts and ends at the same point without intersecting itself, it is closed and simple. A Jordan curve has only one connected component and it is homeomorphic to a circle. Unlike Jordan curves, a simple algebraic plane curve can consist of multiple components, and the components can be homeomorphic to a circle or to the real line. Table 5 \@vpageref []tab:square-topologies tabulates the number of squares found on plane curves computed for this thesis with the code from Listing Code on page Code; the rows of the table are indexed by the number of components homeomorphic to the real line, and the columns are indexed by the number of components homeomorphic to a circle (called ovals).

The example curves homeomorphic to a real line, as well as some other topological types of curves, exhibit a parity condition on the number of inscribed squares just as in the Jordan case, see Section 6.1 \@vpageref []sec:possible-parity. The types for which this occurs have their entries shaded gray in Table 5 \@vpageref []tab:square-topologies. Whether this parity condition is an actual property of these curves or an artifact of our selection of examples remains to be seen. Other topological types have both an odd and an even number of squares, these are listed in Section 6.2 \@vpageref []sec:no-parity.

\diaghead(5,-2){lines ova $i$}{{\footnotesize\shortstack[l]{lines $i$}}}{{\footnotesize\shortstack[r]{ovals $j$}}} | 0 | 1 | 2 | 3 | 4 |

0 |  | 1, 3, 5, 7 | 0, 2, 4, 6, 16 |  | 8 |

1 | 0, 2, 4, 6, 12 | 1, 2 ∗ 2^{*}, 3, 5, 7, 9, 11 |  |  |  |

2 | 1, 4, 8, 9, 11 | 3, 5, 7 |  |  |  |

3 | 1, 4, 7, 8, 10, 11, 12 | 8, 9, 11 |  |  |  |

Table 5: Number of squares inscribed on curves of degree up to five. The ( i, j) (i,j) -th cell corresponds to curves homeomorphic to i i copies of the real line and j j copies of the circle. The entry 2 ∗ 2^{*} in the (1, 1) cell corresponds to Figure 26(b) \@vpageref []fig:debate.

The 2 2 that occurs in the entry for curves that consist of one line and one oval corresponds to Figure 26(b) \@vpageref []fig:debate. Inclusion of this reducible curve is debatable. If one allows reducible curves, then taking unions of lower degree curves will construct examples where the total number of inscribed squares is the sum of the squares inscribed on each curve in the union, each part behaving independently. At this point it is not clear to us whether reducible curves should be excluded.

 | 0 | 1 |

0 |  |  |

1 | 0, 2, 6, 12 | 1, 2, 3, 5, 7, 9, 11 |

2 |  |  |

3 | 4, 7, 8, 10, 11, 12 |  |

(a) Squares inscribed on degree three curves

 | 0 | 1 | 2 | 3 | 4 |

0 |  | 1, 3, 5, 7 | 0, 2, 4, 6, 16 |  | 8 |

1 |  |  |  |  |  |

2 | 4, 8, 9, 11 | 3, 5, 7 |  |  |  |

3 |  |  |  |  |  |

(b) Squares inscribed on degree four curves

Table 6: Number of squares inscribed on curves of degree three and four. The ( i, j) (i,j) -th cell corresponds to curves homeomorphic to i i copies of the real line and j j copies of the circle.

### 6.1 Topological types of curves with a possible parity condition on the number of inscribed squares

#### 6.1.1 One topological line inscribing an even number of squares

A straight line does not inscribe any squares. Among the curves computed for this thesis, all of the curves that consist of one topological component homeomorphic to the real line inscribe an even number of squares. Included are two examples of cubic curves inscribing the maximal number of twelve squares: Figure 22 \@vpageref []fig:twelve-clear and Figure 21(f) \@vpageref []fig:inscribed-oneZero-12-max. The other curves in Figure 21 \@vpageref []fig:inscribed-oneZero inscribe zero, two, four and six squares.

Curves that are homeomorphic to a real line but not neccessarily algebraic are not restricted by this parity condition of inscribing an even number of squares. Consider the curve, displayed in Figure 20 \@vpageref []fig:geo-zigzag, consisting of two parallel rays in opposite directions, connected by a line segment at a fortyfive degree angle to both the rays. This curve inscribes one square, it has the line segment B ​ C BC as a diagonal.

[image: Refer to caption] Figure 20: A topological line inscribing one square.

[image: Refer to caption] (a) Zero squares inscribed on f 1 f_{1} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Two squares inscribed on f 2 f_{2} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Four squares inscribed on f 3 f_{3} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (d) Six squares inscribed on f 4 f_{4} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (e) Six squares inscribed on f 5 f_{5} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (f) Twelve squares inscribed on f 6 f_{6} in Table 7 \@vpageref []tab:long-polys

Figure 21: An even number of squares inscribed on a line.[image: Refer to caption] Figure 22: Twelve squares inscribed on f 7 f_{7} in Table 7 \@vpageref []tab:long-polys

#### 6.1.2 Pairs of ovals inscribing an even number of squares

The curves in Figure 23 \@vpageref []fig:inscribed-zeroTwo consist of two ovals and inscribe zero, two, four, six and sixteen isolated squares. The curves in Figure 23(a) \@vpageref []fig:inscribed-zeroTwo-zero and Figure 23(e) \@vpageref []fig:inscribed-zeroTwo-sixteen are of the form ( X 2 + Y 2 / 4 − 1) ​ ( X 2 / 4 + Y 2 − 1) + k (X^{2}+Y^{2}/4-1)(X^{2}/4+Y^{2}-1)+k. If ( X, Y) (X,Y) lies on such a curve, then by symmetry it forms one corner of a square centered at the origin. The squares depicted in Figures 23(a) and 23(e) are the squares that do not lie on the positive-dimensional components of respectively 𝐕 ⁡ ( I f 41) \mathbf{V}(I_{f_{41}}) and 𝐕 ⁡ ( I f 45) \mathbf{V}(I_{f_{45}}).

[image: Refer to caption] (a) Zero squares inscribed on f 41 f_{41} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Two squares inscribed on f 42 f_{42} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Four squares inscribed on f 43 f_{43} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (d) Six squares inscribed on f 44 f_{44} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (e) Sixteen squares inscribed on f 45 f_{45} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (f) Up to rotational symmetry, four squares inscribed on f 45 f_{45}

Figure 23: Two ovals inscribing an even number of squares.

#### 6.1.3 An oval and two lines inscribing an odd number of squares

The curves in Figure 25 \@vpageref []fig:inscribed-twoOne inscribe an odd number of squares: three, five and seven.

[image: Refer to caption] (a) Three squares inscribed on f 34 f_{34} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Three squares inscribed on f 35 f_{35} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (a) Five squares inscribed on f 36 f_{36} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Seven squares inscribed on f 37 f_{37} in Table 7 \@vpageref []tab:long-polys

Figure 25: An oval and two lines inscribing an odd number of squares.

### 6.2 Topological types of curves lacking a parity condition on the number of inscribed squares

#### 6.2.1 Squares inscribed on one oval and one line

The curves in Figure 26 \@vpageref []fig:inscribed-oneOne inscribe one, two, three, five, seven, nine and eleven squares. Note that the curve in Figure 26(b) is reducible.

[image: Refer to caption] (a) One square inscribed on f 18 f_{18} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Two squares inscribed on f 19 f_{19} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Three squares inscribed on f 20 f_{20} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (d) Five squares inscribed on f 21 f_{21} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (e) Five squares inscribed on f 22 f_{22} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (f) Seven squares inscribed on f 23 f_{23} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (g) Seven squares inscribed on f 24 f_{24} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (h) Nine squares inscribed on f 25 f_{25} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (i) Eleven squares inscribed on f 26 f_{26} in Table 7 \@vpageref []tab:long-polys

Figure 26: Squares inscribed on an oval and a line.

#### 6.2.2 Squares inscribed on two lines

The curves in Figure 27 \@vpageref []fig:inscribed-twoZero inscribe one, four, eight, nine and eleven squares.

[image: Refer to caption] (a) One square inscribed on f 13 f_{13} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Four squares inscribed on f 14 f_{14} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Eight squares inscribed on f 15 f_{15} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (d) Nine squares inscribed on f 16 f_{16} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (e) Eleven squares inscribed on f 17 f_{17} in Table 7 \@vpageref []tab:long-polys

Figure 27: Squares inscribed on two lines.

#### 6.2.3 Squares inscribed on three lines

The curves in Figure 28 \@vpageref []fig:inscribed-threeZero inscribe one, four, seven, eight, ten and eleven squares. Figure 29 \@vpageref []fig:twelve-awesome depicts a third degree curve consisting of three lines inscribing the maximal number of twelve squares.

[image: Refer to caption] (a) One square inscribed on f 8 f_{8} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Four squares inscribed on f 9 f_{9} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Seven squares inscribed on f 10 f_{10} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (d) Eight squares inscribed on f 11 f_{11} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (e) Eight squares inscribed on f 38 f_{38} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (f) Ten squares inscribed on f 39 f_{39} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (g) Eleven squares inscribed on f 40 f_{40} in Table 7 \@vpageref []tab:long-polys

Figure 28: Squares inscribed on three lines.[image: Refer to caption] Figure 29: Twelve squares inscribed on f 12 f_{12} in Table 7 \@vpageref []tab:long-polys

#### 6.2.4 Squares inscribed on an oval and three lines

The curves in Figure 30 \@vpageref []fig:inscribed-threeOne inscribe eight, nine and eleven squares.

[image: Refer to caption] (a) Eight squares inscribed on f 27 f_{27} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (b) Nine squares inscribed on f 28 f_{28} in Table 7 \@vpageref []tab:long-polys

[image: Refer to caption] (c) Eleven squares inscribed on f 29 f_{29} in Table 7 \@vpageref []tab:long-polys

Figure 30: Squares inscribed on an oval and three lines.

## 7 Concluding remarks

The main result of this thesis, Theorem 4.8 in Section 4 \@vpageref []sec:upper-bound, shows that the number of isolated squares inscribed on a degree m m complex algebraic plane curve is at most ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4. The experimental evidence of Section 5 \@vpageref []sec:experimental suggests this statement might be strengthened to “a generic complex algebraic plane curve inscribes precisely ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4 squares”. Whether that is true or not, one can ask for any natural number m m what the maximum attainable number of isolated inscribed squares is on a curve of degree m m. Can we construct a curve that attains the theoretical maximum of ( m 4 − 5 ​ m 2 + 4 ​ m) / 4 (m^{4}-5m^{2}+4m)/4? At least up to degree five any of the curves of Table 4 \@vpageref []tab:experiments provides a positive answer, but we should aim for a theoretical argument for all degrees. Following Rojas [20, Section 3.3, p7], giving the conditions when the maximum number of solutions is attained might be fruitful. Intersection theory may also apply to show that the complex squares from Table 4 \@vpageref []tab:experiments have multiplicity one.

Restricting these questions to real plane curves we can ask again, is there a real algebraic plane curve that attains the bound of Theorem 4.8? Section 6 \@vpageref []sec:illustrative includes several positive examples for degree three.

Certain symmetries in a plane curve give rise to an infinite number of inscribed squares. The author is however not aware of a complete classification of which kinds of curves inscribe an infinitude of squares.

Based on the shaded cells of Table 5 \@vpageref []tab:square-topologies we could conjecture: Is it true that algebraic plane curves homeomorphic to one of

1. 1.

the real line

2. 2.

an oval and two lines

3. 3.

two ovals

inscribe respectively an even, odd, and even number of squares? The other shaded cell corresponds to algebraic Jordan curves, for which it is already known that this class of curves generically inscribes an odd number of squares.

Approximating a general Jordan curve with a subclass of curves for which we know Toeplitz’s conjecture to be true may fail to produce an inscribed square in the limit if the approximating squares degenerate to a point. Pak [18, Section 3.7] remarks that nonetheless the limit argument has its use; for an approximation argument by algebraic curves we will need to have control over the sizes of the squares to prevent the squares from degenerating in the limit.

## References

- [1] D. Bernshtein. The number of roots of a system of equations. Funct. Anal. Appl., 9(3):183–185, 1975.
- [2] B. Büeler, A. Enge and K. Fukuda. Exact volume computation for polytopes: A practical study. In G. Kalai and G. Ziegler, editors, Polytopes — Combinatorics and Computation, volume 29 of DMV Seminar, pages 131–154. Birkhäuser Basel, 2000.
- [3] D. Cox, J. Little and D. O’Shea. Using algebraic geometry, volume 185 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1998.
- [4] D. Cox, J. Little and D. O’Shea. Ideals, varieties, and algorithms: An introduction to computational algebraic geometry and commutative algebra. Undergraduate Texts in Mathematics. Springer, New York, third edition, 2007.
- [5] H. G. Eggleston. Figures inscribed in convex sets. Amer. Math. Monthly, 65(2):76–80, 1958.
- [6] D. Eisenbud. Commutative algebra: With a view toward algebraic geometry, volume 150 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1995.
- [7] A. Emch. Some properties of closed convex curves in a plane. Amer. J. Math., 35(4):407–412, 1913.
- [8] A. Emch. On some properties of the medians of closed continuous curves formed by analytic arcs. Amer. J. Math., 38(1):6–18, 1916.
- [9] D. R. Grayson and M. E. Stillman. Macaulay2 version 1.6, a software system for research in algebraic geometry. Available at [http://www.math.uiuc.edu/Macaulay2/][1].
- [10] E. Gross, S. Petrović and J. Verschelde. Interfacing with PHCpack. J. Softw. Algebra Geom., 5:20–25, 2013.
- [11] D. A. Gudkov. The topology of real projective algebraic varieties. Russian Math. Surveys, 29(4):1–79, Aug. 1974.
- [12] B. Huber and B. Sturmfels. Bernstein’s theorem in affine space. Discrete Comput. Geom., 17(2):137–141, 1997.
- [13] R. P. Jerrard. Inscribed squares in plane curves. Trans. Amer. Math. Soc., 98:234–241, 1961.
- [14] B. Matschke. A survey on the Square Peg Problem. Notices Amer. Math. Soc., 61(4):346–352, 2014.
- [15] M. D. Meyerson. Balancing acts. In The Proceedings of the 1981 Topology Conference (Blacksburg, Va., 1981), volume 6, pages 59–75 (1982), 1981.
- [16] M. J. Nielsen. Triangles inscribed in simple closed curves. Geom. Dedicata, 43(3):291–297, 1992.
- [17] I. Pak. Lectures on Discrete and Polyhedral Geometry. Book in progress, accessed March 2014. Available at [http://www.math.ucla.edu/~pak/book.htm][2].
- [18] I. Pak. The discrete square peg problem, 2008, arXiv:0804.0657. preprint, 10pp.
- [19] S. G. Popvassilev. On the number of inscribed squares of a simple closed curve in the plane, 2008, arXiv:0810.4806. preprint, 5pp.
- [20] J. M. Rojas. Toric intersection theory for affine root counting. J. Pure Appl. Algebra, 136(1):67–100, 1999.
- [21] M. Safey El Din. RAGlib version 3.21, a Maple package for real solving polynomial systems of equations and inequalities. Available at [http://www-polsys.lip6.fr/~safey/RAGLib/][3].
- [22] F. Sagols and R. Marín. The inscribed square conjecture in the digital plane. In Combinatorial image analysis, volume 5852 of Lecture Notes in Comput. Sci., pages 411–424. Springer, Berlin, 2009.
- [23] R. Schneider. Convex bodies: the Brunn-Minkowski theory, volume 44 of Encyclopedia of Mathematics and its Applications. Cambridge University Press, Cambridge, 1993.
- [24] F. Sottile. From enumerative geometry to solving systems of polynomials equations. In Computations in algebraic geometry with Macaulay 2, volume 8 of Algorithms Comput. Math., pages 101–129. Springer, Berlin, 2002.
- [25] P. Stein. Classroom Notes: A note on the volume of a simplex. Amer. Math. Monthly, 73(3):299–301, 1966.
- [26] W. Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika, 36(2):187–197 (1990), 1989.
- [27] G. M. Ziegler. Lectures on polytopes, volume 152 of Graduate Texts in Mathematics. Springer-Verlag, New York, 1995.

## Appendix

### Table of polynomials

Table 7: Polynomials defining curves in Section 6 \@vpageref []sec:illustrative.

f 1 f_{1} | ( 3 / 8) ​ x 3 + 4 ​ x 2 ​ y + ( 10 / 7) ​ x ​ y 2 + ( 2 / 7) ​ y 3 + x 2 + 10 ​ x ​ y + ( 7 / 9) ​ y 2 + ( 1 / 7) ​ x + ( 4 / 5) ​ y + 10369 / 300 \scriptstyle(3/8)x^{3}+4x^{2}y+(10/7)xy^{2}+(2/7)y^{3}+x^{2}+10xy+(7/9)y^{2}+(1/7)x+(4/5)y+10369/300 |

f 2 f_{2} | − ( 1013346057932523458320374654611 / 2350924922880000000000) ​ x 3 + ( 2584640714944881315625401696659 / 1959104102400000000000) ​ x 2 ​ y − ( 24370961833016176942717940959039 / 58773123072000000000000) ​ x ​ y 2 + ( 495964933561657788423357606871 / 489776025600000000000) ​ y 3 − ( 17651791649159643199956179410837 / 23509249228800000000000) ​ x 2 + ( 255915596711949314264306252576989 / 117546246144000000000000) ​ x ​ y − ( 5664920610070897911630510019033 / 653034700800000000000) ​ y 2 − ( 45022793169990743253008147707121 / 11754624614400000000000) ​ x + ( 659705135608555410904182133087481 / 58773123072000000000000) ​ y + 12665836021084318920971168631593 / 11754624614400000000000 \scriptstyle-(1013346057932523458320374654611/2350924922880000000000)x^{3}+(2584640714944881315625401696659/1959104102400000000000)x^{2}y-(24370961833016176942717940959039/58773123072000000000000)xy^{2}+(495964933561657788423357606871/489776025600000000000)y^{3}-(17651791649159643199956179410837/23509249228800000000000)x^{2}+(255915596711949314264306252576989/117546246144000000000000)xy-(5664920610070897911630510019033/653034700800000000000)y^{2}-(45022793169990743253008147707121/11754624614400000000000)x+(659705135608555410904182133087481/58773123072000000000000)y+12665836021084318920971168631593/11754624614400000000000 |

f 3 f_{3} | ( 1 / 7) ​ x 5 + ( 6 / 7) ​ x 4 ​ y + ( 9 / 5) ​ x 3 ​ y 2 + x 2 ​ y 3 + 7 ​ x ​ y 4 + 10 ​ y 5 + x 4 + ( 4 / 5) ​ x 3 ​ y + ( 10 / 7) ​ x 2 ​ y 2 + 3 ​ x ​ y 3 + ( 7 / 5) ​ y 4 + ( 7 / 6) ​ x 3 + ( 1 / 8) ​ x 2 ​ y + ( 3 / 4) ​ x ​ y 2 + ( 1 / 3) ​ y 3 + ( 3 / 10) ​ x 2 + ( 4 / 5) ​ x ​ y + ( 5 / 3) ​ y 2 + ( 5 / 3) ​ x + ( 10 / 9) ​ y + 9 / 4 \scriptstyle(1/7)x^{5}+(6/7)x^{4}y+(9/5)x^{3}y^{2}+x^{2}y^{3}+7xy^{4}+10y^{5}+x^{4}+(4/5)x^{3}y+(10/7)x^{2}y^{2}+3xy^{3}+(7/5)y^{4}+(7/6)x^{3}+(1/8)x^{2}y+(3/4)xy^{2}+(1/3)y^{3}+(3/10)x^{2}+(4/5)xy+(5/3)y^{2}+(5/3)x+(10/9)y+9/4 |

f 4 f_{4} | ( 1 / 2) ​ x 3 + 5 ​ x 2 ​ y + ( 2 / 9) ​ x ​ y 2 + ( 5 / 6) ​ y 3 + ( 9 / 7) ​ x 2 + 9 ​ x ​ y + ( 1 / 9) ​ y 2 + ( 7 / 5) ​ x + ( 10 / 9) ​ y + 5 / 6 \scriptstyle(1/2)x^{3}+5x^{2}y+(2/9)xy^{2}+(5/6)y^{3}+(9/7)x^{2}+9xy+(1/9)y^{2}+(7/5)x+(10/9)y+5/6 |

f 5 f_{5} | ( 1 / 3) ​ x 3 + x 2 ​ y + ( 7 / 9) ​ x ​ y 2 + 9 ​ y 3 + ( 10 / 9) ​ x 2 + 2 ​ x ​ y + ( 7 / 2) ​ y 2 + ( 8 / 7) ​ x + ( 1 / 10) ​ y + 1 / 3 \scriptstyle(1/3)x^{3}+x^{2}y+(7/9)xy^{2}+9y^{3}+(10/9)x^{2}+2xy+(7/2)y^{2}+(8/7)x+(1/10)y+1/3 |

f 6 f_{6} | ( 3 / 8) ​ x 3 + 4 ​ x 2 ​ y + ( 10 / 7) ​ x ​ y 2 + ( 2 / 7) ​ y 3 + x 2 + 10 ​ x ​ y + ( 7 / 9) ​ y 2 + ( 1 / 7) ​ x + ( 4 / 5) ​ y − 19 / 600 \scriptstyle(3/8)x^{3}+4x^{2}y+(10/7)xy^{2}+(2/7)y^{3}+x^{2}+10xy+(7/9)y^{2}+(1/7)x+(4/5)y-19/600 |

f 7 f_{7} | ( 32357486150754911 / 3402639576000000) ​ x 3 − ( 14565996465296101997 / 2143662932880000000) ​ x 2 ​ y + ( 93487619285326211413 / 135050764771440000000) ​ x ​ y 2 + ( 295881163208333 / 837368333156250) ​ y 3 − \scriptstyle(32357486150754911/3402639576000000)x^{3}-(14565996465296101997/2143662932880000000)x^{2}y+(93487619285326211413/135050764771440000000)xy^{2}+(295881163208333/837368333156250)y^{3}-
( 16455993365369237399 / 1071831466440000000) ​ x 2 \scriptstyle(16455993365369237399/1071831466440000000)x^{2}
+ ( 2262751792681121895697 / 270101529542880000000) ​ x ​ y \scriptstyle+(2262751792681121895697/270101529542880000000)xy
− ( 44377450778015156987 / 16881345596430000000) ​ y 2 \scriptstyle-(44377450778015156987/16881345596430000000)y^{2}
+ ( 483511249013004548209 / 90033843180960000000) ​ x \scriptstyle+(483511249013004548209/90033843180960000000)x
+ ( 43079601667153982323 / 33762691192860000000) ​ y − 9025382297117723393 / 11254230397620000000 \scriptstyle+(43079601667153982323/33762691192860000000)y-9025382297117723393/11254230397620000000 |

f 8 f_{8} | ( 4 / 3) ​ x 5 + 7 ​ x 4 ​ y + ( 7 / 3) ​ x 3 ​ y 2 + ( 1 / 2) ​ x 2 ​ y 3 + ( 1 / 2) ​ x ​ y 4 + ( 1 / 10) ​ y 5 + ( 10 / 7) ​ x 4 + ( 7 / 3) ​ x 3 ​ y + ( 2 / 5) ​ x 2 ​ y 2 + ( 2 / 3) ​ x ​ y 3 + ( 5 / 9) ​ y 4 + ( 3 / 2) ​ x 3 + 3 ​ x 2 ​ y + x ​ y 2 + ( 1 / 3) ​ y 3 + 4 ​ x 2 + ( 2 / 3) ​ x ​ y + ( 8 / 9) ​ y 2 + ( 8 / 3) ​ x + ( 1 / 10) ​ y + 7 / 5 \scriptstyle(4/3)x^{5}+7x^{4}y+(7/3)x^{3}y^{2}+(1/2)x^{2}y^{3}+(1/2)xy^{4}+(1/10)y^{5}+(10/7)x^{4}+(7/3)x^{3}y+(2/5)x^{2}y^{2}+(2/3)xy^{3}+(5/9)y^{4}+(3/2)x^{3}+3x^{2}y+xy^{2}+(1/3)y^{3}+4x^{2}+(2/3)xy+(8/9)y^{2}+(8/3)x+(1/10)y+7/5 |

f 9 f_{9} | ( 84600046159243700856114369758453 / 7304069487211315200000000) ​ x 3 + ( 84129864593783714477250895601927 / 4869379658140876800000000) ​ x 2 ​ y − ( 92678186386758381841697632332217 / 7304069487211315200000000) ​ x ​ y 2 − ( 985032890300878882041984922489 / 2921627794884526080000000) ​ y 3 − ( 8432107925141586913574285861810083 / 97387593162817536000000000) ​ x 2 − ( 42810357305315843166329246331701 / 1803473947459584000000000) ​ x ​ y + ( 798870306331587087351224027449571 / 58432555897690521600000000) ​ y 2 + ( 841046078607802229000433529244096647 / 5258930030792146944000000000) ​ x − ( 50130881628172999018538048620781701 / 5258930030792146944000000000) ​ y − 120544249950526645232049562396939597 / 1752976676930715648000000000 \scriptstyle(84600046159243700856114369758453/7304069487211315200000000)x^{3}+(84129864593783714477250895601927/4869379658140876800000000)x^{2}y-(92678186386758381841697632332217/7304069487211315200000000)xy^{2}-(985032890300878882041984922489/2921627794884526080000000)y^{3}-(8432107925141586913574285861810083/97387593162817536000000000)x^{2}-(42810357305315843166329246331701/1803473947459584000000000)xy+(798870306331587087351224027449571/58432555897690521600000000)y^{2}+(841046078607802229000433529244096647/5258930030792146944000000000)x-(50130881628172999018538048620781701/5258930030792146944000000000)y-120544249950526645232049562396939597/1752976676930715648000000000 |

f 10 f_{10} | ( 17071630870821024280289 / 127253121732748247040000000) ​ x 3 + ( 44219727353738152825699 / 5302213405531176960000000) ​ x 2 ​ y − ( 4775926187801988597243641 / 127253121732748247040000000) ​ x ​ y 2 + ( 2615354993498783429179 / 108208436847575040000000) ​ y 3 − ( 218792069736804757977449 / 38955037265127014400000000) ​ x 2 + ( 303432548905886033642387 / 6362656086637412352000000) ​ x ​ y − ( 15987089135911642991445653 / 381759365198244741120000000) ​ y 2 − ( 86769535959101859196900919 / 7635187303964894822400000000) ​ x + ( 1265378561015612782058837 / 61081498431719158579200000) ​ y − 2225833681103904456175739 / 763518730396489482240000000 \scriptstyle(17071630870821024280289/127253121732748247040000000)x^{3}+(44219727353738152825699/5302213405531176960000000)x^{2}y-(4775926187801988597243641/127253121732748247040000000)xy^{2}+(2615354993498783429179/108208436847575040000000)y^{3}\phantom{breakheregoddamnit}-(218792069736804757977449/38955037265127014400000000)x^{2}+(303432548905886033642387/6362656086637412352000000)xy-(15987089135911642991445653/381759365198244741120000000)y^{2}-(86769535959101859196900919/7635187303964894822400000000)x+(1265378561015612782058837/61081498431719158579200000)y-2225833681103904456175739/763518730396489482240000000 |

f 11 f_{11} | − ( 107666602244268965505153 / 34359738368000000000000) ​ x 3 + ( 244020905347080929848137 / 13743895347200000000000) ​ x 2 ​ y + ( 3029447197152010641168729 / 34359738368000000000000) ​ x ​ y 2 − ( 2494391888436262290669501 / 68719476736000000000000) ​ y 3 − ( 6731424554769315405645039 / 1374389534720000000000000) ​ x 2 − ( 1119679636867415864847621 / 4294967296000000000000) ​ x ​ y − ( 88162122657769201785657501 / 1374389534720000000000000) ​ y 2 + ( 1720365306508271453007846519 / 13743895347200000000000000) ​ x + ( 5145387047581092010866673443 / 13743895347200000000000000) ​ y − 676235828568952472903449101 / 3435973836800000000000000 \scriptstyle-(107666602244268965505153/34359738368000000000000)x^{3}+(244020905347080929848137/13743895347200000000000)x^{2}y\phantom{breakheregoddamnit}+(3029447197152010641168729/34359738368000000000000)xy^{2}-(2494391888436262290669501/68719476736000000000000)y^{3}\phantom{breakheregoddamnit}-(6731424554769315405645039/1374389534720000000000000)x^{2}-(1119679636867415864847621/4294967296000000000000)xy\phantom{breakheregoddamnit}-(88162122657769201785657501/1374389534720000000000000)y^{2}+(1720365306508271453007846519/13743895347200000000000000)x+(5145387047581092010866673443/13743895347200000000000000)y-676235828568952472903449101/3435973836800000000000000 |

f 12 f_{12} | − ( 4963493942513921243 / 65548320768000000) ​ x 3 + ( 326139891975237682121 / 1123685498880000000) ​ x 2 ​ y − ( 50931413248303191071 / 299649466368000000) ​ x ​ y 2 − ( 14263797412722377 / 339738624000000) ​ y 3 + ( 37805850432694119373 / 327741603840000000) ​ x 2 − ( 19179033623835553860379 / 31463193968640000000) ​ x ​ y + ( 1018795941059176616167 / 1997663109120000000) ​ y 2 + ( 1330205416456247598397 / 10487731322880000000) ​ x − ( 2843296777056554250263 / 13983641763840000000) ​ y + 95073566433481051 / 5202247680000000 \scriptstyle-(4963493942513921243/65548320768000000)x^{3}+(326139891975237682121/1123685498880000000)x^{2}y-(50931413248303191071/299649466368000000)xy^{2}-(14263797412722377/339738624000000)y^{3}+(37805850432694119373/327741603840000000)x^{2}\phantom{breakheregoddamnit}-(19179033623835553860379/31463193968640000000)xy\phantom{breakheregoddamnit}+(1018795941059176616167/1997663109120000000)y^{2}\phantom{breakheregoddamnit}+(1330205416456247598397/10487731322880000000)x\phantom{breakheregoddamnit}-(2843296777056554250263/13983641763840000000)y+95073566433481051/5202247680000000 |

f 13 f_{13} | 12415 ​ x 8 + 11377 ​ x 7 ​ y + 15240 ​ x 6 ​ y 2 − 451 ​ x 5 ​ y 3 + 4672 ​ x 4 ​ y 4 + 4256 ​ x 3 ​ y 5 + 2937 ​ x 2 ​ y 6 − 14392 ​ x ​ y 7 − 11440 ​ y 8 − 1118 ​ x 7 + 8649 ​ x 6 ​ y + 9988 ​ x 5 ​ y 2 + 15342 ​ x 4 ​ y 3 − 13207 ​ x 3 ​ y 4 + 4533 ​ x 2 ​ y 5 + 13680 ​ x ​ y 6 + 9917 ​ y 7 − 8343 ​ x 6 − 6757 ​ x 5 ​ y − 8308 ​ x 4 ​ y 2 + 7606 ​ x 3 ​ y 3 + 3138 ​ x 2 ​ y 4 − 5358 ​ x ​ y 5 + 11848 ​ y 6 + 12694 ​ x 5 + 181 ​ x 4 ​ y + 3136 ​ x 3 ​ y 2 − 12922 ​ x 2 ​ y 3 − 14700 ​ x ​ y 4 + 9107 ​ y 5 + 9973 ​ x 4 + 1173 ​ x 3 ​ y − 15433 ​ x 2 ​ y 2 + 2406 ​ x ​ y 3 − 13196 ​ y 4 − 8485 ​ x 3 − 8414 ​ x 2 ​ y − 15263 ​ x ​ y 2 + 15206 ​ y 3 − 7714 ​ x 2 − 7243 ​ x ​ y + 4230 ​ y 2 − 10183 ​ x + 5303 ​ y − 3662 \scriptstyle 12415x^{8}+11377x^{7}y+15240x^{6}y^{2}-451x^{5}y^{3}+4672x^{4}y^{4}+4256x^{3}y^{5}+2937x^{2}y^{6}-14392xy^{7}-11440y^{8}-1118x^{7}+8649x^{6}y+9988x^{5}y^{2}+15342x^{4}y^{3}-13207x^{3}y^{4}+4533x^{2}y^{5}+13680xy^{6}+9917y^{7}-8343x^{6}-6757x^{5}y-8308x^{4}y^{2}+7606x^{3}y^{3}+3138x^{2}y^{4}-5358xy^{5}+11848y^{6}+12694x^{5}+181x^{4}y+3136x^{3}y^{2}-12922x^{2}y^{3}-14700xy^{4}+9107y^{5}+9973x^{4}+1173x^{3}y-15433x^{2}y^{2}+2406xy^{3}-13196y^{4}-8485x^{3}-8414x^{2}y-15263xy^{2}+15206y^{3}-7714x^{2}-7243xy+4230y^{2}-10183x+5303y-3662 |

f 14 f_{14} | ( 10 / 9) ​ x 4 + ( 2 / 7) ​ x 3 ​ y + 2 ​ x 2 ​ y 2 + 5 ​ x ​ y 3 + ( 10 / 7) ​ y 4 + 5 ​ x 3 + ( 10 / 3) ​ x 2 ​ y + ( 2 / 5) ​ x ​ y 2 + ( 1 / 7) ​ y 3 + ( 1 / 2) ​ x 2 + ( 10 / 9) ​ x ​ y + ( 3 / 2) ​ y 2 + ( 1 / 7) ​ x + ( 5 / 9) ​ y + 4 \scriptstyle(10/9)x^{4}+(2/7)x^{3}y+2x^{2}y^{2}+5xy^{3}+(10/7)y^{4}+5x^{3}+(10/3)x^{2}y+(2/5)xy^{2}+(1/7)y^{3}+(1/2)x^{2}+(10/9)xy+(3/2)y^{2}+(1/7)x+(5/9)y+4 |

f 15 f_{15} | ( 1 / 4) ​ x 4 + 5 ​ x 3 ​ y + ( 5 / 3) ​ x 2 ​ y 2 + ( 1 / 10) ​ x ​ y 3 + ( 1 / 9) ​ y 4 + x 3 + ( 2 / 3) ​ x 2 ​ y + 9 ​ x ​ y 2 + ( 1 / 8) ​ y 3 + ( 7 / 10) ​ x 2 + ( 1 / 5) ​ x ​ y + ( 4 / 5) ​ y 2 + ( 4 / 5) ​ x + ( 5 / 8) ​ y + 3 / 10 \scriptstyle(1/4)x^{4}+5x^{3}y+(5/3)x^{2}y^{2}+(1/10)xy^{3}+(1/9)y^{4}+x^{3}+(2/3)x^{2}y+9xy^{2}+(1/8)y^{3}+(7/10)x^{2}+(1/5)xy+(4/5)y^{2}+(4/5)x+(5/8)y+3/10 |

f 16 f_{16} | ( 1 / 4) ​ x 4 + 5 ​ x 3 ​ y + ( 5 / 3) ​ x 2 ​ y 2 + ( 1 / 10) ​ x ​ y 3 + ( 1 / 9) ​ y 4 + x 3 + ( 2 / 3) ​ x 2 ​ y + 9 ​ x ​ y 2 + ( 1 / 8) ​ y 3 + ( 7 / 10) ​ x 2 + ( 1 / 5) ​ x ​ y + ( 4 / 5) ​ y 2 + ( 4 / 5) ​ x + ( 5 / 8) ​ y − 97 / 10 \scriptstyle(1/4)x^{4}+5x^{3}y+(5/3)x^{2}y^{2}+(1/10)xy^{3}+(1/9)y^{4}+x^{3}+(2/3)x^{2}y+9xy^{2}+(1/8)y^{3}+(7/10)x^{2}+(1/5)xy+(4/5)y^{2}+(4/5)x+(5/8)y-97/10 |

f 17 f_{17} | ( 1 / 4) ​ x 4 + 5 ​ x 3 ​ y + ( 5 / 3) ​ x 2 ​ y 2 + ( 1 / 10) ​ x ​ y 3 + ( 1 / 9) ​ y 4 + x 3 + ( 2 / 3) ​ x 2 ​ y + 9 ​ x ​ y 2 + ( 1 / 8) ​ y 3 + ( 7 / 10) ​ x 2 + ( 1 / 5) ​ x ​ y + ( 4 / 5) ​ y 2 + ( 4 / 5) ​ x + ( 5 / 8) ​ y − 27 / 10 \scriptstyle(1/4)x^{4}+5x^{3}y+(5/3)x^{2}y^{2}+(1/10)xy^{3}+(1/9)y^{4}+x^{3}+(2/3)x^{2}y+9xy^{2}+(1/8)y^{3}+(7/10)x^{2}+(1/5)xy+(4/5)y^{2}+(4/5)x+(5/8)y-27/10 |

f 18 f_{18} | − x 3 + y 2 + x \scriptstyle-x^{3}+y^{2}+x |

f 19 f_{19} | − ( 1 / 5) ​ x 3 + x 2 ​ y − ( 1 / 5) ​ x ​ y 2 + y 3 + ( 8 / 5) ​ x ​ y − 8 ​ y 2 − ( 12 / 5) ​ x + 12 ​ y + 1 / 100 \scriptstyle-(1/5)x^{3}+x^{2}y-(1/5)xy^{2}+y^{3}+(8/5)xy-8y^{2}-(12/5)x+12y+1/100 |

f 20 f_{20} | ( 3 / 8) ​ x 3 + 4 ​ x 2 ​ y + ( 10 / 7) ​ x ​ y 2 + ( 2 / 7) ​ y 3 + x 2 + 10 ​ x ​ y + ( 7 / 9) ​ y 2 + ( 1 / 7) ​ x + ( 4 / 5) ​ y + 1687 / 300 \scriptstyle(3/8)x^{3}+4x^{2}y+(10/7)xy^{2}+(2/7)y^{3}+x^{2}+10xy+(7/9)y^{2}+(1/7)x+(4/5)y+1687/300 |

f 21 f_{21} | ( 4 / 9) ​ x 3 + ( 10 / 7) ​ x 2 ​ y + x ​ y 2 + ( 3 / 4) ​ y 3 + ( 7 / 2) ​ x 2 + 8 ​ x ​ y + ( 4 / 7) ​ y 2 + ( 4 / 3) ​ x + ( 1 / 2) ​ y + 5 / 7 \scriptstyle(4/9)x^{3}+(10/7)x^{2}y+xy^{2}+(3/4)y^{3}+(7/2)x^{2}+8xy+(4/7)y^{2}+(4/3)x+(1/2)y+5/7 |

f 22 f_{22} | ( 1 / 4) ​ x 5 + 2 ​ x 4 ​ y + ( 8 / 5) ​ x 3 ​ y 2 + ( 7 / 6) ​ x 2 ​ y 3 + ( 2 / 9) ​ x ​ y 4 + ( 1 / 2) ​ y 5 + ( 3 / 5) ​ x 4 + 8 ​ x 3 ​ y + 5 ​ x 2 ​ y 2 + ( 9 / 5) ​ x ​ y 3 + 2 ​ y 4 + ( 7 / 10) ​ x 3 + 7 ​ x 2 ​ y + 9 ​ x ​ y 2 + 2 ​ y 3 + 3 ​ x 2 + 4 ​ x ​ y + ( 10 / 9) ​ y 2 + ( 10 / 3) ​ x + ( 1 / 4) ​ y + 1 / 3 \scriptstyle(1/4)x^{5}+2x^{4}y+(8/5)x^{3}y^{2}+(7/6)x^{2}y^{3}+(2/9)xy^{4}+(1/2)y^{5}+(3/5)x^{4}+8x^{3}y+5x^{2}y^{2}+(9/5)xy^{3}+2y^{4}+(7/10)x^{3}+7x^{2}y+9xy^{2}+2y^{3}+3x^{2}+4xy+(10/9)y^{2}+(10/3)x+(1/4)y+1/3 |

f 23 f_{23} | ( 8 / 3) ​ x 3 + ( 7 / 8) ​ x 2 ​ y + ( 1 / 5) ​ x ​ y 2 + ( 1 / 2) ​ y 3 + ( 1 / 2) ​ x 2 + 8 ​ x ​ y + 6 ​ y 2 + ( 5 / 4) ​ x + 5 ​ y + 1 / 5 \scriptstyle(8/3)x^{3}+(7/8)x^{2}y+(1/5)xy^{2}+(1/2)y^{3}+(1/2)x^{2}+8xy+6y^{2}+(5/4)x+5y+1/5 |

f 24 f_{24} | ( 1 / 5) ​ x 3 + x 2 ​ y + ( 7 / 4) ​ x ​ y 2 + ( 4 / 5) ​ y 3 + ( 9 / 7) ​ x 2 + 10 ​ x ​ y + 7 ​ y 2 + 2 ​ x + ( 7 / 10) ​ y + 5 / 8 \scriptstyle(1/5)x^{3}+x^{2}y+(7/4)xy^{2}+(4/5)y^{3}+(9/7)x^{2}+10xy+7y^{2}+2x+(7/10)y+5/8 |

f 25 f_{25} | ( 1 / 2) ​ x 3 + ( 3 / 2) ​ x 2 ​ y + 2 ​ x ​ y 2 + ( 2 / 9) ​ y 3 + x 2 + 9 ​ x ​ y + ( 3 / 2) ​ y 2 + ( 6 / 7) ​ x + ( 2 / 3) ​ y + 5 / 4 \scriptstyle(1/2)x^{3}+(3/2)x^{2}y+2xy^{2}+(2/9)y^{3}+x^{2}+9xy+(3/2)y^{2}+(6/7)x+(2/3)y+5/4 |

f 26 f_{26} | ( 3 / 8) ​ x 3 + 4 ​ x 2 ​ y + ( 10 / 7) ​ x ​ y 2 + ( 2 / 7) ​ y 3 + x 2 + 10 ​ x ​ y + ( 7 / 9) ​ y 2 + ( 1 / 7) ​ x + ( 4 / 5) ​ y + 1 / 3 \scriptstyle(3/8)x^{3}+4x^{2}y+(10/7)xy^{2}+(2/7)y^{3}+x^{2}+10xy+(7/9)y^{2}+(1/7)x+(4/5)y+1/3 |

f 27 f_{27} | ( 1 / 2) ​ x 5 + ( 9 / 4) ​ x 4 ​ y + ( 8 / 5) ​ x 3 ​ y 2 + ( 5 / 7) ​ x 2 ​ y 3 + ( 4 / 3) ​ x ​ y 4 + ( 1 / 8) ​ y 5 + ( 4 / 5) ​ x 4 + ( 2 / 5) ​ x 3 ​ y + ( 8 / 5) ​ x 2 ​ y 2 + 7 ​ x ​ y 3 + ( 2 / 3) ​ y 4 + ( 5 / 8) ​ x 3 + ( 3 / 7) ​ x 2 ​ y + ( 9 / 7) ​ x ​ y 2 + ( 3 / 5) ​ y 3 + x 2 + ( 6 / 7) ​ x ​ y + ( 1 / 3) ​ y 2 + ( 1 / 2) ​ x + ( 5 / 2) ​ y − 4 / 3 \scriptstyle(1/2)x^{5}+(9/4)x^{4}y+(8/5)x^{3}y^{2}+(5/7)x^{2}y^{3}+(4/3)xy^{4}+(1/8)y^{5}+(4/5)x^{4}+(2/5)x^{3}y+(8/5)x^{2}y^{2}+7xy^{3}+(2/3)y^{4}+(5/8)x^{3}+(3/7)x^{2}y+(9/7)xy^{2}+(3/5)y^{3}+x^{2}+(6/7)xy+(1/3)y^{2}+(1/2)x+(5/2)y-4/3 |

f 28 f_{28} | ( 1 / 2) ​ x 5 + ( 9 / 4) ​ x 4 ​ y + ( 8 / 5) ​ x 3 ​ y 2 + ( 5 / 7) ​ x 2 ​ y 3 + ( 4 / 3) ​ x ​ y 4 + ( 1 / 8) ​ y 5 + ( 4 / 5) ​ x 4 + ( 2 / 5) ​ x 3 ​ y + ( 8 / 5) ​ x 2 ​ y 2 + 7 ​ x ​ y 3 + ( 2 / 3) ​ y 4 + ( 5 / 8) ​ x 3 + ( 3 / 7) ​ x 2 ​ y + ( 9 / 7) ​ x ​ y 2 + ( 3 / 5) ​ y 3 + x 2 + ( 6 / 7) ​ x ​ y + ( 1 / 3) ​ y 2 + ( 1 / 2) ​ x + ( 5 / 2) ​ y − 8 / 15 \scriptstyle(1/2)x^{5}+(9/4)x^{4}y+(8/5)x^{3}y^{2}+(5/7)x^{2}y^{3}+(4/3)xy^{4}+(1/8)y^{5}+(4/5)x^{4}+(2/5)x^{3}y+(8/5)x^{2}y^{2}+7xy^{3}+(2/3)y^{4}+(5/8)x^{3}+(3/7)x^{2}y+(9/7)xy^{2}+(3/5)y^{3}+x^{2}+(6/7)xy+(1/3)y^{2}+(1/2)x+(5/2)y-8/15 |

f 29 f_{29} | ( 1 / 2) ​ x 5 + ( 9 / 4) ​ x 4 ​ y + ( 8 / 5) ​ x 3 ​ y 2 + ( 5 / 7) ​ x 2 ​ y 3 + ( 4 / 3) ​ x ​ y 4 + ( 1 / 8) ​ y 5 + ( 4 / 5) ​ x 4 + ( 2 / 5) ​ x 3 ​ y + ( 8 / 5) ​ x 2 ​ y 2 + 7 ​ x ​ y 3 + ( 2 / 3) ​ y 4 + ( 5 / 8) ​ x 3 + ( 3 / 7) ​ x 2 ​ y + ( 9 / 7) ​ x ​ y 2 + ( 3 / 5) ​ y 3 + x 2 + ( 6 / 7) ​ x ​ y + ( 1 / 3) ​ y 2 + ( 1 / 2) ​ x + ( 5 / 2) ​ y + 461 / 750 \scriptstyle(1/2)x^{5}+(9/4)x^{4}y+(8/5)x^{3}y^{2}+(5/7)x^{2}y^{3}+(4/3)xy^{4}+(1/8)y^{5}+(4/5)x^{4}+(2/5)x^{3}y+(8/5)x^{2}y^{2}+7xy^{3}+(2/3)y^{4}+(5/8)x^{3}+(3/7)x^{2}y+(9/7)xy^{2}+(3/5)y^{3}+x^{2}+(6/7)xy+(1/3)y^{2}+(1/2)x+(5/2)y+461/750 |

f 30 f_{30} | ( 7 / 9) ​ x 4 + ( 1 / 2) ​ x 3 ​ y + ( 7 / 6) ​ x 2 ​ y 2 + ( 4 / 5) ​ x ​ y 3 + ( 4 / 3) ​ y 4 + ( 2 / 7) ​ x 3 + ( 4 / 7) ​ x 2 ​ y + ( 8 / 3) ​ x ​ y 2 + ( 1 / 5) ​ y 3 + ( 7 / 10) ​ x 2 + ( 3 / 5) ​ x ​ y + ( 1 / 6) ​ y 2 + 5 ​ x + ( 5 / 7) ​ y + 3 / 10 \scriptstyle(7/9)x^{4}+(1/2)x^{3}y+(7/6)x^{2}y^{2}+(4/5)xy^{3}+(4/3)y^{4}+(2/7)x^{3}+(4/7)x^{2}y+(8/3)xy^{2}+(1/5)y^{3}+(7/10)x^{2}+(3/5)xy+(1/6)y^{2}+5x+(5/7)y+3/10 |

f 31 f_{31} | ( 3 / 10) ​ x 4 + ( 5 / 4) ​ x 3 ​ y + ( 7 / 5) ​ x 2 ​ y 2 + ( 1 / 5) ​ x ​ y 3 + y 4 + ( 9 / 10) ​ x 3 + 4 ​ x 2 ​ y + ( 2 / 9) ​ x ​ y 2 + y 3 + ( 3 / 4) ​ x 2 + ( 3 / 4) ​ x ​ y + y 2 + ( 1 / 2) ​ x + ( 9 / 2) ​ y + 9 / 8 \scriptstyle(3/10)x^{4}+(5/4)x^{3}y+(7/5)x^{2}y^{2}+(1/5)xy^{3}+y^{4}+(9/10)x^{3}+4x^{2}y+(2/9)xy^{2}+y^{3}+(3/4)x^{2}+(3/4)xy+y^{2}+(1/2)x+(9/2)y+9/8 |

f 32 f_{32} | 4 ​ x 4 + ( 1 / 2) ​ x 3 ​ y + ( 1 / 9) ​ x 2 ​ y 2 + 2 ​ x ​ y 3 + ( 9 / 7) ​ y 4 + 9 ​ x 3 + 5 ​ x 2 ​ y + ( 5 / 3) ​ x ​ y 2 + ( 4 / 3) ​ y 3 + ( 4 / 3) ​ x 2 + ( 5 / 2) ​ x ​ y + y 2 + ( 1 / 3) ​ x + ( 7 / 6) ​ y + 71 / 200 \scriptstyle 4x^{4}+(1/2)x^{3}y+(1/9)x^{2}y^{2}+2xy^{3}+(9/7)y^{4}+9x^{3}+5x^{2}y+(5/3)xy^{2}+(4/3)y^{3}+(4/3)x^{2}+(5/2)xy+y^{2}+(1/3)x+(7/6)y+71/200 |

f 33 f_{33} | 4 ​ x 4 + ( 1 / 2) ​ x 3 ​ y + ( 1 / 9) ​ x 2 ​ y 2 + 2 ​ x ​ y 3 + ( 9 / 7) ​ y 4 + 9 ​ x 3 + 5 ​ x 2 ​ y + ( 5 / 3) ​ x ​ y 2 + ( 4 / 3) ​ y 3 + ( 4 / 3) ​ x 2 + ( 5 / 2) ​ x ​ y + y 2 + ( 1 / 3) ​ x + ( 7 / 6) ​ y + 3 / 8 \scriptstyle 4x^{4}+(1/2)x^{3}y+(1/9)x^{2}y^{2}+2xy^{3}+(9/7)y^{4}+9x^{3}+5x^{2}y+(5/3)xy^{2}+(4/3)y^{3}+(4/3)x^{2}+(5/2)xy+y^{2}+(1/3)x+(7/6)y+3/8 |

f 34 f_{34} | ( 9 / 4) ​ x 4 + 3 ​ x 3 ​ y + ( 1 / 7) ​ x 2 ​ y 2 + ( 2 / 7) ​ x ​ y 3 + ( 1 / 3) ​ y 4 + ( 4 / 5) ​ x 3 + ( 1 / 5) ​ x 2 ​ y + 8 ​ x ​ y 2 + 4 ​ y 3 + 2 ​ x 2 + ( 10 / 9) ​ x ​ y + ( 5 / 3) ​ y 2 + ( 1 / 9) ​ x + ( 1 / 5) ​ y + 2 \scriptstyle(9/4)x^{4}+3x^{3}y+(1/7)x^{2}y^{2}+(2/7)xy^{3}+(1/3)y^{4}+(4/5)x^{3}+(1/5)x^{2}y+8xy^{2}+4y^{3}+2x^{2}+(10/9)xy+(5/3)y^{2}+(1/9)x+(1/5)y+2 |

f 35 f_{35} | ( 1 / 4) ​ x 4 + 5 ​ x 3 ​ y + ( 5 / 3) ​ x 2 ​ y 2 + ( 1 / 10) ​ x ​ y 3 + ( 1 / 9) ​ y 4 + x 3 + ( 2 / 3) ​ x 2 ​ y + 9 ​ x ​ y 2 + ( 1 / 8) ​ y 3 + ( 7 / 10) ​ x 2 + ( 1 / 5) ​ x ​ y + ( 4 / 5) ​ y 2 + ( 4 / 5) ​ x + ( 5 / 8) ​ y + 33 / 10 \scriptstyle(1/4)x^{4}+5x^{3}y+(5/3)x^{2}y^{2}+(1/10)xy^{3}+(1/9)y^{4}+x^{3}+(2/3)x^{2}y+9xy^{2}+(1/8)y^{3}+(7/10)x^{2}+(1/5)xy+(4/5)y^{2}+(4/5)x+(5/8)y+33/10 |

f 36 f_{36} | ( 1 / 5) ​ x 4 + ( 7 / 8) ​ x 3 ​ y + ( 1 / 2) ​ x 2 ​ y 2 + ( 5 / 4) ​ x ​ y 3 + y 4 + ( 1 / 3) ​ x 3 + x 2 ​ y + 8 ​ x ​ y 2 + y 3 + ( 3 / 4) ​ x 2 + ( 5 / 7) ​ x ​ y + ( 5 / 9) ​ y 2 + ( 9 / 8) ​ x + 5 ​ y + 4 / 3 \scriptstyle(1/5)x^{4}+(7/8)x^{3}y+(1/2)x^{2}y^{2}+(5/4)xy^{3}+y^{4}+(1/3)x^{3}+x^{2}y+8xy^{2}+y^{3}+(3/4)x^{2}+(5/7)xy+(5/9)y^{2}+(9/8)x+5y+4/3 |

f 37 f_{37} | ( 1 / 4) ​ x 4 + 5 ​ x 3 ​ y + ( 5 / 3) ​ x 2 ​ y 2 + ( 1 / 10) ​ x ​ y 3 + ( 1 / 9) ​ y 4 + x 3 + ( 2 / 3) ​ x 2 ​ y + 9 ​ x ​ y 2 + ( 1 / 8) ​ y 3 + ( 7 / 10) ​ x 2 + ( 1 / 5) ​ x ​ y + ( 4 / 5) ​ y 2 + ( 4 / 5) ​ x + ( 5 / 8) ​ y + 13 / 10 \scriptstyle(1/4)x^{4}+5x^{3}y+(5/3)x^{2}y^{2}+(1/10)xy^{3}+(1/9)y^{4}+x^{3}+(2/3)x^{2}y+9xy^{2}+(1/8)y^{3}+(7/10)x^{2}+(1/5)xy+(4/5)y^{2}+(4/5)x+(5/8)y+13/10 |

f 38 f_{38} | ( 1 / 7) ​ x 3 + ( 7 / 2) ​ x 2 ​ y + ( 7 / 3) ​ x ​ y 2 + ( 1 / 10) ​ y 3 + ( 6 / 7) ​ x 2 + 9 ​ x ​ y + ( 1 / 2) ​ y 2 + ( 7 / 5) ​ x + y + 1 \scriptstyle(1/7)x^{3}+(7/2)x^{2}y+(7/3)xy^{2}+(1/10)y^{3}+(6/7)x^{2}+9xy+(1/2)y^{2}+(7/5)x+y+1 |

f 39 f_{39} | ( 1 / 8) ​ x 3 + x 2 ​ y + 2 ​ x ​ y 2 + ( 1 / 6) ​ y 3 + ( 6 / 7) ​ x 2 + 9 ​ x ​ y + ( 7 / 9) ​ y 2 + ( 1 / 9) ​ x + ( 2 / 9) ​ y + 8 / 5 \scriptstyle(1/8)x^{3}+x^{2}y+2xy^{2}+(1/6)y^{3}+(6/7)x^{2}+9xy+(7/9)y^{2}+(1/9)x+(2/9)y+8/5 |

f 40 f_{40} | ( 1 / 10) ​ x 3 + ( 7 / 6) ​ x 2 ​ y + ( 9 / 7) ​ x ​ y 2 + ( 1 / 8) ​ y 3 + ( 9 / 4) ​ x 2 + 10 ​ x ​ y + 2 ​ y 2 + 5 ​ x + ( 3 / 4) ​ y + 1 / 6 \scriptstyle(1/10)x^{3}+(7/6)x^{2}y+(9/7)xy^{2}+(1/8)y^{3}+(9/4)x^{2}+10xy+2y^{2}+5x+(3/4)y+1/6 |

f 41 f_{41} | ( 1 / 4) ​ x 4 + ( 17 / 16) ​ x 2 ​ y 2 + ( 1 / 4) ​ y 4 − ( 5 / 4) ​ x 2 − ( 5 / 4) ​ y 2 + 4382 / 7225 \scriptstyle(1/4)x^{4}+(17/16)x^{2}y^{2}+(1/4)y^{4}-(5/4)x^{2}-(5/4)y^{2}+4382/7225 |

f 42 f_{42} | 4 ​ x 4 + ( 1 / 2) ​ x 3 ​ y + ( 1 / 9) ​ x 2 ​ y 2 + 2 ​ x ​ y 3 + ( 9 / 7) ​ y 4 + 9 ​ x 3 + 5 ​ x 2 ​ y + ( 5 / 3) ​ x ​ y 2 + ( 4 / 3) ​ y 3 + ( 4 / 3) ​ x 2 + ( 5 / 2) ​ x ​ y + y 2 + ( 1 / 3) ​ x + ( 7 / 6) ​ y + 7 / 8 \scriptstyle 4x^{4}+(1/2)x^{3}y+(1/9)x^{2}y^{2}+2xy^{3}+(9/7)y^{4}+9x^{3}+5x^{2}y+(5/3)xy^{2}+(4/3)y^{3}+(4/3)x^{2}+(5/2)xy+y^{2}+(1/3)x+(7/6)y+7/8 |

f 43 f_{43} | 4 ​ x 4 + ( 1 / 2) ​ x 3 ​ y + ( 1 / 9) ​ x 2 ​ y 2 + 2 ​ x ​ y 3 + ( 9 / 7) ​ y 4 + 9 ​ x 3 + 5 ​ x 2 ​ y + ( 5 / 3) ​ x ​ y 2 + ( 4 / 3) ​ y 3 + ( 4 / 3) ​ x 2 + ( 5 / 2) ​ x ​ y + y 2 + ( 1 / 3) ​ x + ( 7 / 6) ​ y + 27 / 40 \scriptstyle 4x^{4}+(1/2)x^{3}y+(1/9)x^{2}y^{2}+2xy^{3}+(9/7)y^{4}+9x^{3}+5x^{2}y+(5/3)xy^{2}+(4/3)y^{3}+(4/3)x^{2}+(5/2)xy+y^{2}+(1/3)x+(7/6)y+27/40 |

f 44 f_{44} | 4 ​ x 4 + ( 1 / 2) ​ x 3 ​ y + ( 1 / 9) ​ x 2 ​ y 2 + 2 ​ x ​ y 3 + ( 9 / 7) ​ y 4 + 9 ​ x 3 + 5 ​ x 2 ​ y + ( 5 / 3) ​ x ​ y 2 + ( 4 / 3) ​ y 3 + ( 4 / 3) ​ x 2 + ( 5 / 2) ​ x ​ y + y 2 + ( 1 / 3) ​ x + ( 7 / 6) ​ y + 19 / 40 \scriptstyle 4x^{4}+(1/2)x^{3}y+(1/9)x^{2}y^{2}+2xy^{3}+(9/7)y^{4}+9x^{3}+5x^{2}y+(5/3)xy^{2}+(4/3)y^{3}+(4/3)x^{2}+(5/2)xy+y^{2}+(1/3)x+(7/6)y+19/40 |

f 45 f_{45} | ( 1 / 4) ​ x 4 + ( 17 / 16) ​ x 2 ​ y 2 + ( 1 / 4) ​ y 4 − ( 5 / 4) ​ x 2 − ( 5 / 4) ​ y 2 + 40453 / 43350 \scriptstyle(1/4)x^{4}+(17/16)x^{2}y^{2}+(1/4)y^{4}-(5/4)x^{2}-(5/4)y^{2}+40453/43350 |

### Code

Listing 1: minvol.m2 -- Calculate the Minkowski volume -- of m*P1 + l*P2 + g*Delta for degree k R = QQ[k, e_1..e_2, m_1..m_2][l_1..l_4] K = (m_1 + m_2 + l_4)*k L = (m_1*e_1 + m_2*e_2) M = (l_4 + m_1)*k + m_2*(k - 1) Vol = (K - L)^3 * (K + 3*L) - (K - M)^3 * (K + 3*M) volToMvol = (substitutions) -> ( vol := sub(Vol, substitutions); Mvol := (last coefficients (vol, Monomials => {l_1*l_2*l_3*l_4}))_0_0; Mvol = Mvol/4!; -- Compensate for the volume of the standard simplex assert (Mvol == k^4 - 5*k^2 + 4*k); -- Confirm we got the answer we expect return Mvol;) -- When k is even there is one copy of P1 (even monomials) and two of -- P2 (odd monomials) and the other way around when k is odd. ({m_1 => l_1, m_2 => l_2 + l_3, e_1 => 2, e_2 => 1}, {m_1 => l_2 + l_3, m_2 => l_1, e_1 => 1, e_2 => 2}) / volToMvol

Listing 2: lowDegreeBKK.m2 -- For m=2, 3 the polytopes do not have their general shape (and -- aren’t full dimensional either). However, the Minkowski sum / -- mixed volume calculation still makes sense. So just do that for -- these special cases. needsPackage "PHCpack" -- m = 2 case g4 = (a^2 + b^2 + c^2 + d^2 + 1) g1 = (c^2 + d^2) g2 = (c + d)*(1 + a + b) mv = mixedVolume {g1, g2, g2, g4} assert (mv == 2^4 - 5*2^2 + 4*2) -- m = 3 case R = CC[a, b, c, d] P4 = newtonPolytope g4 = (a^3 + b^3 + c^3 + d^3 + 1) g1 = ((c^2 + d^2)*(1 + a + b)) g2 = ((c + d)*(1 + a^2 + b^2) + (c^3 + d^3)) mv = mixedVolume {g1, g2, g2, g4} assert (mv == 3^4 - 5*3^2 + 4*3)

Listing 3: numevidIdeal.m2 -- Numerical evidence for sharp BKK bound via degree counting. S = QQ; load "preamble.m2"; D = 3; degreeSetup(D) H = new MutableHashTable from {} coeffs = unique toList apply(1..100, i -> randomCoefficients_D()); curves = coeffs / (c -> sub(abstractCurve_D, c)); fillIn_countSquares_H curves tally values H

Listing 4: poging3.m2 S = QQ; load "preamble.m2"; D = 3; degreeSetup(D) use ring abstractCurve_D monomialTerms = terms sub(abstractCurve_D, validDegrees_D / (i -> C_i => 1)) curveThroughPoints = (N) -> ( use ring abstractCurve_D; planePoints := toList(apply(1..N, i -> (random(S), random(S)))); M := matrix ( {monomialTerms} | (planePoints / (p -> monomialTerms / (t -> sub(t, {X => p_0, Y => p_1}))))); return determinant M;); H = new MutableHashTable from {}; curves = toList select(apply(1..20, i -> curveThroughPoints(9)), c -> 0 != c) fillIn_(realSolutions_D @@ curveToCoeff_D)_H curves pairs H / last / length tally oo

Listing 5: preamble.m2 load "realroots.m2" needsPackage "PHCpack" W = S[a, b, c, d, MonomialSize => 8]; excess = ideal(c, d); PHCring = CC[a, b, c, d]; sparseCoeffs = (coeff, localD) -> ( H := new HashTable from coeff; -- Poor mans dict.update(H) return for deg in (validDegrees_localD / (d -> C_d)) list (if H#?deg then (deg => H#deg) else (deg => 0));); zerofy = (squares) -> ( squares / (square -> for x in square list if abs(x) < 1.0e-15 then 0.0 else x))); filterReal = (solutions) -> ( return select(solutions / coordinates, j -> all(j, i -> 1.0e-90 > abs imaginaryPart i)) / (s -> s / realPart);); forMaple = (D, coeff, solss) -> ( bounds := {"-10..10", "-10..10"}; if length solss > 0 then ( sols := solss / toList; Xen := flatten(sols / (s -> {s_0 + s_2, s_0 - s_2, s_0 + s_3, s_0 - s_3} )); Yen := flatten(sols / (s -> {s_1 + s_2, s_1 - s_2, s_1 + s_3, s_1 - s_3} )); bounds = (Xen, Yen) / (l -> toString floor(-2 + min l) | ".." | toString ceiling(2 + max l));) else ( sols = [];); return "plotSquaresOnCurve" | toString ("(X, Y) -> " | toString sub(abstractCurve_D, coeff), " [X=" | bounds_0 | ", Y=" | bounds_1 | ", gridrefine=4] ", replace("\\}|\\)", "]", replace("\\{|\\(", "[", toString sols))) | ";";); forMapleSimple = (curve, squares) -> ( return "plotSquaresOnCurve((X, Y) -> " | toString curve | ", opts, " | replace("\\}|\\)", "]", replace("\\{|\\(", "[", toString squares)) |")\n";); forMapleSequence = (curves, solutions) -> ( assert(length curves == length solutions); contentS := toString(toList( apply(0..length(curves) - 1, i -> forMapleSimple(curves_i, solutions_i)))); return "opts := []; display(" | contentS | ", insequence=true);";); forMapleArray = (curves, solutions) -> ( assert(length curves == length solutions); contentS := toString(toList( apply(0..length(curves) - 1, i -> forMapleSimple(curves_i, solutions_i)))); return "opts := []; display(Array([[" | contentS | "]], transpose));";); fillIn = (work, H, curves) -> ( for curve in curves do ( if not H #? curve then ( result := work curve; H # curve = result;) else ( print ("Curve " | toString curve | " already present");););); countSquares = (curve) -> ( I := time saturate(makeIdeal_D curveToCoeff_D curve, excess); return (dim I, degree I);); degreeSetup = (D) -> ( validDegrees_D = select(toList( set toList(0..D))^**2 / toList, d -> sum(d) <= D); R_D = S[apply(validDegrees_D, d -> C_d), MonomialSize => 8][a, b, c, d, MonomialSize => 8]; T_D = R_D[X, Y]; curveToCoeff_D = (curve) -> ( sparseCoeffs(terms curve / (j -> C_(first exponents j) => leadCoefficient j), D);); use T_D; abstractCurve_D = sum(validDegrees_D / (d -> C_d * X^(d_0) * Y^(d_1))); use R_D; corners_D = {{ X => a + c, Y => b + d }, { X => a - c, Y => b - d }, { X => a + d, Y => b - c }, { X => a - d, Y => b + c }} / (corner -> sub(abstractCurve_D, corner)); IJ_D = ideal( corners_D_0 + corners_D_1 - corners_D_2 - corners_D_3, corners_D_0 - corners_D_1, corners_D_2 - corners_D_3, corners_D_3); -- FIXME: doing the saturation here is perhaps the wrong point. -- On the other hand, if we can store this computation, it might speed -- things up. randomCoefficients_D = () -> ( return apply(validDegrees_D, s -> C_s => random(S))); makeIdeal_D = (coeff) -> ( use W; I := sub(sub(IJ_D, coeff), W); J := I; return J;); realSolutions_D = (coeff) -> ( IP := sub(makeIdeal_D(coeff), PHCring); use PHCring; -- this is done to avoid the "key not found" complexSols := solveSystem IP_*; sols := unique zerofy filterReal complexSols; squares := select(sols, s -> s_2 >= 0 and s_3 > 0); if (length sols != 4 * length squares) then ( print("Mismatch in solutions and squares " | toString (length sols, length squares)); sols = unique zerofy filterReal refineSolutions(IP_*, complexSols, 18); squares = sort select(sols, s -> s_2 >= 0 and s_3 > 0);); return squares);)

Listing 6: drawSquares.mw with(plots): with(plottools): with(RAGMaple): SquarePegs:=module() option package; export plotSquare, plotSquaresOnCurve, componentsPoints; local colorList; componentsPoints := (curve) -> ( seq(point([rhs(P[1]), rhs(P[2])]), P in PointsPerComponents([ curve = 0 ], [X, Y]))); plotSquare := proc(param, kleur) local a, b, c, d, p1, p2, p3, p4, line1, line2, line3, line4, plotOpts; (a, b, c, d) := op(param); plotOpts := thickness=2, color=kleur; p1 := [a + c, b + d]: p2 := [a - d, b + c]: p3 := [a - c, b - d]: p4 := [a + d, b - c]: display(CURVES([p1, p2, p3, p4, p1]), plotOpts): end proc: colorList := [navy, orange, plum, cyan, blue, green, black, maroon, gold, brown, pink, coral, magenta, khaki]; plotSquaresOnCurve := proc(curve, curveOpts, squares, showComponents::boolean := true, showLegend::boolean := true) local curvePlot, squaresPlot, setopts, xsX, ysY, passOpts, plotList, componentPoints; setopts := [seq(lhs(o), o in curveOpts)]; passOpts := curveOpts; if evalb(showComponents) then componentPoints := [seq( [rhs(P[1]), rhs(P[2])], P in PointsPerComponents([curve(X, Y) = 0], [X, Y]))]; else componentPoints := []; end if; if evalb(not X in setopts) then xsX := ListTools[Flatten]( [seq([s[1] + s[3], s[1] + s[4], s[1] - s[3], s[1] - s[4]], s in squares)]); passOpts := [op(passOpts), X=-1+floor(min(xsX, seq( P[1], P in componentPoints)))..1 +ceil(max(xsX, seq(P[1], P in componentPoints)))]; end if; if evalb(not Y in setopts) then ysY := ListTools[Flatten]([seq( [s[2] + s[3], s[2] + s[4], s[2] - s[3], s[2] - s[4]], s in squares)]); passOpts := [op(passOpts), Y=-1+floor(min(ysY, seq( P[2], P in componentPoints)))..1 +ceil(max(ysY, seq(P[2], P in componentPoints)))]; end if; if evalb(not gridrefine in setopts) then passOpts := [op(passOpts), gridrefine=4]; end if; if evalb(showLegend) then curvePlot := implicitplot(curve(X, Y) = 0, op(passOpts), color=red, caption=typeset(curve(x, y), " inscribing ", nops(squares), " squares.")): else curvePlot := implicitplot(curve(X, Y) = 0, op(passOpts), color=red): end if; squaresPlot := [seq(plotSquare(squares[1 + i], colorList[1 + (i mod nops(colorList))]), i=0..nops(squares) - 1)]: if evalb(showComponents) then plotList := [curvePlot, op(squaresPlot), seq(point(P), P in componentPoints)]; else plotList := [curvePlot, op(squaresPlot)]; end if; display(plotList, scaling=constrained): end proc: end module:

[◄][4][image: ar5iv homepage] [5]
[Feeling lucky?][6] [7]
[Conversion report][8]
[Report an issue][9]
[View original on arXiv][10] [►][11]


## Links

[1]: http://www.math.uiuc.edu/Macaulay2/
[2]: http://www.math.ucla.edu/~pak/book.htm
[3]: http://www-polsys.lip6.fr/~safey/RAGLib/
[4]: /html/1403.5978
[5]: /
[6]: /feeling_lucky
[7]: /land_of_honey_and_milk
[8]: /log/1403.5979
[9]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1403.5979
[10]: https://arxiv.org/pdf/1403.5979
[11]: /html/1403.5980
