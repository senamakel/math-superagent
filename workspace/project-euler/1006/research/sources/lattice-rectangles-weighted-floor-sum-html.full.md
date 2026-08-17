<!-- source: https://arxiv.org/html/2604.22456v2 | converted from HTML -->

Counting All Lattice Rectangles in the Square Grid in Near-Linear Time

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2604.22456v2 [cs.CG] 01 May 2026

Francedimitry008@gmail.com Francebsl84848@gmail.com

# Counting All Lattice Rectangles in the Square Grid in Near-Linear Time

Dmitry Babichev Sergey Babichev

###### Abstract

We study the exact counting problem for all lattice rectangles contained in the square [0, n) × [0, n) [0,n)\times[0,n), including non-axis-parallel ones. Starting from the standard parametrization by a primitive direction ( u, v) (u,v) and two side lengths, we derive several exact algorithms: the classical O ⁡ ( n 2) O(n^{2}) sweep, decompositions of complexity O ⁡ ( n 3 / 2 ​ log ⁡ n) O(n^{3/2}\log n) and O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n), a ten-moment weighted-floor-sum reduction of complexity O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n), and a divisor-layer algorithm with the complexity O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n). We also give an all-values algorithm that computes F ⁡ ( 1), …, F ⁡ ( N) F(1),\ldots,F(N) in O ⁡ ( N 3 / 2) O(N^{3/2}) arithmetic operations. The main idea behind the near-linear one-value algorithms is to reduce the geometric summation to constant-size families of weighted floor sums closed under Euclidean-style affine and reciprocal transformations. Besides the exact algorithmic results, we derive a two-term asymptotic expansion, F ⁡ ( n) = 4 ​ log ⁡ 2 − 1 π 2 ​ n 4 ​ log ⁡ n + B ​ n 4 + o ⁡ ( n 4) F(n)=\frac{4\log 2-1}{\pi^{2}}n^{4}\log n+B\,n^{4}+o(n^{4}) with the explicit formula for B B, which provides an independent consistency check for the large- n n numerical data produced by the algorithms.

###### ccs

Theory of computation Computational geometry

###### ccs

Theory of computation Design and analysis of algorithms

###### ccs

Mathematics of computing Discrete mathematics

###### keywords

Lattice rectangles, grid enumeration, floor sums, Möbius inversion

† † runningauthor: Dmitry Babichev and Sergey Babichev

## 1 Introduction

We study the following problem.

Problem. Count all rectangles whose vertices lie in the integer lattice and are contained in the square [0, n) × [0, n) [0,n)\times[0,n), including non-axis-parallel rectangles.

Counting lattice configurations in planar grids is a classical topic at the interface of combinatorics, geometry of numbers, and lattice-point enumeration. In this paper we study an exact counting problem for lattice rectangles.

The resulting counting function is the OEIS sequence A085582 [14]. Geometrically, it extends the classical axis-parallel rectangle count to arbitrary lattice orientations in the same n × n n\times n grid of points. Arithmetically, each non-axis-parallel family is governed by a primitive direction ( u, v) (u,v), which brings in coprimality, divisor sums, and floor-sum recurrences. Computationally, the OEIS entry already collects exact values, tables, and scripts, so faster exact algorithms are useful both for extending the data and for testing asymptotic predictions.

The classical split appears in the OEIS decomposition A ​ 085582 ​ ( n) = A ​ 000537 ​ ( n − 1) + A ​ 113751 ​ ( n), A085582(n)=A000537(n-1)+A113751(n), where A ​ 000537 ​ ( n − 1) = ( n 2) 2 A000537(n-1)=\binom{n}{2}^{2} is the axis-parallel count and A ​ 113751 ​ ( n) A113751(n) records the non-axis-parallel contribution [14]. Our goal is to show that the full sequence is not merely a table of values, but a structured counting problem admitting several increasingly efficient exact algorithms.

We are not aware of prior work on this exact enumeration problem in the present algorithmic form. Our main contribution is an algorithmic reduction from geometric enumeration to a constant-size family of weighted Euclidean floor-sum kernels, which yields the complexity improvements proved below. For related background on floor-sum reciprocity, elementary number-theoretic estimates, and lattice-point enumeration, see [2, Section 3.5] and [3, 1, 7, 10]. The use of primitive lattice directions also connects the problem to the broader literature on primitive lattice points in planar domains and polygonal counting problems [8, 9].

Our main contributions are as follows.

1. 1.

We derive several exact one-value algorithms beyond the quadratic baseline, with complexities O ⁡ ( n 3 / 2 ​ log ⁡ n) O(n^{3/2}\log n), O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n), O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n), and O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n). The O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) method uses Möbius divisor layers and a square-root cover inside each layer, while the weighted floor-sum kernels are evaluated by Euclidean recurrences. See \cref tab:algorithm-summary for more details.

2. 2.

We also derive an all-values algorithm computing the whole prefix table F ⁡ ( 1), …, F ⁡ ( N) F(1),\ldots,F(N) in O ⁡ ( N 3 / 2) O(N^{3/2}) arithmetic operations and O ⁡ ( N) O(N) memory. It replaces repeated summatory evaluations by coefficient arrays indexed by the exact threshold a ​ x + b ​ y ax+by and then applies a Möbius divisor convolution.

Method | Main idea | Time | Authors | Kernel |

Baseline | primitive-direction enumeration | O ⁡ ( n 2) O(n^{2}) | Radcliffe | none |

Square-root | small/large split; coprime prefixes | O ⁡ ( n 3 / 2 ​ log ⁡ n) O(n^{3/2}\log n) | this paper | coprime prefixes |

Cubic-root | dual parametrization; six moments | O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n) | this paper | six-moment weighted floor-sum |

Ten-moment | Möbius inversion; weighted floor sums | O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) | this paper | ten-moment weighted floor-sum |

Divisor-layer | Möbius layers; square-root cover | O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) | this paper | six-moment weighted floor-sum |

All-values | event arrays; Möbius convolution | O ⁡ ( N 3 / 2) O(N^{3/2}) | this paper | arithmetic-progression updates |

Table 1: Summary of the algorithms discussed in the paper.
3. 3.

We derive a two-term asymptotic expansion F ⁡ ( n) = 4 ​ log ⁡ 2 − 1 π 2 ​ n 4 ​ log ⁡ n + B ​ n 4 + o ⁡ ( n 4), F(n)=\frac{4\log 2-1}{\pi^{2}}n^{4}\log n+B\,n^{4}+o(n^{4}), with an explicit constant B B. This asymptotic analysis is partly independent of the algorithmic development, but it is included here because it gives a stringent large- n n validation of the exact counts and in particular of the high-precision computations used in the fastest implementations.

The intermediate algorithms are included because they expose the structural reductions leading to the near-linear methods: the O ⁡ ( n 3 / 2 ​ log ⁡ n) O(n^{3/2}\log n) split introduces the direction/side-length duality, the O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n) algorithm isolates a finite floor-moment state space, the O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) algorithm uses a ten-state weighted floor-sum kernel, and the O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) divisor-layer algorithm combines the same six-state kernel with a Möbius-layer square-root cover. The all-values algorithm uses the same threshold geometry, but stores coefficients by exact threshold so that the whole table is recovered by prefix sums.

Throughout the paper we count arithmetic operations in a standard RAM model. In the implementation, all loop indices and intermediate affine parameters are stored in std::int128_t, which is exact throughout the benchmarked range reported in \cref sec:experiments. Accordingly, the stated running times should be read as arithmetic-operation bounds rather than bit-complexity bounds for arbitrarily large integers. The recursive floor-sum kernels have O ⁡ ( 1) O(1) state size; the remaining memory usage comes from the preprocessing tables.

## 2 The standard parametrization

This section fixes the basic parametrization and separates the easy axis-parallel and boundary contributions from the primitive non-axis-parallel part.

Let ( u, v) (u,v) be a primitive lattice direction, so u ⩾ v > 0 u\geqslant v>0 and gcd ⁡ ( u, v) = 1 \gcd(u,v)=1. The orthogonal direction is ( − v, u) (-v,u). A rectangle with side lengths a, b ⩾ 1 a,b\geqslant 1 in these two directions is generated by a ⋅ ( u, v) a\cdot(u,v) and b ⋅ ( − v, u) b\cdot(-v,u), hence its axis-aligned bounding box has side lengths a ​ u + b ​ v au+bv and a ​ v + b ​ u av+bu. Therefore it fits into the half-open square [0, n) × [0, n) [0,n)\times[0,n) if and only if

 | a ​ u + b ​ v ⩽ n, a ​ v + b ​ u ⩽ n. au+bv\leqslant n,\qquad av+bu\leqslant n. |  | (1) |

For such a quadruple ( u, v, a, b) (u,v,a,b), the number of placements equals

 | ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u). (n-au-bv)(n-av-bu). |  | (2) |

We split F ⁡ ( n) = F 0 ​ ( n) + F 1 ​ ( n). F(n)=F_{0}(n)+F_{1}(n). Here F 0 ​ ( n) F_{0}(n) collects the axis-parallel orientations together with the boundary direction ( 1, 1) (1,1), while F 1 ​ ( n) F_{1}(n) contains all primitive directions with 0 < v < u 0<v<u. The axis-parallel term is the classical rectangular-grid count, the direction ( 1, 1) (1,1) is the simplest genuinely tilted family, and all remaining work is concentrated in the primitive non-axis-parallel directions. These cases are separated to avoid double counting and to isolate the boundary direction ( 1, 1) (1,1). The axis-parallel rectangles contribute ( n 2) 2 = n 2 ​ ( n − 1) 2 / 4 \binom{n}{2}^{2}=n^{2}(n-1)^{2}/4, and the direction ( 1, 1) (1,1) contributes n ​ ( n − 1) 2 ​ ( n − 2) / 12 n(n-1)^{2}(n-2)/12. Hence

 | F 0 ​ ( n) = n 2 ​ ( n − 1) 2 4 + n ​ ( n − 1) 2 ​ ( n − 2) 12. F_{0}(n)=\frac{n^{2}(n-1)^{2}}{4}+\frac{n(n-1)^{2}(n-2)}{12}. |  |

For F 1 ​ ( n) F_{1}(n), by symmetry in a, b a,b, set x:= max ⁡ ( a, b) x:=\max(a,b) and y:= min ⁡ ( a, b) y:=\min(a,b), so x ⩾ y ⩾ 1 x\geqslant y\geqslant 1. The constraints become x ​ u + y ​ v ⩽ n xu+yv\leqslant n and x ​ v + y ​ u ⩽ n xv+yu\leqslant n, and the second inequality is redundant because x ⩾ y x\geqslant y and u > v u>v. Thus the two orderings of ( a, b) (a,b) collapse into one term; swapping ( u, v) (u,v) with ( v, u) (v,u) only produces the reflected direction, excluded by the convention u > v > 0 u>v>0. Thus we get

 | F 1 ​ ( n) = ∑ u > v > 0, x ⩾ y ⩾ 1 gcd ⁡ ( u, v) = 1, x ​ u + y ​ v ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − yv) ​ ( n − xv − yu), F_{1}(n)=\!\!\!\!\!\!\!\!\!\!\sum_{\begin{subarray}{c}u>v>0,\ x\geqslant y\geqslant 1\\ \gcd(u,v)=1,\ xu+yv\leqslant n\end{subarray}}\!\!\!\!\!\!\!\!\!\!\mult(x,y)\,(n-xu-yv)(n-xv-yu), |  | (3) |

where 𝒲 ⁡ ( x, y) = 2 \mult(x,y)=2 if x = y x=y and 𝒲 ⁡ ( x, y) = 4 \mult(x,y)=4 if x > y x>y. This identity will be the common starting point for the reparametrizations below.

## 3 The classical quadratic algorithm

We record the natural O ⁡ ( n 2) O(n^{2}) baseline obtained by sweeping over primitive directions and summing admissible side-length pairs [14, 15].

### 3.1 Direction sweep

Fix a primitive direction ( u, v) (u,v) with u > v u>v. For each admissible y y, the variable x x runs through an interval determined by \cref eq:xyuv-standard. A straightforward implementation computes the contribution of one primitive direction in time O ⁡ ( n / u), O\!\left(n/u\right), or in time O ⁡ ( n / u ⋅ log ⁡ n) O\!\left(n/u\cdot\log n\right) if one performs coprimality tests online and evaluates the inner arithmetic progressions without the closed-form simplifications.

The number of primitive pairs with first coordinate u u is φ ⁡ ( u) + O ⁡ ( 1) \varphi(u)+O(1), so using the classical estimate ∑ u ⩽ n φ ⁡ ( u) u = O ⁡ ( n) \sum_{u\leqslant n}\frac{\varphi(u)}{u}=O(n) we get:

 | ∑ u ⩽ n φ ⁡ ( u) ​ n u = O ⁡ ( n 2), ∑ u ⩽ n φ ⁡ ( u) ​ n ​ log ⁡ n u = O ⁡ ( n 2 ​ log ⁡ n), \sum_{u\leqslant n}\varphi(u)\frac{n}{u}=O(n^{2}),\qquad\sum_{u\leqslant n}\varphi(u)\frac{n\log n}{u}=O(n^{2}\log n), |  |

###### Proposition 1 (classical baseline).

The rectangle-counting problem admits

- •

a direct implementation of complexity O ⁡ ( n 2 ​ log ⁡ n) O(n^{2}\log n) if primitivity and inner summation are handled naively, and

- •

an O ⁡ ( n 2) O(n^{2}) implementation after standard preprocessing of primitive directions and elementary arithmetic simplifications.

Algorithmically, the classical baseline sweeps over primitive directions ( u, v) (u,v) and, for each such direction, over the admissible values of the secondary side length parameter; for fixed ( u, v, y) (u,v,y), the remaining interval in x x is summed explicitly. We state this baseline explicitly because every later improvement modifies exactly one bottleneck of this sweep. Compare the standard divisor-summation and hyperbola-method viewpoints in [4, 5]; a more implementation-oriented version is recorded in \cref app:pseudocode. For readers coming from the OEIS entry, this is also the closest formalization of the straightforward computation behind the existing tables and scripts [15].

## 4 A square-root decomposition: O ⁡ ( n 3 / 2 ​ log ⁡ n) O(n^{3/2}\log n)

Let B:= ⌊ n ⌋. B:=\left\lfloor\sqrt{n}\right\rfloor. We split the set of primitive directions into two regions

 | 𝒟 small = { ( u, v): gcd ( u, v) = 1, u > v > 0, u ⩽ B }, \mathcal{D}_{\mathrm{small}}=\{(u,v):\gcd(u,v)=1,\ u>v>0,\ u\leqslant B\}, |  |

 | 𝒟 large = { ( u, v): gcd ( u, v) = 1, u > v > 0, u > B }. \mathcal{D}_{\mathrm{large}}=\{(u,v):\gcd(u,v)=1,\ u>v>0,\ u>B\}. |  |

### 4.1 Small directions

For ( u, v) ∈ 𝒟 small (u,v)\in\mathcal{D}_{\mathrm{small}}, we keep the classical parametrization ( u, v, x, y) (u,v,x,y). The contribution of one direction is computed in time O ⁡ ( n / u ⋅ log ⁡ n), O\!\left(n/u\cdot\log n\right), and hence the total cost is

 | ∑ u ⩽ B φ ⁡ ( u) ​ n ​ log ⁡ n u = O ⁡ ( n ​ B ​ log ​ n) = O ⁡ ( n 3 / 2 ​ log ​ n). \sum_{u\leqslant B}\varphi(u)\frac{n\log n}{u}=O(nB\log n)=O(n^{3/2}\log n). |  |

### 4.2 Large directions

If ( u, v) ∈ 𝒟 large (u,v)\in\mathcal{D}_{\mathrm{large}}, then u > B u>B, hence every admissible rectangle has x ⩽ n / u < n / B x\leqslant n/u<n/B. Therefore we switch the order of summation and use the parameterization from \cref sec:standard. Restricting the formula for F 1 ​ ( n) F_{1}(n) to 𝒟 large \mathcal{D}_{\mathrm{large}}, we obtain

 | F 1, large ​ ( n) = ∑ ( u, v) ∈ 𝒟 large x ⩾ y ⩾ 1, x ​ u + y ​ v ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − yv) ​ ( n − xv − yu). F_{1,\mathrm{large}}(n)=\sum_{\begin{subarray}{c}(u,v)\in\mathcal{D}_{\mathrm{large}}\\ x\geqslant y\geqslant 1,\ xu+yv\leqslant n\end{subarray}}\mult(x,y)\,(n-xu-yv)(n-xv-yu). |  |

Fix u, x, y u,x,y and set

 | v max:= min ⁡ ( u − 1, ⌊ n − x ​ u y ⌋). v_{\max}:=\min\!\left(u-1,\left\lfloor\frac{n-xu}{y}\right\rfloor\right). |  |

Then the inner summation runs over all v ∈ [1, v max] v\in[1,v_{\max}] with gcd ⁡ ( u, v) = 1 \gcd(u,v)=1, and the placement factor is a quadratic polynomial in v v:

 | ( n − x ​ u − y ​ v) ​ ( n − x ​ v − y ​ u) = A 0 ​ ( u, x, y) + A 1 ​ ( u, x, y) ​ v + A 2 ​ ( x, y) ​ v 2, (n-xu-yv)(n-xv-yu)=A_{0}(u;x,y)+A_{1}(u;x,y)\,v+A_{2}(x,y)\,v^{2}, |  |

where

 | A 0 ​ ( u, x, y) = ( n − x ​ u) ​ ( n − y ​ u), A 1 ​ ( u, x, y) = − ( x ⁡ ( n − x ​ u) + y ⁡ ( n − y ​ u)), A 2 ​ ( x, y) = x ​ y. A_{0}(u;x,y)=(n-xu)(n-yu),\qquad A_{1}(u;x,y)=-(x(n-xu)+y(n-yu)),\qquad A_{2}(x,y)=xy. |  |

Hence for fixed u, x, y u,x,y we need only the three coprime prefix sums

 | C j ​ ( u, X):= ∑ 1 ⩽ v ⩽ X gcd ⁡ ( u, v) = 1 v j, j ∈ { 0, 1, 2 }. C_{j}(u;X):=\sum_{\begin{subarray}{c}1\leqslant v\leqslant X\\ \gcd(u,v)=1\end{subarray}}v^{j},\qquad j\in\{0,1,2\}. |  |

Indeed, by Möbius inversion, 𝟏 gcd ⁡ ( u, v) = 1 = ∑ d | u, d | v μ ⁡ ( d) \mathbf{1}_{\gcd(u,v)=1}=\sum_{d\mid u,\ d\mid v}\mu(d), and therefore

 | C j ​ ( u, X) = ∑ d | u μ ⁡ ( d) ​ ∑ m ⩽ X / d ( d ​ m) j. C_{j}(u;X)=\sum_{d\mid u}\mu(d)\sum_{m\leqslant X/d}(dm)^{j}. |  |

Consequently the v v -sum becomes

 | ∑ 1 ⩽ v ⩽ v max gcd ⁡ ( u, v) = 1 ( n − x ​ u − y ​ v) ​ ( n − x ​ v − y ​ u) = A 0 ​ C 0 ​ ( u, v max) + A 1 ​ C 1 ​ ( u, v max) + A 2 ​ C 2 ​ ( u, v max). \sum_{\begin{subarray}{c}1\leqslant v\leqslant v_{\max}\\ \gcd(u,v)=1\end{subarray}}(n-xu-yv)(n-xv-yu)=A_{0}C_{0}(u;v_{\max})+A_{1}C_{1}(u;v_{\max})+A_{2}C_{2}(u;v_{\max}). |  |

So the whole large-direction contribution is

 | F 1, large ​ ( n) = ∑ u > B ∑ x ⩽ n / u ∑ y ⩽ x 𝒲 ⁡ ( x, y) ​ ( A 0 ​ C 0 ​ ( u, v max) + A 1 ​ C 1 ​ ( u, v max) + A 2 ​ C 2 ​ ( u, v max)). F_{1,\mathrm{large}}(n)=\sum_{u>B}\ \sum_{x\leqslant n/u}\ \sum_{y\leqslant x}\mult(x,y)\bigl(A_{0}C_{0}(u;v_{\max})+A_{1}C_{1}(u;v_{\max})+A_{2}C_{2}(u;v_{\max})\bigr). |  |

For each fixed u u, the number of pairs ( x, y) (x,y) is O ⁡ ( ( n / u) 2) O((n/u)^{2}), and one coprime-prefix query is answered in O ⁡ ( τ ⁡ ( u)) O(\tau(u)) time from the squarefree divisors of u u. Summing over u > B u>B gives

 | ∑ u > B O ⁡ ( τ ⁡ ( u) ​ ( n u) 2) = O ⁡ ( n 2 ​ ∑ u > B τ ⁡ ( u) u 2) = O ⁡ ( n 2 ​ log ⁡ n B). \sum_{u>B}O\!\left(\tau(u)\Bigl(\frac{n}{u}\Bigr)^{2}\right)=O\!\left(n^{2}\sum_{u>B}\frac{\tau(u)}{u^{2}}\right)=O\!\left(\frac{n^{2}\log n}{B}\right). |  |

###### Theorem 2 (square-root decomposition).

Choosing B = ⌊ n ⌋ B=\left\lfloor\sqrt{n}\right\rfloor and treating small directions and large directions by dual parametrizations yields an algorithm of complexity O ⁡ ( n 3 / 2 ​ log ⁡ n). O(n^{3/2}\log n).

At the algorithmic level, one chooses the threshold B = ⌊ n ⌋ B=\left\lfloor\sqrt{n}\right\rfloor, evaluates the small-direction range u ⩽ B u\leqslant B by the one-direction routine from the previous section, and evaluates the complementary range by the dual sweep in the ( x, y) (x,y) variables. \cref app:pseudocode records a fuller pseudocode version of this decomposition.

## 5 A cubic-root decomposition: O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n)

The next refinement follows the same philosophy as the square-root split, but with a stronger one-direction kernel. Let

 | B:= ⌊ n 2 / 3 ⌋. B:=\left\lfloor n^{2/3}\right\rfloor. |  |

We again split the set of primitive directions at the threshold u = B u=B.

### 5.1 Small directions: one primitive pair in O ⁡ ( log ⁡ n) O(\log n)

Fix a primitive direction ( u, v) (u,v) with

 | u > v ⩾ 1, gcd ⁡ ( u, v) = 1. u>v\geqslant 1,\qquad\gcd(u,v)=1. |  |

Denote by c u, v ​ ( n) c_{u,v}(n) its total contribution in the parametrization of ( 3):

 | c u, v ​ ( n):= ∑ x ⩾ y ⩾ 1 x ​ u + y ​ v ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − yv) ​ ( n − xv − yu), c_{u,v}(n):=\sum_{\begin{subarray}{c}x\geqslant y\geqslant 1\\ xu+yv\leqslant n\end{subarray}}\mult(x,y)\,(n-xu-yv)(n-xv-yu), |  |

We sum over x x, with y y as the inner variable. For fixed x x, the admissible values of y y satisfy

 | 1 ⩽ y ⩽ min ⁡ ( x, M ⁡ ( x)), where ​ M ​ ( x) = ⌊ n − x ​ u v ⌋ 1\leqslant y\leqslant\min\!\left(x,M(x)\right),\text{ where }M(x)=\left\lfloor\frac{n-xu}{v}\right\rfloor |  |

Thus the x x -range splits at the transition point x = n u + v x=\frac{n}{u+v}. Therefore we obtain two segments:

 | I 1 = [1, ⌊ n u + v ⌋], I 2 = [⌊ n u + v ⌋ + 1, ⌊ n u ⌋]. I_{1}=\left[1,\left\lfloor\frac{n}{u+v}\right\rfloor\right],\qquad I_{2}=\left[\left\lfloor\frac{n}{u+v}\right\rfloor+1,\left\lfloor\frac{n}{u}\right\rfloor\right]. |  |

On the first segment I 1 I_{1}, the bound coming from x ​ u + y ​ v ⩽ n xu+yv\leqslant n is inactive, so 1 ⩽ y ⩽ x 1\leqslant y\leqslant x. On the second segment I 2 I_{2}, the active upper bound is 1 ⩽ y ⩽ ⌊ n − x ​ u v ⌋. 1\leqslant y\leqslant\left\lfloor\frac{n-xu}{v}\right\rfloor. Thus c u, v ​ ( n) c_{u,v}(n) is the sum of two segment contributions.

On I 1 I_{1}, we separate the diagonal y = x y=x from the strict range 1 ⩽ y < x 1\leqslant y<x. The diagonal contribution is computable in O ⁡ ( 1) O(1) time.

On I 2 I_{2}, the upper bound for y y is M ⁡ ( x) M(x), and since M ⁡ ( x) < x M(x)<x throughout this segment, we always have x > y x>y, hence 𝒲 ⁡ ( x, y) = 4 \mult(x,y)=4. Expanding

 | ( n − x ​ u − y ​ v) ​ ( n − x ​ v − y ​ u) = P 0 ​ ( x) + P 1 ​ ( x) ​ y + P 2 ​ y 2, (n-xu-yv)(n-xv-yu)=P_{0}(x)+P_{1}(x)y+P_{2}y^{2}, |  |

where P 0 ​ ( x) P_{0}(x) is quadratic in x x, P 1 ​ ( x) P_{1}(x) is linear in x x, and P 2 P_{2} is constant, and then carrying out the inner summation over y y, we obtain a polynomial in x x and M ⁡ ( x) M(x). More precisely, the total contribution of I 2 I_{2} is a fixed linear combination of the six floor moments

 | ∑ x ∈ I 2 M ⁡ ( x), ∑ x ∈ I 2 x ​ M ​ ( x), ∑ x ∈ I 2 x 2 ​ M ​ ( x), ∑ x ∈ I 2 M ​ ( x) 2, ∑ x ∈ I 2 x ​ M ​ ( x) 2, ∑ x ∈ I 2 M ​ ( x) 3. \sum_{x\in I_{2}}M(x),\ \ \sum_{x\in I_{2}}xM(x),\ \ \sum_{x\in I_{2}}x^{2}M(x),\ \ \sum_{x\in I_{2}}M(x)^{2},\ \ \sum_{x\in I_{2}}xM(x)^{2},\ \ \sum_{x\in I_{2}}M(x)^{3}. |  | (4) |

To formalize the required queries, for integers N ⩾ 0 N\geqslant 0, m ⩾ 1 m\geqslant 1, and a, b ⩾ 0 a,b\geqslant 0, define the six-moment kernel

 | ℋ p, q ​ ( N, m, a, b):= ∑ t = 0 N − 1 t p ​ ⌊ a ​ t + b m ⌋ q, ( p, q) ∈ { ( 0, 1), ( 1, 1), ( 2, 1), ( 0, 2), ( 1, 2), ( 0, 3) }. \mathcal{H}_{p,q}(N;m,a,b):=\sum_{t=0}^{N-1}t^{p}\left\lfloor\frac{at+b}{m}\right\rfloor^{q},\ \ (p,q)\in\{(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)\}. |  | (5) |

The interval sums appearing in ( 4) have negative slope in the summation variable, so before invoking the kernel we first reverse the index.

###### Lemma 3 (sign reversal for floor moments).

Let m ⩾ 1 m\geqslant 1, u ⩾ 0 u\geqslant 0, B ∈ ℤ B\in\mathbb{Z}, and L ⩽ R L\leqslant R. Put N:= R − L + 1 N:=R-L+1. Then for every p ⩾ 0 p\geqslant 0 and q ⩾ 1 q\geqslant 1,

 | ∑ x = L R x p ​ ⌊ B − u ​ x m ⌋ q = ∑ j = 0 p ( − 1) j ​ ( p j) ​ R p − j ​ ℋ j, q ​ ( N, m, u, B − u ​ R). \sum_{x=L}^{R}x^{p}\left\lfloor\frac{B-ux}{m}\right\rfloor^{q}=\sum_{j=0}^{p}(-1)^{j}\binom{p}{j}R^{p-j}\mathcal{H}_{j,q}(N;m,u,B-uR). |  |

