<!-- source: https://arxiv.org/html/2407.20721 | converted from HTML -->

On the cyclicity of hyperbolic polycycles

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2407.20721v2 [math.DS] 20 Feb 2025

# On the cyclicity of hyperbolic polycycles

Claudio Buzzi 1, Armengol Gasull 2 and Paulo Santana 1 Address: 1 IBILCE–UNESP, CEP 15054–000, S. J. Rio Preto, São Paulo, Brazil Email address: [claudio.buzzi@unesp.br; paulo.santana@unesp.br][3] Address: 2 Departament de Matemàtiques, Facultat de Ciències, Universitat Autònoma de Barcelona and Centre de Recerca Matemàtica, Spain Email address: [armengol.gasull@uab.cat][4]

###### Abstract.

Let X X be a planar smooth vector field with a polycycle Γ n \Gamma^{n} with n n sides and all its corners, that are at most n n singularities, being hyperbolic saddles. In this paper we study the cyclicity of Γ n \Gamma^{n} in terms of the hyperbolicity ratios of these saddles, giving explicit conditions that ensure that it is at least k, k, for any k ⩽ n. k\leqslant n. Our result extends old results and also provides a more accurate proof of the known ones because we rely on some recent powerful works that study in more detail the regularity with respect to initial conditions and parameters of the Dulac map of hyperbolic saddles for families of vector fields. We also prove that when X X is polynomial there is a polynomial perturbation (in general with degree much higher that the one of X X) that attains each of the obtained lower bounds for the cyclicities. Finally, we also study some related inverse problems and provide concrete examples of applications in the polynomial world.

###### Key words and phrases:

Polycycle, limit cycle, displacement map, cyclicity, heteroclinic and homoclinic orbits

###### 2020 Mathematics Subject Classification

Primary: 34C37. Secondary: 37C29 and 34C23.

## 1. Introduction and Main Result

Let X X be a planar smooth vector field (i.e. of class C ∞ C^{\infty}). A *graphic*Γ \Gamma for X X is a compact, non-empty invariant subset which is a continuous (but not necessarily homeomorphic) image of 𝕊 1 \mathbb{S}^{1} and consists of a finite number of isolated singularities { p 1, …, p n } \{p_{1},\dots,p_{n}\} (not necessarily distinct) and a compatibly set of distinct regular orbits { L 1, …, L n } \{L_{1},\dots,L_{n}\} such that p i p_{i} is the ω \omega -limit of L i L_{i}. A *polycycle*is a graphic with a well defined first return map on one of its sides. A polycycle is *hyperbolic*if all its singularities are hyperbolic saddles. Let Γ n \Gamma^{n} denote a hyperbolic polycycle composed by the hyperbolic saddles { p 1, …, p n } \{p_{1},\dots,p_{n}\} (not necessarily distinct) and by the distinct regular orbits { L 1, …, L n }, \{L_{1},\dots,L_{n}\}, the sides of the polycycle, such that p i p_{i} is the ω \omega -limit of L i, L_{i}, see Figure 1.

\begin{overpic}[Fig24.eps] \put(95.0,23.0){$p_{1}$} \put(0.0,23.0){$p_{2}$} \put(60.0,36.0){$L_{1}$} \put(30.0,8.0){$L_{2}$} \end{overpic}

( a) (a)

\begin{overpic}[Fig25.eps] \put(54.0,22.5){$p_{1}=p_{2}$} \put(84.0,6.0){$L_{1}$} \put(15.0,38.0){$L_{2}$} \end{overpic}

( b) (b)

Figure 1. Illustration of Γ 2 \Gamma^{2}, with ( a) (a) distinct and ( b) (b) non-distinct hyperbolic saddles.

Let λ i s < 0 < λ i u \lambda_{i}^{s}<0<\lambda_{i}^{u} be the associated eigenvalues of the saddle p i p_{i}, i ∈ { 1, …, n } i\in\{1,\dots,n\}. The *hyperbolicity ratio*of p i p_{i} is the positive real number

(1) |  | r i = | λ i s | λ i u. r_{i}=\frac{|\lambda_{i}^{s}|}{\lambda_{i}^{u}}. |  |

The *graphic number*of Γ n \Gamma^{n} is the positive real number given by,

(2) |  | r ⁡ ( Γ n) = ∏ i = 1 n r i. r(\Gamma^{n})=\prod_{i=1}^{n}r_{i}. |  |

Cherkas [4] proved that if r ⁡ ( Γ n) ≠ 1 r(\Gamma^{n})\neq 1, then Γ n \Gamma^{n} has a well defined stability. More precisely, if r ⁡ ( Γ n) > 1 r(\Gamma^{n})>1, then Γ n \Gamma^{n} is stable (i.e. it attracts the orbits in the region where the first return map is defined). Similarly, if r ⁡ ( Γ n) < 1 r(\Gamma^{n})<1, then Γ n \Gamma^{n} is unstable. Since r ⁡ ( Γ n) r(\Gamma^{n}) depends continuously on smooth perturbations, it follows that if r ⁡ ( Γ n) ≠ 1 r(\Gamma^{n})\neq 1, then Γ n \Gamma^{n} has no change of stability for small perturbations that do not break the polycycle. According with the terminology introduced by Sotomayor [34, Section 2.2], when r ⁡ ( Γ n) ≠ 1 r(\Gamma^{n})\neq 1 it is said that Γ n \Gamma^{n} is *simple*.

Roughly speaking, we say that Γ n \Gamma^{n} has *cyclicity*greater or equal k k inside a family of vector fields containing X X if it is possible to bifurcate at least k k limit cycles from Γ n \Gamma^{n} for some arbitrarily small perturbations of X X inside this family (a more rigorous definition shall be given latter). Several authors have results computing also exact cyclicities or upper bounds, but our results are restricted to give lower bounds. For instance, Andronov and Leontovich [1] proved that if n = 1 n=1 and r ⁡ ( Γ 1) = r 1 ≠ 1 r(\Gamma^{1})=r_{1}\neq 1, then the cyclicity of Γ 1 \Gamma^{1} is at most one. For accessible and didactic versions of this result, we refer to Andronov et al [2, § ​ 29 \mathsection 29] or Kuznetsov [17, Section 6.2]. If n = 2 n=2, Mourtada [25] proved that if ( r 1 − 1) ​ ( r 2 − 1) ≠ 0 (r_{1}-1)(r_{2}-1)\neq 0, then the cyclicity of Γ 2 \Gamma^{2} is at most 2 2. Moreover, if ( r 1 − 1) ​ ( r 2 − 1) < 0 (r_{1}-1)(r_{2}-1)<0, then it is 2 2 for suitable families. For n ∈ { 3, 4 } n\in\{3,4\}, Mourtada [26, 14] also proved similar generic results, showing also the striking result that when n = 4 n=4 there are generic families with cyclicity 5. 5. For more details, we refer to Roussarie [29, Chapter 5 5]. We remark that to obtain such cyclicities, in general it is necessary to break the polycycles. To understand why this jump in the cyclicity happens when n n increases it is instructive to read the recent paper of Panazzolo [27] where the author proposes a representative model for the breaking of hyperbolic polycycles.

Recently, Dukov [5] proved that for each n ⩾ 2 n\geqslant 2, if Γ n \Gamma^{n} satisfies again some generic conditions, then any limit cycle bifurcating from Γ n \Gamma^{n} by a finite-dimensional perturbation has multiplicity at most n n.

On the other hand, on non-generic cases and with suitable perturbations, it is known that the cyclicity can be much higher than n. n. For instance, for n = 1 n=1 (resp. n = 2 n=2) Han and Zhu [12] have provided an example of Γ 1 \Gamma^{1} with cyclicity at least 5 5 (resp. 12 12), inside the polynomial systems of degree 8 8 (resp. 11 11). A higher cyclicity for n = 2 n=2 is given by Tian and Han in [36].

For a study of the cyclicity of *persistent*polycycles (i.e. to obtain limit cycles without breaking the original polycycle), we refer to Marin and Villadelprat [20]. For other examples of lower bounds for the cyclicity of Γ n \Gamma^{n} for low values of n n, we refer to [33] and the references therein. We also refer to the works of Gasull et al [7] and Han et al [10] for the study of the stability of polycycles where the graphic number ( 2) is equal to 1 1.

In recent years there is an extension of some results, such as the one of Cherkas, to the case of planar non-smooth vector fields (also known as piecewise smooth or Filippov systems). See Santana [30].

Inspired by the work of Han et al [11], in this paper we study under generic conditions the cyclicity of Γ n \Gamma^{n}, n ⩾ 1 n\geqslant 1, both in the smooth and polynomial cases.

In a few words, the geometric idea behind the bifurcations of the limit cycles consists in breaking a given polycycle Γ n \Gamma^{n} in “sub-polycycles” Γ n − 1 \Gamma^{n-1}, Γ n − 2, … \Gamma^{n-2},\dots by casting out its hyperbolic saddles one-by-one in such a way that at least one limit cycle bifurcates at each step, see Figure 2.

\begin{overpic}[Fig10.eps] \put(78.0,85.0){$p_{1}$} \put(14.0,85.0){$p_{2}$} \put(-10.0,43.0){$p_{3}$} \put(14.0,0.0){$p_{4}$} \put(78.0,0.0){$p_{5}$} \put(101.0,43.0){$p_{6}$} \end{overpic}

( a) (a) Unperturbed.

\begin{overpic}[Fig11x.eps] \put(79.0,85.0){$p_{1}$} \put(12.0,85.0){$p_{2}$} \put(-10.0,43.0){$p_{3}$} \put(14.0,0.0){$p_{4}$} \put(78.0,0.0){$p_{5}$} \put(101.0,43.0){$p_{6}$} \end{overpic}

( b) (b) First perturbation.

\begin{overpic}[Fig22x.eps] \put(78.0,85.0){$p_{1}$} \put(14.0,85.0){$p_{2}$} \put(-10.0,43.0){$p_{3}$} \put(14.0,0.0){$p_{4}$} \put(78.0,0.0){$p_{5}$} \put(101.0,43.0){$p_{6}$} \end{overpic}

( c) (c) Second perturbation.

Figure 2. Illustration of the bifurcation process. Blue means stable and red means unstable. Colors available in the online version.

More precisely, if at a given step the polycycles Γ n 0 \Gamma^{n_{0}} and Γ n 0 − 1 \Gamma^{n_{0}-1} have opposite stabilities, then it follows from the Poincaré-Bendixson Theorem (and some technical results) that at least one limit cycle of odd multiplicity bifurcates when we break from Γ n 0 \Gamma^{n_{0}} to Γ n 0 − 1 \Gamma^{n_{0}-1}. To ensure these opposite stabilities it is sufficient to have ( r ⁡ ( Γ n 0) − 1) ​ ( r ⁡ ( Γ n 0 − 1) − 1) < 0 (r(\Gamma^{n_{0}})-1)(r(\Gamma^{n_{0}-1})-1)<0, see ( 2). Moreover when casting out the hyperbolic saddles we do not need to follow the “canonical” indexation { p 1, …, p 6 } \{p_{1},\dots,p_{6}\}, as in Figure 2. Rather at each step we can choose which singularity to expel in order to maximize the number of stability changes and thus the number of limit cycles. At Figure 2 for example, one could start the process by expelling p 4 p_{4} and then p 1 p_{1} and etc.

As we shall see in Proposition 9, any possible combination of n n hyperbolicity ratios ( 1) r 1, …, r n r_{1},\dots,r_{n} is realizable by a polynomial vector field of degree n n. Hence, the possibility to choose the most convenient singularity to expel at each steep of the bifurcation process is very important in order to obtain better lower bounds for the number of limit cycles.

Therefore the main objective of this paper is to formalize this geometric idea, which includes developing the technical machinery necessary to it. At the end we also apply these ideas on concrete polynomial vector fields. In particular, for instance we prove that Figure 2 is realizable by a polynomial vector field of degree six, see Proposition 10.

To state precisely our main result we need to introduce some notations. Given r ⩾ 1 r\geqslant 1*finite*, let C r ​ ( ℝ 2, ℝ 2) C^{r}(\mathbb{R}^{2},\mathbb{R}^{2}) be the set of the functions f: ℝ 2 → ℝ 2 f\colon\mathbb{R}^{2}\to\mathbb{R}^{2} of class C r C^{r}. Given f ∈ C r ​ ( ℝ 2, ℝ 2) f\in C^{r}(\mathbb{R}^{2},\mathbb{R}^{2}), a compact set B ⊂ ℝ 2 B\subset\mathbb{R}^{2} and ε > 0 \varepsilon>0, let V ⁡ ( f, B, ε) ⊂ C r ​ ( ℝ 2, ℝ 2) V(f,B,\varepsilon)\subset C^{r}(\mathbb{R}^{2},\mathbb{R}^{2}) be the set of C r C^{r} -functions g: ℝ 2 → ℝ 2 g\colon\mathbb{R}^{2}\to\mathbb{R}^{2} such that

 | max x ∈ B | k | ⩽ r ⁡ | | ∂ | k | f ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) − ∂ | k | g ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) | | < ε, \max_{\begin{subarray}{c}x\in B\\ |k|\leqslant r\end{subarray}}\left|\left|\frac{\partial^{|k|}f}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)-\frac{\partial^{|k|}g}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)\right|\right|<\varepsilon, |  |

where x = ( x 1, x 2) x=(x_{1},x_{2}), k = ( k 1, k 2) ∈ ℤ ⩾ 0 2 k=(k_{1},k_{2})\in\mathbb{Z}^{2}_{\geqslant 0} and | k | = k 1 + k 2 |k|=k_{1}+k_{2}. The Whitney’s weak C r C^{r} -topology [13, Chapter 2] is the topology on C r ​ ( ℝ 2, ℝ 2) C^{r}(\mathbb{R}^{2},\mathbb{R}^{2}) having the family of all such V ⁡ ( f, B, ε) V(f,B,\varepsilon) as a sub-base. In other words, it is the smaller topology that contains all such V ⁡ ( f, B, ε) V(f,B,\varepsilon). Let now 𝒫 \mathcal{P} be the set of planar polynomial vector fields *of any degree*. Since 𝒫 ⊂ C r ​ ( ℝ 2, ℝ 2) \mathcal{P}\subset C^{r}(\mathbb{R}^{2},\mathbb{R}^{2}), we can endow 𝒫 \mathcal{P} with the *subspace topology*τ r \tau_{r}, inherited from Whitney’s weak C r C^{r} -topology. Hence, we set the topological space 𝒫 r = ( 𝒫, τ r) \mathcal{P}^{r}=(\mathcal{P},\tau_{r}). Observe that two vector fields X X, Y ∈ 𝒫 r Y\in\mathcal{P}^{r} are close if there is a “big” compact B ⊂ ℝ 2 B\subset\mathbb{R}^{2} and a small ε > 0 \varepsilon>0 such that

 | max x ∈ B | k | ⩽ r ⁡ | | ∂ | k | X ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) − ∂ | k | Y ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) | | < ε. \max_{\begin{subarray}{c}x\in B\\ |k|\leqslant r\end{subarray}}\left|\left|\frac{\partial^{|k|}X}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)-\frac{\partial^{|k|}Y}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)\right|\right|<\varepsilon. |  |

Let 𝔛 = C ∞ ​ ( ℝ 2, ℝ 2) \mathfrak{X}=C^{\infty}(\mathbb{R}^{2},\mathbb{R}^{2}) be the set of planar smooth vector fields. We endow 𝔛 \mathfrak{X} with Whitney’s strong C ∞ C^{\infty} -topology τ ∞ \tau_{\infty}, see [13, Chapter 2] and [8, Section 2.3 2.3]. Let 𝔛 ∞ = ( 𝔛, τ ∞) \mathfrak{X}^{\infty}=(\mathfrak{X},\tau_{\infty}). Roughly speaking, Y n → X Y_{n}\to X in 𝔛 ∞ \mathfrak{X}^{\infty} if and only if for every r ⩾ 0 r\geqslant 0 finite there is a compact B r ⊂ ℝ 2 B_{r}\subset\mathbb{R}^{2} and n r ∈ ℕ n_{r}\in\mathbb{N} such that

 | lim n → ∞ max x ∈ B r | k | ⩽ r ⁡ | | ∂ | k | Y n ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) − ∂ | k | X ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) | | = 0 \lim\limits_{n\to\infty}\max_{\begin{subarray}{c}x\in B_{r}\\ |k|\leqslant r\end{subarray}}\left|\left|\frac{\partial^{|k|}Y_{n}}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)-\frac{\partial^{|k|}X}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)\right|\right|=0 |  |

and Y n | ℝ 2 ∖ B r = X | ℝ 2 ∖ B R \left.Y_{n}\right|_{\mathbb{R}^{2}\setminus B_{r}}=\left.X\right|_{\mathbb{R}^{2}\setminus B_{R}}, for every n ⩾ n r n\geqslant n_{r}, see Golubitsky and Guillemin [8, p. 43 43]. Given X ∈ 𝔛 ∞ X\in\mathfrak{X}^{\infty} an example of convergence Y n → X Y_{n}\to X, in 𝔛 ∞ \mathfrak{X}^{\infty}, that we shall use in this paper is the one given by Y n = X + 1 n ​ Φ Y_{n}=X+\frac{1}{n}\Phi, where Φ ∈ C ∞ ​ ( ℝ 2, ℝ 2) \Phi\in C^{\infty}(\mathbb{R}^{2},\mathbb{R}^{2}) has compact support.

When interested only in a particular compact set B B, we may restrict 𝔛 ∞ \mathfrak{X}^{\infty} to it and say that Y n → X Y_{n}\to X in 𝔛 ∞ \mathfrak{X}^{\infty} restricted to B B if for every r ⩾ 0 r\geqslant 0 finite we have,

 | lim n → ∞ max x ∈ B | k | ⩽ r ⁡ | | ∂ | k | Y n ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) − ∂ | k | X ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) | | = 0. \lim\limits_{n\to\infty}\max_{\begin{subarray}{c}x\in B\\ |k|\leqslant r\end{subarray}}\left|\left|\frac{\partial^{|k|}Y_{n}}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)-\frac{\partial^{|k|}X}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)\right|\right|=0. |  |

Let Γ n \Gamma^{n} be a hyperbolic polycycle composed by the (not necessarily distinct) hyperbolic saddles { p 1, …, p n } \{p_{1},\dots,p_{n}\}. Let I n I_{n} be the set of the permutations of n n elements. Given σ ∈ I n \sigma\in I_{n} let

 | R 0, σ = R 1, σ − 1, R i, σ = ∏ j = 1 i r σ ⁡ ( j), i ∈ { 1, …, n }, R_{0,\sigma}=R_{1,\sigma}^{-1},\quad R_{i,\sigma}=\prod_{j=1}^{i}r_{\sigma(j)},\quad i\in\{1,\dots,n\}, |  |

where r k r_{k} is the hyperbolicity ratio ( 1) of p k p_{k}. Let also

 | Δ ⁡ ( Γ n, σ) = #⁡ { i ∈ { 1, …, n }: ( R i, σ − 1) ​ ( R i − 1, σ − 1) < 0 }, \Delta(\Gamma^{n},\sigma)=\#\{i\in\{1,\dots,n\}\colon(R_{i,\sigma}-1)(R_{i-1,\sigma}-1)<0\}, |  |

where #​ I \#I denotes the cardinality of I I. Finally, let

 | Δ ⁡ ( Γ n) = max ⁡ { Δ ⁡ ( Γ n, σ): σ ∈ I n }. \Delta(\Gamma^{n})=\max\{\Delta(\Gamma^{n},\sigma)\colon\sigma\in I_{n}\}. |  |

Observe that 0 ⩽ Δ ⁡ ( Γ n) ⩽ n 0\leqslant\Delta(\Gamma^{n})\leqslant n. In particular, Δ ⁡ ( Γ n) = 0 \Delta(\Gamma^{n})=0 if, and only if, r 1 = ⋯ = r n = 1 r_{1}=\dots=r_{n}=1.

Inspired by Roussarie [29, Definition 12 12], we now properly define what we mean when we say that a polycycle Γ n \Gamma^{n} of a vector field X, X, that belongs to a topological spaces 𝔛, \mathfrak{X}, has *cyclicity greater than or equal k. k.*Given two compacts C 1 C_{1}, C 2 ⊂ ℝ 2 C_{2}\subset\mathbb{R}^{2}, recall that the *Hausdorff distance*between them is given by,

 | d H ​ ( C 1, C 2) = max ⁡ { sup x ∈ C 1 d ⁡ ( x, C 2), sup x ∈ C 2 d ⁡ ( C 1, x) }, d_{H}(C_{1},C_{2})=\max\Big\{\sup_{x\in C_{1}}d(x,C_{2}),\sup_{x\in C_{2}}d(C_{1},x)\Big\}, |  |

where d ⁡ ( x, C) = inf { ‖ x − y ‖: y ∈ C } d(x,C)=\inf\{||x-y||\colon y\in C\} is the usual distance between a point and a set in the euclidean space. Then, we will say that Cycl ​ ( X, 𝒳, Γ n) ⩾ k \textit{Cycl }(X,\mathcal{X},\Gamma^{n})\geqslant k if, given any ε > 0 \varepsilon>0 there exists a vector field Y ε ∈ 𝒳, Y_{\varepsilon}\in\mathcal{X}, such that it has at least k k limit cycles γ j ​ ( ε), j = 1, …, k \gamma_{j}(\varepsilon),j=1,\ldots,k such that

 | max ⁡ { d H ​ ( γ j ​ ( ε), Γ n): j ∈ { 1, …, k } } < ε \max\left\{d_{H}(\gamma_{j}(\varepsilon),\Gamma^{n})\colon j\in\{1,\dots,k\}\right\}<\varepsilon |  |

