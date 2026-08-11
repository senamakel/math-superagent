<!-- source: https://ar5iv.labs.arxiv.org/html/1108.3113 | converted from HTML -->

[1108.3113] Cubes of integral vectors in dimension four

# Cubes of integral vectors in dimension four Thanks: Supported by Hungarian Nat. Sci. Found. (OTKA) Grant No. NK72523.

Emil W. Kiss, Péter Kutas Emil W. Kiss Eötvös University
Department of Algebra and Number Theory
1117 Budapest, Pázmány Péter sétány 1/c
Hungary Email address, Emil W. Kiss : [ewkiss@math.elte.hu][1] Email address, Péter Kutas : [kutasp@gmail.com][2]

Date: Int4vec8, 22 April, 2011

###### Abstract.

A system of m m nonzero vectors in ℤ n \BZ^{n} is called an m m -icube if they are pairwise orthogonal and have the same length. The paper describes m m -icubes in ℤ 4 \BZ^{4} for 2 ≤ m ≤ 4 2\leq m\leq 4 using Hurwitz integral quaternions, counts the number of them with given edge length, and proves that unlimited extension is possible in ℤ 4 \BZ^{4}.

###### Key words and phrases:

Integral cube, Hurwitz integral quaternion

###### 1991 Mathematics Subject Classification

11R52, 52C07

## 1. Introduction and main results

Two vectors are called *twins*if they are orthogonal, and have the same length. An *m m -icube*in ℤ n \BZ^{n} is a sequence ( v 1, …, v m) (v_{1},\ldots,v_{m}) of nonzero vectors in ℤ n \BZ^{n} that are twins pairwise. The common *length*of the vectors v ℓ v_{\ell} is the *edge length*of the icube. By the *norm*of v ℓ v_{\ell} we mean the square of its length. The main object of this paper is to study how icubes can be constructed, extended and counted. The paper [3] investigates these questions extensively in ℤ 3 \BZ^{3}, using the number theory of quaternions.

For a trivial example, if the dimension is even, then every vector ( a 1, …, a n) (a_{1},\ldots,a_{n}) has a twin, namely ( a 2, − a 1, a 4, − a 3, …, a n, − a n − 1) (a_{2},-a_{1},a_{4},-a_{3},\ldots,a_{n},-a_{n-1}). Similarly, the rows of the matrix

 | ( a b c d e f g h b − a d − c f − e − h g c − d − a b g h − e − f d c − b − a h − g f − e e − f − g − h − a b c d f e − h g − b − a − d c g h e − f − c d − a − b h − g f e − d − c b − a) \begin{pmatrix}a&\hphantom{-}b&\hphantom{-}c&\hphantom{-}d&\hphantom{-}e&\hphantom{-}f&\hphantom{-}g&\hphantom{-}h\\ b&-a&\hphantom{-}d&-c&\hphantom{-}f&-e&-h&\hphantom{-}g\\ c&-d&-a&\hphantom{-}b&\hphantom{-}g&\hphantom{-}h&-e&-f\\ d&\hphantom{-}c&-b&-a&\hphantom{-}h&-g&\hphantom{-}f&-e\\ e&-f&-g&-h&-a&\hphantom{-}b&\hphantom{-}c&\hphantom{-}d\\ f&\hphantom{-}e&-h&\hphantom{-}g&-b&-a&-d&\hphantom{-}c\\ g&\hphantom{-}h&\hphantom{-}e&-f&-c&\hphantom{-}d&-a&-b\\ h&-g&\hphantom{-}f&\hphantom{-}e&-d&-c&\hphantom{-}b&-a\end{pmatrix} |  |

form an 8 8 -icube, proving that every 8 8 -dimensional integral vector can be extended to an 8 8 -icube. The above matrix comes from the multiplication table of Cayley-numbers. The 4 × 4 4\times 4 minor in the upper left corner yields a 4 4 -icube in dimension 4 4, extending an arbitrary element of ℤ 4 \BZ^{4}.

Classical results of Hurwitz [6] and Radon [7] show, however, that a similar “permutational” extension is possible only in dimensions 1 1, 2 2, 4 4 and 8 8 (an interesting approach using extraspecial 2 2 -groups is given by Eckmann in [2]). To prove further extension theorems we have to explore the number-theoretic structure of the components of the vectors. An example for this type of argument is the Euler-matrix

 | ( m 2 + n 2 − p 2 − q 2 − 2 ​ m ​ q + 2 ​ n ​ p 2 ​ m ​ p + 2 ​ n ​ q 2 ​ m ​ q + 2 ​ n ​ p m 2 − n 2 + p 2 − q 2 − 2 ​ m ​ n + 2 ​ p ​ q − 2 ​ m ​ p + 2 ​ n ​ q 2 ​ m ​ n + 2 ​ p ​ q m 2 − n 2 − p 2 + q 2), \begin{pmatrix}m^{2}+n^{2}-p^{2}-q^{2}&-2mq+2np&2mp+2nq\\ 2mq+2np&m^{2}-n^{2}+p^{2}-q^{2}&-2mn+2pq\\ -2mp+2nq&2mn+2pq&m^{2}-n^{2}-p^{2}+q^{2}\end{pmatrix}\,, |  |

which is a “typical” 3 3 -icube in dimension 3 3 (see [8] and [3]). We start with an extension theorem that generalizes Corollary 5.11 of [3].

###### Theorem 1.1.

Let ( v 1, …, v n − 1) (v_{1},\ldots,v_{n-1}) be an n − 1 n-1 -icube in ℤ n \BZ^{n}, where n ≥ 2 n\geq 2. If n n is even, then this icube can be extended to an n n -icube. If n n is odd, then such an extension is possible if and only if the common length of the vectors v ℓ v_{\ell} is an integer.

Note that this extending vector, if exists, is obviously unique up to sign.

###### Proof.

Let N N denote the edge norm of ( v 1, …, v n − 1) (v_{1},\ldots,v_{n-1}). By Proposition 1.3 of [3], if n n is odd, then the edge length of any n n -icube in ℤ n \BZ^{n} is an integer. Therefore an extension is only possible if n n is even or if N N is a square.

Define L L to be the n × ( n − 1) n\times(n-1) matrix whose columns are v 1, …, v n − 1 v_{1},\ldots,v_{n-1}. Then L T ​ L = N ​ I n − 1 L^{T}L=NI_{n-1} (where I n − 1 I_{n-1} denotes the identity matrix). The Cauchy-Binet formula therefore implies that

 | det ( L 1) 2 + ⋯ + det ( L n) 2 = N n − 1, \det(L_{1})^{2}+\dots+\det(L_{n})^{2}=N^{n-1}\,, |  |

where L i L_{i} is the minor of L L obtained by deleting the i i -th row.

Let M i = ( − 1) n + i ​ det ( L i) M_{i}=(-1)^{n+i}\det(L_{i}). Add a last column to L L whose entries are M i / N ( n − 2) / 2 M_{i}/N^{(n-2)/2}, and denote the resulting matrix by K K. Then the columns of L L are pairwise orthogonal by the Laplace expansion theorem for determinants. The displayed formula above shows that K T ​ K = N ​ I n K^{T}K=NI_{n}. This implies that K ​ K T = N ​ I n KK^{T}=NI_{n}. Denote the rows of L L by s i s_{i}. We get that the scalar product of s i s_{i} by itself, which is an integer, equals N − M i 2 / N n − 2 N-M_{i}^{2}/N^{n-2}. Therefore if n n is even or if N N is a square, then N ( n − 2) / 2 N^{(n-2)/2} divides M i M_{i}, and the last column of K K consists of integers. ∎