###### Proof.

Let x = R − t x=R-t, where 0 ⩽ t ⩽ R − L 0\leqslant t\leqslant R-L. Then

 | ⌊ B − u ​ x m ⌋ = ⌊ B − u ​ R + u ​ t m ⌋, x p = ( R − t) p = ∑ j = 0 p ( − 1) j ​ ( p j) ​ R p − j ​ t j. \left\lfloor\frac{B-ux}{m}\right\rfloor=\left\lfloor\frac{B-uR+ut}{m}\right\rfloor,\qquad x^{p}=(R-t)^{p}=\sum_{j=0}^{p}(-1)^{j}\binom{p}{j}R^{p-j}t^{j}. |  |

Substituting and exchanging the finite sums gives the claim. ∎

In particular, each of the six sums in ( 4) is a linear combination of six-moment kernel values with nonnegative slope a = u a=u; these six direct states are already recursively closed, since the affine and reciprocal Euclidean steps do not increase the total weighted degree p + q p+q, so the family with q ⩾ 1 q\geqslant 1 and p + q ⩽ 3 p+q\leqslant 3 is stable. The exact transition formulas are recorded in \cref app:six-moments. The reciprocal step used below is analogous to the classical conjugation/reciprocity viewpoint in integer-partition decompositions [13].

###### Lemma 4 (affine closure of the six-moment kernel).

Each affine normalization step expresses a state ℋ p, q ​ ( N, m, a, b) \mathcal{H}_{p,q}(N;m,a,b) as a linear combination of states ℋ p ′, q ′ ​ ( N, m, a ′, b ′) \mathcal{H}_{p^{\prime},q^{\prime}}(N;m,a^{\prime},b^{\prime}) inside the same six-state family, together with ordinary polynomial sums.

###### Proof.

Write the floor argument as q 1 ​ t + q 0 + g ⁡ ( t) q_{1}t+q_{0}+g(t) after removing the easy Euclidean quotients. Expanding ( q 1 ​ t + q 0 + g ⁡ ( t)) q (q_{1}t+q_{0}+g(t))^{q} shows that every nontrivial term still has the form t p ′ ​ g ​ ( t) q ′ t^{p^{\prime}}g(t)^{q^{\prime}} with ( p ′, q ′) ∈ { ( 0, 1), ( 1, 1), ( 2, 1), ( 0, 2), ( 1, 2), ( 0, 3) } (p^{\prime},q^{\prime})\in\{(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)\}, while the terms with q ′ = 0 q^{\prime}=0 are ordinary polynomial sums. The explicit identities are listed in \cref app:six-moments. ∎

###### Lemma 5 (reciprocal closure of the six-moment kernel).

Under the reciprocal Euclidean step, each state of the six-moment family is expressible as a linear combination of states of the same family and polynomial sums.

###### Proof.

Write

 | ℋ p, q ​ ( N, m, a, b) = ∑ x = 0 N − 1 x p ​ y ​ ( x) q, y ⁡ ( x):= ⌊ a ​ x + b m ⌋, \mathcal{H}_{p,q}(N;m,a,b)=\sum_{x=0}^{N-1}x^{p}y(x)^{q},\qquad y(x):=\left\lfloor\frac{ax+b}{m}\right\rfloor, |  |

and assume 0 ⩽ a, b < m 0\leqslant a,b<m. Put

 | Y:= ⌊ a ⁡ ( N − 1) + b m ⌋. Y:=\left\lfloor\frac{a(N-1)+b}{m}\right\rfloor. |  |

Instead of summing by columns indexed by x x, we regroup the same staircase region by horizontal levels t = 0, 1, …, Y − 1 t=0,1,\dots,Y-1. The condition y ⁡ ( x) ⩾ t + 1 y(x)\geqslant t+1 is equivalent to

 | x ⩾ ⌊ m ​ t + ( m − b − 1) a ⌋ + 1. x\geqslant\left\lfloor\frac{mt+(m-b-1)}{a}\right\rfloor+1. |  |

Hence the transposed staircase is encoded by the reciprocal floor function

 | g ⁡ ( t):= ⌊ m ​ t + ( m − b − 1) a ⌋, 0 ⩽ t < Y, g(t):=\left\lfloor\frac{mt+(m-b-1)}{a}\right\rfloor,\qquad 0\leqslant t<Y, |  |

which is exactly the same construction with the roles of a a and m m interchanged. When one rewrites the sums over the horizontal strips, the lower bounds contribute only polynomial weights in t t, so every term becomes a linear combination of moments

 | ∑ t = 0 Y − 1 t p ′ ​ g ​ ( t) q ′ = ℋ p ′, q ′ ​ ( Y, a, m, m − b − 1), \sum_{t=0}^{Y-1}t^{p^{\prime}}g(t)^{q^{\prime}}=\mathcal{H}_{p^{\prime},q^{\prime}}(Y;a,m,m-b-1), |  |

with ( p ′, q ′) ∈ { ( 0, 1), ( 1, 1), ( 2, 1), ( 0, 2), ( 1, 2), ( 0, 3) } (p^{\prime},q^{\prime})\in\{(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)\}, together with ordinary power sums. Thus the same six-state family is preserved under the reciprocal step, and the larger Euclidean parameter decreases from m m to a < m a<m. The explicit coefficient identities are listed in \cref app:six-moments. ∎

###### Corollary 6 (evaluation of the six-moment kernel).

For fixed integers ( n, m, a, b) (n,m,a,b), the six moments in ( 4) can be computed in time O ⁡ ( log ⁡ n) O(\log n) by an Euclidean recursion. The recursive system is closed: no moments outside the family ( 4) are generated.

###### Proof.

By \cref lem:six-affine,lem:six-reciprocal, the recursion alternates between two Euclidean-style operations: affine normalization replaces ( a, b) (a,b) by their residues modulo m m, and the reciprocal step then swaps the active pair ( m, a) (m,a) to ( a, m) (a,m) with a < m a<m. Thus after each nontrivial cycle the larger Euclidean parameter strictly decreases, exactly as in the ordinary Euclidean algorithm. The recursion therefore has depth O ⁡ ( log ⁡ m) = O ⁡ ( log ⁡ n) O(\log m)=O(\log n), and each step performs only O ⁡ ( 1) O(1) arithmetic operations on the constant-size family of moments. Hence the six-moment kernel is evaluable in O ⁡ ( log ⁡ n) O(\log n) time. ∎

On the first segment, all required quantities reduce to polynomial sums, hence are computable in O ⁡ ( 1) O(1) time. On the second segment, \cref lem:six-sign-reversal,cor:floor-kernel gives an O ⁡ ( log ⁡ n) O(\log n) evaluation.

###### Corollary 7.

For a fixed primitive direction ( u, v) (u,v) with u ⩾ v ⩾ 1 u\geqslant v\geqslant 1, the contribution c u, v ​ ( n) c_{u,v}(n) can be computed in time O ⁡ ( log ⁡ n). O(\log n).

Since the number of primitive pairs with u ⩽ B u\leqslant B is O ⁡ ( B 2) O(B^{2}), the total cost of the small part is O ⁡ ( B 2 ​ log ⁡ n) = O ⁡ ( n 4 / 3 ​ log ⁡ n). O(B^{2}\log n)=O(n^{4/3}\log n).

### 5.2 Large directions

We now consider the complementary region u > B = n 2 / 3 u>B=n^{2/3}. Geometrically, this is completely analogous to the large-direction analysis in \cref sec:sqrt. The difference is only that the cutoff is now B = n 2 / 3 B=n^{2/3} and that, instead of the square-root sweep, we evaluate the resulting one-dimensional sums by coprime prefix sums.

 | ∑ u > B O ⁡ ( τ ⁡ ( u) ​ ( n u) 2) = O ⁡ ( n 2 ​ ∑ u > B τ ⁡ ( u) u 2) = O ⁡ ( n 2 ​ log ⁡ n B) = O ⁡ ( n 4 / 3 ​ log ​ n). \sum_{u>B}O\!\left(\tau(u)\Bigl(\frac{n}{u}\Bigr)^{2}\right)=O\!\left(n^{2}\sum_{u>B}\frac{\tau(u)}{u^{2}}\right)=O\!\left(\frac{n^{2}\log n}{B}\right)=O(n^{4/3}\log n). |  |

Thus the large-direction part matches the cost of the small-direction part, but it uses a different kernel: coprime prefix sums of orders 0, 1, 2 0,1,2, not floor moments.

###### Theorem 8 (cubic-root decomposition).

The lattice-rectangle counting problem admits an algorithm of complexity O ⁡ ( n 4 / 3 ​ log ⁡ n). O(n^{4/3}\log n).

Fix B = ⌊ n 2 / 3 ⌋ B=\left\lfloor n^{2/3}\right\rfloor. For u ⩽ B u\leqslant B, each primitive direction is reduced to O ⁡ ( 1) O(1) queries to the six-moment kernel; for u > B u>B, the dual parametrization is handled by the coprime prefix sums C 0, C 1, C 2 C_{0},C_{1},C_{2}. The main text proves the reduction and the resulting complexity bound, while \cref app:pseudocode and \cref app:six-moments record the corresponding implementation details and explicit kernel transitions.

## 6 A ten-moment reduction to weighted floor sums: O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n)

We now turn to the ten-moment weighted-floor-sum reduction. This section explains how the quantities R u, y, d R_{u,y,d} arise and how they reduce to weighted floor sums. We first isolate the required weighted floor-sum queries and derive the global complexity conditionally on an O ⁡ ( log ⁡ n) O(\log n) query bound; this temporary assumption is discharged below by proving that the relevant kernel is recursively closed and evaluable in O ⁡ ( log ⁡ n) O(\log n) time.

### 6.1 From primitive directions to Möbius inversion

We start from the contribution of the non-axis-parallel directions, restricting to u > v ⩾ 1 u>v\geqslant 1. The coprimality condition is removed by the Möbius identity. Writing v = d ​ t v=dt with d | u d\mid u, t ⩾ 1 t\geqslant 1, and d ​ t < u dt<u, we obtain

 | F 1 ​ ( n) = ∑ u = 2 n ∑ d | u μ ⁡ ( d) ≠ 0 μ ⁡ ( d) ​ ∑ 1 ⩽ t < u / d ∑ x ⩾ y ⩾ 1 x ​ u + y ​ d ​ t ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − y ​ dt) ​ ( n − x ​ dt − yu). F_{1}(n)=\sum_{u=2}^{n}\sum_{\begin{subarray}{c}d\mid u\\ \mu(d)\neq 0\end{subarray}}\mu(d)\sum_{1\leqslant t<u/d}\sum_{\begin{subarray}{c}x\geqslant y\geqslant 1\\ xu+y\,dt\leqslant n\end{subarray}}\mult(x,y)\,(n-xu-y\,dt)(n-x\,dt-yu). |  |

Now fix u u, y y, and d d. The remaining inner contribution depends only on these three outer parameters, so we define

 | R u, y, d:= ∑ 1 ⩽ t < u / d ∑ x ⩾ y ⩾ 1 x ​ u + y ​ d ​ t ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − y ​ dt) ​ ( n − x ​ dt − yu). R_{u,y,d}:=\sum_{1\leqslant t<u/d}\sum_{\begin{subarray}{c}x\geqslant y\geqslant 1\\ xu+y\,dt\leqslant n\end{subarray}}\mult(x,y)\,(n-xu-y\,dt)(n-x\,dt-yu). |  | (6) |

Since necessarily 1 ⩽ y ⩽ ⌊ n / u ⌋ 1\leqslant y\leqslant\lfloor n/u\rfloor, the whole sum becomes

 | F 1 ​ ( n) = ∑ u = 2 n ∑ 1 ⩽ y ⩽ ⌊ n / u ⌋ ∑ d | u μ ⁡ ( d) ​ R u, y, d. F_{1}(n)=\sum_{u=2}^{n}\sum_{1\leqslant y\leqslant\lfloor n/u\rfloor}\sum_{d\mid u}\mu(d)\,R_{u,y,d}. |  | (7) |

### 6.2 How many outer triples?

Let T ⁡ ( n) T(n) be the number of admissible outer triples ( u, y, d) (u,y,d), where 1 ⩽ y ⩽ ⌊ n / u ⌋ 1\leqslant y\leqslant\lfloor n/u\rfloor and d | u d\mid u is squarefree. For fixed u u, the number of squarefree divisors of u u equals 2 ω ⁡ ( u) 2^{\omega(u)}, where ω ⁡ ( u) \omega(u) is the number of distinct prime divisors of u u. Thus

 | T ⁡ ( n) = ∑ u ⩽ n 2 ω ⁡ ( u) ​ ⌊ n u ⌋. T(n)=\sum_{u\leqslant n}2^{\omega(u)}\Bigl\lfloor\frac{n}{u}\Bigr\rfloor. |  |

For the algorithmic analysis we only need the upper bound T ⁡ ( n) = O ⁡ ( n ​ log 2 ​ n) T(n)=O(n\log^{2}n). Indeed, this upper bound follows from ⌊ n / u ⌋ ⩽ n / u \lfloor n/u\rfloor\leqslant n/u, which gives T ⁡ ( n) ⩽ n ​ ∑ u ⩽ n 2 ω ⁡ ( u) / u T(n)\leqslant n\sum_{u\leqslant n}2^{\omega(u)}/u. Next, using 2 ω ⁡ ( m) = ∑ d | m μ 2 ​ ( d) 2^{\omega(m)}=\sum_{d\mid m}\mu^{2}(d), where μ 2 ​ ( d) \mu^{2}(d) is the indicator of squarefree integers, we obtain

 | ∑ u ⩽ n 2 ω ⁡ ( u) u = ∑ d ⩽ n μ 2 ​ ( d) d ​ ∑ m ⩽ n / d 1 m. \sum_{u\leqslant n}\frac{2^{\omega(u)}}{u}=\sum_{d\leqslant n}\frac{\mu^{2}(d)}{d}\sum_{m\leqslant n/d}\frac{1}{m}. |  |

Now ∑ m ⩽ X 1 / m = O ⁡ ( log ⁡ X) \sum_{m\leqslant X}1/m=O(\log X) and ∑ d ⩽ n μ 2 ​ ( d) / d = O ⁡ ( log ⁡ n) \sum_{d\leqslant n}\mu^{2}(d)/d=O(\log n), so ∑ u ⩽ n 2 ω ⁡ ( u) / u = O ⁡ ( log 2 ⁡ n) \sum_{u\leqslant n}2^{\omega(u)}/u=O(\log^{2}n) and therefore T ⁡ ( n) = O ⁡ ( n ​ log 2 ​ n). T(n)=O(n\log^{2}n). Consequently, if each set R u, y, d R_{u,y,d} can be processed in time O ⁡ ( log ⁡ n) O(\log n) then the total running time is O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n). The remainder of this section proves exactly this O ⁡ ( log ⁡ n) O(\log n) evaluation bound by showing that all required weighted floor sums belong to a finite recursively closed Euclidean kernel.

### 6.3 Weighted floor-sum reduction

The purpose of this subsection is to isolate the one-dimensional arithmetic kernel behind the ten-moment algorithm. The explicit affine and reciprocal transition identities for this kernel are somewhat lengthy and are therefore deferred to \cref app:ten-moments; here we state the kernel, explain why it is the right one, and derive the global O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) bound from the structural properties proved there.

Fix u, y, d u,y,d. By definition,

 | R u, y, d = ∑ t < u / d ∑ x ⩾ y ⩾ 1 x ​ u + y ​ d ​ t ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − y ​ dt) ​ ( n − x ​ dt − yu). R_{u,y,d}=\sum_{t<u/d}\sum_{\begin{subarray}{c}x\geqslant y\geqslant 1\\ xu+y\,dt\leqslant n\end{subarray}}\mult(x,y)\,(n-xu-y\,dt)(n-x\,dt-yu). |  |

For each fixed x ⩾ y x\geqslant y, the variable t t runs over

 | 1 ⩽ t ⩽ T ⁡ ( x), T ⁡ ( x):= min ⁡ ( ⌊ u − 1 d ⌋, ⌊ n − u ​ x y ​ d ⌋). 1\leqslant t\leqslant T(x),\qquad T(x):=\min\!\left(\Bigl\lfloor\frac{u-1}{d}\Bigr\rfloor,\,\Bigl\lfloor\frac{n-ux}{yd}\Bigr\rfloor\right). |  |

Write

 | T 0:= ⌊ u − 1 d ⌋, G ⁡ ( x):= ⌊ n − u ​ x y ​ d ⌋. T_{0}:=\Bigl\lfloor\frac{u-1}{d}\Bigr\rfloor,\qquad G(x):=\Bigl\lfloor\frac{n-ux}{yd}\Bigr\rfloor. |  |

Then the summation over x x naturally splits into two zones:

- •

the *capped zone*, where G ⁡ ( x) ⩾ T 0 G(x)\geqslant T_{0} and therefore T ⁡ ( x) = T 0 T(x)=T_{0};

- •

the *active-floor zone*, where 1 ⩽ G ⁡ ( x) < T 0 1\leqslant G(x)<T_{0} and therefore T ⁡ ( x) = G ⁡ ( x) T(x)=G(x).

The split point is determined by the inequality n − u ​ x ⩾ y ​ d ​ T 0 n-ux\geqslant ydT_{0}, that is,

 | x ⩽ X 0:= ⌊ n − y ​ d ​ T 0 u ⌋. x\leqslant X_{0}:=\Bigl\lfloor\frac{n-ydT_{0}}{u}\Bigr\rfloor. |  |

Hence the capped zone contributes only polynomial sums in x x, while the active-floor zone is exactly where the weighted floor-sum kernel appears. More precisely,

 | R u, y, d = ∑ y ⩽ x ⩽ X 0 𝒲 ⁡ ( x, y) ​ S x cap + ∑ x > X 0 𝒲 ⁡ ( x, y) ​ S x act, where R_{u,y,d}=\sum_{y\leqslant x\leqslant X_{0}}\mult(x,y)\,S_{x}^{\mathrm{cap}}+\sum_{x>X_{0}}\mult(x,y)\,S_{x}^{\mathrm{act}},\quad\text{where} |  |

 | S x cap:= ∑ 1 ⩽ t ⩽ T 0 ( n − x ​ u − y ​ d ​ t) ​ ( n − x ​ d ​ t − y ​ u), S x act:= ∑ 1 ⩽ t ⩽ G ⁡ ( x) ( n − x ​ u − y ​ d ​ t) ​ ( n − x ​ d ​ t − y ​ u). S_{x}^{\mathrm{cap}}:=\sum_{1\leqslant t\leqslant T_{0}}(n-xu-y\,dt)(n-xdt-yu),\qquad S_{x}^{\mathrm{act}}:=\sum_{1\leqslant t\leqslant G(x)}(n-xu-y\,dt)(n-xdt-yu). |  |

In the capped zone the inner sum is a polynomial in x x because the upper limit T 0 T_{0} is constant, and in the active-floor zone the same expansion reduces everything to moments of G ⁡ ( x) = ⌊ ( n − u ​ x) / ( y ​ d) ⌋ G(x)=\left\lfloor(n-ux)/(yd)\right\rfloor. Expanding the summand as a quadratic polynomial in t t, we obtain

 | ( n − x ​ u − y ​ d ​ t) ​ ( n − x ​ d ​ t − y ​ u) = P 0 ​ ( x) + P 1 ​ ( x) ​ t + P 2 ​ ( x) ​ t 2, where (n-xu-y\,dt)(n-xdt-yu)=P_{0}(x)+P_{1}(x)t+P_{2}(x)t^{2},\quad\text{where} |  |

 | P 0 ​ ( x) = ( n − x ​ u) ​ ( n − y ​ u), P 1 ​ ( x) = − d ⁡ ( y ⁡ ( n − y ​ u) + x ⁡ ( n − x ​ u)), P 2 ​ ( x) = x ​ y ​ d 2. P_{0}(x)=(n-xu)(n-yu),\qquad P_{1}(x)=-d\bigl(y(n-yu)+x(n-xu)\bigr),\qquad P_{2}(x)=xyd^{2}. |  |

Using the identities

 | ∑ t = 1 T 1 = T, ∑ t = 1 T t = T ⁡ ( T + 1) 2, ∑ t = 1 T t 2 = T ​ ( T + 1) ​ ( 2 ​ T + 1) 6, \sum_{t=1}^{T}1=T,\qquad\sum_{t=1}^{T}t=\frac{T(T+1)}{2},\qquad\sum_{t=1}^{T}t^{2}=\frac{T(T+1)(2T+1)}{6}, |  |

we see that each inner sum is a polynomial in x x and in its upper limit T 0 T_{0} or G ⁡ ( x) G(x). Thus the direct expansion expresses R u, y, d R_{u,y,d} through the following seven basic weighted floor sums:

 |  | ∑ T ⁡ ( x), ∑ x ​ T ​ ( x), ∑ x 2 ​ T ​ ( x), \displaystyle\sum T(x),\quad\sum xT(x),\quad\sum x^{2}T(x), | ∑ T ​ ( x) 2, ∑ x ​ T ​ ( x) 2, ∑ x 2 ​ T ​ ( x) 2, ∑ x ​ T ​ ( x) 3. \displaystyle\sum T(x)^{2},\quad\sum xT(x)^{2},\quad\sum x^{2}T(x)^{2},\quad\sum xT(x)^{3}. |  |

Now 𝒲 ⁡ ( x, y) = 4 − 2 ​ 1 x = y \mult(x,y)=4-2\,\mathbf{1}_{x=y}, so the diagonal contribution x = y x=y contributes only a constant-size correction.

###### Lemma 9 (direct weighted floor-sum reduction).

For fixed ( u, y, d) (u,y,d), the quantity R u, y, d R_{u,y,d} is a linear combination of the seven basic sums displayed above over the active-floor zone x > X 0 x>X_{0}, together with ordinary polynomial sums in x x coming from the capped zone y ⩽ x ⩽ X 0 y\leqslant x\leqslant X_{0} and the diagonal correction x = y x=y.

The seven direct states are not closed under the Euclidean transitions. We therefore enlarge them to the ten-moment family from \cref app:ten-moments. For integers N ⩾ 0 N\geqslant 0, m ⩾ 1 m\geqslant 1, and a, b ⩾ 0 a,b\geqslant 0, define

 | ℋ p, q ​ ( N, m, a, b):= ∑ x = 0 N − 1 x p ​ ⌊ a ​ x + b m ⌋ q, q ⩾ 1, p ⩾ 0, p + q ⩽ 4. \mathcal{H}_{p,q}(N;m,a,b):=\sum_{x=0}^{N-1}x^{p}\left\lfloor\frac{ax+b}{m}\right\rfloor^{q},\qquad q\geqslant 1,\quad p\geqslant 0,\quad p+q\leqslant 4. |  | (8) |

Equivalently, the state space is indexed by

 | ( p, q) ∈ { ( 0, 1), ( 1, 1), ( 2, 1), ( 3, 1), ( 0, 2), ( 1, 2), ( 2, 2), ( 0, 3), ( 1, 3), ( 0, 4) }. (p,q)\in\{(0,1),(1,1),(2,1),(3,1),(0,2),(1,2),(2,2),(0,3),(1,3),(0,4)\}. |  |

As in the six-state kernel discussed earlier, the affine and reciprocal Euclidean steps do not increase the total weighted degree p + q p+q; since the seven direct queries all satisfy p + q ⩽ 4 p+q\leqslant 4, their closure is therefore contained in the ten-state family above, while the five cases with q = 0 q=0 are ordinary monomial sums treated separately. Since the floor term has negative slope in x x, we first reverse the index. Thus for any interval [L, R] [L,R],

 | ∑ x = L R x p ​ ⌊ N − u ​ x y ​ d ⌋ q = ∑ j = 0 p ( − 1) j ​ ( p j) ​ R p − j ​ ℋ j, q ​ ( R − L + 1, y ​ d, u, N − u ​ R). \sum_{x=L}^{R}x^{p}\left\lfloor\frac{N-ux}{yd}\right\rfloor^{q}=\sum_{j=0}^{p}(-1)^{j}\binom{p}{j}R^{p-j}\mathcal{H}_{j,q}(R-L+1;yd,u,N-uR). |  |

###### Lemma 10 (affine closure of the weighted kernel).

For the evaluation of ( 8), each affine normalization step expresses a state ℋ p, q ​ ( N, m, a, b) \mathcal{H}_{p,q}(N;m,a,b) as a linear combination of states ℋ p ′, q ′ ​ ( N, m, a ′, b ′) \mathcal{H}_{p^{\prime},q^{\prime}}(N;m,a^{\prime},b^{\prime}) with q ′ ⩾ 1 q^{\prime}\geqslant 1, p ′ ⩾ 0 p^{\prime}\geqslant 0, p ′ + q ′ ⩽ 4 p^{\prime}+q^{\prime}\leqslant 4, together with polynomial sums.

###### Lemma 11 (reciprocal closure of the weighted kernel).

Under the reciprocal Euclidean step, each state of the extended family is expressible as a linear combination of states of the same family and polynomial sums.

###### Corollary 12 (evaluation of the weighted kernel).

The ten-moment kernel ( 8) is evaluable in O ⁡ ( log ⁡ n) O(\log n) time.

The proofs follow the same Euclidean-recursion scheme as in \cref lem:six-affine,lem:six-reciprocal,cor:floor-kernel. The same affine and reciprocal Euclidean steps preserve the enlarged ten-state family; only the explicit coefficient formulas are longer, so they are deferred to \cref app:ten-moments.

###### Corollary 13 (evaluation of outer contributions).

Each outer contribution R u, y, d R_{u,y,d} is computable in time O ⁡ ( log ⁡ n) O(\log n).

###### Proof.

By Lemma 9, each R u, y, d R_{u,y,d} reduces to a constant number of shifted instances of the ten-moment kernel ( 8) plus polynomial sums. By Corollary 12, each such kernel query costs O ⁡ ( log ⁡ n) O(\log n) time, while the polynomial-zone contribution is evaluated in O ⁡ ( 1) O(1) time. ∎

Combining the O ⁡ ( log ⁡ n) O(\log n) evaluation of each outer contribution R u, y, d R_{u,y,d} with the O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) bound on the number of admissible outer triples yields the stated complexity bound. For an explicit implementation, we also precompute the Möbius values and the squarefree divisor lists

 | D ( u) = { ( d, μ ( d)): d ∣ u, d squarefree }, u ⩽ n. D(u)=\{(d,\mu(d)):d\mid u,\ d\text{ squarefree}\},\qquad u\leqslant n. |  |

These lists can be generated from a smallest-prime-factor sieve; their total size is ∑ u ⩽ n 2 ω ⁡ ( u) = O ⁡ ( n ​ log ⁡ n) \sum_{u\leqslant n}2^{\omega(u)}=O(n\log n). Thus the preprocessing time and storage are O ⁡ ( n ​ log ⁡ n) O(n\log n) and are dominated by the main O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) summation.

###### Theorem 14 (ten-moment complexity).

After O ⁡ ( n ​ log ⁡ n) O(n\log n) preprocessing and using O ⁡ ( n ​ log ⁡ n) O(n\log n) storage for the squarefree divisor lists, the lattice-rectangle counting problem admits an exact O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) algorithm.

###### Proof.

There are O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) admissible triples ( u, y, d) (u,y,d), and each corresponding contribution R u, y, d R_{u,y,d} is computable in O ⁡ ( log ⁡ n) O(\log n) time by Corollary 13. Summing over all outer triples proves the stated running time. The squarefree-list preprocessing has size and construction time O ⁡ ( n ​ log ⁡ n) O(n\log n), so it does not change the asymptotic time bound; it accounts for the stated storage. ∎

