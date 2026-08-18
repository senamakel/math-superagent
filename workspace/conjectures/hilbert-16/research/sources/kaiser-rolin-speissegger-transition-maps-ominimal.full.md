<!-- source: https://ar5iv.labs.arxiv.org/html/math/0612745 | converted from HTML -->

[math/0612745] Transition maps at non-resonant hyperbolic singularities are o-minimal

# Transition maps at non-resonant hyperbolic singularities are o-minimal Thanks: Supported by DFG, CNRS and NSERC

T. Kaiser, J.-P. Rolin and P. Speissegger Address: Universität Regensburg
NWF I-Mathematik
93040 Regensburg, Germany Email address: [tobias.kaiser@mathematik.uni-regensburg.de][1] Address: Université de Bourgogne
UFR Sciences et Techniques
9 avenue Alain Savary - B.P. 47870
21078 Dijon Cedex
France Email address: [Jean-Philippe.Rolin@u-bourgogne.fr][2] Address: McMaster University
Department of Mathematics & Statistics, 1280 Main Street West
Hamilton, Ontario L8S 4K1
Canada Email address: [speisseg@math.mcmaster.ca][3]

Date: August 8, 2026; Preprint.

###### Abstract.

We construct a model complete and o-minimal expansion ℝ 𝒬 \mathbb{R}_{\mathcal{Q}} of the field of real numbers such that, for any planar analytic vector field ξ \xi and any isolated, non-resonant hyperbolic singularity p p of ξ \xi, a transition map for ξ \xi at p p is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. This expansion also defines all convergent generalized power series with natural support and is polynomially bounded.

###### Key words and phrases:

Vector fields, transition maps, o-minimal structures

###### 1991 Mathematics Subject Classification

37C27, 37E35, 03C64

## Introduction

One of the motivations for this paper is the following: let ξ \xi be a (real) analytic vector field on ℝ 2 \mathbb{R}^{2} such that ξ − 1 ​ ( 0) = { p } \xi^{-1}(0)=\{p\} is an isolated singularity of ξ \xi. We assume here that the flow of ξ \xi near p p is as pictured in Figure 1 below: there are two trajectories of ξ \xi at p p, one incoming to p p, called γ − \gamma^{-}, and the other outgoing from p p, called γ + \gamma^{+}. To describe the flow of ξ \xi near these trajectories, we fix two small segments Λ − \Lambda^{-} and Λ + \Lambda^{+} transverse to ξ \xi and equipped with analytic charts x x and y y such that x = 0 x=0 is the intersection point of γ − \gamma^{-} with Λ − \Lambda^{-} and x > 0 x>0 to the right of γ − \gamma^{-}, and similarly y = 0 y=0 is the intersection point of γ + \gamma^{+} with Λ + \Lambda^{+} and y > 0 y>0 above γ + \gamma^{+}. Then for all sufficiently small x > 0 x>0, the trajectory of ξ \xi crossing Λ − \Lambda^{-} in the point x x later crosses Λ + \Lambda^{+} in the point y = g ⁡ ( x) y=g(x) of Λ + \Lambda^{+}.

-4,-3.3)(3.65,3.65) \pstVerb 1 setlinejoin (-1.9895,-2.0386)(0.1228,0.1228)

Figure 1. Transition map g g at the hyperbolic singular point p p

For any sufficiently small ϵ > 0 \epsilon>0, the map g: ( 0, ϵ) ⟶ ( 0, ∞) g:(0,\epsilon)\longrightarrow(0,\infty) defined in this way is called a transition map of ξ \xi at p p. The study of transition maps is at the heart of Ilyashenko’s solution of Dulac’s Problem [7]. Somewhat more precisely, Ilyashenko proves that any finite composition of such transition maps has only finitely many isolated fixed points. (Independently, Ecalle [6] proves that these maps are analyzable and deduces his own proof of Dulac’s Problem.)

Ilyashenko’s analysis of transition maps suggests to us the following

Question: are the transition maps of ξ \xi near p p definable in some fixed o-minimal expansion ℛ \mathcal{R} of the real field?

If the answer to this question is positive, it would follow that some Poincaré return map near any polycycle of ξ \xi (see Section 8 for details) is also definable in ℛ \mathcal{R}, because the family of functions definable in ℛ \mathcal{R} is closed under composition. It would then follow from Dulac’s arguments [5] that ξ \xi has at most finitely many limit cycles.

In this paper, we give a positive answer to the above question under some restrictions on ξ \xi. First, we assume that the singularity p p of ξ \xi is hyperbolic, that is, the linear part of ξ \xi at p p has two nonzero real eigenvalues of opposite signs. In this situation, Dulac proves in [5, chapters 23 and 35] that for a transition map g g as above, there exist a choice of charts x x and y y, a p 0 > 0 p_{0}>0, real polynomials p j p_{j} in one variable for j = 1, 2, … j=1,2,\dots, and real numbers 0 < ν 0 < ν 1 < ⋯ 0<\nu_{0}<\nu_{1}<\cdots, such that lim j ν j = + ∞ \lim_{j}\nu_{j}=+\infty and for every n ∈ ℕ n\in\mathbb{N} the following asymptotic relation holds:

- (D)

g ⁡ ( x) − p 0 ​ x ν 0 − ∑ j = 1 n p j ​ ( log ⁡ x) ​ x ν j = o ⁡ ( x ν n) g(x)-p_{0}x^{\nu_{0}}-\sum_{j=1}^{n}p_{j}(\log x)x^{\nu_{j}}=o\left(x^{\nu_{n}}\right) as x → 0 x\to 0.

Moreover, Ilyashenko obtains the following strengthening in Chapter 1 of [7]: a set W ⊆ ℂ W\subseteq\mathbb{C} is a standard quadratic domain if there are constant c ∈ ℝ c\in\mathbb{R} and C > 0 C>0 such that

 | W = { z ∈ ℂ: Re ⁡ z < c − C ​ | Im ⁡ z | }. W=\left\{z\in\mathbb{C}:\ \re z<c-C\sqrt{|\im z|}\right\}. |  |

Then for g g as above,

- (I1)

there exists a standard quadratic domain W ⊆ ℂ W\subseteq\mathbb{C} such that g ∘ exp g\circ\exp extends to a holomorphic mapping G: W ⟶ ℂ G:W\longrightarrow\mathbb{C};

- (I2)

for all n ∈ ℕ n\in\mathbb{N}, we have the asymptotic relation

 | G ( z) − p 0 e ν 0 ​ z − ∑ j = 1 n p j ( z) e ν j ​ z = o ( e ν n ​ Re ⁡ z) as | z | → + ∞ in W. G(z)-p_{0}e^{\nu_{0}z}-\sum_{j=1}^{n}p_{j}(z)e^{\nu_{j}z}=o\left(e^{\nu_{n}\re z}\right)\text{ as }|z|\to+\infty\text{ in }W. |  |

Slightly abusing notations (to be clarified in Section 2 below), we summarize here conditions (I1) and (I2) by saying that there is a standard quadratic domain W ⊆ ℂ W\subseteq\mathbb{C} such that g ∼ W p 0 x ν 0 + ∑ n = 1 ∞ p j ( log x) x ν n g\sim_{W}p_{0}x^{\nu_{0}}+\sum_{n=1}^{\infty}p_{j}(\log x)x^{\nu_{n}}. A Phragmen-Lindelöf argument [7, p. 23] shows that these conditions suffice to conclude that g g has at most finitely many isolated fixed points.

The main body of Ilyashenko’s proof consists in extending this Phragmen-Lindelöf argument to finite compositions of transition maps (not just in the hyperbolic case). In contrast, our approach is to try to prove that all transition maps generate an o-minimal expansion of the real field. Since finite compositions of functions definable in an o-minimal structure are again definable in that same structure, it would then follow that all finite compositions of transition maps have finitely many isolated fixed points.

In this paper, we carry out our approach under the additional hypotheses of hyperbolicity and

- (NR)

the singularity p p is non-resonant, that is, the ratio of the two eigenvalues of the linear part of ξ \xi at p p is an irrational number.

It follows from Dulac’s argument that under the assumption (NR), the polynomials p j p_{j} in the asymptotic series of g g above are all constant.

Thus, we let ℝ ​ [[X ∗]] ω \mathbb{R}[\![X^{*}]\!]^{\omega} be the set of all formal power series F = ∑ α ≥ 0 a α ​ X α F=\sum_{\alpha\geq 0}a_{\alpha}X^{\alpha} such that a α ∈ ℝ a_{\alpha}\in\mathbb{R} for each α ≥ 0 \alpha\geq 0 and the support

 | supp ⁡ ( F):= { α ≥ 0: a α ≠ 0 } \supp(F):=\left\{\alpha\geq 0:\ a_{\alpha}\neq 0\right\} |  |

of F F is such that supp ⁡ ( F) ∩ [0, R] \supp(F)\cap[0,R] is finite for every R > 0 R>0. Note that ℝ ​ [[X ∗]] ω \mathbb{R}[\![X^{*}]\!]^{\omega} is a subset of the set ℝ ⁡ [[X ∗]] \mathbb{R}[\![X^{*}]\!] of all generalized power series defined by Van den Dries and Speissegger in [3]. (In the latter, o-minimality is established for the expansion of the real field by all convergent generalized power series; in contrast, the generalized power series studied here are in general not convergent.) Since we do not use the larger class ℝ ⁡ [[X ∗]] \mathbb{R}[\![X^{*}]\!] here, we shall routinely omit the superscript ω \omega.

Next, for every ϵ > 0 \epsilon>0, we let 𝒬 ϵ \mathcal{Q}_{\epsilon} be the set of all functions f: [0, ϵ] ⟶ ℝ f:[0,\epsilon]\longrightarrow\mathbb{R} for which there exist an F ∈ ℝ ⁡ [[X ∗]] F\in\mathbb{R}[\![X^{*}]\!] and a standard quadratic domain W ⊆ ℂ W\subseteq\mathbb{C} such that ( 0, ϵ] ⊆ exp ⁡ ( W) (0,\epsilon]\subseteq\exp(W) and f ∼ W F f\sim_{W}F. (Thus by definition, for any f ∈ 𝒬 ϵ f\in\mathcal{Q}_{\epsilon} the only point in [0, ϵ] [0,\epsilon] where f f is not necessarily analytic is 0 0.) Our goal here is to prove that the expansion of the real field by all functions in 𝒬 1 \mathcal{Q}_{1} is o-minimal; to do so, we follow the method developed in [3].

Roughly speaking, the method in [3] goes as follows: starting from a quasianalytic class 𝒞 \mathcal{C} of functions in several variables, we consider “mixed” functions that behave like functions in 𝒞 \mathcal{C} for some of the variables and are analytic in the remaining variables [3, section 5]. We show that the algebra of these mixed functions possesses certain closure properties [3, section 6], most notably closure under blow-up substitutions (which correspond to the charts of certain blowings-up) and under Weierstrass preparation with respect to the analytic variables. These closure properties allow us [3, section 7 and Proposition 8.4] to use resolution of singularities to describe 𝒞 \mathcal{C} -sets, which are defined by equations and inequalities among functions from 𝒞 \mathcal{C}; in particular, we show that 𝒞 \mathcal{C} -sets have finitely many connected components. We then adapt in [3, section 8] Gabrielov’s fiber cutting argument to conclude that the complement of a projection of a 𝒞 \mathcal{C} -set is again the projection of a 𝒞 \mathcal{C} -set. The o-minimality of the expansion of the real field by the functions in 𝒞 \mathcal{C} follows as outlined in [3, section 2].

This means in particular that we need to define classes 𝒬 ρ \mathcal{Q}_{\rho}, where ρ ∈ ( 0, ∞) m \rho\in(0,\infty)^{m} is a polyradius, of functions f: [0, ρ 1] × ⋯ × [0, ρ m] ⟶ ℝ f:[0,\rho_{1}]\times\cdots\times[0,\rho_{m}]\longrightarrow\mathbb{R} with analytic-extension and asymptotic properties in several variables corresponding to (I1) and (I2) above. It turns out, however, that the most natural definition of these 𝒬 ρ \mathcal{Q}_{\rho} is insufficient to obtain all the necessary closure properties, and we refer the reader to Section 5 for the correct definition of these classes.

Once the classes 𝒬 ρ \mathcal{Q}_{\rho} are introduced we define, for each m ∈ ℕ m\in\mathbb{N} and m m -variable function f ∈ 𝒬 1, …, 1 f\in\mathcal{Q}_{1,\dots,1}, a total function f ~: ℝ m ⟶ ℝ \widetilde{f}:\mathbb{R}^{m}\longrightarrow\mathbb{R} given by

 | f ~ ​ ( x):= { f ⁡ ( x) if ​ x ∈ [0, 1] m, 0 otherwise. \widetilde{f}(x):=\begin{cases}f(x)&\text{if }x\in[0,1]^{m},\\ 0&\text{otherwise.}\end{cases} |  |

We let ℝ 𝒬:= ( ℝ, <, 0, 1, +, −, ⋅, ( f ~: f ∈ 𝒬 1, …, 1, m ∈ ℕ)) \mathbb{R}_{\mathcal{Q}}:=\left(\mathbb{R},<,0,1,+,-,\ \!\cdot\ \!,\left(\widetilde{f}:\ f\in\mathcal{Q}_{1,\dots,1},m\in\mathbb{N}\right)\right); note that in particular, every function in 𝒬 ϵ \mathcal{Q}_{\epsilon}, for any ϵ > 0 \epsilon>0, is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. Our partial answer to the question above is the following:

###### Theorem A 0.

The structure ℝ 𝒬 \mathbb{R}_{\mathcal{Q}} is model complete, o-minimal and admits analytic cell decomposition.

Moreover, our method of proving Theorem A also gives a kind of “Puiseux theorem” for the one-variable functions definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}:

###### Theorem B 0.

Let ϵ > 0 \epsilon>0 and f: ( 0, ϵ) ⟶ ℝ f:(0,\epsilon)\longrightarrow\mathbb{R} be definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. Then there are a function g ∈ 𝒬 δ g\in\mathcal{Q}_{\delta} for some δ ∈ ( 0, ϵ) \delta\in(0,\epsilon) and an r ∈ ℝ r\in\mathbb{R} such that g ⁡ ( 0) ≠ 0 g(0)\neq 0 and f ⁡ ( x) = x r ​ g ​ ( x) f(x)=x^{r}g(x) for all x ∈ ( 0, δ) x\in(0,\delta).

Our discussion above of transition maps now implies:

###### Corollary 0.

Assume that p p is a non-resonant hyperbolic singularity of ξ \xi, and let g: ( 0, ϵ) ⟶ ( 0, ∞) g:(0,\epsilon)\longrightarrow(0,\infty) be a transition map of ξ \xi at p p, expressed in the charts x x and y y such that (D) holds. Then for every δ ∈ ( 0, ϵ) \delta\in(0,\epsilon), the function g | ( 0, δ) g|_{(0,\delta)} is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. ∎

The transition maps discussed here are not the only functions of interest definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}: in two forthcoming papers, the first author shows that both the Riemann maps and the solutions of Dirichlet’s Problem on certain subanalytic domains with non-analytic boundary are definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}.

Moreover, we construct in Section 8 of this paper an analytic unfolding ξ μ \xi_{\mu} of ξ \xi in a neighbourhood of a polycycle Γ \Gamma of ξ \xi, in the spirit of Roussarie [9]. The unfolding ξ μ \xi_{\mu} is such that each ξ μ \xi_{\mu} has the same set of singularities as ξ \xi and each of these singularities is non-resonant hyperbolic. Thus we obtain an analytic family of transition maps at each of these singularities; in fact, we show that each such family of transition maps is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. It follows that there is a definable family of functions P μ P_{\mu} such that for every μ \mu, the function P μ P_{\mu} is a Poincaré return map for ξ μ \xi_{\mu} near Γ \Gamma. The uniform finiteness property of o-minimal structures [2, chapter 3, section 3] then implies that there is a uniform bound on the number of fixed points of these functions P μ P_{\mu}. The question whether such uniform bounds exist is related to Hilbert’s 16th problem and remains open for general ξ \xi and Γ \Gamma. (See [8] for a survey on Hilbert’s 16th problem and [9] for the relationship between Hilbert’s 16th problem and analytic unfoldings.)

Except for Section 8, the content of this paper is entirely focussed on the construction of the o-minimal structure ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. There are various related questions that we do not know how to answer at this point, such as:

1. (1)

Is ℝ 𝒢 \mathbb{R}_{\mathcal{G}}, the o-minimal structure generated by all functions that are multisummable in the positive real direction [4], a reduct of ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}? Or is ℝ 𝒬 \mathbb{R}_{\mathcal{Q}} a reduct of the Pfaffian closure of ℝ 𝒢 \mathbb{R}_{\mathcal{G}} (see [10])?

2. (2)

Are transition maps near resonant hyperbolic singularities of ξ \xi definable in the Pfaffian closure of ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}?

This paper is organized as follows: in Section 1, we define the class of generalized power series with natural support, and we establish some truncation properties needed later. Our first and most straightforward attempt at defining the classes 𝒬 ρ \mathcal{Q}_{\rho} is made in Section 2, where we also establish some useful criteria for functions to belong to these classes. The reasons why this first attempt is insufficient are explained in Section 3, which lead us to a correct definition in Section 5, where we also establish the first closure properties needed to apply the method of [3]. In fact, in order to apply this method, we need to introduce corresponding “mixed” functions that are, roughly speaking, of asymptotic type (I1) and (I2) in some variables and analytic in the other variables. One of the reasons for studying these mixed classes is discussed in Section 6, where we show that they admit Weierstrass preparation with respect to the analytic variables. To reduce the study of sets defined by functions in the 𝒬 ρ \mathcal{Q}_{\rho} to that of sets defined by functions in the mixed classes, we use the blow-up substitutions introduced in Section 4. Having established all the properties necessary to apply the method of [3], we obtain Theorems A and B in Section 7.

## 1. Generalized power series with natural support

Let m ∈ ℕ m\in\mathbb{N}, and let X = ( X 1, …, X m) X=(X_{1},\dots,X_{m}) be a tuple of indeterminates. For α = ( α 1, …, α m) ∈ [0, ∞) m \alpha=(\alpha_{1},\dots,\alpha_{m})\in[0,\infty)^{m}, we write X α:= X 1 α 1 ⋯ X m α m X^{\alpha}:=X_{1}^{\alpha_{1}}\cdots X_{m}^{\alpha_{m}}, and we let X ∗ X^{*} be the multiplicative monoid consisting of all such X α X^{\alpha}, multiplied according to X α ⋅ X β = X α + β X^{\alpha}\cdot X^{\beta}=X^{\alpha+\beta}. The identity element of X ∗ X^{*} is X 0 = 1 X^{0}=1, where 0 = ( 0, …, 0) 0=(0,\dots,0).

Let A A be a commutative ring with 1 ≠ 0 1\neq 0. We let A ⁡ [[X ∗]] A[\![X^{*}]\!] denote the set of all formal power series f ⁡ ( X) = ∑ α ≥ 0 a α ​ X α f(X)=\sum_{\alpha\geq 0}a_{\alpha}X^{\alpha} such that a α ∈ A a_{\alpha}\in A for each α ≥ 0 \alpha\geq 0 and the support supp ⁡ ( f):= { α ≥ 0: a α ≠ 0 } \supp(f):=\left\{\alpha\geq 0:\ a_{\alpha}\neq 0\right\} of f f is well-ordered, as defined in Section 4.4 of [3]. The elements of A ⁡ [[X ∗]] A[\![X^{*}]\!] are called generalized power series.

###### Definition 1.1.

A set S ⊆ [0, ∞) m S\subseteq[0,\infty)^{m} is natural if Π X i ​ ( S) ∩ [0, R] \Pi_{X_{i}}(S)\cap[0,R] is finite for every R > 0 R>0 and each i = 1, …, m i=1,\dots,m, where Π X i: ℝ m ⟶ ℝ \Pi_{X_{i}}:\mathbb{R}^{m}\longrightarrow\mathbb{R} is the projection on the coordinate X i X_{i}.

We denote by A ​ [[X ∗]] ω A[\![X^{*}]\!]^{\omega} the set of all generalized power series in X X whose support is a natural subset of [0, ∞) m [0,\infty)^{m}.

### Convention

All results established in Section 4 of [3] go through literally with A ​ [[X ∗]] ω A[\![X^{*}]\!]^{\omega} in place of A ⁡ [[X ∗]] A[\![X^{*}]\!], as already pointed out in the second concluding remark of that paper. To simplify notations, we shall from now on omit the superscript ω \omega. Thus, throughout this paper, every series in A ⁡ [[X ∗]] A[\![X^{*}]\!] is assumed to have natural support, and all results in [3] referenced here are interpreted in this context.

Let Y = ( Y 1, …, Y n) Y=(Y_{1},\dots,Y_{n}) be another tuple of indeterminates. For a, b ∈ ℝ k a,b\in\mathbb{R}^{k}, we write a ≤ b a\leq b (resp. a < b a<b) if and only if a i ≤ b i a_{i}\leq b_{i} (resp. a i < b i a_{i}<b_{i}) for i = 1, …, k i=1,\dots,k.

###### Definition 1.2.

Let S ⊆ [0, ∞) m × ℕ n S\subseteq[0,\infty)^{m}\times\mathbb{N}^{n} and F = ∑ a ( α, β) ​ X α ​ Y β ∈ A ⁡ [[X ∗, Y]] F=\sum a_{(\alpha,\beta)}X^{\alpha}Y^{\beta}\in A[\![X^{*},Y]\!]. We define inf S = ( a, b) = ( a 1, …, a m, b 1, …, b n) \inf S=(a,b)=(a_{1},\dots,a_{m},b_{1},\dots,b_{n}), where a i:= inf ( Π X i ​ ( S)) a_{i}:=\inf(\Pi_{X_{i}}(S)) for i = 1, …, m i=1,\dots,m and b i:= min ⁡ ( Π Y i ​ ( S)) b_{i}:=\min(\Pi_{Y_{i}}(S)) for i = 1, …, n i=1,\dots,n, and we put

 | F S:= ∑ ( α, β) ∈ S a ( α, β) ​ X α − a ​ Y β − b, an element of ​ A ​ [[X ∗, Y]]. F_{S}:=\sum_{(\alpha,\beta)\in S}a_{(\alpha,\beta)}X^{\alpha-a}Y^{\beta-b},\quad\text{an element of }A[\![X^{*},Y]\!]. |  |

For γ ∈ [0, ∞) m × ℕ n \gamma\in[0,\infty)^{m}\times\mathbb{N}^{n}, we write F γ F_{\gamma} in place of F { α: α ≥ γ } F_{\{\alpha:\ \alpha\geq\gamma\}}.

###### Remark.

Let F, G ∈ A ⁡ [[X ∗, Y]] F,G\in A[\![X^{*},Y]\!] and γ ∈ [0, ∞) m × ℕ n \gamma\in[0,\infty)^{m}\times\mathbb{N}^{n}. Then ( F + G) γ = F γ + G γ (F+G)_{\gamma}=F_{\gamma}+G_{\gamma}.

In the remainder of this section, we study how the operation F ↦ F γ F\mapsto F_{\gamma} behaves with respect to various other operations on natural power series.

### Differentiation

Let F = ∑ a ( α, β) ​ X α ​ Y β ∈ A ⁡ [[X ∗, Y]] F=\sum a_{(\alpha,\beta)}X^{\alpha}Y^{\beta}\in A[\![X^{*},Y]\!]. For β ∈ ℕ n \beta\in\mathbb{N}^{n} and j = 1, …, n j=1,\dots,n, we put β j:= ( β 1, …, β j − 1, β j − 1, β j + 1, …, β n) \beta^{j}:=(\beta_{1},\dots,\beta_{j-1},\beta_{j}-1,\beta_{j+1},\dots,\beta_{n}). We define

 | ∂ i F:= ∑ α i ⋅ a ( α, β) ​ X α ​ Y β for ​ i = 1, …, m, \partial_{i}F:=\sum\alpha_{i}\cdot a_{(\alpha,\beta)}X^{\alpha}Y^{\beta}\quad\text{for }i=1,\dots,m, |  |

and

 | ∂ F ∂ Y j:= ∑ β j ⋅ a ( α, β) ​ X α ​ Y β j for ​ j = 1, …, n. \frac{\partial F}{\partial Y_{j}}:=\sum\beta_{j}\cdot a_{(\alpha,\beta)}X^{\alpha}Y^{\beta^{j}}\quad\text{for }j=1,\dots,n. |  |

Note that each ∂ i F \partial_{i}F and each ∂ F / ∂ Y j \partial F/\partial Y_{j} belongs to A ⁡ [[X ∗, Y]] A[\![X^{*},Y]\!]. Since each ∂ i \partial_{i} is a derivation on A ⁡ [[X ∗, Y]] A[\![X^{*},Y]\!], we obtain:

###### Lemma 1.3.

Let F ∈ A ⁡ [[X ∗, Y]] F\in A[\![X^{*},Y]\!] and γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}. Then:

1. (1)

( ∂ F / ∂ Y j) ( γ, 0) = ∂ ( F ( γ, 0)) / ∂ Y j (\partial F/\partial Y_{j})_{(\gamma,0)}=\partial(F_{(\gamma,0)})/\partial Y_{j} for each j = 1, …, n j=1,\dots,n.

2. (2)

( ∂ i F) ( γ, 0) = γ i ⋅ F ( γ, 0) + ∂ i ( F ( γ, 0)) (\partial_{i}F)_{(\gamma,0)}=\gamma_{i}\cdot F_{(\gamma,0)}+\partial_{i}(F_{(\gamma,0)}) for each i = 1, …, m i=1,\dots,m; in particular, if γ i = 0 \gamma_{i}=0, then ( ∂ i F) ( γ, 0) = ∂ i ( F ( γ, 0)) (\partial_{i}F)_{(\gamma,0)}=\partial_{i}(F_{(\gamma,0)}).

###### Proof.

Parts (1) straightforward. Since X γ ⋅ G γ X^{\gamma}\cdot G_{\gamma} is just the truncation of G G at γ \gamma for any G ∈ A ⁡ [[X ∗]] G\in A[\![X^{*}]\!], we have X γ ⋅ ( ∂ i F) ( γ, 0) = ∂ i ( X γ ⋅ F ( γ, 0)) X^{\gamma}\cdot(\partial_{i}F)_{(\gamma,0)}=\partial_{i}\left(X^{\gamma}\cdot F_{(\gamma,0)}\right). Part (2) follows from the latter, because ∂ i \partial_{i} is a derivation. ∎

Before continuing with the behavior of the operation F ↦ F γ F\mapsto F_{\gamma}, we make some crucial observations.

### Representation

Let I ⊂ { 1, …, m } I\subset\{1,\dots,m\}. Below we write X I:= ( X i) i ∈ I X_{I}:=(X_{i})_{i\in I}, and if x ∈ ℝ m x\in\mathbb{R}^{m} we write x I:= ( x i) i ∈ I x_{I}:=(x_{i})_{i\in I}. We let Π I: ℝ m + n ⟶ ℝ | I | \Pi_{I}:\mathbb{R}^{m+n}\longrightarrow\mathbb{R}^{|I|} be the projection defined by Π I ​ ( x, y):= x I \Pi_{I}(x,y):=x_{I}. We write I ¯:= { 1, …, m } ∖ I \overline{I}:=\{1,\dots,m\}\setminus I. For F ∈ A ⁡ [[X ∗, Y]] F\in A[\![X^{*},Y]\!] and γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, we put B γ, ∅:= { 0 } B_{\gamma,\emptyset}:=\{0\}, and for nonempty I ⊂ { 1, …, m } I\subset\{1,\dots,m\}, we put

 | B γ, I = B γ, I ​ ( F):= { α ∈ Π I ​ ( supp ⁡ F): α < γ I }. B_{\gamma,I}=B_{\gamma,I}(F):=\left\{\alpha\in\Pi_{I}(\supp F):\ \alpha<\gamma_{I}\right\}. |  |

###### Lemma 1.4.

Let F ∈ A ⁡ [[X ∗, Y]] F\in A[\![X^{*},Y]\!] and γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}. Then for each I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\}, the set B γ, I B_{\gamma,I} is finite, and for each α ∈ B γ, I \alpha\in B_{\gamma,I}, there is a unique F γ, I, α ∈ A ⁡ [[X I ¯ ∗, Y]] F_{\gamma,I,\alpha}\in A[\![X_{\overline{I}}^{*},Y]\!] such that

(1.1) |  | F ⁡ ( X, Y) = ∑ I ⊂ { 1, …, m } X I ¯ γ I ¯ ​ ( ∑ α ∈ B γ, I X I α ​ F γ, I, α ​ ( X I ¯, Y)). F(X,Y)=\sum_{I\subset\{1,\dots,m\}}X_{\overline{I}}^{\gamma_{\overline{I}}}\left(\sum_{\alpha\in B_{\gamma,I}}X_{I}^{\alpha}F_{\gamma,I,\alpha}(X_{\overline{I}},Y)\right). |  |

###### Proof.

For each ( α, β) ∈ supp ⁡ F (\alpha,\beta)\in\supp F, there is a unique I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\} such that for all i = 1, …, m i=1,\dots,m, we have α i < γ i \alpha_{i}<\gamma_{i} iff i ∈ I i\in I. Moreover, α I ∈ B γ, I \alpha_{I}\in B_{\gamma,I} and X α / ( X I ¯ γ I ¯ ​ X I α I) X^{\alpha}/\left(X_{\overline{I}}^{\gamma_{\overline{I}}}X_{I}^{\alpha_{I}}\right) is a monomial in X I ¯ X_{\overline{I}}. ∎

###### Definition 1.5.

Let F ∈ A ⁡ [[X ∗, Y]] F\in A[\![X^{*},Y]\!] and γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}. We call the right-hand side of equation ( 1.1) the γ \gamma -representation of F F. For each I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\}, we put

 | F γ, I ​ ( X, Y):= ∑ α ∈ B γ, I X I α ​ F γ, I, α ​ ( X I ¯, Y), F_{\gamma,I}(X,Y):=\sum_{\alpha\in B_{\gamma,I}}X_{I}^{\alpha}F_{\gamma,I,\alpha}(X_{\overline{I}},Y), |  |

so that F ⁡ ( X, Y) = ∑ I ⊆ { 1, …, m } X I ¯ γ I ¯ ​ F γ, I ​ ( X, Y) F(X,Y)=\sum_{I\subseteq\{1,\dots,m\}}X_{\overline{I}}^{\gamma_{\overline{I}}}F_{\gamma,I}(X,Y).

###### Remark 1.6.

In the situation of Definition 1.5, we have F ( γ, 0) = F γ, ∅, 0 F_{(\gamma,0)}=F_{\gamma,\emptyset,0}. More generally, for each γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, each I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\} and each α ∈ B γ, I \alpha\in B_{\gamma,I}, the series F γ, I, α ​ ( X I ¯, Y) F_{\gamma,I,\alpha}(X_{\overline{I}},Y), considered as an element of A ⁡ [[X ∗, Y]] A[\![X^{*},Y]\!], is equal to F S F_{S} for some S ⊆ [0, ∞) m × ℕ n S\subseteq[0,\infty)^{m}\times\mathbb{N}^{n} of the following form:

###### Definition 1.7.

Recall that a box in ℝ k \mathbb{R}^{k} is a set of the form B = { α ∈ ℝ k: a i ∗ i, 1 α i ∗ i, 2 b i for each i } B=\left\{\alpha\in\mathbb{R}^{k}:\ a_{i}\ast_{i,1}\alpha_{i}\ast_{i,2}b_{i}\text{ for each }i\right\}, where a, b ∈ ( ℝ ∪ { ∞ }) k a,b\in(\mathbb{R}\cup\{\infty\})^{k} and ∗ i, 1, ∗ i, 2 ∈ { <, ≤ } \ast_{i,1},\ast_{i,2}\in\{<,\leq\}. A set E ⊆ ℝ k E\subseteq\mathbb{R}^{k} is elementary if E E is a finite Boolean combination of boxes.

###### Remark 1.8.

If B ⊆ [0, ∞) k B\subseteq[0,\infty)^{k} is a box, then [0, ∞) k ∖ B [0,\infty)^{k}\setminus B is a finite union of pairwise disjoint boxes; also, any finite intersection of boxes is a box. Therefore, every elementary set is a finite union of pairwise disjoint boxes.

###### Example 1.9.

1. (1)

For each i ∈ { 1, …, k } i\in\{1,\dots,k\} and every a > 0 a>0, the set { α ∈ [0, ∞) k: α i = a } \{\alpha\in[0,\infty)^{k}:\alpha_{i}=a\} is elementary.

2. (2)

For all a 1, …, a k, b ≥ 0 a_{1},\dots,a_{k},b\geq 0 and every natural set S ⊆ [0, ∞) k S\subseteq[0,\infty)^{k}, there is an elementary set E ⊆ ℝ k E\subseteq\mathbb{R}^{k} such that

 | S ∩ { α ∈ [0, ∞) k: ∑ i = 1 k a i ⋅ α i ≥ b } = S ∩ E. S\cap\left\{\alpha\in[0,\infty)^{k}:\sum_{i=1}^{k}a_{i}\cdot\alpha_{i}\geq b\right\}=S\cap E. |  |

Intersections of natural sets and boxes can be further simplified:

###### Lemma 1.10.

Let B ⊆ [0, ∞) k B\subseteq[0,\infty)^{k} be a box and S ⊆ [0, ∞) k S\subseteq[0,\infty)^{k} be a natural set. Then there exist γ, δ 1, …, δ k ∈ [0, ∞) k \gamma,\delta^{1},\dots,\delta^{k}\in[0,\infty)^{k} such that γ ≤ δ j \gamma\leq\delta^{j} for each j j and S ∩ B = S ∩ { α ≥ γ } ∖ ⋃ j = 1 k S ∩ { α ≥ δ j } S\cap B=S\cap\{\alpha\geq\gamma\}\setminus\bigcup_{j=1}^{k}S\cap\{\alpha\geq\delta^{j}\}.

###### Proof.

Say B = { α ∈ ℝ k: a i ∗ i, 1 α i ∗ i, 2 b i for each i } B=\left\{\alpha\in\mathbb{R}^{k}:\ a_{i}\ast_{i,1}\alpha_{i}\ast_{i,2}b_{i}\text{ for each }i\right\}, where a, b ∈ ( ℝ ∪ { ∞ }) k a,b\in(\mathbb{R}\cup\{\infty\})^{k} and ∗ i, 1, ∗ i, 2 ∈ { <, ≤ } \ast_{i,1},\ast_{i,2}\in\{<,\leq\}. For each i ∈ { 1, …, k } i\in\{1,\dots,k\}, we define γ i:= min ⁡ { r ∈ Π X i ​ ( S): a i ∗ i, 1 r } \gamma_{i}:=\min\left\{r\in\Pi_{X_{i}}(S):a_{i}\ast_{i,1}r\right\} and δ i:= max ⁡ { r ∈ Π X i ​ ( S): r ∗ i, 2 b i } \delta_{i}:=\max\left\{r\in\Pi_{X_{i}}(S):r\ast_{i,2}b_{i}\right\}. Then S ∩ B = S ∩ { γ ≤ α ≤ δ } S\cap B=S\cap\left\{\gamma\leq\alpha\leq\delta\right\}, so the lemma follows with δ j \delta^{j} defined by δ i j:= γ i \delta^{j}_{i}:=\gamma_{i} if i ≠ j i\neq j and δ j j:= min ⁡ { r ∈ Π X j ​ ( S): r > δ j } \delta^{j}_{j}:=\min\{r\in\Pi_{X_{j}}(S):\ r>\delta_{j}\}. ∎

We now return to the study of the operation F ↦ F γ F\mapsto F_{\gamma}. Since the observations below are rather technical and not clearly motivated at this point, the reader may want to skip the rest of this section and come back to it later as needed (while reading Section 5, say).

### Blow-up substitutions

Let i, j ∈ { 1, …, m } i,j\in\{1,\dots,m\} be such that i ≠ j i\neq j, and let ρ > 0 \rho>0 and λ ≥ 0 \lambda\geq 0. Using the binomial expansion

 | ( λ + X j) β:= ∑ p ∈ ℕ ( β p) ​ λ β − p ​ X j p if ​ λ > 0 ​ and ​ β ≥ 0, (\lambda+X_{j})^{\beta}:=\sum_{p\in\mathbb{N}}\begin{pmatrix}\beta\\ p\end{pmatrix}\lambda^{\beta-p}X_{j}^{p}\quad\text{if }\lambda>0\text{ and }\beta\geq 0, |  |