Here are the main results of this paper.

###### Theorem 1.2.

Every m m -icube in ℤ 4 \BZ^{4} can be extended to a 4 4 -icube for 1 ≤ m ≤ 3 1\leq m\leq 3.

Of course, the only nontrivial case occurs when m = 2 m=2, according to the statements above. The proof is found at the end of Section 3.

The following result, proved in Section 4, counts the number of m m -icubes in ℤ 4 \BZ^{4}. Denote by f m ​ ( N) f_{m}(N) the number of m m -icubes with edge norm N N (that is, edge length N \sqrt{N}) in ℤ 4 \BZ^{4}. A famous theorem by Jacobi provides the value of f 1 ​ ( N) f_{1}(N), we include it for comparison. Let c m = 24 ⋅ 2 m / ( 4 − m)! c_{m}=24\cdot 2^{m}/(4-m)!, thus c 1 = 8 c_{1}=8, c 2 = 48 c_{2}=48, c 3 = 192 c_{3}=192 and c 4 = 384 c_{4}=384. Furthermore, if p p is a (positive) odd prime and k ≥ 1 k\geq 1, then define

 | g ⁡ ( p k) = ( k + 1) ​ p k ​ ( p 2 − 1) − 2 ​ ( p k + 1 − 1) ( p − 1) 2. g(p^{k})=\frac{(k+1)p^{k}(p^{2}-1)-2(p^{k+1}-1)}{(p-1)^{2}}\,. |  |

###### Theorem 1.3.

Let g m ​ ( N) = f m ​ ( N) / c m g_{m}(N)=f_{m}(N)/c_{m}. Then g m g_{m} is a multiplicative function for every 1 ≤ m ≤ 4 1\leq m\leq 4, whose value on prime powers is given by the following formulae, where p p is an odd prime and k ≥ 1 k\geq 1.

1. ( 1) (1)

g m ​ ( 2 k) = 3 g_{m}(2^{k})=3 for every k ≥ 1 k\geq 1.

2. ( 2) (2)

g 1 ​ ( p k) = σ ⁡ ( p k) = ( p k + 1 − 1) / ( p − 1) g_{1}(p^{k})=\sigma(p^{k})=(p^{k+1}-1)/(p-1) (this is Jacobi’s classical result) and g 3 ​ ( p k) = g 4 ​ ( p k) = g ⁡ ( p k) g_{3}(p^{k})=g_{4}(p^{k})=g(p^{k}) (the function defined before the theorem).

3. ( 3) (3)

If p ≡ 3 ​ ( 4) p\equiv 3~(4), then g 2 ​ ( p k) = g ⁡ ( p k) g_{2}(p^{k})=g(p^{k}). If p ≡ 1 ​ ( 4) p\equiv 1~(4), then g 2 ​ ( p k) = ( k + 1) ​ p k g_{2}(p^{k})=(k+1)p^{k}.

In particular, we have that f 4 ​ ( N) = 2 ​ f 3 ​ ( N) f_{4}(N)=2f_{3}(N).

The proofs are based on a representation theorem of icubes using Hurwitz integral quaternions (see Theorems 3.5, 3.9, 4.2 and 4.4).

## 2. Integral quaternions

We review some properties of integral quaternions. The general references are [1], [5] and [4], but we ask the reader to browse Section 2 of [3] for background, as we shall use the notation and the results introduced there. The *norm*of α = a + b ​ i + c ​ j + d ​ k \alpha=a+bi+cj+dk is N ⁡ ( α) = a 2 + b 2 + c 2 + d 2 \Norm(\alpha)=a^{2}+b^{2}+c^{2}+d^{2}. This α \alpha is a *Hurwitz*integral quaternion if 2 ​ a, 2 ​ b, 2 ​ c, 2 ​ d 2a,2b,2c,2d are all integers of the same parity. Hurwitz integral quaternions form a left Euclidean ring 𝔼 \BE. The ring of quaternions with integral coefficients is denoted by 𝕃 \BL (these are the *Lipschitz*integral quaternions). The sign α | β \alpha\mid\beta means: α \alpha divides β \beta on the left in 𝔼 \BE. The ring 𝔼 \BE has 24 24 units. Every element α \alpha of 𝔼 \BE has a left associate in 𝕃 \BL and a right associate in 𝕃 \BL.

###### Theorem 2.1 ( [3], Theorem 2.7; see Theorem 377 of [4] and the note after the proof of Theorem 3 in Section 5.3 of [1]).

An integral quaternion is irreducible in the ring 𝔼 \BE if and only if its norm is a prime in ℤ \BZ. The only elements of 𝔼 \BE whose norm is 2 2 are 1 + i 1+i and its left associates. If p > 2 p>2 is a prime in ℤ \BZ, then there exist exactly 24 ​ ( p + 1) 24(p+1) integral quaternions whose norm is p p.

###### Lemma 2.2 ( [3], Lemma 2.5).

Suppose that α ∈ 𝔼 \alpha\in\BE and p ∈ ℤ p\in\BZ is a prime such that p | N ⁡ ( α) p\mid\Norm(\alpha) but p p does not divide α \alpha. Then α \alpha can be written as π ​ α ′ \pi\alpha^{\prime} where N ⁡ ( π) = p \Norm(\pi)=p, and this π \pi is uniquely determined up to right association.

###### Lemma 2.3 ( [3], Lemma 2.6).

Suppose that θ, η, π ∈ 𝔼 \theta,\eta,\pi\in\BE such that N ⁡ ( π) = p \Norm(\pi)=p is a prime in ℤ \BZ. If π | θ \pi\mid\theta, p | θ ¯ ​ η p\mid\overline{\theta}\eta but p p does not divide θ \theta, then π | η \pi\mid\eta.

We shall reduce questions to quaternions having odd norm, using the following assertion.

###### Claim 2.4.

Let α = a + b ​ i + c ​ j + d ​ k ∈ 𝕃 \alpha=a+bi+cj+dk\in\BL.

1. ( 1) (1)

There exists an element β ∈ 𝕃 \beta\in\BL such that α = ( 1 + i) ​ β \alpha=(1+i)\beta if and only if a ≡ b ⁡ ( 2) a\equiv b~(2) and c ≡ d ⁡ ( 2) c\equiv d~(2). The analogous statements hold for 1 + j 1+j and 1 + k 1+k.

2. ( 2) (2)

If 8 | N ⁡ ( α) 8\mid\Norm(\alpha), then each coefficient of α \alpha is even.

3. ( 3) (3)

If N ⁡ ( α) ≡ 4 ​ ( 8) \Norm(\alpha)\equiv 4~(8), then α = ( 1 + i) ​ β \alpha=(1+i)\beta for some β ∈ 𝕃 \beta\in\BL.

4. ( 4) (4)

If N ⁡ ( α) ≡ 2 ​ ( 4) \Norm(\alpha)\equiv 2~(4), then there is exactly one element η ∈ { 1 + i, 1 + j, 1 + k } \eta\in\{1+i,1+j,1+k\} such that α = η ​ β \alpha=\eta\beta for some β ∈ 𝕃 \beta\in\BL.

###### Proof.

