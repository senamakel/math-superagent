<!-- source: https://arxiv.org/html/2004.10189v5 | converted from HTML -->

Counting points on superelliptic curves in average polynomial time

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2004.10189v5 [math.NT] 20 Feb 2025

# Counting points on superelliptic curves in average polynomial time Thanks: The author was supported by Simons Foundation grant 550033

Andrew V. Sutherland

###### Abstract.

We describe the practical implementation of an average polynomial-time algorithm for counting points on superelliptic curves defined over 𝐐 \mathbf{Q} that is substantially faster than previous approaches. Our algorithm takes as input a superelliptic curve y m = f ⁡ ( x) y^{m}=f(x) with m ≥ 2 m\geq 2 and f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] any squarefree polynomial of degree d ≥ 3 d\geq 3, along with a positive integer N N. It can compute #​ X ​ ( 𝐅 p) \#X(\mathbf{F}_{p}) for all p ≤ N p\leq N not dividing m ​ lc ⁡ ( f) ​ disc ​ ( f) m\operatorname{lc}(f)\operatorname{disc}(f) in time O ⁡ ( m ​ d 3 ​ N ​ log 3 ​ N ​ log ⁡ log ⁡ N) O(md^{3}N\log^{3}N\log\log N). It achieves this by computing the trace of the Cartier–Manin matrix of reductions of X X. We can also compute the Cartier–Manin matrix itself, which determines the p p -rank of the Jacobian of X X and the numerator of its zeta function modulo p p.

In memory of [Peter L. Montgomery][3].

## 1. Introduction

Let X / k X/k by a smooth projective curve of genus g > 0 g>0 whose function field is defined by an equation of the form

 | y m = f ⁡ ( x), y^{m}=f(x), |  |

with m > 1 m>1 prime to the characteristic p p of k k and f ∈ k ⁡ [x] f\in k[x] a squarefree polynomial of degree d ≥ 3 d\geq 3. We shall call such a curve X X a superelliptic curve. We note that not all authors require f f to be squarefree or p - m p\nmid m, while others require d d and m m to be coprime; our definition follows the convention in [23, 31] and is equivalent to the class of cyclic covers of 𝐏 1 \mathbf{P}^{1} considered in [2, 14]. One can compute the genus of X X as

(1) |  | g = ( d − 2) ​ ( m − 1) + m − gcd ⁡ ( m, d) 2, g=\frac{(d-2)(m-1)+m-\gcd(m,d)}{2}, |  |

via the Riemann-Hurwitz formula. Well known examples of superelliptic curves include elliptic curves, hyperelliptic curves, Picard curves, and Fermat curves.

We are primarily interested in k = 𝐐 k=\mathbf{Q} where X X has an associated L L -function L ⁡ ( X, s) = ∑ a n ​ n − s L(X,s)=\sum a_{n}n^{-s} that we would like to “compute”. For us this means computing the integers a n a_{n} for all n n up to a bound N N that is large enough for us to approximate special values of L ⁡ ( X, s) L(X,s) to high precision, and to compute upper bounds on its analytic rank that we can reasonably expect to be sharp. This requires N N to be on the order of the square root of the conductor of the Jacobian of X X, and in practice we typically take N N to be about 30 times this value.

The fact that L ⁡ ( X, s) L(X,s) is defined by an Euler product implies that it suffices to compute a n a_{n} for prime powers n ≤ N n\leq N. Nearly all of the prime powers n ≤ N n\leq N are in fact primes p p, so this task is overwhelmingly dominated by the time to compute a p a_{p} for primes p ≤ N p\leq N. Indeed, if we spend O ⁡ ( p e − 1 ​ log 2 ​ p) O(p^{e-1}\log^{2}p) time computing each a p e ≤ N a_{p^{e}}\leq N with e > 1 e>1, we will have spent only O ⁡ ( N ​ log ⁡ N) O(N\log N) time, which is roughly the time it takes just to write down the a n a_{n} for n ≤ N n\leq N. For primes of good reduction for X X, which includes all p - m ​ lc ⁡ ( f) ​ disc ​ ( f) p\nmid m\operatorname{lc}(f)\operatorname{disc}(f), 1 1 1 When m m divides d d there may be good primes that divide lc ⁡ ( f) \operatorname{lc}(f), but to simplify the presentation we shall exclude them. we can compute a p a_{p} as

 | a p = p + 1 − #​ X ​ ( 𝐅 p), a_{p}=p+1-\#X(\mathbf{F}_{p}), |  |

in other words, by counting points on the reduction of X X modulo p p. See [7] for a discussion of how primes of bad reduction may be treated. Alternatively, if one is willing to assume that the Hasse-Weil conjecture for L ⁡ ( X, s) L(X,s) holds, one can use the knowledge of a n a_{n} at powers of good primes to determine the a n a_{n} at powers of bad primes (and in particular, the primes p | m p|m not treated by [7]) by using the functional equation to rule out all but one possibility; see [3, §5] for a discussion of this approach when g = 2 g=2.

Another motivation for computing a p a_{p} for good primes p ≤ N p\leq N is to compute the sequence of normalized Frobenius traces a p / p a_{p}/\sqrt{p} that appear in generalizations of the Sato-Tate conjecture. The moments of this distribution encode certain arithmetic invariants of X X, including, for example, the rank of the endomorphism ring of its Jacobian [10, Prop, 1], as well as information about its Sato-Tate group [28, 12]. Indeed, the initial motivation for this work (and its first application) was to compute Sato-Tate distributions for the three types of genus 3 superelliptic curves with ( m, d) ∈ { ( 3, 4), ( 4, 3), ( 4, 4) } (m,d)\in\{(3,4),(4,3),(4,4)\} that arise as smooth plane quartics in the database described in [30], which played a role in the recent classification of Sato–Tate groups of abelian threefolds [13]. The sequence of normalized Frobenius traces can also be used to numerically investigate the error term in the Sato-Tate conjecture, and in particular, predictions regarding its leading constant [8]. The ability to efficiently compute many integer values of a p a_{p} also supports investigations of generalizations of the Lang-Trotter conjecture, as well as a recent question of Serre regarding the density of “record” primes, those for which − a p > 2 ​ g ​ p − 1 -a_{p}>2g\sqrt{p}-1 [29].

The algorithm we present here actually does more than just compute a p a_{p}. Following the approach of [20, 21, 22], which treated the case of hyperelliptic curves, for each good prime p p we compute a g × g g\times g matrix A p A_{p} giving the action of the Cartier–Manin operator on a basis for the space of regular differentials of the reduction of X X modulo p p; see § 2 for details. This matrix A p A_{p} is the transpose of the Hasse–Witt matrix, and like the Hasse–Witt matrix it satisfies the identity

 | det ( I − T ​ A p) ≡ L p ​ ( T) mod p, \det(I-TA_{p})\equiv L_{p}(T)\bmod p, |  |

where L p ​ ( T) L_{p}(T) is the integer polynomial that appears in both the Euler product L ⁡ ( X, s) = ∏ p L p ​ ( p − s) − 1 L(X,s)=\prod_{p}L_{p}(p^{-s})^{-1} and the numerator of the zeta function of the reduction of X X modulo p p:

 | Z p ​ ( T):= exp ⁡ ( ∑ n ≥ 1 #​ X ​ ( 𝐅 p n) ​ T n n) = L p ​ ( T) ( 1 − T) ​ ( 1 − p ​ T). Z_{p}(T):=\exp\left(\sum_{n\geq 1}\#X(\mathbf{F}_{p^{n}})\frac{T^{n}}{n}\right)=\frac{L_{p}(T)}{(1-T)(1-pT)}. |  |

In particular, we have a p ≡ tr ⁡ A p mod p a_{p}\equiv\operatorname{tr}A_{p}\bmod p, and for p > 16 ​ g 2 p>16g^{2} this uniquely determines a p ∈ 𝐙 a_{p}\in\mathbf{Z}, since | a p | ≤ 2 ​ g ​ p |a_{p}|\leq 2g\sqrt{p}, by the Weil bounds. The matrix A p A_{p} is also of independent interest, since it can be used to compute the p p -rank of the reduction of X X modulo p p, something that cannot be deduced solely from L p ​ ( T) mod p L_{p}(T)\bmod p.

Our main result is the following theorem, in which ‖ f ‖ ≔ log ⁡ max i ​ | f i | \|f\|\coloneqq\log\max_{i}|f_{i}| denotes the logarithmic height of a nonzero integer polynomial f ⁡ ( x) = ∑ i f i ​ x i f(x)=\sum_{i}f_{i}x^{i}.

###### 1.

Given a superelliptic curve X: y m = f ⁡ ( x) X\colon y^{m}=f(x) with f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] of degree d d and N ∈ 𝐙 > 0 N\in\mathbf{Z}_{>0}, the algorithm ComputeCartierManinMatrices outputs the Cartier–Manin matrices A p A_{p} of the reductions of X X modulo all primes p ≤ N p\leq N not dividing m ​ lc ⁡ ( f) ​ disc ​ ( f) m\operatorname{lc}(f)\operatorname{disc}(f). If we assume m m, d d, ‖ f ‖ \|f\| are bounded by O ⁡ ( log ⁡ N) O(\log N) the algorithm runs in O ⁡ ( m 2 ​ d 3 ​ N ​ log 3 ​ N) O(m^{2}d^{3}N\log^{3}\!N) time using O ⁡ ( m ​ d 2 ​ N) O(md^{2}N) space; it can alternatively compute Frobenius traces a p ∈ 𝐙 a_{p}\in\mathbf{Z} for p ≤ N p\leq N in time O ⁡ ( m ​ d 3 ​ N ​ log 3 ​ N) O(md^{3}N\log^{3}\!N).

###### Remark 2.

The assumption m, d, ‖ f ‖ = O ⁡ ( log ⁡ N) m,d,\|f\|=O(\log N) ensures that the complexity of multiplying the integer matrices used in the algorithm is dominated by the cost of computing FFT transforms of the matrix entries, which eliminates any dependence on the exponent ! \omega of matrix multiplication; one can replace d 3 d^{3} with d! + 1 d^{\omega+1} and then remove this assumption. We note that our complexity bound relies on the recently improved 𝖬 ⁡ ( n) = n ​ log ⁡ n \M(n)=n\log n bound on integer multiplication [18]. While the algorithm that achieves this bound is not practical, many FFT-based implementations effectively achieve this growth rate within the feasible range of computation, which for our purposes, is certainly limited to integers that fit in random access memory; see [15, Alg. 8.25], for example.

We also obtain an algorithm that can be used to compute A p A_{p} for a single superelliptic curve X / 𝐅 p X/\mathbf{F}_{p}. The asymptotic complexity is comparable to that achieved in [2] which describes the algorithm that is now implemented in version 9 of Sage [25]. We include this result because it contains several components that are used by the average polynomial-time algorithm we present. We should emphasize that the algorithm in [2] can compute L p ​ ( T) mod p n L_{p}(T)\bmod p^{n} for any n ≥ 1 n\geq 1, and taking n n sufficiently large yields L p ∈ 𝐙 ⁡ [T] L_{p}\in\mathbf{Z}[T], whereas we focus solely on the case n = 1 n=1 (we gain a small but not particularly significant performance advantage in this case).

###### 3.

Given a superelliptic curve X: y m = f ⁡ ( x) X\colon y^{m}=f(x) with f ∈ 𝐅 p ​ [x] f\in\mathbf{F}_{p}[x] of degree d d, the algorithm ComputeCartierManinMatrix can compute the Cartier–Manin matrix of X X in O ⁡ ( m ​ d 3 ​ p 1 / 2 ​ log ⁡ p ⁡ ( d! − 2 ​ log ⁡ log ⁡ p + log ⁡ p)) O(md^{3}p^{1/2}\log p(d^{\omega-2}\log\log p+\log p)) time using O ⁡ ( m ​ d 2 ​ p 1 / 2 ​ log ⁡ p) O(md^{2}p^{1/2}\!\log p) space, and also in O ⁡ ( m ​ d 2 ​ ( p + d) ​ log ⁡ p ​ log ⁡ log ⁡ p) O(md^{2}(p+d)\log p\log\log p) time using O ⁡ ( ( m ​ d + d 2) ​ log ⁡ p) O((md+d^{2})\log p) space.

In the article [2] noted above the authors consider a particular curve

 | X: y 7 = x 3 + 4 ​ x 2 + 3 ​ x − 1, X\colon y^{7}=x^{3}+4x^{2}+3x-1, |  |

for which they estimate that it would take approximately six months (on a single core) for their algorithm to compute the L L -polynomials L p ​ ( T) L_{p}(T) for all primes p ≤ 2 24 p\leq 2^{24} of good reduction. This is an improvement over an estimated three years for an earlier algorithm due to Minzlaff [24] that is implemented in Magma [4]. Computing L p ​ ( T) mod p L_{p}(T)\bmod p is an easier problem that would likely take about a week or so using the algorithm in [2], based on timings taken using a representative sample of p ≤ 2 24 p\leq 2^{24}. The algorithm we present here can accomplish this task in half an hour, and less than ten minutes if we only compute Frobenius traces.

See Tables 1 and 2 in § 7 for detailed performance comparisons for various shapes of superelliptic curves.

## 2. The Cartier operator

For background on differentials of algebraic function fields we refer the reader to [9, §2] and [26, §4]. Let K K be a function field of one variable over a perfect field k k of characteristic p > 0 p>0 that we assume is the full field of constants of K K. Let K denote its module of differentials, which we identify with its module of Weil differentials via [26, Def. 4.17] and [26, Rm. 4.3.7]. Let x ∈ K x\in K be a separating element, so that K / k ⁡ ( x) K/k(x) is a finite separable extension, and let K p K^{p} denote the subfield of p p th powers. Then ( 1, x, …, x p − 1) (1,x,\ldots,x^{p-1}) is a basis for K K as a K p K^{p} -vector space, and every z ∈ K z\in K has a unique representation of the form

 | z = z 0 p + z 1 p ​ x + ⋯ + z p − 1 p ​ x p − 1, z=z_{0}^{p}+z_{1}^{p}x+\cdots+z_{p-1}^{p}x^{p-1}, |  |

with z 0, …, z p − 1 ∈ K z_{0},\ldots,z_{p-1}\in K, and every rational differential form ! = z ​ d ​ x \omega=zdx can be uniquely written in the form

 | ! = ( z 0 p + z 1 p x + ⋯ z p − 1 p x p − 1) d x. \omega=(z_{0}^{p}+z_{1}^{p}x+\cdots z_{p-1}^{p}x^{p-1})dx. |  |

The (modified) *Cartier operator*𝒞: K → K \mathcal{C}\colon{}_{K}\to{}_{K} is then defined by

 | 𝒞 ⁡ (!) ≔ z p − 1 ​ d ​ x. \mathcal{C}(\omega)\coloneqq z_{p-1}dx. |  |

The Cartier operator is uniquely characterized by the following properties:

1. (1)

𝒞 ⁡ (! 1 +! 2) = 𝒞 ⁡ (! 1) + 𝒞 ⁡ (! 2) \mathcal{C}(\omega_{1}+\omega_{2})=\mathcal{C}(\omega_{1})+\mathcal{C}(\omega_{2}) for all ! 1,! 2 ∈ K \omega_{1},\omega_{2}\in{}_{K};

2. (2)

𝒞 ⁡ ( z p ​!) = z ​ 𝒞 ​ (!) \mathcal{C}(z^{p}\omega)=z\,\mathcal{C}(\omega) for all z ∈ K z\in K and ! ∈ K \omega\in{}_{K};

3. (3)

𝒞 ⁡ ( d ​ z) = 0 \mathcal{C}(dz)=0 for all z ∈ K z\in K;

4. (4)