we let 𝐁 i ​ j ρ, λ: A ⁡ [[X ∗]] ⟶ A ⁡ [[X ∗]] \mathbf{B}^{\rho,\lambda}_{ij}:A[\![X^{*}]\!]\longrightarrow A[\![X^{*}]\!] be the unique A A -algebra homomorphism satisfying

 | 𝐁 i ​ j ρ, λ ​ ( X k) = { X k if ​ k ≠ i, X j ρ ​ ( λ + X i) if ​ k = i. \mathbf{B}^{\rho,\lambda}_{ij}(X_{k})=\begin{cases}X_{k}&\text{if }k\neq i,\\ X_{j}^{\rho}(\lambda+X_{i})&\text{if }k=i.\end{cases} |  |

The homomorphism 𝐁 i ​ j ρ, λ \mathbf{B}^{\rho,\lambda}_{ij} is called a blow-up substitution; we call 𝐁 i ​ j ρ, 0 \mathbf{B}^{\rho,0}_{ij} singular, and if λ > 0 \lambda>0, we call 𝐁 i ​ j ρ, λ \mathbf{B}^{\rho,\lambda}_{ij} regular. We shall often write 𝐁 i ​ j ρ, λ ​ F \mathbf{B}^{\rho,\lambda}_{ij}F in place of 𝐁 i ​ j ρ, λ ​ ( F) \mathbf{B}^{\rho,\lambda}_{ij}(F), for F ∈ A ⁡ [[X ∗]] F\in A[\![X^{*}]\!].

###### Remark 1.11.

The substitution 𝐁 i ​ j ρ, 0 \mathbf{B}^{\rho,0}_{ij} is the A A -algebra homomorphism s i ​ j ρ s^{\rho}_{ij} defined in Section 4.13 of [3].

###### Proposition 1.12.

Let F ∈ A ⁡ [[X ∗]] F\in A[\![X^{*}]\!] and put X ′:= ( X 1, …, X m − 1) X^{\prime}:=(X_{1},\dots,X_{m-1}).

1. (1)

For λ > 0 \lambda>0, we have 𝐁 m, m − 1 ρ, λ ​ F ∈ A ⁡ [[( X ′) ∗, X m]] \mathbf{B}^{\rho,\lambda}_{m,m-1}F\in A[\![(X^{\prime})^{*},X_{m}]\!].

2. (2)

Let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, and assume that γ m = 0 \gamma_{m}=0 if λ > 0 \lambda>0. Then there are α 1, …, α k ∈ [0, ∞) m \alpha_{1},\dots,\alpha_{k}\in[0,\infty)^{m} and elementary sets E 1, …, E k ⊆ [0, ∞) m E_{1},\dots,E_{k}\subseteq[0,\infty)^{m} such that

 | ( 𝐁 m, m − 1 ρ, λ ​ F) γ = ∑ l = 1 k X α l ⋅ 𝐁 m, m − 1 ρ, λ ​ F E l. \left(\mathbf{B}^{\rho,\lambda}_{m,m-1}F\right)_{\gamma}=\sum_{l=1}^{k}X^{\alpha_{l}}\cdot\mathbf{B}^{\rho,\lambda}_{m,m-1}F_{E_{l}}. |  |

###### Proof.

Part (1) follows from the binomial expansion. Next, for k = 1, …, m k=1,\dots,m, we put

 | δ k:= { γ k if ​ k ≠ m, max ⁡ { γ m, γ m − 1 ρ } if ​ k = m, \delta_{k}:=\begin{cases}\gamma_{k}&\text{if }k\neq m,\\ \max\left\{\gamma_{m},\frac{\gamma_{m-1}}{\rho}\right\}&\text{if }k=m,\end{cases} |  |

and δ:= ( δ 1, …, δ m) \delta:=(\delta_{1},\dots,\delta_{m}). Let

 | F ⁡ ( X) = ∑ I ⊂ { 1, …, m } X I ¯ δ I ¯ ​ ( ∑ α ∈ B δ, I X I α ​ F δ, I, α ​ ( X I ¯)) F(X)=\sum_{I\subset\{1,\dots,m\}}X_{\overline{I}}^{\delta_{\overline{I}}}\left(\sum_{\alpha\in B_{\delta,I}}X_{I}^{\alpha}F_{\delta,I,\alpha}(X_{\overline{I}})\right) |  |

be the δ \delta -representation of F F. Put B δ, I ′:= B δ, I B^{\prime}_{\delta,I}:=B_{\delta,I} if I = ∅ I=\emptyset or I = { m − 1 } I=\{m-1\}, B δ, { m } ′:= { α ∈ B δ, I: α m ≥ γ m } B^{\prime}_{\delta,\{m\}}:=\left\{\alpha\in B_{\delta,I}:\ \alpha_{m}\geq\gamma_{m}\right\} and

 | B δ, { m − 1, m } ′:= { α ∈ B δ, I: α m ≥ γ m, α m − 1 + ρ α m ≥ γ m − 1 }. B^{\prime}_{\delta,\{m-1,m\}}:=\left\{\alpha\in B_{\delta,I}:\ \alpha_{m}\geq\gamma_{m},\,\alpha_{m-1}+\rho\alpha_{m}\geq\gamma_{m-1}\right\}. |  |

Then by the hypothesis on γ \gamma,

 | X γ ⋅ ( 𝐁 m, m − 1 ρ, λ ​ F ​ ( X)) γ = ∑ I ⊆ { m − 1, m } ∑ α ∈ B δ, I ′ 𝐁 m, m − 1 ρ, λ ​ ( X I ¯ δ I ¯ ​ X I α) ⋅ 𝐁 m, m − 1 ρ, λ ​ ( F δ, I, α ​ ( X I ¯)). X^{\gamma}\cdot\left(\mathbf{B}^{\rho,\lambda}_{m,m-1}F(X)\right)_{\gamma}\\ =\sum_{I\subseteq\{m-1,m\}}\sum_{\alpha\in B^{\prime}_{\delta,I}}\mathbf{B}^{\rho,\lambda}_{m,m-1}\left(X_{\overline{I}}^{\delta_{\overline{I}}}X_{I}^{\alpha}\right)\cdot\mathbf{B}^{\rho,\lambda}_{m,m-1}(F_{\delta,I,\alpha}(X_{\overline{I}})). |  |

Since each term 𝐁 m, m − 1 ρ, λ ​ ( X I ¯ δ I ¯ ​ X I α) \mathbf{B}^{\rho,\lambda}_{m,m-1}\left(X_{\overline{I}}^{\delta_{\overline{I}}}X_{I}^{\alpha}\right) on the right-hand side is divisible by X γ X^{\gamma}, part (2) follows. ∎

### Composition

Let F ∈ A ⁡ [[X ∗, Y]] F\in A[\![X^{*},Y]\!]. For the next lemma, we also let 𝐪 = ( 𝐪 1, …, 𝐪 n) ∈ ℕ n \mathbf{q}=(\mathbf{q}_{1},\dots,\mathbf{q}_{n})\in\mathbb{N}^{n} and put 𝐤:= | 𝐪 | \mathbf{k}:=|\mathbf{q}|. We let Z = ( Z 1, …, Z 𝐤) Z=(Z_{1},\dots,Z_{\mathbf{k}}) be a tuple of indeterminates and define

 | F 𝐪 ​ ( X, Z):= F ⁡ ( X, Z 1 + ⋯ + Z 𝐪 1, …, Z 𝐪 1 + ⋯ + 𝐪 n − 1 + 1 + ⋯ + Z 𝐤). F_{\mathbf{q}}(X,Z):=F\left(X,Z_{1}+\cdots+Z_{\mathbf{q}_{1}},\dots,Z_{\mathbf{q}_{1}+\cdots+\mathbf{q}_{n-1}+1}+\cdots+Z_{\mathbf{k}}\right). |  |

Note that F 𝐪 ∈ A ⁡ [[X ∗, Z]] F_{\mathbf{q}}\in A[\![X^{*},Z]\!].

###### Proposition 1.13.

Let G = ( G 1, …, G n) ∈ ( A ⁡ [[X ∗, Y]]) n G=(G_{1},\dots,G_{n})\in(A[\![X^{*},Y]\!])^{n} be such that G ⁡ ( 0) = 0 G(0)=0. Then the series F ⁡ ( X, G ⁡ ( X, Y)) F(X,G(X,Y)) belongs to A ⁡ [[X ∗, Y]] A[\![X^{*},Y]\!], and for each γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, there are

1. (i)

a p ∈ ℕ p\in\mathbb{N} and a tuple 𝐪 ∈ ℕ n \mathbf{q}\in\mathbb{N}^{n} and, with 𝐤:= | 𝐪 | \mathbf{k}:=|\mathbf{q}|,

2. (ii)

elementary E 1, …, E p ⊆ [0, ∞) m × ℕ 𝐤 E_{1},\dots,E_{p}\subseteq[0,\infty)^{m}\times\mathbb{N}^{\mathbf{k}} and B i, j ⊆ [0, ∞) m × ℕ n B_{i,j}\subseteq[0,\infty)^{m}\times\mathbb{N}^{n} for each pair ( i, j) (i,j) satisfying i ∈ { 1, …, n } i\in\{1,\dots,n\} and j ∈ { 1, …, 𝐪 i } j\in\{1,\dots,\mathbf{q}_{i}\},

such that, with G B:= ( ( G 1) B 1, 1, …, ( G 1) B 1, 𝐪 1, ( G 2) B 2, 1, …, ( G n) B n, 𝐪 n) G_{B}:=((G_{1})_{B_{1,1}},\dots,(G_{1})_{B_{1,\mathbf{q}_{1}}},(G_{2})_{B_{2,1}},\dots,(G_{n})_{B_{n,\mathbf{q}_{n}}}), we have G B ​ ( 0) = 0 G_{B}(0)=0, each term ( X, G B ​ ( X, Y)) inf E j (X,G_{B}(X,Y))^{\inf E_{j}} is divisible by X γ X^{\gamma} in 𝔸 ⁡ [[X ∗, Y]] \mathbb{A}[\![X^{*},Y]\!] and

 | F ​ ( X, G ⁡ ( X, Y)) ( γ, 0) = ∑ j = 1 p ( X, G B ​ ( X, Y)) inf E j X γ ⋅ ( F 𝐪) E j ​ ( X, G B ​ ( X, Y)). F(X,G(X,Y))_{(\gamma,0)}=\sum_{j=1}^{p}\frac{(X,G_{B}(X,Y))^{\inf E_{j}}}{X^{\gamma}}\cdot(F_{\mathbf{q}})_{E_{j}}(X,G_{B}(X,Y)). |  |

###### Proof.

It is standard to check that F ⁡ ( Y, G ⁡ ( X, Y)) ∈ A ⁡ [[X ∗, Y]] F(Y,G(X,Y))\in A[\![X^{*},Y]\!]; we leave the details to the reader. Let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, and for each j ∈ { 1, …, n } j\in\{1,\dots,n\}, we let

 | G j = ∑ I ⊆ { 1, …, m } X I ¯ γ I ¯ ​ ( ∑ α ∈ B I ​ ( G j) X I α ⋅ ( G j) I, α ​ ( X I ¯, Y)) G_{j}=\sum_{I\subseteq\{1,\dots,m\}}X_{\overline{I}}^{\gamma_{\overline{I}}}\left(\sum_{\alpha\in B_{I}(G_{j})}X_{I}^{\alpha}\cdot(G_{j})_{I,\alpha}(X_{\overline{I}},Y)\right) |  |

be the γ \gamma -representation of G j G_{j}. (We omit the subscript γ \gamma in these notations for the duration of this proof.) We let 𝒥 \mathcal{J} be the set of all triples ( j, I, α) (j,I,\alpha) such that j ∈ { 1, …, n } j\in\{1,\dots,n\}, I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\} and α ∈ B I ​ ( G j) \alpha\in B_{I}(G_{j}), and we put κ:= | 𝒥 | \kappa:=|\mathcal{J}| and fix a bijection σ: { 1, …, κ } ⟶ 𝒥 \sigma:\{1,\dots,\kappa\}\longrightarrow\mathcal{J}. Below, we write σ ⁡ ( λ) = ( j ⁡ ( λ), I ⁡ ( λ), α ⁡ ( λ)) \sigma(\lambda)=(j(\lambda),I(\lambda),\alpha(\lambda)) for λ = 1, …, κ \lambda=1,\dots,\kappa; without loss of generality, we may assume that j ⁡ ( λ) ≤ j ⁡ ( λ ′) j(\lambda)\leq j(\lambda^{\prime}) whenever λ ≤ λ ′ \lambda\leq\lambda^{\prime}.

For each λ = 1, …, κ \lambda=1,\dots,\kappa, we let Z λ Z_{\lambda} be a new indeterminate and put

 | G λ ​ ( X, Y):= X I ¯ γ I ¯ ​ X I α ⋅ ( G j) I, α ​ ( X I ¯, Y) G_{\lambda}(X,Y):=X_{\overline{I}}^{\gamma_{\overline{I}}}X_{I}^{\alpha}\cdot(G_{j})_{I,\alpha}(X_{\overline{I}},Y) |  |

with ( j, I, α) = ( j ⁡ ( λ), I ⁡ ( λ), α ⁡ ( λ)) (j,I,\alpha)=(j(\lambda),I(\lambda),\alpha(\lambda)). We write G B:= ( G 1, …, G κ) G_{B}:=(G_{1},\dots,G_{\kappa}); note that G B ​ ( 0) = 0 G_{B}(0)=0. We also put

 | H ⁡ ( X, Z):= F ⁡ ( X, ∑ j ⁡ ( λ) = 1 Z λ, …, ∑ j ⁡ ( λ) = n Z λ), H(X,Z):=F\left(X,\sum_{j(\lambda)=1}Z_{\lambda}\,,\dots,\sum_{j(\lambda)=n}Z_{\lambda}\right), |  |

and we write H ⁡ ( X, Z) = ∑ c μ, ν ​ X μ ​ Z ν H(X,Z)=\sum c_{\mu,\nu}X^{\mu}Z^{\nu}, where μ \mu ranges over [0, ∞) m [0,\infty)^{m} and ν \nu ranges over ℕ κ \mathbb{N}^{\kappa}. Note that F ⁡ ( X, G ⁡ ( X, Y)) = H ⁡ ( X, G B ​ ( X, Y)) F(X,G(X,Y))=H(X,G_{B}(X,Y)) and H = F 𝐪 H=F_{\mathbf{q}} for some 𝐪 ∈ ℕ n \mathbf{q}\in\mathbb{N}^{n} with | 𝐪 | = κ |\mathbf{q}|=\kappa.

For Q ⊆ { 1, …, κ } Q\subseteq\{1,\dots,\kappa\}, we put I Q:= ⋂ λ ∈ Q I ⁡ ( λ) I_{Q}:=\bigcap_{\lambda\in Q}I(\lambda). Let μ ∈ [0, ∞) m \mu\in[0,\infty)^{m} and ν ∈ ℕ κ \nu\in\mathbb{N}^{\kappa}, and put Q ⁡ ( ν):= { λ: ν λ ≠ 0 } Q(\nu):=\left\{\lambda:\ \nu_{\lambda}\neq 0\right\}. Then

(1.2) |  | X γ ⋅ ( X μ ​ G B ​ ( X, Y) ν) ( γ, 0) = { X μ ​ G B ​ ( X, Y) ν if ​ μ i + ∑ λ = 1 κ ν λ ⋅ α ​ ( λ) i ≥ γ i ​ for each ​ i ∈ I Q ⁡ ( ν), 0 otherwise. X^{\gamma}\cdot\left(X^{\mu}G_{B}(X,Y)^{\nu}\right)_{(\gamma,0)}=\\ \begin{cases}X^{\mu}G_{B}(X,Y)^{\nu}&\text{if }\mu_{i}+\sum_{\lambda=1}^{\kappa}\nu_{\lambda}\cdot\alpha(\lambda)_{i}\geq\gamma_{i}\text{ for each }i\in I_{Q(\nu)},\\ 0&\text{otherwise.}\end{cases} |  |

Therefore, for each Q ⊆ { 1, …, κ } Q\subseteq\{1,\dots,\kappa\}, we let S Q ⊆ [0, ∞) m × ℕ k S_{Q}\subseteq[0,\infty)^{m}\times\mathbb{N}^{k} be the set defined by

 | S Q:= { ( μ, ν) ∈ supp ( H): ν λ = 0 iff λ ∉ Q, μ i + ∑ λ ∈ Q ν λ ⋅ α ( λ) i ≥ γ i for each i ∈ I Q }. S_{Q}:=\Big\{(\mu,\nu)\in\supp(H):\ \nu_{\lambda}=0\text{ iff }\lambda\notin Q,\\ \quad\mu_{i}+\sum_{\lambda\in Q}\nu_{\lambda}\cdot\alpha(\lambda)_{i}\geq\gamma_{i}\text{ for each }i\in I_{Q}\Big\}. |  |

S Q S_{Q} is in turn the disjoint union of the following sets: for each map η: I Q ⟶ Q \eta:I_{Q}\longrightarrow Q, we define

 | S Q, η:= { ( μ, ν) ∈ S Q: μ i + ∑ λ ∈ Q, λ < η ⁡ ( i) ν λ ⋅ α ( λ) i < γ i and μ i + ∑ λ ∈ Q, λ ≤ η ⁡ ( i) ν λ ⋅ α ( λ) i ≥ γ i for each i ∈ I Q }. S_{Q,\eta}:=\Big\{(\mu,\nu)\in S_{Q}:\ \mu_{i}+\sum_{\lambda\in Q,\,\lambda<\eta(i)}\nu_{\lambda}\cdot\alpha(\lambda)_{i}<\gamma_{i}\text{ and }\\ \mu_{i}+\sum_{\lambda\in Q,\,\lambda\leq\eta(i)}\nu_{\lambda}\cdot\alpha(\lambda)_{i}\geq\gamma_{i}\text{ for each }i\in I_{Q}\Big\}. |  |

Then S Q = S Q, 0 ∪ ⋃ η S Q, η S_{Q}=S_{Q,0}\cup\bigcup_{\eta}S_{Q,\eta}, where S Q, 0:= { ( μ, ν) ∈ S Q: μ I Q ≥ γ I Q } S_{Q,0}:=\left\{(\mu,\nu)\in S_{Q}:\ \mu_{I_{Q}}\geq\gamma_{I_{Q}}\right\}. Moreover for each η: I Q ⟶ Q \eta:I_{Q}\longrightarrow Q, we write max ⁡ η:= max i ∈ I Q ⁡ η ⁡ ( i) \max\eta:=\max_{i\in I_{Q}}\eta(i) and J η:= { λ < max η: α ( λ) i > 0 J_{\eta}:=\{\lambda<\max\eta:\ \alpha(\lambda)_{i}>0 for some i ∈ I Q } i\in I_{Q}\}. Then the set C Q, η:= { ( μ I Q, ν J η): ( μ, ν) ∈ S Q, η } C_{Q,\eta}:=\left\{(\mu_{I_{Q}},\nu_{J_{\eta}}):\ (\mu,\nu)\in S_{Q,\eta}\right\} is finite, and S Q, η S_{Q,\eta} is the disjoint union of the sets S Q, η ∩ E Q, η, β S_{Q,\eta}\cap E_{Q,\eta,\beta} as β \beta ranges over C Q, η C_{Q,\eta}, where

 | E Q, η, β:= { ( μ, ν): ( μ I Q, ν J η) = β, ν max ⁡ η ⋅ α ( max η) i ≥ γ i − μ i − ∑ λ ∈ Q, λ < max ⁡ η ν λ ⋅ α ( λ) i for each i ∈ I Q }. E_{Q,\eta,\beta}:=\Big\{(\mu,\nu):\ (\mu_{I_{Q}},\nu_{J_{\eta}})=\beta,\\ \nu_{\max\eta}\cdot\alpha(\max\eta)_{i}\geq\gamma_{i}-\mu_{i}-\sum_{\lambda\in Q,\,\lambda<\max\eta}\nu_{\lambda}\cdot\alpha(\lambda)_{i}\text{ for each }i\in I_{Q}\Big\}. |  |

By Example 1.9, each set E Q, η, β E_{Q,\eta,\beta} is elementary. It follows from ( 1.2) above that

 | X γ ⋅ F ​ ( X, G ⁡ ( X, Y)) ( γ, 0) = ∑ Q, η, β ( X, G B ​ ( X, Y)) inf E Q, η, β ⋅ H E Q, η, β ​ ( X, G B ​ ( X, Y)), X^{\gamma}\cdot F(X,G(X,Y))_{(\gamma,0)}=\\ \sum_{Q,\eta,\beta}(X,G_{B}(X,Y))^{\inf E_{Q,\eta,\beta}}\cdot H_{E_{Q,\eta,\beta}}(X,G_{B}(X,Y)), |  |

and it follows from the definition of each E Q, η, β E_{Q,\eta,\beta} that X γ X^{\gamma} divides the factor ( X, G B ​ ( X, Y)) inf E Q, η, β (X,G_{B}(X,Y))^{\inf E_{Q,\eta,\beta}} in 𝔸 ⁡ [[X ∗, Y]] \mathbb{A}[\![X^{*},Y]\!], as required. ∎

## 2. Natural asymptotic expansions

Throughout this paper, we denote by ‖ z ‖ \|z\| the Euclidean norm of z ∈ ℂ n z\in\mathbb{C}^{n}, and we put | z |:= z 1 + ⋯ + z n |z|:=z_{1}+\cdots+z_{n} for such z z. We let 𝐋 = { ( r, φ): r > 0, φ ∈ ℝ } \mathbf{L}=\left\{(r,\varphi):\ r>0,\,\varphi\in\mathbb{R}\right\} be the Riemann surface of the logarithm. We fix an arbitrary m ∈ ℕ m\in\mathbb{N} and write

 | x = ( x 1, …, x m) = ( ( r 1, φ 1), …, ( r m, φ m)) x=(x_{1},\dots,x_{m})=((r_{1},\varphi_{1}),\dots,(r_{m},\varphi_{m})) |  |

for elements of 𝐋 m \mathbf{L}^{m}. For such x x, we put ‖ x ‖:= ‖ ( r 1, …, r m) ‖ \|x\|:=\|(r_{1},\dots,r_{m})\|, arg ⁡ ( x):= ( φ 1, …, φ m) \arg(x):=(\varphi_{1},\dots,\varphi_{m}) and

 | log m ⁡ x:= ( log ⁡ r 1 + i ​ φ 1, …, log ⁡ r m + i ​ φ m) ∈ ℂ m; \log_{m}x:=(\log r_{1}+i\varphi_{1},\dots,\log r_{m}+i\varphi_{m})\in\mathbb{C}^{m}; |  |

we omit the subscript m m whenever it is clear from context. Note that log: 𝐋 m ⟶ ℂ m \log:\mathbf{L}^{m}\longrightarrow\mathbb{C}^{m} is an analytic isomorphism. Below, we let z = ( z 1, …, z m) z=(z_{1},\dots,z_{m}) range over ℂ m \mathbb{C}^{m}.

Recall that for an open set U ⊆ 𝐋 U\subseteq\mathbf{L}, a function f: U ⟶ ℂ f:U\longrightarrow\mathbb{C} is holomorphic if the function f ∘ log − 1: log ⁡ ( U) ⟶ ℂ f\circ\log^{-1}:\log(U)\longrightarrow\mathbb{C} is holomorphic. The set of holomorphic functions on U U is denoted by 𝒪 ⁡ ( U) \mathcal{O}(U).

###### Definition 2.1.

Let U ⊆ 𝐋 m U\subseteq\mathbf{L}^{m} be open. For f ∈ 𝒪 ⁡ ( U) f\in\mathcal{O}(U) and i ∈ { 1, …, m } i\in\{1,\dots,m\}, we define ∂ i f: U ⟶ ℂ \partial_{i}f:U\longrightarrow\mathbb{C} by

 | ∂ i f ⁡ ( x):= ∂ ( f ∘ log − 1) ∂ z i ​ ( log ⁡ x). \partial_{i}f(x):=\frac{\partial(f\circ\log^{-1})}{\partial z_{i}}(\log x). |  |

Note that ∂ i f ∈ 𝒪 ⁡ ( U) \partial_{i}f\in\mathcal{O}(U).

###### Example 2.2.

Let α = ( α 1, …, α m) ∈ ℂ m \alpha=(\alpha_{1},\dots,\alpha_{m})\in\mathbb{C}^{m}. We put x α:= x 1 α 1 ⋯ x m α m x^{\alpha}:=x_{1}^{\alpha_{1}}\cdots x_{m}^{\alpha_{m}}, where x i α i:= exp ⁡ ( α i ​ log ⁡ ( x i)) x_{i}^{\alpha_{i}}:=\exp(\alpha_{i}\log(x_{i})) for each i i. The function ( ⋅) α: 𝐋 m ⟶ ℂ (\cdot)^{\alpha}:\mathbf{L}^{m}\longrightarrow\mathbb{C} is holomorphic and ∂ i ( x α) = α i ​ x α \partial_{i}(x^{\alpha})=\alpha_{i}x^{\alpha} for each i i.

For R > 0 R>0, we write B 𝐋 ​ ( R):= { x ∈ 𝐋: ‖ x ‖ < R } B_{\mathbf{L}}(R):=\left\{x\in\mathbf{L}:\ \|x\|<R\right\}.

###### Definition 2.3.

Let W ⊆ 𝐋 W\subseteq\mathbf{L}. The set W W is a standard quadratic domain if there are constants c, C > 0 c,C>0 such that

 | W = { ( r, φ) ∈ 𝐋: 0 < r < c ​ exp ⁡ ( − C ​ | φ |) }. W=\left\{(r,\varphi)\in\mathbf{L}:\ 0<r<c\exp\left(-C\sqrt{|\varphi|}\right)\right\}. |  |

Below, we put 𝐋 0:= 𝐋 ∪ { 0 } \mathbf{L}_{0}:=\mathbf{L}\cup\{0\}, and we extend the topology on 𝐋 \mathbf{L} to a topology on 𝐋 0 \mathbf{L}_{0} by taking the set B 𝐋 ​ ( R) ∪ { 0 } B_{\mathbf{L}}(R)\cup\{0\}, for R > 0 R>0, as a basis of open neighborhoods of 0 0 in 𝐋 0 \mathbf{L}_{0}. For a subset W W of 𝐋 m \mathbf{L}^{m}, we shall write cl 0 ⁡ ( W) \cl_{0}(W) for the topological closure of W W in 𝐋 0 m \mathbf{L}_{0}^{m}.

###### Remark.

Note that if W ⊆ 𝐋 W\subseteq\mathbf{L} is a standard quadratic domain, then W ∪ { 0 } W\cup\{0\} is not an open neighborhood of 0 0 in 𝐋 0 \mathbf{L}_{0}. In particular, int ⁡ ( cl 0 ⁡ ( W)) = W \ir(\cl_{0}(W))=W.

###### Definition 2.4.

A set W ⊆ 𝐋 W\subseteq\mathbf{L} is a quadratic domain if W W contains a standard quadratic domain and int ⁡ ( cl 0 ⁡ ( W)) = W \ir(\cl_{0}(W))=W.

Let U ⊆ 𝐋 m U\subseteq\mathbf{L}^{m} and k ≤ m k\leq m. We say that U U is k k -quadratic if

1. (i)

there is a quadratic domain W ⊆ 𝐋 W\subseteq\mathbf{L} and an R > 0 R>0 such that W k × B 𝐋 ​ ( R) m − k ⊆ U W^{k}\times B_{\mathbf{L}}(R)^{m-k}\subseteq U;

2. (ii)

0 ∉ int ⁡ ( cl 0 ⁡ ( Π X i ​ U)) 0\notin\ir(\cl_{0}(\Pi_{X_{i}}U)) for each i = 1, …, k i=1,\dots,k.

###### Remarks 2.5.

Let k ≤ m k\leq m.

1. (1)

Let R > 0 R>0 and W ⊆ 𝐋 W\subseteq\mathbf{L} be a quadratic domain such that W ⊆ B 𝐋 ​ ( R) W\subseteq B_{\mathbf{L}}(R). If l ≥ k l\geq k, then W l × B 𝐋 ​ ( R) m − l ⊆ W k × B 𝐋 ​ ( R) m − k W^{l}\times B_{\mathbf{L}}(R)^{m-l}\subseteq W^{k}\times B_{\mathbf{L}}(R)^{m-k}; therefore, every k k -quadratic domain in 𝐋 m \mathbf{L}^{m} contains an l l -quadratic domain.

2. (2)

Let U ⊆ 𝐋 m U\subseteq\mathbf{L}^{m} be a k k -quadratic domain, and let r ∈ ( 0, ∞) m r\in(0,\infty)^{m}. Then the set V:= log − 1 ⁡ ( log ⁡ ( U) − r) V:=\log^{-1}(\log(U)-r) is a k k -quadratic domain.

We now fix an m m -quadratic domain U ⊆ 𝐋 m U\subseteq\mathbf{L}^{m}.

###### Definition 2.6.

Let f ∈ 𝒪 ⁡ ( U) f\in\mathcal{O}(U) and F = ∑ a α ​ X α ∈ ℂ ⁡ [[X ∗]] F=\sum a_{\alpha}X^{\alpha}\in\mathbb{C}[\![X^{*}]\!]. We say that f f has asymptotic expansion F F on U U and write f ∼ U F f\sim_{U}F, if for each 𝐚 > 0 \mathbf{a}>0 there is an m m -quadratic domain U 𝐚 ⊆ U U_{\mathbf{a}}\subseteq U such that

 | f ⁡ ( x) − ∑ | α | ≤ 𝐚 a α ​ x α = o ⁡ ( ‖ x ‖ 𝐚) as ​ ‖ x ‖ → 0 ​ on ​ U 𝐚. f(x)-\sum_{|\alpha|\leq\mathbf{a}}a_{\alpha}x^{\alpha}=o\left(\|x\|^{\mathbf{a}}\right)\quad\text{as }\|x\|\to 0\text{ on }U_{\mathbf{a}}. |  |

Note that in this situation, F F is the unique series G ∈ ℂ ⁡ [[X ∗]] G\in\mathbb{C}[\![X^{*}]\!] with f ∼ U G f\sim_{U}G; we therefore also write T ​ f:= F Tf:=F, and we put f ⁡ ( 0):= lim ‖ x ‖ → 0, x ∈ U 𝐚 f ⁡ ( x) f(0):=\lim_{\|x\|\to 0,\,x\in U_{\mathbf{a}}}f(x) for any 𝐚 > 0 \mathbf{a}>0. We let 𝒜 ⁡ ( U) \mathcal{A}(U) be the set of all f ∈ 𝒪 ⁡ ( U) f\in\mathcal{O}(U) for which there is an F ∈ ℂ ⁡ [[X ∗]] F\in\mathbb{C}[\![X^{*}]\!] such that f ∼ U F f\sim_{U}F.

###### Remark 2.7.

1. (1)

If f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U) and n ≥ m n\geq m, then we consider f f as an holomorphic function f: U × 𝐋 n − m f:U\times\mathbf{L}^{n-m} in the obvious way; under this identification, we get 𝒜 ⁡ ( U) ⊆ 𝒜 ⁡ ( U × 𝐋 n − m) \mathcal{A}(U)\subseteq\mathcal{A}(U\times\mathbf{L}^{n-m}).

2. (2)

Let f ∈ 𝒪 ⁡ ( U) f\in\mathcal{O}(U) and V ⊆ U V\subseteq U. Then f | V ∈ 𝒜 ⁡ ( V) f|_{V}\in\mathcal{A}(V) if and only if f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U).

3. (3)

The set 𝒜 ⁡ ( U) \mathcal{A}(U) is a ℂ \mathbb{C} -algebra, and the map T: 𝒜 ⁡ ( U) ⟶ ℂ ⁡ [[X ∗]] T:\mathcal{A}(U)\longrightarrow\mathbb{C}[\![X^{*}]\!] given by T ⁡ ( f):= T ​ f T(f):=Tf is a ℂ \mathbb{C} -algebra homomorphism satisfying f ​ ( 0) = ( T ​ f) ​ ( 0) f(0)=(Tf)(0).

For R > 0 R>0, we put

 | ( 0, R) 𝐋:= { x ∈ 𝐋: ‖ x ‖ < R ​ and ​ arg ⁡ ( x) = 0 }. (0,R)_{\mathbf{L}}:=\left\{x\in\mathbf{L}:\ \|x\|<R\text{ and }\arg(x)=0\right\}. |  |

###### Proposition 2.8.

The map T: 𝒜 ⁡ ( U) ⟶ ℂ ⁡ [[X ∗]] T:\mathcal{A}(U)\longrightarrow\mathbb{C}[\![X^{*}]\!] is injective.

###### Proof.

Let f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U), and assume that f ∼ U 0 f\sim_{U}0; it suffices to show that f = 0 f=0. Let c, C > 0 c,C>0 and

 | W:= { ( r, φ) ∈ 𝐋: 0 < r < c ​ exp ⁡ ( − C ​ | φ |) } W:=\left\{(r,\varphi)\in\mathbf{L}:\ 0<r<c\exp\left(-C\sqrt{|\varphi|}\right)\right\} |  |

be such that W m ⊆ U W^{m}\subseteq U. For s = ( s 1, …, s m) ∈ ( 0, 1] m s=(s_{1},\dots,s_{m})\in(0,1]^{m}, we define f s: W ⟶ ℂ f_{s}:W\longrightarrow\mathbb{C} by f s ​ ( r, φ):= f ⁡ ( ( s 1 ​ r, φ), …, ( s m ​ r, φ)) f_{s}(r,\varphi):=f((s_{1}r,\varphi),\dots,(s_{m}r,\varphi)). Then f s ∈ 𝒪 ⁡ ( W) f_{s}\in\mathcal{O}(W), and our hypothesis implies that f s ∼ W 0 f_{s}\sim_{W}0. This means that

 | ‖ f s ∘ log − 1 ⁡ ( z) ‖ = o ⁡ ( e − n ​ Re ⁡ z) as ​ Re ⁡ z → − ∞ ​ in ​ log ⁡ ( W) \|f_{s}\circ\log^{-1}(z)\|=o(e^{-n\re z})\quad\text{as }\re z\to-\infty\text{ in }\log(W) |  |

for every n ∈ ℕ n\in\mathbb{N}; hence f s = 0 f_{s}=0 by Theorem 2 on p. 23 of [7]. In particular, f ⁡ ( ( s 1 ​ c, 0), …, ( s m ​ c, 0)) = 0 f((s_{1}c,0),\dots,(s_{m}c,0))=0 for all s ∈ ( 0, 1) m s\in(0,1)^{m}, that is, f | ( 0, c) 𝐋 m = 0 f|_{(0,c)_{\mathbf{L}}^{m}}=0. Therefore, the holomorphic map h:= f ∘ log − 1 h:=f\circ\log^{-1} vanishes on ( − ∞, log ⁡ c) m (-\infty,\log c)^{m}. Since log ⁡ ( U) ⊆ ℂ m \log(U)\subseteq\mathbb{C}^{m} is connected, it follows that h = 0 h=0 and hence that f = 0 f=0. ∎

###### Proposition 2.9.

Let f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U) and i ∈ { 1, …, m } i\in\{1,\dots,m\}. Then ∂ i f \partial_{i}f belongs to 𝒜 ⁡ ( U) \mathcal{A}(U) and satisfies T ⁡ ( ∂ i f) = ∂ i ( T ​ f) T(\partial_{i}f)=\partial_{i}(Tf).

###### Proof.

Let 𝐚 > 0 \mathbf{a}>0, and assume that U U is an m m -quadratic domain and ‖ f ⁡ ( x) ‖ = o ⁡ ( ‖ x ‖ 𝐚) \|f(x)\|=o(\|x\|^{\mathbf{a}}) as ‖ x ‖ → 0 \|x\|\to 0 with x ∈ U x\in U. By Remark 2.7 (2) and Example 2.2, it suffices to find an m m -quadratic domain V ⊆ U V\subseteq U such that ‖ ∂ i f ⁡ ( x) ‖ = o ⁡ ( ‖ x ‖ 𝐚) \|\partial_{i}f(x)\|=o(\|x\|^{\mathbf{a}}) as ‖ x ‖ → 0 \|x\|\to 0 with x ∈ V x\in V.

We claim that V:= log − 1 ⁡ ( log ⁡ ( U) − ( 1, …, 1)) V:=\log^{-1}(\log(U)-(1,\dots,1)) works; by Remark 2.5 (2), V V is an m m -quadratic domain contained in U U. To see the claim, for each r > 0 r>0, we put

 | M r:= max ⁡ { ‖ f ⁡ ( x) ‖: x ∈ U ​ and ​ ‖ x ‖ ≤ r } M_{r}:=\max\left\{\|f(x)\|:\ x\in U\text{ and }\|x\|\leq r\right\} |  |

and

 | N r:= max ⁡ { ‖ ∂ i f ⁡ ( x) ‖: x ∈ V ​ and ​ ‖ x ‖ ≤ r }. N_{r}:=\max\left\{\|\partial_{i}f(x)\|:\ x\in V\text{ and }\|x\|\leq r\right\}. |  |

By assumption, we have M r / r 𝐚 → 0 M_{r}/r^{\mathbf{a}}\to 0 as r → 0 r\to 0; we need to show that N r / r 𝐚 → 0 N_{r}/r^{\mathbf{a}}\to 0 as r → 0 r\to 0. To do so, it suffices to show that N r ≤ M r ⋅ e N_{r}\leq M_{r\cdot e} for each r > 0 r>0, where e:= exp ⁡ ( 1) e:=\exp(1). By the Cauchy estimates, we have for all x ∈ V x\in V with ‖ x ‖ ≤ r \|x\|\leq r that

 | ‖ ∂ i f ⁡ ( x) ‖ = ‖ ∂ ( f ∘ log − 1) ∂ z i ​ ( log ⁡ x) ‖ ≤ M r ⋅ e, \|\partial_{i}f(x)\|=\left\|\frac{\partial(f\circ\log^{-1})}{\partial z_{i}}(\log x)\right\|\leq M_{r\cdot e}, |  |

because M r ⋅ e M_{r\cdot e} is the maximum of all ‖ ( f ∘ log − 1) ​ ( z) ‖ \|(f\circ\log^{-1})(z)\| such that z ∈ log ⁡ ( U) z\in\log(U) and Re ⁡ z j ≤ log ⁡ r − 1 \re z_{j}\leq\log r-1 for each j j. This finishes the proof of the proposition. ∎

We now also fix a k ≤ m k\leq m.

###### Definition 2.10.

