<!-- source: https://arxiv.org/html/2607.17961v1 | converted from HTML -->

Counting Lattice Rectangles in O ( ⁢ n log n ) Arithmetic Operations

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2607.17961v1 [cs.CG] 20 Jul 2026

Independent researcher, France Independent researcher, France \modulolinenumbers [5]

# Counting Lattice Rectangles in O ⁡ ( n ​ log ⁡ n) O(n\log n) Arithmetic Operations

Dmitry Babichev Tatiana Shpakova

###### Abstract

Let F ⁡ ( n) F(n) be the number of rectangles, not necessarily axis-parallel, whose vertices belong to the n × n n\times n square grid of lattice points. We give an exact algorithm that computes one prescribed value F ⁡ ( n) F(n) in O ⁡ ( n ​ log ⁡ n) O(n\log n) arithmetic operations and O ⁡ ( n 3 / 4) O(n^{3/4}) arithmetic words of working memory. The algorithm decomposes the count into Möbius divisor layers, partitions weighted floor-moment queries by a truncated Euclidean coefficient-cone recursion, and reuses uniform marker grids along common coefficient paths. Each marker requires only its uniform cell and constant-size corrections at nearby boundaries, which select an exact precompiled cell operator. All integer operands have O ⁡ ( log ⁡ n) O(\log n) bits. An exact 128-bit C++ implementation for the reported input range is compared experimentally with the previous O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) algorithm.

###### ccs

Theory of computation Design and analysis of algorithms

###### ccs

Theory of computation Computational geometry

###### keywords

Lattice rectangles, exact counting, floor sums, Möbius inversion, Euclidean algorithm

† † runningtitle: Counting Lattice Rectangles in O ⁡ ( n ​ log ⁡ n) O(n\log n) Operations † † runningauthor: Dmitry Babichev and Tatiana Shpakova † † copyright: Dmitry Babichev and Tatiana Shpakova

## 1 Introduction

Let F ⁡ ( n) F(n) denote the number of rectangles, axis-parallel or oblique, whose four vertices belong to the point grid { 0, …, n − 1 } 2 \{0,\ldots,n-1\}^{2}. This is OEIS A085582 [15]. Previous work by Babichev and Babichev [2] computes one exact value in O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) arithmetic operations. We reduce this bound to O ⁡ ( n ​ log ⁡ n) O(n\log n) while retaining sublinear working memory.

The problem combines lattice-point enumeration with primitive-direction counting. General rational-polyhedral methods are developed by Beck and Robins [7] and Barvinok [4]; primitive planar lattice points have also been studied analytically [13] and algorithmically [16]. Here the orthogonality and side-multiplicity structure of rectangles leads to a more specialized floor-moment problem.

Weighted floor sums and reciprocity also occur in integer-point transforms of rational cones and in power sums of floor functions, notably through Dedekind–Carlitz and Rademacher–Carlitz polynomials and generalized Dedekind sums [5, 6, 9]; the continued-fraction and continuant facts used below are standard [17]. Reusing initial Euclidean quotient sequences goes back at least to Lehmer’s large-integer GCD method and its modern fast-arithmetic descendants [14, 8]. Those methods accelerate one large GCD instance. Here common prefixes are instead shared across the Θ ⁡ ( N) \Theta(N) related coefficient pairs of a layer of size N N and are coupled to two finite-endpoint marker traces.

The first step expresses the non-axis-parallel contribution through primitive direction vectors and then through Möbius divisor layers. For one layer of size N N, a half-domain reduction leaves six weighted floor moments. A truncated Euclidean recursion groups their parameters by coefficient paths. Uniform marker grids compile the common part of each path, while a constant menu of local boundary corrections identifies the exact cell operator for every query. Choosing the three internal scales as N 1 / 2, N 1 / 4, N 1 / 4 N^{1/2},N^{1/4},N^{1/4} gives linear arithmetic work per distinct divisor layer and O ⁡ ( N 3 / 4) O(N^{3/4}) words of peak storage. Summing the distinct quotient layers yields the claimed O ⁡ ( n ​ log ⁡ n) O(n\log n) total.

The geometric parametrization, Möbius divisor-layer identity, and pointwise six-moment Euclidean kernel build on [2]. We restate those reductions in the exact form needed here. The new contribution starts at batch evaluation: coefficient cones compile common coefficient traces, modular-orbit marker grids classify both finite endpoints, and constant-size correction menus select an exact precompiled cell operator. These ingredients replace an independent O ⁡ ( log ⁡ N) O(\log N) recursion for each coefficient pair by linear work per layer. We give the complete algorithm and prove its O ⁡ ( n ​ log ⁡ n) O(n\log n) time and O ⁡ ( n 3 / 4) O(n^{3/4}) memory bounds. A companion manuscript in preparation studies the complementary all-values problem of computing the complete prefix F ⁡ ( 1), …, F ⁡ ( N) F(1),\ldots,F(N) by rational generating series [3].

We distinguish arithmetic-operation bounds from bit complexity. An *arithmetic word*stores a signed integer of O ⁡ ( log ⁡ n) O(\log n) bits, and one arithmetic operation is an exact addition, subtraction, multiplication, Euclidean division or remainder, or comparison on such words; random-access table lookup costs O ⁡ ( 1) O(1). GCD and modular-inverse construction costs are accounted for explicitly where they occur; see also the standard computational algebra model in [19]. Lemma 20 proves that every exact operand fits this model. Thus the arithmetic bound implies O ⁡ ( n ​ log ⁡ n ​ 𝖬 ℤ ​ ( log ⁡ n)) O(n\log n\,\mathsf{M}_{\mathbb{Z}}(\log n)) bit operations, where 𝖬 ℤ ​ ( b) \mathsf{M}_{\mathbb{Z}}(b) is the cost of multiplying two b b -bit integers. Fast exact division and remainder have the same asymptotic cost at this scale [8]. The classical Schönhage–Strassen bound is 𝖬 ℤ ​ ( b) = O ⁡ ( b ​ log ⁡ b ​ log ⁡ log ⁡ b) \mathsf{M}_{\mathbb{Z}}(b)=O(b\log b\log\log b) [18]; using the current 𝖬 ℤ ​ ( b) = O ⁡ ( b ​ log ⁡ b) \mathsf{M}_{\mathbb{Z}}(b)=O(b\log b) bound [12] gives O ⁡ ( n ​ log 2 ​ n ​ log ⁡ log ⁡ n) O(n\log^{2}n\log\log n) bit operations.

The paper first derives the geometric and moment reductions, then outlines the batching architecture and develops its Euclidean state recursion, marker corrections, cell operators, and complete algorithm. The experiments follow the main theorem. Lengthier identities and proofs are collected in the appendices.

## 2 Geometric reduction and Möbius divisor layers

Every lattice rectangle has two perpendicular side vectors x ⁡ ( u, v) x(u,v) and y ⁡ ( − v, u) y(-v,u), where x, y x,y are positive integers and ( u, v) (u,v) is a primitive integer vector. Reflecting and interchanging the sides gives a unique representative with u ⩾ v ⩾ 0 u\geqslant v\geqslant 0 and x ⩾ y x\geqslant y. Its axis-aligned bounding box has width x ​ u + y ​ v xu+yv and height x ​ v + y ​ u xv+yu, hence it has ( n − x ​ u − y ​ v) ​ ( n − x ​ v − y ​ u) (n-xu-yv)(n-xv-yu) translations in the n × n n\times n point grid. For 0 < v < u 0<v<u, the reflection orbit has size two when x = y x=y and four when x > y x>y; set 𝒲 ⁡ ( x, y) = 2 \mult(x,y)=2 when x = y x=y and 𝒲 ⁡ ( x, y) = 4 \mult(x,y)=4 when x > y x>y.

There are two boundary direction classes. If v = 0 v=0, primitivity forces ( u, v) = ( 1, 0) (u,v)=(1,0) and gives the axis-parallel rectangles. If u = v u=v, primitivity forces ( u, v) = ( 1, 1) (u,v)=(1,1) and gives the rectangles whose sides have slopes 1 1 and − 1 -1. Writing s = x + y s=x+y in this diagonal class, their total is

 | F 0 ​ ( n) = ( n 2) 2 + ∑ s = 2 n − 1 ( s − 1) ​ ( n − s) 2 = n ​ ( n − 1) 2 ​ ( 2 ​ n − 1) 6. F_{0}(n)=\binom{n}{2}^{2}+\sum_{s=2}^{n-1}(s-1)(n-s)^{2}=\frac{n(n-1)^{2}(2n-1)}{6}. |  | (1) |

The remaining representatives have u > v > 0 u>v>0, so

 | F 1 ​ ( n) = ∑ u > v > 0, x ⩾ y ⩾ 1 ( u, v) = 1, x ​ u + y ​ v ⩽ n 𝒲 ⁡ ( x, y) ​ ( n − xu − yv) ​ ( n − xv − yu). F_{1}(n)=\sum_{\begin{subarray}{c}u>v>0,\ x\geqslant y\geqslant 1\\ (u,v)=1,\ xu+yv\leqslant n\end{subarray}}\mult(x,y)(n-xu-yv)(n-xv-yu). |  | (2) |

Here ( x ​ u + y ​ v) − ( x ​ v + y ​ u) = ( u − v) ​ ( x − y) ⩾ 0 (xu+yv)-(xv+yu)=(u-v)(x-y)\geqslant 0, so the first bounding-box dimension dominates the second and the single inequality in ( 2) is sufficient. The preceding classification is exhaustive and its representatives are disjoint, hence

 | F ⁡ ( n) = F 0 ​ ( n) + F 1 ​ ( n). F(n)=F_{0}(n)+F_{1}(n). |  | (3) |

Use the standard Möbius identity 𝟏 ( u, v) = 1 = ∑ d | u, d | v μ ⁡ ( d) \mathbf{1}_{(u,v)=1}=\sum_{d\mid u,\,d\mid v}\mu(d) [1, Chapter 2], where 𝟏 E \mathbf{1}_{E} is the indicator of E E and μ \mu is the Möbius function. Write u = d ​ a u=da, v = d ​ b v=db, and put

 | N d = ⌊ n / d ⌋, S d ​ ( n) = ∑ a > b ⩾ 1, x ⩾ y ⩾ 1 a ​ x + b ​ y ⩽ N d 𝒲 ⁡ ( x, y) ​ ( n − d ⁡ ( ax + by)) ​ ( n − d ⁡ ( bx + ay)). N_{d}=\left\lfloor n/d\right\rfloor,\qquad S_{d}(n)=\sum_{\begin{subarray}{c}a>b\geqslant 1,\ x\geqslant y\geqslant 1\\ ax+by\leqslant N_{d}\end{subarray}}\mult(x,y)\bigl(n-d(ax+by)\bigr)\bigl(n-d(bx+ay)\bigr). |  | (4) |

Then

 | F 1 ​ ( n) = ∑ d ⩽ n μ ⁡ ( d) ​ S d ​ ( n). F_{1}(n)=\sum_{d\leqslant n}\mu(d)S_{d}(n). |  | (5) |

For a fixed layer size N N, let

 | Ω N = { ( a, b, x, y): a > b ⩾ 1, x ⩾ y ⩾ 1, a x + b y ⩽ N } \Omega_{N}=\{(a,b,x,y):a>b\geqslant 1,\ x\geqslant y\geqslant 1,\ ax+by\leqslant N\} |  |

and define

 | A ⁡ ( N) \displaystyle A(N) | = ∑ Ω N 𝒲 ⁡ ( x, y), \displaystyle=\sum_{\Omega_{N}}\mult(x,y), |  |

 | B ⁡ ( N) \displaystyle B(N) | = ∑ Ω N 𝒲 ⁡ ( x, y) ​ ( a + b) ​ ( x + y), \displaystyle=\sum_{\Omega_{N}}\mult(x,y)(a+b)(x+y), |  |

 | C ⁡ ( N) \displaystyle C(N) | = ∑ Ω N 𝒲 ⁡ ( x, y) ​ ( ab ⁡ ( x 2 + y 2) + ( a 2 + b 2) ​ xy). \displaystyle=\sum_{\Omega_{N}}\mult(x,y)\bigl(ab(x^{2}+y^{2})+(a^{2}+b^{2})xy\bigr). |  |

We call the coefficient triple ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) (A(N),B(N),C(N)) the *divisor layer of size N N*. Since ( a − b) ​ ( x − y) ⩾ 0 (a-b)(x-y)\geqslant 0, the displayed constraint also enforces the second bounding-box inequality. Expanding the two linear factors gives

 | S d ​ ( n) = n 2 ​ A ​ ( N d) − n ​ d ​ B ​ ( N d) + d 2 ​ C ​ ( N d). S_{d}(n)=n^{2}A(N_{d})-ndB(N_{d})+d^{2}C(N_{d}). |  | (6) |

Hence quotient blocking evaluates ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) (A(N),B(N),C(N)) once and reuses it for all divisors with the same N d N_{d}.

## 3 Weighted floor moments

This section converts the four-dimensional layer sum into at most one six-moment floor query per coefficient pair, plus formulas involving ordinary power sums only. The half-domain symmetry is the interface between the geometric counting problem and the recursive Euclidean transducer developed below. For background on floor functions and their role in lattice-point reciprocity, see [11, 7].

For 0 ⩽ b, β < a 0\leqslant b,\beta<a and q ⩾ 0 q\geqslant 0, put f ⁡ ( t) = ⌊ ( b ​ t + β) / a ⌋ f(t)=\left\lfloor(bt+\beta)/a\right\rfloor for 0 ⩽ t < q 0\leqslant t<q. A query with q = 0 q=0 has an empty summation range. A normalized query with b = 0 b=0 is also identically zero because 0 ⩽ β < a 0\leqslant\beta<a. Both cases return the zero moment vector before any reciprocal step. In the sequel a *nontrivial query*means q > 0 q>0 and 0 < b < a 0<b<a. Write

 | Φ i ​ j ​ ( f):= ∑ 0 ⩽ t < q t i ​ f ​ ( t) j, 𝚽 ⁡ ( f):= ( Φ 01, Φ 11, Φ 21, Φ 02, Φ 12, Φ 03) 𝖳. \Phi_{ij}(f):=\sum_{0\leqslant t<q}t^{i}f(t)^{j},\qquad\boldsymbol{\Phi}(f):=(\Phi_{01},\Phi_{11},\Phi_{21},\Phi_{02},\Phi_{12},\Phi_{03})^{\mathsf{T}}. |  | (7) |

This six-moment vector is required by the geometric upper-limit formulas in Appendix A.1. The Euclidean recurrence, however, has a simpler closed action on the six lattice moments

 | 𝖫 i ​ j ​ ( f):= ∑ 0 ⩽ t < q ∑ 1 ⩽ s ⩽ f ⁡ ( t) t i ​ s j, 𝐋 ⁡ ( f):= ( 𝖫 00, 𝖫 10, 𝖫 20, 𝖫 01, 𝖫 11, 𝖫 02) 𝖳, \mathsf{L}_{ij}(f):=\sum_{0\leqslant t<q}\sum_{1\leqslant s\leqslant f(t)}t^{i}s^{j},\qquad\mathbf{L}(f):=(\mathsf{L}_{00},\mathsf{L}_{10},\mathsf{L}_{20},\mathsf{L}_{01},\mathsf{L}_{11},\mathsf{L}_{02})^{\mathsf{T}}, |  |

by the explicit identities

 | Φ 01 = 𝖫 00, Φ 11 = 𝖫 10, Φ 21 = 𝖫 20, Φ 02 = 2 𝖫 01 − 𝖫 00, Φ 12 = 2 𝖫 11 − 𝖫 10, Φ 03 = 3 𝖫 02 − 3 𝖫 01 + 𝖫 00. \begin{gathered}\Phi_{01}=\mathsf{L}_{00},\quad\Phi_{11}=\mathsf{L}_{10},\quad\Phi_{21}=\mathsf{L}_{20},\\ \Phi_{02}=2\mathsf{L}_{01}-\mathsf{L}_{00},\quad\Phi_{12}=2\mathsf{L}_{11}-\mathsf{L}_{10},\quad\Phi_{03}=3\mathsf{L}_{02}-3\mathsf{L}_{01}+\mathsf{L}_{00}.\end{gathered} |  | (8) |

The vector 𝐋 \mathbf{L} is the internal state transported by every compiled operator in Section 8; the algorithm converts 𝐋 \mathbf{L} to the required Φ \Phi -moments only once, after the root staircase has been evaluated.

Put D = ⌊ N ⌋ D=\left\lfloor\sqrt{N}\right\rfloor. For a fixed direction pair a > b ⩾ 1 a>b\geqslant 1 and a summed side pair x > y ⩾ 1 x>y\geqslant 1, define

 | 𝐰 a, b ​ ( x, y) = ( 1, ( a + b) ​ ( x + y), a ​ b ​ ( x 2 + y 2) + ( a 2 + b 2) ​ x ​ y). \mathbf{w}_{a,b}(x,y)=\left(1,(a+b)(x+y),ab(x^{2}+y^{2})+(a^{2}+b^{2})xy\right). |  |

This is the contribution to ( A, B, C) (A,B,C) before the side-multiplicity factor.

###### Lemma 1 (Half-domain moment reduction).

The triple ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) (A(N),B(N),C(N)) is given by the formulas in Appendix A.1. The reduction uses at most one six-moment floor query for every a > b ⩾ 1 a>b\geqslant 1 with a ⩽ D a\leqslant D, O ⁡ ( 1) O(1) power-sum evaluations per pair, and an O ⁡ ( N) O(N) diagonal sum. In particular, one layer contains at most D ⁡ ( D − 1) / 2 D(D-1)/2 nonempty floor queries and is generated in O ⁡ ( N) O(N) operations.

###### Proof sketch.

Exchange the direction pair ( a, b) (a,b) with the side pair ( x, y) (x,y) and keep the half with a ⩽ x a\leqslant x. Then a ⩽ N a\leqslant\sqrt{N}, which leaves only O ⁡ ( N) O(N) direction pairs. For a fixed pair, the admissible values of x x form one interval for every y y. Reversing the y y -order turns its upper endpoint into the single normalized floor query f ⁡ ( t) = ⌊ ( b ​ t + β) / a ⌋ f(t)=\left\lfloor(bt+\beta)/a\right\rfloor, 0 ⩽ t < q 0\leqslant t<q. Its six moments give all degree-two sums over the interval. The lower endpoint, the equality boundary a = x a=x, and the side diagonal x = y x=y are ordinary power sums. The exact interval endpoints, six moment conversions, and boundary formulas are collected in Appendix A.1. ∎

For each coefficient pair, call its nonempty normalized floor query together with the data needed to recover its contribution to ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) (A(N),B(N),C(N)) a *floor-moment record*. The formulas in Appendix A.1 completely specify record generation. There are at most D ⁡ ( D − 1) / 2 = O ⁡ ( N) D(D-1)/2=O(N) six-moment queries in one layer.

The six moments are closed under extracting integral parts and under the reciprocal floor transformation. A pointwise query therefore costs O ⁡ ( log ⁡ a) O(\log a); evaluating all queries pointwise would cost O ⁡ ( N ​ log ⁡ N) O(N\log N) for the layer. The next section outlines how common quotient prefixes and uniform marker grids remove this logarithm. All running times below use the arithmetic-word model fixed in the introduction.

## 4 Idea of the O ⁡ ( n ​ log ⁡ n) O(n\log n) algorithm

For a fixed divisor layer of size N N, Lemma 1 produces a linear-size family of closely related floor staircases. The algorithm shares their Euclidean work at two levels. Recall that D = ⌊ N ⌋ D=\left\lfloor\sqrt{N}\right\rfloor is the coefficient cap, and let τ = Θ ⁡ ( D) \tau=\Theta(\sqrt{D}) be the path threshold. We write P P for a coefficient path of length d d and L L for its number of marker slots. Nonempty queries with root length q ⩽ 5 ​ τ q\leqslant 5\tau use the pointwise recursion; the remaining nonempty queries are called *long*. The indices i, j i,j label exact marker slots on P P.

First, coefficient pairs with the same initial Euclidean divisions form one batch. Their common coefficient path is identified once, and each original pair is left with only a small terminal pair ( M, R) (M,R).

Within one batch, the cell operators also share prefixes. If its L 2 L^{2} cell operators were compiled independently, replaying a path of length d d for every cell would cost O ⁡ ( L 2 ​ d) O(L^{2}d). Since d d can be logarithmic, this would add one logarithm to the final running time. Instead, a prefix tree merges cell traces while they are equal and compiles all L 2 L^{2} operators in O ⁡ ( L 2) O(L^{2}) work.

The endpoint classification is shared at the batch level as well. Each batch receives two uniform grids for the endpoint markers u u and v v. The exact boundaries move slightly with ( M, R) (M,R), but inside one uniform cell only three nearby boundaries can matter. We test those few boundaries and record a local correction in { 0, 1, 2, 3 } \{0,1,2,3\}.

For two markers, the two uniform cells give a rectangle 𝒱 x ​ y \mathcal{V}_{xy}, and the two local corrections ( α u, α v) (\alpha_{u},\alpha_{v}) select one of at most sixteen conceptual entries. That entry identifies the exact rectangle operator. The reference implementation evaluates this constant-size map implicitly from prefix counts and the local comparisons, then indexes the compiled operator directly; it does not store a separate 4 × 4 4\times 4 table for every rectangle. The operator sends the record to a small terminal staircase, which is answered from a shared table and lifted back to the six required moments.

The grids and their correction data are built once per coefficient path. Building a separate marker partition for every one of the Θ ⁡ ( D 2) \Theta(D^{2}) coefficient pairs would cost O ⁡ ( D 2 ​ τ) = O ⁡ ( N 5 / 4) O(D^{2}\tau)=O(N^{5/4}); sharing them keeps the divisor layer linear.

uniform marker grid for one path P P 𝒱 x ​ y \mathcal{V}_{xy} one record u u v v local correction menu at most 16 16 entries α u \alpha_{u} α v \alpha_{v} compiled operator 𝖮𝗉 P; i, j \mathsf{Op}_{P;i,j} terminal lookup and operator lift six root moments local corrections ( α u, α v) = ( 2, 2) (\alpha_{u},\alpha_{v})=(2,2) Figure 1: A record first enters the uniform rectangle 𝒱 x ​ y \mathcal{V}_{xy}. Only the nearby dashed true boundaries matter inside that rectangle; they give the local corrections ( α u, α v) (\alpha_{u},\alpha_{v}). The selected conceptual menu entry identifies the exact compiled operator.

Four facts give linear work in one divisor layer: the coefficient batches partition all direction pairs; each path has only quadratically many cell operators and correction-menu entries; their total number over all paths is linear in the layer size; and every long record performs constant work. Quotient blocking over the divisor layers then gives the claimed O ⁡ ( n ​ log ⁡ n) O(n\log n) running time.

The remaining construction is organized as follows. Section 5 derives the exact reciprocal rule for one query. Section 6 defines coefficient batches and terminal coordinates. Section 7 defines the uniform-grid corrections, and Section 8 compiles the true operators and specifies the correction map. The technical proofs are collected in Appendix B; the marker-grid construction is detailed in Appendix B.3.

## 5 One-query Euclidean cycle and affine lift

Section 3 reduces one divisor layer to O ⁡ ( N) O(N) floor-moment queries. Evaluating every query by its own Euclidean recursion would cost O ⁡ ( N ​ log ⁡ N) O(N\log N). This section derives the local reciprocal cycle for one query; Sections 6 – 8 then compile and reuse it across a batch. A normalized query has four independent parameters, but the recurrence becomes affine after two endpoint data are made explicit. The direction pair ( a, b) (a,b) determines the ordinary Euclidean quotients, whereas the intercept β \beta and the interval length q q determine where the finite floor staircase begins and ends.