and Y ε Y_{\varepsilon} tends to X X when ε \varepsilon goes to 0 0.

Our main result is the following.

###### Theorem 1.

Let 𝒳 \mathcal{X} be one of the topological spaces 𝔛 ∞ \mathfrak{X}^{\infty} or 𝒫 r \mathcal{P}^{r}, for some r ⩾ 1 r\geqslant 1. If X ∈ 𝒳 X\in\mathcal{X} has a hyperbolic polycycle Γ n \Gamma^{n}, then Cycl ​ ( X, 𝒳, Γ n) ⩾ Δ ⁡ ( Γ n) \textit{Cycl }(X,\mathcal{X},\Gamma^{n})\geqslant\Delta(\Gamma^{n}).

Given a polycycle Γ n \Gamma^{n}, the *trivial permutation*τ ∈ I n \tau\in I_{n} of Γ n \Gamma^{n} is the permutation of the indexes of { p 1, …, p n } \{p_{1},\dots,p_{n}\} such that p i + 1 p_{i+1} and p i p_{i} are the α \alpha and ω \omega -limits of L i L_{i}, respectively, with p n + 1 = p 1 p_{n+1}=p_{1}. See Figure 3.

\begin{overpic}[Fig26.eps] \put(101.0,43.0){$p_{6}$} \put(78.0,85.0){$p_{1}$} \put(14.0,85.0){$p_{2}$} \put(-9.0,43.0){$p_{3}$} \put(14.0,0.0){$p_{4}$} \put(78.0,0.0){$p_{5}$} \par\put(50.0,76.0){$L_{1}$} \put(18.0,63.0){$L_{2}$} \put(12.0,32.0){$L_{3}$} \put(39.0,9.0){$L_{4}$} \put(72.0,23.0){$L_{5}$} \put(74.0,59.0){$L_{6}$} \par\end{overpic}

( a) (a)

\begin{overpic}[Fig26.eps] \put(101.0,43.0){$p_{6}$} \put(78.0,85.0){$p_{3}$} \put(14.0,85.0){$p_{2}$} \put(-9.0,43.0){$p_{4}$} \put(14.0,0.0){$p_{1}$} \put(78.0,0.0){$p_{5}$} \par\put(50.0,76.0){$L_{3}$} \put(18.0,63.0){$L_{2}$} \put(12.0,32.0){$L_{4}$} \put(39.0,9.0){$L_{1}$} \put(72.0,23.0){$L_{5}$} \put(74.0,59.0){$L_{6}$} \end{overpic}

( b) (b)

Figure 3. Illustration of Γ 6 \Gamma^{6} with ( a) (a) trivial and ( b) (b) non trivial permutation on the indexes of the singularities.

The case X ∈ 𝔛 ∞ X\in\mathfrak{X}^{\infty} of our main result is an extension of [11, Theorem 1.1 1.1] that corresponds to the case Δ ⁡ ( Γ n, τ) = n \Delta(\Gamma^{n},\tau)=n where τ \tau is the trivial permutation of Γ n \Gamma^{n}. Our proof is inspired in the ideas of that paper but it is more detailed and transparent because it relies on recent results of Marin and Villadelaprat [18, 19, 21] that give regularity properties with respect initial conditions and parameters of the Dulac map associated to the hyperbolic sectors of hyperbolic saddles for families of vector fields, see Section 2.1. We comment in more detail about the differences between our proof and that of [11] in Remark 7.

The result in the polynomial case X ∈ 𝒫 r X\in\mathcal{P}^{r} is totally new. It is motivated by the only open problem left in order to get a complete characterization of the structurable stable polynomials vector fields of degree n n with the topology of the coefficients. This open problem consists on knowing whether non-hyperbolic limit cycles of odd multiplicity can be structurable stables or not, see [30, 32, 35]. Although we have not advanced on this question we have achieved a related result. More concretely, under generic conditions, we have been able to bifurcate n n limit cycles from a polycycle Γ n \Gamma^{n} of a polynomial vector field X X with a polynomial perturbation and without losing control of its derivatives in any prescribed compact. Unfortunately, we have not been able to perform this unfold with the degree of the perturbations equals to the one of X X.

In a few words, in the case Δ ⁡ ( Γ n) = n \Delta(\Gamma^{n})=n what we prove is that starting from Γ n \Gamma^{n} we can perturb X X such that from Γ n \Gamma^{n} bifurcate a limit cycle and a new polycycle Γ n − 1, \Gamma^{n-1}, satisfying similar hypotheses to the ones of Γ n. \Gamma^{n}. Then, this process can be repeated n − 1 n-1 times until arriving to n n limit cycles, all near Γ n. \Gamma^{n}. The technical part of the proof is the control of the continuity and differentiability, with respect to initial conditions and parameters, of the various return maps associated to the appearing polycycles.

The paper is structured as follows. In Section 2 we recall some preliminary results about the Dulac and the displacement maps. In Section 3 we work on the displacement map between non-subsequent saddles. In Section 4 we prove some technical lemmas about the approximation of planar smooth functions by polynomials functions; the existence of positive or negative invariant regions; and the perturbation of periodic orbits. Theorem 1 is proved in Section 5. In Section 6 we solve the inverse problem of constructing a vector field X X with a polycycle Γ n \Gamma^{n} with any given set of prescribed hyperbolicity ratios and we apply our techniques to a concrete polynomial example. At Section 7 we include some brief considerations about the current state of the theory of unfolding of polycycles and how our results can be applied to it, specially in the polynomial case.

## 2. Dulac and displacement maps

### 2.1. The Dulac map

Let X μ X_{\mu} be a planar smooth vector field depending on a smooth way on a parameter μ ∈ ℝ N \mu\in\mathbb{R}^{N}, N ⩾ 1 N\geqslant 1, defined in a neighborhood of a hyperbolic saddle p p at μ = 0 \mu=0. Since p p is hyperbolic, it follows that if Λ ⊂ ℝ N \Lambda\subset\mathbb{R}^{N} is a small enough neighborhood of the origin, then the perturbation p ⁡ ( μ) p(\mu) of p p is well defined and it is also a hyperbolic saddle, for every μ ∈ Λ \mu\in\Lambda. Moreover, restricting Λ \Lambda if necessary, it is well known (see Lemma 4.3 4.3 of [19]) that there are neighborhoods U ⊂ ℝ 2 U\subset\mathbb{R}^{2} of p p and V ⊂ ℝ 2 V\subset\mathbb{R}^{2} of the origin 𝒪 \mathcal{O}, and a smooth map Φ: U × Λ → V \Phi:U\times\Lambda\to V such that for each μ ∈ Λ \mu\in\Lambda the map Φ ⁡ ( ⋅, μ): U → V \Phi(\cdot,\mu)\colon U\to V is a smooth change of coordinates that sends p ⁡ ( μ) p(\mu) to the origin 𝒪 \mathcal{O} and its (local) unstable and stable manifolds ℓ u ​ ( μ) \ell^{u}(\mu) and ℓ s ​ ( μ) \ell^{s}(\mu) to the axis O ​ x Ox and O ​ y Oy, respectively. By abuse of notation we still denote this new vector field by X μ X_{\mu}. Given ε > 0 \varepsilon>0 small, let σ: ( − ε, ε) × Λ → Σ σ \sigma\colon(-\varepsilon,\varepsilon)\times\Lambda\to\Sigma_{\sigma} and τ: ( − ε, ε) × Λ → Σ τ \tau\colon(-\varepsilon,\varepsilon)\times\Lambda\to\Sigma_{\tau} be two C ∞ C^{\infty} transverse sections to X μ X_{\mu} defined by

 | σ ⁡ ( s, μ) = ( σ 1 ​ ( s, μ), σ 2 ​ ( s, μ)), τ ⁡ ( s, μ) = ( τ 1 ​ ( s, μ), τ 2 ​ ( s, μ)), \sigma(s,\mu)=(\sigma_{1}(s,\mu),\sigma_{2}(s,\mu)),\quad\tau(s,\mu)=(\tau_{1}(s,\mu),\tau_{2}(s,\mu)), |  |

and such that σ 1 ​ ( 0, μ) = 0 \sigma_{1}(0,\mu)=0 and τ 2 ​ ( 0, μ) = 0 \tau_{2}(0,\mu)=0, for every μ ∈ Λ \mu\in\Lambda. Suppose also that if s > 0 s>0, then σ 1 ​ ( s, μ) > 0 \sigma_{1}(s,\mu)>0 and τ 2 ​ ( s, μ) > 0 \tau_{2}(s,\mu)>0. Let

 | Σ σ + = { σ ⁡ ( s, μ) ∈ Σ σ: s > 0 }, Σ τ + = { τ ⁡ ( s, μ) ∈ Σ σ: s > 0 }. \Sigma_{\sigma}^{+}=\{\sigma(s,\mu)\in\Sigma_{\sigma}\colon s>0\},\quad\Sigma_{\tau}^{+}=\{\tau(s,\mu)\in\Sigma_{\sigma}\colon s>0\}. |  |

Let also φ ⁡ ( t, x, μ) \varphi(t,x;\mu) be the solution of X μ X_{\mu} passing through x ∈ V x\in V at t = 0 t=0. On the first quadrant, φ \varphi defines a transition map Σ σ + ↦ Σ τ + \Sigma_{\sigma}^{+}\mapsto\Sigma_{\tau}^{+}, which can be seen as a map

(3) |  | D: ( 0, ε) × Λ → ( 0, ε), D\colon(0,\varepsilon)\times\Lambda\to(0,\varepsilon), |  |

due to the transverses section σ \sigma and τ \tau. See Figure 4.

\begin{overpic}[Fig16.eps] \put(52.0,45.0){$\Sigma_{\sigma}$} \put(23.0,36.0){$\sigma$} \put(1.0,25.0){$0$} \put(9.0,26.0){$s$} \par\put(72.0,23.0){$\Sigma_{\tau}$} \put(87.0,24.0){$\tau$} \put(87.5,37.0){$0$} \put(94.0,37.0){$D(s)$} \par\put(32.0,2.0){$\mathcal{O}$} \put(28.0,50.0){$Oy^{+}$} \put(80.0,3.0){$Ox^{+}$} \put(48.0,25.0){$\varphi(\cdot,\sigma(s);\mu)$} \end{overpic} Figure 4. The Dulac map near a hyperbolic saddle.

The map ( 3) is the *Dulac map*. In recently years, Marin and Villadelprat [18, 19, 21] provided a full characterization of the Dulac map (and also of the Dulac time). In what follows, we will state some properties of the Dulac map, that will be sufficient for the objectives of this paper. We recall that r ⁡ ( μ) r(\mu) denotes the hiperbolicity ratio ( 1) of the hyperbolic saddle p ⁡ ( μ) p(\mu), μ ∈ Λ \mu\in\Lambda.

###### Proposition 1.

If r ⁡ ( 0) > 1 r(0)>1, then the Dulac map ( 3) can be extended to s = 0 s=0 in a C 1 C^{1} -way and can be written as

 | D ⁡ ( s, μ) = Δ 00 ​ ( μ) ​ s r ⁡ ( μ) + ℛ ⁡ ( s, μ), D(s,\mu)=\Delta_{00}(\mu)s^{r(\mu)}+\mathscr{R}(s,\mu), |  |

where Δ 00: Λ → ℝ \Delta_{00}\colon\Lambda\to\mathbb{R} is a strictly positive function of class C ∞ C^{\infty} and ℛ: [0, ε) × Λ → ℝ \mathscr{R}\colon[0,\varepsilon)\times\Lambda\to\mathbb{R} is a function of class C 1 C^{1} satisfying

 | ℛ ⁡ ( 0, μ) = 0, ∂ ℛ ∂ s ​ ( 0, μ) = 0, ∂ ℛ ∂ μ j ​ ( 0, μ) = 0, \mathscr{R}(0,\mu)=0,\quad\frac{\partial\mathscr{R}}{\partial s}(0,\mu)=0,\quad\frac{\partial\mathscr{R}}{\partial\mu_{j}}(0,\mu)=0, |  |

for every μ ∈ Λ \mu\in\Lambda and j ∈ { 1, …, N } j\in\{1,\dots,N\}. In particular,

 | lim s → 0 + D ⁡ ( s, μ) = 0, lim s → 0 + ∂ D ∂ s ​ ( s, μ) = 0, lim s → 0 + ∂ D ∂ μ j ​ ( s, μ) = 0, \lim\limits_{s\to 0^{+}}D(s,\mu)=0,\quad\lim\limits_{s\to 0^{+}}\frac{\partial D}{\partial s}(s,\mu)=0,\quad\lim\limits_{s\to 0^{+}}\frac{\partial D}{\partial\mu_{j}}(s,\mu)=0, |  |

for every μ ∈ Λ \mu\in\Lambda and j ∈ { 1, …, N } j\in\{1,\dots,N\}.

###### Remark 1.

Under the notation of [19, Theorem B B], Proposition 1 follows by taking L = r ⁡ ( 0) L=r(0) and by replacing the flat term by its C 1 C^{1} extension, which existence follows from r ⁡ ( 0) > 1 r(0)>1. See Remark 3 3 right after [19, Theorem B B].

Observe that if we invert the time variable, then the solution of − X μ -X_{\mu} defines a transition map Σ τ + ↦ Σ σ + \Sigma_{\tau}^{+}\mapsto\Sigma_{\sigma}^{+} which can be seen as a map

(4) |  | D − 1: ( 0, ε) × Λ → ( 0, ε), D^{-1}\colon(0,\varepsilon)\times\Lambda\to(0,\varepsilon), |  |

satisfying

 | D − 1 ​ ( D ⁡ ( s), μ) = s, D ⁡ ( D − 1 ​ ( s), μ) = s, D^{-1}(D(s),\mu)=s,\quad D(D^{-1}(s),\mu)=s, |  |

for every μ ∈ Λ \mu\in\Lambda. Since the hyperbolicity ratio of 𝒪 \mathcal{O} in relation to − X μ -X_{\mu} is given by r ​ ( μ) − 1 r(\mu)^{-1} and D − 1 D^{-1} is the Dulac map of − X μ -X_{\mu}, we also have the following result.

###### Proposition 2.

If r ⁡ ( 0) < 1 r(0)<1, then the Dulac map ( 4) can be extended to s = 0 s=0 in a C 1 C^{1} -way and can be written as

 | D − 1 ​ ( s, μ) = Δ 00 ∗ ​ ( μ) ​ s 1 r ⁡ ( μ) + ℛ ∗ ​ ( s, μ), D^{-1}(s,\mu)=\Delta_{00}^{*}(\mu)s^{\frac{1}{r(\mu)}}+\mathscr{R}^{*}(s,\mu), |  |

where Δ 00 ∗: Λ → ℝ \Delta_{00}^{*}\colon\Lambda\to\mathbb{R} is a strictly positive function of class C ∞ C^{\infty} and ℛ ∗: [0, ε) × Λ → ℛ \mathscr{R}^{*}\colon[0,\varepsilon)\times\Lambda\to\mathscr{R} is a function of class C 1 C^{1} satisfying

 | ℛ ∗ ​ ( 0, μ) = 0, ∂ ℛ ∗ ∂ s ​ ( 0, μ) = 0, ∂ ℛ ∗ ∂ μ j ​ ( 0, μ) = 0, \mathscr{R}^{*}(0,\mu)=0,\quad\frac{\partial\mathscr{R}^{*}}{\partial s}(0,\mu)=0,\quad\frac{\partial\mathscr{R}^{*}}{\partial\mu_{j}}(0,\mu)=0, |  |

for every μ ∈ Λ \mu\in\Lambda and j ∈ { 1, …, N } j\in\{1,\dots,N\}. In particular,

 | lim s → 0 + D − 1 ​ ( s, μ) = 0, lim s → 0 + ∂ D − 1 ∂ s ​ ( s, μ) = 0, lim s → 0 + ∂ D − 1 ∂ μ j ​ ( s, μ) = 0, \lim\limits_{s\to 0^{+}}D^{-1}(s,\mu)=0,\quad\lim\limits_{s\to 0^{+}}\frac{\partial D^{-1}}{\partial s}(s,\mu)=0,\quad\lim\limits_{s\to 0^{+}}\frac{\partial D^{-1}}{\partial\mu_{j}}(s,\mu)=0, |  |

for every μ ∈ Λ \mu\in\Lambda and j ∈ { 1, …, N } j\in\{1,\dots,N\}.

###### Remark 2 (Theorem B B and Lemma 4.3 4.3 of [19]).

The smooth change of coordinates Φ: U × Λ → V \Phi\colon U\times\Lambda\to V that sends p ⁡ ( μ) p(\mu) to the origin and the unstable and stable manifolds ℓ u ​ ( μ) \ell^{u}(\mu) and ℓ s ​ ( μ) \ell^{s}(\mu) to the axis O ​ x Ox and O ​ y Oy is not necessarily for the characterization of the Dulac map. Moreover, the transverse sections Σ σ \Sigma_{\sigma} and Σ τ \Sigma_{\tau} does not need to be sufficiently close to p ⁡ ( μ) p(\mu). In particular, no normal form is needed to apply Propositions 1 and 2.

### 2.2. The displacement map

Let X X be a planar smooth vector field with polycycle Γ n \Gamma^{n} composed by n n hyperbolic saddles p i p_{i}, i ∈ { 1, …, n } i\in\{1,\dots,n\}. In what follows, Γ n \Gamma^{n} is endowed with the trivial permutation unless explicitly stated otherwise. Without loss of generality, suppose that Γ n \Gamma^{n} is oriented in the clockwise way. Let L i L_{i} be the regular orbit of X X from p i + 1 p_{i+1} to p i p_{i} (i.e. ω ⁡ ( L i) = p i \omega(L_{i})=p_{i} and α ⁡ ( L i) = p i + 1 \alpha(L_{i})=p_{i+1}, with p n + 1 = p 1 p_{n+1}=p_{1}). Let X = ( P, Q) X=(P,Q) and define X ⟂ = ( − Q, P) X^{\perp}=(-Q,P). For each i ∈ { 1, …, n } i\in\{1,\dots,n\}, let x i ∈ L i x_{i}\in L_{i} and let l i l_{i} be the normal section of L i L_{i}, at x i x_{i}, with the directed vector

(5) |  | v i = 1 ‖ X ⟂ ​ ( x i) ‖ ​ X ⟂ ​ ( x i). v_{i}=\frac{1}{||X^{\perp}(x_{i})||}X^{\perp}(x_{i}). |  |

Let X μ X_{\mu} be a smooth perturbation of X X, with μ ∈ ℝ N \mu\in\mathbb{R}^{N}, N ⩾ 1 N\geqslant 1, and X 0 = X X_{0}=X. Since the saddles p i p_{i} are hyperbolic, it follows that if Λ ⊂ ℝ N \Lambda\subset\mathbb{R}^{N} is a small enough neighborhood of the origin and μ ∈ Λ \mu\in\Lambda, then the perturbation p i ​ ( μ) p_{i}(\mu) of p i p_{i} is well defined and it is also a hyperbolic saddle. For each i ∈ { 1, …, n } i\in\{1,\dots,n\}, let L i s ​ ( μ) L_{i}^{s}(\mu) and L i u ​ ( μ) L_{i}^{u}(\mu) be the perturbations of L i L_{i} such that ω ⁡ ( L i s ​ ( μ)) = p i ​ ( μ) \omega(L_{i}^{s}(\mu))=p_{i}(\mu) and α ⁡ ( L i u ​ ( μ)) = p i + 1 ​ ( μ) \alpha(L_{i}^{u}(\mu))=p_{i+1}(\mu). Let also x i s ​ ( μ) x_{i}^{s}(\mu) and x i u ​ ( μ) x_{i}^{u}(\mu) be the intersections of L i s ​ ( μ) L_{i}^{s}(\mu) and L i u ​ ( μ) L_{i}^{u}(\mu) with l i l_{i}, respectively. See Figure 5.

\begin{overpic}[Fig1.eps] \put(88.0,57.0){$p_{2}$} \put(17.0,55.0){$p_{3}$} \put(68.0,4.0){$p_{1}$} \put(49.0,51.5){$x_{2}$} \put(37.0,23.0){$x_{3}$} \put(76.0,37.0){$x_{1}$} \put(70.0,57.0){$L_{2}$} \put(20.0,32.0){$L_{3}$} \put(76.0,18.0){$L_{1}$} \put(49.0,60.0){$l_{2}$} \put(31.0,15.0){$l_{3}$} \put(87.0,40.0){$l_{1}$} \end{overpic}

Unperturbed

\begin{overpic}[Fig2.eps] \put(84.0,57.0){$p_{2}$} \put(6.0,53.0){$p_{3}$} \put(65.0,0.0){$p_{1}$} \par\put(47.0,56.0){$x_{2}^{u}$} \put(39.0,49.0){$x_{2}^{s}$} \put(25.0,59.0){$L_{2}^{u}$} \put(55.0,44.0){$L_{2}^{s}$} \par\put(29.0,25.0){$x_{3}^{u}$} \put(29.0,14.0){$x_{3}^{s}$} \put(49.0,16.0){$L_{3}^{u}$} \put(12.0,28.0){$L_{3}^{s}$} \par\put(75.0,33.0){$x_{1}^{u}$} \put(85.0,38.0){$x_{1}^{s}$} \put(73.0,45.0){$L_{1}^{u}$} \put(84.0,18.0){$L_{1}^{s}$} \end{overpic}

Perturbed