We let 𝒜 k m ​ ( U) \mathcal{A}^{m}_{k}(U) be the set of all f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U) such that T ​ f ∈ ℂ ⁡ [[X { 1, …, k } ∗, X { k + 1, …, m }]] Tf\in\mathbb{C}[\![X_{\{1,\dots,k\}}^{*},X_{\{k+1,\dots,m\}}]\!]. We also let π k m: 𝐋 0 m ⟶ 𝐋 0 k × ℂ m − k \pi^{m}_{k}:\mathbf{L}_{0}^{m}\longrightarrow\mathbf{L}_{0}^{k}\times\mathbb{C}^{m-k} be the map defined by π k m ​ ( x) = ( y 1, …, y m) \pi^{m}_{k}(x)=(y_{1},\dots,y_{m}), where

 | y i:= { x i if ​ i ≤ k, x i 1 if i > k and x i ≠ 0, 0 otherwise. y_{i}:=\begin{cases}x_{i}&\text{if }i\leq k,\\ x_{i}^{1}&\text{if }i>k\text{ and }x_{i}\neq 0,\\ 0&\text{otherwise.}\end{cases} |  |

We also denote by cl 0 \cl_{0} the topological closure in 𝐋 0 k × ℂ m − k \mathbf{L}_{0}^{k}\times\mathbb{C}^{m-k}. As usual, we shall omit the superscript m m if clear from context.

Finally, for each i = 1, …, m i=1,\dots,m, we let p i: 𝐋 m ⟶ 𝐋 m p_{i}:\mathbf{L}^{m}\longrightarrow\mathbf{L}^{m} be the map defined by p i ​ ( x):= y p_{i}(x):=y with y j:= x j y_{j}:=x_{j} if j ≠ i j\neq i, ‖ y i ‖:= ‖ x i ‖ \|y_{i}\|:=\|x_{i}\| and arg ⁡ ( y i):= arg ⁡ ( x i) + 2 ​ π \arg(y_{i}):=\arg(x_{i})+2\pi.

###### Proposition 2.11.

Let f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U). The following are equivalent:

1. (1)

f ∈ 𝒜 k ​ ( U) f\in\mathcal{A}_{k}(U).

2. (2)

There are a k k -quadratic domain V ⊆ 𝐋 m V\subseteq\mathbf{L}^{m} and a holomorphic f ♯: int ⁡ ( cl 0 ⁡ ( π k ​ ( V))) ⟶ ℂ f^{\sharp}:\ir(\cl_{0}(\pi_{k}(V)))\longrightarrow\mathbb{C} such that f ⁡ ( x) = f ♯ ​ ( π k ​ ( x)) f(x)=f^{\sharp}(\pi_{k}(x)) for all x ∈ U ∩ V x\in U\cap V.

3. (3)

For every i = k + 1, …, m i=k+1,\dots,m and every x ∈ U x\in U satisfying p i ​ ( x) ∈ U p_{i}(x)\in U, we have f ⁡ ( x) = f ⁡ ( p i ​ ( x)) f(x)=f(p_{i}(x)).

###### Proof.

(2) ⇒ \Rightarrow (3): straightforward, since U U is connected.

(3) ⇒ \Rightarrow (2): without loss of generality, we may assume that U = W m U=W^{m} for some quadratic domain W ⊆ 𝐋 W\subseteq\mathbf{L}. Let R > 0 R>0 be such that B ⁡ ( 0, R) ⊆ int ⁡ ( cl ⁡ ( π 0 1 ​ ( W))) B(0,R)\subseteq\ir(\cl(\pi^{1}_{0}(W))), and put V:= W k × B 𝐋 ​ ( R) m − k V:=W^{k}\times B_{\mathbf{L}}(R)^{m-k}. Then the assumption on f f and Riemann’s theorem on removable singularities imply that there is a holomorphic g: int ⁡ ( cl 0 ⁡ ( π k ​ ( V))) ⟶ ℂ g:\ir(\cl_{0}(\pi_{k}(V)))\longrightarrow\mathbb{C} such that f ⁡ ( x) = g ⁡ ( π k ​ ( x)) f(x)=g(\pi_{k}(x)) for all x ∈ U ∩ V x\in U\cap V, which proves (2).

(3) ⇒ \Rightarrow (1): Assume (3) and let i ∈ { k + 1, …, m } i\in\{k+1,\dots,m\}. Write T ​ f ​ ( X) = ∑ a α ​ X α Tf(X)=\sum a_{\alpha}X^{\alpha}, and let α ∈ [0, ∞) m \alpha\in[0,\infty)^{m} be such that α i ∉ ℕ \alpha_{i}\notin\mathbb{N}; we need to show that a α = 0 a_{\alpha}=0. Permuting coordinates if necessary, we may assume that i = m i=m. Let R > 0 R>0 be such that the set V:= ( 0, R) 𝐋 m ∪ p m ​ ( ( 0, R) 𝐋 m) V:=(0,R)_{\mathbf{L}}^{m}\cup p_{m}((0,R)_{\mathbf{L}}^{m}) is contained in U U.

Put 𝐚:= | α | > 0 \mathbf{a}:=|\alpha|>0, and define g: V ⟶ ℂ g:V\longrightarrow\mathbb{C} by g ⁡ ( x):= f ⁡ ( x) − ∑ | β | ≤ 𝐚 a β ​ x β g(x):=f(x)-\sum_{|\beta|\leq\mathbf{a}}a_{\beta}x^{\beta}. Since f ∈ 𝒜 ⁡ ( U) f\in\mathcal{A}(U), we have g ⁡ ( x) = o ⁡ ( ‖ x ‖ 𝐚) g(x)=o\left(\|x\|^{\mathbf{a}}\right) as ‖ z ‖ → 0 \|z\|\to 0 in V V; in particular, for s ∈ ( 0, R) s\in(0,R) and any t ∈ ( 0, 1) m t\in(0,1)^{m}, we have

(2.1) |  | g ⁡ ( s ​ t 1, …, s ​ t m) − g ⁡ ( p m ​ ( s ​ t 1, …, s ​ t m)) = o ⁡ ( s 𝐚) as ​ s → 0. g(st_{1},\dots,st_{m})-g(p_{m}(st_{1},\dots,st_{m}))=o(s^{\mathbf{a}})\quad\text{as }s\to 0. |  |

On the other hand,

 | g ⁡ ( s ​ t 1, …, s ​ t m) − g ⁡ ( p m ​ ( s ​ t 1, …, s ​ t m)) = ∑ | β | ≤ 𝐚 β m ∉ ℕ a β ​ ( e 2 ​ π ​ i ⋅ β m − 1) ​ t β ​ s | β |. g(st_{1},\dots,st_{m})-g(p_{m}(st_{1},\dots,st_{m}))=\sum_{\begin{subarray}{c}|\beta|\leq\mathbf{a}\\ \beta_{m}\notin\mathbb{N}\end{subarray}}a_{\beta}\left(e^{2\pi i\cdot\beta_{m}}-1\right)t^{\beta}s^{|\beta|}. |  |

It follows from ( 2.1) that ∑ | β | ≤ 𝐚 β m ∉ ℕ a β ​ ( e 2 ​ π ​ i ⋅ β m − 1) ​ t β = 0 \sum_{\begin{subarray}{c}|\beta|\leq\mathbf{a}\\ \beta_{m}\notin\mathbb{N}\end{subarray}}a_{\beta}\left(e^{2\pi i\cdot\beta_{m}}-1\right)t^{\beta}=0. Since t ∈ ( 0, 1) m t\in(0,1)^{m} was arbitrary, we obtain that a β = 0 a_{\beta}=0 for every β ∈ [0, ∞) m \beta\in[0,\infty)^{m} satisfying | β | ≤ 𝐚 |\beta|\leq\mathbf{a} and β m ∉ ℕ \beta_{m}\notin\mathbb{N}; in particular, a α = 0 a_{\alpha}=0.

(1) ⇒ \Rightarrow (3): assume that T ​ f ∈ ℂ ⁡ [[X { 1, …, k } ∗, X { k + 1, …, m }]] Tf\in\mathbb{C}[\![X_{\{1,\dots,k\}}^{*},X_{\{k+1,\dots,m\}}]\!], and let i ∈ { k + 1, …, m } i\in\{k+1,\dots,m\}. Then there is a quadratic domain V ⊆ U V\subseteq U such that p i ​ ( V) ⊆ U p_{i}(V)\subseteq U, and we define g: V ⟶ ℂ g:V\longrightarrow\mathbb{C} by g ⁡ ( x):= f ⁡ ( x) − f ⁡ ( p i ​ ( x)) g(x):=f(x)-f(p_{i}(x)). Then g ∈ 𝒪 ⁡ ( V) g\in\mathcal{O}(V), and since T ​ f ∈ ℂ ⁡ [[X { 1, …, k } ∗, X { k + 1, …, m }]] Tf\in\mathbb{C}[\![X_{\{1,\dots,k\}}^{*},X_{\{k+1,\dots,m\}}]\!], we have g ∼ V 0 g\sim_{V}0. Thus g = 0 g=0 by Proposition 2.8, which proves (3). ∎

Assume that U U is a k k -quadratic domain and let f ∈ 𝒜 k ​ ( U) f\in\mathcal{A}_{k}(U). Let V V and f ♯ f^{\sharp} be as in Proposition 2.11 (2); by analytic continuation, we may assume that U = V U=V. We extend f f to a function on π k − 1 ​ ( int ⁡ ( cl 0 ⁡ ( π k ​ ( U)))) \pi_{k}^{-1}(\ir(\cl_{0}(\pi_{k}(U)))) by putting f ⁡ ( x):= f ♯ ​ ( π k ​ ( x)) f(x):=f^{\sharp}(\pi_{k}(x)). For example, we let W ⊆ 𝐋 W\subseteq\mathbf{L} be a quadratic domain and R > 0 R>0 be such that W k × B 𝐋 ​ ( R) m − k ⊆ U W^{k}\times B_{\mathbf{L}}(R)^{m-k}\subseteq U. Then the value f ⁡ ( x ′, 0) f(x^{\prime},0) is well defined for all x ′ ∈ W k × B 𝐋 ​ ( R) m − k − 1 x^{\prime}\in W^{k}\times B_{\mathbf{L}}(R)^{m-k-1}, and we have:

###### Corollary 2.12.

The function g: W k × B 𝐋 ​ ( R) m − k − 1 ⟶ ℂ g:W^{k}\times B_{\mathbf{L}}(R)^{m-k-1}\longrightarrow\mathbb{C} defined by g ⁡ ( x ′):= f ⁡ ( x ′, 0) g(x^{\prime}):=f(x^{\prime},0) belongs to 𝒜 k m − 1 ​ ( W k × B 𝐋 ​ ( R) m − k − 1) \mathcal{A}_{k}^{m-1}(W^{k}\times B_{\mathbf{L}}(R)^{m-k-1}) and satisfies T ​ g ​ ( X ′) = T ​ f ​ ( X ′, 0) Tg(X^{\prime})=Tf(X^{\prime},0). ∎

Moreover, we let i ∈ { k + 1, …, m } i\in\{k+1,\dots,m\}. Then the partial derivative ∂ f ♯ / ∂ z i: π k ​ ( U) ⟶ ℂ \partial f^{\sharp}/\partial z_{i}:\pi_{k}(U)\longrightarrow\mathbb{C} is defined as usual; using this, we define the partial derivative ∂ f / ∂ x i: U ⟶ ℂ \partial f/\partial x_{i}:U\longrightarrow\mathbb{C} by

 | ∂ f ∂ x i ​ ( x):= ∂ f ♯ ∂ z i ​ ( π k ​ ( x)). \frac{\partial f}{\partial x_{i}}(x):=\frac{\partial f^{\sharp}}{\partial z_{i}}(\pi_{k}(x)). |  |

Using the Cauchy estimates (similarly as in the proof of Proposition 2.9) and Proposition 2.8, we obtain:

###### Corollary 2.13.

Assume that U U is a k k -quadratic domain, and let f ∈ 𝒜 k ​ ( U) f\in\mathcal{A}_{k}(U). Then for every i = k + 1, …, m i=k+1,\dots,m, the partial derivative ∂ f / ∂ x i \partial f/\partial x_{i} belongs to 𝒜 k ​ ( U) \mathcal{A}_{k}(U) and satisfies T ⁡ ( ∂ f / ∂ x i) = ∂ ( T ​ f) / ∂ X i T(\partial f/\partial x_{i})=\partial(Tf)/\partial X_{i}; in particular, x i ⋅ ( ∂ f / ∂ x i) ​ ( x) = ∂ i f ⁡ ( x) x_{i}\cdot(\partial f/\partial x_{i})(x)=\partial_{i}f(x) for all x ∈ U x\in U. ∎

Finally, we establish some criteria for membership in 𝒜 k ​ ( U) \mathcal{A}_{k}(U): we fix an l ∈ { k, …, m } l\in\{k,\dots,m\}. For x ∈ 𝐋 m x\in\mathbf{L}^{m} we write Y:= ( X 1, …, X l) Y:=(X_{1},\dots,X_{l}), y:= ( x 1, …, x l) y:=(x_{1},\dots,x_{l}), Z:= ( X l + 1, …, X m) Z:=(X_{l+1},\dots,X_{m}) and z:= ( x l + 1, …, x m) z:=(x_{l+1},\dots,x_{m}). We assume that U = W k × B 𝐋 ​ ( R) m − k U=W^{k}\times B_{\mathbf{L}}(R)^{m-k} for some quadratic domain W ⊆ 𝐋 W\subseteq\mathbf{L} and some R > 0 R>0, and we let f ∈ 𝒜 k ​ ( U) f\in\mathcal{A}_{k}(U). By Proposition 2.11, for each x = ( y, z) ∈ U x=(y,z)\in U we have a convergent power series representation

 | f ⁡ ( x) = ∑ p ∈ ℕ m − l a p ​ ( y) ​ z p. f(x)=\sum_{p\in\mathbb{N}^{m-l}}a_{p}(y)z^{p}. |  |

Writing T ​ f = ∑ p ∈ ℕ m − l α ∈ [0, ∞) k × ℕ l − k a p, α ⋅ Y α ​ Z p Tf=\sum_{\begin{subarray}{c}p\in\mathbb{N}^{m-l}\\ \alpha\in[0,\infty)^{k}\times\mathbb{N}^{l-k}\end{subarray}}a_{p,\alpha}\cdot Y^{\alpha}Z^{p}, we put

 | A p ( Y):= ∑ α ∈ [0, ∞) k × ℕ l − k a p, α ⋅ Y α, for each p ∈ ℕ m − l. A_{p}(Y):=\sum_{\alpha\in[0,\infty)^{k}\times\mathbb{N}^{l-k}}a_{p,\alpha}\cdot Y^{\alpha},\quad\text{for each }p\in\mathbb{N}^{m-l}. |  |

Shrinking U U if necessary, there is an M > 0 M>0 such that ‖ f ⁡ ( x) ‖ ≤ M \|f(x)\|\leq M for all x ∈ U x\in U. Finally, we put U ′:= W k × B 𝐋 ​ ( R) l − k U^{\prime}:=W^{k}\times B_{\mathbf{L}}(R)^{l-k}. Since a p ​ ( y) = 1 p! ⋅ ∂ p f / ∂ ( z) p ​ ( y, 0) a_{p}(y)=\frac{1}{p!}\cdot\partial^{p}f/\partial(z)^{p}(y,0) for all p ∈ ℕ m − l p\in\mathbb{N}^{m-l} and all y ∈ U ′ y\in U^{\prime}, we obtain from the Cauchy estimates and Corollaries 2.12 and 2.13:

###### Proposition 2.14.

For each p ∈ ℕ m − l p\in\mathbb{N}^{m-l}, the function a p: U ′ ⟶ ℂ a_{p}:U^{\prime}\longrightarrow\mathbb{C} belongs to 𝒜 k l ​ ( U ′) \mathcal{A}^{l}_{k}(U^{\prime}) and satisfies T ​ a p = A p Ta_{p}=A_{p} and ‖ a p ​ ( y) ‖ ≤ M / R | p | \|a_{p}(y)\|\leq M/R^{|p|} for all y ∈ U ′ y\in U^{\prime}. ∎

The following converse to Proposition 2.14 is our principal test for membership in 𝒜 k ​ ( U) \mathcal{A}_{k}(U):

###### Proposition 2.15.

Let S ⊆ [0, ∞) k × ℕ l − k S\subseteq[0,\infty)^{k}\times\mathbb{N}^{l-k} be natural, let A > 0 A>0, and for each p ∈ ℕ m − l p\in\mathbb{N}^{m-l} let b p ∈ 𝒜 k l ​ ( U ′) b_{p}\in\mathcal{A}^{l}_{k}(U^{\prime}) be such that

1. (i)

supp ⁡ ( T ​ b p) ⊆ S \supp(Tb_{p})\subseteq S;

2. (ii)

| | b p ( y) ∥ ≤ A / R | p | ||b_{p}(y)\|\leq A/R^{|p|} for all y ∈ U ′ y\in U^{\prime}.

Then the function g: U ⟶ ℂ g:U\longrightarrow\mathbb{C} defined by g ⁡ ( x):= ∑ p ∈ ℕ m − l b p ​ ( y) ⋅ z p g(x):=\sum_{p\in\mathbb{N}^{m-l}}b_{p}(y)\cdot z^{p} belongs to 𝒜 k ​ ( U) \mathcal{A}_{k}(U) and satisfies T ​ f = ∑ p ∈ ℕ m − l T ​ b p ​ ( Y) ⋅ Z p Tf=\sum_{p\in\mathbb{N}^{m-l}}Tb_{p}(Y)\cdot Z^{p}.

###### Proof.

It follows from the assumptions that g g is holomorphic on U U; it remains to show that g ∼ ∑ p ∈ ℕ m − l U ⁡ T ​ b p ​ ( Y) ​ Z p g\sim_{U}\sum_{p\in\mathbb{N}^{m-l}}Tb_{p}(Y)Z^{p}. Let 𝐚 > 0 \mathbf{a}>0; for each p ∈ ℕ m − l p\in\mathbb{N}^{m-l}, we write T ​ b p = ∑ b p, α ​ Y α Tb_{p}=\sum b_{p,\alpha}Y^{\alpha} and define ϵ p: U ′ ⟶ ℂ \epsilon_{p}:U^{\prime}\longrightarrow\mathbb{C} by

 | ϵ p ​ ( y):= b p ​ ( y) − ∑ | α | ≤ 𝐚 − | p | b p, α ​ y α. \epsilon_{p}(y):=b_{p}(y)-\sum_{|\alpha|\leq\mathbf{a}-|p|}b_{p,\alpha}y^{\alpha}. |  |

After shrinking W W if necessary, there is a constant C > 0 C>0 such that | ϵ p ​ ( y) | ≤ C ​ ‖ y ‖ 𝐚 − | p | |\epsilon_{p}(y)|\leq C\|y\|^{\mathbf{a}-|p|} whenever | p | ≤ 𝐚 |p|\leq\mathbf{a} and y ∈ U ′ y\in U^{\prime}. For every x ∈ U x\in U, we have

 | g ⁡ ( x) − ∑ | ( α, p) | ≤ 𝐚 b p, α ​ y α ​ z p = ∑ | p | ≤ 𝐚 ϵ p ​ ( y) ​ z p + ∑ | p | > 𝐚 b p ​ ( y) ​ z p. g(x)-\sum_{|(\alpha,p)|\leq\mathbf{a}}b_{p,\alpha}y^{\alpha}z^{p}=\sum_{|p|\leq\mathbf{a}}\epsilon_{p}(y)z^{p}+\sum_{|p|>\mathbf{a}}b_{p}(y)z^{p}. |  |

By the above, ∑ | p | ≤ 𝐚 ϵ p ​ ( y) ​ z p = o ⁡ ( ‖ x ‖ 𝐚) \sum_{|p|\leq\mathbf{a}}\epsilon_{p}(y)z^{p}=o\left(\|x\|^{\mathbf{a}}\right) as ‖ x ‖ → 0 \|x\|\to 0 in U U; so it suffices to show, after shrinking U U again if necessary, that ∑ | p | > 𝐚 b p ​ ( y) ​ z p = o ⁡ ( ‖ x ‖ 𝐚) \sum_{|p|>\mathbf{a}}b_{p}(y)z^{p}=o\left(\|x\|^{\mathbf{a}}\right) as ‖ x ‖ → 0 \|x\|\to 0 in U U. Let ρ:= inf { | p | − 𝐚: | p | > 𝐚 } > 0 \rho:=\inf\left\{|p|-\mathbf{a}:\ |p|>\mathbf{a}\right\}>0. By assumption (ii), we have for x ∈ U x\in U satisfying ‖ z ‖ ≤ ρ 2 \|z\|\leq\frac{\rho}{2} that

 | | ∑ | p | > 𝐚 b p ​ ( y) ​ z p | ≤ A R 𝐚 + ρ ​ ( ∑ | p | ≥ 𝐚 + ρ 2 𝐚 + ρ − | p |) ⋅ ‖ z ‖ 𝐚 + ρ = o ⁡ ( ‖ x ‖ 𝐚) \left|\sum_{|p|>\mathbf{a}}b_{p}(y)z^{p}\right|\leq\frac{A}{R^{\mathbf{a}+\rho}}\left(\sum_{|p|\geq\mathbf{a}+\rho}2^{\mathbf{a}+\rho-|p|}\right)\cdot\|z\|^{\mathbf{a}+\rho}=o\left(\|x\|^{\mathbf{a}}\right) |  |

as ‖ x ‖ → 0 \|x\|\to 0, as required. ∎

The following criterion for membership in 𝒜 k ​ ( U) \mathcal{A}_{k}(U) will be useful in Section 8:

###### Corollary 2.16.

Let f: U ⟶ ℂ f:U\longrightarrow\mathbb{C} be holomorphic, and let W ⊆ 𝐋 W\subseteq\mathbf{L} be a quadratic domain and R > 0 R>0 be such that W k × B 𝐋 ​ ( R) m − k ⊆ U W^{k}\times B_{\mathbf{L}}(R)^{m-k}\subseteq U. Let S ⊆ [0, ∞) k S\subseteq[0,\infty)^{k} be a natural set, and assume that for each α ∈ S \alpha\in S, there is a holomorphic function a α: B 𝐋 ​ ( R) m − k ⟶ ℂ a_{\alpha}:B_{\mathbf{L}}(R)^{m-k}\longrightarrow\mathbb{C} such that

1. (i)

for every z ∈ B 𝐋 ​ ( R) m − k z\in B_{\mathbf{L}}(R)^{m-k}, the function f z: W k ⟶ ℂ f_{z}:W^{k}\longrightarrow\mathbb{C} defined by f z ​ ( y):= f ​ ( y, z) f_{z}(y):=f(y,z) belongs to 𝒜 k ​ ( W k) \mathcal{A}_{k}(W^{k}) with T ​ f z = ∑ α ∈ S a α ​ ( z) ​ y α Tf_{z}=\sum_{\alpha\in S}a_{\alpha}(z)y^{\alpha};

2. (ii)

for each ν > 0 \nu>0, there are constants K ν, ϵ ν > 0 K_{\nu},\epsilon_{\nu}>0 and a quadratic domain W ν ⊆ W W_{\nu}\subseteq W such that ‖ f ⁡ ( y, z) − ∑ | α | ≤ ν a α ​ ( z) ​ y α ‖ ≤ K ν ​ ‖ y ‖ ν + ϵ ν \left\|f(y,z)-\sum_{|\alpha|\leq\nu}a_{\alpha}(z)y^{\alpha}\right\|\leq K_{\nu}\|y\|^{\nu+\epsilon_{\nu}} for all ( y, z) ∈ W ν k × B 𝐋 ​ ( R) m − k (y,z)\in W_{\nu}^{k}\times B_{\mathbf{L}}(R)^{m-k}.

Then f ∈ 𝒜 k ​ ( W k × B 𝐋 ​ ( R) m − k) f\in\mathcal{A}_{k}\left(W^{k}\times B_{\mathbf{L}}(R)^{m-k}\right), and if T ​ a α = ∑ a α, p ​ z p Ta_{\alpha}=\sum a_{\alpha,p}z^{p} for each α ∈ S \alpha\in S, then T ​ f = ∑ a α, p ​ y α ​ z p Tf=\sum a_{\alpha,p}y^{\alpha}z^{p}.

###### Proof.

By assumption (i) and Proposition 2.15, it suffices to show that the function f ( l): W k ⟶ ℂ f^{(l)}:W^{k}\longrightarrow\mathbb{C} defined by f ( l) ​ ( y):= ( ∂ l f / ∂ y l) ​ ( y, 0) f^{(l)}(y):=(\partial^{l}f/\partial y^{l})(y,0) belongs to 𝒜 k ​ ( W k) \mathcal{A}_{k}(W^{k}) for each l ∈ ℕ m − k l\in\mathbb{N}^{m-k}. But for any such l l, any ν > 0 \nu>0 and any y ∈ W ν y\in W_{\nu}, we get from the Cauchy estimates that

 | ‖ f ( l) ​ ( y) − ∑ | α | ≤ ν a α ( l) ​ ( 0) ​ y α ‖ \displaystyle\left\|f^{(l)}(y)-\sum_{|\alpha|\leq\nu}a_{\alpha}^{(l)}(0)y^{\alpha}\right\| | = ‖ ∂ l ∂ y l ​ ( f ⁡ ( y, z) − ∑ | α | ≤ ν a α ​ ( z) ​ y α) ​ ( y, 0) ‖ \displaystyle=\left\|\frac{\partial^{l}}{\partial y^{l}}\left(f(y,z)-\sum_{|\alpha|\leq\nu}a_{\alpha}(z)y^{\alpha}\right)(y,0)\right\| |  |

 |  | ≤ K ν R | l | ​ ‖ y ‖ ν + ϵ ν, \displaystyle\leq\frac{K_{\nu}}{R^{|l|}}\|y\|^{\nu+\epsilon_{\nu}}, |  |

as required. ∎

## 3. Truncation-division, Taylor expansion and composition in the holomorphic variables

It will be convenient from now on to more explicitely separate the holomorphic variables from the non-holomorphic ones. Thus, we let m, n ∈ ℕ m,n\in\mathbb{N}, and let U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} be an m m -quadratic domain. Below, we let y = ( y 1, …, y n) y=(y_{1},\dots,y_{n}) range over 𝐋 n \mathbf{L}^{n} and Y = ( Y 1, …, Y n) Y=(Y_{1},\dots,Y_{n}) be indeterminates.

###### Remark 3.1.

Let σ \sigma be a permutation of { 1, …, m } \{1,\dots,m\} and τ \tau be a permutation of { 1, …, n } \{1,\dots,n\}. We associate to σ \sigma and τ \tau the substitution automorphisms σ, τ: ℂ ⁡ [[X ∗, Y]] ⟶ ℂ ⁡ [[X ∗, Y]] \sigma,\tau:\mathbb{C}[\![X^{*},Y]\!]\longrightarrow\mathbb{C}[\![X^{*},Y]\!] defined by σ ⁡ ( X, Y):= ( X σ ⁡ ( 1), …, X σ ⁡ ( m), Y) \sigma(X,Y):=(X_{\sigma(1)},\dots,X_{\sigma(m)},Y) and τ ⁡ ( X, Y):= ( X, Y τ ⁡ ( 1), …, Y τ ⁡ ( n)) \tau(X,Y):=(X,Y_{\tau(1)},\dots,Y_{\tau(n)}) and the maps σ, τ: 𝐋 m + n ⟶ 𝐋 m + n \sigma,\tau:\mathbf{L}^{m+n}\longrightarrow\mathbf{L}^{m+n} defined by σ ⁡ ( x, y):= ( x σ ⁡ ( 1), …, x σ ⁡ ( m), y) \sigma(x,y):=(x_{\sigma(1)},\dots,x_{\sigma(m)},y) and τ ⁡ ( x, y):= ( x, y τ ⁡ ( 1), …, y τ ⁡ ( n)) \tau(x,y):=(x,y_{\tau(1)},\dots,y_{\tau(n)}). Then for every f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U), we have f ∘ σ ∈ 𝒜 m ​ ( σ − 1 ​ ( U)) f\circ\sigma\in\mathcal{A}_{m}(\sigma^{-1}(U)) with T ⁡ ( f ∘ σ) = σ ⁡ ( T ​ f) T(f\circ\sigma)=\sigma(Tf) and f ∘ τ ∈ 𝒜 m ​ ( τ − 1 ​ ( U)) f\circ\tau\in\mathcal{A}_{m}(\tau^{-1}(U)) with T ⁡ ( f ∘ τ) = τ ⁡ ( T ​ f) T(f\circ\tau)=\tau(Tf).

### Truncation-division

First, we show that the natural operations of truncation and division by monomials in the Y Y variables of T ​ f Tf, where f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U), lead to new functions in 𝒜 m ​ ( U) \mathcal{A}_{m}(U).

###### Proposition 3.2.

Let f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U) and δ ∈ ℕ n \delta\in\mathbb{N}^{n}.

1. (1)

Assume that T ​ f = Y δ ⋅ G Tf=Y^{\delta}\cdot G for some G ∈ ℂ ⁡ [[X ∗, Y]] G\in\mathbb{C}[\![X^{*},Y]\!]. Then there is a g ∈ 𝒜 m ​ ( U) g\in\mathcal{A}_{m}(U) such that T ​ g = G Tg=G.

2. (2)

There is an f ( 0, δ) ∈ 𝒜 m ​ ( U) f_{(0,\delta)}\in\mathcal{A}_{m}(U) such that T ​ f ( 0, δ) = ( T ​ f) ( 0, δ) Tf_{(0,\delta)}=(Tf)_{(0,\delta)}.

###### Proof.

Below, we write y ^ j:= ( y 1, …, y j − 1, 0, y j + 1, …, y n) \widehat{y}_{j}:=(y_{1},\dots,y_{j-1},0,y_{j+1},\dots,y_{n}) for each j = 1, …, n j=1,\dots,n.

(1) Working by induction on | δ | |\delta| and using Remark 3.1, we may assume that δ = ( 0, …, 0, 1) \delta=(0,\dots,0,1). Given h ∈ 𝒜 m ​ ( U) h\in\mathcal{A}_{m}(U), the function I ⁡ ( h): U ⟶ ℂ I(h):U\longrightarrow\mathbb{C} defined by

 | I ⁡ ( h) ​ ( x, y):= ∫ 0 1 h ⁡ ( x, y 1, …, y n − 1, t ​ y n) ​ 𝑑 t I(h)(x,y):=\int_{0}^{1}h(x,y_{1},\dots,y_{n-1},ty_{n})dt |  |

belongs to 𝒜 m ​ ( U) \mathcal{A}_{m}(U), where t ⋅ ( r, φ):= ( t ​ r, φ) t\cdot(r,\varphi):=(tr,\varphi) for t > 0 t>0 and ( r, φ) ∈ 𝐋 (r,\varphi)\in\mathbf{L}. Since f ⁡ ( x, y ^ n) = 0 f(x,\widehat{y}_{n})=0, we get from the fundamental theorem of calculus that f ⁡ ( x, y) = y n ⋅ I ⁡ ( ∂ f / ∂ y n) ​ ( x, y) f(x,y)=y_{n}\cdot I(\partial f/\partial y_{n})(x,y) for all ( x, y) ∈ U (x,y)\in U, so part (1) follows from Corollary 2.13.

(2) We define h: U ⟶ ℂ h:U\longrightarrow\mathbb{C} by

 | h ⁡ ( x, y):= f ⁡ ( x, y) − ∑ j = 1 n ∑ p = 0 δ j − 1 1 p! ​ ∂ p f ∂ y j p ​ ( x, y ^ j) ⋅ y j p. h(x,y):=f(x,y)-\sum_{j=1}^{n}\sum_{p=0}^{\delta_{j}-1}\frac{1}{p!}\frac{\partial^{p}f}{\partial y_{j}^{p}}(x,\widehat{y}_{j})\cdot y_{j}^{p}. |  |

By Corollaries 2.12 and 2.13, the function h h belongs to 𝒜 m ​ ( U) \mathcal{A}_{m}(U) and T ​ h = Y δ ⋅ G Th=Y^{\delta}\cdot G for some G ∈ ℂ ⁡ [[X ∗, Y]] G\in\mathbb{C}[\![X^{*},Y]\!]. Part (2) now follows from part (1). ∎

###### Remark 3.3.

We do not know whether, in the situation of Proposition 3.2, a corresponding statements holds for all variables, that is, whether

- ( ∗) f (\ast)_{f}

for every elementary set S ⊆ [0, ∞) m × ℕ n S\subseteq[0,\infty)^{m}\times\mathbb{N}^{n}, there are an m m -quadratic V ⊆ U V\subseteq U and an f S ∈ 𝒜 m ​ ( V) f_{S}\in\mathcal{A}_{m}(V) such that T ​ f S = ( T ​ f) S Tf_{S}=(Tf)_{S}.

This is the first of two reasons to eventually restrict our attention to a subclass of 𝒜 m ​ ( U) \mathcal{A}_{m}(U) introduced in Section 5.

### Taylor expansion

Next, we establish a Taylor expansion result with respect to the y y variables. Let V ⊆ 𝐋 p V\subseteq\mathbf{L}^{p} be open; recall that a map 𝐟: V ⟶ 𝐋 p \mathbf{f}:V\longrightarrow\mathbf{L}^{p} is holomorphic if the function log p ∘ 𝐟 ∘ log p − 1: log p ⁡ ( V) ⟶ ℂ p \log_{p}\circ\mathbf{f}\circ\log_{p}^{-1}:\log_{p}(V)\longrightarrow\mathbb{C}^{p} is holomorphic. Note that if W ⊆ 𝐋 q W\subseteq\mathbf{L}^{q} and 𝐠: W ⟶ 𝐋 p \mathbf{g}:W\longrightarrow\mathbf{L}^{p} is holomorphic such that 𝐠 ⁡ ( W) ⊆ V \mathbf{g}(W)\subseteq V, then the composition 𝐟 ∘ g: W ⟶ 𝐋 p \mathbf{f}\circ g:W\longrightarrow\mathbf{L}^{p} is holomorphic.

###### Definition 3.4 (Translation).

Let λ ∈ ℂ \lambda\in\mathbb{C} be nonzero, and denote by Arg λ ∈ ( − π 2, π 2] \Arg\lambda\in(-\frac{\pi}{2},\frac{\pi}{2}] the standard argument of λ \lambda. We put

 | ℂ λ:= { z ∈ ℂ: Arg ⁡ λ − π 2 < arg ⁡ z < Arg ⁡ λ + π 2 }, \mathbb{C}_{\lambda}:=\left\{z\in\mathbb{C}:\ \Arg\lambda-\frac{\pi}{2}<\arg z<\Arg\lambda+\frac{\pi}{2}\right\}, |  |

and we let 𝐥 λ: ℂ λ ⟶ 𝐋 \mathbf{l}_{\lambda}:\mathbb{C}_{\lambda}\longrightarrow\mathbf{L} be defined by 𝐥 λ ​ ( z):= ( | z |, arg ⁡ z) \mathbf{l}_{\lambda}(z):=(|z|,\arg z) and put D ⁡ ( λ):= 𝐥 λ ​ ( B ⁡ ( λ, | λ |)) D(\lambda):=\mathbf{l}_{\lambda}(B(\lambda,|\lambda|)). We let 𝐭 λ: B 𝐋 ​ ( λ) ⟶ D ⁡ ( λ) \mathbf{t}_{\lambda}:B_{\mathbf{L}}(\lambda)\longrightarrow D(\lambda) be the holomorphic map defined by 𝐭 λ ​ ( x):= 𝐥 λ ​ ( λ + ( x) 1) \mathbf{t}_{\lambda}(x):=\mathbf{l}_{\lambda}\left(\lambda+(x)^{1}\right).

For completeness’ sake, we also define 𝐭 0: 𝐋 ⟶ 𝐋 \mathbf{t}_{0}:\mathbf{L}\longrightarrow\mathbf{L} by 𝐭 0 ​ ( x):= x \mathbf{t}_{0}(x):=x.

For λ ∈ ℂ p \lambda\in\mathbb{C}^{p} and w ∈ 𝐋 p w\in\mathbf{L}^{p}, we write 𝐭 λ ​ ( w):= ( 𝐭 λ 1 ​ ( w 1), …, 𝐭 λ p ​ ( w p)) \mathbf{t}_{\lambda}(w):=(\mathbf{t}_{\lambda_{1}}(w_{1}),\dots,\mathbf{t}_{\lambda_{p}}(w_{p})). Abusing notation, we identify the set { x ∈ 𝐋 0 p: − π < arg x i ≤ π \big\{x\in\mathbf{L}^{p}_{0}:\ -\pi<\arg x_{i}\leq\pi for each i } i\big\} with ℂ p \mathbb{C}^{p}.

###### Remark 3.5.

Let λ ∈ ℂ m + n ∩ cl 0 ⁡ ( U) \lambda\in\mathbb{C}^{m+n}\cap\cl_{0}(U) and f ∈ 𝒪 ⁡ ( U) f\in\mathcal{O}(U). An elementary calculation shows that for each i ∈ { 1, …, m } i\in\{1,\dots,m\}, we have

 | ∂ i ( f ∘ 𝐭 λ) = ( ( ∂ i f) ∘ 𝐭 λ) ⋅ x i 1 λ i + x i 1. \partial_{i}(f\circ\mathbf{t}_{\lambda})=\Big((\partial_{i}f)\circ\mathbf{t}_{\lambda}\Big)\cdot\frac{x_{i}^{1}}{\lambda_{i}+x_{i}^{1}}. |  |

