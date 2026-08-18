<!-- source: https://arxiv.org/html/2405.04281v3 | converted from HTML -->

On a variant of Hilbert’s 16th problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2405.04281v3 [math.DS] 26 Sep 2024

# On a variant of Hilbert’s 16th problem

Armengol Gasull 1 and Paulo Santana 2 Address: 1 Departament de Matemàtiques, Facultat de Ciències, Universitat Autònoma de Barcelona, 08193 Bellaterra, Barcelona, Spain ; and Centre de Recerca Matemàtica, Edifici Cc, Campus de Bellaterra, 08193 Cerdanyola del Vallès (Barcelona), Spain Email address: [armengol.gasull@uab.cat][3] Address: 2 IBILCE–UNESP, CEP 15054–000, S. J. Rio Preto, São Paulo, Brazil Email address: [paulo.santana@unesp.br][4]

###### Abstract.

We study the number of limit cycles that a planar polynomial vector field can have as a function of its number m m of monomials. We prove that the number of limit cycles increases at least quadratically with m m and we provide good lower bounds for m ⩽ 10 m\leqslant 10.

###### Key words and phrases:

Limit cycles; Hilbert 16th problem; Abelian integrals

###### 2020 Mathematics Subject Classification

Primary: 34C07. Secondary: 37G15

## 1. Introduction and statement of the main results

In his address to the International Congress of Mathematicians in Paris 1900, David Hilbert raised his famous list of problems for the 20 20 th century [8], with the 16 16 th problem being divided in two parts. In the first part motivated by *Harnack’s Curve Theorem*[22], Hilbert asks from a description of the relative positions of the ovals of the algebraic curves satisfying Harnack’s upper bound.

In the second part, motivated by finding an analogous to Harnack’s result, Hilbert asks for the maximum number and relative position of limit cycles of planar polynomial vector fields. More precisely, given a planar polynomial vector field X X, let π ⁡ ( X) \pi(X) denote its number of limit cycles (i.e. isolated periodic orbits), where the value infinity is also admitted. Let also 𝒳 n \mathcal{X}_{n} be the family of the planar polynomial vector fields X = ( P, Q) X=(P,Q) of degree n n (i.e. max ⁡ { deg ⁡ P, deg ⁡ Q } = n \max\{\deg P,\deg Q\}=n). The *Hilbert number*ℋ ⁡ ( n) ∈ ℤ ⩾ 0 ∪ { ∞ } \mathcal{H}(n)\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\} is given by

 | ℋ ⁡ ( n) = sup { π ⁡ ( X): X ∈ 𝒳 n }. \mathcal{H}(n)=\sup\{\pi(X)\colon X\in\mathcal{X}_{n}\}. |  |

The second part of Hilbert’s 16 16 th problem consists in providing an upper bound for ℋ ⁡ ( n) \mathcal{H}(n), as a function of n n, and a description of the relative position of such limit cycles. This problem is still open and is also part of Smale’s list of problems for the 21 21 th century [38]. In his own words: *except for the Riemann hypothesis it seems to be the most elusive of Hilbert’s problems*. Despite the many attempts, no progress was made in finding upper bounds for ℋ ⁡ ( n) \mathcal{H}(n). So far it is not even known if ℋ ⁡ ( 2) \mathcal{H}(2) is finite or not. While it has not been possible to find upper bounds for ℋ ⁡ ( n) \mathcal{H}(n), there has been success in obtaining lower bounds. It is known that ℋ ⁡ ( n) \mathcal{H}(n) increases at least as fast as O ⁡ ( n 2 ​ ln ⁡ n) O(n^{2}\ln n). See [12, 21]. In fact, it was even conjectured in 1988 by Lloyd that ℋ ⁡ ( n) \mathcal{H}(n) is of order O ⁡ ( n 3), O(n^{3}), see [27]. For lower values of n n, as far as we know, at this moment the best lower bounds are ℋ ⁡ ( 2) ⩾ 4 \mathcal{H}(2)\geqslant 4 [10, 39], ℋ ⁡ ( 3) ⩾ 13 \mathcal{H}(3)\geqslant 13 [26] and ℋ ⁡ ( 4) ⩾ 28 \mathcal{H}(4)\geqslant 28 [33]. For more lower bounds, we refer to [33, 21].

In this paper we study a variant of Hilbert’s 16 16 th problem. Instead of looking at the number of limit cycles as a function of the degree of X X, we look it as a function of the number of monomials.

We now provide a precise statements of our main results. Given a planar polynomial vector field X = ( P, Q) X=(P,Q), we say that X X has m m monomials if the sum of the number of monomials of P P and Q Q is equal to m m. Let ℳ m \mathcal{M}_{m} be the family of planar polynomial vector fields with m m monomials, independently of its degree. We define the *Hilbert monomial number*ℋ M ​ ( m) ∈ ℤ ⩾ 0 ∪ { ∞ } \mathcal{H}^{M}(m)\in\mathbb{Z}_{\geqslant 0}\cup\{\infty\} as

 | ℋ M ​ ( m) = sup { π ⁡ ( X): X ∈ ℳ m }. \mathcal{H}^{M}(m)=\sup\{\pi(X)\colon X\in\mathcal{M}_{m}\}. |  |

So far very little is known about ℋ M ​ ( m) \mathcal{H}^{M}(m). It follows from Buzzi et al [9] that ℋ M ​ ( m) = 0 \mathcal{H}^{M}(m)=0 for m ∈ { 1, 2, 3 } m\in\{1,2,3\}, ℋ M ​ ( m) ⩾ m − 3 \mathcal{H}^{M}(m)\geqslant m-3 for m ⩾ 4 m\geqslant 4 and that there is a sequence of positive integer numbers m k → ∞ m_{k}\to\infty, such that ℋ M ​ ( m k) ⩾ N ⁡ ( m k) \mathcal{H}^{M}(m_{k})\geqslant N(m_{k}), with N ⁡ ( m) N(m) of order O ⁡ ( m ​ ln ⁡ m) O(m\ln m). This second lower bound follows from the results of Álvarez and collaborators [1] obtained for Liénard type vector fields and it can be seen that it can also be obtained from the lower bound of type O ⁡ ( n 2 ​ ln ⁡ n) O(n^{2}\ln n) of ℋ ⁡ ( n). \mathcal{H}(n).

In our first main result we improve these general lower bounds proving that ℋ M ​ ( m) \mathcal{H}^{M}(m) increases at least with order O ⁡ ( m 2) O(m^{2}).

###### Theorem 1.

If m ⩾ 9 m\geqslant 9, then ℋ M ​ ( m) ⩾ 1 2 ​ m 2 − 3 ​ m − 8 \mathcal{H}^{M}(m)\geqslant\frac{1}{2}m^{2}-3m-8.

As we will see, our proof is based on the study of some Abelian integrals and it is self-contained.

We remark that the main goal of the above result is only to show the quadratic growth of ℋ M ​ ( m) \mathcal{H}^{M}(m). For small m m the given lower bound is not good at all. For instance the result shows that ℋ M ​ ( 10) ⩾ 12 \mathcal{H}^{M}(10)\geqslant 12 while in our next result we prove that ℋ M ​ ( 10) ⩾ 32 \mathcal{H}^{M}(10)\geqslant 32. In fact, as we will see, Theorem 1 is a corollary of the sharper result given in Proposition 1: for any non-negative integer numbers n n and r r, there are planar polynomial vector fields with n + r + 4 n+r+4 monomials and at least 2 ​ n ​ ( r + 1) + n ⁡ ( 1 + ( − 1) r) 2n(r+1)+n\big(1+(-1)^{r}\big) limit cycles. Next we will study in more detail better lower bounds of ℋ M ​ ( m) \mathcal{H}^{M}(m) for m ≤ 10. m\leq 10.

It follows among the series of papers about the limit cycles of cubic Liénard systems of Dumortier and Li that ℋ M ​ ( 6) ⩾ 4 \mathcal{H}^{M}(6)\geqslant 4 [15] and ℋ M ​ ( 7) ⩾ 5 \mathcal{H}^{M}(7)\geqslant 5 [16]. Also, it follows from Chow et al [11, Sect. 4.2 4.2] that ℋ M ​ ( 5) ⩾ 3 \mathcal{H}^{M}(5)\geqslant 3. In recent years Bréhard et al [6, Chap. 6 6] and [7, Sect. 7 7] developed a computed assisted method to study the zeros of Abelian integrals. With this method they provided a computed assisted proof of the existence of a quartic vector field with at least 24 24 limit cycles. Since this vector field has only nine momonials, it follows that ℋ M ​ ( 9) ⩾ 24 \mathcal{H}^{M}(9)\geqslant 24. As far as we known, these are the only specific lower bounds known for small values of m m. In our second main result we obtain better lower bounds for values of 4 ⩽ m ⩽ 10. 4\leqslant m\leqslant 10. For m = 9 m=9, we replicate the known lower bound ℋ M ​ ( 9) ⩾ 24 \mathcal{H}^{M}(9)\geqslant 24 with a direct proof. For a summary of the previous and new lower bounds, see Table 1.

###### Theorem 2.

If m ∈ { 4, 5, 6 } m\in\{4,5,6\}, then ℋ M ​ ( m) ⩾ 12 \mathcal{H}^{M}(m)\geqslant 12. Moreover, ℋ M ​ ( 7) ⩾ 16 \mathcal{H}^{M}(7)\geqslant 16, ℋ M ​ ( 8) ⩾ 20 \mathcal{H}^{M}(8)\geqslant 20, ℋ M ​ ( 9) ⩾ 24 \mathcal{H}^{M}(9)\geqslant 24, and ℋ M ​ ( 10) ⩾ 32 \mathcal{H}^{M}(10)\geqslant 32.