( 1) (1) can be shown by direct calculation. Since m 2 ≡ 1 ​ ( 8) m^{2}\equiv 1~(8) for every odd integer m m, we see that N ⁡ ( α) \Norm(\alpha) is divisible by 8 8 if and only if a a, b b, c c, d d are all even, so ( 2) (2) holds. By the same argument, if 4 | N ⁡ ( α) 4\mid\Norm(\alpha), then a a, b b, c c, d d are all even, or are all odd. In the first case we have ( 3) (3), since 2 = ( 1 + i) ​ ( 1 − i) 2=(1+i)(1-i). In the second case ( 3) (3) also holds by ( 1) (1). Now suppose that N ⁡ ( α) ≡ 2 ​ ( 4) \Norm(\alpha)\equiv 2~(4). Then two numbers of a a, b b, c c, d d are even and two are odd. If a ≡ b ⁡ ( 2) a\equiv b~(2), then c ≡ d ⁡ ( 2) c\equiv d~(2), so ( 1) (1) shows that ( 1 + i) (1+i) can be pulled out from α \alpha, but 1 + j 1+j and 1 + k 1+k cannot. ∎

Next we investigate quaternions with integral coefficients having odd norm. Let K = { 1, i, j, k } K=\{1,i,j,k\}, and write a general quaternion α ∈ 𝕃 \alpha\in\BL as a 1 + a i ​ i + a j ​ j + a k ​ k a_{1}+a_{i}i+a_{j}j+a_{k}k. For g ∈ K g\in K define

 | S g = { a 1 + a i i + a j j + a k k ∈ 𝕃 ∣ a g ≢ a h ​ ( 2) for every h ≠ g, where h ∈ K }. S_{g}=\{a_{1}+a_{i}i+a_{j}j+a_{k}k\in\BL\mid\penalty\text{$a_{g}\not\equiv a_{h}~(2)$ for every $h\neq g$, where $h\in K$}\}\,. |  |

So for example the elements of S i S_{i} are those where the coefficient of i i is odd and the other coefficients are even, or vice versa. Let ∗ *denote the Klein-group multiplication on K K (which is quaternion-multiplication, but disregards the signs). Call two nonzero quaternions *twins*if so are the vectors formed by their coefficients. The following claim summarizes well-known, easy facts.

###### Claim 2.5.

Let α, β ∈ 𝕃 \alpha,\beta\in\BL with odd norm and 2 ​ σ = 1 + i + j + k 2\sigma=1+i+j+k.

1. ( 1) (1)

Both α \alpha and β \beta belong to exactly one of the sets S g S_{g}. If they are twins, then they cannot belong to the same S g S_{g}.

2. ( 2) (2)

If N ⁡ ( α) ≡ 1 ​ ( 4) \Norm(\alpha)\equiv 1~(4) then α ∈ S g \alpha\in S_{g} if and only if α ≡ g ⁡ ( 2) \alpha\equiv g~(2) in 𝕃 \BL if and only if α ≡ g ⁡ ( 2) \alpha\equiv g~(2) in 𝔼 \BE.

3. ( 3) (3)

If N ⁡ ( α) ≡ 3 ​ ( 4) \Norm(\alpha)\equiv 3~(4), then α ∈ S g \alpha\in S_{g} if and only if α ≡ 2 ​ σ − g ⁡ ( 2) \alpha\equiv 2\sigma-g~(2) in 𝕃 \BL if and only if α ≡ 2 ​ σ − g ⁡ ( 2) \alpha\equiv 2\sigma-g~(2) in 𝔼 \BE.

4. ( 4) (4)

If α ∈ S g \alpha\in S_{g} and β ∈ S h \beta\in S_{h}, then α ​ β ∈ S g ∗ h \alpha\beta\in S_{g*h}.

5. ( 5) (5)

If α ∈ S 1 \alpha\in S_{1} and γ ∈ 𝔼 \gamma\in\BE, then γ ∈ S g ⇔ α ​ γ ∈ S g ⇔ γ ​ α ∈ S g \gamma\in S_{g}\iff\alpha\gamma\in S_{g}\iff\gamma\alpha\in S_{g}.

###### Proof.

If N ⁡ ( α) ≡ 1 ​ ( 4) \Norm(\alpha)\equiv 1~(4), then α \alpha has exactly one odd component. If N ⁡ ( α) ≡ 3 ​ ( 4) \Norm(\alpha)\equiv 3~(4), then α \alpha has exactly one even component. Suppose that α \alpha and β \beta are twins in S g S_{g}. Then N ⁡ ( α) = N ⁡ ( β) ≡ 1 ​ ( 4) \Norm(\alpha)=\Norm(\beta)\equiv 1~(4) implies that the scalar product of the corresponding vectors is congruent to 1 1 modulo 2 2, which is impossible, since they are orthogonal. If N ⁡ ( α) = N ⁡ ( β) ≡ 3 ​ ( 4) \Norm(\alpha)=\Norm(\beta)\equiv 3~(4), then this scalar product is congruent to 3 3 modulo 2 2, also a contradiction. This shows ( 1) (1). The proofs of ( 2) − ( 4) (2)-(4) are left to the reader.

Suppose that α ∈ S 1 \alpha\in S_{1} and α ​ γ = δ ∈ S g \alpha\gamma=\delta\in S_{g}. Then N ⁡ ( α) ​ γ = α ¯ ​ δ ∈ 𝕃 \Norm(\alpha)\gamma=\overline{\alpha}\delta\in\BL. Since N ⁡ ( α) \Norm(\alpha) is odd, this implies that γ ∈ 𝕃 \gamma\in\BL. The norm of γ \gamma is odd, so ( 5) (5) follows from ( 4) (4). ∎

Call a quaternion α \alpha*primary*if α ∈ S 1 \alpha\in S_{1} and a 1 + a i + a j + a k ≡ 1 ​ ( 4) a_{1}+a_{i}+a_{j}+a_{k}\equiv 1~(4). Obviously, if α ∈ S 1 \alpha\in S_{1}, then exactly one of α \alpha and − α -\alpha is primary.

###### Claim 2.6.

The following hold.

1. ( 1) (1)

If γ ∈ 𝔼 \gamma\in\BE has odd norm, then γ \gamma has exactly one primary left associate, and exactly one primary right associate.

2. ( 2) (2)

The primary quaternions form a semigroup under multiplication. Moreover, if the (left or right) quotient of two primary quaternions is in 𝔼 \BE, then it is also primary.

3. ( 3) (3)

Let α \alpha be a primary quaternion and ε ∈ 𝔼 \varepsilon\in\BE a unit. Then ε ​ α ∈ 𝕃 \varepsilon\alpha\in\BL (or α ​ ε ∈ 𝕃 \alpha\varepsilon\in\BL) if and only if ε ∈ Q = { ± 1, ± i, ± j, ± k } \varepsilon\in Q=\{\pm 1,\pm i,\pm j,\pm k\}.

###### Proof.

Statement ( 3) (3) clearly follows from Claim 2.5 ( 5) (5). The rest of the proof is left to the reader. ∎

We close this section with two counting results. Call a quaternion with integral coefficients *primitive*, if its coefficients are relatively prime.

###### Claim 2.7 (Jacobi).

Let N > 1 N>1 be odd. Then the number of primary primitive quaternions with norm N N is h ⁡ ( N) = N ​ ∏ p ( 1 + ( 1 / p)) h(N)=N\prod_{p}\big(1+(1/p)\big), where p p runs over the prime divisors of N N.

A *pure*quaternion is one with real part zero.

###### Lemma 2.8 (see [3], Theorem 4.2).

Let θ ∈ 𝔼 \theta\in\BE be a primitive pure quaternion whose norm is a square. Then θ \theta can be written as γ ​ i ​ γ ¯ \gamma\,i\,\overline{\gamma} for some γ ∈ 𝔼 \gamma\in\BE. Here γ \gamma is uniquely determined in the sense that any two such elements γ \gamma are right associates via a unit in { 1, − 1, i, − i } \{1,-1,i,-i\}.

