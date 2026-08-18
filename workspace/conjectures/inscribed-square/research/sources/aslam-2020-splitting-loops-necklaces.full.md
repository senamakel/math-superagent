<!-- source: https://ar5iv.labs.arxiv.org/html/1806.02484 | converted from HTML -->

[1806.02484] Splitting loops and necklaces: Variants of the square peg problem

# Splitting loops and necklaces:
Variants of the square peg problem

Jai Aslam, Shujian Chen, Florian Frick, Sam Saloff-Coste,
Linus Setiabrata, and Hugh Thomas JA, SC Dept. Math., Northeastern University, Boston, MA 02115, USA Email address: [{aslam.j, chen.shuj}@husky.neu.edu][1] FF, SSC, LS Dept. Math., Cornell University, Ithaca, NY 14853, USA Email address: [{ff238, sps247, ls823}@cornell.edu][2] HT Math. Dept., Université du Québec á Montréal, Canada Email address: [thomas.hugh_r@uqam.ca][3]

Date: August 9, 2026

###### Abstract.

Toeplitz conjectured that any simple planar loop inscribes a square. Here we prove variants of Toeplitz’ square peg problem. We prove Hadwiger’s 1971 conjecture that any simple loop in 3 3 -space inscribes a parallelogram. We show that any simple planar loop inscribes sufficiently many rectangles that their vertices are dense in the loop (independently due to Schwartz). If the loop is rectifiable, there is a rectangle that cuts the loop into four pieces that can be rearranged to form two loops of equal length. A rectifiable loop in d d -space can be cut into ( r − 1) ​ ( d + 1) + 1 (r-1)(d+1)+1 pieces that can be rearranged by translations to form r r loops of equal length. We relate our results to fair divisions of necklaces in the sense of Alon and to Tverberg-type results. This provides a new approach and a common framework to obtain variants of Toeplitz’ square peg problem for the class of all continuous curves.

## 1. Introduction

Toeplitz [31] conjectured that an embedded continuous closed curve (a *loop*) in the plane *inscribes*a square, that is, it contains the four vertices of a square. This conjecture has been settled in several special cases, such as piecewise analytic curves (Emch [10]), C 2 C^{2} curves (Schnirelman [27], see also Guggenheimer [12]), C 1 C^{1} curves (Stromquist [29]), or homotopically nontrivial loops contained in certain annuli, and an open and dense class of curves (Matschke [21]); also see Matschke’s survey [22]. Recently, Tao [30] provided a novel approach to Toeplitz’ conjecture proving it for curves that arise as the union of two graphs of Lipschitz functions with Lipschitz constant less than one. Results for the class of all continuous closed curves are rare. It seems that the most general statements towards Toeplitz’ conjecture are that any loop inscribes a rhombus with two sides parallel to a given line (see Nielsen [25]) and that any loop inscribes a rectangle; this was proven by Vaughan, and the proof appears in Meyerson’s manuscript [24]. See also Pak’s book [26, Prop. 5.4] and Schwartz’ recent trichotomy of inscribed rectangles [28]. For additional very recent progress on special inscribed quadrilaterals see [1, 16, 23].

Nielsen’s result proceeds by approximating continuous curves by piecewise linear curves while certifying that the rhombus does not degenerate in this process. Similarly, Schwartz approximates loops by generic polygons. Vaughan’s result is particular to the case of inscribed rectangles and does not lend itself easily to proving variants. Here we describe a novel technique that proves relatives of Toeplitz’ conjecture for all continuous curves in the same generalized fashion without a need for approximation.

An important variant of the square peg problem is a 1971 conjecture of Hadwiger [14] that states that any loop in ℝ 3 \mathbb{R}^{3} inscribes a parallelogram. Guggenheimer [13] established this for C 2 C^{2} curves and Makeev [19] for C 1 C^{1} curves. Vrećica and Živaljević [33] develop a general proof method that also yields Hadwiger’s conjecture for C 1 C^{1} curves. In fact, all of these results establish the existence of an inscribed rhombus.

We relate inscribing special n n -gons into loops to results of fair division on the real line, such as the Hobby–Rice theorem in L 1 L^{1} approximation (see Theorem 2.1) as well as its generalizations. We prove the following results:

- •

Hadwiger’s conjecture holds: any simple loop in ℝ 3 \mathbb{R}^{3} inscribes a parallelogram. In fact, it inscribes so many parallelograms that the set of vertices is dense in the loop; see Theorem 2.4. Here we allow parallelograms that consist of four pairwise distinct points on a line and that are the limit of a sequence of parallelograms (so does Hadwiger).

- •

Any simple planar loop inscribes sufficiently many rectangles that the set of vertices is dense in the loop; see Theorem 2.6. Schwartz [28] recently and independently proved that all but at most four points of a loop are the vertices of a rectangle.

- •

Any rectifiable simple planar loop inscribes a rectangle that cuts the loop into four parts γ ( 1) \gamma^{(1)}, γ ( 2) \gamma^{(2)}, γ ( 3) \gamma^{(3)}, γ ( 4) \gamma^{(4)} in cyclic order such that the total length of γ ( 1) \gamma^{(1)} and γ ( 3) \gamma^{(3)} is equal to the total length of γ ( 2) \gamma^{(2)} and γ ( 4) \gamma^{(4)}; see Theorem 3.2.

- •

Any rectifiable loop in ℝ d \mathbb{R}^{d} can be cut into ( r − 1) ​ ( d + 1) + 1 (r-1)(d+1)+1 pieces that may be rearranged by translations to form r r loops of equal length; see Theorem 3.1.

- •

We prove a proper extension of Alon’s necklace splitting result [3] for divisions of the unit interval into a prime number of parts by applying the topological machinery of the optimal colored Tverberg theorem of Blagojević, Matschke, and Ziegler [7]; see Theorem 4.1. This allows us to prove a proper strengthening of Theorem 3.1 for primes r r; see Corollary 4.5.

## 2. Inscribing parallelograms and rectangles

We find it instructive to first discuss why any planar C 1 C^{1} loop inscribes a parallelogram with a prescribed vertex. This result follows easily from the Hobby–Rice theorem below. After deducing this special case, we will discuss how to obtain generalizations.

###### Theorem 2.1 (Hobby and Rice [15]).

Let μ \mu be a finite nonatomic real measure on [0, 1] [0,1]. Let f i: [0, 1] ⟶ ℝ {f_{i}\colon[0,1]\longrightarrow\mathbb{R}}, i = 1, …, n i=1,\dots,n, be functions in L 1 ​ ( d ​ μ) L^{1}(d\mu). Then there are points t i t_{i} with 0 = t 0 ≤ t 1 ≤ ⋯ ≤ t n ≤ t n + 1 = 1 0=t_{0}\leq t_{1}\leq\dots\leq t_{n}\leq t_{n+1}=1 such that

 | ∑ j = 1 n + 1 ( − 1) j ​ ∫ t j − 1 t j f i ​ ( t) ​ 𝑑 μ ​ ( t) = 0 for every ​ i = 1, …, n. \sum_{j=1}^{n+1}(-1)^{j}\int_{t_{j-1}}^{t_{j}}f_{i}(t)\ d\mu(t)=0\quad\text{for every}\ i=1,\dots,n. |  |

Let γ: [0, 1] ⟶ ℝ 2, t ↦ ( γ 1 ​ ( t), γ 2 ​ ( t)) \gamma\colon[0,1]\longrightarrow\mathbb{R}^{2},t\mapsto(\gamma_{1}(t),\gamma_{2}(t)) be a C 1 C^{1} loop in the plane. We note that

 | ∫ 0 1 γ i ′ ​ ( t) ​ 𝑑 t = γ i ​ ( 1) − γ i ​ ( 0) = 0 for ​ i = 1, 2. \int_{0}^{1}\gamma^{\prime}_{i}(t)\ dt=\gamma_{i}(1)-\gamma_{i}(0)=0\quad\text{for}\ i=1,2. |  |

The Hobby–Rice theorem implies that there are three points 0 ≤ a ≤ b ≤ c ≤ 1 0\leq a\leq b\leq c\leq 1 such that

 | ∫ 0 a | γ ′ ​ ( t) | ​ 𝑑 t + ∫ b c | γ ′ ​ ( t) | ​ 𝑑 t = ∫ a b | γ ′ ​ ( t) | ​ 𝑑 t + ∫ c 1 | γ ′ ​ ( t) | ​ 𝑑 t \int_{0}^{a}|\gamma^{\prime}(t)|\ dt+\int_{b}^{c}|\gamma^{\prime}(t)|\ dt=\int_{a}^{b}|\gamma^{\prime}(t)|\ dt+\int_{c}^{1}|\gamma^{\prime}(t)|\ dt |  | (1) |

and

 | ∫ 0 a γ i ′ ​ ( t) ​ 𝑑 t + ∫ b c γ i ′ ​ ( t) ​ 𝑑 t = ∫ a b γ i ′ ​ ( t) ​ 𝑑 t + ∫ c 1 γ i ′ ​ ( t) ​ 𝑑 t, \int_{0}^{a}\gamma^{\prime}_{i}(t)\ dt+\int_{b}^{c}\gamma^{\prime}_{i}(t)\ dt=\int_{a}^{b}\gamma^{\prime}_{i}(t)\ dt+\int_{c}^{1}\gamma^{\prime}_{i}(t)\ dt, |  |

