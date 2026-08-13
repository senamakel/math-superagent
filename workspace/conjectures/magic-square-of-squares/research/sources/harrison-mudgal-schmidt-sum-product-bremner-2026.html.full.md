<!-- source: https://arxiv.org/html/2603.06483v1 | converted from HTML -->

Uniform sum-product phenomenon for algebraic groups and Bremner’s conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2603.06483v1 [math.NT] 06 Mar 2026

# Uniform sum-product phenomenon for algebraic groups and Bremner’s conjecture

Joseph Harrison, Akshat Mudgal, Harry Schmidt Address: Mathematics Institute, Zeeman Building, University of Warwick, Coventry CV4 7AL, United Kingdom Email address: [joseph.s.harrison@warwick.ac.uk][3] Email address: [Akshat.Mudgal@warwick.ac.uk][4] Email address: [Harry.Schmidt@warwick.ac.uk][5]

###### Abstract.

In this paper we combine methods from additive combinatorics and Diophantine geometry to study the generalised sum-product phenomenon in algebraic groups. As an application of this circle of ideas, we resolve a conjecture of Bremner on arithmetic progressions in coordinates of elliptic curves, along with various other generalisations studied in the literature.

We also prove a uniform Bourgain–Chang-type sum-product estimate for general 1 1 -dimensional algebraic groups G G over ℂ \mathbb{C}. Using these ideas, we provide an alternative solution to a problem of Bays–Breuillard. Furthermore, we show an Elekes–Szabó type result in the same setting for sets with small doubling, improving upon an earlier result of Bays–Breuillard when G G is not 𝔾 a \mathbb{G}_{a}. Our power saving here can be shown to be quantitatively optimal.

We use a combination of deep, classical results in Diophantine geometry due to David–Philippon, Laurent and Evertse–Schmidt–Schlickewei along with the recent breakthrough work on the weak Polynomial Freiman–Ruzsa conjecture over integers due to Gowers–Green–Manners–Tao.

###### Key words and phrases:

Bourgain–Chang sum-product result over algebraic groups, Bremner’s conjecture, Mordell–Lang, Freiman–Ruzsa theorem, Elekes–Szabó

###### 2020 Mathematics Subject Classification

11B13, 11B25, 11B30, 11G05

## 1. Introduction

Many questions in number theory concern an incongruence between two distinct arithmetic structures. Bremner [6] made this observation in the course of his investigations into the length of arithmetic progressions in the coordinates of the rational points of an elliptic curve. Here, additive structure, represented by an arithmetic progression, and the group structure on the elliptic curve should not correlate with each other, which led him to suspect that the length of a possible arithmetic progression should be bounded solely in terms of the rank of the curve. He confirmed his suspicions partly in work with Silverman and Tzanakis [4].

Another example of this phenomenon is the infamous sum–product conjecture in combinatorial number theory due to Erdős–Szemerédi [17]. This concerns expansion of finite sets of integers under the operation of taking sums or products, a manifestation of the incompatibility of additive and multiplicative structure. Progress towards this type of problem has led to a variety of applications in number theory and harmonic analysis.

A third example of this phenomenon concerns expansion of arbitrary sets of real numbers under sufficiently non-degenerate polynomial maps. This was first investigated by Elekes–Rónyai [12] and Elekes–Szabó [13], and since their work, this subject has seen significant activity, in part due to its connections to questions in combinatorial geometry and topics in model theory. In this paper, we unify these a priori disparate themes and prove effective, quantitative results regarding them.

We first turn towards the question of Bremner which concerns upper bounds on possible lengths of arithmetic progressions in the coordinates of the rational points of an elliptic curve. Replacing the additive structure by the multiplicative one, one may similarly suspect that the length of a geometric progression should be bounded, see work of Bremner–Ulas [5]. Another line of inquiry, in the same spirit, concerns the length of the longest sequence of consecutive squares in the coordinates of rational points on elliptic curves, see work of Kamel–Sadek [28].

As a straightforward consequence of the methods discussed in this article, we confirm Bremner’s speculation [6, §5] in the following general result.

###### Theorem 1.1.

There is an effectively computable constant C ≥ 1 C\geq 1 with the following property. Let E E be an elliptic curve in Weierstrass form

(1.1) |  | y 2 = x 3 + a ​ x + b, a, b ∈ ℚ, \displaystyle y^{2}=x^{3}+ax+b,\penalty\ \penalty\ a,b\in\mathbb{Q}, |  |

and let r r be the rank of E ⁡ ( ℚ) E(\mathbb{Q}). Let X = { x ⁡ ( P): P ∈ E ⁡ ( ℚ) } X=\{x(P):P\in E(\mathbb{Q})\} and Y = { y ⁡ ( P): P ∈ E ⁡ ( ℚ) } Y=\{y(P):P\in E(\mathbb{Q})\}. Let A A be either an arithmetic progression, a geometric progression or a set of the form

 | { u 2, ( u + d) 2, ( u + 2 ​ d) 2, …, ( u + d ​ l) 2 }, \{u^{2},(u+d)^{2},(u+2d)^{2},\dots,(u+dl)^{2}\}, |  |

with u, d ∈ ℚ u,d\in\mathbb{Q}, and l ∈ ℕ l\in\mathbb{N}. If A ⊆ X A\subseteq X or A ⊆ Y A\subseteq Y, then | A | ≤ C 1 + r |A|\leq C^{1+r}.

We note that the constant C C in Theorem 1.1 does not depend on a, b a,b, and for families of elliptic curves of bounded rank we obtain a uniform bound. It is to this day unclear whether there exist elliptic curves of arbitrary large rank. Recently, an elliptic curve of rank at least 29 was discovered [15, 16]. It is straightforward to see that Siegel’s theorem for S S -integral points [25, Theorem D.9.1] on elliptic curves implies that there can be no infinite arithmetic or geometric sequence or sequence of squares in E ⁡ ( ℚ) E(\mathbb{Q}). However, it does not provide a uniform bound, even for a fixed elliptic curve, since the number of primes that need inverting depends on the particular sequence.

For arithmetic progressions, Garcia–Fritz and Pasten [21] prove a bound of the form C 1 + r C^{1+r} with C C depending on E E but it is conceivable that their methods could lead to a uniform bound, had they used a uniform version of Mordell–Lang, e.g., [11]. However, for geometric progressions and consecutive squares no such general bounds seem to be known, even when allowing a dependence on E E. We prove a more general version of Theorem 1.1 (Corollary 2.2) for correspondences and finite rank groups that applies to a plethora of similar sequences. Theorem 1.1 can also be formulated in terms of rational points on a surface of general type in a high dimensional projective space. As a consequence we determine the Zariski closure of the rational points of certain projective surfaces (see Theorem A.1).

We now turn towards the sum-product phenomenon. Thus, given finite sets A, B ⊆ ℂ A,B\subseteq\mathbb{C}, we define the sumset and the product set as

 | A + B = { a + b: a ∈ A, b ∈ B } and A ⋅ B = { a b: a ∈ A, b ∈ B }. A+B=\{a+b:a\in A,b\in B\}\ \ \text{and}\ \ A\cdot B=\{ab:a\in A,b\in B\}. |  |

It is expected that if | A + A | |A+A| is small in terms of | A | |A|, then A A should be additively structured, and if | A ⋅ A | |A\cdot A| is small in terms of | A | |A|, then A A should be multiplicatively structured. Speculating that these two types of structures should not coexist simultaneously, Erdős–Szemerédi [17] conjectured that for any finite set A ⊆ ℂ A\subseteq\mathbb{C}, either A + A A+A or A ⋅ A A\cdot A must have size close to | A | 2 |A|^{2}. More generally, writing

 | g A = { a 1 + ⋯ + a g: a 1, …, a g ∈ A } and A ( g) = { a 1 … a g: a 1, …, a g ∈ A }, gA=\{a_{1}+\dots+a_{g}:a_{1},\dots,a_{g}\in A\}\ \ \text{and}\ \ A^{(g)}=\{a_{1}\dots a_{g}:a_{1},\dots,a_{g}\in A\}, |  |

for any g ∈ ℕ g\in\mathbb{N}, Erdős–Szemerédi conjectured the following.

###### Conjecture 1.2.

For any g ∈ ℕ g\in\mathbb{N}, any ε > 0 \varepsilon>0 and any set A ⊆ ℂ A\subseteq\mathbb{C}, one should have

 | max { | g A |, | A ( g) | } ≫ g, ε | A | g − ε. \max\{|gA|,|A^{(g)}|\}\gg_{g,\varepsilon}|A|^{g-\varepsilon}. |  |

A significant body of work addresses this conjecture, mostly focusing on the case when g = 2 g=2. Some of the highlights in this setting have been the works of Elekes [14] and Solymosi [42], who used geometric insights to provide short proofs of strong sum-product estimates. The current best known result here arises from some very recent work of Cushman [10], who employed incidence geometric and additive combinatorial methods to prove that

 | max { | 2 A |, | A ( 2) | } ≫ ε | A | 4 3 + 10 4407 − ε \max\{|2A|,|A^{(2)}|\}\gg_{\varepsilon}|A|^{\frac{4}{3}+\frac{10}{4407}-\varepsilon} |  |

for all sets A ⊆ ℝ A\subseteq\mathbb{R} and all ε > 0 \varepsilon>0.

One can interpret the sum-product phenomenon as a disruption of structure between two non-isogenous algebraic groups. Indeed, one can set 𝔾 m = ( ℂ ∗, ×) \mathbb{G}_{m}=(\mathbb{C}^{\ast},\times) and 𝔾 a = ( ℂ, +) \mathbb{G}_{a}=(\mathbb{C},+) and take 𝒞 \mathcal{C} to be the *correspondence*whose complex points are of the form ( x, x) (x,x) for x ∈ 𝔾 m ​ ( ℂ) x\in\mathbb{G}_{m}(\mathbb{C}). See §3 for a brief introduction about algebraic groups and correspondences between them. We let π 1: 𝒞 → 𝔾 m \pi_{1}:\mathcal{C}\to\mathbb{G}_{m} and π 2: 𝒞 → 𝔾 a \pi_{2}:\mathcal{C}\to\mathbb{G}_{a} be the standard projection maps. Given a finite set A ⊆ 𝔾 m ​ ( ℂ) A\subseteq\mathbb{G}_{m}(\mathbb{C}), we write

 | 𝒞 ⁡ ( A) = ⋃ x ∈ A π 2 ​ ( π 1 − 1 ​ ( x)). \mathcal{C}(A)=\bigcup_{x\in A}\pi_{2}(\pi_{1}^{-1}(x)). |  |

Note that 𝒞 ⁡ ( A) \mathcal{C}(A) is a subset of 𝔾 a ​ ( ℂ) \mathbb{G}_{a}(\mathbb{C}). The sum-product phenomenon is now equivalent to saying that for any finite A ⊆ 𝔾 m ​ ( ℂ) A\subseteq\mathbb{G}_{m}(\mathbb{C}), either | A + A | |A+A| or | 𝒞 ⁡ ( A) + 𝒞 ⁡ ( A) | |\mathcal{C}(A)+\mathcal{C}(A)| must be much larger than | A | |A|.

In a very nice paper, Bays–Breuillard [1] employed a model theoretic approach to generalise this circle of ideas to a much more broader family of algebraic groups. In particular, given 1 1 -dimensional, connected, non-isogenous algebraic groups G G and H H over ℂ \mathbb{C} and given some algebraic correspondence 𝒞 \mathcal{C} between G G and H H of degree d d, Bays--Breuillard 1 1 1 Bays–Breuillard [1] actually proved that for non-constant rational maps f 1: G → ℂ f_{1}:G\to\mathbb{C} and f 2: H → ℂ f_{2}:H\to\mathbb{C}, and all finite sets A ⊆ ℂ A\subseteq\mathbb{C}, one either has | f 1 − 1 ​ ( A) + f 1 − 1 ​ ( A) | ≥ c ​ | A | 1 + δ |f_{1}^{-1}(A)+f_{1}^{-1}(A)|\geq c|A|^{1+\delta} or | f 2 − 1 ​ ( A) + f 2 − 1 ​ ( A) | ≥ c ​ | A | 1 + δ |f_{2}^{-1}(A)+f_{2}^{-1}(A)|\geq c|A|^{1+\delta}, where c, δ > 0 c,\delta>0 are constants depending on G, H, f 1 G,H,f_{1} and f 2 f_{2}. This can be written in the framework of correspondences by considering the correspondence given by an irreducible component of { ( x, y) ∈ G × H: f 1 ​ ( x) = f 2 ​ ( y) } \{(x,y)\in G\times H:f_{1}(x)=f_{2}(y)\}. proved that there exists some δ = δ ⁡ ( G, H, 𝒞) > 0 \delta=\delta(G,H,\mathcal{C})>0 such that for any finite set A ⊆ G A\subseteq G, one has

(1.2) |  | max { | A + A |, | 𝒞 ( A) + 𝒞 ( A) | } ≫ G, H, C | A | 1 + δ. \max\{|A+A|,|\mathcal{C}(A)+\mathcal{C}(A)|\}\gg_{G,H,C}|A|^{1+\delta}. |  |

In contrast to the g = 2 g=2 setting of Conjecture 1.2, much less is known about the case when one requires *unbounded expansion*, that is, given any real number k > 1 k>1, one wishes to find some 1 ≤ g ≪ k 1 1\leq g\ll_{k}1 such that

(1.3) |  | max { | g A |, | A ( g) | } ≫ k | A | k \max\{|gA|,|A^{(g)}|\}\gg_{k}|A|^{k} |  |

holds for all finite sets A ⊆ ℂ A\subseteq\mathbb{C}. While incidence geometric methods seem to work quite effectively when k ≤ 2 k\leq 2, they do not seem to give any results when k > 2 k>2. In a breakthrough paper, Bourgain–Chang [3] employed intricate harmonic analytic techniques along with a clever arithmetic lemma to prove that ( 1.3) holds for all finite sets A ⊆ ℚ A\subseteq\mathbb{Q}. Their work was subsequently simplified and quantitatively improved by Pálvölgyi–Zhelezov [36], giving the best known bounds for g g in terms of k k for this problem. These ideas have since been extended by replacing the sumset g ​ A gA by other measures of additive structure. In particular, Hanson–Roche-Newton–Zhelezov [24] proved an analogue of ( 1.3) with the sumset g ​ A gA replaced by the shifted product set ( A + 1) ( g) (A+1)^{(g)}. This has been further generalised by the second author [35], who proved analogues of ( 1.3) with g ​ A gA first replaced by the sumset φ 1 ​ ( A) + ⋯ + φ g ​ ( A) \varphi_{1}(A)+\dots+\varphi_{g}(A) and then by the product set φ 1 ​ ( A) ​ … ​ φ g ​ ( A) \varphi_{1}(A)\dots\varphi_{g}(A), for suitably chosen polynomials φ 1, …, φ g ∈ ℤ ⁡ [x] \varphi_{1},\dots,\varphi_{g}\in\mathbb{Z}[x] with bounded degree.

All the aforementioned results in [3, 36, 24, 35] crucially employed properties about prime factorisation of integers, and subsequently do not generalise to sets of real numbers. In fact, an important problem in this area was to prove ( 1.3) for sets A ⊆ ℝ A\subseteq\mathbb{R}. Building on earlier work of Chang [7], the second author [34] utilised results from diophantine geometry to prove this conditionally on an infamous conjecture in additive combinatorics known as the weak polynomial Freiman–Ruzsa conjecture over ℤ \mathbb{Z}. The latter has now been resolved in the spectacular work of Gowers–Green–Manners–Tao [22].

Our main result on the generalised sum-product phenomenon is a Bourgain–Chang type unbounded expansion result in the vastly broader setting of 1-dimensional, connected algebraic groups over ℂ \mathbb{C}.

###### Theorem 1.3.

Given integers k ≥ 1 k\geq 1 and d ≥ 2 d\geq 2, there exists an integer g ≥ 1 g\geq 1 such that the following holds. Let G G and H H be algebraic groups of dimension 1 1, and let 𝒞 1, ⋯, 𝒞 g \mathcal{C}_{1},\cdots,\mathcal{C}_{g} be correspondences of degree d d between G G and H H. Suppose no 𝒞 i \mathcal{C}_{i} is a translate of an algebraic subgroup, and suppose that G G is not isomorphic to 𝔾 a \mathbb{G}_{a}. Then for all finite, non-empty sets A ⊆ G A\subseteq G, one has

 | max { | g A |, | 𝒞 1 ( A) + ⋯ + 𝒞 g ( A) | } ≫ d, k | A | k. \max\{|gA|,|\mathcal{C}_{1}(A)+\dots+\mathcal{C}_{g}(A)|\}\gg_{d,k}|A|^{k}. |  |

Setting G = 𝔾 m G=\mathbb{G}_{m} and H = 𝔾 a H=\mathbb{G}_{a}, we let 𝒞 i \mathcal{C}_{i} be given by the graph of the inclusion ℂ ∗ ↪ ℂ \mathbb{C}^{\ast}\hookrightarrow\mathbb{C}. The conclusion of Theorem 1.3 then immediately implies ( 1.3) for arbitrary finite sets A ⊆ ℂ A\subseteq\mathbb{C}. Similarly setting G = 𝔾 m G=\mathbb{G}_{m} and H = 𝔾 m H=\mathbb{G}_{m} or 𝔾 a \mathbb{G}_{a} and setting 𝒞 i \mathcal{C}_{i} to be given by the graph of ( x, φ i ​ ( x)) (x,\varphi_{i}(x)) in G × H G\times H for suitably chosen polynomials φ 1, …, φ g \varphi_{1},\dots,\varphi_{g} delivers the following corollary.

###### Corollary 1.4.

For all integers k ≥ 2 k\geq 2, there exists an integer g ≥ 2 g\geq 2 such that the following holds. For any non-constant φ 1, …, φ g ∈ ℂ ⁡ [x] \varphi_{1},\dots,\varphi_{g}\in\mathbb{C}[x] with degree at most d d and any finite set A ⊆ ℂ A\subseteq\mathbb{C}, one has

 | max { | A ( g) |, | φ 1 ( A) + ⋯ + φ g ( A) | } ≫ d, k | A | k. \max\{|A^{(g)}|,|\varphi_{1}(A)+\dots+\varphi_{g}(A)|\}\gg_{d,k}|A|^{k}. |  |

Moreover, if each φ i ​ ( x) \varphi_{i}(x) for 1 ≤ i ≤ g 1\leq i\leq g is not of the form a ​ x n ax^{n} for any a ∈ ℂ a\in\mathbb{C} and any n ∈ ℕ n\in\mathbb{N}, then we also have

 | max { | A ( g) |, | φ 1 ( A) … φ g ( A) | } ≫ d, k | A | k. \max\{|A^{(g)}|,|\varphi_{1}(A)\dots\varphi_{g}(A)|\}\gg_{d,k}|A|^{k}. |  |

This recovers the results of [24, 35] qualitatively in the much more general setting where A ⊆ ℂ A\subseteq\mathbb{C} instead of A ⊆ ℚ A\subseteq\mathbb{Q} and the polynomials φ 1, …, φ g \varphi_{1},\dots,\varphi_{g} are allowed to have complex coefficients instead of rational coefficients. We defer further applications of our methods, including an alternative proof of a conjecture of Bays–Breuillard, to § 2.

We also consider problems concerning expansion in the image set of polynomials as well as intersection of varieties with discrete boxes in algebraic groups. This relates to Elekes–Szabó and Elekes–Rónyai type problems. We briefly describe the former, and so, given n ≥ 3 n\geq 3 and some polynomial P ∈ ℂ ⁡ [x 1, …, x n] P\in\mathbb{C}[x_{1},\dots,x_{n}], when is it the case that for any finite, non-empty set A ⊆ ℂ A\subseteq\mathbb{C}, one has

(1.4) |  | | { ( a 1, …, a n) ∈ A n: P ⁡ ( a 1, …, a n) = 0 } | ≪ | A | n − 1 − η |\{(a_{1},\dots,a_{n})\in A^{n}:P(a_{1},\dots,a_{n})=0\}|\ll|A|^{n-1-\eta} |  |

for some constant η > 0 \eta>0? Such a characterisation was first studied by Elekes–Szabó [13], and since then, has seen a flurry of activity, in part due to its connections to a variety of combinatorial geometric problems [38, 37, 41] as well as to model theoretic results [9, 1, 8].

In their aforementioned work, Bays–Breuillard [1] introduced a model theoretic approach to this question, thus generalising the above results for irreducible algebraic sets in ℂ n \mathbb{C}^{n}. They further noted that upon restricting to a special family of sets A ⊆ ℂ A\subseteq\mathbb{C}, one can obtain power saving of the shape ( 1.4) for a much broader collection of varieties. In particular, in the setting of a 1 1 -dimensional, complex, connected algebraic group G G, they proved that for any subvariety 𝒱 ⊆ G n \mathcal{V}\subseteq G^{n} which is not a coset of a subgroup, there exist constants ε, η > 0 \varepsilon,\eta>0 depending only on G G and 𝒱 \mathcal{V} such that for any finite set A ⊆ G A\subseteq G satisfying | A + A | ≤ | A | 1 + ε |A+A|\leq|A|^{1+\varepsilon}, one has

(1.5) |  | | A n ∩ 𝒱 | ≪ G, 𝒱 | A | dim ( 𝒱) − η. |A^{n}\cap\mathcal{V}|\ll_{G,\mathcal{V}}|A|^{\dim(\mathcal{V})-\eta}. |  |

It is natural to ask what is the best possible value of η \eta that is admissible in ( 1.5). When G G is not isomorphic to 𝔾 a \mathbb{G}_{a}, we resolve this question.

###### Theorem 1.5.