### 5.1 The staircase and its two boundary markers

After the zero cases above have been removed, every nontrivial floor query has the normalized form

 | f ⁡ ( t) = ⌊ b ​ t + β a ⌋, 0 ⩽ t < q, q > 0, 0 < b < a, 0 ⩽ β < a. f(t)=\left\lfloor\frac{bt+\beta}{a}\right\rfloor,\qquad 0\leqslant t<q,\qquad q>0,\quad 0<b<a,\quad 0\leqslant\beta<a. |  | (9) |

Its lattice staircase is

 | Λ f = { ( t, s) ∈ ℤ 2: 0 ⩽ t < q, 1 ⩽ s ⩽ f ( t) }. \Lambda_{f}=\{(t,s)\in\mathbb{Z}^{2}:0\leqslant t<q,\ 1\leqslant s\leqslant f(t)\}. |  | (10) |

Its graph is a staircase inside a rectangle of width q q. Its height is h = f ⁡ ( q − 1) = ⌊ ( b ⁡ ( q − 1) + β) / a ⌋ h=f(q-1)=\left\lfloor(b(q-1)+\beta)/a\right\rfloor. The standard reciprocal transformation counts the complementary staircase after interchanging the two coordinate directions. The transformed floor function is

 | f ^ ​ ( k) = ⌊ a ​ k + u b ⌋, 0 ⩽ k < h, u = a − β − 1. \widehat{f}(k)=\left\lfloor\frac{ak+u}{b}\right\rfloor,\qquad 0\leqslant k<h,\qquad u=a-\beta-1. |  | (11) |

Thus u u records the left boundary of the complementary staircase. At the right boundary, write the endpoint numerator as b ⁡ ( q − 1) + β = a ​ h + v b(q-1)+\beta=ah+v. The remainder v v records where the final step meets that boundary.

###### Definition 2 (Affine query state).

The *affine query state*of the normalized floor query ( 9) is the six-coordinate column vector

 | 𝐬 ⁡ ( a, b, q, β):= ( a, b, q, h, u, v) 𝖳, u = a − β − 1, v = b ⁡ ( q − 1) + β − a ​ h. \mathbf{s}(a,b,q,\beta):=(a,b;q,h;u,v)^{\mathsf{T}},\qquad u=a-\beta-1,\quad v=b(q-1)+\beta-ah. |  | (12) |

The semicolons group its coordinates as

 | ( a, b) ⏟ direction coefficients; ( q, h) ⏟ staircase dimensions; ( u, v) ⏟ boundary markers. \underbrace{(a,b)}_{\text{direction coefficients}}\ ;\quad\underbrace{(q,h)}_{\text{staircase dimensions}}\ ;\quad\underbrace{(u,v)}_{\text{boundary markers}}. |  |

For a sequence of reciprocal cycles, 𝐬 root \mathbf{s}_{\mathrm{root}} denotes its initial state and 𝐬 term \mathbf{s}_{\mathrm{term}} the state after the last cycle.

###### Definition 3 (Boundary markers and quotient trace).

For a normalized finite staircase, the remainders u u and v v in ( 12) are its *left*and *right boundary markers*. They record where the complementary staircase starts and where the final step meets the opposite boundary. At reciprocal cycle i i, write the current state as ( a i, b i, q i, h i, u i, v i) (a_{i},b_{i};q_{i},h_{i};u_{i},v_{i}) and define A i = ⌊ a i / b i ⌋ A_{i}=\left\lfloor a_{i}/b_{i}\right\rfloor, U i = ⌊ u i / b i ⌋ U_{i}=\left\lfloor u_{i}/b_{i}\right\rfloor, and V i = ⌊ v i / b i ⌋ V_{i}=\left\lfloor v_{i}/b_{i}\right\rfloor. These are respectively the coefficient, left-marker, and right-marker quotients. A *word*here is simply a finite sequence of quotients. Thus ( A i) i (A_{i})_{i} is the *coefficient word*, while ( U i) i (U_{i})_{i} and ( V i) i (V_{i})_{i} are the two *marker words*. The sequence of quotient triples ( (,,,,,)) i ((A_{i},U_{i},V_{i}))_{i} is the *complete quotient trace*of the query.

The coefficient word depends only on ( a, b) (a,b). The marker words additionally depend on the finite endpoints of the staircase. A shared operator is therefore indexed by the coefficient word and both marker words.

Although ( a, b, q, β) (a,b,q,\beta) determines the query and β = a − u − 1 \beta=a-u-1, the lifted state retains h h, because it becomes the next interval length, and retains u, v u,v, because U = ⌊ u / b ⌋ U=\left\lfloor u/b\right\rfloor and V = ⌊ v / b ⌋ V=\left\lfloor v/b\right\rfloor are classified separately. We therefore retain the affine lift throughout. Its bounds are 0 < b < a 0<b<a, 0 ⩽ u, v < a 0\leqslant u,v<a, q > 0 q>0, and h ⩾ 0 h\geqslant 0. If h = 0 h=0, monotonicity of f f shows that all its values are zero; such a state is terminal and is never used as the parent of another reciprocal cycle.

The affine lift describes one finite staircase, whereas the six-moment vector in ( 7) contains six aggregate sums over that staircase. A compiled operator updates the state affinely and transports the moment vector linearly, with a polynomial boundary correction.

### 5.2 One complete Euclidean cycle

Assume in this subsection that h > 0 h>0, so another cycle is required. The reciprocal query ( 11) is not yet normalized because its coefficient a a can exceed its modulus b b. Extract the three quotients A = ⌊ a / b ⌋ A=\left\lfloor a/b\right\rfloor, U = ⌊ u / b ⌋ U=\left\lfloor u/b\right\rfloor, and V = ⌊ v / b ⌋ V=\left\lfloor v/b\right\rfloor. Put b ′ = a − A ​ b b^{\prime}=a-Ab and β ′ = u − U ​ b \beta^{\prime}=u-Ub. Then the normalized child is f ′ ​ ( k) = ⌊ ( b ′ ​ k + β ′) / b ⌋ f^{\prime}(k)=\left\lfloor(b^{\prime}k+\beta^{\prime})/b\right\rfloor, and f ^ ​ ( k) = A ​ k + U + f ′ ​ ( k) \widehat{f}(k)=Ak+U+f^{\prime}(k). Write the current and child states explicitly as

 | 𝐬 = ( a, b, q, h, u, v) 𝖳 → 𝒯 A, U, V 𝐬 ′ = ( a ′, b ′, q ′, h ′, u ′, v ′) 𝖳. \mathbf{s}=(a,b;q,h;u,v)^{\mathsf{T}}\xrightarrow{\ \mathcal{T}_{A,U,V}\ }\mathbf{s}^{\prime}=(a^{\prime},b^{\prime};q^{\prime},h^{\prime};u^{\prime},v^{\prime})^{\mathsf{T}}. |  |

The reciprocal transformation followed by normalization is the coordinate form of this affine state transition:

 | a ′ \displaystyle a^{\prime} | = b, \displaystyle=b, | b ′ \displaystyle b^{\prime} | = a − A ​ b, \displaystyle=a-Ab, |  |

 | q ′ \displaystyle q^{\prime} | = h, \displaystyle=h, | h ′ \displaystyle h^{\prime} | = q − A ​ h − ( U + V + 2 − A), \displaystyle=q-Ah-(U+V+2-A), |  | (13) |

 | u ′ \displaystyle u^{\prime} | = ( U + 1) ​ b − u − 1, \displaystyle=(U+1)b-u-1, | v ′ \displaystyle v^{\prime} | = ( V + 1) ​ b − v − 1. \displaystyle=(V+1)b-v-1. |  |

Its direct derivation from the reciprocal floor function is given in Appendix B.1.

Equation ( 13) is the payoff for the lift: once the quotient triple ( A, U, V) (A,U,V) is fixed, one complete cycle is a fixed integral affine map. The reciprocal and polynomial moment identities are fixed as well. Hence a whole common quotient trace can be composed in advance into one constant-size operator and then applied to every query in the corresponding piece of the parameter space.

(a) one normalized query f ⁡ ( t) = ⌊ ( 8 ​ t + 3) / 17 ⌋ f(t)=\left\lfloor(8t+3)/17\right\rfloor 0 ≤ t < 18 0\leq t<18, 𝐬 = ( 17, 8, 18, 8, 13, 3) 𝖳 \mathbf{s}=(17,8;18,8;13,3)^{\mathsf{T}} t t s s q = 18 q=18 𝐬 ↦ 𝐬 ′ \mathbf{s}\mapsto\mathbf{s}^{\prime} transpose the complement extract ( A, U, V) = ( 2, 1, 0) (A,U,V)=(2,1,0) f ^ ​ ( k) = 2 ​ k + 1 + f ′ ​ ( k) \widehat{f}(k)=2k+1+f^{\prime}(k) (b) reciprocal query f ^ ​ ( k) = ⌊ ( 17 ​ k + 13) / 8 ⌋ \widehat{f}(k)=\left\lfloor(17k+13)/8\right\rfloor 𝐬 ′ = ( 8, 1, 8, 1, 2, 4) 𝖳 \mathbf{s}^{\prime}=(8,1;8,1;2,4)^{\mathsf{T}} k k f ^ \widehat{f} affine part 2 ​ k + 1 2k+1 child f ′ ​ ( k) f^{\prime}(k)

Figure 2: One reciprocal cycle for a normalized query. All displayed cells are equal squares. Left: Λ f \Lambda_{f} (blue) and its complement (gray). Right: the transposed complement splits into the affine part (orange) and the recursive child (blue); the red staircase is the graph of f ^ \widehat{f}.

In the left panel of Figure 2, the orange point in row s s marks t = f ^ ​ ( s − 1) + 1 t=\widehat{f}(s-1)+1, the first admitted column. In the right panel, transposition gives f ^ ​ ( k) = 2 ​ k + 1 + f ′ ​ ( k) \widehat{f}(k)=2k+1+f^{\prime}(k) and the state transition 𝐬 ↦ 𝐬 ′ = ( 8, 1, 8, 1, 2, 4) 𝖳 \mathbf{s}\mapsto\mathbf{s}^{\prime}=(8,1;8,1;2,4)^{\mathsf{T}}. This is the local identity from which an operator is built. The construction of true marker rectangles, uniform-grid correction maps, and their operators is given in Sections 7 and 8.

### 5.3 Why the one-query rule can be reused

For the displayed query ( a, b, q, β) = ( 17, 8, 18, 3) (a,b,q,\beta)=(17,8,18,3), the lift is ( 17, 8, 18, 8, 13, 3) (17,8;18,8;13,3) and ( A, U, V) = ( 2, 1, 0) (A,U,V)=(2,1,0). Changing only the intercept to β = 4 \beta=4 gives the different lift ( 17, 8, 18, 8, 12, 4) (17,8;18,8;12,4) but the same quotient triple. Equation ( 13) therefore applies the same affine state update to both queries; only the numerical marker values differ. More generally, once the complete quotient trace ( (,,,,,)) i ((A_{i},U_{i},V_{i}))_{i} is fixed, its cycle maps can be composed once. The paired construction attaches that operator to every true rectangle on which the sequence is fixed, and the local correction menu selects it from the two marker codes.

## 6 Coefficient-cone recursion and terminal coordinates

Fix one layer and put

 | D = ⌊ N ⌋, σ = ⌈ D ⌉, τ = ⌈ 3 ​ σ / 8 ⌉, κ = max ⁡ ( τ, ⌈ D / τ ⌉). D=\left\lfloor\sqrt{N}\right\rfloor,\qquad\sigma=\left\lceil\sqrt{D}\right\rceil,\qquad\tau=\left\lceil 3\sigma/8\right\rceil,\qquad\kappa=\max\!\left(\tau,\left\lceil D/\tau\right\rceil\right). |  | (14) |

###### Definition 4 (Layer and batching scales).

D D is the largest coefficient occurring in the layer. The auxiliary scale σ \sigma is its square-root scale. The *path threshold*τ \tau limits the common Euclidean prefix compiled for one coefficient batch. The *terminal threshold*κ \kappa limits the moduli stored in the shared small-modulus table of Section 8.3. Since κ ⩾ ⌈ D / τ ⌉ \kappa\geqslant\left\lceil D/\tau\right\rceil, we have τ ​ κ ⩾ D \tau\kappa\geqslant D, while both τ \tau and κ \kappa are Θ ⁡ ( D) \Theta(\sqrt{D}). The product inequality guarantees that when a large pair with R > 0 R>0 cannot extend its compiled path, one further Euclidean step reaches a modulus below κ \kappa; the case R = 0 R=0 is already terminal. This is formalized in Lemma 7.

One Euclidean division a i = A i ​ b i + r i a_{i}=A_{i}b_{i}+r_{i} replaces ( a i, b i) (a_{i},b_{i}) by ( b i, r i) (b_{i},r_{i}). A coefficient path of length d d consists of d d such divisions, with quotients A 0, …, A d − 1 A_{0},\ldots,A_{d-1}. The matrix

 | Q ⁡ ( A):= ( A 1 1 0), ( a i b i) = Q ⁡ ( A i) ​ ( b i r i), Q(A):=\begin{pmatrix}A&1\\ 1&0\end{pmatrix},\qquad\binom{a_{i}}{b_{i}}=Q(A_{i})\binom{b_{i}}{r_{i}}, |  |

reverses one step. For the full length- d d prefix define P 0 = I P_{0}=I, P i + 1 = P i ​ Q ​ ( A i) P_{i+1}=P_{i}Q(A_{i}), and P = P d P=P_{d}. Thus P i P_{i} maps the coefficient pair after i i divisions back to the root pair, and P = ( π i ​ j) 1 ⩽ i, j ⩽ 2 P=(\pi_{ij})_{1\leqslant i,j\leqslant 2} is the *path matrix*of the full prefix.

###### Definition 5 (Coefficient path and cone).

The coefficient word A 0, …, A d − 1 A_{0},\ldots,A_{d-1} is an *accepted coefficient path*if every entry of its path matrix P P is at most τ \tau. Its *coefficient cone*is the set of direction pairs ( a, b) (a,b) whose canonical Euclidean divisions begin with this word. After these divisions the remaining pair ( M, R) (M,R) is called the *terminal pair*, or the terminal coordinates of ( a, b) (a,b) on the path. The root and terminal pairs satisfy

 | ( a b) = P ​ ( M R), M > R ⩾ 0, 1 ⩽ b < a ⩽ D. \binom{a}{b}=P\binom{M}{R},\qquad M>R\geqslant 0,\qquad 1\leqslant b<a\leqslant D. |  | (15) |

The generator starts with the empty path P = I P=I. At a stored path it tries the canonical next quotient A = ⌊ M / R ⌋ A=\left\lfloor M/R\right\rfloor, whenever R > 0 R>0. The child P ​ Q ​ ( A) PQ(A) is accepted exactly when its four entries remain at most τ \tau. Geometrically this splits one rational cone in the coefficient triangle into subcones with a common longer prefix.

###### Definition 6 (Stopping rule and coefficient batch).

For an accepted path P P define ext ⁡ ( P) = max ⁡ { A ⩾ 1: max i, j ⁡ ( P ​ Q ​ ( A)) i ​ j ⩽ τ } \operatorname{ext}(P)=\max\{A\geqslant 1:\max_{i,j}(PQ(A))_{ij}\leqslant\tau\}, with value zero if no child is accepted. A root pair stops at its current path when M ⩽ τ M\leqslant\tau, R = 0 R=0, or R > 0 R>0 and ⌊ M / R ⌋ > ext ⁡ ( P) \left\lfloor M/R\right\rfloor>\operatorname{ext}(P). All root pairs that stop at the same path form one *coefficient batch*. The path matrix and coefficient word are shared by the whole batch; only ( M, R) (M,R) varies.

For direct implementation the maximum in this definition is the explicit integer expression

 | ext ⁡ ( P) = min ⁡ { ⌊ τ − π 12 π 11 ⌋, ⌊ τ − π 22 π 21 ⌋ }, \operatorname{ext}(P)=\min\!\left\{\left\lfloor\frac{\tau-\pi_{12}}{\pi_{11}}\right\rfloor,\left\lfloor\frac{\tau-\pi_{22}}{\pi_{21}}\right\rfloor\right\}, |  | (16) |

where the second term is omitted when π 21 = 0 \pi_{21}=0. Indeed, the only entries of P ​ Q ​ ( A) PQ(A) that depend on A A are π 11 ​ A + π 12 \pi_{11}A+\pi_{12} and π 21 ​ A + π 22 \pi_{21}A+\pi_{22}; the other two are already entries of the accepted matrix P P. Thus no search over candidate quotients is required.

For direct integer enumeration at a stored node, let A last A_{\rm last} be the incoming quotient, absent at the root. The stopped terminal pairs are exactly the following disjoint pieces:

1. 1.

M ⩽ τ M\leqslant\tau, with either P = I P=I or A last ​ M + R > τ A_{\rm last}M+R>\tau;

2. 2.

at a nonroot node, M > τ M>\tau, R = 0 R=0, and A last ⩾ 2 A_{\rm last}\geqslant 2;

3. 3.

M > τ M>\tau, R > 0 R>0, and M ⩾ ( ext ⁡ ( P) + 1) ​ R M\geqslant(\operatorname{ext}(P)+1)R.

The predecessor guard in the first piece enforces that the recursive parent was active. The condition in the second piece is the standard convention for the finite Euclidean algorithm: a zero remainder is never represented by an artificial trailing quotient one. Denote this stopped set by 𝒯 ⁡ ( P) \mathcal{T}(P).

###### Lemma 7 (One-step terminal).

At a stopped coefficient cone, either R = 0 R=0, or M ⩽ κ M\leqslant\kappa, or one further ordinary Euclidean step reaches a positive modulus below κ \kappa.

The short inequality proof is given in Appendix B.2.

###### Lemma 8 (Cone partition and enumeration).

The map ( P, M, R) ⟼ ( a, b) = P ⁡ ( M, R) (P,M,R)\longmapsto(a,b)=P(M,R), with ( M, R) ∈ 𝒯 ⁡ ( P) (M,R)\in\mathcal{T}(P), is a bijection onto the D ⁡ ( D − 1) / 2 D(D-1)/2 pairs 1 ⩽ b < a ⩽ D 1\leqslant b<a\leqslant D. The recursion has O ⁡ ( τ 2) O(\tau^{2}) matrices, and all stopped pairs can be enumerated in O ⁡ ( D 2 + τ 4) O(D^{2}+\tau^{4}) arithmetic operations.

The bijection follows by stopping each canonical Euclidean path at its first failed continuation. The matrix count and the explicit integer intervals used for enumeration are proved in Appendix B.2.

## 7 Uniform marker grids and local corrections

Fix one coefficient path P P, one stopped terminal pair ( M, R) (M,R), and its root pair ( a, b) = P ⁡ ( M, R) (a,b)=P(M,R). Put H = a H=a. As a marker t t ranges over [0, H) [0,H), its complete quotient trace changes only at finitely many boundary values. Between consecutive boundaries the same compiled operator applies. Thus the two markers u u and v v divide their square into rectangles on which one operator is valid.

###### Definition 9 (Boundary multiset and true marker rectangles).

Let L L be the number of one-dimensional marker slots for the current coefficient path. Their ordered boundaries form the nondecreasing list 0 = e 0 ⩽ e 1 ⩽ ⋯ ⩽ e L = H 0=e_{0}\leqslant e_{1}\leqslant\cdots\leqslant e_{L}=H. Repetitions are retained, so the same L L is used throughout the coefficient batch even when some boundaries coincide. The true marker slots are I j = [e j, e j + 1) I_{j}=[e_{j},e_{j+1}) for 0 ⩽ j < L 0\leqslant j<L, with product rectangles 𝒞 i ​ j:= I i × I j \mathcal{C}_{ij}:=I_{i}\times I_{j}. A repeated boundary gives an empty slot. Every nonempty I j I_{j} is a maximal interval on which the marker trace, and hence the compiled operator, is fixed.

For a numerical marker t t, let

 | ι ( t) = max { j: 0 ⩽ j < L, e j ⩽ t } \iota(t)=\max\{j:0\leqslant j<L,\ e_{j}\leqslant t\} |  | (17) |

be its true slot.

The true boundaries depend on ( M, R) (M,R), so constructing this partition anew for every stopped pair would be too expensive. We start instead with two uniform grids 𝒢 0 ​ ( P) \mathcal{G}_{0}(P) and 𝒢 1 ​ ( P) \mathcal{G}_{1}(P) of [0, H) [0,H), each with O ⁡ ( τ) O(\tau) intervals. The first grid agrees with the true boundaries at R = 0 R=0, and the second agrees with them at the limiting endpoint R = M R=M. For a given terminal pair we choose the closer reference: ν = 0 \nu=0 when 2 ​ R ⩽ M 2R\leqslant M and ν = 1 \nu=1 otherwise. Every true boundary then moves by less than one uniform cell.

The true boundaries are not exactly the grid lines, but only a few of them can affect the answer inside one uniform cell. The grid construction attaches those candidate boundaries to the cell. If x x is the cell of t t in the selected grid ν \nu, let α ν ​ ( t) \alpha_{\nu}(t) be the number of its candidates lying at or before t t. Computing α ν ​ ( t) \alpha_{\nu}(t) is the small local correction to the uniform partition.

###### Definition 10 (Uniform cell and local correction).

The *marker code*code ν ⁡ ( t):= ( x, α ν ​ ( t)) \operatorname{code}_{\nu}(t):=(x,\alpha_{\nu}(t)) consists of the uniform cell x x and the local correction α ν ​ ( t) \alpha_{\nu}(t).

For two markers, write α u:= α ν ​ ( u) \alpha_{u}:=\alpha_{\nu}(u) and α v:= α ν ​ ( v) \alpha_{v}:=\alpha_{\nu}(v). Their uniform cells ( x, y) (x,y) form a uniform rectangle 𝒱 x ​ y \mathcal{V}_{xy}. Each marker has at most four possible corrections, so 𝒱 x ​ y \mathcal{V}_{xy} needs at most 4 × 4 4\times 4 entries. Entry ( α u, α v) (\alpha_{u},\alpha_{v}) points to the exact true rectangle 𝒞 ι ⁡ ( u), ι ⁡ ( v) \mathcal{C}_{\iota(u),\iota(v)}, its compiled operator, and its terminal data. Denote this menu by ℳ ν, P ​ ( x, y) \mathcal{M}_{\nu,P}(x,y). Figure 1 shows this single local correction step.

###### Theorem 11 (Uniform-grid correction).

For every accepted path, the two uniform grids and their conceptual local correction menus have O ⁡ ( τ 2) O(\tau^{2}) entries and can be constructed in O ⁡ ( τ 2) O(\tau^{2}) time. Inside a uniform cell, at most three true boundaries need to be tested, so α ν ​ ( t) ∈ { 0, 1, 2, 3 } \alpha_{\nu}(t)\in\{0,1,2,3\}. The marker code determines the exact true slot ( 17); hence two marker codes select the exact true rectangle and its operator in constant time.

Appendix B.3 gives the grid construction, the explicit correction formula, and the proof. The main algorithm needs only the resulting constant-size menu.

## 8 Cell operators and small terminal base cases

For every nonempty true slot, Appendix B.3 supplies its marker trace. Pairing two slot lists then composes the reciprocal operator for every true rectangle. The first two subsections compile these cell operators; the third explains how the remaining small terminal staircase is answered, and the final subsection assembles the evaluation of one record. We first record the constant-size algebraic form of one cell operator.

### 8.1 Operator attached to one true marker rectangle