𝒞 ⁡ ( d ​ z / z) = d ​ z / z \mathcal{C}(dz/z)=dz/z for all z ∈ K × z\in K^{\times}.

In particular, it does not depend on our choice of a separating element x x. Moreover, it maps regular differentials to regular differentials and thus restricts to an operator on the space ( 0) K ≔ {! ∈: K! = 0 or div (!) ≥ 0 } {}_{K}(0)\coloneqq\{\omega\in{}_{K}:\omega=0\text{ or }\operatorname{div}(\omega)\geq 0\}, which we recall is a k k -vector space whose dimension g g is equal to (and often used as the definition of) the genus of K K; see [26, Ex. 4.12-17] for these and other standard facts about the Cartier operator.

###### Definition 4.

Let ! ≔ (! 1, …,! g) {\boldsymbol{\omega}}\coloneqq(\omega_{1},\ldots,\omega_{g}) be a basis for ( 0) K {}_{K}(0) and define a i ​ j ∈ k a_{ij}\in k via

 | 𝒞 ⁡ (! j) = ∑ i = 1 g a i ​ j ​! i. \mathcal{C}(\omega_{j})=\sum_{i=1}^{g}a_{ij}\omega_{i}. |  |

The Cartier–Manin matrix of K K (with respect to ! {\boldsymbol{\omega}}) is the matrix A ≔ [a i ​ j] ∈ k g × g A\coloneqq[a_{ij}]\in k^{g\times g}.

If X / k X/k is a smooth projective curve with function field k ⁡ ( X) = K k(X)=K, we also call A A the Cartier–Manin matrix of X X. This matrix is closely related to the Hasse-Witt matrix B B of X X, which is defined as the matrix of the p p -power Frobenius operator acting on H 1 ​ ( X, 𝒪 X) H^{1}(X,\mathcal{O}_{X}) with respect to some basis. As carefully explained in [1], the matrices A A and B B can be related via Serre duality, and for a suitable choice of basis one finds that B = [a i ​ j p] 𝖳 B=[a_{ij}^{p}]^{\mathsf{T}}. In the case of interest to us k = 𝐅 p k=\mathbf{F}_{p} is a prime field and the Cartier–Manin and Hasse–Witt matrices are simply transposes of eachother, hence have the same rank and characteristic polynomials, but we shall follow the warning/request of [1] and call A A the Cartier–Manin matrix, although one can find examples in the literature where A A is called the Hasse–Witt matrix (see [1] for a list).

We shall apply the method of Stöhr–Voloch [27] to compute the Cartier–Manin matrix of a smooth projective curve X X with function field K = k ⁡ ( X) K=k(X). Let us write K K as k ​ ( x) ​ [y] / ( F) k(x)[y]/(F), where x ∈ X x\in X is a separating element and y y is an integral generator for the finite separable extension K / k ⁡ ( x) K/k(x) with minimal polynomial F ∈ k ​ [x] ​ [y] F\in k[x][y]. We now define the differential operator

 | ∇ ≔ ∂ 2 ​ p − 2 ∂ x p − 1 ​ ∂ y p − 1, \nabla\coloneqq\frac{\partial^{2p-2}}{\partial x^{p-1}\partial y^{p-1}}, |  |

which maps x ( i + 1) ​ p − 1 ​ y ( j + 1) ​ p − 1 x^{(i+1)p-1}y^{(j+1)p-1} to x i ​ p ​ y j ​ p x^{ip}y^{jp} and annihilates monomials not of this form; it thus defines a semilinear map ∇: K → K p \nabla\colon K\to K^{p}. Writing F y F_{y} for ∂ ∂ y ​ F ∈ k ⁡ [x, y] \frac{\partial}{\partial y}F\in k[x,y], for any h ∈ K h\in K we have the identity

(2) |  | 𝒞 ⁡ ( h ​ d ​ x F y) = ( ∇ ( F p − 1 ​ h)) 1 / p ​ d ​ x F y \mathcal{C}\left(h\frac{dx}{F_{y}}\right)=\left(\nabla(F^{p-1}h)\right)^{1/p}\frac{dx}{F_{y}} |  |

given by [27, Thm. 1.1]. If we choose a basis for ( 0) X {}_{X}(0) using regular differentials of the form h ​ d ​ x / F y hdx/F_{y}, we can compute the action of the Cartier operator on this basis via ( 2). To construct such a basis we shall use differentials of the form

(3) |  | ! k ​ ℓ ≔ x k − 1 y ℓ − 1 d ​ x F y ( k, ℓ ≥ 1, k + ℓ ≤ deg ( F) − 1). \omega_{k\ell}\coloneqq x^{k-1}y^{\ell-1}\frac{dx}{F_{y}}\qquad(k,\ell\geq 1,\ \ k+\ell\leq\deg(F)-1). |  |

Writing F ​ ( x, y) p − 1 = ∑ i, j F i ​ j p − 1 ​ x i ​ y j F(x,y)^{p-1}=\sum_{i,j}F^{p-1}_{ij}x^{i}y^{j} (defining F i, j p − 1 ∈ k F^{p-1}_{i,j}\in k for all i, j ∈ 𝐙 i,j\in\mathbf{Z}), for k, ℓ ≥ 1 k,\ell\geq 1 one finds that

(4) |  | ∇ ( ∑ i, j ≥ 0 F i ​ j p − 1 ​ x i + k − 1 ​ y j + ℓ − 1) = ∑ i, j ≥ 1 F i ​ p − k, j ​ p − ℓ p − 1 ​ x ( i − 1) ​ p ​ y ( j − 1) ​ p. \nabla\left(\sum_{i,j\geq 0}F^{p-1}_{ij}x^{i+k-1}y^{j+\ell-1}\right)=\sum_{i,j\geq 1}F^{p-1}_{ip-k,\,jp-\ell}x^{(i-1)p}y^{(j-1)p}. |  |

Now F i ​ p − k, j ​ p − ℓ p − 1 F^{p-1}_{ip-k,\,jp-\ell} is nonzero only if we have ( i + j) ​ p − ( k + ℓ) ≤ ( p − 1) ​ deg ⁡ ( F) (i+j)p-(k+\ell)\leq(p-1)\deg(F), and k + ℓ ≤ deg ⁡ ( F) − 1 k+\ell\leq\deg(F)-1, so we can restrict the sum on the RHS to i + j ≤ deg ⁡ ( F) − 1 i+j\leq\deg(F)-1. From ( 2) and ( 4) we obtain

(5) |  | 𝒞 ⁡ (! k ​ ℓ) = ∑ i, j ≥ 1 ( F i ​ p − k, j ​ p − ℓ p − 1) 1 / p ​! i ​ j. \mathcal{C}(\omega_{k\ell})=\sum_{i,j\geq 1}\left(F_{ip-k,\,jp-\ell}^{p-1}\right)^{1/p}\omega_{ij}. |  |

When X X is a smooth plane curve the complete set of ! i ​ j \omega_{ij} defined in ( 3) is a basis for ( 0) K {}_{K}(0) and we can read off the entries of the Cartier–Manin matrix for X X directly from ( 5). In general not all of the ! i ​ j \omega_{ij} necessarily lie in ( 0) K {}_{K}(0), some of them might not be regular, but the subset that do (those corresponding to adjoint polynomials) form a basis for ( 0) K {}_{K}(0); see [16, 27]. In the case of superelliptic curves this subset is given explicitly by Lemma 6 below.

###### Definition 5.

For a, b ∈ 𝐙 a,b\in\mathbf{Z} with b > 0 b>0 let a ​ rem ⁡ b ≔ a − b ⁡ ⌊ a / b ⌋ a\operatorname{rem}b\coloneqq a-b\lfloor a/b\rfloor denote the unique integer in [0, b − 1] ∩ ( a + b ​ 𝐙) [0,b-1]\cap(a+b\mathbf{Z}).

###### Lemma 6.

Let k k be a perfect field of positive characteristic p p, let X / k X/k be a superelliptic curve defined by F ⁡ ( x, y) ≔ y m − f ⁡ ( x) = 0 F(x,y)\coloneqq y^{m}-f(x)=0, let d ≔ deg ⁡ f d\coloneqq\deg f, and for i, j ≥ 1 i,j\geq 1 let ! i ​ j ≔ x i − 1 y j − 1 d x / F y ∈ K \omega_{ij}\coloneqq x^{i-1}y^{j-1}dx/F_{y}\in{}_{K}, where K ≔ k ​ ( x) ​ [y] / ( F) K\coloneqq k(x)[y]/(F) is the function field of X X. Then the set

 | ! ≔ {! i ​ j: m ​ i + d ​ j < m ​ d }, {\boldsymbol{\omega}}\coloneqq\{\omega_{ij}\colon mi+dj<md\}, |  |

is a k k -basis for ( 0) K {}_{K}(0), with 1 ≤ i < d − ⌊ d / m ⌋ 1\leq i<d-\lfloor d/m\rfloor and 1 ≤ j < m − ⌊ m / d ⌋ 1\leq j<m-\lfloor m/d\rfloor. Moreover, if we define

(6) |  | d j ≔ d − ⌊ d ​ j / m ⌋ − 1 and m i ≔ m − ⌊ m ​ i / d ⌋ − 1, d_{j}\coloneqq d-\lfloor dj/m\rfloor-1\qquad\text{and}\qquad m_{i}\coloneqq m-\lfloor mi/d\rfloor-1, |  |

then the ! i ​ j ∈! \omega_{ij}\in{\boldsymbol{\omega}} are precisely those for which 1 ≤ i ≤ d j 1\leq i\leq d_{j} and 1 ≤ j ≤ m i 1\leq j\leq m_{i}.

###### Proof.

Note that ! i ​ j = 1 m ​ x i − 1 ​ y j − m ​ d ​ x \omega_{ij}=\frac{1}{m}x^{i-1}y^{j-m}dx, with p - m p\nmid m. It follows from [23, 3.8] (which treats X / 𝐂 X/\mathbf{C} but whose proof also works for X / k X/k and can be independently derived using the methods of [16]) that the set

 | { x i − 1 y − k d x: 1 ≤ i < d, 1 ≤ k ≤ m − 1, d k − m i ≥ gcd ( m, d) } \{x^{i-1}y^{-k}dx:1\leq i<d,\ 1\leq k\leq m-1,\ dk-mi\geq\gcd(m,d)\} |  |

is a basis for ( 0) K {}_{K}(0). Taking k = m − j k=m-j and rearranging yields the basis

 | ! = {! i ​ j: m ​ i + d ​ j ≤ m ​ d − gcd ⁡ ( m, d) } = {! i ​ j: m ​ i + d ​ j < m ​ d }, {\boldsymbol{\omega}}=\{\omega_{ij}:mi+dj\leq md-\gcd(m,d)\}=\{\omega_{ij}:mi+dj<md\}, |  |

and the bounds on i i and j j immediately follow. ∎

