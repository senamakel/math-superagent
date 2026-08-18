<!-- source: https://arxiv.org/html/1502.00689 | converted from HTML -->

Finite cyclicity of some graphics through a nilpotent point of saddle type inside quadratic systems

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1502.00689v1 [math.CA] 03 Feb 2015

# Finite cyclicity of some graphics through a nilpotent point of saddle type inside quadratic systems This research was supported by NSERC of Canada

Christiane Rousseau Affiliation: Department of Mathematics and Statistics and CRM,University of Montreal, Montreal, Canada H3C 3J7 Chunhua Shan Affiliation: Department of Mathematical and Statistical Sciences,University of Alberta, Edmonton, Canada T6G 2G1 Huaiping Zhu Affiliation: Department of Mathematics and Statistics and LAMPS,York University, Toronto, Canada, M3J 1P3

Abstract. In this paper we show the finite cyclicity of the two graphics ( I 12 1) (I_{12}^{1}) and ( I 13 1) (I_{13}^{1}) through a triple nilpotent point of saddle type inside quadratic vector fields. These results contribute to the program launched in 1994 by Dumortier, Roussarie and Rousseau (DRR program) to show the existence of a uniform upper bound for the number of limit cycles for planar quadratic vector fields.

Key words. Nilpotent saddle; Graphics; Cyclicity; DDR program; Poincaré first return map; Finiteness part of Hilbert’s 16th problem.

## 1 Introduction

Hilbert’s 16th problem, second part, asks for the maximum number of limit cycles, called H ⁡ ( n) H(n), as well as the relative positions of limit cycles of a polynomial vector field P ⁡ ( x, y) ​ ∂ ∂ x + Q ⁡ ( x, y) ​ ∂ ∂ y P(x,y)\frac{\partial}{\partial x}+Q(x,y)\frac{\partial}{\partial y} as a function of n = max ⁡ ( deg ⁡ ( P), deg ⁡ ( Q)) n=\max(\mathrm{deg}(P),\mathrm{deg}(Q)). It is still unknown whether H ⁡ ( n) H(n) is finite. The DRR program started in 1994 by Dumortier, Roussarie and Rousseau ( [1]) produces a procedure to prove that H ⁡ ( 2) < ∞ H(2)<\infty. The underlying idea is a compactness argument. Indeed, polynomial vector fields can be extended to the Poincaré sphere 𝕊 2 {\mathbb{S}}^{2} by adding points at infinity in all directions. The number of limit cycles of a vector field depends only on its equivalence class under affine transformations and time rescalings. Also, limit cycles in quadratic vector fields necessarily surround a unique singular point with nondegenerate linear part, and linear vector fields can have no limit cycles. Hence, it is possible to compactify the space of equivalence classes of quadratic vector fields with a nondegenerate singular point of anti-saddle type: this yields a compact parameter space K K. Limit cycles in the compact set 𝕊 2 × K {\mathbb{S}}^{2}\times K accumulate on *graphics*, which are unions of trajectories and singular points for a given value of the parameters. The DRR program reduces the proof that H ⁡ ( 2) < ∞ H(2)<\infty to the proof that each graphic Γ ⊂ 𝕊 2 \Gamma\subset{\mathbb{S}}^{2} surrounding a nondegenerate singular point of anti-saddle type and occurring for a parameter value A 0 ∈ K A_{0}\in K has finite cyclicity in 𝕊 2 × K {\mathbb{S}}^{2}\times K, i.e. can produce only a finite number of limit cycles in a neighborhood U U of Γ \Gamma for parameter values A A in a neighborhood V V of A 0 A_{0}. Achieving the DRR program requires proving the finite cyclicity of 121 graphics in 𝕊 2 × K {\mathbb{S}}^{2}\times K. This program has stimulated the development of highly sophisticated methods to treat problems of increasing complexity. The graphics can be grouped in large classes and the strategy is to treat one class at a time. In this paper, we prove that the two graphics through a nilpotent point of saddle type, ( I 12 1) (I_{12}^{1}) and ( I 13 1) (I_{13}^{1}), that do not surround a center, have finite cyclicity. Therefore the results from this paper will bring the number of graphics of the program for which finite cyclicity is proved to 88.

In practice, in this paper we address the following questions:

- (1)

We first show that a generic graphic through a nilpotent saddle of multiplicity 3 has finite multiplicity in the case where one connection is fixed. The case of codimension 3 was already treated in [7] and it suffices to treat the case a = − 1 2 a=-\frac{1}{2} corresponding to b = 0 b=0 in the DRS normal form ( [3]).

- (2)

In quadratic systems, we show that the genericity condition is met for ( I 12 1) (I_{12}^{1}). This amounts to show that the integral of the divergence along the invariant parabola is nonzero. Note that the same computation shows the finite cyclicity of ( I 9 ​ b 2) (I_{9b}^{2}) when the codimension of the point is 3 3 (corresponding to ϵ 2 ≠ 0 {\epsilon}_{2}\neq 0 in [3]).

- (3)

We show that a generic graphic through a nilpotent saddle of multiplicity 3 and a saddle-node with central transition has finite multiplicity in the case where one connection is fixed. As an application, this yields the finite cyclicity of the graphic ( I 13 1) (I_{13}^{1}) inside quadratic systems.

(a) ( I 12 1) (I_{12}^{1})

(b) ( I 13 1) (I_{13}^{1})

Figure 1: Graphics for which we prove finite cyclicity

## 2 Preliminaries

### 2.1 Normal form for the unfolding of a nilpotent triple point of saddle type

We consider graphics through one singular point, which is a triple nilpotent point of saddle type. A germ of vector field in the neighborhood of such a point has the form

 | x ˙ = y y ˙ = x 3 + b ​ x ​ y + η ​ x 2 ​ y + y ​ O ​ ( x 3) + O ⁡ ( y 2). \displaystyle\begin{split}\dot{x}&=y\\ \dot{y}&=x^{3}+bxy+\eta x^{2}y+yO(x^{3})+O(y^{2}).\end{split} |  | (2.1) |

The unfolding of such points has been studied by Dumortier, Roussarie and Sotomayor, [3], including a normal form for the unfolding of the family. A different normal form has been used in [7] for studying the finite cyclicity of generic graphics through such singular points, which is particularly suitable for applications in quadratic vector fields, where there is always an invariant line through a nilpotent point of multiplicity 3 3.

Indeed, a germ of C ∞ C^{\infty} vector field in the neighborhood of a nilpotent point of multiplicity 3 3 of saddle type can be brought by an analytic change of coordinates to the form

 | x ˙ = y + a ​ x 2, y ˙ = y ⁡ ( x + η ​ x 2 + o ⁡ ( x 2) + O ⁡ ( y)), \displaystyle\begin{split}\dot{x}&=y+ax^{2},\\ \dot{y}&=y(x+\eta x^{2}+o(x^{2})+O(y)),\end{split} |  | (2.2) |

with a < 0 a<0 (see Figure 2).

Figure 2: A nilpotent saddle

A generic unfolding depending on a multi-parameter λ = ( μ 1, μ 2, μ 3, μ) \lambda=(\mu_{1},\mu_{2},\mu_{3},\mu) in a neighborhood of the origin has the form

 | x ˙ = y + a ⁡ ( λ) ​ x 2 + μ 2, y ˙ = μ 1 + μ 3 ​ y + x 4 ​ h 1 ​ ( x, λ) + y ⁡ ( x + η ​ x 2 + x 3 ​ h 2 ​ ( x, λ)) + y 2 ​ Q ​ ( x, y, λ), \displaystyle\begin{split}\dot{x}&=y+a(\lambda)x^{2}+\mu_{2},\\ \dot{y}&=\mu_{1}+\mu_{3}y+x^{4}h_{1}(x,\lambda)+y(x+\eta x^{2}+x^{3}h_{2}(x,\lambda))+y^{2}Q(x,y,\lambda),\end{split} |  | (2.3) |

where h 1 ​ ( x, λ) = O ⁡ ( | λ |) h_{1}(x,\lambda)=O(|\lambda|). Moreover, h 1, h 2, Q h_{1},h_{2},Q are C ∞ C^{\infty} functions, and Q Q can be chosen of arbitrarily high order in λ \lambda.

### 2.2 Finite cyclicity of a graphic

###### Definition 2.1.

A *graphic*Γ \Gamma of a vector field X 0 X_{0}, i.e. a union of trajectories and singular points, has *finite cyclicity*inside a family X λ X_{\lambda} if there exists N ∈ ℕ N\in\mathbb{N}, ϵ > 0 {\epsilon}>0 and δ > 0 \delta>0 such that any vector field X λ X_{\lambda} with | λ | < δ |\lambda|<\delta has at most N N periodic solutions at a Hausdorff distance less than ϵ {\epsilon} from Γ \Gamma. The minimum value N N is the *cyclicity*of the graphic.

When studying the finite cyclicity of a graphic Γ \Gamma, we need to find a uniform bound for the number of periodic solutions that can appear from it, for *all*values of the multi-parameter in a small neighborhood W W of the origin. Typically, we need to find a uniform bound for the number of fixed points of the Poincaré return map or, equivalently, for the number of zeros of some displacement map between two transversal sections to the graphic. With graphics containing a nilpotent singular point there is no way to make a uniform treatment for all λ ∈ W \lambda\in W, and we cover W W by an infinite number of sectors with conic structure, one around each direction in parameter space. On each sector, we give a uniform bound for the finite cyclicity. Since the set of directions in parameter space is compact, we extract a finite subcovering: the maximum of the cyclicities on each sector of the covering is the cyclicity of the graphic Γ \Gamma. The method for doing this is the *blow-up of the family*, which was first introduced by Roussarie.