To illustrate some of the vector fields involved in the proof of the above theorem we show the two families of vector fields that we have used to prove that ℋ M ​ ( 4) ⩾ 12 \mathcal{H}^{M}(4)\geqslant 12 and ℋ M ​ ( 9) ⩾ 24 \mathcal{H}^{M}(9)\geqslant 24. They are

(1) |  | x ˙ = α 1 ​ x g 11 ​ y g 12 − β 1 ​ x h 11 ​ y h 12, y ˙ = α 2 ​ x g 21 ​ y g 22 − β 2 ​ x h 21 ​ y h 22, \dot{x}=\alpha_{1}x^{g_{11}}y^{g_{12}}-\beta_{1}x^{h_{11}}y^{h_{12}},\quad\dot{y}=\alpha_{2}x^{g_{21}}y^{g_{22}}-\beta_{2}x^{h_{21}}y^{h_{22}}, |  |

for some α i \alpha_{i}, β i ∈ ℝ \beta_{i}\in\mathbb{R} and g i ​ j g_{ij}, h i ​ j ∈ ℤ > 0 h_{ij}\in\mathbb{Z}_{>0}, and

(2) |  | x ˙ = y − y 3 + ∑ k = 0 5 ( − 1) k ​ x 2 ​ ( 5 − k) + 1 ​ ( y a k) 2 ​ m k, y ˙ = x, \dot{x}=y-y^{3}+\sum_{k=0}^{5}(-1)^{k}x^{2(5-k)+1}\left(\frac{y}{a_{k}}\right)^{2m_{k}},\quad\dot{y}=x, |  |

with a i > 0 a_{i}>0, m i ∈ ℤ > 0 m_{i}\in\mathbb{Z}_{>0} and 1 ≪ m 1 ≪ ⋯ ≪ m 5 1\ll m_{1}\ll\dots\ll m_{5}, respectively. Notice that they have respectively 4 and 9 monomials, and we will show that there are values of the parameters with at least 12 and 24 limit cycles, respectively. The first one ( 1) is constructed from a so called *Planar-S system*studied at [4, 5] and having three limit cycles. That planar-S system is exactly of the form ( 1), but with exponents g i ​ j g_{ij}, h i ​ j ∈ ℝ, h_{ij}\in\mathbb{R}, and it is only defined in the first quadrant. As we will see, by perturbing these exponents (to transform them into rational numbers) and after some suitable changes of variables and time we will arrive to a new system of the form ( 1) that has at last three limit cycles in each quadrant, providing the desired lower bound. The second one ( 2) is studied by using Abelian integrals.

Table 1. Summary of the lower bounds of the Hilbert monomial numbers. Recall that ℋ M ​ ( m) = 0 \mathcal{H}^{M}(m)=0 for m ⩽ 3 m\leqslant 3.

Monomials | New lower bounds | Previous lower bounds |

4 4 | 12 12 | 1 1 |

5 5 | 12 12 | 3 3 |

6 6 | 12 12 | 4 4 |

7 7 | 16 16 | 5 5 |

8 8 | 20 20 | 5 5 |

9 9 | 24 24 | 24 24 |

10 10 | 32 32 | 24 24 |

m ⩾ 11 m\geqslant 11 | 1 2 ​ m 2 − 3 ​ m − 8 \frac{1}{2}m^{2}-3m-8 | m − 3 m-3 |

Asymptotic | O ⁡ ( m 2) O(m^{2}) | O ⁡ ( m ​ ln ⁡ m) O(m\ln m) |

We remark that in the third column of Table 1, the lower bound ℋ M ​ ( 10) ⩾ 24 \mathcal{H}^{M}(10)\geqslant 24 follows from the fact that in the previous known lower bound ℋ M ​ ( 9) ⩾ 24 \mathcal{H}^{M}(9)\geqslant 24, all the limit cycles have odd multiplicity and thus are persistent under small perturbations. Similarly the two lower bounds in the second column for m = 5 m=5 and 6 6 follow from the one obtained from m = 4. m=4. It is natural to believe that these two lower bounds could be improved, but until now, we have not been able to do it.

It is curious to observe that if we address to a similar question but for planar polynomial vector fields written in complex coordinates, that is the ones given by z ˙ = F ⁡ ( z, z ¯) \dot{z}=F(z,\bar{z}), where F F is a polynomial with m m monomials, a totally different result happens. On the one hand, these vector fields with m = 1 m=1 or m = 2 m=2 have at most 0, or 1 limit cycle, respectively [2]. On the other hand, when m = 3 m=3 (or higher) there is no upper bound for the number of limit cycles [20].

The idea of looking for the number of monomials instead of the degree of polynomials goes back to Descartes and his *rule of signs*, which states that if p: ℝ → ℝ p\colon\mathbb{R}\to\mathbb{R} is a polynomial with m m nonzero monomials, independently of its degree, then p p has at most m − 1 m-1 positive real roots, counting with multiplicity. In particular, it also follows that p p has at most 2 ​ m − 1 2m-1 distinct real roots ( m − 1 m-1 positive, m − 1 m-1 negative and eventually the root x = 0 x=0, which can be of any multiplicity). Moreover, there are attempts to extended Descartes’ rule of signs to the multiple variable case, such as the Kouchnirenko’s conjecture (nowadays known to be false). For more details, we refer to Problems 28 28 and 29 29 of [19].

Furthermore in more recent developments on real algebraic geometry, Harnack’s Curve Theorem is replaced by an upper bound depending solely on the *number of integer points*contained in the interior of the Newton polygon of the given real polynomial [25, 29], which in turn is related to the monomials of the polynomial. Moreover, it has also been shown by Mikhalkin [29] that this upper bound is also related to the connected components of the complement of the amoeba associated to the polynomial. For more details we refer to the survey of Mikhalkin [30] and the book of Itenberg et al [23]. For applications of such techniques of algebraic geometry to polynomial vector fields, we refer to Itenberg and Shustin [24]. For applications of the relation between a polynomial vector fields and its Newton polygon, we refer to Dalbelo et al [14] and the references therein.

Sprott [40] brought also applied the idea of looking to the number of monomials to the field of qualitative theory of ordinary differential equations by seeking for the *simplest*polynomial vector field in ℝ 3 \mathbb{R}^{3} exhibiting chaos. By *simple*Sprott means with as few monomials as possible. In his own words: *the simplicity refers to the algebraic representation rather than to the physical process described by the equations.*In particular, Sprott was able to find nineteen different quadratic vector fields defined on ℝ 3 \mathbb{R}^{3} exhibiting chaos and with either five monomials being two of them nonlinear, or six monomials being one of them nonlinear. Nowadays such quadratic vector fields are known as *Sprott A, Sprott B, … \dots, Sprott S*. For a qualitative study on some Sprott systems, we refer to [31] and references therein. Later Sprott [41] was able to find a simpler chaotic system, with five monomials being only one nonlinear. From this point of view it is interesting to observe that the celebrated Lorenz [28] and Rössler [35] systems are also quadratic, have seven monomials and, respectively, two or one of them are nonlinear.

Following this notion of simple vector field, Gasull [19] asks in his 8 ​ t ​ h 8th problem for the minimal m 0 ∈ ℕ m_{0}\in\mathbb{N} such that ℋ M ​ ( m 0) > m 0 \mathcal{H}^{M}(m_{0})>m_{0}, i.e. for the *simplest vector field with more limit cycles than monomials*. On that time it was known that 4 ⩽ m 0 ⩽ 9 4\leqslant m_{0}\leqslant 9 due to the cubic vector field of Li et al [26], with 9 9 monomials and 13 13 limit cycles. From Theorem 2 it now follows that m 0 = 4 m_{0}=4. As we will see in the proof that ℋ M ​ ( 4) ⩾ 12, \mathcal{H}^{M}(4)\geqslant 12, a system proving that m 0 = 4 m_{0}=4 is one of the form ( 1), but the approach used in the proof only shows the existence of an example and it does not provide neither explicit exponents nor explicit parameters. On the other hand, a very simple explicit example showing that ℋ M ​ ( 4) ⩾ 4 \mathcal{H}^{M}(4)\geqslant 4 is

(3) |  | x ˙ = a ​ x 2 ​ y 5 − a ​ y, y ˙ = x 3 ​ y 2 − x, \dot{x}=ax^{2}y^{5}-ay,\quad\dot{y}=x^{3}y^{2}-x, |  |

with a = − ( 1 + ε) a=-(1+\varepsilon) and ε > 0 \varepsilon>0 small enough. It has a limit cycle surrounding each one of the four critical points ( ± 1, ± 1) (\pm 1,\pm 1) born via an Andronov-Hopf bifurcation, see the end of the proof of Theorem 2.

While preparing a first version of this paper we thought that the first wanderings about the question of relating the number of limit cycles with the number of monomials were introduced in 2021 paper [9], but this is not true. To the best of our knowledge the first authors to address this type of questions were Boros, Hofbauer and coauthors, see the 2019 papers [4, 5]. In fact, in a recent 2024 meeting they comment this fact to the first author and also that their approach could be used to get good lower bounds for ℋ M ​ ( 4). \mathcal{H}^{M}(4). We thank very much them for their suggestion that have leaded us to improve the lower bounds of a previous version of Theorem 2.