For X / k X/k defined by F ⁡ ( x, y) = f ⁡ ( x) − y m = 0 F(x,y)=f(x)-y^{m}=0, if we let f a n f^{n}_{a} denote the coefficient of x a x^{a} in f ​ ( x) n f(x)^{n} then

 | F a, b p − 1 = { f a p − 1 − b / m, if ​ m | b ​ and ​ b ≤ m ⁡ ( p − 1), 0 otherwise, F^{p-1}_{a,b}=\begin{cases}f^{p-1-b/m}_{a},&\text{if }m\mid b\text{ and }b\leq m(p-1),\\ 0&\text{otherwise},\end{cases} |  |

(here we have used ( p − 1 e) ​ ( − 1) e ≡ 1 mod p \binom{p-1}{e}(-1)^{e}\equiv 1\bmod p), thus for all 1 ≤ i, k < d 1\leq i,k<d and 1 ≤ j, ℓ < m 1\leq j,\ell<m we have

 | F i ​ p − k, j ​ p − ℓ p − 1 = { f i ​ p − k p − 1 − ( j ​ p − ℓ) / m if ​ m | ( j ​ p − ℓ), 0 otherwise. F^{p-1}_{ip-k,\,jp-\ell}=\begin{cases}f^{p-1-(jp-\ell)/m}_{ip-k}&\text{if }m\mid(jp-\ell),\\ 0&\text{otherwise}.\end{cases} |  |

Now 1 ≤ j, ℓ < m 1\leq j,\ell<m and p - m p\nmid m, so whenever F i ​ p − k, j ​ p − ℓ p − 1 ≠ 0 F^{p-1}_{ip-k,\,jp-\ell}\neq 0 we must have ℓ = j ​ p ​ rem ⁡ m > 0 \ell=jp\operatorname{rem}m>0 and

(7) |  | n j ≔ p − 1 − ( j ​ p − ℓ) / m = ( m − j) ​ p − ( m − ℓ) m = p − 1 − ⌊ j ​ p / m ⌋. n_{j}\coloneqq p-1-(jp-\ell)/m=\frac{(m-j)p-(m-\ell)}{m}=p-1-\lfloor jp/m\rfloor. |  |

Let us order the basis for ( 0) K {}_{K}(0) given by Lemma 6 as ! = (! 11,! 21, …,! 12, …) {\boldsymbol{\omega}}=(\omega_{11},\omega_{21},\ldots,\omega_{12},\ldots) with the ! i ​ j \omega_{ij} ordered first by j j and then by i i. The Cartier–Manin matrix of X X can then be described in block form with blocks indexed by j j and ℓ \ell containing entries indexed by i i and k k:

(8) |  | A p \displaystyle A_{p} | ≔ [B j ​ ℓ] j ​ ℓ 1 ≤ j, ℓ ≤ � ≔ m 1 = m − ⌊ m / d ⌋ − 1, \displaystyle\coloneqq[B^{j\ell}]_{j\ell}\qquad\qquad\qquad\,1\leq j,\ell\leq\mu\coloneqq m_{1}=m-\lfloor m/d\rfloor-1, |  |

 | B j ​ ℓ \displaystyle B^{j\ell} | ≔ [( b i ​ k j ​ ℓ) 1 / p] i ​ k 1 ≤ i ≤ d j ​ and ​ 1 ≤ k ≤ d ℓ, \displaystyle\coloneqq[(b^{j\ell}_{ik})^{1/p}]_{ik}\,\qquad\qquad 1\leq i\leq d_{j}\text{ and }1\leq k\leq d_{\ell}, |  |

 | b i ​ k j ​ ℓ \displaystyle b^{j\ell}_{ik} | ≔ { f i ​ p − k n j if ( j ​ p − ℓ) / m ∈ 𝐙 ≥ 0, 0 otherwise. \displaystyle\coloneqq\begin{cases}f^{n_{j}}_{ip-k}&\qquad\qquad\quad\ \text{if $(jp-\ell)/m\in\mathbf{Z}_{\geq 0}$},\\ 0&\qquad\qquad\quad\ \text{otherwise}.\end{cases} |  |

The diagonal blocks B j, j B^{j,j} are square but the others typically will not be square, since the bound on i i depends on j j while the bound on k k depends on ℓ \ell. We also note that there is at most one nonzero B j ​ ℓ B^{j\ell} in each row j j, and in each column ℓ \ell of [B j ​ ℓ] j ​ ℓ [B^{j\ell}]_{j\ell}, since any nonzero B j ​ ℓ B^{j\ell} must have ℓ ≡ j ​ p mod m \ell\equiv jp\bmod m (there will be no nonzero B j ​ ℓ B^{j\ell} for j j if no ℓ ≤ � \ell\leq\mu satisfies ℓ ≡ j ​ p mod m \ell\equiv jp\bmod m; this happens, for example, when j = 1 j=1 and d = m = 5 d=m=5 with p ≡ 4 mod 5 p\equiv 4\bmod 5).

###### Example 7.

For m = 5 m=5 and d = 3 d=3 we have g = 4 g=4, and the 4 × 4 4\times 4 matrix A p A_{p} consists of 3 × 3 = 9 3\times 3=9 blocks: one 2 × 2 2\times 2, two 2 × 1 2\times 1, two 1 × 2 1\times 2, and four 1 × 1 1\times 1. For k = 𝐅 p k=\mathbf{F}_{p}, the matrices A p A_{p} for p ≡ 1, 2, 3, 4 mod 5 p\equiv 1,2,3,4\bmod 5 are

 | ( f p − 1 ( 4 ​ p − 4) / 5 f p − 2 ( 4 ​ p − 4) / 5 0 0 f 2 ​ p − 1 ( 4 ​ p − 4) / 5 f 2 ​ p − 2 ( 4 ​ p − 4) / 5 0 0 0 0 f p − 1 ( 3 ​ p − 3) / 5 0 0 0 0 f p − 1 ( 2 ​ p − 2) / 5), ( 0 0 f p − 1 ( 4 ​ p − 3) / 5 0 0 0 f 2 ​ p − 1 ( 4 ​ p − 3) / 5 0 0 0 0 0 f p − 1 ( 2 ​ p − 4) / 5 f p − 2 ( 2 ​ p − 4) / 5 0 0), \begin{pmatrix}f_{p-1}^{(4p-4)/5}&f_{p-2}^{(4p-4)/5}&0&0\\ f_{2p-1}^{(4p-4)/5}&f_{2p-2}^{(4p-4)/5}&0&0\\ 0&0&f_{p-1}^{(3p-3)/5}&0\\ 0&0&0&f_{p-1}^{(2p-2)/5}\end{pmatrix},\ \begin{pmatrix}0&0&f_{p-1}^{(4p-3)/5}&0\\ 0&0&f_{2p-1}^{(4p-3)/5}&0\\ 0&0&0&0\\ f_{p-1}^{(2p-4)/5}&f_{p-2}^{(2p-4)/5}&0&0\end{pmatrix}, |  |

 | ( 0 0 0 f p − 1 ( 4 ​ p − 2) / 5 0 0 0 f 2 ​ p − 1 ( 4 ​ p − 2) / 5 f p − 1 ( 3 ​ p − 4) / 5 f p − 2 ( 3 ​ p − 4) / 5 0 0 0 0 0 0), ( 0 0 0 0 0 0 0 0 0 0 0 f p − 1 ( 3 ​ p − 2) / 5 0 0 f p − 1 ( 2 ​ p − 3) / 5 0). \begin{pmatrix}0&0&0&f_{p-1}^{(4p-2)/5}\\ 0&0&0&f_{2p-1}^{(4p-2)/5}\\ f_{p-1}^{(3p-4)/5}&f_{p-2}^{(3p-4)/5}&0&0\\ 0&0&0&0\end{pmatrix},\ \begin{pmatrix}0&0&0&0\\ 0&0&0&0\\ 0&0&0&f_{p-1}^{(3p-2)/5}\\ 0&0&f_{p-1}^{(2p-3)/5}&0\end{pmatrix}. |  |

For m = 3 m=3 and d = 5 d=5 we also have g = 4 g=4 but now the 4 × 4 4\times 4 matrix A p A_{p} consists of 2 × 2 = 4 2\times 2=4 blocks: one 3 × 3 3\times 3, one 3 × 1 3\times 1, one 1 × 3 1\times 3, and one 1 × 1 1\times 1. For k = 𝐅 p k=\mathbf{F}_{p} the matrices A p A_{p} for p ≡ 1, 2 mod 3 p\equiv 1,2\bmod 3 are

 | ( f p − 1 ( 2 ​ p − 2) / 3 f p − 2 ( 2 ​ p − 2) / 3 f p − 3 ( 2 ​ p − 2) / 3 0 f 2 ​ p − 1 ( 2 ​ p − 2) / 3 f 2 ​ p − 2 ( 2 ​ p − 2) / 3 f 2 ​ p − 3 ( 2 ​ p − 2) / 3 0 f 3 ​ p − 1 ( 2 ​ p − 2) / 3 f 3 ​ p − 2 ( 2 ​ p − 2) / 3 f 3 ​ p − 3 ( 2 ​ p − 2) / 3 0 0 0 0 f p − 1 ( p − 1) / 3), ( 0 0 0 f p − 1 ( 2 ​ p − 1) / 3 0 0 0 f 2 ​ p − 1 ( 2 ​ p − 1) / 3 0 0 0 f 3 ​ p − 1 ( 2 ​ p − 1) / 3 f p − 1 ( p − 2) / 3 f p − 2 ( p − 2) / 3 f p − 3 ( p − 2) / 3 0). \begin{pmatrix}f_{p-1}^{(2p-2)/3}&f_{p-2}^{(2p-2)/3}&f_{p-3}^{(2p-2)/3}&0\\ f_{2p-1}^{(2p-2)/3}&f_{2p-2}^{(2p-2)/3}&f_{2p-3}^{(2p-2)/3}&0\\ f_{3p-1}^{(2p-2)/3}&f_{3p-2}^{(2p-2)/3}&f_{3p-3}^{(2p-2)/3}&0\\ 0&0&0&f_{p-1}^{(p-1)/3}\end{pmatrix},\ \begin{pmatrix}0&0&0&f_{p-1}^{(2p-1)/3}\\ 0&0&0&f_{2p-1}^{(2p-1)/3}\\ 0&0&0&f_{3p-1}^{(2p-1)/3}\\ f_{p-1}^{(p-2)/3}&f_{p-2}^{(p-2)/3}&f_{p-3}^{(p-2)/3}&0\end{pmatrix}. |  |

In both cases tr ⁡ A p = 0 \operatorname{tr}A_{p}=0 for p ≢ 1 mod m p\not\equiv 1\bmod m, but this is not true in general (consider m = 4 m=4 and d = 3 d=3, for example).

The block form of the Cartier–Manin matrix A p A_{p} given by ( 8) implies the following theorem, which plays a key role in our algorithm for computing A p A_{p} and may also be of independent interest.

###### 8.

Let X: y m = f ⁡ ( x) X\colon y^{m}=f(x) be a superelliptic curve over a perfect field of characteristic p > 0 p>0 with d ≔ deg ⁡ ( f) d\coloneqq\deg(f). Let ! {\boldsymbol{\omega}} be the basis of ( 0) k ⁡ ( X) {}_{k(X)}(0) given by Lemma 6, and for 1 ≤ j ≤ m 1 = m − ⌊ m / d ⌋ − 1 1\leq j\leq m_{1}=m-\lfloor m/d\rfloor-1, let ! j ≔ {! i ​ j ′ ∈!: j ′ = j } {\boldsymbol{\omega}}_{j}\coloneqq\{\omega_{ij^{\prime}}\in\boldsymbol{\omega}:j^{\prime}=j\}. For 1 ≤ j ≤ m 1 1\leq j\leq m_{1} the Cartier operator maps the subspace spanned by ! 𝐣 {\boldsymbol{\omega_{j}}} to the subspace spanned by ! ℓ {\boldsymbol{\omega}}_{\ell}, with ℓ ≡ j ​ p mod m \ell\equiv jp\bmod m, and this action is given by the matrix B j ​ ℓ B^{j\ell} defined in ( 8). In particular, when p ≡ 1 mod m p\equiv 1\bmod m the Cartier operator fixes each of the subspaces spanned by ! j {\boldsymbol{\omega}}_{j}.

###### Proof.

This is an immediate consequence of ( 8). ∎

###### Remark 9.

In [6, Lemma 5.1] Bouw gives formulas for the coefficients of the Hasse–Witt matrix of a general cyclic cover Y: y m = f ⁡ ( x) Y\colon y^{m}=f(x) of 𝐏 1 \mathbf{P}^{1} in terms of the (possibly repeated) roots of the polynomial f ∈ k ⁡ [x] f\in k[x], where k k is an algebraically close field of characteristic p p. When f f is squarefree, Bouw’s formulas agree with ( 8), after taking into account the transposition needed to get the Cartier–Manin matrix and a possible change of basis (I’m grateful to Wanlin Li and John Voight for bringing this to my attention). One can compute analogs of the formulas in ( 8) to handle f f that are not squarefree that take into account the multiplicities of its root, but we do not consider this case here. Note that the genus of Y Y and therefore the dimensions of A p A_{p} will be less than that given by ( 1) when f f is not squarefree, so while the formulas may be more involved, the problem is computationally easier.

## 3. Linear recurrences

The results of the previous section imply that to compute the Cartier–Manin matrix A p A_{p} of a superelliptic curve X: y m = f ⁡ ( x) X\colon y^{m}=f(x) over 𝐅 p \mathbf{F}_{p} it suffices to compute certain coefficients of certain powers of f ⁡ ( x) f(x). In this section we derive linear recurrences that allow us to do this efficiently, both when f ∈ 𝐅 p ​ [x] f\in\mathbf{F}_{p}[x] and when f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] and we wish to compute certain coefficients of certain powers of the reduction of f f modulo many primes p p. In this section we generalize [22, §2], which treated the case m = 2 m=2, in which case A p = B A_{p}=B consists of a single block B 11 B^{11} (so j = ℓ = 1 j=\ell=1), the powers f n f^{n} that appear in the matrix entries are always the same ( n = ( p − 1) / 2 n=(p-1)/2), and every prime p - m p\nmid m is congruent to 1 1 modulo m m. Here we allow all of these parameters to vary.

Let f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] be a squarefree polynomial of degree d ≥ 3 d\geq 3, which we shall write as f ⁡ ( x) = x c ​ h ​ ( x) f(x)=x^{c}h(x) with c = 0, 1 c=0,1 and h ⁡ ( 0) ≠ 0 h(0)\neq 0 (note that x 2 - f x^{2}\nmid f). 2 2 2 The reader may wish to assume c = 0 c=0 and f = h f=h on a first reading. Let h ⁡ ( x) = ∑ i = 0 r h i ​ x i h(x)=\sum_{i=0}^{r}h_{i}x^{i}, and for n ≥ 1 n\geq 1 let h i n h^{n}_{i} denote the coefficient of x i x^{i} in h ​ ( x) n h(x)^{n}. As shown in [22, §2], the identities h n + 1 = h ⋅ h n h^{n+1}=h\cdot h^{n} and ( h n + 1) ′ = ( n + 1) ​ h n (h^{n+1})^{\prime}=(n+1)h^{n} yield the linear relation

(9) |  | ∑ i = 0 r ( ( n + 1) ​ i − k) ​ h i ​ h k − i n = 0, \sum_{i=0}^{r}((n+1)i-k)h_{i}h^{n}_{k-i}=0, |  |

which is valid for all k ∈ 𝐙 k\in\mathbf{Z} and n ∈ 𝐙 ≥ 0 n\in\mathbf{Z}_{\geq 0}. Observing that n j = ( ( m − j) ​ p − ( m − ℓ)) / m n_{j}=((m-j)p-(m-\ell))/m is the exponent on f f in every entry of the nonzero block B j ​ ℓ B^{j\ell} defined in ( 8), let us set n = n j n=n_{j} and rewrite ( 9) as

(10) |  | OPEN 0 = ∑ i = 0 r ( ( m − j) ​ p + ℓ) ​ i − m ​ k) ​ h i ​ h k − i n j ≡ ∑ i = 0 r ( ℓ ​ i − m ​ k) ​ h i ​ h k − i n j mod p, 0=\sum_{i=0}^{r}((m-j)p+\ell)i-mk)h_{i}h^{n_{j}}_{k-i}\equiv\sum_{i=0}^{r}(\ell i-mk)h_{i}h^{n_{j}}_{k-i}\bmod p, |  |

which is valid for all k ∈ 𝐙 k\in\mathbf{Z}. We now define

 | v k n j:= [h k − r + 1 n j, …, h k n j] ∈ 𝐙 r, v^{n_{j}}_{k}:=[h^{n_{j}}_{k-r+1},\ldots,h^{n_{j}}_{k}]\in\mathbf{Z}^{r}, |  |

and put s ≔ p − 1 − c ​ n j s\coloneqq p-1-cn_{j}. The entries of v s n mod p v^{n}_{s}\bmod p suffice to compute the first row of block B j ​ ℓ B^{j\ell} in A p A_{p}; note that n n (and potentially s s) depend on j j and will vary from block to block. We have v 0 n j = [0, …, 0, h 0 n j] = h 0 n j ​ v 0 0 v^{n_{j}}_{0}=[0,\ldots,0,h_{0}^{n_{j}}]=h_{0}^{n_{j}}v_{0}^{0}, where v 0 0 ≔ [0, …, 0, 1] v_{0}^{0}\coloneqq[0,\ldots,0,1]. Noting that s < p s<p and p - m p\nmid m and p - h 0 p\nmid h_{0} (since f f is squarefree), solving for h k n h_{k}^{n} in ( 10) yields

(11) |  | v s n j ≡ v 0 n j ( m ​ h 0) s ​ s! ​ ∏ i = 0 s − 1 M i ℓ ≡ m c ​ n j ​ h 0 ( c + 1) ​ n j ​ ( − 1) c ​ n j + 1 ​ ( c ​ n j)! ​ v 0 0 ​ ∏ i = 0 s − 1 M i ℓ mod p, v^{n_{j}}_{s}\equiv\frac{v^{n_{j}}_{0}}{(mh_{0})^{s}s!}\prod_{i=0}^{s-1}M^{\ell}_{i}\equiv m^{cn_{j}}h_{0}^{(c+1)n_{j}}(-1)^{cn_{j}+1}(cn_{j})!v^{0}_{0}\prod_{i=0}^{s-1}M^{\ell}_{i}\bmod p, |  |

where

(12) |  | M i − 1 ℓ:= [0 ⋯ 0 ( ℓ ​ r − m ​ i) ​ h r m ​ i ​ h 0 ⋯ 0 ( ℓ ⁡ ( r − 1) − m ​ i) ​ h r − 1 ⋱ 0 ⋯ m ​ i ​ h 0 ( ℓ − m ​ i) ​ h 1] M^{\ell}_{i-1}:=\begin{bmatrix}0&\cdots&0&(\ell r-mi)h_{r}\\ mih_{0}&\cdots&0&(\ell(r-1)-mi)h_{r-1}\\ \vdots&\ddots&\vdots&\vdots\\ 0&\cdots&mih_{0}&(\ell-mi)h_{1}\end{bmatrix} |  |

is an integer matrix that depends on the integers i, ℓ, m i,\ell,m and the polynomial h h of degree r r, but is independent of p p. This independence is the key to obtaining an average polynomial-time algorithm.

###### Remark 10.

Alternatively, if we define w k n ≔ [h k + r − 1 n j, h k + r − 2 n j, …, h k n j] w_{k}^{n}\coloneqq[h_{k+r-1}^{n_{j}},h_{k+r-2}^{n_{j}},\ldots,h_{k}^{n_{j}}] and t ≔ d j ​ p − d ℓ − c ​ n j t\coloneqq d_{j}p-d_{\ell}-cn_{j}, the entries of w t n w_{t}^{n} suffice to compute the last row of block B j ​ ℓ B^{j\ell} in A p A_{p}. Equivalently, if we put h ~ ​ ( x) ≔ x r ​ h ​ ( 1 / x) \tilde{h}(x)\coloneqq x^{r}h(1/x) (in other words, reverse the coefficients of h h) and define v ~ k n \tilde{v}_{k}^{n} in terms of h ~ n \tilde{h}^{n} as above, it suffices to compute v ~ s ~ n \tilde{v}_{\tilde{s}}^{n} where