### 2.3 Blow-up of the family

Let us make the change of parameters

 | ( μ 1, μ 2, μ 3) = ( ν 3 ​ μ ¯ 1, ν 2 ​ μ ¯ 2, ν ​ μ ¯ 3). (\mu_{1},\mu_{2},\mu_{3})=(\nu^{3}\overline{\mu}_{1},\nu^{2}\overline{\mu}_{2},\nu\overline{\mu}_{3}). |  | (2.4) |

We take a neighborhood of the origin in parameter-space of the form 𝕊 2 × [0, ν 0) × U {\mathbb{S}}^{2}\times[0,\nu_{0})\times U, where U U is a neighborhood of 0 0 in μ \mu -space, M ¯ = ( μ ¯ 1, μ ¯ 2, μ ¯ 3) ∈ 𝕊 2 \overline{M}=(\overline{\mu}_{1},\overline{\mu}_{2},\overline{\mu}_{3})\in{\mathbb{S}}^{2} and ν ∈ [0, ν 0) \nu\in[0,\nu_{0}).

Note that 𝕊 2 {\mathbb{S}}^{2} is compact. Hence, to give an argument of finite cyclicity for the graphic Γ \Gamma, it suffices to find a neighborhood of each M ¯ = ( μ ¯ 1, μ ¯ 2, μ ¯ 3) ∈ 𝕊 2 \overline{M}=(\overline{\mu}_{1},\overline{\mu}_{2},\overline{\mu}_{3})\in{\mathbb{S}}^{2} inside 𝕊 2 {\mathbb{S}}^{2}, a corresponding ν 0 > 0 \nu_{0}>0 and a corresponding U U on which we can give a bound for the number of limit cycles. In our study, we will consider special values a 0 a_{0} of a a. It is important to note that a ⁡ ( λ) a(\lambda) depends on λ \lambda, and hence that a − a 0 a-a_{0} is a parameter in itself.

The way to handle this program is to do a *blow-up of the family*, a technique developed by Roussarie. For this, we introduce the weighted blow-up of the singular point ( 0, 0, 0) (0,0,0) of the three-dimensional family of vector fields obtained by adding the equation ν ˙ = 0 \dot{\nu}=0 to the 2-dimensional system ( 2.3). The blow-up transformation is given by

 | ( x, y, ν) = ( r ​ x ¯, r 2 ​ y ¯, r ​ ρ), (x,y,\nu)=(r\overline{x},r^{2}\overline{y},r\rho), |  | (2.5) |

with r > 0 r>0 and ( x ¯, y ¯, ρ) ∈ 𝕊 2 (\overline{x},\overline{y},\rho)\in{\mathbb{S}}^{2}. After dividing by r r the transformed vector field, we get a family of C ∞ C^{\infty} vector fields X ¯ A \overline{X}_{A}, depending on the parameters A = ( a − a 0, M ¯, μ) A=(a-a_{0},\overline{M},\mu). The foliation { ν = r ρ = C o n s t } \{\nu=r\rho=Const\} is invariant under the flow. The leaves { r ρ = ν } \{r\rho=\nu\} with ν > 0 \nu>0 are regular two-dimensional manifolds, while the critical locus { r ρ = 0 } \{r\rho=0\} is stratified and contains the two strata (see Figure 3):

- •

𝕊 1 × ℝ + {\mathbb{S}}^{1}\times{\mathbb{R}}^{+} is the blow-up of X 0 X_{0} (for λ = 0 \lambda=0);

- •

D μ ¯ = { x ¯ 2 + y ¯ 2 + ρ 2 = 1 ∣ ρ ≥ 0 } D_{\overline{\mu}}=\{\overline{x}^{2}+\overline{y}^{2}+\rho^{2}=1\mid\rho\geq 0\}.

### 2.4 Limit periodic sets in the blow-up family

The strategy for studying the finite cyclicity of Γ \Gamma is the following. We study the singular points of X ¯ \overline{X} on r = ρ = 0 r=\rho=0. For a ≠ 1 2 a\neq\frac{1}{2}, there will be four distinct singular points (occuring in two pairs) corresponding to y ¯ = 0 \overline{y}=0 (for P 1 P_{1} and P 2 P_{2}) and y ¯ = 1 − 2 ​ a 2 \overline{y}=\frac{1-2a}{2} (for P 3 P_{3} and P 4 P_{4}): see Figure 3. Their eigenvalues appear in Table 1.

Figure 3: The stratified set { r ρ = 0 } \{r\rho=0\} in the blow-up.

 | r r | ρ \rho | y y |

P 1 P_{1} | − a -a | a \ \ a | − ( 1 − 2 ​ a) -(1-2a) |

P 2 P_{2} | a \ \ a | − a -a | ( 1 − 2 ​ a) \ \ (1-2a) |

P 3 P_{3} | 1 / 2 \ \ 1/2 | − 1 / 2 -1/2 | − ( 1 − 2 ​ a) -(1-2a) |

P 4 P_{4} | − 1 / 2 -1/2 | 1 / 2 \ \ 1/2 | ( 1 − 2 ​ a) \ \ (1-2a) |

Table 1: The eigenvalues at P i P_{i} ( i = 1, 2, 3, 4 i=1,2,3,4)

In this paper we study the finite cyclicity of a graphic Γ \Gamma joining P 3 P_{3} and P 4 P_{4}. We consider a particular value A 0 = ( a 0, M ¯ 0) A_{0}=(a_{0},\overline{M}_{0}). Here is the strategy for finding an upper bound for the number of limit cycles that appear for A A in a neighborhood of A 0 A_{0}. We determine the phase portrait of the family rescaling ( 2.6) on D μ ¯ D_{\overline{\mu}}: this allows determining *limit periodic sets*Γ ¯ \overline{\Gamma}, which are formed by the union of Γ \Gamma with a finite number of trajectories and singular points on D μ ¯ D_{\overline{\mu}} joining P 4 P_{4} and P 3 P_{3}, so that their orientation will be compatible with that of Γ \Gamma. The limit periodic sets to be studied appear in Table 2. They are continuous families of limit periodic sets. We use the convention to label the different types: Sxhhia, Sxhhib, etc, starting from the top. For instance, Sxhh1a corresponds to the boundary upper limit periodic set, Sxhh1b corresponds to any of the intermediate limit periodic set, and Sxhh1c corresponds to the lower periodic set through the saddle point. They come from studying the phase portrait of the *family rescaling*

 | x ¯ ˙ = y ¯ + a ​ x ¯ 2 + μ ¯ 2, y ¯ ˙ = μ ¯ 1 + μ ¯ 3 ​ y ¯ + x ¯ ​ y ¯, \displaystyle\begin{split}\dot{\overline{x}}&=\overline{y}+a\overline{x}^{2}+\overline{\mu}_{2},\\ \dot{\overline{y}}&=\overline{\mu}_{1}+\overline{\mu}_{3}\overline{y}+\overline{x}\overline{y},\end{split} |  | (2.6) |

obtained by putting ρ = 1 \rho=1 and r = 0 r=0. It then suffices to show that each limit periodic set has finite cyclicity, i.e. to show the existence of an upper bound for the number of periodic solutions of X ¯ A \overline{X}_{A} for A A in a small neighborhood of A 0 A_{0}.

 |  |  |

Sxhh1 | Sxhh2 | Sxhh3 |

 |  |  |

Sxhh4 | Sxhh5 | Sxhh6 |

 |  |  |

Sxhh7 |  | Sxhh8 |

 |  |  |

Sxhh9 |  | Sxhh10 |

Table 2: Convex limit periodic sets of hh-type for a graphic with a nilpotent saddle

### 2.5 Proving the finite cyclicity of a limit periodic set

The following argument will be used for proving the finite cyclicity of a limit periodic set: limit cycles correspond to fixed points of a Poincaré return map defined on a section or, equivalently, to zeroes of a displacement map between two sections. The sections are 2-dimensional but, because of the invariant foliation, the problem can be reduced to a 1-dimensional problem and the conclusion follows by a derivation-division argument.

To compute the displacement map, we decompose the related transition maps between sections into compositions of Dulac maps in the neighborhood of the singular points and regular C k C^{k} transitions elsewhere.

### 2.6 Dulac maps

The Dulac maps have been computed in [7]. There are two types of Dulac transitions. The first type of transition map goes from a section { r = r 0 } \{r=r_{0}\} to a section { ρ = ρ 0 } \{\rho=\rho_{0}\}, or the other way around. This type of transition typically behaves as an affine map which is a very strong contraction or dilatation. The study of the number of zeroes of a displacement map involving only Dulac maps of the first type is reduced to the study of the number of zeroes of a 1-dimensional map.

The second type of Dulac map is concerned with a transition from a section { y ¯ = y ¯ 0 } \{\overline{y}=\overline{y}_{0}\} to, either a section { r = r 0 } \{r=r_{0}\}, or a section { ρ = ρ 0 } \{\rho=\rho_{0}\}. Here we only need the first type of Dulac map. We recall the precise results here.

#### 2.6.1 First type of Dulac map

We consider a Dulac map D i D_{i} from a section Π i = { ρ = ρ 0 } \Pi_{i}=\{\rho=\rho_{0}\} to a section Σ i = { r = r 0 } \Sigma_{i}=\{r=r_{0}\} in the neighborhood of a singular point P i P_{i} (potentially following the flow backwards). We decide to choose ( ν, y ~ i) (\nu,\tilde{y}_{i}) as coordinates on the sections Π i \Pi_{i} and Σ i \Sigma_{i}, where y ~ i \tilde{y}_{i} is a normalizing coordinate for the blow-up system in the neighborhood of P i P_{i}. The normal form near P i P_{i} is given by

 | r ˙ = r, ρ ˙ = − ρ, y ~ ˙ i = G ⁡ ( r, ρ, y ~ i), \displaystyle\begin{split}\dot{r}&=r,\\ \dot{\rho}&=-\rho,\\ \dot{\tilde{y}}_{i}&=G(r,\rho,\tilde{y}_{i}),\end{split} |  | (2.7) |