which implies that both sides of this latter equation vanish. This implies that γ ⁡ ( a) − γ ⁡ ( 0) = γ ⁡ ( b) − γ ⁡ ( c) \gamma(a)-\gamma(0)=\gamma(b)-\gamma(c) and γ ⁡ ( b) − γ ⁡ ( a) = γ ⁡ ( c) − γ ⁡ ( 1) \gamma(b)-\gamma(a)=\gamma(c)-\gamma(1). This implies that the points γ ⁡ ( 0), γ ⁡ ( a), γ ⁡ ( b) \gamma(0),\gamma(a),\gamma(b), and γ ⁡ ( c) \gamma(c) describe a parallelogram inscribed into γ \gamma, where the vertex γ ⁡ ( 0) \gamma(0) was prescribed in advance. Equation ( 1) ensures that the parallelogram is non-degenerate.

The requirement that γ \gamma be continuously differentiable may be relaxed to γ \gamma being continuous since we differentiate γ \gamma and then integrate again. This will require a slight extension of the Hobby–Rice theorem. In fact, we will immediately prove a version that instead of splitting [0, 1] [0,1] into positive and negative subintervals, splits a partition of [0, 1] [0,1] into r r parts that equalize given functions on the intervals of each part. One such extension of the Hobby–Rice theorem is due to Alon [3]. The theorem below is a slight modification, but can be proven in a similar way. We also refer to the statement and proof in Matoušek’s book [20].

###### Theorem 2.2.

Let f 1, …, f m: [0, 1] ⟶ ℝ f_{1},\dots,f_{m}\colon[0,1]\longrightarrow\mathbb{R} be continuous functions. Let r ≥ 2 r\geq 2 be an integer, and set n = ( r − 1) ​ m {n=(r-1)m}. Then there are points 0 = t 0 ≤ t 1 ≤ ⋯ ≤ t n + 1 = 1 0=t_{0}\leq t_{1}\leq\dots\leq t_{n+1}=1 and a partition of the set [n + 1] [n+1] into subsets T 1, …, T r T_{1},\dots,T_{r} such that

 | ∑ j ∈ T 1 f k ( t j) − f k ( t j − 1) = ∑ j ∈ T 2 f k ( t j) − f k ( t j − 1) = ⋯ = ∑ j ∈ T r f k ( t j) − f k ( t j − 1), k = 1, …, m. \sum_{j\in T_{1}}f_{k}(t_{j})-f_{k}(t_{j-1})=\sum_{j\in T_{2}}f_{k}(t_{j})-f_{k}(t_{j-1})=\dots=\sum_{j\in T_{r}}f_{k}(t_{j})-f_{k}(t_{j-1}),\quad k=1,\dots,m. |  |

Alon’s theorem guarantees a fair splitting of measures μ 1, …, μ m \mu_{1},\dots,\mu_{m} on [0, 1] [0,1] that are continuous in the sense that ∫ 0 x d ​ μ k \int_{0}^{x}\ d\mu_{k} is continuous in x x. We recover this case by setting f k ​ ( x) = ∫ 0 x d ​ μ k f_{k}(x)=\int_{0}^{x}\ d\mu_{k}. The popular interpretation of Alon’s theorem is that r r thieves have stolen a necklace with m m kinds of beads, whose densities along the necklace are given by μ 1, …, μ m \mu_{1},\dots,\mu_{m}. Then the thieves can split the necklace with ( r − 1) ​ m (r-1)m cuts such that each thief receives an equal amount of each kind of bead.

We first need some notation before we can prove this result. By W r = { ( y 1, …, y r) ∈ ℝ r | ∑ y i = 0 } W_{r}=\{(y_{1},\dots,y_{r})\in\mathbb{R}^{r}\ |\ \sum y_{i}=0\} we denote the standard representation of the symmetric group S r S_{r}. For abstract simplicial complexes K K and L L on disjoint vertex sets denote their join by K ∗ L {K*L}, that is, the abstract simplicial complex whose faces are σ ∪ τ \sigma\cup\tau with σ ∈ K \sigma\in K and τ ∈ L \tau\in L. If we take the join of simplicial complexes whose vertex set is not disjoint to begin with, such as K ∗ K K*K, we first force the vertex sets to be disjoint. The r r -fold, deleted join of K K, denoted K Δ ∗ r K^{*r}_{\Delta}, is the subcomplex of the r r -fold join of K K, where unions of faces σ 1, …, σ r \sigma_{1},\dots,\sigma_{r} that were not pairwise disjoint to begin with have been deleted. We refer to Matoušek [20] for details. Given two topological spaces X X and Y Y with G G -actions, we call a continuous map f: X ⟶ Y f\colon X\longrightarrow Y equivariant (or G G -equivariant) if f ⁡ ( g ⋅ x) = g ⋅ f ⁡ ( x) f(g\cdot x)=g\cdot f(x) for all x ∈ X x\in X and g ∈ G {g\in G}.

Matoušek [20, Theorem 6.6.1] describes how points in the r r -fold deleted join ( Δ n) Δ ∗ r (\Delta_{n})^{*r}_{\Delta} of the n n -simplex Δ n \Delta_{n} correspond to n n points 0 ≤ t 1 ≤ ⋯ ≤ t n ≤ 1 0\leq t_{1}\leq\dots\leq t_{n}\leq 1 and partitions of [n + 1] [n+1] into r r parts. We describe an alternative way of seeing this parametrization in the proof below. It follows from a theorem of Dold [9] that for n = ( r − 1) ​ m n=(r-1)m and r r a prime, any S r S_{r} -equivariant map ( Δ n) Δ ∗ r ⟶ W r ⊕ m (\Delta_{n})^{*r}_{\Delta}\longrightarrow W_{r}^{\oplus m} must include the origin in its image; see [20, Corollary 6.4.4].

###### Proof of Theorem 2.2.

First let r ≥ 2 r\geq 2 be a prime. We will induct on the number of prime divisors in the end. We first describe how points in the r r -fold deleted join ( Δ n) Δ ∗ r (\Delta_{n})^{*r}_{\Delta} of an n n -simplex correspond to divisions of [0, 1] [0,1] into n + 1 n+1 (possibly empty) intervals, and a partition of those intervals into r r (possibly empty) parts. In the following we will identify the vertex set of Δ n \Delta_{n} with [n + 1] [n+1]. The simplicial complex ( Δ n) Δ ∗ r (\Delta_{n})^{*r}_{\Delta} consists of joins σ 1 ∗ ⋯ ∗ σ r \sigma_{1}*\dots*\sigma_{r} of r r pairwise disjoint faces σ i \sigma_{i} of the n n -simplex Δ n \Delta_{n}. A point in the geometric realization of σ 1 ∗ ⋯ ∗ σ r \sigma_{1}*\dots*\sigma_{r} corresponds to a convex combination λ 1 ​ x 1 + ⋯ + λ r ​ x r \lambda_{1}x_{1}+\dots+\lambda_{r}x_{r} of points x i ∈ σ i x_{i}\in\sigma_{i}. In particular, λ i ≥ 0 \lambda_{i}\geq 0 and ∑ λ i = 1 \sum\lambda_{i}=1.

Let λ 1 ​ x 1 + ⋯ + λ r ​ x r \lambda_{1}x_{1}+\dots+\lambda_{r}x_{r} be an arbitrary point in ( Δ n) Δ ∗ r (\Delta_{n})^{*r}_{\Delta}. We can think of the expression λ 1 ​ x 1 + ⋯ + λ r ​ x r \lambda_{1}x_{1}+\dots+\lambda_{r}x_{r} as a convex combination of points x i x_{i} in the simplex Δ n \Delta_{n}, and thus as a point x x in the standard n n -simplex Δ n = { ( x 0, …, x n) ∈ ℝ n + 1 | x i ≥ 0 ​ and ​ ∑ x i = 1 } \Delta_{n}=\{(x^{0},\dots,x^{n})\in\mathbb{R}^{n+1}\ |\ x^{i}\geq 0\ \text{and}\ \sum x^{i}=1\}. Such a point corresponds to a partition of [0, 1] [0,1] into the n + 1 n+1 intervals [0, x 0], [x 0, x 0 + x 1], …, [x 0 + ⋯ + x n − 1, 1] [0,x^{0}],[x^{0},x^{0}+x^{1}],\dots,[x^{0}+\dots+x^{n-1},1]. Let t j t_{j} denote x 0 + x 1 + ⋯ + x j − 1 x^{0}+x^{1}+\dots+x^{j-1} for j ∈ [n] j\in[n], t 0 = 0 t_{0}=0, and t n + 1 = 1 t_{n+1}=1. The point λ 1 ​ x 1 + ⋯ + λ r ​ x r \lambda_{1}x_{1}+\dots+\lambda_{r}x_{r} is in a join of pairwise disjoint faces σ 1 ∗ ⋯ ∗ σ r \sigma_{1}*\dots*\sigma_{r}, where σ i \sigma_{i} is the minimal supporting face of x i x_{i}. To split the n + 1 n+1 intervals into r r groups of intervals, let j ∈ [n + 1] j\in[n+1] be in T i T_{i} if and only if the j j th vertex of Δ n \Delta_{n} is contained in σ i \sigma_{i} and λ i > 0 \lambda_{i}>0. Notice that if j j is not contained in any T i T_{i}, then t j = t j − 1 t_{j}=t_{j-1} and we can add it to an arbitrary set T i T_{i}.

