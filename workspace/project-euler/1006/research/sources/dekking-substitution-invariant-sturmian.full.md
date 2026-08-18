<!-- source: https://arxiv.org/html/1705.08607 | converted from HTML -->

Substitution invariant Sturmian words and binary trees

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1705.08607v1 [math.CO] 24 May 2017

# Substitution invariant Sturmian words and binary trees

Michel Dekking

Date: August 11, 2026

###### Abstract.

We take a global view at substitution invariant Sturmian sequences. We show that homogeneous substitution invariant Sturmian sequences s α, α s_{\alpha,\alpha} can be indexed by two binary trees, associated directly to Johannes Kepler’s tree of harmonic fractions from 1619. We obtain similar results for the inhomogeneous sequences s α, 1 − α s_{\alpha,1-\alpha} and s α, 0 s_{\alpha,0}.

Key words. Sturmian word; morphism; substitution; Sturm numbers; binary tree; harmonic fraction; Kepler.

Delft University of Technology,
Faculty EEMCS, P.O. Box 5031,
2600 GA Delft, The Netherlands.
Email: F.M.Dekking@math.tudelft.nl

## 1. Introduction

A Sturmian word w w is an infinite word w = w 1 ​ w 2 ​ … w=w_{1}w_{2}\dots, in which occur only n + 1 n+1 subwords of length n n for n = 0, 1, 2 ​ … n=0,1,2\dots. It is well known (see, e.g. [12]) that the Sturmian words w w can be directly derived from rotations on the circle as

(1) |  | w n = s α, ρ ( n) = [( n + 1) α + ρ] − [n α + ρ], n = 0, 1, 2, …. w_{n}=s_{\alpha,\rho}(n)=[(n+1)\alpha+\rho]-[n\alpha+\rho],\quad n=0,1,2,\dots. |  |

or as

(2) |  | w n = s α, ρ ′ ( n) = ⌈ ( n + 1) α + ρ ⌉ − ⌈ n α + ρ ⌉, n = 0, 1, 2, …. w_{n}=s^{\prime}_{\alpha,\rho}(n)=\lceil(n+1)\alpha+\rho\rceil-\lceil n\alpha+\rho\rceil,\quad n=0,1,2,\dots. |  |

Here 0 < α < 1 0<\alpha<1 and ρ \rho are real numbers, [⋅] [\cdot] is the floor function, and ⌈ ⋅ ⌉ \lceil\cdot\rceil is the ceiling function.

Sturmian words have been named after Jacques Charles François Sturm, who never studied them. A whole chapter is dedicated to them in Lothaire’s book ‘Algebraic combinatorics on words’ ( [12]). There is a huge literature, in particular on the *homogeneous*Sturmian words

 | c α:= s α, α, c_{\alpha}:=s_{\alpha,\alpha}, |  |

which have been studied since Johann III Bernoulli. The homogeneous Sturmian words are also known as *characteristic words*see Chapter 9 in [2].

Interestingly, for certain α \alpha and ρ \rho the Sturmian word w w is a fixed point σ ⁡ ( w) = w \sigma(w)=w of a morphism 1 1 1 We interchangeably use the terms morphisms and substitutions. σ \sigma of the monoid of words over the alphabet { 0, 1 } \{0,1\}. For example, for α = ρ = ( 3 − 5) / 2 \alpha=\rho=(3-\sqrt{5})/2 one obtains the Fibonacci word c α = 0100101 ​ … c_{\alpha}=0100101\dots, fixed point of the Fibonacci morphism φ \varphi given by φ ⁡ ( 0) = 01 \varphi(0)=01, φ ⁡ ( 1) = 0 \varphi(1)=0. Another example is the Pell word c α = 0010010001 ​ … c_{\alpha}=0010010001\dots obtained for α = ρ = ( 2 − 2) / 2 \alpha=\rho=(2-\sqrt{2})/2, with morphism given by 0 → 001, 1 → 0 0\rightarrow 001,\;1\rightarrow 0.

It is well known for which α \alpha one obtains a morphism invariant c α c_{\alpha}. This was first obtained in [11], and an extensive treatment can be found in [12, Section 2.3.6]. The result is that α ∈ ( 0, 1 2) \alpha\in(0,\tfrac{1}{2}) gives a fixed point if and only if there exists a natural number k k such that α \alpha has continued fraction expansion

(3) |  | α = [0; 1 + a 0, a 1 ​ … ​ a k ¯], a k ≥ a 0 ≥ 1, \alpha=[0;1+a_{0},\overline{a_{1}\dots a_{k}}],\qquad a_{k}\geq a_{0}\geq 1, |  |

and α ∈ ( 1 2, 1) \alpha\in(\tfrac{1}{2},1) gives a fixed point if and only if there exists a natural number k k such that α \alpha has continued fraction expansion

(4) |  | α = [0; 1, a 0, a 1 ​ … ​ a k ¯], a k ≥ a 0. \alpha=[0;1,a_{0},\overline{a_{1}\dots a_{k}}],\qquad a_{k}\geq a_{0}. |  |

The Fibonacci word is obtained for k = 1, a 0 = a 1 = 1 k=1,a_{0}=a_{1}=1, and the Pell word for k = 1, a 0 = 2, a 1 = 3 k=1,a_{0}=2,a_{1}=3.

Any α \alpha that gives a substitution invariant c α c_{\alpha} is called a *Sturm number*. In terms of their continued fraction expansions these are characterized in equations ( 3) and ( 4). There is however a simple algebraic way to describe them, given in [1]:

an irrational number α ∈ ( 0, 1) \alpha\in(0,1) is a Sturm number if and only if it is a quadratic irrational number whose algebraic conjugate α ¯ \overline{\alpha}, defined by the equation ( x − α) ​ ( x − α ¯) = 0 (x-\alpha)(x-\overline{\alpha})=0, satisfies

 | α ¯ ∉ [0, 1]. \overline{\alpha}\notin[0,1]. |  |