where

 | G ⁡ ( r, ρ, y ~ i) = { y ~ i ​ ( − σ + φ i ​ ( ν)), σ 0 ∉ ℚ, y ~ i ​ ( − σ + φ i ​ ( ν) + f i ​ ( r p ​ y ~ i)) + η i ​ ( ν) ​ ρ p, σ 0 = p ∈ ℕ, y ~ i ​ ( − σ + φ i ​ ( ν) + f i ​ ( r p ​ y ~ i q)), σ 0 = p q, q > 1 G(r,\rho,\tilde{y}_{i})=\begin{cases}\tilde{y}_{i}(-\sigma+\varphi_{i}(\nu)),&\sigma_{0}\notin{\mathbb{Q}},\\ \tilde{y}_{i}(-\sigma+\varphi_{i}(\nu)+f_{i}(r^{p}\tilde{y}_{i}))+\eta_{i}(\nu)\rho^{p},&\sigma_{0}=p\in{\mathbb{N}},\\ \tilde{y}_{i}(-\sigma+\varphi_{i}(\nu)+f_{i}(r^{p}\tilde{y}_{i}^{q})),&\sigma_{0}=\frac{p}{q},\>q>1\end{cases} |  | (2.8) |

where

 | σ = { 2 ​ ( 1 − 2 ​ a) = 2 ​ ( 1 − 2 ​ a 0) + α, i = 3, 4, 2 ​ a − 1 a = 2 ​ a 0 − 1 a 0 + α, i = 1, 2. \sigma=\begin{cases}2(1-2a)=2(1-2a_{0})+\alpha,&i=3,4,\\ \frac{2a-1}{a}=\frac{2a_{0}-1}{a_{0}}+\alpha,&i=1,2.\end{cases} |  |

###### Definition 2.2.

The compensator ω \omega is a univeral unfolding of the function − log ⁡ x -\log x, namely

 | ω ⁡ ( x, α) = { x − α − 1 α, α ≠ 0, − log ⁡ x, α = 0. \omega(x,\alpha)=\begin{cases}\frac{x^{-\alpha}-1}{\alpha},&\alpha\neq 0,\\ -\log x,&\alpha=0.\end{cases} |  | (2.9) |

The form of the Dulac map was first studied in [7]. The following form is a refinement from [6].

###### Theorem 2.3.

We consider the Dulac map from the section { ρ = ρ 0 } \{\rho=\rho_{0}\} to the section { r = r 0 } \{r=r_{0}\}, both parametrized by ( y ~ i, ν). (\tilde{y}_{i},\nu). Let ν 0 = r 0 ​ ρ 0 \nu_{0}=r_{0}\rho_{0} and

 | σ ¯ i = σ − φ i ​ ( ν) = σ 0 + α i. \bar{\sigma}_{i}=\sigma-\varphi_{i}(\nu)=\sigma_{0}+\alpha_{i}. |  | (2.10) |

The y ~ i \tilde{y}_{i} -component of the transition map D i D_{i} has the following expression:

1. 1.

If σ 0 ∉ ℚ: \sigma_{0}\not\in{\mathbb{Q}}:

 | D i ​ ( y ~ i, ν) = ( ν ν 0) σ ¯ ​ y ~ i. D_{i}(\tilde{y}_{i},\nu)=\Big(\frac{\nu}{\nu_{0}}\Big)^{\bar{\sigma}}\tilde{y}_{i}. |  | (2.11) |

2. 2.

If σ 0 = p q ∈ ℚ \sigma_{0}=\frac{p}{q}\in{\mathbb{Q}} with ( p, q) = 1 (p,q)=1:

 | D i ( y ~ i, ν) = η i ( ν) ρ 0 p ( ν ν 0) σ ¯ ω ( ν ν 0, α i) + ( ν ν 0) σ ¯ ( y ~ i + ϕ i ( y ~ i, ν,)), D_{i}(\tilde{y}_{i},\nu)=\eta_{i}(\nu)\rho_{0}^{p}\Big(\frac{\nu}{\nu_{0}}\Big)^{\bar{\sigma}}\omega\Big(\frac{\nu}{\nu_{0}},\alpha_{i}\Big)+\Big(\frac{\nu}{\nu_{0}}\Big)^{\bar{\sigma}}\Big(\tilde{y}_{i}+\phi_{i}(\tilde{y}_{i},\nu,)\Big), |  | (2.12) |

where

  - •

ϕ i = O ⁡ ( ν p + q ​ α i ​ ω q + 1 ​ ( ν ν 0, α i) ​ | ln ⁡ ν |) \phi_{i}=O\left(\nu^{p+q\alpha_{i}}\omega^{q+1}\left(\frac{\nu}{\nu_{0}},\alpha_{i}\right)|\ln\nu|\right) and for any integer l ≥ 2, l\geq 2, ϕ μ, σ \phi_{\mu,\sigma} is of class 𝒞 l − 2 {\mathcal{C}}^{l-2} in ( y ~ i, ν 1 / l, ν 1 / l ​ ω ​ ( ν ν 0, α i), ν, μ, σ) \left(\tilde{y}_{i},\nu^{1/l},\nu^{1/l}\omega\left(\frac{\nu}{\nu_{0}},\alpha_{i}\right),\nu,\mu,\sigma\right);

  - •

η i \eta_{i} is as in ( 2.8). In particular, η i ≡ 0 \eta_{i}\equiv 0 when σ 0 ∉ ℕ. \sigma_{0}\not\in{\mathbb{N}}.

###### Remark 2.4.

It follows from the form of ϕ \phi as a function of class 𝒞 l − 2 {\mathcal{C}}^{l-2} on the generalized monomials y ~ i \tilde{y}_{i}, ν 1 / l \nu^{1/l} and ν 1 / l ​ ω ​ ( ν ν 0, α i) \nu^{1/l}\omega\left(\frac{\nu}{\nu_{0}},\alpha_{i}\right) that all its derivatives with respect to y ~ i \tilde{y}_{i} of small order are O ⁡ ( ν β) O(\nu^{\beta}) for some β > 0 \beta>0. We say that ϕ \phi has property J J.

### 2.7 Dulac map near a hyperbolic or semi-hyperbolic point

When considering limit periodic sets, we will have additional singular points on them, and their associated Dulac maps. These can be explicitly calculated when the system is in C k C^{k} normal form. We recall very briefly the form of these Dulac maps.

###### Theorem 2.5.

We consider a polynomial normal form for a family depending on a multi-parameter A A, in the neighborhood of a hyperbolic saddle point with eigenvalues λ 1 ​ ( A) > 0, − λ 2 ​ ( A) < 0 \lambda_{1}(A)>0,-\lambda_{2}(A)<0. The *hyperbolicity ratio*is defined as the quotient τ = λ 2 ​ ( A) λ 1 ​ ( A) \tau=\frac{\lambda_{2}(A)}{\lambda_{1}(A)}. If the system near the saddle has the following C k C^{k} normal form for A A close to A 0: A_{0}:

 | x ˙ = λ 1 ​ ( A) ​ x, y ˙ = − λ 2 ​ ( A) ​ y ​ ( 1 + Q ⁡ ( x, y)), \displaystyle\begin{split}\dot{x}&=\lambda_{1}(A)x,\\ \dot{y}&=-\lambda_{2}(A)y(1+Q(x,y)),\end{split} |  | (2.13) |

with

 | Q ⁡ ( x, y) = { 0, τ ⁡ ( A 0) ∉ ℚ +, ∑ i = 1 K c i ​ ( A) ​ ( x p ​ y q) i, τ ⁡ ( A 0) = p q, Q(x,y)=\begin{cases}0,&\tau(A_{0})\notin{\mathbb{Q}}^{+},\\ \sum_{i=1}^{K}c_{i}(A)(x^{p}y^{q})^{i},&\tau(A_{0})=\frac{p}{q},\end{cases} |  |

then the Dulac map from { y = Y 0 } \{y=Y_{0}\} to { x = X 0 } \{x=X_{0}\} is of the form

 | D A ​ ( x) = Y 0 ​ X 0 − τ ⁡ ( A) ​ x τ ⁡ ( A) ​ ( 1 + ϕ ⁡ ( x, A)), D_{A}(x)=Y_{0}X_{0}^{-\tau(A)}x^{\tau(A)}(1+\phi(x,A)), |  |

where ϕ \phi has the property I I of Mourtada given in Definition 2.6 below. Note that ϕ ≡ 0 \phi\equiv 0, when τ ⁡ ( A 0) ∉ ℚ \tau(A_{0})\notin{\mathbb{Q}}.

In the particular case τ ⁡ ( A 0) = 1 \tau(A_{0})=1, we need the more refined form

 | D A ​ ( x) = Y 0 ​ X 0 − τ ⁡ ( A) ​ ( x + α ​ x ​ ω ​ ( x, α) + ϕ ⁡ ( x, A)) D_{A}(x)=Y_{0}X_{0}^{-\tau(A)}(x+\alpha x\omega(x,\alpha)+\phi(x,A)) |  |

where ω \omega is the compensator defined in ( 2.9), τ = 1 − α \tau=1-\alpha, and ϕ \phi has the property I I of Mourtada, with ϕ ⁡ ( x, A) = O ⁡ ( x 1 + δ) \phi(x,A)=O(x^{1+\delta}) for some δ > 0 \delta>0.

###### Definition 2.6.

A function ϕ ⁡ ( y, A) \phi(y,A) has the property (I) of Mourtada if ϕ \phi is C K C^{K} for some K K on ( 0, y 0) × W (0,y_{0})\times W, where W W is a neighborhood of A 0 A_{0} in A A -space, and if there exists some neighborhood W ′ W^{\prime} of the origin in A A -space such that for all 0 ≤ j ≤ K 0\leq j\leq K,

 | lim y → 0 y i ​ ∂ j ϕ ∂ y j ​ ( y, λ) = 0, \lim_{y\to 0}y^{i}\frac{\partial^{j}\phi}{\partial y^{j}}(y,\lambda)=0, |  |

uniformly for λ ∈ W ′ \lambda\in W^{\prime}.

###### Theorem 2.7.

[2] We consider a polynomial normal form for a family depending on a multi-parameter A A in the neighborhood of a saddle-node with eigenvalues 0, − λ < 0 0,-\lambda<0, for A = A 0 A=A_{0}. If the system has the following normal form near the saddle-node

 | x ˙ = ( x 2 + η ⁡ ( A)) ​ ( 1 + C ⁡ ( A) ​ x 2) = F ⁡ ( x), y ˙ = − λ ​ y, \displaystyle\begin{split}\dot{x}&=(x^{2}+\eta(A))(1+C(A)x^{2})=F(x),\\ \dot{y}&=-\lambda y,\end{split} |  | (2.14) |

with η ⁡ ( A 0) = 0 \eta(A_{0})=0, then

1. 1.

Case of central transition: for η > 0 \eta>0, the Dulac map from { x = − X 0 } \{x=-X_{0}\} to { x = X 0 } \{x=X_{0}\} is linear of the form D A ​ ( y) = ϵ ​ ( A) ​ y D_{A}(y)={\epsilon}(A)y, with ϵ ⁡ ( A) > 0 {\epsilon}(A)>0 exponentially small in η \sqrt{\eta};

2. 2.

Case of stable-center transition: the Dulac map D A ​ ( x) D_{A}(x) from { y = Y 0 } \{y=Y_{0}\} to { x = X 0 } \{x=X_{0}\} is flat in x x, as well as all its partial derivatives in x x and in the parameters.

## 3 Finite cyclicity of convex graphics through a nilpotent saddle of multiplicity 3 3

It was shown in [7] that a graphic through a nilpotent saddle of codimension 3 3 has finite cyclicity as soon as the first return map along the graphic has a derivative different from 1 1. This excludes the value a 0 = − 1 2 a_{0}=-\frac{1}{2} in ( 2.3). This hypothesis was only used in studying the finite cyclicity of the limit periodic sets in S ​ x ​ h ​ h ​ 1 Sxhh1 and S ​ x ​ h ​ h ​ 5 Sxhh5. We now consider the case a 0 = − 1 2 a_{0}=-\frac{1}{2}. We show that all limit periodic sets in S ​ x ​ h ​ h ​ 1 Sxhh1 have finite cyclicity. Under the additional hypothesis that the line on the blow-up sphere is a fixed connection, we also show that all limit periodic sets in S ​ x ​ h ​ h ​ 1 Sxhh1 have finite cyclicity.

###### Theorem 3.1.

We consider a convex graphic through a nilpotent saddle of multiplicity 3 with a 0 = − 1 2 a_{0}=-\frac{1}{2} and such that the derivative of the first return map γ ∗ = P ′ ​ ( 0) ≠ 1 \gamma^{\ast}=P^{\prime}(0)\neq 1. Then all limit periodic sets in Sxhh1 have finite cyclicity.

###### Proof.

Without loss of generality we can suppose that the limit periodic set Γ \Gamma joins P 3 P_{3} and P 4 P_{4} (see Figure 3). Note that the finite cyclicity of the upper boundary graphic of S ​ x ​ h ​ h ​ 1 Sxhh1 was proved in [7]. Therefore, we only need to prove that the intermediate graphics S ​ x ​ h ​ h ​ 1 ​ b Sxhh1b and the lower boundary graphic of S ​ x ​ h ​ h ​ 1 ​ c Sxhh1c have finite cyclicity. The only place where the hypothesis a 0 ≠ − 1 2 a_{0}\neq-\frac{1}{2} was used in [7] is when the hyperbolicity ratio τ ⁡ ( M ¯ 0) \tau(\overline{M}_{0}) (i.e. the quotient of minus the negative eigenvalue to the positive one) is equal to 1 1 at the saddle point of ( 2.6). Since the divergence of ( 2.6) is identically equal to μ ¯ 3 \bar{\mu}_{3} for a 0 = − 1 2 a_{0}=-\frac{1}{2}, we need only consider the case A 0 = ( − 1 2, μ ¯ 1, μ ¯ 2, 0, 0) A_{0}=(-\frac{1}{2},\overline{\mu}_{1},\overline{\mu}_{2},0,0).

Figure 4: Transition map for the hh-graphics of saddle type

Let Γ ¯ \overline{\Gamma} be any intermediate or lower boundary graphic of S ​ x ​ h ​ h ​ 1 Sxhh1. To study its cyclicity, we take coordinates ( r, ρ, y ¯ i) (r,\rho,\overline{y}_{i}) in the neighborhood of P i P_{i}, i = 3, 4 i=3,4, where r = x r=x (resp. − x -x) for P 3 P_{3} (resp. P 4 P_{4}) and y ¯ i = y ¯ − 1 − 2 ​ a 2 \overline{y}_{i}=\overline{y}-\frac{1-2a}{2} (hence y ¯ i = 0 \overline{y}_{i}=0 at P i P_{i}). A C k C^{k} -change of coordinates to normal form in the neighborhood of P i P_{i} can be taken of the form y ~ i = y ¯ i + f i ​ ( r, ρ, y ¯ i) \tilde{y}_{i}=\overline{y}_{i}+f_{i}(r,\rho,\overline{y}_{i}). Let us take sections Σ i = { r = r 0 } \Sigma_{i}=\{r=r_{0}\} and Π i = { ρ = ρ 0 } \Pi_{i}=\{\rho=\rho_{0}\} as shown in Fig. 4 in the normal form coordinates ( r, ρ, y ~ i) (r,\rho,\tilde{y}_{i}) in the neighborhood of the singular point P i P_{i} ( i = 3, 4 i=3,4). We will study the displacement map L: Π 4 ⟶ Σ 3 L:\Pi_{4}\longrightarrow\Sigma_{3} defined by

 | L = R − 1 ∘ D 4 − D 3 ∘ T, L=R^{-1}\circ D_{4}-D_{3}\circ T, |  | (3.1) |

where R: Σ 3 ⟶ Σ 4 R:\Sigma_{3}\longrightarrow\Sigma_{4} and T: Π 4 ⟶ Π 3 T:\Pi_{4}\longrightarrow\Pi_{3} are the transition maps along the regular orbits in the normal form coordinates, and D i: Π i ⟶ Σ i D_{i}:\Pi_{i}\longrightarrow\Sigma_{i} are the Dulac maps. We will study the maximum number of small roots of L = 0 L=0.

We decide to choose ( ν, y ~ i) (\nu,\tilde{y}_{i}) as coordinates on the sections Π i \Pi_{i} and Σ i \Sigma_{i}. The maps R R and T T are two-dimensional but, since they preserve the ν \nu -coordinate, we will cheat a little and identify them with their second component which depends on ν \nu, and which we denote R ν R_{\nu} and T ν T_{\nu}. We denote by L ν L_{\nu} the corresponding second component of L L in ( 3.1). For ν ∈ [0, ν 0) \nu\in[0,\nu_{0}), R ν R_{\nu} and T ν T_{\nu} are regular C k C^{k} -diffeomorphisms. Let S ν = R ν − 1 S_{\nu}=R_{\nu}^{-1}. The Dulac maps D i D_{i} near P 4 P_{4} (following the flow backwards) and near P 3 P_{3} are calculated in Theorem 2.3, with σ 0 = 4 \sigma_{0}=4.

Let

 | α 34 = σ ¯ 3 − σ ¯ 4 = ν ​ O ​ ( 1). \alpha_{34}=\overline{\sigma}_{3}-\overline{\sigma}_{4}=\nu O(1). |  |

The map L ν L_{\nu} has the form

 | L ν ​ ( y ~) = m 0 ​ ( ν, λ) + ( ν ν 0) σ ¯ 3 ​ [T ν ′ ​ ( 0) − S ν ′ ​ ( 0) ​ ( ν ν 0) − α 34 + O ⁡ ( ν)] ​ y ~ 4 + ( ν ν 0) σ ¯ 3 ​ o ​ ( y ~ 4). L_{\nu}(\tilde{y})=m_{0}(\nu,\lambda)+\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}\left[T_{\nu}^{\prime}(0)-S_{\nu}^{\prime}(0)\left(\frac{\nu}{\nu_{0}}\right)^{-\alpha_{34}}+O(\nu)\right]\tilde{y}_{4}+\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}o(\tilde{y}_{4}). |  | (3.2) |

It is clear that an intermediate graphic has cyclicity 1 1 as soon as T ν ′ ​ ( 0) − S ν ′ ​ ( 0) ​ ν σ ¯ 4 − σ ¯ 3 T_{\nu}^{\prime}(0)-S_{\nu}^{\prime}(0)\nu^{\overline{\sigma}_{4}-\overline{\sigma}_{3}} is bounded away from 0 0 for A A in a neighborhood of A 0 = ( − 1 2, M ¯ 0, 0) A_{0}=(-\frac{1}{2},\overline{M}_{0},0). This is precisely the case when T ν ′ ​ ( 0) T_{\nu}^{\prime}(0) is close to 1 1. Indeed, we know that S ν ′ ​ ( 0) ≠ 1 S_{\nu}^{\prime}(0)\neq 1. Also,

 | ( ν ν 0) − α 34 = e − α 34 ​ log ⁡ ( ν / ν 0) = 1 + O ⁡ ( ν 1 − δ) \left(\frac{\nu}{\nu_{0}}\right)^{-\alpha_{34}}=e^{-\alpha_{34}\log(\nu/\nu_{0})}=1+O(\nu^{1-\delta}) |  |

for some small δ \delta, since α 34 = O ⁡ ( ν) \alpha_{34}=O(\nu). Hence, it suffices to show that T 0 ′ ​ ( 0) = 1 T_{0}^{\prime}(0)=1 when A 0 = ( − 1 2, μ ¯ 1, μ ¯ 2, 0, 0) A_{0}=(-\frac{1}{2},\overline{\mu}_{1},\overline{\mu}_{2},0,0). We show the stronger property that T 0 ≡ i ​ d T_{0}\equiv id for such an A 0 A_{0}. For this purpose, we use that the system ( 2.6) is Hamiltonian for a = − 1 2 a=-\frac{1}{2} and μ ¯ 3 = 0 \overline{\mu}_{3}=0: the trajectories are level curves H ⁡ ( x ¯, y ¯) = C H(\overline{x},\overline{y})=C of the Hamiltonian

 | H ⁡ ( x ¯, y ¯) = 1 2 ​ y ¯ 2 − 1 2 ​ x ¯ 2 ​ y ¯ + μ ¯ 2 ​ y ¯ − μ ¯ 1 ​ x ¯. H(\overline{x},\overline{y})=\frac{1}{2}\overline{y}^{2}-\frac{1}{2}\overline{x}^{2}\overline{y}+\overline{\mu}_{2}\overline{y}-\overline{\mu}_{1}\overline{x}. |  |

Hence, we must explain the link between the constant C C and the corresponding normalizing coordinates y ~ 3 \tilde{y}_{3} (resp. y ~ 4 \tilde{y}_{4}) on Π 3 \Pi_{3} (resp. Π 4 \Pi_{4}). For this, we must not forget that the family rescaling has been obtained by putting ρ = 1 \rho=1 after the blow-up. For r = 0 r=0, the system in ( ρ, y ¯) (\rho,\overline{y}) -coordinates is given by

 | ρ ˙ = ∓ ρ ⁡ ( y ¯ − 1 2 + μ ¯ 2 ​ ρ 2), y ¯ ˙ = ± 2 ​ y ¯ ∓ 2 ​ y ¯ 2 ∓ 2 ​ μ ¯ 2 ​ y ¯ ​ ρ 2 + μ ¯ 1 ​ ρ 3, \displaystyle\begin{split}\dot{\rho}&=\mp\rho(\overline{y}-\frac{1}{2}+\overline{\mu}_{2}\rho^{2}),\\ \dot{\overline{y}}&=\pm 2\overline{y}\mp 2\overline{y}^{2}\mp 2\overline{\mu}_{2}\overline{y}\rho^{2}+\overline{\mu}_{1}\rho^{3},\end{split} |  | (3.3) |

where the sign + + (resp. − -) comes from putting x ¯ = + 1 \overline{x}=+1 (resp x ¯ = − 1 \overline{x}=-1). The function ρ − 5 \rho^{-5} is an integrating factor of ( 3.3), which yields first integrals

 | H ¯ ± = y ¯ 2 2 ​ ρ 4 − y ¯ 2 ​ ρ 4 + μ ¯ 2 ​ y ¯ ρ 2 ∓ μ ¯ 1 ​ 1 ρ. \overline{H}_{\pm}=\frac{\overline{y}^{2}}{2\rho^{4}}-\frac{\overline{y}}{2\rho^{4}}+\overline{\mu}_{2}\frac{\overline{y}}{\rho^{2}}\mp\overline{\mu}_{1}\frac{1}{\rho}. |  |

We need to localize at P 3 P_{3} and P 4 P_{4} by letting z = y ¯ − 1 z=\overline{y}-1. Then

 | H ¯ ± = z 2 2 ​ ρ 4 + z 2 ​ ρ 4 + μ ¯ 2 ​ z + 1 ρ 2 ∓ μ ¯ 1 ​ 1 ρ, \overline{H}_{\pm}=\frac{z^{2}}{2\rho^{4}}+\frac{z}{2\rho^{4}}+\overline{\mu}_{2}\frac{z+1}{\rho^{2}}\mp\overline{\mu}_{1}\frac{1}{\rho}, |  |

which means that the trajectories are given by

 | Z = z 2 2 + z 2 + μ ¯ 2 ​ ( z + 1) ​ ρ 2 ∓ μ ¯ 1 ​ ρ 3 = C ± ​ ρ 4, Z=\frac{z^{2}}{2}+\frac{z}{2}+\overline{\mu}_{2}(z+1)\rho^{2}\mp\overline{\mu}_{1}\rho^{3}=C_{\pm}\rho^{4}, |  |

The change of coordinate z ↦ Z z\mapsto Z is invertible for small z z and is precisely the normalizing coordinate. Then it is easy to see that on sections Π 3 \Pi_{3} and Π 4 \Pi_{4} with common equation { ρ = ρ 0 } \{\rho=\rho_{0}\} we have y ~ 3 = C + ​ ρ 0 4 \tilde{y}_{3}=C_{+}\rho_{0}^{4} and y ~ 4 = C − ​ ρ 0 4 \tilde{y}_{4}=C_{-}\rho_{0}^{4}, and also that C + = C = C − C_{+}=C=C- for a given trajectory. Hence T 0 ≡ i ​ d T_{0}\equiv id, which means that T ′ T^{\prime} is close to 1 1 for A A close to A 0 A_{0} in the neighborhood of the limit periodic set.

We now only need to consider the lower graphic Sxhh1c for A 0 = ( − 1 2, μ ¯ 1, μ ¯ 2, 0, 0) A_{0}=(-\frac{1}{2},\overline{\mu}_{1},\overline{\mu}_{2},0,0). Let τ ⁡ ( M) = 1 − α \tau(M)=1-\alpha be the hyperbolicity ratio at the saddle point of ( 2.6).

Using Theorem 2.5, the regular transition near the hyberbolic saddle in suitable normal form coordinates has the form

 | V ν ​ ( y ~) = m 0 ​ ( A) + m 1 ​ ( A) ​ α ​ ω ​ ( y ~, α) ​ y ~ + m 2 ​ ( A) ​ y ~ + O ⁡ ( y ~ 2 ​ ω ​ ( y ~, α)), V_{\nu}(\tilde{y})=m_{0}(A)+m_{1}(A)\alpha\omega(\tilde{y},\alpha)\tilde{y}+m_{2}(A)\tilde{y}+O\left(\tilde{y}^{2}\,\omega(\tilde{y},\alpha)\right), |  |

with m 0 ​ ( A 0) = m 1 ​ ( A 0) = m 2 ​ ( A 0) − 1 = 0 m_{0}(A_{0})=m_{1}(A_{0})=m_{2}(A_{0})-1=0, which yields that the transition map T ν T_{\nu} has the form

 | T ν ​ ( y ~ 3) = n 0 ​ ( A) + n 1 ​ ( A) ​ α ​ y ~ 3 ​ ω ​ ( y ~ 3, α) ​ ( 1 + ϕ 1 ​ ( y ~ 3, α)) + n 2 ​ ( A) ​ y ~ 3 ​ ( 1 + ϕ 2 ​ ( y ~ 3, α)) + O ⁡ ( y ~ 2 ​ ω ​ ( y ~, α)), \displaystyle\begin{split}T_{\nu}(\tilde{y}_{3})&=n_{0}(A)+n_{1}(A)\alpha\tilde{y}_{3}\omega(\tilde{y}_{3},\alpha)(1+\phi_{1}(\tilde{y}_{3},\alpha))\\ &\qquad\quad+n_{2}(A)\tilde{y}_{3}(1+\phi_{2}(\tilde{y}_{3},\alpha))+O\left(\tilde{y}^{2}\,\omega(\tilde{y},\alpha)\right),\end{split} |  | (3.4) |

with n 0 ​ ( A 0) = n 1 ​ ( A 0) = n 2 ​ ( A 0) − 1 = 0 n_{0}(A_{0})=n_{1}(A_{0})=n_{2}(A_{0})-1=0, where the functions ϕ j \phi_{j} have the property (I) of Mourtada (see Definition 2.6).

This yields that L ν ​ ( y ~ 3) L_{\nu}(\tilde{y}_{3}) has the form

 | L ν ​ ( y ~ 3) = n ~ 0 ​ ( A, ν) + n 1 ​ ( A, ν) ​ ( ν ν 0) σ ¯ 3 ​ α ​ y ~ 3 ​ ω ​ ( y ~ 3, α) ​ ( 1 + ψ 1 ​ ( y ~ 3, ν)) + ( ν ν 0) σ ¯ 3 ​ [n 2 ​ ( A ν) − S ν ′ ​ ( 0) ​ ( ν ν 0) α 34 + O ⁡ ( ν)] ​ y ~ 3 ​ ( 1 + ψ 2 ​ ( y ~ 3, ν)), \displaystyle\begin{split}L_{\nu}(\tilde{y}_{3})&=\tilde{n}_{0}(A,\nu)+n_{1}(A,\nu)\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}\alpha\tilde{y}_{3}\omega(\tilde{y}_{3},\alpha)(1+\psi_{1}(\tilde{y}_{3},\nu))\\ &\qquad+\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}\left[n_{2}(A_{\nu})-S_{\nu}^{\prime}(0)\left(\frac{\nu}{\nu_{0}}\right)^{\alpha_{34}}+O(\nu)\right]\tilde{y}_{3}(1+\psi_{2}(\tilde{y}_{3},\nu)),\end{split} |  | (3.5) |

