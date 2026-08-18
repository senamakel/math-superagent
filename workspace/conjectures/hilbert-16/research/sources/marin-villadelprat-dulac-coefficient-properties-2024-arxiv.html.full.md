<!-- source: https://arxiv.org/html/2105.09785 | converted from HTML -->

Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: Coefficient properties 2010 AMS Subject Classification: 34C07; 34C20; 34C23. Key words and phrases: Dulac map, Dulac time, asymptotic expansion, incomplete Mellin transform. This work has been partially funded by the Ministry of Science, Innovation and Universities of Spain through the grants PGC2018-095998-B-I00 and MTM2017-86795-C3-2-P and by the Agency for Management of University and Research Grants of Catalonia through the grants 2017SGR1725 and 2017SGR1617.

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2105.09785v1 [math.DS] 20 May 2021

# Asymptotic expansion of the Dulac map and time for
unfoldings of hyperbolic saddles: Coefficient properties 0 0 footnotetext: 2010 AMS Subject Classification: 34C07; 34C20; 34C23. 0 0 footnotetext: Key words and phrases: Dulac map, Dulac time, asymptotic expansion, incomplete Mellin transform. 0 0 footnotetext: This work has been partially funded by the Ministry of Science, Innovation and Universities of Spain through the grants PGC2018-095998-B-I00 and MTM2017-86795-C3-2-P and by the Agency for Management of University and Research Grants of Catalonia through the grants 2017SGR1725 and 2017SGR1617.

D. Marín J. Villadelprat Affiliation: *[.1truecm] Departament de Matemàtiques, Edifici Cc, Universitat Autònoma de Barcelona, Affiliation: *[-.05truecm] 08193 Cerdanyola del Vallès (Barcelona), Spain Affiliation: *[-.05truecm] Centre de Recerca Matemàtica, Edifici Cc, Campus de Bellaterra, Affiliation: *[-.05truecm] 08193 Cerdanyola del Vallès (Barcelona), Spain Affiliation: *[.1truecm] Departament d’Enginyeria Informàtica i Matemàtiques, ETSE, Affiliation: *[-.05truecm] Universitat Rovira i Virgili, 43007 Tarragona, Spain

August 11, 2026

###### Abstract

We consider a 𝒞 ∞ \mathscr{C}^{\infty} family of planar vector fields { X μ ^ } μ ^ ∈ W ^ \{X_{\hat{\mu}}\}_{\hat{\mu}\in\hat{W}} having a hyperbolic saddle and we study the Dulac map D ⁡ ( s, μ ^) D(s;\hat{\mu}) and the Dulac time T ⁡ ( s, μ ^) T(s;\hat{\mu}) from a transverse section at the stable separatrix to a transverse section at the unstable separatrix, both at arbitrary distance from the saddle. Since the hyperbolicity ratio λ \lambda of the saddle plays an important role, we consider it as an independent parameter, so that μ ^ = ( λ, μ) ∈ W ^ = ( 0, + ∞) × W \hat{\mu}=(\lambda,\mu)\in\hat{W}=(0,+\infty)\times W, where W W is an open subset of ℝ N. \mathbb{R}^{N}. For each μ ^ 0 ∈ W ^ \hat{\mu}_{0}\in\hat{W} and L > 0 L>0, the functions D ⁡ ( s, μ ^) D(s;\hat{\mu}) and T ⁡ ( s, μ ^) T(s;\hat{\mu}) have an asymptotic expansion at s = 0 s=0 and μ ^ ≈ μ ^ 0 \hat{\mu}\approx\hat{\mu}_{0} with the remainder being uniformly L L -flat with respect to the parameters. The principal part of both asymptotic expansions is given in a monomial scale containing a deformation of the logarithm, the so-called Ecalle-Roussarie compensator. In this paper we are interested in the coefficients of these monomials, which are functions depending on μ ^ \hat{\mu} that can be shown to be 𝒞 ∞ \mathscr{C}^{\infty} in their respective domains and “universally” defined, meaning that their existence is stablished before fixing the flatness L L and the unfolded parameter μ ^ 0. \hat{\mu}_{0}. Each coefficient has its own domain and it is of the form ( ( 0, + ∞) ∖ D) × W ((0,+\infty)\setminus D)\times W, where D D a discrete set of rational numbers at which a resonance of the hyperbolicity ratio λ \lambda occurs. In our main result, Theorem A, we give the explicit expression of some of these coefficients and to this end a fundamental tool is the employment of a sort of incomplete Mellin transform. With regard to these coefficients we also prove that they have poles of order at most two at D × W D\times W and we give the corresponding residue, that plays an important role when compensators appear in the principal part. Furthermore we prove a result, Corollary B, showing that in the analytic setting each coefficient given in Theorem A is meromorphic on ( 0, + ∞) × W (0,+\infty)\times W and has only poles, of order at most two, along D × W. D\times W.

## 1 Introduction and statements of main results

In this paper we consider 𝒞 ∞ \mathscr{C}^{\infty} unfoldings of planar vector fields with a hyperbolic saddle. The study of the so-called Dulac map of the saddle has attracted the attention of many authors (see for instance [3, 4, 5, 12, 24, 29] and references there in) due, among other reasons, to its close connection with Hilbert’s 16th problem (see [13, 30] for details). If μ ^ {{\hat{\mu}}} is the parameter unfolding, the *Dulac map*D ⁡ ( ⋅, μ ^) D(\,\cdot\,;{{\hat{\mu}}}) of the saddle is the transition map from a transverse section Σ 1 \Sigma_{1} at its stable separatrix W 1 W_{1} to a transverse section Σ 2 \Sigma_{2} at its unstable separatrix W 2 W_{2}, whereas the *Dulac time*T ⁡ ( ⋅, μ ^) T(\,\cdot\,;{{\hat{\mu}}}) is the time that spends the flow to do this transition, see Figure 1. In a recent paper [23] we prove a general result for studying the asymptotic expansions of D ⁡ ( s, μ ^) D(s;{{\hat{\mu}}}) and T ⁡ ( s, μ ^) T(s;{{\hat{\mu}}}) at s = 0 s=0, where s s is the variable parameterizing the transverse section Σ 1 \Sigma_{1} and s = 0 s=0 corresponds to the intersection point W 1 ∩ Σ 1. W_{1}\cap\Sigma_{1}. In short, this general result gives a remainder that behaves well (i.e., uniformly on the parameters OPEN μ ^) {{\hat{\mu}}}) with respect to ∂ s \partial_{s} and provides a detailed description of the monomials appearing in the principal part. A key feature of this principal part is that the monomials can be ordered as s → 0 + s\to 0^{+}. This is a very important result for the theoretical point of view because it enables to bound the number of limit cycles or critical periodic orbits bifurcating from a polycycle. However there are specific problems where it is not only interesting to bound this number but also to determine from which parameters μ ^ {{\hat{\mu}}} these bifurcations occur. Having explicit expressions of the coefficients of the monomials in the principal part is crucial for this purpose, see for instance [32, 33] for limit cycles and [18, 19] for critical periodic orbits. The present paper is addressed to this issue. There are two features to be noted with regard to the hypothesis on the unfolding under consideration. On the one hand we suppose that the saddle is at the origin and, more significant, that the separatrices lay on the coordinate axis for all μ ^ {{\hat{\mu}}}. It is important to point out that there is no loss of generality in assuming this since we prove in [23, Lemma 4.3] that there exists a smooth diffeomorphism, depending on the parameters, that straightens the two segments of the separatrices joining the points W 1 ∩ Σ 1 W_{1}\cap\Sigma_{1} and W 2 ∩ Σ 2 W_{2}\cap\Sigma_{2} with the saddle. That being said, we suppose on the other hand that the vector field has poles along the axis. The reason why we permit this “polar” factor is because, when dealing with polynomial vector fields, a special attention must be paid to the study of those polycycles with vertices at infinity in the Poincaré disc. The factor can come from the line at infinity in a saddle at infinity or, more generally, appear in a divisor after desingularizing a non-elementary singular point. We remark that (by means of a reparametrization of time) this factor can be neglected to study the Dulac map but, on the contrary, this cannot be done when dealing with the Dulac time.

The present paper is the continuation of [22] and [23] and concludes our contribution to the study of the theoretical aspects of the asymptotic expansion of the Dulac map and Dulac time of an unfolding of a hyperbolic saddle. Naturally the results that we shall obtain in this paper are strongly related with our previous ones. For reader’s convenience we shall recall the essential results and definitions from [22, 23] in order to ease the legibility. Before that let us specify the hypothesis that we shall use throughout the paper. Setting μ ^:= ( λ, μ) ∈ W ^:= ( 0, + ∞) × W {{\hat{\mu}}}\!:=(\lambda,\mu)\in\hat{W}\!:=(0,+\infty)\times W with W W an open set of ℝ N, \mathbb{R}^{N}, we consider the family of vector fields { X μ ^ } μ ^ ∈ W ^ \{X_{{{\hat{\mu}}}}\}_{{{\hat{\mu}}}\in\hat{W}} with

 | X μ ^ ( x 1, x 2):= 1 x 1 n 1 ​ x 2 n 2 ( x 1 P 1 ( x 1, x 2; μ ^) ∂ x 1 + x 2 P 2 ( x 1, x 2; μ ^) ∂ x 2), X_{{\hat{\mu}}}({x_{1}},{x_{2}})\!:=\frac{1}{x_{1}^{n_{1}}x_{2}^{n_{2}}}\Big({x_{1}}P_{1}({x_{1}},{x_{2}};{{\hat{\mu}}})\partial_{x_{1}}+{x_{2}}P_{2}({x_{1}},{x_{2}};{{\hat{\mu}}})\partial_{x_{2}}\Big), |  | (1) |

where

- •

n:= ( n 1, n 2) ∈ ℤ ≥ 0 2, n\!:=(n_{1},n_{2})\in\mathbb{Z}^{2}_{\geq 0},

- •

P 1 P_{1} and P 2 P_{2} belong to 𝒞 ∞ ​ ( 𝒰 × W ^) \mathscr{C}^{\infty}(\mathscr{U}\!\times\!\hat{W}) for some open set 𝒰 \mathscr{U} of ℝ 2 \mathbb{R}^{2} containing the origin,

- •

P 1 ​ ( x 1, 0, μ ^) > 0 P_{1}({x_{1}},0;{{\hat{\mu}}})>0 and P 2 ​ ( 0, x 2, μ ^) < 0 P_{2}(0,{x_{2}};{{\hat{\mu}}})<0 for all ( x 1, 0), ( 0, x 2) ∈ 𝒰 ({x_{1}},0),(0,{x_{2}})\in\mathscr{U} and μ ^ ∈ W ^, {{\hat{\mu}}}\in\hat{W},

- •

λ = − P 2 ​ ( 0, 0, μ ^) P 1 ​ ( 0, 0, μ ^) \lambda=-\frac{P_{2}(0,0;{{\hat{\mu}}})}{P_{1}(0,0;{{\hat{\mu}}})}.

Moreover, for i = 1, 2, i=1,2, let σ i: ( − ε, ε) × W ^ ⟶ Σ i {\sigma_{i}}\!:{(-\varepsilon,\varepsilon)\times\hat{W}}\longrightarrow{\Sigma_{i}} be a 𝒞 ∞ \mathscr{C}^{\infty} transverse section to X μ ^ X_{{{\hat{\mu}}}} at x i = 0 x_{i}=0 defined by

 | σ i ​ ( s, μ ^) = ( σ i ​ 1 ​ ( s, μ ^), σ i ​ 2 ​ ( s, μ ^)) \sigma_{i}(s;{{\hat{\mu}}})=\bigl(\sigma_{i1}(s;{{\hat{\mu}}}),\sigma_{i2}(s;{{\hat{\mu}}})\bigr) |  |

such that σ 1 ​ ( 0, μ ^) ∈ { ( 0, x 2); x 2 > 0 } \sigma_{1}(0,{{\hat{\mu}}})\in\{(0,x_{2});x_{2}>0\} and σ 2 ​ ( 0, μ ^) ∈ { ( x 1, 0); x 1 > 0 } \sigma_{2}(0,{{\hat{\mu}}})\in\{(x_{1},0);x_{1}>0\} for all μ ^ ∈ W ^. {{\hat{\mu}}}\in\hat{W}. We denote the Dulac map and Dulac time of X μ ^ X_{{\hat{\mu}}} from Σ 1 \Sigma_{1} to Σ 2 \Sigma_{2} by D ⁡ ( ⋅, μ ^) D(\,\cdot\,;{{\hat{\mu}}}) and T ⁡ ( ⋅, μ ^) T(\,\cdot\,;{{\hat{\mu}}}), respectively (see Figure 1).

Figure 1: Definition of T ⁡ ( ⋅, μ ^) T(\,\cdot\,;{{\hat{\mu}}}) and D ⁡ ( ⋅, μ ^) D(\,\cdot\,;{{\hat{\mu}}}), where φ ⁡ ( t, p, μ ^) \varphi(t,p;{{\hat{\mu}}}) is the solution of X μ ^ X_{{\hat{\mu}}} passing through the point p ∈ 𝒰 p\in\mathscr{U} at time t = 0. t=0.

Of course, in order that these functions are well defined for s > 0 s>0 small enough, the open set 𝒰 \mathscr{U} must contain the corner

 | { ( x 1, 0); x 1 ∈ [0, σ 21 ​ ( 0)] } ∪ { ( 0, x 2); x 2 ∈ [0, σ 12 ​ ( 0)] }. \left\{(x_{1},0);\,x_{1}\in\big[0,\sigma_{21}(0)\big]\right\}\cup\left\{(0,x_{2});x_{2}\in\big[0,\sigma_{12}(0)\big]\right\}. |  |

? ⟨ \langle def_int ⟩ \rangle?

For convenience, taking ρ > 0 \rho>0 small enough, we define the open intervals

 | I 1:= ( − ρ, σ 12 ​ ( 0) + ρ) ​ and ​ I 2:= ( − ρ, σ 21 ​ ( 0) + ρ) I_{1}\!:=\big(-\rho,\sigma_{12}(0)+\rho\big)\text{ and }I_{2}\!:=\big(-\rho,\sigma_{21}(0)+\rho\big) |  |

and assume in what follows that 𝒰 \mathscr{U} contains ( { 0 } × I 1) ∪ ( I 2 × { 0 }). \big(\{0\}\!\times\!I_{1}\big)\cup\big(I_{2}\times\{0\}\big). Note then that, for i = 1, 2 i=1,2 and any k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0}, the map ( u, μ ^) ↦ ∂ 1 k P i ​ ( 0, u, μ ^) (u,{{\hat{\mu}}})\mapsto\partial_{1}^{k}P_{i}(0,u;{{\hat{\mu}}}) is 𝒞 ∞ \mathscr{C}^{\infty} on I 1 × W ^ I_{1}\!\times\!\hat{W} and the map ( u, μ ^) ↦ ∂ 2 k P i ​ ( u, 0, μ ^) (u,{{\hat{\mu}}})\mapsto\partial_{2}^{k}P_{i}(u,0;{{\hat{\mu}}}) is 𝒞 ∞ \mathscr{C}^{\infty} on I 2 × W ^ I_{2}\!\times\!\hat{W}. Moreover 0 ∈ I i 0\in I_{i} for i = 1, 2. i=1,2. This technical observation will be important later on. □ \square

? ⟨ \langle defi_fun ⟩ \rangle?

Consider K ∈ ℤ ≥ 0 ∪ { + ∞ } K\in\mathbb{Z}_{\geq 0}\cup\{+\infty\} and an open subset U ⊂ W ^ ⊂ ℝ N + 1. U\subset\hat{W}\subset\mathbb{R}^{N+1}. We say that a function ψ ⁡ ( s, μ ^) \psi(s;{{\hat{\mu}}}) belongs to the class 𝒞 s > 0 K ​ ( U) \mathscr{C}^{K}_{s>0}(U), respectively ℰ K ​ ( U), \mathcal{E}^{K}(U), if there exist an open neighbourhood Ω \Omega of

 | { ( s, μ ^) ∈ ℝ N + 2; s = 0, μ ^ ∈ U } = { 0 } × U \{(s,{{\hat{\mu}}})\in\mathbb{R}^{N+2};s=0,{{\hat{\mu}}}\in U\}=\{0\}\times U |  |

in ℝ N + 2 \mathbb{R}^{N+2} such that ( s, μ ^) ↦ ψ ⁡ ( s, μ ^) (s,{{\hat{\mu}}})\mapsto\psi(s;{{\hat{\mu}}}) is 𝒞 K \mathscr{C}^{K} on Ω ∩ ( ( 0, + ∞) × U), \Omega\cap\big((0,+\infty)\times U\big), respectively Ω \Omega. Finally we denote

 | ℰ + K ​ ( U):= { ψ ⁡ ( s, μ ^) ∈ ℰ K ​ ( U); ψ ⁡ ( 0, μ ^) > 0 ​ for all μ ^ ∈ U }. \mathcal{E}_{+}^{K}(U)\!:=\{\psi(s;{{\hat{\mu}}})\in\mathcal{E}^{K}(U);\,\psi(0;{{\hat{\mu}}})>0\text{ for all ${{\hat{\mu}}}\in U$}\}. |  |

Here the letter ℰ \mathcal{E} stands for functions in 𝒞 s > 0 K ​ ( U) \mathscr{C}^{K}_{s>0}(U) having *extension*to s = 0. s=0. □ \square

More formally, the definition of 𝒞 s > 0 K ​ ( U) \mathscr{C}^{K}_{s>0}(U) and ℰ K ​ ( U) \mathcal{E}^{K}(U) must be thought in terms of germs with respect to relative neighborhoods of { 0 } × U \{0\}\times U in ( 0, + ∞) × U (0,+\infty)\times U. In doing so these sets become rings and we have the inclusions 𝒞 K ​ ( U) ⊂ ℰ K ​ ( U) ⊂ 𝒞 s > 0 K ​ ( U) \mathscr{C}^{K}(U)\subset\mathcal{E}^{K}(U)\subset\mathscr{C}^{K}_{s>0}(U).

We can now introduce the notion of (finitely) flatness that we shall use in the sequel.

? ⟨ \langle defi2 ⟩ \rangle?

Consider K ∈ ℤ ≥ 0 ∪ { + ∞ } K\in\mathbb{Z}_{\geq 0}\cup\{+\infty\} and an open subset U ⊂ W ^ ⊂ ℝ N + 1. U\subset\hat{W}\subset\mathbb{R}^{N+1}. Given L ∈ ℝ L\in\mathbb{R} and μ ^ 0 ∈ U {{\hat{\mu}}}_{0}\in U, we say that ψ ⁡ ( s, μ ^) ∈ 𝒞 s > 0 K ​ ( U) \psi(s;{{\hat{\mu}}})\in\mathscr{C}^{K}_{s>0}(U) is *( L, K) (L,K) -flat with respect to s s at μ ^ 0 {{\hat{\mu}}}_{0}*, and we write ψ ∈ ℱ L K ​ ( μ ^ 0) \psi\in\mathcal{F}_{L}^{K}({{\hat{\mu}}}_{0}), if for each ν = ( ν 0, …, ν N + 1) ∈ ℤ ≥ 0 N + 2 \nu=(\nu_{0},\ldots,\nu_{N+1})\in\mathbb{Z}_{\geq 0}^{N+2} with | ν | = ν 0 + ⋯ + ν N + 1 ⩽ K |\nu|=\nu_{0}+\cdots+\nu_{N+1}\leqslant K there exist a neighbourhood V V of μ ^ 0 {{\hat{\mu}}}_{0} and C, s 0 > 0 C,s_{0}>0 such that

 | | ∂ | ν | ψ ⁡ ( s, μ ^) ∂ s ν 0 ∂ μ ^ 1 ν 1 ⋯ ∂ μ ^ N + 1 ν N + 1 | ⩽ C ​ s L − ν 0 ​ for all s ∈ ( 0, s 0) and μ ^ ∈ V. \left|\frac{\partial^{|\nu|}\psi(s;{{\hat{\mu}}})}{\partial s^{\nu_{0}}\partial{{\hat{\mu}}}_{1}^{\nu_{1}}\cdots\partial{{\hat{\mu}}}_{N+1}^{\nu_{N+1}}}\right|\leqslant Cs^{L-\nu_{0}}\text{ for all $s\in(0,s_{0})$ and ${{\hat{\mu}}}\in V$.} |  |

If W W is a (not necessarily open) subset of U U then define ℱ L K ​ ( W):= ⋂ μ ^ 0 ∈ W ℱ L K ​ ( μ ^ 0). \mathcal{F}_{L}^{K}(W)\!:=\bigcap_{{{\hat{\mu}}}_{0}\in W}\mathcal{F}_{L}^{K}({{\hat{\mu}}}_{0}). □ \square

The principal part of the Dulac map and Dulac time will be expressed in terms of the following deformation of the logarithm.

The function defined for s > 0 s>0 and α ∈ ℝ \alpha\in\mathbb{R} by means of

 | ω ⁡ ( s, α) = { s − α − 1 α if α ≠ 0, − log ⁡ s if α = 0, \omega(s;\alpha)\>=\left\{\begin{array}[]{ll}\frac{s^{-\alpha}-1}{\alpha}&\text{if $\alpha\neq 0,$}\\[2.0pt] -\log s&\text{if $\alpha=0,$}\end{array}\right. |  |

is called the *Ecalle-Roussarie compensator*. □ \square

Figure 2: The filled dots are points ( i, j) ∈ ℤ ≥ 0 2 (i,j)\in\mathbb{Z}_{\geq 0}^{2} in the set Λ k \Lambda_{k} for k = ( k 1, k 2) k=(k_{1},k_{2}).

? ⟨ \langle alldefi ⟩ \rangle?

Given any k = ( k 1, k 2) ∈ ℤ ≥ 0 2 k=(k_{1},k_{2})\in\mathbb{Z}^{2}_{\geq 0}, throughout the paper we shall use the following notation:

- •

Λ k:= ( ℤ ≥ k 1 × { 0 }) ∪ ( ℤ ≥ 0 × ℤ ≥ k 2) \Lambda_{k}\!:=(\mathbb{Z}_{\geq k_{1}}\!\times\{0\})\cup(\mathbb{Z}_{\geq 0}\!\times\mathbb{Z}_{\geq k_{2}}), see Figure 2.

- •

D i ​ j k:= { λ > 0: there exits ​ ( i ′, j ′) ∈ Λ k ∖ { ( i, j) } ​ such that ​ i + λ ​ j = i ′ + λ ​ j ′ } D_{ij}^{k}\!:=\big\{\lambda>0:\text{there exits }(i^{\prime},j^{\prime})\in\Lambda_{k}\setminus\{(i,j)\}\text{ such that }i+\lambda j=i^{\prime}+\lambda j^{\prime}\big\}.

- •

ℬ λ, L k:= { ( i, j) ∈ Λ k: i + λ ​ j ⩽ L } \mathscr{B}_{\lambda,L}^{k}\!:=\big\{(i,j)\in\Lambda_{k}:i+\lambda j\leqslant L\big\} for each L ∈ ℝ L\in\mathbb{R} and λ > 0 \lambda>0.

- •

D L k:= { λ > 0: there exits ​ ( i, j) ∈ ℬ λ, L k ​ such that ​ λ ∈ D i ​ j k }. D_{L}^{k}\!:=\big\{\lambda>0:\text{there exits }(i,j)\in\mathscr{B}_{\lambda,L}^{k}\text{ such that }\lambda\in D_{ij}^{k}\big\}.

- •

For λ = p / q ∈ ℚ > 0 \lambda=p/q\in\mathbb{Q}_{>0} with gcd ⁡ ( p, q) = 1 \gcd(p,q)=1 and ( i, j) ∈ Λ k (i,j)\in\Lambda_{k},

 | 𝒜 i ​ j ​ λ k:= { ∅ if ( i + r ​ p, j − r ​ q) ∈ Λ k for some r ∈ ℕ, { r ∈ ℤ ≥ 0: ( i − r ​ p, j + r ​ q) ∈ Λ k } otherwise. \mathscr{A}_{ij\lambda}^{k}\!:=\left\{\begin{array}[]{cl}\emptyset&\text{ if $(i+rp,j-rq)\in\Lambda_{k}$ for some $r\in\mathbb{N},$}\\[5.0pt] \left\{r\in\mathbb{Z}_{\geq 0}\,:\,(i-rp,j+rq)\in\Lambda_{k}\right\}&\text{ otherwise.}\end{array}\right. |  |

Observe that if k 2 = 0 k_{2}=0 then Λ k = ℤ ≥ 0 2 = Λ 0 \Lambda_{k}=\mathbb{Z}^{2}_{\geq 0}=\Lambda_{0} regardless of the value of k 1 k_{1}. One can prove on the other hand, see [23, Remark 3.3], that D i ​ j k D_{ij}^{k} and D L k D_{L}^{k} are discrete subsets of ℚ > 0 \mathbb{Q}_{>0}. □ \square

Let us point out that in the previous definition k k stands always for a two-dimensional vector with components in ℤ ≥ 0 \mathbb{Z}_{\geq 0}. That being said, if k = ( 0, 0) k=(0,0) then we write Λ 0 \Lambda_{0}, D i ​ j 0 D_{ij}^{0}, ℬ λ, L 0 \mathscr{B}_{\lambda,L}^{0}, D L 0 D_{L}^{0} and 𝒜 i ​ j ​ λ 0 \mathscr{A}_{ij\lambda}^{0} for shortness.

For the reader’s convenience we merge Theorems A and B of [23] in the following result. In its statement we use the notation introduced so far and denote

 | T 0 ​ ( μ ^) = { 0 if ​ n ≠ ( 0, 0), − 1 P ⁡ ( 0, 0, μ ^) if ​ n = ( 0, 0), T_{0}({{\hat{\mu}}})=\left\{\begin{array}[]{cl}0&\text{if }n\neq(0,0),\\[3.0pt] \frac{-1}{P(0,0;{{\hat{\mu}}})}&\text{if }n=(0,0),\end{array}\right. |  |

where recall that the components of n = ( n 1, n 2) ∈ ℤ ≥ 0 2 n=(n_{1},n_{2})\in\mathbb{Z}_{\geq 0}^{2} are the orders of the poles of X μ ^ X_{{\hat{\mu}}} along the axis.

###### Theorem 1.6.

? ⟨ \langle oldA ⟩ \rangle?

Let D ⁡ ( s, μ ^) D(s;{{\hat{\mu}}}) and T ⁡ ( s, μ ^) T(s;{{\hat{\mu}}}) be, respectively, the Dulac map and the Dulac time of the hyperbolic saddle ( 1) (\ref{X}\immediate) from Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2}.

1. ( a) (a)

For each ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} there exists Δ i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ j 0) × W) \Delta_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{ij}^{0})\times W\big) such that, for every L > 0 L>0 and λ 0 > 0, \lambda_{0}>0, the following hold:

  1. ( a ​ 1) (a1)

If λ 0 ∉ D L − λ 0 0 \lambda_{0}\notin D^{0}_{L-\lambda_{0}} then

 | D ⁡ ( s, μ ^) = s λ ​ ∑ ( i, j) ∈ ℬ λ 0, L − λ 0 0 Δ i ​ j ​ ( μ ^) ​ s i + λ ​ j + ℱ L ∞ ​ ( { λ 0 } × W). D(s;{{\hat{\mu}}})=s^{\lambda}\sum_{(i,j)\in\mathscr{B}_{\lambda_{0},L-\lambda_{0}}^{0}}\Delta_{ij}({{\hat{\mu}}})s^{i+\lambda j}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W). |  |

  2. ( a ​ 2) (a2)

If λ 0 ∈ D L − λ 0 0 \lambda_{0}\in D^{0}_{L-\lambda_{0}} then there exists a neighbourhood U ^ \hat{U} of { λ 0 } × W \{\lambda_{0}\}\times W such that

 | D ⁡ ( s, μ ^) = s λ ​ ∑ ( i, j) ∈ ℬ λ 0, L − λ 0 0 𝚫 i ​ j λ 0 ​ ( ω ⁡ ( s, α), μ ^) ​ s i + λ ​ j + ℱ L ∞ ​ ( { λ 0 } × W), D(s;{{\hat{\mu}}})=s^{\lambda}\sum_{(i,j)\in\mathscr{B}_{\lambda_{0},L-\lambda_{0}}^{0}}\boldsymbol{\Delta}_{ij}^{\lambda_{0}}\big(\omega(s;\alpha);{{\hat{\mu}}}\big)s^{i+\lambda j}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W), |  |

where λ 0 = p / q \lambda_{0}=p/q with gcd ⁡ ( p, q) = 1 \gcd(p,q)=1, α ⁡ ( μ ^) = p − λ ​ q \alpha({{\hat{\mu}}})=p-\lambda q and 𝚫 i ​ j λ 0 ​ ( w, μ ^) ∈ 𝒞 ∞ ​ ( U ^) ​ [w] \boldsymbol{\Delta}_{ij}^{\lambda_{0}}(w;{{\hat{\mu}}})\in\mathscr{C}^{\infty}(\hat{U})[w] with

 | 𝚫 i ​ j λ 0 ​ ( w, μ ^) = ∑ r ∈ 𝒜 i ​ j ​ λ 0 0 Δ i − r ​ p, j + r ​ q ​ ( μ ^) ​ ( 1 + α ​ w) r ​ for λ ≠ λ 0. \boldsymbol{\Delta}_{ij}^{\lambda_{0}}(w;{{\hat{\mu}}})=\sum_{r\in\mathscr{A}_{ij\lambda_{0}}^{0}}\Delta_{i-rp,j+rq}({{\hat{\mu}}})(1+\alpha w)^{r}\text{ for $\lambda\neq\lambda_{0}$.} |  |

Moreover Δ 00 ​ ( μ ^) > 0 \Delta_{00}({{\hat{\mu}}})>0 for all μ ^ ∈ W ^. {{\hat{\mu}}}\in\hat{W}.

2. ( b) (b)

For each ( i, j) ∈ Λ n (i,j)\in\Lambda_{n} there exists T i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ j n) × W) T_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{ij}^{n})\times W\big) such that, for every L > 0 L>0 and λ 0 > 0, \lambda_{0}>0, the following hold:

  1. ( b ​ 1) (b1)

If λ 0 ∉ D L n \lambda_{0}\notin D^{n}_{L} then

 | T ⁡ ( s, μ ^) = T 0 ​ ( μ ^) ​ log ⁡ s + ∑ ( i, j) ∈ ℬ λ 0, L n T i ​ j ​ ( μ ^) ​ s i + λ ​ j + ℱ L ∞ ​ ( { λ 0 } × W). T(s;{{\hat{\mu}}})=T_{0}({{\hat{\mu}}})\log s+\sum_{(i,j)\in\mathscr{B}_{\lambda_{0},L}^{n}}T_{ij}({{\hat{\mu}}})s^{i+\lambda j}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W). |  |

  2. ( b ​ 2) (b2)

If λ 0 ∈ D L n \lambda_{0}\in D^{n}_{L} then there exists a neighbourhood U ^ \hat{U} of { λ 0 } × W \{\lambda_{0}\}\times W such that

 | T ⁡ ( s, μ ^) = T 0 ​ ( μ ^) ​ log ⁡ s + ∑ ( i, j) ∈ ℬ λ 0, L n 𝑻 i ​ j λ 0 ​ ( ω ⁡ ( s, α), μ ^) ​ s i + λ ​ j + ℱ L ∞ ​ ( { λ 0 } × W), T(s;{{\hat{\mu}}})=T_{0}({{\hat{\mu}}})\log s+\sum_{(i,j)\in\mathscr{B}_{\lambda_{0},L}^{n}}\boldsymbol{T}_{ij}^{\lambda_{0}}\big(\omega(s;\alpha);{{\hat{\mu}}}\big)s^{i+\lambda j}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W), |  |

where λ 0 = p / q \lambda_{0}=p/q with gcd ⁡ ( p, q) = 1 \gcd(p,q)=1, α ⁡ ( μ ^) = p − λ ​ q \alpha({{\hat{\mu}}})=p-\lambda q and 𝑻 i ​ j λ 0 ​ ( w, μ ^) ∈ 𝒞 ∞ ​ ( U ^) ​ [w] \boldsymbol{T}_{ij}^{\lambda_{0}}(w;{{\hat{\mu}}})\in\mathscr{C}^{\infty}(\hat{U})[w] with

 | 𝑻 i ​ j λ 0 ​ ( w, μ ^) = ∑ r ∈ 𝒜 i ​ j ​ λ 0 n T i − r ​ p, j + r ​ q ​ ( μ ^) ​ ( 1 + α ​ w) r ​ for λ ≠ λ 0. \boldsymbol{T}_{ij}^{\lambda_{0}}(w;{{\hat{\mu}}})=\sum_{r\in\mathscr{A}_{ij\lambda_{0}}^{n}}T_{i-rp,j+rq}({{\hat{\mu}}})(1+\alpha w)^{r}\text{ for $\lambda\neq\lambda_{0}$.} |  |

For every ( i, j) ∈ Λ n (i,j)\in\Lambda_{n}, Theorem 1.6 shows that T i ​ j ​ ( λ, μ) T_{ij}(\lambda,\mu) is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D i ​ j n) × W ((0,+\infty)\setminus D_{ij}^{n})\times W. We will prove, see Lemma 3.1, that for each λ 0 ∈ D i ​ j n \lambda_{0}\in D_{ij}^{n} there exists ℓ ∈ ℤ ≥ 0 \ell\in\mathbb{Z}_{\geq 0} such that μ ^ ↦ ( λ − λ 0) ℓ ​ T i ​ j ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{\ell}T_{ij}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} to { λ 0 } × W. \{\lambda_{0}\}\times W. Moreover the number ℓ \ell, which depends on ( i, j) (i,j), λ 0 \lambda_{0} and n = ( n 1, n 2) n=(n_{1},n_{2}), is bounded by i + j. i+j. Hence, roughly speaking, the coefficient T i ​ j ​ ( λ, μ) T_{ij}(\lambda,\mu) has poles of order at most i + j i+j along D i ​ j n × W. D_{ij}^{n}\times W. Likewise, by Lemma 3.1 as well, it follows that Δ i ​ j ​ ( λ, μ) \Delta_{ij}(\lambda,\mu) has poles of order at most i + j i+j along D i ​ j 0 × W. D_{ij}^{0}\times W.

One of the main goals in this paper is to obtain explicit formulas for some of the coefficients Δ i ​ j \Delta_{ij} of the Dulac map and some of the coefficients T i ​ j T_{ij} of the Dulac time. More concretely, we will give the expressions of Δ i ​ j \Delta_{ij} for ( i, j) ∈ { ( 0, 0), ( 0, 1), ( 1, 0), ( 1, 1) } (i,j)\in\{(0,0),(0,1),(1,0),(1,1)\} and T i ​ j T_{ij} for ( i, j) ∈ { ( n 1, 0), ( n 1 + 1, 0), ( 0, n 2), ( 0, n 2 + 1) } (i,j)\in\{(n_{1},0),(n_{1}+1,0),(0,n_{2}),(0,n_{2}+1)\}. This information is relevant because the corresponding monomials s i + λ ​ j s^{i+\lambda j} are the first (as s → 0 + s\to 0^{+}) that appear in the asymptotic expansion of the Dulac map (see Theorem 4.1) and the Dulac time (see Theorem 4.3). With this aim in view we next define some functions that depend uniquely on P i ​ ( x 1, x 2, μ ^) P_{i}(x_{1},x_{2};{{\hat{\mu}}}), for i = 1, 2 i=1,2, and n = ( n 1, n 2) n=(n_{1},n_{2}), see ( 1) (\ref{X}\hbox{}). The latter is fixed, whereas the dependence on μ ^ {{\hat{\mu}}} will be omitted for shortness.

 | L 1 ( u):= exp ∫ 0 u ( P 1 ​ ( 0, z) P 2 ​ ( 0, z) + 1 λ) d ​ z z L 2 ( u):= exp ∫ 0 u ( P 2 ​ ( z, 0) P 1 ​ ( z, 0) + λ) d ​ z z M 1 ​ ( u):= L 1 ​ ( u) ​ ∂ 1 ( P 1 P 2) ​ ( 0, u) M 2 ​ ( u):= L 2 ​ ( u) ​ ∂ 2 ( P 2 P 1) ​ ( u, 0) A 1 ​ ( u):= L 1 n 1 ​ ( u) P 2 ​ ( 0, u) A 2 ​ ( u):= L 2 n 2 ​ ( u) P 1 ​ ( u, 0) B 1 ​ ( u):= n 1 ​ A 1 ​ ( u) ​ M ^ 1 ​ ( 1 / λ, u) B 2 ​ ( u):= n 2 ​ A 2 ​ ( u) ​ M ^ 2 ​ ( λ, u) + L 1 n 1 + 1 ( u) ∂ 1 P 2 − 1 ( 0, u) + L 2 n 2 + 1 ( u) ∂ 2 P 1 − 1 ( u, 0) C 1 ​ ( u):= L 1 2 ​ ( u) ​ ∂ 1 2 P 2 − 1 ​ ( 0, u) C 2 ​ ( u):= L 2 2 ​ ( u) ​ ∂ 2 2 P 1 − 1 ​ ( u, 0) + 2 L 1 ( u) M ^ 1 ( 1 / λ, u) ∂ 1 P 2 − 1 ( 0, u) + 2 L 2 ( u) M ^ 2 ( λ, u) ∂ 2 P 1 − 1 ( u, 0) \begin{array}[]{ll}\displaystyle L_{1}(u)\!:=\exp\int_{0}^{u}\left(\frac{P_{1}(0,z)}{P_{2}(0,z)}+\frac{1}{\lambda}\right)\frac{dz}{z}&\displaystyle L_{2}(u)\!:=\exp\int_{0}^{u}\left(\frac{P_{2}(z,0)}{P_{1}(z,0)}+{\lambda}\right)\frac{dz}{z}\\[15.0pt] \displaystyle M_{1}(u)\!:=L_{1}(u)\partial_{1}\!\left(\frac{P_{1}}{P_{2}}\right)(0,u)&\displaystyle M_{2}(u)\!:=L_{2}(u)\partial_{2}\!\left(\frac{P_{2}}{P_{1}}\right)(u,0)\\[15.0pt] \displaystyle A_{1}(u)\!:=\frac{L_{1}^{n_{1}}(u)}{P_{2}(0,u)}&\displaystyle A_{2}(u)\!:=\frac{L_{2}^{n_{2}}(u)}{P_{1}(u,0)}\\[15.0pt] \displaystyle B_{1}(u)\!:=n_{1}A_{1}(u)\hat{M}_{1}(1/\lambda,u)&\displaystyle B_{2}(u)\!:=n_{2}A_{2}(u)\hat{M}_{2}(\lambda,u)\\[3.0pt] \displaystyle\hskip 79.6678pt+L_{1}^{n_{1}+1}(u)\partial_{1}P_{2}^{-1}(0,u)&\displaystyle\hskip 79.6678pt+L_{2}^{n_{2}+1}(u)\partial_{2}P_{1}^{-1}(u,0)\\[15.0pt] \displaystyle C_{1}(u)\!:=L_{1}^{2}(u)\partial_{1}^{2}P_{2}^{-1}(0,u)&\displaystyle C_{2}(u)\!:=L_{2}^{2}(u)\partial_{2}^{2}P_{1}^{-1}(u,0)\\[3.0pt] \displaystyle\hskip 68.28644pt+2L_{1}(u)\hat{M}_{1}(1/\lambda,u)\partial_{1}P_{2}^{-1}(0,u)&\displaystyle\hskip 68.28644pt+2L_{2}(u)\hat{M}_{2}(\lambda,u)\partial_{2}P_{1}^{-1}(u,0)\end{array} |  | (2) |

Here, given α ∈ ℝ ∖ ℤ ≥ 0 \alpha\in\mathbb{R}\setminus\mathbb{Z}_{\geq 0} and a real valued function f ⁡ ( x) f(x) that is 𝒞 ∞ \mathscr{C}^{\infty} in an open interval containing x = 0 x=0, f ^ ​ ( α, x) \hat{f}(\alpha,x) is a sort of incomplete Mellin transform that we will introduce in Appendix B. In this regard we point out, see Lemma 2.3, that the functions L i ​ ( u), L_{i}(u), M i ​ ( u) M_{i}(u) and A i ​ ( u) A_{i}(u) are 𝒞 ∞ \mathscr{C}^{\infty} on an interval I i I_{i} that contains u = 0 u=0 for i = 1, 2. i=1,2. On the other hand, for shortness as well, in the statement of our main result we use the compact notation σ i ​ j ​ k \sigma_{ijk} for the k k th derivative at s = 0 s=0 of the j j th component of σ i ​ ( s, μ ^) \sigma_{i}(s;{{\hat{\mu}}}), i.e.,

 | σ i ​ j ​ k ​ ( μ ^):= ∂ s k σ i ​ j ​ ( 0, μ ^). \sigma_{ijk}({{\hat{\mu}}})\!:=\partial^{k}_{s}\sigma_{ij}(0;{{\hat{\mu}}}). |  |

In particular we consider the following real values (where once again we omit the dependence on μ ^ {{\hat{\mu}}}):

 | S 1:= σ 112 2 ​ σ 111 − σ 121 σ 120 ​ ( P 1 P 2) ​ ( 0, σ 120) − σ 111 L 1 ​ ( σ 120) ​ M ^ 1 ​ ( 1 / λ, σ 120) S 2:= σ 222 2 ​ σ 221 − σ 211 σ 210 ​ ( P 2 P 1) ​ ( σ 210, 0) − σ 221 L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210). \begin{array}[]{l}\displaystyle S_{1}\!:=\frac{\sigma_{112}}{2\sigma_{111}}-\frac{\sigma_{121}}{\sigma_{120}}\left(\frac{P_{1}}{P_{2}}\right)\!(0,\sigma_{120})-\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{M}_{1}(1/\lambda,\sigma_{120})\\[20.0pt] \displaystyle S_{2}\!:=\frac{\sigma_{222}}{2\sigma_{221}}-\frac{\sigma_{211}}{\sigma_{210}}\left(\frac{P_{2}}{P_{1}}\right)\!(\sigma_{210},0)-{\frac{\sigma_{221}}{L_{2}(\sigma_{210})}}\hat{M}_{2}(\lambda,\sigma_{210}).\end{array} |  | (3) |

We are now in position to state the main result of the present paper, Theorem A, which provides the explicit expression of the above-mentioned coefficients, see points ( b) (b) and ( c) (c). In addition to that we also establish in point ( a) (a) a factorization property among the coefficients Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} that holds for arbitrary ( i, j) (i,j). This factorization is along the lines of the one given by Roussarie (see [28, Theorem F] or [30, §5.1.3]) for the coefficients of the local Dulac map.

###### Theorem A.

? ⟨ \langle A ⟩ \rangle?

Assume n ≠ ( 0, 0) n\neq(0,0) and let D ⁡ ( s, μ ^) D(s;{{\hat{\mu}}}) and T ⁡ ( s, μ ^) T(s;{{\hat{\mu}}}) be, respectively, the Dulac map and the Dulac time of the hyperbolic saddle ( 1) (\ref{X}\hbox{}) from Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2}. Consider moreover the coefficients Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} given by Theorem 1.6. Then the following assertions hold:

1. ( a) (a)

? ⟨ \langle a ⟩ \rangle?

There exists a sequence { Ω i ​ j } ( i, j) ∈ Λ 0 \{\Omega_{ij}\}_{(i,j)\in\Lambda_{0}} with Ω i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ 0 0) × W) \Omega_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{i0}^{0})\times W\big) such that if ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} then

 | Δ i ​ j ​ ( μ ^) \displaystyle\Delta_{ij}({{\hat{\mu}}}) | = Ω i ​ j ​ ( μ ^) ​ Δ 0 ​ j ​ ( μ ^) ​ for all μ ^ ∈ W ^ with λ ∉ D i ​ j 0, \displaystyle=\Omega_{ij}({{\hat{\mu}}})\Delta_{0j}({{\hat{\mu}}})\text{ for all ${{\hat{\mu}}}\in\hat{W}$ with $\lambda\notin D_{ij}^{0}$,} |  |

and if ( i, j) ∈ Λ n (i,j)\in\Lambda_{n} with j > 0 j>0 then |

 | T i ​ j ​ ( μ ^) \displaystyle T_{ij}({{\hat{\mu}}}) | = Ω i, j − 1 ​ ( μ ^) ​ T 0 ​ j ​ ( μ ^) ​ for all μ ^ ∈ W ^ with λ ∉ D i ​ j n ∪ D i ​ 0 0 ⊂ D i ​ j 0. \displaystyle=\Omega_{i,j-1}({{\hat{\mu}}})T_{0j}({{\hat{\mu}}})\text{ for all ${{\hat{\mu}}}\in\hat{W}$ with $\lambda\notin D_{ij}^{n}\cup D_{i0}^{0}\subset D_{ij}^{0}$.} |  |

2. ( b) (b)

? ⟨ \langle b ⟩ \rangle?

The coefficients Δ i ​ j \Delta_{ij} for ( i, j) ∈ { ( 0, 0), ( 0, 1), ( 1, 0), ( 1, 1) } (i,j)\in\{(0,0),(0,1),(1,0),(1,1)\} of the Dulac map are given by

 | Δ 00 ​ ( μ ^) = σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120) ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ, Δ 01 ​ ( μ ^) = − Δ 00 2 ​ S 2, Δ 10 ​ ( μ ^) = Δ 00 ​ λ ​ S 1 ​ and ​ Δ 11 ​ ( μ ^) = − 2 ​ Δ 00 2 ​ λ ​ S 1 ​ S 2, \Delta_{00}({{\hat{\mu}}})=\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}},\quad\Delta_{01}({{\hat{\mu}}})=-\Delta_{00}^{2}S_{2},\quad\Delta_{10}({{\hat{\mu}}})=\Delta_{00}\lambda S_{1}\text{ and }\Delta_{11}({{\hat{\mu}}})=-2\Delta_{00}^{2}\lambda S_{1}S_{2}, |  |

where each equality is valid for all μ ^ ∈ W ^ {{\hat{\mu}}}\in\hat{W} with λ ∉ D i ​ j 0 \lambda\notin D_{ij}^{0}. In particular, Ω 10 ​ ( μ ^) = λ ​ S 1 \Omega_{10}({{\hat{\mu}}})=\lambda S_{1} and Ω 11 ​ ( μ ^) = 2 ​ λ ​ S 1 \Omega_{11}({{\hat{\mu}}})=2\lambda S_{1}.

3. ( c) (c)

? ⟨ \langle c ⟩ \rangle?

The coefficients T i ​ j T_{ij} for ( i, j) ∈ { ( n 1, 0), ( n 1 + 1, 0), ( 0, n 2), ( 0, n 2 + 1) } (i,j)\in\{(n_{1},0),(n_{1}+1,0),(0,n_{2}),(0,n_{2}+1)\} of the Dulac time are given by

 |  | T n 1, 0 ​ ( μ ^) = − σ 111 n 1 ​ σ 120 n 2 L 1 n 1 ​ ( σ 120) ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120), \displaystyle T_{n_{1},0}({{\hat{\mu}}})=-\frac{\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}}}{L_{1}^{n_{1}}(\sigma_{120})}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120}), |  |

 |  | T 0, n 2 ​ ( μ ^) = Δ 00 n 2 ​ σ 210 n 1 ​ σ 221 n 2 L 2 n 2 ​ ( σ 210) ​ A ^ 2 ​ ( n 2 ​ λ − n 1, σ 210), \displaystyle T_{0,n_{2}}({{\hat{\mu}}})=\Delta_{00}^{n_{2}}\frac{\sigma_{210}^{n_{1}}\sigma_{221}^{n_{2}}}{L_{2}^{n_{2}}(\sigma_{210})}\hat{A}_{2}(n_{2}\lambda-n_{1},\sigma_{210}), |  |

 |  | T n 1 + 1, 0 ​ ( μ ^) = − σ 111 n 1 ​ σ 120 n 2 ​ ( σ 121 σ 120 ​ P 2 ​ ( 0, σ 120) + n 1 ​ S 1 L 1 n 1 ​ ( σ 120) ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120) CLOSE \displaystyle T_{n_{1}+1,0}({{\hat{\mu}}})=-\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}}\left(\frac{\sigma_{121}}{\sigma_{120}P_{2}(0,\sigma_{120})}+\frac{n_{1}S_{1}}{L_{1}^{n_{1}}(\sigma_{120})}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})\right. |  |

 |  | OPEN + σ 111 L 1 n 1 + 1 ​ ( σ 120) ​ B ^ 1 ​ ( ( n 1 + 1) / λ − n 2, σ 120)), \displaystyle\hskip 163.60333pt+\left.\frac{\sigma_{111}}{L_{1}^{n_{1}+1}(\sigma_{120})}\hat{B}_{1}\big((n_{1}+1)/\lambda-n_{2},\sigma_{120}\big)\right), |  |

 |  | T 0, n 2 + 1 ​ ( μ ^) = Δ 00 n 2 + 1 ​ σ 210 n 1 ​ σ 221 n 2 ​ ( σ 211 σ 210 ​ P 1 ​ ( σ 210, 0) + σ 221 L 2 n 2 + 1 ​ ( σ 210) ​ B ^ 2 ​ ( λ ⁡ ( n 2 + 1) − n 1, σ 210)), \displaystyle T_{0,n_{2}+1}({{\hat{\mu}}})=\Delta_{00}^{n_{2}+1}\sigma_{210}^{n_{1}}\sigma_{221}^{n_{2}}\left(\frac{\sigma_{211}}{\sigma_{210}P_{1}(\sigma_{210},0)}+\frac{\sigma_{221}}{L_{2}^{n_{2}+1}(\sigma_{210})}\hat{B}_{2}\big(\lambda(n_{2}+1)-n_{1},\sigma_{210}\big)\right), |  |

where each equality is valid for all μ ^ ∈ W ^ {{\hat{\mu}}}\in\hat{W} with λ ∉ D i ​ j n, \lambda\notin D_{ij}^{n}, except for the third one in which the values λ = 1 k \lambda=\frac{1}{k}, k = 1, 2, …, ⌈ n 2 n 1 + 1 ⌉ − 1, k=1,2,\ldots,\lceil\frac{n_{2}}{n_{1}+1}\rceil-1, must be excluded as well. Moreover, if n 1 = 0 n_{1}=0 then

 |  | T 20 ​ ( μ ^) = − σ 120 n 2 ​ ( σ 122 ​ σ 120 + ( n 2 − 1) ​ σ 121 2 2 ​ σ 120 2 ​ P 2 ​ ( 0, σ 120) + σ 121 2 2 ​ σ 120 ​ ∂ 2 P 2 − 1 ​ ( 0, σ 120) + σ 121 ​ σ 111 σ 120 ​ ∂ 1 P 2 − 1 ​ ( 0, σ 120) CLOSE \displaystyle T_{20}({{\hat{\mu}}})=-\sigma_{120}^{n_{2}}\left(\frac{\sigma_{122}\sigma_{120}+(n_{2}-1)\sigma_{121}^{2}}{2\sigma_{120}^{2}P_{2}(0,\sigma_{120})}+\frac{\sigma_{121}^{2}}{2\sigma_{120}}\partial_{2}P_{2}^{-1}(0,\sigma_{120})+\frac{\sigma_{121}\sigma_{111}}{\sigma_{120}}\partial_{1}P_{2}^{-1}(0,\sigma_{120})\right. |  |

 |  | OPEN + σ 111 2 2 ​ L 1 2 ​ ( σ 120) ​ C ^ 1 ​ ( 2 / λ − n 2, σ 120) + σ 111 ​ S 1 L 1 ​ ( σ 120) ​ B ^ 1 ​ ( 1 / λ − n 2, σ 120)), \displaystyle\left.\hskip 113.81102pt+\frac{\sigma_{111}^{2}}{2L_{1}^{2}(\sigma_{120})}\hat{C}_{1}(2/\lambda-n_{2},\sigma_{120})+\frac{\sigma_{111}S_{1}}{L_{1}(\sigma_{120})}\hat{B}_{1}(1/\lambda-n_{2},\sigma_{120})\right), |  |

for all μ ^ ∈ W ^ {{\hat{\mu}}}\in\hat{W} with λ ∉ D 20 n ∪ { 1 k; k = 1, 2, …, ⌈ n 2 2 ⌉ − 1 }. \lambda\notin D_{20}^{n}\cup\left\{\frac{1}{k};\,k=1,2,\ldots,\lceil\frac{n_{2}}{2}\rceil-1\right\}. Finally if n 2 = 0 n_{2}=0 then

 |  | T 02 ​ ( μ ^) = Δ 00 2 ​ σ 210 n 1 ​ ( σ 212 ​ σ 210 + ( n 1 − 1) ​ σ 211 2 2 ​ σ 210 2 ​ P 1 ​ ( σ 210, 0) + σ 211 2 2 ​ σ 210 ​ ∂ 1 P 1 − 1 ​ ( σ 210, 0) + σ 211 ​ σ 221 σ 210 ​ ∂ 2 P 1 − 1 ​ ( σ 210, 0) CLOSE \displaystyle T_{02}({{\hat{\mu}}})=\Delta_{00}^{2}\sigma_{210}^{n_{1}}\left(\frac{\sigma_{212}\sigma_{210}+(n_{1}-1)\sigma_{211}^{2}}{2\sigma_{210}^{2}P_{1}(\sigma_{210},0)}+\frac{\sigma_{211}^{2}}{2\sigma_{210}}\partial_{1}P_{1}^{-1}(\sigma_{210},0)+\frac{\sigma_{211}\sigma_{221}}{\sigma_{210}}\partial_{2}P_{1}^{-1}(\sigma_{210},0)\right. |  |

 |  | OPEN + σ 221 2 2 ​ L 2 2 ​ ( σ 210) ​ C ^ 2 ​ ( 2 ​ λ − n 1, σ 210) − σ 211 ​ S 2 2 ​ σ 210 ​ P 1 ​ ( σ 210, 0)) \displaystyle\hskip 159.3356pt\left.+\frac{\sigma_{221}^{2}}{2L_{2}^{2}(\sigma_{210})}\hat{C}_{2}(2\lambda-n_{1},\sigma_{210})-\frac{\sigma_{211}S_{2}}{2\sigma_{210}P_{1}(\sigma_{210},0)}\right) |  |

for all μ ^ ∈ W ^ {{\hat{\mu}}}\in\hat{W} with λ ∉ D 02 n \lambda\notin D_{02}^{n}.

We point out that the coefficients T i ​ j ​ ( μ ^) T_{ij}({{\hat{\mu}}}) depend on μ ^ {{\hat{\mu}}} but also on n = ( n 1, n 2). n=(n_{1},n_{2}). We do not specify this dependence in the notation for the sake of shortness. This is the reason why, for instance, the expression for T n 1 + 1, 0 ​ ( μ ^) T_{n_{1}+1,0}({{\hat{\mu}}}) does not follow by replacing n 1 n_{1} by n 1 + 1 n_{1}+1 in the expression for T n 1, 0 ​ ( μ ^) T_{n_{1},0}({{\hat{\mu}}}).

The employment of the incomplete Mellin transform introduced in Appendix B allows us to generalise and unify several formulas that we obtained previously in [18, 21] under more restrictive hypothesis. With regard to the hypothesis, in those papers we restrict ourselves to the analytic setting (see Remark 1 below) and, more restraining, we assume that the family of vector fields { X μ ^ } μ ^ ∈ W ^ \{X_{{{\hat{\mu}}}}\}_{{{\hat{\mu}}}\in\hat{W}} in ( 1) (\ref{X}\hbox{}) verifies the *family linearization property*(FLP, for short), which means that { X μ ^ } μ ^ ∈ W ^ \{X_{{{\hat{\mu}}}}\}_{{{\hat{\mu}}}\in\hat{W}} is locally analytically equivalent to its linear part. In the present paper we do not require the FLP assumption and we consider the smooth setting instead of the analytic one. Furthermore the expressions for the coefficients that we obtain in those papers are only valid for hyperbolicity ratios varying in a specific range. By using the properties of the incomplete Mellin transform proved in Theorem B.1 we can get through this constrain as well. Let us exemplify this by noting that if n 1 = 0 n_{1}=0 and n 2 > 0 n_{2}>0 then

 | T 0 ​ n 2 ​ ( μ ^) \displaystyle T_{0n_{2}}({{\hat{\mu}}}) | = ( σ 221 ​ Δ 00 L 2 ​ ( σ 210)) n 2 ​ A ^ 2 ​ ( n 2 ​ λ, σ 210) \displaystyle=\left(\frac{\sigma_{221}\Delta_{00}}{L_{2}(\sigma_{210})}\right)^{n_{2}}\hat{A}_{2}(n_{2}\lambda,\sigma_{210}) |  |

 |  | = ( σ 221 ​ Δ 00 L 2 ​ ( σ 210)) n 2 ​ ( − A 2 ​ ( 0) n 2 ​ λ + σ 210 n 2 ​ λ ​ ∫ 0 σ 210 ( A 2 ​ ( u) − A 2 ​ ( 0)) ​ u − n 2 ​ λ ​ d ​ u u). \displaystyle=\left(\frac{\sigma_{221}\Delta_{00}}{L_{2}(\sigma_{210})}\right)^{n_{2}}\!\left(-\frac{A_{2}(0)}{n_{2}\lambda}+\sigma_{210}^{n_{2}\lambda}\int_{0}^{\sigma_{210}}\left(A_{2}(u)-A_{2}(0)\right)u^{-n_{2}\lambda}\frac{du}{u}\right). |  |

Here the first equality follows by ( c) (c) in Theorem A (and it is valid for all λ ∉ D 0 ​ n 2 n = ℕ n 2 \lambda\notin D_{0n_{2}}^{n}=\frac{\mathbb{N}}{n_{2}}, see Remark 1 below), whereas the second one follows by applying ( b) (b) in Theorem B.1 with k = 1 k=1 and assuming n 2 ​ λ < 1 n_{2}\lambda<1 additionally. In [18] we study the case { n 1 = 0, n 2 > 0 } \{n_{1}=0,n_{2}>0\} and the integral expression for T 0 ​ n 2 T_{0n_{2}} obtained after the second equality is precisely the one that we give in that paper, which only holds for λ ∈ ( 0, 1 n 2) \lambda\in(0,\frac{1}{n_{2}}) because the integrand has a pole of order n 2 ​ λ + 1 n_{2}\lambda+1 at u = 0. u=0. Similarly, if n 1 = 0 n_{1}=0 and n 2 > 0 n_{2}>0 then

 | T 10 ​ ( μ ^) \displaystyle T_{10}({{\hat{\mu}}}) | = − σ 120 n 2 ​ ( σ 121 σ 120 ​ P 2 ​ ( 0, σ 120) + σ 111 L 1 ​ ( σ 120) ​ B ^ 1 ​ ( 1 / λ − n 2, σ 120)) \displaystyle=-\sigma_{120}^{n_{2}}\left(\frac{\sigma_{121}}{\sigma_{120}P_{2}(0,\sigma_{120})}+\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{B}_{1}(1/\lambda-n_{2},\sigma_{120})\right) |  |

 |  | = − σ 120 n 2 ​ ( σ 121 σ 120 ​ P 2 ​ ( 0, σ 120) + σ 111 L 1 ​ ( σ 120) ​ σ 120 1 / λ − n 2 ​ ∫ 0 σ 120 B 1 ​ ( u) ​ u n 2 − 1 / λ ​ d ​ u u). \displaystyle=-\sigma_{120}^{n_{2}}\left(\frac{\sigma_{121}}{\sigma_{120}P_{2}(0,\sigma_{120})}+\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\sigma_{120}^{1/\lambda-n_{2}}\int_{0}^{\sigma_{120}}B_{1}(u)\,u^{n_{2}-1/\lambda}\frac{du}{u}\right). |  |

In this case the first equality follows by ( c) (c) in Theorem A (and it is valid as long as λ ∉ D 10 n = 1 ℕ ≥ n 2 \lambda\notin D_{10}^{n}=\frac{1}{\mathbb{N}_{\geq n_{2}}}, see Remark 1 below) and the second one follows by applying ( b) (b) in Theorem B.1 with k = 0 k=0 provided that 1 / λ − n 2 < 0 1/\lambda-n_{2}<0. The integral expression for T 10 T_{10} obtained after the second equality is precisely the one that we give in [18], which only converges for λ ∈ ( 1 n 2, + ∞). \lambda\in(\frac{1}{n_{2}},+\infty). In [21] we extend the results in [18] to arbitrary n = ( n 1, n 2) n=(n_{1},n_{2}) but still in the analytic setting and under the FLP assumption. The coefficient formulas given in that paper are also particular cases of the ones in Theorem A.

? ⟨ \langle domains ⟩ \rangle?

For the reader’s convenience we specify the sets D i ​ j 0 D_{ij}^{0} and D i ​ j n D_{ij}^{n} corresponding to the coefficients in points ( b) (b) and ( c) (c) in Theorem A. Taking Definition 1 into account one can readily get that

 | D 00 0 = ∅, D 01 0 = ℕ, D 10 0 = 1 ℕ ​ and ​ D 11 0 = ℕ ∪ 1 ℕ D_{00}^{0}=\emptyset,\;D_{01}^{0}=\mathbb{N},\;D_{10}^{0}=\frac{1}{\mathbb{N}}\text{ and }D_{11}^{0}=\mathbb{N}\cup\frac{1}{\mathbb{N}} |  |

for the coefficients of the Dulac map. Similarly, for the coefficients of the Dulac time, we have D 00 n = ∅ D_{00}^{n}=\emptyset,

 | D n 1, 0 n = ⋃ i = 1 n 1 i ℕ ≥ n 2, D 0, n 2 n = { ℕ ≥ n 1 n 2 if n 2 ⩾ 1, ∅ if n 2 = 0, ​ D n 1 + 1, 0 n = ⋃ i = 1 n 1 + 1 i ℕ ≥ n 2 ​ and ​ D 0, n 2 + 1 n = ℕ ≥ n 1 n 2 + 1 ∪ ℕ, D_{n_{1},0}^{n}=\bigcup_{i=1}^{n_{1}}\frac{i}{\mathbb{N}_{\geq n_{2}}},\;D_{0,n_{2}}^{n}=\left\{\begin{array}[]{cl}\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}}&\text{ if $n_{2}\geqslant 1$,}\\[5.0pt] \emptyset&\text{ if $n_{2}=0$,}\end{array}\right.\;D_{n_{1}+1,0}^{n}=\bigcup_{i=1}^{n_{1}+1}\frac{i}{\mathbb{N}_{\geq n_{2}}}\text{ and }D_{0,n_{2}+1}^{n}=\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}+1}\cup\mathbb{N}, |  |

together with D 20 n = 2 ℕ ≥ n 2 D_{20}^{n}=\frac{2}{\mathbb{N}_{\geq n_{2}}} for n 1 = 0 n_{1}=0 and D 02 n = ℕ 2 D_{02}^{n}=\frac{\mathbb{N}}{2} for n 2 = 0 n_{2}=0. □ \square

As we already mentioned, by Lemma 3.1 we know that the coefficients Δ i ​ j ​ ( λ, μ) \Delta_{ij}(\lambda,\mu) and T i ​ j ​ ( λ, μ) T_{ij}(\lambda,\mu) have poles of order at most i + j i+j along { λ 0 } × W \{\lambda_{0}\}\times W with λ 0 ∈ D i ​ j 0 \lambda_{0}\in D_{ij}^{0} and along { λ 0 } × W \{\lambda_{0}\}\times W with λ 0 ∈ D i ​ j n \lambda_{0}\in D_{ij}^{n}, respectively. This general result will be proved in Section 3. In that section we sharpen this upper bound for the coefficients given in points ( b) (b) and ( c) (c) of Theorem A and we also compute the corresponding residues. This information is of relevance because these residues are the values at λ 0 \lambda_{0} of the leading coefficients of the polynomials 𝚫 i ​ j λ 0 ​ ( w, μ ^) \boldsymbol{\Delta}_{ij}^{\lambda_{0}}(w;{{\hat{\mu}}}) and 𝑻 i ​ j λ 0 ​ ( w, μ ^) \boldsymbol{T}_{ij}^{\lambda_{0}}(w;{{\hat{\mu}}}) in Theorem 4.1 and Theorem 4.3, respectively. We illustrate this in Example 4 for the Dulac map.

? ⟨ \langle analytic_setting ⟩ \rangle?

In this paper, foreseeing future applications, we will sometimes consider the analytic setting. By *analytic setting*we mean that, for i = 1, 2 i=1,2, the function P i ​ ( x 1, x 2, μ ^) P_{i}(x_{1},x_{2};{{\hat{\mu}}}) in ( 1) (\ref{X}\hbox{}) is analytic on V × W ^ V\times\hat{W} and that the parametrization σ i ​ ( s, μ ^) \sigma_{i}(s;{{\hat{\mu}}}) of the transverse section Σ i \Sigma_{i} is analytic on ( − ε, ε) × W ^. (-\varepsilon,\varepsilon)\times\hat{W}. Note in particular, see Remark 1, that ∂ 1 k P i ​ ( 0, u, μ ^) ∈ 𝒞 ω ​ ( I 1 × W ^) \partial_{1}^{k}P_{i}(0,u;{{\hat{\mu}}})\in\mathscr{C}^{\omega}(I_{1}\!\times\!\hat{W}) and ∂ 2 k P i ​ ( u, 0, μ ^) ∈ 𝒞 ω ​ ( I 2 × W ^) \partial_{2}^{k}P_{i}(u,0;{{\hat{\mu}}})\in\mathscr{C}^{\omega}(I_{2}\!\times\!\hat{W}) for i = 1, 2 i=1,2 and k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0}. □ \square

In view of the above discussion about the poles of the coefficients, it is reasonable to expect that in the analytic setting the coefficients are meromorphic. In the present paper we are able to prove that this is the case for the coefficients considered in Theorem A. The following constitutes our second main result:

###### Corollary B.

? ⟨ \langle analitico ⟩ \rangle?

In the analytic setting the following assertions hold:

1. ( a) (a)

For each ( i, j) ∈ { ( 0, 0), ( 1, 0), ( 0, 1), ( 1, 1) } (i,j)\in\{(0,0),(1,0),(0,1),(1,1)\}, the coefficient Δ i ​ j \Delta_{ij} of the Dulac map is meromorphic on W ^ = ( ( 0, + ∞) × W CLOSE \hat{W}=((0,+\infty)\times W and has only poles, of order at most two, along D i ​ j 0 × W. D_{ij}^{0}\times W.

2. ( b) (b)

For each ( i, j) ∈ { ( 0, 0), ( n 1, 0), ( 0, n 2), ( n 1 + 1, 0), ( 0, n 2 + 1) } (i,j)\in\{(0,0),(n_{1},0),(0,n_{2}),(n_{1}+1,0),(0,n_{2}+1)\}, the coefficient T i ​ j T_{ij} of the Dulac time is meromorphic on W ^ = ( ( 0, + ∞) × W CLOSE \hat{W}=((0,+\infty)\times W and has only poles, of order at most two, along D i ​ j n × W. D_{ij}^{n}\times W. This is also the case for ( i, j) = ( 2, 0) (i,j)=(2,0) and ( i, j) = ( 0, 2) (i,j)=(0,2) assuming n 1 = 0 n_{1}=0 and n 2 = 0 n_{2}=0, respectively.

Taking this partial result into account in the analytic setting we conjecture that for arbitrary ( i, j) (i,j) the coefficient Δ i ​ j ​ ( λ, μ) \Delta_{ij}(\lambda,\mu) of the Dulac map is meromorphic on ( 0, + ∞) × W (0,+\infty)\times W with poles along λ ∈ D i ​ j 0 \lambda\in D_{ij}^{0} and that the coefficient T i ​ j ​ ( λ, μ) T_{ij}(\lambda,\mu) of the Dulac time is meromorphic on ( 0, + ∞) × W (0,+\infty)\times W with poles along λ ∈ D i ​ j n \lambda\in D_{ij}^{n}.

The paper is organized in the following way. Section 2 is mainly devoted to prove Theorem A. Once this is done, and as an intermediate step towards the proof of Corollary B, at the end of Section 2 we show that, in the analytic setting, the coefficients Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} listed in ( a) (a) and ( b) (b) of Theorem A, respectively, are analytic in their domains (see Proposition 2.9). In Section 3 we study the poles and residues of the coefficients. We begin by proving the above-mentioned Lemma 3.1, which constitutes a general result about the order of the poles. Next we prove a bunch of propositions that give the order of the pole and the respective residue for each coefficient listed in points ( a) (a) and ( b) (b) of Theorem A. Finally we conclude the section with the proof of Corollary B. Section 4 aims at future applications of the tools developed so far. The main result of this paper, Theorem A, is intended to be applied in combination with Theorem 1.6, that gathers our main results in [23]. For this reason, and in order to ease the applicability, in Section 4 we particularise Theorem 1.6 to specify the first monomials appearing in the asymptotic expansion of the Dulac map D ⁡ ( s, μ ^) D(s;{{\hat{\mu}}}), see Theorem 4.1, and the Dulac time T ⁡ ( s, μ ^) T(s;{{\hat{\mu}}}), see Theorem 4.3, for arbitrary hyperbolicity ratio λ 0 \lambda_{0}. By “first monomials” we mean as s → 0 + s\to 0^{+}, more concretely with respect to the strict partial order ≺ λ 0 \prec_{\lambda_{0}} introduced in [23, Definition 1.7]. It is here, dealing with a resonant hyperbolicity ratio λ 0 = p / q \lambda_{0}=p/q, where the compensator ω ⁡ ( s, p − λ ​ q) \omega(s;p-\lambda q) comes into play and the residues of the poles are needed, see Example 4.

## 2 Proof of Theorem A

For the reader’s convenience we state first a result that we proved in a previous paper, see [23, Corollary 2.2]. In its statement we follow the notation introduced in Definitions 1 and 1.

###### Lemma 2.1.

? ⟨ \langle new-factor1 ⟩ \rangle?

Consider f ⁡ ( s, μ ^) ∈ ℰ K ​ ( U) f(s;{{\hat{\mu}}})\in\mathcal{E}^{K}(U) with K ∈ ℕ K\in\mathbb{N} and any m ∈ ℕ m\in\mathbb{N} with m ⩽ K m\leqslant K. Then the following hold:

1. ( a) (a)

There exist f i ​ ( μ ^) ∈ 𝒞 K − i ​ ( U) f_{i}({{\hat{\mu}}})\in\mathscr{C}^{K-i}(U), i = 0, 1, …, m − 1 i=0,1,\ldots,m-1, and g ⁡ ( s, μ ^) ∈ ℰ K − m ​ ( U) g(s;{{\hat{\mu}}})\in\mathcal{E}^{K-m}(U) such that

 | f ⁡ ( s, μ ^) = ∑ i = 0 m − 1 f i ​ ( μ ^) ​ s i + s m ​ g ​ ( s, μ ^). f(s;{{\hat{\mu}}})=\sum_{i=0}^{m-1}f_{i}({{\hat{\mu}}})s^{i}+s^{m}g(s;{{\hat{\mu}}}). |  |

2. ( b) (b)

For any L ⩾ 0, L\geqslant 0, ℰ K ​ ( U) ⊂ 𝒞 K ′ ​ ( U) ​ [s] + ℱ L K ′ ​ ( U) \mathcal{E}^{K}(U)\subset\mathscr{C}^{K^{\prime}}(U)[s]+\mathcal{F}_{L}^{K^{\prime}}(U) provided that K ⩾ K ′ + L K\geqslant K^{\prime}+L.

The previous statement is aimed to study the flatness of the remainder in the asymptotic expansions that we shall deal with. The proof of ( a) (a) shows in fact, see [23], that if f ∈ 𝒞 K ​ ( I × U) f\in\mathscr{C}^{K}(I\times U) with I I an open interval of ℝ \mathbb{R} containing 0 0 then g ∈ 𝒞 K − m ​ ( I × U) g\in\mathscr{C}^{K-m}(I\times U). We prove next that this result has its obvious analytic and smooth analogous. From now on, for simplicity in the exposition, we shall use ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\} as a wild card in 𝒞 ϖ \mathscr{C}^{\varpi} for the smooth class 𝒞 ∞ \mathscr{C}^{\infty} and the analytic class 𝒞 ω \mathscr{C}^{\omega}.

###### Lemma 2.2.

? ⟨ \langle new-factor2 ⟩ \rangle?

Let us consider an open interval I I of ℝ \mathbb{R} containing 0 0, an open subset U U of ℝ N \mathbb{R}^{N} and m ∈ ℕ m\in\mathbb{N}. If f ⁡ ( s, ν) ∈ 𝒞 ϖ ​ ( I × U) f(s;\nu)\in\mathscr{C}^{\varpi}(I\times U) with ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\} then there exists g ⁡ ( s, ν) ∈ 𝒞 ϖ ​ ( I × U) g(s;\nu)\in\mathscr{C}^{\varpi}(I\times U) such that

 | f ⁡ ( s, ν) = ∑ i = 0 m − 1 ∂ s i f ⁡ ( 0, ν) i! ​ s i + s m ​ g ​ ( s, ν). f(s;\nu)=\sum_{i=0}^{m-1}\frac{\partial_{s}^{i}f(0;\nu)}{i!}s^{i}+s^{m}g(s;\nu). |  |

Given ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\}, we claim that if f ⁡ ( s, ν) ∈ 𝒞 ϖ ​ ( I × U) f(s;\nu)\in\mathscr{C}^{\varpi}(I\times U) verifies f ⁡ ( 0, ν) = 0 f(0;\nu)=0 for all ν ∈ U \nu\in U then there exists q ⁡ ( s, ν) ∈ 𝒞 ϖ ​ ( I × U) q(s;\nu)\in\mathscr{C}^{\varpi}(I\times U) such that f ⁡ ( s, ν) = s ​ q ​ ( s, ν). f(s;\nu)=sq(s;\nu). In order to prove the claim note first that the existence of q q in a neighbourhood of any ( s 0, ν 0) ∈ I × U (s_{0},\nu_{0})\in I\times U with s 0 ≠ 0 s_{0}\neq 0 is clear. Moreover this function is uniquely defined on ( I ∖ { 0 }) × U. (I\setminus\{0\})\times U. If s 0 = 0 s_{0}=0 then there exist 𝒞 ϖ \mathscr{C}^{\varpi} functions q ⁡ ( s, ν) q(s;\nu) and r ⁡ ( ν) r(\nu) in a neighbourhood V V of ( 0, ν 0) (0,\nu_{0}) in ℝ N + 1 \mathbb{R}^{N+1} such that f ⁡ ( s, ν) = s ​ q ​ ( s, ν) + r ⁡ ( ν) f(s;\nu)=sq(s;\nu)+r(\nu). Indeed, the case ϖ = ω \varpi=\omega follows by the Weierstrass Division Theorem (see [11, Theorem 1.8] or [15, Theorem 6.1.3]), whereas the case ϖ = ∞ \varpi=\infty is a consequence of the Malgrange Division Theorem (see [25, Theorem 2] for instance). Furthermore, due to r ⁡ ( ν) = f ⁡ ( 0, ν) = 0 r(\nu)=f(0;\nu)=0, we get that f ⁡ ( s, ν) = s ​ q ​ ( s, ν) f(s;\nu)=sq(s;\nu). Hence for each ν 0 ∈ U \nu_{0}\in U there exist a neighbourhood V ν 0 V_{\nu_{0}} of ( 0, ν 0) (0,\nu_{0}) in ℝ N + 1 \mathbb{R}^{N+1} and a function q ν 0 ∈ 𝒞 ϖ ​ ( V ν 0) q_{\nu_{0}}\in\mathscr{C}^{\varpi}(V_{\nu_{0}}) such that f ⁡ ( s, ν) = s ​ q ν 0 ​ ( s, ν). f(s;\nu)=sq_{\nu_{0}}(s;\nu). Since q ν 0 ​ ( s, ν) = f ⁡ ( s, ν) s q_{\nu_{0}}(s;\nu)=\frac{f(s;\nu)}{s} for all ( s, ν) ∈ V ν 0 (s,\nu)\in V_{\nu_{0}} with s ≠ 0, s\neq 0, we conclude that q ν 1 = q ν 2 q_{\nu_{1}}=q_{\nu_{2}} whenever V ν 1 ∩ V ν 2 ≠ ∅ V_{\nu_{1}}\cap V_{\nu_{2}}\neq\emptyset. This proves the claim.

The desired result follows from the claim by using induction on m. m. More precisely, for the base case m = 1 m=1 we apply the claim to f ⁡ ( s, ν) − f ⁡ ( 0, ν) f(s;\nu)-f(0;\nu). For the inductive step we apply the claim to g ⁡ ( s, ν) − g ⁡ ( 0, ν) g(s;\nu)-g(0;\nu), where g g is the remainder for the inductive hypothesis. In this way one can prove the existence of functions f i ∈ 𝒞 ϖ ​ ( U) f_{i}\in\mathscr{C}^{\varpi}(U) and g ∈ 𝒞 ϖ ​ ( I × U) g\in\mathscr{C}^{\varpi}(I\times U) verifying that f ⁡ ( s, ν) = ∑ i = 0 m − 1 f i ​ ( ν) ​ s i + s m ​ g ​ ( s, ν). f(s;\nu)=\sum_{i=0}^{m-1}f_{i}(\nu)s^{i}+s^{m}g(s;\nu). From here one can readily see that f i ​ ( ν) = ∂ s i f ⁡ ( 0, ν) i! f_{i}(\nu)=\frac{\partial_{s}^{i}f(0;\nu)}{i!} and this completes the proof.

In the next lemma we show that the regularity assumptions on the vector field ( 1) (\ref{X}\hbox{}), see Remarks 1 and 1, are transferred to the functions defined in ( 2) (\ref{def_fun}\immediate).

###### Lemma 2.3.

? ⟨ \langle fun_ok ⟩ \rangle?

Fix ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\} and let us assume the following:

1. ( a) (a)

P 1 ​ ( u, 0, μ ^) P_{1}(u,0;{{\hat{\mu}}}) and P 2 ​ ( 0, u, μ ^) P_{2}(0,u;{{\hat{\mu}}}) are non-vanishing functions on I 2 × W ^ I_{2}\!\times\!\hat{W} and I 1 × W ^ I_{1}\!\times\!\hat{W}, respectively.

2. ( b) (b)

∂ 1 k P i ​ ( 0, u, μ ^) ∈ 𝒞 ϖ ​ ( I 1 × W ^) \partial_{1}^{k}P_{i}(0,u;{{\hat{\mu}}})\in\mathscr{C}^{\varpi}(I_{1}\!\times\!\hat{W}) and ∂ 2 k P i ​ ( u, 0, μ ^) ∈ 𝒞 ϖ ​ ( I 2 × W ^) \partial_{2}^{k}P_{i}(u,0;{{\hat{\mu}}})\in\mathscr{C}^{\varpi}(I_{2}\!\times\!\hat{W}) for i = 1, 2 i=1,2 and k = 0, 1, 2. k=0,1,2.

Then, for i = 1, 2 i=1,2, the functions L i ​ ( u, μ ^) L_{i}(u;{{\hat{\mu}}}), M i ​ ( u, μ ^) M_{i}(u;{{\hat{\mu}}}) and A i ​ ( u, μ ^) A_{i}(u;{{\hat{\mu}}}) given in ( 2) (\ref{def_fun}\hbox{}) are 𝒞 ϖ \mathscr{C}^{\varpi} on I i × W ^ I_{i}\times\hat{W}. Moreover,

1. 1.

the functions B 1 ​ ( u, μ ^) B_{1}(u;{{\hat{\mu}}}) and C 1 ​ ( u, μ ^) C_{1}(u;{{\hat{\mu}}}) are 𝒞 ϖ \mathscr{C}^{\varpi} on I 1 × ( ( 0, + ∞) ∖ 1 ℕ) × W I_{1}\times((0,+\infty)\setminus\frac{1}{\mathbb{N}})\times W, and

2. 2.

the functions B 2 ​ ( u, μ ^) B_{2}(u;{{\hat{\mu}}}) and C 2 ​ ( u, μ ^) C_{2}(u;{{\hat{\mu}}}) are 𝒞 ϖ \mathscr{C}^{\varpi} on I 2 × ( ( 0, + ∞) ∖ ℕ) × W I_{2}\times((0,+\infty)\setminus\mathbb{N})\times W.

Since P 2 ​ ( 0, 0, μ ^) P 1 ​ ( 0, 0, μ ^) = − λ \frac{P_{2}(0,0;{{\hat{\mu}}})}{P_{1}(0,0;{{\hat{\mu}}})}=-\lambda by definition, the application of Lemma 2.2 with m = 1 m=1 implies that L i ​ ( u, μ ^) L_{i}(u;{{\hat{\mu}}}) is 𝒞 ϖ ​ ( I i × W ^) \mathscr{C}^{\varpi}(I_{i}\times\hat{W}) for i = 1, 2 i=1,2. In its turn this shows that A i ​ ( u, μ ^) A_{i}(u;{{\hat{\mu}}}) and M i ​ ( u, μ ^) M_{i}(u;{{\hat{\mu}}}) are 𝒞 ϖ ​ ( I i × W ^) \mathscr{C}^{\varpi}(I_{i}\times\hat{W}) for i = 1, 2 i=1,2. Then, by Theorem B.1, we can assert that M ^ i ​ ( α, u, μ ^) \hat{M}_{i}(\alpha,u;{{\hat{\mu}}}) is 𝒞 ϖ \mathscr{C}^{\varpi} on ( ℝ ∖ ℤ ≥ 0) × I i × W ^. (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I_{i}\times\hat{W}. More precisely, we use assertion ( a) (a) for the case ϖ = ∞ \varpi=\infty and assertion ( d) (d) for the ϖ = ω. \varpi=\omega. This easily implies, see ( 2) (\ref{def_fun}\hbox{}), that the assertions 1 and 2 in the statement are true and completes the proof of the result.

All the assertions except the last one in the next result are proved in [23, Lemma A.2]. The last one follows as a particular case of assertion ( c) (c) in [23, Lemma A.3].

###### Lemma 2.4.

? ⟨ \langle FLK ⟩ \rangle?

Let U U and U ′ U^{\prime} be open sets of ℝ N \mathbb{R}^{N} and ℝ N ′ \mathbb{R}^{N^{\prime}} respectively and consider W ⊂ U W\subset U and W ′ ⊂ U ′. W^{\prime}\subset U^{\prime}. Then the following holds:

1. ( a) (a)

ℱ L K ​ ( W) ⊂ ℱ L K ​ ( W ^) \mathcal{F}_{L}^{K}(W)\subset\mathcal{F}_{L}^{K}(\hat{W}) for any W ^ ⊂ W \hat{W}\subset W and ⋂ n ℱ L K ​ ( W n) = ℱ L K ​ ( ⋃ n W n) \bigcap_{n}\mathcal{F}_{L}^{K}(W_{n})=\mathcal{F}_{L}^{K}\left(\bigcup_{n}W_{n}\right).

2. ( b) (b)

ℱ L K ​ ( W) ⊂ ℱ L K ​ ( W × W ′) \mathcal{F}_{L}^{K}(W)\subset\mathcal{F}_{L}^{K}(W\times W^{\prime}).

3. ( c) (c)

𝒞 K ​ ( U) ⊂ ℰ K ​ ( U) ⊂ ℱ 0 K ​ ( W) \mathscr{C}^{K}(U)\subset\mathcal{E}^{K}(U)\subset\mathcal{F}_{0}^{K}(W).

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

9. ( i) (i)

If α ∈ 𝒞 K ​ ( U) \alpha\in\mathscr{C}^{K}(U) then s α ∈ ℱ L K ​ ( { ν ∈ U: α ⁡ ( ν) > L }) s^{\alpha}\in\mathcal{F}_{L}^{K}(\{\nu\in U:\alpha(\nu)>L\}).

By applying the previous lemmas we can now prove the following:

###### Lemma 2.5.

? ⟨ \langle composition ⟩ \rangle?

Let V V an open set of ℝ N \mathbb{R}^{N} and consider a polynomial Q ⁡ ( ⋅, ν) Q(\,\cdot\,;\nu) with coefficients in 𝒞 K ​ ( V) \mathscr{C}^{K}(V) such that Q ⁡ ( 0, ν) > 0 Q(0;\nu)>0 for all ν ∈ V. \nu\in V. Let us also take L > 0 L>0 and L ′ ⩾ 1 L^{\prime}\geqslant 1 together with α ∈ 𝒞 K ​ ( V) \alpha\in\mathscr{C}^{K}(V) such that α ⁡ ( ν) > 0 \alpha(\nu)>0 for all ν ∈ V \nu\in V. Then the following holds:

1. ( a) (a)

( s ​ Q ​ ( s) + ℱ L + 1 K ​ ( V)) α ⊂ s α ​ Q α ​ ( s) + ℱ L K ​ ( V) \left(sQ(s)+\mathcal{F}_{L+1}^{K}(V)\right)^{\alpha}\subset s^{\alpha}Q^{\alpha}(s)+\mathcal{F}_{L}^{K}(V), and

2. ( b) (b)

ℱ L ′ K ​ ( V) ∘ ( s α ​ Q ​ ( s) + ℱ L K ​ ( V)) ⊂ ℱ L K ​ ( { ν ∈ V: α ⁡ ( ν) > L / L ′ }). \mathcal{F}_{L^{\prime}}^{K}(V)\circ\left(s^{\alpha}Q(s)+\mathcal{F}_{L}^{K}(V)\right)\subset\mathcal{F}_{L}^{K}\left(\left\{\nu\in V:\alpha(\nu)>L/L^{\prime}\right\}\right).

In order to prove ( a) (a) note first that

 | ( s ​ Q ​ ( s) + ℱ L + 1 K ​ ( V)) α ⊂ s α ​ ( Q ⁡ ( s) + ℱ L K ​ ( V)) α ⊂ s α ​ Q α ​ ( s) ​ ( 1 + ℱ L K ​ ( V)) α. (sQ(s)+\mathcal{F}_{L+1}^{K}(V))^{\alpha}\subset s^{\alpha}(Q(s)+\mathcal{F}_{L}^{K}(V))^{\alpha}\subset s^{\alpha}Q^{\alpha}(s)(1+\mathcal{F}_{L}^{K}(V))^{\alpha}. |  | (4) |

Indeed, this follows by using twice ( g) (g) in Lemma 2.4. More concretely, in the first equality together with the fact that 1 / s ∈ ℱ − 1 K ​ ( V) 1/s\in\mathcal{F}_{-1}^{K}(V), whereas in the second one noting also that 1 / Q ⁡ ( s) ∈ ℰ K ​ ( V) ⊂ ℱ 0 K ​ ( V) 1/Q(s)\in\mathcal{E}^{K}(V)\subset\mathcal{F}_{0}^{K}(V). On the other hand, by using Lemmas 2.1 and 2.4,

 | g ⁡ ( x):= ( 1 + x) α − 1 ∈ s ​ ℰ ∞ ​ ( V) ⊂ ℱ 1 ∞ ​ ( V) ​ ℱ 0 ∞ ​ ( V) ⊂ ℱ 1 ∞ ​ ( V), g(x)\!:=(1+x)^{\alpha}-1\in s\mathcal{E}^{\infty}(V)\subset\mathcal{F}_{1}^{\infty}(V)\mathcal{F}_{0}^{\infty}(V)\subset\mathcal{F}_{1}^{\infty}(V), |  |

Thus g ∘ ℱ L K ​ ( V) ∈ ℱ L K ​ ( V) g\circ\mathcal{F}_{L}^{K}(V)\in\mathcal{F}_{L}^{K}(V) by ( h) (h) in Lemma 2.4 and, therefore, ( 1 + ℱ L K ​ ( V)) α ⊂ 1 + ℱ L K ​ ( V) (1+\mathcal{F}_{L}^{K}(V))^{\alpha}\subset 1+\mathcal{F}_{L}^{K}(V). Taking this into account, the assertion in ( a) (a) follows from ( 4) (\ref{comp_eq1}\immediate) noting that s α ​ Q α ​ ( s) ​ ℱ L K ​ ( V) ⊂ ℱ 0 K ​ ( V) ​ ℱ L K ​ ( V) ⊂ ℱ L K ​ ( V) s^{\alpha}Q^{\alpha}(s)\mathcal{F}_{L}^{K}(V)\subset\mathcal{F}_{0}^{K}(V)\mathcal{F}_{L}^{K}(V)\subset\mathcal{F}_{L}^{K}(V) due to s α ∈ ℱ 0 K ​ ( V) s^{\alpha}\in\mathcal{F}_{0}^{K}(V) by ( i) (i) in Lemma 2.4.

Let us turn next to the assertion in ( b) (b). To this end note that s α Q ( s) ∈ ℱ L / L ′ K ( V ∩ { α > L / L ′ }) s^{\alpha}Q(s)\in\mathcal{F}_{L/L^{\prime}}^{K}(V\cap\{\alpha>L/L^{\prime}\}) by ( i) (i) in Lemma 2.4. On the other hand, due to L ′ > 1, L^{\prime}>1, ℱ L K ( V) ⊂ ℱ L / L ′ K ( V) ⊂ ℱ L / L ′ K ( V ∩ { α > L / L ′ }) \mathcal{F}_{L}^{K}(V)\subset\mathcal{F}_{L/L^{\prime}}^{K}(V)\subset\mathcal{F}_{L/L^{\prime}}^{K}(V\cap\{\alpha>L/L^{\prime}\}) by ( d) (d) and ( a) (a) in Lemma 2.4. Thus, by ( e) (e) in Lemma 2.4,

 | s α Q ( s) + ℱ L K ( V) ⊂ ℱ L / L ′ K ( V ∩ { α > L / L ′ }). s^{\alpha}Q(s)+\mathcal{F}_{L}^{K}(V)\subset\mathcal{F}_{L/L^{\prime}}^{K}(V\cap\{\alpha>L/L^{\prime}\}). |  |

On account of this and that, by ( a) (a) in Lemma 2.4 again, ℱ L ′ K ( V) ⊂ ℱ L ′ K ( V ∩ { α > L / L ′ }) \mathcal{F}_{L^{\prime}}^{K}(V)\subset\mathcal{F}_{L^{\prime}}^{K}(V\cap\{\alpha>L/L^{\prime}\}), the application of ( h) (h) in Lemma 2.4 shows that

 | ℱ L ′ K ​ ( V) ∘ ( s α ​ Q ​ ( s) + ℱ L K ​ ( V)) \displaystyle\mathcal{F}_{L^{\prime}}^{K}(V)\circ\left(s^{\alpha}Q(s)+\mathcal{F}_{L}^{K}(V)\right) | ⊂ ℱ L ′ K ( V ∩ { α > L / L ′ }) ∘ ℱ L / L ′ K ( V ∩ { α > L / L ′ }) \displaystyle\subset\mathcal{F}_{L^{\prime}}^{K}(V\cap\{\alpha>L/L^{\prime}\})\circ\mathcal{F}_{L/L^{\prime}}^{K}(V\cap\{\alpha>L/L^{\prime}\}) |  |

 |  | ⊂ ℱ L K ( V ∩ { α > L / L ′ }). \displaystyle\subset\mathcal{F}_{L}^{K}(V\cap\{\alpha>L/L^{\prime}\}). |  |

This completes the proof of the result.

We only need one more technical result in order to tackle the proof of Theorem A. It will be a consequence of the following easy observation.

? ⟨ \langle rm1 ⟩ \rangle?

If ∑ i = 1 m a i ​ x λ i + ψ ⁡ ( x) = 0 \sum_{i=1}^{m}a_{i}x^{\lambda_{i}}+\psi(x)=0 for all x ∈ ( 0, ε), x\in(0,\varepsilon), where λ i ∈ ℝ \lambda_{i}\in\mathbb{R} with λ 1 < λ 2 < ⋯ < λ m \lambda_{1}<\lambda_{2}<\cdots<\lambda_{m}, a 1, a 2, …, a m ∈ ℝ a_{1},a_{2},\ldots,a_{m}\in\mathbb{R} and ψ ⁡ ( x) = o ⁡ ( x λ m) \psi(x)=\mathrm{o}(x^{\lambda_{m}}) then a 1 = a 2 = ⋯ = a m = 0 a_{1}=a_{2}=\cdots=a_{m}=0. □ \square

###### Lemma 2.7.

? ⟨ \langle combinacio ⟩ \rangle?

Consider α, β ∈ ℝ ∖ ℤ \alpha,\beta\in\mathbb{R}\setminus\mathbb{Z} with α − β ∉ ℤ \alpha-\beta\notin\mathbb{Z} and two functions f f and g g that are 𝒞 K \mathscr{C}^{K} on the interval ( − δ, δ) (-\delta,\delta) with K > − min ⁡ ( α, β). K>-\min(\alpha,\beta). If there exists c ∈ ℝ c\in\mathbb{R} satisfying that x α ​ f ​ ( x) + x β ​ g ​ ( x) = c x^{\alpha}f(x)+x^{\beta}g(x)=c for all x ∈ ( 0, δ) x\in(0,\delta) then c = 0. c=0.

Suppose that α < β \alpha<\beta and n:= min ⁡ { i ∈ ℤ ≥ 0: α + i > 0 }. n\!:=\min\{i\in\mathbb{Z}_{\geq 0}:\alpha+i>0\}. Hence K ⩾ n K\geqslant n and by applying Taylor’s theorem we can write

 | f ⁡ ( x) = a 0 + a 1 ​ x + … + a n ​ x n + x n ​ R 1 ​ ( x) ​ and ​ g ​ ( x) = b 0 + b 1 ​ x + … + b n ​ x n + x n ​ R 2 ​ ( x), f(x)=a_{0}+a_{1}x+\ldots+a_{n}x^{n}+x^{n}R_{1}(x)\text{ and }g(x)=b_{0}+b_{1}x+\ldots+b_{n}x^{n}+x^{n}R_{2}(x), |  |

with lim x → 0 R i ​ ( x) = 0. \lim_{x\to 0}R_{i}(x)=0. Let us also set κ:= min ⁡ { i ∈ ℤ ≥ 0: β + i > α + n }. \kappa\!:=\min\{i\in\mathbb{Z}_{\geq 0}:\beta+i>\alpha+n\}. Note then that κ ∈ { 0, 1 ​ …, n }. \kappa\in\{0,1\ldots,n\}. If we define ψ ⁡ ( x):= ( b κ ​ x κ + b κ + 1 ​ x κ + 1 + … + b n ​ x n) ​ x β + x n ​ ( x α ​ R 1 ​ ( x) + x β ​ R 2 ​ ( x)) \psi(x)\!:=(b_{\kappa}x^{\kappa}+b_{\kappa+1}x^{\kappa+1}+\ldots+b_{n}x^{n})x^{\beta}+x^{n}(x^{\alpha}R_{1}(x)+x^{\beta}R_{2}(x)) then, on account of the assumption x α ​ f ​ ( x) + x β ​ g ​ ( x) = c, x^{\alpha}f(x)+x^{\beta}g(x)=c, we get that

 | − c ​ x 0 + a 0 ​ x α + a 1 ​ x α + 1 + … + a n ​ x α + n + b 0 ​ x β + b 1 ​ x β + 1 + … + b κ − 1 ​ x β + κ − 1 + ψ ⁡ ( x) = 0 -cx^{0}+a_{0}x^{\alpha}+a_{1}x^{\alpha+1}+\ldots+a_{n}x^{\alpha+n}+b_{0}x^{\beta}+b_{1}x^{\beta+1}+\ldots+b_{\kappa-1}x^{\beta+\kappa-1}+\psi(x)=0 |  |

for all x ∈ ( 0, δ). x\in(0,\delta). Taking the definition of n n and κ \kappa into account, note that ψ ​ ( s) = o ​ ( x 0) \psi(s)=\mbox{\rm o}(x^{0}), ψ ​ ( s) = o ​ ( x α + n) \psi(s)=\mbox{\rm o}(x^{\alpha+n}) and ψ ​ ( s) = o ​ ( x β + κ − 1) \psi(s)=\mbox{\rm o}(x^{\beta+\kappa-1}). Moreover all the exponents in x 0, x α, x α + 1, …, x α + n, x β, x β + 1, …, x β + κ − 1 x^{0},x^{\alpha},x^{\alpha+1},\ldots,x^{\alpha+n},x^{\beta},x^{\beta+1},\ldots,x^{\beta+\kappa-1} are different by the hypothesis on α \alpha and β \beta, so that they can be ordered. Thus, on account of Remark 2, we can assert that all their coefficients are equal to zero, in particular c = 0. c=0.

Note first that by Theorem 1.6 we have two well defined sequences { Δ i ​ j } ( i, j) ∈ Λ 0 \{\Delta_{ij}\}_{(i,j)\in\Lambda_{0}} and { T i ​ j } ( i, j) ∈ Λ n \{T_{ij}\}_{(i,j)\in\Lambda_{n}} with Δ i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ j 0) × W) \Delta_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{ij}^{0})\times W\big) and T i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ j n) × W) T_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{ij}^{n})\times W\big) where, by applying [23, Lemma 3.2], D i ​ j 0 D_{ij}^{0} and D i ​ j n D_{ij}^{n} are discrete sets of rational numbers in ( 0, + ∞). (0,+\infty). In order to prove the assertions in ( a) (\ref{a}\immediate), for each ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} and μ ^ ∈ ( ( 0, + ∞) ∖ D i ​ 0 0) × W {{\hat{\mu}}}\in((0,+\infty)\setminus D_{i0}^{0})\times W we define Ω i ​ j ​ ( μ ^) \Omega_{ij}({{\hat{\mu}}}) by means of

 | ( 1 + ∑ i = 1 ∞ Δ i ​ 0 ​ ( μ ^) Δ 00 ​ ( μ ^) ​ s i) j + 1 = ∑ i = 0 ∞ Ω i ​ j ​ ( μ ^) ​ s i, \left(1+\sum_{i=1}^{\infty}\frac{\Delta_{i0}({{\hat{\mu}}})}{\Delta_{00}({{\hat{\mu}}})}s^{i}\right)^{j+1}=\sum_{i=0}^{\infty}\Omega_{ij}({{\hat{\mu}}})s^{i}, |  | (5) |

where the equality must be thought in the ring of formal power series in s s. Hence Ω i ​ j ∈ ℚ ⁡ [Δ 10 Δ 00, Δ 20 Δ 00, …, Δ i ​ 0 Δ 00] \Omega_{ij}\in\mathbb{Q}\left[\frac{\Delta_{10}}{\Delta_{00}},\frac{\Delta_{20}}{\Delta_{00}},\ldots,\frac{\Delta_{i0}}{\Delta_{00}}\right] for each fixed ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0}. One can verify, see Definition 1, that D i ​ 0 0 = ⋃ ℓ = 1 i ℓ ℕ D_{i0}^{0}=\bigcup_{\ell=1}^{i}\frac{\ell}{\mathbb{N}} and thus ∪ k = 1 i D k ​ 0 0 = D i ​ 0 0. \cup_{k=1}^{i}D_{k0}^{0}=D_{i0}^{0}. Consequently, since Δ 00 > 0 \Delta_{00}>0 on W ^ \hat{W} by ( a) (a) in Theorem 1.6, we can assert that

 | Ω i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ 0 0) × W). \Omega_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{i0}^{0})\times W\big). |  |

That being said, our first goal is to prove that if ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} then

 |  | Δ i ​ j ​ ( μ ^) − Ω i ​ j ​ ( μ ^) ​ Δ 0 ​ j ​ ( μ ^) = 0 ​ for all μ ^ ∈ W ^ with λ ∉ D i ​ j 0, \displaystyle\Delta_{ij}({{\hat{\mu}}})-\Omega_{ij}({{\hat{\mu}}})\Delta_{0j}({{\hat{\mu}}})=0\text{ for all ${{\hat{\mu}}}\in\hat{W}$ with $\lambda\notin D_{ij}^{0}$,} |  | (6) |

and that if ( i, j) ∈ Λ n (i,j)\in\Lambda_{n} with j > 0 j>0 then |

 |  | T i ​ j ​ ( μ ^) − Ω i, j − 1 ​ ( μ ^) ​ T 0 ​ j ​ ( μ ^) = 0 ​ for all μ ^ ∈ W ^ with λ ∉ D i ​ j n ∪ D i ​ 0 0. \displaystyle T_{ij}({{\hat{\mu}}})-\Omega_{i,j-1}({{\hat{\mu}}})T_{0j}({{\hat{\mu}}})=0\text{ for all ${{\hat{\mu}}}\in\hat{W}$ with $\lambda\notin D_{ij}^{n}\cup D_{i0}^{0}$.} |  | (7) |

To this aim let us note that the function on the left hand side of the equality in ( 6) (\ref{Aeq30}\immediate), respectively ( 7) (\ref{Aeq31}\immediate), is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of any μ ^ ⋆ = ( λ ⋆, μ ⋆) ∈ ( 0, + ∞) × W {{\hat{\mu}}}_{\star}=(\lambda_{\star},\mu_{\star})\in(0,+\infty)\times W with λ ⋆ \lambda_{\star} outside the discrete set D i ​ j 0 ∪ D i ​ 0 0 ∪ D 0 ​ j 0 D_{ij}^{0}\cup D_{i0}^{0}\cup D_{0j}^{0}, respectively D i ​ j n ∪ D i ​ 0 0 ∪ D 0 ​ j n D_{ij}^{n}\cup D_{i0}^{0}\cup D_{0j}^{n}. In this regard observe that D i ​ j n ⊂ D i ​ j 0, D_{ij}^{n}\subset D_{ij}^{0}, see Definition 1. It is also easy to show that, for any given any k ∈ ℤ ≥ 0 2, k\in\mathbb{Z}_{\geq 0}^{2}, we have D i ​ 0 k ⊂ D i ​ j k D_{i0}^{k}\subset D_{ij}^{k} and D 0 ​ j k ⊂ D i ​ j k. D_{0j}^{k}\subset D_{ij}^{k}. Consequently

 | D i ​ j 0 ∪ D i ​ 0 0 ∪ D 0 ​ j 0 = D i ​ j 0 ​ and ​ D i ​ j n ∪ D i ​ 0 0 ∪ D 0 ​ j n = D i ​ j n ∪ D i ​ 0 0 ⊂ D i ​ j 0, D_{ij}^{0}\cup D_{i0}^{0}\cup D_{0j}^{0}=D_{ij}^{0}\text{ and }D_{ij}^{n}\cup D_{i0}^{0}\cup D_{0j}^{n}=D_{ij}^{n}\cup D_{i0}^{0}\subset D_{ij}^{0}, |  |

so that the function in ( 6) (\ref{Aeq30}\hbox{}) is continuous on ( ( 0, + ∞) ∖ D i ​ j 0) × W ((0,+\infty)\setminus D_{ij}^{0})\times W whereas the function in ( 7) (\ref{Aeq31}\hbox{}) is continuous on ( ( 0, + ∞) ∖ ( D i ​ j n ∪ D i ​ 0 0)) × W ((0,+\infty)\setminus(D_{ij}^{n}\cup D_{i0}^{0}))\times W. Since D i ​ j 0 D_{ij}^{0} and D i ​ j n ∪ D i ​ 0 0 D_{ij}^{n}\cup D_{i0}^{0} are discrete sets of rational number in ( 0, + ∞) (0,+\infty), it is clear that both identities will follow by continuity once we prove it for any μ ^ = ( λ, μ) ∈ W ^ {{\hat{\mu}}}=(\lambda,\mu)\in\hat{W} with λ ∉ ℚ. \lambda\notin\mathbb{Q}.

The strategy to prove the identities in ( b) (\ref{b}\immediate) and ( c) (\ref{c}\immediate) will be the same. Indeed, let us write them as

 | Δ i ​ j ​ ( λ, μ) = Δ ~ i ​ j ​ ( λ, μ) ​ and ​ T i ​ j ​ ( λ, μ) = T ~ i ​ j ​ ( λ, μ), \Delta_{ij}(\lambda,\mu)=\tilde{\Delta}_{ij}(\lambda,\mu)\text{ and }T_{ij}(\lambda,\mu)=\tilde{T}_{ij}(\lambda,\mu), |  |

i.e., Δ ~ i ​ j \tilde{\Delta}_{ij} and T ~ i ​ j \tilde{T}_{ij} are the functions on the right hand side of the equalities in the statement we want to prove. As we already mentioned, we know that

 | Δ i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ j 0) × W) ​ and ​ T i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D i ​ j n) × W) \Delta_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{ij}^{0})\times W\big)\text{ and }T_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus D_{ij}^{n})\times W\big) |  |

by Theorem 1.6. On the other hand it turns out that there exist D ~ i ​ j 0, D ~ i ​ j n ⊂ ℚ > 0 \tilde{D}_{ij}^{0},\tilde{D}_{ij}^{n}\subset\mathbb{Q}_{>0} such that

 | Δ ~ i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D ~ i ​ j 0) × W) ​ and ​ T ~ i ​ j ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D ~ i ​ j n) × W). \tilde{\Delta}_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus\tilde{D}_{ij}^{0})\times W\big)\text{ and }\tilde{T}_{ij}\in\mathscr{C}^{\infty}\big(((0,+\infty)\setminus\tilde{D}_{ij}^{n})\times W\big). |  |

The sets D ~ i ​ j 0 \tilde{D}_{ij}^{0} and D ~ i ​ j n \tilde{D}_{ij}^{n} will be given explicitly later on but at this moment the relevant property is that they are discrete in ( 0, + ∞) (0,+\infty) as well. That said, for simplicity in the exposition, let us explain how the proof goes for the identity T 0, n 2 ​ ( λ, μ) = T ~ 0, n 2 ​ ( λ, μ) T_{0,n_{2}}(\lambda,\mu)=\tilde{T}_{0,n_{2}}(\lambda,\mu). Thus, since D 0, n 2 n ∪ D ~ 0, n 2 n D_{0,n_{2}}^{n}\cup\tilde{D}_{0,n_{2}}^{n} is a discrete set of rational numbers in ( 0, + ∞) (0,+\infty), for any given λ ⋆ ∉ D 0, n 2 n ∪ D ~ 0, n 2 n \lambda_{\star}\notin D_{0,n_{2}}^{n}\cup\tilde{D}_{0,n_{2}}^{n} there exists a sequence of irrational numbers ( λ k) k ∈ ℕ (\lambda_{k})_{k\in\mathbb{N}} such that lim k → ∞ λ k = λ ⋆ \lim_{k\to\infty}\lambda_{k}=\lambda_{\star}. Hence, if we take any μ ∈ W \mu\in W then, by continuity, lim k → ∞ T 0, n 2 ​ ( λ k, μ) = T 0, n 2 ​ ( λ ⋆, μ) \lim_{k\to\infty}T_{0,n_{2}}(\lambda_{k},\mu)=T_{0,n_{2}}(\lambda_{\star},\mu) and lim k → ∞ T ~ 0, n 2 ​ ( λ k, μ) = T ~ 0, n 2 ​ ( λ ⋆, μ). \lim_{k\to\infty}\tilde{T}_{0,n_{2}}(\lambda_{k},\mu)=\tilde{T}_{0,n_{2}}(\lambda_{\star},\mu). So it is clear that the validity of the equality T 0, n 2 ​ ( λ, μ) = T ~ 0, n 2 ​ ( λ, μ) T_{0,n_{2}}(\lambda,\mu)=\tilde{T}_{0,n_{2}}(\lambda,\mu) at any λ = λ ⋆ \lambda=\lambda_{\star} which is not inside D 0, n 2 n ∪ D ~ 0, n 2 n D_{0,n_{2}}^{n}\cup\tilde{D}_{0,n_{2}}^{n} will follow once we prove it for any μ ^ = ( λ, μ) ∈ W ^ {{\hat{\mu}}}=(\lambda,\mu)\in\hat{W} with λ ∉ ℚ. \lambda\notin\mathbb{Q}. This will be precisely our goal to prove each one of the equalities in the statement. As a matter of fact we will show that each equality is true in a neighbourhood of any μ ^ 0 = ( λ 0, μ 0) ∈ W ^ {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in\hat{W} with λ 0 ∉ ℚ. \lambda_{0}\notin\mathbb{Q}.

In addition to the identities in ( b) (\ref{b}\hbox{}) and ( c) (\ref{c}\hbox{}) we shall prove the equality in ( 6) (\ref{Aeq30}\hbox{}) for ( i, j) = ( i 1, j 1) (i,j)=(i_{1},j_{1}) and the equality in ( 7) (\ref{Aeq31}\hbox{}) for ( i, j) = ( i 2, j 2) (i,j)=(i_{2},j_{2}), where ( i 1, j 1) ∈ Λ 0 (i_{1},j_{1})\in\Lambda_{0} and ( i 2, j 2) ∈ Λ n (i_{2},j_{2})\in\Lambda_{n} are arbitrary but fixed. To this end, in view of the previous considerations, we fix any μ ^ 0 = ( λ 0, μ 0) ∈ W ^ {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in\hat{W} with λ 0 ∉ ℚ. \lambda_{0}\notin\mathbb{Q}. Then by [20, Theorem A] we know that for each K ∈ ℕ {K}\in\mathbb{N} there exists a 𝒞 K \mathscr{C}^{K} diffeomorphism

 | Φ ⁡ ( u 1, u 2, μ ^) = ( u 1 ​ ψ 1 ​ ( u 1, u 2, μ ^), u 2 ​ ψ 2 ​ ( u 1, u 2, μ ^), μ ^), \Phi(u_{1},u_{2},{{\hat{\mu}}})=\big(u_{1}\psi_{1}(u_{1},u_{2};{{\hat{\mu}}}),u_{2}\psi_{2}(u_{1},u_{2};{{\hat{\mu}}}),{{\hat{\mu}}}\big), |  |

defined in an open set U × V U\times V with ( 0, 0) ∈ U ⊂ ℝ 2 (0,0)\in U\subset\mathbb{R}^{2} and μ ^ 0 ∈ V ⊂ W ^ {{\hat{\mu}}}_{0}\in V\subset\hat{W}, verifying

 | Φ ∗ X μ ^ = P 1 ​ ( 0, 0, μ ^) u 1 n 1 ​ u 2 n 2 ( u 1 ∂ u 1 − λ u 2 ∂ u 2) \Phi^{*}X_{{\hat{\mu}}}=\frac{P_{1}(0,0;{{\hat{\mu}}})}{u_{1}^{n_{1}}u_{2}^{n_{2}}}(u_{1}\partial_{u_{1}}-\lambda u_{2}\partial_{u_{2}}) |  | (8) |

and such that ψ i ​ ( 0, 0, μ ^) = 1 \psi_{i}(0,0;{{\hat{\mu}}})=1, i = 1, 2. i=1,2. Let us point out that in the forthcoming analysis it will be crucial that K K is larger than some fixed quantity 𝒩 = 𝒩 ⁡ ( λ 0, n 1, n 2, i 1, i 2, j 1, j 2). \mathcal{N}=\mathcal{N}(\lambda_{0},n_{1},n_{2},i_{1},i_{2},j_{1},j_{2}). We will specify at each step of the proof which is the necessary lower bound for K K and, at the end, 𝒩 \mathcal{N} will be the maximum of them. This provides us with a specific value for 𝒩 \mathcal{N} (that is not relevant at all) and in what follows we simply suppose that we take a 𝒞 K \mathscr{C}^{K} normalising diffeomorphism Φ \Phi with K ⩾ 𝒩. K\geqslant\mathcal{N}.

For convenience we assume, without lost of generality, that

 | U = { ( u 1, u 2) ∈ ℝ 2: | u 1 | < δ ​ and ​ | u 2 | < δ } = ( − δ, δ) 2 U=\{(u_{1},u_{2})\in\mathbb{R}^{2}:|u_{1}|<\delta\text{ and }|u_{2}|<\delta\}=(-\delta,\delta)^{2} |  |

for some δ > 0 \delta>0 small enough such that, see Remark 1, Φ ⁡ ( ( − δ, δ) 2 × V) ⊂ ( − ρ, ρ) 2 × V. \Phi\big((-\delta,\delta)^{2}\times V)\subset(-\rho,\rho)^{2}\times V. Taking ε 1, ε 2 ∈ ( 0, δ) \varepsilon_{1},\varepsilon_{2}\in(0,\delta) we consider auxiliary 𝒞 K \mathscr{C}^{K} transverse sections Σ 1 ℓ \Sigma_{1}^{\ell} and Σ 2 ℓ \Sigma_{2}^{\ell} to x 1 = 0 x_{1}=0 and x 2 = 0 x_{2}=0, see Figure 3, parametrized by

 | τ 1 ​ ( s, ε 1, μ ^):= Φ ⁡ ( s, ε 1, μ ^) ​ and ​ τ 2 ​ ( s, ε 2, μ ^):= Φ ⁡ ( ε 2, s, μ ^), \tau_{1}(s;\varepsilon_{1},{{\hat{\mu}}})\!:=\Phi(s,\varepsilon_{1};{{\hat{\mu}}})\text{ and }\tau_{2}(s;\varepsilon_{2},{{\hat{\mu}}})\!:=\Phi(\varepsilon_{2},s;{{\hat{\mu}}}), |  | (9) |

respectively. From now on, in addition to μ ^ {{\hat{\mu}}}, we will also consider ε:= ( ε 1, ε 2) \varepsilon\!:=(\varepsilon_{1},\varepsilon_{2}) as parameter. In this respect we remark that τ i ​ ( s, ε i, μ ^) \tau_{i}(s;\varepsilon_{i},{{\hat{\mu}}}) is a 𝒞 K \mathscr{C}^{K} function on U × V U\times V for i = 1, 2. i=1,2. Similarly as we did with σ i \sigma_{i}, we denote

 | τ i ​ j ​ k ​ ( ε i, μ ^):= ∂ s k τ i ​ j ​ ( 0, ε i, μ ^) \tau_{ijk}(\varepsilon_{i},{{\hat{\mu}}})\!:=\partial_{s}^{k}\tau_{ij}(0;\varepsilon_{i},{{\hat{\mu}}}) |  |

and we will write τ i ​ j ​ k \tau_{ijk} for the sake of shortness.

Figure 3: Auxiliary transverse sections in the decomposition of T. T.

The idea now is to decompose the Dulac map D ⁡ ( s, μ ^) D(s;{{\hat{\mu}}}) and the Dulac time T ⁡ ( s, μ ^) T(s;{{\hat{\mu}}}) as

 | D ⁡ ( s) = R 2 ​ ( D 0 ​ ( R 1 ​ ( s))) ​ and ​ T ​ ( s) = T 1 ​ ( s) + T 0 ​ ( R 1 ​ ( s)) + T 2 ​ ( D 0 ​ ( R 1 ​ ( s))). D(s)=R_{2}(D_{0}(R_{1}(s)))\text{ and }T(s)=T^{1}(s)+T^{0}(R_{1}(s))+T^{2}(D_{0}(R_{1}(s))). |  | (10) |

Here R 1 ​ ( ⋅, ε 1, μ ^) R_{1}(\,\cdot\,;\varepsilon_{1},{{\hat{\mu}}}), D 0 ​ ( ⋅, ε, μ ^) D_{0}(\,\cdot\,;\varepsilon,{{\hat{\mu}}}) and R 2 ​ ( ⋅, ε 2, μ ^) R_{2}(\,\cdot\,;\varepsilon_{2},{{\hat{\mu}}}) are, respectively, the transitions maps from Σ 1 \Sigma_{1} to Σ 1 ℓ \Sigma_{1}^{\ell}, from Σ 1 ℓ \Sigma_{1}^{\ell} to Σ 2 ℓ \Sigma_{2}^{\ell}, and from Σ 2 ℓ \Sigma_{2}^{\ell} to Σ 2 \Sigma_{2}, whereas T 1 ​ ( ⋅, ε 1, μ ^) T^{1}(\,\cdot\,;\varepsilon_{1},{{\hat{\mu}}}), T 0 ​ ( ⋅, ε, μ ^) T^{0}(\,\cdot\,;\varepsilon,{{\hat{\mu}}}) and T 2 ​ ( ⋅, ε 2, μ ^) T^{2}(\,\cdot\,;\varepsilon_{2},{{\hat{\mu}}}) are, respectively, the time that spends the flow to do this transition. It is well known that D 0 D_{0} and T 0 T^{0} are singular at s = 0 s=0, whereas the other ones are regular. We study the latter by applying the results obtained in Appendix A and to this end, see ( 42) (\ref{ap1}\immediate), we rewrite the given vector field as

 | X μ ^ = 1 x 1 n 1 ​ x 2 n 2 ( x 1 P 1 ( x 1, x 2) ∂ x 1 + x 2 P 2 ( x 1, x 2) ∂ x 2) = 1 x i 2 n i 2 ​ f i 2 ​ ( x i 1, x i 2) ( ∂ x i 1 + h i 2 ( x i 1, x i 2) x i 2 ∂ x i 2) X_{{\hat{\mu}}}=\frac{1}{x_{1}^{n_{1}}x_{2}^{n_{2}}}\left(x_{1}P_{1}(x_{1},x_{2})\partial_{x_{1}}+x_{2}P_{2}(x_{1},x_{2})\partial_{x_{2}}\right)=\frac{1}{x_{i_{2}}^{n_{i_{2}}}f_{i_{2}}(x_{i_{1}},x_{i_{2}})}\left(\partial_{x_{i_{1}}}+h_{i_{2}}(x_{i_{1}},x_{i_{2}})x_{i_{2}}\partial_{x_{i_{2}}}\right) |  |

where ( i 1, i 2) ∈ { ( 2, 1), ( 1, 2) } (i_{1},i_{2})\in\{(2,1),(1,2)\} and

 | f 1 ​ ( u, v) = u n 2 − 1 P 2 ​ ( v, u) h 1 ​ ( u, v) = P 1 ​ ( v, u) u ​ P 2 ​ ( v, u) f 2 ​ ( u, v) = u n 1 − 1 P 1 ​ ( u, v) h 2 ​ ( u, v) = P 2 ​ ( u, v) u ​ P 1 ​ ( u, v) \begin{array}[]{lll}\displaystyle f_{1}(u,v)=\frac{u^{n_{2}-1}}{P_{2}(v,u)}&&\displaystyle h_{1}(u,v)=\frac{P_{1}(v,u)}{uP_{2}(v,u)}\\[10.0pt] \displaystyle f_{2}(u,v)=\frac{u^{n_{1}-1}}{P_{1}(u,v)}&&\displaystyle h_{2}(u,v)=\frac{P_{2}(u,v)}{uP_{1}(u,v)}\end{array} |  | (11) |

(At this point, and in what follows, we omit the dependence on the parameters for the sake of shortness when there is no risk of ambiguity. Moreover all though the proof the scripts 1 1 and 2 2 refer, respectively, to the first and second regular passage.) Setting I:= ( 0, δ), I\!:=(0,\delta), we apply (twice) Lemma A.3 with ν = ( ε i, μ ^) ∈ I × V \nu=(\varepsilon_{i},{{\hat{\mu}}})\in I\times V for i = 1, 2. i=1,2. In doing so, and taking Lemma 2.1 also into account, we can assert that

 | R i ​ ( s, ε i, μ ^) = ∑ k = 1 L i R i ​ k ​ ( ε i, μ ^) ​ s k + ℱ L i + 1 0 ​ ( I × V) ​ and ​ T i ​ ( s, ε i, μ ^) = ∑ k = n i L i T k i ​ ( ε i, μ ^) ​ s k + ℱ L i + 1 0 ​ ( I × V), R_{i}(s;\varepsilon_{i},{{\hat{\mu}}})=\sum_{k=1}^{L_{i}}R_{ik}(\varepsilon_{i},{{\hat{\mu}}})s^{k}+\mathcal{F}_{{L_{i}}+1}^{0}(I\!\times\!V)\text{ and }T^{i}(s;\varepsilon_{i},{{\hat{\mu}}})=\sum_{k=n_{i}}^{L_{i}}T^{i}_{k}(\varepsilon_{i},{{\hat{\mu}}})s^{k}+\mathcal{F}_{{L_{i}}+1}^{0}(I\!\times\!V), |  | (12) |

with R i ​ k, T k i ∈ 𝒞 0 ​ ( I × V) R_{ik},T^{i}_{k}\in\mathscr{C}^{0}(I\times V) provided that K ⩾ L i + 1 {K}\geqslant{L_{i}}+1 for i = 1, 2 i=1,2. We know furthermore that R i ​ 1 > 0 R_{i1}>0. Turning to the assumption K ⩾ 𝒩 K\geqslant\mathcal{N}, let us advance that we will also require that L i ⩾ 𝒩 L_{i}\geqslant\mathcal{N} for i = 1, 2 i=1,2, which is neither a problem because, as we explained before, 𝒩 = 𝒩 ⁡ ( λ 0, n 1, n 2, i 1, i 2, j 1, j 2) \mathcal{N}=\mathcal{N}(\lambda_{0},n_{1},n_{2},i_{1},i_{2},j_{1},j_{2}) and we can take K K large enough from the very beginning.

With regard to the passage from Σ 1 ℓ \Sigma_{1}^{\ell} to Σ 2 ℓ, \Sigma_{2}^{\ell}, taking ( 8) (\ref{Aeq3}\immediate) and ( 9) (\ref{Aeq2}\immediate) into account (see also Figure 3), an easy computation shows that

 | D 0 ​ ( s) \displaystyle D_{0}(s) | = d s λ with d:= ε 1 ​ ε 2 − λ \displaystyle=ds^{\lambda}\text{ with $d\!:=\varepsilon_{1}\varepsilon_{2}^{-\lambda}$} |  | (13) |

and |

 | T 0 ​ ( s) \displaystyle T^{0}(s) | = ∫ s ε 2 u 1 n 1 ​ u 2 n 2 P 1 ​ ( 0, 0) | u 2 = ε 1 ​ ( s u 1) λ ​ d ​ u 1 u 1 = T 1 0 ​ s n 1 + T 2 0 ​ ( d ​ s λ) n 2, \displaystyle=\int_{s}^{\varepsilon_{2}}\left.\frac{u_{1}^{n_{1}}u_{2}^{n_{2}}}{P_{1}(0,0)}\right|_{u_{2}=\varepsilon_{1}\left(\frac{s}{u_{1}}\right)^{\lambda}}\frac{du_{1}}{u_{1}}=T_{1}^{0}s^{n_{1}}+T_{2}^{0}(ds^{\lambda})^{n_{2}}, |  | (14) |

where |

 | T 1 0 \displaystyle T_{1}^{0} | := − ε 1 n 2 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0) ​ and ​ T 2 0:= ε 2 n 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0). \displaystyle\!:=\frac{-\varepsilon_{1}^{n_{2}}}{(n_{1}-\lambda n_{2})P_{1}(0,0)}\text{ and }T_{2}^{0}\!:=\frac{\varepsilon_{2}^{n_{1}}}{(n_{1}-\lambda n_{2})P_{1}(0,0)}. |  |

(Here, on account of λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q}, we reduce V V so that n 1 − λ ​ n 2 ≠ 0 n_{1}-\lambda n_{2}\neq 0 for all μ ^ ∈ V. {{\hat{\mu}}}\in V.) Hence D ⁡ ( s) = R 2 ​ ( d ​ R 1 λ ​ ( s)) D(s)=R_{2}(dR_{1}^{\lambda}(s)). If we take any strictly positive β ​ ( μ ^) ∈ 𝒞 0 ​ ( V) \beta({{\hat{\mu}}})\in\mathscr{C}^{0}(V) then, due to R 11 > 0 R_{11}>0,

 | R 1 β ​ ( s) = s β ​ R 11 β ​ ( 1 + ∑ k = 2 L 1 R 1 ​ k R 11 ​ s k − 1) β + ℱ L 1 0 ​ ( I × V) = s β ​ R 11 β ​ ∑ ℓ = 0 L 1 − 1 Υ ℓ [β] ​ s ℓ + ℱ L 1 0 ​ ( I × V), R_{1}^{\beta}(s)=s^{\beta}R_{11}^{\beta}\left(1+\sum_{k=2}^{L_{1}}\frac{R_{1k}}{R_{11}}s^{k-1}\right)^{\beta}+\mathcal{F}_{L_{1}}^{0}(I\times V)=s^{\beta}R_{11}^{\beta}\sum_{\ell=0}^{L_{1}-1}\Upsilon^{[\beta]}_{\ell}s^{\ell}+\mathcal{F}_{L_{1}}^{0}(I\times V), |  | (15) |

where in the first equality we apply by ( a) (a) in Lemma 2.5 and in the second one we define Υ ℓ [β] = Υ ℓ [β] ​ ( ε 1, μ ^) \Upsilon^{[\beta]}_{\ell}=\Upsilon^{[\beta]}_{\ell}(\varepsilon_{1},{{\hat{\mu}}}) for ℓ = 0, 1, …, L 1 − 1 \ell=0,1,\ldots,L_{1}-1 as the 𝒞 0 ​ ( I × V) \mathscr{C}^{0}(I\times V) functions verifying

 | ( 1 + ∑ k = 2 L 1 R 1 ​ k R 11 ​ s k − 1) β = ∑ ℓ = 0 L 1 − 1 Υ ℓ [β] ​ s ℓ + ℱ L 1 0 ​ ( I × V). \left(1+\sum_{k=2}^{L_{1}}\frac{R_{1k}}{R_{11}}s^{k-1}\right)^{\beta}=\sum_{\ell=0}^{L_{1}-1}\Upsilon^{[\beta]}_{\ell}s^{\ell}+\mathcal{F}_{L_{1}}^{0}(I\times V). |  | (16) |

(Here we apply Taylor’s theorem at order L 1 L_{1} to the function x ↦ ( 1 + x) β x\mapsto(1+x)^{\beta} taking a uniform estimate of the remainder by means of its integral form.) Note in particular that Υ 0 [β] = 1. \Upsilon_{0}^{[\beta]}=1. Taking ( 15) (\ref{Aeq5}\immediate) with β ⁡ ( μ ^) = λ \beta({{\hat{\mu}}})=\lambda and applying ( b) (b) in Lemma 2.5 we obtain

 | D ⁡ ( s) = R 2 ​ ( d ​ R 1 λ ​ ( s)) = ∑ k = 1 L 2 R 2 ​ k ​ d k ​ R 1 λ ​ k ​ ( s) + ℱ L 1 0 ​ ( { ( ε, μ ^) ∈ I 2 × V: λ > L 1 L 2 + 1 }) D(s)=\textstyle R_{2}(dR_{1}^{\lambda}(s))=\sum\limits_{k=1}^{L_{2}}R_{2k}d^{k}R_{1}^{\lambda k}(s)+\mathcal{F}_{L_{1}}^{0}\!\left(\left\{(\varepsilon,{{\hat{\mu}}})\in I^{2}\!\times\!V:\lambda>\frac{L_{1}}{L_{2}+1}\right\}\right) |  |

Now we choose L 1 L_{1} and L 2 L_{2} such that λ 0 > L 1 L 2 + 1 \lambda_{0}>\frac{L_{1}}{L_{2}+1} and we shrink V V if necessary in order that λ > L 1 L 2 + 1 \lambda>\frac{L_{1}}{L_{2}+1} for all μ ^ ∈ V. {{\hat{\mu}}}\in V. In doing so we get that

 | D ⁡ ( s) = R 2 ​ ( d ​ R 1 λ ​ ( s)) = ∑ k = 1 L 2 R 2 ​ k ​ d k ​ R 1 λ ​ k ​ ( s) + ℱ L 1 0 ​ ( I 2 × V). D(s)=\textstyle R_{2}(dR_{1}^{\lambda}(s))=\sum\limits_{k=1}^{L_{2}}R_{2k}d^{k}R_{1}^{\lambda k}(s)+\mathcal{F}_{L_{1}}^{0}(I^{2}\!\times\!V). |  |

Next, by taking ( 15) (\ref{Aeq5}\hbox{}) with β ⁡ ( μ ^) = λ ​ k \beta({{\hat{\mu}}})=\lambda k, k = 1, 2, …, L 2 k=1,2,\ldots,L_{2},

 | D ⁡ ( s) \displaystyle D(s) | = ∑ k = 1 L 2 ∑ ℓ = 0 L 1 − 1 R 2 ​ k ​ R 11 λ ​ k ​ d k ​ Υ ℓ [λ ​ k] ​ s ℓ + λ ​ k + ℱ L 1 0 ​ ( I 2 × V) \displaystyle=\sum\limits_{k=1}^{L_{2}}\sum\limits_{\ell=0}^{L_{1}-1}R_{2k}R_{11}^{\lambda k}d^{k}\Upsilon^{[\lambda k]}_{\ell}s^{\ell+\lambda k}+\mathcal{F}_{L_{1}}^{0}(I^{2}\!\times\!V) |  |

 |  | = s λ ​ ∑ ℓ = 0 L 1 − 1 ∑ k = 0 L 2 − 1 R 2, k + 1 ​ R 11 λ ⁡ ( k + 1) ​ d k + 1 ​ Υ ℓ [λ ⁡ ( k + 1)] ​ s ℓ + λ ​ k + ℱ L 1 0 ​ ( I 2 × V). \displaystyle=s^{\lambda}\sum\limits_{\ell=0}^{L_{1}-1}\sum\limits_{k=0}^{L_{2}-1}R_{2,k+1}R_{11}^{\lambda(k+1)}d^{k+1}\Upsilon_{\ell}^{[\lambda(k+1)]}s^{\ell+\lambda k}+\mathcal{F}_{L_{1}}^{0}(I^{2}\!\times\!V). |  |

Since λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q}, assertion ( a ​ 1) (a1) in Theorem 1.6 shows that

 | Δ ℓ ​ k = R 2, k + 1 ​ R 11 λ ⁡ ( k + 1) ​ d k + 1 ​ Υ ℓ [λ ⁡ ( k + 1)] ​ for all ( ε, μ ^) ∈ I 2 × V. \Delta_{\ell k}=R_{2,k+1}R_{11}^{\lambda(k+1)}d^{k+1}\Upsilon_{\ell}^{[\lambda(k+1)]}\text{ for all $(\varepsilon,{{\hat{\mu}}})\in I^{2}\!\times\!V.$} |  | (17) |

Here we also take Remark 2 into account, shrinking (if necessary) the neighbourhood V V of μ ^ 0 = ( λ 0, μ 0) {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0}) in order that all the exponents ℓ + λ ​ k \ell+\lambda k are different for every μ ^ ∈ V. {{\hat{\mu}}}\in V. At this point it is worth to make the following remarks with regard to the previous equality:

- •

It gives the expression of Δ i ​ j \Delta_{ij} provided that 0 ⩽ i ⩽ L 1 − 1 0\leqslant i\leqslant L_{1}-1, 0 ⩽ j ⩽ L 2 − 1 0\leqslant j\leqslant L_{2}-1 and i + λ 0 ​ j < L 1. i+\lambda_{0}j<L_{1}. Since we are just interested in ( i, j) ∈ { ( 0, 0), ( 0, 1), ( 1, 0), ( 1, 1), ( i 1, j 1) } (i,j)\in\{(0,0),(0,1),(1,0),(1,1),(i_{1},j_{1})\}, these conditions reduce to specific lower bounds for L 1 L_{1} and L 2 L_{2} that depend only on λ 0, \lambda_{0}, i 1 i_{1} and j 1. j_{1}. For instance, in order to prove that the factorization in ( 6) (\ref{Aeq30}\hbox{}) holds for ( i, j) = ( i 1, j 1) (i,j)=(i_{1},j_{1}) we need that

 | L 1 > max ⁡ ( i 1 + λ 0 ​ j, i 1 + 1) ​ and ​ L 2 > j 2 + 1. L_{1}>\max(i_{1}+\lambda_{0}j,i_{1}+1)\text{ and }L_{2}>j_{2}+1. |  |

This does not constitute a problem because we can take K {K}, and therefore L 1 L_{1} and L 2 L_{2}, arbitrarily large.

- •

The coefficient Δ ℓ ​ k \Delta_{\ell k} is a function that depends only on μ ^ {{\hat{\mu}}}, whereas each function on the right hand side of ( 17) (\ref{Aeq6}\immediate) depends on μ ^ {{\hat{\mu}}} but also on ε \varepsilon. This constitutes a key point that we will exploit in the forthcoming arguments. Particularized to ℓ = 0 \ell=0, from ( 13) (\ref{Aeq13}\immediate) and ( 17) (\ref{Aeq6}\hbox{}) we get that

 | Δ 0 ​ k = ( R 2, k + 1 ​ ε 2 − λ ⁡ ( k + 1)) ​ ( R 11 λ ​ ε 1) k + 1 \Delta_{0k}=\big(R_{2,k+1}\varepsilon_{2}^{-\lambda(k+1)}\big)\big(R_{11}^{\lambda}\varepsilon_{1}\big)^{k+1} |  | (18) |

does not depend on ε = ( ε 1, ε 2). \varepsilon=(\varepsilon_{1},\varepsilon_{2}). Since the first factor does not depend on ε 1 \varepsilon_{1} and the second one does not depend on ε 2 \varepsilon_{2}, taking k = 0 k=0 and using that Δ 00 ​ ( μ ^) ≠ 0 \Delta_{00}({{\hat{\mu}}})\neq 0 for all μ ^ ∈ W ^, {{\hat{\mu}}}\in\hat{W}, we conclude that

 | R 2, 1 ​ ( ε 2, μ ^) ​ ε 2 − λ ​ and ​ R 11 λ ​ ( ε 1, μ ^) ​ ε 1 ​ do not depend on ε, R_{2,1}(\varepsilon_{2},{{\hat{\mu}}})\varepsilon_{2}^{-\lambda}\text{ and }R_{11}^{\lambda}(\varepsilon_{1},{{\hat{\mu}}})\varepsilon_{1}\text{ do not depend on $\varepsilon$,} |  |

which in its turn, again from ( 18) (\ref{Aeq15}\immediate), implies that

 | R 2, k + 1 ​ ( ε 2, μ ^) ​ ε 2 − λ ⁡ ( k + 1) ​ does not depend on ε for all k ⩾ 1. R_{2,k+1}(\varepsilon_{2},{{\hat{\mu}}})\varepsilon_{2}^{-\lambda(k+1)}\text{ does not depend on $\varepsilon$ for all $k\geqslant 1$.} |  | (19) |

Since Υ 0 [β] = 1 \Upsilon_{0}^{[\beta]}=1 for any function β, \beta, the factorization in ( 17) (\ref{Aeq6}\hbox{}) also shows that

 | Δ ℓ ​ k = Υ ℓ [λ ⁡ ( k + 1)] ​ Δ 0 ​ k. \Delta_{\ell k}=\Upsilon_{\ell}^{[\lambda(k+1)]}\Delta_{0k}. |  | (20) |

Consequently

 | ∑ ℓ = 0 L 1 − 1 Υ ℓ [λ ⁡ ( k + 1)] ​ s ℓ \displaystyle\sum_{\ell=0}^{L_{1}-1}\Upsilon^{[\lambda(k+1)]}_{\ell}s^{\ell} | + ℱ L 1 0 ​ ( I × V) = ( 1 + ∑ ℓ = 2 L 1 R 1 ​ ℓ R 11 ​ s ℓ − 1) λ ⁡ ( k + 1) \displaystyle+\mathcal{F}_{L_{1}}^{0}(I\times V)=\left(1+\sum_{\ell=2}^{L_{1}}\frac{R_{1\ell}}{R_{11}}s^{\ell-1}\right)^{\lambda(k+1)} |  |

 |  | = ( ∑ ℓ = 0 L 1 − 1 Υ ℓ [λ] ​ s ℓ + ℱ L 1 0 ​ ( I × V)) k + 1 = ( ∑ ℓ = 0 L 1 − 1 Δ ℓ ​ 0 Δ 00 ​ s ℓ + ℱ L 1 0 ​ ( I × V)) k + 1 \displaystyle=\left(\;\sum_{\ell=0}^{L_{1}-1}\Upsilon^{[\lambda]}_{\ell}s^{\ell}+\mathcal{F}_{L_{1}}^{0}(I\times V)\right)^{k+1}=\left(\;\sum_{\ell=0}^{L_{1}-1}\frac{\Delta_{\ell 0}}{\Delta_{00}}s^{\ell}+\mathcal{F}_{L_{1}}^{0}(I\times V)\right)^{k+1} |  |

 |  | = ( ∑ ℓ = 0 L 1 − 1 Δ ℓ ​ 0 Δ 00 ​ s ℓ) k + 1 + ℱ L 1 0 ​ ( I × V) = ∑ ℓ = 0 L 1 − 1 Ω ℓ ​ k ​ s ℓ + ℱ L 1 0 ​ ( I × V), \displaystyle=\left(\;\sum_{\ell=0}^{L_{1}-1}\frac{\Delta_{\ell 0}}{\Delta_{00}}s^{\ell}\right)^{k+1}+\mathcal{F}_{L_{1}}^{0}(I\times V)=\sum_{\ell=0}^{L_{1}-1}\Omega_{\ell k}s^{\ell}+\mathcal{F}_{L_{1}}^{0}(I\times V), |  |

where in the first and second equalities we use the definition of Υ ℓ [β] \Upsilon_{\ell}^{[\beta]} in ( 16) (\ref{Aeq18}\immediate) with β ⁡ ( μ ^) = λ ⁡ ( k + 1) \beta({{\hat{\mu}}})=\lambda(k+1) and β ⁡ ( μ ^) = λ \beta({{\hat{\mu}}})=\lambda, respectively, in the third one we use ( 20) (\ref{Aeq35}\immediate) with k = 0 k=0, in the fourth one we apply the binomial formula and Lemma 2.4 and, finally, the last one follows from the definition in ( 5) (\ref{Aeq33}\immediate). Clearly this implies that

 | Υ ℓ [λ ⁡ ( k + 1)] = Ω ℓ ​ k ​ for ℓ = 0, 1, …, L 1 − 1. \Upsilon_{\ell}^{[\lambda(k+1)]}=\Omega_{\ell k}\text{ for $\ell=0,1,\ldots,L_{1}-1$.} |  | (21) |

Particularized to ( ℓ, k) = ( i 1, j 1) (\ell,k)=(i_{1},j_{1}), from ( 20) (\ref{Aeq35}\hbox{}) once again we obtain that

 | Δ i 1 ​ j 1 = Υ i 1 [λ ⁡ ( j 1 + 1)] ​ Δ 0 ​ j 1 = Ω i 1 ​ j 1 ​ Δ 0 ​ j 1. \Delta_{i_{1}j_{1}}=\Upsilon_{i_{1}}^{[\lambda(j_{1}+1)]}\Delta_{0j_{1}}=\Omega_{i_{1}j_{1}}\Delta_{0j_{1}}. |  |

This identity holds for all μ ^ ∈ V. {{\hat{\mu}}}\in V. On account of the considerations explained in the beginning of the proof this shows that the assertion in ( 6) (\ref{Aeq30}\hbox{}) is true for ( i, j) = ( i 1, j 1) (i,j)=(i_{1},j_{1}) as desired.

We turn now to the study of the coefficients of the Dulac time. For convenience we write it as

 | T ⁡ ( s) = T − ​ ( s) + T + ​ ( s), T(s)=T^{-}(s)+T^{+}(s), |  |

where we define, recall ( 10) (\ref{Aeq7}\immediate) and ( 14) (\ref{Aeq8}\immediate),

 | T − ​ ( s):= T 1 ​ ( s) + T 1 0 ​ R 1 n 1 ​ ( s) ​ and ​ T + ​ ( s):= ( T 2 ​ ( u) + T 2 0 ​ u n 2) | u = D 0 ​ ( R 1 ​ ( s)). T^{-}(s)\!:=T^{1}(s)+T^{0}_{1}R_{1}^{n_{1}}(s)\text{ and }T^{+}(s)\!:=\big(T^{2}(u)+T^{0}_{2}u^{n_{2}}\big)\big|_{u=D_{0}(R_{1}(s))}. |  |

With respect to the first summand we observe that, from ( 12) (\ref{Aeq9}\immediate) and taking ( 15) (\ref{Aeq5}\hbox{}) with β ⁡ ( μ ^) = n 1 \beta({{\hat{\mu}}})=n_{1},

 | T − ​ ( s) = ∑ k = n 1 L 1 − 1 T k ​ 0 − ​ s k + ℱ L 1 0 ​ ( I × V) ​ where ​ T k ​ 0 −:= T k 1 + T 1 0 ​ R 11 n 1 ​ Υ k − n 1 [n 1]. T^{-}(s)=\sum_{k=n_{1}}^{L_{1}-1}T_{k0}^{-}s^{k}+\mathcal{F}_{L_{1}}^{0}(I\times V)\text{ where }T_{k0}^{-}\!:=T_{k}^{1}+T_{1}^{0}R_{11}^{n_{1}}\Upsilon_{k-n_{1}}^{[n_{1}]}. |  | (22) |

On the other hand, from ( 12) (\ref{Aeq9}\hbox{}), we can write T 2 ​ ( u) + T 2 0 ​ u n 2 = ∑ k = n 2 L 2 T ¯ k 2 ​ u k + ℱ L 2 + 1 0 ​ ( I × V) T^{2}(u)+T^{0}_{2}u^{n_{2}}=\sum\limits_{k=n_{2}}^{L_{2}}\bar{T}_{k}^{2}u^{k}+\mathcal{F}_{L_{2}+1}^{0}(I\times V) where

 | T ¯ k 2:= { T k 2 + T 2 0 if k = n 2, T k 2 if k > n 2. \bar{T}^{2}_{k}\!:=\left\{\begin{array}[]{cc}T^{2}_{k}+T^{0}_{2}&\text{if $k=n_{2}$,}\\[3.0pt] T^{2}_{k}&\text{if $k>n_{2}$.}\end{array}\right. |  | (23) |

Consequently, taking ( 15) (\ref{Aeq5}\hbox{}) with β ⁡ ( μ ^) = λ \beta({{\hat{\mu}}})=\lambda and applying ( b) (b) in Lemma 2.5 we obtain

 | T + ​ ( s) = ( T 2 ​ ( u) + T 2 0 ​ u n 2) | u = d ​ R 1 λ ​ ( s) \displaystyle T^{+}(s)=\big(T^{2}(u)+T^{0}_{2}u^{n_{2}}\big)\big|_{u=dR_{1}^{\lambda}(s)} | = ∑ k = n 2 L 2 T ¯ k 2 ​ d k ​ R 1 λ ​ k + ℱ L 1 0 ​ ( I 2 × V) \displaystyle=\sum\limits_{k=n_{2}}^{L_{2}}\bar{T}^{2}_{k}d^{k}R_{1}^{\lambda k}+\mathcal{F}_{L_{1}}^{0}(I^{2}\!\times\!V) |  |

 |  | = ∑ k = n 2 L 2 T ¯ k 2 ​ d k ​ ( s λ ​ k ​ R 11 λ ​ k ​ ∑ ℓ = 0 L 1 − 1 Υ ℓ [λ ​ k] ​ s ℓ + ℱ L 1 0 ​ ( I × V)) + ℱ L 1 0 ​ ( I 2 × V) \displaystyle=\sum\limits_{k=n_{2}}^{L_{2}}\bar{T}^{2}_{k}d^{k}\left(s^{\lambda k}R_{11}^{\lambda k}\sum\limits_{\ell=0}^{L_{1}-1}\Upsilon_{\ell}^{[\lambda k]}s^{\ell}+\mathcal{F}_{L_{1}}^{0}(I\times V)\right)+\mathcal{F}_{L_{1}}^{0}(I^{2}\!\times\!V) |  |

 |  | = ∑ k = n 2 L 2 ∑ ℓ = 0 L 1 − 1 T ℓ ​ k + ​ s ℓ + λ ​ k + ℱ L 1 0 ​ ( I 2 × V). \displaystyle=\sum\limits_{k=n_{2}}^{L_{2}}\sum\limits_{\ell=0}^{L_{1}-1}T^{+}_{\ell k}s^{\ell+\lambda k}+\mathcal{F}_{L_{1}}^{0}(I^{2}\!\times\!V). |  | (24) |

Here we also use λ > L 1 L 2 + 1 \lambda>\frac{L_{1}}{L_{2}+1} for all μ ^ ∈ V {{\hat{\mu}}}\in V in the first equality, in the second one we take ( 15) (\ref{Aeq5}\hbox{}) with β ⁡ ( μ ^) = λ ​ k \beta({{\hat{\mu}}})=\lambda k, whereas in the last one we use that d = ε 1 ​ ε 2 − λ d=\varepsilon_{1}\varepsilon_{2}^{-\lambda} and define

 | T ℓ ​ k +:= ( T ¯ k 2 ​ ε 2 − λ ​ k) ​ ( ε 1 ​ R 11 λ) k ​ Υ ℓ [λ ​ k]. T_{\ell k}^{+}\!:=(\bar{T}^{2}_{k}\varepsilon_{2}^{-\lambda k})(\varepsilon_{1}R_{11}^{\lambda})^{k}\Upsilon_{\ell}^{[\lambda k]}. |  | (25) |

Note that T ℓ ​ 0 + = 0 T_{\ell 0}^{+}=0 for all ℓ ⩾ 1 \ell\geqslant 1 due to Υ ℓ [0] = 0 \Upsilon_{\ell}^{[0]}=0 for all ℓ ⩾ 1. \ell\geqslant 1. Consequently, since T ℓ ​ k T_{\ell k} is by definition the coefficient of s ℓ + λ ​ k s^{\ell+\lambda k} in T ⁡ ( s) = T − ​ ( s) + T + ​ ( s) T(s)=T^{-}(s)+T^{+}(s), from ( 22) (\ref{Aeq10}\immediate) and ( 24) (\ref{Aeq11}\immediate) we get that

 | T ℓ ​ k = { T ℓ ​ k + if k > 0. T ℓ ​ 0 − if k = 0 and ℓ ⩾ 1. T_{\ell k}=\left\{\begin{array}[]{ll}T_{\ell k}^{+}&\text{ if $k>0.$}\\ T_{\ell 0}^{-}&\text{ if $k=0$ and $\ell\geqslant 1.$}\end{array}\right. |  | (26) |

(To be more precise, the above equality follows from Remark 2 and by applying ( b ​ 1) (b1) in Theorem 1.6 thanks to λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q} and shrinking, if necessary, the neighbourhood V V of μ ^ 0 = ( λ 0, μ 0) {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0}) in order that all the exponents ℓ + λ ​ k \ell+\lambda k are different for every μ ^ ∈ V.) {{\hat{\mu}}}\in V.) Finally, since the coefficient T 00 T_{00} only exists in case the that n 1 ​ n 2 = 0 n_{1}n_{2}=0 and n ≠ ( 0, 0) n\neq(0,0) by hypothesis, we have that

 | T 00 = { T 00 − if n 1 = 0, T 00 + if n 2 = 0. T_{00}=\left\{\begin{array}[]{ll}T_{00}^{-}&\text{if $n_{1}=0$,}\\[3.0pt] T_{00}^{+}&\text{if $n_{2}=0$.}\end{array}\right. |  |

Similarly as we noted previously for Δ i ​ j \Delta_{ij}, let us remark that since we are only interested in the coefficients

 | T i ​ j ​ with ​ ( i, j) ∈ { ( n 1, 0), ( n 1 + 1, 0), ( 0, n 2), ( 0, n 2 + 1), ( i 2, j 2) }, T_{ij}\text{ with }(i,j)\in\{(n_{1},0),(n_{1}+1,0),(0,n_{2}),(0,n_{2}+1),(i_{2},j_{2})\}, |  |

from ( 22) (\ref{Aeq10}\hbox{}) and ( 24) (\ref{Aeq11}\hbox{}) we get specific lower bounds for L 1 L_{1} and L 2 L_{2} to be satisfied. Once again, this is not a problem because these lower bounds are given in terms of λ 0 \lambda_{0}, n 1 n_{1}, n 2 n_{2}, i 2 i_{2} and j 2 j_{2} and, on the other hand, we can take K, K, and so L 1 L_{1} and L 2, L_{2}, arbitrarily large. For instance, in order to show that the factorization in ( 7) (\ref{Aeq31}\hbox{}) holds for ( i, j) = ( i 2, j 2) (i,j)=(i_{2},j_{2}) with j 2 > 0 j_{2}>0 we argue as follows. Precisely due to j 2 > 0 j_{2}>0, we get that

 | T i 2 ​ j 2 = T i 2 ​ j 2 + = T 0 ​ j 2 + ​ Υ i 2 [λ ​ j 2] = T 0 ​ j 2 ​ Ω i 2, j 2 − 1, T_{i_{2}j_{2}}=T_{i_{2}j_{2}}^{+}=T_{0j_{2}}^{+}\Upsilon_{i_{2}}^{[\lambda j_{2}]}=T_{0j_{2}}\Omega_{i_{2},j_{2}-1}, |  |

where in the first equality we take ( 26) (\ref{Aeq22}\immediate) into account, the second one follows readily from ( 25) (\ref{Aeq21}\immediate) thanks to Υ 0 [λ ​ j 2] = 1 \Upsilon_{0}^{[\lambda j_{2}]}=1, and in the last one we apply the identity in ( 21) (\ref{Aeq36}\immediate). For this to happen, see also ( 24) (\ref{Aeq11}\hbox{}), we need that

 | L 1 > max ⁡ ( i 2 + 1, i 2 + λ 0 ​ j 2) ​ and ​ L 2 > j 2. L_{1}>\max(i_{2}+1,i_{2}+\lambda_{0}j_{2})\text{ and }L_{2}>j_{2}. |  |

This shows the validity of the factorization for all μ ^ ∈ V. {{\hat{\mu}}}\in V. As we explained at the beginning of the proof, this factorization extends to all μ ^ = ( λ, μ) ∈ W ^ {{\hat{\mu}}}=(\lambda,\mu)\in\hat{W} with λ ∉ D i 2 ​ j 2 n ∪ D i 2 ​ 0 0 \lambda\notin D_{i_{2}j_{2}}^{n}\cup D_{i_{2}0}^{0} by continuity and the fact that D i 2 ​ j 2 n ∪ D i 2 ​ 0 0 D_{i_{2}j_{2}}^{n}\cup D_{i_{2}0}^{0} is a discrete subset of rational numbers in ( 0, + ∞). (0,+\infty).

So far we have proved ( 6) (\ref{Aeq30}\hbox{}) and ( 7) (\ref{Aeq31}\hbox{}), which constitute assertion ( a) (\ref{a}\hbox{}) in the statement. In doing so we have also identified all the elements needed to compute Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} but recall that we must only analyze the cases ( i, j) ∈ { ( 0, 0), ( 1, 0), ( 0, 1), ( 1, 1) } (i,j)\in\{(0,0),(1,0),(0,1),(1,1)\} and ( i, j) ∈ { ( n 1, 0), ( n 1 + 1, 0), ( 0, n 2), ( 0, n 2 + 1) }, (i,j)\in\{(n_{1},0),(n_{1}+1,0),(0,n_{2}),(0,n_{2}+1)\}, respectively. With this aim in view we shall apply Lemma A.3 to obtain the explicit expressions of the coefficients R i ​ 1, R_{i1}, R i ​ 2, R_{i2}, T n i i T^{i}_{n_{i}} and T n i + 1 i T^{i}_{n_{i}+1} in ( 12) (\ref{Aeq9}\hbox{}) for i = 1, 2 i=1,2. Let us advance that the formulae for i = 1 i=1 and i = 2 i=2 are related by switching λ \lambda and 1 / λ 1/\lambda, σ \sigma and τ \tau, the subscripts 1 1 and 2 2 (with the exception of the third subscript k k in σ i ​ j ​ k \sigma_{ijk} and τ i ​ j ​ k \tau_{ijk}) and by exchanging the order of the variables in the functions f i f_{i} and h i h_{i}.

For the reader’s convenience we sum up in Table 1 the fundamental information for applying the results in Appendix A to study the regular passages, see Figure 3, together with the functions L i L_{i} defined in ( 2) (\ref{def_fun}\hbox{}) and the functions f i f_{i} and h i h_{i} given in ( 11) (\ref{Aeq0}\immediate).

 | First regular | Second regular |

 | passage | passage |

ℓ \ell | n 1 n_{1} | n 2 n_{2} |

ν \nu | ( ε 1, μ ^) (\varepsilon_{1},{{\hat{\mu}}}) | ( ε 2, μ ^) (\varepsilon_{2},{{\hat{\mu}}}) |

h ⁡ ( x, y) h(x,y) | P 1 ​ ( y, x) x ​ P 2 ​ ( y, x) \frac{P_{1}(y,x)}{xP_{2}(y,x)} | P 2 ​ ( x, y) x ​ P 1 ​ ( x, y) \frac{P_{2}(x,y)}{xP_{1}(x,y)} |

H ⁡ ( x, y) H(x,y) | ( y x) 1 λ ​ L 1 ​ ( x) L 1 ​ ( y) \left(\frac{y}{x}\right)^{\frac{1}{\lambda}}\!\frac{L_{1}(x)}{L_{1}(y)} | ( y x) λ ​ L 2 ​ ( x) L 2 ​ ( y) \left(\frac{y}{x}\right)^{\lambda}\!\frac{L_{2}(x)}{L_{2}(y)} |

f ⁡ ( x, y) f(x,y) | x n 2 − 1 P 2 ​ ( y, x) \frac{x^{n_{2}-1}}{P_{2}(y,x)} | x n 1 − 1 P 1 ​ ( x, y) \frac{x^{n_{1}-1}}{P_{1}(x,y)} |

ξ ⁡ ( s, ν) \xi(s;\nu) | ( σ 12 ​ ( s, μ ^), σ 11 ​ ( s, μ ^)) \big(\sigma_{12}(s;{{\hat{\mu}}}),\sigma_{11}(s;{{\hat{\mu}}})\big) | ( τ 21 ​ ( s, ε 2, μ ^), τ 22 ​ ( s, ε 2, μ ^)) \big(\tau_{21}(s;\varepsilon_{2},{{\hat{\mu}}}),\tau_{22}(s;\varepsilon_{2},{{\hat{\mu}}})\big) |

ζ ⁡ ( s, ν) \zeta(s;\nu) | ( τ 12 ​ ( s, ε 1, μ ^), τ 11 ​ ( s, ε 1, μ ^)) \big(\tau_{12}(s;\varepsilon_{1},{{\hat{\mu}}}),\tau_{11}(s;\varepsilon_{1},{{\hat{\mu}}})\big) | ( σ 21 ​ ( s, μ ^), σ 22 ​ ( s, μ ^)) \big(\sigma_{21}(s;{{\hat{\mu}}}),\sigma_{22}(s;{{\hat{\mu}}})\big) |

Table 1: Information related with the application of the results in Appendix A. The auxiliary sections Σ 1 ℓ \Sigma_{1}^{\ell} and Σ 2 ℓ \Sigma_{2}^{\ell} are given by τ 1 ​ ( s, ε 1, μ ^) = Φ ⁡ ( s, ε 1, μ ^) \tau_{1}(s;\varepsilon_{1},{{\hat{\mu}}})=\Phi(s,\varepsilon_{1};{{\hat{\mu}}}) and τ 2 ​ ( s, ε 2, μ ^) = Φ ⁡ ( ε 2, s, μ ^) \tau_{2}(s;\varepsilon_{2},{{\hat{\mu}}})=\Phi(\varepsilon_{2},s;{{\hat{\mu}}}), respectively, see ( 9) (\ref{Aeq2}\hbox{}).

On account of this the application of Lemma A.2 yields

 | ρ 11 ​ ( x) \displaystyle\rho_{11}(x) | = α 11 ​ x − 1 λ ​ L 1 ​ ( x) ​ with ​ α 11:= σ 111 ​ σ 120 1 λ L 1 ​ ( σ 120) \displaystyle=\alpha_{11}x^{\frac{-1}{\lambda}}L_{1}(x)\text{ with }\alpha_{11}\!:=\frac{\sigma_{111}\sigma_{120}^{\frac{1}{\lambda}}}{L_{1}(\sigma_{120})} |  | (27) |

for the first regular passage and |

 | ρ 21 ​ ( x) \displaystyle\rho_{21}(x) | = α 21 ​ x − λ ​ L 2 ​ ( x) ​ with ​ α 21:= τ 221 ​ τ 210 λ L 2 ​ ( τ 210) \displaystyle=\alpha_{21}x^{-{\lambda}}L_{2}(x)\text{ with }\alpha_{21}\!:=\frac{\tau_{221}\tau_{210}^{{\lambda}}}{L_{2}(\tau_{210})} |  |

for the second one. (Here, to be consistent with the previous notation, the subscript i i in ρ i ​ j \rho_{ij} refers to the first or second regular passage, whereas j j refers to the derivation’s order.) Next, by applying Lemma A.3,

 | R 11 = α 11 ​ τ 120 − 1 λ ​ L 1 ​ ( τ 120) τ 111 ​ and ​ R 21 = α 21 ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ. R_{11}=\alpha_{11}\frac{\tau_{120}^{\frac{-1}{\lambda}}L_{1}(\tau_{120})}{\tau_{111}}\text{ and }R_{21}=\alpha_{21}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}. |  | (28) |

Observe at this point that α 11 \alpha_{11} does not depend on ε \varepsilon and that, see ( 19) (\ref{Aeq14}\immediate), this is also the case of R 11 λ ​ ε 1. R_{11}^{\lambda}\varepsilon_{1}. From the first equality in ( 28) (\ref{Aeq27}\immediate), this implies that L 1 λ ​ ( τ 120) τ 111 λ ​ τ 120 ​ ε 1 \frac{L_{1}^{\lambda}(\tau_{120})}{\tau_{111}^{\lambda}\tau_{120}}\varepsilon_{1} does not depend on ε \varepsilon. On the other hand, τ 120 = ε 1 ​ ψ 2 ​ ( 0, ε 1) \tau_{120}=\varepsilon_{1}\psi_{2}(0,\varepsilon_{1}) and τ 111 = ψ 1 ​ ( 0, ε 1), \tau_{111}=\psi_{1}(0,\varepsilon_{1}), see ( 9) (\ref{Aeq2}\hbox{}), together with ψ i ​ ( 0, 0) = L 1 ​ ( 0) = 1, \psi_{i}(0,0)=L_{1}(0)=1, imply that lim ε 1 → 0 L 1 λ ​ ( τ 120) τ 111 λ ​ τ 120 ​ ε 1 = 1 \lim_{\varepsilon_{1}\to 0}\frac{L_{1}^{\lambda}(\tau_{120})}{\tau_{111}^{\lambda}\tau_{120}}\varepsilon_{1}=1. Thus L 1 λ ​ ( τ 120) τ 111 λ ​ τ 120 ​ ε 1 = 1 \frac{L_{1}^{\lambda}(\tau_{120})}{\tau_{111}^{\lambda}\tau_{120}}\varepsilon_{1}=1 and, consequently, R 11 λ ​ ε 1 = α 11 λ R_{11}^{\lambda}\varepsilon_{1}=\alpha_{11}^{\lambda}. In short,

 | τ 111 λ ​ τ 120 L 1 λ ​ ( τ 120) = ε 1 and R 11 = α 11 ε 1 − 1 / λ = σ 111 ​ σ 120 1 / λ L 1 ​ ( σ 120) ε 1 − 1 / λ. \frac{\tau_{111}^{\lambda}\tau_{120}}{L_{1}^{\lambda}(\tau_{120})}=\varepsilon_{1}\text{ and }R_{11}=\alpha_{11}\varepsilon_{1}^{-1/\lambda}=\frac{\sigma_{111}\sigma_{120}^{1/\lambda}}{L_{1}(\sigma_{120})}\varepsilon_{1}^{-1/\lambda}. |  | (29) |

Furthermore, from ( 19) (\ref{Aeq14}\hbox{}) again, R 21 ​ ε 2 − λ R_{21}\varepsilon_{2}^{-\lambda} does not depend on ε. \varepsilon. This implies, on account of the second equality in ( 28) (\ref{Aeq27}\hbox{}), that α 21 ​ ε 2 − λ \alpha_{21}\varepsilon_{2}^{-\lambda} does not depend on ε \varepsilon neither. Then, taking ε 2 → 0 \varepsilon_{2}\to 0 exactly as before, we conclude that

 | α 21 = ε 2 λ. \alpha_{21}=\varepsilon_{2}^{\lambda}. |  | (30) |

Therefore R 21 = ε 2 λ ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ R_{21}=\varepsilon_{2}^{\lambda}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}} and consequently, from ( 18) (\ref{Aeq15}\hbox{}),

 | Δ 00 ​ ( μ ^) = ( R 11 λ ​ ε 1) ​ ( R 21 ​ ε 2 − λ) = σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120) ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ ​ for all μ ^ ∈ V. \Delta_{00}({{\hat{\mu}}})=(R_{11}^{\lambda}\varepsilon_{1})(R_{21}\varepsilon_{2}^{-\lambda})=\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}\text{ for all ${{\hat{\mu}}}\in V.$} |  |

On account of the considerations explained in the first paragraph of the proof, this shows the validity of the first equality in ( b) (\ref{b}\hbox{}) for all μ ^ = ( λ, μ) ∈ ( 0, + ∞) × W {{\hat{\mu}}}=(\lambda,\mu)\in(0,+\infty)\times W. Indeed, following the notation introduced there, Δ ~ 00 \tilde{\Delta}_{00} is the function on the right hand side of the above equality, which belongs to 𝒞 ∞ ​ ( ( 0 + ∞) × W) \mathscr{C}^{\infty}\big((0+\infty)\times W\big) by Lemma 2.3, i.e., D ~ 00 0 = ∅, \tilde{D}_{00}^{0}=\emptyset, and we have on the other hand, see Remark 1, D 00 0 = ∅ D_{00}^{0}=\emptyset as well.

Next we proceed with the computation of the second order derivatives in Lemma A.2. Using the first column in Table 1, some long but easy computations show that

 | ρ 12 ​ ( x) \displaystyle\rho_{12}(x) | = α 11 σ 111 ​ x − 1 λ ​ L 1 ​ ( x) ​ ( σ 112 − 2 ​ σ 121 ​ σ 111 σ 120 ​ ( P 1 P 2) ​ ( 0, σ 120) + 2 ​ σ 111 ​ α 11 ​ ∫ σ 120 x L 1 ​ ( u) ​ ∂ 1 ( P 1 P 2) ​ ( 0, u) ⏟ M 1 ​ ( u) ​ u − 1 λ ​ d ​ u u) \displaystyle=\frac{\alpha_{11}}{\sigma_{111}}x^{\frac{-1}{\lambda}}L_{1}(x)\bigg(\sigma_{112}-\frac{2\sigma_{121}\sigma_{111}}{\sigma_{120}}\left(\frac{P_{1}}{P_{2}}\right)\!(0,\sigma_{120})+2\sigma_{111}\alpha_{11}\int_{\sigma_{120}}^{x}\underbrace{L_{1}(u)\,\partial_{1}\!\left(\frac{P_{1}}{P_{2}}\right)\!(0,u)}_{M_{1}(u)}\,u^{\frac{-1}{\lambda}}\frac{du}{u}\bigg) |  |

 |  | = α 12 ​ x − 1 λ ​ L 1 ​ ( x) + 2 ​ α 11 2 ​ x − 2 λ ​ L 1 ​ ( x) ​ M ^ 1 ​ ( 1 / λ, x), \displaystyle=\alpha_{12}x^{\frac{-1}{\lambda}}L_{1}(x)+2\alpha_{11}^{2}x^{\frac{-2}{\lambda}}L_{1}(x)\hat{M}_{1}(1/\lambda,x), |  | (31) |

for all x ∈ I 1 ∩ ( 0, + ∞) x\in I_{1}\cap(0,+\infty) with |

 | α 12 \displaystyle\alpha_{12} | := α 11 σ 111 ​ ( σ 112 − 2 ​ σ 121 ​ σ 111 σ 120 ​ ( P 1 P 2) ​ ( 0, σ 120)) − 2 ​ α 11 2 ​ σ 120 − 1 λ ​ M ^ 1 ​ ( 1 / λ, σ 120). \displaystyle\!:=\frac{\alpha_{11}}{\sigma_{111}}\left(\sigma_{112}-\frac{2\sigma_{121}\sigma_{111}}{\sigma_{120}}\left(\frac{P_{1}}{P_{2}}\right)\!(0,\sigma_{120})\right)-2\alpha_{11}^{2}\sigma_{120}^{\frac{-1}{\lambda}}\hat{M}_{1}(1/\lambda,\sigma_{120}). |  | (32) |

Here we use for the first time the properties of the incomplete Mellin transform introduced in Appendix B. More concretely, by Lemma 2.3, M 1 ​ ( u, μ ^) ∈ 𝒞 ∞ ​ ( I 1 × W ^) M_{1}(u;{{\hat{\mu}}})\in\mathscr{C}^{\infty}(I_{1}\times\hat{W}) with 0 ∈ I 1 0\in I_{1}. Hence, by applying Theorem B.1 there exists a unique M ^ 1 ​ ( α, u, μ ^) ∈ 𝒞 ∞ ​ ( ( ℝ ∖ ℤ ≥ 0) × I 1 × W ^) \hat{M}_{1}(\alpha,u;{{\hat{\mu}}})\in\mathscr{C}^{\infty}((\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I_{1}\times\hat{W}) such that ∂ u ( M ^ 1 ​ ( α, u) ​ u − α) = M 1 ​ ( u) ​ u − α − 1 \partial_{u}\big(\hat{M}_{1}(\alpha,u)u^{-\alpha}\big)=M_{1}(u)u^{-\alpha-1} for all u ∈ I 1 ∩ ( 0, + ∞) u\in I_{1}\cap(0,+\infty). Analogously, taking the second column in Table 1, one can also verify that

 | ρ 22 ​ ( x) \displaystyle\rho_{22}(x) | = α 22 ​ x − λ ​ L 2 ​ ( x) + 2 ​ α 21 2 ​ x − 2 ​ λ ​ L 2 ​ ( x) ​ M ^ 2 ​ ( λ, x) ​ for all x ∈ I 2 ∩ ( 0, + ∞), \displaystyle=\alpha_{22}x^{-\lambda}L_{2}(x)+2\alpha_{21}^{2}x^{-2\lambda}L_{2}(x)\hat{M}_{2}(\lambda,x)\text{ for all $x\in I_{2}\cap(0,+\infty)$,} |  | (33) |

with |

 | α 22 \displaystyle\alpha_{22} | := α 21 τ 221 ​ ( τ 222 − 2 ​ τ 211 ​ τ 221 τ 210 ​ ( P 2 P 1) ​ ( τ 210, 0)) − 2 ​ α 21 2 ​ τ 210 − λ ​ M ^ 2 ​ ( λ, τ 210). \displaystyle\!:=\frac{\alpha_{21}}{\tau_{221}}\left(\tau_{222}-\frac{2\tau_{211}\tau_{221}}{\tau_{210}}\left(\frac{P_{2}}{P_{1}}\right)\!(\tau_{210},0)\right)-2\alpha_{21}^{2}\tau_{210}^{-\lambda}\hat{M}_{2}(\lambda,\tau_{210}). |  |

We claim that α 22 = ε 2 λ ​ φ 1 ​ ( ε 2, μ ^) \alpha_{22}=\varepsilon_{2}^{\lambda}\varphi_{1}(\varepsilon_{2},{{\hat{\mu}}}) with φ 1 ∈ 𝒞 K ​ ( ( − δ, δ) × V). \varphi_{1}\in\mathscr{C}^{K}\big((-\delta,\delta)\times V\big). Indeed, this is so due to the following facts:

1. 1.

P 1 ​ ( x 1, x 2, μ ^) P_{1}(x_{1},x_{2};{{\hat{\mu}}}) and P 2 ​ ( x 1, x 2, μ ^) P_{2}(x_{1},x_{2};{{\hat{\mu}}}) are 𝒞 ∞ \mathscr{C}^{\infty} and do not vanish on x 2 = 0 x_{2}=0 and x 1 = 0 x_{1}=0, respectively.

2. 2.

L 2 ​ ( u, μ ^) L_{2}(u;{{\hat{\mu}}}) and M 2 ​ ( u, μ ^) M_{2}(u;{{\hat{\mu}}}) are 𝒞 ∞ ​ ( I 2 × W ^) \mathscr{C}^{\infty}(I_{2}\times\hat{W}) by Lemma 2.3 and the first one does not vanish.

3. 3.

The parametrization τ 2 ​ ( s, ε 2, μ ^) \tau_{2}(s;\varepsilon_{2},{{\hat{\mu}}}) of the section Σ 2 ℓ \Sigma_{2}^{\ell} is defined by means of Φ ∈ 𝒞 K ​ ( U × V) \Phi\in\mathscr{C}^{K}(U\times V), see ( 9) (\ref{Aeq2}\hbox{}), where recall that U = ( − δ, δ) × ( − δ, δ), U=(-\delta,\delta)\times(-\delta,\delta),

4. 4.

and therefore, the map ( ε 2, μ ^) ↦ M ^ 2 ​ ( λ, τ 210, μ ^) (\varepsilon_{2},{{\hat{\mu}}})\mapsto\hat{M}_{2}(\lambda,\tau_{210};{{\hat{\mu}}}) belongs to 𝒞 K ​ ( ( − δ, δ) × V) \mathscr{C}^{K}\big((-\delta,\delta)\times V\big) by ( a) (a) in Theorem B.1 since λ ∉ ℤ ≥ 0 \lambda\notin\mathbb{Z}_{\geq 0} due to λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q} and shrinking V V if necessary.

5. 5.

τ 221 = ψ 2 ​ ( ε 2, 0) \tau_{221}=\psi_{2}(\varepsilon_{2},0) and τ 210 = ε 2 ​ ψ 1 ​ ( ε 2, 0) \tau_{210}=\varepsilon_{2}\psi_{1}(\varepsilon_{2},0) with ψ i ​ ( 0, 0) = 1. \psi_{i}(0,0)=1. Moreover, see ( 30) (\ref{Aeq17}\immediate), α 21 = ε 2 λ. \alpha_{21}=\varepsilon_{2}^{\lambda}.

The key point for our purposes will be that, for each fixed μ ^ {{\hat{\mu}}}, the function φ 1 \varphi_{1} is 𝒞 K \mathscr{C}^{K} in a neighbourhood of ε 2 = 0. \varepsilon_{2}=0. On account of this, for simplicity in the exposition we will say that α 22 = ε 2 λ ​ φ 1 ​ ( ε 2) \alpha_{22}=\varepsilon_{2}^{\lambda}\varphi_{1}(\varepsilon_{2}) with φ 1 ∈ 𝒞 K \varphi_{1}\in\mathscr{C}^{K}. In what follows we will deal several times with this type of situation and for shortness we will omit the previous details. More generally, for the same reason, when we write φ k ​ ( ε i) \varphi_{k}(\varepsilon_{i}) with i = 1, 2 i=1,2 and any subscript k k we shall mean that φ k \varphi_{k} is some function depending only on ε i \varepsilon_{i} and μ ^ {{\hat{\mu}}} that belongs to 𝒞 K ​ ( ( − δ, δ) × V) \mathscr{C}^{K}((-\delta,\delta)\times V\big).

We are now in position to compute the second order derivatives by means of Lemma A.3. In this case, for the sake of convenience in the exposition, we begin with the second regular passage. In doing so, and using Table 1 together with the expressions for R 21 R_{21} and ρ 22 \rho_{22} given in ( 28) (\ref{Aeq27}\hbox{}) and ( 33) (\ref{Aeq28}\immediate), respectively, we get

 | R 22 = ( σ 211 σ 210 ​ ( P 2 P 1) ​ ( σ 210, 0) − σ 222 2 ​ σ 221) ​ α 21 2 ​ σ 210 − 2 ​ λ σ 221 2 ​ L 2 2 ​ ( σ 210) \displaystyle R_{22}=\left(\frac{\sigma_{211}}{\sigma_{210}}\!\left(\frac{P_{2}}{P_{1}}\right)\!(\sigma_{210},0)-\frac{\sigma_{222}}{2\sigma_{221}}\right)\alpha_{21}^{2}\frac{\sigma_{210}^{-2{\lambda}}}{\sigma_{221}^{2}}L_{2}^{2}(\sigma_{210}) | + α 22 2 ​ σ 210 − λ σ 221 ​ L 2 ​ ( σ 210) \displaystyle+\frac{\alpha_{22}}{2}\frac{\sigma_{210}^{-{\lambda}}}{\sigma_{221}}L_{2}(\sigma_{210}) |  |

 |  | + α 21 2 ​ σ 210 − 2 ​ λ σ 221 ​ L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210). \displaystyle+\alpha_{21}^{2}\frac{\sigma_{210}^{-2{\lambda}}}{\sigma_{221}}L_{2}(\sigma_{210})\hat{M}_{2}(\lambda,\sigma_{210}). |  |

This implies that α 22 ​ ε 2 − 2 ​ λ \alpha_{22}\varepsilon_{2}^{-2\lambda} does not depend on ε \varepsilon because this is the case for σ 2 \sigma_{2} and R 22 ​ ε 2 − 2 ​ λ R_{22}\varepsilon_{2}^{-2\lambda}, see ( 19) (\ref{Aeq14}\hbox{}), and moreover α 21 = ε 2 λ \alpha_{21}=\varepsilon_{2}^{\lambda} from ( 30) (\ref{Aeq17}\hbox{}). Hence the previous claim shows that α 22 ​ ε 2 − 2 ​ λ = ε 2 − λ ​ φ 1 ​ ( ε 2) = c \alpha_{22}\varepsilon_{2}^{-2\lambda}=\varepsilon_{2}^{-\lambda}\varphi_{1}(\varepsilon_{2})=c where c c is a constant depending only on μ ^. {{\hat{\mu}}}. Therefore φ 1 ​ ( ε 2) = c ​ ε 2 λ \varphi_{1}(\varepsilon_{2})=c\varepsilon_{2}^{\lambda}. Since λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q}, we have that λ ∉ ℤ ≥ 0 \lambda\notin\mathbb{Z}_{\geq 0} for all μ ^ ∈ V {{\hat{\mu}}}\in V (shrinking V V if necessary) and, consequently, c = 0 c=0 because φ 1 \varphi_{1} is 𝒞 K \mathscr{C}^{K} in a neighbourhood of ε 2 = 0 \varepsilon_{2}=0 with K {K} arbitrarily large. (More precisely it suffices to take K > λ 0 {K}>\lambda_{0} and make smaller V V so that K > λ K>\lambda for all μ ^ ∈ V. {{\hat{\mu}}}\in V.) Accordingly

 | α 22 = 0 \alpha_{22}=0 |  | (34) |

and, since α 21 = ε 2 λ \alpha_{21}=\varepsilon_{2}^{\lambda} on account of ( 30) (\ref{Aeq17}\hbox{}),

 | R 22 = − ε 2 2 ​ λ ​ ( σ 222 2 ​ σ 221 − σ 211 σ 210 ​ ( P 2 P 1) ​ ( σ 210, 0) − σ 221 L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210) ⏟ S 2) ​ ( L 2 ​ ( σ 210 CLOSE σ 221 ​ σ 210 λ) 2. R_{22}=-\varepsilon_{2}^{2\lambda}\bigg(\underbrace{\frac{\sigma_{222}}{2\sigma_{221}}-\frac{\sigma_{211}}{\sigma_{210}}\!\left(\frac{P_{2}}{P_{1}}\right)\!(\sigma_{210},0)-\frac{\sigma_{221}}{L_{2}(\sigma_{210})}\hat{M}_{2}(\lambda,\sigma_{210})}_{S_{2}}\bigg)\left(\frac{L_{2}(\sigma_{210}}{\sigma_{221}\sigma_{210}^{\lambda}}\right)^{2}. |  | (35) |

Then, using ( 18) (\ref{Aeq15}\hbox{}) with k = 1 k=1 and the expression of R 11 R_{11} in ( 29) (\ref{Aeq16}\immediate),

 | Δ 01 = − S 2 ​ ( L 2 ​ ( σ 210 CLOSE σ 221 ​ σ 210 λ) 2 ​ ( σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120)) 2 = − S 2 ​ Δ 00 2 ​ for all μ ^ ∈ V. \Delta_{01}=-S_{2}\left(\frac{L_{2}(\sigma_{210}}{\sigma_{221}\sigma_{210}^{\lambda}}\right)^{2}\left(\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\right)^{2}=-S_{2}\Delta_{00}^{2}\text{ for all ${{\hat{\mu}}}\in V.$} |  |

By applying Lemma 2.3 and Theorem B.1, the function M ^ 2 ​ ( λ, σ 210) \hat{M}_{2}(\lambda,\sigma_{210}) in S 2 S_{2} is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of any ( λ ⋆, μ ⋆) ∈ ( 0, + ∞) × W (\lambda_{\star},\mu_{\star})\in(0,+\infty)\times W such that λ ⋆ ∉ ℤ ≥ 0. \lambda_{\star}\notin\mathbb{Z}_{\geq 0}. Thus the function on the right hand side of the above equality, that we denote by Δ ~ 01 \tilde{\Delta}_{01} in the second paragraph of the proof, is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D ~ 01 n) × W ((0,+\infty)\setminus\tilde{D}_{01}^{n})\times W with D ~ 01 n:= ℕ \tilde{D}_{01}^{n}\!:=\mathbb{N}. Since we know on the other hand by Theorem 1.6 that Δ 01 ∈ 𝒞 ∞ ​ ( ( ( 0, + ∞) ∖ D 01 n) × W) \Delta_{01}\in\mathscr{C}^{\infty}(((0,+\infty)\setminus D_{01}^{n})\times W) with D 01 n = ℕ D_{01}^{n}=\mathbb{N}, see Remark 1, this implies by continuity that the second equality in ( b) (\ref{b}\hbox{}) is true for ( λ, μ) ∈ ( ( 0, + ∞) ∖ D 01 0) × W. (\lambda,\mu)\in\big((0,+\infty)\setminus D_{01}^{0}\big)\times W. Certainly we also use here, and it is essential, that the parameter μ ^ 0 = ( λ 0, μ 0) ∈ W ^ {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in\hat{W} with λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q} that we fix at the very beginning is arbitrary.

Let us begin now with the computation of R 21 R_{21}, i.e., the second coefficient of the transition map for the first passage, by means of Lemma A.3. In this case, using Table 1 together with ( 29) (\ref{Aeq16}\hbox{}) and ( 31) (\ref{Aeq29}\immediate), we get

 | R 12 = ( τ 121 τ 120 ( P 1 P 2) ( 0, τ 120) − τ 112 2 ​ τ 111) α 11 2 τ 120 − 2 λ τ 111 2 ​ L 1 2 ​ ( τ 120) ⏟ ε 1 − 2 / λ + α 12 2 τ 120 − 1 λ τ 111 ​ L 1 ​ ( τ 120) ⏟ ε 1 − 1 / λ + α 11 2 τ 120 − 2 λ τ 111 ​ L 1 ​ ( τ 120) ​ M ^ 1 ​ ( 1 / λ, τ 120) ⏟ ε 1 − 2 / λ φ 2 ( ε 1). R_{12}=\left(\frac{\tau_{121}}{\tau_{120}}\!\left(\frac{P_{1}}{P_{2}}\right)\!(0,\tau_{120})-\frac{\tau_{112}}{2\tau_{111}}\right)\!\alpha_{11}^{2}\underbrace{\frac{\tau_{120}^{{\frac{-2}{\lambda}}}}{\tau_{111}^{2}}L_{1}^{2}(\tau_{120})}_{\varepsilon_{1}^{{-2/\lambda}}}+\frac{\alpha_{12}}{2}\underbrace{\frac{\tau_{120}^{{\frac{-1}{\lambda}}}}{\tau_{111}}L_{1}(\tau_{120})}_{\varepsilon_{1}^{{-1/\lambda}}}+\alpha_{11}^{2}\underbrace{\frac{\tau_{120}^{{\frac{-2}{\lambda}}}}{\tau_{111}}L_{1}(\tau_{120})\hat{M}_{1}(1/\lambda,\tau_{120})}_{\varepsilon_{1}^{{-2/\lambda}}\varphi_{2}(\varepsilon_{1})}. |  |

Since R 11 = ε 1 − 1 / λ α 11 R_{11}=\varepsilon_{1}^{-1/\lambda}\alpha_{11} from ( 29) (\ref{Aeq16}\hbox{}) once again and, on the other hand, τ 120 = ε 1 ​ ψ 2 ​ ( 0, ε 1) \tau_{120}=\varepsilon_{1}\psi_{2}(0,\varepsilon_{1}) with ψ 2 ​ ( 0, 0) = 1 \psi_{2}(0,0)=1, it follows that we can write

 | R 12 R 11 = φ 3 ( ε 1) ε 1 − 1 / λ − 1 + α 12 2 ​ α 11. \frac{R_{12}}{R_{11}}=\varphi_{3}(\varepsilon_{1})\varepsilon_{1}^{-1/\lambda-1}+\frac{\alpha_{12}}{2\alpha_{11}}. |  |

Observe that the quotient R 12 R 11 \frac{R_{12}}{R_{11}} does not depend on ε \varepsilon because, from ( 16) (\ref{Aeq18}\hbox{}) and ( 17) (\ref{Aeq6}\hbox{})

 | Δ 1 ​ k Δ 0 ​ k = Υ 1 [λ ⁡ ( k + 1)] = λ ⁡ ( k + 1) ​ R 12 R 11. \frac{\Delta_{1k}}{\Delta_{0k}}=\Upsilon_{1}^{[\lambda(k+1)]}=\lambda(k+1)\frac{R_{12}}{R_{11}}. |  |

Since this is also the case for the quotient α 12 α 11, \frac{\alpha_{12}}{\alpha_{11}}, see ( 27) (\ref{Aeq25}\immediate) and ( 32) (\ref{Aeq19}\immediate), it turns out that φ 3 ( ε 1) ε 1 − 1 / λ − 1 = c \varphi_{3}(\varepsilon_{1})\varepsilon_{1}^{-1/\lambda-1}=c for some constant depending only on μ ^ {{\hat{\mu}}}. Thus φ 3 ​ ( ε 1) = c ​ ε 1 1 / λ + 1 \varphi_{3}(\varepsilon_{1})=c\varepsilon_{1}^{1/\lambda+1} and, due to λ ≈ λ 0 ∉ ℚ, \lambda\approx\lambda_{0}\notin\mathbb{Q}, this implies c = 0 c=0. Therefore,

 | R 12 R 11 = α 12 2 ​ α 11 = σ 112 2 ​ σ 111 − σ 121 σ 120 ​ ( P 1 P 2) ​ ( 0, σ 120) − σ 111 L 1 ​ ( σ 120) ​ M ^ 1 ​ ( 1 / λ, σ 120) = S 1, \frac{R_{12}}{R_{11}}=\frac{\alpha_{12}}{2\alpha_{11}}=\frac{\sigma_{112}}{2\sigma_{111}}-\frac{\sigma_{121}}{\sigma_{120}}\!\left(\frac{P_{1}}{P_{2}}\right)\!(0,\sigma_{120})-\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{M}_{1}(1/\lambda,\sigma_{120})=S_{1}, |  | (36) |

where the second equality follows from ( 27) (\ref{Aeq25}\hbox{}) and ( 32) (\ref{Aeq19}\hbox{}) again and the last one from the definition in ( 3) (\ref{def_S}\immediate). Hence

 | Δ 10 = Δ 00 ​ λ ​ S 1 ​ and ​ Δ 11 = Δ 01 ​ 2 ​ λ ​ S 1 = − Δ 00 2 ​ 2 ​ λ ​ S 1 ​ S 2 ​ for all μ ^ ∈ V. \Delta_{10}=\Delta_{00}\lambda S_{1}\text{ and }\Delta_{11}=\Delta_{01}2\lambda S_{1}=-\Delta_{00}^{2}2\lambda S_{1}S_{2}\text{ for all ${{\hat{\mu}}}\in V.$} |  |

On account of the expression of S 2 S_{2} and S 1 S_{1} given in ( 35) (\ref{Aeq26}\immediate) and ( 36) (\ref{Aeq23}\immediate), respectively, the application of Theorem B.1 shows (following the notation introduced in the first paragraph of the proof) that D ~ 10 0 = 1 ℕ \tilde{D}_{10}^{0}=\frac{1}{\mathbb{N}} and D ~ 11 0 = ℕ ∪ 1 ℕ. \tilde{D}_{11}^{0}=\mathbb{N}\cup\frac{1}{\mathbb{N}}. Since these sets coincide with D 10 0 D_{10}^{0} and D 11 0, D_{11}^{0}, respectively, this concludes the proof of assertion ( b) (\ref{b}\hbox{}).

Let us show next the validity of the identities in assertion ( c) (\ref{c}\hbox{}), that deal with the coefficients of the Dulac time. As before we begin with the study of the regular passages and the computation of the first coefficients of their time functions. With regard to T 1 ​ ( s, ε 1, μ ^) T^{1}(s;\varepsilon_{1},{{\hat{\mu}}}) it turns out that

 | T n 1 1 = α 11 n 1 ​ ∫ σ 120 τ 120 L 1 n 1 ​ ( x) P 2 ​ ( 0, x) ⏟ A 1 ​ ( x) ​ x n 2 − n 1 λ ​ d ​ x x = α 11 n 1 ​ ( τ 120 n 2 − n 1 λ ​ A ^ 1 ​ ( n 1 / λ − n 2, τ 120) ⏟ ε 1 n 2 − n 1 λ ​ φ 4 ​ ( ε 1) − σ 120 n 2 − n 1 λ ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120)). T^{1}_{n_{1}}=\alpha_{11}^{n_{1}}\int_{\sigma_{120}}^{\tau_{120}}\underbrace{\frac{L_{1}^{n_{1}}(x)}{P_{2}(0,x)}}_{A_{1}(x)}x^{n_{2}-\frac{n_{1}}{\lambda}}\frac{dx}{x}=\alpha_{11}^{n_{1}}\bigg(\underbrace{\tau_{120}^{n_{2}-\frac{n_{1}}{\lambda}}\hat{A}_{1}(n_{1}/\lambda-n_{2},\tau_{120})}_{\varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\varphi_{4}(\varepsilon_{1})}-\sigma_{120}^{n_{2}-\frac{n_{1}}{\lambda}}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})\bigg). |  |

The first equality above follows by Lemma A.3 taking into account the expression of ρ 11 \rho_{11} in ( 27) (\ref{Aeq25}\hbox{}) and Table 1. The second equality follows by applying Theorem B.1 with A 1 ​ ( x, μ ^) A_{1}(x;{{\hat{\mu}}}), that belongs to 𝒞 ∞ ​ ( I 1 × W ^) \mathscr{C}^{\infty}(I_{1}\times\hat{W}) by Lemma 2.3, and the fact that τ 120 = ε 1 ​ ψ 2 ​ ( 0, ε 1) \tau_{120}=\varepsilon_{1}\psi_{2}(0,\varepsilon_{1}) with ψ 2 ​ ( 0, 0) = 1 \psi_{2}(0,0)=1. Then

 | T n 1 ​ 0 \displaystyle T_{n_{1}0} | = T n 1 ​ 0 − = T n 1 1 + T 1 0 ​ R 11 n 1 \displaystyle=T_{n_{1}0}^{-}=T^{1}_{n_{1}}+T_{1}^{0}R_{11}^{n_{1}} |  |

 |  | = α 11 n 1 ​ ( ε 1 n 2 − n 1 λ ​ ( φ 4 ​ ( ε 1) − 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0)) − σ 120 n 2 − n 1 λ ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120)) \displaystyle=\alpha_{11}^{n_{1}}\left(\varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\left(\varphi_{4}(\varepsilon_{1})-\frac{1}{(n_{1}-\lambda n_{2})P_{1}(0,0)}\right)-\sigma_{120}^{n_{2}-\frac{n_{1}}{\lambda}}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})\right) |  |

 |  | = − σ 111 n 1 ​ σ 120 n 2 L 1 n 1 ​ ( σ 120) ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120). \displaystyle=-\frac{\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}}}{L_{1}^{n_{1}}(\sigma_{120})}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120}). |  |

The first and second equalities above follow from ( 26) (\ref{Aeq22}\hbox{}) and ( 22) (\ref{Aeq10}\hbox{}), respectively, and the third one by using ( 14) (\ref{Aeq8}\hbox{}) together with ( 29) (\ref{Aeq16}\hbox{}). In the last equality we use that T n 1 ​ 0 T_{n_{1}0}, α 11 = σ 111 ​ σ 120 1 / λ L 1 ​ ( σ 120) \alpha_{11}=\frac{\sigma_{111}\sigma_{120}^{1/\lambda}}{L_{1}(\sigma_{120})} and σ 1 \sigma_{1} do not depend on ε \varepsilon and this, on account of λ ≈ λ 0 ∉ ℚ \lambda\approx\lambda_{0}\notin\mathbb{Q}, implies that φ 4 ​ ( ε 1) = 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0) \varphi_{4}(\varepsilon_{1})=\frac{1}{(n_{1}-\lambda n_{2})P_{1}(0,0)}. For the reader’s convenience let us be more precise in this last implication because we use the same argument repeatedly. The point is that there exists c c, not depending on ε 1 \varepsilon_{1}, such that

 | ε 1 n 2 − n 1 λ ​ ( φ 4 ​ ( ε 1) − 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0)) = c ​ for all ε 1 \varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\left(\varphi_{4}(\varepsilon_{1})-\frac{1}{(n_{1}-\lambda n_{2})P_{1}(0,0)}\right)=c\text{ for all $\varepsilon_{1}$} |  |

and we know on the other hand that φ 4 \varphi_{4} is 𝒞 K ​ ( (,,,)) \mathscr{C}^{K}((-\delta,\delta)) with K {K} arbitrarily large. In this case for our purpose we need K > n 1 λ 0 − n 2 {K}>\frac{n_{1}}{\lambda_{0}}-n_{2}, so that (by shrinking V V) we have K > n 1 λ − n 2 {K}>\frac{n_{1}}{\lambda}-n_{2} for all μ ^ ∈ V {{\hat{\mu}}}\in V. Since λ 0 ∉ ℚ \lambda_{0}\notin\mathbb{Q} we can also assume that n 1 λ − n 2 ∉ ℤ ≥ 0 \frac{n_{1}}{\lambda}-n_{2}\notin\mathbb{Z}_{\geq 0} for all μ ^ ∈ V. {{\hat{\mu}}}\in V. That being said, note then that from the above equality it turns out that φ 4 \varphi_{4} is a 𝒞 K \mathscr{C}^{K} function that is written as φ 4 ​ ( ε 1) = c ​ ε 1 n 1 λ − n 2 + c ^ \varphi_{4}(\varepsilon_{1})=c\varepsilon_{1}^{\frac{n_{1}}{\lambda}-n_{2}}+\hat{c} with the exponent n 1 λ − n 2 \frac{n_{1}}{\lambda}-n_{2} smaller than K {K} and not being in ℤ ≥ 0. \mathbb{Z}_{\geq 0}. It is evident that this is only possible if c = 0 c=0, as we claimed. Hence

 | T n 1 ​ 0 = σ 111 n 1 ​ σ 120 n 2 L 1 n 1 ​ ( σ 120) ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120) ​ for all μ ^ ∈ V. T_{n_{1}0}=\frac{\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}}}{L_{1}^{n_{1}}(\sigma_{120})}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})\text{ for all ${{\hat{\mu}}}\in V.$} |  |

By Theorem B.1, the function on the right hand side is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of any ( λ ⋆, μ ⋆) ∈ W ^ (\lambda_{\star},\mu_{\star})\in\hat{W} with n 1 λ ⋆ − n 2 ∉ ℤ ≥ 0, \frac{n_{1}}{\lambda_{\star}}-n_{2}\notin\mathbb{Z}_{\geq 0}, i.e., λ ⋆ ∉ D ~ n 1, 0 n:= n 1 ℕ ≥ n 2. \lambda_{\star}\notin\tilde{D}_{n_{1},0}^{n}\!:=\frac{n_{1}}{\mathbb{N}_{\geq n_{2}}}. Thus D ~ n 1, 0 n ⊂ D n 1, 0 n = ⋃ i = 1 n 1 i ℕ ≥ n 2, \tilde{D}_{n_{1},0}^{n}\subset D_{n_{1},0}^{n}=\bigcup_{i=1}^{n_{1}}\frac{i}{\mathbb{N}_{\geq n_{2}}}, see Remark 1, and therefore by continuity the above equality is valid provided that λ ∉ D n 1, 0 n. \lambda\notin D_{n_{1},0}^{n}. This proves the first identity in ( c) (\ref{c}\hbox{}).

Regarding the time function T 2 ​ ( s, ε 2, μ ^) T^{2}(s;\varepsilon_{2},{{\hat{\mu}}}) of the second regular passage one can check that

 | T n 2 2 \displaystyle T^{2}_{n_{2}} | = ε 2 n 2 ​ λ ​ ( σ 210 n 1 − n 2 ​ λ ​ A ^ 2 ​ ( n 2 ​ λ − n 1, σ 210) − τ 210 n 1 − λ ​ n 2 ​ A ^ 2 ​ ( n 2 ​ λ − n 1, τ 210) ⏟ ε 2 n 1 − n 2 ​ λ ​ φ 5 ​ ( ε 2)) \displaystyle=\varepsilon_{2}^{n_{2}\lambda}\bigg(\sigma_{210}^{n_{1}-n_{2}\lambda}\hat{A}_{2}(n_{2}\lambda-n_{1},\sigma_{210})-\underbrace{\tau_{210}^{n_{1}-\lambda n_{2}}\hat{A}_{2}(n_{2}\lambda-n_{1},\tau_{210})}_{\varepsilon_{2}^{n_{1}-n_{2}\lambda}\varphi_{5}(\varepsilon_{2})}\bigg) |  |

 |  | = ε 2 n 2 ​ λ ​ σ 210 n 1 − n 2 ​ λ ​ A ^ 2 ​ ( n 2 ​ λ − n 1, σ 210) + ε 2 n 1 ​ φ 5 ​ ( ε 2), \displaystyle=\varepsilon_{2}^{n_{2}\lambda}\sigma_{210}^{n_{1}-n_{2}\lambda}\hat{A}_{2}(n_{2}\lambda-n_{1},\sigma_{210})+\varepsilon_{2}^{n_{1}}\varphi_{5}(\varepsilon_{2}), |  |

where the first equality follows by Lemma A.3 and on account of ρ 21 ​ ( x) = ε 2 λ ​ x − λ ​ L 2 ​ ( x) \rho_{21}(x)=\varepsilon_{2}^{\lambda}x^{-\lambda}L_{2}(x), and the second equality by applying Theorem B.1 with A 2 ​ ( x, μ ^) A_{2}(x;{{\hat{\mu}}}), that belongs to 𝒞 ∞ ​ ( I 2 × W ^) \mathscr{C}^{\infty}(I_{2}\times\hat{W}) by Lemma 2.3. Hence, taking ( 14) (\ref{Aeq8}\hbox{}) and ( 23) (\ref{Aeq20}\immediate) into account,

 | T ¯ n 2 2 = T n 2 2 + T 2 0 = ε 2 n 2 ​ λ ​ σ 210 n 1 − n 2 ​ λ ​ A ^ 2 ​ ( n 2 ​ λ − n 1, σ 210) + ε 2 n 1 ​ ( φ 5 ​ ( ε 2) + 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0)) \bar{T}^{2}_{n_{2}}=T^{2}_{n_{2}}+T^{0}_{2}=\varepsilon_{2}^{n_{2}\lambda}\sigma_{210}^{n_{1}-n_{2}\lambda}\hat{A}_{2}(n_{2}\lambda-n_{1},\sigma_{210})+\varepsilon_{2}^{n_{1}}\left(\varphi_{5}(\varepsilon_{2})+\frac{1}{(n_{1}-\lambda n_{2})P_{1}(0,0)}\right) |  |

and, accordingly,

 | T 0, n 2 = T 0, n 2 + = ( T ¯ n 2 2 ​ ε 2 − n 2 ​ λ) ​ ( R 11 λ ​ ε 1) n 2 = σ 210 n 1 − n 2 ​ λ ​ A ^ 2 ​ ( n 2 ​ λ − n 1, σ 210) ​ ( σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120)) n 2, T_{0,n_{2}}=T^{+}_{0,n_{2}}=(\bar{T}^{2}_{n_{2}}\varepsilon_{2}^{-n_{2}\lambda})(R_{11}^{\lambda}\varepsilon_{1})^{n_{2}}=\sigma_{210}^{n_{1}-n_{2}\lambda}\hat{A}_{2}(n_{2}\lambda-n_{1},\sigma_{210})\left(\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\right)^{n_{2}}, |  |

where the first and second equalities follow from ( 26) (\ref{Aeq22}\hbox{}) and ( 25) (\ref{Aeq21}\hbox{}), respectively. Finally, in the last equality we use that σ 1 \sigma_{1} and σ 2 \sigma_{2} do not depend on ε \varepsilon and that this is also the case for T 0, n 2 T_{0,n_{2}} and, see ( 29) (\ref{Aeq16}\hbox{}), R 11 ​ ε 1 1 / λ = σ 111 ​ σ 120 1 / λ L 1 ​ ( σ 120) R_{11}\varepsilon_{1}^{1/\lambda}=\frac{\sigma_{111}\sigma_{120}^{1/\lambda}}{L_{1}(\sigma_{120})}. Since λ ≈ λ 0 ∉ ℚ \lambda\approx\lambda_{0}\notin\mathbb{Q}, this implies φ 5 ​ ( ε 2) = − 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0) \varphi_{5}(\varepsilon_{2})=\frac{-1}{(n_{1}-\lambda n_{2})P_{1}(0,0)} and finishes the proof of the second identity in ( c) (\ref{c}\hbox{}).

We proceed next with the computation of the coefficient T n 1 + 1 1 T_{n_{1}+1}^{1}. To this end we apply Lemma A.3 taking account of Table 1 and the expressions of ρ 11 \rho_{11}, R 11 R_{11} and ρ 12 \rho_{12} given in ( 27) (\ref{Aeq25}\hbox{}), ( 29) (\ref{Aeq16}\hbox{}) and ( 31) (\ref{Aeq29}\hbox{}), respectively. In doing so we obtain

 | T n 1 + 1 1 \displaystyle T^{1}_{n_{1}+1} | = ( ε 1 − 1 λ ​ α 11) n 1 + 1 ​ τ 121 ​ τ 111 n 1 ​ τ 120 n 2 − 1 P 2 ​ ( 0, τ 120) ⏟ ε 1 n 2 − n 1 + 1 λ ​ φ 6 ​ ( ε 1) − σ 121 ​ σ 111 n 1 ​ σ 120 n 2 − 1 P 2 ​ ( 0, σ 120) + α 11 n 1 + 1 ​ ∫ σ 120 τ 120 L 1 n 1 + 1 ​ ( x) ​ x n 2 − n 1 + 1 λ ​ ∂ 1 P 2 − 1 ​ ( 0, x) ​ d ​ x x \displaystyle=\underbrace{\left(\varepsilon_{1}^{\frac{-1}{\lambda}}\alpha_{11}\right)^{n_{1}+1}\frac{\tau_{121}\tau_{111}^{n_{1}}\tau_{120}^{n_{2}-1}}{P_{2}(0,\tau_{120})}}_{\varepsilon_{1}^{n_{2}-\frac{n_{1}+1}{\lambda}}\varphi_{6}(\varepsilon_{1})}-\frac{\sigma_{121}\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}-1}}{P_{2}(0,\sigma_{120})}+\alpha_{11}^{n_{1}+1}\int_{\sigma_{120}}^{\tau_{120}}L_{1}^{n_{1}+1}(x)x^{n_{2}-\frac{n_{1}+1}{\lambda}}\partial_{1}P_{2}^{-1}(0,x)\frac{dx}{x} |  |

 |  | + n 1 2 α 11 n 1 − 1 ∫ σ 120 τ 120 L 1 n 1 − 1 ( x) x − ( n 1 − 1) λ ( α 12 x − 1 λ L 1 ( x) + 2 α 11 2 x − 2 λ L 1 ( x) M ^ 1 ( 1 / λ, x)) x n 2 − 1 P 2 ​ ( 0, x) d x. \displaystyle\quad+\frac{n_{1}}{2}\alpha_{11}^{n_{1}-1}\int_{\sigma_{120}}^{\tau_{120}}L_{1}^{n_{1}-1}(x)x^{\frac{-(n_{1}-1)}{\lambda}}\left(\alpha_{12}x^{\frac{-1}{\lambda}}L_{1}(x)+2\alpha_{11}^{2}x^{\frac{-2}{\lambda}}L_{1}(x)\hat{M}_{1}(1/\lambda,x)\right)\frac{x^{n_{2}-1}}{P_{2}(0,x)}dx. |  |

Here we also use that τ 1 \tau_{1} does not depend on ε 2 \varepsilon_{2} and that τ 120 \tau_{120} and τ 121 \tau_{121} vanish at ε 1 = 0. \varepsilon_{1}=0. Then some easy manipulations first, on account of the definitions of A 1 A_{1} and B 1 B_{1} given in ( 2) (\ref{def_fun}\hbox{}), and next the application of Theorem B.1 yields to

 | T n 1 + 1 1 \displaystyle T_{n_{1}+1}^{1} | = ε 1 n 2 − n 1 + 1 λ ​ φ 6 ​ ( ε 1) − σ 121 ​ σ 111 n 1 ​ σ 120 n 2 − 1 P 2 ​ ( 0, σ 120) \displaystyle=\varepsilon_{1}^{n_{2}-\frac{n_{1}+1}{\lambda}}\varphi_{6}(\varepsilon_{1})-\frac{\sigma_{121}\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}-1}}{P_{2}(0,\sigma_{120})} |  |

 |  | + α 11 n 1 + 1 ∫ σ 120 τ 120 B 1 ( x) x n 2 − n 1 + 1 λ d ​ x x + n 1 ​ α 12 ​ α 11 n 1 − 1 2 ∫ σ 120 τ 120 A 1 ( x) x n 2 − n 1 λ d ​ x x \displaystyle\quad+\alpha_{11}^{n_{1}+1}\int_{\sigma_{120}}^{\tau_{120}}B_{1}(x)x^{n_{2}-\frac{n_{1}+1}{\lambda}}\frac{dx}{x}+\frac{n_{1}\alpha_{12}\alpha_{11}^{n_{1}-1}}{2}\int_{\sigma_{120}}^{\tau_{120}}A_{1}(x)x^{n_{2}-\frac{n_{1}}{\lambda}}\frac{dx}{x} |  |

 |  | = − σ 121 ​ σ 111 n 1 ​ σ 120 n 2 − 1 P 2 ​ ( 0, σ 120) + ε 1 n 2 − n 1 + 1 λ ​ φ 7 ​ ( ε 1) + ε 1 n 2 − n 1 λ ​ φ 8 ​ ( ε 1) \displaystyle=-\frac{\sigma_{121}\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}-1}}{P_{2}(0,\sigma_{120})}+\varepsilon_{1}^{n_{2}-\frac{n_{1}+1}{\lambda}}\varphi_{7}(\varepsilon_{1})+\varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\varphi_{8}(\varepsilon_{1}) |  |

 |  | − α 11 n 1 + 1 ​ σ 120 n 2 − n 1 + 1 λ ​ B ^ 1 ​ ( n 1 + 1 λ − n 2, σ 120) − n 1 ​ α 12 ​ α 11 n 1 − 1 2 ​ σ 120 n 2 − n 1 λ ​ A ^ 1 ​ ( n 1 λ − n 2, σ 120), \displaystyle\quad-\alpha_{11}^{n_{1}+1}\sigma_{120}^{n_{2}-\frac{n_{1}+1}{\lambda}}\hat{B}_{1}\!\left(\frac{n_{1}+1}{\lambda}-n_{2},\sigma_{120}\right)-\frac{n_{1}\alpha_{12}\alpha_{11}^{n_{1}-1}}{2}\sigma_{120}^{n_{2}-\frac{n_{1}}{\lambda}}\hat{A}_{1}\!\left(\frac{n_{1}}{\lambda}-n_{2},\sigma_{120}\right), |  |

where in the second equality we also use that α 11 \alpha_{11} and α 12 \alpha_{12} do not depend on ε, \varepsilon, see ( 27) (\ref{Aeq25}\hbox{}) and ( 32) (\ref{Aeq19}\hbox{}), respectively. Notice that

 | T n 1 + 1, 0 = T n 1 + 1, 0 − = T n 1 + 1 1 + T 1 0 ​ R 11 n 1 ​ Υ 1 [n 1] = T n 1 + 1 1 + n 1 ​ T 1 0 ​ R 11 n 1 ​ R 12 R 11 = T n 1 + 1 1 + n 1 ​ T 1 0 ​ R 11 n 1 ​ S 1, T_{n_{1}+1,0}=T_{n_{1}+1,0}^{-}=T^{1}_{n_{1}+1}+T_{1}^{0}R_{11}^{n_{1}}\Upsilon_{1}^{[n_{1}]}=T^{1}_{n_{1}+1}+n_{1}T_{1}^{0}R_{11}^{n_{1}}\frac{R_{12}}{R_{11}}=T^{1}_{n_{1}+1}+n_{1}T_{1}^{0}R_{11}^{n_{1}}S_{1}, |  |

where in the first equality we use ( 26) (\ref{Aeq22}\hbox{}), in the second one ( 22) (\ref{Aeq10}\hbox{}) with k = n 1 + 1 k=n_{1}+1, in the third one the fact that Υ 1 [n 1] = n 1 ​ R 12 R 11 \Upsilon_{1}^{[n_{1}]}=n_{1}\frac{R_{12}}{R_{11}} from ( 16) (\ref{Aeq18}\hbox{}), and in the last one that S 1 = R 12 R 11 = α 12 2 ​ α 11 S_{1}=\frac{R_{12}}{R_{11}}=\frac{\alpha_{12}}{2\alpha_{11}} from ( 36) (\ref{Aeq23}\hbox{}). On account of this and using also that, from ( 14) (\ref{Aeq8}\hbox{}) and ( 29) (\ref{Aeq16}\hbox{}), T 1 0 ​ R 11 n 1 = − ε 1 n 2 − n 1 λ ​ α 11 n 1 ( n 1 − λ ​ n 2) ​ P 1 ​ ( 0, 0) T_{1}^{0}R_{11}^{n_{1}}=-\varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\frac{\alpha_{11}^{n_{1}}}{(n_{1}-\lambda n_{2})P_{1}(0,0)} we get

 | T n 1 + 1, 0 = \displaystyle T_{n_{1}+1,0}= | − σ 121 ​ σ 111 n 1 ​ σ 120 n 2 − 1 P 2 ​ ( 0, σ 120) + ε 1 n 2 − n 1 + 1 λ ​ φ 7 ​ ( ε 1) + ε 1 n 2 − n 1 λ ​ φ 9 ​ ( ε 1) \displaystyle-\frac{\sigma_{121}\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}-1}}{P_{2}(0,\sigma_{120})}+\varepsilon_{1}^{n_{2}-\frac{n_{1}+1}{\lambda}}\varphi_{7}(\varepsilon_{1})+\varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\varphi_{9}(\varepsilon_{1}) |  |

 |  | − α 11 n 1 + 1 ​ σ 120 n 2 − n 1 + 1 λ ​ B ^ 1 ​ ( n 1 + 1 λ − n 2, σ 120) − n 1 ​ S 1 ​ α 11 n 1 ​ σ 120 n 2 − n 1 λ ​ A ^ 1 ​ ( n 1 λ − n 2, σ 120) \displaystyle-\alpha_{11}^{n_{1}+1}\sigma_{120}^{n_{2}-\frac{n_{1}+1}{\lambda}}\hat{B}_{1}\!\left(\frac{n_{1}+1}{\lambda}-n_{2},\sigma_{120}\right)-n_{1}S_{1}\alpha_{11}^{n_{1}}\sigma_{120}^{n_{2}-\frac{n_{1}}{\lambda}}\hat{A}_{1}\!\left(\frac{n_{1}}{\lambda}-n_{2},\sigma_{120}\right) |  |

 | = \displaystyle= | − σ 121 ​ σ 111 n 1 ​ σ 120 n 2 − 1 P 2 ​ ( 0, σ 120) − α 11 n 1 ​ σ 120 n 2 − n 1 λ ​ ( α 11 ​ σ 120 − 1 λ ​ B ^ 1 ​ ( n 1 + 1 λ − n 2, σ 120) + n 1 ​ S 1 ​ A ^ 1 ​ ( n 1 λ − n 2, σ 120)). \displaystyle-\frac{\sigma_{121}\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}-1}}{P_{2}(0,\sigma_{120})}-\alpha_{11}^{n_{1}}\sigma_{120}^{n_{2}-\frac{n_{1}}{\lambda}}\left(\alpha_{11}\sigma_{120}^{\frac{-1}{\lambda}}\hat{B}_{1}\!\left(\frac{n_{1}+1}{\lambda}-n_{2},\sigma_{120}\right)+n_{1}S_{1}\hat{A}_{1}\!\left(\frac{n_{1}}{\lambda}-n_{2},\sigma_{120}\right)\right). |  |

Here we also use that σ 1 \sigma_{1}, α 11 \alpha_{11}, T n 1 + 1, 0 T_{n_{1}+1,0} and S 1 S_{1} do not depend on ε \varepsilon and apply Lemma 2.7 to conclude that

 | ε 1 n 2 − n 1 + 1 λ ​ φ 7 ​ ( ε 1) + ε 1 n 2 − n 1 λ ​ φ 9 ​ ( ε 1) = 0. \varepsilon_{1}^{n_{2}-\frac{n_{1}+1}{\lambda}}\varphi_{7}(\varepsilon_{1})+\varepsilon_{1}^{n_{2}-\frac{n_{1}}{\lambda}}\varphi_{9}(\varepsilon_{1})=0. |  |

Then by using the expression of α 11 \alpha_{11} in ( 27) (\ref{Aeq25}\hbox{}) and an easy manipulation we get that

 |  | T n 1 + 1, 0 ​ ( μ ^) = − σ 111 n 1 ​ σ 120 n 2 ​ ( σ 121 σ 120 ​ P 2 ​ ( 0, σ 120) + n 1 ​ S 1 L 1 n 1 ​ ( σ 120) ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120) CLOSE \displaystyle T_{n_{1}+1,0}({{\hat{\mu}}})=-\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}}\left(\frac{\sigma_{121}}{\sigma_{120}P_{2}(0,\sigma_{120})}+\frac{n_{1}S_{1}}{L_{1}^{n_{1}}(\sigma_{120})}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})\right. |  |

 |  | OPEN + σ 111 L 1 n 1 + 1 ​ ( σ 120) ​ B ^ 1 ​ ( ( n 1 + 1) / λ − n 2, σ 120)) \displaystyle\hskip 163.60333pt+\left.\frac{\sigma_{111}}{L_{1}^{n_{1}+1}(\sigma_{120})}\hat{B}_{1}\big((n_{1}+1)/\lambda-n_{2},\sigma_{120}\big)\right) |  |

for all μ ^ ∈ V. {{\hat{\mu}}}\in V. The application of Lemma 2.3 and Theorem B.1 shows that the function on the right hand side is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of any ( λ ⋆, μ ⋆) ∈ W ^ (\lambda_{\star},\mu_{\star})\in\hat{W} such that { 1 λ ⋆, n 1 λ ⋆ − n 2, n 1 + 1 λ ⋆ − n 2 } ∩ ℤ ≥ 0 = ∅, \left\{\frac{1}{\lambda_{\star}},\frac{n_{1}}{\lambda_{\star}}-n_{2},\frac{n_{1}+1}{\lambda_{\star}}-n_{2}\right\}\!\cap\mathbb{Z}_{\geq 0}=\emptyset, i.e.,

 | λ ⋆ ∉ D ~ n 1 + 1, 0 n:= 1 ℕ ∪ n 1 ℕ ≥ n 2 ∪ n 1 + 1 ℕ ≥ n 2. \lambda_{\star}\notin\tilde{D}_{n_{1}+1,0}^{n}\!:=\frac{1}{\mathbb{N}}\cup\frac{n_{1}}{\mathbb{N}_{\geq n_{2}}}\cup\frac{n_{1}+1}{\mathbb{N}_{\geq n_{2}}}. |  |

Since D n 1 + 1, 0 n = ⋃ i = 1 n 1 + 1 i ℕ ≥ n 2 D_{n_{1}+1,0}^{n}=\bigcup_{i=1}^{n_{1}+1}\frac{i}{\mathbb{N}_{\geq n_{2}}}, see Remark 1, by continuity we can assert that the third identity in ( c) (\ref{c}\hbox{}) is true at any μ ^ = ( λ, μ) ∈ W ^ {{\hat{\mu}}}=(\lambda,\mu)\in\hat{W} with λ ∉ D n 1 + 1, 0 n ∪ D ~ n 1 + 1, 0 n = D n 1 + 1, 0 n ∪ { 1 k; k = 1, 2, …, ⌈ n 2 n 1 + 1 ⌉ − 1 }. \lambda\notin D_{n_{1}+1,0}^{n}\cup\tilde{D}_{n_{1}+1,0}^{n}=D_{n_{1}+1,0}^{n}\cup\left\{\frac{1}{k};\,k=1,2,\ldots,\lceil\frac{n_{2}}{n_{1}+1}\rceil-1\right\}.

We begin at this point the computation of the coefficient T n 2 + 1. T_{n_{2}+1}. To this aim we apply Lemma A.3 using in this case the second column in Table 1 and the expressions of R 21 R_{21}, ρ 21 \rho_{21} and ρ 22 \rho_{22}. We thus obtain

 | T n 2 + 1 2 = \displaystyle T_{n_{2}+1}^{2}= | α 21 n 2 + 1 ⏟ ε 2 λ ⁡ ( n 2 + 1) ​ σ 211 ​ σ 221 n 2 ​ ( L 2 ​ ( σ 210) σ 221 ​ σ 210 λ) n 2 + 1 ​ σ 210 n 1 − 1 P 1 ​ ( σ 210, 0) − τ 211 ​ τ 221 n 2 ​ τ 210 n 1 − 1 P 1 ​ ( τ 210, 0) ⏟ ε 2 n 1 ​ φ 10 ​ ( ε 2) \displaystyle\,\underbrace{\alpha_{21}^{n_{2}+1}}_{\varepsilon_{2}^{\lambda(n_{2}+1)}}\sigma_{211}\sigma_{221}^{n_{2}}\left(\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}\right)^{n_{2}+1}\frac{\sigma_{210}^{n_{1}-1}}{P_{1}(\sigma_{210},0)}-\underbrace{\frac{\tau_{211}\tau_{221}^{n_{2}}\tau_{210}^{n_{1}-1}}{P_{1}(\tau_{210},0)}}_{\varepsilon_{2}^{n_{1}}\varphi_{10}(\varepsilon_{2})} |  |

 |  | + 1 2 α 21 n 2 + 1 ⏟ ε 2 λ ⁡ ( n 2 + 1) ∫ τ 210 σ 210 x − λ ⁡ ( n 2 − 1) L 2 n 2 − 1 ( x) ( n 2 ( α 21 − 2 α 22 ⏟ 0 x − λ L 2 ( x) + 2 x − 2 ​ λ L 2 ( x) M 2 ^ ( λ, x)) x n 1 − 1 P 1 ​ ( x, 0) \displaystyle+\frac{1}{2}\underbrace{\alpha_{21}^{n_{2}+1}}_{\varepsilon_{2}^{\lambda(n_{2}+1)}}\int_{\tau_{210}}^{\sigma_{210}}x^{-\lambda(n_{2}-1)}L_{2}^{n_{2}-1}(x)\Bigg(n_{2}\bigg(\alpha_{21}^{-2}\underbrace{\alpha_{22}}_{0}x^{-\lambda}L_{2}(x)+2x^{-2\lambda}L_{2}(x)\hat{M_{2}}(\lambda,x)\bigg)\frac{x^{n_{1}-1}}{P_{1}(x,0)} |  |

 |  | + 2 x − 2 ​ λ L 2 2 ( x) x n 1 − 1 ∂ 2 P 1 − 1 ( x, 0)) d x, \displaystyle\hskip 170.71652pt+2x^{-2\lambda}L_{2}^{2}(x)x^{n_{1}-1}\partial_{2}P_{1}^{-1}(x,0)\Bigg)dx, |  |

where we use that α 21 = ε 2 λ \alpha_{21}=\varepsilon_{2}^{\lambda} from ( 30) (\ref{Aeq17}\hbox{}), α 22 = 0 \alpha_{22}=0 from ( 34) (\ref{Aeq24}\immediate) and the fact that τ 210 \tau_{210} and τ 211 \tau_{211} vanish at ε 2 = 0 \varepsilon_{2}=0. Notice on the other hand that, by using ( 23) (\ref{Aeq20}\hbox{}), ( 25) (\ref{Aeq21}\hbox{}) and ( 26) (\ref{Aeq22}\hbox{}),

 | T 0, n 2 + 1 = T 0, n 2 + 1 + = ( T n 2 + 1 2 ​ ε 2 − λ ⁡ ( n 2 + 1)) ​ ( ε 1 ​ R 11 λ) n 2 + 1, T_{0,n_{2}+1}=T_{0,n_{2}+1}^{+}=\left(T_{n_{2}+1}^{2}\varepsilon_{2}^{-\lambda(n_{2}+1)}\right)(\varepsilon_{1}R_{11}^{\lambda})^{n_{2}+1}, |  |

which in particular shows that T n 2 + 1 2 ​ ε 2 − λ ⁡ ( n 2 + 1) T_{n_{2}+1}^{2}\varepsilon_{2}^{-\lambda(n_{2}+1)} does not depend on ε. \varepsilon. Having said this, note that

 | T n 2 + 1 2 ​ ε 2 − λ ⁡ ( n 2 + 1) = \displaystyle T_{n_{2}+1}^{2}\varepsilon_{2}^{-\lambda(n_{2}+1)}= | σ 211 ​ σ 210 n 1 − 1 − λ ⁡ ( n 2 + 1) σ 221 ​ L 2 n 2 + 1 ​ ( σ 210) P 1 ​ ( σ 210, 0) + ε 2 n 1 − λ ⁡ ( n 2 + 1) ​ φ 10 ​ ( ε 2) \displaystyle\,\frac{\sigma_{211}\sigma_{210}^{n_{1}-1-\lambda(n_{2}+1)}}{\sigma_{221}}\frac{L_{2}^{n_{2}+1}(\sigma_{210})}{P_{1}(\sigma_{210},0)}+\varepsilon_{2}^{n_{1}-\lambda(n_{2}+1)}\varphi_{10}(\varepsilon_{2}) |  |

 |  | + ∫ τ 210 σ 210 ( n 2 ​ L 2 n 2 ​ ( x) P 1 ​ ( x, 0) ​ M ^ 2 ​ ( λ, x) + L 2 n 2 + 1 ​ ( x) ​ ∂ 2 P 1 − 1 ​ ( x, 0) ⏟ B 2 ​ ( x)) x n 1 − λ ⁡ ( n 2 + 1) d ​ x x \displaystyle+\int_{\tau_{210}}^{\sigma_{210}}\bigg(\underbrace{n_{2}\frac{L_{2}^{n_{2}}(x)}{P_{1}(x,0)}\hat{M}_{2}(\lambda,x)+L_{2}^{n_{2}+1}(x)\partial_{2}P_{1}^{-1}(x,0)}_{B_{2}(x)}\bigg)x^{n_{1}-\lambda(n_{2}+1)}\frac{dx}{x} |  |

 | = \displaystyle= | σ 211 ​ σ 210 n 1 − 1 − λ ⁡ ( n 2 + 1) σ 221 ​ L 2 n 2 + 1 ​ ( σ 210) P 1 ​ ( σ 210, 0) + ε 2 n 1 − λ ⁡ ( n 2 + 1) ​ φ 10 ​ ( ε 2) \displaystyle\,\frac{\sigma_{211}\sigma_{210}^{n_{1}-1-\lambda(n_{2}+1)}}{\sigma_{221}}\frac{L_{2}^{n_{2}+1}(\sigma_{210})}{P_{1}(\sigma_{210},0)}+\varepsilon_{2}^{n_{1}-\lambda(n_{2}+1)}\varphi_{10}(\varepsilon_{2}) |  |

 |  | + σ 210 n 1 − λ ⁡ ( n 2 + 1) ​ B ^ 2 ​ ( λ ⁡ ( n 2 + 1) − n 1, σ 210) − τ 210 n 1 − λ ⁡ ( n 2 + 1) ​ B ^ 2 ​ ( λ ⁡ ( n 2 + 1) − n 1, τ 210) ⏟ ε 2 n 1 − λ ⁡ ( n 2 + 1) ​ φ 11 ​ ( ε 2) \displaystyle+\sigma_{210}^{n_{1}-\lambda(n_{2}+1)}\hat{B}_{2}(\lambda(n_{2}+1)-n_{1},\sigma_{210})-\underbrace{\tau_{210}^{n_{1}-\lambda(n_{2}+1)}\hat{B}_{2}(\lambda(n_{2}+1)-n_{1},\tau_{210})}_{\varepsilon_{2}^{n_{1}-\lambda(n_{2}+1)}\varphi_{11}(\varepsilon_{2})} |  |

 | = \displaystyle= | σ 211 ​ σ 210 n 1 − 1 − λ ⁡ ( n 2 + 1) σ 221 ​ L 2 n 2 + 1 ​ ( σ 210) P 1 ​ ( σ 210, 0) + σ 210 n 1 − λ ⁡ ( n 2 + 1) ​ B ^ 2 ​ ( λ ⁡ ( n 2 + 1) − n 1, σ 210), \displaystyle\,\frac{\sigma_{211}\sigma_{210}^{n_{1}-1-\lambda(n_{2}+1)}}{\sigma_{221}}\frac{L_{2}^{n_{2}+1}(\sigma_{210})}{P_{1}(\sigma_{210},0)}+\sigma_{210}^{n_{1}-\lambda(n_{2}+1)}\hat{B}_{2}(\lambda(n_{2}+1)-n_{1},\sigma_{210}), |  |

where in the second equality we apply Theorem B.1 and in the third one we take advantage of the fact that T n 2 + 1 2 ​ ε 2 − λ ⁡ ( n 2 + 1) T_{n_{2}+1}^{2}\varepsilon_{2}^{-\lambda(n_{2}+1)} and σ 2 \sigma_{2} do not depend on ε \varepsilon to conclude, thanks to λ ≈ λ 0 ∉ ℚ, \lambda\approx\lambda_{0}\notin\mathbb{Q}, that φ 10 = φ 11. \varphi_{10}=\varphi_{11}. Hence, due to ε 1 ​ R 11 λ = σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120) \varepsilon_{1}R_{11}^{\lambda}=\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})} by the second equality in ( 29) (\ref{Aeq16}\hbox{}), we get that

 | T 0, n 2 + 1 = \displaystyle T_{0,n_{2}+1}= | ( T n 2 + 1 2 ​ ε 2 − λ ⁡ ( n 2 + 1)) ​ ( ε 1 ​ R 11 λ) n 2 + 1 \displaystyle\left(T_{n_{2}+1}^{2}\varepsilon_{2}^{-\lambda(n_{2}+1)}\right)(\varepsilon_{1}R_{11}^{\lambda})^{n_{2}+1} |  |

 | = \displaystyle= | ( σ 111 λ ​ σ 120 L 1 λ ​ ( σ 120)) n 2 + 1 ​ ( σ 211 ​ σ 210 n 1 − 1 − λ ⁡ ( n 2 + 1) σ 221 ​ L 2 n 2 + 1 ​ ( σ 210) P 1 ​ ( σ 210, 0) + σ 210 n 1 − λ ⁡ ( n 2 + 1) ​ B ^ 2 ​ ( λ ⁡ ( n 2 + 1) − n 1, σ 210)). \displaystyle\left(\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{120})}\right)^{n_{2}+1}\left(\frac{\sigma_{211}\sigma_{210}^{n_{1}-1-\lambda(n_{2}+1)}}{\sigma_{221}}\frac{L_{2}^{n_{2}+1}(\sigma_{210})}{P_{1}(\sigma_{210},0)}+\sigma_{210}^{n_{1}-\lambda(n_{2}+1)}\hat{B}_{2}(\lambda(n_{2}+1)-n_{1},\sigma_{210})\right). |  |

From here, taking the expression of Δ 00 \Delta_{00} into account, we can assert that

 | T 0, n 2 + 1 ​ ( μ ^) = Δ 00 n 2 + 1 ​ σ 210 n 1 ​ σ 221 n 2 ​ ( σ 211 σ 210 ​ P 1 ​ ( σ 210, 0) + σ 221 L 2 n 2 + 1 ​ ( σ 210) ​ B ^ 2 ​ ( λ ⁡ ( n 2 + 1) − n 1, σ 210)) T_{0,n_{2}+1}({{\hat{\mu}}})=\Delta_{00}^{n_{2}+1}\sigma_{210}^{n_{1}}\sigma_{221}^{n_{2}}\left(\frac{\sigma_{211}}{\sigma_{210}P_{1}(\sigma_{210},0)}+\frac{\sigma_{221}}{L_{2}^{n_{2}+1}(\sigma_{210})}\hat{B}_{2}\big(\lambda(n_{2}+1)-n_{1},\sigma_{210}\big)\right) |  |

for all μ ^ ∈ V. {{\hat{\mu}}}\in V. Exactly as in the previous cases, by applying Lemma 2.3 and Theorem B.1 it turns out that the function on the right hand side is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D ~ 0, n 2 + 1 n) × W \big((0,+\infty)\setminus\tilde{D}_{0,n_{2}+1}^{n}\big)\times W with D ~ 0, n 2 + 1 n:= ℕ ≥ n 1 n 2 + 1 \tilde{D}_{0,n_{2}+1}^{n}\!:=\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}+1}. Furthermore, by Theorem 1.6 we know that the function on the left hand side is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D 0, n 2 + 1 n) × W \big((0,+\infty)\setminus D_{0,n_{2}+1}^{n}\big)\times W where, see Remark 1, D 0, n 2 + 1 n = ℕ ≥ n 1 n 2 + 1 ∪ ℕ. D_{0,n_{2}+1}^{n}=\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}+1}\cup\mathbb{N}. Accordingly, due to D ~ 0, n 2 + 1 n ⊂ D 0, n 2 + 1 n, \tilde{D}_{0,n_{2}+1}^{n}\subset D_{0,n_{2}+1}^{n}, by continuity we can conclude that the fourth equality in ( c) (\ref{c}\hbox{}) is true on the given domain.

It only remains to compute T 20 T_{20} and T 02 T_{02} in the case that n 1 = 0 n_{1}=0 and n 2 = 0 n_{2}=0, respectively. Let us consider first the case n 1 = 0. n_{1}=0. To this end we begin by computing the coefficient of s 2 s^{2} in the time function T 1 T^{1} of the first regular passage. By applying ( b) (b) in Lemma A.3 for the case ℓ = 0 \ell=0 and taking f ⁡ ( x 1, x 2) = x 1 n 2 − 1 P 2 ​ ( x 2, x 1) f(x_{1},x_{2})=\frac{x_{1}^{n_{2}-1}}{P_{2}(x_{2},x_{1})}, see Table 1, we know that it is written as T 2 1 = 1 2 ​ ( U 1 − V 1 + W 1) T_{2}^{1}=\frac{1}{2}(U_{1}-V_{1}+W_{1}) with

 | U 1 \displaystyle U_{1} | = ( τ 122 ​ R 11 2 + τ 121 ​ R 12) ​ f ​ ( τ 120, 0) + τ 121 2 ​ R 11 2 ​ ∂ 1 f ⁡ ( τ 120, 0) + 2 ​ τ 121 ​ τ 111 ​ R 11 2 ​ ∂ 2 f ⁡ ( τ 120, 0) \displaystyle=(\tau_{122}R_{11}^{2}+\tau_{121}R_{12})f(\tau_{120},0)+\tau_{121}^{2}R_{11}^{2}\partial_{1}f(\tau_{120},0)+2\tau_{121}\tau_{111}R_{11}^{2}\partial_{2}f(\tau_{120},0) |  |

 |  | = ε 1 n 2 − 1 / λ ​ φ 12 ​ ( ε 1) + ε 1 n 2 − 2 / λ ​ φ 13 ​ ( ε 1), \displaystyle=\varepsilon_{1}^{n_{2}-1/\lambda}\varphi_{12}(\varepsilon_{1})+\varepsilon_{1}^{n_{2}-2/\lambda}\varphi_{13}(\varepsilon_{1}), |  |

 | V 1 \displaystyle V_{1} | = σ 122 ​ f ​ ( σ 120, 0) + σ 121 2 ​ ∂ 1 f ⁡ ( σ 120, 0) + 2 ​ σ 121 ​ σ 111 ​ ∂ 2 f ⁡ ( σ 120, 0) \displaystyle=\sigma_{122}f(\sigma_{120},0)+\sigma_{121}^{2}\partial_{1}f(\sigma_{120},0)+2\sigma_{121}\sigma_{111}\partial_{2}f(\sigma_{120},0) |  |

 |  | = σ 122 ​ σ 120 n 2 − 1 2 ​ P 2 ​ ( 0, σ 120) + σ 121 2 ​ σ 120 n 2 − 2 2 ​ ( n 2 − 1 P 2 ​ ( 0, σ 120) + σ 120 ​ ∂ 2 P 2 − 1 ​ ( 0, σ 120)) + σ 121 ​ σ 111 ​ σ 120 n 2 − 1 ​ ∂ 1 P 2 − 1 ​ ( 0, σ 120) \displaystyle=\frac{\sigma_{122}\sigma_{120}^{n_{2}-1}}{2P_{2}(0,\sigma_{120})}+\frac{\sigma_{121}^{2}\sigma_{120}^{n_{2}-2}}{2}\left(\frac{n_{2}-1}{P_{2}(0,\sigma_{120})}+\sigma_{120}\partial_{2}P_{2}^{-1}(0,\sigma_{120})\right)+\sigma_{121}\sigma_{111}\sigma_{120}^{n_{2}-1}\partial_{1}P_{2}^{-1}(0,\sigma_{120}) |  |

and |

 | W 1 \displaystyle W_{1} | = ∫ σ 120 τ 120 ( ( α 11 ​ x − 1 λ ​ L 1 ​ ( x)) 2 ​ ∂ 2 2 f ⁡ ( x, 0) + ( α 12 ​ x − 1 λ ​ L 1 ​ ( x) + 2 ​ α 11 2 ​ x − 2 λ ​ L 1 ​ ( x) ​ M ^ 1 ​ ( 1 / λ, x)) ​ ∂ 2 f ⁡ ( x, 0)) ​ 𝑑 x \displaystyle=\int_{\sigma_{120}}^{\tau_{120}}\left((\alpha_{11}x^{\frac{-1}{\lambda}}L_{1}(x))^{2}\partial_{2}^{2}f(x,0)+\big(\alpha_{12}x^{\frac{-1}{\lambda}}L_{1}(x)+2\alpha_{11}^{2}x^{\frac{-2}{\lambda}}L_{1}(x)\hat{M}_{1}(1/\lambda,x)\big)\partial_{2}f(x,0)\right)dx |  |

 |  | = α 11 2 ​ ∫ σ 120 τ 120 C 1 ​ ( x) ​ x n 2 − 2 λ ​ d ​ x x + α 12 ​ ∫ σ 120 τ 120 B 1 ​ ( x) ​ x n 2 − 1 λ ​ d ​ x x \displaystyle=\alpha_{11}^{2}\int_{\sigma_{120}}^{\tau_{120}}C_{1}(x)x^{n_{2}-\frac{2}{\lambda}}\frac{dx}{x}+\alpha_{12}\int_{\sigma_{120}}^{\tau_{120}}B_{1}(x)x^{n_{2}-\frac{1}{\lambda}}\frac{dx}{x} |  |

 |  | = α 11 2 ​ ( τ 120 n 2 − 2 λ ​ C ^ 1 ​ ( 2 / λ − n 2, τ 120) ⏟ ε 1 n 2 − 2 / λ ​ φ 14 ​ ( ε 1) − σ 120 n 2 − 2 λ ​ C ^ 1 ​ ( 2 / λ − n 2, σ 120)) \displaystyle=\alpha_{11}^{2}\bigg(\underbrace{\tau_{120}^{n_{2}-\frac{2}{\lambda}}\hat{C}_{1}(2/\lambda-n_{2},\tau_{120})}_{\varepsilon_{1}^{n_{2}-2/\lambda}\varphi_{14}(\varepsilon_{1})}-\sigma_{120}^{n_{2}-\frac{2}{\lambda}}\hat{C}_{1}(2/\lambda-n_{2},\sigma_{120})\bigg) |  |

 |  | + α 12 ​ ( τ 120 n 2 − 1 λ ​ B ^ 1 ​ ( 1 / λ − n 2, τ 120) ⏟ ε 1 n 2 − 1 / λ ​ φ 15 ​ ( ε 1) − σ 120 n 2 − 1 λ ​ B ^ 1 ​ ( 1 / λ − n 2, σ 120)). \displaystyle\hskip 142.26378pt+\alpha_{12}\bigg(\underbrace{\tau_{120}^{n_{2}-\frac{1}{\lambda}}\hat{B}_{1}(1/\lambda-n_{2},\tau_{120})}_{\varepsilon_{1}^{n_{2}-1/\lambda}\varphi_{15}(\varepsilon_{1})}-\sigma_{120}^{n_{2}-\frac{1}{\lambda}}\hat{B}_{1}(1/\lambda-n_{2},\sigma_{120})\bigg). |  |

Let us note that to rearrange U 1 U_{1} we use that R 11 = α 11 ε 1 − 1 / λ R_{11}=\alpha_{11}\varepsilon_{1}^{-1/\lambda} and R 12 = 1 2 α 12 ε 1 − 1 / λ R_{12}=\frac{1}{2}\alpha_{12}\varepsilon_{1}^{-1/\lambda} from ( 29) (\ref{Aeq16}\hbox{}) and ( 36) (\ref{Aeq23}\hbox{}), respectively, and moreover that τ 122, \tau_{122}, τ 120 \tau_{120} and τ 121 \tau_{121} vanish at ε 1 = 0. \varepsilon_{1}=0. On the other hand, to simplify W 1 W_{1} we apply Theorem B.1 and use that, in this case, B 1 ​ ( x) = L 1 ​ ( x) ​ ∂ 1 P 2 − 1 ​ ( 0, x) B_{1}(x)=L_{1}(x)\partial_{1}P_{2}^{-1}(0,x) due to n 1 = 0. n_{1}=0. By the same reason, using also ( 22) (\ref{Aeq10}\hbox{}) and ( 26) (\ref{Aeq22}\hbox{}), we get that

 | T 20 = T 20 − = T 2 1 + T 1 0 ​ Υ 2 [0] = T 2 1 = 1 2 ​ ( U 1 − V 1 + W 1) T_{20}=T_{20}^{-}=T^{1}_{2}+T^{0}_{1}\Upsilon^{[0]}_{2}=T^{1}_{2}=\frac{1}{2}(U_{1}-V_{1}+W_{1}) |  |

since Υ 2 [0] = 0. \Upsilon^{[0]}_{2}=0. This shows in particular that U 1 − V 1 + W 1 U_{1}-V_{1}+W_{1} does not depend on ε \varepsilon and, since this is also the case for α 11 \alpha_{11} and α 12, \alpha_{12}, we can assert that

 | ε 1 n 2 − 1 / λ ​ ( φ 12 ​ ( ε 1) + α 12 ​ φ 15 ​ ( ε 1)) + ε 1 n 2 − 2 / λ ​ ( φ 13 ​ ( ε 1) + α 11 2 ​ φ 14 ​ ( ε 1)) = 0 \varepsilon_{1}^{n_{2}-1/\lambda}(\varphi_{12}(\varepsilon_{1})+\alpha_{12}\varphi_{15}(\varepsilon_{1}))+\varepsilon_{1}^{n_{2}-2/\lambda}(\varphi_{13}(\varepsilon_{1})+\alpha_{11}^{2}\varphi_{14}(\varepsilon_{1}))=0 |  |

by applying Lemma 2.7 and using that λ ≈ λ 0 ∉ ℚ. \lambda\approx\lambda_{0}\notin\mathbb{Q}. Finally, since α 11 = σ 111 ​ σ 120 1 / λ L 1 ​ ( σ 120) \alpha_{11}=\frac{\sigma_{111}\sigma_{120}^{1/\lambda}}{L_{1}(\sigma_{120})} and α 12 = 2 ​ α 11 ​ S 1 \alpha_{12}=2\alpha_{11}S_{1} by ( 27) (\ref{Aeq25}\hbox{}) and ( 36) (\ref{Aeq23}\hbox{}), respectively, we obtain that

 | T 20 ​ ( μ ^) = \displaystyle T_{20}({{\hat{\mu}}})= | − σ 122 ​ σ 120 n 2 − 1 2 ​ P 2 ​ ( 0, σ 120) − σ 121 2 ​ σ 120 n 2 − 2 2 ​ ( n 2 − 1 P 2 ​ ( 0, σ 120) + σ 120 ​ ∂ 2 P 2 − 1 ​ ( 0, σ 120)) − σ 121 ​ σ 111 ​ σ 120 n 2 − 1 ​ ∂ 1 P 2 − 1 ​ ( 0, σ 120) \displaystyle-\frac{\sigma_{122}\sigma_{120}^{n_{2}-1}}{2P_{2}(0,\sigma_{120})}-\frac{\sigma_{121}^{2}\sigma_{120}^{n_{2}-2}}{2}\left(\frac{n_{2}-1}{P_{2}(0,\sigma_{120})}+\sigma_{120}\partial_{2}P_{2}^{-1}(0,\sigma_{120})\right)-\sigma_{121}\sigma_{111}\sigma_{120}^{n_{2}-1}\partial_{1}P_{2}^{-1}(0,\sigma_{120}) |  |

 |  | − σ 111 2 ​ σ 120 n 2 2 ​ L 1 2 ​ ( σ 120) ​ C ^ 1 ​ ( 2 / λ − n 2, σ 120) − S 1 ​ σ 111 ​ σ 120 n 2 L 1 ​ ( σ 120) ​ B ^ 1 ​ ( 1 / λ − n 2, σ 120) \displaystyle-\frac{\sigma_{111}^{2}\sigma_{120}^{n_{2}}}{2L_{1}^{2}(\sigma_{120})}\hat{C}_{1}(2/\lambda-n_{2},\sigma_{120})-S_{1}\frac{\sigma_{111}\sigma_{120}^{n_{2}}}{L_{1}(\sigma_{120})}\hat{B}_{1}(1/\lambda-n_{2},\sigma_{120}) |  |

for all μ ^ ∈ V. {{\hat{\mu}}}\in V. By applying Lemma 2.3 and Theorem B.1 we have that C ^ 1 ​ ( 2 / λ − n 2, σ 120) \hat{C}_{1}(2/\lambda-n_{2},\sigma_{120}) is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of any ( λ ⋆, μ ⋆) ∈ W ^ (\lambda_{\star},\mu_{\star})\in\hat{W} such that { 1 / λ ⋆, 2 / λ ⋆ − n 2 } ∩ ℤ ≥ 0 = ∅. \left\{1/{\lambda_{\star}},2/{\lambda_{\star}}-n_{2}\right\}\cap\mathbb{Z}_{\geq 0}=\emptyset. The condition for the function S 1 S_{1}, see ( 3) (\ref{def_S}\hbox{}), and B ^ 1 ​ ( 1 / λ − n 2, σ 120) \hat{B}_{1}(1/\lambda-n_{2},\sigma_{120}) is 1 / λ ⋆ ∉ ℤ ≥ 0 1/\lambda_{\star}\notin\mathbb{Z}_{\geq 0} and 1 / λ ⋆ − n 2 ∉ ℤ ≥ 0 1/\lambda_{\star}-n_{2}\notin\mathbb{Z}_{\geq 0}, respectively. Therefore the function on the right hand side in the above equality is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D ~ 20 n) × W \big((0,+\infty)\setminus\tilde{D}_{20}^{n}\big)\times W with D ~ 20 n:= 1 ℕ ∪ 2 ℕ ≥ n 2 \tilde{D}_{20}^{n}\!:=\frac{1}{\mathbb{N}}\cup\frac{2}{\mathbb{N}_{\geq n_{2}}}. Due to D 20 n = 2 ℕ ≥ n 2 D_{20}^{n}=\frac{2}{\mathbb{N}_{\geq n_{2}}} from Remark 1, we get that D 20 n ∪ D ~ 20 n = D 20 n ∪ { 1 k; k = 1, 2, …, ⌈ n 2 2 ⌉ − 1 } D_{20}^{n}\cup\tilde{D}_{20}^{n}=D_{20}^{n}\cup\left\{\frac{1}{k};\,k=1,2,\ldots,\lceil\frac{n_{2}}{2}\rceil-1\right\} and, on account of the considerations in the second paragraph of the proof, this shows that the above equality is true in the domain given in the statement.

Let us turn finally to the computation of T 02 T_{02} for the case n 2 = 0. n_{2}=0. Similarly as before we apply ( b) (b) in Lemma A.3 with f ⁡ ( x 1, x 2) = x 1 n 1 − 1 P 1 ​ ( x 1, x 2) f(x_{1},x_{2})=\frac{x_{1}^{n_{1}-1}}{P_{1}(x_{1},x_{2})} to get that T 2 2 = 1 2 ​ ( U 2 − V 2 + W 2) T^{2}_{2}=\frac{1}{2}(U_{2}-V_{2}+W_{2}). In this case some long but easy computations taking account of Table 1 give

 | U 2 \displaystyle U_{2} | = ( σ 212 ​ R 21 2 + σ 211 ​ R 22) ​ f ​ ( σ 210, 0) + σ 211 2 ​ R 21 2 ​ ∂ 1 f ⁡ ( σ 210, 0) + 2 ​ σ 211 ​ σ 221 ​ R 21 2 ​ ∂ 2 f ⁡ ( σ 210, 0) \displaystyle=(\sigma_{212}R_{21}^{2}+\sigma_{211}R_{22})f(\sigma_{210},0)+\sigma_{211}^{2}R_{21}^{2}\partial_{1}f(\sigma_{210},0)+2\sigma_{211}\sigma_{221}R_{21}^{2}\partial_{2}f(\sigma_{210},0) |  |

 |  | = ε 2 2 ​ λ ​ σ 210 n 1 ​ ( L 2 ​ ( σ 210) σ 221 ​ σ 210 λ) 2 ​ ( 2 ​ Z − σ 211 ​ S 2 σ 210 ​ P 1 ​ ( σ 210, 0)), \displaystyle=\varepsilon_{2}^{2\lambda}\sigma_{210}^{n_{1}}\left(\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}\right)^{2}\left(2Z-\frac{\sigma_{211}S_{2}}{\sigma_{210}P_{1}(\sigma_{210},0)}\right), |  |

where we use that R 21 = ε 2 λ ​ L 2 ​ ( σ 210) σ 221 ​ σ 210 λ R_{21}=\varepsilon_{2}^{\lambda}\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}} from ( 28) (\ref{Aeq27}\hbox{}) and ( 30) (\ref{Aeq17}\hbox{}) and that R 22 = − ε 2 2 ​ λ ​ S 2 ​ ( L 2 ​ ( σ 210) σ 221 ​ σ 210 λ) 2 R_{22}=-\varepsilon_{2}^{2\lambda}S_{2}\left(\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}\right)^{2} from ( 35) (\ref{Aeq26}\hbox{}) and, for the sake of shortness, we denote

 | Z:= σ 212 ​ σ 210 + ( n 1 − 1) ​ σ 211 2 2 ​ σ 210 2 ​ P 1 ​ ( σ 210, 0) + σ 211 2 2 ​ σ 210 ​ ∂ 1 P 1 − 1 ​ ( σ 210, 0) + σ 211 ​ σ 221 σ 210 ​ ∂ 2 P 1 − 1 ​ ( σ 210, 0). Z\!:=\frac{\sigma_{212}\sigma_{210}+(n_{1}-1)\sigma_{211}^{2}}{2\sigma_{210}^{2}P_{1}(\sigma_{210},0)}+\frac{\sigma_{211}^{2}}{2\sigma_{210}}\partial_{1}P_{1}^{-1}(\sigma_{210},0)+\frac{\sigma_{211}\sigma_{221}}{\sigma_{210}}\partial_{2}P_{1}^{-1}(\sigma_{210},0). |  |

Since τ 210 \tau_{210}, τ 211 \tau_{211} and τ 212 \tau_{212} vanish at ε 2 = 0 \varepsilon_{2}=0, one can also verify that

 | V 2 = τ 212 ​ f 2 ​ ( τ 210, 0) + τ 211 2 ​ ∂ 1 f 2 ​ ( τ 210, 0) + 2 ​ τ 211 ​ τ 221 ​ ∂ 2 f 2 ​ ( τ 210, 0) = ε 2 n 1 ​ φ 16 ​ ( ε 2). V_{2}=\tau_{212}f_{2}(\tau_{210},0)+\tau_{211}^{2}\partial_{1}f_{2}(\tau_{210},0)+2\tau_{211}\tau_{221}\partial_{2}f_{2}(\tau_{210},0)=\varepsilon_{2}^{n_{1}}\varphi_{16}(\varepsilon_{2}). |  |

Furthermore, on account of the definition of the function C 2 C_{2} given in ( 2) (\ref{def_fun}\hbox{}) and applying Theorem B.1,

 | W 2 \displaystyle W_{2} | = ∫ τ 210 σ 210 ( ( ε 2 λ ​ x − λ ​ L 2 ​ ( x)) 2 ​ x n 1 ​ ∂ 2 2 P 1 − 1 ​ ( x, 0) + 2 ​ ε 2 2 ​ λ ​ x n 1 − 2 ​ λ ​ L 2 ​ ( x) ​ M ^ 2 ​ ( λ, x) ​ ∂ 2 P 1 − 1 ​ ( x, 0)) ​ d ​ x x \displaystyle=\int_{\tau_{210}}^{\sigma_{210}}\left((\varepsilon_{2}^{\lambda}x^{-\lambda}L_{2}(x))^{2}x^{n_{1}}\partial_{2}^{2}P_{1}^{-1}(x,0)+2\varepsilon_{2}^{2\lambda}x^{n_{1}-2\lambda}L_{2}(x)\hat{M}_{2}(\lambda,x)\partial_{2}P_{1}^{-1}(x,0)\right)\frac{dx}{x} |  |

 |  | = ε 2 2 ​ λ ​ ∫ τ 210 σ 210 C 2 ​ ( x) ​ x n 1 − 2 ​ λ ​ d ​ x x = ε 2 2 ​ λ ​ ( σ 210 n 1 − 2 ​ λ ​ C ^ 2 ​ ( 2 ​ λ − n 1, σ 210) − τ 210 n 1 − 2 ​ λ ​ C ^ 2 ​ ( 2 ​ λ − n 1, τ 210) ⏟ ε 2 n 1 − 2 ​ λ ​ φ 17 ​ ( ε 2)). \displaystyle=\varepsilon_{2}^{2\lambda}\int_{\tau_{210}}^{\sigma_{210}}C_{2}(x)x^{n_{1}-2\lambda}\frac{dx}{x}=\varepsilon_{2}^{2\lambda}\bigg(\sigma_{210}^{n_{1}-2\lambda}\hat{C}_{2}(2\lambda-n_{1},\sigma_{210})-\underbrace{\tau_{210}^{n_{1}-2\lambda}\hat{C}_{2}(2\lambda-n_{1},\tau_{210})}_{\varepsilon_{2}^{n_{1}-2\lambda}\varphi_{17}(\varepsilon_{2})}\bigg). |  |

Notice at this point that, from ( 23) (\ref{Aeq20}\hbox{}), ( 25) (\ref{Aeq21}\hbox{}) and ( 26) (\ref{Aeq22}\hbox{}), T 02 = T 02 + = ( T 2 2 ​ ε 2 − 2 ​ λ) ​ ( ε 1 ​ R 11 λ) 2 T_{02}=T_{02}^{+}=(T_{2}^{2}\varepsilon_{2}^{-2\lambda})(\varepsilon_{1}R_{11}^{\lambda})^{2}, which shows in particular that T 2 2 ​ ε 2 − 2 ​ λ T_{2}^{2}\varepsilon_{2}^{-2\lambda} does not depend on ε \varepsilon because this is the case for T 02 T_{02} and, see ( 29) (\ref{Aeq16}\hbox{}), ε 1 ​ R 11 λ = α 11 \varepsilon_{1}R_{11}^{\lambda}=\alpha_{11}. Consequently U 2 − V 2 + W 2 U_{2}-V_{2}+W_{2} does not depend on ε \varepsilon and so ε 2 n 1 − 2 ​ λ ​ ( φ 16 ​ ( ε 2) − φ 17 ​ ( ε 2)) = c \varepsilon_{2}^{n_{1}-2\lambda}(\varphi_{16}(\varepsilon_{2})-\varphi_{17}(\varepsilon_{2}))=c. Since λ ≈ λ 0 ∉ ℚ \lambda\approx\lambda_{0}\notin\mathbb{Q}, this implies that φ 16 = φ 17 \varphi_{16}=\varphi_{17} and therefore

 | T 02 \displaystyle T_{02} | = ( σ 111 λ ​ σ 120 L 1 λ ​ ( σ 210)) 2 ​ ( σ 210 n 1 ​ ( L 2 ​ ( σ 210) σ 221 ​ σ 210 λ) 2 ​ ( Z − σ 211 ​ S 2 2 ​ σ 210 ​ P 1 ​ ( σ 210, 0)) + 1 2 ​ σ 210 n 1 − 2 ​ λ ​ C ^ 2 ​ ( 2 ​ λ − n 1, σ 210)) \displaystyle=\left(\frac{\sigma_{111}^{\lambda}\sigma_{120}}{L_{1}^{\lambda}(\sigma_{210})}\right)^{2}\left(\sigma_{210}^{n_{1}}\left(\frac{L_{2}(\sigma_{210})}{\sigma_{221}\sigma_{210}^{\lambda}}\right)^{2}\left(Z-\frac{\sigma_{211}S_{2}}{2\sigma_{210}P_{1}(\sigma_{210},0)}\right)+\frac{1}{2}\sigma_{210}^{n_{1}-2\lambda}\hat{C}_{2}(2\lambda-n_{1},\sigma_{210})\right) |  |

 |  | = Δ 00 2 ​ σ 210 n 1 ​ ( Z − σ 211 ​ S 2 2 ​ σ 210 ​ P 1 ​ ( σ 210, 0) + σ 221 2 2 ​ L 2 2 ​ ( σ 210) ​ C ^ 2 ​ ( 2 ​ λ − n 1, σ 210)). \displaystyle=\Delta_{00}^{2}\sigma_{210}^{n_{1}}\left(Z-\frac{\sigma_{211}S_{2}}{2\sigma_{210}P_{1}(\sigma_{210},0)}+\frac{\sigma_{221}^{2}}{2L_{2}^{2}(\sigma_{210})}\hat{C}_{2}(2\lambda-n_{1},\sigma_{210})\right). |  |

for all μ ^ ∈ V. {{\hat{\mu}}}\in V. Exactly as before, by applying Lemma 2.3 and Theorem B.1 we can assert that C ^ 2 ​ ( 2 ​ λ − n 1, σ 210) \hat{C}_{2}(2\lambda-n_{1},\sigma_{210}) is 𝒞 ∞ \mathscr{C}^{\infty} in a neighbourhood of any ( λ ⋆, μ ⋆) ∈ W ^ (\lambda_{\star},\mu_{\star})\in\hat{W} such that { λ ⋆, 2 ​ λ ⋆ − n 1 } ∩ ℤ ≥ 0 = ∅. \left\{\lambda_{\star},2\lambda_{\star}-n_{1}\right\}\cap\mathbb{Z}_{\geq 0}=\emptyset. The corresponding condition for the function S 2 S_{2}, see ( 3) (\ref{def_S}\hbox{}), is λ ⋆ ∉ ℤ ≥ 0 \lambda_{\star}\notin\mathbb{Z}_{\geq 0}. Thus the function on the right hand side in the above equality is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D ~ 02 n) × W \big((0,+\infty)\setminus\tilde{D}_{02}^{n}\big)\times W with D ~ 02 n:= ℕ ∪ ℕ ≥ n 1 2 \tilde{D}_{02}^{n}\!:=\mathbb{N}\cup\frac{\mathbb{N}_{\geq n_{1}}}{2}. Due to D 02 n = ℕ 2 D_{02}^{n}=\frac{\mathbb{N}}{2} from Remark 1, it turns out that D 20 n ∪ D ~ 20 n = D 20 n D_{20}^{n}\cup\tilde{D}_{20}^{n}=D_{20}^{n} and, on account of the considerations in the second paragraph of the proof, this shows that the above equality is true in the domain given in the statement. This concludes the proof of the result.

###### Lemma 2.8.

? ⟨ \langle toma ⟩ \rangle?

Let Φ ⁡ ( x, y) \Phi(x,y), with x = ( x 1, x 2, …, x n) ∈ ℝ N x=(x_{1},x_{2},\ldots,x_{n})\in\mathbb{R}^{N} and y ∈ ℝ y\in\mathbb{R}, be a continuous function in a neighbourhood of ( 0, 0) ∈ ℝ N × ℝ. (0,0)\in\mathbb{R}^{N}\times\mathbb{R}. If y ​ Φ ​ ( x, y) y\Phi(x,y) is analytic in a neighbourhood of ( 0, 0) (0,0) then Φ ⁡ ( x, y) \Phi(x,y) is analytic in a neighbourhood of ( 0, 0) (0,0).

By the Weierstrass Division Theorem (see [11, Theorem 1.8] or [15, Theorem 6.1.3]) there exist a neighbourhood U U of 0 ∈ ℝ N 0\in\mathbb{R}^{N} and an open interval I I containing y = 0 y=0 such that y ​ Φ ​ ( x, y) = y ​ g ​ ( x, y) + r ⁡ ( x) y\Phi(x,y)=yg(x,y)+r(x) with g ∈ 𝒞 ω ​ ( U × I) g\in\mathscr{C}^{\omega}(U\times I) and r ∈ 𝒞 ω ​ ( I) r\in\mathscr{C}^{\omega}(I). The evaluation of this equality at y = 0 y=0 yields r ≡ 0. r\equiv 0. Consequently Φ ⁡ ( x, y) = g ⁡ ( x, y) \Phi(x,y)=g(x,y) for all ( x, y) ∈ U × ( I ∖ { 0 }) (x,y)\in U\times(I\setminus\{0\}) and, by the continuity of Φ \Phi in a neighbourhood of ( 0, 0) (0,0), we easily get Φ ≡ g \Phi\equiv g on U × I U\times I. This proves the result because g ∈ 𝒞 ω ​ ( U × I) g\in\mathscr{C}^{\omega}(U\times I).

###### Proposition 2.9.

? ⟨ \langle pre-analitico ⟩ \rangle?

In the analytic setting ( ( see Remark 1)), the following assertions hold:

1. ( a) (a)

The coefficient Δ i ​ j \Delta_{ij} of the Dulac map is 𝒞 ω \mathscr{C}^{\omega} on ( ( 0, + ∞) ∖ D i ​ j 0) × W ((0,+\infty)\setminus D_{ij}^{0})\times W for ( i, j) ∈ { ( 0, 0), ( 1, 0), ( 0, 1), ( 1, 1) } (i,j)\in\{(0,0),(1,0),(0,1),(1,1)\}.

2. ( b) (b)

For each ( i, j) ∈ { ( n 1, 0), ( 0, n 2), ( n 1 + 1, 0), ( 0, n 2 + 1) } (i,j)\in\{(n_{1},0),(0,n_{2}),(n_{1}+1,0),(0,n_{2}+1)\}, the coefficient T i ​ j T_{ij} of the Dulac time is analytic on ( ( 0, + ∞) ∖ D i ​ j n) × W ((0,+\infty)\setminus D_{ij}^{n})\times W. This is also the case for ( i, j) = ( 2, 0) (i,j)=(2,0) and ( i, j) = ( 0, 2) (i,j)=(0,2) assuming n 1 = 0 n_{1}=0 and n 2 = 0 n_{2}=0, respectively.

By applying Lemma 2.3 we know that, for i = 1, 2 i=1,2, the functions L i ​ ( u, μ ^) L_{i}(u;{{\hat{\mu}}}), M i ​ ( u, μ ^) M_{i}(u;{{\hat{\mu}}}) and A i ​ ( u, μ ^) A_{i}(u;{{\hat{\mu}}}) given in ( 2) (\ref{def_fun}\hbox{}) are analytic on I i × W ^ I_{i}\times\hat{W}. In addition,

- •

the functions B 1 ​ ( u, μ ^) B_{1}(u;{{\hat{\mu}}}) and C 1 ​ ( u, μ ^) C_{1}(u;{{\hat{\mu}}}) are analytic on I 1 × ( ( 0, + ∞) ∖ 1 ℕ) × W I_{1}\times((0,+\infty)\setminus\frac{1}{\mathbb{N}})\times W, and

- •

the functions B 2 ​ ( u, μ ^) B_{2}(u;{{\hat{\mu}}}) and C 2 ​ ( u, μ ^) C_{2}(u;{{\hat{\mu}}}) are analytic on I 2 × ( ( 0, + ∞) ∖ ℕ) × W I_{2}\times((0,+\infty)\setminus\mathbb{N})\times W.

Moreover, since the parametrization σ i ​ ( s, μ ^) \sigma_{i}(s;{{\hat{\mu}}}) of the transverse section Σ i \Sigma_{i} is analytic by assumption for i = 1, 2 i=1,2, from ( 3) (\ref{def_S}\hbox{}) we get that S 1 ​ ( λ, μ) S_{1}(\lambda,\mu) and S 2 ​ ( λ, μ) S_{2}(\lambda,\mu) are analytic on ( ( 0, + ∞) ∖ 1 ℕ) × W ((0,+\infty)\setminus\frac{1}{\mathbb{N}})\times W and ( ( 0, + ∞) ∖ ℕ) × W, ((0,+\infty)\setminus\mathbb{N})\times W, respectively.

The fact that each coefficient Δ i ​ j ​ ( λ, μ) \Delta_{ij}(\lambda,\mu) in assertion ( b) (b) of Theorem A is analytic on ( ( 0, + ∞) ∖ D i ​ j 0) × W ((0,+\infty)\setminus D_{ij}^{0})\times W follows readily from regularity properties stated in the previous paragraph because, see Remark 1,

 | D 00 0 = ∅, D 01 0 = ℕ, D 10 0 = 1 ℕ ​ and ​ D 11 0 = ℕ ∪ 1 ℕ. D_{00}^{0}=\emptyset,\;D_{01}^{0}=\mathbb{N},\;D_{10}^{0}=\frac{1}{\mathbb{N}}\text{ and }D_{11}^{0}=\mathbb{N}\cup\frac{1}{\mathbb{N}}. |  |

This proves assertion ( a) (a).

By the first assertion in ( d) (d) of Theorem B.1, the regularity properties established in the first paragraph also imply that each coefficient T i ​ j ​ ( λ, μ) T_{ij}(\lambda,\mu) listed in ( c) (c) of Theorem A is analytic on ( ( 0, + ∞) ∖ D i ​ j n) × W ((0,+\infty)\setminus D_{ij}^{n})\times W, with the exception of the special values

- •

λ = 1 k \lambda=\frac{1}{k} with k ∈ { 1, 2, …, ⌈ n 2 n 1 + 1 ⌉ − 1 } k\in\big\{1,2,\ldots,\lceil\frac{n_{2}}{n_{1}+1}\rceil-1\big\} for T n 1 + 1, 0 ​ ( λ, μ) T_{n_{1}+1,0}(\lambda,\mu), and

- •

λ = 1 k \lambda=\frac{1}{k} with k ∈ { 1, 2, …, ⌈ n 2 2 ⌉ − 1 } k\in\big\{1,2,\ldots,\lceil\frac{n_{2}}{2}\rceil-1\big\} for T 20 ​ ( λ, μ) T_{20}(\lambda,\mu),

where the respective formula does not hold. Indeed this follows using that, see Remark 1 again, D 00 n = ∅ D_{00}^{n}=\emptyset,

 | D n 1, 0 n = ⋃ i = 1 n 1 i ℕ ≥ n 2, D 0, n 2 n = { ℕ ≥ n 1 n 2 if n 2 ⩾ 1, ∅ if n 2 = 0, ​ D n 1 + 1, 0 n = ⋃ i = 1 n 1 + 1 i ℕ ≥ n 2 ​ and ​ D 0, n 2 + 1 n = ℕ ≥ n 1 n 2 + 1 ∪ ℕ, D_{n_{1},0}^{n}=\bigcup_{i=1}^{n_{1}}\frac{i}{\mathbb{N}_{\geq n_{2}}},\;D_{0,n_{2}}^{n}=\left\{\begin{array}[]{cl}\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}}&\text{ if $n_{2}\geqslant 1$,}\\[5.0pt] \emptyset&\text{ if $n_{2}=0$,}\end{array}\right.\;D_{n_{1}+1,0}^{n}=\bigcup_{i=1}^{n_{1}+1}\frac{i}{\mathbb{N}_{\geq n_{2}}}\text{ and }D_{0,n_{2}+1}^{n}=\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}+1}\cup\mathbb{N}, |  |

together with D 20 n = 2 ℕ ≥ n 2 D_{20}^{n}=\frac{2}{\mathbb{N}_{\geq n_{2}}} for n 1 = 0 n_{1}=0 and D 02 n = ℕ 2 D_{02}^{n}=\frac{\mathbb{N}}{2} for n 2 = 0 n_{2}=0. For instance, due to A 2 ​ ( u, μ ^) ∈ 𝒞 ω ​ ( I 2 × W ^) A_{2}(u;{{\hat{\mu}}})\in\mathscr{C}^{\omega}(I_{2}\times\hat{W}), the first assertion in ( d) (d) of Theorem B.1 implies that A ^ 2 ​ ( α, u, μ ^) \hat{A}_{2}(\alpha,u;{{\hat{\mu}}}) is analytic on ( ℝ ∖ ℤ ≥ 0) × I 2 × W ^ (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I_{2}\times\hat{W} and hence

 | T 0, n 2 ​ ( μ ^) = Δ 00 n 2 ​ σ 210 n 1 ​ σ 221 n 2 L 2 n 2 ​ ( σ 210) ​ A ^ 2 ​ ( n 2 ​ λ − n 1, σ 210) T_{0,n_{2}}({{\hat{\mu}}})=\Delta_{00}^{n_{2}}\frac{\sigma_{210}^{n_{1}}\sigma_{221}^{n_{2}}}{L_{2}^{n_{2}}(\sigma_{210})}\hat{A}_{2}(n_{2}\lambda-n_{1},\sigma_{210}) |  |

is analytic at λ = λ 0 \lambda=\lambda_{0} provided that n 2 ​ λ 0 − n 1 ∉ ℤ ≥ 0, n_{2}\lambda_{0}-n_{1}\notin\mathbb{Z}_{\geq 0}, i.e., λ 0 ∉ D 0, n 2 n \lambda_{0}\notin D_{0,n_{2}}^{n}. The analysis of the other coefficients follows similarly and the details are omitted for the sake of brevity.

So let us focus on the analyticity of T n 1 + 1, 0 T_{n_{1}+1,0} and T 20 T_{20} at the special values listed above. In order to study the first case let us fix λ 0 = 1 k \lambda_{0}=\frac{1}{k} with k ∈ { 1, …, ⌈ n 2 n 1 + 1 ⌉ − 1 } k\in\{1,\ldots,\lceil\frac{n_{2}}{n_{1}+1}\rceil-1\}. Note that we can write, see ( c) (c) in Theorem A,

 | T n 1 + 1, 0 = f 0 + f 1 ​ S 1 ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120) + f 2 ​ B ^ 1 ​ ( ( n 1 + 1) / λ − n 2, σ 120) T_{n_{1}+1,0}=f_{0}+f_{1}S_{1}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})+f_{2}\hat{B}_{1}\big((n_{1}+1)/\lambda-n_{2},\sigma_{120}\big) |  | (37) |

where, see ( 2) (\ref{def_fun}\hbox{}), B 1 ​ ( u) = g 1 ​ ( u) ​ M ^ 1 ​ ( 1 / λ, u) + g 2 ​ ( u) B_{1}(u)=g_{1}(u)\hat{M}_{1}(1/\lambda,u)+g_{2}(u) and S 1 = f 3 + f 4 ​ M ^ 1 ​ ( 1 / λ, σ 120) S_{1}=f_{3}+f_{4}\hat{M}_{1}(1/\lambda,\sigma_{120}) with g i ​ ( u, μ ^) ∈ 𝒞 ω ​ ( I 1 × W ^) g_{i}(u;{{\hat{\mu}}})\in\mathscr{C}^{\omega}(I_{1}\times\hat{W}) and f i ​ ( μ ^) ∈ 𝒞 ω ​ ( W ^) f_{i}({{\hat{\mu}}})\in\mathscr{C}^{\omega}(\hat{W}). That being said we argue as follows:

1. 1.

A ^ 1 ​ ( n 1 / λ − n 2, σ 120) \hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120}) is analytic at λ = λ 0 \lambda=\lambda_{0} due to n 1 λ 0 − n 2 = n 1 ​ k − n 2 ∈ ℤ < 0 \frac{n_{1}}{\lambda_{0}}-n_{2}=n_{1}k-n_{2}\in\mathbb{Z}_{<0} by the first assertion in ( d) (d) of Theorem B.1.

2. 2.

( λ − λ 0) ​ M ^ 1 ​ ( 1 / λ, u, μ ^) (\lambda-\lambda_{0})\hat{M}_{1}(1/\lambda,u;{{\hat{\mu}}}), and consequently ( λ − λ 0) ​ B 1 ​ ( u, μ ^) (\lambda-\lambda_{0})B_{1}(u;{{\hat{\mu}}}) and ( λ − λ 0) ​ S 1 ​ ( μ ^) (\lambda-\lambda_{0})S_{1}({{\hat{\mu}}}), extends analytically at λ = λ 0 \lambda=\lambda_{0} by the second assertion in ( d) (d) of Theorem B.1 since 1 / λ 0 = k ∈ ℤ ≥ 0, 1/\lambda_{0}=k\in\mathbb{Z}_{\geq 0},

3. 3.

and this implies (in this case by applying the first assertion) that ( λ − λ 0) ​ B ^ 1 ​ ( ( n 1 + 1) / λ − n 2, σ 120) (\lambda-\lambda_{0})\hat{B}_{1}((n_{1}+1)/\lambda-n_{2},\sigma_{120}) extends analytically at λ = λ 0 \lambda=\lambda_{0} because n 1 + 1 λ 0 − n 2 = ( n 1 + 1) ​ k − n 2 ∈ ℤ < 0. \frac{n_{1}+1}{\lambda_{0}}-n_{2}=(n_{1}+1)k-n_{2}\in\mathbb{Z}_{<0}.

Taking this into account, from ( 37) (\ref{corBeq1}\immediate) it follows readily that ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) (\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}}) extends analytically at λ = λ 0 \lambda=\lambda_{0}. On the other hand, since λ 0 ∉ D n 1 + 1, 0 n \lambda_{0}\notin D_{n_{1}+1,0}^{n}, note that T n 1 + 1, 0 ​ ( μ ^) T_{n_{1}+1,0}({{\hat{\mu}}}) is smooth at λ = λ 0 \lambda=\lambda_{0} by ( b) (b) in Theorem 1.6. Accordingly, in view of Lemma 2.8, we can assert that T n 1 + 1, 0 ​ ( μ ^) T_{n_{1}+1,0}({{\hat{\mu}}}) is analytic at λ = λ 0 \lambda=\lambda_{0} as desired.

Let us turn next to the second case. So let us fix λ 0 = 1 k \lambda_{0}=\frac{1}{k} with k ∈ { 1, …, ⌈ n 2 2 ⌉ − 1 } k\in\{1,\ldots,\lceil\frac{n_{2}}{2}\rceil-1\} and observe that from ( c) (c) in Theorem A we get that if n 1 = 0 n_{1}=0 then we can write

 | T 20 = f 0 + f 1 ​ C ^ 1 ​ ( 2 / λ − n 2, σ 120) + f 2 ​ S 1 ​ B ^ 1 ​ ( 1 / λ − n 2, σ 120) T_{20}=f_{0}+f_{1}\hat{C}_{1}(2/\lambda-n_{2},\sigma_{120})+f_{2}S_{1}\hat{B}_{1}(1/\lambda-n_{2},\sigma_{120}) |  | (38) |

with, see ( 2) (\ref{def_fun}\hbox{}), C 1 ​ ( u) = B 1 ​ ( u) ​ ( L 1 ​ ( u) + 2 ​ M ^ 1 ​ ( 1 / λ, u)) C_{1}(u)=B_{1}(u)\big(L_{1}(u)+2\hat{M}_{1}(1/\lambda,u)\big) and S 1 = f 3 + f 4 ​ M ^ 1 ​ ( 1 / λ, σ 120) S_{1}=f_{3}+f_{4}\hat{M}_{1}(1/\lambda,\sigma_{120}) for some f i ∈ 𝒞 ω ​ ( W ^) f_{i}\in\mathscr{C}^{\omega}(\hat{W}). We point out that in this case, since n 1 = 0, n_{1}=0, B 1 ​ ( u) = L 1 ​ ( u) ​ ∂ 1 P 2 − 1 ​ ( 0, u) B_{1}(u)=L_{1}(u)\partial_{1}P_{2}^{-1}(0,u) is analytic on I 1 × W ^. I_{1}\times\hat{W}. Then we proceed as follows:

1. 1.

B ^ 1 ​ ( 1 / λ − n 2, σ 120) \hat{B}_{1}(1/\lambda-n_{2},\sigma_{120}) is analytic at λ = λ 0 \lambda=\lambda_{0} due to 1 / λ 0 − n 2 = k − n 2 ∈ ℤ < 0 1/\lambda_{0}-n_{2}=k-n_{2}\in\mathbb{Z}_{<0} by the first assertion in ( d) (d) of Theorem B.1.

2. 2.

( λ − λ 0) ​ M ^ 1 ​ ( 1 / λ, u, μ ^) (\lambda-\lambda_{0})\hat{M}_{1}(1/\lambda,u;{{\hat{\mu}}}) extends analytically at λ = λ 0 \lambda=\lambda_{0} by the second assertion in ( d) (d) of Theorem B.1 because 1 / λ 0 = k ∈ ℤ ≥ 0 1/\lambda_{0}=k\in\mathbb{Z}_{\geq 0} and,

3. 3.

consequently, this is so for ( λ − λ 0) ​ S 1 ​ ( μ ^) (\lambda-\lambda_{0})S_{1}({{\hat{\mu}}}) and ( λ − λ 0) ​ C ^ 1 ​ ( 2 / λ − n 2, σ 120), (\lambda-\lambda_{0})\hat{C}_{1}(2/\lambda-n_{2},\sigma_{120}), the latter by the first assertion in ( d) (d) of Theorem B.1 since 2 / λ 0 − n 2 = 2 ​ k − n 2 ∈ ℤ < 0. 2/\lambda_{0}-n_{2}=2k-n_{2}\in\mathbb{Z}_{<0}.

On account of this, from ( 38) (\ref{corBeq2}\immediate) we get that ( λ − λ 0) ​ T 20 ​ ( μ ^) (\lambda-\lambda_{0})T_{20}({{\hat{\mu}}}) extends analytically at λ = λ 0. \lambda=\lambda_{0}. Exactly as before, it happens that T 20 ​ ( μ ^) T_{20}({{\hat{\mu}}}) is smooth at λ = λ 0 \lambda=\lambda_{0} by ( b) (b) in Theorem 1.6 due to λ 0 ∉ D 20 n. \lambda_{0}\notin D_{20}^{n}. Therefore, by Lemma 2.8 again, we can assert that T 20 ​ ( μ ^) T_{20}({{\hat{\mu}}}) is analytic at λ = λ 0 \lambda=\lambda_{0} as desired. This proves the validity of ( b) (b).

## 3 Poles and residues of the coefficients

Let us recall, see Theorem 1.6, that the coefficient Δ i ​ j ​ ( λ, μ) \Delta_{ij}(\lambda,\mu) of the Dulac map is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D i ​ j 0) × W ((0,+\infty)\setminus D_{ij}^{0})\times W for each ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} and the coefficient T i ​ j ​ ( λ, μ) T_{ij}(\lambda,\mu) of the Dulac time is 𝒞 ∞ \mathscr{C}^{\infty} on ( ( 0, + ∞) ∖ D i ​ j n) × W ((0,+\infty)\setminus D_{ij}^{n})\times W for each ( i, j) ∈ Λ n. (i,j)\in\Lambda_{n}. The next result is addressed to the behaviour of these coefficients at the boundaries of their respective domains of definition.

###### Lemma 3.1.

? ⟨ \langle polos ⟩ \rangle?

Consider the coefficients Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} of the Dulac map and the Dulac time, respectively, given by Theorem 1.6. The following assertions hold:

1. ( a) (a)

If ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} and λ 0 ∈ D i ​ j 0 \lambda_{0}\in D_{ij}^{0} then there exists ℓ ∈ ℤ ≥ 0 \ell\in\mathbb{Z}_{\geq 0} such that the function μ ^ ↦ ( λ − λ 0) ℓ ​ Δ i ​ j ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{\ell}\Delta_{ij}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} to { λ 0 } × W \{\lambda_{0}\}\times W.

2. ( b) (b)

If ( i, j) ∈ Λ n (i,j)\in\Lambda_{n} and λ 0 ∈ D i ​ j n \lambda_{0}\in D_{ij}^{n} then there exists ℓ ∈ ℤ ≥ 0 \ell\in\mathbb{Z}_{\geq 0} such that the function μ ^ ↦ ( λ − λ 0) ℓ ​ T i ​ j ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{\ell}T_{ij}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} to { λ 0 } × W \{\lambda_{0}\}\times W.

Moreover, setting λ 0 = p / q \lambda_{0}=p/q with gcd ⁡ ( p, q) = 1 \gcd(p,q)=1, the estimates ℓ ⩽ i p + j q ⩽ i + j \ell\leqslant\frac{i}{p}+\frac{j}{q}\leqslant i+j hold in both cases.

For convenience we prove ( b) (b) first. Due to λ 0 ∈ D i ​ j n \lambda_{0}\in D_{ij}^{n}, we have λ 0 ∈ ℚ \lambda_{0}\in\mathbb{Q} and we write λ 0 = p / q \lambda_{0}=p/q with gcd ⁡ ( p, q) = 1. \gcd(p,q)=1. Setting r n:= max ⁡ { r ∈ ℤ ≥ 0: ( i, j) + r ⁡ ( p, − q) ∈ Λ n } r_{n}\!:=\max\{r\in\mathbb{Z}_{\geq 0}:(i,j)+r(p,-q)\in\Lambda_{n}\}, we define ( i n, j n) = ( i, j) + r n ​ ( p, − q) (i_{n},j_{n})=(i,j)+r_{n}(p,-q). Then λ 0 ∈ D i n, j n n \lambda_{0}\in D_{i_{n},j_{n}}^{n}, 𝒜 i n ​ j n ​ λ 0 n ≠ ∅ \mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n}\neq\emptyset, see Definition 1, and we take ℓ:= max ⁡ 𝒜 i n ​ j n ​ λ 0 n. \ell\!:=\max\mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n}. By ( b ​ 2) (b2) in Theorem 1.6 we know that 𝑻 i n, j n λ 0 ​ ( w, μ ^) ∈ 𝒞 ∞ ​ ( U ^) ​ [w] \boldsymbol{T}_{i_{n},j_{n}}^{\lambda_{0}}(w;{{\hat{\mu}}})\in\mathscr{C}^{\infty}(\hat{U})[w], where U ^ \hat{U} is an open neighbourhood of { λ 0 } × W, \{\lambda_{0}\}\times W, and

 | 𝑻 i n ​ j n λ 0 ​ ( w, μ ^) = ∑ r ∈ 𝒜 i n ​ j n ​ λ 0 n T i n − r ​ p, j n + r ​ q ​ ( μ ^) ​ ( 1 + α ​ w) r ​ for λ ≠ λ 0, \boldsymbol{T}_{i_{n}j_{n}}^{\lambda_{0}}(w;{{\hat{\mu}}})=\sum_{r\in\mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n}}T_{i_{n}-rp,j_{n}+rq}({{\hat{\mu}}})(1+\alpha w)^{r}\text{ for $\lambda\neq\lambda_{0}$,} |  |

where α = p − λ ​ q. \alpha=p-\lambda q. Let us write 𝑻 i n ​ j n λ 0 ​ ( w, μ ^) = ∑ k = 0 ℓ A k ​ ( μ ^) ​ w k \boldsymbol{T}_{i_{n}j_{n}}^{\lambda_{0}}(w;{{\hat{\mu}}})=\sum_{k=0}^{\ell}A_{k}({{\hat{\mu}}})w^{k} with A k ∈ 𝒞 ∞ ​ ( U ^) A_{k}\in\mathscr{C}^{\infty}(\hat{U}). For convenience we define u:= 1 + α ​ w, u\!:=1+\alpha w, so that w = α − 1 ​ ( u − 1) w=\alpha^{-1}(u-1) for α ≠ 0 \alpha\neq 0. Thus w k = α − k ​ ∑ r = 0 k ( k r) ​ ( − 1) k − r ​ u r w^{k}=\alpha^{-k}\sum_{r=0}^{k}{k\choose r}(-1)^{k-r}u^{r} and, for λ ≠ λ 0, \lambda\neq\lambda_{0},

 | 𝑻 i n ​ j n λ 0 ​ ( w, μ ^) = ∑ r = 0 ℓ ( ∑ k = r ℓ A k ​ ( μ ^) ​ α − k ​ ( k r) ​ ( − 1) k − r) ​ ( 1 + α ​ w) r. \boldsymbol{T}_{i_{n}j_{n}}^{\lambda_{0}}(w;{{\hat{\mu}}})=\sum_{r=0}^{\ell}\left(\sum_{k=r}^{\ell}A_{k}({{\hat{\mu}}})\alpha^{-k}{k\choose r}(-1)^{k-r}\right)(1+\alpha w)^{r}. |  |

Accordingly this shows that T i n − r ​ p, j n + r ​ q ​ ( μ ^) = ∑ k = r ℓ A k ​ ( μ ^) ​ α − k ​ ( k r) ​ ( − 1) k − r T_{i_{n}-rp,j_{n}+rq}({{\hat{\mu}}})=\sum_{k=r}^{\ell}A_{k}({{\hat{\mu}}})\alpha^{-k}{k\choose r}(-1)^{k-r} provided that r ∈ 𝒜 i n ​ j n ​ λ 0 n r\in\mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n} and λ ≠ λ 0 \lambda\neq\lambda_{0}. With regard to the first condition let us observe that r n ∈ 𝒜 i n ​ j n ​ λ 0 n r_{n}\in\mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n} by construction. Hence T i, j ​ ( μ ^) = ∑ k = r n ℓ A k ​ ( μ ^) ​ α − k ​ ( k r n) ​ ( − 1) k − r n T_{i,j}({{\hat{\mu}}})=\sum_{k=r_{n}}^{\ell}A_{k}({{\hat{\mu}}})\alpha^{-k}{k\choose r_{n}}(-1)^{k-r_{n}} and, due to α = q ⁡ ( λ 0 − λ), \alpha=q(\lambda_{0}-\lambda),

 | ( λ − λ 0) ℓ ​ T i, j ​ ( μ ^) = ( − 1) r n ​ ∑ k = r n ℓ q − k ​ A k ​ ( μ ^) ​ ( λ − λ 0) ℓ − k ​ ( k r n) ​ for λ ≠ λ 0. (\lambda-\lambda_{0})^{\ell}T_{i,j}({{\hat{\mu}}})=(-1)^{r_{n}}\sum_{k=r_{n}}^{\ell}q^{-k}A_{k}({{\hat{\mu}}})(\lambda-\lambda_{0})^{\ell-k}{k\choose r_{n}}\text{ for $\lambda\neq\lambda_{0}$}. |  |

Since A k ∈ 𝒞 ∞ ​ ( U ^) A_{k}\in\mathscr{C}^{\infty}(\hat{U}), this shows that μ ^ ↦ ( λ − λ 0) ℓ ​ T i ​ j ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{\ell}T_{ij}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} to { λ 0 } × W \{\lambda_{0}\}\times W and proves ( b) (b).

The proof of ( a) (a) follows verbatim replacing n = ( n 1, n 2) n=(n_{1},n_{2}) by 0 = ( 0, 0) 0=(0,0) and is omitted for the sake of shortness. Let us turn now to the proof of the last assertion in the statement. The estimate for the the case in ( a) (a), i.e., ( i, j) ∈ Λ 0 (i,j)\in\Lambda_{0} and λ 0 ∈ D i ​ j 0, \lambda_{0}\in D_{ij}^{0}, is clear because

 | max ⁡ 𝒜 i 0 ​ j 0 ​ λ 0 0 ⩽ i 0 p = i p + r 0 ⩽ i p + j q ⩽ i + j. \max\mathscr{A}_{i_{0}j_{0}\lambda_{0}}^{0}\leqslant\frac{i_{0}}{p}=\frac{i}{p}+r_{0}\leqslant\frac{i}{p}+\frac{j}{q}\leqslant i+j. |  |

Here the first inequality follows using that 𝒜 i 0 ​ j 0 ​ λ 0 0 ≠ ∅ \mathscr{A}_{i_{0}j_{0}\lambda_{0}}^{0}\neq\emptyset and ( i 0 − r ​ p, j 0 + r ​ q) ∈ Λ 0 = ℤ ≥ 0 × ℤ ≥ 0 (i_{0}-rp,j_{0}+rq)\in\Lambda_{0}=\mathbb{Z}_{\geq 0}\times\mathbb{Z}_{\geq 0} for all r ∈ 𝒜 i 0 ​ j 0 ​ λ 0 0 r\in\mathscr{A}_{i_{0}j_{0}\lambda_{0}}^{0}, see Definition 1, the equality is due to ( i 0, j 0):= ( i, j) + r 0 ​ ( p, − q) (i_{0},j_{0})\!:=(i,j)+r_{0}(p,-q), the second inequality is a consequence of j − r 0 ​ q = j 0 ⩾ 0 j-r_{0}q=j_{0}\geqslant 0 and the third inequality is evident since p, q ∈ ℕ. p,q\in\mathbb{N}. Finally, the estimate for the case in ( b) (b), i.e., ( i, j) ∈ Λ n (i,j)\in\Lambda_{n} and λ 0 ∈ D i ​ j n, \lambda_{0}\in D_{ij}^{n}, is a consequence of the previous discussion and the fact that, by construction, 𝒜 i n ​ j n ​ λ 0 n ≠ ∅ \mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n}\neq\emptyset and max ⁡ 𝒜 i n ​ j n ​ λ 0 n ⩽ max ⁡ 𝒜 i 0 ​ j 0 ​ λ 0 0 \max\mathscr{A}_{i_{n}j_{n}\lambda_{0}}^{n}\leqslant\max\mathscr{A}_{i_{0}j_{0}\lambda_{0}}^{0}. This completes the proof of the result.

By Lemma 3.1 the coefficients Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} have poles at D i ​ j 0 × W D_{ij}^{0}\times W and D i ​ j n × W D_{ij}^{n}\times W, respectively, of order at most i + j. i+j. This is a general result, meaning that it holds for any ( i, j). (i,j). Theorem A provides the explicit expression of some of these coefficients and the rest of the present section is devoted to give sharps bounds for the order of their poles. We will also compute the residues of these coefficients at their poles, which determine the values of the leading terms of the polynomials 𝚫 i ​ j λ 0 ​ ( ω, μ ^) \boldsymbol{\Delta}_{ij}^{\lambda_{0}}(\omega;{{\hat{\mu}}}) at λ 0 ∈ D i ​ j 0 \lambda_{0}\in D_{ij}^{0} and 𝑻 i ​ j λ 0 ​ ( ω, μ ^) \boldsymbol{T}_{ij}^{\lambda_{0}}(\omega;{{\hat{\mu}}}) at λ 0 ∈ D i ​ j n \lambda_{0}\in D_{ij}^{n} (see Theorem 4.1 and Theorem 4.3, respectively, in Section 4). We illustrate the use of the residues for this purpose in Example 4. Let us also advance that at the end of the section we will finish the proof of Corollary B, which shows that in the analytic setting these coefficients are meromorphic on W ^ = ( 0, + ∞) × W \hat{W}=(0,+\infty)\times W.

With regard to the next statement we recall that D 01 0 = ℕ D_{01}^{0}=\mathbb{N}, D 10 0 = 1 ℕ D_{10}^{0}=\frac{1}{\mathbb{N}} and D 11 0 = ℕ ∪ 1 ℕ D_{11}^{0}=\mathbb{N}\cup\frac{1}{\mathbb{N}} (see Remark 1).

###### Proposition 3.2.

? ⟨ \langle poles1 ⟩ \rangle?

The following assertions hold:

1. ( a) (a)

For any μ ^ 0 = ( λ 0, μ 0) ∈ D 10 0 × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{10}^{0}\times W, the function μ ^ ↦ ( λ − λ 0) ​ Δ 10 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})\Delta_{10}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}, and if λ 0 = 1 i \lambda_{0}=\frac{1}{i} with i ∈ ℕ i\in\mathbb{N} then lim μ ^ → μ ^ 0 ( λ − λ 0) ​ Δ 10 ​ ( μ ^) = − Δ 00 ​ σ 111 ​ σ 120 i L 1 ​ ( σ 120) ​ i 3 ​ M 1 ( i) ​ ( 0) i! | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})\Delta_{10}({{\hat{\mu}}})=-\frac{\Delta_{00}\sigma_{111}\sigma_{120}^{i}}{L_{1}(\sigma_{120})i^{3}}\frac{M_{1}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

2. ( b) (b)

For any μ ^ 0 = ( λ 0, μ 0) ∈ D 01 0 × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{01}^{0}\times W, the function μ ^ ↦ ( λ − λ 0) ​ Δ 01 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})\Delta_{01}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}, and if λ 0 = i ∈ ℕ \lambda_{0}=i\in\mathbb{N} then lim μ ^ → μ ^ 0 ( λ − λ 0) ​ Δ 01 ​ ( μ ^) = − Δ 00 2 ​ σ 221 ​ σ 210 i L 2 ​ ( σ 210) ​ M 2 ( i) ​ ( 0) i! | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})\Delta_{01}({{\hat{\mu}}})=-\frac{\Delta_{00}^{2}\sigma_{221}\sigma_{210}^{i}}{L_{2}(\sigma_{210})}\frac{M_{2}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

3. ( c) (c)

For any μ ^ 0 = ( λ 0, μ 0) ∈ ( D 11 0 ∖ { 1 }) × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in(D_{11}^{0}\setminus\{1\})\times W, the function μ ^ ↦ ( λ − λ 0) ​ Δ 11 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})\Delta_{11}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and

  1. ( c ​ 1) (c1)

if λ 0 = 1 i \lambda_{0}=\frac{1}{i} with i ∈ ℕ ≥ 2 i\in\mathbb{N}_{\geq 2} then lim μ ^ → μ ^ 0 ( λ − λ 0) ​ Δ 11 ​ ( μ ^) = 2 ​ Δ 00 2 ​ σ 111 ​ σ 120 i L 1 ​ ( σ 120) ​ i 3 ​ M 1 ( i) ​ ( 0) i! ​ S 2 | μ ^ = μ ^ 0, \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})\Delta_{11}({{\hat{\mu}}})=\frac{2\Delta_{00}^{2}\sigma_{111}\sigma_{120}^{i}}{L_{1}(\sigma_{120})i^{3}}\frac{M_{1}^{(i)}(0)}{i!}S_{2}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}},

  2. ( c ​ 2) (c2)

if λ 0 = i ∈ ℕ ≥ 2 \lambda_{0}=i\in\mathbb{N}_{\geq 2} then lim μ ^ → μ ^ 0 ( λ − λ 0) ​ Δ 11 ​ ( μ ^) = − 2 ​ i ​ Δ 00 2 ​ σ 221 ​ σ 210 i L 2 ​ ( σ 210) ​ M 2 ( i) ​ ( 0) i! ​ S 1 | μ ^ = μ ^ 0 \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})\Delta_{11}({{\hat{\mu}}})=-\frac{2i\Delta_{00}^{2}\sigma_{221}\sigma_{210}^{i}}{L_{2}(\sigma_{210})}\frac{M_{2}^{(i)}(0)}{i!}S_{1}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

Finally, for any μ ^ 0 = ( λ 0, μ 0) ∈ { 1 } × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in\{1\}\times W, the function μ ^ ↦ ( λ − λ 0) 2 ​ Δ 11 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{2}\Delta_{11}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and lim μ ^ → μ ^ 0 ( λ − λ 0) 2 ​ Δ 11 ​ ( μ ^) = 2 ​ Δ 00 2 ​ σ 111 ​ σ 120 ​ M 1 ′ ​ ( 0) OPEN L 1 ​ ( σ 120)) ​ σ 221 ​ σ 210 ​ M 2 ′ ​ ( 0) L 2 ​ ( σ 210) | μ ^ = μ ^ 0 \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})^{2}\Delta_{11}({{\hat{\mu}}})=2\Delta_{00}^{2}\frac{\sigma_{111}\sigma_{120}M_{1}^{\prime}(0)}{L_{1}(\sigma_{120}))}\frac{\sigma_{221}\sigma_{210}M_{2}^{\prime}(0)}{L_{2}(\sigma_{210})}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

In order to show ( a) (a) we fix μ ^ 0 = ( 1 / i, μ 0) ∈ D 10 0 × W {{\hat{\mu}}}_{0}=(1/i,\mu_{0})\in D_{10}^{0}\times W with i ∈ ℕ i\in\mathbb{N} and note that, by ( b) (b) in Theorem A, Δ 10 = Δ 00 ​ λ ​ S 1 \Delta_{10}=\Delta_{00}\lambda S_{1} where Δ 00 ∈ 𝒞 ∞ ​ ( W ^) \Delta_{00}\in\mathscr{C}^{\infty}(\hat{W}) and, see ( 3) (\ref{def_S}\hbox{}), S 1 = f 1 − σ 111 L 1 ​ ( σ 120) ​ M ^ 1 ​ ( 1 / λ, σ 120) S_{1}=f_{1}-\frac{\sigma_{111}}{L_{1}(\sigma_{120})}\hat{M}_{1}(1/\lambda,\sigma_{120}) with f 1 ∈ 𝒞 ∞ ​ ( W ^) f_{1}\in\mathscr{C}^{\infty}(\hat{W}). On account of this and ( c) (c) in Theorem B.1, the function ( λ − 1 / i) ​ Δ 10 ​ ( μ ^) (\lambda-1/i)\Delta_{10}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and

 | lim μ ^ → μ ^ 0 ( λ − 1 / i) ​ S 1 = − σ 111 L 1 ​ ( σ 120) | μ ^ = μ ^ 0 ​ lim μ ^ → μ ^ 0 i − 1 / λ i / λ ​ M ^ 1 ​ ( 1 / λ, σ 120) = − σ 111 L 1 ​ ( σ 120) ​ i 2 ​ M 1 ( i) ​ ( 0) i! ​ σ 120 i | μ ^ = μ ^ 0. \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-1/i)S_{1}=\frac{-\sigma_{111}}{L_{1}(\sigma_{120})}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}\frac{i-1/\lambda}{i/\lambda}\hat{M}_{1}(1/\lambda,\sigma_{120})=\frac{-\sigma_{111}}{L_{1}(\sigma_{120})i^{2}}\frac{M_{1}^{(i)}(0)}{i!}\sigma_{120}^{i}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  | (39) |

Therefore lim μ ^ → μ ^ 0 ( λ − 1 / i) ​ Δ 10 ​ ( μ ^) = − Δ 00 ​ σ 111 ​ σ 120 i L 1 ​ ( σ 120) ​ i 3 ​ M 1 ( i) ​ ( 0) i! | μ ^ = μ ^ 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-1/i)\Delta_{10}({{\hat{\mu}}})=-\frac{\Delta_{00}\sigma_{111}\sigma_{120}^{i}}{L_{1}(\sigma_{120})i^{3}}\frac{M_{1}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

To prove ( b) (b) we fix μ ^ 0 = ( i, μ 0) ∈ D 01 0 × W {{\hat{\mu}}}_{0}=(i,\mu_{0})\in D_{01}^{0}\times W with i ∈ ℕ i\in\mathbb{N} and note that, by ( b) (b) in Theorem A, Δ 01 = − Δ 00 2 ​ S 2 \Delta_{01}=-\Delta_{00}^{2}S_{2} where S 2 = f 2 − σ 221 L 2 ​ ( σ 210) ​ M ^ 2 ​ ( λ, σ 210) S_{2}=f_{2}-{\frac{\sigma_{221}}{L_{2}(\sigma_{210})}}\hat{M}_{2}(\lambda,\sigma_{210}) with f 2 ∈ 𝒞 ∞ ​ ( W ^). f_{2}\in\mathscr{C}^{\infty}(\hat{W}). Exactly as before, ( c) (c) in Theorem B.1 implies that the function ( λ − i) ​ Δ 01 ​ ( μ ^) (\lambda-i)\Delta_{01}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and, moreover, that

 | lim μ ^ → μ ^ 0 ( λ − i) ​ S 2 = σ 221 L 2 ​ ( σ 210) | μ ^ = μ ^ 0 ​ lim μ ^ → μ ^ 0 ( i − λ) ​ M ^ 2 ​ ( λ, σ 210) = σ 221 L 2 ​ ( σ 210) ​ M 2 ( i) ​ ( 0) i! ​ σ 210 i | μ ^ = μ ^ 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-i)S_{2}=\frac{\sigma_{221}}{L_{2}(\sigma_{210})}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(i-\lambda)\hat{M}_{2}(\lambda,\sigma_{210})=\frac{\sigma_{221}}{L_{2}(\sigma_{210})}\frac{M_{2}^{(i)}(0)}{i!}\sigma_{210}^{i}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}} |  | (40) |

and, consequently, lim μ ^ → μ ^ 0 ( λ − i) ​ Δ 01 ​ ( μ ^) = − Δ 00 2 ​ σ 221 ​ σ 210 i L 2 ​ ( σ 210) ​ M 2 ( i) ​ ( 0) i! | μ ^ = μ ^ 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-i)\Delta_{01}({{\hat{\mu}}})=-\frac{\Delta_{00}^{2}\sigma_{221}\sigma_{210}^{i}}{L_{2}(\sigma_{210})}\frac{M_{2}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

Let us turn to the proof of ( c) (c). To this end we note that, by ( b) (b) in Theorem A, Δ 11 = − 2 ​ Δ 00 2 ​ λ ​ S 1 ​ S 2. \Delta_{11}=-2\Delta_{00}^{2}\lambda S_{1}S_{2}. If μ ^ 0 = ( 1 / i, μ ^ 0) ∈ D 11 0 × W {{\hat{\mu}}}_{0}=(1/i,{{\hat{\mu}}}_{0})\in D_{11}^{0}\times W with i ∈ ℕ ≥ 2 i\in\mathbb{N}_{\geq 2} then S 2 S_{2} is smooth at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} by ( a) (a) in Theorem B.1 and therefore from ( 39) (\ref{42eq1}\immediate) it follows that

 | lim μ ^ → μ ^ 0 ( λ − 1 / i) ​ Δ 11 ​ ( μ ^) = 2 ​ Δ 00 2 ​ σ 111 ​ σ 120 i L 1 ​ ( σ 120) ​ i 3 ​ M 1 ( i) ​ ( 0) i! ​ S 2 | μ ^ = μ ^ 0. \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-1/i)\Delta_{11}({{\hat{\mu}}})=\frac{2\Delta_{00}^{2}\sigma_{111}\sigma_{120}^{i}}{L_{1}(\sigma_{120})i^{3}}\frac{M_{1}^{(i)}(0)}{i!}S_{2}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

Exactly as before, the fact that ( λ − 1 / i) ​ Δ 11 ​ ( μ ^) (\lambda-1/i)\Delta_{11}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} follows by ( c) (c) in Theorem B.1. This shows the assertion in ( c ​ 1) (c1). Similarly if μ ^ 0 = ( i, μ ^ 0) ∈ D 11 0 × W {{\hat{\mu}}}_{0}=(i,{{\hat{\mu}}}_{0})\in D_{11}^{0}\times W with i ∈ ℕ ≥ 2 i\in\mathbb{N}_{\geq 2} then S 1 S_{1} is smooth at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} by ( a) (a) in Theorem B.1 and, from ( 40) (\ref{42eq2}\immediate),

 | lim μ ^ → μ ^ 0 ( λ − i) ​ Δ 11 ​ ( μ ^) = − 2 ​ i ​ Δ 00 2 ​ σ 221 ​ σ 210 i L 2 ​ ( σ 210) ​ M 2 ( i) ​ ( 0) i! ​ S 1 | μ ^ = μ ^ 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-i)\Delta_{11}({{\hat{\mu}}})=-\frac{2i\Delta_{00}^{2}\sigma_{221}\sigma_{210}^{i}}{L_{2}(\sigma_{210})}\frac{M_{2}^{(i)}(0)}{i!}S_{1}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}} |  |

which proves ( c ​ 2) (c2). Finally, if μ ^ 0 = ( 1, μ 0) {{\hat{\mu}}}_{0}=(1,\mu_{0}) with μ 0 ∈ W \mu_{0}\in W, the combination of ( 39) (\ref{42eq1}\hbox{}) and ( 40) (\ref{42eq2}\hbox{}) easily implies that

 | lim μ ^ → μ ^ 0 ( λ − 1) 2 ​ Δ 11 ​ ( μ ^) \displaystyle\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-1)^{2}\Delta_{11}({{\hat{\mu}}}) | = 2 ​ Δ 00 2 | μ ^ = μ ^ 0 ​ lim μ ^ → μ ^ 0 ( λ − 1) ​ S 1 ​ lim μ ^ → μ ^ 0 ( λ − 1) ​ S 2 \displaystyle=2\Delta_{00}^{2}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-1)S_{1}\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-1)S_{2} |  |

 |  | = 2 ​ Δ 00 2 ​ σ 111 ​ σ 120 ​ σ 221 ​ σ 210 L 1 ​ ( σ 120) ​ L 2 ​ ( σ 210) ​ M 1 ′ ​ ( 0) ​ M 2 ′ ​ ( 0) | μ ^ = μ ^ 0 \displaystyle=\frac{2\Delta_{00}^{2}\sigma_{111}\sigma_{120}\sigma_{221}\sigma_{210}}{L_{1}(\sigma_{120})L_{2}(\sigma_{210})}M_{1}^{\prime}(0)M_{2}^{\prime}(0)\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}} |  |

and, on the other hand, ( c) (c) in Theorem B.1 shows that ( λ − 1) 2 ​ Δ 11 ​ ( μ ^) (\lambda-1)^{2}\Delta_{11}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}. This proves the last assertion in ( c) (c) and concludes the proof of the result.

We omit the proof of the next result for the sake of brevity since it is very similar to the previous one. With regard to its statement we recall that D 0, n 2 n = ℕ ≥ n 1 n 2 D_{0,n_{2}}^{n}=\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}} and D n 1, 0 n = ⋃ i = 1 n 1 i ℕ ≥ n 2 D_{n_{1},0}^{n}=\bigcup_{i=1}^{n_{1}}\frac{i}{\mathbb{N}_{\geq n_{2}}} (see Remark 1).

###### Proposition 3.3.

? ⟨ \langle poles2 ⟩ \rangle?

The following assertions hold:

1. ( a) (a)

For any μ ^ 0 = ( λ 0, μ 0) ∈ D 0 ​ n 2 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{0n_{2}}^{n}\times W with n 2 > 0 n_{2}>0, the function μ ^ ↦ ( λ − λ 0) ​ T 0 ​ n 2 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{0n_{2}}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}, and if λ 0 = n 1 + i n 2 \lambda_{0}=\frac{n_{1}+i}{n_{2}} with i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0} then lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T 0 ​ n 2 ​ ( μ ^) = − Δ 00 n 2 n 2 ​ σ 210 n 1 + i ​ σ 221 n 2 L 2 n 2 ​ ( σ 210) ​ A 2 ( i) ​ ( 0) i! | μ ^ = μ ^ 0 \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{0n_{2}}({{\hat{\mu}}})=-\frac{\Delta_{00}^{n_{2}}}{n_{2}}\frac{\sigma_{210}^{n_{1}+i}\sigma_{221}^{n_{2}}}{L_{2}^{n_{2}}(\sigma_{210})}\frac{A_{2}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

2. ( b) (b)

For any μ ^ 0 = ( λ 0, μ 0) ∈ D n 1 ​ 0 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{n_{1}0}^{n}\times W with λ 0 ∉ n 1 ℕ ≥ n 2 \lambda_{0}\notin\frac{n_{1}}{\mathbb{N}_{\geq n_{2}}}, the function T n 1 ​ 0 ​ ( μ ^) T_{n_{1}0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0. {{\hat{\mu}}}={{\hat{\mu}}}_{0}. In the case that λ 0 = n 1 n 2 + i \lambda_{0}=\frac{n_{1}}{n_{2}+i} with i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0}, then the function μ ^ ↦ ( λ − λ 0) ​ T n 1 ​ 0 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{n_{1}0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T n 1 ​ 0 ​ ( μ ^) = − n 1 ( n 2 + i) 2 ​ σ 111 n 1 ​ σ 120 n 2 + i L 1 n 1 ​ ( σ 210) ​ A 1 ( i) ​ ( 0) i! | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{n_{1}0}({{\hat{\mu}}})=-\frac{n_{1}}{(n_{2}+i)^{2}}\frac{\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}+i}}{L_{1}^{n_{1}}(\sigma_{210})}\frac{A_{1}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

Let us recall in regard to the next statement that D 0, n 2 + 1 n = ℕ ≥ n 1 n 2 + 1 ∪ ℕ, D_{0,n_{2}+1}^{n}=\frac{\mathbb{N}_{\geq n_{1}}}{n_{2}+1}\cup\mathbb{N}, see Remark 1.

###### Proposition 3.4.

? ⟨ \langle poles3 ⟩ \rangle?

The following assertions hold:

1. ( a) (a)

For any μ ^ 0 = ( λ 0, μ 0) ∈ D 0, n 2 + 1 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{0,n_{2}+1}^{n}\times W with λ 0 ∈ ℕ ≥ n 1 n 2, \lambda_{0}\in\mathbb{N}_{\geq\frac{n_{1}}{n_{2}}}, the function μ ^ ↦ ( λ − λ 0) 2 ​ T 0, n 2 + 1 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{2}T_{0,n_{2}+1}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}, and if λ 0 = i ∈ ℕ ≥ n 1 n 2 \lambda_{0}=i\in\mathbb{N}_{\geq\frac{n_{1}}{n_{2}}} then

 | lim μ ^ → μ ^ 0 ( λ − λ 0) 2 ​ T 0, n 2 + 1 ​ ( μ ^) = n 2 ​ Δ 00 n 2 + 1 ​ σ 210 ( n 2 + 1) ​ i ​ σ 221 n 2 + 1 ( n 2 + 1) ​ L 2 n 2 + 1 ​ ( σ 210) ​ M 2 ( i) ​ ( 0) i! ​ A 2 ( n 2 ​ i − n 1) ​ ( 0) ( n 2 ​ i − n 1)! | μ ^ = μ ^ 0. \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})^{2}T_{0,n_{2}+1}({{\hat{\mu}}})=\frac{n_{2}\Delta_{00}^{n_{2}+1}\sigma_{210}^{(n_{2}+1)i}\sigma_{221}^{n_{2}+1}}{(n_{2}+1)L_{2}^{n_{2}+1}(\sigma_{210})}\frac{M_{2}^{(i)}(0)}{i!}\frac{A_{2}^{(n_{2}i-n_{1})}(0)}{(n_{2}i-n_{1})!}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

2. ( b) (b)

For any μ ^ 0 = ( λ 0, μ 0) ∈ D 0, n 2 + 1 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{0,n_{2}+1}^{n}\times W with λ 0 ∉ ℕ ≥ n 1 n 2, \lambda_{0}\notin\mathbb{N}_{\geq\frac{n_{1}}{n_{2}}}, the function μ ^ ↦ ( λ − λ 0) ​ T 0, n 2 + 1 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{0,n_{2}+1}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}, and

  1. ( b ​ 1) (b1)

if λ 0 = i ∈ ℕ < n 1 n 2 \lambda_{0}=i\in\mathbb{N}_{<\frac{n_{1}}{n_{2}}} then, setting i 1:= ( n 2 + 1) ​ i − n 1, i_{1}\!:=(n_{2}+1)i-n_{1},

 | lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T 0, n 2 + 1 ​ ( μ ^) \displaystyle\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{0,n_{2}+1}({{\hat{\mu}}}) | = − Δ 00 n 2 + 1 ​ σ 221 n 2 + 1 ​ σ 210 n 1 L 2 n 2 + 1 ​ ( σ 210) ​ ( n 2 ​ M 2 ( i) ​ ( 0) i! ​ σ 210 i ​ A ^ 2 ​ ( i ​ n 2 − n 1, σ 210) CLOSE \displaystyle=-\frac{\Delta_{00}^{n_{2}+1}\sigma_{221}^{n_{2}+1}\sigma_{210}^{n_{1}}}{L_{2}^{n_{2}+1}(\sigma_{210})}\Bigg(n_{2}\frac{M_{2}^{(i)}(0)}{i!}\sigma_{210}^{i}\hat{A}_{2}(in_{2}-n_{1},\sigma_{210}) |  |

 |  | + n 2 ​ σ 210 i 1 ( n 2 + 1) ​ i 0! ∑ j = 0 i 1 ( i 1 j) M 2 ( j) ​ ( 0) ​ A 2 ( i 1 − j) ​ ( 0) j − i + R) | μ ^ = μ ^ 0, \displaystyle\qquad\qquad+\frac{n_{2}\sigma_{210}^{i_{1}}}{(n_{2}+1)i_{0}!}\sum_{j=0}^{i_{1}}{i_{1}\choose j}\frac{M_{2}^{(j)}(0)A_{2}^{(i_{1}-j)}(0)}{j-i}+R\Bigg)\Bigg|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}, |  |

where R = σ 210 i 1 ( n 2 + 1) ​ i 1! ​ ∂ u i 1 ( L 2 n 2 + 1 ​ ( u) ​ ∂ 2 P 1 − 1 ​ ( u, 0)) | u = 0 R=\frac{\sigma_{210}^{i_{1}}}{(n_{2}+1)i_{1}!}\partial^{i_{1}}_{u}\left(L_{2}^{n_{2}+1}(u)\partial_{2}P_{1}^{-1}(u,0)\right)\big|_{u=0} for i 1 ⩾ 0 i_{1}\geqslant 0 and R = 0 R=0 otherwise,

  2. ( b ​ 2) (b2)

if λ 0 = n 1 + i n 2 + 1 ∉ ℕ \lambda_{0}=\frac{n_{1}+i}{n_{2}+1}\notin\mathbb{N} with i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0}, then lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T 0, n 2 + 1 ​ ( μ ^) = − Δ 00 n 2 + 1 ​ σ 221 n 2 + 1 ​ σ 210 n 1 + i ( n 2 + 1) ​ L 2 n 2 + 1 ​ ( σ 210) ​ B 2 ( i) ​ ( 0) i! | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{0,n_{2}+1}({{\hat{\mu}}})=-\frac{\Delta_{00}^{n_{2}+1}\sigma_{221}^{n_{2}+1}\sigma_{210}^{n_{1}+i}}{(n_{2}+1)L_{2}^{n_{2}+1}(\sigma_{210})}\frac{B_{2}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

For the sake of convenience we write T 0, n 2 + 1 T_{0,n_{2}+1}, see ( c) (c) in Theorem A, as

 | T 0, n 2 + 1 = f 0 ​ ( f 1 + f 2 ​ B ^ 2 ​ ( ( n 2 + 1) ​ λ − n 1, σ 210)) T_{0,n_{2}+1}=f_{0}\left(f_{1}+f_{2}\hat{B}_{2}((n_{2}+1)\lambda-n_{1},\sigma_{210})\right) |  | (41) |

with f 0:= Δ 00 n 2 + 1 ​ σ 210 n 1 ​ σ 221 n 2 f_{0}\!:=\Delta_{00}^{n_{2}+1}\sigma_{210}^{n_{1}}\sigma_{221}^{n_{2}}, f 1:= σ 211 σ 210 ​ P 1 ​ ( σ 210, 0) f_{1}\!:=\frac{\sigma_{211}}{\sigma_{210}P_{1}(\sigma_{210},0)}, f 2:= σ 221 L 2 n 2 + 1 ​ ( σ 221) f_{2}\!:=\frac{\sigma_{221}}{L_{2}^{n_{2}+1}(\sigma_{221})} and where, recall ( 2) (\ref{def_fun}\hbox{}),

 | B 2 ( u) = n 2 A 2 ( u) M ^ 2 ( λ, u) + f 3 ( u) with f 3 ​ ( u):= L 2 n 2 + 1 ​ ( u) ​ ∂ 2 P 1 − 1 ​ ( u, 0). B_{2}(u)=n_{2}A_{2}(u)\hat{M}_{2}(\lambda,u)+f_{3}(u)\text{ with $f_{3}(u)\!:=L_{2}^{n_{2}+1}(u)\partial_{2}P_{1}^{-1}(u,0)$.} |  |

That being said we begin with the proof of ( b ​ 2) (b2). With this aim we note first that B 2 ​ ( u, λ, μ) B_{2}(u;\lambda,\mu) is smooth along λ = λ 0 ∉ ℤ ≥ 0 \lambda=\lambda_{0}\notin\mathbb{Z}_{\geq 0} because so is M ^ 2 ​ ( λ, u, μ ^) \hat{M}_{2}(\lambda,u;{{\hat{\mu}}}) by ( a) (a) in Theorem B.1. For this reason, since n 1 + i n 2 + 1 ∉ ℤ ≥ 0 \frac{n_{1}+i}{n_{2}+1}\notin\mathbb{Z}_{\geq 0} by assumption, we can apply Corollary B.4 taking α = λ, \alpha=\lambda, ν = ( λ, μ) \nu=(\lambda,\mu), α 0 = n 1 + i n 2 + 1 \alpha_{0}=\frac{n_{1}+i}{n_{2}+1}, ν 0 = ( n 1 + i n 2 + 1, μ 0) \nu_{0}=(\frac{n_{1}+i}{n_{2}+1},\mu_{0}), κ 1 = n 2 + 1 \kappa_{1}=n_{2}+1 and κ 2 = − n 1 \kappa_{2}=-n_{1} to conclude that

 | lim μ ^ → μ ^ 0 ( n 1 + i n 2 + 1 − λ) ​ B ^ 2 ​ ( ( n 2 + 1) ​ λ − n 1, σ 210) = B 2 ( i) ​ ( 0) ( n 2 + 1) ​ i! ​ σ 210 i | μ ^ = μ ^ 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}\left(\frac{n_{1}+i}{n_{2}+1}-\lambda\right)\hat{B}_{2}\big((n_{2}+1)\lambda-n_{1},\sigma_{210}\big)=\frac{B_{2}^{(i)}(0)}{(n_{2}+1)i!}\sigma_{210}^{i}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}} |  |

Hence, on account of ( 41) (\ref{44eq1}\immediate) and by applying Corollary B.4, the function μ ^ ↦ ( λ − n 1 + i n 2 + 1) ​ T 0, n 2 + 1 ​ ( μ ^) {{\hat{\mu}}}\mapsto\big(\lambda-\frac{n_{1}+i}{n_{2}+1}\big)T_{0,n_{2}+1}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and tends to − Δ 00 n 2 + 1 ​ σ 221 n 2 + 1 ​ σ 210 n 1 + i ( n 2 + 1) ​ L 2 n 2 + 1 ​ ( σ 210) ​ B 2 ( i) ​ ( 0) i! | μ ^ = μ ^ 0 -\frac{\Delta_{00}^{n_{2}+1}\sigma_{221}^{n_{2}+1}\sigma_{210}^{n_{1}+i}}{(n_{2}+1)L_{2}^{n_{2}+1}(\sigma_{210})}\frac{B_{2}^{(i)}(0)}{i!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}} as μ ^ → μ ^ 0 {{\hat{\mu}}}\to{{\hat{\mu}}}_{0} and this shows ( b ​ 2) (b2).

Let us turn now to the proof of assertion ( a) (a). So assume that λ 0 = i ∈ ℕ \lambda_{0}=i\in\mathbb{N} with n 2 ​ i − n 1 ⩾ 0 n_{2}i-n_{1}\geqslant 0 and observe that, by Corollary B.4, the function μ ^ ↦ ( λ − i) 2 ​ f ^ 3 ​ ( ( n 2 + 1) ​ λ − n 1, σ 210) {{\hat{\mu}}}\mapsto(\lambda-i)^{2}\hat{f}_{3}((n_{2}+1)\lambda-n_{1},\sigma_{210}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and tends to 0 as μ ^ → μ ^ 0. {{\hat{\mu}}}\to{{\hat{\mu}}}_{0}. Thus, by applying firstly ( a) (a) in Corollary B.3 and secondly ( a) (a) in Lemma B.5 with { α = λ, ν = ( λ, μ), p = n 1, q = n 2 } \{\alpha=\lambda,\nu=(\lambda,\mu),p=n_{1},q=n_{2}\}, from ( 41) (\ref{44eq1}\hbox{}) we can assert that μ ^ ↦ ( λ − i) 2 ​ T 0, n 2 + 1 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-i)^{2}T_{0,n_{2}+1}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and, moreover,

 | lim μ ^ → μ ^ 0 ( λ − i) 2 ​ T 0, n 2 + 1 ​ ( μ ^) = n 2 ​ f 0 ​ f 2 | μ ^ = μ ^ 0 ​ σ 210 n 2 ​ i − n 1 n 2 + 1 ​ M 2 ( i) ​ ( 0) i! ​ A 2 ( n 2 ​ i − n 1) ​ ( 0) ( n 2 ​ i − n 1)! | μ ^ = μ ^ 0, \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-i)^{2}T_{0,n_{2}+1}({{\hat{\mu}}})=n_{2}f_{0}f_{2}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}\frac{\sigma_{210}^{n_{2}i-n_{1}}}{n_{2}+1}\frac{M_{2}^{(i)}(0)}{i!}\frac{A_{2}^{(n_{2}i-n_{1})}(0)}{(n_{2}i-n_{1})!}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}, |  |

which proves ( a) (a). In order to show ( b ​ 1) (b1) we consider λ 0 = i ∈ ℕ \lambda_{0}=i\in\mathbb{N} with n 2 ​ i − n 1 < 0. n_{2}i-n_{1}<0. In this case, if i 1:= ( n 2 + 1) ​ i − n 1 ⩾ 0 i_{1}\!:=(n_{2}+1)i-n_{1}\geqslant 0 then lim μ ^ → μ ^ 0 ( λ − i) ​ f ^ 3 ​ ( ( n 2 + 1) ​ λ − n 1, σ 210) = − σ 210 i 1 n 2 + 1 ​ f 3 ( i 1) ​ ( 0) i 1! | μ ^ = μ ^ 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-i)\hat{f}_{3}((n_{2}+1)\lambda-n_{1},\sigma_{210})=\frac{-\sigma_{210}^{i_{1}}}{n_{2}+1}\frac{f_{3}^{(i_{1})}(0)}{i_{1}!}\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}} by Corollary B.4, whereas if i 1 < 0 i_{1}<0 then lim μ ^ → μ ^ 0 ( λ − i) ​ f ^ 3 ​ ( ( n 2 + 1) ​ λ − n 1, σ 210) = 0 \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-i)\hat{f}_{3}((n_{2}+1)\lambda-n_{1},\sigma_{210})=0 by ( a) (a) in Theorem B.1. Taking this into account the assertion in ( b ​ 1) (b1) follows by applying firstly ( a) (a) in Corollary B.3 and secondly ( b) (b) in Lemma B.5 with { α = λ, ν = ( λ, μ), p = n 1, q = n 2 } \{\alpha=\lambda,\nu=(\lambda,\mu),p=n_{1},q=n_{2}\}. This concludes the proof of the result.

Regarding the next statement let us recall, see Remark 1, that D n 1 + 1, 0 n = ⋃ i = 1 n 1 + 1 i ℕ ≥ n 2 D_{n_{1}+1,0}^{n}=\bigcup_{i=1}^{n_{1}+1}\frac{i}{\mathbb{N}_{\geq n_{2}}}.

###### Proposition 3.5.

? ⟨ \langle poles4 ⟩ \rangle?

Let us consider any μ ^ 0 = ( λ 0, μ 0) ∈ D n 1 + 1, 0 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{n_{1}+1,0}^{n}\times W. Then the following assertions hold:

1. ( a) (a)

Case λ 0 ∈ 1 ℕ. \lambda_{0}\in\frac{1}{\mathbb{N}}.

  1. ( a ​ 1) (a1)

If λ 0 = 1 i \lambda_{0}=\frac{1}{i} with i ∈ ℕ ≥ n 2 n 1 i\in\mathbb{N}_{\geq\frac{n_{2}}{n_{1}}} then the function μ ^ ↦ ( λ − λ 0) 2 ​ T n 1 + 1, 0 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{2}T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and

 | lim μ ^ → μ ^ 0 ( λ − λ 0) 2 ​ T n 1 + 1, 0 ​ ( μ ^) = − σ 111 n 1 + 1 ​ σ 120 ( n 1 + 1) ​ i ( n 1 + 1) ​ i 2 ​ L 1 n 1 + 1 ​ ( σ 120) ​ M 1 ( i) ​ ( 0) i! ​ A 1 ( n 1 ​ i − n 2) ​ ( 0) ( n 1 ​ i − n 2)! | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})^{2}T_{n_{1}+1,0}({{\hat{\mu}}})=-\frac{\sigma_{111}^{n_{1}+1}\sigma_{120}^{(n_{1}+1)i}}{(n_{1}+1)i^{2}L_{1}^{n_{1}+1}(\sigma_{120})}\frac{M_{1}^{(i)}(0)}{i!}\frac{A_{1}^{(n_{1}i-n_{2})}(0)}{(n_{1}i-n_{2})!}\Bigg|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

  2. ( a ​ 2) (a2)

If λ 0 = 1 i \lambda_{0}=\frac{1}{i} with i ∈ ℕ ∩ [n 2 n 1 + 1, n 2 n 1) i\in\mathbb{N}\cap[\frac{n_{2}}{n_{1}+1},\frac{n_{2}}{n_{1}}) then the function μ ^ ↦ ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and, setting i 0 = ( n 1 + 1) ​ i − n 2, i_{0}=(n_{1}+1)i-n_{2},

 | lim μ ^ → μ ^ 0 ( λ − λ 0) T n 1 + 1, 0 ( μ ^) = − \displaystyle\lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}})=- | σ 111 n 1 + 1 ​ σ 120 i ⁡ ( n 1 + 1) ( n 1 + 1) ​ i 2 ​ i 0! ​ L 1 n 1 + 1 ​ ( σ 120) ​ ( n 1 ​ ∑ j = 0 i 0 ( i 0 j) ​ M 1 ( j) ​ ( 0) ​ A 1 ( i 0 − j) ​ ( 0) j − i CLOSE \displaystyle\frac{\sigma_{111}^{n_{1}+1}\sigma_{120}^{i(n_{1}+1)}}{(n_{1}+1)i^{2}i_{0}!L_{1}^{n_{1}+1}(\sigma_{120})}\Bigg(n_{1}\sum_{j=0}^{i_{0}}{i_{0}\choose j}\frac{M_{1}^{(j)}(0)A_{1}^{(i_{0}-j)}(0)}{j-i} |  |

 |  | + ∂ u i 0 ( L 1 n 1 + 1 ( u) ∂ 1 P 2 − 1 ( u, 0)) | u = 0) | μ ^ = μ ^ 0. \displaystyle\qquad\qquad+\partial_{u}^{i_{0}}\left(L_{1}^{n_{1}+1}(u)\partial_{1}P_{2}^{-1}(u,0)\right)\big|_{u=0}\Bigg)\Bigg|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

  3. ( a ​ 3) (a3)

If λ 0 = 1 i \lambda_{0}=\frac{1}{i} with i ∈ ℕ < n 2 n 1 + 1 i\in\mathbb{N}_{<\frac{n_{2}}{n_{1}+1}} then T n 1 + 1, 0 ​ ( μ ^) T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} to { λ 0 } × W \{\lambda_{0}\}\times W.

2. ( b) (b)

Case λ 0 ∈ ( n 1 ℕ ≥ n 2 ∪ n 1 + 1 ℕ ≥ n 2) ∖ 1 ℕ \lambda_{0}\in\left(\frac{n_{1}}{\mathbb{N}_{\geq n_{2}}}\cup\frac{n_{1}+1}{\mathbb{N}_{\geq n_{2}}}\right)\setminus\frac{1}{\mathbb{N}}.

  1. ( b ​ 1) (b1)

If λ 0 = n 1 n 2 + i ∉ n 1 + 1 ℕ ≥ n 2 \lambda_{0}=\frac{n_{1}}{n_{2}+i}\notin\frac{n_{1}+1}{\mathbb{N}_{\geq n_{2}}} with i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0} then the function μ ^ ↦ ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) = − n 1 ​ λ 0 ​ σ 111 n 1 ​ σ 120 n 2 + i ( n 2 + i) ​ L 1 n 1 ​ ( σ 120) ​ A 1 ( i) ​ ( 0) i! ​ S 1 | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}})=-\frac{n_{1}\lambda_{0}\sigma_{111}^{n_{1}}\sigma_{120}^{n_{2}+i}}{(n_{2}+i)L_{1}^{n_{1}}(\sigma_{120})}\frac{A_{1}^{(i)}(0)}{i!}S_{1}\Big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}.

  2. ( b ​ 2) (b2)

If λ 0 = n 1 + 1 n 2 + i ∉ n 1 ℕ ≥ n 2 \lambda_{0}=\frac{n_{1}+1}{n_{2}+i}\notin\frac{n_{1}}{\mathbb{N}_{\geq n_{2}}} with i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0} then μ ^ ↦ ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and

 | lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) = n 1 ​ λ 0 ​ σ 111 n 1 + 1 ​ σ 120 n 2 + i ( n 2 + i) ​ L 1 n 1 + 1 ​ ( σ 120) ​ ( A 1 ​ M ^ 1 ​ ( 1 λ 0, ⋅)) ( i) ​ ( 0) i! | μ ^ = μ ^ 0. \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}})=\frac{n_{1}\lambda_{0}\sigma_{111}^{n_{1}+1}\sigma_{120}^{n_{2}+i}}{(n_{2}+i)L_{1}^{n_{1}+1}(\sigma_{120})}\frac{(A_{1}\hat{M}_{1}(\frac{1}{\lambda_{0}},\cdot))^{(i)}(0)}{i!}\Bigg|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

  3. ( b ​ 3) (b3)

If λ 0 = n 1 n 2 + i 1 = n 1 + 1 n 2 + i 2 \lambda_{0}=\frac{n_{1}}{n_{2}+i_{1}}=\frac{n_{1}+1}{n_{2}+i_{2}} for some i 1, i 2 ∈ ℤ ≥ 0 i_{1},i_{2}\in\mathbb{Z}_{\geq 0} then the function μ ^ ↦ ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0} and

 | lim μ ^ → μ ^ 0 ( λ − λ 0) ​ T n 1 + 1, 0 ​ ( μ ^) = n 1 ​ λ 0 ​ σ 111 n 1 L 1 n 1 ​ ( σ 120) ​ ( − σ 120 n 2 + i 1 n 2 + i 1 ​ A 1 ( i 1) ​ ( 0) i 1! ​ S 1 + σ 120 n 2 + i 2 n 2 + i 2 ​ ( A 1 ​ M ^ 1 ​ ( 1 λ 0, ⋅)) ( i 2) ​ ( 0) i 2!) | μ ^ = μ ^ 0. \lim_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(\lambda-\lambda_{0})T_{n_{1}+1,0}({{\hat{\mu}}})=\frac{n_{1}\lambda_{0}\sigma_{111}^{n_{1}}}{L_{1}^{n_{1}}(\sigma_{120})}\left(-\frac{\sigma_{120}^{n_{2}+i_{1}}}{n_{2}+i_{1}}\frac{A_{1}^{(i_{1})}(0)}{i_{1}!}S_{1}+\frac{\sigma_{120}^{n_{2}+i_{2}}}{n_{2}+i_{2}}\frac{(A_{1}\hat{M}_{1}(\frac{1}{\lambda_{0}},\cdot))^{(i_{2})}(0)}{i_{2}!}\right)\Bigg|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

3. ( c) (c)

Finally, if λ 0 ∉ 1 ℕ ∪ n 1 ℕ ≥ n 2 ∪ n 1 + 1 ℕ ≥ n 2 \lambda_{0}\notin\frac{1}{\mathbb{N}}\cup\frac{n_{1}}{\mathbb{N}_{\geq n_{2}}}\cup\frac{n_{1}+1}{\mathbb{N}_{\geq n_{2}}} then T n 1 + 1, 0 ​ ( μ ^) T_{n_{1}+1,0}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ = μ ^ 0 {{\hat{\mu}}}={{\hat{\mu}}}_{0}.

For the sake of brevity we omit the proof of Proposition 3.5. Let us only mention for reader’s convenience that, by ( c) (c) in Theorem A,

 | T n 1 + 1, 0 = f 0 ​ ( f 1 + f 2 ​ B ^ 1 ​ ( ( n 1 + 1) / λ − n 2, σ 120) + f 3 ​ S 1 ​ A ^ 1 ​ ( n 1 / λ − n 2, σ 120)) T_{n_{1}+1,0}=f_{0}\left(f_{1}+f_{2}\hat{B}_{1}((n_{1}+1)/\lambda-n_{2},\sigma_{120})+f_{3}S_{1}\hat{A}_{1}(n_{1}/\lambda-n_{2},\sigma_{120})\right) |  |

with f i ∈ 𝒞 ∞ ​ ( W ^). f_{i}\in\mathscr{C}^{\infty}(\hat{W}). This expression is similar to the one in ( 41) (\ref{44eq1}\hbox{}) for T 0, n 2 + 1 T_{0,n_{2}+1} that we analysed in the proof of Proposition 3.4, but with the additional summand f 3 ​ S 1 ​ A ^ 1 f_{3}S_{1}\hat{A}_{1}. This extra term increases the number of cases to be studied in terms of λ 0 \lambda_{0} but they follow using exactly the same arguments as those explained in the proofs of Propositions 3.2 and 3.4.

Lastly we state a result concerning the poles of the coefficients T 20 T_{20} and T 02 T_{02} in the cases n 1 = 0 n_{1}=0 and n 2 = 0 n_{2}=0, respectively. For the sake of shortness we do not specify the value of the residues, which can be computed using the same techniques as in the previous results. For the same reason we neither include the proof. With regard to its statement let us recall that D 20 n = 2 ℕ ≥ n 2 D_{20}^{n}=\frac{2}{\mathbb{N}_{\geq n_{2}}} and D 02 n = ℕ 2 D_{02}^{n}=\frac{\mathbb{N}}{2}, see Remark 1.

###### Proposition 3.6.

? ⟨ \langle poles5 ⟩ \rangle?

The following assertions hold:

1. ( a) (a)

Assume that n 1 = 0 n_{1}=0 and consider any μ ^ 0 = ( λ 0, μ 0) ∈ D 20 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{20}^{n}\times W.

  1. ( a ​ 1) (a1)

If λ 0 ∈ 1 ℕ ≥ n 2 \lambda_{0}\in\frac{1}{\mathbb{N}_{\geq n_{2}}} then the function μ ^ ↦ ( λ − λ 0) 2 ​ T 20 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{2}T_{20}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ 0 {{\hat{\mu}}}_{0}.

  2. ( a ​ 2) (a2)

If λ 0 ∉ 1 ℕ ≥ n 2 \lambda_{0}\notin\frac{1}{\mathbb{N}_{\geq n_{2}}} then the function μ ^ ↦ ( λ − λ 0) ​ T 20 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{20}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ 0 {{\hat{\mu}}}_{0}.

2. ( b) (b)

Assume that n 2 = 0 n_{2}=0 and consider any μ ^ 0 = ( λ 0, μ 0) ∈ D 02 n × W {{\hat{\mu}}}_{0}=(\lambda_{0},\mu_{0})\in D_{02}^{n}\times W.

  1. ( b ​ 1) (b1)

If λ 0 ∈ ℕ ≥ n 1 \lambda_{0}\in\mathbb{N}_{\geq n_{1}} then the function μ ^ ↦ ( λ − λ 0) 2 ​ T 02 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})^{2}T_{02}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ 0 {{\hat{\mu}}}_{0}.

  2. ( b ​ 2) (b2)

If λ 0 ∈ ℕ < n 1 ∪ ( ℕ ≥ n 1 2 ∖ ℕ) \lambda_{0}\in\mathbb{N}_{<n_{1}}\cup\left(\frac{\mathbb{N}_{\geq n_{1}}}{2}\setminus\mathbb{N}\right) then the function μ ^ ↦ ( λ − λ 0) ​ T 02 ​ ( μ ^) {{\hat{\mu}}}\mapsto(\lambda-\lambda_{0})T_{02}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ 0 {{\hat{\mu}}}_{0}.

  3. ( b ​ 3) (b3)

If λ 0 ∈ ℕ < n 1 2 ∖ ℕ \lambda_{0}\in\frac{\mathbb{N}_{<n_{1}}}{2}\setminus\mathbb{N} then T 0 ​ n 2 ​ ( μ ^) T_{0n_{2}}({{\hat{\mu}}}) extends 𝒞 ∞ \mathscr{C}^{\infty} at μ ^ 0 {{\hat{\mu}}}_{0}.

We are now in position to conclude the proof of Corollary B.

In the analytic setting (see Remark 1) we know by Proposition 2.9 that the coefficients Δ i ​ j \Delta_{ij} and T i ​ j T_{ij} listed in Theorem A are analytic on ( ( 0, + ∞) ∖ D i ​ j 0) × W ((0,+\infty)\setminus D_{ij}^{0})\times W and ( ( 0, + ∞) ∖ D i ​ j 0) × W ((0,+\infty)\setminus D_{ij}^{0})\times W, respectively. The fact that each Δ i ​ j \Delta_{ij} is meromorphic on W ^ = ( 0, + ∞) × W \hat{W}=(0,+\infty)\times W with poles of order at most two along D i ​ j 0 × W D_{ij}^{0}\times W follows by realising that in the analytic setting the statement of Proposition 3.2 is true replacing 𝒞 ∞ \mathscr{C}^{\infty} by 𝒞 ω, \mathscr{C}^{\omega}, i.e., that the extensions are analytic. Indeed, the proof of this analytic version is literally the same but appealing to the analytic assertions in Theorem B.1 instead of the smooth counterparts. More specifically, using ( d) (d) in the place of ( a) (a) and ( c). (c). Similarly, the fact that each T i ​ j T_{ij} is meromorphic on W ^ = ( 0, + ∞) × W \hat{W}=(0,+\infty)\times W with poles of order at most two along D i ​ j n × W D_{ij}^{n}\times W follows by noting that in the analytic setting the statements of Propositions 3.3, 3.4, 3.5 and 3.6 are true replacing 𝒞 ∞ \mathscr{C}^{\infty} by 𝒞 ω. \mathscr{C}^{\omega}. In this case, besides appealing to ( d) (d) in Theorem B.1 in the place of ( a) (a) and ( c) (c), we apply the analytic versions of Corollary B.4 and Lemma B.5, i.e., taking ϖ = ω \varpi=\omega instead of ϖ = ∞ \varpi=\infty. This completes the proof of the result.

## 4 First monomials in the asymptotic expansions

Theorem A is the main result of the present paper and it is intended to be applied in combination with Theorem 1.6 (which in fact gathers our main results in [23]). Because of this, in order to ease the applicability, we next particularise Theorem 1.6 to specify the first monomials appearing in the asymptotic expansion of the Dulac map, see Theorem 4.1, and the Dulac time, see Theorem 4.3, for arbitrary hyperbolicity ratio λ 0 \lambda_{0}. In both statements, the order L L ranges in a certain interval depending on λ 0. \lambda_{0}. The left endpoint of this interval is only given for completeness to guarantee that none of the monomials in the principal part can be included in the remainder.

###### Theorem 4.1.

? ⟨ \langle 3punts ⟩ \rangle?

Let D ⁡ ( s, μ ^) D(s;{{\hat{\mu}}}) be the Dulac map of the hyperbolic saddle ( 1) (\ref{X}\hbox{}) from Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2}.

1. ( 1) (1)

If λ 0 < 1 \lambda_{0}<1 then D ⁡ ( s, μ ^) = Δ 00 ​ ( μ ^) ​ s λ + Δ 01 ​ ( μ ^) ​ s 2 ​ λ + ℱ L ∞ ​ ( { λ 0 } × W) D(s;{{\hat{\mu}}})=\Delta_{00}({{\hat{\mu}}})s^{\lambda}+\Delta_{01}({{\hat{\mu}}})s^{2\lambda}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2 ​ λ 0, min ⁡ ( 3 ​ λ 0, 1 + λ 0)) L\in\big[2\lambda_{0},\min(3\lambda_{0},1+\lambda_{0})\big).

2. ( 2) (2)

If λ 0 = 1 \lambda_{0}=1 then D ⁡ ( s, μ ^) = Δ 00 ​ ( μ ^) ​ s λ + 𝚫 10 λ 0 ​ ( ω, μ ^) ​ s 1 + λ + ℱ L ∞ ​ ( { λ 0 } × W) D(s;{{\hat{\mu}}})=\Delta_{00}({{\hat{\mu}}})s^{\lambda}+\boldsymbol{\Delta}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})s^{1+\lambda}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2, 3), L\in[2,3), where

 | 𝚫 10 λ 0 ​ ( ω, μ ^) = Δ 10 ​ ( μ ^) + Δ 01 ​ ( μ ^) ​ ( 1 + α ​ ω), \boldsymbol{\Delta}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\Delta_{10}({{\hat{\mu}}})+\Delta_{01}({{\hat{\mu}}})(1+\alpha\omega), |  |

α = 1 − λ \alpha=1-\lambda and ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha).

3. ( 3) (3)

If λ 0 > 1 \lambda_{0}>1 then D ⁡ ( s, μ ^) = Δ 00 ​ ( μ ^) ​ s λ + Δ 10 ​ ( μ ^) ​ s λ + 1 + ℱ L ∞ ​ ( { λ 0 } × W) D(s;{{\hat{\mu}}})=\Delta_{00}({{\hat{\mu}}})s^{\lambda}+\Delta_{10}({{\hat{\mu}}})s^{\lambda+1}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [λ 0 + 1, min ( 2 + λ 0, 2 λ 0)) L\in\big[\lambda_{0}+1,\min(2+\lambda_{0},2\lambda_{0})\big).

1. (1)

We begin by showing that the assumptions on λ 0 \lambda_{0} and L L imply ℬ λ 0, L − λ 0 0 = { ( 0, 0), ( 0, 1) } \mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}}=\{(0,0),(0,1)\}. Let us prove first that L < min ⁡ ( 3 ​ λ 0, 1 + λ 0) L<\min(3\lambda_{0},1+\lambda_{0}) implies ℬ λ 0, L − λ 0 0 ⊂ { ( 0, 0), ( 0, 1) } \mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}}\subset\{(0,0),(0,1)\}. Indeed, we claim that if ( i, j) ∈ Λ 0 ∖ { ( 0, 0), ( 0, 1) } (i,j)\in\Lambda_{0}\setminus\{(0,0),(0,1)\} then ( i, j) ∉ ℬ λ 0, L − λ 0 0 (i,j)\notin\mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}}, i.e., i + λ 0 ​ j > L − λ 0. i+\lambda_{0}j>L-\lambda_{0}. It is clear that the claim will follow once we prove its validity for ( i, j) = ( 0, 2) (i,j)=(0,2) and ( i, j) = ( 1, 0). (i,j)=(1,0). For the first case observe that 2 ​ λ 0 > L − λ 0 2\lambda_{0}>L-\lambda_{0} holds because L < 3 ​ λ 0 L<3\lambda_{0} and, for the second one, 1 > L − λ 0 1>L-\lambda_{0} holds due to L < 1 + λ 0 L<1+\lambda_{0}. One can verify similarly that the reverse inclusion ℬ λ 0, L − λ 0 0 ⊃ { ( 0, 0), ( 0, 1) } \mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}}\supset\{(0,0),(0,1)\} is guaranteed by 2 ​ λ 0 ⩽ L. 2\lambda_{0}\leqslant L.

Let us show next that λ 0 < 1 \lambda_{0}<1 implies λ 0 ∉ D L − λ 0 0 \lambda_{0}\notin D^{0}_{L-\lambda_{0}}. To prove this we use firstly that D 00 0 ∪ D 01 0 = ℕ D_{00}^{0}\cup D_{01}^{0}=\mathbb{N} by Remark 1, so that λ 0 ∉ D 00 0 ∪ D 01 0. \lambda_{0}\notin D_{00}^{0}\cup D_{01}^{0}. Secondly, see Definition 1, we use that λ 0 ∈ D L − λ 0 0 \lambda_{0}\in D^{0}_{L-\lambda_{0}} if and only if there exists ( i, j) ∈ ℬ λ 0, L − λ 0 0 (i,j)\in\mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}} such that λ 0 ∈ D i ​ j 0 \lambda_{0}\in D_{ij}^{0}, which is not possible since ℬ λ 0, L − λ 0 0 = { ( 0, 0), ( 0, 1) } \mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}}=\{(0,0),(0,1)\} and λ 0 ∉ D 00 0 ∪ D 01 0. \lambda_{0}\notin D_{00}^{0}\cup D_{01}^{0}. Hence λ 0 ∉ D L − λ 0 0 \lambda_{0}\notin D^{0}_{L-\lambda_{0}} and the asymptotic expansion follows by ( a ​ 1) (a1) in Theorem 1.6.

2. (2)

Exactly as we did in the previous case, λ 0 = 1 \lambda_{0}=1 and L ∈ [2, 3) L\in[2,3) yields ℬ λ 0, L − λ 0 0 = { ( 0, 0), ( 1, 0), ( 0, 1) } \mathscr{B}_{\lambda_{0},L-\lambda_{0}}^{0}=\{(0,0),(1,0),(0,1)\}. This implies, due to λ 0 = 1 ∈ D 10 0 = ℕ \lambda_{0}=1\in D_{10}^{0}=\mathbb{N} by Remark 1, that λ 0 ∈ D L − λ 0 0 \lambda_{0}\in D_{L-\lambda_{0}}^{0}. Then, by ( a ​ 2) (a2) in Theorem 1.6,

 | D ⁡ ( s, μ ^) = Δ 00 ​ ( μ ^) ​ s λ + 𝚫 10 λ 0 ​ ( ω, μ ^) ​ s 1 + λ + ℱ L ∞ ​ ( { λ 0 } × W) D(s;{{\hat{\mu}}})=\Delta_{00}({{\hat{\mu}}})s^{\lambda}+\boldsymbol{\Delta}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})s^{1+\lambda}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) |  |

with ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha), α = 1 − λ \alpha=1-\lambda and 𝚫 10 λ 0 ​ ( ω, μ ^) = ∑ r = 0 1 Δ 1 − r ​ p, 0 + r ​ q ​ ( μ ^) ​ ( 1 + α ​ ω) r = Δ 10 ​ ( μ ^) + Δ 01 ​ ( μ ^) ​ ( 1 + α ​ ω) \boldsymbol{\Delta}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\sum_{r=0}^{1}\Delta_{1-rp,0+rq}({{\hat{\mu}}})(1+\alpha\omega)^{r}=\Delta_{10}({{\hat{\mu}}})+\Delta_{01}({{\hat{\mu}}})(1+\alpha\omega) because, see Definition 1, 𝒜 01 ​ λ 0 0 = { 0, 1 } \mathscr{A}_{01\lambda_{0}}^{0}=\{0,1\}, 𝒜 10 ​ λ 0 0 = ∅ \mathscr{A}_{10\lambda_{0}}^{0}=\emptyset and 𝒜 00 ​ λ 0 0 = { 0 } \mathscr{A}_{00\lambda_{0}}^{0}=\{0\}.

3. (3)

Similarly as we argue in ( 1) (1), in this case the assumptions on λ 0 \lambda_{0} and L L imply ℬ λ 0, L − λ 0 0 = { ( 0, 0), ( 1, 0) } \mathscr{B}^{0}_{\lambda_{0},L-\lambda_{0}}=\{(0,0),(1,0)\}. Then, since D 00 0 ∪ D 10 0 = 1 ℕ D_{00}^{0}\cup D_{10}^{0}=\frac{1}{\mathbb{N}} and λ 0 > 1 \lambda_{0}>1, it turns out that λ 0 ∉ D L − λ 0 0 \lambda_{0}\notin D_{L-\lambda_{0}}^{0} and thus the asymptotic expansion in the statement follows by ( a ​ 1) (a1) of Theorem 1.6.

This proves the validity of the result.

? ⟨ \langle ex1 ⟩ \rangle?

By Theorem 4.1, if λ 0 = 1 \lambda_{0}=1 then D ⁡ ( s, μ ^) = Δ 00 ​ ( μ ^) ​ s λ + 𝚫 10 λ 0 ​ ( ω, μ ^) ​ s 1 + λ + ℱ L ∞ ​ ( { λ 0 } × W) D(s;{{\hat{\mu}}})=\Delta_{00}({{\hat{\mu}}})s^{\lambda}+\boldsymbol{\Delta}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})s^{1+\lambda}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2, 3), L\in[2,3), where

 | 𝚫 10 λ 0 ​ ( ω, μ ^) = Δ 10 ​ ( μ ^) + Δ 01 ​ ( μ ^) ​ ( 1 + α ​ ω), \boldsymbol{\Delta}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\Delta_{10}({{\hat{\mu}}})+\Delta_{01}({{\hat{\mu}}})(1+\alpha\omega), |  |

α = 1 − λ \alpha=1-\lambda and ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha). The order of monomials in the principal part as s → 0 + s\to 0^{+} is s λ ≺ λ 0 s 1 + λ ω ≺ λ 0 s 1 + λ s^{\lambda}\prec_{\lambda_{0}}s^{1+\lambda}\omega\prec_{\lambda_{0}}s^{1+\lambda}, see [23, Definition 1.7] for details. The coefficient of s λ s^{\lambda} at μ ^ 0 = ( 1, μ 0) {{\hat{\mu}}}_{0}=(1,\mu_{0}) follows directly by evaluating the expression of Δ 00 \Delta_{00} given in assertion ( b) (b) of Theorem A. The subsequent coefficient is the one of s 1 + λ ​ ω s^{1+\lambda}\omega and, by applying ( b) (b) in Proposition 3.2 with i = 1, i=1, its expression at μ ^ 0 = ( 1, μ 0) {{\hat{\mu}}}_{0}=(1,\mu_{0}) is equal to

 | lim μ ^ → μ ^ 0 ( 1 − λ) ​ Δ 01 ​ ( μ ^) = Δ 00 2 ​ σ 221 ​ σ 210 L 2 ​ ( σ 210) ​ M 2 ′ ​ ( 0) | μ ^ = μ ^ 0. \lim\limits_{{{\hat{\mu}}}\to{{\hat{\mu}}}_{0}}(1-\lambda)\Delta_{01}({{\hat{\mu}}})=\frac{\Delta_{00}^{2}\sigma_{221}\sigma_{210}}{L_{2}(\sigma_{210})}M_{2}^{\prime}(0)\big|_{{{\hat{\mu}}}={{\hat{\mu}}}_{0}}. |  |

Moreover some easy computations on account of the definitions given in ( 2) (\ref{def_fun}\hbox{}) show that

 | M 2 ′ ​ ( 0) = ∂ 1 ( P 2 P 1) ​ ( 0, 0) ​ ∂ 2 ( P 2 P 1) ​ ( 0, 0) + ∂ 12 ( P 2 P 1) ​ ( 0, 0). M_{2}^{\prime}(0)=\partial_{1}\!\left(\frac{P_{2}}{P_{1}}\right)\!(0,0)\partial_{2}\!\left(\frac{P_{2}}{P_{1}}\right)\!(0,0)+\partial_{12}\!\left(\frac{P_{2}}{P_{1}}\right)\!(0,0). |  |

Let us also remark that, more generally, one can compute all the derivatives of L i ​ ( u), L_{i}(u), M i ​ ( u), M_{i}(u), A i ​ ( u), A_{i}(u), B i ​ ( u) B_{i}(u) and C i ​ ( u) C_{i}(u) at u = 0 u=0, for i = 1, 2, i=1,2, in terms of the derivatives of P 1 ​ ( x, y) P_{1}(x,y) and P 2 ​ ( x, y) P_{2}(x,y) at ( x, y) = ( 0, 0) (x,y)=(0,0). □ \square

The second part of Theorem 1.6 provides the asymptotic expansion of the Dulac time associated to a vector field ( 1) (\ref{X}\hbox{}) having poles of arbitrary order n = ( n 1, n 2) ∈ ℤ ≥ 0 2. n=(n_{1},n_{2})\in\mathbb{Z}_{\geq 0}^{2}. In Theorem 4.3 we restrict ourselves to the case n 1 = 0 n_{1}=0 and n 2 ⩾ 1 n_{2}\geqslant 1 for several reasons. Firstly, for the sake of simplicity in the exposition, since dealing with the general situation will increase very much the number of cases to consider. Secondly because the study of the Dulac time of a hyperbolic saddle at infinity of any polynomial vector field of degree d d yields to the case n 1 = 0 n_{1}=0 and n 2 = d − 1. n_{2}=d-1. Thirdly, and more important for us, because it allows to tackle the conjectural bifurcation diagram of the period function of the quadratic centers that we undertook in [19].

###### Theorem 4.3.

? ⟨ \langle 9punts ⟩ \rangle?

Assuming n 1 = 0 n_{1}=0 and n 2 ⩾ 1 n_{2}\geqslant 1, let T ⁡ ( s, μ ^) T(s;{{\hat{\mu}}}) be the Dulac time of the hyperbolic saddle ( 1) (\ref{X}\hbox{}) from Σ 1 \Sigma_{1} and Σ 2 \Sigma_{2}.

1. ( 1) (1)

If λ 0 ∈ ( 0, 1 n 2 + 1) \lambda_{0}\in(0,\frac{1}{n_{2}+1}) then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 0 ​ n 2 ​ ( μ ^) ​ s λ ​ n 2 + T 0, n 2 + 1 ​ ( μ ^) ​ s λ ⁡ ( n 2 + 1) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{0n_{2}}({{\hat{\mu}}})s^{\lambda n_{2}}+T_{0,n_{2}+1}({{\hat{\mu}}})s^{\lambda(n_{2}+1)}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [λ 0 ​ ( n 2 + 1), min ⁡ ( 1, λ 0 ​ ( n 2 + 2))) L\in\big[\lambda_{0}(n_{2}+1),\min(1,\lambda_{0}(n_{2}+2))\big).

2. ( 2) (2)

If λ 0 ∈ ( 1 n 2 + 1, 2 n 2 + 1) ∖ { 1 n 2 } \lambda_{0}\in(\frac{1}{n_{2}+1},\frac{2}{n_{2}+1})\setminus\{\frac{1}{n_{2}}\} then

 | T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 0 ​ n 2 ​ ( μ ^) ​ s λ ​ n 2 + T 10 ​ ( μ ^) ​ s + T 0, n 2 + 1 ​ ( μ ^) ​ s λ ⁡ ( n 2 + 1) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{0n_{2}}({{\hat{\mu}}})s^{\lambda n_{2}}+T_{10}({{\hat{\mu}}})s+T_{0,n_{2}+1}({{\hat{\mu}}})s^{\lambda(n_{2}+1)}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) |  |

for any L ∈ [max ( 1, λ 0 ( n 2 + 1), min ( 2, λ 0 n 2 + 1, λ 0 ( n 2 + 2))) L\in\big[\max(1,\lambda_{0}(n_{2}+1),\min(2,\lambda_{0}n_{2}+1,\lambda_{0}(n_{2}+2))\big).

3. ( 3) (3)

If λ 0 ∈ ( 2 n 2 + 1, 2 n 2) \lambda_{0}\in(\frac{2}{n_{2}+1},\frac{2}{n_{2}}) then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 10 ​ ( μ ^) ​ s + T 0 ​ n 2 ​ ( μ ^) ​ s λ ​ n 2 + T 20 ​ ( μ ^) ​ s 2 + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{10}({{\hat{\mu}}})s+T_{0n_{2}}({{\hat{\mu}}})s^{\lambda n_{2}}+T_{20}({{\hat{\mu}}})s^{2}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [max ( 2, λ 0 n 2), λ 0 n 2 + min ( 1, λ 0)) L\in\big[\max(2,\lambda_{0}n_{2}),\lambda_{0}n_{2}+\min(1,\lambda_{0})\big).

4. ( 4) (4)

If λ 0 > 2 n 2 \lambda_{0}>\frac{2}{n_{2}} then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 10 ​ ( μ ^) ​ s + T 20 ​ ( μ ^) ​ s 2 + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{10}({{\hat{\mu}}})s+T_{20}({{\hat{\mu}}})s^{2}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2, min ⁡ ( 3, λ 0 ​ n 2)) L\in\big[2,\min(3,\lambda_{0}n_{2})\big).

5. ( 5) (5)

If λ 0 = 1 n 2 + 1 \lambda_{0}=\frac{1}{n_{2}+1} then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 0 ​ n 2 ​ ( μ ^) ​ s λ ​ n 2 + s ​ 𝑻 10 λ 0 ​ ( ω, μ ^) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{0n_{2}}({{\hat{\mu}}})s^{\lambda n_{2}}+s\boldsymbol{T}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [1, n 2 + 2 n 2 + 1) L\in[1,\frac{n_{2}+2}{n_{2}+1}), where

 | 𝑻 10 λ 0 ​ ( ω, μ ^) = T 10 ​ ( μ ^) + T 0, n 2 + 1 ​ ( μ ^) ​ ( 1 + α ​ ω), \boldsymbol{T}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=T_{10}({{\hat{\mu}}})+T_{0,n_{2}+1}({{\hat{\mu}}})(1+\alpha\omega), |  |

α = 1 − λ ⁡ ( n 2 + 1) \alpha=1-\lambda(n_{2}+1) and ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha).

6. ( 6) (6)

If λ 0 = 1 n 2 \lambda_{0}=\frac{1}{n_{2}} with n 2 > 1 n_{2}>1 then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + s ​ 𝑻 10 λ 0 ​ ( ω, μ ^) + T 0, n 2 + 1 ​ ( μ ^) ​ s λ ⁡ ( n 2 + 1) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+s\boldsymbol{T}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})+T_{0,n_{2}+1}({{\hat{\mu}}})s^{\lambda(n_{2}+1)}+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [n 2 + 1 n 2, n 2 + 2 n 2) L\in[\frac{n_{2}+1}{n_{2}},\frac{n_{2}+2}{n_{2}}), where

 | 𝑻 10 λ 0 ​ ( ω, μ ^) = T 10 ​ ( μ ^) + T 0 ​ n 2 ​ ( μ ^) ​ ( 1 + α ​ ω), \boldsymbol{T}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=T_{10}({{\hat{\mu}}})+T_{0n_{2}}({{\hat{\mu}}})(1+\alpha\omega), |  |

α = 1 − λ ​ n 2 \alpha=1-\lambda n_{2} and ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha).

7. ( 7) (7)

If λ 0 = 2 n 2 + 1 \lambda_{0}=\frac{2}{n_{2}+1} with n 2 > 1 n_{2}>1 then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 10 ​ ( μ ^) ​ s + T 0 ​ n 2 ​ ( μ ^) ​ s λ ​ n 2 + s 2 ​ 𝑻 20 λ 0 ​ ( ω, μ ^) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{10}({{\hat{\mu}}})s+T_{0n_{2}}({{\hat{\mu}}})s^{\lambda n_{2}}+s^{2}\boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2, min ⁡ ( 2 ​ n 2 + 4 n 2 + 1, 3 ​ n 2 + 1 n 2 + 1)) L\in\big[2,\min\big(\frac{2n_{2}+4}{n_{2}+1},\frac{3n_{2}+1}{n_{2}+1}\big)\big), where

 | 𝑻 20 λ 0 ​ ( ω, μ ^) = T 20 ​ ( μ ^) + T 0, n 2 + 1 ​ ( μ ^) ​ ( 1 + α ​ ω) d, \boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=T_{20}({{\hat{\mu}}})+T_{0,n_{2}+1}({{\hat{\mu}}})\left(1+\alpha\omega\right)^{d}, |  |

d = gcd ⁡ ( 2, n 2 + 1) d=\gcd(2,n_{2}+1), α = 2 − λ ⁡ ( n 2 + 1) d \alpha=\frac{2-\lambda(n_{2}+1)}{d} and ω = ω ⁡ ( s, α). \omega=\omega(s;\alpha).

8. ( 8) (8)

If λ 0 = 1 \lambda_{0}=1 and n 2 = 1 n_{2}=1 then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + s ​ 𝑻 10 λ 0 ​ ( ω, μ ^) + s 2 ​ 𝑻 20 λ 0 ​ ( ω, μ ^) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+s\boldsymbol{T}_{10}^{\lambda_{0}}(\omega;{{\hat{\mu}}})+s^{2}\boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2, 3) L\in[2,3), where

 | 𝑻 r ​ 0 λ 0 ​ ( ω, μ ^) = ∑ i = 0 r T r − i, i ​ ( μ ^) ​ ( 1 + α ​ ω) i ​, for r = 1, 2, \boldsymbol{T}_{r0}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\sum_{i=0}^{r}T_{r-i,i}({{\hat{\mu}}})(1+\alpha\omega)^{i}\text{, for $r=1,2$,} |  |

α = 1 − λ \alpha=1-\lambda and ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha).

9. ( 9) (9)

If λ 0 = 2 n 2 \lambda_{0}=\frac{2}{n_{2}} then T ⁡ ( s, μ ^) = T 00 ​ ( μ ^) + T 10 ​ ( μ ^) ​ s + s 2 ​ 𝑻 20 λ 0 ​ ( ω, μ ^) + ℱ L ∞ ​ ( { λ 0 } × W) T(s;{{\hat{\mu}}})=T_{00}({{\hat{\mu}}})+T_{10}({{\hat{\mu}}})s+s^{2}\boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})+\mathcal{F}_{L}^{\infty}(\{\lambda_{0}\}\times W) for any L ∈ [2, min ⁡ ( 3, 2 + 2 n 2)) L\in\big[2,\min\big(3,2+\frac{2}{n_{2}}\big)\big), where

 | 𝑻 20 λ 0 ​ ( ω, μ ^) = T 20 ​ ( μ ^) + T 0 ​ n 2 ​ ( μ ^) ​ ( 1 + α ​ ω) d, \boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=T_{20}({{\hat{\mu}}})+T_{0n_{2}}({{\hat{\mu}}})\left(1+\alpha\omega\right)^{d}, |  |

d = gcd ⁡ ( 2, n 2) d=\gcd(2,n_{2}), α = 2 − λ ​ n 2 d \alpha=\frac{2-\lambda n_{2}}{d} and ω = ω ⁡ ( s, α). \omega=\omega(s;\alpha).

The asymptotic expansions in ( 1), (1), ( 2) (2), ( 3) (3) and ( 4) (4) will follow by applying ( b ​ 1) (b1) in Theorem 1.6 once we determine the grids ℬ λ 0, L n \mathscr{B}_{\lambda_{0},L}^{n} and show that, under the respective assumptions on λ 0 \lambda_{0} and L L, we have λ 0 ∉ D L n \lambda_{0}\notin D^{n}_{L}. Next we particularise the arguments leading to this in each case:

1. ( 1) (1)

In this case the hypothesis λ 0 ​ ( n 2 + 1) ⩽ L < min ⁡ ( 1, λ 0 ​ ( n 2 + 2)) \lambda_{0}(n_{2}+1)\leqslant L<\min(1,\lambda_{0}(n_{2}+2)) yield ℬ λ 0, L n = { ( 0, 0), ( 0, n 2), ( 0, n 2 + 1) } \mathscr{B}_{\lambda_{0},L}^{n}=\{(0,0),(0,n_{2}),(0,n_{2}+1)\}. For instance let us show that L < min ⁡ ( 1, λ 0 ​ ( n 2 + 2)) L<\min(1,\lambda_{0}(n_{2}+2)) implies ℬ λ 0, L n ⊂ { ( 0, 0), ( 0, n 2), ( 0, n 2 + 1) } \mathscr{B}_{\lambda_{0},L}^{n}\subset\{(0,0),(0,n_{2}),(0,n_{2}+1)\}. To prove this it suffices to check that ( 1, 0) (1,0) and ( 0, n 2 + 2) (0,n_{2}+2) do not belong to ℬ λ 0, L n \mathscr{B}_{\lambda_{0},L}^{n}, which is indeed a consequence of L < 1 L<1 and L < λ 0 ​ ( n 2 + 2) L<\lambda_{0}(n_{2}+2), respectively. The reverse inclusion ⊃ \supset follows similarly taking λ 0 ​ ( n 2 + 1) ⩽ L \lambda_{0}(n_{2}+1)\leqslant L into account. Since the assumption λ 0 ∈ ( 0, 1 n 2 + 1) \lambda_{0}\in(0,\frac{1}{n_{2}+1}) and Remark 1 imply that λ 0 ∉ D 00 n ∪ D 0 ​ n 2 n ∪ D 0, n 2 + 1 n = ∅ ∪ ℕ n 2 ∪ ( ℕ n 2 + 1 ∪ ℕ) \lambda_{0}\notin D_{00}^{n}\cup D_{0n_{2}}^{n}\cup D_{0,n_{2}+1}^{n}=\emptyset\cup\frac{\mathbb{N}}{n_{2}}\cup\big(\frac{\mathbb{N}}{n_{2}+1}\cup\mathbb{N}\big), we can assert that λ 0 ∉ D L n. \lambda_{0}\notin D_{L}^{n}.

2. ( 2) (2)

In this case it turns out that max ( 1, λ 0 ( n 2 + 1) ⩽ L < min ( 2, λ 0 n 2 + 1, λ 0 ( n 2 + 2)) \max(1,\lambda_{0}(n_{2}+1)\leqslant L<\min(2,\lambda_{0}n_{2}+1,\lambda_{0}(n_{2}+2)) implies that the grid is given by ℬ λ 0, L n = { ( 0, 0), ( 0, n 2), ( 1, 0), ( 0, n 2 + 1) }. \mathscr{B}_{\lambda_{0},L}^{n}=\{(0,0),(0,n_{2}),(1,0),(0,n_{2}+1)\}. For instance, to show the inclusion ⊂ \subset is enough to verify that ( 2, 0) (2,0), ( 1, n 2) (1,n_{2}) and ( 0, n 2 + 2) (0,n_{2}+2) do not belong to ℬ λ 0, L n \mathscr{B}_{\lambda_{0},L}^{n}, which is a consequence of L < 2 L<2, L < 1 + λ 0 ​ n 2 L<1+\lambda_{0}n_{2} and L < λ 0 ​ ( n 2 + 2) L<\lambda_{0}(n_{2}+2), respectively. That being said, we know by Remark 1 that D 0 ​ n 2 n = ℕ n 2 D_{0n_{2}}^{n}=\frac{\mathbb{N}}{n_{2}}, D 10 n = 1 ℕ ≥ n 2 D_{10}^{n}=\frac{1}{\mathbb{N}_{\geq n_{2}}} and D 0, n 2 + 1 n = ℕ n 2 + 1 ∪ ℕ. D_{0,n_{2}+1}^{n}=\frac{\mathbb{N}}{n_{2}+1}\cup\mathbb{N}. Thus, on account of the assumption λ 0 ∈ ( 1 n 2 + 1, 2 n 2 + 1) ∖ { 1 n 2 } \lambda_{0}\in(\frac{1}{n_{2}+1},\frac{2}{n_{2}+1})\setminus\{\frac{1}{n_{2}}\}, we get λ 0 ∉ D 00 n ∪ D 0 ​ n 2 n ∪ D 10 n ∪ D 0, n 2 + 1 n \lambda_{0}\notin D_{00}^{n}\cup D_{0n_{2}}^{n}\cup D_{10}^{n}\cup D_{0,n_{2}+1}^{n}. Hence, see Definition 1, λ 0 ∉ D L n \lambda_{0}\notin D^{n}_{L}.

3. ( 3) (3)

If max ⁡ ( 2, n 2 ​ λ 0) ⩽ L < min ⁡ ( λ 0 ​ n 2 + 1, λ 0 ​ ( n 2 + 1)) \max(2,n_{2}\lambda_{0})\leqslant L<\min(\lambda_{0}n_{2}+1,\lambda_{0}(n_{2}+1)) then ℬ λ 0, L n = { ( 0, 0), ( 1, 0), ( 2, 0), ( 0, n 2) } \mathscr{B}_{\lambda_{0},L}^{n}=\{(0,0),(1,0),(2,0),(0,n_{2})\}. Indeed, the lower bound gives the inclusion ⊃. \supset. To prove the inclusion ⊂ \subset it suffices to check that ( 3, 0) (3,0), ( 1, n 2) (1,n_{2}) and ( 0, n 2 + 1) (0,n_{2}+1) do not belong to ℬ λ 0, L n \mathscr{B}_{\lambda_{0},L}^{n}, which is a consequence of L < 3 L<3, L < 1 + λ 0 ​ n 2 L<1+\lambda_{0}n_{2} and L < λ 0 ​ ( n 2 + 1) L<\lambda_{0}(n_{2}+1), respectively. These three inequalities follow by the assumption L < min ⁡ ( λ 0 ​ n 2 + 1, λ 0 ​ ( n 2 + 1)) L<\min(\lambda_{0}n_{2}+1,\lambda_{0}(n_{2}+1)) together with the fact that λ 0 ​ n 2 < 2 \lambda_{0}n_{2}<2 due to λ 0 ∈ ( 2 n 2 + 1, 2 n 2) \lambda_{0}\in(\frac{2}{n_{2}+1},\frac{2}{n_{2}}). This last condition, taking Remark 1 also into account, implies λ 0 ∉ D 00 n ∪ D 10 n ∪ D 0, n 2 n ∪ D 20 n = ∅ ∪ 1 ℕ ≥ n 2 ∪ ℕ n 2 \lambda_{0}\notin D_{00}^{n}\cup D_{10}^{n}\cup D_{0,n_{2}}^{n}\cup D_{20}^{n}=\emptyset\cup\frac{1}{\mathbb{N}_{\geq n_{2}}}\cup\frac{\mathbb{N}}{n_{2}} and then λ 0 ∉ D L n \lambda_{0}\notin D^{n}_{L}.

4. ( 4) (4)

Similarly as in the previous cases, if 2 ⩽ L < min ⁡ ( 3, λ 0 ​ n 2) 2\leqslant L<\min(3,\lambda_{0}n_{2}) then ℬ λ 0, L n = { ( 0, 0), ( 1, 0), ( 2, 0) } \mathscr{B}^{n}_{\lambda_{0},L}=\{(0,0),(1,0),(2,0)\}. Moreover, by Remark 1 and the hypothesis λ 0 > 2 n 2 \lambda_{0}>\frac{2}{n_{2}}, we get λ 0 ∉ D 00 n ∪ D 10 n ∪ D 20 n = ∅ ∪ 1 ℕ ≥ n 2 ∪ 2 ℕ ≥ n 2 \lambda_{0}\notin D^{n}_{00}\cup D^{n}_{10}\cup D^{n}_{20}=\emptyset\cup\frac{1}{\mathbb{N}_{\geq n_{2}}}\cup\frac{2}{\mathbb{N}_{\geq n_{2}}}. Therefore λ 0 ∉ D L n \lambda_{0}\notin D^{n}_{L}.

The remaining assertions follow by applying ( b ​ 2) (b2) in Theorem 1.6. To this end we need to verify that λ 0 ∈ D L n \lambda_{0}\in D^{n}_{L} and determine the grid ℬ λ 0, L n \mathscr{B}_{\lambda_{0},L}^{n} together with the corresponding sets 𝒜 i ​ j ​ λ 0 n \mathscr{A}_{ij\lambda_{0}}^{n}. As before we next particularise this in each case:

1. ( 5) (5)

If λ 0 = 1 n 2 + 1 \lambda_{0}=\frac{1}{n_{2}+1} and 1 ⩽ L < 1 + 1 n 2 + 1 1\leqslant L<1+\frac{1}{n_{2}+1} then ℬ λ 0, L n = { ( 0, 0), ( 0, n 2), ( 0, n 2 + 1), ( 1, 0) } \mathscr{B}^{n}_{\lambda_{0},L}=\{(0,0),(0,n_{2}),(0,n_{2}+1),(1,0)\}. Indeed, to show the inclusion ⊂ \subset it suffices to check that ( 1, n 2) (1,n_{2}), ( 0, n 2 + 2) (0,n_{2}+2) and ( 2, 0) (2,0) do not belong to ℬ λ 0, L n \mathscr{B}^{n}_{\lambda_{0},L}, which is equivalent to L < 1 + λ 0 ​ n 2 = 1 + n 2 n 2 + 1 L<1+\lambda_{0}n_{2}=1+\frac{n_{2}}{n_{2}+1}, L < λ 0 ​ ( n 2 + 2) = 1 + 1 n 2 + 1 L<\lambda_{0}(n_{2}+2)=1+\frac{1}{n_{2}+1} and L < 2 L<2, respectively. These three conditions are a consequence of the assumption L < 1 + 1 n 2 + 1 L<1+\frac{1}{n_{2}+1}. With regard to the inclusion ⊃ \supset, the fact that ( 0, 0) (0,0), ( 0, n 2), (0,n_{2}), ( 0, n 2 + 1) (0,n_{2}+1) and ( 1, 0) (1,0) belong to ℬ λ 0, L n \mathscr{B}^{n}_{\lambda_{0},L} is written as L ⩾ 0, L\geqslant 0, L ⩾ λ 0 ​ n 2 = n 2 n 2 + 1 L\geqslant\lambda_{0}n_{2}=\frac{n_{2}}{n_{2}+1}, L ⩾ λ 0 ​ ( n 2 + 1) = 1 L\geqslant\lambda_{0}(n_{2}+1)=1 and L ⩾ 1, L\geqslant 1, respectively, which are guaranteed by the assumption L ⩾ 1. L\geqslant 1. Since, on the other hand, λ 0 = 1 n 2 + 1 ∈ D 0, n 2 + 1 n = ℕ n 2 + 1 \lambda_{0}=\frac{1}{n_{2}+1}\in D_{0,n_{2}+1}^{n}=\frac{\mathbb{N}}{n_{2}+1} by Remark 1, it turns out that λ 0 ∈ D L n \lambda_{0}\in D^{n}_{L}, see Definition 1.

Finally the result follows, see Definition 1 again, using that 𝒜 10 ​ λ 0 n = { 0, 1 }, \mathscr{A}_{10\lambda_{0}}^{n}=\{0,1\}, 𝒜 00 ​ λ 0 n = 𝒜 0 ​ n 2 ​ λ 0 n = { 0 } \mathscr{A}_{00\lambda_{0}}^{n}=\mathscr{A}_{0n_{2}\lambda_{0}}^{n}=\{0\} and 𝒜 0, n 2 + 1, λ 0 n = ∅, \mathscr{A}_{0,n_{2}+1,\lambda_{0}}^{n}=\emptyset, together with p = 1 p=1 and q = n 2 + 1 q=n_{2}+1, so that α = 1 − λ ⁡ ( n 2 + 1). \alpha=1-\lambda(n_{2}+1).

2. ( 6) (6)

If λ 0 = 1 n 2 \lambda_{0}=\frac{1}{n_{2}} with n 2 > 1 n_{2}>1 and n 2 + 1 n 2 ⩽ L < n 2 + 2 n 2 \frac{n_{2}+1}{n_{2}}\leqslant L<\frac{n_{2}+2}{n_{2}} then, just as we argue in the previous cases, we get that ℬ λ 0, L n = { ( 0, 0), ( 1, 0), ( 0, n 2), ( 0, n 2 + 1) } \mathscr{B}_{\lambda_{0},L}^{n}=\{(0,0),(1,0),(0,n_{2}),(0,n_{2}+1)\}. Furthermore, since λ 0 = 1 n 2 ∈ D 10 n = 1 ℕ ≥ n 2 \lambda_{0}=\frac{1}{n_{2}}\in D_{10}^{n}=\frac{1}{\mathbb{N}_{\geq n_{2}}} by Remark 1, it turns out that λ 0 ∈ D L n \lambda_{0}\in D^{n}_{L}. On account of this the result follows using that 𝒜 10 ​ λ 0 n = { 0, 1 }, \mathscr{A}_{10\lambda_{0}}^{n}=\{0,1\}, 𝒜 00 ​ λ 0 n = 𝒜 0, n 2 + 1, λ 0 n = { 0 } \mathscr{A}_{00\lambda_{0}}^{n}=\mathscr{A}_{0,n_{2}+1,\lambda_{0}}^{n}=\{0\} and 𝒜 0 ​ n 2 ​ λ 0 n = ∅, \mathscr{A}_{0n_{2}\lambda_{0}}^{n}=\emptyset, together with the fact that α = 1 − λ ​ n 2 \alpha=1-\lambda n_{2}, which in turn follows due to p = 1 p=1 and q = n 2 q=n_{2}.

3. ( 7) (7)

If λ 0 = 2 n 2 + 1 \lambda_{0}=\frac{2}{n_{2}+1} with n 2 > 1 n_{2}>1 and 2 ⩽ L < min ⁡ ( 2 ​ n 2 + 4 n 2 + 1, 3 ​ n 2 + 1 n 2 + 1) 2\leqslant L<\min\big(\frac{2n_{2}+4}{n_{2}+1},\frac{3n_{2}+1}{n_{2}+1}\big) then

 | ℬ λ 0, L n = { ( 0, 0), ( 1, 0), ( 0, n 2), ( 2, 0), ( 0, n 2 + 1) }. \mathscr{B}^{n}_{\lambda_{0},L}=\{(0,0),(1,0),(0,n_{2}),(2,0),(0,n_{2}+1)\}. |  |

As usual, the inequality L < min ⁡ ( 2 ​ n 2 + 4 n 2 + 1, 3 ​ n 2 + 1 n 2 + 1) L<\min\big(\frac{2n_{2}+4}{n_{2}+1},\frac{3n_{2}+1}{n_{2}+1}\big) gives the inclusion ⊂ \subset, in this case by showing that ( 3, 0), ( 1, n 2), ( 0, n 2 + 2) ∉ ℬ λ 0, L n (3,0),(1,n_{2}),(0,n_{2}+2)\notin\mathscr{B}^{n}_{\lambda_{0},L}, whereas the inequality 2 ⩽ L 2\leqslant L implies the reverse inclusion ⊃ \supset. Hence, since λ 0 = 2 n 2 + 1 ∈ D 02 n = 2 ℕ ≥ n 2 \lambda_{0}=\frac{2}{n_{2}+1}\in D_{02}^{n}=\frac{2}{\mathbb{N}_{\geq n_{2}}} by Remark 1, we conclude that λ 0 ∈ D L n. \lambda_{0}\in D_{L}^{n}. On the other hand, due to n 2 > 1 n_{2}>1, one can verify that 𝒜 00 ​ λ 0 n = 𝒜 10 ​ λ 0 n = 𝒜 0 ​ n 2 ​ λ 0 n = { 0 } \mathscr{A}_{00\lambda_{0}}^{n}=\mathscr{A}_{10\lambda_{0}}^{n}=\mathscr{A}_{0n_{2}\lambda_{0}}^{n}=\{0\}, 𝒜 0, n 2 + 1, λ 0 n = ∅ \mathscr{A}_{0,n_{2}+1,\lambda_{0}}^{n}=\emptyset and 𝒜 02 ​ λ 0 n = { 0, d }, \mathscr{A}_{02\lambda_{0}}^{n}=\{0,d\}, where d = gcd ⁡ ( 2, n 2 + 1). d=\gcd(2,n_{2}+1). Since p = 2 d p=\frac{2}{d} and q = n 2 + 1 d q=\frac{n_{2}+1}{d}, the last equality yields

 | 𝑻 20 λ 0 ​ ( ω, μ ^) = ∑ r ∈ { 0, d } T 2 − 2 d ​ r, n 2 + 1 d ​ r ​ ( μ ^) ​ ( 1 + α ​ ω) r = T 20 ​ ( μ ^) + T 0, n 2 + 1 ​ ( μ ^) ​ ( 1 + α ​ ω) d, \boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\sum_{r\in\{0,d\}}T_{2-\frac{2}{d}r,\frac{n_{2}+1}{d}r}({{\hat{\mu}}})\left(1+\alpha\omega\right)^{r}=T_{20}({{\hat{\mu}}})+T_{0,n_{2}+1}({{\hat{\mu}}})\left(1+\alpha\omega\right)^{d}, |  |

where ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha) and α = 2 − λ ⁡ ( n 2 + 1) d \alpha=\frac{2-\lambda(n_{2}+1)}{d}. This proves the validity of the statement.

4. ( 8) (8)

If λ 0 = 1 \lambda_{0}=1, n 2 = 1 n_{2}=1 and 2 ⩽ L < 3 2\leqslant L<3 then one can readily show that

 | ℬ λ 0, L n = { ( 0, 0), ( 1, 0), ( 0, 1), ( 2, 0), ( 1, 1), ( 0, 2) }. \mathscr{B}^{n}_{\lambda_{0},L}=\{(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\}. |  |

On account of this, since λ 0 = 1 ∈ D 01 n = ℕ \lambda_{0}=1\in D_{01}^{n}=\mathbb{N} by Remark 1 due to n = ( 0, 1) n=(0,1), we can assert that λ 0 ∈ D L n. \lambda_{0}\in D_{L}^{n}. In this case one can easily verify that 𝒜 00 ​ λ 0 n = { 0 } \mathscr{A}_{00\lambda_{0}}^{n}=\{0\}, 𝒜 01 ​ λ 0 n = 𝒜 02 ​ λ 0 n = 𝒜 11 ​ λ 0 n = ∅ \mathscr{A}_{01\lambda_{0}}^{n}=\mathscr{A}_{02\lambda_{0}}^{n}=\mathscr{A}_{11\lambda_{0}}^{n}=\emptyset, 𝒜 10 ​ λ 0 n = { 0, 1 } \mathscr{A}_{10\lambda_{0}}^{n}=\{0,1\} and 𝒜 20 ​ λ 0 n = { 0, 1, 2 }. \mathscr{A}_{20\lambda_{0}}^{n}=\{0,1,2\}. Since p = q = 1 p=q=1, the two last equalities show, respectively,

 | 𝑻 r ​ 0 λ 0 ​ ( ω, μ ^) = ∑ i = 0 r T r − i, i ​ ( μ ^) ​ ( 1 + α ​ ω) i ​, for r = 1, 2, \boldsymbol{T}_{r0}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\sum_{i=0}^{r}T_{r-i,i}({{\hat{\mu}}})(1+\alpha\omega)^{i}\text{, for $r=1,2$,} |  |

where α = 1 − λ \alpha=1-\lambda and ω = ω ⁡ ( s, α). \omega=\omega(s;\alpha).

5. ( 9) (9)

If λ 0 = 2 n 2 \lambda_{0}=\frac{2}{n_{2}} and 2 ⩽ L < min ⁡ ( 3, 2 + 2 n 2) 2\leqslant L<\min(3,2+\frac{2}{n_{2}}) then ℬ λ 0, L n = { ( 0, 0), ( 1, 0), ( 2, 0), ( 0, n 2) } \mathscr{B}^{n}_{\lambda_{0},L}=\{(0,0),(1,0),(2,0),(0,n_{2})\}. Consequently, due to λ 0 = 2 n 2 ∈ D 0 ​ n 2 n = ℕ n 2 \lambda_{0}=\frac{2}{n_{2}}\in D^{n}_{0n_{2}}=\frac{\mathbb{N}}{n_{2}} by Remark 1, we have λ 0 ∈ D L n \lambda_{0}\in D^{n}_{L}. Moreover 𝒜 00 ​ λ 0 n = 𝒜 10 ​ λ 0 n = { 0 } \mathscr{A}_{00\lambda_{0}}^{n}=\mathscr{A}_{10\lambda_{0}}^{n}=\{0\}, 𝒜 0 ​ n 2 ​ λ 0 n = ∅ \mathscr{A}_{0n_{2}\lambda_{0}}^{n}=\emptyset and 𝒜 20 ​ λ 0 n = { 0, d } \mathscr{A}_{20\lambda_{0}}^{n}=\{0,d\} with d = gcd ⁡ ( 2, n 2). d=\gcd(2,n_{2}). Since p = 2 d p=\frac{2}{d} and q = n 2 d q=\frac{n_{2}}{d}, from the last equality it follows that

 | 𝑻 20 λ 0 ​ ( ω, μ ^) = ∑ r ∈ { 0, d } T 2 − 2 d ​ r, n 2 d ​ r ​ ( μ ^) ​ ( 1 + α ​ ω) r = T 20 ​ ( μ ^) + T 0, n 2 ​ ( μ ^) ​ ( 1 + α ​ ω) d, \boldsymbol{T}_{20}^{\lambda_{0}}(\omega;{{\hat{\mu}}})=\sum_{r\in\{0,d\}}T_{2-\frac{2}{d}r,\frac{n_{2}}{d}r}({{\hat{\mu}}})\left(1+\alpha\omega\right)^{r}=T_{20}({{\hat{\mu}}})+T_{0,n_{2}}({{\hat{\mu}}})\left(1+\alpha\omega\right)^{d}, |  |

where ω = ω ⁡ ( s, α) \omega=\omega(s;\alpha) and α = 2 − λ ​ n 2 d \alpha=\frac{2-\lambda n_{2}}{d}.

This concludes the proof of the result.

Let us finish this section by pointing out that the formula of every coefficient T i ​ j T_{ij} appearing in Theorem 4.3 is given in assertion ( c) (c) of Theorem A, except for T 11 T_{11} in point ( 8) (8), that corresponds to λ 0 = n 2 = 1 \lambda_{0}=n_{2}=1. The formula of this coefficient follows by applying also assertions ( a) (a) and ( b) (b), which show that T 11 = Ω 10 ​ T 01 T_{11}=\Omega_{10}T_{01} and Ω 10 = λ ​ S 1 \Omega_{10}=\lambda S_{1}. Also with regard to this statement, it is worth noting that the order as s → 0 + s\to 0^{+} of the monomials in points from ( 1) (1) to ( 4) (4) follow readily from Figure 4. For instance, 1 ≺ λ 0 s λ ​ n 2 ≺ λ 0 s λ ⁡ ( n 2 + 1) ≺ λ 0 s ≺ λ 0 s 2 1\prec_{\lambda_{0}}s^{\lambda n_{2}}\prec_{\lambda_{0}}s^{\lambda(n_{2}+1)}\prec_{\lambda_{0}}s\prec_{\lambda_{0}}s^{2} for λ 0 ∈ ( 0, 1 n 2 + 1) \lambda_{0}\in(0,\frac{1}{n_{2}+1}) and 1 ≺ λ 0 s λ ​ n 2 ≺ λ 0 s ≺ λ 0 s λ ⁡ ( n 2 + 1) ≺ λ 0 s 2 1\prec_{\lambda_{0}}s^{\lambda n_{2}}\prec_{\lambda_{0}}s\prec_{\lambda_{0}}s^{\lambda(n_{2}+1)}\prec_{\lambda_{0}}s^{2} for λ 0 ∈ ( 1 n 2 + 1, 1 n 2) \lambda_{0}\in(\frac{1}{n_{2}+1},\frac{1}{n_{2}}), see [23, Definition 1.7] for details. For λ ≈ λ 0 = 1 n 2 + 1 \lambda\approx\lambda_{0}=\frac{1}{n_{2}+1}, which corresponds to an intersection between two straight-lines in Figure 4, the compensators come into play and we have 1 ≺ λ 0 s λ ​ n 2 ≺ λ 0 s ω ( s; α) ≺ λ 0 s ≺ λ 0 s 2 1\prec_{\lambda_{0}}s^{\lambda n_{2}}\prec_{\lambda_{0}}s\omega(s;\alpha)\prec_{\lambda_{0}}s\prec_{\lambda_{0}}s^{2} with α = 1 − λ ⁡ ( n 2 + 1), \alpha=1-\lambda(n_{2}+1), see point ( 5) (5) in Theorem 4.3. This type of information is very relevant in order to apply [23, Theorem C] to bound the number of critical periods or limit cycles that bifurcate from a hyperbolic polycycle.

Figure 4: Going upward from each abscissa λ 0 ∈ ( 0, + ∞) \lambda_{0}\in(0,+\infty), order of monomials s i + λ ​ j s^{i+\lambda j} as s → 0 + s\to 0^{+} and λ ≈ λ 0 \lambda\approx\lambda_{0} for ( i, j) ∈ { ( 0, 0), ( 1, 0), ( 2, 0), ( 0, n 2), ( 0, n 2 + 1) } (i,j)\in\{(0,0),(1,0),(2,0),(0,n_{2}),(0,n_{2}+1)\}.

## Appendix A Derivatives of regular transition map and transition time

In this section we consider a family of vector fields of the form

 | Y ν = 1 y ℓ ​ f ​ ( x, y, ν) ( ∂ x + y h ( x, y; ν) ∂ y), Y_{\nu}=\frac{1}{y^{{\ell}}f(x,y;\nu)}\bigl(\partial_{x}+yh(x,y;\nu)\partial_{y}\bigr), |  | (42) |

where

- •

ℓ ∈ ℤ {\ell}\in\mathbb{Z} and ν ∈ U \nu\in U, where U U is some open set of ℝ N, \mathbb{R}^{N},

- •

f, h ∈ 𝒞 K ​ ( V × U) f,h\in\mathscr{C}^{K}(V\!\times\!U) with V:= ( a, b) × ( − c, c) ⊂ ℝ 2 V\!:=(a,b)\!\times\!(-c,c)\subset\mathbb{R}^{2}, a < b a<b and c > 0, c>0,

- •

f ⁡ ( x, 0, ν) ≠ 0 f(x,0;\nu)\neq 0 for all x ∈ ( a, b) x\in(a,b) and ν ∈ U \nu\in U.

We also consider two 𝒞 K \mathscr{C}^{K} families of transverse sections ξ ⁡ ( ⋅, ν): ( − ε, ε) ⟶ Π 1 {\xi(\,\cdot\,;\nu)}\!:{(-\varepsilon,\varepsilon)}\longrightarrow{\Pi_{1}} and ζ ⁡ ( ⋅, ν): ( − ε, ε) ⟶ Π 2 {\zeta(\,\cdot\,;\nu)}\!:{(-\varepsilon,\varepsilon)}\longrightarrow{\Pi_{2}} to the straight line { y = 0 } \{y=0\}, i.e., verifying ξ 2 ​ ( 0) = ζ 2 ​ ( 0) = 0 \xi_{2}(0)=\zeta_{2}(0)=0 together with ξ 2 ′ ​ ( 0) ≠ 0 \xi_{2}^{\prime}(0)\neq 0 and ζ 2 ′ ​ ( 0) ≠ 0. \zeta_{2}^{\prime}(0)\neq 0. Our goal is to give the first non-trivial terms of the transition map P ⁡ ( ⋅, ν) P(\,\cdot\,;\nu) and the transition time T ⁡ ( ⋅, ν) T(\,\cdot\,;\nu) between Π 1 \Pi_{1} and Π 2. \Pi_{2}. More precisely, denoting by φ ⁡ ( t, p 0, ν) \varphi(t,p_{0};\nu) the solution of Y ν Y_{\nu} with initial condition p 0 ∈ V p_{0}\in V, we define P ⁡ ( s, ν) P(s;\nu) and T ⁡ ( s, ν) T(s;\nu) by means of φ ⁡ ( T ⁡ ( s), ξ ⁡ ( s)) = ζ ⁡ ( P ⁡ ( s)). \varphi(T(s),\xi(s))=\zeta(P(s)). The smoothness assumption for the results in this appendix is K ⩾ 3. K\geqslant 3.

In what follows ϕ ⁡ ( t, p 0, ν) \phi(t,p_{0};\nu) denotes the solution of Z ν:= ∂ x + y h ( x, y; ν) ∂ y Z_{\nu}\!:=\partial_{x}+yh(x,y;\nu)\partial_{y} with initial condition at p 0 = ( x, y). p_{0}=(x,y). It is clear that ϕ ⁡ ( t, p 0, ν) = ( x + t, ϕ 2 ​ ( t, p 0, ν)) \phi(t,p_{0};\nu)=\big(x+t,\phi_{2}(t,p_{0};\nu)). With regard to the second component we prove the next result:

###### Lemma A.1.

? ⟨ \langle L1 ⟩ \rangle?

Let us define H ⁡ ( x, y, ν) = exp ⁡ ( ∫ y x h ⁡ ( u, 0, ν) ​ 𝑑 u) \displaystyle H(x,y;\nu)=\exp\left(\int_{y}^{x}h(u,0;\nu)du\right). Then the following hold:

1. ( a) (a)

∂ x ϕ 2 ​ ( t, ( x, 0)) = 0 \partial_{x}\phi_{2}(t,(x,0))=0 and ∂ x ​ x 2 ϕ 2 ​ ( t, ( x, 0)) = 0 \partial_{xx}^{2}\phi_{2}(t,(x,0))=0,

2. ( b) (b)

∂ y ϕ 2 ​ ( t, ( x, 0)) = H ⁡ ( x + t, x) \partial_{y}\phi_{2}(t,(x,0))=H(x+t,x) and ∂ x ​ y 2 ϕ 2 ​ ( t, ( x, 0)) = H ⁡ ( x + t, x) ​ ( h ⁡ ( x + t, 0) − h ⁡ ( x, 0)) \partial_{xy}^{2}\phi_{2}(t,(x,0))=H(x+t,x)\big(h(x+t,0)-h(x,0)\big),

3. ( c) (c)

∂ y ​ y 2 ϕ 2 ​ ( t, ( x, 0)) = 2 ​ H ​ ( x + t, x) ​ ∫ 0 t H ⁡ ( x + v, x) ​ ∂ 2 h ⁡ ( x + v, 0) ​ 𝑑 v \partial_{yy}^{2}\phi_{2}(t,(x,0))=2H(x+t,x)\int_{0}^{t}H(x+v,x)\partial_{2}h(x+v,0)dv.

On account of ∂ t ϕ 2 ​ ( t, ( x, y)) = ϕ 2 ​ ( t, ( x, y)) ​ h ​ ( x + t, ϕ 2 ​ ( t, ( x, y))) \partial_{t}\phi_{2}(t,(x,y))=\phi_{2}(t,(x,y))h\big(x+t,\phi_{2}(t,(x,y))\big) and ϕ 2 ​ ( t, ( x, 0)) = 0 \phi_{2}(t,(x,0))=0 we obtain

 | ∂ t ∂ x ϕ 2 ​ ( t, ( x, 0)) = h ⁡ ( x + t, 0) ​ ∂ x ϕ 2 ​ ( t, ( x, 0)). \partial_{t}\partial_{x}\phi_{2}(t,(x,0))=h(x+t,0)\partial_{x}\phi_{2}(t,(x,0)). |  |

Since ∂ x ϕ 2 ​ ( 0, ( x, 0)) = 0 \partial_{x}\phi_{2}(0,(x,0))=0 due to ϕ 2 ​ ( 0, ( x, y)) = y \phi_{2}(0,(x,y))=y, we get ∂ x ϕ 2 ​ ( t, ( x, 0)) = 0 \partial_{x}\phi_{2}(t,(x,0))=0. Accordingly ∂ x ​ x 2 ϕ 2 ​ ( t, ( x, 0)) = 0 \partial^{2}_{xx}\phi_{2}(t,(x,0))=0 and this shows ( a) (a). Similarly we obtain ∂ t ∂ y ϕ 2 ​ ( t, ( x, 0)) = h ⁡ ( x + t, 0) ​ ∂ y ϕ 2 ​ ( t, ( x, 0)) \partial_{t}\partial_{y}\phi_{2}(t,(x,0))=h(x+t,0)\partial_{y}\phi_{2}(t,(x,0)) and ∂ y ϕ 2 ​ ( 0, ( x, 0)) = 1 \partial_{y}\phi_{2}(0,(x,0))=1. Consequently

 |  | ∂ y ϕ 2 ​ ( t, ( x, 0)) = exp ⁡ ( ∫ 0 t h ⁡ ( x + u, 0) ​ 𝑑 u) = H ⁡ ( x + t, x) \displaystyle\partial_{y}\phi_{2}(t,(x,0))=\exp\left(\int_{0}^{t}h(x+u,0)du\right)=H(x+t,x) |  | (43) |

and |

 |  | ∂ x ​ y 2 ϕ 2 ​ ( t, ( x, 0)) = exp ⁡ ( ∫ 0 t h ⁡ ( x + u, 0) ​ 𝑑 u) ​ ∫ 0 t ∂ 1 h ⁡ ( x + u, 0) ​ 𝑑 u = H ⁡ ( x + t, x) ​ ( h ⁡ ( x + t, 0) − h ⁡ ( x, 0)), \displaystyle\partial^{2}_{xy}\phi_{2}(t,(x,0))=\exp\left(\int_{0}^{t}h(x+u,0)du\right)\int_{0}^{t}\partial_{1}h(x+u,0)du=H(x+t,x)\big(h(x+t,0)-h(x,0)\big), |  |

which shows the validity of ( b) (b). Finally, using that

 | ∂ t ∂ y ​ y 2 ϕ 2 ​ ( t, ( x, 0)) \displaystyle\partial_{t}\partial_{yy}^{2}\phi_{2}(t,(x,0)) | = ∂ y ​ y 2 ( h ⁡ ( x + t, ϕ 2 ​ ( t, ( x, y))) ​ ϕ 2 ​ ( t, ( x, y))) | y = 0 \displaystyle=\left.\partial_{yy}^{2}\Big(h(x+t,\phi_{2}(t,(x,y)))\phi_{2}(t,(x,y))\Big)\right|_{y=0} |  |

 |  | = 2 ​ ∂ 2 h ⁡ ( x + t, 0) ​ ( ∂ y ϕ 2 ​ ( t, ( x, 0))) 2 + h ⁡ ( x + t, 0) ​ ∂ y ​ y 2 ϕ 2 ​ ( t, ( x, 0)), \displaystyle=2\partial_{2}h(x+t,0)(\partial_{y}\phi_{2}(t,(x,0)))^{2}+h(x+t,0)\partial_{yy}^{2}\phi_{2}(t,(x,0)), |  |

together with ∂ y ​ y 2 ϕ 2 ​ ( 0, ( x, 0)) = 0 \partial_{yy}^{2}\phi_{2}(0,(x,0))=0 and ( 43) (\ref{L1eq1}\immediate), we get

 | ∂ y ​ y 2 ϕ 2 ​ ( t, ( x, 0)) = 2 ​ exp ⁡ ( ∫ 0 t h ⁡ ( x + u, 0) ​ 𝑑 u) ​ ∫ 0 t exp ⁡ ( ∫ 0 v h ⁡ ( x + u, 0) ​ 𝑑 u) ​ ∂ 2 h ⁡ ( x + v, 0) ​ 𝑑 v. \partial_{yy}^{2}\phi_{2}(t,(x,0))=2\exp\left(\int_{0}^{t}h(x+u,0)du\right)\int_{0}^{t}\exp\left(\int_{0}^{v}h(x+u,0)du\right)\partial_{2}h(x+v,0)dv. |  |

Taking ( 43) (\ref{L1eq1}\hbox{}) into account once again, the above equality shows ( c) (c) and concludes the proof of the result.

Let us remark that in the previous result (and in what follows when there is no risk of ambiguity) we omit the dependence with respect to the parameter ν \nu for the sake of shortness. Note on the other hand that the solution φ ⁡ ( t, ξ ⁡ ( s)) \varphi(t,\xi(s)) of Y ν Y_{\nu} is inside { y = ϕ 2 ( x − ξ 1 ( s), ξ ( s)) } \{y=\phi_{2}(x-\xi_{1}(s),\xi(s))\}. Thus, in order to obtain the first coefficients of the Taylor expansion of T ⁡ ( s) T(s) and P ⁡ ( s) P(s) at s = 0 s=0, we compute first the ones of

 | s ⟼ Ω ⁡ ( x, s, ν):= ϕ 2 ​ ( x − ξ 1 ​ ( s, ν), ξ ⁡ ( s, ν), ν). s\longmapsto\Omega(x,s;\nu)\!:=\phi_{2}\big(x-\xi_{1}(s;\nu),\xi(s;\nu);\nu\big). |  |

This is done in the next result, where H ⁡ ( x, y) = exp ⁡ ( ∫ y x h ⁡ ( u, 0) ​ 𝑑 u) H(x,y)=\exp\left(\int_{y}^{x}h(u,0)du\right), see Lemma A.1, and we use the compact notation ξ i ​ k = ξ i ( k) ​ ( 0) \xi_{ik}=\xi_{i}^{(k)}(0) for i = 1, 2. i=1,2.

###### Lemma A.2.

? ⟨ \langle L2 ⟩ \rangle?

The function Ω ⁡ ( x, s, ν) \Omega(x,s;\nu) is 𝒞 K \mathscr{C}^{K} on ( a, b) × ( − ε, ε) × U. (a,b)\!\times\!(-\varepsilon,\varepsilon)\!\times\!U. Moreover it verifies Ω ⁡ ( x, 0, ν) = 0 \Omega(x,0;\nu)=0, ρ 1 ​ ( x, ν):= ∂ s Ω ⁡ ( x, 0, ν) = ξ 21 ​ H ​ ( x, ξ 10) \rho_{1}(x;\nu)\!:=\partial_{s}\Omega(x,0;\nu)=\xi_{21}H(x,\xi_{10}) and

 | ρ 2 ​ ( x, ν):= ∂ s ​ s 2 Ω ⁡ ( x, 0, ν) = H ⁡ ( x, ξ 10) ​ ( ξ 22 − 2 ​ ξ 11 ​ ξ 21 ​ h ​ ( ξ 10, 0) + 2 ​ ξ 21 2 ​ ∫ ξ 10 x H ⁡ ( u, ξ 10) ​ ∂ 2 h ⁡ ( u, 0) ​ 𝑑 u). \rho_{2}(x;\nu)\!:=\partial_{ss}^{2}\Omega(x,0;\nu)=H(x,\xi_{10})\left(\xi_{22}-2\xi_{11}\xi_{21}h(\xi_{10},0)+2\xi_{21}^{2}\int_{\xi_{10}}^{x}H(u,\xi_{10})\partial_{2}h(u,0)du\right). |  |

The fact that Ω \Omega is 𝒞 K \mathscr{C}^{K} on ( a, b) × ( − ε, ε) × U (a,b)\!\times\!(-\varepsilon,\varepsilon)\!\times\!U follows from the smooth dependence of solutions with respect to initial conditions and parameters (see for instance [9, Theorem 1.1]) and that Ω ⁡ ( x, 0, ν) = 0 \Omega(x,0;\nu)=0 is due to the invariance of the straight line { y = 0 }. \{y=0\}.

Since ϕ ⁡ ( t, ( x, y)) \phi(t,(x,y)) is the solution of Z ν Z_{\nu} with initial condition at ( x, y) (x,y), in order to to avoid any ambiguity we consider Ω ⁡ ( z, s) = ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) \Omega(z,s)=\phi_{2}(z-\xi_{1}(s),\xi(s)) and so we keep the notation ∂ t \partial_{t}, ∂ x \partial_{x} and ∂ y \partial_{y} for the partial derivatives of ϕ 2 ​ ( t, ( x, y)). \phi_{2}(t,(x,y)). In doing so we obtain

 | ρ 1 ​ ( z) = ∂ s ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) | s = 0 = \displaystyle\rho_{1}(z)=\left.\partial_{s}\phi_{2}\big(z-\xi_{1}(s),\xi(s)\big)\right|_{s=0}= | − ∂ t ϕ 2 ( z − ξ 1 ( s), ξ ( s)) ξ 1 ′ ( s) \displaystyle-\partial_{t}\phi_{2}(z-\xi_{1}(s),\xi(s))\xi_{1}^{\prime}(s) |  |

 |  | + ∂ x ϕ 2 ( z − ξ 1 ( s), ξ ( s)) ξ 1 ′ ( s) + ∂ y ϕ 2 ( z − ξ 1 ( s), ξ ( s)) ξ 2 ′ ( s) | s = 0 \displaystyle+\left.\partial_{x}\phi_{2}(z-\xi_{1}(s),\xi(s))\xi_{1}^{\prime}(s)+\partial_{y}\phi_{2}(z-\xi_{1}(s),\xi(s))\xi_{2}^{\prime}(s)\right|_{s=0} |  |

 | = \displaystyle= | − ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) ​ h ​ ( z, ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s))) ​ ξ 1 ′ ​ ( s) \displaystyle-\phi_{2}(z-\xi_{1}(s),\xi(s))h\big(z,\phi_{2}(z-\xi_{1}(s),\xi(s))\big)\xi_{1}^{\prime}(s) |  |

 |  | + ∂ x ϕ 2 ( z − ξ 1 ( s), ξ ( s)) ξ 1 ′ ( s) + ∂ y ϕ 2 ( z − ξ 1 ( s), ξ ( s)) ξ 2 ′ ( s) | s = 0 \displaystyle\left.+\partial_{x}\phi_{2}(z-\xi_{1}(s),\xi(s))\xi_{1}^{\prime}(s)+\partial_{y}\phi_{2}(z-\xi_{1}(s),\xi(s))\xi_{2}^{\prime}(s)\right|_{s=0} |  | (44) |

 | = \displaystyle= | ξ 21 ​ H ​ ( z, ξ 1 ​ s), \displaystyle\,\xi_{21}H(z,\xi_{1s}), |  |

where in the third equality we use that ϕ \phi is the flow of Z ν = ∂ x + y h ( x, y; ν) ∂ y Z_{\nu}=\partial_{x}+yh(x,y;\nu)\partial_{y} and in the fourth one that ϕ 2 ​ ( x − ξ 1 ​ ( 0), ξ ⁡ ( 0)) = 0 \phi_{2}(x-\xi_{1}(0),\xi(0))=0 due to ξ 2 ​ ( 0) = 0 \xi_{2}(0)=0, together with ∂ x ϕ 2 ​ ( t, ( x, 0)) = 0 \partial_{x}\phi_{2}(t,(x,0))=0 and ∂ y ϕ 2 ​ ( t, ( x, 0)) = H ⁡ ( x + t, x) \partial_{y}\phi_{2}(t,(x,0))=H(x+t,x), as established by Lemma A.1.

Next we proceed with the computation of ρ 2 ​ ( z). \rho_{2}(z). With this aim in view note that, from ( A) (\ref{L2eq1}\immediate),

 | ρ 2 ​ ( z) = ∂ s ​ s 2 ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) | s = 0 = \displaystyle\rho_{2}(z)=\left.\partial_{ss}^{2}\phi_{2}(z-\xi_{1}(s),\xi(s))\right|_{s=0}= | − ξ 11 h ( z, 0) ∂ s ϕ 2 ( z − ξ 1 ( s), ξ ( s)) + ξ 11 ∂ s ∂ x ϕ 2 ( z − ξ 1 ( s), ξ ( s)) \displaystyle-\xi_{11}h(z,0)\partial_{s}\phi_{2}\big(z-\xi_{1}(s),\xi(s)\big)+\xi_{11}\partial_{s}\partial_{x}\phi_{2}(z-\xi_{1}(s),\xi(s)) |  |

 |  | + ∂ s ( ∂ y ϕ 2 ( z − ξ 1 ( s), ξ ( s)) ξ 2 ′ ( s)) | s = 0. \displaystyle+\left.\partial_{s}\Big(\partial_{y}\phi_{2}(z-\xi_{1}(s),\xi(s))\xi_{2}^{\prime}(s)\Big)\right|_{s=0}. |  | (45) |

By applying Lemma A.1, some computations show that

 | ∂ s ∂ x ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) | s = 0 \displaystyle\left.\partial_{s}\partial_{x}\phi_{2}(z-\xi_{1}(s),\xi(s))\right|_{s=0} | = ξ 11 ( − ∂ t ∂ x ϕ 2 + ∂ x ​ x 2 ϕ 2) ( z − ξ 10, ( ξ 10, 0)) + ξ 21 ∂ x ​ y 2 ϕ 2 ( z − ξ 10, ( ξ 10, 0)) \displaystyle=\xi_{11}\Big(-\partial_{t}\partial_{x}\phi_{2}+\partial_{xx}^{2}\phi_{2}\Big)(z-\xi_{10},(\xi_{10},0))+\xi_{21}\partial_{xy}^{2}\phi_{2}(z-\xi_{10},(\xi_{10},0)) |  |

 |  | = ξ 21 ​ H ​ ( z, ξ 10) ​ ( h ⁡ ( z, 0) − h ⁡ ( ξ 10, 0)). \displaystyle=\xi_{21}H(z,\xi_{10})\big(h(z,0)-h(\xi_{10},0)\big). |  |

and |

 | ∂ s ∂ y ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) | s = 0 \displaystyle\left.\partial_{s}\partial_{y}\phi_{2}(z-\xi_{1}(s),\xi(s))\right|_{s=0} | = ξ 11 ( − ∂ t ∂ y ϕ 2 + ∂ x ​ y 2 ϕ 2) ( z − ξ 10, ( ξ 10, 0)) + ξ 21 ∂ y ​ y 2 ϕ 2 ( z − ξ 10, ( ξ 10, 0)) \displaystyle=\xi_{11}\Big(-\partial_{t}\partial_{y}\phi_{2}+\partial_{xy}^{2}\phi_{2}\Big)(z-\xi_{10},(\xi_{10},0))+\xi_{21}\partial_{yy}^{2}\phi_{2}(z-\xi_{10},(\xi_{10},0)) |  |

 |  | = H ⁡ ( z, ξ 10) ​ ( − ξ 11 ​ h ​ ( ξ 10, 0) + 2 ​ ξ 21 ​ ∫ ξ 10 z H ⁡ ( u, ξ 10) ​ ∂ 2 h ⁡ ( u, 0) ​ 𝑑 u). \displaystyle=H(z,\xi_{10})\left(-\xi_{11}h(\xi_{10},0)+2\xi_{21}\int_{\xi_{10}}^{z}H(u,\xi_{10})\partial_{2}h(u,0)du\right). |  |

Since ∂ s ϕ 2 ​ ( z − ξ 1 ​ ( s), ξ ⁡ ( s)) | s = 0 = ∂ y ϕ 2 ​ ( z − ξ 1 ​ ( 0), ξ ⁡ ( 0)) ​ ξ 2 ′ ​ ( 0) = ξ 21 ​ H ​ ( z, ξ 10) \left.\partial_{s}\phi_{2}\big(z-\xi_{1}(s),\xi(s)\big)\right|_{s=0}=\partial_{y}\phi_{2}\big(z-\xi_{1}(0),\xi(0)\big)\xi_{2}^{\prime}(0)=\xi_{21}H(z,\xi_{10}) by Lemma A.1 once again, the substitution of the two previous identities in ( 45) (\ref{L2eq2}\immediate) yields

 | ρ 2 ​ ( z) = H ⁡ ( z, ξ 10) ​ ( ξ 22 − 2 ​ ξ 11 ​ ξ 21 ​ h ​ ( ξ 10, 0) + 2 ​ ξ 21 2 ​ ∫ ξ 10 z H ⁡ ( u, ξ 10) ​ ∂ 2 h ⁡ ( u, 0) ​ 𝑑 u), \rho_{2}(z)=H(z,\xi_{10})\left(\xi_{22}-2\xi_{11}\xi_{21}h(\xi_{10},0)+2\xi_{21}^{2}\int_{\xi_{10}}^{z}H(u,\xi_{10})\partial_{2}h(u,0)du\right), |  |

as desired. Hence the result is proved.

We are now in position to give the two first non-trivial coefficients of the transition map P ⁡ ( ⋅, ν) P(\,\cdot\,;\nu) and the transition time T ⁡ ( ⋅, ν) T(\,\cdot\,;\nu) between Π 1 \Pi_{1} and Π 2. \Pi_{2}. In this regard it is to be quoted a previous result by Chicone (see [8, Theorem 2.2]), where it is given the expression of ∂ s P ⁡ ( 0, ν) \partial_{s}P(0;\nu) for vector fields in general position, i.e., not assuming that the straight line { y = 0 } \{y=0\} is invariant. He also gives the formula of ∂ s T ⁡ ( 0, ν) \partial_{s}T(0;\nu) in the case that ℓ = 0. \ell=0. More recently, explicit formulas of ∂ s P ⁡ ( 0, ν) \partial_{s}P(0;\nu) and also ∂ s ​ s P ⁡ ( 0, ν) \partial_{ss}P(0;\nu) for vector fields in general position are given in [16, Theorem 4.2]. The proofs in [8, 16] are based on Diliberto’s theorem on the integration of the homogeneous variational equations of a plane autonomous differential system in terms of geometric quantities along a given trajectory. (Similar results for the transition map can be found in the book of Andronov et al. [1].) In our next lemma, besides these coefficients, we also give the second coefficient of the transition time, which to the best of our knowledge constitutes a new result. The lemma is in fact an upgrade of [23, Lemma 2.4], where we study the regularity properties of these maps without giving the expression of the coefficients. In the statement for the sake of shortness we use the compact notation ξ i ​ k = ξ i ( k) ​ ( 0) \xi_{ik}=\xi_{i}^{(k)}(0) and ζ i ​ k = ζ i ( k) ​ ( 0) \zeta_{ik}=\zeta_{i}^{(k)}(0), i = 1, 2 i=1,2, for the derivatives of the parametrization of the transverse sections. We also remark that the functions ρ 1 \rho_{1} and ρ 2 \rho_{2} appearing in these coefficients are the ones given in Lemma A.2.

###### Lemma A.3.

? ⟨ \langle L3 ⟩ \rangle?

Let P ⁡ ( s, ν) P(s;\nu) and T ⁡ ( s, ν) T(s;\nu) be respectively the transition map and transition time of the flow given by ( 42) (\ref{ap1}\hbox{}) between the transverse sections ξ ⁡ ( ⋅, ν): ( − ε, ε) ⟶ Π 1 {\xi(\,\cdot\,;\nu)}\!:{(-\varepsilon,\varepsilon)}\longrightarrow{\Pi_{1}} and ζ ⁡ ( ⋅, ν): ( − ε, ε) ⟶ Π 2 {\zeta(\,\cdot\,;\nu)}\!:{(-\varepsilon,\varepsilon)}\longrightarrow{\Pi_{2}} to { y = 0 } \{y=0\}. Then the following hold:

1. ( a) (a)

The function P ⁡ ( s, ν) P(s;\nu) is 𝒞 K \mathscr{C}^{K} on ( ( − ε, ε) × U) \big((-\varepsilon,\varepsilon)\times U\big). Moreover P ⁡ ( 0, ν) = 0, P(0;\nu)=0,

 |  | p 1 ​ ( ν):= ∂ s P ⁡ ( 0, ν) = ξ 21 ζ 21 ​ exp ⁡ ( ∫ ξ 10 ζ 10 h ⁡ ( u, 0) ​ 𝑑 u) \displaystyle p_{1}(\nu)\!:=\partial_{s}P(0;\nu)=\frac{\xi_{21}}{\zeta_{21}}\exp\left(\int_{\xi_{10}}^{\zeta_{10}}h(u,0)du\right) |  |

and |

 |  | p 2 ​ ( ν):= ∂ s ​ s 2 P ⁡ ( 0, ν) = ( 2 ​ ζ 11 ​ ζ 21 ​ h ​ ( ζ 10, 0) − ζ 22) ​ p 1 2 + ρ 2 ​ ( ζ 10) ζ 21. \displaystyle p_{2}(\nu)\!:=\partial_{ss}^{2}P(0;\nu)=\frac{\big(2\zeta_{11}\zeta_{21}h(\zeta_{10},0)-\zeta_{22}\big)p_{1}^{2}+\rho_{2}(\zeta_{10})}{\zeta_{21}}. |  |

2. ( b) (b)

T ⁡ ( s, ν) = s ℓ ​ T ~ ​ ( s, ν) T(s;\nu)=s^{{\ell}}\tilde{T}(s;\nu) with T ~ ∈ 𝒞 K − 1 ​ ( ( − ε, ε) × U) \tilde{T}\in\mathscr{C}^{K-1}\big((-\varepsilon,\varepsilon)\times U\big) verifying T ~ ​ ( 0, ν) = ∫ ξ 10 ζ 10 ρ 1 ℓ ​ ( x) ​ f ​ ( x, 0) ​ 𝑑 x \tilde{T}(0;\nu)=\displaystyle\int_{\xi_{10}}^{\zeta_{10}}\!\!\rho_{1}^{{\ell}}(x)f(x,0)dx and

 | ∂ s T ~ ​ ( 0, ν) = \displaystyle\partial_{s}\tilde{T}(0;\nu)= | ζ 11 ​ ζ 21 ℓ ​ p 1 ℓ + 1 ​ f ​ ( ζ 10, 0) − ξ 11 ​ ξ 21 ℓ ​ f ​ ( ξ 10, 0) \displaystyle\,\zeta_{11}\zeta_{21}^{{\ell}}p_{1}^{{{\ell}}+1}f(\zeta_{10},0)-\xi_{11}\xi_{21}^{{\ell}}f(\xi_{10},0) |  |

 |  | + 1 2 ∫ ξ 10 ζ 10 ρ 1 ℓ − 1 ( x) ( ℓ ρ 2 ( x) f ( x, 0) + 2 ρ 1 2 ( x) ∂ 2 f ( x, 0)) d x. \displaystyle+\frac{1}{2}\int_{\xi_{10}}^{\zeta_{10}}\!\!\rho_{1}^{{{\ell}}-1}(x)\Big({{\ell}}\rho_{2}(x)f(x,0)+2\rho_{1}^{2}(x)\partial_{2}f(x,0)\Big)dx. |  |

Moreover if ℓ = 0 {{\ell}}=0 then T ∈ 𝒞 K ​ ( ( − ε, ε) × U) T\in\mathscr{C}^{K}\big((-\varepsilon,\varepsilon)\times U\big) and

 | ∂ s ​ s 2 T ⁡ ( 0, ν) = \displaystyle\partial_{ss}^{2}T(0;\nu)= | ( ζ 12 ​ p 1 2 + ζ 11 ​ p 2) ​ f ​ ( ζ 10, 0) + ζ 11 2 ​ p 1 2 ​ ∂ 1 f ⁡ ( ζ 10, 0) + 2 ​ ζ 11 ​ ζ 21 ​ p 1 2 ​ ∂ 2 f ⁡ ( ζ 10, 0) \displaystyle\,\big(\zeta_{12}p_{1}^{2}+\zeta_{11}p_{2}\big)f(\zeta_{10},0)+\zeta_{11}^{2}p_{1}^{2}\partial_{1}f(\zeta_{10},0)+2\zeta_{11}\zeta_{21}p_{1}^{2}\partial_{2}f(\zeta_{10},0) |  |

 |  | − ξ 12 ​ f ​ ( ξ 10, 0) − ξ 11 2 ​ ∂ 1 f ⁡ ( ξ 10, 0) − 2 ​ ξ 11 ​ ξ 21 ​ ∂ 2 f ⁡ ( ξ 10, 0) \displaystyle-\xi_{12}f(\xi_{10},0)-\xi_{11}^{2}\partial_{1}f(\xi_{10},0)-2\xi_{11}\xi_{21}\partial_{2}f(\xi_{10},0) |  |

 |  | + ∫ ξ 10 ζ 10 ( ρ 1 2 ( x) ∂ 22 2 f ( x, 0) + ρ 2 ( x) ∂ 2 f ( x, 0)) d x. \displaystyle+\int_{\xi_{10}}^{\zeta_{10}}\Big(\rho_{1}^{2}(x)\partial_{22}^{2}f(x,0)+\rho_{2}(x)\partial_{2}f(x,0)\Big)dx. |  |

The assertion concerning the smoothness of P ⁡ ( s, ν) P(s;\nu) follows by the smooth dependence of solutions with respect to initial conditions and parameters and the application of the implicit function theorem (see for instance [9, Theorem 1.1]). Note on the other hand that, by definition, φ ⁡ ( T ⁡ ( s), ξ ⁡ ( s)) = ζ ⁡ ( P ⁡ ( s)) \varphi(T(s),\xi(s))=\zeta(P(s)) where φ ⁡ ( t, p 0) \varphi(t,p_{0}) is solution of Y ν Y_{\nu} with initial condition p 0 ∈ V. p_{0}\in V. Since Z ν = y ℓ f ( x, y; ν) Y ν = ∂ x + y h ( x, y) ∂ y Z_{\nu}=y^{\ell}f(x,y;\nu)Y_{\nu}=\partial_{x}+yh(x,y)\partial_{y}, it follows that

 | ζ 2 ​ ( P ⁡ ( s)) = ϕ 2 ​ ( ζ 1 ​ ( P ⁡ ( s)) − ξ 1 ​ ( s), ξ ⁡ ( s)) = Ω ⁡ ( ζ 1 ​ ( P ⁡ ( s)), s), \zeta_{2}(P(s))=\phi_{2}\big(\zeta_{1}(P(s))-\xi_{1}(s),\xi(s)\big)=\Omega\big(\zeta_{1}(P(s)),s\big), |  |

where ϕ ⁡ ( t, ( x, y)) = ( t + x, ϕ 2 ​ ( t, ( x, y)) CLOSE \phi(t,(x,y))=(t+x,\phi_{2}(t,(x,y)) is the flow of Z ν Z_{\nu} and, by definition, Ω ⁡ ( x, s) = ϕ 2 ​ ( x − ξ 1 ​ ( s), ξ ⁡ ( s)). \Omega(x,s)=\phi_{2}(x-\xi_{1}(s),\xi(s)). Accordingly

 | ζ 2 ′ ​ ( P ⁡ ( s)) ​ P ′ ​ ( s) = ∂ 1 Ω ⁡ ( ζ 1 ​ ( P ⁡ ( s)), s) ​ ζ 1 ′ ​ ( P ⁡ ( s)) ​ P ′ ​ ( s) + ∂ 2 Ω ⁡ ( ζ 1 ​ ( P ⁡ ( s)), s), \zeta_{2}^{\prime}(P(s))P^{\prime}(s)=\partial_{1}\Omega\big(\zeta_{1}(P(s)),s\big)\zeta_{1}^{\prime}(P(s))P^{\prime}(s)+\partial_{2}\Omega\big(\zeta_{1}(P(s)),s\big), |  |

which, evaluated at s = 0 s=0 and applying Lemma A.2, gives ζ 21 ​ P ′ ​ ( 0) = ∂ 2 Ω ⁡ ( ζ 10, 0) = ρ 1 ​ ( ζ 10) = ξ 21 ​ H ​ ( ζ 10, ξ 10). \zeta_{21}P^{\prime}(0)=\partial_{2}\Omega(\zeta_{10},0)=\rho_{1}(\zeta_{10})=\xi_{21}H(\zeta_{10},\xi_{10}). Therefore p 1 = P ′ ​ ( 0) = ξ 21 ζ 21 ​ H ​ ( ζ 10, ξ 10), p_{1}=P^{\prime}(0)=\frac{\xi_{21}}{\zeta_{21}}H(\zeta_{10},\xi_{10}), as desired. By computing an additional derivative with respect to s s in the above equality and evaluating at s = 0 s=0 afterwards we get

 | ζ 22 ​ p 1 2 + ζ 21 ​ P ′′ ​ ( 0) = 2 ​ ∂ 12 2 Ω ⁡ ( ζ 10, 0) ​ ζ 11 ​ p 1 + ∂ 22 2 Ω ⁡ ( ζ 10, 0) = 2 ​ ρ 1 ​ ( ζ 10) ​ h ​ ( ζ 10, 0) ​ ζ 11 ​ p 1 + ρ 2 ​ ( ζ 10), \zeta_{22}p_{1}^{2}+\zeta_{21}P^{\prime\prime}(0)=2\partial_{12}^{2}\Omega(\zeta_{10},0)\zeta_{11}p_{1}+\partial_{22}^{2}\Omega(\zeta_{10},0)=2\rho_{1}(\zeta_{10})h(\zeta_{10},0)\zeta_{11}p_{1}+\rho_{2}(\zeta_{10}), |  |

where we apply Lemma A.2 and take ρ 1 ′ ​ ( ζ 10) = ξ 21 ​ ∂ 1 H ⁡ ( ζ 10, ξ 10) = ξ 21 ​ H ​ ( ζ 10, ξ 10) ​ h ​ ( ζ 10, 0) = ζ 21 ​ p 1 ​ h ​ ( ζ 10, 0) \rho_{1}^{\prime}(\zeta_{10})=\xi_{21}\partial_{1}H(\zeta_{10},\xi_{10})=\xi_{21}H(\zeta_{10},\xi_{10})h(\zeta_{10},0)=\zeta_{21}p_{1}h(\zeta_{10},0) into account. Consequently,

 | P ′′ ​ ( 0) = p 2 = ( 2 ​ ζ 11 ​ ζ 21 ​ h ​ ( ζ 10, 0) − ζ 22) ​ p 1 2 + ρ 2 ​ ( ζ 10) ζ 21 P^{\prime\prime}(0)=p_{2}=\frac{\big(2\zeta_{11}\zeta_{21}h(\zeta_{10},0)-\zeta_{22}\big)p_{1}^{2}+\rho_{2}(\zeta_{10})}{\zeta_{21}} |  |

and this proves ( a) (a). Let us turn now to the proof of the assertions in ( b) (b). With this aim we note first that the transition time between Π 1 \Pi_{1} and Π 2 \Pi_{2} has the following integral expression

 | T ⁡ ( s) = ∫ ξ 1 ​ ( s) ζ 1 ​ ( P ​ ( s)) Ω ​ ( x, s) ℓ ​ f ​ ( x, Ω ⁡ ( x, s)) ​ 𝑑 x. T(s)=\int_{\xi_{1}(s)}^{\zeta_{1}(P(s))}\Omega(x,s)^{{\ell}}f(x,\Omega(x,s))dx. |  |

By Lemma A.2 we know that Ω \Omega is a 𝒞 K \mathscr{C}^{K} function such that Ω ⁡ ( x, 0) = 0 \Omega(x,0)=0 and ∂ 2 Ω ⁡ ( x, 0) = ρ 1 ​ ( x) \partial_{2}\Omega(x,0)=\rho_{1}(x). Hence, the application of Lemma 2.1 shows that Ω ⁡ ( x, s) = s ⁡ ( ρ 1 ​ ( x) + R ⁡ ( x, s)) \Omega(x,s)=s(\rho_{1}(x)+R(x,s)) for some 𝒞 K − 1 \mathscr{C}^{K-1} function R R with R ⁡ ( x, 0) = 0 R(x,0)=0. Accordingly T ⁡ ( s) = s ℓ ​ T ~ ​ ( s) T(s)=s^{{\ell}}\tilde{T}(s) with

 | T ~ ​ ( s):= ∫ ξ 1 ​ ( s) ζ 1 ​ ( P ​ ( s)) ( ρ 1 ​ ( x) + R ⁡ ( x, s)) ℓ ​ f ​ ( x, Ω ⁡ ( x, s)) ​ 𝑑 x. \tilde{T}(s)\!:=\int_{\xi_{1}(s)}^{\zeta_{1}(P(s))}(\rho_{1}(x)+R(x,s))^{{\ell}}f(x,\Omega(x,s))dx. |  |

Then, since ρ 1 \rho_{1} does not vanish, by a well-known result on the regularity properties of integrals depending on parameters (see [34, page 411]) it follows that T ~ \tilde{T} is 𝒞 K − 1 \mathscr{C}^{K-1} as well. Let us compute now T ~ ​ ( 0) \tilde{T}(0) and T ~ ′ ​ ( 0) \tilde{T}^{\prime}(0). This is easy for the first one because T ~ ​ ( 0) = ∫ ξ 10 ζ 10 ρ 1 ℓ ​ ( x) ​ f ​ ( x, 0) ​ 𝑑 x. \tilde{T}(0)=\int_{\xi_{10}}^{\zeta_{10}}\rho_{1}^{{\ell}}(x)f(x,0)dx. Concerning the second one we note that

 | T ~ ′ ​ ( 0) = ρ 1 ℓ ​ ( ζ 10) ​ f ​ ( ζ 10, 0) ​ ζ 11 ​ p 1 − ρ 1 ℓ ​ ( ξ 10) ​ f ​ ( ξ 10, 0) ​ ξ 11 + ∫ ξ 10 ζ 10 ρ 1 ℓ − 1 ​ ( x) ​ ( 1 2 ​ ℓ ​ ρ 2 ​ ( x) ​ f ​ ( x, 0) + ∂ 2 f ⁡ ( x, 0) ​ ρ 1 2 ​ ( x)) ​ 𝑑 x. \tilde{T}^{\prime}(0)=\rho_{1}^{{\ell}}(\zeta_{10})f(\zeta_{10},0)\zeta_{11}p_{1}-\rho_{1}^{{\ell}}(\xi_{10})f(\xi_{10},0)\xi_{11}+\int^{\zeta_{10}}_{\xi_{10}}\!\!\rho_{1}^{{{\ell}}-1}(x)\left(\frac{1}{2}{{\ell}}\rho_{2}(x)f(x,0)+\partial_{2}f(x,0)\rho_{1}^{2}(x)\right)dx. |  |

Here we use that, thanks to Lemma A.2, ∂ s R ⁡ ( x, 0) = 1 2 ​ ∂ 22 2 Ω ⁡ ( x, 0) = 1 2 ​ ρ 2 ​ ( x). \partial_{s}R(x,0)=\frac{1}{2}\partial_{22}^{2}\Omega(x,0)=\frac{1}{2}\rho_{2}(x). Now, taking ρ 1 ​ ( ξ 10) = ξ 21 \rho_{1}(\xi_{10})=\xi_{21} and ρ 1 ​ ( ζ 10) = ζ 21 ​ p 1 \rho_{1}(\zeta_{10})=\zeta_{21}p_{1} into account, one can verify that the above expression is equal to the one given in the statement. Hence it only remains to prove the assertions concerning the case ℓ = 0. {{\ell}}=0. The fact that if ℓ = 0 {{\ell}}=0 then T T is 𝒞 K \mathscr{C}^{K} follows from the regularity properties of integrals depending on parameters that we mention above. With regard to the expression of T ′′ ​ ( 0) T^{\prime\prime}(0) we note that if ℓ = 0 \ell=0 then

 | T ′ ​ ( s) = \displaystyle T^{\prime}(s)= | f ⁡ ( ζ 1 ​ ( P ⁡ ( s)), Ω ⁡ ( ζ 1 ​ ( P ⁡ ( s)), s)) ​ ζ 1 ′ ​ ( P ⁡ ( s)) ​ P ′ ​ ( s) − f ⁡ ( ξ 1 ​ ( s), Ω ⁡ ( ξ 1 ​ ( s), s)) ​ ξ 1 ′ ​ ( s) \displaystyle f\big(\zeta_{1}(P(s)),\Omega(\zeta_{1}(P(s)),s)\big)\zeta_{1}^{\prime}(P(s))P^{\prime}(s)-f\big(\xi_{1}(s),\Omega(\xi_{1}(s),s)\big)\xi_{1}^{\prime}(s) |  |

 |  | + ∫ ξ 1 ​ ( s) ζ 1 ​ ( P ​ ( s)) ∂ 2 f ( x, Ω ( x, s)) ∂ 2 Ω ( x, s) d x. \displaystyle+\int_{\xi_{1}(s)}^{\zeta_{1}(P(s))}\partial_{2}f(x,\Omega(x,s))\partial_{2}\Omega(x,s)dx. |  |

Accordingly, since ∂ 1 Ω ⁡ ( x, 0) = 0 \partial_{1}\Omega(x,0)=0, ∂ 2 Ω ⁡ ( x, 0) = ρ 1 ​ ( x) \partial_{2}\Omega(x,0)=\rho_{1}(x) and ∂ 22 2 Ω ⁡ ( x, 0) = ρ 2 ​ ( x) \partial_{22}^{2}\Omega(x,0)=\rho_{2}(x), some easy computations give

 | T ′′ ​ ( 0) = \displaystyle T^{\prime\prime}(0)= | ∂ 1 f ⁡ ( ζ 10, 0) ​ ζ 11 2 ​ p 1 2 + 2 ​ ∂ 2 f ⁡ ( ζ 10, 0) ​ ρ 1 ​ ( ζ 10) ​ ζ 11 ​ p 1 + f ⁡ ( ζ 10, 0) ​ ( ζ 12 ​ p 1 2 + 2 ​ ζ 11 ​ p 2) \displaystyle\,\partial_{1}f(\zeta_{10},0)\zeta_{11}^{2}p_{1}^{2}+2\partial_{2}f(\zeta_{10},0)\rho_{1}(\zeta_{10})\zeta_{11}p_{1}+f(\zeta_{10},0)\big(\zeta_{12}p_{1}^{2}+2\zeta_{11}p_{2}\big) |  |

 |  | − ∂ 1 f ( ξ 10, 0) ξ 11 2 − 2 ∂ 2 f ( ξ 10, 0) ρ 1 ( ξ 10) ξ 11 − f ( ξ 10, 0) ξ 12 \displaystyle-\partial_{1}f(\xi_{10},0)\xi_{11}^{2}-2\partial_{2}f(\xi_{10},0)\rho_{1}(\xi_{10})\xi_{11}-f(\xi_{10},0)\xi_{12} |  |

 |  | + ∫ ξ 10 ζ 10 ( ∂ 22 2 f ( x, 0) ρ 1 2 ( x) + ρ 2 ( x) ∂ 2 f ( x, 0)) d x. \displaystyle+\int^{\zeta_{10}}_{\xi_{10}}\Big(\partial_{22}^{2}f(x,0)\rho_{1}^{2}(x)+\rho_{2}(x)\partial_{2}f(x,0)\Big)dx. |  |

Finally the substitution of ρ 1 ​ ( ξ 10) = ξ 21 \rho_{1}(\xi_{10})=\xi_{21} and ρ 1 ​ ( ζ 10) = ζ 21 ​ p 1 \rho_{1}(\zeta_{10})=\zeta_{21}p_{1} yields to the expression of T ′′ ​ ( 0) T^{\prime\prime}(0) given in the statement. This concludes the proof of the result.

## Appendix B An incomplete Mellin transform

In this appendix we introduce a sort of incomplete Mellin transform that is a key tool for giving a closed expression for the coefficients of the first monomials in the asymptotic expansion of the Dulac map and Dulac time. In short, given α ∈ ℝ ∖ ℤ ≥ 0 \alpha\in\mathbb{R}\setminus\mathbb{Z}_{\geq 0} and a smooth function f ⁡ ( x) f(x) on an open interval I I that contains x = 0 x=0, we consider the singular scalar differential equation

 | x ​ y ′ − α ​ y = f ⁡ ( x). xy^{\prime}-\alpha y=f(x). |  |

It turns out that this differential equation has for each α \alpha a unique solution y = f ^ ​ ( α, x) y=\hat{f}(\alpha,x) which is smooth on I I. As we will see, the fact that 0 ∈ I 0\in I turns out to be crucial for the uniqueness. The idea is to relate this particular solution with the trajectories of the autonomous planar differential system

 | { x ˙ = x, y ˙ = α ​ y + f ⁡ ( x), \left\{\!\begin{array}[]{l}\dot{x}=x,\\[2.0pt] \dot{y}=\alpha y+f(x),\end{array}\right. |  |

that has a hyperbolic critical point at ( 0, − f ( 0) / α) (0,-f(0)/\alpha) being a saddle for α < 0 \alpha<0 and a focus for α > 0. \alpha>0. In the saddle case, which is the simplest one, y = f ^ ​ ( α, x) y=\hat{f}(\alpha,x) is no more than the graph of the stable separatrix. This is in fact the idea in the proof of our next result, which is a little more complicated than it should be because in our applications f f depends on parameters and we need good regularity properties of the solution with respect to α \alpha and these parameters as well. For that purpose we apply the so-called center-stable manifold theorem (see for instance [14, Theorem 1]) but instead one may use the parametrization method for invariant manifolds (see [6, 7]).

###### Theorem B.1.

? ⟨ \langle L8 ⟩ \rangle?

Let us consider an open interval I I of ℝ \mathbb{R} containing x = 0 x=0 and an open subset U U of ℝ N \mathbb{R}^{N}.

1. ( a) (a)

Given f ⁡ ( x, ν) ∈ 𝒞 ∞ ​ ( I × U) f(x;\nu)\in\mathscr{C}^{\infty}(I\times U), there exits a unique f ^ ​ ( α, x, ν) ∈ 𝒞 ∞ ​ ( ( ℝ ∖ ℤ ≥ 0) × I × U) \hat{f}(\alpha,x;\nu)\in\mathscr{C}^{\infty}((\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I\times U) such that

 | x ​ ∂ x f ^ ​ ( α, x, ν) − α ​ f ^ ​ ( α, x, ν) = f ⁡ ( x, ν). x\partial_{x}\hat{f}({\alpha},x;\nu)-\alpha\hat{f}({\alpha},x;\nu)=f(x;\nu). |  | (46) |

2. ( b) (b)

If x ∈ I ∖ { 0 } x\in I\setminus\{0\} then ∂ x ( f ^ ​ ( α, x, ν) ​ | x | − α) = f ⁡ ( x, ν) ​ | x | − α x \partial_{x}(\hat{f}({\alpha},x;\nu)|x|^{-\alpha})=f(x;\nu)\frac{|x|^{-\alpha}}{x} and, taking any k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0} with k > α k>\alpha,

 | f ^ ​ ( α, x, ν) = ∑ i = 0 k − 1 ∂ x i f ⁡ ( 0, ν) i! ​ ( i − α) ​ x i + | x | α ​ ∫ 0 x ( f ⁡ ( s, ν) − T 0 k − 1 ​ f ​ ( s, ν)) ​ | s | − α ​ d ​ s s, \hat{f}(\alpha,x;\nu)=\sum_{i=0}^{k-1}\frac{\partial_{x}^{i}f(0;\nu)}{i!(i-\alpha)}x^{i}+|x|^{\alpha}\int_{0}^{x}\!\left(f(s;\nu)-T_{0}^{k-1}f(s;\nu)\right)|s|^{-\alpha}\frac{ds}{s}, |  | (47) |

where T 0 k ​ f ​ ( x, ν) = ∑ i = 0 k 1 i! ​ ∂ x i f ⁡ ( 0, ν) ​ x i T_{0}^{k}f(x;\nu)=\sum_{i=0}^{k}\frac{1}{i!}\partial_{x}^{i}f(0;\nu)x^{i} is the k k -th degree Taylor polynomial of f ⁡ ( x, ν) f(x;\nu) at x = 0 x=0.

3. ( c) (c)

For each ( i 0, x 0, ν 0) ∈ ℤ ≥ 0 × I × W (i_{0},x_{0},\nu_{0})\in\mathbb{Z}_{\geq 0}\times I\times W the function ( α, x, ν) ↦ ( i 0 − α) ​ f ^ ​ ( α, x, ν) (\alpha,x,\nu)\mapsto(i_{0}-\alpha)\hat{f}(\alpha,x;\nu) extends 𝒞 ∞ \mathscr{C}^{\infty} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) and, moreover, it tends to 1 i 0! ​ ∂ x i 0 f ⁡ ( 0, ν 0) ​ x 0 i 0 \frac{1}{i_{0}!}\partial_{x}^{i_{0}}f(0;\nu_{0})x_{0}^{i_{0}} as ( α, x, ν) → ( i 0, x 0, ν 0). (\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0}).

4. ( d) (d)

If f ⁡ ( x, ν) f(x;\nu) is analytic on I × U I\times U then f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) is analytic on ( ℝ ∖ ℤ ≥ 0) × I × U (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I\times U. Finally, for each ( α 0, x 0, ν 0) ∈ ℤ ≥ 0 × I × U (\alpha_{0},x_{0},\nu_{0})\in\mathbb{Z}_{\geq 0}\times I\times U the function ( α, x, ν) ↦ ( α 0 − α) ​ f ^ ​ ( α, x, ν) (\alpha,x,\nu)\mapsto(\alpha_{0}-\alpha)\hat{f}(\alpha,x;\nu) extends analytically to ( α 0, x 0, ν 0) (\alpha_{0},x_{0},\nu_{0}).

The plan to prove ( a) (a) is the following. The uniqueness will be proved firstly. We will show, secondly, the existence for α < 0 \alpha<0 and, thirdly, the existence for α > 0 \alpha>0.

To prove the uniqueness let us suppose that, for some α ∉ ℤ ≥ 0 \alpha\notin\mathbb{Z}_{\geq 0}, the differential equation x ​ y ′ − α ​ y = f ⁡ ( x, ν) xy^{\prime}-\alpha y=f(x;\nu) has two solutions, y = f ^ 1 ​ ( α, x, ν) y=\hat{f}_{1}(\alpha,x;\nu) and y = f ^ 2 ​ ( α, x, ν) y=\hat{f}_{2}(\alpha,x;\nu), that are 𝒞 ∞ \mathscr{C}^{\infty} on ( ℝ ∖ ℤ ≥ 0) × I × U (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I\times U. Then f ^ 1 − f ^ 2 \hat{f}_{1}-\hat{f}_{2} is a smooth function that verifies the homogeneous linear differential equation x ​ y ′ − α ​ y = 0 xy^{\prime}-\alpha y=0 which, in the case that α ∉ ℤ ≥ 0 \alpha\notin\mathbb{Z}_{\geq 0}, has y = 0 y=0 as unique 𝒞 ∞ \mathscr{C}^{\infty} solution passing through x = 0. x=0. Consequently f ^ 1 = f ^ 2, \hat{f}_{1}=\hat{f}_{2}, as desired.

Let us prove now the existence for the case α < 0. \alpha<0. To this end, related with the scalar differential equation in ( 46) (\ref{Mellin-eq}\immediate), note that the planar vector field x ∂ x + ( α y + f ( x; ν)) ∂ y x\partial_{x}+(\alpha y+f(x;\nu))\partial_{y} has, for each fixed α < 0 \alpha<0 and ν ∈ U \nu\in U, a hyperbolic saddle at ( 0, − f ( 0; ν) / α) (0,-f(0;\nu)/\alpha) with a non-vertical stable separatrix. In order to study its regularity with respect to the parameters we consider the augmented system

 | { x ˙ = x, y ˙ = α ​ y + f ⁡ ( x, ν), α ˙ = 0, ν ˙ = 0. \left\{\!\begin{array}[]{l}\dot{x}=x,\\[2.0pt] \dot{y}=\alpha y+f(x;\nu),\\[2.0pt] \dot{\alpha}=0,\\[2.0pt] \dot{\nu}=0.\end{array}\right. |  |

For each fixed α 0 ∈ ( − ∞, 0) \alpha_{0}\in(-\infty,0) and ν 0 ∈ U, \nu_{0}\in U, the application of [14, Theorem 1] shows that for every k ∈ ℕ k\in\mathbb{N} there exists a local center-stable manifold W W at ( 0, − f ( 0; ν 0) / α 0, α 0, ν 0) (0,-f(0;\nu_{0})/\alpha_{0},\alpha_{0},\nu_{0}) that is written as y = f ^ l ​ o ​ c ​ ( α, x, ν) y=\hat{f}_{loc}(\alpha,x;\nu) where f ^ l ​ o ​ c \hat{f}_{loc} is a 𝒞 k \mathscr{C}^{k} function in a neighbourhood V V of ( α 0, 0, ν 0). (\alpha_{0},0,\nu_{0}). In this context, contrary to what happens in general, it turns out that the center-stable manifold is unique, which implies that f ^ l ​ o ​ c \hat{f}_{loc} is 𝒞 ∞ \mathscr{C}^{\infty} (see [27, p. 165]). That being said, we assume without lost of generality that V V is a cube with center ( α 0, 0, ν 0) (\alpha_{0},0,\nu_{0}) and edge length 4 ​ ε 4\varepsilon. Then for the points in the strip 𝒮 = { ( α, x, ν): x ∈ I ​ and ​ ( α, 0, ν) ∈ V } \mathcal{S}=\{(\alpha,x,\nu):x\in I\text{ and }(\alpha,0,\nu)\in V\} we define

 | f ^ ​ ( α, x, ν):= { x α ​ ( f ^ l ​ o ​ c ​ ( α, ε, ν) ​ ε − α + ∫ ε x f ⁡ ( s, ν) ​ s − α ​ d ​ s s) if x ∈ I ∩ ( 0, + ∞), f ^ l ​ o ​ c ​ ( α, 0, ν) if x = 0, ( − x) α ​ ( f ^ l ​ o ​ c ​ ( α, − ε, ν) ​ ε − α + ∫ − ε x f ⁡ ( s, ν) ​ ( − s) − α ​ d ​ s s) if x ∈ I ∩ ( − ∞, 0), \hat{f}(\alpha,x;\nu)\!:=\left\{\begin{array}[]{ll}\displaystyle x^{\alpha}\left(\hat{f}_{loc}(\alpha,\varepsilon;\nu)\varepsilon^{-\alpha}+\int_{\varepsilon}^{x}f(s;\nu)s^{-\alpha}\frac{ds}{s}\right)&\text{ if $x\in I\cap(0,+\infty),$}\\[10.0pt] \hat{f}_{loc}(\alpha,0;\nu)&\text{ if $x=0,$}\\[10.0pt] \displaystyle(-x)^{\alpha}\left(\hat{f}_{loc}(\alpha,-\varepsilon;\nu)\varepsilon^{-\alpha}+\int_{-\varepsilon}^{x}f(s;\nu)(-s)^{-\alpha}\frac{ds}{s}\right)&\text{ if $x\in I\cap(-\infty,0),$}\end{array}\right. |  | (48) |

which is clearly 𝒞 ∞ \mathscr{C}^{\infty} on 𝒮 ∖ { x = 0 } \mathcal{S}\setminus\{x=0\}. An easy computation shows that the above function verifies the scalar differential equation ( 46) (\ref{Mellin-eq}\hbox{}) for all ( α, x, ν) ∈ 𝒮 (\alpha,x,\nu)\in\mathcal{S} with x ≠ 0. x\neq 0. Hence, due to f ^ ​ ( α, ± ε, ν) = f ^ l ​ o ​ c ​ ( α, ± ε, ν) \hat{f}(\alpha,\pm\varepsilon;\nu)=\hat{f}_{loc}(\alpha,\pm\varepsilon;\nu), by the existence and uniqueness theorem for solutions of differential equations (see [9, Theorem 1.1] for instance) we have that f ^ | V = f ^ l ​ o ​ c \hat{f}|_{V}=\hat{f}_{loc} and, consequently, f ^ ∈ 𝒞 ∞ ​ ( 𝒮) \hat{f}\in\mathscr{C}^{\infty}(\mathcal{S}). On account of the uniqueness of f ^ \hat{f} proved firstly, the arbitrariness of α 0 ∈ ( − ∞, 0) \alpha_{0}\in(-\infty,0) and ν 0 ∈ U \nu_{0}\in U shows that ( 48) (\ref{Meq1}\immediate) provides a well defined 𝒞 ∞ \mathscr{C}^{\infty} function f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) on ( − ∞, 0) × I × U (-\infty,0)\times I\times U. This proves the existence for the case α < 0. \alpha<0.

Let us show next the existence for the case α > 0. \alpha>0. In what follows we shall use the more compact notation ℓ ^ α ​ ( x, ν) = ℓ ^ ​ ( α, x, ν) \hat{\ell}_{\alpha}(x;\nu)=\hat{\ell}(\alpha,x;\nu) omitting also the dependence on x x and ν \nu when there is no risk of ambiguity. Following this notation, some easy computations show that

1. 1. 1.

If ℓ = g + h \ell=g+h then ℓ ^ α = g ^ α + h ^ α \hat{\ell}_{\alpha}=\hat{g}_{\alpha}+\hat{h}_{\alpha}, provided that g ^ α \hat{g}_{\alpha} and h ^ α \hat{h}_{\alpha} exist.

2. 2. 2.

If ℓ ⁡ ( x, ν) = ∑ i = 0 k d i ​ ( ν) ​ x i \ell(x;\nu)=\sum_{i=0}^{k}d_{i}(\nu)x^{i} and α ∉ { 0, 1, 2, …, k } \alpha\notin\{0,1,2,\ldots,k\} then ℓ ^ α ​ ( x, ν) = ∑ i = 0 k d i ​ ( ν) i − α ​ x i \hat{\ell}_{\alpha}(x;\nu)=\sum_{i=0}^{k}\frac{d_{i}(\nu)}{i-\alpha}x^{i}.

3. 3. 3.

If ℓ ⁡ ( x, ν) = x m ​ g ​ ( x, ν) \ell(x;\nu)=x^{m}g(x;\nu) with m > α m>\alpha then ℓ ^ α ​ ( x, ν) = x m ​ g ^ α − m ​ ( x, ν) \hat{\ell}_{\alpha}(x;\nu)=x^{m}\hat{g}_{\alpha-m}(x;\nu).

That being said, let us fix an arbitrary m ∈ ℕ m\in\mathbb{N} and note that, by applying Lemma 2.2, we can write

 | f ⁡ ( x, ν) = ∑ i = 0 m − 1 d i ​ ( ν) ​ x i + x m ​ g ​ ( x, ν), f(x;\nu)=\sum_{i=0}^{m-1}d_{i}(\nu)x^{i}+x^{m}g(x;\nu), |  |

with d i ∈ 𝒞 ∞ ​ ( U) d_{i}\in\mathscr{C}^{\infty}(U) and g ∈ 𝒞 ∞ ​ ( I × U). g\in\mathscr{C}^{\infty}(I\times U). On account of this, since we have already proved the existence of f ^ α \hat{f}_{\alpha} for α < 0 \alpha<0, the three properties above imply the existence of f ^ ​ ( α, x, ν) ∈ 𝒞 ∞ ​ ( ( ( − ∞, m) ∖ ℤ ≥ 0) × I × U) \hat{f}(\alpha,x;\nu)\in\mathscr{C}^{\infty}\big(((-\infty,m)\setminus\mathbb{Z}_{\geq 0})\times I\times U\big) satisfying ( 46) (\ref{Mellin-eq}\hbox{}). Finally the arbitrariness of m ∈ ℕ m\in\mathbb{N} and the uniqueness of f ^ \hat{f} proved firstly imply that f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) is a well defined 𝒞 ∞ \mathscr{C}^{\infty} function on ( ℝ ∖ ℤ ≥ 0) × I × U (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I\times U verifying ( 46) (\ref{Mellin-eq}\hbox{}). This concludes the proof of ( a CLOSE (a).

Let us prove next the assertions in ( b) (b). The fact that the equality ∂ x ( f ^ ​ ( α, x, ν) ​ | x | − α) = f ⁡ ( x, ν) ​ | x | − α x \partial_{x}(\hat{f}({\alpha},x;\nu)|x|^{-\alpha})=f(x;\nu)\frac{|x|^{-\alpha}}{x} holds for all x ∈ I ∖ { 0 } x\in I\setminus\{0\} follows easily from ( 46) (\ref{Mellin-eq}\hbox{}) by considering the cases x > 0 x>0 and x < 0 x<0 separately. In order to prove ( 47) (\ref{Mellin-int}\immediate) we note first that, thanks to Lemma 2.2, we can write f ⁡ ( x, ν) − T 0 k − 1 ​ f ​ ( x, ν) = x k ​ g ​ ( x, ν) f(x;\nu)-T_{0}^{k-1}f(x;\nu)=x^{k}g(x;\nu) with g ∈ 𝒞 ∞ ​ ( I × U). g\in\mathscr{C}^{\infty}(I\times U). Taking this into account and performing the coordinate change s = t ​ x s=tx we get

 | | x | α ​ ∫ 0 x ( f ⁡ ( s, ν) − T 0 k − 1 ​ f ​ ( s, ν)) ​ | s | − α ​ d ​ s s = | x | ∫ 0 x α ⁡ s k ​ g ​ ( s, ν) ​ | s | − α ​ d ​ s s = x k ​ ∫ 0 1 t k − α ​ g ​ ( t ​ x, ν) ​ d ​ t t. |x|^{\alpha}\int_{0}^{x}(f(s;\nu)-T_{0}^{k-1}f(s;\nu))|s|^{-\alpha}\frac{ds}{s}=|x|^{\alpha}\int_{0}^{x}s^{k}g(s;\nu)|s|^{-\alpha}\frac{ds}{s}=x^{k}\int_{0}^{1}t^{k-\alpha}g(tx;\nu)\frac{dt}{t}. |  |

We claim that this is a 𝒞 ∞ \mathscr{C}^{\infty} function of ( α, x, ν) ∈ ( − ∞, k) × I × U (\alpha,x,\nu)\in(-\infty,k)\times I\times U. To prove this we apply assertions ( i) (i), ( c) (c) and ( g) (g) in Lemma 2.4 to conclude that ( t, α, x, ν) ↦ t k − α − 1 ​ g ​ ( t ​ x, ν) (t;\alpha,x,\nu)\mapsto t^{k-\alpha-1}g(tx;\nu) belongs to ℱ L ∞ ​ ( ( − ∞, k − 1 − L) × I × U) \mathcal{F}_{L}^{\infty}((-\infty,k-1-L)\times I\times U) for any L ∈ ℝ. L\in\mathbb{R}. Consequently, if we fix any α 0 ∈ ( − ∞, k) \alpha_{0}\in(-\infty,k) and take L = k − α 0 2 − 1 L=\frac{k-\alpha_{0}}{2}-1 then for any x 0 ∈ I x_{0}\in I, ν 0 ∈ U \nu_{0}\in U, K ∈ ℤ ≥ 0 K\in\mathbb{Z}_{\geq 0} and ν ∈ ℤ ≥ 0 N + 2 \nu\in\mathbb{Z}_{\geq 0}^{N+2} with | ν | ⩽ K |\nu|\leqslant K there exist a compact neighborhood Q Q of ( α 0, x 0, ν 0) (\alpha_{0},x_{0},\nu_{0}) and constants C, t 0 > 0 C,t_{0}>0 such that the absolute value of

 | ∂ ν ( t k − α − 1 ​ g ​ ( t ​ x, ν)) = ∂ | ν | ( t k − α − 1 ​ g ​ ( t ​ x, ν)) ∂ ν 1 ν 1 ⋯ ∂ ν N ν N ∂ ν N + 1 α ∂ ν N + 2 x \partial^{\nu}\big(t^{k-\alpha-1}g(tx;\nu)\big)=\frac{\partial^{|\nu|}(t^{k-\alpha-1}g(tx;\nu))}{\partial^{\nu_{1}}\nu_{1}\cdots\partial^{\nu_{N}}\nu_{N}\partial^{\nu_{N+1}}\alpha\partial^{\nu_{N+2}}x} |  |

is bounded by C ​ t L Ct^{L} for all ( α, x, ν) ∈ Q (\alpha,x,\nu)\in Q and t ∈ ( 0, t 0) t\in(0,t_{0}). It is clear on the other hand that there exists C ′ > 0 C^{\prime}>0 such that | ∂ ν ( t k − α − 1 ​ g ​ ( t ​ x, ν)) | ⩽ C ′ |\partial^{\nu}(t^{k-\alpha-1}g(tx;\nu))|\leqslant C^{\prime} for all ( α, x, ν) ∈ Q (\alpha,x,\nu)\in Q and t ∈ [t 0, 1] t\in[t_{0},1]. Accordingly | ∂ ν ( t k − α − 1 ​ g ​ ( t ​ x, ν)) | |\partial^{\nu}(t^{k-\alpha-1}g(tx;\nu))| is bounded by an integrable function of t ∈ [0, 1] t\in[0,1] not depending on ( α, x, ν) (\alpha,x,\nu). Hence, by applying the Dominated Convergence Theorem (see [31, Theorem 11.30] and also [34, pp. 409–410]) we can assert that the function ( α, x, ν) ↦ ∫ 0 1 t k − α ​ g ​ ( t ​ x, ν) ​ d ​ t t (\alpha,x,\nu)\mapsto\int_{0}^{1}t^{k-\alpha}g(tx;\nu)\frac{dt}{t} is 𝒞 ∞ \mathscr{C}^{\infty} on a neighbourhood of ( α 0, x 0, ν 0) (\alpha_{0},x_{0},\nu_{0}). This proves the claim and shows in particular that the function on the right hand side of the equality in ( 47) (\ref{Mellin-int}\hbox{}) is written as

 | ψ ⁡ ( α, x, ν):= ∑ i = 0 k − 1 ∂ x i f ⁡ ( 0, ν) i! ​ ( i − α) ​ x i + x k ​ ∫ 0 1 t k − α ​ g ​ ( t ​ x, ν) ​ d ​ t t ​ for all x ∈ I ∖ { 0 }. \psi(\alpha,x;\nu)\!:=\sum_{i=0}^{k-1}\frac{\partial_{x}^{i}f(0;\nu)}{i!(i-\alpha)}x^{i}+x^{k}\int_{0}^{1}t^{k-\alpha}g(tx;\nu)\frac{dt}{t}\text{ for all $x\in I\setminus\{0\}$.} |  |

Furthermore, on account of the claim, ψ ∈ 𝒞 ∞ ​ ( ( ( − ∞, k) ∖ ℤ ≥ 0) × I × U). \psi\in\mathscr{C}^{\infty}\big(((-\infty,k)\setminus\mathbb{Z}_{\geq 0})\times I\times U\big). On the other hand, by applying the integration by parts formula it follows easily that x ​ ∂ x ψ − α ​ ψ = f x\partial_{x}\psi-\alpha\psi=f. Consequently

 | f ^ ​ ( α, x, ν) \displaystyle\hat{f}(\alpha,x;\nu) | = ∑ i = 0 k − 1 ∂ x i f ⁡ ( 0, ν) i! ​ ( i − α) ​ x i + x k ​ ∫ 0 1 t k − α ​ g ​ ( t ​ x, ν) ​ d ​ t t \displaystyle=\sum_{i=0}^{k-1}\frac{\partial_{x}^{i}f(0;\nu)}{i!(i-\alpha)}x^{i}+x^{k}\int_{0}^{1}t^{k-\alpha}g(tx;\nu)\frac{dt}{t} |  | (49) |

 |  | = ∑ i = 0 k − 1 ∂ x i f ⁡ ( 0, ν) i! ​ ( i − α) ​ x i + | x | α ​ ∫ 0 x ( f ⁡ ( s, ν) − T 0 k − 1 ​ f ​ ( s, ν)) ​ | s | − α ​ d ​ s s, \displaystyle=\sum_{i=0}^{k-1}\frac{\partial_{x}^{i}f(0;\nu)}{i!(i-\alpha)}x^{i}+|x|^{\alpha}\int_{0}^{x}\!\left(f(s;\nu)-T_{0}^{k-1}f(s;\nu)\right)|s|^{-\alpha}\frac{ds}{s}, |  |

where the first equality is true for all ( α, x, ν) ∈ ( ( − ∞, k) ∖ ℤ ≥ 0) × I × U (\alpha,x,\nu)\in((-\infty,k)\setminus\mathbb{Z}_{\geq 0})\times I\times U by the uniqueness of f ^ \hat{f} and the second one holds only for x ≠ 0 x\neq 0 by the variable change s = t ​ x. s=tx. This completes the proof of ( b) (b).

In order to prove ( c) (c) let us fix ( i 0, x 0, ν 0) ∈ ℤ ≥ 0 × I × U ({i_{0}},x_{0},\nu_{0})\in\mathbb{Z}_{\geq 0}\times I\times U and take any k ∈ ℤ ≥ 0 k\in\mathbb{Z}_{\geq 0} such that k > i 0. k>{i_{0}}. Then the equality in ( 49) (\ref{B1eq2}\immediate) shows that ( α, x, ν) ↦ ( i 0 − α) ​ f ^ ​ ( α, x, ν) (\alpha,x,\nu)\mapsto({i_{0}}-\alpha)\hat{f}(\alpha,x;\nu) extends 𝒞 ∞ \mathscr{C}^{\infty} at ( i 0, x 0, ν 0) ({i_{0}},x_{0},\nu_{0}) and, moreover, that it tends to 1 i 0! ​ ∂ x i 0 f ⁡ ( 0, ν 0) ​ x 0 i 0 \frac{1}{i_{0}!}\partial_{x}^{i_{0}}f(0;\nu_{0})x_{0}^{i_{0}} as ( α, x, ν) → ( i 0, x 0, ν 0). (\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0}).

Let us turn finally to the proof of ( d) (d), so we assume henceforth that f ⁡ ( x, ν) f(x;\nu) is analytic on I × U I\times U. Fix any α 0 ∈ ℝ ∖ ℤ ≥ 0 \alpha_{0}\in\mathbb{R}\setminus\mathbb{Z}_{\geq 0} and ν 0 ∈ U \nu_{0}\in U. We claim that the singular differential equation x ​ y ′ − α ​ y = f ⁡ ( x, ν) xy^{\prime}-\alpha y=f(x;\nu) has a solution y = f ^ l ​ o ​ c ​ ( α, x, ν) y=\hat{f}_{loc}(\alpha,x;\nu) with f ^ l ​ o ​ c ​ ( α, 0, ν) = − 1 α ​ f ​ ( 0, ν) \hat{f}_{loc}(\alpha,0;\nu)=-\frac{1}{\alpha}f(0;\nu) that is analytic in a neighbourhood of ( α 0, 0, ν 0) (\alpha_{0},0,\nu_{0}) inside ( ℝ ∖ ℤ ≥ 0) × I × U. (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I\times U.

To prove the claim we consider the holomorphic extension F ⁡ ( x, ν) F(x,\nu) of f ⁡ ( x, ν) f(x;\nu) in a neighbourhood Ω \Omega of ( 0, ν 0) ∈ ℂ N + 1 (0,\nu_{0})\in\mathbb{C}^{N+1} and for each i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0} we define G i ​ ( α, x, ν):= ∂ x i F ⁡ ( 0, ν) i! ​ ( i − α) ​ x i G_{i}(\alpha,x,\nu)\!:=\frac{\partial_{x}^{i}F(0,\nu)}{i!(i-\alpha)}x^{i}, which is clearly a holomorphic function on ( ℂ ∖ ℤ ≥ 0) × Ω. (\mathbb{C}\setminus\mathbb{Z}_{\geq 0})\times\Omega. We will see that

 | S ⁡ ( α, x, ν):= ∑ i = 0 ∞ G i ​ ( α, x, ν) S(\alpha,x,\nu)\!:=\sum_{i=0}^{\infty}G_{i}(\alpha,x,\nu) |  | (50) |

is a holomorphic function in a neighbourhood of ( α 0, 0, ν 0) ∈ ( ℂ ∖ ℤ ≥ 0) × Ω (\alpha_{0},0,\nu_{0})\in(\mathbb{C}\setminus\mathbb{Z}_{\geq 0})\times\Omega. To this end we observe that:

1. ( i) (i)

By Cauchy’s Estimates, see for instance [31], if | F ⁡ ( x, ν) | ⩽ M |F(x,\nu)|\leqslant M for all ( x, ν) ∈ Ω (x,\nu)\in\Omega with | x | < R |x|<R and | ν − ν 0 | < ε |\nu-\nu_{0}|<\varepsilon then | ∂ x i F ⁡ ( 0, ν) | ⩽ i! ​ M R i. |\partial_{x}^{i}F(0,\nu)|\leqslant\frac{i!M}{R^{i}}.

2. ( i ​ i) (ii)

There exist δ 1, δ 2 > 0 \delta_{1},\delta_{2}>0 small enough such that if | α − α 0 | < δ 1 |\alpha-\alpha_{0}|<\delta_{1} then | i − α | > δ 2 |i-\alpha|>\delta_{2} for all i ∈ ℤ ≥ 0 i\in\mathbb{Z}_{\geq 0}.

Consequently | G i ​ ( α, x, ν) | < M δ 2 ​ ( L R) i |G_{i}(\alpha,x,\nu)|<\frac{M}{\delta_{2}}\left(\frac{L}{R}\right)^{i} for all ( α, x, ν) ∈ ℂ N + 2 (\alpha,x,\nu)\in\mathbb{C}^{N+2} with | x | < L < R |x|<L<R, | ν − ν 0 | < ε |\nu-\nu_{0}|<\varepsilon and | α − α 0 | < δ 1. |\alpha-\alpha_{0}|<\delta_{1}. This shows that ( 50) (\ref{analitico1}\immediate) converges uniformly in a neighbourhood of ( α 0, 0, ν 0) ∈ ( ℂ ∖ ℤ ≥ 0) × Ω (\alpha_{0},0,\nu_{0})\in(\mathbb{C}\setminus\mathbb{Z}_{\geq 0})\times\Omega. On account of this, and the fact that G i ​ ( α, x, ν) G_{i}(\alpha,x,\nu) is holomorphic on ( ℂ ∖ ℤ ≥ 0) × Ω (\mathbb{C}\setminus\mathbb{Z}_{\geq 0})\times\Omega for all i ⩾ 0 i\geqslant 0, we can assert (see for instance [17, Proposition 2]) that S ⁡ ( α, x, ν) S(\alpha,x,\nu) is holomorphic on ( ℂ ∖ ℤ ≥ 0) × Ω (\mathbb{C}\setminus\mathbb{Z}_{\geq 0})\times\Omega. We have on the other hand that x ​ ∂ x S − α ​ S = F x\partial_{x}S-\alpha S=F because, by the uniform convergence again,

 | x ​ ∂ x S ⁡ ( α, x, ν) − α ​ S ​ ( α, x, ν) = x ​ ∑ i = 0 ∞ ∂ x i F ⁡ ( 0, ν) i! ​ ( i − α) ​ i ​ x i − 1 − α ​ ∑ i = 0 ∞ ∂ x i F ⁡ ( 0, ν) i! ​ ( i − α) ​ x i = ∑ i = 0 ∞ ∂ x i F ⁡ ( 0, ν) i! ​ x i = F ⁡ ( x, ν). x\partial_{x}S(\alpha,x,\nu)-\alpha S(\alpha,x,\nu)=x\sum_{i=0}^{\infty}\frac{\partial_{x}^{i}F(0,\nu)}{i!(i-\alpha)}ix^{i-1}-\alpha\sum_{i=0}^{\infty}\frac{\partial_{x}^{i}F(0,\nu)}{i!(i-\alpha)}x^{i}=\sum_{i=0}^{\infty}\frac{\partial_{x}^{i}F(0,\nu)}{i!}x^{i}=F(x;\nu). |  |

Therefore the claim follows taking f ^ l ​ o ​ c ​ ( α, x, ν) \hat{f}_{loc}(\alpha,x;\nu) to be the restriction of S ⁡ ( α, x, ν) S(\alpha,x;\nu) to the real domain.

Suppose that f ^ l ​ o ​ c ​ ( α, x, ν) \hat{f}_{loc}(\alpha,x;\nu) is analytic in some open cube V V with center ( α 0, 0, ν 0) (\alpha_{0},0,\nu_{0}) and edge length 4 ​ ε 4\varepsilon. Then from here we follow exactly the same approach as in the proof of ( a) (a), i.e., we define f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) in 𝒮 = { ( α, x, ν): x ∈ I ​ and ​ ( α, 0, ν) ∈ V } \mathcal{S}=\{(\alpha,x,\nu):x\in I\text{ and }(\alpha,0,\nu)\in V\} by means of ( 48) (\ref{Meq1}\hbox{}) and it turns out that f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) is analytic on 𝒮 ∖ { x = 0 } \mathcal{S}\setminus\{x=0\}. Indeed, this follows from the analyticity of f ⁡ ( x, ν) f(x;\nu) and that, on account of the previous claim, ( α, ν) ↦ f ^ l ​ o ​ c ​ ( α, ± ε, ν) (\alpha,\nu)\mapsto\hat{f}_{loc}(\alpha,\pm\varepsilon;\nu) is analytic at ( α 0, ν 0) (\alpha_{0},\nu_{0}). Then, exactly as for the regularity assertion in ( a) (a), by the existence and uniqueness theorem for solutions of differential equations we have that f ^ \hat{f} is an analytic function on 𝒮 \mathcal{S}. By the arbitrariness of ν 0 ∈ U \nu_{0}\in U and α 0 ∈ ℝ ∖ ℤ ≥ 0, \alpha_{0}\in\mathbb{R}\setminus\mathbb{Z}_{\geq 0}, this shows that f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) is analytic on ( ℝ ∖ ℤ ≥ 0) × I × U (\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\times I\times U.

In order to prove the second assertion in ( d) (d) we fix α 0 ∈ ℤ ≥ 0 \alpha_{0}\in\mathbb{Z}_{\geq 0} and ν 0 ∈ U. \nu_{0}\in U. Then the proof of the previous claim shows that ( α, x, ν) ⟼ ( α − α 0) ​ f ^ ​ ( α, x, ν) (\alpha,x,\nu)\longmapsto(\alpha-\alpha_{0})\hat{f}(\alpha,x,\nu) is analytic at ( α 0, x 0, ν 0) (\alpha_{0},x_{0},\nu_{0}) for x 0 = 0. x_{0}=0. To prove that this is also true for any x 0 ∈ I x_{0}\in I we argue exactly as before by using the extension defined in ( 48) (\ref{Meq1}\hbox{}) and, for the sake of shortness, it is left to the reader. This concludes the proof of the result.

There are some previous results related with the function f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) defined in Theorem B.1 that should be referred here:

1. ( i) (i)

Bénoit uses in [2, p. 106] a transformation M α: ℂ ⁡ [[t]] → ℂ ⁡ [[t]] M_{\alpha}:\mathbb{C}[[t]]\to\mathbb{C}[[t]] for every fixed α ∈ ℝ > 0 ∖ ℤ \alpha\in\mathbb{R}_{>0}\setminus\mathbb{Z} defined, for each formal series f ∈ ℂ ⁡ [[t]] f\in\mathbb{C}[[t]], by means of the differential equation − t ​ d d ​ t ​ M α ​ ( f) + α ​ M α ​ ( f) = f -t\frac{d}{dt}M_{\alpha}(f)+\alpha M_{\alpha}(f)=f. Hence, by assertion ( a) (a) in Theorem B.1, if f ∈ ℝ ⁡ [[t]] f\in\mathbb{R}[[t]] is convergent then M α ​ ( f) = − f ^ ​ ( α, t) M_{\alpha}(f)=-\hat{f}(\alpha,t).

2. ( i ​ i) (ii)

If α < 0 \alpha<0 then we can take k = 0 k=0 in ( 47) (\ref{Mellin-int}\hbox{}) and get that

 | f ^ ​ ( α, x) = x α ​ ∫ 0 x f ⁡ ( s) ​ s − α ​ d ​ s s ​ for x > 0. \hat{f}(\alpha,x)=x^{\alpha}\int_{0}^{x}f(s)s^{-\alpha}\frac{ds}{s}\text{ for $x>0.$} |  |

Therefore if α > 0 \alpha>0 then lim x → + ∞ x α ​ f ^ ​ ( − α, x) \lim_{x\to+\infty}x^{\alpha}\hat{f}(-\alpha,x) coincides with the usual Mellin transform (see [10])

 | ℳ ​ f ​ ( α) = ∫ 0 ∞ f ⁡ ( s) ​ s α ​ d ​ s s. \mathscr{M}f(\alpha)=\int_{0}^{\infty}f(s)s^{\alpha}\frac{ds}{s}. |  |

3. ( i ​ i ​ i) (iii)

Novikov introduces in [26] a truncated (the author calls it one-sided) Mellin transform as

 | u ∈ L l ​ o ​ c 1 ​ ( ( 0, 1]) ⟼ ℳ 1 ​ u ​ ( α):= ∫ 0 1 s α − 1 ​ u ​ ( s) ​ 𝑑 s u\in L_{loc}^{1}\big((0,1]\big)\longmapsto\mathscr{M}_{1}u(\alpha)\!:=\int_{0}^{1}s^{\alpha-1}u(s)ds |  |

and observe in this regard that ℳ 1 ​ u ​ ( α) = u ^ ​ ( − α, 1) \mathscr{M}_{1}u(\alpha)=\hat{u}({-\alpha},1) for α > 0 \alpha>0.

The formula in ( 47) (\ref{Mellin-int}\hbox{}) enables to interpret f ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu) as a sort of incomplete (and parametric) version of the Mellin transform of f ⁡ ( x, ν) f(x;\nu). As we have seen in the proof of Theorem B.1, ( 47) (\ref{Mellin-int}\hbox{}) extends 𝒞 ∞ \mathscr{C}^{\infty} to x = 0 x=0 by means of the expression ( 49) (\ref{B1eq2}\hbox{}) taking the 𝒞 ∞ \mathscr{C}^{\infty} function g ⁡ ( x, ν) = f ⁡ ( x, ν) − T 0 k − 1 ​ f ​ ( x, ν) x k g(x;\nu)=\frac{f(x;\nu)-T_{0}^{k-1}f(x;\nu)}{x^{k}}, see Lemma 2.2. □ \square

The proof of the following two results is omitted because it is an easy application of Theorem B.1.

###### Corollary B.3.

? ⟨ \langle B21 ⟩ \rangle?

Consider an open interval I I of ℝ \mathbb{R} containing x = 0 x=0, an open subset U U of ℝ N \mathbb{R}^{N} and α ∈ ℝ ∖ ℤ ≥ 0. \alpha\in\mathbb{R}\setminus\mathbb{Z}_{\geq 0}. Then the following hold:

1. ( a) (a)

If f ⁡ ( x, ν) = g ⁡ ( x, ν) + h ⁡ ( x, ν) f(x;\nu)=g(x;\nu)+h(x;\nu) with g, h ∈ 𝒞 ∞ ​ ( I × U) g,h\in\mathscr{C}^{\infty}(I\times U) then f ^ ​ ( α, x, ν) = g ^ ​ ( α, x, ν) + h ^ ​ ( α, x, ν) \hat{f}(\alpha,x;\nu)=\hat{g}(\alpha,x;\nu)+\hat{h}(\alpha,x;\nu).

2. ( b) (b)

If f ⁡ ( x, ν) = c ⁡ ( ν) ​ g ​ ( x, ν) f(x;\nu)=c(\nu)g(x;\nu) with g ∈ 𝒞 ∞ ​ ( I × U) g\in\mathscr{C}^{\infty}(I\times U) and c ∈ 𝒞 ∞ ​ ( U) c\in\mathscr{C}^{\infty}(U) then f ^ ​ ( α, x, ν) = c ⁡ ( ν) ​ g ^ ​ ( α, x, ν). \hat{f}(\alpha,x;\nu)=c(\nu)\hat{g}(\alpha,x;\nu).

3. ( c) (c)

If f ⁡ ( x, ν) = x n ​ g ​ ( x, ν) f(x;\nu)=x^{n}g(x;\nu) with g ∈ 𝒞 ∞ ​ ( I × U) g\in\mathscr{C}^{\infty}(I\times U) and n ∈ ℕ n\in\mathbb{N} then f ^ ​ ( α, x, ν) = x n ​ g ^ ​ ( α − n, x, ν). \hat{f}(\alpha,x;\nu)=x^{n}\hat{g}(\alpha-n,x;\nu).

4. ( d) (d)

If f ⁡ ( x, ν) ≡ 1 f(x;\nu)\equiv 1 then f ^ ​ ( α, x, ν) ≡ − 1 α. \hat{f}(\alpha,x;\nu)\equiv-\frac{1}{\alpha}.

The next two results are equally valid in the smooth category 𝒞 ∞ \mathscr{C}^{\infty} and the analytic category 𝒞 ω \mathscr{C}^{\omega}. For simplicity in the exposition we write 𝒞 ϖ \mathscr{C}^{\varpi} with the wild card ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\}.

###### Corollary B.4.

? ⟨ \langle B22 ⟩ \rangle?

Let us fix ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\} and consider an open interval I I of ℝ \mathbb{R} containing x = 0 x=0 and an open subset U U of ℝ N \mathbb{R}^{N}. If f ⁡ ( x, ν) ∈ 𝒞 ϖ ​ ( I × U) f(x;\nu)\in\mathscr{C}^{\varpi}(I\times U) and κ 1, κ 2, α 0 ∈ ℝ \kappa_{1},\kappa_{2},\alpha_{0}\in\mathbb{R} verify κ 1 ≠ 0 \kappa_{1}\neq 0 and i 0:= κ 1 ​ α 0 + κ 2 ∈ ℤ ≥ 0 i_{0}\!:=\kappa_{1}\alpha_{0}+\kappa_{2}\in\mathbb{Z}_{\geq 0} then, for any ( x 0, ν 0) ∈ I × U (x_{0},\nu_{0})\in I\times U, the function ( α, x, ν) ↦ ( α 0 − α) ​ f ^ ​ ( κ 1 ​ α + κ 2, x, ν) (\alpha,x,\nu)\mapsto(\alpha_{0}-\alpha)\hat{f}(\kappa_{1}\alpha+\kappa_{2},x;\nu) extends 𝒞 ϖ \mathscr{C}^{\varpi} at ( α 0, x 0, ν 0) (\alpha_{0},x_{0},\nu_{0}) and it tends to 1 κ 1 ​ i 0! ​ ∂ x i 0 f ⁡ ( 0, ν 0) ​ x 0 i 0 \frac{1}{\kappa_{1}i_{0}!}\partial_{x}^{i_{0}}f(0;\nu_{0})x_{0}^{i_{0}} as ( α, x, ν) → ( α 0, x 0, ν 0) (\alpha,x,\nu)\to(\alpha_{0},x_{0},\nu_{0}).

We conclude the present appendix by proving a technical lemma to be applied for studying the poles of the coefficients obtained in Theorem A.

###### Lemma B.5.

? ⟨ \langle gorrobis ⟩ \rangle?

Let us fix ϖ ∈ { ∞, ω } \varpi\in\{\infty,\omega\} and consider an open interval I I of ℝ \mathbb{R} containing x = 0 x=0, an open subset U U of ℝ N \mathbb{R}^{N} and α ∈ ℝ ∖ ℤ ≥ 0. \alpha\in\mathbb{R}\setminus\mathbb{Z}_{\geq 0}. Let M ⁡ ( x, ν) M(x;\nu) and A ⁡ ( x, ν) A(x;\nu) be 𝒞 ϖ \mathscr{C}^{\varpi} functions on I × U I\times U and define

 | B ⁡ ( x, α, ν):= A ⁡ ( x, ν) ​ M ^ ​ ( α, x, ν), B(x;\alpha,\nu)\!:=A(x;\nu)\hat{M}(\alpha,x;\nu), |  |

which is a 𝒞 ϖ \mathscr{C}^{\varpi} function on I × ( ℝ ∖ ℤ ≥ 0) × U I\!\times\!(\mathbb{R}\setminus\mathbb{Z}_{\geq 0})\!\times\!U by Theorem B.1. Finally let us take i 0, p, q ∈ ℤ i_{0},p,q\in\mathbb{Z}, with i 0 ⩾ 0 i_{0}\geqslant 0 and q ≠ − 1 q\neq-1, and set i 1:= q ​ i 0 − p i_{1}\!:=qi_{0}-p and i 2:= ( q + 1) ​ i 0 − p i_{2}\!:=(q+1)i_{0}-p. The following assertions hold:

1. ( a) (a)

If i 1 ⩾ 0 i_{1}\geqslant 0 then, for any ( x 0, ν 0) ∈ I × U (x_{0},\nu_{0})\in I\times U, the function ( α, x, ν) ↦ ( i 0 − α) 2 ​ B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) (\alpha,x,\nu)\mapsto(i_{0}-\alpha)^{2}\hat{B}((q+1)\alpha-p,x;\alpha,\nu) extends 𝒞 ϖ \mathscr{C}^{\varpi} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) and it tends to

 | x 0 i 2 q + 1 ​ M ( i 0) ​ ( 0, ν 0) i 0! ​ A ( i 1) ​ ( 0, ν 0) i 1! ​ as ( α, x, ν) → ( i 0, x 0, ν 0). \frac{x_{0}^{i_{2}}}{q+1}\frac{M^{(i_{0})}(0;\nu_{0})}{i_{0}!}\frac{A^{(i_{1})}(0;\nu_{0})}{i_{1}!}\text{ as $(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0})$}. |  |

2. ( b) (b)

If i 1 < 0 i_{1}<0 then, for any ( x 0, ν 0) ∈ I × U (x_{0},\nu_{0})\in I\times U, the function ( α, x, ν) ↦ ( i 0 − α) ​ B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) (\alpha,x,\nu)\mapsto(i_{0}-\alpha)\hat{B}((q+1)\alpha-p,x;\alpha,\nu) extends 𝒞 ϖ \mathscr{C}^{\varpi} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) and it tends to

 |  | x 0 i 2 ( q + 1) ​ i 2! ​ ∑ j = 0 i 2 ( i 2 j) ​ M ( j) ​ ( 0, ν 0) ​ A ( i 2 − j) ​ ( 0, ν 0) j − i 0 + x 0 i 0 ​ M ( i 0) ​ ( 0, ν 0) i 0! ​ A ^ ​ ( i 1, x 0, ν 0) ​ as ( α, x, ν) → ( i 0, x 0, ν 0), \displaystyle\frac{x_{0}^{i_{2}}}{(q+1)\,i_{2}!}\sum_{j=0}^{i_{2}}{i_{2}\choose j}\frac{M^{(j)}(0;\nu_{0})A^{(i_{2}-j)}(0;\nu_{0})}{j-i_{0}}+x_{0}^{i_{0}}\frac{M^{(i_{0})}(0;\nu_{0})}{i_{0}!}\hat{A}(i_{1},x_{0};\nu_{0})\text{ as $(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0}),$} |  |

where the summation is zero in the case that i 2 < 0. i_{2}<0.

By applying Lemma 2.2 we can write M ⁡ ( x, ν) = ∑ j = 0 i 0 M ( j) ​ ( 0, ν) j! ​ x j + x i 0 + 1 ​ g ​ ( x, ν) M(x;\nu)=\sum_{j=0}^{i_{0}}\frac{M^{(j)}(0;\nu)}{j!}x^{j}+x^{{i_{0}}+1}g(x;\nu) with g ∈ 𝒞 ϖ ​ ( I × U) g\in\mathscr{C}^{\varpi}(I\times U). Then the application of Corollary B.3 shows that M ^ ​ ( α, x, ν) = ∑ j = 0 i 0 M ( j) ​ ( 0, ν) j! ​ ( j − α) ​ x j + x i 0 + 1 ​ g ^ ​ ( α − i 0 − 1, x, ν) \hat{M}(\alpha,x;\nu)=\sum_{j=0}^{i_{0}}\frac{M^{(j)}(0;\nu)}{j!(j-\alpha)}x^{j}+x^{{i_{0}}+1}\hat{g}(\alpha-{i_{0}}-1,x;\nu). Consequently, on account of B ⁡ ( x, α, ν):= A ⁡ ( x, ν) ​ M ^ ​ ( α, x, ν) B(x;\alpha,\nu)\!:=A(x;\nu)\hat{M}(\alpha,x;\nu), we get that

 | B ⁡ ( x, α, ν) = ∑ j = 0 i 0 M ( j) ​ ( 0, ν) j! ​ ( j − α) ​ x j ​ A ​ ( x, ν) + x i 0 + 1 ​ N ​ ( x, α, ν), B(x;\alpha,\nu)=\sum_{j=0}^{i_{0}}\frac{M^{(j)}(0;\nu)}{j!(j-\alpha)}x^{j}A(x;\nu)+x^{{i_{0}}+1}N(x;\alpha,\nu), |  |

where we set N ⁡ ( x, α, ν):= A ⁡ ( x, ν) ​ g ^ ​ ( α − i 0 − 1, x, ν) N(x;\alpha,\nu)\!:=A(x;\nu)\hat{g}(\alpha-{i_{0}}-1,x;\nu) for shortness. Observe that, since g ^ ​ ( α − i 0 − 1, x, ν) \hat{g}(\alpha-{i_{0}}-1,x;\nu) is 𝒞 ϖ \mathscr{C}^{\varpi} along α = i 0 \alpha={i_{0}} by Theorem B.1, so is N ⁡ ( x, α, ν) N(x;\alpha,\nu). Hence, by applying Corollary B.3 again with α ′ = ( q + 1) ​ α − p \alpha^{\prime}=(q+1)\alpha-p and ν ′ = ( α, ν) \nu^{\prime}=(\alpha,\nu),

 | B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) = ∑ j = 0 i 0 M ( j) ​ ( 0, ν) j! ​ ( j − α) ​ x j ​ A ^ ​ ( ( q + 1) ​ α − p − j, x, ν) + x i 0 + 1 ​ N ^ ​ ( ( q + 1) ​ α − p − i 0 − 1, x, α, ν). \hat{B}\big((q+1)\alpha-p,x;\alpha,\nu\big)=\sum_{j=0}^{i_{0}}\frac{M^{(j)}(0;\nu)}{j!(j-\alpha)}x^{j}\hat{A}\big((q+1)\alpha-p-j,x;\nu\big)+x^{{i_{0}}+1}\hat{N}\big((q+1)\alpha-p-{i_{0}}-1,x;\alpha,\nu\big). |  |

Thus multiplying by ( i 0 − α) k ({i_{0}}-\alpha)^{k} on both sides of the above equality we get

 | ( i 0 − α) k ​ B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) = \displaystyle({i_{0}}-\alpha)^{k}\hat{B}\big((q+1)\alpha-p,x;\alpha,\nu\big)= | ∑ j = 0 i 0 M ( j) ​ ( 0, ν) j! ​ ( i 0 − α) k j − α ​ A ^ ​ ( ( q + 1) ​ α − p − j, x, ν) ​ x j \displaystyle\sum_{j=0}^{i_{0}}\frac{M^{(j)}(0;\nu)}{j!}\frac{({i_{0}}-\alpha)^{k}}{j-\alpha}\hat{A}\big((q+1)\alpha-p-j,x;\nu\big)x^{j} |  |

 |  | + ( i 0 − α) k ​ x i 0 + 1 ​ N ^ ​ ( ( q + 1) ​ α − p − i 0 − 1, x, α, ν). \displaystyle\quad+({i_{0}}-\alpha)^{k}x^{{i_{0}}+1}\hat{N}\big((q+1)\alpha-p-{i_{0}}-1,x;\alpha,\nu\big). |  | (51) |

In order to prove ( a) (a) we set k = 2 k=2 above, so that

 | ( i 0 − α) 2 ​ B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) \displaystyle({i_{0}}-\alpha)^{2}\hat{B}\big((q+1)\alpha-p,x;\alpha,\nu\big) | = M ( i 0) ​ ( 0, ν) i 0! ​ ( i 0 − α) ​ A ^ ​ ( ( q + 1) ​ α − p − i 0, x, ν) ​ x i \displaystyle=\frac{M^{({i_{0}})}(0;\nu)}{{i_{0}}!}({i_{0}}-\alpha)\hat{A}\big((q+1)\alpha-p-{i_{0}},x;\nu\big)x^{i} |  |

 |  | + ∑ j = 0 i 0 − 1 M ( j) ​ ( 0, ν) j! ( i 0 − α) 2 j − α A ^ ( ( q + 1) α − p − j, x; ν) x j \displaystyle\quad+\sum_{j=0}^{{i_{0}}-1}\frac{M^{(j)}(0;\nu)}{j!}\frac{({i_{0}}-\alpha)^{2}}{j-\alpha}\hat{A}\big((q+1)\alpha-p-j,x;\nu\big)x^{j} |  |

 |  | + ( i 0 − α) 2 ​ x i 0 + 1 ​ N ^ ​ ( ( q + 1) ​ α − p − i 0 − 1, x, α, ν). \displaystyle\quad+({i_{0}}-\alpha)^{2}x^{{i_{0}}+1}\hat{N}\big((q+1)\alpha-p-{i_{0}}-1,x;\alpha,\nu\big). |  |

By Corollary B.4 this expressions shows that ( α, x, ν) ↦ ( i 0 − α) 2 ​ B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) (\alpha,x,\nu)\mapsto(i_{0}-\alpha)^{2}\hat{B}((q+1)\alpha-p,x;\alpha,\nu) extends 𝒞 ϖ \mathscr{C}^{\varpi} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) for any ( x 0, ν 0) ∈ I × U. (x_{0},\nu_{0})\in I\times U. Furthermore, since all the summands except the first one tend to zero as ( α, x, ν) → ( i 0, x 0, ν 0) (\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0}) by Corollary B.4 again,

 | lim ( α, x, ν) → ( i 0, x 0, ν 0) ( i 0 − α) 2 \displaystyle\lim_{(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0})}({i_{0}}-\alpha)^{2} | B ^ ​ ( ( q + 1) ​ α − p, x, ν) \displaystyle\hat{B}((q+1)\alpha-p,x;\nu) |  | (52) |

 |  | = M ( i 0) ​ ( 0, ν 0) i 0! ​ x 0 i 0 ​ lim ( α, x, ν) → ( i 0, x 0, ν 0) ( i 0 − α) ​ A ^ ​ ( ( q + 1) ​ α − p − i 0, x, ν) \displaystyle=\frac{M^{({i_{0}})}(0;\nu_{0})}{{i_{0}}!}x_{0}^{i_{0}}\lim_{(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0})}({i_{0}}-\alpha)\hat{A}\big((q+1)\alpha-p-{i_{0}},x;\nu\big) |  |

provided that the limit on the right hand side exists. In order to compute it we apply Corollary B.4 once again, with κ 1 = q + 1 \kappa_{1}=q+1 and κ 2 = − p − i 0 \kappa_{2}=-p-{i_{0}}, to conclude that

 | lim ( α, x, ν) → ( i 0, x 0, ν o) A ^ ​ ( ( q + 1) ​ α − p − i 0, x, ν) = x 0 i 1 q + 1 ​ A ( i 1) ​ ( 0, ν 0) i 1!, \lim_{(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{o})}\hat{A}\big((q+1)\alpha-p-{i_{0}},x;\nu\big)=\frac{x_{0}^{i_{1}}}{q+1}\frac{A^{(i_{1})}(0;\nu_{0})}{i_{1}!}, |  |

where we also take the assumption i 1 = q ​ i 0 − p = κ 1 ​ i 0 + κ 2 ∈ ℤ ≥ 0 i_{1}=q{i_{0}}-p=\kappa_{1}{i_{0}}+\kappa_{2}\in\mathbb{Z}_{\geq 0} into account. Consequently, from ( 52) (\ref{B3eq1}\immediate),

 | lim ( α, x, ν) → ( i 0, x 0, ν 0) ( i 0 − α) 2 ​ B ^ ​ ( ( q + 1) ​ α − p, x, ν) = x 0 i 0 + i 1 q + 1 ​ M ( i 0) ​ ( 0, ν 0) i 0! ​ A ( i 1) ​ ( 0, ν 0) i 1! \lim_{(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0})}({i_{0}}-\alpha)^{2}\hat{B}((q+1)\alpha-p,x;\nu)=\frac{x_{0}^{{i_{0}}+i_{1}}}{q+1}\frac{M^{({i_{0}})}(0;\nu_{0})}{{i_{0}}!}\frac{A^{(i_{1})}(0;\nu_{0})}{i_{1}!} |  |

and this proves ( a) (a). Let us turn next to the assertion in ( b) (b). In this case we set k = 1 k=1 in ( 51) (\ref{B3eq0}\immediate) to obtain

 | ( i 0 − α) ​ B ^ ​ ( ( q + 1) ​ α − p, x, α, ν) \displaystyle({i_{0}}-\alpha)\hat{B}\big((q+1)\alpha-p,x;\alpha,\nu\big) | = M ( i 0) ​ ( 0, ν) i 0! ​ A ^ ​ ( ( q + 1) ​ α − p − i 0, x, ν) ​ x i 0 \displaystyle=\frac{M^{({i_{0}})}(0;\nu)}{{i_{0}}!}\hat{A}\big((q+1)\alpha-p-{i_{0}},x;\nu\big)x^{i_{0}} |  |

 |  | + ∑ j = 0 i 0 − 1 M ( j) ​ ( 0, ν) j! i 0 − α j − α A ^ ( ( q + 1) α − p − j, x; ν) x j \displaystyle\quad+\sum_{j=0}^{{i_{0}}-1}\frac{M^{(j)}(0;\nu)}{j!}\frac{{i_{0}}-\alpha}{j-\alpha}\hat{A}\big((q+1)\alpha-p-j,x;\nu\big)x^{j} |  |

 |  | + ( i 0 − α) ​ x i 0 + 1 ​ N ^ ​ ( ( q + 1) ​ α − p − i 0 − 1, x, α, ν). \displaystyle\quad+({i_{0}}-\alpha)x^{{i_{0}}+1}\hat{N}\big((q+1)\alpha-p-{i_{0}}-1,x;\alpha,\nu\big). |  |

Note that the last summand on the right hand side is 𝒞 ϖ \mathscr{C}^{\varpi} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) by applying Theorem B.1 because ( q + 1) ​ α − p − i 0 − 1 | α = i 0 = i 1 − 1 < 0 (q+1)\alpha-p-{i_{0}}-1|_{\alpha={i_{0}}}=i_{1}-1<0 due to the hypothesis i 1:= q ​ i 0 − p < 0 i_{1}\!:=q{i_{0}}-p<0. It shows furthermore that it tends to zero as ( α, x, ν) → ( i 0, x 0, ν 0) (\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0}). Exactly the same reason shows that the first summand is 𝒞 ϖ \mathscr{C}^{\varpi} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) and that it tends to M ( i 0) ​ ( 0, ν 0) i 0! ​ A ^ ​ ( q ​ i 0 − p, x 0, ν 0) \frac{M^{(i_{0})}(0;\nu_{0})}{i_{0}!}\hat{A}\big(q{i_{0}}-p,x_{0};\nu_{0}\big) as ( α, x, ν) → ( i 0, x 0, ν 0) (\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0}). Then, by applying Corollary B.4 with κ 1 = q + 1 \kappa_{1}=q+1 and κ 2 = − p − j \kappa_{2}=-p-j, the remaining summands on the right hand side also extend 𝒞 ϖ \mathscr{C}^{\varpi} at ( i 0, x 0, ν 0) (i_{0},x_{0},\nu_{0}) and

 | lim ( α, x, ν) → ( i 0, x 0, ν 0) \displaystyle\lim_{(\alpha,x,\nu)\to(i_{0},x_{0},\nu_{0})} | ( i 0 − α) ​ B ^ ​ ( ( q + 1) ​ α − p, x, ν) \displaystyle(i_{0}-\alpha)\hat{B}((q+1)\alpha-p,x;\nu) |  |

 |  | = 1 q + 1 ​ ∑ j = 0 i 2 x 0 i 2 j − i 0 ​ M ( j) ​ ( 0, ν 0) j! ​ A ( i 2 − j) ​ ( 0, ν 0) ( i 2 − j)! + x 0 i 0 ​ M ( i 0) ​ ( 0, ν 0) i 0! ​ A ^ ​ ( q ​ i 0 − p, x 0, ν 0). \displaystyle=\frac{1}{q+1}\sum_{j=0}^{i_{2}}\frac{x_{0}^{i_{2}}}{j-{i_{0}}}\frac{M^{(j)}(0;\nu_{0})}{j!}\frac{A^{(i_{2}-j)}(0;\nu_{0})}{(i_{2}-j)!}+x_{0}^{i_{0}}\frac{M^{({i_{0}})}(0;\nu_{0})}{{i_{0}}!}\hat{A}(q{i_{0}}-p,x_{0};\nu_{0}). |  |

Here we also use that κ 1 ​ i 0 + κ 2 = ( q + 1) ​ i 0 − p − j ⩾ 0 \kappa_{1}{i_{0}}+\kappa_{2}=(q+1){i_{0}}-p-j\geqslant 0 if and only if j ⩽ ( q + 1) ​ i 0 − p =: i 2 j\leqslant(q+1){i_{0}}-p=:\!i_{2}. This proves ( b) (b) and concludes the proof of the result.

## References

- [1] A. A. Andronov, E. A. Leontovich, I. I. Gordon and A. G. Maĭer, “Theory of bifurcations of dynamic systems on a plane”. Translated from the Russian. Halsted Press, New York-Toronto, Ont.; Israel Program for Scientific Translations, Jerusalem-London, 1973. xiv+482 pp.
- [2] É. Bénoit, Perturbation singulière en dimension trois : canards en un point pseudo-singulier noeud, Bull. Soc. Math. France 129 (2001), 91–113.
- [3] F. Dumortier, M. El Morsalani and C. Rousseau, Hilbert’s 16th problem for quadratic systems and cyclicity of elementary graphics, Nonlinearity 9 (1996) 1209–1261.
- [4] F. Dumortier, R. Roussarie and C. Rousseau, Elementary Graphics of cyclicity 1 and 2, Nonlinearity 7 (1994) 1001–1043.
- [5] F. Dumortier, R. Roussarie and C. Rousseau, Hilbert’s 16th problem for quadratic vector fields, J. Differential Equations 110 (1994) 86–133.
- [6] X. Cabré, E. Fontich and R. de la Llave, The parameterization method for invariant manifolds. I. Manifolds associated to non-resonant subspaces, Indiana Univ. Math. J. 52 (2003) 283–328.
- [7] X. Cabré, E. Fontich and R. de la Llave, The parameterization method for invariant manifolds. III. Overview and applications, J. Differential Equations 218 (2005) 444–515.
- [8] C. Chicone, Bifurcations of nonlinear oscillations and frequency entrainment near resonance, SIAM J. Math. Anal. 23 (1992) 1577–1608.
- [9] S.-N. Chow and J.K. Hale, “Methods of bifurcation theory”, Springer-Verlag New York, 1982.
- [10] P. Flajolet, X. Gourdon and P. Dumas, Mellin transforms and asymptotics: Harmonic sums, Theoretical Computer Science. 144 (1995) 3–58.
- [11] G.-M. Greuel, C. Lossen and E. Shustin, “Introduction to singularities and deformations”, Springer Monogr. Math., Springer, Berlin, 2007.
- [12] Y. Il’yashenko and S. Yakovenko, Finitely smooth normal forms of local families of diffeomorphisms and vector fields, (Russian) Uspekhi Mat. Nauk 46 (1991) 3–39, 240; translation in Russian Math. Surveys 46 (1991) 1–43.
- [13] Y. Ilyashenko, Centennial history of Hilbert’s 16th problem, Bull. Amer. Math. Soc. 39 (2002) 301–354.
- [14] A. Kelley, The stable, center-stable, center, center-unstable, unstable manifolds, J. Differential Equations 3 (1967) 546–570.
- [15] S. G. Krantz and H. R. Parks, “A Primer of Real Analytic Functions”, Birkhäuser Advanced Texts, Birkhäuser Basel, 2002.
- [16] S. Luca, F. Dumortier, M. Caubergh and R. Roussarie, Detecting alien limit cycles near a Hamiltonian 2-saddle cycle, Discrete Contin. Dyn. Syst. 25 (2009) 1081–1108.
- [17] B. Malgrange, “Lectures on the theory of functions of several complex variables”, Tata Institute of Fundamental Research, Springer-Verlag, 1984.
- [18] P. Mardešić, D. Marín and J. Villadelprat, On the time function of the Dulac map for families of meromorphic vector fields, Nonlinearity 16 (2003) 855–881.
- [19] P. Mardešić, D. Marín and J. Villadelprat, *The period function of reversible quadratic centers*, J. Differential Equations 224 (2006) 120–171.
- [20] P. Mardešić, D. Marín and J. Villadelprat, Unfolding of resonant saddles and the Dulac time, Discrete Contin. Dyn. Syst. 21 (2008) 1221–1244.
- [21] D. Marín and J. Villadelprat, *On the return time function around monodromic polycycles,*J. Differential Equations 228 (2006) 226–258.
- [22] D. Marín and J. Villadelprat, *Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: local setting,*J. Differential Equations 269 (2020) 8425–8467.
- [23] D. Marín, J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: general setting, J. Differential Equations, in press (2020) https://doi.org/10.1016/j.jde.2020.11.020.
- [24] A. Mourtada, Cyclicité finie des polycycles hyperboliques de champs de vecteurs du plan: mise sous forme normale, in: Bifurcations of Planar Vector Fields (J.P. Françoise and R Roussarie, eds.), Lecture Notes in Math. 1455, Springer-Verlag, Berlin - Heidelberg - New York (1990) 272-314.
- [25] L. Nirenberg, A proof of the Malgrange preparation theorem, Proceedings of Liverpool Singularities–Symposium, I (1969/70), pp. 97Ð105. Lecture Notes in Mathematics, Vol. 192. Springer, Berlin, 1971.
- [26] D. Novikov, *On limit cycles appearing by polynomial perturbation of Darbouxian integrable systems,*Geom. Funct. Anal. 18 (2009) 1750–1773.
- [27] J. Palis and F. Takens, “Hyperbolicity and sensitive chaotic dynamics at homoclinic bifurcations. Fractal dimensions and infinitely many attractors”, Cambridge Studies in Advanced Mathematics, 35. Cambridge University Press, Cambridge, 1993.
- [28] R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix loop of planar vector fields, Bol. Soc. Brasil. Mat. 17 (1986) 67–101.
- [29] R. Roussarie, Cyclicité finie des lacets et des points cuspidaux, Nonlinearity 2 (1989) 7–117.
- [30] R. Roussarie, “Bifurcations of planar vector fields and Hilbert’s sixteenth problem” [2013] reprint of the 1998 edition. Modern Birkhäuser Classics. Birkhäuser/Springer, Basel, 1998.
- [31] W. Rudin, “Real and complex analysis” McGraw-Hill Book Co., New York-Toronto, Ont.-London 1966.
- [32] D. S. Shafer and A. Zegeling, Bifurcation of limit cycles from quadratic centers, J. Differential Equations 122 (1995) 48–70.
- [33] G. Swirszcz, Cyclicity of infinite contour around certain reversible quadratic center, J. Differential Equations 154 (1999) 239–266.
- [34] V. A. Zorich, “Mathematical analysis II” Translated from the 2002 fourth Russian edition by Roger Cooke. Universitext. Springer-Verlag, Berlin, 2004.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