Algorithmically, the ten-moment method iterates over the admissible outer triples ( u, y, d) (u,y,d), evaluates each contribution R u, y, d R_{u,y,d} by the recursive weighted floor-sum kernel, and accumulates it with weight μ ⁡ ( d) \mu(d). The next two sections give the faster divisor-layer one-value algorithm and the all-values algorithm; see \cref app:pseudocode,app:ten-moments for the corresponding pseudocode and full transition identities for this ten-moment stage.

## 7 A divisor-layer algorithm for one value: O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n)

The ten-moment algorithm of \cref sec:final inserts Möbius inversion inside a larger summation over directions and side lengths. The final one-value improvement comes from reversing this order. We keep the Möbius divisor fixed, remove the coprimality condition for the whole layer at once, and then apply the same square-root principle used in the earlier decompositions. Thus the proof has three parts: a divisor-layer identity, a disjoint square-root cover inside one primitive-free layer, and a reduction of the required layer moments to the six-state floor-sum kernel.

### 7.1 Divisor layers

Let F 1 ​ ( n) F_{1}(n) denote the non-axis-parallel contribution, so that F ⁡ ( n) = F 0 ​ ( n) + F 1 ​ ( n) F(n)=F_{0}(n)+F_{1}(n) and F 0 ​ ( n) F_{0}(n) is the closed-form term handled earlier. In the standard variables,

 | F 1 ​ ( n) = ∑ u > v > 0, x ⩾ y ⩾ 1 gcd ⁡ ( u, v) = 1, x ​ u + y ​ v ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − yv) ​ ( n − xv − yu). F_{1}(n)=\sum_{\begin{subarray}{c}u>v>0,\ x\geqslant y\geqslant 1\\ \gcd(u,v)=1,\ xu+yv\leqslant n\end{subarray}}\mult(x,y)\,(n-xu-yv)(n-xv-yu). |  | (9) |

Here, as before, 𝒲 ⁡ ( x, y) = 2 \mult(x,y)=2 for x = y x=y and 𝒲 ⁡ ( x, y) = 4 \mult(x,y)=4 for x > y x>y. We now insert

 | 𝟏 gcd ⁡ ( u, v) = 1 = ∑ d | u, d | v μ ⁡ ( d). \mathbf{1}_{\gcd(u,v)=1}=\sum_{d\mid u,\ d\mid v}\mu(d). |  |

All sums are finite, so the order of summation may be changed. In the summand with fixed d d, write u = d ​ a u=da and v = d ​ b v=db. Then x ​ u + y ​ v ⩽ n xu+yv\leqslant n becomes a ​ x + b ​ y ⩽ ⌊ n / d ⌋ ax+by\leqslant\lfloor n/d\rfloor. Hence

 | F 1 ​ ( n) = ∑ d ⩽ n μ ⁡ ( d) ​ S d ​ ( n), F_{1}(n)=\sum_{d\leqslant n}\mu(d)S_{d}(n), |  | (10) |

where N d = ⌊ n / d ⌋ N_{d}=\lfloor n/d\rfloor and

 | S d ​ ( n) = ∑ a > b ⩾ 1, x ⩾ y ⩾ 1 a ​ x + b ​ y ⩽ N d 𝒲 ⁡ ( x, y) ​ ( n − d ⁡ ( ax + by)) ​ ( n − d ⁡ ( bx + ay)). S_{d}(n)=\sum_{\begin{subarray}{c}a>b\geqslant 1,\ x\geqslant y\geqslant 1\\ ax+by\leqslant N_{d}\end{subarray}}\mult(x,y)\bigl(n-d(ax+by)\bigr)\bigl(n-d(bx+ay)\bigr). |  | (11) |

This is the same contribution as in ( 9): summing μ ⁡ ( d) \mu(d) over common divisors of u u and v v restores exactly the primitive-direction condition. The advantage is that the inner layer ( 11) is primitive-free. Its weight is the quadratic polynomial

 | ( n − d ⁡ ( a ​ x + b ​ y)) ​ ( n − d ⁡ ( b ​ x + a ​ y)) = n 2 − n ​ d ​ ( a + b) ​ ( x + y) + d 2 ​ ( a ​ b ​ ( x 2 + y 2) + ( a 2 + b 2) ​ x ​ y). \bigl(n-d(ax+by)\bigr)\bigl(n-d(bx+ay)\bigr)=n^{2}-nd(a+b)(x+y)+d^{2}\bigl(ab(x^{2}+y^{2})+(a^{2}+b^{2})xy\bigr). |  | (12) |

Thus each layer reduces to quadratic moments over the region a > b a>b, x ⩾ y x\geqslant y, a ​ x + b ​ y ⩽ N d ax+by\leqslant N_{d}.

### 7.2 A square-root cover inside one layer

Fix d d, write N = N d N=N_{d}, and put B = ⌊ N ⌋ B=\lfloor\sqrt{N}\rfloor. Since a ​ x ⩽ a ​ x + b ​ y ⩽ N ax\leqslant ax+by\leqslant N, an admissible tuple cannot have both a > B a>B and x > B x>B. We use the disjoint form of this square-root cover,

 | { a x + b y ⩽ N, a > b, x ⩾ y } = { x ⩽ B } ⊔ { a ⩽ B, x > B }. \{ax+by\leqslant N,\ a>b,\ x\geqslant y\}=\{x\leqslant B\}\ \sqcup\ \{a\leqslant B,\ x>B\}. |  | (13) |

It is equivalent to the symmetric cover { a ⩽ B } ∪ { x ⩽ B } \{a\leqslant B\}\cup\{x\leqslant B\}, but avoids an explicit inclusion–exclusion step. The first part fixes a small side pair and sums over all direction pairs; the second fixes a small direction pair and keeps only the large-side range x > B x>B, which is imposed by subtracting capped side moments. For 1 ⩽ q < p ⩽ B 1\leqslant q<p\leqslant B and 0 ⩽ i + j ⩽ 2 0\leqslant i+j\leqslant 2, define

 | M i ​ j ​ ( p, q, N) = ∑ X ⩾ Y ⩾ 1 p ​ X + q ​ Y ⩽ N X i ​ Y j, T = ⌊ N p + q ⌋, D j ​ ( T) = ∑ t = 1 T t j. M_{ij}(p,q;N)=\sum_{\begin{subarray}{c}X\geqslant Y\geqslant 1\\ pX+qY\leqslant N\end{subarray}}X^{i}Y^{j},\qquad T=\left\lfloor\frac{N}{p+q}\right\rfloor,\qquad D_{j}(T)=\sum_{t=1}^{T}t^{j}. |  | (14) |

Here p, q p,q denote the fixed pair, and X, Y X,Y denote the remaining pair being summed. Let

 | Φ p, q ( d) = \displaystyle\Phi_{p,q}^{(d)}={} | n 2 ​ M 00 − n ​ d ​ ( p + q) ​ ( M 10 + M 01) \displaystyle n^{2}M_{00}-nd(p+q)(M_{10}+M_{01}) |  | (15) |

 |  | + d 2 ​ p ​ q ​ ( M 20 + M 02) + d 2 ​ ( p 2 + q 2) ​ M 11, \displaystyle+d^{2}pq(M_{20}+M_{02})+d^{2}(p^{2}+q^{2})M_{11}, |  |

where the moments are evaluated at ( p, q, N) (p,q;N). Thus Φ p, q ( d) \Phi_{p,q}^{(d)} is the unweighted sum of ( 12) after fixing one ordered non-diagonal pair equal to ( p, q) (p,q). Let

 | Δ p, q ( d) = n 2 ​ D 0 ​ ( T) − 2 ​ n ​ d ​ ( p + q) ​ D 1 ​ ( T) + d 2 ​ ( p + q) 2 ​ D 2 ​ ( T). \Delta_{p,q}^{(d)}=n^{2}D_{0}(T)-2nd(p+q)D_{1}(T)+d^{2}(p+q)^{2}D_{2}(T). |  | (16) |

We also use capped moments

 | M i ​ j ∩ ​ ( p, q, N, B) = ∑ B ⩾ X ⩾ Y ⩾ 1 p ​ X + q ​ Y ⩽ N X i ​ Y j M_{ij}^{\cap}(p,q;N,B)=\sum_{\begin{subarray}{c}B\geqslant X\geqslant Y\geqslant 1\\ pX+qY\leqslant N\end{subarray}}X^{i}Y^{j} |  |

and define Φ p, q ( d), ∩ \Phi_{p,q}^{(d),\cap} from ( 15) with M i ​ j M_{ij} replaced by M i ​ j ∩ M_{ij}^{\cap}. The capped diagonal term Δ p, q ( d), ∩ \Delta_{p,q}^{(d),\cap} is obtained from ( 16) with T T replaced by min ⁡ ( B, ⌊ N / ( p + q) ⌋) \min(B,\lfloor N/(p+q)\rfloor).

There remains the diagonal-side part of the first set in ( 13). For x = y = t ⩽ B x=y=t\leqslant B put

 | C t ( d) = 2 ​ ∑ s ⩽ N / t ⌊ s − 1 2 ⌋ ​ ( n − d ​ t ​ s) 2. C_{t}^{(d)}=2\sum_{s\leqslant N/t}\left\lfloor\frac{s-1}{2}\right\rfloor(n-dts)^{2}. |  | (17) |

Here s = a + b s=a+b, and ⌊ ( s − 1) / 2 ⌋ \lfloor(s-1)/2\rfloor is the number of pairs a > b ⩾ 1 a>b\geqslant 1 with sum s s.

###### Lemma 15 (one layer formula).

For every d ⩽ n d\leqslant n,

 | S d ​ ( n) = ∑ 1 ⩽ q < p ⩽ B ( 8 ​ Φ p, q ( d) − 6 ​ Δ p, q ( d) − 4 ​ Φ p, q ( d), ∩ + 2 ​ Δ p, q ( d), ∩) + ∑ t = 1 B C t ( d). S_{d}(n)=\sum_{1\leqslant q<p\leqslant B}\left(8\Phi_{p,q}^{(d)}-6\Delta_{p,q}^{(d)}-4\Phi_{p,q}^{(d),\cap}+2\Delta_{p,q}^{(d),\cap}\right)+\sum_{t=1}^{B}C_{t}^{(d)}. |  | (18) |

###### Proof.

Use the disjoint cover ( 13). First consider the part x ⩽ B x\leqslant B. If the fixed side is non-diagonal, say ( x, y) = ( p, q) (x,y)=(p,q) with p > q p>q, then the direction variables satisfy a > b a>b and therefore the diagonal a = b a=b must be removed completely. The quadratic weight ( 12) is symmetric under simultaneously exchanging the fixed pair and the summed pair, so the required moment is the same Φ p, q ( d) \Phi_{p,q}^{(d)}. Thus the non-diagonal side contribution is 4 ​ Φ p, q ( d) − 4 ​ Δ p, q ( d) 4\Phi_{p,q}^{(d)}-4\Delta_{p,q}^{(d)}. The diagonal sides in this same part have x = y = t ⩽ B x=y=t\leqslant B and contribute the terms C t ( d) C_{t}^{(d)}.

It remains to count the second disjoint part, where a ⩽ B a\leqslant B and x > B x>B. Fix the direction ( a, b) = ( p, q) (a,b)=(p,q). Without the restriction x > B x>B, summing over all sides gives 4 ​ Φ p, q ( d) − 2 ​ Δ p, q ( d) 4\Phi_{p,q}^{(d)}-2\Delta_{p,q}^{(d)}, because the side multiplier is 4 4 for X > Y X>Y and 2 2 for X = Y X=Y. The excluded subrange x ⩽ B x\leqslant B is exactly the capped contribution 4 ​ Φ p, q ( d), ∩ − 2 ​ Δ p, q ( d), ∩ 4\Phi_{p,q}^{(d),\cap}-2\Delta_{p,q}^{(d),\cap}. Hence this second part contributes

 | 4 ​ Φ p, q ( d) − 2 ​ Δ p, q ( d) − 4 ​ Φ p, q ( d), ∩ + 2 ​ Δ p, q ( d), ∩. 4\Phi_{p,q}^{(d)}-2\Delta_{p,q}^{(d)}-4\Phi_{p,q}^{(d),\cap}+2\Delta_{p,q}^{(d),\cap}. |  |

Adding it to the non-diagonal and diagonal pieces of the x ⩽ B x\leqslant B part gives ( 18). ∎

### 7.3 Moment evaluation and complexity

It remains to show that the moments in ( 18) are cheap. For example,

 | M i ​ j ​ ( p, q, N) = ∑ Y = 1 ⌊ N / ( p + q) ⌋ Y j ​ ( P i ​ ( ⌊ N − q ​ Y p ⌋) − P i ​ ( Y − 1)), M_{ij}(p,q;N)=\sum_{Y=1}^{\lfloor N/(p+q)\rfloor}Y^{j}\left(P_{i}\!\left(\left\lfloor\frac{N-qY}{p}\right\rfloor\right)-P_{i}(Y-1)\right), |  | (19) |

where P i ​ ( R) = ∑ 1 ⩽ X ⩽ R X i P_{i}(R)=\sum_{1\leqslant X\leqslant R}X^{i}. Since i ⩽ 2 i\leqslant 2, expanding P i P_{i} expresses every non-polynomial term as a constant-size linear combination of sums

 | ∑ 0 ⩽ z < m z α ​ ⌊ A ​ z + C M ⌋ β, ( α, β) ∈ { ( 0, 1), ( 1, 1), ( 2, 1), ( 0, 2), ( 1, 2), ( 0, 3) }, \sum_{0\leqslant z<m}z^{\alpha}\left\lfloor\frac{Az+C}{M}\right\rfloor^{\beta},\qquad(\alpha,\beta)\in\{(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)\}, |  | (20) |

up to harmless shifts of the summation interval. This is precisely the six-state kernel of \cref app:six-moments. Capped moments are treated the same way: in

 | M i ​ j ∩ ​ ( p, q, N, B) = ∑ Y = 1 min ⁡ ( B, ⌊ N / ( p + q) ⌋) Y j ​ ( P i ​ ( min ⁡ ( B, ⌊ N − q ​ Y p ⌋)) − P i ​ ( Y − 1)), M_{ij}^{\cap}(p,q;N,B)=\sum_{Y=1}^{\min(B,\lfloor N/(p+q)\rfloor)}Y^{j}\left(P_{i}\!\left(\min\!\left(B,\left\lfloor\frac{N-qY}{p}\right\rfloor\right)\right)-P_{i}(Y-1)\right), |  |

the minimum is removed by splitting the range of Y Y at ⌊ ( N − p ​ B) / q ⌋ \lfloor(N-pB)/q\rfloor, with empty ranges ignored. One side of the split is polynomial, and the other is another instance of ( 20). Finally, each C t ( d) C_{t}^{(d)} is a sum over s s of a quadratic polynomial times ⌊ ( s − 1) / 2 ⌋ \lfloor(s-1)/2\rfloor; splitting by the parity of s s evaluates it in O ⁡ ( 1) O(1) time.

###### Lemma 16 (one layer cost).

For fixed d d, the layer S d ​ ( n) S_{d}(n) can be evaluated in O ⁡ ( N d ​ log ⁡ N d) O(N_{d}\log N_{d}) arithmetic operations and O ⁡ ( N d) O(N_{d}) working memory.

###### Proof.

There are O ⁡ ( B 2) = O ⁡ ( N d) O(B^{2})=O(N_{d}) pairs 1 ⩽ q < p ⩽ B 1\leqslant q<p\leqslant B. For each pair, the uncapped and capped moment reductions above use only a constant number of six-state kernel calls, and each such call costs O ⁡ ( log ⁡ N d) O(\log N_{d}) by \cref cor:floor-kernel,app:six-moments. The diagonal-side terms contribute O ⁡ ( B) O(B) closed-form evaluations. Therefore the layer cost is O ⁡ ( N d ​ log ⁡ N d) O(N_{d}\log N_{d}). ∎

###### Theorem 17 (one value).

A single value F ⁡ ( n) F(n) can be computed exactly in O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) arithmetic operations and O ⁡ ( n) O(n) memory.

###### Proof.

By ( 10), it is enough to compute S d ​ ( n) S_{d}(n) for d ⩽ n d\leqslant n and combine the results with the weights μ ⁡ ( d) \mu(d). Using \cref lem:one-layer-cost, the total time is

 | ∑ d ⩽ n O ⁡ ( n d ​ log ⁡ n d) = O ⁡ ( n ​ log 2 ​ n). \sum_{d\leqslant n}O\!\left(\frac{n}{d}\log\frac{n}{d}\right)=O(n\log^{2}n). |  |

The values of μ ⁡ ( d) \mu(d) are obtained by a linear or Eratosthenes-type sieve. At any moment we store only this array and the temporary data for one layer, so the memory consumption is O ⁡ ( n) O(n). The closed form for F 0 ​ ( n) F_{0}(n) is then added in constant time. ∎

###### Remark 18 (quotient grouping).

The implementation may group all divisors with the same quotient N d = ⌊ n / d ⌋ N_{d}=\lfloor n/d\rfloor. For fixed N d N_{d}, the layer formula is a quadratic polynomial in d d, so prefix sums of μ ⁡ ( d) \mu(d), d ​ μ ​ ( d) d\mu(d), and d 2 ​ μ ​ ( d) d^{2}\mu(d) combine such blocks at once. This is only a constant-factor improvement and is not used in the asymptotic bound.

## 8 All values in O ⁡ ( N 3 / 2) O(N^{3/2})

We now compute the whole table F ⁡ ( 1), F ⁡ ( 2), …, F ⁡ ( N) F(1),F(2),\ldots,F(N) in one run. This section follows the same divisor-expanded viewpoint as \cref sec:one-value, but replaces repeated one-value summation by event arrays. A primitive-free quadruple is stored at the exact threshold where it first becomes active; after all thresholds have been filled, prefix sums recover every value of the sequence. As before, only the non-axis-parallel part F 1 F_{1} is generated explicitly, and the closed form for F 0 ​ ( n) F_{0}(n) is added at the end.

### 8.1 Event arrays and recovery

For a primitive-free quadruple a > b ⩾ 1 a>b\geqslant 1, x ⩾ y ⩾ 1 x\geqslant y\geqslant 1, put

 | L = a ​ x + b ​ y, K = b ​ x + a ​ y. L=ax+by,\qquad K=bx+ay. |  |

After applying the Möbius divisor d d, this quadruple contributes exactly for those n n with n ⩾ d ​ L n\geqslant dL, and its contribution at such an n n is

 | μ ⁡ ( d) ​ 𝒲 ⁡ ( x, y) ​ ( n − dL) ​ ( n − dK). \mu(d)\mult(x,y)(n-dL)(n-dK). |  |

Thus the activation threshold is d ​ L dL; the value of K K only enters the polynomial coefficient. For every event with threshold at most N N, add

 | E 0 ​ [d ​ L] \displaystyle E_{0}[dL] | + = μ ( d) 𝒲 ( x, y), \displaystyle\mathrel{+}=\mu(d)\mult(x,y), |  |

 | E 1 ​ [d ​ L] \displaystyle E_{1}[dL] | + = μ ( d) d 𝒲 ( x, y) ( L + K), \displaystyle\mathrel{+}=\mu(d)d\mult(x,y)(L+K), |  |

 | E 2 ​ [d ​ L] \displaystyle E_{2}[dL] | + = μ ( d) d 2 𝒲 ( x, y) LK. \displaystyle\mathrel{+}=\mu(d)d^{2}\mult(x,y)LK. |  |

Let

 | P i ​ ( n) = ∑ t ⩽ n E i ​ [t]. P_{i}(n)=\sum_{t\leqslant n}E_{i}[t]. |  |

Then

 | F 1 ​ ( n) = n 2 ​ P 0 ​ ( n) − n ​ P 1 ​ ( n) + P 2 ​ ( n), F_{1}(n)=n^{2}P_{0}(n)-nP_{1}(n)+P_{2}(n), |  | (21) |

and F ⁡ ( n) = F 0 ​ ( n) + F 1 ​ ( n) F(n)=F_{0}(n)+F_{1}(n).

###### Lemma 19 (event recovery).

If the arrays E 0, E 1, E 2 E_{0},E_{1},E_{2} contain exactly the event contributions above for all thresholds at most N N, then ( 21) gives the correct value of F 1 ​ ( n) F_{1}(n) for every 1 ⩽ n ⩽ N 1\leqslant n\leqslant N.

###### Proof.

For a fixed quadruple and divisor, the term contributes to F 1 ​ ( n) F_{1}(n) if and only if d ​ L ⩽ n dL\leqslant n. Summing all events with threshold at most n n gives

 | ∑ d ​ L ⩽ n μ ⁡ ( d) ​ 𝒲 ⁡ ( x, y) ​ ( n 2 − nd ⁡ ( L + K) + d 2 ​ LK), \sum_{dL\leqslant n}\mu(d)\mult(x,y)\left(n^{2}-nd(L+K)+d^{2}LK\right), |  |

which is exactly n 2 ​ P 0 ​ ( n) − n ​ P 1 ​ ( n) + P 2 ​ ( n) n^{2}P_{0}(n)-nP_{1}(n)+P_{2}(n) by the definitions of the three event arrays. ∎

### 8.2 Separating the Möbius convolution

First build divisor-free coefficient arrays G 0, G 1, G 2 G_{0},G_{1},G_{2} indexed by L L. This separates the geometric construction of the coefficients from the arithmetic Möbius convolution, which is applied only once:

 | G 0 ​ [L] \displaystyle G_{0}[L] | = ∑ a ​ x + b ​ y = L 𝒲 ⁡ ( x, y), \displaystyle=\sum_{ax+by=L}\mult(x,y), |  |

 | G 1 ​ [L] \displaystyle G_{1}[L] | = ∑ a ​ x + b ​ y = L 𝒲 ⁡ ( x, y) ​ ( L + K), \displaystyle=\sum_{ax+by=L}\mult(x,y)(L+K), |  |

 | G 2 ​ [L] \displaystyle G_{2}[L] | = ∑ a ​ x + b ​ y = L 𝒲 ⁡ ( x, y) ​ LK, \displaystyle=\sum_{ax+by=L}\mult(x,y)LK, |  |

where the sums are over a > b ⩾ 1 a>b\geqslant 1 and x ⩾ y ⩾ 1 x\geqslant y\geqslant 1. Then

 | E 0 ​ [t] \displaystyle E_{0}[t] | = ∑ d | t μ ⁡ ( d) ​ G 0 ​ ( t / d), \displaystyle=\sum_{d\mid t}\mu(d)G_{0}(t/d), |  | (22) |

 | E 1 ​ [t] \displaystyle E_{1}[t] | = ∑ d | t μ ⁡ ( d) ​ d ​ G 1 ​ ( t / d), \displaystyle=\sum_{d\mid t}\mu(d)d\,G_{1}(t/d), |  |

 | E 2 ​ [t] \displaystyle E_{2}[t] | = ∑ d | t μ ⁡ ( d) ​ d 2 ​ G 2 ​ ( t / d). \displaystyle=\sum_{d\mid t}\mu(d)d^{2}G_{2}(t/d). |  |

The convolution is evaluated by looping over d d and then over multiples t = d ​ L ⩽ N t=dL\leqslant N. Its cost is ∑ d ⩽ N O ⁡ ( N / d) = O ⁡ ( N ​ log ⁡ N) \sum_{d\leqslant N}O(N/d)=O(N\log N), so the main remaining task is the construction of the three arrays G i G_{i}.

### 8.3 Constructing the coefficient arrays

Let B = ⌊ N ⌋ B=\lfloor\sqrt{N}\rfloor. Since L = a ​ x + b ​ y ⩽ N L=ax+by\leqslant N implies a ​ x ⩽ N ax\leqslant N, every quadruple satisfies a ⩽ B a\leqslant B or x ⩽ B x\leqslant B. We use the disjoint cover

 | { x ⩽ B } ⊔ { a ⩽ B, x > B }. \{x\leqslant B\}\ \sqcup\ \{a\leqslant B,\ x>B\}. |  | (23) |

In the part a ⩽ B a\leqslant B, fix a > b a>b and write x = y + s x=y+s with s ⩾ 0 s\geqslant 0. Then

 | L = ( a + b) ​ y + a ​ s, K = ( a + b) ​ y + b ​ s. L=(a+b)y+as,\qquad K=(a+b)y+bs. |  |

The disjoint condition is x = y + s > B x=y+s>B. Hence for fixed a, b, y a,b,y the parameter s s runs over the interval

 | max ⁡ ( 0, B + 1 − y) ⩽ s ⩽ ⌊ N − ( a + b) ​ y a ⌋, \max(0,B+1-y)\leqslant s\leqslant\left\lfloor\frac{N-(a+b)y}{a}\right\rfloor, |  |

with the interval omitted if the upper bound is smaller than the lower bound. Along this interval L L is an arithmetic progression with step a a, and the updates to G 0, G 1, G 2 G_{0},G_{1},G_{2} are polynomials of degree at most two in s s. The possible singleton s = 0 s=0 has multiplier 2 2, while the range s ⩾ 1 s\geqslant 1 has multiplier 4 4.

In the part x ⩽ B x\leqslant B, fix x > y x>y and write a = b + r a=b+r with r ⩾ 1 r\geqslant 1. Then

 | L = ( x + y) ​ b + x ​ r, K = ( x + y) ​ b + y ​ r. L=(x+y)b+xr,\qquad K=(x+y)b+yr. |  |

For fixed x, y, r x,y,r, the parameter b b runs over

 | 1 ⩽ b ⩽ ⌊ N − x ​ r x + y ⌋, 1\leqslant b\leqslant\left\lfloor\frac{N-xr}{x+y}\right\rfloor, |  |

again with empty intervals ignored. Along this interval L L is an arithmetic progression with step x + y x+y, and the three coefficient updates are polynomials of degree at most two in b b. Finally, for diagonal sides x = y = t x=y=t, write s = a + b s=a+b. Since L = K = t ​ s L=K=ts and the number of pairs a > b ⩾ 1 a>b\geqslant 1 with a + b = s a+b=s is ⌊ ( s − 1) / 2 ⌋ \lfloor(s-1)/2\rfloor, we add, for t ​ s ⩽ N ts\leqslant N,

 | G 0 ​ [t ​ s] \displaystyle G_{0}[ts] | + = 2 ⌊ s − 1 2 ⌋, \displaystyle\mathrel{+}=2\left\lfloor\frac{s-1}{2}\right\rfloor, |  | (24) |

 | G 1 ​ [t ​ s] \displaystyle G_{1}[ts] | + = 4 t s ⌊ s − 1 2 ⌋, \displaystyle\mathrel{+}=4ts\left\lfloor\frac{s-1}{2}\right\rfloor, |  |

 | G 2 ​ [t ​ s] \displaystyle G_{2}[ts] | + = 2 ( t s) 2 ⌊ s − 1 2 ⌋. \displaystyle\mathrel{+}=2(ts)^{2}\left\lfloor\frac{s-1}{2}\right\rfloor. |  |

All non-diagonal updates have the generic form

 | G ⁡ [L 0 + m ​ ℓ] + = c 0 + c 1 ​ ℓ + c 2 ​ ℓ 2, ℓ 0 ⩽ ℓ ⩽ ℓ 1. G[L_{0}+m\ell]\mathrel{+}=c_{0}+c_{1}\ell+c_{2}\ell^{2},\qquad\ell_{0}\leqslant\ell\leqslant\ell_{1}. |  | (25) |