where n ~ 0 ​ ( A 0, 0) = α ⁡ ( A 0, 0) = 0 \tilde{n}_{0}(A_{0},0)=\alpha(A_{0},0)=0. Let n ~ 2 ​ ( A, ν) = n 2 ​ ( A ν) − S ν ′ ​ ( 0) ​ ( ν ν 0) α 34 + O ⁡ ( ν) \tilde{n}_{2}(A,\nu)=n_{2}(A_{\nu})-S_{\nu}^{\prime}(0)\left(\frac{\nu}{\nu_{0}}\right)^{\alpha_{34}}+O(\nu), then we have n ~ 2 ​ ( A 0, 0) ≠ 0 \tilde{n}_{2}(A_{0},0)\neq 0. ψ 1, ψ 2 \psi_{1},\psi_{2} are finite sums of products of functions with property (I) or (J).

By Rolle’s theorem, the number of zeroes of L ν L_{\nu} is at most 1 1 plus the number of zeroes of N 1, ν ​ ( y ~ 3) = ( ν ν 0) − σ ¯ 3 ​ d ​ L d ​ y ~ 3 ​ ( y ~ 3) N_{1,\nu}(\tilde{y}_{3})=\left(\frac{\nu}{\nu_{0}}\right)^{-\overline{\sigma}_{3}}\frac{dL}{d\tilde{y}_{3}}(\tilde{y}_{3}). Considering that the derivative of ω ⁡ ( y ~ 3, α) \omega(\tilde{y}_{3},\alpha) is 1 + α ​ ω ​ ( y ~ 3, α) 1+\alpha\omega(\tilde{y}_{3},\alpha), we have

 | N 1, ν ​ ( y ~ 3) = n 1 ​ ( A, ν) ​ [( 1 − α) ​ ω ​ ( y ~ 3, α) − 1] ​ ( 1 + ξ 1 ​ ( y ~ 3, ν)) + n ~ 2 ​ ( A, ν) ​ ( 1 + ξ 2 ​ ( y ~ 3, ν)), N_{1,\nu}(\tilde{y}_{3})=n_{1}(A,\nu)[(1-\alpha)\omega(\tilde{y}_{3},\alpha)-1](1+\xi_{1}(\tilde{y}_{3},\nu))+\tilde{n}_{2}(A,\nu)(1+\xi_{2}(\tilde{y}_{3},\nu)), |  |