Let G G be a connected algebraic group over ℂ \mathbb{C} of dimension 1 1. Suppose that G G is not isomorphic to 𝔾 a \mathbb{G}_{a}. Let A ⊆ G A\subseteq G be a finite set such that | A + A | ≤ K ​ | A | |A+A|\leq K|A| for some K ≥ 1 K\geq 1. Then for any irreducible subvariety 𝒱 ⊆ G g \mathcal{V}\subseteq G^{g}, that is not a translate of an algebraic subgroup of G g G^{g}, one has

 | | 𝒱 ∩ A g | ≪ g, deg ⁡ ( 𝒱) K C + | A | dim ( 𝒱) − 1, \displaystyle|\mathcal{V}\cap A^{g}|\ll_{g,\deg(\mathcal{V})}K^{C}+|A|^{\dim(\mathcal{V})-1}, |  |

where C > 0 C>0 is some constant depending only on deg ⁡ ( 𝒱) \deg(\mathcal{V}) and g g.

In particular, when G G is not isomorphic to 𝔾 a \mathbb{G}_{a} and 𝒱 \mathcal{V} is not a translate of an algebraic subgroup, there exists some ε > 0 \varepsilon>0 depending only on 𝒱 \mathcal{V} and g g, such that whenever | A + A | ≤ | A | 1 + ε |A+A|\leq|A|^{1+\varepsilon}, one has

 | | 𝒱 ∩ A g | ≪ g, deg ⁡ ( 𝒱) | A | dim ( 𝒱) − 1. |\mathcal{V}\cap A^{g}|\ll_{g,\deg(\mathcal{V})}|A|^{\dim(\mathcal{V})-1}. |  |

We further note that this upper bound is of the right order.

###### Example 1.6.

Let G = 𝔾 m G=\mathbb{G}_{m} and g = 3 g=3. The variety 𝒱 \mathcal{V} defined by the polynomial

(1.6) |  | P ⁡ ( X 1, X 2, X 3) = X 2 ​ X 3 − X 1 + 1 P(X_{1},X_{2},X_{3})=X_{2}X_{3}-X_{1}+1 |  |

contains the translates X 2 ​ X 3 = γ, X 1 = γ + 1 X_{2}X_{3}=\gamma,X_{1}=\gamma+1 of the algebraic subgroup X 2 ​ X 3 = 1, X 1 = 1 X_{2}X_{3}=1,X_{1}=1, for any γ ∉ { − 1, 0 } \gamma\not\in\{-1,0\}. Setting

 | A = { γ i: − N ≤ i ≤ N } ∪ { γ + 1 }, A=\{\gamma^{i}:-N\leq i\leq N\}\cup\{\gamma+1\}, |  |

it is easy to see that for all N ≥ 3 N\geq 3, we have | 𝒱 ∩ A 3 | ≫ | A | |\mathcal{V}\cap A^{3}|\gg|A| and | A ⋅ A | ≤ 3 ​ | A | |A\cdot A|\leq 3|A|. However, 𝒱 \mathcal{V} is not a translate of an algebraic subgroup.

In fact, our methods deliver even stronger upper bounds that depend on the largest dimension of a maximal translate of an algebraic subgroup contained in 𝒱 \mathcal{V}, see Theorem 2.6 for further details.

We also note that while previous approaches to Elekes–Szabó type problems employed combinatorial geometric methods or model theory, our own approach utilises a novel interaction between Mordell–Lang and S S -unit type results along with recent developments in additive combinatorics involving Freiman–Ruzsa type results.

One can similarly consider expansion in the image set of polynomials, that is, given some polynomial P ∈ ℂ ⁡ [x 1, …, x n] P\in\mathbb{C}[x_{1},\dots,x_{n}] and some finite set A ⊆ ℂ A\subseteq\mathbb{C}, when is the set

 | P ( A, …, A) = { P ( a 1, …, a n): a 1, …, a n ∈ A } P(A,\dots,A)=\{P(a_{1},\dots,a_{n}):a_{1},\dots,a_{n}\in A\} |  |

significantly larger than A A. The first result in this direction is due to Elekes–Rónyai [12] who proved that either P ∈ ℂ ⁡ [x, y] P\in\mathbb{C}[x,y] is degenerate, in the sense that P = h ⁡ ( f ⁡ ( x) + g ⁡ ( y)) P=h(f(x)+g(y)) or P = h ⁡ ( f ⁡ ( x) ​ g ​ ( y)) P=h(f(x)g(y)) for some univariate polynomials f, g, h f,g,h, or one has | P ⁡ ( A, A) | ≫ | A | 1 + η |P(A,A)|\gg|A|^{1+\eta} for every finite A ⊆ ℂ A\subseteq\mathbb{C}, with η > 0 \eta>0 being an absolute constant. There have been various subsequent quantitative improvements, as well as explorations of cases where, as before, one restricts to a special family of sets A A in order to widen the choices for P P and get better quantitative values of η \eta, see [1, 26, 34] as well as [24, 35] for related sum-product type problems.

Our main result in this direction is a significant generalisation of the above result in the wider setting of algebraic groups. In order to state this, we will need the following definition.

###### Definition 1.7.

Let G G be a 1 1 -dimensional, connected algebraic group over ℂ \mathbb{C}, and let ℬ \mathcal{B} be a projective variety of positive dimension. Let π 1: G g × ℬ → G g \pi_{1}:G^{g}\times\mathcal{B}\to G^{g} and π 2: G g × ℬ → ℬ \pi_{2}:G^{g}\times\mathcal{B}\to\mathcal{B} be the canonical projection maps. We call an irreducible subvariety 𝒱 ⊆ G g × ℬ \mathcal{V}\subseteq G^{g}\times\mathcal{B}*degenerate*, if there exists a connected algebraic group H ⊆ G g H\subseteq G^{g} of positive dimension, and a proper subvariety 𝒲 ⊊ G g / H × ℬ \mathcal{W}\subsetneq G^{g}/H\times\mathcal{B} such that

 | 𝒱 = π H − 1 ​ ( 𝒲), \mathcal{V}=\pi_{H}^{-1}(\mathcal{W}), |  |

for the projection π H: G g × ℬ → G g / H × ℬ \pi_{H}:G^{g}\times\mathcal{B}\rightarrow G^{g}/H\times\mathcal{B}. If 𝒱 \mathcal{V} is not degenerate, we call 𝒱 \mathcal{V} non-degenerate.

An example of a degenerate subvariety is given by the equation P ⁡ ( X 1, X 2, X 3) = t P(X_{1},X_{2},X_{3})=t, where P P is given by ( 1.6). An example of a non-degenerate subvariety is provided after the statement of Theorem 1.8 below.

With this in hand, we state our result as follows.

###### Theorem 1.8.

Let G, ℬ, π 1 G,\mathcal{B},\pi_{1} and π 2 \pi_{2} be as in Definition 1.7, with G G not isomorphic to 𝔾 a \mathbb{G}_{a}. Let 𝒱 ⊆ G g × ℬ \mathcal{V}\subseteq G^{g}\times\mathcal{B} be non-degenerate of dimension g g and degree d d, and such that π 1 \pi_{1} and π 2 \pi_{2} restricted to 𝒱 \mathcal{V} are dominant. Let A ⊆ G A\subseteq G be a finite, non-empty set such that | A + A | ≤ K ​ | A | |A+A|\leq K|A|. Then for all X ⊆ A X\subseteq A, we have

(1.7) |  | | π 2 ( ( X g × ℬ) ∩ 𝒱) | ≫ d, g | X | g K O d, g ​ ( 1). |\pi_{2}((X^{g}\times\mathcal{B})\cap\mathcal{V})|\gg_{d,g}\frac{|X|^{g}}{K^{O_{d,g}(1)}}. |  |

As an example, one may set G = 𝔾 m, B = ℙ 1 G=\mathbb{G}_{m},B=\mathbb{P}^{1} and the variety 𝒱 \mathcal{V} to be defined by the equation P ⁡ ( x 1, …, x g) = t P(x_{1},\dots,x_{g})=t, where P ∈ ℂ ⁡ [x 1, …, x g] P\in\mathbb{C}[x_{1},\dots,x_{g}] is some polynomial. We refer to P P as *non-degenerate*with respect to G g G^{g} if the variety 𝒱 \mathcal{V} is non-degenerate. One can see that this is equivalent to the fact that P ⁡ ( 𝒙) ≠ F ⁡ ( m 1 ​ ( 𝒙), …, m g − 1 ​ ( 𝒙)) P(\bm{x})\neq F(m_{1}(\bm{x}),\dots,m_{g-1}(\bm{x})) for any choice of monomials m 1, …, m g − 1 ∈ ℂ ⁡ [x 1, …, x g] m_{1},\dots,m_{g-1}\in\mathbb{C}[x_{1},\dots,x_{g}] and any F ∈ ℂ ⁡ [y 1, …, y g − 1] F\in\mathbb{C}[y_{1},\dots,y_{g-1}]. In this case, we have

 | π 2 ​ ( ( A g × ℬ) ∩ 𝒱) = P ⁡ ( A, …, A). \pi_{2}((A^{g}\times\mathcal{B})\cap\mathcal{V})=P(A,\dots,A). |  |

Thus ( 1.7) implies that for any finite set A ⊆ ℂ ∗ A\subseteq\mathbb{C}^{*} satisfying | A ⋅ A | ≤ K ​ | A | |A\cdot A|\leq K|A|, one has

(1.8) |  | | P ( A, …, A) | ≫ d, g | A | g K O d, g ​ ( 1). |P(A,\dots,A)|\gg_{d,g}\frac{|A|^{g}}{K^{O_{d,g}(1)}}. |  |

The lower bound in ( 1.8) was proved in [34] conditional on the weak PFR conjecture over ℤ \mathbb{Z}. In fact, Theorem 1.8 can be seen as a generalisation of the results from [34] to the much broader setting of varieties in 1 1 -dimensional algebraic groups over ℂ \mathbb{C}.

Apart from having applications to various sum-product type questions, a nice aspect of this notion of degeneracy is that it is optimal. In particular, if a polynomial P P is degenerate in the above sense, then [34, Proposition 1.2] implies that for any finite A ⊊ ℤ A\subsetneq\mathbb{Z} with | A ⋅ A | ≤ K ​ | A | |A\cdot A|\leq K|A| one has

 | | P ( A, …, A) | ≪ P K O P ​ ( 1) | A | g − 1. |P(A,\dots,A)|\ll_{P}K^{O_{P}(1)}|A|^{g-1}. |  |

Furthermore, the lower bound in ( 1.7) is almost optimal in the sense that it matches the trivial upper bound | X | g |X|^{g} up to factors of K O d, g ​ ( 1) K^{O_{d,g}(1)}.

We note that in some of our results, including Theorem 1.8, we assume that the algebraic group G G is not isomorphic to 𝔾 a \mathbb{G}_{a}. In fact, this is a necessary condition for many of these to hold. For example, Theorem 1.8 is not true for the case when G = 𝔾 a G=\mathbb{G}_{a}.

###### Example 1.9.

Let P ⁡ ( x, y, z) = x ​ y + y ​ z + z ​ x P(x,y,z)=xy+yz+zx. One can show that this polynomial is non-degenerate with respect to 𝔾 a 3 \mathbb{G}_{a}^{3}, see Appendix B. Moreover, the set A = { 1, 2, …, N } A=\{1,2,\dots,N\} is a subset of 𝔾 a \mathbb{G}_{a} with | A + A | ≤ 2 ​ | A | |A+A|\leq 2|A|. Finally, | P ⁡ ( A, A, A) | ≪ N 2 = | A | 2 |P(A,A,A)|\ll N^{2}=|A|^{2} implying that a conclusion akin to ( 1.8) in this case fails to hold true.

It is worth mentioning that Theorem 1.8 can be employed to prove its counterpart where we replace the condition that A A has a small sumset with A A lying in a subgroup of small rank, see Theorem 4.2. In particular, given some subgroup Γ ⊆ G \Gamma\subseteq G of rank r r and some finite set Y ⊆ Γ Y\subseteq\Gamma, Theorem 1.8 implies that one must have

(1.9) |  | | π 2 ( ( Y g × ℬ) ∩ 𝒱) | ≫ d, g | Y | g 2 O d, g ​ ( r). |\pi_{2}((Y^{g}\times\mathcal{B})\cap\mathcal{V})|\gg_{d,g}\frac{|Y|^{g}}{2^{O_{d,g}(r)}}. |  |

Indeed, let Γ \Gamma be generated by γ 1, …, γ r \gamma_{1},\dots,\gamma_{r}. Now, given any finite set Y ⊆ Γ Y\subseteq\Gamma, we can find some L ∈ ℕ L\in\mathbb{N} such that Y ⊆ A Y\subseteq A, where A = { n 1 γ 1 + ⋯ + n r γ r: | n 1 |, …, | n r | ≤ L } A=\{n_{1}\gamma_{1}+\dots+n_{r}\gamma_{r}:|n_{1}|,\dots,|n_{r}|\leq L\}. Moreover, note that | A + A | ≤ 2 r ​ | A | |A+A|\leq 2^{r}|A|. We may now apply Theorem 1.8 to obtain ( 1.9). Furthermore, this means that we may deduce Theorem 1.1 and its generalisation Corollary 2.2 via a combination of inequality ( 1.9) and Proposition 5.1.

An important step towards proving our results is that the above implication can be roughly reversed as well. We perform this reversal by combining the recent resolution of the weak polynomial Freiman–Ruzsa conjecture due to Gowers–Green–Manners–Tao [22] along with various additive combinatorial techniques and the fact that a finite subgroup of an algebraic group has a uniformly bounded number of generators, which is a simple consequence of its Lie theory.

Thus, it suffices to work in the setting where our sets are lying in subgroups of bounded rank. One of our key results here is Theorem 4.2, whose conclusion is also recorded in ( 1.9). This is where a significant portion of our input from Diophantine geometry comes in, including utilisation of a uniform version of Mordell–Lang by David–Philippon [11] and the S S -unit bounds by Evertse–Schlickewei–Schmidt [18].

A third step that is required to prove our sum-product results such as Theorem 1.3, involves showing that an auxiliary variety, which captures the movement of additive structure through the correspondences, is non-degenerate in the sense of Definition 1.7. This is precisely the content of Proposition 5.1. For the proof, which can be found in section 5, we work on the tangent space of our algebraic groups. We note that Proposition 5.1, when combined with Theorem 4.2, implies a suitable variant of Theorem 1.3 which holds for sets contained in finite rank subgroups, see Theorem 2.1. The latter is already sufficient for our applications to Bremner’s conjecture.

There is little doubt in the authors minds that the slick interaction of Diophantine geometry with additive combinatorics that is apparent here seems to suggest that correspondences between algebraic groups present a very suitable framework to conceptualise the sum-product phenomenon. One way of viewing this interaction is that the weak polynomial Freiman–Ruzsa conjecture over ℤ \mathbb{Z} is a statement concerning simply addition in ℤ r \mathbb{Z}^{r}. The latter can be embedded into algebraic groups via rank r r groups in a myriad ways. This is combined with the algebraic structure that is implicitly present in 𝔾 a, 𝔾 m \mathbb{G}_{a},\mathbb{G}_{m} and elliptic curves. Ultimately, the Mordell–Lang conjecture tells us how the group arithmetic interacts with the Zariski-topology of the groups. This is especially convincing, if we remember the special role played by isogenies as these are precisely the maps that respect both the algebraic and the group structure. Any correspondence that is not a translate of an algebraic subgroup should destroy the approximate group structure of any finite set as it transports the set from one group law to another.

### Outline

We will present some further applications of our ideas in § 2. We use § 3 to give a brief introduction about algebraic groups and correspondences, as well as record some consequences of the uniform version of Mordell–Lang by David–Philippon [11] and the S S -unit bounds by Evertse–Schlickewei–Schmidt [18]. We dedicate § 4 to proving Theorem 4.2, and in § 5, we will prove Proposition 5.1. We use § 6 to prove the additive combinatorial structural results that we require for the proofs of our results. Finally in § 7, we provide all the proofs of our results from § 1 and § 2. In Appendix A, we give some applications of our results to Diophantine equations. Moreover, we make some brief remarks about properties of degenerate polynomials in Appendix B.

### Notation

We use Vinogradov notation. Thus we write X ≪ z Y X\ll_{z}Y to mean that | X | ≤ C ​ Y |X|\leq CY where C > 0 C>0 is some constant depending on the parameter z z. We write X = O ⁡ ( Y) X=O(Y) to mean X ≪ Y X\ll Y, and we write X ≍ Y X\asymp Y to mean X ≪ Y ≪ X X\ll Y\ll X. We will often write A ⊆ G A\subseteq G for a finite set A A and an algebraic group G G. In this case we identify (by abuse of notation) A A with a 0-dimensional algebraic subvariety consisting of the points of A A with multiplicity 1.

### Acknowledgements

The second author is supported by a Leverhulme early career fellowship ECF-2025-148.

## 2. Further Applications

### 2.1. Generalised Bremner

We mention a generalised version of Theorem 1.1 for correspondences between algebraic groups. We first record an expansion version for correspondences.

###### Theorem 2.1.

For all integers d ≥ 1 d\geq 1 and g ≥ 2 g\geq 2, there is a positive constant 0 < c ⁡ ( d, g) < 1 0<c(d,g)<1 with the following property. Let 𝒞 1, ⋯, 𝒞 g \mathcal{C}_{1},\cdots,\mathcal{C}_{g} be correspondences of degree d d between algebraic groups G G and H H of dimension 1. Suppose no 𝒞 i \mathcal{C}_{i} is a translate of an algebraic subgroup and that G G is not isomorphic to the additive group 𝔾 a \mathbb{G}_{a}. Let Γ ⊆ G ⁡ ( ℂ) \Gamma\subseteq G(\mathbb{C}) be a subgroup of finite rank r r. Then for any finite subset A ⊆ Γ A\subseteq\Gamma, one has

 | | 𝒞 1 ​ ( A) + ⋯ + 𝒞 g ​ ( A) | ≥ c ​ ( d, g) 1 + r ​ | A | g. |\mathcal{C}_{1}(A)+\cdots+\mathcal{C}_{g}(A)|\geq c(d,g)^{1+r}|A|^{g}. |  |

We note that the theorem is slightly asymmetric as we can not allow G G to be isomorphic to 𝔾 a \mathbb{G}_{a}. This is indeed necessary as for example Γ = ℤ \Gamma=\mathbb{Z}, H = 𝔾 m H=\mathbb{G}_{m} and Δ \Delta the diagonal as described above shows that if we drop that assumption that would imply that any set in ℤ \mathbb{Z} has big product set, which is wrong.

It is also worth noting that fixing an elliptic curve E E over a number field K K, there are only finitely many elliptic curves over K K, that are isogenous to it, even over an algebraic closure. This is a consequence of Faltings’s famous theorem [19], later significantly improved by Masser–Wüstholz [31], which shows that, even for a fixed number field, our theorems apply to a vast zoo of non-isogenous algebraic groups.

Given k ∈ ℕ k\in\mathbb{N}, we define a *proper generalised arithmetic progression of rank k k*to be a set P P of the form

(2.1) |  | P = { P 0 + ℓ 1 ​ P 1 + ⋯ + ℓ k ​ P k: 0 ≤ ℓ i ≤ L i − 1 }, P=\{P_{0}+\ell_{1}P_{1}+\cdots+\ell_{k}P_{k}\ :\ 0\leq\ell_{i}\leq L_{i}-1\}, |  |

where P 0, …, P k ∈ H P_{0},\dots,P_{k}\in H and L 1, …, L k ≥ 2 L_{1},\dots,L_{k}\geq 2 are integers and one has | P | = L 1 ​ … ​ L k |P|=L_{1}\dots L_{k}. These sets play a crucial role in additive combinatorics and number theory since they act as an important family of sets that exhibit additive structure. With this in hand, we now prove our main result on Bremner’s conjecture and related questions.

###### Corollary 2.2.

For all integers d ≥ 1 d\geq 1 there exists a constant D = D ⁡ ( d) D=D(d) with the following property. Let G G be either 𝔾 m \mathbb{G}_{m} or an elliptic curve E E, and let 𝒞 \mathcal{C} be a correspondence of degree at most d d between G G and an algebraic group H H of dimension 1, that is not the translate of an algebraic subgroup. Then for any subgroup Γ ⊆ G ⁡ ( ℂ) \Gamma\subseteq G(\mathbb{C}) of rank r r, a proper generalised arithmetic progression P P of rank k k in 𝒞 ⁡ ( Γ) \mathcal{C}(\Gamma) satisfies

 | | P | ≤ D 1 + r. |P|\leq D^{1+r}. |  |

Theorem 1.1 follows in a straightforward manner from the above result, see § 7. Corollary 2.2 also gives a more general and uniform version of [21, Theorem 6.1].

A nice aspect of our upper bound is that it is completely independent of the rank k k of the progression. Moreover, generalised arithmetic progressions are indeed a strictly more general pattern. For example, the generalised arithmetic progression P ′ P^{\prime} as described in ( 2.1) can not be covered by fewer than C k C^{k} arithmetic progressions, for some constant C > 1 C>1, but we still obtain a uniform upper bound of the form | P ′ | ≤ D 1 + r |P^{\prime}|\leq D^{1+r} for some 0 < D ≪ d 1 0<D\ll_{d}1 which is independent of k k.

### 2.2. Sum-product phenomenon

Returning to the generalised sum-product phenomenon, Bays–Breuillard [1] speculated that the exponent δ \delta in their result recorded in ( 1.2) should be independent of G G and H H. Significantly generalising this model-theoretic and incidence-geometric framework, Chernikov–Peterzil–Starchenko [8] confirmed the speculation of Bays–Breuillard in a quantitative sense. In particular, they proved that δ = 1 / 21 \delta=1/21 is admissible in ( 1.2). As an application of our methods, we prove an asymmetric, uniform version of ( 1.2), thus confirming the speculation of Bays–Breuillard via a very different set of techniques.

###### Theorem 2.3.