(13) |  | s ~ ≔ r ​ n j − t \displaystyle\tilde{s}\coloneqq rn_{j}-t | = d ​ n j − d j ​ p + d ℓ = p − 1 − ⌊ ( d ​ j ​ rem ⁡ m) ​ p / m ⌋ \displaystyle=dn_{j}-d_{j}p+d_{\ell}=p-1-\lfloor(dj\operatorname{rem}m)p/m\rfloor |  |

When m - d ​ j m\nmid dj we will have s ~ < s \tilde{s}<s if c = 0 c=0 (and possibly even if c = 1 c=1), in which case we can compute the last row more efficiently than the first.

We have shown how to compute the first (or last) row of each of the blocks B j ​ ℓ B^{j\ell} that appear in the Cartier–Manin matrix of the superelliptic curve X X (either for X / 𝐅 p X/\mathbf{F}_{p} or for the reductions of X / 𝐐 X/\mathbf{Q} modulo varying primes p p) by computing reductions of products of integer matrices modulo primes. To compute the remaining rows in the same fashion would require working modulo powers of primes, which is something we wish to avoid. In the next section we show how to efficiently reduce the computation of the remaining rows to the computation of the first row using translated curves, which allows us to always work modulo primes.

## 4. Translation tricks

Let X: y m = f ⁡ ( x) X\colon y^{m}=f(x) be a superelliptic curve over 𝐅 p \mathbf{F}_{p} of genus g g, with d ≔ deg ⁡ ( f) d\coloneqq\deg(f). Let A p A_{p} be the Cartier–Manin matrix A p A_{p}, and for a ∈ 𝐅 p a\in\mathbf{F}_{p}, let A p ​ ( a) A_{p}(a) be the Cartier–Manin matrix of the translated curve X a: y m = f ⁡ ( x + a) X_{a}\colon y^{m}=f(x+a), whose blocks we denote B j ​ ℓ ​ ( a) B^{j\ell}(a) with entries b i ​ k j ​ ℓ ​ ( a) b^{j\ell}_{ik}(a). We omit the exponent 1 / p 1/p that appears in ( 8) because we are now working over 𝐅 p \mathbf{F}_{p}. The curve X a X_{a} is isomorphic to X X, which forces A p A_{p} and A p ​ ( a) A_{p}(a) to be conjugate, but these matrices are typically not equal. Our objective in this section is to show that we can compute B j ​ ℓ B^{j\ell} by solving a linear system that involves the entries that appear in just the first rows of B j ​ ℓ ​ ( a) B^{j\ell}(a), where a a ranges over d j = d − ⌊ d ​ j / m ⌋ − 1 d_{j}=d-\lfloor dj/m\rfloor-1 distinct values of a ∈ 𝐅 p a\in\mathbf{F}_{p}. Note that B j ​ ℓ B^{j\ell} has d j d_{j} rows and d ℓ d_{\ell} columns, and we recall from ( 8) that the g × g g\times g matrix A p A_{p} is made up of � 2 \mu^{2} blocks B j ​ ℓ B^{j\ell}, where � ≔ m 1 = m − ⌊ m / d ⌋ − 1 \mu\coloneqq m_{1}=m-\lfloor m/d\rfloor-1, and we have d 1 + ⋯ + d � = g d_{1}+\cdots+d_{\mu}=g. We shall assume p ≥ d p\geq d, so that d j < d d_{j}<d distinct values of a a exist in 𝐅 p \mathbf{F}_{p}; for p < d p<d we can easily compute A p A_{p} directly from ( 8).

The results in this section generalize [22, §5], which treated the case m = 2 m=2, where � = 1 \mu=1 and A = B 11 A=B^{11}. In our current setting A p A_{p} consists of � × � \mu\times\mu rectangular blocks B j ​ ℓ B^{j\ell} that need not be square.

For a ∈ 𝐅 p a\in\mathbf{F}_{p} and 1 ≤ j ≤ � 1\leq j\leq\mu we define the upper triangular d j × d j d_{j}\times d_{j} matrix

 | T j ​ ( a) ≔ [t i ​ k j ​ ( a)] i ​ k, t i ​ k j ​ ( a) ≔ ( k − 1 i − 1) ​ a k − i, 1 ≤ i, k ≤ d j. T^{j}(a)\coloneqq[t_{ik}^{j}(a)]_{ik},\qquad t^{j}_{ik}(a)\coloneqq\binom{k-1}{i-1}a^{k-i},\qquad 1\leq i,k\leq d_{j}. |  |

We also define T ⁡ ( a) T(a) to be the g × g g\times g block diagonal matrix with the matrices T j ​ ( a) T^{j}(a) on the diagonal, for 1 ≤ j ≤ � 1\leq j\leq\mu. We note that T j ​ ( a) − 1 = T j ​ ( − a) T^{j}(a)^{-1}=T^{j}(-a) and T ​ ( a) − 1 = T ⁡ ( − a) T(a)^{-1}=T(-a), as the reader may verify (or see the proof below).

###### Lemma 11.

For a ∈ 𝐅 p a\in\mathbf{F}_{p} we have B j ​ ℓ ​ ( a) ​ T ℓ ​ ( a) = T j ​ ( a) ​ B j ​ ℓ B^{j\ell}(a)T^{\ell}(a)=T^{j}(a)B^{j\ell} for all 1 ≤ j, ℓ ≤ � 1\leq j,\ell\leq\mu, and A p ​ ( a) = T ⁡ ( a) ​ A p ​ T ​ ( − a) A_{p}(a)=T(a)A_{p}T(-a).

###### Proof.

From the block structure of A p A_{p} given by ( 8) it is clear that the first statement implies the second. Let ! ​ ( a) = {! i ​ j ​ ( a) } {\boldsymbol{\omega}}(a)=\{\omega_{ij}(a)\} be the basis given by Lemma 6 for X a X_{a} and define ! j ​ ( a) ≔ {! i ​ j ′ ​ ( a) ∈!: j ′ = j } {\boldsymbol{\omega}}_{j}(a)\coloneqq\{\omega_{ij^{\prime}}(a)\in{\boldsymbol{\omega}}:j^{\prime}=j\}. By Theorem 8, the Cartier operator of X X maps the subspace spanned by ! j {\boldsymbol{\omega}}_{j} to the subspace spanned by ! ℓ {\boldsymbol{\omega}}_{\ell} via the matrix B j ​ ℓ B^{j\ell}, and the Cartier operator of X a X_{a} maps the subspace spanned by ! j ​ ( a) {\boldsymbol{\omega}}_{j}(a) to the subspace spanned by ! ℓ ​ ( a) {\boldsymbol{\omega}}_{\ell}(a) via the matrix B j ​ ℓ ​ ( a) B^{j\ell}(a). We just need to check that the matrices T ℓ ​ ( a) T^{\ell}(a) and T j ​ ( a) T^{j}(a) correspond to the change of basis that occurs when we replace x x with x + a x+a. Noting that d ⁡ ( x + a) = d ​ x d(x+a)=dx and F ​ ( x + a) y = F ​ ( x) y F(x+a)_{y}=F(x)_{y}, we have

 | ! k ​ j ​ ( a) = ( x + a) k − 1 ​ y j − 1 ​ d ​ x / F y \displaystyle\omega_{kj}(a)=(x+a)^{k-1}y^{j-1}dx/F_{y} | = ∑ i = 1 k ( k − 1 i − 1) ​ a k − i ​ x i − 1 ​ y j − 1 ​ d ​ x / F y \displaystyle=\sum_{i=1}^{k}\binom{k-1}{i-1}a^{k-i}x^{i-1}y^{j-1}dx/F_{y} |  |

 |  | = ∑ i = 1 k t i ​ k j ​ ( a) ​! i ​ j = ∑ i = 1 d j t i ​ k j ​ ( a) ​! i ​ j, \displaystyle=\sum_{i=1}^{k}t^{j}_{ik}(a)\omega_{ij}=\sum_{i=1}^{d_{j}}t^{j}_{ik}(a)\omega_{ij}, |  |

and it follows that ! j ​ ( a) = T j ​ ( a) ​! j {\boldsymbol{\omega}}_{j}(a)=T^{j}(a){\boldsymbol{\omega}}_{j} (here we are viewing ! j {\boldsymbol{\omega}}_{j} and ! j ​ ( a) {\boldsymbol{\omega}}_{j}(a) as column vectors). This holds for any j j, including ℓ \ell, and the lemma follows. ∎

Let us now consider the computation of the d j × d ℓ d_{j}\times d_{\ell} block B j ​ ℓ B^{j\ell}. Computing the k k th entry in the first row of both sides of the identity B j ​ ℓ ​ ( a) ​ T ℓ ​ ( a) = T j ​ ( a) ​ B j ​ ℓ B^{j\ell}(a)T^{\ell}(a)=T^{j}(a)B^{j\ell} given by Lemma 11 yields

 | ∑ s = 1 d ℓ b 1 ​ s j ​ ℓ ​ ( a) ​ t s ​ k ℓ ​ ( a) = ∑ t = 1 d j t 1 ​ t j ​ ( a) ​ b t ​ k j ​ ℓ, \sum_{s=1}^{d_{\ell}}b_{1s}^{j\ell}(a)t_{sk}^{\ell}(a)=\sum_{t=1}^{d_{j}}t^{j}_{1t}(a)b^{j\ell}_{tk}, |  |

which defines a linear equation with d j d_{j} unknowns b t ​ k j ​ ℓ b^{j\ell}_{tk} in terms of the b 1 ​ s j ​ ℓ ​ ( a) b_{1s}^{j\ell}(a) and matrices T j ​ ( a) T^{j}(a) and T ℓ ​ ( a) T^{\ell}(a) we assume are known. Taking d j d_{j} distinct values of a a, say ( a 1, …, a d j) (a_{1},\ldots,a_{d_{j}}) yields a linear system with d j d_{j} equations and d j d_{j} unknowns that we can solve because the d j × d j d_{j}\times d_{j} matrix [t 1 ​ t j ​ ( a i)] i ​ t = [a i t − 1] i ​ t [t^{j}_{1t}(a_{i})]_{it}=[a_{i}^{t-1}]_{it} is an invertible Vandermonde matrix V ⁡ ( a 1, …, a d j) V(a_{1},\ldots,a_{d_{j}}). If we now define the d j × d ℓ d_{j}\times d_{\ell} matrix

(14) |  | B 1 j ​ ℓ ​ ( a 1, …, a d j) ≔ [b 1 ​ s j ​ ℓ ​ ( a i)] i ​ s B^{j\ell}_{1}(a_{1},\ldots,a_{d_{j}})\coloneqq[b_{1s}^{j\ell}(a_{i})]_{is} |  |

and let W 1 j ​ ℓ W_{1}^{j\ell} be the d j × d ℓ d_{j}\times d_{\ell} matrix whose i i th row is the i i th row of B 1 j ​ ℓ B_{1}^{j\ell} times T ℓ ​ ( a i) T^{\ell}(a_{i}), we can compute B j ​ ℓ B^{j\ell} as

(15) |  | B j ​ ℓ = V ​ ( a 1, …, a d j) − 1 ​ W 1 j ​ ℓ. B^{j\ell}=V(a_{1},\ldots,a_{d_{j}})^{-1}W_{1}^{j\ell}. |  |

###### Remark 12.

If we use Remark 10 to compute the last row of B j ​ ℓ B^{j\ell} we can compute the first row of B j ​ ℓ ​ ( a i) B^{j\ell}(a_{i}) for a 1, …, a d j − 1 a_{1},\ldots,a_{d_{j}-1} and use ( 15) to deduce the last row of W 1 j ​ ℓ W_{1}^{j\ell} from the last row of B j ​ ℓ B^{j\ell}. One might suppose that we could instead compute the last rows of the B j ​ ℓ ​ ( a i) B^{j\ell}(a_{i}) instead of their first rows, but this is not enough to deduce B j ​ ℓ B^{j\ell}.

###### Lemma 13.

Let X: y m = f ⁡ ( x) X\colon y^{m}=f(x) be a superelliptic curve over 𝐅 p \mathbf{F}_{p} with d ≔ deg ⁡ ( f) d\coloneqq\deg(f), and let a 1, …, a d 1 a_{1},\ldots,a_{d_{1}} be distinct elements of 𝐅 p \mathbf{F}_{p}, where d 1 = d − ⌊ d / m ⌋ − 1 d_{1}=d-\lfloor d/m\rfloor-1. Given the matrices B 1 j ​ ℓ ​ ( a 1, …, a d j) B_{1}^{j\ell}(a_{1},\ldots,a_{d_{j}}) for 1 ≤ j ≤ � = m 1 = m − ⌊ m / d ⌋ − 1 1\leq j\leq\mu=m_{1}=m-\lfloor m/d\rfloor-1 with ℓ ≡ j ​ p mod m \ell\equiv jp\bmod m, we can compute the Cartier–Manin matrix A p A_{p} of X X using O ⁡ ( m ​ d 3) O(md^{3}) ring operations in 𝐅 p \mathbf{F}_{p} and space for O ⁡ ( m ​ d + d 2) O(md+d^{2}) elements of 𝐅 p \mathbf{F}_{p}.

###### Proof.

We can compute V ​ ( a 1, …, a d j) − 1 V(a_{1},\ldots,a_{d_{j}})^{-1} using O ⁡ ( d j 2) O(d_{j}^{2}) ring operations in 𝐅 p \mathbf{F}_{p} [11], and we can compute T ℓ ​ ( a i) T^{\ell}(a_{i}) in O ⁡ ( d j 2) O(d_{j}^{2}) ring operations (using ( k i) = ( k − 1 i − 1) + ( k − 1 i) \binom{k}{i}=\binom{k-1}{i-1}+\binom{k-1}{i}). The computation of W j ​ ℓ W^{j\ell} requires O ⁡ ( d j ​ d ℓ 2) O(d_{j}d_{\ell}^{2}) 𝐅 p \mathbf{F}_{p} -operations, and the matrix product in ( 14) uses O ⁡ ( d j 2 ​ d l) O(d_{j}^{2}d_{l}) ring operations, so it takes O ⁡ ( d j 2 ​ d ℓ + d ℓ ​ d j 2) = O ⁡ ( d 3) O(d_{j}^{2}d_{\ell}+d_{\ell}d_{j}^{2})=O(d^{3}) ring operations to compute each B j ​ ℓ B^{j\ell}. There are at most � < m \mu<m nonzero B j ​ ℓ B^{j\ell} to compute, so the total cost of computing A p A_{p} given the matrices B 1 j ​ ℓ ​ ( a 1, …, a d j) B_{1}^{j\ell}(a_{1},\ldots,a_{d_{j}}) is O ⁡ ( m ​ d 3) O(md^{3}) ring operations in 𝐅 p \mathbf{F}_{p} while storing O ⁡ ( m ​ d + d 2) O(md+d^{2}) elements of 𝐅 p \mathbf{F}_{p}. ∎

###### Remark 14.

In terms of the genus g ∼ m ​ d / 2 g\sim md/2, the bound O ⁡ ( m ​ d 3) O(md^{3}) is equivalent to O ⁡ ( g ​ d 2) O(gd^{2}), which is always bounded by O ⁡ ( g 3) O(g^{3}) but can be as small as O ⁡ ( g) O(g) if d = O ⁡ ( 1) d=O(1) (this assumes we use a sparse representation of A p A_{p}).

###### Remark 15.

