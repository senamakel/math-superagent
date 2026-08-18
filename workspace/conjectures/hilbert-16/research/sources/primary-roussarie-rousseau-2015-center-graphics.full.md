<!-- source: https://arxiv.org/html/1506.07104v1 | converted from HTML -->

Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1506.07104v1 [math.DS] 23 Jun 2015

# Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems Thanks: This research was supported by NSERC in Canada.

Robert Roussarie Université de Bourgogne Affiliation: Christiane Rousseau, Université de Montréal

###### Abstract

In this paper we introduce new methods to prove the finite cyclicity of some graphics through a triple nilpotent point of saddle or elliptic type surrounding a center. After applying a blow-up of the family, yielding a singular 3-dimensional foliation, this amounts to proving the finite cyclicity of a family of limit periodic sets of the foliation. The boundary limit periodic sets of these families were the most challenging, but the new methods are quite general for treating such graphics. We apply these techniques to prove the finite cyclicity of the graphic ( I 14 1) (I_{14}^{1}), which is part of the program started in 1994 by Dumortier, Roussarie and Rousseau (and called DRR program) to show that there exists a uniform upper bound for the number of limit cycles of a planar quadratic vector field. We also prove the finite cyclicity of the boundary limit periodic sets in all graphics but one through a triple nilpotent point at infinity of saddle, elliptic or degenerate type (with a line of zeros) and surrounding a center, namely the graphics ( I 6 ​ b 1) (I_{6b}^{1}), ( H 13 3) (H_{13}^{3}), and ( D ​ I 2 ​ b) (DI_{2b}).

## 1 Introduction

This paper is part of a long term program to prove the finiteness part of Hilbert’s 16th problem for quadratic vector fields, sometimes written H ⁡ ( 2) < ∞ H(2)<\infty, namely the existence of a uniform bound for the number of limit cycles of quadratic vector fields. The DRR program (see paper [2]) reduces this problem to proving that 121 graphics (limit periodic sets) have finite cyclicity inside quadratic vector fields, and the long term program is to prove the finite cyclicity of all these graphics.

This program has been an opportunity to develop new more sophisticated methods for analyzing the finiteness of the number of limit cycles bifurcating from graphics in generic families of C ∞ C^{\infty} vector fields, in analytic families of vector fields, and in finite-parameter families of polynomial vector fields. In this paper, we focus on some graphics in the latter case: graphics through a nilpotent point and surrounding a center inside quadratic systems. The general method is to use the Bautin trick, namely transforming a proof of finite cyclicity of a generic graphic into a proof of finite cyclicity of a graphic surrounding a center. This is possible in quadratic systems since the center conditions are well known: indeed all graphics through a nilpotent point and surrounding a center occur in the stratum of reversible systems. The systems of this stratum are symmetric with respect to an axis, and are also Darboux integrable with an invariant line and an invariant conic. In practice, the Bautin trick consists in dividing a displacement map V V in a center ideal, i.e. in writing it as a finite sum of “generalized monomials” times non vanishing functions of the form

 | V ⁡ ( z) = ∑ i = 1 n a i ​ m i ​ ( 1 + h i ​ ( z)), V(z)=\sum_{i=1}^{n}a_{i}m_{i}(1+h_{i}(z)), |  | (1.1) |

where each a i a_{i} belongs to the center ideal in parameter space, m i m_{i} is a generalized monomial in z z and h i ​ ( z) = o ​ ( 1) h_{i}(z)=o(1) behaves well under derivation.

To compute the displacement map, we write it as a difference of compositions of regular transitions and Dulac maps near the singular points. The Dulac maps are calculated in C k C^{k} normalizing coordinates for a family unfolding the vector field. In this paper, we develop some general additional methods, which allow to prove the finite cyclicity of the graphic ( I 14 1) (I_{14}^{1}) (Figure 1 (a)). In particular, for the unfolding of this graphic, it is very helpful to be able to claim that all regular transitions are the identity in the center case. This is possible if we exploit the fact that the centers occur when the system is symmetric, and if we choose cleverly the sections on which the different transition maps are defined. Also, in the center case, the Dulac maps have a simple form since the system is Darboux integrable.

(a) ( I 14 1) (I_{14}^{1})

(b) ( I 6 ​ b 1) (I_{6b}^{1})

(c) ( H 13 3) (H_{13}^{3})

(d) ( D ​ I 2 ​ b) (DI_{2b})

Figure 1: The graphics ( I 14 1) (I_{14}^{1}), ( I 6 ​ b 1) (I_{6b}^{1}), ( H 13 3) (H_{13}^{3}) and ( D ​ I 2 ​ b) (DI_{2b}).

The methods can be summarized as follows.

- •

We highlight that the change to C k C^{k} normalizing coordinates in the neighborhood of the singular points on the blow-up locus can be done by an operator. This allows preserving the symmetry in the center case when changing to normalizing coordinates.

- •

We introduce a uniform way of calculating the two types of Dulac maps when entering the blow-up through a much shorter proof than the one given in [8].

- •

Although each Dulac map is not C k C^{k}, we can divide in the center ideal its difference to the corresponding Dulac map in the integrable case.

- •

The method of the blow-up of the family allows reducing the proof of finite cyclicity of the graphic to the proof that a certain number of limit periodic sets have finite cyclicity. These limit periodic sets are defined in the blown-up space. The ones obtained in blowing up a nilpotent saddle are shown in Table 2. For all of them but one (the boundary limit periodic set), we can reduce the displacement map to a 1 1 -dimensional map, the number of zeros of which can be bounded by the Bautin trick and a derivation-division algorithm on a map of type ( 1.1). The boundary limit periodic set is more challenging, since we need to work with a 2-dimensional displacement map, the zeros of which we must study along the leaves of an invariant foliation coming from the blow-up. We introduce a generalized derivation operator, which allows performing a derivation-division algorithm on functions of the type

 | V ⁡ ( r, ρ) = ∑ i = 1 n a i ​ m i ​ ( 1 + h i ​ ( r, ρ)), V(r,\rho)=\sum_{i=1}^{n}a_{i}m_{i}(1+h_{i}(r,\rho)), |  | (1.2) |

where h i h_{i} are 𝒞 k {\mathcal{C}}^{k} -functions on monomials and m i m_{i} are generalized monomials in r r, ρ \rho (see definitions in Appendix II). During this process, we have to take into account that r ​ ρ = Cst r\rho=\mathrm{Cst}.

We have a partial result for every graphic, but one (namely ( H 14 3) (H^{3}_{14})), through a triple point at infinity:

###### Theorem 1.1.

Let us consider the graphics ( I 14 1) (I^{1}_{14}), ( I 6 ​ b 1) (I^{1}_{6b}), ( H 13 3) (H^{3}_{13}) and ( D ​ I 2 ​ b) (DI_{2b}) through a triple point at infinity (see Figure 1). Then for any of them, the boundary periodic limit set obtained in the blowing up has a finite cyclicity.

Theorem 1.1 is not sufficient to prove that the given graphic has a finite cyclicity inside the family of quadratic vector fields. The reason is that, beside the boundary limit periodic set, other limit periodic sets (see for instance Table 2 for ( I 14 1) (I_{14}^{1})) are obtained in the blowing up and, as explained above, we have to prove that each of them has also a finite cyclicity. We present here a complete result for the first graphic:

###### Theorem 1.2.

The graphic ( I 14 1) (I^{1}_{14}) has a finite cyclicity inside the family of quadratic vector fields.

As for the finite cyclicity of the other graphics ( I 6 ​ b 1) (I_{6b}^{1}), ( H 13 3) (H_{13}^{3}) and ( D ​ I 2 ​ b) (DI_{2b}), we intend to address the problem in the next future. The finite cyclicity of ( H 13 3) (H_{13}^{3}) should be straightforward with arguments identical to those used for ( I 14 1) (I_{14}^{1}). It will be done simultaneously with the corresponding generic graphic ( H 12 3) (H_{12}^{3}). Some of the limit periodic sets to be studied for ( I 6 ​ b 1) (I_{6b}^{1}) will involve four Dulac maps of second type. For these limit periodic sets, it is not possible to reduce the study of the cyclicity to a single equation. Hence, new methods will need to be adapted to treat the center case, when the periodic solutions correspond to a system of two equations in the four variables r 1, ρ 1, r 2, ρ 2 r_{1},\rho_{1},r_{2},\rho_{2}, with r 1 ​ ρ 1 = ν 1 r_{1}\rho_{1}=\nu_{1} and r 2 ​ ρ 2 = ν 2 r_{2}\rho_{2}=\nu_{2}. As for the graphic ( D ​ I 2 ​ b) (DI_{2b}), some of the limit periodic sets to be studied involve four Dulac maps of second type, two of them through the semi-hyperbolic points P 1 P_{1} and P 2 P_{2} on the blown-up sphere.

The techniques developed in this paper can be adapted for studying the boundary limit periodic sets of graphics of the DRR program through a nilpotent finite singular point. The only new difficulty in that case is to show that the three parameters of the leading terms in the displacement map do indeed generate the center ideal. We also hope to adapt them to study the boundary graphic of the hemicycle ( H 14 3) (H^{3}_{14}): there, the additional difficulty is the two semi-hyperbolic points along the equator.

Proofs of Theorems 1.1 and 1.2 are given in Section 3 and Appendix II, where the detailed computations of cyclicity are found in Theorems 5.8, 5.12 and 5.13. Theorem 4.1 in Appendix I, gives a statement about normal form for 3-dimensional hyperbolic saddle points in a way adapted to this paper. Theorem 4.5 of the same appendix gives a new proof for Dulac transitions near these saddle points, shorter than the one given in [8]. Precise properties for the specific unfoldings deduced from the quadratic family are proved in Appendix III. These properties of some parameter functions are needed to obtain the results of finite cyclicity.

## 2 Preliminaries

### 2.1 Normal form for the unfolding of a nilpotent triple point of saddle or elliptic type

We consider graphics through one singular point, which is a triple nilpotent point of saddle or elliptic type. A germ of vector field in the neighborhood of such a point has the form

 | x ˙ = y y ˙ = ± x 3 + b ​ x ​ y + η ​ x 2 ​ y + y ​ O ​ ( x 3) + O ⁡ ( y 2). \displaystyle\begin{split}\dot{x}&=y\\ \dot{y}&=\pm x^{3}+bxy+\eta x^{2}y+yO(x^{3})+O(y^{2}).\end{split} |  | (2.1) |

The saddle case corresponds to the plus sign, and the elliptic case to the minus sign with | b | ≥ 2 ​ 2 |b|\geq 2\sqrt{2}. In the elliptic case, we limit ourselves here to the case | b | > 2 ​ 2 |b|>2\sqrt{2}, which corresponds geometrically to a nilpotent point with hyperbolic points on the divisor of the quasi-homogeneous blow-up.

The unfolding of such points has been studied by Dumortier, Roussarie and Sotomayor, [4], including a normal form for the unfolding of the family. A different normal form has been used in [8] for studying the finite cyclicity of generic graphics through such singular points, when we limit ourselves to | b | > 2 ​ 2 |b|>2\sqrt{2} in the elliptic case. This normal form is particularly suitable for applications in quadratic vector fields, where there is always an invariant line through a nilpotent point of multiplicity 3 3.

A germ of C ∞ C^{\infty} vector field in the neighborhood of a nilpotent point of multiplicity 3 3 of saddle or elliptic type can be brought by an analytic change of coordinates to the form

 | x ˙ = y + a ​ x 2, y ˙ = y ⁡ ( x + η ​ x 2 + o ⁡ ( x 2) + O ⁡ ( y)). \displaystyle\begin{split}\dot{x}&=y+ax^{2},\\ \dot{y}&=y(x+\eta x^{2}+o(x^{2})+O(y)).\end{split} |  | (2.2) |

This requires an additional change of variable and scaling compared to what has been done in [8]. The point is a nilpotent saddle when a < 0 a<0 and a nilpotent elliptic point when a > 0 a>0 (see Figure 2). The case | b | = 2 ​ 2 |b|=2\sqrt{2} corresponds to a = 1 2 a=\frac{1}{2}.

(a) Saddle case

(b) Elliptic case

Figure 2: The different topological types

For a ≠ 1 2 a\neq\frac{1}{2}, a generic unfolding depending on a multi-parameter λ = ( μ 1, μ 2, μ 3, μ) \lambda=(\mu_{1},\mu_{2},\mu_{3},\mu) has the form

 | x ˙ = y + a ⁡ ( λ) ​ x 2 + μ 2, y ˙ = μ 1 + μ 3 ​ y + x 4 ​ h 1 ​ ( x, ε) + y ⁡ ( x + η ​ x 2 + x 3 ​ h 2 ​ ( x, λ)) + y 2 ​ Q ​ ( x, y, λ), \displaystyle\begin{split}\dot{x}&=y+a(\lambda)x^{2}+\mu_{2},\\ \dot{y}&=\mu_{1}+\mu_{3}y+x^{4}h_{1}(x,{\varepsilon})+y(x+\eta x^{2}+x^{3}h_{2}(x,\lambda))+y^{2}Q(x,y,\lambda),\end{split} |  | (2.3) |

where h 1 ​ ( x, λ) = O ⁡ ( | λ |) h_{1}(x,\lambda)=O(|\lambda|). Moreover, h 1, h 2, Q h_{1},h_{2},Q are C ∞ C^{\infty} functions, and Q Q can be chosen of arbitrarily high order in λ \lambda.

### 2.2 Finite cyclicity of a graphic

###### Definition 2.1.

A *graphic*Γ \Gamma of a vector field X 0 X_{0}, i.e. a union of trajectories and singular points, has *finite cyclicity*inside a family X λ X_{\lambda} if there exists N ∈ ℕ N\in\mathbb{N}, ε > 0 {\varepsilon}>0 and δ > 0 \delta>0 such that any vector field X λ X_{\lambda} with | λ | < δ |\lambda|<\delta has at most N N periodic solutions at a Hausdorff distance less than ε {\varepsilon} from Γ \Gamma. If a graphic has a finite cyclicity, its *cyclicity*is the minimum of such numbers N N.

This means that when studying the finite cyclicity of a graphic Γ \Gamma, we need to find a uniform bound for the number of periodic solutions that can appear from it, for all values of the multi-parameter in a small neighborhood W W of the origin. Typically we need to find a uniform bound for the number of fixed points of the Poincaré return map or, equivalently, for the number of zeros of some displacement map between two transversal sections to the graphic. With graphics containing a nilpotent singular point there is no way to make a uniform treatment for all λ ∈ W \lambda\in W, and we typically cover W W by a finite number of sectors, on each of which we give a uniform bound. The method for doing this is the *blow-up of the family*, which was first introduced in [6], and next applied to slow-fast systems in [1].

### 2.3 Blow-up of the family

We take the neighborhood of the origin in parameter-space of the form 𝕊 2 × [0, ν 0) × U \mathbb{S}^{2}\times[0,\nu_{0})\times U, where U U is a neighborhood of 0 0 in μ \mu -space and we make the change of parameters

 | ( μ 1, μ 2, μ 3) = ( ν 3 ​ μ ¯ 1, ν 2 ​ μ ¯ 2, ν ​ μ ¯ 3), (\mu_{1},\mu_{2},\mu_{3})=(\nu^{3}\overline{\mu}_{1},\nu^{2}\overline{\mu}_{2},\nu\overline{\mu}_{3}), |  | (2.4) |

where M ¯ = ( μ ¯ 1, μ ¯ 2, μ ¯ 3) ∈ 𝕊 2 \overline{M}=(\overline{\mu}_{1},\overline{\mu}_{2},\overline{\mu}_{3})\in\mathbb{S}^{2} and ν ∈ [0, ν 0) \nu\in[0,\nu_{0}).

Note that 𝕊 2 \mathbb{S}^{2} is compact. Hence, to give an argument of finite cyclicity for the graphic Γ \Gamma, it suffices to find a neighborhood of each M ¯ = ( μ ¯ 1, μ ¯ 2, μ ¯ 3) ∈ 𝕊 2 \overline{M}=(\overline{\mu}_{1},\overline{\mu}_{2},\overline{\mu}_{3})\in\mathbb{S}^{2} inside 𝕊 2 \mathbb{S}^{2}, a corresponding ν 0 > 0 \nu_{0}>0 and a corresponding U U on which we can give a bound for the number of limit cycles. In our study, we will consider special values a 0 a_{0} of a a. It is important to note that a ⁡ ( λ) a(\lambda) depends on λ \lambda, and hence that a − a 0 a-a_{0} is in some sense a parameter in itself.

The way to handle this program is to do a *blow-up of the family.*For this, we introduce the weighted blow-up of the singular point ( 0, 0, 0) (0,0,0) of the three-dimensional family of vector fields, obtained by adding the equation ν ˙ = 0 \dot{\nu}=0 to ( 2.3). The blow-up transformation is given by

 | ( x, y, ν) = ( r ​ x ¯, r 2 ​ y ¯, r ​ ρ), (x,y,\nu)=(r\overline{x},r^{2}\overline{y},r\rho), |  | (2.5) |

with r > 0 r>0 and ( x ¯, y ¯, ρ) ∈ 𝕊 2 (\overline{x},\overline{y},\rho)\in\mathbb{S}^{2}. After dividing by r r the transformed vector field, we get a family of C ∞ C^{\infty} vector fields X ¯ A \overline{X}_{A}, depending on the parameters A = ( a − a 0, M ¯, μ) A=(a-a_{0},\overline{M},\mu). The foliation { ν = r ρ = Cst } \{\nu=r\rho=\mathrm{Cst}\} is invariant under the flow. The leaves { r ρ = ν } \{r\rho=\nu\}, with ν > 0 \nu>0, are regular two-dimensional manifolds, while the critical locus { r ρ = 0 } \{r\rho=0\} is stratified and contains the two strata (see Figure 3):

- •

𝕊 1 × ℝ + \mathbb{S}^{1}\times\mathbb{R}^{+} is the blow-up of X 0 X_{0} (for λ = 0 \lambda=0);

- •

D μ ¯ = { x ¯ 2 + y ¯ 2 + ρ 2 = 1 ∣ ρ ≥ 0 } D_{\overline{\mu}}=\{\overline{x}^{2}+\overline{y}^{2}+\rho^{2}=1\mid\rho\geq 0\}, for any μ ¯ ∈ 𝕊 2 \overline{\mu}\in\mathbb{S}^{2}.

### 2.4 Limit periodic sets in the blown-up family

The vector field X ¯ A \overline{X}_{A} has singular points on r = ρ = 0 r=\rho=0. For a ≠ 1 2 a\neq\frac{1}{2}, there will be four distinct singular points (occuring in two pairs) corresponding to y ¯ = 0 \overline{y}=0 (for P 1 P_{1} and P 2 P_{2}) and y ¯ = 1 − 2 ​ a 2 \overline{y}=\frac{1-2a}{2} (for P 3 P_{3} and P 4 P_{4}): see Figure 3. Their eigenvalues appear in Table 1.

(a) The saddle case

(b) The elliptic case

Figure 3: The stratified set { r ρ = 0 } \{r\rho=0\} in the blow-up

 | r r | ρ \rho | y y |

P 1 P_{1} | − a -a | a \ \ a | − ( 1 − 2 ​ a) -(1-2a) |

P 2 P_{2} | a \ \ a | − a -a | ( 1 − 2 ​ a) \ \ (1-2a) |

P 3 P_{3} | 1 / 2 \ \ 1/2 | − 1 / 2 -1/2 | − ( 1 − 2 ​ a) -(1-2a) |

P 4 P_{4} | − 1 / 2 -1/2 | 1 / 2 \ \ 1/2 | ( 1 − 2 ​ a) \ \ (1-2a) |

Table 1: The eigenvalues at P i P_{i} ( i = 1, 2, 3, 4 i=1,2,3,4)

We will study the finite cyclicity of a graphic Γ \Gamma joining a pair of opposite points P i P_{i} and P i + 1 P_{i+1} in X ¯ \overline{X}, with i = 1 i=1 or i = 3 i=3. We consider a particular value A 0 = ( a 0, M ¯ 0, μ 0) A_{0}=(a_{0},\overline{M}_{0},\mu_{0}). Here is the strategy for finding an upper bound for the number of limit cycles that appear for A A in a neighborhood of A 0 A_{0}. We determine the phase portrait of the family rescaling ( 2.6) on D μ ¯ D_{\overline{\mu}}: this allows determining *limit periodic sets*Γ ¯ \overline{\Gamma}, which are formed by the union of Γ \Gamma with a finite number of trajectories and singular points on D μ ¯ D_{\overline{\mu}} joining P i P_{i} and P i + 1 P_{i+1}, so that their orientation be compatible with that of Γ \Gamma. The limit periodic sets to be studied appear in Table 2 for the saddle case. They come from studying the phase portrait of the *family rescaling*

 | x ¯ ˙ = y ¯ + a ​ x ¯ 2 + μ ¯ 2, y ¯ ˙ = μ ¯ 1 + μ ¯ 3 ​ y ¯ + x ¯ ​ y ¯, \displaystyle\begin{split}\dot{\overline{x}}&=\overline{y}+a\overline{x}^{2}+\overline{\mu}_{2},\\ \dot{\overline{y}}&=\overline{\mu}_{1}+\overline{\mu}_{3}\overline{y}+\overline{x}\,\overline{y},\end{split} |  | (2.6) |

obtained by putting ρ = 1 \rho=1 and r = 0 r=0. It then suffices to show that each limit periodic set has finite cyclicity, i.e. to show the existence of an upper bound for the number of periodic solutions of X ¯ A \overline{X}_{A} for A A in a small neighborhood of A 0 A_{0}.

 |  |  |

Sxhh1 | Sxhh2 | Sxhh3 |

 |  |  |

Sxhh4 | Sxhh5 | Sxhh6 |

 |  |  |

Sxhh7 |  | Sxhh8 |

 |  |  |

Sxhh9 |  | Sxhh10 |

Table 2: Convex limit periodic sets of hh-type for a graphic with a nilpotent saddle.

### 2.5 Proving the finite cyclicity of a limit periodic set

Typically, the kind of argument we will use for proving the finite cyclicity of a limit periodic set is the following: we look for the zeroes of a displacement map between two sections. The sections are 2-dimensional but, because of the invariant foliation, the problem can be reduced to a 1-dimensional problem and the conclusion follows by, either an iteration of Rolle’s theorem, or its generalization, namely a derivation-division argument. The technique can be adapted to non generic graphics occurring inside integrable systems: the proof in the generic case is transformed into a proof for the corresponding graphic, using some adequate division of the coefficients of the displacement map in the ideal of conditions for integrability.

To compute the displacement map, we decompose the related transition maps between sections into compositions of Dulac maps in the neighborhood of the singular points and regular C k C^{k} transitions elsewhere.

### 2.6 Dulac maps

The Dulac maps are the transition maps in the neighborhood of a singular point on r = ρ = 0 r=\rho=0. They are computed when the system is in C k C^{k} normal form. The normalizing theorem is Theorem 4.1 of Appendix I. There, it is proved that the normal form is obtained by a normalizing operator 𝒩 {\mathcal{N}}, a crucial property for this paper. The theorem establishes the existence of a parameter-depending local change of coordinates of class 𝒞 k {\mathcal{C}}^{k} bringing the blow-up of ( 2.3) in the neighborhood of one of the points P i P_{i} into the normal form X ¯ A N \overline{X}_{A}^{N} (up to t ↦ − t t\mapsto-t) written in normal form coordinates ( Y ¯, r, ρ) (\overline{Y},r,\rho) (provided that the eigenvalue in r r has a sign opposite to the two other eigenvalues). Using Table 1, we take σ = 2 ​ ( 1 − 2 ​ a) \sigma=2(1-2a) near σ 0 = 2 ​ ( 1 − 2 ​ a 0) \sigma_{0}=2(1-2a_{0}) for P 3 P_{3} and P 4 P_{4} when a 0 < 1 2 a_{0}<\frac{1}{2}, and σ = 2 ​ a − 1 a \sigma=\frac{2a-1}{a} near σ 0 = 2 ​ a 0 − 1 a 0 \sigma_{0}=\frac{2a_{0}-1}{a_{0}} for P 1 P_{1} and P 2 P_{2} when a > 1 2 a>\frac{1}{2}. The normal form X ¯ A N \overline{X}_{A}^{N} is given by

1. 1.