Given d ∈ ℕ d\in\mathbb{N}, there exists some constant D = D ⁡ ( d) > 0 D=D(d)>0 such that the following is true. Let δ > 0 \delta>0, let G G and H H be connected algebraic groups of dimension 1 with G G not isomorphic to 𝔾 a \mathbb{G}_{a}, and let 𝒞 \mathcal{C} be an algebraic correspondence between G G and H H of degree d ≥ 2 d\geq 2 that is not the translate of an algebraic subgroup. Then for any finite, non-empty set A ⊆ G A\subseteq G, one has either

(2.2) |  | | A + A | > | A | 1 + δ or | 𝒞 ⁡ ( A) + 𝒞 ⁡ ( A) | ≥ D − 1 ​ | A | 2 − D ​ δ. |A+A|>|A|^{1+\delta}\ \ \text{or}\ \ |\mathcal{C}(A)+\mathcal{C}(A)|\geq D^{-1}|A|^{2-D\delta}. |  |

Indeed, Theorem 2.3 implies that δ = 1 / ( D + 1) \delta=1/(D+1) is admissible in ( 1.2). While this choice of δ \delta is much smaller than 1 / 21 1/21, the main novelty of our result lies in the asymmetry between the lower bounds for | A + A | |A+A| and | 𝒞 ⁡ ( A) + 𝒞 ⁡ ( A) | |\mathcal{C}(A)+\mathcal{C}(A)| in ( 2.2). For instance, if we set G = 𝔾 m G=\mathbb{G}_{m} and H = 𝔾 a H=\mathbb{G}_{a} or 𝔾 m \mathbb{G}_{m} and the correspondence 𝒞 \mathcal{C} to be given by the graph of y = φ ⁡ ( x) y=\varphi(x) for some suitable polynomial φ ∈ ℂ ⁡ [x] \varphi\in\mathbb{C}[x], we obtain the following corollary.

###### Corollary 2.4.

Let A ⊆ ℂ A\subseteq\mathbb{C} be a finite set, let d ≥ 1 d\geq 1 be an integer, let K ≥ 1 K\geq 1 and let φ ∈ ℂ ⁡ [x] \varphi\in\mathbb{C}[x] have deg ⁡ φ = d \deg\varphi=d. If | A ⋅ A | ≤ K ​ | A | |A\cdot A|\leq K|A|, then

(2.3) |  | | φ ( A) + φ ( A) | ≫ d | A | 2 / K D |\varphi(A)+\varphi(A)|\gg_{d}|A|^{2}/K^{D} |  |

where D > 0 D>0 is some constant depending on d d. Moreover, if φ ⁡ ( x) \varphi(x) is not of the form c ​ x d cx^{d} for any c ∈ ℂ c\in\mathbb{C}, then we also have

 | | φ ( A) ⋅ φ ( A) | ≫ d | A | 2 / K D. |\varphi(A)\cdot\varphi(A)|\gg_{d}|A|^{2}/K^{D}. |  |

We note that simply setting φ = x \varphi=x in ( 2.3) immediately delivers the so-called weak Erdős–Szemerédi Conjecture over ℂ \mathbb{C}. This was first proven by Bourgain–Chang [3] for sets A ⊆ ℚ A\subseteq\mathbb{Q}, with work of Chang [7] delivering this conclusion for sets A ⊆ ℝ A\subseteq\mathbb{R}, conditional on the weak PFR conjecture over ℤ \mathbb{Z}. Building on the work of Chang and employing the resolution of the weak PFR conjecture over ℤ \mathbb{Z} due to Gowers–Green–Manners–Tao [22], the second author proved that for any finite set A ⊊ ℂ A\subsetneq\mathbb{C} with | A ⋅ A | ≤ K ​ | A | |A\cdot A|\leq K|A|, one has at most | A | 2 / K O ⁡ ( 1) |A|^{2}/K^{O(1)} many quadruples a 1, …, a 4 ∈ A a_{1},\dots,a_{4}\in A such that a 1 + a 2 = a 3 + a 4 a_{1}+a_{2}=a_{3}+a_{4}, see [33, Proposition 1.5]. This then immediately implies that | A + A | ≥ | A | 2 / K O ⁡ ( 1) |A+A|\geq|A|^{2}/K^{O(1)}.

### 2.3. Elekes–Szabó

As remarked in §1, we are able to prove a more general upper bound for quantities of the form | 𝒱 ∩ A g | |\mathcal{V}\cap A^{g}| which depend on the maximal dimension of a translate of an algebraic subgroup contained in 𝒱 \mathcal{V}. In order to elaborate on this, we present the following definition.

###### Definition 2.5.

For an irreducible subvariety 𝒱 ⊆ G g \mathcal{V}\subseteq G^{g}, we define the coset defect, denoted codef ​ ( 𝒱) \text{codef}(\mathcal{V}), to be the maximal dimension of a connected algebraic group H ⊆ G g H\subseteq G^{g}, such that γ + H ⊆ 𝒱 \gamma+H\subseteq\mathcal{V} for some γ ∈ G g ​ ( ℂ) \gamma\in G^{g}(\mathbb{C}).

With this in hand, we state our result.

###### Theorem 2.6.

Let G G be a 1 1 -dimensional, connected algebraic group over ℂ \mathbb{C} not isomorphic to 𝔾 a \mathbb{G}_{a}. Let A ⊆ G A\subseteq G be a finite set such that | A + A | ≤ K ​ | A | |A+A|\leq K|A| for some K ≥ 1 K\geq 1. Then for any irreducible subvariety 𝒱 ⊆ G g \mathcal{V}\subseteq G^{g}, one has

 | | 𝒱 ∩ A g | ≪ g, deg ⁡ ( 𝒱) ( K C + | A | codef ⁡ ( 𝒱)), \displaystyle|\mathcal{V}\cap A^{g}|\ll_{g,\deg(\mathcal{V})}(K^{C}+|A|^{{\rm codef}(\mathcal{V})}), |  |

where the constant C > 0 C>0 depends only on deg ⁡ ( 𝒱) \deg(\mathcal{V}) and g g.

We note that 𝒱 \mathcal{V} might be covered by translates of algebraic subgroups even though 𝒱 \mathcal{V} is not a translate of an algebraic subgroup. However, Theorem 2.6 still applies to such varieties. For example, for g = 3 g=3 the variety 𝒱 \mathcal{V} defined by X 1 ​ X 2 2 ​ X 3 − X 2 ​ X 3 − 1 = 0 X_{1}X_{2}^{2}X_{3}-X_{2}X_{3}-1=0 is not a coset, but is covered by cosets of the form X 2 ​ X 3 = γ, X 1 ​ X 2 = ( 1 + γ) / γ X_{2}X_{3}=\gamma,X_{1}X_{2}=(1+\gamma)/\gamma for γ ∈ ℂ ∖ { − 1, 0 } \gamma\in\mathbb{C}\setminus\{-1,0\}. Theorem 2.6 admits the following corollary.

###### Corollary 2.7.

For every d, g ≥ 1 d,g\geq 1 there exists ϵ > 0 \epsilon>0, such that for an irreducible variety 𝒱 ⊆ G g \mathcal{V}\subseteq G^{g} of degree at most d d, if | A + A | ≤ | A | 1 + ϵ |A+A|\leq|A|^{1+\epsilon} and codef ⁡ ( 𝒱) ≥ 1 {\rm codef}(\mathcal{V})\geq 1, then

(2.4) |  | | A g ∩ 𝒱 | ≪ g, deg ⁡ ( 𝒱) | A | codef ⁡ ( 𝒱). \displaystyle|A^{g}\cap\mathcal{V}|\ll_{g,\deg(\mathcal{V})}|A|^{{\rm codef}(\mathcal{V})}. |  |

Finally, if 𝒱 \mathcal{V} does not contain a positive dimensional coset, then for every ϵ > 0 \epsilon>0, if | A + A | ≤ | A | 1 + ϵ |A+A|\leq|A|^{1+\epsilon}, then

 | | 𝒱 ∩ A g | ≪ g, deg ⁡ ( 𝒱) | A | C ​ ϵ, |\mathcal{V}\cap A^{g}|\ll_{g,\deg(\mathcal{V})}|A|^{C\epsilon}, |  |

where C > 0 C>0 is some constant depending on deg ⁡ ( 𝒱) \deg(\mathcal{V}) and g g.

As in the case of Theorem 1.5 and Example 1.6, one can show that the upper bounds in Theorem 2.6 and inequality 2.4 are of the right order.

## 3. Setup

### 3.1. Algebraic groups

We will be working with connected algebraic groups over ℂ \mathbb{C} of dimension 1 1. An algebraic group (over ℂ \mathbb{C}) is an algebraic variety G G with a morphism from G × G G\times G to G G that induces a group operation on G ⁡ ( ℂ) G(\mathbb{C}). As an example, consider the algebraic group given by the variety 𝔸 1 \mathbb{A}^{1} along with the morphism which maps ( x, y) (x,y) to x + y x+y. We refer to this algebraic group as the additive group 𝔾 a \mathbb{G}_{a}. Another example is the algebraic group given by the algebraic variety 𝔸 1 ∖ { 0 } \mathbb{A}^{1}\setminus\{0\} with the morphism that maps ( x, y) (x,y) to x ​ y xy. We refer to this algebraic group as the multiplicative group 𝔾 m \mathbb{G}_{m}. A third example of this is an elliptic curve over ℂ \mathbb{C} with its canonical group operation [40, III.2].

All the above three examples are 1 1 -dimensional, connected algebraic groups over ℂ \mathbb{C}, and in fact, these are essentially the only possible examples. In order to see this, note that the analytification of G G is a complex Lie group, and therefore has an exponential map

 | exp G: ℂ → G ⁡ ( ℂ), \displaystyle\exp_{G}:\mathbb{C}\to G(\mathbb{C}), |  |

which is analytic and non-constant, since it is a local diffeomorphism [30, Proposition 20.8 (f)]. When G G is commutative, exp G \exp_{G} is a morphism of Lie groups. For this, see [30, Exercise 20-8] or the Baker–Campbell–Hausdorff formula. The following argument in complex analysis now implies that exp G \exp_{G} is surjective with discrete kernel.

###### Proposition 3.1.

Let G G and H H be complex Lie groups of dimension 1 1. Suppose that H H is connected. Every morphism of complex Lie groups from G G to H H is either trivial or is surjective with discrete kernel.

###### Proof.

Suppose the morphism f f is not trivial. Discreteness of the kernel follows from the uniqueness of analytic continuation. Since dim ( G) = dim ( H) = 1 \dim(G)=\dim(H)=1, the open mapping theorem implies that the image U U of f f is open. The set U U is also a Lie subgroup of H H. Therefore H H is a disjoint union of the cosets of U U, each of which is open. Since H H is connected, there can be at most one coset, i.e., U = H U=H. ∎

There are therefore three options for G G depending on the kernel of exp G \exp_{G}.

1. (1)

The kernel is trivial. In this case G ⁡ ( ℂ) G(\mathbb{C}) is isomorphic to the additive group of complex numbers ℂ \mathbb{C}.

2. (2)

The kernel is a lattice of rank one. In this case G ⁡ ( ℂ) G(\mathbb{C}) is isomorphic to the multiplicative group of complex numbers ℂ ∗ \mathbb{C}^{\ast}. For example, the linear map on the tangent space ℂ \mathbb{C} that takes the kernel of exp G \exp_{G} to the lattice 2 ​ π ​ i ​ ℤ 2\pi i\mathbb{Z} is such an isomorphism.

3. (3)

The kernel is a lattice Λ \Lambda of rank two. In this case G ⁡ ( ℂ) G(\mathbb{C}) is isomorphic to the complex torus ℂ / Λ \mathbb{C}/\Lambda. It can be shown via the classical Weierstrass theory [40, Proposition VI.3.6] that G G is isomorphic to the group of complex points of an elliptic curve.

In each case, the isomorphism of G ⁡ ( ℂ) G(\mathbb{C}) with ℂ, ℂ ∗ \mathbb{C},\mathbb{C}^{\ast} or ℂ / Λ \mathbb{C}/\Lambda can be promoted to an isomorphism of G G with 𝔾 a, 𝔾 m \mathbb{G}_{a},\mathbb{G}_{m} or an elliptic curve E E by extending the isomorphism to the closure of G ⁡ ( ℂ) G(\mathbb{C}) in some projective space, and applying Serre’s GAGA theorem.

The exponential map exp G \exp_{G} of an algebraic group admits a local inverse, which we denote by log G \log_{G}. We note that exp 𝔾 a ​ ( ℂ) = id ℂ \exp_{\mathbb{G}_{a}(\mathbb{C})}=\textrm{id}_{\mathbb{C}} and exp 𝔾 m ​ ( ℂ) \exp_{\mathbb{G}_{m}(\mathbb{C})} is the usual exponential function exp: ℂ → ℂ ∗ \exp:\mathbb{C}\to\mathbb{C}^{\ast}. Furthermore, when G G is an elliptic curve embedded into ℙ 2 \mathbb{P}^{2} via its Weierstrass form, then exp G: ℂ → G ⁡ ( ℂ) ⊆ ℙ 2 ​ ( ℂ) \exp_{G}:\mathbb{C}\to G(\mathbb{C})\subseteq\mathbb{P}^{2}(\mathbb{C}) satisfies

 | exp G ( z) = ( 2 σ ( z) 3 ℘ ( z): σ ( z) 3 ℘ ′ ( z): 2 σ ( z) 3) \exp_{G}(z)=(2\sigma(z)^{3}\wp(z):\sigma(z)^{3}\wp^{\prime}(z):2\sigma(z)^{3}) |  |

for all z ∈ ℂ z\in\mathbb{C}, where ℘ \wp and σ \sigma denote the classical Weierstrass ℘ \wp -function and σ \sigma -function associated to the lattice given by the kernel of exp G \exp_{G}.

We remark that this classification of connected algebraic groups of dimension 1 1 extends to any algebraically closed field in characteristic zero. This follows from the Barsotti–Chevalley–Rosenlicht theorem, see [32, Theorem 10.25].

If G G is an algebraic group, then a closed subvariety of G G is called an algebraic subgroup if it is an algebraic group with the same group operation. In particular, we require algebraic subgroups to be closed, but not irreducible.

Given algebraic groups G G and H H, a morphism from G G to H H is a morphism of the underlying varieties that also induces a group homomorphism from G ⁡ ( ℂ) G(\mathbb{C}) to H ⁡ ( ℂ) H(\mathbb{C}). For example, every morphism from 𝔾 m \mathbb{G}_{m} to 𝔾 m \mathbb{G}_{m} is given by sending x x to x n x^{n} for some n ∈ ℤ n\in\mathbb{Z}. Moreover, every morphism from 𝔾 m \mathbb{G}_{m} to 𝔾 a \mathbb{G}_{a} is trivial; that is, it sends x x to 0 0. The kernel of a morphism of algebraic groups is an algebraic subgroup. Moreover, if dim ( G) = dim ( H) = 1 \dim(G)=\dim(H)=1, then any morphism of algebraic groups from G G to H H is either trivial or it is surjective with finite kernel. This follow from Proposition 3.1 upon observing that the kernel is discrete in the analytic topology and closed in the Zariski topology. Morphisms of algebraic groups that are surjective with finite kernel are called *isogenies*. Moreover, G G and H H are called *isogenous*if there is an isogeny from G G to H H. Thus, any morphism of algebraic groups of dimension 1 1 is either trivial or an isogeny. If two connected algebraic groups of dimension 1 1 are isogenous, then they are either isomorphic or they are elliptic curves. We will use the following well-known fact about complex algebraic groups.

###### Lemma 3.2.

Let G, H G,H be one dimensional complex connected algebraic groups and 𝒞 ⊊ G × H \mathcal{C}\subsetneq G\times H an algebraic correspondence. Suppose that there is a one dimensional vector space V ⊊ ℂ 2, b ∈ ℂ 2 V\subsetneq\mathbb{C}^{2},b\in\mathbb{C}^{2} and a non-empty open set U ⊆ ℂ 2 U\subseteq\mathbb{C}^{2}, such that U ∩ ( V + b) U\cap(V+b) is non-empty and

 | exp G × H ⁡ ( U ∩ ( V + b)) ⊆ 𝒞 ⁡ ( ℂ). \exp_{G\times H}(U\cap(V+b))\subseteq\mathcal{C}(\mathbb{C}). |  |

Then 𝒞 \mathcal{C} is a translate of an algebraic group.

We will provide a proof for the benefit of the reader.

###### Proof.

We can translate 𝒞 \mathcal{C} by P = exp G × H ⁡ ( b) P=\exp_{G\times H}(b) so that we can assume that b = 0 b=0 and U U is a neighbourhood of the identity. Now exp G × H ⁡ ( U ∩ V) ⊆ 𝒞 ⁡ ( ℂ) \exp_{G\times H}(U\cap V)\subseteq\mathcal{C}(\mathbb{C}). There is an open non-empty set U ′ ⊆ U U^{\prime}\subseteq U, such that U + x ∩ U U+x\cap U is non-empty for all x ∈ U ′ x\in U^{\prime}. Thus exp ( U ′) ⊊ Stab ( 𝒞) = { P ∈ 𝒞 ( ℂ); P + 𝒞 = 𝒞 } \exp(U^{\prime})\subsetneq\text{Stab}(\mathcal{C})=\{P\in\mathcal{C}(\mathbb{C});P+\mathcal{C}=\mathcal{C}\}. Since the stabiliser Stab is an algebraic variety and 𝒞 \mathcal{C} is irreducible 𝒞 = Stab ​ ( 𝒞) \mathcal{C}=\text{Stab}(\mathcal{C}). We also note that the stabilizer is a group and thus an algebraic subgroup of G × H G\times H. ∎

### 3.2. Degrees

Given an algebraic group G G and some subvariety 𝒱 \mathcal{V} of G G, we will often need to define the degree of 𝒱 \mathcal{V}. It is worth mentioning that our varieties will always be pure dimensional and otherwise we talk about Zariski-closed sets. In order to define the degree of 𝒱 \mathcal{V}, we need a map from from G G to projective space ℙ n \mathbb{P}^{n} for some n ∈ ℕ n\in\mathbb{N}. Such maps are parameterised by line bundles.

Thus, let G G be an algebraic group of dimension 1 1. If G G is 𝔾 a \mathbb{G}_{a} or 𝔾 m \mathbb{G}_{m}, we fix a canonical open immersion G → ℙ 1 G\to\mathbb{P}^{1}. In this case, the Zariski closure G ¯ \overline{G} of G G in ℙ 1 \mathbb{P}^{1} satisfies G ¯ = ℙ 1 \overline{G}=\mathbb{P}^{1}. We let L G L_{G} denote the line bundle O ℙ 1 ​ ( 1) O_{\mathbb{P}^{1}}(1) on ℙ 1 \mathbb{P}^{1}. If G G is an elliptic curve, let L G L_{G} be the ample line bundle O G ​ ( O) O_{G}(O), where O O is the identity of E E. Moreover, in the case of elliptic curves, we have G ¯ = G \overline{G}=G.

On a product of algebraic groups G 1 × ⋯ × G g G_{1}\times\dots\times G_{g}, we will always use the line bundle

 | L = ( π 1 ∗ ​ L G 1) ⊗ ⋯ ⊗ ( π g ∗ ​ L G g), \displaystyle L=(\pi_{1}^{\ast}L_{G_{1}})\otimes\dots\otimes(\pi_{g}^{\ast}L_{G_{g}}), |  |

where for each i ∈ { 1, …, g } i\in\{1,\dots,g\}, the map

 | π i: G 1 ¯ × ⋯ × G g ¯ → G i ¯ \displaystyle\pi_{i}:\overline{G_{1}}\times\dots\times\overline{G_{g}}\to\overline{G_{i}} |  |

is the projection morphism, and π i ∗ \pi_{i}^{\ast} is the pullback morphism on line bundles.

With the line bundle L L fixed, the *degree*deg L ⁡ ( 𝒱) \deg_{L}(\mathcal{V}) of a (quasi-projective) subvariety 𝒱 \mathcal{V} of dimension n n in G ¯ 1 × ⋯ × G ¯ g \overline{G}_{1}\times\dots\times\overline{G}_{g} is the intersection product

 | deg L ⁡ ( 𝒱) = c 1 ​ ( L) n ⋅ [V], \displaystyle\deg_{L}(\mathcal{V})=c_{1}(L)^{n}\cdot[V], |  |

where c 1 ​ ( L) c_{1}(L) is the first Chern class of L L. For the definition of the intersection product and Chern classes, see [20, Chapter 2.5]. A viewpoint requiring less machinery is that a multiple of L L is very ample and gives an embedding into projective space. The degree of 𝒱 \mathcal{V} is then the degree of the image of the embedding.

###### Remark 3.3.

If G G is 𝔾 a \mathbb{G}_{a} or 𝔾 m \mathbb{G}_{m} and 𝒱 \mathcal{V} is a hypersurface defined by a single polynomial, the above definition somewhat closely resembles an intuitive definition of the degree of polynomial. In particular, letting X 1, … ​ X g X_{1},\dots X_{g} denote the cartesian coordinates of G g G^{g}, we view the hypersurface 𝒱 \mathcal{V} as a subvariety of 𝔸 g \mathbb{A}^{g} defined by some polynomial

 | f 𝒱 = ∑ 𝝀 ∈ A c ⁡ ( 𝝀) ​ X 𝝀, f_{\mathcal{V}}=\sum_{\bm{\lambda}\in A}c(\bm{\lambda})X^{\bm{\lambda}}, |  |