For each i ∈ { 1, …, r } i\in\{1,\dots,r\} define the continuous map

 | F i: ( Δ n) Δ ∗ r ⟶ ℝ m, λ 1 ​ x 1 + ⋯ + λ r ​ x r ↦ ( ∑ j ∈ T i f 1 ​ ( t j) − f 1 ​ ( t j − 1), …, ∑ j ∈ T i f m ​ ( t j) − f m ​ ( t j − 1)), F_{i}\colon(\Delta_{n})^{*r}_{\Delta}\longrightarrow\mathbb{R}^{m},\lambda_{1}x_{1}+\dots+\lambda_{r}x_{r}\mapsto\left(\sum_{j\in T_{i}}f_{1}(t_{j})-f_{1}(t_{j-1}),\dots,\sum_{j\in T_{i}}f_{m}(t_{j})-f_{m}(t_{j-1})\right), |  |

and define F: ( Δ n) Δ ∗ r ⟶ ( ℝ m) r F\colon(\Delta_{n})^{*r}_{\Delta}\longrightarrow(\mathbb{R}^{m})^{r} by F ⁡ ( x) = ( F 1 ​ ( x), …, F r ​ ( x)) F(x)=(F_{1}(x),\dots,F_{r}(x)). There is an action by the symmetric group S r S_{r} on ( Δ n) Δ ∗ r (\Delta_{n})^{*r}_{\Delta} that permutes copies of Δ n \Delta_{n}, and the map F F is equivariant with respect to this action, where S r S_{r} permutes the F i F_{i} accordingly.

Observe that if the theorem was false, then the image of F F would not map to the diagonal D = { ( y 1, …, y r) ∈ ( ℝ m) r | y 1 = ⋯ = y r } D=\{(y_{1},\dots,y_{r})\in(\mathbb{R}^{m})^{r}\ |\ y_{1}=\dots=y_{r}\}. Orthogonally projecting along the diagonal gives an equivariant map F ^: ( Δ n) Δ ∗ r ⟶ W r ⊕ m \widehat{F}\colon(\Delta_{n})^{*r}_{\Delta}\longrightarrow W_{r}^{\oplus m} that does not include the origin in its image. This is a contradiction to [20, Corollary 6.4.4].

It remains to be shown that if the statement of the theorem holds for r = q r=q and r = p r=p then it also holds for their product r = p ​ q r=pq. Let [a i, b i] ⊂ [0, 1] [a_{i},b_{i}]\subset[0,1], i ∈ [ℓ] i\in[\ell], be a collection of pairwise disjoint intervals. Denote their union by I = ⋃ i [a i, b i] I=\bigcup_{i}[a_{i},b_{i}]. Let f 1, …, f m: I ⟶ ℝ f_{1},\dots,f_{m}\colon I\longrightarrow\mathbb{R} be continuous functions with f k ​ ( b i) = f k ​ ( a i + 1) f_{k}(b_{i})=f_{k}(a_{i+1}) for all i ∈ [ℓ − 1] i\in[\ell-1] and all k ∈ [m] k\in[m]. Then the theorem holds in the same way for the functions f i f_{i}, since we can simply reparametrize to obtain continuous functions on all of [0, 1] [0,1].

Assume that we have shown the theorem for r = p r=p and r = q r=q. Now given continuous maps f 1, …, f m: [0, 1] ⟶ ℝ f_{1},\dots,f_{m}\colon[0,1]\longrightarrow\mathbb{R}, let n = ( p − 1) ​ m n=(p-1)m. Find points 0 = t 0 ≤ t 1 ≤ ⋯ ≤ t n + 1 = 1 0=t_{0}\leq t_{1}\leq\dots\leq t_{n+1}=1 and a partition of the set [n + 1] [n+1] into subsets T 1, …, T p T_{1},\dots,T_{p} such that

 | ∑ j ∈ T 1 f k ( t j) − f k ( t j − 1) = ∑ j ∈ T 2 f k ( t j) − f k ( t j − 1) = ⋯ = ∑ j ∈ T p f k ( t j) − f k ( t j − 1), k = 1, …, m. \sum_{j\in T_{1}}f_{k}(t_{j})-f_{k}(t_{j-1})=\sum_{j\in T_{2}}f_{k}(t_{j})-f_{k}(t_{j-1})=\dots=\sum_{j\in T_{p}}f_{k}(t_{j})-f_{k}(t_{j-1}),\quad k=1,\dots,m. |  |

The sum ∑ i = 1 p ∑ j ∈ T i f k ​ ( t j) − f k ​ ( t j − 1) \sum_{i=1}^{p}\sum_{j\in T_{i}}f_{k}(t_{j})-f_{k}(t_{j-1}) telescopes and is equal to f k ​ ( 1) − f k ​ ( 0) f_{k}(1)-f_{k}(0). Thus ∑ j ∈ T i f k ​ ( t j) − f k ​ ( t j − 1) = 1 p ​ ( f k ​ ( 1) − f k ​ ( 0)) \sum_{j\in T_{i}}f_{k}(t_{j})-f_{k}(t_{j-1})=\frac{1}{p}(f_{k}(1)-f_{k}(0)) for all i i and k k. Fix one set T i T_{i} and consider I = ⋃ j ∈ T i [t j − 1, t j] I=\bigcup_{j\in T_{i}}\ [t_{j-1},t_{j}]. Let y y be the left-most point in T i T_{i}, and let z z be the right-most point in T i T_{i}. Define h k: I ⟶ ℝ h_{k}\colon I\longrightarrow\mathbb{R} by h k ​ ( x) = f k ​ ( x) − f k ​ ( t j − 1) + ∑ f k ​ ( t s) − f k ​ ( t s − 1) h_{k}(x)=f_{k}(x)-f_{k}(t_{j-1})+\sum f_{k}(t_{s})-f_{k}(t_{s-1}) if x ∈ [t j − 1, t j] x\in[t_{j-1},t_{j}], where the sum is taken over all s ∈ T i s\in T_{i} with s < j s<j. The map h k h_{k} is defined precisely in such a way that the value of h k h_{k} at a right endpoint of an interval in I I is equal to its value at the successive left endpoint of an interval in I I. Thus we can now split the maps h 1, …, h m h_{1},\dots,h_{m} for r = q r=q. In this way we obtain a partition T 1 ′, …, T q ′ T^{\prime}_{1},\dots,T^{\prime}_{q} of [( q − 1) ​ m + 1] [(q-1)m+1] and points y = t 0 ′ ≤ t 1 ′ ≤ ⋯ ≤ t ( q − 1) ​ m + 1 ′ = z y=t^{\prime}_{0}\leq t^{\prime}_{1}\leq\dots\leq t^{\prime}_{(q-1)m+1}=z, t i ′ ∈ I t^{\prime}_{i}\in I for i ∈ [( q − 1) ​ m] i\in[(q-1)m], such that

 | ∑ j ∈ T 1 ′ h k ( t j ′) − h k ( t j − 1 ′) = ∑ j ∈ T 2 ′ h k ( t j ′) − h k ( t j − 1 ′) = ⋯ = ∑ j ∈ T q ′ h k ( t j ′) − h k ( t j − 1 ′), k = 1, …, m. \sum_{j\in T^{\prime}_{1}}h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1})=\sum_{j\in T^{\prime}_{2}}h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1})=\dots=\sum_{j\in T^{\prime}_{q}}h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1}),\quad k=1,\dots,m. |  |