###### Claim 2.9.

Let N > 1 N>1 be odd. Then the number of primary quaternions γ \gamma with norm N N such that γ ​ i ​ γ ¯ \gamma\,i\,\overline{\gamma} is primitive is q ⁡ ( N) = N ​ ∏ p ( 1 − ( s p / p)) q(N)=N\prod_{p}\big(1-(s_{p}/p)\big), where p p runs over the prime divisors of N N and s p ∈ { 1, − 1 } s_{p}\in\{1,-1\} is congruent to p p modulo 4 4.

(In other words, s p = ( − 1) ( p − 1) / 2 = ( − 1 / p) s_{p}=(-1)^{(p-1)/2}=(-1/p) as a Legendre-symbol).

###### Proof.

Theorem 4.8 in [3] implies that the number of primitive vectors ( x, y, z) (x,y,z) with norm N 2 N^{2} is 6 ​ q ​ ( N) 6q(N). By Lemma 2.8, the quaternions corresponding to such vectors can be written as θ = γ ​ i ​ γ ¯ \theta=\gamma\,i\,\overline{\gamma} for some γ ∈ 𝔼 \gamma\in\BE. Conjugacy with the units in 𝔼 \BE yields an equivalence relation on the set of all such elements θ \theta. The fact that θ \theta is primitive, but not a unit implies that at least two of its components are nonzero. Therefore each conjugacy class has 12 12 elements (the stabilizer is just { 1, − 1 } \{1,-1\} in each case). It is sufficient to show that exactly two of these conjugates can be written in the form γ ​ i ​ γ ¯ \gamma\,i\,\overline{\gamma} such that γ \gamma is primary.

If θ = γ ​ i ​ γ ¯ \theta=\gamma\,i\,\overline{\gamma}, then Claim 2.6 shows that γ = ε ​ α \gamma=\varepsilon\alpha, where ε \varepsilon is a unit and α \alpha is primary. Therefore θ \theta has a conjugate of the required form, namely α ​ i ​ α ¯ \alpha\,i\,\overline{\alpha}. Exactly one of β = ± i ​ α ​ i ¯ \beta=\pm i\alpha\overline{i} is primary, and β ​ i ​ β ¯ = i ​ θ ​ i ¯ \beta\,i\,\overline{\beta}=i\theta\overline{i} is a conjugate of θ \theta that is different from θ \theta.

Conversely, suppose that θ \theta has two conjugates θ 1 = γ 1 ​ i ​ γ 1 ¯ \theta_{1}=\gamma_{1}\,i\,\overline{\gamma_{1}} and θ 2 = γ 2 ​ i ​ γ 2 ¯ \theta_{2}=\gamma_{2}\,i\,\overline{\gamma_{2}} such that γ 1 \gamma_{1} and γ 2 \gamma_{2} are primary. Thus θ 2 = ε ​ θ 1 ​ ε ¯ \theta_{2}=\varepsilon\theta_{1}\overline{\varepsilon} for some unit ε \varepsilon. By the uniqueness statement of Lemma 2.8, ε ​ γ 1 = γ 2 ​ ρ \varepsilon\gamma_{1}=\gamma_{2}\rho for some ρ ∈ { 1, − 1, i, − i } \rho\in\{1,-1,i,-i\}. Claim 2.6 shows that ε ∈ Q \varepsilon\in Q, and Claim 2.5 ( 5) (5) gives that ε = ± ρ \varepsilon=\pm\rho. If ε = ± 1 \varepsilon=\pm 1, then θ 1 = θ 2 \theta_{1}=\theta_{2}. If ε = ± i \varepsilon=\pm i, then θ 2 = i ​ θ 1 ​ i ¯ \theta_{2}=i\theta_{1}\overline{i}. ∎

There is an alternative argument for the previous statement: the reader may go through the proof of Theorem 4.8 in [3], and modify it in such a way that only primary prime factors are used when building γ \gamma.

## 3. Construction and extension

We shall speak about m m -icubes ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}) in 𝔼 \BE and in 𝕃 \BL, meaning that this is a sequence of simultaneous twins such that each α ℓ \alpha_{\ell} lies in 𝔼 \BE or in 𝕃 \BL, respectively.

###### Lemma 3.1.

The quaternions α \alpha and β \beta are twins if and only if their norms are equal, and α ¯ ​ β = − β ¯ ​ α \overline{\alpha}\beta=-\overline{\beta}\alpha (or equivalently, α ​ β ¯ = − β ​ α ¯ \alpha\overline{\beta}=-\beta\overline{\alpha}) holds.

###### Proof.

If α = a 1 + a i ​ i + a j ​ j + a k ​ k \alpha=a_{1}+a_{i}i+a_{j}j+a_{k}k and β = b 1 + b i ​ i + b j ​ j + b k ​ k \beta=b_{1}+b_{i}i+b_{j}j+b_{k}k, then the real part of α ​ β \alpha\beta is a 1 ​ b 1 − a i ​ b i − a j ​ b j − a k ​ b k a_{1}b_{1}-a_{i}b_{i}-a_{j}b_{j}-a_{k}b_{k}. Therefore the vectors corresponding to α \alpha and β \beta are orthogonal if and only if the real part of α ​ β ¯ \alpha\overline{\beta} is zero (if and only if the real part of α ¯ ​ β \overline{\alpha}\beta is zero). However, the real part of a quaternion is zero if and only if its conjugate is its negative. ∎

###### Corollary 3.2.

If γ ≠ 0 \gamma\neq 0, then α \alpha and β \beta are twins if and only if α ​ γ \alpha\gamma and β ​ γ \beta\gamma are twins if and only if γ ​ α \gamma\alpha and γ ​ β \gamma\beta are twins.∎

###### Lemma 3.3.

Let α, β ∈ 𝔼 \alpha,\beta\in\BE be twins and p ∈ ℤ p\in\BZ be a prime dividing N ⁡ ( α) = N ⁡ ( β) \Norm(\alpha)=\Norm(\beta). Then there exists a quaternion π ∈ 𝔼 \pi\in\BE with norm p p such that either π \pi divides both α \alpha and β \beta on the left, or π \pi divides both α \alpha and β \beta on the right. If β ​ α ¯ \beta\overline{\alpha} is divisible by p p, then the second case surely holds.

###### Proof.

If p | α p\mid\alpha, then every π ∈ 𝔼 \pi\in\BE with norm p p divides α \alpha both on the left and on the right, since p = π ​ π ¯ = π ¯ ​ π p=\pi\overline{\pi}=\overline{\pi}\pi (and such an element exists by Theorem 2.1). If α \alpha is not divisible by p p, then Lemma 2.2 yields a left divisor π 1 ∈ 𝔼 \pi_{1}\in\BE with norm p p. Applying this lemma to α ¯ \overline{\alpha} we get a right divisor π 2 \pi_{2} of α \alpha with norm p p. Similarly, β \beta has a left divisor π 3 \pi_{3} and a right divisor π 4 \pi_{4} of norm p p. We also see that if α \alpha or β \beta is divisible by p p, then π 1 = π 3 \pi_{1}=\pi_{3}*and*π 2 = π 4 \pi_{2}=\pi_{4} can be achieved, so the statement of the lemma holds both on the left and on the right.