where A A is some finite, non-empty subset of ℤ ≥ 0 g \mathbb{Z}_{\geq 0}^{g}, c ⁡ ( 𝝀) ≠ 0 c(\bm{\lambda})\neq 0 for all 𝝀 ∈ E \bm{\lambda}\in E, and X 𝝀 = X 1 λ 1 ​ … ​ X g λ g X^{\bm{\lambda}}=X_{1}^{\lambda_{1}}\dots X_{g}^{\lambda_{g}}. Then it turns out that deg L ⁡ ( 𝒱) = j 1 + ⋯ + j g \deg_{L}(\mathcal{V})=j_{1}+\dots+j_{g}, where for each 1 ≤ i ≤ k 1\leq i\leq k, the number j i j_{i} is the largest non-negative integer j j such that there is a monomial X 𝝀 X^{\bm{\lambda}}, with 𝝀 ∈ E \bm{\lambda}\in E, which is divisible by X i j X_{i}^{j}. This can be strictly larger than the usual total degree of a polynomial, which is defined as the largest degree of a monomial with non-zero coefficient.

### 3.3. Correspondences

We first make the concept of a correspondence precise.

###### Definition 3.4.

Let X X and Y Y be irreducible curves. A correspondence 𝒞 \mathcal{C} between X X and Y Y is an irreducible curve 𝒞 ⊆ X × Y \mathcal{C}\subseteq X\times Y such that the canonical projections π X: 𝒞 → X \pi_{X}:\mathcal{C}\to X and π Y: 𝒞 → Y \pi_{Y}:\mathcal{C}\to Y are dominant. Moreover, for any set A ⊆ X ⁡ ( ℂ) A\subseteq X(\mathbb{C}), we define

 | 𝒞 ⁡ ( A) = { π Y ​ ( π X − 1 ​ ( x)): x ∈ A } = π Y ​ ( 𝒞 ∩ ( A × Y)). \mathcal{C}(A)=\{\pi_{Y}(\pi_{X}^{-1}(x)):x\in A\}=\pi_{Y}(\mathcal{C}\cap(A\times Y)). |  |

Here, we recall that the projection π X \pi_{X} is finite if for every x ∈ X x\in X, the set π X − 1 ​ ( x) = { z ∈ 𝒞 ⁡ ( ℂ): π X ​ ( z) = x } \pi_{X}^{-1}(x)=\{z\in\mathcal{C}(\mathbb{C}):\pi_{X}(z)=x\} is finite. Since all curves involved are irreducible this is equivalent to π X \pi_{X} being dominant. We recall that the projection π X \pi_{X} is dominant if π X ​ ( 𝒞 ​ ( ℂ)) \pi_{X}(\mathcal{C}(\mathbb{C})) is dense in X X. Note that here we use the fact that π X ​ ( 𝒞 ​ ( ℂ)) \pi_{X}(\mathcal{C}(\mathbb{C})) is either finite, empty or co-finite; this is not true for an arbitrary dense set A ⊆ X ⁡ ( ℂ) A\subseteq X(\mathbb{C}).

If A ⊆ X ⁡ ( ℂ) A\subseteq X(\mathbb{C}) is a finite set, then 𝒞 ⁡ ( A) \mathcal{C}(A) is also finite by our assumptions on the dimensions of X, Y X,Y and 𝒞 \mathcal{C}. If d X d_{X} and d Y d_{Y} are the degrees of the projection maps π X \pi_{X} and π Y \pi_{Y}, then since X, Y, 𝒞 X,Y,\mathcal{C} are irreducible algebraic curves, d X, d Y d_{X},d_{Y} are equal to the maximal cardinality of a fibre. Thus | 𝒞 ⁡ ( A) | ≤ d X ​ | A | |\mathcal{C}(A)|\leq d_{X}|A| and

 | 1 d Y ​ | A | ≤ | 𝒞 ⁡ ( A) | \displaystyle\frac{1}{d_{Y}}|A|\leq|\mathcal{C}(A)| |  |

if A A lies in the image of π Y \pi_{Y}. In particular, the lower bound holds for all finite sets A A when π Y \pi_{Y} is surjective.

Let L X L_{X} and L Y L_{Y} be line bundles on projective varieties X X and Y Y, respectively, and let L = π X ∗ ​ L X ⊗ π Y ∗ ​ L Y L=\pi_{X}^{\ast}L_{X}\otimes\pi_{Y}^{\ast}L_{Y}. If 𝒞 \mathcal{C} is a correspondence between X X and Y Y, then

 | deg L ⁡ ( 𝒞) = deg L X ⁡ ( ( π X) ∗ ​ [𝒞]) + deg L Y ⁡ ( ( π Y) ∗ ​ [𝒞]) = d X ​ deg L X ⁡ ( X) + d Y ​ deg L Y ⁡ ( Y) \displaystyle\deg_{L}(\mathcal{C})=\deg_{L_{X}}((\pi_{X})_{\ast}[\mathcal{C}])+\deg_{L_{Y}}((\pi_{Y})_{\ast}[\mathcal{C}])=d_{X}\deg_{L_{X}}(X)+d_{Y}\deg_{L_{Y}}(Y) |  |

by the projection formula. Thus if L X L_{X} and L Y L_{Y} are ample, then

 | | 𝒞 ( A) | ≍ deg L ⁡ ( 𝒞) | A | \displaystyle|\mathcal{C}(A)|\asymp_{\deg_{L}(\mathcal{C})}|A| |  |

for all finite sets A A. In particular this will be true in our setup, described above in Section 3.2.

We will be working with correspondences between algebraic groups. If there is a correspondence between algebraic groups G G and H H that is the translate of an algebraic group, then G G and H H are isogenous. Let us now give two intuitive examples.

###### Example 3.5.

We can fix a rational map φ: X → Y \varphi:X\rightarrow Y that is well-defined on an open U ⊆ X U\subseteq X and then consider 𝒞 \mathcal{C} to be the Zariski-closure of the graph of φ \varphi. Bremner’s question, discussed in the introduction, concerns the case where X X is an elliptic curve in Weierstrass form y 2 = x 3 + a ​ x + b y^{2}=x^{3}+ax+b, U = X ∖ { O } U=X\setminus\{O\} is X X without its point at infinity, Y = 𝔾 a Y=\mathbb{G}_{a}, and φ ⁡ ( x, y) = x \varphi(x,y)=x. If A ⊆ U ⁡ ( ℂ) A\subseteq U(\mathbb{C}) is a finite set, then 𝒞 ⁡ ( A) \mathcal{C}(A) is the set of all x x -coordinates occuring among points of A A.

###### Example 3.6.

Let φ \varphi be a polynomial of degree d ≥ 1 d\geq 1. We can consider a correspondence between 𝔾 m × 𝔾 m \mathbb{G}_{m}\times\mathbb{G}_{m} whose complex points are given by { ( x, φ ⁡ ( x)): x ∈ 𝔾 m ​ ( ℂ) } \{(x,\varphi(x)):x\in\mathbb{G}_{m}(\mathbb{C})\}. One can see that the degree of this correspondence is d + 1 d+1. Moreover, 𝒞 \mathcal{C} is a translate of an algebraic subgroup if and only if φ \varphi is of the form c ​ x d cx^{d} for some c ∈ ℂ c\in\mathbb{C}. This is precisely the correspondence that we use for our deduction of Corollary 1.4 from Theorem 1.3.

### 3.4. Mordell–Lang and S S -unit equations.

We recall here the deep results of Laurent, David–Philippon and Evertse–Schlickewei–Schmidt on the Mordell–Lang conjecture.

###### Theorem 3.7.

[11, 29, 18] For any positive integers d, g d,g, there exists a constant C = C ⁡ ( d, g) ∈ ℕ C=C(d,g)\in\mathbb{N} with the following property. Suppose G G is an elliptic curve or 𝔾 m \mathbb{G}_{m}. Let 𝒱 ⊆ G g \mathcal{V}\subseteq G^{g} be an algebraic variety of degree d d and 𝒱 c ​ o \mathcal{V}^{co} be

 | 𝒱 c ​ o = 𝒱 ∖ ⋃ R + B ⊂ 𝒱, dim ( B) > 0 ( R + B), \mathcal{V}^{co}=\mathcal{V}\setminus\bigcup_{R+B\subset\mathcal{V},\dim(B)>0}(R+B), |  |

where R R runs through points in G g G^{g} and B B through connected algebraic subgroups. Then

 | | 𝒱 c ​ o ∩ Γ | ≤ C 1 + r |\mathcal{V}^{co}\cap\Gamma|\leq C^{1+r} |  |

for any subgroup Γ ⊆ G g ​ ( ℂ) \Gamma\subseteq G^{g}(\mathbb{C}) of rank r r. More generally, one has

 | 𝒱 ∩ Γ = ⋃ i = 1 C 1 + r ( γ i + H i) ∩ Γ, \displaystyle\mathcal{V}\cap\Gamma=\bigcup_{i=1}^{C^{1+r}}(\gamma_{i}+H_{i})\cap\Gamma, |  |

where γ 1, …, γ C 1 + r \gamma_{1},\dots,\gamma_{C^{1+r}} are elements of Γ \Gamma, and H 1, …, H C 1 + r H_{1},\dots,H_{C^{1+r}} are connected subgroups of G g G^{g} whose degrees are bounded in terms of d d.

###### Proof.

If G G is an elliptic curve then this theorem follows directly from [11, Théorème 1.13].

For G = 𝔾 m G=\mathbb{G}_{m}, we first prove the first part. We fix polynomials Q 1, …, Q k ∈ ℂ ⁡ [X 1, …, X g] Q_{1},\dots,Q_{k}\in\mathbb{C}[X_{1},\dots,X_{g}], such that 𝒱 \mathcal{V} is their common zero-set. Their degree is bounded by the degree of 𝒱 \mathcal{V} and the number of non-zero monomials in Q i Q_{i} is bounded by deg ⁡ ( Q i) g \deg(Q_{i})^{g} for i = 1, …, g i=1,\dots,g. If we have a point γ ∈ 𝒱 ∩ Γ \gamma\in\mathcal{V}\cap\Gamma, then Q i ( γ) = 0, i = 1, …, k Q_{i}(\gamma)=0,i=1,\dots,k and if γ ∈ 𝒱 c ​ o \gamma\in\mathcal{V}^{co}, then there is at least one i i, such that no subsum of the monomials in Q i Q_{i} vanishes if evaluated at γ \gamma. This follows from the proof of Laurent [29]. The number of solutions of Q i ​ ( γ) = 0 Q_{i}(\gamma)=0 with no vanishing subsum is bounded by c ​ ( deg ⁡ ( Q i), g) 1 + r c(\deg(Q_{i}),g)^{1+r} for all i i [18]. This gives the first claim.

For the general statement we follow the proof of Laurent [29]. Each maximal algebraic group contained in 𝒱 \mathcal{V} corresponds to a partition of the support of its defining equations. Thus, their number and degree is bounded only in terms of the degree of 𝒱 \mathcal{V}. For each algebraic subgroup given by a partition, Laurent constructs a map that reduces counting the number of intersection points to the S S -unit equation for which we can apply the main theorem in [18].

Finally, the fact that the degree of each H i H_{i} is bounded in terms of d d follows from the argument in [2, Lemma 2]. ∎

Note that 𝒱 c ​ o \mathcal{V}^{co} might be empty, even if 𝒱 \mathcal{V} is not a coset. An easy example is a product 𝒞 × 𝔾 m ⊆ 𝔾 m 3 \mathcal{C}\times\mathbb{G}_{m}\subseteq\mathbb{G}_{m}^{3} for a curve 𝒞 \mathcal{C}, that is covered by cosets of the form { P } × 𝔾 m \{P\}\times\mathbb{G}_{m}.

## 4. Projecting cartesian products

The main goal of this section is to prove Theorem 4.2 which describes expansion properties for certain projections of varieties.

Thus, let G G to be some 1 1 -dimensional, connected algebraic group over ℂ \mathbb{C}, not isomorphic to 𝔾 a \mathbb{G}_{a}, and let ℬ \mathcal{B} be a projective variety of positive dimension. Let π 1: G g × ℬ → G g \pi_{1}:G^{g}\times\mathcal{B}\to G^{g} and π 2: G g × ℬ → ℬ \pi_{2}:G^{g}\times\mathcal{B}\to\mathcal{B} be the canonical projection maps. We recall the notion of a degenerate variety as described in Definition 1.7.

###### Definition 4.1.

We call an irreducible subvariety 𝒱 ⊆ G g × ℬ \mathcal{V}\subseteq G^{g}\times\mathcal{B}*degenerate*, if there exists a connected algebraic group H ⊆ G g H\subseteq G^{g} of positive dimension, and a proper subvariety 𝒲 ⊆ G g / H × ℬ \mathcal{W}\subseteq G^{g}/H\times\mathcal{B} such that

 | 𝒱 = π H − 1 ​ ( 𝒲), \mathcal{V}=\pi_{H}^{-1}(\mathcal{W}), |  |

for the projection π H: G g × ℬ → G g / H × ℬ \pi_{H}:G^{g}\times\mathcal{B}\rightarrow G^{g}/H\times\mathcal{B}. If 𝒱 \mathcal{V} is not degenerate, we call 𝒱 \mathcal{V} non-degenerate.

With this in hand, we now state our version of Theorem 1.8 for sets lying in low rank subgroups.

###### Theorem 4.2.

Let 𝒱 ⊆ G g × ℬ \mathcal{V}\subseteq G^{g}\times\mathcal{B} be a non-degenerate subvariety of dimension g g, such that π 1 \pi_{1} and π 2 \pi_{2} restricted to 𝒱 \mathcal{V} are dominant. Let Γ ⊆ G ⁡ ( ℂ) \Gamma\subseteq G(\mathbb{C}) be subgroup of rank r r. Then for any finite set A ⊆ Γ A\subseteq\Gamma we have

 | | π 2 ​ ( ( A g × ℬ) ∩ 𝒱) | ≥ c ​ ( g, deg ⁡ ( 𝒱)) 1 + r ​ | A | g, |\pi_{2}((A^{g}\times\mathcal{B})\cap\mathcal{V})|\geq c(g,\deg(\mathcal{V}))^{1+r}|A|^{g}, |  |

for a constant c = c ⁡ ( g, deg ⁡ ( 𝒱)) > 0 c=c(g,\deg(\mathcal{V}))>0 depending only on g g and deg ⁡ ( 𝒱) \deg(\mathcal{V}).

In order to prove Theorem 4.2, we will require the following lemma.

###### Lemma 4.3.

Suppose that 𝒱 ⊆ G g × ℬ \mathcal{V}\subseteq G^{g}\times\mathcal{B} is a non-degenerate subvariety of dimension g g, and suppose that the maps π 1 \pi_{1} and π 2 \pi_{2} are dominant. Then there exists a proper Zariski closed set Z ⊆ G g Z\subseteq G^{g}, such that if there is a positive dimensional subgroup H ⊆ G g H\subseteq G^{g} and ( P, Q) ∈ ( G g × ℬ) ​ ( ℂ) (P,Q)\in(G^{g}\times\mathcal{B})(\mathbb{C}) with

(4.1) |  | { ( P + T, Q): T ∈ H ⁡ ( ℂ) } ⊆ 𝒱, \displaystyle\{(P+T,Q):T\in H(\mathbb{C})\}\subseteq\mathcal{V}, |  |

then P + H ⊆ Z P+H\subseteq Z. Moreover, the degree of the components of Z Z and their number is bounded by a constant depending only on g, deg ⁡ ( 𝒱) g,\deg(\mathcal{V}).

###### Proof.

We first fix a connected algebraic subgroup H H of dimension k k, and show that all P P such that ( P + H) × { Q } ⊆ 𝒱 (P+H)\times\{Q\}\subseteq\mathcal{V} for some Q Q are contained in a Zariski closed set Z H Z_{H}, that depends on H H. The lemma will be proved by taking a union of such sets Z H Z_{H}. Let p H p_{H} be the restriction of the quotient map π H: G g × ℬ → ( G g / H) × ℬ \pi_{H}:G^{g}\times\mathcal{B}\to(G^{g}/H)\times\mathcal{B} to 𝒱 \mathcal{V}. By Chevalley’s theorem [23, Theorem 1.3.1] the set

 | Z H = { y ∈ 𝒱 ⁡ ( ℂ): dim ( p H − 1 ​ ( p H ​ ( y))) ≥ k } Z^{H}=\{y\in\mathcal{V}(\mathbb{C}):\dim(p_{H}^{-1}(p_{H}(y)))\geq k\} |  |

is closed. Thus if ( P + H) × { Q } ⊆ 𝒱 (P+H)\times\{Q\}\subseteq\mathcal{V} then ( P + H) × { Q } ⊆ p H − 1 ​ ( p H ​ ( P, Q)) (P+H)\times\{Q\}\subseteq p_{H}^{-1}(p_{H}(P,Q)), and so ( P, Q) ∈ Z H (P,Q)\in Z^{H}.

Since ℬ \mathcal{B} is projective, the projection π 1: G g × ℬ → G g \pi_{1}:G^{g}\times\mathcal{B}\to G^{g} is closed [39, Theorem 1.11]. Therefore Z H = π 1 ​ ( Z H) Z_{H}=\pi_{1}(Z^{H}) is closed in G g G^{g}. If Z H = G g Z_{H}=G^{g} then Z H Z^{H} has dimension g g, and is therefore equal to 𝒱 \mathcal{V}. Also, the degree of Z H Z_{H} is bounded by the degree of Z H Z^{H}, by the projection formula. It therefore suffices to show that Z H Z^{H} is not equal to 𝒱 \mathcal{V} and that the degree of Z H Z^{H} is bounded in terms of g g and deg ⁡ ( 𝒱) \deg(\mathcal{V}).

We will first prove that Z H ≠ 𝒱 Z^{H}\neq\mathcal{V}, and so, suppose that Z H = 𝒱 Z^{H}=\mathcal{V}. Then consider 𝒲 \mathcal{W}, the Zariski closure of π H ​ ( 𝒱) \pi_{H}(\mathcal{V}) and Z ′ = π H − 1 ​ ( 𝒲) Z^{\prime}=\pi_{H}^{-1}(\mathcal{W}), which is a subvariety of G g × ℬ G^{g}\times\mathcal{B} containing 𝒱 \mathcal{V}. Firstly, 𝒲 \mathcal{W} is irreducible, because 𝒱 \mathcal{V} is irreducible. Since H H is connected, the fibres of π H \pi_{H} are irreducible, and so [39, Theorem 1.26] implies that Z ′ Z^{\prime} is irreducible. Since π H ​ ( 𝒱) \pi_{H}(\mathcal{V}) is constructible it contains U U that is Zariski–open (dense) in 𝒲 \mathcal{W}. We thus have that Z ′ = π H − 1 ​ ( U) ∪ ℰ Z^{\prime}=\pi_{H}^{-1}(U)\cup\mathcal{E}, where ℰ \mathcal{E} is the a finite union of irreducible subvarieties E = π H − 1 ​ ( E ′) E=\pi_{H}^{-1}(E^{\prime}), with E ′ E^{\prime} running over all irreducible components of 𝒲 ∖ U \mathcal{W}\setminus U. By the fibre dimension theorem dim ( E) < dim ( Z ′) \dim(E)<\dim(Z^{\prime}) for all E E. Since π H − 1 ​ ( U) ⊂ 𝒱 \pi_{H}^{-1}(U)\subset\mathcal{V}, we have that Z ′ ⊆ 𝒱 ∪ ℰ Z^{\prime}\subseteq\mathcal{V}\cup\mathcal{E}, and a dimension count shows that dim ( 𝒱) = dim ( Z ′) \dim(\mathcal{V})=\dim(Z^{\prime}). Since both 𝒱 \mathcal{V} and Z ′ Z^{\prime} are irreducible 𝒱 = Z ′ \mathcal{V}=Z^{\prime}. This means that

 | 𝒱 = π H − 1 ​ ( 𝒲) \mathcal{V}=\pi_{H}^{-1}(\mathcal{W}) |  |

and so 𝒱 \mathcal{V} is degenerate. This contradicts our assumption on 𝒱 \mathcal{V}.

We will now prove that the degree of Z H Z^{H} is bounded in terms of g g and deg ⁡ ( 𝒱) \deg(\mathcal{V}). For g ≥ 1 g\geq 1, define exp G g \exp_{G^{g}} the exponential of G g G^{g} at the identity and ℱ \mathcal{F} a suitably chosen fundamental domain for exp G \exp_{G}. The graph exp G \exp_{G} restricted to ℱ \mathcal{F} is a sub-Pfaffian set of complexity bounded by an absolute (effectively computable) constant, see work of Jones and the third author [27]. Each algebraic group H H, corresponds to a vector space T H T_{H}, such that exp G g ⁡ ( T H) = H \exp_{G^{g}}(T_{H})=H. We then consider the set

 | T H = { γ ∈ ℱ g: there exists ​ b ∈ ℬ ⁡ ( ℂ) ​ such that ​ exp G g ⁡ ( γ + T H) ⊆ 𝒱 ∩ ( G g × { b }) }, T^{H}=\{\gamma\in\mathcal{F}^{g}:\text{there exists }b\in\mathcal{B}(\mathbb{C})\ \text{such that}\ \exp_{G^{g}}(\gamma+T_{H})\subseteq\mathcal{V}\cap(G^{g}\times\{b\})\}, |  |

which is a sub-Pfaffian set of complexity c comp c_{\text{comp}}, where c comp c_{\text{comp}} depends only on deg ⁡ ( 𝒱) \deg(\mathcal{V}). We then have Z H = exp G g ⁡ ( T H) Z^{H}=\exp_{G^{g}}(T^{H}), which has also bounded complexity, and it is a closed algebraic variety. The complexity of Z H Z^{H} bounds its degree, and so, we have proven this claim as well.

