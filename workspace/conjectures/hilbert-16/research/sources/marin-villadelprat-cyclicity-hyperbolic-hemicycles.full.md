<!-- source: https://arxiv.org/html/2501.16924 | converted from HTML -->

The cyclicity of hyperbolic hemicycles 2010 AMS Subject Classification: 34C07; 34C20; 34C23. Key words and phrases: limit cycle, hemicycle, cyclicity, asymptotic expansion, Dulac map. This work has been partially funded by the Ministry of Science, Innovation and Universities of Spain through the grants PID2020-118281GB-C33, PID2021-125625NB-I00 and PID2022-136613NB-I00, and by the Agency for Management of University and Research Grants of Catalonia through the grants 2021SGR00113 and 2021SGR01015.

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2501.16924v1 [math.DS] 28 Jan 2025

# The cyclicity of hyperbolic hemicycles 0 0 footnotetext: 2010 AMS Subject Classification: 34C07; 34C20; 34C23. 0 0 footnotetext: Key words and phrases: limit cycle, hemicycle, cyclicity, asymptotic expansion, Dulac map. 0 0 footnotetext: This work has been partially funded by the Ministry of Science, Innovation and Universities of Spain through the grants PID2020-118281GB-C33, PID2021-125625NB-I00 and PID2022-136613NB-I00, and by the Agency for Management of University and Research Grants of Catalonia through the grants 2021SGR00113 and 2021SGR01015.

D. Marín J. Villadelprat Affiliation: *[.1truecm] Departament de Matemàtiques, Edifici Cc, Universitat Autònoma de Barcelona, Affiliation: *[-.05truecm] 08193 Cerdanyola del Vallès (Barcelona), Spain

August 11, 2026

###### Abstract

We consider families of planar polynomial vector fields of degree n n and study the cyclicity of a type of unbounded polycycle Γ \Gamma called hemicycle. Compactified to the Poincaré disc, Γ \Gamma consists of an affine straight line together with half of the line at infinity and has two singular points, which are hyperbolic saddles located at infinity. We prove four main results. Theorem A deals with the cyclicity of Γ \Gamma when perturbed without breaking the saddle connections. For the other results we consider the case n = 2 n=2. More concretely they are addressed to the quadratic integrable systems belonging to the class Q 3 R Q_{3}^{R} and having two hemicycles, Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell}, surrounding each one a center. Theorem B gives the cyclicity of Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} when perturbed inside the whole family of quadratic systems. In Theorem C we study the number of limit cycles bifurcating simultaneously from Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} when perturbed as well inside the whole family of quadratic systems. Finally, in Theorem D we show that for three specific cases there exists a simultaneous alien limit cycle bifurcation from Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell}.

## 1 Introduction and main results

In this paper we consider families of planar polynomial vector fields X μ X_{\mu} depending on a parameter μ ∈ ℝ N \mu\in\mathbb{R}^{N} and we are interested in the number of limit cycles (i.e., isolated periodic orbits). More concretely, we study their bifurcations, which occur at the limit periodic sets of the family (where limit cycles accumulate as μ \mu varies). In this setting the first step is to obtain the sharp bound for the number of limit cycles that bifurcate from each limit periodic set Γ. \Gamma. This bound is called the cyclicity of Γ. \Gamma. The computation of the cyclicity is a crucial step to determine the bifurcation diagram for the number of limit cycles within the family. Before stating our main results we will give a precise definition of all these notions. The problems that we discuss in the present paper are related to questions surrounding Hilbert’s 16th problem and its various weakened forms. We refer the interested reader to the monographs of Il’yashenko [13], Jibin Li [15], or Roussarie [25] for more information on these issues.

We begin by recalling the notion of limit periodic set as introduced in [25, Definition 10]. This is the fundamental object that we aim to study and its definition is given in terms of the Hausdorff topology, which for reader’s convenience we briefly explain next.

Let S S be a metrizable space and denote by 𝒞 ⁡ ( S) \mathcal{C}(S) the set of all compact non-empty subsets of S. S. Given any K 1, K 2 ∈ 𝒞 ⁡ ( S) K_{1},K_{2}\in\mathcal{C}(S) we define

 | d H ​ ( K 1, K 2) = sup x 1 ∈ K 1, x 2 ∈ K 2 { inf x 2 ′ ∈ K 2 d ⁡ ( x 1, x 2 ′), inf x 1 ′ ∈ K 1 d ⁡ ( x 1 ′, x 2) }. d_{H}(K_{1},K_{2})=\sup_{x_{1}\in K_{1},x_{2}\in K_{2}}\left\{\inf_{x_{2}^{\prime}\in K_{2}}d(x_{1},x_{2}^{\prime})\,,\inf_{x_{1}^{\prime}\in K_{1}}d(x_{1}^{\prime},x_{2})\right\}. |  |

One can readily show that d H d_{H} is a distance. It defines a topology on 𝒞 ⁡ ( S) \mathcal{C}(S), which is independent of the distance d d chosen, that is called the *Hausdorff topology*. Moreover it turns out that

 | d H ​ ( K 1, K 2) = inf { ε > 0: K 1 ⊂ N ε ​ ( K 2) ​ and ​ K 2 ⊂ N ε ​ ( K 1) }, d_{H}(K_{1},K_{2})=\inf\big\{\varepsilon>0:K_{1}\subset N_{\varepsilon}(K_{2})\text{ and }K_{2}\subset N_{\varepsilon}(K_{1})\big\}, |  |

where N ε ​ ( K) N_{\varepsilon}(K) is the ε \varepsilon -neighbourhood of K K. Finally, if ( S, d) (S,d) is a compact metric space then so is ( 𝒞 ⁡ ( S), d H) (\mathcal{C}(S),d_{H}). The interested reader is referred to [23, p. 279] for both assertions. □ \square

A non-empty compact subset Γ \Gamma of a surface S S is a *limit periodic set*for a germ of a family { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} of vector fields on S S if there exists a sequence of parameters { μ n } n ∈ ℕ \{\mu_{n}\}_{n\in\mathbb{N}} converging to μ 0 \mu_{0} such that each X μ n X_{\mu_{n}} has a limit cycle γ n \gamma_{n} and the sequence { γ n } n ∈ ℕ \{\gamma_{n}\}_{n\in\mathbb{N}} converges to Γ \Gamma as n → ∞ n\to\infty in the Hausdorff topology of the space 𝒞 ⁡ ( S) \mathcal{C}(S) of compact non-empty subsets of S S. □ \square

It is well known, see [25, Theorem 5], that any limit periodic set of a germ of an analytic family { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} such that X μ 0 X_{\mu_{0}} has only isolated singular points is either a singular point, a period orbit or a graphic of X μ 0 X_{\mu_{0}}. We recall the notion of graphic and polycycle below:

Let X X be a vector field on ℝ 2 \mathbb{R}^{2} (or 𝕊 2 \mathbb{S}^{2}). A *graphic*Γ \Gamma for X X is a compact, non-empty invariant subset which is a continuous image of 𝕊 1 \mathbb{S}^{1} and consists of a finite number of isolated singularities { p 1, …, p m, p m + 1 = p 1 } \{p_{1},\ldots,p_{m},p_{m+1}=p_{1}\} (not necessarily distinct) and compatibly oriented separatrices { s 1, …, s m } \{s_{1},\ldots,s_{m}\} connecting them (i.e., such that the α \alpha -limit set of s j s_{j} is p j p_{j} and the ω \omega -limit set of s j s_{j} is p j + 1 p_{j+1}). A graphic is said to be *hyperbolic*if all its singular points are hyperbolic saddles. A *polycycle*is a graphic with a return map defined on one of its sides. □ \square

The polycycles that we aim to study are unbounded and for this reason we need to compactify the vector field. Recall that to investigate the phase portrait of a polynomial vector field Y Y near infinity we can consider its Poincaré compactification p ⁡ ( Y) p(Y), see [1, §5] for details, which is an analytically equivalent vector field defined on the sphere 𝕊 2 \mathbb{S}^{2}. The points at infinity of ℝ 2 \mathbb{R}^{2} are in bijective correspondence with the points of the equator of 𝕊 2 \mathbb{S}^{2}, that we denote by ℓ ∞ \ell_{\infty}. Moreover the trajectories of p ⁡ ( Y) p(Y) in 𝕊 2 \mathbb{S}^{2} are symmetric with respect to the origin and so it suffices to draw its flow in the closed northern hemisphere only, the so called Poincaré disc.

Let Π \Pi be an arbitrary collection of limit periodic sets for the germ of an analytic family { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} of vector fields on 𝕊 2 \mathbb{S}^{2}. We define the *cyclicity*of Π \Pi with respect to { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} as

 | Cycl ( ( Π, X μ 0), X μ):= inf ε, δ > 0 sup μ ∈ B δ ​ ( μ 0) #{ γ limit cycle of X μ such that d H ( γ, Γ) < ε for some Γ ∈ Π }, \mathrm{Cycl}\big((\Pi,X_{\mu_{0}}),X_{\mu}\big)\!:=\inf\limits_{\varepsilon,\delta>0}\sup\limits_{\mu\in B_{\delta}(\mu_{0})}\#\big\{\gamma\text{ limit cycle of $X_{\mu}$ such that }d_{H}(\gamma,\Gamma)<\varepsilon\text{ for some $\Gamma\in\Pi$}\big\}, |  |

which may be infinite. □ \square

Let us point out that if Π = { Γ } \Pi=\{\Gamma\} then the cyclicity of Π \Pi coincides with the usual cyclicity Cycl ⁡ ( ( Γ, X μ 0), X μ) \mathrm{Cycl}\big((\Gamma,X_{\mu_{0}}),X_{\mu}\big) of the limit periodic set Γ \Gamma, cf. [25, Definition 12]. In contrast, if Π \Pi consists of more than one limit periodic set then the cyclicity of Π \Pi accounts for the limit cycles bifurcating *simultaneously*from any of them. Finally, observe that if Π ⊂ Π ′ \Pi\subset\Pi^{\prime} then Cycl ⁡ ( ( Π, X μ 0), X μ) ⩽ Cycl ⁡ ( ( Π ′, X μ 0), X μ) \mathrm{Cycl}\big((\Pi,X_{\mu_{0}}),X_{\mu}\big)\leqslant\mathrm{Cycl}\big((\Pi^{\prime},X_{\mu_{0}}),X_{\mu}\big). □ \square

Γ − \Gamma_{-} Γ + \Gamma_{+} γ − \gamma_{-} γ + \gamma_{+} γ \gamma Figure 1: “Figure eight-loop” Γ = Γ − ∪ Γ + \Gamma=\Gamma_{-}\cup\Gamma_{+} formed by two homoclinic connections Γ − \Gamma_{-} and Γ + \Gamma_{+}. The limit cycles γ − \gamma_{-}, γ + \gamma_{+} and γ \gamma are close (with respect to the Hausdorff distance) to Γ − \Gamma_{-}, Γ + \Gamma_{+} and Γ \Gamma, respectively.

Note that the simultaneous cyclicity of { Γ 1, …, Γ r } \{\Gamma_{1},\ldots,\Gamma_{r}\} may not coincide with the cyclicity of Γ 1 ∪ ⋯ ∪ Γ r \Gamma_{1}\cup\cdots\cup\Gamma_{r}, even in case that the latter is a limit periodic set. For instance, consider a germ { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} such that X μ 0 X_{\mu_{0}} has a saddle point with two homoclinic loops Γ − \Gamma_{-} and Γ + \Gamma_{+} making up a “figure eight-loop” Γ = Γ − ∪ Γ + \Gamma=\Gamma_{-}\cup\Gamma_{+}, see Figure 1. Then the values of Cycl ⁡ ( ( Π, X μ 0), X μ) \mathrm{Cycl}\big((\Pi,X_{\mu_{0}}),X_{\mu}\big) for

 | Π = { Γ + }, Π = { Γ − }, Π = { Γ }, Π = { Γ +, Γ − }, Π = { Γ +, Γ }, Π = { Γ −, Γ } ​ and ​ Π = { Γ +, Γ −, Γ } \Pi=\{\Gamma_{+}\},\;\Pi=\{\Gamma_{-}\},\;\Pi=\{\Gamma\},\;\Pi=\{\Gamma_{+},\Gamma_{-}\},\;\Pi=\{\Gamma_{+},\Gamma\},\;\Pi=\{\Gamma_{-},\Gamma\}\text{ and }\Pi=\{\Gamma_{+},\Gamma_{-},\Gamma\} |  |

may be all different. On the other hand, it is clear that

 | max j ∈ { 1, 2, …, r } ⁡ { Cycl ⁡ ( ( Γ j, X μ 0), X μ) } ⩽ Cycl ⁡ ( ( { Γ 1, …, Γ r }, X μ 0), X μ) ⩽ ∑ j = 1 r Cycl ⁡ ( ( Γ j, X μ 0), X μ). \max_{j\in\{1,2,\ldots,r\}}\left\{\mathrm{Cycl}\big((\Gamma_{j},X_{\mu_{0}}),X_{\mu}\big)\right\}\leqslant\mathrm{Cycl}\big((\{\Gamma_{1},\ldots,\Gamma_{r}\},X_{\mu_{0}}),X_{\mu}\big)\leqslant\sum_{j=1}^{r}\mathrm{Cycl}\big((\Gamma_{j},X_{\mu_{0}}),X_{\mu}\big). |  |

In this paper we study the cyclicity problem for perturbations of planar polynomial vector fields with an invariant straight line (see [7, 9] and references therein for previous results on the issue). After a suitable rotation we can assume that this invariant straight line is { y = 0 }. \{y=0\}. In the first part of the paper this line is assumed to be invariant throughout all the perturbation. Any such family { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} can be written as

 | X μ { x ˙ = y ​ f ​ ( x, y, μ) + g ⁡ ( x, μ), y ˙ = y ​ q ​ ( x, y, μ), X_{\mu}\quad\left\{\!\begin{array}[]{l}\dot{x}=yf(x,y;\mu)+g(x;\mu),\\[2.0pt] \dot{y}=yq(x,y;\mu),\end{array}\right. |  | (1) |

where Λ \Lambda is an open subset of ℝ N \mathbb{R}^{N} and f f, g g and q q are polynomials with the coefficients depending analytically on μ. \mu. We assume that deg ⁡ ( f) = deg ⁡ ( q) = n \deg(f)=\deg(q)=n and deg ⁡ ( g) = n + 1 \deg(g)=n+1 and that the following hypothesis hold:

1. H1

g ⁡ ( x, μ) < 0 g(x;\mu)<0 for all x ∈ ℝ x\in\mathbb{R} and μ ∈ Λ \mu\in\Lambda, which implies that n n is odd, and

2. H2

ℓ n + 1 ​ ( x, y, μ):= y ​ f n ​ ( x, y, μ) − x ​ q n ​ ( x, y, μ) + g n + 1 ​ ( μ) ​ x n + 1 > 0 {\ell_{n+1}}(x,y;\mu)\!:=yf_{n}(x,y;\mu)-xq_{n}(x,y;\mu)+g_{n+1}(\mu)x^{n+1}>0 for all ( x, y) ≠ ( 0, 0) (x,y)\neq(0,0) and μ ∈ Λ \mu\in\Lambda.

Here, and in what follows, f n ​ ( x, y, μ) f_{n}(x,y;\mu) and q n ​ ( x, y, μ) q_{n}(x,y;\mu) denote, respectively, the homogeneous part of degree n n of f ⁡ ( x, y, μ) f(x,y;\mu) and q ⁡ ( x, y, μ) q(x,y;\mu), whereas g n + 1 ​ ( μ) g_{n+1}(\mu) is the leading coefficient of g ⁡ ( x, μ). g(x;\mu). The second hypothesis is related with the angle variation θ \theta of the solutions of ( 1) (\ref{DS}) near the infinity because one can verify that

 | r 2 ​ θ ˙ = y ⁡ ( x ​ q ​ ( x, y) − y ​ f ​ ( x, y) − g ⁡ ( x)). r^{2}\dot{\theta}=y\big(xq(x,y)-yf(x,y)-g(x)\big). |  |

Since ℓ n + 1 {\ell_{n+1}} is a homogeneous polynomial of even degree, H2 is equivalent to z ​ f n ​ ( 1, z) − q n ​ ( 1, z) + g n + 1 > 0 zf_{n}(1,z)-q_{n}(1,z)+g_{n+1}>0 and f n ​ ( z, 1) − z ​ q n ​ ( z, 1) + g n + 1 ​ z n + 1 > 0 f_{n}(z,1)-zq_{n}(z,1)+g_{n+1}z^{n+1}>0 for all z ∈ ℝ z\in\mathbb{R} and μ ∈ Λ. \mu\in\Lambda.

Conditions H1 and H2 guarantee that, after compactifying the polynomial vector field X μ X_{\mu} to the Poincaré disc, the boundary of the upper (respectively, lower) half-plane is a polycycle Γ u \Gamma_{u} (respectively, Γ ℓ \Gamma_{\ell}) with two hyperbolic saddles, see Figure 2,

Figure 2: Placement of the hyperbolic saddles and the polycycles Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} in the Poincaré disc for the polynomial vector field ( 1) (\ref{DS}).

 | s 1:= { y = 0, x > 0 } ∩ ℓ ∞ s_{1}\!:=\{y=0,x>0\}\cap\ell_{\infty} and s 2:= { y = 0, x < 0 } ∩ ℓ ∞. s_{2}\!:=\{y=0,x<0\}\cap\ell_{\infty}. |  |

This type of polycycle, formed by an invariant line and half of the equator of 𝕊 2 \mathbb{S}^{2}, is called *hemicycle*in [7]. Moreover the vector fields of the form ( 1) (\ref{DS}) verifying H1 and H2 are called *D-systems*by the authors in [9].

Our first main result is addressed to the cyclicity of Γ u \Gamma_{u} when perturbed *inside*the family of D D -systems. This result will be given in terms of two functions d 0 ​ ( μ) d_{0}(\mu) and d 1 ​ ( μ) d_{1}(\mu). In order to define them we first need to introduce several other functions. For the sake of shortness we shall omit the dependence of μ \mu in these functions when there is no risk of confusion. We define

 | K ⁡ ( x 1, x 2, μ):= 1 − x ​ q ​ ( x, y) y ​ f ​ ( x, y) + g ⁡ ( x) | ( x, y) = ( 1 x 1, x 2 x 1) ​ and ​ λ ​ ( μ):= − K ⁡ ( 0, 0, μ) = − 1 + q n ​ ( 1, 0) g n + 1 > 0. K(x_{1},x_{2};\mu)\!:=\left.1-\frac{xq(x,y)}{yf(x,y)+g(x)}\right|_{(x,y)=\left(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\right)}\text{ and }\lambda(\mu)\!:=-K(0,0;\mu)=-1+\frac{q_{n}(1,0)}{g_{n+1}}>0. |  | (2) |

The function K K is related to the projective compactification of X μ X_{\mu}, whereas λ ⁡ ( μ) \lambda(\mu) is the hyperbolicity ratio of its saddle at infinity. Let us remark that, on account of H1 and H2, the functions K K and 1 / K 1/K are well defined in a neighbourhood of { x 1 = 0 } \{x_{1}=0\} and { x 2 = 0 }. \{x_{2}=0\}. Then, setting

 |  | M 1 ​ ( u) = exp ⁡ ( ∫ 0 u ( 1 K ⁡ ( 0, z) + 1 λ) ​ d ​ z z) ​ ∂ 1 ( 1 K) ​ ( 0, u) \displaystyle M_{1}(u)=\exp\left(\int_{0}^{u}\left(\frac{1}{K(0,z)}+\frac{1}{\lambda}\right)\frac{dz}{z}\right)\partial_{1}\Big(\frac{1}{K}\Big)(0,u) |  |

and |

 |  | M 2 ​ ( u) = exp ⁡ ( ∫ 0 u ( K ⁡ ( z, 0) + λ) ​ d ​ z z) ​ ∂ 2 K ⁡ ( u, 0), \displaystyle M_{2}(u)=\exp\left(\int_{0}^{u}\big(K(z,0)+\lambda\big)\frac{dz}{z}\right)\partial_{2}K(u,0), |  |

we define

 | F 1 ​ ( μ) \displaystyle F_{1}(\mu) | = − ∫ 0 + ∞ ( M 1 ( z) − M 1 ( 0) + exp ( G 1) ( M 1 ( − z) − M 1 ( 0))) d ​ z z 1 + 1 / λ, \displaystyle=-\int_{0}^{+\infty}\Big(M_{1}(z)-M_{1}(0)+\exp(G_{1})\big(M_{1}(-z)-M_{1}(0)\big)\Big)\frac{dz}{z^{1+1/\lambda}}, |  | (3) |

 | F 2 ​ ( μ) \displaystyle F_{2}(\mu) | = ∫ 0 + ∞ ( M 2 ​ ( − z) − M 2 ​ ( 0) + exp ⁡ ( G 2) ​ ( M 2 ​ ( z) − M 2 ​ ( 0))) ​ d ​ z z 1 + λ \displaystyle=\int_{0}^{+\infty}\Big(M_{2}(-z)-M_{2}(0)+\exp(G_{2})\big(M_{2}(z)-M_{2}(0)\big)\Big)\frac{dz}{z^{1+\lambda}} |  | (4) |

and |

 | F 3 ​ ( μ) \displaystyle F_{3}(\mu) | = − G 2 ​ ( ∂ 1 K ​ ∂ 2 K + ∂ 12 K) ​ ( 0, 0), \displaystyle=-G_{2}\big(\partial_{1}K\partial_{2}K+\partial_{12}K\big)(0,0), |  | (5) |

where

 | G 1 = ∫ − 1 1 ( q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z) + 1 + 1 λ + z ​ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) ​ d ​ z z ​ and ​ G 2 = ∫ 0 + ∞ ( q ⁡ ( z, 0) g ⁡ ( z) + q ⁡ ( − z, 0) g ⁡ ( − z)) ​ 𝑑 z. G_{1}=\int_{-1}^{1}\left(\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}+1+\frac{1}{\lambda}+\frac{zq_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)\frac{dz}{z}\\ \text{ and }G_{2}=\int_{0}^{{+\infty}}\left(\frac{q(z,0)}{g(z)}+\frac{q(-z,0)}{g(-z)}\right)dz. |  |

Taking this notation into account, the functions that determine the cyclicity (and stability) of the polycyle Γ u \Gamma_{u} at first and second order are the following:

 | d 0 ( μ):= − ∫ − ∞ + ∞ ( q ⁡ ( z, 0) g ⁡ ( z) + λ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) d z and d 1 ( μ):= { F 1 ​ ( μ) if λ ⁡ ( μ) > 1, F 2 ​ ( μ) if λ ⁡ ( μ) < 1, F 3 ​ ( μ) if λ ⁡ ( μ) = 1. d_{0}(\mu)\!:=-\int_{-{\infty}}^{+\infty}\left(\frac{q(z,0)}{g(z)}+\lambda\frac{q_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)dz\;\text{ and }\;d_{1}(\mu)\!:=\left\{\begin{array}[]{ll}F_{1}(\mu)&\text{ if $\lambda(\mu)>1,$}\\[5.0pt] F_{2}(\mu)&\text{ if $\lambda(\mu)<1,$}\\[5.0pt] F_{3}(\mu)&\text{ if $\lambda(\mu)=1.$}\end{array}\right. |  | (6) |

Let us advance that the function d 0 d_{0}, together with the functions F 1, F_{1}, F 2 F_{2} and F 3 F_{3} defining d 1, d_{1}, generate the ideal of coefficients at order one and two of the asymptotic expansions of the displacement function studied in Theorem 2.1. This result also shows that d 0 d_{0} is analytic on Λ \Lambda and d 1 d_{1} is analytic on Λ ∖ Λ 1 \Lambda\setminus\Lambda_{1}, where Λ 1:= { μ ∈ Λ: λ ⁡ ( μ) = 1 }. \Lambda_{1}\!:=\{\mu\in\Lambda:\lambda(\mu)=1\}. In the next statement ℛ u ​ ( ⋅, μ) \mathscr{R}_{u}(\,\cdot\,;\mu) stands for the return map of the vector field X μ X_{\mu} around the polycycle Γ u \Gamma_{u}, see Figure 2, and we use the notion of functional independence given in Definition A.

###### Theorem A.

Let us consider the family of polynomial vector fields { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} given in ( 1) (\ref{DS}) and verifying the assumptions H1 and H2. Then the following assertions hold for any μ 0 ∈ Λ \mu_{0}\in\Lambda such that ℛ u ​ ( ⋅, μ 0) ≢ Id: \mathscr{R}_{u}(\,\cdot\,;\mu_{0})\not\equiv\text{Id}:

1. ( a) (a)

If d 0 ​ ( μ 0) ≠ 0 d_{0}(\mu_{0})\neq 0 then Cycl ⁡ ( ( Γ u, X μ 0), X μ) = 0. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)=0.

2. ( b) (b)

If d 0 d_{0} vanishes and is independent at μ 0 \mu_{0} then Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 1. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 1.

3. ( c) (c)

If d 1 ​ ( μ 0) ≠ 0 d_{1}(\mu_{0})\neq 0 then Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩽ 1. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\leqslant 1.

4. ( d) (d)

If d 0 d_{0} and d 1 d_{1} vanish and are independent at μ 0 \mu_{0} and λ ⁡ ( μ 0) ≠ 1 \lambda(\mu_{0})\neq 1 then Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 2. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 2. Moreover the same lower bound holds in case that λ ⁡ ( μ 0) = 1 \lambda(\mu_{0})=1 and the restrictions d 0 | Λ 1 \left.d_{0}\right|_{\Lambda_{1}} and d 1 | Λ 1 \left.d_{1}\right|_{\Lambda_{1}} vanish and are independent at μ 0 \mu_{0}.

With regard to the application of Theorem A it is worth noting that if d 0 ​ ( μ 0) ≠ 0 d_{0}(\mu_{0})\neq 0, or d 1 ​ ( μ 0) ≠ 0 d_{1}(\mu_{0})\neq 0, then ℛ u ​ ( ⋅, μ 0) ≢ Id. \mathscr{R}_{u}(\,\cdot\,;\mu_{0})\not\equiv\text{Id}. This is a consequence of Theorem 2.1, which is a fundamental result to prove Theorem A.

The stability of this kind of hemicycle was previously studied in [9, Theorem 7]. Indeed, using our notation, the authors prove that ℛ u ​ ( s, μ) = e d 0 ​ ( μ) ​ s + o ​ ( s) \mathscr{R}_{u}(s;\mu)=e^{d_{0}(\mu)}s+\mbox{\rm o}(s), so that if d 0 ​ ( μ 0) < 0 d_{0}(\mu_{0})<0 (respectively, d 0 ​ ( μ 0) > 0 d_{0}(\mu_{0})>0) then the polycycle Γ u \Gamma_{u} of the vector field X μ 0 X_{\mu_{0}} is asymptotically stable (respectively, unstable). In this paper, by performing a second order analysis we also obtain the stability in case that d 0 ​ ( μ 0) = 0 d_{0}(\mu_{0})=0 and d 1 ​ ( μ 0) ≠ 0 d_{1}(\mu_{0})\neq 0 (see Remark 2). That being said, the goal of the present paper is not to study the stability of the hemicycle but its cyclicity. The first notion concerns single vector fields, whereas the second one is addressed to families of vector fields (i.e., depending on parameters). This is the reason why we need the remainder in the asymptotic expansion of ℛ u ​ ( s, μ) \mathscr{R}_{u}(s;\mu) at s = 0 s=0 to be uniform with respect to the parameters. Let us also note that similar results (for both, stability and cyclicity) can be obtained for the hemicycle Γ ℓ \Gamma_{\ell} by performing the change of variables ( x, y) ↦ ( x, − y). (x,y)\mapsto(x,-y).

Theorem A is a general result for the cyclicity of the polycycle Γ u \Gamma_{u} of a D-system X μ 0 X_{\mu_{0}} with ℛ u ​ ( ⋅, μ 0) ≢ Id \mathscr{R}_{u}(\,\cdot\,;\mu_{0})\not\equiv\text{Id} when perturbed inside the family of D-systems ( 1) (\ref{DS}). Note that in doing so the polycycle Γ u \Gamma_{u} is persistent (i.e., the connections between the two vertices remain unbroken through the perturbation). In contrast, the rest of our main results concern the cyclicity of quadratic D-systems X μ 0 X_{\mu_{0}} with ℛ u ​ ( ⋅, μ 0) ≡ Id \mathscr{R}_{u}(\,\cdot\,;\mu_{0})\equiv\text{Id} when perturbed inside the whole family of quadratic systems. This means in particular that the connection breaks, see Figure 7. More concretely, in Theorems B, C and D, for each ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2), we perturb the quadratic D-system

Figure 3: Phase portrait in the Poincaré disc of the quadratic differential system ( 7) (\ref{DSq}) for each ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2).

 | { x ˙ = b 0 − 2 4 + ( 1 − b 0) ​ y + a 0 ​ x 2 + b 0 ​ y 2, y ˙ = − 2 ​ x ​ y, \left\{\!\begin{array}[]{l}\dot{x}=\frac{b_{0}-2}{4}+(1-b_{0})y+a_{0}x^{2}+b_{0}y^{2},\\[2.0pt] \dot{y}=-2xy,\end{array}\right. |  | (7) |

that one can show it verifies assumptions H1 and H2. Moreover it has two centers, located at the points ( 0, 1 2) (0,\frac{1}{2}) and ( 0, b 0 − 2 2 ​ b 0) (0,\frac{b_{0}-2}{2b_{0}}) whose period annulus foliate, respectively, the upper and lower half-planes, see Figure 3.

###### Theorem B.

Let us take any ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2). Then the cyclicity of Γ u \Gamma_{u} when we perturb ( 7) (\ref{DSq}) inside the whole family of quadratic differential systems is exactly 2 if a 0 ≠ − 1 a_{0}\neq-1 and at least 2 if a 0 = − 1. a_{0}=-1. Moreover the same statement is true for Γ ℓ. \Gamma_{\ell}.

We point out that this result does not imply that the number of limit cycles bifurcating simultaneously from Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} is four. As a matter of fact this number is at most three by the forthcoming Theorem C. Using the terminology from [12], both centers of the unperturbed system ( 7) (\ref{DSq}) are inside the reversible component Q 3 R Q_{3}^{R} of the *center manifold*of the quadratic systems. There are three other components: Hamiltonian Q 3 H Q_{3}^{H}, codimension four Q 4 Q_{4} and generalized Lotka-Volterra Q 3 L ​ V Q_{3}^{LV}. It turns out (cf. Lemma 3.3) that the centers of the unperturbed system belong also to the Q 3 L ​ V Q_{3}^{LV} component in case that ( a 0 + b 0) ​ ( a 0 − b 0 + 2) = 0 (a_{0}+b_{0})(a_{0}-b_{0}+2)=0, and when this occurs the proof of Theorem B is a little more difficult.

Closely related to Theorem B, a result due to Swirszcz (see [32, Theorem 1]) is worth to be quoted. Indeed, in that paper the author also studies the cyclicity of a polycycle of a quadratic reversible system when perturbed inside the whole quadratic family. More concretely, he perturbs the differential system ( 7) (\ref{DSq}) but taking ( a 0, b 0) ∈ 𝒮:= { 0 < b 0 < − a 0 } ∩ { a 0 < − 2 } (a_{0},b_{0})\in\mathcal{S}\!:=\{0<b_{0}<-a_{0}\}\cap\{a_{0}<-2\}. For these parameters the singular point ( 0, 1 2) (0,\frac{1}{2}) is also a center but the polycycle at the boundary of its period annulus is not an hemicycle. It is a bicycle Γ b \Gamma_{b} with the two vertices at infinity, and consisting of a branch of a hyperbola together with a segment of ℓ ∞ \ell_{\infty}. Recall that the *period annulus*of a center p p is its largest punctured neighbourhood 𝒫 \mathscr{P} which is entirely covered by periodic orbits, and that its boundary ∂ 𝒫 \partial\mathscr{P} has two connected components: the center itself and a polycycle. By using a completely different approach than ours, and with a lower level of detail in the proofs, Swirszcz identifies a curve 𝒞 \mathcal{C} (see Figure 4) such that the cyclicity of Γ b \Gamma_{b} is 3 if ( a 0, b 0) ∈ 𝒮 ∩ 𝒞 (a_{0},b_{0})\in\mathcal{S}\cap\mathcal{C} and 2 if ( a 0, b 0) ∈ 𝒮 ∖ 𝒞 (a_{0},b_{0})\in\mathcal{S}\setminus\mathcal{C}. It is to be noted that the only parameter value in 𝒮 \mathcal{S} which intersects another center component is ( a 0, b 0) = ( − 4, 2), (a_{0},b_{0})=(-4,2), that belongs also to the Q 4 Q_{4} component.

Q 4 + Q_{4}^{+} S 2 S_{2} − 2 -2 2 2 0 0 S 4 S_{4} S 3 S_{3} S 1 S_{1} Q 4 − Q_{4}^{-} 3 ​ a 0 + 5 ​ b 0 + 2 = 0 3a_{0}+5b_{0}+2=0 𝒞 \mathcal{C} a 0 a_{0} b 0 b_{0} 1 1 − 1 -1 − 4 -4 1 1 − 1 -1 Figure 4: According to Illiev’s conjecture, the shaded area corresponds to those parameters ( a 0, b 0) (a_{0},b_{0}) for which the period annulus 𝒫 \mathscr{P} of the center at ( 0, 1 2) (0,\frac{1}{2}) of system ( 7) (\ref{DSq}) has cyclicity 3. Its boundary has two components: the straight line 3 ​ a 0 + 5 ​ b 0 + 2 = 0 3a_{0}+5b_{0}+2=0 and a piecewise curve 𝒞. \mathcal{C}. The straight line corresponds to parameters for which the center itself has cyclicity 3. The curve 𝒞 \mathcal{C} corresponds to parameters for which the polycycle at ∂ 𝒫 \partial\mathscr{P} has cyclicity 3. The parameters S 1 = ( − 1, 1) S_{1}=(-1,1), S 2 = ( − 2, 0) S_{2}=(-2,0), S 3 = ( − 1 2, 0) S_{3}=(-\frac{1}{2},0) and S 4 = ( − 4, 1) S_{4}=(-4,1) are the four isochronous quadratic centers. The blue straight lines are the intersection points with the component Q 3 L ​ V Q_{3}^{LV} of the center manifold. The parameters Q 4 + = ( − 4, 2) Q_{4}^{+}=(-4,2) and Q 4 − = ( − 2 3, 0) Q_{4}^{-}=(-\frac{2}{3},0) are the intersection points with the component Q 4 Q_{4}.

In another vein, Iliev studies in his seminal paper [12] the cyclicity of the period annulus 𝒫 \mathscr{P} of the quadratic centers. We stress that the definition of cyclicity for 𝒫 \mathscr{P} is different than the one for a polycycle because the former is open (see Definition 1). Among other results Iliev proves that the cyclicity of the period annulus 𝒫 \mathscr{P} of the center at ( 0, 1 2) (0,\frac{1}{2}) of the differential system ( 7) (\ref{DSq}) is 3 3 for ( a 0, b 0) = ( − 4, 2) (a_{0},b_{0})=(-4,2) and 2 2 for ( a 0, b 0) = ( − 1, 1) (a_{0},b_{0})=(-1,1). These two parameters are denoted, respectively, by Q 4 + Q_{4}^{+} and S 1 S_{1} in Figure 4. Moreover he conjectures that the cyclicity of 𝒫 \mathscr{P} is equal to 3 if ( a 0, b 0) (a_{0},b_{0}) is inside the shaded area in Figure 4 and equal to 2 if ( a 0, b 0) (a_{0},b_{0}) is outside. Previous to Iliev’s conjecture, there is a result by Shafer and Zegeling (see [29, Theorem 3.2]) that determines some regions where the cyclicity of 𝒫 \mathscr{P} is equal to 3. They also give a numerical approximation to the curve 𝒞. \mathcal{C}. In this setting Theorem B reinforces Iliev’s conjecture because it shows that the curve 𝒞 \mathcal{C} does not enter the square ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2).

Let us recall at this point that *Hilbert’s 16th problem*asks for the maximum number H ⁡ ( n) H(n) of limit cycles of a planar polynomial differential system of degree ⩽ n. \leqslant n. It is still open for any n ⩾ 2. n\geqslant 2. In 1994 Dumortier, Roussarie and Rousseau conceived a program (see [7]) to prove that H ⁡ ( 2) H(2) is finite. In short, they reduced this problem to prove the finite cyclicity for only 121 (different classes of) graphics occurring in quadratic systems. According to the notation in that paper, the quadratic system ( 7) (\ref{DSq}) with ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2) is inside the class H 2 1 H_{2}^{1} of hyperbolic hemicycles surrounding a center (see [7, Figure 7]). Thus, Theorem B can be viewed as a small contribution to the completion of the program to prove that H ⁡ ( 2) < ∞. H(2)<\infty. Nevertheless some authors (e.g. [27]) attribute to Mourtada the proof of the finite cyclicity of any hyperbolic polycycle in an unpublished series of manuscripts (see [18, Theorem 0] and references therein). For other results about the cyclicity of quadratic hemicycles in this context the interested reader is referred to [5, 26].

Note that Theorem B provides the cyclicity of Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} individually, i.e., taking Π = { Γ u } \Pi=\{\Gamma_{u}\} and Π = { Γ ℓ } \Pi=\{\Gamma_{\ell}\} in Definition 1. In our third main result we study the cyclicity of Π = { Γ u, Γ ℓ } \Pi=\{\Gamma_{u},\Gamma_{\ell}\}, cf. Remark 1, when we perturb ( 7) (\ref{DSq}) inside the family of quadratic differential systems. In its statement we use the following parameter subsets:

 |  | 𝒦 1:= { ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2): a 0 + b 0 ⩽ 0 ​ or ​ a 0 − b 0 + 2 ⩽ 0 } \displaystyle\mathcal{K}_{1}\!:=\{(a_{0},b_{0})\in(-2,0)\times(0,2):a_{0}+b_{0}\leqslant 0\text{ or }a_{0}-b_{0}+2\leqslant 0\} |  |

and |

 |  | 𝒦 2:= { ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2): a 0 + b 0 > 0 ​ and ​ a 0 − b 0 + 2 > 0 }. \displaystyle\mathcal{K}_{2}\!:=\{(a_{0},b_{0})\in(-2,0)\times(0,2):a_{0}+b_{0}>0\text{ and }a_{0}-b_{0}+2>0\}. |  |

###### Theorem C.

If ( a 0, b 0) (a_{0},b_{0}) belongs to 𝒦 1 ∖ { a 0 = − 1 } \mathcal{K}_{1}\setminus\{a_{0}=-1\} ( ( respectively, 𝑂𝑃𝐸𝑁 𝒦 2) \mathcal{K}_{2}) then the cyclicity of Π = { Γ u, Γ ℓ } \Pi=\{\Gamma_{u},\Gamma_{\ell}\} when we perturb ( 7) (\ref{DSq}) inside the whole family of quadratic differential systems is exactly 3 ( ( respectively, 2)). Moreover it is at least 3 for ( a 0, b 0) ∈ { − 1 } × ( 0, 2). (a_{0},b_{0})\in\{-1\}\times(0,2).

We stress that Theorem C deals with the simultaneous bifurcation of limit cycles from Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell}, which are the outer boundaries of two period annuli. Note that if this simultaneous cyclicity is 3 then, as a consequence of Theorem B, two limit cycles bifurcate from Γ u \Gamma_{u} and one from Γ ℓ \Gamma_{\ell}, or vice versa. The simultaneous bifurcation of limit cycles from the two period annuli has been studied for a 0 = − 3 2 a_{0}=-\frac{3}{2} and a 0 = − 1 2 a_{0}=-\frac{1}{2} in [17] and [3], respectively, and also for ( a 0, b 0) = ( − 1 2, 1 2) (a_{0},b_{0})=(-\frac{1}{2},\frac{1}{2}) and ( a 0, b 0) = ( − 1, 1) (a_{0},b_{0})=(-1,1) in [24] and [8], respectively. The authors do not know of any previous work dealing with the simultaneous bifurcation from two polycycles.

We turn now to the statement of our last main result, Theorem D, which deals with alien limit cycles. This notion was introduced by Dumortier and Roussarie in [6], where the authors bring to light that there are limit cycles bifurcating from a polycycle which cannot be detected as a zero of the first Melnikov function (see also [2, 4, 11, 16]). Our aim in this paper with regard to this issue is twofold. On the one hand, to propose a definition of this phenomenon more intrinsic and geometric than the one used in the literature and not depending on the computation of Melnikov functions. On the other hand we want to show that there exist alien limit cycles in the context of *simultaneous bifurcations*. To this end, following Gavrilov [10] we first introduce the notion of cyclicity of an open subset U U as follows. (He considers the case when U U is a period annulus and here we extend it slightly.)

Let { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} be a germ of an analytic family of vector fields on 𝕊 2 \mathbb{S}^{2} and let K K be a compact subset of 𝕊 2 \mathbb{S}^{2}. We define the cyclicity of K K with respect to the germ { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} as

 | Cycl G ( ( K, X μ 0), X μ) = inf ε, δ > 0 sup μ ∈ B δ ​ ( μ 0) #{ γ ⊂ N ε ( K) limit cycle of X μ } ∈ ℤ ≥ 0 ∪ { ∞ }, \mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big)=\inf\limits_{\varepsilon,\delta>0}\sup\limits_{\mu\in B_{\delta}(\mu_{0})}\#\big\{\gamma\subset N_{\varepsilon}(K)\text{ limit cycle of $X_{\mu}$}\big\}\in\mathbb{Z}_{\geq 0}\cup\{\infty\}, |  |

where N ε ​ ( K) N_{\varepsilon}(K) is the tubular ε \varepsilon -neighbourhood of K K. If U ⊂ 𝕊 2 U\subset\mathbb{S}^{2} is open we define

 | Cycl G ​ ( ( U, X μ 0), X μ) = sup { Cycl G ​ ( ( U, X μ 0), X μ): K ⊂ U ​ compact }, \mathrm{Cycl}_{G}\big((U,X_{\mu_{0}}),X_{\mu}\big)=\sup\left\{\mathrm{Cycl}_{G}\big((U,X_{\mu_{0}}),X_{\mu}\big):K\subset U\text{ compact}\right\}, |  |

which may also be infinite. □ \square

In case that U U is a period annulus with finite cyclicity in the above sense, Gavrilov proves in [10, Theorem 1] that Cycl G ​ ( ( U, X μ 0), X μ) \mathrm{Cycl}_{G}\big((U,X_{\mu_{0}}),X_{\mu}\big) is the same as in an appropriate one-parameter analytic deformation. This is related with the notion of essential perturbation introduced by Illiev [12] and enables to tackle the problem by computing Melnikov functions. This well-known approach allows to bound the number of limit cycles bifurcating from any compact set K ⊂ U K\subset U by means of the Weierstrass Preparation Theorem, however it gives not enough information on U ∖ K. U\setminus K. This motivates the following definition.

Let { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} be a germ of an analytic family of vector fields on 𝕊 2 \mathbb{S}^{2} and consider an open subset U U of 𝕊 2 \mathbb{S}^{2}. We define the *boundary cyclicity of U U from inside*as

 | Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) = inf { Cycl G ​ ( ( U ∖ K, X μ 0), X μ): K ⊂ U ​ compact } ∈ ℤ ≥ 0 ∪ { ∞ }. \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)=\inf\left\{\mathrm{Cycl}_{G}\big((U\setminus K,X_{\mu_{0}}),X_{\mu}\big):K\subset U\text{ compact}\right\}\in\mathbb{Z}_{\geq 0}\cup\{\infty\}. |  |

□ \square

If ∂ U \partial U is a polycycle with a return map which is not the identity then it can be shown by a compactness and continuity argument that Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) = 0 \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)=0. On the other hand, we prove in Lemma 5.1 that

 | Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) ⩽ Cycl G ​ ( ( ∂ U, X μ 0), X μ). \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)\leqslant\mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big). |  |

These two facts lead to the following definition:

Let { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} be a germ of an analytic family of vector fields on 𝕊 2 \mathbb{S}^{2} such that X μ 0 X_{\mu_{0}} is a D-system satisfying hypothesis 𝐇𝟏 \mathbf{H1} and 𝐇𝟐 \mathbf{H2}. Assume additionally that the return maps ℛ u ​ ( ⋅, μ 0) \mathscr{R}_{u}(\,\cdot\,;\mu_{0}) and ℛ ℓ ​ ( ⋅, μ 0) \mathscr{R}_{\ell}(\,\cdot\,;\mu_{0}) of the hemicycles Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} are both the identity. Taking U = ℝ 2 ∖ { y = 0 } U=\mathbb{R}^{2}\setminus\{y=0\}, if

 | Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) < Cycl G ​ ( ( ∂ U, X μ 0), X μ) \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)<\mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big) |  |

then we say that an *alien limit cycle bifurcation*occurs at ∂ U = Γ u ∪ Γ ℓ \partial U=\Gamma_{u}\cup\Gamma_{\ell} from inside U U for { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}}. □ \square

We have not given the notion of alien limit cycle bifurcation for an arbitrary collection of limit periodic sets because the involved casuistry would make the definition more complicated than it should be. This is already evident for the case of the “figure eight-loop” in Figure 1. That being said, we do give the definition of alien limit cycle bifurcation for any unfolding of a polycycle satisfying rather natural hypothesis, which is the case of those 2-saddle cycles studied in [2, 4, 6, 11, 16]. This will be done in Section 5, see Definition 5. Our definition differs from the one used by Dumortier and Roussarie in [6] because we account only for limit cycles which cannot be detected as zeroes of any Melnikov function of *any*order, cf. Lemma 5.4.

Under the hypothesis in Definition 1, the vertices of Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} are hyperbolic saddles. In this case it follows from Lemma 5.2 that

 | Cycl G ​ ( ( ∂ U, X μ 0), X μ) = Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ). \mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)=\mathrm{Cycl}\big((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu}\big). |  |

Hence Definition 1 takes into account the *simultaneous*bifurcation of limit cycles from Γ u \Gamma_{u} and Γ ℓ. \Gamma_{\ell}. In this regard we obtain the following result about alien bifurcations in the quadratic family:

###### Theorem D.

If ( a 0, b 0) ∈ { ( − 1, 1), ( − 1 2, 1 2), ( − 1 2, 3 2) } (a_{0},b_{0})\in\{(-1,1),(-\frac{1}{2},\frac{1}{2}),(-\frac{1}{2},\frac{3}{2})\} then an alien limit cycle bifurcation occurs at Γ u ∪ Γ ℓ \Gamma_{u}\cup\Gamma_{\ell} when we perturb ( 7) (\ref{DSq}) inside the whole family of quadratic differential systems.

Let us remark that in the present paper we consider families of planar polynomial vector fields { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} and that the statements of our main results should more formally be addressed to the compactified family { p ⁡ ( X μ) } μ ∈ Λ \{p(X_{\mu})\}_{\mu\in\Lambda} of analytic vector fields on the Poincaré sphere 𝕊 2. \mathbb{S}^{2}. For simplicity in the exposition we commit an abuse of language by identifying both families. It is clear that the number of limit cycles of X μ X_{\mu} and p ⁡ ( X μ) p(X_{\mu}) is the same because the line at infinity ℓ ∞ \ell_{\infty} is invariant in all the cases under consideration. Related with this we note that, although the corresponding analytic extension of the polynomial vector field to 𝕊 2 \mathbb{S}^{2} does not descend to the quotient ℝ ​ ℙ 2 \mathbb{RP}^{2} of 𝕊 2 \mathbb{S}^{2} by the central symmetry with respect to the origin, the induced foliation does. Since limit cycles depend on the foliation, and not on the specific way in which the orbits are parametrized, one could consider the notion of cyclicity in the real projective plane ℝ ​ ℙ 2 \mathbb{RP}^{2} instead of the sphere 𝕊 2 \mathbb{S}^{2}. It is worth to point out that these two notions are not equivalent. Indeed, the two hemicycles Γ u \Gamma_{u} and Γ ℓ \Gamma_{\ell} in 𝕊 2 \mathbb{S}^{2} project to the same polycycle Γ ¯ u = Γ ¯ ℓ \bar{\Gamma}_{u}=\bar{\Gamma}_{\ell} on ℝ ​ ℙ 2 \mathbb{RP}^{2} (see Figure 5) and by applying Theorems B and C, respectively,

 | Cycl ⁡ ( ( Γ u, X μ 0), X μ) = 2 ​ and ​ Cycl ℝ ​ ℙ 2 ​ ( ( Γ ¯ u, X μ 0), X μ) = 3 \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)=2\text{ and }\mathrm{Cycl}_{\mathbb{RP}^{2}}\big((\bar{\Gamma}_{u},X_{\mu_{0}}),X_{\mu}\big)=3 |  |

for any ( a 0, b 0) ∈ 𝒦 1 ∖ { a 0 = − 1 } (a_{0},b_{0})\in\mathcal{K}_{1}\setminus\{a_{0}=-1\}.

[image: Refer to caption] Figure 5: Quadratic reversible double centers in ( 7) (\ref{DSq}) compactified to the Moebius strip ℝ ​ ℙ 2 ∖ 𝔻 \mathbb{RP}^{2}\setminus\mathbb{D}. One of the two centers is depicted at the front of the drawing, while we place the other one in the removed invariant disk 𝔻 \mathbb{D} for convenience. The polycycle Γ ¯ u = Γ ¯ ℓ \bar{\Gamma}_{u}=\bar{\Gamma}_{\ell} is represented by the two circles in blue and green intersecting at the saddle point at the back.

The paper is organized as follows. Sections 2 and 3 are devoted to prove Theorems A and B, respectively. Both results strongly rely on the asymptotic development of the difference map 𝒟 ⁡ ( s, μ) \mathscr{D}(s;\mu) given in Theorem 2.1. This is a rather technical result that follows by applying the tools developed in [19, 20, 21] to study the Dulac map and its proof is deferred to Appendix B for reader’s convenience. Another important ingredient in the proof of Theorem B is Theorem 3.5, which provides a very useful division of the difference map in the ideal generated by its coefficients. The proofs of Theorems C and D are given in sections 4 and 5, respectively. Appendix A gathers the essential definitions and results from [19, 20, 21] that we use in the present paper, together with some other auxiliary results. Finally, in Appendix B we demonstrate Theorem 2.1 and Proposition 3.2, which have the longest and most technical proofs.

## 2 Proof of Theorem A

In this section we consider the family of vector fields { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} given by ( 1) (\ref{DS}) and satisfying the hypothesis H1 and H2. We take two local transverse sections, Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2} parametrised, respectively, by s ↦ ( 0, 1 s) s\mapsto(0,\frac{1}{s}) and s ↦ ( 0, s) s\mapsto(0,s) with s > 0. s>0. We also define D + ​ ( s, μ) D_{+}(s;\mu) to be the Dulac map of X μ X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} and D − ​ ( s, μ) D_{-}(s;\mu) to be the Dulac map of − X μ -X_{\mu} from Σ 1 \Sigma_{1} to Σ 2, \Sigma_{2}, see Figure 6. The limit cycles of X μ X_{\mu} that are close to Γ u \Gamma_{u} in Hausdorff sense are in one to one correspondence with the isolated positive zeroes of the *difference map*

 | 𝒟 ⁡ ( s, μ):= D + ​ ( s, μ) − D − ​ ( s, μ) \mathscr{D}(s;\mu)\!:=D_{+}(s;\mu)-D_{-}(s;\mu) |  |

near s = 0. s=0. The following result gives the asymptotic development of 𝒟 ⁡ ( s, μ) \mathscr{D}(s;\mu) at s = 0 s=0 and the functions λ, \lambda, F 1 F_{1}, F 2 F_{2}, F 3 F_{3} and d 0 d_{0} in its statement are the ones defined in ( 2) (\ref{K}), ( 3) (\ref{F1}), ( 4) (\ref{F2}), ( 5) (\ref{F3}) and ( 6) (\ref{d0}), respectively. In the statement we use the Ecalle-Roussarie comensator ω ⁡ ( s, α) \omega(s;\alpha), see Definition A, and ℱ ℓ ∞ ​ ( μ 0) \mathcal{F}_{\ell}^{\infty}(\mu_{0}) stands for a function ℓ \ell -flat with respect to s s at μ 0 \mu_{0}, see Definition A.

###### Theorem 2.1.

Let us fix any μ 0 ∈ Λ \mu_{0}\in\Lambda and set λ 0:= λ ⁡ ( μ 0). \lambda_{0}\!:=\lambda(\mu_{0}). Then 𝒟 ⁡ ( s, μ) = Δ 0 ​ ( μ) ​ s λ + ℱ ℓ ∞ ​ ( μ 0) \mathscr{D}(s;{\mu})=\Delta_{0}({\mu})s^{\lambda}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) for any ℓ ∈ [λ 0, min ⁡ ( 2 ​ λ 0, λ 0 + 1)), {\ell}\in\big[\lambda_{0},\min(2\lambda_{0},\lambda_{0}+1)\big), where Δ 0 \Delta_{0} is an analytic function at μ 0 \mu_{0} that can be written as Δ 0 = κ 0 ​ d 0 \Delta_{0}=\kappa_{0}d_{0}, with κ 0 \kappa_{0} analytic at μ 0 \mu_{0} and κ 0 ​ ( μ 0) > 0. \kappa_{0}(\mu_{0})>0. In addition,

1. ( 1) (1)

If λ 0 > 1 \lambda_{0}>1 then 𝒟 ⁡ ( s, μ) = Δ 0 ​ ( μ) ​ s λ + Δ 1 ​ ( μ) ​ s λ + 1 + ℱ ℓ ∞ ​ ( μ 0) \mathscr{D}(s;{\mu})=\Delta_{0}({\mu})s^{\lambda}+\Delta_{1}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) for any ℓ ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {\ell}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big). Furthermore Δ 1 \Delta_{1} is an analytic function at μ 0 \mu_{0} that can be written as Δ 1 = κ 1 ​ F 1 + κ ¯ 1 ​ Δ 0 \Delta_{1}=\kappa_{1}F_{1}+\bar{\kappa}_{1}\Delta_{0}, where κ 1 \kappa_{1} and κ ¯ 1 \bar{\kappa}_{1} are analytic at μ 0 \mu_{0} and κ 1 ​ ( μ 0) > 0. \kappa_{1}(\mu_{0})>0.

2. ( 2) (2)

If λ 0 < 1 \lambda_{0}<1 then 𝒟 ⁡ ( s, μ) = Δ 0 ​ ( μ) ​ s λ + Δ 2 ​ ( μ) ​ s 2 ​ λ + ℱ ℓ ∞ ​ ( μ 0) \mathscr{D}(s;{\mu})=\Delta_{0}({\mu})s^{\lambda}+\Delta_{2}({\mu})s^{2\lambda}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) for any ℓ ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big). Moreover Δ 2 \Delta_{2} is an analytic function at μ 0 \mu_{0} that can be written as Δ 2 = κ 2 ​ F 2 + κ ¯ 2 ​ Δ 0 \Delta_{2}=\kappa_{2}F_{2}+\bar{\kappa}_{2}\Delta_{0}, where κ 2 \kappa_{2} and κ ¯ 4 \bar{\kappa}_{4} are analytic at μ 0 \mu_{0} and κ 2 ​ ( μ 0) > 0. \kappa_{2}(\mu_{0})>0.

3. ( 3) (3)

If λ 0 = 1 \lambda_{0}=1 then 𝒟 ⁡ ( s, μ) = Δ 0 ​ ( μ) ​ s λ + Δ 3 ​ ( μ) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ 4 ​ ( μ) ​ s λ + 1 + ℱ ℓ ∞ ​ ( μ 0) \mathscr{D}(s;{\mu})=\Delta_{0}({\mu})s^{\lambda}+\Delta_{3}({\mu})s^{\lambda+1}\omega(s;1-\lambda)+\Delta_{4}(\mu)s^{\lambda+1}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) for any ℓ ∈ [2, 3) {\ell}\in[2,3) and where Δ 3 \Delta_{3} and Δ 4 \Delta_{4} are analytic functions at μ 0 \mu_{0}. Moreover there exist analytic functions κ 3 \kappa_{3} and κ ¯ 3 \bar{\kappa}_{3} at μ 0 \mu_{0} with κ 3 ​ ( μ 0) > 0 \kappa_{3}(\mu_{0})>0 such that the equality Δ 3 = κ 3 ​ F 3 + κ ¯ 3 ​ Δ 0 \Delta_{3}=\kappa_{3}F_{3}+\bar{\kappa}_{3}\Delta_{0} holds on { μ ∈ Λ: λ ⁡ ( μ) = 1 }. \{\mu\in\Lambda:\lambda(\mu)=1\}.

Figure 6: Dulac maps for the definition of 𝒟 = D + − D − \mathscr{D}=D_{+}-D_{-} in Theorem 2.1

Since the proof of Theorem 2.1 is rather long and technical and also requires several results from previous papers, we postpone it to Appendix B for reader’s convenience.

On account of the definition of d 1 d_{1} given in ( 6) (\ref{d0}), Theorem 2.1 provides the following information about the stability of the polycycle Γ u \Gamma_{u} for the vector field X μ 0 X_{\mu_{0}}:

1. ( a) (a)

If d 0 ​ ( μ 0) < 0 d_{0}(\mu_{0})<0 (respectively, d 0 ​ ( μ 0) > 0 d_{0}(\mu_{0})>0) then Γ u \Gamma_{u} is asymptotically stable (respectively, unstable).

2. ( b) (b)

If d 0 ​ ( μ 0) = 0 d_{0}(\mu_{0})=0 and d 1 ​ ( μ 0) < 0 d_{1}(\mu_{0})<0 (respectively, d 1 ​ ( μ 0) > 0 d_{1}(\mu_{0})>0) then Γ u \Gamma_{u} is asymptotically stable (respectively, unstable).

The key point for this observation is that the functions κ i \kappa_{i} in the statement of Theorem 2.1 are strictly positive at μ 0. \mu_{0}. □ \square

For simplicity in the exposition, from now on we will use the following definition.

Let h ⁡ ( s, μ) h(s;\mu) be a function in 𝒞 s > 0 ∞ ​ ( U) \mathscr{C}^{\infty}_{s>0}(U) for some open set U ⊂ ℝ N. U\subset\mathbb{R}^{N}. Given any μ 0 ∈ U \mu_{0}\in U we define 𝒵 0 ​ ( h ⁡ ( ⋅, μ), μ 0) \mathcal{Z}_{0}(h(\,\cdot\,;\mu),\mu_{0}) to be the smallest integer ℓ \ell having the property that there exist δ > 0 \delta>0 and a neighbourhood V V of μ 0 \mu_{0} such that for every μ ∈ V \mu\in V the function h ⁡ ( s, μ) h(s;\mu) has no more than ℓ \ell isolated zeros on ( 0, δ) (0,\delta) counted with multiplicities. □ \square

Recall (see Figure 6) that the limit cycles of the vector field ( 1) (\ref{DS}) that are close to Γ u \Gamma_{u} in Hausdorff sense are in one to one correspondence with the isolated positive zeroes of the difference map

 | 𝒟 ⁡ ( s, μ) = D + ​ ( s, μ) − D − ​ ( s, μ) \mathscr{D}(s;\mu)=D_{+}(s;\mu)-D_{-}(s;\mu) |  |

near s = 0. s=0. Hence, see Definition 2, we have that Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩽ 𝒵 0 ​ ( 𝒟 ⁡ ( ⋅, μ), μ 0) \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\leqslant\mathcal{Z}_{0}\big(\mathscr{D}(\,\cdot\,;\mu),\mu_{0}\big). Note moreover that, by Theorem 2.1,

 | 𝒟 ⁡ ( s, μ) = Δ 0 ​ ( μ) ​ s λ + ℱ ℓ ∞ ​ ( μ 0) \mathscr{D}(s;{\mu})=\Delta_{0}({\mu})s^{\lambda}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) |  | (8) |

for any ℓ ∈ [λ 0, min ⁡ ( 2 ​ λ 0, λ 0 + 1)), {\ell}\in\big[\lambda_{0},\min(2\lambda_{0},\lambda_{0}+1)\big), where λ 0:= λ ⁡ ( μ 0) \lambda_{0}\!:=\lambda(\mu_{0}) and Δ 0 = κ 0 ​ d 0 \Delta_{0}=\kappa_{0}d_{0} with κ 0 ​ ( μ 0) > 0. \kappa_{0}(\mu_{0})>0. If d 0 ​ ( μ 0) ≠ 0 d_{0}(\mu_{0})\neq 0 then, taking any ℓ > λ 0 \ell>\lambda_{0} (see Definition A),

 | lim ( s, μ) → ( 0 +, μ 0) s − λ ​ 𝒟 ​ ( s, μ) = Δ 0 ​ ( μ 0) ≠ 0, \lim_{(s,\mu)\to(0^{+},\mu_{0})}s^{-\lambda}\mathscr{D}(s;{\mu})=\Delta_{0}(\mu_{0})\neq 0, |  |

which implies 𝒵 0 ​ ( 𝒟 ⁡ ( ⋅, μ), μ 0) = 0 \mathcal{Z}_{0}\big(\mathscr{D}(\,\cdot\,;\mu),\mu_{0}\big)=0 and proves ( a) (a).

On the other hand, since 𝒟 ⁡ ( ⋅, μ 0) ≡ 0 \mathscr{D}(\,\cdot\,;\mu_{0})\equiv 0 if, and only if, ℛ u ​ ( ⋅, μ 0) ≡ Id, \mathscr{R}_{u}(\,\cdot\,;\mu_{0})\equiv\text{Id}, the assertion in ( b) (b) follows from the equality in ( 8) (\ref{teoAeq1}) by applying Proposition A.12 with n = 1. n=1.

We turn next to the proof of ( c) (c) and ( d) (d). To this end we shall use that, by applying Theorem 2.1,

 | 𝒟 ⁡ ( s, μ) = Δ 0 ​ ( μ) ​ s λ + { Δ 1 ​ ( μ) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ 0) if λ 0 > 1, Δ 2 ​ ( μ) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ 0) if λ 0 < 1, Δ 3 ​ ( μ) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ 4 ​ ( μ) ​ s λ + 1 + ℱ ℓ 3 ∞ ​ ( μ 0) if λ 0 = 1, \mathscr{D}(s;\mu)=\Delta_{0}({\mu})s^{\lambda}+\left\{\begin{array}[]{ll}\Delta_{1}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}>1,$}\\[10.0pt] \Delta_{2}({\mu})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}<1,$}\\[10.0pt] \Delta_{3}({\mu})s^{\lambda+1}\omega(s;1-\lambda)+\Delta_{4}(\mu)s^{\lambda+1}+\mathcal{F}_{\ell_{3}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}=1,$}\end{array}\right. |  | (9) |

for any ℓ 1 ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {\ell_{1}}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big), ℓ 2 ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell_{2}}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big) and ℓ 3 ∈ [2, 3) \ell_{3}\in[2,3), respectively. Moreover, in its respective case, the coefficient Δ i \Delta_{i} is an analytic function at μ 0 \mu_{0}. In addition, for i ∈ { 0, 1, 2, 3 }, i\in\{0,1,2,3\}, there exist analytic functions κ i \kappa_{i} and κ ¯ i \bar{\kappa}_{i} at μ 0 \mu_{0} with κ i ​ ( μ 0) > 0 \kappa_{i}(\mu_{0})>0 such that we can write

 | Δ 0 = κ 0 ​ d 0, Δ 1 = κ 1 ​ F 1 + κ ¯ 1 ​ Δ 0, Δ 2 = κ 2 ​ F 2 + κ ¯ 2 ​ Δ 0 ​ and ​ Δ 3 | Λ 1 = ( κ 3 ​ F 3 + κ ¯ 3 ​ Δ 0) | Λ 1 \Delta_{0}=\kappa_{0}d_{0},\quad\Delta_{1}=\kappa_{1}F_{1}+\bar{\kappa}_{1}\Delta_{0},\quad\Delta_{2}=\kappa_{2}F_{2}+\bar{\kappa}_{2}\Delta_{0}\,\text{ and }\,\left.\Delta_{3}\right|_{\Lambda_{1}}=\left.(\kappa_{3}F_{3}+\bar{\kappa}_{3}\Delta_{0})\right|_{\Lambda_{1}} |  | (10) |

where recall that Λ 1:= { μ ∈ Λ: λ ⁡ ( μ) = 1 }. \Lambda_{1}\!:=\{\mu\in\Lambda:\lambda(\mu)=1\}.

In order to show ( c) (c) we can suppose that Δ 0 = κ 0 ​ d 0 \Delta_{0}=\kappa_{0}d_{0} vanishes at μ 0 \mu_{0} because otherwise we have already proved that Cycl ⁡ ( ( Γ u, X μ 0), X μ) = 0. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)=0. On account of this the assumption d 1 ​ ( μ 0) ≠ 0 d_{1}(\mu_{0})\neq 0 implies, see the definition given in ( 6) (\ref{d0}), that Δ 1 ​ ( μ 0) ≠ 0 \Delta_{1}(\mu_{0})\neq 0 if λ 0 > 1, \lambda_{0}>1, Δ 2 ​ ( μ 0) ≠ 0 \Delta_{2}(\mu_{0})\neq 0 if λ 0 < 1 \lambda_{0}<1 and Δ 3 ​ ( μ 0) ≠ 0 \Delta_{3}(\mu_{0})\neq 0 if λ 0 = 1. \lambda_{0}=1. In the first case, from ( 9) (\ref{teoAeq3}) and applying Lemma A.7,

 | ∂ s ( s − λ ​ 𝒟 ​ ( s, μ)) \displaystyle\partial_{s}\big(s^{-\lambda}\mathscr{D}(s;\mu)\big) | = ∂ s ( Δ 0 ​ ( μ) + Δ 1 ​ ( μ) ​ s + s − λ ​ ℱ ℓ 1 ∞ ​ ( μ 0)) \displaystyle=\partial_{s}\big(\Delta_{0}(\mu)+\Delta_{1}(\mu)s+s^{-\lambda}\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})\big) |  |

 |  | = Δ 1 ​ ( μ) − λ ​ s − λ − 1 ​ ℱ ℓ 1 ∞ ​ ( μ 0) + s − λ ​ ℱ ℓ 1 − 1 ∞ ​ ( μ 0) \displaystyle=\Delta_{1}(\mu)-\lambda s^{-\lambda-1}\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})+s^{-\lambda}\mathcal{F}_{\ell_{1}-1}^{\infty}(\mu_{0}) |  |

 |  | = Δ 1 ​ ( μ) + ℱ ε ∞ ​ ( μ 0) \displaystyle=\Delta_{1}(\mu)+\mathcal{F}_{\varepsilon}^{\infty}(\mu_{0}) |  |

for some ε > 0 \varepsilon>0 small enough since we can take ℓ 1 > λ 0 + 1 \ell_{1}>\lambda_{0}+1. Therefore, see Definition A, the derivative ∂ s ( s − λ ​ 𝒟 ​ ( s, μ)) \partial_{s}\big(s^{-\lambda}\mathscr{D}(s;\mu)\big) tends to Δ 1 ​ ( μ 0) ≠ 0 \Delta_{1}(\mu_{0})\neq 0 as ( s, μ) → ( 0 +, μ 0). (s,\mu)\to(0^{+},\mu_{0}). Thus, by applying Rolle’s Theorem,

 | Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩽ 𝒵 0 ​ ( 𝒟 ⁡ ( ⋅, μ), μ 0) ⩽ 1, \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\leqslant\mathcal{Z}_{0}\big(\mathscr{D}(\,\cdot\,;\mu),\mu_{0}\big)\leqslant 1, |  |

as desired. Similarly, in the second case (i.e., λ 0 < 1 \lambda_{0}<1) we have that

 | ∂ s ( s − λ ​ 𝒟 ​ ( s, μ)) = λ ​ Δ 2 ​ ( μ) ​ s λ − 1 + ℱ ε ∞ ​ ( μ 0) = s λ − 1 ​ ( λ ​ Δ 2 ​ ( μ) + s 1 − λ ​ ℱ ε ∞ ​ ( μ 0)) \partial_{s}\big(s^{-\lambda}\mathscr{D}(s;\mu)\big)=\lambda\Delta_{2}(\mu)s^{\lambda-1}+\mathcal{F}_{\varepsilon}^{\infty}(\mu_{0})=s^{\lambda-1}\big(\lambda\Delta_{2}(\mu)+s^{1-\lambda}\mathcal{F}_{\varepsilon}^{\infty}(\mu_{0})\big) |  |

for some ε > 0 \varepsilon>0 small enough. Then, due to Δ 2 ​ ( μ 0) ≠ 0 \Delta_{2}(\mu_{0})\neq 0, we conclude by Rolle’s Theorem as before that 𝒵 0 ​ ( 𝒟 ⁡ ( ⋅, μ), μ 0) ⩽ 1 \mathcal{Z}_{0}\big(\mathscr{D}(\,\cdot\,;\mu),\mu_{0}\big)\leqslant 1. If λ 0 = 1 \lambda_{0}=1 then, from ( 9) (\ref{teoAeq3}) once again and taking ℓ 3 ∈ [2, 3) \ell_{3}\in[2,3) into account, the application of Lemma A.7 yields

 | ∂ s ( s − λ ​ 𝒟 ​ ( s, μ)) \displaystyle\partial_{s}\big(s^{-\lambda}\mathscr{D}(s;\mu)\big) | = ∂ s ( Δ 0 ​ ( μ) + Δ 3 ​ ( μ) ​ s ​ ω ​ ( s, 1 − λ) + Δ 4 ​ ( μ) ​ s + s − λ ​ ℱ ℓ 3 ∞ ​ ( μ 0)) \displaystyle=\partial_{s}\big(\Delta_{0}(\mu)+\Delta_{3}(\mu)s\omega(s;1-\lambda)+\Delta_{4}(\mu)s+s^{-\lambda}\mathcal{F}_{\ell_{3}}^{\infty}(\mu_{0})\big) |  |

 |  | = Δ 3 ​ ( μ) ​ λ ​ ω ​ ( s, 1 − λ) + Δ 4 ​ ( μ) − Δ 3 ​ ( μ) + ℱ ε ∞ ​ ( μ 0) \displaystyle=\Delta_{3}(\mu)\lambda\omega(s;1-\lambda)+\Delta_{4}(\mu)-\Delta_{3}(\mu)+\mathcal{F}_{\varepsilon}^{\infty}(\mu_{0}) |  |

for ε > 0 \varepsilon>0 small enough. Here we use that ∂ s s ​ ω ​ ( s, α) = ( 1 − α) ​ ω ​ ( s, α) − 1, \partial_{s}s\omega(s;\alpha)=(1-\alpha)\omega(s;\alpha)-1, see Definition A. Consequently, after dividing the above asymptotic expansion by its leading monomial, one can show that if ( s, μ) → ( 0 +, μ 0) (s,\mu)\to(0^{+},\mu_{0}) then

 | ∂ s ( s − λ ​ 𝒟 ​ ( s, μ)) ω ⁡ ( s, 1 − λ) = λ ​ Δ 3 ​ ( μ) + Δ 4 ​ ( μ) − Δ 3 ​ ( μ) ω ⁡ ( s, 1 − λ) + ℱ ε ∞ ​ ( μ 0) ω ⁡ ( s, 1 − λ) → λ 0 ​ Δ 3 ​ ( μ 0) ≠ 0, \frac{\partial_{s}\big(s^{-\lambda}\mathscr{D}(s;\mu)\big)}{\omega(s;1-\lambda)}=\lambda\Delta_{3}(\mu)+\frac{\Delta_{4}(\mu)-\Delta_{3}(\mu)}{\omega(s;1-\lambda)}+\frac{\mathcal{F}_{\varepsilon}^{\infty}(\mu_{0})}{\omega(s;1-\lambda)}\to\lambda_{0}\Delta_{3}(\mu_{0})\neq 0, |  |

since lim ( s, α) → ( 0 +, 0) 1 ω ⁡ ( s, α) = 0 \lim_{(s,\alpha)\to(0^{+},0)}\frac{1}{\omega(s;\alpha)}=0 by ( a) (a) in [19, Lemma A.4]. By Rolle’s Theorem again, this implies that 𝒵 0 ​ ( 𝒟 ⁡ ( ⋅, μ), μ 0) ⩽ 1 \mathcal{Z}_{0}\big(\mathscr{D}(\,\cdot\,;\mu),\mu_{0}\big)\leqslant 1 in the case λ 0 = 1 \lambda_{0}=1 as well and completes the proof of assertion ( c) (c).

Let us show finally the validity of the two assertions in ( d) (d). The first one concerns the case μ 0 ∉ Λ 1, \mu_{0}\notin\Lambda_{1}, i.e., λ 0 ≠ 1. \lambda_{0}\neq 1. If λ 0 > 1 \lambda_{0}>1 then, from ( 9) (\ref{teoAeq3}),

 | s − λ ​ 𝒟 ​ ( s, μ) \displaystyle s^{-\lambda}\mathscr{D}(s;\mu) | = Δ 0 ​ ( μ) + Δ 1 ​ ( μ) ​ s + f 2 ​ ( s, μ) \displaystyle=\Delta_{0}(\mu)+\Delta_{1}(\mu)s+f_{2}(s;\mu) |  |

 |  | = κ 0 ​ d 0 + ( κ 1 ​ F 1 + κ ¯ 1 ​ κ 0 ​ d 0) ​ s + f 2 ​ ( s, μ) \displaystyle=\kappa_{0}d_{0}+(\kappa_{1}F_{1}+\bar{\kappa}_{1}\kappa_{0}d_{0})s+f_{2}(s;\mu) |  |

 |  | = d 0 ​ κ 0 ​ ( 1 + κ ¯ 1 ​ s) + d 1 ​ κ 1 ​ s + f 2 ​ ( s, μ), \displaystyle=d_{0}\kappa_{0}(1+\bar{\kappa}_{1}s)+d_{1}\kappa_{1}s+f_{2}(s;\mu), |  |

where in the first equality f 2 ∈ s − λ ​ ℱ ℓ 1 ∞ ​ ( μ 0) ⊂ ℱ 1 + ε ∞ ​ ( μ 0) f_{2}\in s^{-\lambda}\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})\subset\mathcal{F}_{1+\varepsilon}^{\infty}(\mu_{0}) for ε > 0 \varepsilon>0 small enough by Lemma A.7 due to ℓ 1 > λ 0 + 1 \ell_{1}>\lambda_{0}+1, in the second one we take ( 10) (\ref{teoAeq5}) into account, and in the third one that d 1 ​ ( μ) = F 1 ​ ( μ) d_{1}(\mu)=F_{1}(\mu) if λ ⁡ ( μ) > 1. \lambda(\mu)>1. Thus, setting f 0 ​ ( s, μ) = κ 0 ​ ( 1 + κ ¯ 1 ​ s) f_{0}(s;\mu)=\kappa_{0}(1+\bar{\kappa}_{1}s) and f 1 ​ ( s, μ) = κ 1 ​ s f_{1}(s;\mu)=\kappa_{1}s, we can write

 | s − λ ​ 𝒟 ​ ( s, μ) = d 0 ​ ( μ) ​ f 0 ​ ( s, μ) + d 1 ​ ( μ) ​ f 1 ​ ( s, μ) + f 2 ​ ( s, μ). s^{-\lambda}\mathscr{D}(s;\mu)=d_{0}(\mu)f_{0}(s;\mu)+d_{1}(\mu)f_{1}(s;\mu)+f_{2}(s;\mu). |  | (11) |

By assumption we have that d 0 d_{0} and d 1 d_{1} vanish and are independent at μ 0 \mu_{0} and that 𝒟 ⁡ ( ⋅, μ 0) ≢ 0 \mathscr{D}(\,\cdot\,;\mu_{0})\not\equiv 0 due to ℛ u ​ ( ⋅, μ 0) ≢ Id \mathscr{R}_{u}(\,\cdot\,;\mu_{0})\not\equiv\text{Id}. Accordingly, since f 1 ​ ( s, μ) f 0 ​ ( s, μ) = κ 1 ​ s κ 0 ​ ( 1 + κ ¯ 1 ​ s) \frac{f_{1}(s;\mu)}{f_{0}(s;\mu)}=\frac{\kappa_{1}s}{\kappa_{0}(1+\bar{\kappa}_{1}s)} and f 2 ​ ( s, μ) f 1 ​ ( s, μ) ∈ s − 1 ​ ℱ 1 + ε ∞ ​ ( μ 0) \frac{f_{2}(s;\mu)}{f_{1}(s;\mu)}\in s^{-1}\mathcal{F}_{1+\varepsilon}^{\infty}(\mu_{0}) tend to zero as s → 0 + s\to 0^{+}, we can apply Proposition A.12 with n = 2 n=2 to conclude that Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 2. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 2. If λ 0 < 1 \lambda_{0}<1 then following verbatim from ( 9) (\ref{teoAeq3}) and ( 10) (\ref{teoAeq5}) we get the equality in ( 11) (\ref{teoAeq4}) with f 0 ​ ( s, μ) = κ 0 ​ ( 1 + κ ¯ 2 ​ s λ) f_{0}(s;\mu)=\kappa_{0}(1+\bar{\kappa}_{2}s^{\lambda}), f 1 ​ ( s, μ) = κ 2 ​ s λ f_{1}(s;\mu)=\kappa_{2}s^{\lambda} and f 2 ∈ s − λ ​ ℱ ℓ 2 ∞ ​ ( μ 0) ⊂ ℱ λ 0 + ε ∞ ​ ( μ 0) f_{2}\in s^{-\lambda}\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})\subset\mathcal{F}_{\lambda_{0}+\varepsilon}^{\infty}(\mu_{0}). Thus the assumptions in Proposition A.12 are also verified and so the lower bound Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 2 \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 2 is true for the case λ 0 > 1 \lambda_{0}>1 as well. Let us consider finally the case λ 0 = 1, \lambda_{0}=1, which is slightly different. In this case, from ( 9) (\ref{teoAeq3}) and taking Definition A into account, if μ ∈ Λ 1 \mu\in\Lambda_{1} then

 | s − λ ​ 𝒟 ​ ( s, μ) \displaystyle s^{-\lambda}\mathscr{D}(s;\mu) | = Δ 0 ​ ( μ) − Δ 3 ​ ( μ) ​ s ​ log ⁡ s + Δ 4 ​ ( μ) ​ s + f ^ 2 ​ ( s, μ) \displaystyle=\Delta_{0}(\mu)-\Delta_{3}(\mu)s\log s+\Delta_{4}(\mu)s+\hat{f}_{2}(s;\mu) |  |

 |  | = d 0 ​ κ 0 ​ ( 1 − κ ¯ 3 ​ s ​ log ⁡ s) − F 3 ​ κ 3 ​ s ​ log ⁡ s + Δ 4 ​ s + f ^ 2 ​ ( s, μ), \displaystyle=d_{0}\kappa_{0}(1-\bar{\kappa}_{3}s\log s)-F_{3}\kappa_{3}s\log s+\Delta_{4}s+\hat{f}_{2}(s;\mu), |  |

where in the first equality f ^ 2 ∈ s − 1 ​ ℱ ℓ 3 ∞ ​ ( μ 0) ⊂ ℱ 1 + ε ∞ ​ ( μ 0) \hat{f}_{2}\in s^{-1}\mathcal{F}_{\ell_{3}}^{\infty}(\mu_{0})\subset\mathcal{F}_{1+\varepsilon}^{\infty}(\mu_{0}) and the second one follows from ( 10) (\ref{teoAeq5}) due to μ ∈ Λ 1 \mu\in\Lambda_{1}. Hence, since d 1 = F 3 d_{1}=F_{3} on Λ 1, \Lambda_{1}, we can write

 | s − λ ​ 𝒟 ​ ( s, μ) | μ ∈ Λ 1 = d 0 | Λ 1 ​ f 0 ​ ( s, μ) + d 1 | Λ 1 ​ f 1 ​ ( s, μ) + f 2 ​ ( s, μ) \left.s^{-\lambda}\mathscr{D}(s;\mu)\right|_{\mu\in\Lambda_{1}}=\left.d_{0}\right|_{\Lambda_{1}}f_{0}(s;\mu)+\left.d_{1}\right|_{\Lambda_{1}}f_{1}(s;\mu)+f_{2}(s;\mu) |  |

taking the functions f 0 ​ ( s, μ) = κ 0 ​ ( 1 − κ ¯ 3 ​ s ​ log ⁡ s), f_{0}(s;\mu)=\kappa_{0}(1-\bar{\kappa}_{3}s\log s), f 1 ​ ( s, μ) = − κ 3 ​ s ​ log ⁡ s f_{1}(s;\mu)=-\kappa_{3}s\log s and f 2 ​ ( s, μ) = Δ 4 ​ s + f ^ ​ ( s, μ). f_{2}(s;\mu)=\Delta_{4}s+\hat{f}(s;\mu). Once again, f 1 ​ ( s, μ) f 0 ​ ( s, μ) = − κ 3 ​ s ​ log ⁡ s κ 0 ​ ( 1 − κ ¯ 3 ​ s ​ log ⁡ s) \frac{f_{1}(s;\mu)}{f_{0}(s;\mu)}=-\frac{\kappa_{3}s\log s}{\kappa_{0}(1-\bar{\kappa}_{3}s\log s)} and f 2 ​ ( s, μ) f 1 ​ ( s, μ) = − Δ 4 + s − 1 ​ f ^ ​ ( s, μ) κ 3 ​ log ⁡ s \frac{f_{2}(s;\mu)}{f_{1}(s;\mu)}=-\frac{\Delta_{4}+s^{-1}\hat{f}(s;\mu)}{\kappa_{3}\log s} tend to zero as s → 0 + s\to 0^{+} and, on the other hand, d 1 | Λ 1 \left.d_{1}\right|_{\Lambda_{1}} and d 1 | Λ 1 \left.d_{1}\right|_{\Lambda_{1}} vanish and are independent at μ 0 \mu_{0} by assumption. Consequently, by applying Proposition A.12 with W = Λ 1 W=\Lambda_{1} and n = 2 n=2 we get that Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 2 \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 2 in case that λ 0 = 1, \lambda_{0}=1, as desired. This proves the second assertion in ( d) (d) and concludes the proof of the result.

## 3 Proof of Theorem B

The following result shows that to prove Theorem B it suffices to consider a 5-dimensional perturbation.

###### Lemma 3.1.

Any quadratic differential system which is close ( ( in the topology of coefficients)) to ( 7) (\ref{DSq}) for some ( a 0, b 0) ∈ ℝ 2 (a_{0},b_{0})\in\mathbb{R}^{2} with a 0 ≠ − 2 a_{0}\neq-2 can be brought by means of an affine change of coordinates and a constant rescaling of time to

 | X μ { x ˙ = b − 2 4 + ε 1 ​ x + ( 1 − b) ​ y + a ​ x 2 + ε 2 ​ x ​ y + b ​ y 2, y ˙ = ε 0 − 2 ​ x ​ y, X_{\mu}\quad\left\{\!\begin{array}[]{l}\dot{x}=\frac{b-2}{4}+\varepsilon_{1}x+(1-b)y+ax^{2}+\varepsilon_{2}xy+by^{2},\\[2.0pt] \dot{y}=\varepsilon_{0}-2xy,\end{array}\right. |  | (12) |

with ( a, b, ε 0, ε 1, ε 2) ≈ ( a 0, b 0, 0, 0, 0). (a,b,\varepsilon_{0},\varepsilon_{1},\varepsilon_{2})\approx(a_{0},b_{0},0,0,0).

We consider the group Aff ⁡ ( 2, ℝ) \mathrm{Aff}(2,\mathbb{R}) of affine transformations

 | g ⁡ ( x, y) = ( g 11 ​ x + g 12 ​ y + g 13, g 21 ​ x + g 22 ​ y + g 23) g(x,y)=(g_{11}x+g_{12}y+g_{13},g_{21}x+g_{22}y+g_{23}) |  |

and the pull-back g ⋆ ​ ( Y a, b) = ( D ​ g − 1) ​ ( Y a, b ∘ g) g^{\star}(Y_{a,b})=\big(Dg^{-1}\big)(Y_{a,b}\circ g) of

 | Y a, b:= ( ( 1 − b) y + b y 2 + b − 2 4 + a x 2) ∂ x − 2 x y ∂ y. Y_{a,b}\!:=\left((1-b)y+by^{2}+\frac{b-2}{4}+ax^{2}\right)\!\partial_{x}-2xy\partial_{y}. |  |

Note that Y a, b = w 0 + a ​ w 1 + b ​ w 2 Y_{a,b}=w_{0}+aw_{1}+bw_{2} with w 0:= ( y − 1 2) ∂ x − 2 x y ∂ y w_{0}\!:=(y-\frac{1}{2})\partial_{x}-2xy\partial_{y}, w 1:= x 2 ∂ x w_{1}\!:=x^{2}\partial_{x} and w 2:= ( − y + y 2 + 1 4) ∂ x w_{2}\!:=(-y+y^{2}+\frac{1}{4})\partial_{x}. An easy computation performed with Maple shows that if a 0 ≠ − 2 a_{0}\neq-2 then the vector fields v 0 = ∂ y v_{0}=\partial_{y}, v 1 = x ∂ x v_{1}=x\partial_{x} and v 2 = x y ∂ x v_{2}=xy\partial_{x} span a complementary to the tangent space at the point ( λ, g, a, b) = ( 1, id, a 0, b 0) (\lambda,g,a,b)=(1,\mathrm{id},a_{0},b_{0}) of the orbit

 | { λ g ⋆ ( Y a, b): λ ∈ ℝ ∗, g ∈ Aff ( 2, ℝ), a, b ∈ ℝ } \{\lambda g^{\star}(Y_{a,b}):\,\lambda\in\mathbb{R}^{*},\ g\in\mathrm{Aff}(2,\mathbb{R}),\ a,b\in\mathbb{R}\} |  |

in the 12 12 -dimensional space 𝒫 2 \mathcal{P}_{2} of all polynomial vector fields of degree 2. In other words, if a 0 ≠ − 2 a_{0}\neq-2 then the map F: U:= ℝ ∗ × Aff ⁡ ( 2, ℝ) × ℝ 5 → 𝒫 2 F:U\!:=\mathbb{R}^{*}\!\times\mathrm{Aff}(2,\mathbb{R})\times\mathbb{R}^{5}\to\mathcal{P}_{2} defined by

 | F ⁡ ( λ, g, a, b, ε 0, ε 1, ε 2) = λ ​ g ⋆ ​ ( Y a, b + ε 0 ​ v 0 + ε 1 ​ v 1 + ε 2 ​ v 2) F(\lambda,g,a,b,\varepsilon_{0},\varepsilon_{1},\varepsilon_{2})=\lambda g^{\star}\big(Y_{a,b}+\varepsilon_{0}v_{0}+\varepsilon_{1}v_{1}+\varepsilon_{2}v_{2}\big) |  |

is a local diffeomorphism between neighbourhoods of ( 1, id, a 0, b 0, 0, 0, 0) (1,\mathrm{id},a_{0},b_{0},0,0,0) in U U and Y a 0, b 0 Y_{a_{0},b_{0}} in 𝒫 2 \mathcal{P}_{2}. This proves the result.

We stress that henceforth X μ X_{\mu} refers to the differential system in ( 12) (\ref{pert}). That being said, the key point for our purposes is that X μ X_{\mu} writes as

 | { x ˙ = y ​ f ​ ( x, y, μ) + g ⁡ ( x, μ), y ˙ = ε 0 + y ​ q ​ ( x, y, μ), \left\{\!\begin{array}[]{l}\dot{x}=yf(x,y;\mu)+g(x;\mu),\\[2.0pt] \dot{y}=\varepsilon_{0}+yq(x,y;\mu),\end{array}\right. |  |

with f ⁡ ( x, y) = 1 − b + ε 2 ​ x + b ​ y, f(x,y)=1-b+\varepsilon_{2}x+by, g ⁡ ( x) = b − 2 4 + ε 1 ​ x + a ​ x 2 g(x)=\frac{b-2}{4}+\varepsilon_{1}x+ax^{2} and q ⁡ ( x, y) = − 2 ​ x, q(x,y)=-2x, so that X μ X_{\mu} is a D-system for ε 0 = 0 \varepsilon_{0}=0. Moreover one can easily check that X μ X_{\mu} with a ∈ ( − 2, 0) a\in(-2,0), b ∈ ( 0, 2) b\in(0,2), ε 0 = 0 \varepsilon_{0}=0, ε 1 ≈ 0 \varepsilon_{1}\approx 0 and ε 2 ≈ 0 \varepsilon_{2}\approx 0 verifies assumptions H1 and H2. Accordingly, for these parameter values, X μ X_{\mu} has a polycycle Γ u \Gamma_{u} at the boundary of the upper half-plane with two hyperbolic saddles, s 1 = { y = 0, x > 0 } ∩ ℓ ∞ s_{1}=\{y=0,x>0\}\cap\ell_{\infty} and s 2 = { y = 0, x < 0 } ∩ ℓ ∞ s_{2}=\{y=0,x<0\}\cap\ell_{\infty}. Since ε 0 \varepsilon_{0} does not affect the homogenous part of higher degree of X μ X_{\mu}, the location and character of these two singular points remains unaltered taking ε i ≈ 0 \varepsilon_{i}\approx 0 for i = 0, 1, 2. i=0,1,2.

Let us fix any μ 0 = ( a 0, b 0, ε 0, ε 1, ε 2) \mu_{0}=(a_{0},b_{0},\varepsilon_{0},\varepsilon_{1},\varepsilon_{2}) with ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2) and ε i ≈ 0 \varepsilon_{i}\approx 0 for i = 0, 1, 2. i=0,1,2. We take two transverse sections on x = 0 x=0: Σ 1 \Sigma_{1}, parametrized by s ↦ ( 0, 1 / s) s\mapsto(0,1/s) with s ∈ ( 0, δ), s\in(0,\delta), and Σ 2 \Sigma_{2}, parametrized by s ↦ ( 0, s) s\mapsto(0,s) with s ∈ ( − δ, δ). s\in(-\delta,\delta). For μ ≈ μ 0 \mu\approx\mu_{0} and δ > 0 \delta>0 small enough, we have a well defined Dulac map D + u ​ ( ⋅, μ) D^{u}_{+}(\,\cdot\,;\mu) for X μ X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} and a well defined Dulac map D − u ​ ( ⋅, μ) D^{u}_{-}(\,\cdot\,;\mu) for − X μ -X_{\mu} from Σ 1 \Sigma_{1} to Σ 2, \Sigma_{2}, see Figure 7. This follows by first applying the local center-stable manifold theorem (see [14, Theorem 1] for instance) and then appealing to the smooth dependence of the solutions of X μ X_{\mu} on initial conditions and parameters.

Figure 7: Phase portrait in the Poincaré disc of the vector field X μ X_{\mu} in ( 12) (\ref{pert}) for ε 0 = ε 1 = ε 2 = 0 \varepsilon_{0}=\varepsilon_{1}=\varepsilon_{2}=0 (left) and ε 0 ≠ 0 \varepsilon_{0}\neq 0 (right). On the right, Dulac maps D ± D_{\pm} to define the function 𝒟 u ​ ( s, μ) = D + u ​ ( s, μ) − D − u ​ ( s, μ) \mathscr{D}_{u}(s;\mu)=D^{u}_{+}(s;\mu)-D^{u}_{-}(s;\mu) studied in Proposition 3.2. The points in red are ( 0, D ± u ​ ( s)) (0,D^{u}_{\pm}(s)) and ( 0, 1 / s) (0,1/s).

In our next result we study the asymptotic development of the difference map

 | 𝒟 u ​ ( s, μ):= D + u ​ ( s, μ) − D − u ​ ( s, μ). \mathscr{D}_{u}(s;\mu)\!:=D^{u}_{+}(s;\mu)-D^{u}_{-}(s;\mu). |  |

It is clear that the positive zeros of this function are in one-to-one correspondence with the limit cycles of X μ X_{\mu} bifurcating from Γ u \Gamma_{u} to the upper half-plane.

###### Proposition 3.2.

Fix any μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) with ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2). Then

 | 𝒟 u ​ ( s, μ) = δ u + Δ 0 u ​ s λ + ℱ L ∞ ​ ( μ 0), for any L ∈ [λ 0, min ⁡ ( 2 ​ λ 0, λ 0 + 1)), \mathscr{D}_{u}(s;{\mu})=\delta_{u}+\Delta^{u}_{0}s^{\lambda}+\mathcal{F}_{{L}}^{\infty}(\mu_{0}),\text{ for any ${{L}}\in\big[\lambda_{0},\min(2\lambda_{0},\lambda_{0}+1)\big)$,} |  |

where λ \lambda, δ u \delta_{u} and Δ 0 u \Delta^{u}_{0} are smooth functions in a neighbourhood of μ 0 \mu_{0} and λ 0:= λ ⁡ ( μ 0) = − a 0 + 2 a 0. \lambda_{0}\!:=\lambda(\mu_{0})=-\frac{a_{0}+2}{a_{0}}. In addition 𝒟 u ​ ( s, μ 0) ≡ 0 \mathscr{D}_{u}(s;{\mu_{0}})\equiv 0, ∂ ε 0 δ u ​ ( μ 0) > 0 \partial_{\varepsilon_{0}}\delta_{u}(\mu_{0})>0, ∂ ε 1 δ u ​ ( μ 0) = ∂ ε 2 δ u ​ ( μ 0) = 0 \partial_{\varepsilon_{1}}\delta_{u}(\mu_{0})=\partial_{\varepsilon_{2}}\delta_{u}(\mu_{0})=0 and

 | Δ 0 u ​ ( μ) = − κ 01 ​ ( μ) ​ ( 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 + ε 2) + κ 02 ​ ( μ) ​ δ u ​ ( μ), \textstyle\Delta^{u}_{0}(\mu)=-\kappa_{01}(\mu)\left(2\frac{\sqrt{b(a+2)}}{\sqrt{a(b-2)}}\,\varepsilon_{1}+\varepsilon_{2}\right)+\kappa_{02}(\mu)\delta_{u}(\mu), |  |

where κ 0 ​ i \kappa_{0i} are smooth functions at μ = μ 0 \mu=\mu_{0} for i = 1, 2 i=1,2 and κ 01 ​ ( μ 0) > 0. \kappa_{01}(\mu_{0})>0. Furthermore the following assertions are also true in case that a 0 ≠ − 1: a_{0}\neq-1:

1. ( 1) (1)

If a 0 > − 1 a_{0}>-1 then 𝒟 u ​ ( s, μ) = δ u + Δ 0 u ​ s λ + Δ 1 u ​ s λ + 1 + ℱ L ∞ ​ ( μ 0) \mathscr{D}_{u}(s;{\mu})=\delta_{u}+\Delta^{u}_{0}s^{\lambda}+\Delta^{u}_{1}s^{\lambda+1}+\mathcal{F}_{{L}}^{\infty}(\mu_{0}) for any L ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {{L}}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big), where Δ 1 u \Delta^{u}_{1} is a smooth function in a neighbourhood of μ 0 \mu_{0} satisfying that

 | Δ 1 u ​ ( μ) = κ 11 ​ ( μ) ​ ( ε 1 + a ⁡ ( b − 1) 2 ​ ( a + 1) ​ b ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) + κ 12 ​ ( μ) ​ Δ 0 u ​ ( μ) + κ 13 ​ ( μ) ​ δ u ​ ( μ) \textstyle\Delta^{u}_{1}(\mu)=\kappa_{11}(\mu)\left(\varepsilon_{1}+\frac{a(b-1)}{2(a+1)b}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)+\kappa_{12}(\mu)\Delta^{u}_{0}(\mu)+\kappa_{13}(\mu)\delta_{u}(\mu) |  |

where κ 1 ​ i \kappa_{1i} are smooth functions at μ = μ 0 \mu=\mu_{0} for i = 1, 2, 3 i=1,2,3 and κ 11 ​ ( μ 0) > 0. \kappa_{11}(\mu_{0})>0.

2. ( 2) (2)

If a 0 < − 1 a_{0}<-1 then 𝒟 u ​ ( s, μ) = δ u + Δ 0 u ​ s λ + Δ 2 u ​ s 2 ​ λ + ℱ L ∞ ​ ( μ 0) \mathscr{D}_{u}(s;{\mu})=\delta_{u}+\Delta^{u}_{0}s^{\lambda}+\Delta^{u}_{2}s^{2\lambda}+\mathcal{F}_{{L}}^{\infty}(\mu_{0}) for any L ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {{L}}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big), where Δ 2 u \Delta^{u}_{2} is a smooth function in a neighbourhood of μ 0 \mu_{0} satisfying that

 | Δ 2 u ​ ( μ) = κ 21 ​ ( μ) ​ ( 2 ​ ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) ​ ε 1 + ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) + κ 22 ​ ( μ) ​ Δ 0 u ​ ( μ) + κ 23 ​ ( μ) ​ δ u ​ ( μ), \textstyle\Delta^{u}_{2}(\mu)=\kappa_{21}(\mu)\left(\frac{2(a+2)(b-1)}{(a+1)(b-2)}\varepsilon_{1}+\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)+\kappa_{22}(\mu)\Delta^{u}_{0}(\mu)+\kappa_{23}(\mu)\delta_{u}(\mu), |  |

where κ 2 ​ i \kappa_{2i} are smooth functions at μ = μ 0 \mu=\mu_{0} for i = 1, 2, 3 i=1,2,3 and κ 21 ​ ( μ 0) > 0. \kappa_{21}(\mu_{0})>0.

For reader’s convenience the proof of Proposition 3.2 is deferred to Subsection B.2.

Let us fix μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) with a 0 ∈ ( − 2, 0) a_{0}\in(-2,0) and b 0 ∈ ( 0, 2) b_{0}\in(0,2). The differential system ( 12) (\ref{pert}) has only two finite singularities for μ ≈ μ 0 \mu\approx\mu_{0}, which are of focus type and close to the points ( 0, 1 2) (0,\frac{1}{2}) and ( 0, b 0 − 2 2 ​ b 0) (0,\frac{b_{0}-2}{2b_{0}}). Let us denote them by c u ​ ( μ) c_{u}(\mu) and c ℓ ​ ( μ) c_{\ell}(\mu), respectively. We also define the parameter subset

 | 𝒵 u:= { μ ≈ μ 0: 𝒟 u ​ ( ⋅, μ) ≡ 0 }. \mathcal{Z}_{u}\!:=\{\mu\approx\mu_{0}:\mathscr{D}_{u}(\,\cdot\,;\mu)\equiv 0\}. |  |

The next result shows that 𝒵 u \mathcal{Z}_{u} is precisely the center manifold for the focus at ( 0, 1 2) (0,\frac{1}{2}). We remark, in connection with our discussion in Figure 4, that the subsets Z 0 Z_{0} and Z 1 Z_{1} correspond to the components Q 3 R Q_{3}^{R} and Q 3 L ​ V Q_{3}^{LV}, respectively. For completeness, we note that the combination of this result with Lemma 4.1 provides also the description of the center manifold for the focus at ( 0, b 0 − 2 2 ​ b 0) (0,\frac{b_{0}-2}{2b_{0}}).

###### Lemma 3.3.

𝒵 u = { μ ≈ μ 0: c u ​ ( μ) ​ is a center of ​ X μ } \mathcal{Z}_{u}=\textstyle\{\mu\approx\mu_{0}:c_{u}(\mu)\text{ is a center of }X_{\mu}\} and 𝒵 u = Z 0 ∪ Z 1 \mathcal{Z}_{u}=Z_{0}\cup Z_{1}, where

 | Z 0:= { μ ≈ μ 0: ε 0 = ε 1 = ε 2 = 0 } ​ and ​ Z 1:= { μ ≈ μ 0: a + b = ε 0 = 2 ​ ε 1 + ε 2 = 0 }. Z_{0}\!:=\{\mu\approx\mu_{0}:\varepsilon_{0}=\varepsilon_{1}=\varepsilon_{2}=0\}\text{ and }Z_{1}\!:=\{\mu\approx\mu_{0}:a+b=\varepsilon_{0}=2\varepsilon_{1}+\varepsilon_{2}=0\}. |  |

Moreover, if μ ∈ 𝒵 u \mu\in\mathcal{Z}_{u} then the period annulus of the center at ( 0, 1 2) (0,\frac{1}{2}) is { ( x, y) ∈ ℝ 2: y > 0 } ∖ { ( 0, 1 2) } \big\{(x,y)\in\mathbb{R}^{2}:y>0\big\}\setminus\{(0,\frac{1}{2})\}.

Let us fix μ ^ ≈ μ 0 \hat{\mu}\approx\mu_{0} and consider the straight line L L passing through the singularities c u ​ ( μ ^) c_{u}(\hat{\mu}) and c ℓ ​ ( μ ^) c_{\ell}(\hat{\mu}). These two points split L L into three open segments where X μ ^ X_{\hat{\mu}} is transverse because the vector field is quadratic. Let us denote the unbounded segment having c u ​ ( μ ^) c_{u}(\hat{\mu}) as endpoint by Σ 1 \Sigma_{1} and the bounded segment by Σ 2. \Sigma_{2}. We parametrize them analytically by σ 1: ( 0, 1) ⟶ Σ 1 {\sigma_{1}}\!:{(0,1)}\longrightarrow{\Sigma_{1}} and σ 2: ( 0, 1) ⟶ Σ 2 {\sigma_{2}}\!:{(0,1)}\longrightarrow{\Sigma_{2}}, respectively, such that lim s → 0 ‖ σ 1 ​ ( s) ‖ = + ∞ \lim_{s\to 0}\|\sigma_{1}(s)\|=+\infty, lim s → 1 σ 1 ​ ( s) = c u ​ ( μ ^) \lim_{s\to 1}\sigma_{1}(s)=c_{u}(\hat{\mu}), lim s → 0 σ 2 ​ ( s) = c ℓ ​ ( μ ^) \lim_{s\to 0}\sigma_{2}(s)=c_{\ell}(\hat{\mu}) and lim s → 1 σ 2 ​ ( s) = c u ​ ( μ ^). \lim_{s\to 1}\sigma_{2}(s)=c_{u}(\hat{\mu}). By transversality and the fact that c u ​ ( μ ^) c_{u}(\hat{\mu}) and c ℓ ​ ( μ ^) c_{\ell}(\hat{\mu}) are the only finite singularities of X μ ^ X_{\hat{\mu}}, the application of the Poincaré-Bendixson Theorem shows that there is a well defined Poincaré map for X μ ^ X_{\hat{\mu}} from Σ 1 \Sigma_{1} to Σ 2. \Sigma_{2}. Taking the parametrizations previously introduced, we denote it by 𝒫 +: ( 0, 1) ⟶ ( 0, 1) {\mathcal{P}_{+}}\!:{(0,1)}\longrightarrow{(0,1)}, which is an analytic function by applying the Implicit Function Theorem. Similarly, we denote by 𝒫 −: ( 0, 1) ⟶ ( 0, 1) {\mathcal{P}_{-}}\!:{(0,1)}\longrightarrow{(0,1)} the Poincaré map for − X μ ^ -X_{\hat{\mu}} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2}, which is analytic as well. Observe that, by construction, the periodic orbits surrounding c u ​ ( μ ^) c_{u}({\hat{\mu}}) correspond to zeros of 𝒟:= 𝒫 + − 𝒫 −. \mathcal{D}\!:=\mathcal{P}_{+}-\mathcal{P}_{-}. Moreover μ ^ ∈ 𝒵 u \hat{\mu}\in\mathcal{Z}_{u} if, and only if, 𝒟 ≡ 0 \mathcal{D}\equiv 0 on ( 0, δ 1) (0,\delta_{1}) and, on the other hand, c u ​ ( μ ^) c_{u}(\hat{\mu}) is a center if, and only if, 𝒟 ≡ 0 \mathcal{D}\equiv 0 on ( 1 − δ 2, 1). (1-\delta_{2},1). Accordingly, since 𝒟 \mathcal{D} is analytic on ( 0, 1) (0,1), this proves that μ ^ ∈ 𝒵 u \hat{\mu}\in\mathcal{Z}_{u} if, and only if, c u ​ ( μ ^) c_{u}(\hat{\mu}) is a center. So far we have proved that

 | 𝒵 u = { μ ≈ μ 0: c u ​ ( μ) ​ is a center of ​ X μ } =: U. \mathcal{Z}_{u}=\textstyle\{\mu\approx\mu_{0}:c_{u}(\mu)\text{ is a center of }X_{\mu}\}=:U. |  |

Our next task is to show that U = Z 0 ∪ Z 1. U=Z_{0}\cup Z_{1}. To prove the inclusion U ⊂ Z 0 ∪ Z 1 U\subset Z_{0}\cup Z_{1} we take any μ ∈ U \mu\in U and, due to U = 𝒵 u U=\mathcal{Z}_{u}, by applying Proposition 3.2 we get that δ u ​ ( μ) = 0 \delta_{u}(\mu)=0 and Δ 0 u ​ ( μ) = 0 \Delta_{0}^{u}(\mu)=0, which imply

 | ε 0 = 0 ​ and ​ 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 + ε 2 = 0. \varepsilon_{0}=0\text{ and }2\frac{\sqrt{b(a+2)}}{\sqrt{a(b-2)}}\,\varepsilon_{1}+\varepsilon_{2}=0. |  |

Here the first equality follows by the Implicit Function Theorem using that δ u | ε 0 ≡ 0 \delta_{u}|_{\varepsilon_{0}}\equiv 0 and ∂ ε 0 δ u ​ ( μ 0) ≠ 0. \partial_{\varepsilon_{0}}\delta_{u}(\mu_{0})\neq 0. Recall on the other hand that trace equal to zero is a necessary condition for a singular point to be a center. One can verify that if ε 0 = 0 \varepsilon_{0}=0 then c u ​ ( μ) = ( 0, 1 2) c_{u}(\mu)=(0,\frac{1}{2}) and that its trace is equal to ε 1 + 1 2 ​ ε 2 \varepsilon_{1}+\frac{1}{2}\varepsilon_{2}. The vanishing of this quantity, together with the two equalities above, yields to either { ε 0 = ε 1 = ε 2 = 0 } \{\varepsilon_{0}=\varepsilon_{1}=\varepsilon_{2}=0\} or { a + b = ε 0 = 2 ε 1 + ε 2 = 0 }. \{a+b=\varepsilon_{0}=2\varepsilon_{1}+\varepsilon_{2}=0\}. Therefore U ⊂ Z 0 ∪ Z 1 U\subset Z_{0}\cup Z_{1}. To prove the reverse inclusion we note first that if μ ∈ Z 0 \mu\in Z_{0} then the function

 | H 0 ​ ( x, y) = | y | a ​ ( x 2 + l ​ y 2 + m ​ y + n), H_{0}(x,y)=|y|^{a}(x^{2}+ly^{2}+my+n), |  |

with l = b a + 2 l=\frac{b}{a+2}, m = − b − 1 a + 1 m=-\frac{b-1}{a+1} and n = b − 2 4 ​ a n=\frac{b-2}{4a}, is a global first integral of X μ X_{\mu}. The continuity of H 0 H_{0} at c u ​ ( μ) c_{u}(\mu) implies that it must be a center, so that μ ∈ U. \mu\in U. Finally, if μ ∈ Z 1 \mu\in Z_{1} then one can verify that

 | H 1 ​ ( x, y) \displaystyle H_{1}(x,y) | = | y | a ​ ( r 1 ​ ( x, y) + i ​ α 1 ​ x) 1 − i ​ ε 2 α 1 ​ ( r 1 ​ ( x, y) − i ​ α 1 ​ x) 1 + i ​ ε 2 α 1 \displaystyle=|y|^{a}(r_{1}(x,y)+i\alpha_{1}x)^{1-i\frac{\varepsilon_{2}}{\alpha_{1}}}(r_{1}(x,y)-i\alpha_{1}x)^{1+i\frac{\varepsilon_{2}}{\alpha_{1}}} |  |

 |  | = | y | a ​ ( r 1 ​ ( x, y) 2 + α 1 2 ​ x 2) ​ e 2 ​ ε 2 α 1 ​ arg ​ ( r 1 ​ ( x, y) + i ​ α 1 ​ x), \displaystyle=|y|^{a}(r_{1}(x,y)^{2}+\alpha_{1}^{2}x^{2})e^{\frac{2\varepsilon_{2}}{\alpha_{1}}\mathrm{arg}(r_{1}(x,y)+i\alpha_{1}x)}, |  |

with r 1 ​ ( x, y) = 2 ​ b ​ y + ( 2 − b) + ε 2 ​ x r_{1}(x,y)=2by+(2-b)+\varepsilon_{2}x and α 1 = 4 ​ b ​ ( 2 − b) − ε 2 2 \alpha_{1}=\sqrt{4b(2-b)-\varepsilon_{2}^{2}}, is a well defined first integral of X μ X_{\mu} outside any ray from { r 1 ​ ( x, y) = 0, x = 0 } = { c ℓ ​ ( μ) } \{r_{1}(x,y)=0,x=0\}=\{c_{\ell}(\mu)\} to infinity. In particular it is continuous at c u ​ ( μ) c_{u}(\mu), so that again it must be a center and μ ∈ U. \mu\in U. This proves the result.

###### Lemma 3.4.

Suppose that F ⁡ ( u 1, u 2, v) F(u_{1},u_{2},v) is a smooth function on a neighbourhood U U of ( 0, 0, v 0) ∈ ℝ 2 × ℝ n (0,0,v_{0})\in\mathbb{R}^{2}\times\mathbb{R}^{n} verifying F = o ⁡ ( ‖ ( u 1, u 2) ‖) F=\mathrm{o}(\|(u_{1},u_{2})\|). Then there exist smooth functions F 1 ​ ( u 1, u 2, v) F_{1}(u_{1},u_{2},v) and F 2 ​ ( u 2, v) F_{2}(u_{2},v) on U U such that F ⁡ ( u 1, u 2, v) = u 1 ​ F 1 ​ ( u 1, u 2, v) + u 2 2 ​ F 2 ​ ( u 2, v) F(u_{1},u_{2},v)=u_{1}F_{1}(u_{1},u_{2},v)+u_{2}^{2}F_{2}(u_{2},v).

The hypothesis implies that F ⁡ ( 0, 0, v) ≡ 0 F(0,0,v)\equiv 0 and ∂ u i F ⁡ ( 0, 0, v) ≡ 0 \partial_{u_{i}}F(0,0,v)\equiv 0. Then

 | F ⁡ ( u 1, u 2, v) \displaystyle F(u_{1},u_{2},v) | = F ⁡ ( u 1, u 2, v) − F ⁡ ( 0, u 2, v) + F ⁡ ( 0, u 2, v) − F ⁡ ( 0, 0, v) \displaystyle=F(u_{1},u_{2},v)-F(0,u_{2},v)+F(0,u_{2},v)-F(0,0,v) |  |

 |  | = u 1 ​ ∫ 0 1 ∂ u 1 F ⁡ ( t ​ u 1, u 2, v) ​ d t ⏟ F 1 ​ ( u 1, u 2, v) + u 2 ​ ∫ 0 1 ∂ u 2 F ⁡ ( 0, t ​ u 2, v) ​ d t ⏟ G ⁡ ( u 2, v) \displaystyle=u_{1}\underbrace{\int_{0}^{1}\partial_{u_{1}}F(tu_{1},u_{2},v)dt}_{F_{1}(u_{1},u_{2},v)}+u_{2}\underbrace{\int_{0}^{1}\partial_{u_{2}}F(0,tu_{2},v)dt}_{G(u_{2},v)} |  |

where F 1 F_{1} and G G are smooth functions on U U. Since G ⁡ ( 0, v) = ∂ u 2 F ⁡ ( 0, 0, v) = 0 G(0,v)=\partial_{u_{2}}F(0,0,v)=0, we also deduce that G ⁡ ( u 2, v) = u 2 ​ F 2 ​ ( u 2, v) G(u_{2},v)=u_{2}F_{2}(u_{2},v) where

 | F 2 ​ ( u 2, v) = ∫ 0 1 ∂ u 2 G ⁡ ( t ​ u 2, v) ​ 𝑑 t F_{2}(u_{2},v)=\int_{0}^{1}\partial_{u_{2}}G(tu_{2},v)dt |  |

is also smooth on U U. Hence we can write F = u 1 ​ F 1 + u 2 2 ​ F 2 F=u_{1}F_{1}+u_{2}^{2}F_{2} and the result follows.

In the statement of our next result, and in what follows, we denote

 | ε ± ​ ( μ) = − ε 2 ∓ 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 ​ and ​ c ± ​ ( μ) = ( a + 1) ± ( 1 − b). \varepsilon_{\pm}(\mu)=-\varepsilon_{2}\mp 2\sqrt{\frac{b(a+2)}{a(b-2)}}\varepsilon_{1}\text{ and }c_{\pm}(\mu)=(a+1)\pm(1-b). |  | (13) |

###### Theorem 3.5.

Given any μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) with a 0 ∈ ( − 2, 0) ∖ { − 1 } a_{0}\in(-2,0)\setminus\{-1\} and b 0 ∈ ( 0, 2), b_{0}\in(0,2), there exist a neighbourhood U U of μ 0 \mu_{0} in ℝ 5 \mathbb{R}^{5} and δ > 0 \delta>0 such that ν = Φ ⁡ ( μ):= ( ε 0, ε +, ε −, c +, c −) \nu=\Phi(\mu)\!:=(\varepsilon_{0},\varepsilon_{+},\varepsilon_{-},c_{+},c_{-}) is a local change of coordinates in U U and we can write

 | 𝒟 u ​ ( s, μ) | μ = Φ − 1 ​ ( ν) = ν 1 ​ g 1 ​ ( s, ν) + ν 2 ​ g 2 ​ ( s, ν) + ν 3 ​ ν 5 ​ g 3 ​ ( s, ν), \left.\mathscr{D}_{u}(s;\mu)\right|_{\mu=\Phi^{-1}(\nu)}=\nu_{1}g_{1}(s;\nu)+\nu_{2}g_{2}(s;\nu)+\nu_{3}\nu_{5}g_{3}(s;\nu), |  | (14) |

where, setting ν 0 = Φ ⁡ ( μ 0) = ( 0, 0, 0, ν 4 0, ν 5 0), \nu_{0}=\Phi(\mu_{0})=(0,0,0,\nu_{4}^{0},\nu_{5}^{0}),

1. ( a) (a)

g 1 ​ ( s, ν) = κ 1 ​ ( ν) + ℱ δ ∞ ​ ( ν 0) g_{1}(s;\nu)=\kappa_{1}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0}),

2. ( b) (b)

g 2 ​ ( s, ν) = s λ ¯ ​ ( ν) ​ ( κ 2 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) g_{2}(s;\nu)=s^{\underline{\lambda}(\nu)}\big(\kappa_{2}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) where λ ¯ ​ ( ν) | ν = Φ ⁡ ( μ) = − a + 2 a, \underline{\lambda}(\nu)|_{\nu=\Phi(\mu)}=-\frac{a+2}{a}, and

3. ( c) (c)

g 3 ​ ( s, ν) = s λ ¯ ′ ​ ( ν) ​ ( κ 3 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) g_{3}(s;\nu)=s^{\underline{\lambda}^{\prime}(\nu)}\big(\kappa_{3}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) where λ ¯ ′ ​ ( ν) = λ ¯ ​ ( ν) + min ⁡ ( λ ¯ ​ ( ν), 1). \underline{\lambda}^{\prime}(\nu)=\underline{\lambda}(\nu)+\min\big(\underline{\lambda}(\nu),1\big).

Moreover κ 1, \kappa_{1}, κ 2 \kappa_{2} and κ 3 \kappa_{3} are smooth strictly positive functions on Φ ⁡ ( U). \Phi(U).

The result is a consequence of Proposition 3.2. Note first that, since ∂ ε 0 δ u ​ ( μ 0) > 0 \partial_{\varepsilon_{0}}\delta_{u}(\mu_{0})>0 and δ u | ε 0 = 0 ≡ 0, \delta_{u}|_{\varepsilon_{0}=0}\equiv 0, we can write δ u = ρ 0 ​ ε 0 \delta_{u}=\rho_{0}\varepsilon_{0} with ρ 0 \rho_{0} a smooth positive function. Thus, setting λ ′ ​ ( μ):= λ ⁡ ( μ) + min ⁡ ( λ ⁡ ( μ), 1), \lambda^{\prime}(\mu)\!:=\lambda(\mu)+\min\big(\lambda(\mu),1\big),

 | α 1:= { − 2 ​ ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) if a < − 1, − 1 if a > − 1, α 2:= { − 1 if a < − 1, − a ⁡ ( b − 1) 2 ​ ( a + 1) ​ b if a > − 1, ​ and ​ ρ 1:= { κ 11 if a > − 1, κ 12 if a < − 1, \alpha_{1}\!:=\left\{\begin{array}[]{ll}-\frac{2(a+2)(b-1)}{(a+1)(b-2)}&\text{if $a<-1$,}\\ -1&\text{if $a>-1$,}\end{array}\right.\quad\alpha_{2}\!:=\left\{\begin{array}[]{ll}-1&\text{if $a<-1$,}\\ -\frac{a(b-1)}{2(a+1)b}&\text{if $a>-1$,}\end{array}\right.\text{ and }\rho_{1}\!:=\left\{\begin{array}[]{ll}\kappa_{11}&\text{if $a>-1$,}\\ \kappa_{12}&\text{if $a<-1$,}\end{array}\right. |  |

we can recap the whole statement of Proposition 3.2 as

 | 𝒟 u ( s; μ) = ε 0 ( ρ 0 + ⋆ s λ + ⋆ s λ ′) + ε + ( κ 01 s λ + ⋆ s λ ′) + ( α 1 ε 1 + α 2 ε 2 + ρ 2) ρ 1 s λ ′ + ℱ L ∞ ( μ 0), \mathscr{D}_{u}(s;\mu)=\varepsilon_{0}(\rho_{0}+\star s^{\lambda}+\star s^{\lambda^{\prime}})+\varepsilon_{+}(\kappa_{01}s^{\lambda}+\star s^{\lambda^{\prime}})+(\alpha_{1}\varepsilon_{1}+\alpha_{2}\varepsilon_{2}+\rho_{2})\rho_{1}s^{\lambda^{\prime}}+\mathcal{F}_{L}^{\infty}(\mu_{0}), |  | (15) |

where ⋆ \star are unspecified smooth functions on μ \mu, ρ 2 = ρ 2 ​ ( a, b, ε 1, ε 2) = o ​ ( ‖ ( ε 1, ε 2) ‖) \rho_{2}=\rho_{2}(a,b,\varepsilon_{1},\varepsilon_{2})=\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) and L = λ ′ ​ ( μ 0) + δ ′ L=\lambda^{\prime}(\mu_{0})+\delta^{\prime} for some δ ′ > 0 \delta^{\prime}>0 small enough. We remark that κ 01, \kappa_{01}, κ 11 \kappa_{11} and κ 21 \kappa_{21} are smooth strictly positive functions given in Proposition 3.2. Thus ρ 1 \rho_{1} is a smooth strictly positive function as well.

On the other hand, from ( 13) (\ref{c_pm}) we get that α 1 ​ ε 1 + α 2 ​ ε 2 = α + ​ ε + + α − ​ ε − \alpha_{1}\varepsilon_{1}+\alpha_{2}\varepsilon_{2}=\alpha_{+}\varepsilon_{+}+\alpha_{-}\varepsilon_{-} with

 | α ±:= 1 2 ​ ( − α 2 ∓ α 1 2 ​ a ⁡ ( b − 2) b ⁡ ( a + 2)) = { 1 2 ​ ( 1 ± ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) ​ a ⁡ ( b − 2) b ⁡ ( a + 2)) if a < − 1, 1 4 ​ ( a ⁡ ( b − 1) ( a + 1) ​ b ± a ⁡ ( b − 2) b ⁡ ( a + 2)) if a > − 1. \alpha_{\pm}\!:=\frac{1}{2}\left(-\alpha_{2}\mp\frac{\alpha_{1}}{2}\sqrt{\frac{a(b-2)}{b(a+2)}}\right)=\left\{\begin{array}[]{ll}\frac{1}{2}\left(1\pm\frac{(a+2)(b-1)}{(a+1)(b-2)}\sqrt{\frac{a(b-2)}{b(a+2)}}\right)&\text{if $a<-1$,}\\[7.0pt] \frac{1}{4}\left(\frac{a(b-1)}{(a+1)b}\pm\sqrt{\frac{a(b-2)}{b(a+2)}}\right)&\text{if $a>-1$.}\end{array}\right. |  | (16) |

Hence, since ν = Φ ⁡ ( a, b, ε 0, ε 1, ε 2):= ( ε 0, ε +, ε −, c +, c −) \nu=\Phi(a,b,\varepsilon_{0},\varepsilon_{1},\varepsilon_{2})\!:=(\varepsilon_{0},\varepsilon_{+},\varepsilon_{-},c_{+},c_{-}) is a smooth change of coordinates in a neighbourhood U U of μ 0 \mu_{0} and ( ρ 2 ∘ Φ − 1) ​ ( ν) = ρ ¯ 2 ​ ( ε +, ε −, c +, c −) = o ​ ( ‖ ( ε +, ε −) ‖) \big(\rho_{2}\circ\Phi^{-1}\big)(\nu)=\underline{\rho}_{2}(\varepsilon_{+},\varepsilon_{-},c_{+},c_{-})=\mbox{\rm o}(\|(\varepsilon_{+},\varepsilon_{-})\|), the application of Lemma 3.4 yields

 | ( α 1 ε 1 + α 2 ε 2 + ρ 2 ( μ)) | μ = Φ − 1 ​ ( ν) = ( α ¯ + + ⋆) ε + + ( α ¯ − + ε − η 1) ε − = ⋆ ε + + ( α ¯ − + ε − η 1) ε − \left.\big(\alpha_{1}\varepsilon_{1}+\alpha_{2}\varepsilon_{2}+\rho_{2}(\mu)\big)\right|_{\mu=\Phi^{-1}(\nu)}=(\underline{\alpha}_{+}+\star)\varepsilon_{+}+(\underline{\alpha}_{-}+\varepsilon_{-}\eta_{1})\varepsilon_{-}=\star\varepsilon_{+}+(\underline{\alpha}_{-}+\varepsilon_{-}\eta_{1})\varepsilon_{-} |  | (17) |

with η 1 = η 1 ​ ( ε −, c +, c −) \eta_{1}=\eta_{1}(\varepsilon_{-},c_{+},c_{-}). Here, and in what follows, for the sake of shortness, given a function h = h ⁡ ( μ) h=h(\mu) we denote h ¯ = h ¯ ​ ( ν) = h ⁡ ( μ) | μ = Φ − 1 ​ ( ν). \underline{h}=\underline{h}(\nu)=h(\mu)|_{\mu=\Phi^{-1}(\nu)}. Following this convention, from ( 15) (\ref{diveq0}) and ( 17) (\ref{diveq1}) we get

 | 𝒟 u ( s; μ) | μ = Φ − 1 ​ ( ν) = ε 0 ( ρ ¯ 0 + ⋆ s λ ¯ + ⋆ s λ ¯ ′) + ε + ( κ ¯ 01 s λ ¯ + ⋆ s λ ¯ ′) + ε − ( α ¯ − + ε − η 1) ρ ¯ 1 s λ ¯ ′ + r ( s; ν), \mathscr{D}_{u}(s;\mu)|_{\mu=\Phi^{-1}(\nu)}=\varepsilon_{0}(\underline{\rho}_{0}+\star s^{\underline{\lambda}}+\star s^{\underline{\lambda}^{\prime}})+\varepsilon_{+}(\underline{\kappa}_{01}s^{\underline{\lambda}}+\star s^{\underline{\lambda}^{\prime}})+\varepsilon_{-}(\underline{\alpha}_{-}+\varepsilon_{-}\eta_{1})\underline{\rho}_{1}s^{\underline{\lambda}^{\prime}}+r(s;\nu), |  |

where, setting ν 0:= Φ ⁡ ( μ 0) \nu_{0}\!:=\Phi(\mu_{0}) and applying assertion ( h) (h) in Lemma A.7, r ∈ ℱ L ∞ ​ ( ν 0) r\in\mathcal{F}_{L}^{\infty}(\nu_{0}). Note that, by Lemma 3.3, if μ ∈ Z 0 = { ε 0 = ε 1 = ε 2 = 0 } \mu\in Z_{0}=\{\varepsilon_{0}=\varepsilon_{1}=\varepsilon_{2}=0\} then 𝒟 u ​ ( s, μ) ≡ 0. \mathscr{D}_{u}(s;\mu)\equiv 0. Thus, since Φ ( Z 0) = { ε 0 = ε + = ε − = 0 } \Phi(Z_{0})=\{\varepsilon_{0}=\varepsilon_{+}=\varepsilon_{-}=0\}, we get that r ⁡ ( s, ν) | ε 0 = ε + = ε − = 0 ≡ 0 r(s;\nu)|_{\varepsilon_{0}=\varepsilon_{+}=\varepsilon_{-}=0}\equiv 0. By applying Lemma A.10 this implies that the remainder can be written as r = ε 0 ​ r 0 + ε + ​ r 1 + ε − ​ r 2 r=\varepsilon_{0}r_{0}+\varepsilon_{+}r_{1}+\varepsilon_{-}r_{2} with r i ∈ ℱ L ∞ ​ ( ν 0). r_{i}\in\mathcal{F}_{L}^{\infty}(\nu_{0}). Consequently

 | 𝒟 u ( s; Φ − 1 ( ν)) = ε 0 ( ρ ¯ 0 + ⋆ s λ ¯ + ⋆ s λ ¯ ′ + r 0 ( s; ν)) + ε + ( κ ¯ 01 s λ ¯ + ⋆ s λ ¯ ′ + r 1 ( s; ν)) + ε − ( ( α ¯ − + ε − η 1) ρ ¯ 1 s λ ¯ ′ + r 2 ( s; ν)). \mathscr{D}_{u}(s;\Phi^{-1}(\nu))=\varepsilon_{0}\big(\underline{\rho}_{0}+\star s^{\underline{\lambda}}+\star s^{\underline{\lambda}^{\prime}}+r_{0}(s;\nu)\big)+\varepsilon_{+}\big(\underline{\kappa}_{01}s^{\underline{\lambda}}+\star s^{\underline{\lambda}^{\prime}}+r_{1}(s;\nu)\big)+\varepsilon_{-}\big((\underline{\alpha}_{-}+\varepsilon_{-}\eta_{1})\underline{\rho}_{1}s^{\underline{\lambda}^{\prime}}+r_{2}(s;\nu)\big). |  |

Furthermore, by Lemma 3.3 again, if μ ∈ Z 1 = { a + b = ε 0 = 2 ε 1 + ε 2 = 0 } \mu\in Z_{1}=\{a+b=\varepsilon_{0}=2\varepsilon_{1}+\varepsilon_{2}=0\} then 𝒟 u ​ ( s, μ) ≡ 0. \mathscr{D}_{u}(s;\mu)\equiv 0. Thus, since one can easily check that Φ ( Z 1) = { ε 0 = ε + = c − = 0 } \Phi(Z_{1})=\{\varepsilon_{0}=\varepsilon_{+}=c_{-}=0\}, we can assert that

 | ( α ¯ − + ε − ​ η 1) ​ ρ ¯ 1 ​ s λ ¯ ′ + r 2 ​ ( s, ν) | ε 0 = ε + = c − = 0 ≡ 0. \left.(\underline{\alpha}_{-}+\varepsilon_{-}\eta_{1})\underline{\rho}_{1}s^{\underline{\lambda}^{\prime}}+r_{2}(s;\nu)\right|_{\varepsilon_{0}=\varepsilon_{+}=c_{-}=0}\equiv 0. |  |

Since ρ 1 ​ ( μ 0) > 0 \rho_{1}(\mu_{0})>0 and one can verify using ( 16) (\ref{diveq3}) that α ¯ − = c − ​ η 2 \underline{\alpha}_{-}=c_{-}\eta_{2} with η 2 ​ ( ν 0) > 0 \eta_{2}(\nu_{0})>0, the above identity implies η 1 ​ ( ε −, c +, c −) | c − = 0 ≡ 0 \eta_{1}(\varepsilon_{-},c_{+},c_{-})|_{c_{-}=0}\equiv 0 and r 2 ​ ( s, ν) | ε 0 = ε + = c − = 0 ≡ 0. r_{2}(s;\nu)|_{\varepsilon_{0}=\varepsilon_{+}=c_{-}=0}\equiv 0. Accordingly η 1 ​ ( ε −, c +, c −) = c − ​ η 3 ​ ( ε −, c +, c −) \eta_{1}(\varepsilon_{-},c_{+},c_{-})=c_{-}\eta_{3}(\varepsilon_{-},c_{+},c_{-}) and, by Lemma A.10 once again, r 2 = ε 0 ​ r 3 + ε + ​ r 4 + c − ​ r 5 r_{2}=\varepsilon_{0}r_{3}+\varepsilon_{+}r_{4}+c_{-}r_{5} with r i ∈ ℱ L ∞ ​ ( ν 0). r_{i}\in\mathcal{F}_{L}^{\infty}(\nu_{0}). Consequently

 | 𝒟 u ( s; Φ − 1 ( ν)) = ε 0 ( ρ ¯ 0 + ⋆ s λ ¯ + ⋆ s λ ¯ ′ + r ¯ 0 ( s; ν)) + ε + ( κ ¯ 01 s λ ¯ + ⋆ s λ ¯ ′ + r ¯ 1 ( s; ν)) + c − ε − ( η 4 s λ ¯ ′ + r 5 ( s; ν)). \mathscr{D}_{u}(s;\Phi^{-1}(\nu))=\varepsilon_{0}\big(\underline{\rho}_{0}+\star s^{\underline{\lambda}}+\star s^{\underline{\lambda}^{\prime}}+\bar{r}_{0}(s;\nu)\big)+\varepsilon_{+}\big(\underline{\kappa}_{01}s^{\underline{\lambda}}+\star s^{\underline{\lambda}^{\prime}}+\bar{r}_{1}(s;\nu)\big)+c_{-}\varepsilon_{-}\big(\eta_{4}s^{\underline{\lambda}^{\prime}}+r_{5}(s;\nu)\big). |  |

where the new remainders r ¯ 0 = r 0 + r 3 \bar{r}_{0}=r_{0}+r_{3} and r ¯ 1 = r 1 + r 4 \bar{r}_{1}=r_{1}+r_{4} also belong to ℱ L ​ ( ν 0) \mathcal{F}_{L}(\nu_{0}) and η 4:= ( η 2 + ε − ​ η 3) ​ ρ ¯ 1 \eta_{4}\!:=(\eta_{2}+\varepsilon_{-}\eta_{3})\underline{\rho}_{1} satisfies η 4 ​ ( ν 0) = ( η 2 ​ ρ ¯ 1) ​ ( ν 0) > 0. \eta_{4}(\nu_{0})=(\eta_{2}\underline{\rho}_{1})(\nu_{0})>0. By applying Lemma A.7 we can take δ > 0 \delta>0 small enough in order that the functions s λ ¯ s^{\underline{\lambda}}, s λ ¯ ′ s^{\underline{\lambda}^{\prime}}, s λ ¯ ′ − λ ¯ s^{\underline{\lambda}^{\prime}-\underline{\lambda}}, s − λ ¯ ​ r ¯ 1 s^{-\underline{\lambda}}\bar{r}_{1} and s − λ ¯ ′ ​ r 5 s^{-\underline{\lambda}^{\prime}}r_{5} belong to ℱ δ ​ ( ν 0) \mathcal{F}_{\delta}(\nu_{0}). In doing so we obtain

 | 𝒟 u ​ ( s, Φ − 1 ​ ( ν)) = ε 0 ​ ( ρ ¯ 0 + ℱ δ ​ ( ν 0)) + ε + ​ s λ ¯ ​ ( κ ¯ 01 + ℱ δ ​ ( ν 0)) + c − ​ ε − ​ s λ ¯ ′ ​ ( η 4 + ℱ δ ​ ( ν 0)). \mathscr{D}_{u}(s;\Phi^{-1}(\nu))=\varepsilon_{0}\big(\underline{\rho}_{0}+\mathcal{F}_{\delta}(\nu_{0})\big)+\varepsilon_{+}s^{\underline{\lambda}}\big(\underline{\kappa}_{01}+\mathcal{F}_{\delta}(\nu_{0})\big)+c_{-}\varepsilon_{-}s^{\underline{\lambda}^{\prime}}\big(\eta_{4}+\mathcal{F}_{\delta}(\nu_{0})\big). |  |

Since ν = ( ε 0, ε +, ε −, c +, c −) \nu=(\varepsilon_{0},\varepsilon_{+},\varepsilon_{-},c_{+},c_{-}), from this expression we obtain ( 14) (\ref{thmdiv}) by renaming the unit functions. This completes the proof.

We prove first the assertion with regard to the hemicycle Γ u \Gamma_{u}. By Lemma 3.1 it suffices to consider the quadratic 5-parameter perturbation given in ( 12) (\ref{pert}). We set μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) and note that the limit cycles of X μ X_{\mu} that are close to Γ u \Gamma_{u} in Hausdorff sense are in one to one correspondence with the isolated positive zeroes of

 | 𝒟 u ​ ( s, μ) = D + u ​ ( s, μ) − D − u ​ ( s, μ), \mathscr{D}_{u}(s;\mu)=D^{u}_{+}(s;\mu)-D^{u}_{-}(s;\mu), |  |

see Figure 7. That being said, by applying Theorem 3.5 we know that there exist a neighbourhood U U of μ 0 \mu_{0} and δ > 0 \delta>0 small enough such that ν:= Φ ⁡ ( μ) = ( ε 0, ε +, ε −, c +, c −) \nu\!:=\Phi(\mu)=(\varepsilon_{0},\varepsilon_{+},\varepsilon_{-},c_{+},c_{-}) is a local change of coordinates in U U and

 | 𝒟 u ​ ( s, μ) | μ = Φ − 1 ​ ( ν) = ν 1 ​ ( κ 1 + ℱ δ ∞ ​ ( ν 0)) + ν 2 ​ s λ ¯ ​ ( ν) ​ ( κ 2 + ℱ δ ∞ ​ ( ν 0)) + ν 3 ​ ν 5 ​ s λ ¯ ′ ​ ( ν) ​ ( κ 3 + ℱ δ ∞ ​ ( ν 0)), \left.\mathscr{D}_{u}(s;\mu)\right|_{\mu=\Phi^{-1}(\nu)}=\nu_{1}\big(\kappa_{1}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)+\nu_{2}s^{\underline{\lambda}(\nu)}\big(\kappa_{2}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)+\nu_{3}\nu_{5}s^{\underline{\lambda}^{\prime}(\nu)}\big(\kappa_{3}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big), |  | (18) |

where ν 0 = Φ ⁡ ( μ 0) \nu_{0}=\Phi(\mu_{0}), κ i ​ ( ν 0) > 0 \kappa_{i}(\nu_{0})>0 and λ ¯ ′ = λ ¯ + min ⁡ ( λ ¯, 1). \underline{\lambda}^{\prime}=\underline{\lambda}+\min(\underline{\lambda},1).

Recall on the other hand, see Lemma 3.3, that 𝒟 u ​ ( s, μ) ≡ 0 \mathscr{D}_{u}(s;\mu)\equiv 0 if, and only if, μ ∈ Z 0 ∪ Z 1 \mu\in Z_{0}\cup Z_{1} where

 | Z 0 = { ε 0 = ε 1 = ε 2 = 0 } and Z 1 = { a + b = ε 0 = 2 ε 1 + ε 2 = 0 }. Z_{0}=\{\varepsilon_{0}=\varepsilon_{1}=\varepsilon_{2}=0\}\text{ and }Z_{1}=\{a+b=\varepsilon_{0}=2\varepsilon_{1}+\varepsilon_{2}=0\}. |  |

One can check in this respect that Φ ( Z 0 ∪ Z 1) = { ν 1 = ν 2 = ν 3 ν 5 = 0 }. \Phi(Z_{0}\cup Z_{1})=\{\nu_{1}=\nu_{2}=\nu_{3}\nu_{5}=0\}. Taking this into account, and the fact that Φ ⁡ ( μ 0) = ν 0, \Phi(\mu_{0})=\nu_{0}, we claim that there exist s 0 > 0 s_{0}>0 and an open ball B r ​ ( ν 0) B_{r}(\nu_{0}) of radius r > 0 r>0 centered ν 0 \nu_{0} such that ( 18) (\ref{proBeq1}) has at most two zeros on ( 0, s 0) (0,s_{0}), counted with multiplicities, for all ν \nu inside V:= B r ( ν 0) ∩ { ν 1 2 + ν 2 2 + ( ν 3 ν 5) 2 ≠ 0 }. V\!:=B_{r}(\nu_{0})\cap\{\nu_{1}^{2}+\nu_{2}^{2}+(\nu_{3}\nu_{5})^{2}\neq 0\}. This will imply, see Definition 2, that

 | Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩽ 𝒵 0 ​ ( 𝒟 u ​ ( ⋅, μ), μ 0) = 𝒵 0 ​ ( 𝒟 u ​ ( ⋅, Φ − 1 ​ ( ν)), ν 0) ⩽ 2. \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\leqslant\mathcal{Z}_{0}\big(\mathscr{D}_{u}(\,\cdot\,;\mu),\mu_{0}\big)=\mathcal{Z}_{0}\big(\mathscr{D}_{u}(\,\cdot\,;\Phi^{-1}(\nu)),\nu_{0}\big)\leqslant 2. |  |

In order to prove the claim we note first that, due to lim s → 0 ( κ 1 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) = κ 1 ​ ( ν) ≠ 0 \lim_{s\to 0}\big(\kappa_{1}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)=\kappa_{1}(\nu)\neq 0 uniformly for ν ≈ ν 0 \nu\approx\nu_{0}, we can take r > 0 r>0 and s 0 > 0 s_{0}>0 small enough such that

 | ℛ 0 ​ ( s, ν):= 𝒟 u ​ ( s, μ) | μ = Φ − 1 ​ ( ν) κ 1 + ℱ δ ∞ ​ ( ν 0) = ν 1 + ν 2 ​ s λ ¯ ​ ( ν) ​ ( κ 4 + ℱ δ ∞ ​ ( ν 0)) + ν 3 ​ ν 5 ​ s λ ¯ ′ ​ ( ν) ​ ( κ 5 + ℱ δ ∞ ​ ( ν 0)) \mathscr{R}_{0}(s;\nu)\!:=\frac{\left.\mathscr{D}_{u}(s;\mu)\right|_{\mu=\Phi^{-1}(\nu)}}{\kappa_{1}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})}=\nu_{1}+\nu_{2}s^{\underline{\lambda}(\nu)}\big(\kappa_{4}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)+\nu_{3}\nu_{5}s^{\underline{\lambda}^{\prime}(\nu)}\big(\kappa_{5}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) |  |

is well defined for all s ∈ ( 0, s 0) s\in(0,s_{0}) and ν ∈ B r ​ ( ν 0) \nu\in B_{r}(\nu_{0}) and has exactly the same number of zeros, counted with multiplicities, as 𝒟 u ​ ( s, Φ − 1 ​ ( ν)) \mathscr{D}_{u}(s;\Phi^{-1}(\nu)). Accordingly 𝒵 0 ​ ( ℛ 0 ​ ( ⋅, ν), ν 0) = 𝒵 0 ​ ( 𝒟 u ​ ( ⋅, μ), μ 0). \mathcal{Z}_{0}\big(\mathscr{R}_{0}(\,\cdot\,;\nu),\nu_{0}\big)=\mathcal{Z}_{0}\big(\mathscr{D}_{u}(\,\cdot\,;\mu),\mu_{0}\big). We note that the second equality above follows from ( 18) (\ref{proBeq1}) by applying Lemma A.7 and that κ 4:= κ 2 / κ 1 \kappa_{4}\!:=\kappa_{2}/\kappa_{1} and κ 5: κ 3 / κ 1 \kappa_{5}\!:\kappa_{3}/\kappa_{1} are strictly positive smooth functions. If ν ∈ V \nu\in V verifies ν 2 = ν 3 ​ ν 5 = 0 \nu_{2}=\nu_{3}\nu_{5}=0 then ν 1 ≠ 0 \nu_{1}\neq 0 and, consequently, ℛ 0 ​ ( s, ν) ≠ 0 \mathscr{R}_{0}(s;\nu)\neq 0. This remark shows the validity of the claim for all ν ∈ V \nu\in V such that ν 2 = ν 3 ​ ν 5 = 0 \nu_{2}=\nu_{3}\nu_{5}=0. To study the other cases we apply the so-called derivation-division algorithm. To this end we first observe that, by Lemma A.7 again,

 |  | ∂ s ℛ 0 ​ ( s, ν) = ν 2 ​ s λ ¯ − 1 ​ ( λ ¯ ​ κ 4 + ℱ δ ∞ ​ ( ν 0)) + ν 3 ​ ν 5 ​ s λ ¯ ′ − 1 ​ ( λ ¯ ′ ​ κ 5 + ℱ δ ∞ ​ ( ν 0)) \displaystyle\partial_{s}\mathscr{R}_{0}(s;\nu)=\nu_{2}s^{\underline{\lambda}-1}\big(\underline{\lambda}\kappa_{4}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)+\nu_{3}\nu_{5}s^{\underline{\lambda}^{\prime}-1}\big(\underline{\lambda}^{\prime}\kappa_{5}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) |  |

and |

 |  | ℛ 1 ​ ( s, ν):= ∂ s ℛ 0 ​ ( s, ν) s λ ¯ − 1 ​ ( λ ¯ ​ κ 4 + ℱ δ ∞ ​ ( ν 0)) = ν 2 + ν 3 ​ ν 5 ​ s λ ¯ ′ − λ ¯ ​ ( κ 6 + ℱ δ ∞ ​ ( ν 0)), \displaystyle\mathscr{R}_{1}(s;\nu)\!:=\frac{\partial_{s}\mathscr{R}_{0}(s;\nu)}{s^{\underline{\lambda}-1}\big(\underline{\lambda}\kappa_{4}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)}=\nu_{2}+\nu_{3}\nu_{5}s^{\underline{\lambda}^{\prime}-\underline{\lambda}}\big(\kappa_{6}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big), |  |

where κ 6 ​ ( ν 0) > 0 \kappa_{6}(\nu_{0})>0. Note that lim s → 0 + ( λ ¯ ​ κ 4 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) = λ ¯ ​ κ 4 ​ ( ν) ≠ 0 \lim_{s\to 0^{+}}\big(\underline{\lambda}\kappa_{4}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)=\underline{\lambda}\kappa_{4}(\nu)\neq 0 uniformly for ν ≈ ν 0. \nu\approx\nu_{0}. Therefore, by reducing r > 0 r>0 and s 0 > 0 s_{0}>0 if necessary, ℛ 1 ​ ( s, ν) \mathscr{R}_{1}(s;\nu) is well defined for all s ∈ ( 0, s 0) s\in(0,s_{0}) and ν ∈ B r ​ ( ν 0) \nu\in B_{r}(\nu_{0}) and has exactly the same number of zeros, counted with multiplicities, as ∂ s ℛ 0 ​ ( s, ν) \partial_{s}\mathscr{R}_{0}(s;\nu). If ν ∈ V \nu\in V verifies ν 3 ​ ν 5 = 0 \nu_{3}\nu_{5}=0 then we can suppose that ν 2 ≠ 0 \nu_{2}\neq 0 (otherwise we end up in the previous case) and, consequently, ℛ 1 ​ ( s, ν) ≠ 0 \mathscr{R}_{1}(s;\nu)\neq 0. Hence, by applying Rolle’s Theorem, the claim follows in this case. So far we have proved the validity of the claim for all ν ∈ V \nu\in V such that ν 3 ​ ν 5 = 0. \nu_{3}\nu_{5}=0. To study the case ν 3 ​ ν 5 ≠ 0 \nu_{3}\nu_{5}\neq 0 we apply Lemma A.7 once again to obtain

 | ℛ 2 ​ ( s, ν):= ∂ s ℛ 1 ​ ( s, ν) = ν 3 ​ ν 5 ​ s λ ¯ ′ − λ ¯ − 1 ​ ( κ 7 + ℱ δ ∞ ​ ( ν 0)) \mathscr{R}_{2}(s;\nu)\!:=\partial_{s}\mathscr{R}_{1}(s;\nu)=\nu_{3}\nu_{5}s^{\underline{\lambda}^{\prime}-\underline{\lambda}-1}\big(\kappa_{7}+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) |  |

with κ 5 = ( λ ¯ ′ − λ ¯) ​ κ 6 ≠ 0 \kappa_{5}=(\underline{\lambda}^{\prime}-\underline{\lambda})\kappa_{6}\neq 0 for ν ≈ ν 0. \nu\approx\nu_{0}. Exactly as before, by reducing r > 0 r>0 and s 0 > 0 s_{0}>0 if necessary, we have that κ 7 ​ ( ν) + ℱ δ ∞ ​ ( ν 0) ≠ 0 \kappa_{7}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\neq 0 for all ν ∈ B r ​ ( ν 0) \nu\in B_{r}(\nu_{0}) and s ∈ ( 0, s 0). s\in(0,s_{0}). Therefore ℛ 2 ​ ( s, ν) ≠ 0 \mathscr{R}_{2}(s;\nu)\neq 0 for all ν ∈ V \nu\in V with ν 3 ​ ν 5 ≠ 0 \nu_{3}\nu_{5}\neq 0 and s ∈ ( 0, s 0) s\in(0,s_{0}) and the claim follows in this case by applying twice Rolle’s Theorem. This exhausts all the possible cases for ν ∈ V \nu\in V and completes the proof of the claim. Accordingly Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩽ 2 \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\leqslant 2.

The fact that Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 2 \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 2 is also a consequence of ( 18) (\ref{proBeq1}). Indeed, by applying Proposition A.12 we can take a sequence lim n → ∞ ν ^ n = ν 0 \lim_{n\to\infty}\hat{\nu}_{n}=\nu_{0} with ν ^ n ∈ Φ ( U) ∩ { ν 1 = ν 2 = 0 and ν 3 ν 5 ≠ 0 } \hat{\nu}_{n}\in\Phi(U)\cap\{\nu_{1}=\nu_{2}=0\text{ and }\nu_{3}\nu_{5}\neq 0\} such that, setting μ ^ n:= Φ − 1 ​ ( ν ^ n) \hat{\mu}_{n}\!:=\Phi^{-1}(\hat{\nu}_{n}), we have Cycl ⁡ ( ( Γ u, X μ ^ n), X μ) ⩾ 2 \mathrm{Cycl}\big((\Gamma_{u},X_{\hat{\mu}_{n}}),X_{\mu}\big)\geqslant 2 for all n ∈ ℕ. n\in\mathbb{N}. Since lim n → ∞ μ ^ n = μ 0 \lim_{n\to\infty}\hat{\mu}_{n}=\mu_{0} this clearly implies that Cycl ⁡ ( ( Γ u, X μ 0), X μ) ⩾ 2 \mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big)\geqslant 2, as desired.

So far we have proved that the cyclicity of Γ u \Gamma_{u} when we perturb ( 7) (\ref{DSq}) inside the whole family of quadratic differential systems is exactly 2. In order to show this for Γ ℓ \Gamma_{\ell} we use an orbital symmetry that preserves the two-parameter family ( 7) (\ref{DSq}) and interchanges Γ ℓ \Gamma_{\ell} with Γ u \Gamma_{u}. More concretely, we take ϕ ⁡ ( x, y) = ( η ​ x, − η 2 ​ y) \phi(x,y)=(\eta x,-\eta^{2}y) with η:= b 0 2 − b 0 \eta\!:=\sqrt{\frac{b_{0}}{2-b_{0}}}. Then one can verify that the coordinate change ( x ¯, y ¯) = ϕ ⁡ ( x, y) (\bar{x},\bar{y})=\phi(x,y), together with the time reparametrization t ¯ = η − 1 ​ t \bar{t}=\eta^{-1}t, induce the parameter change ( a ¯ 0, b ¯ 0) = ( a 0, 2 − b 0) (\bar{a}_{0},\bar{b}_{0})=(a_{0},2-b_{0}) in the family ( 7) (\ref{DSq}). Due to ϕ ⁡ ( Γ ℓ) = Γ u \phi(\Gamma_{\ell})=\Gamma_{u}, the result follows because we have already proved its validity for Γ u \Gamma_{u}. This completes the proof of the result.

## 4 Proof of Theorem C

###### Lemma 4.1.

For each b ∈ ( 0, 2) b\in(0,2), define the linear map ϕ ⁡ ( x, y) = ( η b ​ x, − η b 2 ​ y) \phi(x,y)=(\eta_{b}x,-\eta_{b}^{2}y) with η b:= b 2 − b \eta_{b}\!:=\sqrt{\frac{b}{2-b}} and consider the vector field X μ X_{\mu} in ( 12) (\ref{pert}). Then ϕ ⋆ ​ ( X μ) = η b − 1 ​ X σ ⁡ ( μ) \phi_{\star}(X_{\mu})=\eta_{b}^{-1}X_{\sigma(\mu)} with σ ( a, b, ε 0, ε 1, ε 2) = ( a, 2 − b, − η b 3 ε 0, η b ε 1, − ε 2 / η b) \sigma(a,b,\varepsilon_{0},\varepsilon_{1},\varepsilon_{2})=(a,2-b,-\eta_{b}^{3}\varepsilon_{0},\eta_{b}\varepsilon_{1},-\varepsilon_{2}/\eta_{b}).

This follows by an easy computation and it is left to the reader.

Figure 8: Dulac maps D ± ℓ D^{\ell}_{\pm} to define 𝒟 ℓ ​ ( s, μ) = D + ℓ ​ ( s, μ) − D − ℓ ​ ( s, μ) \mathscr{D}_{\ell}(s;\mu)=D^{\ell}_{+}(s;\mu)-D^{\ell}_{-}(s;\mu). The points in red are ( 0, D ± ℓ ​ ( s)) (0,D^{\ell}_{\pm}(s)) and ( 0, − 1 / s) (0,-1/s).

The previous result will enable us to study the limit cycles bifurcating from Γ ℓ \Gamma_{\ell} by taking advantage of Theorem 3.5, which is addressed to the ones bifurcating from Γ u \Gamma_{u}. To this end we take two transverse sections on x = 0 x=0, Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2}, parametrized by s ↦ ( 0, − 1 / s) s\mapsto(0,-1/s) with s ∈ ( 0, δ) s\in(0,\delta) and s ↦ ( 0, s) s\mapsto(0,s) with s ∈ ( − δ, δ) s\in(-\delta,\delta), respectively. Then, see Figure 8, we consider the Dulac map D + ℓ ​ ( ⋅, μ) D^{\ell}_{+}(\,\cdot\,;\mu) for X μ X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} and the Dulac map D − ℓ ​ ( ⋅, μ) D^{\ell}_{-}(\,\cdot\,;\mu) for − X μ -X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} and define

 | 𝒟 ℓ ​ ( s, μ):= D + ℓ ​ ( s, μ) − D − ℓ ​ ( s, μ). \mathscr{D}_{\ell}(s;\mu)\!:=D^{\ell}_{+}(s;\mu)-D^{\ell}_{-}(s;\mu). |  |

We remark that, according to the parametrization of Σ 1 \Sigma_{1}, the function 𝒟 ℓ ​ ( s, μ) \mathscr{D}_{\ell}(s;\mu) is defined for positive s. s. Taking these definitions into account we now prove the following result. With regard to its statement we stress that the change of parameters ν = Φ ⁡ ( μ) \nu=\Phi(\mu) is the same as the one given in Theorem 3.5, cf. ( 13) (\ref{c_pm}).

###### Corollary 4.2.

Given any μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) with a 0 ∈ ( − 2, 0) ∖ { − 1 } a_{0}\in(-2,0)\setminus\{-1\} and b 0 ∈ ( 0, 2), b_{0}\in(0,2), there exist a neighbourhood U U of μ 0 \mu_{0} in ℝ 5 \mathbb{R}^{5} and δ > 0 \delta>0 such ν = Φ ⁡ ( μ):= ( ε 0, ε +, ε −, c +, c −) \nu=\Phi(\mu)\!:=(\varepsilon_{0},\varepsilon_{+},\varepsilon_{-},c_{+},c_{-}) is a local change of coordinates in U U and we can write

 | 𝒟 ℓ ​ ( s, μ) | μ = Φ − 1 ​ ( ν) = ν 1 ​ g ^ 1 ​ ( s, ν) + ν 3 ​ g ^ 2 ​ ( s, ν) + ν 2 ​ ν 4 ​ g ^ 3 ​ ( s, ν), \left.\mathscr{D}_{\ell}(s;\mu)\right|_{\mu=\Phi^{-1}(\nu)}=\nu_{1}\hat{g}_{1}(s;\nu)+\nu_{3}\hat{g}_{2}(s;\nu)+\nu_{2}\nu_{4}\hat{g}_{3}(s;\nu), |  |

where, setting ν 0 = Φ ⁡ ( μ 0) = ( 0, 0, 0, ν 4 0, ν 5 0), \nu_{0}=\Phi(\mu_{0})=(0,0,0,\nu_{4}^{0},\nu_{5}^{0}),

1. ( a) (a)

g ^ 1 ​ ( s, ν) = κ ^ 1 ​ ( ν) + ℱ δ ∞ ​ ( ν 0) \hat{g}_{1}(s;\nu)=\hat{\kappa}_{1}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0}),

2. ( b) (b)

g ^ 2 ​ ( s, ν) = s λ ¯ ​ ( ν) ​ ( κ ^ 2 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) \hat{g}_{2}(s;\nu)=s^{\underline{\lambda}(\nu)}\big(\hat{\kappa}_{2}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) where λ ¯ ​ ( ν) | ν = Φ ⁡ ( μ) = − a + 2 a, \underline{\lambda}(\nu)|_{\nu=\Phi(\mu)}=-\frac{a+2}{a}, and

3. ( c) (c)

g ^ 3 ​ ( s, ν) = s λ ¯ ′ ​ ( ν) ​ ( κ ^ 3 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) \hat{g}_{3}(s;\nu)=s^{\underline{\lambda}^{\prime}(\nu)}\big(\hat{\kappa}_{3}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) where λ ¯ ′ ​ ( ν) = λ ¯ ​ ( ν) + min ⁡ ( λ ¯ ​ ( ν), 1). \underline{\lambda}^{\prime}(\nu)=\underline{\lambda}(\nu)+\min\big(\underline{\lambda}(\nu),1\big).

Moreover κ ^ 1, \hat{\kappa}_{1}, κ ^ 2 \hat{\kappa}_{2} and κ ^ 3 \hat{\kappa}_{3} are smooth strictly positive functions on Φ ⁡ ( U). \Phi(U).

By applying Lemma 4.1 (and following the notation given in its statement) one can easily show that D ± ℓ ​ ( s, μ) = − η b − 2 ​ D ± u ​ ( η b − 2 ​ s, σ ⁡ ( μ)). D_{\pm}^{\ell}(s;\mu)=-\eta_{b}^{-2}D_{\pm}^{u}\big(\eta_{b}^{-2}s;\sigma(\mu)\big). Thus 𝒟 ℓ ​ ( s, μ) = − η b − 2 ​ 𝒟 u ​ ( η b − 2 ​ s, σ ⁡ ( μ)) \mathscr{D}_{\ell}(s;\mu)=-\eta_{b}^{-2}\mathscr{D}_{u}\big(\eta_{b}^{-2}s;\sigma(\mu)\big) and, consequently,

 | 𝒟 ℓ ​ ( s, μ) | μ = Φ − 1 ​ ( ν) \displaystyle\mathscr{D}_{\ell}(s;\mu)|_{\mu=\Phi^{-1}(\nu)} | = − η b − 2 ​ 𝒟 u ​ ( η b − 2 ​ s, σ ⁡ ( μ)) | μ = Φ − 1 ​ ( ν) \displaystyle=-\left.\eta_{b}^{-2}\mathscr{D}_{u}\big(\eta_{b}^{-2}s;\sigma(\mu)\big)\right|_{\mu=\Phi^{-1}(\nu)} |  |

 |  | = − η ^ ν − 2 ​ 𝒟 u ​ ( η ^ ν − 2 ​ s, σ ⁡ ( Φ − 1 ​ ( ν))) \displaystyle=-\hat{\eta}_{\nu}^{-2}\mathscr{D}_{u}\big(\hat{\eta}_{\nu}^{-2}s;\sigma(\Phi^{-1}(\nu))\big) |  |

 |  | = − η ^ ν − 2 ​ 𝒟 u ​ ( η ^ ν − 2 ​ s, μ) | μ = Φ − 1 ​ ( σ ^ ​ ( ν)) \displaystyle=-\hat{\eta}_{\nu}^{-2}\mathscr{D}_{u}\big(\hat{\eta}_{\nu}^{-2}s;\mu\big)|_{\mu=\Phi^{-1}(\hat{\sigma}(\nu))} |  |

where in the second equality we set η ^ ν:= η b | μ = Φ − 1 ​ ( ν) = 2 − ν 4 + ν 5 2 + ν 4 − ν 5 \hat{\eta}_{\nu}\!:=\eta_{b}|_{\mu=\Phi^{-1}(\nu)}=\sqrt{\frac{2-\nu_{4}+\nu_{5}}{2+\nu_{4}-\nu_{5}}} and in the third one σ ^:= Φ ∘ σ ∘ Φ − 1. \hat{\sigma}\!:=\Phi\circ\sigma\circ\Phi^{-1}. Some computations show that

 | σ ^ ( ν) = ( − η ^ ν 3 ν 1, − ν 3 / η ^ ν, − ν 2 / η ^ ν, ν 5, ν 4). \hat{\sigma}(\nu)=(-\hat{\eta}_{\nu}^{3}\nu_{1},-\nu_{3}/\hat{\eta}_{\nu},-\nu_{2}/\hat{\eta}_{\nu},\nu_{5},\nu_{4}). |  |

Therefore, from the equality ( 14) (\ref{thmdiv}) in Theorem 3.5, we obtain that

 | 𝒟 ℓ ​ ( s, μ) | μ = Φ − 1 ​ ( ν) \displaystyle\mathscr{D}_{\ell}(s;\mu)|_{\mu=\Phi^{-1}(\nu)} | = − η ^ ν − 2 ​ 𝒟 u ​ ( η ^ ν − 2 ​ s, μ) | μ = Φ − 1 ​ ( σ ^ ​ ( ν)) \displaystyle=-\hat{\eta}_{\nu}^{-2}\mathscr{D}_{u}\big(\hat{\eta}_{\nu}^{-2}s;\mu\big)|_{\mu=\Phi^{-1}(\hat{\sigma}(\nu))} |  |

 |  | = η ^ ν − 2 ​ ( η ^ ν 3 ​ ν 1 ​ g 1 ​ ( η ^ ν − 2 ​ s, σ ^ ​ ( ν)) + ν 3 / η ^ ν ​ g 2 ​ ( η ^ ν − 2 ​ s, σ ^ ​ ( ν)) + ν 2 ​ ν 4 / η ^ ν ​ g 3 ​ ( η ^ ν − 2 ​ s, σ ^ ​ ( ν))), \displaystyle=\hat{\eta}_{\nu}^{-2}\Big(\hat{\eta}_{\nu}^{3}\nu_{1}g_{1}\big(\hat{\eta}_{\nu}^{-2}s;\hat{\sigma}(\nu)\big)+\nu_{3}/\hat{\eta}_{\nu}g_{2}\big(\hat{\eta}_{\nu}^{-2}s;\hat{\sigma}(\nu)\big)+\nu_{2}\nu_{4}/{\hat{\eta}_{\nu}}g_{3}\big(\hat{\eta}_{\nu}^{-2}s;\hat{\sigma}(\nu)\big)\Big), |  |

and so the result follows setting

 | g ^ 1 ​ ( s, ν):= η ^ ν ​ g 1 ​ ( η ^ ν − 2 ​ s, σ ^ ​ ( ν)), g ^ 2 ​ ( s, ν):= η ^ ν − 3 ​ g 2 ​ ( η ^ ν − 2 ​ s, σ ^ ​ ( ν)) ​ and ​ g ^ 3 ​ ( s, ν):= η ^ ν − 3 ​ g 3 ​ ( η ^ ν − 2 ​ s, σ ^ ​ ( ν)), \hat{g}_{1}(s;\nu)\!:=\hat{\eta}_{\nu}g_{1}\big(\hat{\eta}_{\nu}^{-2}s;\hat{\sigma}(\nu)\big),\;\hat{g}_{2}(s;\nu)\!:=\hat{\eta}_{\nu}^{-3}g_{2}\big(\hat{\eta}_{\nu}^{-2}s;\hat{\sigma}(\nu)\big)\text{ and }\hat{g}_{3}(s;\nu)\!:=\hat{\eta}_{\nu}^{-3}g_{3}\big(\hat{\eta}_{\nu}^{-2}s;\hat{\sigma}(\nu)\big), |  |

which satisfy conditions ( a) (a), ( b) (b) and ( c) (c) in the statement due to λ ¯ ∘ σ ^ = λ ¯ \underline{\lambda}\circ\hat{\sigma}=\underline{\lambda}, η ^ ν > 0 \hat{\eta}_{\nu}>0 and assertion ( h) (h) of Lemma A.7. This concludes the proof of the result.

By applying Lemma 3.1 it suffices to consider the quadratic 5-perturbation { X μ } \{X_{\mu}\} given in ( 12) (\ref{pert}). To begin with let us take μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) with a 0 ≠ − 1 a_{0}\neq-1 and note that then by Theorem 3.5 and Corollary 4.2, respectively, we obtain that

 | ℛ u ​ ( s, ν):= 𝒟 u ​ ( s, μ) | μ = Φ − 1 ​ ( ν) g 1 ​ ( s, ν) \displaystyle\mathscr{R}_{u}(s;\nu)\!:=\frac{\left.\mathscr{D}_{u}(s;\mu)\right|_{\mu=\Phi^{-1}(\nu)}}{g_{1}(s;\nu)} | = ν 1 + ν 2 ​ g 2 ​ ( s, ν) g 1 ​ ( s, ν) + ν 3 ​ ν 5 ​ g 3 ​ ( s, ν) g 1 ​ ( s, ν) \displaystyle=\nu_{1}+\nu_{2}\frac{g_{2}(s;\nu)}{g_{1}(s;\nu)}+\nu_{3}\nu_{5}\frac{g_{3}(s;\nu)}{g_{1}(s;\nu)} |  |

 |  | = ν 1 + ν 2 ​ h 2 ​ ( s, ν) + ν 3 ​ ν 5 ​ h 3 ​ ( s, ν) \displaystyle=\nu_{1}+\nu_{2}h_{2}(s;\nu)+\nu_{3}\nu_{5}h_{3}(s;\nu) |  | (19) |

and |

 | ℛ ℓ ​ ( s, ν):= 𝒟 ℓ ​ ( s, μ) | μ = Φ − 1 ​ ( ν) g ^ 1 ​ ( s, ν) \displaystyle\mathscr{R}_{\ell}(s;\nu)\!:=\frac{\left.\mathscr{D}_{\ell}(s;\mu)\right|_{\mu=\Phi^{-1}(\nu)}}{\hat{g}_{1}(s;\nu)} | = ν 1 + ν 3 ​ g ^ 2 ​ ( s, ν) g ^ 1 ​ ( s, ν) + ν 2 ​ ν 4 ​ g ^ 3 ​ ( s, ν) g ^ 1 ​ ( s, ν) \displaystyle=\nu_{1}+\nu_{3}\frac{\hat{g}_{2}(s;\nu)}{\hat{g}_{1}(s;\nu)}+\nu_{2}\nu_{4}\frac{\hat{g}_{3}(s;\nu)}{\hat{g}_{1}(s;\nu)} |  |

 |  | = ν 1 + ν 3 ​ h ^ 2 ​ ( s, ν) + ν 2 ​ ν 4 ​ h ^ 3 ​ ( s, ν), \displaystyle=\nu_{1}+\nu_{3}\hat{h}_{2}(s;\nu)+\nu_{2}\nu_{4}\hat{h}_{3}(s;\nu), |  | (20) |

where by applying Lemma A.7 we have that

 | h 2:= g 2 / g 1 = s λ ¯ ​ ( ν) ​ ( κ 4 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) ​ and ​ h 3:= g 3 / g 1 = s λ ¯ ′ ​ ( ν) ​ ( κ 5 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) h_{2}\!:=g_{2}/g_{1}=s^{\underline{\lambda}(\nu)}\big(\kappa_{4}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)\text{ and }h_{3}\!:=g_{3}/g_{1}=s^{\underline{\lambda}^{\prime}(\nu)}\big(\kappa_{5}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) |  | (21) |

with κ i ​ ( ν 0) > 0 \kappa_{i}(\nu_{0})>0 and

 | h ^ 2:= g ^ 2 / g ^ 1 = s λ ¯ ​ ( ν) ​ ( κ ^ 4 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) ​ and ​ h ^ 3:= g ^ 3 / g ^ 1 = s λ ¯ ′ ​ ( ν) ​ ( κ ^ 5 ​ ( ν) + ℱ δ ∞ ​ ( ν 0)) \hat{h}_{2}\!:=\hat{g}_{2}/\hat{g}_{1}=s^{\underline{\lambda}(\nu)}\big(\hat{\kappa}_{4}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big)\text{ and }\hat{h}_{3}\!:=\hat{g}_{3}/\hat{g}_{1}=s^{\underline{\lambda}^{\prime}(\nu)}\big(\hat{\kappa}_{5}(\nu)+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\big) |  | (22) |

with κ ^ i ​ ( ν 0) > 0 \hat{\kappa}_{i}(\nu_{0})>0. Note that the limit cycles of X μ X_{\mu} that are close to Γ u \Gamma_{u} (respectively, Γ ℓ \Gamma_{\ell}) in Hausdorff sense are in one to one correspondence with the isolated positive zeroes of 𝒟 u ​ ( ⋅, μ) \mathscr{D}_{u}(\,\cdot\,;\mu) (respectively, 𝒟 ℓ ​ ( ⋅, μ) \mathscr{D}_{\ell}(\,\cdot\,;\mu)). In turn, those zeroes are in one to one correspondence with the ones of ℛ u ​ ( ⋅, ν) \mathscr{R}_{u}(\,\cdot\,;\nu) and ℛ ℓ ​ ( ⋅, ν) \mathscr{R}_{\ell}(\,\cdot\,;\nu), respectively, where ν = Φ ⁡ ( μ). \nu=\Phi(\mu).

We claim first that Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩽ 3. \mathrm{Cycl}\big((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu}\big)\leqslant 3. We prove it by contradiction. If the claim is false then, since we know by Theorem B that Cycl ⁡ ( ( Γ u, X μ 0), X μ) = Cycl ⁡ ( ( Γ ℓ, X μ 0), X μ) = 2 \mathrm{Cycl}((\Gamma_{u},X_{\mu_{0}}),X_{\mu})=\mathrm{Cycl}((\Gamma_{\ell},X_{\mu_{0}}),X_{\mu})=2, by applying Rolle’s Theorem there would exist three sequences s n → 0 + s_{n}\to 0^{+}, s n ′ → 0 + s_{n}^{\prime}\to 0^{+} and ν n → ν 0:= Φ ⁡ ( μ 0) \nu_{n}\to\nu_{0}\!:=\Phi(\mu_{0}) such that ∂ s ℛ u ​ ( s n, ν n) = ∂ s ℛ ℓ ​ ( s n ′, ν n) = 0 \partial_{s}\mathscr{R}_{u}(s_{n};\nu_{n})=\partial_{s}\mathscr{R}_{\ell}(s^{\prime}_{n};\nu_{n})=0 for all n n. On the other hand, by Lemma A.7 again, from ( 21) (\ref{thCeq3}) we get that

 | lim s → 0 + ∂ s h 3 ​ ( s, ν) ∂ s h 2 ​ ( s, ν) = 0 ​ uniformly on ν ≈ ν 0. \lim_{s\to 0^{+}}\frac{\partial_{s}h_{3}(s;\nu)}{\partial_{s}h_{2}(s;\nu)}=0\text{ uniformly on $\nu\approx\nu_{0}.$} |  |

Then from ( 19) (\ref{thCeq1}) we obtain that ∂ s ℛ u ​ ( s n, ν n) = ν 2 ​ ∂ s h 2 ​ ( s n, ν) + ν 3 ​ ν 5 ​ ∂ s h 3 ​ ( s n, ν) | ν = ν n = 0 \partial_{s}\mathscr{R}_{u}(s_{n};\nu_{n})=\nu_{2}\partial_{s}h_{2}(s_{n};\nu)+\nu_{3}\nu_{5}\partial_{s}h_{3}(s_{n};\nu)\big|_{\nu=\nu_{n}}=0 for all n n and, consequently,

 | ν 2 ν 3 ​ ν 5 | ν = ν n = − ∂ s h 3 ​ ( s n, ν n) ∂ s h 2 ​ ( s n, ν n) → 0 ​ as n → ∞. \left.\frac{\nu_{2}}{\nu_{3}\nu_{5}}\right|_{\nu=\nu_{n}}=-\frac{\partial_{s}h_{3}(s_{n};\nu_{n})}{\partial_{s}h_{2}(s_{n};\nu_{n})}\to 0\text{ as $n\to\infty.$} |  |

Therefore lim n → ∞ ν 2 ν 3 ​ ν 5 | ν = ν n = 0. \lim_{n\to\infty}\frac{\nu_{2}}{\nu_{3}\nu_{5}}\big|_{\nu=\nu_{n}}=0. Exactly the same way, but using ( 22) (\ref{thCeq4}) and that ∂ s ℛ ℓ ​ ( s n ′, ν n) = 0 \partial_{s}\mathscr{R}_{\ell}(s^{\prime}_{n};\nu_{n})=0 for all n, n, we get that lim n → ∞ ν 3 ν 2 ​ ν 4 | ν = ν n = 0 \lim_{n\to\infty}\frac{\nu_{3}}{\nu_{2}\nu_{4}}\big|_{\nu=\nu_{n}}=0. The combination of both limits implies that 1 ν 4 ​ ν 5 | ν = ν n \frac{1}{\nu_{4}\nu_{5}}\big|_{\nu=\nu_{n}} tends to 0 0 as n → ∞, n\to\infty, which is a contradiction because lim n → ∞ ν n = ν 0 ∈ ℝ 5. \lim_{n\to\infty}\nu_{n}=\nu_{0}\in\mathbb{R}^{5}. This proves the claim.

In order to proceed we take ε > 0 \varepsilon>0 and s 0 > 0 s_{0}>0 small enough such that the functions h i ​ ( s, ν) h_{i}(s;\nu) and h ^ i ​ ( s, ν) \hat{h}_{i}(s;\nu) for i = 1, 2 i=1,2 are strictly positive for all s ∈ ( 0, s 0) s\in(0,s_{0}) and ν ∈ B ε ​ ( ν 0). \nu\in B_{\varepsilon}(\nu_{0}).

We claim next that Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩾ 3 \mathrm{Cycl}((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu})\geqslant 3 for all ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2) with a 0 ≠ − 1 a_{0}\neq-1 verifying that a 0 + b 0 ⩽ 0 a_{0}+b_{0}\leqslant 0 or a 0 + 2 − b 0 ⩽ 0. a_{0}+2-b_{0}\leqslant 0. Let us assume for instance that a 0 + b 0 ⩽ 0 a_{0}+b_{0}\leqslant 0 (the other case follows verbatim). To this end recall, see ( 13) (\ref{c_pm}), that ν 0 = Φ ⁡ ( μ 0) = ( 0, 0, 0, a 0 + 2 − b 0, a 0 + b 0) \nu_{0}=\Phi(\mu_{0})=(0,0,0,a_{0}+2-b_{0},a_{0}+b_{0}) and so the fifth component of ν 0 \nu_{0} is not positive. That being said we take ν ¯ ∈ B ε ( ν 0) ∩ { ν 1 = ν 2 = 0, ν 3 ≠ 0, ν 5 < 0 } \bar{\nu}\in B_{\varepsilon}(\nu_{0})\cap\{\nu_{1}=\nu_{2}=0,\nu_{3}\neq 0,\nu_{5}<0\} and s 1 ∈ ( 0, s 0) s_{1}\in(0,s_{0}) in order that ν ¯ 3 ​ ℛ u ​ ( s 1, ν ¯) < 0 \bar{\nu}_{3}\mathscr{R}_{u}(s_{1};\bar{\nu})<0 and ν ¯ 3 ​ ℛ ℓ ​ ( s 1, ν ¯) > 0 \bar{\nu}_{3}\mathscr{R}_{\ell}(s_{1};\bar{\nu})>0, see ( 19) (\ref{thCeq1}) and ( 20) (\ref{thCeq2}), respectively. Next, by continuity, we can take ν ^ ∈ B ε ​ ( ν 0) ∩ { ν 1 = 0, ν 2 ​ ν 3 > 0 } \hat{\nu}\in B_{\varepsilon}(\nu_{0})\cap\{\nu_{1}=0,\nu_{2}\nu_{3}>0\} close enough to ν ¯ \bar{\nu} in order to have

 | ν ^ 3 ​ ν ¯ 3 > 0, ℛ u ​ ( s 1, ν ^) ​ ℛ u ​ ( s 1, ν ¯) > 0 ​ and ​ ℛ ℓ ​ ( s 1, ν ^) ​ ℛ ℓ ​ ( s 1, ν ¯) > 0. \hat{\nu}_{3}\bar{\nu}_{3}>0,\quad\mathscr{R}_{u}(s_{1};\hat{\nu})\mathscr{R}_{u}(s_{1};\bar{\nu})>0\text{ and }\mathscr{R}_{\ell}(s_{1};\hat{\nu})\mathscr{R}_{\ell}(s_{1};\bar{\nu})>0. |  |

We take then s 2 ∈ ( 0, s 1) s_{2}\in(0,s_{1}) small enough such that, on account of ( 19) (\ref{thCeq1}) and ( 21) (\ref{thCeq3}), ν ^ 2 ​ ℛ u ​ ( s 2, ν ^) > 0. \hat{\nu}_{2}\mathscr{R}_{u}(s_{2};\hat{\nu})>0. Finally, by continuity again, we choose ν ⋆ ∈ B ε ( ν 0) ∩ { ν 1 ν 2 < 0 } \nu^{\star}\in B_{\varepsilon}(\nu_{0})\cap\{\nu_{1}\nu_{2}<0\} close enough to ν ^ \hat{\nu} such that

 | ℛ u ​ ( s 1, ν ⋆) ​ ℛ u ​ ( s 1, ν ^) > 0 ν 2 ⋆ ​ ν ^ 2 > 0 ℛ ℓ ​ ( s 1, ν ⋆) ​ ℛ ℓ ​ ( s 1, ν ^) > 0 ν 3 ⋆ ​ ν ^ 3 > 0 ℛ u ​ ( s 2, ν ⋆) ​ ℛ u ​ ( s 2, ν ^) > 0 \begin{array}[]{ll}\mathscr{R}_{u}(s_{1};\nu^{\star})\mathscr{R}_{u}(s_{1};\hat{\nu})>0&\qquad\nu_{2}^{\star}\hat{\nu}_{2}>0\\[7.0pt] \mathscr{R}_{\ell}(s_{1};\nu^{\star})\mathscr{R}_{\ell}(s_{1};\hat{\nu})>0&\qquad\nu_{3}^{\star}\hat{\nu}_{3}>0\\[7.0pt] \mathscr{R}_{u}(s_{2};\nu^{\star})\mathscr{R}_{u}(s_{2};\hat{\nu})>0&\end{array} |  |

Observe that we can also take s 3 ∈ ( 0, s 2) s_{3}\in(0,s_{2}) small enough such that, thanks to ( 19) (\ref{thCeq1}) and ( 20) (\ref{thCeq2}),

 | ν 1 ⋆ ​ ℛ u ​ ( s 3, ν ⋆) > 0 ​ and ​ ν 1 ⋆ ​ ℛ ℓ ​ ( s 3, ν ⋆) > 0. \nu_{1}^{\star}\mathscr{R}_{u}(s_{3};\nu^{\star})>0\text{ and }\nu_{1}^{\star}\mathscr{R}_{\ell}(s_{3};\nu^{\star})>0. |  |

Then ℛ ℓ ​ ( s 1, ν ⋆) ​ ℛ ℓ ​ ( s 3, ν ⋆) < 0 \mathscr{R}_{\ell}(s_{1};\nu^{\star})\mathscr{R}_{\ell}(s_{3};\nu^{\star})<0 due to ν 2 ⋆ ​ ν 3 ⋆ > 0 \nu_{2}^{\star}\nu_{3}^{\star}>0 and ν 1 ⋆ ​ ν 2 ⋆ < 0. \nu_{1}^{\star}\nu_{2}^{\star}<0. Therefore, by Bolzano’s Theorem, there exists s ℓ ∈ ( s 3, s 1) s_{\ell}\in(s_{3},s_{1}) such that ℛ ℓ ​ ( s ℓ, ν ⋆) = 0. \mathscr{R}_{\ell}(s_{\ell};\nu^{\star})=0. On the other hand,

 | ℛ u ​ ( s 3, ν ⋆) ​ ℛ u ​ ( s 2, ν ⋆) < 0 ​ and ​ ℛ u ​ ( s 2, ν ⋆) ​ ℛ u ​ ( s 1, ν ⋆) < 0 \mathscr{R}_{u}(s_{3};\nu^{\star})\mathscr{R}_{u}(s_{2};\nu^{\star})<0\text{ and }\mathscr{R}_{u}(s_{2};\nu^{\star})\mathscr{R}_{u}(s_{1};\nu^{\star})<0 |  |

due to ν 1 ⋆ ​ ν 2 ⋆ < 0 \nu_{1}^{\star}\nu_{2}^{\star}<0 and ν 2 ⋆ ​ ν 3 ⋆ > 0 \nu_{2}^{\star}\nu_{3}^{\star}>0, respectively. Consequently, by applying Bolzano’s Theorem again, there exist s u 1 ∈ ( s 3, s 2) s_{u}^{1}\in(s_{3},s_{2}) and s u 2 ∈ ( s 2, s 1) s_{u}^{2}\in(s_{2},s_{1}) such that ℛ u ​ ( s u 1, ν ⋆) = ℛ u ​ ( s u 2, ν ⋆) = 0. \mathscr{R}_{u}(s_{u}^{1};\nu^{\star})=\mathscr{R}_{u}(s_{u}^{2};\nu^{\star})=0. Summing-up, we have proved that there exist ν ⋆ ∈ B ε ​ ( ν 0) \nu^{\star}\in B_{\varepsilon}(\nu_{0}) and s ℓ, s u 1, s u 2 ∈ ( 0, s 0) s_{\ell},s_{u}^{1},s_{u}^{2}\in(0,s_{0}) with s u 1 ≠ s u 2 s_{u}^{1}\neq s_{u}^{2} such that

 | ℛ ℓ ​ ( s ℓ, ν ⋆) = ℛ u ​ ( s u 1, ν ⋆) = ℛ u ​ ( s u 2, ν ⋆) = 0. \mathscr{R}_{\ell}(s_{\ell};\nu^{\star})=\mathscr{R}_{u}(s_{u}^{1};\nu^{\star})=\mathscr{R}_{u}(s_{u}^{2};\nu^{\star})=0. |  |

Accordingly Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩾ 3 \mathrm{Cycl}((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu})\geqslant 3 because ν 0 = Φ ⁡ ( μ 0) \nu_{0}=\Phi(\mu_{0}) and we can take ε > 0 \varepsilon>0 and s 0 > 0 s_{0}>0 arbitrarily small. This proves the claim. (For completeness let us note that the case a 0 + 2 − b 0 ⩽ 0 a_{0}+2-b_{0}\leqslant 0 leads to the simultaneous bifurcation of one limit cycle from Γ u \Gamma_{u} and two from Γ ℓ. \Gamma_{\ell}.)

Thanks to the claim we also have that Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩾ 3 \mathrm{Cycl}((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu})\geqslant 3 for each μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) with ( a 0, b 0) ∈ { − 1 } × ( 0, 2) (a_{0},b_{0})\in\{-1\}\times(0,2) because in any neighbourhood of such μ 0 \mu_{0} there exist a parameter μ ⋆ \mu_{\star}, not in { a = − 1 }, \{a=-1\}, verifying that Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ ⋆), X μ) ⩾ 3 \mathrm{Cycl}((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{\star}}),X_{\mu})\geqslant 3.

Our last task is to show that if ( a 0, b 0) ∈ 𝒦 2, (a_{0},b_{0})\in\mathcal{K}_{2}, i.e., a 0 + b 0 > 0 a_{0}+b_{0}>0 and a 0 + 2 − b 0 > 0 a_{0}+2-b_{0}>0 is verified, then Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) = 2 \mathrm{Cycl}((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu})=2. To this end, on account of

 | Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩾ max ⁡ { Cycl ⁡ ( ( Γ u, X μ 0), X μ), Cycl ⁡ ( ( Γ ℓ, X μ 0), X μ) } = 2, \mathrm{Cycl}\big((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu}\big)\geqslant\max\left\{\mathrm{Cycl}\big((\Gamma_{u},X_{\mu_{0}}),X_{\mu}\big),\mathrm{Cycl}\big((\Gamma_{\ell},X_{\mu_{0}}),X_{\mu}\big)\right\}=2, |  |

it is clear that it suffices to prove that Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩽ 2. \mathrm{Cycl}\big((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu}\big)\leqslant 2. We shall bound this number by studying the positive zeros of ℛ u ​ ( s, ν) \mathscr{R}_{u}(s;\nu) and ℛ ℓ ​ ( s, ν) \mathscr{R}_{\ell}(s;\nu), see ( 19) (\ref{thCeq1}) and ( 20) (\ref{thCeq2}), bifurcating from s = 0 s=0 when ν \nu tends to ν 0 ∈ { ν 1 = ν 2 = ν 3 = 0, ν 4 > 0 and ν 5 > 0 }. \nu_{0}\in\{\nu_{1}=\nu_{2}=\nu_{3}=0,\nu_{4}>0\text{ and }\nu_{5}>0\}. Recall here that ν 0 = Φ ⁡ ( μ 0) = ( 0, 0, 0, a 0 + 2 − b 0, a 0 + b 0) \nu_{0}=\Phi(\mu_{0})=(0,0,0,a_{0}+2-b_{0},a_{0}+b_{0}). On account of ( 21) (\ref{thCeq3}) and ( 22) (\ref{thCeq4}), respectively, the application of Lemma A.7 yields

 | h 2 ​ ( s, ν) = κ 4 ​ ( ν) ​ ( s ⁡ ( 1 + ℱ δ ∞ ​ ( ν 0))) λ ¯ ​ ( ν) ​ and ​ h ^ 2 ​ ( s, ν) = κ ^ 4 ​ ( ν) ​ ( s ⁡ ( 1 + ℱ δ ∞ ​ ( ν 0))) λ ¯ ​ ( ν). h_{2}(s;\nu)=\kappa_{4}(\nu)\left(s\left(1+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\right)\right)^{\underline{\lambda}(\nu)}\text{ and }\hat{h}_{2}(s;\nu)=\hat{\kappa}_{4}(\nu)\left(s\left(1+\mathcal{F}_{\delta}^{\infty}(\nu_{0})\right)\right)^{\underline{\lambda}(\nu)}. |  |

Accordingly, by applying twice Lemma A.9 we deduce that

 | ( t, ν) = Ψ ⁡ ( s, ν):= ( h 2 ​ ( s, ν), ν) ​ and ​ ( t, ν) = Ψ ^ ​ ( s, ν):= ( h ^ 2 ​ ( s, ν), ν) (t,\nu)=\Psi(s,\nu)\!:=\big(h_{2}(s;\nu),\nu\big)\text{ and }(t,\nu)=\hat{\Psi}\big(s;\nu)\!:=\big(\hat{h}_{2}(s;\nu),\nu\big) |  |

are well defined changes of variables satisfying

 | Ψ − 1 ​ ( t, ν) = ( σ ⁡ ( ( t / κ 4 ​ ( ν)) 1 / λ ¯ ​ ( ν), ν), ν) ​ and ​ Ψ ^ − 1 ​ ( t, ν) = ( σ ^ ​ ( ( t / κ ^ 4 ​ ( ν)) 1 / λ ¯ ​ ( ν), ν), ν), \Psi^{-1}(t,\nu)=\big(\sigma((t/\kappa_{4}(\nu))^{1/\underline{\lambda}(\nu)};\nu),\nu\big)\text{ and }\hat{\Psi}^{-1}(t,\nu)=\big(\hat{\sigma}((t/\hat{\kappa}_{4}(\nu))^{1/\underline{\lambda}(\nu)};\nu),\nu\big), |  |

where σ ⁡ ( u, ν):= u ⁡ ( 1 + ℱ δ ∞ ​ ( ν 0)) \sigma(u;\nu)\!:=u(1+\mathcal{F}_{\delta}^{\infty}(\nu_{0})) and σ ^ ​ ( u, ν):= u ⁡ ( 1 + ℱ δ ∞ ​ ( ν 0)) \hat{\sigma}(u;\nu)\!:=u(1+\mathcal{F}_{\delta}^{\infty}(\nu_{0})). Our aim is to apply these changes of variables in ( 19) (\ref{thCeq1}) and ( 20) (\ref{thCeq2}), respectively. To this end note that, by Lemma A.7 once again, from ( 21) (\ref{thCeq3}) and ( 22) (\ref{thCeq4}) we get

 | ( h 3 ∘ Ψ − 1) ​ ( t, ν) = t ϑ ⁡ ( ν) ​ ( κ ⁡ ( ν) + f ⁡ ( t, ν)) ​ and ​ ( h ^ 3 ∘ Ψ ^ − 1) ​ ( t, ν) = t ϑ ⁡ ( ν) ​ ( κ ^ ​ ( ν) + f ^ ​ ( t, ν)) \big(h_{3}\circ\Psi^{-1}\big)(t;\nu)=t^{\vartheta(\nu)}(\kappa(\nu)+f(t;\nu))\text{ and }\big(\hat{h}_{3}\circ\hat{\Psi}^{-1}\big)(t;\nu)=t^{\vartheta(\nu)}(\hat{\kappa}(\nu)+\hat{f}(t;\nu)) |  |

with ϑ ⁡ ( ν):= λ ¯ ′ ​ ( ν) / λ ¯ ​ ( ν) = 1 + min ⁡ ( 1, 1 / λ ¯ ​ ( ν)) > 1 \vartheta(\nu)\!:=\underline{\lambda}^{\prime}(\nu)/\underline{\lambda}(\nu)=1+\min(1,1/\underline{\lambda}(\nu))>1, κ \kappa and κ ^ \hat{\kappa} smooth positive functions, and f, f ^ ∈ ℱ δ 1 ∞ ​ ( ν 0) f,\hat{f}\in\mathcal{F}^{\infty}_{\delta_{1}}(\nu_{0}) for some δ 1 > 0 \delta_{1}>0 small enough. Accordingly, from ( 19) (\ref{thCeq1}) and ( 20) (\ref{thCeq2}),

 | ℛ ¯ u ​ ( t, ν):= ( ℛ u ∘ Ψ − 1) ​ ( t, ν) \displaystyle\bar{\mathscr{R}}_{u}(t;\nu)\!:=(\mathscr{R}_{u}\circ\Psi^{-1})(t,\nu) | = ν 1 + ν 2 ​ t + ν 3 ​ ν 5 ​ t ϑ ⁡ ( ν) ​ ( κ ⁡ ( ν) + f ⁡ ( t, ν)) \displaystyle=\nu_{1}+\nu_{2}t+\nu_{3}\nu_{5}t^{\vartheta(\nu)}(\kappa(\nu)+f(t;\nu)) |  |

and |

 | ℛ ¯ ℓ ​ ( t, ν):= ( ℛ ℓ ∘ Ψ ^ − 1) ​ ( t, ν) \displaystyle\bar{\mathscr{R}}_{\ell}(t;\nu)\!:=(\mathscr{R}_{\ell}\circ\hat{\Psi}^{-1})(t,\nu) | = ν 1 + ν 3 ​ t + ν 2 ​ ν 4 ​ t ϑ ⁡ ( ν) ​ ( κ ^ ​ ( ν) + f ^ ​ ( t, ν)). \displaystyle=\nu_{1}+\nu_{3}t+\nu_{2}\nu_{4}t^{\vartheta(\nu)}(\hat{\kappa}(\nu)+\hat{f}(t;\nu)). |  |

We are now in position to prove that Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩽ 2 \mathrm{Cycl}((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu})\leqslant 2. By contradiction, if this number is greater than 2 then (by exchanging the subindices u u and ℓ \ell if necessary) for all ε > 0 \varepsilon>0 there would exist

 | ( t 1, t 2, t 3, ν) ∈ W ε:= ( 0, ε) 3 × B ε ( ν 0) ∖ { t 1 = t 2 or ν 1 = ν 2 = ν 3 = 0 } (t_{1},t_{2},t_{3},\nu)\in W_{\varepsilon}\!:=(0,\varepsilon)^{3}\times B_{\varepsilon}(\nu_{0})\setminus\big\{t_{1}=t_{2}\text{ or }\nu_{1}=\nu_{2}=\nu_{3}=0\big\} |  |

verifying that

 | ℛ ¯ u ​ ( t 1, ν) = ℛ ¯ u ​ ( t 2, ν) = ℛ ¯ ℓ ​ ( t 3, ν) = 0. \bar{\mathscr{R}}_{u}(t_{1};\nu)=\bar{\mathscr{R}}_{u}(t_{2};\nu)=\bar{\mathscr{R}}_{\ell}(t_{3};\nu)=0. |  |

These three equalities can be written as

 | ( 1 t 1 ν 5 ​ t 1 ϑ ⁡ ( ν) ​ ( κ ⁡ ( ν) + f ⁡ ( t 1, ν)) 1 t 2 ν 5 ​ t 2 ϑ ⁡ ( ν) ​ ( κ ⁡ ( ν) + f ⁡ ( t 2, ν)) 1 ν 4 ​ t 3 ϑ ⁡ ( ν) ​ ( κ ^ ​ ( ν) + f ^ ​ ( t 3, ν)) t 3) ​ ( ν 1 ν 2 ν 3) = ( 0 0 0). \left(\begin{array}[]{ccc}1&t_{1}&\nu_{5}t_{1}^{\vartheta(\nu)}(\kappa(\nu)+f(t_{1};\nu))\\ 1&t_{2}&\nu_{5}t_{2}^{\vartheta(\nu)}(\kappa(\nu)+f(t_{2};\nu))\\ 1&\nu_{4}t_{3}^{\vartheta(\nu)}(\hat{\kappa}(\nu)+\hat{f}(t_{3};\nu))&t_{3}\end{array}\right)\left(\begin{array}[]{c}\nu_{1}\\ \nu_{2}\\ \nu_{3}\end{array}\right)=\left(\begin{array}[]{c}0\\ 0\\ 0\end{array}\right). |  |

A necessary condition for this to hold is that the determinant

 | D ⁡ ( t 1, t 2, t 3, ν):= | 1 t 1 ν 5 ​ t 1 ϑ ⁡ ( ν) ​ ( κ ⁡ ( ν) + f ⁡ ( t 1, ν)) 1 t 2 ν 5 ​ t 2 ϑ ⁡ ( ν) ​ ( κ ⁡ ( ν) + f ⁡ ( t 2, ν)) 1 ν 4 ​ t 3 ϑ ⁡ ( ν) ​ ( κ ^ ​ ( ν) + f ^ ​ ( t 3, ν)) t 3 | D(t_{1},t_{2},t_{3};\nu)\!:=\left|\begin{array}[]{ccc}1&t_{1}&\nu_{5}t_{1}^{\vartheta(\nu)}(\kappa(\nu)+f(t_{1};\nu))\\ 1&t_{2}&\nu_{5}t_{2}^{\vartheta(\nu)}(\kappa(\nu)+f(t_{2};\nu))\\ 1&\nu_{4}t_{3}^{\vartheta(\nu)}(\hat{\kappa}(\nu)+\hat{f}(t_{3};\nu))&t_{3}\end{array}\right| |  |

is equal to zero because ( t 1, t 2, t 3, ν) ∈ W ε (t_{1},t_{2},t_{3},\nu)\in W_{\varepsilon}. An easy computation shows that we can write

 | D ⁡ ( t 1, t 2, t 3, ν) t 2 − t 1 = t 3 ​ ( 1 − ν 5 ​ t 3 ϑ ⁡ ( ν) − 1 ​ ( κ ^ ​ ( ν) + f ^ ​ ( t 3, ν)) ​ A 0 ​ ( t 1, t 2, ν)) + ν 5 ​ t 1 ​ t 2 ​ A 1 ​ ( t 1, t 2, ν), \frac{D(t_{1},t_{2},t_{3};\nu)}{t_{2}-t_{1}}=t_{3}\left(1-\nu_{5}t_{3}^{\vartheta(\nu)-1}\left(\hat{\kappa}(\nu)+\hat{f}(t_{3};\nu)\right)A_{0}(t_{1},t_{2};\nu)\right)+\nu_{5}t_{1}t_{2}A_{1}(t_{1},t_{2};\nu), |  | (23) |

where, for i = 0, 1 i=0,1,

 | A i ​ ( t 1, t 2, ν):= \displaystyle A_{i}(t_{1},t_{2};\nu)\!:=\, | t 2 ϑ ⁡ ( ν) − i ​ ( κ ⁡ ( ν) + f ⁡ ( t 2, ν)) − t 1 ϑ ⁡ ( ν) − i ​ ( κ ⁡ ( ν) + f ⁡ ( t 1, ν)) t 2 − t 1 \displaystyle\frac{t_{2}^{\vartheta(\nu)-i}(\kappa(\nu)+f(t_{2};\nu))-t_{1}^{\vartheta(\nu)-i}(\kappa(\nu)+f(t_{1};\nu))}{t_{2}-t_{1}} |  |

 | = \displaystyle=\, | t 2 ϑ ⁡ ( ν) − i − t 1 ϑ ⁡ ( ν) − i t 2 − t 1 ​ ( κ ⁡ ( ν) + f i ​ ( t 2 ϑ ⁡ ( ν) − i, ν) − f i ​ ( t 1 ϑ ⁡ ( ν) − i, ν) t 2 ϑ ⁡ ( ν) − i − t 1 ϑ ⁡ ( ν) − i), \displaystyle\frac{t_{2}^{\vartheta(\nu)-i}-t_{1}^{\vartheta(\nu)-i}}{t_{2}-t_{1}}\left(\kappa(\nu)+\frac{f_{i}\big(t_{2}^{\vartheta(\nu)-i};\nu\big)-f_{i}\big(t_{1}^{\vartheta(\nu)-i};\nu\big)}{t_{2}^{\vartheta(\nu)-i}-t_{1}^{\vartheta(\nu)-i}}\right), |  |

with f i ​ ( r, ν):= r ​ f ​ ( r 1 ϑ ⁡ ( ν) − i, ν) ∈ ℱ 1 + δ 2 ∞ ​ ( ν 0) f_{i}(r;\nu)\!:=rf\left(r^{\frac{1}{\vartheta(\nu)-i}};\nu\right)\in\mathcal{F}_{1+\delta_{2}}^{\infty}(\nu_{0}) for some δ 2 > 0 \delta_{2}>0 small enough. By applying (twice) the Mean Value Theorem there exist α i > 0 \alpha_{i}>0 between t 1 t_{1} and t 2 t_{2}, together with β i > 0 \beta_{i}>0 between t 1 ϑ ⁡ ( ν) − i t_{1}^{\vartheta(\nu)-i} and t 2 ϑ ⁡ ( ν) − i t_{2}^{\vartheta(\nu)-i}, (depending both on t 1 t_{1}, t 2 t_{2} and ν \nu) such that

 | A i ​ ( t 1, t 2, ν) = ( ϑ ⁡ ( ν) − i) ​ α i ϑ ⁡ ( ν) − i − 1 ​ ( κ ⁡ ( ν) + ∂ r f i ​ ( β i, ν)) ​ for each i = 0, 1. A_{i}(t_{1},t_{2};\nu)=\big(\vartheta(\nu)-i\big)\alpha_{i}^{\vartheta(\nu)-i-1}\big(\kappa(\nu)+\partial_{r}f_{i}(\beta_{i};\nu)\big)\text{ for each $i=0,1.$} |  |

On account of ϑ ⁡ ( ν 0) > 1 \vartheta(\nu_{0})>1 and ∂ r f i ∈ ℱ δ 2 ∞ ​ ( ν 0) \partial_{r}f_{i}\in\mathcal{F}_{\delta_{2}}^{\infty}(\nu_{0}) with δ 2 > 0, \delta_{2}>0, we can assert that A 0 ​ ( t 1, t 2, ν) A_{0}(t_{1},t_{2};\nu) tends to zero as ( t 1, t 2, ν) → ( 0 +, 0 +, ν 0) (t_{1},t_{2},\nu)\to(0^{+},0^{+},\nu_{0}) and that A 1 ​ ( t 1, t 2, ν) > 0 A_{1}(t_{1},t_{2};\nu)>0 on W ε W_{\varepsilon} for ε > 0 \varepsilon>0 small enough. Since ν 5 > 0 \nu_{5}>0, from ( 23) (\ref{thCeq5}) we conclude that ( t 2 − t 1) ​ D ​ ( t 1, t 2, t 3, ν) > 0 (t_{2}-t_{1})D(t_{1},t_{2},t_{3};\nu)>0 for all ( t 1, t 2, t 3, ν) ∈ W ε (t_{1},t_{2},t_{3},\nu)\in W_{\varepsilon} with ε > 0 \varepsilon>0 small enough. This contradicts D ⁡ ( t 1, t 2, t 3, ν) = 0 D(t_{1},t_{2},t_{3};\nu)=0 and so Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) ⩽ 2. \mathrm{Cycl}\big((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu}\big)\leqslant 2. This concludes the proof of the result.

## 5 Proof of Theorem D

In this section we shall demonstrate Theorem D. However, prior to that, we shall give two general results regarding the different notions of cyclicity considered in this paper. Thus, otherwise explicitly stated, we consider a germ { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} of an arbitrary analytic family of vector fields on 𝕊 2 \mathbb{S}^{2}. Given U ⊆ 𝕊 2, U\subseteq\mathbb{S}^{2}, we denote by 𝒞 ⁡ ( U) \mathcal{C}(U) the set of compact subsets K ⊂ U K\subset U and, as usual, N ε ​ ( U) N_{\varepsilon}(U) stands for the open ε \varepsilon -neighbourhood of U. U. We also denote the set of limit periodic sets of the germ { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} by ℒ \mathcal{L}, so that ℒ ⊂ 𝒞 ⁡ ( 𝕊 2) \mathcal{L}\subset\mathcal{C}(\mathbb{S}^{2}), see Definition 1.

###### Lemma 5.1.

If U U is an open subset of 𝕊 2 \mathbb{S}^{2} then Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) ⩽ Cycl G ​ ( ( ∂ U, X μ 0), X μ). \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)\leqslant\mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big).

Fix a natural number c ⩽ Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) c\leqslant\underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big). For any ρ > 0 \rho>0 the set K ρ:= U ¯ ∖ N ρ ​ ( ∂ U) ∈ 𝒞 ⁡ ( U) K_{\rho}\!:=\overline{U}\setminus N_{\rho}(\partial U)\in\mathcal{C}(U) verifies U ∖ K ρ ⊂ N ρ ​ ( ∂ U) U\setminus K_{\rho}\subset N_{\rho}(\partial U) and, on the other hand (see Definition 1), Cycl G ​ ( ( U ∖ K ρ, X μ 0), X μ) ⩾ c \mathrm{Cycl}_{G}\big((U\setminus K_{\rho},X_{\mu_{0}}),X_{\mu}\big)\geqslant{c}. This means, recall Definition 1, that there exists L ρ ∈ 𝒞 ⁡ ( U ∖ K ρ) L_{\rho}\in\mathcal{C}(U\setminus K_{\rho}) for which Cycl G ​ ( ( L ρ, X μ 0), X μ) ⩾ c \mathrm{Cycl}_{G}\big((L_{\rho},X_{\mu_{0}}),X_{\mu}\big)\geqslant{c}, i.e., for all ε, δ > 0 \varepsilon,\delta>0 there exists μ ∈ B δ ​ ( μ 0) \mu\in B_{\delta}(\mu_{0}) such that X μ X_{\mu} has at least c {c} limit cycles inside N ε ​ ( L ρ) ⊂ N ε + ρ ​ ( ∂ U) N_{\varepsilon}(L_{\rho})\subset N_{\varepsilon+\rho}(\partial U). According to Definition 1 again, we conclude that Cycl G ​ ( ( ∂ U, X μ 0), X μ) ⩾ c \mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)\geqslant{c}. If Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big) is finite we can take c = Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) c=\underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big) to obtain that Cycl G ​ ( ( ∂ U, X μ 0), X μ) ⩾ Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) \mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)\geqslant\underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big), otherwise we easily deduce Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) = ∞ = Cycl G ​ ( ( ∂ U, X μ 0), X μ) \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)=\infty=\mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big).

###### Lemma 5.2.

If K ∈ 𝒞 ⁡ ( 𝕊 2) K\in\mathcal{C}(\mathbb{S}^{2}) then Cycl G ​ ( ( K, X μ 0), X μ) = Cycl ⁡ ( ( ℒ ⁡ ( K), X μ 0), X μ), \mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big)=\mathrm{Cycl}\big((\mathcal{L}(K),X_{\mu_{0}}),X_{\mu}\big), where ℒ ⁡ ( K) = ℒ ∩ 𝒞 ⁡ ( K) \mathcal{L}(K)=\mathcal{L}\cap\mathcal{C}(K).

By Remark 1, the set { γ ​ limit cycle of ​ X μ ​ contained in ​ N ε ​ ( K) } \{\gamma\text{ limit cycle of }X_{\mu}\text{ contained in }N_{\varepsilon}(K)\} contains

 | { γ limit cycle of X μ with d H ( γ, Γ) < ε for some Γ ∈ ℒ ( K) }. \{\gamma\text{ limit cycle of }X_{\mu}\text{ with }d_{H}(\gamma,\Gamma)<\varepsilon\text{ for some }\Gamma\in\mathcal{L}(K)\}. |  |

Accordingly, on account of Definitions 1 and 1, it follows that

 | Cycl G ​ ( ( K, X μ 0), X μ) ⩾ Cycl ⁡ ( ( ℒ ⁡ ( K), X μ 0), X μ). \mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big)\geqslant\mathrm{Cycl}\big((\mathcal{L}(K),X_{\mu_{0}}),X_{\mu}\big). |  |

Fix a natural number c ⩽ Cycl G ​ ( ( K, X μ 0), X μ) c\leqslant\mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big). Then, see Definition 1 again, for any n ∈ ℕ n\in\mathbb{N} there exists μ n ∈ B 1 / n ​ ( μ 0) \mu_{n}\in B_{1/n}(\mu_{0}) such that X μ n X_{\mu_{n}} has at least c c limit cycles γ n 1, …, γ n c \gamma_{n}^{1},\ldots,\gamma_{n}^{c} contained in N 1 / n ​ ( K) N_{1/n}(K). Since ( 𝒞 ⁡ ( 𝕊 2), d H) \big(\mathcal{C}(\mathbb{S}^{2}),d_{H}\big) is compact (see Remark 1 again), by taking a subsequence we can assume that γ n j → Γ j ∈ ℒ ⁡ ( K) \gamma_{n}^{j}\to\Gamma^{j}\in\mathcal{L}(K) as n → ∞ n\to\infty. Consequently, for each ε, δ > 0 \varepsilon,\delta>0, there exists n ∈ ℕ n\in\mathbb{N} such that μ n ∈ B δ ​ ( μ 0) \mu_{n}\in B_{\delta}(\mu_{0}) and d H ​ ( γ n j, Γ j) < ε d_{H}(\gamma_{n}^{j},\Gamma^{j})<\varepsilon. Therefore, see Definition 1, Cycl ⁡ ( ( ℒ ⁡ ( K), X μ 0), X μ) ⩾ c \mathrm{Cycl}\big((\mathcal{L}(K),X_{\mu_{0}}),X_{\mu}\big)\geqslant c. If Cycl G ​ ( ( K, X μ 0), X μ) \mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big) is finite then we can take c = Cycl G ​ ( ( K, X μ 0), X μ) c=\mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big) to conclude that Cycl ⁡ ( ( ℒ ⁡ ( K), X μ 0), X μ) ⩾ Cycl G ​ ( ( K, X μ 0), X μ) \mathrm{Cycl}\big((\mathcal{L}(K),X_{\mu_{0}}),X_{\mu}\big)\geqslant\mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big), and the result follows. Otherwise one can easily show that

 | Cycl G ​ ( ( K, X μ 0), X μ) = ∞ = Cycl ⁡ ( ( ℒ ⁡ ( K), X μ 0), X μ), \mathrm{Cycl}_{G}\big((K,X_{\mu_{0}}),X_{\mu}\big)=\infty=\mathrm{Cycl}\big((\mathcal{L}(K),X_{\mu_{0}}),X_{\mu}\big), |  |

and so the result follows as well.

Let { X μ } μ ∈ Λ \{X_{\mu}\}_{\mu\in\Lambda} be the whole quadratic family of vector fields and X μ 0 X_{\mu_{0}} the vector field ( 7) (\ref{DSq}) with ( a 0, b 0) ∈ { ( − 1, 1), ( − 1 2, 1 2), ( − 1 2, 3 2) } (a_{0},b_{0})\in\{(-1,1),(-\frac{1}{2},\frac{1}{2}),(-\frac{1}{2},\frac{3}{2})\}. Setting U = ℝ 2 ∖ { y = 0 } U=\mathbb{R}^{2}\setminus\{y=0\}, so that ∂ U = Γ u ∪ Γ ℓ \partial U=\Gamma_{u}\cup\Gamma_{\ell}, we get

 | Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) \displaystyle\underline{\mathrm{Cycl}}_{\,G}^{\,U}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big) | ⩽ ( 1) Cycl G ​ ( ( U, X μ 0), X μ) = ( 2) 2 < 3 ⩽ ( 3) Cycl ⁡ ( ( { Γ u, Γ ℓ }, X μ 0), X μ) \displaystyle\stackrel{{\scriptstyle(1)}}{{\leqslant}}\mathrm{Cycl}_{G}\big((U,X_{\mu_{0}}),X_{\mu}\big)\stackrel{{\scriptstyle(2)}}{{=}}2<3\stackrel{{\scriptstyle(3)}}{{\leqslant}}\mathrm{Cycl}\big((\{\Gamma_{u},\Gamma_{\ell}\},X_{\mu_{0}}),X_{\mu}\big) |  |

 |  | = ( 4) Cycl ⁡ ( ( ℒ ⁡ ( ∂ U), X μ 0), X μ) = ( 5) Cycl G ​ ( ( ∂ U, X μ 0), X μ). \displaystyle\stackrel{{\scriptstyle(4)}}{{=}}\mathrm{Cycl}\big((\mathcal{L}(\partial U),X_{\mu_{0}}),X_{\mu}\big)\stackrel{{\scriptstyle(5)}}{{=}}\mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big). |  |

The inequality ( 1) (1) follows from Definition 1 taking K = ∅ K=\emptyset. The equality ( 2) (2) for ( a 0, b 0) = ( − 1, 1) (a_{0},b_{0})=(-1,1) follows from [8, Theorem 11], for ( a 0, b 0) = ( − 1 2, 1 2) (a_{0},b_{0})=(-\frac{1}{2},\frac{1}{2}) follows from [24, Theorem 1.2] and for ( a 0, b 0) = ( − 1 2, 3 2) (a_{0},b_{0})=(-\frac{1}{2},\frac{3}{2}) is a consequence of the latter by applying Lemmas 3.1 and 4.1. The inequality ( 3) (3) follows from Theorem C. The equality ( 4) (4) is due to the fact that the only limit periodic sets inside ∂ U = Γ u ∪ Γ ℓ \partial U=\Gamma_{u}\cup\Gamma_{\ell} are Γ u \Gamma_{u} and Γ ℓ. \Gamma_{\ell}. Finally, the equality ( 5) (5) follows from Lemma 5.2. This proves the result.

We conclude the present section by resuming the remark that we made in the paragraph just after Definition 1. The following is the intrinsic notion of alien limit cycle for an unfolding of a polycycle that we propose:

Let { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} be a germ of an analytic family of vector fields on 𝕊 2 \mathbb{S}^{2} such that X μ 0 X_{\mu_{0}} has a polycycle Γ \Gamma with only a well-defined return map on one side, which is the identity. Assume moreover that Γ \Gamma does not contain any proper subset being a limit periodic set of the unfolding. Let U U be the connected component of 𝕊 2 ∖ Γ \mathbb{S}^{2}\setminus\Gamma containing the side of Γ \Gamma where the return map is defined. Then, if

 | Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) < Cycl G ​ ( ( ∂ U, X μ 0), X μ), \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)<\mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big), |  |

we say that an *alien limit cycle bifurcation*occurs at ∂ U = Γ \partial U=\Gamma from inside U U for { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}}. □ \square

In the above definition, the hypothesis that Γ \Gamma has a well-defined return map only on one side, together with the requirement that Γ \Gamma does not contain any proper subset being a limit periodic set of the unfolding, guarantee that Cycl G ​ ( ( ∂ U, X μ 0), X μ) \mathrm{Cycl}_{G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big) accounts for the limit cycles coming from U U only. On the other hand, if the return map is not the identity then Cycl ¯ G U ​ ( ( ∂ U, X μ 0), X μ) = 0 \underline{\mathrm{Cycl}}^{\,U}_{\,G}\big((\partial U,X_{\mu_{0}}),X_{\mu}\big)=0.

Next we particularize Definition 5 to the case of a 2-saddle cycle and show its relation with Melnikov functions. With this aim, let { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}} be a germ of an analytic family of vector fields on 𝕊 2 \mathbb{S}^{2} such that X μ 0 X_{\mu_{0}} has a hyperbolic 2 2 -saddle cycle Γ \Gamma homeomorphic to 𝕊 1 \mathbb{S}^{1} and with the return map being the identity. We assume moreover that at most one saddle connection in Γ \Gamma breaks when μ ≈ μ 0 \mu\approx\mu_{0}. Similarly as we do in Figure 7 we take a transversal section Σ 1 \Sigma_{1} in the unbroken connection and a transversal section Σ 2 \Sigma_{2} in the other one, and we consider the difference map 𝒟 ⁡ ( s, μ) \mathscr{D}(s;\mu) between the corresponding Dulac maps, which is defined on ( 0, s 0) (0,s_{0}). If f ⁡ ( s) f(s) is a smooth function on ( 0, s 0) (0,s_{0}) and I I is an interval inside ( 0, s 0) (0,s_{0}), we denote by Z I ​ ( f) Z_{I}(f) (respectively, Z I m ​ ( f) Z^{m}_{I}(f)) the number of zeros of f f in I I (respectively, counted with multiplicities). Then, following this notation, we have that

 | Cycl G ​ ( ( ∂ U, X μ 0), X μ) = Cycl ⁡ ( ( Γ, X μ 0), X μ) = inf ε, δ > 0 sup μ ∈ B δ ​ ( μ 0) Z ( 0, ε) ​ ( 𝒟 ⁡ ( ⋅, μ)) =: 𝒵, \mathrm{Cycl}_{G}((\partial U,X_{\mu_{0}}),X_{\mu})=\mathrm{Cycl}((\Gamma,X_{\mu_{0}}),X_{\mu})=\inf\limits_{\varepsilon,\delta>0}\sup\limits_{\mu\in B_{\delta}(\mu_{0})}Z_{(0,\varepsilon)}\big(\mathscr{D}(\cdot;\mu)\big)=:\mathcal{Z}, |  | (24) |

where the first equality follows by using Lemma 5.2 and the assumption that Γ \Gamma does not contain any proper subset being a limit periodic set of the unfolding. In the second equality we use that the limit cycles of X μ X_{\mu} which are Hausdorff close to Γ \Gamma correspond to small isolated zeros of the displacement function 𝒟 ⁡ ( s, μ). \mathscr{D}(s;\mu). On the other hand, for each analytic arc μ = ξ ⁡ ( ϵ) \mu=\xi(\epsilon) with ξ ⁡ ( 0) = μ 0 \xi(0)=\mu_{0} such that 𝒟 ⁡ ( s, ξ ⁡ ( ϵ)) ≢ 0 \mathscr{D}\big(s;\xi(\epsilon)\big)\not\equiv 0, we can take the Taylor’s expansion at ϵ = 0 \epsilon=0 and write 𝒟 ⁡ ( s, ξ ⁡ ( ϵ)) = ϵ k ξ ​ ( M ξ ​ ( s) + O ⁡ ( ϵ)) \mathscr{D}\big(s;\xi(\epsilon)\big)=\epsilon^{k_{\xi}}(M_{\xi}(s)+O(\epsilon)), where M ξ ​ ( s) M_{\xi}(s) is the first non-identically zero Melnikov function associated to the one-parameter unfolding { X ξ ⁡ ( ϵ) } ϵ ≈ 0 \{X_{\xi(\epsilon)}\}_{\epsilon\approx 0}. We then define

 | ℳ:= inf ε > 0 sup ξ ⁡ ( 0) = μ 0 Z ( 0, ε) m ​ ( M ξ), \mathcal{M}\!:=\inf\limits_{\varepsilon>0}\sup\limits_{\xi(0)=\mu_{0}}Z_{(0,\varepsilon)}^{m}(M_{\xi}), |  |

where the supremum ranges over all the analytic arcs μ = ξ ⁡ ( ϵ) \mu=\xi(\epsilon) with ξ ⁡ ( 0) = μ 0 \xi(0)=\mu_{0} such that 𝒟 ⁡ ( s, ξ ⁡ ( ϵ)) ≢ 0 \mathscr{D}\big(s;\xi(\epsilon)\big)\not\equiv 0. (We point out that here ε \varepsilon and ϵ \epsilon play different roles.)

###### Lemma 5.4.

Under the previous assumptions and notation, let U U be the connected component of 𝕊 2 ∖ Γ \mathbb{S}^{2}\setminus\Gamma where the return map of X μ 0 X_{\mu_{0}} is well defined and suppose that the boundary cyclicity of U U from inside is finite. If ℳ < 𝒵 \mathcal{M}<\mathcal{Z} then an alien limit cycle bifurcation occurs at ∂ U = Γ \partial U=\Gamma from inside U U for { X μ } μ ≈ μ 0 \{X_{\mu}\}_{\mu\approx\mu_{0}}.

To show the result we note that

 | Cycl ¯ G U ​ ( ( ∂ U CLOSE CLOSE, \displaystyle\underline{\mathrm{Cycl}}_{\,G}^{\,U}((\partial U, | OPEN OPEN X μ 0), X μ) = ( 1) inf K ∈ 𝒞 ⁡ ( U) Cycl G ​ ( ( U ∖ K, X μ 0), X μ) = ( 2) inf K ∈ 𝒞 ⁡ ( U) Cycl G ​ ( ( U ∖ K, X μ 0), X ξ K ​ ( ϵ)) \displaystyle X_{\mu_{0}}),X_{\mu})\stackrel{{\scriptstyle(1)}}{{=}}\inf_{K\in\mathcal{C}(U)}\mathrm{Cycl}_{\,G}\big((U\setminus K,X_{\mu_{0}}),X_{\mu}\big)\stackrel{{\scriptstyle(2)}}{{=}}\inf_{K\in\mathcal{C}(U)}\mathrm{Cycl}_{\,G}\big((U\setminus K,X_{\mu_{0}}),X_{\xi_{K}(\epsilon)}\big) |  |

 |  | ⩽ ( 3) inf K ∈ 𝒞 ⁡ ( U) Z ( 0, ε K) m ​ ( M ξ K) ⩽ ( 4) inf ε > 0 sup ξ ⁡ ( 0) = μ 0 Z ( 0, ε) m ​ ( M ξ) = ( 5) ℳ < 𝒵 = ( 6) Cycl G ​ ( ( ∂ U, X μ 0), X μ). \displaystyle\stackrel{{\scriptstyle(3)}}{{\leqslant}}\inf_{K\in\mathcal{C}(U)}Z^{m}_{(0,\varepsilon_{K})}\big(M_{\xi_{K}}\big)\stackrel{{\scriptstyle(4)}}{{\leqslant}}\inf\limits_{\varepsilon>0}\sup\limits_{\xi(0)=\mu_{0}}Z_{(0,\varepsilon)}^{m}(M_{\xi})\stackrel{{\scriptstyle(5)}}{{=}}\mathcal{M}<\mathcal{Z}\stackrel{{\scriptstyle(6)}}{{=}}\mathrm{Cycl}_{G}((\partial U,X_{\mu_{0}}),X_{\mu}). |  |

Here the equalities ( 1) (1) and ( 5) (5) follow by definition. The equality ( 2) (2) follows by the assumption that the boundary cyclicity of U U from inside is finite and applying [10, Theorem 1] to the period annulus U ∖ K U\setminus K for each fixed K ∈ 𝒞 ⁡ ( U) K\in\mathcal{C}(U). (It is clear that we can take K K to be an invariant closed disc of X μ 0 X_{\mu_{0}} without loss of generality.) The inequality ( 3) (3) is a consequence of the Weierstrass Preparation Theorem and ( 4) (4) is obvious because we take the supremum over all the analytic arcs instead of the ones given by the realization theorem of Gavrilov. Finally the equality ( 6) (6) follows from ( 24) (\ref{alien_eq2}).

This lemma is related with the approach made by Dumortier, Roussarie and collaborators in [2, 6, 4, 16]. Indeed, following our notation, they say that an alien limit cycle bifurcation occurs in case that ℳ 1 < 𝒵 \mathcal{M}_{1}<\mathcal{Z}, where ℳ 1 \mathcal{M}_{1} is defined as ℳ \mathcal{M} but taking the supremum only over all the radial arcs ξ \xi for which k ξ = 1 k_{\xi}=1. For other results related with alien limit cycles the reader is referred to the contributions of Han and collaborators in [30, 31, 33] and references therein.

## Appendix A The asymptotic expansion of the Dulac map and related results

In order to prove Theorems A and B we will appeal to some previous results from [19, 20, 21] about the asymptotic expansion of the Dulac map. For reader’s convenience we gather these results in Proposition A.4. To this end it is first necessary to introduce some new notation and definitions. For simplicity in the exposition, we use ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\} as a wild card in 𝒞 ϖ \mathscr{C}^{\varpi} for the smooth class 𝒞 ∞ \mathscr{C}^{\infty} and the analytic class 𝒞 ω \mathscr{C}^{\omega}.

Setting ν ^:= ( λ, ν) ∈ W ^:= ( 0, + ∞) × W \hat{\nu}\!:=(\lambda,\nu)\in\hat{W}\!:=(0,+\infty)\times W with W W an open set of ℝ N, \mathbb{R}^{N}, we consider the family of vector fields { X ν ^ } ν ^ ∈ W ^ \{X_{\hat{\nu}}\}_{{\hat{\nu}}\in\hat{W}} with

 | X ν ^ ( x 1, x 2) = x 1 P 1 ( x 1, x 2; ν ^) ∂ x 1 + x 2 P 2 ( x 1, x 2; ν ^) ∂ x 2 X_{\hat{\nu}}({x_{1}},{x_{2}})={x_{1}}P_{1}({x_{1}},{x_{2}};{\hat{\nu}})\partial_{x_{1}}+{x_{2}}P_{2}({x_{1}},{x_{2}};{\hat{\nu}})\partial_{x_{2}} |  | (25) |

where

- •

P 1 P_{1} and P 2 P_{2} belong to 𝒞 ϖ ​ ( 𝒰 × W ^) \mathscr{C}^{\varpi}(\mathscr{U}\!\times\!\hat{W}) for some open set 𝒰 \mathscr{U} of ℝ 2 \mathbb{R}^{2} containing the origin,

- •

P 1 ​ ( x 1, 0, ν ^) > 0 P_{1}({x_{1}},0;{\hat{\nu}})>0 and P 2 ​ ( 0, x 2, ν ^) < 0 P_{2}(0,{x_{2}};{\hat{\nu}})<0 for all ( x 1, 0), ( 0, x 2) ∈ 𝒰 ({x_{1}},0),(0,{x_{2}})\in\mathscr{U} and ν ^ ∈ W ^, {\hat{\nu}}\in\hat{W},

- •

λ = − P 2 ​ ( 0, 0, ν ^) P 1 ​ ( 0, 0, ν ^) \lambda=-\frac{P_{2}(0,0;\hat{\nu})}{P_{1}(0,0;\hat{\nu})}.

Thus, for all ν ^ ∈ W ^ \hat{\nu}\in\hat{W}, the origin is a hyperbolic saddle of X ν ^ X_{\hat{\nu}} with the separatrices lying in the axis. We point out that here the hyperbolicity ratio of the saddle is an independent parameter, although in the applications we will have λ = λ ⁡ ( ν) \lambda=\lambda(\nu). The reason for this is that the hyperbolicity ratio turns out to be the ruling parameter in our results and, besides, having it uncoupled from the rest of parameters simplifies the notation in the statements. Moreover, for i = 1, 2, i=1,2, we consider a 𝒞 ϖ \mathscr{C}^{\varpi} transverse section σ i: ( − ε, ε) × W ^ ⟶ Σ i {\sigma_{i}}\!:{(-\varepsilon,\varepsilon)\times\hat{W}}\longrightarrow{\Sigma_{i}} to X ν ^ X_{{\hat{\nu}}} at x i = 0 x_{i}=0 defined by

 | σ i ​ ( s, ν ^) = ( σ i ​ 1 ​ ( s, ν ^), σ i ​ 2 ​ ( s, ν ^)) \sigma_{i}(s;{\hat{\nu}})=\bigl(\sigma_{i1}(s;{\hat{\nu}}),\sigma_{i2}(s;{\hat{\nu}})\bigr) |  |

such that σ 1 ​ ( 0, ν ^) ∈ { ( 0, x 2); x 2 > 0 } \sigma_{1}(0,{\hat{\nu}})\in\{(0,x_{2});x_{2}>0\} and σ 2 ​ ( 0, ν ^) ∈ { ( x 1, 0); x 1 > 0 } \sigma_{2}(0,{\hat{\nu}})\in\{(x_{1},0);x_{1}>0\} for all ν ^ ∈ W ^. {\hat{\nu}}\in\hat{W}. We denote the Dulac map of X ν ^ X_{\hat{\nu}} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} by D ⁡ ( ⋅, ν ^) D(\,\cdot\,;{\hat{\nu}}), see Figure 9.

Figure 9: Definition of the Dulac map D ⁡ ( ⋅, ν ^) D(\,\cdot\,;{\hat{\nu}}), where φ ⁡ ( t, p, ν ^) \varphi(t,p;{\hat{\nu}}) is the solution of X ν ^ X_{\hat{\nu}} passing through the point p ∈ 𝒰 p\in\mathscr{U} at time t = 0. t=0.

The asymptotic expansion of D ⁡ ( s, ν ^) D(s;\hat{\nu}) at s = 0 s=0 consists of a remainder and a principal part. The principal part is given in a monomial scale that contains a deformation of the logarithm, the so-called Ecalle-Roussarie compensator, whereas the remainder has good flatness properties with respect to the parameters. We next give precise definitions of these key notions.

The function defined for s > 0 s>0 and α ∈ ℝ \alpha\in\mathbb{R} by means of

 | ω ⁡ ( s, α) = { s − α − 1 α if α ≠ 0, − log ⁡ s if α = 0, \omega(s;\alpha)\>=\left\{\begin{array}[]{ll}\frac{s^{-\alpha}-1}{\alpha}&\text{if $\alpha\neq 0,$}\\[2.0pt] -\log s&\text{if $\alpha=0,$}\end{array}\right. |  |

is called the *Ecalle-Roussarie compensator*. □ \square

Consider K ∈ ℤ ≥ 0 ∪ { ∞ } K\in\mathbb{Z}_{\geq 0}\cup\{\infty\} and an open subset U ⊂ W ^ ⊂ ℝ N + 1. U\subset\hat{W}\subset\mathbb{R}^{N+1}. We say that a function ψ ⁡ ( s, ν ^) \psi(s;{\hat{\nu}}) belongs to the class 𝒞 s > 0 K ​ ( U) \mathscr{C}^{K}_{s>0}(U), respectively 𝒞 s = 0 K ​ ( U) \mathscr{C}^{K}_{s=0}(U), if there exist an open neighbourhood Ω \Omega of

 | { ( s, ν ^) ∈ ℝ N + 2; s = 0, ν ^ ∈ U } = { 0 } × U \{(s,{\hat{\nu}})\in\mathbb{R}^{N+2};s=0,{\hat{\nu}}\in U\}=\{0\}\times U |  |

in ℝ N + 2 \mathbb{R}^{N+2} such that ( s, ν ^) ↦ ψ ⁡ ( s, ν ^) (s,{\hat{\nu}})\mapsto\psi(s;{\hat{\nu}}) is 𝒞 K \mathscr{C}^{K} on Ω ∩ ( ( 0, + ∞) × U) \Omega\cap\big((0,+\infty)\times U\big), respectively Ω. \Omega. □ \square

Consider K ∈ ℤ ≥ 0 ∪ { ∞ } K\in\mathbb{Z}_{\geq 0}\cup\{\infty\} and an open subset U ⊂ W ^ ⊂ ℝ N + 1. U\subset\hat{W}\subset\mathbb{R}^{N+1}. Given L ∈ ℝ L\in\mathbb{R} and ν ^ 0 ∈ U {\hat{\nu}}_{0}\in U, we say that a function ψ ⁡ ( s, ν ^) ∈ 𝒞 s > 0 K ​ ( U) \psi(s;{\hat{\nu}})\in\mathscr{C}^{K}_{s>0}(U) is *( L, K) (L,K) -flat with respect to s s at ν ^ 0 {\hat{\nu}}_{0}*, and we write ψ ∈ ℱ L K ​ ( ν ^ 0) \psi\in\mathcal{F}_{L}^{K}({\hat{\nu}}_{0}), if for each ℓ = ( ℓ 0, …, ℓ N + 1) ∈ ℤ ≥ 0 N + 2 \ell=(\ell_{0},\ldots,\ell_{N+1})\in\mathbb{Z}_{\geq 0}^{N+2} with | ℓ | = ℓ 0 + … + ℓ N + 1 ⩽ K |\ell|=\ell_{0}+\ldots+\ell_{N+1}\leqslant K there exist a neighbourhood V V of ν ^ 0 {\hat{\nu}}_{0} and C, s 0 > 0 C,s_{0}>0 such that

 | | ∂ | ℓ | ψ ⁡ ( s, ν ^) ∂ s ℓ 0 ∂ ν ^ 1 ℓ 1 ⋯ ∂ ν ^ N + 1 ℓ N + 1 | ⩽ C ​ s L − ℓ 0 ​ for all s ∈ ( 0, s 0) and ν ^ ∈ V. \left|\frac{\partial^{|\ell|}\psi(s;{\hat{\nu}})}{\partial s^{\ell_{0}}\partial{\hat{\nu}}_{1}^{\ell_{1}}\cdots\partial{\hat{\nu}}_{N+1}^{\ell_{N+1}}}\right|\leqslant Cs^{L-\ell_{0}}\text{ for all $s\in(0,s_{0})$ and ${\hat{\nu}}\in V$.} |  |

If W W is a (not necessarily open) subset of U U then define ℱ L K ​ ( W):= ⋂ ν ^ 0 ∈ W ℱ L K ​ ( ν ^ 0). \mathcal{F}_{L}^{K}(W)\!:=\bigcap_{{\hat{\nu}}_{0}\in W}\mathcal{F}_{L}^{K}({\hat{\nu}}_{0}). □ \square

Apart from the remainder and the monomial order, the most important ingredient for our purposes is the explicit expression of the coefficients in the asymptotic expansion. In order to give them we introduce next some additional notation, where for the sake of shortness the dependence on ν ^ = ( λ, ν) {\hat{\nu}}=(\lambda,\nu) is omitted. We define the functions:

 | L 1 ( u):= exp ∫ 0 u ( P 1 ​ ( 0, z) P 2 ​ ( 0, z) + 1 λ) d ​ z z L 2 ( u):= exp ∫ 0 u ( P 2 ​ ( z, 0) P 1 ​ ( z, 0) + λ) d ​ z z M 1 ​ ( u):= L 1 ​ ( u) ​ ∂ 1 ( P 1 P 2) ​ ( 0, u) M 2 ​ ( u):= L 2 ​ ( u) ​ ∂ 2 ( P 2 P 1) ​ ( u, 0) \begin{array}[]{ll}\displaystyle L_{1}(u)\!:=\exp\int_{0}^{u}\left(\frac{P_{1}(0,z)}{P_{2}(0,z)}+\frac{1}{\lambda}\right)\frac{dz}{z}&\displaystyle L_{2}(u)\!:=\exp\int_{0}^{u}\left(\frac{P_{2}(z,0)}{P_{1}(z,0)}+{\lambda}\right)\frac{dz}{z}\\[15.0pt] \displaystyle M_{1}(u)\!:=L_{1}(u)\partial_{1}\!\left(\frac{P_{1}}{P_{2}}\right)(0,u)&\displaystyle M_{2}(u)\!:=L_{2}(u)\partial_{2}\!\left(\frac{P_{2}}{P_{1}}\right)(u,0)\\[15.0pt] \end{array} |  | (26) |

On the other hand, for shortness as well, we use the compact notation σ i ​ j ​ k \sigma_{ijk} for the k k th derivative at s = 0 s=0 of the j j th component of σ i ​ ( s, ν ^) \sigma_{i}(s;{\hat{\nu}}), i.e.,

 | σ i ​ j ​ k ​ ( ν ^):= ∂ s k σ i ​ j ​ ( 0, ν ^). \sigma_{ijk}({\hat{\nu}})\!:=\partial^{k}_{s}\sigma_{ij}(0;{\hat{\nu}}). |  |

Taking this notation into account we also introduce the following real values, where once again we omit the dependence on ν ^ {\hat{\nu}}:

 | S 1:= σ 112 2 ​ σ 111 − σ 121 σ 120 ​ ( P 1 P 2) ​ ( 0, σ 120) − σ 111 L 1 ​ ( σ 120) ​ M ^ 1 ​ ( 1 / λ, σ 120) S 2:= σ 222 2 ​ σ 221 − σ 211 σ 210 ​ ( P 2 P 1) ​ ( σ 210, 0) − σ 221 L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210) S 3:= σ 221 ​ σ 210 L 2 ​ ( σ 210) ​ M 2 ′ ​ ( 0). \begin{array}[]{l}\displaystyle S_{1}\!:=\frac{\sigma_{112}}{2\sigma_{111}}-\frac{\sigma_{121}}{\sigma_{120}}\left(\frac{P_{1}}{P_{2}}\right)\!(0,\sigma_{120})-\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{M}_{1}(1/\lambda,\sigma_{120})\\[20.0pt] \displaystyle S_{2}\!:=\frac{\sigma_{222}}{2\sigma_{221}}-\frac{\sigma_{211}}{\sigma_{210}}\left(\frac{P_{2}}{P_{1}}\right)\!(\sigma_{210},0)-{\frac{\sigma_{221}}{L_{2}(\sigma_{210})}}\hat{M}_{2}(\lambda,\sigma_{210})\\[20.0pt] \displaystyle S_{3}\!:=\frac{\sigma_{221}\sigma_{210}}{L_{2}(\sigma_{210})}M_{2}^{\prime}(0).\end{array} |  | (27) |

Here M ^ i \hat{M}_{i} stands for a sort of incomplete Mellin transform of M i M_{i} that will be defined by Proposition A.5 below. The next proposition gathers the essential results in [21] that we shall need to prove the first main result in the present paper.

###### Proposition A.4.

Let D ⁡ ( s, ν ^) D(s;{\hat{\nu}}) be the Dulac map of the hyperbolic saddle ( 25) (\ref{X}) from Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2} and consider any λ 0 > 0. \lambda_{0}>0. Then D ⁡ ( s, ν ^) = Δ 0 ​ ( ν ^) ​ s λ + ℱ ℓ ∞ ​ ( { λ 0 } × W) D(s;{\hat{\nu}})=\Delta_{0}({\hat{\nu}})s^{\lambda}+\mathcal{F}_{\ell}^{\infty}(\{\lambda_{0}\}\times W) for any ℓ ∈ [λ 0, min ⁡ ( 2 ​ λ 0, λ 0 + 1)) {\ell}\in\big[\lambda_{0},\min(2\lambda_{0},\lambda_{0}+1)\big) where Δ 0 \Delta_{0} is a strictly positive 𝒞 ϖ \mathscr{C}^{\varpi} function on W ^ \hat{W} and

 | Δ 0 ​ ( ν ^) = σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120) ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ. \Delta_{0}(\hat{\nu})=\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}. |  |

Moreover,

1. ( 1) (1)

If λ 0 > 1 \lambda_{0}>1 then D ⁡ ( s, ν ^) = Δ 0 ​ ( ν ^) ​ s λ + Δ 1 ​ ( ν ^) ​ s λ + 1 + ℱ ℓ ∞ ​ ( { λ 0 } × W) D(s;{\hat{\nu}})=\Delta_{0}({\hat{\nu}})s^{\lambda}+\Delta_{1}({\hat{\nu}})s^{\lambda+1}+\mathcal{F}_{\ell}^{\infty}(\{\lambda_{0}\}\times W) for any ℓ ∈ [λ 0 + 1, min ( λ 0 + 2, 2 λ 0)) {\ell}\in\big[\lambda_{0}+1,\min(\lambda_{0}+2,2\lambda_{0})\big) where Δ 1 \Delta_{1} is a 𝒞 ϖ \mathscr{C}^{\varpi} function in a neighbourhood of { λ 0 } × W \{\lambda_{0}\}\times W and Δ 1 ​ ( ν ^) = Δ 0 ​ λ ​ S 1. \Delta_{1}(\hat{\nu})=\Delta_{0}\lambda S_{1}.

2. ( 2) (2)

If λ 0 < 1 \lambda_{0}<1 then D ⁡ ( s, ν ^) = Δ 0 ​ ( ν ^) ​ s λ + Δ 2 ​ ( ν ^) ​ s 2 ​ λ + ℱ ℓ ∞ ​ ( { λ 0 } × W) D(s;{\hat{\nu}})=\Delta_{0}({\hat{\nu}})s^{\lambda}+\Delta_{2}({\hat{\nu}})s^{2\lambda}+\mathcal{F}_{\ell}^{\infty}(\{\lambda_{0}\}\times W) for any ℓ ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big) where Δ 2 \Delta_{2} is a 𝒞 ϖ \mathscr{C}^{\varpi} function in a neighbourhood of { λ 0 } × W \{\lambda_{0}\}\times W and Δ 2 ​ ( ν ^) = − Δ 0 2 ​ S 2 \Delta_{2}(\hat{\nu})=-\Delta_{0}^{2}S_{2}.

3. ( 3) (3)

If λ 0 = 1 \lambda_{0}=1 then D ⁡ ( s, ν ^) = Δ 0 ​ ( ν ^) ​ s λ + Δ 3 ​ ( ν ^) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ 4 ​ ( ν ^) ​ s λ + 1 + ℱ ℓ ∞ ​ ( { 1 } × W) D(s;{\hat{\nu}})=\Delta_{0}({\hat{\nu}})s^{\lambda}+\Delta_{3}({\hat{\nu}})s^{\lambda+1}\omega(s;1-\lambda)+\Delta_{4}(\hat{\nu})s^{\lambda+1}+\mathcal{F}_{\ell}^{\infty}(\{1\}\times W) for any ℓ ∈ [2, 3) {\ell}\in[2,3) where Δ 3 \Delta_{3} and Δ 4 \Delta_{4} are 𝒞 ϖ \mathscr{C}^{\varpi} functions in a neighbourhood of { 1 } × W \{1\}\times W and Δ 3 ​ ( ν ^) | λ = 1 = Δ 0 2 ​ S 3 | λ = 1. \Delta_{3}(\hat{\nu})|_{\lambda=1}=\Delta_{0}^{2}S_{3}|_{\lambda=1}.

For the ease of the reader, let us explain regarding this result that the structure of the asymptotic expansion follows from [21, Theorem 4.1], whereas the properties (i.e., regularity and explicit expression) of the coefficients follow by applying Theorem A, Corollary B and Proposition 3.2 of the same paper. Furthermore, the flatness ℓ \ell of the remainder can range in a certain interval depending on λ 0. \lambda_{0}. The left endpoint of this interval is only given for completeness to guarantee that all the monomials in the principal part are relevant (i.e., they cannot be included in the remainder). The important information about the flatness is given by the right endpoint. A key tool in order to give a closed expression of the coefficients Δ i \Delta_{i} is the use of a sort of incomplete Mellin transform, which is accurately defined in the next result. For a proof of this result the reader is referred to [21, Appendix B].

###### Proposition A.5.

Let us consider an open interval I I of ℝ \mathbb{R} containing x = 0 x=0 and an open subset U U of ℝ M \mathbb{R}^{M}.

1. ( a) (a)

Given f ⁡ ( x, υ) ∈ 𝒞 ∞ ​ ( I × U) f(x;{\upsilon})\in\mathscr{C}^{\infty}(I\times U), there exits a unique f ^ ​ ( α, x, υ) ∈ 𝒞 ∞ ​ ( ( ℝ ∖ ℤ ⩾ 0) × I × U) \hat{f}(\alpha,x;{\upsilon})\in\mathscr{C}^{\infty}((\mathbb{R}\setminus\mathbb{Z}_{\geqslant 0})\times I\times U) such that

 | x ​ ∂ x f ^ ​ ( α, x, υ) − α ​ f ^ ​ ( α, x, υ) = f ⁡ ( x, υ). x\partial_{x}\hat{f}({\alpha},x;{\upsilon})-\alpha\hat{f}({\alpha},x;{\upsilon})=f(x;{\upsilon}). |  |

2. ( b) (b)

If x ∈ I ∖ { 0 } x\in I\setminus\{0\} then ∂ x ( f ^ ​ ( α, x, υ) ​ | x | − α) = f ⁡ ( x, υ) ​ | x | − α x \partial_{x}(\hat{f}({\alpha},x;{\upsilon})|x|^{-\alpha})=f(x;{\upsilon})\frac{|x|^{-\alpha}}{x} and, taking any k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0} with k > α k>\alpha,

 | f ^ ​ ( α, x, υ) = ∑ i = 0 k − 1 ∂ x i f ⁡ ( 0, υ) i! ​ ( i − α) ​ x i + | x | α ​ ∫ 0 x ( f ⁡ ( s, υ) − T 0 k − 1 ​ f ​ ( s, υ)) ​ | s | − α ​ d ​ s s, \hat{f}(\alpha,x;{\upsilon})=\sum_{i=0}^{k-1}\frac{\partial_{x}^{i}f(0;{\upsilon})}{i!(i-\alpha)}x^{i}+|x|^{\alpha}\int_{0}^{x}\!\left(f(s;{\upsilon})-T_{0}^{k-1}f(s;{\upsilon})\right)|s|^{-\alpha}\frac{ds}{s}, |  |

where T 0 k ​ f ​ ( x, υ) = ∑ i = 0 k 1 i! ​ ∂ x i f ⁡ ( 0, υ) ​ x i T_{0}^{k}f(x;{\upsilon})=\sum_{i=0}^{k}\frac{1}{i!}\partial_{x}^{i}f(0;{\upsilon})x^{i} is the k k -th degree Taylor polynomial of f ⁡ ( x, υ) f(x;{\upsilon}) at x = 0 x=0.

3. ( c) (c)

For each ( i 0, x 0, υ 0) ∈ ℤ ⩾ 0 × I × W (i_{0},x_{0},{\upsilon}_{0})\in\mathbb{Z}_{\geqslant 0}\times I\times W the function ( α, x, υ) ↦ ( i 0 − α) ​ f ^ ​ ( α, x, υ) (\alpha,x,{\upsilon})\mapsto(i_{0}-\alpha)\hat{f}(\alpha,x;{\upsilon}) extends 𝒞 ∞ \mathscr{C}^{\infty} at ( i 0, x 0, υ 0) (i_{0},x_{0},{\upsilon}_{0}) and, moreover, it tends to 1 i 0! ​ ∂ x i 0 f ⁡ ( 0, υ 0) ​ x 0 i 0 \frac{1}{i_{0}!}\partial_{x}^{i_{0}}f(0;{\upsilon}_{0})x_{0}^{i_{0}} as ( α, x, υ) → ( i 0, x 0, υ 0). (\alpha,x,{\upsilon})\to(i_{0},x_{0},{\upsilon}_{0}).

4. ( d) (d)

If f ⁡ ( x, υ) f(x;{\upsilon}) is analytic on I × U I\times U then f ^ ​ ( α, x, υ) \hat{f}(\alpha,x;{\upsilon}) is analytic on ( ℝ ∖ ℤ ⩾ 0) × I × U (\mathbb{R}\setminus\mathbb{Z}_{\geqslant 0})\times I\times U. Finally, for each ( α 0, x 0, υ 0) ∈ ℤ ⩾ 0 × I × U (\alpha_{0},x_{0},{\upsilon}_{0})\in\mathbb{Z}_{\geqslant 0}\times I\times U the function ( α, x, υ) ↦ ( α 0 − α) ​ f ^ ​ ( α, x, υ) (\alpha,x,{\upsilon})\mapsto(\alpha_{0}-\alpha)\hat{f}(\alpha,x;{\upsilon}) extends analytically to ( α 0, x 0, υ 0) (\alpha_{0},x_{0},{\upsilon}_{0}).

On account of this result for each M i ​ ( u, ν ^) M_{i}(u;\hat{\nu}) in ( 26) (\ref{def_fun}) we have that ( α, u, ν ^) ↦ M ^ i ​ ( α, u, ν ^) (\alpha,u;\hat{\nu})\mapsto\hat{M}_{i}(\alpha,u;\hat{\nu}) is a well defined meromorphic function with poles only at α ∈ ℤ ≥ 0 \alpha\in\mathbb{Z}_{\geq 0}. Accordingly, see ( 27) (\ref{def_S}), M ^ 1 ​ ( 1 / λ, σ 120) \hat{M}_{1}(1/\lambda,\sigma_{120}) and M ^ 2 ​ ( λ, σ 210) \hat{M}_{2}(\lambda,\sigma_{210}) are the values (depending on ν ^ \hat{\nu}) that we obtain by taking M ^ 1 ​ ( α, u, ν ^) \hat{M}_{1}(\alpha,u;\hat{\nu}) with α = 1 / λ \alpha=1/\lambda and u = σ 120 ​ ( ν ^) u=\sigma_{120}(\hat{\nu}) and by taking M ^ 2 ​ ( α, u, ν ^) \hat{M}_{2}(\alpha,u;\hat{\nu}) with α = λ \alpha=\lambda and u = σ 210 ​ ( ν ^), u=\sigma_{210}(\hat{\nu}), respectively.

The next result (see [20, Lemma 4.3]) is addressed to study the case in which the separatrices depicted in Figure 9 are not straight lines.

###### Lemma A.6.

Consider a 𝒞 ∞ \mathscr{C}^{\infty} family { X μ } μ ∈ ℝ N \{X_{\mu}\}_{\mu\in\mathbb{R}^{N}} of planar vector fields defined in some open set W W of ℝ 2 \mathbb{R}^{2}. Let us fix some μ 0 ∈ ℝ N \mu_{0}\in\mathbb{R}^{N} and assume that, for all μ ≈ μ 0, \mu\approx\mu_{0}, X μ X_{\mu} has a hyperbolic saddle point at p μ ∈ W p_{\mu}\in W with ( ( global)) stable and unstable separatrices S μ + S_{\mu}^{+} and S μ − S_{\mu}^{-}, respectively. Consider two closed connected arcs ℓ ± ⊂ S μ 0 ± \ell^{\pm}\subset S^{\pm}_{\mu_{0}}, having both an endpoint at p μ 0 p_{\mu_{0}}. In case of a homoclinic connection ( ( i.e., 𝑂𝑃𝐸𝑁 S μ 0 + = S μ 0 −) S^{+}_{\mu_{0}}=S^{-}_{\mu_{0}}) we require additionally that ℓ + ∩ ℓ − = { p μ 0 } \ell^{+}\cap\ell^{-}=\{p_{\mu_{0}}\}. Then there exists a neighbourhood V V of ( ℓ + ∪ ℓ −) × { μ 0 } (\ell^{+}\cup\ell^{-})\times\{\mu_{0}\} in ℝ 2 × ℝ N \mathbb{R}^{2}\times\mathbb{R}^{N} and a 𝒞 ∞ \mathscr{C}^{\infty} diffeomorphism Φ: V → Φ ⁡ ( V) ⊂ ℝ 2 × ℝ N \Phi:V\rightarrow\Phi(V)\subset\mathbb{R}^{2}\times\mathbb{R}^{N} with Φ ⁡ ( x, y, μ) = ( ϕ μ ​ ( x, y), μ) \Phi(x,y,\mu)=(\phi_{\mu}(x,y),\mu) such that

 | Φ ( ( S μ + × { μ }) ∩ V) ⊂ { x = 0 } × { μ } and Φ ( ( S μ − × { μ }) ∩ V) ⊂ { y = 0 } × { μ }. \Phi((S_{\mu}^{+}\times\{\mu\})\cap V)\subset\{x=0\}\times\{\mu\}\text{ and }\Phi((S_{\mu}^{-}\times\{\mu\})\cap V)\subset\{y=0\}\times\{\mu\}. |  |

In other words, ( ϕ μ) ⋆ ​ ( X μ) = X ^ μ (\phi_{\mu})_{\star}(X_{\mu})=\hat{X}_{\mu} where X ^ μ ( x, y) = x P ( x, y; μ) ∂ x + y Q ( x, y; μ) ∂ y, \hat{X}_{\mu}(x,y)=xP(x,y;\mu)\partial_{x}+yQ(x,y;\mu)\partial_{y}, with P, Q ∈ 𝒞 ∞ ​ ( Φ ⁡ ( V)). P,Q\in\mathscr{C}^{\infty}(\Phi(V)).

Next result gathers some general properties (see [19, Lemma A.3]) with regard to operations between functions in ℱ L K ​ ( W) \mathcal{F}_{L}^{K}(W) with L ∈ ℝ L\in\mathbb{R}.

###### Lemma A.7.

Let U U and U ′ U^{\prime} be open sets of ℝ N \mathbb{R}^{N} and ℝ N ′ \mathbb{R}^{N^{\prime}} respectively and consider W ⊂ U W\subset U and W ′ ⊂ U ′. W^{\prime}\subset U^{\prime}. Then the following holds:

1. ( a) (a)

ℱ L K ​ ( W) ⊂ ℱ L K ​ ( W ^) \mathcal{F}_{L}^{K}(W)\subset\mathcal{F}_{L}^{K}(\hat{W}) for any W ^ ⊂ W \hat{W}\subset W and ⋂ n ℱ L K ​ ( W n) = ℱ L K ​ ( ⋃ n W n) \bigcap_{n}\mathcal{F}_{L}^{K}(W_{n})=\mathcal{F}_{L}^{K}\left(\bigcup_{n}W_{n}\right).

2. ( b) (b)

ℱ L K ​ ( W) ⊂ ℱ L K ​ ( W × W ′) \mathcal{F}_{L}^{K}(W)\subset\mathcal{F}_{L}^{K}(W\times W^{\prime}).

3. ( c) (c)

𝒞 K ​ ( U) ⊂ 𝒞 s = 0 K ​ ( U) ⊂ ℱ 0 K ​ ( W) \mathscr{C}^{K}(U)\subset\mathscr{C}^{K}_{s=0}(U)\subset\mathcal{F}_{0}^{K}(W).

4. ( d) (d)

If K ⩾ K ′ K\geqslant K^{\prime} and L ⩾ L ′ L\geqslant L^{\prime} then ℱ L K ​ ( W) ⊂ ℱ L ′ K ′ ​ ( W) \mathcal{F}_{L}^{K}(W)\subset\mathcal{F}_{L^{\prime}}^{K^{\prime}}(W).

5. ( e) (e)

ℱ L K ​ ( W) \mathcal{F}_{L}^{K}(W) is closed under addition.

6. ( f) (f)

If f ∈ ℱ L K ​ ( W) f\in\mathcal{F}_{L}^{K}(W) and ν ∈ ℤ ≥ 0 N + 1 \nu\in\mathbb{Z}_{\geq 0}^{N+1} with | ν | ⩽ K |\nu|\leqslant K then ∂ ν f ∈ ℱ L − ν 0 K − | ν | ​ ( W) \partial^{\nu}f\in\mathcal{F}_{L-\nu_{0}}^{K-|\nu|}(W).

7. ( g) (g)

ℱ L K ​ ( W) ⋅ ℱ L ′ K ​ ( W) ⊂ ℱ L + L ′ K ​ ( W) \mathcal{F}_{L}^{K}(W)\cdot\mathcal{F}_{L^{\prime}}^{K}(W)\subset\mathcal{F}_{L+L^{\prime}}^{K}(W).

8. ( h) (h)

Assume that ϕ: U ′ ⟶ U {\phi}\!:{U^{\prime}}\longrightarrow{U} is a 𝒞 K \mathscr{C}^{K} function with ϕ ⁡ ( W ′) ⊂ W \phi(W^{\prime})\subset W and let us take g ∈ ℱ L ′ K ​ ( W ′) g\in\mathcal{F}_{L^{\prime}}^{K}(W^{\prime}) with L ′ > 0 L^{\prime}>0 and verifying g ⁡ ( s, η) > 0 g(s;\eta)>0 for all η ∈ W ′ \eta\in W^{\prime} and s > 0 s>0 small enough. Consider also any f ∈ ℱ L K ​ ( W) f\in\mathcal{F}_{L}^{K}(W). Then h ⁡ ( s, η):= f ⁡ ( g ⁡ ( s, η), ϕ ⁡ ( η)) h(s;\eta)\!:=f(g(s;\eta);\phi(\eta)) is a well-defined function that belongs to ℱ L ​ L ′ K ​ ( W ′) \mathcal{F}_{LL^{\prime}}^{K}(W^{\prime}).

From Definition A it follows easily that if ∂ ν f ∈ ℱ L − ν 0 K ​ ( W) \partial^{\nu}f\in\mathcal{F}_{L-\nu_{0}}^{K}(W) for all ν ∈ ℤ ≥ 0 N + 1 \nu\in\mathbb{Z}^{N+1}_{\geq 0} with | ν | ⩽ 1 |\nu|\leqslant 1 then f ∈ ℱ L K + 1 ​ ( W). f\in\mathcal{F}_{L}^{K+1}(W). This is a sort of converse for assertion ( f) (f) in Lemma A.7. □ \square

###### Lemma A.9.

Let us consider f ⁡ ( s, μ) ∈ ℱ δ ∞ ​ ( μ 0) f(s;\mu)\in\mathcal{F}_{\delta}^{\infty}(\mu_{0}) with δ > 0 \delta>0 and define ψ ⁡ ( s, μ) = ( s ⁡ ( 1 + f ⁡ ( s, μ)), μ) \psi(s,\mu)=\big(s(1+f(s;\mu)),\mu\big) for 0 < s ≪ 1 0<s\ll 1 and μ ≈ μ 0. \mu\approx\mu_{0}. Then ψ \psi extends to a local 𝒞 1 \mathscr{C}^{1} diffeomorphism on a neighbourhood of ( 0, μ 0) (0,\mu_{0}). Moreover its inverse, for 0 < s ≪ 1 0<s\ll 1 and μ ≈ μ 0, \mu\approx\mu_{0}, writes as ψ − 1 ​ ( s, μ) = ( s ⁡ ( 1 + g ⁡ ( s, μ)), μ) \psi^{-1}(s,\mu)=\big(s(1+g(s;\mu)),\mu\big) with g ∈ ℱ δ ∞ ​ ( μ 0) g\in\mathcal{F}_{\delta}^{\infty}(\mu_{0}).

Since f ⁡ ( s, μ) ∈ ℱ δ ∞ ​ ( μ 0) f(s;\mu)\in\mathcal{F}_{\delta}^{\infty}(\mu_{0}) with δ > 0 \delta>0 then s ​ f ​ ( s, μ) ∈ ℱ 1 + δ ∞ ​ ( μ 0) sf(s;\mu)\in\mathcal{F}_{1+\delta}^{\infty}(\mu_{0}) extends to a 𝒞 1 \mathscr{C}^{1} function on some neighbourhood of ( 0, μ 0) (0,\mu_{0}) by [19, Lemma A.1]. Thus F ⁡ ( s, u, μ):= s ⁡ ( 1 + f ⁡ ( s, μ)) − u F(s,u,\mu)\!:=s(1+f(s;\mu))-u is 𝒞 1 \mathscr{C}^{1} at ( 0, 0, μ 0) (0,0,\mu_{0}), F ⁡ ( 0, 0, μ 0) = 0 F(0,0,\mu_{0})=0 and ∂ s F ⁡ ( 0, 0, μ 0) = 1 \partial_{s}F(0,0,\mu_{0})=1, and by applying the Implicit Function Theorem there exists a unique 𝒞 1 \mathscr{C}^{1} function σ ⁡ ( u, μ) \sigma(u,\mu) on a neighbourhood ( − ε, ε) × U (-\varepsilon,\varepsilon)\times U of ( 0, μ 0) (0,\mu_{0}) such that σ ⁡ ( 0, μ 0) = 0 \sigma(0,\mu_{0})=0 and F ⁡ ( σ ⁡ ( u, μ), u, μ) ≡ 0, F(\sigma(u,\mu),u,\mu)\equiv 0, i.e., σ ⁡ ( u, μ) ​ ( 1 + f ⁡ ( σ ⁡ ( u, μ), μ)) = u \sigma(u,\mu)(1+f(\sigma(u,\mu);\mu))=u. Moreover the uniqueness implies that σ ⁡ ( 0, μ) = 0 \sigma(0,\mu)=0 for all μ ∈ U. \mu\in U.

We claim that σ ∈ ⋂ K = 0 ∞ ℱ 1 K ​ ( μ 0) = ℱ 1 ∞ ​ ( μ 0) \sigma\in\bigcap_{K=0}^{\infty}\mathcal{F}_{1}^{K}(\mu_{0})=\mathcal{F}_{1}^{\infty}(\mu_{0}). The proof follows by induction on K ∈ ℤ ≥ 0. K\in\mathbb{Z}_{\geq 0}. Indeed, due to σ ⁡ ( 0, μ) = 0 \sigma(0,\mu)=0 for all μ ∈ U, \mu\in U, we can write

 | σ ⁡ ( u, μ) = u ​ ∫ 0 1 ∂ u σ ⁡ ( t ​ u, μ) ​ 𝑑 t ∈ u ​ 𝒞 u = 0 0 ​ ( U) ⊂ ℱ 1 0 ​ ( μ 0), \sigma(u,\mu)=u\int_{0}^{1}\partial_{u}\sigma(tu;\mu)dt\in u\mathscr{C}^{0}_{u=0}(U)\subset\mathcal{F}_{1}^{0}(\mu_{0}), |  |

where the inclusion follows by ( c) (c) in Lemma A.7. Since f ∈ 𝒞 s > 0 ∞ ​ ( U) f\in\mathscr{C}_{s>0}^{\infty}(U), by applying the Implicit Function Theorem to the equality F ⁡ ( s, u, μ) = 0 F(s,u,\mu)=0 at the points ( s, u, μ) = ( σ ⁡ ( u ⋆, μ ⋆), u ⋆, μ ⋆) (s,u,\mu)=(\sigma(u_{\star},\mu_{\star}),u_{\star},\mu_{\star}) with ( u ⋆, μ ⋆) ∈ ( 0, ε) × U (u_{\star},\mu_{\star})\in(0,\varepsilon)\times U and taking the uniqueness of σ \sigma into account, we deduce that σ ∈ 𝒞 s > 0 ∞ ​ ( U) \sigma\in\mathscr{C}_{s>0}^{\infty}(U). Furthermore

 |  | ∂ u σ ⁡ ( u, μ) = − ( ∂ u F ∂ s F) ​ ( σ ⁡ ( u, μ), u, μ) = 1 1 + f 1 ​ ( σ ⁡ ( u, μ), μ) \displaystyle\partial_{u}\sigma(u,\mu)=-\left(\frac{\partial_{u}F}{\partial_{s}F}\right)\!\big(\sigma(u,\mu),u,\mu\big)=\frac{1}{1+f_{1}(\sigma(u,\mu);\mu)} |  |

and |

 |  | ∂ μ i σ ⁡ ( u, μ) = − ( ∂ μ i F ∂ s F) ​ ( σ ⁡ ( u, μ), u, μ) = − σ ⁡ ( u, μ) ​ ∂ μ i f ⁡ ( σ ⁡ ( u, μ), μ) 1 + f 1 ​ ( σ ⁡ ( u, μ), μ), \displaystyle\partial_{\mu_{i}}\sigma(u,\mu)=-\left(\frac{\partial_{\mu_{i}}F}{\partial_{s}F}\right)\!\big(\sigma(u,\mu),u,\mu\big)=-\frac{\sigma(u,\mu)\partial_{\mu_{i}}f(\sigma(u,\mu);\mu)}{1+f_{1}(\sigma(u,\mu);\mu)}, |  |

where f 1:= f + s ​ ∂ s f ∈ ℱ δ ∞ ​ ( μ 0) f_{1}\!:=f+s\partial_{s}f\in\mathcal{F}_{\delta}^{\infty}(\mu_{0}) by ( f) (f) in Lemma A.7. On account of these two expressions, and by applying Lemma A.7 once again, we can assert that if σ ∈ ℱ 1 K ​ ( μ 0) \sigma\in\mathcal{F}_{1}^{K}(\mu_{0}) then ∂ u σ ∈ ℱ 0 K ​ ( μ 0) \partial_{u}\sigma\in\mathcal{F}_{0}^{K}(\mu_{0}) and ∂ μ i σ ∈ ℱ 1 K ​ ( μ 0), \partial_{\mu_{i}}\sigma\in\mathcal{F}_{1}^{K}(\mu_{0}), and consequently, see Remark A, σ ∈ ℱ 1 K + 1 ​ ( μ 0) \sigma\in\mathcal{F}_{1}^{K+1}(\mu_{0}). Accordingly, since we already proved that σ ∈ ℱ 1 0 ​ ( μ 0) \sigma\in\mathcal{F}_{1}^{0}(\mu_{0}), we conclude that σ ∈ ℱ 1 ∞ ​ ( μ 0) \sigma\in\mathcal{F}_{1}^{\infty}(\mu_{0}) and f ⁡ ( σ ⁡ ( u, μ), μ) ∈ ℱ δ ∞ ​ ( μ 0) f(\sigma(u,\mu);\mu)\in\mathcal{F}_{\delta}^{\infty}(\mu_{0}) by induction. Hence

 | σ ⁡ ( u, μ) = u 1 + f ⁡ ( σ ⁡ ( u, μ), μ) = u 1 + ℱ δ ∞ ​ ( μ 0) = u ⁡ ( 1 + g ⁡ ( u, μ)) \sigma(u,\mu)=\frac{u}{1+f(\sigma(u,\mu);\mu)}=\frac{u}{1+\mathcal{F}_{\delta}^{\infty}(\mu_{0})}=u(1+g(u,\mu)) |  |

with g ∈ ℱ δ ∞ ​ ( μ 0) g\in\mathcal{F}_{\delta}^{\infty}(\mu_{0}), thanks to Lemma A.7 again. This concludes the proof of the result.

The following result is a kind of division theorem among the class of flat functions and its proof can be found in [22, Lemma 4.1].

###### Lemma A.10.

Let us fix L ⩾ 0 L\geqslant 0 and n ∈ ℕ. n\in\mathbb{N}. If f ⁡ ( s, μ 1, …, μ n) ∈ ℱ L ∞ ​ ( 0 n) f(s;\mu_{1},\ldots,\mu_{n})\in\mathcal{F}^{\infty}_{L}(0_{n}) verifies that

 | f ⁡ ( s, μ 1, …, μ k − 1, 0, …, 0) ≡ 0 ​, for some k ∈ { 1, 2, …, n }, f(s;\mu_{1},\ldots,\mu_{k-1},0,\ldots,0)\equiv 0\text{, for some $k\in\{1,2,\ldots,n\}$,} |  |

then there exist f k, …, f n ∈ ℱ L ∞ ​ ( 0 n) f_{k},\ldots,f_{n}\in\mathcal{F}_{L}^{\infty}(0_{n}) such that f = ∑ i = k n μ i ​ f i f=\sum_{i=k}^{n}\mu_{i}f_{i}.

We give at this point the precise definition of independence of functions that we use in this paper and a subsequent result addressed to obtain lower bounds for the number of bifurcating zeros.

Let W W be a subset of ℝ N \mathbb{R}^{N} (not necessarily open) and consider the functions g i: W ⟶ ℝ {g_{i}}\!:{W}\longrightarrow{\mathbb{R}} for i = 1, 2, …, k i=1,2,\ldots,k. The *real variety*V ⁡ ( g 1, g 2, …, g k) ⊂ W V(g_{1},g_{2},\ldots,g_{k})\subset W is defined to be the set of μ ∈ W \mu\in W such that g i ​ ( μ) = 0 g_{i}(\mu)=0 for i = 1, 2, …, k. i=1,2,\ldots,k. We say that g 1, g 2, …, g k g_{1},g_{2},\ldots,g_{k} are *independent*at μ ⋆ ∈ V ⁡ ( g 1, g 2, …, g k) \mu_{\star}\in V(g_{1},g_{2},\ldots,g_{k}) if the following conditions are satisfied:

1. ( 1) (1)

Every neighbourhood of μ ⋆ \mu_{\star} contains two points μ 1, μ 2 ∈ V ⁡ ( g 1, …, g k − 1) \mu_{1},\mu_{2}\in V(g_{1},\ldots,g_{k-1}) such that g k ​ ( μ 1) ​ g k ​ ( μ 2) < 0 g_{k}(\mu_{1})g_{k}(\mu_{2})<0 (if k = 1 k=1 then we set V ⁡ ( g 1, …, g k − 1) = V ⁡ ( 0) = W V(g_{1},\ldots,g_{k-1})=V(0)=W for this to hold).

2. ( 2) (2)

The varieties V ⁡ ( g 1, …, g i) V(g_{1},\ldots,g_{i}), 2 ⩽ i ⩽ k − 1, 2\leqslant i\leqslant k-1, are such that if μ 0 ∈ V ⁡ ( g 1, …, g i) \mu_{0}\in V(g_{1},\ldots,g_{i}) and g i + 1 ​ ( μ 0) ≠ 0 g_{i+1}(\mu_{0})\neq 0, then every neighbourhood of μ 0 \mu_{0} contains a point μ ∈ V ⁡ ( g 1, …, g i − 1) \mu\in V(g_{1},\ldots,g_{i-1}) such that g i ​ ( μ) ​ g i + 1 ​ ( μ 0) < 0. g_{i}(\mu)g_{i+1}(\mu_{0})<0.

3. ( 3) (3)

If μ 0 ∈ V ⁡ ( g 1) \mu_{0}\in V(g_{1}) and g 2 ​ ( μ 0) ≠ 0 g_{2}(\mu_{0})\neq 0, then every open neighbourhood of μ 0 \mu_{0} contains a point μ ∈ W \mu\in W such that g 1 ​ ( μ) ​ g 2 ​ ( μ 0) < 0. g_{1}(\mu)g_{2}(\mu_{0})<0.

It is clear that if W W is an open subset of ℝ N \mathbb{R}^{N} and g i ∈ 𝒞 1 ​ ( W) g_{i}\in\mathscr{C}^{1}(W) for i = 1, 2, …, k i=1,2,\ldots,k then a sufficient condition for g 1, g 2, …, g k g_{1},g_{2},\ldots,g_{k} to be independent at μ ⋆ \mu_{\star} is that the gradients ∇ g 1 ​ ( μ ⋆), ∇ g 2 ​ ( μ ⋆) ​ …, ∇ g k ​ ( μ ⋆) \nabla g_{1}(\mu_{\star}),\nabla g_{2}(\mu_{\star})\dots,\nabla g_{k}(\mu_{\star}) are linearly independent vectors of ℝ N. \mathbb{R}^{N}. □ \square

###### Proposition A.12.

Let W W be a subset of ℝ N \mathbb{R}^{N} ( ( not necessarily open)) and consider

 | F ⁡ ( s, μ) = ∑ i = 1 n δ i ​ ( μ) ​ f i ​ ( s, μ) + f n + 1 ​ ( s, μ), F(s;\mu)=\sum_{i=1}^{n}\delta_{i}(\mu)f_{i}(s;\mu)+f_{n+1}(s;\mu), |  |

where f i: ( 0, ε) × W ⟶ ℝ {f_{i}}\!:{(0,\varepsilon)\!\times\!W}\longrightarrow{\mathbb{R}} and δ i: W ⟶ ℝ {\delta_{i}}\!:{W}\longrightarrow{\mathbb{R}} are continuous functions ( ( with respect to the induced topology)). If μ ⋆ ∈ V ⁡ ( δ 1, δ 2, …, δ n) ⊂ W \mu_{\star}\in V(\delta_{1},\delta_{2},\ldots,\delta_{n})\subset W satisfies

1. ( a) (a)

F ⁡ ( s, μ ⋆) F(s;\mu_{\star}) is not identically zero on ( 0, ρ) (0,\rho) for every ρ ∈ ( 0, ε), \rho\in(0,\varepsilon),

2. ( b) (b)

f i ​ ( s, μ) > 0 f_{i}(s;\mu)>0, 1 ⩽ i ⩽ n, 1\leqslant i\leqslant n, for all ( s, μ) (s,\mu) in a neighbourhood of ( 0, μ ⋆) (0,\mu_{\star}) in ( 0, ε) × W (0,\varepsilon)\!\times\!W,

3. ( c) (c)

lim s → 0 f i + 1 ​ ( s, μ) f i ​ ( s, μ) = 0 \lim_{s\to 0}\frac{f_{i+1}(s;\mu)}{f_{i}(s;\mu)}=0, 1 ⩽ i ⩽ n, 1\leqslant i\leqslant n, for every μ \mu in a neighbourhood of μ ⋆ \mu_{\star} in W W, and

4. ( d) (d)

δ 1, δ 2, …, δ n \delta_{1},\delta_{2},\ldots,\delta_{n} are independent at μ ⋆, \mu_{\star},

then for every neighbourhood V V of μ ⋆ \mu_{\star} in W W and ρ > 0 \rho>0 there exists μ 0 ∈ V \mu_{0}\in V such that F ⁡ ( s, μ 0) F(s;\mu_{0}) has at least n n different zeros inside the interval ( 0, ρ). (0,\rho).

Fix any ρ > 0 \rho>0 and any neighbourhood U U of μ ⋆ {{\mu}}_{\star} in W W. Then, by the assumption ( a) (a), there exists s 1 ∈ ( 0, ρ) s_{1}\in(0,\rho) such that F ⁡ ( s 1, μ ⋆) = f n + 1 ​ ( s 1, μ ⋆) ≠ 0. F(s_{1};{{\mu}}_{\star})=f_{n+1}(s_{1};{{\mu}}_{\star})\neq 0. Suppose for instance that F ⁡ ( s 1, μ ⋆) > 0. F(s_{1};{{\mu}}_{\star})>0. Then, on account of ( 1) (1) in Definition A, we can take μ 1 ∈ U ∩ V ⁡ ( δ 1, δ 2, …, δ n − 1) {{\mu}}_{1}\in U\cap V(\delta_{1},\delta_{2},\ldots,\delta_{n-1}) such that δ n ​ ( μ 1) < 0 \delta_{n}({{\mu}}_{1})<0 and close enough to μ ⋆ {{\mu}}_{\star} so that, by continuity, F ⁡ ( s 1, μ 1) > 0. F(s_{1};{{\mu}}_{1})>0. Observe that

 | F ⁡ ( s, μ 1) = δ n ​ ( μ 1) ​ f n ​ ( s, μ 1) + f n + 1 ​ ( s, μ 1). F(s;{{\mu}}_{1})=\delta_{n}({{\mu}}_{1})f_{n}(s;{{\mu}}_{1})+f_{n+1}(s;{{\mu}}_{1}). |  |

Thus, by ( b) (b) and ( c) (c), lim s → 0 F ⁡ ( s, μ 1) f n ​ ( s, μ 1) = δ n ​ ( μ 1) < 0 \lim_{s\to 0}\frac{F(s;{{\mu}}_{1})}{f_{n}(s;{{\mu}}_{1})}=\delta_{n}({{\mu}}_{1})<0 and we can take s 2 ∈ ( 0, s 1) s_{2}\in(0,s_{1}) such that F ⁡ ( s 2, μ 1) < 0 F(s_{2};{{\mu}}_{1})<0. Next, thanks to ( 2) (2) in Definition A, we can choose μ 2 ∈ U ∩ V ⁡ ( δ 1, δ 2, …, δ n − 2) {{\mu}}_{2}\in U\cap V(\delta_{1},\delta_{2},\ldots,\delta_{n-2}) with δ n − 1 ​ ( μ 2) > 0 \delta_{n-1}({{\mu}}_{2})>0 and close enough to μ 1 {{\mu}}_{1} so that F ⁡ ( s 1, μ 2) > 0 F(s_{1};{{\mu}}_{2})>0 and F ⁡ ( s 2, μ 2) < 0 F(s_{2};{{\mu}}_{2})<0. Note that

 | F ⁡ ( s, μ 2) = δ n − 1 ​ ( μ 2) ​ f n − 1 ​ ( s, μ 2) + δ n ​ ( μ 2) ​ f n ​ ( s, μ 2) + f n + 1 ​ ( s, μ 2). F(s;{{\mu}}_{2})=\delta_{n-1}({{\mu}}_{2})f_{n-1}(s;{{\mu}}_{2})+\delta_{n}({{\mu}}_{2})f_{n}(s;{{\mu}}_{2})+f_{n+1}(s;{{\mu}}_{2}). |  |

Consequently, by ( b) (b) and ( c) (c), lim s → 0 F ⁡ ( s, μ 2) f n − 1 ​ ( s, μ 2) = δ n − 1 ​ ( μ 2) > 0 \lim_{s\to 0}\frac{F(s;{{\mu}}_{2})}{f_{n-1}(s;{{\mu}}_{2})}=\delta_{n-1}({{\mu}}_{2})>0 and we can choose s 3 ∈ ( 0, s 2) s_{3}\in(0,s_{2}) such that F ⁡ ( s 3, μ 2) > 0. F(s_{3};{{\mu}}_{2})>0. Next we take μ 3 ∈ U ∩ V ⁡ ( δ 1, δ 2, …, δ n − 3) {{\mu}}_{3}\in U\cap V(\delta_{1},\delta_{2},\ldots,\delta_{n-3}) with δ n − 2 ​ ( μ 3) < 0 \delta_{n-2}({{\mu}}_{3})<0 and close enough to μ 2 {{\mu}}_{2} so that F ⁡ ( s 1, μ 3) > 0 F(s_{1};{{\mu}}_{3})>0, F ⁡ ( s 2, μ 3) < 0 F(s_{2};{{\mu}}_{3})<0 and F ⁡ ( s 3, μ 3) > 0 F(s_{3};{{\mu}}_{3})>0. We repeat this process n − 2 n-2 times after which we find a parameter μ n + 1 ∈ U {{\mu}}_{n+1}\in U and 0 < s n + 1 < s n < … < s 2 < s 1 < ρ 0<s_{n+1}<s_{n}<\ldots<s_{2}<s_{1}<\rho, such that ( − 1) i + 1 ​ F ​ ( s i, μ n + 1) > 0 (-1)^{i+1}F(s_{i};{{\mu}}_{n+1})>0 for all i = 1, 2, …, n + 1. i=1,2,\ldots,n+1. By applying Bolzano’s theorem we can assert the existence of at least n n different zeros of F ⁡ ( ⋅, μ n + 1) F(\,\cdot\,;{{\mu}}_{n+1}) inside the interval ( 0, ρ). (0,\rho). This concludes the proof of the result.

## Appendix B Deferred proofs

In this section, we collect the longest and most technical proofs.

### B.1 Proof of Theorem 2.1

We shall study first the Dulac map D + ​ ( ⋅, μ) D_{+}(\,\cdot\,;\mu) of X μ X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2}. For convenience we introduce auxiliary transverse sections Σ 1 η \Sigma_{1}^{\eta} and Σ 2 η \Sigma_{2}^{\eta} parametrized by σ 1 η ​ ( s) = ( η s, 1 s) \sigma_{1}^{\eta}(s)=(\frac{\eta}{s},\frac{1}{s}) and σ 2 η ​ ( s) = ( η, s) \sigma_{2}^{\eta}(s)=(\eta,s) with η ≈ 0 \eta\approx 0, respectively. On the other hand, setting ℓ α:= x + α ⁡ ( y + 1) \ell_{\alpha}\!:=x+\alpha(y+1), we perform the projective change of coordinates ( x 1, x 2) = ϕ ⁡ ( x, y, α):= ( 1 ℓ α, y ℓ α) (x_{1},x_{2})=\phi(x,y;\alpha)\!:=(\frac{1}{\ell_{\alpha}},\frac{y}{\ell_{\alpha}}) to the vector field X μ X_{\mu}, that recall is given by

 | { x ˙ = y ​ f ​ ( x, y, μ) + g ⁡ ( x, μ), y ˙ = y ​ q ​ ( x, y, μ). \left\{\!\begin{array}[]{l}\dot{x}=yf(x,y;\mu)+g(x;\mu),\\[2.0pt] \dot{y}=yq(x,y;\mu).\end{array}\right. |  |

In doing so we obtain that

 | ϕ ( ⋅; α) ⋆ X μ = 1 x 1 n ( x 1 P ¯ 1 ( x 1, x 2; μ, α) ∂ x 1 + x 2 P ¯ 2 ( x 1, x 2; μ, α) ∂ x 2), {\phi(\,\cdot\,;\alpha)}_{\star}X_{\mu}=\frac{1}{x_{1}^{n}}\left(x_{1}\bar{P}_{1}(x_{1},x_{2};\mu,\alpha)\partial_{x_{1}}+x_{2}\bar{P}_{2}(x_{1},x_{2};\mu,\alpha)\partial_{x_{2}}\right), |  |

where one can verify that

 | P 1 ​ ( x 1, x 2, μ) \displaystyle\textstyle P_{1}(x_{1},x_{2};\mu) | := P ¯ 1 ​ ( x 1, x 2, μ, 0) = − x 2 ​ x 1 n ​ f ​ ( 1 x 1, x 2 x 1) − x 1 n + 1 ​ g ​ ( 1 x 1) \displaystyle\!:=\bar{P}_{1}(x_{1},x_{2};\mu,0)=\textstyle-x_{2}x_{1}^{n}f\left(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\right)-x_{1}^{n+1}g\left(\frac{1}{x_{1}}\right) |  | (28) |

and |

 | P 2 ​ ( x 1, x 2, μ) \displaystyle\textstyle P_{2}(x_{1},x_{2};\mu) | := P ¯ 2 ​ ( x 1, x 2, μ, 0) = − x 2 ​ x 1 n ​ f ​ ( 1 x 1, x 2 x 1) − x 1 n + 1 ​ g ​ ( 1 x 1) + x 1 n ​ q ​ ( 1 x 1, x 2 x 1). \displaystyle\!:=\bar{P}_{2}(x_{1},x_{2};\mu,0)=\textstyle-x_{2}x_{1}^{n}f\left(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\right)-x_{1}^{n+1}g\left(\frac{1}{x_{1}}\right)+x_{1}^{n}q\left(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\right). |  | (29) |

Let us note at this point, see ( 2) (\ref{K}), that

 | P 2 ​ ( x 1, x 2, μ) P 1 ​ ( x 1, x 2, μ) = 1 − x ​ q ​ ( x, y) y ​ f ​ ( x, y) + g ⁡ ( x) | ( x, y) = ( 1 x 1, x 2 x 1) = K ⁡ ( x 1, x 2). \frac{P_{2}(x_{1},x_{2};\mu)}{P_{1}(x_{1},x_{2};\mu)}=\left.1-\frac{xq(x,y)}{yf(x,y)+g(x)}\right|_{(x,y)=\left(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\right)}=K(x_{1},x_{2}). |  | (30) |

The origin ( x 1, x 2) = ( 0, 0) (x_{1},x_{2})=(0,0) is a hyperbolic saddle of x 1 ​ ϕ ⋆ ​ ( X μ, α) x_{1}\phi_{\star}(X_{\mu};\alpha) with hyperbolicity ratio equal to

 | λ ⁡ ( μ) = − K ⁡ ( 0, 0, μ) = − 1 + q n ​ ( 1, 0) g n + 1. \lambda(\mu)=-K(0,0;\mu)=-1+\frac{q_{n}(1,0)}{g_{n+1}}. |  |

By introducing α \alpha and η \eta (that will make easier the forthcoming computations) we shall work in an extended parameter space μ ¯:= ( μ, α, η) \bar{\mu}\!:=(\mu,\alpha,\eta) with the admissibility conditions Σ i η ⊂ { ℓ α > 0 } \Sigma_{i}^{\eta}\subset\{\ell_{\alpha}>0\} for i = 1, 2 i=1,2. Let D ¯ ​ ( ⋅, μ, α, η) \bar{D}(\,\cdot\,;\mu,\alpha,\eta) be the Dulac map of X ¯ μ ¯:= x 1 ​ ϕ ​ ( ⋅, α) ⋆ ​ X μ \bar{X}_{\bar{\mu}}\!:=x_{1}{\phi(\,\cdot\,;\alpha)}_{\star}X_{\mu} from Σ 1 η \Sigma_{1}^{\eta} to Σ 2 η \Sigma_{2}^{\eta}. The key point is that, by construction, D ¯ ​ ( ⋅, μ, α, η) \bar{D}(\,\cdot\,;\mu,\alpha,\eta) does not depend on α \alpha and that D ¯ ​ ( ⋅, μ, α, 0) = D + ​ ( ⋅, μ). \bar{D}(\,\cdot\,;\mu,\alpha,0)=D_{+}(\,\cdot\,;\mu).

Let us fix any admissible α 0 \alpha_{0} and η 0 \eta_{0}. By applying Proposition A.4 to the analytic family of vector fields

 | X ¯ μ ¯ = x 1 P ¯ 1 ( x 1, x 2; μ, α) ∂ x 1 + x 2 P ¯ 2 ( x 1, x 2; μ, α) ∂ x 2 \bar{X}_{\bar{\mu}}=x_{1}\bar{P}_{1}(x_{1},x_{2};\mu,\alpha)\partial_{x_{1}}+x_{2}\bar{P}_{2}(x_{1},x_{2};\mu,\alpha)\partial_{x_{2}} |  |

at μ ¯ 0 = ( μ 0, α 0, η 0) \bar{\mu}_{0}=(\mu_{0},\alpha_{0},\eta_{0}) we can assert that

 | D ¯ ​ ( s, μ ¯) = Δ ¯ 0 ​ ( μ ¯) ​ s λ + { Δ ¯ 1 ​ ( μ ¯) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ ¯ 0) if λ 0 > 1, Δ ¯ 2 ​ ( μ ¯) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ ¯ 0) if λ 0 < 1, Δ ¯ 3 ​ ( μ ¯) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ ¯ 4 ​ ( μ ¯) ​ s λ + 1 + ℱ ℓ 3 ∞ ​ ( μ ¯ 0) if λ 0 = 1, \bar{D}(s;{\bar{\mu}})=\bar{\Delta}_{0}({\bar{\mu}})s^{\lambda}+\left\{\begin{array}[]{ll}\bar{\Delta}_{1}({\bar{\mu}})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\bar{\mu}_{0})&\text{ if $\lambda_{0}>1,$}\\[10.0pt] \bar{\Delta}_{2}({\bar{\mu}})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\bar{\mu}_{0})&\text{ if $\lambda_{0}<1,$}\\[10.0pt] \bar{\Delta}_{3}({\bar{\mu}})s^{\lambda+1}\omega(s;1-\lambda)+\bar{\Delta}_{4}(\bar{\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{3}}^{\infty}(\bar{\mu}_{0})&\text{ if $\lambda_{0}=1,$}\end{array}\right. |  |

for any ℓ 1 ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {\ell_{1}}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big), ℓ 2 ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell_{2}}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big) and ℓ 3 ∈ [2, 3) \ell_{3}\in[2,3), respectively.

We remark that λ 0 = λ ⁡ ( μ 0) = − K ⁡ ( 0, 0, μ) \lambda_{0}=\lambda(\mu_{0})=-K(0,0;\mu) because, although the new vector field X ¯ μ ¯ \bar{X}_{\bar{\mu}} depends on α \alpha, the hyperbolicity ratio of the saddle does not. We only need to compute the coefficients of the asymptotic development for η = 0 \eta=0 and to this aim notice that

 | Δ i + ​ ( μ):= Δ ¯ i ​ ( μ, α, 0) = lim η → 0 + Δ ¯ i ​ ( μ, α, η) = lim η → 0 + Δ ¯ i ​ ( μ, 0, η), \Delta_{i}^{+}(\mu)\!:=\bar{\Delta}_{i}(\mu,\alpha,0)=\lim_{\eta\to 0^{+}}\bar{\Delta}_{i}(\mu,\alpha,\eta)=\lim_{\eta\to 0^{+}}\bar{\Delta}_{i}(\mu,0,\eta), |  |

where in the third equality we use that the coefficients do not depend on α. \alpha. So it suffices to perform all the computations with α = 0 \alpha=0. The parametrisations of the auxiliary transverse sections Σ 1 η \Sigma_{1}^{\eta} and Σ 2 η \Sigma_{2}^{\eta} in coordinates ( x 1, x 2) (x_{1},x_{2}) for α = 0 \alpha=0 are σ 1 ​ ( s) = ( s η, 1 η) \sigma_{1}(s)=(\frac{s}{\eta},\frac{1}{\eta}) and σ 2 ​ ( s) = ( 1 η, s η) \sigma_{2}(s)=(\frac{1}{\eta},\frac{s}{\eta}) respectively, so that σ i ​ j ​ k = 1 η \sigma_{ijk}=\frac{1}{\eta} for ( i, j, k) ∈ { ( 1, 1, 1), ( 1, 2, 0), ( 2, 1, 0), ( 2, 2, 1) } (i,j,k)\in\{(1,1,1),(1,2,0),(2,1,0),(2,2,1)\}. Taking this into account, by applying Proposition A.4,

 | Δ ¯ 0 ​ ( μ, 0, η) = exp ⁡ ( ∫ 0 1 / η ( P 2 ​ ( z, 0) P 1 ​ ( z, 0) + λ − λ ​ P 1 ​ ( 0, z) P 2 ​ ( 0, z) − 1) ​ d ​ z z), \bar{\Delta}_{0}(\mu,0,\eta)=\exp\left(\int_{0}^{1/\eta}\left(\frac{P_{2}(z,0)}{P_{1}(z,0)}+{\lambda}-\lambda\frac{P_{1}(0,z)}{P_{2}(0,z)}-1\right)\frac{dz}{z}\right), |  |

where

 | P 2 ​ ( z, 0) P 1 ​ ( z, 0) = 1 − q ⁡ ( 1 / z, 0) z ​ g ​ ( 1 / z) ​ and ​ P 1 ​ ( 0, z) P 2 ​ ( 0, z) = 1 + q n ​ ( 1, z) z ​ f n ​ ( 1, z) + g n + 1 − q n ​ ( 1, z) = 1 + q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z). \frac{P_{2}(z,0)}{P_{1}(z,0)}=1-\frac{q(1/z,0)}{zg(1/z)}\;\text{ and }\;\frac{P_{1}(0,z)}{P_{2}(0,z)}=1+\frac{q_{n}(1,z)}{zf_{n}(1,z)+g_{n+1}-q_{n}(1,z)}=1+\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}. |  |

Consequently

 | Δ 0 + ​ ( μ) = Δ ¯ 0 ​ ( μ, α, 0) = lim η → 0 + Δ ¯ 0 ​ ( μ, 0, η) \displaystyle\Delta_{0}^{+}(\mu)=\bar{\Delta}_{0}(\mu,\alpha,0)=\lim_{\eta\to 0^{+}}\bar{\Delta}_{0}(\mu,0,\eta) | = exp ( − ∫ 0 + ∞ ( q ⁡ ( 1 / z, 0) z ​ g ​ ( 1 / z) + λ q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z)) d ​ z z) \displaystyle=\exp\left(-\int_{0}^{+\infty}\left(\frac{q(1/z,0)}{zg(1/z)}+\lambda\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}\right)\frac{dz}{z}\right) |  |

 |  | = exp ( − ∫ 0 + ∞ ( q ⁡ ( w, 0) g ⁡ ( w) + λ q n ​ ( w, 1) ℓ n + 1 ​ ( w, 1)) d w). \displaystyle=\exp\left(-\int_{0}^{+\infty}\left(\frac{q(w,0)}{g(w)}+\lambda\frac{q_{n}(w,1)}{{\ell_{n+1}}(w,1)}\right)dw\right). |  | (31) |

In the third equality we apply the Dominated Convergence Theorem [28, Theorem 11.30] taking into account that the integrand does not grow faster than z − 2 z^{-2} at infinity, which follows by the assumptions H1 and H2. Moreover, in the last equality, we perform the change of coordinates w = 1 / z w=1/z and take advantage of the homogeneity of the functions q n q_{n} and ℓ n + 1. {\ell_{n+1}}.

Next, we compute Δ ¯ 2 ​ ( μ, α, 0) \bar{\Delta}_{2}(\mu,\alpha,0) under the assumption λ 0 < 1 \lambda_{0}<1. By Proposition A.4, Δ ¯ 2 = − ( Δ ¯ 0) 2 ​ S 2 \bar{\Delta}_{2}=-(\bar{\Delta}_{0})^{2}S_{2} with

 | S 2 = σ 222 2 ​ σ 221 − σ 211 σ 210 ​ P 2 P 1 ​ ( σ 210, 0) − σ 221 L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210) = − 1 / η L 2 ​ ( 1 / η) ​ M ^ 2 ​ ( λ, 1 / η), S_{2}=\frac{\sigma_{222}}{2\sigma_{221}}-\frac{\sigma_{211}}{\sigma_{210}}\frac{P_{2}}{P_{1}}(\sigma_{210},0)-\frac{\sigma_{221}}{L_{2}(\sigma_{210})}\hat{M}_{2}(\lambda,\sigma_{210})=-\frac{1/\eta}{L_{2}(1/\eta)}\hat{M}_{2}(\lambda,1/\eta), |  |

where, see ( 30) (\ref{K_teo1}) and ( 26) (\ref{def_fun}), M 2 ​ ( u) = L 2 ​ ( u) ​ ∂ 2 K ⁡ ( u, 0) M_{2}(u)=L_{2}(u)\partial_{2}K(u,0) with

 | L 2 ( u) = exp ∫ 0 u ( K ( z, 0) + λ) d ​ z z L_{2}(u)=\exp\int_{0}^{u}\big(K(z,0)+{\lambda}\big)\frac{dz}{z} |  |

and we take σ 2 ​ ( s) = ( 1 η, s η) \sigma_{2}(s)=(\frac{1}{\eta},\frac{s}{\eta}) into account. To perform the limit of S 2 S_{2} as η → 0 + \eta\to 0^{+} we need to study the growth of the functions that are involved. With this aim observe that, since λ ⁡ ( μ) < 1 \lambda(\mu)<1 for μ ≈ μ 0 \mu\approx\mu_{0}, we can take k = 1 k=1 in ( b) (b) of Proposition A.5 to get

 | M ^ 2 ​ ( λ, 1 / η) = M 2 ​ ( 0) − λ + η − λ ​ ∫ 0 1 / η ( M 2 ​ ( u) − M 2 ​ ( 0)) ​ u − λ ​ d ​ u u. \hat{M}_{2}(\lambda,1/\eta)=\frac{M_{2}(0)}{-\lambda}+\eta^{-\lambda}\int_{0}^{1/\eta}(M_{2}(u)-M_{2}(0))u^{-\lambda}\frac{du}{u}. |  | (32) |

Setting f ~ ​ ( x 1, x 2) = x 1 n ​ f ​ ( 1 x 1, x 2 x 1) \tilde{f}(x_{1},x_{2})=x_{1}^{n}f\big(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\big), q ~ ​ ( x 1, x 2) = x 1 n ​ q ​ ( 1 x 1, x 2 x 1) \tilde{q}(x_{1},x_{2})=x_{1}^{n}q\big(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\big) and g ~ ​ ( x 1) = x 1 n + 1 ​ g ​ ( 1 x 1) \tilde{g}(x_{1})=x_{1}^{n+1}g\big(\frac{1}{x_{1}}\big), from ( 28) (\ref{defP1}) and ( 29) (\ref{defP2}),

 | ∂ 2 K ⁡ ( u, 0) = ∂ 2 ( P 2 P 1) ​ ( u, 0) = q ~ ​ ( u, 0) ​ f ~ ​ ( u, 0) − ∂ 2 q ~ ​ ( u, 0) ​ g ~ ​ ( u) g ~ ​ ( u) 2. \partial_{2}K(u,0)=\partial_{2}\left(\frac{P_{2}}{P_{1}}\right)(u,0)=\frac{\tilde{q}(u,0)\tilde{f}(u,0)-\partial_{2}\tilde{q}(u,0)\tilde{g}(u)}{\tilde{g}(u)^{2}}. |  |

Hence, using that deg ⁡ ( g ~) = n + 1 \deg(\tilde{g})=n+1 due to g ⁡ ( 0) ≠ 0 g(0)\neq 0 (see H1) it follows that ∂ 2 K ⁡ ( u, 0) \partial_{2}K(u,0) does not grow faster than u − 2 u^{-2} at u = + ∞ u=+\infty. We write this assertion as ∂ 2 K ⁡ ( u, 0) ≺ u − 2 \partial_{2}K(u,0)\prec u^{-2} and in what follows we shall use this notation for shortness. Since ( λ + 1) ​ ∫ 1 1 / η d ​ z z = − log ⁡ η 1 + λ (\lambda+1)\int_{1}^{1/\eta}\frac{dz}{z}=-\log\eta^{1+\lambda}, an easy computation yields

 | log ⁡ L 2 ​ ( 1 / η) \displaystyle\log L_{2}(1/\eta) | = ∫ 0 1 / η ( K ⁡ ( z, 0) + λ) ​ d ​ z z = ∫ 0 1 / η ( 1 − q ⁡ ( 1 / z, 0) z ​ g ​ ( 1 / z) + λ) ​ d ​ z z \displaystyle=\int_{0}^{1/\eta}\big(K(z,0)+\lambda\big)\frac{dz}{z}=\int_{0}^{1/\eta}\left(1-\frac{q(1/z,0)}{zg(1/z)}+\lambda\right)\frac{dz}{z} |  |

 |  | = ∫ 0 1 ( 1 − q ⁡ ( 1 / z, 0) z ​ g ​ ( 1 / z) + λ) ​ d ​ z z − ∫ η 1 q ⁡ ( w, 0) g ⁡ ( w) ​ 𝑑 w − log ⁡ η λ + 1. \displaystyle=\int_{0}^{1}\left(1-\frac{q(1/z,0)}{zg(1/z)}+\lambda\right)\frac{dz}{z}-\int_{\eta}^{1}\frac{q(w,0)}{g(w)}dw-\log\eta^{\lambda+1}. |  |

Accordingly, due to g ⁡ ( 0) ≠ 0 g(0)\neq 0 (see H1), setting

 | G 2 +:= ∫ 0 1 ( λ + 1 − q ⁡ ( 1 / z, 0) z ​ g ​ ( 1 / z) − z ​ q ​ ( z, 0) g ⁡ ( z)) ​ d ​ z z, G_{2}^{+}\!:=\int_{0}^{1}\left(\lambda+1-\frac{q(1/z,0)}{zg(1/z)}-\frac{zq(z,0)}{g(z)}\right)\frac{dz}{z}, |  |

the Dominated Convergence Theorem shows the validity of the limit

 | lim η → 0 + η λ + 1 ​ L 2 ​ ( 1 / η) = exp ⁡ ( G 2 +). \lim_{\eta\to 0^{+}}\eta^{\lambda+1}L_{2}(1/\eta)=\exp(G_{2}^{+}). |  | (33) |

In particular, L 2 ​ ( u) ≺ u λ + 1 L_{2}(u)\prec u^{\lambda+1}. Therefore M 2 ​ ( u) = L 2 ​ ( u) ​ ∂ 2 K ⁡ ( u, 0) ≺ u λ − 1 M_{2}(u)=L_{2}(u)\partial_{2}K(u,0)\prec u^{\lambda-1}. Hence, due to λ < 1 \lambda<1, we can assert that ( M 2 ​ ( u) − M 2 ​ ( 0)) ​ u − λ − 1 ≺ u − λ − 1 ≺ u − 2. (M_{2}(u)-M_{2}(0))u^{-\lambda-1}\prec u^{-\lambda-1}\prec u^{-2}. Accordingly, from ( 32) (\ref{teo1eq1}),

 | lim η → 0 + η λ ​ M ^ 2 ​ ( λ, 1 / η) = ∫ 0 + ∞ ( M 2 ​ ( u) − M 2 ​ ( 0)) ​ d ​ u u λ + 1. \lim_{\eta\to 0^{+}}\eta^{\lambda}\hat{M}_{2}(\lambda,1/\eta)=\int_{0}^{+\infty}\big(M_{2}(u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}. |  |

Finally, the combination of this with ( 33) (\ref{teo1eq2}) yields

 | Δ 2 + ​ ( μ) \displaystyle\Delta_{2}^{+}(\mu) | = Δ ¯ 2 ( μ, α, 0) = lim η → 0 + Δ ¯ 2 ( μ, 0, η) = − lim η → 0 + ( ( Δ ¯ 0) 2 S 2) ( μ, 0, η) \displaystyle=\bar{\Delta}_{2}(\mu,\alpha,0)=\lim_{\eta\to 0^{+}}\bar{\Delta}_{2}(\mu,0,\eta)=-\lim_{\eta\to 0^{+}}\big((\bar{\Delta}_{0})^{2}S_{2}\big)(\mu,0,\eta) |  |

 |  | = ( Δ 0 +) 2 ​ exp ⁡ ( − G 2 +) ​ ∫ 0 + ∞ ( M 2 ​ ( u) − M 2 ​ ( 0)) ​ d ​ u u λ + 1. \displaystyle=(\Delta_{0}^{+})^{2}\exp(-G_{2}^{+})\int_{0}^{+\infty}\big(M_{2}(u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}. |  | (34) |

Our next task is to compute Δ ¯ 1 ​ ( μ, α, 0) \bar{\Delta}_{1}(\mu,\alpha,0) under the assumption λ 0 > 1 \lambda_{0}>1, which is given by Δ ¯ 1 = λ ​ Δ ¯ 0 ​ S 1 \bar{\Delta}_{1}=\lambda\bar{\Delta}_{0}S_{1} thanks to the first assertion in Proposition A.4. Taking the derivatives of σ 1 ​ ( s) = ( s η, 1 η) \sigma_{1}(s)=(\frac{s}{\eta},\frac{1}{\eta}) at s = 0 s=0 into account we get that

 | S 1 ​ ( μ, 0, η) = σ 112 2 ​ σ 111 − σ 121 σ 120 ​ P 1 P 2 ​ ( 0, σ 120) − σ 111 L 1 ​ ( σ 120) ​ M ^ 1 ​ ( 1 / λ, σ 120) = − 1 η ​ L 1 ​ ( 1 / η) ​ M ^ 1 ​ ( 1 / λ, 1 / η), S_{1}(\mu,0,\eta)=\frac{\sigma_{112}}{2\sigma_{111}}-\frac{\sigma_{121}}{\sigma_{120}}\frac{P_{1}}{P_{2}}(0,\sigma_{120})-\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{M}_{1}(1/\lambda,\sigma_{120})=-\frac{1}{\eta L_{1}(1/\eta)}\hat{M}_{1}(1/\lambda,1/\eta), |  |

where, see ( 30) (\ref{K_teo1}) and ( 26) (\ref{def_fun}), M 1 ​ ( u) = L 1 ​ ( u) ​ ∂ 1 ( 1 K) ​ ( 0, u) M_{1}(u)=L_{1}(u)\partial_{1}\!\left(\frac{1}{K}\right)(0,u) with

 | L 1 ( u) = exp ∫ 0 u ( 1 K ⁡ ( 0, z) + 1 λ) d ​ z z. L_{1}(u)=\exp\int_{0}^{u}\left(\frac{1}{K(0,z)}+\frac{1}{\lambda}\right)\frac{dz}{z}. |  |

Moreover

 | ∂ 1 ( 1 K) ​ ( 0, u) = ∂ 1 ( 1 + q ~ ​ ( x 1, x 2) x 2 ​ f ~ ​ ( x 1, x 2) + g ~ ​ ( x 1) − q ~ ​ ( x 1, x 2)) | ( x 1, x 2) = ( 0, u) ≺ u − 2. \partial_{1}\!\left(\frac{1}{K}\right)(0,u)=\partial_{1}\left(1+\frac{\tilde{q}(x_{1},x_{2})}{x_{2}\tilde{f}(x_{1},x_{2})+\tilde{g}(x_{1})-\tilde{q}(x_{1},x_{2})}\right)\Big|_{(x_{1},x_{2})=(0,u)}\prec u^{-2}. |  |

Here the assertion with regard to the growth at infinity is a consequence of f n ​ ( 0, 1) ≠ 0 f_{n}(0,1)\neq 0 (see H2), which implies that f ~ ​ ( 0, u) \tilde{f}(0,u) has degree exactly n n. On the other hand, by applying ( b) (b) in Proposition A.5 and taking 1 / λ < 1 1/\lambda<1 into account, we get

 | M ^ 1 ( 1 / λ, 1 / η) = − λ M 1 ( 0) + η − 1 / λ ∫ 0 1 / η ( M 1 ( u) − M 1 ( 0)) u − 1 / λ d ​ u u. \hat{M}_{1}(1/\lambda,1/\eta)=-\lambda M_{1}(0)+\eta^{-1/\lambda}\int_{0}^{1/\eta}(M_{1}(u)-M_{1}(0))u^{-1/\lambda}\frac{du}{u}. |  | (35) |

Moreover

 | log ⁡ L 1 ​ ( 1 / η) = \displaystyle\log L_{1}(1/\eta)= | ∫ 0 1 / η ( 1 K ⁡ ( 0, z) + 1 λ) ​ d ​ z z = ∫ 0 1 / η ( q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z) + 1 + 1 λ) ​ d ​ z z \displaystyle\int_{0}^{1/\eta}\left(\frac{1}{K(0,z)}+\frac{1}{\lambda}\right)\frac{dz}{z}=\int_{0}^{1/\eta}\left(\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}+1+\frac{1}{\lambda}\right)\frac{dz}{z} |  |

 | = \displaystyle= | ∫ 0 1 ( q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z) + 1 + 1 λ) ​ d ​ z z + ∫ η 1 q n ​ ( w, 1) ℓ n + 1 ​ ( w, 1) ​ 𝑑 w − ( 1 + 1 λ) ​ log ⁡ η, \displaystyle\int_{0}^{1}\left(\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}+1+\frac{1}{\lambda}\right)\frac{dz}{z}+\int_{\eta}^{1}\frac{q_{n}(w,1)}{{\ell_{n+1}}(w,1)}dw-\left(1+\frac{1}{\lambda}\right)\log\eta, |  |

where in the last equality we use the coordinate change z = 1 / w. z=1/w. Consequently, by applying the Dominated Convergence Theorem using that f n ​ ( 0, 1) ≠ 0, f_{n}(0,1)\neq 0,

 | lim η → 0 + η 1 + 1 / λ ​ L 1 ​ ( 1 / η) = exp ⁡ ( G 1 +), \lim_{\eta\to 0^{+}}\eta^{1+1/\lambda}L_{1}(1/\eta)=\exp(G_{1}^{+}), |  | (36) |

where

 | G 1 +:= ∫ 0 1 ( q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z) + 1 + 1 λ + z ​ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) ​ d ​ z z. G_{1}^{+}\!:=\int_{0}^{1}\left(\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}+1+\frac{1}{\lambda}+\frac{zq_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)\frac{dz}{z}. |  |

This implies in particular that L 1 ​ ( u) ≺ u 1 + 1 / λ L_{1}(u)\prec u^{1+1/\lambda} and, accordingly, M 1 ​ ( u) ≺ u − 1 + 1 / λ M_{1}(u)\prec u^{-1+1/\lambda}. The combination of this, together with ( 35) (\ref{teo1eq3}) and ( 36) (\ref{teo1eq4}), yields

 | lim η → 0 + S 1 ( μ, 0, η) = − lim η → 0 + η 1 / λ ​ M ^ 1 ​ ( 1 / λ, 1 / η) η 1 + 1 / λ ​ L 1 ​ ( 1 / η) = − exp ( − G 1 +) ∫ 0 + ∞ ( M 1 ( u) − M 1 ( 0)) d ​ u u 1 + 1 / λ. \lim_{\eta\to 0^{+}}S_{1}(\mu,0,\eta)=-\lim_{\eta\to 0^{+}}\frac{\eta^{1/\lambda}\hat{M}_{1}(1/\lambda,1/\eta)}{\eta^{1+1/\lambda}L_{1}(1/\eta)}=-\exp(-G_{1}^{+})\int_{0}^{+\infty}(M_{1}(u)-M_{1}(0))\frac{du}{u^{1+1/\lambda}}. |  |

Therefore

 | Δ 1 + ​ ( μ) = \displaystyle\Delta_{1}^{+}(\mu)= | Δ ¯ 1 ​ ( μ, α, 0) = ( λ ​ Δ ¯ 0 ​ S 1) ​ ( μ, α, 0) \displaystyle\,\bar{\Delta}_{1}(\mu,\alpha,0)=\big(\lambda\bar{\Delta}_{0}S_{1}\big)(\mu,\alpha,0) |  |

 | = \displaystyle= | − λ Δ 0 + exp ( − G 1 +) ∫ 0 + ∞ ( M 1 ( u) − M 1 ( 0)) d ​ u u 1 + 1 / λ. \displaystyle-\lambda\Delta_{0}^{+}\exp(-G_{1}^{+})\int_{0}^{+\infty}\big(M_{1}(u)-M_{1}(0)\big)\frac{du}{u^{1+1/\lambda}}. |  | (37) |

Now we turn to the computation of the coefficient Δ ¯ 3 ​ ( μ, α, 0) \bar{\Delta}_{3}(\mu,\alpha,0) in case that λ ⁡ ( μ) = 1. \lambda(\mu)=1. By the third assertion in Proposition A.4 we have that Δ ¯ 3 | λ = 1 = ( Δ ¯ 0) 2 ​ S 3 | λ = 1 \left.\bar{\Delta}_{3}\right|_{\lambda=1}=\left.(\bar{\Delta}_{0})^{2}S_{3}\right|_{\lambda=1} with

 | S 3 = σ 221 ​ σ 210 L 2 ​ ( σ 210) ​ M 2 ′ ​ ( 0). S_{3}=\frac{\sigma_{221}\sigma_{210}}{L_{2}(\sigma_{210})}M_{2}^{\prime}(0). |  |

Note that if λ = 1 \lambda=1 then the quotient σ 221 ​ σ 210 L 2 ​ ( σ 210) = 1 η 2 ​ L 2 ​ ( 1 / η) \frac{\sigma_{221}\sigma_{210}}{L_{2}(\sigma_{210})}=\frac{1}{\eta^{2}L_{2}(1/\eta)} tends to exp ⁡ ( − G 2 +) \exp(-G_{2}^{+}) as η → 0 + \eta\to 0^{+} thanks to ( 33) (\ref{teo1eq2}), which is true for any λ > 0. \lambda>0. Consequently, if λ = 1 \lambda=1 then

 | Δ 3 + ​ ( μ) = Δ ¯ 3 ​ ( μ, α, 0) = lim η → 0 + Δ ¯ 3 ​ ( μ, 0, η) = ( Δ 0 +) 2 ​ exp ⁡ ( − G 2 +) ​ M 2 ′ ​ ( 0). \Delta_{3}^{+}(\mu)=\bar{\Delta}_{3}(\mu,\alpha,0)=\lim_{\eta\to 0^{+}}\bar{\Delta}_{3}(\mu,0,\eta)=(\Delta_{0}^{+})^{2}\exp(-G_{2}^{+})M^{\prime}_{2}(0). |  | (38) |

So far we have proved that

 | D + ​ ( s, μ) = Δ 0 + ​ ( μ) ​ s λ + { Δ 1 + ​ ( μ) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ 0) if λ 0 > 1, Δ 2 + ​ ( μ) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ 0) if λ 0 < 1 Δ 3 + ​ ( μ) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ 4 + ​ ( μ) ​ s λ + 1 + ℱ ℓ 3 ∞ ​ ( μ 0) if λ 0 = 1. D_{+}(s;{\mu})=\Delta_{0}^{+}({\mu})s^{\lambda}+\left\{\begin{array}[]{ll}\Delta_{1}^{+}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}>1,$}\\[10.0pt] \Delta_{2}^{+}({\mu})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}<1$}\\[10.0pt] \Delta_{3}^{+}({\mu})s^{\lambda+1}\omega(s;1-\lambda)+\Delta_{4}^{+}(\mu)s^{\lambda+1}+\mathcal{F}_{\ell_{3}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}=1.$}\end{array}\right. |  |

We turn next to the study of the Dulac map D − ​ ( ⋅, μ) D_{-}(\,\cdot\,;\mu) of − X μ -X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2}. To this aim the idea is to take advantage of the previous results for D + ​ ( ⋅, μ) D_{+}(\,\cdot\,;\mu) using the fact that ( x, y) ↦ ( − x, y) (x,y)\mapsto(-x,y) sends − X μ -X_{\mu} to

 | X ~ μ:= ( y f ¯ ( x, y; μ) + g ¯ ( x; μ)) ∂ x + y q ¯ ( x, y; μ) ∂ y \tilde{X}_{\mu}\!:=\big(y\bar{f}(x,y;\mu)+\bar{g}(x;\mu)\big)\partial_{x}+y\bar{q}(x,y;\mu)\partial_{y} |  |

with f ¯ ​ ( x, y) = f ​ ( − x, y) \bar{f}(x,y)=f(-x,y), g ¯ ​ ( x) = g ​ ( − x) \bar{g}(x)=g(-x) and q ¯ ​ ( x, y) = − q ⁡ ( − x, y). \bar{q}(x,y)=-q(-x,y). In particular, following the obvious notation one can check that ℓ ¯ n + 1 ​ ( x, y) = ℓ n + 1 ​ ( − x, y), \bar{\ell}_{n+1}(x,y)={\ell_{n+1}}(-x,y), together with

 | L ¯ i ​ ( u) = L i ​ ( − u) ​ and ​ M ¯ i ​ ( u) = − M i ​ ( − u) ​ for i = 1, 2 \bar{L}_{i}(u)=L_{i}(-u)\text{ and }\bar{M}_{i}(u)=-M_{i}(-u)\text{ for $i=1,2$} |  | (39) |

is verified. By applying the above assertions to the Dulac map of X ~ μ \tilde{X}_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} we get that

 | D − ​ ( s, μ) = Δ 0 − ​ ( μ) ​ s λ + { Δ 1 − ​ ( μ) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ 0) if λ 0 > 1, Δ 2 − ​ ( μ) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ 0) if λ 0 < 1, Δ 3 − ​ ( μ) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ 4 − ​ ( μ) ​ s λ + 1 + ℱ ℓ 3 ∞ ​ ( μ 0) if λ 0 = 1, D_{-}(s;{\mu})=\Delta_{0}^{-}({\mu})s^{\lambda}+\left\{\begin{array}[]{ll}\Delta_{1}^{-}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}>1,$}\\[10.0pt] \Delta_{2}^{-}({\mu})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}<1,$}\\[10.0pt] \Delta_{3}^{-}({\mu})s^{\lambda+1}\omega(s;1-\lambda)+\Delta_{4}^{-}(\mu)s^{\lambda+1}+\mathcal{F}_{\ell_{3}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}=1,$}\end{array}\right. |  |

where each coefficient Δ i − \Delta_{i}^{-} is the counterpart for X ~ μ \tilde{X}_{\mu} of the coefficient Δ i + \Delta_{i}^{+} that we have obtained previously for X μ. X_{\mu}. We can thus assert that

 | 𝒟 ⁡ ( s, μ) \displaystyle\mathscr{D}(s;\mu) | = D + ​ ( s, μ) − D − ​ ( s, μ) \displaystyle=D_{+}(s;{\mu})-D_{-}(s;\mu) |  |

 |  | = Δ 0 ​ ( μ) ​ s λ + { Δ 1 ​ ( μ) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ 0) if λ 0 > 1, Δ 2 ​ ( μ) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ 0) if λ 0 < 1, Δ 3 ​ ( μ) ​ s λ + 1 ​ ω ​ ( s, 1 − λ) + Δ 4 ​ ( μ) ​ s λ + 1 + ℱ ℓ 3 ∞ ​ ( μ 0) if λ 0 = 1, \displaystyle=\Delta_{0}({\mu})s^{\lambda}+\left\{\begin{array}[]{ll}\Delta_{1}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}>1,$}\\[10.0pt] \Delta_{2}({\mu})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}<1,$}\\[10.0pt] \Delta_{3}({\mu})s^{\lambda+1}\omega(s;1-\lambda)+\Delta_{4}(\mu)s^{\lambda+1}+\mathcal{F}_{\ell_{3}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}=1,$}\end{array}\right. |  |

where Δ i:= Δ i + − Δ i − \Delta_{i}\!:=\Delta_{i}^{+}-\Delta_{i}^{-} for i = 0, 1, 2, 3, 4. i=0,1,2,3,4. Our next task is to compute each coefficient. Note that, from ( 31) (\ref{teo1eq10}),

 | Δ 0 − ​ ( μ) \displaystyle\Delta_{0}^{-}(\mu) | = exp ⁡ ( ∫ 0 + ∞ ( q ⁡ ( − w, 0) g ⁡ ( − w) + λ ​ q n ​ ( − w, 1) ℓ n + 1 ​ ( − w, 1)) ​ 𝑑 w) \displaystyle=\exp\left(\int_{0}^{+\infty}\left(\frac{q(-w,0)}{g(-w)}+\lambda\frac{q_{n}(-w,1)}{{\ell_{n+1}}(-w,1)}\right)dw\right) |  |

 |  | = exp ⁡ ( ∫ − ∞ 0 ( q ⁡ ( z, 0) g ⁡ ( z) + λ ​ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) ​ 𝑑 z). \displaystyle=\exp\left(\int^{0}_{-\infty}\left(\frac{q(z,0)}{g(z)}+\lambda\frac{q_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)dz\right). |  |

It is clear now that

 | log ( Δ 0 +) − log ( Δ 0 −) = − ∫ − ∞ + ∞ ( q ⁡ ( z, 0) g ⁡ ( z) + λ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) d z =: d 0 \log(\Delta_{0}^{+})-\log(\Delta_{0}^{-})=-\int^{+\infty}_{-\infty}\left(\frac{q(z,0)}{g(z)}+\lambda\frac{q_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)dz=:\!d_{0} |  |

On account of this, and the fact that x ↦ log ⁡ x x\mapsto\log x is strictly increasing, the application of the mean value theorem shows that Δ 0 = Δ 0 + − Δ 0 − = κ 0 ​ d 0 \Delta_{0}=\Delta_{0}^{+}-\Delta_{0}^{-}=\kappa_{0}d_{0} for some analytic function κ 0 \kappa_{0} with κ 0 ​ ( μ 0) > 0. \kappa_{0}(\mu_{0})>0.

We turn next to the computation of Δ 2 − \Delta_{2}^{-}. To this end we again take advantage of the expression of Δ 2 + \Delta_{2}^{+} thanks to the fact that ( x, y) ↦ ( − x, y) (x,y)\mapsto(-x,y) sends − X μ -X_{\mu} to X ~ μ \tilde{X}_{\mu}. In doing so, recall ( 39) (\ref{teo1eq5}), from ( 34) (\ref{teo1eq6}) we get

 | Δ 2 − = − ( Δ 0 −) 2 exp ( − G 2 −) ∫ 0 + ∞ ( M 2 ( − u) − M 2 ( 0)) d ​ u u λ + 1. \Delta_{2}^{-}=-(\Delta_{0}^{-})^{2}\exp(-G_{2}^{-})\int_{0}^{+\infty}\big(M_{2}(-u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}. |  | (40) |

where

 | G 2 −:= ∫ 0 1 ( λ + 1 + q ( − 1 / z, 0) z g ( − 1 / z) + z ​ q ​ ( − z, 0) g ⁡ ( − z)) ​ d ​ z z. G_{2}^{-}\!:=\int_{0}^{1}\left(\lambda+1+\frac{q(-1/z,0)}{zg(-1/z)}+\frac{zq(-z,0)}{g(-z)}\right)\frac{dz}{z}. |  |

In order to study Δ 2 = Δ 2 + − Δ 2 − \Delta_{2}=\Delta_{2}^{+}-\Delta_{2}^{-} we first observe that

 | G 2 − − G 2 + \displaystyle G_{2}^{-}-G_{2}^{+} | = ∫ 0 1 ( q ⁡ ( 1 / z, 0) z ​ g ​ ( 1 / z) + q ( − 1 / z, 0) z g ( − 1 / z)) ​ d ​ z z + ∫ 0 1 ( q ⁡ ( z, 0) g ⁡ ( z) + q ⁡ ( − z, 0) g ⁡ ( − z)) ​ 𝑑 z \displaystyle=\int_{0}^{1}\left(\frac{q(1/z,0)}{zg(1/z)}+\frac{q(-1/z,0)}{zg(-1/z)}\right)\frac{dz}{z}+\int_{0}^{1}\left(\frac{q(z,0)}{g(z)}+\frac{q(-z,0)}{g(-z)}\right)dz |  |

 |  | = − ∫ + ∞ 1 ( q ⁡ ( u, 0) g ⁡ ( u) + q ⁡ ( − u, 0) g ⁡ ( − u)) d u + ∫ 0 1 ( q ⁡ ( z, 0) g ⁡ ( z) + q ⁡ ( − z, 0) g ⁡ ( − z)) d z \displaystyle=-\int_{+\infty}^{1}\left(\frac{q(u,0)}{g(u)}+\frac{q(-u,0)}{g(-u)}\right)du+\int_{0}^{1}\left(\frac{q(z,0)}{g(z)}+\frac{q(-z,0)}{g(-z)}\right)dz |  |

 |  | = ∫ 0 + ∞ ( q ⁡ ( z, 0) g ⁡ ( z) + q ⁡ ( − z, 0) g ⁡ ( − z)) ​ 𝑑 z =: G 2, \displaystyle=\int_{0}^{+\infty}\left(\frac{q(z,0)}{g(z)}+\frac{q(-z,0)}{g(-z)}\right)dz=:\!G_{2}, |  |

where in the second equality we perform the change of coordinates u = 1 / z u=1/z. Then, from ( 34) (\ref{teo1eq6}) and ( 40) (\ref{teo1eq7}),

 | Δ 2 = Δ 2 + − Δ 2 − \displaystyle\Delta_{2}=\Delta_{2}^{+}-\Delta_{2}^{-} | = exp ⁡ ( − G 2 −) ​ ( ( Δ 0 −) 2 ​ ∫ 0 + ∞ ( M 2 ​ ( − u) − M 2 ​ ( 0)) ​ d ​ u u λ + 1 CLOSE \displaystyle=\exp(-G_{2}^{-})\left((\Delta_{0}^{-})^{2}\int_{0}^{+\infty}\big(M_{2}(-u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}\right. |  |

 |  | + ( Δ 0 +) 2 exp ( G 2) ∫ 0 + ∞ ( M 2 ( u) − M 2 ( 0)) d ​ u u λ + 1) \displaystyle\qquad\left.+(\Delta_{0}^{+})^{2}\exp(G_{2})\int_{0}^{+\infty}\big(M_{2}(u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}\right) |  |

 |  | = κ ¯ 2 ​ Δ 0 + exp ⁡ ( − G 2 −) ​ ( Δ 0 −) 2 ​ ( ∫ 0 + ∞ ( M 2 ​ ( − u) − M 2 ​ ( 0)) ​ d ​ u u λ + 1 CLOSE \displaystyle=\bar{\kappa}_{2}\Delta_{0}+\exp(-G_{2}^{-})(\Delta_{0}^{-})^{2}\left(\int_{0}^{+\infty}\big(M_{2}(-u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}\right. |  |

 |  | + exp ( G 2) ∫ 0 + ∞ ( M 2 ( u) − M 2 ( 0)) d ​ u u λ + 1) \displaystyle\qquad\left.+\exp(G_{2})\int_{0}^{+\infty}\big(M_{2}(u)-M_{2}(0)\big)\frac{du}{u^{\lambda+1}}\right) |  |

 |  | = κ ¯ 2 ​ Δ 0 + κ 2 ​ F 2, \displaystyle=\bar{\kappa}_{2}\Delta_{0}+\kappa_{2}F_{2}, |  |

where in the second equality we use that G 2 − − G 2 + = G 2 G_{2}^{-}-G_{2}^{+}=G_{2}, in the third one we plug Δ 0 + = Δ 0 + Δ 0 − \Delta_{0}^{+}=\Delta_{0}+\Delta_{0}^{-} to get an analytic function κ ¯ 2 = κ ¯ 2 ​ ( μ) \bar{\kappa}_{2}=\bar{\kappa}_{2}(\mu) multiplying Δ 0 \Delta_{0} and in the last one we set κ 2 = exp ⁡ ( − G 2 −) ​ ( Δ 0 −) 2 \kappa_{2}=\exp(-G_{2}^{-})(\Delta_{0}^{-})^{2}. Accordingly Δ 2 = κ 2 ​ F 2 + κ ¯ 2 ​ Δ 0 \Delta_{2}=\kappa_{2}F_{2}+\bar{\kappa}_{2}\Delta_{0} with κ 2 ​ ( μ 0) > 0, \kappa_{2}(\mu_{0})>0, so the assertion ( 2) (2) in the statement is true.

In order to obtain the expression for Δ 1 = Δ 1 + − Δ 1 − \Delta_{1}=\Delta_{1}^{+}-\Delta_{1}^{-} we follow the same strategy as before. First we take advantage of the expression of Δ 1 + \Delta_{1}^{+} in ( 37) (\ref{teo1eq8}) and the equalities in ( 39) (\ref{teo1eq5}) to get that

 | Δ 1 − = λ ​ Δ 0 − ​ exp ⁡ ( − G 1 −) ​ ∫ 0 + ∞ ( M 1 ​ ( − u) − M 1 ​ ( 0)) ​ d ​ u u 1 + 1 / λ, \Delta_{1}^{-}=\lambda\Delta_{0}^{-}\exp(-G_{1}^{-})\int_{0}^{+\infty}\big(M_{1}(-u)-M_{1}(0)\big)\frac{du}{u^{1+1/\lambda}}, |  | (41) |

where

 | G 1 −:= \displaystyle G_{1}^{-}\!:= | ∫ 0 1 ( − q n ​ ( − 1, z) ℓ n + 1 ​ ( − 1, z) + 1 + 1 λ − z ​ q n ​ ( − z, 1) ℓ n + 1 ​ ( − z, 1)) ​ d ​ z z \displaystyle\int_{0}^{1}\left(-\frac{q_{n}(-1,z)}{{\ell_{n+1}}(-1,z)}+1+\frac{1}{\lambda}-\frac{zq_{n}(-z,1)}{{\ell_{n+1}}(-z,1)}\right)\frac{dz}{z} |  |

 | = \displaystyle= | − ∫ − 1 0 ( q n ​ ( 1, u) ℓ n + 1 ​ ( 1, u) + 1 + 1 λ + u ​ q n ​ ( u, 1) ℓ n + 1 ​ ( u, 1)) d ​ u u. \displaystyle-\int_{-1}^{0}\left(\frac{q_{n}(1,u)}{{\ell_{n+1}}(1,u)}+1+\frac{1}{\lambda}+\frac{uq_{n}(u,1)}{{\ell_{n+1}}(u,1)}\right)\frac{du}{u}. |  |

Here we use first the homogeneity of q n q_{n} and ℓ n + 1 {\ell_{n+1}} and then we perform the change of coordinates u = − z. u=-z. Consequently

 | G 1 + − G 1 − = ∫ − 1 1 ( q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z) + 1 + 1 λ + z ​ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) ​ d ​ z z =: G 1 G_{1}^{+}-G_{1}^{-}=\int_{-1}^{1}\left(\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}+1+\frac{1}{\lambda}+\frac{zq_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)\frac{dz}{z}=:\!G_{1} |  |

On account of this, the combination of ( 37) (\ref{teo1eq8}) and ( 41) (\ref{teo1eq9}) yields

 | Δ 1 = Δ 1 + − Δ 1 − \displaystyle\Delta_{1}=\Delta_{1}^{+}-\Delta_{1}^{-} | = − λ ​ exp ⁡ ( − G 1 +) ​ ( Δ 0 + ​ ∫ 0 + ∞ ( M 1 ​ ( u) − M 1 ​ ( 0)) ​ d ​ u u 1 + 1 / λ CLOSE \displaystyle=-\lambda\exp(-G_{1}^{+})\left(\Delta_{0}^{+}\int_{0}^{+\infty}\big(M_{1}(u)-M_{1}(0)\big)\frac{du}{u^{1+1/\lambda}}\right. |  |

 |  | + Δ 0 − exp ( G 1) ∫ 0 + ∞ ( M 1 ( − u) − M 1 ( 0)) d ​ u u 1 + 1 / λ) \displaystyle\qquad\left.+\Delta_{0}^{-}\exp(G_{1})\int_{0}^{+\infty}\big(M_{1}(-u)-M_{1}(0)\big)\frac{du}{u^{1+1/\lambda}}\right) |  |

 |  | = κ ¯ 1 ​ Δ 0 − λ ​ Δ 0 + ​ exp ⁡ ( − G 2 +) ​ ( ∫ 0 + ∞ ( M 1 ​ ( u) − M 1 ​ ( 0)) ​ d ​ u u 1 + 1 / λ CLOSE \displaystyle=\bar{\kappa}_{1}\Delta_{0}-\lambda\Delta_{0}^{+}\exp(-G_{2}^{+})\left(\int_{0}^{+\infty}\big(M_{1}(u)-M_{1}(0)\big)\frac{du}{u^{1+1/\lambda}}\right. |  |

 |  | + exp ( G 1) ∫ 0 + ∞ ( M 1 ( − u) − M 1 ( 0)) d ​ u u 1 + 1 / λ) \displaystyle\qquad\left.+\exp(G_{1})\int_{0}^{+\infty}\big(M_{1}(-u)-M_{1}(0)\big)\frac{du}{u^{1+1/\lambda}}\right) |  |

 |  | = κ ¯ 1 ​ Δ 0 + κ 1 ​ F 1, \displaystyle=\bar{\kappa}_{1}\Delta_{0}+\kappa_{1}F_{1}, |  |

where in the second equality we use that G 1 + − G 1 − = G 1 G_{1}^{+}-G_{1}^{-}=G_{1}, in the third one we replace Δ 0 + \Delta_{0}^{+} by Δ 0 + Δ 0 − \Delta_{0}+\Delta_{0}^{-} to obtain a function κ ¯ 1 \bar{\kappa}_{1} multiplying Δ 0 \Delta_{0} and in the last one we set κ 1 = λ ​ Δ 0 + ​ exp ⁡ ( − G 2 +) \kappa_{1}=\lambda\Delta_{0}^{+}\exp(-G_{2}^{+}). Therefore Δ 1 = κ 1 ​ F 1 + κ ¯ 1 ​ Δ 0 \Delta_{1}=\kappa_{1}F_{1}+\bar{\kappa}_{1}\Delta_{0} with κ 1 ​ ( μ 0) > 0 \kappa_{1}(\mu_{0})>0. Since one can easily verify that κ ¯ 1 \bar{\kappa}_{1} is analytic at μ 0 \mu_{0} with λ ⁡ ( μ 0) > 1, \lambda(\mu_{0})>1, this concludes the proof of assertion ( 1) (1).

It only remains to compute Δ 3 = Δ 3 + − Δ 3 − \Delta_{3}=\Delta_{3}^{+}-\Delta_{3}^{-} in case that λ ⁡ ( μ) = 1. \lambda(\mu)=1. Exactly as before, since ( x, y) ↦ ( − x, y) (x,y)\mapsto(-x,y) sends − X μ -X_{\mu} to X ~ μ \tilde{X}_{\mu}, from the expression of Δ 3 + \Delta_{3}^{+} in ( 38) (\ref{teo1eq4.5}) and taking ( 39) (\ref{teo1eq5}) into account we get

 | Δ 3 − | λ = 1 = ( Δ 0 −) 2 ​ exp ⁡ ( − G 2 −) ​ M ¯ 2 ′ ​ ( 0) = ( Δ 0 −) 2 ​ exp ⁡ ( − G 2 −) ​ M 2 ′ ​ ( 0). \left.\Delta_{3}^{-}\right|_{\lambda=1}=(\Delta_{0}^{-})^{2}\exp(-G_{2}^{-})\bar{M}_{2}^{\prime}(0)=(\Delta_{0}^{-})^{2}\exp(-G_{2}^{-})M_{2}^{\prime}(0). |  |

Hence some straightforward computations show that

 | Δ 3 | λ = 1 \displaystyle\left.\Delta_{3}\right|_{\lambda=1} | = ( ( Δ 0 +) 2 ​ exp ⁡ ( − G 2 +) − ( Δ 0 −) 2 ​ exp ⁡ ( − G 2 −)) ​ M 2 ′ ​ ( 0) \displaystyle=\left((\Delta_{0}^{+})^{2}\exp(-G_{2}^{+})-(\Delta_{0}^{-})^{2}\exp(-G_{2}^{-})\right)M_{2}^{\prime}(0) |  |

 |  | = ( ( Δ 0 + Δ 0 −) 2 ​ exp ⁡ ( − G 2 − G 2 −) − ( Δ 0 −) 2 ​ exp ⁡ ( − G 2 −)) ​ M 2 ′ ​ ( 0) \displaystyle=\left((\Delta_{0}+\Delta_{0}^{-})^{2}\exp(-G_{2}-G_{2}^{-})-(\Delta_{0}^{-})^{2}\exp(-G_{2}^{-})\right)M_{2}^{\prime}(0) |  |

 |  | = − κ 3 ​ G 2 ​ M 2 ′ ​ ( 0) + κ ¯ 3 ​ Δ 0, \displaystyle=-\kappa_{3}G_{2}M_{2}^{\prime}(0)+\bar{\kappa}_{3}\Delta_{0}, |  |

where

 | κ 3:= ( Δ 0 −) 2 ​ exp ⁡ ( − G 2 −) ​ 1 − exp ⁡ ( − G 2) G 2 ​ and ​ κ ¯ 3:= ( Δ 0 + 2 ​ Δ 0 −) ​ exp ⁡ ( − G 2 +) ​ M 2 ′ ​ ( 0), \kappa_{3}\!:=(\Delta_{0}^{-})^{2}\exp(-G_{2}^{-})\frac{1-\exp(-G_{2})}{G_{2}}\text{ and }\bar{\kappa}_{3}\!:=(\Delta_{0}+2\Delta_{0}^{-})\exp(-G_{2}^{+})M_{2}^{\prime}(0), |  |

which are analytic functions at μ 0 \mu_{0} and κ 3 ​ ( μ 0) > 0. \kappa_{3}(\mu_{0})>0. Finally, due to M 2 ​ ( u) = L 2 ​ ( u) ​ ∂ 2 K ⁡ ( u, 0) M_{2}(u)=L_{2}(u)\partial_{2}K(u,0) with

 | M 2 ( u) = L 2 ( u) ∂ 2 K ( u, 0) and L 2 ( u) = exp ∫ 0 u ( K ( z, 0) + λ) d ​ z z, M_{2}(u)=L_{2}(u)\partial_{2}K(u,0)\text{ and }L_{2}(u)=\exp\int_{0}^{u}\big(K(z,0)+{\lambda}\big)\frac{dz}{z}, |  |

one can easily show that M 2 ′ ​ ( 0) = L 2 ′ ​ ( 0) ​ ∂ 2 K ⁡ ( 0, 0) + L 2 ​ ( 0) ​ ∂ 12 K ⁡ ( 0, 0) = ∂ 1 K ⁡ ( 0, 0) ​ ∂ 2 K ⁡ ( 0, 0) + ∂ 12 K ⁡ ( 0, 0) M_{2}^{\prime}(0)=L_{2}^{\prime}(0)\partial_{2}K(0,0)+L_{2}(0)\partial_{12}K(0,0)=\partial_{1}K(0,0)\partial_{2}K(0,0)+\partial_{12}K(0,0). We thus obtain that Δ 3 | λ = 1 = κ 3 ​ F 3 + κ ¯ 3 ​ Δ 0 \Delta_{3}|_{\lambda=1}=\kappa_{3}F_{3}+\bar{\kappa}_{3}\Delta_{0} with F 3 = − G 2 ​ ( ∂ 1 K ​ ∂ 2 K + ∂ 12 K) ​ ( 0, 0), F_{3}=-G_{2}\big(\partial_{1}K\partial_{2}K+\partial_{12}K\big)(0,0), as desired. This proves the validity of the third assertion in the statement and concludes the proof of the result.

### B.2 Proof of Proposition 3.2

In this section we prove Proposition 3.2, which gives the asymptotic development of the difference map

 | 𝒟 u ​ ( s, μ):= D + u ​ ( s, μ) − D − u ​ ( s, μ), \mathscr{D}_{u}(s;\mu)\!:=D^{u}_{+}(s;\mu)-D^{u}_{-}(s;\mu), |  |

see Figure 7, together with some properties of its coefficients. To this end we need first two auxiliary results.

###### Lemma B.1.

Fix any μ 0 = ( a 0, b 0, ε 0, ε 1, ε 2) \mu_{0}=(a_{0},b_{0},\varepsilon_{0},\varepsilon_{1},\varepsilon_{2}) with ( a 0, b 0) ∈ ( − 2, 0) × ( 0, 2) (a_{0},b_{0})\in(-2,0)\times(0,2) and ε i ≈ 0 \varepsilon_{i}\approx 0 for i = 0, 1, 2. i=0,1,2. Then

 | D ± u ​ ( s, μ) = δ ± + Δ 0 ± ​ s λ + ℱ ℓ ∞ ​ ( μ 0), for any ℓ ∈ [λ 0, min ⁡ ( 2 ​ λ 0, λ 0 + 1)), D^{u}_{\pm}(s;{\mu})=\delta_{\pm}+\Delta_{0}^{\pm}s^{\lambda}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}),\text{ for any ${\ell}\in\big[\lambda_{0},\min(2\lambda_{0},\lambda_{0}+1)\big)$,} |  |

where λ \lambda, δ ± \delta_{\pm} and Δ 0 ± \Delta_{0}^{\pm} are 𝒞 ∞ \mathscr{C}^{\infty} functions on μ ≈ μ 0 \mu\approx\mu_{0} and λ 0:= λ ⁡ ( μ 0) = − a 0 + 2 a 0. \lambda_{0}\!:=\lambda(\mu_{0})=-\frac{a_{0}+2}{a_{0}}. Moreover, for a 0 ≠ − 1, a_{0}\neq-1,

1. ( 1) (1)

If a 0 > − 1 a_{0}>-1 then D ± u ​ ( s, μ) = δ ± + Δ 0 ± ​ s λ + Δ 1 ± ​ s λ + 1 + ℱ ℓ ∞ ​ ( μ 0) D^{u}_{\pm}(s;{\mu})=\delta_{\pm}+\Delta_{0}^{\pm}s^{\lambda}+\Delta_{1}^{\pm}s^{\lambda+1}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) for any ℓ ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {\ell}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big), where Δ 1 ± \Delta_{1}^{\pm} is a 𝒞 ∞ \mathscr{C}^{\infty} function on μ ≈ μ 0. \mu\approx\mu_{0}.

2. ( 2) (2)

If a 0 < − 1 a_{0}<-1 then D ± u ​ ( s, μ) = δ ± + Δ 0 ± ​ s λ + Δ 2 ± ​ s 2 ​ λ + ℱ ℓ ∞ ​ ( μ 0) D^{u}_{\pm}(s;{\mu})=\delta_{\pm}+\Delta_{0}^{\pm}s^{\lambda}+\Delta_{2}^{\pm}s^{2\lambda}+\mathcal{F}_{\ell}^{\infty}(\mu_{0}) for any ℓ ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big), where Δ 2 ± \Delta_{2}^{\pm} is a 𝒞 ∞ \mathscr{C}^{\infty} function on μ ≈ μ 0. \mu\approx\mu_{0}.

For the sake of simplicity in the exposition we omit the superscript in D ± u D^{u}_{\pm}. That being said, let us prove the result for the Dulac map D + ​ ( ⋅, μ) D_{+}(\,\cdot\,;\mu), the proof for D − ​ ( ⋅, μ) D_{-}(\,\cdot\,;\mu) follows verbatim. We denote the y y -coordinate of the intersection point with x = 0 x=0 of the unstable separatrix of the saddle at s 1 s_{1} by δ + ​ ( μ) \delta_{+}(\mu). The function μ ↦ δ + ​ ( μ) \mu\mapsto\delta_{+}(\mu) is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of μ = μ 0 \mu=\mu_{0}. Indeed, this follows by first applying the local center-stable manifold theorem (see [14, Theorem 1] for instance) to s 1 s_{1} and then appealing to the smooth dependence of the solutions of X μ X_{\mu} on initial conditions and parameters. It is clear moreover that δ + | ε 0 = 0 ≡ 0. \delta_{+}|_{\varepsilon_{0}=0}\equiv 0. For convenience we change the parametrisation on Σ 2 \Sigma_{2} by s ^ ↦ ( 0, s ^ + δ + ​ ( μ)) \hat{s}\mapsto\big(0,\hat{s}+\delta_{+}(\mu)\big) for s ^ > 0 \hat{s}>0 small enough and we denote by D ^ + ​ ( s, μ) \hat{D}_{+}(s;\mu) the Dulac map of X μ X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} with this new parametrisation in the arrival section. It is then clear that D + ​ ( s, μ) = δ + ​ ( μ) + D ^ + ​ ( s, μ) D_{+}(s;\mu)=\delta_{+}(\mu)+\hat{D}_{+}(s;\mu) for s > 0. s>0. To study D ^ + ​ ( ⋅, μ) \hat{D}_{+}(\,\cdot\,;\mu) we first compactify the vector field X μ X_{\mu} by using the projective coordinates ( u, v) = ϕ 1 ​ ( x, y):= ( 1 x + y + 1, y x + y + 1). (u,v)=\phi_{1}(x,y)\!:=(\frac{1}{x+y+1},\frac{y}{x+y+1}). The key point here is that the trajectories of X μ X_{\mu} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} do not intersect x + y + 1 = 0 x+y+1=0. In doing so we obtain an analytic family of vector fields which is orbitally equivalent to a polynomial one, say Y μ, Y_{\mu}, that has a finite hyperbolic saddle at the origin. By construction its stable separatrix is at u = 0 u=0 for all μ, \mu, whereas its unstable one is at v = 0 v=0 only when ε 0 = 0. \varepsilon_{0}=0. In order to straighten both separatrices for all μ \mu we apply Lemma A.6, that gives a 𝒞 ∞ \mathscr{C}^{\infty} family of diffeomorphisms ϕ 2 ​ ( u, v, μ) \phi_{2}(u,v;\mu) such that the push-forward ( ϕ 2) ⋆ ​ ( Y μ) (\phi_{2})_{\star}\big(Y_{\mu}\big) writes as in ( 25) (\ref{X}) with ϖ = ∞. \varpi=\infty. By construction, setting ϕ = ϕ 2 ∘ ϕ 1 \phi\>=\phi_{2}\circ\phi_{1}, its Dulac map from ϕ ⁡ ( Σ 1) \phi(\Sigma_{1}) to ϕ ⁡ ( Σ 2) \phi(\Sigma_{2}), parametrised, respectively, by σ 1 ​ ( s, μ) = ϕ ⁡ ( 0, 1 / s, μ) \sigma_{1}(s;\mu)=\phi(0,1/s;\mu) and σ 2 ​ ( s, μ) = ϕ ⁡ ( 0, s + δ + ​ ( μ), μ) \sigma_{2}(s;\mu)=\phi(0,s+\delta_{+}(\mu);\mu), is precisely D ^ ​ ( s, μ). \hat{D}(s;\mu). Observe in this regard that the parametrisations of the transverse sections are 𝒞 ∞. \mathscr{C}^{\infty}. Accordingly, by applying Proposition A.4,

 | D ^ + ​ ( s, μ) = Δ 0 + ​ ( μ) ​ s λ + { Δ 1 + ​ ( μ) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ 0) if λ 0 > 1, Δ 2 + ​ ( μ) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ 0) if λ 0 < 1, \hat{D}_{+}(s;{\mu})=\Delta_{0}^{+}({\mu})s^{\lambda}+\left\{\begin{array}[]{ll}\Delta_{1}^{+}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}>1,$}\\[10.0pt] \Delta_{2}^{+}({\mu})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})&\text{ if $\lambda_{0}<1,$}\end{array}\right. |  |

for any ℓ 2 ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell_{2}}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big) and ℓ 1 ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {\ell_{1}}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big). Here λ = λ ⁡ ( μ) \lambda=\lambda(\mu) is the hyperbolicity ratio of the saddle of X μ X_{\mu} at s 1 s_{1} and λ 0 = λ ⁡ ( μ 0) = − a 0 + 2 a 0 \lambda_{0}=\lambda(\mu_{0})=-\frac{a_{0}+2}{a_{0}}. Moreover the coefficient Δ 0 + \Delta_{0}^{+} is 𝒞 ∞ \mathscr{C}^{\infty} at μ 0 \mu_{0} and, on the other hand, the coefficient Δ 1 + \Delta_{1}^{+} (respectively, Δ 2 + \Delta_{2}^{+}) is 𝒞 ∞ \mathscr{C}^{\infty} at μ 0 \mu_{0} provided that λ 0 > 1 \lambda_{0}>1 (respectively, λ 0 < 1 \lambda_{0}<1). On account of D + ​ ( s, μ) = δ + ​ ( μ) + D ^ + ​ ( s, μ) D_{+}(s;\mu)=\delta_{+}(\mu)+\hat{D}_{+}(s;\mu) this concludes the proof of the result.

###### Lemma B.2.

∂ ε 0 ( δ + − δ −) ​ ( μ) > 0 \partial_{\varepsilon_{0}}\big(\delta_{+}-\delta_{-}\big)(\mu)>0 for all μ = ( a, b, 0, 0, 0) \mu=(a,b,0,0,0) with a ∈ ( − 2, 0) ∖ { − 1 } a\in(-2,0)\setminus\{-1\} and b ∈ ( 0, 2). b\in(0,2).

The differential form associated to system ( 12) (\ref{pert}) is given by

 | Ω:= ( 2 ​ x ​ y − ε 0) ​ d ​ x + ( b − 2 4 + ε 1 ​ x + ( 1 − b) ​ y + a ​ x 2 + ε 2 ​ x ​ y + b ​ y 2) ​ d ​ y. \textstyle\Omega\!:=\big(2xy-\varepsilon_{0}\big)dx+\big(\frac{b-2}{4}+\varepsilon_{1}x+(1-b)y+ax^{2}+\varepsilon_{2}xy+by^{2}\big)dy. |  |

We know on the other hand that

 | H ⁡ ( x, y):= y ​ ( x 2 + ℓ ​ y 2 + m ​ y + n) 1 a, H(x,y)\!:=y(x^{2}+\ell y^{2}+my+n)^{\frac{1}{a}}, |  | (42) |

with ℓ = b a + 2, \ell=\frac{b}{a+2}, m = − b − 1 a + 1 m=-\frac{b-1}{a+1} and n = b − 2 4 ​ a n=\frac{b-2}{4a}, is a first integral of ( 12) (\ref{pert}) for ε 0 = ε 1 = ε 2 = 0 \varepsilon_{0}=\varepsilon_{1}=\varepsilon_{2}=0. We observe in this regard that

 | a ​ d ​ H H = a ​ d ​ y y + 2 ​ x ​ d ​ x + ( 2 ​ ℓ ​ y + m) ​ d ​ y x 2 + ℓ ​ y 2 + m ​ y + n, a\frac{dH}{H}=a\frac{dy}{y}+\frac{2xdx+(2\ell y+m)dy}{x^{2}+\ell y^{2}+my+n}, |  |

which yields

 | a ​ y 1 − a ​ H a − 1 ​ d ​ H = 2 ​ x ​ y ​ d ​ x + ( a ​ n + ( a + 1) ​ m ​ y + a ​ x 2 + ( a + 2) ​ ℓ ​ y 2) ​ d ​ y = Ω | ε 1 = ε 2 = 0 + ε 0 ​ d ​ x, ay^{1-a}H^{a-1}dH=2xy\,dx+\big(an+(a+1)my+ax^{2}+(a+2)\ell y^{2}\big)dy=\Omega|_{\varepsilon_{1}=\varepsilon_{2}=0}+\varepsilon_{0}dx, |  |

where in the second equality we use the expression of ℓ \ell, m m and n n in terms of a a and b. b. This shows that Ω | ε 1 = ε 2 = 0 \Omega|_{\varepsilon_{1}=\varepsilon_{2}=0} is proportional to Ω 0:= d ​ H − ε 0 a ​ H 1 − a ​ y a − 1 ​ d ​ x. \Omega_{0}\!:=dH-\frac{\varepsilon_{0}}{a}H^{1-a}y^{a-1}dx. On account of this, if we take any μ 0 = ( a, b, ε 0, 0, 0) \mu_{0}=(a,b,\varepsilon_{0},0,0) and denote by Γ s, ε 0 \Gamma_{s,\varepsilon_{0}} the oriented arc of orbit of X μ 0 X_{\mu_{0}} that joins the points ( 0, D + u ​ ( s, μ 0)) \big(0,D^{u}_{+}(s;\mu_{0})\big) and ( 0, D − u ​ ( s, μ 0)) \big(0,D^{u}_{-}(s;\mu_{0})\big) then we have that

 | 0 = ∫ Γ s, ε 0 Ω 0 = H ⁡ ( 0, D + u ​ ( s, μ 0)) − H ⁡ ( 0, D − u ​ ( s, μ 0)) − ε 0 a ​ ∫ Γ s, ε 0 H ​ ( x, y) 1 − a ​ y a − 1 ​ 𝑑 x, 0=\int_{\Gamma_{s,\varepsilon_{0}}}\Omega_{0}=H\big(0,D^{u}_{+}(s;\mu_{0})\big)-H\big(0,D^{u}_{-}(s;\mu_{0})\big)-\frac{\varepsilon_{0}}{a}\int_{\Gamma_{s,\varepsilon_{0}}}H(x,y)^{1-a}y^{a-1}dx, |  |

where D ± u ​ ( s, μ) D^{u}_{\pm}(s;\mu) is Dulac map in Lemma B.1. Consequently

 | H ⁡ ( 0, D + u ​ ( s, μ 0)) − H ⁡ ( 0, D − u ​ ( s, μ 0)) = ε 0 a ​ ∫ Γ s, ε 0 H ​ ( x, y) 1 − a ​ y a − 1 ​ 𝑑 x ​ for all ε 0 ≈ 0. H\big(0,D^{u}_{+}(s;\mu_{0})\big)-H\big(0,D^{u}_{-}(s;\mu_{0})\big)=\frac{\varepsilon_{0}}{a}\int_{\Gamma_{s,\varepsilon_{0}}}H(x,y)^{1-a}y^{a-1}dx\text{ for all $\varepsilon_{0}\approx 0.$} |  |

The derivative of this expression with respect to ε 0 \varepsilon_{0} evaluated at μ ¯ 0:= ( a, b, 0, 0, 0) \bar{\mu}_{0}\!:=(a,b,0,0,0) yields

 | ∂ y H ⁡ ( 0, D + u ​ ( s, μ ¯ 0)) ​ ∂ ε 0 D + u ​ ( s, μ ¯ 0) − ∂ y H ⁡ ( 0, D − u ​ ( s, μ ¯ 0)) ​ ∂ ε 0 D − u ​ ( s, μ ¯ 0) = 1 a ​ ∫ Γ s, 0 H ​ ( x, y) 1 − a ​ y a − 1 ​ 𝑑 x. \partial_{y}H\big(0,D^{u}_{+}(s;\bar{\mu}_{0})\big)\partial_{\varepsilon_{0}}D^{u}_{+}(s;\bar{\mu}_{0})-\partial_{y}H\big(0,D^{u}_{-}(s;\bar{\mu}_{0})\big)\partial_{\varepsilon_{0}}D^{u}_{-}(s;\bar{\mu}_{0})=\frac{1}{a}\int_{\Gamma_{s,0}}H(x,y)^{1-a}y^{a-1}dx. |  |

Our next goal will be to make s → 0 + s\to 0^{+} in this equality. With this aim in view note that, by the first assertion in Lemma B.1, D ± u ​ ( s, μ) = δ ± ​ ( μ) + ℱ ρ ∞ ​ ( μ 0) D^{u}_{\pm}(s;\mu)=\delta_{\pm}(\mu)+\mathcal{F}_{\rho}^{\infty}(\mu_{0}) for any ρ > 0 \rho>0 small enough. Consequently, since δ ± ​ ( μ ¯ 0) = 0, \delta_{\pm}(\bar{\mu}_{0})=0, we get that

 | lim s → 0 + ∂ y H ⁡ ( 0, D ± u ​ ( s, μ ¯ 0)) ​ ∂ ε 0 D ± u ​ ( s, μ ¯ 0) = ∂ y H ⁡ ( 0, 0) ​ ∂ ε 0 δ ± ​ ( μ ¯ 0) = n 1 / a ​ ∂ ε 0 δ ± ​ ( μ ¯ 0), \lim_{s\to 0^{+}}\partial_{y}H\big(0,D^{u}_{\pm}(s;\bar{\mu}_{0})\big)\partial_{\varepsilon_{0}}D^{u}_{\pm}(s;\bar{\mu}_{0})=\partial_{y}H(0,0)\partial_{\varepsilon_{0}}\delta_{\pm}(\bar{\mu}_{0})=n^{1/a}\partial_{\varepsilon_{0}}\delta_{\pm}(\bar{\mu}_{0}), |  |

where in the first equality we use the good properties of the remainder with respect to the derivation of the parameters, see Definition A, and in the second one the expression in ( 42) (\ref{lem0eq1}). Therefore

 | a ​ n 1 / a ​ ( ∂ ε 0 δ + ​ ( μ ¯ 0) − ∂ ε 0 δ − ​ ( μ ¯ 0)) = lim s → 0 + ∫ Γ s, 0 H ​ ( x, y) 1 − a ​ y a − 1 ​ 𝑑 x. an^{1/a}\big(\partial_{\varepsilon_{0}}\delta_{+}(\bar{\mu}_{0})-\partial_{\varepsilon_{0}}\delta_{-}(\bar{\mu}_{0})\big)=\lim_{s\to 0^{+}}\int_{\Gamma_{s,0}}H(x,y)^{1-a}y^{a-1}dx. |  | (43) |

Note at this point that Γ s, 0 \Gamma_{s,0} is a periodic orbit of X μ ¯ 0. X_{\bar{\mu}_{0}}. Thus it is contained inside the level set H ⁡ ( x, y) = h H(x,y)=h where h = h ⁡ ( s) h=h(s) verifies

 | h = H ⁡ ( 0, 1 / s) = s − 1 − 2 / a ​ ( ℓ + m ​ s + n ​ s 2) 1 a. h=H(0,1/s)=s^{-1-2/a}(\ell+ms+ns^{2})^{\frac{1}{a}}. |  |

Here we use ( 42) (\ref{lem0eq1}) once again and that the parametrization of Σ 1 \Sigma_{1} is given by s ↦ ( 0, 1 / s). s\mapsto(0,1/s). Since a ∈ ( − 2, 0) a\in(-2,0) by assumption, this shows that lim s → 0 + h ⁡ ( s) = 0. \lim_{s\to 0^{+}}h(s)=0. Accordingly, if we denote by γ h \gamma_{h} the periodic orbit of X μ ¯ 0 X_{\bar{\mu}_{0}} inside the level curve H = h H=h, from ( 43) (\ref{lem0eq2}) we get that

 | a ​ n 1 / a ​ ∂ ε 0 ( δ + − δ −) ​ ( μ ¯ 0) = lim h → 0 h 1 − a ​ ∫ γ h y a − 1 ​ 𝑑 x. an^{1/a}\partial_{\varepsilon_{0}}\big(\delta_{+}-\delta_{-}\big)(\bar{\mu}_{0})=\lim_{h\to 0}h^{1-a}\int_{\gamma_{h}}y^{a-1}dx. |  |

It is clear then that the result will follow once we prove that the above limit exists and is different from zero. To this end, setting γ h +:= γ h ∩ { x ⩾ 0 } \gamma_{h}^{+}\!:=\gamma_{h}\cap\{x\geqslant 0\}, we first observe that

 | ∫ γ h y a − 1 ​ 𝑑 x = 2 ​ ∫ γ h + y a − 1 ​ 𝑑 x \int_{\gamma_{h}}y^{a-1}dx=2\int_{\gamma^{+}_{h}}y^{a-1}dx |  |

since X μ ¯ 0 X_{\bar{\mu}_{0}} is symmetric with respect to x = 0 x=0. To compute this Abelian integral we perform the projective change of coordinates ( u, v) = ( 1 x, y x) (u,v)=(\frac{1}{x},\frac{y}{x}) and in these new variables, see ( 42) (\ref{lem0eq1}), we have that

 | γ h + ⊂ { H ^ ( u, v) = h a }, where H ^ ​ ( u, v):= u − a − 2 ​ v a ​ ( 1 + ℓ ​ v 2 + m ​ u ​ v + n ​ u 2). \gamma_{h}^{+}\subset\{\hat{H}(u,v)=h^{a}\},\text{ where $\hat{H}(u,v)\!:=u^{-a-2}v^{a}({1+\ell v^{2}+muv+nu^{2}}).$} |  |

A computation shows that

 | ∂ u H ^ ​ ( u, v) ∂ v H ^ ​ ( u, v) = − u v ​ ( u − 2 ​ v) ​ ( ( b − 2) ​ u − 2 ​ b ​ v) + 4 ​ a ( u − 2 ​ v) ​ ( ( b − 2) ​ u − 2 ​ b ​ v) + 4 ​ ( a + 2), \frac{\partial_{u}\hat{H}(u,v)}{\partial_{v}\hat{H}(u,v)}=-\frac{u}{v}\frac{(u-2v)\big((b-2)u-2bv\big)+4a}{(u-2v)\big((b-2)u-2bv\big)+4(a+2)}, |  | (44) |

which gives, up to a unity, the expression of the partial derivatives of H ^. \hat{H}. Then, taking ( a, b) ∈ ( − 2, 0) × ( 0, 2) (a,b)\in(-2,0)\times(0,2) into account, it follows that ∂ v H ^ ​ ( u, v) ≠ 0 \partial_{v}\hat{H}(u,v)\neq 0 on 0 < u ⩽ 2 ​ v 0<u\leqslant 2v and ∂ u H ^ ​ ( u, v) ≠ 0 \partial_{u}\hat{H}(u,v)\neq 0 on 0 < 2 ​ v ⩽ u. 0<2v\leqslant u. Observe also that, for each h > 0 h>0, the arc γ h + \gamma_{h}^{+} has exactly one intersection point with the straight line u = 2 ​ v u=2v because H ^ ​ ( u, u) = h a \hat{H}(u,u)=h^{a} if, and only if, u = ± c ⁡ ( h) u=\pm c(h) where c ( h):= ( 2 a + 2 h a − ( ℓ + 2 m + 4 n)) − 1 / 2. c(h)\!:=(2^{a+2}h^{a}-(\ell+2m+4n))^{-1/2}. Therefore, by applying (twice) the Implicit Function Theorem to H ^ ​ ( u, v) = h a \hat{H}(u,v)=h^{a} we can split γ h + \gamma_{h}^{+} as

 | γ h + = { u = u ( v; h), v ∈ [c ( h), + ∞) } ∪ { v = v ( u; h), u ∈ [c ( h), + ∞) }. \gamma_{h}^{+}=\big\{u=u(v;h),v\in[c(h),+\infty)\big\}\cup\big\{v=v(u;h),u\in[c(h),+\infty)\big\}. |  |

Accordingly, from ( 42) (\ref{lem0eq1}) once again,

 | lim h → 0 h 1 − a ​ ∫ γ h + y a − 1 ​ 𝑑 x \displaystyle\lim_{h\to 0}h^{1-a}\int_{\gamma_{h}^{+}}y^{a-1}dx | = lim h → 0 ∫ γ h + ( x 2 + ℓ ​ y 2 + m ​ y + n) 1 a − 1 ​ 𝑑 x \displaystyle=\lim_{h\to 0}\int_{\gamma_{h}^{+}}(x^{2}+\ell y^{2}+my+n)^{\frac{1}{a}-1}dx |  |

 |  | = − lim h → 0 ( ∫ c ⁡ ( h) + ∞ ( 1 + ℓ v 2 + m u v + n u 2) 1 − a a | v = v ⁡ ( u, h) u − 2 a d u \displaystyle=-\lim_{h\to 0}\left(\int_{c(h)}^{+\infty}\left.(1+\ell v^{2}+muv+nu^{2})^{\frac{1-a}{a}}\right|_{v=v(u;h)}u^{-\frac{2}{a}}du\right. |  |

 |  | − ∫ c ⁡ ( h) + ∞ ( 1 + ℓ v 2 + m v u + n u 2) 1 − a a u − 2 a | u = u ⁡ ( v, h) ∂ v u ( v; h) d v). \displaystyle\hskip 36.98866pt\left.-\int_{c(h)}^{+\infty}\left.(1+\ell v^{2}+mvu+nu^{2})^{\frac{1-a}{a}}u^{-\frac{2}{a}}\right|_{u=u(v;h)}\partial_{v}u(v;h)dv\right). |  |

In order to make this limit let us first observe that lim h → 0 c ⁡ ( h) = 0 \lim_{h\to 0}c(h)=0 due to a < 0. a<0. On the other hand, lim h → 0 u ⁡ ( v, h) = 0 \lim_{h\to 0}u(v;h)=0, uniformly in v v, and lim h → 0 v ⁡ ( u, h) = 0 \lim_{h\to 0}v(u;h)=0, uniformly in u u, because the oval γ h \gamma_{h} tends to the polycycle (in Hausdorff sense) as h → 0. h\to 0. Furthermore, due to

 | ∂ v u ⁡ ( v, h) = d ​ u d ​ v = − ∂ v H ^ ​ ( u, v) ∂ u H ^ ​ ( u, v) | u = u ⁡ ( v, h), \partial_{v}u(v;h)=\frac{du}{dv}=-\left.\frac{\partial_{v}\hat{H}(u,v)}{\partial_{u}\hat{H}(u,v)}\right|_{u=u(v;h)}, |  |

from the expression in ( 44) (\ref{lem0eq3}) we deduce that | ∂ v u ⁡ ( v, h) | |\partial_{v}u(v;h)| is uniformly bounded since 0 < u ⁡ ( v, h) ⩽ 2 ​ v 0<u(v;h)\leqslant 2v for any v ∈ [c ( h), + ∞) v\in[c(h),+\infty). Taking these facts into account, together with the assumption a ∈ ( − 2, 0) a\in(-2,0), by applying the Dominated Convergence Theorem we conclude that

 | lim h → 0 h 1 − a ∫ γ h + y a − 1 d x = − ∫ 0 + ∞ ( 1 + n u 2) 1 − a a u − 2 a d u =: p ∈ ℝ < 0. \lim_{h\to 0}h^{1-a}\int_{\gamma_{h}^{+}}y^{a-1}dx=-\int_{0}^{+\infty}(1+nu^{2})^{\frac{1-a}{a}}u^{-\frac{2}{a}}du=:\!p\in\mathbb{R}_{<0}. |  |

Hence ∂ ε 0 ( δ + − δ −) ​ ( μ ¯ 0) = 2 p n − 1 / a a > 0 \partial_{\varepsilon_{0}}\big(\delta_{+}-\delta_{-}\big)(\bar{\mu}_{0})=\frac{2pn^{-1/a}}{a}>0 and this finishes the proof of the result.

The three assertions with regard to structure of the asymptotic development follow from Lemma B.1 setting Δ i u:= Δ i + − Δ i − \Delta^{u}_{i}\!:=\Delta_{i}^{+}-\Delta_{i}^{-} for i = 0, 1, 2 i=0,1,2 and δ u:= δ + − δ − \delta_{u}\!:=\delta_{+}-\delta_{-} because then

 | 𝒟 u ​ ( s, μ) = D + ​ ( s, μ) − D − ​ ( s, μ) = δ u ​ ( μ) + Δ 0 u ​ ( μ) ​ s λ + { Δ 1 u ​ ( μ) ​ s λ + 1 + ℱ ℓ 1 ∞ ​ ( μ 0) if a 0 > − 1, Δ 2 u ​ ( μ) ​ s 2 ​ λ + ℱ ℓ 2 ∞ ​ ( μ 0) if a 0 < − 1, \mathscr{D}_{u}(s;\mu)=D_{+}(s;\mu)-D_{-}(s;\mu)=\delta_{u}(\mu)+\Delta^{u}_{0}({\mu})s^{\lambda}+\left\{\begin{array}[]{ll}\Delta^{u}_{1}({\mu})s^{\lambda+1}+\mathcal{F}_{\ell_{1}}^{\infty}(\mu_{0})&\text{ if $a_{0}>-1,$}\\[10.0pt] \Delta^{u}_{2}({\mu})s^{2\lambda}+\mathcal{F}_{\ell_{2}}^{\infty}(\mu_{0})&\text{ if $a_{0}<-1,$}\end{array}\right. |  | (45) |

for any ℓ 2 ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, λ 0 + 1)) {\ell_{2}}\in\big[2\lambda_{0},\min(3\lambda_{0},\lambda_{0}+1)\big) and ℓ 1 ∈ [λ 0 + 1, min ( 2 λ 0, λ 0 + 2)) {\ell_{1}}\in\big[\lambda_{0}+1,\min(2\lambda_{0},\lambda_{0}+2)\big). Since we will deal with the “upper case” only, for simplicity in the exposition we shall omit any subscript and superscript u u from now on.

It is clear that 𝒟 ⁡ ( s, μ 0) ≡ 0 \mathscr{D}(s;{\mu_{0}})\equiv 0 because X μ X_{\mu} is inside the center variety when μ = μ 0 \mu=\mu_{0}. On the other hand, by Lemma B.2, ∂ ε 0 δ ⁡ ( μ 0) > 0 \partial_{\varepsilon_{0}}\delta(\mu_{0})>0. Note also that the straight line y = 0 y=0 is invariant in case that ε 0 = 0. \varepsilon_{0}=0. Hence δ ⁡ ( μ) | ε 0 = 0 ≡ 0 \delta(\mu)|_{\varepsilon_{0}=0}\equiv 0 by definition and, consequently, ∂ ε 1 δ ⁡ ( μ 0) = ∂ ε 2 δ ⁡ ( μ 0) = 0. \partial_{\varepsilon_{1}}\delta(\mu_{0})=\partial_{\varepsilon_{2}}\delta(\mu_{0})=0. That being stablished, our main task is to compute the partial derivatives ∂ ε 1 Δ k \partial_{\varepsilon_{1}}\Delta_{k} and ∂ ε 2 Δ k \partial_{\varepsilon_{2}}\Delta_{k} evaluated at μ 0 = ( a 0, b 0, 0, 0, 0) \mu_{0}=(a_{0},b_{0},0,0,0) for each k = 0, 1, 2. k=0,1,2. To this end the key point is that we can perform the computations setting ε 0 = 0 \varepsilon_{0}=0 and that in this case X μ X_{\mu} is a D-system, more concretely, with f ⁡ ( x, y) = 1 − b + ε 2 ​ x + b ​ y, f(x,y)=1-b+\varepsilon_{2}x+by, g ⁡ ( x) = b − 2 4 + ε 1 ​ x + a ​ x 2 g(x)=\frac{b-2}{4}+\varepsilon_{1}x+ax^{2}, q ⁡ ( x, y) = − 2 ​ x q(x,y)=-2x and n = 1, n=1, so that

 | ℓ 2 ​ ( x, y) = ( a + 2) ​ x 2 + ε 2 ​ x ​ y + b ​ y 2. \ell_{2}(x,y)=(a+2)x^{2}+\varepsilon_{2}xy+by^{2}. |  |

Let us remark that it is only for ε 0 = 0 \varepsilon_{0}=0 that X μ X_{\mu} becomes a D-system. Thus, for the sake of consistency we shall denote μ ¯ = ( a, b, ε 1, ε 2) \bar{\mu}=(a,b,\varepsilon_{1},\varepsilon_{2}) and μ ¯ 0 = ( a, b, 0, 0) \bar{\mu}_{0}=(a,b,0,0). That being said, following the notation in Theorem 2.1, that we stress it is addressed to D-systems, from ( 2) (\ref{K}) we have

 | K ⁡ ( x 1, x 2, μ ¯) = 1 − x ​ q ​ ( x, y) y ​ f ​ ( x, y) + g ⁡ ( x) | ( x, y) = ( 1 x 1, x 2 x 1) = 1 + 2 a + ε 1 ​ x 1 + ε 2 ​ x 2 + b − 2 4 ​ x 1 2 + ( 1 − b) ​ x 1 ​ x 2 + b ​ x 2 2. K(x_{1},x_{2};\bar{\mu})=\left.1-\frac{xq(x,y)}{yf(x,y)+g(x)}\right|_{(x,y)=\left(\frac{1}{x_{1}},\frac{x_{2}}{x_{1}}\right)}=1+\frac{2}{a+\varepsilon_{1}x_{1}+\varepsilon_{2}x_{2}+\frac{b-2}{4}x_{1}^{2}+(1-b)x_{1}x_{2}+bx_{2}^{2}}. |  |

Hence λ ⁡ ( μ ¯) = − a + 2 a. \lambda(\bar{\mu})=-\frac{a+2}{a}. From ( 6) (\ref{d0}) we get that

 | d 0 ​ ( μ ¯) \displaystyle d_{0}(\bar{\mu}) | = 2 ​ ∫ − ∞ + ∞ ( z b − 2 4 + ε 1 ​ z + a ​ z 2 + λ ​ z ( a + 2) ​ z 2 + ε 2 ​ z + b) ​ 𝑑 z \displaystyle=2\int_{-\infty}^{+\infty}\left(\frac{z}{\frac{b-2}{4}+\varepsilon_{1}z+az^{2}}+\lambda\frac{z}{(a+2)z^{2}+\varepsilon_{2}z+b}\right)dz |  |

 |  | = 2 ​ π a ​ ( ε 1 ( b − 2) ​ a − ε 1 2 + ε 2 4 ​ b ​ ( a + 2) − ε 2 2). \displaystyle=\frac{2\pi}{a}\left(\frac{\varepsilon_{1}}{\sqrt{(b-2)a-\varepsilon_{1}^{2}}}+\frac{\varepsilon_{2}}{\sqrt{4b(a+2)-\varepsilon_{2}^{2}}}\right). |  |

On account of this one can verify that d 0 ​ ( μ ¯) = − ρ 0 ​ ( μ ¯) ​ ( 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 + ε 2) d_{0}(\bar{\mu})=-\rho_{0}(\bar{\mu})\Big(2\frac{\sqrt{b(a+2)}}{\sqrt{a(b-2)}}\,\varepsilon_{1}+\varepsilon_{2}\Big) where ρ 0 \rho_{0} is a smooth function with ρ 0 ​ ( μ ¯ 0) > 0 \rho_{0}(\bar{\mu}_{0})>0 since a 0 ∈ ( − 2, 0). a_{0}\in(-2,0). Hence, from ( 45) (\ref{lem2eq0}) and applying Theorem 2.1,

 | Δ 0 ​ ( μ) | ε 0 = 0 = − κ 01 ​ ( μ ¯) ​ ( 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 + ε 2) ​ with κ 01 ​ ( μ ¯ 0) > 0. \left.\Delta_{0}(\mu)\right|_{\varepsilon_{0}=0}=-\kappa_{01}(\bar{\mu})\left(2\frac{\sqrt{b(a+2)}}{\sqrt{a(b-2)}}\,\varepsilon_{1}+\varepsilon_{2}\right)\text{ with $\kappa_{01}(\bar{\mu}_{0})>0.$} |  |

Consequently, there exists a smooth function ρ 1 = ρ 1 ​ ( μ) \rho_{1}=\rho_{1}(\mu) such that

 | Δ 0 ​ ( μ) = − κ 01 ​ ( μ ¯) ​ ( 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 + ε 2) + ε 0 ​ ρ 1 ​ ( μ) = − κ 01 ​ ( μ ¯) ​ ( 2 ​ b ⁡ ( a + 2) a ⁡ ( b − 2) ​ ε 1 + ε 2) + κ 02 ​ ( μ) ​ δ ​ ( μ), \Delta_{0}(\mu)=-\kappa_{01}(\bar{\mu})\left(2\frac{\sqrt{b(a+2)}}{\sqrt{a(b-2)}}\,\varepsilon_{1}+\varepsilon_{2}\right)+\varepsilon_{0}\rho_{1}(\mu)=-\kappa_{01}(\bar{\mu})\left(2\frac{\sqrt{b(a+2)}}{\sqrt{a(b-2)}}\,\varepsilon_{1}+\varepsilon_{2}\right)+\kappa_{02}(\mu)\delta(\mu), |  |

where in the second equality we use that we can write δ ⁡ ( μ) = ε 0 ​ ρ 2 ​ ( μ) \delta(\mu)=\varepsilon_{0}\rho_{2}(\mu) with ρ 2 ​ ( μ 0) ≠ 0 \rho_{2}(\mu_{0})\neq 0 due to δ ⁡ ( μ) | ε 0 = 0 ≡ 0 \delta(\mu)|_{\varepsilon_{0}=0}\equiv 0 and ∂ ε 0 δ ⁡ ( μ 0) ≠ 0 \partial_{\varepsilon_{0}}\delta(\mu_{0})\neq 0. Since κ 01 ​ ( μ ¯) \kappa_{01}(\bar{\mu}) is a smooth function on μ \mu, this proves the assertion with regard to Δ 0 ​ ( μ). \Delta_{0}(\mu).

Let us assume now that a 0 ∈ ( − 2, − 1) a_{0}\in(-2,-1) and turn to the study of Δ 2 \Delta_{2}. This, on account of Theorem 2.1, leads to the computation of F 2 F_{2}. According to ( 4) (\ref{F2}) its expression is given by

 | F 2 ​ ( μ ¯) = ∫ 0 + ∞ ( M 2 ​ ( − z) − M 2 ​ ( 0) + exp ⁡ ( G 2) ​ ( M 2 ​ ( z) − M 2 ​ ( 0))) ​ d ​ z z 1 + λ F_{2}(\bar{\mu})=\int_{0}^{+\infty}\Big(M_{2}(-z)-M_{2}(0)+\exp(G_{2})\big(M_{2}(z)-M_{2}(0)\big)\Big)\frac{dz}{z^{1+\lambda}} |  | (46) |

where M 2 ​ ( u) = L 2 ​ ( u) ​ ∂ 2 K ⁡ ( u, 0) M_{2}(u)=L_{2}(u)\partial_{2}K(u,0) with L 2 ​ ( u):= exp ⁡ ( ∫ 0 u ( K ⁡ ( z, 0) + λ) ​ d ​ z z). L_{2}(u)\!:=\exp\left(\int_{0}^{u}\big(K(z,0)+\lambda\big)\frac{dz}{z}\right). After some lengthy computations we obtain that

 | L 2 ​ ( u) = ( 1 + ε 1 a ​ u + η 2 ​ u 2) − 1 a ​ B 2 ​ ( u), L_{2}(u)=\left(1+\frac{\varepsilon_{1}}{a}u+{\eta_{2}}u^{2}\right)^{-\frac{1}{a}}B_{2}(u), |  |

where η 2:= b − 2 4 ​ a > 0 {\eta_{2}}\!:=\frac{b-2}{4a}>0 for all ( a, b) ∈ ( − 2, 0) × ( 0, 2) (a,b)\in(-2,0)\times(0,2) and

 | B 2 ​ ( u):= exp ⁡ ( − 2 ​ ε 1 a ​ a ⁡ ( b − 2) − ε 1 2 ​ ( arctan ⁡ ( b − 2 2 ​ u + ε 1 a ⁡ ( b − 2) − ε 1 2) − arctan ⁡ ( ε 1 a ⁡ ( b − 2) − ε 1 2))). B_{2}(u)\!:=\exp\left(\frac{-2\varepsilon_{1}}{a\sqrt{a(b-2)-\varepsilon_{1}^{2}}}\left(\arctan\left(\frac{\frac{b-2}{2}u+\varepsilon_{1}}{\sqrt{a\left(b-2\right)-\varepsilon_{1}^{2}}}\right)-\arctan\left(\frac{\varepsilon_{1}}{\sqrt{a(b-2)-\varepsilon_{1}^{2}}}\right)\right)\right). |  |

The explicit computation of F 2 ​ ( μ ¯) F_{2}(\bar{\mu}) for arbitrary μ ¯ \bar{\mu} requires a primitive of u ↦ ( M 2 ​ ( u) − M 2 ​ ( 0)) ​ u − 1 − λ, u\mapsto(M_{2}(u)-M_{2}(0))\,u^{-1-\lambda}, which is not feasible because M 2 ​ ( u) = L 2 ​ ( u) ​ ∂ 2 K ⁡ ( u, 0) M_{2}(u)=L_{2}(u)\partial_{2}K(u,0) where

 | ∂ 2 K ⁡ ( u, 0) = 2 a 2 ​ ( b − 1) ​ u − ε 2 ( 1 + ε 1 a ​ u + η 2 ​ u 2) 2. \partial_{2}K(u,0)=\frac{2}{a^{2}}\frac{(b-1)u-\varepsilon_{2}}{\big(1+\frac{\varepsilon_{1}}{a}u+{\eta_{2}}u^{2}\big)^{2}}. |  |

To bypass this problem the strategy is to compute only the first order Taylor’s expansion of this function at ( ε 1, ε 2) = ( 0, 0). (\varepsilon_{1},\varepsilon_{2})=(0,0). In doing so we get

 | M 2 ​ ( u) − M 2 ​ ( 0) = \displaystyle M_{2}(u)-M_{2}(0)= | 2 ​ ( b − 1) a 2 ​ u ​ ( 1 + η 2 ​ u 2) − 2 − 1 a \displaystyle\,\frac{2(b-1)}{a^{2}}\,u(1+{\eta_{2}}u^{2})^{-2-\frac{1}{a}} |  |

 |  | − 2 ​ ( b − 1) a 4 ​ η 2 ​ u ​ ( 1 + η 2 ​ u 2) − 3 − 1 a ​ ( ( 1 + η 2 ​ u 2) ​ arctan ⁡ ( η 2 ​ u) + η 2 ​ ( 1 + 2 ​ a) ​ u) ​ ε 1 \displaystyle-\frac{2(b-1)}{a^{4}\sqrt{{\eta_{2}}}}\,u(1+{\eta_{2}}u^{2})^{-3-\frac{1}{a}}\big((1+{\eta_{2}}u^{2})\arctan(\sqrt{{\eta_{2}}}u)+\sqrt{{\eta_{2}}}(1+2a)u\big)\varepsilon_{1} |  |

 |  | − 2 a 2 ​ ( ( 1 + η 2 ​ u 2) − 2 − 1 a − 1) ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖). \displaystyle-\frac{2}{a^{2}}\big((1+{\eta_{2}}u^{2})^{-2-\frac{1}{a}}-1\big)\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|). |  |

Thus, on account of the parity of each coefficient with respect to u, u, if we write

 | ∫ 0 + ∞ ( M 2 ​ ( ± u) − M 2 ​ ( 0)) ​ d ​ u u 1 + λ = m 0 ± + m 1 ± ​ ε 1 + m 2 ± ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖) \int_{0}^{+\infty}\big(M_{2}(\pm u)-M_{2}(0)\big)\frac{du}{u^{1+\lambda}}=m_{0}^{\pm}+m_{1}^{\pm}\varepsilon_{1}+m_{2}^{\pm}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) |  | (47) |

then it turns out that m 0 − = − m 0 + m_{0}^{-}=-m_{0}^{+}, m 1 − = m 1 + m_{1}^{-}=m_{1}^{+} and m 2 − = m 2 + m_{2}^{-}=m_{2}^{+}. Of course to obtain the above equality we must prove that the higher order terms can also be neglected after integration. To show this let us note first that, as a matter of fact, the higher order terms do not depend on ε 2 \varepsilon_{2} because M 2 ​ ( u, μ ¯) M_{2}(u;\bar{\mu}) is linear in this parameter. Therefore to get m 0 ± m_{0}^{\pm} we need a result to pass the limit ε 1 → 0 \varepsilon_{1}\to 0 under the integral sign, and to get m 1 ± m_{1}^{\pm} a similar result for the derivation with respect to ε 1 \varepsilon_{1}. With this aim we appeal to the results in [34, §17.2] about improper integrals depending on a parameter. More concretely, Proposition 2, which is a sort of Weierstrass test for the uniform convergence of an improper integral depending on a parameter, and Proposition 6, that gives sufficient conditions for the differentiation of an improper integral with respect to a parameter. To this end the key points are that, on one hand, λ = λ ⁡ ( μ ¯) = − a + 2 a ∈ ( 0, 1) \lambda=\lambda(\bar{\mu})=-\frac{a+2}{a}\in(0,1) for μ ¯ ≈ μ ¯ 0 \bar{\mu}\approx\bar{\mu}_{0} due to a 0 ∈ ( − 2, − 1) a_{0}\in(-2,-1) and, on the other hand, that B 2 ​ ( u, μ ¯) B_{2}(u;\bar{\mu}) and ∂ ε 1 B 2 ​ ( u, μ ¯) \partial_{\varepsilon_{1}}B_{2}(u;\bar{\mu}) are bounded for u ∈ ( 0, + ∞) u\in(0,+\infty) and ε 1 ≈ 0 \varepsilon_{1}\approx 0 by a constant. That being said, some computations show that

 | m 0 + = \displaystyle m_{0}^{+}= | 2 ​ ( b − 1) a 2 ​ ∫ 0 + ∞ ( 1 + η 2 ​ u 2) − 2 − 1 a ​ u 2 a + 1 ​ 𝑑 u = ( b − 1) ​ η 2 − 1 − 1 a a ⁡ ( a + 1) \displaystyle\frac{2(b-1)}{a^{2}}\int_{0}^{+\infty}(1+{\eta_{2}}u^{2})^{-2-\frac{1}{a}}u^{\frac{2}{a}+1}du=\frac{(b-1){\eta_{2}}^{-1-\frac{1}{a}}}{a(a+1)} |  |

and |

 | m 2 + = \displaystyle m_{2}^{+}= | − 2 a 2 ∫ 0 + ∞ ( ( 1 + η 2 u 2) − 2 − 1 a − 1) u 2 a d u = − π 2 ​ a 2 Γ ⁡ ( a + 2 2 ​ a) Γ ⁡ ( 2 ​ a + 1 a) η 2 − a + 2 2 ​ a. \displaystyle-\frac{2}{a^{2}}\int_{0}^{+\infty}\big((1+{\eta_{2}}u^{2})^{-2-\frac{1}{a}}-1\big)u^{\frac{2}{a}}du=-\frac{\sqrt{\pi}}{2a^{2}}\frac{\Gamma\left(\frac{a+2}{2a}\right)}{\Gamma\left(\frac{2a+1}{a}\right)}{\eta_{2}}^{-\frac{a+2}{2a}}. |  |

One can readily check in particular that m 2 + > 0 m_{2}^{+}>0 for all ( a, b) ∈ ( − 2, − 1) × ( 0, 2). (a,b)\in(-2,-1)\times(0,2). Computing m 1 + m_{1}^{+} is a little more involved. In this case

 | − a 4 2 ​ ( b − 1) ​ m 1 + = \displaystyle-\frac{a^{4}}{2(b-1)}m_{1}^{+}= | 1 η 2 ​ ∫ 0 + ∞ ( 1 + η 2 ​ u 2) − 2 − 1 a ​ arctan ⁡ ( η 2 ​ u) ​ u 1 + 2 a ​ 𝑑 u + ( 1 + 2 ​ a) ​ ∫ 0 + ∞ ( 1 + η 2 ​ u 2) − 3 − 1 a ​ u 2 + 2 a ​ 𝑑 u \displaystyle\frac{1}{\sqrt{{\eta_{2}}}}\int_{0}^{+\infty}(1+{\eta_{2}}u^{2})^{-2-\frac{1}{a}}\arctan(\sqrt{{\eta_{2}}}u)u^{1+\frac{2}{a}}du+(1+2a)\int_{0}^{+\infty}(1+{\eta_{2}}u^{2})^{-3-\frac{1}{a}}u^{2+\frac{2}{a}}du |  |

 | = \displaystyle= | a ​ π ​ η 2 − 3 ​ a + 2 2 ​ a 4 ​ ( 1 + a) − a ​ π 4 ​ ( a + 1) ​ Γ ⁡ ( 3 ​ a + 2 2 ​ a) Γ ⁡ ( 2 ​ a + 1 a) ​ η 2 − 3 ​ a + 2 2 ​ a + ( 1 + 2 ​ a) ​ π 4 ​ Γ ⁡ ( 3 ​ a + 2 2 ​ a) Γ ⁡ ( 3 ​ a + 1 a) ​ η 2 − 3 ​ a + 2 2 ​ a, \displaystyle\frac{a\pi{\eta_{2}}^{-\frac{3a+2}{2a}}}{4(1+a)}-\frac{a\sqrt{\pi}}{4(a+1)}\frac{\Gamma\left(\frac{3a+2}{2a}\right)}{\Gamma\left(\frac{2a+1}{a}\right)}{\eta_{2}}^{-\frac{3a+2}{2a}}+(1+2a)\frac{\sqrt{\pi}}{4}\frac{\Gamma\left(\frac{3a+2}{2a}\right)}{\Gamma\left(\frac{3a+1}{a}\right)}{\eta_{2}}^{-\frac{3a+2}{2a}}, |  |

and after some simplifications we get that

 | m 1 + = − π ​ ( b − 1) 2 ​ a 2 ​ ( a + 1) ​ ( Γ ⁡ ( 3 ​ a + 2 2 ​ a) Γ ⁡ ( 2 ​ a + 1 a) + π a) ​ η 2 − 3 ​ a + 2 2 ​ a. m_{1}^{+}=-\frac{\sqrt{\pi}(b-1)}{2a^{2}(a+1)}\left(\frac{\Gamma\left(\frac{3a+2}{2a}\right)}{\Gamma\left(\frac{2a+1}{a}\right)}+\frac{\sqrt{\pi}}{a}\right){\eta_{2}}^{-\frac{3a+2}{2a}}. |  |

On the other hand,

 | G 2 = ∫ 0 + ∞ ( q ⁡ ( u, 0) g ⁡ ( u) + q ⁡ ( − u, 0) g ⁡ ( − u)) ​ 𝑑 u = − 2 ​ π ​ ε 1 a ​ ( b − 2) ​ a − ε 1 2, G_{2}=\int_{0}^{+\infty}\left(\frac{q(u,0)}{g(u)}+\frac{q(-u,0)}{g(-u)}\right)du=-\frac{2\pi\varepsilon_{1}}{a\sqrt{(b-2)a-\varepsilon_{1}^{2}}}, |  |

so that exp ⁡ ( G 2) = 1 + 2 ​ π a 3 ​ ( b − 2) ​ ε 1 + o ​ ( ε 1) \exp(G_{2})=1+\frac{2\pi}{\sqrt{a^{3}(b-2)}}\varepsilon_{1}+\mbox{\rm o}(\varepsilon_{1}) due to a < 0. a<0. Accordingly the substitution of ( 47) (\ref{lem2eq4}) in ( 46) (\ref{lem2eq0bis}) yields

 | F 2 \displaystyle F_{2} | = m 0 − + m 1 − ​ ε 1 + m 2 − ​ ε 2 + ( 1 + 2 ​ π a 3 ​ ( b − 2) ​ ε 1) ​ ( m 0 + + m 1 + ​ ε 1 + m 2 + ​ ε 2) + o ​ ( ‖ ( ε 1, ε 2) ‖) \displaystyle=m_{0}^{-}+m_{1}^{-}\varepsilon_{1}+m_{2}^{-}\varepsilon_{2}+\left(1+\frac{2\pi}{\sqrt{a^{3}(b-2)}}\varepsilon_{1}\right)\left(m_{0}^{+}+m_{1}^{+}\varepsilon_{1}+m_{2}^{+}\varepsilon_{2}\right)+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) |  |

 |  | = m 0 − + m 0 + + ( m 1 − + m 1 + + 2 ​ π a 3 ​ ( b − 2) ​ m 0 +) ​ ε 1 + ( m 2 − + m 2 +) ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖) \displaystyle=m_{0}^{-}+m_{0}^{+}+\left(m_{1}^{-}+m_{1}^{+}+\frac{2\pi}{\sqrt{a^{3}(b-2)}}m_{0}^{+}\right)\varepsilon_{1}+\left(m_{2}^{-}+m_{2}^{+}\right)\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) |  |

 |  | = 2 ​ ( m 1 + + π a 3 ​ ( b − 2) ​ m 0 +) ​ ε 1 + 2 ​ m 2 + ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖) \displaystyle=2\left(m_{1}^{+}+\frac{\pi}{\sqrt{a^{3}(b-2)}}m_{0}^{+}\right)\varepsilon_{1}+2m_{2}^{+}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) |  |

and let us note that

 | m 1 + + π a 3 ​ ( b − 2) ​ m 0 + = − π 2 ​ a 2 ​ b − 1 a + 1 ​ Γ ⁡ ( 3 ​ a + 2 2 ​ a) Γ ⁡ ( 2 ​ a + 1 a) ​ η 2 − 3 ​ a + 2 2 ​ a. m_{1}^{+}+\frac{\pi}{\sqrt{a^{3}(b-2)}}m_{0}^{+}=-\frac{\sqrt{\pi}}{2a^{2}}\frac{b-1}{a+1}\frac{\Gamma\left(\frac{3a+2}{2a}\right)}{\Gamma\left(\frac{2a+1}{a}\right)}{\eta_{2}}^{-\frac{3a+2}{2a}}. |  |

Hence m 1 + + π a 3 ​ ( b − 2) ​ m 0 + = 2 ​ ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) ​ m 2 +, m_{1}^{+}+\frac{\pi}{\sqrt{a^{3}(b-2)}}m_{0}^{+}=\frac{2(a+2)(b-1)}{(a+1)(b-2)}m_{2}^{+}, so that

 | F 2 ​ ( μ ¯) = ρ 3 ​ ( μ ¯) ​ ( 2 ​ ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) ​ ε 1 + ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) ​ with ρ 3 ​ ( μ ¯ 0) > 0. F_{2}(\bar{\mu})=\rho_{3}(\bar{\mu})\left(\frac{2(a+2)(b-1)}{(a+1)(b-2)}\varepsilon_{1}+\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)\text{ with $\rho_{3}(\bar{\mu}_{0})>0.$} |  |

Finally, from ( 45) (\ref{lem2eq0}) and the last assertion in ( 2) (2) of Theorem 2.1 we get that

 | Δ 2 ​ ( μ) | ε 0 = 0 = κ 21 ​ ( μ ¯) ​ ( 2 ​ ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) ​ ε 1 + ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) + κ 22 ​ ( μ ¯) ​ Δ 0 ​ ( μ) | ε 0 = 0 ​ with κ 21 ​ ( μ ¯ 0) > 0. \left.\Delta_{2}(\mu)\right|_{\varepsilon_{0}=0}=\kappa_{21}(\bar{\mu})\left(\frac{2(a+2)(b-1)}{(a+1)(b-2)}\varepsilon_{1}+\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)+\kappa_{22}(\bar{\mu})\left.\Delta_{0}(\mu)\right|_{\varepsilon_{0}=0}\text{ with $\kappa_{21}(\bar{\mu}_{0})>0.$} |  |

Let us stress here that κ 21 \kappa_{21} and κ 22 \kappa_{22} are smooth functions in a neighbourhood of μ ¯ 0 \bar{\mu}_{0} provided that a 0 ∈ ( − 2, − 1). a_{0}\in(-2,-1). Consequently, since δ ⁡ ( μ) | ε 0 = 0 ≡ 0 \delta(\mu)|_{\varepsilon_{0}=0}\equiv 0 and ∂ ε 0 δ ⁡ ( μ 0) ≠ 0 \partial_{\varepsilon_{0}}\delta(\mu_{0})\neq 0, we get that

 | Δ 2 ​ ( μ) = κ 21 ​ ( μ ¯) ​ ( 2 ​ ( a + 2) ​ ( b − 1) ( a + 1) ​ ( b − 2) ​ ε 1 + ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) + κ 22 ​ ( μ ¯) ​ Δ 0 ​ ( μ) + κ 23 ​ ( μ) ​ δ ​ ( μ) \Delta_{2}(\mu)=\kappa_{21}(\bar{\mu})\left(\frac{2(a+2)(b-1)}{(a+1)(b-2)}\varepsilon_{1}+\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)+\kappa_{22}(\bar{\mu})\Delta_{0}(\mu)+\kappa_{23}(\mu)\delta(\mu) |  |

for some smooth function κ 23 \kappa_{23} and this proves the assertion in ( 2). (2).

So far we have studied the coefficient Δ 2 \Delta_{2} assuming a 0 ∈ ( − 2, − 1), a_{0}\in(-2,-1), i.e., λ 0 < 1. \lambda_{0}<1. Our next task is to do the same for the coefficient Δ 1 \Delta_{1} assuming a 0 ∈ ( − 1, 0), a_{0}\in(-1,0), i.e., λ 0 > 1. \lambda_{0}>1. In this case, see ( 3) (\ref{F1}), we have to compute

 | F 1 ( μ) = − ∫ 0 + ∞ ( M 1 ( z) − M 1 ( 0) + exp ( G 1) ( M 1 ( − z) − M 1 ( 0))) d ​ z z 1 + 1 / λ, F_{1}(\mu)=-\int_{0}^{+\infty}\Big(M_{1}(z)-M_{1}(0)+\exp(G_{1})\big(M_{1}(-z)-M_{1}(0)\big)\Big)\frac{dz}{z^{1+1/\lambda}}, |  | (48) |

where M 1 ​ ( u) = L 1 ​ ( u) ​ ∂ 1 ( 1 K) ​ ( 0, u) M_{1}(u)=L_{1}(u)\partial_{1}\big(\frac{1}{K}\big)(0,u) with L 1 ​ ( u):= exp ⁡ ( ∫ 0 u ( 1 K ⁡ ( 0, z) + 1 λ) ​ d ​ z z). L_{1}(u)\!:=\exp\left(\int_{0}^{u}\left(\frac{1}{K(0,z)}+\frac{1}{\lambda}\right)\frac{dz}{z}\right). In doing so exactly as before we obtain that

 | L 1 ​ ( u) = ( 1 + ε 2 a + 2 ​ u + η 1 ​ u 2) 1 a + 2 ​ B 1 ​ ( u), L_{1}(u)=\left(1+\frac{\varepsilon_{2}}{a+2}u+\eta_{1}u^{2}\right)^{\frac{1}{a+2}}B_{1}(u), |  |

where η 1:= b a + 2 > 0 \eta_{1}\!:=\frac{b}{a+2}>0 for all ( a, b) ∈ ( − 2, 0) × ( 0, 2) (a,b)\in(-2,0)\times(0,2) and

 | B 1 ​ ( u):= exp ⁡ ( 2 ​ ε 2 ( a + 2) ​ 4 ​ b ​ ( a + 2) − ε 2 2 ​ ( arctan ⁡ ( 2 ​ b ​ u + ε 2 4 ​ b ​ ( a + 2) − ε 2 2) − arctan ⁡ ( ε 2 4 ​ b ​ ( a + 2) − ε 2 2))). B_{1}(u)\!:=\exp\left(\frac{2\varepsilon_{2}}{(a+2)\sqrt{4b(a+2)-\varepsilon_{2}^{2}}}\left(\arctan\left(\frac{2bu+\varepsilon_{2}}{\sqrt{4b(a+2)-\varepsilon_{2}^{2}}}\right)-\arctan\left(\frac{\varepsilon_{2}}{\sqrt{4b(a+2)-\varepsilon_{2}^{2}}}\right)\right)\right). |  |

Since one can also verify that

 | ∂ 1 ( 1 K) ​ ( 0, u) = 2 ( a + 2) 2 ​ ( 1 − b) ​ u + ε 1 ( 1 + ε 2 a + 2 ​ u + η 1 ​ u 2) 2, \partial_{1}\!\left(\frac{1}{K}\right)(0,u)=\frac{2}{(a+2)^{2}}\frac{(1-b)u+\varepsilon_{1}}{\big(1+\frac{\varepsilon_{2}}{a+2}u+\eta_{1}u^{2}\big)^{2}}, |  |

it turns out that the function M 1 ​ ( u) = L 1 ​ ( u) ​ ∂ 1 ( 1 K) ​ ( 0, u) M_{1}(u)=L_{1}(u)\partial_{1}\!\left(\frac{1}{K}\right)(0,u) is linear in ε 1 \varepsilon_{1}. That being said, some computations show that

 | M 1 ​ ( u) − M 1 ​ ( 0) \displaystyle M_{1}(u)-M_{1}(0) | = 2 ​ ( 1 − b) ( a + 2) 2 ​ u ​ ( 1 + η 1 ​ u 2) − 2 ​ a + 3 a + 2 \displaystyle=\frac{2(1-b)}{(a+2)^{2}}u(1+{\eta_{1}}u^{2})^{-\frac{2a+3}{a+2}} |  |

 |  | + 2 ( a + 2) 2 ​ ( ( 1 + η 1 ​ u 2) − 2 ​ a + 3 a + 2 − 1) ​ ε 1 \displaystyle+\frac{2}{(a+2)^{2}}\left((1+{\eta_{1}}u^{2})^{-\frac{2a+3}{a+2}}-1\right)\varepsilon_{1} |  |

 |  | + 2 ​ ( 1 − b) ​ u ( a + 2) 3 ​ b ⁡ ( a + 2) ​ ( 1 + η 1 ​ u 2) − 2 ​ a + 3 a + 2 ​ ( arctan ⁡ ( η 1 ​ u) − ( 2 ​ a + 3) ​ η 1 ​ u 1 + η 1 ​ u 2) ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖). \displaystyle+\frac{2(1-b)u}{(a+2)^{3}\sqrt{b(a+2)}}(1+{\eta_{1}}u^{2})^{-\frac{2a+3}{a+2}}\left(\arctan(\sqrt{{\eta_{1}}}u)-\frac{(2a+3)\sqrt{{\eta_{1}}}u}{1+{\eta_{1}}u^{2}}\right)\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|). |  |

Following the obvious notation, if we write

 | ∫ 0 + ∞ ( M 1 ​ ( ± u) − M 1 ​ ( 0)) ​ u − 1 − 1 / λ ​ 𝑑 u = n 0 ± + n 1 ± ​ ε 1 + n 2 ± ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖), \int_{0}^{+\infty}\big(M_{1}(\pm u)-M_{1}(0)\big)u^{-1-1/\lambda}du=n_{0}^{\pm}+n_{1}^{\pm}\varepsilon_{1}+n_{2}^{\pm}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|), |  |

then n 0 − = − n 0 + n_{0}^{-}=-n_{0}^{+}, n 1 − = n 1 + n_{1}^{-}=n_{1}^{+} and n 2 − = n 2 + n_{2}^{-}=n_{2}^{+} due to the parity of each coefficient with respect to u. u. Here we follow exactly the same strategy as before, by using the results from [34, §17.2] about improper integrals depending on a parameter, to show that the higher order terms can be neglected after integration. Moreover

 | G 1 = ∫ − 1 1 ( q n ​ ( 1, z) ℓ n + 1 ​ ( 1, z) + 1 + 1 λ + z ​ q n ​ ( z, 1) ℓ n + 1 ​ ( z, 1)) ​ d ​ z z = 2 ​ π ​ ε 2 ( a + 2) ​ 4 ​ b ​ ( a + 2) − ε 2 2, G_{1}=\int_{-1}^{1}\left(\frac{q_{n}(1,z)}{{\ell_{n+1}}(1,z)}+1+\frac{1}{\lambda}+\frac{zq_{n}(z,1)}{{\ell_{n+1}}(z,1)}\right)\frac{dz}{z}=\frac{2\pi\varepsilon_{2}}{(a+2)\sqrt{4b(a+2)-\varepsilon_{2}^{2}}}, |  |

so that exp ⁡ ( G 1) = 1 + π ( a + 2) ​ b ⁡ ( a + 2) ​ ε 2 + o ​ ( ε 2). \exp(G_{1})=1+\frac{\pi}{(a+2)\sqrt{b(a+2)}}\varepsilon_{2}+\mbox{\rm o}(\varepsilon_{2}). Accordingly, from ( 48) (\ref{lem2eq1bis}) we can assert that

 | F 1 \displaystyle F_{1} | = − ( n 0 + + n 1 + ​ ε 1 + n 2 + ​ ε 2) − ( 1 + π b ​ ( a + 2) 3 ​ ε 2) ​ ( n 0 − + n 1 − ​ ε 1 + n 2 − ​ ε 2) + o ​ ( ‖ ( ε 1, ε 2) ‖) \displaystyle=-(n_{0}^{+}+n_{1}^{+}\varepsilon_{1}+n_{2}^{+}\varepsilon_{2})-\left(1+\frac{\pi}{\sqrt{b(a+2)^{3}}}\varepsilon_{2}\right)\left(n_{0}^{-}+n_{1}^{-}\varepsilon_{1}+n_{2}^{-}\varepsilon_{2}\right)+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) |  |

 |  | = − n 0 − − n 0 + − ( n 1 − + n 1 +) ​ ε 1 − ( n 2 − + n 2 + + π b ​ ( a + 2) 3 ​ n 0 −) ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖) \displaystyle=-n_{0}^{-}-n_{0}^{+}-\left(n_{1}^{-}+n_{1}^{+}\right)\varepsilon_{1}-\left(n_{2}^{-}+n_{2}^{+}+\frac{\pi}{\sqrt{b(a+2)^{3}}}n_{0}^{-}\right)\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|) |  |

 |  | = − 2 ​ n 1 + ​ ε 1 − ( 2 ​ n 2 + − π b ​ ( a + 2) 3 ​ n 0 +) ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖). \displaystyle=-2n_{1}^{+}\varepsilon_{1}-\left(2n_{2}^{+}-\frac{\pi}{\sqrt{b(a+2)^{3}}}n_{0}^{+}\right)\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|). |  |

In order to compute this coefficients let us note that

 | n 0 + \displaystyle n_{0}^{+} | = 2 ​ ( 1 − b) ( a + 2) 2 ​ ∫ 0 + ∞ ( 1 + η 1 ​ u 2) − 2 ​ a + 3 a + 2 ​ d ​ u u 1 / λ = 1 − b ( a + 1) ​ ( a + 2) ​ η 1 − a + 1 a + 2 \displaystyle=\frac{2(1-b)}{(a+2)^{2}}\int_{0}^{+\infty}(1+{\eta_{1}}u^{2})^{-\frac{2a+3}{a+2}}\frac{du}{u^{1/\lambda}}=\frac{1-b}{(a+1)(a+2)}\eta_{1}^{-\frac{a+1}{a+2}} |  |

and |

 | n 1 + \displaystyle n_{1}^{+} | = 2 ( a + 2) 2 ​ ∫ 0 + ∞ ( ( 1 + η 1 ​ u 2) − 2 ​ a + 3 a + 2 − 1) ​ d ​ u u 1 + 1 / λ = π 2 ​ ( a + 2) 2 ​ Γ ⁡ ( a 2 ​ ( a + 2)) Γ ⁡ ( 2 ​ a + 3 a + 2) ​ η 1 − a 2 ​ ( a + 2). \displaystyle=\frac{2}{(a+2)^{2}}\int_{0}^{+\infty}\left((1+{\eta_{1}}u^{2})^{-\frac{2a+3}{a+2}}-1\right)\frac{du}{u^{1+1/\lambda}}=\frac{\sqrt{\pi}}{2(a+2)^{2}}\frac{\Gamma\left(\frac{a}{2(a+2)}\right)}{\Gamma\left(\frac{2a+3}{a+2}\right)}\eta_{1}^{-\frac{a}{2(a+2)}}. |  |

The computations of n 2 + n_{2}^{+} is a little more involved. In this case

 | ( a + 2) 3 ​ b ⁡ ( a + 2) 2 ​ ( 1 − b) ​ n 2 + = \displaystyle\frac{(a+2)^{3}\sqrt{b(a+2)}}{2(1-b)}\,n_{2}^{+}= | ∫ 0 + ∞ ( 1 + η 1 u 2) − 2 ​ a + 3 a + 2 arctan ( η 1 u) u − 1 / λ d u \displaystyle\int_{0}^{+\infty}(1+{\eta_{1}}u^{2})^{-\frac{2a+3}{a+2}}\arctan(\sqrt{{\eta_{1}}}u)u^{-1/\lambda}du |  |

 |  | − ( 2 a + 3) η 1 ∫ 0 + ∞ ( 1 + η 1 u 2) − 3 ​ a + 5 a + 2 u 1 − 1 / λ d u \displaystyle-(2a+3)\sqrt{{\eta_{1}}}\int_{0}^{+\infty}(1+{\eta_{1}}u^{2})^{-\frac{3a+5}{a+2}}u^{1-1/\lambda}du |  |

 | = \displaystyle= | π ​ ( a + 2) 2 4 ​ ( a + 1) ​ ( Γ ⁡ ( 3 ​ a + 4 2 ​ ( a + 2)) Γ ⁡ ( 2 ​ a + 3 a + 2) − π a + 2) ​ η 1 − a + 1 a + 2, \displaystyle\,\frac{\sqrt{\pi}(a+2)^{2}}{4(a+1)}\left(\frac{\Gamma\left(\frac{3a+4}{2(a+2)}\right)}{\Gamma\left(\frac{2a+3}{a+2}\right)}-\frac{\sqrt{\pi}}{a+2}\right)\eta_{1}^{-\frac{a+1}{a+2}}, |  |

where to obtain the expression of the first integral we perform integration by parts. From here some additional computations show that

 | 2 ​ n 2 + − π b ​ ( a + 2) 3 ​ n 0 + = π ​ ( b − 1) ​ η 1 − a + 1 a + 2 ( a + 1) ​ b ​ ( a + 2) 3 ​ Γ ⁡ ( 3 ​ a + 4 2 ​ ( a + 2)) Γ ⁡ ( 2 ​ a + 3 a + 2) 2n_{2}^{+}-\frac{\pi}{\sqrt{b(a+2)^{3}}}n_{0}^{+}=\frac{\sqrt{\pi}(b-1)\eta_{1}^{-\frac{a+1}{a+2}}}{(a+1)\sqrt{b(a+2)^{3}}}\frac{\Gamma\left(\frac{3a+4}{2(a+2)}\right)}{\Gamma\left(\frac{2a+3}{a+2}\right)} |  |

and, on account of this,

 | 2 ​ n 2 + − π b ​ ( a + 2) 3 ​ n 0 + 2 ​ n 1 + = a ⁡ ( b − 1) 2 ​ ( a + 1) ​ b. \frac{2n_{2}^{+}-\frac{\pi}{\sqrt{b(a+2)^{3}}}n_{0}^{+}}{2n_{1}^{+}}=\frac{a(b-1)}{2(a+1)b}. |  |

Since n 1 + < 0 n_{1}^{+}<0 for all a ∈ ( − 1, 0) a\in(-1,0) and b ∈ ( 0, 2), b\in(0,2), we have that F 1 ​ ( μ ¯) = ρ 4 ​ ( μ ¯) ​ ( ε 1 + a ⁡ ( b − 1) 2 ​ ( a + 1) ​ b ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) F_{1}(\bar{\mu})=\rho_{4}(\bar{\mu})\left(\varepsilon_{1}+\frac{a(b-1)}{2(a+1)b}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right) with ρ 4 ​ ( μ ¯ 0) > 0 \rho_{4}(\bar{\mu}_{0})>0. Accordingly, the combination of ( 45) (\ref{lem2eq0}) and the last assertion in ( 1) (1) of Theorem 2.1 yields

 | Δ 1 ​ ( μ) | ε 0 = 0 = κ 11 ​ ( μ ¯) ​ ( ε 1 + a ⁡ ( b − 1) 2 ​ ( a + 1) ​ b ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) + κ 12 ​ ( μ ¯) ​ Δ 0 ​ ( μ) | ε 0 = 0 \left.\Delta_{1}(\mu)\right|_{\varepsilon_{0}=0}=\kappa_{11}(\bar{\mu})\left(\varepsilon_{1}+\frac{a(b-1)}{2(a+1)b}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)+\kappa_{12}(\bar{\mu})\left.\Delta_{0}(\mu)\right|_{\varepsilon_{0}=0} |  |

with κ 11 ​ ( μ ¯ 0) > 0. \kappa_{11}(\bar{\mu}_{0})>0. Finally, once again thanks to ∂ ε 0 δ ⁡ ( μ 0) ≠ 0 \partial_{\varepsilon_{0}}\delta(\mu_{0})\neq 0, we can write

 | Δ 1 ​ ( μ) = κ 11 ​ ( μ ¯) ​ ( ε 1 + a ⁡ ( b − 1) 2 ​ ( a + 1) ​ b ​ ε 2 + o ​ ( ‖ ( ε 1, ε 2) ‖)) + κ 12 ​ ( μ ¯) ​ Δ 0 ​ ( μ) + κ 13 ​ ( μ) ​ δ ​ ( μ) \Delta_{1}(\mu)=\kappa_{11}(\bar{\mu})\left(\varepsilon_{1}+\frac{a(b-1)}{2(a+1)b}\varepsilon_{2}+\mbox{\rm o}(\|(\varepsilon_{1},\varepsilon_{2})\|)\right)+\kappa_{12}(\bar{\mu})\Delta_{0}(\mu)+\kappa_{13}(\mu)\delta(\mu) |  |

for some smooth function κ 13 \kappa_{13} in a neighbourhood of μ 0 \mu_{0}. This proves the last assertion in ( 1) (1) and completes the proof of the result.

## References

- [1] J.C. Artés, F. Dumortier and J. Llibre, “Qualitative theory of planar differential systems”, Universitext, Springer-Verlag, Berlin, 2006.
- [2] M. Caubergh, F. Dumortier and R. Roussarie, Alien limit cycles in rigid unfoldings of a Hamiltonian 2-saddle cycle, Commun. Pure Appl. Anal. 6 (2007) 1–21.
- [3] B. Coll, C. Li, R. Prohens, Quadratic perturbations of a class of quadratic reversible systems with two centers, Discrete and Continuous Dynamical Systems 24 (2009) 699–729.
- [4] B. Coll, F. Dumortier, and R. Prohens, Alien limit cycles in Liénard equations, J. Differerential Equations 254 (2013) 1582–1600.
- [5] F. Dumortier, A. Guzmán and C. Rousseau, Finite cyclicity of elementary graphics surrounding a focus or center in quadratic systems, Qual. Theory Dyn. Syst. 3 (2002) 123–154.
- [6] F. Dumortier and R. Roussarie, Abelian integrals and limit cycles, J. Differential Equations 224 (2006) 296–313.
- [7] F. Dumortier, R. Roussarie and C. Rousseau, Hilbert’s 16th problem for quadratic vector fields, J. Differential Equations 110 (1994) 86–133.
- [8] J.-P. Françoise and L. Gavrilov, Perturbation theory of the quadratic Lotka-Volterra double center, Commun. Contemp. Math. 24 (2022), no. 5, paper no. 2150064, 38 pp.
- [9] A. Gasull, V. Mañosa and F. Mañosas, Stability of certain planar unbounded polycycles, J. Math. Anal. Appl. 269 (2002) 332–351.
- [10] L. Gavrilov, Cyclicity of period annuli and principalization of Bautin ideals, Ergod. Th. & Dynam. Sys. 28 (2008) 1497–1507.
- [11] L. Gavrilov and I. Illiev, Perturbations of quadratic Hamiltonian two-saddle cycles, Ann. Inst. H. Poincaré C Anal. Non Linéaire 32 (2015) 307–324.
- [12] I.D. Iliev, Perturbations of quadratic centers, Bull. Sci. Math. 122 (1998) 107–161.
- [13] Y. Ilyashenko, Centennial history of Hilbert’s 16th problem, Bull. Amer. Math. Soc. 39 (2002) 301–354.
- [14] A. Kelley, The stable, center-stable, center, center-unstable, unstable manifolds, J. Differential Equations 3 (1967) 546–570.
- [15] J. Li, Hilbert’s 16th problem and bifurcations of planar polynomial vector fields, Internat. J. Bifur. Chaos Appl. Sci. Engrg. 13 (2003) 47–106.
- [16] S. Luca, F. Dumortier, M. Caubergh and R. Roussarie, Detecting alien limit cycles near a Hamiltonian 2-saddle cycle, Discrete Contin. Dyn. Syst. 4 (2009) 723–781.
- [17] C. Liu, The cyclicity of period annuli of a class of quadratic reversible systems with two centers, J. Differential Equations 252 (2012) 5260–5273.
- [18] A. Mourtada, Action de derivations irreductibles sur les algebres quasi-regulieres d’Hilbert, preprint (2009), [arXiv:0912.1560v1][3].
- [19] D. Marín and J. Villadelprat, *Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: local setting,*J. Differential Equations 269 (2020) 8425–8467.
- [20] D. Marín and J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: general setting, J. Differential Equations 275 (2021) 684–732.
- [21] D. Marín and J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: coefficient properties, J. Differential Equations 404 (2024) 43–107.
- [22] D. Marín and J. Villadelprat, The criticality of reversible quadratic centers at the outer boundary of its period annulus, J. Differential Equations 332 (2022), 123–201.
- [23] J.R. Munkres, “Topology: a first course”, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1975
- [24] L. Peng, Z. Feng and C. Liu, Quadratic perturbations of a quadratic reversible Lotka-Volterra system with two centers, Discrete and Continuous Dynamical Systems 34 (2014) 4807–4826.
- [25] R. Roussarie, “Bifurcations of planar vector fields and Hilbert’s sixteenth problem” [2013] reprint of the 1998 edition. Modern Birkhäuser Classics. Birkhäuser/Springer, Basel, 1998.
- [26] R. Roussarie and C. Rousseau, Finite cyclicity of nilpotent graphics of pp-type surrounding a center, Bull. Belg. Math. Soc. Simon Stevin 15 (2008) 889–920.
- [27] C. Rousseau, Normal forms, bifurcations and finiteness properties of vector fields, NATO Sci. Ser. II Math. Phys. Chem. 137, Kluwer Academic Publishers, Dordrecht (2004) 431–470.
- [28] W. Rudin, “Real and complex analysis” McGraw-Hill Book Co., New York-Toronto, Ont.-London 1966.
- [29] D. S. Shafer and A. Zegeling, Bifurcation of limit cycles from quadratic centers, J. Differential Equations 122 (1995) 48–70.
- [30] L. Sheng and M. Han, Bifurcation of limit cycles from a compound loop with five saddles, J. Appl. Anal. Comput. 9 (2019) 2482–2495.
- [31] L. Sheng, M. Han and Y. Tian, On the number of limit cycles bifurcating from a compound polycycle, Int. J. Bifur. Chaos Appl. Sci. Eng. 30 (2020) no. 7, paper no. 2050099, 16 pp.
- [32] G. Swirszcz, Cyclicity of Infinite Contour around Certain Reversible Quadratic Center, J. Differential Equations 154 (1999) 239–266.
- [33] J. Yang, Y. Xiong and M. Han, Limit cycle bifurcations near a 2-polycycle or double 2-polycycle of planar systems, Nonlinear Anal. 95 (2014) 756–773.
- [34] V. A. Zorich, “Mathematical analysis II” Translated from the 2002 fourth Russian edition by Roger Cooke. Universitext. Springer-Verlag, Berlin, 2004.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://arxiv.org/pdf/0912.1560v1