Figure 5. An example of a perturbation of Γ 3 \Gamma^{3}, with d 1 ​ ( μ) < 0 d_{1}(\mu)<0, d 2 ​ ( μ) > 0 d_{2}(\mu)>0 and d 3 ​ ( μ) < 0 d_{3}(\mu)<0. For simplicity, we omitted the dependence on μ \mu in the expressions of x i s, u x_{i}^{s,u} and L i s, u L_{i}^{s,u}.

Observe that a point q ∈ l i q\in l_{i} can be represented as q = x i + λ ​ v i q=x_{i}+\lambda v_{i}. Hence, for each i ∈ { 1, …, n } i\in\{1,\dots,n\}, let b i s ​ ( μ) b_{i}^{s}(\mu), b i u ​ ( μ) ∈ ℝ b_{i}^{u}(\mu)\in\mathbb{R} be such that,

(6) |  | x i s ​ ( μ) = x i + b i s ​ ( μ) ​ v i, x i u ​ ( μ) = x i + b i u ​ ( μ) ​ v i. x_{i}^{s}(\mu)=x_{i}+b_{i}^{s}(\mu)v_{i},\quad x_{i}^{u}(\mu)=x_{i}+b_{i}^{u}(\mu)v_{i}. |  |

The *displacement function*d i: Λ → ℝ d_{i}\colon\Lambda\to\mathbb{R} is given by,

(7) |  | d i ​ ( μ) = b i u ​ ( μ) − b i s ​ ( μ). d_{i}(\mu)=b_{i}^{u}(\mu)-b_{i}^{s}(\mu). |  |

It follows from Perko [28, Lemma 2 2] and Guckenheimer and Holmes [9, Section 4.5] that if Λ \Lambda is a small enough, then d i d_{i} is a well defined function of class C ∞ C^{\infty}. Moreover if we write X μ ​ ( x) = X ⁡ ( x) + K ⁡ ( x, μ) X_{\mu}(x)=X(x)+K(x,\mu), with K ⁡ ( x, 0) ≡ 0 K(x,0)\equiv 0, then the partial derivatives of d i d_{i} at μ = 0 \mu=0 are given by

(8) |  | ∂ d i ∂ μ j ( 0) = 1 ‖ X ⁡ ( x i) ‖ ∫ − ∞ + ∞ e − ∫ 0 t div X ( γ i ( s)) d s X ( γ i ( t)) ∧ ∂ K ∂ μ j ( γ i ( t), 0) d t, \frac{\partial d_{i}}{\partial\mu_{j}}(0)=\frac{1}{||X(x_{i})||}\int_{-\infty}^{+\infty}e^{-\int_{0}^{t}\operatorname{div}X(\gamma_{i}(s))\;ds}X(\gamma_{i}(t))\land\frac{\partial K}{\partial\mu_{j}}(\gamma_{i}(t),0)\;dt, |  |

where ( x 1, y 1) ∧ ( x 2, y 2) = x 1 ​ y 2 − x 2 ​ y 1 (x_{1},y_{1})\land(x_{2},y_{2})=x_{1}y_{2}-x_{2}y_{1} and γ i ​ ( t) \gamma_{i}(t) is the parametrization of L i L_{i} given by the solution of X X, with initial condition γ i ​ ( 0) = x i \gamma_{i}(0)=x_{i}. For more details, we also refer to the survey of Blows and Perko [3].

###### Remark 3.

From [28, Lemma 1 1] and [9, Section 4.5] it can be seen that the functions b i u b_{i}^{u}, b i s: Λ → ℝ b_{i}^{s}\colon\Lambda\to\mathbb{R}, given at ( 7) are also of class C ∞ C^{\infty}, individually.

###### Remark 4.

We observe that both in [28, Lemma 2 2] and [9, Section 4.5], the displacement map ( 7) is constructed for loops, i.e. for polycycles Γ 1 \Gamma^{1}. However, it is clear from the proofs of such results that the hypothesis of having a loop is not necessary. Actually, the existence of the polycycle itself is not necessary. Only the existence of a connection between two saddles, which may be the same.

## 3. The displacement map between non-subsequent saddles

Under the context of Section 2.2, let σ 0 ∈ { − 1, 1 } \sigma_{0}\in\{-1,1\} be given by σ 0 = − 1 \sigma_{0}=-1 (resp. OPEN σ 0 = 1) \sigma_{0}=1) if the first return map associated to Γ n \Gamma^{n} is defined in the inner (resp. outer) region defined by Γ n \Gamma^{n}. Suppose n ⩾ 2 n\geqslant 2. Observe that if σ 0 ​ d n ​ ( μ) > 0 \sigma_{0}d_{n}(\mu)>0, then the intersection

 | L n u ​ ( μ) ∩ l n − 1 = { x n − 1 ( 1) ​ ( μ) }, L_{n}^{u}(\mu)\cap l_{n-1}=\left\{x_{n-1}^{(1)}(\mu)\right\}, |  |

is well defined, see Figure 7. Similarly, if σ 0 ​ d n − 1 ​ ( μ) < 0 \sigma_{0}d_{n-1}(\mu)<0, then

 | L n − 1 s ​ ( μ) ∩ l n = { x n ( 1) ​ ( μ) } L_{n-1}^{s}(\mu)\cap l_{n}=\left\{x_{n}^{(1)}(\mu)\right\} |  |

is also well defined, see Figure 7.

\begin{overpic}[Fig3.eps] \put(55.0,40.0){$x_{2}^{s}(\mu)$} \put(62.0,62.0){$x_{2}^{(1)}(\mu)$} \put(26.0,12.0){$x_{3}^{s}(\mu)$} \put(21.0,61.0){$x_{2}^{u}(\mu)$} \put(51.0,27.5){$x_{3}^{u}(\mu)$} \par\put(84.0,57.0){$p_{2}$} \put(6.0,53.0){$p_{3}$} \put(65.0,0.0){$p_{1}$} \end{overpic}

σ 0 = − 1 \sigma_{0}=-1 and n = 3 n=3.

\begin{overpic}[Fig3x.eps] \put(78.0,62.0){$x_{1}^{s}(\mu)$} \put(39.0,43.5){$x_{1}^{u}(\mu)$} \put(45.0,32.5){$x_{1}^{(1)}(\mu)$} \put(62.0,22.0){$x_{2}^{s}(\mu)$} \put(19.0,-1.0){$x_{2}^{u}(\mu)$} \par\put(95.0,31.0){$p_{1}$} \put(13.0,31.5){$p_{2}$} \end{overpic}

σ 0 = 1 \sigma_{0}=1 and n = 2 n=2.

Figure 6. An illustration of x n − 1 ( 1) x_{n-1}^{(1)}.

\begin{overpic}[Fig4.eps] \put(46.0,32.0){$x_{3}^{u}(\mu)$} \put(4.0,18.0){$x_{3}^{s}(\mu)$} \put(11.0,6.0){$x_{3}^{(1)}(\mu)$} \par\put(61.0,60.0){$x_{2}^{u}(\mu)$} \put(60.0,43.0){$x_{2}^{s}(\mu)$} \par\put(84.0,57.0){$p_{2}$} \put(6.0,53.0){$p_{3}$} \put(65.0,0.0){$p_{1}$} \end{overpic}

σ 0 = − 1 \sigma_{0}=-1 and n = 3 n=3.

\begin{overpic}[Fig4x.eps] \put(78.0,62.0){$x_{1}^{s}(\mu)$} \put(39.0,43.5){$x_{1}^{u}(\mu)$} \put(64.0,16.0){$x_{2}^{(1)}(\mu)$} \put(49.0,24.5){$x_{2}^{s}(\mu)$} \put(19.0,-1.0){$x_{2}^{u}(\mu)$} \par\put(95.0,31.0){$p_{1}$} \put(13.0,31.5){$p_{2}$} \end{overpic}

σ 0 = 1 \sigma_{0}=1 and n = 2 n=2.

Figure 7. An illustration of x n ( 1) x_{n}^{(1)}.

Similarly to ( 6), let (when well defined) b n − 1 ( 1) ​ ( μ) b_{n-1}^{(1)}(\mu), b n ( 1) ​ ( μ) ∈ ℝ b_{n}^{(1)}(\mu)\in\mathbb{R} be such that,

(9) |  | x n − 1 ( 1) ​ ( μ) = x n − 1 + b n − 1 ( 1) ​ ( μ) ​ v n − 1, x n ( 1) ​ ( μ) = x n + b n ( 1) ​ ( μ) ​ v n. x_{n-1}^{(1)}(\mu)=x_{n-1}+b_{n-1}^{(1)}(\mu)v_{n-1},\quad x_{n}^{(1)}(\mu)=x_{n}+b_{n}^{(1)}(\mu)v_{n}. |  |

Suppose r n > 1 r_{n}>1. In this case, we define the displacement map d n − 1 ( 1): Λ → ℝ d_{n-1}^{(1)}\colon\Lambda\to\mathbb{R} by