A simple manipulation shows that for α ∈ ( 0, 1 2) \alpha\in(0,\tfrac{1}{2}) the number β = 1 − α \beta=1-\alpha has an expansion as in equation ( 4) with the same k k and a j, j = 0, …, k a_{j},\,j=0,\dots,k. Moreover, the Sturmian word w ⁡ ( β) w(\beta) is equal to the word E ⁡ ( w ⁡ ( α)) E(w(\alpha)), where E E is the ‘exchange’ morphism

 | E: { 0 → 1 1 → 0. E:\;{\Big\{\begin{aligned} 0&\rightarrow 1\\[-2.84544pt] 1&\rightarrow 0\end{aligned}}\>. |  |

The latter is shown in the proof of Theorem 2.3.25 in [12]. Note that this implies that if σ \sigma generates w ⁡ ( α) w(\alpha), then E ​ σ ​ E E\sigma E generates w ⁡ ( 1 − α) w(1-\alpha). Because of this duality we will confine ourselves often to α \alpha with 0 < α < 1 2 0<\alpha<\tfrac{1}{2} in the sequel.

The first question we will consider is: what are the morphisms that leave a homogeneous Sturmian sequence c α c_{\alpha} invariant? The answer in [11] is: they are compositions of the infinitely many morphisms G k: 0 → 1 k ​ 0, 1 → 1 G_{k}:\;0\rightarrow 1^{k}0,\,1\rightarrow 1 and H k = G k ​ E H_{k}=G_{k}E. The answer in [2] is: they are compositions of the infinitely many morphisms h k: 0 → 0 k ​ 1, 1 → 0 → 0 k ​ 10 h_{k}:\;0\rightarrow 0^{k}1,\,1\rightarrow 0\rightarrow 0^{k}10 (actually only for α \alpha ’s with a purely periodic continued fraction expansion). See [19] for yet another infinite family of morphisms.

In the paper [9] the authors call the inhomogeneous sequence s α, 0 s_{\alpha,0} a characteristic sequence, and do actually derive a result close to our Theorem 3, using completely different techniques with continued fractions and extensive matrix multiplications.

More satisfactory is the answer in the book [12] or the paper [5], where only two generating morphisms are used, namely the exchange morphism E E and the morphism G G given by G ⁡ ( 0) =: 0, G ⁡ ( 1) = 01. G(0)=:0,\,G(1)=01. What we propose are also only two generators, which we denote by φ 0 \varphi_{0} and φ 1 \varphi_{1}, given by

 | φ 0: { 0 → 0 1 → 01 φ 1: { 0 → 01 1 → 0. \varphi_{0}:\;\Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 01\end{aligned}\qquad\varphi_{1}:\;\Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 0\end{aligned}\>. |  |

Note that φ 0 = G \varphi_{0}=G, and that φ 1 = G ​ E \varphi_{1}=GE, the Fibonacci morphism. Obviously, this proposal is very close to the one in [12], but what we gain is a natural way to index all the morphisms that leave homogeneous Sturmian words invariant by a binary tree (actually two binary trees, one for α ∈ ( 0, 1 2) \alpha\in(0,\tfrac{1}{2}), and a dual version for α ∈ ( 1 2, 1) \alpha\in(\tfrac{1}{2},1)). In Section 2.1 we treat some preliminaries to give in Section 2.2 our main result.

We remark that a similar tree associated to the rational numbers appears in the work of de Luca [13, 14]. The labeling there is not with morphisms, but with words.

The second question we will consider is: what are the substitution invariant Sturmian words that can only be obtained via the ceiling function, i.e., the Sturmian words that can only be obtained as in equation ( 2)? In this respect the homogeneous Sturmian words are regular, in that for all α \alpha

 | c α = s α, α = s α, α ′. c_{\alpha}=s_{\alpha,\alpha}=s^{\prime}_{\alpha,\alpha}. |  |

So these ‘strictly ceiling’ Sturmian words have to be sought among the inhomogeneous Sturmian words, what we do in Section 3.

The short Section 4 is more or less independent of the remainder of the paper, but its contents have been very useful in our research.

## 2. Homogeneous Sturmian words

### 2.1. The binary tree of harmonic fractions

The binary tree is a graph with 2 n 2^{n} nodes i 1 ​ … ​ i n i_{1}\dots i_{n} at level n n for n = 1, 2, … n=1,2,\dots, where the i k i_{k} are 0 or 1. At level 0 there is the root node Λ \Lambda.

1 2 \frac{1}{2} 1 3 \frac{1}{3} 1 4 \frac{1}{4} 1 5 \frac{1}{5} 4 5 \frac{4}{5} 3 4 \frac{3}{4} 3 7 \frac{3}{7} 4 7 \frac{4}{7} 2 3 \frac{2}{3} 2 5 \frac{2}{5} 2 7 \frac{2}{7} 5 7 \frac{5}{7} 3 5 \frac{3}{5} 3 8 \frac{3}{8} 5 8 \frac{5}{8}

As early as 1619 Johannes Kepler defined in [15] a binary tree with fractions p q \tfrac{p}{q} at the nodes. In the root there is 1 2 \tfrac{1}{2}, and if p q \tfrac{p}{q} is at a node, then the two children nodes receive the fractions

p p + q, q p + q. \hskip 28.45274pt\dfrac{p}{p+q},\quad\dfrac{q}{p+q}.

Rather surprisingly, every rational number p / q p/q with ( p, q) = 1 (p,q)=1 in the interval (0,1) occurs exactly once in the tree. This is not hard to prove, see, e.g., the paper [21]. We remark that the paper [17] consider this problem for larger classes of trees, but regretfully the rules for what the author’s call the Kepler tree are different from Kepler’s, but rather like those for the Calkin-Wilf tree (see [7]).

We introduce the two 2 × 2 2\times 2 matrices

K 0:= ( 1 0 1 1), K 1:= ( 0 1 1 1), \hskip 28.45274ptK_{0}:=\left(\begin{matrix}1\,0\\ 1\,1\end{matrix}\right),\quad K_{1}:=\left(\begin{matrix}0\,1\\ 1\,1\end{matrix}\right),

which we call the *Kepler matrices*.

( 1 0 0 1) \left(\begin{smallmatrix}1&0\\[1.42271pt] 0&1\end{smallmatrix}\right) ( 1 0 1 1) \left(\begin{smallmatrix}1&0\\[1.42271pt] 1&1\end{smallmatrix}\right) ( 1 0 2 1) \left(\begin{smallmatrix}1&0\\[1.42271pt] 2&1\end{smallmatrix}\right) ( 1 0 3 1) \left(\begin{smallmatrix}1&0\\[1.42271pt] 3&1\end{smallmatrix}\right) ( 2 1 3 1) \left(\begin{smallmatrix}2&1\\[1.42271pt] 3&1\end{smallmatrix}\right) ( 1 1 2 1) \left(\begin{smallmatrix}1&1\\[1.42271pt] 2&1\end{smallmatrix}\right) ( 1 1 3 2) \left(\begin{smallmatrix}1&1\\[1.42271pt] 3&2\end{smallmatrix}\right) ( 2 1 3 2) \left(\begin{smallmatrix}2&1\\[1.42271pt] 3&2\end{smallmatrix}\right) ( 0 1 1 1) \left(\begin{smallmatrix}0&1\\[1.42271pt] 1&1\end{smallmatrix}\right) ( 0 1 1 2) \left(\begin{smallmatrix}0&1\\[1.42271pt] 1&2\end{smallmatrix}\right) ( 0 1 1 3) \left(\begin{smallmatrix}0&1\\[1.42271pt] 1&3\end{smallmatrix}\right) ( 1 2 1 3) \left(\begin{smallmatrix}1&2\\[1.42271pt] 1&3\end{smallmatrix}\right) ( 1 1 1 2) \left(\begin{smallmatrix}1&1\\[1.42271pt] 1&2\end{smallmatrix}\right) ( 1 1 2 3) \left(\begin{smallmatrix}1&1\\[1.42271pt] 2&3\end{smallmatrix}\right) ( 1 2 2 3) \left(\begin{smallmatrix}1&2\\[1.42271pt] 2&3\end{smallmatrix}\right)

It is clear that the fraction at the node i ¯ = i 1 ​ … ​ i n \underline{i}=i_{1}\dots i_{n} in Kepler’s tree of fractions is equal to p / q p/q, where

( p q) = K i n ⋯ K i 1 ( 1 2). \hskip 28.45274pt\left(\begin{matrix}p\,\\ q\,\end{matrix}\right)=K_{i_{n}}\cdots K_{i_{1}}\left(\begin{matrix}1\\ 2\end{matrix}\right).

We claim that all the matrices K i n ⋯ K i 1 K_{i_{n}}\cdots K_{i_{1}} are different when n n ranges over the natural numbers, and i 1 ​ … ​ i n i_{1}\dots i_{n} is a string of 0’s and 1’s. Formulated slightly differently we have the following.

###### Lemma 1.

The monoid of matrices generated by K 0 K_{0} and K 1 K_{1} is free.

*Proof:*If K i ¯ = K j ¯ K_{\underline{i}}=K_{\underline{j}}, then K i ¯ ​ ( 1 2) = K j ¯ ​ ( 1 2) K_{\underline{i}}\left(\begin{smallmatrix}1\\ 2\end{smallmatrix}\right)=K_{\underline{j}}\left(\begin{smallmatrix}1\\ 2\end{smallmatrix}\right), contradicting uniqueness on the Kepler tree.

We remark that in general it is hard to determine freeness of matrix monoids. It is for instance an undecidable problem for 3 × 3 3\times 3 nonnegative integer matrices ( [18], see also [8]). We mention also that K 0 K_{0} and K 1 K_{1} are unimodular matrices, but that they do not satisfy the criteria in [20].

### 2.2. A tree of morphisms

Let φ 0 \varphi_{0} and φ 1 \varphi_{1} be the two morphisms given by

 | φ 0: { 0 → 0 1 → 01 φ 1: { 0 → 01 1 → 0. \varphi_{0}:\;\Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 01\end{aligned}\qquad\varphi_{1}:\;\Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 0\end{aligned}. |  |

We form a tree of morphisms 𝒯 φ \mathcal{T}_{\varphi} by putting Id: 0 → 0, 1 → 1 {\rm Id}\!:0\rightarrow 0,\,1\rightarrow 1 at Λ \Lambda, and φ i n ⋯ φ i 1 \varphi_{i_{n}}\cdots\varphi_{i_{1}} at node i ¯ = i 1 ​ … ​ i n \underline{i}=i_{1}\dots i_{n} for all n n and all i k ∈ { 0, 1 } i_{k}\in\{0,1\}, k = 1, …, n k=1,\dots,n.

Id { 0 → 0 1 → 01 \Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 01\end{aligned} { 0 → 0 1 → 001 \Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 001\end{aligned} { 0 → 0 1 → 0001 \Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 0001\end{aligned} { 0 → 01 1 → 01010 \Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 01010\end{aligned} { 0 → 01 1 → 010 \Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 010\end{aligned} { 0 → 001 1 → 0010 \Big\{\begin{aligned} 0&\rightarrow 001\\[-2.84544pt] 1&\rightarrow 0010\end{aligned} { 0 → 010 1 → 01001 \Big\{\begin{aligned} 0&\rightarrow 010\\[-2.84544pt] 1&\rightarrow 01001\end{aligned} { 0 → 01 1 → 0 \Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 0\end{aligned} { 0 → 001 1 → 0 \Big\{\begin{aligned} 0&\rightarrow 001\\[-2.84544pt] 1&\rightarrow 0\end{aligned} { 0 → 0001 1 → 0 \Big\{\begin{aligned} 0&\rightarrow 0001\\[-2.84544pt] 1&\rightarrow 0\end{aligned} { 0 → 01010 1 → 01 \Big\{\begin{aligned} 0&\rightarrow 01010\\[-2.84544pt] 1&\rightarrow 01\end{aligned} { 0 → 010 1 → 01 \Big\{\begin{aligned} 0&\rightarrow 010\\[-2.84544pt] 1&\rightarrow 01\end{aligned} { 0 → 0010 1 → 001 \Big\{\begin{aligned} 0&\rightarrow 0010\\[-2.84544pt] 1&\rightarrow 001\end{aligned} { 0 → 01001 1 → 010 \Big\{\begin{aligned} 0&\rightarrow 01001\\[-2.84544pt] 1&\rightarrow 010\end{aligned}

The figure shows the first 3 levels of this tree, labeled with the morphisms. Note that the left edge of 𝒯 φ \mathcal{T}_{\varphi} with nodes i ¯ = 0 n \underline{i}=0^{n} contains the morphisms φ 0 n \varphi_{0}^{n}, which do not generate infinite words.

###### Theorem 1.

The tree 𝒯 φ \mathcal{T}_{\varphi} contains all morphisms that have homogeneous Sturmian words c α c_{\alpha} as fixed point, for any α \alpha with 0 < α < 1 2 0<\alpha<\tfrac{1}{2}. Each such morphism occurs exactly once.

*Proof:*In [12] it is proved that for α ∈ ( 0, 1) \alpha\in(0,1), any morphism f f fixing a homogeneous Sturmian word is a composition of the two morphisms E E and G G, excluding f = E n f=E^{n}, f = G n f=G^{n} and f = E ​ G n ​ E f=EG^{n}E for n ≥ 1 n\geq 1. Moreover, if 0 < α < 1 2 0<\alpha<\tfrac{1}{2}, then the first element in the composition of f f is G G. But since E 2 = Id E^{2}={\rm Id}, f f can then be written as a composition of G = φ 0 G=\varphi_{0} and G ​ E = φ 1 GE=\varphi_{1}. This finishes the existence part of the proof.

For the uniqueness part, we remark first that it is shown in [12, Corollary 2.3.15], that in the monoid generated by the two morphisms E E and G ​ E GE the only relation is E 2 = Id E^{2}={\rm Id}. This implies, of course, that the monoid generated by G = φ 0 G=\varphi_{0} and G ​ E = φ 1 GE=\varphi_{1}, is free, but here we prefer to give a short self-contained proof, proving something stronger, which yields the emergence of the binary tree.

Consider the incidence matrices of the morphisms φ 0 \varphi_{0} and φ 1 \varphi_{1}:

M 0:= ( 1 1 0 1), M 1:= ( 1 1 1 0). \hskip 28.45274ptM_{0}:=\left(\begin{matrix}1\,1\\ 0\,1\end{matrix}\right),\quad M_{1}:=\left(\begin{matrix}1\,1\\ 1\,0\end{matrix}\right).

( 1 0 0 1) \left(\begin{smallmatrix}1&0\\[1.42271pt] 0&1\end{smallmatrix}\right) ( 1 1 0 1) \left(\begin{smallmatrix}1&1\\[1.42271pt] 0&1\end{smallmatrix}\right) ( 1 2 0 1) \left(\begin{smallmatrix}1&2\\[1.42271pt] 0&1\end{smallmatrix}\right) ( 1 3 0 1) \left(\begin{smallmatrix}1&3\\[1.42271pt] 0&1\end{smallmatrix}\right) ( 1 3 1 2) \left(\begin{smallmatrix}1&3\\[1.42271pt] 1&2\end{smallmatrix}\right) ( 1 2 1 1) \left(\begin{smallmatrix}1&2\\[1.42271pt] 1&1\end{smallmatrix}\right) ( 2 3 1 1) \left(\begin{smallmatrix}2&3\\[1.42271pt] 1&1\end{smallmatrix}\right) ( 2 3 1 2) \left(\begin{smallmatrix}2&3\\[1.42271pt] 1&2\end{smallmatrix}\right) ( 1 1 1 0) \left(\begin{smallmatrix}1&1\\[1.42271pt] 1&0\end{smallmatrix}\right) ( 2 1 1 0) \left(\begin{smallmatrix}2&1\\[1.42271pt] 1&0\end{smallmatrix}\right) ( 3 1 1 0) \left(\begin{smallmatrix}3&1\\[1.42271pt] 1&0\end{smallmatrix}\right) ( 3 1 2 1) \left(\begin{smallmatrix}3&1\\[1.42271pt] 2&1\end{smallmatrix}\right) ( 2 1 1 1) \left(\begin{smallmatrix}2&1\\[1.42271pt] 1&1\end{smallmatrix}\right) ( 3 2 1 1) \left(\begin{smallmatrix}3&2\\[1.42271pt] 1&1\end{smallmatrix}\right) ( 3 2 2 1) \left(\begin{smallmatrix}3&2\\[1.42271pt] 2&1\end{smallmatrix}\right)

Obviously morphisms with different incidence matrices are different. Let 𝒯 M {\mathcal{T}}_{M} be the tree with the matrix product M i n ⋯ M i 1 M_{i_{n}}\cdots M_{i_{1}} at node i 1 ​ … ​ i n i_{1}\dots i_{n}.

The matrices M 0 M_{0} and M 1 M_{1} are conjugate to the matrices K 0 K_{0} and K 1 K_{1} by the same conjugation matrix ( 0 1 1 0) \left(\begin{smallmatrix}0&1\\[1.42271pt] 1&0\end{smallmatrix}\right). It follows that for *any*node i ¯ \underline{i} one has

M i ¯ = ( 0 1 1 0) ​ K i ¯ ​ ( 0 1 1 0). \hskip 28.45274ptM_{\underline{i}}=\left(\begin{matrix}0\,1\\ 1\,0\end{matrix}\right)K_{\underline{i}}\left(\begin{matrix}0\,1\\ 1\,0\end{matrix}\right).

But then Lemma 1 implies that all the M i ¯ M_{\underline{i}} on 𝒯 M {\mathcal{T}}_{M} are different, and so each morphism occurs exactly once on 𝒯 φ \mathcal{T}_{\varphi}.

### 2.3. A tree of Sturm numbers

The tree of morphisms 𝒯 φ \mathcal{T}_{\varphi} has a left edge with morphisms that do not generate infinite words. Below we display the first three levels of the tree of Sturm numbers α \alpha with α < 1 2 \alpha<\frac{1}{2} associated to the morphisms of 𝒯 φ \mathcal{T}_{\varphi}. Each such α \alpha will occur infinitely times, since the powers of a morphism generate the same Sturmian word. In particular we will see on the right edge the number ( 3 − 5) / 2 (3-\sqrt{5})/2 associated to the the powers of the Fibonacci morphism φ 1 n \varphi_{1}^{n}.

∅ \emptyset ∅ \emptyset ∅ \emptyset ∅ \emptyset 13 − 1 6 \dfrac{\sqrt{13}-1}{6} 2 − 1 \sqrt{2}-1 13 − 3 2 \dfrac{\sqrt{13}-3}{2} 3 − 1 2 \dfrac{\sqrt{3}-1}{2} 3 − 5 2 \dfrac{3-\sqrt{5}}{2} 1 − 2 2 1-\dfrac{\sqrt{2}}{2} 5 − 13 6 \dfrac{5-\sqrt{13}}{6} 1 − 3 3 1-\dfrac{\sqrt{3}}{3} 3 − 5 2 \dfrac{3-\sqrt{5}}{2} 2 − 3 2-\sqrt{3} 3 − 5 2 \dfrac{3-\sqrt{5}}{2}

## 3. Inhomogeneous Sturmian words

In this section we consider *all*substitution invariant Sturmian words. There is again a simple algebraic characterization given by Yasutomi in ( [22]):

Let 0 < α < 1 0<\alpha<1 and 0 ≤ ρ ≤ 1 0\leq\rho\leq 1. Then s α, ρ s_{\alpha,\rho} is substitution invariant if and only if the following two conditions are satisfied:

 |  | ( i) \displaystyle(i) | α ​ is ​ an ​ irrational ​ quadratic ​ number ​ and ​ ρ ∈ ℚ ⁡ ( α); \displaystyle\alpha\;{\rm is\,an\,irrational\,quadratic\,number\,and\;}\rho\in\mathbb{Q}(\alpha); |  |

 |  | ( i ​ i) \displaystyle(ii) | α ¯ > 1, 1 − α ¯ ≤ ρ ¯ ≤ α ¯ or α ¯ < 0, α ¯ ≤ ρ ¯ ≤ 1 − α ¯. \displaystyle\overline{\alpha}>1,\,1-\overline{\alpha}\leq\overline{\rho}\leq\overline{\alpha}\quad{\rm or\quad}\overline{\alpha}<0,\,\overline{\alpha}\leq\overline{\rho}\leq 1-\overline{\alpha}. |  |

### 3.1. The eight elementary morphisms

We define the morphisms ψ i \psi_{i} for i = 1, …, 8 i=1,\dots,8 by

 |  | ψ 1: \displaystyle\psi_{1}: | 0 → 01, 1 → 0, ψ 2: 0 → 10, 1 → 0, ψ 3: 0 → 0, 1 → 01, ψ 4: 0 → 0, 1 → 10. \displaystyle\;0\rightarrow 01,\,1\rightarrow 0,\quad\psi_{2}:\;0\rightarrow 10,\,1\rightarrow 0,\quad\psi_{3}:\;\;0\rightarrow 0,\,1\rightarrow 01,\quad\psi_{4}:\;\;0\rightarrow 0,\,1\rightarrow 10. |  |

 |  | ψ 5: \displaystyle\psi_{5}: | 0 → 1, 1 → 10, ψ 6: 0 → 1, 1 → 01, ψ 7: 0 → 10, 1 → 1, ψ 8: 0 → 01, 1 → 1. \displaystyle\;0\rightarrow 1,\,1\rightarrow 10,\quad\psi_{6}:\;0\rightarrow 1,\,1\rightarrow 01,\quad\psi_{7}:\;\;0\rightarrow 10,\,1\rightarrow 1,\quad\psi_{8}:\;\;0\rightarrow 01,\,1\rightarrow 1. |  |

In the previous section the two morphisms ψ 1 = φ 1 \psi_{1}=\varphi_{1}, and ψ 3 = φ 0 \psi_{3}=\varphi_{0} were used. The first four morphisms are linked to Sturmian words with slope α < 1 / 2 \alpha<1/2, the last four to Sturmian words with slope α > 1 / 2 \alpha>1/2. In the columns there is duality: ψ i + 4 = E ​ ψ i ​ E \psi_{i+4}=E\psi_{i}E for i = 1, 2, 3, 4 i=1,2,3,4. We also have ψ 2 ​ i = ψ ~ 2 ​ i − 1 \psi_{2i}=\widetilde{\psi}_{2i-1} for i = 1, 2, 3, 4 i=1,2,3,4, where σ ~ \widetilde{\sigma} is the time reversal of a morphism σ \sigma.

The notation used in [12] is:

 | ψ 1 = φ, ψ 2 = φ ~, ψ 3 = φ ​ E, ψ 4 = φ ~ ​ E, ψ 5 = E ​ φ ​ E, ψ 6 = E ​ φ ~ ​ E, ψ 7 = E ​ φ, ψ 8 = E ​ φ ~. \psi_{1}=\varphi,\quad\psi_{2}=\widetilde{\varphi},\quad\psi_{3}=\varphi E,\quad\psi_{4}=\widetilde{\varphi}E,\quad\psi_{5}=E\varphi E,\quad\psi_{6}=E\widetilde{\varphi}E,\quad\psi_{7}=E\varphi,\quad\psi_{8}=E\widetilde{\varphi}. |  |

Let ℳ i, j = ⟨ ψ i, ψ j ⟩ \mathcal{M}_{i,j}=\langle\psi_{i},\psi_{j}\rangle denote the monoid generated by the morphisms ψ i \psi_{i} and ψ j \psi_{j}. We will also need ℳ i = ⟨ ψ i ⟩ \mathcal{M}_{i}=\langle\psi_{i}\rangle, the set of powers of ψ i \psi_{i}.

### 3.2. The floor-ceiling structure of Sturmian sequences

For most α \alpha ’s and ρ \rho ’s the floor and the ceiling representation of a Sturmian word in equations ( 1) and ( 2) are equal. Rather surprisingly, *if*they are not equal, then they only differ in at most two consecutive indices ( [12]). If there exists a natural number m ⋄ m_{\diamond} such that

 | s α, ρ ​ ( m ⋄ − 1) ≠ s α, ρ ′ ​ ( m ⋄ − 1) ​ and ​ s α, ρ ​ ( m ⋄) ≠ s α, ρ ′ ​ ( m ⋄), s_{\alpha,\rho}(m_{\diamond}-1)\neq s^{\prime}_{\alpha,\rho}(m_{\diamond}-1)\;{\rm and\;}s_{\alpha,\rho}(m_{\diamond})\neq s^{\prime}_{\alpha,\rho}(m_{\diamond}), |  |

then we call ( s α, ρ, s α, ρ ′) (s_{\alpha,\rho},s^{\prime}_{\alpha,\rho}) a *lozenge pair*with index m ⋄ m_{\diamond}. In case m ⋄ = 0 m_{\diamond}=0, there is actually only the index 0 where they differ. As indicated on page 48 of [12], ( s α, ρ, s α, ρ ′) (s_{\alpha,\rho},s^{\prime}_{\alpha,\rho}) is a lozenge pair with index m ⋄ m_{\diamond} if and only if

(5) |  | α ​ m ⋄ + ρ ∈ ℕ. \alpha m_{\diamond}+\rho\in\mathbb{N}. |  |

Example Let α = ( 3 − 5) / 2 \alpha=(3-\sqrt{5})/2 and ρ = ( 5 − 1) / 2 \rho=(\sqrt{5}-1)/2. Then α + ρ = 1 \alpha+\rho=1, so ( s α, ρ, s α, ρ ′) (s_{\alpha,\rho},s^{\prime}_{\alpha,\rho}) is a lozenge pair with index 1. Here s α, ρ = 1001001010010010 ​ … s_{\alpha,\rho}=1001001010010010\dots and s α, ρ ′ = 0101001010010010, … s^{\prime}_{\alpha,\rho}=0101001010010010,\dots. Both words are substitution invariant for the substitution 0 → 010, 1 → 10 0\rightarrow 010,1\rightarrow 10.

The following result is related to Corollary 1.4. in [3].

###### Proposition 1.

For substitution invariant lozenge pairs m ⋄ = 0 m_{\diamond}=0 or m ⋄ = 1 m_{\diamond}=1.

*Proof:*This follows directly from equation ( 5) and Yasutomi’s characterization.
Suppose m ⋄ ≥ 2 m_{\diamond}\geq 2 and α ​ m ⋄ + ρ = k \alpha m_{\diamond}+\rho=k for an integer k k. Since 0 < α ​ m ⋄ < m ⋄ 0<\alpha m_{\diamond}<m_{\diamond} and 0 ≤ ρ ≤ 1 0\leq\rho\leq 1 we must have

 | α ​ m ⋄ + ρ = k, where ​ k ∈ { 1, 2, …, m ⋄ }. \alpha m_{\diamond}+\rho=k,{\rm where\;}k\in\{1,2,\dots,m_{\diamond}\}. |  |

One easily checks that ρ ¯ = k − α ¯ ​ m ⋄ \overline{\rho}=k-\overline{\alpha}m_{\diamond}. Now if α ¯ > 1 \overline{\alpha}>1, then it should hold that

 | 1 − α ¯ ≤ ρ ¯ = k − α ¯ ​ m ⋄ ⇒ ( m ⋄ − 1) ​ α ¯ ≤ k − 1 ⇒ α ¯ ≤ 1, 1-\overline{\alpha}\leq\overline{\rho}=k-\overline{\alpha}m_{\diamond}\;\Rightarrow\;(m_{\diamond}-1)\overline{\alpha}\leq k-1\;\Rightarrow\;\overline{\alpha}\leq 1, |  |

yielding a contradiction. Similarly the case α ¯ < 0 \overline{\alpha}<0 yields a contradiction. ∎

We undertake the task of determining all substitution invariant Sturmian words that are lozenge pairs. We start with the case m ⋄ = 1 m_{\diamond}=1, which is simpler than m ⋄ = 0 m_{\diamond}=0.

### 3.3. Substitution invariant Sturmian words with 𝐦 ⋄ = 𝟏 \mathbf{m_{\mathbf{\diamond}}=1}

Note that m ⋄ = 1 m_{\diamond}=1 implies

 | α + ρ = 1. \alpha+\rho=1. |  |

We first give a very simple way to obtain the lozenge pair.

###### Proposition 2.

For α ∈ ( 0, 1) \alpha\in(0,1) let ( s α, 1 − α, s α, 1 − α ′) (s_{\alpha,1-\alpha},s^{\prime}_{\alpha,1-\alpha}) be the lozenge pair with m ⋄ = 1 m_{\diamond}=1. Then

 | s α, 1 − α = 10 ​ c α and s α, 1 − α ′ = 01 ​ c α. s_{\alpha,1-\alpha}=10\,c_{\alpha}\quad{\rm and\quad}s^{\prime}_{\alpha,1-\alpha}=01\,c_{\alpha}. |  |

*Proof:*Since α < 1, s α, 1 − α ​ ( 0) = [α + ρ] − [ρ] = 1 \alpha<1,\,s_{\alpha,1-\alpha}(0)=[\alpha+\rho]-[\rho]=1 and s α, 1 − α ​ ( 1) = [2 ​ α + ρ] − [α + ρ] = 0 s_{\alpha,1-\alpha}(1)=[2\alpha+\rho]-[\alpha+\rho]=0. Also, s α, 1 − α ′ ​ ( 0) = ⌈ α + ρ ⌉ − ⌈ ρ ⌉ = 0 s^{\prime}_{\alpha,1-\alpha}(0)=\lceil\alpha+\rho\rceil-\lceil\rho\rceil=0 and s α, 1 − α ′ ​ ( 1) = ⌈ 2 ​ α + ρ ⌉ − ⌈ α + ρ ⌉ = 1 s^{\prime}_{\alpha,1-\alpha}(1)=\lceil 2\alpha+\rho\rceil-\lceil\alpha+\rho\rceil=1. Let S S be the shift: S ⁡ ( w 0 ​ w 1 ​ w 2 ​ …) = w 1 ​ w 2 ​ … S(w_{0}w_{1}w_{2}\dots)=w_{1}w_{2}\dots. Adding α \alpha to ρ \rho shifts a Sturmian sequence by one: s α, ρ + α = S ⁡ ( s α, ρ) s_{\alpha,\rho+\alpha}=S(s_{\alpha,\rho}). So S 2 ​ ( s α, 1 − α) = s α, 1 + α = s α, α = c α S^{2}(s_{\alpha,1-\alpha})=s_{\alpha,1+\alpha}=s_{\alpha,\alpha}=c_{\alpha}. ∎

We still have to investigate whether s α, 1 − α s_{\alpha,1-\alpha} and s α, 1 − α ′ s^{\prime}_{\alpha,1-\alpha} are substitution invariant. This can be directly derived from [6], but we give here a short and more global proof. We start with a combinatorial lemma.

###### Lemma 2.

For any ψ ∈ ℳ 1, 3 \psi\in\mathcal{M}_{1,3} the words 01 ​ ψ 2 ​ ( 0) 01\psi^{2}(0) and 10 ​ ψ 2 ​ ( 1) 10\psi^{2}(1) are palindromes.

*Proof:*This relies on the notions and results of [12, Section 2.2.1]. The standard morphisms are the elements of ⟨ φ, E ⟩ = ⟨ ψ 1, E ⟩ \langle\varphi,E\rangle=\langle\psi_{1},E\rangle. Since ψ 3 = φ ​ E \psi_{3}=\varphi E, all ψ \psi from ℳ 1, 3 \mathcal{M}_{1,3} are standard. By Proposition 2.2.2 and Proposition 2.3.11 of [12], the words ψ ⁡ ( 0) \psi(0) and ψ ⁡ ( 1) \psi(1) are two standard words, which differ in their last two letters. But then ψ 2 ​ ( 0) \psi^{2}(0) and ψ 2 ​ ( 1) \psi^{2}(1) are standard words so that ψ 2 ​ ( 0) \psi^{2}(0) ends in 0, and ψ 2 ​ ( 1) \psi^{2}(1) ends in 1. Moreover, according to [12, Theorem 2.2.4], a word w w is standard if and only if it has length 1 or there exists a palindrome word p p such that w = p ​ 01 w=p\,01 or w = p ​ 10 w=p\,10. So the words

 | 01 ​ ψ 2 ​ ( 0) = 01 ​ p ​ 10 and ​ 10 ​ ψ 2 ​ ( 1) = 10 ​ p ′ ​ 01 01\psi^{2}(0)=01p\,10\quad{\rm and\;}10\psi^{2}(1)=10p^{\prime}01 |  |

are palindromes. The length 1 case may occur, but then 010 is a palindrome. ∎

###### Theorem 2.

Let s α, ρ s_{\alpha,\rho} and s α, ρ ′ s^{\prime}_{\alpha,\rho} be substitution invariant Sturmian words with m ⋄ = 1 m_{\diamond}=1 and α < 1 / 2 \alpha<1/2. Then these two words are fixed points of ψ 2 \psi^{2}, where ψ ∈ ℳ 2, 4 ∖ ℳ 4 \psi\in\mathcal{M}_{2,4}\smallsetminus\mathcal{M}_{4}. Here ψ \psi is given by ψ ~ ​ ( c α) = c α \widetilde{\psi}(c_{\alpha})=c_{\alpha}.

*Proof:*The condition m ⋄ = 1 m_{\diamond}=1 means that ρ = 1 − α \rho=1-\alpha. What we will show is that s α, 1 − α s_{\alpha,1-\alpha} and s α, 1 − α ′ s^{\prime}_{\alpha,1-\alpha} are fixed points of ψ ~ 2 \widetilde{\psi}^{2}, where ψ \psi fixes c α c_{\alpha}. Recall that ψ ~ \widetilde{\psi} is the time reversal of ψ \psi, and that ψ ~ 1 = ψ 2 \widetilde{\psi}_{1}=\psi_{2}, and ψ ~ 3 = ψ 4 \widetilde{\psi}_{3}=\psi_{4}. In general one has σ ​ τ ~ = σ ~ ​ τ ~ \widetilde{\sigma\tau}=\widetilde{\sigma}\widetilde{\tau} for two morphisms σ \sigma and τ \tau. It thus follows from Lemma 2 that for ψ ∈ ℳ 1, 3 \psi\in\mathcal{M}_{1,3} and all n ≥ 1 n\geq 1

 | 01 ​ ψ 2 ​ n ​ ( 0) = ψ ~ 2 ​ n ​ ( 0) ​ 10 and 10 ​ ψ 2 ​ n ​ ( 1) = ψ ~ 2 ​ n ​ ( 1) ​ 01. 01\,\psi^{2n}(0)=\widetilde{\psi}^{2n}(0)\,10\quad{\rm and\quad}10\,\psi^{2n}(1)=\widetilde{\psi}^{2n}(1)\,01. |  |

For such ψ \psi, not from ℳ 3 \mathcal{M}_{3}, when n → ∞ n\rightarrow\infty, the left sides converge to 01 ​ c α 01c_{\alpha}, respectively 10 ​ c α 10c_{\alpha}, and thus by Proposition 2, the right sides converge to s α, 1 − α s_{\alpha,1-\alpha} respectively s α, 1 − α ′ s^{\prime}_{\alpha,1-\alpha}. ∎

It is easily seen via duality that Theorem 2 also applies in case α > 1 / 2 \alpha>1/2, where ℳ 2, 4 ∖ ℳ 4 \mathcal{M}_{2,4}\smallsetminus\mathcal{M}_{4} has to be replaced by ℳ 6, 8 ∖ ℳ 8 \mathcal{M}_{6,8}\smallsetminus\mathcal{M}_{8}.

### 3.4. Substitution invariant Sturmian words with 𝐦 ⋄ = 𝟎 \mathbf{m_{\mathbf{\diamond}}=0}

Note that m ⋄ = 0 m_{\diamond}=0 implies ρ = 0. \rho=0. As in the case of m ⋄ = 1 m_{\diamond}=1 there is a simple way to obtain the lozenge pair:

 | s α, 0 = 0 ​ c α and s α, 0 ′ = 1 ​ c α. s_{\alpha,0}=0\,c_{\alpha}\quad{\rm and\quad}s^{\prime}_{\alpha,0}=1\,c_{\alpha}. |  |

It is well known that 0 ​ c α 0\,c_{\alpha} is substitution invariant, see, e.g., Corollary 1.4. in [3]. However, it is now less simple to determine the substitution fixing 0 ​ c α 0\,c_{\alpha} for a given α \alpha.

Example Let α = ( 13 − 1) / 6 \alpha=(\sqrt{13}-1)/6. Then γ ⁡ ( c α) = c α \gamma(c_{\alpha})=c_{\alpha} for γ \gamma given by γ ⁡ ( 0) = 01, γ ⁡ ( 1) = 01010. \gamma(0)=01,\;\gamma(1)=01010.
(The same morphism is considered in [6] on page 262.)
Here ψ ⁡ ( s α, 0) = s α, 0 \psi(s_{\alpha,0})=s_{\alpha,0} for ψ \psi given by
ψ ⁡ ( 0) = 0010101, ψ ⁡ ( 1) = 0010101001010101. \psi(0)=0010101,\quad\psi(1)=0010101001010101.

A recipe is given in [6]. The recipe depends strongly on the last letter of γ ⁡ ( 0) \gamma(0), so it is useful to characterize the morphisms γ \gamma with γ ⁡ ( 0) \gamma(0) ending in 0 0.

###### Lemma 3.

Let γ = ψ i 1 ​ … ​ ψ i m \gamma=\psi_{i_{1}}\dots\psi_{i_{m}} be a morphism from ℳ 1, 3 \mathcal{M}_{1,3}, then γ ⁡ ( 0) \gamma(0) ends in 0 0 if and only if the number of 1 1 in i 1 ​ … ​ i m i_{1}\dots i_{m} is even.

*Proof:*All three words ψ 1 ​ ( 1), ψ 3 ​ ( 0), ψ 3 ​ ( 1) \psi_{1}(1),\psi_{3}(0),\psi_{3}(1) end in 0 0, but ψ 1 ​ ( 0) \psi_{1}(0) ends in 1 1. ∎

We denote the set of γ \gamma from ℳ 1, 3 \mathcal{M}_{1,3} such γ ⁡ ( 0) \gamma(0) ends in 0 0 by ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}.

###### Proposition 3.

Let γ ∈ ℳ 1, 3 0 \gamma\in\mathcal{M}^{0}_{1,3}, such that γ ⁡ ( c α) = c α \gamma(c_{\alpha})=c_{\alpha}. Let Ψ γ \Psi_{\gamma} be conjugate to γ \gamma, with conjugating word equal to u = γ ⁡ ( 0) ​ 0 − 1 u=\gamma(0)0^{-1}. Then

 | Ψ γ ​ ( 0 ​ c α) = 0 ​ c α. \Psi_{\gamma}(0c_{\alpha})=0c_{\alpha}. |  |

For a proof of this proposition, see [6, Theorem 3.1].

###### Proposition 4.

Let γ, δ ∈ ℳ 1, 3 0 \gamma,\delta\in\mathcal{M}^{0}_{1,3}. Then Ψ γ ​ δ = Ψ γ ​ Ψ δ. \Psi_{\gamma\delta}=\Psi_{\gamma}\Psi_{\delta}.

*Proof:*We assume that | γ ⁡ ( 0) | < | γ ⁡ ( 1) | |\gamma(0)|<|\gamma(1)|, the proof of the other case is quite similar. It is well known that there exist words u, v, x, u,v,x, and y y such that

 | γ: { 0 → u ​ 0 1 → u ​ 0 ​ v Ψ γ: { 0 → 0 ​ u 1 → 0 ​ v ​ u δ: { 0 → x ​ 0, 1 → x ​ 0 ​ y Ψ δ: { 0 → 0 ​ x 1 → 0 ​ y ​ x. \gamma:\left\{\begin{aligned} 0&\rightarrow u\,0\\ 1&\rightarrow u\,0\,v\end{aligned}\right.\quad\Psi_{\gamma}:\left\{\begin{aligned} 0&\rightarrow 0\,u\\ 1&\rightarrow 0\,v\,u\end{aligned}\right.\qquad\delta:\left\{\begin{aligned} 0&\rightarrow x\,0,\\ 1&\rightarrow x\,0\,y\end{aligned}\right.\quad\Psi_{\delta}:\left\{\begin{aligned} 0&\rightarrow 0\,x\\ 1&\rightarrow 0\,y\,x.\end{aligned}\right. |  |

The product γ ​ δ \gamma\delta also generates a characteristic sequence, and we have

 | γ δ: { 0 → γ ⁡ ( x) ​ γ ​ ( 0) = γ ⁡ ( x) ​ u ​ 0 1 → γ ⁡ ( x) ​ γ ​ ( 0) ​ γ ​ ( y) = γ ⁡ ( x) ​ u ​ 0 ​ γ ​ ( y) Ψ γ ​ δ: { 0 → 0 ​ γ ​ ( x) ​ u 1 → 0 ​ γ ​ ( y) ​ γ ​ ( x) ​ u. \gamma\delta:\left\{\begin{aligned} 0&\rightarrow\gamma(x)\,\gamma(0)=\gamma(x)\,u\,0\\ 1&\rightarrow\gamma(x)\,\gamma(0)\,\gamma(y)=\gamma(x)\,u\,0\,\gamma(y)\end{aligned}\right.\qquad\Psi_{\gamma\delta}:\left\{\begin{aligned} 0&\rightarrow 0\,\gamma(x)\,u\\ 1&\rightarrow 0\,\gamma(y\,)\gamma(x)\,u.\end{aligned}\right. |  |

This is a slightly extended version of [12, Lemma 2.3.17 (iii)], which leads to Ψ γ ​ δ = Ψ γ ​ Ψ δ, \Psi_{\gamma\delta}=\Psi_{\gamma}\Psi_{\delta}, since

 | Ψ γ Ψ δ: { 0 → Ψ γ ​ ( 0) ​ Ψ γ ​ ( x) = 0 ​ u ​ Ψ γ ​ ( x) = 0 ​ γ ​ ( x) ​ u 1 → Ψ γ ​ ( 0) ​ Ψ γ ​ ( y) ​ Ψ γ ​ ( x) = 0 ​ u ​ Ψ γ ​ ( y) ​ Ψ γ ​ ( x) = 0 ​ γ ​ ( y) ​ γ ​ ( x) ​ u, \Psi_{\gamma}\Psi_{\delta}:\left\{\begin{aligned} 0&\rightarrow\Psi_{\gamma}(0)\,\Psi_{\gamma}(x)=0\,u\,\Psi_{\gamma}(x)=0\,\gamma(x)\,u\\ 1&\rightarrow\Psi_{\gamma}(0)\,\Psi_{\gamma}(y)\,\Psi_{\gamma}(x)=0\,u\,\Psi_{\gamma}(y)\,\Psi_{\gamma}(x)=0\,\gamma(y\,)\gamma(x)\,u,\end{aligned}\right. |  |

where we use the conjugation relation u ​ Ψ γ ​ ( w) = γ ⁡ ( w) ​ u u\,\Psi_{\gamma}(w)=\gamma(w)\,u for w = x, y ​ x w=x,yx. ∎

For a further description we need next to ψ 3 \psi_{3} yet another elementary morphism ψ 8 = E ​ φ ~ \psi_{8}=E\,\widetilde{\varphi}:

 | ψ 3: 0 → 0, 1 → 01, ψ 8: 0 → 01, 1 → 1. \psi_{3}:\;0\rightarrow 0,\,1\rightarrow 01,\qquad\psi_{8}:\;0\rightarrow 01,\,1\rightarrow 1. |  |

###### Lemma 4.

Let γ = ψ 1 ​ ψ 3 n ​ ψ 1 \gamma=\psi_{1}\psi_{3}^{n}\psi_{1} for some n ≥ 0 n\geq 0. Then Ψ γ = ψ 3 ​ ψ 8 n + 1 \Psi_{\gamma}=\psi_{3}\psi_{8}^{n+1}.

*Proof:*One easily finds that for all n ≥ 0 n\geq 0

 | ψ 1 ​ ψ 3 n ​ ψ 1 ​ ( 0) = ( 01) n + 1 ​ 0, ψ 1 ​ ψ 3 n ​ ψ 1 ​ ( 1) = 01; ψ 3 ​ ψ 8 n + 1 ​ ( 0) = 0 ​ ( 01) n + 1, ψ 3 ​ ψ 8 n + 1 ​ ( 1) = 01. \psi_{1}\psi_{3}^{n}\psi_{1}(0)=(01)^{n+1}0,\;\psi_{1}\psi_{3}^{n}\psi_{1}(1)=01;\quad\psi_{3}\psi_{8}^{n+1}(0)=0(01)^{n+1},\;\psi_{3}\psi_{8}^{n+1}(1)=01. |  |

This implies the statement of the lemma. ∎

We need more details on the structure of the map γ ↦ Ψ γ \gamma\mapsto\Psi_{\gamma}.

###### Proposition 5.

Let γ \gamma be a morphism from ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}. Then

 | Ψ E ​ γ ​ E = E ​ Ψ ~ γ ​ E. \Psi_{E\gamma E}=E\,\widetilde{\Psi}_{\gamma}\,E. |  |

Moreover, Ψ E ​ γ ​ E = Ψ γ ∗ \Psi_{E\gamma E}=\Psi_{\gamma}^{*}, where ⋅ ∗ \cdot^{*} is the homomorphism defined by ψ 3 ∗ = ψ 8, ψ 8 ∗ = ψ 3 \psi_{3}^{*}=\psi_{8},\,\psi_{8}^{*}=\psi_{3}.

*Proof:*We assume that | γ ⁡ ( 0) | < | γ ⁡ ( 1) | |\gamma(0)|<|\gamma(1)|, the proof of the other case is quite similar. We use the same facts on γ \gamma from [12] as in the proof of Lemma 2. Since ( γ ⁡ ( 0), γ ⁡ ( 1)) (\gamma(0),\gamma(1)) is a standard pair, and all γ ⁡ ( 0) \gamma(0) from ℳ 1, 3 \mathcal{M}_{1,3} start with 0, there exist 2 2 2 Here we admit p = 0 − 1 p=0^{-1}, with length | p | = − 1 |p|=-1. palindromes p p and q q such that

 | γ: { 0 → 0 ​ p ​ 0 1 0 1 → 0 ​ p ​ 0 1 0 ​ q ​ 0 1, Ψ γ: { 0 → 0 0 ​ p ​ 0 1 1 → 0 ​ q ​ 0 1 0 ​ p ​ 0 1. \gamma:\left\{\begin{aligned} 0&\rightarrow 0\,p\,0\,1\,0\\ 1&\rightarrow 0\,p\,0\,1\,0\,q\,0\,1,\end{aligned}\right.\qquad\Psi_{\gamma}:\left\{\begin{aligned} 0&\rightarrow 0\,0\,p\,0\,1\\ 1&\rightarrow 0\,q\,0\,1\,0\,p\,0\,1.\end{aligned}\right. |  |

So we have

 | Ψ ~ γ: { 0 → 1 0 ​ p ​ 0 0 1 → 1 0 ​ p ​ 0 1 0 ​ q ​ 0, E Ψ ~ γ E: { 0 → 0 1 ​ p ¯ ​ 1 0 1 ​ q ¯ ​ 1 1 → 0 1 ​ p ¯ ​ 1 1. \widetilde{\Psi}_{\gamma}:\left\{\begin{aligned} 0&\rightarrow 1\,0\,p\,0\,0\\ 1&\rightarrow 1\,0\,p\,0\,1\,0\,q\,0,\end{aligned}\right.\qquad E\widetilde{\Psi}_{\gamma}E:\left\{\begin{aligned} 0&\rightarrow 0\,1\,\overline{p}\,1\,0\,1\overline{q}\,1\\ 1&\rightarrow 0\,1\,\overline{p}\,1\,1.\end{aligned}\right. |  |

On the other hand,

 | E γ E: { 0 → 1 ​ p ¯ ​ 1 0 1 ​ q ¯ ​ 1 0 1 → 1 ​ p ¯ ​ 1 0 1, Ψ E ​ γ ​ E: { 0 → 0 1 ​ p ¯ ​ 1 0 1 ​ q ¯ ​ 1 1 → …. E\gamma E:\left\{\begin{aligned} 0&\rightarrow 1\,\overline{p}\,1\,0\,1\overline{q}\,1\,0\\ 1&\rightarrow 1\,\overline{p}\,1\,0\,1,\end{aligned}\right.\qquad\Psi_{E\gamma E}:\left\{\begin{aligned} 0&\rightarrow 0\,1\,\overline{p}\,1\,0\,1\overline{q}\,1\\ 1&\rightarrow\dots.\end{aligned}\right. |  |

Note that we showed Ψ E ​ γ ​ E ​ ( 0) = E ​ Ψ ~ γ ​ E ​ ( 0) \Psi_{E\gamma E}(0)=E\widetilde{\Psi}_{\gamma}E(0), but for 1 this is trickier. A way to look at conjugation is by simultaneous repeated rotation. Here by *rotation*we mean the map ρ \rho on words defined by

 | ρ ⁡ ( w 1 ​ w 2 ​ … ​ w m) = w 2 ​ … ​ w m ​ w 1. \rho(w_{1}w_{2}\dots w_{m})=w_{2}\dots w_{m}w_{1}. |  |

Moreover, words may only be rotated simultaneously if their first letters are equal.

From this viewpoint,

 | Ψ E ​ γ ​ E ​ ( 0) = ρ | E ​ γ ​ E ​ ( 0) | − 1 ​ E ​ γ ​ E ​ ( 0) = ρ | p | + | q | + 5 ​ E ​ γ ​ E ​ ( 0). \Psi_{E\gamma E}(0)=\rho^{|E\gamma E(0)|-1}E\gamma E(0)=\rho^{|p|+|q|+5}E\gamma E(0). |  |

Since the length of E ​ γ ​ E ​ ( 1) E\gamma E(1) equals | p | + 4 |p|+4, and E ​ γ ​ E ​ ( 1) E\gamma E(1) is a prefix of E ​ γ ​ E ​ ( 0) E\gamma E(0), we may first rotate | p | + 4 |p|+4 times, obtaining

 | ρ | p | + 4 ​ Ψ E ​ γ ​ E ​ ( 0) = q ¯ ​ 1 0 1 ​ p ¯ ​ 1 0 1 ρ | p | + 4 ​ Ψ E ​ γ ​ E ​ ( 1) = 1 ​ p ¯ ​ 1 0 1. \rho^{|p|+4}\Psi_{E\gamma E}(0)=\overline{q}\,1\,0\,1\,\overline{p}\,1\,0\,1\quad\rho^{|p|+4}\Psi_{E\gamma E}(1)=1\,\overline{p}\,1\,0\,1. |  |

To continue rotating | q | + 1 |q|+1 times, , we must see that q ¯ ​ 1 \overline{q}\,1 is a prefix of 1 ​ p ¯ ​ 1 0 1 1\,\overline{p}\,1\,0\,1, *and*we want to see that the outcome is

 | ρ | q | + 1 ​ ( 1 ​ p ¯ ​ 1 0 1) = 0 1 ​ p ¯ ​ 1 1, or ​ equivalently, ρ | q | + 1 ​ ( 0 ​ p ​ 0 1 0) = 1 0 ​ p ​ 0 0. \rho^{|q|+1}(1\,\overline{p}\,1\,0\,1)=0\,1\,\overline{p}\,1\,1,\quad{\rm or\,equivalently,\quad}\rho^{|q|+1}(0\,p\,0\,1\,0)=1\,0\,p\,0\,0. |  |

This requires for the time being that | q | ≤ | p | + 4 |q|\leq|p|+4.

According to [12, Theorem 2.2.4] the word 0 ​ p ​ 0 1 0 ​ q 0\,p\,0\,1\,0\,q is a palindrome, and so

 | 0 ​ p ​ 0 1 0 ​ q = q ​ 0 1 0 ​ p ​ 0, 0\,p\,0\,1\,0\,q=q\,0\,1\,0\,p\,0, |  |

hence ρ | q | + 1 ​ ( 0 ​ p ​ 0 1 0) \rho^{|q|+1}(0\,p\,0\,1\,0) has prefix 1 0 ​ p ​ 0 1\,0\,p\,0, and the next letter is a 0 0, because we see also from this equation that the first letter of q q is a 0 0. Note that this palindrome equation also implies that q ¯ ​ 1 \overline{q}\,1 is a prefix of 1 ​ p ¯ ​ 1 0 1 1\,\overline{p}\,1\,0\,1.

In the case that | q | > | p | + 4 |q|>|p|+4, suppose that | q | = a ⁡ ( | p | + 4) + b |q|=a(|p|+4)+b, where b < | p | + 4 b<|p|+4. Then one rotates with ρ | p | + 4 \rho^{|p|+4} a + 1 a+1 times, followed by a rotation ρ b + 1 \rho^{b+1}. That this is possible, one can deduce from [12, Proposition 2.2.2], which states that only the last two letters of the words γ ⁡ ( 0) ​ γ ​ ( 1) \gamma(0)\gamma(1) and γ ⁡ ( 1) ​ γ ​ ( 0) \gamma(1)\gamma(0) are different. A zig-zag argument then gives that γ ⁡ ( 1) = γ ​ ( 0) a + 1 ​ 01 \gamma(1)=\gamma(0)^{a+1}01.

For the second part of the proposition, note that ψ 3 ∗ = E ​ ψ ~ 3 ​ E = ψ 8 \psi_{3}^{*}=E\widetilde{\psi}_{3}E=\psi_{8}, and ψ 8 ∗ = E ​ ψ ~ 8 ​ E = ψ 3 \psi_{8}^{*}=E\widetilde{\psi}_{8}E=\psi_{3}. Let Ψ γ = ψ i 1 ​ … ​ ψ i m \Psi_{\gamma}=\psi_{i_{1}}\dots\psi_{i_{m}}. Then we have, using the first part of the proposition,

 | Ψ E ​ γ ​ E = E ​ Ψ ~ γ ​ E = E ​ ψ ~ i 1 ​ … ​ ψ ~ i m ​ E = E ​ ψ ~ i 1 ​ E ​ E ​ ψ ~ i 2 ​ E ​ … ​ E ​ ψ ~ i m ​ E = ψ i 1 ∗ ​ ψ i 2 ∗ ​ … ​ ψ i m ∗ = Ψ γ ∗. ∎ \Psi_{E\gamma E}=E\,\widetilde{\Psi}_{\gamma}\,E=E\widetilde{\psi}_{i_{1}}\dots\widetilde{\psi}_{i_{m}}E=E\widetilde{\psi}_{i_{1}}EE\widetilde{\psi}_{i_{2}}E\dots E\widetilde{\psi}_{i_{m}}E=\psi_{i_{1}}^{*}\psi_{i_{2}}^{*}\dots\psi_{i_{m}}^{*}=\Psi_{\gamma}^{*}.\hfill\qed |  |

###### Theorem 3.

Let α \alpha be a Sturmian number, with 0 < α < 1 0<\alpha<1. Then s α, 0 s_{\alpha,0} is a fixed point of some ψ ∈ ℳ 3, 8 \psi\in\mathcal{M}_{3,8}. Conversely, any ψ ∈ ℳ 3, 8 ∖ { ℳ 3 ∪ ℳ 8 } \psi\in\mathcal{M}_{3,8}\smallsetminus\{\mathcal{M}_{3}\cup\mathcal{M}_{8}\} fixes an s α, 0 s_{\alpha,0}. The same statements hold for s α, 0 ′ s^{\prime}_{\alpha,0}, but then with ℳ 3, 8 \mathcal{M}_{3,8} replaced by ℳ 4, 7 \mathcal{M}_{4,7}.

*Proof:*We have s α, 0 = 0 ​ c α s_{\alpha,0}=0\,c_{\alpha}. Suppose γ ∈ ℳ 1, 3 \gamma\in\mathcal{M}_{1,3} satisfies γ ⁡ ( c α) = c α \gamma(c_{\alpha})=c_{\alpha}. Then γ 2 ​ ( c α) = c α \gamma^{2}(c_{\alpha})=c_{\alpha} and γ 2 ∈ ℳ 1, 3 0 \gamma^{2}\in\mathcal{M}^{0}_{1,3}, so by Proposition 3, s α, 0 s_{\alpha,0} is fixed point of Ψ γ 2 \Psi_{\gamma^{2}}.

We claim that any Ψ γ \Psi_{\gamma}, where γ \gamma is from ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}, is an element of ℳ 3, 8 \mathcal{M}_{3,8}. We prove this claim by induction on m m where γ = ψ i 1 ​ … ​ ψ i m \gamma=\psi_{i_{1}}\dots\psi_{i_{m}}. For m = 2 m=2, γ = ψ 1 2 \gamma=\psi_{1}^{2}, and the claim is true by Lemma 4. Suppose the claim is true for all γ \gamma from ℳ 1, 3 0 \mathcal{M}^{0}_{1,3} with length m m or less. An arbitrary γ = ψ i 1 ​ … ​ ψ i m + 1 \gamma=\psi_{i_{1}}\dots\psi_{i_{m+1}} from ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}, can be written as γ = γ ′ ​ γ ′′ \gamma=\gamma^{\prime}\gamma^{\prime\prime}, where γ ′ \gamma^{\prime} and γ ′′ \gamma^{\prime\prime} are non-trivial elements of ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}, *unless*γ \gamma has the form

 | γ = ψ 1 ​ ψ 3 m − 1 ​ ψ 1, \gamma=\psi_{1}\psi_{3}^{m-1}\psi_{1}, |  |

but then Ψ γ ∈ ℳ 3, 8 \Psi_{\gamma}\in\mathcal{M}_{3,8} according to Lemma 4. The first part of the theorem is proved.

For the second part, we divide the morphisms in ℳ 3, 8 \mathcal{M}_{3,8} into two types: the ones starting with ψ 3 \psi_{3} and the ones starting with ψ 8 \psi_{8}. A density argument shows that first type corresponds to ψ \psi with α < 1 / 2 \alpha<1/2, and the second type to ψ \psi with α > 1 / 2 \alpha>1/2. Moreover, by Proposition 5 these are in 1-to-1 correspondence with each other by replacing all ψ 3 \psi_{3} by ψ 8 \psi_{8} and conversely. It suffices therefore, to show that any ψ \psi from ℳ 3, 8 ∖ ℳ 3 \mathcal{M}_{3,8}\smallsetminus\mathcal{M}_{3} starting with ψ 3 \psi_{3} fixes an s α, 0 = 0 ​ c α s_{\alpha,0}=0c_{\alpha}. This can be done with an argument similar to the one above. Let ψ = ψ 3 ​ ψ i 2 ​ … ​ ψ i m \psi=\psi_{3}\psi_{i_{2}}\dots\psi_{i_{m}}. When m = 2 m=2, ψ = ψ 3 ​ ψ 8 \psi=\psi_{3}\psi_{8}, and we know that ψ ⁡ ( 0 ​ c α) = c α \psi(0c_{\alpha})=c_{\alpha}, where c α c_{\alpha} is the fixed point of ψ 1 2 \psi_{1}^{2}. Proceed by induction, using Proposition 4. Now ψ \psi can be written as ψ ′ ​ ψ ′′ \psi^{\prime}\psi^{\prime\prime} with ψ ′ = ψ 3 ​ … \psi^{\prime}=\psi_{3}\dots and ψ ′′ = ψ 3 ​ … \psi^{\prime\prime}=\psi_{3}\dots*unless*ψ \psi has the form ψ 3 ​ ψ 8 m \psi_{3}\psi_{8}^{m}, but then we can use Lemma 4.

To handle s α, 0 ′ = 1 ​ c α s^{\prime}_{\alpha,0}=1c_{\alpha}, we use the property that in general s α, ρ ′ = E ​ s 1 − α, 1 − ρ s^{\prime}_{\alpha,\rho}=E\,s_{1-\alpha,1-\rho} (see [12, Lemma 2.2.17]). This yields

 | s α, 0 ′ = E ​ s 1 − α, 1 = E ​ s 1 − α, 0. s^{\prime}_{\alpha,0}=E\,s_{1-\alpha,1}=E\,s_{1-\alpha,0}. |  |

Since in general E ⁡ ( w) E(w) is a fixed point of E ​ σ ​ E E\sigma E when w w is a fixed point of σ \sigma, we obtain that the s α, 0 ′ s^{\prime}_{\alpha,0} are generated by the morphisms from the monoid ℳ 4, 7 \mathcal{M}_{4,7}, since E ​ ψ 3 ​ E = ψ 7 E\psi_{3}E=\psi_{7} and E ​ ψ 8 ​ E = ψ 4 E\psi_{8}E=\psi_{4}. ∎

Remark 1 There is an interesting coding from the morphisms starting with ψ 3 \psi_{3} in ℳ 3, 8 \mathcal{M}_{3,8} to ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}. Let + be binary addition with 3 and 8: 3+3=3, 8+8=3, 3+8=8, 8+3=8. Add i 2 ​ i 3 ​ … ​ i m ​ 3 i_{2}i_{3}\dots i_{m}3 to 3 ​ i 2 ​ … ​ i m 3\,i_{2}\dots i_{m}, and replace 8 8 by 1. For example: 38 ​ … ​ 88 + 88 ​ … ​ 83 = 83 ​ … ​ 38 ↦ 13 ​ … ​ 31 38...88+88...83=83...38\mapsto 13...31.

We display the first three levels of the binary tree 𝒯 3, 8 \mathcal{T}_{3,8}, where the nodes are labeled with the morphisms given by Theorem 3.

Id { 0 → 0 1 → 01 \Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 01\end{aligned} { 0 → 0 1 → 001 \Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 001\end{aligned} { 0 → 0 1 → 0001 \Big\{\begin{aligned} 0&\rightarrow 0\\[-2.84544pt] 1&\rightarrow 0001\end{aligned} { 0 → 01 1 → 01011 \Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 01011\end{aligned} { 0 → 01 1 → 011 \Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 011\end{aligned} { 0 → 001 1 → 00101 \Big\{\begin{aligned} 0&\rightarrow 001\\[-2.84544pt] 1&\rightarrow 00101\end{aligned} { 0 → 011 1 → 0111 \Big\{\begin{aligned} 0&\rightarrow 011\\[-2.84544pt] 1&\rightarrow 0111\end{aligned} { 0 → 01 1 → 1 \Big\{\begin{aligned} 0&\rightarrow 01\\[-2.84544pt] 1&\rightarrow 1\end{aligned} { 0 → 001 1 → 01 \Big\{\begin{aligned} 0&\rightarrow 001\\[-2.84544pt] 1&\rightarrow 01\end{aligned} { 0 → 0001 1 → 001 \Big\{\begin{aligned} 0&\rightarrow 0001\\[-2.84544pt] 1&\rightarrow 001\end{aligned} { 0 → 01011 1 → 011 \Big\{\begin{aligned} 0&\rightarrow 01011\\[-2.84544pt] 1&\rightarrow 011\end{aligned} { 0 → 011 1 → 1 \Big\{\begin{aligned} 0&\rightarrow 011\\[-2.84544pt] 1&\rightarrow 1\end{aligned} { 0 → 00101 1 → 01 \Big\{\begin{aligned} 0&\rightarrow 00101\\[-2.84544pt] 1&\rightarrow 01\end{aligned} { 0 → 0111 1 → 1 \Big\{\begin{aligned} 0&\rightarrow 0111\\[-2.84544pt] 1&\rightarrow 1\end{aligned}

Remark 2 Just as in Theorem 1, each morphism generating an s α, 0 s_{\alpha,0} occurs exactly once on the tree 𝒯 3, 8 \mathcal{T}_{3,8}. This can be deduced from the fact that we have a coding between ℳ 3, 8 \mathcal{M}_{3,8} and ℳ 1, 3 0 \mathcal{M}^{0}_{1,3}, but also because the monoid generated by the incidence matrices of ψ 3 \psi_{3} and ψ 8 \psi_{8} is free. Arnoux remarks that this can be derived in an elementary way ( [4, Lemma 6.5.14]).

## 4. Generating substitution invariant Sturmian words

There is a direct, more analytic way to find substitution invariant Sturmian words. We use an idea already considered by self-similarity expert Douglas Hofstadter in 1963 ( [10]). To solve the fixed point equation ψ ⁡ ( s α, ρ) = s α, ρ \psi(s_{\alpha,\rho})=s_{\alpha,\rho} for ψ \psi, we can equivalently solve the fixed point equation

 | T ψ ​ ( x, y) = ( x, y) for ​ 0 < x, y < 1, T_{\psi}(x,y)=(x,y)\quad{\rm for\;}0<x,y<1, |  |

where T ψ = T i 1 ​ … ​ T i n T_{\psi}=T_{i_{1}}\dots T_{i_{n}} if ψ = ψ i 1 ​ … ​ ψ i n \psi=\psi_{i_{1}}\dots\psi_{i_{n}} with the i k i_{k} from some subset of { 1, …, 8 } \{1,\dots,8\}. Here the T i T_{i} are two-dimensional fractional linear functions, such that

 | ψ i ​ ( s α, ρ) = s T i ​ ( α, ρ). \psi_{i}(s_{\alpha,\rho})=s_{T_{i}(\alpha,\rho)}. |  |

Some T i T_{i} are given by [12, Lemma 2.2.18], and the others can be computed in a similar way. We have for example

 | T 1 ​ ( x, y) = ( 1 − x 2 − x, 1 − y 2 − x), T 3 ​ ( x, y) = ( x 1 + x, y 1 + x), T 8 ​ ( x, y) = ( 1 2 − x, y 2 − x). T_{1}(x,y)=\left(\frac{1-x}{2-x},\frac{1-y}{2-x}\right),\quad T_{3}(x,y)=\left(\frac{x}{1+x},\frac{y}{1+x}\right),\quad T_{8}(x,y)=\left(\frac{1}{2-x},\frac{y}{2-x}\right). |  |

Note that both T 3 T_{3} and T 8 T_{8} leave the line y = 0 y=0 invariant; this suggests the use of products of ψ 3 \psi_{3} and ψ 8 \psi_{8} to solve the equation ψ ⁡ ( s α, 0) = s α, 0 \psi(s_{\alpha,0})=s_{\alpha,0}, as we did in Theorem 3. We mention that the triple T 1, T 3, T 8 T_{1},T_{3},T_{8} occurs in [9], where they are used to connect two-dimensional continued fraction expansions to substitution invariant Sturmian words.

Solving the equation T ψ ​ ( x, y) = ( x, y) T_{\psi}(x,y)=(x,y) is straightforward: there is a one-dimensional fractional linear function fixed point equation for x x, which is quadratic, and then there is a linear equation for y y, since one can show by induction on the number of ψ i \psi_{i} in ψ \psi that only ± y \pm y will occur in the second component of T ψ ​ ( x, y) T_{\psi}(x,y).

We mention that is some cases the equation is actually ψ ⁡ ( s α, ρ) = s T ψ ​ ( α, ρ) ′ \psi(s_{\alpha,\rho})=s^{\prime}_{T_{\psi}(\alpha,\rho)}, but this can be dealt with by passing to the square of ψ \psi, or by using Proposition 1.

## References

- [1] C. Allauzen, Une caractérisation simple des nombres de Sturm, J. Théor. Nombres Bordeaux 10 (1998), 237–241.
- [2] Allouche, Jean-Paul and Shallit, Jeffrey, Automatic sequences, Theory, applications, generalizations, Cambridge University Press, Cambridge, 2003, xvi+571.
- [3] Valérie Berthé, Hiromi Ei, Shunji Ito and Hui Rao, On substitution invariant words: an application of Rauzy fractals. RAIRO-Inf. Theor. Appl. 41 (2007), 329-349
- [4] P.Arnoux, Sturmian sequences. In: N. Pytheas Fogg, Substitutions in Dynamics, Arithmetics and Combinatorics Editors: Valérie Berthé, Sébastien Ferenczi, Christian Mauduit, Anne Siegel. Lecture Notes in Mathematics Volume 1794 (2002), Pages 143–198.
- [5] J. Berstel et P. Séébold, Morphismes de Sturm, Bull. Belg. Math. Soc. 1, (1994),175–189.
- [6] J. Berstel et P. Séébold, A remark on Sturmian words. Informatique théorique et applications 28 (1994),255–263.
- [7] N. Calkin, H.S. Wilf, Recounting the rationals, Amer. Math. Monthly 107 (2000), 4, 360-363.
- [8] J. Cassaigne, T. Harju and J. Karhumäki, On the undecidability of freeness of matrix semigroups, Internat. J. Algebra Comput. 9 (1999), 295-305.
- [9] S. Ito and S. Yasutomi, On continued fractions, substitutions and characteristic sequences, Japan. J. Math. 16 (1990), 287–306. MR 1091163 — Zbl 0721.11009
- [10] Douglas R. Hofstadter, ETA-LORE, unpublished manuscript. First presented at the Stanford Math. Club, Stanford, California (1963). Available from OEIS: https://oeis.org/A006336/a006336_1.pdf
- [11] D. Crisp; W. Moran; A. Pollington; P. Shiue, Substitution invariant cutting sequences, Journal de théorie des nombres de Bordeaux 5, (1993), p. 123–137.
- [12] M. Lothaire, Algebraic combinatorics of words, Cambridge University Press, Online publication date: April 2013 Print publication year: 2002.
- [13] Aldo de Luca, Standard Sturmian morphisms, Theoretical Computer Science 178 ( 1997), 205–224.
- [14] Aldo de Luca, Sturmian words: structure, combinatorics, and their arithmetics, Theoretical Computer Science 183 (1997), 45–82.
- [15] Johannes Kepler, “Harmonices mundi”, Book III, 1619.
- [16] Johannes Kepler with E.J. Aiton, A.M. Duncan, and J.V. Field, trans., The Harmony of the World (Philadelphia, Pennsylvania: American Philosophical Society, 1997)
- [17] C. Kimberling, P.J.C. Moses, The infinite Fibonacci tree and other trees generated by rules, Fibonacci Quarterly 52 (2014), 136–149.
- [18] D. A. Klarner, J.-C. Birget, and W. Satterfield. On the undecidability of the freeness of integer matrix semigroups. International Journal of Algebra and Computation 1(2) (1991), p.223-226.
- [19] T. Komatsu and A. J. van der Poorten, Substitution invariant Beatty sequences, Japan. J. Math 22, (1996), 349–354.
- [20] Lyndon, R. C.; Ullman, J. L. Pairs of real 2 -by- 2 matrices that generate free products. Michigan Math. J. 15 (1968), no. 2, 161–166.
- [21] L. Smolinsky, Features of a high school Olympiad problem, arXiv:1602.08028, 2016.
- [22] S.-I. Yasutomi, On Sturmian sequences which are invariant under some substitutions, in Number theory and its applications (Kyoto, 1997). Kluwer Acad. Publ., Dordrecht (1999) 347373.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