Thus we can assume that α \alpha and β \beta are not divisible by p p. By Lemma 3.1, we have α ​ β ¯ = − β ​ α ¯ \alpha\overline{\beta}=-\beta\overline{\alpha}. Suppose first that this quaternion is not divisible by p p. The uniqueness statement of Lemma 2.2 can be applied to α ​ β ¯ = − β ​ α ¯ \alpha\overline{\beta}=-\beta\overline{\alpha}, so π 1 \pi_{1} and π 3 \pi_{3} are right associates, and the statement of the lemma holds on the left.

If α ​ β ¯ = − β ​ α ¯ \alpha\overline{\beta}=-\beta\overline{\alpha} is divisible by p p, then apply Lemma 2.3 to π = π 2 ¯ \pi=\overline{\pi_{2}}, θ = α ¯ \theta=\overline{\alpha}, η = β ¯ \eta=\overline{\beta}. We get that π 2 ¯ | β ¯ \overline{\pi_{2}}\mid\overline{\beta}, so π 2 \pi_{2} is a right divisor of β \beta, too, and the statement of the lemma holds on the right. ∎

###### Lemma 3.4.

Let α 1, …, α m ∈ 𝔼 \alpha_{1},\ldots,\alpha_{m}\in\BE be pairwise twins and p ∈ ℤ p\in\BZ a prime dividing their common norm. Then there exists a quaternion π ∈ 𝔼 \pi\in\BE with norm p p such that either π \pi divides every α ℓ \alpha_{\ell} on the left, or π \pi divides every α ℓ \alpha_{\ell} on the right.

###### Proof.

Lemma 2.2 yields a left divisor π ℓ \pi_{\ell} of α ℓ \alpha_{\ell} and a right divisor ρ ℓ \rho_{\ell} of α ℓ \alpha_{\ell} with norm p p. If p p does not divide α ℓ \alpha_{\ell}, then π ℓ \pi_{\ell} and ρ ℓ \rho_{\ell} are essentially unique, otherwise they can be chosen arbitrarily. Thus we can disregard those α ℓ \alpha_{\ell} that are divisible by p p, and can assume (to simplify notation) that no α ℓ \alpha_{\ell} is divisible by p p.

Consider the complete graph on { 1, 2, …, m } \{1,2,\ldots,m\}. Color the edge { u, v } \{u,v\} to Lilac if π u \pi_{u} and π v \pi_{v} are right associates, and to Red if ρ u \rho_{u} and ρ v \rho_{v} are left associates (any edge can carry both colors). The previous lemma shows that every edge has a color. By uniqueness, the lilac edges, as well as the red edges yield a transitive relation. This implies by an elementary graph-theoretic argument that either every edge is lilac, or every edge is red. ∎

Recall that Q = { ± 1, ± i, ± j, ± k } Q=\{\pm 1,\pm i,\pm j,\pm k\}. We characterize icubes in 𝔼 \BE first.

###### Theorem 3.5.

Let ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}) be an m m -icube ∈ 𝔼 \in\BE. Then there exist γ, δ ∈ 𝔼 \gamma,\delta\in\BE and an m m -icube ( ε 1, …, ε m) ∈ Q m (\varepsilon_{1},\ldots,\varepsilon_{m})\in Q^{m} such that ε 1 = 1 \varepsilon_{1}=1 and α ℓ = γ ​ ε ℓ ​ δ \alpha_{\ell}=\gamma\varepsilon_{\ell}\delta for every 1 ≤ ℓ ≤ m 1\leq\ell\leq m. Conversely, every such ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) (\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta) is an m m -icube in 𝔼 \BE.

###### Proof.

Corollary 3.2 implies that ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) (\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta) is an m m -icube. Conversely, suppose that C = ( α 1, …, α m) C=(\alpha_{1},\ldots,\alpha_{m}) is an m m -icube in 𝔼 \BE. Applying Lemma 3.4 and Corollary 3.2 several times successively we see that C = ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) C=(\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta) for some γ, δ ∈ 𝔼 \gamma,\delta\in\BE and units ε ℓ ∈ 𝔼 \varepsilon_{\ell}\in\BE. Replacing γ \gamma by γ ​ ε 1 \gamma\varepsilon_{1} we can assume that ε 1 = 1 \varepsilon_{1}=1. Then ( ε 1, …, ε m) (\varepsilon_{1},\ldots,\varepsilon_{m}) is an m m -icube by Corollary 3.2. Since 1 1 and ε ℓ \varepsilon_{\ell} are twins, the real part of each ε ℓ \varepsilon_{\ell} is zero for ℓ ≥ 2 \ell\geq 2, and therefore ε ℓ \varepsilon_{\ell} has integer coefficients. ∎

To prove extension results we have to characterize icubes in 𝕃 \BL. To count them, we need uniqueness in the above decomposition. To achieve these ends we reduce the problem to quaternions with odd norm. The next statement is clear by Claim 2.4.

###### Claim 3.6.

Suppose that N = 2 n ​ D N=2^{n}D where n ≥ 2 n\geq 2 and D D is odd. Then every m m -icube ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}) in 𝕃 \BL with edge norm N N can be written uniquely as

 | ( ( 1 + i) n − 1 ​ β 1, …, ( 1 + i) n − 1 ​ β m), \big((1+i)^{n-1}\beta_{1},\ldots,(1+i)^{n-1}\beta_{m}\big)\,, |  |

where ( β 1, …, β m) (\beta_{1},\ldots,\beta_{m}) is also an m m -icube in 𝕃 \BL. Thus f m ​ ( N) = f m ​ ( 2 ​ D) f_{m}(N)=f_{m}(2D).∎

###### Claim 3.7.

Let N = 2 ​ D N=2D where D D is odd. Then every m m -icube ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}) in 𝕃 \BL with edge norm N N can be written uniquely as ( η ​ β 1, …, η ​ β m) (\eta\beta_{1},\ldots,\eta\beta_{m}), where ( β 1, …, β m) (\beta_{1},\ldots,\beta_{m}) is an m m -icube in 𝕃 \BL and η ∈ { 1 + i, 1 + j, 1 + k } \eta\in\{1+i,1+j,1+k\}. Therefore f m ​ ( N) = 3 ​ f m ​ ( D) f_{m}(N)=3f_{m}(D).

###### Proof.

By the proof of Claim 2.4 we see that exactly two of the components of every α ℓ \alpha_{\ell} are even. Since the vectors corresponding to α 1, …, α m \alpha_{1},\ldots,\alpha_{m} are pairwise orthogonal, looking at the scalar products modulo 2 2 we see that these two-element subsets of the indices are either equal or disjoint. Thus ( 1) (1) of Claim 2.4 shows that the same element of { 1 + i, 1 + j, 1 + k } \{1+i,1+j,1+k\} can be pulled out of each α i \alpha_{i} on the left. This shows that every m m -icube of edge norm D D yields exactly three m m -icubes of edge norm 2 ​ D 2D. ∎

To each m m -icube ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}) with odd edge norm assign the unique sequence ( g 1, …, g m) (g_{1},\ldots,g_{m}) with the property that α ℓ ∈ S g ℓ \alpha_{\ell}\in S_{g_{\ell}} for every 1 ≤ ℓ ≤ m 1\leq\ell\leq m (see Claim 2.5). This sequence is called the *type*of ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}). By Claim 2.5 (1), the elements g ℓ ∈ K g_{\ell}\in K are pairwise different. Call an m m -icube ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m})*orderly*, if its type is ( 1) (1) or ( 1, i) (1,i), or ( 1, i, j) (1,i,j), or ( 1, i, j, k) (1,i,j,k), depending on m m.