The approach of counting the monomials of a vector field instead of its degree can be seen both as a strength or a weakness. This is so, because for instance affine changes of variables change the number of monomials, but keep the degree. It is a weakness, because in most cases the number of monomials increases but it is a strength because occasionally it can go down. A similar situation happens with the degree by using birational transformations, together with time reparametrizations. In any case, it is an interesting point of view to try to go inside the study of the number of limit cycles of natural families of vector fields.

Applications of this approach can be seen in the field of *Chemical reaction network*(CRN) [18], specially under the hypothesis of *mass action kinetics*(MAK) [42]. Roughly speaking, CRN models the behavior of real-world chemical systems, while MAK is the assumption that the *rate of a chemical reaction is directly proportional to the product of the activities or concentrations of the reactants*. For example, this means that given a chemical reaction A + 2 ​ B → C A+2B\to C, the *rate of occurrence*of the reaction is given by r ⁡ ( c A, c B) = α ​ c A ​ c B 2 r(c_{A},c_{B})=\alpha c_{A}c_{B}^{2}, where c A c_{A} and c B c_{B} are the concentrations of the chemicals A A and B B and α ∈ ℝ \alpha\in\mathbb{R} is a constant. Therefore, given a system of interrelated chemical reactions, its dynamics is molded by a polynomial system of differential equations in which each monomial represents a reaction. For an introduction of the topic, we refer to Müller and Regensburger [32]. For other applications we refer to [17, Chapter 7 7].

To fix a simple example with a limit cycle when m = 4, m=4, we recall the Higgins-Seklov model of glicolysis, see [37]. In adimensional form it writes as

 | x ˙ = 1 − x ​ y 2, y ˙ = a ​ x ​ y 2 − a ​ y, \dot{x}=1-xy^{2},\quad\dot{y}=axy^{2}-ay, |  |

where a a is a real positive parameter.

This paper is organized as follows. In next section we include some preliminaries about the well-known Poincaré–Pontryagin Theorem. Theorems 1 and 2 are proved in Section 3. The work ends with a small section with further thoughts.

## 2. The Poincaré–Pontryagin Theorem

Given a polynomial (resp. analytic or smooth) function H: ℝ 2 → ℝ H\colon\mathbb{R}^{2}\to\mathbb{R}, we associate the planar polynomial (resp. analytic or smooth) vector field X = ( P, Q) X=(P,Q) given by

 | P ⁡ ( x, y) = − ∂ H ∂ y ​ ( x, y), Q ⁡ ( x, y) = ∂ H ∂ x ​ ( x, y). P(x,y)=-\frac{\partial H}{\partial y}(x,y),\quad Q(x,y)=\frac{\partial H}{\partial x}(x,y). |  |

In this case we say that X X is *Hamiltonian*and that H H is its Hamiltonian function. In particular, observe that H H is a first integral of X X. Suppose that X X has a continuum of periodic orbits

 | A = { γ h: h ∈ ( a, b) } ⊂ { ( x, y) ∈ ℝ 2: H ⁡ ( x, y) ∈ ( a, b) }, A=\{\gamma_{h}\colon h\in(a,b)\}\subset\{(x,y)\in\mathbb{R}^{2}\colon H(x,y)\in(a,b)\}, |  |

with γ h \gamma_{h} depending continuously on h h. See Figure 1 (a). A maximal set with this property is called a period annulus.

\begin{overpic}[Fig1.eps] \put(101.0,83.0){$\gamma_{h_{3}}$} \put(97.0,76.0){$\gamma_{h_{2}}$} \put(95.0,70.0){$\gamma_{h_{1}}$} \put(13.0,85.0){$A$} \end{overpic}

( a) (a)

\begin{overpic}[Fig2.eps] \put(11.0,88.0){$A$} \put(60.0,37.5){$h$} \put(55.0,49.5){$\sigma$} \put(98.0,47.5){$P(h,\varepsilon)$} \put(50.0,89.0){$\gamma(h,\varepsilon)$} \end{overpic}

( b) (b)

Figure 1. Illustration of a continuum of periodic orbits and a displacement map.

Let X ε = ( P ε, Q ε) X_{\varepsilon}=(P_{\varepsilon},Q_{\varepsilon}) be a perturbation of X X given by

 | P ε ​ ( x, y) = P ⁡ ( x, y) + ε ​ f ​ ( x, y), Q ε ​ ( x, y) = Q ⁡ ( x, y) + ε ​ g ​ ( x, y), P_{\varepsilon}(x,y)=P(x,y)+\varepsilon f(x,y),\quad Q_{\varepsilon}(x,y)=Q(x,y)+\varepsilon g(x,y), |  |

with f f, g: ℝ 2 → ℝ g\colon\mathbb{R}^{2}\to\mathbb{R} real polynomials and | ε | |\varepsilon| small. Let σ ⊂ A \sigma\subset A be a segment that is transversal to every periodic orbit γ h ⊂ A \gamma_{h}\subset A of the unperturbed vector field X X. Given h ∈ ( a, b) h\in(a,b) and ε ≠ 0 \varepsilon\neq 0 small, let γ ⁡ ( h, ε) \gamma(h,\varepsilon) be the piece of orbit of the perturbed vector field X ε X_{\varepsilon} between the starting point h h on σ \sigma and the next intersection point P ⁡ ( h, ε) P(h,\varepsilon) with σ \sigma. See Figure 1 (b). Let d ⁡ ( h, ε) = P ⁡ ( h, ε) − h d(h,\varepsilon)=P(h,\varepsilon)-h be the *displacement map*associated to the perturbation X ε X_{\varepsilon}. As usual, observe that γ ⁡ ( h, ε) \gamma(h,\varepsilon) is a periodic orbit of X ε X_{\varepsilon} (resp. limit cycle) if, and only if, ( h, ε) (h,\varepsilon) is a zero (resp. isolated zero) of the displacement map. Moreover, given h ∈ ( a, b) h\in(a,b) we associate to γ h \gamma_{h} the line integral

(4) |  | I ⁡ ( h) = ∮ γ h f ​ 𝑑 y − g ​ 𝑑 x, I(h)=\oint_{\gamma_{h}}f\;dy-g\;dx, |  |

known as *Abelian Integral*.

###### Theorem 3 (Poincaré–Pontryagin).

Let X ε X_{\varepsilon}, d ⁡ ( h, ε) d(h,\varepsilon) and I ⁡ ( h) I(h) be as above. Then

(5) |  | d ⁡ ( h, ε) = ε ​ I ​ ( h) + ε 2 ​ φ ​ ( h, ε), d(h,\varepsilon)=\varepsilon I(h)+\varepsilon^{2}\varphi(h,\varepsilon), |  |

where φ ⁡ ( h, ε) \varphi(h,\varepsilon) is analytic and uniformly bounded for ( h, ε) (h,\varepsilon) in a neighborhood of ( h, 0) (h,0), h ∈ ( a, b) h\in(a,b).

For a proof of Theorem 3, see Christopher et al [13, p. 143 143]. It follows from ( 5) that if I I is well defined on ( h 1, h 2) (h_{1},h_{2}) and I ⁡ ( h 1) ​ I ​ ( h 2) < 0 I(h_{1})I(h_{2})<0, then for | ε | > 0 |\varepsilon|>0 small enough γ ⁡ ( h 1, ε) \gamma(h_{1},\varepsilon) and γ ⁡ ( h 2, ε) \gamma(h_{2},\varepsilon) bound, together with two segments of σ \sigma, a positive or negative invariant region of X ε X_{\varepsilon}. See Figure 2.

\begin{overpic}[Fig3.eps] \put(30.0,61.5){$\gamma(h_{1},\varepsilon)$} \put(95.0,90.0){$\gamma(h_{2},\varepsilon)$} \put(11.0,87.0){$A$} \end{overpic}

I ⁡ ( h 1) > 0 I(h_{1})>0 and I ⁡ ( h 2) < 0 I(h_{2})<0

\begin{overpic}[Fig4.eps] \put(30.0,61.5){$\gamma(h_{1},\varepsilon)$} \put(97.0,89.0){$\gamma(h_{2},\varepsilon)$} \put(11.0,87.0){$A$} \end{overpic}

I ⁡ ( h 1) < 0 I(h_{1})<0 and I ⁡ ( h 2) > 0 I(h_{2})>0

Figure 2. Illustration of the positive and negative invariant regions.

Hence, it follows from the Poincaré-Bendixson Theorem that X ε X_{\varepsilon} has at least one limit cycle between γ ⁡ ( h 1, ε) \gamma(h_{1},\varepsilon) and γ ⁡ ( h 2, ε) \gamma(h_{2},\varepsilon). Therefore, we have the following well-known corollary.

###### Corollary 1.

Let X ε X_{\varepsilon} and I ⁡ ( h) I(h) be as above. If I I is well defined on ( h 1, h 2) (h_{1},h_{2}) and I ⁡ ( h 1) ​ I ​ ( h 2) < 0 I(h_{1})I(h_{2})<0, then there is ε 0 > 0 \varepsilon_{0}>0 such that X ε X_{\varepsilon} has at least one limit cycle between γ h 1 \gamma_{h_{1}} and γ h 2 \gamma_{h_{2}}, for 0 < | ε | < ε 0 0<|\varepsilon|<\varepsilon_{0}.

###### Remark 1.