We now let l ∈ { 1, …, n } l\in\{1,\dots,n\}, and we write y ′:= ( y 1, …, y n − l) y^{\prime}:=(y_{1},\dots,y_{n-l}), Y ′:= ( Y 1, …, Y n − l) Y^{\prime}:=(Y_{1},\dots,Y_{n-l}), z = ( z 1, …, z l):= ( y n − l + 1, …, y n) z=(z_{1},\dots,z_{l}):=(y_{n-l+1},\dots,y_{n}) and Z = ( Z 1, …, Z l):= ( Y n − l + 1, …, Y n) Z=(Z_{1},\dots,Z_{l}):=(Y_{n-l+1},\dots,Y_{n}). We assume that U = W m × B 𝐋 ​ ( R) n U=W^{m}\times B_{\mathbf{L}}(R)^{n} for some quadratic domain W ⊆ 𝐋 W\subseteq\mathbf{L} and some R > 0 R>0. We let f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U) and λ ∈ B ​ ( 0, R) l \lambda\in B(0,R)^{l}, and we put U ′:= W m × B 𝐋 ​ ( R) n − l U^{\prime}:=W^{m}\times B_{\mathbf{L}}(R)^{n-l}.

###### Lemma 3.6.

Assume ( ∗) f (\ast)_{f} holds. Then the formal sum T ​ f ​ ( X, Y ′, λ) Tf(X,Y^{\prime},\lambda) gives a series in ℂ ⁡ [[X ∗, Y ′]] \mathbb{C}[\![X^{*},Y^{\prime}]\!]. Moreover, the function ( x, y ′) ↦ f ⁡ ( x, y ′, λ): U ′ ⟶ ℂ (x,y^{\prime})\mapsto f(x,y^{\prime},\lambda):U^{\prime}\longrightarrow\mathbb{C}, denoted simply by f ⁡ ( x, y ′, λ) f(x,y^{\prime},\lambda), satisfies ( ∗) f ⁡ ( x, y ′, λ) (\ast)_{f(x,y^{\prime},\lambda)} with

 | T ⁡ ( f ⁡ ( x, y ′, λ)) = ( T ​ f) ​ ( X, Y ′, λ). T(f(x,y^{\prime},\lambda))=(Tf)(X,Y^{\prime},\lambda). |  |

###### Proof.

We assume that l = 1 l=1; the general case follows by induction on l l. Throughout this proof, we let γ \gamma and p p range over [0, ∞) m × ℕ n − 1 [0,\infty)^{m}\times\mathbb{N}^{n-1} and ℕ \mathbb{N}, respectively. We write f ⁡ ( x, y) = ∑ a p ​ ( x, y ′) ​ z p f(x,y)=\sum a_{p}(x,y^{\prime})z^{p} as a convergent power series in z = y n z=y_{n} and T ​ f = ∑ a ( γ, p) ​ ( X, Y ′) γ ​ Z p Tf=\sum a_{(\gamma,p)}(X,Y^{\prime})^{\gamma}Z^{p}. From ( ∗) f (\ast)_{f} and Propositions 2.14 and 2.8, we see that ( ∗) a p (\ast)_{a_{p}} holds (with n − 1 n-1 in place of n n) for each p ∈ ℕ p\in\mathbb{N}. Hence

1. (i)

f ( γ, 0) ​ ( x, y) = ∑ ( a p) γ ​ ( x, y ′) ​ z p f_{(\gamma,0)}(x,y)=\sum(a_{p})_{\gamma}(x,y^{\prime})z^{p} for all γ \gamma and all sufficiently small ( x, y) ∈ U (x,y)\in U;

2. (ii)

a ( γ, p) = ( a p) γ ​ ( 0, 0) a_{(\gamma,p)}=(a_{p})_{\gamma}(0,0) for all γ \gamma and p p.

It follows from (ii) and Proposition 2.14 that

 | T ​ f ​ ( X, Y ′, λ) = ∑ γ ( ∑ p a ( γ, p) ​ λ p) ​ ( X, Y ′) γ Tf(X,Y^{\prime},\lambda)=\sum_{\gamma}\left(\sum_{p}a_{(\gamma,p)}\lambda^{p}\right)(X,Y^{\prime})^{\gamma} |  |

belongs to ℂ ⁡ [[X ∗, Y ′]] \mathbb{C}[\![X^{*},Y^{\prime}]\!], which proves the first assertion.

Next, we let 𝐚 > 0 \mathbf{a}>0 and consider the finite set

 | S 𝐚:= { γ ∈ Π m + n − 1 ​ ( supp ⁡ T ​ f): | γ | ≤ 𝐚 }. S_{\mathbf{a}}:=\left\{\gamma\in\Pi_{m+n-1}(\supp Tf):\ |\gamma|\leq\mathbf{a}\right\}. |  |

Note that, by (ii) above and Proposition 2.14, for every γ ∈ S 𝐚 \gamma\in S_{\mathbf{a}} we have f { γ } × ℕ ​ ( x, y) = ∑ p a ( γ, p) ​ z p f_{\{\gamma\}\times\mathbb{N}}(x,y)=\sum_{p}a_{(\gamma,p)}z^{p} for all sufficiently small ( x, y) ∈ U (x,y)\in U. Therefore, after shrinking U U if necessary, the function

 | g ⁡ ( x, y):= f ⁡ ( x, y) − ∑ γ ∈ S 𝐚 f { γ } × ℕ ​ ( x, y) ⋅ ( x, y ′) γ g(x,y):=f(x,y)-\sum_{\gamma\in S_{\mathbf{a}}}f_{\{\gamma\}\times\mathbb{N}}(x,y)\cdot(x,y^{\prime})^{\gamma} |  |

belongs to 𝒜 m ​ ( U) \mathcal{A}_{m}(U) and satisfies T ​ g = T ​ f − ∑ γ ∈ S 𝐚 ( T ​ f) { γ } × ℕ ⋅ ( X, Y ′) γ Tg=Tf-\sum_{\gamma\in S_{\mathbf{a}}}(Tf)_{\{\gamma\}\times\mathbb{N}}\cdot(X,Y^{\prime})^{\gamma}. By the above, it follows that

 | T ​ g ​ ( X, Y) = T ​ f ​ ( X, Y) − ∑ γ ∈ S 𝐚 ∑ p a ( γ, p) ⋅ ( X, Y ′) γ ​ Z p; Tg(X,Y)=Tf(X,Y)-\sum_{\gamma\in S_{\mathbf{a}}}\sum_{p}a_{(\gamma,p)}\cdot(X,Y^{\prime})^{\gamma}Z^{p}\ ; |  |

in particular, f ⁡ ( x, y ′, λ) − ∑ | γ | ≤ 𝐚 ( ∑ p a ( γ, p) ​ λ p) ⋅ ( x, y ′) γ = o ⁡ ( ‖ ( x, y ′) ‖ 𝐚) f(x,y^{\prime},\lambda)-\sum_{|\gamma|\leq\mathbf{a}}\left(\sum_{p}a_{(\gamma,p)}\lambda^{p}\right)\cdot(x,y^{\prime})^{\gamma}=o(\|(x,y^{\prime})\|^{\mathbf{a}}) as ‖ ( x, y ′) ‖ → 0 \|(x,y^{\prime})\|\to 0 in U ′ U^{\prime}. Hence f ⁡ ( x, y ′, λ) ∈ 𝒜 m ​ ( U ′) f(x,y^{\prime},\lambda)\in\mathcal{A}_{m}(U^{\prime}) with T ⁡ ( f ⁡ ( x, y ′, λ)) = ( T ​ f) ​ ( X, Y ′, λ) T(f(x,y^{\prime},\lambda))=(Tf)(X,Y^{\prime},\lambda).

Finally, given an elementary set S ⊆ [0, ∞) m × ℕ n − 1 S\subseteq[0,\infty)^{m}\times\mathbb{N}^{n-1} and arguing as above with f S × { 0 } f_{S\times\{0\}} in place of f f, we see that ( ∗) f ⁡ ( x, y ′, λ) (\ast)_{f(x,y^{\prime},\lambda)} holds. ∎

We put R ′:= min i = 1, …, l ⁡ ( R − | λ i |) R^{\prime}:=\min_{i=1,\dots,l}(R-|\lambda_{i}|) and V:= W m × B 𝐋 ​ ( R) n − l × B 𝐋 ​ ( R ′) l V:=W^{m}\times B_{\mathbf{L}}(R)^{n-l}\times B_{\mathbf{L}}(R^{\prime})^{l}. From the Taylor expansion theorem for holomorphic functions, Propositions 2.14 and 2.15 and Lemma 3.6, we obtain:

###### Corollary 3.7.

Assume ( ∗) f (\ast)_{f} holds. Then the function g: V ⟶ ℂ g:V\longrightarrow\mathbb{C} defined by g ⁡ ( x, y):= f ⁡ ( x, y ′, 𝐭 λ ​ ( z)) g(x,y):=f(x,y^{\prime},\mathbf{t}_{\lambda}(z)) satisfies ( ∗) g (\ast)_{g} with

 | T ​ g ​ ( X, Y) = ∑ p ∈ ℕ l 1 p! ​ ∂ p ( T ​ f) ∂ Z p ​ ( X, Y ′, λ) ⋅ Z p. ∎ Tg(X,Y)=\sum_{p\in\mathbb{N}^{l}}\frac{1}{p!}\frac{\partial^{p}(Tf)}{\partial Z^{p}}(X,Y^{\prime},\lambda)\cdot Z^{p}.\qed |  |

In the situation of Corollary 3.7, we also write 𝐭 ( 0, λ) ​ f \mathbf{t}_{(0,\lambda)}f and T ( 0, λ) ​ f T_{(0,\lambda)}f for the function g g and the series T ​ g Tg, respectively.

###### Remark 3.8.

We are not aware of a statement corresponding to Corollary 3.7 for translation in the x x variables. This is the second reason to restrict our attention to a subclass of 𝒜 m ​ ( U) \mathcal{A}_{m}(U), done in Section 5.

### Composition

Let f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U). Let V ⊆ 𝐋 m + n V\subseteq\mathbf{L}^{m+n} be an m m -quadratic domain and let g = ( g 1, …, g n) ∈ 𝒜 m ​ ( V) n g=(g_{1},\dots,g_{n})\in\mathcal{A}_{m}(V)^{n}. Abusing notation, for ( x, y) ∈ V (x,y)\in V we write ( x, g ⁡ ( x, y)) ∈ U (x,g(x,y))\in U to mean ( x, g ⁡ ( x, y)) ∈ int ⁡ ( cl 0 ⁡ ( π m ​ ( U))) (x,g(x,y))\in\ir(\cl_{0}(\pi_{m}(U))), and if the latter is the case, we also write f ⁡ ( x, g ⁡ ( x, y)) f(x,g(x,y)) in place of f ♯ ​ ( x, g ​ ( x, y)) f^{\sharp}(x,g(x,y)).

For the next lemma, we assume that g ⁡ ( 0, 0) = 0 g(0,0)=0 and ( x, g ⁡ ( x, y)) ∈ U (x,g(x,y))\in U for all ( x, y) ∈ V (x,y)\in V, and we define the holomorphic function h: V ⟶ ℂ h:V\longrightarrow\mathbb{C} by h ⁡ ( x, y):= f ⁡ ( x, g ⁡ ( x, y)). h(x,y):=f(x,g(x,y)).

###### Proposition 3.9.

The function h h belongs to 𝒜 m ​ ( V) \mathcal{A}_{m}(V) and T ​ h ​ ( X, Y) = T ​ f ​ ( X, T ​ g ​ ( X, Y)) Th(X,Y)=Tf(X,Tg(X,Y)).

We will deduce this proposition from the following two special cases:

###### Lemma 3.10.

Assume that T ​ g ​ ( X, 0) = T ​ g ​ ( X, Y) Tg(X,0)=Tg(X,Y). Then h ∈ 𝒜 m ​ ( V) h\in\mathcal{A}_{m}(V) and T ​ h ​ ( X, Y) = T ​ f ​ ( X, T ​ g ​ ( X, Y)) Th(X,Y)=Tf(X,Tg(X,Y)).

###### Proof.

We write T ​ f ​ ( X, Y) = ∑ a γ, p ​ X γ ​ Y p Tf(X,Y)=\sum a_{\gamma,p}X^{\gamma}Y^{p} and T ​ g j ​ ( X) = ∑ b j, δ ​ X δ Tg_{j}(X)=\sum b_{j,\delta}X^{\delta}; note that b j, 0 = 0 b_{j,0}=0 for each j j. Then ( T ​ f) ​ ( X, ( T ​ g) ​ ( X, Y)) = ∑ c α ​ X α (Tf)(X,(Tg)(X,Y))=\sum c_{\alpha}X^{\alpha}, where for each α ∈ [0, ∞) m \alpha\in[0,\infty)^{m},

 | Σ ( α):= { ( γ, p, δ): γ ∈ Π m ( supp ( T f)), p ∈ ℕ n, and δ = ( δ 1, …, δ | p |) ∈ ( ⋃ supp ( g j)) | p | with γ + δ 1 + ⋯ δ | p | = α } \Sigma(\alpha):=\big\{(\gamma,p,\delta):\ \gamma\in\Pi_{m}(\supp(Tf)),\,p\in\mathbb{N}^{n},\text{ and }\\ \delta=(\delta^{1},\dots,\delta^{|p|})\in\left(\bigcup\supp(g_{j})\right)^{|p|}\text{ with }\gamma+\delta^{1}+\cdots\delta^{|p|}=\alpha\big\} |  |

and

 | c α:= ∑ ( γ, p, δ) ∈ Σ ⁡ ( α) a γ, p ⋅ ∏ j = 1 n ∏ l = p 1 + ⋯ + p j − 1 + 1 p 1 + ⋯ + p l b j, δ l. c_{\alpha}:=\sum_{(\gamma,p,\delta)\in\Sigma(\alpha)}a_{\gamma,p}\cdot\prod_{j=1}^{n}\prod_{l=p_{1}+\cdots+p_{j-1}+1}^{p_{1}+\cdots+p_{l}}b_{j,\delta^{l}}. |  |

Since each b j, 0 = 0 b_{j,0}=0, each set Σ ⁡ ( α) \Sigma(\alpha) is finite; in fact, with

 | q ⁡ ( r):= ∑ i = 1 m | Π X i ​ ( { β ∈ ⋃ supp ⁡ ( g j): | β | ≤ r }) |, q(r):=\sum_{i=1}^{m}\left|\Pi_{X_{i}}\left(\left\{\beta\in\bigcup\supp(g_{j}):\ |\beta|\leq r\right\}\right)\right|, |  |

we have | p | ≤ q ⁡ ( | α |) |p|\leq q(|\alpha|) for all ( γ, p, δ) ∈ Σ ⁡ ( α) (\gamma,p,\delta)\in\Sigma(\alpha).

Let now 𝐚 > 1 \mathbf{a}>1, and for all suitable ( x, y) ∈ 𝐋 m + n (x,y)\in\mathbf{L}^{m+n}, we define

 | f 𝐚 ​ ( x, y):= f ⁡ ( x, y) − ∑ | γ | + | p | ≤ 𝐚 + q ⁡ ( 𝐚) a γ, p ​ x γ ​ y p f^{\mathbf{a}}(x,y):=f(x,y)-\sum_{|\gamma|+|p|\leq\mathbf{a}+q(\mathbf{a})}a_{\gamma,p}x^{\gamma}y^{p} |  |

and

 | g j 𝐚 ( x):= g j ( x, 0) − ∑ | δ | ≤ 𝐚 b j, δ x δ, for j = 1, …, n. g_{j}^{\mathbf{a}}(x):=g_{j}(x,0)-\sum_{|\delta|\leq\mathbf{a}}b_{j,\delta}x^{\delta},\quad\text{for }j=1,\dots,n. |  |

Then f 𝐚 ​ ( x, y) = o ⁡ ( ‖ ( x, y) ‖ 𝐚 + q ⁡ ( 𝐚)) f^{\mathbf{a}}(x,y)=o\left(\|(x,y)\|^{\mathbf{a}+q(\mathbf{a})}\right) as ‖ ( x, y) ‖ → 0 \|(x,y)\|\to 0 in some m m -quadratic domain, and g j 𝐚 ​ ( x) = o ⁡ ( ‖ x ‖ 𝐚) g_{j}^{\mathbf{a}}(x)=o(\|x\|^{\mathbf{a}}) for each j j as ‖ x ‖ → 0 \|x\|\to 0 in some quadratic domain. Thus, f 𝐚 ​ ( x, g a ​ ( x)) = o ⁡ ( ‖ x ‖ 𝐚) f^{\mathbf{a}}(x,g^{a}(x))=o(\|x\|^{\mathbf{a}}), and there is a polynomial P ⁡ ( x) = ∑ d β ​ X β P(x)=\sum d_{\beta}X^{\beta} such that | β | > 𝐚 |\beta|>\mathbf{a} whenever d β ≠ 0 d_{\beta}\neq 0 and

 | P ⁡ ( x) = f ⁡ ( x, g ⁡ ( x, 0)) − f 𝐚 ​ ( x, g 𝐚 ​ ( x)) − ∑ | α | ≤ 𝐚 c α ​ x α P(x)=f(x,g(x,0))-f^{\mathbf{a}}(x,g^{\mathbf{a}}(x))-\sum_{|\alpha|\leq\mathbf{a}}c_{\alpha}x^{\alpha} |  |

for all sufficiently small x x. In particular, f ⁡ ( x, g ⁡ ( x, 0)) − ∑ | α | ≤ 𝐚 c α ​ x α = o ⁡ ( ‖ x ‖ 𝐚) f(x,g(x,0))-\sum_{|\alpha|\leq\mathbf{a}}c_{\alpha}x^{\alpha}=o(\|x\|^{\mathbf{a}}), which proves the lemma. ∎

###### Lemma 3.11.

Assume that T ​ g ​ ( X, 0) = 0 Tg(X,0)=0. Then h ∈ 𝒜 m ​ ( V) h\in\mathcal{A}_{m}(V) and T ​ h ​ ( X, Y) = T ​ f ​ ( X, T ​ g ​ ( X, Y)) Th(X,Y)=Tf(X,Tg(X,Y)).

###### Proof.

After shrinking U U and V V if necessary, we may assume that f f is bounded on U U. By Proposition 2.14, we can write f ⁡ ( x) = ∑ a p ​ ( x) ​ y p f(x)=\sum a_{p}(x)y^{p} for all ( x, y) ∈ U (x,y)\in U and g j ​ ( x, y) = ∑ b j, p ​ ( x) ​ y p g_{j}(x,y)=\sum b_{j,p}(x)y^{p} for all ( x, y) ∈ V (x,y)\in V and j = 1, …, n j=1,\dots,n, and there are an m m -quadratic domain W ⊆ 𝐋 m W\subseteq\mathbf{L}^{m} and constants A, B > 0 A,B>0 such that a p, b j, p ∈ 𝒜 m ​ ( W m) a_{p},b_{j,p}\in\mathcal{A}_{m}(W^{m}) and ‖ a p ​ ( x) ‖, ‖ b j, p ​ ( x) ‖ ≤ A ​ B | p | \|a_{p}(x)\|,\|b_{j,p}(x)\|\leq AB^{|p|} for all x ∈ W m x\in W^{m}, p ∈ ℕ n p\in\mathbb{N}^{n} and j = 1, …, n j=1,\dots,n. Our assumption on g g implies that b j, 0 = 0 b_{j,0}=0 for each j j. Thus, after shrinking W W if necessary, there is an R > 0 R>0 such that for all ( x, y) ∈ W × B 𝐋 ​ ( R) n (x,y)\in W\times B_{\mathbf{L}}(R)^{n},

 | h ⁡ ( x, y) = f ⁡ ( x, g ⁡ ( x, y)) = ∑ p ∈ ℕ n a p ​ ( x) ​ g ​ ( x, y) p = ∑ r ∈ ℕ n c r ​ ( x) ​ y r, h(x,y)=f(x,g(x,y))=\sum_{p\in\mathbb{N}^{n}}a_{p}(x)g(x,y)^{p}=\sum_{r\in\mathbb{N}^{n}}c_{r}(x)y^{r}, |  |

where, for r ∈ ℕ n r\in\mathbb{N}^{n} and x ∈ W m x\in W^{m}, we put

 | c r ​ ( x):= ∑ ( p, q) ∈ Σ ⁡ ( r) a p ​ ( x) ⋅ ∏ i = 1 n ∏ j = p 1 + ⋯ + p i − 1 + 1 p 1 + ⋯ + p i b i, q j ​ ( x) c_{r}(x):=\sum_{(p,q)\in\Sigma(r)}a_{p}(x)\cdot\prod_{i=1}^{n}\prod_{j=p_{1}+\cdots+p_{i-1}+1}^{p_{1}+\cdots+p_{i}}b_{i,q^{j}}(x) |  |

with

 | Σ ( r):= { ( p, q): p ∈ ℕ n with | p | ≤ | r |, and q = ( q 1, …, q | p |) ∈ ( ℕ n ∖ { 0 }) | p | with q 1 + ⋯ + q | p | = r }. \Sigma(r):=\big\{(p,q):\ p\in\mathbb{N}^{n}\text{ with }|p|\leq|r|,\text{ and }\\ q=(q^{1},\dots,q^{|p|})\in(\mathbb{N}^{n}\setminus\{0\})^{|p|}\text{ with }q^{1}+\cdots+q^{|p|}=r\big\}. |  |

Note that each Σ ⁡ ( r) \Sigma(r) is finite, because | p | ≤ | r | |p|\leq|r| for each ( p, q) ∈ Σ ⁡ ( r) (p,q)\in\Sigma(r); we only need to consider such p p, because each b j, 0 = 0 b_{j,0}=0.) Since h h is bounded and holomorphic on W m × B 𝐋 ​ ( R) n W^{m}\times B_{\mathbf{L}}(R)^{n}, there are C, D > 0 C,D>0 such that ‖ c r ​ ( x) ‖ ≤ C ​ D | r | \|c_{r}(x)\|\leq CD^{|r|} for all x ∈ W m x\in W^{m} and r ∈ ℕ n r\in\mathbb{N}^{n}. Finally, writing T ​ f ​ ( X, Y) = ∑ p ∈ ℕ n A p ​ ( X) ​ Y p Tf(X,Y)=\sum_{p\in\mathbb{N}^{n}}A_{p}(X)Y^{p} and T ​ g j ​ ( X, Y) = ∑ q ∈ ℕ n B j, p ​ ( X) ​ Y q Tg_{j}(X,Y)=\sum_{q\in\mathbb{N}^{n}}B_{j,p}(X)Y^{q} for j = 1, …, n j=1,\dots,n, it follows from Remark 2.7 (3) that each c r c_{r} belongs to 𝒜 m ​ ( W m) \mathcal{A}_{m}(W^{m}) and satisfies

 | T ​ c r ​ ( X) = ∑ ( p, q) ∈ Σ ⁡ ( r) A p ​ ( X) ⋅ ∏ i = 1 n ∏ j = p 1 + ⋯ + p i − 1 + 1 p 1 + ⋯ + p i B i, q j ​ ( x). Tc_{r}(X)=\sum_{(p,q)\in\Sigma(r)}A_{p}(X)\cdot\prod_{i=1}^{n}\prod_{j=p_{1}+\cdots+p_{i-1}+1}^{p_{1}+\cdots+p_{i}}B_{i,q^{j}}(x). |  |

The claim now follows from Proposition 2.15, because supp ⁡ ( T ​ c r) ⊆ Π m ​ ( supp ⁡ T ​ f ​ ( X, T ​ g ​ ( X, Y))) \supp(Tc_{r})\subseteq\Pi_{m}\big(\supp Tf(X,Tg(X,Y))\big) for each r ∈ ℕ n r\in\mathbb{N}^{n} and the latter is a natural set by Proposition 1.13. ∎

###### Proof of Proposition 3.9.

We define f ′ ​ ( x, z, y):= f ⁡ ( x, z + y) f^{\prime}(x,z,y):=f(x,z+y), g 0 ​ ( x):= g ​ ( x, 0) g^{0}(x):=g(x,0) and g ′ ​ ( x, y):= g ⁡ ( x, y) − g ⁡ ( x, 0) g^{\prime}(x,y):=g(x,y)-g(x,0) for all suitable x ∈ 𝐋 m x\in\mathbf{L}^{m} and y, z ∈ 𝐋 n y,z\in\mathbf{L}^{n}. By Lemma 3.11, there is an m m -quadratic U ′ ⊆ 𝐋 m + 2 ​ n U^{\prime}\subseteq\mathbf{L}^{m+2n} such that f ′ ∈ 𝒜 m ​ ( U ′) f^{\prime}\in\mathcal{A}_{m}(U^{\prime}). Note that T ⁡ ( g 0) ​ ( X, 0) = T ⁡ ( g 0) ​ ( X, Y) T(g^{0})(X,0)=T(g^{0})(X,Y) and T ⁡ ( g ′) ​ ( X, 0) = 0 T(g^{\prime})(X,0)=0. Hence by Lemmas 3.6 and 3.10, there is an m m -quadratic V ′ ⊆ 𝐋 m + n V^{\prime}\subseteq\mathbf{L}^{m+n} such that f ′ ​ ( x, g 0 ​ ( x, y), y) ∈ 𝒜 m ​ ( V ′) f^{\prime}(x,g^{0}(x,y),y)\in\mathcal{A}_{m}(V^{\prime}), and by Lemma 3.11, there is an m m -quadratic V ′′ ⊆ 𝐋 m + n V^{\prime\prime}\subseteq\mathbf{L}^{m+n} such that f ′ ​ ( x, g 0 ​ ( x, y), g ′ ​ ( x, y)) ∈ 𝒜 m ​ ( V ′′) f^{\prime}(x,g^{0}(x,y),g^{\prime}(x,y))\in\mathcal{A}_{m}(V^{\prime\prime}). Since f ⁡ ( x, g ⁡ ( x, y)) = f ′ ​ ( x, g 0 ​ ( x), g ′ ​ ( x, y)) f(x,g(x,y))=f^{\prime}(x,g^{0}(x),g^{\prime}(x,y)) for all suitable ( x, y) ∈ 𝐋 m + n (x,y)\in\mathbf{L}^{m+n}, the proposition follows from Remark 2.7 (2). ∎

## 4. Blow-up substitutions in the non-holomorphic variables

We continue to work with m, n ∈ ℕ m,n\in\mathbb{N} and an m m -quadratic domain U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n}. For each real ρ > 0 \rho>0, the map 𝐩 ρ: 𝐋 ⟶ 𝐋 \mathbf{p}^{\rho}:\mathbf{L}\longrightarrow\mathbf{L} defined by

 | 𝐩 ρ ​ ( r, φ):= ( r ρ, ρ ​ φ) \mathbf{p}^{\rho}(r,\varphi):=(r^{\rho},\rho\varphi) |  |

is holomorphic, and the map 𝐦: 𝐋 2 ⟶ 𝐋 \mathbf{m}:\mathbf{L}^{2}\longrightarrow\mathbf{L} defined by

 | 𝐦 ⁡ ( ( r 1, φ 1), ( r 2, φ 2)):= ( r 1 ​ r 2, φ 1 + φ 2) \mathbf{m}((r_{1},\varphi_{1}),(r_{2},\varphi_{2})):=(r_{1}r_{2},\varphi_{1}+\varphi_{2}) |  |

is holomorphic. Note that for all x, x 1, x 2 ∈ 𝐋 x,x_{1},x_{2}\in\mathbf{L}, we have ( 𝐩 ρ ​ ( x)) 1 = x ρ (\mathbf{p}^{\rho}(x))^{1}=x^{\rho} for each ρ > 0 \rho>0 and ( 𝐦 ⁡ ( x 1, x 2)) 1 = ( x 1) 1 ⋅ ( x 2) 1 (\mathbf{m}(x_{1},x_{2}))^{1}=(x_{1})^{1}\cdot(x_{2})^{1}.

If m ≥ 2 m\geq 2 and ρ ∈ ( 0, ∞) m \rho\in(0,\infty)^{m}, we define the holomorphic map 𝐩 ρ: 𝐋 m ⟶ 𝐋 \mathbf{p}^{\rho}:\mathbf{L}^{m}\longrightarrow\mathbf{L} by induction on m m:

 | 𝐩 ρ ​ ( x):= 𝐦 ⁡ ( 𝐩 ρ ′ ​ ( x ′), 𝐩 ρ m ​ ( x m)), \mathbf{p}^{\rho}(x):=\mathbf{m}\left(\mathbf{p}^{\rho^{\prime}}(x^{\prime}),\mathbf{p}^{\rho_{m}}(x_{m})\right), |  |

where x ′:= ( x 1, …, x m − 1) x^{\prime}:=(x_{1},\dots,x_{m-1}) and ρ ′:= ( ρ 1, …, ρ m − 1) \rho^{\prime}:=(\rho_{1},\dots,\rho_{m-1}).

###### Definition 4.1.

Let m ≥ 2 m\geq 2 and i, j ∈ { 1, …, m } i,j\in\{1,\dots,m\} be such that i ≠ j i\neq j, and let ρ > 0 \rho>0. The singular blowing-up 𝐬 i ​ j ρ: 𝐋 m + n ⟶ 𝐋 m + n \mathbf{s}^{\rho}_{ij}:\mathbf{L}^{m+n}\longrightarrow\mathbf{L}^{m+n} is defined as 𝐬 i ​ j ρ ​ ( x, y) = ( z, y) \mathbf{s}^{\rho}_{ij}(x,y)=(z,y), where

 | z k:= { x k if ​ k ≠ i, 𝐦 ⁡ ( 𝐩 ρ ​ ( x j), x i) if ​ k = i. z_{k}:=\begin{cases}x_{k}&\text{if }k\neq i,\\ \mathbf{m}(\mathbf{p}^{\rho}(x_{j}),x_{i})&\text{if }k=i.\end{cases} |  |

###### Proposition 4.2.

Let m ≥ 2 m\geq 2 and f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U). Then the there is an m m -quadratic V ⊆ 𝐋 m + n V\subseteq\mathbf{L}^{m+n} such that 𝐬 i ​ j ρ ​ ( V) ⊆ U \mathbf{s}^{\rho}_{ij}(V)\subseteq U and the function f ∘ 𝐬 i ​ j ρ f\circ\mathbf{s}^{\rho}_{ij} belongs to 𝒜 m ​ ( V) \mathcal{A}_{m}(V) and satisfies T ⁡ ( f ∘ 𝐬 i ​ j ρ) = 𝐁 i ​ j ρ, 0 ​ ( T ​ f) T\left(f\circ\mathbf{s}^{\rho}_{ij}\right)=\mathbf{B}^{\rho,0}_{ij}(Tf).

###### Proof.

Without loss of generality, we may assume that i = m i=m and j = m − 1 j=m-1. Below, we write 𝐬 \mathbf{s} and 𝐁 \mathbf{B} in place of 𝐬 i ​ j ρ \mathbf{s}^{\rho}_{ij} and 𝐁 i ​ j ρ, 0 \mathbf{B}^{\rho,0}_{ij}. Let W ⊆ 𝐋 W\subseteq\mathbf{L} be quadratic and 1 > R > 0 1>R>0 be such that f ∈ 𝒜 m ​ ( W m × B 𝐋 ​ ( R) n) f\in\mathcal{A}_{m}(W^{m}\times B_{\mathbf{L}}(R)^{n}); we may assume that

 | W = { ( r, φ) ∈ 𝐋: 0 < r < c ​ exp ⁡ ( − C ​ | φ |) } W=\left\{(r,\varphi)\in\mathbf{L}:\ 0<r<c\exp\left(-C\sqrt{|\varphi|}\right)\right\} |  |

for some c, C > 0 c,C>0 satisfying c < R c<R. We let D:= C / min ⁡ { ρ, 1 } D:=C/\min\{\sqrt{\rho},1\} and put

 | W ′:= { ( r, φ) ∈ 𝐋: 0 < r < c ​ exp ⁡ ( − D ​ | φ |) } ⊆ W W^{\prime}:=\left\{(r,\varphi)\in\mathbf{L}:\ 0<r<c\exp\left(-D\sqrt{|\varphi|}\right)\right\}\subseteq W |  |

and V:= ( W ′) m × B 𝐋 ​ ( R) n V:=(W^{\prime})^{m}\times B_{\mathbf{L}}(R)^{n}; we claim that 𝐬 ⁡ ( V) ⊆ U \mathbf{s}(V)\subseteq U. To see this, we write x k = ( r k, φ k) x_{k}=(r_{k},\varphi_{k}) for k = 1, …, m k=1,\dots,m. Then

 | ‖ ( 𝐬 ⁡ ( x)) m ‖ \displaystyle\left\|\left(\mathbf{s}(x)\right)_{m}\right\| | ≤ c ρ + 1 ​ exp ⁡ ( − D ⁡ ( ρ ​ | φ m − 1 | + | φ m |)) \displaystyle\leq c^{\rho+1}\exp\left(-D\left(\rho\sqrt{|\varphi_{m-1}|}+\sqrt{|\varphi_{m}|}\right)\right) |  |

 |  | ≤ c ​ exp ⁡ ( − D ⁡ ( ρ ​ | φ m − 1 | + | φ m |)); \displaystyle\leq c\exp\left(-D\left(\rho\sqrt{|\varphi_{m-1}|}+\sqrt{|\varphi_{m}|}\right)\right); |  |

since

 | C ​ | ρ ​ φ m − 1 + φ m | \displaystyle C\sqrt{|\rho\varphi_{m-1}+\varphi_{m}|} | ≤ C ⁡ ( ρ ​ | φ m − 1 | + | φ m |) \displaystyle\leq C\left(\sqrt{\rho}\sqrt{|\varphi_{m-1}|}+\sqrt{|\varphi_{m}|}\right) |  |

 |  | ≤ D ⁡ ( ρ ​ | φ m − 1 | + | φ m |), \displaystyle\leq D\left(\rho\sqrt{|\varphi_{m-1}|}+\sqrt{|\varphi_{m}|}\right), |  |

the claim follows.

Since f ∘ 𝐬 f\circ\mathbf{s} is holomorphic on V V, for each β ∈ ℕ n \beta\in\mathbb{N}^{n} the function a β: ( W ′) m ⟶ ℂ a_{\beta}:(W^{\prime})^{m}\longrightarrow\mathbb{C} defined by

 | a β ​ ( x ′):= 1 β! ​ ( ∂ β f ∂ y β ∘ 𝐬) ​ ( x, 0) a_{\beta}(x^{\prime}):=\frac{1}{\beta!}\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}\circ\mathbf{s}\right)(x,0) |  |

is holomorphic. By Proposition 2.15, it suffices to show that a β ∈ 𝒜 ⁡ ( ( W ′) m) a_{\beta}\in\mathcal{A}((W^{\prime})^{m}) for each β \beta. We fix β ∈ ℕ n \beta\in\mathbb{N}^{n} and write T ⁡ ( ∂ β f ∂ y β ​ ( X, 0)) = ∑ a α ​ X α T\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}(X,0)\right)=\sum a_{\alpha}X^{\alpha}, and we let 𝐚 > 0 \mathbf{a}>0. Shrinking W W and W ′ W^{\prime} if necessary, we may assume by Lemma 3.6 that

(4.1) |  | ‖ ∂ β f ∂ y β ​ ( x, 0) − ∑ | α | ≤ 𝐚 a α ​ x α ‖ = o ⁡ ( ‖ x ‖ 𝐚) as ​ ‖ x ‖ → 0 ​ in ​ W m. \left\|\frac{\partial^{\beta}f}{\partial y^{\beta}}(x,0)-\sum_{|\alpha|\leq\mathbf{a}}a_{\alpha}x^{\alpha}\right\|=o\left(\|x\|^{\mathbf{a}}\right)\quad\text{as }\|x\|\to 0\text{ in }W^{m}. |  |

We now define ρ: [0, ∞) m ⟶ [0, ∞) m \rho:[0,\infty)^{m}\longrightarrow[0,\infty)^{m} by

 | ρ ⁡ ( α):= ( α 1, …, α m − 2, α m − 1 + ρ ​ α m, α m). \rho(\alpha):=(\alpha_{1},\dots,\alpha_{m-2},\alpha_{m-1}+\rho\alpha_{m},\alpha_{m}). |  |

Note that 𝐁 ⁡ ( T ⁡ ( ∂ β f / ∂ Y β)) ​ ( X, 0) = ∑ a α ​ X ρ ⁡ ( α) \mathbf{B}(T(\partial^{\beta}f/\partial Y^{\beta}))(X,0)=\sum a_{\alpha}X^{\rho(\alpha)} and 𝐬 ​ ( x) α = x ρ ⁡ ( α) \mathbf{s}(x)^{\alpha}=x^{\rho(\alpha)} for all x ∈ ( W ′) m x\in(W^{\prime})^{m} and α ∈ [0, ∞) m \alpha\in[0,\infty)^{m}. Since W ⊆ B 𝐋 ​ ( 1) W\subseteq B_{\mathbf{L}}(1), we have ‖ 𝐬 ⁡ ( x) ‖ ≤ ‖ x ‖ \|\mathbf{s}(x)\|\leq\|x\|, so it follows from ( 4.1) that

(4.2) |  | ‖ ( ∂ β f ∂ y β ∘ 𝐬) ​ ( x, 0) − ∑ | α | ≤ 𝐚 a α ​ x ρ ⁡ ( α) ‖ = o ⁡ ( ‖ x ‖ 𝐚) \left\|\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}\circ\mathbf{s}\right)(x,0)-\sum_{|\alpha|\leq\mathbf{a}}a_{\alpha}x^{\rho(\alpha)}\right\|=o\left(\|x\|^{\mathbf{a}}\right) |  |