(10) |  | d n − 1 ( 1) ​ ( μ) = { b n − 1 u ​ ( μ) − b n − 1 s ​ ( μ), if ​ σ 0 ​ d n ​ ( μ) ⩽ 0, b n − 1 ( 1) ​ ( μ) − b n − 1 s ​ ( μ), if ​ σ 0 ​ d n ​ ( μ) > 0. d_{n-1}^{(1)}(\mu)=\left\{\begin{array}[]{ll}b_{n-1}^{u}(\mu)-b_{n-1}^{s}(\mu),&\text{if }\sigma_{0}d_{n}(\mu)\leqslant 0,\\ b_{n-1}^{(1)}(\mu)-b_{n-1}^{s}(\mu),&\text{if }\sigma_{0}d_{n}(\mu)>0.\end{array}\right. |  |

###### Proposition 3.

If r n > 1 r_{n}>1, then the displacement map ( 10) is a well defined function of class C 1 C^{1}.

###### Proof.

For simplicity, assume first that σ 0 = − 1 \sigma_{0}=-1, i.e. the displacement map is in the inner region of Γ n \Gamma^{n}. In this case, it follows from ( 10) that,

(11) |  | d n − 1 ( 1) ​ ( μ) = { b n − 1 u ​ ( μ) − b n − 1 s ​ ( μ), if ​ d n ​ ( μ) ⩾ 0, b n − 1 ( 1) ​ ( μ) − b n − 1 s ​ ( μ), if ​ d n ​ ( μ) < 0. d_{n-1}^{(1)}(\mu)=\left\{\begin{array}[]{ll}b_{n-1}^{u}(\mu)-b_{n-1}^{s}(\mu),&\text{if }d_{n}(\mu)\geqslant 0,\\ b_{n-1}^{(1)}(\mu)-b_{n-1}^{s}(\mu),&\text{if }d_{n}(\mu)<0.\end{array}\right. |  |

Let μ ∈ Λ \mu\in\Lambda be such that d n ​ ( μ) < 0 d_{n}(\mu)<0. It follows from ( 7) and ( 11) that,

(12) |  | d n − 1 ( 1) ​ ( μ) = d n − 1 ​ ( μ) + ( b n − 1 ( 1) ​ ( μ) − b n − 1 u ​ ( μ)). d_{n-1}^{(1)}(\mu)=d_{n-1}(\mu)+\bigl(b_{n-1}^{(1)}(\mu)-b_{n-1}^{u}(\mu)\bigr). |  |

For every i ∈ { 1, …, n } i\in\{1,\dots,n\}, let u i = − v i u_{i}=-v_{i} (recall from ( 5) that v i v_{i} points outwards Γ n \Gamma^{n} and thus u i u_{i} points inwards). Given q ∈ l n q\in l_{n}, observe that there exists a unique ξ ⩾ 0 \xi\geqslant 0 such that,

(13) |  | q = x n s ​ ( μ) + ξ ​ u n. q=x_{n}^{s}(\mu)+\xi u_{n}. |  |

In particular, ξ = 0 \xi=0 if and only if, q = x n s ​ ( μ) q=x_{n}^{s}(\mu). If ξ ⩾ 0 \xi\geqslant 0 is small enough, then the orbit of X μ X_{\mu} through q = q ⁡ ( ξ) q=q(\xi) will intersect l n − 1 l_{n-1} in the point p = p ⁡ ( ξ) p=p(\xi) given

(14) |  | p = x n − 1 u ​ ( μ) + D n ​ ( ξ, μ) ​ u n − 1, p=x_{n-1}^{u}(\mu)+D_{n}(\xi,\mu)u_{n-1}, |  |

where D n: l n × Λ → l n − 1 D_{n}\colon l_{n}\times\Lambda\to l_{n-1} is the Dulac map associated to p n ​ ( μ) p_{n}(\mu), see Figure 7. From ( 6),

(15) |  | x n u ​ ( μ) = ( x n + b n s ​ ( μ) ​ v n) + ( b n u ​ ( μ) − b n s ​ ( μ)) ​ v n = x n s ​ ( μ) + d n ​ ( μ) ​ v n, x_{n}^{u}(\mu)=\bigl(x_{n}+b_{n}^{s}(\mu)v_{n}\bigr)+\bigl(b_{n}^{u}(\mu)-b_{n}^{s}(\mu)\bigr)v_{n}=x_{n}^{s}(\mu)+d_{n}(\mu)v_{n}, |  |

and from ( 9) we have,

(16) |  | x n − 1 ( 1) ​ ( μ) = ( x n − 1 + b n − 1 u ​ ( μ) ​ v n − 1) + ( b n − 1 ( 1) ​ ( μ) − b n − 1 u ​ ( μ)) ​ v n − 1 = x n − 1 u ​ ( μ) + ( b n − 1 ( 1) ​ ( μ) − b n − 1 u ​ ( μ)) ​ v n − 1. x_{n-1}^{(1)}(\mu)=\bigl(x_{n-1}+b_{n-1}^{u}(\mu)v_{n-1}\bigr)+\bigl(b_{n-1}^{(1)}(\mu)-b_{n-1}^{u}(\mu)\bigr)v_{n-1}=x_{n-1}^{u}(\mu)+\bigl(b_{n-1}^{(1)}(\mu)-b_{n-1}^{u}(\mu)\bigr)v_{n-1}. |  |

Hence, if we let q = x n u ​ ( μ) q=x_{n}^{u}(\mu), then it follows from ( 13) and ( 15) that ξ = − d n ​ ( μ) \xi=-d_{n}(\mu) (recall that d n ​ ( μ) < 0 d_{n}(\mu)<0). Since x n − 1 ( 1) ​ ( μ) x_{n-1}^{(1)}(\mu) is the intersection of the positive orbit through x n u ​ ( μ) x_{n}^{u}(\mu) with l n − 1 l_{n-1}, it follows from ( 14) and ( 16) that,

 | b n − 1 ( 1) ​ ( μ) − b n − 1 u ​ ( μ) = − D n ​ ( − d n ​ ( μ), μ). b_{n-1}^{(1)}(\mu)-b_{n-1}^{u}(\mu)=-D_{n}(-d_{n}(\mu),\mu). |  |

Therefore, it follows from ( 12) that if d n ​ ( μ) < 0 d_{n}(\mu)<0, then

(17) |  | d n − 1 ( 1) ​ ( μ) = d n − 1 ​ ( μ) − D n ​ ( − d n ​ ( μ), μ). d_{n-1}^{(1)}(\mu)=d_{n-1}(\mu)-D_{n}(-d_{n}(\mu),\mu). |  |

Hence, as a consequence of ( 11) and ( 17) we arrive to

 | d n − 1 ( 1) ​ ( μ) = d n − 1 ​ ( μ) + R ⁡ ( μ), d_{n-1}^{(1)}(\mu)=d_{n-1}(\mu)+R(\mu), |  |

where R: Λ → ℝ R\colon\Lambda\to\mathbb{R} is given by

 | R ⁡ ( μ) = { 0, if ​ d n ​ ( μ) ⩾ 0, − D n ​ ( − d n ​ ( μ), μ), if ​ d n ​ ( μ) < 0. R(\mu)=\left\{\begin{array}[]{ll}0,&\text{if }d_{n}(\mu)\geqslant 0,\\ -D_{n}(-d_{n}(\mu),\mu),&\text{if }d_{n}(\mu)<0.\end{array}\right. |  |

Since r n > 1 r_{n}>1, it follows from Proposition 1 and Remark 2 that if d n ​ ( μ) < 0 d_{n}(\mu)<0, then

(18) |  | ∂ R ∂ μ j ​ ( μ) = ∂ D n ∂ s ​ ( − d n ​ ( μ), μ) ​ ∂ d n ∂ μ j ​ ( μ) − ∂ D n ∂ μ j ​ ( − d n ​ ( μ), μ). \frac{\partial R}{\partial\mu_{j}}(\mu)=\frac{\partial D_{n}}{\partial s}(-d_{n}(\mu),\mu)\frac{\partial d_{n}}{\partial\mu_{j}}(\mu)-\frac{\partial D_{n}}{\partial\mu_{j}}(-d_{n}(\mu),\mu). |  |

Hence, if we take μ 0 ∈ d n − 1 ​ ( { 0 }) \mu_{0}\in d_{n}^{-1}(\{0\}), then from ( 18) and Proposition 1 we know that,

 | lim μ → μ 0 ∂ R ∂ μ j ​ ( μ) = 0, lim μ → μ 0 R ⁡ ( μ) = 0. \lim\limits_{\mu\to\mu_{0}}\frac{\partial R}{\partial\mu_{j}}(\mu)=0,\quad\lim\limits_{\mu\to\mu_{0}}R(\mu)=0. |  |

Therefore, R R is of class C 1 C^{1} and thus d n − 1 ( 1) d_{n-1}^{(1)} is also C 1 C^{1}. The proof for the case σ 0 = 1 \sigma_{0}=1 follows similarly. We only observe that in general we have u i = σ 0 ​ v i u_{i}=\sigma_{0}v_{i} and

 | d n − 1 ( 1) ​ ( μ) = d n − 1 ​ ( μ) + R σ 0 ​ ( μ), d_{n-1}^{(1)}(\mu)=d_{n-1}(\mu)+R_{\sigma_{0}}(\mu), |  |

where,

 | R σ 0 ​ ( μ) = { 0, if ​ σ 0 ​ d n ​ ( μ) ⩽ 0, σ 0 ​ D n ​ ( σ 0 ​ d n ​ ( μ), μ), if ​ σ 0 ​ d n ​ ( μ) > 0. R_{\sigma_{0}}(\mu)=\left\{\begin{array}[]{ll}0,&\text{if }\sigma_{0}d_{n}(\mu)\leqslant 0,\\ \sigma_{0}D_{n}(\sigma_{0}d_{n}(\mu),\mu),&\text{if }\sigma_{0}d_{n}(\mu)>0.\end{array}\right. |  |

This finishes the proof. ∎

###### Remark 5.

If r n > 1 r_{n}>1, then it follows from ( 10) that if σ 0 ​ d n ​ ( μ) > 0 \sigma_{0}d_{n}(\mu)>0 and d n − 1 ( 1) ​ ( μ) = 0 d_{n-1}^{(1)}(\mu)=0, then we have a heteroclinic (or homoclinic, if n = 2 n=2) connection from p 1 p_{1} to p n − 1 p_{n-1}, bypassing p n p_{n}. In particular, if there is μ 0 ∈ Λ \mu_{0}\in\Lambda such that σ 0 ​ d n ​ ( μ 0) > 0 \sigma_{0}d_{n}(\mu_{0})>0, then from the continuity of d n d_{n} we know that there is a neighborhood Λ 1 ⊂ Λ \Lambda_{1}\subset\Lambda of μ 0 \mu_{0} such that σ 0 ​ d n ​ ( μ) > 0 \sigma_{0}d_{n}(\mu)>0 for every μ ∈ Λ 1 \mu\in\Lambda_{1}. Hence, if μ ∈ Λ 1 \mu\in\Lambda_{1} is such that d n − 1 ( 1) ​ ( μ) = 0 d_{n-1}^{(1)}(\mu)=0, then there is a connection from p 1 p_{1} to p n − 1 p_{n-1}, bypassing p n p_{n}.

Suppose now that r n < 1 r_{n}<1. In this case, we define the displacement map d n − 1 ( 1): Λ → ℝ d_{n-1}^{(1)}\colon\Lambda\to\mathbb{R} by,

(19) |  | d n − 1 ( 1) ​ ( μ) = { b n u ​ ( μ) − b n s ​ ( μ), if ​ σ 0 ​ d n − 1 ​ ( μ) ⩾ 0, b n u ​ ( μ) − b n ( 1) ​ ( μ), if ​ σ 0 ​ d n − 1 ​ ( μ) < 0. d_{n-1}^{(1)}(\mu)=\left\{\begin{array}[]{ll}b_{n}^{u}(\mu)-b_{n}^{s}(\mu),&\text{if }\sigma_{0}d_{n-1}(\mu)\geqslant 0,\\ b_{n}^{u}(\mu)-b_{n}^{(1)}(\mu),&\text{if }\sigma_{0}d_{n-1}(\mu)<0.\end{array}\right. |  |

###### Proposition 4.

If r n < 1 r_{n}<1, then the displacement map ( 19) is a well defined function of class C 1 C^{1}.

###### Proof.

The proof follows similarly to the proof of Proposition 3. We only observe that in this case we have,

 | d n − 1 ( 1) ​ ( μ) = d n ​ ( μ) + R σ 0 ∗ ​ ( μ), d_{n-1}^{(1)}(\mu)=d_{n}(\mu)+R_{\sigma_{0}}^{*}(\mu), |  |

with,

 | R σ 0 ∗ ​ ( μ) = { 0, if ​ σ 0 ​ d n − 1 ​ ( μ) ⩾ 0, σ 0 ​ D n − 1 ​ ( σ 0 ​ d n − 1 ​ ( μ), μ), if ​ σ 0 ​ d n − 1 ​ ( μ) < 0, R_{\sigma_{0}}^{*}(\mu)=\left\{\begin{array}[]{ll}0,&\text{if }\sigma_{0}d_{n-1}(\mu)\geqslant 0,\\ \sigma_{0}D_{n}^{-1}(\sigma_{0}d_{n-1}(\mu),\mu),&\text{if }\sigma_{0}d_{n-1}(\mu)<0,\end{array}\right. |  |

where D n D_{n} is the displacement map associated to p n p_{n}. ∎

In case r n < 1 r_{n}<1 a remark similar to Remark 5 could be done.

###### Corollary 1.

If r n ≠ 1 r_{n}\neq 1, then

 | ∂ d n − 1 ( 1) ∂ μ j ​ ( 0) = { ∂ d n − 1 ∂ μ j ​ ( 0), if ​ r n > 1, ∂ d n ∂ μ j ​ ( 0), if ​ r n < 1, \frac{\partial d_{n-1}^{(1)}}{\partial\mu_{j}}(0)=\left\{\begin{array}[]{ll}\displaystyle\frac{\partial d_{n-1}}{\partial\mu_{j}}(0),&\text{if }r_{n}>1,\\ \displaystyle\frac{\partial d_{n}}{\partial\mu_{j}}(0),&\text{if }r_{n}<1,\end{array}\right. |  |

for every j ∈ { 1, …, N } j\in\{1,\dots,N\}.

###### Remark 6.

As a consequence of Propositions 3 and 4, for d n − 1 ( 1), d_{n-1}^{(1)}, defined as in ( 10) or ( 19), respectively, to be of class C 1 C^{1} it is sufficient to have r n ≠ 1 r_{n}\neq 1. If r n = 1 r_{n}=1, then it follows from [19] that we can write

 | D ⁡ ( s, μ) = Δ 00 ​ ( μ) ​ s r ⁡ ( μ) + ℛ ⁡ ( s, μ), D(s,\mu)=\Delta_{00}(\mu)s^{r(\mu)}+\mathscr{R}(s,\mu), |  |

with ℛ: [0, ε) × Λ → ℝ \mathscr{R}\colon[0,\varepsilon)\times\Lambda\to\mathbb{R} continuous, C 1 C^{1} in ( 0, ε) × Λ (0,\varepsilon)\times\Lambda and such that

 | ℛ ⁡ ( 0, μ) = 0, lim s → 0 + ∂ ℛ ∂ μ j ​ ( 0, μ) = 0, \mathscr{R}(0,\mu)=0,\quad\lim\limits_{s\to 0^{+}}\frac{\partial\mathscr{R}}{\partial\mu_{j}}(0,\mu)=0, |  |

for every μ ∈ Λ \mu\in\Lambda and j ∈ { 1, …, N } j\in\{1,\dots,N\}. In particular, D D can be continuously extended to s = 0 s=0 and, in relation to the parameter μ \mu, can also be C 1 C^{1} -extended. However, such C 1 C^{1} -extension does not necessarily hold in relation to s s and thus we cannot in general apply the limit in ( 18). Hence, if r n = 1 r_{n}=1, then ( 10) and ( 19) are both well defined continuous functions, but not necessarily of class C 1 C^{1}.

###### Remark 7.

Our construction of the map d n − 1 ( 1) d_{n-1}^{(1)} given in this section is inspired on the construction of the map d n − 1 ∗ d_{n-1}^{*} of [11, Lemma 2.2 2.2]. However, in the construction given there the authors do not give the proof that the Dulac map in relation to the perturbative parameter μ \mu is continuously differentiate. We prove this regularity by using the recent works [18, 19, 21] that give properties of the Dulac map not know at that time. Moreover, when defining d n − 1 ∗ d_{n-1}^{*} the authors in [11] seem not to be aware that the points x n − 1 ( 1) ​ ( μ) x_{n-1}^{(1)}(\mu) and x n ( 1) ​ ( μ) x_{n}^{(1)}(\mu) are not well defined for every μ ∈ Λ \mu\in\Lambda. Hence, in our proof we need to define d n − 1 ( 1) d_{n-1}^{(1)} in a multiple-folded way, depending on the sign of σ 0 \sigma_{0}, d n ​ ( μ) d_{n}(\mu) and d n − 1 ​ ( μ) d_{n-1}(\mu).

## 4. Some technical results

### 4.1. Polynomial approximation of a bump function

Let F: [0, 1] 2 → ℝ F\colon[0,1]^{2}\to\mathbb{R} be a map of class C r C^{r}, r ⩾ 0 r\geqslant 0. The *Bernstein polynomial*associated to F F is given by

 | B m, n F ​ ( x 1, x 2) = ∑ r = 0 m ∑ s = 0 n F ⁡ ( r m, s n) ​ ( m r) ​ ( n s) ​ x 1 r ​ x 2 s ​ ( 1 − x 1) m − r ​ ( 1 − x 2) n − s, B_{m,n}^{F}(x_{1},x_{2})=\sum_{r=0}^{m}\sum_{s=0}^{n}F\left(\frac{r}{m},\frac{s}{n}\right)\binom{m}{r}\binom{n}{s}x_{1}^{r}x_{2}^{s}(1-x_{1})^{m-r}(1-x_{2})^{n-s}, |  |

where ( n k) = n! k! ​ ( n − k)! \binom{n}{k}=\frac{n!}{k!(n-k)!}. An important property of the Bernstein polynomials is that B n, m ⇉ F B_{n,m}\rightrightarrows F uniformly in the C r C^{r} -topology. More precisely, we have the following theorem (see Kingsley [16]).

###### Proposition 5.

If F: [0, 1] 2 → ℝ F\colon[0,1]^{2}\to\mathbb{R} is of class C r C^{r}, r ⩾ 0 r\geqslant 0 finite, then

 | lim ( n, m) → ∞ ∂ | k | B m, n F ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x 1, x 2) = ∂ | k | F ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x 1, x 2), \lim\limits_{(n,m)\to\infty}\frac{\partial^{|k|}B_{m,n}^{F}}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x_{1},x_{2})=\frac{\partial^{|k|}F}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x_{1},x_{2}), |  |

uniformly in ( x 1, x 2) ∈ [0, 1] 2 (x_{1},x_{2})\in[0,1]^{2}, where k = ( k 1, k 2) ∈ ℤ ⩾ 0 2 k=(k_{1},k_{2})\in\mathbb{Z}_{\geqslant 0}^{2}, | k | = k 1 + k 2 |k|=k_{1}+k_{2} and | k | ⩽ r |k|\leqslant r.

In particular, we can use Proposition 5 to construct suitable polynomial approximations of a given bump function. More precisely, given δ 2 > δ 1 > 0 \delta_{2}>\delta_{1}>0 and c ∈ ℝ 2 c\in\mathbb{R}^{2}, we say that a C ∞ C^{\infty} -function φ: ℝ 2 → [0, 1] \varphi\colon\mathbb{R}^{2}\to[0,1] is a ( δ 1, δ 2, c) (\delta_{1},\delta_{2},c) -bump function if

 | φ ⁡ ( x) = { 1, if ​ ‖ x − c ‖ ⩽ δ 1, 0, if ​ ‖ x − c ‖ ⩾ δ 2. \varphi(x)=\left\{\begin{array}[]{ll}1,&\text{if }||x-c||\leqslant\delta_{1},\\ 0,&\text{if }||x-c||\geqslant\delta_{2}.\end{array}\right. |  |

###### Proposition 6.

Set r ⩾ 0 r\geqslant 0 finite and let φ: ℝ 2 → [0, 1] \varphi\colon\mathbb{R}^{2}\to[0,1] be a ( δ 1, δ 2, c) (\delta_{1},\delta_{2},c) -bump function. Then for every compact B ⊂ ℝ 2 B\subset\mathbb{R}^{2} and ε > 0 \varepsilon>0, there is a polynomial q: ℝ 2 → ℝ q\colon\mathbb{R}^{2}\to\mathbb{R} such that

(20) |  | max x ∈ B | k | ⩽ r ⁡ | ∂ | k | φ ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) − ∂ | k | q ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) | < ε, \max_{\begin{subarray}{c}x\in B\\ |k|\leqslant r\end{subarray}}\left|\frac{\partial^{|k|}\varphi}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)-\frac{\partial^{|k|}q}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)\right|<\varepsilon, |  |

where k = ( k 1, k 2) ∈ ℤ ⩾ 0 2 k=(k_{1},k_{2})\in\mathbb{Z}^{2}_{\geqslant 0} and | k | = k 1 + k 2 |k|=k_{1}+k_{2}. Moreover, q q can be chosen such that

(21) |  | φ ⁡ ( x) + 1 4 ​ ε < q ⁡ ( x) < φ ⁡ ( x) + 3 4 ​ ε, \varphi(x)+\frac{1}{4}\varepsilon<q(x)<\varphi(x)+\frac{3}{4}\varepsilon, |  |

for every x ∈ B x\in B. In particular, q ⁡ ( x) > 0 q(x)>0 for every x ∈ B x\in B.

###### Proof.

Except by a translation and a linear change of coordinates, we can suppose B ⊂ [0, 1] 2 B\subset[0,1]^{2}. It follows from Proposition 5 that there is a polynomial q ¯: ℝ 2 → ℝ \overline{q}\colon\mathbb{R}^{2}\to\mathbb{R} such that,

(22) |  | max x ∈ [0, 1] 2 | k | ⩽ r ⁡ | ∂ | k | φ ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) − ∂ | k | q ¯ ∂ x 1 k 1 ​ ∂ x 2 k 2 ​ ( x) | < 1 4 ​ ε. \max_{\begin{subarray}{c}x\in[0,1]^{2}\\ |k|\leqslant r\end{subarray}}\left|\frac{\partial^{|k|}\varphi}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)-\frac{\partial^{|k|}\overline{q}}{\partial x_{1}^{k_{1}}\partial x_{2}^{k_{2}}}(x)\right|<\frac{1}{4}\varepsilon. |  |

Consider now the polynomial q: ℝ 2 → ℝ q\colon\mathbb{R}^{2}\to\mathbb{R} given by q ​ ( x) = q ¯ ​ ( x) + 1 2 ​ ε q(x)=\overline{q}(x)+\frac{1}{2}\varepsilon. We claim that it satisfies ( 20) and ( 21). Indeed, since q q is a translation of q ¯ \overline{q} it follows that its partial derivatives of order | k | |k|, | k | ⩾ 1 |k|\geqslant 1, are equal. Therefore ( 20) follows directly from ( 22), when | k | ⩾ 1 |k|\geqslant 1. We now look the case | k | = 0 |k|=0, i.e. the function q q itself. It follows from ( 22), with | k | = 0 |k|=0, that

(23) |  | φ ⁡ ( x) − 1 4 ​ ε < q ¯ ​ ( x) < φ ⁡ ( x) + 1 4 ​ ε. \varphi(x)-\frac{1}{4}\varepsilon<\overline{q}(x)<\varphi(x)+\frac{1}{4}\varepsilon. |  |

Adding 1 2 ​ ε \frac{1}{2}\varepsilon on all sides of ( 23) we obtain

(24) |  | φ ⁡ ( x) + 1 4 ​ ε < q ⁡ ( x) < φ ⁡ ( x) + 3 4 ​ ε. \varphi(x)+\frac{1}{4}\varepsilon<q(x)<\varphi(x)+\frac{3}{4}\varepsilon. |  |

which is precisely ( 21). Moreover, it also follows from ( 24) that

 | φ ⁡ ( x) − ε < q ⁡ ( x) < φ ⁡ ( x) + ε, \varphi(x)-\varepsilon<q(x)<\varphi(x)+\varepsilon, |  |

and thus we have ( 20) with | k | = 0 |k|=0, completing the proof. ∎

###### Remark 8.

Let φ: ℝ 2 → [0, 1] \varphi\colon\mathbb{R}^{2}\to[0,1] be a ( δ 1, δ 2, c) (\delta_{1},\delta_{2},c) -bump, function and set ε ¯ > 0 \overline{\varepsilon}>0 and ε > 0 \varepsilon>0 such that ε ⩽ 1 3 ​ ε ¯ \varepsilon\leqslant\frac{1}{3}\overline{\varepsilon}. Let q ε ¯ q_{\overline{\varepsilon}} and q ε q_{\varepsilon} be the respective polynomials given by Proposition 6. It follows from ( 24) that

 | φ ⁡ ( x) < q ε ​ ( x) < φ ⁡ ( x) + 3 4 ​ ε ⩽ φ ⁡ ( x) + 1 4 ​ ε ¯ < q ε ¯ ​ ( x). \varphi(x)<q_{\varepsilon}(x)<\varphi(x)+\frac{3}{4}\varepsilon\leqslant\varphi(x)+\frac{1}{4}\overline{\varepsilon}<q_{\overline{\varepsilon}}(x). |  |

In particular, φ ​ ( x) < q ε ¯ ​ ( x) \varphi(x)<q_{\overline{\varepsilon}}(x) and q ε ​ ( x) < q ε ¯ ​ ( x) q_{\varepsilon}(x)<q_{\overline{\varepsilon}}(x) for all x ∈ B x\in B.

### 4.2. Positive or negative invariant regions associated to a simple polycycle

Let X X be a planar smooth vector field and Ω ⊂ ℝ 2 \Omega\subset\mathbb{R}^{2} an open set. We say that Ω \Omega is *positive-invariant*(resp. *negative-invariant*) by X X if for every x ∈ Ω x\in\Omega we have γ ⁡ ( t) ∈ Ω \gamma(t)\in\Omega for all t ⩾ 0 t\geqslant 0 (resp. t ⩽ 0 t\leqslant 0), where γ ⁡ ( t) \gamma(t) is the orbit of X X with initial condition γ ⁡ ( 0) = x \gamma(0)=x.

Let S ⊂ ℝ 2 S\subset\mathbb{R}^{2} be a continuous simple closed curve. We say that S S is *piecewise smooth*if it is of class C ∞ C^{\infty} except, perhaps, in at most a finite number of points. We will say that a piecewise smooth closed curve is without contact with a smooth vector field if on each of the closed C ∞ C^{\infty} sides of S, S, the scalar product ⟨ X, ∇ S ⟩ \left<X,\nabla S\right> keeps sign on all the regular points of S, S, and on S S either X X points always towards the interior of the region delimited by S S or X X points always towards the exterior of this region.

The proof of next result follows mutatis mutandis the proof of a similar result, but with an isolated limit cycle instead of a polycycle, see [31, Proposition 1 1]. We omit the details. For an illustration of the situation see Figure 8. As usual, given a compact set B ⊂ ℝ 2 B\subset\mathbb{R}^{2}, let Int ​ ( B) \textnormal{Int}(B) be its topological interior.

###### Proposition 7.

Let 𝒳 \mathcal{X} be one of the topological spaces 𝔛 ∞ \mathfrak{X}^{\infty} or 𝒫 r \mathcal{P}^{r}, for some r ⩾ 1 r\geqslant 1. Let X ∈ 𝒳 X\in\mathcal{X} having a simple polycycle Γ n \Gamma^{n} composed by n ⩾ 1 n\geqslant 1 hyperbolic saddles and let B ⊂ ℝ 2 B\subset\mathbb{R}^{2} be a compact set such that Γ n ⊂ Int ⁡ ( B). \Gamma^{n}\subset\operatorname{Int}(B). Then there is a continuous and piecewise smooth simple closed curve S ⊂ Int ⁡ ( B) S\subset\operatorname{Int}(B), on the same connected component of B \ Γ n B\backslash\Gamma^{n} as the first-return map of Γ n \Gamma^{n}, such that if Ω ⊂ Int ⁡ ( B) \Omega\subset\operatorname{Int}(B) is the open region bounded by S S and Γ n \Gamma^{n}, then following statements hold.

1. (a)

There is no singularity of X X in Ω \Omega.

2. (b)

There is no periodic orbit of X X in Ω \Omega.

3. (c)

X X is without contact with S S.

4. (d)

If r ⁡ ( Γ n) > 1 r(\Gamma^{n})>1, then Ω \Omega is positive invariant by X X.

5. (e)

If r ⁡ ( Γ n) < 1 r(\Gamma^{n})<1, then Ω \Omega is negative invariant by X X.

###### Remark 9.

Under the statement of Proposition 7, it follows from the compactness of S S and the continuity of the inner product ⟨ ⋅, ⋅ ⟩ \left<\cdot,\cdot\right> that there is a neighborhood N ⊂ 𝒳 N\subset\mathcal{X} of X X such that ⟨ X ⁡ ( s), Y ⁡ ( s) ⟩ > 0 \left<X(s),Y(s)\right>>0 for every Y ∈ N Y\in N and s ∈ S s\in S. In particular, Y Y is also without contact with S S and points in the same direction as X X.

\begin{overpic}[Fig31x.eps] \put(22.0,30.0){$S$} \put(85.0,75.0){$\Gamma^{n}$} \end{overpic}

S S in the bounded region of Γ n \Gamma^{n}.

\begin{overpic}[Fig33x.eps] \put(59.0,90.0){$S$} \put(20.0,25.0){$\Gamma^{n}$} \end{overpic}

S S in the unbounded region of Γ n \Gamma^{n}.

Figure 8. Illustration of of the curve S S and the flow of X X on it, for the case r ⁡ ( Γ n) > 1 r(\Gamma^{n})>1.

### 4.3. Periodic orbits of smooth vector fields

Let X X be a planar smooth vector field with a periodic orbit γ ⁡ ( t) \gamma(t) (not necessarily isolated), with period T > 0 T>0. It follows from Andronov et al [2, Lemma 1 1, p. 124 124] that there is a neighborhood A ⊂ ℝ 2 A\subset\mathbb{R}^{2} of γ \gamma and a smooth function Φ: A → ℝ \Phi\colon A\to\mathbb{R} such that

(25) |  | Φ ⁡ ( γ ⁡ ( t)) = 0, ( ∂ Φ ∂ x ​ ( γ ⁡ ( t))) 2 + ( ∂ Φ ∂ y ​ ( γ ⁡ ( t))) 2 > 0, \Phi(\gamma(t))=0,\quad\left(\frac{\partial\Phi}{\partial x}(\gamma(t))\right)^{2}+\left(\frac{\partial\Phi}{\partial y}(\gamma(t))\right)^{2}>0, |  |

for every t ∈ [0, T] t\in[0,T]. In particular, by means of *bump-functions*we can suppose that Φ \Phi is defined on the entire plane and has compact support. The authors in [2, Theorem 19 19] use Φ \Phi to perturb the stability of non-hyperbolic limit cycles, bifurcating new ones in the process. In the next result we enunciate and proof a simple version of their results, sufficient for our objectives in this paper.

###### Proposition 8.

Let X = ( P, Q) X=(P,Q), γ \gamma and Φ \Phi be as above and consider the one-parameter family of planar smooth vector fields X λ = ( P λ, Q λ) X_{\lambda}=(P_{\lambda},Q_{\lambda}) given by,

(26) |  | P λ ​ ( x, y) = P ⁡ ( x, y) + λ ​ Φ ​ ( x, y) ​ ∂ Φ ∂ x ​ ( x, y), Q λ ​ ( x, y) = Q ⁡ ( x, y) + λ ​ Φ ​ ( x, y) ​ ∂ Φ ∂ y ​ ( x, y), P_{\lambda}(x,y)=P(x,y)+\lambda\Phi(x,y)\frac{\partial\Phi}{\partial x}(x,y),\quad Q_{\lambda}(x,y)=Q(x,y)+\lambda\Phi(x,y)\frac{\partial\Phi}{\partial y}(x,y), |  |

with λ ∈ ℝ \lambda\in\mathbb{R}. Then if γ \gamma is not a hyperbolic limit cycle for X X then it is a hyperbolic limit cycle for every λ ≠ 0 \lambda\neq 0 and its stability depends on the sign of λ \lambda. Otherwise, it is hyperbolic for | λ | |\lambda| small enough.

###### Proof.

It follows from ( 25) that X λ ​ ( γ ⁡ ( t)) = X ⁡ ( γ ⁡ ( t)) X_{\lambda}(\gamma(t))=X(\gamma(t)) for every t ∈ [0, T] t\in[0,T] and λ ∈ ℝ \lambda\in\mathbb{R}. Hence, γ ⁡ ( t) \gamma(t) is also a periodic orbit of X λ X_{\lambda}. The first derivative of the Poincaré first return map of X λ X_{\lambda} at γ \gamma is given by

 | r ⁡ ( λ):= ∫ 0 T ( ∂ P λ ∂ x + ∂ Q λ ∂ y) ​ ( γ ⁡ ( t)) ​ 𝑑 t, r(\lambda):=\int_{0}^{T}\left(\frac{\partial P_{\lambda}}{\partial x}+\frac{\partial Q_{\lambda}}{\partial y}\right)(\gamma(t))\;dt, |  |

see for example [6, Theorem 1.23 1.23]. It follows from the expression ( 26) of X λ X_{\lambda} that

 | r ⁡ ( λ) = ∫ 0 T ∂ P ∂ x + ∂ Q ∂ y ​ 𝑑 t + λ ​ ∫ 0 T Φ ​ ∂ 2 Φ ∂ x 2 + Φ ​ ∂ 2 Φ ∂ y 2 ​ 𝑑 t + λ ​ ∫ 0 T ( ∂ Φ ∂ x) 2 + ( ∂ Φ ∂ y) 2 ​ 𝑑 t, r(\lambda)=\int_{0}^{T}\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\;dt+\lambda\int_{0}^{T}\Phi\frac{\partial^{2}\Phi}{\partial x^{2}}+\Phi\frac{\partial^{2}\Phi}{\partial y^{2}}\;dt+\lambda\int_{0}^{T}\left(\frac{\partial\Phi}{\partial x}\right)^{2}+\left(\frac{\partial\Phi}{\partial y}\right)^{2}\;dt, |  |

where term γ ⁡ ( t) \gamma(t) was omitted by simplicity. Observe that the middle integral of the right-hand side is equal to zero because Φ ⁡ ( γ) ≡ 0. \Phi(\gamma)\equiv 0. Thus

 | r ⁡ ( λ) = r ⁡ ( 0) + λ ​ ∫ 0 T ( ∂ Φ ∂ x ​ ( γ ⁡ ( t))) 2 + ( ∂ Φ ∂ y ​ ( γ ⁡ ( t))) 2 ​ 𝑑 t. r(\lambda)=r(0)+\lambda\int_{0}^{T}\left(\frac{\partial\Phi}{\partial x}(\gamma(t))\right)^{2}+\left(\frac{\partial\Phi}{\partial y}(\gamma(t))\right)^{2}\;dt. |  |

From ( 25) we have that the above integral is positive and thus if r ⁡ ( 0) = 0 r(0)=0 (i.e. γ \gamma is not hyperbolic for X X) then r ⁡ ( λ) ≠ 0 r(\lambda)\neq 0 for every λ ≠ 0 \lambda\neq 0. In particular, sign ​ ( r ​ ( λ)) = sign ​ ( λ) \text{sign}(r(\lambda))=\text{sign}(\lambda) and thus we can choose the stability of γ \gamma. If γ \gamma is a hyperbolic limit cycle for X X then r ⁡ ( 0) ≠ 0 r(0)\neq 0 and thus γ \gamma remains a hyperbolic limit cycle of same stability for | λ | |\lambda| small enough. ∎

## 5. Proof of Theorem 1

For simplicity, we assume for now that Γ n \Gamma^{n} is endowed with the trivial permutation τ \tau. We recall that R i = ∏ j = 1 i r j R_{i}=\prod_{j=1}^{i}r_{j}, where r i r_{i} are the hyperbolicity ratios ( 1) of the hyperbolic saddles of the polycycle Γ n \Gamma^{n}. Let L i L_{i} and x i x_{i} be as in Section 2.2. For each i ∈ { 1, …, n } i\in\{1,\dots,n\}, let γ i ​ ( t) \gamma_{i}(t) be the parametrization of L i L_{i} given by the solution of X X and with the initial condition γ i ​ ( 0) = x i \gamma_{i}(0)=x_{i}. Let also L i + = { γ i ​ ( t): t > 0 } L_{i}^{+}=\{\gamma_{i}(t)\colon t>0\}. Let B ⊂ ℝ 2 B\subset\mathbb{R}^{2} be a closed ball such that Γ n ⊂ Int ⁡ ( B) \Gamma^{n}\subset\operatorname{Int}(B). For each i ∈ { 1, …, n } i\in\{1,\dots,n\}, let c i ∈ L i + c_{i}\in L_{i}^{+} and let δ i, 2 > δ i, 1 > 0 \delta_{i,2}>\delta_{i,1}>0 be small enough such that the compact sets

 | G i, j = { ( x 1, x 2) ∈ ℝ 2: ‖ x − c i ‖ ⩽ δ i, j }, G_{i,j}=\{(x_{1},x_{2})\in\mathbb{R}^{2}\colon||x-c_{i}||\leqslant\delta_{i,j}\}, |  |

satisfies the following statements.

1. (a)

Γ n ∩ G i, j = L i + ∩ G i, j ≠ ∅ \Gamma^{n}\cap G_{i,j}=L_{i}^{+}\cap G_{i,j}\neq\emptyset, j ∈ { 1, 2 } j\in\{1,2\};

2. (b)

If i ≠ k i\neq k, then G i, 2 ∩ G k, 2 = ∅ G_{i,2}\cap G_{k,2}=\emptyset;

3. (c)

G i, j ⊂ Int ⁡ ( B) G_{i,j}\subset\operatorname{Int}(B).

See Figure 9.

\begin{overpic}[Fig5.eps] \put(79.0,57.0){$p_{1}$} \put(12.0,55.0){$p_{2}$} \put(62.0,13.0){$p_{3}$} \put(95.0,72.0){$B$} \put(60.0,48.0){$G_{1,j}$} \put(28.0,45.0){$G_{2,j}$} \put(72.0,22.0){$G_{3,j}$} \put(38.0,57.0){$L_{1}$} \put(38.0,20.0){$L_{2}$} \put(74.0,35.0){$L_{3}$} \end{overpic}

\begin{overpic}[Fig27.eps] \put(54.0,45.0){$p_{1}=p_{2}$} \put(26.0,80.0){$L_{1}$} \put(49.0,18.0){$L_{2}$} \put(72.0,95.0){$B$} \put(59.0,56.0){$G_{1,j}$} \put(13.0,40.0){$G_{2,j}$} \end{overpic}

Figure 9. An illustration of the sets G i, j G_{i,j}.

Let φ i: ℝ 2 → ℝ \varphi_{i}\colon\mathbb{R}^{2}\to\mathbb{R} be a ( δ i, 1, δ i, 2, c i) (\delta_{i,1},\delta_{i,2},c_{i}) -bump function. Given ε > 0 \varepsilon>0, let q i, ε: ℝ 2 → ℝ q_{i,\varepsilon}\colon\mathbb{R}^{2}\to\mathbb{R} be the polynomial approximation of φ i \varphi_{i}, on B B, given by Proposition 6. Write X = ( P, Q) X=(P,Q) and let X ⟂ = ( − Q, P) X^{\perp}=(-Q,P). Let K: ℝ 2 × ℝ n × ( 0, + ∞) → ℝ 2 K\colon\mathbb{R}^{2}\times\mathbb{R}^{n}\times(0,+\infty)\to\mathbb{R}^{2} be given by

(27) |  | K ⁡ ( x, μ, ε) = ( ∑ i = 1 n μ i ​ q i, ε ​ ( x)) ​ X ⟂ ​ ( x), K(x,\mu,\varepsilon)=\left(\sum_{i=1}^{n}\mu_{i}q_{i,\varepsilon}(x)\right)X^{\perp}(x), |  |

and denote

(28) |  | X μ, ε ​ ( x) = X ⁡ ( x) + K ⁡ ( x, μ, ε). X_{\mu,\varepsilon}(x)=X(x)+K(x,\mu,\varepsilon). |  |

It follows from Proposition 6 that q i, ε → φ i q_{i,\varepsilon}\to\varphi_{i} in the C r C^{r} -topology (restricted to B B) as ε → 0 \varepsilon\to 0. Hence we also let K: ℝ 2 × ℝ n × { 0 } → ℝ 2 K\colon\mathbb{R}^{2}\times\mathbb{R}^{n}\times\{0\}\to\mathbb{R}^{2} be given by

(29) |  | K ⁡ ( x, μ, 0) = ( ∑ i = 1 n μ i ​ φ i ​ ( x)) ​ X ⟂ ​ ( x), K(x,\mu,0)=\left(\sum_{i=1}^{n}\mu_{i}\varphi_{i}(x)\right)X^{\perp}(x), |  |

and denote

(30) |  | X μ, 0 ​ ( x) = X ⁡ ( x) + K ⁡ ( x, μ, 0). X_{\mu,0}(x)=X(x)+K(x,\mu,0). |  |

Observe X 0, ε = X X_{0,\varepsilon}=X for every ε ⩾ 0 \varepsilon\geqslant 0 and that *for each fixed*ε ⩾ 0 \varepsilon\geqslant 0 the family X μ, ε X_{\mu,\varepsilon} is a well defined family of C ∞ C^{\infty} -vector fields containing X X, relative to the parameter μ ∈ Λ \mu\in\Lambda. Moreover it is also polynomial if X X is polynomial and ε > 0 \varepsilon>0. In other words, X μ, ε X_{\mu,\varepsilon} is rather a one-parameter family of one-parameter families of vector fields ( X μ) ε (X_{\mu})_{\varepsilon}, than a two-parameter family. However for simplicity we write X μ, ε X_{\mu,\varepsilon}.

Observe that X μ, 0 → X X_{\mu,0}\to X in 𝔛 ∞ \mathfrak{X}^{\infty} as μ → 0 \mu\to 0 and that if X X is polynomial, then given any neighborhood N ⊂ 𝒫 r N\subset\mathcal{P}^{r} of X X we can extend the compact B ⊂ ℝ 2 B\subset\mathbb{R}^{2} if necessary such that X μ, ε ∈ N X_{\mu,\varepsilon}\in N for every ( μ, ε) ≈ ( 0, 0) (\mu,\varepsilon)\approx(0,0), ε > 0 \varepsilon>0. Let Λ ⊂ ℝ n \Lambda\subset\mathbb{R}^{n} be a small enough neighborhood of the origin and let ε ¯ > 0 \overline{\varepsilon}>0 be small enough. Observe that for each ε ∈ ( 0, ε ¯] \varepsilon\in(0,\overline{\varepsilon}] we have X μ, ε → X 0, ε = X X_{\mu,\varepsilon}\to X_{0,\varepsilon}=X in 𝔛 ∞ \mathfrak{X}^{\infty} restricted to B B (and in particular in a neighborhood of Γ n \Gamma^{n}), as μ → 0 \mu\to 0. Hence it follows that for each ε ∈ ( 0, ε ¯] \varepsilon\in(0,\overline{\varepsilon}] the displacement maps d i, ε: Λ → ℝ d_{i,\varepsilon}\colon\Lambda\to\mathbb{R}, i ∈ { 1, …, n } i\in\{1,\dots,n\}, are well defined and of class C ∞ C^{\infty}. Moreover from ( 8) we get that,

(31) |  | ∂ d i, ε ∂ μ j ( 0) = 1 ‖ X ⁡ ( x i) ‖ ∫ − ∞ + ∞ e − ∫ 0 t div X ( γ i ( s)) d s X ( γ i ( t)) ∧ ∂ K ∂ μ j ( γ i ( t), 0, ε) d t. \frac{\partial d_{i,\varepsilon}}{\partial\mu_{j}}(0)=\frac{1}{||X(x_{i})||}\int_{-\infty}^{+\infty}e^{-\int_{0}^{t}\operatorname{div}X(\gamma_{i}(s))\;ds}X(\gamma_{i}(t))\land\frac{\partial K}{\partial\mu_{j}}(\gamma_{i}(t),0,\varepsilon)\;dt. |  |

In particular, the improper integrals in the right hand-side of ( 31) are convergent. Similarly, it follows that for ε = 0 \varepsilon=0 the displacement maps d i, 0: Λ → ℝ d_{i,0}\colon\Lambda\to\mathbb{R}, i ∈ { 1, …, n } i\in\{1,\dots,n\}, are also well defined C ∞ C^{\infty} -maps and their partial derivatives are given by,

(32) |  | ∂ d i, 0 ∂ μ j ( 0) = 1 ‖ X ⁡ ( x i) ‖ ∫ − ∞ + ∞ e − ∫ 0 t div X ( γ i ( s)) d s X ( γ i ( t)) ∧ ∂ K ∂ μ j ( γ i ( t), 0, 0) d t. \frac{\partial d_{i,0}}{\partial\mu_{j}}(0)=\frac{1}{||X(x_{i})||}\int_{-\infty}^{+\infty}e^{-\int_{0}^{t}\operatorname{div}X(\gamma_{i}(s))\;ds}X(\gamma_{i}(t))\land\frac{\partial K}{\partial\mu_{j}}(\gamma_{i}(t),0,0)\;dt. |  |

We claim that

(33) |  | lim ε → 0 ∂ d i, ε ∂ μ j ​ ( 0) = ∂ d i, 0 ∂ μ j ​ ( 0), \lim\limits_{\varepsilon\to 0}\frac{\partial d_{i,\varepsilon}}{\partial\mu_{j}}(0)=\frac{\partial d_{i,0}}{\partial\mu_{j}}(0), |  |

for every i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}. Indeed, observe that if ε > 0 \varepsilon>0, then it follows from ( 27) and ( 28) that,

(34) |  | X ⁡ ( x) ∧ ∂ K ∂ μ j ​ ( x, 0, ε) = ( P, Q) ∧ ( − q j, ε ​ Q, q j, ε ​ P) = q j, ε ​ ( P 2 + Q 2). X(x)\land\frac{\partial K}{\partial\mu_{j}}(x,0,\varepsilon)=(P,Q)\land(-q_{j,\varepsilon}Q,q_{j,\varepsilon}P)=q_{j,\varepsilon}(P^{2}+Q^{2}). |  |

Similarly, observe that if ε = 0 \varepsilon=0, then it follows from ( 29) and ( 30) that,

(35) |  | X ⁡ ( x) ∧ ∂ K ∂ μ j ​ ( x, 0, 0) = φ j ​ ( P 2 + Q 2). X(x)\land\frac{\partial K}{\partial\mu_{j}}(x,0,0)=\varphi_{j}(P^{2}+Q^{2}). |  |

For each ε ∈ [0, ε ¯] \varepsilon\in[0,\overline{\varepsilon}] and i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}, let

 | Φ ε i, j ( t) = e − ∫ 0 t div X ( γ i ( s)) d s X ( γ i ( t)) ∧ ∂ K ∂ μ j ( γ i ( t), 0, ε) \Phi^{i,j}_{\varepsilon}(t)=e^{-\int_{0}^{t}\operatorname{div}X(\gamma_{i}(s))\;ds}X(\gamma_{i}(t))\land\frac{\partial K}{\partial\mu_{j}}(\gamma_{i}(t),0,\varepsilon) |  |

be the integrand of the right-hand side of ( 31) and ( 32). From Proposition 6 we know that q j, ε > φ j ⩾ 0 q_{j,\varepsilon}>\varphi_{j}\geqslant 0 and thus from ( 34) and ( 35) we have that Φ ε i, j ​ ( t) ⩾ 0 \Phi^{i,j}_{\varepsilon}(t)\geqslant 0 for each t ∈ ℝ t\in\mathbb{R}, ε ∈ [0, ε ¯] \varepsilon\in[0,\overline{\varepsilon}] and i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}.

From Remark 8 we have that Φ ε i, j \Phi^{i,j}_{\varepsilon}, with ε ∈ [0, 1 3 ​ ε ¯] \varepsilon\in[0,\frac{1}{3}\overline{\varepsilon}], is dominated by Φ ε ¯ i, j \Phi^{i,j}_{\overline{\varepsilon}} (i.e | Φ ε i, j ​ ( t) | ⩽ Φ ε ¯ i, j ​ ( t) |\Phi^{i,j}_{\varepsilon}(t)|\leqslant\Phi^{i,j}_{\overline{\varepsilon}}(t), for each t ∈ ℝ t\in\mathbb{R}). Moreover since ( 31) is well defined for ε = ε ¯ \varepsilon=\overline{\varepsilon}, it follows that

 | ∫ − ∞ + ∞ Φ ε ¯ i, j ​ ( t) ​ 𝑑 t < ∞, \int_{-\infty}^{+\infty}\Phi^{i,j}_{\overline{\varepsilon}}(t)\;dt<\infty, |  |

for i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}, with the convergence absolute because Φ ε ¯ i, j ​ ( t) ⩾ 0 \Phi^{i,j}_{\overline{\varepsilon}}(t)\geqslant 0. Hence it follows from the *Weierstrass M-test for uniform convergence of an integral*(see [37, p. 417 417, Proposition 2 2]) that for each i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}, the ε \varepsilon -family of improper integrals

 | ∫ − ∞ + ∞ Φ ε i, j ​ ( t) ​ 𝑑 t < ∞, \int_{-\infty}^{+\infty}\Phi^{i,j}_{\varepsilon}(t)\;dt<\infty, |  |

converges absolutely for each ε ∈ [0, 1 3 ​ ε ¯] \varepsilon\in[0,\frac{1}{3}\overline{\varepsilon}] and uniformly in [0, 1 3 ​ ε ¯] [0,\frac{1}{3}\overline{\varepsilon}].

Moreover from Proposition 6 and Remark 8 we have that for each closed bounded interval [a, b] ⊂ ℝ [a,b]\subset\mathbb{R} it holds

 | lim ε → 0 Φ ε i, j ​ ( t) = Φ 0 i, j ​ ( t), \lim\limits_{\varepsilon\to 0}\Phi^{i,j}_{\varepsilon}(t)=\Phi^{i,j}_{0}(t), |  |

*uniformly*in t ∈ [a, b] t\in[a,b] and ε ∈ [0, 1 3 ​ ε ¯] \varepsilon\in[0,\frac{1}{3}\overline{\varepsilon}], respectively. Thus it follows from [37, p. 420 420, Proposition 4 4] that

 | lim ε → 0 ∫ − ∞ + ∞ Φ ε i, j ​ ( t) ​ 𝑑 t = ∫ − ∞ + ∞ Φ 0 i, j ​ ( t) ​ 𝑑 t, \lim\limits_{\varepsilon\to 0}\int_{-\infty}^{+\infty}\Phi^{i,j}_{\varepsilon}(t)\;dt=\int_{-\infty}^{+\infty}\Phi^{i,j}_{0}(t)\;dt, |  |

for every i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}. Therefore ( 33) holds and the claim is proved.