Let I ⁡ ( h) I(h) be as in ( 4). It follows from Green’s Theorem that if γ h \gamma_{h} is positively oriented then

 | I ⁡ ( h) = ∬ Γ h ∂ f ∂ x + ∂ g ∂ y ​ 𝑑 x ​ 𝑑 y, I(h)=\iint_{\Gamma_{h}}\frac{\partial f}{\partial x}+\frac{\partial g}{\partial y}\;dxdy, |  |

where Γ h ⊂ ℝ 2 \Gamma_{h}\subset\mathbb{R}^{2} is the interior region bounded by γ h \gamma_{h}.

## 3. Proof of the main results

###### Lemma 1.

Given r ∈ ℤ ⩾ 0 r\in\mathbb{Z}_{\geqslant 0}, let X r = ( P, Q r) X_{r}=(P,Q_{r}) be the planar polynomial vector field given by,

(6) |  | P ⁡ ( x, y) = P ⁡ ( y) = y − y 3, Q r ​ ( x, y) = Q r ​ ( x) = x ​ ∏ k = − r r ( x − k). P(x,y)=P(y)=y-y^{3},\quad Q_{r}(x,y)=Q_{r}(x)=x\prod_{k=-r}^{r}(x-k). |  |

Then the following statements hold.

1. (i)

X r X_{r} is Hamiltonian

2. (ii)

X r X_{r} has r + 3 r+3 monomials

3. (iii)

X r X_{r} has r + 1 r+1 centers on each of the lines y = ± 1 y=\pm 1 and r r centers on the line y = 0. y=0.

###### Proof.

Statements ( i) (i) and ( i ​ i) (ii) follow directly from ( 6). Hence, we focus on statement ( i ​ i ​ i) (iii). Observe that the singularities of X r X_{r} on the lines y = ± 1 y=\pm 1 are given by ( j, ± 1) (j,\pm 1), with j ∈ { − r, …, r } j\in\{-r,\dots,r\}. The Jacobian matrix at these singularities is given by,

 | D ​ X ​ ( j, ± 1) = ( 0 − 2 Q r ′ ​ ( j) 0). DX(j,\pm 1)=\left(\begin{array}[]{cc}0&-2\\ Q_{r}^{\prime}(j)&0\end{array}\right). |  |

Hence,

(7) |  | det D ​ X ​ ( j, ± 1) = 2 ​ Q r ′ ​ ( j) = 2 ​ ( − 1) r − j ​ ∏ k = − r k ≠ j r | j − k |. \det DX(j,\pm 1)=2Q_{r}^{\prime}(j)=2(-1)^{r-j}\prod_{\begin{subarray}{c}k=-r\\ k\neq j\end{subarray}}^{r}|j-k|. |  |

Since X r X_{r} is Hamiltonian, it follows from ( 7) that ( j, ± 1) (j,\pm 1) is either a hyperbolic saddle or a center, with the later occurring if, and only if, det D ​ X ​ ( j, ± 1) > 0 \det DX(j,\pm 1)>0. Thus, we get from ( 7) that ( j, ± 1) (j,\pm 1) is a center if, and only if, j ≡ r mod 2 j\equiv r\mod 2. Therefore, either with r r even or odd, it is easy to see that we have exactly r + 1 r+1 centers in each of the lines y = ± 1 y=\pm 1. The study of the critical points on the line y = 0 y=0 is similar.∎

###### Proposition 1.

Given r ∈ ℤ ⩾ 0 r\in\mathbb{Z}_{\geqslant 0}, let P ⁡ ( y) P(y) and Q r ​ ( x) Q_{r}(x) be given by ( 6). Then given n ⩾ 1 n\geqslant 1, there is a polynomial R n: ℝ 2 → ℝ R_{n}\colon\mathbb{R}^{2}\to\mathbb{R} with n + 1 n+1 monomials and ε 0 > 0 \varepsilon_{0}>0 such that the perturbed system X n, r = ( P n, Q r) X_{n,r}=(P_{n},Q_{r}) given by

 | P n ​ ( x, y) = P ⁡ ( y) + ε ​ R n ​ ( x, y), Q r ​ ( x, y) = Q r ​ ( x), P_{n}(x,y)=P(y)+\varepsilon R_{n}(x,y),\quad Q_{r}(x,y)=Q_{r}(x), |  |

has at least

 | 2 ​ n ​ ( r + 1) + n ⁡ ( 1 + ( − 1) r) 2n(r+1)+n\big(1+(-1)^{r}\big) |  |

limit cycles, for 0 < | ε | < ε 0 0<|\varepsilon|<\varepsilon_{0}. In particular, X n, r X_{n,r} has n + r + 4 n+r+4 monomials.

###### Proof.

Let p k = ( x k, − 1) p_{k}=(x_{k},-1), k ∈ { 1, …, r + 1 } k\in\{1,\dots,r+1\}, and p k = ( x k, 1) p_{k}=(x_{k},1), k ∈ { r + 2, …, 2 ​ r + 2 } k\in\{r+2,\dots,2r+2\}, be the centers of X r X_{r} such that x i < x j x_{i}<x_{j} for i < j ⩽ r + 1 i<j\leqslant r+1 and x i > x j x_{i}>x_{j} for i > j ⩾ r + 2 i>j\geqslant r+2. See Figure 3.

\begin{overpic}[Fig7.eps] \put(99.0,40.5){$x$} \put(49.0,79.0){$y$} \put(99.0,61.5){$y=a_{1}$} \put(99.0,16.0){$y=-a_{1}$} \par\put(14.0,25.0){$p_{1}$} \put(-1.0,27.0){$\gamma_{0}^{1}$} \put(2.0,33.5){$\gamma_{1}^{1}$} \par\put(48.5,23.0){$p_{2}$} \put(31.0,27.0){$\gamma_{0}^{2}$} \put(33.5,33.5){$\gamma_{1}^{2}$} \par\put(78.0,25.0){$p_{3}$} \put(64.0,27.0){$\gamma_{0}^{3}$} \put(66.5,33.5){$\gamma_{1}^{3}$} \par\put(78.0,52.5){$p_{4}$} \put(92.0,50.5){$\gamma_{0}^{4}$} \put(89.5,44.0){$\gamma_{1}^{4}$} \par\put(48.5,55.0){$p_{5}$} \put(60.0,50.5){$\gamma_{0}^{5}$} \put(58.0,44.0){$\gamma_{1}^{5}$} \par\put(14.0,52.5){$p_{6}$} \put(28.0,50.5){$\gamma_{0}^{6}$} \put(25.0,44.0){$\gamma_{1}^{6}$} \end{overpic} Figure 3. Illustration of p k p_{k} and γ i k \gamma_{i}^{k}, for r = 2 r=2 and n = 1 n=1.

Let A k A_{k} be the period annulus associated to p k p_{k} and let γ 0 k, γ 1 k, …, γ n k \gamma_{0}^{k},\gamma_{1}^{k},\dots,\gamma_{n}^{k} be fixed periodic orbits in A k A_{k}, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}, such that γ i − 1 k ⊂ Γ i k \gamma_{i-1}^{k}\subset\Gamma_{i}^{k}, where Γ i k \Gamma_{i}^{k} is the open interior region bounded by γ i k \gamma_{i}^{k}, i ∈ { 1, …, n } i\in\{1,\dots,n\}. See Figure 3. Observe that each γ i k \gamma_{i}^{k} is positively oriented, i ∈ { 0, …, n } i\in\{0,\dots,n\}, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Let

 | α i k = sup { | y |: ( x, y) ∈ Γ i k }, \alpha_{i}^{k}=\sup\{|y|\colon(x,y)\in\Gamma_{i}^{k}\}, |  |

i ∈ { 0, …, n } i\in\{0,\dots,n\}, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Observe that α n k > ⋯ > α 0 k > 0 \alpha_{n}^{k}>\dots>\alpha_{0}^{k}>0, for each k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Observe also that we can choose γ 0 k, γ 1 k, …, γ n k \gamma_{0}^{k},\gamma_{1}^{k},\dots,\gamma_{n}^{k} such that for each i ∈ { 1, …, n } i\in\{1,\dots,n\} there is a i > 0 a_{i}>0 satisfying α i − 1 k < a i < α i k \alpha_{i-1}^{k}<a_{i}<\alpha_{i}^{k}, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. See Figure 3. Given a polynomial R: ℝ 2 → ℝ R\colon\mathbb{R}^{2}\to\mathbb{R} and a periodic orbit γ \gamma of X r X_{r}, set

 | I ⁡ ( R, γ) = ∬ Γ ∂ R ∂ x ​ ( x, y) ​ 𝑑 x ​ 𝑑 y, I(R,\gamma)=\iint_{\Gamma}\frac{\partial R}{\partial x}(x,y)\;dxdy, |  |

where Γ \Gamma is the interior region bounded by γ \gamma. It follows from Remark 1 that if γ \gamma is positively oriented, then I ⁡ ( R, γ) I(R,\gamma) is the Abelian integral of the perturbed vector field

 | P n ​ ( x, y) = P ⁡ ( y) + ε ​ R ​ ( x, y), Q r ​ ( x, y) = Q r ​ ( x), P_{n}(x,y)=P(y)+\varepsilon R(x,y),\quad Q_{r}(x,y)=Q_{r}(x), |  |