as ‖ x ‖ → 0 \|x\|\to 0 in ( W ′) m (W^{\prime})^{m}. Finally, for x ∈ W m x\in W^{m} we have

 | ‖ ( ∂ β f ∂ y β ∘ 𝐬) ​ ( x, 0) − ∑ | ρ ⁡ ( α) | ≤ 𝐚 a α ​ x ρ ⁡ ( α) ‖ ≤ ‖ ( ∂ β f ∂ y β ∘ 𝐬) ​ ( x, 0) − ∑ | α | ≤ 𝐚 a α ​ x ρ ⁡ ( α) ‖ + ‖ ∑ | α | ≤ 𝐚 < | ρ ⁡ ( α) | a α ​ x ρ ⁡ ( α) ‖. \left\|\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}\circ\mathbf{s}\right)(x,0)-\sum_{|\rho(\alpha)|\leq\mathbf{a}}a_{\alpha}x^{\rho(\alpha)}\right\|\\ \leq\left\|\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}\circ\mathbf{s}\right)(x,0)-\sum_{|\alpha|\leq\mathbf{a}}a_{\alpha}x^{\rho(\alpha)}\right\|+\left\|\sum_{|\alpha|\leq\mathbf{a}<|\rho(\alpha)|}a_{\alpha}x^{\rho(\alpha)}\right\|. |  |

The right-hand side above is o ⁡ ( ‖ x ‖ 𝐚) o\left(\|x\|^{\mathbf{a}}\right) as ‖ x ‖ → 0 \|x\|\to 0 in ( W ′) m (W^{\prime})^{m}, by ( 4.2) and because the sum in the second summand is finite and each of its summands has an exponent γ \gamma satisfying | γ | > 𝐚 |\gamma|>\mathbf{a}. This proves the proposition. ∎

###### Definition 4.3.

Let m ≥ 2 m\geq 2 and λ > 0 \lambda>0. The regular blowing-up 𝐫 ρ, λ: 𝐋 m − 1 × B 𝐋 ​ ( λ) × 𝐋 n ⟶ 𝐋 m + n \mathbf{r}^{\rho,\lambda}:\mathbf{L}^{m-1}\times B_{\mathbf{L}}(\lambda)\times\mathbf{L}^{n}\longrightarrow\mathbf{L}^{m+n} is defined as 𝐫 ρ, λ ​ ( x, y) = ( z, y) \mathbf{r}^{\rho,\lambda}(x,y)=(z,y), where

 | z k:= { x k if ​ k < m, 𝐦 ⁡ ( 𝐩 ρ ​ ( x m − 1), 𝐭 λ ​ ( x m)) if ​ k = m. z_{k}:=\begin{cases}x_{k}&\text{if }k<m,\\ \mathbf{m}\left(\mathbf{p}^{\rho}(x_{m-1}),\mathbf{t}_{\lambda}(x_{m})\right)&\text{if }k=m.\end{cases} |  |

###### Proposition 4.4.

Let m ≥ 2 m\geq 2, λ > 0 \lambda>0 and f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U). Then there is an ( m − 1) (m-1) -quadratic V ⊆ 𝐋 m − 1 × B 𝐋 ​ ( λ) × 𝐋 n V\subseteq\mathbf{L}^{m-1}\times B_{\mathbf{L}}(\lambda)\times\mathbf{L}^{n} such that 𝐫 ρ, λ ​ ( V) ⊆ U \mathbf{r}^{\rho,\lambda}(V)\subseteq U and the function f ∘ 𝐫 ρ, λ: V ⟶ ℂ f\circ\mathbf{r}^{\rho,\lambda}:V\longrightarrow\mathbb{C} belongs to 𝒜 m − 1 ​ ( V) \mathcal{A}_{m-1}(V) and satisfies T ⁡ ( f ∘ 𝐫 ρ, λ) = 𝐁 m, m − 1 ρ, λ ​ ( T ​ f) T\left(f\circ\mathbf{r}^{\rho,\lambda}\right)=\mathbf{B}^{\rho,\lambda}_{m,m-1}(Tf).

###### Proof.

Below, we write 𝐫 \mathbf{r} and 𝐁 \mathbf{B} in place of 𝐫 ρ, λ \mathbf{r}^{\rho,\lambda} and 𝐁 m, m − 1 ρ, λ \mathbf{B}^{\rho,\lambda}_{m,m-1}. Let W ′ ⊆ 𝐋 W^{\prime}\subseteq\mathbf{L} be quadratic and min ⁡ { 1, λ } > R > 0 \min\{1,\lambda\}>R>0 be such that U ′:= ( W ′) m × B 𝐋 ​ ( R) n ⊆ U U^{\prime}:=(W^{\prime})^{m}\times B_{\mathbf{L}}(R)^{n}\subseteq U; we may assume that

 | W ′ = { ( r, φ) ∈ 𝐋: 0 < r < c ​ exp ⁡ ( − C ​ | φ |) } W^{\prime}=\left\{(r,\varphi)\in\mathbf{L}:\ 0<r<c\exp\left(-C\sqrt{|\varphi|}\right)\right\} |  |

for some c, C > 0 c,C>0 satisfying c < R c<R. We let

 | D:= C min ⁡ { ρ, 1 } and d:= min ⁡ { c, ( c 2 ​ λ ​ exp ⁡ ( D ​ π / 2)) 1 / ρ }, D:=\frac{C}{\min\{\sqrt{\rho},1\}}\quad\text{and}\quad d:=\min\left\{c,\left(\frac{c}{2\lambda\exp\left(D\sqrt{\pi/2}\right)}\right)^{1/\rho}\right\}, |  |

and we put

 | W:= { ( r, φ) ∈ 𝐋: 0 < r < d ​ exp ⁡ ( − D ​ | φ |) } ⊆ W ′ W:=\left\{(r,\varphi)\in\mathbf{L}:\ 0<r<d\exp\left(-D\sqrt{|\varphi|}\right)\right\}\subseteq W^{\prime} |  |

and V:= W m − 1 × B 𝐋 ​ ( R) n + 1 V:=W^{m-1}\times B_{\mathbf{L}}(R)^{n+1}; we claim that 𝐫 ⁡ ( V) ⊆ U \mathbf{r}(V)\subseteq U. To see this, we write x k = ( r k, φ k) x_{k}=(r_{k},\varphi_{k}) for k = 1, …, m k=1,\dots,m. Then

 | ‖ ( 𝐫 ⁡ ( x)) m ‖ \displaystyle\left\|\left(\mathbf{r}(x)\right)_{m}\right\| | ≤ d ρ ​ exp ⁡ ( − D ​ ρ ​ | φ m − 1 |) ⋅ 2 ​ λ \displaystyle\leq d^{\rho}\exp\left(-D\rho\sqrt{|\varphi_{m-1}|}\right)\cdot 2\lambda |  |

 |  | ≤ c ​ exp ⁡ ( − D ⁡ ( ρ ​ | φ m − 1 | + π / 2)). \displaystyle\leq c\exp\left(-D\left(\rho\sqrt{|\varphi_{m-1}|}+\sqrt{\pi/2}\right)\right). |  |

Since | arg ⁡ ( 𝐭 λ ​ ( w)) | ≤ π / 2 |\arg(\mathbf{t}_{\lambda}(w))|\leq\pi/2 for all w ∈ 𝐋 w\in\mathbf{L}, we also get

 | C ​ | ρ ​ φ m − 1 + arg ⁡ ( 𝐭 λ ​ ( x m)) | \displaystyle C\sqrt{|\rho\varphi_{m-1}+\arg(\mathbf{t}_{\lambda}(x_{m}))|} | ≤ C ⁡ ( ρ ​ | φ m − 1 | + π / 2) \displaystyle\leq C\left(\sqrt{\rho}\sqrt{|\varphi_{m-1}|}+\sqrt{\pi/2}\right) |  |

 |  | ≤ D ⁡ ( ρ ​ | φ m − 1 | + π / 2). \displaystyle\leq D\left(\rho\sqrt{|\varphi_{m-1}|}+\sqrt{\pi/2}\right). |  |

The claim follows.

We write x ′:= ( x 1, …, x m − 1) x^{\prime}:=(x_{1},\dots,x_{m-1}) for x ∈ 𝐋 m x\in\mathbf{L}^{m}. Since f ∘ 𝐫 f\circ\mathbf{r} is holomorphic on V V, for each p ∈ ℕ p\in\mathbb{N} and each β ∈ ℕ n \beta\in\mathbb{N}^{n} the function a ( p, β): ( W ′) m − 1 ⟶ ℂ a_{(p,\beta)}:(W^{\prime})^{m-1}\longrightarrow\mathbb{C} defined by

 | a ( p, β) ​ ( x ′):= 1 p! ​ β! ​ ∂ p ( ( ∂ f / ∂ y β) ∘ 𝐫) ∂ x m p ​ ( x ′, λ, 0) a_{(p,\beta)}(x^{\prime}):=\frac{1}{p!\beta!}\frac{\partial^{p}((\partial f/\partial y^{\beta})\circ\mathbf{r})}{\partial x_{m}^{p}}(x^{\prime},\lambda,0) |  |

is holomorphic. Moreover, we put X ′:= ( X 1, …, X m − 1) X^{\prime}:=(X_{1},\dots,X_{m-1}), and α ′:= ( α 1, …, α m − 1) \alpha^{\prime}:=(\alpha_{1},\dots,\alpha_{m-1}), and we fix p ∈ ℕ p\in\mathbb{N} and β ∈ ℕ n \beta\in\mathbb{N}^{n} and write T ⁡ ( ∂ β f ∂ y β ​ ( X, 0)) = ∑ a α ​ X α T\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}(X,0)\right)=\sum a_{\alpha}X^{\alpha}. By the above and Proposition 2.15, it now suffices to show that a ( p, β) ∈ 𝒜 ⁡ ( ( W ′) m − 1) a_{(p,\beta)}\in\mathcal{A}((W^{\prime})^{m-1}) with T ​ a ( p, β) = 1 β! ​ A ( p, β) Ta_{(p,\beta)}=\frac{1}{\beta!}A_{(p,\beta)}, where

 | A ( p, β) ​ ( X ′):= ∑ α ( α m p) ​ λ α m − p ​ a α ​ ( X ′) α ′ ​ X m − 1 ρ ​ α m. A_{(p,\beta)}(X^{\prime}):=\sum_{\alpha}\begin{pmatrix}\alpha_{m}\\ p\end{pmatrix}\lambda^{\alpha_{m}-p}a_{\alpha}(X^{\prime})^{\alpha^{\prime}}X_{m-1}^{\rho\alpha_{m}}. |  |

Let 𝐚 > 0 \mathbf{a}>0, and choose 𝐚 ′ > 𝐚 / min ⁡ { ρ, 1 } \mathbf{a}^{\prime}>\mathbf{a}/\min\{\rho,1\}. Shrinking W W and W ′ W^{\prime} if necessary, we may assume by Lemma 3.6 that

 | ‖ ∂ β f ∂ y β ​ ( x, 0) − ∑ | α | ≤ 𝐚 ′ a α ​ x α ‖ = o ⁡ ( ‖ x ‖ 𝐚 ′) as ​ ‖ x ‖ → 0 ​ in ​ W m. \left\|\frac{\partial^{\beta}f}{\partial y^{\beta}}(x,0)-\sum_{|\alpha|\leq\mathbf{a}^{\prime}}a_{\alpha}x^{\alpha}\right\|=o\left(\|x\|^{\mathbf{a}^{\prime}}\right)\quad\text{as }\|x\|\to 0\text{ in }W^{m}. |  |

Therefore,

(4.3) |  | ‖ ( ∂ β f ∂ y β ∘ 𝐫) ​ ( x, 0) − ∑ | α | ≤ 𝐚 ′ a α ⋅ ( 𝐫 ⁡ ( x)) α ‖ = o ⁡ ( ‖ 𝐫 ⁡ ( x) ‖ 𝐚 ′) \left\|\left(\frac{\partial^{\beta}f}{\partial y^{\beta}}\circ\mathbf{r}\right)(x,0)-\sum_{|\alpha|\leq\mathbf{a}^{\prime}}a_{\alpha}\cdot(\mathbf{r}(x))^{\alpha}\right\|=o\left(\|\mathbf{r}(x)\|^{\mathbf{a}^{\prime}}\right) |  |

as ‖ x ‖ → 0 \|x\|\to 0 in ( W ′) m (W^{\prime})^{m}. We now define ρ: [0, ∞) m ⟶ [0, ∞) m − 1 \rho:[0,\infty)^{m}\longrightarrow[0,\infty)^{m-1} by ρ ⁡ ( α):= ( α 1, …, α m − 2, α m − 1 + ρ ​ α m) \rho(\alpha):=(\alpha_{1},\dots,\alpha_{m-2},\alpha_{m-1}+\rho\alpha_{m}). Note that formally A ( p, β) ​ ( X ′) = ∑ α ( α m p) ​ λ α m − p ​ a α ​ ( X ′) ρ ⁡ ( α) A_{(p,\beta)}(X^{\prime})=\sum_{\alpha}\begin{pmatrix}\alpha_{m}\\ p\end{pmatrix}\lambda^{\alpha_{m}-p}a_{\alpha}(X^{\prime})^{\rho(\alpha)}, and for all x ∈ ( W ′) m x\in(W^{\prime})^{m} and α ∈ [0, ∞) m \alpha\in[0,\infty)^{m} that 𝐫 ​ ( x) α = ( x ′) ρ ⁡ ( α) ⋅ ∑ q ∈ ℕ ( α m q) ​ λ α m − q ​ x m q \mathbf{r}(x)^{\alpha}=(x^{\prime})^{\rho(\alpha)}\cdot\sum_{q\in\mathbb{N}}\begin{pmatrix}\alpha_{m}\\ q\end{pmatrix}\lambda^{\alpha_{m}-q}x_{m}^{q}. Differentiating ( 4.3), it follows from the Cauchy estimates and our choice of 𝐚 ′ \mathbf{a}^{\prime} that

 | ‖ β! ⋅ a ( p, β) ​ ( x ′) − ∑ | α | ≤ 𝐚 ′ ( α m p) ​ λ α m − p ​ a α ​ ( x ′) ρ ⁡ ( α) ‖ = o ⁡ ( ‖ x ′ ‖ 𝐚) \left\|\beta!\cdot a_{(p,\beta)}(x^{\prime})-\sum_{|\alpha|\leq\mathbf{a}^{\prime}}\begin{pmatrix}\alpha_{m}\\ p\end{pmatrix}\lambda^{\alpha_{m}-p}a_{\alpha}(x^{\prime})^{\rho(\alpha)}\right\|=o\left(\|x^{\prime}\|^{\mathbf{a}}\right) |  |

as ‖ x ′ ‖ → 0 \|x^{\prime}\|\to 0 in ( W ′) m − 1 (W^{\prime})^{m-1}. Finally, for x ′ ∈ ( W ′) m − 1 x^{\prime}\in(W^{\prime})^{m-1} we have

 | ‖ β! ⋅ a ( p, β) ​ ( x ′) − ∑ | ρ ⁡ ( α) | ≤ 𝐚 ( α m p) ​ λ α m − p ​ a α ​ ( x ′) ρ ⁡ ( α) ‖ ≤ ‖ β! ⋅ a ( p, β) ​ ( x ′) − ∑ | α | ≤ 𝐚 ′ ( α m p) ​ λ α m − p ​ a α ​ ( x ′) ρ ⁡ ( α) ‖ + ‖ ∑ | α | ≤ 𝐚 ′ | ρ ⁡ ( α) | > 𝐚 ( α m p) ​ λ α m − p ​ a α ​ ( x ′) ρ ⁡ ( α) ‖. \left\|\beta!\cdot a_{(p,\beta)}(x^{\prime})-\sum_{|\rho(\alpha)|\leq\mathbf{a}}\begin{pmatrix}\alpha_{m}\\ p\end{pmatrix}\lambda^{\alpha_{m}-p}a_{\alpha}(x^{\prime})^{\rho(\alpha)}\right\|\\ \leq\left\|\beta!\cdot a_{(p,\beta)}(x^{\prime})-\sum_{|\alpha|\leq\mathbf{a}^{\prime}}\begin{pmatrix}\alpha_{m}\\ p\end{pmatrix}\lambda^{\alpha_{m}-p}a_{\alpha}(x^{\prime})^{\rho(\alpha)}\right\|\\ +\left\|\sum_{\begin{subarray}{c}|\alpha|\leq\mathbf{a}^{\prime}\\ |\rho(\alpha)|>\mathbf{a}\end{subarray}}\begin{pmatrix}\alpha_{m}\\ p\end{pmatrix}\lambda^{\alpha_{m}-p}a_{\alpha}(x^{\prime})^{\rho(\alpha)}\right\|. |  |

The right-hand side above is o ⁡ ( ‖ x ′ ‖ 𝐚) o\left(\|x^{\prime}\|^{\mathbf{a}}\right) as ‖ x ′ ‖ → 0 \|x^{\prime}\|\to 0 in ( W ′) m − 1 (W^{\prime})^{m-1}, by ( 4.3) and because the sum in the second summand is finite and each of its summands has an exponent β \beta satisfying | β | > 𝐚 |\beta|>\mathbf{a}, as | ρ ⁡ ( α) | ≥ | α | ​ min ⁡ { ρ, 1 } |\rho(\alpha)|\geq|\alpha|\min\{\rho,1\} for all α \alpha. This proves the proposition. ∎

## 5. The class 𝒬 \mathcal{Q}

Let m, n ∈ ℕ m,n\in\mathbb{N}, and let U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} be an m m -quadratic domain. Below, we let y = ( y 1, …, y n) y=(y_{1},\dots,y_{n}) range over 𝐋 n \mathbf{L}^{n} and Y = ( Y 1, …, Y n) Y=(Y_{1},\dots,Y_{n}) be indeterminates.

With Remarks 3.3 and 3.8 in mind, we now restrict our attention to a subclass of 𝒜 m ​ ( U) \mathcal{A}_{m}(U). Abusing notation, we identify [0, ∞) [0,\infty) with the set { 0 } ∪ ( 0, ∞) 𝐋 ⊆ 𝐋 0 \{0\}\cup(0,\infty)_{\mathbf{L}}\subseteq\mathbf{L}_{0}.

###### Definition 5.1.

We define the class 𝒬 m m + n ​ ( U) \mathcal{Q}^{m+n}_{m}(U) to be the set of all f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U) such that for every γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m},

- (TD)

there are an m m -quadratic V = V ⁡ ( f, γ) ⊆ U V=V(f,\gamma)\subseteq U and an f ( γ, 0) ∈ 𝒜 m ​ ( V) f_{(\gamma,0)}\in\mathcal{A}_{m}(V) such that T ​ f ( γ, 0) = ( T ​ f) ( γ, 0) Tf_{(\gamma,0)}=(Tf)_{(\gamma,0)};

- (TE)

for every κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} with ( κ, 0) ∈ cl 0 ⁡ ( U) (\kappa,0)\in\cl_{0}(U), there is an m m -quadratic W = W ⁡ ( f ( γ, 0), κ) ⊆ 𝐋 m + n W=W(f_{(\gamma,0)},\kappa)\subseteq\mathbf{L}^{m+n} such that ( 𝐭 κ ​ ( x), y) ∈ V (\mathbf{t}_{\kappa}(x),y)\in V for all ( x, y) ∈ W (x,y)\in W and the function 𝐭 ( κ, 0) ​ f ( γ, 0): W ⟶ ℂ \mathbf{t}_{(\kappa,0)}f_{(\gamma,0)}:W\longrightarrow\mathbb{C} defined by ( 𝐭 ( κ, 0) ​ f ( γ, 0)) ​ ( x, y):= f ( γ, 0) ​ ( 𝐭 κ ​ ( x), y) (\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)})(x,y):=f_{(\gamma,0)}(\mathbf{t}_{\kappa}(x),y) belongs to 𝒜 m ​ ( W) \mathcal{A}_{m}(W).

We shall omit the superscript m + n m+n whenever clear from context.

###### Remarks 5.2.

1. (1)

By Proposition 2.8, for each f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U) and each γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, the function f ( γ, 0) f_{(\gamma,0)} in the definition above is unique in 𝒜 m ​ ( V ​ ( f, γ)) \mathcal{A}_{m}(V(f,\gamma)).

2. (2)

Let f: U ⟶ ℂ f:U\longrightarrow\mathbb{C} be holomorphic, and let V ⊆ U V\subseteq U be an m m -quadratic domain. Then by Remark 2.7 (2) and the above definition, f | V ∈ 𝒬 m ​ ( V) f|_{V}\in\mathcal{Q}_{m}(V) iff f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U).

3. (3)

By definition, the collection 𝒬 1 ​ ( U) \mathcal{Q}_{1}(U) is equal to the set of all f ∈ 𝒜 1 ​ ( U) f\in\mathcal{A}_{1}(U) such that (TD) holds for every γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}; in particular, 𝒬 1 1 ​ ( U) = 𝒜 1 1 ​ ( U) \mathcal{Q}^{1}_{1}(U)=\mathcal{A}^{1}_{1}(U). Moreover, 𝒜 0 ​ ( U) = 𝒬 0 ​ ( U) \mathcal{A}_{0}(U)=\mathcal{Q}_{0}(U) by Proposition 3.2 and Corollary 3.7.

4. (4)

Let σ \sigma be a permutation of { 1, …, m } \{1,\dots,m\} and τ \tau be a permutation of { 1, …, n } \{1,\dots,n\}, and let f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U). Then f ∘ σ f\circ\sigma and f ∘ τ f\circ\tau belong to 𝒬 m ​ ( U) \mathcal{Q}_{m}(U).

For p ∈ ℕ p\in\mathbb{N} and q ∈ { 1, …, p } q\in\{1,\dots,p\}, we say that ρ ∈ [0, ∞) p \rho\in[0,\infty)^{p} is q q -zero if ρ 1 = ⋯ = ρ q = 0 \rho_{1}=\cdots=\rho_{q}=0 and ρ q + 1, …, ρ p > 0 \rho_{q+1},\dots,\rho_{p}>0. From Proposition 2.11, we obtain:

###### Corollary 5.3.

Let f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U), and let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, k ∈ { 1, …, m } k\in\{1,\dots,m\}, κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be k k -zero such that ( κ, 0) ∈ cl 0 ⁡ ( U) (\kappa,0)\in\cl_{0}(U) and σ \sigma a permutation of { 1, …, m } \{1,\dots,m\}. Then there is a k k -quadratic domain W ⊆ 𝐋 m + n W\subseteq\mathbf{L}^{m+n} such that σ ⁡ ( 𝐭 κ ​ ( x), y) ∈ V ⁡ ( f, γ) \sigma(\mathbf{t}_{\kappa}(x),y)\in V(f,\gamma) for all ( x, y) ∈ W (x,y)\in W and the function 𝐭 ( κ, 0) ​ ( f ( γ, 0) ∘ σ) \mathbf{t}_{(\kappa,0)}(f_{(\gamma,0)}\circ\sigma) belongs to 𝒜 k ​ ( W) \mathcal{A}_{k}(W). ∎

###### Definition 5.4.

Let ℰ m m + n \mathcal{E}^{m+n}_{m} be the union of all 𝒬 m ​ ( U) \mathcal{Q}_{m}(U) as U U ranges over the m m -quadratic domains in 𝐋 m + n \mathbf{L}^{m+n}. We define an equivalence relation ≡ \equiv on ℰ m m + n \mathcal{E}^{m+n}_{m} as follows: f ≡ g f\equiv g if and only of there is an m m -quadratic domain U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} such that f | U = g | U f|_{U}=g|_{U}. We let 𝒬 m m + n \mathcal{Q}^{m+n}_{m} be the set of all ≡ \equiv -equivalence classes.

We shall omit the superscript m + n m+n whenever it is clear from context. We will not distinguish between f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U) and its equivalence class in 𝒬 m \mathcal{Q}_{m}, which we also denote by f f. With this identification, whenever U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} is an m m -quadratic domain, we have 𝒬 m ​ ( U) ⊆ 𝒬 m \mathcal{Q}_{m}(U)\subseteq\mathcal{Q}_{m}. Moreover, for every f, g ∈ ℰ m f,g\in\mathcal{E}_{m} such that f ≡ g f\equiv g, we have T ​ f = T ​ g Tf=Tg; hence, the map f ↦ T ​ f: ℰ m ⟶ ℂ ⁡ [[X ∗, Y]] f\mapsto Tf:\mathcal{E}_{m}\longrightarrow\mathbb{C}[\![X^{*},Y]\!] induces a map f ↦ T ​ f: 𝒬 m ⟶ ℂ ⁡ [[X ∗, Y]] f\mapsto Tf:\mathcal{Q}_{m}\longrightarrow\mathbb{C}[\![X^{*},Y]\!]. Finally, for r ≥ 0 r\geq 0 we simply write x r x^{r} for the germ of the function x ↦ x r: 𝐋 ⟶ ℂ x\mapsto x^{r}:\mathbf{L}\longrightarrow\mathbb{C}.

###### Lemma 5.5.

1. (1)

Let f, g ∈ 𝒬 m f,g\in\mathcal{Q}_{m} and a ∈ ℂ a\in\mathbb{C}. Then f + g ∈ 𝒬 m f+g\in\mathcal{Q}_{m} and a ​ f ∈ 𝒬 m af\in\mathcal{Q}_{m}.

2. (2)

If m + n ≥ l ≥ m m+n\geq l\geq m, then 𝒬 m ⊆ 𝒬 l \mathcal{Q}_{m}\subseteq\mathcal{Q}_{l}.

3. (3)

Let f ∈ 𝒬 m f\in\mathcal{Q}_{m} and ( λ, μ) ∈ ( 0, ∞) m + n (\lambda,\mu)\in(0,\infty)^{m+n}. Then the function

 | f ⁡ ( 𝐦 ⁡ ( λ 1, x 1), …, 𝐦 ⁡ ( λ m, x m), 𝐦 ⁡ ( μ 1, y 1), …, 𝐦 ⁡ ( μ n, y n)) f(\mathbf{m}(\lambda_{1},x_{1}),\dots,\mathbf{m}(\lambda_{m},x_{m}),\mathbf{m}(\mu_{1},y_{1}),\dots,\mathbf{m}(\mu_{n},y_{n})) |  |

belongs to 𝒬 m \mathcal{Q}_{m}.

###### Proof.

(1) Let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}; then ( T ​ f) ( γ, 0) + ( T ​ g) ( γ, 0) = ( T ⁡ ( f + g)) ( γ, 0) (Tf)_{(\gamma,0)}+(Tg)_{(\gamma,0)}=(T(f+g))_{(\gamma,0)} and a ​ ( T ​ f) ( γ, 0) = T ​ ( a ​ f) ( γ, 0) a(Tf)_{(\gamma,0)}=T(af)_{(\gamma,0)}. Let also κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be sufficiently small. Then f ∘ 𝐭 ( κ, 0) + g ∘ 𝐭 ( κ, 0) = ( f + g) ∘ 𝐭 ( κ, 0) f\circ\mathbf{t}_{(\kappa,0)}+g\circ\mathbf{t}_{(\kappa,0)}=(f+g)\circ\mathbf{t}_{(\kappa,0)} and a ⁡ ( f ∘ 𝐭 ( κ, 0)) = ( a ​ f) ∘ 𝐭 ( κ, 0) a(f\circ\mathbf{t}_{(\kappa,0)})=(af)\circ\mathbf{t}_{(\kappa,0)}, so we define 𝐭 ( κ, 0) ​ ( f + g):= 𝐭 ( κ, 0) ​ f + 𝐭 ( κ, 0) ​ g \mathbf{t}_{(\kappa,0)}(f+g):=\mathbf{t}_{(\kappa,0)}f+\mathbf{t}_{(\kappa,0)}g and 𝐭 ( κ, 0) ​ ( a ​ f):= a ​ 𝐭 ( κ, 0) ​ f \mathbf{t}_{(\kappa,0)}(af):=a\mathbf{t}_{(\kappa,0)}f.

(2) Let m + n ≥ l ≥ m m+n\geq l\geq m, and let f ∈ 𝒬 m f\in\mathcal{Q}_{m} and ρ ∈ [0, ∞) l \rho\in[0,\infty)^{l}. Let also ρ ′ \rho^{\prime} be the least τ ∈ [0, ∞) m × ℕ l − m \tau\in[0,\infty)^{m}\times\mathbb{N}^{l-m} such that τ ≥ ρ \tau\geq\rho. Then we can take f ( ρ, 0):= ( x, y) ρ ′ − ρ ⋅ f ( ρ ′, 0) f_{(\rho,0)}:=(x,y)^{\rho^{\prime}-\rho}\cdot f_{(\rho^{\prime},0)}. It follows easily that f ∈ 𝒬 l f\in\mathcal{Q}_{l}.

(3) Writing 𝐦 ⁡ ( ( λ, μ), ( x, y)):= ( 𝐦 ⁡ ( λ 1, x 1), …, 𝐦 ⁡ ( μ n, y n)) \mathbf{m}((\lambda,\mu),(x,y)):=(\mathbf{m}(\lambda_{1},x_{1}),\dots,\mathbf{m}(\mu_{n},y_{n})), and writing ( λ, μ) ⋅ ( X, Y):= ( λ 1 ​ X 1, …, μ n ​ Y n) (\lambda,\mu)\cdot(X,Y):=(\lambda_{1}X_{1},\dots,\mu_{n}Y_{n}), we see that

 | T ​ f ​ ( ( λ, μ) ⋅ ( X, Y)) ( γ, 0) = ( T ​ f) ( γ, 0) ​ ( ( λ, μ) ⋅ ( X, Y)) Tf((\lambda,\mu)\cdot(X,Y))_{(\gamma,0)}=(Tf)_{(\gamma,0)}((\lambda,\mu)\cdot(X,Y)) |  |

for all γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, and that

 | 𝐭 ( κ, 0) ​ ( f ⁡ ( 𝐦 ⁡ ( ( λ, μ), ( x, y)))) = ( 𝐭 ( λ ​ κ, 0) ​ f) ​ ( 𝐦 ⁡ ( ( λ, μ), ( x, y))) \mathbf{t}_{(\kappa,0)}(f(\mathbf{m}((\lambda,\mu),(x,y))))=(\mathbf{t}_{(\lambda\kappa,0)}f)(\mathbf{m}((\lambda,\mu),(x,y))) |  |

for all sufficiently small ( x, y) ∈ 𝐋 m + n (x,y)\in\mathbf{L}^{m+n}, where λ ​ κ:= ( λ 1 ​ κ 1, …, λ m ​ κ m) \lambda\kappa:=(\lambda_{1}\kappa_{1},\dots,\lambda_{m}\kappa_{m}). Part (3) follows. ∎

###### Proposition 5.6.

Let f ∈ 𝒬 m f\in\mathcal{Q}_{m}.

1. (1)

For every elementary set S ⊆ [0, ∞) m × ℕ n S\subseteq[0,\infty)^{m}\times\mathbb{N}^{n}, there is a unique f S ∈ 𝒬 m f_{S}\in\mathcal{Q}_{m} such that T ⁡ ( f S) = ( T ​ f) S T(f_{S})=(Tf)_{S}.

2. (2)

For every k ∈ { 1, …, m } k\in\{1,\dots,m\}, every sufficiently small k k -zero ( κ, λ) ∈ [0, ∞) m × ℝ n (\kappa,\lambda)\in[0,\infty)^{m}\times\mathbb{R}^{n} and every permutation σ \sigma of { 1, …, m } \{1,\dots,m\}, the function 𝐭 ( κ, λ) σ ​ f:= f ∘ σ ∘ 𝐭 ( κ, λ) \mathbf{t}^{\sigma}_{(\kappa,\lambda)}f:=f\circ\sigma\circ\mathbf{t}_{(\kappa,\lambda)} belongs to 𝒬 k \mathcal{Q}_{k}.

###### Proof.

(1) By Remark 1.8 and Lemmas 1.10 and 5.5, it suffices to consider S = { ( ( α, β) ∈ [0, ∞) m × ℕ n: ( α, β) ≥ ( γ, δ) } S=\left\{((\alpha,\beta)\in[0,\infty)^{m}\times\mathbb{N}^{n}:\ (\alpha,\beta)\geq(\gamma,\delta)\right\} for some ( γ, δ) ∈ [0, ∞) m × ℕ n (\gamma,\delta)\in[0,\infty)^{m}\times\mathbb{N}^{n}. By Lemma 5.5 and Proposition 2.8, we may even assume that either γ = 0 \gamma=0 or δ = 0 \delta=0. We assume first that δ = 0 \delta=0 and let f ( γ, 0) f_{(\gamma,0)} be as in (TD); we need to show that f ( γ, 0) ∈ 𝒬 m f_{(\gamma,0)}\in\mathcal{Q}_{m}. So let γ ′ ∈ [0, ∞) m \gamma^{\prime}\in[0,\infty)^{m} and κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be sufficiently small. Since ( T ​ f) ( γ + γ ′, 0) = ( T ​ f ( γ, 0)) ( γ ′, 0) (Tf)_{(\gamma+\gamma^{\prime},0)}=(Tf_{(\gamma,0)})_{(\gamma^{\prime},0)}, we can take ( f ( γ, 0)) ( γ ′, 0):= f ( γ + γ ′, 0) (f_{(\gamma,0)})_{(\gamma^{\prime},0)}:=f_{(\gamma+\gamma^{\prime},0)} and 𝐭 ( κ, 0) ​ ( ( f ( γ, 0)) ( γ ′, 0)):= 𝐭 ( κ, 0) ​ f ( γ + γ ′, 0) \mathbf{t}_{(\kappa,0)}\big((f_{(\gamma,0)})_{(\gamma^{\prime},0)}\big):=\mathbf{t}_{(\kappa,0)}f_{(\gamma+\gamma^{\prime},0)}. Second, the case γ = 0 \gamma=0 follows from Proposition 3.2 and Corollary 3.7.

(2) Let k ∈ { 1, …, m } k\in\{1,\dots,m\} and ( κ, λ) ∈ [0, ∞) m × ℝ n (\kappa,\lambda)\in[0,\infty)^{m}\times\mathbb{R}^{n} be sufficiently small and k k -zero; by Remark 5.2 (4), it suffices to prove that 𝐭 ( κ, λ) ​ f \mathbf{t}_{(\kappa,\lambda)}f belongs to 𝒬 k \mathcal{Q}_{k}. Since 𝐭 ( κ, λ) ​ f = 𝐭 ( κ, 0) ​ ( 𝐭 ( 0, λ) ​ f) \mathbf{t}_{(\kappa,\lambda)}f=\mathbf{t}_{(\kappa,0)}(\mathbf{t}_{(0,\lambda)}f), we may assume by Corollary 3.7 that λ = 0 \lambda=0. Let γ ∈ [0, ∞) k × { 0 } m − k \gamma\in[0,\infty)^{k}\times\{0\}^{m-k}. By (1), there is for each I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\} and each α ∈ B γ, I = B γ, I ​ ( T ​ f) \alpha\in B_{\gamma,I}=B_{\gamma,I}(Tf) a unique f γ, I, α ∈ 𝒬 m f_{\gamma,I,\alpha}\in\mathcal{Q}_{m} such that

 | f = ∑ I ⊆ { 1, …, m } x I ¯ γ I ¯ ​ ( ∑ α ∈ B γ, I x I α ⋅ f γ, I, α) f=\sum_{I\subseteq\{1,\dots,m\}}x_{\overline{I}}^{\gamma_{\overline{I}}}\left(\sum_{\alpha\in B_{\gamma,I}}x_{I}^{\alpha}\cdot f_{\gamma,I,\alpha}\right) |  |

and each f γ, I, α f_{\gamma,I,\alpha} depends only on the variables x I ¯ x_{\overline{I}} and y y. Since γ k + 1 = ⋯ = γ m = 0 \gamma_{k+1}=\cdots=\gamma_{m}=0, we have B γ, I = ∅ B_{\gamma,I}=\emptyset whenever I ⊈ { 1, …, k } I\nsubseteq\{1,\dots,k\}. Therefore,

 | 𝐭 ( κ, 0) ​ f = ∑ I ⊆ { 1, …, m } x I ¯ γ I ¯ ​ ( ∑ α ∈ B γ, I x I α ⋅ 𝐭 ( κ, 0) ​ f γ, I, α), \mathbf{t}_{(\kappa,0)}f=\sum_{I\subseteq\{1,\dots,m\}}x_{\overline{I}}^{\gamma_{\overline{I}}}\left(\sum_{\alpha\in B_{\gamma,I}}x_{I}^{\alpha}\cdot\mathbf{t}_{(\kappa,0)}f_{\gamma,I,\alpha}\right), |  |

and hence T ⁡ ( 𝐭 ( κ, 0) ​ f) = ∑ I X I ¯ γ I ¯ ​ ( ∑ α X I α ⋅ T ⁡ ( 𝐭 ( κ, 0) ​ f γ, I, α)) T(\mathbf{t}_{(\kappa,0)}f)=\sum_{I}X_{\overline{I}}^{\gamma_{\overline{I}}}\left(\sum_{\alpha}X_{I}^{\alpha}\cdot T(\mathbf{t}_{(\kappa,0)}f_{\gamma,I,\alpha})\right) is the unique γ \gamma -representation of T ⁡ ( 𝐭 ( κ, 0) ​ f) T(\mathbf{t}_{(\kappa,0)}f). Since f γ, ∅, 0 = f ( γ, 0) f_{\gamma,\emptyset,0}=f_{(\gamma,0)}, it follows that we can take ( 𝐭 ( κ, 0) ​ f) ( γ, 0):= 𝐭 ( κ, 0) ​ f ( γ, 0) (\mathbf{t}_{(\kappa,0)}f)_{(\gamma,0)}:=\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)}. Moreover, if κ ′ ∈ [0, ∞) k × { 0 } m − k \kappa^{\prime}\in[0,\infty)^{k}\times\{0\}^{m-k} is sufficiently small, then

 | 𝐭 ( κ ′, 0) ​ ( ( 𝐭 ( κ, 0) ​ f) ( γ, 0)) = 𝐭 ( κ ′, 0) ​ ( 𝐭 ( κ, 0) ​ f ( γ, 0)) = 𝐭 ( κ + κ ′, 0) ​ f ( γ, 0), \mathbf{t}_{(\kappa^{\prime},0)}((\mathbf{t}_{(\kappa,0)}f)_{(\gamma,0)})=\mathbf{t}_{(\kappa^{\prime},0)}(\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)})=\mathbf{t}_{(\kappa+\kappa^{\prime},0)}f_{(\gamma,0)}, |  |