Permuting the components of vectors preserves norm as well as orthogonality. If ( g 1, …, g m) (g_{1},\ldots,g_{m}) and ( h 1, …, h m) (h_{1},\ldots,h_{m}) are types, then one can fix a permutation r r of K K that maps each h ℓ h_{\ell} to g ℓ g_{\ell}. This permutation induces a bijection on 𝕃 \BL:

 | α = a 1 + a i ​ i + a j ​ j + a k ​ k ↦ r ⁡ ( α) = a r ⁡ ( 1) + a r ⁡ ( i) ​ i + a r ⁡ ( j) ​ j + a r ⁡ ( k) ​ k. \alpha=a_{1}+a_{i}i+a_{j}j+a_{k}k\mapsto r(\alpha)=a_{r(1)}+a_{r(i)}i+a_{r(j)}j+a_{r(k)}k\,. |  |

If ( α 1, …, α m) (\alpha_{1},\ldots,\alpha_{m}) has type ( g 1, …, g m) (g_{1},\ldots,g_{m}), then ( r ⁡ ( α 1), …, r ⁡ ( α m)) \big(r(\alpha_{1}),\ldots,r(\alpha_{m})\big) has type ( h 1, …, h m) (h_{1},\ldots,h_{m}), so the number of m m -icubes of type ( g 1, …, g m) (g_{1},\ldots,g_{m}) does not depend on ( g 1, …, g m) (g_{1},\ldots,g_{m}). The number of possible types is 4 ⋅ 3 ⋅ … ⋅ ( 4 − m + 1) = 24 / ( 4 − m)! 4\cdot 3\cdot\ldots\cdot(4-m+1)=24/(4-m)!. Hence:

###### Claim 3.8.

Let N N be odd. Then f m ​ ( N) = 24 ​ M / ( 4 − m)! f_{m}(N)=24M/(4-m)!, where M M is the number of orderly m m -icubes with edge norm N N.∎

###### Theorem 3.9.

Let γ \gamma and δ ∈ 𝕃 \delta\in\BL be primary quaternions, and ε 1 = ± 1 \varepsilon_{1}=\pm 1, ε 2 = ± i \varepsilon_{2}=\pm i, ε 3 = ± j \varepsilon_{3}=\pm j and ε 4 = ± k \varepsilon_{4}=\pm k. Then ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) (\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta) is an orderly m m -icube in 𝕃 \BL. Conversely, every orderly m m -icube in 𝕃 \BL with odd edge norm can be obtained this way.

###### Proof.

Since γ \gamma and δ \delta are primary, ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) (\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta) is orderly by ( 4) (4) of Claim 2.5. Conversely, suppose that C C is an orderly m m -icube in 𝕃 \BL with odd edge norm. Apply Lemma 3.4 successively, but in every step make sure that π \pi is primary (this can be done by Claim 2.6). Claim 2.5 ensures that after pulling out π \pi we get an orderly icube in 𝕃 \BL. Thus we get a representation C = ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) C=(\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta), where γ \gamma and δ \delta are primary. Since ( ε 1, …, ε m) (\varepsilon_{1},\ldots,\varepsilon_{m}) is orderly, ε 1 = ± 1 \varepsilon_{1}=\pm 1, ε 2 = ± i \varepsilon_{2}=\pm i, ε 3 = ± j \varepsilon_{3}=\pm j and ε 4 = ± k \varepsilon_{4}=\pm k. ∎

Now we prove the extension property (Theorem 1.2). Suppose that an m m -icube C C in 𝕃 \BL is given. Claims 3.6 and 3.7 show that we can write C C as ( η ​ β 1, …, η ​ β m) (\eta\beta_{1},\ldots,\eta\beta_{m}), where ( β 1, …, β m) (\beta_{1},\ldots,\beta_{m}) is an m m -icube in 𝕃 \BL with odd edge norm. By rearranging the coordinates of the vectors we get an m m -icube of the form ( γ ​ ε 1 ​ δ, …, γ ​ ε m ​ δ) (\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m}\delta) by Theorem 3.9. This clearly extends to an m + 1 m+1 -icube ( γ ​ ε 1 ​ δ, …, γ ​ ε m + 1 ​ δ) (\gamma\varepsilon_{1}\delta,\ldots,\gamma\varepsilon_{m+1}\delta). Permuting the coordinates back, and then multiplying by η \eta we get the desired extension of C C.

## 4. Counting

To deal with the case m = 3 m=3 and m = 4 m=4 we prove uniqueness in Theorem 3.9. We keep the notation that ε 1 = ± 1 \varepsilon_{1}=\pm 1, ε 2 = ± i \varepsilon_{2}=\pm i, ε 3 = ± j \varepsilon_{3}=\pm j and ε 4 = ± k \varepsilon_{4}=\pm k.

###### Lemma 4.1.

Suppose that γ 1 ​ ε ℓ ​ δ 1 = γ 2 ​ ε ℓ ​ δ 2 \gamma_{1}\varepsilon_{\ell}\delta_{1}=\gamma_{2}\varepsilon_{\ell}\delta_{2} for ℓ = u, v \ell=u,v and N ⁡ ( γ 1 ​ δ 1) = N ⁡ ( γ 2 ​ δ 2) ≠ 0 \Norm(\gamma_{1}\delta_{1})=\Norm(\gamma_{2}\delta_{2})\neq 0. Then γ 1 ¯ ​ γ 2 \overline{\gamma_{1}}\gamma_{2} permutes with ε u ​ ε v ¯ \varepsilon_{u}\overline{\varepsilon_{v}}.

###### Proof.

Multiply the first equation by the conjugate of the second. We obtain that N ⁡ ( δ 1) ​ γ 1 ​ ε u ​ ε v ¯ ​ γ 1 ¯ = N ⁡ ( δ 2) ​ γ 2 ​ ε u ​ ε v ¯ ​ γ 2 ¯ \Norm(\delta_{1})\gamma_{1}\varepsilon_{u}\overline{\varepsilon_{v}}\;\overline{\gamma_{1}}=\Norm(\delta_{2})\gamma_{2}\varepsilon_{u}\overline{\varepsilon_{v}}\;\overline{\gamma_{2}}. Now multiply on the left by γ 1 ¯ \overline{\gamma_{1}} and on the right by γ 2 \gamma_{2}, and then simplify by N ⁡ ( γ 1 ​ δ 1) = N ⁡ ( γ 2 ​ δ 2) \Norm(\gamma_{1}\delta_{1})=\Norm(\gamma_{2}\delta_{2}). ∎

An m m -icube is called *primitive*, if the 4 ​ m 4m components of its m m vectors have no common divisor other than ± 1 \pm 1.

###### Theorem 4.2.

Suppose that m ≥ 3 m\geq 3 and ( γ 1 ​ ε 1 ​ δ 1, …, γ 1 ​ ε m ​ δ 1) = ( γ 2 ​ ε 1 ​ δ 2, …, γ 2 ​ ε m ​ δ 2) (\gamma_{1}\varepsilon_{1}\delta_{1},\ldots,\gamma_{1}\varepsilon_{m}\delta_{1})=(\gamma_{2}\varepsilon_{1}\delta_{2},\ldots,\gamma_{2}\varepsilon_{m}\delta_{2}) are two representations of an icube given by Theorem 3.9, where γ 1 \gamma_{1} and γ 2 \gamma_{2} are primitive. Then γ 1 = γ 2 \gamma_{1}=\gamma_{2} and δ 1 = δ 2 \delta_{1}=\delta_{2}. Furthermore, such an icube ( γ 1 ​ ε 1 ​ δ 1, …, γ 1 ​ ε m ​ δ 1) (\gamma_{1}\varepsilon_{1}\delta_{1},\ldots,\gamma_{1}\varepsilon_{m}\delta_{1}) is primitive if and only if γ 1 \gamma_{1} and δ 1 \delta_{1} are both primitive.