associated to γ \gamma. Let R 0 ​ ( x) = x 2 ​ n + 1 R_{0}(x)=x^{2n+1} and observe that I ⁡ ( R 0, γ i k) > 0 I(R_{0},\gamma_{i}^{k})>0 for every i ∈ { 0, …, n } i\in\{0,\dots,n\} and k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Given m 1 ⩾ 1 m_{1}\geqslant 1 let,

 | R 1 ​ ( x, y) = R 1 ​ ( x, y, m 1) = x 2 ​ n + 1 − x 2 ​ n − 1 ​ ( y a 1) 2 ​ m 1. R_{1}(x,y)=R_{1}(x,y;m_{1})=x^{2n+1}-x^{2n-1}\left(\frac{y}{a_{1}}\right)^{2m_{1}}. |  |

We claim that there is m 1 ⩾ 1 m_{1}\geqslant 1 big enough such that I ⁡ ( R 1, γ 0 k) > 0 I(R_{1},\gamma_{0}^{k})>0 and I ⁡ ( R 1, γ 1 k) < 0 I(R_{1},\gamma_{1}^{k})<0, for every k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Indeed, first observe that if y ∈ ℝ y\in\mathbb{R} is such that | y | < a 1 |y|<a_{1}, then

(8) |  | lim m 1 → ∞ ( y a 1) 2 ​ m 1 = 0. \lim\limits_{m_{1}\to\infty}\left(\frac{y}{a_{1}}\right)^{2m_{1}}=0. |  |

Hence, it follows from ( 8), from the compactness of Γ 0 k ¯ \overline{\Gamma_{0}^{k}} (i.e. the topological closure of Γ 0 k \Gamma_{0}^{k}) and from the fact that α 0 k < a 1 \alpha_{0}^{k}<a_{1} that

(9) |  | lim m 1 → ∞ x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 = 0, \lim\limits_{m_{1}\to\infty}x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}=0, |  |

uniformly in ( x, y) ∈ Γ 0 k (x,y)\in\Gamma_{0}^{k}, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Thus we have,

 | lim m 1 → ∞ I ⁡ ( R 1, γ 0 k) = lim m 1 → ∞ ∬ Γ 0 k ( 2 ​ n + 1) ​ x 2 ​ n − ( 2 ​ n − 1) ​ x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 ​ 𝑑 x ​ 𝑑 y = I ⁡ ( R 0, γ 0 k) − lim m 1 → ∞ ∬ Γ 0 k ( 2 ​ n − 1) ​ x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 ​ 𝑑 x ​ 𝑑 y = I ⁡ ( R 0, γ 0 k) > 0, \begin{array}[]{rl}\displaystyle\lim\limits_{m_{1}\to\infty}I(R_{1},\gamma_{0}^{k})&\displaystyle=\lim\limits_{m_{1}\to\infty}\iint_{\Gamma_{0}^{k}}(2n+1)x^{2n}-(2n-1)x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}\;dxdy\\ &\displaystyle=I(R_{0},\gamma_{0}^{k})-\lim\limits_{m_{1}\to\infty}\iint_{\Gamma_{0}^{k}}(2n-1)x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}\;dxdy\\ &\displaystyle=I(R_{0},\gamma_{0}^{k})>0,\end{array} |  |

for k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}, with the last equality following from ( 9). Let

 | Ω i k = { ( x, y) ∈ Γ i: | y | > a i }, \Omega_{i}^{k}=\{(x,y)\in\Gamma_{i}\colon|y|>a_{i}\}, |  |

and observe that Ω i k \Omega_{i}^{k} has positive Lebesgue measure, i ∈ { 1, …, n } i\in\{1,\dots,n\}. See the gray-shaded area in Figure 3. Hence, it follows that

 | lim m 1 → ∞ ∬ Γ 1 k x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 ​ 𝑑 x ​ 𝑑 y ⩾ lim m 1 → ∞ ∬ Ω 1 k x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 ​ 𝑑 x ​ 𝑑 y = + ∞. \lim\limits_{m_{1}\to\infty}\iint_{\Gamma_{1}^{k}}x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}\;dxdy\geqslant\lim\limits_{m_{1}\to\infty}\iint_{\Omega_{1}^{k}}x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}\;dxdy=+\infty. |  |

Therefore,

 | lim m 1 → ∞ I ⁡ ( R 1, γ 1 k) = lim m 1 → ∞ ∬ Γ 1 k ( 2 ​ n + 1) ​ x 2 ​ n − ( 2 ​ n − 1) ​ x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 ​ 𝑑 x ​ 𝑑 y ⩽ I ⁡ ( R 0, γ 1 k) − lim m 1 → ∞ ∬ Ω 1 k ( 2 ​ n − 1) ​ x 2 ​ n − 2 ​ ( y a 1) 2 ​ m 1 ​ 𝑑 x ​ 𝑑 y = − ∞. \begin{array}[]{rl}\displaystyle\lim\limits_{m_{1}\to\infty}I(R_{1},\gamma_{1}^{k})&\displaystyle=\lim\limits_{m_{1}\to\infty}\iint_{\Gamma_{1}^{k}}(2n+1)x^{2n}-(2n-1)x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}\;dxdy\\ &\displaystyle\leqslant I(R_{0},\gamma_{1}^{k})-\lim\limits_{m_{1}\to\infty}\iint_{\Omega_{1}^{k}}(2n-1)x^{2n-2}\left(\frac{y}{a_{1}}\right)^{2m_{1}}\;dxdy\\ &\displaystyle=-\infty.\end{array} |  |

This proves the claim. That is, there is m 1 ⩾ 1 m_{1}\geqslant 1 big enough such that

(10) |  | I ⁡ ( R 1, γ 0 k) > 0, I ⁡ ( R 1, γ 1 k) < 0, I(R_{1},\gamma_{0}^{k})>0,\quad I(R_{1},\gamma_{1}^{k})<0, |  |

for every k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. From now on, we fix m 1 ∈ ℕ m_{1}\in\mathbb{N} big enough such that ( 10) is satisfied. It follows from the proof of Lemma 1 that if r r is even, then

 | p k 1 = p r / 2 + 1, p k 2 = p 3 ​ r / 2 + 2 p_{k_{1}}=p_{r/2+1},\quad p_{k_{2}}=p_{{3r}/{2}+2} |  |

lie on the line x = 0 x=0. See Figure 3. We claim that we can choose γ − 1 k j ⊂ Γ 0 k j \gamma_{-1}^{k_{j}}\subset\Gamma_{0}^{k_{j}} such that I ⁡ ( R 1, γ − 1 k j) < 0 I(R_{1},\gamma_{-1}^{k_{j}})<0, j ∈ { 1, 2 } j\in\{1,2\}. Indeed, let

(11) |  | b 0 k j = inf { | y |: ( x, y) ∈ Γ 0 k j }, b_{0}^{k_{j}}=\inf\{|y|\colon(x,y)\in\Gamma_{0}^{k_{j}}\}, |  |

and observe that b 0 k j > 0 b_{0}^{k_{j}}>0, j ∈ { 1, 2 } j\in\{1,2\}. Observe also that

(12) |  | ∂ R 1 ∂ x ​ ( x, y) < 0 ⇔ x 2 < 2 ​ n − 1 2 ​ n + 1 ​ ( y a 1) 2 ​ m 1. \frac{\partial R_{1}}{\partial x}(x,y)<0\Leftrightarrow x^{2}<\frac{2n-1}{2n+1}\left(\frac{y}{a_{1}}\right)^{2m_{1}}. |  |

Let γ − 1 k j ⊂ Γ 0 k j \gamma_{-1}^{k_{j}}\subset\Gamma_{0}^{k_{j}} be of small enough amplitude such that

(13) |  | ( x, y) ∈ Γ − 1 k j ⇒ x 2 < 2 ​ n − 1 2 ​ n + 1 ​ ( b 0 k j a 1) 2 ​ m 1, (x,y)\in\Gamma_{-1}^{k_{j}}\Rightarrow x^{2}<\frac{2n-1}{2n+1}\left(\frac{b_{0}^{k_{j}}}{a_{1}}\right)^{2m_{1}}, |  |

where Γ − 1 k j \Gamma_{-1}^{k_{j}} is the interior region bounded by γ − 1 k j \gamma_{-1}^{k_{j}}, j ∈ { 1, 2 } j\in\{1,2\}. Observe that it is possible to choose γ − 1 k j \gamma_{-1}^{k_{j}} precisely because p k j p_{k_{j}} lies in the line x = 0 x=0 and it is not the origin, j ∈ { 1, 2 } j\in\{1,2\}. Hence, it follows from ( 11), ( 12) and ( 13) that

 | ∂ R 1 ∂ x ​ ( x, y) | Γ − 1 k j < 0, \left.\frac{\partial R_{1}}{\partial x}(x,y)\right|_{\Gamma_{-1}^{k_{j}}}<0, |  |

and thus we have I ⁡ ( R 1, γ − 1 k j) < 0 I(R_{1},\gamma_{-1}^{k_{j}})<0, j ∈ { 1, 2 } j\in\{1,2\}. This proves the claim. Therefore, it follows that if | ε | > 0 |\varepsilon|>0 is small enough, then the perturbed vector field X 1, r = ( P 1, Q r) X_{1,r}=(P_{1},Q_{r}) given by

 | P 1 ​ ( x, y) = P ⁡ ( y) + ε ​ R 1 ​ ( x, y), Q r ​ ( x, y) = Q r ​ ( x), P_{1}(x,y)=P(y)+\varepsilon R_{1}(x,y),\quad Q_{r}(x,y)=Q_{r}(x), |  |