From definition of the bump-functions φ j \varphi_{j} we know that if i ≠ j i\neq j, then φ j ​ ( γ i ​ ( t)) ≡ 0 \varphi_{j}(\gamma_{i}(t))\equiv 0. Hence, from ( 31) and ( 35) we obtain that

(36) |  | ∂ d i, 0 ∂ μ j ​ ( 0) = 0, \frac{\partial d_{i,0}}{\partial\mu_{j}}(0)=0, |  |

for every i i, j ∈ { 1, …, n } j\in\{1,\dots,n\}, with i ≠ j i\neq j. Similarly, if i = j i=j, then it follows from ( 35) that

(37) |  | ∂ d i, 0 ∂ μ i ​ ( 0) > 0, \frac{\partial d_{i,0}}{\partial\mu_{i}}(0)>0, |  |

for every i ∈ { 1, …, n } i\in\{1,\dots,n\}.

We now deal with the bifurcation of the limit cycles. The proof will be by induction on n n. First, observe that if n = 1, n=1, μ = μ 1 \mu=\mu_{1} and Δ ⁡ ( Γ 1, τ) = 1 \Delta(\Gamma^{1},\tau)=1 (i.e. if R 1 = r 1 ≠ 1 R_{1}=r_{1}\neq 1), then by using for instance Andronov et al [2, § ​ 29 \mathsection 29] we get that X μ, ε X_{\mu,\varepsilon} has a limit cycle near Γ 1 \Gamma^{1} if, and only if, ( r 1 − 1) ​ μ ≲ 0 (r_{1}-1)\mu\lesssim 0. Therefore, from now on assume n ⩾ 2 n\geqslant 2. Let μ = ( μ 1, …, μ n) \mu=(\mu_{1},\dots,\mu_{n}) and suppose that the theorem holds for n − 1 n-1. Assume for now that Δ ⁡ ( Γ n, τ) = n \Delta(\Gamma^{n},\tau)=n. That is, assume that ( R i − 1) ​ ( R i − 1 − 1) < 0 (R_{i}-1)(R_{i-1}-1)<0 for every i ∈ { 2, …, n } i\in\{2,\dots,n\} and that R 1 ≠ 1 R_{1}\neq 1. For definiteness, assume also that R n > 1 R_{n}>1 and R n − 1 < 1 R_{n-1}<1. In special, observe that r n > 1 r_{n}>1. Since R n > 1 R_{n}>1, from Cherkas [4] we know that Γ n \Gamma^{n} is stable. Moreover, for each ε ∈ [0, ε ¯] \varepsilon\in[0,\overline{\varepsilon}], it follows from Proposition 3 and Corollary 1 that d n − 1, ε ( 1): Λ → ℝ d_{n-1,\varepsilon}^{(1)}\colon\Lambda\to\mathbb{R} is a well defined function of class C 1 C^{1} such that,

(38) |  | ∂ d n − 1, ε ( 1) ∂ μ j ​ ( 0) = ∂ d n − 1, ε ∂ μ j ​ ( 0), \frac{\partial d_{n-1,\varepsilon}^{(1)}}{\partial\mu_{j}}(0)=\frac{\partial d_{n-1,\varepsilon}}{\partial\mu_{j}}(0), |  |

for every j ∈ { 1, …, n } j\in\{1,\dots,n\}. For each ε ∈ [0, ε ¯] \varepsilon\in[0,\overline{\varepsilon}], let F ε: Λ → ℝ n − 1 F_{\varepsilon}\colon\Lambda\to\mathbb{R}^{n-1} be given by

 | F ε ​ ( μ) = ( d 1, ε ​ ( μ), …, d n − 2, ε ​ ( μ), d n − 1, ε ( 1) ​ ( μ)), F_{\varepsilon}(\mu)=\left(d_{1,\varepsilon}(\mu),\dots,d_{n-2,\varepsilon}(\mu),d_{n-1,\varepsilon}^{(1)}(\mu)\right), |  |