so part (2) follows. ∎

From Proposition 5.6 and Lemma 1.4, we obtain:

###### Corollary 5.7.

Let f ∈ 𝒬 m f\in\mathcal{Q}_{m} and γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}. Then for each I ⊂ { 1, …, m } I\subset\{1,\dots,m\} and each α ∈ B γ, I = B γ, I ​ ( T ​ f) \alpha\in B_{\gamma,I}=B_{\gamma,I}(Tf), there is a unique f γ, I, α ∈ 𝒬 m f_{\gamma,I,\alpha}\in\mathcal{Q}_{m} such that

 | f = ∑ I ⊂ { 1, …, m } x I ¯ γ I ¯ ​ ( ∑ α ∈ B γ, I x I α ⋅ f γ, I, α) f=\sum_{I\subset\{1,\dots,m\}}x_{\overline{I}}^{\gamma_{\overline{I}}}\left(\sum_{\alpha\in B_{\gamma,I}}x_{I}^{\alpha}\cdot f_{\gamma,I,\alpha}\right) |  |

and each f γ, I, α f_{\gamma,I,\alpha} depends only on the variables x I ¯ x_{\overline{I}} and y y. ∎

###### Proposition 5.8.

Let f ∈ 𝒬 m f\in\mathcal{Q}_{m}.

1. (1)

For each i = 1, …, m i=1,\dots,m, the function ∂ i f \partial_{i}f belongs to 𝒬 m \mathcal{Q}_{m} and satisfies T ⁡ ( ∂ i f) = ∂ i ( T ​ f) T(\partial_{i}f)=\partial_{i}(Tf).

2. (2)

For each j = 1, …, n j=1,\dots,n, the function ∂ f / ∂ y j \partial f/\partial y_{j} belongs to 𝒬 m \mathcal{Q}_{m} and satisfies T ⁡ ( ∂ f / ∂ y j) = ∂ ( T ​ f) / ∂ Y j T(\partial f/\partial y_{j})=\partial(Tf)/\partial Y_{j}.

3. (3)

The function g:= f ⁡ ( x, y 1, …, y n − 1, 0) g:=f(x,y_{1},\dots,y_{n-1},0) belongs to 𝒬 m m + n − 1 \mathcal{Q}^{m+n-1}_{m}.

###### Proof.

Let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}. It follows from Propositions 2.9 and 5.6 and Lemmas 1.3 and 5.5 that ( ∂ i f) ( γ, 0):= γ i ⋅ f ( γ, 0) + ∂ i ( f ( γ, 0)) (\partial_{i}f)_{(\gamma,0)}:=\gamma_{i}\cdot f_{(\gamma,0)}+\partial_{i}(f_{(\gamma,0)}) belongs to 𝒜 m ​ ( V) \mathcal{A}_{m}(V) for a suitable V ⊆ 𝐋 m + n V\subseteq\mathbf{L}^{m+n} and satisfies T ⁡ ( ( ∂ i f) ( γ, 0)) = ∂ i ( ( T ​ f) ( γ, 0)) T((\partial_{i}f)_{(\gamma,0)})=\partial_{i}((Tf)_{(\gamma,0)}). Moreover, we let k ∈ { 1, …, m } k\in\{1,\dots,m\} and a k k -zero κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be sufficiently small. If i ≤ k i\leq k, then 𝐭 ( κ, 0) ​ ( ∂ i f ( γ, 0)) = ∂ i ( 𝐭 ( κ, 0) ​ f ( γ, 0)) \mathbf{t}_{(\kappa,0)}(\partial_{i}f_{(\gamma,0)})=\partial_{i}(\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)}) by Remark 3.5. If i > k i>k, then 𝐭 ( κ, 0) ​ f ( γ, 0) \mathbf{t}_{(\kappa,0)}f_{(\gamma,0)} belongs to 𝒬 k \mathcal{Q}_{k} by Proposition 5.6 (2), and it follows from Corollary 2.13 and Remark 3.5 that

 | x i 1 ⋅ ∂ ∂ x i ​ ( 𝐭 ( κ, 0) ​ f ( γ, 0)) = ∂ i ( 𝐭 ( κ, 0) ​ f ( γ, 0)) = x i 1 κ i + x i 1 ⋅ 𝐭 ( κ, 0) ​ ( ∂ i f ( γ, 0)). x_{i}^{1}\cdot\frac{\partial}{\partial x_{i}}(\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)})=\partial_{i}(\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)})=\frac{x_{i}^{1}}{\kappa_{i}+x_{i}^{1}}\cdot\mathbf{t}_{(\kappa,0)}(\partial_{i}f_{(\gamma,0)}). |  |

Therefore, 𝐭 ( κ, 0) ​ ( ∂ i f ( γ, 0)) \mathbf{t}_{(\kappa,0)}(\partial_{i}f_{(\gamma,0)}) belongs to 𝒜 m ​ ( V) \mathcal{A}_{m}(V) for some suitable V V with T ⁡ ( 𝐭 ( κ, 0) ​ ( ∂ i f ( γ, 0))) = ( κ i + X i) ⋅ ( ∂ / ∂ X i) ​ ( T ⁡ ( 𝐭 ( κ, 0) ​ f ( γ, 0))) T(\mathbf{t}_{(\kappa,0)}(\partial_{i}f_{(\gamma,0)}))=(\kappa_{i}+X_{i})\cdot(\partial/\partial X_{i})(T(\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)})), which proves part (1).

Part (2) is more straightforward and follows from Corollary 2.13, Proposition 5.6 and Lemmas 1.3 and 5.5. For (3), note that for all γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, we can take g ( γ, 0):= f ( γ, 0) ​ ( x, y 1, …, y n − 1, 0) g_{(\gamma,0)}:=f_{(\gamma,0)}(x,y_{1},\dots,y_{n-1},0). Then for every sufficiently small κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m}, we have

 | 𝐭 ( κ, 0) ​ g ( γ, 0) = ( 𝐭 ( κ, 0) ​ f ( γ, 0)) ​ ( x, y 1, …, y n − 1, 0), \mathbf{t}_{(\kappa,0)}g_{(\gamma,0)}=(\mathbf{t}_{(\kappa,0)}f_{(\gamma,0)})(x,y_{1},\dots,y_{n-1},0), |  |

and part (3) follows. ∎

### Composition

Let f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U). For the next lemma, we let 𝐪 = ( 𝐪 1, …, 𝐪 n) ∈ ℕ n \mathbf{q}=(\mathbf{q}_{1},\dots,\mathbf{q}_{n})\in\mathbb{N}^{n} and put 𝐤:= | 𝐪 | \mathbf{k}:=|\mathbf{q}|. We let z = ( z 1, …, z 𝐤) z=(z_{1},\dots,z_{\mathbf{k}}) range over 𝐋 𝐤 \mathbf{L}^{\mathbf{k}} and U ′ ⊆ 𝐋 m + 𝐤 U^{\prime}\subseteq\mathbf{L}^{m+\mathbf{k}} be an m m -quadratic domain such that ( x, z 1 + ⋯ + z 𝐪 1, …, z 𝐪 1 + ⋯ + 𝐪 n − 1 + 1 + ⋯ + z 𝐤) ∈ U (x,z_{1}+\cdots+z_{\mathbf{q}_{1}},\dots,z_{\mathbf{q}_{1}+\cdots+\mathbf{q}_{n-1}+1}+\cdots+z_{\mathbf{k}})\in U for all ( x, z) ∈ U ′ (x,z)\in U^{\prime}. In this situation, we define the holomorphic function f 𝐪: U ′ ⟶ ℂ f_{\mathbf{q}}:U^{\prime}\longrightarrow\mathbb{C} by

 | f 𝐪 ​ ( x, z):= f ⁡ ( x, z 1 + ⋯ + z 𝐪 1, …, z 𝐪 1 + ⋯ + 𝐪 n − 1 + 1 + ⋯ + z 𝐤). f_{\mathbf{q}}(x,z):=f(x,z_{1}+\cdots+z_{\mathbf{q}_{1}},\dots,z_{\mathbf{q}_{1}+\cdots+\mathbf{q}_{n-1}+1}+\cdots+z_{\mathbf{k}}). |  |

###### Lemma 5.9.

We have f 𝐪 ∈ 𝒬 m ​ ( U ′) f_{\mathbf{q}}\in\mathcal{Q}_{m}(U^{\prime}) and T ⁡ ( f 𝐪) = ( T ​ f) 𝐪 T(f_{\mathbf{q}})=(Tf)_{\mathbf{q}}.

###### Proof.

We first show that f 𝐪 ∈ 𝒜 m ​ ( U ′) f_{\mathbf{q}}\in\mathcal{A}_{m}(U^{\prime}) and T ⁡ ( f 𝐪) = ( T ​ f) 𝐪 T(f_{\mathbf{q}})=(Tf)_{\mathbf{q}}. Arguing by induction on 𝐤 \mathbf{k} (simultaneously for all m m) and permuting the last n n coordinates if necessary, it suffices to consider the case where n = 1 n=1 and 𝐤 = 𝐪 1 = 2 \mathbf{k}=\mathbf{q}_{1}=2. In this situation, by Proposition 2.14 and after shrinking U U if necessary, we can write f ⁡ ( x, y) = ∑ p ∈ ℕ a p ​ ( x) ​ y p f(x,y)=\sum_{p\in\mathbb{N}}a_{p}(x)y^{p} for all ( x, y) ∈ U (x,y)\in U, and there are a quadratic domain W ⊆ 𝐋 W\subseteq\mathbf{L} and constants A, B > 0 A,B>0 such that a p ∈ 𝒜 m ​ ( W m) a_{p}\in\mathcal{A}_{m}(W^{m}) and ‖ a p ​ ( x) ‖ ≤ A ​ B p \|a_{p}(x)\|\leq AB^{p} for all x ∈ W m x\in W^{m} and each p ∈ ℕ p\in\mathbb{N}. Hence

 | f 𝐪 ​ ( x, z) = ∑ p ∈ ℕ a p ​ ( x) ​ ( z 1 + z 2) p = ∑ p, q ∈ ℕ b p, q ​ ( x) ​ z 1 p ​ z 2 q f_{\mathbf{q}}(x,z)=\sum_{p\in\mathbb{N}}a_{p}(x)(z_{1}+z_{2})^{p}=\sum_{p,q\in\mathbb{N}}b_{p,q}(x)z_{1}^{p}z_{2}^{q} |  |

for all sufficiently small ( x, z) ∈ U ′ (x,z)\in U^{\prime}, where b p, q:= ( p + q p) ​ a p + q b_{p,q}:=\begin{pmatrix}p+q\\ p\end{pmatrix}a_{p+q} for all p, q ∈ ℕ p,q\in\mathbb{N}. Since ‖ b p, q ‖ ≤ A ​ ( 2 ​ B) p + q \|b_{p,q}\|\leq A(2B)^{p+q}, it follows from Propositions 2.14 and 2.15 that f 𝐪 ∈ 𝒜 m ​ ( U ′) f_{\mathbf{q}}\in\mathcal{A}_{m}(U^{\prime}), as required.

Next, for every γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, we have OPEN T ​ ( f ( γ, 0)) 𝐪) = ( T ​ f 𝐪) ( γ, 0) T(f_{(\gamma,0)})_{\mathbf{q}})=(Tf_{\mathbf{q}})_{(\gamma,0)}, so we can take ( f 𝐪) ( γ, 0):= ( f ( γ, 0)) 𝐪 (f_{\mathbf{q}})_{(\gamma,0)}:=(f_{(\gamma,0)})_{\mathbf{q}}. Moreover, for every sufficiently small κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m}, the previous paragraph and Proposition 2.15 now also show that 𝐭 ( κ, 0) ​ ( f 𝐪) ( γ, 0) \mathbf{t}_{(\kappa,0)}(f_{\mathbf{q}})_{(\gamma,0)} belongs to 𝒜 m ​ ( V ′) \mathcal{A}_{m}(V^{\prime}) for some appropriate V ′ V^{\prime}. ∎

For the next proposition, we let g = ( g 1, …, g n) ∈ 𝒬 m ​ ( V) n g=(g_{1},\dots,g_{n})\in\mathcal{Q}_{m}(V)^{n} be such that g ⁡ ( 0) = 0 g(0)=0 and ( x, g ⁡ ( x, y)) ∈ U (x,g(x,y))\in U for all ( x, y) ∈ V (x,y)\in V, and we define the holomorphic function h: V ⟶ ℂ h:V\longrightarrow\mathbb{C} by h ⁡ ( x, y):= f ⁡ ( x, g ⁡ ( x, y)). h(x,y):=f(x,g(x,y)).

###### Proposition 5.10.

The function h h belongs to 𝒬 m ​ ( V) \mathcal{Q}_{m}(V) and T ​ h ​ ( X, Y) = T ​ f ​ ( X, T ​ g ​ ( X, Y)) Th(X,Y)=Tf(X,Tg(X,Y)).

###### Proof.

First, let κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be such that ( κ, 0) ∈ cl 0 ⁡ ( V) (\kappa,0)\in\cl_{0}(V). Then 𝐭 ( κ, 0) ​ h = ( 𝐭 ( κ, 0) ​ f) ​ ( x, 𝐭 ( κ, 0) ​ g) \mathbf{t}_{(\kappa,0)}h=(\mathbf{t}_{(\kappa,0)}f)(x,\mathbf{t}_{(\kappa,0)}g), so Corollary 3.7 (with λ \lambda there equal to 𝐭 ( κ, 0) ​ g ​ ( 0, 0) \mathbf{t}_{(\kappa,0)}g(0,0)) and Proposition 3.9 show that 𝐭 ( κ, 0) ​ h ∈ 𝒜 m ​ ( W) \mathbf{t}_{(\kappa,0)}h\in\mathcal{A}_{m}(W) for some appropriate W W.

Second, let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}; we need to find an m m -quadratic domain V ′ ⊆ V V^{\prime}\subseteq V and an h ′ ∈ 𝒜 m ​ ( V ′) h^{\prime}\in\mathcal{A}_{m}(V^{\prime}) such that T ⁡ ( h ′) = ( T ​ h) ( γ, 0) T(h^{\prime})=(Th)_{(\gamma,0)}. By Proposition 1.13, there are p ∈ ℕ p\in\mathbb{N}, a tuple 𝐪 ∈ ℕ n \mathbf{q}\in\mathbb{N}^{n} and, with 𝐤:= | 𝐪 | \mathbf{k}:=|\mathbf{q}|, elementary sets E 1, …, E p ⊆ [0, ∞) m × ℕ 𝐤 E_{1},\dots,E_{p}\subseteq[0,\infty)^{m}\times\mathbb{N}^{\mathbf{k}} and B i, j ⊆ [0, ∞) m × ℕ n B_{i,j}\subseteq[0,\infty)^{m}\times\mathbb{N}^{n} for each pair ( i, j) (i,j) satisfying i ∈ { 1, …, n } i\in\{1,\dots,n\} and j ∈ { 1, …, 𝐪 i } j\in\{1,\dots,\mathbf{q}_{i}\}, such that

 | T ​ f ​ ( X, T ​ g) ( γ, 0) = ∑ q = 1 p ( X, ( T ​ g) B) inf E q X γ ⋅ ( ( T ​ f) 𝐪) E q ​ ( X, ( T ​ g) B) Tf(X,Tg)_{(\gamma,0)}=\sum_{q=1}^{p}\frac{(X,(Tg)_{B})^{\inf E_{q}}}{X^{\gamma}}\cdot((Tf)_{\mathbf{q}})_{E_{q}}(X,(Tg)_{B}) |  |

with ( T ​ g) B:= ( ( T ​ g 1) B 1, 1, …, ( T ​ g n) B n, 𝐪 n) (Tg)_{B}:=((Tg_{1})_{B_{1,1}},\dots,(Tg_{n})_{B_{n,\mathbf{q}_{n}}}) and each ( X, ( T ​ g) B) inf E q (X,(Tg)_{B})^{\inf E_{q}} divisible by X γ X^{\gamma}. After shrinking V V if necessary and writing g B:= ( ( g 1) B 1, 1, …, ( g n) B n, 𝐪 n) g_{B}:=((g_{1})_{B_{1,1}},\dots,(g_{n})_{B_{n,\mathbf{q}_{n}}}), we get from Lemma 5.9, Proposition 5.6 and the above that, for each q = 1, …, p q=1,\dots,p, the function

 | h q:= x − γ ⋅ ( x, g B) inf E q ⋅ ( f 𝐪) E q ​ ( x, g B) h_{q}:=x^{-\gamma}\cdot(x,g_{B})^{\inf E_{q}}\cdot(f_{\mathbf{q}})_{E_{q}}(x,g_{B}) |  |

belongs to 𝒜 m ​ ( V) \mathcal{A}_{m}(V) and satisfies

 | T ​ h 𝐪 = X − γ ⋅ ( X, ( T ​ g) B) inf E q ⋅ ( ( T ​ f) 𝐪) E q ​ ( X, ( T ​ g) B). Th_{\mathbf{q}}=X^{-\gamma}\cdot(X,(Tg)_{B})^{\inf E_{q}}\cdot((Tf)_{\mathbf{q}})_{E_{q}}(X,(Tg)_{B}). |  |

Hence by Lemma 5.5, we can take h ′:= h 1 + ⋯ + h p h^{\prime}:=h_{1}+\cdots+h_{p}.

Finally, it follows from the last paragraph and the first observation above that h ∈ 𝒬 m h\in\mathcal{Q}_{m}. ∎

Here are some immediate applications of Proposition 5.10:

###### Proposition 5.11.

The set 𝒬 m \mathcal{Q}_{m} is a ℂ \mathbb{C} -algebra, and the map f ↦ T ​ f: 𝒬 m ⟶ ℂ ⁡ [[X ∗, Y]] f\mapsto Tf:\mathcal{Q}_{m}\longrightarrow\mathbb{C}[\![X^{*},Y]\!] is an injective ℂ \mathbb{C} -algebra homomorphism such that f ​ ( 0) = ( T ​ f) ​ ( 0) f(0)=(Tf)(0) for all f ∈ 𝒬 m f\in\mathcal{Q}_{m}.

###### Proof.

Let f, g ∈ 𝒬 m f,g\in\mathcal{Q}_{m}; we need to show that f ​ g ∈ 𝒬 m fg\in\mathcal{Q}_{m}. Put f 1:= f − f ⁡ ( 0) f_{1}:=f-f(0) and g 1:= g − g ⁡ ( 0) g_{1}:=g-g(0); then f 1, g 1 ∈ 𝒬 m f_{1},g_{1}\in\mathcal{Q}_{m} by Lemma 5.5, and f ​ g = P ⁡ ( f 1, g 1) fg=P(f_{1},g_{1}) with P ⁡ ( Y 1, Y 2):= ( f ⁡ ( 0) + Y 1) ​ ( g ⁡ ( 0) + Y 2) P(Y_{1},Y_{2}):=(f(0)+Y_{1})(g(0)+Y_{2}). Hence f ​ g ∈ 𝒬 m fg\in\mathcal{Q}_{m} by Proposition 5.10. ∎

###### Proposition 5.12.

Let f ∈ 𝒬 m f\in\mathcal{Q}_{m}. Then

1. (1)

f f is a unit in 𝒬 m \mathcal{Q}_{m} if and only if f ⁡ ( 0) ≠ 0 f(0)\neq 0;

2. (2)

if f ⁡ ( 0) = 0 f(0)=0, then there are ( γ, δ) ∈ ( 0, ∞) m × ( ℕ ∖ { 0 }) n (\gamma,\delta)\in(0,\infty)^{m}\times(\mathbb{N}\setminus\{0\})^{n} and f 1, …, f m + n ∈ 𝒬 m f_{1},\dots,f_{m+n}\in\mathcal{Q}_{m} such that f = X 1 γ 1 ​ f 1 + ⋯ + Y n δ n ​ f m + n f=X_{1}^{\gamma_{1}}f_{1}+\cdots+Y_{n}^{\delta_{n}}f_{m+n}.

###### Proof.

(1) Assume first that f f is a unit in 𝒬 m \mathcal{Q}_{m}, and let g ∈ Q m g\in Q_{m} be such that f ⋅ g = 1 f\cdot g=1. Then T ​ f ⋅ T ​ h = 1 Tf\cdot Th=1 and hence f ⁡ ( 0) = T ​ f ​ ( 0) ≠ 0 f(0)=Tf(0)\neq 0. Conversely, assume that f ⁡ ( 0) ≠ 0 f(0)\neq 0; we may assume that f ⁡ ( 0) = 1 f(0)=1, and we put f 1:= 1 − f ∈ 𝒬 m f_{1}:=1-f\in\mathcal{Q}_{m}. Let 𝐚 > 0 \mathbf{a}>0 and U 𝐚 ⊆ 𝐋 m + n U_{\mathbf{a}}\subseteq\mathbf{L}^{m+n} be an m m -quadratic domain such that f 1 ​ ( x, y) = o ⁡ ( ‖ ( x, y) ‖ 𝐚) f_{1}(x,y)=o(\|(x,y)\|^{\mathbf{a}}) as ‖ ( x, y) ‖ → 0 \|(x,y)\|\to 0 in U 𝐚 U_{\mathbf{a}}. Thus, there is an m m -quadratic domain U ⊆ U 𝐚 U\subseteq U_{\mathbf{a}} such that ‖ f 1 ​ ( x, y) ‖ ≤ 1 2 \|f_{1}(x,y)\|\leq\frac{1}{2} for all ( x, y) ∈ U (x,y)\in U. Let ϕ: B ⁡ ( 0, 1) ⟶ ℂ \phi:B(0,1)\longrightarrow\mathbb{C} be the holomorphic function defined by ϕ ⁡ ( z):= 1 1 − z \phi(z):=\frac{1}{1-z}, and define g: U ⟶ ℂ g:U\longrightarrow\mathbb{C} by g ⁡ ( x, y):= ϕ ⁡ ( f 1 ​ ( x, y)) g(x,y):=\phi(f_{1}(x,y)). Then f ⋅ g = 1 f\cdot g=1, and g ∈ 𝒬 m ​ ( U) g\in\mathcal{Q}_{m}(U) by Proposition 5.10.

(2) follows from Lemma 4.8 of [3] and Proposition 5.6. ∎

Finally, Proposition 5.10 allows us to make sense of certain substitutions in the x x -variables:

###### Definition 5.13.

Let W ⊆ 𝐋 W\subseteq\mathbf{L} be a quadratic domain and R > 0 R>0, and let f ∈ 𝒬 m ​ ( W m × B 𝐋 ​ ( R)) f\in\mathcal{Q}_{m}(W^{m}\times B_{\mathbf{L}}(R)). Let also V ⊆ 𝐋 m + n V\subseteq\mathbf{L}^{m+n} be m m -quadratic and g = ( g 1, …, g m) ∈ 𝒬 m ​ ( V) m g=(g_{1},\dots,g_{m})\in\mathcal{Q}_{m}(V)^{m} be such that λ:= g ⁡ ( 0, 0) ∈ W m ∩ ( 0, ∞) m \lambda:=g(0,0)\in W^{m}\cap(0,\infty)^{m}. Then g ⁡ ( x, y) = λ + h ⁡ ( x, y) g(x,y)=\lambda+h(x,y) with h ∈ 𝒬 m ​ ( V) m h\in\mathcal{Q}_{m}(V)^{m} satisfying h ⁡ ( 0) = 0 h(0)=0, and we define f ⁡ ( g ⁡ ( x, y), y):= ( 𝐭 ( λ, 0) ​ f) ​ ( h ⁡ ( x, y), y) f(g(x,y),y):=(\mathbf{t}_{(\lambda,0)}f)(h(x,y),y).

###### Corollary 5.14.

The function f ⁡ ( g ⁡ ( x, y), y) f(g(x,y),y) in Definition 5.13 belongs to 𝒬 m \mathcal{Q}_{m}. ∎

Some of the substitutions not covered by the previous corollary are the blow-up substitutions:

###### Proposition 5.15.

Let ρ, λ > 0 \rho,\lambda>0 and i, j ∈ { 1, …, m } i,j\in\{1,\dots,m\} be distinct.

1. (1)

The function f ∘ 𝐬 i, j ρ f\circ\mathbf{s}^{\rho}_{i,j} belongs to 𝒬 m \mathcal{Q}_{m} for every f ∈ 𝒬 m f\in\mathcal{Q}_{m}, and the map 𝐬 i ​ j ρ: 𝒬 m ⟶ 𝒬 m \mathbf{s}^{\rho}_{ij}:\mathcal{Q}_{m}\longrightarrow\mathcal{Q}_{m} defined by 𝐬 i ​ j ρ ​ ( f):= f ∘ 𝐬 i ​ j ρ \mathbf{s}^{\rho}_{ij}(f):=f\circ\mathbf{s}^{\rho}_{ij} is a ℂ \mathbb{C} -algebra homomorphism such that T ∘ 𝐬 i ​ j ρ = 𝐁 i ​ j ρ, 0 ∘ T T\circ\mathbf{s}^{\rho}_{ij}=\mathbf{B}^{\rho,0}_{ij}\circ T.

2. (2)

The function f ∘ 𝐫 ρ, λ f\circ\mathbf{r}^{\rho,\lambda} belong to 𝒬 m − 1 \mathcal{Q}_{m-1} for every f ∈ 𝒬 m f\in\mathcal{Q}_{m}, and the map 𝐫 ρ, λ: 𝒬 m ⟶ 𝒬 m − 1 \mathbf{r}^{\rho,\lambda}:\mathcal{Q}_{m}\longrightarrow\mathcal{Q}_{m-1} defined by 𝐫 ρ, λ ​ ( f):= f ∘ 𝐫 ρ, λ \mathbf{r}^{\rho,\lambda}(f):=f\circ\mathbf{r}^{\rho,\lambda} is a ℂ \mathbb{C} -algebra homomorphism such that T ∘ 𝐫 ρ, λ = 𝐁 m, m − 1 ρ, λ ∘ T T\circ\mathbf{r}^{\rho,\lambda}=\mathbf{B}^{\rho,\lambda}_{m,m-1}\circ T.

Whenever convenient, we shall write 𝐬 i ​ j ρ ​ f \mathbf{s}^{\rho}_{ij}f and 𝐫 ρ, λ ​ f \mathbf{r}^{\rho,\lambda}f in place of 𝐬 i ​ j ρ ​ ( f) \mathbf{s}^{\rho}_{ij}(f) and 𝐫 ρ, λ ​ ( f) \mathbf{r}^{\rho,\lambda}(f).

###### Proof.

The proofs for parts (1) and (2) are similar; we prove (1) here and leave (2) to the reader. We may assume that i = m i=m and j = m − 1 j=m-1, and we write 𝐬 \mathbf{s} and ℬ \mathcal{B} in place of 𝐬 m, m − 1 ρ \mathbf{s}^{\rho}_{m,m-1} and ℬ m, m − 1 ρ \mathcal{B}^{\rho}_{m,m-1}. Let f ∈ 𝒬 m f\in\mathcal{Q}_{m}; if suffices to prove that f ∘ 𝐬 ∈ 𝒬 m f\circ\mathbf{s}\in\mathcal{Q}_{m}.

To do so, we let W ⊆ 𝐋 W\subseteq\mathbf{L} be quadratic and 1 > R > 0 1>R>0 be such that f ∈ 𝒜 m ​ ( W m × B 𝐋 ​ ( R) n) f\in\mathcal{A}_{m}(W^{m}\times B_{\mathbf{L}}(R)^{n}), and we let W ′ W^{\prime} and V V be as in the proof of Proposition 4.2. We also let κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be nonzero such that ( κ, 0) ∈ cl 0 ⁡ ( V) (\kappa,0)\in\cl_{0}(V), and let W κ ⊆ W ′ W_{\kappa}\subseteq W^{\prime} be quadratic such that 𝐭 ( κ, 0) ​ ( x, y) ∈ V \mathbf{t}_{(\kappa,0)}(x,y)\in V for all ( x, y) ∈ V κ:= ( W κ) m × B 𝐋 ​ ( R) n (x,y)\in V_{\kappa}:=(W_{\kappa})^{m}\times B_{\mathbf{L}}(R)^{n}. By Propositions 1.12 and 5.6, it remains to prove that

- ( ∗) (\ast)

𝐭 ( κ, 0) ​ ( f ∘ 𝐬) \mathbf{t}_{(\kappa,0)}(f\circ\mathbf{s}) belongs to 𝒜 m ​ ( V κ) \mathcal{A}_{m}(V_{\kappa}).

Writing κ ′ = ( κ 1, …, κ m − 2) \kappa^{\prime}\>=(\kappa_{1},\dots,\kappa_{m-2}) and κ ′′:= ( κ m − 1, κ m) \kappa^{\prime\prime}:=(\kappa_{m-1},\kappa_{m}), we see that 𝐭 ( κ, 0) ​ ( f ∘ 𝐬) = 𝐭 ( 0, κ ′′, 0) ​ ( 𝐭 ( κ ′, 0, 0) ​ ( f ∘ 𝐬)) \mathbf{t}_{(\kappa,0)}(f\circ\mathbf{s})=\mathbf{t}_{(0,\kappa^{\prime\prime},0)}(\mathbf{t}_{(\kappa^{\prime},0,0)}(f\circ\mathbf{s})); since 𝐭 ( κ ′, 0, 0) ​ ( f ∘ 𝐬) = ( 𝐭 ( κ ′, 0, 0) ​ f) ∘ 𝐬 \mathbf{t}_{(\kappa^{\prime},0,0)}(f\circ\mathbf{s})=(\mathbf{t}_{(\kappa^{\prime},0,0)}f)\circ\mathbf{s}, we may even assume that κ 1 = ⋯ = κ m − 2 = 0 \kappa_{1}=\cdots=\kappa_{m-2}=0. We now distinguish three cases:

Case 1: both κ m − 1 \kappa_{m-1} and κ m \kappa_{m} are nonzero. Then

 | 𝐭 ( κ, 0) ​ ( f ∘ 𝐬) ​ ( x, y) = ( 𝐭 ( 0, κ m − 1, κ m − 1 ρ ​ κ m, 0) ​ f) ​ ( x ′, g ⁡ ( x m − 1, x m), y), \mathbf{t}_{(\kappa,0)}(f\circ\mathbf{s})(x,y)=(\mathbf{t}_{(0,\kappa_{m-1},\kappa_{m-1}^{\rho}\kappa_{m},0)}f)(x^{\prime},g(x_{m-1},x_{m}),y), |  |

where x ′:= ( x 1, …, x m − 1) x^{\prime}:=(x_{1},\dots,x_{m-1}) and g g is an analytic function satisfying g ⁡ ( 0) = 0 g(0)=0. Since 𝐭 ( 0, κ m − 1, κ m − 1 ρ ​ κ m, 0) ​ f \mathbf{t}_{(0,\kappa_{m-1},\kappa_{m-1}^{\rho}\kappa_{m},0)}f belongs to 𝒬 m − 2 \mathcal{Q}_{m-2} by Proposition 5.6, ( ∗) (\ast) follows from Proposition 5.10 in this case.

Case 2: κ m − 1 = 0 \kappa_{m-1}=0 and κ m > 0 \kappa_{m}>0. Then 𝐭 ( κ, 0) ​ ( f ∘ 𝐬) = f ∘ 𝐫 ρ, κ m \mathbf{t}_{(\kappa,0)}(f\circ\mathbf{s})=f\circ\mathbf{r}^{\rho,\kappa_{m}}, so ( ∗) (\ast) follows from Proposition 4.4 in this case.

Case 3: κ m − 1 ≠ 0 \kappa_{m-1}\neq 0 and κ m = 0 \kappa_{m}=0. We define ϕ ⁡ ( z 1, …, z m + 1, y):= 𝐭 ( κ, 0) ​ f ​ ( z 1, …, z m − 1, z m + 1, y) \phi(z_{1},\dots,z_{m+1},y):=\mathbf{t}_{(\kappa,0)}f(z_{1},\dots,z_{m-1},z_{m+1},y). Then ϕ ∈ 𝒬 m + 1 \phi\in\mathcal{Q}_{m+1}, and there is an analytic one-variable function g g with g ⁡ ( 0) = 0 g(0)=0 such that

 | 𝐭 ( κ, 0) ​ ( f ∘ 𝐬) ​ ( x, y) = ( ϕ ∘ 𝐫 1, κ m − 1 ρ) ​ ( x, g ⁡ ( x m − 1), y). \mathbf{t}_{(\kappa,0)}(f\circ\mathbf{s})(x,y)=\left(\phi\circ\mathbf{r}^{1,\kappa_{m-1}^{\rho}}\right)(x,g(x_{m-1}),y). |  |

Thus, ( ∗) (\ast) follows from Propositions 4.4 and 3.9 in this case. ∎

As a consequence of Proposition 5.15, we extend Corollary 5.14 to certain functions with zero constant coefficient:

###### Definition 5.16.

Let m ≥ 1 m\geq 1, let W ⊆ 𝐋 W\subseteq\mathbf{L} be a quadratic domain and R > 0 R>0, and let f ∈ 𝒬 m ​ ( W m × B 𝐋 ​ ( R) n) f\in\mathcal{Q}_{m}(W^{m}\times B_{\mathbf{L}}(R)^{n}). Let also V ⊆ 𝐋 V\subseteq\mathbf{L} be a quadratic domain and g ∈ Q 1 ​ ( V) g\in Q_{1}(V) be such that g ⁡ ( t) ∈ W ∩ ( 0, ∞) g(t)\in W\cap(0,\infty) for all t ∈ V ∩ ( 0, ∞) t\in V\cap(0,\infty). Then g ⁡ ( t) = t ρ ​ ( λ + h ⁡ ( t)) g(t)=t^{\rho}(\lambda+h(t)) for some ρ, λ > 0 \rho,\lambda>0 and some h ∈ 𝒬 1 ​ ( V) h\in\mathcal{Q}_{1}(V) with h ⁡ ( 0) = 0 h(0)=0. We write x ′:= ( x 1, …, x m − 1) x^{\prime}:=(x_{1},\dots,x_{m-1}) and let f ~ ∈ 𝒬 m + 1 ​ ( W m + 1 × B 𝐋 ​ ( R) n) \widetilde{f}\in\mathcal{Q}_{m+1}(W^{m+1}\times B_{\mathbf{L}}(R)^{n}) be the function defined by f ~ ​ ( x ′, u, v, y):= f ⁡ ( x ′, v, y) \widetilde{f}(x^{\prime},u,v,y):=f(x^{\prime},v,y). Then 𝐫 ρ, λ ​ f ~ ∈ 𝒬 m m + n + 1 \mathbf{r}^{\rho,\lambda}\widetilde{f}\in\mathcal{Q}_{m}^{m+n+1}, and we define

 | f ⁡ ( x ′, g ⁡ ( t), y):= ( 𝐫 ρ, λ ​ f ~) ​ ( x ′, t, h ⁡ ( t), y). f(x^{\prime},g(t),y):=\left(\mathbf{r}^{\rho,\lambda}\widetilde{f}\right)(x^{\prime},t,h(t),y). |  |

###### Corollary 5.17.

The function f ⁡ ( x ′, g ⁡ ( t), y) f(x^{\prime},g(t),y) in Definition 5.16 belongs to 𝒬 m m + n \mathcal{Q}_{m}^{m+n}. ∎

## 6. Weierstrass Preparation

We continue to work in the setting of the previous section. In this section, we establish a Weierstrass Preparation Theorem for the classes 𝒬 m \mathcal{Q}_{m}. We follow Brieskorn and Knörrer’s exposition in Section 8.2 of [1]; to do so, we need to first establish an implicit function theorem and a theorem on symmetric functions. We thank Lou van den Dries for his helpfull suggestions on this section, especially the proof of Corollary 6.2 below.

We start with a single implicit variable and write y ′:= ( y 1, …, y n − 1) y^{\prime}:=(y_{1},\dots,y_{n-1}) and Y ′:= ( Y 1, …, Y n − 1) Y^{\prime}:=(Y_{1},\dots,Y_{n-1}).

###### Proposition 6.1.

Let f ∈ 𝒬 m m + n f\in\mathcal{Q}_{m}^{m+n}, and assume that f ⁡ ( 0) = 0 f(0)=0 and ∂ f / ∂ y n ​ ( 0) ≠ 0 \partial f/\partial y_{n}(0)\neq 0. Then there is an h ∈ 𝒬 m m + n − 1 h\in\mathcal{Q}_{m}^{m+n-1} such that h ⁡ ( 0) = 0 h(0)=0 and f ⁡ ( x, y ′, h) = 0 f(x,y^{\prime},h)=0.

###### Proof.

We let U = W m × B 𝐋 ​ ( R) n U=W^{m}\times B_{\mathbf{L}}(R)^{n} for some quadratic W ⊆ 𝐋 W\subseteq\mathbf{L} and R > 0 R>0 be such that f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U), and we put V:= W m × B 𝐋 ​ ( R) n − 1 V:=W^{m}\times B_{\mathbf{L}}(R)^{n-1}. During the proof below, we may have to shrink W W and R R (and all related quantities introduced below) on various occasions; we will not explicitely mention this. By Proposition 5.8, the function ( ∂ f / ∂ y n) ​ ( x, y ′, 0) (\partial f/\partial y_{n})(x,y^{\prime},0) belongs to 𝒬 m ​ ( V) \mathcal{Q}_{m}(V). Hence by hypothesis, there is a constant c > 0 c>0 such that | ( ∂ f / ∂ y n) ​ ( x, y ′, 0) | ≥ c |(\partial f/\partial y_{n})(x,y^{\prime},0)|\geq c for all ( x, y ′) ∈ V (x,y^{\prime})\in V. On the other hand, by Proposition 2.14, we can write f ⁡ ( x, y) = ∑ p ∈ ℕ a p ​ ( x, y ′) ​ y n p f(x,y)=\sum_{p\in\mathbb{N}}a_{p}(x,y^{\prime})y_{n}^{p} with each a p ∈ 𝒪 m ​ ( V) a_{p}\in\mathcal{O}_{m}(V).