has r + 5 r+5 monomials and at least 2 ​ ( r + 1) + 1 + ( − 1) r 2(r+1)+1+(-1)^{r} limit cycles, being 2 ​ ( r + 1) 2(r+1) of them bifurcating between the orbits γ 0 k \gamma_{0}^{k} and γ 1 k \gamma_{1}^{k}, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\} and the other (possibly) two between γ 0 k j \gamma_{0}^{k_{j}} and γ − 1 k j \gamma_{-1}^{k_{j}}, j ∈ { 1, 2 } j\in\{1,2\}, when r r is even. Similarly, we can continue this process and obtain moreover another family of 2 ​ ( r + 1) + 1 + ( − 1) r 2(r+1)+1+(-1)^{r} cycles by considering,

 | R 2 ​ ( x, y) = R 2 ​ ( x, y, m 1, m 2) = x 2 ​ n + 1 − x 2 ​ n − 1 ​ ( y a 1) 2 ​ m 1 + x 2 ​ n − 3 ​ ( y a 2) 2 ​ m 2. R_{2}(x,y)=R_{2}(x,y;m_{1},m_{2})=x^{2n+1}-x^{2n-1}\left(\frac{y}{a_{1}}\right)^{2m_{1}}+x^{2n-3}\left(\frac{y}{a_{2}}\right)^{2m_{2}}. |  |

Then, for this vector field we have obtained 4 ​ ( r + 1) + 2 ​ ( 1 + ( − 1) r) 4(r+1)+2(1+(-1)^{r}) limit cycles. More precisely, once obtained R 1 R_{1}, we can take m 2 > m 1 m_{2}>m_{1} big enough such that none of the previous Abelian integrals changes sign at the same time that I ⁡ ( R 2, γ 2 k) > 0 I(R_{2},\gamma_{2}^{k})>0, k ∈ { 1, …, 2 ​ r + 2 } k\in\{1,\dots,2r+2\}. Then, if r r is even, we can choose γ − 2 k j ⊂ Γ − 1 k j \gamma_{-2}^{k_{j}}\subset\Gamma_{-1}^{k_{j}} small enough such that I ⁡ ( R 2, γ − 2 k j) > 0 I(R_{2},\gamma_{-2}^{k_{j}})>0, j ∈ { 1, 2 } j\in\{1,2\}.

Continuing this process, we obtain a perturbation of the form

 | R n ​ ( x, y) = ∑ k = 0 n ( − 1) k ​ x 2 ​ ( n − k) + 1 ​ ( y a k) 2 ​ m k, R_{n}(x,y)=\sum_{k=0}^{n}(-1)^{k}x^{2(n-k)+1}\left(\frac{y}{a_{k}}\right)^{2m_{k}}, |  |

with a 0 = 1 a_{0}=1, m 0 = 0 m_{0}=0 and m k ≫ m k − 1 m_{k}\gg m_{k-1}, k ∈ { 1, …, n } k\in\{1,\dots,n\}, such that the perturbed vector field X n, r = ( P n, Q r) X_{n,r}=(P_{n},Q_{r}) given by

 | P n ​ ( x, y) = P ⁡ ( y) + ε ​ R n ​ ( x, y), Q r ​ ( x, y) = Q r ​ ( x), P_{n}(x,y)=P(y)+\varepsilon R_{n}(x,y),\quad Q_{r}(x,y)=Q_{r}(x), |  |

has n + r + 4 n+r+4 monomials and at least 2 ​ n ​ ( r + 1) + n ⁡ ( 1 + ( − 1) r) 2n(r+1)+n\big(1+(-1)^{r}\big) limit cycles, for | ε | > 0 |\varepsilon|>0 small enough. ∎

###### Proof of Theorem 1.

It follows from Proposition 1 that we have a two-parameter family of planar polynomial vector fields X n, r X_{n,r}, with r ⩾ 0 r\geqslant 0 and n ⩾ 1 n\geqslant 1, such that

(14) |  | ℋ M ​ ( n + r + 4) ⩾ 2 ​ n ​ ( r + 1) + n ⁡ ( 1 + ( − 1) r) ⩾ 2 ​ n ​ ( r + 1). \mathcal{H}^{M}(n+r+4)\geqslant 2n(r+1)+n\big(1+(-1)^{r}\big)\geqslant 2n(r+1). |  |

If we replace m = n + r + 4 m=n+r+4 at ( 14) we obtain,

(15) |  | ℋ M ​ ( m) ⩾ 2 ​ ( m − r − 4) ​ ( r + 1). \mathcal{H}^{M}(m)\geqslant 2(m-r-4)(r+1). |  |

In order to maximize the leading coefficient of the right-hand side of ( 15), and knowing that r r must be an integer, we take

(16) |  | r = 1 2 ​ m + ( − 1) m − 1 4. r=\frac{1}{2}m+\frac{(-1)^{m}-1}{4}. |  |

Replacing ( 16) at ( 15) we obtain,

(17) |  | ℋ M ​ ( m) ⩾ 1 2 ​ m 2 − 3 ​ m − 8 + 9 4 ​ ( 1 − ( − 1) m) ⩾ 1 2 ​ m 2 − 3 ​ m − 8. \mathcal{H}^{M}(m)\geqslant\frac{1}{2}m^{2}-3m-8+\frac{9}{4}(1-(-1)^{m})\geqslant\frac{1}{2}m^{2}-3m-8. |  |

This finishes the proof.∎

###### Proof of Theorem 2.

Let X n, r X_{n,r} be given by Proposition 1. We recall that X n, r X_{n,r} has n + r + 4 n+r+4 monomials and at least 2 ​ n ​ ( r + 1) + n ⁡ ( 1 + ( − 1) r) 2n(r+1)+n\big(1+(-1)^{r}\big) limit cycles, for | ε | > 0 |\varepsilon|>0 small. If we take r = 2 r=2 and n = 3 n=3 (resp. n = 4 n=4) we obtain ℋ M ​ ( 9) ⩾ 24 \mathcal{H}^{M}(9)\geqslant 24 (resp. ℋ M ​ ( 10) ⩾ 32 \mathcal{H}^{M}(10)\geqslant 32).

We now focus on the claim that ℋ M ​ ( m) ⩾ 12 \mathcal{H}^{M}(m)\geqslant 12 for m ∈ { 4, 5, 6 } m\in\{4,5,6\}. Consider the analytic system defined on the open first quadrant of ℝ 2 \mathbb{R}^{2} and given by

(18) |  | x ˙ = α 1 ​ x g 11 ​ y g 12 − β 1 ​ x h 11 ​ y h 12, y ˙ = α 2 ​ x g 21 ​ y g 22 − β 2 ​ x h 21 ​ y h 22, \dot{x}=\alpha_{1}x^{g_{11}}y^{g_{12}}-\beta_{1}x^{h_{11}}y^{h_{12}},\quad\dot{y}=\alpha_{2}x^{g_{21}}y^{g_{22}}-\beta_{2}x^{h_{21}}y^{h_{22}}, |  |

with α i \alpha_{i}, β i \beta_{i}, g i ​ j g_{ij}, h i ​ j ∈ ℝ h_{ij}\in\mathbb{R}. It follows from Boros and Hofbauer [5, Section 7 7] that for some choice of the parameters and exponents, system ( 18) has at least three limit cycles of odd multiplicity. In particular, such limit cycles persist under small perturbations. Therefore, we can take a rational approximation of such exponents and thus suppose that system ( 18) can be written as

(19) |  | x ˙ = α 1 ​ x a 1 b 1 ​ y c 1 d 1 − β 1 ​ x a 2 b 2 ​ y c 2 d 2, y ˙ = α 2 ​ x a 3 b 3 ​ y c 3 d 3 − β 2 ​ x a 4 b 4 ​ y c 4 d 4, \dot{x}=\alpha_{1}x^{\frac{a_{1}}{b_{1}}}y^{\frac{c_{1}}{d_{1}}}-\beta_{1}x^{\frac{a_{2}}{b_{2}}}y^{\frac{c_{2}}{d_{2}}},\quad\dot{y}=\alpha_{2}x^{\frac{a_{3}}{b_{3}}}y^{\frac{c_{3}}{d_{3}}}-\beta_{2}x^{\frac{a_{4}}{b_{4}}}y^{\frac{c_{4}}{d_{4}}}, |  |