where ξ 1, ξ 2 \xi_{1},\xi_{2} are finite sums of functions with property (I) and (J). The number of zeroes of N 1, ν ​ ( y ~ 3) N_{1,\nu}(\tilde{y}_{3}) is the same as the number of zeroes of

 | N 2, ν ​ ( y ~ 3) = N 1, ν ​ ( y ~ 3) [( 1 − α) ​ ω ​ ( y ~ 3, α) − 1] ​ ( 1 + ξ 1 ​ ( y ~ 3, ν)). N_{2,\nu}(\tilde{y}_{3})=\frac{N_{1,\nu}(\tilde{y}_{3})}{[(1-\alpha)\omega(\tilde{y}_{3},\alpha)-1](1+\xi_{1}(\tilde{y}_{3},\nu))}. |  |

By Rolle’s theorem again, this number is at most 1 1 plus the number of zeroes of N 3, ν ​ ( y ~ 3) = d ​ N 2, ν d ​ y ~ 3 ​ ( y ~ 3) N_{3,\nu}(\tilde{y}_{3})=\frac{dN_{2,\nu}}{d\tilde{y}_{3}}(\tilde{y}_{3}), given by

 | N 3, ν ​ ( y ~ 3) = − n ~ 2 ​ ( A, ν) ​ ( 1 − α) ​ y ~ 3 − 1 − α [( 1 − α) ​ ω ​ ( y ~ 3, α) − 1] 2 ​ ( 1 + χ 2 ​ ( y ~ 3, ν)) ≠ 0, N_{3,\nu}(\tilde{y}_{3})=-\tilde{n}_{2}(A,\nu)\frac{(1-\alpha)\tilde{y}_{3}^{-1-\alpha}}{[(1-\alpha)\omega(\tilde{y}_{3},\alpha)-1]^{2}}(1+\chi_{2}(\tilde{y}_{3},\nu))\neq 0, |  |