In addition to playing a key role in our strategy for computing A p A_{p}, using translated curves can improve performance, as noted in the case of hyperelliptic curves in [22, §6.1]. In particular, if f ⁡ ( x) f(x) has a rational root a a then the translated curve X a: y m = f ⁡ ( x + a) = x ​ h ​ ( x) X_{a}\colon y^{m}=f(x+a)=xh(x) will have r = d − 1 r=d-1 and c = d − r = 1 c=d-r=1, reducing both the dimension r r and number t = p − 1 − c ​ n t=p-1-cn of matrices M k ℓ M^{\ell}_{k} that appear in the product in ( 11). It thus makes sense to choose our distinct translation points a a to be roots of f ⁡ ( x) f(x) whenever possible. Additionally, if d d is divisible by m m and f ⁡ ( x) f(x) has a rational root a a, we can replace X X with X ′: y m = x d ​ f ​ ( 1 / x + a) = g ⁡ ( x) X^{\prime}\colon y^{m}=x^{d}f(1/x+a)=g(x), where g ⁡ ( x) g(x) has degree d − 1 d-1, and this also applies to all translated curves X a ′ ′ X^{\prime}_{a^{\prime}}. This applies both locally (over 𝐅 p \mathbf{F}_{p}) and globally (over 𝐐 \mathbf{Q}).

## 5. Accumulating remainder trees and forests

In this section we briefly recall some background on accumulating remainder trees and related complexity bounds. Given a sequence of r × r r\times r matrices M 0, …, M N − 1 M_{0},\ldots,M_{N-1} and a sequence of coprime integers m 0, …, m N − 1 m_{0},\ldots,m_{N-1} we wish to compute the sequence of reduced partial products

 | A k ≔ M 0 ⋯ M k mod m k A_{k}\coloneqq M_{0}\cdots M_{k}\bmod m_{k} |  |

for 0 ≤ k < N 0\leq k<N. Let M − 1 ≔ M N ≔ m N ≔ 1 M_{-1}\coloneqq M_{N}\coloneqq m_{N}\coloneqq 1, and for 0 ≤ k < N / 2 0\leq k<N/2 let B k ≔ M 2 ​ k − 1 ​ M 2 ​ k B_{k}\coloneqq M_{2k-1}M_{2k} and b k ≔ m 2 ​ k ​ m 2 ​ k + 1 b_{k}\coloneqq m_{2k}m_{2k+1}. If we recursively compute C k ≔ B 0 ⋯ B k mod b k = M 0 ⋯ M 2 ​ k mod m 2 ​ k m 2 ​ k + 1 C_{k}\coloneqq B_{0}\cdots B_{k}\bmod b_{k}=M_{0}\cdots M_{2k}\bmod m_{2k}m_{2k+1} for 0 ≤ k < N / 2 0\leq k<N/2, we then have

 | A 2 ​ k = C k mod m 2 ​ k and A 2 ​ k + 1 = C k ​ M 2 ​ k + 1 mod m 2 ​ k + 1, A_{2k}=C_{k}\bmod m_{2k}\qquad\text{and}\qquad A_{2k+1}=C_{k}M_{2k+1}\bmod m_{2k+1}, |  |

This is the RemainderTree algorithm given in [21]. In our setting we actually want to compute products of the form V ​ ∏ k M k V\prod_{k}M_{k} that involve a row vector V V, and for this problem the RemainderForest algorithm in [21] achieves an improved time (and especially) space complexity by splitting the remainder tree into 2 � 2^{\kappa} -subtrees, for a suitable choice of � \kappa. We record the following result from [22], in which ‖ x ‖ \|x\| denotes the logarithm of the largest absolute value appearing in nonzero integer matrix or integer vector x x, including the case where x x is a single nonzero integer.

###### 16 [22].

Given V ∈ 𝐙 r V\in\mathbf{Z}^{r}, M 1, …, M N ∈ 𝐙 r × r M_{1},\ldots,M_{N}\in\mathbf{Z}^{r\times r}, and m 1, …, m N ∈ 𝐙 m_{1},\ldots,m_{N}\in\mathbf{Z}, let n ≔ ⌈ log 2 ⁡ N ⌉ n\coloneqq\lceil\log_{2}N\rceil, let B B be an upper bound on ‖ ∏ j = 1 N m j ‖ \|\prod_{j=1}^{N}m_{j}\| such that B / 2 � B/2^{\kappa} is an upper bound on ‖ ∏ j = s ​ t s ​ t + t − 1 m j ‖ \|\prod_{j=st}^{st+t-1}m_{j}\| for 1 ≤ s ≤ N / t 1\leq s\leq N/t, where t:= 2 n − � t:=2^{n-\kappa}. Let B ′ B^{\prime} be an upper bound on ‖ V ‖ \|V\|, and let H H be an upper bound on ‖ m k ‖, ‖ A k ‖ \|m_{k}\|,\|A_{k}\| for 1 ≤ k ≤ N 1\leq k\leq N, such that log ⁡ r ≤ H \log r\leq H, and assume that r = O ⁡ ( log ⁡ N) r=O(\log N). The RemainderForest algorithm computes the vectors V k ≔ V M 1 ⋯ M k mod m k ∈ ( 𝐙 / m k 𝐙) r V_{k}\coloneqq VM_{1}\cdots M_{k}\bmod m_{k}\in(\mathbf{Z}/m_{k}\mathbf{Z})^{r} for 1 ≤ k ≤ N 1\leq k\leq N in

 | O ⁡ ( r 2 ​ 𝖬 ⁡ ( B + NH) ​ ( n − �) + 2 � ​ r 2 ​ 𝖬 ⁡ ( B) + r ​ 𝖬 ⁡ ( B ′)) O(r^{2}\M(B+NH)(n-\kappa)+2^{\kappa}r^{2}\M(B)+r\M(B^{\prime})) |  |

time using space bounded by

 | O ⁡ ( 2 − � ​ r 2 ​ ( B + N ​ H) ​ ( n − �) + r ⁡ ( B + B ′)). O(2^{-\kappa}r^{2}(B+NH)(n-\kappa)+r(B+B^{\prime})). |  |

This theorem implies the following corollary, which is all we shall use.

###### Corollary 17.

Fix an absolute constant c > 0 c>0. Let N N be a positive integer, let m 1, …, m N m_{1},\ldots,m_{N} be a sequence of positive coprime integers with log ⁡ m k ≤ c ​ log ⁡ N \log m_{k}\leq c\log N, let M 0, …, M N − 1 ∈ 𝐙 r × r M_{0},\ldots,M_{N-1}\in\mathbf{Z}^{r\times r} be integer matrices with r, ‖ M k ‖ ≤ c ​ log ⁡ N r,\|M_{k}\|\leq c\log N, and let v 0 ∈ 𝐙 r v_{0}\in\mathbf{Z}^{r} be a row vector with ‖ v 0 ‖ = c ​ N ​ log ⁡ N \|v_{0}\|=cN\log N. We can compute the vectors

 | v k ≔ v 0 ​ ∏ i = 0 k − 1 M i mod m k v_{k}\coloneqq v_{0}\prod_{i=0}^{k-1}M_{i}\bmod m_{k} |  |

for 1 ≤ k ≤ N 1\leq k\leq N in O ⁡ ( r 2 ​ N ​ log 3 ​ N) O(r^{2}N\log^{3}\!N) time using O ⁡ ( r 2 ​ N) O(r^{2}N) space.

###### Proof.

Applying Theorem 16 with � ≔ 2 ​ log ⁡ log ​ N \kappa\coloneqq 2\log\log N, B = c ​ N ​ log ⁡ N B=cN\log N, B ′ = c ​ log ⁡ N B^{\prime}=c\log N, and H = c ​ log ⁡ N H=c\log N, yields an O ⁡ ( r 2 ​ 𝖬 ⁡ ( N ​ log ⁡ N) ​ log ​ N) O(r^{2}\M(N\log N)\log N) time bound using O ⁡ ( r 2 ​ N) O(r^{2}N) space. Now apply 𝖬 ⁡ ( N) = O ⁡ ( N ​ log ⁡ N) \M(N)=O(N\log N) from [18]. ∎

## 6. Algorithms

We now give our algorithms for computing the Cartier–Manin matrix A p A_{p} of a superelliptic curve X / 𝐅 p X/\mathbf{F}_{p} and for the reductions of a superelliptic curve X / 𝐐 X/\mathbf{Q} modulo all good primes p ≤ N p\leq N. In the descriptions below, expressions of the form “ a ​ rem ⁡ m a\operatorname{rem}m ” denote the least nonnegative remainder in Euclidean division of a a by m m. As above we assume X X is defined by y m = f ⁡ ( x) y^{m}=f(x) with f ⁡ ( x) f(x) squarefree of degree d ≥ 3 d\geq 3. We define � ≔ m − ⌊ m / d ⌋ − 1 \mu\coloneqq m-\lfloor m/d\rfloor-1, and for 1 ≤ j ≤ � 1\leq j\leq\mu we put d j ≔ d − ⌊ d ​ j / m ⌋ − 1 d_{j}\coloneqq d-\lfloor dj/m\rfloor-1, with d 1 ≥ d 2 ≥ ⋯ d � d_{1}\geq d_{2}\geq\cdots d_{\mu} as in ( 6). Recall that the genus g g of X X is g ≔ ( ( d − 2) ​ ( m − 1) + m − gcd ⁡ ( m, d)) / 2 g\coloneqq((d-2)(m-1)+m-\gcd(m,d))/2, as in ( 1).

Algorithm ComputeCartierManinMatrix

Given m ≥ 2 m\geq 2 and squarefree f ∈ 𝐅 p ​ [x] f\in\mathbf{F}_{p}[x] of degree 3 ≤ d ≤ p 3\leq d\leq p with p - m p\nmid m, compute the Cartier–Manin matrix A p ∈ 𝐅 p g × g A_{p}\in\mathbf{F}_{p}^{g\times g} of X: y m = f ⁡ ( x) X\colon y^{m}=f(x) as follows:

1. 1.

Fix distinct a 1, …, a d 1 ∈ 𝐅 p a_{1},\ldots,a_{d_{1}}\in\mathbf{F}_{p} that include as many roots of f ⁡ ( x) f(x) as possible.

2. 2.

For j j from 1 1 to � \mu such that ℓ ≔ j ​ p ​ rem ⁡ m ≤ � \ell\coloneqq jp\operatorname{rem}m\leq\mu:

  1. a.

For i i from 1 1 to d j d_{j}:

    1. i.

Let f ⁡ ( x + a i) = x c ​ h ​ ( x) ∈ 𝐅 p ​ [x] f(x+a_{i})=x^{c}h(x)\in\mathbf{F}_{p}[x] with c ∈ { 0, 1 } c\in\{0,1\} and put r ≔ deg ⁡ ( h) r\coloneqq\deg(h).

    2. ii.

Set n ≔ ( ( m − j) ​ p − ( m − ℓ)) / m ∈ 𝐙 n\coloneqq((m-j)p-(m-\ell))/m\in\mathbf{Z} and s ≔ p − 1 − c ​ n s\coloneqq p-1-cn.

    3. iii.

Compute w s ≔ v 0 0 ​ ∏ i = 0 s − 1 M i ℓ ∈ 𝐅 p r w_{s}\coloneqq v_{0}^{0}\prod_{i=0}^{s-1}M_{i}^{\ell}\in\mathbf{F}_{p}^{r}, with M i ℓ ∈ 𝐅 p r × r M_{i}^{\ell}\in\mathbf{F}_{p}^{r\times r} as in ( 12), and u s ≔ s! ∈ 𝐅 p u_{s}\coloneqq s!\in\mathbf{F}_{p}.

    4. iv.

Compute � ≔ v s n = m − s ​ h 0 n − s ​ u s − 1 ​ w s ∈ 𝐅 p r \alpha\coloneqq v_{s}^{n}=m^{-s}h_{0}^{n-s}u_{s}^{-1}w_{s}\in\mathbf{F}_{p}^{r} via ( 11).

    5. v.

Let b 1 j ​ ℓ ​ ( a i) ≔ [� r, � r − 1, … ​ � r − d ℓ + 1] ∈ 𝐅 p d ℓ b_{1}^{j\ell}(a_{i})\coloneqq[\alpha_{r},\alpha_{r-1},\ldots\alpha_{r-d_{\ell}+1}]\in\mathbf{F}_{p}^{d_{\ell}}.

  2. b.

Let B 1 j ​ ℓ ∈ 𝐅 p d j × d ℓ B_{1}^{j\ell}\in\mathbf{F}_{p}^{d_{j}\times d_{\ell}} be the matrix with i i th row b 1 j ​ ℓ ​ ( a i) b_{1}^{j\ell}(a_{i}) as in ( 14) and use B 1 j ​ ℓ B_{1}^{j\ell} to compute B j ​ ℓ ∈ 𝐅 p d j × d ℓ B^{j\ell}\in\mathbf{F}_{p}^{d_{j}\times d_{\ell}} via ( 15).

3. 3.

Output A p ≔ [B j ​ ℓ] j ​ ℓ ∈ 𝐅 p g × g A_{p}\coloneqq[B^{j\ell}]_{j\ell}\in\mathbf{F}_{p}^{g\times g} defined as in ( 8), with B j ​ ℓ ≔ 0 B^{j\ell}\coloneqq 0 for ℓ ≢ j ​ p mod m \ell\not\equiv jp\bmod m.