For a fixed step m ⩽ 2 ​ B m\leqslant 2B and residue class modulo m m, rewrite the right-hand side as a quadratic polynomial in the quotient index of the progression. Three ordinary difference arrays add such a polynomial on an interval in O ⁡ ( 1) O(1) time. The construction processes the steps one at a time: while step m m is active, the buffers store only the quotient-index difference arrays for the residue classes modulo m m. Their combined length is O ⁡ ( N) O(N), because every integer L ⩽ N L\leqslant N belongs to exactly one residue class for this fixed step. After all updates with step m m have been inserted, a single flush over the residue classes materializes their contribution to the global arrays G 0, G 1, G 2 G_{0},G_{1},G_{2}; the buffers are then cleared and reused for the next step. Thus the O ⁡ ( N) O(N) flush cost is paid separately for each m m, but the buffer memory is not multiplied by the number of steps.

###### Lemma 20 (coefficient-array construction).

The arrays G 0, G 1, G 2 G_{0},G_{1},G_{2} for all L ⩽ N L\leqslant N can be constructed in O ⁡ ( N 3 / 2) O(N^{3/2}) arithmetic operations and O ⁡ ( N) O(N) memory.

###### Proof.

The cover ( 23) is disjoint and exhaustive, so no tuple is missed or counted twice. In the part a ⩽ B a\leqslant B, for fixed a, b a,b the number of possible y y is O ⁡ ( N / ( a + b)) O(N/(a+b)), so the number of arithmetic-progression updates is

 | ∑ a ⩽ B ∑ b < a O ⁡ ( N a + b) = O ⁡ ( N ​ B), \sum_{a\leqslant B}\sum_{b<a}O\!\left(\frac{N}{a+b}\right)=O(NB), |  |

because ∑ b < a ( a + b) − 1 = O ⁡ ( 1) \sum_{b<a}(a+b)^{-1}=O(1) for each a a. In the non-diagonal part x ⩽ B x\leqslant B, for fixed x, y x,y the number of possible r r is O ⁡ ( N / x) O(N/x), so the number of updates is

 | ∑ x ⩽ B ∑ y < x O ⁡ ( N x) = O ⁡ ( N ​ B). \sum_{x\leqslant B}\sum_{y<x}O\!\left(\frac{N}{x}\right)=O(NB). |  |

The diagonal-side updates contribute ∑ t ⩽ B O ⁡ ( N / t) = O ⁡ ( N ​ log ⁡ N) \sum_{t\leqslant B}O(N/t)=O(N\log N) more. For each step m ⩽ 2 ​ B m\leqslant 2B, the total length of all residue-class buffers is O ⁡ ( N) O(N) and flushing them once costs O ⁡ ( N) O(N); over all O ⁡ ( B) O(B) possible steps this gives O ⁡ ( N ​ B) O(NB) flush time. Since the steps are processed sequentially, the same buffers are reused after each flush. Therefore the working memory consists of the global arrays G i G_{i} plus the buffers for a single step, all of total size O ⁡ ( N) O(N), rather than O ⁡ ( N ​ B) O(NB). With B = ⌊ N ⌋ B=\lfloor\sqrt{N}\rfloor, the total time is O ⁡ ( N 3 / 2) O(N^{3/2}). ∎

###### Theorem 21 (all values).

The whole table F ⁡ ( 1), F ⁡ ( 2), …, F ⁡ ( N) F(1),F(2),\ldots,F(N) can be computed exactly in O ⁡ ( N 3 / 2) O(N^{3/2}) arithmetic operations and O ⁡ ( N) O(N) memory.

###### Proof.

By \cref lem:coefficient-array-construction, the divisor-free coefficient arrays are built in O ⁡ ( N 3 / 2) O(N^{3/2}) time. The Möbius convolution ( 22) costs O ⁡ ( N ​ log ⁡ N) O(N\log N), which is absorbed by O ⁡ ( N 3 / 2) O(N^{3/2}) for N ⩾ 2 N\geqslant 2. Prefixing the three event arrays and applying ( 21) for all n ⩽ N n\leqslant N is linear. Adding the closed form for F 0 ​ ( n) F_{0}(n) for every n n is also linear. ∎

## 9 Asymptotics

In this section we state the final two-term asymptotic expansion and explain the structure of its proof. This part of the paper is somewhat more independent than the algorithmic sections, but we include it here because it gives a stringent large- n n consistency check for the exact values computed by the algorithms. The full derivation is deferred to \cref app:second-term.

The directions collected in F 0 ​ ( n) F_{0}(n) contribute only at order n 4 n^{4}, so the logarithmic term comes entirely from the primitive directions with u > v ⩾ 1 u>v\geqslant 1. The key observation is that the remaining part admits an inclusion–exclusion decomposition associated with the covering

 | { admissible quadruples } = { u, v ⩽ n } ∪ { a, b ⩽ n }, \{\text{admissible quadruples}\}=\{u,v\leqslant\sqrt{n}\}\cup\{a,b\leqslant\sqrt{n}\}, |  |

whose precise form is proved later as the covering identity in \cref lem:asym-cover. Writing S 1 ​ ( n) S_{1}(n) for the contribution of the region u, v ⩽ n u,v\leqslant\sqrt{n}, S 2 ​ ( n) S_{2}(n) for the contribution of the region a, b ⩽ n a,b\leqslant\sqrt{n}, and S 12 ​ ( n) S_{12}(n) for their overlap, one therefore has F ⁡ ( n) − F 0 ​ ( n) = S 1 ​ ( n) + S 2 ​ ( n) − S 12 ​ ( n). F(n)-F_{0}(n)=S_{1}(n)+S_{2}(n)-S_{12}(n).

The terms S 1 ​ ( n) S_{1}(n) and S 2 ​ ( n) S_{2}(n) are symmetric: after rescaling, each is governed by the same integral kernel and therefore contributes the same coefficient to the n 4 ​ log ⁡ n n^{4}\log n term. The overlap term S 12 ​ ( n) S_{12}(n) is counted in both pieces and must be subtracted once by inclusion–exclusion; it contributes only at order n 4 n^{4}. Thus the logarithmic main term is obtained by computing one of the two symmetric pieces and doubling its contribution, while the constant-order term comes from keeping track of all three pieces together with F 0 ​ ( n) F_{0}(n).

###### Theorem 22 (two-term asymptotic expansion).

Let F ⁡ ( n) F(n) be the total number of lattice rectangles contained in [0, n) × [0, n) [0,n)\times[0,n). Then F ⁡ ( n) = A ​ n 4 ​ log ⁡ n + B ​ n 4 + o ⁡ ( n 4), F(n)=A\,n^{4}\log n+B\,n^{4}+o(n^{4}), where

 | A = 4 ​ log ⁡ 2 − 1 π 2, B = − 4 ​ log ⁡ 2 − 1 6 ​ ζ ′ ​ ( 2) ζ ​ ( 2) 2 + 24 ​ ( 4 ​ log ⁡ 2 − 1) ​ γ + 72 ​ log 2 ​ 2 − 76 ​ log ⁡ 2 + 1 12 ​ π 2 − 1 4. A=\frac{4\log 2-1}{\pi^{2}},\ \ B=-\frac{4\log 2-1}{6}\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}+\frac{24(4\log 2-1)\gamma+72\log^{2}2-76\log 2+1}{12\pi^{2}}-\frac{1}{4}. |  |

The proof, including the decomposition into S 1 S_{1}, S 2 S_{2}, and S 12 S_{12} and the evaluation of the corresponding constants to order o ⁡ ( n 4) o(n^{4}), is given in \cref app:second-term. A numerical validation of the constants using exact values at powers of two is reported in \cref sec:large-values.

## 10 Experiments

All benchmark implementations, reference Python versions, the CUDA code used for the largest one-value computations, and the compressed all-values data are available at [https://github.com/flykiller/lattice-rectangles][3]. The one-value algorithms were benchmarked in single-threaded C++ on one core of an Intel i7-13700 at 5.2 GHz, compiled with clang++ 20.1.8 and -O3 -march=native, using std::int128_t throughout the tested range. The plots in \cref fig:timings report wall-clock seconds for n = 2 13, …, 2 30 n=2^{13},\dots,2^{30}; each point is the median of repeated runs, with relative variation below 0.5 % 0.5\%.

### 10.1 Comparison of one-value algorithms

\Cref

fig:timings compares all five implemented one-value algorithms: the quadratic primitive-direction sweep, the square-root decomposition, the cubic-root moment reduction, the ten-moment weighted floor-sum reduction, and the divisor-layer algorithm of \cref sec:one-value. The log–log plots are nearly linear with the expected slopes. The right panel normalizes each curve by its proved complexity, namely by n 2 n^{2}, n 3 / 2 ​ log ⁡ n n^{3/2}\log n, n 4 / 3 ​ log ⁡ n n^{4/3}\log n, n ​ log 3 ​ n n\log^{3}n, and n ​ log 2 ​ n n\log^{2}n, respectively.

The comparison shows the practical effect of the successive reductions. The square-root and cubic-root reorganizations already reduce the growth rate substantially; the weighted floor-sum kernel improves the one-value computation further; and the divisor-layer method gives the best asymptotic bound among the tested one-value algorithms. Its curve is included in the same plot because it is computing the same quantity F ⁡ ( n) F(n), with the Möbius divisor layers replacing the older outer organization.

Figure 1: Wall-clock running times of the five tested one-value algorithms on inputs n = 2 13, …, 2 30 n=2^{13},\dots,2^{30} (left) and after normalization by their respective theoretical complexities (right).

### 10.2 All-values experiment

We also benchmarked the all-values algorithm of \cref sec:all-values, which computes the whole table F ⁡ ( 1), …, F ⁡ ( N) F(1),\ldots,F(N) in one run. The implementation was tested for N = 2 5, 2 6, …, 2 24 N=2^{5},2^{6},\ldots,2^{24}. In addition, we used the same O ⁡ ( N 3 / 2) O(N^{3/2}) implementation to compute all exact values up to N = 10 8 N=10^{8}. The full table is too large to include here, but the results are available in compressed form in the GitHub repository mentioned above. In \cref fig:all-values-timings, the left panel gives the total wall-clock time, while the right panel plots the normalized quantity 10 6 ​ T ​ ( N) / N 3 / 2 10^{6}T(N)/N^{3/2}.

The normalized curve is not perfectly flat: after the smallest inputs, it gradually increases in the larger range of the experiment. This does not contradict the O ⁡ ( N 3 / 2) O(N^{3/2}) operation count. The all-values implementation maintains several arrays of length N N and performs repeated strided updates and flushes through these arrays. For small N N, most of this working set stays in cache; as N N grows, the coefficient arrays, event arrays, and temporary buffers exceed the faster cache levels, and the computation becomes increasingly limited by cache misses, TLB pressure, and memory bandwidth. Thus the observed growth of T ⁡ ( N) / N 3 / 2 T(N)/N^{3/2} is best understood as a memory-hierarchy effect rather than as a change in the arithmetic complexity.

This algorithm is also much less convenient to parallelize than the one-value divisor-layer computation. Its updates are not independent outputs: many iterations write into the same coefficient arrays, event arrays, or residue-class buffers. A parallel implementation must therefore either keep large private copies of these arrays for different workers and merge them afterwards, which greatly increases memory consumption, or let workers share the arrays and pay for synchronization or atomic writes, which creates many write conflicts. For this reason the experiment above is intended as a single-threaded baseline for the O ⁡ ( N 3 / 2) O(N^{3/2}) all-values method.

Figure 2: All-values experiment for N = 2 5, …, 2 24 N=2^{5},\dots,2^{24}: total running time (left) and normalized running time 10 6 ​ T ​ ( N) / N 3 / 2 10^{6}T(N)/N^{3/2} (right).

### 10.3 Large exact values and asymptotic check

For convenience we record exact values of F ⁡ ( 2 k) F(2^{k}) for 1 ⩽ k ⩽ 40 1\leqslant k\leqslant 40. Smaller entries were cross-checked against slower exact methods whenever feasible. The largest entries, up to 2 40 2^{40}, were obtained with a separate CUDA implementation of the divisor-layer one-value formula of \cref sec:one-value. At a high level, the CUDA code uses a segmented GPU sieve to build Möbius-summed divisor layers, splits each layer into independent arithmetic-progression work items, processes these work items with persistent CUDA blocks, accumulates exact partial sums in a fixed-width 192-bit representation, and performs a final reduction. These values also serve as input for the asymptotic comparison below.

k k | F ⁡ ( 2 k) F(2^{k}) | k k | F ⁡ ( 2 k) F(2^{k}) |

1 1 | 1 1 | 21 21 | 48931868439876126051425552 48931868439876126051425552 |

2 2 | 44 44 | 22 22 | 821437615651793675198669752 821437615651793675198669752 |

3 3 | 1192 1192 | 23 23 | 13759445380252558103053449112 13759445380252558103053449112 |

4 4 | 27128 27128 | 24 24 | 230014222561387209679445816240 230014222561387209679445816240 |

5 5 | 564120 564120 | 25 25 | 3838037104619867210112196814232 3838037104619867210112196814232 |

6 6 | 11114080 11114080 | 26 26 | 63933546372113490066412405897360 63933546372113490066412405897360 |

7 7 | 211224480 211224480 | 27 27 | 1063335985124949941305863686097296 1063335985124949941305863686097296 |

8 8 | 3914221216 3914221216 | 28 28 | 17659763652737469299382592232330696 17659763652737469299382592232330696 |

9 9 | 71182606216 71182606216 | 29 29 | 292898424695610564494215857912343064 292898424695610564494215857912343064 |

10 10 | 1275797150128 1275797150128 | 30 30 | 4851850095158746095561485451592336296 4851850095158746095561485451592336296 |

11 11 | 22602804487208 22602804487208 | 31 31 | 80277206323003614389748671287223855080 80277206323003614389748671287223855080 |

12 12 | 396685572297544 396685572297544 | 32 32 | 1326796977975476403092689286862986516504 1326796977975476403092689286862986516504 |

13 13 | 6907621416632376 6907621416632376 | 33 33 | 21906538476526319541299023010218991588136 21906538476526319541299023010218991588136 |

14 14 | 119492377263166968 119492377263166968 | 34 34 | 361349204887120272089523042249821840571528 361349204887120272089523042249821840571528 |

15 15 | 2055404973525169560 2055404973525169560 | 35 35 | 5955100706397110811260922659812491131662432 5955100706397110811260922659812491131662432 |

16 16 | 35182910663019639384 35182910663019639384 | 36 36 | 98057826153604756744005601368029402514221504 98057826153604756744005601368029402514221504 |

17 17 | 599669468453524178752 599669468453524178752 | 37 37 | 1613344656077691850026984888873116366804460232 1613344656077691850026984888873116366804460232 |

18 18 | 10182597857710132553464 10182597857710132553464 | 38 38 | 26524225499163321460061315970545176007812869616 26524225499163321460061315970545176007812869616 |

19 19 | 172327747508964813792096 172327747508964813792096 | 39 39 | 435758984017337173124103405065600778830350047408 435758984017337173124103405065600778830350047408 |

20 20 | 2907742868855598433202344 2907742868855598433202344 | 40 40 | 7154085760768979246024995359851578213153827420872 7154085760768979246024995359851578213153827420872 |

Table 2: Exact values of F ⁡ ( 2 k) F(2^{k}) for 1 ⩽ k ⩽ 40 1\leqslant k\leqslant 40.

Two-term fit. With the numerical constants A = ( 4 ​ log ⁡ 2 − 1) / π 2 A=(4\log 2-1)/\pi^{2} and B ≈ − 0.084567061533 B\approx-0.084567061533, evaluated in the appendix, it is natural to inspect F ⁡ ( n) − A ​ n 4 ​ log ⁡ n n 4. \frac{F(n)-An^{4}\log n}{n^{4}}. For the computed values n = 2 k n=2^{k}, this quantity appears to stabilize rapidly near the predicted constant B B. Thus the data are fully consistent with the two-term asymptotic F ⁡ ( n) = A ​ n 4 ​ log ⁡ n + B ​ n 4 + o ⁡ ( n 4) F(n)=An^{4}\log n+Bn^{4}+o(n^{4}), and provide a simple numerical check.

## 11 Summary and future work

We obtained exact one-value algorithms of complexity O ⁡ ( n 2) O(n^{2}) for the classical primitive-direction sweep, O ⁡ ( n 3 / 2 ​ log ⁡ n) O(n^{3/2}\log n) for the square-root decomposition, O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n) for the cubic-root decomposition with floor moments, O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) for the ten-moment weighted floor-sum reduction, and O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) for the divisor-layer square-root-cover algorithm. We also obtained an all-values algorithm computing F ⁡ ( 1), …, F ⁡ ( N) F(1),\ldots,F(N) in O ⁡ ( N 3 / 2) O(N^{3/2}) time and O ⁡ ( N) O(N) memory. The key structural feature of the fastest stages is the collapse of the geometric summation to one-dimensional arithmetic kernels or exact-threshold coefficient arrays: a six-state floor-moment kernel in the O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n) and O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) algorithms, a ten-state Euclidean kernel in the O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) reduction, and arithmetic-progression event updates in the all-values algorithm. \Cref app:engineering records implementation-level simplifications that preserve the asymptotic complexity while improving the practical running time by more than a factor of three.

Natural directions include further reducing the one-value complexity below O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n), sharpening the remainder beyond o ⁡ ( n 4) o(n^{4}), extending the methods to other lattice objects and higher dimensions, and improving the all-values construction below the square-root barrier. A genuinely sublinear algorithm for a single value F ⁡ ( n) F(n) would likely require a different idea: even in the divisor-layer formulation there are Θ ⁡ ( n) \Theta(n) natural outer scales to account for, so an Ω ⁡ ( n) \Omega(n) -type barrier appears heuristically unavoidable unless one finds additional global cancellations or a new transform-level description of the count.

## Appendix A Algorithmic appendix: expanded pseudocode

This appendix records more explicit procedural versions of the algorithmic stages. The aim is not to specify low-level implementation details, but to make the control flow of each algorithm and the interfaces between the geometric summation and the one-dimensional kernels transparent. Throughout this appendix, the three directions ( 0, 1) (0,1), ( 1, 0) (1,0), and ( 1, 1) (1,1) are excluded from the loops and are handled separately through the closed-form term F 0 ​ ( n) F_{0}(n).

\captionsetup

[algorithm]font=small,skip=4pt

Algorithm 1 Classical quadratic baseline.

1: Initialize a ​ n ​ s ← 0 ans\leftarrow 0.

2: for each primitive ( u, v) (u,v) with u > v > 0 u>v>0 do

3: determine y min ⩽ y ⩽ y max y_{\min}\leqslant y\leqslant y_{\max} from \cref eq:basic-constraints

4: for y = y min, …, y max y=y_{\min},\dots,y_{\max} do

5: determine the induced interval x min ​ ( y) ⩽ x ⩽ x max ​ ( y) x_{\min}(y)\leqslant x\leqslant x_{\max}(y)

6: if nonempty, add the closed polynomial sum of 𝒲 ⁡ ( x, y) \mult(x,y) times ( 2) over x x

7: end for

8: end for

9: return F 0 ​ ( n) + a ​ n ​ s F_{0}(n)+ans.

Algorithm 2 Square-root decomposition.

1: Set B ← ⌊ n ⌋ B\leftarrow\left\lfloor\sqrt{n}\right\rfloor and a ​ n ​ s ← 0 ans\leftarrow 0.

2: for each primitive ( u, v) (u,v) with u ⩽ B u\leqslant B and u > v > 0 u>v>0 do

3: evaluate c u, v ​ ( n) c_{u,v}(n) by the baseline routine and add c u, v ​ ( n) c_{u,v}(n)

4: end for

5: for each ( x, y) (x,y) with x ⩾ y ⩾ 1 x\geqslant y\geqslant 1 and x ⩽ ⌊ n / B ⌋ x\leqslant\left\lfloor n/B\right\rfloor do

6: pass to the dual ( x, y) (x,y) -parametrization and determine L ⩽ v ⩽ U L\leqslant v\leqslant U

7: accumulate the primitive contribution on [L, U] [L,U] by coprime prefix sums, including the multiplier 𝒲 ⁡ ( x, y) \mult(x,y)

8: end for

9: return F 0 ​ ( n) + a ​ n ​ s F_{0}(n)+ans.

Algorithm 3 Cubic-root decomposition.

1: Set B ← ⌊ n 2 / 3 ⌋ B\leftarrow\left\lfloor n^{2/3}\right\rfloor and a ​ n ​ s ← 0 ans\leftarrow 0.

2: for each primitive ( u, v) (u,v) with u ⩽ B u\leqslant B and u > v > 0 u>v>0 do

3: rewrite c u, v ​ ( n) c_{u,v}(n) as a fixed linear combination of six moments

4: evaluate the required values 𝐇 ⁡ ( ⋅, ⋅, ⋅, ⋅) \mathbf{H}(\cdot;\cdot,\cdot,\cdot) by \cref app:six-moments and add c u, v ​ ( n) c_{u,v}(n)

5: end for

6: for u = B + 1, …, n u=B+1,\dots,n do

7: set x max ← ⌊ n / u ⌋ x_{\max}\leftarrow\left\lfloor n/u\right\rfloor

8: for each ( x, y) (x,y) with 1 ⩽ y ⩽ x ⩽ x max 1\leqslant y\leqslant x\leqslant x_{\max} do

9: set m ← 2 m\leftarrow 2 if x = y x=y, and m ← 4 m\leftarrow 4 otherwise

10: set v max ← min ⁡ ( u − 1, ⌊ n − x ​ u y ⌋) v_{\max}\leftarrow\min\!\left(u-1,\left\lfloor\frac{n-xu}{y}\right\rfloor\right)

11: if v max < 1 v_{\max}<1, continue to the next pair ( x, y) (x,y)

12: evaluate ( C 0, C 1, C 2) (C_{0},C_{1},C_{2}) on 1 ⩽ v ⩽ v max 1\leqslant v\leqslant v_{\max} by coprime prefix sums

13: add m ⁡ ( ( n − x ​ u) ​ ( n − y ​ u) ​ C 0 − ( x ⁡ ( n − x ​ u) + y ⁡ ( n − y ​ u)) ​ C 1 + x ​ y ​ C 2) m\bigl((n-xu)(n-yu)C_{0}-(x(n-xu)+y(n-yu))C_{1}+xyC_{2}\bigr)

14: end for

15: end for

16: return F 0 ​ ( n) + a ​ n ​ s F_{0}(n)+ans.

Algorithm 4 Ten-moment weighted-floor-sum algorithm.

1: Precompute the squarefree divisor lists D ( u) = { ( d, μ ( d)): d ∣ u, d squarefree } D(u)=\{(d,\mu(d)):d\mid u,\ d\text{ squarefree}\} for all u ⩽ n u\leqslant n.

2: Initialize a ​ n ​ s ← 0 ans\leftarrow 0.

3: for u = 2, …, n u=2,\dots,n and each y y with 1 ⩽ y ⩽ ⌊ n / u ⌋ 1\leqslant y\leqslant\lfloor n/u\rfloor do

4: for each ( d, μ ⁡ ( d)) ∈ D ⁡ ( u) (d,\mu(d))\in D(u) with d < u d<u and y ⁡ ( u + d) ⩽ n y(u+d)\leqslant n do

5: form the Möbius-expanded quantity R u, y, d R_{u,y,d}

6: split R u, y, d R_{u,y,d} into its polynomial and weighted floor-sum parts

7: evaluate the weighted queries by \cref app:ten-moments

8: add μ ⁡ ( d) ​ R u, y, d \mu(d)R_{u,y,d} to a ​ n ​ s ans

9: end for

10: end for

11: return F 0 ​ ( n) + a ​ n ​ s F_{0}(n)+ans.

Algorithm 5 Divisor-layer one-value algorithm.

1: Precompute μ ⁡ ( d) \mu(d) for d ⩽ n d\leqslant n.

2: Initialize a ​ n ​ s ← 0 ans\leftarrow 0.

3: for d = 1, …, n d=1,\dots,n with μ ⁡ ( d) ≠ 0 \mu(d)\neq 0 do

4: set N d ← ⌊ n / d ⌋ N_{d}\leftarrow\lfloor n/d\rfloor, B ← ⌊ N d ⌋ B\leftarrow\lfloor\sqrt{N_{d}}\rfloor, and S ← 0 S\leftarrow 0 ⊳ \triangleright use { x ⩽ B } ⊔ { a ⩽ B, x > B } \{x\leqslant B\}\sqcup\{a\leqslant B,\ x>B\}

5: for 1 ⩽ q < p ⩽ B 1\leqslant q<p\leqslant B do

6: evaluate the moments M i ​ j ​ ( p, q, N d) M_{ij}(p,q;N_{d}) and M i ​ j ∩ ​ ( p, q, N d, B) M^{\cap}_{ij}(p,q;N_{d},B) for 0 ⩽ i + j ⩽ 2 0\leqslant i+j\leqslant 2 by \cref app:six-moments

7: form Φ p, q ( d) \Phi_{p,q}^{(d)}, Δ p, q ( d) \Delta_{p,q}^{(d)}, Φ p, q ( d), ∩ \Phi_{p,q}^{(d),\cap}, and Δ p, q ( d), ∩ \Delta_{p,q}^{(d),\cap}

8: add 8 ​ Φ p, q ( d) − 6 ​ Δ p, q ( d) − 4 ​ Φ p, q ( d), ∩ + 2 ​ Δ p, q ( d), ∩ 8\Phi_{p,q}^{(d)}-6\Delta_{p,q}^{(d)}-4\Phi_{p,q}^{(d),\cap}+2\Delta_{p,q}^{(d),\cap} to S S

9: end for

10: for t = 1, …, B t=1,\dots,B do

11: add the closed diagonal-side sum C t ( d) C_{t}^{(d)} to S S

12: end for

13: add μ ⁡ ( d) ​ S \mu(d)S to a ​ n ​ s ans

14: end for

15: return F 0 ​ ( n) + a ​ n ​ s F_{0}(n)+ans.

Algorithm 6 All-values event-array algorithm.

1: Set B ← ⌊ N ⌋ B\leftarrow\lfloor\sqrt{N}\rfloor and initialize G 0, G 1, G 2 G_{0},G_{1},G_{2} to zero.

2: Insert the arithmetic-progression updates from the disjoint cover { x ⩽ B } ⊔ { a ⩽ B, x > B } \{x\leqslant B\}\sqcup\{a\leqslant B,\ x>B\}.

3: Flush the step buffers to materialize all entries of G 0, G 1, G 2 G_{0},G_{1},G_{2}.

4: Precompute μ ⁡ ( d) \mu(d) for d ⩽ N d\leqslant N and initialize E 0, E 1, E 2 E_{0},E_{1},E_{2} to zero.

5: for d = 1, …, N d=1,\dots,N and all multiples t = d ​ L ⩽ N t=dL\leqslant N do

6: add μ ⁡ ( d) ​ G 0 ​ [L] \mu(d)G_{0}[L], μ ⁡ ( d) ​ d ​ G 1 ​ [L] \mu(d)dG_{1}[L], and μ ⁡ ( d) ​ d 2 ​ G 2 ​ [L] \mu(d)d^{2}G_{2}[L] to E 0 ​ [t] E_{0}[t], E 1 ​ [t] E_{1}[t], and E 2 ​ [t] E_{2}[t]

7: end for

8: Prefix the three event arrays to obtain P 0, P 1, P 2 P_{0},P_{1},P_{2}.

9: for n = 1, …, N n=1,\dots,N do

10: output F ⁡ ( n) = F 0 ​ ( n) + n 2 ​ P 0 ​ ( n) − n ​ P 1 ​ ( n) + P 2 ​ ( n) F(n)=F_{0}(n)+n^{2}P_{0}(n)-nP_{1}(n)+P_{2}(n).

11: end for

The squarefree divisor lists used in the ten-moment algorithm can be generated once by a sieve for the smallest prime factor together with the recursive construction of all squarefree divisors of each u u. Their total size up to n n is ∑ u ⩽ n 2 ω ⁡ ( u) = O ⁡ ( n ​ log ⁡ n) \sum_{u\leqslant n}2^{\omega(u)}=O(n\log n), so this preprocessing does not affect the O ⁡ ( n ​ log 3 ​ n) O(n\log^{3}n) complexity bound.