with a i a_{i}, c i ∈ ℤ c_{i}\in\mathbb{Z} and b i b_{i}, d i ∈ ℤ > 0 d_{i}\in\mathbb{Z}_{>0} relatively primes and has yet at least three limit cycles of odd multiplicity. Let b = 2 ​ b 1 ​ b 2 ​ b 3 ​ b 4 b=2b_{1}b_{2}b_{3}b_{4}, d = 2 ​ d 1 ​ d 2 ​ d 3 ​ d 4 d=2d_{1}d_{2}d_{3}d_{4} and observe that b ⩾ 2 b\geqslant 2 and d ⩾ 2 d\geqslant 2 are even natural numbers. Applying the non-reversible transformation ( x, y) = ( u b, v d) (x,y)=(u^{b},v^{d}) we obtain a new vector field given by

 | u ˙ = 1 b ​ u b − 1 ​ ( α 1 ​ u 2 ​ a 1 ​ b 2 ​ b 3 ​ b 4 ​ v 2 ​ c 1 ​ d 2 ​ d 3 ​ d 4 − β 1 ​ u 2 ​ b 1 ​ a 2 ​ b 3 ​ b 4 ​ v 2 ​ d 1 ​ c 2 ​ d 3 ​ d 4), v ˙ = 1 d ​ v d − 1 ​ ( α 2 ​ u 2 ​ b 1 ​ b 2 ​ a 3 ​ b 4 ​ v 2 ​ d 1 ​ d 2 ​ c 3 ​ d 4 − β 2 ​ u 2 ​ b 1 ​ b 2 ​ b 3 ​ a 4 ​ v 2 ​ d 1 ​ d 2 ​ d 3 ​ c 4). \begin{array}[]{l}\displaystyle\dot{u}=\frac{1}{bu^{b-1}}\left(\alpha_{1}u^{2a_{1}b_{2}b_{3}b_{4}}v^{2c_{1}d_{2}d_{3}d_{4}}-\beta_{1}u^{2b_{1}a_{2}b_{3}b_{4}}v^{2d_{1}c_{2}d_{3}d_{4}}\right),\\ \displaystyle\dot{v}=\frac{1}{dv^{d-1}}\left(\alpha_{2}u^{2b_{1}b_{2}a_{3}b_{4}}v^{2d_{1}d_{2}c_{3}d_{4}}-\beta_{2}u^{2b_{1}b_{2}b_{3}a_{4}}v^{2d_{1}d_{2}d_{3}c_{4}}\right).\end{array} |  |

By using the rescaling of time d ​ t / d ​ τ = b ​ d ​ u b − 1 + 2 ​ k ​ v d − 1 + 2 ​ k dt/d\tau=bdu^{b-1+2k}v^{d-1+2k}, with k ∈ ℤ > 0 k\in\mathbb{Z}_{>0}, we obtain

(20) |  | u ˙ = d ​ v d − 1 ​ ( α 1 ​ u 2 ​ ( a 1 ​ b 2 ​ b 3 ​ b 4 + k) ​ v 2 ​ ( c 1 ​ d 2 ​ d 3 ​ d 4 + k) − β 1 ​ u 2 ​ ( b 1 ​ a 2 ​ b 3 ​ b 4 + k) ​ v 2 ​ ( d 1 ​ c 2 ​ d 3 ​ d 4 + k)), v ˙ = b ​ u b − 1 ​ ( α 2 ​ u 2 ​ ( b 1 ​ b 2 ​ a 3 ​ b 4 + k) ​ v 2 ​ ( d 1 ​ d 2 ​ c 3 ​ d 4 + k) − β 2 ​ u 2 ​ ( b 1 ​ b 2 ​ b 3 ​ a 4 + k) ​ v 2 ​ ( d 1 ​ d 2 ​ d 3 ​ c 4 + k)). \begin{array}[]{l}\displaystyle\dot{u}=dv^{d-1}\left(\alpha_{1}u^{2(a_{1}b_{2}b_{3}b_{4}+k)}v^{2(c_{1}d_{2}d_{3}d_{4}+k)}-\beta_{1}u^{2(b_{1}a_{2}b_{3}b_{4}+k)}v^{2(d_{1}c_{2}d_{3}d_{4}+k)}\right),\\ \displaystyle\dot{v}=bu^{b-1}\left(\alpha_{2}u^{2(b_{1}b_{2}a_{3}b_{4}+k)}v^{2(d_{1}d_{2}c_{3}d_{4}+k)}-\beta_{2}u^{2(b_{1}b_{2}b_{3}a_{4}+k)}v^{2(d_{1}d_{2}d_{3}c_{4}+k)}\right).\end{array} |  |

Observe that ( 20) is polynomial for k ∈ ℤ > 0 k\in\mathbb{Z}_{>0} big enough. Moreover, since b ⩾ 2 b\geqslant 2 and d ⩾ 2 d\geqslant 2 are even numbers, it follows that ( 20) is reversible in relation to the lines u = 0 u=0 and v = 0 v=0. Hence, ( 20) has diffeomorphic copies of ( 19) at each open quadrant and thus we obtain ℋ M ​ ( 4) ⩾ 12 \mathcal{H}^{M}(4)\geqslant 12. Since each of these limit cycles has odd multiplicity, it follows that they persist under small perturbations and thus we also have ℋ M ​ ( m) ⩾ 12 \mathcal{H}^{M}(m)\geqslant 12 for m ∈ { 5, 6 } m\in\{5,6\}.

Finally, we now prove that ℋ M ​ ( 8) ⩾ 20 \mathcal{H}^{M}(8)\geqslant 20 and ℋ M ​ ( 7) ⩾ 16 \mathcal{H}^{M}(7)\geqslant 16. The proof will follow by studying the cyclicity of some weak foci. For a general theory of cyclicity of limit sets, we refer to Roussarie [36, Chapter 2 2]. For more details about the cyclicity of weak focus in polynomial vector fields, we refer to Christopher et al [13, Chapter 1 1]. For a more computational approach, we refer to Romanovski and Shafer [34, Chapter 6 6].

Consider the system with eight monomials

(21) |  | x ˙ = a 5 ​ y 6 + a 4 ​ y 5 + a 3 ​ y 4 + a 2 ​ y 3 + a 1 ​ x ​ y 2 − a, y ˙ = x ​ y − 1, \dot{x}=a_{5}y^{6}+a_{4}y^{5}+a_{3}y^{4}+a_{2}y^{3}+a_{1}xy^{2}-a,\quad\dot{y}=xy-1, |  |

where a = a 1 + ⋯ + a 5 a=a_{1}+\dots+a_{5}. It is not hard to see that if a j = a j ∗ a_{j}=a_{j}^{*}, j = 1, …, 5 j=1,\dots,5, where

 | a 1 ∗ = − 1, a 2 ∗ = − 161 17, a 3 ∗ = 17 11, a 4 ∗ = − 6 11, a 5 ∗ = 7 99, a_{1}^{*}=-1,\quad a_{2}^{*}=-\frac{161}{17},\quad a_{3}^{*}=\frac{17}{11},\quad a_{4}^{*}=-\frac{6}{11},\quad a_{5}^{*}=\frac{7}{99}, |  |

then the point p = ( 1, 1) p=(1,1) is a weak focus of order five, i.e. it is not hyperbolic, L 1 = ⋯ = L 4 = 0 L_{1}=\dots=L_{4}=0 and L 5 ≠ 0 L_{5}\neq 0, where L j L_{j} is its j j th *Lyapunov constant*(see Adronov et al. [3, p. 254]). Moreover, if we calculate the Jacobian matrix of L 1, L 2, L 3, L 4 L_{1},L_{2},L_{3},L_{4} in relation to a 2, a 3, a 4, a 5 a_{2},a_{3},a_{4},a_{5}, at a j = a j ∗ a_{j}=a_{j}^{*}, j = 2, 3, 4, 5 j=2,3,4,5, it can be seen that

 | det ∂ ( L 1, L 2, L 3, L 4) ∂ ( a 2, a 3, a 4, a 5) ​ ( a 2 ∗, a 3 ∗, a 4 ∗, a 5 ∗) ≠ 0. \det\frac{\partial(L_{1},L_{2},L_{3},L_{4})}{\partial(a_{2},a_{3},a_{4},a_{5})}(a_{2}^{*},a_{3}^{*},a_{4}^{*},a_{5}^{*})\neq 0. |  |

Hence, it follows from Christopher et al [13, Theorem 1.5 1.5] that we can choose a j ≈ a j ∗ a_{j}\approx a_{j}^{*}, j ∈ { 2, 3, 4, 5 } j\in\{2,3,4,5\}, such that four limit cycles bifurcate from p p. Now we move a 1 a_{1} to perturb the trace of ( 21) at p p and thus to bifurcate a fifth limit cycle (see Romanovski and Shafer [34, Theorem 6.2.7 6.2.7]). Therefore, for some specific values of the parameters, system ( 21) has at least five limit cycles near the point p = ( 1, 1) p=(1,1) and surrounding it. Thus, similarly to the previous argumentation, we now use the non-invertible change of variables ( x, y) = ( u 2, v 2) (x,y)=(u^{2},v^{2}), followed by the rescaling of time d ​ t / d ​ τ = 2 ​ u ​ v dt/d\tau=2uv, obtaining the new system

(22) |  | u ˙ = a 5 ​ v 13 + a 4 ​ v 11 + a 3 ​ v 9 + a 2 ​ v 7 + a 1 ​ u 2 ​ v 5 − a ​ v, v ˙ = u 3 ​ v 2 − u. \dot{u}=a_{5}v^{13}+a_{4}v^{11}+a_{3}v^{9}+a_{2}v^{7}+a_{1}u^{2}v^{5}-av,\quad\dot{v}=u^{3}v^{2}-u. |  |

It has again eight monomials and moreover it has a diffeomorphic copy, in each open quadrant, of the first open quadrant of ( 21). In particular, it has 20 20 limit cycles for some values of the coefficients and thus ℋ M ​ ( 8) ⩾ 20 \mathcal{H}^{M}(8)\geqslant 20. To prove ℋ M ​ ( 7) ⩾ 16 \mathcal{H}^{M}(7)\geqslant 16, we substitute a 5 = 0 a_{5}=0 in ( 21), obtaining a system with seven mononials. In this system, if a j = a j ¯ a_{j}=\overline{a_{j}}, j = 1, …, 4 j=1,\ldots,4, where

 | a 1 ¯ = − 1, a 2 ¯ = − 42 109, a 3 ¯ = 31 109, a 4 ¯ = − 6 109, \overline{a_{1}}=-1,\quad\overline{a_{2}}=-\frac{42}{109},\quad\overline{a_{3}}=\frac{31}{109},\quad\overline{a_{4}}=-\frac{6}{109}, |  |