There are two ways to compute w s w_{s} in step iii. One is to compute s s vector-matrix products w i + 1 ≔ w i ​ M i ℓ w_{i+1}\coloneqq w_{i}M_{i}^{\ell} starting with w 0 ≔ [0, …, 0, 1] ∈ 𝐅 p r w_{0}\coloneqq[0,\ldots,0,1]\in\mathbf{F}_{p}^{r}, which can be accomplished with O ⁡ ( p ​ r) O(pr) ring operations in 𝐅 p \mathbf{F}_{p}, each of which takes time 𝖬 ⁡ ( log ⁡ p) = O ⁡ ( log ⁡ p ​ log ⁡ log ⁡ p) \M(\log p)=O(\log p\log\log p) via [19], yielding a time complexity of O ⁡ ( r ​ p ​ log ⁡ p ​ log ⁡ log ⁡ p) O(rp\log p\log\log p) and a space complexity of O ⁡ ( r ​ log ⁡ p) O(r\log p) (note that M i ℓ M_{i}^{\ell} has only 2 ​ r − 1 2r-1 nonzero entries). Alternatively one can use the Bostan-Gaudry-Schost algorithm [5], which uses an optimized interpolation/evaluation approach to compute products of matrices over polynomial rings evaluated along an arithmetic progression; in our setting we view the M i ℓ M_{i}^{\ell} as matrices of linear polynomials in i i evaluated along the arithmetic progression i = 0, 1, 2, …, s − 1 i=0,1,2,\ldots,s-1. This has a bit complexity of O ⁡ ( r 2 ​ p 1 / 2 ​ log ⁡ p ⁡ ( r! − 2 ​ log ⁡ log ⁡ p + log ⁡ p) CLOSE O(r^{2}p^{1/2}\log p(r^{\omega-2}\log\log p+\log p) using O ⁡ ( r 2 ​ p 1 / 2 ​ log ⁡ p) O(r^{2}p^{1/2}\log p) space via [5, Thm. 8] and [19], and we can similarly compute u s = s! u_{s}=s! (but note that u s = − 1 u_{s}=-1 in the typical case where c = 0 c=0). Note that r r is either d d or d − 1 d-1, so we can replace r r with d d in these bounds. This analysis leads to Theorem 3 given in the introduction, which we restate here for convenience.

See 3

###### Proof.

Excluding step iii, applying Lemma 13 with an O ⁡ ( log ⁡ p ​ log ⁡ log ​ p) O(\log p\log\log p) cost per ring operation in 𝐅 p \mathbf{F}_{p} yields a time complexity of O ⁡ ( m ​ d 3 ​ log ⁡ p ​ log ⁡ log) O(md^{3}\log p\log\log) using O ⁡ ( ( m ​ d + d 2) ​ log ⁡ p) O((md+d^{2})\log p) space. Step iii is executed O ⁡ ( m ​ d) O(md) times and we can bound the time and space by simply multiplying the estimates above by m ​ d md. Taking the maximum of the complexity of Lemma 3 and the time spent in step iii yields the theorem, after noting that O ⁡ ( m ​ d 2 ​ p 1 / 2 ​ log ⁡ p) O(md^{2}p^{1/2}\log p) dominates all of the space bounds. ∎

We now present our main result, an average polynomial-time algorithm to compute the Cartier–Manin matrices of the reductions of a superelliptic curve X / 𝐐 X/\mathbf{Q} at all good primes p ≤ N p\leq N.

Algorithm ComputeCartierManinMatrices

Given m ≥ 2 m\geq 2 and squarefree f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] of degree d ≥ 3 d\geq 3, compute the Cartier–Manin matrices A p A_{p} of the reductions of X: y m = f ⁡ ( x) X\colon y^{m}=f(x) modulo primes p ≤ N p\leq N with p - m ​ lc ⁡ ( f) ​ disc ​ ( f) p\nmid m\operatorname{lc}(f)\operatorname{disc}(f) as follows:

1. 1.

For primes p ≤ N p\leq N with p - m ​ lc ⁡ ( f) ​ disc ​ ( f) p\nmid m\operatorname{lc}(f)\operatorname{disc}(f) initialize A p ∈ 𝐅 p g × g A_{p}\in\mathbf{F}_{p}^{g\times g} to the zero matrix.

2. 2.

Fix distinct a 1, …, a d 1 ∈ 𝐙 a_{1},\ldots,a_{d_{1}}\in\mathbf{Z} that include as many roots of f f as possible.

3. 3.

For each pair of integers j, ℓ ∈ [1, �] j,\ell\in[1,\mu]:

  1. a.

Compute the set P = { p 1, p 2, ⋯ } P=\{p_{1},p_{2},\cdots\} of primes p ≤ N p\leq N with j ​ p ≡ ℓ mod m jp\equiv\ell\bmod m
such that p - m ​ lc ⁡ ( f) ​ disc ​ ( f) p\nmid m\operatorname{lc}(f)\operatorname{disc}(f) and a 1, …, a d 1 a_{1},\ldots,a_{d_{1}} are distinct modulo p p.

  2. b.

If the set P P is empty proceed to the next pair j, ℓ j,\ell.

  3. c.

For i i from 1 1 to d j d_{j}:

    1. i.

Let f ⁡ ( x + a i) = x c ​ h ​ ( x) ∈ 𝐙 ⁡ [x] f(x+a_{i})=x^{c}h(x)\in\mathbf{Z}[x] with c ∈ { 0, 1 } c\in\{0,1\} and put r ≔ deg ⁡ ( h) r\coloneqq\deg(h).

    2. ii.

Let N ′ ≔ N N^{\prime}\coloneqq N if c = 0 c=0 and N ′ ≔ ⌊ ( j N − ℓ) / m) ⌋ N^{\prime}\coloneqq\lfloor(jN-\ell)/m)\rfloor otherwise.

    3. iii.

Define coprime moduli m 1, …, m N ′ m_{1},\ldots,m_{N^{\prime}} as follows:
D If c = 0 c=0 then m k ≔ k + 1 m_{k}\coloneqq k+1 for k + 1 ∈ P k+1\in P.
D If c = 1 c=1 then m k ≔ ( m ​ k + ℓ) / j m_{k}\coloneqq(mk+\ell)/j for ( m ​ k + ℓ) / j ∈ P (mk+\ell)/j\in P.
D For any m k m_{k} not defined above, let m k ≔ 1 m_{k}\coloneqq 1.
For p ∈ P p\in P let k ⁡ ( p) k(p) denote the index k k of the m k m_{k} for which m k = p m_{k}=p.

    4. iv.

Compute w k ≔ v 0 0 ​ ∏ i = 0 k − 1 M i ℓ mod m k w_{k}\coloneqq v_{0}^{0}\prod_{i=0}^{k-1}M_{i}^{\ell}\bmod m_{k} and u k ≔ k! mod m k u_{k}\coloneqq k!\bmod m_{k} for 1 ≤ k ≤ N ′ 1\leq k\leq N^{\prime} as in Corollary 17.

    5. v.

For p ∈ P p\in P use w k ⁡ ( p) w_{k(p)}, u k ⁡ ( p) u_{k(p)} to compute b 1 j ​ ℓ ​ ( a i) ∈ 𝐅 p d ℓ b_{1}^{j\ell}(a_{i})\in\mathbf{F}_{p}^{d_{\ell}} as in ComputeCartierManinMatrix.

  4. d.

For p ∈ P p\in P, let B 1 j ​ ℓ ∈ 𝐅 p d j × d ℓ B_{1}^{j\ell}\in\mathbf{F}_{p}^{d_{j}\times d_{\ell}} have rows b 1 j ​ ℓ ​ ( a i) ∈ 𝐅 p d ℓ b_{1}^{j\ell}(a_{i})\in\mathbf{F}_{p}^{d_{\ell}} as in ( 14), use B 1 j ​ ℓ B_{1}^{j\ell} to compute B j ​ ℓ ∈ 𝐅 p d j × d ℓ B^{j\ell}\in\mathbf{F}_{p}^{d_{j}\times d_{\ell}} via ( 15), and set the j, ℓ j,\ell block of A p A_{p} to B j ​ ℓ B^{j\ell} as in ( 8).

4. 4.

Let S S be the set of primes p ≤ N p\leq N satisfying p - m ​ lc ⁡ ( f) ​ disc ​ ( f) p\nmid m\operatorname{lc}(f)\operatorname{disc}(f) for which the a 1, … ​ a d 1 a_{1},\ldots a_{d_{1}} are not distinct modulo p p. For p ∈ S p\in S compute A p A_{p} using algorithm ComputeCartierManinMatrix if p ≥ d p\geq d and otherwise compute A p A_{p} directly from ( 8) by extracting coefficients of powers of f ∈ 𝐅 p ​ [x] f\in\mathbf{F}_{p}[x].

5. 5.

Output A p ∈ 𝐅 p g × g A_{p}\in\mathbf{F}_{p}^{g\times g} for all primes p ≤ N p\leq N such that p - m ​ lc ⁡ ( f) ​ disc ​ ( f) p\nmid m\operatorname{lc}(f)\operatorname{disc}(f).

###### Remark 18.

To compute Frobenius traces a p ∈ 𝐙 a_{p}\in\mathbf{Z}, we modify step 3 to loop over integers j = ℓ ∈ [1, �] j=\ell\in[1,\mu] and output just the traces of the A p A_{p} in step 5. This gives the traces of Frobenius a p mod p a_{p}\bmod p. For p > 16 ​ g 2 p>16g^{2} these determine a p ∈ 𝐙 a_{p}\in\mathbf{Z}, by the Weil bounds, and for p ≤ 16 ​ g 2 p\leq 16g^{2} we can compute a p = p + 1 − #​ X ​ ( 𝐅 p) a_{p}=p+1-\#X(\mathbf{F}_{p}) by enumerating values of f ⁡ ( x) f(x) and looking them up in a precomputed table of m m th powers.

###### Remark 19.

The inner loop in step 3.c is executed (up to) � ​ g \mu g times. Each of these computations is completely independent of the others, which makes it easy to efficiently distribute the work across � ​ g \mu g threads. In principal one can also parallelize the integer matrix multiplications performed by the RemainderForest algorithm in step iv, but in practice it is extremely difficult to do this efficiently.

We now prove Theorem 1, which we restate for convenience.

See 1

###### Proof.

The total time to compute all the sets P P using a sieve is bounded by O ⁡ ( N ​ log ⁡ N) O(N\log N) time using O ⁡ ( N) O(N) space, and this also bounds the total time and space for steps i, ii, iii, under our assumption that m, d, ‖ f ‖ = O ⁡ ( log ⁡ N) m,d,\|f\|=O(\log N). Corollary 17 yields an O ⁡ ( d 2 ​ N ​ log 3 ​ N) O(d^{2}N\log^{3}N) bound on each of the O ⁡ ( m 2 ​ d) O(m^{2}d) iterations of step iv. This yields the claimed time bound of O ⁡ ( m 2 ​ d 3 ​ N ​ log 3 ​ N) O(m^{2}d^{3}N\log^{3}N) for step 3.c, which we claim dominates. Lemma 13 implies that the total cost of step 3.d is bounded by O ⁡ ( � ​ ( N) ​ m 2 ​ d 3 ​ log ⁡ N) O(\pi(N)m^{2}d^{3}\log N), which is negligible, as is the cost of the rest of the algorithm. Note that the cardinality of the set S S in step 4 is at worst quadratic in d d and log ⁡ ( N) \log(N) under our assumption ‖ f ‖ = O ⁡ ( log ⁡ N) \|f\|=O(\log N), so we can easily afford the calls to ComputeCartierManinMatrix and use a brute force approach to compute A p A_{p} for primes p < d p<d of good reduction.

The space bound follows from the bound in Corollary 17, which covers steps iv (it is easy to see that all of the other steps fit within the claimed bound).

To compute Frobenius traces a p ∈ 𝐙 a_{p}\in\mathbf{Z} we apply Remark 18 and note that restricting to j = ℓ j=\ell in step 3 reduces the number of iterations of the main loop by a factor of m m. The cost of computing #​ X ​ ( 𝐅 p) \#X(\mathbf{F}_{p}) by looking up values of f ⁡ ( x) f(x) in a table of m m th powers is O ⁡ ( p ​ d) O(pd) ring operations in 𝐅 p \mathbf{F}_{p}. The total time to compute a p = p + 1 − #​ X ​ ( 𝐅 p) a_{p}=p+1-\#X(\mathbf{F}_{p}) for good p ≤ 16 ​ g 2 p\leq 16g^{2} is then O ⁡ ( d ​ g 2 ​ � ​ ( g 2) ​ log ​ g ​ log ⁡ log ⁡ g) = O ⁡ ( d ​ ( log ⁡ N) 4 ​ log ​ log ⁡ N) O(dg^{2}\pi(g^{2})\log g\log\log g)=O(d(\log N)^{4}\log\log N), which is negligible. ∎

## 7. Performance comparison

Tables 1 and 2 compare the performance of the average polynomial-time algorithm ComputeCartierManinMatrices with the O ~ ​ ( p 1 / 2) \tilde{O}(p^{1/2}) algorithm for computing zeta functions of cyclic covers implemented in Sage version 9.0. The Sage implementation provides the function CyclicCover which takes an integer m m and a squarefree polynomial f ∈ 𝐅 p ​ [x] f\in\mathbf{F}_{p}[x] and returns an object that represents a superelliptic curve y m = f ⁡ ( x) y^{m}=f(x) over 𝐅 p \mathbf{F}_{p}. Invoking the frobenius_matrix method of this object with the p p -adic precision set to 1 1 yields a matrix that encodes essentially the same information as the Cartier–Manin matrix A p A_{p}; in particular it determines the p p -rank of X X and its zeta function modulo p p.

Each table lists the genus g g and invariants m m and d d of a superelliptic curve X: y m = f ⁡ ( x) X\colon y^{m}=f(x) defined over 𝐐 \mathbf{Q} with f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] of degree d d. There is a row for every pair m ≥ 2 m\geq 2 and d ≥ 3 d\geq 3 for which m 2 ​ d 3 ≤ 6 5 m^{2}d^{3}\leq 6^{5}, which includes all superelliptic curves of genus g ≤ 5 g\leq 5 as well as plane quintics and sextics, and other curves of genus up to 15. The times listed are average times in milliseconds for primes p ≤ N p\leq N for increasing values of N N. For each N N three times are listed: one to compute Frobenius matrices using Sage, one to compute Cartier–Manin matrices using algorithm ComputeCartierManinMatrices, and one to to compute Frobenius traces via Remark 18. For the Sage timings we only computed Frobenius matrices for every n n th good prime p ≤ N p\leq N with n n chosen so that the computation would complete in less than a day (many of the computations would have taken months otherwise).

In Table 1 we show timings with f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] having coefficients f d + 1 − n ≔ p n f_{d+1-n}\coloneqq p_{n} for 1 ≤ n ≤ d 1\leq n\leq d, where p n p_{n} is the n n th prime. These polynomials are all irreducible, so our algorithm was unable to choose any a i a_{i} to be roots of f f; this is the generic situation, and the worst case for our algorithm. In Table 2 we show timings with f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] a product of linear factors, which represents the best case for our algorithm.

 |  |  |  | N = 2 16 N=2^{16} |  | N = 2 20 N=2^{20} |  | N = 2 24 N=2^{24} |  | N = 2 28 N=2^{28} |

g g | m m | d d |  | sage | matrix | trace |  | sage | matrix | trace |  | sage | matrix | trace |  | sage | matrix | trace |

1 | 2 | 3 |  | 21 | 0.01 | 0.01 |  | 27 | 0.05 | 0.05 |  | 67 | 0.13 | 0.13 |  | 230 | 0.30 | 0.30 |

1 | 2 | 4 |  | 27 | 0.04 | 0.04 |  | 41 | 0.17 | 0.16 |  | 120 | 0.42 | 0.42 |  | 454 | 0.95 | 0.93 |

1 | 3 | 3 |  | 27 | 0.02 | 0.02 |  | 46 | 0.08 | 0.08 |  | 141 | 0.20 | 0.20 |  | 499 | 0.48 | 0.49 |

2 | 2 | 5 |  | 30 | 0.08 | 0.08 |  | 55 | 0.38 | 0.38 |  | 163 | 0.92 | 0.92 |  | 580 | 2.02 | 2.01 |

2 | 2 | 6 |  | 42 | 0.16 | 0.16 |  | 83 | 0.73 | 0.74 |  | 280 | 1.77 | 1.77 |  | 1070 | 3.89 | 3.92 |

3 | 2 | 7 |  | 53 | 0.24 | 0.24 |  | 112 | 1.30 | 1.29 |  | 307 | 3.19 | 3.12 |  | 1217 | 6.47 | 6.71 |

3 | 2 | 8 |  | 74 | 0.34 | 0.34 |  | 169 | 2.15 | 2.07 |  | 528 | 5.02 | 4.94 |  | 2106 | 10.20 | 10.57 |

3 | 3 | 4 |  | 34 | 0.10 | 0.05 |  | 61 | 0.53 | 0.26 |  | 178 | 1.38 | 0.70 |  | 702 | 3.14 | 1.63 |

3 | 4 | 3 |  | 32 | 0.03 | 0.03 |  | 58 | 0.14 | 0.15 |  | 165 | 0.37 | 0.37 |  | 601 | 0.89 | 0.89 |

3 | 4 | 4 |  | 49 | 0.09 | 0.09 |  | 101 | 0.44 | 0.44 |  | 343 | 1.14 | 1.14 |  | 1283 | 2.55 | 2.63 |

4 | 2 | 9 |  | 96 | 0.43 | 0.44 |  | 194 | 3.22 | 3.24 |  | 576 | 7.65 | 7.70 |  | 2214 | 16.12 | 15.90 |

4 | 2 | 10 |  | 138 | 0.55 | 0.55 |  | 319 | 4.78 | 4.65 |  | 974 | 11.10 | 10.98 |  | 3693 | 22.13 | 22.79 |

4 | 3 | 5 |  | 47 | 0.22 | 0.11 |  | 93 | 1.29 | 0.65 |  | 287 | 3.37 | 1.67 |  | 1105 | 7.64 | 3.68 |

4 | 3 | 6 |  | 71 | 0.36 | 0.18 |  | 152 | 2.59 | 1.28 |  | 535 | 6.34 | 3.20 |  | 2121 | 14.04 | 7.07 |