and consider its ( n − 1) × n (n-1)\times n Jacobian matrix at μ = 0 \mu=0,

 | D ​ F ε ​ ( 0) = ( ∂ d 1, ε ∂ μ 1 ​ ( 0) ∂ d 1, ε ∂ μ 2 ​ ( 0) … ∂ d 1, ε ∂ μ n − 1 ​ ( 0) ∂ d 1, ε ∂ μ n ​ ( 0) ∂ d 2, ε ∂ μ 1 ​ ( 0) ∂ d 2, ε ∂ μ 2 ​ ( 0) … ∂ d 2, ε ∂ μ n − 1 ​ ( 0) ∂ d 2, ε ∂ μ n ​ ( 0) ⋮ ⋮ ⋱ ⋮ ⋮ ∂ d n − 1, ε ( 1) ∂ μ 1 ​ ( 0) ∂ d n − 1, ε ( 1) ∂ μ 2 ​ ( 0) … ∂ d n − 1, ε ( 1) ∂ μ n − 1 ​ ( 0) ∂ d n − 1, ε ( 1) ∂ μ n ​ ( 0)). DF_{\varepsilon}(0)=\left(\begin{array}[]{ccccc}\displaystyle\frac{\partial d_{1,\varepsilon}}{\partial\mu_{1}}(0)&\displaystyle\frac{\partial d_{1,\varepsilon}}{\partial\mu_{2}}(0)&\dots&\displaystyle\frac{\partial d_{1,\varepsilon}}{\partial\mu_{n-1}}(0)&\displaystyle\frac{\partial d_{1,\varepsilon}}{\partial\mu_{n}}(0)\\ \displaystyle\frac{\partial d_{2,\varepsilon}}{\partial\mu_{1}}(0)&\displaystyle\frac{\partial d_{2,\varepsilon}}{\partial\mu_{2}}(0)&\dots&\displaystyle\frac{\partial d_{2,\varepsilon}}{\partial\mu_{n-1}}(0)&\displaystyle\frac{\partial d_{2,\varepsilon}}{\partial\mu_{n}}(0)\\ \vdots&\vdots&\ddots&\vdots&\vdots\\ \displaystyle\frac{\partial d_{n-1,\varepsilon}^{(1)}}{\partial\mu_{1}}(0)&\displaystyle\frac{\partial d_{n-1,\varepsilon}^{(1)}}{\partial\mu_{2}}(0)&\dots&\displaystyle\frac{\partial d_{n-1,\varepsilon}^{(1)}}{\partial\mu_{n-1}}(0)&\displaystyle\frac{\partial d_{n-1,\varepsilon}^{(1)}}{\partial\mu_{n}}(0)\end{array}\right). |  |

Let A ε A_{\varepsilon} be the ( n − 1) × ( n − 1) (n-1)\times(n-1) submatrix of D ​ F ε ​ ( 0) DF_{\varepsilon}(0) given by its first n − 1 n-1 columns. It follows from ( 36), ( 37) and ( 38) that det A 0 > 0 \det A_{0}>0. Hence, by using ( 33) and from the continuity of the determinant we know that det A ε > 0 \det A_{\varepsilon}>0 for ε ⩾ 0 \varepsilon\geqslant 0 small enough. Therefore, if we fix ε 0 ⩾ 0 \varepsilon_{0}\geqslant 0 small enough, we get from the Implicit Function Theorem that there are unique C 1 C^{1} functions μ i ∗ = μ i ∗ ​ ( μ n) \mu_{i}^{*}=\mu_{i}^{*}(\mu_{n}), i ∈ { 1, …, n − 1 } i\in\{1,\dots,n-1\}, with μ i ∗ ​ ( 0) = 0 \mu_{i}^{*}(0)=0 and such that

(39) |  | F ε 0 ​ ( μ 1 ∗ ​ ( μ n), …, μ n − 1 ∗ ​ ( μ n), μ n) = 0, F_{\varepsilon_{0}}(\mu_{1}^{*}(\mu_{n}),\dots,\mu_{n-1}^{*}(\mu_{n}),\mu_{n})=0, |  |

for | μ n | |\mu_{n}| small. Moreover, it follows from ( 33) and ( 37) that,

 | ∂ d n, ε 0 ∂ μ n ​ ( 0) > 0. \frac{\partial d_{n,\varepsilon_{0}}}{\partial\mu_{n}}(0)>0. |  |

Hence, d n, ε 0 ​ ( μ) ≠ 0 d_{n,\varepsilon_{0}}(\mu)\neq 0 if μ n ≠ 0 \mu_{n}\neq 0. Therefore, from ( 39) we know that for | μ n | ≠ 0 |\mu_{n}|\neq 0 small enough and μ i = μ i ∗ ​ ( μ n) \mu_{i}=\mu_{i}^{*}(\mu_{n}), X μ, ε 0 X_{\mu,\varepsilon_{0}} has a polycycle Γ n − 1 = Γ n − 1 ​ ( μ n) \Gamma^{n-1}=\Gamma^{n-1}(\mu_{n}) formed by n − 1 n-1 hyperbolic saddles p 1 ​ ( μ n), …, p n − 1 ​ ( μ n) p_{1}(\mu_{n}),\dots,p_{n-1}(\mu_{n}), and n − 1 n-1 heteroclinic connections L i ∗ = L i ∗ ​ ( μ n) L_{i}^{*}=L_{i}^{*}(\mu_{n}). It follows from the Implicit Function Theorem that p i ​ ( μ n) → p i p_{i}(\mu_{n})\to p_{i} as μ n → 0 \mu_{n}\to 0. In addition, from the continuous dependence with respect to initial conditions [2, Theorem 8 8] and the local Center-Stable Manifold Theorem [15, Theorem 1 1] we get that the closure L i ¯ \overline{L_{i}} of each regular orbit L i L_{i} of Γ n − 1 ​ ( μ n) \Gamma^{n-1}(\mu_{n}) (i.e. the regular orbit together with the two singularities given by its α \alpha and ω \omega -limits) converges to the closure of the regular orbits of Γ n \Gamma^{n}, in relation to the Hausdorff distance, as μ n → 0 \mu_{n}\to 0. More precisely, for every ε > 0 \varepsilon>0 there is δ > 0 \delta>0 such that if | μ n | < δ |\mu_{n}|<\delta, then the following statements hold.

1. (a)

d H ​ ( Γ n − 1 ​ ( μ n), Γ n) < ε d_{H}(\Gamma^{n-1}(\mu_{n}),\Gamma^{n})<\varepsilon.

2. (b)

d H ​ ( L n − 1 ∗ ​ ( μ n) ¯, L n ∪ L n − 1 ¯) < ε d_{H}(\overline{L_{n-1}^{*}(\mu_{n})},\overline{L_{n}\cup L_{n-1}})<\varepsilon.

3. (c)

d H ​ ( L i ∗ ​ ( μ n) ¯, L i ¯) < ε d_{H}(\overline{L_{i}^{*}(\mu_{n})},\overline{L_{i}})<\varepsilon, for each i ∈ { 1, …, n − 2 } i\in\{1,\dots,n-2\}.

see Figures 2 and 10.

\begin{overpic}[Fig6.eps] \put(80.0,57.0){$p_{1}$} \put(12.0,55.0){$p_{2}$} \put(62.0,13.0){$p_{3}$} \put(95.0,72.0){$B$} \put(56.5,35.5){$S$} \end{overpic}

Before the perturbation.

\begin{overpic}[Fig7x.eps] \put(80.0,57.0){$p_{1}$} \put(12.0,55.0){$p_{2}$} \put(62.0,13.0){$p_{3}$} \put(95.0,72.0){$B$} \put(56.0,36.0){$S$} \end{overpic}

After the perturbation.

\begin{overpic}[Fig28x.eps] \put(53.0,45.0){$p_{1}=p_{2}$} \put(7.0,50.0){$S$} \put(72.0,95.0){$B$} \end{overpic}

Before the perturbation.

\begin{overpic}[Fig29xx.eps] \put(52.5,44.5){$p_{1}$} \put(7.0,50.0){$S$} \put(72.0,95.0){$B$} \end{overpic}

After the perturbation.

Figure 10. Two llustrations of the bifurcation process. Since R n > 1 R_{n}>1 and R n − 1 < 1 R_{n-1}<1, it follows that Γ n \Gamma^{n} is stable and Γ n − 1 \Gamma^{n-1} is unstable.

For each j ∈ { 1, …, n − 1 } j\in\{1,\dots,n-1\}, let

 | R j ∗ ​ ( μ n) = ∏ i = 1 j r i | μ i = μ i ∗ ​ ( μ n), i ∈ { 1, …, n − 1 }, R_{j}^{*}(\mu_{n})=\prod_{i=1}^{j}r_{i}|_{\mu_{i}=\mu_{i}^{*}(\mu_{n}),\;i\in\{1,\dots,n-1\}}, |  |

and observe that R n − 1 ∗ < 1 R_{n-1}^{*}<1 and ( R i ∗ − 1) ​ ( R i − 1 ∗ − 1) < 0 (R_{i}^{*}-1)(R_{i-1}^{*}-1)<0, i ∈ { 2, …, n − 1 } i\in\{2,\dots,n-1\}, provided | μ n | > 0 |\mu_{n}|>0 is small enough. Hence, Γ n − 1 \Gamma^{n-1} is unstable if | μ n | ≠ 0 |\mu_{n}|\neq 0. Let S S be the curve given by Proposition 7 and let Ω μ n \Omega_{\mu_{n}} be the open region bounded by S S and Γ n − 1 ​ ( μ n) \Gamma^{n-1}(\mu_{n}). Since Ω μ n \Omega_{\mu_{n}} is positive invariant by the flow of X μ, ε 0 X_{\mu,\varepsilon_{0}} and Γ n − 1 \Gamma^{n-1} is unstable, it follows from the Poincaré-Bendixson Theorem that there is at least one periodic orbit C n ​ ( μ n) C_{n}(\mu_{n}) in Ω μ n \Omega_{\mu_{n}} that is not unstable.

If X X is not polynomial then we are outside the analytic framework and thus we might have the bifurcation of infinitely many periodic orbits (see Remark 10). In particular, C n ​ ( μ n) C_{n}(\mu_{n}) may not be isolated. In this case we can apply Proposition 8, with the compact support of Φ \Phi small enough such that it does not intersect a neighborhood of Γ n − 1 \Gamma^{n-1} (and thus does not perturb it), and hence obtain a close enough perturbed vector field that has C n ​ ( μ n) C_{n}(\mu_{n}) as a stable hyperbolic limit cycle.

On the other hand, we may have the bifurcation of at most a finite amount of periodic orbits. In this case every periodic orbit is isolated and thus C n ​ ( μ n) C_{n}(\mu_{n}) is a limit cycle.

If X X is polynomial then the perturbation is also polynomial and in particular analytic. This in addition with the fact that Γ n − 1 \Gamma^{n-1} is unstable (and thus cannot be accumulated by periodic orbits) and the fact that for analytic vector fields all limit cycles are isolated and with finite multiplicity, ensures the bifurcation of at most a finite number of periodic orbits. In particular, C n ​ ( μ n) C_{n}(\mu_{n}) is a limit cycle.

Either in the smooth or polynomial case, we claim that if at most a finite amount of periodic orbits bifurcate, then we can choose C n ​ ( μ n) C_{n}(\mu_{n}) to be stable limit cycle (but not necessarily hyperbolic). Indeed, if C n ​ ( μ n) C_{n}(\mu_{n}) is the unique limit cycle that bifurcates from Γ n \Gamma^{n}, then it is clear that it is stable. Suppose therefore that there are the bifurcation of k k nested limit cycles γ 1 ​ ( μ n), …, γ k ​ ( μ n) \gamma_{1}(\mu_{n}),\dots,\gamma_{k}(\mu_{n}), with γ j − 1 \gamma_{j-1} in the bounded region limited by γ j \gamma_{j}. Since γ k \gamma_{k} is the outermost limit cycle, it follows that γ k \gamma_{k} is stable from outside. Therefore if γ k \gamma_{k} is not stable, then it is unstable from the inside and thus γ k − 1 \gamma_{k-1} is stable from the outside. Similarly, if γ k − 1 \gamma_{k-1} is not stable then it is unstable from the inside. Therefore if none of γ 2, …, γ k \gamma_{2},\dots,\gamma_{k} are stable, then γ 1 \gamma_{1} must be stable from the outside. However since γ 1 \gamma_{1} is the innermost limit cycle, it also follows that it is stable from the inside and thus γ 1 \gamma_{1} is stable. This proves the claim.

In particular either in the smooth or polynomial case, observe that C n ​ ( μ n) C_{n}(\mu_{n}) has odd multiplicity and thus its existence persist for small perturbations.

Hence, if we fix μ n = μ n ∗ \mu_{n}=\mu_{n}^{*} small enough and let μ ∗ = ( μ 1 ∗ ​ ( μ n ∗), …, μ n − 1 ∗ ​ ( μ n ∗), μ n ∗) \mu^{*}=(\mu_{1}^{*}(\mu_{n}^{*}),\dots,\mu_{n-1}^{*}(\mu_{n}^{*}),\mu_{n}^{*}), then it follows by induction that there is an arbitrarily small perturbation of X μ ∗, ε 0 X_{\mu^{*},\varepsilon_{0}} bifurcating at least n − 1 n-1 limit cycles from Γ n − 1 ​ ( μ n ∗) \Gamma^{n-1}(\mu_{n}^{*}). Since C n ​ ( μ n ∗) C_{n}(\mu_{n}^{*}) persists for small perturbations, we have the bifurcation of at least n n limit cycles from Γ n \Gamma^{n}. This proves the theorem for the case Δ ⁡ ( Γ n, τ) = n \Delta(\Gamma^{n},\tau)=n.

We now study the general case. First observe that to expel p n p_{n} it is only necessary to have r n ≠ 1 r_{n}\neq 1, regardless of having r k = 1 r_{k}=1 for some other k ∈ { 1, …, n − 1 } k\in\{1,\dots,n-1\}. This can be seen by the definition of the map F ε: Λ → ℝ n − 1 F_{\varepsilon}\colon\Lambda\to\mathbb{R}^{n-1} given by,

 | F ε ​ ( μ) = ( d 1, ε ​ ( μ), …, d n − 2, ε ​ ( μ), d n − 1, ε ( 1) ​ ( μ)). F_{\varepsilon}(\mu)=\left(d_{1,\varepsilon}(\mu),\dots,d_{n-2,\varepsilon}(\mu),d_{n-1,\varepsilon}^{(1)}(\mu)\right). |  |

More precisely observe that components d 1, ε, …, d n − 2, ε d_{1,\varepsilon},\dots,d_{n-2,\varepsilon} are always smooth, while the last component d n − 1, ε ( 1) d_{n-1,\varepsilon}^{(1)} is smooth because r n ≠ 1 r_{n}\neq 1.

If Δ ⁡ ( Γ n) = n \Delta(\Gamma^{n})=n, then there is a permutation of the indexes σ \sigma such that Δ ⁡ ( Γ n, σ) = n \Delta(\Gamma^{n},\sigma)=n. In particular it is not hard to see that r σ ⁡ ( i) ≠ 1 r_{\sigma(i)}\neq 1 for every i ∈ { 1, …, n } i\in\{1,\dots,n\} and thus we can expel the singularities p σ ⁡ ( n), …, p σ ⁡ ( 1) p_{\sigma(n)},\dots,p_{\sigma(1)} one at a each step. Moreover it follows from the definition of Δ ⁡ ( Γ n, σ) = n \Delta(\Gamma^{n},\sigma)=n that at each step the stability of the polycycle reverses and then we have the bifurcation of at least one limit cycle.

If Δ ⁡ ( Γ n) = n − 1 \Delta(\Gamma^{n})=n-1 then there is a permutation of the indexes σ \sigma such that Δ ⁡ ( Γ n, σ) = n − 1 \Delta(\Gamma^{n},\sigma)=n-1. To simplify the notation we shall assume that σ \sigma is the trivial permutation τ \tau. From Δ ⁡ ( Γ n, τ) = n − 1 \Delta(\Gamma^{n},\tau)=n-1 we have that there is a unique i 0 ∈ { 1, …, n } i_{0}\in\{1,\dots,n\} such that

 | ( R i 0 − 1 − 1) ​ ( R i 0 − 1) ⩾ 0, ( R i − 1 − 1) ​ ( R i − 1) < 0, i ∈ { 1, …, i 0 − 1, i 0 + 1, …, n }, (R_{i_{0}-1}-1)(R_{i_{0}}-1)\geqslant 0,\quad(R_{i-1}-1)(R_{i}-1)<0,\quad i\in\{1,\dots,i_{0}-1,i_{0}+1,\dots,n\}, |  |

where R i = ∏ j = 1 i r j R_{i}=\prod_{j=1}^{i}r_{j}, i ∈ { 1, …, n } i\in\{1,\dots,n\}, and R 0 = R 1 − 1 R_{0}=R_{1}^{-1}. Observe that if ( R i − 1 − 1) ​ ( R i − 1) < 0 (R_{i-1}-1)(R_{i}-1)<0, then r i ≠ 1 r_{i}\neq 1.

If i 0 < n i_{0}<n then we can expel the singularities p n, p n − 1, …, p i 0 + 1 p_{n},p_{n-1},\dots,p_{i_{0}+1} one at a time and obtain a limit cycle at each step. In particular, we now have n − i 0 n-{i_{0}} limit cycles and a polycycle with hyperbolic saddles p 1, …, p i 0 − 1, p i 0 p_{1},\dots,p_{i_{0}-1},p_{i_{0}} such that

 | ( R i 0 − 1 − 1) ​ ( R i 0 − 1) ⩾ 0, ( R i − 1 − 1) ​ ( R i − 1) < 0, i ∈ { 1, …, i 0 − 1 }. (R_{i_{0}-1}-1)(R_{i_{0}}-1)\geqslant 0,\quad(R_{i-1}-1)(R_{i}-1)<0,\quad i\in\{1,\dots,i_{0}-1\}. |  |

If r i 0 ≠ 1 r_{i_{0}}\neq 1 then we just expel p i 0 p_{i_{0}} (resulting in no limit cycles in this particular step) and thus the following steps are now free to proceed normally.

If r i 0 = 1 r_{i_{0}}=1 then it plays no role in the alternation of the signs of R i − 1 R_{i}-1 and thus we can take a new indexation given by p i 0 ↦ p 1 p_{i_{0}}\mapsto p_{1} and p i ↦ p i + 1 p_{i}\mapsto p_{i+1} for i ∈ { 1, …, i 0 − 1 } i\in\{1,\dots,i_{0}-1\}. We now have a polycycle such that

 | ( R 0 − 1) ​ ( R 1 − 1) = 0, ( R 1 − 1) ​ ( R 2 − 1) = 0, ( R i − 1 − 1) ​ ( R i − 1) < 0, i ∈ { 3, …, i 0 }, (R_{0}-1)(R_{1}-1)=0,\quad(R_{1}-1)(R_{2}-1)=0,\quad(R_{i-1}-1)(R_{i}-1)<0,\quad i\in\{3,\dots,i_{0}\}, |  |

with the two equations on the left-hand side due to R 1 = r i 0 = 1 R_{1}=r_{i_{0}}=1 and R 0 = R 1 − 1 = 1 R_{0}=R_{1}^{-1}=1.

Hence we can expel the hyperbolic saddles p i 0, …, p 3 p_{i_{0}},\dots,p_{3}, obtaining i 0 − 2 i_{0}-2 more limit cycles, which adds up to n − 2 n-2 with the previous n − i 0 n-i_{0} that we had already bifurcated. We now have a polycycle Γ 2 \Gamma^{2} with two hyperbolic saddles p 1 p_{1} and p 2 p_{2} such that r 1 = r i 0 = 1 r_{1}=r_{i_{0}}=1 and r 2 ≠ 1 r_{2}\neq 1 and we must obtain one more limit cycle. To do this, observe that Γ 2 \Gamma^{2} has a well defined stability because R 2 = r 2 ≠ 1 R_{2}=r_{2}\neq 1. Let S S be the curve given by Proposition 7. Instead of expelling p 2 p_{2}, we now use the displacement maps d 1, ε d_{1,\varepsilon} and d 2, ε d_{2,\varepsilon} to break Γ 2 \Gamma^{2} in such a way that in addition with the curve S S, it creates an invariant region Ω \Omega from which the Poincaré-Bendixson Theorem ensures the existence of at least one limit cycle.

The case Δ ⁡ ( Γ n) = n − k \Delta(\Gamma^{n})=n-k for some k ∈ { 1, …, n − 2 } k\in\{1,\dots,n-2\} follows similarly. The only difference is that at the end to bifurcate the last limit cycle we may have a polycycle Γ k 0 + 1 \Gamma^{k_{0}+1}, for some k 0 ∈ { 1, …, k } k_{0}\in\{1,\dots,k\}, such that all its hyperbolic saddles p 1, …, p k 0, p k 0 + 1 p_{1},\dots,p_{k_{0}},p_{k_{0}+1}, except one, have hyperbolicity number r j = 1 r_{j}=1. In particular Γ k 0 + 1 \Gamma^{k_{0}+1} has a well defined stability and thus we can apply Proposition 7. At this point we can use the displacement functions d 1, ε, …, d k 0 + 1, ε d_{1,\varepsilon},\dots,d_{k_{0}+1,\varepsilon} to break all the heteroclinic connections of Γ k 0 + 1 \Gamma^{k_{0}+1} in such a way that we can apply the Poincaré-Bendixson Theorem to bifurcate at least one more limit cycle. See Figure 11.

\begin{overpic}[Fig10.eps] \put(78.0,85.0){$p_{1}$} \put(14.0,85.0){$p_{2}$} \put(-10.0,43.0){$p_{3}$} \put(14.0,0.0){$p_{4}$} \put(78.0,0.0){$p_{5}$} \put(101.0,43.0){$p_{6}$} \put(65.0,35.0){$S$} \end{overpic}

Unperturbed.

\begin{overpic}[Fig34.eps] \put(78.0,90.0){$p_{1}$} \put(14.0,90.0){$p_{2}$} \put(-9.0,45.0){$p_{3}$} \put(16.0,0.0){$p_{4}$} \put(76.0,0.0){$p_{5}$} \put(101.0,45.0){$p_{6}$} \put(62.0,35.0){$S$} \end{overpic}

