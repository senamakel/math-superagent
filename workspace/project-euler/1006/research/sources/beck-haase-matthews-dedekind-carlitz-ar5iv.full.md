<!-- source: https://ar5iv.labs.arxiv.org/html/0710.1323 | converted from HTML -->

[0710.1323] Dedekind–Carlitz Polynomials as Lattice-Point Enumerators in Rational Polyhedra

# Dedekind–Carlitz Polynomials as Lattice-Point Enumerators in Rational Polyhedra Thanks: Research of Haase supported by DFG Emmy Noether fellowship HA 4383/1. We thank Robin Chapman, Eric Mortenson, and an anonymous referee for helpful comments.

Matthias Beck Address: Department of Mathematics
San Francisco State University
San Francisco, CA 94132, USA Email address: [beck@math.sfsu.edu][1] URL: [http://math.sfsu.edu/beck][2], Christian Haase Address: Fachbereich Mathematik & Informatik
Freie Universität Berlin
14195 Berlin
Germany Email address: [christian.haase@math.fu-berlin.de][3] URL: [http://ehrhart.math.fu-berlin.de][4] and Asia R. Matthews Address: Department of Mathematics & Statistics
Queen’s University
Kingston, ON, K7L 3N6, Canada Email address: [asiamath@mast.queensu.ca][5]

Date: 8 February 2008

###### Abstract.

We study higher-dimensional analogs of the *Dedekind–Carlitz polynomials*

 | c ⁡ ( u, v, a, b):= ∑ k = 1 b − 1 u ⌊ k ​ a b ⌋ ​ v k − 1, {\rm c}\left(u,v;a,b\right):=\sum_{k=1}^{b-1}u^{\left\lfloor{\frac{ka}{b}}\right\rfloor}v^{k-1}, |  |

where u u and v v are indeterminates and a a and b b are positive integers. Carlitz proved that these polynomials satisfy the *reciprocity law*

 | ( v − 1) ​ c ​ ( u, v, a, b) + ( u − 1) ​ c ​ ( v, u, b, a) = u a − 1 ​ v b − 1 − 1, \left(v-1\right)\,{\rm c}\left(u,v;a,b\right)+\left(u-1\right)\,{\rm c}\left(v,u;b,a\right)=u^{a-1}v^{b-1}-1\,, |  |

from which one easily deduces many classical reciprocity theorems for the Dedekind sum and its generalizations. We illustrate that Dedekind–Carlitz polynomials appear naturally in generating functions of rational cones and use this fact to give geometric proofs of the Carlitz reciprocity law and various extensions of it. Our approach gives rise to new reciprocity theorems and computational complexity results for Dedekind–Carlitz polynomials, a characterization of Dedekind–Carlitz polynomials in terms of generating functions of lattice points in triangles, and a multivariate generalization of the Mordell–Pommersheim theorem on the appearance of Dedekind sums in Ehrhart polynomials of 3-dimensional lattice polytopes.

###### Key words and phrases:

Dedekind sum, Carlitz polynomial, reciprocity, lattice point, rational polyhedron, polytope, generating function, Ehrhart polynomial

###### 2000 Mathematics Subject Classification

Primary 11P21, 11L03; Secondary 05A15, 52C07.

## 1. Introduction

While studying the transformation properties of η ⁡ ( z):= e π ​ i ​ z / 12 ​ ∏ n ≥ 1 ( 1 − e 2 ​ π ​ i ​ n ​ z) \eta(z):=e^{\pi iz/12}\prod_{n\geq 1}\left(1-e^{2\pi inz}\right) under SL 2 ​ ( ℤ) \mbox{SL}_{2}(\mathbb{Z}), Richard Dedekind, in the 1880’s [9], naturally arrived at what we today call the *Dedekind sum*

 | s ⁡ ( a, b):= ∑ k = 0 b − 1 ( ( k ​ a b)) ​ ( ( k b)), {\rm s}\left(a,b\right):=\sum_{k=0}^{b-1}\left(\!\left(\frac{ka}{b}\right)\!\right)\left(\!\left(\frac{k}{b}\right)\!\right), |  |

where a a and b b are positive integers, and ( ( x)) \left(\!\left(x\right)\!\right) is the *sawtooth function*defined by

 | ( ( x)):= { { x } − 1 2 if ​ x ∉ ℤ, 0 if ​ x ∈ ℤ. \left(\!\left(x\right)\!\right):=\begin{cases}\left\{{x}\right\}-\frac{1}{2}&\text{ if }x\notin\mathbb{Z},\\ 0&\text{ if }x\in\mathbb{Z}.\end{cases} |  |

Here { x } = x − ⌊ x ⌋ \left\{{x}\right\}=x-\left\lfloor{x}\right\rfloor denotes the *fractional part*of x x. The Dedekind sum and its generalizations have since intrigued mathematicians from various areas such as analytic [1, 10] and algebraic number theory [15, 22], topology [13, 16], algebraic [6, 18] and combinatorial geometry [4, 17], and algorithmic complexity [14].

Almost a century after the appearance of Dedekind sums, Leonard Carlitz introduced the following polynomial generalization, which we will call a *Dedekind–Carlitz polynomial*:

 | c ⁡ ( u, v, a, b):= ∑ k = 1 b − 1 u ⌊ k ​ a b ⌋ ​ v k − 1. {\rm c}\left(u,v;a,b\right):=\sum_{k=1}^{b-1}u^{\left\lfloor{\frac{ka}{b}}\right\rfloor}v^{k-1}. |  |

Here u u and v v are indeterminates and a a and b b are positive integers. Undoubtedly the most important basic property for any Dedekind-like sum is *reciprocity*. For the Dedekind–Carlitz polynomials, this takes on the following form [7].

###### Theorem 1 (Carlitz).

If u u and v v are indeterminates, and a a and b b are relatively prime positive integers, then

 | ( v − 1) ​ c ​ ( u, v, a, b) + ( u − 1) ​ c ​ ( v, u, b, a) = u a − 1 ​ v b − 1 − 1. \left(v-1\right)\,{\rm c}\left(u,v;a,b\right)+\left(u-1\right)\,{\rm c}\left(v,u;b,a\right)=u^{a-1}v^{b-1}-1\,. |  |

Carlitz’s reciprocity theorem generalizes that of Dedekind [9], which states that for relatively prime positive integers a a and b b,

(1) |  | s ⁡ ( a, b) + s ⁡ ( b, a) = − 1 4 + 1 12 ​ ( a b + 1 a ​ b + b a). {\rm s}\left(a,b\right)+{\rm s}\left(b,a\right)=-\frac{1}{4}+\frac{1}{12}\left(\frac{a}{b}+\frac{1}{ab}+\frac{b}{a}\right). |  |

Dedekind reciprocity follows from Theorem 1 by applying the operators u ​ ∂ u u\,\partial{u} twice and v ​ ∂ v v\,\partial v once to Carlitz’s reciprocity identity and converting the greatest-integer functions into fractional parts.

Our motivation for this paper stems from the appearance of Dedekind sums in lattice-point enumerators for rational polyhedra. The first such instance was discovered by Mordell [17] (the case t = 1 t=1 in the following theorem) and vastly generalized by Pommersheim [18], who laid the foundation for the appearance of Dedekind-like sums in *Ehrhart polynomials*L 𝒫 ​ ( t):= #⁡ ( t ​ 𝒫 ∩ ℤ d) L_{\mathcal{P}}(t):=\#\left(t{\mathcal{P}}\cap\mathbb{Z}^{d}\right); here 𝒫 {\mathcal{P}} is a lattice d d -polytope (i.e., 𝒫 {\mathcal{P}} has integral vertices) and t t denotes a positive integer.

###### Theorem 2 (Mordell–Pommersheim).

Let 𝒯 {\mathcal{T}} be the convex hull of ( a, 0, 0) (a,0,0), ( 0, b, 0) (0,b,0), ( 0, 0, c) (0,0,c), and ( 0, 0, 0) (0,0,0), where a, b a,b and c c are pairwise relatively prime positive integers. Then the Ehrhart polynomial of 𝒯 {\mathcal{T}} is

 | L 𝒯 ​ ( t) = \displaystyle L_{\mathcal{T}}(t)= | a ​ b ​ c 6 ​ t 3 + a ​ b + a ​ c + b ​ c + 1 4 ​ t 2 \displaystyle\frac{abc}{6}\,t^{3}+\frac{ab+ac+bc+1}{4}\,t^{2} |  |

 |  | + ( 3 4 + a + b + c 4 + 1 12 ​ ( b ​ c a + c ​ a b + a ​ b c + 1 a ​ b ​ c) − s ⁡ ( b ​ c, a) − s ⁡ ( c ​ a, b) − s ⁡ ( a ​ b, c)) ​ t + 1. \displaystyle+\left(\frac{3}{4}+\frac{a+b+c}{4}+\frac{1}{12}\left(\frac{bc}{a}+\frac{ca}{b}+\frac{ab}{c}+\frac{1}{abc}\right)-{\rm s}\left(bc,a\right)-{\rm s}\left(ca,b\right)-{\rm s}\left(ab,c\right)\right)t+1\,. |  |

There are natural geometric interpretations for three of the four coefficients appearing in the Ehrhart polynomial of the Mordell–Pommersheim tetrahedron 𝒯 {\mathcal{T}}: the leading coefficient is the volume of 𝒯 {\mathcal{T}}, the second leading coefficient equals half of the sum of the areas of the faces of 𝒯 {\mathcal{T}}, and the constant term is the Euler characteristic of 𝒯 {\mathcal{T}}. (In fact, similar interpretations hold for any d d -dimensional lattice polytope [4, 11].) However, aside from toric varieties attached to 𝒯 {\mathcal{T}} [18], a geometric reason for the appearance of Dedekind sums in the linear term of the Ehrhart polynomial in Theorem 2 has so far eluded mathematicians. In this paper we attempt to shed some light on their appearance.

We begin by studying Dedekind–Carlitz sums through the generating function attached to the lattice points of a rational polyhedron 𝒫 ⊆ ℝ d {\mathcal{P}}\subseteq\mathbb{R}^{d}, namely, the *integer-point transform*

 | σ 𝒫 ​ ( 𝒛) = σ 𝒫 ​ ( z 1, z 2, … ​ z d):= ∑ 𝒎 ∈ 𝒫 ∩ ℤ d 𝒛 𝒎, \sigma_{\mathcal{P}}\left({\boldsymbol{z}}\right)=\sigma_{\mathcal{P}}\left(z_{1},z_{2},\dots z_{d}\right):=\sum_{{\boldsymbol{m}}\in{{\mathcal{P}}\cap\mathbb{Z}^{d}}}{\boldsymbol{z}}^{\boldsymbol{m}}\,, |  |

where 𝒛 𝒎 = z 1 m 1 z 2 m 2 ⋯ z d m d {\boldsymbol{z}}^{\boldsymbol{m}}=z_{1}^{m_{1}}z_{2}^{m_{2}}\cdots z_{d}^{m_{d}}. Our goals in this paper are as follows:

- •

We show that Dedekind–Carlitz polynomials appear naturally in integer-point transforms of rational cones (Section 2).

- •

We give novel *geometric*proofs of Theorem 1, some of its generalizations, and some new reciprocity theorems (Sections 3 and 5).

- •

We show that our geometric setup immediately implies that (higher-dimensional) Dedekind–Carlitz polynomials can be computed in polynomial time (Section 4).

- •

We realize the equivalence of Dedekind–Carlitz polynomials and the integer-point transform of a two-dimensional analogue of the Mordell–Pommersheim tetrahedron (Section 6).

- •

We give an intrinsic geometric reason why Dedekind sums appear in Theorem 2 by applying Brion’s decomposition theorem [6] to the Mordell–Pommersheim tetrahedron (Section 7).

While we believe that this paper constitutes the first fundamental study of Carlitz–Dedekind sum through a geometric setup, a part of this setup can implicitly be found in papers by Solomon [22] and Chapman [8] on generalized Dedekind sums, as well as in [3].

## 2. Polyhedral Cones Give Rise to Dedekind–Carlitz Polynomials

We start by decomposing the first quadrant ℝ ≥ 0 2 \mathbb{R}_{\geq 0}^{2} into two cones, namely

 | 𝒦 1 \displaystyle{\mathcal{K}}_{1} | = { λ 1 ( 0, 1) + λ 2 ( a, b): λ 1, λ 2 ≥ 0 }, \displaystyle=\left\{\lambda_{1}(0,1)+\lambda_{2}(a,b):\,\lambda_{1},\lambda_{2}\geq 0\right\}, |  |

 | 𝒦 2 \displaystyle{\mathcal{K}}_{2} | = { λ 1 ( 1, 0) + λ 2 ( a, b): λ 1 > 0, λ 2 ≥ 0 }. \displaystyle=\left\{\lambda_{1}(1,0)+\lambda_{2}(a,b):\,\lambda_{1}>0,\lambda_{2}\geq 0\right\}. |  |

Thus 𝒦 1 {\mathcal{K}}_{1} is closed, 𝒦 2 {\mathcal{K}}_{2} is half-open, and ℝ ≥ 0 2 \mathbb{R}_{\geq 0}^{2} is the disjoint union of 𝒦 1 {\mathcal{K}}_{1} and 𝒦 2 {\mathcal{K}}_{2}. Let’s compute their integer-point transforms. By a simple tiling argument (see, for example, [4, Chapter 3]),

 | σ 𝒦 1 ​ ( u, v) = σ Π 1 ​ ( u, v) ​ ( ∑ j ≥ 0 v j) ​ ( ∑ k ≥ 0 u k ​ a ​ v k ​ b) = σ Π 1 ​ ( u, v) ( 1 − v) ​ ( 1 − u a ​ v b), \sigma_{{\mathcal{K}}_{1}}(u,v)=\sigma_{\Pi_{1}}(u,v)\left(\sum_{j\geq 0}v^{j}\right)\left(\sum_{k\geq 0}u^{ka}v^{kb}\right)=\frac{\sigma_{\Pi_{1}}(u,v)}{\left(1-v\right)\left(1-u^{a}v^{b}\right)}\,, |  |

where

 | Π 1 = { λ 1 ( 0, 1) + λ 2 ( a, b): 0 ≤ λ 1, λ 2 < 1 } \Pi_{1}=\left\{\lambda_{1}(0,1)+\lambda_{2}(a,b):\,0\leq\lambda_{1},\lambda_{2}<1\right\} |  |

is the *fundamental parallelogram*of the cone 𝒦 1 {\mathcal{K}}_{1}. Analogously, we can write

 | σ 𝒦 2 ​ ( u, v) = σ Π 2 ​ ( u, v) ( 1 − u) ​ ( 1 − u a ​ v b), \sigma_{{\mathcal{K}}_{2}}(u,v)=\frac{\sigma_{\Pi_{2}}(u,v)}{\left(1-u\right)\left(1-u^{a}v^{b}\right)}\,, |  |

where

 | Π 2 = { λ 1 ( 1, 0) + λ 2 ( a, b): 0 < λ 1 ≤ 1, 0 ≤ λ 2 < 1 }. \Pi_{2}=\left\{\lambda_{1}(1,0)+\lambda_{2}(a,b):\,0<\lambda_{1}\leq 1,\,0\leq\lambda_{2}<1\right\}. |  |

Note that we need to include different sides of the half-open parallelograms Π 1 \Pi_{1} and Π 2 \Pi_{2}.

[image: Refer to caption] Figure 1. The fundamental parallelogram Π 1 \Pi_{1}.

Now we list the integer points in the half-open parallelepiped Π 1 \Pi_{1}. We may assume that a a and b b are relatively prime. Then, since Π 1 \Pi_{1} has height 1,

 | Π 1 ∩ ℤ 2 = { ( 0, 0), ( k, ⌊ k ​ b a ⌋ + 1): 1 ≤ k ≤ a − 1, k ∈ ℤ }, \Pi_{1}\cap\mathbb{Z}^{2}=\left\{(0,0),\left(k,\left\lfloor{\frac{kb}{a}}\right\rfloor+1\right):\,1\leq k\leq a-1,\,k\in\mathbb{Z}\right\}, |  |

whence

 | σ K 1 ​ ( u, v) = 1 + ∑ k = 1 a − 1 u k ​ v ⌊ k ​ b a ⌋ + 1 ( 1 − v) ​ ( 1 − u a ​ v b) = 1 + u ​ v ​ c ​ ( v, u, b, a) ( v − 1) ​ ( u a ​ v b − 1). \sigma_{K_{1}}(u,v)=\frac{1+\sum_{k=1}^{a-1}u^{k}v^{\left\lfloor{\frac{kb}{a}}\right\rfloor+1}}{(1-v)(1-u^{a}v^{b})}=\frac{1+uv\,{\rm c}\left(v,u;b,a\right)}{(v-1)\left(u^{a}v^{b}-1\right)}\,. |  |

We obtain the integer-point transform for K 2 K_{2} in the same way, carefully adjusting our sums for the half-open parallelepiped Π 2 \Pi_{2}:

 | σ K 2 ​ ( u, v) = u + ∑ k = 1 b − 1 v k ​ u ⌊ k ​ a b ⌋ + 1 ( 1 − u) ​ ( 1 − u a ​ v b) = u + u ​ v ​ c ​ ( u, v, a, b) ( u − 1) ​ ( u a ​ v b − 1). \sigma_{K_{2}}(u,v)=\frac{u+\sum_{k=1}^{b-1}v^{k}u^{\left\lfloor{\frac{ka}{b}}\right\rfloor+1}}{(1-u)(1-u^{a}v^{b})}=\frac{u+uv\,{\rm c}\left(u,v;a,b\right)}{(u-1)\left(u^{a}v^{b}-1\right)}\,. |  |

## 3. Carlitz Reciprocity

The reciprocity theorem for Dedekind–Carlitz sums now follows almost instantly from our geometric setup.

###### Proof of Theorem 1.

We have constructed two cones 𝒦 1 {\mathcal{K}}_{1} and 𝒦 2 {\mathcal{K}}_{2} such that ℝ ≥ 0 2 = 𝒦 1 ⊔ 𝒦 2 \mathbb{R}_{\geq 0}^{2}={\mathcal{K}}_{1}\sqcup{\mathcal{K}}_{2} as a disjoint union. In the language of integer-point transforms, this means

(2) |  | σ ℝ ≥ 0 2 ​ ( u, v) = σ 𝒦 1 ​ ( u, v) + σ 𝒦 2 ​ ( u, v). \sigma_{\mathbb{R}_{\geq 0}^{2}}(u,v)=\sigma_{{\mathcal{K}}_{1}}(u,v)+\sigma_{{\mathcal{K}}_{2}}(u,v)\,. |  |

We just computed the rational generating functions on the right-hand side, and the integer-point transform for the first quadrant is simple: σ ℝ ≥ 0 2 ​ ( u, v) = 1 ( 1 − u) ​ ( 1 − v) \sigma_{\mathbb{R}_{\geq 0}^{2}}(u,v)=\frac{1}{(1-u)(1-v)}. Thus ( 2) becomes

 | 1 ( u − 1) ​ ( v − 1) = 1 + u ​ v ​ c ​ ( v, u, b, a) ( v − 1) ​ ( u a ​ v b − 1) + u + u ​ v ​ c ​ ( u, v, a, b) ( u − 1) ​ ( u a ​ v b − 1), \frac{1}{(u-1)(v-1)}=\frac{1+uv\,{\rm c}\left(v,u;b,a\right)}{(v-1)\left(u^{a}v^{b}-1\right)}+\frac{u+uv\,{\rm c}\left(u,v;a,b\right)}{(u-1)\left(u^{a}v^{b}-1\right)}\,, |  |

which yields the identity of Theorem 1 after clearing denominators. ∎

Our new, geometric proof of Carlitz’s reciprocity theorem has a natural generalization to higher dimensions, which yields the reciprocity identity for the *higher-dimensional Dedekind–Carlitz polynomials*

 | c ( u 1, u 2, …, u n; a 1, a 2, …, a n):= ∑ k = 1 a n − 1 u 1 ⌊ k ​ a 1 a n ⌋ u 2 ⌊ k ​ a 2 a n ⌋ ⋯ u n − 1 ⌊ k ​ a n − 1 a n ⌋ u n k − 1, {\rm c}\left(u_{1},u_{2},\dots,u_{n};a_{1},a_{2},\dots,a_{n}\right):=\sum_{k=1}^{a_{n}-1}u_{1}^{\left\lfloor{\frac{ka_{1}}{a_{n}}}\right\rfloor}u_{2}^{\left\lfloor{\frac{ka_{2}}{a_{n}}}\right\rfloor}\cdots u_{n-1}^{\left\lfloor{\frac{ka_{n-1}}{a_{n}}}\right\rfloor}u_{n}^{k-1}, |  |

where u 1, u 2, …, u n u_{1},u_{2},\dots,u_{n} are indeterminates and a 1, a 2, …, a n a_{1},a_{2},\dots,a_{n} are positive integers. The reciprocity theorem for these polynomials is due to Berndt and Dieter [5], and we give a novel proof using essentially the same geometric picture as in our previous proof.

###### Theorem 3 (Berndt–Dieter).

If a 1, a 2, …, a n a_{1},a_{2},\dots,a_{n} are pairwise relatively prime positive integers, then

 |  | ( u n − 1) ​ c ​ ( u 1, u 2, …, u n, a 1, a 2, …, a n) \displaystyle\left(u_{n}-1\right){\rm c}\left(u_{1},u_{2},\dots,u_{n};a_{1},a_{2},\dots,a_{n}\right) |  |

 |  | + ( u n − 1 − 1) ​ c ​ ( u n, u 1, …, u n − 2, u n − 1, a n, a 1, …, a n − 2, a n − 1) \displaystyle\qquad+\left(u_{n-1}-1\right){\rm c}\left(u_{n},u_{1},\dots,u_{n-2},u_{n-1};a_{n},a_{1},\dots,a_{n-2},a_{n-1}\right) |  |

 |  | + ⋯ + ( u 1 − 1) c ( u 2, u 3, …, u n, u 1; a 2, a 3, …, a n, a 1) \displaystyle\qquad+\cdots+\left(u_{1}-1\right){\rm c}\left(u_{2},u_{3},\dots,u_{n},u_{1};a_{2},a_{3},\dots,a_{n},a_{1}\right) |  |

 |  | = u 1 a 1 − 1 u 2 a 2 − 1 ⋯ u n a n − 1 − 1. \displaystyle\qquad=u_{1}^{a_{1}-1}u_{2}^{a_{2}-1}\cdots u_{n}^{a_{n}-1}-1\,. |  |

###### Proof.

Analogous to our proof of Theorem 1, we construct a single ray in n n -dimensional space, and then we decompose the non-negative orthant into n n cones as follows. Let 𝒂:= ( a 1, a 2, …, a n) ∈ ℝ n {\boldsymbol{a}}:=(a_{1},a_{2},\dots,a_{n})\in\mathbb{R}^{n}, denote the j th j^{\text{th}} unit vector by 𝒆 j {\boldsymbol{e}}_{j}, and define

 | 𝒦 1 \displaystyle{\mathcal{K}}_{1} | = { λ 2 𝒆 2 + λ 3 𝒆 3 + ⋯ + λ n 𝒆 n + λ 𝒂: λ 2, …, λ n, λ ≥ 0 }, \displaystyle=\left\{\lambda_{2}{{\boldsymbol{e}}}_{2}+\lambda_{3}{{\boldsymbol{e}}}_{3}+\cdots+\lambda_{n}{{\boldsymbol{e}}}_{n}+\lambda{\boldsymbol{a}}:\,\lambda_{2},\dots,\lambda_{n},\lambda\geq 0\right\}, |  |

 | 𝒦 2 \displaystyle{\mathcal{K}}_{2} | = { λ 1 𝒆 1 + λ 3 𝒆 3 + ⋯ + λ n 𝒆 n + λ 𝒂: λ 1 > 0, λ 3, …, λ n, λ ≥ 0 }, \displaystyle=\left\{\lambda_{1}{{\boldsymbol{e}}}_{1}+\lambda_{3}{{\boldsymbol{e}}}_{3}+\cdots+\lambda_{n}{{\boldsymbol{e}}}_{n}+\lambda{\boldsymbol{a}}:\,\lambda_{1}>0,\,\lambda_{3},\dots,\lambda_{n},\lambda\geq 0\right\}, |  |

 |  |  |

 | 𝒦 j \displaystyle{\mathcal{K}}_{j} | = { λ 1 ​ 𝒆 1 + ⋯ + λ j − 1 ​ 𝒆 j − 1 + λ j + 1 ​ 𝒆 j + 1 + ⋯ + λ n ​ 𝒆 n + λ ​ 𝒂: λ 1, …, λ j − 1 > 0, λ j + 1, …, λ n, λ ≥ 0 }, \displaystyle=\left\{\begin{array}[]{l}\lambda_{1}{{\boldsymbol{e}}}_{1}+\cdots+\lambda_{j-1}{{\boldsymbol{e}}}_{j-1}+\lambda_{j+1}{{\boldsymbol{e}}}_{j+1}+\cdots+\lambda_{n}{{\boldsymbol{e}}}_{n}+\lambda{\boldsymbol{a}}:\\ \lambda_{1},\dots,\lambda_{j-1}>0,\,\lambda_{j+1},\dots,\lambda_{n},\lambda\geq 0\end{array}\right\}, |  |

 |  |  |

 | 𝒦 n \displaystyle{\mathcal{K}}_{n} | = { λ 1 𝒆 1 + λ 2 𝒆 2 + ⋯ + λ n − 1 𝒆 n − 1 + λ 𝒂: λ 1, …, λ n − 1 > 0, λ ≥ 0 }. \displaystyle=\left\{\lambda_{1}{{\boldsymbol{e}}}_{1}+\lambda_{2}{{\boldsymbol{e}}}_{2}+\cdots+\lambda_{n-1}{{\boldsymbol{e}}}_{n-1}+\lambda{\boldsymbol{a}}:\,\lambda_{1},\dots,\lambda_{n-1}>0,\,\lambda\geq 0\right\}. |  |

The fundamental parallelepiped of 𝒦 j {\mathcal{K}}_{j} is

 | Π j = { λ 1 ​ 𝒆 1 + ⋯ + λ j − 1 ​ 𝒆 j − 1 + λ j + 1 ​ 𝒆 j + 1 + ⋯ + λ n ​ 𝒆 n + λ ​ 𝒂: 0 < λ 1, …, λ j − 1 ≤ 1, 0 ≤ λ j + 1, …, λ n, λ < 1 }. \Pi_{j}=\left\{\begin{array}[]{l}\lambda_{1}{{\boldsymbol{e}}}_{1}+\cdots+\lambda_{j-1}{{\boldsymbol{e}}}_{j-1}+\lambda_{j+1}{{\boldsymbol{e}}}_{j+1}+\cdots+\lambda_{n}{{\boldsymbol{e}}}_{n}+\lambda{\boldsymbol{a}}:\\ 0<\lambda_{1},\dots,\lambda_{j-1}\leq 1,\,0\leq\lambda_{j+1},\dots,\lambda_{n},\lambda<1\end{array}\right\}. |  |

Thus a point in Π j \Pi_{j} will look like

 | ( λ 1 + λ ​ a 1, …, λ j − 1 + λ ​ a j − 1, λ ​ a j, λ j + 1 + λ ​ a j + 1, …, λ n + λ ​ a n), \left(\lambda_{1}+\lambda a_{1},\dots,\lambda_{j-1}+\lambda a_{j-1},\lambda a_{j},\lambda_{j+1}+\lambda a_{j+1},\dots,\lambda_{n}+\lambda a_{n}\right), |  |

and a slice of this parallelepiped at x j = k x_{j}=k (where 1 ≤ k ≤ a j − 1 1\leq k\leq a_{j}-1) will contain

 | ( ⌊ k ​ a 1 a j ⌋ + 1, …, ⌊ k ​ a j − 1 a j ⌋ + 1, k, ⌊ k ​ a j + 1 a j ⌋ + 1, …, ⌊ k ​ a n a j ⌋ + 1) \left(\left\lfloor{\frac{ka_{1}}{a_{j}}}\right\rfloor+1,\dots,\left\lfloor{\frac{ka_{j-1}}{a_{j}}}\right\rfloor+1,k,\left\lfloor{\frac{ka_{j+1}}{a_{j}}}\right\rfloor+1,\dots,\left\lfloor{\frac{ka_{n}}{a_{j}}}\right\rfloor+1\right) |  |

as the only integer point. Note also that the integer point 𝒆 1 + ⋯ + 𝒆 j − 1 {\boldsymbol{e}}_{1}+\dots+{\boldsymbol{e}}_{j-1} is in Π j \Pi_{j}. Combining this information as in Section 2 yields the integer-point transform

 |  | σ 𝒦 j ​ ( 𝒖) = σ Π j ​ ( 𝒖) ( 1 − 𝒖 𝒂) ( 1 − u 1) ⋯ ( 1 − u j − 1) ( 1 − u j + 1) ⋯ ( 1 − u n) \displaystyle\sigma_{{\mathcal{K}}_{j}}({\boldsymbol{u}})=\frac{\sigma_{\Pi_{j}}({\boldsymbol{u}})}{\left(1-{\boldsymbol{u}}^{\boldsymbol{a}}\right)\left(1-u_{1}\right)\cdots\left(1-u_{j-1}\right)\left(1-u_{j+1}\right)\cdots\left(1-u_{n}\right)} |  |

 |  | = u 1 u 2 ⋯ u j − 1 + ∑ k = 1 a j − 1 u 1 ⌊ k ​ a 1 a j ⌋ + 1 ⋯ u j − 1 ⌊ k ​ a j − 1 a j ⌋ + 1 u j k u j + 1 ⌊ k ​ a j + 1 a j ⌋ + 1 ⋯ u n ⌊ k ​ a n a j ⌋ + 1 ( 1 − 𝒖 𝒂) ( 1 − u 1) ⋯ ( 1 − u j − 1) ( 1 − u j + 1) ⋯ ( 1 − u n) \displaystyle\qquad=\frac{u_{1}u_{2}\cdots u_{j-1}+\sum_{k=1}^{a_{j}-1}u_{1}^{\left\lfloor{\frac{ka_{1}}{a_{j}}}\right\rfloor+1}\cdots u_{j-1}^{\left\lfloor{\frac{ka_{j-1}}{a_{j}}}\right\rfloor+1}u_{j}^{k}u_{j+1}^{\left\lfloor{\frac{ka_{j+1}}{a_{j}}}\right\rfloor+1}\cdots u_{n}^{\left\lfloor{\frac{ka_{n}}{a_{j}}}\right\rfloor+1}}{\left(1-{\boldsymbol{u}}^{\boldsymbol{a}}\right)\left(1-u_{1}\right)\cdots\left(1-u_{j-1}\right)\left(1-u_{j+1}\right)\cdots\left(1-u_{n}\right)} |  |

 |  | = u 1 u 2 ⋯ u j − 1 + u 1 u 2 ⋯ u n c ( u 1, …, u j − 1, u j + 1, …, u n, u j; a 1, …, a j − 1, a j + 1, …, a n, a j) ( 1 − 𝒖 𝒂) ( 1 − u 1) ⋯ ( 1 − u j − 1) ( 1 − u j + 1) ⋯ ( 1 − u n), \displaystyle\qquad=\frac{u_{1}u_{2}\cdots u_{j-1}+u_{1}u_{2}\cdots u_{n}\,{\rm c}\left(u_{1},\dots,u_{j-1},u_{j+1},\dots,u_{n},u_{j};a_{1},\dots,a_{j-1},a_{j+1},\dots,a_{n},a_{j}\right)}{\left(1-{\boldsymbol{u}}^{\boldsymbol{a}}\right)\left(1-u_{1}\right)\cdots\left(1-u_{j-1}\right)\left(1-u_{j+1}\right)\cdots\left(1-u_{n}\right)}\,, |  |

where 𝒖:= ( u 1, u 2, ⋯, u n) {\boldsymbol{u}}:=\left(u_{1},u_{2},\cdots,u_{n}\right) and 𝒖 𝒂:= u 1 a 1 u 2 a 2 ⋯ u n a n {\boldsymbol{u}}^{{\boldsymbol{a}}}:=u_{1}^{a_{1}}u_{2}^{a_{2}}\cdots u_{n}^{a_{n}}. Since ⋃ j = 1 n 𝒦 j = ℝ ≥ 0 n \bigcup_{j=1}^{n}{\mathcal{K}}_{j}=\mathbb{R}_{\geq 0}^{n} is a disjoint union of the nonnegative n n -dimensional orthant,

 | σ 𝒦 1 ​ ( 𝒖) + σ 𝒦 2 ​ ( 𝒖) + ⋯ + σ 𝒦 n ​ ( 𝒖) = σ ℝ ≥ 0 n ​ ( 𝒖) = 1 ( 1 − u 1) ⋯ ( 1 − u n). \sigma_{{\mathcal{K}}_{1}}({\boldsymbol{u}})+\sigma_{{\mathcal{K}}_{2}}({\boldsymbol{u}})+\cdots+\sigma_{{\mathcal{K}}_{n}}({\boldsymbol{u}})=\sigma_{\mathbb{R}_{\geq 0}^{n}}({\boldsymbol{u}})=\frac{1}{\left(1-u_{1}\right)\cdots\left(1-u_{n}\right)}\,. |  |

Theorem 3 follows upon clearing denominators in this identity. ∎

To virtually every theorem in this paper, there exist translate companions, i.e., we can shift the cones involved in our proofs by a fixed vector. This gives rise to shifts in the greatest-integer functions, and the resulting Carlitz sums are polynomial analogues of *Dedekind–Rademacher sums*[21]. For the sake of clarity of exposition, we only give integer-vertex versions of our cones, but the reader should keep in mind that arbitrary vertices do, in principal, not cause any additional problems.

## 4. Computational Complexity

Dedekind’s reciprocity law ( 1) together with the identity s ⁡ ( a, b) = s ⁡ ( c, b) {\rm s}(a,b)={\rm s}(c,b), if a ≡ c mod b a\equiv c\bmod b, allows us to compute the classical Dedekind sum in a Euclidean-algorithm style and thus very efficiently, namely in linear time. (Computational complexity is measured in terms of the input length, e.g., in this case log ⁡ a + log ⁡ b \log a+\log b.) We do not know how to apply a similar reasoning to the Dedekind–Carlitz polynomials via Carlitz’s reciprocity law Theorem 1; however, the following central theorem of Barvinok [2] allows us to deduce that (higher-dimensional) Dedekind–Carlitz polynomials can be computed efficiently.

###### Theorem 4 (Barvinok).

In fixed dimension, the integer-point transform σ 𝒫 ​ ( z 1, z 2, …, z d) \sigma_{\mathcal{P}}\left(z_{1},z_{2},\dots,z_{d}\right) of a rational polyhedron 𝒫 {\mathcal{P}} can be computed as a sum of rational functions in z 1, z 2, …, z d z_{1},z_{2},\dots,z_{d} in time polynomial in the input size of 𝒫 {\mathcal{P}}.

Note that Barvinok’s theorem says, in particular, that the rational functions whose sum represents σ 𝒫 ​ ( 𝒛) \sigma_{\mathcal{P}}({\boldsymbol{z}}) are *short*, i.e., the set of data needed to output this sum of rational functions is of size that is polynomial in the input size of 𝒫 {\mathcal{P}}. The application of Barvinok’s theorem to any of the cones appearing in the proof of Theorem 3 immediately yields the following novel complexity result.

###### Theorem 5.

For fixed n n, the higher-dimensional Dedekind–Carlitz polynomial
c ⁡ ( u 1, u 2, …, u n, a 1, a 2, …, a n) {\rm c}\left(u_{1},u_{2},\dots,u_{n};a_{1},a_{2},\dots,a_{n}\right) can be computed in time polynomial in the size of a 1, a 2, …, a n a_{1},a_{2},\dots,a_{n}.

In particular, this result says that there is a more economical way to write the “long” polynomial c ⁡ ( u 1, u 2, …, u n, a 1, a 2, …, a n) {\rm c}\left(u_{1},u_{2},\dots,u_{n};a_{1},a_{2},\dots,a_{n}\right) as a short sum of rational functions. Theorem 5 implies that any Dedekind-like sum that can be efficiently derived from Dedekind–Carlitz polynomials (e.g., by applying differential operators) can also be computed efficiently.

## 5. Variations on a Theme

The geometry we have used so far is very simple: it is based on one ray in space. Naturally, this can be extended in numerous ways. To illustrate one of them, consider two rays through the points ( a, b) (a,b) and ( c, d) (c,d) in the first quadrant of the plane, where a, b, c, d a,b,c,d are positive integers. This construction decomposes the first quadrant into three rational cones as shown in Figure .

[image: Refer to caption] Figure 2. Two-ray decomposition of the first quadrant.

The integer-point transform of each of the two exterior cones, 𝒦 1 {\mathcal{K}}_{1} and 𝒦 3 {\mathcal{K}}_{3}, is easily computed in the same manner as in Section 2. However, the cone in the middle, 𝒦 2 {\mathcal{K}}_{2}, is bounded on either side by a non-unit vector, and therefore the interior points of the fundamental parallelogram of this cone are not trivial to list. We will use unimodular transformations to compute σ 𝒦 2 \sigma_{{\mathcal{K}}_{2}}. This construction leads to a new reciprocity identity (Theorem 7 below). We start by computing the integer-point transform for a general rational cone in ℝ 2 \mathbb{R}^{2}, i.e., 𝒦 2 {\mathcal{K}}_{2} in Figure .

###### Lemma 6.

Suppose a, b, c, d a,b,c,d are positive integers such that a ​ d > b ​ c ad>bc and gcd ⁡ ( a, b) = gcd ⁡ ( c, d) = 1 \gcd(a,b)=\gcd(c,d)=1, and let x, y ∈ ℤ x,y\in\mathbb{Z} such that a ​ x + b ​ y = 1 ax+by=1. Then the cone 𝒦:= { λ ( a, b) + μ ( c, d): λ, μ ≥ 0 } {\mathcal{K}}:=\left\{\lambda(a,b)+\mu(c,d):\,\lambda,\mu\geq 0\right\} has the integer-point transform

 | σ 𝒦 ​ ( u, v) = 1 + u a − y ​ v b + x ​ c ​ ( u a ​ v b, u − y ​ v x, c ​ x + d ​ y, a ​ d − b ​ c) ( u a ​ v b − 1) ​ ( u c ​ v d − 1). \sigma_{{\mathcal{K}}}(u,v)=\frac{1+u^{a-y}v^{b+x}\,{\rm c}\left(u^{a}v^{b},u^{-y}v^{x};cx+dy,ad-bc\right)}{\left(u^{a}v^{b}-1\right)\left(u^{c}v^{d}-1\right)}\,. |  |

###### Proof.

To compute the generating function σ 𝒦 \sigma_{{\mathcal{K}}}, note that the linear transformation given by

 | M:= ( x y − b a) M:=\left(\begin{array}[]{cc}x&y\\ -b&a\end{array}\right) |  |

maps 𝒦 {\mathcal{K}} to the cone M ⁡ ( 𝒦) M({\mathcal{K}}) generated by ( 1, 0) (1,0) and ( c ​ x + d ​ y, a ​ d − b ​ c) (cx+dy,ad-bc), whose integer-point transform we know how to compute from Section 2. Since

 | M − 1 = ( a − y b x) M^{-1}=\left(\begin{array}[]{cc}a&-y\\ b&x\end{array}\right) |  |

we obtain

 | σ 𝒦 ​ ( u, v) \displaystyle\sigma_{{\mathcal{K}}}(u,v) | = ∑ ( m, n) ∈ 𝒦 ∩ ℤ 2 u m ​ v n = ∑ ( m, n) ∈ M ⁡ ( 𝒦) ∩ ℤ 2 u a ​ m − y ​ n ​ v b ​ m + x ​ n = ∑ ( m, n) ∈ M ⁡ ( 𝒦) ∩ ℤ 2 ( u a ​ v b) m ​ ( u − y ​ v x) n \displaystyle=\sum_{(m,n)\in{\mathcal{K}}\cap\mathbb{Z}^{2}}u^{m}v^{n}=\sum_{(m,n)\in M({\mathcal{K}})\cap\mathbb{Z}^{2}}u^{am-yn}v^{bm+xn}=\sum_{(m,n)\in M({\mathcal{K}})\cap\mathbb{Z}^{2}}\left(u^{a}v^{b}\right)^{m}\left(u^{-y}v^{x}\right)^{n} |  |

 |  | = 1 + u a − y ​ v b + x ​ c ​ ( u a ​ v b, u − y ​ v x, c ​ x + d ​ y, a ​ d − b ​ c) ( u a ​ v b − 1) ​ ( u c ​ v d − 1). ∎ \displaystyle=\frac{1+u^{a-y}v^{b+x}{\rm c}\left(u^{a}v^{b},u^{-y}v^{x};cx+dy,ad-bc\right)}{\left(u^{a}v^{b}-1\right)\left(u^{c}v^{d}-1\right)}\,.\qed |  |

###### Theorem 7.

Suppose a, b, c, d a,b,c,d are positive integers such that a ​ d > b ​ c ad>bc and gcd ⁡ ( a, b) = gcd ⁡ ( c, d) = 1 \gcd(a,b)=\gcd(c,d)=1, and let x, y ∈ ℤ x,y\in\mathbb{Z} such that a ​ x + b ​ y = 1 ax+by=1. Then

 |  | u ​ v ​ ( u − 1) ​ ( u a ​ v b − 1) ​ c ​ ( v, u, d, c) + u ​ v ​ ( v − 1) ​ ( u c ​ v d − 1) ​ c ​ ( u, v, a, b) \displaystyle uv(u-1)\left(u^{a}v^{b}-1\right){\rm c}\left(v,u;d,c\right)+uv(v-1)\left(u^{c}v^{d}-1\right){\rm c}\left(u,v;a,b\right) |  |

 |  | + u a − y ​ v b + x ​ ( u − 1) ​ ( v − 1) ​ c ​ ( u a ​ v b, u − y ​ v x, c ​ x + d ​ y, a ​ d − b ​ c) \displaystyle\qquad+u^{a-y}v^{b+x}\left(u-1\right)\left(v-1\right){\rm c}\left(u^{a}v^{b},u^{-y}v^{x};cx+dy,ad-bc\right) |  |

 |  | = u a + c ​ v b + d − u a ​ v b ​ ( u ​ v − v + 1) − u c ​ v d ​ ( u ​ v − u + 1) + u ​ v. \displaystyle\qquad=u^{a+c}v^{b+d}-u^{a}v^{b}(uv-v+1)-u^{c}v^{d}(uv-u+1)+uv\,. |  |

###### Proof.

Again, we prove the theorem geometrically. Let

 |  | 𝒦 1 = { λ 2 𝒆 2 + λ c ​ d ( c, d): λ 2 > 0, λ c ​ d ≥ 0 }, \displaystyle{\mathcal{K}}_{1}=\left\{\lambda_{2}{{\boldsymbol{e}}}_{2}+\lambda_{cd}(c,d):\,\lambda_{2}>0,\,\lambda_{cd}\geq 0\right\}, |  |

 |  | 𝒦 2 = { λ a ​ b ( a, b) + λ c ​ d ( c, d): λ a ​ b, λ c ​ d ≥ 0 }, \displaystyle{\mathcal{K}}_{2}=\left\{\lambda_{ab}(a,b)+\lambda_{cd}(c,d):\,\lambda_{ab},\lambda_{cd}\geq 0\right\}, |  |

 |  | 𝒦 3 = { λ 1 𝒆 1 + λ a ​ b ( a, b): λ 1 > 0, λ a ​ b ≥ 0 }, \displaystyle{\mathcal{K}}_{3}=\left\{\lambda_{1}{{\boldsymbol{e}}}_{1}+\lambda_{ab}(a,b):\,\lambda_{1}>0,\,\lambda_{ab}\geq 0\right\}, |  |

so that 𝒦 2 {\mathcal{K}}_{2} is closed and 𝒦 1 {\mathcal{K}}_{1} and 𝒦 3 {\mathcal{K}}_{3} are half-open, and 𝒦 1 ⊔ 𝒦 2 ⊔ 𝒦 3 = ℝ ≥ 0 2 {\mathcal{K}}_{1}\sqcup{\mathcal{K}}_{2}\sqcup{\mathcal{K}}_{3}=\mathbb{R}_{\geq 0}^{2} is a disjoint union of the first quadrant. With the methods introduced in Section 2, the integer-point transforms of 𝒦 1 {\mathcal{K}}_{1} and 𝒦 3 {\mathcal{K}}_{3} are

 |  | σ 𝒦 1 ​ ( u, v) = v + ∑ k = 1 c − 1 u k ​ v ⌊ k ​ d c ⌋ + 1 ( 1 − v) ​ ( 1 − u c ​ v d) = v + u ​ v ​ c ​ ( v, u, d, c) ( v − 1) ​ ( u c ​ v d − 1), \displaystyle\sigma_{{\mathcal{K}}_{1}}(u,v)=\frac{v+\sum_{k=1}^{c-1}u^{k}v^{\left\lfloor{\frac{kd}{c}}\right\rfloor+1}}{(1-v)\left(1-u^{c}v^{d}\right)}=\frac{v+uv\,{\rm c}\left(v,u;d,c\right)}{(v-1)\left(u^{c}v^{d}-1\right)}\,, |  |

 |  | σ 𝒦 3 ​ ( u, v) = u + ∑ k = 1 b − 1 v k ​ u ⌊ k ​ a b ⌋ + 1 ( 1 − u) ​ ( 1 − u a ​ v b) = u + u ​ v ​ c ​ ( u, v, a, b) ( u − 1) ​ ( u a ​ v b − 1), \displaystyle\sigma_{{\mathcal{K}}_{3}}(u,v)=\frac{u+\sum_{k=1}^{b-1}v^{k}u^{\left\lfloor{\frac{ka}{b}}\right\rfloor+1}}{(1-u)\left(1-u^{a}v^{b}\right)}=\frac{u+uv\,{\rm c}\left(u,v;a,b\right)}{(u-1)\left(u^{a}v^{b}-1\right)}\,, |  |

and the integer-point transform of 𝒦 2 {\mathcal{K}}_{2} was computed in Lemma 6. By our construction,

 | σ 𝒦 1 ​ ( u, v) + σ 𝒦 2 ​ ( u, v) + σ 𝒦 3 ​ ( u, v) = σ ℝ ≥ 0 2 ​ ( u, v) = 1 ( 1 − u) ​ ( 1 − v), \sigma_{{\mathcal{K}}_{1}}(u,v)+\sigma_{{\mathcal{K}}_{2}}(u,v)+\sigma_{{\mathcal{K}}_{3}}(u,v)=\sigma_{\mathbb{R}_{\geq 0}^{2}}(u,v)=\frac{1}{(1-u)(1-v)}\,, |  |

from which Theorem 7 follows upon clearing denominators. ∎

Theorem 7 is the polynomial analogue of the following result due to Pommersheim [18, Theorem 7]:

###### Theorem 8 (Pommersheim).

Suppose a, b, c, d a,b,c,d are positive integers such that gcd ⁡ ( a, b) = gcd ⁡ ( c, d) = 1 \gcd(a,b)=\gcd(c,d)=1, and let x, y ∈ ℤ x,y\in\mathbb{Z} such that a ​ x + b ​ y = 1 ax+by=1. Then

 | s ⁡ ( a, b) + s ⁡ ( c, d) = s ⁡ ( c ​ x − d ​ y, a ​ d + b ​ c) − 1 4 + 1 12 ​ ( b d ⁡ ( a ​ d + b ​ c) + d b ⁡ ( a ​ d + b ​ c) + a ​ d + b ​ c b ​ d). \displaystyle{\rm s}(a,b)+{\rm s}(c,d)={\rm s}(cx-dy,ad+bc)-\frac{1}{4}+\frac{1}{12}\left(\frac{b}{d(ad+bc)}+\frac{d}{b(ad+bc)}+\frac{ad+bc}{bd}\right). |  |

This, in turn, generalizes Rademacher’s three-term reciprocity theorem [19]:

###### Corollary 9 (Rademacher).

If a, b, c a,b,c are pairwise coprime positive integers then

 | s ⁡ ( a ​ b − 1, c) + s ⁡ ( c ​ a − 1, b) + s ⁡ ( b ​ c − 1, a) = − 1 4 + 1 12 ​ ( a b ​ c + b c ​ a + c a ​ b), {\rm s}\left(ab^{-1},c\right)+{\rm s}\left(ca^{-1},b\right)+{\rm s}\left(bc^{-1},a\right)=-\frac{1}{4}+\frac{1}{12}\left(\frac{a}{bc}+\frac{b}{ca}+\frac{c}{ab}\right), |  |

where a − 1 ​ a ≡ 1 mod b a^{-1}a\equiv 1\bmod b, b − 1 ​ b ≡ 1 mod c b^{-1}b\equiv 1\bmod c, and c − 1 ​ c ≡ 1 mod a c^{-1}c\equiv 1\bmod a.

The case n = 3 n=3 of Berndt–Dieter’s Theorem 3 is the polynomial analogue of this three-term law. Clearly, Dedekind’s reciprocity theorem ( 1) is implied by Corollary 9, and Girstmair showed [12] that ( 1) implies Theorem 8, so that, in fact, Dedekind’s, Rademacher’s, and Pommersheim’s reciprocity theorems are equivalent. Such an equivalence can clearly not hold on the polynomial level, but one could ask whether Theorems 1 and 7 are equivalent.

Theorem 7 could be generalized in several ways, e.g., to higher dimensions or to more than three cones in dimension 2 (this yields a Carlitz polynomial analogue of [18, Theorem 8]), but we digress.

Theorem 7 simplifies when a ​ d − b ​ c = 1 ad-bc=1: then the third Dedekind–Carlitz polynomial disappears. Geometrically, this stems from the fact that the cone 𝒦 2 {\mathcal{K}}_{2} is *unimodular*, i.e., its fundamental parallelogram contains only the origin.

###### Corollary 10.

If a, b, c, d a,b,c,d are positive integers such that a ​ d − b ​ c = 1 ad-bc=1, then

 |  | ( u − 1) ​ ( u a ​ v b − 1) ​ c ​ ( v, u, d, c) + ( v − 1) ​ ( u c ​ v d − 1) ​ c ​ ( u, v, a, b) \displaystyle(u-1)\left(u^{a}v^{b}-1\right){\rm c}\left(v,u;d,c\right)+(v-1)\left(u^{c}v^{d}-1\right){\rm c}\left(u,v;a,b\right) |  |

 |  | = u a + c − 1 ​ v b + d − 1 − u a ​ v b − u c ​ v d + u a − 1 ​ v b + u c ​ v d − 1 − u a − 1 ​ v b − 1 − u c − 1 ​ v d − 1 + 1. \displaystyle\qquad=u^{a+c-1}v^{b+d-1}-u^{a}v^{b}-u^{c}v^{d}+u^{a-1}v^{b}+u^{c}v^{d-1}-u^{a-1}v^{b-1}-u^{c-1}v^{d-1}+1\,. |  |

This is the polynomial analogue of the following result due to Rademacher [20].

###### Corollary 11 (Rademacher).

If a, b, c, d a,b,c,d are positive integers such that a ​ d − b ​ c = 1 ad-bc=1, then

 | s ⁡ ( a, b) + s ⁡ ( d, c) = − 1 2 + 1 12 ​ ( a b + a c + d b + d c). {\rm s}(a,b)+{\rm s}(d,c)=-\frac{1}{2}+\frac{1}{12}\left(\frac{a}{b}+\frac{a}{c}+\frac{d}{b}+\frac{d}{c}\right). |  |

## 6. Dedekind–Carlitz Polynomials as Integer-Point Transforms of Triangles

We have shown that Dedekind–Carlitz polynomials appear as natural ingredients of integer-point transforms of cones. In this light, it should come as no surprise that the following conic decomposition theorem of Brion [6] will prove useful. We remind the reader that a *rational polytope*is the convex hull of finitely many rational points in ℝ d \mathbb{R}^{d}. If 𝒗 {\boldsymbol{v}} is a vertex of the polytope 𝒫 {\mathcal{P}}, then the *vertex cone*𝒦 𝒗 {\mathcal{K}}_{\boldsymbol{v}} is the smallest cone with apex 𝒗 {\boldsymbol{v}} that contains 𝒫 {\mathcal{P}}.

###### Theorem 12 (Brion).

Suppose 𝒫 {\mathcal{P}} is a rational convex polytope. Then we have the following identity of rational functions:

 | σ 𝒫 ​ ( 𝒛) = ∑ 𝒗 σ 𝒦 𝒗 ​ ( 𝒛), \sigma_{\mathcal{P}}({\boldsymbol{z}})=\sum_{{\boldsymbol{v}}}\sigma_{{\mathcal{K}}_{\boldsymbol{v}}}({\boldsymbol{z}})\,, |  |

where the sum is over all vertices of P P.

Brion’s theorem allows us to give a novel expression for the Dedekind–Carlitz polynomial as the integer-point transform of a certain triangle.

###### Theorem 13.

Let a a and b b be relatively prime positive integers and u u and v v be indeterminates. If Δ \Delta is the triangle with vertices ( 0, 0) (0,0), ( a, 0) (a,0), and ( 0, b) (0,b), then the Dedekind–Carlitz polynomial c ⁡ ( 1 u, v, a, b) {\rm c}\left(\frac{1}{u},v;a,b\right) and the integer-point transform of Δ \Delta are related in the following manner:

 | ( u − 1) ​ σ Δ ​ ( u, v) = u a ​ v ​ c ​ ( 1 u, v, a, b) + u ⁡ ( u a + v b) − v b + 1 − 1 ( v − 1). (u-1)\,\sigma_{\Delta}(u,v)=u^{a}v\,{\rm c}\left(\frac{1}{u},v;a,b\right)+u\left(u^{a}+v^{b}\right)-\frac{v^{b+1}-1}{(v-1)}\,. |  |

###### Proof.

The triangle Δ \Delta comes with the vertex cones

 | 𝒦 1 \displaystyle{\mathcal{K}}_{1} | = { j ( 1, 0) + k ( 0, 1): j, k ≥ 0 }, \displaystyle=\left\{j(1,0)+k(0,1):\,j,k\geq 0\right\}, |  |

 | 𝒦 2 \displaystyle{\mathcal{K}}_{2} | = { ( a, 0) + j ( − 1, 0) + k ( − a, b): j, k ≥ 0 }, \displaystyle=\left\{(a,0)+j(-1,0)+k(-a,b):\,j,k\geq 0\right\}, |  |

 | 𝒦 3 \displaystyle{\mathcal{K}}_{3} | = { ( 0, b) + j ( a, − b) + k ( 0, − 1): j, k ≥ 0 }. \displaystyle=\left\{(0,b)+j(a,-b)+k(0,-1):\,j,k\geq 0\right\}. |  |

Once more we apply the methods of Section 2 and obtain the integer-point transforms

 | σ 𝒦 1 ​ ( u, v) \displaystyle\sigma_{{\mathcal{K}}_{1}}(u,v) | = 1 ( 1 − u) ​ ( 1 − v), \displaystyle=\frac{1}{(1-u)(1-v)}\,, |  |

 | σ 𝒦 2 ​ ( u, v) \displaystyle\sigma_{{\mathcal{K}}_{2}}(u,v) | = u a ​ 1 + ∑ k = 1 b − 1 v k ​ u ⌊ − k ​ a b ⌋ ( 1 − u − 1) ​ ( 1 − u − a ​ v b) = − u a + 1 + u a ​ v ​ c ​ ( 1 u, v, a, b) ( u − 1) ​ ( u − a ​ v b − 1), \displaystyle=u^{a}\frac{1+\sum_{k=1}^{b-1}v^{k}u^{\left\lfloor{-\frac{ka}{b}}\right\rfloor}}{\left(1-u^{-1}\right)\left(1-u^{-a}v^{b}\right)}=-\frac{u^{a+1}+u^{a}v\,{\rm c}\left(\frac{1}{u},v;a,b\right)}{(u-1)\left(u^{-a}v^{b}-1\right)}\,, |  |

 | σ 𝒦 3 ​ ( u, v) \displaystyle\sigma_{{\mathcal{K}}_{3}}(u,v) | = v b ​ 1 + ∑ k = 1 a − 1 u k ​ v ⌊ − k ​ b a ⌋ ( 1 − v − 1) ​ ( 1 − u a ​ v − b) = − v b + 1 + u ​ v b ​ c ​ ( 1 v, u, b, a) ( v − 1) ​ ( u a ​ v − b − 1). \displaystyle=v^{b}\frac{1+\sum_{k=1}^{a-1}u^{k}v^{\left\lfloor{-\frac{kb}{a}}\right\rfloor}}{\left(1-v^{-1}\right)\left(1-u^{a}v^{-b}\right)}=-\frac{v^{b+1}+uv^{b}\,{\rm c}\left(\frac{1}{v},u;b,a\right)}{(v-1)\left(u^{a}v^{-b}-1\right)}\,. |  |

Now Brion’s Theorem 12 gives

 | σ Δ ​ ( u, v) = 1 ( u − 1) ​ ( v − 1) − u a + 1 + u a ​ v ​ c ​ ( 1 u, v, a, b) ( u − 1) ​ ( u − a ​ v b − 1) − v b + 1 + u ​ v b ​ c ​ ( 1 v, u, b, a) ( v − 1) ​ ( u a ​ v − b − 1) \sigma_{\Delta}(u,v)=\frac{1}{(u-1)(v-1)}-\frac{u^{a+1}+u^{a}v\,{\rm c}\left(\frac{1}{u},v;a,b\right)}{(u-1)\left(u^{-a}v^{b}-1\right)}-\frac{v^{b+1}+uv^{b}\,{\rm c}\left(\frac{1}{v},u;b,a\right)}{(v-1)\left(u^{a}v^{-b}-1\right)} |  |

or, after some manipulations,

(3) |  | ( u − 1) ​ ( v − 1) ​ ( u a − v b) ​ σ Δ ​ ( u, v) = u a − v b + u 2 ​ a + 1 ​ ( v − 1) − v 2 ​ b + 1 ​ ( u − 1) + u 2 ​ a ​ v ​ ( v − 1) ​ c ​ ( 1 u, v, a, b) − u ​ v 2 ​ b ​ ( u − 1) ​ c ​ ( 1 v, u, b, a). (u-1)(v-1)\left(u^{a}-v^{b}\right)\sigma_{\Delta}(u,v)=u^{a}-v^{b}+u^{2a+1}(v-1)-v^{2b+1}(u-1)\\ \qquad+u^{2a}v(v-1)\,{\rm c}\left(\frac{1}{u},v;a,b\right)-uv^{2b}(u-1)\,{\rm c}\left(\frac{1}{v},u;b,a\right)\,. |  |

The two Dedekind–Carlitz polynomials in this expression are actually related by reciprocity: after a simple change of variables, Carlitz’s Theorem 1 implies

 | u ​ v b ​ ( u − 1) ​ c ​ ( 1 v, u, b, a) − u a ​ v ​ ( v − 1) ​ c ​ ( 1 u, v, a, b) = u a ​ v − u ​ v b, uv^{b}(u-1)\,{\rm c}\left(\frac{1}{v},u;b,a\right)-u^{a}v(v-1)\,{\rm c}\left(\frac{1}{u},v;a,b\right)=u^{a}v-uv^{b}, |  |

and substituting this into ( 3) finishes the proof. ∎

We remark that we could also deal with triangles with rational vertices. The setup is exactly the same, however, the formulas become quite a bit messier.

## 7. The Mordell–Pommersheim Tetrahedron

In this final section we derive a generating-function equivalent to Theorem 2. It is natural to extend the application of Brion’s theorem in the last section to polytopes in higher dimensions, which we will do with the tetrahedron 𝒯 {\mathcal{T}}. Since our ultimate goal is a geometric proof of Theorem 2, we will apply Brion’s theorem to the dilate t ​ 𝒯 t{\mathcal{T}} for any positive integral t t. As we will see, the following higher-dimensional extensions of Dedekind–Carlitz polynomials will appear naturally in the integer-point transforms of the vertex cones of 𝒯 {\mathcal{T}}. For positive integers a, b, c a,b,c, and indeterminates u, v, w u,v,w, we define the *Dedekind–Rademacher–Carlitz (DRC) sum*

 | drc ⁡ ( u, v, w, a, b, c):= ∑ k = 0 c − 1 ∑ j = 0 b − 1 u ⌊ j ​ a b + k ​ a c ⌋ ​ v j ​ w k. {\rm drc}(u,v,w;a,b,c):=\sum_{k=0}^{c-1}\sum_{j=0}^{b-1}u^{\left\lfloor{\frac{ja}{b}+\frac{ka}{c}}\right\rfloor}v^{j}w^{k}. |  |

The DRC sums are the main ingredients for the integer-point transform of 𝒯 {\mathcal{T}}.

###### Theorem 14.

Let 𝒯 {\mathcal{T}} be the convex hull of ( a, 0, 0) (a,0,0), ( 0, b, 0) (0,b,0), ( 0, 0, c) (0,0,c), and ( 0, 0, 0) (0,0,0), where a, b a,b and c c are pairwise relatively prime positive integers. Then

 |  | ( u − 1) ​ ( v − 1) ​ ( w − 1) ​ ( u a − v b) ​ ( u a − w c) ​ ( v b − w c) ​ σ t ​ 𝒯 ​ ( u, v, w) \displaystyle(u-1)(v-1)(w-1)\left(u^{a}-v^{b}\right)\left(u^{a}-w^{c}\right)\left(v^{b}-w^{c}\right)\sigma_{t{\mathcal{T}}}(u,v,w) |  |

 |  | = u ( t + 2) ​ a ​ ( v − 1) ​ ( w − 1) ​ ( v b − w c) ​ ( ( u − 1) + drc ⁡ ( u − 1, v, w, a, b, c)) \displaystyle\quad=u^{(t+2)a}(v-1)(w-1)\left(v^{b}-w^{c}\right)\left((u-1)+{\rm drc}\left(u^{-1},v,w;a,b,c\right)\right) |  |

 |  | − v ( t + 2) ​ b ​ ( u − 1) ​ ( w − 1) ​ ( u a − w c) ​ ( ( v − 1) + drc ⁡ ( v − 1, u, w, b, a, c)) \displaystyle\qquad-v^{(t+2)b}(u-1)(w-1)\left(u^{a}-w^{c}\right)\left((v-1)+{\rm drc}\left(v^{-1},u,w;b,a,c\right)\right) |  |

 |  | + w ( t + 2) ​ c ​ ( u − 1) ​ ( w − 1) ​ ( u a − v b) ​ ( ( w − 1) + drc ⁡ ( w − 1, u, v, c, a, b)) \displaystyle\qquad+w^{(t+2)c}(u-1)(w-1)\left(u^{a}-v^{b}\right)\left((w-1)+{\rm drc}\left(w^{-1},u,v;c,a,b\right)\right) |  |

 |  | − ( u a − v b) ​ ( u a − w c) ​ ( v b − w c). \displaystyle\qquad-\left(u^{a}-v^{b}\right)\left(u^{a}-w^{c}\right)\left(v^{b}-w^{c}\right). |  |

###### Proof.

The tetrahedron t ​ 𝒯 t{\mathcal{T}} has the vertex cones

 | 𝒦 0 \displaystyle{\mathcal{K}}_{0} | = { λ 1 ( 1, 0, 0) + λ 2 ( 0, 1, 0) + λ 3 ( 0, 0, 1): λ 1, λ 2, λ 3 ≥ 0 }, \displaystyle=\left\{\lambda_{1}(1,0,0)+\lambda_{2}(0,1,0)+\lambda_{3}(0,0,1):\,\lambda_{1},\lambda_{2},\lambda_{3}\geq 0\right\}, |  |

 | 𝒦 1 \displaystyle{\mathcal{K}}_{1} | = { ( t a, 0, 0) + λ 1 ( − 1, 0, 0) + λ 2 ( − a, b, 0) + λ 3 ( − a, 0, c): λ 1, λ 2, λ 3 ≥ 0 }, \displaystyle=\left\{(ta,0,0)+\lambda_{1}(-1,0,0)+\lambda_{2}(-a,b,0)+\lambda_{3}(-a,0,c):\,\lambda_{1},\lambda_{2},\lambda_{3}\geq 0\right\}, |  |

 | 𝒦 2 \displaystyle{\mathcal{K}}_{2} | = { ( 0, t b, 0) + λ 1 ( a, − b, 0) + λ 2 ( 0, − 1, 0) + λ 3 ( 0, − b, c): λ 1, λ 2, λ 3 ≥ 0 }, \displaystyle=\left\{(0,tb,0)+\lambda_{1}(a,-b,0)+\lambda_{2}(0,-1,0)+\lambda_{3}(0,-b,c):\,\lambda_{1},\lambda_{2},\lambda_{3}\geq 0\right\}, |  |

 | 𝒦 3 \displaystyle{\mathcal{K}}_{3} | = { ( 0, 0, t c) + λ 1 ( a, 0, − c) + λ 2 ( 0, b, − c) + λ 3 ( 0, 0, − 1): λ 1, λ 2, λ 3 ≥ 0 }, \displaystyle=\left\{(0,0,tc)+\lambda_{1}(a,0,-c)+\lambda_{2}(0,b,-c)+\lambda_{3}(0,0,-1):\,\lambda_{1},\lambda_{2},\lambda_{3}\geq 0\right\}, |  |

and we will ultimately apply Brion’s Theorem 12 to obtain

(4) |  | σ t ​ 𝒯 ​ ( 𝒛) = σ 𝒦 0 ​ ( 𝒛) + σ 𝒦 1 ​ ( 𝒛) + σ 𝒦 2 ​ ( 𝒛) + σ 𝒦 3 ​ ( 𝒛), \sigma_{t{\mathcal{T}}}({\boldsymbol{z}})=\sigma_{{\mathcal{K}}_{0}}({\boldsymbol{z}})+\sigma_{{\mathcal{K}}_{1}}({\boldsymbol{z}})+\sigma_{{\mathcal{K}}_{2}}({\boldsymbol{z}})+\sigma_{{\mathcal{K}}_{3}}({\boldsymbol{z}})\,, |  |

which will yield Theorem 14.

The computation of the integer-point transforms of the vertex cones should be routine by now; we will derive only one of them in detail. The vertex cone 𝒦 1 {\mathcal{K}}_{1} has the fundamental parallelepiped

 | Π = ( t a, 0, 0) + { λ 1 ( − 1, 0, 0) + λ 2 ( − a, b, 0) + λ 3 ( − a, 0, c): 0 ≤ λ 1, λ 2, λ 3 < 1 }. \Pi=(ta,0,0)+\left\{\lambda_{1}(-1,0,0)+\lambda_{2}(-a,b,0)+\lambda_{3}(-a,0,c):\,0\leq\lambda_{1},\lambda_{2},\lambda_{3}<1\right\}. |  |

There exists exactly one integer point in Π \Pi at each integer j j along the y y -axis and k k along the z z -axis. In other words, for j, k ∈ ℤ ≥ 0 j,k\in\mathbb{Z}_{\geq 0}, ( x, j, k) ∈ Π (x,j,k)\in\Pi is written as ( x, j, k) = ( − λ 1 − λ 2 ​ a − λ 3 ​ a, λ 2 ​ b, λ 3 ​ c) (x,j,k)=\left(-\lambda_{1}-\lambda_{2}a-\lambda_{3}a,\lambda_{2}b,\lambda_{3}c\right) and hence λ 2 = j b \lambda_{2}=\frac{j}{b} and λ 3 = k c \lambda_{3}=\frac{k}{c}. Thus

 | Π ∩ ℤ 3 = { ( ⌊ − j ​ a b − k ​ a c ⌋, j, k): j, k = 0, 1, …, b − 1 } \Pi\cap\mathbb{Z}^{3}=\left\{\left(\left\lfloor{-\frac{ja}{b}-\frac{ka}{c}}\right\rfloor,j,k\right):\,j,k=0,1,\dots,b-1\right\} |  |

and

 | σ 𝒦 1 ​ ( u, v, w) \displaystyle\sigma_{{\mathcal{K}}_{1}}(u,v,w) | = u t ​ a ​ ( ∑ k = 0 c − 1 ∑ j = 0 b = 1 u ⌊ − j ​ a b − k ​ a c ⌋ ​ v j ​ w k ( 1 − u − 1) ​ ( 1 − u − a ​ v b) ​ ( 1 − u − a ​ w c)) \displaystyle=u^{ta}\left(\frac{\sum_{k=0}^{c-1}\sum_{j=0}^{b=1}u^{\left\lfloor{-\frac{ja}{b}-\frac{ka}{c}}\right\rfloor}v^{j}w^{k}}{\left(1-u^{-1}\right)\left(1-u^{-a}v^{b}\right)\left(1-u^{-a}w^{c}\right)}\right) |  |

 |  | = u t ​ a ​ ( 1 + ∑ k = 0 c − 1 ∑ j = 0 b = 1 u − ⌊ j ​ a b + k ​ a c ⌋ − 1 ​ v j ​ w k − u − 1 u − 2 ​ a − 1 ​ ( u − 1) ​ ( u a − v b) ​ ( u a − w c)) \displaystyle=u^{ta}\left(\frac{1+\sum_{k=0}^{c-1}\sum_{j=0}^{b=1}u^{-\left\lfloor{\frac{ja}{b}+\frac{ka}{c}}\right\rfloor-1}v^{j}w^{k}-u^{-1}}{u^{-2a-1}\left(u-1\right)\left(u^{a}-v^{b}\right)\left(u^{a}-w^{c}\right)}\right) |  |

 |  | = u ( t + 2) ​ a ​ [( u − 1) + drc ⁡ ( u − 1, v, w, a, b, c)] ( u − 1) ​ ( u a − v b) ​ ( u a − w c). \displaystyle=\frac{u^{(t+2)a}\left[(u-1)+{\rm drc}\left(u^{-1},v,w;a,b,c\right)\right]}{\left(u-1\right)\left(u^{a}-v^{b}\right)\left(u^{a}-w^{c}\right)}\,. |  |

Similarly, we derive

 | σ 𝒦 2 ​ ( u, v, w) \displaystyle\sigma_{{\mathcal{K}}_{2}}(u,v,w) | = − v ( t + 2) ​ b ​ [( v − 1) + drc ⁡ ( v − 1, u, w, b, a, c)] ( v − 1) ​ ( u a − v b) ​ ( v b − w c), \displaystyle=-\frac{v^{(t+2)b}\left[(v-1)+{\rm drc}\left(v^{-1},u,w;b,a,c\right)\right]}{\left(v-1\right)\left(u^{a}-v^{b}\right)\left(v^{b}-w^{c}\right)}\,, |  |

 | σ 𝒦 3 ​ ( u, v, w) \displaystyle\sigma_{{\mathcal{K}}_{3}}(u,v,w) | = w ( t + 2) ​ c ​ [( w − 1) + drc ⁡ ( w − 1, u, v, c, a, b)] ( w − 1) ​ ( u a − w c) ​ ( v b − w c), \displaystyle=\frac{w^{(t+2)c}\left[(w-1)+{\rm drc}\left(w^{-1},u,v;c,a,b\right)\right]}{\left(w-1\right)\left(u^{a}-w^{c}\right)\left(v^{b}-w^{c}\right)}\,, |  |

and

 | σ 𝒦 0 ​ ( u, v, w) = − 1 ( u − 1) ​ ( v − 1) ​ ( w − 1). \sigma_{{\mathcal{K}}_{0}}(u,v,w)=-\frac{1}{(u-1)(v-1)(w-1)}\,. |  |

Substituting these rational functions into ( 4) and clearing denominators gives the theorem. ∎

###### Proof of Theorem 2.

Theorem 14 gives σ t ​ 𝒯 ​ ( u, v, w) = N D \sigma_{t{\mathcal{T}}}(u,v,w)=\frac{N}{D} with numerator

 | N \displaystyle N | = u ( t + 2) ​ a ​ ( v − 1) ​ ( w − 1) ​ ( v b − w c) ​ ( ( u − 1) + drc ⁡ ( u − 1, v, w, a, b, c)) \displaystyle=u^{(t+2)a}(v-1)(w-1)\left(v^{b}-w^{c}\right)\left((u-1)+{\rm drc}\left(u^{-1},v,w;a,b,c\right)\right) |  |

 |  | − v ( t + 2) ​ b ​ ( u − 1) ​ ( w − 1) ​ ( u a − w c) ​ ( ( v − 1) + drc ⁡ ( v − 1, u, w, b, a, c)) \displaystyle\qquad-v^{(t+2)b}(u-1)(w-1)\left(u^{a}-w^{c}\right)\left((v-1)+{\rm drc}\left(v^{-1},u,w;b,a,c\right)\right) |  |

 |  | + w ( t + 2) ​ c ​ ( u − 1) ​ ( w − 1) ​ ( u a − v b) ​ ( ( w − 1) + drc ⁡ ( w − 1, u, v, c, a, b)) \displaystyle\qquad+w^{(t+2)c}(u-1)(w-1)\left(u^{a}-v^{b}\right)\left((w-1)+{\rm drc}\left(w^{-1},u,v;c,a,b\right)\right) |  |

 |  | − ( u a − v b) ​ ( u a − w c) ​ ( v b − w c) \displaystyle\qquad-\left(u^{a}-v^{b}\right)\left(u^{a}-w^{c}\right)\left(v^{b}-w^{c}\right) |  |

and denominator D = ( u − 1) ​ ( v − 1) ​ ( w − 1) ​ ( u a − v b) ​ ( u a − w c) ​ ( v b − w c) D=(u-1)(v-1)(w-1)\left(u^{a}-v^{b}\right)\left(u^{a}-w^{c}\right)\left(v^{b}-w^{c}\right). We obtain the Ehrhart polynomial L 𝒯 ​ ( t) = σ t ​ 𝒯 ​ ( 1, 1, 1) L_{\mathcal{T}}(t)=\sigma_{t{\mathcal{T}}}(1,1,1) by taking the limit of this rational function as u, v, w → 1 u,v,w\to 1. We need to use L’Hospital’s rule and take partial derivatives with respect to u u once, v v twice, and w w three times in both numerator and denominator before substituting u = v = w = 1 u=v=w=1. This is easily done for the denominator D D with the result − 12 ​ b ​ c 2 -12bc^{2}.

The numerator N N of σ t ​ 𝒯 ​ ( u, v, w) \sigma_{t{\mathcal{T}}}(u,v,w) is not handled as easily. After differentiating and setting u = v = w = 1 u=v=w=1 it becomes

 |  | − 2 ​ a ​ b 2 ​ c 3 ​ t 3 − 6 ​ a ​ b 2 ​ c 3 ​ t 2 − 6 ​ b ​ c 2 ​ t 2 − 4 ​ a ​ b 2 ​ c 3 ​ t − 18 ​ b ​ c 2 ​ t \displaystyle-2ab^{2}c^{3}t^{3}-6ab^{2}c^{3}t^{2}-6bc^{2}t^{2}-4ab^{2}c^{3}t-18bc^{2}t |  |

 |  | + 6 b c t ∑ j = 0 a − 1 ∑ k = 0 c − 1 ⌊ j ​ b a + k ​ b c ⌋ − 6 b c 2 t ∑ j = 0 a − 1 ∑ k = 0 c − 1 ⌊ j ​ b a + k ​ b c ⌋ \displaystyle+6bct\sum_{j=0}^{a-1}\sum_{k=0}^{c-1}\left\lfloor{\frac{jb}{a}+\frac{kb}{c}}\right\rfloor-6bc^{2}t\sum_{j=0}^{a-1}\sum_{k=0}^{c-1}\left\lfloor{\frac{jb}{a}+\frac{kb}{c}}\right\rfloor |  |

(5) |  |  | − 12 b c t ∑ j = 0 a − 1 ∑ k = 0 c − 1 k ⌊ j ​ b a + k ​ b c ⌋ − 6 b c t ∑ j = 0 a − 1 ∑ k = 0 b − 1 ⌊ j ​ c a + k ​ c b ⌋ \displaystyle-12bct\sum_{j=0}^{a-1}\sum_{k=0}^{c-1}k\left\lfloor{\frac{jb}{a}+\frac{kb}{c}}\right\rfloor-6bct\sum_{j=0}^{a-1}\sum_{k=0}^{b-1}\left\lfloor{\frac{jc}{a}+\frac{kc}{b}}\right\rfloor |  |

 |  | + 24 b c 2 t ∑ j = 0 a − 1 ∑ k = 0 b − 1 ⌊ j ​ c a + k ​ c b ⌋ + 6 b c 2 t 2 ∑ j = 0 a − 1 ∑ k = 0 b − 1 ⌊ j ​ c a + k ​ c b ⌋ \displaystyle+24bc^{2}t\sum_{j=0}^{a-1}\sum_{k=0}^{b-1}\left\lfloor{\frac{jc}{a}+\frac{kc}{b}}\right\rfloor+6bc^{2}t^{2}\sum_{j=0}^{a-1}\sum_{k=0}^{b-1}\left\lfloor{\frac{jc}{a}+\frac{kc}{b}}\right\rfloor |  |

 |  | − 6 b c t ∑ j = 0 a − 1 ∑ k = 0 b − 1 ⌊ j ​ c a + k ​ c b ⌋ ( 1 + ⌊ j ​ c a + k ​ c b ⌋) \displaystyle-6bct\sum_{j=0}^{a-1}\sum_{k=0}^{b-1}\left\lfloor{\frac{jc}{a}+\frac{kc}{b}}\right\rfloor\left(1+\left\lfloor{\frac{jc}{a}+\frac{kc}{b}}\right\rfloor\right) |  |

plus numerous terms that do not depend on t t. Fortunately, because the constant term of L 𝒯 L_{\mathcal{T}} is 1 1 (see, for example, [4, Corollary 3.15]), we are not concerned with these extra terms. As before, we replace all greatest-integer functions with fractional-part functions to modify ( 5) to

 |  | − 2 ​ a ​ b 2 ​ c 3 ​ t 3 − 3 ​ b 2 ​ c 3 ​ t 2 − 3 ​ a ​ b ​ c 3 ​ t 2 − 6 ​ b ​ c 2 ​ t 2 − b 2 ​ c 3 a ​ t − 6 ​ a ​ b ​ c 3 ​ t \displaystyle-2ab^{2}c^{3}t^{3}-3b^{2}c^{3}t^{2}-3abc^{3}t^{2}-6bc^{2}t^{2}-\frac{b^{2}c^{3}}{a}t-6abc^{3}t |  |

 |  | − 3 ​ b ​ c 3 ​ t − a ​ c 3 ​ t + 6 ​ a ​ b 2 ​ c 2 ​ t + 6 ​ a ​ b ​ c 2 ​ t − 18 ​ b ​ c 2 ​ t − 5 ​ a ​ b 2 ​ c ​ t \displaystyle-3bc^{3}t-ac^{3}t+6ab^{2}c^{2}t+6abc^{2}t-18bc^{2}t-5ab^{2}ct |  |

(6) |  |  | − 6 b c t ∑ k = 0 c − 1 ∑ j = 0 a − 1 { j ​ b a + k ​ b c } + 6 b c 2 t ∑ k = 0 c − 1 ∑ j = 0 a − 1 { j ​ b a + k ​ b c } + 12 b c t ∑ k = 0 c − 1 ∑ j = 0 a − 1 k { j ​ b a + k ​ b c } \displaystyle-6bct\sum_{k=0}^{c-1}\sum_{j=0}^{a-1}\left\{\frac{jb}{a}+\frac{kb}{c}\right\}+6bc^{2}t\sum_{k=0}^{c-1}\sum_{j=0}^{a-1}\left\{\frac{jb}{a}+\frac{kb}{c}\right\}+12bct\sum_{k=0}^{c-1}\sum_{j=0}^{a-1}k\left\{\frac{jb}{a}+\frac{kb}{c}\right\} |  |

 |  | + 12 b c t ∑ k = 0 b − 1 ∑ j = 0 a − 1 { j ​ c a + k ​ c b } − 24 b c 2 t ∑ k = 0 b − 1 ∑ j = 0 a − 1 { j ​ c a + k ​ c b } − 6 b c 2 t 2 ∑ k = 0 b − 1 ∑ j = 0 a − 1 { j ​ c a + k ​ c b } \displaystyle+12bct\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}\left\{\frac{jc}{a}+\frac{kc}{b}\right\}-24bc^{2}t\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}\left\{\frac{jc}{a}+\frac{kc}{b}\right\}-6bc^{2}t^{2}\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}\left\{\frac{jc}{a}+\frac{kc}{b}\right\} |  |

 |  | + 12 ​ b ​ c 2 a t ∑ k = 0 b − 1 ∑ j = 0 a − 1 j { j ​ c a + k ​ c b } + 12 c 2 t ∑ k = 0 b − 1 ∑ j = 0 a − 1 k { j ​ c a + k ​ c b } − 6 b c t ∑ k = 0 b − 1 ∑ j = 0 a − 1 { j ​ c a + k ​ c b } 2. \displaystyle+\frac{12bc^{2}}{a}t\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}j\left\{\frac{jc}{a}+\frac{kc}{b}\right\}+12c^{2}t\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}k\left\{\frac{jc}{a}+\frac{kc}{b}\right\}-6bct\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}\left\{\frac{jc}{a}+\frac{kc}{b}\right\}^{2}. |  |