## Appendix B A six-moment weighted kernel

This appendix records the floor-moment kernel used in the small-direction part of the O ⁡ ( n 4 / 3 ​ log ⁡ n) O(n^{4/3}\log n) algorithm. In the main text, each contribution c u, v ​ ( n) c_{u,v}(n) with 2 ⩽ u ⩽ B 2\leqslant u\leqslant B and 1 ⩽ v < u 1\leqslant v<u is reduced to a fixed linear combination of floor sums of the form ∑ x p ​ ⌊ ( a ​ x + b) / m ⌋ q \sum x^{p}\lfloor(ax+b)/m\rfloor^{q} with p + q ⩽ 3 p+q\leqslant 3; the six-moment family below is exactly the closure of those sums under the Euclidean recursion.

### B.1 Definition of the family

For integers n ⩾ 0 n\geqslant 0, m ⩾ 1 m\geqslant 1, and a, b ⩾ 0 a,b\geqslant 0, define

 | ℋ p, q ​ ( n, m, a, b):= ∑ x = 0 n − 1 x p ​ ⌊ a ​ x + b m ⌋ q, q ⩾ 1, p + q ⩽ 3. \mathcal{H}_{p,q}(n;m,a,b):=\sum_{x=0}^{n-1}x^{p}\left\lfloor\frac{ax+b}{m}\right\rfloor^{q},\qquad q\geqslant 1,\quad p+q\leqslant 3. |  |

Equivalently, we work with the six quantities

 | 𝐇 ⁡ ( n, m, a, b):= ( ℋ 0, 1, ℋ 1, 1, ℋ 2, 1, ℋ 0, 2, ℋ 1, 2, ℋ 0, 3). \mathbf{H}(n;m,a,b):=(\mathcal{H}_{0,1},\ \mathcal{H}_{1,1},\ \mathcal{H}_{2,1},\ \mathcal{H}_{0,2},\ \mathcal{H}_{1,2},\ \mathcal{H}_{0,3}). |  |

We also use the power sums

 | P r ( n):= ∑ x = 0 n − 1 x r, r = 0, 1, 2, 3, P_{r}(n):=\sum_{x=0}^{n-1}x^{r},\qquad r=0,1,2,3, |  |

namely

 | P 0 ​ ( n) = n, P 1 ​ ( n) = n ⁡ ( n − 1) 2, P 2 ​ ( n) = n ​ ( n − 1) ​ ( 2 ​ n − 1) 6, P 3 ​ ( n) = P 1 ​ ( n) 2. P_{0}(n)=n,\qquad P_{1}(n)=\frac{n(n-1)}{2},\qquad P_{2}(n)=\frac{n(n-1)(2n-1)}{6},\qquad P_{3}(n)=P_{1}(n)^{2}. |  |

### B.2 Base case

If a = 0 a=0, then ⌊ ( a ​ x + b) / m ⌋ = c:= ⌊ b / m ⌋ \left\lfloor(ax+b)/m\right\rfloor=c:=\left\lfloor b/m\right\rfloor is constant, and therefore

 | 𝐇 ⁡ ( n, m, 0, b) = ( c ​ P 0, c ​ P 1, c ​ P 2, c 2 ​ P 0, c 2 ​ P 1, c 3 ​ P 0), \mathbf{H}(n;m,0,b)=\bigl(cP_{0},\ cP_{1},\ cP_{2},\ c^{2}P_{0},\ c^{2}P_{1},\ c^{3}P_{0}\bigr), |  |

where P r = P r ​ ( n) P_{r}=P_{r}(n).

### B.3 Affine step

Assume a ⩾ m a\geqslant m or b ⩾ m b\geqslant m. Write

 | a = A ​ m + a ′, b = B ​ m + b ′, 0 ⩽ a ′, b ′ < m. a=Am+a^{\prime},\qquad b=Bm+b^{\prime},\qquad 0\leqslant a^{\prime},b^{\prime}<m. |  |

Then

 | ⌊ a ​ x + b m ⌋ = A ​ x + B + ⌊ a ′ ​ x + b ′ m ⌋. \left\lfloor\frac{ax+b}{m}\right\rfloor=Ax+B+\left\lfloor\frac{a^{\prime}x+b^{\prime}}{m}\right\rfloor. |  |

Hence the six moments for ( m, a, b) (m,a,b) are explicit linear combinations of the six moments for ( m, a ′, b ′) (m,a^{\prime},b^{\prime}) and of the power sums.

Let

 | 𝐁:= 𝐇 ⁡ ( n, m, a ′, b ′) = ( b 01, b 11, b 21, b 02, b 12, b 03), \mathbf{B}:=\mathbf{H}(n;m,a^{\prime},b^{\prime})=(b_{01},b_{11},b_{21},b_{02},b_{12},b_{03}), |  |

and abbreviate

 | P r:= P r ​ ( n). P_{r}:=P_{r}(n). |  |

Then the affine reduction gives

 | ℋ 0, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,1}(n;m,a,b) | = b 01 + A ​ P 1 + B ​ P 0, \displaystyle=b_{01}+AP_{1}+BP_{0}, |  |

 | ℋ 1, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,1}(n;m,a,b) | = b 11 + A ​ P 2 + B ​ P 1, \displaystyle=b_{11}+AP_{2}+BP_{1}, |  |

 | ℋ 2, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{2,1}(n;m,a,b) | = b 21 + A ​ P 3 + B ​ P 2, \displaystyle=b_{21}+AP_{3}+BP_{2}, |  |

 | ℋ 0, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,2}(n;m,a,b) | = b 02 + 2 ​ A ​ b 11 + 2 ​ B ​ b 01 + A 2 ​ P 2 + 2 ​ A ​ B ​ P 1 + B 2 ​ P 0, \displaystyle=b_{02}+2Ab_{11}+2Bb_{01}+A^{2}P_{2}+2ABP_{1}+B^{2}P_{0}, |  |

 | ℋ 1, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,2}(n;m,a,b) | = b 12 + 2 ​ A ​ b 21 + 2 ​ B ​ b 11 + A 2 ​ P 3 + 2 ​ A ​ B ​ P 2 + B 2 ​ P 1, \displaystyle=b_{12}+2Ab_{21}+2Bb_{11}+A^{2}P_{3}+2ABP_{2}+B^{2}P_{1}, |  |

 | ℋ 0, 3 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,3}(n;m,a,b) | = b 03 + 3 ​ A ​ b 12 + 3 ​ B ​ b 02 + 3 ​ A 2 ​ b 21 + 6 ​ A ​ B ​ b 11 + 3 ​ B 2 ​ b 01 \displaystyle=b_{03}+3Ab_{12}+3Bb_{02}+3A^{2}b_{21}+6ABb_{11}+3B^{2}b_{01} |  |

 |  | + A 3 ​ P 3 + 3 ​ A 2 ​ B ​ P 2 + 3 ​ A ​ B 2 ​ P 1 + B 3 ​ P 0. \displaystyle\qquad+A^{3}P_{3}+3A^{2}BP_{2}+3AB^{2}P_{1}+B^{3}P_{0}. |  |

### B.4 Reciprocal step

Now assume

 | 0 ⩽ a, b < m. 0\leqslant a,b<m. |  |

Set

 | Y:= ⌊ a ⁡ ( n − 1) + b m ⌋. Y:=\left\lfloor\frac{a(n-1)+b}{m}\right\rfloor. |  |

If Y = 0 Y=0, then all six moments vanish.

Otherwise define

 | g ⁡ ( t):= ⌊ m ​ t + ( m − b − 1) a ⌋, 0 ⩽ t ⩽ Y − 1. g(t):=\left\lfloor\frac{mt+(m-b-1)}{a}\right\rfloor,\qquad 0\leqslant t\leqslant Y-1. |  |

As usual, the reciprocal transformation exchanges the graph of

 | f ⁡ ( x):= ⌊ a ​ x + b m ⌋ f(x):=\left\lfloor\frac{ax+b}{m}\right\rfloor |  |

with the complementary staircase determined by g g, and therefore expresses the moments for ( n, m, a, b) (n;m,a,b) through the moments for ( Y, a, m, m − b − 1) (Y;a,m,m-b-1).

Write

 | 𝐆 = 𝐇 ⁡ ( Y, a, m, m − b − 1) = ( g 01, g 11, g 21, g 02, g 12, g 03), \mathbf{G}=\mathbf{H}(Y;a,m,m-b-1)=(g_{01},g_{11},g_{21},g_{02},g_{12},g_{03}), |  |

and let

 | P r:= P r ​ ( n), Q r:= P r ​ ( Y). P_{r}:=P_{r}(n),\qquad Q_{r}:=P_{r}(Y). |  |

Then

 | ℋ 0, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,1}(n;m,a,b) | = P 0 ​ Y − Q 0 − g 01, \displaystyle=P_{0}Y-Q_{0}-g_{01}, |  |

 | ℋ 1, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,1}(n;m,a,b) | = 2 ​ P 1 ​ Y − g 01 − g 02 2, \displaystyle=\frac{2P_{1}Y-g_{01}-g_{02}}{2}, |  |

 | ℋ 2, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{2,1}(n;m,a,b) | = 6 ​ P 2 ​ Y − g 01 − 3 ​ g 02 − 2 ​ g 03 6, \displaystyle=\frac{6P_{2}Y-g_{01}-3g_{02}-2g_{03}}{6}, |  |

 | ℋ 0, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,2}(n;m,a,b) | = P 0 ​ Y 2 − Q 0 − g 01 − 2 ​ Q 1 − 2 ​ g 11, \displaystyle=P_{0}Y^{2}-Q_{0}-g_{01}-2Q_{1}-2g_{11}, |  |

 | ℋ 1, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,2}(n;m,a,b) | = 2 ​ P 1 ​ Y 2 − g 01 − g 02 − 2 ​ g 11 − 2 ​ g 12 2, \displaystyle=\frac{2P_{1}Y^{2}-g_{01}-g_{02}-2g_{11}-2g_{12}}{2}, |  |

 | ℋ 0, 3 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,3}(n;m,a,b) | = P 0 ​ Y 3 − Q 0 − g 01 − 3 ​ Q 1 − 3 ​ g 11 − 3 ​ Q 2 − 3 ​ g 21. \displaystyle=P_{0}Y^{3}-Q_{0}-g_{01}-3Q_{1}-3g_{11}-3Q_{2}-3g_{21}. |  |

###### Lemma 23.

The six moments

 | ℋ 0, 1, ℋ 1, 1, ℋ 2, 1, ℋ 0, 2, ℋ 1, 2, ℋ 0, 3 \mathcal{H}_{0,1},\ \mathcal{H}_{1,1},\ \mathcal{H}_{2,1},\ \mathcal{H}_{0,2},\ \mathcal{H}_{1,2},\ \mathcal{H}_{0,3} |  |

admit a recursive evaluation in O ⁡ ( log ⁡ m) O(\log m) arithmetic operations.

###### Proof.

The affine step reduces ( a, b) (a,b) modulo m m. The reciprocal step replaces ( n, m, a, b) (n;m,a,b) by

 | ( Y, a, m, m − b − 1), Y = ⌊ a ⁡ ( n − 1) + b m ⌋, (Y;a,m,m-b-1),\qquad Y=\left\lfloor\frac{a(n-1)+b}{m}\right\rfloor, |  |

so the first modulus strictly decreases from m m to a < m a<m. Hence the recursion has Euclidean depth O ⁡ ( log ⁡ m) O(\log m). Each step performs only O ⁡ ( 1) O(1) arithmetic operations on the six stored moments and the power sums. ∎

### B.5 Complexity bound

Each recursive call either reduces a a and b b modulo m m (the affine step) or swaps the roles of ( a, m) (a,m) with strictly smaller Euclidean parameters (the reciprocal step). Hence the recursion depth is O ⁡ ( log ⁡ m) = O ⁡ ( log ⁡ n) O(\log m)=O(\log n). Every step performs only O ⁡ ( 1) O(1) arithmetic operations on a constant-size family of moments.

## Appendix C A ten-moment weighted kernel

This appendix records a compact floor-moment kernel sufficient for the weighted reduction of \cref eq:main-floor-family. In the main text, each outer term R u, y, d R_{u,y,d} is reduced to a constant number of weighted floor sums whose polynomial weights have total degree at most 4 4; the ten moments below are the minimal closed family we use to evaluate those queries recursively.

### C.1 Definition of the family

For integers n ⩾ 0 n\geqslant 0, m ⩾ 1 m\geqslant 1, and a, b ⩾ 0 a,b\geqslant 0, define

 | ℋ p, q ​ ( n, m, a, b):= ∑ x = 0 n − 1 x p ​ ⌊ a ​ x + b m ⌋ q, q ⩾ 1, p + q ⩽ 4. \mathcal{H}_{p,q}(n;m,a,b):=\sum_{x=0}^{n-1}x^{p}\left\lfloor\frac{ax+b}{m}\right\rfloor^{q},\qquad q\geqslant 1,\quad p+q\leqslant 4. |  |

Equivalently, we work with the ten quantities

 | 𝐇 ⁡ ( n, m, a, b):= ( ℋ 0, 1, ℋ 1, 1, ℋ 2, 1, ℋ 3, 1, ℋ 0, 2, ℋ 1, 2, ℋ 2, 2, ℋ 0, 3, ℋ 1, 3, ℋ 0, 4). \mathbf{H}(n;m,a,b):=(\mathcal{H}_{0,1},\ \mathcal{H}_{1,1},\ \mathcal{H}_{2,1},\ \mathcal{H}_{3,1},\ \mathcal{H}_{0,2},\ \mathcal{H}_{1,2},\ \mathcal{H}_{2,2},\ \mathcal{H}_{0,3},\ \mathcal{H}_{1,3},\ \mathcal{H}_{0,4}). |  |

We also use the power sums

 | P r ( n):= ∑ x = 0 n − 1 x r, r = 0, 1, 2, 3, 4, P_{r}(n):=\sum_{x=0}^{n-1}x^{r},\qquad r=0,1,2,3,4, |  |

namely

 | P 0 ​ ( n) = n, P 1 ​ ( n) = n ⁡ ( n − 1) 2, P 2 ​ ( n) = n ​ ( n − 1) ​ ( 2 ​ n − 1) 6, P_{0}(n)=n,\qquad P_{1}(n)=\frac{n(n-1)}{2},\qquad P_{2}(n)=\frac{n(n-1)(2n-1)}{6}, |  |

 | P 3 ​ ( n) = ( n ⁡ ( n − 1) 2) 2, P 4 ​ ( n) = n ⁡ ( n − 1) ​ ( 2 ​ n − 1) ​ ( 3 ​ n 2 − 3 ​ n − 1) 30. P_{3}(n)=\left(\frac{n(n-1)}{2}\right)^{2},\qquad P_{4}(n)=\frac{n(n-1)(2n-1)(3n^{2}-3n-1)}{30}. |  |

### C.2 Base case

If a = 0 a=0, then ⌊ ( a ​ x + b) / m ⌋ = c:= ⌊ b / m ⌋ \left\lfloor(ax+b)/m\right\rfloor=c:=\left\lfloor b/m\right\rfloor is constant, and therefore

 | 𝐇 ⁡ ( n, m, 0, b) = ( c ​ P 0, c ​ P 1, c ​ P 2, c ​ P 3, c 2 ​ P 0, c 2 ​ P 1, c 2 ​ P 2, c 3 ​ P 0, c 3 ​ P 1, c 4 ​ P 0), \mathbf{H}(n;m,0,b)=\bigl(cP_{0},\ cP_{1},\ cP_{2},\ cP_{3},\ c^{2}P_{0},\ c^{2}P_{1},\ c^{2}P_{2},\ c^{3}P_{0},\ c^{3}P_{1},\ c^{4}P_{0}\bigr), |  |

where P r = P r ​ ( n) P_{r}=P_{r}(n).

### C.3 Affine step

Assume a ⩾ m a\geqslant m or b ⩾ m b\geqslant m. Write

 | a = A ​ m + a ′, b = B ​ m + b ′, 0 ⩽ a ′, b ′ < m. a=Am+a^{\prime},\qquad b=Bm+b^{\prime},\qquad 0\leqslant a^{\prime},b^{\prime}<m. |  |

Then

 | ⌊ a ​ x + b m ⌋ = A ​ x + B + ⌊ a ′ ​ x + b ′ m ⌋. \left\lfloor\frac{ax+b}{m}\right\rfloor=Ax+B+\left\lfloor\frac{a^{\prime}x+b^{\prime}}{m}\right\rfloor. |  |

Hence the ten moments for ( m, a, b) (m,a,b) are explicit linear combinations of the ten moments for ( m, a ′, b ′) (m,a^{\prime},b^{\prime}) and of the power sums.

Let

 | 𝐁:= 𝐇 ⁡ ( n, m, a ′, b ′) = ( b 01, b 11, b 21, b 31, b 02, b 12, b 22, b 03, b 13, b 04), \mathbf{B}:=\mathbf{H}(n;m,a^{\prime},b^{\prime})=(b_{01},b_{11},b_{21},b_{31},b_{02},b_{12},b_{22},b_{03},b_{13},b_{04}), |  |

and abbreviate

 | P r:= P r ​ ( n). P_{r}:=P_{r}(n). |  |

Then the affine reduction gives

 | ℋ 0, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,1}(n;m,a,b) | = b 01 + A ​ P 1 + B ​ P 0, \displaystyle=b_{01}+AP_{1}+BP_{0}, |  |

 | ℋ 1, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,1}(n;m,a,b) | = b 11 + A ​ P 2 + B ​ P 1, \displaystyle=b_{11}+AP_{2}+BP_{1}, |  |

 | ℋ 2, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{2,1}(n;m,a,b) | = b 21 + A ​ P 3 + B ​ P 2, \displaystyle=b_{21}+AP_{3}+BP_{2}, |  |

 | ℋ 3, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{3,1}(n;m,a,b) | = b 31 + A ​ P 4 + B ​ P 3, \displaystyle=b_{31}+AP_{4}+BP_{3}, |  |

 | ℋ 0, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,2}(n;m,a,b) | = b 02 + 2 ​ A ​ b 11 + 2 ​ B ​ b 01 + A 2 ​ P 2 + 2 ​ A ​ B ​ P 1 + B 2 ​ P 0, \displaystyle=b_{02}+2Ab_{11}+2Bb_{01}+A^{2}P_{2}+2ABP_{1}+B^{2}P_{0}, |  |

 | ℋ 1, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,2}(n;m,a,b) | = b 12 + 2 ​ A ​ b 21 + 2 ​ B ​ b 11 + A 2 ​ P 3 + 2 ​ A ​ B ​ P 2 + B 2 ​ P 1, \displaystyle=b_{12}+2Ab_{21}+2Bb_{11}+A^{2}P_{3}+2ABP_{2}+B^{2}P_{1}, |  |

 | ℋ 2, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{2,2}(n;m,a,b) | = b 22 + 2 ​ A ​ b 31 + 2 ​ B ​ b 21 + A 2 ​ P 4 + 2 ​ A ​ B ​ P 3 + B 2 ​ P 2, \displaystyle=b_{22}+2Ab_{31}+2Bb_{21}+A^{2}P_{4}+2ABP_{3}+B^{2}P_{2}, |  |

 | ℋ 0, 3 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,3}(n;m,a,b) | = b 03 + 3 ​ A ​ b 12 + 3 ​ B ​ b 02 + 3 ​ A 2 ​ b 21 + 6 ​ A ​ B ​ b 11 + 3 ​ B 2 ​ b 01 \displaystyle=b_{03}+3Ab_{12}+3Bb_{02}+3A^{2}b_{21}+6ABb_{11}+3B^{2}b_{01} |  |

 |  | + A 3 ​ P 3 + 3 ​ A 2 ​ B ​ P 2 + 3 ​ A ​ B 2 ​ P 1 + B 3 ​ P 0, \displaystyle\qquad+A^{3}P_{3}+3A^{2}BP_{2}+3AB^{2}P_{1}+B^{3}P_{0}, |  |

 | ℋ 1, 3 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,3}(n;m,a,b) | = b 13 + 3 ​ A ​ b 22 + 3 ​ B ​ b 12 + 3 ​ A 2 ​ b 31 + 6 ​ A ​ B ​ b 21 + 3 ​ B 2 ​ b 11 \displaystyle=b_{13}+3Ab_{22}+3Bb_{12}+3A^{2}b_{31}+6ABb_{21}+3B^{2}b_{11} |  |

 |  | + A 3 ​ P 4 + 3 ​ A 2 ​ B ​ P 3 + 3 ​ A ​ B 2 ​ P 2 + B 3 ​ P 1, \displaystyle\qquad+A^{3}P_{4}+3A^{2}BP_{3}+3AB^{2}P_{2}+B^{3}P_{1}, |  |

 | ℋ 0, 4 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,4}(n;m,a,b) | = b 04 + 4 ​ A ​ b 13 + 4 ​ B ​ b 03 + 6 ​ A 2 ​ b 22 + 12 ​ A ​ B ​ b 12 + 6 ​ B 2 ​ b 02 \displaystyle=b_{04}+4Ab_{13}+4Bb_{03}+6A^{2}b_{22}+12ABb_{12}+6B^{2}b_{02} |  |

 |  | + 4 ​ A 3 ​ b 31 + 12 ​ A 2 ​ B ​ b 21 + 12 ​ A ​ B 2 ​ b 11 + 4 ​ B 3 ​ b 01 \displaystyle\qquad+4A^{3}b_{31}+12A^{2}Bb_{21}+12AB^{2}b_{11}+4B^{3}b_{01} |  |

 |  | + A 4 ​ P 4 + 4 ​ A 3 ​ B ​ P 3 + 6 ​ A 2 ​ B 2 ​ P 2 + 4 ​ A ​ B 3 ​ P 1 + B 4 ​ P 0. \displaystyle\qquad+A^{4}P_{4}+4A^{3}BP_{3}+6A^{2}B^{2}P_{2}+4AB^{3}P_{1}+B^{4}P_{0}. |  |

### C.4 Reciprocal step

Now assume

 | 0 ⩽ a, b < m. 0\leqslant a,b<m. |  |

Set

 | Y:= ⌊ a ⁡ ( n − 1) + b m ⌋. Y:=\left\lfloor\frac{a(n-1)+b}{m}\right\rfloor. |  |

If Y = 0 Y=0, then all ten moments vanish.

Otherwise define

 | g ⁡ ( t):= ⌊ m ​ t + ( m − b − 1) a ⌋, 0 ⩽ t ⩽ Y − 1. g(t):=\left\lfloor\frac{mt+(m-b-1)}{a}\right\rfloor,\qquad 0\leqslant t\leqslant Y-1. |  |

As usual, the reciprocal transformation exchanges the graph of

 | f ⁡ ( x):= ⌊ a ​ x + b m ⌋ f(x):=\left\lfloor\frac{ax+b}{m}\right\rfloor |  |

with the complementary staircase determined by g g, and therefore expresses the moments for ( n, m, a, b) (n;m,a,b) through the moments for ( Y, a, m, m − b − 1) (Y;a,m,m-b-1).

Write

 | 𝐆 = 𝐇 ⁡ ( Y, a, m, m − b − 1) = ( g 01, g 11, g 21, g 31, g 02, g 12, g 22, g 03, g 13, g 04), \mathbf{G}=\mathbf{H}(Y;a,m,m-b-1)=(g_{01},g_{11},g_{21},g_{31},g_{02},g_{12},g_{22},g_{03},g_{13},g_{04}), |  |

and let

 | P r:= P r ​ ( n), Q r:= P r ​ ( Y). P_{r}:=P_{r}(n),\qquad Q_{r}:=P_{r}(Y). |  |

Then

 | ℋ 0, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,1}(n;m,a,b) | = P 0 ​ Y − Q 0 − g 01, \displaystyle=P_{0}Y-Q_{0}-g_{01}, |  |

 | ℋ 1, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,1}(n;m,a,b) | = 2 ​ P 1 ​ Y − g 01 − g 02 2, \displaystyle=\frac{2P_{1}Y-g_{01}-g_{02}}{2}, |  |

 | ℋ 2, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{2,1}(n;m,a,b) | = 6 ​ P 2 ​ Y − g 01 − 3 ​ g 02 − 2 ​ g 03 6, \displaystyle=\frac{6P_{2}Y-g_{01}-3g_{02}-2g_{03}}{6}, |  |

 | ℋ 3, 1 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{3,1}(n;m,a,b) | = 4 ​ P 3 ​ Y − g 02 − 2 ​ g 03 − g 04 4, \displaystyle=\frac{4P_{3}Y-g_{02}-2g_{03}-g_{04}}{4}, |  |

 | ℋ 0, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,2}(n;m,a,b) | = P 0 ​ Y 2 − Q 0 − g 01 − 2 ​ Q 1 − 2 ​ g 11, \displaystyle=P_{0}Y^{2}-Q_{0}-g_{01}-2Q_{1}-2g_{11}, |  |

 | ℋ 1, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,2}(n;m,a,b) | = 2 ​ P 1 ​ Y 2 − g 01 − g 02 − 2 ​ g 11 − 2 ​ g 12 2, \displaystyle=\frac{2P_{1}Y^{2}-g_{01}-g_{02}-2g_{11}-2g_{12}}{2}, |  |

 | ℋ 2, 2 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{2,2}(n;m,a,b) | = 6 ​ P 2 ​ Y 2 − g 01 − 3 ​ g 02 − 2 ​ g 03 − 2 ​ g 11 − 6 ​ g 12 − 4 ​ g 13 6, \displaystyle=\frac{6P_{2}Y^{2}-g_{01}-3g_{02}-2g_{03}-2g_{11}-6g_{12}-4g_{13}}{6}, |  |

 | ℋ 0, 3 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,3}(n;m,a,b) | = P 0 ​ Y 3 − Q 0 − g 01 − 3 ​ Q 1 − 3 ​ g 11 − 3 ​ Q 2 − 3 ​ g 21, \displaystyle=P_{0}Y^{3}-Q_{0}-g_{01}-3Q_{1}-3g_{11}-3Q_{2}-3g_{21}, |  |

 | ℋ 1, 3 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{1,3}(n;m,a,b) | = 2 ​ P 1 ​ Y 3 − g 01 − g 02 − 3 ​ g 11 − 3 ​ g 12 − 3 ​ g 21 − 3 ​ g 22 2, \displaystyle=\frac{2P_{1}Y^{3}-g_{01}-g_{02}-3g_{11}-3g_{12}-3g_{21}-3g_{22}}{2}, |  |

 | ℋ 0, 4 ​ ( n, m, a, b) \displaystyle\mathcal{H}_{0,4}(n;m,a,b) | = P 0 ​ Y 4 − Q 0 − g 01 − 4 ​ Q 1 − 4 ​ g 11 − 6 ​ Q 2 − 6 ​ g 21 − 4 ​ Q 3 − 4 ​ g 31. \displaystyle=P_{0}Y^{4}-Q_{0}-g_{01}-4Q_{1}-4g_{11}-6Q_{2}-6g_{21}-4Q_{3}-4g_{31}. |  |

###### Lemma 24.

The ten moments

 | ℋ 0, 1, ℋ 1, 1, ℋ 2, 1, ℋ 3, 1, ℋ 0, 2, ℋ 1, 2, ℋ 2, 2, ℋ 0, 3, ℋ 1, 3, ℋ 0, 4 \mathcal{H}_{0,1},\ \mathcal{H}_{1,1},\ \mathcal{H}_{2,1},\ \mathcal{H}_{3,1},\ \mathcal{H}_{0,2},\ \mathcal{H}_{1,2},\ \mathcal{H}_{2,2},\ \mathcal{H}_{0,3},\ \mathcal{H}_{1,3},\ \mathcal{H}_{0,4} |  |