Perturbed.

Figure 11. Illustration of the bifurcation process with n = 6 n=6, k 0 = 5 k_{0}=5 and such that there exists a unique i 0 ∈ { 1, …, 6 } i_{0}\in\{1,\dots,6\} such that r i 0 > 1 r_{i_{0}}>1 and r i = 1 r_{i}=1 for i ≠ i 0 i\neq i_{0}. In particular observe that Δ ⁡ ( Γ 6) = 1 \Delta(\Gamma^{6})=1. Blue means stable. Colors available in the online version.

Finally, observe that if X X is polynomial and ε 0 > 0 \varepsilon_{0}>0 is small enough, then X μ ∗, ε 0 X_{\mu^{*},\varepsilon_{0}} is also polynomial. On the other hand, if X X is smooth, then its approximations constructed in the proof are smooth as well. □ \square

###### Remark 10.

At the proof of Theorem 1 we observe that the case in which X X is smooth and infinitely many periodic orbits bifurcate from it is an exceptional case. More precisely, Mourtada [24, Theorem 3 3] proved that even in the smooth case, generically speaking at most a finite amount of periodic orbits bifurcate from a given hyperbolic polycycle. For more details, see Section 7.

## 6. The inverse problem and a concrete example

We start this section by considering an inverse problem. More concretely the problem of constructing a polycycle Γ n \Gamma^{n} from a given set { r 1, …, r n } \{r_{1},\dots,r_{n}\} of desired hyperbolicity ratios. In particular, we prove that every possibility is realizable by a polynomial vector field of degree at most n. n.

###### Proposition 9.

Given n ⩾ 3 n\geqslant 3, let r 1, …, r n ∈ ℝ r_{1},\dots,r_{n}\in\mathbb{R} be positive real numbers. Then there is a planar polynomial vector field X X of degree at most n n with a polycycle Γ n \Gamma^{n} composed by n n distinct hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n} such that r i r_{i} is the hyperbolicity ratio of p i p_{i}, i ∈ { 1, …, n } i\in\{1,\dots,n\}.

###### Proof.

For each i ∈ { 1, …, n } i\in\{1,\dots,n\} let ξ i = cos ⁡ ( 2 ​ i ​ π / n) + i ​ sin ⁡ ( 2 ​ i ​ π / n) \xi_{i}=\cos(2i\pi/n)+i\sin(2i\pi/n) be the roots of unity of order n n. For each ξ i ∈ ℂ \xi_{i}\in\mathbb{C} we associate the point p i ∈ ℝ 2 p_{i}\in\mathbb{R}^{2} given by p i = ( cos ⁡ ( 2 ​ i ​ π / n), sin ⁡ ( 2 ​ i ​ π / n)) p_{i}=(\cos(2i\pi/n),\sin(2i\pi/n)). It is well known that ξ 1, …, ξ n ∈ ℂ \xi_{1},\dots,\xi_{n}\in\mathbb{C} divides the unit circle equally and thus it can be seen as the vertices of a regular polygon of n n edges. Hence, the points p 1, …, p n ∈ ℝ 2 p_{1},\dots,p_{n}\in\mathbb{R}^{2} can also be seen as the vertices of a regular polygon Γ n ⊂ ℝ 2 \Gamma^{n}\subset\mathbb{R}^{2} of n n edges. Let l 1, …, l n ⊂ ℝ 2 l_{1},\dots,l_{n}\subset\mathbb{R}^{2} be the n n straight lines such that l i ∩ l i − 1 = { p i } l_{i}\cap l_{i-1}=\{p_{i}\}, i ∈ { 1, …, n } i\in\{1,\dots,n\}, with l 0 = l n, l_{0}=l_{n}, see Figure 12.

\begin{overpic}[Fig8.eps] \put(101.0,43.0){$p_{6}$} \put(78.0,85.0){$p_{1}$} \put(14.0,85.0){$p_{2}$} \put(-9.0,43.0){$p_{3}$} \put(14.0,0.0){$p_{4}$} \put(78.0,0.0){$p_{5}$} \par\put(48.0,75.0){$l_{1}$} \put(20.0,60.0){$l_{2}$} \put(20.0,25.0){$l_{3}$} \put(48.0,8.0){$l_{4}$} \put(75.0,25.0){$l_{5}$} \put(75.0,60.0){$l_{6}$} \end{overpic}

n = 6 n=6.

\begin{overpic}[Fig9.eps] \put(101.0,49.0){$p_{7}$} \put(81.0,91.0){$p_{1}$} \put(22.0,98.0){$p_{2}$} \put(-10.0,70.0){$p_{3}$} \put(-10.0,28.0){$p_{4}$} \put(22.0,0.0){$p_{5}$} \put(81.0,8.0){$p_{6}$} \par\put(53.0,82.0){$l_{1}$} \put(22.0,77.0){$l_{2}$} \put(8.0,47.0){$l_{3}$} \put(22.0,19.0){$l_{4}$} \put(53.0,12.0){$l_{5}$} \put(75.0,32.0){$l_{6}$} \put(75.0,65.0){$l_{7}$} \end{overpic}

n = 7 n=7.

Figure 12. Illustration of Γ n \Gamma^{n} with n = 6 n=6 and n = 7 n=7.

Let α i \alpha_{i}, β i \beta_{i}, d i ∈ ℝ d_{i}\in\mathbb{R} be such that l i l_{i} is given by α i ​ x 1 + β i ​ x 2 − d i = 0 \alpha_{i}x_{1}+\beta_{i}x_{2}-d_{i}=0 and write l i ​ ( x) = α i ​ x 1 + β i ​ x 2 − d i l_{i}(x)=\alpha_{i}x_{1}+\beta_{i}x_{2}-d_{i}. Let also X = ( P, Q) X=(P,Q) be the planar polynomial system of degree n n given by

(40) |  | P ( x) = − ∑ i = 1 n [β i A i ( x) ∏ j ≠ i l j ( x)], Q ( x) = ∑ i = 1 n [α i A i ( x) ∏ j ≠ i l j ( x)]. P(x)=-\sum_{i=1}^{n}\left[\beta_{i}A_{i}(x)\prod_{j\neq i}l_{j}(x)\right],\quad Q(x)=\sum_{i=1}^{n}\left[\alpha_{i}A_{i}(x)\prod_{j\neq i}l_{j}(x)\right]. |  |

with deg ⁡ A i = 1 \deg A_{i}=1, i ∈ { 1, …, n } i\in\{1,\dots,n\}. We claim that each l i l_{i} is an invariant straight line of X X. Indeed, let w ∈ l s w\in l_{s} and observe that

(41) |  | P ( w) = − β s A s ( w) ∏ j ≠ s l s ( w), Q ( w) = α s A s ( w) ∏ j ≠ s l s ( w). P(w)=-\beta_{s}A_{s}(w)\prod_{j\neq s}l_{s}(w),\quad Q(w)=\alpha_{s}A_{s}(w)\prod_{j\neq s}l_{s}(w). |  |

The claim now follows from the fact that ⟨ X ⁡ ( w), ( α s, β s) ⟩ = 0 \left<X(w),(\alpha_{s},\beta_{s})\right>=0, where recall ⟨ ⋅, ⋅ ⟩ \left<\cdot,\cdot\right> denotes the standard inner product of ℝ 2 \mathbb{R}^{2}. We now study the Jacobian matrix of X X at p s p_{s}, s ∈ { 1, …, n } s\in\{1,\dots,n\}. It follows from ( 40) that,

(42) |  | ∂ P ∂ x 1 = − ∑ i = 1 n [β i ∂ A i ∂ x 1 ∏ j ≠ i l j + β i A i ∑ k ≠ i ( α k ∏ j ≠ i, k l j)]. \frac{\partial P}{\partial x_{1}}=-\sum_{i=1}^{n}\left[\beta_{i}\frac{\partial A_{i}}{\partial x_{1}}\prod_{j\neq i}l_{j}+\beta_{i}A_{i}\sum_{k\neq i}\left(\alpha_{k}\prod_{j\neq i,k}l_{j}\right)\right]. |  |

For each s ∈ { 1, …, n } s\in\{1,\dots,n\} let,

(43) |  | M ⁡ ( s) = ∏ j ≠ s j ≠ s − 1 l j ​ ( p s). M(s)=\prod_{\begin{subarray}{c}j\neq s\\ j\neq s-1\end{subarray}}l_{j}(p_{s}). |  |

Since l s ​ ( p s) = l s − 1 ​ ( p s) = 0 l_{s}(p_{s})=l_{s-1}(p_{s})=0, from ( 42) we obtain that

(44) |  | ∂ P ∂ x 1 ​ ( p s) = − M ⁡ ( s) ​ ( α s − 1 ​ β s ​ A s ​ ( p s) + α s ​ β s − 1 ​ A s − 1 ​ ( p s)). \frac{\partial P}{\partial x_{1}}(p_{s})=-M(s)\bigl(\alpha_{s-1}\beta_{s}A_{s}(p_{s})+\alpha_{s}\beta_{s-1}A_{s-1}(p_{s})\bigr). |  |

Similarly,

(45) |  | ∂ P ∂ x 2 ​ ( p s) = − β s ​ β s − 1 ​ M ​ ( s) ​ ( A s ​ ( p s) + A s − 1 ​ ( p s)), ∂ Q ∂ x 1 ​ ( p s) = α s ​ α s − 1 ​ M ​ ( s) ​ ( A s ​ ( p s) + A s − 1 ​ ( p s)), ∂ Q ∂ x 2 ​ ( p s) = M ⁡ ( s) ​ ( α s ​ β s − 1 ​ A s ​ ( p s) + α s − 1 ​ β s ​ A s − 1 ​ ( p s)). \begin{array}[]{l}\displaystyle\frac{\partial P}{\partial x_{2}}(p_{s})=-\beta_{s}\beta_{s-1}M(s)\bigl(A_{s}(p_{s})+A_{s-1}(p_{s})\bigr),\\ \displaystyle\frac{\partial Q}{\partial x_{1}}(p_{s})=\alpha_{s}\alpha_{s-1}M(s)\bigl(A_{s}(p_{s})+A_{s-1}(p_{s})\bigr),\\ \displaystyle\frac{\partial Q}{\partial x_{2}}(p_{s})=M(s)\bigl(\alpha_{s}\beta_{s-1}A_{s}(p_{s})+\alpha_{s-1}\beta_{s}A_{s-1}(p_{s})\bigr).\end{array} |  |

Hence, from ( 44) and ( 45) the determinant of the Jacobian matrix of X X at p s p_{s} is

(46) |  | det D ​ X ​ ( p s) = − M ​ ( s) 2 ​ ( α s ​ β s − 1 − α s − 1 ​ β s) 2 ​ A s ​ ( p s) ​ A s − 1 ​ ( p s). \det DX(p_{s})=-M(s)^{2}(\alpha_{s}\beta_{s-1}-\alpha_{s-1}\beta_{s})^{2}A_{s}(p_{s})A_{s-1}(p_{s}). |  |

Since p s ∈ l i p_{s}\in l_{i} if, and only if i ∈ { s, s − 1 } i\in\{s,s-1\}, it follows that M ⁡ ( s) ≠ 0 M(s)\neq 0. Moreover, observe that

(47) |  | α s ​ β s − 1 − α s − 1 ​ β s = det ( α s α s − 1 β s β s − 1). \alpha_{s}\beta_{s-1}-\alpha_{s-1}\beta_{s}=\det\left(\begin{array}[]{cc}\alpha_{s}&\alpha_{s-1}\\ \beta_{s}&\beta_{s-1}\end{array}\right). |  |

Since l s l_{s} and l s − 1 l_{s-1} are never parallel, we know that ( 47) never vanishes. Therefore, it follows from ( 46) that p s p_{s} is a hyperbolic saddle if, and only if, A s ​ ( p s) ​ A s − 1 ​ ( p s) > 0 A_{s}(p_{s})A_{s-1}(p_{s})>0. Moreover, its eigenvalues are given by

(48) |  | μ s = − ( α s ​ β s − 1 − α s − 1 ​ β s) ​ M ​ ( s) ​ A s ​ ( p s), ν s = ( α s ​ β s − 1 − α s − 1 ​ β s) ​ M ​ ( s) ​ A s − 1 ​ ( p s). \mu_{s}=-(\alpha_{s}\beta_{s-1}-\alpha_{s-1}\beta_{s})M(s)A_{s}(p_{s}),\quad\nu_{s}=(\alpha_{s}\beta_{s-1}-\alpha_{s-1}\beta_{s})M(s)A_{s-1}(p_{s}). |  |

Given s ∈ { 1, …, n } s\in\{1,\dots,n\}, let w ∈ l s w\in l_{s} be in the segment between p s + 1 p_{s+1} and p s p_{s}. For Γ n \Gamma^{n} to be a polycycle, is necessary that w w is not a singularity of X X. It follows from ( 41) that w w is a singularity if, and only if A s ​ ( w) = 0 A_{s}(w)=0. Hence, we conclude that Γ n \Gamma^{n} is a polycycle composed by n n hyperbolic saddles p 1, …, p n p_{1},\dots,p_{n} if, and only if, A s ​ ( p s) ​ A s − 1 ​ ( p s) > 0 A_{s}(p_{s})A_{s-1}(p_{s})>0 and A s ​ ( w) ≠ 0 A_{s}(w)\neq 0, for every w ∈ l s w\in l_{s} in the segment between p s + 1 p_{s+1} and p s p_{s}, s ∈ { 1, …, n } s\in\{1,\dots,n\} and p n + 1 = p 1 p_{n+1}=p_{1}. We now study the hyperbolicity ratio of p s p_{s}. Observe that we can choose α s \alpha_{s} and β s \beta_{s} such that v s = ( α s, β s) v_{s}=(\alpha_{s},\beta_{s}) is unitary. Hence, ( 47) is the sine of the angle between ℓ s − 1 \ell_{s-1} and ℓ s \ell_{s}. Since Γ n \Gamma^{n} is a regular polygon, it follows that there is θ n ∈ ( 0, π) \theta_{n}\in(0,\pi) such that α s − 1 ​ β s − α s ​ β s − 1 = sin ⁡ θ n \alpha_{s-1}\beta_{s}-\alpha_{s}\beta_{s-1}=\sin\theta_{n}, for every s ∈ { 1, …, n } s\in\{1,\dots,n\}. Observe that we can choose v s v_{s} to points towards the bounded region of Γ n \Gamma^{n}, for every s ∈ { 1, …, n } s\in\{1,\dots,n\}.

Moreover, observe that l j ​ ( p s) l_{j}(p_{s}) is the distance with sign between p s p_{s} and l j l_{j}. Since Γ n \Gamma^{n} is a regular polygon, v s v_{s} is unitary and points towards the bounded region of Γ n \Gamma^{n}, we get from ( 43) that M ⁡ ( s) = M n > 0 M(s)=M_{n}>0, for every s ∈ { 1, …, n } s\in\{1,\dots,n\}. Therefore from ( 48) we obtain that

(49) |  | μ s = − sin ⁡ θ n ​ M n ​ A s ​ ( p s), ν s = sin ⁡ θ n ​ M n ​ A s − 1 ​ ( p s). \mu_{s}=-\sin\theta_{n}M_{n}A_{s}(p_{s}),\quad\nu_{s}=\sin\theta_{n}M_{n}A_{s-1}(p_{s}). |  |

Thus, if we choose A 1, …, A n A_{1},\dots,A_{n} such that A s ​ ( p s) > 0 A_{s}(p_{s})>0 and A s − 1 ​ ( p s) > 0 A_{s-1}(p_{s})>0, then we conclude that the hyperbolicity ratio of p s p_{s} is given by,

(50) |  | | μ s | ν s = A s ​ ( p s) A s − 1 ​ ( p s), \frac{|\mu_{s}|}{\nu_{s}}=\frac{A_{s}(p_{s})}{A_{s-1}(p_{s})}, |  |

for s ∈ { 1, …, n } s\in\{1,\dots,n\}. Given r 1, …, r n ∈ ℝ r_{1},\dots,r_{n}\in\mathbb{R} positive real numbers, we can choose the polynomial A s: ℝ 2 → ℝ A_{s}\colon\mathbb{R}^{2}\to\mathbb{R} of degree one such that

(51) |  | A s ​ ( p s) = r s, A s − 1 ​ ( p s) = 1, A_{s}(p_{s})=r_{s},\quad A_{s-1}(p_{s})=1, |  |

for every s ∈ { 1, …, n } s\in\{1,\dots,n\}. Hence, from ( 50) we know that r s r_{s} is the hyperbolicity ratio of p s p_{s}. Moreover, observe that since A s ​ ( p s) = r s > 0 A_{s}(p_{s})=r_{s}>0, A s ​ ( p s + 1) = 1 > 0 A_{s}(p_{s+1})=1>0 and deg ⁡ A s = 1 \deg A_{s}=1, it follows that A s ​ ( w) > 0 A_{s}(w)>0 for every w ∈ l s w\in l_{s} in the segment between p s + 1 p_{s+1} and p s p_{s}. Therefore, X X has no singularities between p s + 1 p_{s+1} and p s p_{s} and thus Γ n \Gamma^{n} is indeed a polycycle. ∎

###### Remark 11.

We observe that the construction presented at Proposition 9 results in a polycycle with the clockwise orientation, see Figure 2. If one wants a polycycle with the counter clockwise orientation, then it is sufficient to replace ( 51) by

 | A s ​ ( p s) = − 1, A s − 1 ​ ( p s) = − r s. A_{s}(p_{s})=-1,\quad A_{s-1}(p_{s})=-r_{s}. |  |

In particular, the hyperbolicity ratio is now given by | ν s | / μ s |\nu_{s}|/\mu_{s}.

We end this section with an example.

###### Proposition 10.

Set n ⩾ 3 n\geqslant 3. Then there is a polynomial vector field X X of degree n n with a polycycle Γ n \Gamma^{n} that has cyclicity at least n n inside the space of polynomial vector fields of degree n n, with the coefficients topology.

###### Proof.

Given n ⩾ 3 n\geqslant 3, let r 1, …, r n ∈ ℝ r_{1},\dots,r_{n}\in\mathbb{R} be positive real numbers and consider R i = ∏ j = 1 i r j R_{i}=\prod_{j=1}^{i}r_{j}. Observe that we can choose r 1, …, r n r_{1},\dots,r_{n} recursively such that R 1 ≠ 1 R_{1}\neq 1 and ( R i − 1) ​ ( R i − 1 − 1) < 0 (R_{i}-1)(R_{i-1}-1)<0, for every i ∈ { 2, …, n } i\in\{2,\dots,n\}. Without loss of generality, we can suppose r n > 1 r_{n}>1. For these r 1, …, r n r_{1},\dots,r_{n}, let X X be the planar polynomial vector field of degree n n given by Proposition 9. That is, let X = ( P, Q) X=(P,Q) be given by ( 40),

 | P ( x) = − ∑ i = 1 n [β i A i ( x) ∏ j ≠ i l j ( x)], Q ( x) = ∑ i = 1 n [α i A i ( x) ∏ j ≠ i l j ( x)], P(x)=-\sum_{i=1}^{n}\left[\beta_{i}A_{i}(x)\prod_{j\neq i}l_{j}(x)\right],\quad Q(x)=\sum_{i=1}^{n}\left[\alpha_{i}A_{i}(x)\prod_{j\neq i}l_{j}(x)\right], |  |

where l i ​ ( x) = α i ​ x 1 + β i ​ x 2 − d i l_{i}(x)=\alpha_{i}x_{1}+\beta_{i}x_{2}-d_{i} are such that the straight lines l i ​ ( x) = 0 l_{i}(x)=0 are invariant and satisfy l i ∩ l i − 1 = { p i } l_{i}\cap l_{i-1}=\{p_{i}\}, with p i = ( cos ⁡ ( 2 ​ i ​ π / n), sin ⁡ ( 2 ​ i ​ π / n)) p_{i}=(\cos(2i\pi/n),\sin(2i\pi/n)), for i ∈ { 1, …, n } i\in\{1,\dots,n\}. Moreover, recall that deg ⁡ A i = 1 \deg A_{i}=1 and A i ​ ( w) > 0 A_{i}(w)>0 for every w ∈ l i w\in l_{i} in the segment between p i + 1 p_{i+1} and p i p_{i}, i ∈ { 1, …, n } i\in\{1,\dots,n\}. Without loss of generality we can assume that Γ n \Gamma^{n} has the clockwise orientation. For s ∈ { 1, …, n } s\in\{1,\dots,n\} let H s: ℝ 2 → ℝ H_{s}\colon\mathbb{R}^{2}\to\mathbb{R} be the polynomial of degree n − 1 n-1 given by,

 | H s ​ ( x) = ∏ j ≠ s l j ​ ( x). H_{s}(x)=\prod_{j\neq s}l_{j}(x). |  |

Consider now the polynomial K: ℝ 2 × ℝ n → ℝ 2 K\colon\mathbb{R}^{2}\times\mathbb{R}^{n}\to\mathbb{R}^{2}

 | K ⁡ ( x, μ) = ∑ s = 1 n μ s ​ H s ​ ( x) ​ Y s ​ ( x), K(x,\mu)=\sum_{s=1}^{n}\mu_{s}H_{s}(x)Y_{s}(x), |  |