If σ 0 ∉ ℚ: \sigma_{0}\not\in\mathbb{Q}:

 | X ¯ A N: { r ˙ = r, ρ ˙ = − ρ, Y ¯ ˙ = − ( σ + φ A ​ ( ν)) ​ Y ¯. \overline{X}^{N}_{A}:\begin{cases}{\dot{r}}=r,\\ {\dot{\rho}}=-\rho,\\ \dot{\overline{Y}}=-(\sigma+\varphi_{A}(\nu))\overline{Y}.\end{cases} |  | (2.7) |

2. 2.

If σ 0 = p q ∈ ℚ, \sigma_{0}=\frac{p}{q}\in\mathbb{Q}, with ( p, q) = 1 (p,q)=1 when q ≠ 1: q\not=1:

 | X ¯ A N: { r ˙ = r, ρ ˙ = − ρ, Y ¯ ˙ = − ( σ + φ A ​ ( ν)) ​ Y ¯ + Φ A ​ ( ν, r p ​ Y ¯ q) ​ Y ¯ + ρ p ​ η A ​ ( ν), \overline{X}^{N}_{A}:\begin{cases}{\dot{r}}=r,\\ {\dot{\rho}}=-\rho,\\ {\dot{\overline{Y}}}=-\Big(\sigma+\varphi_{A}(\nu)\Big)\overline{Y}+\Phi_{A}(\nu,r^{p}\overline{Y}^{q})\overline{Y}+\rho^{p}\eta_{A}(\nu),\end{cases} |  | (2.8) |

with η A ≡ 0 \eta_{A}\equiv 0 when σ 0 ∉ ℕ \sigma_{0}\not\in\mathbb{N} ( q ≠ 1 q\not=1).

The functions φ A, Φ A, η A \varphi_{A},\Phi_{A},\eta_{A} are polynomials of degree ≤ K ⁡ ( k) \leq K(k) increasing with k, k, with smooth coefficients in A A and Φ A ​ ( ν, 0) ≡ 0. \Phi_{A}(\nu,0)\equiv 0.

We introduce the “compensator” function ω ⁡ ( ξ, α) \omega(\xi,\alpha), also denoted ω α ​ ( ξ) \omega_{\alpha}(\xi), defined by

 | ω ⁡ ( ξ, α) = ω α ​ ( ξ) = { ξ − α − 1 α, α ≠ 0, − ln ⁡ ξ, α = 0. \omega(\xi,\alpha)=\omega_{\alpha}(\xi)=\begin{cases}\frac{\xi^{-\alpha}-1}{\alpha},&\alpha\not=0,\\ -\ln\xi,&\alpha=0.\end{cases} |  | (2.9) |

We propose in Appendix I a new computation of the Dulac maps previously studied in [8]. There are two types of Dulac transitions. The first type of transition map goes from a section { r = r 0 } \{r=r_{0}\} to a section { ρ = ρ 0 } \{\rho=\rho_{0}\}, or the other way around. This type of transition typically behaves as an affine map, which is a very strong contraction or dilatation. The study of the number of zeroes of a displacement involving only Dulac maps of the first type is reduced to the study of the number of zeroes of a 1-dimensional map.

The second type of Dulac map is concerned with a transition map from a section { Y ¯ = Y 0 } \{\overline{Y}=Y_{0}\} to, either a section { r = r 0 } \{r=r_{0}\}, or a section { ρ = ρ 0 } \{\rho=\rho_{0}\}. We take ν 0 = r 0 ​ ρ 0. \nu_{0}=r_{0}\rho_{0}.

#### 2.6.1 First type of Dulac map

###### Theorem 2.2.

We consider the Dulac map from the section { ρ = ρ 0 } \{\rho=\rho_{0}\} to the section { r = r 0 } \{r=r_{0}\}, both parametrized by ( Y ¯, ν). (\overline{Y},\nu). Let

 | σ ¯ = σ ¯ ​ ( σ, ν) = σ + φ A ​ ( ν) \bar{\sigma}=\bar{\sigma}(\sigma,\nu)=\sigma+\varphi_{A}(\nu) |  |

and

 | α = α ⁡ ( σ, ν) = σ ¯ ​ ( σ, ν) − σ 0. \alpha=\alpha(\sigma,\nu)=\bar{\sigma}(\sigma,\nu)-\sigma_{0}. |  |

The Y ¯ \overline{Y} -component of the transition map D A D_{A} has the following expression:

1. 1.

If σ 0 ∉ ℚ: \sigma_{0}\not\in\mathbb{Q}:

 | D A ​ ( Y ¯, ν) = ( ν ν 0) σ ¯ ​ Y ¯. D_{A}(\overline{Y},\nu)=\Big(\frac{\nu}{\nu_{0}}\Big)^{\bar{\sigma}}\overline{Y}. |  | (2.10) |

2. 2.

If σ 0 = p q ∈ ℚ \sigma_{0}=\frac{p}{q}\in\mathbb{Q} with ( p, q) = 1 (p,q)=1 when σ 0 ∉ ℕ: \sigma_{0}\not\in\mathbb{N}:

 | D A ​ ( Y ¯, ν) = η A ​ ( ν) ​ ρ 0 p ​ ( ν ν 0) σ ¯ ​ ω ​ ( ν ν 0, α) + ( ν ν 0) σ ¯ ​ ( Y ¯ + ϕ A ​ ( Y ¯, ν)), D_{A}(\overline{Y},\nu)=\eta_{A}(\nu)\rho_{0}^{p}\Big(\frac{\nu}{\nu_{0}}\Big)^{\bar{\sigma}}\omega\Big(\frac{\nu}{\nu_{0}},\alpha\Big)+\Big(\frac{\nu}{\nu_{0}}\Big)^{\bar{\sigma}}\Big(\overline{Y}+\phi_{A}(\overline{Y},\nu)\Big), |  | (2.11) |

with η A \eta_{A} as in ( 2.8). In particular, η A ≡ 0 \eta_{A}\equiv 0 when σ 0 ∉ ℕ. \sigma_{0}\not\in\mathbb{N}.

The function family ϕ A \phi_{A} in ( 2.11) is of order O ⁡ ( ν p + q ​ α ​ ω q + 1 ​ ( ν ν 0, α) ​ | ln ⁡ ν |) O(\nu^{p+q\alpha}\omega^{q+1}\Big(\frac{\nu}{\nu_{0}},\alpha\Big)|\ln\nu|) and for any integer l ≥ 2, l\geq 2, is of class 𝒞 l − 2 {\mathcal{C}}^{l-2} in ( Y ¯, ν 1 / l, ν 1 / l ​ ω ​ ( ν ν 0, α), ν, μ, σ) (\overline{Y},\nu^{1/l},\nu^{1/l}\omega\Big(\frac{\nu}{\nu_{0}},\alpha\Big),\nu,\mu,\sigma).

#### 2.6.2 Second type of Dulac map

###### Theorem 2.3.

We consider the Dulac map from the section { Y ¯ = Y 0 }, \{\overline{Y}=Y_{0}\}, parametrized by ( r, ρ) (r,\rho) to a section { r = r 0 } \{r=r_{0}\} parameterized by ( Y ¯, ν) (\overline{Y},\nu). It has the form ( r, ρ) ↦ ( D A ​ ( r, ρ), ν) (r,\rho)\mapsto(D_{A}(r,\rho),\nu), with its Y ¯ \overline{Y} -component, ( D A ​ ( r, ρ) 𝐶𝐿𝑂𝑆𝐸 (D_{A}(r,\rho), given by:

1. 1.

If σ 0 ∉ ℚ: \sigma_{0}\not\in\mathbb{Q}:

 | D A ​ ( r, ρ) = ( r r 0) σ ¯ ​ Y 0. D_{A}(r,\rho)=\Big(\frac{r}{r_{0}}\Big)^{\bar{\sigma}}Y_{0}. |  | (2.12) |

2. 2.

If σ 0 = p q ∈ ℚ \sigma_{0}=\frac{p}{q}\in\mathbb{Q} with ( p, q) = 1 (p,q)=1 when σ 0 ∉ ℕ: \sigma_{0}\not\in\mathbb{N}:

 | D A ​ ( r, ρ) = η A ​ ( ν) ​ ρ p ​ ( r r 0) σ ¯ ​ ω ​ ( r r 0, α) + ( r r 0) σ ¯ ​ ( Y 0 + ϕ A ​ ( r, ρ)), D_{A}(r,\rho)=\eta_{A}(\nu)\rho^{p}\Big(\frac{r}{r_{0}}\Big)^{\bar{\sigma}}\omega\Big(\frac{r}{r_{0}},\alpha\Big)+\Big(\frac{r}{r_{0}}\Big)^{\bar{\sigma}}\Big(Y_{0}+\phi_{A}(r,\rho)\Big), |  | (2.13) |

with η A \eta_{A} as in ( 2.8) ( η A ≡ 0 \eta_{A}\equiv 0 when OPEN σ 0 ∉ ℕ). \sigma_{0}\not\in\mathbb{N}).

The function family ϕ A \phi_{A} in ( 2.13) is of order O ⁡ ( r p + q ​ α ​ ω q + 1 ​ ( r r 0, α) ​ | ln ⁡ r |) O(r^{p+q\alpha}\omega^{q+1}\Big(\frac{r}{r_{0}},\alpha\Big)|\ln r|) and, for any integer l ≥ 2, l\geq 2, is of class 𝒞 l − 2 {\mathcal{C}}^{l-2} in ( r 1 / l, r 1 / l ​ ω ​ ( r r 0, α), ρ, μ, σ) (r^{1/l},r^{1/l}\omega\Big(\frac{r}{r_{0}},\alpha\Big),\rho,\mu,\sigma).

## 3 Applications to quadratic systems

### 3.1 Quadratic systems with a nilpotent singular point at infinity

###### Theorem 3.1.

A quadratic system with a triple singularity point of saddle or elliptic type at infinity and a finite singular point of center type can be brought to the form

 | { x ˙ = − y + B 0 ​ x 2, y ˙ = x + x ​ y, \left\{\begin{array}[]{ll}\dot{x}&=-y+B_{0}x^{2},\\ \dot{y}&=x+xy,\end{array}\right. |  | (3.1) |

with B 0 > 0 B_{0}>0. For B 0 ≠ 1 B_{0}\neq 1, the full 5 5 -parameter unfolding inside quadratic systems is given with B = B 0 + μ 0 B=B_{0}+\mu_{0} inside the family

 | { x ˙ = − y + B ​ x 2 + μ 2 ​ y 2 + ( μ 4 + B ​ μ 5) ​ x y ˙ = x + x ​ y + μ 3 ​ y 2 + ( 1 − 2 ​ B) ​ μ 5 ​ y. \left\{\begin{array}[]{ll}\dot{x}&=-y+Bx^{2}+\mu_{2}y^{2}+\left(\mu_{4}+B\mu_{5}\right)x\\ \dot{y}&=x+xy+\mu_{3}y^{2}+(1-2B)\mu_{5}y.\end{array}\right. |  | (3.2) |

For B 0 = 1 B_{0}=1, the full 5 5 -parameter unfolding inside quadratic systems is rather given with B = 1 + μ 0 B=1+\mu_{0} inside the family

 | { x ˙ = − y + ( 1 + μ 0) ​ x 2 + μ 2 ​ y 2 + μ 5 ​ x y ˙ = x + ( μ 4 + μ 5) ​ x 2 + x ​ y + μ 3 ​ y 2. \left\{\begin{array}[]{ll}\dot{x}&=-y+(1+\mu_{0})x^{2}+\mu_{2}y^{2}+\mu_{5}x\\ \dot{y}&=x+(\mu_{4}+\mu_{5})x^{2}+xy+\mu_{3}y^{2}.\end{array}\right. |  | (3.3) |

The parameter μ 2 \mu_{2} (resp. μ 3 \mu_{3}) corresponds to a nonzero multiple of the parameter μ 2 \mu_{2} (resp. μ 3 \mu_{3}) in the blow-up of the family at the singular point. There is no parameter μ 1 \mu_{1} in this family since the connection along the equator is fixed.

Moreover for ( 3.1) we have:

1. 1.

B 0 > 1 B_{0}>1 for a nilpotent saddle;

B 0 = 3 2 B_{0}=\frac{3}{2} corresponds to a = − 1 2 a=-\frac{1}{2} in ( 2.2) ( b = 0 b=0 in ( 2.1)).

2. 2.

B 0 < 1 B_{0}<1 for an elliptic point; the elliptic point is of larger codimension, type 1 (the singular points in the blow-up coallesce by pairs) if B 0 = 1 2 B_{0}=\frac{1}{2} (corresponding to a = 1 2 a=\frac{1}{2} in ( 2.2), i.e., b = 2 ​ 2 b=2\sqrt{2} in ( 2.1)).

3. 3.

The system ( 3.2) has an invariant line y = − 1 y=-1 if μ 3 − ( 1 − 2 ​ B) ​ μ 5 = 0 \mu_{3}-(1-2B)\mu_{5}=0.

4. 4.

If μ 2 = μ 3 = μ 4 = 0 \mu_{2}=\mu_{3}=\mu_{4}=0, the system ( 3.2) has an invariant parabola

 | y = 2 ​ B − 1 2 ​ x 2 + ( 2 ​ B − 1) ​ μ 5 ​ x − 1 2 ​ B + ( 2 ​ B − 1) ​ μ 5 2. y=\frac{2B-1}{2}x^{2}+(2B-1)\mu_{5}x-\frac{1}{2B}+(2B-1)\mu_{5}^{2}. |  | (3.4) |

The parabola y = 1 2 ​ x 2 − 1 2 y=\frac{1}{2}x^{2}-\frac{1}{2} is invariant for system ( 3.3) when μ 0 = μ 2 = μ 3 = μ 4 = 0 \mu_{0}=\mu_{2}=\mu_{3}=\mu_{4}=0.

5. 5.

The integrability condition is μ 3 = μ 4 = μ 5 = 0 \mu_{3}=\mu_{4}=\mu_{5}=0, for which we have the following graphics with return map

  - •

B > 1 B>1: ( I 14 1) (I_{14}^{1}),

  - •

1 2 < B < 1 \frac{1}{2}<B<1: ( I 6 ​ b 1) (I_{6b}^{1}),

  - •

0 < B < 1 2 0<B<\frac{1}{2}: ( H 13 3) (H_{13}^{3}),

  - •

B = 0 B=0: ( H 14 3) (H_{14}^{3}),

  - •

B = 1 B=1: ( D ​ I 2 ​ b) (DI_{2b}).

6. 6.

The value of “ a a ” in the corresponding normal form ( 2.3) is a = 1 − B a=1-B, and the parameters μ 2 \mu_{2} and μ 3 \mu_{3} correspond to μ 2 \mu_{2} and μ 3 \mu_{3} up to a nonzero constant.

###### Proof.

We can suppose that the nilpotent singular point at infinity is located on the y-axis, the other singular point at infinity on the x-axis, and the focus or center at the origin. Then the system can be brought to the form

 | { x ˙ = δ 10 ​ x + δ 01 ​ y + δ 20 ​ x 2 + δ 11 ​ x ​ y, y ˙ = γ 10 ​ x + γ 01 ​ y + γ 11 ​ x ​ y + γ 02 ​ y 2. \left\{\begin{array}[]{ll}\dot{x}&=\delta_{10}x+\delta_{01}y+\delta_{20}x^{2}+\delta_{11}xy,\\ \dot{y}&=\gamma_{10}x+\gamma_{01}y+\gamma_{11}xy+\gamma_{02}y^{2}.\end{array}\right. |  | (3.5) |

Localizing the system ( 3.5) at the singular point at infinity on y-axis by v = x y, w = 1 y v=\frac{x}{y},\ \ w=\frac{1}{y}, we have

 | { v ˙ = ( δ 11 − γ 02) ​ v − δ 01 ​ w + ( δ 20 − γ 11) ​ v 2 + ( δ 10 − γ 01) ​ v ​ w − γ 10 ​ v 2 ​ w, w ˙ = w ⁡ ( − γ 02 − γ 01 ​ w − γ 11 ​ v − γ 10 ​ v ​ w). \left\{\begin{array}[]{ll}\dot{v}&=(\delta_{11}-\gamma_{02})v-\delta_{01}w+(\delta_{20}-\gamma_{11})v^{2}+(\delta_{10}-\gamma_{01})vw-\gamma_{10}v^{2}w,\\ \dot{w}&=w(-\gamma_{02}-\gamma_{01}w-\gamma_{11}v-\gamma_{10}vw).\end{array}\right. |  | (3.6) |

For the singular point ( 0, 0) (0,0) of system ( 3.6) to be nilpotent, we should have δ 11 = γ 02 = 0 \delta_{11}=\gamma_{02}=0. The point is triple if γ 11 ≠ 0 \gamma_{11}\neq 0.

We want the finite singular point to be a center, which corresponds in this case to the system being reversible with respect to a line. Because of our choice of singular points at infinity this line can only be the y y -axis. Then δ 10 = γ 01 = 0 \delta_{10}=\gamma_{01}=0.

By a rescaling and still using the original coordinates ( x, y) (x,y), we obtain the system ( 3.1).

The change of coordinates W = − w + ( B 0 − 1) ​ v 2 W=-w+(B_{0}-1)v^{2} brings the system ( 3.6) into the equivalent form

 | { V ˙ = W W ˙ = ( B 0 − 1) ​ V 3 + ( 2 ​ B 0 − 3) ​ V ​ W + o ⁡ ( V 3) + o ⁡ ( V ​ W). \left\{\begin{array}[]{ll}\dot{V}&=W\\ \dot{W}&=(B_{0}-1)V^{3}+(2B_{0}-3)VW+o(V^{3})+o(VW).\end{array}\right. |  | (3.7) |

The classification of the nilpotent singularity at infinity follows.

A general unfolding preserving the singular point at the origin (which is simple) is of the form (after scaling of x x, y y, and t t)

 | { x ˙ = − y + B ​ x 2 + m 10 ​ x + m 11 ​ x ​ y + m 02 ​ y 2 y ˙ = x + x ​ y + n 01 ​ y + n 20 ​ x 2 + n 02 ​ y 2, \left\{\begin{array}[]{ll}\dot{x}&=-y+Bx^{2}+m_{10}x+m_{11}xy+m_{02}y^{2}\\ \dot{y}&=x+xy+n_{01}y+n_{20}x^{2}+n_{02}y^{2},\end{array}\right. |  | (3.8) |

with B B close to B 0 B_{0}. We use a change of variable ( X, Y) = ( x + ζ 1 ​ y, ζ 2 ​ x + y) (X,Y)=(x+\zeta_{1}y,\zeta_{2}x+y) for small ζ 1, ζ 2 \zeta_{1},\zeta_{2}. The terms in X ​ Y XY in the expression of X ˙ \dot{X} and the term in X 2 X^{2} in the expression of Y ˙ \dot{Y} vanish precisely when

 | { ( 2 ​ B − 1) ​ ζ 1 − m 11 ​ ( 1 + ζ 1 ​ ζ 2) + 2 ​ ζ 2 ​ m 02 + 2 ​ ζ 1 ​ n 02 ​ ( ζ 1 + ζ 2) − ζ 1 2 ​ ζ 2 = 0, ( B − 1) ​ ζ 2 + ( 1 + ζ 2 2) ​ n 02 − ζ 2 2 ​ n 11 + ζ 2 3 ​ m 02 = 0, \begin{cases}(2B-1)\zeta_{1}-m_{11}(1+\zeta_{1}\zeta_{2})+2\zeta_{2}m_{02}+2\zeta_{1}n_{02}(\zeta_{1}+\zeta_{2})-\zeta_{1}^{2}\zeta_{2}=0,\\ (B-1)\zeta_{2}+(1+\zeta_{2}^{2})n_{02}-\zeta_{2}^{2}n_{11}+\zeta_{2}^{3}m_{02}=0,\end{cases} |  |

which can be solved for ( ζ 1, ζ 2) (\zeta_{1},\zeta_{2}) by the implicit function theorem except for B 0 = 1 B_{0}=1. When B 0 = 1 B_{0}=1, we replace the second equation by the vanishing of the term in Y Y in in the expression of Y ˙ \dot{Y}, namely

 | ζ 1 + ζ 2 − n 01 + m 10 ​ ζ 1 ​ ζ 2 = 0. \zeta_{1}+\zeta_{2}-n_{01}+m_{10}\zeta_{1}\zeta_{2}=0. |  |

Again, we get a system that can be solved for ( ζ 1, ζ 2) (\zeta_{1},\zeta_{2}) by the implicit function theorem. ∎

### 3.2 Finite cyclicity of the boundary limit periodic sets of ( I 14 1) (I_{14}^{1}), ( I 6 ​ b) (I_{6b}) and ( D ​ I 2 ​ b) (DI_{2b})

###### Notation 3.2.

In the whole paper, ∗ *denotes a nonzero constant, which may depend on some parameters.

###### Theorem 3.3.

The boundary limit periodic sets of ( I 14 1) (I_{14}^{1}), ( I 6 ​ b) (I_{6b}) and ( D ​ I 2 ​ b) (DI_{2b}) (see Figures 1 (a), (b) and (d) and 4) have finite cyclicity.

Figure 4: The boundary graphic through P 3 P_{3} and P 4 P_{4} and the four sections Σ i \Sigma_{i} and Π i \Pi_{i}, i = 3, 4 i=3,4, in the normalizing coordinates.

###### Proof.

The finite cyclicity of the boundary limit periodic set is studied inside the family ( 3.2) when B 0 ≠ 1 B_{0}\neq 1, and we will discuss later the adjustment when B 0 = 1 B_{0}=1.

Choice of parameters. We take as parameters

 | M = ( μ ¯ 3, μ 4, μ 5, μ ¯ 2, B 0 − 1) = ( M C, μ ¯ 2, B 0 − 1), M=(\overline{\mu}_{3},\mu_{4},\mu_{5},\overline{\mu}_{2},B_{0}-1)=(M_{C},\overline{\mu}_{2},B_{0}-1), |  | (3.9) |

with ( μ ¯ 2, μ ¯ 3) ∈ 𝕊 1 (\overline{\mu}_{2},\overline{\mu}_{3})\in\mathbb{S}_{1} and ( B 0 − 1, μ 4, μ 5) (B_{0}-1,\mu_{4},\mu_{5}) in a small ball. The parameters

 | M C = ( μ ¯ 3, μ 4, μ 5) M_{C}=(\overline{\mu}_{3},\mu_{4},\mu_{5}) |  | (3.10) |

unfold the integrable situation. We let I C I_{C} be the ideal of germs of C k C^{k} -functions of the parameters generated by { μ ¯ 3, μ 4, μ 5 } \{\overline{\mu}_{3},\mu_{4},\mu_{5}\}.

###### Notation 3.4.

1. 1.

The symbol O P ​ ( M C) O_{P}(M_{C}) refers to a function in the parameter M M belonging to the ideal I C I_{C}.

2. 2.

The symbol O G ​ ( M C) O_{G}(M_{C}) refers to a function of ( X, M) (X,M) which belongs to the ideal generated by I C I_{C} inside the space of functions of ( X, M). (X,M). Depending on the limit periodic set, we could have X = x ¯ 3 X=\overline{x}_{3}, where x ¯ 3 \overline{x}_{3} is the normalizing coordinate near P 3 P_{3}, or X = ( r, ρ) X=(r,\rho).

The displacement map. It is better to consider the chart y ¯ = 1 \overline{y}=1 in the blow-up. We take C k C^{k} normalizing charts in the neighborhood of P 3 P_{3} and P 4 P_{4}. As discussed above, these C k C^{k} normalizing charts can be chosen symmetric one to the other under the center conditions. The normalizing coordinates are ( r, ρ, x ¯ i) (r,\rho,\overline{x}_{i}) near P i P_{i}. We consider sections Σ i = { x ¯ i = X 0 } \Sigma_{i}=\{\overline{x}_{i}=X_{0}\} and Π i = { r = r 0 } \Pi_{i}=\{r=r_{0}\} in the normalizing charts. The sections Σ i \Sigma_{i} are parameterized by ( r, ρ) (r,\rho), and the sections Π i \Pi_{i} by ( x ¯ i, ν) (\overline{x}_{i},\nu).

Let V = D 4 ∘ S − T ∘ D 3 V=D_{4}\circ S-T\circ D_{3} be the displacement map from Σ 3 \Sigma_{3} to Π 4 \Pi_{4}: T T and D 3 D_{3} follow the flow forward, while S S and D 4 D_{4} follow the flow backwards.

Let us first give the proof when σ i ​ ( 0) ∉ ℚ \sigma_{i}(0)\notin\mathbb{Q}. The Dulac maps are defined from sections Σ i = { x ¯ i = X 0 } \Sigma_{i}=\{\overline{x}_{i}=X_{0}\} to sections Π i = { r = r 0 } \Pi_{i}=\{r=r_{0}\}, with X 0 X_{0} and r 0 r_{0} fixed. Then the Dulac maps D i D_{i} have the form

 | D i ​ ( r, ρ) = ( C i ​ ( M) ​ r σ ¯ i, r ​ ρ). D_{i}(r,\rho)=(C_{i}(M)r^{\overline{\sigma}_{i}},r\rho). |  | (3.11) |

We can choose X 0 X_{0} and r 0 r_{0} so that C i ​ ( 0) = 1 C_{i}(0)=1, i.e. X 0 ​ r 0 − σ 0 = 1 X_{0}r_{0}^{-\sigma_{0}}=1, and C 3 ​ ( M) = C 4 ​ ( M) C_{3}(M)=C_{4}(M) under the center conditions.

The map T T has the form

 | T ⁡ ( x ¯ 3, ν) = ( H ⁡ ( x ¯ 3, ν), ν). T(\overline{x}_{3},\nu)=(H(\overline{x}_{3},\nu),\nu). |  | (3.12) |

Because of the symmetry of the sections, then H ≡ i ​ d H\equiv id under the center conditions.

The planes r = 0 r=0 and ρ = 0 \rho=0 are invariant under the map S S, which hence has the form

 | S ⁡ ( r, ρ) = ( r ​ F ​ ( r, ρ), ρ ​ F − 1 ​ ( r, ρ)), S(r,\rho)=(rF(r,\rho),\rho F^{-1}(r,\rho)), |  | (3.13) |

with F F of class C k C^{k}, since ν = r ​ ρ \nu=r\rho is invariant. Moreover, it is known from [8] that F ⁡ ( 0, 0) = 1 F(0,0)=1 when the sections Σ i \Sigma_{i} are symmetric.

The displacement map then has the form

 | Δ ⁡ ( r, ρ) = ( C 4 ​ ( M) ​ r σ ¯ 4 ​ F σ ¯ 4 ​ ( r, ρ) − H ⁡ ( C 3 ​ ( M) ​ r σ ¯ 3), ν). \Delta(r,\rho)=\left(C_{4}(M)r^{\overline{\sigma}_{4}}F^{\overline{\sigma}_{4}}(r,\rho)-H\left(C_{3}(M)r^{\overline{\sigma}_{3}}\right),\nu\right). |  | (3.14) |

Let V ⁡ ( r, ρ) V(r,\rho) be the first component of Δ \Delta. Then periodic solutions correspond to zeroes of V V.

We now need to compute F F and H H.

Computation of H H.

The map H H is C k C^{k} in ( x ¯ 3, ν) (\overline{x}_{3},\nu). It has the form

 | H ⁡ ( x ¯ 3, ν) = x ¯ 3 + ε 0 ​ ( M) + ε 1 ​ ( M) ​ x ¯ 3 + O ⁡ ( x ¯ 3 2) ​ O G ​ ( M C), H(\overline{x}_{3},\nu)=\overline{x}_{3}+{\varepsilon}_{0}(M)+{\varepsilon}_{1}(M)\overline{x}_{3}+O(\overline{x}_{3}^{2})O_{G}(M_{C}), |  | (3.15) |

with ε 0 ​ ( M) = O P ​ ( M C), ε 1 ​ ( M) = O P ​ ( M C) {\varepsilon}_{0}(M)=O_{P}(M_{C}),{\varepsilon}_{1}(M)=O_{P}(M_{C}).

For μ 2 = μ 3 = μ 4 = 0 \mu_{2}=\mu_{3}=\mu_{4}=0, the system ( 3.2) has the invariant parabola ( 3.4). The term μ 4 ​ x \mu_{4}x in x ˙ \dot{x} is without contact, which yields that

 | ε 0 ( M) = ∗ μ 4 ( 1 + O ( M)) + O ( μ 3) + O ( μ 5) O ( M) = ∗ μ 4 ( 1 + O ( M)) + O ( μ ¯ 3 ν) + O ( μ 5) O ( M), {\varepsilon}_{0}(M)=*\mu_{4}(1+O(M))+O(\mu_{3})+O(\mu_{5})O(M)=*\mu_{4}(1+O(M))+O(\overline{\mu}_{3}\nu)+O(\mu_{5})O(M), |  | (3.16) |

where ∗ *denotes a nonzero constant. Lemma 6.1 in Appendix II shows that the same is true for ( 3.3). Let us again take μ 2 = μ 3 = μ 4 = 0 \mu_{2}=\mu_{3}=\mu_{4}=0. The divergence is then ( 2 ​ B + 1) ​ x + ( 1 − B) ​ μ 5 (2B+1)x+(1-B)\mu_{5}. Proposition 6.2 in the Appendix II shows that

 | ε 1 ( M) = ∗ μ 5 ( 1 + O ( M)) + O ( μ ¯ 3 ν) + O ( μ 4). {\varepsilon}_{1}(M)=*\mu_{5}(1+O(M))+O(\overline{\mu}_{3}\nu)+O(\mu_{4}). |  | (3.17) |

The center ideal. The equations ( 3.16) and ( 3.17) imply that we can take { ε 0, ε 1, μ ¯ 3 } \{{\varepsilon}_{0},{\varepsilon}_{1},\overline{\mu}_{3}\} as generators of the center ideal I C I_{C}.

Computation of F F. The function F F has the form:

 | F ( r, ρ) = 1 + ∗ μ ¯ 3 ρ ( 1 + O ( ρ)) + O ( r) O G ( M C). F(r,\rho)=1+*\overline{\mu}_{3}\rho(1+O(\rho))+O(r)O_{G}(M_{C}). |  | (3.18) |

Indeed, it is proved in Lemma 6.3 in the Appendix that the second derivative of ρ ​ F ​ ( 0, ρ) \rho F(0,\rho) is a nonzero multiple of μ ¯ 3 \overline{\mu}_{3}. Moreover, the blown-up vector field is integrable on r = 0 r=0 for μ ¯ 3 = 0 \overline{\mu}_{3}=0.

Writing the displacement as a finite sum of terms. We need grouping all terms of the displacement map into a finite sum of the form ( 1.2). We will see that three terms are sufficient and show that

 | V ( r, ρ) = − ε 0 ( M) ( 1 + h 0 ( r, ρ)) − C 3 ( M) ε 1 ( M) r σ ¯ 3 ( 1 + h 1 ( r, ρ)) + ∗ μ ¯ 3 r σ ¯ 3 ρ ( 1 + h 2 ( r, ρ)). V(r,\rho)=-{\varepsilon}_{0}(M)(1+h_{0}(r,\rho))-C_{3}(M){\varepsilon}_{1}(M)r^{\overline{\sigma}_{3}}(1+h_{1}(r,\rho))+*\overline{\mu}_{3}r^{\overline{\sigma}_{3}}\rho(1+h_{2}(r,\rho)). |  | (3.19) |

We now explain how to group the different terms.

###### Notation 3.5.

The symbol O ⁡ ( r δ) O(r^{\delta}) used in the sequel, is for an unspecified δ > 0, \delta>0, which may vary from one formula to the other.

Let us first consider the terms coming from H ∘ D 3 H\circ D_{3}. Remember that H H is the identity when we have a center. Moreover, the map H H really takes place in the initial ( x, y) (x,y) -plane, where the center ideal is generated by { ε 0, ε 1, μ 3 } \{{\varepsilon}_{0},{\varepsilon}_{1},\mu_{3}\}. Hence, the higher order terms of H ∘ D 3 H\circ D_{3} are of the form

 | r 2 ​ σ ¯ 3 ​ ( ε 0 ​ ( M) ​ k 0 ​ ( r, ρ) + ε 1 ​ ( M) ​ k 1 ​ ( r, ρ) + μ 3 ​ k 2 ​ ( r, ρ)). r^{2\overline{\sigma}_{3}}\left({\varepsilon}_{0}(M)k_{0}(r,\rho)+{\varepsilon}_{1}(M)k_{1}(r,\rho)+\mu_{3}k_{2}(r,\rho)\right). |  |

The first two terms contribute to h 0 ​ ( r, ρ) h_{0}(r,\rho) and h 1 ​ ( r, ρ), h_{1}(r,\rho), as contributions of order O ⁡ ( r δ). O(r^{\delta}). As for the third term, we use the fact that μ 3 = r ​ ρ ​ μ ¯ 3 \mu_{3}=r\rho\overline{\mu}_{3}. Hence it contributes to h 2 ​ ( r, ρ), h_{2}(r,\rho), also as a term of order O ⁡ ( r δ). O(r^{\delta}). The term C 3 ​ ( M) ​ r σ ¯ 3 C_{3}(M)r^{\overline{\sigma}_{3}} will be later grouped with the corresponding term C 4 ​ ( M) ​ r σ ¯ 4 C_{4}(M)r^{\overline{\sigma}_{4}} coming from D 4 ∘ S. D_{4}\circ S.

Let us now consider the other terms coming from D 4 ∘ S ⁡ ( r, ρ) = C 4 ​ ( M) ​ r σ ¯ 4 ​ F ​ ( r, ρ) σ ¯ 4 D_{4}\circ S(r,\rho)=C_{4}(M)r^{\overline{\sigma}_{4}}F(r,\rho)^{\overline{\sigma}_{4}}. Again we use that F F is the identity when there is a center, i.e. all its terms are divisible in the ideal I C I_{C}. One of them is the term ∗ μ ¯ 3 ​ r σ ¯ 4 ​ ρ *\overline{\mu}_{3}r^{\overline{\sigma}_{4}}\rho coming from the term ∗ μ ¯ 3 ​ ρ *\overline{\mu}_{3}\rho of F F. As mentioned above, all higher order terms r σ ¯ 4 ​ o ​ ( ρ) r^{\overline{\sigma}_{4}}o(\rho) have coefficients divisible by μ ¯ 3 \overline{\mu}_{3}. Also, all terms in r σ ¯ 4 ​ ρ ​ O ​ ( r) r^{\overline{\sigma}_{4}}\rho O(r) can be distributed in h 0 h_{0}, h 1 h_{1} and h 2, h_{2}, as terms of order O ⁡ ( r δ) O(r^{\delta}). Hence, we only need to consider the pure terms in o ⁡ ( r σ ¯ 4) o(r^{\overline{\sigma}_{4}}). It suffices to show that all such terms can be divided in { ε 0, ε 1 } \{{\varepsilon}_{0},{\varepsilon}_{1}\}. This comes from the fact that the computation of the pure terms in r r can be done in the plane ρ = 0 \rho=0, and that the system restricted to this plane does not contain any term in μ ¯ 3 \overline{\mu}_{3}. Since

 | σ ¯ 4 − σ ¯ 3 = ν ​ O P ​ ( M C) ​ f ​ ( ν) = r ​ ρ ​ O P ​ ( M C) ​ f ​ ( ν), \overline{\sigma}_{4}-\overline{\sigma}_{3}=\nu O_{P}(M_{C})f(\nu)=r\rho O_{P}(M_{C})f(\nu), |  | (3.20) |

with f f of class C k C^{k}, we can replace everywhere σ ¯ 4 \overline{\sigma}_{4} by σ ¯ 3, \overline{\sigma}_{3}, up to terms of order O ⁡ ( r δ), O(r^{\delta}), distributed in h 0, h 1 h_{0},h_{1} and h 2. h_{2}.

We are left with the terms C 3 ​ ( M) ​ r σ ¯ 3 − C 4 ​ ( M) ​ r σ ¯ 4 C_{3}(M)r^{\overline{\sigma}_{3}}-C_{4}(M)r^{\overline{\sigma}_{4}}. We write this as

 | C 3 ​ ( M) ​ r σ ¯ 3 − C 4 ​ ( M) ​ r σ ¯ 4 = ( C 3 ​ ( M) − C 4 ​ ( M)) ​ r σ ¯ 3 + C 4 ​ ( M) ​ ( r σ ¯ 3 − r σ ¯ 4) = ( C 3 ​ ( M) − C 4 ​ ( M)) ​ r σ ¯ 3 + C 4 ​ ( M) ​ ( σ ¯ 3 − σ ¯ 4) ​ r σ ¯ 3 ​ ω ​ ( r, σ ¯ 3 − σ ¯ 4). \displaystyle\begin{split}C_{3}(M)r^{\overline{\sigma}_{3}}-C_{4}(M)r^{\overline{\sigma}_{4}}&=(C_{3}(M)-C_{4}(M))r^{\overline{\sigma}_{3}}+C_{4}(M)(r^{\overline{\sigma}_{3}}-r^{\overline{\sigma}_{4}})\\ &=(C_{3}(M)-C_{4}(M))r^{\overline{\sigma}_{3}}+C_{4}(M)(\overline{\sigma}_{3}-\overline{\sigma}_{4})r^{\overline{\sigma}_{3}}\omega(r,\overline{\sigma}_{3}-\overline{\sigma}_{4}).\end{split} |  | (3.21) |

The difference C 3 ​ ( M) − C 4 ​ ( M) C_{3}(M)-C_{4}(M) is X 0 ​ r 0 − σ ¯ 3 ​ ( 1 − r 0 σ ¯ 3 − σ ¯ 4) X_{0}r_{0}^{-\overline{\sigma}_{3}}(1-r_{0}^{\overline{\sigma}_{3}-\overline{\sigma}_{4}}). Using ( 3.20), the two terms can be decomposed in sums of terms contributing to h 0, h 1, h 2 h_{0},h_{1},h_{2}, as terms of order O ⁡ ( r δ). O(r^{\delta}).

Finite cyclicity in the case σ 0 \sigma_{0} irrational. The displacement map V V in ( 3.19) is a special case of a universal family

 | a 0 ​ ( 1 + h 0 ​ ( r, ρ)) + a 1 ​ r σ ¯ 3 ​ ( 1 + h 1 ​ ( r, ρ)) + a 2 ​ r σ ¯ 3 ​ ρ ​ ( 1 + h 2 ​ ( r, ρ)), a_{0}(1+h_{0}(r,\rho))+a_{1}r^{\overline{\sigma}_{3}}(1+h_{1}(r,\rho))+a_{2}r^{\overline{\sigma}_{3}}\rho(1+h_{2}(r,\rho)), |  | (3.22) |

with h 0, h 1 h_{0},h_{1} of order O ⁡ ( r δ) O(r^{\delta}) and h 2 h_{2} is of order O ⁡ ( ρ) + O ⁡ ( r δ). O(\rho)+O(r^{\delta}). Using that these three functions are of order o ⁡ ( 1), o(1), we show in Theorem 5.8 below that this family has at most two small zeros along any curve r ​ ρ = Cst r\rho=\mathrm{Cst} for r, ρ < δ r,\rho<\delta for some small δ \delta. This implies that, either V V has at most two small zeros, or V V is identically zero, in which case we have a center.

Adjustment of the proof when σ 0 = p q \sigma_{0}=\frac{p}{q} with q > 1 q>1. The adjustments are minimal. Indeed, the formula of the Dulac map is more complicated:

 | D i ​ ( r, ρ) = ( r σ ¯ ​ ( C i ​ ( M) + ϕ ⁡ ( r, ρ)), r ​ ρ), D_{i}(r,\rho)=(r^{\overline{\sigma}}(C_{i}(M)+\phi(r,\rho)),r\rho), |  | (3.23) |

with ϕ ⁡ ( r, ρ) \phi(r,\rho) as in Theorem 2.3. Hence ϕ ⁡ ( r, ρ) \phi(r,\rho) produces in V V new terms of order O ⁡ ( r δ), O(r^{\delta}), distributed in h 0, h 1, h 2. h_{0},h_{1},h_{2}.

Adjustement of the proof when σ 0 = p \sigma_{0}=p. Here the first component of D i ​ ( r, ρ) D_{i}(r,\rho) has an additional term of the form

 | κ i ​ ( r, ρ) = η i ​ ( ν) ​ ρ p ​ r σ ¯ i ​ ω ​ ( r r 0, σ ¯ i − p). \kappa_{i}(r,\rho)=\eta_{i}(\nu)\rho^{p}r^{\overline{\sigma}_{i}}\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{i}-p\right). |  |

All higher order terms can be distributed in h 0, h 1, h 2 h_{0},h_{1},h_{2} and we need only consider the term E ~ = κ 4 ∘ S − ( 1 + ε 1 ​ ( M)) ​ κ 3 = ( κ 4 ∘ S − κ 4) + E \tilde{E}=\kappa_{4}\circ S-(1+{\varepsilon}_{1}(M))\kappa_{3}=\left(\kappa_{4}\circ S-\kappa_{4}\right)+E with E = κ 4 ​ ( r, ρ) − ( 1 + ε 1 ​ ( M)) ​ κ 3 ​ ( r, ρ) E=\kappa_{4}(r,\rho)-(1+{\varepsilon}_{1}(M))\kappa_{3}(r,\rho).

1. 1.

We consider first the term κ 4 ∘ S − κ 4. \kappa_{4}\circ S-\kappa_{4}. Let β = σ ¯ 4 − p \beta=\overline{\sigma}_{4}-p. We have that

 | κ 4 ​ ( r ​ F) − κ 4 ​ ( r) = η 4 ​ ν p ​ r β ​ [F β ​ ω β ​ ( F ​ r r 0) − ω β ​ ( r r 0)] ⏟ G ⁡ ( r, ρ). \kappa_{4}(rF)-\kappa_{4}(r)=\eta_{4}\nu^{p}r^{\beta}\underbrace{\Big[F^{\beta}\omega_{\beta}\Big(\frac{Fr}{r_{0}}\Big)-\omega_{\beta}\Big(\frac{r}{r_{0}}\Big)\Big]}_{G(r,\rho)}. |  |

Let us consider G ⁡ ( r, ρ) G(r,\rho):

 | G ⁡ ( r, ρ) = F β ​ ( ω β ​ ( F ​ r r 0) − ω β ​ ( r r 0)) + ( F β − 1) ​ ω β ​ ( r r 0). G(r,\rho)=F^{\beta}\Big(\omega_{\beta}\Big(\frac{Fr}{r_{0}}\Big)-\omega_{\beta}\Big(\frac{r}{r_{0}}\Big)\Big)+(F^{\beta}-1)\omega_{\beta}\Big(\frac{r}{r_{0}}\Big). |  |

Since

 | ω β ​ ( F ​ r r 0) − ω β ​ ( r r 0) = ( r r 0) − β ​ F − β − 1 β, \omega_{\beta}\Big(\frac{Fr}{r_{0}}\Big)-\omega_{\beta}\Big(\frac{r}{r_{0}}\Big)=\Big(\frac{r}{r_{0}}\Big)^{-\beta}\frac{F^{-\beta}-1}{\beta}, |  |

we obtain that

 | G ⁡ ( r, ρ) = − F β − 1 β ​ ( r r 0) − β + ( F β − 1) ​ ω β ​ ( r r 0) = F β − 1 β ​ ( − ( r r 0) − β + β ​ ω β ​ ( r r 0)), G(r,\rho)=-\frac{F^{\beta}-1}{\beta}\Big(\frac{r}{r_{0}}\Big)^{-\beta}+(F^{\beta}-1)\omega_{\beta}\Big(\frac{r}{r_{0}}\Big)=\frac{F^{\beta}-1}{\beta}\Big(-\Big(\frac{r}{r_{0}}\Big)^{-\beta}+\beta\omega_{\beta}\Big(\frac{r}{r_{0}}\Big)\Big), |  |

i.e. G ⁡ ( r, ρ) = − F β − 1 β G(r,\rho)=-\frac{F^{\beta}-1}{\beta}, and then κ 4 ​ ( r ​ F) − κ 4 ​ ( r) = − η 4 ​ ν p ​ r β ​ F β − 1 β. \kappa_{4}(rF)-\kappa_{4}(r)=-\eta_{4}\nu^{p}r^{\beta}\frac{F^{\beta}-1}{\beta}.

As F = 1 + ∗ μ ¯ 3 ρ ( 1 + ρ g ¯ ( ρ)) + r O G ( M C), F=1+*\bar{\mu}_{3}\rho(1+\rho\bar{g}(\rho))+rO_{G}(M_{C}), we have that

 | F β − 1 β = ∗ μ ¯ 3 ρ ( 1 + ρ g ¯ ( ρ)) + r O G ( M C), \frac{F^{\beta}-1}{\beta}=*\bar{\mu}_{3}\rho(1+\rho\bar{g}(\rho))+rO_{G}(M_{C}), |  |

and then that

 | κ 4 ( r F) − κ 4 ( r) = − η 4 ν p r β ( ∗ μ ¯ 3 ρ ( 1 + ρ g ( ρ)) + r O G ( M C)). \kappa_{4}(rF)-\kappa_{4}(r)=-\eta_{4}\nu^{p}r^{\beta}(*\bar{\mu}_{3}\rho(1+\rho g(\rho))+rO_{G}(M_{C})). |  |

The term OPEN r ​ O G ​ ( M C)) rO_{G}(M_{C})) gives contributions of order O ⁡ ( r δ) O(r^{\delta}) in h 0, h 1, h 2. h_{0},h_{1},h_{2}. Next, the term ∗ μ ¯ 3 ​ ρ ​ ( 1 + ρ ​ g ¯ ​ ( ρ)) *\bar{\mu}_{3}\rho(1+\rho\bar{g}(\rho)) gives the contribution − ∗ η 4 ν p − 1 ρ ( 1 + ρ g ¯ ( ρ)) -*\eta_{4}\nu^{p-1}\rho(1+\rho\bar{g}(\rho)) in h 2. h_{2}. If p ≥ 2, p\geq 2, this term is also of order O ⁡ ( r ​ ρ), O(r\rho), and it is of order O ⁡ ( ρ) O(\rho) if p = 1. p=1.

2. 2.

We consider now:

 | E = ρ p [( η 4 ( ν) − η 3 ( ν) ( 1 + ε 1 ( M)) r σ ¯ 3 ω ( r r 0, σ ¯ 3 − p) + η 4 ​ ( ν) ​ ( r σ ¯ 4 − r σ ¯ 3) ​ ω ​ ( r r 0, σ ¯ 3 − p) + η 4 ( ν) r σ ¯ 4 ( ω ( r r 0, σ ¯ 3 − p) − ω ( r r 0, σ ¯ 4 − p))]. \displaystyle\begin{split}E&=\rho^{p}\left[\left(\eta_{4}(\nu)-\eta_{3}(\nu)(1+{\varepsilon}_{1}(M)\right)r^{\overline{\sigma}_{3}}\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p\right)\right.\\ &\qquad+\eta_{4}(\nu)\left(r^{\overline{\sigma}_{4}}-r^{\overline{\sigma}_{3}}\right)\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p\right)\\ &\qquad\left.+\eta_{4}(\nu)r^{\overline{\sigma}_{4}}\left(\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p\right)-\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{4}-p\right)\right)\right].\end{split} |  |

The second term in the bracket is of the form

 | η 4 ​ ( ν) ​ ( σ ¯ 3 − σ ¯ 4) ​ r σ ¯ 3 ​ ω ​ ( r, σ ¯ 3 − σ ¯ 4) ​ ω ​ ( r r 0, σ ¯ 3 − p). \eta_{4}(\nu)(\overline{\sigma}_{3}-\overline{\sigma}_{4})r^{\overline{\sigma}_{3}}\omega(r,\overline{\sigma}_{3}-\overline{\sigma}_{4})\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p\right). |  |

Using ( 3.20), this term can be distributed in h 0, h 1, h 2, h_{0},h_{1},h_{2}, as terms of order O ⁡ ( r δ). O(r^{\delta}). A similar argument holds for the third term. Indeed, we introduce a compensator

 | Ω ⁡ ( ξ, α, β) = Ω α, β ​ ( ξ) = { ω ⁡ ( ξ, α) − ω ⁡ ( ξ, β) α − β, α ≠ β, 1 2 ​ ( ln ⁡ ξ) 2, α = β, \Omega(\xi,\alpha,\beta)=\Omega_{\alpha,\beta}(\xi)=\begin{cases}\frac{\omega(\xi,\alpha)-\omega(\xi,\beta)}{\alpha-\beta},&\alpha\neq\beta,\\ \frac{1}{2}(\ln\xi)^{2},&\alpha=\beta,\end{cases} |  | (3.24) |

allowing to rewrite this term as

 | η 4 ​ ( ν) ​ r σ ¯ 4 ​ ( σ ¯ 3 − σ ¯ 4) ​ Ω ​ ( r r 0, σ ¯ 3 − p, σ ¯ 4 − p). \eta_{4}(\nu)r^{\overline{\sigma}_{4}}(\overline{\sigma}_{3}-\overline{\sigma}_{4})\Omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p,\overline{\sigma}_{4}-p\right). |  |

Again, using ( 3.20), this term can be distributed in h 0, h 1, h 2, h_{0},h_{1},h_{2}, as terms of order O ⁡ ( r δ) O(r^{\delta}).

This allows writing the displacement map as a sum of four terms

 | V ⁡ ( r, ρ) = − ε 0 ​ ( M) ​ ( 1 + h 0 ​ ( r, ρ)) − C 3 ​ ( M) ​ ε 1 ​ ( M) ​ r σ ¯ 3 ​ ( 1 + h 1 ​ ( r, ρ)) + ∗ μ ¯ 3 r σ ¯ 3 ρ ( 1 + h 2 ( r, ρ)) + K ( M) r σ ¯ 3 ρ p ω ( r r 0, σ ¯ 3 − p), \displaystyle\begin{split}V(r,\rho)&=-{\varepsilon}_{0}(M)(1+h_{0}(r,\rho))-C_{3}(M){\varepsilon}_{1}(M)r^{\overline{\sigma}_{3}}(1+h_{1}(r,\rho))\\ &\qquad+*\overline{\mu}_{3}r^{\overline{\sigma}_{3}}\rho(1+h_{2}(r,\rho))+K(M)r^{\overline{\sigma}_{3}}\rho^{p}\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p\right),\end{split} |  | (3.25) |

with h 0, h 1 h_{0},h_{1} of order O ⁡ ( r δ). O(r^{\delta}). Moreover, K ⁡ ( M) = η 4 ​ ( ν) − η 3 ​ ( ν) ​ ( 1 − ε 1 ​ ( M)) = O P ​ ( M C) K(M)=\eta_{4}(\nu)-\eta_{3}(\nu)(1-{\varepsilon}_{1}(M))=O_{P}(M_{C}). For p ≥ 2 p\geq 2, we conclude that the cyclicity is at most 3 3 by Theorem 5.12.

For p = 1 p=1, we will prove in Theorem 5.13 that the cyclicity is at most 2. 2. To this end, we will use that η 4 ​ ( 0) = − η 3 ​ ( 0) = μ ¯ 3 \eta_{4}(0)=-\eta_{3}(0)=\overline{\mu}_{3} and then that K ( M) = ∗ μ ¯ 3 + O ( ν) O P ( M C), K(M)=*\overline{\mu}_{3}+O(\nu)O_{P}(M_{C}), in order to rewrite V V as:

 | V ⁡ ( r, ρ) = − ε 0 ​ ( M) ​ ( 1 + h 0 ​ ( r, ρ)) − C 3 ​ ( M) ​ ε 1 ​ ( M) ​ r σ ¯ 3 ​ ( 1 + h 1 ​ ( r, ρ)) + ∗ μ ¯ 3 r σ ¯ 3 ρ ( 1 + h 2 ( r, ρ)) + ∗ μ ¯ 3 r σ ¯ 3 ρ ω ( r r 0, σ ¯ 3 − p) ( 1 + h 3 ( r, ρ)), \displaystyle\begin{split}V(r,\rho)&=-{\varepsilon}_{0}(M)(1+h_{0}(r,\rho))-C_{3}(M){\varepsilon}_{1}(M)r^{\overline{\sigma}_{3}}(1+h_{1}(r,\rho))\\ &+*\overline{\mu}_{3}r^{\overline{\sigma}_{3}}\rho(1+h_{2}(r,\rho))+*\overline{\mu}_{3}r^{\overline{\sigma}_{3}}\rho\omega\left(\frac{r}{r_{0}},\overline{\sigma}_{3}-p\right)(1+h_{3}(r,\rho)),\end{split} |  | (3.26) |

with h 0, h 1 h_{0},h_{1} and h 3 h_{3} of order O ⁡ ( r δ). O(r^{\delta}). ∎

### 3.3 Finite cyclicity of the boundary limit periodic sets of ( H 13 3) (H_{13}^{3})

###### Theorem 3.6.

The boundary limit periodic set of ( H 13 3) (H_{13}^{3}) (see Figures 1 (c) and 5) has finite cyclicity.

Figure 5: The boundary graphic through P 1 P_{1} and P 2 P_{2} and the four sections Σ i \Sigma_{i} and Π i \Pi_{i}, i = 1, 2 i=1,2, in the normalizing coordinates.

###### Proof.

The proof is very similar to that of Theorem 3.3. The graphic occurs in the family ( 3.1) for B < 1 2 B<\frac{1}{2}, which corresponds to 1 2 < a < 1 \frac{1}{2}<a<1, but we prefer to use the following equivalent unfolding inside quadratic systems (only parameters’ names are changed so that they play similar role as in Theorem 3.3)

 | { x ˙ = − y + B ​ x 2 + μ 2 ​ y 2 + μ 5 ​ x y ˙ = x + x ​ y + μ 3 ​ y 2 + μ 4 ​ y. \left\{\begin{array}[]{ll}\dot{x}&=-y+Bx^{2}+\mu_{2}y^{2}+\mu_{5}x\\ \dot{y}&=x+xy+\mu_{3}y^{2}+\mu_{4}y.\end{array}\right. |  | (3.27) |

The point P 4 P_{4} (resp. P 3 P_{3}) is replaced by P 1 P_{1} (resp. P 2 P_{2}). The quantity σ i \sigma_{i} is now given by σ i = 2 ​ a − 1 a \sigma_{i}=\frac{2a-1}{a}. The main difference with Theorem 3.3 is that the transition from Π 2 \Pi_{2} to Π 1 \Pi_{1} is replaced by the composition T r − 1 ∘ D r − 1 ∘ T ∘ D ℓ ∘ T ℓ T_{r}^{-1}\circ D_{r}^{-1}\circ T\circ D_{\ell}\circ T_{\ell}. The transitions T ℓ T_{\ell} and T r T_{r} are along the equator of the Poincaré sphere and hence preserve the connection (no translation terms). The saddle points P ℓ P_{\ell} and P r P_{r} have inverse hyperbolicity ratios: τ ℓ = 1 / τ r = 1 − B B < 1 \tau_{\ell}=1/\tau_{r}=\frac{1-B}{B}<1. Hence, it is better to consider a displacement map

 | V: Σ 2 → Π r, V = T ∘ D ℓ ∘ T ℓ ∘ D 2 − D r ∘ T r ∘ D 1 ∘ S. V:\Sigma_{2}\rightarrow\Pi_{r},\qquad V=T\circ D_{\ell}\circ T_{\ell}\circ D_{2}-D_{r}\circ T_{r}\circ D_{1}\circ S. |  | (3.28) |

The computation of S S is the same as before.

Computation of T ℓ T_{\ell} and T r T_{r}. T r T_{r} and T ℓ T_{\ell} are regular C k C^{k} -transitions with no translation terms. They can be computed in the coordinates ( v, w) = ( − x y, 1 y) (v,w)=(-\frac{x}{y},\frac{1}{y}). The transformed system in these coordinates is given in ( 6.1). The transitions take place along w = 0 w=0. Along this line, div = ( 3 − 2 ​ B) ​ v − 2 ​ μ 3 \mathrm{div}=(3-2B)v-2\mu_{3}. Hence T r ′ ​ ( 0) − T ℓ ′ ​ ( 0) = O ⁡ ( μ 3) = ν ​ O ​ ( μ ¯ 3) T_{r}^{\prime}(0)-T_{\ell}^{\prime}(0)=O(\mu_{3})=\nu O(\overline{\mu}_{3}). This property is preserved in the normalizing coordinates.

Computation of T T. The transition T T in studied in ( 3.2). The line y = − 1 y=-1 is invariant under μ 3 = μ 4 \mu_{3}=\mu_{4}. Hence, the constant term is of the form

 | T ( 0) = ε 0 ( M) = ∗ ( μ 4 − ν μ ¯ 3). T(0)={\varepsilon}_{0}(M)=*(\mu_{4}-\nu\overline{\mu}_{3}). |  | (3.29) |

Under the condition ε 0 = 0 {\varepsilon}_{0}=0, we have div | y = − 1 = ( 2 ​ B + 1) ​ x + μ 5 − ν ​ μ ¯ 3 \mathrm{div}|_{y=-1}=(2B+1)x+\mu_{5}-\nu\overline{\mu}_{3}. Hence,

 | T ′ ( 0) = ε 1 ( M) = ∗ μ 5 + O ( μ 4) + O ( ν) O ( μ ¯ 3). T^{\prime}(0)={\varepsilon}_{1}(M)=*\mu_{5}+O(\mu_{4})+O(\nu)O(\overline{\mu}_{3}). |  | (3.30) |

The equations ( 3.29) and ( 3.30) remain valid in the normalizing coordinates, and we call the corresponding coefficients ε ~ 0 \tilde{{\varepsilon}}_{0} and ε ~ 1 \tilde{{\varepsilon}}_{1}.

The Dulac maps D ℓ D_{\ell} and D r D_{r}. We first localize the system ( 3.27) using coordinates ( u, z) = ( y x, 1 x) (u,z)=(\frac{y}{x},\frac{1}{x}). The normalizing coordinates are of the form ( u ¯ i, z) (\overline{u}_{i},z), i ∈ { ℓ, r } i\in\{\ell,r\}. Then,

 | D i ​ ( z) = { C i ​ ( M) ​ z τ ℓ, 1 − B 0 B 0 ∉ ℚ, C i ​ ( M) ​ z τ ℓ ​ ( 1 + ζ ⁡ ( z, M)), 1 − B 0 B 0 ∈ ℚ, D_{i}(z)=\begin{cases}C_{i}(M)z^{\tau_{\ell}},&\frac{1-B_{0}}{B_{0}}\notin\mathbb{Q},\\ C_{i}(M)z^{\tau_{\ell}}(1+\zeta(z,M)),&\frac{1-B_{0}}{B_{0}}\in\mathbb{Q},\end{cases} |  | (3.31) |

with ζ \zeta, a 𝒞 k {\mathcal{C}}^{k} -function on monomials (see Appendix II).

The Dulac maps D 1 D_{1} and D 2 D_{2}. They are given in Theorem 2.2. Since the connection along the equator is fixed, then the coefficient η i \eta_{i} vanishes identically when σ 0 ∈ ℕ \sigma_{0}\in\mathbb{N}.

Hence, the displacement map V ⁡ ( r, ρ) V(r,\rho) has the form

 | V ( r, ρ) = ε ~ 0 ( 1 + h 0 ( r, ρ)) + ∗ ε ~ 1 r σ ¯ 2 + τ ℓ ( 1 + h 1 ( r, ρ)) − ∗ μ ¯ 3 r σ ¯ 2 + τ ℓ ρ ( 1 + h 2 ( r, ρ)). V(r,\rho)=\tilde{{\varepsilon}}_{0}(1+h_{0}(r,\rho))+*\tilde{{\varepsilon}}_{1}r^{\overline{\sigma}_{2}+\tau_{\ell}}(1+h_{1}(r,\rho))-*\overline{\mu}_{3}r^{\overline{\sigma}_{2}+\tau_{\ell}}\rho(1+h_{2}(r,\rho)). |  | (3.32) |

This equation contains no resonant monomials since σ ¯ 2 + τ ℓ = 1 − B − B 2 B ⁡ ( 1 − B) ≠ 1 \overline{\sigma}_{2}+\tau_{\ell}=\frac{1-B-B^{2}}{B(1-B)}\neq 1 as soon as B ≠ 1 2 B\neq\frac{1}{2}. We conclude that the cyclicity is at most two by Theorem 5.8. ∎

### 3.4 Finite cyclicity of ( I 14 1) (I_{14}^{1})

We now prove Theorem 1.2, i.e. that the graphic ( I 14 1) (I_{14}^{1}) has finite cyclicity inside quadratic systems (see Figure 1 (a)).

Proof of Theorem 1.2. Such a graphic occurs for system ( 3.1) when B 0 > 1 B_{0}>1, and its deformation in quadratic systems is given in ( 3.2). As usual, we should normally consider all limit periodic sets of Table 2. It was shown in [8] that a graphic through a nilpotent saddle point has finite cyclicity inside any C ∞ C^{\infty} -unfolding under the generic conditions that the return map P P along the graphic has a derivative different from one and that the nilpotent saddle point has codimension 3. But the only limit periodic sets of Table 2 for which we use the genericity hypotheses are the boundary limit periodic sets which have been treated in Theorem 3.3, and the intermediate and lower limit periodic sets of Sxhh1 and Sxhh5.

For these limit periodic sets, we only have Dulac maps of the first type as in Theorem 2.2. Hence, we can work with a 1-dimensional displacement map, which we take as V: Σ 3 ⟶ Π 4 V:\Sigma_{3}\longrightarrow\Pi_{4}, V = D 4 ∘ S − T ∘ D 3 V=D_{4}\circ S-T\circ D_{3} (see figure 6). As before the sections Σ i \Sigma_{i} and Π i \Pi_{i} are parameterized by the normalizing coordinate x ¯ i \overline{x}_{i} near P i P_{i}, which are chosen so that S S and T T are the identity in the center case.

Figure 6: Intermediate and lower limit periodic sets of Sxhh1 and Sxhh5: the four sections Σ i \Sigma_{i} and Π i \Pi_{i}, i = 3, 4 i=3,4, in the normalizing coordinates near P 3 P_{3} and P 4 P_{4}.

The technique is to write V V in the form of a finite sum

 | V ⁡ ( x ¯ 3, μ) = ϵ ~ 0 + ν σ ¯ ​ ( ∑ i = 1 n ε ~ i ​ h i ​ ( x ¯ 3, μ)), V(\overline{x}_{3},\mu)=\tilde{\epsilon}_{0}+\nu^{\overline{\sigma}}\left(\sum_{i=1}^{n}\tilde{{\varepsilon}}_{i}h_{i}(\overline{x}_{3},\mu)\right), |  | (3.33) |

for some σ ¯ > 0 \overline{\sigma}>0. The parameters are the same as in ( 3.9) and ( 3.10). We write little details since they are very similar to [7].

The intermediate graphics. For these graphics, the map V ⁡ ( x ¯ 3, μ) V(\overline{x}_{3},\mu) is C k C^{k} in x ¯ 3 \overline{x}_{3}. Under the condition μ 2 = μ 3 = 0 \mu_{2}=\mu_{3}=0 for a nilpotent saddle, ( 3.2) has an invariant parabola for μ 4 = 0 \mu_{4}=0, which is the only possible connection at a nilpotent saddle. Hence, T T has a constant term of the form ∗ μ 4 + O ⁡ ( μ 3) + μ 5 ​ O ​ ( M) *\mu_{4}+O(\mu_{3})+\mu_{5}O(M). The constant term of the transition S S has the form O ⁡ ( μ ¯ 3) O(\overline{\mu}_{3}) since μ ¯ 2 \overline{\mu}_{2} respects the symmetry, and hence does not contribute to the breaking of the connection.

When σ 0 ∉ ℕ \sigma_{0}\notin\mathbb{N}, this yields that the constant term ε ~ 0 \tilde{{\varepsilon}}_{0} in the displacement map has the form ε ~ 0 = ∗ μ 4 + O ( ν) O ( μ ¯ 3) + μ 5 O ( M). \tilde{{\varepsilon}}_{0}=*\mu_{4}+O(\nu)O(\overline{\mu}_{3})+\mu_{5}O(M).

When σ 0 = p ∈ ℕ \sigma_{0}=p\in\mathbb{N}, there are additional terms

 | η 3 ​ ρ 0 p ​ ( ν ν 0) σ ¯ 3 ​ ω ​ ( ν ν 0, α 3) − η 4 ​ ρ 0 p ​ ( ν ν 0) σ ¯ 4 ​ ω ​ ( ν ν 0, α 4) = ( η 3 − η 4) ​ ρ 0 p ​ ( ν ν 0) σ ¯ 3 ​ ω ​ ( ν ν 0, α 3) + η 4 ​ ( α 3 − α 4) ​ ρ 0 p ​ ( ν ν 0) σ ¯ 3 ​ ω ​ ( ν ν 0, α 3 − α 4) ​ ω ​ ( ν ν 0, α 3) + η 4 ​ ( α 3 − α 4) ​ ρ 0 p ​ ( ν ν 0) σ ¯ 4 ​ Ω ​ ( ν ν 0, α 3, α 4). \displaystyle\begin{split}&\eta_{3}\rho_{0}^{p}\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}\omega\left(\frac{\nu}{\nu_{0}},\alpha_{3}\right)-\eta_{4}\rho_{0}^{p}\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{4}}\omega\left(\frac{\nu}{\nu_{0}},\alpha_{4}\right)\\ &\qquad=(\eta_{3}-\eta_{4})\rho_{0}^{p}\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}\omega\left(\frac{\nu}{\nu_{0}},\alpha_{3}\right)\\ &\qquad\qquad+\eta_{4}(\alpha_{3}-\alpha_{4})\rho_{0}^{p}\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{3}}\omega\left(\frac{\nu}{\nu_{0}},\alpha_{3}-\alpha_{4}\right)\omega\left(\frac{\nu}{\nu_{0}},\alpha_{3}\right)\\ &\qquad\qquad+\eta_{4}(\alpha_{3}-\alpha_{4})\rho_{0}^{p}\left(\frac{\nu}{\nu_{0}}\right)^{\overline{\sigma}_{4}}\Omega\left(\frac{\nu}{\nu_{0}},\alpha_{3},\alpha_{4}\right).\end{split} |  | (3.34) |

In this expression η 3 − η 4 = O P ​ ( M C) \eta_{3}-\eta_{4}=O_{P}(M_{C}) and α 3 − α 4 = O P ​ ( M C) ​ O ​ ( ν) \alpha_{3}-\alpha_{4}=O_{P}(M_{C})O(\nu). Hence, in all cases we have

 | ε ~ 0 = ∗ μ 4 + O ( ν) O ( μ ¯ 3) + μ 5 O ( M) + O ( ν) O P ( M C). \tilde{{\varepsilon}}_{0}=*\mu_{4}+O(\nu)O(\overline{\mu}_{3})+\mu_{5}O(M)+O(\nu)O_{P}(M_{C}). |  | (3.35) |

The linear term has the form OPEN ν σ ¯ 3 ​ T ′ ​ ( 0) − ν σ ¯ 4 ​ S ′ ​ ( 0)) \nu^{\overline{\sigma}_{3}}T^{\prime}(0)-\nu^{\overline{\sigma}_{4}}S^{\prime}(0)). Moreover, S ′ ​ ( 0) | ρ = 0 ≡ 1 S^{\prime}(0)|_{\rho=0}\equiv 1 precisely when μ ¯ 3 = 0 \overline{\mu}_{3}=0. Also, Lemma 6.2 shows that T ′ ( 0) − 1 = ∗ μ 5 + O ( μ 4) + O ( μ 3) T^{\prime}(0)-1=*\mu_{5}+O(\mu_{4})+O(\mu_{3}). Considering that σ ¯ 3 − σ ¯ 4 = O ⁡ ( ν) \overline{\sigma}_{3}-\overline{\sigma}_{4}=O(\nu), then

 | ν σ ¯ 4 = ν σ ¯ 3 ​ ( 1 + ( σ ¯ 3 − σ ¯ 4) ​ ω ​ ( ν, σ ¯ 3 − σ ¯ 4) = ν σ ¯ 3 ​ ( 1 + O ⁡ ( ν)) CLOSE. \nu^{\overline{\sigma}_{4}}=\nu^{\overline{\sigma}_{3}}(1+(\overline{\sigma}_{3}-\overline{\sigma}_{4})\omega(\nu,\overline{\sigma}_{3}-\overline{\sigma}_{4})=\nu^{\overline{\sigma}_{3}}(1+O(\nu)). |  |

This yields

 | ε ~ 1 = ν σ ¯ 3 ( ∗ μ 5 + O ( μ 4) + O ( ν) O ( μ ¯ 3)). \tilde{{\varepsilon}}_{1}=\nu^{\overline{\sigma}_{3}}\left(*\mu_{5}+O(\mu_{4})+O(\nu)O(\overline{\mu}_{3})\right). |  | (3.36) |

Now, because of the funneling effect, any nonlinearity on the side of T T has a high coefficient in ν \nu which damps it. Hence, the only significant nonlinearities are on the side of S S. We are sure that S S is nonlinear when μ ¯ 3 ≠ 0 \overline{\mu}_{3}\neq 0. This comes from the fact that the graphic belongs to a family of graphics. In the case of Sxhh1, this family ends in a lower graphic with a saddle point and its hyperbolicity ratio τ \tau is different from 1 1 precisely when μ ¯ 3 ≠ 0 \overline{\mu}_{3}\neq 0, yielding that S ⁡ ( x ¯ 3) = C 0 + C 1 ​ x ¯ 3 τ + o ⁡ ( x ¯ 3 τ), S(\overline{x}_{3})=C_{0}+C_{1}\overline{x}_{3}^{\tau}+o(\overline{x}_{3}^{\tau}), with C 1 ≠ 0, C_{1}\not=0, for graphics near the saddle point, and hence that S S is nonlinear on the whole section Σ 3 \Sigma_{3}. Then, for any graphic occuring for a value x ¯ 3, 0 \overline{x}_{3,0}, there exists n n such that S ( n) ​ ( x ¯ 3) = c n, 3 ​ μ ¯ 3 ≠ 0 S^{(n)}(\overline{x}_{3})=c_{n,3}\overline{\mu}_{3}\neq 0. Hence, V ( n) ​ ( x ¯ 3, 0) = ν σ ¯ 4 ​ [c n, 3 ​ μ ¯ 3 + O ⁡ ( ν) ​ O P ​ ( M C)] = ε ~ n V^{(n)}(\overline{x}_{3,0})=\nu^{\overline{\sigma}_{4}}\left[c_{n,3}\overline{\mu}_{3}+O(\nu)O_{P}(M_{C})\right]=\tilde{{\varepsilon}}_{n}. Moreover, for all graphics except a few isolated ones we have that n = 2 n=2. The same argument can be applied for Sxhh5 since the connection is fixed between the two saddles and the product of their hyperbolicity ratios is different from 1 1 precisely when μ 3 ≠ 0 \mu_{3}\neq 0. Hence, we have written V V under the form ( 3.33) with h i ​ ( x ¯ 3) = x ¯ 3 i ​ ( 1 + O ⁡ ( x ¯ 3)) h_{i}(\overline{x}_{3})=\overline{x}_{3}^{i}(1+O(\overline{x}_{3})). We conclude to finite cyclicity by means of Theorem 5.8.

The lower graphic of Sxhh1. The study is very similar and divided in two cases. When μ ¯ 3 ≠ 0 \overline{\mu}_{3}\neq 0, it was already shown in [8] that the lower graphic of Sxhh1 has finite cyclicity. This comes from the fact that the hyperbolicity ratio τ \tau at the saddle point is non equal to 1 1 precisely when μ ¯ 3 ≠ 0 \overline{\mu}_{3}\neq 0, in which case we conclude to finite cyclicity because of the nonlinearity of S S. Hence the difficult case is the neighborhood of μ ¯ 3 = 0 \overline{\mu}_{3}=0 since, for this value, τ 0 = 1 \tau_{0}=1. In that case we reparameterize the section Σ 3 \Sigma_{3} by means of x ~ 3 = x ¯ 3 − c 0 ​ ( M) \tilde{x}_{3}=\overline{x}_{3}-c_{0}(M), so that x ~ 3 = 0 \tilde{x}_{3}=0 corresponds to the unstable manifold of the saddle point on the blow-up sphere. Then, as before, we write V V as a sum of terms:

 | V ⁡ ( x ~ 3, M) = ε ~ 0 ​ h 0 ​ ( x ~ 3, M) + μ ¯ 3 ​ x ~ 3 ​ ω ​ ( x ~ 3, τ − 1) ​ h 3 ​ ( x ~ 3, M) + ε ~ 1 ​ x ~ 3 ​ h 1 ​ ( x ~ 3, M), V(\tilde{x}_{3},M)=\tilde{{\varepsilon}}_{0}h_{0}(\tilde{x}_{3},M)+\overline{\mu}_{3}\tilde{x}_{3}\omega(\tilde{x}_{3},\tau-1)h_{3}(\tilde{x}_{3},M)+\tilde{{\varepsilon}}_{1}\tilde{x}_{3}h_{1}(\tilde{x}_{3},M), |  | (3.37) |

with h i ​ ( 0, 0) ≠ 0 h_{i}(0,0)\neq 0. We conclude to finite cyclicity by means of Theorem 5.8.

The lower graphic of Sxhh5. Such a graphic occurs for μ ¯ 2 > 0 \overline{\mu}_{2}>0. Because the connection is fixed between the two saddles, the map S S can easily be computed and has the form c 0 + c 1 ​ x ¯ 3 τ + o ⁡ ( x ¯ 3 τ) c_{0}+c_{1}\overline{x}_{3}^{\tau}+o(\overline{x}_{3}^{\tau}), where τ = 1 − 2 ​ μ ¯ 3 − μ ¯ 2 a + μ ¯ 3 \tau=1-\frac{2\overline{\mu}_{3}}{\sqrt{-\frac{\overline{\mu}_{2}}{a}}+\overline{\mu}_{3}} is the product of the two hyperbolicity ratios. Again, we reparameterize the section Σ 3 \Sigma_{3} by means of x ~ 3 = x ¯ 3 − c 0 ​ ( M) \tilde{x}_{3}=\overline{x}_{3}-c_{0}(M), so that x ~ 3 = 0 \tilde{x}_{3}=0 corresponds to the unstable manifold of the right saddle point on the blow-up sphere. This allows writing the map V V in the form

 | { V ⁡ ( x ~ 3) = ∑ i = 0 max ⁡ ( ⌊ τ ⌋, 1) ε ~ i ​ x ~ 3 i ​ h i ​ ( x ~ 3, M) + μ ¯ 3 ​ x ~ 3 τ ​ h τ ​ ( x ~ 3, M), τ 0 ∉ ℕ, V ⁡ ( x ~ 3) = ∑ i = 0 τ 0 ε ~ i ​ x ~ 3 i ​ h i ​ ( x ~ 3, M) + μ ¯ 3 ​ x ~ 3 τ 0 ​ ω ​ ( x ~ 3, τ − τ 0) ​ h τ ​ ( x ~ 3, M), τ 0 ∈ ℕ, \begin{cases}V(\tilde{x}_{3})=\sum_{i=0}^{\max(\lfloor\tau\rfloor,1)}\tilde{{\varepsilon}}_{i}\tilde{x}_{3}^{i}h_{i}(\tilde{x}_{3},M)+\overline{\mu}_{3}\tilde{x}_{3}^{\tau}h_{\tau}(\tilde{x}_{3},M),&\tau_{0}\notin\mathbb{N},\\ V(\tilde{x}_{3})=\sum_{i=0}^{\tau_{0}}\tilde{{\varepsilon}}_{i}\tilde{x}_{3}^{i}h_{i}(\tilde{x}_{3},M)+\overline{\mu}_{3}\tilde{x}_{3}^{\tau_{0}}\omega(\tilde{x}_{3},\tau-\tau_{0})h_{\tau}(\tilde{x}_{3},M),&\tau_{0}\in\mathbb{N},\end{cases} |  |

with h i ​ ( 0, 0) ≠ 0 h_{i}(0,0)\neq 0. We conclude to finite cyclicity by means of Theorem 5.8. □ \Box

## 4 Appendix I — Hyperbolic fixed points

We will consider germs of smooth family of 3 3 -dimensional vector fields X μ, σ X_{\mu,\sigma} at ( 0) ∈ ℝ 3, (0)\in\mathbb{R}^{3}, with coordinates ( u, v, y), (u,v,y), which are quasi-linear of the form:

 | X μ, σ: { u ˙ = u, v ˙ = − v, y ˙ = − σ ​ y + F μ ​ ( u, v, y), X_{\mu,\sigma}:\begin{cases}{\dot{u}}=u,\\ {\dot{v}}=-v,\\ {\dot{y}}=-\sigma y+F_{\mu}(u,v,y),\end{cases} |  | (4.1) |

where σ \sigma is a parameter in a neighborhood of σ 0 ∈ ℝ + \sigma_{0}\in\mathbb{R}^{+}, and μ \mu a parameter in a neighborhood of μ 0 \mu_{0} in some Euclidean space. Moreover, F μ = O ⁡ ( | ( u, v, y) | 2) F_{\mu}=O(|(u,v,y)|^{2}) at the origin, for any value of the parameter ( μ, σ). (\mu,\sigma). The system has the first integral: ν = u ​ v. \nu=uv.

### 4.1 Normal form

It is possible to find local normal form coordinates for X μ, σ X_{\mu,\sigma} by a coordinate change preserving the coordinates u u and v. v. More precisely, we have the following normal form result:

###### Theorem 4.1.

There exists a normalizing operator 𝒩 \mathcal{N} defined on each pair ( X μ, σ, k) (X_{\mu,\sigma},k), where X μ, σ X_{\mu,\sigma} is a family as above and k ∈ ℕ ∗ k\in\mathbb{N}^{*}, such that ,

 | 𝒩 ⁡ ( X μ, σ, k) = ( δ k, K ⁡ ( k), ε k, η k, G μ, σ), \mathcal{N}(X_{\mu,\sigma},k)=\left(\delta_{k},K(k),{\varepsilon}_{k},\eta_{k},G_{\mu,\sigma}\right), |  |

where

 | ( u, v, y) → ( u, v, Y = G μ, σ ​ ( u, v, y)), (u,v,y)\rightarrow(u,v,Y=G_{\mu,\sigma}(u,v,y)), |  |

is a parameter-depending change of coordinates of class C k C^{k} defined defined for | σ − σ 0 | ≤ δ |\sigma-\sigma_{0}|\leq\delta, | μ − μ 0 | < ε k, |\mu-\mu_{0}|<{\varepsilon}_{k}, and | ( u, v, y) | < η k |(u,v,y)|<\eta_{k}, such that d ​ G μ, σ ​ ( 0, 0, 0) = Id, dG_{\mu,\sigma}(0,0,0)=\mathrm{Id}, which brings X μ, σ X_{\mu,\sigma} to the following polynomial normal form of degree K ⁡ ( k) K(k):

1. 1.

If σ 0 ∉ ℚ: \sigma_{0}\not\in\mathbb{Q}:

 | X μ, σ N: { u ˙ = u, v ˙ = − v, Y ˙ = − ( σ + φ μ, σ ​ ( ν)) ​ Y. X^{N}_{\mu,\sigma}:\begin{cases}{\dot{u}}=u,\\ {\dot{v}}=-v,\\ {\dot{Y}}=-(\sigma+\varphi_{\mu,\sigma}(\nu))Y.\end{cases} |  | (4.2) |

2. 2.

If σ 0 = p q ∈ ℚ, \sigma_{0}=\frac{p}{q}\in\mathbb{Q}, with ( p, q) = 1 (p,q)=1 when q ≠ 1: q\not=1:

 | X μ, σ N: { u ˙ = u, v ˙ = − v, Y ˙ = − ( σ + φ μ, σ ​ ( ν)) ​ Y + Φ μ, σ ​ ( ν, u p ​ Y q) ​ Y + v p ​ η μ, σ ​ ( ν), X^{N}_{\mu,\sigma}:\begin{cases}{\dot{u}}=u,\\ {\dot{v}}=-v,\\ {\dot{Y}}=-\Big(\sigma+\varphi_{\mu,\sigma}(\nu)\Big)Y+\Phi_{\mu,\sigma}(\nu,u^{p}Y^{q})Y+v^{p}\eta_{\mu,\sigma}(\nu),\end{cases} |  | (4.3) |

with η μ, σ ≡ 0 \eta_{\mu,\sigma}\equiv 0 when σ 0 ∉ ℕ \sigma_{0}\not\in\mathbb{N} ( q ≠ 1 q\not=1).

The functions φ μ, σ, Φ μ, σ, η μ, σ \varphi_{\mu,\sigma},\Phi_{\mu,\sigma},\eta_{\mu,\sigma} are polynomials of degree ≤ K ⁡ ( k) \leq K(k), with C ∞ C^{\infty} coefficients in ( μ, σ) (\mu,\sigma) and Φ μ, σ ​ ( ν, 0) ≡ 0. \Phi_{\mu,\sigma}(\nu,0)\equiv 0.

###### Proof.

The proof is standard in the literature, and we only recall the main steps.

The degree K ⁡ ( k) K(k) can be determined algorithmically from the eigenvalues { 1, − 1, − σ 0 } \{1,-1,-\sigma_{0}\}.

The number δ k \delta_{k} is chosen sufficiently small so as not to introduce any new resonant terms of degree ≤ K ⁡ ( k) \leq K(k) for some σ ∈ [σ 0 − δ k, σ 0 + δ k] \sigma\in[\sigma_{0}-\delta_{k},\sigma_{0}+\delta_{k}].

The first step is to bring the system to normal form up to degree K ⁡ ( k) K(k)

 | X μ, σ p: { u ˙ = u, v ˙ = − v, z ˙ = P ⁡ ( σ, μ, u, v, z) + R ⁡ ( σ, μ, u, v, z). X^{p}_{\mu,\sigma}:\begin{cases}{\dot{u}}=u,\\ {\dot{v}}=-v,\\ {\dot{z}}=P(\sigma,\mu,u,v,z)+R(\sigma,\mu,u,v,z).\end{cases} |  | (4.4) |

where P ⁡ ( σ, μ, u, v, z) P(\sigma,\mu,u,v,z) is a polynomial in u, v, z u,v,z of degree K ⁡ ( k) K(k) containing only resonant terms, and R ⁡ ( σ, μ, u, v, z) = o ⁡ ( | ( u, v, z) | K ⁡ ( k) CLOSE R(\sigma,\mu,u,v,z)=o(|(u,v,z)|^{K(k)}. This can be done by means of a polynomial change of coordinate

 | y = z + ∑ i + j + ℓ = 2 i − j + σ 0 ​ ( ℓ − 1) ≠ 0 K ⁡ ( k) a i ​ j ​ ℓ ​ r i ​ ρ j ​ z ℓ. y=z+\sum_{\begin{subarray}{c}i+j+\ell=2\\ i-j+\sigma_{0}(\ell-1)\neq 0\end{subarray}}^{K(k)}a_{ij\ell}r^{i}\rho^{j}z^{\ell}. |  |

Because this change of coordinate is tangent to the identity and contains no resonant monomial, then it is uniquely determined.

The second step is to kill the remainder R R in ( 4.4). For this purpose, we decompose R R as R = R 1 + R 2 R=R_{1}+R_{2}, with R 1 = O ⁡ ( u ⌊ K ⁡ ( k) / 2 ⌋) R_{1}=O(u^{\lfloor K(k)/2\rfloor}) and R 2 = O ⁡ ( | ( v, z) | ⌊ K ⁡ ( k) / 2 ⌋) R_{2}=O(|(v,z)|^{\lfloor K(k)/2\rfloor}). Each part is killed by the homotopy method. The details are exactly the same as in [5]. Again, this step is algorithmic. ∎

### 4.2 Properties of compensators

This section is devoted to properties of different fonctions useful for the expression of the results, and in particular the so-called compensators ω α ​ ( ξ) \omega_{\alpha}(\xi) and Ω α, β ​ ( ξ) \Omega_{\alpha,\beta}(\xi) defined in ( 2.9) and ( 3.24).

First, we introduce the analytic function

 | κ ⁡ ( η) = { e η − 1 η, η ≠ 0, 1, η = 0. \kappa(\eta)=\begin{cases}\frac{e^{\eta}-1}{\eta},&\eta\not=0,\\ 1,&\eta=0.\end{cases} |  | (4.5) |

The following Lemma gives some useful properties of κ \kappa:

###### Lemma 4.2.

The function κ \kappa is an entire analytic real function whose series is given by κ ⁡ ( η) = ∑ 0 + ∞ η n ( n + 1)! \kappa(\eta)=\sum_{0}^{+\infty}\frac{\eta^{n}}{(n+1)!}. It follows that d ​ κ d ​ η ​ ( η) < κ ⁡ ( η) < e η \frac{d\kappa}{d\eta}(\eta)<\kappa(\eta)<e^{\eta} for η > 0. \eta>0. Moreover, κ ⁡ ( η) > 0, \kappa(\eta)>0, d ​ κ d ​ η ​ ( η) > 0 \frac{d\kappa}{d\eta}(\eta)>0, and d 2 ​ κ d ​ η 2 ​ ( η) > 0, \frac{d^{2}\kappa}{d\eta^{2}}(\eta)>0, for all η ∈ ℝ. \eta\in\mathbb{R}.

###### Proof.

We have that κ ⁡ ( η) = 1 η ​ ( ∑ 0 + ∞ η n n! − 1) = ∑ 0 + ∞ η n ( n + 1)! \kappa(\eta)=\frac{1}{\eta}(\sum_{0}^{+\infty}\frac{\eta^{n}}{n!}-1)=\sum_{0}^{+\infty}\frac{\eta^{n}}{(n+1)!} and then: d ​ κ d ​ η ​ ( η) = ∑ 0 + ∞ η n n! ​ ( n + 2). \frac{d\kappa}{d\eta}(\eta)=\sum_{0}^{+\infty}\frac{\eta^{n}}{n!(n+2)}. The inequalities d ​ κ d ​ η ​ ( η) < κ ⁡ ( η) < e η \frac{d\kappa}{d\eta}(\eta)<\kappa(\eta)<e^{\eta} for η > 0, \eta>0, follow trivially.

Clearly, κ ⁡ ( η) ≠ 0 \kappa(\eta)\not=0 for all η ∈ ℝ ∖ { 0 } \eta\in\mathbb{R}\setminus\{0\} and as κ ⁡ ( 0) = 1, \kappa(0)=1, it follows that κ ⁡ ( η) > 0 \kappa(\eta)>0 for all η ∈ ℝ. \eta\in\mathbb{R}.

Next, as d ​ κ d ​ η ​ ( η) = η ​ e η − e η + 1 η 2, \frac{d\kappa}{d\eta}(\eta)=\frac{\eta e^{\eta}-e^{\eta}+1}{\eta^{2}}, any root η ≠ 0 \eta\not=0 of d ​ κ d ​ η ​ ( η) = 0 \frac{d\kappa}{d\eta}(\eta)=0 verifies that e η = 1 1 − η. e^{\eta}=\frac{1}{1-\eta}. Comparing the series of these two functions, we see that e η < 1 1 − η e^{\eta}<\frac{1}{1-\eta} for η ∈] 0, 1 [. \eta\in]0,1[. The inequality d ​ κ d ​ η ​ ( η) > 0 \frac{d\kappa}{d\eta}(\eta)>0 is trivially verified when η ≥ 1. \eta\geq 1. Finally, when η < 0, \eta<0, we put η = − δ, \eta=-\delta, with δ ∈ ℝ + \delta\in\mathbb{R}^{+}. The trivial inequality: e δ > 1 + δ, e^{\delta}>1+\delta, for δ ∈ ℝ + \delta\in\mathbb{R}^{+} implies that e η < 1 1 − η e^{\eta}<\frac{1}{1-\eta} for η < 0. \eta<0. As d ​ κ d ​ η ​ ( 0) = 1 2, \frac{d\kappa}{d\eta}(0)=\frac{1}{2}, we have that d ​ κ d ​ η ​ ( η) > 0 \frac{d\kappa}{d\eta}(\eta)>0 for all η ∈ ℝ. \eta\in\mathbb{R}.

To finish, since d 2 ​ κ d ​ η 2 ​ ( η) = ( η 2 − 2 ​ η + 2) ​ e η − 2 η 3, \frac{d^{2}\kappa}{d\eta^{2}}(\eta)=\frac{(\eta^{2}-2\eta+2)e^{\eta}-2}{\eta^{3}}, any root η ≠ 0 \eta\not=0 of d 2 ​ κ d ​ η 2 ​ ( η) = 0 \frac{d^{2}\kappa}{d\eta^{2}}(\eta)=0 verifies that e η = 1 1 − η + 1 2 ​ η 2 e^{\eta}=\frac{1}{1-\eta+\frac{1}{2}\eta^{2}}, or equivalently e − η = 1 − η + 1 2 ​ η 2 e^{-\eta}=1-\eta+\frac{1}{2}\eta^{2}. Let g ⁡ ( η) = e − η − 1 + η − 1 2 ​ η 2 g(\eta)=e^{-\eta}-1+\eta-\frac{1}{2}\eta^{2}. Let us show that g ⁡ ( η) ≠ 0 g(\eta)\neq 0 for η ≠ 0 \eta\neq 0. Indeed, g ′ ​ ( η) = − e − η + 1 − η < 0 g^{\prime}(\eta)=-e^{-\eta}+1-\eta<0. The numerator of d ​ κ d ​ η ​ ( η) \frac{d\kappa}{d\eta}(\eta) is − e η ​ g ′ ​ ( η) -e^{\eta}g^{\prime}(\eta) and is positive for η ≠ 0 \eta\neq 0. Hence, g ′ ​ ( η) < 0 g^{\prime}(\eta)<0 for η ≠ 0 \eta\neq 0, and since g ⁡ ( 0) = 0 g(0)=0, then η ​ g ​ ( η) < 0 \eta g(\eta)<0 for η ≠ 0 \eta\neq 0. As d 2 ​ κ d ​ η 2 ​ ( 0) = 1 3, \frac{d^{2}\kappa}{d\eta^{2}}(0)=\frac{1}{3}, we have that d 2 ​ κ d ​ η 2 ​ ( η) > 0 \frac{d^{2}\kappa}{d\eta^{2}}(\eta)>0 for all η ∈ ℝ. \eta\in\mathbb{R}. ∎

The following lemma gives the relation of ω \omega defined in ( 2.9) with κ \kappa, and interesting properties which can be easily deduced using this relation:

###### Lemma 4.3.

We have that ω ⁡ ( ξ, α) = − κ ⁡ ( − α ​ ln ​ ξ) ​ ln ​ ξ. \omega(\xi,\alpha)=-\kappa(-\alpha\ln\xi)\ln\xi. The compensator ω \omega verifies the following estimates

1. 1.

ω ⁡ ( ξ, α) ≤ − ln ⁡ ξ \omega(\xi,\alpha)\leq-\ln\xi if α ≤ 0 \alpha\leq 0 and ω ⁡ ( ξ, α) ≤ − ξ − α ​ ln ⁡ ξ \omega(\xi,\alpha)\leq-\xi^{-\alpha}\ln\xi if α ≥ 0, \alpha\geq 0, and then

 | ω ⁡ ( ξ, α) = O ⁡ ( ξ − | α | ​ | ln ⁡ ξ |). \omega(\xi,\alpha)=O(\xi^{-|\alpha|}|\ln\xi|). |  | (4.6) |

2. 2.

 | ω ⁡ ( ξ, α) → + ∞ when ( ξ, α) → ( 0, 0). \omega(\xi,\alpha)\rightarrow+\infty\ \ \mathrm{when}\ \ (\xi,\alpha)\rightarrow(0,0). |  | (4.7) |

###### Proof.

Using properties of κ \kappa given in Lemma 4.2, it follows that:

1. 1.

If α ≥ 0, \alpha\geq 0, i.e − α ​ ln ⁡ ξ ≥ 0, -\alpha\ln\xi\geq 0, then ω ⁡ ( ξ, α) = − κ ⁡ ( − α ​ ln ​ ξ) ​ ln ​ ξ \omega(\xi,\alpha)=-\kappa(-\alpha\ln\xi)\ln\xi is less than − e − α ​ ln ⁡ ξ ​ ln ⁡ ξ = − ξ − α ​ ln ⁡ ξ. -e^{-\alpha\ln\xi}\ln\xi=-\xi^{-\alpha}\ln\xi.

2. 2.

If α ≤ 0, \alpha\leq 0, i.e − α ​ ln ⁡ ξ ≤ 0, -\alpha\ln\xi\leq 0, then ω ⁡ ( ξ, α) = − κ ⁡ ( − α ​ ln ​ ξ) ​ ln ​ ξ ≤ − ln ⁡ ξ \omega(\xi,\alpha)=-\kappa(-\alpha\ln\xi)\ln\xi\leq-\ln\xi (indeed, κ \kappa is increasing, κ ⁡ ( 0) = 1, \kappa(0)=1, yielding κ ⁡ ( η) ≤ 1 \kappa(\eta)\leq 1 when OPEN η ≤ 0). \eta\leq 0).

The estimate ( 4.6) follows from these two inequalities. In order to prove ( 4.7), we take any K > 0. K>0.

1. 1.

If − α ​ ln ⁡ ξ ≥ − K, -\alpha\ln\xi\geq-K, we have that κ ⁡ ( − α ​ ln ⁡ ξ) ≥ κ ⁡ ( − K), \kappa(-\alpha\ln\xi)\geq\kappa(-K), as κ \kappa is increasing, and then ω ⁡ ( ξ, α) ≥ − κ ⁡ ( − K) ​ ln ⁡ ξ. \omega(\xi,\alpha)\geq-\kappa(-K)\ln\xi.

2. 2.

If − α ​ ln ⁡ ξ ≤ − K -\alpha\ln\xi\leq-K (in particular α ≤ 0 \alpha\leq 0), we have that

 | ω ⁡ ( ξ, α) = 1 − e − α ​ ln ⁡ ξ | α | ≥ 1 − e − K | α |, \omega(\xi,\alpha)=\frac{1-e^{-\alpha\ln\xi}}{|\alpha|}\geq\frac{1-e^{-K}}{|\alpha|}, |  |

from which ( 4.7) follows. ∎

In parallel with the compensator Ω \Omega introduced in ( 3.24), we introduce the symmetric function

 | 𝒦 ⁡ ( η, δ) = { κ ⁡ ( η) − κ ⁡ ( δ) η − δ, η ≠ δ, d ​ κ d ​ η ​ ( η), η = δ. {\mathcal{K}}(\eta,\delta)=\begin{cases}\frac{\kappa(\eta)-\kappa(\delta)}{\eta-\delta},&\eta\not=\delta,\\ \frac{d\kappa}{d\eta}(\eta),&\eta=\delta.\end{cases} |  | (4.8) |

This yields

 | Ω ⁡ ( ξ, α, β) = 𝒦 ⁡ ( − α ​ ln ⁡ ξ, − β ​ ln ⁡ ξ) ​ ln 2 ​ ξ. \Omega(\xi,\alpha,\beta)={\mathcal{K}}(-\alpha\ln\xi,-\beta\ln\xi)\ln^{2}\xi. |  |

The useful properties of Ω ⁡ ( ξ, α, β) \Omega(\xi,\alpha,\beta) are given by the following lemma:

###### Lemma 4.4.

Ω α, β ​ ( ξ) = O ⁡ ( ξ − γ ​ ln 2 ​ ξ), \Omega_{\alpha,\beta}(\xi)=O(\xi^{-\gamma}\ln^{2}\xi), where γ = max ​ { | α |, | β | } \gamma=\mathrm{max}\{|\alpha|,|\beta|\}, and Ω α, β ​ ( ξ) → + ∞, \Omega_{\alpha,\beta}(\xi)\rightarrow+\infty, when ( ξ, α, β) → ( 0, 0, 0). (\xi,\alpha,\beta)\rightarrow(0,0,0).

###### Proof.

To prove the two claims, we just have to use the Mean Value Theorem for the function 𝒦 {\mathcal{K}}: there exists θ ∈ [η, δ], \theta\in[\eta,\delta], such that 𝒦 ​ ( η, δ) = d ​ κ d ​ η ​ ( θ). {\mathcal{K}}(\eta,\delta)=\frac{d\kappa}{d\eta}(\theta).

Let us begin by the first claim. Let us start with the case α ≥ β \alpha\geq\beta. Then 𝒦 ⁡ ( − α ​ ln ⁡ ξ, − β ​ ln ⁡ ξ) = d ​ κ d ​ η ​ ( θ), {\mathcal{K}}(-\alpha\ln\xi,-\beta\ln\xi)=\frac{d\kappa}{d\eta}(\theta), for some θ ∈ [− β ​ ln ⁡ ξ, − α ​ ln ⁡ ξ]. \theta\in[-\beta\ln\xi,-\alpha\ln\xi]. As d ​ κ d ​ η ​ ( η) \frac{d\kappa}{d\eta}(\eta) is an increasing function (see Lemma 4.2), we have that 𝒦 ⁡ ( − α ​ ln ​ ξ, − β ​ ln ​ ξ) ≤ d ​ κ d ​ η ​ ( − α ​ ln ​ ξ). {\mathcal{K}}(-\alpha\ln\xi,-\beta\ln\xi)\leq\frac{d\kappa}{d\eta}(-\alpha\ln\xi). If α ≤ 0, \alpha\leq 0, we use that d ​ κ d ​ η ​ ( − α ​ ln ⁡ ξ) ≤ d ​ κ d ​ η ​ ( 0) = 1 2 \frac{d\kappa}{d\eta}(-\alpha\ln\xi)\leq\frac{d\kappa}{d\eta}(0)=\frac{1}{2} to obtain that Ω α, β ​ ( ξ) ≤ 1 2 ​ ln 2 ​ ξ. \Omega_{\alpha,\beta}(\xi)\leq\frac{1}{2}\ln^{2}\xi. If α ≥ 0, \alpha\geq 0, again using Lemma 4.2, we have that d ​ κ d ​ η ​ ( − α ​ ln ⁡ ξ) ≤ e − α ​ ln ⁡ ξ = ξ − α \frac{d\kappa}{d\eta}(-\alpha\ln\xi)\leq e^{-\alpha\ln\xi}=\xi^{-\alpha}, and then that: Ω α, β ​ ( ξ) ≤ ξ − α ​ ln 2 ​ ξ. \Omega_{\alpha,\beta}(\xi)\leq\xi^{-\alpha}\ln^{2}\xi. We can summarize the two possibilities by writing that Ω α, β ​ ( ξ) ≤ ξ − | α | ​ ln 2 ​ ξ, \Omega_{\alpha,\beta}(\xi)\leq\xi^{-|\alpha|}\ln^{2}\xi, as soon as α ≥ β \alpha\geq\beta and ξ \xi and | α | |\alpha| sufficiently small. Using the symmetry of Ω α, β ​ ( ξ) \Omega_{\alpha,\beta}(\xi) we can permute α \alpha and β \beta in the above argument to obtain finally that Ω α, β ​ ( ξ) = O ⁡ ( ξ − γ ​ ln 2 ​ ξ), \Omega_{\alpha,\beta}(\xi)=O(\xi^{-\gamma}\ln^{2}\xi), where γ = max ​ { | α |, | β | }. \gamma=\mathrm{max}\{|\alpha|,|\beta|\}.

We now prove the second claim. By symmetry on α \alpha and β \beta it suffices to prove the claim for α ≥ β. \alpha\geq\beta. As above, we can write that Ω α, β ​ ( ξ) = d ​ κ d ​ η ​ ( θ) ​ ln 2 ​ ξ, \Omega_{\alpha,\beta}(\xi)=\frac{d\kappa}{d\eta}(\theta)\ln^{2}\xi, for some θ ∈ [− β ​ ln ⁡ ξ, − α ​ ln ⁡ ξ]. \theta\in[-\beta\ln\xi,-\alpha\ln\xi]. Now, we want to bound Ω α, β \Omega_{\alpha,\beta} from below. Since d ​ κ d ​ η \frac{d\kappa}{d\eta} is increasing, Ω α, β ​ ( ξ) ≥ d ​ κ d ​ η ​ ( − β ​ ln ⁡ ξ) ​ ln 2 ​ ξ. \Omega_{\alpha,\beta}(\xi)\geq\frac{d\kappa}{d\eta}(-\beta\ln\xi)\ln^{2}\xi. If β ≥ 0, \beta\geq 0, we just use that d ​ κ d ​ η ​ ( − β ​ ln ⁡ ξ) ≥ d ​ κ d ​ η ​ ( 0) = 1 2, \frac{d\kappa}{d\eta}(-\beta\ln\xi)\geq\frac{d\kappa}{d\eta}(0)=\frac{1}{2}, to obtain that Ω α, β ​ ( ξ) ≥ 1 2 ​ ln 2 ​ ξ. \Omega_{\alpha,\beta}(\xi)\geq\frac{1}{2}\ln^{2}\xi. If β ≤ 0, \beta\leq 0, we have to compute d ​ κ d ​ η ​ ( − β ​ ln ⁡ ξ) = d ​ κ d ​ η ​ ( | β | ​ ln ⁡ ξ) = d ​ κ d ​ η ​ ( ln ⁡ ξ | β |). \frac{d\kappa}{d\eta}(-\beta\ln\xi)=\frac{d\kappa}{d\eta}(|\beta|\ln\xi)=\frac{d\kappa}{d\eta}(\ln\xi^{|\beta|}). As d ​ κ d ​ η ​ ( η) = ( η − 1) ​ e η + 1 η 2, \frac{d\kappa}{d\eta}(\eta)=\frac{(\eta-1)e^{\eta}+1}{\eta^{2}}, we have that d ​ κ d ​ η ​ ( − β ​ ln ⁡ ξ) = ( | β | ​ ln ⁡ ξ − 1) ​ ξ | β | + 1 | β | 2 ​ ln 2 ​ ξ \frac{d\kappa}{d\eta}(-\beta\ln\xi)=\frac{(|\beta|\ln\xi-1)\xi^{|\beta|}+1}{|\beta|^{2}\ln^{2}\xi} and then: Ω α, β ​ ( ξ) ≥ ( | β | ​ ln ⁡ ξ − 1) ​ ξ | β | + 1 | β | 2, \Omega_{\alpha,\beta}(\xi)\geq\frac{(|\beta|\ln\xi-1)\xi^{|\beta|}+1}{|\beta|^{2}}, yielding that Ω α, β ​ ( ξ) → + ∞. \Omega_{\alpha,\beta}(\xi)\rightarrow+\infty. This yields the conclusion. ∎

### 4.3 Transition along the trajectories

We want to study transition maps for ( 4.1), in the region Q = { u ≥ 0, v ≥ 0, } ⊂ ℝ 3 Q=\{u\geq 0,v\geq 0,\}\subset\mathbb{R}^{3} near the origin. More precisely, let W W be a neighborhood of the origin in ℝ 3 \mathbb{R}^{3}, and Π ⊂ { u = u 0 }, \Pi\subset\{u=u_{0}\}, for u 0 > 0 u_{0}>0, be a section. The neighborhood W W can be chosen sufficiently small so that the trajectory starting at any point in W ∩ { u > 0 } W\cap\{u>0\} reaches Π \Pi for a finite positive time (in particular, OPEN W ∩ Π = ∅). W\cap\Pi=\emptyset). We consider the transition T μ, σ T_{\mu,\sigma} from the points in W ∩ { u > 0 } W\cap\{u>0\} to the section Π. \Pi.

We will compute T μ, σ, T_{\mu,\sigma}, in the 𝒞 k {\mathcal{C}}^{k} -coordinates given by Theorem 4.1. In this system of coordinates the family is the smooth family of polynomial vector fields X μ, σ N X^{N}_{\mu,\sigma} (this means polynomial in ( u, v, y) (u,v,y) with smooth coefficients in OPEN ( μ, σ)). (\mu,\sigma)).

We take Π = [− Y 0, Y 0] × [0, v 0] × { u 0 } \Pi=[-Y_{0},Y_{0}]\times[0,v_{0}]\times\{u_{0}\} for some Y 0 > 0, v 0 > 0. Y_{0}>0,v_{0}>0. On Π \Pi, we replace the coordinate v v by ν = u 0 ​ v, \nu=u_{0}v, with ν ∈ [0, ν 0 = u 0 ​ v 0]. \nu\in[0,\nu_{0}=u_{0}v_{0}]. Then, we can write T μ, σ ​ ( u, v, Y) = ( Y ~ μ, σ ​ ( u, v, Y), ν = u ​ v). T_{\mu,\sigma}(u,v,Y)=(\widetilde{Y}_{\mu,\sigma}(u,v,Y),\nu=uv).

The expression of the Y Y -component Y ~ μ, σ \widetilde{Y}_{\mu,\sigma} is given by the following Theorem:

###### Theorem 4.5.

Let σ ¯ = σ ¯ ​ ( σ, ν) = σ + φ μ, σ ​ ( ν) \bar{\sigma}=\bar{\sigma}(\sigma,\nu)=\sigma+\varphi_{\mu,\sigma}(\nu) and α = α ⁡ ( σ, ν) = σ ¯ ​ ( σ, ν) − σ 0 \alpha=\alpha(\sigma,\nu)=\bar{\sigma}(\sigma,\nu)-\sigma_{0}, where φ μ, σ \varphi_{\mu,\sigma} is the polynomial family introduced in Theorem 4.1. The Y Y -component of the transition map T μ, σ T_{\mu,\sigma} has the following expression on W ∩ { u > 0 } W\cap\{u>0\}:

1. 1.

If σ 0 ∉ ℚ: \sigma_{0}\not\in\mathbb{Q}:

 | Y ~ μ, σ ​ ( u, v, Y) = ( u u 0) σ ¯ ​ Y. \widetilde{Y}_{\mu,\sigma}(u,v,Y)=\Big(\frac{u}{u_{0}}\Big)^{\bar{\sigma}}Y. |  | (4.9) |

2. 2.

If σ 0 = p q ∈ ℚ \sigma_{0}=\frac{p}{q}\in\mathbb{Q} with ( p, q) = 1, (p,q)=1, when σ 0 ∉ ℕ: \sigma_{0}\not\in\mathbb{N}:

 | Y ~ μ, σ ​ ( u, v, Y) = η μ, σ ​ ( ν) ​ v p ​ ( u u 0) σ ¯ ​ ω ​ ( u u 0, α) + ( u u 0) σ ¯ ​ ( Y + ϕ μ, σ ​ ( Y, u, v)), \widetilde{Y}_{\mu,\sigma}(u,v,Y)=\eta_{\mu,\sigma}(\nu)v^{p}\Big(\frac{u}{u_{0}}\Big)^{\bar{\sigma}}\omega\Big(\frac{u}{u_{0}},\alpha\Big)+\Big(\frac{u}{u_{0}}\Big)^{\bar{\sigma}}\Big(Y+\phi_{\mu,\sigma}(Y,u,v)\Big), |  | (4.10) |

where η μ, σ \eta_{\mu,\sigma} is the same as in ( 4.3) (in particular, η μ, σ ≡ 0 \eta_{\mu,\sigma}\equiv 0 when OPEN σ 0 ∉ ℕ). \sigma_{0}\not\in\mathbb{N}).

The function family ϕ μ, σ \phi_{\mu,\sigma} in ( 4.10) is of order O ⁡ ( u p + q ​ α ​ ω q + 1 ​ ( u u 0, α) ​ | ln ⁡ u |) O\left(u^{p+q\alpha}\omega^{q+1}\Big(\frac{u}{u_{0}},\alpha\Big)|\ln u|\right) and, for any integer l ≥ 2, l\geq 2, is of class 𝒞 l − 2 {\mathcal{C}}^{l-2} in ( Y, u 1 / l, u 1 / l ​ ω ​ ( u u 0, α), v, μ, σ) (Y,u^{1/l},u^{1/l}\omega\Big(\frac{u}{u_{0}},\alpha\Big),v,\mu,\sigma).

Proof. The time to go from a point ( u, v, Y) ∈ W ∩ { u > 0 } (u,v,Y)\in W\cap\{u>0\} to the section Π \Pi along the flow of X μ, σ N X^{N}_{\mu,\sigma} is equal to − ln ⁡ u u 0. -\ln\frac{u}{u_{0}}. Expression ( 4.9) follows trivially from the integration of the third line of the system ( 4.2).

Then, from now on, we will assume that σ 0 ∈ ℚ \sigma_{0}\in\mathbb{Q} and we will study the integration of the system ( 4.3). The trajectory through the point ( u, v, Y) (u,v,Y) is equal to ( u ​ e t, v ​ e − t, Y ⁡ ( t)) (ue^{t},ve^{-t},Y(t)) where Y ⁡ ( t) Y(t) is solution of the 1 1 -dimensional non-autonomous differential equation:

 | Y ˙ ​ ( t) = − σ ¯ ​ Y ​ ( t) + Φ μ, σ ​ ( ν, u p ​ e p ​ t ​ Y ​ ( t) q) ​ Y ​ ( t) + e − p ​ t ​ v p ​ η μ, σ ​ ( ν), {\dot{Y}}(t)=-\bar{\sigma}Y(t)+\Phi_{\mu,\sigma}(\nu,u^{p}e^{pt}Y(t)^{q})Y(t)+e^{-pt}v^{p}\eta_{\mu,\sigma}(\nu), |  | (4.11) |

with initial condition Y ⁡ ( 0) = Y. Y(0)=Y.

In order to eliminate the linear term in ( 4.11) we look for Y ⁡ ( t) Y(t) in the form Y ⁡ ( t) = e − σ ¯ ​ t ​ Z ​ ( t). Y(t)=e^{-\bar{\sigma}t}Z(t). As Y ˙ ​ ( t) = e − σ ¯ ​ t ​ Z ˙ ​ ( t) − σ ¯ ​ Y ​ ( t), \dot{Y}(t)=e^{-\bar{\sigma}t}\dot{Z}(t)-\bar{\sigma}Y(t), and letting σ ¯ = p q + α \bar{\sigma}=\frac{p}{q}+\alpha, we obtain the following differential equation for Z ⁡ ( t): Z(t):

 | Z ˙ = Φ μ, σ ​ ( ν, e − q ​ α ​ t ​ u p ​ Z q) ​ Z + e α ​ t ​ v p ​ η μ, σ ​ ( ν), \dot{Z}=\Phi_{\mu,\sigma}(\nu,e^{-q\alpha t}u^{p}Z^{q})Z+e^{\alpha t}v^{p}\eta_{\mu,\sigma}(\nu), |  | (4.12) |

with initial condition Z ⁡ ( 0) = Y. Z(0)=Y. Note that the term in η μ, σ \eta_{\mu,\sigma} is only present when q = 1. q=1.

The 1 1 -dimensional non-autonomous differential equation ( 4.12) is smooth in ( t, Z, σ, ν, u, v, μ) (t,Z,\sigma,\nu,u,v,\mu) and can be integrated for any time t ∈ [0, − ln ⁡ u u 0]. t\in[0,-\ln\frac{u}{u_{0}}]. If Z ⁡ ( t) Z(t) is the solution of ( 4.12) with initial condition Z ⁡ ( 0) = Y, Z(0)=Y, we will have that

 | Y ~ μ, σ ​ ( u, v, Y) = ( u u 0) σ ¯ ​ Z ​ ( − ln ⁡ u u 0). \widetilde{Y}_{\mu,\sigma}(u,v,Y)=\Big(\frac{u}{u_{0}}\Big)^{\bar{\sigma}}Z\Big(-\ln\frac{u}{u_{0}}\Big). |  | (4.13) |

The above expression has to be studied for u > 0 u>0 (we extend Y ~ \widetilde{Y} along { u = 0 } \{u=0\} by OPEN Y ~ μ, σ ​ ( 0, v, Y) = 0). \widetilde{Y}_{\mu,\sigma}(0,v,Y)=0). We first study the integration of ( 4.12).

To begin, it is easy to get rid of the term e α ​ t ​ v p ​ η μ, σ ​ ( ν) e^{\alpha t}v^{p}\eta_{\mu,\sigma}(\nu) in ( 4.12). Let us consider the analytic function

 | Θ ⁡ ( t, α) = { e α ​ t − 1 α, α ≠ 0, t, α = 0. \Theta(t,\alpha)=\begin{cases}\frac{e^{\alpha t}-1}{\alpha},&\alpha\not=0,\\ t,&\alpha=0.\end{cases} |  |

which verifies Θ ˙ = e α ​ t. \dot{\Theta}=e^{\alpha t}. We have that Θ ⁡ ( t, α) = t ​ κ ​ ( α ​ t) \Theta(t,\alpha)=t\kappa(\alpha t) and then ω ⁡ ( ξ, α) = Θ ⁡ ( − ln ⁡ ξ, α). \omega(\xi,\alpha)=\Theta(-\ln\xi,\alpha).

Putting Z ⁡ ( t) = v p ​ η μ, σ ​ ( ν) ​ Θ ​ ( t, α) + Z ¯ ​ ( t), Z(t)=v^{p}\eta_{\mu,\sigma}(\nu)\Theta(t,\alpha)+\bar{Z}(t), we see that Z ¯ ​ ( t) \bar{Z}(t) is the solution of the differential equation

 | Z ¯ ˙ = Φ μ, σ ​ ( ν, u p ​ e − q ​ α ​ t ​ ( v p ​ η μ, σ ​ ( ν) ​ Θ ​ ( t, α) + Z ¯) q) ​ ( v p ​ η μ, σ ​ ( ν) ​ Θ ​ ( t, α) + Z ¯), \dot{\bar{Z}}=\Phi_{\mu,\sigma}\Big(\nu,u^{p}e^{-q\alpha t}(v^{p}\eta_{\mu,\sigma}(\nu)\Theta(t,\alpha)+\bar{Z})^{q}\Big)(v^{p}\eta_{\mu,\sigma}(\nu)\Theta(t,\alpha)+\bar{Z}), |  | (4.14) |

with initial condition Z ¯ ​ ( 0) = Y. \bar{Z}(0)=Y.

As Φ μ, σ ​ ( ν, 0) ≡ 0, \Phi_{\mu,\sigma}(\nu,0)\equiv 0, we can write Φ μ, σ ​ ( ν, ξ) = ξ ​ H μ, σ ​ ( ν, ξ), \Phi_{\mu,\sigma}(\nu,\xi)=\xi H_{\mu,\sigma}(\nu,\xi), where H μ, σ H_{\mu,\sigma} is a smooth function. Now, let us notice that e α ​ t = Θ ˙ = 1 + α ​ Θ. e^{\alpha t}=\dot{\Theta}=1+\alpha\Theta. Moreover the map t → Θ ⁡ ( t, α) t\rightarrow\Theta(t,\alpha) is invertible (for any α \alpha). Then, we can change the time t t by the time Θ \Theta in the differential equation ( 4.14). We obtain the new equation

 | d ​ Z ¯ d ​ Θ = u p ​ H ¯ ​ ( Θ, Z ¯, u, v, ν, α, μ, σ) \frac{d\bar{Z}}{d\Theta}=u^{p}\bar{H}(\Theta,\bar{Z},u,v,\nu,\alpha,\mu,\sigma) |  | (4.15) |

with

 | H ¯ = ( 1 + α ​ Θ) − ( 1 + q) ​ ( v p ​ η ​ Θ + Z ¯) q + 1 ​ H μ, σ ​ ( ν, u p ​ ( 1 + α ​ Θ) − q ​ ( v p ​ η ​ Θ + Z ¯) q), \bar{H}=(1+\alpha\Theta)^{-(1+q)}(v^{p}\eta\Theta+\bar{Z})^{q+1}H_{\mu,\sigma}\Big(\nu,u^{p}(1+\alpha\Theta)^{-q}(v^{p}\eta\Theta+\bar{Z})^{q}\Big), |  | (4.16) |

where η = η μ, σ ​ ( ν). \eta=\eta_{\mu,\sigma}(\nu). Let Ψ ⁡ ( Θ, Y, u, v, ν, α, μ, σ) \Psi\left(\Theta,Y,u,v,\nu,\alpha,\mu,\sigma\right) be the solution of ( 4.15), with the “time” Θ. \Theta. Up to now, Θ \Theta is seen as an independent variable; in particular it is independent from α \alpha. For t = − ln ⁡ u u 0, t=-\ln\frac{u}{u_{0}}, then Θ = ω α ​ ( u u 0), \Theta=\omega_{\alpha}(\frac{u}{u_{0}}), yielding

 | Z ⁡ ( − ln ⁡ u u 0) = Ψ ⁡ ( ω ⁡ ( u u 0, α), Y, u, v, ν, α, μ, σ) + v p ​ η μ, σ ​ ( ν) ​ ω ​ ( u u 0, α), Z\Big(-\ln\frac{u}{u_{0}}\Big)=\Psi\left(\omega\Big(\frac{u}{u_{0}},\alpha\Big),Y,u,v,\nu,\alpha,\mu,\sigma\right)+v^{p}\eta_{\mu,\sigma}(\nu)\omega\Big(\frac{u}{u_{0}},\alpha\Big), |  | (4.17) |

and then, the computation of Y ~ μ, σ ​ ( u, v, Y) \widetilde{Y}_{\mu,\sigma}(u,v,Y) reduces to the computation of Ψ ⁡ ( ω ⁡ ( u u 0, α), Y, u, v, μ, σ). \Psi\left(\omega\Big(\frac{u}{u_{0}},\alpha\Big),Y,u,v,\mu,\sigma\right).

One difficulty in the study of Ψ ⁡ ( ω ⁡ ( u u 0, α), Y, u, v, ν, α, μ, σ) \Psi\left(\omega\Big(\frac{u}{u_{0}},\alpha\Big),Y,u,v,\nu,\alpha,\mu,\sigma\right) is that ω ⁡ ( u u 0, α) → + ∞ \omega\Big(\frac{u}{u_{0}},\alpha\Big)\rightarrow+\infty if u → 0. u\rightarrow 0. To overcome this difficulty we will exploit the fact that the right hand side of ( 4.15) is divisible by u p. u^{p}.

We first study the differential equation ( 4.15). We put u = U l u=U^{l} and change the time Θ \Theta by the time τ = U ​ Θ \tau=U\Theta (and not just by u ​ Θ, u\Theta, as it could seem more natural). The equation ( 4.15) is replaced by the following equation

 | d ​ Z ¯ d ​ τ = U p ​ l − 1 ​ H ¯ ​ ( τ U, Z ¯, U p, v, ν, α, μ, σ), \frac{d\bar{Z}}{d\tau}=U^{pl-1}\bar{H}\Big(\frac{\tau}{U},\bar{Z},U^{p},v,\nu,\alpha,\mu,\sigma\Big), |  | (4.18) |

where H ¯ \bar{H} is given by ( 4.16). Let G ¯ \bar{G} be the right hand side of ( 4.18). It is smooth for U > 0, U>0, but since it is function of α ​ τ U, \alpha\frac{\tau}{U}, it is not well-defined in a whole neighborhood of the point { ( τ, Z ¯, U, v, ν, α, μ, σ) = ( 0, 0, 0, 0, 0, 0, μ 0, σ 0) }. \{(\tau,\bar{Z},U,v,\nu,\alpha,\mu,\sigma)=(0,0,0,0,0,0,\mu_{0},\sigma_{0})\}. Fortunately, we only need to integrate ( 4.18) in a closed domain 𝒟 ¯ \overline{\mathcal{D}}:

Definition of 𝒟 ¯ \overline{\mathcal{D}}. The domain 𝒟 ¯ \overline{\mathcal{D}} is defined in the space ( τ, U, Z ¯, v, ν, α, μ, σ) (\tau,U,\bar{Z},v,\nu,\alpha,\mu,\sigma) defined by

1. 1.

U ∈ [0, U 1], U\in[0,U_{1}], | α | ≤ α 0 |\alpha|\leq\alpha_{0} and τ ∈ [0, U ​ ω ​ ( U l u 0, α)] \tau\in[0,U\omega(\frac{U^{l}}{u_{0}},\alpha)], where U 1, α 0 > 0 U_{1},\alpha_{0}>0 are chosen arbitrarily small (the time τ = U ​ ω ​ ( U l u 0, α) \tau=U\omega(\frac{U^{l}}{u_{0}},\alpha) corresponds to the time OPEN t = − ln ⁡ u u 0 = − l ​ ln ⁡ U u 0) t=-\ln\frac{u}{u_{0}}=-l\ln\frac{U}{u_{0}}),

2. 2.

( Z ¯, v, ν, α, μ, σ) ∈ 𝒜, (\bar{Z},v,\nu,\alpha,\mu,\sigma)\in\mathcal{A}, an arbitrarily small closed neighborhood of the value ( 0, 0, 0, 0, μ 0, σ 0). (0,0,0,0,\mu_{0},\sigma_{0}).

We want to prove that G ¯ \bar{G} is of class 𝒞 l − 2 {\mathcal{C}}^{l-2} on 𝒟 ¯. \overline{\mathcal{D}}. We will first prove a technical lemma about the partial derivatives of the function G ¯. \bar{G}. Let us denote by ∂ m G ¯ \partial_{m}\bar{G} any partial derivative of G ¯ \bar{G} corresponding to a multi-index m = ( m 1, …, m s) m=(m_{1},\ldots,m_{s}) associated to the variables τ, U, Z ¯, v, ν, α, μ, σ \tau,U,\bar{Z},v,\nu,\alpha,\mu,\sigma and the coordinates of μ. \mu. Let | m | = m 1 + ⋯ + m s |m|=m_{1}+\cdots+m_{s} be the degree of m. m. We will note by δ, \delta, a strictly positive number, which can be made arbitrarily small by appropriately choosing U 1 U_{1} and 𝒜. \mathcal{A}. We have the following:

###### Lemma 4.6.

Let be σ 0 = p q \sigma_{0}=\frac{p}{q} as above. Let m m be any multi-index such that | m | ≤ l − 2. |m|\leq l-2. Then, for any δ > 0 \delta>0, there exists a domain 𝒟 ¯ \overline{\mathcal{D}} as above, such that *on the restriction to the domain 𝒟 ¯ \overline{\mathcal{D}}*we have that

 | ∂ m G ¯ = O ⁡ ( U p ​ l − | m | − 1 − δ). \partial_{m}\bar{G}=O(U^{pl-|m|-1-\delta}). |  | (4.19) |

###### Proof.

Recall that G ¯ = U p ​ l ​ H ¯, \bar{G}=U^{pl}\bar{H}, where H ¯ \bar{H} is given by ( 4.16) and Θ \Theta is replaced by τ U. \frac{\tau}{U}. The proof is straightforward, but rather tedious, and we just give the main steps. First, let us notice that on 𝒟 ¯ \overline{\mathcal{D}} we have that, for any s ∈ ℤ s\in\mathbb{Z}:

 | ( 1 + α ​ τ U) s = ( 1 + α ​ Θ) s = e s ​ α ​ t = O ⁡ ( U − | s ​ l ​ α |). \Big(1+\alpha\frac{\tau}{U}\Big)^{s}=(1+\alpha\Theta)^{s}=e^{s\alpha t}=O(U^{-|sl\alpha|}). |  | (4.20) |

Also, using Lemma 4.3, we have that:

 | τ U = Θ = κ ⁡ ( α ​ t) ​ t ≤ e | α | ​ t ​ t ≤ l ​ U − | l ​ α | ​ | ln ⁡ U |. \frac{\tau}{U}=\Theta=\kappa(\alpha t)t\leq e^{|\alpha|t}t\leq lU^{-|l\alpha|}|\ln U|. |  |

These estimations imply that ( 1 + α ​ τ U) − ( q + 1) \Big(1+\alpha\frac{\tau}{U}\Big)^{-(q+1)} and τ U \frac{\tau}{U} have an order O ⁡ ( U − δ). O(U^{-\delta}). As H ¯ \bar{H} is bounded on 𝒟 ¯, \bar{\mathcal{D}}, we have that G ¯ = O ⁡ ( U p ​ l − 1 − δ). \bar{G}=O(U^{pl-1-\delta}). This is the expected result for m = 0. m=0.

Next, we use the expression of the partial derivatives of G ¯, \bar{G}, in terms of the functions Θ, \Theta, ( 1 + α ​ Θ) − q (1+\alpha\Theta)^{-q} or ( 1 + α ​ Θ) − ( q + 1) (1+\alpha\Theta)^{-(q+1)} and the partial derivatives of H μ, σ, H_{\mu,\sigma}, evaluated on 𝒟 ¯ \overline{\mathcal{D}} (these partial derivatives are bounded on OPEN 𝒟 ¯). \overline{\mathcal{D}}). We have for instance that:

 | ∂ ∂ U ​ ( 1 + α ​ Θ) − q = − q ​ l ​ α ​ ( 1 + α ​ Θ) − ( q) ​ 1 U = O ⁡ ( U − 1 − δ). \frac{\partial}{\partial U}(1+\alpha\Theta)^{-q}=-ql\alpha(1+\alpha\Theta)^{-(q)}\frac{1}{U}=O(U^{-1-\delta}). |  |

As ( 1 + α ​ Θ) − q = O ⁡ ( U − δ), (1+\alpha\Theta)^{-q}=O(U^{-\delta}), we remark that the order in U U has discreased by one unit (modulo an order in OPEN δ). \delta).

It is easy to see that this observation can be generalized for any partial derivative: the previous order in U U decreases by one unity for each first order partial derivation (modulo an order in OPEN δ). \delta).

Then, starting with G ¯ = O ⁡ ( U p ​ l − 1 − δ) \bar{G}=O(U^{pl-1-\delta}) for m = 0, m=0, the estimation ( 4.18) for any multi-index m m follows directly by recurence from this fall of order (let us notice that, in a symbolic way, we have: OPEN `​ `​ δ + δ = δ ​ "). ``\delta+\delta=\delta"). ∎

End of the proof of Theorem 4.5

Lemma 4.6 says that each partial derivative ∂ m G ¯ \partial_{m}\bar{G} can be extended continuously on τ = U = 0 \tau=U=0 by giving it the value zero at these points. Then, as the function G ¯ \bar{G} is smooth on 𝒟 ¯ ∖ { τ = U = 0 }, \overline{\mathcal{D}}\setminus\{\tau=U=0\}, the restriction of G ¯ \bar{G} to 𝒟 ¯ \overline{\mathcal{D}} is a function of differentiability class 𝒞 l − 2, {\mathcal{C}}^{l-2}, on the whole domain 𝒟 ¯, \overline{\mathcal{D}}, including the points on { τ = U = 0 }, \{\tau=U=0\}, when we give to each partial derivative of G ¯ \bar{G} or order less than l − 2 l-2 the value 0 0 at these points. Let ℬ \mathcal{B} be a closed neighborhood of ( 0, 0, 0) (0,0,0) in the ( τ, α, U) (\tau,\alpha,U) -plane, containing the closed set

 | { ( τ, α, U) | τ ∈ [0, − l U ln U U 0], | α | ≤ α 0, U ∈ [0, U 1] } \{(\tau,\alpha,U)\ |\ \tau\in[0,-lU\ln\frac{U}{U_{0}}],\ |\alpha|\leq\alpha_{0},\ U\in[0,U_{1}]\} |  |

that we have introduced above in the definition of 𝒟 ¯ \overline{\mathcal{D}}. The closed domain 𝒟 ¯ \overline{\mathcal{D}} is contained in the neighborhood 𝒜 × ℬ. \mathcal{A}\times\mathcal{B}. Using the Whitney Theorem for the extention of differentiable functions (see [M] for instance), we can find a 𝒞 l − 2 {\mathcal{C}}^{l-2} -function G ~ \widetilde{G} on a 𝒜 × ℬ \mathcal{A}\times\mathcal{B} such that G ~ | 𝒟 ¯ ≡ G ¯ \widetilde{G}|_{\overline{\mathcal{D}}}\equiv\bar{G} (here, this extention can also be easily constructed by hand, in an elementary way).

For times τ ∈ [0, − l ​ U ​ ln ⁡ U U 0] \tau\in[0,-lU\ln\frac{U}{U_{0}}] the flow Ψ ⁡ ( τ, Z ¯, U, v, ν, α, μ, σ) \Psi(\tau,\bar{Z},U,v,\nu,\alpha,\mu,\sigma) of the differential equation ( 4.15): d ​ Z ¯ d ​ τ = G ¯ \frac{d\bar{Z}}{d\tau}=\bar{G} coincides with the flow Ψ ~ ​ ( τ, Z ¯, U, v, ν, α, μ, σ) \widetilde{\Psi}(\tau,\bar{Z},U,v,\nu,\alpha,\mu,\sigma) of the differential equation d ​ Z ¯ d ​ τ = G ~. \frac{d\bar{Z}}{d\tau}=\widetilde{G}. This equation is of differentiability class 𝒞 l − 2 {\mathcal{C}}^{l-2} on 𝒜 × ℬ, \mathcal{A}\times\mathcal{B}, as well as its flow Ψ ~. \widetilde{\Psi}.

In particular, we have that

 | Z ¯ ​ ( − ln ⁡ u u 0) = Ψ ~ ​ ( U ​ ω ​ ( U l u 0, α), Y, U, v, ν, α, μ, σ), \bar{Z}\Big(-\ln\frac{u}{u_{0}}\Big)=\widetilde{\Psi}\left(U\omega\Big(\frac{U^{l}}{u_{0}},\alpha\Big),Y,U,v,\nu,\alpha,\mu,\sigma\right), |  | (4.21) |

is a 𝒞 l − 2 {\mathcal{C}}^{l-2} -function of ( Y, U, U ​ ω ​ ( U l u 0, α), v, ν, α, μ, σ) (Y,U,U\omega\Big(\frac{U^{l}}{u_{0}},\alpha\Big),v,\nu,\alpha,\mu,\sigma), i.e. is a 𝒞 l − 2 {\mathcal{C}}^{l-2} -function in the variables ( Y, u 1 l, u 1 l ​ ω ​ ( u u 0, α), v, ν, α, μ, σ) \left(Y,u^{\frac{1}{l}},u^{\frac{1}{l}}\omega(\frac{u}{u_{0}},\alpha),v,\nu,\alpha,\mu,\sigma\right), a function which is defined on a neighborhood of the point ( 0, 0, 0, 0, 0, μ 0, σ 0). (0,0,0,0,0,\mu_{0},\sigma_{0}). We can replace α \alpha (outside ω \omega) by its expression in ( σ, ν) (\sigma,\nu) and ν \nu by u ​ v uv to obtain finally that Z ¯ ​ ( − ln ⁡ u u 0) \bar{Z}\Big(-\ln\frac{u}{u_{0}}\Big) is a 𝒞 l − 2 {\mathcal{C}}^{l-2} -function of ( Y, u 1 l, u 1 l ​ ω ​ ( u u 0, α), v, μ, σ) \left(Y,u^{\frac{1}{l}},u^{\frac{1}{l}}\omega(\frac{u}{u_{0}},\alpha),v,\mu,\sigma\right). As Z ¯ ​ ( 0) = Y, \bar{Z}(0)=Y, we can write

 | Z ¯ ​ ( − ln ⁡ u u 0) = Y + ϕ μ, σ ​ ( Y, u, v), \bar{Z}\Big(-\ln\frac{u}{u_{0}}\Big)=Y+\phi_{\mu,\sigma}(Y,u,v), |  | (4.22) |

where

 | ϕ μ, σ = Ψ ~ ​ ( U ​ ω ​ ( U l u 0, α), Y, U, v, ν, α, μ, σ) − Y \phi_{\mu,\sigma}=\widetilde{\Psi}\left(U\omega\Big(\frac{U^{l}}{u_{0}},\alpha\Big),Y,U,v,\nu,\alpha,\mu,\sigma\right)-Y |  | (4.23) |

is a 𝒞 l − 2 {\mathcal{C}}^{l-2} -function of ( Y, u 1 l, u 1 l ​ ω ​ ( u u 0, α), v, μ, σ). \left(Y,u^{\frac{1}{l}},u^{\frac{1}{l}}\omega(\frac{u}{u_{0}},\alpha),v,\mu,\sigma\right). Finally, collecting the different terms in ( 4.13), ( 4.17), ( 4.22) and ( 4.23), we obtain the expression ( 4.10) in Theorem 4.5, for the transition function Y ~ μ, σ ​ ( u, v, Y). \widetilde{Y}_{\mu,\sigma}(u,v,Y).

We can estimate ϕ μ, σ \phi_{\mu,\sigma} from the differential equation ( 4.14) for Z ¯ ​ ( t). \bar{Z}(t). If G ⁡ ( t, Z ¯, u, v, ν, α, σ, μ) G(t,\bar{Z},u,v,\nu,\alpha,\sigma,\mu) is the right hand side of ( 4.14), we have that G = O ⁡ ( u p ​ e − q ​ α ​ t ​ Θ q + 1) G=O(u^{p}e^{-q\alpha t}\Theta^{q+1}) on the domain 𝒟 ¯ \overline{\mathcal{D}} defined above. As t ≤ − ln ⁡ u u 0 t\leq-\ln\frac{u}{u_{0}} on 𝒟 ¯, \overline{\mathcal{D}}, then Θ ⁡ ( t, α) ≤ ω ⁡ ( u u 0, α) \Theta(t,\alpha)\leq\omega\Big(\frac{u}{u_{0}},\alpha\Big), yielding G = O ⁡ ( u p + q ​ α ​ ω q + 1 ​ ( u u 0, α)). G=O(u^{p+q\alpha}\omega^{q+1}(\frac{u}{u_{0}},\alpha)). From this estimate of the order of G G, it follows that

 | ϕ μ, σ = Z ¯ ​ ( − ln ⁡ u u 0) − Y = O ⁡ ( u p + q ​ α ​ ω q + 1 ​ ( u u 0, α) ​ | ln ⁡ u |), \phi_{\mu,\sigma}=\bar{Z}\Big(-\ln\frac{u}{u_{0}}\Big)-Y=O(u^{p+q\alpha}\omega^{q+1}\Big(\frac{u}{u_{0}},\alpha\Big)|\ln u|), |  |

which is the estimation in the statement of Theorem 4.5. □ \Box

### 4.4 Transitions between sections

Theorem 4.5 gives the expression of the transition T μ, σ = ( ν, Y ~ μ, σ), T_{\mu,\sigma}=(\nu,\widetilde{Y}_{\mu,\sigma}), starting from any point ( u, v, Y) (u,v,Y) in the domain W ∩ { u > 0 } W\cap\{u>0\} and landing on a section Π ⊂ { u = u 0 }, \Pi\subset\{u=u_{0}\}, for some u 0 > 0 u_{0}>0 (we can extend trivially T μ, σ T_{\mu,\sigma} to the whole neighborhood W W by taking OPEN Y ~ μ, σ ​ ( u, v, 0) = 0). \widetilde{Y}_{\mu,\sigma}(u,v,0)=0). We apply this to get Theorems 2.2 and 2.3 after changing ( u, v) ↦ ( r, ρ) (u,v)\mapsto(r,\rho).

Discussion of Theorems 2.2 and 2.3. A previous version of Theorems 2.2 and 2.3 was given in Theorems 4.10 and 4.14 of [8]. It is interesting to compare their proofs and formulations with the proofs and formulations in the present paper.

1. 1.

The proof in the present version is unified: Theorem 4.5 gives a formula for a global transition from any point in a 3 3 -dimensional neighborhood W, W, formula which is easy to restrict on the two different types of section Σ. \Sigma. Next, the proof of Theorem 4.5, even if it is based on the same normal form, is much shorter than the proofs of Theorems 4.10 and 4.14 given in [8]. The reason seems to be that in [8] the transition function Y ~ \widetilde{Y} and its partial derivatives are directly estimated by a variational method. In the present paper, we have replaced the 1 1 -dimensional non-autonomous differential system: Z ¯ ˙ = G ¯, \dot{\bar{Z}}=\bar{G}, which is not defined in a neighborhood of the point { ( τ, Z ¯, U, v, ν, α, μ, σ) = ( 0, 0, 0, 0, 0, 0, μ 0, σ 0) }, \{(\tau,\bar{Z},U,v,\nu,\alpha,\mu,\sigma)=(0,0,0,0,0,0,\mu_{0},\sigma_{0})\}, by a differential equation: Z ¯ ˙ = G ~, \dot{\bar{Z}}=\widetilde{G}, differentiable on a neighborhood of this point. As a consequence, we obtain almost without computation that the function ϕ μ, σ \phi_{\mu,\sigma} is differentiable (in terms of fractional power and a compensator of some variable). In fact, the heavy computations made in [8] are replaced by an implicit use of the Cauchy Theorem for differential equations.

2. 2.

We can compare the statements in [8] and in the present paper. We restrict the comparison to the only non-trivial case: σ 0 ∈ ℚ \sigma_{0}\in\mathbb{Q}. The transition function called here Y ~ μ, σ \widetilde{Y}_{\mu,\sigma} is given by the formula (4.11) of Theorem 4.10 of [8]. We can observe that it is quite similar to the above formula ( 4.20), up to the changes of notations. The same remarks are valid for the transition of type II which is treated in Theorem 4.14 in [8]. The only important difference is in the form and properties of the function ϕ μ, σ, \phi_{\mu,\sigma}, which is called ϕ \phi or θ \theta in [8]. We will comment on this in the next items.

3. 3.

The function ϕ μ, σ \phi_{\mu,\sigma} in Theorem 2.2 is of order O ⁡ ( ν p + q ​ α ​ ω q + 1 ​ ( ν ν 0, α) ​ | ln ⁡ ν |). O(\nu^{p+q\alpha}\omega^{q+1}\Big(\frac{\nu}{\nu_{0}},\alpha\Big)|\ln\nu|). This order has to be compared with the order given for the function ϕ \phi in Theorem 4.10 of [8] which is exactly the same order for α < 0 \alpha<0, but equal to O ⁡ ( ν p ​ ω q + 1 ​ ( ν ν 0, α) ​ | ln ⁡ ν |) O(\nu^{p}\omega^{q+1}\Big(\frac{\nu}{\nu_{0}},\alpha\Big)|\ln\nu|) for α > 0. \alpha>0. This minor difference is probably due to the difference in the method of proof. It is less easy to compare the order of ϕ μ, σ \phi_{\mu,\sigma} in Theorem 2.3 with the order of θ \theta in Theorem 4.14 of [8].

4. 4.

In Theorem 4.10 of [8], ϕ \phi is a 𝒞 ∞ {\mathcal{C}}^{\infty} -function of ω ⁡ ( ν ν 0, α) \omega\Big(\frac{\nu}{\nu_{0}},\alpha\Big) and other variables. Since ω → + ∞ \omega\rightarrow+\infty for ν → 0, \nu\rightarrow 0, this means that the domain of ϕ \phi has to be unbounded. This implies that it is not possible to deduce directly the order of the partial derivatives of ϕ. \phi. This order is obtained by using variational methods and heavy computations. On the contrary, the formulation given in Theorems 2.2 and 2.3, permits a direct deduction of the order of any partial derivative of ϕ μ, σ. \phi_{\mu,\sigma}. Let us show this on an example for a transition map of type I. Considering any l ∈ ℕ l\in\mathbb{N} and observing that ϕ μ, σ \phi_{\mu,\sigma} is of order O ⁡ ( ν p − δ), O(\nu^{p-\delta}), we can write

 | ϕ μ, σ = ν p − 1 l ​ ϕ ¯ μ, σ, \phi_{\mu,\sigma}=\nu^{p-\frac{1}{l}}\bar{\phi}_{\mu,\sigma}, |  |

where ϕ ¯ μ, σ \bar{\phi}_{\mu,\sigma} is a 𝒞 l − p − 3 {\mathcal{C}}^{l-p-3} -function in ( Y, ν 1 / l, ν 1 / l ​ ω ​ ( ν ν 0, α), μ, σ) (Y,\nu^{1/l},\nu^{1/l}\omega\Big(\frac{\nu}{\nu_{0}},\alpha\Big),\mu,\sigma).

As a consequence any partial derivative of ϕ μ, σ \phi_{\mu,\sigma} in terms of Y, μ, σ, Y,\mu,\sigma, of degree less than l − p − 3, l-p-3, is of order O ⁡ ( ν p − 1 l). O(\nu^{p-\frac{1}{l}}). Taking into account that we can take l l arbirarily large, this order in very similar to the order obtained in Theorem 4.10 of [8].

## 5 Appendix II—Counting the number of roots

### 5.1 Differentiable functions on monomials

We come back to the notations of Section 3: r, ρ r,\rho are variables defined in a compact neighborhood 𝒜 \mathcal{A} of ( 0, 0) (0,0) in the first quadrant Q = { r ≥ 0, ρ ≥ 0 }. Q=\{r\geq 0,\rho\geq 0\}. We will always choose 𝒜 \mathcal{A} to be a rectangle [0, r 1] × [0, ρ 1], [0,r_{1}]\times[0,\rho_{1}], in order to have connected curves l ν = { ( r, ρ) ∈ 𝒜 | r ​ ρ = 0 }. l_{\nu}=\{(r,\rho)\in\mathcal{A}\ |\ r\rho=0\}. In the following definitions we will use also compensators ω γ \omega_{\gamma} and Ω γ, δ, \Omega_{\gamma,\delta}, depending on other parameters γ, δ. \gamma,\delta. We will often use the shortened notation ω γ, Ω γ, δ \omega_{\gamma},\Omega_{\gamma,\delta} for ω γ ​ ( r r 0), Ω γ, δ ​ ( r r 0). \omega_{\gamma}\Big(\frac{r}{r_{0}}\Big),\Omega_{\gamma,\delta}\Big(\frac{r}{r_{0}}\Big). Moreover, changing r r to r r 0 \frac{r}{r_{0}}, we can of course suppose that r 0 = 1 r_{0}=1.

We consider a multi-parameter λ \lambda in a compact neighborhood ℬ \mathcal{B} of a value λ 0 \lambda_{0} in some euclidean space ℰ. {\mathcal{E}}. The neighborhood ℬ \mathcal{B} will be chosen sufficiently small to have the desired properties.

We also consider functions which are differentiable on real powers of r, ρ r,\rho and compensators in r. r. We give a precise definition of this notion.

###### Definition 5.1.

1. 1.

A *primary monomial (monomial in short),*is an expression M = r a, ρ b, M=r^{a},\ \rho^{b}, r a ​ ω γ ​ ( r) c, r a ​ Ω γ 1, γ 2 ​ ( r) d \ r^{a}\omega_{\gamma}(r)^{c},\ r^{a}\Omega_{\gamma_{1},\gamma_{2}}(r)^{d} or ω γ ​ ( r) − e \omega_{\gamma}(r)^{-e} where a, b, c, d, e a,b,c,d,e and γ, γ 1, γ 2 \gamma,\gamma_{1},\gamma_{2} are smooth functions of λ. \lambda. Moreover a, b, e a,b,e are strictly positive and γ ⁡ ( λ 0) = γ 1 ​ ( λ 0) = γ 2 ​ ( λ 0) = 0 \gamma(\lambda_{0})=\gamma_{1}(\lambda_{0})=\gamma_{2}(\lambda_{0})=0 (we can have γ = α \gamma=\alpha or β \beta and OPEN ( γ 1, γ 2) = ( α, β)). (\gamma_{1},\gamma_{2})=(\alpha,\beta)). For instance, r 2 3, ρ 1 5, ω α − 1, r ​ Ω α, β r^{\frac{2}{3}},\ \rho^{\frac{1}{5}},\omega_{\alpha}^{-1},r\Omega_{\alpha,\beta} are primary monomials but not r α r^{\alpha} or ω α α. \omega_{\alpha}^{\alpha}.

A monomial M M defines a λ \lambda -family of functions M ⁡ ( r, ρ, λ) M(r,\rho,\lambda) on Q = { r ≥ 0, ρ ≥ 0 }, Q=\{r\geq 0,\ \rho\geq 0\}, M M is smooth for r > 0 r>0 and, by Lemmas 4.3 and 4.4, it can be extended continuously along { r = 0 }); \{r=0\}); we have that M ⁡ ( 0, 0, λ 0) = 0 M(0,0,\lambda_{0})=0 (i.e. M = o ⁡ ( 1), M=o(1), in terms of some distance of ( r, ρ, λ) (r,\rho,\lambda) to OPEN ( 0, 0, λ 0)). (0,0,\lambda_{0})).

2. 2.

We say that a function f ⁡ ( r, ρ, λ) f(r,\rho,\lambda) on 𝒜 × ℬ \mathcal{A}\times\mathcal{B} is a *𝒞 k {\mathcal{C}}^{k} -function on the monomials M 1, …, M l M_{1},\ldots,M_{l}*if there exists a 𝒞 k {\mathcal{C}}^{k} -function f ~ ​ ( ξ 1, …, ξ l, λ) \tilde{f}(\xi_{1},\ldots,\xi_{l},\lambda) defined on 𝒜 ~ × ℬ, \widetilde{\mathcal{A}}\times\mathcal{B}, where 𝒜 ~ \widetilde{\mathcal{A}} is a neighborhood of 0 ∈ ℝ l 0\in\mathbb{R}^{l} such that f ⁡ ( r, ρ, λ) = f ~ ​ ( M 1, …, M l, λ). f(r,\rho,\lambda)=\tilde{f}(M_{1},\ldots,M_{l},\lambda). If the number of monomials and their type is not specified, we just say that f f is a 𝒞 k {\mathcal{C}}^{k} -function on monomials.

Clearly, the space of 𝒞 k {\mathcal{C}}^{k} -functions on monomials, defined on 𝒜 × ℬ \mathcal{A}\times\mathcal{B} is a ring. The classical theorems of differential calculus (Taylor formula, division theorem and so on) can be extended to these functions by applying them to the function f ~. \tilde{f}. Since the differentiability class k k is finite, there will be falls of differentiability class in these operations: Lemma 5.3 is one example. For this reason, we will consider functions f f with the property to be 𝒞 k {\mathcal{C}}^{k} -functions on monomials, for any k ∈ ℕ k\in\mathbb{N} (but with a choice of monomials and a size of the neighborhood 𝒜 × ℬ \mathcal{A}\times\mathcal{B} that may depend on k k). The functions ψ μ, σ ​ ( Y, u, v), ψ μ, σ ​ ( Y, ν) \psi_{\mu,\sigma}(Y,u,v),\psi_{\mu,\sigma}(Y,\nu) and ψ μ, σ ​ ( u, v) \psi_{\mu,\sigma}(u,v) introduced in the statements of Theorems 4.5 are, 2.2, and 2.3 are examples of 𝒞 k {\mathcal{C}}^{k} -functions on monomials for any k, k, which use only the single compensator ω α. \omega_{\alpha}. The functions h i h_{i} entering in the expression of the displacement map V V in Section 3 are using other compensators ω γ \omega_{\gamma}, and also Ω α, β. \Omega_{\alpha,\beta}.

### 5.2 Procedure of division-derivation for functions with 2 2 variables

###### Notation 5.2.

In this section, h ⁡ ( r, ρ, λ) = o ⁡ ( 1) h(r,\rho,\lambda)=o(1) will mean that h ⁡ ( 0, 0, λ 0) = 0. h(0,0,\lambda_{0})=0.

We want to bound the number of roots of an equation { V ( r, ρ, λ) = 0 } \{V(r,\rho,\lambda)=0\} along the curves l ν = { r ​ ρ = ν | ( r, ρ) ∈ 𝒜 }, l_{\nu}=\{r\rho=\nu\ |\ (r,\rho)\in\mathcal{A}\}, for ν > 0 \nu>0 and a neighborhood 𝒜 × ℬ \mathcal{A}\times\mathcal{B} sufficiently small. The function V V is expressed using 𝒞 k {\mathcal{C}}^{k} -functions on monomials. To obtain this bound, we will apply Rolle’s Theorem, and to this end we will use recurrently the Lie-derivative L 𝒳 L_{\mathcal{X}} of V V by the vector field

 | 𝒳 = r ​ ∂ ∂ r − ρ ​ ∂ ∂ ρ. {\mathcal{X}}=r\frac{\partial}{\partial r}-\rho\frac{\partial}{\partial\rho}. |  | (5.1) |

Hence, we need some properties of L 𝒳 L_{\mathcal{X}} acting on 𝒞 k {\mathcal{C}}^{k} -functions on monomials. It is easy to see that:

 | { L 𝒳 ​ r a = a ​ r a, L 𝒳 ​ ρ b = − b ​ ρ b, L 𝒳 ​ ω γ = − ( 1 + γ ​ ω γ), L 𝒳 ​ Ω γ 1, γ 2 = − ( ω γ 1 + γ 2 ​ Ω γ 1, γ 2). \begin{cases}L_{\mathcal{X}}r^{a}=ar^{a},\\ L_{\mathcal{X}}\rho^{b}=-b\rho^{b},\\ L_{\mathcal{X}}\omega_{\gamma}=-(1+\gamma\omega_{\gamma}),\\ L_{\mathcal{X}}\Omega_{\gamma_{1},\gamma_{2}}=-(\omega_{\gamma_{1}}+\gamma_{2}\Omega_{\gamma_{1},\gamma_{2}}).\end{cases} |  | (5.2) |

From this, it follows that

###### Lemma 5.3.

If f f is a 𝒞 k {\mathcal{C}}^{k} -function on monomials, then L 𝒳 ​ f L_{\mathcal{X}}f is a 𝒞 k − 1 {\mathcal{C}}^{k-1} -function on monomials and L 𝒳 ​ f = o ⁡ ( 1). L_{\mathcal{X}}f=o(1).

###### Proof.

If M M is any monomial, L 𝒳 ​ M L_{\mathcal{X}}M is a linear combinaison of monomials. Then, L 𝒳 ​ f = ∑ i ∂ f ~ ∂ ξ i ​ L 𝒳 ​ M i, L_{\mathcal{X}}f=\sum_{i}\frac{\partial\tilde{f}}{\partial\xi_{i}}L_{\mathcal{X}}M_{i}, is a 𝒞 k − 1 {\mathcal{C}}^{k-1} -function on monomials and, since each monomial is o ⁡ ( 1), o(1), this function L 𝒳 ​ f L_{\mathcal{X}}f is also o ⁡ ( 1) o(1). ∎

For the procedure of division-derivation we will need more general monomials than the admissible ones:

###### Definition 5.4.

1. 1.

A *general monomial*is an expression M = r a ​ ρ b ​ ∏ i ω i c i ​ ∏ j Ω j d j M=r^{a}\rho^{b}\prod_{i}\omega_{i}^{c_{i}}\prod_{j}\Omega_{j}^{d_{j}} where i i and j j belong to finite sets of indices. The coefficients a, b, c i, d j, a,b,c_{i},d_{j}, as well as the internal parameters of the compensators ω i, Ω j, \omega_{i},\Omega_{j}, are smooth functions of λ \lambda (without any restriction on sign). Let a ⁡ ( λ 0) = a 0, b ⁡ ( λ 0) = b 0. a(\lambda_{0})=a^{0},b(\lambda_{0})=b^{0}.

2. 2.

A general monomial is *resonant*if a 0 = b 0 a^{0}=b^{0} (in this case the “polynomial” part r a 0 ​ ρ b 0 r^{a^{0}}\rho^{b^{0}} of M M reduces to the first integral ν a 0 \nu^{a^{0}}). Seen as a function of ( r, ρ, λ), (r,\rho,\lambda), such a monomial is in general not defined for r = 0 r=0 and ρ = 0. \rho=0.

###### Remark 5.5.

An interesting property is that if M M is a general monomial, then M − 1 M^{-1} is also a general monomial.

###### Notation 5.6.

For convenience, if ω i = ω ⁡ ( r, γ i) \omega_{i}=\omega(r,\gamma_{i}) we will use the contracting expressions: ω = ( ω i) i, γ = ( γ i) i, c = ( c i) i, ∏ i ω i c i = ω c, ∑ i γ i ​ c i = γ ​ c. \omega=(\omega_{i})_{i},\ \gamma=(\gamma_{i})_{i},\ c=(c_{i})_{i},\ \prod_{i}\omega_{i}^{c_{i}}=\omega^{c},\sum_{i}\gamma_{i}c_{i}=\gamma c.

A first easy result, which will be the principal tool in the proof of Theorem 5.8 below, is the following:

###### Lemma 5.7.

We consider an expression f = M ⁡ ( 1 + h) f=M(1+h) where M = r a ​ ρ b ​ ω c M=r^{a}\rho^{b}\omega^{c} is a general non-resonant monomial without Ω \Omega -factor and h h is a 𝒞 k {\mathcal{C}}^{k} -function on monomials, of order o ⁡ ( 1). o(1). Then, on a sufficiently small neighborhood ℬ \mathcal{B}, we can write:

 | L 𝒳 ​ f = ( a − b + γ ​ c) ​ M ​ ( 1 + g), L_{\mathcal{X}}f=(a-b+\gamma c)M(1+g), |  | (5.3) |

with g, g, a 𝒞 k − 1 {\mathcal{C}}^{k-1} -function on monomials, of order o ⁡ ( 1). o(1).

###### Proof.

We have that L 𝒳 ​ f = L 𝒳 ​ M ​ ( 1 + h) + M ​ L 𝒳 ​ h. L_{\mathcal{X}}f=L_{\mathcal{X}}M(1+h)+ML_{\mathcal{X}}h. Using the formula of derivation for ω \omega, we obtain that L 𝒳 ​ M = ( a − b + γ ​ c + c ​ ω − 1) ​ M. L_{\mathcal{X}}M=(a-b+\gamma c+c\omega^{-1})M. As M M is non-resonant, we have that a 0 − b 0 ≠ 0 a^{0}-b^{0}\not=0 and, if ℬ \mathcal{B} is a sufficiently small neighborhood of λ 0, \lambda_{0}, we will also have that a − b + γ ​ c ≠ 0 a-b+\gamma c\not=0 on ℬ. \mathcal{B}. Then, we obtain that:

 | L 𝒳 ​ f = ( a − b + γ ​ c) ​ ( 1 + c ​ ω − 1 a − b + γ ​ c) ​ M ​ ( 1 + h) + M ​ L 𝒳 ​ h. L_{\mathcal{X}}f=(a-b+\gamma c)\Big(1+\frac{c\omega^{-1}}{a-b+\gamma c}\Big)M(1+h)+ML_{\mathcal{X}}h. |  |

We can write this expression as L 𝒳 ​ f = ( a − b + γ ​ c) ​ M ​ ( 1 + g), L_{\mathcal{X}}f=(a-b+\gamma c)M(1+g), with

 | g = h + c ​ ω − 1 ​ ( 1 + h) + L 𝒳 ​ h a − b + γ ​ c. g=h+\frac{c\omega^{-1}(1+h)+L_{\mathcal{X}}h}{a-b+\gamma c}. |  |

It follows from Lemmas 5.3 and 5.7 that g g is a 𝒞 k − 1 {\mathcal{C}}^{k-1} -function on monomials, of order o ⁡ ( 1). o(1). ∎

We want to use the algorithm of division-derivation in order to prove the following result:

###### Theorem 5.8.

Let V ⁡ ( r, ρ, λ) V(r,\rho,\lambda) be a function on 𝒜 × ℬ ∩ { r > 0, ρ > 0 }, \mathcal{A}\times\mathcal{B}\cap\{r>0,\ \rho>0\}, of the form

 | V ⁡ ( r, ρ, λ) = ∑ i = 1 l A i ​ ( λ) ​ M i ​ ( 1 + g i ​ ( r, ρ, λ)), V(r,\rho,\lambda)=\sum_{i=1}^{l}A_{i}(\lambda)M_{i}\Big(1+g_{i}(r,\rho,\lambda)\Big), |  | (5.4) |

where:

1. 1.

the leading monomials M i = r a i ​ ρ b i ​ ω c i M_{i}=r^{a_{i}}\rho^{b_{i}}\omega^{c_{i}} are general monomials, without Ω \Omega -factor ( ω = ( ω j) j, \omega=(\omega_{j})_{j}, c i = ( c i j) j c_{i}=(c_{i}^{j})_{j} with j ∈ J, j\in J, a finite set),

2. 2.

the functions g i g_{i} are 𝒞 k {\mathcal{C}}^{k} -functions on monomials, with k ≥ l, k\geq l, and of order o ⁡ ( 1), o(1),

3. 3.

the functions A i ​ ( λ) A_{i}(\lambda) are continuous,

4. 4.

the monomials M j ​ M i − 1 M_{j}M_{i}^{-1} for i ≠ j i\not=j are non-resonant, i.e.

 | a j 0 − a i 0 − b j 0 + b i 0 ≠ 0 for i ≠ j. a_{j}^{0}-a_{i}^{0}-b_{j}^{0}+b_{i}^{0}\not=0\ \ \mathrm{for}\ \ i\not=j. |  | (5.5) |

Then, if 𝒜 × ℬ \mathcal{A}\times\mathcal{B} is chosen sufficiently small,

i) either the function V V has at most l − 1 l-1 isolated roots counted with their multiplicity, on each curve l ν = { r ρ = ν } ⊂ 𝒜, l_{\nu}=\{r\rho=\nu\}\subset\mathcal{A},

ii) or V V is identically zero.

###### Proof.

We suppose that V V is defined for λ ∈ ℬ \lambda\in\mathcal{B} (some neighborhood of OPEN λ 0) \lambda_{0}) and we define the following closed subsets:

 | ℬ i = { λ ∈ ℬ | A i ( λ) ≥ A j ( λ), ∀ j = 1, …, l }. \mathcal{B}_{i}=\{\lambda\in\mathcal{B}\ |\ A_{i}(\lambda)\geq A_{j}(\lambda),\forall j=1,\ldots,l\}. |  |

Of course we have ℬ = ∪ i ℬ i \mathcal{B}=\cup_{i}\mathcal{B}_{i}, and it is sufficient to prove the result for any ℬ i \mathcal{B}_{i} (and ℬ \mathcal{B} sufficiently small). Then let us pick any i = 1, …, l. i=1,\ldots,l. By reordering the indices, we can suppose that we have picked i = l. i=l.

The algorithm of division-derivation consists in the production of a sequence of functions: V 0 = V, V 1, …, V l − 1, V_{0}=V,V_{1},\ldots,V_{l-1}, such that each V j V_{j} is a summation similar to V V but only on l − j l-j terms, and is defined on a smaller neighborhood 𝒜 j × ℬ j \mathcal{A}^{j}\times\mathcal{B}^{j} of ( 0, 0, λ 0). (0,0,\lambda_{0}).

To define V 1, V_{1}, we first divide V V by M 1 ​ ( 1 + g 1) M_{1}(1+g_{1}) (a division step). This is made on a neighborhood 𝒜 1 × ℬ 1 ⊂ 𝒜 × ℬ \mathcal{A}^{1}\times\mathcal{B}^{1}\subset\mathcal{A}\times\mathcal{B} chosen such that 1 + g 1 ​ ( r, ρ, λ) ≠ 0 1+g_{1}(r,\rho,\lambda)\not=0 for all ( r, ρ, λ) ∈ 𝒜 1 × ℬ 1. (r,\rho,\lambda)\in\mathcal{A}^{1}\times\mathcal{B}^{1}. On this neigborhood we consider the function:

 | V M 1 ​ ( 1 + g 1) = A 1 + ∑ i = 2 k A i ​ M i ​ M 1 − 1 ​ ( 1 + g ~ i), \frac{V}{M_{1}(1+g_{1})}=A_{1}+\sum_{i=2}^{k}A_{i}M_{i}M_{1}^{-1}\Big(1+\tilde{g}_{i}\Big), |  |

where the function g ~ i, \tilde{g}_{i}, defined by 1 + g ~ i = 1 + g i 1 + g 1, 1+\tilde{g}_{i}=\frac{1+g_{i}}{1+g_{1}}, is 𝒞 k {\mathcal{C}}^{k} on monomials and of order o ⁡ ( 1). o(1).

Next we apply the operator L 𝒳 L_{\mathcal{X}} (a derivation step). Since the monomials M i ​ M 1 − 1 M_{i}M_{1}^{-1} are non resonant for i ≠ 1, i\not=1, we can apply Lemma 5.7 to obtain the following function V 1 V_{1} on 𝒜 1 × ℬ 1 \mathcal{A}^{1}\times\mathcal{B}^{1}:

 | V 1 = L 𝒳 ​ [V M 1 ​ ( 1 + g 1)] = ∑ i = 2 l ( a i − a 1 − b i + b 1) ​ A i ​ M i ​ M 1 − 1 ​ ( 1 + g i 1 ​ ( y, z)), V_{1}=L_{\mathcal{X}}\Big[\frac{V}{M_{1}(1+g_{1})}\Big]=\sum_{i=2}^{l}(a_{i}-a_{1}-b_{i}+b_{1})A_{i}M_{i}M_{1}^{-1}\Big(1+g_{i}^{1}(y,z)\Big), |  |

with the function g i 1 g_{i}^{1}, 𝒞 k {\mathcal{C}}^{k} on monomials and of order o ⁡ ( 1). o(1). The effect of the derivation is to kill the first term A 1 A_{1}, thus reducing by one the number of terms in the summation. Except from this fact, the terms of the summation are completely similar to the ones in V V, but with the functions A i A_{i} replaced by ( a i − a 1 − b i + b 1) ​ A i (a_{i}-a_{1}-b_{i}+b_{1})A_{i}, and the monomials M i M_{i} replaced by the monomials M i ​ M 1 − 1. M_{i}M_{1}^{-1}.

For the recurrence step of order j + 1 = 1, …, k − 1, j+1=1,\ldots,k-1, we assume that we have a function:

 | V j = ∑ i = j + 1 l ( ∏ m = 1 j ( a i − b i − a m + b m)) ​ A i ​ ( λ) ​ M i ​ M j − 1 ​ ( 1 + g i j), V_{j}=\sum_{i=j+1}^{l}\Big(\prod_{m=1}^{j}(a_{i}-b_{i}-a_{m}+b_{m})\Big)A_{i}(\lambda)M_{i}M_{j}^{-1}\Big(1+g_{i}^{j}\Big), |  |

defined on some neighborhood 𝒜 j × ℬ j \mathcal{A}^{j}\times\mathcal{B}^{j} with functions g i j, g_{i}^{j}, 𝒞 k − j {\mathcal{C}}^{k-j} on monomials and of order o ⁡ ( 1). o(1). As in the first step from V V to V 1, V_{1}, we divide V j V_{j} by M j + 1 ​ M j − 1 ​ ( 1 + g j + 1 j), M_{j+1}M_{j}^{-1}\Big(1+g_{j+1}^{j}\Big), which is possible on some neighborhood 𝒜 j + 1 × ℬ j + 1 ⊂ 𝒜 j × ℬ j, \mathcal{A}^{j+1}\times\mathcal{B}^{j+1}\subset\mathcal{A}^{j}\times\mathcal{B}^{j}, and next apply the differential operator L 𝒳 L_{\mathcal{X}} to produce a function

 | V j + 1 = ∑ i = j + 2 l ( ∏ m = 1 j + 1 ( a i − b i − a m + b m)) ​ A i ​ ( λ) ​ M i ​ M j + 1 − 1 ​ ( 1 + g i j + 1), V_{j+1}=\sum_{i=j+2}^{l}\Big(\prod_{m=1}^{j+1}(a_{i}-b_{i}-a_{m}+b_{m})\Big)A_{i}(\lambda)M_{i}M_{j+1}^{-1}\Big(1+g_{i}^{j+1}\Big), |  |

where the g i j + 1 g_{i}^{j+1} are 𝒞 k − j − 1 {\mathcal{C}}^{k-j-1} on monomials and of order o ⁡ ( 1). o(1).

Performing the l − 1 l-1 steps of the recurrence, we end up with a function

 | V l − 1 = ( a l − b l − a 1 + b 1) ⋯ ( a l − b l − a l − 1 + b l − 1) A l ( λ) M l M l − 1 − 1 ( 1 + g l l), V_{l-1}=(a_{l}-b_{l}-a_{1}+b_{1})\cdots(a_{l}-b_{l}-a_{l-1}+b_{l-1})A_{l}(\lambda)M_{l}M_{l-1}^{-1}\Big(1+g_{l}^{l}\Big), |  |

where g l l g_{l}^{l} is 𝒞 k − l {\mathcal{C}}^{k-l} on monomials and of order o ⁡ ( 1). o(1).

As g l l = o ⁡ ( 1), g^{l}_{l}=o(1), and at least 𝒞 0 {\mathcal{C}}^{0} on monomials, we can choose a last neighborhood 𝒜 l × ℬ l ⊂ 𝒜 l − 1 × ℬ l − 1, \mathcal{A}^{l}\times\mathcal{B}^{l}\subset\mathcal{A}^{l-1}\times\mathcal{B}^{l-1}, such that the function 1 + g l l 1+g_{l}^{l} is nowhere zero on it. We restrict now λ ∈ W l = ℬ l ∩ ℬ l. \lambda\in W_{l}=\mathcal{B}^{l}\cap\mathcal{B}_{l}. On this set we have the following alternative: A l ​ ( λ) ≠ 0 A_{l}(\lambda)\not=0 or A 1 ​ ( λ) = ⋯ = A l ​ ( λ) = 0. A_{1}(\lambda)=\cdots=A_{l}(\lambda)=0. In the last case, the function V V is identical to 0 0 and has no isolated roots.

Then we just have to look at values λ \lambda where A l ​ ( λ) ≠ 0. A_{l}(\lambda)\not=0. For such a value of λ, \lambda, the function V l − 1 V_{l-1} itself is nowhere zero on 𝒜 l × W. \mathcal{A}^{l}\times W. Consider now any curve l ν l_{\nu} in 𝒜 l. \mathcal{A}^{l}. Recall that the derivation L 𝒳 L_{\mathcal{X}} of a function G G corresponds to the derivation of G G along the flow of 𝒳 {\mathcal{X}} and that l ν l_{\nu} is an orbit of this vector field. Then, as V l − 1 V_{l-1} is equal to the derivation of V l − 2, V_{l-2}, up to a non-zero function, Rolle’s Theorem applied to V l − 2, V_{l-2}, implies that the restriction of this function to l ν, l_{\nu}, has at most one root (let us notice that ł ν \l_{\nu} is connected!). The same argument based on Rolle’s Theorem can be applied by recurrence to obtain for each j ≤ l, j\leq l, that the function V l − j V_{l-j} has at most j − 1 j-1 roots, counted with their multiplicity. Finally, the function V V has at most l − 1 l-1 roots counted with their multiplicity on ł ν ∩ 𝒜 l, \l_{\nu}\cap\mathcal{A}^{l}, for λ ∈ W l. \lambda\in W_{l}.

We obtain the result by considering in the same way the different subsets ℬ i. \mathcal{B}_{i}. ∎

###### Remark 5.9.

1. 1.

Even if V V is a summation on admissible monomials, it is clear that, in general, the division step may produce general monomials. This is the reason why we begin with general monomials in ( 5.4).

2. 2.

Using the first integral r ​ ρ = ν, r\rho=\nu, we can rewrite the leading monomial M i M_{i} in the form M i = ν b i ​ r a i − b i ​ ω c i; M_{i}=\nu^{b_{i}}r^{a_{i}-b_{i}}\omega^{c_{i}}; We call M ¯ i = r a i − b i ​ ω c i \bar{M}_{i}=r^{a_{i}-b_{i}}\omega^{c_{i}} a reduced monomial. The sum ( 5.4) may be written in reduced form, with p i = a i − b i p_{i}=a_{i}-b_{i}:

 | V ⁡ ( r, ρ, λ) = ∑ i = 1 l ν b i ​ A i ​ ( λ) ​ r p i ​ ω c i ​ ( 1 + g i ​ ( r, ρ, λ)), V(r,\rho,\lambda)=\sum_{i=1}^{l}\nu^{b_{i}}A_{i}(\lambda)r^{p_{i}}\omega^{c_{i}}\Big(1+g_{i}(r,\rho,\lambda)\Big), |  | (5.6) |

3. 3.

The non-resonance condition ( 5.5) in Theorem 5.8 is equivalent to the condition that the p i ​ ( λ 0) = p i 0 p_{i}(\lambda_{0})=p_{i}^{0} in ( 5.6) are two by two distinct. Up to a change of indices and a reordering, we can suppose in this case that p 1 0 < p 2 0 ⋯ < p l 0 p_{1}^{0}<p_{2}^{0}\cdots<p_{l}^{0}. Let us note that some of p i 0 p_{i}^{0} may be negative, and also that one of them may be equal to zero.

### 5.3 The results of finite cyclicity for the boundary limit periodic set

We now want to apply Theorem 5.8 to the displacement function V V in the text. We write σ ¯ 3 = σ 0 + α. \bar{\sigma}_{3}=\sigma_{0}+\alpha. After putting this function in the reduced form ( 5.5), we have the following.

1. 1.

In the case σ 0 ∉ ℕ \sigma_{0}\not\in\mathbb{N}, the function V V is given in ( 3.19) and we have the sequence of monomials: { 1, r σ 0 + α, r σ 0 − 1 + α } \{1,r^{\sigma_{0}+\alpha},r^{\sigma_{0}-1+\alpha}\}. This allows applying Theorem 5.8, yielding that the boundary limit periodic set is at most 2 2.

2. 2.

In the case σ 0 = p ∈ ℕ, \sigma_{0}=p\in\mathbb{N}, the function V V is given in ( 3.25) or ( 3.26), and the sequence of monomials is: { 1, r p + α, r p − 1 + α, r α ​ ω α }. \{1,r^{p+\alpha},r^{p-1+\alpha},r^{\alpha}\omega_{\alpha}\}. We have two resonant leading monomials when p ≠ 1 p\not=1, and even 3 3 when p = 1. p=1. Theorem 5.8 does not apply in none of these cases.

Hence, we give a direct proof for σ 0 ∈ ℕ, \sigma_{0}\in\mathbb{N}, using exactly the same procedure of derivation-division as in Theorem 5.8, but based on a more refined estimation than the formula ( 5.3) used to prove Theorem 5.8. Recall that the parameter was called M M in this context. It will not be sufficient to consider the leading reduced monomials for M = M 0 M=M_{0}, and we will have to look more precisely at the form of certain remainders.

We need the following result:

###### Lemma 5.10.

 | L 𝒳 ​ [r α ​ ω α ​ ( 1 + O ⁡ ( r δ))] = − r α ​ ( 1 + O ⁡ ( r δ)), L_{\mathcal{X}}\Big[r^{\alpha}\omega_{\alpha}\Big(1+O(r^{\delta})\Big)\Big]=-r^{\alpha}\Big(1+O(r^{\delta})\Big), |  | (5.7) |

###### Proof.

We have that L 𝒳 ​ [r α ​ ω α ​ ( 1 + O ⁡ ( r δ))] = L 𝒳 ​ [r α ​ ω α] ​ ( 1 + O ⁡ ( r δ)) + r α ​ ω α ​ O ​ ( r δ). L_{\mathcal{X}}\Big[r^{\alpha}\omega_{\alpha}\Big(1+O(r^{\delta})\Big)\Big]=L_{\mathcal{X}}\Big[r^{\alpha}\omega_{\alpha}\Big](1+O(r^{\delta}))+r^{\alpha}\omega_{\alpha}O(r^{\delta}). Now, L 𝒳 ​ [r α ​ ω α] = α ​ r α ​ ω α − r α ​ r − α. L_{\mathcal{X}}\Big[r^{\alpha}\omega_{\alpha}\Big]=\alpha r^{\alpha}\omega_{\alpha}-r^{\alpha}r^{-\alpha}. As r − α = 1 + α ​ ω α, r^{-\alpha}=1+\alpha\omega_{\alpha}, we have that L 𝒳 ​ [r α ​ ω α] = − r α. L_{\mathcal{X}}\Big[r^{\alpha}\omega_{\alpha}\Big]=-r^{\alpha}. Since r α ​ ω α ​ O ​ ( r δ) r^{\alpha}\omega_{\alpha}O(r^{\delta}) is of order O ⁡ ( r δ) O(r^{\delta}) (for a smaller δ \delta), we obtain ( 5.7) by grouping the terms. ∎

###### Remark 5.11.

The formula ( 5.7) is wrong in general if we replace the remainder by the more general remainder o ⁡ ( 1). o(1). Let us consider for instance the expression f = r α ​ ω α ​ ( 1 + ρ). f=r^{\alpha}\omega_{\alpha}(1+\rho). We have that L 𝒳 ​ f = − r α ​ ( 1 + ρ) − r α ​ ω α ​ ρ = − r α ​ ( 1 + ρ + ω α ​ ρ). L_{\mathcal{X}}f=-r^{\alpha}(1+\rho)-r^{\alpha}\omega_{\alpha}\rho=-r^{\alpha}(1+\rho+\omega_{\alpha}\rho). The term ω α ​ ρ \omega_{\alpha}\rho is not of order o ⁡ ( 1). o(1).

Let 𝒜, ℬ \mathcal{A},\mathcal{B} be neighborhoods defined as above. First we have the following result when σ 0 ≠ 1 \sigma_{0}\not=1:

###### Theorem 5.12.

Consider the case σ 0 = p ∈ ℕ \sigma_{0}=p\in\mathbb{N}, with p ≠ 1. p\not=1. Then the cyclicity of the boundary limit periodic set is at most 3 3, namely for sufficiently small neighborhoods 𝒜 \mathcal{A} and ℬ \mathcal{B}, the equation V ⁡ ( r, ρ, M) = 0 V(r,\rho,M)=0 has at most 3 3 roots, counted with their multiplicities, on each curve l ν ⊂ 𝒜. l_{\nu}\subset\mathcal{A}.

###### Proof.

Recall that the displacement map V V is given by

 | V ( r, ρ) = ∗ ε 0 ( 1 + h 0) + ∗ ε 1 r p + α ( 1 + h 1) + ∗ μ ¯ 3 ν r p − 1 + α ( 1 + h 2) + ∗ K ( M) ν p r α ω α. V(r,\rho)=*\varepsilon_{0}(1+h_{0})+*\varepsilon_{1}r^{p+\alpha}(1+h_{1})+*\bar{\mu}_{3}\nu r^{p-1+\alpha}(1+h_{2})+*K(M)\nu^{p}r^{\alpha}\omega_{\alpha}. |  | (5.8) |

The sequence of leading monomials in ( 5.8) does not verify the condition of non-resonance. To overcome this difficulty, we will use that there is no remainder in the last term, and that h 0 h_{0} is of order O ⁡ ( r δ). O(r^{\delta}). For h 1 h_{1} and h 2 h_{2}, it will be sufficient to know that they are o ⁡ ( 1). o(1).

As in the proof of Theorem 5.8, we define the partition ℬ = ℬ 1 ∪ ℬ 2 ∪ ℬ 3 ∪ ℬ 4 \mathcal{B}=\mathcal{B}_{1}\cup\mathcal{B}_{2}\cup\mathcal{B}_{3}\cup\mathcal{B}_{4} in terms of the coefficients in ( 5.8). At each step we will have to restrict the size of ℬ. \mathcal{B}. We will not recall it.

As the three last leading monomials in ( 5.8) are o ⁡ ( 1), o(1), the cyclicity is trivially 0 0 when M ∈ ℬ 1. M\in\mathcal{B}_{1}. We suppose now that M ∈ ℬ 2 ∪ ℬ 3 ∪ ℬ 4. M\in\mathcal{B}_{2}\cup\mathcal{B}_{3}\cup\mathcal{B}_{4}. Using ( 5.7), we obtain:

 | L 𝒳 V 1 + h 0 = ∗ ε 1 r p + α ( 1 + g 1) + ∗ μ ¯ 3 ν r p − 1 + α ( 1 + g 2) + ∗ K ( M) ν p r α. L_{\mathcal{X}}\frac{V}{1+h_{0}}=*\varepsilon_{1}r^{p+\alpha}(1+g_{1})+*\bar{\mu}_{3}\nu r^{p-1+\alpha}(1+g_{2})+*K(M)\nu^{p}r^{\alpha}. |  |

Now, the sequence of leading monomials { r p + α, r p − 1 + α, r α } \{r^{p+\alpha},r^{p-1+\alpha},r^{\alpha}\} verifies the condition of non-resonance and we can apply Theorem 5.8 to L 𝒳 ​ V 1 + h 0. L_{\mathcal{X}}\frac{V}{1+h_{0}}. Then, this function has at most 2 2 roots, and the function V V itself has at most 3 3 roots, when M ∈ ℬ 2 ∪ ℬ 3 ∪ ℬ 4. M\in\mathcal{B}_{2}\cup\mathcal{B}_{3}\cup\mathcal{B}_{4}. ∎

Finally, we have

###### Theorem 5.13.

Consider the case σ 0 = 1. \sigma_{0}=1. Then the cyclicity of the boundary limit periodic set is at most 2 2.

###### Proof.

We can start with the formula ( 5.8) which is valid for any p ∈ ℕ. p\in\mathbb{N}. Moreover, for p = 1 p=1 we have that K ( M) = η 4 ( ν) − η 3 ( ν) ( 1 + ε 1) = ∗ μ ¯ 3 + O ( ν) O P ( M C). K(M)=\eta_{4}(\nu)-\eta_{3}(\nu)(1+\varepsilon_{1})=*\bar{\mu}_{3}+O(\nu)O_{P}(M_{C}). This is a direct consequence of the fact that the linear part of the system at the points P 3 P_{3} and P 4 P_{4} is given, up to a constant, by r ˙ = r, ρ ˙ = − ρ, y ¯ ˙ = − σ ⁡ ( y ¯ + μ ¯ 3 ​ ρ). \dot{r}=r,\ \dot{\rho}=-\rho,\ \dot{\bar{y}}=-\sigma(\bar{y}+\bar{\mu}_{3}\rho). Then, we can split the last term in ( 5.8) as the sum ∗ μ ¯ 3 ​ ν ​ r α ​ ω α + ν ​ r α ​ ω α ​ O ​ ( ν) ​ O P ​ ( M C). *\bar{\mu}_{3}\nu r^{\alpha}\omega_{\alpha}+\nu r^{\alpha}\omega_{\alpha}O(\nu)O_{P}(M_{C}). The second term gives contributions of order O ⁡ ( r δ) O(r^{\delta}) in h 0, h 1 h_{0},h_{1} and h 2 h_{2}, and produces a remainder h 3 h_{3} of order O ⁡ ( r δ) O(r^{\delta}) for the last leading monomial r α ​ ω α. r^{\alpha}\omega_{\alpha}.

Then, for p = 1, p=1, the displacement map V V takes the form:

 | V ( r, ρ) = ∗ ε 0 ( 1 + h 0) + ∗ ε 1 r 1 + α ( 1 + h 1) + ∗ μ ¯ 3 ν r α ( 1 + h 2) + ∗ μ ¯ 3 ν r α ω α ( 1 + h 3) V(r,\rho)=*\varepsilon_{0}(1+h_{0})+*\varepsilon_{1}r^{1+\alpha}(1+h_{1})+*\bar{\mu}_{3}\nu r^{\alpha}(1+h_{2})+*\bar{\mu}_{3}\nu r^{\alpha}\omega_{\alpha}(1+h_{3}) |  | (5.9) |

The sequence of leading monomials in ( 5.9) does not verify the condition of non-resonance. To overcome this difficulty, we will use that h 0 h_{0} and h 3 h_{3} are of order O ⁡ ( r δ). O(r^{\delta}). It will be sufficient to know that h 1 h_{1} and h 2 h_{2} are o ⁡ ( 1). o(1).

As in the proof of Theorem 5.12, the cyclicity is 0 0 if | ε 0 | ≥ max ⁡ { | ε 1 |, | μ ¯ 3 | }. |\varepsilon_{0}|\geq\mathrm{max}\{|\varepsilon_{1}|,|\bar{\mu}_{3}|\}.

Otherwise, let us consider L 𝒳 ​ V 1 + h 0. L_{\mathcal{X}}\frac{V}{1+h_{0}}. Using ( 5.7), we have that

 | L 𝒳 V 1 + h 0 = ∗ ε 1 r 1 + α ( 1 + g 1) + ∗ μ ¯ 3 ν [α r α ( 1 + h 2) + r α L 𝒳 h 2] + ∗ μ ¯ 3 ν r α ( 1 + g 3), L_{\mathcal{X}}\frac{V}{1+h_{0}}=*\varepsilon_{1}r^{1+\alpha}(1+g_{1})+*\bar{\mu}_{3}\nu\Big[\alpha r^{\alpha}(1+h_{2})+r^{\alpha}L_{\mathcal{X}}h_{2}\Big]+*\bar{\mu}_{3}\nu r^{\alpha}(1+g_{3}), |  |

with g 3 g_{3} of order O ⁡ ( r δ). O(r^{\delta}). Grouping the different terms, we obtain

 | L 𝒳 V 1 + h 0 = r 1 + α [∗ ε 1 ( 1 + g 1) + ∗ μ ¯ 3 ρ ( 1 + ∗ α + g 4)], L_{\mathcal{X}}\frac{V}{1+h_{0}}=r^{1+\alpha}\Big[*\varepsilon_{1}(1+g_{1})+*\bar{\mu}_{3}\rho(1+*\alpha+g_{4})\Big], |  |

where g 4 = ∗ α h 2 + L 𝒳 h 2 + g 3 g_{4}=*\alpha h_{2}+L_{\mathcal{X}}h_{2}+g_{3} is of order o ⁡ ( 1). o(1). Now, the sequence of leading monomials { 1, ρ } \{1,\rho\} verifies the condition of non-resonance and we can apply Theorem 5.8 to r − 1 − α ​ L 𝒳 ​ V 1 + h 0. r^{-1-\alpha}L_{\mathcal{X}}\frac{V}{1+h_{0}}. This function has at most 1 1 root, yielding that V V itself has at most 2 2 roots, if | ε 0 | ≤ max ⁡ { | ε 1 |, | μ ¯ 3 | }. |\varepsilon_{0}|\leq\mathrm{max}\{|\varepsilon_{1}|,|\bar{\mu}_{3}|\}. ∎

## 6 Appendix III

###### Lemma 6.1.

The parameter function ε 0 {\varepsilon}_{0} in the expression of the displacement map V V has the form ( 3.16) for system ( 3.3).

###### Proof.

Since the system has an invariant parabola for μ 0 = μ 2 = μ 3 = μ 4 = 0 \mu_{0}=\mu_{2}=\mu_{3}=\mu_{4}=0, it suffices to make the calculation for μ 0 = μ 2 = μ 3 = μ 5 = 0 \mu_{0}=\mu_{2}=\mu_{3}=\mu_{5}=0. The system is integrable when μ 4 = 0 \mu_{4}=0, with integrating factor ( 1 + y) 3 (1+y)^{3}. Hence, it suffices to show that the following Melnikov integral is a nonzero multiple of μ 4 \mu_{4}. Indeed,

 | ∫ y = 1 2 ​ x 2 − 1 2 μ 4 x 2 ( 1 + y) 3 d x = ∫ − ∞ ∞ 8 μ 4 x 2 ( 1 + x 2) 3 d x = ∗ μ 4. \int_{y=\frac{1}{2}x^{2}-\frac{1}{2}}\mu_{4}\frac{x^{2}}{(1+y)^{3}}\,dx=\int_{-\infty}^{\infty}8\mu_{4}\frac{x^{2}}{(1+x^{2})^{3}}\,dx=*\mu_{4}. |  |

∎

###### Lemma 6.2.

The parameter function ε 1 {\varepsilon}_{1} in the expression of the displacement map V V has the form ( 3.17) for both systems ( 3.2) and ( 3.3).

###### Proof.

It has been proved in [3] (see for instance Theorem 3.5) that it suffices to show that ∫ div d t = ∗ μ 5 \int\mathrm{div}\,dt=*\mu_{5} along the invariant parabola when all parameters but μ 5 \mu_{5} vanish. Two different calculations are needed for the cases ( 3.2) and ( 3.3). In the first case, the invariant parabola is given by ( 3.4). Then,

 | ∫ div ​ 𝑑 t = lim X 0 → ∞ ∫ − X 0 X 0 ( 2 ​ B + 1) ​ x + ( 1 − B) ​ μ 5 − y + B ​ x 2 + B ​ μ 5 ​ x ​ 𝑑 x = lim X 0 → ∞ ( ( 2 ​ B + 1) ​ ln ⁡ 1 + B ​ ( X 0 + ( B − 1) ​ μ 5) 2 + o ⁡ ( μ 5) 1 + B ​ ( X 0 − ( B − 1) ​ μ 5) 2 + o ⁡ ( μ 5) CLOSE OPEN + 2 ​ B 3 / 2 ​ ( B − 1) ​ μ 5 ​ ( arctan ⁡ ( B ​ ( X 0 + O ⁡ ( μ 5))) − arctan ⁡ ( B ​ ( − X 0 + O ⁡ ( μ 5))))) = 2 ​ B 3 / 2 ​ ( B − 1) ​ π ​ μ 5 + o ⁡ ( μ 5). \displaystyle\begin{split}\int\mathrm{div}\,dt&=\lim_{X_{0}\to\infty}\int_{-X_{0}}^{X_{0}}\frac{(2B+1)x+(1-B)\mu_{5}}{-y+Bx^{2}+B\mu_{5}x}\,dx\\ &=\lim_{X_{0}\to\infty}\left((2B+1)\ln\frac{1+B(X_{0}+(B-1)\mu_{5})^{2}+o(\mu_{5})}{1+B(X_{0}-(B-1)\mu_{5})^{2}+o(\mu_{5})}\right.\\ &\qquad\left.+2B^{3/2}(B-1)\mu_{5}\left(\arctan\left(\sqrt{B}(X_{0}+O(\mu_{5}))\right)-\arctan\left(\sqrt{B}(-X_{0}+O(\mu_{5}))\right)\right)\right)\\ &=2B^{3/2}(B-1)\pi\mu_{5}+o(\mu_{5}).\end{split} |  |

The second case of ( 3.3) is easier since the invariant parabola y = 1 2 ​ x 2 + 1 2 y=\frac{1}{2}x^{2}+\frac{1}{2} is independent of μ 5 \mu_{5}. Then

 | ∫ y = 1 2 ​ x 2 + 1 2 div ​ 𝑑 t = ∫ − ∞ ∞ 2 ​ μ 5 ​ d ​ x x 2 + 1 = 2 ​ π ​ μ 5. \int_{y=\frac{1}{2}x^{2}+\frac{1}{2}}\mathrm{div}\,dt=\int_{-\infty}^{\infty}2\mu_{5}\frac{dx}{x^{2}+1}=2\pi\mu_{5}. |  |

∎

###### Lemma 6.3.

The second derivative of the map S = ρ ​ F ​ ( 0, ρ) S=\rho F(0,\rho), where F F is defined in ( 3.18) is a nonzero multiple of μ ¯ 3 \overline{\mu}_{3}.

###### Proof.

We first localize the system ( 3.2) at the nilpotent point at infinity using the coordinates ( v, w) = ( − x y, 1 y) (v,w)=(-\frac{x}{y},\frac{1}{y}): after mutiplication by w w, this yields

 | v ˙ = w + ( 1 − B) ​ v 2 − μ 2 − μ 3 ​ v + v ​ w ​ ( ( 3 ​ B − 1) ​ μ 5 + μ 4) + v 2 ​ w, w ˙ = v ​ w − μ 3 ​ w − ( 1 − 2 ​ B) ​ μ 5 ​ w 2 + v ​ w 2. \displaystyle\begin{split}\dot{v}&=w+(1-B)v^{2}-\mu_{2}-\mu_{3}v+vw((3B-1)\mu_{5}+\mu_{4})+v^{2}w,\\ \dot{w}&=vw-\mu_{3}w-(1-2B)\mu_{5}w^{2}+vw^{2}.\end{split} |  | (6.1) |

A similar localization can be done for ( 3.3). We now let the blow-up ( v, w) = ( r ​ x ¯, r 2) (v,w)=(r\overline{x},r^{2}) for w > 0 w>0, and we consider the restriction of the blow-up system to the ( ρ, x ¯) (\rho,\overline{x}) -plane for r = 0 r=0, (after multiplication by 2 2)

 | ρ ˙ = − ρ ⁡ ( x ¯ − μ ¯ 3 ​ ρ) = P ⁡ ( ρ, x ¯), x ¯ ˙ = 2 + ( 1 − 2 ​ B) ​ x ¯ 2 − 2 ​ μ ¯ 2 ​ ρ 2 − μ ¯ 3 ​ x ¯ ​ ρ = Q ⁡ ( ρ, x ¯). \displaystyle\begin{split}\dot{\rho}&=-\rho(\overline{x}-\overline{\mu}_{3}\rho)=P(\rho,\overline{x}),\\ \dot{\overline{x}}&=2+(1-2B)\overline{x}^{2}-2\overline{\mu}_{2}\rho^{2}-\overline{\mu}_{3}\overline{x}\rho=Q(\rho,\overline{x}).\end{split} |  |

Note that this system is the same for ( 3.2) and ( 3.3). The singular points occur at x ¯ = ± β \overline{x}=\pm\beta with β = 2 2 ​ B − 1 \beta=\sqrt{\frac{2}{2B-1}}. We localize at P 3 P_{3} using x 3 = β − x ¯ x_{3}=\beta-\overline{x} and at P 4 P_{4} using x 4 = β + x ¯ x_{4}=\beta+\overline{x}. Hence, the system at P 4 P_{4} is obtained from that at P 3 P_{3} through ( x 3, β) ↦ ( − x 4, − β) (x_{3},\beta)\mapsto(-x_{4},-\beta). The map is between two sections { x ¯ i = X 0 } \{\overline{x}_{i}=X_{0}\} in the normal form coordinates x ¯ i \overline{x}_{i} near P i P_{i} and we take X 0 X_{0} small. The section { x ¯ 4 = X 0 } \{\overline{x}_{4}=X_{0}\} (resp { x ¯ 3 = X 0 } \{\overline{x}_{3}=X_{0}\}) has equation x ¯ = f 4 ​ ( ρ) = − x 0 + O ⁡ ( ρ) \overline{x}=f_{4}(\rho)=-x_{0}+O(\rho) (resp. x ¯ = f 3 ​ ( ρ) = x 0 + O ⁡ ( ρ) \overline{x}=f_{3}(\rho)=x_{0}+O(\rho)). A formula for the second derivative was given in [8] (Proposition 5.2), namely

 | S ′′ ​ ( 0) = S ′ ( 0) [2 ( f 4 ′ ( 0) S ′ ( 0) ( P ρ ′ Q) ( 0, f 4 ( 0)) − f 3 ′ ( 0) ( P ρ ′ Q) ( 0, f 3 ( 0))) + ∫ f 3 ​ ( 0) f 4 ​ ( 0) ( P ρ ​ ρ ′′ Q ( 0, x ¯) − 2 P ρ ′ ​ Q ρ ′ Q 2 ( 0, x ¯)) exp ( ∫ f 3 ​ ( 0) x ¯ ( P ρ ′ Q) ( 0, x) d x) d x ¯]. \displaystyle\begin{split}S^{\prime\prime}(0)&=S^{\prime}(0)\left[2\left(f_{4}^{\prime}(0)S^{\prime}(0)\left(\frac{P_{\rho}^{\prime}}{Q}\right)(0,f_{4}(0))-f_{3}^{\prime}(0)\left(\frac{P_{\rho}^{\prime}}{Q}\right)(0,f_{3}(0))\right)\right.\\ &\qquad+\left.\int_{f_{3}(0)}^{f_{4}(0)}\left(\frac{P_{\rho\rho}^{\prime\prime}}{Q}(0,\overline{x})-2\frac{P_{\rho}^{\prime}Q_{\rho}^{\prime}}{Q^{2}}(0,\overline{x})\right)\exp\left(\int_{f_{3}(0)}^{\overline{x}}\left(\frac{P_{\rho}^{\prime}}{Q}\right)(0,x)dx\right)d\overline{x}\right].\end{split} |  | (6.2) |

Here, S ′ ​ ( 0) = 1 S^{\prime}(0)=1. We call the three terms in the bracket 2 ​ I 1 2I_{1}, 2 ​ I 2 2I_{2} and I 3 I_{3}. Let us first consider I 3 I_{3}.

 | I 3 = 4 ​ μ ¯ 3 ​ ( 2 + ( 1 − 2 ​ B) ​ x 0 2) 1 2 ​ ( 1 − 2 ​ B) ​ ∫ x 0 − x 0 ( 1 − B ​ x ¯ 2) ​ ( 2 + ( 1 − 2 ​ B) ​ x ¯ 2) 8 ​ B − 5 2 ​ ( 1 − 2 ​ B) ​ 𝑑 x ¯. I_{3}=4\overline{\mu}_{3}(2+(1-2B)x_{0}^{2})^{\frac{1}{2(1-2B)}}\int_{x_{0}}^{-x_{0}}(1-B\overline{x}^{2})(2+(1-2B)\overline{x}^{2})^{\frac{8B-5}{2(1-2B)}}d\overline{x}. |  | (6.3) |

There are two different cases for f j ′ ​ ( 0) f_{j}^{\prime}(0) depending whether B 0 = 3 4 B_{0}=\frac{3}{4} or not.

The case B 0 = 3 4 B_{0}=\frac{3}{4}. In this case, the singular point has equal eigenvalues and a Jordan normal form for nonzero μ ¯ 3 \overline{\mu}_{3}. Hence, the change of coordinate to normal form is tangent to the identity and f 3 ′ ​ ( 0), f 4 ′ ​ ( 0) = O ⁡ ( μ ¯ 3) ​ O ​ ( X 0) f_{3}^{\prime}(0),f_{4}^{\prime}(0)=O(\overline{\mu}_{3})O(X_{0}). Also the integral part of I 3 I_{3} in ( 6.3) is equal to − 2 ​ ( 3 2 ​ x 0 − ln ⁡ 2 + x 0 2 − x 0) ≠ 0 -2\left(\frac{3}{2}x_{0}-\ln\frac{2+x_{0}}{2-x_{0}}\right)\not=0. The result follows in that case.

The case B 0 ≠ 3 4 B_{0}\neq\frac{3}{4}. In this case, the change of coordinates to normal form is given by x ¯ = β − ( x ¯ 3 − μ ¯ 3 3 − 4 ​ B ​ ρ) + O ⁡ ( | ( ρ, x ¯ 3) | 2) \overline{x}=\beta-\left(\overline{x}_{3}-\frac{\overline{\mu}_{3}}{3-4B}\rho\right)+O(|(\rho,\overline{x}_{3})|^{2}) for P 3 P_{3} (resp. x ¯ = − β + ( x ¯ 4 + μ ¯ 3 3 − 4 ​ B ​ ρ) + O ⁡ ( | ( ρ, x ¯ 4) | 2) \overline{x}=-\beta+\left(\overline{x}_{4}+\frac{\overline{\mu}_{3}}{3-4B}\rho\right)+O(|(\rho,\overline{x}_{4})|^{2}) for P 4 P_{4}), yielding f i ′ ​ ( 0) = μ ¯ 3 3 − 4 ​ B ​ ( 1 + O ⁡ ( X 0)) f_{i}^{\prime}(0)=\frac{\overline{\mu}_{3}}{3-4B}(1+O(X_{0}));

 | 2 ​ I 1 + 2 ​ I 2 = [[+]] ​ μ ¯ 3 ​ 4 3 − 4 ​ B ​ x 0 2 + ( 1 − 2 ​ B) ​ x 0 2 2I_{1}+2I_{2}=[[+]]\overline{\mu}_{3}\frac{4}{3-4B}\,\frac{x_{0}}{2+(1-2B)x_{0}^{2}} |  |

As for the integral part in I 3 I_{3}, it is given by

 | 2 3 ​ 2 5 − 8 ​ B 2 ​ ( 2 ​ B − 1) ​ x 0 ​ [− 3 2 ​ F 1 ​ ( 1 2, 5 − 8 ​ B 2 ​ ( 1 − 2 ​ B), 3 2, 2 ​ B − 1 2 ​ x 0 2) + B ​ x 0 2 ​ F 1 2 ​ ( 3 2, 5 − 8 ​ B 2 ​ ( 1 − 2 ​ B), 5 2, 2 ​ B − 1 2 ​ x 0 2)], \frac{2}{3}2^{\frac{5-8B}{2(2B-1)}}x_{0}\left[-3\phantom{,}_{2}F_{1}\left(\frac{1}{2},\frac{5-8B}{2(1-2B)};\frac{3}{2};\frac{2B-1}{2}x_{0}^{2}\right)+Bx_{0}^{2}\phantom{,}{}_{2}F_{1}\left(\frac{3}{2},\frac{5-8B}{2(1-2B)};\frac{5}{2};\frac{2B-1}{2}x_{0}^{2}\right)\right], |  | (6.4) |

where F 1 2 ​ ( a, b, c, z) \phantom{,}{}_{2}F_{1}(a,b;c;z) is the Gauss hypergeometric function defined by

 | F 1 2 ​ ( a, b, c, z) = ∑ i = 0 ∞ ( a) n ​ ( b) n ( c) n ​ z n n!, \phantom{,}{}_{2}F_{1}(a,b;c;z)=\sum_{i=0}^{\infty}\frac{(a)_{n}(b)_{n}}{(c)_{n}}\,\frac{z^{n}}{n!}, |  |

with

 | ( a) 0 = 1, ( a) n = a ⁡ ( a + 1) ​ … ​ ( a + n − 1). (a)_{0}=1,\qquad(a)_{n}=a(a+1)\dots(a+n-1). |  |

The function F 1 2 ​ ( a, b, c, z) \phantom{,}{}_{2}F_{1}(a,b;c;z) is analytic in the whole plane, except for a singularity at z = 1 z=1. Moreover, F 1 2 ​ ( a, b, c, 0) = 1 \phantom{,}{}_{2}F_{1}(a,b;c;0)=1 and

 | F 1 2 ​ ( a, b, c, z) = Γ ⁡ ( c) ​ Γ ​ ( c − a − b) Γ ⁡ ( c − a) ​ Γ ​ ( c − b) 2 ​ F 1 ​ ( a, b, a + b − c + 1, 1 − z) + ( 1 − z) c − a − b ​ Γ ⁡ ( c) ​ Γ ​ ( a + b − c) Γ ⁡ ( a) ​ Γ ​ ( b) 2 ​ F 1 ​ ( c − a, c − b, c − a − b + 1, 1 − z) \displaystyle\begin{split}&\phantom{,}{}_{2}F_{1}(a,b;c;z)=\frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}\phantom{,}_{2}F_{1}(a,b;a+b-c+1;1-z)\\ &\qquad+(1-z)^{c-a-b}\frac{\Gamma(c)\Gamma(a+b-c)}{\Gamma(a)\Gamma(b)}\phantom{,}_{2}F_{1}(c-a,c-b;c-a-b+1;1-z)\end{split} |  | (6.5) |

for z ∈ ( − 1, 1) z\in(-1,1). This yields that near z = 1 z=1

 | F 1 2 ​ ( a, b, c, z) = Γ ⁡ ( c) ​ Γ ​ ( c − a − b) Γ ⁡ ( c − a) ​ Γ ​ ( c − b) + Γ ⁡ ( c) ​ Γ ​ ( a + b − c) Γ ⁡ ( a) ​ Γ ​ ( b) ​ ( 1 − z) c − a − b. \phantom{,}{}_{2}F_{1}(a,b;c;z)=\frac{\Gamma(c)\Gamma(c-a-b)}{\Gamma(c-a)\Gamma(c-b)}+\frac{\Gamma(c)\Gamma(a+b-c)}{\Gamma(a)\Gamma(b)}(1-z)^{c-a-b}. |  | (6.6) |

In the two hypergeometric functions appearing in ( 6.4), the exponent of ( 1 − z) (1-z) in ( 6.6) is

 | c − a − b = 4 ​ B − 3 2 ​ ( 1 − 2 ​ B) ​ { < 0, B > 3 4, > 0, B < 3 4.. c-a-b=\frac{4B-3}{2(1-2B)}\begin{cases}<0,&B>\frac{3}{4},\\ >0,&B<\frac{3}{4}.\end{cases}. |  |

Hence, the first (resp. second) term in ( 6.6) is dominant when B < 3 4 B<\frac{3}{4} (resp. B > 3 4 B>\frac{3}{4}). We treat the two cases.

The case B < 3 4 B<\frac{3}{4}. For 2 ​ B − 1 2 ​ x 0 2 \frac{2B-1}{2}x_{0}^{2} close to 1 1, the bracket part of ( 6.4) is close to

 | − 3 ​ Γ ⁡ ( 3 2) ​ Γ ​ ( 4 ​ B − 3 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( 1) ​ Γ ​ ( B − 1 1 − 2 ​ B) + B ​ x 0 2 ​ Γ ⁡ ( 5 2) ​ Γ ​ ( 4 ​ B − 3 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( 1) ​ Γ ​ ( B − 1 1 − 2 ​ B + 1) = Γ ⁡ ( 3 2) ​ Γ ​ ( 4 ​ B − 3 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( 1) ​ Γ ​ ( B − 1 1 − 2 ​ B) ​ ( − 3 + 3 ​ ( 1 − 2 ​ B) 2 ​ ( B − 1) ​ B ​ x 0 2), -3\frac{\Gamma(\frac{3}{2})\Gamma(\frac{4B-3}{2(1-2B)})}{\Gamma(1)\Gamma(\frac{B-1}{1-2B})}+Bx_{0}^{2}\frac{\Gamma(\frac{5}{2})\Gamma(\frac{4B-3}{2(1-2B)})}{\Gamma(1)\Gamma(\frac{B-1}{1-2B}+1)}=\frac{\Gamma(\frac{3}{2})\Gamma(\frac{4B-3}{2(1-2B)})}{\Gamma(1)\Gamma(\frac{B-1}{1-2B})}\left(-3+\frac{3(1-2B)}{2(B-1)}Bx_{0}^{2}\right), |  |

since Γ ⁡ ( x + 1) = x ​ Γ ​ ( x) \Gamma(x+1)=x\Gamma(x). We let x 0 2 = 2 2 ​ B − 1 − δ x_{0}^{2}=\frac{2}{2B-1}-\delta, with δ > 0 \delta>0 small. Using that Γ ⁡ ( 3 2) = 1 2 ​ π, \Gamma(\frac{3}{2})=\frac{1}{2}\sqrt{\pi}, the integral part of I 3 I_{3} in ( 6.3) is close to

 | { − 3 ​ π 2 ​ Γ ⁡ ( 4 ​ B − 3 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( B − 1 1 − 2 ​ B) ​ 2 ​ B − 1 2 ​ ( B − 1) ​ ( 2 − B ​ δ), B 0 ≠ 1 3 ​ π 4 ​ Γ ⁡ ( 4 ​ B − 3 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( − B 1 − 2 ​ B) ​ B ​ x 0 2 + O ⁡ ( B − B 0), B 0 = 1. \begin{cases}-\frac{3\sqrt{\pi}}{2}\frac{\Gamma(\frac{4B-3}{2(1-2B)})}{\Gamma(\frac{B-1}{1-2B})}\frac{2B-1}{2(B-1)}(2-B\delta),&B_{0}\neq 1\\ \frac{3\sqrt{\pi}}{4}\frac{\Gamma(\frac{4B-3}{2(1-2B)})}{\Gamma(\frac{-B}{1-2B})}Bx_{0}^{2}+O(B-B_{0}),&B_{0}=1.\end{cases} |  |

The coefficient is nonzero for δ > 0 \delta>0 as soon as B 0 ≠ 1 B_{0}\neq 1 (resp. B 0 = 1 B_{0}=1) and B − 1 1 − 2 ​ B \frac{B-1}{1-2B} (resp. − B 1 − 2 ​ B -\frac{B}{1-2B}) is not a negative integer, which is the case for B > 1 2 B>\frac{1}{2}. This shows that I 3 I_{3} grows as ( 2 + ( 1 − 2 ​ B) ​ x 0 2) 1 2 ​ ( 1 − 2 ​ B) (2+(1-2B)x_{0}^{2})^{\frac{1}{2(1-2B)}}, while 2 ​ ( I 1 + I 2) 2(I_{1}+I_{2}) grows as ( 2 + ( 1 − 2 ​ B) ​ x 0 2) − 1 (2+(1-2B)x_{0}^{2})^{-1}. Hence, [[I 3 I_{3}]] is dominant when B < 3 4 B<\frac{3}{4}, and 2 ( I 1 + I 2) + I 3 = ∗ μ ¯ 3 ≠ 0 2(I_{1}+I_{2})+I_{3}=*\overline{\mu}_{3}\neq 0 when B < 3 4 B<\frac{3}{4}.

The case B > 3 4 B>\frac{3}{4}. [[For 2 ​ B − 1 2 ​ x 0 2 \frac{2B-1}{2}x_{0}^{2} close to 1 1, the bracket part of ( 6.4) has two parts J 3 ′ J_{3}^{\prime} and J 3 ′′ J_{3}^{\prime\prime}.

 | J 3 ′ = − 3 ​ π 2 ​ Γ ⁡ ( 4 ​ B − 3 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( B − 1 1 − 2 ​ B) ​ 2 ​ B − 1 2 ​ ( B − 1) ​ ( 2 + O ⁡ ( δ)). J_{3}^{\prime}=-\frac{3\sqrt{\pi}}{2}\frac{\Gamma(\frac{4B-3}{2(1-2B)})}{\Gamma(\frac{B-1}{1-2B})}\frac{2B-1}{2(B-1)}(2+O(\delta)). |  |

 | J 3 ′′ = ( 1 − 2 ​ B − 1 2 ​ x 0 2) 4 ​ B − 3 2 ​ ( 1 − 2 ​ B) ​ ( − 3 ​ Γ ⁡ ( 3 2) ​ Γ ​ ( 3 − 4 ​ B 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( 1 2) ​ Γ ​ ( 5 − 8 ​ B 2 ​ ( 1 − 2 ​ B)) + B ​ x 0 2 ​ Γ ⁡ ( 5 2) ​ Γ ​ ( 3 − 4 ​ B 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( 3 2) ​ Γ ​ ( 5 − 8 ​ B 2 ​ ( 1 − 2 ​ B)) + O ⁡ ( δ)) = 3 2 ​ ( 1 − 2 ​ B − 1 2 ​ x 0 2) 4 ​ B − 3 2 ​ ( 1 − 2 ​ B) ​ Γ ⁡ ( 3 − 4 ​ B 2 ​ ( 1 − 2 ​ B)) Γ ⁡ ( 5 − 8 ​ B 2 ​ ( 1 − 2 ​ B)) ​ ( B ​ x 0 2 − 1 + O ⁡ ( δ)) − 3 3 − 4 ​ B ​ ( 1 − 2 ​ B − 1 2 ​ x 0 2) 4 ​ B − 3 2 ​ ( 1 − 2 ​ B) ​ ( 1 + O ⁡ ( δ)). \displaystyle\begin{split}J_{3}^{\prime\prime}&=\left(1-\frac{2B-1}{2}x_{0}^{2}\right)^{\frac{4B-3}{2(1-2B)}}\left(-3\frac{\Gamma(\frac{3}{2})\Gamma(\frac{3-4B}{2(1-2B)})}{\Gamma(\frac{1}{2})\Gamma(\frac{5-8B}{2(1-2B)})}+Bx_{0}^{2}\frac{\Gamma(\frac{5}{2})\Gamma(\frac{3-4B}{2(1-2B)})}{\Gamma(\frac{3}{2})\Gamma(\frac{5-8B}{2(1-2B)})}+O(\delta)\right)\\ &=\frac{3}{2}\left(1-\frac{2B-1}{2}x_{0}^{2}\right)^{\frac{4B-3}{2(1-2B)}}\frac{\Gamma(\frac{3-4B}{2(1-2B)})}{\Gamma(\frac{5-8B}{2(1-2B)})}(Bx_{0}^{2}-1+O(\delta))\\ &-\frac{3}{3-4B}\left(1-\frac{2B-1}{2}x_{0}^{2}\right)^{\frac{4B-3}{2(1-2B)}}(1+O(\delta)).\end{split} |  |

This yields the corresponding parts I 3 ′ I_{3}^{\prime} and I 3 ′′ I_{3}^{\prime\prime} for I 3 I_{3}, considering that δ = 2 + ( 1 − 2 ​ B) ​ x 0 2 \delta=2+(1-2B)x_{0}^{2}:

 | { I 3 ′ = ∗ μ ¯ 3 J 3 ′ δ 1 2 ​ ( 1 − 2 ​ B), I 3 ′′ = − μ ¯ 3 ​ 4 ​ x 0 3 − 4 ​ B ​ δ − 1 + O ⁡ ( 1). \begin{cases}I_{3}^{\prime}=*\overline{\mu}_{3}J_{3}^{\prime}\delta^{\frac{1}{2(1-2B)}},\\ I_{3}^{\prime\prime}=-\overline{\mu}_{3}\frac{4x_{0}}{3-4B}\delta^{-1}+O(1).\end{cases} |  |

Considering that 1 2 ​ ( 1 − 2 ​ B) ∈ ( − 1, 0) \frac{1}{2(1-2B)}\in(-1,0), Then 2 ( I 1 + I 2) + I 3 = ∗ μ ¯ 3 δ 1 2 ​ ( 1 − 2 ​ B) ( 1 + O ( δ)) ≠ 0 2(I_{1}+I_{2})+I_{3}=*\overline{\mu}_{3}\delta^{\frac{1}{2(1-2B)}}(1+O(\delta))\neq 0. ]] ∎

## References

- [1] F. Dumortier, R. Roussarie, Duck cycles and centre manifolds, Memoirs of A.M.S., vol. 121, n ∘ 577 {}^{\circ}577 (1996) 1–100.
- [2] F. Dumortier, R. Roussarie and C. Rousseau, Hilbert’s 16th problem for quadratic vector fields, J. Differential Equations 110 (1994), no. 1, 86–133.
- [3] F. Dumortier, M. El Morsalani and C. Rousseau, Hilbert’s 16th problem for quadratic systems and cyclicity of elementary graphics, Nonlinearity 9 (1996), 1209–1261.
- [4] F. Dumortier, R. Roussarie and S. Sotomayor, Generic 3-parameter families of vector fields in the plane, unfoldings of saddle, focus and elliptic singularities with nilpotent linear parts. Springer Lecture Notes in Mathematics 1480, 1–164 (1991).
- [5] Y. Ilyashenko and S. Yakovenko, Finitely-smooth normal forms of local families of diffeomorphisms and vector fields, Russian Mathematical Surveys 46 (1991), 1–43.
- [6] R. Roussarie, Desingularisation of unfoldings of cuspidal loops, in: ”Geometry and analysis in nonlinear dynamics”. H. Broer, F. Takens, Eds. Pitman Research Notes in Math. Series, n ∘ 222, {}^{\circ}222, Longman Scientific and Technical (1992) 41–55.
- [7] R. Roussarie and C. Rousseau, Finite cyclicity of nilpotent graphics of pp-type surrounding a center, Bull. Belg. Math. Soc. Simon Stevin 15 (2008), 547–614.
- [8] H. Zhu and C. Rousseau, Finite cyclicity of graphics with a nilpotent singularity of saddle or elliptic type, J. Differential Equations 178 (2002), 325–436.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