Use the lattice staircase Λ f \Lambda_{f} from ( 10) and its six degree-two moments

 | 𝖫 i ​ j ​ ( f) = ∑ ( t, s) ∈ Λ f t i ​ s j, ( i, j) ∈ 𝒟 2:= { ( 0, 0), ( 1, 0), ( 2, 0), ( 0, 1), ( 1, 1), ( 0, 2) }. \mathsf{L}_{ij}(f)=\sum_{(t,s)\in\Lambda_{f}}t^{i}s^{j},\qquad(i,j)\in\mathscr{D}_{2}:=\{(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)\}. |  |

This is the coordinate order fixed in the definition of 𝐋 ⁡ ( f) \mathbf{L}(f) in Section 3. Their exact integral conversion to the floor-power moments is ( 8); the reverse direction follows by summing 1, s, s 2 1,s,s^{2} over 1 ⩽ s ⩽ f ⁡ ( t) 1\leqslant s\leqslant f(t).

Recall from Section 5 that one normalized reciprocal step writes f ^ ​ ( k) = A ​ k + U + f ′ ​ ( k) \widehat{f}(k)=Ak+U+f^{\prime}(k), where f ′ f^{\prime} is the child floor query. For z ⩾ 0 z\geqslant 0 write Pow i ⁡ ( z) = ∑ t = 0 z t i \operatorname{Pow}_{i}(z)=\sum_{t=0}^{z}t^{i}. The exact one-step lattice identity is as follows. Put k = s − 1 k=s-1. For 0 ⩽ k < h 0\leqslant k<h, the condition s ⩽ f ⁡ ( t) s\leqslant f(t) is equivalent to t ⩾ f ^ ​ ( k) + 1 = A ​ k + U + f ′ ​ ( k) + 1 t\geqslant\widehat{f}(k)+1=Ak+U+f^{\prime}(k)+1. Consequently, for every ( i, j) ∈ 𝒟 2 (i,j)\in\mathscr{D}_{2},

 | 𝖫 i ​ j ​ ( f) = ∑ k = 0 h − 1 ( Pow i ⁡ ( q − 1) − Pow i ⁡ ( A ​ k + U) − ∑ r = 1 f ′ ​ ( k) ( A ​ k + r + U) i) ​ ( k + 1) j. \mathsf{L}_{ij}(f)=\sum_{k=0}^{h-1}\!\left(\operatorname{Pow}_{i}(q-1)-\operatorname{Pow}_{i}(Ak+U)-\sum_{r=1}^{f^{\prime}(k)}(Ak+r+U)^{i}\right)(k+1)^{j}. |  | (18) |

The inner sum is empty when f ′ ​ ( k) = 0 f^{\prime}(k)=0. Thus the child coordinates ( k, r) (k,r) enter the root coordinates through

 | t = A ​ k + r + U, s = k + 1. t=Ak+r+U,\qquad s=k+1. |  | (19) |

The first two terms inside the parentheses in ( 18) are explicit power sums; the inner sum is the affine image of the child with a minus sign. Thus the child-to-root moment map is the signed action induced by the affine coordinate map, and ( 18) completely specifies its one-step action on all six moments.

Because the lengths ( q, h) (q,h) vary across a rectangle, the explicit part of ( 18) is retained as a degree-four polynomial in those two lengths. This fixed polynomial space, the six moment coordinates, and the affine state map are all closed under composition. The exact monomial basis, coefficient counts, and common integral scaling are recorded in Appendix B.4.

###### Definition 12 (Operator of a true marker rectangle).

Fix an accepted coefficient path P P and a true marker rectangle 𝒞 i ​ j = I i × I j \mathcal{C}_{ij}=I_{i}\times I_{j}. The quotient triple at every step is then fixed. Their composition is the *rectangle operator*𝖮𝗉 P; i, j:= ( 𝖠 P; i, j, 𝖴 P; i, j, Π P; i, j) \mathsf{Op}_{P;i,j}:=(\mathsf{A}_{P;i,j},\mathsf{U}_{P;i,j},\Pi_{P;i,j}). It depends only on the path P P and the rectangle indices ( i, j) (i,j), equivalently on the fixed quotient trace. Its stored coefficients do not depend on the numerical terminal pair ( M, R) (M,R), the marker values ( u, v) (u,v), or the root lengths ( q, h) (q,h). Here 𝖠 P; i, j \mathsf{A}_{P;i,j} is the 7 × 7 7\times 7 homogeneous integral matrix mapping the affine query state of Definition 2, augmented by a constant coordinate, from root to terminal; 𝖴 P; i, j \mathsf{U}_{P;i,j} is the 6 × 6 6\times 6 matrix transporting the six lattice moments; and Π P; i, j ​ ( q, h) \Pi_{P;i,j}(q,h) is the six-component polynomial boundary correction.

###### Lemma 13 (Operator closure).

For every fixed coefficient prefix and marker rectangle, let 𝐬 root \mathbf{s}_{\mathrm{root}} and 𝐬 term \mathbf{s}_{\mathrm{term}} be the initial and final affine query states of Definition 2. Then the terminal state and all six root lattice moments have the forms

 | ( 𝐬 term 1) = 𝖠 P; i, j ​ ( 𝐬 root 1), 𝐋 root = 𝖴 P; i, j ​ 𝐋 term + Π P; i, j ​ ( q, h), \binom{\mathbf{s}_{\mathrm{term}}}{1}=\mathsf{A}_{P;i,j}\binom{\mathbf{s}_{\mathrm{root}}}{1},\qquad\mathbf{L}_{\rm root}=\mathsf{U}_{P;i,j}\mathbf{L}_{\mathrm{term}}+\Pi_{P;i,j}(q,h), |  |

where 𝖴 P; i, j \mathsf{U}_{P;i,j} is induced by one affine coordinate map and one sign, and every component of Π P; i, j \Pi_{P;i,j} is a bivariate polynomial of total degree at most four. Both composition and application cost O ⁡ ( 1) O(1) arithmetic operations.

Closure follows from affine substitution in the six degree-two monomials and in the fixed degree-four boundary space. The full proof is in Appendix B.4.

### 8.2 Compiling the cell operators

Recall that L L is the number of one-dimensional true marker slots for the current coefficient path. The cell operator depends on P P and the two slot indices, not on the numerical terminal pair ( M, R) (M,R); all stopped pairs on the path reuse it. Pairing the L L slots of u u with the L L slots of v v gives exactly L 2 L^{2} true rectangles and hence L 2 L^{2} cell operators. Compile them by sharing their common trace prefixes. At each Euclidean step, marker slots with the same trace so far form one group. For every pair of groups, extend the current operator once by their next quotient triple ( A, U, V) (A,U,V) from Definition 3. When the traces finish, every pair ( I i, I j) (I_{i},I_{j}) has its operator 𝖮𝗉 P; i, j \mathsf{Op}_{P;i,j}.

###### Lemma 14 (Shared-prefix compilation bound).

For a coefficient path with L L true marker slots, all L 2 L^{2} cell operators can be compiled in O ⁡ ( L 2) O(L^{2}) arithmetic operations and stored in O ⁡ ( L 2) O(L^{2}) arithmetic words.

The proof, based on the growth of the continuants along the prefix tree, is in Appendix B.5.

For the analysis, attach the constant-size correction menu of Theorem 11 to every uniform rectangle. Its entries identify the required cell operator and affine terminal data. In the reference implementation, equations ( 44) and ( 45) compute the two slot indices on demand, after which the corresponding member of the L 2 L^{2} operator array is accessed directly. It suffices to retain these operators and the grid prefix data while processing the stopped pairs of the current path and to discard them afterward; together they require O ⁡ ( τ 2) O(\tau^{2}) path-local words.

### 8.3 Small-modulus terminal lookup

The compiled operator removes the long common quotient trace but leaves a small terminal staircase. If its width or height is zero, or if R = 0 R=0, all six moments vanish. If M ⩽ κ M\leqslant\kappa, the terminal query is read from the table directly. Otherwise Lemma 7 permits one additional reciprocal cycle, whose child coefficients are ( R, M mod R) (R,M\bmod R) and are both below κ \kappa; after the child lookup, identity ( 18) lifts its moments back to the original terminal query.

The lookup table stores one normalized staircase for every coprime pair of coefficients at most κ \kappa. The stored staircase has zero intercept, and we keep prefixes of the six floor-power moments in ( 7) over two consecutive periods. Equation ( 8) then gives the six terminal lattice moments required by the compiled operator.

A query whose coefficients are at most κ \kappa is reduced to this stored form in three constant-time steps. First divide its two coefficients by their greatest common divisor. Second, use one precomputed modular inverse to turn the intercept into a cyclic shift of the zero-intercept staircase; this shift changes only the origin and adds a constant to the floor values. Third, split the requested length into complete periods and one final fragment. The fragment uses at most two stored prefixes, while all complete periods are combined by ordinary power sums.

Horizontal and vertical shifts act affinely on the same six-moment family, so the shifted prefixes are converted back by one fixed constant-size calculation. Thus the table contains no separate copy for every intercept: all intercepts of one reduced coefficient pair reuse the same zero-intercept data. The exact shift identities are proved in Appendix B.5.1.

###### Lemma 15 (Periodic table size).

The reduced periodic table, including the divisor lookup described in the appendix, has O ⁡ ( κ 3) O(\kappa^{3}) entries, is constructed in O ⁡ ( κ 3) O(\kappa^{3}) arithmetic operations, and answers every terminal query in O ⁡ ( 1) O(1) operations.

The construction and size count are also proved in Appendix B.5.1.

### 8.4 Evaluation of one record

This subsection applies to a long record, so its root length satisfies q > 5 ​ τ q>5\tau. Let 𝐬 root = ( a, b, q, h, u, v) 𝖳 \mathbf{s}_{\mathrm{root}}=(a,b;q,h;u,v)^{\mathsf{T}} be its affine query state from Definition 2. Select the first uniform grid when 2 ​ R ⩽ M 2R\leqslant M and the second one otherwise, and compute code ν ⁡ ( u) = ( x, α u) \operatorname{code}_{\nu}(u)=(x,\alpha_{u}) and code ν ⁡ ( v) = ( y, α v) \operatorname{code}_{\nu}(v)=(y,\alpha_{v}). The menu entry ℳ ν, P ​ ( x, y) ​ [α u, α v] \mathcal{M}_{\nu,P}(x,y)[\alpha_{u},\alpha_{v}] returns the exact true indices ( i, j) (i,j) and the operator 𝖮𝗉 P; i, j \mathsf{Op}_{P;i,j}. Write the terminal state as 𝐬 term = ( M, R, q term, h term, u term, v term) 𝖳 \mathbf{s}_{\mathrm{term}}=(M,R;q_{\mathrm{term}},h_{\mathrm{term}};u_{\mathrm{term}},v_{\mathrm{term}})^{\mathsf{T}}. The affine component of the stored operator supplies it in homogeneous coordinates as ( 𝐬 term 1) = 𝖠 P; i, j ​ ( 𝐬 root 1) \binom{\mathbf{s}_{\mathrm{term}}}{1}=\mathsf{A}_{P;i,j}\binom{\mathbf{s}_{\mathrm{root}}}{1}. If R = 0 R=0, q term = 0 q_{\mathrm{term}}=0, or h term = 0 h_{\mathrm{term}}=0, the terminal moments vanish. Otherwise Lemma 7 permits at most one additional reciprocal step, and Lemma 15 returns in O ⁡ ( 1) O(1) operations the six lattice moments 𝐋 term \mathbf{L}_{\mathrm{term}} of the original terminal query, including the lift through this optional step. Finally, 𝐋 root = 𝖴 P; i, j ​ 𝐋 term + Π P; i, j ​ ( q, h) \mathbf{L}_{\rm root}=\mathsf{U}_{P;i,j}\mathbf{L}_{\mathrm{term}}+\Pi_{P;i,j}(q,h). First convert 𝐋 root \mathbf{L}_{\rm root} to the six required Φ \Phi -moments by ( 8). Then Equations ( 23)–( 26) add the record to the layer accumulator. Thus a long record is processed and accumulated immediately during the visit to its coefficient path.

## 9 Short-query fallback

Lemma 1 emits at most one recursive floor query for each coefficient pair. In the normalized notation of ( 9), it is ⌊ ( b ​ t + β) / a ⌋ \left\lfloor(bt+\beta)/a\right\rfloor for 0 ⩽ t < q 0\leqslant t<q, where β ≡ N − b ​ q ( mod a) \beta\equiv N-bq\pmod{a} and 0 ⩽ β < a 0\leqslant\beta<a. All other terms of the moment reduction are explicit power-sum expressions. Call a nonempty query *short*when 0 < q ⩽ 5 ​ τ 0<q\leqslant 5\tau, with τ \tau from ( 14). Every short query is sent directly to the pointwise recursion; every remaining nonempty query follows its compiled coefficient path to the terminal table.

A short query is evaluated without a precompiled operator by the direct six-floor-moment recurrence ( 53)–( 54). It returns 𝚽 \boldsymbol{\Phi} itself, so no intermediate lattice-moment conversion is needed. The base cases q = 0 q=0, b = 0 b=0, and zero floor height return six zeros. Every other call first extracts the integral coefficient and intercept parts; the normalized reciprocal branch then exchanges the two positive coefficients. Thus the modulus sequence is the ordinary Euclidean sequence and the recursion terminates. The executable formulas and exact recursive argument order are given in Appendix B.4.

###### Theorem 16 (Short-query bound).

In a layer of size N N, with the layer scale D D and path threshold τ \tau from ( 14), there are O ⁡ ( D ​ τ) = O ⁡ ( N 3 / 4) O(D\tau)=O(N^{3/4}) short queries, and their total evaluation time is

 | T short = O ⁡ ( D ​ τ ​ log ⁡ ( 2 + τ)) = O ⁡ ( N 3 / 4 ​ log ⁡ N) = o ⁡ ( N). T_{\rm short}=O(D\tau\log(2+\tau))=O(N^{3/4}\log N)=o(N). |  |

Moreover, every query whose floor height would become zero before the end of its compiled path is short. Hence every nonempty non-short query can safely follow the entire compiled path.

For a query that would terminate along its compiled path, reversing the length recurrence bounds both root lengths by 5 ​ τ 5\tau. Counting all roots with 0 < q ⩽ 5 ​ τ 0<q\leqslant 5\tau gives O ⁡ ( D ​ τ) O(D\tau) queries, and their pointwise-recursion depth is O ⁡ ( log ⁡ D) = O ⁡ ( log ⁡ ( 2 + τ)) O(\log D)=O(\log(2+\tau)). The full continuant calculation is in Appendix B.6.

## 10 Assembling the complete O ⁡ ( n ​ log ⁡ n) O(n\log n) algorithm

The preceding sections provide all reusable components: the geometric reduction creates one floor-moment record for each direction pair, the coefficient path and uniform-grid correction choose its compiled operator, and the small-modulus table supplies the terminal moments. Their assembly has two levels.

Inside one divisor layer, enumerate every direction pair and immediately add the part of its contribution given by explicit power-sum expressions. A nonempty staircase also emits one record. Records with the same coefficient path form one batch. For that batch construct the true marker slots, compile the cell operators through their shared prefix tree, and prepare the two uniform grids and their prefix data. Each long record then selects one exact cell operator, and its small terminal staircase is answered by the periodic table. Short records are handled by the pointwise recurrence. The returned six moments supply the deferred part of the geometric contribution. After all records of the path have been processed, discard its operators and grid data.

Outside the layer routine, quotient blocking groups all divisors that produce the same layer size. Three weighted Möbius prefixes provide the weights of each block, and one read-only periodic table is reused by every layer. Thus each distinct layer is constructed once and its three coefficients are added to the final answer with the corresponding block weights.

The exact two-stage contribution formulas, the weighted Möbius recurrence, the cone-visitor pseudocode, a worked end-to-end record, and the formal correctness chain are given in Appendix B.7. All expensive objects are shared at the path or global level, so processing one long record after its path is known takes constant time.

## 11 Linear layer and main theorem

###### Theorem 17 (Linear divisor layer).

The coefficient triple ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) (A(N),B(N),C(N)) can be computed exactly in O ⁡ ( N) O(N) arithmetic operations and O ⁡ ( N 3 / 4) O(N^{3/4}) arithmetic words of working memory.

With D = Θ ⁡ ( N 1 / 2) D=\Theta(N^{1/2}) and τ, κ = Θ ⁡ ( N 1 / 4) \tau,\kappa=\Theta(N^{1/4}), record generation and application cost O ⁡ ( D 2) O(D^{2}), constructing all cell operators and correction data costs O ⁡ ( τ 4) O(\tau^{4}), the terminal table costs O ⁡ ( κ 3) O(\kappa^{3}), and short queries are lower order. Hence the time is O ⁡ ( N) O(N); the terminal table dominates memory at O ⁡ ( N 3 / 4) O(N^{3/4}). The complete cost table and the reason the three scales cannot all be decreased are in Appendix B.8.

###### Lemma 18 (Distinct-layer sum).

Let 𝒱 n = { ⌊ n / d ⌋: 1 ⩽ d ⩽ n } \mathcal{V}_{n}=\{\left\lfloor n/d\right\rfloor:1\leqslant d\leqslant n\} be the layer sizes evaluated after quotient blocking. Then ∑ N ∈ 𝒱 n N = O ⁡ ( n ​ log ⁡ n) \sum_{N\in\mathcal{V}_{n}}N=O(n\log n).

###### Proof.

Put D 0 = ⌊ n ⌋ D_{0}=\left\lfloor\sqrt{n}\right\rfloor. Quotients at most D 0 D_{0} contribute O ⁡ ( D 0 2) = O ⁡ ( n) O(D_{0}^{2})=O(n). Every larger distinct quotient has the form ⌊ n / d ⌋ \left\lfloor n/d\right\rfloor with d ⩽ D 0 d\leqslant D_{0}, and ∑ d ⩽ D 0 ⌊ n / d ⌋ = O ⁡ ( n ​ log ⁡ n) \sum_{d\leqslant D_{0}}\left\lfloor n/d\right\rfloor=O(n\log n). ∎

###### Theorem 19 (Main theorem).

The exact number F ⁡ ( n) F(n) of lattice rectangles in an n × n n\times n square grid can be computed in O ⁡ ( n ​ log ⁡ n) O(n\log n) arithmetic operations and O ⁡ ( n 3 / 4) O(n^{3/4}) arithmetic words of working memory.

###### Proof.

Apply Theorem 17 inside the divisor-layer formula ( 5). Quotient blocking evaluates each N ∈ 𝒱 n N\in\mathcal{V}_{n} once, and Lemma 18 gives O ⁡ ( n ​ log ⁡ n) O(n\log n) total layer work.

The three weighted Möbius prefixes in ( 69) take O ⁡ ( n 2 / 3) O(n^{2/3}) time and storage by a cutoff sieve followed by quotient-block recurrences; the calculation is given in Appendix B.8.1. This is lower order, while sequential layer processing uses O ⁡ ( n 3 / 4) O(n^{3/4}) peak memory. ∎

###### Lemma 20 (One-value operand size).

Every exact integer stored or multiplied by the one-value algorithm has O ⁡ ( log ⁡ n) O(\log n) bits.

All coordinates are polynomially bounded in n n, and composition has fixed dimension and logarithmic depth. The coefficient-growth calculation is in Appendix B.8.

## 12 Experiments

We compare the O ⁡ ( n ​ log ⁡ n) O(n\log n) algorithm with the exact O ⁡ ( n ​ log 2 ​ n) O(n\log^{2}n) divisor-layer implementation from the public code repository on an AMD Ryzen 9 5950X running Windows. Both implementations use the same experimental interface and return exactly one prescribed value F ⁡ ( n) F(n) per invocation. GCC 8.1.0 from MinGW-w64 compiled both programs with -O3 -DNDEBUG -march=native -flto.

At each n = 2 k n=2^{k}, both programs are run ten times. Every timed computation starts with an empty auxiliary cache and includes all preprocessing performed by the corresponding implementation; only output is excluded. Both processes are pinned to a fixed logical processor, run at high priority under the Windows high-performance power plan.

Figure 3 reports the arithmetic means of the ten elapsed times at n = 2 k n=2^{k}. In the right panel, each running time is normalized by the corresponding theoretical complexity; values are in seconds.

2 10 2^{10} 2 11 2^{11} 2 12 2^{12} 2 13 2^{13} 2 14 2^{14} 2 15 2^{15} 2 16 2^{16} 2 17 2^{17} 2 18 2^{18} 2 19 2^{19} 2 20 2^{20} 2 21 2^{21} 2 22 2^{22} 2 23 2^{23} 2 24 2^{24} 2 25 2^{25} 10 − 3 10^{-3} 10 − 2 10^{-2} 10 − 1 10^{-1} 10 0 10^{0} 10 1 10^{1} 10 2 10^{2} grid size n = 2 k n=2^{k} running time (seconds) Running times of the algorithms O ⁡ ( n ​ log 2 2 ​ n) O(n\log_{2}^{2}n) O ⁡ ( n ​ log 2 ​ n) O(n\log_{2}n) 2 10 2^{10} 2 11 2^{11} 2 12 2^{12} 2 13 2^{13} 2 14 2^{14} 2 15 2^{15} 2 16 2^{16} 2 17 2^{17} 2 18 2^{18} 2 19 2^{19} 2 20 2^{20} 2 21 2^{21} 2 22 2^{22} 2 23 2^{23} 2 24 2^{24} 2 25 2^{25} 3 3 10 10 30 30 100 100 grid size n = 2 k n=2^{k} normalized running time (ns) Normalized running times O ⁡ ( n ​ log 2 2 ​ n) O(n\log_{2}^{2}n) O ⁡ ( n ​ log 2 ​ n) O(n\log_{2}n)

Figure 3: Mean one-value running times over ten runs on logarithmic scales. Left: elapsed time. Right: time normalized by the corresponding theoretical complexity.

On larger inputs, the broadly stable normalized curves support the predicted scaling. Small residual high-end fluctuations may reflect growing working sets crossing cache-capacity thresholds. Despite its lower O ⁡ ( n ​ log ⁡ n) O(n\log n) complexity, the new algorithm has a larger constant from storing and applying relatively heavy compiled kernels; its lower asymptotic growth compensates on sufficiently large inputs.

## 13 Reproducibility

Links to the GitHub repository containing the reference implementations, build instructions, and experiment scripts will be added in the next version.

## 14 Future work

The reference C++ implementation is single-threaded. Divisor layers and coefficient paths are independent, but a parallel version should share the Möbius prefixes, marker data, and terminal table among workers.

The terminal periodic table causes the O ⁡ ( n 3 / 4) O(n^{3/4}) working-memory term; the live data for one coefficient path is smaller. Achieving the same O ⁡ ( n ​ log ⁡ n) O(n\log n) arithmetic bound with a smaller terminal representation remains open, perhaps by evaluating selected periodic prefixes on demand while preserving enough sharing to avoid restoring a logarithmic factor in time.

## 15 Conclusion

For a prescribed n × n n\times n grid, the exact lattice-rectangle count is computable in O ⁡ ( n ​ log ⁡ n) O(n\log n) arithmetic operations and O ⁡ ( n 3 / 4) O(n^{3/4}) arithmetic words of working memory. The method compiles shared prefixes of weighted Euclidean floor-moment recurrences, uses uniform marker grids to locate queries, and resolves constant-size local boundary corrections. Its operands have O ⁡ ( log ⁡ n) O(\log n) bits, and the implementation exhibits the predicted n ​ log ⁡ n n\log n scaling over the tested range.

## Appendix A Geometric and moment identities

### A.1 Full half-domain moment reduction