The sum ∑ i = 1 q ∑ j ∈ T i ′ h k ​ ( t j ′) − h k ​ ( t j − 1 ′) \sum_{i=1}^{q}\sum_{j\in T^{\prime}_{i}}h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1}) is equal to h k ​ ( z) − h k ​ ( y) h_{k}(z)-h_{k}(y). By definition of h k h_{k} this is equal to ∑ j ∈ T i f k ​ ( t j) − f k ​ ( t j − 1) = 1 p ​ ( f k ​ ( 1) − f k ​ ( 0)) \sum_{j\in T_{i}}f_{k}(t_{j})-f_{k}(t_{j-1})=\frac{1}{p}(f_{k}(1)-f_{k}(0)). Thus ∑ j ∈ T i ′ h k ​ ( t j ′) − h k ​ ( t j − 1 ′) = 1 p ​ q ​ ( f k ​ ( 1) − f k ​ ( 0)) \sum_{j\in T^{\prime}_{i}}h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1})=\frac{1}{pq}(f_{k}(1)-f_{k}(0)) for all i i and k k. Now if t j − 1 ′ t^{\prime}_{j-1} and t j ′ t^{\prime}_{j} are in the same interval [t ℓ − 1, t ℓ] [t_{\ell-1},t_{\ell}], then h k ​ ( t j ′) − h k ​ ( t j − 1 ′) = f k ​ ( t j ′) − f k ​ ( t j − 1 ′) h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1})=f_{k}(t^{\prime}_{j})-f_{k}(t^{\prime}_{j-1}). Whereas if t j − 1 ′ ∈ [t λ − 1, t λ] t^{\prime}_{j-1}\in[t_{\lambda-1},t_{\lambda}] and t j ′ ∈ [t ℓ − 1, t ℓ] t^{\prime}_{j}\in[t_{\ell-1},t_{\ell}], then

 |  | h k ​ ( t j ′) − h k ​ ( t j − 1 ′) \displaystyle h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1}) |  |

 |  | = f k ​ ( t j ′) − f k ​ ( t ℓ − 1) + ( ∑ s < ℓ, s ∈ T i f k ​ ( t s) − f k ​ ( t s − 1)) − [f k ​ ( t j − 1 ′) − f k ​ ( t λ − 1) + ( ∑ s < λ, s ∈ T i f k ​ ( t s) − f k ​ ( t s − 1))] \displaystyle=f_{k}(t^{\prime}_{j})-f_{k}(t_{\ell-1})+\left(\sum_{s<\ell,s\in T_{i}}f_{k}(t_{s})-f_{k}(t_{s-1})\right)-\left[f_{k}(t^{\prime}_{j-1})-f_{k}(t_{\lambda-1})+\left(\sum_{s<\lambda,s\in T_{i}}f_{k}(t_{s})-f_{k}(t_{s-1})\right)\right] |  |

 |  | = f k ​ ( t j ′) − f k ​ ( t ℓ − 1) + ( ∑ λ ≤ s < ℓ, s ∈ T i f k ​ ( t s) − f k ​ ( t s − 1)) + f k ​ ( t j − 1 ′) − f k ​ ( t λ − 1). \displaystyle=f_{k}(t^{\prime}_{j})-f_{k}(t_{\ell-1})+\left(\sum_{\lambda\leq s<\ell,s\in T_{i}}f_{k}(t_{s})-f_{k}(t_{s-1})\right)+f_{k}(t^{\prime}_{j-1})-f_{k}(t_{\lambda-1}). |  |

Let T ′′ T^{\prime\prime} be the set of points { t 0, …, t n + 1, t 0 ′, …, t ( q − 1) ​ m + 1 ′ } \{t_{0},\dots,t_{n+1},t^{\prime}_{0},\dots,t^{\prime}_{(q-1)m+1}\}, and write t 0 ′′ < t 1 ′′ < ⋯ < t N ′′ t^{\prime\prime}_{0}<t^{\prime\prime}_{1}<\dots<t^{\prime\prime}_{N} for the points in T ′′ T^{\prime\prime}. Let T i ′′ ⊂ [N] T^{\prime\prime}_{i}\subset[N] be the set of indices corresponding to points in T i ′ T^{\prime}_{i} and for any pair of consecutive points in T i ′ T^{\prime}_{i} add those indices corresponding to all points of { t 0, …, t n + 1 } \{t_{0},\dots,t_{n+1}\} that are between them. Then by the above calculations

 | 1 p ​ q ​ ( f k ​ ( 1) − f k ​ ( 0)) = ∑ j ∈ T i ′ h k ​ ( t j ′) − h k ​ ( t j − 1 ′) = ∑ j ∈ T i ′′ f k ​ ( t j ′′) − f k ​ ( t j − 1 ′′). \frac{1}{pq}(f_{k}(1)-f_{k}(0))=\sum_{j\in T^{\prime}_{i}}h_{k}(t^{\prime}_{j})-h_{k}(t^{\prime}_{j-1})=\sum_{j\in T^{\prime\prime}_{i}}f_{k}(t^{\prime\prime}_{j})-f_{k}(t^{\prime\prime}_{j-1}). |  |

The total number of points required for this division is ( p − 1) ​ m + p ⁡ ( q − 1) ​ m = ( p ​ q − 1) ​ m (p-1)m+p(q-1)m=(pq-1)m. This completes the induction on prime divisors. ∎

For the reader who found the induction on the number of prime divisors in the proof above difficult to follow, we mention that we use Theorem 2.2 for all integers r ≥ 2 r\geq 2 only to show Theorem 3.1 in full generality. But the induction on prime divisors for this latter theorem is of much lower technical difficulty.

To prove results about inscribing parallelograms and rectangles we need a Hobby–Rice theorem for maps defined on the circle S 1 S^{1}. Consider the following first approximation to the desired result: For any m ≥ 2 m\geq 2 continuous maps f 1, …, f m: S 1 ⟶ ℝ f_{1},\dots,f_{m}\colon S^{1}\longrightarrow\mathbb{R} one can find m m points t 1, …, t m ∈ S 1 t_{1},\dots,t_{m}\in S^{1} and a partition T 1 ⊔ T 2 T_{1}\sqcup T_{2} of [m] [m] such that ∑ j ∈ T 1 f k ​ ( t j) − f k ​ ( t j − 1) = ∑ j ∈ T 2 f k ​ ( t j) − f k ​ ( t j − 1) \sum_{j\in T_{1}}f_{k}(t_{j})-f_{k}(t_{j-1})=\sum_{j\in T_{2}}f_{k}(t_{j})-f_{k}(t_{j-1}) for all k k. Here t 0 t_{0} denotes t m t_{m}. As stated this result trivially holds for t 1 = t 2 = ⋯ = t m t_{1}=t_{2}=\dots=t_{m}. To avoid this degeneracy we will cut the circle S 1 S^{1} open at an arbitrary point to obtain maps f i: [0, 1] ⟶ ℝ f_{i}\colon[0,1]\longrightarrow\mathbb{R}, and we will always require that at least one map, say f m f_{m}, satisfies f m ​ ( 0) ≠ f m ​ ( 1) f_{m}(0)\neq f_{m}(1), that is, f m f_{m} did not come from a map defined on S 1 S^{1}. Then the above theorem holds true if m m is even (and is false for odd m m by a degrees of freedom counting argument). We will mostly need the following special case:

###### Corollary 2.3.

Let f 1, …, f 4: [0, 1] ⟶ ℝ f_{1},\dots,f_{4}\colon[0,1]\longrightarrow\mathbb{R} be continuous functions. Then there are points 0 ≤ t 1 ≤ ⋯ ≤ t 4 ≤ 1 0\leq t_{1}\leq\dots\leq t_{4}\leq 1 such that

 | 2 ​ f k ​ ( t 1) + 2 ​ f k ​ ( t 3) + f k ​ ( 1) = 2 ​ f k ​ ( t 2) + 2 ​ f k ​ ( t 4) + f k ​ ( 0) for all ​ k. 2f_{k}(t_{1})+2f_{k}(t_{3})+f_{k}(1)=2f_{k}(t_{2})+2f_{k}(t_{4})+f_{k}(0)\quad\text{for all}\ k. |  |

###### Proof.

We use Theorem 2.2 with r = 2 r=2 and m = 4 m=4. This provides us with four points 0 ≤ t 1 ≤ ⋯ ≤ t 4 ≤ 1 0\leq t_{1}\leq\dots\leq t_{4}\leq 1 and a partition T 1 ⊔ T 2 T_{1}\sqcup T_{2} of [5] [5]. If T 1 = { 1, 3, 5 } T_{1}=\{1,3,5\} and T 2 = { 2, 4 } T_{2}=\{2,4\} (or vice versa) then the conclusion of Theorem 2.2 is equivalent to 2 ​ f k ​ ( t 1) + 2 ​ f k ​ ( t 3) + f k ​ ( 1) = 2 ​ f k ​ ( t 2) + 2 ​ f k ​ ( t 4) + f k ​ ( 0) 2f_{k}(t_{1})+2f_{k}(t_{3})+f_{k}(1)=2f_{k}(t_{2})+2f_{k}(t_{4})+f_{k}(0). For any other partition of [5] [5] at least one of the T i T_{i} has successive elements. Suppose j j and j + 1 j+1 are in T 1 T_{1} (say) and they are the largest successive pair of numbers in the same T i T_{i}. Swap j + 1 j+1 into T 2 T_{2}, j + 2 j+2 into T 1 T_{1}, and so on up to j + ℓ = 5 j+\ell=5. Call the new partition of [5] [5] obtained in this way T 1 ′ ⊔ T 2 ′ T^{\prime}_{1}\sqcup T^{\prime}_{2}. Forget the point t j t_{j} and reindex to get new points t i ′ t^{\prime}_{i} as follows: t 1 ′ = t 1, …, t j − 1 ′ = t j − 1 t^{\prime}_{1}=t_{1},\dots,t^{\prime}_{j-1}=t_{j-1}, t j ′ = t j + 1, …, t 3 ′ = t 4 t^{\prime}_{j}=t_{j+1},\dots,t^{\prime}_{3}=t_{4}, and t 4 ′ = 1 t^{\prime}_{4}=1. The equation ∑ j ∈ T 1 f k ​ ( t j) − f k ​ ( t j − 1) = ∑ j ∈ T 2 f k ​ ( t j) − f k ​ ( t j − 1) \sum_{j\in T_{1}}f_{k}(t_{j})-f_{k}(t_{j-1})=\sum_{j\in T_{2}}f_{k}(t_{j})-f_{k}(t_{j-1}) is equivalent to ∑ j ∈ T 1 ′ f k ​ ( t j ′) − f k ​ ( t j − 1 ′) = ∑ j ∈ T 2 ′ f k ​ ( t j ′) − f k ​ ( t j − 1 ′) \sum_{j\in T^{\prime}_{1}}f_{k}(t^{\prime}_{j})-f_{k}(t^{\prime}_{j-1})=\sum_{j\in T^{\prime}_{2}}f_{k}(t^{\prime}_{j})-f_{k}(t^{\prime}_{j-1}). So we can successively reduce to the case T 1 = { 1, 3, 5 } T_{1}=\{1,3,5\} and T 2 = { 2, 4 } T_{2}=\{2,4\}. ∎