with χ 2 \chi_{2} a sum of functions with property (I) and (J), since it is standard that x n ​ ω ​ ( x, α) x^{n}\omega(x,\alpha) is small for positive n n and small ( x, α) (x,\alpha). ∎

###### Theorem 3.2.

We consider a convex graphic through a nilpotent saddle of multiplicity 3 with a 0 = − 1 2 a_{0}=-\frac{1}{2} passing through the points P 3 P_{3} and P 4 P_{4} of the blow-up, and such that the derivative of the first return map γ ∗ = P ′ ​ ( 0) ≠ 1 \gamma^{\ast}=P^{\prime}(0)\neq 1. We also suppose that there is a fixed connection on the blow-up sphere along a line joining P 1 P_{1} and P 2 P_{2} (corresponding to μ 1 = 0 \mu_{1}=0 in ( 2.3). Then all limit periodic sets in Sxhh5 have finite cyclicity.

###### Proof.

The proof is very similar to that of Theorem 3.1. When μ ¯ 3 ≠ 0 \overline{\mu}_{3}\neq 0, then the product of the hyperbolicity ratios τ 1 ​ τ 2 \tau_{1}\tau_{2} at the two saddle points is different from 1 1, and the finite cyclicity was proven in [7]. When μ ¯ 3 = 0 \overline{\mu}_{3}=0, then the family rescaling ( 2.6) is integrable, both because it is symmetric and Hamiltonian. Hence, for the intermediate limit periodic sets, the transition map T ν T_{\nu} is close to the identity. As for the lower periodic set through the two saddle points, the transition map T ν T_{\nu} has the same form as in ( 3.4) with τ = τ 1 ​ τ 2 = 1 − α \tau=\tau_{1}\tau_{2}=1-\alpha. ∎

###### Remark 3.3.

We conjecture that the hypothesis that μ 1 = 0 \mu_{1}=0 in Theorem 3.2 can be dropped, but we have not been able to prove it.

###### Corollary 3.4.

We consider a convex graphic through a nilpotent saddle of multiplicity 3 with a 0 = − 1 2 a_{0}=-\frac{1}{2} passing through the points P 3 P_{3} and P 4 P_{4} of the blow-up, and such that the derivative of the first return map γ ∗ = P ′ ​ ( 0) ≠ 1 \gamma^{\ast}=P^{\prime}(0)\neq 1. We also suppose that there is a fixed connection on the blow-up sphere along a line joining P 1 P_{1} and P 2 P_{2}. Then the graphic has finite cyclicity.

###### Proof.

All limit periodic sets except Sxhh1 and SXhh5 were proved in [7] to have finite cyclicity for any a 0 a_{0} negative. And we have proved the finite cyclicity of SXhh1 and Sxhh5 in Theorems 3.1 and 3.2. ∎

## 4 Applications to quadratic systems

### 4.1 Quadratic systems with a nilpotent singular point at infinity

###### Proposition 4.1.

A quadratic system with a triple singular point of saddle or elliptic type at infinity and a finite singular point of focus or center type can be brought to the form

 | { x ˙ = δ ​ x − y + B ​ x 2 y ˙ = x + γ ​ y + x ​ y. \left\{\begin{array}[]{ll}\dot{x}&=\delta x-y+Bx^{2}\\ \dot{y}&=x+\gamma y+xy.\end{array}\right. |  | (4.1) |

The value of “ a a ” in the corresponding normal form ( 2.3) is a = 1 − B a=1-B. Moreover

1. 1.

When B > 1 B>1, the singular point is a nilpotent saddle.

2. 2.

For B ≠ 0, 1 2 B\neq 0,\frac{1}{2}, the system has an invariant parabola

 | y = ( B − 1 2) ​ x 2 + ( 2 − 1 B) ​ δ ​ x − B + ( 1 − 2 ​ B) ​ δ 2 2 ​ B 2 y=(B-\frac{1}{2})x^{2}+(2-\frac{1}{B})\delta x-\frac{\ B+(1-2B)\delta^{2}\ }{2B^{2}} |  | (4.2) |

if

 | γ ​ B − ( 1 − 2 ​ B) ​ δ = 0. \gamma B-(1-2B)\delta=0. |  | (4.3) |

3. 3.

The nilpotent saddle point is of codimension 4 4 when B = 3 2 B=\frac{3}{2} (corresponding to a = − 1 2 a=-\frac{1}{2}).

4. 4.

The integrability condition is γ = δ = 0 \gamma=\delta=0.

###### Proof.

We can suppose that the nilpotent singular point at infinity is located on the y-axis, the other singular point at infinity on the x-axis and the focus or center at the origin. Then the system can be brought to the form

 | { x ˙ = δ 10 ​ x + δ 01 ​ y + δ 20 ​ x 2 + δ 11 ​ x ​ y y ˙ = γ 10 ​ x + γ 01 ​ y + γ 11 ​ x ​ y + γ 02 ​ y 2. \left\{\begin{array}[]{ll}\dot{x}&=\delta_{10}x+\delta_{01}y+\delta_{20}x^{2}+\delta_{11}xy\\ \dot{y}&=\gamma_{10}x+\gamma_{01}y+\gamma_{11}xy+\gamma_{02}y^{2}.\end{array}\right. |  | (4.4) |

For the finite singular point to be a focus or center, we should have δ 10 ​ γ 01 − δ 01 ​ γ 10 > 0 \delta_{10}\gamma_{01}-\delta_{01}\gamma_{10}>0.

Localizing the system ( 4.4) at the singular point at infinity on y-axis by v = x y, z = 1 y v=\frac{x}{y},\ \ z=\frac{1}{y}, we have

 | { v ˙ = ( δ 11 − γ 02) ​ v + δ 01 ​ z + ( δ 20 − γ 11) ​ v 2 + ( δ 10 − γ 01) ​ v ​ z − γ 10 ​ v 2 ​ z z ˙ = z ⁡ ( − γ 02 − γ 01 ​ z − γ 11 ​ v − γ 10 ​ v ​ z) \left\{\begin{array}[]{ll}\dot{v}&=(\delta_{11}-\gamma_{02})v+\delta_{01}z+(\delta_{20}-\gamma_{11})v^{2}+(\delta_{10}-\gamma_{01})vz-\gamma_{10}v^{2}z\\ \dot{z}&=z(-\gamma_{02}-\gamma_{01}z-\gamma_{11}v-\gamma_{10}vz)\end{array}\right. |  | (4.5) |

The singular point ( 0, 0) (0,0) of system ( 4.5) is nilpotent, if δ 11 = γ 02 = 0 \delta_{11}=\gamma_{02}=0. It is triple if γ 11 ​ ( δ 20 − γ 11) ≠ 0 \gamma_{11}(\delta_{20}-\gamma_{11})\neq 0. By a rescaling and still using the original coordinates ( x, y) (x,y), we obtain the system ( 4.1).

By a transformation tangent to ( v, z) ↦ ( − V, z) (v,z)\mapsto(-V,z) and a time rescaling, we can bring system ( 4.5) into the C ∞ C^{\infty} -equivalent form

 | { V ˙ = Z Z ˙ = ( B − 1) ​ V 3 − γ ​ ( B − 1) 2 ​ V 4 + O ⁡ ( V 5) + Z ⁡ [( 3 − 2 ​ B) ​ V − γ ⁡ ( B − 1) ​ ( B 2 − 2 ​ B + 4) ​ V 2 + O ⁡ ( V 3)] + Z 2 ​ O ​ ( | ( V, Z) | 3). \begin{cases}\dot{V}=Z\\ \dot{Z}=(B-1)V^{3}-\gamma(B-1)^{2}V^{4}+O(V^{5})\\ \qquad+Z\Big[(3-2B)V-\gamma(B-1)(B^{2}-2B+4)V^{2}+O(V^{3})\Big]+Z^{2}O(|(V,Z)|^{3}).\end{cases} |  | (4.6) |

Then η = − γ ​ ( B − 1) 2 ​ ( 5 ​ B 2 − 4 ​ B + 11) \eta=-\gamma(B-1)^{2}(5B^{2}-4B+11) in ( 2.1) does not vanish when γ ≠ 0 \gamma\neq 0 and B > 1 B>1. Also b = 3 − 2 ​ B b=3-2B vanishes for B = 3 2 B=\frac{3}{2}. ∎

### 4.2 Finite cyclicity of graphics with a nilpotent point of saddle-type inside quadratic systems

Figure 5: The graphic ( I 12 1) (I_{12}^{1}).

###### Theorem 4.2.

The graphic ( I 12 1) (I_{12}^{1}) (Figure 5) has finite cyclicity inside quadratic systems.

###### Proof.

The graphic ( I 12 1) (I_{12}^{1}) is an hh-type graphic with a nilpotent saddle of multiplicity 3 at infinity and an invariant parabola as shown in Fig 5.

By Theorem 3.4, to prove the finite cyclicity of ( I 12 1) (I_{12}^{1}), we only need to check that the first return map P P of the system ( 4.1) along the invariant parabola ( 4.2) under condition ( 4.3) satisfies γ ∗ = P ′ ​ ( 0) ≠ 1 \gamma^{\ast}=P^{\prime}(0)\neq 1 when γ ≠ 0 \gamma\neq 0. Along the invariant parabola ( 4.2), we have

 | P ′ ​ ( 0) = exp ⁡ ( ∫ − ∞ ∞ d ​ i ​ v ​ 𝑑 t) = lim x 0 → ∞ exp ⁡ ( ∫ − x 0 x 0 ( 1 + 2 ​ B) ​ x + ( 1 − B) ​ δ B 1 2 ​ x 2 + ( 1 − B) ​ δ B ​ x + ( 1 − 2 ​ B) ​ δ 2 + B 2 ​ B 2 ​ 𝑑 x) = lim x 0 → ∞ [( − B 2 ​ x 0 2 + 2 ​ δ ​ B ​ ( B − 1) ​ x 0 + δ 2 ​ ( 2 ​ B − 1) − B − B 2 ​ x 0 2 − 2 ​ δ ​ B ​ ( B − 1) ​ x 0 + δ 2 ​ ( 2 ​ B − 1) − B) 1 + 2 ​ B exp ( 4 δ B 1 / 2 ( 1 − B) ( 1 − B δ 2) − 1 / 2 arctan − B ​ x + ( B − 1) ​ δ B ⁡ ( 1 − B ​ δ 2)) | x 0 − x 0] = exp ( 4 π δ B 1 / 2 ( 1 − B) ( 1 − B δ 2) − 1 / 2) ≠ 1, \displaystyle\begin{array}[]{ll}P^{\prime}(0)&=\displaystyle{\exp\left(\int^{\infty}_{-\infty}\ div\;dt\right)}\\ &=\displaystyle{\lim_{x_{0}\to\infty}\exp\left(\int^{x_{0}}_{-x_{0}}\frac{(1+2B)x+\frac{(1-B)\delta}{B}}{\quad\frac{1}{2}x^{2}+\frac{(1-B)\delta}{B}x+\frac{(1-2B)\delta^{2}+B}{2B^{2}}\quad}dx\right)}\\ &=\displaystyle{\lim_{x_{0}\to\infty}\left[\left(\frac{\ -B^{2}x_{0}^{2}+2\delta B(B-1)x_{0}+\delta^{2}(2B-1)-B\ }{\ -B^{2}x_{0}^{2}-2\delta B(B-1)x_{0}+\delta^{2}(2B-1)-B\ }\right)^{1+2B}\right.}\\ &\qquad\displaystyle{\left.\exp\left(4\delta B^{1/2}(1-B)(1-B\delta^{2})^{-1/2}\arctan\frac{\ -Bx+(B-1)\delta\ }{\sqrt{B(1-B\delta^{2})}}\right)\Big|^{x_{0}}_{-x_{0}}\right]}\\ &=\displaystyle{\exp\left(4\pi\delta B^{1/2}(1-B)(1-B\delta^{2})^{-1/2}\right)}\neq 1,\end{array} |  |

when δ ≠ 0 \delta\neq 0 and B ≠ 1 B\neq 1. (Note that 1 − B ​ δ 2 > 0 1-B\delta^{2}>0 is the condition that the system has no singular point on the invariant parabola.) ∎

Figure 6: The graphic ( I 13 1) (I_{13}^{1}).

###### Theorem 4.3.

The graphic ( I 13 1) (I_{13}^{1}) (see Figure 6) has finite cyclicity inside quadratic systems.

###### Proof.

This graphic is a convex graphic through a nilpotent saddle of multiplicity 3, and with a central transition through a saddle-node. In quadratic systems, such a graphic occurs when the nilpotent point is at infinity. Then μ 1 = 0 \mu_{1}=0 in the unfolding, because the equator is invariant. This limits the number and complexity of the limit periodic sets to be considered. Without loss of generality, we can suppose that the saddle-node is attracting. The proof is an easy adjustement of that of Corollary 3.4. Indeed, by Theorem 2.7, the central transition through a saddle-node in normal form coordinates is linear with exponentially small coefficient ϵ ⁡ ( A) {\epsilon}(A) in the parameter unfolding the saddle-node.

Because of the restriction to quadratic systems (hence μ 1 = 0 \mu_{1}=0) we need only consider the limit periodic sets occurring in Sxhh1-Sxhh8 of Table 2, and the connection along the invariant line is always fixed. The upper and intermediate graphics all have cyclicity one: indeed, the first return map has a derivative much smaller than one because of the passage near the saddle-node by Theorem 2.7.

Hence, we need only consider the lower limit periodic sets. The cyclicity is one for Sxhh2c. Indeed, the global Poincaré return map has a derivative less than 1 1, since the Dulac map near the attracting saddle-node on the blow-up sphere is flat (Theorem 2.7, case 2), and hence has a very small derivative. The same is true for Sxhh8c because the transition is fixed between the saddle and the saddle-node on the blow-up sphere. Indeed, since the stable-center transition near the saddle-node is flat, then the composition of three maps on the blow-up sphere (the passage near the saddle (given in Theorem 2.5) with the regular transition between the saddle and the saddle-node and the stable-center transition near the saddle-node is flat.

We group the rest of the limit periodic sets into classes and give sketchy arguments, since these are quite classical.

Sxhh1, Sxhh4, Sxhh5 and Sxhh6. The argument is similar to the finite cyclicity of a graphic with a saddle-node with center transition and a hyperbolic saddle. The cyclicity is 1 1 if the hyperbolicity ratio τ \tau at the saddle for Sxhh1 (resp. the product τ \tau of the hyperbolicity ratios at the two saddle points for Sxhh4 and Sxhh6) is greater than one since the Poincaré return map has a derivative less than 1 1.

When τ ≤ 1 \tau\leq 1, we consider the displacement map L ν: Σ 4 ⟶ Σ L_{\nu}:\Sigma_{4}\longrightarrow\Sigma (see Figure 7 (a)), defined by L ν = R 3, ν ∘ D 3, ν ∘ T ν ∘ D 4, ν − 1 − D ν − 1 ∘ R 4, ν − 1 L_{\nu}=R_{3,\nu}\circ D_{3,\nu}\circ T_{\nu}\circ D_{4,\nu}^{-1}-D_{\nu}^{-1}\circ R_{4,\nu}^{-1}. It has been shown in [4] that it is possible to choose normalizing coordinates on Π \Pi, such that R 4, ν R_{4,\nu} is an affine map. Hence, D ν − 1 ∘ R 4, ν − 1 D_{\nu}^{-1}\circ R_{4,\nu}^{-1} is an affine map, whose second derivative is identically zero. If τ < 1 \tau<1, then we directly see that L ν ′′ ​ ( y ~ 4) ≠ 0 L_{\nu}^{\prime\prime}(\tilde{y}_{4})\neq 0, since T ν ​ ( y ~ 4) = ϵ 0 + C ​ y ~ 4 τ + O ⁡ ( y ~ 4) T_{\nu}(\tilde{y}_{4})={\epsilon}_{0}+C\tilde{y}_{4}^{\tau}+O(\tilde{y}_{4}), with C ≠ 0 C\neq 0. If τ = 1 \tau=1, which occurs for μ 3 = 0 \mu_{3}=0, then we can use exactly the same sections and arguments as in Theorem 3.1 since the family rescaling is integrable in this case.

Sxhh3. The argument is similar to the finite cyclicity of a graphic with two saddle-nodes, one with center transition (the one on the blow-up sphere) and one with center-unstable transition. It involves using the Khovanskii method.

(a) Intermediate graphic

(b) Sxhh3

(c) Sxhh7

Figure 7: The sections for ( I 13 1) (I_{13}^{1}).

Indeed, let Σ ′ \Sigma^{\prime} and Π ′ \Pi^{\prime} be two sections in normal form coordinates at the entrance and exit of the saddle-node on the blow-up sphere (see Figure 7 (b)), where Σ ′ \Sigma^{\prime} is parameterized by z z and Π ′ \Pi^{\prime} by w w. We replace considering the displacement map from Π ′ \Pi^{\prime} to Σ ′ \Sigma^{\prime} by considering the equivalent system of two equations

 | { z = S ν ​ ( w), z = D ν ′ − 1 ​ ( w), \begin{cases}z=S_{\nu}(w),\\ z=D_{\nu}^{\prime-1}(w),\end{cases} |  | (4.7) |

where S ν S_{\nu} follows the flow forwards:

 | S ν = T 4, ν ∘ D 4, ν − 1 ∘ R 4, ν ∘ D ν ∘ R 3, ν ∘ D 3, ν ∘ T 3, ν. S_{\nu}=T_{4,\nu}\circ D_{4,\nu}^{-1}\circ R_{4,\nu}\circ D_{\nu}\circ R_{3,\nu}\circ D_{3,\nu}\circ T_{3,\nu}. |  | (4.8) |

The Taylor expansion of S ν S_{\nu} has the form S ν ​ ( w) = ϵ 0 ​ ( A) + ϵ 1 ​ ( A) ​ w ​ ( 1 + h ⁡ ( w, A)) S_{\nu}(w)={\epsilon}_{0}(A)+{\epsilon}_{1}(A)w(1+h(w,A)), where h ⁡ ( w, A) = O ⁡ ( w) h(w,A)=O(w) is bounded and has property (J). Also ϵ 1 ​ ( A) > 0 {\epsilon}_{1}(A)>0, when the saddle-node has disappeared, a necessary condition for the existence of limit cycles. Now, D ν − 1 D_{\nu}^{-1} is the Dulac map following the flow backwards near the saddle-node. The function z = D ν − 1 ​ ( w) z=D_{\nu}^{-1}(w) is solution of the Pfaff equation F A ​ ( w) ​ d ​ z − z ​ d ​ w = 0 F_{A}(w)dz-zdw=0, where F A ​ ( w) = ( w 2 + η ⁡ ( A)) ​ ( 1 + C ⁡ ( A) ​ w) F_{A}(w)=(w^{2}+\eta(A))(1+C(A)w) and F A ​ ( w) ​ ∂ ∂ w + z ​ ∂ ∂ z F_{A}(w)\frac{\partial}{\partial w}+z\frac{\partial}{\partial z} is the normal form of the vector field in the neighborhood of the saddle-node. Hence, we replace the system ( 4.7) by the system

 | { z = S ν ​ ( w), Ω = F A ​ ( w) ​ d ​ z − z ​ d ​ w = 0, \begin{cases}z=S_{\nu}(w),\\ \Omega=F_{A}(w)dz-zdw=0,\end{cases} |  | (4.9) |

Between two solutions of the system ( 4.9), there exists on z = S ν ​ ( w) z=S_{\nu}(w) a contact point of Ω \Omega with z = S ν ​ ( w) z=S_{\nu}(w). Hence, the number of solutions is at most one plus the number of solutions of

 | { z = S ν ​ ( w), z − S ν ′ ​ ( w) ​ F A ​ ( w) = 0, \begin{cases}z=S_{\nu}(w),\\ z-S_{\nu}^{\prime}(w)F_{A}(w)=0,\end{cases} |  | (4.10) |

which yields the 1-dimensional equation V A ​ ( w) = S ν ​ ( w) − S ν ′ ​ ( w) ​ F A ​ ( w) = 0 V_{A}(w)=S_{\nu}(w)-S_{\nu}^{\prime}(w)F_{A}(w)=0. This equation has at most one small solution. Indeed,

 | V A ′ ​ ( w) = ϵ 1 ​ ( A) ​ [1 + O ⁡ ( w) + O ⁡ ( η)] ≠ 0, V_{A}^{\prime}(w)={\epsilon}_{1}(A)\left[1+O(w)+O(\eta)\right]\neq 0, |  |

for small w w and A A sufficiently close to A 0 A_{0}.

Sxhh7. We only need to adapt the argument done for Sxhh3. We consider the sections in Figure 7 (c). Since the connection between the saddle and the saddle-node is fixed on the blow-up sphere, this suggests taking for the displacement map, the map from Π ′ \Pi^{\prime} to Σ ′′ \Sigma^{\prime\prime}, parametrized respectively by z z and w w. As before, we consider the equivalent system of two equations

 | { z = S ν ​ ( w), z = U ν ​ ( w), \begin{cases}z=S_{\nu}(w),\\ z=U_{\nu}(w),\end{cases} |  | (4.11) |

where S ν S_{\nu} is given by ( 4.8) and U ν = D ν ′ ′ − 1 ∘ T ν − 1 ∘ D ν ′ − 1 U_{\nu}=D_{\nu}^{\prime\prime-1}\circ T_{\nu}^{-1}\circ D_{\nu}^{\prime-1}. Let τ ⁡ ( A) \tau(A) be the hyperbolicity ratio at the saddle point. We have

 | v = T ν ∘ D ν ′′ ​ ( z) = c ⁡ ( A) ​ z τ ⁡ ( A) ​ ( 1 + ϕ 1 ​ ( z, A)), v=T_{\nu}\circ D_{\nu}^{\prime\prime}(z)=c(A)z^{\tau(A)}(1+\phi_{1}(z,A)), |  | (4.12) |

where c ⁡ ( A) > 0 c(A)>0 and ϕ 1 \phi_{1} has property (I). As before, the function v = D ν ′ − 1 ​ ( w) v=D_{\nu}^{\prime-1}(w) is solution of the Pfaff equation F A ​ ( w) ​ d ​ v − v ​ d ​ w = 0 F_{A}(w)dv-vdw=0, where F A ​ ( w) = ( w 2 + η) ​ ( 1 + C ⁡ ( A) ​ w) F_{A}(w)=(w^{2}+\eta)(1+C(A)w) and F A ​ ( w) ​ ∂ ∂ w + v ​ ∂ ∂ v F_{A}(w)\frac{\partial}{\partial w}+v\frac{\partial}{\partial v} is the normal form of the vector field in the neighborhood of the saddle-node. Then, replacing ( 4.12) in the Pfaff equation yields

 | τ ⁡ ( A) ​ F A ​ ( w) ​ d ​ z − z ⁡ ( 1 + ϕ 2 ​ ( z, A)) ​ d ​ w = 0, \tau(A)F_{A}(w)dz-z(1+\phi_{2}(z,A))dw=0, |  |

where ϕ 2 ​ ( z, A) \phi_{2}(z,A) has property (I).

The rest of the proof is as for Sxhh3. ∎

## References

- [1] F. Dumortier, R. Roussarie and C. Rousseau, *Hilbert’s 16th problem for quadratic vector fields*, J. Differential Equations 110 (1994), no. 1, 86–133.
- [2] F. Dumortier, R. Roussarie and C. Rousseau, *Elementary graphics of cyclicity 1 and 2*, Nonlinearity 7 (1994), no. 1, 1001–1043.
- [3] F. Dumortier, R. Roussarie and S. Sotomayor, *Generic 3-parameter families of vector fields in the plane, unfoldings of saddle, focus and elliptic singularities with nilpotent linear parts.*Springer Lecture Notes in Mathematics 1480, 1–164 (1991).
- [4] A. Guzman and C. Rousseau, *Genericity conditionsfor finite cyclicity of elementary graphics*, J. Differential Equations 155 (1999), 44–72.
- [5] A. G. Khovanskii, Fewnomials, Translations of Mathematical Mongraphs, 88, American Mathematical Society, 1991.
- [6] R. Roussarie and C. Rousseau, *Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems*, preprint, 2014.
- [7] H. Zhu and C. Rousseau, *Finite cyclicity of graphics with a nilpotent singularity of saddle or elliptic type*, J. Differential Equations 178 (2002), 325–436.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