4 | 5 | 3 |  | 37 | 0.08 | 0.03 |  | 68 | 0.40 | 0.13 |  | 200 | 1.19 | 0.40 |  | 778 | 2.96 | 0.99 |

4 | 6 | 3 |  | 49 | 0.05 | 0.06 |  | 112 | 0.24 | 0.24 |  | 313 | 0.64 | 0.64 |  | 1184 | 1.53 | 1.53 |

5 | 2 | 11 |  | 170 | 0.71 | 0.70 |  | 361 | 7.04 | 7.06 |  | 1024 | 16.57 | 16.30 |  | 3695 | 33.61 | 33.32 |

5 | 2 | 12 |  | 263 | 0.85 | 0.86 |  | 555 | 9.56 | 9.54 |  | 1537 | 21.84 | 22.23 |  | 5820 | 45.98 | 45.65 |

6 | 3 | 7 |  | 90 | 0.53 | 0.27 |  | 200 | 4.61 | 2.32 |  | 632 | 11.53 | 5.52 |  | 2360 | 24.18 | 12.18 |

6 | 4 | 5 |  | 63 | 0.31 | 0.20 |  | 130 | 1.71 | 1.08 |  | 424 | 4.37 | 2.73 |  | 1658 | 9.86 | 5.88 |

6 | 5 | 4 |  | 55 | 0.21 | 0.07 |  | 113 | 1.29 | 0.42 |  | 344 | 3.76 | 1.25 |  | 1358 | 9.08 | 3.03 |

6 | 5 | 5 |  | 90 | 0.39 | 0.13 |  | 201 | 3.06 | 1.02 |  | 671 | 8.98 | 2.92 |  | 2749 | 19.39 | 6.64 |

6 | 7 | 3 |  | 49 | 0.14 | 0.04 |  | 94 | 0.68 | 0.17 |  | 290 | 2.24 | 0.56 |  | 1146 | 5.57 | 1.39 |

7 | 3 | 8 |  | 134 | 0.75 | 0.38 |  | 294 | 8.17 | 4.05 |  | 835 | 19.07 | 9.38 |  | 3279 | 40.32 | 20.49 |

7 | 3 | 9 |  | 187 | 0.99 | 0.50 |  | 437 | 12.77 | 6.32 |  | 1462 | 28.54 | 14.50 |  | 5567 | 61.82 | 29.67 |

7 | 4 | 6 |  | 102 | 0.52 | 0.34 |  | 232 | 3.42 | 2.12 |  | 806 | 8.58 | 5.21 |  | 3160 | 18.99 | 11.54 |

7 | 6 | 4 |  | 75 | 0.21 | 0.15 |  | 153 | 1.08 | 0.77 |  | 524 | 2.79 | 2.00 |  | 2112 | 6.46 | 4.55 |

7 | 8 | 3 |  | 55 | 0.13 | 0.06 |  | 111 | 0.60 | 0.29 |  | 366 | 1.72 | 0.83 |  | 1333 | 4.32 | 2.00 |

7 | 9 | 3 |  | 67 | 0.16 | 0.06 |  | 140 | 0.82 | 0.26 |  | 479 | 2.64 | 0.82 |  | 1870 | 6.77 | 2.03 |

9 | 4 | 7 |  | 139 | 0.80 | 0.53 |  | 302 | 6.49 | 3.94 |  | 941 | 15.10 | 9.42 |  | 3566 | 32.97 | 20.43 |

9 | 7 | 4 |  | 75 | 0.40 | 0.08 |  | 156 | 2.77 | 0.56 |  | 510 | 9.14 | 1.78 |  | 2012 | 20.90 | 4.21 |

9 | 8 | 4 |  | 92 | 0.32 | 0.17 |  | 231 | 1.85 | 0.92 |  | 720 | 5.43 | 2.57 |  | 2941 | 12.58 | 6.12 |

9 | 10 | 3 |  | 65 | 0.16 | 0.08 |  | 137 | 0.76 | 0.34 |  | 429 | 2.29 | 1.01 |  | 1694 | 5.82 | 2.50 |

10 | 5 | 6 |  | 114 | 0.80 | 0.20 |  | 265 | 8.08 | 2.02 |  | 840 | 22.89 | 5.62 |  | 3256 | 51.62 | 12.42 |

10 | 6 | 5 |  | 97 | 0.43 | 0.32 |  | 206 | 2.51 | 1.83 |  | 701 | 6.28 | 4.61 |  | 2700 | 14.07 | 9.88 |

10 | 6 | 6 |  | 175 | 0.71 | 0.53 |  | 379 | 5.05 | 3.49 |  | 1278 | 11.95 | 8.59 |  | 5202 | 26.43 | 18.72 |

10 | 11 | 3 |  | 73 | 0.30 | 0.05 |  | 158 | 1.77 | 0.25 |  | 501 | 6.11 | 0.88 |  | 1878 | 15.32 | 2.12 |

10 | 12 | 3 |  | 91 | 0.17 | 0.11 |  | 187 | 0.80 | 0.49 |  | 636 | 2.35 | 1.39 |  | 2558 | 5.87 | 3.45 |

12 | 7 | 5 |  | 118 | 0.73 | 0.15 |  | 246 | 6.75 | 1.33 |  | 840 | 20.80 | 4.13 |  | 3228 | 48.09 | 9.23 |

12 | 9 | 4 |  | 94 | 0.43 | 0.14 |  | 199 | 2.88 | 0.87 |  | 657 | 8.87 | 2.64 |  | 2655 | 21.75 | 6.24 |

12 | 13 | 3 |  | 94 | 0.38 | 0.05 |  | 175 | 2.43 | 0.29 |  | 616 | 8.24 | 1.03 |  | 2244 | 20.02 | 2.49 |

13 | 10 | 4 |  | 117 | 0.47 | 0.19 |  | 264 | 2.90 | 1.09 |  | 1008 | 8.62 | 3.17 |  | 3762 | 20.08 | 7.47 |

13 | 14 | 3 |  | 90 | 0.30 | 0.09 |  | 193 | 1.58 | 0.43 |  | 619 | 5.01 | 1.36 |  | 2430 | 12.79 | 3.40 |

13 | 15 | 3 |  | 109 | 0.31 | 0.09 |  | 235 | 1.69 | 0.46 |  | 811 | 5.54 | 1.45 |  | 3238 | 13.99 | 3.72 |

15 | 11 | 4 |  | 111 | 0.81 | 0.10 |  | 252 | 6.29 | 0.79 |  | 839 | 22.76 | 2.84 |  | 3334 | 52.85 | 6.59 |

15 | 16 | 3 |  | 110 | 0.32 | 0.11 |  | 223 | 1.79 | 0.53 |  | 733 | 5.66 | 1.63 |  | 2805 | 14.16 | 4.13 |

