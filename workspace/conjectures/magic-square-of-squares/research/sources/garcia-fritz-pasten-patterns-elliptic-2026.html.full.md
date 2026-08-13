<!-- source: https://arxiv.org/html/2605.14962v1 | converted from HTML -->

Patterns on elliptic curves beyond Bremner’s conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2605.14962v1 [math.NT] 14 May 2026

# Patterns on elliptic curves beyond Bremner’s conjecture Thanks: N.G.-F. was supported by ANID Fondecyt Regular grant 1251300 from Chile. H.P. was supported by ANID Fondecyt Regular grant 1230507 from Chile.

Natalia Garcia-Fritz Address: Departamento de Matemáticas, Pontificia Universidad Católica de Chile. Facultad de Matemáticas, 4860 Av. Vicuña Mackenna, Macul, RM, Chile Email address, N. Garcia-Fritz : [natalia.garcia@uc.cl][3] and Hector Pasten Address: Departamento de Matemáticas, Pontificia Universidad Católica de Chile. Facultad de Matemáticas, 4860 Av. Vicuña Mackenna, Macul, RM, Chile Email address, H. Pasten : [hector.pasten@uc.cl][4]

Date: August 11, 2026

###### Abstract.

In the late 1990’s, Bremner conjectured that long arithmetic progressions among the x x -coordinates of rational points of an elliptic curve E E over ℚ \mathbb{Q} should force the rank of E E to be large. This conjecture (and a broad generalization of it) was proved by the authors two decades later, by combining Nevanlinna theory and the Uniform Mordell–Lang theorem of Gao–Ge–Kühne. The proof inspired subsequent work by the authors where a generalization of the Bogomolov–Fu–Tschinkel conjecture was proved by similar means. In this note we isolate a flexible pattern principle implicit in the latter work, obtaining rank-dependent (but otherwise uniform) bounds for more general patterns in the image of finite rank subgroups of elliptic curves under maps to the projective line. These patterns include, for instance, arithmetic progressions, geometric progressions, additive shifts, multiplicative shifts, and Möbius orbits.

###### Key words and phrases:

Bremner’s conjecture, elliptic curves, patterns, arithmetic progressions, geometric progressions

###### 2020 Mathematics Subject Classification

Primary: 11G05; Secondary: 11B25, 14G05

## 1. Introduction

### 1.1. Bremner’s conjecture

In 1999, Bremner [4] conjectured that long arithmetic progressions in the x x -coordinates of rational points of an elliptic curve E E over ℚ \mathbb{Q} with a given Weierstrass equation, should force the rank of E E to be large. Beyond concrete numerical examples, some theoretical evidence was obtained in [5]. This conjecture was proved by the authors in Theorem 6.1 of [10]:

###### Theorem 1.1 (Proof of Bremner’s conjecture).

Let d d be a positive integer. There is a constant c ⁡ ( d) > 1 c(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C} and Γ \Gamma a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). Let ϕ: E → ℙ 1 \phi:E\to\mathbb{P}^{1} be a degree d d morphism, seen as a rational function on E E. If there are P 1, …, P n ∈ Γ P_{1},...,P_{n}\in\Gamma not poles of ϕ \phi such that ϕ ⁡ ( P 1), …, ϕ ⁡ ( P n) \phi(P_{1}),...,\phi(P_{n}) is a non-constant arithmetic progression in ℂ \mathbb{C}, then

 | n ≤ c ​ ( d) 1 + rank ​ Γ. n\leq c(d)^{1+\mathrm{rank}\,\Gamma}. |  |

Bremner’s conjecture in its classical formulation is the case when d = 2 d=2, E E is defined over ℚ \mathbb{Q}, Γ = E ⁡ ( ℚ) \Gamma=E(\mathbb{Q}), and ϕ \phi is the x x -coordinate map.

To be precise, the result in [10] used a theorem of Rémond [16, 17] that introduced a dependence on the j j -invariant of E E and required E E to be defined over ℚ alg \mathbb{Q}^{\mathrm{alg}}. However, as in all applications of Rémond’s bound, this dependence was removed when the Uniform Mordell–Lang Conjecture was proved by Gao–Ge–Kühne in 2021 [13] (over ℂ \mathbb{C}, not just ℚ alg \mathbb{Q}^{\mathrm{alg}}). See [12] for a more detailed account.

### 1.2. Other patterns