###### Proof.

Lemma 4.1 shows that γ 1 ¯ ​ γ 2 \overline{\gamma_{1}}\gamma_{2} permutes with ε 1 ​ ε 2 ¯ = ± i \varepsilon_{1}\overline{\varepsilon_{2}}=\pm i and with ε 1 ​ ε 3 ¯ = ± j \varepsilon_{1}\overline{\varepsilon_{3}}=\pm j. Therefore d = γ 1 ¯ ​ γ 2 d=\overline{\gamma_{1}}\gamma_{2} is a real number. As γ 1 \gamma_{1} and γ 2 \gamma_{2} are primary, d ∈ ℤ d\in\BZ. We have d ​ γ 1 = N ⁡ ( γ 1) ​ γ 2 d\gamma_{1}=\Norm(\gamma_{1})\gamma_{2}. Since γ 1 \gamma_{1} and γ 2 \gamma_{2} are primitive, the gcd of the coefficients of the two sides of this equation is N ⁡ ( γ 1) = ± d \Norm(\gamma_{1})=\pm d. Therefore γ 2 = ± γ 1 \gamma_{2}=\pm\gamma_{1}. Since they are primary, they are equal. Then γ 1 ​ ε 1 ​ δ 1 = γ 2 ​ ε 1 ​ δ 2 \gamma_{1}\varepsilon_{1}\delta_{1}=\gamma_{2}\varepsilon_{1}\delta_{2} yields δ 1 = δ 2 \delta_{1}=\delta_{2}.

Now let C = ( γ 1 ​ ε 1 ​ δ 1, …, γ 1 ​ ε m ​ δ 1) C=(\gamma_{1}\varepsilon_{1}\delta_{1},\ldots,\gamma_{1}\varepsilon_{m}\delta_{1}) such that γ 1 \gamma_{1} and δ 1 \delta_{1} are primitive and assume to get a contradiction that C C is not primitive. Write C C as c ​ C ′ cC^{\prime}, where c > 1 c>1 and C ′ C^{\prime} is a primitive m m -icube. Then C ′ C^{\prime} can be represented as ( γ 3 ​ ε 1 ​ δ 3, …, γ 3 ​ ε m ​ δ 3) (\gamma_{3}\varepsilon_{1}\delta_{3},\ldots,\gamma_{3}\varepsilon_{m}\delta_{3}), where γ 3 \gamma_{3} must be primitive, so C C has a representation C = ( γ 3 ​ ε 1 ​ ( c ​ δ 3), …, γ 3 ​ ε m ​ ( c ​ δ 3)) C=\big(\gamma_{3}\varepsilon_{1}(c\delta_{3}),\ldots,\gamma_{3}\varepsilon_{m}(c\delta_{3})\big). Here c ​ δ 3 c\delta_{3} is also primary, since c c is a positive odd integer. The uniqueness statement proved in the previous paragraph shows that δ 1 = c ​ δ 3 \delta_{1}=c\delta_{3}, contradicting the assumption that δ 1 \delta_{1} is primitive. ∎

###### Corollary 4.3.

Suppose that m ≥ 3 m\geq 3 and N N is an odd integer. Then the number of orderly, primitive m m -icubes with edge norm N N is

 | k ⁡ ( N) = 2 m ​ ∑ d | N h ⁡ ( d) ​ h ​ ( N / d). k(N)=2^{m}\sum_{d\mid N}h(d)h(N/d)\,. |  |

Here h ⁡ ( d) = d ​ ∏ p ( 1 + ( 1 / p)) h(d)=d\prod_{p}\big(1+(1/p)\big), where p p runs over the prime divisors of d d.

###### Proof.

Recall that h ⁡ ( d) h(d) is the number of primitive, primary quaternions with norm d d by Claim 2.7. Consider the unique representation given by Theorem 4.2, and let d = N ⁡ ( γ 1) d=\Norm(\gamma_{1}). Then N ⁡ ( δ 1) = N / d \Norm(\delta_{1})=N/d. These two quaternions can be chosen h ⁡ ( d) ​ h ​ ( N / d) h(d)h(N/d) ways, and d d can be any divisor of N N. Finally, there are 2 m 2^{m} possibilities to chose the signs of ε 1, …, ε m \varepsilon_{1},\ldots,\varepsilon_{m}. ∎

We can now compute f 4 f_{4} as stated in Theorem 1.3. Fix m = 4 m=4 and write N = 2 n ​ D N=2^{n}D, where D D is odd. By Claims 3.6 and 3.7 we have that f 4 ​ ( N) = 3 ​ f 4 ​ ( D) f_{4}(N)=3f_{4}(D) if n ≥ 1 n\geq 1. Next Claim 3.8 shows that f 4 ​ ( D) = 24 ​ M f_{4}(D)=24M, where M M is the number of orderly m m -icubes with edge norm D D. Finally, each orderly m m -icube can be written uniquely as C = c ​ C ′ C=cC^{\prime}, where c c is a positive integer and C ′ C^{\prime} is primitive. Clearly, c | D 2 c\mid D^{2}, and therefore

 | M = ∑ c 2 | N k ⁡ ( N / c 2), M=\sum_{c^{2}\mid N}k(N/c^{2})\,, |  |

where k k is the function defined in Corollary 4.3 for m = 4 m=4. Thus

 | f 4 ​ ( D) = ( 16 ⋅ 24) ​ ∑ c 2 | N ∑ d | ( N / c 2) h ⁡ ( d) ​ h ​ ( N / ( c 2 ​ d)). f_{4}(D)=(16\cdot 24)\sum_{c^{2}\mid N}\sum_{d\,\mid\,(N/c^{2})}h(d)h\big(N/(c^{2}d)\big)\,. |  |

It is a well-known fact that the convolution of multiplicative functions is multiplicative. Since h h is obviously multiplicative, so is k / 16 k/16, which is the convolution of h h by itself. The function assigning 1 1 to squares and 0 0 to all other integers is also multiplicative, so the double sum above (which is f 4 ​ ( D) / 384 f_{4}(D)/384) is also multiplicative for odd values of D D. Finally the remarks at the beginning of this argument show that f 4 ​ ( N) / 384 f_{4}(N)/384 is multiplicative on the set of positive integers.

The proof above clearly shows that f 4 ​ ( 2 n) = 384 ⋅ 3 f_{4}(2^{n})=384\cdot 3 for n ≥ 1 n\geq 1. If p p is an odd prime, then it is a routine calculation to prove, using the last displayed formula, that the value of f 4 ​ ( p n) f_{4}(p^{n}) is the one given in ( 2) (2) of Theorem 1.3. This somewhat complicated summation is left to the reader.

To show that f 3 ​ ( N) = f 4 ​ ( N) / 2 f_{3}(N)=f_{4}(N)/2 one can either go through the argument above with m = 3 m=3, or invoke Theorem 1.1 (stating that each 3 3 -icube has exactly two extensions in dimension 4 4). To compute f 2 ​ ( N) f_{2}(N) we need to improve Theorem 3.9, since uniqueness does not hold for m = 2 m=2.

###### Theorem 4.4.