We can now prove Hadwiger’s conjecture that any simple loop in ℝ 3 \mathbb{R}^{3} inscribes a parallelogram. In fact, any such loop inscribes many parallelograms: their vertex sets are dense in the image of the loop. We consider four pairwise distinct points on a line to be a parallelogram if they arise as the limit of a sequence of parallelograms, and Hadwiger [14] explicitly allows this.

###### Theorem 2.4.

Any simple loop γ: [0, 1] ⟶ ℝ 3 \gamma\colon[0,1]\longrightarrow\mathbb{R}^{3} inscribes sufficiently many parallelograms that their vertex sets are dense in γ ⁡ ( [0, 1]) \gamma([0,1]).

###### Proof.

Apply Corollary 2.3 to the coordinate functions γ 1, γ 2, γ 3 \gamma_{1},\gamma_{2},\gamma_{3}, of γ \gamma, and to the function

 | f ⁡ ( t) = { 0 if ​ t ∈ [0, x] 1 y − x ​ ( t − x) if ​ t ∈ [x, y] 1 if ​ t ∈ [y, 1] f(t)=\begin{cases}0&\text{ if }t\in[0,x]\\ \frac{1}{y-x}(t-x)&\text{ if }t\in[x,y]\\ 1&\text{ if }t\in[y,1]\end{cases} |  |

for a given interval [x, y] ⊂ [0, 1] [x,y]\subset[0,1]. Let 0 ≤ t 1 ≤ ⋯ ≤ t 4 ≤ 1 0\leq t_{1}\leq\dots\leq t_{4}\leq 1 be the points whose existence is guaranteed by Corollary 2.3.

Since γ \gamma is a loop, we have that γ ⁡ ( 0) = γ ⁡ ( 1) \gamma(0)=\gamma(1) and thus γ ⁡ ( t 1) + γ ⁡ ( t 3) = γ ⁡ ( t 2) + γ ⁡ ( t 4) \gamma(t_{1})+\gamma(t_{3})=\gamma(t_{2})+\gamma(t_{4}). So the points γ ⁡ ( t 1), …, γ ⁡ ( t 4) \gamma(t_{1}),\dots,\gamma(t_{4}) form a (possibly degenerate) parallelogram inscribed into γ \gamma. Moreover, we know that 2 ​ f ​ ( t 1) + 2 ​ f ​ ( t 3) + 1 = 2 ​ f ​ ( t 2) + 2 ​ f ​ ( t 4) 2f(t_{1})+2f(t_{3})+1=2f(t_{2})+2f(t_{4}). This does not have a solution where all f ⁡ ( t i) f(t_{i}) are integers. Thus at least one t i t_{i} is in the interval ( x, y) (x,y). Since this is true for any open interval ( x, y) ⊂ [0, 1] (x,y)\subset[0,1], we conclude that the set of vertices of inscribed parallelograms is dense in γ ⁡ ( [0, 1]) \gamma([0,1]).

Lastly, we check that f f prevents the parallelogram from being degenerate. If t 1 = t 2 t_{1}=t_{2}, then γ ⁡ ( t 1) + γ ⁡ ( t 3) = γ ⁡ ( t 2) + γ ⁡ ( t 4) \gamma(t_{1})+\gamma(t_{3})=\gamma(t_{2})+\gamma(t_{4}) implies that t 3 = t 4 t_{3}=t_{4} since γ \gamma is an embedding, but this directly contradicts 2 ​ f ​ ( t 1) + 2 ​ f ​ ( t 3) + 1 = 2 ​ f ​ ( t 2) + 2 ​ f ​ ( t 4) 2f(t_{1})+2f(t_{3})+1=2f(t_{2})+2f(t_{4}). The case t 2 = t 3 t_{2}=t_{3} is similar. ∎

To prove results about inscribed rectangles, we need a lemma that distinguishes rectangles among parallelograms. The British Flag Theorem states that if A ​ B ​ C ​ D ABCD are the vertices of a rectangle in a plane (in cyclic order) and P ∈ ℝ 2 P\in\mathbb{R}^{2} is any point then | P ​ A | 2 + | P ​ C | 2 = | P ​ B | 2 + | P ​ D | 2 |PA|^{2}+|PC|^{2}=|PB|^{2}+|PD|^{2}. We will need the converse of the British Flag Theorem:

###### Lemma 2.5.

Let A, B, C, D ∈ ℝ 2 A,B,C,D\in\mathbb{R}^{2} be the vertices of a parallelogram in counterclockwise order. If there is a point P ∈ ℝ 2 P\in\mathbb{R}^{2} such that | P ​ A | 2 + | P ​ C | 2 = | P ​ B | 2 + | P ​ D | 2 |PA|^{2}+|PC|^{2}=|PB|^{2}+|PD|^{2}, then A ​ B ​ C ​ D ABCD is a rectangle.

###### Proof.

Choose coordinates with the intersection of the diagonals of the parallelogram at the origin. Thus A = − C A=-C and B = − D B=-D, and | P + A | 2 + | P − A | 2 = | P + B | 2 + | P − B | 2 |P+A|^{2}+|P-A|^{2}=|P+B|^{2}+|P-B|^{2}. This is equivalent to 2 ​ | P | 2 + 2 ​ | A | 2 = 2 ​ | P | 2 + 2 ​ | B | 2 2|P|^{2}+2|A|^{2}=2|P|^{2}+2|B|^{2} and thus | A | 2 = | B | 2 = | C | 2 = | D | 2 |A|^{2}=|B|^{2}=|C|^{2}=|D|^{2}, so A ​ B ​ C ​ D ABCD is a rectangle. ∎

We can now prove the existence of many inscribed rectangles. Recently and independently, Schwartz [28] proved a trichotomy for inscribed rectangles in planar loops showing that all but at most four points are the vertices of inscribed rectangles.

###### Theorem 2.6.

Let γ: [0, 1] ⟶ ℝ 2 \gamma\colon[0,1]\longrightarrow\mathbb{R}^{2} be a simple loop. Then γ \gamma inscribes sufficiently many non-degenerate rectangles that the set of vertices is dense in γ ⁡ ( [0, 1]) \gamma([0,1]).

###### Proof.

Apply Corollary 2.3 to the following functions: γ 1, γ 2 \gamma_{1},\gamma_{2}, the function f f from the proof of Theorem 2.4, and g ⁡ ( t) = | γ ⁡ ( t) | 2 g(t)=|\gamma(t)|^{2}. Then the functions γ 1 \gamma_{1}, γ 2 \gamma_{2}, and f f guarantee that we obtain a non-degenerate inscribed parallelogram with at least one vertex in γ ⁡ ( (,,,)) \gamma((x,y)) for some arbitrary interval ( x, y) ⊂ [0, 1] (x,y)\subset[0,1]. The function g g ensures that the parallelogram is actually a rectangle by Lemma 2.5. ∎

###### Example 2.7.

In general we cannot prescribe a vertex of an inscribed rectangle precisely. Consider a curve γ \gamma that traces a triangle. Then we cannot prescribe a vertex of an inscribed rectangle to be a vertex of the triangle at an acute angle.

## 3. Splitting rectifiable loops

We started Section 2 by showing that the Hobby–Rice theorem implies that any planar C 1 C^{1} loop inscribes a parallelogram with one vertex at γ ⁡ ( 0) \gamma(0). We used Equation ( 1) to ensure that the parallelogram is non-degenerate. This equation more generally asserts that the length of γ \gamma over the intervals [0, a] [0,a] and [b, c] [b,c] is equal to length over the intervals [a, b] [a,b] and [c, 1] [c,1]. Thus γ \gamma is cut into four pieces γ | [0, a] \gamma|_{[0,a]}, γ | [a, b] \gamma|_{[a,b]}, γ | [b, c] \gamma|_{[b,c]}, and γ | [c, 1] \gamma|_{[c,1]} such that the pieces can be translated to form two loops of equal length. In this section we extend this result to higher dimensions and splitting into more than two loops of equal length.

For the notion of length to be well-defined the loop γ \gamma needs to be rectifiable. A curve γ: [0, 1] ⟶ ℝ d \gamma\colon[0,1]\longrightarrow\mathbb{R}^{d} is called *rectifiable*if there is a constant C > 0 C>0 such that

 | ∑ j = 1 n − 1 | γ ⁡ ( x j + 1) − γ ⁡ ( x j) | < C \sum_{j=1}^{n-1}{|\gamma(x_{j+1})-\gamma(x_{j})|}<C |  |

for any n n and any set of points x 1 < x 2 < ⋯ < x n x_{1}<x_{2}<\dots<x_{n} in [0, 1] [0,1]. In particular, the length of a rectifiable curve is well-defined. A rectifiable curve γ: [0, 1] ⟶ ℝ d \gamma\colon[0,1]\longrightarrow\mathbb{R}^{d} can be parametrized by arc length.

###### Theorem 3.1.

Let γ: [0, 1] ⟶ ℝ d \gamma\colon[0,1]\longrightarrow\mathbb{R}^{d} be a rectifiable loop. For an integer r ≥ 2 r\geq 2, let n = ( r − 1) ​ ( d + 1) n=(r-1)(d+1). Then there exists a partition of [0, 1] [0,1] into n + 1 n+1 intervals I 1, …, I n + 1 I_{1},\dots,I_{n+1} by n n cuts and a partition of the index set [n + 1] [n+1] into subsets T 1, …, T r T_{1},\dots,T_{r} such that the restrictions γ | I j \gamma|_{I_{j}}, j ∈ T k j\in T_{k}, can be rearranged by translations to form a loop for each k ∈ { 1, …, r } k\in\{1,\dots,r\}, and these r r loops all have the same length.

###### Proof.

Parametrize γ \gamma by arc length and apply Theorem 2.2 to the d d coordinate functions γ 1, …, γ d \gamma_{1},\dots,\gamma_{d} and the function f ⁡ ( t) = t f(t)=t. Then

 | ∑ j ∈ T 1 γ ⁡ ( t j) − γ ⁡ ( t j − 1) = ∑ j ∈ T 2 γ ⁡ ( t j) − γ ⁡ ( t j − 1) = ⋯ = ∑ j ∈ T r γ ⁡ ( t j) − γ ⁡ ( t j − 1) \sum_{j\in T_{1}}\gamma(t_{j})-\gamma(t_{j-1})=\sum_{j\in T_{2}}\gamma(t_{j})-\gamma(t_{j-1})=\dots=\sum_{j\in T_{r}}\gamma(t_{j})-\gamma(t_{j-1}) |  |

implies that ∑ j ∈ T i γ ⁡ ( t j) − γ ⁡ ( t j − 1) = 0 \sum_{j\in T_{i}}\gamma(t_{j})-\gamma(t_{j-1})=0 for all i ∈ [r] i\in[r]. Thus the pieces γ | [t j − 1, t j] \gamma|_{[t_{j-1},t_{j}]}, j ∈ T i j\in T_{i}, of γ \gamma can be rearranged by translations to form a loop for each i ∈ [r] i\in[r]. Moreover, ∑ j ∈ T 1 t j − t j − 1 = ∑ j ∈ T 2 t j − t j − 1 = ⋯ = ∑ j ∈ T r t j − t j − 1 \sum_{j\in T_{1}}t_{j}-t_{j-1}=\sum_{j\in T_{2}}t_{j}-t_{j-1}=\dots=\sum_{j\in T_{r}}t_{j}-t_{j-1} implies that these r r loops have the same length, since γ \gamma is parametrized by arc length. ∎

In particular, for r = 2 r=2 and d = 3 d=3 Theorem 3.1 implies that any simple loop γ \gamma in ℝ 3 \mathbb{R}^{3} inscribes a parallelogram whose vertices cut γ \gamma into four pieces γ ( 1), γ ( 2), γ ( 3), γ ( 4) \gamma^{(1)},\gamma^{(2)},\gamma^{(3)},\gamma^{(4)} in cyclic order such that γ ( 1) \gamma^{(1)} and γ ( 3) \gamma^{(3)} have the same total length as γ ( 2) \gamma^{(2)} and γ ( 4) \gamma^{(4)}.

Theorem 2.6 asserts that any simple planar loop inscribes many rectangles. While we have been unable to use this to derive Toeplitz’ conjecture that one of these rectangles is a square, we can use similar reasoning to that used in the proof of Theorem 3.1 to ensure that the length of the loop over pairs of opposite sides of the rectangle is the same. That is, instead of the sides of the rectangle itself having the same length, we can only ensure this for the pieces of the loop over those sides.

###### Theorem 3.2.

Let γ: [0, 1] ⟶ ℝ 2 \gamma\colon[0,1]\longrightarrow\mathbb{R}^{2} be a simple rectifiable loop. The loop γ \gamma inscribes a non-degenerate rectangle cutting it into four pieces γ ( 1), γ ( 2), γ ( 3), γ ( 4) \gamma^{(1)},\gamma^{(2)},\gamma^{(3)},\gamma^{(4)} in cyclic order such that γ ( 1) \gamma^{(1)} and γ ( 3) \gamma^{(3)} have the same total length as γ ( 2) \gamma^{(2)} and γ ( 4) \gamma^{(4)}.

###### Proof.

Parametrize γ \gamma by arc length. Use Corollary 2.3 for γ 1 \gamma_{1}, γ 2 \gamma_{2}, g ⁡ ( t) = | γ ⁡ ( t) | 2 g(t)=|\gamma(t)|^{2}, and f ⁡ ( t) = t f(t)=t. The first three functions ensure a (possibly degenerate) inscribed rectangle, while f f guarantees that the total length of γ ( 1) \gamma^{(1)} and γ ( 3) \gamma^{(3)} is equal to that of γ ( 2) \gamma^{(2)} and γ ( 4) \gamma^{(4)}. ∎

## 4. Necklace splittings with additional constraints

In this section we prove a proper strengthening of Alon’s necklace splitting result for r r a prime. This in turn yields a strengthened loop splitting result, provided that the number of resulting loops r r is a prime. We find it noteworthy that for these results the usual induction on the number of prime divisors seems to fail entirely. We are unable to derive similar results for non-primes r r. In fact, a result of Blagojević, Matschke, and Ziegler [7] implies that the topological method used in the proof fails outside of the case that r r is a prime. In light of the recent counterexamples to the topological Tverberg conjecture for parameters that are not prime powers [5, 11, 18], this opens the interesting question of whether the primality of r r is perhaps not an artifact of our proof method, but actually an essential prerequisite of our result.

Generalizations of Theorem 2.2 of various kinds have recently received much attention; see for example de Longueville and Živaljević [8], Karasev, Roldán-Pensado, and Soberón [17], Alishahi and Meunier [2], Asada et al. [4], and Blagojević and Soberón [6]. Here we show the following:

###### Theorem 4.1.

Let f 1, …, f m: [0, 1] ⟶ ℝ f_{1},\dots,f_{m}\colon[0,1]\longrightarrow\mathbb{R} be continuous functions. For a prime r ≥ 2 r\geq 2 let n = ( r − 1) ​ m {n=(r-1)m}. Let C 1, …, C ℓ C_{1},\dots,C_{\ell} be a partition of [n + 1] [n+1] with | C i | ≤ r − 1 |C_{i}|\leq r-1. Then there are points 0 = t 0 ≤ t 1 ≤ ⋯ ≤ t n + 1 = 1 0=t_{0}\leq t_{1}\leq\dots\leq t_{n+1}=1 and a partition of the index set [n + 1] [n+1] into subsets T 1, …, T r T_{1},\dots,T_{r} with | C i ∩ T j | ≤ 1 |C_{i}\cap T_{j}|\leq 1 for every i i and j j such that

 | ∑ j ∈ T 1 f k ( t j) − f k ( t j − 1) = ∑ j ∈ T 2 f k ( t j) − f k ( t j − 1) = ⋯ = ∑ j ∈ T r f k ( t j) − f k ( t j − 1), k = 1, …, m. \sum_{j\in T_{1}}f_{k}(t_{j})-f_{k}(t_{j-1})=\sum_{j\in T_{2}}f_{k}(t_{j})-f_{k}(t_{j-1})=\dots=\sum_{j\in T_{r}}f_{k}(t_{j})-f_{k}(t_{j-1}),\quad k=1,\dots,m. |  |

In the usual interpretation of Alon’s result, where [0, 1] [0,1] is thought of as an unclasped necklace with m m types of beads whose density along the necklace is given by μ 1, …, μ m \mu_{1},\dots,\mu_{m} and the sets T i T_{i} are thieves who would like to split the necklace fairly, the result above guarantees that there are blocks of size at most r − 1 r-1 pieces of the necklace such that no thief receives two pieces of the necklace within such a block.

Compare Theorem 4.1 with the following optimal colored Tverberg theorem of Blagojević, Matschke, and Ziegler.

###### Theorem 4.2 (Blagojević, Matschke, and Ziegler [7]).

Let r ≥ 2 r\geq 2 be a prime and d ≥ 1 d\geq 1 be an integer. Let n = ( r − 1) ​ ( d + 1) n=(r-1)(d+1), and let C 1, …, C ℓ C_{1},\dots,C_{\ell} be a partition of the vertex set of the n n -simplex Δ n \Delta_{n} with | C i | ≤ r − 1 |C_{i}|\leq r-1 for all i i. Then for any continuous map f: Δ n ⟶ ℝ d f\colon\Delta_{n}\longrightarrow\mathbb{R}^{d} there are r r pairwise disjoint faces σ 1, …, σ r \sigma_{1},\dots,\sigma_{r} of Δ n \Delta_{n} such that each σ i \sigma_{i} has at most one vertex in each C j C_{j} and with f ⁡ ( σ 1) ∩ ⋯ ∩ f ⁡ ( σ r) ≠ ∅ f(\sigma_{1})\cap\dots\cap f(\sigma_{r})\neq\emptyset.

To prove Theorem 4.1 we combine the central topological result of [7] with Matoušek’s proof of Theorem 2.2 and a combinatorial reduction to a special case; see Lemma 4.4. The complex [n] Δ ∗ m [n]^{*m}_{\Delta} denoted Δ n, m \Delta_{n,m} is called the chessboard complex. Here [n] [n] denotes the 0 0 -dimensional simplicial complex on vertex set [n] [n]. The symmetric group S n S_{n} naturally acts on [n] [n], and the subgroup ℤ / n \mathbb{Z}/n acts by shifts. Thus these groups act diagonally on joins and deleted joins of these complexes, in particular, on chessboard complexes Δ n, m \Delta_{n,m}.

We can now state the central topological lemma needed for the proof of Theorem 4.1. See also Vrećica and Živaljević [32].

###### Lemma 4.3 (Blagojević, Matschke, and Ziegler [7]).

Let r ≥ 2 r\geq 2 be a prime, m ≥ 1 m\geq 1 and integer, and n = ( r − 1) ​ m n=(r-1)m. Then any ℤ / r \mathbb{Z}/r -equivariant map ( Δ r, r − 1) ∗ m ∗ [r] ⟶ W r ⊕ m (\Delta_{r,r-1})^{*m}*[r]\longrightarrow W_{r}^{\oplus m} must have a zero.

The following lemma is analogous to a reduction in [7] for Tverberg-type results.

###### Lemma 4.4.

It is sufficient to prove Theorem 4.1 in the case that ℓ = m + 1 \ell=m+1, | C i | = r − 1 |C_{i}|=r-1 for i < ℓ i<\ell and | C ℓ | = 1 |C_{\ell}|=1.

###### Proof.

We are given continuous functions f 1, …, f m: [0, 1] ⟶ ℝ f_{1},\dots,f_{m}\colon[0,1]\longrightarrow\mathbb{R}, a prime r ≥ 2 r\geq 2, and n = ( r − 1) ​ m {n=(r-1)m}. Let C 1, …, C ℓ C_{1},\dots,C_{\ell} be a partition of [n + 1] [n+1] with | C i | ≤ r − 1 |C_{i}|\leq r-1. Certainly ℓ \ell is larger than m m. We define N N to be the integer ( r − 1) ​ ℓ {(r-1)\ell}, and we enlarge the sets C i C_{i} and add the new set C ℓ + 1 ′ = { N + 1 } C_{\ell+1}^{\prime}=\{N+1\} to be a partition of [N + 1] [N+1]. More precisely, obtain C i ′ C^{\prime}_{i} from C i C_{i} by adding r − 1 − | C i | r-1-|C_{i}| elements in [N] ∖ [n + 1] [N]\setminus[n+1]; this can be done in such a way that C 1 ′, …, C ℓ + 1 ′ C^{\prime}_{1},\dots,C_{\ell+1}^{\prime} is a partition of [N + 1] [N+1].

Define the functions h 1, …, h m: [0, 1] ⟶ ℝ h_{1},\dots,h_{m}\colon[0,1]\longrightarrow\mathbb{R} by h i ​ ( x) = f i ​ ( 2 ​ x) h_{i}(x)=f_{i}(2x) for x ≤ 1 2 x\leq\frac{1}{2} and h i ​ ( x) = f i ​ ( 1) h_{i}(x)=f_{i}(1) for x > 1 2 x>\frac{1}{2}. Let [a 1, b 1], …, [a ℓ − m, b ℓ − m] [a_{1},b_{1}],\dots,[a_{\ell-m},b_{\ell-m}] be pairwise disjoint intervals in [1 2, 1] [\frac{1}{2},1]. Define ℓ − m \ell-m new functions h m + 1, …, h ℓ: [0, 1] ⟶ ℝ h_{m+1},\dots,h_{\ell}\colon[0,1]\longrightarrow\mathbb{R} by h i ​ ( x) = 0 h_{i}(x)=0 for x < a i − m x<a_{i-m}, h i ​ ( x) = 1 h_{i}(x)=1 for x > b i − m x>b_{i-m}, and interpolate linearly in between, that is, h i ​ ( x) = 1 b i − m − a i − m ​ ( x − a i − m) h_{i}(x)=\frac{1}{b_{i-m}-a_{i-m}}(x-a_{i-m}) for x ∈ [a m − i, b m − i] x\in[a_{m-i},b_{m-i}]. When we assume that Theorem 4.1 has been shown for | C i ′ | = r − 1 |C^{\prime}_{i}|=r-1 for i ≤ ℓ i\leq\ell and | C ℓ + 1 ′ | = 1 |C^{\prime}_{\ell+1}|=1, then we can find points 0 = t 0 ≤ t 1 ≤ ⋯ ≤ t N + 1 = 1 0=t_{0}\leq t_{1}\leq\dots\leq t_{N+1}=1 and a partition T 1, …, T r T_{1},\dots,T_{r} of [N + 1] [N+1] such that

 | ∑ j ∈ T 1 h k ( t j) − h k ( t j − 1) = ∑ j ∈ T 2 h k ( t j) − h k ( t j − 1) = ⋯ = ∑ j ∈ T r h k ( t j) − h k ( t j − 1), k = 1, …, m \sum_{j\in T_{1}}h_{k}(t_{j})-h_{k}(t_{j-1})=\sum_{j\in T_{2}}h_{k}(t_{j})-h_{k}(t_{j-1})=\dots=\sum_{j\in T_{r}}h_{k}(t_{j})-h_{k}(t_{j-1}),\quad k=1,\dots,m |  |

and | C i ′ ∩ T j | ≤ 1 |C^{\prime}_{i}\cap T_{j}|\leq 1 for each i i and j j.

Of the points t i t_{i} at least r − 1 r-1 points need to be in each interval [a i, b i] [a_{i},b_{i}], which requires ( r − 1) ​ ( ℓ − m) (r-1)(\ell-m) points in total. Thus at most ( r − 1) ​ m (r-1)m points t i t_{i} are contained in the interval [0, 1 2] [0,\frac{1}{2}]. But then

 | ∑ j ∈ T 1 f k ( 2 t j) − f k ( 2 t j − 1) = ∑ j ∈ T 2 f k ( 2 t j) − f k ( 2 t j − 1) = ⋯ = ∑ j ∈ T r f k ( 2 t j) − f k ( 2 t j − 1), k = 1, …, m \sum_{j\in T_{1}}f_{k}(2t_{j})-f_{k}(2t_{j-1})=\sum_{j\in T_{2}}f_{k}(2t_{j})-f_{k}(2t_{j-1})=\dots=\sum_{j\in T_{r}}f_{k}(2t_{j})-f_{k}(2t_{j-1}),\quad k=1,\dots,m |  |

for those points t i t_{i}, proving the general case of Theorem 4.1. ∎

###### Proof of Theorem 4.1.

By the reduction of Lemma 4.4 we only need to consider the case that ℓ = m + 1 \ell=m+1 with | C 1 | = ⋯ = | C ℓ − 1 | = r − 1 |C_{1}|=\dots=|C_{\ell-1}|=r-1 and | C ℓ | = 1 {|C_{\ell}|=1}, which we will do from here on. We construct the S r S_{r} -equivariant map F: ( Δ n) Δ ∗ r ⟶ ( ℝ m) r F\colon(\Delta_{n})^{*r}_{\Delta}\longrightarrow(\mathbb{R}^{m})^{r} as in the proof of Theorem 2.2. Since we identified the vertex set of Δ n \Delta_{n} with [n + 1] [n+1] each set C i C_{i} is a subset of the vertex set of the n n -simplex, and thus ( C 1 ∗ ⋯ ∗ C ℓ) Δ ∗ r (C_{1}*\dots*C_{\ell})^{*r}_{\Delta} is an S r S_{r} -invariant subcomplex of ( Δ n) Δ ∗ r (\Delta_{n})^{*r}_{\Delta}. A point x ∈ ( C 1 ∗ ⋯ ∗ C ℓ) Δ ∗ r x\in(C_{1}*\dots*C_{\ell})^{*r}_{\Delta} precisely corresponds to points 0 = t 0 ≤ t 1 ≤ ⋯ ≤ t n + 1 = 1 0=t_{0}\leq t_{1}\leq\dots\leq t_{n+1}=1 and a partition T 1, …, T r T_{1},\dots,T_{r} of [n + 1] [n+1] as in the statement of the theorem. Observe that if the theorem was false, then the image of F F restricted to ( C 1 ∗ ⋯ ∗ C ℓ) Δ ∗ r (C_{1}*\dots*C_{\ell})^{*r}_{\Delta} would not intersect the diagonal D = { ( y 1, …, y r) ∈ ( ℝ m) r | y 1 = ⋯ = y r } D=\{(y_{1},\dots,y_{r})\in(\mathbb{R}^{m})^{r}\ |\ y_{1}=\dots=y_{r}\}. Orthogonally projecting along the diagonal gives an equivariant map F ^: ( C 1 ∗ ⋯ ∗ C ℓ) Δ ∗ r ⟶ W r ⊕ m \widehat{F}\colon(C_{1}*\dots*C_{\ell})^{*r}_{\Delta}\longrightarrow W_{r}^{\oplus m} that does not map to zero.

Now since | C 1 | = ⋯ = | C ℓ − 1 | = r − 1 |C_{1}|=\dots=|C_{\ell-1}|=r-1 and | C ℓ | = 1 {|C_{\ell}|=1} and since joins and deleted joins commute the complex ( C 1 ∗ ⋯ ∗ C ℓ) Δ ∗ r (C_{1}*\dots*C_{\ell})^{*r}_{\Delta} is isomorphic to ( [r − 1] Δ ∗ r) ∗ ( ℓ − 1) ∗ [1] Δ ∗ r ≅ ( Δ r, r − 1) ∗ ( ℓ − 1) ∗ [r] ([r-1]^{*r}_{\Delta})^{*(\ell-1)}*[1]^{*r}_{\Delta}\cong(\Delta_{r,r-1})^{*(\ell-1)}*[r]. Thus F ^ \widehat{F} contradicts Lemma 4.3. ∎

The same topological machinery fails for non-primes r r; see Blagojević, Matschke, and Ziegler [7]. In the same way that Theorem 3.1 follows from Theorem 2.2, we can derive the following corollary from Theorem 4.1.

###### Corollary 4.5.

Let γ: [0, 1] ⟶ ℝ d \gamma\colon[0,1]\longrightarrow\mathbb{R}^{d} be a rectifiable loop. For a prime r ≥ 2 r\geq 2, let n = ( r − 1) ​ ( d + 1) n=(r-1)(d+1). Let C 1, …, C m C_{1},\dots,C_{m} be a partition of [n + 1] [n+1] with | C i | ≤ r − 1 |C_{i}|\leq r-1. Then there exists a partition of [0, 1] [0,1] into n + 1 n+1 intervals I 1, …, I n + 1 I_{1},\dots,I_{n+1} by n n cuts and a partition of the index set [n + 1] [n+1] into subsets T 1, …, T r T_{1},\dots,T_{r} with | C i ∩ T k | ≤ 1 |C_{i}\cap T_{k}|\leq 1 such that the restrictions γ | I j \gamma|_{I_{j}}, j ∈ T k j\in T_{k}, can be rearranged by translations to form a loop for each k ∈ { 1, …, r } k\in\{1,\dots,r\}, and these r r loops all have the same length.

###### Question 4.6.

Is the condition that r r is a prime actually required in Theorem 4.1 and Corollary 4.5?

## Acknowledgements

This research was performed during the Summer Program for Undergraduate Research 2017 at Cornell University. The authors are grateful for the excellent research conditions provided by the program. The authors would like to thank Maru Sarazola for many insightful conversations. The authors would also like to thank Camil Muscalu, Phil Sosoe, and Gennady Uraltsev for clarifying discussions.

## References

- [1] Arseniy Akopyan and Sergey Avvakumov, *Any cyclic quadrilateral can be inscribed in any closed convex smooth curve*, arXiv preprint arXiv:1712.10205 (2017).
- [2] Meysam Alishahi and Frédéric Meunier, *Fair splitting of colored paths*, arXiv preprint arXiv:1704.02921 (2017).
- [3] Noga Alon, *Splitting necklaces*, Adv. Math. 63 (1987), no. 3, 247–253.
- [4] Megumi Asada, Florian Frick, Vivek Pisharody, Maxwell Polevy, David Stoner, Ling Hei Tsang, and Zoe Wellner, *Fair division and generalizations of Sperner- and KKM-type results*, SIAM J. Discrete Math. 32 (2018), no. 1, 591–610.
- [5] Pavle V. M. Blagojević, Florian Frick, and Günter M. Ziegler, *Barycenters of Polytope Skeleta and Counterexamples to the Topological Tverberg Conjecture, via Constraints*, J. Europ. Math. Soc., to appear (2018).
- [6] Pavle V. M. Blagojević and Pablo Soberón, *Thieves can make sandwiches*, Bull. Lond. Math. Soc. 50 (2018), no. 1, 108–123.
- [7] Pavle V.M. Blagojević, Benjamin Matschke, and Günter M. Ziegler, *Optimal bounds for the colored Tverberg problem*, J. Europ. Math. Soc. 17 (2015), no. 4, 739–754.
- [8] Mark de Longueville and Rade Živaljević, *Splitting multidimensional necklaces*, Adv. Math. 218 (2008), no. 3, 926–939.
- [9] Albrecht Dold, *Simple proofs of some Borsuk–Ulam results*, Contemp. Math. 19 (1983), 65–69.
- [10] Arnold Emch, *On some properties of the medians of closed continuous curves formed by analytic arcs*, Amer. J. Math. 38 (1916), no. 1, 6–18.
- [11] Florian Frick, *Counterexamples to the topological Tverberg conjecture*, Oberwolfach Rep. 12 (2015), no. 1, 318–321.
- [12] Heinrich Guggenheimer, *Finite sets on curves and surfaces*, Israel J. Math. 3 (1965), no. 2, 104–112.
- [13] Heinrich Guggenheimer, *Proof of a Conjecture of H. Hadwiger*, Elem. Math. 29 (1974), 35–36.
- [14] Hugo Hadwiger, *Ungelöste Probleme Nr. 53*, Elem. Math. 26 (1971), 58.
- [15] Charles R. Hobby and John R. Rice, *A moment problem in L 1 L_{1} approximation*, Proc. Amer. Math. Soc. 16 (1965), no. 4, 665–670.
- [16] Cole Hugelmeyer, *Every smooth Jordan curve has an inscribed rectangle with aspect ratio equal to 3 \sqrt{3}*, arXiv preprint arXiv:1803.07417 (2018).
- [17] Roman Karasev, Edgardo Roldán-Pensado, and Pablo Soberón, *Measure partitions using hyperplanes with fixed directions*, Israel J. Math. 212 (2016), no. 2, 705–728.
- [18] Isaac Mabillard and Uli Wagner, *Eliminating Higher-Multiplicity Intersections, I. A Whitney Trick for Tverberg-Type Problems*, arXiv preprint arXiv:1508.02349 (2015).
- [19] Vladimir Makeev, *Quadrangles inscribed in a closed curve and the vertices of a curve*, J. Math. Sciences 131 (2005), no. 1, 5395–5400.
- [20] Jiří Matoušek, *Using the Borsuk–Ulam Theorem. Lectures on Topological Methods in Combinatorics and Geometry*, second ed., Universitext, Springer-Verlag, Heidelberg, 2008.
- [21] Benjamin Matschke, *Equivariant topology methods in discrete geometry*, Ph.D. thesis, Freie Universität Berlin, 2011.
- [22] Benjamin Matschke, *A survey on the square peg problem*, Notices Amer. Math. Soc. 61 (2014), no. 4, 346–352.
- [23] Benjamin Matschke, *Quadrilaterals inscribed in convex curves*, arXiv preprint arXiv:1801.01945 (2018).
- [24] Mark D. Meyerson, *Balancing acts*, Topology Proc., vol. 6, 1981, pp. 59–75.
- [25] Mark J. Nielsen, *Rhombi inscribed in simple closed curves*, Geom. Ded. 54 (1995), no. 3, 245–254.
- [26] Igor Pak, *Lectures on Discrete and Polyhedral Geometry*, [http://math.ucla.edu/˜pak/book.htm][4], 2010.
- [27] Lev G. Schnirelman, *On some geometric properties of closed curves (in Russian)*, Usp. Mat. Nauk 10 (1944), 34–44.
- [28] Richard Evan Schwartz, *A Trichotomy for Rectangles Inscribed in Jordan Loops*, arXiv preprint arXiv:1804.00740 (2018).
- [29] Walter Stromquist, *Inscribed squares and square-like quadrilaterals in closed curves*, Mathematika 36 (1989), no. 2, 187–197.
- [30] Terence Tao, *An integration approach to the Toeplitz square peg problem*, Forum Math. Sigma 5 (2017).
- [31] Otto Toeplitz, *Ueber einige Aufgaben der Analysis situs*, Verhandlungen der Schweizerischen Naturforschenden Gesellschaft in Solothurn 4 (1911), no. 197, 29–30.
- [32] Siniša T. Vrećica and Rade T. Živaljević, *Chessboard complexes indomitable*, J. Combin. Theory, Ser. A 118 (2011), no. 7, 2157–2166.
- [33] Siniša T. Vrećica and Rade T. Živaljević, *Fulton-MacPherson compactification, cyclohedra, and the polygonal pegs problem*, Israel J. Math. 184 (2011), no. 1, 184–221.

[◄][5][image: ar5iv homepage] [6]
[Feeling lucky?][7] [8]
[Conversion report][9]
[Report an issue][10]
[View original on arXiv][11] [►][12]


## Links

[1]: mailto:{aslam.j,%20chen.shuj}@husky.neu.edu
[2]: mailto:{ff238,%20sps247,%20ls823}@cornell.edu
[3]: mailto:thomas.hugh_r@uqam.ca
[4]: http://math.ucla.edu/~pak/book.htm
[5]: /html/1806.02483
[6]: /
[7]: /feeling_lucky
[8]: /land_of_honey_and_milk
[9]: /log/1806.02484
[10]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1806.02484
[11]: https://arxiv.org/pdf/1806.02484
[12]: /html/1806.02485