Our purpose is to prove extensions of Bremner’s conjecture to other patterns, not just arithmetic progressions. The main point of this note is to isolate a useful pattern principle implicit in our work [11] on the Bogomolov–Fu–Tschinkel conjecture, namely, Theorem 3.1. While the arguments here are short, the outcome goes far beyond Bremner’s conjecture and it seems worth making it explicit in the literature (see Section 3). For instance, we will obtain:

###### Theorem 1.2 (Möbius recurrences).

Let d d be a positive integer. There is a constant c ⁡ ( d) > 1 c(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over a number field k k, let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism over k k of degree at most d d, and let F: ℙ 1 → ℙ 1 F:\mathbb{P}^{1}\to\mathbb{P}^{1} be an automorphism over k k with no iterate equal to the identity (that is, F ∈ PGL 2 ​ ( k) F\in\mathrm{PGL}_{2}(k) is not a torsion element). If P 1, P 2, …, P n ∈ E ⁡ ( k) P_{1},P_{2},...,P_{n}\in E(k) are pairwise distinct points that satisfy g ⁡ ( P j + 1) = F ⁡ ( g ⁡ ( P j)) g(P_{j+1})=F(g(P_{j})) for each j = 1, 2, …, n − 1 j=1,2,...,n-1, then

 | n ≤ c ​ ( d) 1 + rank ​ E ​ ( k). n\leq c(d)^{1+\mathrm{rank}\,E(k)}. |  |

Note that Bremner’s conjecture follows from the special case when k = ℚ k=\mathbb{Q} and F F has the form F ⁡ ( t) = t + a F(t)=t+a for non-zero values of a ∈ ℚ a\in\mathbb{Q}. On the other hand, taking F ⁡ ( t) = q ​ t F(t)=qt for q ∈ ℚ − { − 1, 0, 1 } q\in\mathbb{Q}-\{-1,0,1\} gives the analogue of Bremner’s conjecture for geometric progressions (see [6, 7] for references on this problem), and so forth. Thus, while this theorem is not the most general result in this note, it already gives a broad generalization of Bremner’s conjecture.

### 1.3. Shifts

Beyond recurrences, there is another kind of pattern that we are able to study: *shifts*. For the sake of exposition here we just state the case of elliptic curves over ℚ \mathbb{Q} and the general case (which includes number fields) will be discussed in Section 3.3.

###### Theorem 1.3 (Additive shifts).

Let d d be a positive integer. There is a constant κ ⁡ ( d) > 1 \kappa(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℚ \mathbb{Q}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism over ℚ \mathbb{Q} of degree ≤ d \leq d seen as a rational function on E E. Let a ∈ ℚ × a\in\mathbb{Q}^{\times}. If S ⊆ g ⁡ ( E ⁡ ( ℚ)) S\subseteq g(E(\mathbb{Q})) and S + a ⊆ g ⁡ ( E ⁡ ( ℚ)) S+a\subseteq g(E(\mathbb{Q})), then

 | #​ S ≤ κ ​ ( d) 1 + rank ​ E ​ ( ℚ). \#S\leq\kappa(d)^{1+\mathrm{rank}\,E(\mathbb{Q})}. |  |

###### Theorem 1.4 (Multiplicative shifts).

Let d d be a positive integer. There is a constant κ ⁡ ( d) > 1 \kappa(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℚ \mathbb{Q}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism over ℚ \mathbb{Q} of degree ≤ d \leq d seen as a rational function on E E. Let q ∈ ℚ − { − 1, 0, 1 } q\in\mathbb{Q}-\{-1,0,1\}. If S ⊆ g ⁡ ( E ⁡ ( ℚ)) S\subseteq g(E(\mathbb{Q})) and q ⋅ S ⊆ g ⁡ ( E ⁡ ( ℚ)) q\cdot S\subseteq g(E(\mathbb{Q})), then

 | #​ S ≤ κ ​ ( d) 1 + rank ​ E ​ ( ℚ). \#S\leq\kappa(d)^{1+\mathrm{rank}\,E(\mathbb{Q})}. |  |

Here is an example of the shift phenomenon in the additive and multiplicative setting, which is not merely a single arithmetic or geometric progression:

###### Example.

Consider the elliptic curve

 | E: y 2 + x ​ y = x 3 − x 2 − 79 ​ x + 289 E:\quad y^{2}+xy=x^{3}-x^{2}-79x+289 |  |

with LMFDB label 234446.a1 [15]. The following values occur as x x -coordinates of rational points on E E:

 | − 10, − 9, − 8, − 7, − 4, 0, 1, 3, 4, 5, 6, 7, 8, 12, 13. -10,-9,-8,-7,-4,0,1,3,4,5,6,7,8,12,13. |  |

Hence, for

 | S = { − 10, − 9, − 8, 0, 3, 4, 5, 6, 7, 12 }, S=\{-10,-9,-8,0,3,4,5,6,7,12\}, |  |

we have

 | S + 1 = { − 9, − 8, − 7, 1, 4, 5, 6, 7, 8, 13 } ⊆ x ⁡ ( E ⁡ ( ℚ)). S+1=\{-9,-8,-7,1,4,5,6,7,8,13\}\subseteq x(E(\mathbb{Q})). |  |

Thus S ⊆ x ⁡ ( E ⁡ ( ℚ)) S\subseteq x(E(\mathbb{Q})) and S + 1 ⊆ x ⁡ ( E ⁡ ( ℚ)) S+1\subseteq x(E(\mathbb{Q})), with #​ S = 10 \#S=10.

The same curve also gives a multiplicative-shift example. Namely,

 | S = { − 4, 3, 4, 6 } S=\{-4,3,4,6\} |  |

satisfies

 | 2 ⋅ S = { − 8, 6, 8, 12 } ⊆ x ⁡ ( E ⁡ ( ℚ)). 2\cdot S=\{-8,6,8,12\}\subseteq x(E(\mathbb{Q})). |  |

It turns out that there is a remarkable aspect of this elliptic curve regarding its rank: it is the elliptic curve of smallest conductor having rank 4 4. ∎

### 1.4. Non-linear recurrences: a motivating example

Our results in Section 3 provide bounds for more general patterns, such as the one in the following example:

###### Example.

Consider the elliptic curve

 | E: y 2 + y = x 3 − 7 ​ x + 6 E:\quad y^{2}+y=x^{3}-7x+6 |  |

with LMFDB label 5077.a1 [15]. Define the quadratic polynomial

 | F ⁡ ( t) = − 1 6 ​ t 2 − 7 6 ​ t + 2. F(t)=-\frac{1}{6}t^{2}-\frac{7}{6}t+2. |  |

Then we have the F F -orbit segment

 | 0, 2, − 1, 3, − 3, 4 0,\ 2,\ -1,\ 3,\ -3,\ 4 |  |

namely,

 | F ⁡ ( 0) = 2, F ⁡ ( 2) = − 1, F ⁡ ( − 1) = 3, F ⁡ ( 3) = − 3, F ⁡ ( − 3) = 4. F(0)=2,\quad F(2)=-1,\quad F(-1)=3,\quad F(3)=-3,\quad F(-3)=4. |  |

These 6 6 numbers occur in x ⁡ ( E ⁡ ( ℚ)) x(E(\mathbb{Q})), as we have the rational points

 | x 0 2 − 1 3 − 3 4 y 2 0 3 3 0 6 \begin{array}[]{c|rrrrrr}x&0&2&-1&3&-3&4\\ \hline\cr y&2&0&3&3&0&6\end{array} |  |

It is worth pointing out that E E is the elliptic curve with smallest conductor having rank 3 3. ∎

In simple terms the general principle will be that, unless a pattern is directly related to the group structure of the elliptic curve, *a long pattern implies large rank*.

### 1.5. Outline of the rest of the paper

The rest of the article is organized as follows: first we will recall our work on the Bogomolov–Fu–Tschinkel conjecture [11] and then we will remark that Bremner’s conjecture, as well as its multiplicative analogue for geometric progressions, are just special cases of that work by choosing appropriate parameters. This will serve as a motivation for the other results of the present work, discussed in Section 3. The main result is Theorem 3.1, that we call *the pattern principle*as it is the underlying tool for all the other pattern bounds in this article.

## 2. From Bogomolov–Fu–Tschinkel to Bremner

### 2.1. Intersecting values of rational functions on elliptic curves

In a series of works [1, 2, 3], Bogomolov, Fu, and Tschinkel formulated the following conjecture:

###### Conjecture 2.1.

There is a constant c c with the following property: If E 1 E_{1} and E 2 E_{2} are elliptic curves defined over ℂ \mathbb{C} given by Weierstrass equations y 2 = f 1 ​ ( x) y^{2}=f_{1}(x) and y 2 = f 2 ​ ( x) y^{2}=f_{2}(x) where f 1 f_{1} and f 2 f_{2} do not have the same roots, then

 | #​ x ​ ( E 1 ​ ( ℂ) tor) ∩ x ⁡ ( E 2 ​ ( ℂ) tor) ≤ c. \#x(E_{1}(\mathbb{C})_{\rm tor})\cap x(E_{2}(\mathbb{C})_{\rm tor})\leq c. |  |

After an initial breakthrough in [8], this conjecture was fully proved due to the proof of the Uniform Manin–Mumford Conjecture as noted in [9]. We refer the reader to [11] for a more detailed discussion of this problem. In the same paper [11] we proved a generalization where the x x -coordinate maps can be replaced by other rational functions, namely:

###### Theorem 2.2.

Let d d be a positive integer. There is a constant c ⁡ ( d) > 1 c(d)>1 such that the following holds:

If E 1 E_{1} and E 2 E_{2} are elliptic curves defined over ℂ \mathbb{C} and g j: E j → ℙ 1 g_{j}:E_{j}\to\mathbb{P}^{1} are non-constant morphisms of degree ≤ d \leq d that do not have the same set of branch values, then

 | #⁡ ( g 1 ​ ( E 1 ​ ( ℂ) tor) ∩ g 2 ​ ( E 2 ​ ( ℂ) tor)) ≤ c ⁡ ( d). \#\left(g_{1}(E_{1}(\mathbb{C})_{\rm tor})\cap g_{2}(E_{2}(\mathbb{C})_{\rm tor})\right)\leq c(d). |  |

In [11] we also prove an arithmetic counterpart:

###### Theorem 2.3.

Let d d be a positive integer. There is a constant c ⁡ ( d) > 1 c(d)>1 such that the following holds:

Let k k be a number field. If E 1 E_{1} and E 2 E_{2} are elliptic curves defined over k k and g j: E j → ℙ 1 g_{j}:E_{j}\to\mathbb{P}^{1} are non-constant morphisms of degree ≤ d \leq d defined over k k that do not have the same set of (complex) branch values, then

 | #⁡ ( g 1 ​ ( E 1 ​ ( k)) ∩ g 2 ​ ( E 2 ​ ( k))) ≤ c ​ ( d) 1 + rank ​ E 1 ​ ( k) + rank ​ E 2 ​ ( k). \#\left(g_{1}(E_{1}(k))\cap g_{2}(E_{2}(k))\right)\leq c(d)^{1+\mathrm{rank}\,E_{1}(k)+\mathrm{rank}\,E_{2}(k)}. |  |

### 2.2. Arithmetic and geometric progressions

Let us consider the following special cases of Theorem 2.3: take k = ℚ k=\mathbb{Q}, E:= E 1 = E 2 E:=E_{1}=E_{2} any elliptic curve over ℚ \mathbb{Q}, and choosing a Weierstrass equation for E E let g 1 = x g_{1}=x be the x x -coordinate map. Let d = 2 d=2. Then take any of the following two choices of g 2 g_{2}:

- (i)

For a ∈ ℚ × a\in\mathbb{Q}^{\times} let g 2 = x + a g_{2}=x+a

- (ii)

For q ∈ ℚ − { 0, − 1, 1 } q\in\mathbb{Q}-\{0,-1,1\} take g 2 = q ​ x g_{2}=qx.

In case (i) we deduce Bremner’s conjecture at once: a sequence P 1, …, P n ∈ E ⁡ ( ℚ) P_{1},...,P_{n}\in E(\mathbb{Q}) with x ⁡ ( P j) = a ​ j + b x(P_{j})=aj+b for some b ∈ ℚ b\in\mathbb{Q} satisfies that

 | x ⁡ ( P j + 1) = x ⁡ ( P j) + a ∈ g 1 ​ ( E ⁡ ( ℚ)) ∩ g 2 ​ ( E ⁡ ( ℚ)) for each ​ j = 1, 2, …, n − 1. x(P_{j+1})=x(P_{j})+a\in g_{1}(E(\mathbb{Q}))\cap g_{2}(E(\mathbb{Q}))\quad\mbox{ for each }j=1,2,...,n-1. |  |

Thus, n ≤ 1 + c ​ ( 2) 1 + 2 ​ r ​ a ​ n ​ k ​ E ​ ( ℚ) n\leq 1+c(2)^{1+2\mathrm{rank}\,E(\mathbb{Q})}. So, a long arithmetic progression on the x x -coordinates of E ⁡ ( ℚ) E(\mathbb{Q}) forces rank ​ E ​ ( ℚ) \mathrm{rank}\,E(\mathbb{Q}) to be large.

Case (ii) immediately gives the analogue of Bremner’s conjecture for geometric progressions: any sequence P 1, …, P n ∈ E ⁡ ( ℚ) P_{1},...,P_{n}\in E(\mathbb{Q}) with x ⁡ ( P j) = p ​ q j x(P_{j})=pq^{j} for some p ∈ ℚ × p\in\mathbb{Q}^{\times} satisfies

 | x ⁡ ( P j + 1) = q ⋅ x ⁡ ( P j) ∈ g 1 ​ ( E ⁡ ( ℚ)) ∩ g 2 ​ ( E ⁡ ( ℚ)) for each ​ j = 1, 2, …, n − 1. x(P_{j+1})=q\cdot x(P_{j})\in g_{1}(E(\mathbb{Q}))\cap g_{2}(E(\mathbb{Q}))\quad\mbox{ for each }j=1,2,...,n-1. |  |

Thus, n ≤ 1 + c ​ ( 2) 1 + 2 ​ r ​ a ​ n ​ k ​ E ​ ( ℚ) n\leq 1+c(2)^{1+2\mathrm{rank}\,E(\mathbb{Q})}; hence, a long geometric progression in x ⁡ ( E ⁡ ( ℚ)) x(E(\mathbb{Q})) forces rank ​ E ​ ( ℚ) \mathrm{rank}\,E(\mathbb{Q}) to be large.

Of course there is nothing special about the x x -coordinate map; any non-constant rational function on E E works as long as we keep the degree bounded, e.g. y y -coordinates. After these examples, the proof of Theorem 1.2 is an exercise (in any case, it will follow from the more general results of Section 3).

The special case (i) is not surprising. After all, our arguments in [11] are modeled after our proof of Bremner’s conjecture [10]: Nevanlinna theory plus Uniform Mordell–Lang. Thus, this should be viewed as the same underlying method rather than as a genuinely different proof.

Regarding the case (ii) of geometric progressions, this particular instance of Theorem 2.3 was recently proved independently by Harrison–Mudgal–Schmidt in [14], using rather different methods. In the present framework it is a specialization of Theorem 2.3, as explained above. We note that the applications in [14] are not restricted to geometric progressions and also include an alternative proof of Bremner’s conjecture; the techniques developed there are of independent interest.

### 2.3. The case of finite rank subgroups

In [11] we presented the main results specialized to two extremal cases: the torsion subgroup of a complex elliptic curve, and the Mordell–Weil group of an elliptic curve over a number field. Both cases had the same proof and, in fact, if instead of choosing a particular finite rank subgroup one makes no choice and simply keeps that level of generality (using the Uniform Mordell–Lang theorem of Gao–Ge–Kühne [13] stated as Theorem 4.1 in [11]) then one obtains:

###### Theorem 2.4.

Let d d be a positive integer. There is a constant c ⁡ ( d) c(d) such that the following holds:

Let E 1 E_{1} and E 2 E_{2} be elliptic curves defined over ℂ \mathbb{C} and g j: E j → ℙ 1 g_{j}:E_{j}\to\mathbb{P}^{1} non-constant morphisms of degree ≤ d \leq d that do not have the same set of branch values. Let Γ j ≤ E j ​ ( ℂ) \Gamma_{j}\leq E_{j}(\mathbb{C}) for j = 1, 2 j=1,2 be finite rank subgroups (not necessarily finitely generated). Then

 | #⁡ ( g 1 ​ ( Γ 1) ∩ g 2 ​ ( Γ 2)) ≤ c ​ ( d) 1 + rank ​ Γ 1 + rank ​ Γ 2. \#\left(g_{1}(\Gamma_{1})\cap g_{2}(\Gamma_{2})\right)\leq c(d)^{1+\mathrm{rank}\,\Gamma_{1}+\mathrm{rank}\,\Gamma_{2}}. |  |

The proof is the same as the arguments presented in [11] which, for the convenience of the reader, will be outlined here:

Consider the abelian surface A = E 1 × E 2 A=E_{1}\times E_{2} and the map f: A → ℙ 1 × ℙ 1 f:A\to\mathbb{P}^{1}\times\mathbb{P}^{1} given by f ⁡ ( P, Q) = ( g 1 ​ ( P), g 2 ​ ( Q)) f(P,Q)=(g_{1}(P),g_{2}(Q)). Let C ⊆ A C\subseteq A be the 1 1 -dimensional subvariety given by the support of f ∗ ​ Δ f^{*}\Delta where Δ \Delta is the diagonal of ℙ 1 × ℙ 1 \mathbb{P}^{1}\times\mathbb{P}^{1}. Let Γ = Γ 1 × Γ 2 \Gamma=\Gamma_{1}\times\Gamma_{2}; this is a finite rank subgroup of A ⁡ ( ℂ) A(\mathbb{C}). The key observation is that, in order to bound

 | #⁡ ( g 1 ​ ( Γ 1) ∩ g 2 ​ ( Γ 2)) \#\left(g_{1}(\Gamma_{1})\cap g_{2}(\Gamma_{2})\right) |  |

it suffices to bound

 | #⁡ ( C ∩ Γ). \#\left(C\cap\Gamma\right). |  |

Such a bound follows at once from the Uniform Mordell–Lang Theorem of Gao–Ge–Kühne [13] provided that

- (i)

One bounds the degree of each component of C C with respect to an ample line bundle, and

- (ii)

One shows that each irreducible component of C C is a curve of geometric genus at least 2 2.

The first requirement is an intersection-theoretic computation.

The second one is achieved via Nevanlinna theory of complex holomorphic maps, because a projective complex curve X X has geometric genus 0 0 or 1 1 precisely when there is a non-constant complex holomorphic map h: ℂ → X h:\mathbb{C}\to X. This is the most delicate part of the argument and it is here where the branching hypothesis is used.

With all these elements in place, Theorem 2.4 follows.

## 3. Main Results

### 3.1. The pattern principle

Here is the main result of this note.

###### Theorem 3.1 (The pattern principle).

Let d d be a positive integer. There is a constant κ 1 ​ ( d) > 1 \kappa_{1}(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} and F: ℙ 1 → ℙ 1 F:\mathbb{P}^{1}\to\mathbb{P}^{1} be non-constant morphisms of degree ≤ d \leq d such that g g and F ∘ g F\circ g do not have the same set of branch values. Let Γ \Gamma be a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). If S ⊆ g ⁡ ( Γ) S\subseteq g(\Gamma) and F ⁡ ( S) ⊆ g ⁡ ( Γ) F(S)\subseteq g(\Gamma), then

 | #​ S ≤ κ 1 ​ ( d) 1 + rank ​ Γ. \#S\leq\kappa_{1}(d)^{1+\mathrm{rank}\,\Gamma}. |  |

###### Proof.

This follows from Theorem 2.4 by taking E 1 = E 2 = E E_{1}=E_{2}=E, Γ 1 = Γ 2 = Γ \Gamma_{1}=\Gamma_{2}=\Gamma, g 1 = g g_{1}=g, g 2 = F ∘ g g_{2}=F\circ g (which has degree ≤ d 2 \leq d^{2}), and observing that

 | F ⁡ ( S) ⊆ g 1 ​ ( Γ) ∩ g 2 ​ ( Γ). F(S)\subseteq g_{1}(\Gamma)\cap g_{2}(\Gamma). |  |

From here the desired bound follows from #​ F ​ ( S) ≥ ( #​ S) / d \#F(S)\geq(\#S)/d. ∎

Before any further analysis, let us immediately point out that the branching hypothesis is necessary. For instance, one could take g: E → ℙ 1 g:E\to\mathbb{P}^{1} as the x x -coordinate map for a fixed Weierstrass equation and F F the corresponding Lattès map for duplication on E E. Then F ⁡ ( x ⁡ ( Γ)) = x ⁡ ( [2] ​ ( Γ)) ⊆ x ⁡ ( Γ) F(x(\Gamma))=x([2](\Gamma))\subseteq x(\Gamma).

As an application of the pattern principle, one has control on the patterns that arise from certain recurrences.

###### Theorem 3.2 (Bounding patterns: recurrences).

Let d d be a positive integer. There is a constant κ 2 ​ ( d) > 1 \kappa_{2}(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} and F: ℙ 1 → ℙ 1 F:\mathbb{P}^{1}\to\mathbb{P}^{1} be non-constant morphisms of degree ≤ d \leq d such that g g and F ∘ g F\circ g do not have the same set of branch values. Let Γ \Gamma be a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). Let n ≥ 1 n\geq 1, α 1 ∈ ℙ 1 ​ ( ℂ) \alpha_{1}\in\mathbb{P}^{1}(\mathbb{C}), and for each j = 1, …, n − 1 j=1,...,n-1 define α j + 1 = F ⁡ ( α j) \alpha_{j+1}=F(\alpha_{j}). Suppose that all the α j \alpha_{j} are distinct and belong to g ⁡ ( Γ) g(\Gamma). Then

 | n ≤ κ 2 ​ ( d) 1 + rank ​ Γ. n\leq\kappa_{2}(d)^{1+\mathrm{rank}\,\Gamma}. |  |

###### Proof.

Take S = { α 1, …, α n − 1 } S=\{\alpha_{1},...,\alpha_{n-1}\} in Theorem 3.1. ∎

Note that these results are, in particular, applicable to the case Γ = E ​ ( ℂ) tor \Gamma=E(\mathbb{C})_{\rm tor} (here the rank is 0 0 so the bounds become uniform) as well as when everything is defined over a number field and Γ \Gamma is the Mordell–Weil group of the elliptic curve.

### 3.2. The case of Möbius transformations

There is a case of particular interest where the branching hypothesis is easily seen to be satisfied: when F F is an automorphism of ℙ 1 \mathbb{P}^{1} of infinite order in PGL 2 ​ ( ℂ) \mathrm{PGL}_{2}(\mathbb{C}). Indeed, any non-constant map g: E → ℙ 1 g:E\to\mathbb{P}^{1} is branched on at least 3 3 values in ℙ 1 \mathbb{P}^{1}, and an F ∈ PGL 2 ​ ( ℂ) F\in\mathrm{PGL}_{2}(\mathbb{C}) that permutes them has finite order. Let us state the corresponding two consequences in this setting.

###### Theorem 3.3 (The Möbius case: invariant sets).

Let d d be a positive integer. There is a constant κ 1 ​ ( d) > 1 \kappa_{1}(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism of degree ≤ d \leq d and let F ∈ PGL 2 ​ ( ℂ) F\in\mathrm{PGL}_{2}(\mathbb{C}) be an automorphism of ℙ 1 \mathbb{P}^{1} of infinite order. Let Γ \Gamma be a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). If S ⊆ g ⁡ ( Γ) S\subseteq g(\Gamma) and F ⁡ ( S) ⊆ g ⁡ ( Γ) F(S)\subseteq g(\Gamma), then

 | #​ S ≤ κ 1 ​ ( d) 1 + rank ​ Γ. \#S\leq\kappa_{1}(d)^{1+\mathrm{rank}\,\Gamma}. |  |

###### Theorem 3.4 (The Möbius case: orbits).

Let d d be a positive integer. There is a constant κ 2 ​ ( d) > 1 \kappa_{2}(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism of degree ≤ d \leq d and let F ∈ PGL 2 ​ ( ℂ) F\in\mathrm{PGL}_{2}(\mathbb{C}) be an automorphism of ℙ 1 \mathbb{P}^{1} of infinite order. Let Γ \Gamma be a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). Let n ≥ 1 n\geq 1, α 1 ∈ ℙ 1 ​ ( ℂ) \alpha_{1}\in\mathbb{P}^{1}(\mathbb{C}), and for each j = 1, …, n − 1 j=1,...,n-1 define α j + 1 = F ⁡ ( α j) \alpha_{j+1}=F(\alpha_{j}). Suppose that all the α j \alpha_{j} are distinct and belong to g ⁡ ( Γ) g(\Gamma). Then

 | n ≤ κ 2 ​ ( d) 1 + rank ​ Γ. n\leq\kappa_{2}(d)^{1+\mathrm{rank}\,\Gamma}. |  |

Note that Theorem 1.2 is a special case of Theorem 3.4.

### 3.3. Addition and multiplication

By a suitable choice of F F in Theorem 3.4 we recover Bremner’s conjecture for arithmetic progressions and geometric progressions in a very general form. But actually Theorem 3.3 gives more:

###### Corollary 3.5 (Additive shifts).

Let d d be a positive integer. There is a constant κ 1 ​ ( d) > 1 \kappa_{1}(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism of degree ≤ d \leq d seen as a rational function on E E. Let a ∈ ℂ × a\in\mathbb{C}^{\times}. Let Γ \Gamma be a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). If S ⊆ g ⁡ ( Γ) S\subseteq g(\Gamma) and S + a ⊆ g ⁡ ( Γ) S+a\subseteq g(\Gamma), then

 | #​ S ≤ κ 1 ​ ( d) 1 + rank ​ Γ. \#S\leq\kappa_{1}(d)^{1+\mathrm{rank}\,\Gamma}. |  |

###### Corollary 3.6 (Multiplicative shifts).

Let d d be a positive integer. There is a constant κ 1 ​ ( d) > 1 \kappa_{1}(d)>1 depending only on d d such that the following holds:

Let E E be an elliptic curve over ℂ \mathbb{C}. Let g: E → ℙ 1 g:E\to\mathbb{P}^{1} be a non-constant morphism of degree ≤ d \leq d seen as a rational function on E E. Let q ∈ ℂ × q\in\mathbb{C}^{\times} be a complex number which is not a root of unity. Let Γ \Gamma be a finite rank subgroup of E ⁡ ( ℂ) E(\mathbb{C}). If S ⊆ g ⁡ ( Γ) S\subseteq g(\Gamma) and q ⋅ S ⊆ g ⁡ ( Γ) q\cdot S\subseteq g(\Gamma), then

 | #​ S ≤ κ 1 ​ ( d) 1 + rank ​ Γ. \#S\leq\kappa_{1}(d)^{1+\mathrm{rank}\,\Gamma}. |  |

As it might be of particular interest, at this point we insist that our results are valid in the special cases Γ = E ​ ( ℂ) tor \Gamma=E(\mathbb{C})_{\rm tor} and when Γ \Gamma is the Mordell–Weil group of an elliptic curve over a number field. The latter case over ℚ \mathbb{Q} precisely gives the theorems stated in Section 1.3.

## 4. Acknowledgments

N.G.-F. was supported by ANID Fondecyt Regular grant 1251300 from Chile. H.P. was supported by ANID Fondecyt Regular grant 1230507 from Chile.

## References

- [1] F. Bogomolov, H. Fu, *Division polynomials and intersection of projective torsion points*. Eur. J. Math. 2(3) (2016), 644-660.
- [2] F. Bogomolov, H. Fu, Y. Tschinkel, *Torsion of elliptic curves and unlikely intersections*. in: Geometry and Physics, Vol. I (eds. J. E. Andersen, A. Dancer and O. García-Prada) (Oxford University Press, Oxford, 2018), 19-37.
- [3] F. Bogomolov, Y. Tschinkel, *Algebraic varieties over small fields*. in: Diophantine Geometry, CRM Series, 4 (ed. U. Zannier) (Scuola Normale Superiore di Pisa, Pisa, 2007), 73-91.
- [4] A. Bremner, *On arithmetic progressions on elliptic curves*. Experimental Mathematics, 1999, vol. 8, no 4, p. 409-413.
- [5] A. Bremner, J. Silverman, N. Tzanakis, *Integral points in arithmetic progression on y 2 = x ⁡ ( x 2 − n 2) y^{2}=x(x^{2}-n^{2})*. Journal of Number Theory, (2000) 80(2), 187-208.
- [6] A. Bremner, M. Ulas, *Rational points in geometric progressions on certain hyperelliptic curves*. Publ. Math. Debrecen 82.3–4 (2013): 669-683.
- [7] A. Ciss, D. Moody, *Geometric progressions on elliptic curves*. Glasnik matematicki 52.1 (2017): 1-10.
- [8] L. DeMarco, H. Krieger, H. Ye, *Uniform Manin-Mumford for a family of genus 2 curves*. Ann. of Math. (2) 191 (2020), no. 3, 949-1001.
- [9] H. Fu, M. Stoll, *Elliptic curves with common torsion x x -coordinates and hyperelliptic torsion packets*. Proc. Amer. Math. Soc. 150 (2022), no. 12, 5137-5149.
- [10] N. Garcia-Fritz, H. Pasten, *Elliptic curves with long arithmetic progressions have large rank*. Int. Math. Res. Not. IMRN 2021, no. 10, 7394-7432.
- [11] N. Garcia-Fritz, H. Pasten, *Intersecting the torsion of elliptic curves*. Bull. Aust. Math. Soc. 110 (2024), no. 1, 56-63.
- [12] N. Garcia-Fritz, H. Pasten, *A note on Bremner’s conjecture and uniformity*. Preprint (2026) arXiv:2604.04850
- [13] Z. Gao, T. Ge, L. Kühne, *The Uniform Mordell-Lang Conjecture*. (2021) to appear in Publ. Math. IHES.
- [14] J. Harrison, A. Mudgal, H. Schmidt, *Uniform sum-product phenomenon for algebraic groups and Bremner’s conjecture*. Preprint (2026) arXiv:2603.06483
- [15] The LMFDB Collaboration, *The L L -functions and modular forms database*. [https://www.lmfdb.org][5] (2026).
- [16] G. Rémond, *Décompte dans une conjecture de Lang*. Inventiones Mathematicae, (2000) 142 (3), 513-545.
- [17] G. Rémond, *Sur les sous-variétés des tores*. Compositio Mathematica 134.3 (2002) 337-366.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:natalia.garcia@uc.cl
[4]: mailto:hector.pasten@uc.cl
[5]: https://www.lmfdb.org