where μ = ( μ 1, …, μ n) ∈ ℝ n \mu=(\mu_{1},\dots,\mu_{n})\in\mathbb{R}^{n} and Y s ​ ( x) Y_{s}(x) is the constant vector field given by Y s ​ ( x) ≡ Y s ≡ ( − α s, − β s) Y_{s}(x)\equiv Y_{s}\equiv(-\alpha_{s},-\beta_{s}). Define

 | X μ ​ ( x) = X ⁡ ( x) + K ⁡ ( x, μ). X_{\mu}(x)=X(x)+K(x,\mu). |  |

Since K K has degree n − 1 n-1 in x ∈ ℝ 2 x\in\mathbb{R}^{2}, it follows that X μ X_{\mu} is a polynomial vector field of degree n n. Moreover, clearly X μ → X X_{\mu}\to X in the coefficients topology, as μ → 0 \mu\to 0. Let Λ ⊂ ℝ n \Lambda\subset\mathbb{R}^{n} be a small enough neighborhood of the origin and let d i: Λ → ℝ d_{i}\colon\Lambda\to\mathbb{R} be the displacement maps associated to the heteroclinic connections of Γ n \Gamma^{n}, i ∈ { 1, …, n } i\in\{1,\dots,n\}. Let also d n − 1 ( 1): Λ → ℝ d_{n-1}^{(1)}\colon\Lambda\to\mathbb{R} be the displacement map given by Proposition 3 (recall that r n > 1 r_{n}>1). Notice also that

(52) |  | X ⁡ ( x) ∧ ∂ K ∂ μ j ​ ( x, 0) = ( P, Q) ∧ ( − H j ​ α j, − H j ​ β j) = H j ​ ( − P ​ β j + Q ​ α j). X(x)\land\frac{\partial K}{\partial\mu_{j}}(x,0)=(P,Q)\land(-H_{j}\alpha_{j},-H_{j}\beta_{j})=H_{j}(-P\beta_{j}+Q\alpha_{j}). |  |

Let L i ⊂ l i L_{i}\subset l_{i} be the heteroclinic connection of Γ n \Gamma^{n} from p i + 1 p_{i+1} to p i p_{i}. Similarly to the proof of Theorem 1, we now study the sign of ( 52) on L i L_{i}. Let x i ∈ L i x_{i}\in L_{i} and let γ i ​ ( t) \gamma_{i}(t) be the parametrization of L i L_{i} given by the solution of X X, with initial condition γ i ​ ( 0) = x i \gamma_{i}(0)=x_{i}. It follows from ( 41) that,

(53) |  | P ⁡ ( γ i ​ ( t)) = − β i ​ A i ​ ( γ i ​ ( t)) ​ H i ​ ( γ i ​ ( t)), Q ⁡ ( γ i ​ ( t)) = α i ​ A i ​ ( γ i ​ ( t)) ​ H i ​ ( γ i ​ ( t)). P(\gamma_{i}(t))=-\beta_{i}A_{i}(\gamma_{i}(t))H_{i}(\gamma_{i}(t)),\quad Q(\gamma_{i}(t))=\alpha_{i}A_{i}(\gamma_{i}(t))H_{i}(\gamma_{i}(t)). |  |

Replacing ( 53) at ( 52) and knowing that ( α i, β i) (\alpha_{i},\beta_{i}) is unitary we obtain,

(54) |  | X ⁡ ( γ i ​ ( t)) ∧ ∂ K ∂ μ j ​ ( γ i ​ ( t), 0) = H j ​ ( γ i ​ ( t)) ​ H i ​ ( γ i ​ ( t)) ​ A i ​ ( γ i ​ ( t)). X(\gamma_{i}(t))\land\frac{\partial K}{\partial\mu_{j}}(\gamma_{i}(t),0)=H_{j}(\gamma_{i}(t))H_{i}(\gamma_{i}(t))A_{i}(\gamma_{i}(t)). |  |

Since R j ∘ γ i = 0 R_{j}\circ\gamma_{i}=0 if i ≠ j i\neq j, we conclude from ( 8) and ( 54) that if i ≠ j i\neq j, then ∂ d i ∂ μ j ​ ( 0) = 0 \frac{\partial d_{i}}{\partial\mu_{j}}(0)=0. Moreover, if i = j i=j, then it follows from A i ​ ( γ i ​ ( t)) > 0 A_{i}(\gamma_{i}(t))>0 that ∂ d i ∂ μ i ​ ( 0) > 0 \frac{\partial d_{i}}{\partial\mu_{i}}(0)>0, for every i ∈ { 1, …, n } i\in\{1,\dots,n\}. Since r n > 1 r_{n}>1, it follows from Proposition 3 and Corollary 1 that d n − 1 ( 1): Λ → ℝ d_{n-1}^{(1)}\colon\Lambda\to\mathbb{R} is a well defined function of class C 1 C^{1} such that,

 | ∂ d n − 1 ( 1) ∂ μ j ​ ( 0) = ∂ d n − 1 ∂ μ j ​ ( 0), \frac{\partial d_{n-1}^{(1)}}{\partial\mu_{j}}(0)=\frac{\partial d_{n-1}}{\partial\mu_{j}}(0), |  |

for every j ∈ { 1, …, n } j\in\{1,\dots,n\}. Then we can define F: Λ ⊂ ℝ n → ℝ n − 1 F\colon\Lambda\subset\mathbb{R}^{n}\to\mathbb{R}^{n-1} and

 | F ⁡ ( μ) = ( d 1 ​ ( μ), …, d n − 2 ​ ( μ), d n − 1 ( 1) ​ ( μ)), F(\mu)=\left(d_{1}(\mu),\dots,d_{n-2}(\mu),d_{n-1}^{(1)}(\mu)\right), |  |

and study its zero set to know the limit cycles and polycycles that persist. At this point the proof can be continued similarly to the one of Theorem 1 with minor changes and we omit all the details. ∎

## 7. Final considerations

Let X X be a planar C ∞ C^{\infty} -vector field with a hyperbolic polycycle Γ n \Gamma^{n} with hyperbolic saddles { p 1, …, p n } \{p_{1},\dots,p_{n}\}, hyperbolicity ratios r 1, …, r n ∈ ℝ > 0 r_{1},\dots,r_{n}\in\mathbb{R}_{>0} and distinct regular orbits { L 1, …, L n } \{L_{1},\dots,L_{n}\}, where p i p_{i} is the ω \omega -limit of L i L_{i}. Let also X μ X_{\mu}, with μ ∈ Λ \mu\in\Lambda and Λ ⊂ ℝ n \Lambda\subset\mathbb{R}^{n} a small enough neighborhood of the origin, be a n n -parameter C ∞ C^{\infty} -family of vector fields such that X 0 = X X_{0}=X. Let also d i: Λ → ℝ d_{i}\colon\Lambda\to\mathbb{R} be the associated displacement map of L i L_{i}, i ∈ { 1, …, n } i\in\{1,\dots,n\}.

As anticipated in Remark 10, it follows from Mourtada [24, Theorem 3 3] that generically speaking even in the smooth case the cyclicity of Γ n \Gamma^{n} is finite and depends only on the number n n of hyperbolic saddles. More precisely, for each n ∈ ℕ n\in\mathbb{N} there is a finite set of generic algebraic conditions

(55) |  | g j, n ​ ( r 1, …, r n) ≠ 0, j ∈ { 1, …, N ⁡ ( n) }, g_{j,n}(r_{1},\dots,r_{n})\neq 0,\quad j\in\{1,\dots,N(n)\}, |  |

with g j, n g_{j,n} polynomials of n n variables and with integer coefficients; and an integer number e ⁡ ( n) e(n) that depends only on n n, such that for any smooth vector field X X with a polycycle Γ n \Gamma^{n}, with hyperbolicity ratios satisfying ( 55), and any perturbation family X μ X_{\mu} of X X, it holds Cycl ​ ( X, X μ, Γ n) ⩽ e ⁡ ( n) \textit{Cycl }(X,X_{\mu},\Gamma^{n})\leqslant e(n). See [24, p. 722 722].

Among the generic conditions we have those named by Mourtada [24, p. 722 722] as “ C ​ H CH -conditions” (*Condition Hyperbolique*), given by:

1. [CH]

For each subset J ⊂ { 1, …, n } J\subset\{1,\dots,n\}, ∏ j ∈ J r j ≠ 1 \prod_{j\in J}r_{j}\neq 1.

For n ⩽ 3 n\leqslant 3 these are the only conditions. For n ⩾ 4 n\geqslant 4 other conditions appear, see [24, p. 723]. So far it is known that e ⁡ ( n) = n e(n)=n for n ⩽ 3 n\leqslant 3 and e ⁡ ( 4) = 5 e(4)=5, see [25, 26, 14, 22] and the references therein. Explicit upper bounds for e ⁡ ( n) e(n) are known for n ⩾ 5 n\geqslant 5 but they are extremely large and believed to be not sharp. For example, it is known that e ⁡ ( 5) ⩽ 65533 e(5)\leqslant 65533, see [27].

The semi-algebraic conditions ( 55) define an open and dense semi-algebraic subset U U in ℝ n \mathbb{R}^{n} (the space of the hyperbolicity ratios ( r 1, …, r n) (r_{1},\dots,r_{n})) and for each connected component of U U there is a given cyclicity, Roussarie [29, Remark 30 30].

Therefore we observe that Theorem 1 provides a lower bound on each one of these connected components. In particular, since U U is open and dense, it follows that it contains a n n -tuple ( r 1, …, r n) (r_{1},\dots,r_{n}) such that

 | ( R i − 1) ​ ( R i − 1 − 1) < 0, ∀ i ∈ { 1, …, n }. (R_{i}-1)(R_{i-1}-1)<0,\quad\forall i\in\{1,\dots,n\}. |  |

Hence Theorem 1 also provides a new proof for the already known fact [22] that e ⁡ ( n) ⩾ n e(n)\geqslant n for every n ∈ ℕ n\in\mathbb{N}. Moreover, it follows from Propositions 9 and 10 that this lower bound is realizable by *polynomial*vector fields of degree n n, with the perturbation also polynomial of degree at most n n, and arbitrarily small in relation to the coefficients topology.

Let ℓ = l 1 \ell=l_{1} be the transversal section at the regular orbit L 1 L_{1} where the displacement map d 1 d_{1} takes place, endowed with a coordinate system identifying ℓ \ell with { t ∈ ℝ: | t | < ε } \{t\in\mathbb{R}\colon|t|<\varepsilon\}, ε > 0 \varepsilon>0 small enough, such that t = 0 t=0 is the intersection point ℓ ∩ Γ n \ell\cap\Gamma^{n} and 0 < t < ε 0<t<\varepsilon is contained in the domain of the first return map associated with Γ n \Gamma^{n}. Let also b i ​ ( μ) = σ 0 ​ d i ​ ( μ) b_{i}(\mu)=\sigma_{0}d_{i}(\mu), i ∈ { 1, …, n } i\in\{1,\dots,n\} (where we recall that σ 0 ∈ { − 1, 1 } \sigma_{0}\in\{-1,1\} depends whether the first return map is defined in the inner or outer region of Γ n \Gamma^{n}, see Section 3). If the hyperbolicity ratios r 1, …, r n r_{1},\dots,r_{n} satisfies the generic conditions ( 55), there is a continuous function ρ: Λ → ℝ \rho\colon\Lambda\to\mathbb{R}, with ρ ⁡ ( 0) = 0 \rho(0)=0, such that the first return map π: ( ρ ⁡ ( μ), ε) × Λ → ℓ \pi\colon(\rho(\mu),\varepsilon)\times\Lambda\to\ell is well defined and the solutions of π ⁡ ( t, μ) = t \pi(t,\mu)=t (i.e. the periodic orbits that bifurcate form Γ n \Gamma^{n}) are also solutions of

(56) |  | ( … ( ( t r 1 ​ ( μ) + b 1 ( μ)) r 2 ​ ( μ) + b 2 ( μ)) r 3 ​ ( μ) ⋯ + b n − 1 ( μ)) r n ​ ( μ) + b n ( μ) = α ( μ) t, \Bigr(\dots\bigr((t^{r_{1}(\mu)}+b_{1}(\mu))^{r_{2}(\mu)}+b_{2}(\mu)\bigl)^{r_{3}(\mu)}\dots+b_{n-1}(\mu)\Bigl)^{r_{n}(\mu)}+b_{n}(\mu)=\alpha(\mu)t, |  |

with α ⁡ ( μ) > 0 \alpha(\mu)>0 for every μ ∈ Λ \mu\in\Lambda. See [22] and [23, Theorem 1 1 and p. 276 276]. In particular, we have that the generic cyclicity e ⁡ ( n) e(n) is bounded above by the maximum number fp ⁡ ( n) \operatorname{fp}(n) of solutions of equation ( 56). We observe that these number need not to be equal because ( 56) may have solutions far away from t = 0 t=0, while the limit cycles are represented only by those solutions that bifurcate from t = 0 t=0. If n = 3 n=3 for example, Mourtada [26] proved that e ⁡ ( 3) = 3 e(3)=3, while Panazzolo [27] proved that fp ⁡ ( 3) = 5 \operatorname{fp}(3)=5.

We observe that Propositions 9 and 10 can be used to prove that a given equation of the form ( 56) may be realizable by a family of polynomial vector fields of degree n n. More precisely, Proposition 9 ensures that any prescribed set of hyperbolicity ratios ( r 1 ​ ( 0), …, r n ​ ( 0)) (r_{1}(0),\dots,r_{n}(0)) is realizable, while Proposition 10 provides a perturbation family X μ X_{\mu} such that the map μ ↦ ( b 1 ​ ( μ), …, b n ​ ( μ)) \mu\mapsto(b_{1}(\mu),\dots,b_{n}(\mu)) has full rank at μ = 0 \mu=0.

In other words (see Roussarie [29, Section 5.4.2 5.4.2]), for any prescribed initial condition we have a *generic unfolding*realizable by a family of polynomial vector fields of degree n n.

For more details we refer to Roussarie [29, Chapter 5 5] and Panazzolo [27]. Since the unfolding of the first return map of a hyperbolic polycycle is also intrinsically linked with the unfoldings of the *Dulac map*of its hyperbolic saddles, we also refer to the recent works of Marin and Villadelprat [18, 19, 21].

## Acknowledgments

We thank the reviewers for their careful and thoughtful comments and suggestions which help us to improve the presentation of this paper. This work is supported by the Spanish State Research Agency, through the projects PID2022-136613NB-I00 grant and the Severo Ochoa and María de Maeztu Program for Centers and Units of Excellence in R&D (CEX2020-001084-M), grant 2021-SGR-00113 from AGAUR, Generalitat de Catalunya, by CNPq, grant 304798/2019-3, by Agence Nationale de la Recherche (ANR), project ANR-23-CE40-0028, and São Paulo Research Foundation (FAPESP), grants 2019/10269-3, 2021/01799-9, 2022/14353-1 and 2023/02959-5.

## References

- [1] A. Andronov and E. Leontovich, On the generation of limit cycles from a loop of a separatrix and from the separatrix of the state of equilibrium of saddle-knot type, Mat. Sb., N. Ser. 48(90), 335-376 (1959).
- [2] A. Andronov et al, Theory of bifurcations of dynamic systems on a plane, Translated from the Russian Halsted Press, John Wiley & Sons, New York-Toronto; Israel Program for Scientific Translations, Jerusalem-London, 1973. xiv+482 pp.
- [3] T. R. Blows and L. M. Perko, Bifurcation of limit cycles from centers and separatrix cycles of planar analytic systems, SIAM Rev. 36, No. 3, 341-376 (1994).
- [4] L. Cherkas, The stability of singular cycles, Differ. Equations 4 (1968), 524-526 (1972).
- [5] A. Dukov, Multiplicities of limit cycles appearing after perturbations of hyperbolic polycycles, Sb. Math. 214, No. 2, 226-245 (2023)
- [6] F. Dumortier, J. Llibre and J. C. Artés, Qualitative theory of planar differential systems, Universitext, Springer-Verlag, Berlim, 2006.
- [7] A. Gasull, V. Mañosa and F. Mañosas, Stability of certain planar unbounded polycycles, J. Math. Anal. Appl. 269, No. 1, 332-351 (2002).
- [8] M. Golubitsky and V. Guillemin, Stable mappings and their singularities, Grad. Texts Math., Springer-Verlag. x, 209 p. (1973)
- [9] J. Guckenheimer and P. Holmes, Nonlinear oscillations, dynamical systems, and bifurcations of vector fields, Springer-Verlag, New York, 42. XVI+453 p. (1983).
- [10] M. Han, S. Hu and X. Liu, On the stability of double homoclinic and heteroclinic cycles, Nonlinear Anal., Theory Methods Appl., Ser. A, Theory Methods 53, No. 5, 701-713 (2003).
- [11] M. Han, Y. Wu and P. Bi, Bifurcation of limit cycles near polycycles with n vertices, Chaos Solitons Fractals 22, No. 2, 383-394 (2004).
- [12] M. Han and H. Zhu, The loop quantities and bifurcations of homoclinic loops, J. Differ. Equations 234, No. 2, 339-359 (2007).
- [13] M. W. Hirsch, Differential Topology, Graduate Texts in Mathematics, Springer Verlag (1976).
- [14] A. Jacquemard, F. Khechichine-Mourtada and A. Mourtada, Algorithmes formels appliqués à l’étude de la cyclicité d’un polycycle algébrique générique à quatre sommets hyperboliques, Nonlinearity 10, No. 1, 19-53 (1997).
- [15] A. Kelley, The stable, center-stable, center, center-unstable, unstable manifolds, J. Differ. Equations 3, 546-570 (1967).
- [16] E. H Kingsley, Bernstein Polynomials for Functions of Two Variables of Class C(k), Proc. Am. Math. Soc. 2, 64-71 (1951).
- [17] Y. Kuznetsov, Elements of applied bifurcation theory, Applied Mathematical Sciences 112. New York, NY: Springer. xxii, 631 p. (2004).
- [18] D. Marin and J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: Local setting, J. Differ. Equations 269, No. 10, 8425-8467 (2020).
- [19] D. Marin and J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: General setting, J. Differ. Equations 275, 684-732 (2021).
- [20] D. Marin and J. Villadelprat, On the cyclicity of Kolmogorov polycycles, Electron. J. Qual. Theory Differ. Equ. 2022, Paper No. 35, 31 p. (2022).
- [21] D. Marin and J. Villadelprat, Asymptotic expansion of the Dulac map and time for unfoldings of hyperbolic saddles: coefficient properties J. Differ. Equations 404, 43-107 (2024).
- [22] A. Mourtada, Polycycles hyperboliques génériques à trois et à quatre sommets, These de Doctorat. Universite de Bourgogne
- [23] A. Mourtada, Cyclicite finie des polycycles hyperboliques de champs de vecteurs du plan mise sous forme normale, Bifurcations of planar vector fields, Proc. Meet., Luminy/Fr. 1989, Lect. Notes Math. 1455, 272-314 (1990).
- [24] A. Mourtada, Cyclicité finie des polycycles hyperboliques de champs de vecteurs du plan. Algorithme de finitude, Ann. Inst. Fourier 41, No. 3, 719-753 (1991).
- [25] A. Mourtada, Degenerate and Non-trivial Hyperbolic Polycycles with Two Vertices, J. Differ. Equations 113, No. 1, 68-83 (1994).
- [26] A. Mourtada, Bifurcation de cycles limites au voisinage de polycycles hyperboliques et génériques à trois sommets, Ann. Fac. Sci. Toulouse, VI. Sér., Math. 3, No. 2, 259-292 (1994).
- [27] D. Panazzolo, Solutions of the equation a n + ( a n − 1 + ⋯ ( a 2 + ( a 1 + x r 1) r 2) ⋯) r n = b x a_{n}+(a_{n-1}+\cdots(a_{2}+(a_{1}+x^{r_{1}})^{r_{2}})\cdots)^{r_{n}}=bx, to appear in Saõ Paulo J. Math. Sci. 2024. Stability and Bifurcation - Memorial Issue Dedicated to Jorge Sotomayor.
- [28] L. Perko, Homoclinic loop and multiple limit cycle bifurcation surfaces, Trans. Am. Math. Soc. 344, No. 1, 101-130 (1994).
- [29] R. Roussarie, Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem, Modern Birkhäuser Classics 164. Basel: Birkhäuser. xvii, 204 p. (2013).
- [30] P. Santana, Stability and Cyclicity of Polycycles in Non-smooth Planar Vector Fields, Qual. Theory Dyn. Syst. 22, No. 4, Paper No. 142, 33 p. (2023).
- [31] P. Santana, On the structural instability of non-hyperbolic limit cycles on planar polynomial vector fields, São Paulo J. Math. Sci. (2024).
- [32] D. Shafer, Structural stability and generic properties of planar polynomial vector fields, Rev. Mat. Iberoam. 3, No. 3-4, 337-355 (1987).
- [33] L. Sheng, M. Han, Y. Tian, On the Number of Limit Cycles Bifurcating from a Compound Polycycle, Int. J. Bifurcation Chaos Appl. Sci. Eng. 30, No. 7, 16 p. (2020).
- [34] J. Sotomayor, Curvas Definidas por Equações Diferenciais no Plano, IMPA, 1981, 13º Colóquio Brasileiro de Matemática.
- [35] J. Sotomayor, Stable planar polynomial vector fields, Rev. Mat. Iberoam. 1, No. 2, 15-23 (1985).
- [36] Y. Tian and M. Han, Hopf and homoclinic bifurcations for near-Hamiltonian systems, J. Differ. Equations 262, No. 4, 3214-3234 (2017).
- [37] V. A Zorich, Mathematical analysis II, Universitext, 2nd edition, xx+720 p. (2016).


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:claudio.buzzi@unesp.br;%20paulo.santana@unesp.br
[4]: mailto:armengol.gasull@uab.cat