then p = ( 1, 1) p=(1,1) is a weak focus of order four and the proof follows similarly.

For each k = 1, 2, 3 k=1,2,3 by taking a 5 = a 4 =.. = a k + 1 = 0 a_{5}=a_{4}=..=a_{k+1}=0 and suitable a 1, …, a k a_{1},\ldots,a_{k} in ( 22) we obtain a vector field with k + 3 k+3 monomials and at least 4 ​ k 4k limit cycles, with k k of them included in each quadrant. These results give less limit cycles that the examples constructed from the Boros and coauthor’s result when m = 4, 5 m=4,5 and by taking k = 3 k=3 gives a different proof that ℋ M ​ ( 6) ≥ 12, \mathcal{H}^{M}(6)\geq 12, with the advantage that this new example is explicit. ∎

## 4. Further Thoughts

Regarding the recent developments in the field of algebraic geometry described in the introduction, it is worthy to ask for a variant of the Hilbert number as a function of the associated newton polygon of the polynomial vector field. In particular, as a functions of the number of integer points contained in its interior. Notably, in the case of a Hamiltonian vector field X X associated with a polynomial p p, the Newton polygons N ⁡ ( X) N(X) and N ⁡ ( p) N(p) coincide, differing only by a translation in ℤ 2 \mathbb{Z}^{2}. This observation, combined with the discussion made in the introduction, could be used for instance to establish a bound on the number of distinct periodic annuli of X X in terms of the number of integer points in N ⁡ ( X) N(X). We thank very much the anonymous reviewers for pointing out such developments and suggesting this variation of the problem.

## Acknowledgments

We thank to the reviewers their comments and suggestions which help us to improve the presentation of this paper. This work is supported by the Spanish State Research Agency, through the projects PID2022-136613NB-I00 grant and the Severo Ochoa and María de Maeztu Program for Centers and Units of Excellence in R&D (CEX2020-001084-M), grant 2021-SGR-00113 from AGAUR, Generalitat de Catalunya, and by São Paulo Research Foundation (FAPESP), grants 2019/10269-3, 2021/01799-9 and 2022/14353-1.

## References

- [1] M. J. Álvarez, B. Coll, P. De Maesschalck and R. Prohens, Asymptotic lower bounds on Hilbert numbers using canard cycles, J. Differ. Equations 268 (2020), 3370–3391.
- [2] M. J. Álvarez, A. Gasull and R. Prohens, Uniqueness of limit cycles for complex differential equations with two monomials, J. Math. Anal. Appl., 518 (2023) 126663.
- [3] A. A. Andronov & others. Theory of Bifurcations of Dynamic Systems on a Plane, Wiley, New York & Toronto, 1973.
- [4] B. Boros, J. Hofbauer, S. Müller and G. Regensburger, Planar S-systems: global stability and the center problem, Discrete Contin. Dyn. Syst. 39, No. 2, 707–727 (2019).
- [5] B. Boros and J. Hofbauer, Planar S-systems: permanence, J. Differ. Equations 266, No. 6, 3787–3817 (2019).
- [6] F. Bréhard, Certified Numerics in Function Spaces: Polynomial Approximations Meet Computer Algebra and Formal Proof, Ph.D. Dissertation. École normale supérieure de Lyon, Université de Lyon, Lyon 2019.
- [7] F. Bréhard, N. Brisebarre, M. Joldes and W. Tucker, Efficient and Validated Numerical Evaluation of Abelian Integrals, ACM Trans. Math. Softw, 50 (2024), 1–38.
- [8] F. E. Browder, Mathematical Developments Arising from Hilbert Problems, Proc. Sympos. Pure Math., volume XXVIII, part I (1976).
- [9] C. A. Buzzi, Y. R. Carvalho and A. Gasull, Limit cycles for some families of smooth and non-smooth planar systems, Nonlinear Anal., Theory Methods Appl., Ser. A, Theory Methods, 207 (2021).
- [10] L. Chen and M. Wang, The relative position, and the number, of limit cycles of a quadratic differential system, Acta Math. Sinica (Chin. Ser.) 22 (1979), 751–758.
- [11] S. Chow, C. Li and D. Wang, Normal Forms and Bifurcation of Planar Vector Fields, Cambridge University Press, 1994.
- [12] C. Christopher and N. G. Lloyd, Polynomial Systems: A Lower Bound for the Hilbert Numbers, Proc. R. Soc. Lond., Ser. A, 450 (1995), 219–240.
- [13] C. Christopher, C. Li and J. Torregrosa, Limit Cycles of Differential Equations, Advanced Courses in Mathematics - CRM Barcelona, Birkhäuser Cham, 2024.
- [14] T. M. Dalbelo, R. Oliveira and O. H. Perez, Topological equivalence in the infinity of a planar vector field and its principal part defined through Newton polytope, J. Differ. Equations 408, 230–253 (2024).
- [15] F. Dumortier and C. Li, Perturbations from an Elliptic Hamiltonian of Degree Four: II. Cuspidal Loop, J. Differ. Equations, 175 (2001), 209–243.
- [16] F. Dumortier and C. Li, Perturbations from an Elliptic Hamiltonian of Degree Four: IV. Figure eight-loop, J. Differ. Equations, 188 (2003), 512–554.
- [17] P. Érdi and J. Tóth, Mathematical models of chemical reactions. Theory and applications of deterministic and stochastic models, Nonlinear Anal. Theory and Appl., 259 p. (1989).
- [18] M. Feinberg, Foundations of Chemical Reaction Network Theory, Applied Mathematical Sciences 202. Cham: Springer, 454 p. (2019).
- [19] A. Gasull, Some open problems in low dimensional dynamical systems, SeMA J., 78 (2021), 233–269.
- [20] A. Gasull, C. Li and J. Torregrosa, Limit cycles for 3-monomial differential equations, J. Math. Anal. Appl., 428 (2015), 735–749.
- [21] M. Han and J. Li, Lower bounds for the Hilbert number of polynomial systems, J. Differ. Equations, 252 (2012), 3278–3304.
- [22] A. Harnack, Über Vieltheiligkeit der ebenen algebraischen Curven, Math. Ann. 10, 189-199 (1876).
- [23] I. Itenberg, G. Mikhalkin and E. Shustin, Tropical algebraic geometry, Oberwolfach Seminars 35. Basel: Birkhäuser, 2ed, 104 p. (2009).
- [24] I. Itenberg and E. Shustin, Singular points and limit cycles of planar polynomial vector fields, Duke Math. J. 102, No. 1, 1-37 (2000).
- [25] A. G. Khovanskii, Newton polyhedra and toroidal varieties, Funct. Anal. Appl. 11, 289-296 (1978).
- [26] C. Li, C. Liu and J. Yang, A cubic system with thirteen limit cycles, J. Differ. Equations, 246 (2009), 3609–3619.
- [27] N. G. Lloyd, Limit cycles of polynomial systems-some recent developments, New directions in dynamical systems, London Math. Soc. Lect. Note Ser., 127 (1988), 192–234.
- [28] E. N. Lorenz, Deterministic nonperiodic flow, J. Atmos. Sci., 20 (1963), 130–141.
- [29] G. Mikhalkin, Real algebraic curves, the moment map and amoebas, Ann. Math. (2) 151, No. 1, 309-326 (2000).
- [30] G. Mikhalkin, Amoebas of algebraic varieties and tropical geometry, International Mathematical Series (New York) 3, 257-300 (2004).
- [31] M. Mota and R. Oliveira, Dynamic aspects of Sprott BC chaotic system, Discrete Contin. Dyn. Syst., Ser. B 26 (2021), 1653–1673.
- [32] S. Müller and G. Regensburger, Generalized mass-action systems and positive solutions of polynomial equations with real and symbolic exponents, Computer Algebra in Scientific Computing, 16th international workshop, 302–323 (2014).
- [33] R. Prohens and J. Torregrosa, New lower bounds for the Hilbert numbers using reversible centers, Nonlinearity, 32 (2019), 331–355.
- [34] V. Romanovski and D. Shafer, The Center and Cyclicity Problems, A Computational Algebra Approach, Birkhäuser Boston, MA, Berlim, 2009.
- [35] O. E. Rössler, An equation for continuous chaos, Phys. Lett., 57 (1976), 397–398.
- [36] R. Roussarie, Bifurcations of Planar Vector Fields and Hilbert’s Sixteenth Problem, Modern Birkhäuser Classics, Birkhäuser Basel (2013), reprint of the 1998 edition.
- [37] E. E. Sel’kov, Self-Oscillations in Glycolysis: A Simple Kinetic Model, European J. of Biochemistry, 4 (1968) 79–86.
- [38] S. Smale, Mathematical Problems for the Next Century, Math. Intelligencer (1998), 7–15.
- [39] S. Songling, A concrete example of the existence of four limit cycles for plane quadratic systems, Sci. Sinica, 23 (1980), 153–158.
- [40] J. Sprott, Some simple chaotic flows, Phys. Rev. E, 50 (1994), R647.
- [41] J. Sprott, Simplest dissipative chaotic flow, Phys. Lett., A, 228 (1997), 271–274.
- [42] E. O. Voit, H. A. Martens and S. W. Omholt, 150 years of the mass action law, PLoS Computational Biology 11(1), (2015).


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:armengol.gasull@uab.cat
[4]: mailto:paulo.santana@unesp.br