Define g: U ⟶ ℂ g:U\longrightarrow\mathbb{C} by g ⁡ ( x, y):= f ⁡ ( x, y) − a 0 ​ ( x, y ′) g(x,y):=f(x,y)-a_{0}(x,y^{\prime}); note that g ∈ 𝒪 m ​ ( U) g\in\mathcal{O}_{m}(U). By the above and the usual arguments for the inverse function theorem, there is a ρ > 0 \rho>0 such that for every ( x, y ′) ∈ V (x,y^{\prime})\in V, we have ‖ a 0 ​ ( x, y ′) ‖ ≤ ρ / 2 \|a_{0}(x,y^{\prime})\|\leq\rho/2 and the function g x, y ′: B 𝐋 ​ ( R) ⟶ ℂ g_{x,y^{\prime}}:B_{\mathbf{L}}(R)\longrightarrow\mathbb{C} defined by g x, y ′ ​ ( y n):= g ⁡ ( x, y) g_{x,y^{\prime}}(y_{n}):=g(x,y) is injective and satisfies g x, y ′ ​ ( 0) = 0 g_{x,y^{\prime}}(0)=0 and B ⁡ ( 0, ρ) ⊆ g x, y ′ ​ ( B 𝐋 ​ ( R)) B(0,\rho)\subseteq g_{x,y^{\prime}}(B_{\mathbf{L}}(R)), and such that its compositional inverse g x, y ′ − 1: B 𝐋 ​ ( ρ) ⟶ ℂ g_{x,y^{\prime}}^{-1}:B_{\mathbf{L}}(\rho)\longrightarrow\mathbb{C} is given by a convergent power series

 | g x, y ′ − 1 ​ ( z) = ∑ p ∈ ℕ b p ​ ( x, y ′) ​ y n p. g^{-1}_{x,y^{\prime}}(z)=\sum_{p\in\mathbb{N}}b_{p}(x,y^{\prime})y_{n}^{p}. |  |

We claim that the function H: V × B 𝐋 ​ ( ρ / 2) ⟶ ℂ H:V\times B_{\mathbf{L}}(\rho/2)\longrightarrow\mathbb{C} defined by H ⁡ ( x, y):= g x, y ′ − 1 ​ ( y n) H(x,y):=g_{x,y^{\prime}}^{-1}(y_{n}) belongs to 𝒬 m ​ ( V × B 𝐋 ​ ( ρ / 2)) \mathcal{Q}_{m}(V\times B_{\mathbf{L}}(\rho/2)). The proposition follows from this claim by defining h: V ⟶ ℂ h:V\longrightarrow\mathbb{C} as h ⁡ ( x, y ′):= H ⁡ ( x, y ′, y n − a 0 ​ ( x, y ′)) | y n = 0 h(x,y^{\prime}):=H(x,y^{\prime},y_{n}-a_{0}(x,y^{\prime}))|_{y_{n}=0}.

To see the claim, we note first from the Lagrange inversion formula (see for instance Whittaker and Watson [12, p. 133]) that for all p ∈ ℕ p\in\mathbb{N},

 | b p ​ ( x, y ′) = 1 p! ​ [∂ p − 1 ∂ y n p − 1 ​ ( y n g ⁡ ( x, y)) p] y n = 0. b_{p}(x,y^{\prime})=\frac{1}{p!}\left[\frac{\partial^{p-1}}{\partial y_{n}^{p-1}}\left(\frac{y_{n}}{g(x,y)}\right)^{p}\right]_{y_{n}=0}. |  |

Since a 1 ​ ( 0) ≠ 0 a_{1}(0)\neq 0 by hypothesis, it follows from Propositions 5.12, 5.11 and 5.8 and Remark 5.2 (2) that b p ∈ 𝒬 m ​ ( V) b_{p}\in\mathcal{Q}_{m}(V) for each p p.

Second, we let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m}, and we claim that H ( γ, 0) ∈ 𝒜 m ​ ( V × B 𝐋 ​ ( ρ / 2)) H_{(\gamma,0)}\in\mathcal{A}_{m}(V\times B_{\mathbf{L}}(\rho/2)). It suffices, by Propositions 2.15 and 3.2, to find constants A, B > 0 A,B>0 such that ‖ ( b p) ( γ, 0) ​ ( x, y ′) ‖ ≤ A ​ B p \|(b_{p})_{(\gamma,0)}(x,y^{\prime})\|\leq AB^{p} for all p ∈ ℕ p\in\mathbb{N} and ( x, y ′) ∈ V (x,y^{\prime})\in V. To do so, we shall assume that U ⊆ B 𝐋 ​ ( 1) m + n U\subseteq B_{\mathbf{L}}(1)^{m+n}, and we put 𝐠 ⁡ ( x, y):= y n / g ⁡ ( x, y) ∈ 𝒬 m ​ ( U) \mathbf{g}(x,y):=y_{n}/g(x,y)\in\mathcal{Q}_{m}(U). We let 𝒥 \mathcal{J} be the set of all ordered pairs ( I, α) (I,\alpha) such that I ⊆ { 1, …, m } I\subseteq\{1,\dots,m\} and α ∈ B I = B γ, I ​ ( T ​ 𝔤) \alpha\in B_{I}=B_{\gamma,I}(T\mathfrak{g}), where the latter is defined as in Lemma 1.4. By Corollary 5.7, there is a constant C > 0 C>0 and for each ( I, α) ∈ 𝒥 (I,\alpha)\in\mathcal{J} a function 𝐠 I, α ∈ 𝒬 m ​ ( U) \mathbf{g}_{I,\alpha}\in\mathcal{Q}_{m}(U), depending only on the variables x I ¯ x_{\overline{I}} and y y, such that

 | 𝐠 ⁡ ( x, y) = ∑ ( I, α) ∈ 𝒥 x I ¯ γ I ¯ ​ x I α ​ 𝐠 I, α ​ ( x, y) \mathbf{g}(x,y)=\sum_{(I,\alpha)\in\mathcal{J}}x_{\overline{I}}^{\gamma_{\overline{I}}}x_{I}^{\alpha}\mathbf{g}_{I,\alpha}(x,y) |  |

and ‖ 𝐠 I, α ​ ( x, y) ‖ ≤ C \|\mathbf{g}_{I,\alpha}(x,y)\|\leq C for all ( x, y) ∈ U (x,y)\in U. We fix p ∈ ℕ p\in\mathbb{N} and write 𝐠 p ​ ( x, y):= ( 𝐠 ⁡ ( x, y)) p \mathbf{g}^{p}(x,y):=(\mathbf{g}(x,y))^{p} for all ( x, y) ∈ U (x,y)\in U. Since

 | 𝐠 p ​ ( x, y) = ∑ ( ( I 1, α 1), …, ( I p, α p)) ∈ 𝒥 p x I 1 α 1 ⋯ x I p α p ⋅ x I 1 ¯ γ I 1 ¯ ⋯ x I p ¯ γ I p ¯ ⋅ 𝐠 I 1, α 1 ( x, y) ⋯ 𝐠 I p, α p ( x, y), \mathbf{g}^{p}(x,y)=\\ \sum_{((I_{1},\alpha_{1}),\dots,(I_{p},\alpha_{p}))\in\mathcal{J}^{p}}x_{I_{1}}^{\alpha_{1}}\cdots x_{I_{p}}^{\alpha_{p}}\cdot x_{\overline{I_{1}}}^{\gamma_{\overline{I_{1}}}}\cdots x_{\overline{I_{p}}}^{\gamma_{\overline{I_{p}}}}\cdot\mathbf{g}_{I_{1},\alpha_{1}}(x,y)\cdots\mathbf{g}_{I_{p},\alpha_{p}}(x,y), |  |

and since each 𝔤 I, α \mathfrak{g}_{I,\alpha} only depends on the variables x I ¯ x_{\overline{I}} and y y, we get that

 | ( 𝐠 p) ( γ, 0) ​ ( x, y) = ∑ ( ( I 1, α 1), …, ( I p, α p)) ∈ 𝒥 p x I 1 α 1 ⋯ x I p α p ⋅ x I 1 ¯ γ I 1 ¯ ⋯ x I p ¯ γ I p ¯ x γ ⋅ 𝐠 I 1, α 1 ( x, y) ⋯ 𝐠 I p, α p ( x, y), (\mathbf{g}^{p})_{(\gamma,0)}(x,y)=\\ \sum_{((I_{1},\alpha_{1}),\dots,(I_{p},\alpha_{p}))\in\mathcal{J}_{p}}\frac{x_{I_{1}}^{\alpha_{1}}\cdots x_{I_{p}}^{\alpha_{p}}\cdot x_{\overline{I_{1}}}^{\gamma_{\overline{I_{1}}}}\cdots x_{\overline{I_{p}}}^{\gamma_{\overline{I_{p}}}}}{x^{\gamma}}\cdot\mathbf{g}_{I_{1},\alpha_{1}}(x,y)\cdots\mathbf{g}_{I_{p},\alpha_{p}}(x,y), |  |

where 𝒥 p \mathcal{J}_{p} is the set of all ( ( I 1, α 1), …, ( I p, α p)) ∈ 𝒥 p ((I_{1},\alpha_{1}),\dots,(I_{p},\alpha_{p}))\in\mathcal{J}^{p} such that the monomial x I 1 α 1 ⋯ x I p α p ⋅ x I 1 ¯ γ I 1 ¯ ⋯ x I p ¯ γ I p ¯ x_{I_{1}}^{\alpha_{1}}\cdots x_{I_{p}}^{\alpha_{p}}\cdot x_{\overline{I_{1}}}^{\gamma_{\overline{I_{1}}}}\cdots x_{\overline{I_{p}}}^{\gamma_{\overline{I_{p}}}} is divisible by x γ x^{\gamma}. As U ⊆ B 𝐋 ​ ( 1) m + n U\subseteq B_{\mathbf{L}}(1)^{m+n}, it follows for all x ∈ U x\in U that

 | ‖ ( 𝐠 p) ( γ, 0) ​ ( x, y) ‖ \displaystyle\left\|(\mathbf{g}^{p})_{(\gamma,0)}(x,y)\right\| | ≤ ∑ ( ( I 1, α 1), …, ( I p, α p)) ∈ 𝒥 p ‖ 𝐠 I 1, α 1 ​ ( x, y) ​ ‖ ⋯ ‖ ​ 𝐠 I p, α p ​ ( x, y) ‖ \displaystyle\leq\sum_{((I_{1},\alpha_{1}),\dots,(I_{p},\alpha_{p}))\in\mathcal{J}^{p}}\|\mathbf{g}_{I_{1},\alpha_{1}}(x,y)\|\cdots\|\mathbf{g}_{I_{p},\alpha_{p}}(x,y)\| |  |

 |  | = ( ∑ ( I, α) ∈ 𝒥 ‖ 𝐠 I, α ​ ( x, y) ‖) p \displaystyle=\left(\sum_{(I,\alpha)\in\mathcal{J}}\|\mathbf{g}_{I,\alpha}(x,y)\|\right)^{p} |  |

 |  | ≤ ( | 𝒥 | ​ C) p. \displaystyle\leq\left(|\mathcal{J}|C\right)^{p}. |  |

It follows from Lemma 1.3 and the Cauchy estimates that

 | ‖ ( b p) ( γ, 0) ​ ( x, y ′) ‖ = 1 p! ​ ‖ ∂ p − 1 ( 𝐠 p) ( γ, 0) ∂ y n p − 1 ​ ( x, y ′, 0) ‖ ≤ ( | 𝒥 | ​ C) p ρ p − 1 \|(b_{p})_{(\gamma,0)}(x,y^{\prime})\|=\frac{1}{p!}\left\|\frac{\partial^{p-1}(\mathbf{g}^{p})_{(\gamma,0)}}{\partial y_{n}^{p-1}}(x,y^{\prime},0)\right\|\leq\frac{\left(|\mathcal{J}|C\right)^{p}}{\rho^{p-1}} |  |

for all ( x, y ′) ∈ V (x,y^{\prime})\in V; so we can take A:= ρ A:=\rho and B:= | 𝒥 | ​ C / ρ B:=|\mathcal{J}|C/\rho.

Finally, let κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} be such that ( κ, 0) ∈ cl 0 ⁡ ( V × B 𝐋 ​ ( ρ / 2)) (\kappa,0)\in\cl_{0}(V\times B_{\mathbf{L}}(\rho/2)). Then 𝐭 ( κ, 0) ​ ( b p) ( γ, 0) ∈ 𝒜 m ​ ( V ′) \mathbf{t}_{(\kappa,0)}(b_{p})_{(\gamma,0)}\in\mathcal{A}_{m}(V^{\prime}) for some appropriate V ′ V^{\prime} independent of p p by Remark 2.7 (2). Since ‖ 𝐭 ( κ, 0) ​ ( b p) ( γ, 0) ​ ( x, y ′) ‖ ≤ A ​ B p \|\mathbf{t}_{(\kappa,0)}(b_{p})_{(\gamma,0)}(x,y^{\prime})\|\leq AB^{p} for all ( x, y ′) ∈ V ′ (x,y^{\prime})\in V^{\prime} by the above, it follows that 𝐭 ( κ, 0) ​ H ( γ, 0) \mathbf{t}_{(\kappa,0)}H_{(\gamma,0)} belongs to 𝒜 m ​ ( V ′ × B 𝐋 ​ ( ρ / 2)) \mathcal{A}_{m}(V^{\prime}\times B_{\mathbf{L}}(\rho/2)), and the proposition is proved. ∎

The case of several implicit variables can be reduced to that of one implicit variable: below, we let l ∈ { 1, …, n } l\in\{1,\dots,n\}, and we write y ′:= ( y 1, …, y n − l) y^{\prime}:=(y_{1},\dots,y_{n-l}), z = ( z 1, …, z l):= ( y n − l + 1, …, y n) z=(z_{1},\dots,z_{l}):=(y_{n-l+1},\dots,y_{n}), Y ′:= ( Y 1, …, Y n − l) Y^{\prime}:=(Y_{1},\dots,Y_{n-l}) and Z = ( Z 1, …, Z l):= ( Y n − l + 1, …, Y n) Z=(Z_{1},\dots,Z_{l}):=(Y_{n-l+1},\dots,Y_{n}).

###### Corollary 6.2 (Implicit Function Theorem).

Let f ∈ ( 𝒬 m) l f\in(\mathcal{Q}_{m})^{l} such that f ⁡ ( 0) = 0 f(0)=0 and ∂ f / ∂ z ⁡ ( 0) ≠ 0 \partial f/\partial z(0)\neq 0. Then there is an h ∈ ( 𝒬 m m + n − l) l h\in(\mathcal{Q}_{m}^{m+n-l})^{l} such that h ⁡ ( 0) = 0 h(0)=0 and f ⁡ ( x, y ′, h) = 0 f(x,y^{\prime},h)=0.

###### Proof.

By induction on l l; the case l = 1 l=1 corresponds to Proposition 6.1, so we assume that n ≥ l > 1 n\geq l>1 and the corollary holds for lower values of l l. After permuting the component functions of f f, we may assume that ∂ f l / ∂ y n ​ ( 0) ≠ 0 \partial f_{l}/\partial y_{n}(0)\neq 0. Hence, writing z ′:= ( y n − l + 1, …, y n − 1) z^{\prime}:=(y_{n-l+1},\dots,y_{n-1}), we obtain from Proposition 6.1 a function w ∈ 𝒬 m m + n − 1 w\in\mathcal{Q}_{m}^{m+n-1} such that f l ​ ( x, y ′, z ′, w) = 0 f_{l}(x,y^{\prime},z^{\prime},w)=0. Moreover, there are constants c 1, …, c l − 1 ∈ ℂ c_{1},\dots,c_{l-1}\in\mathbb{C} such that for each i = 1, …, l − 1 i=1,\dots,l-1, defining f i ′:= f i − c i ​ f l f^{\prime}_{i}:=f_{i}-c_{i}f_{l} gives ( ∂ f i ′ / ∂ y n) ​ ( 0) = 0 (\partial f^{\prime}_{i}/\partial y_{n})(0)=0. By the hypothesis of the corollary, the map g ∈ ( 𝒬 m m + n − 1) l − 1 g\in(\mathcal{Q}_{m}^{m+n-1})^{l-1} defined by

 | g i ​ ( x, y ′, z ′):= f i ′ ​ ( x, y ′, z ′, w ⁡ ( x, y ′, z ′)) for ​ i = 1, …, l − 1 g_{i}(x,y^{\prime},z^{\prime}):=f^{\prime}_{i}(x,y^{\prime},z^{\prime},w(x,y^{\prime},z^{\prime}))\quad\text{for }i=1,\dots,l-1 |  |

satisfies g ⁡ ( 0) = 0 g(0)=0 and ( ∂ g / ∂ z ′) ​ ( 0) ≠ 0 (\partial g/\partial z^{\prime})(0)\neq 0. Hence by the inductive hypothesis, there is an h ′ ∈ ( 𝒬 m m + n − l) l − 1 h^{\prime}\in(\mathcal{Q}_{m}^{m+n-l})^{l-1} such that g ⁡ ( x, y ′, h ′) = 0 g(x,y^{\prime},h^{\prime})=0. The corollary follows with h ∈ ( 𝒬 m m + n − l) l h\in(\mathcal{Q}_{m}^{m+n-l})^{l} defined by h i:= h i ′ h_{i}:=h^{\prime}_{i} if i = 1, …, l − 1 i=1,\dots,l-1 and h l ​ ( x, y ′):= w ⁡ ( x, y ′, h ′ ​ ( x, y ′)) h_{l}(x,y^{\prime}):=w(x,y^{\prime},h^{\prime}(x,y^{\prime})). ∎

For the next proposition, we let σ = ( σ 1, …, σ l) \sigma=(\sigma_{1},\dots,\sigma_{l}) be the elementary symmetric functions in the variables z z. Recall that f ∈ 𝒬 m f\in\mathcal{Q}_{m} is symmetric in the variables z z if f ⁡ ( x, y ′, z) = f ⁡ ( x, y ′, λ ⁡ ( z)) f(x,y^{\prime},z)=f(x,y^{\prime},\lambda(z)) for every permutation λ \lambda of { 1, …, l } \{1,\dots,l\}.

###### Proposition 6.3 (Symmetric Function Theorem).

Let f ∈ 𝒬 m f\in\mathcal{Q}_{m} be symmetric in the variables z z. Then there is a g ∈ 𝒬 m g\in\mathcal{Q}_{m} such that f ⁡ ( x, y ′, z) = g ⁡ ( x, y ′, σ) f(x,y^{\prime},z)=g(x,y^{\prime},\sigma).

###### Proof.

First, let γ ∈ [0, ∞) m \gamma\in[0,\infty)^{m} and assume there is a G ∈ ℂ ⁡ [[X ∗, Y ′, Z]] G\in\mathbb{C}[\![X^{*},Y^{\prime},Z]\!] such that T ​ f ​ ( X, Y ′, Z) = G ⁡ ( X, Y ′, σ 1 ​ ( Z), …, σ l ​ ( Z)) Tf(X,Y^{\prime},Z)=G(X,Y^{\prime},\sigma_{1}(Z),\dots,\sigma_{l}(Z)). Then ( T ​ f) ( γ, 0, 0) (Tf)_{(\gamma,0,0)} is symmetric in Z Z and

 | ( T ​ f) ( γ, 0, 0) ​ ( X, Y ′, Z) = G ( γ, 0, 0) ​ ( X, Y ′, σ 1 ​ ( Z), …, σ l ​ ( Z)). (Tf)_{(\gamma,0,0)}(X,Y^{\prime},Z)=G_{(\gamma,0,0)}(X,Y^{\prime},\sigma_{1}(Z),\dots,\sigma_{l}(Z)). |  |

Moreover, if g ∈ 𝒜 m ​ ( V) g\in\mathcal{A}_{m}(V) is such that f ⁡ ( x, y ′, z) = g ⁡ ( x, y ′, σ) f(x,y^{\prime},z)=g(x,y^{\prime},\sigma), and if κ ∈ [0, ∞) m \kappa\in[0,\infty)^{m} is sufficiently small, then 𝐭 ( κ, 0, 0) ​ f \mathbf{t}_{(\kappa,0,0)}f is symmetric in z z and 𝐭 ( κ, 0, 0) ​ f ​ ( x, y ′, z) = 𝐭 ( κ, 0, 0) ​ g ​ ( x, y ′, σ) \mathbf{t}_{(\kappa,0,0)}f(x,y^{\prime},z)=\mathbf{t}_{(\kappa,0,0)}g(x,y^{\prime},\sigma).

Therefore, we assume that f ∈ 𝒜 m ​ ( U) f\in\mathcal{A}_{m}(U) for some m m -quadratic U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} and we need to find, after shrinking U U if necessary, a g ∈ 𝒜 m ​ ( U) g\in\mathcal{A}_{m}(U) such that f ⁡ ( x, y ′, z) = g ⁡ ( x, y ′, σ 1, …, σ l) f(x,y^{\prime},z)=g(x,y^{\prime},\sigma_{1},\dots,\sigma_{l}) for all ( x, y ′, z) ∈ U (x,y^{\prime},z)\in U. Without loss of generality, we also assume that U = W m × B 𝐋 ​ ( R) n U=W^{m}\times B_{\mathbf{L}}(R)^{n} for some quadratic domain W ⊆ 𝐋 W\subseteq\mathbf{L} and some R > 0 R>0, and we put U ′:= W m × B 𝐋 ​ ( R) n − l U^{\prime}:=W^{m}\times B_{\mathbf{L}}(R)^{n-l}.

By Proposition 2.14, there are a q ∈ 𝒜 m m + n − l ​ ( U ′) a_{q}\in\mathcal{A}_{m}^{m+n-l}(U^{\prime}), for q ∈ ℕ l q\in\mathbb{N}^{l}, and constants B, C > 0 B,C>0 such that ‖ a q ​ ( x, y ′) ‖ ≤ B ​ C | q | \|a_{q}(x,y^{\prime})\|\leq BC^{|q|} for each q q and f ⁡ ( x, y ′, z) = ∑ q ∈ ℕ l a q ​ ( x, y ′) ​ z q f(x,y^{\prime},z)=\sum_{q\in\mathbb{N}^{l}}a_{q}(x,y^{\prime})z^{q}. Let also ∼ \sim be the equivalence relation on ℕ l \mathbb{N}^{l} defined by p ∼ q p\sim q if and only if there is a permutation λ \lambda of { 1, …, l } \{1,\dots,l\} such that p = ( q σ ⁡ ( 1), …, q σ ⁡ ( l)) p=(q_{\sigma(1)},\dots,q_{\sigma(l)}), and let E 1, E 2, … E_{1},E_{2},\dots be an enumeration of all equivalence classes of ∼ \sim. Since f f is symmetric in z z, we get for all j ∈ ℕ j\in\mathbb{N} that a p = a q a_{p}=a_{q} for all p, q ∈ E j p,q\in E_{j}. Thus, for each j ∈ ℕ j\in\mathbb{N}, we define b j:= a p b_{j}:=a_{p} for some p ∈ E j p\in E_{j}; then

 | ∑ p ∈ E j a p ​ ( x, y ′) ​ z p = b j ​ ( x, y ′) ⋅ ∑ p ∈ E j z p for all ​ j ∈ ℕ. \sum_{p\in E_{j}}a_{p}(x,y^{\prime})z^{p}=b_{j}(x,y^{\prime})\cdot\sum_{p\in E_{j}}z^{p}\quad\text{for all }j\in\mathbb{N}. |  |

Let j ∈ ℕ j\in\mathbb{N}, and note that the sum ∑ p ∈ E j z p \sum_{p\in E_{j}}z^{p} is a symmetric polynomial in z z that is homogeneous of degree d j:= | p | d_{j}:=|p| for any p ∈ E j p\in E_{j}. By the main theorem on symmetric polynomials (see for instance Van der Waerden [11]), there is a unique polynomial S j ∈ ℂ ⁡ [Z] S_{j}\in\mathbb{C}[Z] of weighted degree d j d_{j} such that ∑ p ∈ E j z p = S j ​ ( σ 1 ​ ( z), …, σ l ​ ( z)) \sum_{p\in E_{j}}z^{p}=S_{j}(\sigma_{1}(z),\dots,\sigma_{l}(z)). (Here “of weighted degree d j d_{j} ” means that any term c ​ z p cz^{p} occurring in S j S_{j} satisfies p 1 + 2 ​ p 2 + ⋯ + l ​ p l = d j p_{1}+2p_{2}+\cdots+lp_{l}=d_{j}.)

We now define S ∈ ℂ ⁡ [[Z]] S\in\mathbb{C}[\![Z]\!] by S ⁡ ( Z):= ∑ j ∈ ℕ S j ​ ( Z) S(Z):=\sum_{j\in\mathbb{N}}S_{j}(Z); we claim that S S is convergent. To see this, note that the product Π i = 1 l ​ ( 1 − Z i) \Pi_{i=1}^{l}(1-Z_{i}) is a symmetric polynomial; hence, there is a polynomial P ∈ ℂ ⁡ [Z] P\in\mathbb{C}[Z] such that P ⁡ ( σ 1 ​ ( Z), …, σ l ​ ( Z)) = Π i = 1 l ​ ( 1 − Z i) P(\sigma_{1}(Z),\dots,\sigma_{l}(Z))=\Pi_{i=1}^{l}(1-Z_{i}). Since P ⁡ ( 0) ≠ 0 P(0)\neq 0, we have that 1 / P ∈ ℂ ⁡ [[Z]] 1/P\in\mathbb{C}[\![Z]\!] converges; but ( 1 / P) ​ ( σ 1 ​ ( Z), …, σ l ​ ( Z)) = ∑ q ∈ ℕ l z q (1/P)(\sigma_{1}(Z),\dots,\sigma_{l}(Z))=\sum_{q\in\mathbb{N}^{l}}z^{q}, and the claim follows.

We now claim that the sum g ⁡ ( x, y ′, z):= ∑ j ∈ ℕ b j ​ ( x, y ′) ​ S j ​ ( z) g(x,y^{\prime},z):=\sum_{j\in\mathbb{N}}b_{j}(x,y^{\prime})S_{j}(z) defines a function g ∈ 𝒜 m ​ ( U) g\in\mathcal{A}_{m}(U). Assuming the claim holds, we necessarily have T ​ g ​ ( X, Y ′, Z) = G ⁡ ( X, Y ′, Z):= ∑ j ∈ ℕ T ​ b j ​ ( X, Y ′) ​ S j ​ ( Z) Tg(X,Y^{\prime},Z)=G(X,Y^{\prime},Z):=\sum_{j\in\mathbb{N}}Tb_{j}(X,Y^{\prime})S_{j}(Z), so g g has the required properties by the injectivity of the map T T and because T ​ f ​ ( X, Y ′, Z) = G ⁡ ( X, Y ′, σ 1 ​ ( Z), …, σ l ​ ( Z)) Tf(X,Y^{\prime},Z)=G(X,Y^{\prime},\sigma_{1}(Z),\dots,\sigma_{l}(Z)).

To see the claim, we first need to rewrite the sum: for each q ∈ ℕ l q\in\mathbb{N}^{l}, we put D q:= { j ∈ ℕ: q ∈ supp ⁡ S j } D_{q}:=\{j\in\mathbb{N}:\ q\in\supp S_{j}\} and c q:= ∑ j ∈ D q b j c_{q}:=\sum_{j\in D_{q}}b_{j}, so that g ⁡ ( x, y ′, z) = ∑ q ∈ ℕ l c q ​ ( x, y ′) ​ z q g(x,y^{\prime},z)=\sum_{q\in\mathbb{N}^{l}}c_{q}(x,y^{\prime})z^{q} for all ( x, y ′, z) ∈ U (x,y^{\prime},z)\in U. Note that for all q ∈ ℕ l q\in\mathbb{N}^{l}, j ∈ D q j\in D_{q} and p ∈ E j p\in E_{j}, we have | p | = q 1 + 2 ​ q 2 + ⋯ + l ​ q l ≤ l ​ | q | |p|=q_{1}+2q_{2}+\cdots+lq_{l}\leq l|q|. Hence, for each q ∈ ℕ l q\in\mathbb{N}^{l}, there is a set C q ⊆ { r ∈ ℕ l: | r | ≤ l ​ | q | } C_{q}\subseteq\left\{r\in\mathbb{N}^{l}:\ |r|\leq l|q|\right\} such that c q = ∑ r ∈ C q a r c_{q}=\sum_{r\in C_{q}}a_{r}. Since | C q | ≤ ( l ​ | q |) l |C_{q}|\leq(l|q|)^{l}, it follows that there are constants 𝐚, 𝐛 > 0 \mathbf{a},\mathbf{b}>0 such that ‖ c q ​ ( x, y ′) ‖ ≤ 𝐚𝐛 | q | \|c_{q}(x,y^{\prime})\|\leq\mathbf{a}\mathbf{b}^{|q|} for every q ∈ ℕ l q\in\mathbb{N}^{l} and all ( x, y ′) ∈ U ′ (x,y^{\prime})\in U^{\prime}. Since c q ∈ 𝒜 m m + n − l ​ ( U ′) c_{q}\in\mathcal{A}_{m}^{m+n-l}(U^{\prime}) for every q ∈ ℕ l q\in\mathbb{N}^{l}, the claim follows from Proposition 2.15. ∎

For the remainder of this section, we write again Y ′ = ( Y 1, …, Y n − 1) Y^{\prime}=(Y_{1},\dots,Y_{n-1}). We recall from Definition 4.16 of [3] that F ∈ ℂ ⁡ [[X ∗, Y]] F\in\mathbb{C}[\![X^{*},Y]\!] is regular in Y n Y_{n} of order d ∈ ℕ d\in\mathbb{N} if F ⁡ ( 0, 0, Y n) = c ​ Y n d + F(0,0,Y_{n})=cY_{n}^{d}+ terms of higher order in Y n Y_{n}.

###### Proposition 6.4 (Weierstrass Preparation).

Assume that n > 0 n>0, and let f ∈ 𝒬 m f\in\mathcal{Q}_{m} be such that T ​ f Tf is regular in Y n Y_{n} of order d ∈ ℕ d\in\mathbb{N}.

1. (1)

For every g ∈ 𝒬 m g\in\mathcal{Q}_{m}, there are a unique q ∈ 𝒬 m q\in\mathcal{Q}_{m} and a unique r ∈ 𝒬 m m + n − 1 ​ [Y n] r\in\mathcal{Q}_{m}^{m+n-1}[Y_{n}] such that g = q ​ f + r g=qf+r and deg Y n ⁡ ( r) < d \deg_{Y_{n}}(r)<d.

2. (2)

There are a unique unit u ∈ 𝒬 m u\in\mathcal{Q}_{m} and a unique w ∈ 𝒬 m m + n − 1 ​ [Y n] w\in\mathcal{Q}_{m}^{m+n-1}[Y_{n}] such that f = u ​ w f=uw and w w is monic of degree d d in Y n Y_{n}.

###### Proof.

The proof of Theorems 1 and 2 on p. 338 of [1] goes through almost literally, using the properties established for the classes 𝒬 m \mathcal{Q}_{m} in the previous sections as well as the Implicit Function Theorem and the Symmetric Function Theorem above, except for the following trivial changes: the variable t t and z 1, …, z n z_{1},\dots,z_{n} there correspond to y n y_{n} and x 1, …, x m, y 1, …, y n − 1 x_{1},\dots,x_{m},y_{1},\dots,y_{n-1} here, and the roles of f f and g g are exchanged. (Note that the uniqueness also follows directly from Proposition 4.17 in [3] and the injectivity of the map T: 𝒬 m ⟶ ℂ ⁡ [[X ∗, Y]] T:\mathcal{Q}_{m}\longrightarrow\mathbb{C}[\![X^{*},Y]\!].) ∎

## 7. 𝒬 \mathcal{Q} -semianalytic sets and model completeness

In this section we prove model completeness and o-minimality of ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. We also show that ℝ 𝒬 \mathbb{R}_{\mathcal{Q}} admits analytic cell decomposition. (An o-minimal expansion ℝ ~ \,\widetilde{\mathbb{R}}\, of the ordered field of real numbers is said to admit analytic cell decomposition if for any A 1, …, A k ⊆ ℝ m A_{1},\dots,A_{k}\subseteq\mathbb{R}^{m} definable in ℝ ~ \,\widetilde{\mathbb{R}}\,, there is a decomposition of ℝ m \mathbb{R}^{m} into analytic cells definable in ℝ ~ \,\widetilde{\mathbb{R}}\, and compatible with each A i A_{i}.)

We let m, n ∈ ℕ m,n\in\mathbb{N} and ρ ∈ ( 0, ∞) m + n \rho\in(0,\infty)^{m+n}, and we put

 | I m, n; ρ:= [0, ρ 1] × ⋯ × [0, ρ m] × [− ρ m + 1, ρ m + 1] × ⋯ × [− ρ m + n, ρ m + n], I_{m,n;\rho}:=[0,\rho_{1}]\times\cdots\times[0,\rho_{m}]\times[-\rho_{m+1},\rho_{m+1}]\times\cdots\times[-\rho_{m+n},\rho_{m+n}], |  |

a subset of ℝ m + n \mathbb{R}^{m+n}. We also write I m, n; ϵ I_{m,n;\epsilon} instead of I m, n; ( ϵ, …, ϵ) I_{m,n;(\epsilon,\dots,\epsilon)}, for ϵ > 0 \epsilon>0, and we put I m, n; ∞:= [0, ∞) m × ℝ n I_{m,n;\infty}:=[0,\infty)^{m}\times\mathbb{R}^{n}. Abusing notation, we identify I m, n; ρ I_{m,n;\rho} with the set

 | { ( x, y) ∈ [0, ∞) 𝐋 0 m × ℝ n: 0 ≤ ∥ x i ∥ ≤ ρ i and − ρ m + j ≤ y j ≤ ρ m + j for i = 1, …, m and j = 1, …, n }. \{(x,y)\in[0,\infty)_{\mathbf{L}_{0}}^{m}\times\mathbb{R}^{n}:\ 0\leq\|x_{i}\|\leq\rho_{i}\text{ and }\\ -\rho_{m+j}\leq y_{j}\leq\rho_{m+j}\ \text{for }i=1,\dots,m\text{ and }j=1,\dots,n\}. |  |

Given an m m -quadratic U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} such that I m, n; ρ ⊆ int ⁡ ( cl ⁡ ( π m m + n ​ ( U)) CLOSE I_{m,n;\rho}\subseteq\ir(\cl(\pi^{m+n}_{m}(U)), and given an f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U), we write f | I m, n; ρ f|_{I_{m,n;\rho}} for the function f ♯ | I m, n; ρ f^{\sharp}|_{I_{m,n;\rho}}.

###### Definition 7.1.

We let 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} be the set of all functions f: I m, n; ρ ⟶ ℝ f:I_{m,n;\rho}\longrightarrow\mathbb{R} for which there exist an m m -quadratic domain U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} and a g ∈ 𝒬 m ​ ( U) g\in\mathcal{Q}_{m}(U) such that I m, n; ρ ⊆ int ⁡ ( cl ⁡ ( π m m + n ​ ( U)) CLOSE I_{m,n;\rho}\subseteq\ir(\cl(\pi^{m+n}_{m}(U)) and f = g | I m, n; ρ f=g|_{I_{m,n;\rho}}.

###### Remark 7.2.

For every f ∈ 𝒬 m, n; ρ f\in\mathcal{Q}_{m,n;\rho}, there are ρ ′ > ρ \rho^{\prime}>\rho and g ∈ 𝒬 m, n, ρ ′ g\in\mathcal{Q}_{m,n,\rho^{\prime}} such that f = g | I m, n; ρ f=g|_{I_{m,n;\rho}}.

###### Proposition 7.3.

Let U ⊆ 𝐋 m + n U\subseteq\mathbf{L}^{m+n} be m m -quadratic such that I m, n; ρ ⊆ int ⁡ ( cl ⁡ ( π m m + n ​ ( U)) 𝐶𝐿𝑂𝑆𝐸 I_{m,n;\rho}\subseteq\ir(\cl(\pi^{m+n}_{m}(U)), and let f ∈ 𝒬 m ​ ( U) f\in\mathcal{Q}_{m}(U). Then f | I m, n; ρ ∈ 𝒬 m, n; ρ f|_{I_{m,n;\rho}}\in\mathcal{Q}_{m,n;\rho} if and only if T ​ f ∈ ℝ ⁡ [[X ∗, Y]] Tf\in\mathbb{R}[\![X^{*},Y]\!].

###### Proof.

The necessity is clear from Definition 2.6, so we assume that T ​ f ∈ ℝ ⁡ [[X ∗, Y]] Tf\in\mathbb{R}[\![X^{*},Y]\!]. Define ( r, φ) ¯:= ( r, − φ) \overline{(r,\varphi)}:=(r,-\varphi) for ( r, φ) ∈ 𝐋 (r,\varphi)\in\mathbf{L} and ( x, y) ¯:= ( x 1 ¯, …, y n ¯) \overline{(x,y)}:=(\overline{x_{1}},\dots,\overline{y_{n}}) for ( x, y) ∈ 𝐋 m + n (x,y)\in\mathbf{L}^{m+n}. Then the function f ¯: U ⟶ ℂ \overline{f}:U\longrightarrow\mathbb{C} defined by f ¯ ​ ( x):= f ⁡ ( x ¯) ¯ \overline{f}(x):=\overline{f(\overline{x})} belongs to 𝒜 ⁡ ( U) \mathcal{A}(U) and satisfies T ⁡ ( f ¯) = T ​ f T\left(\overline{f}\right)=Tf. Hence by Proposition 2.8, we have f ¯ = f \overline{f}=f, which proves the proposition. ∎

Correspondingly, we put ℝ ​ { X ∗, Y } 𝒬, ρ:= { T ​ f: f ∈ 𝒬 m, n; ρ } \mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\rho}:=\left\{Tf:\ f\in\mathcal{Q}_{m,n;\rho}\right\}. If ϵ > 0 \epsilon>0, we write ℝ ​ { X ∗, Y } 𝒬, ϵ \mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\epsilon} and 𝒬 m, n; ϵ \mathcal{Q}_{m,n;\epsilon} instead of ℝ ​ { X ∗, Y } 𝒬, ( ϵ, …, ϵ) \mathbb{R}\{X^{*},Y\}_{\mathcal{Q},(\epsilon,\dots,\epsilon)} and 𝒬 m, n; ( ϵ, …, ϵ) \mathcal{Q}_{m,n;(\epsilon,\dots,\epsilon)}. Next, we put

 | ℝ ​ { X ∗, Y } 𝒬:= ⋃ ρ ∈ ( 0, ∞) m + n ℝ ​ { X ∗, Y } 𝒬, ρ. \mathbb{R}\{X^{*},Y\}_{\mathcal{Q}}:=\bigcup_{\rho\in(0,\infty)^{m+n}}\mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\rho}. |  |

For n = 0 n=0 we just write ℝ ​ { X ∗ } 𝒬, ρ \mathbb{R}\{X^{*}\}_{\mathcal{Q},\rho} instead of ℝ ​ { X ∗, Y } 𝒬, ρ \mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\rho}.