admit a recursive evaluation in O ⁡ ( log ⁡ m) O(\log m) arithmetic operations.

###### Proof.

The affine step reduces ( a, b) (a,b) modulo m m. The reciprocal step replaces ( n, m, a, b) (n;m,a,b) by

 | ( Y, a, m, m − b − 1), Y = ⌊ a ⁡ ( n − 1) + b m ⌋, (Y;a,m,m-b-1),\qquad Y=\left\lfloor\frac{a(n-1)+b}{m}\right\rfloor, |  |

so the first modulus strictly decreases from m m to a < m a<m. Hence the recursion has Euclidean depth O ⁡ ( log ⁡ m) O(\log m). Each step performs only O ⁡ ( 1) O(1) arithmetic operations on the ten stored moments and the power sums. ∎

### C.5 Complexity bound

Each recursive call either reduces a a and b b modulo m m (the affine step) or swaps the roles of ( a, m) (a,m) with strictly smaller Euclidean parameters (the reciprocal step). Hence the recursion depth is O ⁡ ( log ⁡ m) = O ⁡ ( log ⁡ n) O(\log m)=O(\log n). Every step performs only O ⁡ ( 1) O(1) arithmetic operations on a constant-size family of moments. This proves Corollary 12.

## Appendix D Implementation notes

This appendix records two implementation-level simplifications for the ten-moment weighted-floor kernel. They do not change the asymptotic complexity, but together they reduce the constant factor substantially; in our implementation, the combined speedup is a little over 3 × 3\times.

First, we use explicit affine and reciprocal transition formulas instead of constructing the symbolic expansions at run time. This turns each update into a fixed straight-line computation and eliminates most temporary algebra.

Second, we special-case the two most common affine subcases, namely B = 0 B=0 and, within it, A = 1 A=1. Since these patterns occur frequently in the Euclidean recursion, handling them with short handwritten formulas removes another layer of arithmetic overhead.

## Appendix E Proof of the two-term asymptotic expansion

In this appendix we prove Theorem 22. We write

 | S 1 ​ ( n):= 2 ​ ∑ u > v ⩾ 1 ( u, v) = 1 u, v ⩽ n ∑ a, b ⩾ 1 a ​ u + b ​ v ⩽ n a ​ v + b ​ u ⩽ n ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u), S_{1}(n):=2\sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ u,v\leqslant\sqrt{n}\end{subarray}}\ \sum_{\begin{subarray}{c}a,b\geqslant 1\\ au+bv\leqslant n\\ av+bu\leqslant n\end{subarray}}(n-au-bv)(n-av-bu), |  |

 | S 2 ​ ( n):= 2 ​ ∑ 1 ⩽ a, b ⩽ n ∑ u > v ⩾ 1 ( u, v) = 1 a ​ u + b ​ v ⩽ n a ​ v + b ​ u ⩽ n ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u), S_{2}(n):=2\sum_{1\leqslant a,b\leqslant\sqrt{n}}\ \sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ au+bv\leqslant n\\ av+bu\leqslant n\end{subarray}}(n-au-bv)(n-av-bu), |  |

 | S 12 ​ ( n):= 2 ​ ∑ u > v ⩾ 1 ( u, v) = 1 u, v ⩽ n ∑ 1 ⩽ a, b ⩽ n a ​ u + b ​ v ⩽ n a ​ v + b ​ u ⩽ n ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u). S_{12}(n):=2\sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ u,v\leqslant\sqrt{n}\end{subarray}}\ \sum_{\begin{subarray}{c}1\leqslant a,b\leqslant\sqrt{n}\\ au+bv\leqslant n\\ av+bu\leqslant n\end{subarray}}(n-au-bv)(n-av-bu). |  |

Thus F ⁡ ( n) = S 1 ​ ( n) + S 2 ​ ( n) − S 12 ​ ( n) + F 0 ​ ( n) F(n)=S_{1}(n)+S_{2}(n)-S_{12}(n)+F_{0}(n). We derive the required expansions in the order S 1 S_{1}, S 2 S_{2}, S 12 S_{12}, and then assemble them. All remainders in this appendix are tracked only up to o ⁡ ( n 4) o(n^{4}). For the linear constraints defining the summation regions, we use non-strict inequalities throughout, since on the boundary the weight ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u) (n-au-bv)(n-av-bu) vanishes identically. Thus replacing a condition of the form a ​ u + b ​ v < n au+bv<n or a ​ v + b ​ u < n av+bu<n by the corresponding non-strict version does not change the summand at any lattice point. The only genuinely strict inequality that remains is the ordering constraint u > v u>v; for the primitive-direction parameters below we work on the closed triangle T = { ( x, y): 0 ⩽ y ⩽ x ⩽ 1 } T=\{(x,y):0\leqslant y\leqslant x\leqslant 1\}.

### E.1 Shared inputs for S 1 S_{1} and S 2 S_{2}

The next two lemmas are used in both the S 1 S_{1} and S 2 S_{2} analyses.

###### Lemma 25 (evaluation of the kernel).

For p ⩾ q > 0 p\geqslant q>0, let

 | K ⁡ ( p, q):= ∬ α, β > 0 p ​ α + q ​ β < 1 q ​ α + p ​ β < 1 ( 1 − p ​ α − q ​ β) ​ ( 1 − q ​ α − p ​ β) ​ 𝑑 α ​ 𝑑 β. K(p,q):=\iint_{\begin{subarray}{c}\alpha,\beta>0\\ p\alpha+q\beta<1\\ q\alpha+p\beta<1\end{subarray}}(1-p\alpha-q\beta)(1-q\alpha-p\beta)\,d\alpha\,d\beta. |  |

Then K ⁡ ( p, q) = 3 ​ p − q 12 ​ p 2 ​ ( p + q) = 1 3 ​ p ​ ( p + q) − 1 12 ​ p 2 K(p,q)=\frac{3p-q}{12p^{2}(p+q)}=\frac{1}{3p(p+q)}-\frac{1}{12p^{2}} for p > q p>q, while K ⁡ ( p, p) = 1 12 ​ p 2 K(p,p)=\frac{1}{12p^{2}}.

###### Proof.

For p > q p>q, set x = p ​ α + q ​ β x=p\alpha+q\beta and y = q ​ α + p ​ β y=q\alpha+p\beta. The Jacobian is p 2 − q 2 p^{2}-q^{2}, and the inverse map is

 | α = p ​ x − q ​ y p 2 − q 2, β = p ​ y − q ​ x p 2 − q 2. \alpha=\frac{px-qy}{p^{2}-q^{2}},\qquad\beta=\frac{py-qx}{p^{2}-q^{2}}. |  |

Hence

 | K ⁡ ( p, q) = 1 p 2 − q 2 ​ ∬ 0 < x < 1, 0 < y < 1 q ​ x < p ​ y, q ​ y < p ​ x ( 1 − x) ​ ( 1 − y) ​ 𝑑 x ​ 𝑑 y. K(p,q)=\frac{1}{p^{2}-q^{2}}\iint_{\begin{subarray}{c}0<x<1,\ 0<y<1\\ qx<py,\ qy<px\end{subarray}}(1-x)(1-y)\,dx\,dy. |  |

For fixed x ∈ ( 0, 1) x\in(0,1), the variable y y ranges over q p ​ x < y < min ⁡ ( p q ​ x, 1) \frac{q}{p}x<y<\min(\frac{p}{q}x,1), so splitting at x = q / p x=q/p gives

 | K ⁡ ( p, q) = 1 p 2 − q 2 ​ ( ∫ 0 q / p ∫ ( q / p) ​ x ( p / q) ​ x ( 1 − x) ​ ( 1 − y) ​ 𝑑 y ​ 𝑑 x + ∫ q / p 1 ∫ ( q / p) ​ x 1 ( 1 − x) ​ ( 1 − y) ​ 𝑑 y ​ 𝑑 x). K(p,q)=\frac{1}{p^{2}-q^{2}}\left(\int_{0}^{q/p}\!\int_{(q/p)x}^{(p/q)x}(1-x)(1-y)\,dy\,dx+\int_{q/p}^{1}\!\int_{(q/p)x}^{1}(1-x)(1-y)\,dy\,dx\right). |  |

The required elementary integrations are polynomial integrations over triangular regions, a special case of integration over simplices [12]. Evaluating them yields K ⁡ ( p, q) = 3 ​ p − q 12 ​ p 2 ​ ( p + q) K(p,q)=\frac{3p-q}{12p^{2}(p+q)}. For p = q p=q, the region is α + β < 1 / p \alpha+\beta<1/p, hence

 | K ⁡ ( p, p) = ∫ 0 1 / p ∫ 0 1 / p − α ( 1 − p ​ α − p ​ β) 2 ​ 𝑑 β ​ 𝑑 α = 1 12 ​ p 2. ∎ K(p,p)=\int_{0}^{1/p}\int_{0}^{1/p-\alpha}(1-p\alpha-p\beta)^{2}\,d\beta\,d\alpha=\frac{1}{12p^{2}}.\qed |  |

###### Lemma 26.

One has ∑ m ⩾ 1 ( H 2 ​ m − 1 − H m − log ⁡ 2) / m = log 2 ⁡ 2 − π 2 / 6 \sum_{m\geqslant 1}(H_{2m-1}-H_{m}-\log 2)/m=\log^{2}2-\pi^{2}/6.

###### Proof.

Set U:= ∑ m ⩾ 1 ( H 2 ​ m − H m − log ⁡ 2) / m U:=\sum_{m\geqslant 1}(H_{2m}-H_{m}-\log 2)/m. Since H 2 ​ m − 1 = H 2 ​ m − 1 / ( 2 ​ m) H_{2m-1}=H_{2m}-1/(2m),

 | ∑ m ⩾ 1 H 2 ​ m − 1 − H m − log ⁡ 2 m = U − 1 2 ​ ∑ m ⩾ 1 1 m 2 = U − π 2 12. \sum_{m\geqslant 1}\frac{H_{2m-1}-H_{m}-\log 2}{m}=U-\frac{1}{2}\sum_{m\geqslant 1}\frac{1}{m^{2}}=U-\frac{\pi^{2}}{12}. |  |

Also H 2 ​ m − H m − log ⁡ 2 = O ⁡ ( 1 / m) H_{2m}-H_{m}-\log 2=O(1/m), so the defining series for U U is absolutely convergent. Using the classical generating function [2, Sec. 6.3]

 | ∑ n ⩾ 1 H n n ​ x n = Li 2 ⁡ ( x) + 1 2 ​ log 2 ⁡ ( 1 − x) ( | x | < 1), \sum_{n\geqslant 1}\frac{H_{n}}{n}x^{n}=\operatorname{Li}_{2}(x)+\frac{1}{2}\log^{2}(1-x)\qquad(|x|<1), |  |

we get for 0 < x < 1 0<x<1,

 | ∑ m ⩾ 1 H 2 ​ m − H m − log ⁡ 2 m ​ x m = F ⁡ ( x) + F ⁡ ( − x) − F ⁡ ( x) + log ⁡ 2 ​ log ⁡ ( 1 − x), \sum_{m\geqslant 1}\frac{H_{2m}-H_{m}-\log 2}{m}x^{m}=F(\sqrt{x})+F(-\sqrt{x})-F(x)+\log 2\,\log(1-x), |  |

where F ⁡ ( t):= Li 2 ⁡ ( t) + 1 2 ​ log 2 ⁡ ( 1 − t) F(t):=\operatorname{Li}_{2}(t)+\frac{1}{2}\log^{2}(1-t). The duplication identity

 | Li 2 ⁡ ( t) + Li 2 ⁡ ( − t) = 1 2 ​ Li 2 ⁡ ( t 2) \operatorname{Li}_{2}(t)+\operatorname{Li}_{2}(-t)=\frac{1}{2}\operatorname{Li}_{2}(t^{2}) |  |

(compare [6, Eq. 25.12.12]) shows that the right-hand side tends to log 2 ⁡ 2 − π 2 / 12 \log^{2}2-\pi^{2}/12 as x → 1 − x\to 1^{-}. Since the coefficients are absolutely summable, the series on the left converges absolutely at x = 1 x=1 and uniformly for x ∈ [0, 1] x\in[0,1]. Therefore one may pass to the limit x → 1 − x\to 1^{-} termwise, and the left-hand side tends to U U. Hence U = log 2 ⁡ 2 − π 2 / 12 U=\log^{2}2-\pi^{2}/12, and the claim follows. ∎

###### Remark 27 (parametric Euler–Maclaurin patching).

We use a standard local form of weighted Euler–Maclaurin summation on polytopal families; compare, for example, the polytope expansions in [11]. Let Θ \Theta be a compact parameter set, and suppose that it is covered by finitely many relatively open cells Θ ν \Theta_{\nu} such that on each cell the family of polygons P θ P_{\theta} has fixed combinatorial type, the defining affine inequalities depend C 2 C^{2} -smoothly on θ ∈ Θ ν \theta\in\Theta_{\nu}, and the weights w θ ∈ C 2 ​ ( P θ) w_{\theta}\in C^{2}(P_{\theta}) depend C 2 C^{2} -smoothly on θ \theta with bounds uniform on compact subsets of Θ ν \Theta_{\nu}. On each cell, the weighted Euler–Maclaurin formula therefore gives an expansion

 | ∑ m ∈ T ​ P θ ∩ ℤ 2 w θ ​ ( m / T) = T 2 ​ A ν ​ ( θ) + T ​ B ν ​ ( θ) + O ⁡ ( 1) ( T ⩾ 1), \sum_{m\in TP_{\theta}\cap\mathbb{Z}^{2}}w_{\theta}(m/T)=T^{2}A_{\nu}(\theta)+TB_{\nu}(\theta)+O(1)\qquad(T\geqslant 1), |  |

uniformly for θ \theta in compact subsets of Θ ν \Theta_{\nu}.

In the applications below, one checks directly that the area coefficient

 | A ⁡ ( θ):= ∬ P θ w θ ​ ( x) ​ 𝑑 x A(\theta):=\iint_{P_{\theta}}w_{\theta}(x)\,dx |  |

extends continuously and remains bounded on all of Θ \Theta, and, when the linear term is needed, that the boundary coefficient

 | B ⁡ ( θ):= 1 2 ​ ∑ E ⊂ ∂ P θ ∫ E w θ ​ d ​ σ E B(\theta):=\frac{1}{2}\sum_{E\subset\partial P_{\theta}}\int_{E}w_{\theta}\,d\sigma_{E} |  |

does as well. Once these bounded continuous extensions across the finitely many transition strata have been verified, the cellwise expansions may be patched into a single uniform estimate on Θ \Theta of the same shape:

 | ∑ m ∈ T ​ P θ ∩ ℤ 2 w θ ​ ( m / T) = T 2 ​ A ​ ( θ) + T ​ B ​ ( θ) + O ⁡ ( 1), \sum_{m\in TP_{\theta}\cap\mathbb{Z}^{2}}w_{\theta}(m/T)=T^{2}A(\theta)+TB(\theta)+O(1), |  |

or, if only the area term is used, simply

 | ∑ m ∈ T ​ P θ ∩ ℤ 2 w θ ​ ( m / T) = T 2 ​ A ​ ( θ) + O ⁡ ( T). \sum_{m\in TP_{\theta}\cap\mathbb{Z}^{2}}w_{\theta}(m/T)=T^{2}A(\theta)+O(T). |  |

This is exactly the way Euler–Maclaurin is invoked in the analyses of S 1 S_{1}, S 2 S_{2}, and S 12 S_{12}.

###### Remark 28 (replacing n \sqrt{n} by ⌊ n ⌋ \lfloor\sqrt{n}\rfloor).

Let N:= ⌊ n ⌋ N:=\lfloor\sqrt{n}\rfloor. Then

 | N = n + O ⁡ ( 1), log ⁡ N = 1 2 ​ log ⁡ n + o ⁡ ( 1), N 8 = n 4 + o ⁡ ( n 4). N=\sqrt{n}+O(1),\qquad\log N=\frac{1}{2}\log n+o(1),\qquad N^{8}=n^{4}+o(n^{4}). |  |

In particular,

 | n 3 ​ log ​ n = o ⁡ ( n 4), n 3 ​ N = o ⁡ ( n 4), N 7 = o ⁡ ( n 4), N 7 ​ log ​ N = o ⁡ ( n 4). n^{3}\log n=o(n^{4}),\qquad n^{3}N=o(n^{4}),\qquad N^{7}=o(n^{4}),\qquad N^{7}\log N=o(n^{4}). |  |

### E.2 The contribution S 1 S_{1}

###### Lemma 29.

As N → ∞ N\to\infty, one has ∑ u ⩽ N φ ⁡ ( u) / u 2 = 6 π 2 ​ log ⁡ N + ( 6 ​ γ π 2 − ζ ′ ​ ( 2) ζ ​ ( 2) 2) + o ⁡ ( 1) \sum_{u\leqslant N}\varphi(u)/u^{2}=\frac{6}{\pi^{2}}\log N+\bigl(\frac{6\gamma}{\pi^{2}}-\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}\bigr)+o(1).

###### Proof.

Put a n:= φ ⁡ ( n) / n a_{n}:=\varphi(n)/n. Then

 | ∑ n ⩾ 1 a n n s = ∑ n ⩾ 1 φ ⁡ ( n) n s + 1 = ζ ⁡ ( s) ζ ⁡ ( s + 1) ( ℜ ⁡ s > 1). \sum_{n\geqslant 1}\frac{a_{n}}{n^{s}}=\sum_{n\geqslant 1}\frac{\varphi(n)}{n^{s+1}}=\frac{\zeta(s)}{\zeta(s+1)}\qquad(\Re s>1). |  |

As s → 1 + s\to 1^{+},

 | ζ ⁡ ( s) ζ ⁡ ( s + 1) = 6 π 2 ​ 1 s − 1 + ( 6 ​ γ π 2 − ζ ′ ​ ( 2) ζ ​ ( 2) 2) + O ⁡ ( s − 1). \frac{\zeta(s)}{\zeta(s+1)}=\frac{6}{\pi^{2}}\frac{1}{s-1}+\left(\frac{6\gamma}{\pi^{2}}-\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}\right)+O(s-1). |  |

By Delange’s theorem for Dirichlet series with a simple pole (see [5, Ch. II.5, Th. 3]; compare also [4, Ch. 5, §1]), this implies

 | ∑ n ⩽ N a n n = ∑ n ⩽ N φ ⁡ ( n) n 2 = 6 π 2 ​ log ⁡ N + ( 6 ​ γ π 2 − ζ ′ ​ ( 2) ζ ​ ( 2) 2) + o ⁡ ( 1), \sum_{n\leqslant N}\frac{a_{n}}{n}=\sum_{n\leqslant N}\frac{\varphi(n)}{n^{2}}=\frac{6}{\pi^{2}}\log N+\left(\frac{6\gamma}{\pi^{2}}-\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}\right)+o(1), |  |

as claimed. ∎

###### Lemma 30 (kernel row sum).

For u ⩾ 2 u\geqslant 2, let k ⁡ ( u):= ∑ 1 ⩽ v < u ( u, v) = 1 K ⁡ ( u, v) k(u):=\sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}K(u,v). Then

 | k ⁡ ( u) = 4 ​ log ⁡ 2 − 1 12 ​ φ ⁡ ( u) u 2 + r ⁡ ( u), r ⁡ ( u) = O ⁡ ( τ ⁡ ( u) u 2), k(u)=\frac{4\log 2-1}{12}\frac{\varphi(u)}{u^{2}}+r(u),\qquad r(u)=O\!\left(\frac{\tau(u)}{u^{2}}\right), |  |

and therefore

 | ∑ u ⩽ N k ⁡ ( u) = 4 ​ log ⁡ 2 − 1 2 ​ π 2 ​ log ⁡ N + D 1 + o ⁡ ( 1), \sum_{u\leqslant N}k(u)=\frac{4\log 2-1}{2\pi^{2}}\log N+D_{1}+o(1), |  |

where

 | D 1 = 4 ​ log ⁡ 2 − 1 12 ​ ( 6 ​ γ π 2 − ζ ′ ​ ( 2) ζ ​ ( 2) 2 − 1) + 2 ​ log 2 ​ 2 π 2 + log ⁡ 2 3 − 1 3. D_{1}=\frac{4\log 2-1}{12}\left(\frac{6\gamma}{\pi^{2}}-\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}-1\right)+\frac{2\log^{2}2}{\pi^{2}}+\frac{\log 2}{3}-\frac{1}{3}. |  |

###### Proof.

By Lemma 25,

 | k ⁡ ( u) = 1 3 ​ u ​ ∑ 1 ⩽ v < u ( u, v) = 1 1 u + v − φ ⁡ ( u) 12 ​ u 2. k(u)=\frac{1}{3u}\sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}\frac{1}{u+v}-\frac{\varphi(u)}{12u^{2}}. |  |

Using inclusion–exclusion,

 | ∑ 1 ⩽ v < u ( u, v) = 1 1 u + v = ∑ d | u μ ⁡ ( d) ​ ∑ 1 ⩽ v < u d | v 1 u + v = ∑ d | u μ ⁡ ( d) d ​ ∑ 1 ⩽ m < u / d 1 u / d + m. \sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}\frac{1}{u+v}=\sum_{d\mid u}\mu(d)\sum_{\begin{subarray}{c}1\leqslant v<u\\ d\mid v\end{subarray}}\frac{1}{u+v}=\sum_{d\mid u}\frac{\mu(d)}{d}\sum_{1\leqslant m<u/d}\frac{1}{u/d+m}. |  |

Since ∑ 1 ⩽ m < M ( M + m) − 1 = H 2 ​ M − 1 − H M \sum_{1\leqslant m<M}(M+m)^{-1}=H_{2M-1}-H_{M}, this becomes

 | ∑ 1 ⩽ v < u ( u, v) = 1 1 u + v = ∑ d | u μ ⁡ ( d) d ​ ( H 2 ​ u / d − 1 − H u / d). \sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}\frac{1}{u+v}=\sum_{d\mid u}\frac{\mu(d)}{d}\Bigl(H_{2u/d-1}-H_{u/d}\Bigr). |  |

Hence

 | k ⁡ ( u) = 4 ​ log ⁡ 2 − 1 12 ​ φ ⁡ ( u) u 2 + 1 3 ​ u ​ ∑ d | u μ ⁡ ( d) d ​ ( H 2 ​ u / d − 1 − H u / d − log ⁡ 2). k(u)=\frac{4\log 2-1}{12}\frac{\varphi(u)}{u^{2}}+\frac{1}{3u}\sum_{d\mid u}\frac{\mu(d)}{d}\Bigl(H_{2u/d-1}-H_{u/d}-\log 2\Bigr). |  |

The displayed remainder is O ⁡ ( τ ⁡ ( u) / u 2) O(\tau(u)/u^{2}) because H 2 ​ m − 1 − H m − log ⁡ 2 = O ⁡ ( 1 / m) H_{2m-1}-H_{m}-\log 2=O(1/m) uniformly in m ⩾ 1 m\geqslant 1. Let

 | R ⁡ ( N):= ∑ u ⩽ N 1 3 ​ u ​ ∑ d | u μ ⁡ ( d) d ​ ( H 2 ​ u / d − 1 − H u / d − log ⁡ 2). R(N):=\sum_{u\leqslant N}\frac{1}{3u}\sum_{d\mid u}\frac{\mu(d)}{d}\Bigl(H_{2u/d-1}-H_{u/d}-\log 2\Bigr). |  |

Setting u = d ​ m u=dm and exchanging the order of summation gives

 | R ⁡ ( N) = 1 3 ​ ∑ m ⩽ N H 2 ​ m − 1 − H m − log ⁡ 2 m ​ ∑ d ⩽ N / m μ ⁡ ( d) d 2. R(N)=\frac{1}{3}\sum_{m\leqslant N}\frac{H_{2m-1}-H_{m}-\log 2}{m}\sum_{d\leqslant N/m}\frac{\mu(d)}{d^{2}}. |  |

Since H 2 ​ m − 1 − H m − log ⁡ 2 = O ⁡ ( 1 / m) H_{2m-1}-H_{m}-\log 2=O(1/m), the series

 | ∑ m ⩾ 1 | H 2 ​ m − 1 − H m − log ⁡ 2 | m \sum_{m\geqslant 1}\frac{|H_{2m-1}-H_{m}-\log 2|}{m} |  |

converges. Therefore the rearrangement above is absolutely summable, and the passage to the limit below is justified by dominated convergence. Since ∑ d ⩽ X μ ⁡ ( d) / d 2 = 1 / ζ ⁡ ( 2) + O ⁡ ( X − 1) \sum_{d\leqslant X}\mu(d)/d^{2}=1/\zeta(2)+O(X^{-1}), we obtain

 | R ⁡ ( N) = 1 3 ​ ζ ​ ( 2) ​ ∑ m ⩾ 1 H 2 ​ m − 1 − H m − log ⁡ 2 m + o ⁡ ( 1) = 2 ​ log 2 ​ 2 π 2 − 1 6 + o ⁡ ( 1). R(N)=\frac{1}{3\zeta(2)}\sum_{m\geqslant 1}\frac{H_{2m-1}-H_{m}-\log 2}{m}+o(1)=\frac{2\log^{2}2}{\pi^{2}}-\frac{1}{6}+o(1). |  |

Combining this with Lemma 29 gives

 | ∑ u ⩽ N k ⁡ ( u) = 4 ​ log ⁡ 2 − 1 2 ​ π 2 ​ log ⁡ N + 4 ​ log ⁡ 2 − 1 12 ​ ( 6 ​ γ π 2 − ζ ′ ​ ( 2) ζ ​ ( 2) 2) + 2 ​ log 2 ​ 2 π 2 − 1 6 + o ⁡ ( 1). \sum_{u\leqslant N}k(u)=\frac{4\log 2-1}{2\pi^{2}}\log N+\frac{4\log 2-1}{12}\Bigl(\frac{6\gamma}{\pi^{2}}-\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}\Bigr)+\frac{2\log^{2}2}{\pi^{2}}-\frac{1}{6}+o(1). |  |

Since the lemma sums over u ⩾ 2 u\geqslant 2, we must subtract the u = 1 u=1 contribution ( 4 ​ log ⁡ 2 − 1) / 12 (4\log 2-1)/12. This yields exactly the stated constant D 1 D_{1}. ∎

###### Theorem 31 (asymptotic for S 1 S_{1}).

One has

 | S 1 ​ ( n) = A 1 ​ n 4 ​ log ⁡ n + B 1 ​ n 4 + o ⁡ ( n 4), S_{1}(n)=A_{1}n^{4}\log n+B_{1}n^{4}+o(n^{4}), |  |

where A 1 = 4 ​ log ⁡ 2 − 1 2 ​ π 2 A_{1}=\frac{4\log 2-1}{2\pi^{2}} and

 | B 1 = 4 ​ log ⁡ 2 − 1 6 ​ ( 6 ​ γ π 2 − ζ ′ ​ ( 2) ζ ​ ( 2) 2 − 1) + 4 ​ log 2 ​ 2 π 2 + 2 ​ log ⁡ 2 3 − 2 3. B_{1}=\frac{4\log 2-1}{6}\left(\frac{6\gamma}{\pi^{2}}-\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}-1\right)+\frac{4\log^{2}2}{\pi^{2}}+\frac{2\log 2}{3}-\frac{2}{3}. |  |

###### Proof.

Let N:= ⌊ n ⌋ N:=\lfloor\sqrt{n}\rfloor. For fixed primitive u > v u>v, define

 | G n ​ ( u, v):= ∑ a, b ⩾ 1 a ​ u + b ​ v ⩽ n a ​ v + b ​ u ⩽ n ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u). G_{n}(u,v):=\sum_{\begin{subarray}{c}a,b\geqslant 1\\ au+bv\leqslant n\\ av+bu\leqslant n\end{subarray}}(n-au-bv)(n-av-bu). |  |