Finally, suppose P + H P+H is a maximal translate lying in the fibre 𝒱 Q = π 2 − 1 ​ ( Q) ∩ 𝒱 \mathcal{V}_{Q}=\pi_{2}^{-1}(Q)\cap\mathcal{V}. Note that deg ( 𝒱 Q) ≪ g deg ( 𝒱) \deg(\mathcal{V}_{Q})\ll_{g}\deg(\mathcal{V}) by Bézout’s theorem. By an argument of Bombieri–Zannier [2, Lemma 2], if H H is an algebraic subgroup appearing in a maximal translate of 𝒱 Q \mathcal{V}_{Q}, then H H belongs to a finite set { H 1, …, H ℓ } \{H_{1},\dots,H_{\ell}\} with ℓ ≪ g, deg ⁡ ( 𝒱) 1 \ell\ll_{g,\deg(\mathcal{V})}1. The lemma is proved upon taking Z = Z H 1 ∪ ⋯ ∪ Z H ℓ Z=Z_{H_{1}}\cup\dots\cup Z_{H_{\ell}}. ∎

In order to prove Theorem 4.2, we combine Lemma 4.1 with the estimates coming from uniform Mordell–Lang (Theorem 3.7). In order to get control on the contribution of the closed set Z Z from Lemma 4.1 we need the following Schwartz–Zippel type estimate.

###### Lemma 4.4.

Let Z ⊆ G g Z\subseteq G^{g} be an algebraic sub-variety. Then for any finite set A ⊆ G ⁡ ( ℂ) A\subseteq G(\mathbb{C})

 | | Z ∩ A g | ≪ g, deg ⁡ ( Z) | A | dim ( Z). |Z\cap A^{g}|\ll_{g,\deg(Z)}|A|^{\dim(Z)}. |  |

###### Proof.

We prove this by induction on the dimension. We may suppose that Z Z is irreducible, since we can argue component wise. We can also pass to the closure Z ¯ \overline{Z} of Z Z in G ¯ g \overline{G}^{g}. If dim ( Z) = 0 \dim(Z)=0, this is trivial. So assume that dim ( Z) ≥ 1 \dim(Z)\geq 1. We can choose a factor G ¯ \overline{G} in G ¯ g \overline{G}^{g} such that the projection from Z ¯ \overline{Z} to G ¯ \overline{G} is surjective. Without loss of generality, we can assume this is the first factor. Then the intersection Z ¯ ∩ ( { a } × G ¯ g − 1) \overline{Z}\cap(\{a\}\times\overline{G}^{g-1}) has dimension equal to dim ( Z) − 1 \dim(Z)-1. By Bézout’s theorem

 | deg ( Z ¯ ∩ ( { a } × G ¯ g − 1)) ≤ deg ( Z) deg ( G ¯ g − 1) ≪ g deg ( Z). \deg(\overline{Z}\cap(\{a\}\times\overline{G}^{g-1}))\leq\deg(Z)\deg(\overline{G}^{g-1})\ll_{g}\deg(Z). |  |

We then conclude by induction that

 | | Z ∩ A g | ≤ ∑ a ∈ A | A g ∩ ( { a } × G ¯ g − 1) ∩ Z ¯ | ≪ g, deg ⁡ ( Z) | A | | A | dim ( Z) − 1. ∎ |Z\cap A^{g}|\leq\sum_{a\in A}|A^{g}\cap(\{a\}\times\overline{G}^{g-1})\cap\overline{Z}|\ll_{g,\deg(Z)}|A||A|^{\dim(Z)-1}.\qed |  |

We are now ready to prove Theorem 4.2.

###### Proof of Theorem 4.2.

As 𝒱 \mathcal{V} is non-degenerate, a coset contained in a fibre 𝒱 Q = π 2 − 1 ​ ( Q) ∩ 𝒱 \mathcal{V}_{Q}=\pi_{2}^{-1}(Q)\cap\mathcal{V} is contained in a closed set Z ⊆ 𝒱 Z\subseteq\mathcal{V} not depending on Q Q. This is Lemma 4.1. We set A ′ = A g ∖ Z ⁡ ( ℂ) A^{\prime}=A^{g}\setminus Z(\mathbb{C}) and by Lemma 4.4, | Z ∩ A g | ≪ deg ⁡ ( 𝒱) | A | g − 1 |Z\cap A^{g}|\ll_{\deg(\mathcal{V})}|A|^{g-1}. Since the projection π 1 \pi_{1} from 𝒱 \mathcal{V} to G g G^{g} is dominant and ℬ \mathcal{B} is projective, π 1 \pi_{1} is actually surjective, because it is closed [39]. Hence for each point a ∈ A ′ a\in A^{\prime}, there is a point b ∈ B b\in B such that ( a, b) ∈ ( A ′ × ℬ) ∩ 𝒱 (a,b)\in(A^{\prime}\times\mathcal{B})\cap\mathcal{V}. On the other hand, it follows from Theorem 3.7 that for every b ∈ ℬ ⁡ ( ℂ) b\in\mathcal{B}(\mathbb{C}), one has

 | | ( A ′ × { b }) ∩ 𝒱 | ≤ c ​ ( r, g, deg ⁡ ( 𝒱)) r + 1 |(A^{\prime}\times\{b\})\cap\mathcal{V}|\leq c(r,g,\deg(\mathcal{V}))^{r+1} |  |

Thus the image π 2 ​ ( ( A g × ℬ) ∩ 𝒱) \pi_{2}((A^{g}\times\mathcal{B})\cap\mathcal{V}) contains at least

 | c ​ ( r, g, deg ⁡ ( 𝒱)) − 1 − r ​ ( | A | g − c ′ ​ | A | g − 1) c(r,g,\deg(\mathcal{V}))^{-1-r}(|A|^{g}-c^{\prime}|A|^{g-1}) |  |

elements for a constant c ′ > 0 c^{\prime}>0 depending only on deg ⁡ ( 𝒱) \deg(\mathcal{V}) and g g, which finishes the proof of Theorem 4.2. ∎

## 5. Correspondences and cosets

In this section we construct a variety 𝒱 sum \mathcal{V}_{\text{sum}} with the property that π 2 ​ ( ( A g × H) ∩ 𝒱 sum) \pi_{2}((A^{g}\times H)\cap\mathcal{V}_{\text{sum}}) is roughly the sumset 𝒞 1 ​ ( A) + ⋯ + 𝒞 g ​ ( A) \mathcal{C}_{1}(A)+\dots+\mathcal{C}_{g}(A), for correspondences 𝒞 1, …, 𝒞 g \mathcal{C}_{1},\dots,\mathcal{C}_{g} between algebraic groups G G and H H. We would like to apply Theorem 4.2 to 𝒱 sum \mathcal{V}_{\text{sum}}, and so this section is dedicated to showing that this variety is non-degenerate, in the sense of Definition 1.7.

Now let G G and H H be connected algebraic groups of dimension 1, such that G G is not isomorphic to 𝔾 a \mathbb{G}_{a}. We compactify H H as described at the beginning of to section 3.2. Thus H ¯ \overline{H} is either ℙ 1 \mathbb{P}^{1} or an elliptic curve, depending on whether H H is isomorphic to 𝔾 a \mathbb{G}_{a}, 𝔾 m \mathbb{G}_{m} or to an elliptic curve. We also consider the g g -fold sum map on H H

 | p sum: H g \displaystyle p_{\text{sum}}:H^{g} | → H \displaystyle\rightarrow H |  |

 | ( Q 1, …, Q g) \displaystyle(Q_{1},\dots,Q_{g}) | ↦ Q 1 + ⋯ + Q g, \displaystyle\mapsto Q_{1}+\cdots+Q_{g}, |  |

its graph Γ ⁡ ( p sum) ⊆ H g × H \Gamma(p_{\text{sum}})\subseteq H^{g}\times H, and its closure Γ ⁡ ( p sum) ¯ \overline{\Gamma(p_{\text{sum}})} in H ¯ g + 1 \overline{H}^{g+1}.

Let 𝒞 1, …, 𝒞 g ⊆ G × H ¯ \mathcal{C}_{1},\dots,\mathcal{C}_{g}\subseteq G\times\overline{H} be correspondences, none of which is the translate of an algebraic subgroup. We set

 | 𝒱 ∗ = { ( P 1, …, P g, Q 1, …, Q g + 1): ( Q 1, …, Q g + 1) ∈ Γ ⁡ ( p sum) ¯, ( P i, Q i) ∈ 𝒞 i }, \mathcal{V}^{*}=\{(P_{1},\dots,P_{g},Q_{1},\dots,Q_{g+1}):(Q_{1},\dots,Q_{g+1})\in\overline{\Gamma(p_{\text{sum}})},(P_{i},Q_{i})\in\mathcal{C}_{i}\}, |  |

which is an irreducible variety. The projection π G g × H ¯: G g × H ¯ g + 1 → G g × H ¯ \pi_{G^{g}\times\overline{H}}:G^{g}\times\overline{H}^{g+1}\rightarrow G^{g}\times\overline{H} onto G g G^{g} and the last coordinate of H ¯ g + 1 \overline{H}^{g+1} is a closed map by [39, Theorem 1.11]. We set

(5.1) |  | 𝒱 sum = π G g × H ¯ ​ ( 𝒱 ∗) \mathcal{V}_{\text{sum}}=\pi_{G^{g}\times\overline{H}}(\mathcal{V}^{*}) |  |

which is an irreducible variety since it is the image of an irreducible variety under a closed map. Thus the role of the projective variety ℬ \mathcal{B} in Section 4 is played by H ¯ \overline{H}.

Our main goal in this section is to prove the following.

###### Proposition 5.1.

The variety 𝒱 sum ⊆ G g × H ¯ \mathcal{V}_{\rm sum}\subseteq G^{g}\times\overline{H} is non-degenerate of dimension g g. The projection π 1: 𝒱 sum → G g \pi_{1}:\mathcal{V}_{\rm sum}\to G^{g} is surjective and the projection π 2: 𝒱 sum → H ¯ \pi_{2}:\mathcal{V}_{\rm sum}\to\overline{H} is dominant.

As we exclusively work over complex algebraic groups, we will prove a lemma about holomorphic maps between tangent spaces of algebraic groups.

###### Lemma 5.2.

Let U = U 1 × ⋯ × U g U=U_{1}\times\cdots\times U_{g} be an open set of ℂ g \mathbb{C}^{g} and f i: U i → ℂ f_{i}:U_{i}\rightarrow\mathbb{C} non-constant, holomorphic functions for 1 ≤ i ≤ g 1\leq i\leq g. Suppose that there is a vector space W ⊆ ℂ g W\subseteq\mathbb{C}^{g} of dimension 1 1 such that for any b ∈ ℂ g b\in\mathbb{C}^{g}, ( f 1, …, f g) (f_{1},\dots,f_{g}) restricted to ( W + b) ∩ U (W+b)\cap U satisfies

 | f 1 ​ ( z 1) + ⋯ + f g ​ ( z g) ≡ c ​ o ​ n ​ s ​ t. f_{1}(z_{1})+\cdots+f_{g}(z_{g})\equiv const. |  |

Then there is at least one j ∈ { 1, …, g } j\in\{1,\dots,g\} such that f j f_{j} is affine linear.

###### Proof.

After possibly permuting coordinates we can parameterise any co-set W + b W+b by

 | ( b 1, …, b g − k, z, a 1 ​ z + c 1, …, a k − 1 ​ z + c k − 1) (b_{1},\dots,b_{g-k},z,a_{1}z+c_{1},\dots,a_{k-1}z+c_{k-1}) |  |

where k ≥ 1 k\geq 1 is an integer, a 1, …, a k − 1 ∈ ℂ ∗ a_{1},\dots,a_{k-1}\in\mathbb{C}^{*} depend on W W and b 1, …, b g − k, c 1, …, c k − 1 b_{1},\dots,b_{g-k},c_{1},\dots,c_{k-1} depend on W + b W+b. We may assume that k ≠ 1 k\neq 1 since otherwise f g f_{g} is constant. We apply the invertible linear transformation

 | L: ℂ g − k × ℂ × ℂ k − 1 \displaystyle L:\mathbb{C}^{g-k}\times\mathbb{C}\times\mathbb{C}^{k-1} | → ℂ g − k × ℂ × ℂ k − 1 \displaystyle\rightarrow\mathbb{C}^{g-k}\times\mathbb{C}\times\mathbb{C}^{k-1} |  |

 | L ⁡ ( z ¯, z, w ¯) \displaystyle L(\underline{z},z,\underline{w}) | = ( z ¯, z, w 1 − a 1 ​ z, ⋯, w k − 1 − a k − 1 ​ z) \displaystyle=(\underline{z},z,w_{1}-a_{1}z,\cdots,w_{k-1}-a_{k-1}z) |  |

to U U and the open set L ⁡ ( U) L(U) then contains a product set U ~ = U ~ 1 × ⋯ × U ~ g \tilde{U}=\tilde{U}_{1}\times\cdots\times\tilde{U}_{g}. Taking the total derivative with respect to z z we obtain

 | ∂ z g − k + 1 f g − k + 1 ​ ( z) + a 1 ​ ∂ z g − k + 2 f g − k + 2 ​ ( a 1 ​ z + c 1) + ⋯ + a k − 1 ​ ∂ z g f g ​ ( a k − 1 ​ z + c k − 1) = 0, \partial_{z_{g-k+1}}f_{g-k+1}(z)+a_{1}\partial_{z_{g-k+2}}f_{g-k+2}(a_{1}z+c_{1})+\dots+a_{k-1}\partial_{z_{g}}f_{g}(a_{k-1}z+c_{k-1})=0, |  |

for all ( b 1, …, b g − k, z, c 1, …, c k − 1) ∈ U ~. (b_{1},\dots,b_{g-k},z,c_{1},\dots,c_{k-1})\in\tilde{U}. Since k ≥ 2 k\geq 2, we may fix any

 | ( z 0, c 1, 0, …, c k − 2, 0) ∈ U ~ g − k + 1 × ⋯ × U ~ g − 1 (z_{0},c_{1,0},\dots,c_{k-2,0})\in\tilde{U}_{g-k+1}\times\cdots\times\tilde{U}_{g-1} |  |

to find that f g f_{g} is affine linear. ∎

###### Corollary 5.3.

Let U 1 × ⋯ × U g U_{1}\times\cdots\times U_{g} be an open set of ℂ g \mathbb{C}^{g} and f i: U i → ℂ f_{i}:U_{i}\rightarrow\mathbb{C} holomorphic non-constant functions i = 1, …, g i=1,\dots,g. Suppose that there is a vector space V ⊊ ℂ g V\subsetneq\mathbb{C}^{g} of dimension k k such that for any b ∈ ℂ g b\in\mathbb{C}^{g}, ( f 1, …, f g) (f_{1},\dots,f_{g}) restricted to ( V + b) ∩ U (V+b)\cap U satisfies

 | f 1 ​ ( z 1) + ⋯ + f g ​ ( z g) ≡ c ​ o ​ n ​ s ​ t. f_{1}(z_{1})+\cdots+f_{g}(z_{g})\equiv const. |  |

Then f j f_{j} is affine linear for at least one j ∈ { 1, …, g } j\in\{1,\dots,g\}.

###### Proof.

We can cover V V by translates of a one dimensional vector space L L and thus any translate of V V contains a translate of L L. Thus Corollary 5.3 is implied by Lemma 5.2. ∎

###### Proof of Proposition 5.1.

Let 𝒱 o \mathcal{V}^{o} be the variety given by the points ( P 1, …, P g, Q) ∈ G g × H (P_{1},\dots,P_{g},Q)\in G^{g}\times H such that there exists ( P i, Q i) ∈ 𝒞 i ∩ ( G × H ⁡ ( ℂ)) (P_{i},Q_{i})\in\mathcal{C}_{i}\cap(G\times H(\mathbb{C})), with Q 1 + ⋯ + Q g = Q Q_{1}+\cdots+Q_{g}=Q. Note that 𝒱 o \mathcal{V}^{o} is open in 𝒱 sum \mathcal{V}_{\text{sum}}. For all but finitely many P ∈ G ⁡ ( ℂ) P\in G(\mathbb{C}), there exists Q ∈ H ⁡ ( ℂ) Q\in H(\mathbb{C}) such that ( P, Q) ∈ 𝒞 i ​ ( ℂ) (P,Q)\in\mathcal{C}_{i}(\mathbb{C}) for i = 1, …, g i=1,\dots,g. Thus, π 1 \pi_{1} is dominant and by [39, Theorem 1.11] it is surjective. Also, for Q ∈ H ⁡ ( ℂ) Q\in H(\mathbb{C}), we can find ( Q 1, …, Q g) ∈ H ⁡ ( ℂ) (Q_{1},\dots,Q_{g})\in H(\mathbb{C}) such that Q 1 + ⋯ + Q g = Q Q_{1}+\cdots+Q_{g}=Q. It follows that π 2 \pi_{2} is dominant. Now suppose that 𝒱 sum \mathcal{V}_{\text{sum}} is degenerate, that is, there exists a connected algebraic group H ′ ⊆ G g H^{\prime}\subseteq G^{g} of positive dimension, and a proper subvariety 𝒲 ⊆ ( G g / H ′) × H ¯ \mathcal{W}\subseteq(G^{g}/H^{\prime})\times\overline{H} such that

(5.2) |  | 𝒱 sum = π H ′ − 1 ​ ( 𝒲), \mathcal{V}_{\rm sum}=\pi_{H^{\prime}}^{-1}(\mathcal{W}), |  |

for the projection π H ′: G g × H ¯ → ( G g / H ′) × H ¯ \pi_{H^{\prime}}:G^{g}\times\overline{H}\rightarrow(G^{g}/H^{\prime})\times\overline{H}.

Now, let s 1, …, s g s_{1},\dots,s_{g} be analytic functions on an open OPEN U ⊆ G ⁡ ( ℂ)) U\subseteq G(\mathbb{C})) with target H ⁡ ( ℂ) H(\mathbb{C}), such that the graph of s i s_{i} coincides with 𝒞 i ​ ( ℂ) \mathcal{C}_{i}(\mathbb{C}) restricted to U × H ⁡ ( ℂ) U\times H(\mathbb{C}). By ( 5.2) the sum ∑ i = 1 g s i \sum_{i=1}^{g}s_{i} (where we sum in H H) is constant along H ′ + P H^{\prime}+P for all P ∈ G g ​ ( ℂ) P\in G^{g}(\mathbb{C}). After perhaps shrinking U U to ensure that it is simply connected, we lift these functions to functions from the tangent space of G G to the tangent space of H H, via setting f i = exp H ∘ s i ∘ log G, i = 1, …, g f_{i}=\exp_{H}\circ s_{i}\circ\log_{G},i=1,\dots,g. Now setting V V to be the tangent space of H ′ H^{\prime}, and recalling that the sum ∑ i = 1 g s i \sum_{i=1}^{g}s_{i} is constant along translates of H ′ H^{\prime}, we deduce that f 1, …, f g f_{1},\dots,f_{g} satisfy the conditions of Corollary 5.3. Thus at least one of f i f_{i} is affine linear. Lemma 3.2 implies that at least one 𝒞 i \mathcal{C}_{i} is the translate of an algebraic subgroup, which contradicts our assumption on the correspondences and concludes the proof. ∎

## 6. Freiman–type structural theorems

For the purposes of this section and the next, given a 1 1 -dimensional, connected algebraic group H H and some finite, non-empty set A ⊊ H A\subsetneq H, we denote rk ⁡ ( A) \mathrm{rk}(A) to be the smallest integer r ≥ 1 r\geq 1 such that there exist ξ 1, …, ξ r ∈ H \xi_{1},\dots,\xi_{r}\in H satisfying

 | A ⊆ { n 1 ξ 1 + ⋯ + n r ξ r: n 1, …, n r ∈ ℤ }. A\subseteq\{n_{1}\xi_{1}+\dots+n_{r}\xi_{r}:n_{1},\dots,n_{r}\in\mathbb{Z}\}. |  |

The main aim of this section is to prove the following structural result.

###### Lemma 6.1.

Let H H be a connected algebraic group of dimension 1 1, let A ⊆ H A\subseteq H be a finite, non-empty set, let n ≥ 2 n\geq 2 be an integer such that | n ​ A | ≤ K ​ | A | |nA|\leq K|A| for some K > 1 K>1. Then there exists some integer 1 ≤ d 1\leq d and some subset A ′ ⊆ A A^{\prime}\subseteq A such that

 | d ≪ 1 + log ⁡ ( 4 ​ K) log ⁡ n and | A ′ | ≫ | A | K C ​ log ⁡ 2 log ⁡ n and rk ⁡ ( A ′) ≤ d, d\ll 1+\frac{\log(4K)}{\log n}\ \ \text{and}\ \ |A^{\prime}|\gg\frac{|A|}{K^{\frac{C\log 2}{\log n}}}\ \ \text{and}\ \ \mathrm{rk}(A^{\prime})\leq d, |  |

where C > 0 C>0 is some absolute constant.

We will begin by proving the n = 2 n=2 version of this.

###### Lemma 6.2.

Let H H be a connected algebraic group of dimension 1 1, let A ⊆ H A\subseteq H be a finite, non-empty set such that | A + A | ≤ K ​ | A | |A+A|\leq K|A| for some K > 1 K>1. Then there exists some integer 1 ≤ d ≤ C ​ log ⁡ ( 400 ​ K) 1\leq d\leq C\log(400K), and some subset A ′ ⊆ A A^{\prime}\subseteq A such that | A ′ | ≥ | A | / ( 100 ​ K) C ′ |A^{\prime}|\geq|A|/(100K)^{C^{\prime}} and rk ⁡ ( A ′) ≤ d \mathrm{rk}(A^{\prime})\leq d, where C = 140 C=140 and C ′ = 110 C^{\prime}=110.

In order to prove Lemma 6.2, we will need the following very nice result of Gowers–Green–Manners–Tao [22, Theorem 1.3] on the resolution of the weak polynomial Freiman–Ruzsa conjecture over ℤ \mathbb{Z}.

###### Lemma 6.3.