This section supplies the explicit formulas used by Lemma 1. For the strict non-diagonal contribution, the direction pair ( a, b) (a,b) and the side pair ( x, y) (x,y) both have decreasing positive coordinates. The constraint a ​ x + b ​ y ⩽ N ax+by\leqslant N and the vector 𝐰 a, b ​ ( x, y) \mathbf{w}_{a,b}(x,y) are unchanged when the two pairs are exchanged, and the multiplier is four. Pairing a < x a<x with a > x a>x gives

 | ∑ a > b ⩾ 1, x > y ⩾ 1 a ​ x + b ​ y ⩽ N 𝐰 a, b ​ ( x, y) = ∑ a > b ⩾ 1, x > y ⩾ 1 a ⩽ x, a ​ x + b ​ y ⩽ N 𝐰 a, b ​ ( x, y) − ∑ a > b ⩾ 1, x > y ⩾ 1 a = x, a ​ x + b ​ y ⩽ N 𝐰 a, b ​ ( x, y). 4\!\sum_{\begin{subarray}{c}a>b\geqslant 1,\ x>y\geqslant 1\\ ax+by\leqslant N\end{subarray}}\mathbf{w}_{a,b}(x,y)=8\!\sum_{\begin{subarray}{c}a>b\geqslant 1,\ x>y\geqslant 1\\ a\leqslant x,\ ax+by\leqslant N\end{subarray}}\mathbf{w}_{a,b}(x,y)-4\!\sum_{\begin{subarray}{c}a>b\geqslant 1,\ x>y\geqslant 1\\ a=x,\ ax+by\leqslant N\end{subarray}}\mathbf{w}_{a,b}(x,y). |  | (20) |

In the first sum on the right, a ​ x ⩽ N ax\leqslant N and a ⩽ x a\leqslant x, hence a ⩽ D = ⌊ N ⌋ a\leqslant D=\left\lfloor\sqrt{N}\right\rfloor.