Write

 | P u, v:= { ( α, β) ∈ ℝ ⩾ 0 2: u α + v β ⩽ 1, v α + u β ⩽ 1 } P_{u,v}:=\{(\alpha,\beta)\in\mathbb{R}_{\geqslant 0}^{2}:u\alpha+v\beta\leqslant 1,\ v\alpha+u\beta\leqslant 1\} |  |

and

 | w u, v ​ ( α, β):= ( 1 − u ​ α − v ​ β) ​ ( 1 − v ​ α − u ​ β). w_{u,v}(\alpha,\beta):=(1-u\alpha-v\beta)(1-v\alpha-u\beta). |  |

Then

 | G n ​ ( u, v) = n 2 ​ ∑ ( a, b) ∈ n ​ P u, v ∩ ℤ ⩾ 1 2 w u, v ​ ( a / n, b / n). G_{n}(u,v)=n^{2}\sum_{(a,b)\in nP_{u,v}\cap\mathbb{Z}_{\geqslant 1}^{2}}w_{u,v}(a/n,b/n). |  |

After the normalization ( α ~, β ~) = ( u ​ α, u ​ β) (\tilde{\alpha},\tilde{\beta})=(u\alpha,u\beta) and λ:= v / u ∈ [0, 1] \lambda:=v/u\in[0,1], the polygons become

 | P ~ λ:= { ( α ~, β ~) ∈ ℝ ⩾ 0 2: α ~ + λ β ~ ⩽ 1, λ α ~ + β ~ ⩽ 1 }, \widetilde{P}_{\lambda}:=\{(\tilde{\alpha},\tilde{\beta})\in\mathbb{R}_{\geqslant 0}^{2}:\tilde{\alpha}+\lambda\tilde{\beta}\leqslant 1,\ \lambda\tilde{\alpha}+\tilde{\beta}\leqslant 1\}, |  |

and the weights become

 | w ~ λ ​ ( α ~, β ~):= ( 1 − α ~ − λ ​ β ~) ​ ( 1 − λ ​ α ~ − β ~). \widetilde{w}_{\lambda}(\tilde{\alpha},\tilde{\beta}):=(1-\tilde{\alpha}-\lambda\tilde{\beta})(1-\lambda\tilde{\alpha}-\tilde{\beta}). |  |

Thus ( P ~ λ, w ~ λ) (\widetilde{P}_{\lambda},\widetilde{w}_{\lambda}) form a one-parameter piecewise- C 2 C^{2} family for λ ∈ [0, 1] \lambda\in[0,1]. As λ → 1 \lambda\to 1, the polygon converges continuously to the limiting triangle { α ~, β ~ ⩾ 0, α ~ + β ~ ⩽ 1 } \{\tilde{\alpha},\tilde{\beta}\geqslant 0,\ \tilde{\alpha}+\tilde{\beta}\leqslant 1\}, and the weight remains uniformly C 2 C^{2}. In particular, the area term and the linear boundary term stay uniformly bounded and vary continuously up to λ = 1 \lambda=1. Therefore Remark 27 yields, after checking the continuous extension of the area and boundary coefficients to λ = 1 \lambda=1, uniformly for u > v ⩾ 1 u>v\geqslant 1,

 | n 2 ​ ∑ ( a, b) ∈ n ​ P u, v ∩ ℤ ⩾ 0 2 w u, v ​ ( a / n, b / n) = n 4 ​ K ​ ( u, v) + n 3 ​ L ​ ( u, v) + O ⁡ ( n 2), n^{2}\sum_{(a,b)\in nP_{u,v}\cap\mathbb{Z}_{\geqslant 0}^{2}}w_{u,v}(a/n,b/n)=n^{4}K(u,v)+n^{3}L(u,v)+O(n^{2}), |  |

where the two oblique sides contribute 0 0 because w u, v w_{u,v} vanishes identically there, while the horizontal and vertical sides contribute

 | ∫ 0 1 / u ( 1 − u ​ t) ​ ( 1 − v ​ t) ​ 𝑑 t = 3 ​ u − v 6 ​ u 2 \int_{0}^{1/u}(1-ut)(1-vt)\,dt=\frac{3u-v}{6u^{2}} |  |

each. Hence

 | L ( u, v) = 1 2 ⋅ 2 ∫ 0 1 / u ( 1 − u t) ( 1 − v t) d t = 3 ​ u − v 6 ​ u 2. L(u,v)=\frac{1}{2}\cdot 2\int_{0}^{1/u}(1-ut)(1-vt)\,dt=\frac{3u-v}{6u^{2}}. |  |

Now pass from ℤ ⩾ 0 2 \mathbb{Z}_{\geqslant 0}^{2} to ℤ ⩾ 1 2 \mathbb{Z}_{\geqslant 1}^{2} by deleting the two coordinate-axis slices and then adding back the doubly deleted corner ( 0, 0) (0,0). Along the horizontal axis one has

 | n 2 ​ ∑ 0 ⩽ b ⩽ n / u w u, v ​ ( 0, b / n) = n 2 ​ ∑ 0 ⩽ b ⩽ n / u ( 1 − v ​ b / n) ​ ( 1 − u ​ b / n) = n 3 ​ ∫ 0 1 / u ( 1 − v ​ t) ​ ( 1 − u ​ t) ​ 𝑑 t + O ⁡ ( n 2), n^{2}\sum_{0\leqslant b\leqslant n/u}w_{u,v}(0,b/n)=n^{2}\sum_{0\leqslant b\leqslant n/u}(1-vb/n)(1-ub/n)=n^{3}\int_{0}^{1/u}(1-vt)(1-ut)\,dt+O(n^{2}), |  |

by the one-dimensional Euler–Maclaurin formula, and the same estimate holds on the vertical axis. The one-dimensional Euler–Maclaurin remainder here is uniform in u, v ⩽ N u,v\leqslant N: the interval has length 1 / u 1/u, while for f u, v ​ ( t):= ( 1 − v ​ t) ​ ( 1 − u ​ t) f_{u,v}(t):=(1-vt)(1-ut) one has | f u, v ​ ( t) | ⩽ 1 |f_{u,v}(t)|\leqslant 1 and | f u, v ′′ ​ ( t) | = 2 ​ u ​ v |f_{u,v}^{\prime\prime}(t)|=2uv on [0, 1 / u] [0,1/u]. Thus the usual one-dimensional remainder is O ⁡ ( 1) O(1) before the outside factor n 2 n^{2}, hence O ⁡ ( n 2) O(n^{2}) after rescaling. Hence the two deleted slices together subtract

 | 2 ​ n 3 ​ ∫ 0 1 / u ( 1 − v ​ t) ​ ( 1 − u ​ t) ​ 𝑑 t + O ⁡ ( n 2) = 3 ​ u − v 3 ​ u 2 ​ n 3 + O ⁡ ( n 2) 2n^{3}\int_{0}^{1/u}(1-vt)(1-ut)\,dt+O(n^{2})=\frac{3u-v}{3u^{2}}n^{3}+O(n^{2}) |  |

from the expansion over ℤ ⩾ 0 2 \mathbb{Z}_{\geqslant 0}^{2}, while the corner ( 0, 0) (0,0) contributes only n 2 ​ w u, v ​ ( 0, 0) = n 2 n^{2}w_{u,v}(0,0)=n^{2}. Therefore

 | G n ​ ( u, v) = n 4 ​ K ​ ( u, v) − 3 ​ u − v 6 ​ u 2 ​ n 3 + O ⁡ ( n 2), G_{n}(u,v)=n^{4}K(u,v)-\frac{3u-v}{6u^{2}}n^{3}+O(n^{2}), |  |

uniformly for u > v ⩾ 1 u>v\geqslant 1 and u, v ⩽ N u,v\leqslant N. Summing over primitive u > v u>v yields

 | S 1 ​ ( n) = 2 ​ n 4 ​ ∑ u ⩽ N k ⁡ ( u) − n 3 ​ ∑ u ⩽ N ∑ 1 ⩽ v < u ( u, v) = 1 3 ​ u − v 3 ​ u 2 + o ⁡ ( n 4). S_{1}(n)=2n^{4}\sum_{u\leqslant N}k(u)-n^{3}\sum_{u\leqslant N}\sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}\frac{3u-v}{3u^{2}}+o(n^{4}). |  |

Since #{ ( u, v): 1 ⩽ v < u ⩽ N, ( u, v) = 1 } = O ( N 2) = O ( n) \#\{(u,v):1\leqslant v<u\leqslant N,\ (u,v)=1\}=O(N^{2})=O(n), the accumulated O ⁡ ( n 2) O(n^{2}) error from the individual expansions is O ⁡ ( n 3) = o ⁡ ( n 4) O(n^{3})=o(n^{4}), which is absorbed into the remainder above. Since ∑ 1 ⩽ v < u ( u, v) = 1 v = u ​ φ ​ ( u) / 2 \sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}v=u\varphi(u)/2 for u > 1 u>1,

 | ∑ 1 ⩽ v < u ( u, v) = 1 3 ​ u − v 3 ​ u 2 = 5 6 ​ φ ⁡ ( u) u, \sum_{\begin{subarray}{c}1\leqslant v<u\\ (u,v)=1\end{subarray}}\frac{3u-v}{3u^{2}}=\frac{5}{6}\frac{\varphi(u)}{u}, |  |

so

 | S 1 ​ ( n) = 2 ​ n 4 ​ ∑ u ⩽ N k ⁡ ( u) − 5 6 ​ n 3 ​ ∑ u ⩽ N φ ⁡ ( u) u + o ⁡ ( n 4). S_{1}(n)=2n^{4}\sum_{u\leqslant N}k(u)-\frac{5}{6}n^{3}\sum_{u\leqslant N}\frac{\varphi(u)}{u}+o(n^{4}). |  |

The second sum is o ⁡ ( n 4) o(n^{4}) by Remark 28. Therefore Lemma 30 gives

 | 2 ​ n 4 ​ ∑ u ⩽ N k ⁡ ( u) = A 1 ​ n 4 ​ log ⁡ n + B 1 ​ n 4 + o ⁡ ( n 4), 2n^{4}\sum_{u\leqslant N}k(u)=A_{1}n^{4}\log n+B_{1}n^{4}+o(n^{4}), |  |

and the claimed asymptotic follows. ∎

### E.3 The contribution S 2 S_{2}

Throughout this subsection we write

 | M ( x):= ∑ d ⩽ x μ ( d), ε ( x):= exp ( − c ( log x) 3 / 5 ( log log x) − 1 / 5), M(x):=\sum_{d\leqslant x}\mu(d),\qquad\varepsilon(x):=\exp\!\Bigl(-c(\log x)^{3/5}(\log\log x)^{-1/5}\Bigr), |  |

where c > 0 c>0 is an absolute constant. By the classical Walfisz estimate for the Mertens function [5, Ch. I.4],

 | M ⁡ ( x) = O ⁡ ( x ​ ε ​ ( x)). M(x)=O\!\bigl(x\varepsilon(x)\bigr). |  |

###### Lemma 32 (summed second-order input for S 2 S_{2}).

Let N:= ⌊ n ⌋ N:=\lfloor\sqrt{n}\rfloor. For 1 ⩽ a, b ⩽ N 1\leqslant a,b\leqslant N, define

 | H n ​ ( a, b) \displaystyle H_{n}(a,b) | : = ∑ u > v ⩾ 1 ( u, v) = 1 a ​ u + b ​ v ⩽ n a ​ v + b ​ u ⩽ n ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u), \displaystyle:=\sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ au+bv\leqslant n\\ av+bu\leqslant n\end{subarray}}(n-au-bv)(n-av-bu), |  |

 | 𝒥 ⁡ ( a, b) \displaystyle\mathcal{J}(a,b) | : = ∬ x > y > 0 a ​ x + b ​ y ⩽ 1 a ​ y + b ​ x ⩽ 1 ( 1 − a ​ x − b ​ y) ​ ( 1 − a ​ y − b ​ x) ​ d x ​ d y. \displaystyle:=\iint_{\begin{subarray}{c}x>y>0\\ ax+by\leqslant 1\\ ay+bx\leqslant 1\end{subarray}}(1-ax-by)(1-ay-bx)\,dx\,dy. |  |

Then

 | ∑ 1 ⩽ a, b ⩽ N H n ​ ( a, b) = 6 π 2 ​ n 4 ​ ∑ 1 ⩽ a, b ⩽ N 𝒥 ⁡ ( a, b) + o ⁡ ( n 4). \sum_{1\leqslant a,b\leqslant N}H_{n}(a,b)=\frac{6}{\pi^{2}}n^{4}\sum_{1\leqslant a,b\leqslant N}\mathcal{J}(a,b)+o(n^{4}). |  |

###### Proof.

For t ⩾ a + b t\geqslant a+b, let

 | F t ​ ( a, b):= ∑ u > v ⩾ 1 a ​ u + b ​ v ⩽ t a ​ v + b ​ u ⩽ t ( t − a ​ u − b ​ v) ​ ( t − a ​ v − b ​ u), F_{t}(a,b):=\sum_{\begin{subarray}{c}u>v\geqslant 1\\ au+bv\leqslant t\\ av+bu\leqslant t\end{subarray}}(t-au-bv)(t-av-bu), |  |

where the sum is over all u > v ⩾ 1 u>v\geqslant 1, without the coprimality condition. For each pair ( a, b) (a,b), define

 | X a, b:= ⌊ n a + b ⌋. X_{a,b}:=\Bigl\lfloor\frac{n}{a+b}\Bigr\rfloor. |  |

Then Möbius inversion gives

 | H n ​ ( a, b) = ∑ d ⩽ X a, b μ ⁡ ( d) ​ d 2 ​ F n / d ​ ( a, b). H_{n}(a,b)=\sum_{d\leqslant X_{a,b}}\mu(d)d^{2}F_{n/d}(a,b). |  |

Put m:= max ⁡ ( a, b) m:=\max(a,b), p:= a / m p:=a/m, q:= b / m q:=b/m, and τ:= t / m \tau:=t/m. Then ( p, q) (p,q) ranges over the compact set

 | Θ:= { ( p, q) ∈ [0, 1] 2: max ⁡ ( p, q) = 1 }, \Theta:=\{(p,q)\in[0,1]^{2}:\max(p,q)=1\}, |  |

and

 | Ω p, q \displaystyle\Omega_{p,q} | : = { ( x, y): x > y > 0, p x + q y ⩽ 1, q x + p y ⩽ 1 }, \displaystyle:=\{(x,y):x>y>0,\ px+qy\leqslant 1,\ qx+py\leqslant 1\}, |  |

 | w p, q ​ ( x, y) \displaystyle w_{p,q}(x,y) | : = ( 1 − p ​ x − q ​ y) ​ ( 1 − q ​ x − p ​ y). \displaystyle:=(1-px-qy)(1-qx-py). |  |

give the rescaled representation

 | F t ​ ( a, b) = t 2 ​ ∑ ( u, v) ∈ τ ​ Ω p, q ∩ ℤ 2 w p, q ​ ( u / τ, v / τ). F_{t}(a,b)=t^{2}\sum_{(u,v)\in\tau\Omega_{p,q}\cap\mathbb{Z}^{2}}w_{p,q}(u/\tau,v/\tau). |  |

The family ( Ω p, q, w p, q) ( p, q) ∈ Θ (\Omega_{p,q},w_{p,q})_{(p,q)\in\Theta} is compact and piecewise- C 2 C^{2}. Let

 | Ω ¯ p, q:= { ( x, y): x ⩾ y ⩾ 0, p x + q y ⩽ 1, q x + p y ⩽ 1 }. \overline{\Omega}_{p,q}:=\{(x,y):x\geqslant y\geqslant 0,\ px+qy\leqslant 1,\ qx+py\leqslant 1\}. |  |

Passing from the open wedge x > y > 0 x>y>0 to the closed wedge x ⩾ y ⩾ 0 x\geqslant y\geqslant 0 adds only points on the diagonal and coordinate axes. For each fixed ( p, q) (p,q), these boundary slices contain O ⁡ ( τ) O(\tau) lattice points and the weight is uniformly bounded, so the resulting correction to F t ​ ( a, b) F_{t}(a,b) is t 2 ⋅ O ⁡ ( τ) = O ⁡ ( t 3 / m) = O ⁡ ( t 3) t^{2}\cdot O(\tau)=O(t^{3}/m)=O(t^{3}), which is harmless for the final summation. Thus we may invoke Euler–Maclaurin on Ω ¯ p, q \overline{\Omega}_{p,q}. Away from the endpoint ( p, q) = ( 1, 1) (p,q)=(1,1) the combinatorial type is constant on each branch of Θ \Theta, so Remark 27 applies directly there. At ( p, q) = ( 1, 1) (p,q)=(1,1) the quadrilateral degenerates continuously to the limiting triangle. This causes no problem for the coefficient bounds used below: the two oblique sides satisfy w p, q = 0 w_{p,q}=0 identically, while the remaining boundary pieces lie on x = y x=y and on the coordinate axes; along these edges both the edge lengths and the restricted weights stay uniformly bounded as ( p, q) → ( 1, 1) (p,q)\to(1,1). Hence the area coefficient extends continuously and remains uniformly bounded on all of Θ \Theta; since only this coefficient is used below, Remark 27 gives, uniformly in ( p, q) ∈ Θ (p,q)\in\Theta and τ ⩾ 1 \tau\geqslant 1,

 | ∑ ( u, v) ∈ τ ​ Ω ¯ p, q ∩ ℤ 2 w p, q ​ ( u / τ, v / τ) = τ 2 ​ A ​ ( p, q) + O ⁡ ( τ), \sum_{(u,v)\in\tau\overline{\Omega}_{p,q}\cap\mathbb{Z}^{2}}w_{p,q}(u/\tau,v/\tau)=\tau^{2}A(p,q)+O(\tau), |  |

with implied constants independent of ( p, q) (p,q) and τ \tau. Therefore

 | F t ​ ( a, b) = t 4 ​ 𝒥 ​ ( a, b) + O ⁡ ( t 3 max ⁡ ( a, b)) + O ⁡ ( t 2), F_{t}(a,b)=t^{4}\mathcal{J}(a,b)+O\!\left(\frac{t^{3}}{\max(a,b)}\right)+O(t^{2}), |  |

where 𝒥 ⁡ ( a, b) = A ⁡ ( p, q) / m 2 \mathcal{J}(a,b)=A(p,q)/m^{2}, uniformly for 1 ⩽ a, b ⩽ N 1\leqslant a,b\leqslant N and t ⩾ a + b t\geqslant a+b. Substituting this expansion into the Möbius formula and using

 | ∑ d ⩽ x μ ⁡ ( d) d = O ⁡ ( ε ⁡ ( x)), ∑ d ⩽ x μ ⁡ ( d) d 2 = 1 ζ ⁡ ( 2) + O ⁡ ( ε ⁡ ( x) x), M ⁡ ( x) = ∑ d ⩽ x μ ⁡ ( d) = O ⁡ ( x ​ ε ​ ( x)), \sum_{d\leqslant x}\frac{\mu(d)}{d}=O\!\bigl(\varepsilon(x)\bigr),\qquad\sum_{d\leqslant x}\frac{\mu(d)}{d^{2}}=\frac{1}{\zeta(2)}+O\!\left(\frac{\varepsilon(x)}{x}\right),\qquad M(x)=\sum_{d\leqslant x}\mu(d)=O\!\bigl(x\varepsilon(x)\bigr), |  |

we obtain

 | H n ​ ( a, b) = 6 π 2 ​ n 4 ​ 𝒥 ​ ( a, b) + O ⁡ ( ε n ​ n 4 ​ 𝒥 ​ ( a, b) X a, b) + O ⁡ ( ε n ​ n 3 ​ 1 max ⁡ ( a, b)) + O ⁡ ( n 2 ​ | M ⁡ ( X a, b) |), H_{n}(a,b)=\frac{6}{\pi^{2}}n^{4}\mathcal{J}(a,b)+O\!\left(\varepsilon_{n}\frac{n^{4}\mathcal{J}(a,b)}{X_{a,b}}\right)+O\!\left(\varepsilon_{n}n^{3}\frac{1}{\max(a,b)}\right)+O\!\left(n^{2}\bigl|M(X_{a,b})\bigr|\right), |  |

where ε n:= ε ⁡ ( n / 2) \varepsilon_{n}:=\varepsilon(\sqrt{n}/2) and we used X a, b ⩾ 1 2 ​ n X_{a,b}\geqslant\frac{1}{2}\sqrt{n} for a, b ⩽ N = ⌊ n ⌋ a,b\leqslant N=\lfloor\sqrt{n}\rfloor. Since X a, b = ⌊ n / ( a + b) ⌋ X_{a,b}=\lfloor n/(a+b)\rfloor, one has for all sufficiently large n n,

 | n 2 ​ ( a + b) ⩽ X a, b ⩽ n a + b. \frac{n}{2(a+b)}\leqslant X_{a,b}\leqslant\frac{n}{a+b}. |  |

Moreover 𝒥 ⁡ ( a, b) = 1 2 ​ K ​ ( max ⁡ ( a, b), min ⁡ ( a, b)) \mathcal{J}(a,b)=\frac{1}{2}K(\max(a,b),\min(a,b)), so Lemma 25 implies

 | ∑ a, b ⩽ N ( a + b) ​ 𝒥 ​ ( a, b) = O ⁡ ( N). \sum_{a,b\leqslant N}(a+b)\mathcal{J}(a,b)=O(N). |  |

Also,

 | ∑ a, b ⩽ N 1 max ⁡ ( a, b) ⩽ C 2 ​ ∑ m ⩽ N 2 ​ m − 1 m = O ⁡ ( N). \sum_{a,b\leqslant N}\frac{1}{\max(a,b)}\leqslant C_{2}\sum_{m\leqslant N}\frac{2m-1}{m}=O(N). |  |

Using again M ⁡ ( X a, b) = O ⁡ ( X a, b ​ ε n) M(X_{a,b})=O(X_{a,b}\varepsilon_{n}) uniformly in a, b a,b, we obtain

 | ∑ a, b ⩽ N ε n ​ n 4 ​ 𝒥 ​ ( a, b) X a, b = O ⁡ ( ε n ​ n 3 ​ N), ∑ a, b ⩽ N ε n ​ n 3 ​ 1 max ⁡ ( a, b) = O ⁡ ( ε n ​ n 3 ​ N), \sum_{a,b\leqslant N}\varepsilon_{n}\frac{n^{4}\mathcal{J}(a,b)}{X_{a,b}}=O(\varepsilon_{n}n^{3}N),\qquad\sum_{a,b\leqslant N}\varepsilon_{n}n^{3}\frac{1}{\max(a,b)}=O(\varepsilon_{n}n^{3}N), |  |

and

 | ∑ a, b ⩽ N n 2 ​ | M ⁡ ( X a, b) | ⩽ C 4 ​ ε n ​ n 2 ​ ∑ a, b ⩽ N X a, b ⩽ C 5 ​ ε n ​ n 3 ​ ∑ a, b ⩽ N 1 a + b = O ⁡ ( ε n ​ n 3 ​ N) = o ⁡ ( n 4). \sum_{a,b\leqslant N}n^{2}\bigl|M(X_{a,b})\bigr|\leqslant C_{4}\varepsilon_{n}n^{2}\sum_{a,b\leqslant N}X_{a,b}\leqslant C_{5}\varepsilon_{n}n^{3}\sum_{a,b\leqslant N}\frac{1}{a+b}=O(\varepsilon_{n}n^{3}N)=o(n^{4}). |  |

Since N = ⌊ n ⌋ N=\lfloor\sqrt{n}\rfloor, we have n 3 ​ N = n 7 / 2 = o ⁡ ( n 4) n^{3}N=n^{7/2}=o(n^{4}), and since ε n → 0 \varepsilon_{n}\to 0, the first two displayed sums are also o ⁡ ( n 4) o(n^{4}). This proves the claim. ∎

###### Theorem 33 (asymptotic for S 2 S_{2}).

One has

 | S 2 ​ ( n) = A 2 ​ n 4 ​ log ⁡ n + B 2 ​ n 4 + o ⁡ ( n 4), S_{2}(n)=A_{2}n^{4}\log n+B_{2}n^{4}+o(n^{4}), |  |

where A 2 = 4 ​ log ⁡ 2 − 1 2 ​ π 2 A_{2}=\frac{4\log 2-1}{2\pi^{2}} and B 2 = ( 4 ​ log ⁡ 2 − 1) ​ γ + 4 ​ log 2 ​ 2 π 2 − 5 12 B_{2}=\frac{(4\log 2-1)\gamma+4\log^{2}2}{\pi^{2}}-\frac{5}{12}.

###### Proof.

By definition,

 | S 2 ​ ( n) = 2 ​ ∑ 1 ⩽ a, b ⩽ N H n ​ ( a, b), N:= ⌊ n ⌋. S_{2}(n)=2\sum_{1\leqslant a,b\leqslant N}H_{n}(a,b),\qquad N:=\lfloor\sqrt{n}\rfloor. |  |

By Lemma 32,

 | S 2 ​ ( n) = 12 π 2 ​ n 4 ​ ∑ 1 ⩽ a, b ⩽ N 𝒥 ⁡ ( a, b) + o ⁡ ( n 4). S_{2}(n)=\frac{12}{\pi^{2}}n^{4}\sum_{1\leqslant a,b\leqslant N}\mathcal{J}(a,b)+o(n^{4}). |  |

Since 𝒥 ⁡ ( a, b) = 1 2 ​ K ​ ( max ⁡ ( a, b), min ⁡ ( a, b)) \mathcal{J}(a,b)=\frac{1}{2}K(\max(a,b),\min(a,b)), we have

 | ∑ 1 ⩽ a, b ⩽ N 𝒥 ⁡ ( a, b) = ∑ u ⩽ N ∑ v < u K ⁡ ( u, v) + 1 2 ​ ∑ u ⩽ N K ⁡ ( u, u). \sum_{1\leqslant a,b\leqslant N}\mathcal{J}(a,b)=\sum_{u\leqslant N}\sum_{v<u}K(u,v)+\frac{1}{2}\sum_{u\leqslant N}K(u,u). |  |

A direct summation using Lemma 25 gives

 | ∑ v = 1 u − 1 K ⁡ ( u, v) = H 2 ​ u − 1 − H u 3 ​ u − u − 1 12 ​ u 2, K ⁡ ( u, u) = 1 12 ​ u 2. \sum_{v=1}^{u-1}K(u,v)=\frac{H_{2u-1}-H_{u}}{3u}-\frac{u-1}{12u^{2}},\qquad K(u,u)=\frac{1}{12u^{2}}. |  |

Summing over u ⩽ N u\leqslant N, using Lemma 26, and also

 | ∑ u ⩽ N 1 u 2 = π 2 6 − 1 N + O ⁡ ( N − 2), \sum_{u\leqslant N}\frac{1}{u^{2}}=\frac{\pi^{2}}{6}-\frac{1}{N}+O(N^{-2}), |  |

one obtains

 | ∑ u ⩽ N ∑ v < u K ⁡ ( u, v) + 1 2 ​ ∑ u ⩽ N K ⁡ ( u, u) = 4 ​ log ⁡ 2 − 1 12 ​ log ⁡ N + C 0 + o ⁡ ( 1), \sum_{u\leqslant N}\sum_{v<u}K(u,v)+\frac{1}{2}\sum_{u\leqslant N}K(u,u)=\frac{4\log 2-1}{12}\log N+C_{0}+o(1), |  |