Let D D be a positive integer, let A ⊊ ℤ D A\subsetneq\mathbb{Z}^{D} be a finite, non-empty set such that | A + A | ≤ K ​ | A | |A+A|\leq K|A| for some K > 1 K>1. Then there exists some integer 1 ≤ d ≤ C ​ log ⁡ ( 4 ​ K) 1\leq d\leq C\log(4K), some elements 𝐱 1, …, 𝐱 d ∈ ℤ D \bm{x}_{1},\dots,\bm{x}_{d}\in\mathbb{Z}^{D} and some subset A ′ ⊆ A A^{\prime}\subseteq A such that | A ′ | ≥ | A | / K C ′ |A^{\prime}|\geq|A|/K^{C^{\prime}} and

 | A ′ ⊆ { n 1 𝒙 1 + ⋯ + n d 𝒙 d: n 1, …, n d ∈ ℤ }, A^{\prime}\subseteq\{n_{1}\bm{x}_{1}+\dots+n_{d}\bm{x}_{d}:n_{1},\dots,n_{d}\in\mathbb{Z}\}, |  |

where C = 140 C=140 and C ′ = 110 C^{\prime}=110.

We will also need the following simple lemma.

###### Lemma 6.4.

Let H H be a connected algebraic group of dimension 1 1, let A ⊊ H A\subsetneq H be a finite, non-empty set. Then the subgroup generated by S S is isomorphic to some subgroup of ℤ D × ℤ / n ​ ℤ × ℤ / m ​ ℤ \mathbb{Z}^{D}\times\mathbb{Z}/n\mathbb{Z}\times\mathbb{Z}/m\mathbb{Z}, for some non-negative integer D D and some n, m ∈ ℕ n,m\in\mathbb{N}.

###### Proof.

This is true when H = ( ℂ, +) H=(\mathbb{C},+) since any finitely generated subgroup of ( ℂ, +) (\mathbb{C},+) is isomorphic to ℤ D \mathbb{Z}^{D} for some D ∈ ℕ D\in\mathbb{N}. This is slightly more non-trivial when H = ( ℂ ∗, ⋅) H=(\mathbb{C}^{*},\cdot), but it is a standard fact that any finitely generated subgroup of ( ℂ ∗, ⋅) (\mathbb{C}^{*},\cdot) is isomorphic to ℤ D × ℤ / N ​ ℤ \mathbb{Z}^{D}\times\mathbb{Z}/N\mathbb{Z} for some non-negative integer D D and some N ∈ ℕ N\in\mathbb{N}. Finally, when H H is some elliptic curve over ℂ \mathbb{C}, we may use the fact, mentioned in Section 3.1, that H H is isomorphic to ℂ / L \mathbb{C}/L, where L L is some lattice of rank two in ℂ \mathbb{C}, to deduce that any finitely generated subgroup of H H is isomorphic to some subgroup of ℤ D × ℤ / n ​ ℤ × ℤ / m ​ ℤ \mathbb{Z}^{D}\times\mathbb{Z}/n\mathbb{Z}\times\mathbb{Z}/m\mathbb{Z} for some non-negative integer D D and some n, m ∈ ℕ n,m\in\mathbb{N}. ∎

We are now ready to prove Lemma 6.2

###### Proof of Lemma 6.2.

Let Γ \Gamma be the subgroup generated by S S. We can use Lemma 6.4 to view Γ \Gamma as a subgroup of ℤ l × ℤ / n ​ ℤ × ℤ / m ​ ℤ \mathbb{Z}^{l}\times\mathbb{Z}/n\mathbb{Z}\times\mathbb{Z}/m\mathbb{Z} for some integers n, m ≥ 1 n,m\geq 1 and some integer l ≥ 0. l\geq 0. Now, for any 0 ≤ i, j ≤ 9 0\leq i,j\leq 9, define

 | A i = { x ∈ ℤ: i ​ n / 10 ≤ x < ( i + 1) ​ n / 10 } ( mod ​ n) A_{i}=\{x\in\mathbb{Z}:in/10\leq x<(i+1)n/10\}\ \ ({\rm mod}\ n) |  |

and

 | B j = { x ∈ ℤ: j ​ m / 10 ≤ x < ( j + 1) ​ m / 10 } ( mod ​ m). B_{j}=\{x\in\mathbb{Z}:jm/10\leq x<(j+1)m/10\}\ \ ({\rm mod}\ m). |  |

Thus ℤ / n ℤ × ℤ / m ℤ = ∪ 0 ≤ i, j ≤ 9 ( A i × B j) \mathbb{Z}/n\mathbb{Z}\times\mathbb{Z}/m\mathbb{Z}=\cup_{0\leq i,j\leq 9}(A_{i}\times B_{j}). Moreover, let S i, j = S ∩ ( ℤ l × A i × B j) S_{i,j}=S\cap(\mathbb{Z}^{l}\times A_{i}\times B_{j}) for every 0 ≤ i, j ≤ 9 0\leq i,j\leq 9. Since

 | ∑ 0 ≤ i, j ≤ 9 | S i, j | = | S |, \sum_{0\leq i,j\leq 9}|S_{i,j}|=|S|, |  |

by the pigeonhole principle, there exist some 0 ≤ i, j ≤ 9 0\leq i,j\leq 9 such that | S i, j | ≥ | S | / 100 |S_{i,j}|\geq|S|/100.

Let π: ℤ l × ℤ / n ​ ℤ × ℤ / m ​ ℤ → ℤ l + 2 \pi:\mathbb{Z}^{l}\times\mathbb{Z}/n\mathbb{Z}\times\mathbb{Z}/m\mathbb{Z}\to\mathbb{Z}^{l+2} be the map satisfying

 | π ⁡ ( 𝒙, a ⁡ ( mod ​ n), b ⁡ ( mod ​ m)) = ( 𝒙, a, b) \pi(\bm{x},a\ ({\rm mod}\ n),b\ ({\rm mod}\ m))=(\bm{x},a,b) |  |

for all 𝒙 ∈ ℤ l \bm{x}\in\mathbb{Z}^{l} and a ∈ { 0, 1, …, n − 1 } a\in\{0,1,\dots,n-1\} and b ∈ { 0, 1, …, m − 1 } b\in\{0,1,\dots,m-1\}. We now claim that for any s 1, s 2, s 3, s 4 ∈ S i, j s_{1},s_{2},s_{3},s_{4}\in S_{i,j}, one has

(6.1) |  | π ⁡ ( s 1) + π ⁡ ( s 2) = π ⁡ ( s 3) + π ⁡ ( s 4) if and only if s 1 + s 2 = s 3 + s 4. \pi(s_{1})+\pi(s_{2})=\pi(s_{3})+\pi(s_{4})\ \ \text{if and only if}\ \ s_{1}+s_{2}=s_{3}+s_{4}. |  |

In order to see this, first note that since π − 1 \pi^{-1} is just the projection map, it suffices to check that equality on the right hand side implies equality on the left hand side. Writing

 | s l = ( 𝒙 l, a l ​ ( mod ​ n), b l ​ ( mod ​ m)) s_{l}=(\bm{x}_{l},a_{l}\ ({\rm mod}\ n),b_{l}\ ({\rm mod}\ m)) |  |

for every 1 ≤ l ≤ 4 1\leq l\leq 4, we see that s 1 + s 2 = s 3 + s 4 s_{1}+s_{2}=s_{3}+s_{4} implies that

 | a 1 + a 2 − a 3 − a 4 ≡ 0 ​ ( mod ​ n) and b 1 + b 2 − b 3 − b 4 ≡ 0 ​ ( mod ​ m). a_{1}+a_{2}-a_{3}-a_{4}\equiv 0\ ({\rm mod}\ n)\ \ \text{and}\ \ b_{1}+b_{2}-b_{3}-b_{4}\equiv 0\ ({\rm mod}\ m). |  |

Since i ​ n / 10 ≤ a 1, a 2, a 3, a 4 < ( i + 1) ​ n / 10 in/10\leq a_{1},a_{2},a_{3},a_{4}<(i+1)n/10, we see that

 | a 1 + a 2 − a 3 − a 4 ∈ [− n / 5, n / 5] ∩ ℤ. a_{1}+a_{2}-a_{3}-a_{4}\in[-n/5,n/5]\cap\mathbb{Z}. |  |

The preceding congruence condition now necessitates that a 1 + a 2 = a 3 + a 4 a_{1}+a_{2}=a_{3}+a_{4}. A similar argument gives us that b 1 + b 2 = b 3 + b 4 b_{1}+b_{2}=b_{3}+b_{4}.

Thus, writing S 1 = π ⁡ ( S i, j) S_{1}=\pi(S_{i,j}), the equivalence in ( 6.1) implies that

 | | S 1 + S 1 | = | S i, j + S i, j | ≤ | S + S | ≤ K ​ | S | ≤ 100 ​ K | S i, j | = 100 ​ K ​ | S 1 | |S_{1}+S_{1}|=|S_{i,j}+S_{i,j}|\leq|S+S|\leq K|S|\leq 100K|S_{i,j}|=100K|S_{1}| |  |

Since S 1 ⊆ ℤ l + 2 S_{1}\subseteq\mathbb{Z}^{l+2}, we may now apply Lemma 6.3 to find some subset S 1 ′ ⊆ S 1 S_{1}^{\prime}\subseteq S_{1} such that | S 1 ′ | ≥ | S 1 | / ( 100 ​ K) C ′ |S_{1}^{\prime}|\geq|S_{1}|/(100K)^{C^{\prime}} and

 | S 1 ′ ⊂ { n 1 𝒙 1 + ⋯ + n d 𝒙 d: n 1, …, n d ∈ ℤ }, S_{1}^{\prime}\subset\{n_{1}\bm{x}_{1}+\dots+n_{d}\bm{x}_{d}:n_{1},\dots,n_{d}\in\mathbb{Z}\}, |  |

where 𝒙 1, …, 𝒙 d ∈ ℤ l + 2 \bm{x}_{1},\dots,\bm{x}_{d}\in\mathbb{Z}^{l+2} are some elements and 1 ≤ d ≤ C ​ log ⁡ ( 400 ​ K) 1\leq d\leq C\log(400K) is some integer. This implies that

 | π − 1 ( S 1 ′) ⊂ { n 1 π − 1 ( 𝒙 1) + ⋯ + n d π 1 − 1 ( 𝒙 d): n 1, …, n d ∈ ℤ }. \pi^{-1}(S_{1}^{\prime})\subset\{n_{1}\pi^{-1}(\bm{x}_{1})+\dots+n_{d}\pi_{1}^{-1}(\bm{x}_{d}):n_{1},\dots,n_{d}\in\mathbb{Z}\}. |  |

Setting S ′ = π − 1 ​ ( S 1 ′) S^{\prime}=\pi^{-1}(S_{1}^{\prime}) finishes the proof of Lemma 6.2. ∎

We now present our proof of Lemma 6.1.

###### Proof of Lemma 6.1.

Since n ≥ 2 n\geq 2, we have that | 2 ​ S | ≤ | n ​ S | |2S|\leq|nS|, and so, whenever 2 ≤ n ≤ 16 2\leq n\leq 16, we may apply Lemma 6.1 and adjust the implicit constant in the Vinogradov notation to obtain the desired result. Thus, we assume that n > 16 n>16, in which case, writing k = ⌊ ( log ⁡ n) / ( log ⁡ 2) ⌋ k=\lfloor(\log n)/(\log 2)\rfloor, we see that k ≥ 4 k\geq 4. Now since | 2 k ​ S | ≤ | n ​ S | ≤ K ​ | S | |2^{k}S|\leq|nS|\leq K|S|, we get that

 | K ≥ | 2 k ​ S | | S | = ∏ 1 ≤ j ≤ k | 2 j ​ S | | 2 j − 1 ​ S |, K\geq\frac{|2^{k}S|}{|S|}=\prod_{1\leq j\leq k}\frac{|2^{j}S|}{|2^{j-1}S|}, |  |

whence, there exists some 1 ≤ j ≤ k 1\leq j\leq k such that

(6.2) |  | | 2 j ​ S | = | 2 j − 1 ​ S + 2 j − 1 ​ S | ≤ K 1 / k ​ | 2 j − 1 ​ S |. |2^{j}S|=|2^{j-1}S+2^{j-1}S|\leq K^{1/k}|2^{j-1}S|. |  |

Applying Lemma 6.2 for the set 2 j − 1 ​ S 2^{j-1}S, we get that there exists some set X ⊆ 2 j − 1 ​ S X\subseteq 2^{j-1}S such that

(6.3) |  | | X | ≫ | 2 j − 1 ​ S | K C / k and X ⊆ { n 1 ξ 1 + ⋯ + n d ξ d: n 1, …, n d ∈ ℤ }, |X|\gg\frac{|2^{j-1}S|}{K^{C/k}}\ \ \text{and}\ \ X\subseteq\{n_{1}\xi_{1}+\dots+n_{d}\xi_{d}:n_{1},\dots,n_{d}\in\mathbb{Z}\}, |  |

for some

 | d ≪ 1 + log ⁡ ( 4 ​ K) k d\ll 1+\frac{\log(4K)}{k} |  |

and some points ξ 1, …, ξ d ∈ H \xi_{1},\dots,\xi_{d}\in H.

Thus, it suffices to prove that there exists a large subset of S S which is contained in a translate of the set − X -X. In order to do this, note that

 | | X | ​ | S | = ∑ y ∈ X + S | ( y − X) ∩ S | ≤ | X + S | ​ max y ∈ X + S ​ | ( y − X) ∩ S |. |X||S|=\sum_{y\in X+S}|(y-X)\cap S|\leq|X+S|\max_{y\in X+S}|(y-X)\cap S|. |  |

Hence, it suffices to show that

 | | X + S | | X | ≪ K C ′ / k, \frac{|X+S|}{|X|}\ll K^{C^{\prime}/k}, |  |

for some absolute constant C ′ > 0 C^{\prime}>0. In order to see this, we combine the fact that X ⊆ 2 j − 1 ​ S X\subseteq 2^{j-1}S along with ( 6.2) and ( 6.3) to get that

 | | X + S | | X | ≤ | 2 j − 1 ​ S + 2 j − 1 ​ S | | X | ≪ K C / k ​ | 2 j ​ S | | 2 j − 1 ​ S | ≪ K ( C + 1) / k. \frac{|X+S|}{|X|}\leq\frac{|2^{j-1}S+2^{j-1}S|}{|X|}\ll K^{C/k}\frac{|2^{j}S|}{|2^{j-1}S|}\ll K^{(C+1)/k}. |  |

This concludes our proof of Lemma 6.1. ∎

We briefly remark that structural results akin to Freiman’s inverse theorem are often used in unison with covering results. One such result is known as Ruzsa’s covering lemma.

###### Lemma 6.5.

Let G G be an abelian group, let A, B ⊆ G A,B\subseteq G be non-empty sets such that | A + B | ≤ K ​ | B | |A+B|\leq K|B|. Then there exists some non-empty set X ⊆ A X\subseteq A such that | X | ≤ K |X|\leq K and A ⊆ X + B − B. A\subseteq X+B-B.

This immediately combines with Lemma 6.2 to deliver the following result.

###### Lemma 6.6.

Let H H be a connected algebraic group of dimension 1 1, let A ⊆ H A\subseteq H be a finite, non-empty set such that | A + A | ≤ K ​ | A | |A+A|\leq K|A| for some K > 1 K>1. Then there exists some integer 1 ≤ d ≤ C ​ log ⁡ ( 400 ​ K) 1\leq d\leq C\log(400K), some finite subset T ⊊ H T\subsetneq H with rk ⁡ ( T) = d \mathrm{rk}(T)=d and some non-empty X ⊆ H X\subseteq H such that

 | | X | ≤ ( 100 ​ K) C ′ + 1 and A ⊆ X + T, |X|\leq(100K)^{C^{\prime}+1}\ \ \text{and}\ \ A\subseteq X+T, |  |

where C = 140 C=140 and C ′ = 110 C^{\prime}=110.

## 7. Proofs of main results

In this section, we present the proofs of all of our results mentioned in § 1 and § 2.

We begin by deducing Theorem 1.1 from Corollary 2.2.

###### Proof of Theorem 1.1.

Setting G G to be an elliptic curve in Weierstrass form ( 1.1), H = 𝔾 a H=\mathbb{G}_{a} and 𝒞 \mathcal{C} the correspondence given by ( x, y, x) (x,y,x), we can apply Corollary 2.2 to obtain the first part of Theorem 1.1. We can proceed similarly with H = 𝔾 m H=\mathbb{G}_{m} to obtain the desired conclusion for geometric progressions. Setting 𝒞 \mathcal{C} equal to ( x, y, z), x = ( u + z) 2 (x,y,z),x=(u+z)^{2} we get the bound on successive squares. Also, for example choosing z 2 = x z^{2}=x, we can also bound the length of arithmetic progressions in certain higher genus curves. ∎

We will now prove Theorem 1.3 by combining Theorem 2.1 and Lemma 6.1.

###### Proof of Theorem 1.3.

Let k ≥ 1 k\geq 1 and d ≥ 2 d\geq 2 be integers, let g ∈ ℕ g\in\mathbb{N} be sufficiently large in terms of d, k d,k. We may further assume that | g ​ A | ≤ | A | k |gA|\leq|A|^{k} since otherwise we would be done. In this case, we may apply Lemma 6.1 to find some ξ 1, …, ξ r ∈ G \xi_{1},\dots,\xi_{r}\in G and some A ′ ⊆ A A^{\prime}\subseteq A such that r ≪ k ​ log ⁡ | A | / log ⁡ g r\ll k\log|A|/\log g and

 | | A ′ | ≫ | A | 1 − C ​ k / log ⁡ g and A ′ ⊆ { n 1 ξ 1 + ⋯ + n d ξ d: n 1, …, n d ∈ ℤ }. |A^{\prime}|\gg|A|^{1-Ck/\log g}\ \ \text{and}\ \ A^{\prime}\subseteq\{n_{1}\xi_{1}+\dots+n_{d}\xi_{d}:n_{1},\dots,n_{d}\in\mathbb{Z}\}. |  |

The latter condition implies that the subgroup generated by A ′ A^{\prime} has rank at most r r, and so, we may apply Theorem 2.1 to deduce that

 | | 𝒞 1 ​ ( A) + ⋯ + 𝒞 g ​ ( A) | \displaystyle|\mathcal{C}_{1}(A)+\dots+\mathcal{C}_{g}(A)| | ≥ | 𝒞 1 ​ ( A ′) + ⋯ + 𝒞 2 ​ k ​ ( A ′) | \displaystyle\geq|\mathcal{C}_{1}(A^{\prime})+\dots+\mathcal{C}_{2k}(A^{\prime})| |  |

 |  | ≥ c ​ ( d, 2 ​ k) − 1 − r ​ | A ′ | 2 ​ k \displaystyle\geq c(d,2k)^{-1-r}|A^{\prime}|^{2k} |  |

 |  | ≫ k c ( d, 2 k) − 1 | A | − k ​ log ⁡ c ​ ( d, 2 ​ k) log ⁡ g | A ′ | 2 ​ k \displaystyle\gg_{k}c(d,2k)^{-1}|A|^{-\frac{k\log c(d,2k)}{\log g}}|A^{\prime}|^{2k} |  |

 |  | ≫ k, d | A | 2 ​ k − 2 ​ C ​ k 2 log ⁡ g − k ​ log ⁡ c ​ ( 2 ​ k, d) log ⁡ g. \displaystyle\gg_{k,d}|A|^{2k-\frac{2Ck^{2}}{\log g}-\frac{k\log c(2k,d)}{\log g}}. |  |

Choosing g g to be sufficiently large so as to ensure that

 | 2 ​ C ​ k 2 log ⁡ g < k / 2 and k ​ log ⁡ c ​ ( d, 2 ​ k) log ⁡ g < k / 2 and ​ 2 ​ k < g, \frac{2Ck^{2}}{\log g}<k/2\ \ \text{and}\ \ \frac{k\log c(d,2k)}{\log g}<k/2\ \ \text{and}\ \ 2k<g, |  |

we get that

 | | 𝒞 1 ( A) + ⋯ + 𝒞 g ( A) | ≥ | 𝒞 1 ( A) + ⋯ + 𝒞 2 ​ k ( A) | ≫ k, d | A | k. |\mathcal{C}_{1}(A)+\dots+\mathcal{C}_{g}(A)|\geq|\mathcal{C}_{1}(A)+\dots+\mathcal{C}_{2k}(A)|\gg_{k,d}|A|^{k}. |  |

This finishes the proof of Theorem 1.3. ∎

Theorem 1.5 is a special case of Theorem 2.6. Indeed, if 𝒱 \mathcal{V} is an irreducible subvariety of G g G^{g} which is not a coset of a subgroup, then we have the trivial inequality codef ⁡ ( 𝒱) ≤ dim ⁡ ( 𝒱) − 1 {\rm codef}(\mathcal{V})\leq{\rm dim}(\mathcal{V})-1. Thus, we will now prove Theorem 1.8.

###### Proof of Theorem 1.8.

Since | A + A | ≤ K ​ | A | |A+A|\leq K|A|, we may apply Lemma 6.6 to deduce that A ⊆ Y + T A\subseteq Y+T, where T T is contained in a subgroup Γ \Gamma of H H with rank d ≪ log ⁡ K d\ll\log K and Y ⊂ H Y\subset H satisfies | Y | ≤ K O ⁡ ( 1) |Y|\leq K^{O(1)}. Now, since X ⊆ A X\subseteq A, this means that X X is also contained in at most K O ⁡ ( 1) K^{O(1)} translates of some subgroup Γ \Gamma. By the pigeonhole principle, we can find some X ′ ⊆ X X^{\prime}\subseteq X with | X ′ | ≥ | X | / K O ⁡ ( 1) |X^{\prime}|\geq|X|/K^{O(1)} such that X ′ X^{\prime} is contained in a translate of Γ \Gamma, and so, X ′ X^{\prime} is contained in a subgroup of rank d + 1 d+1. We now apply Theorem 4.2 to deduce that

 | | π 2 ​ ( ( X g × ℬ) ∩ 𝒱) | \displaystyle|\pi_{2}((X^{g}\times\mathcal{B})\cap\mathcal{V})| | ≥ | π 2 ​ ( ( X ′ g × ℬ) ∩ 𝒱) | ≥ | X ′ | g C 2 + d \displaystyle\geq|\pi_{2}((X^{\prime g}\times\mathcal{B})\cap\mathcal{V})|\geq\frac{|X^{\prime}|^{g}}{C^{2+d}} |  |

 |  | ≥ | X | g K O ⁡ ( g) ​ 2 C ′ ​ log ⁡ K ≫ | X | g K C ′′ \displaystyle\geq\frac{|X|^{g}}{K^{O(g)}2^{C^{\prime}\log K}}\gg\frac{|X|^{g}}{K^{C^{\prime\prime}}} |  |