The properties described Sections 5, 6 and 4 of the algebras 𝒬 m ​ ( U) \mathcal{Q}_{m}(U) are easily seen to imply corresponding properties of the algebras 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} and ℝ ​ { X ∗, Y } 𝒬, ρ \mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\rho}. Due to Proposition 5.11, we need no longer formally distinguish between f ∈ 𝒬 m, n; ρ f\in\mathcal{Q}_{m,n;\rho} and T ​ f ∈ ℝ ​ { X ∗, Y } 𝒬, ρ Tf\in\mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\rho}; in particular, the notations in Sections 7, 8 and 9 of [3] make sense in our setting.

###### Definition 7.4.

A set A ⊆ I m, n; ρ A\subseteq I_{m,n;\rho} is called a basic 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} -set if there are f, g 1, …, g k ∈ 𝒬 m, n; ρ f,g_{1},\dots,g_{k}\in\mathcal{Q}_{m,n;\rho} such that

 | A = { z ∈ I m, n; ρ: f ( z) = 0, g 1 ( z) > 0, …, g k ( z) > 0 }. A=\left\{z\in I_{m,n;\rho}:\ f(z)=0,\ g_{1}(z)>0,\dots,\ g_{k}(z)>0\right\}. |  |

A 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} -set is a finite union of basic 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} -sets. Note that the 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} -sets form a boolean algebra of subsets of I m, n; ρ I_{m,n;\rho}.

Given a point a = ( a 1, …, a m + n) ∈ ℝ m + n a=(a_{1},\dots,a_{m+n})\in\mathbb{R}^{m+n} and a choice of signs σ ∈ { − 1, 1 } m \sigma\in\{-1,1\}^{m}, we let h a, σ: ℝ m + n ⟶ ℝ m + n h_{a,\sigma}:\ \mathbb{R}^{m+n}\longrightarrow\mathbb{R}^{m+n} be the bijection given by

 | h a, σ ​ ( z):= ( a 1 + σ 1 ​ z 1, …, a m + n + z m + n). h_{a,\sigma}(z):=\left(a_{1}+\sigma_{1}z_{1},\dots,a_{m+n}+z_{m+n}\right). |  |

Note that the maps h a, σ h_{a,\sigma} (with a ∈ ℝ m + n a\in\mathbb{R}^{m+n} and σ ∈ { − 1, 1 } m \sigma\in\{-1,1\}^{m}) form a group of permutations of ℝ m + n \mathbb{R}^{m+n}.

###### Definition 7.5.

A set X ⊆ ℝ m + n X\subseteq\mathbb{R}^{m+n} is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic at a ∈ ℝ m + n a\in\mathbb{R}^{m+n} if there is an ϵ > 0 \epsilon>0 such that for each σ ∈ { − 1, 1 } m \sigma\in\{-1,1\}^{m} there is a 𝒬 m, n; ϵ \mathcal{Q}_{m,n;\epsilon} -set A σ ⊆ I m, n; ϵ A_{\sigma}\subseteq I_{m,n;\epsilon} with

 | X ∩ h a, σ ​ ( I m, n; ϵ) = h a, σ ​ ( A σ). X\cap h_{a,\sigma}(I_{m,n;\epsilon})=h_{a,\sigma}(A_{\sigma}). |  |

A set X ⊆ ℝ m + n X\subseteq\mathbb{R}^{m+n} is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic if it is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic at every point a ∈ ℝ m + n a\in\mathbb{R}^{m+n}. For convenience, if X ⊆ ℝ m X\subseteq\mathbb{R}^{m} is 𝒬 m, 0 \mathcal{Q}_{m,0} -semianalytic we also simply say that X X is 𝒬 m \mathcal{Q}_{m} -semianalytic.

###### Remark 7.6.

1. (1)

If X, Y ⊆ ℝ m + n X,Y\subseteq\mathbb{R}^{m+n} are 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic at a a, then so are X ∪ Y X\cup Y, X ∩ Y X\cap Y and X ∖ Y X\setminus Y.

2. (2)

Let X ⊆ ℝ m + n X\subseteq\mathbb{R}^{m+n} be 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic, a ∈ ℝ m + n a\in\mathbb{R}^{m+n} and σ ∈ { − 1, 1 } m \sigma\in\{-1,1\}^{m}. Then the set h a, σ ​ ( X) h_{a,\sigma}(X) is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic. Moreover by Lemma 5.5 (3), for each λ ∈ ( 0, ∞) m + n \lambda\in(0,\infty)^{m+n} the set E λ ​ ( X) E_{\lambda}(X) is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic, where E λ: ℝ m + n ⟶ ℝ m + n E_{\lambda}:\mathbb{R}^{m+n}\longrightarrow\mathbb{R}^{m+n} is defined by E λ ​ ( z):= ( λ 1 ​ z 1, …, λ m + n ​ z m + n) E_{\lambda}(z):=(\lambda_{1}z_{1},\dots,\lambda_{m+n}z_{m+n}).

3. (3)

If X ⊆ ℝ n X\subseteq\mathbb{R}^{n} is semianalytic, then X X is 𝒬 0, n \mathcal{Q}_{0,n} -semianalytic.

Below we write 0 0 for the point ( 0, …, 0) ∈ ℝ m + n (0,\dots,0)\in\mathbb{R}^{m+n}. The following lemma is now proved just as in [3, Section 7] with obvious changes: “ ℛ … \mathcal{R}_{\dots} -set” is replaced by “ 𝒬 … \mathcal{Q}_{\dots} -set”, ℝ ​ { X ∗, Y } \mathbb{R}\{X^{*},Y\} by ℝ ​ { X ∗, Y } 𝒬 \mathbb{R}\{X^{*},Y\}_{\mathcal{Q}} and the algebras ℛ m, n, … \mathcal{R}_{m,n,\dots} by 𝒬 m, n; … \mathcal{Q}_{m,n;\dots}. Also, the results from Sections 4, 5 and 6 there need to be replaced by the corresponding results of Sections 5, 6 and 4 here. (For example, we use Proposition 5.6 (2) here in place of Corollary 6.7 there; the other replacements are more straightforward.)

###### Lemma 7.7.

1. (1)

Let A ⊆ ℝ m + n A\subseteq\mathbb{R}^{m+n} be 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic at 0 0 and let σ \sigma be a permutation of { 1, …, m } \left\{1,\dots,m\right\}. Then σ ⁡ ( A) \sigma(A) is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic at 0 0.

2. (2)

If n ≥ 1 n\geq 1, then each 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic subset of ℝ m + n \,\mathbb{R}^{m+n} is also 𝒬 m + 1, n − 1 \mathcal{Q}_{m+1,n-1} -semianalytic.

3. (3)

Every 𝒬 m, n; ρ \mathcal{Q}_{m,n;\rho} -set A ⊆ I m, n; ρ A\subseteq I_{m,n;\rho} is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic. ∎

Note that Remark 7.6 (3) and Lemma 7.7 (2) imply in particular that every semianalytic subset of ℝ m + n \mathbb{R}^{m+n} is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic. Also, since every f ∈ ℛ m, n, ρ f\in\mathcal{R}_{m,n,\rho} extends to a holomorphic function g: B 𝐋 ​ ( ρ ′) ⟶ ℂ g:B_{\mathbf{L}}(\rho^{\prime})\longrightarrow\mathbb{C} for some ρ ′ > ρ \rho^{\prime}>\rho, we see that ℛ m, n, ρ ω ⊆ 𝒬 m, n; ρ \mathcal{R}_{m,n,\rho}^{\omega}\subseteq\mathcal{Q}_{m,n;\rho}, where ℛ m, n, ρ ω \mathcal{R}_{m,n,\rho}^{\omega} consists of all f ∈ ℛ m, n, ρ f\in\mathcal{R}_{m,n,\rho} with natural support. In particular, every ℛ m, n ω \mathcal{R}_{m,n}^{\omega} -semianalytic subset of ℝ m + n \mathbb{R}^{m+n} is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic.

We now consider the system Λ = ( Λ p) p ∈ ℕ \Lambda=(\Lambda_{p})_{p\in\mathbb{N}}, where

 | Λ p:= { A ⊆ I p: A ​ is ​ 𝒬 p ​ -semianalytic }. \Lambda_{p}:=\left\{A\subseteq I^{p}:\ A\text{ is }\mathcal{Q}_{p}\text{-semianalytic}\right\}. |  |

Note that if A ⊆ I p A\subseteq I^{p} is 𝒬 m, n \mathcal{Q}_{m,n} -semianalytic with m + n = p m+n=p, then A A is also 𝒬 p \mathcal{Q}_{p} -semianalytic by Lemma 7.7 (2), so A ∈ Λ p A\in\Lambda_{p}. A set A ⊆ ℝ m A\subseteq\mathbb{R}^{m} is called a Λ \Lambda -set if A ∈ Λ n A\in\Lambda_{n}, and B ⊆ ℝ m B\subseteq\mathbb{R}^{m} is called a sub- Λ \Lambda -set if there exist n ∈ ℕ n\in\mathbb{N} and a Λ \Lambda -set A ⊆ ℝ m + n A\subseteq\mathbb{R}^{m+n} such that B = Π m ​ ( A) B=\Pi_{m}(A).

###### Proposition 7.8.

Let A ⊆ [− 1, 1] m A\subseteq[-1,1]^{m} be a sub- Λ \Lambda -set. Then [− 1, 1] m ∖ A [-1,1]^{m}\setminus A is also a sub- Λ \Lambda -set.

###### Sketch of proof.

By Theorem 2.7 of [3], we need to establish Axioms (I)-(IV) listed in [3, Section 2]; the first three are straightforward. For Axiom (IV), the proof proceeds almost literally as for [3, Corollary 8.15], with the obvious changes indicated earlier, as well as the following: ℝ ​ { X ∗, Y } … \mathbb{R}\{X^{*},Y\}_{\dots} there is replaced by ℝ ​ { X ∗, Y } 𝒬, … \mathbb{R}\{X^{*},Y\}_{\mathcal{Q},\dots} here, and the facts of Section 7 here are used in place of the corresponding facts from Section 7 there. Moreover, note that Lemma 6.1 there goes through unchanged here. ∎

Recall that by the remarks after Definition 7.1,

 | ℝ 𝒬 = ( ℝ, <, 0, 1, +, −, ⋅, ( f ~: f ∈ 𝒬 m, 0; 1)). \mathbb{R}_{\mathcal{Q}}=\left(\mathbb{R},<,0,1,+,-,\ \!\cdot\ \!,\left(\widetilde{f}:\ f\in\mathcal{Q}_{m,0;1}\right)\right). |  |

It is clear from Remark 7.6 (2) that every bounded 𝒬 p \ \mathcal{Q}_{p} -semianalytic set, for p ∈ ℕ p\in\mathbb{N}, is quantifier-free definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. We are now ready to prove Theorem A.

###### Theorem 7.9.

The expansion ℝ 𝒬 \mathbb{R}_{\mathcal{Q}} is model complete, o-minimal and admits analytic cell decomposition.

###### Proof.

The theorem follows from the previous remark in view of Propositions 7.8 above and [3, Corollary 2.9]. For analytic cell decomposition, we proceed exactly as in the proof of Corollary 6.10 of [4]. ∎

For Theorem B, we proceed as in Section 9 of [3], with the following changes: we do not need 9.3 there, and use Corollaries 5.14 and 5.17 here in place of Lemma 9.4 there. Moreover, we do not need 9.7 and Lemma 9.8 there, and we give a much simpler proof of Lemma 9.9 there:

###### Lemma 7.10.

Let 0 < f ∈ ℝ ​ { T ∗ } 𝒬 0<f\in\mathbb{R}\{T^{*}\}_{\mathcal{Q}} with f ⁡ ( 0) = 0 f(0)=0. Then there exists g ∈ ℝ ​ { T ∗ } 𝒬 g\in\mathbb{R}\{T^{*}\}_{\mathcal{Q}} such that g > 0 g>0, g ⁡ ( 0) = 0 g(0)=0 and f ⁡ ( g ⁡ ( T)) = T f(g(T))=T.

###### Proof.

By the hypotheses, there are λ, α > 0 \lambda,\alpha>0 and h ∈ ℝ ​ { T ∗ } 𝒬 h\in\mathbb{R}\{T^{*}\}_{\mathcal{Q}} such that f ⁡ ( t) = t α ​ ( λ + h ⁡ ( t)) f(t)=t^{\alpha}(\lambda+h(t)) and h ⁡ ( 0) = 0 h(0)=0. We put ρ:= 1 / α \rho:=1/\alpha and let F, H ∈ ℝ ​ { T ∗, Y ∗ } 𝒬 F,H\in\mathbb{R}\{T^{*},Y^{*}\}_{\mathcal{Q}} be defined by F ⁡ ( T, Y):= f ⁡ ( Y) F(T,Y):=f(Y) and H ⁡ ( T, Y):= h ⁡ ( Y) H(T,Y):=h(Y). By Proposition 5.15, the functions 𝐫 ρ, λ ​ F ​ ( t, y) \mathbf{r}^{\rho,\lambda}F(t,y) and 𝐫 ρ, λ ​ H ​ ( t, y) \mathbf{r}^{\rho,\lambda}H(t,y) belong to ℝ ​ { T ∗, Y } 𝒬 \mathbb{R}\{T^{*},Y\}_{\mathcal{Q}}. We define

 | ϕ ⁡ ( t, y):= ( λ + y) α ​ ( λ + 𝐫 ρ, λ ​ H ​ ( t, y)); \phi(t,y):=(\lambda+y)^{\alpha}\left(\lambda+\mathbf{r}^{\rho,\lambda}H(t,y)\right); |  |

then 𝐫 ρ, λ ​ F ​ ( t, y) = t ⋅ ϕ ⁡ ( t, y) \mathbf{r}^{\rho,\lambda}F(t,y)=t\cdot\phi(t,y), so ϕ ∈ ℝ ​ { T ∗, Y } 𝒬 \phi\in\mathbb{R}\{T^{*},Y\}_{\mathcal{Q}} by Proposition 5.6 (1). Moreover, we have ϕ ⁡ ( 0, 0) = λ α + 1 \phi(0,0)=\lambda^{\alpha+1} and ∂ ϕ ∂ y ​ ( 0, 0) = α ​ λ α > 0 \frac{\partial\phi}{\partial y}(0,0)=\alpha\lambda^{\alpha}>0; hence by the implicit function theorem, there is a ψ ∈ ℝ ​ { T ∗ } 𝒬 \psi\in\mathbb{R}\{T^{*}\}_{\mathcal{Q}} such that ϕ ⁡ ( t, ψ ⁡ ( t)) = 1 \phi(t,\psi(t))=1. Therefore, we have 𝐫 ρ, λ ​ F ​ ( t, ψ ⁡ ( t)) = t \mathbf{r}^{\rho,\lambda}F(t,\psi(t))=t, so we take g ⁡ ( t):= t 1 / α ​ ( λ + ψ ⁡ ( t)) g(t):=t^{1/\alpha}(\lambda+\psi(t)). ∎

Using this lemma in place of Lemma 9.9 in [3], we finish the proof of Theorem B as it is done there, and we obtain corresponding corollaries for 1 1 -dimensional sets definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}.

## 8. Example of a definable family of transition maps

Let ξ \xi be an analytic vector field in ℝ 2 \mathbb{R}^{2}. A polycycle Γ \Gamma of ξ \xi is a cyclically ordered finite set of singular points p 0 = p k, p 1, …, p k, p k + 1 = p 1 p_{0}=p_{k},p_{1},\dots,p_{k},p_{k+1}=p_{1} (with possible repetitions), called vertices, and trajectories γ 1, …, γ k \gamma_{1},\dots,\gamma_{k}, called separatrices, connecting the vertices in the order following the flow of ξ \xi, as in Figure 2. We assume here that each p i p_{i} is a non-resonant hyperbolic singularity of ξ \xi. For each i i, we fix two segments Λ i − \Lambda_{i}^{-} and Λ i + \Lambda_{i}^{+} transverse to ξ \xi and intersecting the separatrices γ i − 1 \gamma_{i-1} and γ i \gamma_{i}, respectively, close to p i p_{i}.

-6.8,-8)(8,8) \pstVerb 1 setlinejoin (-5.0614,5.4825)(0.15,0.15) (5.7456,6.1491)(0.15,0.15) (5.9036,-4.7982)(0.15,0.15) (-5.1842,-6.2544)(0.15,0.15) (-5.4123,-1.0614)(0.15,0.15)

Figure 2. The polycycle Γ \Gamma of ξ = ξ 0 \xi=\xi_{0}

For each i i, we fix analytic charts x i: ( − 1, 1) ⟶ Λ i − x_{i}:(-1,1)\longrightarrow\Lambda_{i}^{-} and y i: ( − 1, 1) ⟶ Λ i + y_{i}:(-1,1)\longrightarrow\Lambda_{i}^{+} such that x i ​ ( 0) x_{i}(0) and y i ​ ( 0) y_{i}(0) are the points of intersection of Λ i − \Lambda_{i}^{-} with γ i − 1 \gamma_{i-1} and of Λ i + \Lambda_{i}^{+} with γ i \gamma_{i}, respectively, and such that x i ​ ( t) x_{i}(t) and y i ​ ( t) y_{i}(t) lie inside the region circumscribed by Γ \Gamma for all t ∈ ( 0, 1) t\in(0,1). We denote by g i: ( 0, 1) ⟶ ( 0, 1) g_{i}:(0,1)\longrightarrow(0,1) the corresponding transition map in the coordinates x i x_{i} and y i y_{i}; we extend g i g_{i} to all of ( − 1, 1) (-1,1) by putting g i ​ ( t):= 0 g_{i}(t):=0 for t ∈ ( − 1, 0] t\in(-1,0]. After an analytic change of coordinates if necessary, it follows from the general theory of analytic differential equations that there are analytic functions f i: ( − 1, 1) ⟶ ( − 1, 1) f_{i}:(-1,1)\longrightarrow(-1,1), for i = 1, …, k i=1,\dots,k, representing the flow of ξ \xi from Λ i − 1 + \Lambda_{i-1}^{+} to Λ i − \Lambda_{i}^{-} in the charts y i − 1 y_{i-1} and x i x_{i}. In fact, these functions f i f_{i} are restricted analytic, that is, they extend analytically to a neighbourhood of [− 1, 1] [-1,1]; in particular, they are definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. The restriction of P:= f k ∘ g k ∘ f k − 1 ∘ ⋯ ∘ f 1 ∘ g 1 P:=f_{k}\circ g_{k}\circ f_{k-1}\circ\cdots\circ f_{1}\circ g_{1} to ( 0, 1) (0,1) represents the Poincaré first return map of ξ \xi at p 1 p_{1} in the chart x 1 x_{1}.

By the corollary and the explanations in the introduction each g i g_{i}, and hence P P, is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. Our goal in this section is to show that for certain analytic unfoldings ξ μ \xi_{\mu} of the vector field ξ \xi, the corresponding Poincaré return map with parameter μ \mu is also definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}.

More precisely, we let ξ μ \xi_{\mu} be an analytic unfolding of ξ \xi, with μ ∈ ℝ p \mu\in\mathbb{R}^{p} and ξ 0 = ξ \xi_{0}=\xi, defined in a neighborhood U U of Γ \Gamma containing each Λ i − \Lambda_{i}^{-} and Λ i + \Lambda_{i}^{+}, with the same singular points inside U U and with the same linear part at each of these singular points as ξ \xi. We assume that the unfolding is small, in the sense that for each μ ∈ ℝ p \mu\in\mathbb{R}^{p} and each i ∈ { 1, …, k } i\in\{1,\dots,k\}, both Λ i − \Lambda_{i}^{-} and Λ i + \Lambda_{i}^{+} remain transverse to ξ μ \xi_{\mu}, the transition map of ξ μ \xi_{\mu} at p i p_{i} is given by a function g μ, i: ( 0, 1) ⟶ ( 0, 1) g_{\mu,i}:(0,1)\longrightarrow(0,1) in the charts x i x_{i} and y i y_{i} (with the latter as above, independent of μ \mu), and there are analytic functions f μ, i: ( − 1, 1) ⟶ ( − 1, 1) f_{\mu,i}:(-1,1)\longrightarrow(-1,1) representing the flow of ξ μ \xi_{\mu} from Λ i − 1 + \Lambda_{i-1}^{+} to Λ i − \Lambda_{i}^{-} in the charts y i − 1 y_{i-1} and x i x_{i}. We extend each g μ, i g_{\mu,i} to ( − 1, 1) (-1,1) by putting g μ, i ​ ( t):= 0 g_{\mu,i}(t):=0 if t ∈ ( − 1, 0] t\in(-1,0]. Then the restriction of P μ:= f μ, k ∘ g μ, k ∘ f μ, k − 1 ∘ ⋯ ∘ f μ, 1 ∘ g μ, 1 P_{\mu}:=f_{\mu,k}\circ g_{\mu,k}\circ f_{\mu,k-1}\circ\cdots\circ f_{\mu,1}\circ g_{\mu,1} to ( 0, 1) (0,1) represents the Poincaré first return map of ξ μ \xi_{\mu} at p 1 p_{1} in the chart x 1 x_{1}.

We define g i: ( − 1, 1) × ℝ p ⟶ ( − 1, 1) g_{i}:(-1,1)\times\mathbb{R}^{p}\longrightarrow(-1,1), f i: ( − 1, 1) × ℝ p ⟶ ( − 1, 1) f_{i}:(-1,1)\times\mathbb{R}^{p}\longrightarrow(-1,1) and P: ( − 1, 1) × ℝ p ⟶ ( − 1, 1) P:(-1,1)\times\mathbb{R}^{p}\longrightarrow(-1,1) by g i ​ ( t, μ):= g μ, i ​ ( t) g_{i}(t,\mu):=g_{\mu,i}(t), f i ​ ( t, μ):= f μ, i ​ ( t) f_{i}(t,\mu):=f_{\mu,i}(t) and P ⁡ ( t, μ):= P μ ​ ( t) P(t,\mu):=P_{\mu}(t). Since the chosen unfolding ξ μ \xi_{\mu} is small, each f i f_{i} is a restricted analytic map and hence definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. Moreover, we have the following:

###### Proposition 8.1.

Each g i g_{i} is definable in the structure ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. In particular, P P is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}, and the number of isolated fixed points of P μ P_{\mu} is uniformly bounded in μ \mu.

For the proof of this proposition, we assume that p 1 = 0 ∈ ℝ 2 p_{1}=0\in\mathbb{R}^{2} and show that g 1 g_{1} is definable in ℝ 𝒬 \mathbb{R}_{\mathcal{Q}}. First, since the ratio λ = λ 2 / λ 1 \lambda=\lambda_{2}/\lambda_{1} of the eigenvalues λ 1 \lambda_{1} (with respect to x 1 x_{1}) and λ 2 \lambda_{2} (with respect to OPEN y 1) y_{1}) of ξ μ \xi_{\mu} at 0 0 is irrational and independent of μ \mu, we may assume, after a change of coordinates that is analytic in both ( x, y) (x,y) and μ \mu, that the incoming and outgoing separatrices of ξ μ \xi_{\mu} at 0 0 are represented by the x x -axis and the y y -axis, respectively, for every μ \mu. In this situation, the normalization method in [5, pp. 70–73] goes through uniformly in the parameter μ \mu and yields:

###### Lemma 8.2.

Let N ∈ ℕ N\in\mathbb{N} be positive. Then there exist analytic functions ϕ N, A N: ℝ 2 + p ⟶ ℝ \phi_{N},A_{N}:\mathbb{R}^{2+p}\longrightarrow\mathbb{R} such that A N ​ ( 0, 0, 0) = 0 A_{N}(0,0,0)=0, the map Φ N: ℝ 2 + p ⟶ ℝ 2 + p \Phi^{N}:\mathbb{R}^{2+p}\longrightarrow\mathbb{R}^{2+p} defined by ( u, v, μ) = Φ N ​ ( x, y, μ):= ( x, ϕ N ​ ( x, y, μ), μ) (u,v,\mu)=\Phi^{N}(x,y,\mu):=(x,\phi_{N}(x,y,\mu),\mu) is a change of coodinates fixing 0 0 and for each μ ∈ ℝ p \mu\in\mathbb{R}^{p}, the push-forward Φ ∗ N ​ ξ μ \Phi^{N}_{*}\xi_{\mu} satisfies the equations

(8.1) |  | u ˙ = u v ˙ = v ⁡ ( λ + u N ​ v N ​ A N ​ ( u, v, μ)). ∎ \begin{split}\dot{u}&=u\\ \dot{v}&=v\left(\lambda+u^{N}v^{N}A_{N}\left(u,v,\mu\right)\right).\qed\end{split} |  |

Second, we fix a segment Λ −:= ( 0, ϵ) × { y 0 } \Lambda^{-}:=(0,\epsilon)\times\{y_{0}\}, parametrized by the x x -coordinate along Λ − \Lambda^{-}, and a segment Λ +:= { x 0 } × ( 0, ϵ) \Lambda^{+}:=\{x_{0}\}\times(0,\epsilon), parametrized by the y y -coordinate along Λ + \Lambda^{+}. We assume that x 0 x_{0}, y 0 y_{0} and ϵ \epsilon are small enough such that Λ − \Lambda^{-} and Λ + \Lambda^{+} are transverse to each Φ ∗ N ​ ξ μ \Phi_{*}^{N}\xi_{\mu}. We denote by g μ N: ( 0, ϵ) ⟶ ( 0, ϵ) g^{N}_{\mu}:(0,\epsilon)\longrightarrow(0,\epsilon) the corresponding transition map of Φ ∗ N ​ ξ μ \Phi_{*}^{N}\xi_{\mu}, and we define g N: ( 0, ϵ) × ℝ p ⟶ ( 0, ϵ) g^{N}:(0,\epsilon)\times\mathbb{R}^{p}\longrightarrow(0,\epsilon) by g N ​ ( t, μ):= g μ N ​ ( t) g^{N}(t,\mu):=g^{N}_{\mu}(t). In this situation, the estimates obtained on pp. 24–29 in [7] go through uniformly in μ \mu; in particular, the domain Ω \Omega defined by inequality ( ∗ ⁣ ∗ ∗) (\overset{*}{{}_{**}}) on p. 29 is independent of μ \mu. Therefore, we obtain:

###### Lemma 8.3.

Let ν > 0 \nu>0. Then there exist an integer N = N ⁡ ( ν) > 0 N=N(\nu)>0, constants K = K ⁡ ( ν) > 0 K=K(\nu)>0 and ϵ = ϵ ⁡ ( ν) > 0 \epsilon=\epsilon(\nu)>0 and a quadratic domain Ω = Ω ⁡ ( ν) \Omega=\Omega(\nu) such that

1. (1)

the map g N g^{N} is analytic in the variable μ \mu and admits an analytic extension to Ω × ℝ p \Omega\times\mathbb{R}^{p};

2. (2)

| g N ​ ( t, μ) − t λ | ≤ K ​ | t | ν + ϵ \left|g^{N}(t,\mu)-t^{\lambda}\right|\leq K|t|^{\nu+\epsilon} for all ( t, μ) ∈ Ω × ℝ p (t,\mu)\in\Omega\times\mathbb{R}^{p}. ∎

Third, it follows from the theory of analytic differential equations that for each N ∈ ℕ N\in\mathbb{N}, there are analytic functions h N −: ( − 1, 1) × ℝ p ⟶ ( − ϵ, ϵ) × ℝ p h_{N}^{-}:(-1,1)\times\mathbb{R}^{p}\longrightarrow(-\epsilon,\epsilon)\times\mathbb{R}^{p} and h N +: ( − ϵ, ϵ) × ℝ p ⟶ ( − 1, 1) × ℝ p h_{N}^{+}:(-\epsilon,\epsilon)\times\mathbb{R}^{p}\longrightarrow(-1,1)\times\mathbb{R}^{p} such that h N − ​ ( 0, μ) = h N + ​ ( 0, μ) = 0 h_{N}^{-}(0,\mu)=h_{N}^{+}(0,\mu)=0 for all μ \mu and g 1 ​ ( t, μ) = h N + ​ ( g N ​ ( h N − ​ ( t, μ), μ), μ) g_{1}(t,\mu)=h_{N}^{+}(g^{N}(h_{N}^{-}(t,\mu),\mu),\mu) for all ( t, μ) (t,\mu).

We write ⟨ 1, λ ⟩ \langle 1,\lambda\rangle for the additive submonoid of ℝ \mathbb{R} generated by 1 1 and λ \lambda. By the binomial theorem, there is for each α ∈ ⟨ 1, λ ⟩ \alpha\in\langle 1,\lambda\rangle and each N ∈ ℕ N\in\mathbb{N} an analytic function c α, N: ℝ p ⟶ ℝ c_{\alpha,N}:\mathbb{R}^{p}\longrightarrow\mathbb{R} such that for each μ ∈ ℝ p \mu\in\mathbb{R}^{p},

 | h N + ​ ( ( h N − ​ ( t, μ)) λ, μ) = ∑ α ∈ ⟨ 1, λ ⟩ c α, N ​ ( μ) ⋅ t α. h_{N}^{+}\left((h_{N}^{-}(t,\mu))^{\lambda},\mu\right)=\sum_{\alpha\in\langle 1,\lambda\rangle}c_{\alpha,N}(\mu)\cdot t^{\alpha}. |  |

On the other hand, given ν > 0 \nu>0, it follows from Lemma 8.3 for each μ ∈ ℝ p \mu\in\mathbb{R}^{p} and each N ≥ N ⁡ ( ν) N\geq N(\nu) that

 | g 1 ​ ( t, μ) − ∑ α ≤ ν c α, N ​ ( μ) ⋅ t α = o ⁡ ( ‖ t ‖ ν) as ​ ‖ t ‖ → 0; g_{1}(t,\mu)-\sum_{\alpha\leq\nu}c_{\alpha,N}(\mu)\cdot t^{\alpha}=o\left(\|t\|^{\nu}\right)\quad\text{as }\|t\|\to 0; |  |

in particular, c α, N = c α, N ′ c_{\alpha,N}=c_{\alpha,N^{\prime}} whenever | α | ≤ ν |\alpha|\leq\nu and N, N ′ ≥ N ⁡ ( ν) N,N^{\prime}\geq N(\nu). Thus, for each α ∈ ⟨ 1, λ ⟩ \alpha\in\langle 1,\lambda\rangle we put c α:= c α, N ⁡ ( | α |) c_{\alpha}:=c_{\alpha,N(|\alpha|)}; then by Lemma 8.3 again, we have for every ν > 0 \nu>0 and all ( t, μ) ∈ Ω ⁡ ( N ⁡ ( ν)) × ℝ p (t,\mu)\in\Omega(N(\nu))\times\mathbb{R}^{p} that

(8.2) |  | ‖ g 1 ​ ( t, μ) − ∑ α ≤ ν c α ​ ( μ) ⋅ t α ‖ ≤ K ⁡ ( ν) ⋅ ‖ t ‖ ν + ϵ ⁡ ( ν). \left\|g_{1}(t,\mu)-\sum_{\alpha\leq\nu}c_{\alpha}(\mu)\cdot t^{\alpha}\right\|\leq K(\nu)\cdot\|t\|^{\nu+\epsilon(\nu)}. |  |

It follows from Corollary 2.16 that g 1 ∈ 𝒜 1 ​ ( Ω ⁡ ( 0) × ℝ p) g_{1}\in\mathcal{A}_{1}(\Omega(0)\times\mathbb{R}^{p}). Finally, given any ν > γ ≥ 0 \nu>\gamma\geq 0, we define ( g 1) γ: Ω ⁡ ( N ⁡ ( γ)) × ℝ p ⟶ ℝ (g_{1})_{\gamma}:\Omega(N(\gamma))\times\mathbb{R}^{p}\longrightarrow\mathbb{R} by

 | ( g 1) γ ​ ( t, μ):= t − γ ​ ( g 1 ​ ( t, μ) − ∑ α < γ c α ​ ( μ) ​ t α). (g_{1})_{\gamma}(t,\mu):=t^{-\gamma}\left(g_{1}(t,\mu)-\sum_{\alpha<\gamma}c_{\alpha}(\mu)t^{\alpha}\right). |  |

Then by ( 8.2) again, we have for all ( t, μ) ∈ Ω ⁡ ( N ⁡ ( ν)) × ℝ p (t,\mu)\in\Omega(N(\nu))\times\mathbb{R}^{p} that

 | ‖ ( g 1) γ ​ ( t, μ) − ∑ γ ≤ α ≤ ν c α ​ ( μ) ⋅ t α − γ ‖ ≤ K ⁡ ( ν) ⋅ ‖ t ‖ ν + ϵ ⁡ ( ν) − γ. \left\|(g_{1})_{\gamma}(t,\mu)-\sum_{\gamma\leq\alpha\leq\nu}c_{\alpha}(\mu)\cdot t^{\alpha-\gamma}\right\|\leq K(\nu)\cdot\|t\|^{\nu+\epsilon(\nu)-\gamma}. |  |

Hence by Corollary 2.16, each ( g 1) γ (g_{1})_{\gamma} belongs to 𝒜 1 ​ ( Ω ⁡ ( N ⁡ ( γ)) × ℝ p) \mathcal{A}_{1}(\Omega(N(\gamma))\times\mathbb{R}^{p}), that is, g 1 g_{1} satisfies condition (TE). It follows that g 1 g_{1} belongs to 𝒬 1 ​ ( Ω ⁡ ( 0) × ℝ p) \mathcal{Q}_{1}(\Omega(0)\times\mathbb{R}^{p}), which proves Proposition 8.1.

## References

- [1] E. Brieskorn and H. Knörrer, Plane algebraic curves, Birkhäuser Verlag, 1986.
- [2] L. van den Dries, Tame Topology and O-minimal Structures, no. 248 in LMS Lecture Note Series, Cambridge University Press, 1998.
- [3] L. van den Dries and P. Speissegger, The real field with convergent generalized power series is model complete and o-minimal, Trans. Amer. Math. Soc., 350 (1998), 4377–4421.
- [4], The field of reals with multisummable series and the exponential function, Proc. London Math. Soc. (3), 81 (2000), 513–565.
- [5] H. Dulac, Sur les cycles limites, Bull. Soc. Math. France, 51 (1923), 45–188.
- [6] J. Ecalle, Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac, Hermann, Paris, 1992.
- [7] Yu. S. Ilyashenko, Finiteness theorems for limit cycles, vol. 94 of Translations of Mathematical Monographs, American Mathematical Society, 1991.
- [8], Centennial history of Hilbert’s sixteenth problem, Bull. Amer. Math. Soc., 39 (2002), 301–354.
- [9] R. Roussarie, Bifurcations of planar vector fields and Hilbert’s sixteenth problem, vol. 164 of Progress in Mathematics, Birkhäuser Verlag, Basel, 1998.
- [10] P. Speissegger, The Pfaffian closure of an o-minimal structure, J. Reine Angew. Math., 508 (1999), 189–211.
- [11] B.L. van der Waerden, Algebra, Springer Verlag, 1967.
- [12] E. Whittaker and G. Watson, A Course of Modern Analysis, Cambridge, 1927.

[◄][4][image: ar5iv homepage] [5]
[Feeling lucky?][6] [7]
[Conversion report][8]
[Report an issue][9]
[View original on arXiv][10] [►][11]


## Links

[1]: mailto:tobias.kaiser@mathematik.uni-regensburg.de
[2]: mailto:Jean-Philippe.Rolin@u-bourgogne.fr
[3]: mailto:speisseg@math.mcmaster.ca
[4]: /html/math/0612743
[5]: /
[6]: /feeling_lucky
[7]: /land_of_honey_and_milk
[8]: /log/math/0612745
[9]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+math/0612745
[10]: https://arxiv.org/pdf/math/0612745
[11]: /html/math/0612746