Now we use three elementary identities:

 |  | ∑ k = 0 b − 1 ∑ j = 0 a − 1 { j ​ c a + k ​ c b } = a ​ b − 1 2, \displaystyle\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}\left\{\frac{jc}{a}+\frac{kc}{b}\right\}=\frac{ab-1}{2}\,, |  |

 |  | ∑ k = 0 b − 1 ∑ j = 0 a − 1 j ⁡ { j ​ c a + k ​ c b } = c ​ s ​ ( a ​ b, c) + a ​ b ​ ( c − 1) 4, \displaystyle\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}j\left\{\frac{jc}{a}+\frac{kc}{b}\right\}=c\,{\rm s}(ab,c)+\frac{ab(c-1)}{4}\,, |  |

 |  | ∑ k = 0 b − 1 ∑ j = 0 a − 1 { j ​ c a + k ​ c b } 2 = ( a ​ b − 1) ​ ( 2 ​ a ​ b − 1) 6 ​ a ​ b. \displaystyle\sum_{k=0}^{b-1}\sum_{j=0}^{a-1}\left\{\frac{jc}{a}+\frac{kc}{b}\right\}^{2}=\frac{(ab-1)(2ab-1)}{6ab}\,. |  |

They allow us to simplify ( 6) to

 |  | − 2 ​ a ​ b 2 ​ c 3 ​ t 3 − 3 ​ b 2 ​ c 3 ​ t 2 − 3 ​ a ​ b ​ c 3 ​ t 2 − 3 ​ b ​ c 2 ​ t 2 − b 2 ​ c 3 a ​ t − 3 ​ b ​ c 3 ​ t − a ​ c 3 ​ t − 3 ​ b 2 ​ c 2 ​ t \displaystyle-2ab^{2}c^{3}t^{3}-3b^{2}c^{3}t^{2}-3abc^{3}t^{2}-3bc^{2}t^{2}-\frac{b^{2}c^{3}}{a}t-3bc^{3}t-ac^{3}t-3b^{2}c^{2}t |  |

 |  | − 3 ​ a ​ b ​ c 2 ​ t − 9 ​ b ​ c 2 ​ t − a ​ b 2 ​ c ​ t − c a ​ t + 12 ​ b ​ c 2 ​ ( s ⁡ ( a ​ b, c) + s ⁡ ( a ​ c, b) + s ⁡ ( b ​ c, a)) ​ t. \displaystyle-3abc^{2}t-9bc^{2}t-ab^{2}ct-\frac{c}{a}t+12bc^{2}\left({\rm s}(ab,c)+{\rm s}(ac,b)+{\rm s}(bc,a)\right)t\,. |  |