where C, C ′, C ′′ > 0 C,C^{\prime},C^{\prime\prime}>0 are constants depending only on g, deg ⁡ ( 𝒱) g,\deg(\mathcal{V}). ∎

Next, we prove Theorem 2.1.

###### Proof of Theorem 2.1.

We consider the variety 𝒱 sum \mathcal{V}_{\rm sum} as described in ( 5.1) and note that for any finite set A ⊂ G A\subset G, the set

 | π 2 ​ ( ( A g × H ¯) ∩ 𝒱 sum) = 𝒞 1 ​ ( A) + ⋯ + 𝒞 g ​ ( A). \pi_{2}((A^{g}\times\overline{H})\cap\mathcal{V}_{\rm sum})=\mathcal{C}_{1}(A)+\dots+\mathcal{C}_{g}(A). |  |

Proposition 5.1 implies that this variety 𝒱 sum \mathcal{V}_{\rm sum} is non-degenerate of dimension g g and the projections π 1 \pi_{1} to G g G^{g} is surjective and π 2 \pi_{2} to H ¯ \overline{H} restricted to 𝒱 \mathcal{V} is dominant. Thus, we may apply Lemma 4.2 to deduce that

 | | 𝒞 1 ​ ( A) + ⋯ + 𝒞 g ​ ( A) | ≥ c ​ ( g, deg ⁡ ( V)) 1 + r ​ | A | g. ∎ |\mathcal{C}_{1}(A)+\dots+\mathcal{C}_{g}(A)|\geq c(g,\deg(V))^{1+r}|A|^{g}.\qed |  |

We will now deduce Corollary 2.2 from Theorem 2.1.

###### Proof of Corollary 2.2.

Throughout this proof, let C 1, C 2, C 3 > 0 C_{1},C_{2},C_{3}>0 be positive constants depending only on d d. Suppose that A A is a generalised arithmetic progression in 𝒞 ⁡ ( Γ) \mathcal{C}(\Gamma) of rank k k for some k ∈ ℕ k\in\mathbb{N}. We will first show that k ≤ C 1 + r k\leq C^{1+r} for some constant 0 < C ≪ d 1 0<C\ll_{d}1. In order to see this, let

(7.1) |  | P ′ = { P 0 + ℓ 1 ​ P 1 + ⋯ + ℓ k ​ P ℓ: 0 ≤ ℓ i ≤ 1 }. P^{\prime}=\{P_{0}+\ell_{1}P_{1}+\cdots+\ell_{k}P_{\ell}:0\leq\ell_{i}\leq 1\}. |  |

Since L 1, …, L k ≥ 2 L_{1},\dots,L_{k}\geq 2, we get that P ′ ⊆ P P^{\prime}\subseteq P. Since P P is proper, we get that P ′ P^{\prime} is also proper, and so, one has

 | | P ′ + P ′ | ≤ 3 k = | P ′ | log ⁡ 3 log ⁡ 2. |P^{\prime}+P^{\prime}|\leq 3^{k}=|P^{\prime}|^{\frac{\log 3}{\log 2}}. |  |

Applying Theorem 2.1 for P ′ P^{\prime}, we get that

 | | P ′ | 2 ​ C 1 − 1 − r ≪ | P ′ + P ′ | ≪ | P ′ | log ⁡ 3 log ⁡ 2, |P^{\prime}|^{2}C_{1}^{-1-r}\ll|P^{\prime}+P^{\prime}|\ll|P^{\prime}|^{\frac{\log 3}{\log 2}}, |  |

whence 2 k = | P ′ | ≤ C 2 1 + r 2^{k}=|P^{\prime}|\leq C_{2}^{1+r}. Now, we consider the set P P and use the preceding upper bound on | P ′ | |P^{\prime}| to observe that

 | | P + P | ≤ ( 2 ​ L 1 − 1) ​ … ​ ( 2 ​ L k − 1) ≤ 2 k ​ L 1 ​ … ​ L k = 2 k ​ | P | ≤ C 2 1 + r ​ | P |. |P+P|\leq(2L_{1}-1)\dots(2L_{k}-1)\leq 2^{k}L_{1}\dots L_{k}=2^{k}|P|\leq C_{2}^{1+r}|P|. |  |

We can now apply Theorem 2.1 to deduce that

 | C 1 − 1 − r ​ | P | 2 ≤ | P + P | ≤ C 2 1 + r ​ | P |, C_{1}^{-1-r}|P|^{2}\leq|P+P|\leq C_{2}^{1+r}|P|, |  |

and so, we obtain the desired claim | P | ≤ C 3 1 + r |P|\leq C_{3}^{1+r}. ∎

We now consider Theorem 2.3. As in the proof of Theorem 1.3, we will derive this by putting together Theorem 2.1 and Lemma 6.1.

###### Proof of Theorem 2.3.

Let A ⊆ G A\subseteq G be a finite, non-empty set. We may assume that | A + A | ≤ | A | 1 + δ |A+A|\leq|A|^{1+\delta}, since otherwise we would be done. In this case, we apply Lemma 6.2 to obtain ξ 1, …, ξ r ∈ G \xi_{1},\dots,\xi_{r}\in G such that

 | r ≤ 140 ​ ( δ ​ log ⁡ | A | + log ⁡ 400) r\leq 140(\delta\log|A|+\log 400) |  |

and some subset A ′ ⊆ A A^{\prime}\subseteq A satisfying

 | | A ′ | ≥ | A | ( 100 ​ | A | δ) 110 and A ′ ⊆ { n 1 ξ 1 + ⋯ + n r ξ r: n 1, …, n r ∈ ℤ }. |A^{\prime}|\geq\frac{|A|}{(100|A|^{\delta})^{110}}\ \ \text{and}\ \ A^{\prime}\subseteq\{n_{1}\xi_{1}+\dots+n_{r}\xi_{r}:n_{1},\dots,n_{r}\in\mathbb{Z}\}. |  |

The latter condition implies that A ′ A^{\prime} is contained in a subgroup of rank ≤ r \leq r whence we may apply Theorem 2.1 to deduce that

 | | 𝒞 ⁡ ( A ′) + 𝒞 ⁡ ( A ′) | \displaystyle|\mathcal{C}(A^{\prime})+\mathcal{C}(A^{\prime})| | ≥ c ​ ( d, 2) − ( r + 1) ​ | A ′ | 2 \displaystyle\geq c(d,2)^{-(r+1)}|A^{\prime}|^{2} |  |

 |  | ≥ c ​ | A | 2 − δ ⁡ ( 140 ​ log ⁡ c ⁡ ( d, 2) + 220). \displaystyle\geq c|A|^{2-\delta(140\log c(d,2)+220)}. |  |

Combining this with the fact that | 𝒞 ⁡ ( A) + 𝒞 ⁡ ( A) | ≥ | 𝒞 ⁡ ( A ′) + 𝒞 ⁡ ( A ′) | |\mathcal{C}(A)+\mathcal{C}(A)|\geq|\mathcal{C}(A^{\prime})+\mathcal{C}(A^{\prime})| then delivers the claimed estimate. ∎

We prove Theorem 2.6 by combining Theorem 3.7 and Lemma 6.6.

###### Proof of Theorem 2.6.

Since 𝒱 \mathcal{V} is not a co-set, we have for every subgroup Γ \Gamma of rank r r, the equality

 | 𝒱 ∩ Γ = ⋃ i = 1 S ( γ i + H i) ∩ Γ, \mathcal{V}\cap\Gamma=\bigcup_{i=1}^{S}(\gamma_{i}+H_{i})\cap\Gamma, |  |

where the H i H_{i} are connected subgroups whose degree is bounded in terms of the degree of 𝒱 \mathcal{V}, and S ≤ c 1 + r S\leq c^{1+r}, where c = c ⁡ ( deg ⁡ ( 𝒱), g) > 0 c=c(\deg(\mathcal{V}),g)>0 is a constant, see Theorem 3.7.

As | A + A | ≤ K ​ | A | |A+A|\leq K|A|, there exists 1 ≤ d ≤ C ​ log ⁡ ( 400 ​ K) 1\leq d\leq C\log(400K), some finite subset T ⊊ G T\subsetneq G, with rk ​ ( T) = d \text{rk}(T)=d and some non-empty subset X ⊊ G X\subsetneq G, such that | X | ≤ ( 100 ​ K) C ′ + 1 |X|\leq(100K)^{C^{\prime}+1}, and A ⊆ X + T A\subseteq X+T, where C = 140, C ′ = 110 C=140,C^{\prime}=110, see Lemma 6.6. We deduce that A g A^{g} is contained in the translate of a finite subset T g T_{g} of rank g ​ d gd translated by a set X g X_{g} of cardinality ( 100 ​ K) g ​ C ′ + g (100K)^{gC^{\prime}+g}. Let Γ A \Gamma_{A} be the group generated by the elements in T g T_{g}. Note that the rank r r of Γ A \Gamma_{A} satisfies

 | r ≤ g ​ d ≪ g ​ log ⁡ ( 100 ​ K). r\leq gd\ll g\log(100K). |  |

Let x ∈ X g x\in X_{g}. From Theorem 3.7 it follows that γ ∈ ( 𝒱 − x) ∩ Γ A \gamma\in(\mathcal{V}-x)\cap\Gamma_{A} either lies in a co-set of degree bounded in terms of the degree of 𝒱 \mathcal{V} or in a set of cardinality c 1 + r c^{1+r}. The number of co-sets for fixed x x is bounded by c 1 + g ​ r c^{1+gr} and so applying Lemma 4.4 to each co-set contained in 𝒱 \mathcal{V}, we get the desired bound. ∎

## Appendix A Diophantine equations

We show that our results related to Bremner’s conjecture have some consequences for the Mordell–Lang conjecture. Roughly speaking, the theorems of David–Philippon and Evertse–Schmidt–Schlickewei give very uniform bounds on the number of points on a variety that lie on a finitely generated group. However, they generally do not provide effective bounds for the height of these points. The situation is, in a strong sense even more dire for elliptic curves. The points on an elliptic curve with coordinates in a number field form a finitely generated group, but there is no known algorithm to determine its generators. It is straightforward to pass from a number estimate to a (partly) effective version of Mordell–Lang. For example for a given curve C C with a bound t t on the number of rational points C ⁡ ( K) C(K) (with K K being some number field), we can easily say that the rational points on C t + 1 ​ ( K) C^{t+1}(K) lie on a finite union of proper subvarieties given by setting some coordinates equal to each other. However, this is still a far cry from actually determining the Zariski-closure of C t + 1 ​ ( K) C^{t+1}(K). Our work does not resolve this issue in general but, fixing a number field K K, and allowing for a very high dimensional power of an elliptic curve E t E^{t}, we can construct large families of surfaces, for which we can determine the Zariski-closure of their rational points. In what follows we let E E be an elliptic curve in Weierstrass form given by

 | y 2 = x 3 + a ​ x + b, y^{2}=x^{3}+ax+b, |  |

with a, b ∈ K a,b\in K, where K K is a number field. Let r r be the rank of E ⁡ ( K) E(K). A tuple ( a 1, a 2, …, a t) (a_{1},a_{2},\dots,a_{t}) forms an arithmetic progression if and only if it is a point on the plane P P in 𝔸 t \mathbb{A}^{t} defined by the equations

(A.1) |  | Z j + 2 − 2 ​ Z j + 1 + Z j = 0. \displaystyle Z_{j+2}-2Z_{j+1}+Z_{j}=0. |  |

for j ∈ { 1, …, t − 2 } j\in\{1,\dots,t-2\}.

Now consider the subvariety of ( 𝔸 2) t × 𝔸 t (\mathbb{A}^{2})^{t}\times\mathbb{A}^{t} defined by the equations

 | Y j 2 − X j 3 − a ​ X j − b = 0 \displaystyle Y_{j}^{2}-X_{j}^{3}-aX_{j}-b=0 |  |

for j ∈ { 1, …, t } j\in\{1,\dots,t\} and

 | Z j + 2 − 2 ​ Z j + 1 + Z j = 0 \displaystyle Z_{j+2}-2Z_{j+1}+Z_{j}=0 |  |

for j ∈ { 1, …, t − 2 } j\in\{1,\dots,t-2\}. Such a variety is merely the product U t × P U^{t}\times P of t t copies of an affine elliptic curve

 | U: y 2 = x 3 + a ​ x + b \displaystyle U:y^{2}=x^{3}+ax+b |  |

with the plane P P, and thus has dimension t + 2 t+2. The points on this variety correspond to t t -tuples of points of an elliptic curve and t t -term arithmetic progressions, with no relation between them.

Finally we impose algebraic relations

 | P i ( X i, Y i, Z i) = 0, i = 1, …, t \displaystyle P_{i}(X_{i},Y_{i},Z_{i})=0,\penalty\ \penalty\ i=1,\dots,t |  |

between the points on the elliptic curve, and the terms of the arithmetic progression. So we also ask that P i ∉ K ⁡ [X i, Y i] ∪ K ⁡ [Z i] P_{i}\notin K[X_{i},Y_{i}]\cup K[Z_{i}] is irreducible such that they induce a correspondence. For example, one can take

 | P i ( X i, Y i, Z i) = X i − Z i 2, i = 1, …, t, \displaystyle P_{i}(X_{i},Y_{i},Z_{i})=X_{i}-Z_{i}^{2},\penalty\ \penalty\ i=1,\dots,t, |  |

which encodes the condition that the x x -coordinates of the points on U U should be squares of elements of an arithmetic progression. Each of these new relations P i P_{i} decreases the dimension by one, because they only involve the variables ( X i, Y i, Z i) (X_{i},Y_{i},Z_{i}). It follows that the subvariety of U t × P U^{t}\times P defined by the t t new relations is a surface S A S_{A}. A similar construction works with the quadratic equations

(A.2) |  | Z j + 1 Z 1 = Z j Z 2, j = 2, …, t − 1. \displaystyle Z_{j+1}Z_{1}=Z_{j}Z_{2},\penalty\ \penalty\ j=2,\dots,t-1. |  |

We get a variety U t × Q U^{t}\times Q and imposing the algebraic conditions given by P i P_{i} result in a surface S G S_{G}. We denote by D ⊊ S A, S B D\subsetneq S_{A},S_{B}, the subvariety, that is given by the additional equation Z 1 = Z 2 Z_{1}=Z_{2}. Thus the points of D D correspond to degenerate arithmetic or geometric progressions.

This is all slightly technical but for P i = Z i − X i P_{i}=Z_{i}-X_{i} the rational point S A ​ ( K) S_{A}(K) correspond to arithmetic progressions in E ⁡ ( K) E(K) of length t t and similarly for S G ​ ( K) S_{G}(K) and geometric progressions. It is not hard to see, and we give the details in the paragraph below, that these surfaces S A, S B S_{A},S_{B} are then of general type. The Mordell–Lang conjecture predicts that the Zariski-closure of S A ​ ( K), S B ​ ( K) S_{A}(K),S_{B}(K) consists of a finite union of elliptic curves and points. This implies that there are only finitely many arithmetic or geometric sequences of length 3 in an elliptic curve.

In this setting, Corollary 2.2 delivers a more precise version that exactly predicts the distribution of rational points, albeit for t t depending on K K.

###### Theorem A.1.

For each d, r ≥ 0 d,r\geq 0, there exists and effectively computable t t, such that S A ​ ( K) = S B ​ ( K) = D ⁡ ( K) S_{A}(K)=S_{B}(K)=D(K).

The variety D D is either the empty set or a finite union of copies of the elliptic curve E E. We can embed 𝔸 3 ​ t \mathbb{A}^{3t} into ℙ 3 ​ t \mathbb{P}^{3t} via

 | ( X 1, Y 1 ​ …, X t, Y t, Z 1, …, Z t) ↪ [X 1, Y 1, …, X t, Y t, Z 1, …, Z t, 1] (X_{1},Y_{1}\dots,X_{t},Y_{t},Z_{1},\dots,Z_{t})\hookrightarrow[X_{1},Y_{1},\dots,X_{t},Y_{t},Z_{1},\dots,Z_{t},1] |  |

and the Zariski-closure S ¯ A \overline{S}_{A} of S A S_{A} is a projective surface. Let d 1, …, d t d_{1},\dots,d_{t} be the degrees P 1, …, P t P_{1},\dots,P_{t} and if S ¯ A \overline{S}_{A} is smooth, then the degree of the canonical class of S ¯ A \overline{S}_{A} is

 | d 1 + ⋯ + d t + t − 3, d_{1}+\cdots+d_{t}+t-3, |  |

see [25, Examples 5.1.1]. Thus S ¯ A \overline{S}_{A} is of general type. A similar argument works for S G S_{G}.

## Appendix B Degenerate polynomials

Let G, ℬ, π, π 2 G,\mathcal{B},\pi,\pi_{2} be as in Definition 1.7. We denote P ∈ ℂ ⁡ [x 1, …, x g] P\in\mathbb{C}[x_{1},\dots,x_{g}] to be degenerate with respect to 𝔾 g \mathbb{G}^{g} if the variety 𝒱 ⊆ 𝔾 a g × ℬ \mathcal{V}\subseteq\mathbb{G}_{a}^{g}\times\mathcal{B} defined by the equation P ⁡ ( x 1, …, x g) = t P(x_{1},\dots,x_{g})=t is degenerate. In this section, we briefly comment on possible ways to check whether a given polynomial P ∈ ℂ ⁡ [x 1, …, x g] P\in\mathbb{C}[x_{1},\dots,x_{g}] is degenerate with respect to G g G^{g} when G = 𝔾 a G=\mathbb{G}_{a} or G = 𝔾 m G=\mathbb{G}_{m}. In the latter case, it was shown by the second author [34] that the polynomial

 | ∑ 𝜶 ∈ E c 𝜶 ​ x 1 α 1 ​ … ​ x g α g, \sum_{\bm{\alpha}\in E}c_{\bm{\alpha}}x_{1}^{\alpha_{1}}\dots x_{g}^{\alpha_{g}}, |  |

where E ⊆ ℂ g E\subseteq\mathbb{C}^{g} is a finite, non-empty set and c 𝜶 ≠ 0 c_{\bm{\alpha}}\neq 0 for all 𝜶 ∈ E \bm{\alpha}\in E, is non-degenerate if and only if { ∑ 𝜶 ∈ E z 𝜶 ⋅ 𝜶: z 𝜶 ∈ ℂ } = ℂ g \{\sum_{\bm{\alpha}\in E}z_{\bm{\alpha}}\cdot\bm{\alpha}:z_{\bm{\alpha}}\in\mathbb{C}\}=\mathbb{C}^{g}.

We will now provide a criterion to check whether a polynomial P ∈ ℂ ⁡ [x 1, …, x g] P\in\mathbb{C}[x_{1},\dots,x_{g}] is non-degenerate with respect to 𝔾 a g \mathbb{G}_{a}^{g}.

###### Lemma B.1.

If P ∈ ℂ ⁡ [x 1, …, x g] P\in\mathbb{C}[x_{1},\dots,x_{g}] is degenerate with respect to 𝔾 a g \mathbb{G}_{a}^{g}, then there exists non-zero 𝐯 ∈ ℂ g \bm{v}\in\mathbb{C}^{g} such that the identity

 | 𝒗 ⋅ ( ( ∇ P) ​ ( x 1, …, x g)) = 0 \bm{v}\cdot((\nabla P)(x_{1},\dots,x_{g}))=0 |  |

holds.

###### Proof.

Let 𝒱 \mathcal{V} be given by the variety P ⁡ ( 𝒙) = t P(\bm{x})=t, where, by abuse of notation, we denote 𝒙 = ( x 1, …, x g) \bm{x}=(x_{1},\dots,x_{g}). Since G = 𝔾 a G=\mathbb{G}_{a} and 𝒱 \mathcal{V} is degenerate, one can deduce that

 | P ⁡ ( 𝒙) = F ⁡ ( L 1, …, L k) P(\bm{x})=F(L_{1},\dots,L_{k}) |  |

for some 0 ≤ k < g 0\leq k<g and some linear forms L 1, …, L k ∈ ℂ ⁡ [x 1, …, x g] L_{1},\dots,L_{k}\in\mathbb{C}[x_{1},\dots,x_{g}] and some F ∈ ℂ ⁡ [y 1, …, y k] F\in\mathbb{C}[y_{1},\dots,y_{k}]. Since k < g k<g, there exists some non-zero 𝒗 = ( v 1, …, v g) ∈ ℂ g \bm{v}=(v_{1},\dots,v_{g})\in\mathbb{C}^{g} such that the identity

 | L i ​ ( 𝒙) = L i ​ ( 𝒙 + t ⋅ 𝒗) L_{i}(\bm{x})=L_{i}(\bm{x}+t\cdot\bm{v}) |  |

holds for all 1 ≤ i ≤ k 1\leq i\leq k and all t ∈ ℝ t\in\mathbb{R}. Here t ⋅ 𝒗 = ( t ​ v 1, …, t ​ v g) t\cdot\bm{v}=(tv_{1},\dots,tv_{g}). In particular, we have the identity

 | P ⁡ ( 𝒙) = P ⁡ ( 𝒙 + t ⋅ 𝒗). P(\bm{x})=P(\bm{x}+t\cdot\bm{v}). |  |