Every orderly 2 2 -icube in 𝕃 \BL with odd edge norm can be written in the from ( γ ​ ε 1 ​ δ, γ ​ ε 2 ​ δ) (\gamma\varepsilon_{1}\delta,\gamma\varepsilon_{2}\delta), where γ \gamma and δ ∈ 𝕃 \delta\in\BL are primary quaternions such that γ ​ i ​ γ ¯ \gamma\,i\,\overline{\gamma} is primitive and ε 1 = ± 1 \varepsilon_{1}=\pm 1, ε 2 = ± i \varepsilon_{2}=\pm i. Here γ \gamma and δ \delta are uniquely determined. Such an icube is primitive if and only if δ \delta is primitive as well.

###### Proof.

Theorem 3.9 yields a decomposition C = ( γ ​ ε 1 ​ δ, γ ​ ε 2 ​ δ) C=(\gamma\varepsilon_{1}\delta,\gamma\varepsilon_{2}\delta). Suppose that γ ​ i ​ γ ¯ \gamma\,i\,\overline{\gamma} is divisible by a prime p p. Apply Lemma 3.3 to α = γ \alpha=\gamma and β = γ ​ i \beta=\gamma i. We get that there is a primary π \pi with norm p p that divides both γ \gamma and γ ​ i \gamma i on the *right.*Let γ = γ 1 ​ π \gamma=\gamma_{1}\pi (so γ 1 \gamma_{1} is primary). Now γ ​ i = γ 1 ​ π ​ i \gamma i=\gamma_{1}\pi i is right divisible by π \pi, so the uniqueness statement of Lemma 2.2 shows that π ​ i = ε ​ π \pi i=\varepsilon\pi for some unit ε \varepsilon. As π \pi is primary, Claim 2.6 gives that ε ∈ Q \varepsilon\in Q, so ε ∈ S i \varepsilon\in S_{i} by Claim 2.5, that is, ε = ± i \varepsilon=\pm i. Therefore we can write C C as ( γ 1 ​ ε 1 ​ ( π ​ δ), γ 1 ​ ( ± ε 2) ​ ( π ​ δ)) \big(\gamma_{1}\varepsilon_{1}(\pi\delta),\gamma_{1}(\pm\varepsilon_{2})(\pi\delta)\big). Applying this several times we get a representation where γ ​ i ​ γ ¯ \gamma\,i\,\overline{\gamma} is primitive.

Suppose that C = ( α 1, α 2) = ( γ 1 ​ ε 1 ​ δ 1, γ 1 ​ ε 2 ​ δ 1) = ( γ 2 ​ ε 1 ​ δ 2, γ 2 ​ ε 2 ​ δ 2) C=(\alpha_{1},\alpha_{2})=(\gamma_{1}\varepsilon_{1}\delta_{1},\gamma_{1}\varepsilon_{2}\delta_{1})=(\gamma_{2}\varepsilon_{1}\delta_{2},\gamma_{2}\varepsilon_{2}\delta_{2}) are two representations such that γ ℓ ​ i ​ γ ℓ ¯ \gamma_{\ell}\,i\,\overline{\gamma_{\ell}} are both primitive. Then α 2 ​ α 1 ¯ = N ⁡ ( δ ℓ) ​ γ ℓ ​ ( ε 2 ​ ε 1 ¯) ​ γ ℓ ¯ \alpha_{2}\overline{\alpha_{1}}=\Norm(\delta_{\ell})\gamma_{\ell}(\varepsilon_{2}\overline{\varepsilon_{1}})\overline{\gamma_{\ell}}. Here ε 2 ​ ε 1 ¯ = ± i \varepsilon_{2}\overline{\varepsilon_{1}}=\pm i, and therefore this quaternion determines N ⁡ ( δ ℓ) \Norm(\delta_{\ell}) as the positive gcd of its coefficients. Thus N ⁡ ( δ 1) = N ⁡ ( δ 2) \Norm(\delta_{1})=\Norm(\delta_{2}) and γ 1 ​ i ​ γ 1 ¯ = γ 2 ​ i ​ γ 2 ¯ \gamma_{1}\,i\,\overline{\gamma_{1}}=\gamma_{2}\,i\,\overline{\gamma_{2}}. The uniqueness statement of Lemma 2.8 shows that γ 1 = γ 2 \gamma_{1}=\gamma_{2}, since both are primary. Thus δ 1 = δ 2 \delta_{1}=\delta_{2} as well. The uniqueness statement in the last sentence of the theorem can be proved exactly as in Theorem 4.2. ∎

###### Corollary 4.5.

Suppose that N N is an odd integer. Then the number of orderly, primitive 2 2 -icubes with edge norm N N is

 | k 2 ​ ( N) = 4 ​ ∑ d | N q ⁡ ( d) ​ h ​ ( N / d), k_{2}(N)=4\sum_{d\mid N}q(d)h(N/d)\,, |  |

where p p runs over the prime divisors of d d and the functions q q and h h are given by Claim 2.9 and Claim 2.7, respectively.

###### Proof.

Consider the unique representation given by Theorem 4.4, and let d = N ⁡ ( γ 1) d=\Norm(\gamma_{1}). Then N ⁡ ( δ 1) = N / d \Norm(\delta_{1})=N/d. These two quaternions can be chosen q ⁡ ( d) ​ h ​ ( N / d) q(d)h(N/d) ways by the claims quoted in the corollary, and d d can be any divisor of N N. Finally, there are 4 4 possibilities to chose the signs of ε 1 \varepsilon_{1} and ε 2 \varepsilon_{2}. ∎

To compute f 2 f_{2} as stated in Theorem 1.3 we mimic the argument presented above for f 4 f_{4}. The reduction to odd norm is the same, and if D D is odd, then we get that

 | f 2 ​ ( D) = ( 4 ⋅ 12) ​ ∑ c 2 | N ∑ d | ( N / c 2) q ⁡ ( d) ​ h ​ ( N / ( c 2 ​ d)). f_{2}(D)=(4\cdot 12)\sum_{c^{2}\mid N}\sum_{d\,\mid\,(N/c^{2})}q(d)h\big(N/(c^{2}d)\big)\,. |  |

Again, the details of the summation are left to the reader.

## References

- [1] J. H. Conway, D. A. Smith, *On Quaternions and Octonions: Their Geometry, Arithmetic and Symmetry*, A K Peters, 2003.
- [2] B. Eckmann, *Gruppentheoretischer Beweis des Satzes von Hurwitz-Radon über die Komposition quadratishcer Formen*, Comment. Math. Helvet. 15 (1943), 358-366.
- [3] L. M. Goswick, E. W. Kiss, G. Moussong, N. Simányi, *Sums of squares and orthogonal integral vectors*, Journal of Number Theory, to appear, see http://arxiv.org/abs/0806.3943.
- [4] G. H. Hardy, E. M. Wright, *An introduction to the theory of numbers, 5th Ed.*, Oxford, Clarendon Press, 1979.
- [5] A. Hurwitz, *Vorlesungen über die Zahlentheorie der Quaternionen*, Berlin, 1919.
- [6] A. Hurwitz, *Über die Komposition der quadratischen Formen*, Math. Ann. 88 (1923) 1-25.
- [7] J. Radon, *Lineare scharen orthogonale Matrizen*, Abh. Math. Sem. Univ. Hamburg 1 (1922), 1-14.
- [8] A. Sárközy, *On lattice-cubes in the three-space*(in Hungarian), Matematikai Lapok, 1961.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:ewkiss@math.elte.hu
[2]: mailto:kutasp@gmail.com
[3]: /html/1108.3112
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/1108.3113
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1108.3113
[9]: https://arxiv.org/abs/1108.3113
[10]: /html/1108.3114