where C 0 = 4 ​ log ⁡ 2 − 1 12 ​ γ + log 2 ⁡ 2 3 − 5 ​ π 2 144 C_{0}=\frac{4\log 2-1}{12}\gamma+\frac{\log^{2}2}{3}-\frac{5\pi^{2}}{144}. Multiplying by ( 12 / π 2) ​ n 4 (12/\pi^{2})n^{4} yields

 | S 2 ​ ( n) = 4 ​ log ⁡ 2 − 1 π 2 ​ n 4 ​ log ⁡ N + 12 ​ C 0 π 2 ​ n 4 + o ⁡ ( n 4). S_{2}(n)=\frac{4\log 2-1}{\pi^{2}}n^{4}\log N+\frac{12C_{0}}{\pi^{2}}n^{4}+o(n^{4}). |  |

Since N = ⌊ n ⌋ N=\lfloor\sqrt{n}\rfloor, one has N / n → 1 N/\sqrt{n}\to 1, hence

 | log ⁡ N = 1 2 ​ log ⁡ n + o ⁡ ( 1). \log N=\frac{1}{2}\log n+o(1). |  |

Therefore

 | S 2 ​ ( n) = A 2 ​ n 4 ​ log ⁡ n + B 2 ​ n 4 + o ⁡ ( n 4), S_{2}(n)=A_{2}n^{4}\log n+B_{2}n^{4}+o(n^{4}), |  |

with B 2 = 12 ​ C 0 / π 2 = ( 4 ​ log ⁡ 2 − 1) ​ γ + 4 ​ log 2 ​ 2 π 2 − 5 12 B_{2}=12C_{0}/\pi^{2}=\frac{(4\log 2-1)\gamma+4\log^{2}2}{\pi^{2}}-\frac{5}{12}. ∎

### E.4 The contribution S 12 S_{12}

###### Lemma 34 (weighted primitive points).

Let

 | T:= { ( x, y) ∈ ℝ 2: 0 ⩽ y ⩽ x ⩽ 1 }. T:=\{(x,y)\in\mathbb{R}^{2}:0\leqslant y\leqslant x\leqslant 1\}. |  |

Assume that g g is continuous on T T, globally Lipschitz on T T, and that there is a finite partition of T T into polygons with piecewise C 2 C^{2} boundaries such that g g is C 2 C^{2} on each cell and its first derivatives are uniformly bounded there. Then

 | ∑ u > v ⩾ 1 ( u, v) = 1 u, v ⩽ N g ⁡ ( u N, v N) = 6 π 2 ​ N 2 ​ ∬ T g ⁡ ( x, y) ​ 𝑑 x ​ 𝑑 y + O g ​ ( N ​ log ​ N). \sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ u,v\leqslant N\end{subarray}}g\!\left(\frac{u}{N},\frac{v}{N}\right)=\frac{6}{\pi^{2}}N^{2}\iint_{T}g(x,y)\,dx\,dy+O_{g}(N\log N). |  |

###### Proof.

By Möbius inversion,

 | ∑ u > v ⩾ 1 ( u, v) = 1 u, v ⩽ N g ⁡ ( u N, v N) = ∑ d ⩽ N μ ⁡ ( d) ​ ∑ m > n ⩾ 1 m, n ⩽ N / d g ⁡ ( d ​ m N, d ​ n N). \sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ u,v\leqslant N\end{subarray}}g\!\left(\frac{u}{N},\frac{v}{N}\right)=\sum_{d\leqslant N}\mu(d)\sum_{\begin{subarray}{c}m>n\geqslant 1\\ m,n\leqslant N/d\end{subarray}}g\!\left(\frac{dm}{N},\frac{dn}{N}\right). |  |

Let M:= N / d M:=N/d and M d:= ⌊ M ⌋ M_{d}:=\lfloor M\rfloor. Then the inner sum is

 | ∑ m > n ⩾ 1 m, n ⩽ M d g ⁡ ( m M, n M). \sum_{\begin{subarray}{c}m>n\geqslant 1\\ m,n\leqslant M_{d}\end{subarray}}g\!\left(\frac{m}{M},\frac{n}{M}\right). |  |

Replacing the cutoff M d M_{d} by M M changes the summation region only in a boundary strip containing O ⁡ ( M) O(M) lattice points, hence contributes O g ​ ( M) O_{g}(M). On the common part, the Lipschitz estimate and | M − 1 − M d − 1 | = O ⁡ ( M − 2) |M^{-1}-M_{d}^{-1}|=O(M^{-2}) give

 | | g ⁡ ( m M, n M) − g ⁡ ( m M d, n M d) | = O g ​ ( M − 1) \left|g\!\left(\frac{m}{M},\frac{n}{M}\right)-g\!\left(\frac{m}{M_{d}},\frac{n}{M_{d}}\right)\right|=O_{g}(M^{-1}) |  |

for each lattice point, hence another total O g ​ ( M) O_{g}(M). Therefore the inner sum differs by at most O g ​ ( M) O_{g}(M) from

 | ∑ m > n ⩾ 1 m, n ⩽ M d g ⁡ ( m M d, n M d). \sum_{\begin{subarray}{c}m>n\geqslant 1\\ m,n\leqslant M_{d}\end{subarray}}g\!\left(\frac{m}{M_{d}},\frac{n}{M_{d}}\right). |  |

Applying the weighted polygonal Euler–Maclaurin expansion separately on the finitely many cells of the partition of the closed triangle T T yields

 | ∑ m > n ⩾ 1 m, n ⩽ M d g ⁡ ( m M d, n M d) = A g ​ M d 2 + O g ​ ( M d), A g:= ∬ T g ⁡ ( x, y) ​ 𝑑 x ​ 𝑑 y, \sum_{\begin{subarray}{c}m>n\geqslant 1\\ m,n\leqslant M_{d}\end{subarray}}g\!\left(\frac{m}{M_{d}},\frac{n}{M_{d}}\right)=A_{g}M_{d}^{2}+O_{g}(M_{d}),\qquad A_{g}:=\iint_{T}g(x,y)\,dx\,dy, |  |

uniformly in M d ⩾ 1 M_{d}\geqslant 1. Since M d = M + O ⁡ ( 1) M_{d}=M+O(1), this becomes

 | ∑ m > n ⩾ 1 m, n ⩽ M d g ⁡ ( m M, n M) = A g ​ M 2 + O g ​ ( M). \sum_{\begin{subarray}{c}m>n\geqslant 1\\ m,n\leqslant M_{d}\end{subarray}}g\!\left(\frac{m}{M},\frac{n}{M}\right)=A_{g}M^{2}+O_{g}(M). |  |

Hence

 | ∑ u > v ⩾ 1 ( u, v) = 1 u, v ⩽ N g ⁡ ( u N, v N) = N 2 ​ A g ​ ∑ d ⩽ N μ ⁡ ( d) d 2 + O g ​ ( N ​ ∑ d ⩽ N | μ ⁡ ( d) | d). \sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ u,v\leqslant N\end{subarray}}g\!\left(\frac{u}{N},\frac{v}{N}\right)=N^{2}A_{g}\sum_{d\leqslant N}\frac{\mu(d)}{d^{2}}+O_{g}\!\left(N\sum_{d\leqslant N}\frac{|\mu(d)|}{d}\right). |  |

Using

 | ∑ d ⩽ N μ ⁡ ( d) d 2 = 1 ζ ⁡ ( 2) + O ⁡ ( 1 N), ∑ d ⩽ N | μ ⁡ ( d) | d = O ⁡ ( log ⁡ N), \sum_{d\leqslant N}\frac{\mu(d)}{d^{2}}=\frac{1}{\zeta(2)}+O\!\left(\frac{1}{N}\right),\qquad\sum_{d\leqslant N}\frac{|\mu(d)|}{d}=O(\log N), |  |

where the second bound is only the standard squarefree-indicator estimate, we obtain the claim. In particular, the N ​ log ⁡ N N\log N remainder comes exactly from the factor N ​ ∑ d ⩽ N | μ ⁡ ( d) | / d N\sum_{d\leqslant N}|\mu(d)|/d. ∎

###### Theorem 35 (asymptotic for S 12 S_{12}).

One has

 | S 12 ​ ( n) = B 12 ​ n 4 + o ⁡ ( n 4), S_{12}(n)=B_{12}n^{4}+o(n^{4}), |  |

where B 12 = − 1 3 + 2 ​ log 2 ​ 2 π 2 + 19 ​ log ⁡ 2 3 ​ π 2 − 1 12 ​ π 2 B_{12}=-\frac{1}{3}+\frac{2\log^{2}2}{\pi^{2}}+\frac{19\log 2}{3\pi^{2}}-\frac{1}{12\pi^{2}}.

###### Proof.

Let N:= ⌊ n ⌋ N:=\lfloor\sqrt{n}\rfloor and put x:= u / N x:=u/N, y:= v / N y:=v/N. For primitive u > v u>v with u, v ⩽ N u,v\leqslant N, write

 | Q N ​ ( u, v):= ∑ 1 ⩽ a, b ⩽ N a ​ u + b ​ v ⩽ n a ​ v + b ​ u ⩽ n ( n − a ​ u − b ​ v) ​ ( n − a ​ v − b ​ u). Q_{N}(u,v):=\sum_{\begin{subarray}{c}1\leqslant a,b\leqslant N\\ au+bv\leqslant n\\ av+bu\leqslant n\end{subarray}}(n-au-bv)(n-av-bu). |  |

After the scaling a = N ​ α a=N\alpha and b = N ​ β b=N\beta, the admissible region becomes

 | D x, y:= [0, 1] 2 ∩ { x α + y β ⩽ 1 } ∩ { y α + x β ⩽ 1 }. D_{x,y}:=[0,1]^{2}\cap\{x\alpha+y\beta\leqslant 1\}\cap\{y\alpha+x\beta\leqslant 1\}. |  |

Therefore, with ρ n:= n / N 2 \rho_{n}:=n/N^{2}, one has

 | Q N ​ ( u, v) = N 4 ​ ∑ ( α, β) ∈ D x, y ( ρ n) ∩ ( N − 1 ​ ℤ) 2 ( ρ n − x ​ α − y ​ β) ​ ( ρ n − y ​ α − x ​ β), Q_{N}(u,v)=N^{4}\sum_{(\alpha,\beta)\in D_{x,y}^{(\rho_{n})}\cap(N^{-1}\mathbb{Z})^{2}}(\rho_{n}-x\alpha-y\beta)(\rho_{n}-y\alpha-x\beta), |  |

where

 | D x, y ( ρ):= [0, 1] 2 ∩ { x α + y β ⩽ ρ } ∩ { y α + x β ⩽ ρ }. D_{x,y}^{(\rho)}:=[0,1]^{2}\cap\{x\alpha+y\beta\leqslant\rho\}\cap\{y\alpha+x\beta\leqslant\rho\}. |  |

By Remark 28, ρ n = 1 + o ⁡ ( 1) \rho_{n}=1+o(1). Write

 | T 0:= T ∩ { x + y ⩽ 1 }, T 1:= T ∩ { x + y ⩾ 1 }. T_{0}:=T\cap\{x+y\leqslant 1\},\qquad T_{1}:=T\cap\{x+y\geqslant 1\}. |  |

On the relative interiors of T 0 T_{0} and T 1 T_{1}, and for ρ \rho in a neighborhood of 1 1, the family ( D x, y ( ρ), ( ρ − x ​ α − y ​ β) ​ ( ρ − y ​ α − x ​ β)) (D_{x,y}^{(\rho)},(\rho-x\alpha-y\beta)(\rho-y\alpha-x\beta)) has fixed combinatorial type and depends piecewise- C 2 C^{2} on ( x, y, ρ) (x,y,\rho) with uniform bounds. Hence Remark 27 applies separately on each relative interior cell and gives there the uniform area-term expansion

 | Q N ​ ( u, v) = N 6 ​ I ρ n ​ ( x, y) + O ⁡ ( N 5), Q_{N}(u,v)=N^{6}I_{\rho_{n}}(x,y)+O(N^{5}), |  |

where

 | I ρ ​ ( x, y):= ∬ D x, y ( ρ) ( ρ − x ​ α − y ​ β) ​ ( ρ − y ​ α − x ​ β) ​ 𝑑 α ​ 𝑑 β. I_{\rho}(x,y):=\iint_{D_{x,y}^{(\rho)}}(\rho-x\alpha-y\beta)(\rho-y\alpha-x\beta)\,d\alpha\,d\beta. |  |

Along the interface x + y = 1 x+y=1 the combinatorial type changes, but the domains vary continuously, and the only edges that appear or disappear are the oblique edges on which the weight vanishes identically. Hence the area coefficient matches continuously across the interface and remains uniformly bounded there, so the same expansion holds uniformly for all ( x, y) ∈ T (x,y)\in T and ρ \rho near 1 1. Since the family is piecewise C 1 C^{1} in ρ \rho near 1 1, uniformly in ( x, y) (x,y) one has

 | I ρ n ​ ( x, y) = I ⁡ ( x, y) + O ⁡ ( | ρ n − 1 |), I:= I 1. I_{\rho_{n}}(x,y)=I(x,y)+O(|\rho_{n}-1|),\qquad I:=I_{1}. |  |

The resulting change in the main contribution to S 12 ​ ( n) S_{12}(n) is bounded by

 | N 6 ⋅ O ( | ρ n − 1 |) ⋅ #{ ( u, v): u > v ⩾ 1, u, v ⩽ N, ( u, v) = 1 } = O ( N 8 | ρ n − 1 |) = o ( n 4), N^{6}\cdot O(|\rho_{n}-1|)\cdot\#\{(u,v):u>v\geqslant 1,\ u,v\leqslant N,\ (u,v)=1\}=O(N^{8}|\rho_{n}-1|)=o(n^{4}), |  |

because #{ ( u, v): u > v ⩾ 1, u, v ⩽ N, ( u, v) = 1 } = O ( N 2) \#\{(u,v):u>v\geqslant 1,\ u,v\leqslant N,\ (u,v)=1\}=O(N^{2}), N 8 = n 4 + o ⁡ ( n 4) N^{8}=n^{4}+o(n^{4}), and ρ n − 1 = o ⁡ ( 1) \rho_{n}-1=o(1). Thus it is enough to work with ρ = 1 \rho=1, that is, with

 | D x, y = D x, y ( 1) = [0, 1] 2 ∩ { x α + y β ⩽ 1 } ∩ { y α + x β ⩽ 1 }. D_{x,y}=D_{x,y}^{(1)}=[0,1]^{2}\cap\{x\alpha+y\beta\leqslant 1\}\cap\{y\alpha+x\beta\leqslant 1\}. |  |

Thus I I is continuous on T T. On the relative interiors of T 0 T_{0} and T 1 T_{1}, I I is piecewise C 1 C^{1} with bounded first derivatives, as follows from the explicit formulas below; hence I I is globally Lipschitz on T T and satisfies the assumptions of Lemma 34. Applying Lemma 34 to I I gives

 | N 6 ​ ∑ u > v ⩾ 1 ( u, v) = 1 u, v ⩽ N I ⁡ ( u N, v N) = 12 π 2 ​ N 8 ​ ∬ T I ⁡ ( x, y) ​ 𝑑 x ​ 𝑑 y + O ⁡ ( N 7 ​ log ​ N). N^{6}\sum_{\begin{subarray}{c}u>v\geqslant 1\\ (u,v)=1\\ u,v\leqslant N\end{subarray}}I\!\left(\frac{u}{N},\frac{v}{N}\right)=\frac{12}{\pi^{2}}N^{8}\iint_{T}I(x,y)\,dx\,dy+O(N^{7}\log N). |  |

The uniform O ⁡ ( N 5) O(N^{5}) remainder contributes at most

 | O ( N 5) ⋅ #{ ( u, v): u > v ⩾ 1, u, v ⩽ N, ( u, v) = 1 } = O ( N 7) = o ( n 4). O(N^{5})\cdot\#\{(u,v):u>v\geqslant 1,\ u,v\leqslant N,\ (u,v)=1\}=O(N^{7})=o(n^{4}). |  |

Therefore

 | S 12 ​ ( n) = 12 π 2 ​ N 8 ​ ∬ T I ⁡ ( x, y) ​ 𝑑 x ​ 𝑑 y + O ⁡ ( N 7 ​ log ⁡ N). S_{12}(n)=\frac{12}{\pi^{2}}N^{8}\iint_{T}I(x,y)\,dx\,dy+O(N^{7}\log N). |  |

To evaluate the bulk integral, split T T into the two regions T 0:= T ∩ { x + y ⩽ 1 } T_{0}:=T\cap\{x+y\leqslant 1\} and T 1:= T ∩ { x + y > 1 } T_{1}:=T\cap\{x+y>1\}. On T 0 T_{0} one has D x, y = [0, 1] 2 D_{x,y}=[0,1]^{2}, hence

 | I ⁡ ( x, y) = ∫ 0 1 ∫ 0 1 ( 1 − x ​ α − y ​ β) ​ ( 1 − y ​ α − x ​ β) ​ 𝑑 α ​ 𝑑 β = 1 − x − y + x 2 + y 2 4 + 2 ​ x ​ y 3. I(x,y)=\int_{0}^{1}\!\!\int_{0}^{1}(1-x\alpha-y\beta)(1-y\alpha-x\beta)\,d\alpha\,d\beta=1-x-y+\frac{x^{2}+y^{2}}{4}+\frac{2xy}{3}. |  |

On T 1 T_{1}, with

 | W x, y ​ ( α, β):= ( 1 − x ​ α − y ​ β) ​ ( 1 − y ​ α − x ​ β), W_{x,y}(\alpha,\beta):=(1-x\alpha-y\beta)(1-y\alpha-x\beta), |  |

and

 | β 1 ​ ( α):= 1 − x ​ α y, β 2 ​ ( α):= 1 − y ​ α x, \beta_{1}(\alpha):=\frac{1-x\alpha}{y},\qquad\beta_{2}(\alpha):=\frac{1-y\alpha}{x}, |  |

one has

 | I ⁡ ( x, y) = \displaystyle I(x,y)={} | ∫ 0 1 − x y ∫ 0 1 W x, y ​ ( α, β) ​ 𝑑 β ​ 𝑑 α \displaystyle\int_{0}^{\frac{1-x}{y}}\!\int_{0}^{1}W_{x,y}(\alpha,\beta)\,d\beta\,d\alpha |  |

 |  | + ∫ 1 − x y 1 − y x ∫ 0 β 1 ​ ( α) W x, y ( α, β) d β d α \displaystyle+\int_{\frac{1-x}{y}}^{\frac{1-y}{x}}\!\int_{0}^{\beta_{1}(\alpha)}W_{x,y}(\alpha,\beta)\,d\beta\,d\alpha |  |

 |  | + ∫ 1 − y x 1 ∫ 0 β 2 ​ ( α) W x, y ( α, β) d β d α, \displaystyle+\int_{\frac{1-y}{x}}^{1}\!\int_{0}^{\beta_{2}(\alpha)}W_{x,y}(\alpha,\beta)\,d\beta\,d\alpha, |  |

and evaluating these elementary integrals gives

 | I ⁡ ( x, y) = \displaystyle I(x,y)={} | 1 − x − y + x 2 + y 2 4 + 2 ​ x ​ y 3 \displaystyle 1-x-y+\frac{x^{2}+y^{2}}{4}+\frac{2xy}{3} |  |

 |  | − ( x + y − 1) 4 24 ​ x 6 ​ y 6 ​ ( x 10 − 4 ​ x 9 ​ y + 7 ​ x 8 ​ y 2 − 8 ​ x 7 ​ y 3 + 7 ​ x 6 ​ y 4 − 4 ​ x 5 ​ y 5 CLOSE \displaystyle-\frac{(x+y-1)^{4}}{24x^{6}y^{6}}\,\Bigl(x^{10}-4x^{9}y+7x^{8}y^{2}-8x^{7}y^{3}+7x^{6}y^{4}-4x^{5}y^{5} |  |

 |  | OPEN + 7 ​ x 4 ​ y 6 − 8 ​ x 3 ​ y 7 + 7 ​ x 2 ​ y 8 − 4 ​ x ​ y 9 + y 10). \displaystyle}{\displaystyle+7x^{4}y^{6}-8x^{3}y^{7}+7x^{2}y^{8}-4xy^{9}+y^{10}\Bigr). |  |

The two formulas agree continuously along x + y = 1 x+y=1, so I I is continuous on T T. Integrating them over T 0 T_{0} and T 1 T_{1} gives

 | ∬ T I ⁡ ( x, y) ​ 𝑑 x ​ 𝑑 y = − 1 144 − π 2 36 + log 2 ⁡ 2 6 + 19 ​ log ⁡ 2 36. \iint_{T}I(x,y)\,dx\,dy=-\frac{1}{144}-\frac{\pi^{2}}{36}+\frac{\log^{2}2}{6}+\frac{19\log 2}{36}. |  |

Thus 12 π 2 ​ ∬ T I = B 12 \frac{12}{\pi^{2}}\iint_{T}I=B_{12}. Since N = ⌊ n ⌋ N=\lfloor\sqrt{n}\rfloor, Remark 28 gives N 8 = n 4 + o ⁡ ( n 4) N^{8}=n^{4}+o(n^{4}) and N 7 ​ log ⁡ N = o ⁡ ( n 4) N^{7}\log N=o(n^{4}). Therefore

 | S 12 ​ ( n) = B 12 ​ n 4 + o ⁡ ( n 4), S_{12}(n)=B_{12}n^{4}+o(n^{4}), |  |

as claimed. ∎

### E.5 Assembly

###### Lemma 36 (covering identity).

For every admissible quadruple ( u, v, a, b) (u,v,a,b) with u > v ⩾ 1 u>v\geqslant 1, ( u, v) = 1 (u,v)=1, a, b ⩾ 1 a,b\geqslant 1, a ​ u + b ​ v ⩽ n au+bv\leqslant n, and a ​ v + b ​ u ⩽ n av+bu\leqslant n, one has either u, v ⩽ n u,v\leqslant\sqrt{n} or a, b ⩽ n a,b\leqslant\sqrt{n}. Consequently,

 | F ⁡ ( n) = S 1 ​ ( n) + S 2 ​ ( n) − S 12 ​ ( n) + F 0 ​ ( n). F(n)=S_{1}(n)+S_{2}(n)-S_{12}(n)+F_{0}(n). |  |

Here F 0 ​ ( n) F_{0}(n) is exactly the exceptional contribution of the three directions ( 1, 0) (1,0), ( 0, 1) (0,1), and ( 1, 1) (1,1) that were removed from the primitive summations at the start of the appendix.

###### Proof.

If u > n u>\sqrt{n}, then a ​ u < n au<n and b ​ u < n bu<n, hence a, b < n / u < n a,b<n/u<\sqrt{n}. Thus every admissible quadruple lies in { u, v ⩽ n } ∪ { a, b ⩽ n } \{u,v\leqslant\sqrt{n}\}\cup\{a,b\leqslant\sqrt{n}\}, and the formula for F ⁡ ( n) F(n) follows by inclusion–exclusion. ∎

###### Theorem 37 (assembly of the two-term asymptotic).

One has

 | F ⁡ ( n) = A ​ n 4 ​ log ⁡ n + B ​ n 4 + o ⁡ ( n 4), F(n)=A\,n^{4}\log n+B\,n^{4}+o(n^{4}), |  |

where

 | A = 4 ​ log ⁡ 2 − 1 π 2 A=\frac{4\log 2-1}{\pi^{2}} |  |

and

 | B = − 4 ​ log ⁡ 2 − 1 6 ​ ζ ′ ​ ( 2) ζ ​ ( 2) 2 + 24 ​ ( 4 ​ log ⁡ 2 − 1) ​ γ + 72 ​ log 2 ​ 2 − 76 ​ log ⁡ 2 + 1 12 ​ π 2 − 1 4. B=-\frac{4\log 2-1}{6}\frac{\zeta^{\prime}(2)}{\zeta(2)^{2}}+\frac{24(4\log 2-1)\gamma+72\log^{2}2-76\log 2+1}{12\pi^{2}}-\frac{1}{4}. |  |

###### Proof.

By Lemma 36 and the closed form from Section 2,

 | F ⁡ ( n) = S 1 ​ ( n) + S 2 ​ ( n) − S 12 ​ ( n) + F 0 ​ ( n), F 0 ​ ( n) = 1 3 ​ n 4 + O ⁡ ( n 3). F(n)=S_{1}(n)+S_{2}(n)-S_{12}(n)+F_{0}(n),\qquad F_{0}(n)=\frac{1}{3}n^{4}+O(n^{3}). |  |

Applying Theorems 31, 33, and 35, we obtain

 | A = A 1 + A 2 = 4 ​ log ⁡ 2 − 1 π 2, B = B 1 + B 2 − B 12 + 1 3. A=A_{1}+A_{2}=\frac{4\log 2-1}{\pi^{2}},\qquad B=B_{1}+B_{2}-B_{12}+\frac{1}{3}. |  |

Note in particular that S 12 ​ ( n) S_{12}(n) contributes only at order n 4 n^{4}, so the entire n 4 ​ log ⁡ n n^{4}\log n term comes from S 1 ​ ( n) + S 2 ​ ( n) S_{1}(n)+S_{2}(n). Equivalently, the logarithm arises from the one-parameter sums in S 1 S_{1} and S 2 S_{2}, whereas the overlap S 12 S_{12} already lives on the doubly truncated scale u, v, a, b ≪ n u,v,a,b\ll\sqrt{n} and therefore has size only n 4 n^{4}. Substituting the explicit constants yields the stated formula for B B. ∎

## References

- [1] M. Beck and S. Robins, *Computing the Continuous Discretely: Integer-Point Enumeration in Polyhedra*, 2nd ed., Undergraduate Texts in Mathematics, Springer, New York, 2015.
- [2] R. L. Graham, D. E. Knuth, and O. Patashnik, *Concrete Mathematics*, 2nd ed., Addison–Wesley, Reading, MA, 1994.
- [3] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed., Oxford University Press, Oxford, 2008.
- [4] H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press, Cambridge, 2007.
- [5] G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., Graduate Studies in Mathematics, Vol. 163, American Mathematical Society, Providence, RI, 2015.
- [6] NIST Digital Library of Mathematical Functions, release 1.2.4, F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds., https://dlmf.nist.gov/25.12.E12.
- [7] M. Beck and S. Robins, Dedekind sums: a combinatorial-geometric viewpoint, in *Unusual Applications of Number Theory*, DIMACS Ser. Discrete Math. Theoret. Comput. Sci., vol. 64, Amer. Math. Soc., Providence, RI, 2004, pp. 25–35.
- [8] M. N. Huxley and W. G. Nowak, Primitive lattice points in convex planar domains, *Acta Arith.*76 (1996), 271–283.
- [9] M. Pătraşcu, Farey statistics in time n 2 / 3 n^{2/3} and counting primitive lattice points in polygons, arXiv:0708.0080, 2007.
- [10] D. Zagier, Higher dimensional Dedekind sums, *Math. Ann.*202 (1973), 149–172.
- [11] L. Brandolini, L. Colzani, B. Gariboldi, G. Gigante, and A. Monguzzi, Euler–MacLaurin summation formula on polytopes and expansions in multivariate Bernoulli polynomials, *J. Fourier Anal. Appl.*29 (2023), Art. 33.
- [12] V. Baldoni, N. Berline, J. A. De Loera, M. Köppe, and M. Vergne, How to integrate a polynomial over a simplex, *Math. Comp.*80 (2011), 297–325.
- [13] G. E. Andrews and K. Eriksson. *Integer Partitions*. Cambridge University Press, 2004.
- [14] OEIS Foundation Inc., *A085582: Number of rectangles (orthogonal or not) with corners on an n × n n\times n grid of points*. The On-Line Encyclopedia of Integer Sequences, accessed April 2026.
- [15] D. Radcliffe. *Table and Python script for OEIS A085582*. Linked from the OEIS entry A085582, accessed April 2026.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://github.com/flykiller/lattice-rectangles