Differentiating with respect to t t, we get that

 | 0 = ∑ j = 1 k ( ∂ F ∂ y j) ​ ( L 1 ​ ( 𝒙 + t ⋅ 𝒗), …, L k ​ ( 𝒙 + t ⋅ 𝒗)) ⋅ ∑ l = 1 g ( ∂ L j ∂ x l) ​ ( 𝒙 + t ⋅ 𝒗) ⋅ v l \displaystyle 0=\sum_{j=1}^{k}\left(\frac{\partial F}{\partial y_{j}}\right)(L_{1}(\bm{x}+t\cdot\bm{v}),\dots,L_{k}(\bm{x}+t\cdot\bm{v}))\cdot\sum_{l=1}^{g}\left(\frac{\partial L_{j}}{\partial x_{l}}\right)(\bm{x}+t\cdot\bm{v})\cdot v_{l} |  |

for all t ∈ ℝ t\in\mathbb{R}. Setting t = 0 t=0 and rearranging the sums, we get that

 | 0 \displaystyle 0 | = ∑ l = 1 g v l ​ ( ∑ j = 1 k ( ∂ F ∂ y j) ​ ( L 1 ​ ( 𝒙), …, L k ​ ( 𝒙)) ⋅ ( ∂ L j ∂ x l) ​ ( 𝒙)) = 𝒗 ⋅ ( ( ∇ P) ​ ( 𝒙)). ∎ \displaystyle=\sum_{l=1}^{g}v_{l}\left(\sum_{j=1}^{k}\left(\frac{\partial F}{\partial y_{j}}\right)(L_{1}(\bm{x}),\dots,L_{k}(\bm{x}))\cdot\left(\frac{\partial L_{j}}{\partial x_{l}}\right)(\bm{x})\right)=\bm{v}\cdot((\nabla P)(\bm{x})).\qed |  |

We will use this to prove that the polynomial P ⁡ ( x, y, z) = x ​ y + y ​ z + z ​ x P(x,y,z)=xy+yz+zx is non-degenerate with respect to 𝔾 a 3 \mathbb{G}_{a}^{3}. Indeed, if P P were to be degenerate with respect to 𝔾 a 3 \mathbb{G}_{a}^{3}, then Lemma B.1 implies that there would exist some non-zero 𝒗 = ( v 1, v 2, v 3) ∈ ℂ 3 \bm{v}=(v_{1},v_{2},v_{3})\in\mathbb{C}^{3} such that the identity

 | 𝒗 ⋅ ( ( ∇ P) ​ ( x, y, z)) = v 1 ​ ( y + z) + v 2 ​ ( x + y) + v 3 ​ ( z + x) = 0 \bm{v}\cdot((\nabla P)(x,y,z))=v_{1}(y+z)+v_{2}(x+y)+v_{3}(z+x)=0 |  |

holds. In particular, this would mean that

 | v 1 + v 2 = v 2 + v 3 = v 3 + v 1 = 0, v_{1}+v_{2}=v_{2}+v_{3}=v_{3}+v_{1}=0, |  |

that is, v 1 = v 2 = v 3 = 0 v_{1}=v_{2}=v_{3}=0. This contradicts the hypothesis that 𝒗 \bm{v} is non-zero, and so, P P must be non-degenerate with respect to 𝔾 a 3 \mathbb{G}_{a}^{3}.

## References

- [1] M. Bays and E. Breuillard (2021) Projective geometries arising from Elekes-Szabó problems. Ann. Sci. Éc. Norm. Supér. (4) 54 ( 3), pp. 627–681. External Links: ISSN 0012-9593,1873-2151, [Document][6], [Link][7], [MathReview (Piotr Pokora)][8] Cited by: §1, §1, §1, §1, §2.2, footnote 1.
- [2] E. Bombieri and U. Zannier (1996) Heights of algebraic points on subvarieties of abelian varieties. Ann. Sc. Norm. Super. Pisa, Cl. Sci., IV. Ser. 23 ( 4), pp. 779–792 ( English). External Links: ISSN 0391-173X, [Link][9] Cited by: §3.4, §4.
- [3] J. Bourgain and M. Chang (2004) On the size of k k -fold sum and product sets of integers. J. Amer. Math. Soc. 17 ( 2), pp. 473–497. External Links: ISSN 0894-0347,1088-6834, [Document][10], [Link][11], [MathReview (Ben Joseph Green)][12] Cited by: §1, §1, §2.2.
- [4] A. Bremner, J. H. Silverman, and N. Tzanakis (2000) Integral points in arithmetic progression on y 2 = x ⁡ ( x 2 − n 2) y^{2}=x(x^{2}-n^{2}). J. Number Theory 80 ( 2), pp. 187–208 ( English). External Links: ISSN 0022-314X, [Document][13] Cited by: §1.
- [5] A. Bremner and M. Ulas (2013) Rational points in geometric progressions on certain hyperelliptic curves. Publ. Math. Debr. 82 ( 3-4), pp. 669–683 ( English). External Links: ISSN 0033-3883, [Document][14] Cited by: §1.
- [6] A. Bremner (1999) On arithmetic progressions on elliptic curves. Experiment. Math. 8 ( 4), pp. 409–413. External Links: ISSN 1058-6458,1944-950X, [Link][15], [MathReview (Akio Tamagawa)][16] Cited by: §1, §1.
- [7] M. Chang (2009) Some consequences of the polynomial Freiman-Ruzsa conjecture. C. R. Math. Acad. Sci. Paris 347 ( 11-12), pp. 583–588. External Links: ISSN 1631-073X,1778-3569, [Document][17], [Link][18], [MathReview (Norbert Hegyvári)][19] Cited by: §1, §2.2.
- [8] A. Chernikov, Y. Peterzil, and S. Starchenko (2024) Model-theoretic Elekes-Szabó for stable and o-minimal hypergraphs. Duke Math. J. 173 ( 3), pp. 419–512. External Links: ISSN 0012-7094,1547-7398, [Document][20], [Link][21], [MathReview (Assaf Hasson)][22] Cited by: §1, §2.2.
- [9] A. Chernikov and S. Starchenko (2021) Model-theoretic Elekes-Szabó in the strongly minimal case. J. Math. Log. 21 ( 2), pp. Paper No. 2150004, 20. External Links: ISSN 0219-0613,1793-6691, [Document][23], [Link][24], [MathReview (Assaf Hasson)][25] Cited by: §1.
- [10] A. Cushman A note on the sum-product problem and the convex sumset problem. arXiv:2512.13849. Cited by: §1.
- [11] S. David and P. Philippon (2007) Minorations des hauteurs normalisées des sous-variétés des puissances des courbes elliptiques. Int. Math. Res. Pap. IMRP ( 3), pp. Art. ID rpm006, 113. External Links: ISSN 1687-3017,1687-3009, [MathReview (Timothy D. Browning)][26] Cited by: §1, §1, §1, §3.4, Theorem 3.7.
- [12] G. Elekes and L. Rónyai (2000) A combinatorial problem on polynomials and rational functions. J. Combin. Theory Ser. A 89 ( 1), pp. 1–20. External Links: ISSN 0097-3165,1096-0899, [Document][27], [Link][28], [MathReview (Volker Strehl)][29] Cited by: §1, §1.
- [13] G. Elekes and E. Szabó (2012) How to find groups? (and how to use them in Erdös geometry?). Combinatorica 32 ( 5), pp. 537–571. External Links: ISSN 0209-9683,1439-6912, [Document][30], [Link][31], [MathReview (Martin Klazar)][32] Cited by: §1, §1.
- [14] G. Elekes (1997) On the number of sums and products. Acta Arith. 81 ( 4), pp. 365–367. External Links: ISSN 0065-1036,1730-6264, [Document][33], [Link][34], [MathReview (Yuri Bilu)][35] Cited by: §1.
- [15] N. D. Elkies and Z. Klagsbrun (2024) ℤ 29 \mathbb{Z}^{29} in E ⁡ ( ℚ) E(\Q). Note: Number theory list server archives Cited by: §1.
- [16] N. D. Elkies and Z. Klagsbrun (2020) New rank records for elliptic curves having rational torsion. In ANTS XIV. Proceedings of the fourteenth algorithmic number theory symposium, Auckland, New Zealand, virtual event, June 29 – July 4, 2020, pp. 233–250 ( English). External Links: ISBN 978-1-935107-07-1; 978-1-935107-08-8, [Document][36] Cited by: §1.
- [17] P. Erdős and E. Szemerédi (1983) On sums and products of integers. ( English). Note: Studies in Pure Mathematics, Mem. of P. Turán, 213-218 (1983). Cited by: §1, §1.
- [18] J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt (2002) Linear equations in variables which lie in a multiplicative group. Ann. Math. (2) 155 ( 3), pp. 807–836 ( English). External Links: ISSN 0003-486X, [Document][37] Cited by: §1, §1, §3.4, §3.4, Theorem 3.7.
- [19] G. Faltings (1983) Endlichkeitssätze für abelsche Varietäten über Zahlkörpern. Invent. Math. 73 ( 3), pp. 349–366. External Links: ISSN 0020-9910, [Document][38], [Link][39], [MathReview (James Milne)][40] Cited by: §2.1.
- [20] W. Fulton (1998) Intersection theory.. 2nd ed. edition, Ergeb. Math. Grenzgeb., 3. Folge, Vol. 2, Berlin: Springer ( English). External Links: ISSN 0071-1136, ISBN 3-540-62046-X Cited by: §3.2.
- [21] N. Garcia-Fritz and H. Pasten (2021) Elliptic curves with long arithmetic progressions have large rank. Int. Math. Res. Not. IMRN ( 10), pp. 7394–7432. External Links: ISSN 1073-7928,1687-0247, [Document][41], [Link][42], [MathReview (Matteo Longo)][43] Cited by: §1, §2.1.
- [22] W. T. Gowers, B. Green, F. Manners, and T. Tao (2025) On a conjecture of Marton. Ann. of Math. (2) 201 ( 2), pp. 515–549. External Links: ISSN 0003-486X,1939-8980, [Document][44], [Link][45], [MathReview Entry][46] Cited by: §1, §1, §2.2, §6.
- [23] A. Grothendieck (1967) Éléments de géométrie algébrique. IV: Étude locale des schémas et des morphismes de schémas (Quatrième partie). Rédigé avec la colloboration de J. Dieudonné. Publ. Math., Inst. Hautes Étud. Sci. 32, pp. 1–361 ( French). External Links: ISSN 0073-8301, [Link][47] Cited by: §4.
- [24] B. Hanson, O. Roche-Newton, and D. Zhelezov (2020) On iterated product sets with shifts, II. Algebra Number Theory 14 ( 8), pp. 2239–2260. External Links: ISSN 1937-0652,1944-7833, [Document][48], [Link][49], [MathReview (Elad Aigner-Horev)][50] Cited by: §1, §1, §1, §1.
- [25] M. Hindry and J. H. Silverman (2000) Diophantine geometry. An introduction. Grad. Texts Math., Vol. 201, New York, NY: Springer ( English). External Links: ISSN 0072-5285, ISBN 0-387-98981-1; 0-387-98975-7 Cited by: Appendix A, §1.
- [26] Y. Jing, S. Roy, and C. Tran (2022) Semialgebraic methods and generalized sum-product phenomena. Discrete Anal., pp. Paper No. 18, 23. External Links: ISSN 2397-3129, [MathReview (Tobias Kaiser)][51] Cited by: §1.
- [27] G. Jones and H. Schmidt (2021) Pfaffian definitions of Weierstrass elliptic functions. Math. Ann. 379 ( 1-2), pp. 825–864. External Links: ISSN 0025-5831,1432-1807, [Document][52], [Link][53], [MathReview (Lei Yang)][54] Cited by: §4.
- [28] M. Kamel and M. Sadek (2019) Sequences of consecutive squares on quartic elliptic curves. Funct. Approximatio, Comment. Math. 60 ( 2), pp. 245–252 ( English). External Links: ISSN 0208-6573, [Document][55] Cited by: §1.
- [29] M. Laurent (1984) Équations diophantiennes exponentielles. Invent. Math. 78 ( 2), pp. 299–327. External Links: ISSN 0020-9910, [Document][56], [Link][57], [MathReview (D. J. Lewis)][58] Cited by: §3.4, §3.4, Theorem 3.7.
- [30] J. M. Lee (2013) Introduction to smooth manifolds. 2nd revised ed edition, Grad. Texts Math., Vol. 218, New York, NY: Springer ( English). External Links: ISSN 0072-5285, ISBN 978-1-4419-9981-8; 978-1-4419-9982-5, [Document][59] Cited by: §3.1.
- [31] D. W. Masser and G. Wüstholz (1990) Estimating isogenies on elliptic curves. Invent. Math. 100 ( 1), pp. 1–24 ( English). External Links: ISSN 0020-9910, [Document][60], [Link][61] Cited by: §2.1.
- [32] J. S. Milne (2017) Algebraic groups. The theory of group schemes of finite type over a field. Camb. Stud. Adv. Math., Vol. 170, Cambridge: Cambridge University Press ( English). External Links: ISBN 978-1-107-16748-3; 978-1-00-901858-6; 978-1-316-71173-6, [Document][62] Cited by: §3.1.
- [33] A. Mudgal On commuting pairs in arbitrary sets of 2 × 2 2\times 2 matrices. arXiv:2411.10404. Cited by: §2.2.
- [34] A. Mudgal (2024) An Elekes-Rónyai theorem for sets with few products. Int. Math. Res. Not. IMRN ( 13), pp. 10410–10424. External Links: ISSN 1073-7928,1687-0247, [Document][63], [Link][64], [MathReview (Frederick Robert William Meath Manners)][65] Cited by: Appendix B, §1, §1, §1, §1.
- [35] A. Mudgal (2024) Unbounded expansion of polynomials and products. Math. Ann. 390 ( 1), pp. 381–415. External Links: ISSN 0025-5831,1432-1807, [Document][66], [Link][67], [MathReview (Yuval Wigderson)][68] Cited by: §1, §1, §1, §1.
- [36] D. Pálvölgyi and D. Zhelezov (2021) Query complexity and the polynomial Freiman-Ruzsa conjecture. Adv. Math. 392, pp. Paper No. 108043, 18. External Links: ISSN 0001-8708,1090-2082, [Document][69], [Link][70], [MathReview (Bidisha Roy)][71] Cited by: §1, §1.
- [37] O. E. Raz, M. Sharir, and F. De Zeeuw (2016) Polynomials vanishing on Cartesian products: the Elekes-Szabó theorem revisited. Duke Math. J. 165 ( 18), pp. 3517–3566. External Links: ISSN 0012-7094,1547-7398, [Document][72], [Link][73], [MathReview (Tom Sanders)][74] Cited by: §1.
- [38] O. E. Raz, M. Sharir, and J. Solymosi (2016) Polynomials vanishing on grids: the Elekes-Rónyai problem revisited. Amer. J. Math. 138 ( 4), pp. 1029–1065. External Links: ISSN 0002-9327,1080-6377, [Document][75], [Link][76], [MathReview (Oliver Roche-Newton)][77] Cited by: §1.
- [39] I. R. Shafarevich (2013) Basic algebraic geometry 1. Varieties in projective space. Translated from the Russian by Miles Reid. 3rd ed. edition, Berlin: Springer ( English). External Links: ISBN 978-3-642-37955-0; 978-3-642-37956-7, [Document][78] Cited by: §4, §4, §4, §5, §5.
- [40] J. H. Silverman (2009) The arithmetic of elliptic curves. 2nd ed. edition, Grad. Texts Math., Vol. 106, New York, NY: Springer ( English). External Links: ISSN 0072-5285, ISBN 978-0-387-09493-9; 978-0-387-09494-6, [Document][79] Cited by: item 3, §3.1.
- [41] J. Solymosi and J. Zahl (2024) Improved Elekes-Szabó type estimates using proximity. J. Combin. Theory Ser. A 201, pp. Paper No. 105813, 9. External Links: ISSN 0097-3165,1096-0899, [Document][80], [Link][81], [MathReview (Jonathan Tidor)][82] Cited by: §1.
- [42] J. Solymosi (2009) Bounding multiplicative energy by the sumset. Adv. Math. 222 ( 2), pp. 402–408. External Links: ISSN 0001-8708,1090-2082, [Document][83], [Link][84], [MathReview (Min Tang)][85] Cited by: §1.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:joseph.s.harrison@warwick.ac.uk
[4]: mailto:Akshat.Mudgal@warwick.ac.uk
[5]: mailto:Harry.Schmidt@warwick.ac.uk
[6]: https://dx.doi.org/10.24033/asens.2467
[7]: https://doi.org/10.24033/asens.2467
[8]: https://www.ams.org/mathscinet-getitem?mr=4311096
[9]: https://eudml.org/doc/84249
[10]: https://dx.doi.org/10.1090/S0894-0347-03-00446-6
[11]: https://doi.org/10.1090/S0894-0347-03-00446-6
[12]: https://www.ams.org/mathscinet-getitem?mr=2051619
[13]: https://dx.doi.org/10.1006/jnth.1999.2430
[14]: https://dx.doi.org/10.5486/PMD.2013.5438
[15]: http://projecteuclid.org/euclid.em/1047262362
[16]: https://www.ams.org/mathscinet-getitem?mr=1737236
[17]: https://dx.doi.org/10.1016/j.crma.2009.04.006
[18]: https://doi.org/10.1016/j.crma.2009.04.006
[19]: https://www.ams.org/mathscinet-getitem?mr=2532910
[20]: https://dx.doi.org/10.1215/00127094-2023-0018
[21]: https://doi.org/10.1215/00127094-2023-0018
[22]: https://www.ams.org/mathscinet-getitem?mr=4729440
[23]: https://dx.doi.org/10.1142/S0219061321500045
[24]: https://doi.org/10.1142/S0219061321500045
[25]: https://www.ams.org/mathscinet-getitem?mr=4290493
[26]: https://www.ams.org/mathscinet-getitem?mr=2355454
[27]: https://dx.doi.org/10.1006/jcta.1999.2976
[28]: https://doi.org/10.1006/jcta.1999.2976
[29]: https://www.ams.org/mathscinet-getitem?mr=1736139
[30]: https://dx.doi.org/10.1007/s00493-012-2505-6
[31]: https://doi.org/10.1007/s00493-012-2505-6
[32]: https://www.ams.org/mathscinet-getitem?mr=3004808
[33]: https://dx.doi.org/10.4064/aa-81-4-365-367
[34]: https://doi.org/10.4064/aa-81-4-365-367
[35]: https://www.ams.org/mathscinet-getitem?mr=1472816
[36]: https://dx.doi.org/10.2140/obs.2020.4.233
[37]: https://dx.doi.org/10.2307/3062133
[38]: https://dx.doi.org/10.1007/BF01388432
[39]: https://doi.org/10.1007/BF01388432
[40]: https://www.ams.org/mathscinet-getitem?mr=718935
[41]: https://dx.doi.org/10.1093/imrn/rnaa061
[42]: https://doi.org/10.1093/imrn/rnaa061
[43]: https://www.ams.org/mathscinet-getitem?mr=4259152
[44]: https://dx.doi.org/10.4007/annals.2025.201.2.5
[45]: https://doi.org/10.4007/annals.2025.201.2.5
[46]: https://www.ams.org/mathscinet-getitem?mr=4880432
[47]: https://eudml.org/doc/103873
[48]: https://dx.doi.org/10.2140/ant.2020.14.2239
[49]: https://doi.org/10.2140/ant.2020.14.2239
[50]: https://www.ams.org/mathscinet-getitem?mr=4172707
[51]: https://www.ams.org/mathscinet-getitem?mr=4527758
[52]: https://dx.doi.org/10.1007/s00208-019-01948-8
[53]: https://doi.org/10.1007/s00208-019-01948-8
[54]: https://www.ams.org/mathscinet-getitem?mr=4211105
[55]: https://dx.doi.org/10.7169/facm/1740
[56]: https://dx.doi.org/10.1007/BF01388597
[57]: https://doi.org/10.1007/BF01388597
[58]: https://www.ams.org/mathscinet-getitem?mr=767195
[59]: https://dx.doi.org/10.1007/978-1-4419-9982-5
[60]: https://dx.doi.org/10.1007/BF01231178
[61]: https://eudml.org/doc/143776
[62]: https://dx.doi.org/10.1017/9781316711736
[63]: https://dx.doi.org/10.1093/imrn/rnae087
[64]: https://doi.org/10.1093/imrn/rnae087
[65]: https://www.ams.org/mathscinet-getitem?mr=4770374
[66]: https://dx.doi.org/10.1007/s00208-023-02762-z
[67]: https://doi.org/10.1007/s00208-023-02762-z
[68]: https://www.ams.org/mathscinet-getitem?mr=4800917
[69]: https://dx.doi.org/10.1016/j.aim.2021.108043
[70]: https://doi.org/10.1016/j.aim.2021.108043
[71]: https://www.ams.org/mathscinet-getitem?mr=4319771
[72]: https://dx.doi.org/10.1215/00127094-3674103
[73]: https://doi.org/10.1215/00127094-3674103
[74]: https://www.ams.org/mathscinet-getitem?mr=3577370
[75]: https://dx.doi.org/10.1353/ajm.2016.0033
[76]: https://doi.org/10.1353/ajm.2016.0033
[77]: https://www.ams.org/mathscinet-getitem?mr=3538150
[78]: https://dx.doi.org/10.1007/978-3-642-37956-7
[79]: https://dx.doi.org/10.1007/978-0-387-09494-6
[80]: https://dx.doi.org/10.1016/j.jcta.2023.105813
[81]: https://doi.org/10.1016/j.jcta.2023.105813
[82]: https://www.ams.org/mathscinet-getitem?mr=4638826
[83]: https://dx.doi.org/10.1016/j.aim.2009.04.006
[84]: https://doi.org/10.1016/j.aim.2009.04.006
[85]: https://www.ams.org/mathscinet-getitem?mr=2538014