Fix ( a, b) (a,b) with a ⩽ D a\leqslant D. For a fixed y y, the admissible x x form the interval

 | x min ​ ( y) ⩽ x ⩽ x max ​ ( y), x max ​ ( y) = ⌊ N − b ​ y a ⌋, x min ​ ( y) = { a, y < a, y + 1, y ⩾ a. x_{\min}(y)\leqslant x\leqslant x_{\max}(y),\qquad x_{\max}(y)=\left\lfloor\frac{N-by}{a}\right\rfloor,\qquad x_{\min}(y)=\begin{cases}a,&y<a,\\ y+1,&y\geqslant a.\end{cases} |  |

Put

 | q sq = ⌊ N − a 2 b ⌋, q = { q sq, q sq < a − 1, max ⁡ { a − 1, ⌊ N − a a + b ⌋ }, q sq ⩾ a − 1. q_{\mathrm{sq}}=\left\lfloor\frac{N-a^{2}}{b}\right\rfloor,\qquad q=\begin{cases}q_{\mathrm{sq}},&q_{\mathrm{sq}}<a-1,\\ \displaystyle\max\!\left\{a-1,\left\lfloor\frac{N-a}{a+b}\right\rfloor\right\},&q_{\mathrm{sq}}\geqslant a-1.\end{cases} |  |

For y < a y<a, nonemptiness is y ⩽ q sq y\leqslant q_{\mathrm{sq}}; if q sq ⩾ a − 1 q_{\mathrm{sq}}\geqslant a-1, the remaining condition is ( a + b) ​ y + a ⩽ N (a+b)y+a\leqslant N. Hence the admissible y y form exactly 1 ⩽ y ⩽ q 1\leqslant y\leqslant q.

For s ⩾ 0 s\geqslant 0 define Σ s ​ ( z) = ∑ 1 ⩽ k ⩽ z k s \Sigma_{s}(z)=\sum_{1\leqslant k\leqslant z}k^{s}, with value zero for z ⩽ 0 z\leqslant 0. For i + j ⩽ 2 i+j\leqslant 2 the required half-domain moments are

 | J i ​ j ​ ( a, b, N) = ∑ y = 1 q y j ​ [Σ i ​ ( ⌊ N − b ​ y a ⌋) − Σ i ​ ( x min ​ ( y) − 1)]. J_{ij}(a,b;N)=\sum_{y=1}^{q}y^{j}\left[\Sigma_{i}\!\left(\left\lfloor\frac{N-by}{a}\right\rfloor\right)-\Sigma_{i}(x_{\min}(y)-1)\right]. |  | (21) |

Write N − b ​ q = η ​ a + β N-bq=\eta a+\beta, 0 ⩽ β < a 0\leqslant\beta<a, and form the single query

 | f ⁡ ( t) = ⌊ b ​ t + β a ⌋, 0 ⩽ t < q. f(t)=\left\lfloor\frac{bt+\beta}{a}\right\rfloor,\qquad 0\leqslant t<q. |  | (22) |

Reversing y = q − t y=q-t gives x max ​ ( q − t) = η + f ⁡ ( t) x_{\max}(q-t)=\eta+f(t). Write Φ i ​ j = Φ i ​ j ​ ( f) \Phi_{ij}=\Phi_{ij}(f) for the six moments in ( 7). Then the upper-limit sums are

 | J 00 upper \displaystyle J^{\mathrm{upper}}_{00} | = q ​ η + Φ 01, \displaystyle=q\eta+\Phi_{01}, |  |

 | J 01 upper \displaystyle J^{\mathrm{upper}}_{01} | = η ​ Σ 1 ​ ( q) + q ​ Φ 01 − Φ 11, \displaystyle=\eta\Sigma_{1}(q)+q\Phi_{01}-\Phi_{11}, |  |

 | J 02 upper \displaystyle J^{\mathrm{upper}}_{02} | = η ​ Σ 2 ​ ( q) + q 2 ​ Φ 01 − 2 ​ q ​ Φ 11 + Φ 21, \displaystyle=\eta\Sigma_{2}(q)+q^{2}\Phi_{01}-2q\Phi_{11}+\Phi_{21}, |  |

 | J 10 upper \displaystyle J^{\mathrm{upper}}_{10} | = q ⁡ ( η 2 + η) + ( 2 ​ η + 1) ​ Φ 01 + Φ 02 2, \displaystyle=\frac{q(\eta^{2}+\eta)+(2\eta+1)\Phi_{01}+\Phi_{02}}{2}, |  |

 | J 11 upper \displaystyle J^{\mathrm{upper}}_{11} | = ( η 2 + η) ​ Σ 1 ​ ( q) + ( 2 ​ η + 1) ​ ( q ​ Φ 01 − Φ 11) + q ​ Φ 02 − Φ 12 2, \displaystyle=\frac{(\eta^{2}+\eta)\Sigma_{1}(q)+(2\eta+1)(q\Phi_{01}-\Phi_{11})+q\Phi_{02}-\Phi_{12}}{2}, |  |

 | J 20 upper \displaystyle J^{\mathrm{upper}}_{20} | = q ⁡ ( 2 ​ η 3 + 3 ​ η 2 + η) + ( 6 ​ η 2 + 6 ​ η + 1) ​ Φ 01 + ( 6 ​ η + 3) ​ Φ 02 + 2 ​ Φ 03 6. \displaystyle=\frac{q(2\eta^{3}+3\eta^{2}+\eta)+(6\eta^{2}+6\eta+1)\Phi_{01}+(6\eta+3)\Phi_{02}+2\Phi_{03}}{6}. |  | (23) |

The lower-limit sums are

 | J i ​ j lower = Σ i ​ ( a − 1) ​ Σ j ​ ( min ⁡ { q, a − 1 }) + ∑ y = a q y j ​ Σ i ​ ( y), J i ​ j = J i ​ j upper − J i ​ j lower. J^{\mathrm{lower}}_{ij}=\Sigma_{i}(a-1)\Sigma_{j}(\min\{q,a-1\})+\sum_{y=a}^{q}y^{j}\Sigma_{i}(y),\qquad J_{ij}=J^{\mathrm{upper}}_{ij}-J^{\mathrm{lower}}_{ij}. |  | (24) |

The last sum is empty when q < a q<a. Since i + j ⩽ 2 i+j\leqslant 2, y j ​ Σ i ​ ( y) y^{j}\Sigma_{i}(y) is a polynomial of degree at most three and is evaluated by Σ 0, …, Σ 3 \Sigma_{0},\ldots,\Sigma_{3} in O ⁡ ( 1) O(1) operations.

For this fixed pair, put

 | 𝒜 a, b ​ ( J) = ( J 00, ( a + b) ​ ( J 10 + J 01), a ​ b ​ ( J 20 + J 02) + ( a 2 + b 2) ​ J 11). \mathcal{A}_{a,b}(J)=\left(J_{00},(a+b)(J_{10}+J_{01}),ab(J_{20}+J_{02})+(a^{2}+b^{2})J_{11}\right). |  | (25) |

The first sum on the right of ( 20) contributes

 | 8 ​ 𝒜 a, b ​ ( J). 8\mathcal{A}_{a,b}(J). |  | (26) |

The equality boundary a = x a=x has 1 ⩽ y ⩽ y ⋆ 1\leqslant y\leqslant y_{\star}, where y ⋆ = min ⁡ { a − 1, q sq } y_{\star}=\min\{a-1,q_{\mathrm{sq}}\}. Its subtracted vector is

 | E a, b = 4 ​ ( y ⋆, ( a + b) ​ ( y ⋆ ​ a + Σ 1 ​ ( y ⋆)), a ​ b ​ ( y ⋆ ​ a 2 + Σ 2 ​ ( y ⋆)) + ( a 2 + b 2) ​ a ​ Σ 1 ​ ( y ⋆)). E_{a,b}=4\left(y_{\star},(a+b)(y_{\star}a+\Sigma_{1}(y_{\star})),ab(y_{\star}a^{2}+\Sigma_{2}(y_{\star}))+(a^{2}+b^{2})a\Sigma_{1}(y_{\star})\right). |  | (27) |

It remains to add the side diagonal x = y = s x=y=s, which has multiplicity two. For c = a + b c=a+b, the number of pairs a > b ⩾ 1 a>b\geqslant 1 with sum c c is ⌊ ( c − 1) / 2 ⌋ \left\lfloor(c-1)/2\right\rfloor. Put

 | Diag t ( m) = ∑ c = 3 m c t ⌊ c − 1 2 ⌋, t = 0, 1, 2. \operatorname{Diag}_{t}(m)=\sum_{c=3}^{m}c^{t}\left\lfloor\frac{c-1}{2}\right\rfloor,\qquad t=0,1,2. |  |

For k + = ⌊ m / 2 ⌋ k_{+}=\left\lfloor m/2\right\rfloor and k − = ⌊ ( m − 1) / 2 ⌋ k_{-}=\left\lfloor(m-1)/2\right\rfloor, separating even and odd c c gives

 | Diag 0 ⁡ ( m) \displaystyle\operatorname{Diag}_{0}(m) | = Σ 1 ​ ( k +) − k + + Σ 1 ​ ( k −), \displaystyle=\Sigma_{1}(k_{+})-k_{+}+\Sigma_{1}(k_{-}), |  |

 | Diag 1 ⁡ ( m) \displaystyle\operatorname{Diag}_{1}(m) | = 2 ​ ( Σ 2 ​ ( k +) − Σ 1 ​ ( k +)) + 2 ​ Σ 2 ​ ( k −) + Σ 1 ​ ( k −), \displaystyle=2(\Sigma_{2}(k_{+})-\Sigma_{1}(k_{+}))+2\Sigma_{2}(k_{-})+\Sigma_{1}(k_{-}), |  |

 | Diag 2 ⁡ ( m) \displaystyle\operatorname{Diag}_{2}(m) | = 4 ​ ( Σ 3 ​ ( k +) − Σ 2 ​ ( k +)) + 4 ​ Σ 3 ​ ( k −) + 4 ​ Σ 2 ​ ( k −) + Σ 1 ​ ( k −). \displaystyle=4(\Sigma_{3}(k_{+})-\Sigma_{2}(k_{+}))+4\Sigma_{3}(k_{-})+4\Sigma_{2}(k_{-})+\Sigma_{1}(k_{-}). |  | (28) |

Therefore the complete diagonal contribution is

 | 𝒟 ⁡ ( N) = ∑ s = 1 ⌊ N / 3 ⌋ ( 2 ​ Diag 0 ⁡ ( ⌊ N / s ⌋), 4 ​ s ​ Diag 1 ⁡ ( ⌊ N / s ⌋), 2 ​ s 2 ​ Diag 2 ⁡ ( ⌊ N / s ⌋)). \mathcal{D}(N)=\sum_{s=1}^{\left\lfloor N/3\right\rfloor}\left(2\operatorname{Diag}_{0}(\left\lfloor N/s\right\rfloor),4s\operatorname{Diag}_{1}(\left\lfloor N/s\right\rfloor),2s^{2}\operatorname{Diag}_{2}(\left\lfloor N/s\right\rfloor)\right). |  | (29) |

It takes O ⁡ ( N) O(N) operations and requires no floor query. Combining all pieces,

 | ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) = 𝒟 ⁡ ( N) + ∑ 1 ⩽ b < a ⩽ D ( 8 ​ 𝒜 a, b ​ ( J) − E a, b). (A(N),B(N),C(N))=\mathcal{D}(N)+\sum_{1\leqslant b<a\leqslant D}\left(8\mathcal{A}_{a,b}(J)-E_{a,b}\right). |  | (30) |

This proves Lemma 1, including its generation bound.

## Appendix B Technical proofs for Euclidean batching

### B.1 Derivation of one complete Euclidean cycle

The reciprocal query ( 11) is not yet normalized because its coefficient a a can exceed its modulus b b. Divide the three quantities that control the next step by b b:

 | a = A ​ b + b ′, u = U ​ b + β ′, v = V ​ b + γ, a=Ab+b^{\prime},\qquad u=Ub+\beta^{\prime},\qquad v=Vb+\gamma, |  | (31) |

where

 | A = ⌊ a / b ⌋, U = ⌊ u / b ⌋, V = ⌊ v / b ⌋, 0 ⩽ b ′, β ′, γ < b. A=\left\lfloor a/b\right\rfloor,\qquad U=\left\lfloor u/b\right\rfloor,\qquad V=\left\lfloor v/b\right\rfloor,\qquad 0\leqslant b^{\prime},\beta^{\prime},\gamma<b. |  |

Then

 | f ^ ​ ( k) = A ​ k + U + f ′ ​ ( k), f ′ ​ ( k) = ⌊ b ′ ​ k + β ′ b ⌋, 0 ⩽ k < h. \widehat{f}(k)=Ak+U+f^{\prime}(k),\qquad f^{\prime}(k)=\left\lfloor\frac{b^{\prime}k+\beta^{\prime}}{b}\right\rfloor,\qquad 0\leqslant k<h. |  | (32) |

The polynomial part A ​ k + U Ak+U is handled explicitly by the six-moment affine formulas. The only recursive child is f ′ f^{\prime}, with

 | a ′ = b, b ′ = a − A ​ b, β ′ = u − U ​ b, q ′ = h. a^{\prime}=b,\qquad b^{\prime}=a-Ab,\qquad\beta^{\prime}=u-Ub,\qquad q^{\prime}=h. |  |

Renormalizing it gives

 | u ′ = a ′ − β ′ − 1 = ( U + 1) ​ b − u − 1, v ′ = b − γ − 1 = ( V + 1) ​ b − v − 1. u^{\prime}=a^{\prime}-\beta^{\prime}-1=(U+1)b-u-1,\qquad v^{\prime}=b-\gamma-1=(V+1)b-v-1. |  |

Finally, substituting b ⁡ ( q − 1) + β = a ​ h + v b(q-1)+\beta=ah+v in the endpoint formula for f ′ f^{\prime} yields

 | h ′ = q − A ​ h − ( U + V + 2 − A). h^{\prime}=q-Ah-(U+V+2-A). |  |

Together these identities give the cycle ( 13).

### B.2 Coefficient cones and terminal coordinates

###### Proof of Lemma 7.

The assertion is immediate if R = 0 R=0. Otherwise suppose M > κ M>\kappa and let A = ⌊ M / R ⌋ A=\left\lfloor M/R\right\rfloor. If ( π 11, π 12) (\pi_{11},\pi_{12}) is the first row of P P, rejection of the next child gives

 | π 11 ​ A + π 12 > τ. \pi_{11}A+\pi_{12}>\tau. |  |

For P = I P=I this is simply A > τ A>\tau. For a nonempty continuant product, its first row dominates the second row componentwise, so an overflowing entry in P ​ Q ​ ( A) PQ(A) implies the same displayed inequality. Therefore

 | a = π 11 ​ M + π 12 ​ R ⩾ ( π 11 ​ A + π 12) ​ R > τ ​ R. a=\pi_{11}M+\pi_{12}R\geqslant(\pi_{11}A+\pi_{12})R>\tau R. |  |

Since a ⩽ D ⩽ τ ​ κ a\leqslant D\leqslant\tau\kappa, it follows that R < κ R<\kappa. The next Euclidean modulus is R R. ∎

###### Proof of Lemma 8.

Starting from any root pair, follow its canonical Euclidean divisions. Enter a child whenever the current terminal pair has M > τ M>\tau and R > 0 R>0 and the child matrix is accepted. The first failed condition is uniquely one of the three stop conditions in Section 6. Conversely each stopped pair reverses through P P to one root pair. Unimodularity makes ( M, R) (M,R) unique, proving the bijection.

For the matrix count, an accepted nonidentity matrix has nonnegative entries, determinant ± 1 \pm 1, and entries at most τ \tau. Write its rows as ( p 1, p 2) (p_{1},p_{2}) and ( r 1, r 2) (r_{1},r_{2}). The first row is primitive, and the continuant inequalities give

 | 0 ⩽ r 1 ⩽ p 1, 0 ⩽ r 2 ⩽ p 2. 0\leqslant r_{1}\leqslant p_{1},\qquad 0\leqslant r_{2}\leqslant p_{2}. |  | (33) |

Fix ( p 1, p 2) (p_{1},p_{2}) and a determinant sign δ \delta. If ( r 1, 0, r 2, 0) (r_{1,0},r_{2,0}) is one solution of p 1 ​ r 2 − p 2 ​ r 1 = δ p_{1}r_{2}-p_{2}r_{1}=\delta, every solution is

 | ( r 1, r 2) = ( r 1, 0, r 2, 0) + t ⁡ ( p 1, p 2), t ∈ ℤ. (r_{1},r_{2})=(r_{1,0},r_{2,0})+t(p_{1},p_{2}),\qquad t\in\mathbb{Z}. |  |

For a nonidentity path both p 1 p_{1} and p 2 p_{2} are positive. Each inequality in ( 33) therefore restricts t t to a closed interval of length at most one, so their intersection contains at most two integers. There are O ⁡ ( τ 2) O(\tau^{2}) possible first rows and two determinant signs. A recursion word is also recovered uniquely from its matrix. Indeed, if P = P − ​ Q ​ ( A) P=P^{-}Q(A) is nonidentity, then

 | A = min ⁡ { ⌊ p 1 / p 2 ⌋, ⌊ r 1 / r 2 ⌋ }, A=\min\!\left\{\left\lfloor p_{1}/p_{2}\right\rfloor,\left\lfloor r_{1}/r_{2}\right\rfloor\right\}, |  |

where a quotient with zero denominator is omitted, and P − P^{-} has first column ( p 2, r 2) 𝖳 (p_{2},r_{2})^{\mathsf{T}} and second column ( p 1 − A ​ p 2, r 1 − A ​ r 2) 𝖳 (p_{1}-Ap_{2},r_{1}-Ar_{2})^{\mathsf{T}}. Repeating this step reaches I I. Thus a matrix is not counted through two recursion words. Including I I gives O ⁡ ( τ 2) O(\tau^{2}) nodes.

The small-modulus piece tests fewer than τ 2 \tau^{2} pairs per node and therefore costs O ⁡ ( τ 4) O(\tau^{4}). The zero-remainder piece is one integer interval in M M. For the overflow piece put A stop = ext ⁡ ( P) + 1 A_{\rm stop}=\operatorname{ext}(P)+1. For every

 | 1 ⩽ R ⩽ ⌊ D π 11 ​ A stop + π 12 ⌋, 1\leqslant R\leqslant\left\lfloor\frac{D}{\pi_{11}A_{\rm stop}+\pi_{12}}\right\rfloor, |  |

the admissible M M form the explicit interval

 | max ⁡ { τ + 1, A stop ​ R, R + 1 } ⩽ M ⩽ ⌊ D − π 12 ​ R π 11 ⌋, \max\{\tau+1,A_{\rm stop}R,R+1\}\leqslant M\leqslant\left\lfloor\frac{D-\pi_{12}R}{\pi_{11}}\right\rfloor, |  |

intersected with 1 ⩽ π 21 ​ M + π 22 ​ R < π 11 ​ M + π 12 ​ R 1\leqslant\pi_{21}M+\pi_{22}R<\pi_{11}M+\pi_{12}R. There is one constant-time interval test per candidate R R. Summed over all nodes these tests cost O ⁡ ( D ​ τ 2) O(D\tau^{2}), which is O ⁡ ( D 2 + τ 4) O(D^{2}+\tau^{4}) by 2 ​ D ​ τ 2 ⩽ D 2 + τ 4 2D\tau^{2}\leqslant D^{2}+\tau^{4}. The emitted pairs themselves number exactly D ⁡ ( D − 1) / 2 D(D-1)/2. ∎

### B.3 Boundary formulas and uniform-grid corrections

Fix an accepted coefficient path

 | ( a 0, b 0), ( a 1, b 1), …, ( a d, b d) = ( M, R), a i = A i ​ b i + r i, (a_{0},b_{0}),(a_{1},b_{1}),\ldots,(a_{d},b_{d})=(M,R),\qquad a_{i}=A_{i}b_{i}+r_{i}, |  |

where ( a i + 1, b i + 1) = ( b i, r i) (a_{i+1},b_{i+1})=(b_{i},r_{i}). Put H = a 0 H=a_{0} and B 0 = b 0 B_{0}=b_{0}. A root marker evolves according to

 | U i = ⌊ u i / b i ⌋, u i + 1 = b i − 1 − ( u i mod b i). U_{i}=\left\lfloor u_{i}/b_{i}\right\rfloor,\qquad u_{i+1}=b_{i}-1-(u_{i}\bmod b_{i}). |  | (34) |

###### Theorem 21 (Modular-orbit boundary formula).

Assume R > 0 R>0. For 1 ⩽ m ⩽ d 1\leqslant m\leqslant d let

 | P m = Q ( A 0) ⋯ Q ( A m − 1), χ m = ( P m) 11, L = 1 + ∑ m = 1 d χ m. P_{m}=Q(A_{0})\cdots Q(A_{m-1}),\qquad\chi_{m}=(P_{m})_{11},\qquad L=1+\sum_{m=1}^{d}\chi_{m}. |  |

Then the boundary multiset of Definition 9 is

 | ( e 0, …, e L − 1) = sort ⁡ ( ( k ​ B 0 mod H) 0 ⩽ k < L), e L = H. (e_{0},\ldots,e_{L-1})=\operatorname{sort}\bigl((kB_{0}\bmod H)_{0\leqslant k<L}\bigr),\qquad e_{L}=H. |  | (35) |

The listed residues are distinct.

###### Proof of Theorem 21.

Put P 0 = I P_{0}=I and write every prefix matrix as

 | P i = ( χ i χ i − 1 η i η i − 1), χ − 1 = 0, χ 0 = 1. P_{i}=\begin{pmatrix}\chi_{i}&\chi_{i-1}\\[2.84526pt] \eta_{i}&\eta_{i-1}\end{pmatrix},\qquad\chi_{-1}=0,\quad\chi_{0}=1. |  |

Thus χ i + 1 = A i ​ χ i + χ i − 1 \chi_{i+1}=A_{i}\chi_{i}+\chi_{i-1} and det P i = ( − 1) i \det P_{i}=(-1)^{i}. Since ( H, B 0) 𝖳 = P i ​ ( a i, b i) 𝖳 (H,B_{0})^{\mathsf{T}}=P_{i}(a_{i},b_{i})^{\mathsf{T}}, we have

 | χ i ​ B 0 − η i ​ H = ( − 1) i ​ b i. \chi_{i}B_{0}-\eta_{i}H=(-1)^{i}b_{i}. |  | (36) |

Consider the edge between two consecutive root markers u − 1 u-1 and u u. As long as their earlier marker quotients agree, the fold ( 34) sends the edge coordinate x i x_{i} to

 | x i + 1 = ( − x i) mod b i. x_{i+1}=(-x_{i})\bmod b_{i}. |  |

The quotient U i U_{i} changes across that edge exactly when x i = 0 x_{i}=0 modulo b i b_{i}. Let L i = 1 + ∑ m = 1 i χ m L_{i}=1+\sum_{m=1}^{i}\chi_{m}.

*Induction claim.*After the first i i marker quotients have been fixed, their cut edges are

 | { k ​ B 0 mod H: 0 ⩽ k < L i }. \{kB_{0}\bmod H:0\leqslant k<L_{i}\}. |  |

For i = 0 i=0, L 0 = 1 L_{0}=1 and the set consists only of the edge zero.

For the induction step, fix an atom J J of the partition made by these edges. Unrolling the first i i folds on J J writes

 | u i = ( − 1) i ​ u + c J u_{i}=(-1)^{i}u+c_{J} |  |

for an integer constant c J c_{J} depending on that atom. Consequently U i U_{i} is constant until this affine lift crosses a multiple of b i b_{i}; at such a crossing it changes by one. Hence locating the new cut edges is equivalent to listing all crossings of consecutive b i b_{i} -blocks by these affine lifts. Equation ( 36) makes the lift of a root translation explicit:

 | ( − 1) i ​ χ i ​ B 0 ≡ b i ( mod H). (-1)^{i}\chi_{i}B_{0}\equiv b_{i}\pmod{H}. |  |

Thus translating a root edge by χ i ​ B 0 \chi_{i}B_{0} advances its lifted value by one whole b i b_{i} -block. Index the new root edges from the end of the old orbit block, so that their orbit indices are L i + j L_{i}+j. The division a i = A i ​ b i + b i + 1 a_{i}=A_{i}b_{i}+b_{i+1} supplies A i A_{i} complete blocks. Each complete block has χ i \chi_{i} lifted positions, and the wraparound recorded by the second column of P i P_{i} has χ i − 1 \chi_{i-1} positions. Equivalently, the possible offsets j j split without overlap as

 | { r χ i + ℓ: 0 ⩽ r < A i, 0 ⩽ ℓ < χ i } ∪ ˙ { A i χ i + ℓ: 0 ⩽ ℓ < χ i − 1 }. \{r\chi_{i}+\ell:0\leqslant r<A_{i},0\leqslant\ell<\chi_{i}\}\;\dot{\cup}\;\{A_{i}\chi_{i}+\ell:0\leqslant\ell<\chi_{i-1}\}. |  |

For fixed r r, the first set is the complete offset block [r ​ χ i, ( r + 1) ​ χ i) [r\chi_{i},(r+1)\chi_{i}) and records the next crossing in each lifted position. The second set is exactly the incomplete wrapped block. Thus every displayed offset gives a crossing, and any other edge stays strictly inside one b i b_{i} -block. The two sets form, without gaps or overlaps, the interval 0 ⩽ j < A i ​ χ i + χ i − 1 = χ i + 1 0\leqslant j<A_{i}\chi_{i}+\chi_{i-1}=\chi_{i+1}. Here the last equality is the continuant recurrence. Hence the new crossing edges are exactly

 | { ( L i + j) ​ B 0 mod H: 0 ⩽ j < χ i + 1 }. \{(L_{i}+j)B_{0}\bmod H:0\leqslant j<\chi_{i+1}\}. |  |

They extend the preceding indices to 0 ⩽ k < L i + 1 0\leqslant k<L_{i+1}; the rotation period bound verified below makes all corresponding root edges disjoint. This proves the claim by induction and, at i = d i=d, proves ( 35) with L = L d L=L_{d}.

The same recurrence gives

 | L ⩽ 2 ​ χ d + χ d − 1. L\leqslant 2\chi_{d}+\chi_{d-1}. |  | (37) |

For the induction step, add χ i + 1 \chi_{i+1} to L i ⩽ 2 ​ χ i + χ i − 1 L_{i}\leqslant 2\chi_{i}+\chi_{i-1} and use χ i + 1 ⩾ χ i + χ i − 1 \chi_{i+1}\geqslant\chi_{i}+\chi_{i-1}.

The orbit points are exactly the cut edges of the marker-word map, so the word is fixed precisely between consecutive distinct boundaries. To verify the distinctness statement, let g = gcd ⁡ ( M, R) g=\gcd(M,R). Unimodularity gives gcd ⁡ ( H, B 0) = g \gcd(H,B_{0})=g. Since R > 0 R>0, we have M / g ⩾ 2 M/g\geqslant 2 and R / g ⩾ 1 R/g\geqslant 1, and hence the rotation period H / g = χ d ​ ( M / g) + χ d − 1 ​ ( R / g) H/g=\chi_{d}(M/g)+\chi_{d-1}(R/g) is at least 2 ​ χ d + χ d − 1 ⩾ L 2\chi_{d}+\chi_{d-1}\geqslant L. Thus the first L L residues are distinct. This completes the proof of the theorem. ∎

Affine endpoints.

Write P = ( π 11 π 12 π 21 π 22) P=\left(\begin{smallmatrix}\pi_{11}&\pi_{12}\\ \pi_{21}&\pi_{22}\end{smallmatrix}\right) and use the interior sample pair ( M, R) = ( 2, 1) (M,R)=(2,1). Put

 | H ∗ = 2 ​ π 11 + π 12, B ∗ = 2 ​ π 21 + π 22. H_{*}=2\pi_{11}+\pi_{12},\qquad B_{*}=2\pi_{21}+\pi_{22}. |  |

Let k 0, …, k L − 1 k_{0},\ldots,k_{L-1} order the residues k ​ B ∗ mod H ∗ kB_{*}\bmod H_{*} increasingly and put c k = ⌊ k ​ B ∗ / H ∗ ⌋ c_{k}=\left\lfloor kB_{*}/H_{*}\right\rfloor. Define

 | λ j = k j ​ π 21 − c k j ​ π 11, ω j = k j ​ π 22 − c k j ​ π 12. \lambda_{j}=k_{j}\pi_{21}-c_{k_{j}}\pi_{11},\qquad\omega_{j}=k_{j}\pi_{22}-c_{k_{j}}\pi_{12}. |  | (38) |

To prove that this sample order is valid throughout the cone, put ξ = R / M \xi=R/M. The rotation number is

 | B 0 H = π 21 + π 22 ​ ξ π 11 + π 12 ​ ξ, \frac{B_{0}}{H}=\frac{\pi_{21}+\pi_{22}\xi}{\pi_{11}+\pi_{12}\xi}, |  |

which lies between π 21 / π 11 \pi_{21}/\pi_{11} and ( π 21 + π 22) / ( π 11 + π 12) (\pi_{21}+\pi_{22})/(\pi_{11}+\pi_{12}). These two fractions are Farey neighbours because π 11 ​ π 22 − π 12 ​ π 21 = det P = ± 1 \pi_{11}\pi_{22}-\pi_{12}\pi_{21}=\det P=\pm 1. A floor ⌊ k ​ B 0 / H ⌋ \left\lfloor kB_{0}/H\right\rfloor with k < L k<L can change only when B 0 / H B_{0}/H reaches a rational whose reduced denominator divides k k; the order of residues with indices k, ℓ < L k,\ell<L can change only when ( k − ℓ) ​ B 0 / H (k-\ell)B_{0}/H is integral. Either event therefore has a reduced denominator below L L. By ( 37), L ⩽ 2 ​ π 11 + π 12 L\leqslant 2\pi_{11}+\pi_{12}, whereas no rational with denominator below this value lies strictly between Farey neighbours whose denominator sum is 2 ​ π 11 + π 12 2\pi_{11}+\pi_{12}. Hence all floors and the residue order are constant for 0 < R < M 0<R<M and may be computed at the sample point ξ = 1 / 2 \xi=1/2. Expanding

 | k j ​ B 0 − c k j ​ H k_{j}B_{0}-c_{k_{j}}H |  |

in M M and R R and using ( 38) gives

 | e j = λ j ​ M + ω j ​ R. e_{j}=\lambda_{j}M+\omega_{j}R. |  | (39) |

For R = 0 R=0 we define the labeled boundary list by the closed specialization of these affine forms. Since e j ​ ( M, R) ⩽ e j + 1 ​ ( M, R) e_{j}(M,R)\leqslant e_{j+1}(M,R) for every 0 < R < M 0<R<M, passage to the limit gives a nondecreasing list at R = 0 R=0; some entries may coalesce at 0 0 or H H. Each quotient test in ( 34) is piecewise affine between consecutive cut edges; at a cut edge the floor and the half-open convention both select the slot on its right. Passing these inequalities to R = 0 R=0 therefore preserves the labeled marker word on every positive-width limiting slot, while intervals that collapse are empty. Thus the specialized list, with repetitions retained and e L = H e_{L}=H, gives exactly the true labeled slots at R = 0 R=0. It is this affine specialization, rather than the ordinary modular residue multiset, that is used for zero-remainder terminal pairs.

Once the marker word is known, no further recurrence is needed at query time. Let b i = ϑ i, 1 ​ M + ϑ i, 2 ​ R b_{i}=\vartheta_{i,1}M+\vartheta_{i,2}R be the second coefficient at depth i i and let U i U_{i} be the fixed marker quotient of one true slot. Unrolling ( 34) gives the executable terminal-marker formula

 | u d = ( − 1) d ​ u 0 + ∑ i = 0 d − 1 ( − 1) d − 1 − i ​ ( ( U i + 1) ​ ( ϑ i, 1 ​ M + ϑ i, 2 ​ R) − 1). u_{d}=(-1)^{d}u_{0}+\sum_{i=0}^{d-1}(-1)^{d-1-i}\bigl((U_{i}+1)(\vartheta_{i,1}M+\vartheta_{i,2}R)-1\bigr). |  | (40) |

The same formula with the second marker word ( V i) i (V_{i})_{i} gives v d v_{d}. Consequently each slot stores four integral coefficients for u d = c u ​ u 0 + c M ​ M + c R ​ R + c 0 u_{d}=c_{u}u_{0}+c_{M}M+c_{R}R+c_{0}; a slot pair and its moment operator determine the complete terminal state in constant time.

Uniform grids and local corrections. Put δ = det P \delta=\det P. The coefficients in ( 39) satisfy

 | π 11 ​ ω j − π 12 ​ λ j = k j ​ δ. \pi_{11}\omega_{j}-\pi_{12}\lambda_{j}=k_{j}\delta. |  |

Consequently the two endpoint specializations give the exact identities

 | π 11 ​ e j = λ j ​ H + k j ​ δ ​ R, ( π 11 + π 12) ​ e j = ( λ j + ω j) ​ H − k j ​ δ ​ ( M − R). \pi_{11}e_{j}=\lambda_{j}H+k_{j}\delta R,\qquad(\pi_{11}+\pi_{12})e_{j}=(\lambda_{j}+\omega_{j})H-k_{j}\delta(M-R). |  | (41) |

For the technical construction define

 | T 0 = π 11, z 0, j = λ j, T 1 = π 11 + π 12, z 1, j = λ j + ω j, T_{0}=\pi_{11},\quad z_{0,j}=\lambda_{j},\qquad T_{1}=\pi_{11}+\pi_{12},\quad z_{1,j}=\lambda_{j}+\omega_{j}, |  |

and let K ν ​ ( z) K_{\nu}(z) be the multiset of indices k j k_{j} with z ν, j = z z_{\nu,j}=z. For a terminal pair select

 | ( ν, T, E, ε) = { ( 0, π 11, R, det P), 2 ​ R ⩽ M, ( 1, π 11 + π 12, M − R, − det P), 2 ​ R > M. (\nu,T,E,\varepsilon)=\begin{cases}(0,\pi_{11},R,\det P),&2R\leqslant M,\\ (1,\pi_{11}+\pi_{12},M-R,-\det P),&2R>M.\end{cases} |  | (42) |

The selected uniform grid divides [0, H) [0,H) into T T equal intervals; the cell of a marker t t is x = ⌊ T ​ t / H ⌋ x=\left\lfloor Tt/H\right\rfloor.

At the two endpoint specializations of ( 39), 0 ⩽ e j ⩽ H 0\leqslant e_{j}\leqslant H gives

 | 0 ⩽ λ j ⩽ π 11, 0 ⩽ λ j + ω j ⩽ π 11 + π 12. 0\leqslant\lambda_{j}\leqslant\pi_{11},\qquad 0\leqslant\lambda_{j}+\omega_{j}\leqslant\pi_{11}+\pi_{12}. |  |

Thus K 0 K_{0} and K 1 K_{1} are stored directly in arrays indexed respectively by 0, …, T 0 0,\ldots,T_{0} and 0, …, T 1 0,\ldots,T_{1}; no associative search structure is needed.

For 2 ​ R ⩽ M 2R\leqslant M, the orbit bound ( 37) gives

 | k j ​ R < ( 2 ​ π 11 + π 12) ​ R ⩽ π 11 ​ M + π 12 ​ R = H. k_{j}R<(2\pi_{11}+\pi_{12})R\leqslant\pi_{11}M+\pi_{12}R=H. |  |

For 2 ​ R > M 2R>M it gives

 | k j ​ ( M − R) < ( 2 ​ π 11 + π 12) ​ ( M − R) < π 11 ​ M + π 12 ​ R = H. k_{j}(M-R)<(2\pi_{11}+\pi_{12})(M-R)<\pi_{11}M+\pi_{12}R=H. |  |

Thus the displacement term in the selected identity of ( 41) is strictly smaller than one uniform cell.

It remains to bound the number of orbit points at one grid position. The continuant recurrence gives 0 ⩽ π 12 ⩽ π 11 0\leqslant\pi_{12}\leqslant\pi_{11}. If λ j = λ j ′ \lambda_{j}=\lambda_{j^{\prime}}, then ( k j − k j ′) ​ π 21 (k_{j}-k_{j^{\prime}})\pi_{21} is divisible by π 11 \pi_{11}. Unimodularity gives gcd ⁡ ( π 11, π 21) = 1 \gcd(\pi_{11},\pi_{21})=1, so the corresponding orbit indices are congruent modulo π 11 \pi_{11}. Since 0 ⩽ k j < L ⩽ 2 ​ π 11 + π 12 ⩽ 3 ​ π 11 0\leqslant k_{j}<L\leqslant 2\pi_{11}+\pi_{12}\leqslant 3\pi_{11}, at most three indices share one position of the first grid. Similarly, gcd ⁡ ( π 11 + π 12, π 21 + π 22) = 1 \gcd(\pi_{11}+\pi_{12},\pi_{21}+\pi_{22})=1; equality of λ j + ω j \lambda_{j}+\omega_{j} and λ j ′ + ω j ′ \lambda_{j^{\prime}}+\omega_{j^{\prime}} makes the two indices congruent modulo π 11 + π 12 \pi_{11}+\pi_{12}. The bound L ⩽ 2 ​ π 11 + π 12 ⩽ 2 ​ ( π 11 + π 12) L\leqslant 2\pi_{11}+\pi_{12}\leqslant 2(\pi_{11}+\pi_{12}) leaves at most two indices at one position of the second grid.

For the selected tuple ( 42), the corresponding identity can be written

 | T ​ e j = z ν, j ​ H + ε ​ k j ​ E, 0 ⩽ k j ​ E < H. Te_{j}=z_{\nu,j}H+\varepsilon k_{j}E,\qquad 0\leqslant k_{j}E<H. |  | (43) |

For later use define the inclusive group prefix

 | pref ν ⁡ ( z) = ∑ w = 0 z | K ν ​ ( w) |, pref ν ⁡ ( − 1) = 0. \operatorname{pref}_{\nu}(z)=\sum_{w=0}^{z}|K_{\nu}(w)|,\qquad\operatorname{pref}_{\nu}(-1)=0. |  |

Let T ​ t = x ​ H + ρ Tt=xH+\rho with 0 ⩽ ρ < H 0\leqslant\rho<H. If ε = 1 \varepsilon=1, all groups at positions below x x lie at or before t t, and a member of K ν ​ ( x) K_{\nu}(x) does so exactly when k ​ E ⩽ ρ kE\leqslant\rho. If ε = − 1 \varepsilon=-1, all groups through position x x lie at or before t t, and a member of K ν ​ ( x + 1) K_{\nu}(x+1) does so exactly when k ​ E ⩾ H − ρ kE\geqslant H-\rho. Thus the local correction of Definition 10 is explicitly

 | α ν ​ ( t) = { ∑ k ∈ K ν ​ ( x) 𝟏 [k E ⩽ ρ], ε = 1, ∑ k ∈ K ν ​ ( x + 1) 𝟏 [k E ⩾ H − ρ], ε = − 1. \alpha_{\nu}(t)=\begin{cases}\displaystyle\sum_{k\in K_{\nu}(x)}\mathbf{1}[kE\leqslant\rho],&\varepsilon=1,\\[5.69054pt] \displaystyle\sum_{k\in K_{\nu}(x+1)}\mathbf{1}[kE\geqslant H-\rho],&\varepsilon=-1.\end{cases} |  | (44) |

The true slot determined by a uniform cell and a local correction is

 | i ν ​ ( x, α) = { pref ν ⁡ ( x − 1) + α − 1, ε = 1, pref ν ⁡ ( x) + α − 1, ε = − 1. i_{\nu}(x,\alpha)=\begin{cases}\operatorname{pref}_{\nu}(x-1)+\alpha-1,&\varepsilon=1,\\ \operatorname{pref}_{\nu}(x)+\alpha-1,&\varepsilon=-1.\end{cases} |  | (45) |

Indeed, the right-hand side is the number of true boundaries at or before t t, minus one. Since e 0 = 0 e_{0}=0, every code attained by a marker gives a valid index and ( 45) equals ι ⁡ ( t) \iota(t).

For a uniform rectangle ( x, y) (x,y) and a valid correction pair define

 | ℳ ν, P ​ ( x, y) ​ [α u, α v] = ( i ν ​ ( x, α u), i ν ​ ( y, α v), 𝖮𝗉 P; i ν ​ ( x, α u), i ν ​ ( y, α v)), \mathcal{M}_{\nu,P}(x,y)[\alpha_{u},\alpha_{v}]=\bigl(i_{\nu}(x,\alpha_{u}),i_{\nu}(y,\alpha_{v}),\mathsf{Op}_{P;i_{\nu}(x,\alpha_{u}),i_{\nu}(y,\alpha_{v})}\bigr), |  | (46) |

together with the affine terminal-marker data of the selected true slot pair. Equation ( 45) depends only on the path, the chosen grid, and the two local corrections. Therefore the menu may be constructed before any stopped terminal pair is processed. The group bounds proved above leave at most four values of each local correction, hence at most sixteen entries per uniform rectangle. Equations ( 44) and ( 45) prove that the selected entry is the exact true rectangle and operator. This proves Theorem 11.

Construction cost. Finally H ∗ = 2 ​ π 11 + π 12 ⩽ 3 ​ τ H_{*}=2\pi_{11}+\pi_{12}\leqslant 3\tau. The L L sample residues can therefore be placed in an array of length H ∗ H_{*} and read in order in O ⁡ ( τ) O(\tau) time and words. Insert each ordered orbit index into K 0 ​ ( λ j) K_{0}(\lambda_{j}) and K 1 ​ ( λ j + ω j) K_{1}(\lambda_{j}+\omega_{j}), then scan the two arrays to form their prefix counts. Their total length is ( π 11 + 1) + ( π 11 + π 12 + 1) = 2 ​ π 11 + π 12 + 2 = O ⁡ ( τ) (\pi_{11}+1)+(\pi_{11}+\pi_{12}+1)=2\pi_{11}+\pi_{12}+2=O(\tau), and the group bounds above give constant-size entries. One fold trace per slot costs O ⁡ ( L ​ d) O(Ld); because every nonempty prefix contributes at least one to L L, we have d < L d<L and thus O ⁡ ( L ​ d) = O ⁡ ( L 2) O(Ld)=O(L^{2}).

Finally enumerate all coarse pairs and their at most sixteen local-code pairs using ( 45). The two complete menu sizes are

 | 16 ​ π 11 2 + 16 ​ ( π 11 + π 12) 2 = O ⁡ ( τ 2). 16\pi_{11}^{2}+16(\pi_{11}+\pi_{12})^{2}=O(\tau^{2}). |  |

This is also their construction time and proves the final cost assertion of Theorem 11.

### B.4 Constant-size operator representation

For one fixed query, pointwise evaluation uses the six lattice moments together with the four univariate power sums Pow 0, …, Pow 3 \operatorname{Pow}_{0},\ldots,\operatorname{Pow}_{3}. For compilation, however, one operator must be applicable before the root lengths q q and h h are known. The complement of the transformed child region must therefore be retained as a boundary-correction polynomial in ( q, h) (q,h). Summing a degree-two lattice monomial over a rectangle can raise the total boundary degree to four; for example,

 | ∑ 0 ⩽ t < q ∑ 1 ⩽ s ⩽ h t 2 = h ​ q ​ ( q − 1) ​ ( 2 ​ q − 1) 6. \sum_{0\leqslant t<q}\sum_{1\leqslant s\leqslant h}t^{2}=h\,\frac{q(q-1)(2q-1)}{6}. |  |

The degree bounds for the six corrections are

 | 2, 3, 4, 3, 4, 4. 2,\quad 3,\quad 4,\quad 3,\quad 4,\quad 4. |  |

We store each correction on the corresponding initial part of the monomial triangle

 | q i ​ h j, i, j ⩾ 0, i + j ⩽ 4, q^{i}h^{j},\qquad i,j\geqslant 0,\quad i+j\leqslant 4, |  |

so the coefficient counts are 6, 10, 15, 10, 15, 15 6,10,15,10,15,15. The number 15 15 is the dimension of the full bivariate degree-four correction space, not the size of the recursive moment kernel, which remains six. Under one cycle the update is ( q, h) ↦ ( h, q − A ​ h − d) (q,h)\mapsto(h,q-Ah-d) with d = U + V + 2 − A d=U+V+2-A. Substitution of these affine forms into the corrections shows that the full degree-four triangle is closed.

Executable one-cycle coefficients. The following formulas remove any need to reconstruct the operator from the geometric argument. Put

 | S r ​ ( h):= ∑ k = 0 h − 1 k r, S r, j + ​ ( h):= ∑ k = 0 h − 1 k r ​ ( k + 1) j = ∑ ℓ = 0 j ( j ℓ) ​ S r + ℓ ​ ( h). S_{r}(h):=\sum_{k=0}^{h-1}k^{r},\qquad S^{+}_{r,j}(h):=\sum_{k=0}^{h-1}k^{r}(k+1)^{j}=\sum_{\ell=0}^{j}\binom{j}{\ell}S_{r+\ell}(h). |  |

Only S 0, S 1, S 2, S 3 S_{0},S_{1},S_{2},S_{3} occur, with

 | S 0 = h, S 1 = h ⁡ ( h − 1) 2, S 2 = h ​ ( h − 1) ​ ( 2 ​ h − 1) 6, S 3 = S 1 2. S_{0}=h,\quad S_{1}=\frac{h(h-1)}{2},\quad S_{2}=\frac{h(h-1)(2h-1)}{6},\quad S_{3}=S_{1}^{2}. |  |

For h ⩾ 1 h\geqslant 1, this notation is related to the earlier power sums by S 0 ​ ( h) = 1 + Σ 0 ​ ( h − 1) S_{0}(h)=1+\Sigma_{0}(h-1) and S r ​ ( h) = Σ r ​ ( h − 1) S_{r}(h)=\Sigma_{r}(h-1) for r ⩾ 1 r\geqslant 1; all these sums are zero at h = 0 h=0. For j = 0, 1, 2 j=0,1,2 define E 0 ​ j E_{0j} by the first line below; for j = 0, 1 j=0,1 define E 1 ​ j E_{1j} by the second line; finally define E 20 E_{20} by the remaining lines:

 | E 0 ​ j ​ ( q, h, A, U) \displaystyle E_{0j}(q,h;A,U) | = ( q − U − 1) ​ S 0, j + − A ​ S 1, j +, \displaystyle=(q-U-1)S^{+}_{0,j}-AS^{+}_{1,j}, |  | (47) |

 | E 1 ​ j ​ ( q, h, A, U) \displaystyle E_{1j}(q,h;A,U) | = 1 2 ​ ( q ⁡ ( q − 1) ​ S 0, j + − A 2 ​ S 2, j + − A ⁡ ( 2 ​ U + 1) ​ S 1, j + − U ⁡ ( U + 1) ​ S 0, j +), \displaystyle=\frac{1}{2}\bigl(q(q-1)S^{+}_{0,j}-A^{2}S^{+}_{2,j}-A(2U+1)S^{+}_{1,j}-U(U+1)S^{+}_{0,j}\bigr), |  | (48) |

 | E 20 ​ ( q, h, A, U) \displaystyle E_{20}(q,h;A,U) | = 1 6 ​ ( q ⁡ ( q − 1) ​ ( 2 ​ q − 1) ​ S 0, 0 + − 2 ​ A 3 ​ S 3, 0 + CLOSE \displaystyle=\frac{1}{6}\bigl(q(q-1)(2q-1)S^{+}_{0,0}-2A^{3}S^{+}_{3,0} |  |

 |  | − 3 ​ A 2 ​ ( 2 ​ U + 1) ​ S 2, 0 + − A ⁡ ( 6 ​ U 2 + 6 ​ U + 1) ​ S 1, 0 + \displaystyle\hskip 45.5244pt{}-3A^{2}(2U+1)S^{+}_{2,0}-A(6U^{2}+6U+1)S^{+}_{1,0} |  |

 |  | OPEN − U ⁡ ( U + 1) ​ ( 2 ​ U + 1) ​ S 0, 0 +). \displaystyle\hskip 45.5244pt{}-U(U+1)(2U+1)S^{+}_{0,0}\bigr). |  | (49) |

Here every S r, j + S^{+}_{r,j} is evaluated at h h. In the fixed coordinate order of ( 10), set

 | 𝐄 ⁡ ( q, h, A, U) = ( E 00, E 10, E 20, E 01, E 11, E 02) 𝖳. \mathbf{E}(q,h;A,U)=(E_{00},E_{10},E_{20},E_{01},E_{11},E_{02})^{\mathsf{T}}. |  |

Expanding the affine image in ( 19) gives the explicit one-step moment identity

 | 𝐋 parent = 𝐄 ⁡ ( q, h, A, U) − 𝖢 ⁡ ( A, U) ​ 𝐋 child, \mathbf{L}_{\rm parent}=\mathbf{E}(q,h;A,U)-\mathsf{C}(A,U)\mathbf{L}_{\rm child}, |  | (50) |

where

 | 𝖢 ⁡ ( A, U) = ( 1 0 0 0 0 0 U A 0 1 0 0 U 2 2 ​ A ​ U A 2 2 ​ U 2 ​ A 1 1 1 0 0 0 0 U A + U A 1 1 0 1 2 1 0 0 0). \mathsf{C}(A,U)=\begin{pmatrix}1&0&0&0&0&0\\ U&A&0&1&0&0\\ U^{2}&2AU&A^{2}&2U&2A&1\\ 1&1&0&0&0&0\\ U&A+U&A&1&1&0\\ 1&2&1&0&0&0\end{pmatrix}. |  |

Equations ( 47)–( 50) are the six scalar formulas used by both pointwise evaluation and operator compilation.

The affine state part is equally explicit. For 𝐬 ~ = ( a, b, q, h, u, v, 1) 𝖳 \widetilde{\mathbf{s}}=(a,b,q,h,u,v,1)^{\mathsf{T}},

 | 𝐬 ~ ′ = 𝖲 ⁡ ( A, U, V) ​ 𝐬 ~, 𝖲 ⁡ ( A, U, V) = ( 0 1 0 0 0 0 0 1 − A 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 − A 0 0 − ( U + V + 2 − A) 0 U + 1 0 0 − 1 0 − 1 0 V + 1 0 0 0 − 1 − 1 0 0 0 0 0 0 1). \widetilde{\mathbf{s}}^{\prime}=\mathsf{S}(A,U,V)\widetilde{\mathbf{s}},\qquad\mathsf{S}(A,U,V)=\begin{pmatrix}0&1&0&0&0&0&0\\ 1&-A&0&0&0&0&0\\ 0&0&0&1&0&0&0\\ 0&0&1&-A&0&0&-(U+V+2-A)\\ 0&U+1&0&0&-1&0&-1\\ 0&V+1&0&0&0&-1&-1\\ 0&0&0&0&0&0&1\end{pmatrix}. |  | (51) |

Finally, suppose 𝖮𝗉 1 = ( 𝖠 1, 𝖴 1, Π 1) \mathsf{Op}_{1}=(\mathsf{A}_{1},\mathsf{U}_{1},\Pi_{1}) maps the root to an intermediate state and 𝖮𝗉 2 \mathsf{Op}_{2} maps that state to the terminal state. Let ( q 1 ​ ( q, h), h 1 ​ ( q, h)) (q_{1}(q,h),h_{1}(q,h)) be the two length coordinates obtained from 𝖠 1 \mathsf{A}_{1}. Appending the second record means

 | 𝖮𝗉 2 ∘ 𝖮𝗉 1 = ( 𝖠 2 ​ 𝖠 1, 𝖴 1 ​ 𝖴 2, Π 1 ​ ( q, h) + 𝖴 1 ​ Π 2 ​ ( q 1 ​ ( q, h), h 1 ​ ( q, h))). \mathsf{Op}_{2}\circ\mathsf{Op}_{1}=\left(\mathsf{A}_{2}\mathsf{A}_{1},\mathsf{U}_{1}\mathsf{U}_{2},\Pi_{1}(q,h)+\mathsf{U}_{1}\Pi_{2}(q_{1}(q,h),h_{1}(q,h))\right). |  | (52) |

Thus composition consists only of two fixed matrix products and one affine substitution in the fifteen degree-four monomials. Formula ( 52) determines the order of multiplication in this composition.

Optimized pointwise six-moment kernel. Short records and the optional terminal reciprocal step use the following floor-moment recurrence directly. To include the unnormalized calls produced inside the recursion, write f ⁡ ( t) = ⌊ ( c ​ t + γ) / m ⌋ f(t)=\left\lfloor(ct+\gamma)/m\right\rfloor on 0 ⩽ t < n 0\leqslant t<n. Let Φ i ​ j f:= Φ i ​ j ​ ( f) \Phi^{f}_{ij}:=\Phi_{ij}(f), and use Φ i ​ j g \Phi^{g}_{ij} for the corresponding moments of a child query g g. Thus

 | ( Φ 01 f, Φ 11 f, Φ 21 f, Φ 02 f, Φ 12 f, Φ 03 f) = ∑ t = 0 n − 1 ( f, t ​ f, t 2 ​ f, f 2, t ​ f 2, f 3). (\Phi^{f}_{01},\Phi^{f}_{11},\Phi^{f}_{21},\Phi^{f}_{02},\Phi^{f}_{12},\Phi^{f}_{03})=\sum_{t=0}^{n-1}(f,tf,t^{2}f,f^{2},tf^{2},f^{3}). |  |

If n = 0 n=0, return six zeros before performing a division. Reuse the already defined power sums S r ​ ( n) = ∑ t = 0 n − 1 t r S_{r}(n)=\sum_{t=0}^{n-1}t^{r}. If c = Q c ​ m + r c=Q_{c}m+r, γ = Q γ ​ m + z \gamma=Q_{\gamma}m+z, and g ⁡ ( t) = ⌊ ( r ​ t + z) / m ⌋ g(t)=\left\lfloor(rt+z)/m\right\rfloor, then f ⁡ ( t) = Q c ​ t + Q γ + g ⁡ ( t) f(t)=Q_{c}t+Q_{\gamma}+g(t) and

 | Φ 01 f \displaystyle\Phi^{f}_{01} | = Q c ​ S 1 ​ ( n) + Q γ ​ n + Φ 01 g, \displaystyle=Q_{c}S_{1}(n)+Q_{\gamma}n+\Phi^{g}_{01}, |  |

 | Φ 11 f \displaystyle\Phi^{f}_{11} | = Q c ​ S 2 ​ ( n) + Q γ ​ S 1 ​ ( n) + Φ 11 g, \displaystyle=Q_{c}S_{2}(n)+Q_{\gamma}S_{1}(n)+\Phi^{g}_{11}, |  |

 | Φ 21 f \displaystyle\Phi^{f}_{21} | = Q c ​ S 3 ​ ( n) + Q γ ​ S 2 ​ ( n) + Φ 21 g, \displaystyle=Q_{c}S_{3}(n)+Q_{\gamma}S_{2}(n)+\Phi^{g}_{21}, |  |

 | Φ 02 f \displaystyle\Phi^{f}_{02} | = Q c 2 ​ S 2 ​ ( n) + 2 ​ Q c ​ Q γ ​ S 1 ​ ( n) + Q γ 2 ​ n + 2 ​ Q c ​ Φ 11 g + 2 ​ Q γ ​ Φ 01 g + Φ 02 g, \displaystyle=Q_{c}^{2}S_{2}(n)+2Q_{c}Q_{\gamma}S_{1}(n)+Q_{\gamma}^{2}n+2Q_{c}\Phi^{g}_{11}+2Q_{\gamma}\Phi^{g}_{01}+\Phi^{g}_{02}, |  |

 | Φ 12 f \displaystyle\Phi^{f}_{12} | = Q c 2 ​ S 3 ​ ( n) + 2 ​ Q c ​ Q γ ​ S 2 ​ ( n) + Q γ 2 ​ S 1 ​ ( n) \displaystyle=Q_{c}^{2}S_{3}(n)+2Q_{c}Q_{\gamma}S_{2}(n)+Q_{\gamma}^{2}S_{1}(n) |  |

 |  | + 2 ​ Q c ​ Φ 21 g + 2 ​ Q γ ​ Φ 11 g + Φ 12 g, \displaystyle\quad+2Q_{c}\Phi^{g}_{21}+2Q_{\gamma}\Phi^{g}_{11}+\Phi^{g}_{12}, |  |

 | Φ 03 f \displaystyle\Phi^{f}_{03} | = Q c 3 ​ S 3 ​ ( n) + 3 ​ Q c 2 ​ Q γ ​ S 2 ​ ( n) \displaystyle=Q_{c}^{3}S_{3}(n)+3Q_{c}^{2}Q_{\gamma}S_{2}(n) |  |

 |  | + 3 ​ Q c ​ Q γ 2 ​ S 1 ​ ( n) + Q γ 3 ​ n \displaystyle\quad+3Q_{c}Q_{\gamma}^{2}S_{1}(n)+Q_{\gamma}^{3}n |  |

 |  | + 3 ​ Q c 2 ​ Φ 21 g + 6 ​ Q c ​ Q γ ​ Φ 11 g + 3 ​ Q γ 2 ​ Φ 01 g \displaystyle\quad+3Q_{c}^{2}\Phi^{g}_{21}+6Q_{c}Q_{\gamma}\Phi^{g}_{11}+3Q_{\gamma}^{2}\Phi^{g}_{01} |  |

 |  | + 3 ​ Q c ​ Φ 12 g + 3 ​ Q γ ​ Φ 02 g + Φ 03 g. \displaystyle\quad+3Q_{c}\Phi^{g}_{12}+3Q_{\gamma}\Phi^{g}_{02}+\Phi^{g}_{03}. |  | (53) |

If r = 0 r=0, then g g is identically zero and its six moments vanish. Otherwise replace ( c, γ) (c,\gamma) by ( r, z) (r,z); hence the remaining branch has 0 < c < m 0<c<m and 0 ⩽ γ < m 0\leqslant\gamma<m. Put

 | h = ⌊ c ⁡ ( n − 1) + γ m ⌋, g ⁡ ( k) = ⌊ m ​ k + m + c − 1 − γ c ⌋, 0 ⩽ k < h. h=\left\lfloor\frac{c(n-1)+\gamma}{m}\right\rfloor,\qquad g(k)=\left\lfloor\frac{mk+m+c-1-\gamma}{c}\right\rfloor,\quad 0\leqslant k<h. |  |

Discrete reciprocity gives

 | Φ 01 f \displaystyle\Phi^{f}_{01} | = n ​ h − Φ 01 g, \displaystyle=nh-\Phi^{g}_{01}, |  |

 | Φ 11 f \displaystyle\Phi^{f}_{11} | = h ​ S 1 ​ ( n) − Φ 02 g − Φ 01 g 2, \displaystyle=hS_{1}(n)-\frac{\Phi^{g}_{02}-\Phi^{g}_{01}}{2}, |  |

 | Φ 21 f \displaystyle\Phi^{f}_{21} | = h ​ S 2 ​ ( n) − 2 ​ Φ 03 g − 3 ​ Φ 02 g + Φ 01 g 6, \displaystyle=hS_{2}(n)-\frac{2\Phi^{g}_{03}-3\Phi^{g}_{02}+\Phi^{g}_{01}}{6}, |  |

 | Φ 02 f \displaystyle\Phi^{f}_{02} | = n ​ h 2 − 2 ​ Φ 11 g − Φ 01 g, \displaystyle=nh^{2}-2\Phi^{g}_{11}-\Phi^{g}_{01}, |  |

 | Φ 12 f \displaystyle\Phi^{f}_{12} | = h 2 ​ S 1 ​ ( n) − Φ 12 g − Φ 02 g 2 + Φ 11 g + Φ 01 g 2, \displaystyle=h^{2}S_{1}(n)-\Phi^{g}_{12}-\frac{\Phi^{g}_{02}}{2}+\Phi^{g}_{11}+\frac{\Phi^{g}_{01}}{2}, |  | (54) |

 | Φ 03 f \displaystyle\Phi^{f}_{03} | = n ​ h 3 − 3 ​ Φ 21 g − 3 ​ Φ 11 g − Φ 01 g. \displaystyle=nh^{3}-3\Phi^{g}_{21}-3\Phi^{g}_{11}-\Phi^{g}_{01}. |  |

If h = 0 h=0, the reciprocal child has empty range and again contributes six zeros. Otherwise it is evaluated recursively with parameters ( m, m + c − 1 − γ, c, h) (m,m+c-1-\gamma,c,h) in the order (coefficient, intercept, modulus, length). The first branch reduces ( c, γ) (c,\gamma) modulo m m and the second exchanges the two positive coefficients, so the recursion has ordinary Euclidean depth. All six outputs are formed from shared powers and power sums; no generic polynomial evaluator is needed.

The universal one-step formulas use power sums whose denominators divide lcm ⁡ ( 2, 4, 6) = 12 \operatorname{lcm}(2,4,6)=12, followed by the fixed conversion to lattice moments. Expanding them shows that every coefficient has denominator dividing 72 72. We therefore store the integral coefficient vector of 72 ​ Π P; i, j 72\Pi_{P;i,j}. Integral affine substitution preserves this scale, and application performs one exact division by 72 72 per returned component.

###### Full proof of Lemma 13.

Equation ( 13) is an integral affine state map, so homogeneous affine matrices are closed under composition. The basis 1, t, t 2, s, t ​ s, s 2 1,t,t^{2},s,ts,s^{2} is closed under an affine substitution in two variables, so ( 19) induces a fixed six-dimensional map. In ( 18), sums of degree-two monomials over the explicit regions have total boundary degree at most four. Since the child staircase dimensions are affine in ( q, h) (q,h) by ( 13), induction preserves this degree. The one-step power sums have common denominator dividing lcm ⁡ ( 2, 4, 6) = 12 \operatorname{lcm}(2,4,6)=12, and the triangular moment conversion adds a divisor of 6 6; hence 72 72 is a common scale. Integral affine substitution preserves it. The constant-size state matrix, six affine coordinate coefficients, one sign, and fifteen scaled monomial coefficients per component are therefore sufficient. ∎

### B.5 Cell-operator and periodic-table bounds

###### Proof of Lemma 14.

Let n j n_{j} be the number of one-marker groups after the first j j coefficient steps. Pairing the groups leaves at most n j 2 n_{j}^{2} active operator states at that step. Apply the boundary construction to the prefix matrix P j P_{j}. If χ j = ( P j) 11 \chi_{j}=(P_{j})_{11} and χ j − 1 = ( P j) 12 \chi_{j-1}=(P_{j})_{12}, then ( 37) gives

 | n j = 1 + ∑ m = 1 j χ m ⩽ 2 ​ χ j + χ j − 1 ⩽ 3 ​ χ j. n_{j}=1+\sum_{m=1}^{j}\chi_{m}\leqslant 2\chi_{j}+\chi_{j-1}\leqslant 3\chi_{j}. |  |

The continuants satisfy

 | χ j + 1 = A j ​ χ j + χ j − 1 ⩾ χ j + χ j − 1, \chi_{j+1}=A_{j}\chi_{j}+\chi_{j-1}\geqslant\chi_{j}+\chi_{j-1}, |  |

so χ j + 2 ⩾ 2 ​ χ j \chi_{j+2}\geqslant 2\chi_{j}. When read backward, each of the even and odd subsequences ( χ j 2) j (\chi_{j}^{2})_{j} is dominated by a geometric series; hence ∑ j χ j 2 = O ⁡ ( χ d 2) \sum_{j}\chi_{j}^{2}=O(\chi_{d}^{2}). Moreover χ d ⩽ L \chi_{d}\leqslant L, and the path depth is O ⁡ ( log ⁡ ( 2 + L)) O(\log(2+L)). Hence ∑ j n j 2 = O ⁡ ( L 2) \sum_{j}n_{j}^{2}=O(L^{2}). Every active state performs one constant-size operator composition, and the final L 2 L^{2} states produce the cell operators. ∎

#### B.5.1 Small-modulus periodic table

###### Proof of Lemma 15.

If q term = 0 q_{\rm term}=0, h term = 0 h_{\rm term}=0, or R = 0 R=0, the terminal staircase is empty and all six moments vanish. Assume below that q term, h term, R > 0 q_{\rm term},h_{\rm term},R>0.

*Gcd lookup.*Store the triangular table

 | 𝖦𝖢𝖣 [s, 0] = s, 𝖦𝖢𝖣 [s, r] = 𝖦𝖢𝖣 [r, s mod r] ( 1 ⩽ r < s ⩽ κ). \mathsf{GCD}[s,0]=s,\qquad\mathsf{GCD}[s,r]=\mathsf{GCD}[r,s\bmod r]\quad(1\leqslant r<s\leqslant\kappa). |  |

Constructing rows in increasing s s makes every entry on the right available when it is needed, and the Euclidean recurrence gives 𝖦𝖢𝖣 ⁡ [s, r] = gcd ⁡ ( s, r) \mathsf{GCD}[s,r]=\gcd(s,r). Hence the table uses O ⁡ ( κ 2) O(\kappa^{2}) time and entries. Every query passed directly to the table has M ⩽ κ M\leqslant\kappa and uses 𝖦𝖢𝖣 ⁡ [M, R] \mathsf{GCD}[M,R].

*Optional reciprocal cycle.*If M > κ M>\kappa for the terminal query, Lemma 7 gives 0 < R < κ 0<R<\kappa. Apply one reciprocal cycle as in ( 32); its child coefficient pair is ( R, M mod R) (R,M\bmod R), with both entries below κ \kappa. A zero second entry gives zero child moments; otherwise the child is evaluated by the table procedure below, including reduction by 𝖦𝖢𝖣 ⁡ [R, M mod R] \mathsf{GCD}[R,M\bmod R]. In both cases, after conversion to lattice moments, identity ( 18) lifts the child moments to those of the original terminal query in O ⁡ ( 1) O(1) operations. Thus it remains to describe the lookup for a query whose coefficients are at most κ \kappa.

*Removing a common divisor.*Consider a nonzero staircase passed to the table,

 | f ⁡ ( t) = ⌊ R ​ t + β M ⌋, g = gcd ⁡ ( M, R), M = g ​ M ¯, R = g ​ R ¯, f(t)=\left\lfloor\frac{Rt+\beta}{M}\right\rfloor,\qquad g=\gcd(M,R),\qquad M=g\bar{M},\quad R=g\bar{R}, |  |

and write β = g ​ c β + r β \beta=gc_{\beta}+r_{\beta}, where 0 ⩽ r β < g 0\leqslant r_{\beta}<g. Then

 | f ⁡ ( t) = ⌊ R ¯ ​ t + c β M ¯ ⌋. f(t)=\left\lfloor\frac{\bar{R}t+c_{\beta}}{\bar{M}}\right\rfloor. |  | (55) |

Indeed, before taking the floor the omitted term is r β / ( g ​ M ¯) < 1 / M ¯ r_{\beta}/(g\bar{M})<1/\bar{M}, while every fractional part of ( R ¯ ​ t + c β) / M ¯ (\bar{R}t+c_{\beta})/\bar{M} is an integral multiple of 1 / M ¯ 1/\bar{M}. The omitted term therefore cannot cross the next integer. This proves ( 55) and reduces the coefficients to the coprime pair ( M ¯, R ¯) (\bar{M},\bar{R}).

*Removing the intercept.*For this coprime pair define the zero-intercept staircase f 0 ​ ( t) = ⌊ R ¯ ​ t / M ¯ ⌋ f_{0}(t)=\left\lfloor\bar{R}t/\bar{M}\right\rfloor. Choose the unique ζ ∈ { 0, …, M ¯ − 1 } \zeta\in\{0,\ldots,\bar{M}-1\} satisfying

 | ζ ≡ c β ​ R ¯ − 1 ( mod M ¯), R ¯ ​ ζ = z 0 ​ M ¯ + c β. \zeta\equiv c_{\beta}\bar{R}^{-1}\pmod{\bar{M}},\qquad\bar{R}\zeta=z_{0}\bar{M}+c_{\beta}. |  |

Equation ( 55) becomes

 | f ⁡ ( t) = f 0 ​ ( t + ζ) − z 0. f(t)=f_{0}(t+\zeta)-z_{0}. |  | (56) |

Thus every intercept for the pair ( M ¯, R ¯) (\bar{M},\bar{R}) is obtained by a cyclic shift and a vertical translation of the same zero-intercept staircase.

*Stored prefixes and one query.*For each coprime ( M ¯, R ¯) (\bar{M},\bar{R}) store R ¯ − 1 mod M ¯ \bar{R}^{-1}\bmod\bar{M} and the prefix vectors

 | Pref ⁡ ( s) = ∑ 0 ⩽ t < s ( f 0 ​ ( t), t ​ f 0 ​ ( t), t 2 ​ f 0 ​ ( t), f 0 ​ ( t) 2, t ​ f 0 ​ ( t) 2, f 0 ​ ( t) 3), 0 ⩽ s ⩽ 2 ​ M ¯. \operatorname{Pref}(s)=\sum_{0\leqslant t<s}\bigl(f_{0}(t),tf_{0}(t),t^{2}f_{0}(t),f_{0}(t)^{2},tf_{0}(t)^{2},f_{0}(t)^{3}\bigr),\qquad 0\leqslant s\leqslant 2\bar{M}. |  |

These are precisely the six floor-power moments in ( 7). The second period is needed because a shifted fragment may start at ζ \zeta and cross the end of the first period. For a requested length q req q_{\rm req}, write q req = w ​ M ¯ + ℓ q_{\rm req}=w\bar{M}+\ell, where w = ⌊ q req / M ¯ ⌋ w=\left\lfloor q_{\rm req}/\bar{M}\right\rfloor and 0 ⩽ ℓ < M ¯ 0\leqslant\ell<\bar{M}. The final fragment is the difference of two stored prefix vectors. The w w complete periods use

 | f 0 ​ ( t + j ​ M ¯) = f 0 ​ ( t) + j ​ R ¯. f_{0}(t+j\bar{M})=f_{0}(t)+j\bar{R}. |  |

Here are the six constant-time shift formulas explicitly. Extend the stored prefix notation by

 | Pref p ​ r ⁡ ( s):= ∑ 0 ⩽ t < s t p ​ f 0 ​ ( t) r, ( p, r) ∈ { ( 0, 1), ( 1, 1), ( 2, 1), ( 0, 2), ( 1, 2), ( 0, 3) }, \operatorname{Pref}_{pr}(s):=\sum_{0\leqslant t<s}t^{p}f_{0}(t)^{r},\qquad(p,r)\in\{(0,1),(1,1),(2,1),(0,2),(1,2),(0,3)\}, |  |

where the six entries with r > 0 r>0 are stored and Pref p ​ 0 ⁡ ( s):= S p ​ ( s) \operatorname{Pref}_{p0}(s):=S_{p}(s) is an ordinary power sum. For 0 ⩽ ℓ ⩽ M ¯ 0\leqslant\ell\leqslant\bar{M} define the phase-corrected fragment moments

 | Frag p ​ r ( ℓ) = ∑ i = 0 p ∑ j = 0 r ( p i) ​ ( r j) ​ ( − ζ) p − i ​ ( − z 0) r − j ​ ( Pref i ​ j ⁡ ( ζ + ℓ) − Pref i ​ j ⁡ ( ζ)). \operatorname{Frag}_{pr}^{(\ell)}=\sum_{i=0}^{p}\sum_{j=0}^{r}\binom{p}{i}\binom{r}{j}(-\zeta)^{p-i}(-z_{0})^{r-j}\bigl(\operatorname{Pref}_{ij}(\zeta+\ell)-\operatorname{Pref}_{ij}(\zeta)\bigr). |  | (57) |

Thus Frag p ​ r ( ℓ) = ∑ 0 ⩽ s < ℓ s p ​ ( f 0 ​ ( s + ζ) − z 0) r \operatorname{Frag}_{pr}^{(\ell)}=\sum_{0\leqslant s<\ell}s^{p}(f_{0}(s+\zeta)-z_{0})^{r}. Put S 1 ​ ( ℓ) = ℓ ⁡ ( ℓ − 1) / 2 S_{1}(\ell)=\ell(\ell-1)/2 and S 2 ​ ( ℓ) = ℓ ⁡ ( ℓ − 1) ​ ( 2 ​ ℓ − 1) / 6 S_{2}(\ell)=\ell(\ell-1)(2\ell-1)/6, consistently with the power sums already used above. The block beginning at horizontal offset j ​ M ¯ j\bar{M} has

 | Block 01 ⁡ ( j, ℓ) \displaystyle\operatorname{Block}_{01}(j;\ell) | = Frag 01 ( ℓ) + j ​ R ¯ ​ ℓ, \displaystyle=\operatorname{Frag}_{01}^{(\ell)}+j\bar{R}\ell, |  | (58) |

 | Block 11 ⁡ ( j, ℓ) \displaystyle\operatorname{Block}_{11}(j;\ell) | = Frag 11 ( ℓ) + j ​ M ¯ ​ Frag 01 ( ℓ) + j ​ R ¯ ​ S 1 ​ ( ℓ) + j 2 ​ M ¯ ​ R ¯ ​ ℓ, \displaystyle=\operatorname{Frag}_{11}^{(\ell)}+j\bar{M}\operatorname{Frag}_{01}^{(\ell)}+j\bar{R}S_{1}(\ell)+j^{2}\bar{M}\bar{R}\ell, |  | (59) |

 | Block 21 ⁡ ( j, ℓ) \displaystyle\operatorname{Block}_{21}(j;\ell) | = Frag 21 ( ℓ) + 2 ​ j ​ M ¯ ​ Frag 11 ( ℓ) + j 2 ​ M ¯ 2 ​ Frag 01 ( ℓ) + j ​ R ¯ ​ S 2 ​ ( ℓ) \displaystyle=\operatorname{Frag}_{21}^{(\ell)}+2j\bar{M}\operatorname{Frag}_{11}^{(\ell)}+j^{2}\bar{M}^{2}\operatorname{Frag}_{01}^{(\ell)}+j\bar{R}S_{2}(\ell) |  |

 |  | + 2 ​ j 2 ​ M ¯ ​ R ¯ ​ S 1 ​ ( ℓ) + j 3 ​ M ¯ 2 ​ R ¯ ​ ℓ, \displaystyle\quad{}+2j^{2}\bar{M}\bar{R}S_{1}(\ell)+j^{3}\bar{M}^{2}\bar{R}\ell, |  | (60) |

 | Block 02 ⁡ ( j, ℓ) \displaystyle\operatorname{Block}_{02}(j;\ell) | = Frag 02 ( ℓ) + 2 ​ j ​ R ¯ ​ Frag 01 ( ℓ) + j 2 ​ R ¯ 2 ​ ℓ, \displaystyle=\operatorname{Frag}_{02}^{(\ell)}+2j\bar{R}\operatorname{Frag}_{01}^{(\ell)}+j^{2}\bar{R}^{2}\ell, |  | (61) |

 | Block 12 ⁡ ( j, ℓ) \displaystyle\operatorname{Block}_{12}(j;\ell) | = Frag 12 ( ℓ) + j ​ M ¯ ​ Frag 02 ( ℓ) + 2 ​ j ​ R ¯ ​ Frag 11 ( ℓ) + 2 ​ j 2 ​ M ¯ ​ R ¯ ​ Frag 01 ( ℓ) \displaystyle=\operatorname{Frag}_{12}^{(\ell)}+j\bar{M}\operatorname{Frag}_{02}^{(\ell)}+2j\bar{R}\operatorname{Frag}_{11}^{(\ell)}+2j^{2}\bar{M}\bar{R}\operatorname{Frag}_{01}^{(\ell)} |  |

 |  | + j 2 ​ R ¯ 2 ​ S 1 ​ ( ℓ) + j 3 ​ M ¯ ​ R ¯ 2 ​ ℓ, \displaystyle\quad{}+j^{2}\bar{R}^{2}S_{1}(\ell)+j^{3}\bar{M}\bar{R}^{2}\ell, |  | (62) |

 | Block 03 ⁡ ( j, ℓ) \displaystyle\operatorname{Block}_{03}(j;\ell) | = Frag 03 ( ℓ) + 3 ​ j ​ R ¯ ​ Frag 02 ( ℓ) + 3 ​ j 2 ​ R ¯ 2 ​ Frag 01 ( ℓ) + j 3 ​ R ¯ 3 ​ ℓ. \displaystyle=\operatorname{Frag}_{03}^{(\ell)}+3j\bar{R}\operatorname{Frag}_{02}^{(\ell)}+3j^{2}\bar{R}^{2}\operatorname{Frag}_{01}^{(\ell)}+j^{3}\bar{R}^{3}\ell. |  | (63) |

Consequently the answer to a table query of length q req = w ​ M ¯ + ℓ q_{\rm req}=w\bar{M}+\ell is, componentwise,

 | Φ p ​ r = ∑ j = 0 w − 1 Block p ​ r ⁡ ( j; M ¯) + Block p ​ r ⁡ ( w; ℓ). \Phi_{pr}=\sum_{j=0}^{w-1}\operatorname{Block}_{pr}(j;\bar{M})+\operatorname{Block}_{pr}(w;\ell). |  | (64) |

The first sum uses only the four ordinary values ∑ 1, ∑ j, ∑ j 2, ∑ j 3 \sum 1,\sum j,\sum j^{2},\sum j^{3}; the second term uses two stored prefix vectors through ( 57). This yields an O ⁡ ( 1) O(1) lookup algorithm for all six moments.

Both the horizontal shift t ↦ t + j ​ M ¯ t\mapsto t+j\bar{M} and the vertical shift f 0 ↦ f 0 + j ​ R ¯ f_{0}\mapsto f_{0}+j\bar{R} are affine. Consequently every one of the six block moments is a polynomial of degree at most three in j j, and the sum over all complete periods is obtained from the ordinary power sums of 1, j, j 2, j 3 1,j,j^{2},j^{3}. Equation ( 56) is one further horizontal and vertical affine shift; any pure powers introduced by the translation are ordinary power sums. Thus the table query is answered with a constant number of prefix lookups and arithmetic operations, and ( 8) converts the result to the six lattice moments. If the optional reciprocal cycle was taken, the constant-size lift described above returns the moments of the original terminal query expected by the rectangle operator.

*Construction size.*For a fixed M ¯ \bar{M} there are φ ⁡ ( M ¯) \varphi(\bar{M}) possible coprime values of R ¯ \bar{R}, and each stores 2 ​ M ¯ + 1 2\bar{M}+1 constant-size vectors. Hence the total number of stored vectors is

 | ∑ 2 ⩽ M ¯ ⩽ κ 2 ​ M ¯ ​ φ ​ ( M ¯) = O ⁡ ( κ 3). \sum_{2\leqslant\bar{M}\leqslant\kappa}2\bar{M}\varphi(\bar{M})=O(\kappa^{3}). |  |

All prefixes take the same O ⁡ ( κ 3) O(\kappa^{3}) construction time. Computing every stored modular inverse separately by extended Euclid costs O ⁡ ( κ 2 ​ log ⁡ κ) = O ⁡ ( κ 3) O(\kappa^{2}\log\kappa)=O(\kappa^{3}) more operations. Together with the O ⁡ ( κ 2) O(\kappa^{2}) gcd table, this proves all three claims of Lemma 15. ∎

### B.6 Short-query fallback

###### Proof of Theorem 16.

At reciprocal state i i, let β i = a i − u i − 1 \beta_{i}=a_{i}-u_{i}-1 be its intercept and write the length pair as ℓ i = ( q i, h i) T \ell_{i}=(q_{i},h_{i})^{T}, the coefficient quotient as A i A_{i}, the two marker quotients as U i, V i U_{i},V_{i}, and Q i:= Q ⁡ ( A i) Q_{i}:=Q(A_{i}). Let e 1 = ( 1, 0) T e_{1}=(1,0)^{T} and e 2 = ( 0, 1) T e_{2}=(0,1)^{T}. Equation ( 13) reversed is

 | ℓ i = Q i ​ ℓ i + 1 + d i ​ e 1, d i = U i + V i + 2 − A i ⩽ A i + 2. \ell_{i}=Q_{i}\ell_{i+1}+d_{i}e_{1},\qquad d_{i}=U_{i}+V_{i}+2-A_{i}\leqslant A_{i}+2. |  | (65) |

The bound follows from 0 ⩽ u i, v i < a i 0\leqslant u_{i},v_{i}<a_{i}, which gives 0 ⩽ U i, V i ⩽ A i 0\leqslant U_{i},V_{i}\leqslant A_{i}. Let P i = Q 0 ⋯ Q i − 1 P_{i}=Q_{0}\cdots Q_{i-1}, let 𝐜 i = P i ​ e 1 \mathbf{c}_{i}=P_{i}e_{1} be its first column, and put 𝐜 − 1 = e 2 \mathbf{c}_{-1}=e_{2}. Then, componentwise,

 | 𝐜 i + 1 = A i ​ 𝐜 i + 𝐜 i − 1, ∑ i = 0 k − 1 𝐜 i ⩽ 𝐜 k + 𝐜 k − 1. \mathbf{c}_{i+1}=A_{i}\mathbf{c}_{i}+\mathbf{c}_{i-1},\qquad\sum_{i=0}^{k-1}\mathbf{c}_{i}\leqslant\mathbf{c}_{k}+\mathbf{c}_{k-1}. |  | (66) |

Suppose that a query would reach zero height before the end of its compiled coefficient path, and let k k be the first state with h k = 0 h_{k}=0. Then ⌊ ( b k ​ ( q k − 1) + β k) / a k ⌋ = 0 \left\lfloor(b_{k}(q_{k}-1)+\beta_{k})/a_{k}\right\rfloor=0, hence q k ⩽ A k + 1 q_{k}\leqslant A_{k}+1. Because the coefficient path continues, the accepted columns 𝐜 k − 1, 𝐜 k, 𝐜 k + 1 \mathbf{c}_{k-1},\mathbf{c}_{k},\mathbf{c}_{k+1} are componentwise at most τ \tau. Iterating ( 65) and using ( 66) gives

 | ℓ 0 = P k ​ ℓ k + ∑ i < k d i ​ 𝐜 i, P k ​ ℓ k = q k ​ 𝐜 k ⩽ ( A k + 1) ​ 𝐜 k ⩽ 𝐜 k + 1 + 𝐜 k ⩽ 2 ​ τ, \ell_{0}=P_{k}\ell_{k}+\sum_{i<k}d_{i}\mathbf{c}_{i},\qquad P_{k}\ell_{k}=q_{k}\mathbf{c}_{k}\leqslant(A_{k}+1)\mathbf{c}_{k}\leqslant\mathbf{c}_{k+1}+\mathbf{c}_{k}\leqslant 2\tau, |  |

and

 | ∑ i < k d i ​ 𝐜 i ⩽ ∑ i < k ( A i + 2) ​ 𝐜 i ⩽ 3 ​ ( 𝐜 k + 𝐜 k − 1) ⩽ 3 ​ 𝐜 k + 1 ⩽ 3 ​ τ. \sum_{i<k}d_{i}\mathbf{c}_{i}\leqslant\sum_{i<k}(A_{i}+2)\mathbf{c}_{i}\leqslant 3(\mathbf{c}_{k}+\mathbf{c}_{k-1})\leqslant 3\mathbf{c}_{k+1}\leqslant 3\tau. |  |

For the middle inequality, the recurrence telescopes to ∑ i < k A i ​ 𝐜 i = 𝐜 k + 𝐜 k − 1 − 𝐜 0 − 𝐜 − 1 \sum_{i<k}A_{i}\mathbf{c}_{i}=\mathbf{c}_{k}+\mathbf{c}_{k-1}-\mathbf{c}_{0}-\mathbf{c}_{-1}, while 2 ​ ∑ i < k 𝐜 i ⩽ 2 ​ ( 𝐜 k + 𝐜 k − 1) 2\sum_{i<k}\mathbf{c}_{i}\leqslant 2(\mathbf{c}_{k}+\mathbf{c}_{k-1}) by ( 66). Therefore both root lengths satisfy q 0, h 0 ⩽ 5 ​ τ q_{0},h_{0}\leqslant 5\tau, so every query that would terminate along its compiled path is short. Pointwise evaluation has ordinary Euclidean depth O ⁡ ( log ⁡ a) = O ⁡ ( log ⁡ D) = O ⁡ ( log ⁡ ( 2 + τ)) O(\log a)=O(\log D)=O(\log(2+\tau)).

Recall q sq = ⌊ ( N − a 2) / b ⌋ q_{\mathrm{sq}}=\left\lfloor(N-a^{2})/b\right\rfloor from Appendix A.1. If q sq ⩾ a − 1 q_{\mathrm{sq}}\geqslant a-1, the bound q ⩽ 5 ​ τ q\leqslant 5\tau leaves only O ⁡ ( τ 2) O(\tau^{2}) pairs ( a, b) (a,b). Otherwise q = q sq ⩽ 5 ​ τ q=q_{\mathrm{sq}}\leqslant 5\tau and

 | N − a 2 < b ⁡ ( 5 ​ τ + 1) ⩽ D ⁡ ( 5 ​ τ + 1). N-a^{2}<b(5\tau+1)\leqslant D(5\tau+1). |  |

Since D 2 ⩽ N D^{2}\leqslant N, this implies D − a < 5 ​ τ + 1 D-a<5\tau+1. Hence there are O ⁡ ( τ) O(\tau) possible moduli and fewer than D D coefficients for each. Altogether there are O ⁡ ( D ​ τ) O(D\tau) short queries; multiplying by the pointwise-recursion depth proves the theorem. ∎

### B.7 Complete O ⁡ ( n ​ log ⁡ n) O(n\log n) algorithm: formulas and pseudocode

Fix a layer size N N. For a direction pair ( a, b) (a,b), the half-domain reduction produces the normalized query ( 9). Its length q q is the number of staircase columns. Write

 | N − b ​ q = η ​ a + β, 0 ⩽ β < a. N-bq=\eta a+\beta,\qquad 0\leqslant\beta<a. |  |

The quotient η \eta is needed only when the staircase moments are converted back to the original side coordinates.

The six moments J i ​ j J_{ij} of ( 21) split as J i ​ j = J i ​ j upper − J i ​ j lower J_{ij}=J^{\mathrm{upper}}_{ij}-J^{\mathrm{lower}}_{ij} by Appendix A.1. The lower part and the equality-boundary correction E a, b E_{a,b} are explicit power-sum expressions, whereas the upper part contains the recursive floor query. Hence record generation adds the known contribution

 | 𝐜 a, b closed:= − 8 ​ 𝒜 a, b ​ ( J lower) − E a, b, \mathbf{c}^{\mathrm{closed}}_{a,b}:=-8\mathcal{A}_{a,b}(J^{\mathrm{lower}})-E_{a,b}, |  | (67) |

and, after the selected cell operator has returned the six staircase moments, adds

 | 𝐜 a, b query:= 8 ​ 𝒜 a, b ​ ( J upper). \mathbf{c}^{\mathrm{query}}_{a,b}:=8\mathcal{A}_{a,b}(J^{\mathrm{upper}}). |  | (68) |

Their sum is exactly the contribution of ( a, b) (a,b) to the layer triple. A nonempty record stores the root state of Definition 2, its stopped terminal pair ( M, R) (M,R), and η \eta. The pointwise recursion recovers its intercept from β = a − u − 1 \beta=a-u-1.

For every integer x ⩾ 0 x\geqslant 0, define the three weighted Möbius prefixes

 | 𝔐 s ( x) = ∑ d ⩽ x μ ( d) d s, s = 0, 1, 2. \mathfrak{M}_{s}(x)=\sum_{d\leqslant x}\mu(d)d^{s},\qquad s=0,1,2. |  |

Thus 𝔐 s ​ ( 0) = 0 \mathfrak{M}_{s}(0)=0. For x ⩾ 1 x\geqslant 1, the identity ∑ d | k μ ( d) = [k = 1] \sum_{d\mid k}\mu(d)=[k=1] gives

 | 𝔐 s ​ ( x) = 1 − ∑ j = 2 x j s ​ 𝔐 s ​ ( ⌊ x / j ⌋). \mathfrak{M}_{s}(x)=1-\sum_{j=2}^{x}j^{s}\mathfrak{M}_{s}(\left\lfloor x/j\right\rfloor). |  | (69) |

Equal quotients in this recurrence are grouped into constant-time blocks by the ordinary power sums. If κ ⁡ ( D) \kappa(D) denotes the terminal threshold for layer cap D D, put

 | κ max ​ ( n) = max 1 ⩽ D ⩽ ⌊ n ⌋ ⁡ κ ⁡ ( D). \kappa_{\max}(n)=\max_{1\leqslant D\leqslant\left\lfloor\sqrt{n}\right\rfloor}\kappa(D). |  |

It is obtained by one scan over these D D values; this costs O ⁡ ( n) O(\sqrt{n}) arithmetic operations and O ⁡ ( 1) O(1) additional words. The periodic table is constructed once at limit κ max ​ ( n) \kappa_{\max}(n) and shared by all layer calls.

Algorithm 1: Quotient-blocked O ⁡ ( n ​ log ⁡ n) O(n\log n) algorithm.

1 | procedure RectangleCount ​ ( n) \textsc{RectangleCount}(n) |

2 | initialize 𝔐 0, 𝔐 1, 𝔐 2 \mathfrak{M}_{0},\mathfrak{M}_{1},\mathfrak{M}_{2} by ( 69) |

3 | construct the read-only periodic table 𝖳 κ max ​ ( n) \mathsf{T}_{\kappa_{\max}(n)} |

4 | a ​ n ​ s ← F 0 ​ ( n) ans\leftarrow F_{0}(n) from ( 1); ℓ ← 1 \ell\leftarrow 1 |

5 | while ℓ ⩽ n \ell\leqslant n do |

6 | N ← ⌊ n / ℓ ⌋ N\leftarrow\left\lfloor n/\ell\right\rfloor; r end ← ⌊ n / N ⌋ r_{\rm end}\leftarrow\left\lfloor n/N\right\rfloor |

7 | for s = 0, 1, 2 s=0,1,2 do Δ s ← 𝔐 s ​ ( r end) − 𝔐 s ​ ( ℓ − 1) \Delta_{s}\leftarrow\mathfrak{M}_{s}(r_{\rm end})-\mathfrak{M}_{s}(\ell-1) |

8 | if ( Δ 0, Δ 1, Δ 2) ≠ ( 0, 0, 0) (\Delta_{0},\Delta_{1},\Delta_{2})\neq(0,0,0) then |

9 | ( A N, B N, C N) ← RecursiveLayer ​ ( N, 𝖳 κ max ​ ( n)) (A_{N},B_{N},C_{N})\leftarrow\textsc{RecursiveLayer}(N,\mathsf{T}_{\kappa_{\max}(n)}) |

10 | a ​ n ​ s ← a ​ n ​ s + n 2 ​ A N ​ Δ 0 − n ​ B N ​ Δ 1 + C N ​ Δ 2 ans\leftarrow ans+n^{2}A_{N}\Delta_{0}-nB_{N}\Delta_{1}+C_{N}\Delta_{2} |

11 | end if; ℓ ← r end + 1 \ell\leftarrow r_{\rm end}+1 |

12 | end while; return a ​ n ​ s ans |

13 | end procedure |

Algorithm 2: Batched divisor layer.

1 | procedure RecursiveLayer ​ ( N, 𝖳) \textsc{RecursiveLayer}(N,\mathsf{T}) |

2 | compute ( D, σ, τ, κ) (D,\sigma,\tau,\kappa) by ( 14) |

3 | Z ← 𝒟 ⁡ ( N) Z\leftarrow\mathcal{D}(N) from ( 29) |

4 | traverse the coefficient-cone recursion P ↦ P ​ Q ​ ( A) P\mapsto PQ(A) |

5 | for every reached cone P P do |

6 | construct the symbolic true-marker slots and their traces as in Appendix B.3 |

7 | compile all 𝖮𝗉 P; i, j \mathsf{Op}_{P;i,j} through the shared prefix tree |

8 | construct both uniform grids and their correction data |

9 | for every stopped pair ( M, R) ∈ 𝒯 ⁡ ( P) (M,R)\in\mathcal{T}(P) do |

10 | ( a b) ← P ​ ( M R) \binom{a}{b}\leftarrow P\binom{M}{R}; compute 𝐜 a, b closed \mathbf{c}^{\mathrm{closed}}_{a,b}; Z ← Z + 𝐜 a, b closed Z\leftarrow Z+\mathbf{c}^{\mathrm{closed}}_{a,b}; generate the possible query record |

11 | if q > 0 q>0 then |

12 | if q ⩽ 5 ​ τ q\leqslant 5\tau then |

13 | obtain 𝚽 \boldsymbol{\Phi} directly from ( 53)–( 54) |

14 | else compute the two marker codes, derive ( i, j) (i,j) by ( 45), and access 𝖮𝗉 P; i, j \mathsf{Op}_{P;i,j} |

15 | evaluate the affine terminal coordinates; obtain 𝐋 term \mathbf{L}_{\mathrm{term}} from 𝖳 \mathsf{T} |

16 | 𝐋 root ← 𝖴 P; i, j ​ 𝐋 term + Π P; i, j ​ ( q, h) \mathbf{L}_{\rm root}\leftarrow\mathsf{U}_{P;i,j}\mathbf{L}_{\mathrm{term}}+\Pi_{P;i,j}(q,h); convert 𝐋 root \mathbf{L}_{\rm root} to 𝚽 \boldsymbol{\Phi} by ( 8) |

17 | end if; form J upper J^{\mathrm{upper}} from 𝚽 \boldsymbol{\Phi} and η \eta by ( 23) |

18 | Z ← Z + 8 ​ 𝒜 a, b ​ ( J upper) Z\leftarrow Z+8\mathcal{A}_{a,b}(J^{\mathrm{upper}}) |

19 | end if |

20 | end for; discard the path-local objects |

21 | end for; return Z = ( A ⁡ ( N), B ⁡ ( N), C ⁡ ( N)) Z=(A(N),B(N),C(N)) |

22 | end procedure |

For correctness, Lemma 1 produces exactly the closed correction and floor-moment record for every direction pair, and Lemma 8 assigns that pair to exactly one accepted coefficient path. Theorem 11 selects its exact true marker rectangle. Lemmas 13 and 15 evaluate every long record, while Section 9 handles every short record. Thus Algorithm 2 contributes every term of ( 30) once. Finally, ( 69) and quotient blocking give ( 5), so Algorithm 1 returns ( 3).

Executable cone traversal. Algorithm 3 expands the “traverse” line of Algorithm 2. The predicate Root ⁡ ( P, M, R) \operatorname{Root}(P,M,R) abbreviates

 | 1 ⩽ π 21 ​ M + π 22 ​ R < π 11 ​ M + π 12 ​ R ⩽ D. 1\leqslant\pi_{21}M+\pi_{22}R<\pi_{11}M+\pi_{12}R\leqslant D. |  |

An intersection with this predicate is an integer interval: its endpoints are obtained by signed ceiling and floor divisions as follows. For fixed R R, a ⩽ D a\leqslant D gives M ⩽ ⌊ ( D − π 12 ​ R) / π 11 ⌋ M\leqslant\left\lfloor(D-\pi_{12}R)/\pi_{11}\right\rfloor; if π 21 > 0 \pi_{21}>0, then b ⩾ 1 b\geqslant 1 gives M ⩾ ⌈ ( 1 − π 22 ​ R) / π 21 ⌉ M\geqslant\left\lceil(1-\pi_{22}R)/\pi_{21}\right\rceil; and if π 11 > π 21 \pi_{11}>\pi_{21}, then b < a b<a gives

 | M ⩾ ⌊ ( π 22 − π 12) ​ R π 11 − π 21 ⌋ + 1. M\geqslant\left\lfloor\frac{(\pi_{22}-\pi_{12})R}{\pi_{11}-\pi_{21}}\right\rfloor+1. |  |

If π 21 = 0 \pi_{21}=0, the condition b ⩾ 1 b\geqslant 1 is checked directly; if π 11 = π 21 \pi_{11}=\pi_{21}, the condition b < a b<a reduces to π 22 ​ R < π 12 ​ R \pi_{22}R<\pi_{12}R. Empty intervals are ignored. Procedure Emit executes the complete inner-loop action of Algorithm 2 for one stopped pair: it adds the closed correction and, when the query is nonempty, evaluates either its short or its long record. The traversal starts with VisitCone ​ ( I, ⊥) \textsc{VisitCone}(I,\bot), where I I is the identity matrix and the absent last quotient is never read.

Algorithm 3: Depth-first visit of one coefficient cone.

1 | procedure VisitCone ​ ( P, A last) \textsc{VisitCone}(P,A_{\rm last}) |

2 | e ← ext ⁡ ( P) e\leftarrow\operatorname{ext}(P) |

3 | construct the path slots, traces, operators, grids, and correction data |

4 | for 1 ⩽ M ⩽ τ 1\leqslant M\leqslant\tau and 0 ⩽ R < M 0\leqslant R<M do |

5 | if Root ⁡ ( P, M, R) \operatorname{Root}(P,M,R) and ( P = I P=I or A last ​ M + R > τ A_{\rm last}M+R>\tau) then Emit ​ ( P, M, R) \textsc{Emit}(P,M,R) |

6 | end for |

7 | if P ≠ I P\neq I and A last ⩾ 2 A_{\rm last}\geqslant 2 then |

8 | for τ < M ⩽ ⌊ D / π 11 ⌋ \tau<M\leqslant\left\lfloor D/\pi_{11}\right\rfloor with Root ⁡ ( P, M, 0) \operatorname{Root}(P,M,0) do Emit ​ ( P, M, 0) \textsc{Emit}(P,M,0) |

9 | end if; A stop ← e + 1 A_{\rm stop}\leftarrow e+1 |

10 | for 1 ⩽ R ⩽ ⌊ D / ( π 11 ​ A stop + π 12) ⌋ 1\leqslant R\leqslant\left\lfloor D/(\pi_{11}A_{\rm stop}+\pi_{12})\right\rfloor do |

11 | ℐ R ← [max ⁡ { τ + 1, A stop ​ R, R + 1 }, ⌊ ( D − π 12 ​ R) / π 11 ⌋] \mathcal{I}_{R}\leftarrow[\max\{\tau+1,A_{\rm stop}R,R+1\},\left\lfloor(D-\pi_{12}R)/\pi_{11}\right\rfloor] |

12 | ℐ R ← ℐ R ∩ { M: Root ⁡ ( P, M, R) } \mathcal{I}_{R}\leftarrow\mathcal{I}_{R}\cap\{M:\operatorname{Root}(P,M,R)\} |

13 | for M ∈ ℐ R ∩ ℤ M\in\mathcal{I}_{R}\cap\mathbb{Z} do Emit ​ ( P, M, R) \textsc{Emit}(P,M,R) |

14 | end for |

15 | discard the path-local objects |

16 | for 1 ⩽ A ⩽ e 1\leqslant A\leqslant e do VisitCone ​ ( P ​ Q ​ ( A), A) \textsc{VisitCone}(PQ(A),A) |

17 | end procedure |

The three emission blocks are respectively the small-modulus, zero-remainder, and overflow pieces of 𝒯 ⁡ ( P) \mathcal{T}(P). The recursive calls are precisely the accepted continuations, so Lemma 8 proves that the visitor emits every root pair once. At a visited path, the path-local setup is also explicit: order the L L sample residues used in ( 35); fold one representative of every nonempty slot to obtain its marker word; pair the two word lists in a prefix tree and compose the corresponding cycle operators; then form the groups K 0, K 1 K_{0},K_{1} and their prefix counts. The implementation evaluates ( 44)–( 45) on demand instead of materializing ( 46). Only after this setup does Emit stream the stopped pairs of that path.

Worked record. Take the layer N = 100 N=100. Then

 | ( D, σ, τ, κ) = ( 10, 4, 2, 5). (D,\sigma,\tau,\kappa)=(10,4,2,5). |  |

For ( a, b) = ( 4, 3) (a,b)=(4,3), the half-domain formulas give

 | q sq = 28, q = 13, N − b ​ q = 61 = 15 ​ a + 1, q_{\rm sq}=28,\qquad q=13,\qquad N-bq=61=15a+1, |  |

so η = 15 \eta=15, β = 1 \beta=1, and the root state is

 | ( a, b, q, h, u, v) = ( 4, 3, 13, 9, 2, 1). (a,b;q,h;u,v)=(4,3;13,9;2,1). |  |

Its first coefficient quotient is one. Thus P = Q ⁡ ( 1) = ( 1 1 1 0) P=Q(1)=\left(\begin{smallmatrix}1&1\\ 1&0\end{smallmatrix}\right) is accepted, the terminal pair is ( M, R) = ( 3, 1) (M,R)=(3,1), and the next quotient three is rejected because P ​ Q ​ ( 3) PQ(3) has an entry four, exceeding τ \tau.

Here L = 1 + χ 1 = 2 L=1+\chi_{1}=2 and the true boundary residues are 0 0 and 3 3 modulo H = 4 H=4. Since 2 ​ R ⩽ M 2R\leqslant M, grid zero is selected; it has T = π 11 = 1 T=\pi_{11}=1 cell. Both markers have code ( 0, 0) (0,0), so the code-to-slot map selects the unique nonempty rectangle containing ( u, v) = ( 2, 1) (u,v)=(2,1) and its operator with quotient triple ( A, U, V) = ( 1, 0, 0) (A,U,V)=(1,0,0). One cycle gives

 | ( 3, 1, 9, 3, 0, 1). (3,1;9,3;0,1). |  |

Because M = 3 ⩽ κ M=3\leqslant\kappa, the terminal table answers f ′ ​ ( k) = ⌊ ( k + 2) / 3 ⌋ f^{\prime}(k)=\left\lfloor(k+2)/3\right\rfloor for 0 ⩽ k < 9 0\leqslant k<9 with

 | 𝐋 term = ( 15, 81, 507, 24, 141, 46) 𝖳. \mathbf{L}_{\rm term}=(15,81,507,24,141,46)^{\mathsf{T}}. |  |

The one-cycle operator ( 18) lifts this to

 | 𝐋 root = ( 57,477, 4475, 204, 1887, 996) 𝖳, \mathbf{L}_{\rm root}=(57,477,4475,204,1887,996)^{\mathsf{T}}, |  |

and ( 8) gives

 | 𝚽 = ( 57,477, 4475, 351, 3297, 2433) 𝖳. \boldsymbol{\Phi}=(57,477,4475,351,3297,2433)^{\mathsf{T}}. |  |

With η = 15 \eta=15, Equation ( 23), in the order J 00, J 01, J 02, J 10, J 11, J 20 J_{00},J_{01},J_{02},J_{10},J_{11},J_{20}, yields

 | J upper = ( 252, 1629, 13991, 2619, 15645, 36061). J^{\rm upper}=(252,1629,13991,2619,15645,36061). |  |

Hence the deferred contribution is

 | 8 ​ 𝒜 4, 3 ​ ( J upper) = ( 2016, 237888, 7933992). 8\mathcal{A}_{4,3}(J^{\rm upper})=(2016,237888,7933992). |  |

For completeness, the explicit lower moments are ( 94,823, 8287, 463, 4561, 3207) (94,823,8287,463,4561,3207) in the same order, and E 4, 3 = ( 12,504, 5376) E_{4,3}=(12,504,5376). Thus 𝐜 4, 3 closed = ( − 764, − 72520, − 2021000) \mathbf{c}^{\rm closed}_{4,3}=(-764,-72520,-2021000), and the complete contribution of this record to the layer accumulator is

 | ( 1252, 165368, 5912992). (1252,165368,5912992). |  |

### B.8 Detailed O ⁡ ( n ​ log ⁡ n) O(n\log n) complexity accounting

From ( 14),

 | D 2 = O ⁡ ( N), τ 4 = O ⁡ ( N), κ 3 = O ⁡ ( N 3 / 4). D^{2}=O(N),\qquad\tau^{4}=O(N),\qquad\kappa^{3}=O(N^{3/4}). |  |

The scales are linked. The half-domain reduction needs every pair up to D = ⌊ N ⌋ D=\left\lfloor\sqrt{N}\right\rfloor. The coefficient-cone and marker-table work is linear only if τ 4 = O ⁡ ( D 2) \tau^{4}=O(D^{2}), hence τ = O ⁡ ( D) \tau=O(\sqrt{D}). Lemma 7 needs τ ​ κ ⩾ D \tau\kappa\geqslant D, so then κ = Ω ⁡ ( D) \kappa=\Omega(\sqrt{D}). Thus τ, κ = Θ ⁡ ( D) \tau,\kappa=\Theta(\sqrt{D}) is the common boundary that preserves linear time and minimizes the terminal-table memory within this construction.

object | arithmetic operations |

coefficient-cone nodes and stopped pairs | O ⁡ ( D 2 + τ 4) O(D^{2}+\tau^{4}) |

all boundary grids and correction data | O ⁡ ( τ 4) O(\tau^{4}) |

all cell-operator compilations | O ⁡ ( τ 4) O(\tau^{4}) |

record generation and long-record applications | O ⁡ ( D 2) O(D^{2}) |

reduced periodic table | O ⁡ ( κ 3) O(\kappa^{3}) |

short-query pointwise evaluations | O ⁡ ( D ​ τ ​ log ⁡ ( 2 + τ)) O(D\tau\log(2+\tau)) |

There are O ⁡ ( τ 2) O(\tau^{2}) paths. Each has L ⩽ 3 ​ τ L\leqslant 3\tau, so its true intervals, L 2 L^{2} operators, and two grids with their prefix data together cost O ⁡ ( τ 2) O(\tau^{2}); over all paths this is O ⁡ ( τ 4) O(\tau^{4}). Long records take constant time and Theorem 16 gives D ​ τ ​ log ⁡ ( 2 + τ) = o ⁡ ( N) D\tau\log(2+\tau)=o(N). Processing one path at a time uses O ⁡ ( τ 2) O(\tau^{2}) live words, while the periodic prefixes use O ⁡ ( κ 3) O(\kappa^{3}) words and dominate. This completes the detailed proof of Theorem 17.

#### B.8.1 Weighted Möbius prefix computation

Algorithms for isolated values of the unweighted Mertens function provide the standard context for this quotient-block approach [10]; here the same decomposition is applied to the three weighted prefixes required by ( 69). Let S μ S_{\mu} be a sieve cutoff. Sieving all arguments up to S μ S_{\mu} costs O ⁡ ( S μ) O(S_{\mu}) time and storage. The larger distinct arguments have the form ⌊ n / j ⌋ \left\lfloor n/j\right\rfloor with j ⩽ n / S μ j\leqslant n/S_{\mu}. Evaluate each such argument once, in increasing order, and memoize its three weighted prefix values. If x = ⌊ n / j ⌋ x=\left\lfloor n/j\right\rfloor, every nontrivial recursive child, with k ⩾ 2 k\geqslant 2, satisfies

 | ⌊ ⌊ n / j ⌋ / k ⌋ = ⌊ n / ( j ​ k) ⌋. \left\lfloor\left\lfloor n/j\right\rfloor/k\right\rfloor=\left\lfloor n/(jk)\right\rfloor. |  |

It is therefore either covered by the sieve or is another member of the same memoized distinct-quotient set, and it is already available in this order. Since the quotient-block recurrence for one argument x x has O ⁡ ( x) O(\sqrt{x}) blocks, the total cost after memoization is bounded by

 | ∑ j ⩽ n / S μ n / j = O ( n S μ − 1 / 2). \sum_{j\leqslant n/S_{\mu}}\sqrt{n/j}=O(nS_{\mu}^{-1/2}). |  |

Thus the combined bound is O ⁡ ( S μ + n / S μ) O(S_{\mu}+n/\sqrt{S_{\mu}}). Balancing its two terms gives S μ = n / S μ S_{\mu}=n/\sqrt{S_{\mu}} and hence S μ = n 2 / 3 S_{\mu}=n^{2/3}. With S μ = ⌈ n 2 / 3 ⌉ S_{\mu}=\left\lceil n^{2/3}\right\rceil, the prefix computation takes O ⁡ ( n 2 / 3) O(n^{2/3}) time and storage.

###### Proof of Lemma 20.

Root coefficient, marker, and length coordinates are at most n n. An accepted continuant matrix has entries at most τ \tau. If A 0, …, A d − 1 A_{0},\ldots,A_{d-1} are the coefficient quotients of its path, then

 | ∏ i A i ⩽ π 11 ⩽ τ, d = O ⁡ ( log ⁡ ( 2 + τ)). \prod_{i}A_{i}\leqslant\pi_{11}\leqslant\tau,\qquad d=O(\log(2+\tau)). |  |

Every local affine-state coefficient is O ⁡ ( A i + 2) O(A_{i}+2) because 0 ⩽ U i, V i ⩽ A i 0\leqslant U_{i},V_{i}\leqslant A_{i}. Composition in a fixed degree-four polynomial basis enlarges coefficient magnitudes by at most C ​ ( A i + 2) C C(A_{i}+2)^{C} for an absolute constant C C. Since every A i ⩾ 1 A_{i}\geqslant 1,

 | ∏ i C ​ ( A i + 2) C ⩽ C d ​ 3 C ​ d ​ ( ∏ i A i) C ⩽ C d ​ 3 C ​ d ​ τ C = τ O ⁡ ( 1), \prod_{i}C(A_{i}+2)^{C}\leqslant C^{d}3^{Cd}\Bigl(\prod_{i}A_{i}\Bigr)^{C}\leqslant C^{d}3^{Cd}\tau^{C}=\tau^{O(1)}, |  |

where the last equality uses d = O ⁡ ( log ⁡ ( 2 + τ)) d=O(\log(2+\tau)). Thus every coefficient stored in an affine endpoint, terminal marker, moment map, or boundary correction is n O ⁡ ( 1) n^{O(1)}. More explicitly, | 𝔐 s ​ ( x) | ⩽ ∑ d ⩽ x d s ⩽ n s + 1 |\mathfrak{M}_{s}(x)|\leqslant\sum_{d\leqslant x}d^{s}\leqslant n^{s+1} for s = 0, 1, 2 s=0,1,2. Every floor or periodic moment sums at most n n terms whose coordinates are at most n n, and hence is n O ⁡ ( 1) n^{O(1)}. Each layer and final accumulator combines only polynomially many such terms; multiplication by the fixed-dimensional operator coefficients therefore preserves a polynomial bound. Finally F ⁡ ( n) ⩽ ( n 2 4) = O ⁡ ( n 8) F(n)\leqslant\binom{n^{2}}{4}=O(n^{8}). Thus every intermediate sum and product is n O ⁡ ( 1) n^{O(1)} and has O ⁡ ( log ⁡ n) O(\log n) bits. ∎

## References

- [1] T. M. Apostol (1976) Introduction to analytic number theory. Undergraduate Texts in Mathematics, Springer. External Links: [Document][3] Cited by: §2.
- [2] D. Babichev and S. Babichev (2026) Counting all lattice rectangles in the square grid in near-linear time. External Links: 2604.22456, [Document][4] Cited by: §1, §1.
- [3] D. Babichev and D. Pinchuk Computing all lattice-rectangle counts by rational staircase sums. Note: Manuscript in preparation, 2026 Cited by: §1.
- [4] A. I. Barvinok (1994) A polynomial time algorithm for counting integral points in polyhedra when the dimension is fixed. Mathematics of Operations Research 19 ( 4), pp. 769–779. External Links: [Document][5] Cited by: §1.
- [5] M. Beck, C. Haase, and A. R. Matthews (2008) Dedekind–Carlitz polynomials as lattice-point enumerators in rational polyhedra. Mathematische Annalen 341 ( 4), pp. 945–961. External Links: [Document][6] Cited by: §1.
- [6] M. Beck and F. Kohl (2014) Rademacher–Carlitz polynomials. Acta Arithmetica 163 ( 4), pp. 379–393. External Links: [Document][7] Cited by: §1.
- [7] M. Beck and S. Robins (2015) Computing the continuous discretely: integer-point enumeration in polyhedra. 2 edition, Undergraduate Texts in Mathematics, Springer. External Links: [Document][8] Cited by: §1, §3.
- [8] R. P. Brent and P. Zimmermann (2010) Modern computer arithmetic. Cambridge Monographs on Applied and Computational Mathematics, Vol. 18, Cambridge University Press. External Links: [Document][9] Cited by: §1, §1.
- [9] S. Brown (2026) On a family of sums of powers of the floor function and their links with generalized Dedekind sums. Notes on Number Theory and Discrete Mathematics 32 ( 1), pp. 76–87. External Links: [Document][10] Cited by: §1.
- [10] M. Deléglise and J. Rivat (1996) Computing the summation of the Möbius function. Experimental Mathematics 5 ( 4), pp. 291–295. External Links: [Document][11] Cited by: §B.8.1.
- [11] R. L. Graham, D. E. Knuth, and O. Patashnik (1994) Concrete mathematics. 2 edition, Addison–Wesley. Cited by: §3.
- [12] D. Harvey and J. van der Hoeven (2021) Integer multiplication in time O ⁡ ( n ​ log ⁡ n) O(n\log n). Annals of Mathematics 193 ( 2), pp. 563–617. External Links: [Document][12] Cited by: §1.
- [13] M. N. Huxley and W. G. Nowak (1996) Primitive lattice points in convex planar domains. Acta Arithmetica 76 ( 3), pp. 271–283. External Links: [Document][13] Cited by: §1.
- [14] D. H. Lehmer (1938) Euclid’s algorithm for large numbers. The American Mathematical Monthly 45 ( 4), pp. 227–233. External Links: [Document][14] Cited by: §1.
- [15] OEIS Foundation A085582: number of rectangles with corners on an n × n n\times n grid. External Links: [Link][15] Cited by: §1.
- [16] J. Pawlewicz and M. Pătraşcu (2009) Order statistics in the Farey sequences in sublinear time and counting primitive lattice points in polygons. Algorithmica 55 ( 2), pp. 271–282. External Links: [Document][16] Cited by: §1.
- [17] A. M. Rockett and P. Szüsz (1992) Continued fractions. World Scientific. External Links: [Document][17] Cited by: §1.
- [18] A. Schönhage and V. Strassen (1971) Schnelle multiplikation großer zahlen. Computing 7 ( 3–4), pp. 281–292. External Links: [Document][18] Cited by: §1.
- [19] J. von zur Gathen and J. Gerhard (2013) Modern computer algebra. 3 edition, Cambridge University Press. External Links: [Document][19] Cited by: §1.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://dx.doi.org/10.1007/978-1-4757-5579-4
[4]: https://dx.doi.org/10.48550/arXiv.2604.22456
[5]: https://dx.doi.org/10.1287/moor.19.4.769
[6]: https://dx.doi.org/10.1007/s00208-008-0220-9
[7]: https://dx.doi.org/10.4064/aa163-4-6
[8]: https://dx.doi.org/10.1007/978-1-4939-2969-6
[9]: https://dx.doi.org/10.1017/CBO9780511921698
[10]: https://dx.doi.org/10.7546/nntdm.2026.32.1.76-87
[11]: https://dx.doi.org/10.1080/10586458.1996.10504594
[12]: https://dx.doi.org/10.4007/annals.2021.193.2.4
[13]: https://dx.doi.org/10.4064/aa-76-3-271-283
[14]: https://dx.doi.org/10.1080/00029890.1938.11990797
[15]: https://oeis.org/A085582
[16]: https://dx.doi.org/10.1007/s00453-008-9221-z
[17]: https://dx.doi.org/10.1142/1725
[18]: https://dx.doi.org/10.1007/BF02242355
[19]: https://dx.doi.org/10.1017/CBO9781139856065