We divide by the denominator − 12 ​ b ​ c 2 -12bc^{2} and add the constant term 1 to arrive at the desired formula for L 𝒯 ​ ( t) L_{\mathcal{T}}(t). ∎

## References

- [1] Gert Almkvist, *Asymptotic formulas and generalized Dedekind sums*, Experiment. Math. 7 (1998), no. 4, 343–359.
- [2] Alexander I. Barvinok, *A polynomial time algorithm for counting integral points in polyhedra when the dimension is fixed*, Math. Oper. Res. 19 (1994), no. 4, 769–779.
- [3] Matthias Beck, *Geometric proofs of polynomial reciprocity laws of Carlitz, Berndt, and Dieter*, Diophantine analysis and related fields 2006, Sem. Math. Sci., vol. 35, Keio Univ., Yokohama, 2006, pp. 11–18.
- [4] Matthias Beck and Sinai Robins, *Computing the continuous discretely: Integer-point enumeration in polyhedra*, Undergraduate Texts in Mathematics, Springer-Verlag, New York, 2007.
- [5] Bruce C. Berndt and Ulrich Dieter, *Sums involving the greatest integer function and Riemann-Stieltjes integration*, J. Reine Angew. Math. 337 (1982), 208–220.
- [6] Michel Brion, *Points entiers dans les polyèdres convexes*, Ann. Sci. École Norm. Sup. (4) 21 (1988), no. 4, 653–663.
- [7] Leonard Carlitz, *Some polynomials associated with Dedekind sums*, Acta Math. Acad. Sci. Hungar. 26 (1975), no. 3-4, 311–319.
- [8] Robin Chapman, *Reciprocity laws for generalized higher dimensional Dedekind sums*, Acta Arith. 93 (2000), no. 2, 189–199.
- [9] Richard Dedekind, *Erläuterungen zu den Fragmenten xxviii*, Collected Works of Bernhard Riemann, Dover Publ., New York, 1953, pp. 466–478.
- [10] Ulrich Dieter, *Das Verhalten der Kleinschen Funktionen log ⁡ σ g, h ​ ( ω 1, ω 2) \log\sigma_{g,h}(\omega_{1},\omega_{2}) gegenüber Modultransformationen und verallgemeinerte Dedekindsche Summen*, J. Reine Angew. Math. 201 (1959), 37–70.
- [11] Eugène Ehrhart, *Sur les polyèdres rationnels homothétiques à n n dimensions*, C. R. Acad. Sci. Paris 254 (1962), 616–618.
- [12] Kurt Girstmair, *Some remarks on Rademacher’s three-term relation*, Arch. Math. (Basel) 73 (1999), no. 3, 205–207.
- [13] Friedrich Hirzebruch and Don Zagier, *The Atiyah-Singer Theorem and Elementary Number Theory*, Publish or Perish Inc., Boston, Mass., 1974.
- [14] Donald E. Knuth, *The Art of Computer Programming. Vol. 2*, second ed., Addison-Wesley Publishing Co., Reading, Mass., 1981.
- [15] Curt Meyer, *Über einige Anwendungen Dedekindscher Summen*, J. Reine Angew. Math. 198 (1957), 143–203.
- [16] Werner Meyer and Robert Sczech, *Über eine topologische und zahlentheoretische Anwendung von Hirzebruchs Spitzenauflösung*, Math. Ann. 240 (1979), no. 1, 69–96.
- [17] Louis J. Mordell, *Lattice points in a tetrahedron and generalized Dedekind sums*, J. Indian Math. Soc. (N.S.) 15 (1951), 41–46.
- [18] James E. Pommersheim, *Toric varieties, lattice points and Dedekind sums*, Math. Ann. 295 (1993), no. 1, 1–24.
- [19] Hans Rademacher, *Generalization of the reciprocity formula for Dedekind sums*, Duke Math. J. 21 (1954), 391–397.
- [20] by same author, *Zur Theorie der Dedekindschen Summen*, Math. Z. 63 (1956), 445–463.
- [21] by same author, *Some remarks on certain generalized Dedekind sums*, Acta Arith. 9 (1964), 97–105.
- [22] David Solomon, *Algebraic properties of Shintani’s generating functions: Dedekind sums and cocycles on PGL 2 ​ ( 𝐐) {\rm PGL}_{2}({\bf Q})*, Compositio Math. 112 (1998), no. 3, 333–362.

[◄][6][image: ar5iv homepage] [7]
[Feeling lucky?][8] [9]
[Conversion report][10]
[Report an issue][11]
[View original on arXiv][12] [►][13]


## Links

[1]: mailto:beck@math.sfsu.edu
[2]: http://math.sfsu.edu/beck
[3]: mailto:christian.haase@math.fu-berlin.de
[4]: http://ehrhart.math.fu-berlin.de
[5]: mailto:asiamath@mast.queensu.ca
[6]: /html/0710.1322
[7]: /
[8]: /feeling_lucky
[9]: /land_of_honey_and_milk
[10]: /log/0710.1323
[11]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0710.1323
[12]: https://arxiv.org/pdf/0710.1323
[13]: /html/0710.1324