Table 1. Comparison with O ~ ​ ( p 1 / 2) \tilde{O}(p^{1/2}) Sage 9.0 implementation [2] for superelliptic curves y m = f ⁡ ( x) y^{m}=f(x) where f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] is irreducible of degree d d. Times are millisecond averages per prime p ≤ N p\leq N for a single thread running on a 2.8GHz Cascade Lake Intel CPU. The sage column lists the average time to execute CyclicCover(m,f.change_ring(GF(p)).frobenius_matrix(1) in Sage 9.0, the matrix column lists the average time to compute the Cartier–Manin matrix modulo p p using algorithm ComputeCartierManinMatrices, and the trace column is the average time to compute the trace of Frobenius via Remark 18.

 |  |  |  | N = 2 16 N=2^{16} |  | N = 2 20 N=2^{20} |  | N = 2 24 N=2^{24} |  | N = 2 28 N=2^{28} |

g g | m m | d d |  | sage | matrix | trace |  | sage | matrix | trace |  | sage | matrix | trace |  | sage | matrix | trace |

1 | 2 | 3 |  | 20 | 0.01 | 0.01 |  | 28 | 0.01 | 0.01 |  | 73 | 0.04 | 0.04 |  | 230 | 0.09 | 0.08 |

1 | 2 | 4 |  | 26 | 0.01 | 0.01 |  | 43 | 0.04 | 0.05 |  | 119 | 0.12 | 0.12 |  | 456 | 0.28 | 0.27 |

1 | 3 | 3 |  | 27 | 0.00 | 0.00 |  | 45 | 0.01 | 0.01 |  | 131 | 0.02 | 0.02 |  | 500 | 0.05 | 0.05 |

2 | 2 | 5 |  | 29 | 0.03 | 0.03 |  | 53 | 0.11 | 0.12 |  | 151 | 0.31 | 0.30 |  | 583 | 0.72 | 0.72 |

2 | 2 | 6 |  | 41 | 0.05 | 0.06 |  | 84 | 0.26 | 0.28 |  | 267 | 0.66 | 0.64 |  | 1071 | 1.40 | 1.40 |

3 | 2 | 7 |  | 53 | 0.10 | 0.10 |  | 116 | 0.55 | 0.54 |  | 311 | 1.22 | 1.20 |  | 1219 | 2.58 | 2.59 |

3 | 2 | 8 |  | 77 | 0.13 | 0.14 |  | 164 | 0.94 | 0.92 |  | 532 | 2.06 | 2.04 |  | 2094 | 4.19 | 4.23 |

3 | 3 | 4 |  | 34 | 0.03 | 0.02 |  | 62 | 0.14 | 0.07 |  | 184 | 0.41 | 0.20 |  | 701 | 0.96 | 0.47 |

3 | 4 | 3 |  | 31 | 0.01 | 0.01 |  | 55 | 0.03 | 0.03 |  | 157 | 0.08 | 0.08 |  | 605 | 0.20 | 0.20 |

3 | 4 | 4 |  | 48 | 0.02 | 0.02 |  | 103 | 0.08 | 0.09 |  | 334 | 0.23 | 0.23 |  | 1286 | 0.55 | 0.54 |

4 | 2 | 9 |  | 94 | 0.19 | 0.19 |  | 199 | 1.50 | 1.47 |  | 586 | 3.48 | 3.41 |  | 2232 | 7.10 | 7.12 |

4 | 2 | 10 |  | 135 | 0.25 | 0.25 |  | 295 | 2.30 | 2.29 |  | 942 | 5.37 | 5.24 |  | 3816 | 10.53 | 10.37 |

4 | 3 | 5 |  | 46 | 0.07 | 0.04 |  | 92 | 0.38 | 0.19 |  | 283 | 1.06 | 0.51 |  | 1111 | 2.40 | 1.21 |

4 | 3 | 6 |  | 72 | 0.12 | 0.06 |  | 153 | 0.79 | 0.41 |  | 529 | 1.85 | 0.91 |  | 2098 | 3.96 | 1.99 |

4 | 5 | 3 |  | 38 | 0.02 | 0.01 |  | 68 | 0.05 | 0.02 |  | 202 | 0.16 | 0.05 |  | 780 | 0.39 | 0.13 |

4 | 6 | 3 |  | 48 | 0.01 | 0.01 |  | 95 | 0.03 | 0.03 |  | 301 | 0.09 | 0.09 |  | 1186 | 0.22 | 0.21 |

5 | 2 | 11 |  | 171 | 0.31 | 0.31 |  | 354 | 3.45 | 3.46 |  | 977 | 7.85 | 7.87 |  | 3682 | 15.94 | 15.85 |

5 | 2 | 12 |  | 246 | 0.37 | 0.40 |  | 530 | 5.11 | 5.12 |  | 1543 | 11.30 | 11.17 |  | 5857 | 22.61 | 22.62 |

6 | 3 | 7 |  | 89 | 0.19 | 0.10 |  | 192 | 1.47 | 0.72 |  | 605 | 3.57 | 1.78 |  | 2361 | 7.67 | 3.79 |

6 | 4 | 5 |  | 64 | 0.08 | 0.05 |  | 136 | 0.32 | 0.25 |  | 416 | 0.94 | 0.61 |  | 1660 | 2.17 | 1.43 |

6 | 5 | 4 |  | 55 | 0.07 | 0.03 |  | 108 | 0.30 | 0.10 |  | 348 | 1.00 | 0.32 |  | 1369 | 2.43 | 0.81 |

6 | 5 | 5 |  | 92 | 0.09 | 0.03 |  | 196 | 0.52 | 0.15 |  | 710 | 1.48 | 0.48 |  | 2755 | 3.49 | 1.16 |

6 | 7 | 3 |  | 50 | 0.03 | 0.01 |  | 96 | 0.06 | 0.02 |  | 296 | 0.23 | 0.06 |  | 1146 | 0.63 | 0.15 |

7 | 3 | 8 |  | 125 | 0.28 | 0.16 |  | 276 | 3.05 | 1.54 |  | 836 | 7.04 | 3.49 |  | 3234 | 15.09 | 7.64 |

7 | 3 | 9 |  | 193 | 0.35 | 0.18 |  | 427 | 4.09 | 2.16 |  | 1409 | 9.28 | 4.74 |  | 5551 | 21.20 | 10.35 |

7 | 4 | 6 |  | 98 | 0.17 | 0.12 |  | 227 | 0.98 | 0.65 |  | 774 | 2.30 | 1.48 |  | 3143 | 5.26 | 3.33 |

7 | 6 | 4 |  | 70 | 0.06 | 0.04 |  | 155 | 0.23 | 0.17 |  | 525 | 0.66 | 0.44 |  | 2108 | 1.53 | 1.04 |

7 | 8 | 3 |  | 55 | 0.02 | 0.02 |  | 111 | 0.06 | 0.04 |  | 343 | 0.20 | 0.12 |  | 1333 | 0.51 | 0.30 |

7 | 9 | 3 |  | 69 | 0.03 | 0.01 |  | 141 | 0.08 | 0.03 |  | 476 | 0.28 | 0.09 |  | 1876 | 0.76 | 0.23 |

9 | 4 | 7 |  | 127 | 0.30 | 0.19 |  | 289 | 1.85 | 1.23 |  | 917 | 4.56 | 2.88 |  | 3555 | 10.28 | 6.23 |

9 | 7 | 4 |  | 71 | 0.12 | 0.03 |  | 156 | 0.61 | 0.10 |  | 509 | 1.78 | 0.35 |  | 2007 | 4.47 | 0.88 |

9 | 8 | 4 |  | 93 | 0.09 | 0.04 |  | 211 | 0.33 | 0.18 |  | 752 | 1.05 | 0.50 |  | 2946 | 2.64 | 1.23 |

9 | 10 | 3 |  | 76 | 0.04 | 0.02 |  | 139 | 0.08 | 0.04 |  | 430 | 0.26 | 0.12 |  | 1694 | 0.66 | 0.31 |

10 | 5 | 6 |  | 115 | 0.25 | 0.07 |  | 253 | 2.08 | 0.52 |  | 825 | 5.96 | 1.49 |  | 3265 | 13.97 | 3.37 |

10 | 6 | 5 |  | 101 | 0.13 | 0.09 |  | 213 | 0.68 | 0.42 |  | 676 | 1.61 | 1.06 |  | 2693 | 3.83 | 2.43 |

10 | 6 | 6 |  | 155 | 0.19 | 0.15 |  | 365 | 1.23 | 0.86 |  | 1276 | 2.94 | 2.00 |  | 5195 | 6.46 | 4.34 |

10 | 11 | 3 |  | 74 | 0.05 | 0.01 |  | 154 | 0.14 | 0.02 |  | 477 | 0.52 | 0.08 |  | 1878 | 1.48 | 0.21 |

10 | 12 | 3 |  | 87 | 0.03 | 0.02 |  | 189 | 0.08 | 0.07 |  | 640 | 0.26 | 0.17 |  | 2552 | 0.63 | 0.42 |

12 | 7 | 5 |  | 113 | 0.18 | 0.04 |  | 242 | 1.22 | 0.24 |  | 879 | 3.99 | 0.77 |  | 3227 | 9.89 | 1.93 |

12 | 9 | 4 |  | 95 | 0.11 | 0.04 |  | 204 | 0.60 | 0.17 |  | 672 | 1.66 | 0.52 |  | 2663 | 4.30 | 1.26 |

12 | 13 | 3 |  | 83 | 0.06 | 0.01 |  | 175 | 0.19 | 0.02 |  | 569 | 0.71 | 0.09 |  | 2245 | 2.06 | 0.25 |

13 | 10 | 4 |  | 119 | 0.13 | 0.05 |  | 267 | 0.64 | 0.22 |  | 942 | 1.69 | 0.65 |  | 3779 | 4.32 | 1.56 |

13 | 14 | 3 |  | 92 | 0.05 | 0.02 |  | 191 | 0.14 | 0.05 |  | 617 | 0.47 | 0.15 |  | 2429 | 1.23 | 0.37 |

13 | 15 | 3 |  | 111 | 0.05 | 0.02 |  | 240 | 0.14 | 0.04 |  | 806 | 0.50 | 0.14 |  | 3246 | 1.35 | 0.36 |

15 | 11 | 4 |  | 119 | 0.20 | 0.04 |  | 251 | 1.15 | 0.14 |  | 836 | 3.92 | 0.49 |  | 3314 | 9.89 | 1.26 |

15 | 16 | 3 |  | 100 | 0.05 | 0.02 |  | 218 | 0.15 | 0.06 |  | 728 | 0.52 | 0.19 |  | 2797 | 1.37 | 0.48 |

Table 2. Timings for superelliptic curves X: y m = f ⁡ ( x) X\colon y^{m}=f(x) when f ∈ 𝐙 ⁡ [x] f\in\mathbf{Z}[x] splits into d d distinct linear factors. Times are millisecond averages per prime p ≤ N p\leq N for a single thread running on a 2.8GHz Cascade Lake Intel CPU. The sage column lists the average time to execute CyclicCover(m,f.change_ring(GF(p)).frobenius_matrix(1) in Sage 9.0, the matrix column lists the average time to compute the Cartier–Manin matrix modulo p p using algorithm ComputeCartierManinMatrices, and the trace column is the average time to compute the trace of Frobenius via Remark 18.

## References

- [1] Jeffrey D. Achter and Everett W. Howe, [Hasse–Witt and Cartier–Manin matrices: A warning and a request][4], Arithmetic Geometry: Computations and Applications, Contemporary Mathematics 722 (2019), 1–18, American Mathematical Society. (MathSciNet: [MR3896846][5], arXiv: [1710.10726v5][6])
- [2] Vishal Arul, Alex J. Best, Edgar Costa, Richard Magner, Nicholas Triantafillou, [Computing zeta functions of cyclic covers in large characteristic][7], in Algorithmic Number Theory 13th International Symposium (ANTS XIII), Open Book Series 2 (2019), 37–53, Mathematical. Sciences. Publishers. (MathSciNet: [MR3952003][8], arXiv: [1806.02262][9])
- [3] Andrew R. Booker, Jeroen Sijsling, Andrew V. Sutherland, John Voight, and Dan Yasaki [A database of genus 2 curves over the rational numbers][10], Twelfth Algorithmic Number Theory Symposium (ANTS XII), LMS J. Comput. Math. 19a (2016), 235–254. (MathSciNet: [MR3540958][11], arXiv: [1602.03715][12])
- [4] Wieb Bosma, John Cannon, and Catherine Playoust, [The Magma algebra system. I. The user language][13], J. Symbolic Comput. 24 (1997), 235–265. (MathSciNet: [MR1484478][14]).
- [5] Alan Bostan, Pierrick Gaudry and Éric Schost. [Linear recurrences with polynomial coefficients and application to integer factorization and Cartier–Manin operator][15], SIAM J. Comput. 36 (2007), 1777–1806. (MathSciNet: [MR2299425][16], HAL-Inria: [00103401][17])
- [6] Irene Bouw, [The p p -rank of ramified covers curves][18], Compositio Math. 126 (2001), 295–322. (MathSciNet: [MR1834740][19])
- [7] Irene Bouw, Stefan Wewers, [Computing L L -functions and semistable reduction of superelliptic curves][20], Glasg. Math. J. 59 (2017), 77-108. (MathSciNet: [MR3576328][21], arXiv: [1211.4459][22])
- [8] Alina Bucur, Francesc Fité, and Kiran S. Kedlaya, [Effective Sato-Tate conjecture for abelian varieties and applications][23], preprint, 2020. (arXiv: [2002.08807][23])
- [9] Claude Chevalley, [Introduction to the theory of algebraic functions of one variable][24], Mathematical Surveys, 6 (1951), American Mathematical Society. (MathSciNet: [MR0042164][25])
- [10] Edgar Costa, Francesc Fité, and Andrew V. Sutherland, [Arithmetic invariants form Sato–Tate moments][26], C.R. Math. Acad. Sci. Paris 357 (2019)), 823–826. (MathSciNet: [MR4038255][27], arXiv: [1910.00518][28])
- [11] Alfredo Eisinberg and Giuseppe Fedele, [On the inversion of the Vandermonde matrix][29], Appl. Math. Comput. 174 (2006), 1384–1397. (MathSciNet: [MR2220623][30]).
- [12] Francesc Fité, Kiran S. Kedlaya, Victor Rotger, and Andrew V. Sutherland, [Sato-Tate distributions and Galois endomorphism modules in genus 2 2][31], Compositio Mathematica 148 (2012), 1390–1442. (MathSciNet: [MR2982436][32], arXiv: [1110.6638][33])
- [13] Francesc Fité, Kiran S. Kedlaya, and Andrew V. Sutherland, [Sato–Tate groups of abelian threefolds: a preview of the classification][34], in Arithmetic Geometry, Cryptography, and Coding Theory, Contemp. Math. 770 (2021), 103–129 (MathSciNet: [MR4280389][35], arXiv: [1911.02071][36])
- [14] Cécile Gonçalves, [A point counting algorithm for cyclic covers of the projective line][37], Algorithmic Arithmetic, Geometry, and Coding Theory, Contemp. Math. 637 (2015), 145–172, American Mathematical Society. (MathSciNet: [MR3364447][38], arXiv: [1408.2095][39])
- [15] Joachim von zur Gathen and Jürgen Gerhard, [Modern computer algebra][40], third edition, Cambridge University Press, 2013. (MathSciNet: [MR3087522][41])
- [16] Daniel Gorenstein, [An arithmetic theory of adjoint plane curves][42], Trans. Amer. Math. Soc. 72 (1952), 414–436. (MathSciNet: [MR0049591][43])
- [17] David Harvey, [Computing zeta functions of arithmetic schemes][44], Proc. Lond. Math. Soc. 111 (2015), 1379–1401. (MathSciNet: [MR3447797][45] arXiv: [1402.3439][46]).
- [18] David Harvey and Joris van der Hoeven, [Integer multiplication in time O ⁡ ( n ​ log ⁡ n) O(n\log n)][47], Annals of Math. 193 (2021), 563–617. (MathSciNet: [MR4224716][48], HAL: [02070778][49])
- [19] David Harvey and Joris van der Hoeven, [Polynomial multiplication over finite fields in time O ⁡ ( n ​ log ⁡ n) O(n\log n)][50], preprint, 2019. (HAL: [02070816][51])
- [20] David Harvey, Maike Massierer, and Andrew V. Sutherland, [Computing L L -series of geometrically hyperelliptic curves of genus three][52], in Algorithmic Number Theory 12th International Symposium (ANTS XII), LMS J. Comput. Math. 19A (2016), 220–234. (MathSciNet: [MR3540957][53], arXiv: [1605.04708][54])
- [21] David Harvey and Andrew V. Sutherland, [Computing Hasse–Witt matrices of hyperelliptic curves in average polynomial time][55], Algorithmic Number Theory 11th International Symposium (ANTS XI), LMS J. Comput. Math. 17A (2014), 257–273. (MathSciNet: [MR3240808][56], arXiv: [1402.3246][57])
- [22] David Harvey and Andrew V. Sutherland, [Computing Hasse–Witt matrices of hyperelliptic curves in average polynomial time, II][58], in Frobenius Distributions: Lang–Trotter and Sato–Tate Conjectures, Contemp. Math. 663 (2016), 127–147, American Mathematical Society. (MathSciNet: [MR3502941][59] arXiv: [1410.5222][60])
- [23] Pascal Molin and Christian Neurohr, [Computing period matrices and the Abel-Jacobi map of superelliptic curves][61], Math. Comp. 88 (2019), 847–888. (MathSciNet: [MR3882287][62], arXiv: [1707.07249][63])
- [24] Moritz Minzlaff, [Computing zeta functions of superelliptic curves in larger characteristic][64], Math. Comput. Sci. 3 (2010), 209–224. (MathSciNet: [MR2608297][65])
- [25] The Sage Developers, [SageMath, the Sage Mathematics Software System Version 9.0][66], available at [https://www.sagemath.org][66], 2019.
- [26] Henning Stichtenoth, [Algebraic function fields and codes][67], Springer, 2009. (MathSciNet: [MR2464941][68])
- [27] Karl-Otto Stöhr and José Felipe Voloch, [A formula for the Cartier operator on plane algebraic curves][69], J. Reine Angew. Math. 377 (1987), 49–64. (MathSciNet: [MR0887399][70])
- [28] Jean-Pierre Serre, [Lectures on N X ​ ( p) N_{X}(p)][71], Research Notes in Mathematics 11, CRC Press, 2012. (MathSciNet: [MR2920749][72])
- [29] Jean-Pierre Serre, Record primes, personal communication, September 19, 2019.
- [30] Andrew V. Sutherland, [A database of nonhyerelliptic curves over 𝐐 \mathbf{Q}][73], Thirteenth Algorithmic Number Theory Symposium (ANTS XIII), Open Book Series 2 (2019), 443–459. (MathSciNet: [MR3952027][74], arXiv: [1806.06289][75])
- [31] Yuri G. Zarhin, [Endomorphism algebras of abelian varieties with special reference to superelliptic Jacobians][76], in Geometry, Algebra, Number Theory, and their Information Technology Appl., Springer Roc. Math. Stat. 251, 2018 (MathSciNet: [MR3880401][77], arXiv: [1706.00110][78])


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://en.wikipedia.org/wiki/Peter_Montgomery_(mathematician)
[4]: https://www.ams.org/books/conm/722/14534
[5]: https://mathscinet.ams.org/mathscinet-getitem?mr=3896846
[6]: https://arxiv.org/abs/1710.10726v5
[7]: https://msp.org/obs/2019/2-1/p03.xhtml
[8]: https://mathscinet.ams.org/mathscinet-getitem?mr=3952003
[9]: https://arxiv.org/abs/1806.02262
[10]: https://dx.doi.org/10.1112/S146115701600019X
[11]: https://mathscinet.ams.org/mathscinet-getitem?mr=3540958
[12]: https://arxiv.org/abs/1602.03715
[13]: http://dx.doi.org/10.1006/jsco.1996.0125
[14]: https://mathscinet.ams.org/mathscinet-getitem?mr=1484478
[15]: https://doi.org/10.1137/S0097539704443793
[16]: https://mathscinet.ams.org/mathscinet-getitem?mr=2299425
[17]: https://hal.inria.fr/inria-00103401/
[18]: https://www.cambridge.org/core/journals/compositio-mathematica/article/prank-of-ramified-covers-of-curves/6D1BEC9200F6849339665AC4371AB7AF
[19]: https://mathscinet.ams.org/mathscinet-getitem?mr=1834740
[20]: https://doi.org/10.1017/S0017089516000057
[21]: https://mathscinet.ams.org/mathscinet-getitem?mr=3576328
[22]: https://arxiv.org/abs/1211.4459
[23]: https://arxiv.org/abs/2002.08807
[24]: https://doi.org/10.1090/surv/006
[25]: https://mathscinet.ams.org/mathscinet-getitem?mr=0042164
[26]: https://doi.org/10.1016/j.crma.2019.11.008
[27]: https://mathscinet.ams.org/mathscinet-getitem?mr=4038255
[28]: https://arxiv.org/abs/1910.00518
[29]: https://doi.org/10.1016/j.amc.2005.06.014
[30]: https://mathscinet.ams.org/mathscinet-getitem?mr=2220623
[31]: https://doi.org/10.1112/S0010437X12000279
[32]: https://mathscinet.ams.org/mathscinet-getitem?mr=2982436
[33]: https://arxiv.org/abs/1110.6638
[34]: https://www.ams.org/books/conm/770/
[35]: https://mathscinet.ams.org/mathscinet-getitem?mr=4280389
[36]: https://arxiv.org/abs/1911.02071
[37]: https://doi.org/10.1090/conm/637/12754
[38]: https://mathscinet.ams.org/mathscinet-getitem?mr=3364447
[39]: https://arxiv.org/abs/1408.2095
[40]: https://doi.org/10.1017/CBO9781139856065
[41]: https://mathscinet.ams.org/mathscinet-getitem?mr=3087522
[42]: https://doi.org/10.2307/1990710
[43]: https://mathscinet.ams.org/mathscinet-getitem?mr=0049591
[44]: https://doi.org/10.1112/plms/pdv056
[45]: https://mathscinet.ams.org/mathscinet-getitem?mr=3447797
[46]: https://arxiv.org/abs/1402.3439
[47]: https://doi.org/10.4007/annals.2021.193.2.4
[48]: https://mathscinet.ams.org/mathscinet-getitem?mr=4224716
[49]: https://hal.archives-ouvertes.fr/hal-02070778/
[50]: https://hal.archives-ouvertes.fr/hal-02070816/document
[51]: https://hal.archives-ouvertes.fr/hal-02070816/
[52]: https://doi.org/10.1112/S1461157016000383
[53]: https://mathscinet.ams.org/mathscinet-getitem?mr=3540957
[54]: https://arxiv.org/abs/1605.04708
[55]: https://dx.doi.org/10.1112/S1461157014000187
[56]: https://mathscinet.ams.org/mathscinet-getitem?mr=3240808
[57]: https://arxiv.org/abs/1402.3246
[58]: https://doi.org/10.1090/conm/663/13352
[59]: https://mathscinet.ams.org/mathscinet-getitem?mr=3502941
[60]: https://arxiv.org/abs/1410.5222
[61]: https://doi.org/10.1090/mcom/3351
[62]: https://mathscinet.ams.org/mathscinet-getitem?mr=3882287
[63]: https://arxiv.org/abs/1707.07249
[64]: https://link.springer.com/article/10.1007/11786-009-0019-4
[65]: https://mathscinet.ams.org/mathscinet-getitem?mr=2608297
[66]: https://www.sagemath.org
[67]: https://doi.org/10.1007/978-3-540-76878-4
[68]: https://mathscinet.ams.org/mathscinet-getitem?mr=2464941
[69]: https://doi.org/10.1515/crll.1987.377.49
[70]: https://mathscinet.ams.org/mathscinet-getitem?mr=0887399
[71]: http://www.crcnetbase.com/isbn/9781466501935
[72]: https://mathscinet.ams.org/mathscinet-getitem?mr=2920749
[73]: https://msp.org/obs/2019/2-1/p27.xhtml
[74]: https://mathscinet.ams.org/mathscinet-getitem?mr=3952027
[75]: https://arxiv.org/abs/1806.06289
[76]: https://link.springer.com/content/pdf/10.1007/978-3-319-97379-1.pdf
[77]: https://mathscinet.ams.org/mathscinet-getitem?mr=3880401
[78]: https://arxiv.org/abs/1706.00110
