<!-- ✗ DEFECTIVE SOURCE FILE — DO NOT USE. This file was downloaded as arXiv:1209.5628 but contains "A Serre derivative for even weight Jacobi forms" (Oberdieck, number theory), NOT Maric-Zivkovic-Vuckovic's "Formalizing Frankl's conjecture: Fc-families" (LNCS 7362, 2012). The run's actual FC-machinery content is carried by Vuckovic-Zivkovic 2017 and Pulaj 2017. See research/summaries/maric-zivkovic-vuckovic-fc-families-2012.md. -->

<!-- source: https://arxiv.org/html/1209.5628 | converted from HTML -->

A Serre derivative for even weight Jacobi forms

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1209.5628v3 [math.NT] 11 Jun 2014

# A Serre derivative for even weight Jacobi forms

Georg Oberdieck

###### Abstract.

Using deformed or twisted Eisenstein Series, we construct a Jacobi-Serre derivative on even-weight Jacobi forms that generalizes the classical Serre derivative on modular forms. As an application, we obtain Ramanujan equations for the index 1 1 Eisenstein series E 4, 1, E 6, 1 E_{4,1},E_{6,1} and a newly defined E 2, 1 E_{2,1}. Finally, we relate the deformed Eisenstein Series directly to the classical first Jacobi theta function.

## 0. Introduction

### 0.1. The Serre derivative

Let τ ∈ ℍ, q = e 2 ​ π ​ i ​ τ \tau\in{\mathbb{H}},q=e^{2\pi i\tau} and let F ⁡ ( τ) ∈ M k F(\tau)\in M_{k} be a modular form of weight k k. The differential F ′:= 1 2 ​ π ​ i ​ ∂ F ∂ τ F^{\prime}:=\frac{1}{2\pi i}\frac{\partial F}{\partial\tau} of F F fails to be modular, but can be completed to a modular form by adding a multiple of the non-modular second Eisenstein series E 2 E_{2}. We obtain a differential operator on modular forms

 | ∂ S: M k ⟶ M k + 2, F ↦ F ′ − k 12 ​ E 2 ​ F, \partial^{S}:M_{k}{\ \longrightarrow\ }M_{k+2},\quad F\mapsto F^{\prime}-\frac{k}{12}E_{2}F, |  |

called the Serre derivative. By the finite dimensionality of the vector space M k M_{k} of modular forms of given weight k k, it is then easy to obtain differential equations among modular forms, e.g. the Ramanujan equations [Ram00] for the Eisenstein series E 4 E_{4} and E 6 E_{6},

(1) |  | ∂ S E 2 + 1 12 E 2 2 = − 1 12 E 4, ∂ S ( E 4) = − 1 3 E 6, and ∂ S ( E 6) = − 1 2 E 4 2. \partial^{S}E_{2}+\frac{1}{12}E_{2}^{2}=-\frac{1}{12}E_{4},\quad\partial^{S}(E_{4})=-\frac{1}{3}E_{6},\quad\text{and}\quad\partial^{S}(E_{6})=-\frac{1}{2}E_{4}^{2}. |  |

### 0.2. Deformed Eisenstein series

Jacobi forms are a natural two-variable generalization of modular forms introduced by Eichler and Zagier in [EZ85]. Let z ∈ ℂ, p = e 2 ​ π ​ i ​ z z\in{\mathbb{C}},p=e^{2\pi iz} and let F ⁡ ( z, τ) F(z,\tau) be a Jacobi form of index m m and weight k k. As in the modular case, the differentials F ′ = 1 2 ​ π ​ i ​ ∂ F ∂ τ F^{\prime}=\frac{1}{2\pi i}\frac{\partial F}{\partial\tau} and F ∙ = 1 2 ​ π ​ i ​ ∂ F ∂ z F^{\bullet}=\frac{1}{2\pi i}\frac{\partial F}{\partial z} are no longer Jacobi forms. The topic of the paper considers the basic question how to complete these differentials (and also higher ones) to honest Jacobi forms.

Let B n B_{n} be the Bernoulli numbers given by x / ( e x − 1) = ∑ n B n ​ x n / n! x/(e^{x}-1)=\sum_{n}B_{n}x^{n}/n!; in particular we have B 1 = − 1 / 2 B_{1}=-1/2. Define the *deformed*or *twisted Eisenstein series*J n ​ ( z, τ) J_{n}(z,\tau) for all n ≥ 0 n\geq 0 by

(2) |  | J n ​ ( z, τ) = δ n, 1 ​ p p − 1 + B n − n ​ ∑ k, r ≥ 1 r n − 1 ​ ( p k + ( − 1) n ​ p − k) ​ q k ​ r. J_{n}(z,\tau)=\delta_{n,1}\frac{p}{p-1}+B_{n}-n\sum_{k,r\geq 1}r^{n-1}(p^{k}+(-1)^{n}p^{-k})q^{kr}. |  |

The name of the J n J_{n} reminds of the fact, that they restrict to the classical Eisenstein series E 2 ​ k E_{2k} at z = 0 z=0,

 | J 2 ​ k ​ ( 0, τ) = B 2 ​ k ​ E 2 ​ k ​ ( τ) and J 2 ​ k + 1 ​ ( 0, τ) = 0. J_{2k}(0,\tau)=B_{2k}E_{2k}(\tau)\quad\quad\text{ and }\quad\quad J_{2k+1}(0,\tau)=0. |  |

Under the elliptic and modular transformations, J n ​ ( z, τ) J_{n}(z,\tau) transforms like a Jacobi form of index 0 0 and weight n n, but adds additional lower order terms. Using these functions, one can complete differentials of Jacobi forms and obtain differential operators on Jacobi forms. This was already observed by Gaberdiel and Keller in [GK09]. As a result, they find a series of differential operators on all Jacobi forms, starting with the classical Heat operator.

Here we use the same principle for the slightly weaker setting of differential operators that are defined only on even-weight Jacobi forms. As a new result, we give a natural and very intersting such operator of degree 2 2.

Let 𝒥 k, m {\mathcal{J}}_{k,m} be the space of Jacobi forms of weight k k and index m m.

###### Theorem 1.

For all k, m ≥ 0 k,m\geq 0, there is a differential operator, called the Jacobi-Serre derivative,

 | ∂ J: 𝒥 2 ​ k, m ⟶ 𝒥 2 ​ k + 2, m, \partial^{J}:{\mathcal{J}}_{2k,m}{\ \longrightarrow\ }{\mathcal{J}}_{2k+2,m}, |  |

such that for every F ⁡ ( z, τ) ∈ 𝒥 2 ​ k, m F(z,\tau)\in{\mathcal{J}}_{2k,m} we have

(3) |  | ( ∂ J F) ​ ( 0, τ) = ∂ S ( F ⁡ ( 0, τ)). (\partial^{J}F)(0,\tau)=\partial^{S}(F(0,\tau)). |  |

∂ J \partial^{J} is given by the formula

 | ∂ J ( F) = F ′ − k 12 ​ E 2 ​ F + 1 1 − 4 ​ m ​ ( F ∙ ⁣ ∙ − J 1 ​ F ∙ + m ​ J 2 ​ F − m 6 ​ E 2 ​ F). \partial^{J}(F)=F^{\prime}-\frac{k}{12}E_{2}F+\frac{1}{1-4m}\Big(F^{\bullet\bullet}-J_{1}F^{\bullet}+mJ_{2}F-\frac{m}{6}E_{2}F\Big). |  |

By equation ( 3), ∂ J \partial^{J} directly generalizes the Serre derivative to Jacobi forms of even weight.

The main application of Theorem 1 and similar constructions for higher differential operators is to find differential equations for Jacobi forms. We examplify this application by stating the index 1 analogs of Ramanujan equation ( 1).

Let

(4) |  | ϕ ⁡ ( z, τ) = ϕ − 2, 1 ​ ( z, τ) = ϕ 10, 1 Δ ⁡ ( τ) \phi(z,\tau)=\phi_{-2,1}(z,\tau)=\frac{\phi_{10,1}}{\Delta(\tau)} |  |

be one of the generators of the algebra of even-weight weak Jacobi forms ( [EZ85], Thm 9.3) and let

 | ℘ ⁡ ( z, τ) = 1 ( 2 ​ π ​ i) 2 ​ ( 1 z 2 + ∑ n ≥ 1 ( 2 ​ n + 1) ​ 2 ​ ζ ​ ( 2 ​ n + 2) ​ E 2 ​ n + 2 ​ z 2 ​ n) \wp(z,\tau)=\frac{1}{(2\pi i)^{2}}\Big(\frac{1}{z^{2}}+\sum_{n\geq 1}(2n+1)2\zeta(2n+2)E_{2n+2}z^{2n}\Big) |  |

be the Weierstrasse ℘ \wp function. We define the analog of E 2 E_{2} for Jacobi forms of index 1 1.

###### Definition 2.

E 2, 1 ​ ( z, τ):= ϕ ⁡ ( z, τ) ​ ( E 2 ​ ( τ) ​ ℘ ​ ( z, τ) − 1 12 ​ E 4). E_{2,1}(z,\tau):=\phi(z,\tau)\Big(E_{2}(\tau)\wp(z,\tau)-\frac{1}{12}E_{4}\Big).

Although E 2, 1 E_{2,1} has several particular properties reminding of E 2 ​ ( τ) E_{2}(\tau), see Lemma 13, the definition is rather ad-hoc and it would be interesting to find a more conceptual approach to E 2, 1 ​ ( z, τ) E_{2,1}(z,\tau). 1 1 1 The function E 2, 1 E_{2,1} introduced by Choie in [Cho97] is different from ours. We state the Ramanujan equation for index 1 1 Jacobi forms.

###### Corollary 3.

Let E 4, 1 E_{4,1} and E 6, 1 E_{6,1} be the Jacobi-Eisenstein series of index 1 1 and weight 4 4 and 6 6 respectively. Then

(5) |  | ∂ J E 2, 1 + 1 12 ​ E 2 ​ E 2, 1 + 1 16 ​ E 4 ′ ​ ϕ − 2, 1 \displaystyle\partial^{J}E_{2,1}+\frac{1}{12}E_{2}E_{2,1}+\frac{1}{16}E_{4}^{\prime}\phi_{-2,1} | = − 1 12 ​ E 4, 1 \displaystyle=-\frac{1}{12}E_{4,1} |  |

 | ∂ J E 4, 1 \displaystyle\partial^{J}E_{4,1} | = − 1 3 ​ E 6, 1 \displaystyle=-\frac{1}{3}E_{6,1} |  |

 | ∂ J E 6, 1 \displaystyle\partial^{J}E_{6,1} | = − 1 2 ​ E 4 ​ E 4, 1. \displaystyle=-\frac{1}{2}E_{4}E_{4,1}. |  |

After restricting ( 5) to z = 0 z=0, we obtain Ramanujans original equations ( 1).

### 0.3. Theta functions

Unrelated to the differential operators above, we derive in the last part of the paper an interesting relation between deformed Eisenstein series and Jacobi theta functions. Let

(6) |  | θ 1 ( z, τ) = − i q 1 / 8 ( p 1 / 2 − p − 1 / 2) ∏ m ≥ 1 ( 1 − q m) ( 1 − p q m) ( 1 − p − 1 q m) \theta_{1}(z,\tau)=-iq^{1/8}(p^{1/2}-p^{-1/2})\prod_{m\geq 1}(1-q^{m})(1-pq^{m})(1-p^{-1}q^{m}) |  |

be the classical first Jacobi theta function. A straight-forward computation shows, that the function J 1 ​ ( z, τ) J_{1}(z,\tau) arises as the logarithmic derivative of θ 1 \theta_{1},

(7) |  | θ 1 ∙ θ 1 = J 1. \frac{\theta_{1}^{\bullet}}{\theta_{1}}=J_{1}. |  |

This can be generalized as follows. For a formal variable x x, let

(8) |  | J = ∑ n ≥ 0 J n n! ​ x n \curly{J}=\sum_{n\geq 0}\frac{J_{n}}{n!}x^{n} |  |

be the generating functions for the J n J_{n} functions.

###### Theorem 4.

We have

 | J = x ⋅ θ 1 ∙ ​ ( 0, τ) ⋅ exp ( x ∂ z) ⋅ θ 1 ( z, τ) θ 1 ​ ( x 2 ​ π ​ i, τ) ​ θ 1 ​ ( z, τ), \curly{J}=x\cdot\theta_{1}^{\bullet}(0,\tau)\cdot\frac{\exp(x\partial_{z})\cdot\theta_{1}(z,\tau)}{\theta_{1}(\frac{x}{2\pi i},\tau)\theta_{1}(z,\tau)}, |  |

where ∂ z = 1 2 ​ π ​ i ∂ ∂ z \partial_{z}=\frac{1}{2\pi i}\frac{\partial}{\partial z} and

 | exp ( x ∂ z) ⋅ θ 1 ( z, τ):= ∑ k ≥ 0 x k k! ∂ z k ( θ 1 ( z, τ)). \exp(x\partial_{z})\cdot\theta_{1}(z,\tau):=\sum_{k\geq 0}\frac{x^{k}}{k!}\partial_{z}^{k}(\theta_{1}(z,\tau)). |  |

As an application, we obtain by a trivial relation among the deformed Eisenstein series a new 2 2 2 to the best of the author’s knowledge sequence of differential relations among the first theta function, see section 3.2.

### 0.4. Plan of the paper

The first section concerns the study of the deformed Eisenstein series J n J_{n}. We first re-derive their transformation behaviour for modular ( ( z, τ) ↦ ( z / τ, − 1 / τ) (z,\tau)\mapsto(z/\tau,-1/\tau)) and the elliptic ( ( z, τ) ↦ ( z + λ ​ τ + μ, τ) (z,\tau)\mapsto(z+\lambda\tau+\mu,\tau)) transformations. Then we complete J n J_{n} to meromorphic Jacobi forms K n K_{n} of index 0 0 and weight n n via,

 | K n = ∑ k = 0 n ( − 1) n + k ​ ( n k) ​ J k ​ J 1 n − k. K_{n}=\sum_{k=0}^{n}(-1)^{n+k}\binom{n}{k}J_{k}J_{1}^{n-k}. |  |

K n K_{n} is an element of weight n n in the vectorspace 𝕍 n {\mathbb{V}}_{n} of meromorphic Jacobi forms of index 0 0 (i.e. double periodic ones) with only pole at 0 0 of order ≤ n \leq n. We show how to use this to easily derive relation among derivatives and products of the functions J n J_{n}.

In the second section, we prove the main theorem 1. For this, we use the basic fact, that the vector space of Jacobi forms of index m m, 𝒥 ∗, m {\mathcal{J}}_{\ast,m}, is isomorphic to 𝕍 m {\mathbb{V}}_{m} by the map F ↦ F / ϕ m F\mapsto F/\phi^{m}. After reexpressing differentials of Jacobi forms in 𝕍 m {\mathbb{V}}_{m}, we can easily write down differential operators for Jacobi forms. This gives a framework to also deal with more complicated differential equations and operators for Jacobi forms. We use this to find the definition for ∂ J \partial^{J} and prove Corollary 3.

Finally, in the last section we prove Theorem 4 using the completions K n K_{n}. We also give a definition of deformed Eisenstein series J i, n J_{i,n} corresponding to the other classical theta functions and prove an analogous statement for them.

### 0.5. Relation to other work

Deformed Eisenstein series were considered already in [GK09] and [MTZ08] in the process of studying N = 2 N=2 superconformal field theories and differential equations for elliptic genera (which are vector valued weak Jacobi Forms). In particular, in [GK09] Gaberdiel and Keller study the modular and periodic properties of deformed Eisenstein Series and the proofs given here are analog. By arguments from conformal field theory, [GK09] then obtain a set differential operators for (all) weak Jacobi forms. In contrast, our method is completely elementary.

Differential equation for Jacobi forms and deformed Eisenstein series appear also when studying Gromov-Witten invariants. The enumerative geometry of K3 surfaces and Hilbert schemes of K3 surfaces is encoded in various modular and Jacobi forms, see [MPT10], [PT14] and [Obe14]. In [Obe14] the calculation of the GW invariants are reduced to solving an explicit set of partial differential equations in 2 variables, that is obtained by applying WDVV equations (see [FP97]) in the case of the Hilbert scheme of 2 2 points of ℙ 1 × E \mathbb{P}^{1}\times E. Here E E is a smooth elliptic curve. The solution to this system is given by Jacobi forms of index 1 1 and deformed Eisenstein series. The equations give then complicated differential equations intertwining Jacobi forms and deformed Eisenstein series. Understanding this system was the author’s main motivation for studying these functions in more generality.

### 0.6. Acknowledgements

I would like to thank the following people. The programmers behind the math software SAGE and mpmath for their work. Özlem Imamoglu, Jonas Jermann, Aaron Pixton, Martin Raum and Emanuel Scheidegger for various discussions and comments on the subject. And my advisor Rahul Pandharipande for his constant support and patience.

## 1. Deformed Eisenstein series

### 1.1. Transformation properties

We prove the transformation property of J n J_{n} for the elliptic and modular transformations.

###### Lemma 5.

For λ, μ ∈ ℤ \lambda,\mu\in{\mathbb{Z}},

 | J n ​ ( z + λ ​ τ + μ, τ) = ∑ k = 0 n ( − 1) n + k ​ ( n k) ​ λ n − k ​ J k ​ ( z, τ). J_{n}(z+\lambda\tau+\mu,\tau)=\sum_{k=0}^{n}(-1)^{n+k}\binom{n}{k}\lambda^{n-k}J_{k}(z,\tau). |  |

###### Proof.

Replace p p by p ​ q λ pq^{\lambda} in the right hand side of ( 2) and calculate. ∎

Note next, that we have for all k ≥ 1 k\geq 1 the basic relation

(9) |  | k k + 1 ​ J k + 1 ∙ = J k ′. \frac{k}{k+1}J_{k+1}^{\bullet}=J_{k}^{\prime}. |  |

###### Lemma 6 ( [GK09]).

J n ( z / τ, − 1 / τ) = ∑ k = 0 n ( n k) z n − k τ k J k \displaystyle{J_{n}(z/\tau,-1/\tau)=\sum_{k=0}^{n}\binom{n}{k}z^{n-k}\tau^{k}J_{k}}.

###### Proof.

Using the Taylor expansion p = ∑ k ≥ 0 ( 2 ​ π ​ i ​ z) k / k! p=\sum_{k\geq 0}(2\pi iz)^{k}/k! in the Fourier expansion of J 1 J_{1}, one obtains

(10) |  | J 1 ​ ( z, τ) = 1 w + ∑ n ≥ 1 w 2 ​ n − 1 ( 2 ​ n)! ⋅ ( B 2 ​ n ​ E 2 ​ n ​ ( τ)), J_{1}(z,\tau)=\frac{1}{w}+\sum_{n\geq 1}\frac{w^{2n-1}}{(2n)!}\cdot\Big(B_{2n}E_{2n}(\tau)\Big), |  |

where w = 2 ​ π ​ i ​ z w=2\pi iz. By the transformation property of the Eisenstein series, we then have

 | J 1 ( z / τ, − 1 / τ) = z + τ J 1 ( z, τ). J_{1}(z/\tau,-1/\tau)=z+\tau J_{1}(z,\tau). |  |

By induction, we proceed now as follows. Suppose we know how J i ​ ( z, τ) J_{i}(z,\tau) transforms under the substition ( z, τ) ↦ ( z / τ, − 1 / τ) (z,\tau)\mapsto(z/\tau,-1/\tau). Then, by differentiating the transformation equation for J i J_{i} with respect to τ \tau, and using ( 9), we obtain an expression for J i + 1 ∙ ( z / τ, − 1 / τ) J_{i+1}^{\bullet}(z/\tau,-1/\tau). Integrating with respect to z z, we find an expression for J i + 1 ( z / τ, − 1 / τ) J_{i+1}(z/\tau,-1/\tau) up to a function that depends only on τ \tau. Plugging in z = 0 z=0 and using that J 2 ​ g J_{2g} restricts to standard Eisenstein series, for which we know the transformation property, while J 2 ​ g + 1 J_{2g+1} restricts to 0 0, we obtain the transformation law for J i + 1 J_{i+1}. ∎

### 1.2. The completion

Define recursively functions K n ​ ( z, τ) K_{n}(z,\tau) for n ≥ 2 n\geq 2 by

(11) |  | K n = J n − J 1 n − ∑ q = 2 n − 1 ( n q) ​ K q ​ J 1 n − q, K_{n}=J_{n}-J_{1}^{n}-\sum_{q=2}^{n-1}\binom{n}{q}K_{q}J_{1}^{n-q}, |  |

where the sum is empty for n = 2 n=2. An explicit formula can be given by

(12) |  | K n = ∑ k = 0 n ( − 1) n + k ​ ( n k) ​ J k ​ J 1 n − k. K_{n}=\sum_{k=0}^{n}(-1)^{n+k}\binom{n}{k}J_{k}J_{1}^{n-k}. |  |

###### Proposition 7.

K n K_{n} are double-periodic in z z and are modular of weight n n, that is for all λ, μ ∈ ℤ \lambda,\mu\in{\mathbb{Z}}

 | K n ​ ( z + λ ​ τ + μ, τ) \displaystyle K_{n}(z+\lambda\tau+\mu,\tau) | = K n ​ ( z, τ) \displaystyle=K_{n}(z,\tau) |  |

 | K n ( z / τ, − 1 / τ) \displaystyle K_{n}(z/\tau,-1/\tau) | = τ n ​ K n. \displaystyle=\tau^{n}K^{n}. |  |

###### Proof.

By induction on n n and a calculation using equation ( 11). ∎

### 1.3. Poles

Let

 | D = { λ + μ τ | 0 ≤ λ, μ < 1 } D=\{\lambda+\mu\tau\ |\ 0\leq\lambda,\mu<1\} |  |

be a fundamental region for z z with respect to a fixed τ \tau. By ( 7), J 1 J_{1} has a single pole of order 1 1 at 0 0 and no other pole in D D. By ( 9), J n J_{n} then has for n ≥ 2 n\geq 2 no poles at all in D D. 3 3 3 By Lemma 5, J n J_{n} has poles outside of D D.

###### Lemma 8.

For all n ≥ 2 n\geq 2, K n K_{n} has a pole of order n n at z = 0 z=0 and no other poles in a fundamental region. Moreover, if K n = ∑ a k ​ ( τ) ​ w k K_{n}=\sum a_{k}(\tau)w^{k}, where w = 2 ​ π ​ i ​ z w=2\pi iz, then a k a_{k} are holomorphic modular forms of weight k + n k+n, a − 1 = 0 a_{-1}=0 and a − n = ( − 1) n + 1 ​ ( n − 1) a_{-n}=(-1)^{n+1}(n-1). In particular,

 | K n ​ ( z, τ) = ( − 1) n + 1 ​ ( n − 1) w n + O ⁡ ( w − n + 4). K_{n}(z,\tau)=\frac{(-1)^{n+1}(n-1)}{w^{n}}+O(w^{-n+4}). |  |

###### Proof.

The first part is by ( 12) and the analysis of the poles of J n J_{n}. The statement on holomorphicity of a k ​ ( τ) a_{k}(\tau) follows from the Fourier expansion of the J n J_{n} for a fixed z ≠ 0 z\neq 0. a − n a_{-n} follows from the expansion ( 10) and a − 1 = 1 a_{-1}=1, since an elliptic function with a single pole has no residuum. ∎

Let 𝕍 {\mathbb{V}} be the ℂ {\mathbb{C}} -vector space spanned by all meromorphic Jacobi forms 4 4 4 that is, a meromorphic function that satisfies the elliptic and modular transformation equation f: ℂ × ℍ ⟶ ℂ ∪ { ∞ } f:{\mathbb{C}}\times{\mathbb{H}}{\ \longrightarrow\ }{\mathbb{C}}\cup\{\infty\} of index 0 0 and some weight, with only pole in the fundamental region at 0 0 and a Laurent series at 0 0 with coefficients holomorphic modular forms in τ \tau. By Lemma 8, a basis of 𝕍 {\mathbb{V}} as a module over the ring of holomorphic modular forms M ∗ M_{\ast} is given by the K n K_{n}. We will use later the natural filtration

 | 𝕍 n = { f ∈ 𝕍 | f ​ has a pole of order ≤ n ​ at ​ 0 }. {\mathbb{V}}_{n}=\{f\in{\mathbb{V}}\ |\ f\text{ has a pole of order }\leq n\text{ at }0\}. |  |

### 1.4. Relations

Two meromorphic Jacobi forms of index 0 0 with the same principal part at their singularities are equal up to a function of τ \tau. Since for n ≤ 5 n\leq 5 we only have a single negative term in the Taylor expansion of K n K_{n}, we easily obtain relations among products and derivatives of the K i K_{i} for low i i. Moreover, using ( 12) and induction on n n, we see that we can rewrite any derivative of J n J_{n} in the form of products of J i J_{i} for i ≤ n + 1 i\leq n+1. We give the first few examples.

###### Example 9.

 | K 2 \displaystyle K_{2} | = J 1 ∙ − 1 12 ​ E 2 ​ ( τ) = − ℘ ⁡ ( z, τ) \displaystyle=J_{1}^{\bullet}-\frac{1}{12}E_{2}(\tau)=-\wp(z,\tau) |  |

 | J 2 ∙ \displaystyle J_{2}^{\bullet} | = J 3 − J 1 ​ J 2 + 1 6 ​ E 2 ​ J 1 \displaystyle=J_{3}-J_{1}J_{2}+\frac{1}{6}E_{2}J_{1} |  |

 | J 3 ∙ \displaystyle J_{3}^{\bullet} | = J 4 − J 3 ​ J 1 + 1 4 ​ J 2 ​ E 2 − 1 120 ​ E 4 \displaystyle=J_{4}-J_{3}J_{1}+\frac{1}{4}J_{2}E_{2}-\frac{1}{120}E_{4} |  |

 | K 2 ⋅ K 2 \displaystyle K_{2}\cdot K_{2} | = − 1 3 ​ K 4 + 1 60 ​ E 4, \displaystyle=-\frac{1}{3}K_{4}+\frac{1}{60}E_{4}, |  |

where we used ( 7) in the second equality of the first line.

## 2. Differential operators

### 2.1. Reduction to 𝕍 {\mathbb{V}}

Let ϕ = ϕ − 2, 1 \phi=\phi_{-2,1} be as in ( 4). As ϕ ⁡ ( z, τ) = θ 1 ​ ( z, τ) 2 / θ 1 ∙ ​ ( 0, τ) 2 \phi(z,\tau)=\theta_{1}(z,\tau)^{2}/\theta_{1}^{\bullet}(0,\tau)^{2} (see e.g. [DMZ12]), ϕ \phi has a single zero at 0 0 of order 2 2 in the fundamental region.

Let F F be a (weak) Jacobi form of index m m and weight k k and consider F / ϕ m F/\phi^{m}. F / ϕ m F/\phi^{m} is a meromorphic Jacobi form of index 0 0, weight 2 ​ k + m 2k+m and has a single pole of order ≤ 2 ​ m \leq 2m at 0 0 in the fundamental region. Moreover, since the coefficients of a Taylor expansion of F F are quasi-modular forms [DMZ12], F / ϕ m ∈ 𝕍 2 ​ m F/\phi^{m}\in{\mathbb{V}}_{2m}. It is then easy to prove the following.

###### Lemma 10.

Let 𝒥 ~ ∗, m \widetilde{{\mathcal{J}}}_{\ast,m} be the space of weak Jacobi forms of index m m. The map

(13) |  | 𝒥 ~ ∗, m ⟶ 𝕍 2 ​ m, F ↦ F / ϕ m \widetilde{{\mathcal{J}}}_{\ast,m}{\ \longrightarrow\ }{\mathbb{V}}_{2m},\quad F\mapsto F/\phi^{m} |  |

is an isomorphism.

We will use this lemma, to transform statements on (weak) Jacobi forms to 𝕍 2 ​ m {\mathbb{V}}_{2m}.

### 2.2. Operators on 𝕍 2 ​ m {\mathbb{V}}_{2m}

Define the three operators,

 | ∙ \displaystyle\bullet | Multiplication by ​ K i: \displaystyle\text{ Multiplication by }K_{i}:\quad\quad | K i ⋅: \displaystyle K_{i}\cdot: | 𝕍 n ⟶ 𝕍 n + i, \displaystyle{\mathbb{V}}_{n}{\ \longrightarrow\ }{\mathbb{V}}_{n+i},\quad | f \displaystyle f | ↦ K i ⋅ f \displaystyle\mapsto K_{i}\cdot f |  |

 | ∙ \displaystyle\bullet | Differentiation by ​ z: \displaystyle\text{ Differentiation by }z: | D z: \displaystyle D_{z}: | 𝕍 n → 𝕍 n + 1, \displaystyle{\mathbb{V}}_{n}\to{\mathbb{V}}_{n+1}, | f \displaystyle f | ↦ f ∙ \displaystyle\mapsto f^{\bullet} |  |

 | ∙ \displaystyle\bullet | Differentiation by ​ τ: \displaystyle\text{ Differentiation by }\tau: | D τ: \displaystyle D_{\tau}: | 𝕍 n → 𝕍 n + 2, \displaystyle{\mathbb{V}}_{n}\to{\mathbb{V}}_{n+2}, | f \displaystyle f | ↦ f ′ − J 1 ​ f ∙ − k 12 ​ E 2 ​ f. \displaystyle\mapsto f^{\prime}-J_{1}f^{\bullet}-\frac{k}{12}E_{2}f. |  |

For every operator T T of this form, we obtain via

(14) |  | T ~: F ↦ ϕ m ​ T ​ ( F / ϕ m) \widetilde{T}:F\mapsto\phi^{m}T(F/\phi^{m}) |  |

an operator on meromorphic Jacobi forms of fixed index m m. In general T ~ \widetilde{T} will introduce poles to holomorphic Jacobi forms, namely K i, D z, D τ K_{i},D_{z},D_{\tau} give rise to to poles of order i, 1, 2 i,1,2 respectively. By using appropriate linear combinations of these operators, one can cancel the appearing poles and obtain operators defined on holomorphic Jacobi forms. We illustrate the method in degree 2 2.

*Case degree 2.*Consider the operators of degree 2 2, D τ, D z 2 D_{\tau},D_{z}^{2} and multiplication by K 2 K_{2}, obtained from the list above. The action on monomials 1 / w n 1/w^{n} and 1 / w n − 1 1/w^{n-1} (with w = 2 ​ π ​ i ​ z w=2\pi iz) is given by

 | D τ ​ ( 1 w n) \displaystyle D_{\tau}(\frac{1}{w^{n}}) | = n w n + 2 + O ⁡ ( w − n) \displaystyle=\frac{n}{w^{n+2}}+O(w^{-n}) | D τ ​ ( 1 w n − 1) \displaystyle D_{\tau}(\frac{1}{w^{n-1}}) | = ( n − 1) ​ 1 w n + 1 + O ⁡ ( w n − 1) \displaystyle=(n-1)\frac{1}{w^{n+1}}+O(w^{n-1}) |  |

 | D z 2 ​ ( 1 w n) \displaystyle D_{z}^{2}(\frac{1}{w^{n}}) | = n ⁡ ( n + 1) ​ 1 w n + 2 + O ⁡ ( w − n) \displaystyle=n(n+1)\frac{1}{w^{n+2}}+O(w^{-n})\quad | D z 2 ​ ( 1 w n − 1) \displaystyle\quad D_{z}^{2}(\frac{1}{w^{n-1}}) | = n ⁡ ( n − 1) ​ 1 w n + 1 + O ⁡ ( w n − 1) \displaystyle=n(n-1)\frac{1}{w^{n+1}}+O(w^{n-1}) |  |

 | K 2 ⋅ 1 w n \displaystyle K_{2}\cdot\frac{1}{w^{n}} | = − 1 w n + 2 + O ⁡ ( w − n) \displaystyle=\frac{-1}{w^{n+2}}+O(w^{-n}) | K 2 ⋅ 1 w n − 1 \displaystyle K_{2}\cdot\frac{1}{w^{n-1}} | = − 1 w n + 1 + O ⁡ ( w n − 1). \displaystyle=-\frac{1}{w^{n+1}}+O(w^{n-1}). |  |

One finds that

 | D H = 2 ​ n ​ D τ − D z 2 + n ⁡ ( n − 1) ​ K 2 D_{H}=2nD_{\tau}-D_{z}^{2}+n(n-1)K_{2} |  |

is the unique linear combination (up to scalar), that sends 𝕍 n {\mathbb{V}}_{n} to 𝕍 n {\mathbb{V}}_{n}; by ( 14), D H D_{H} introduces then a differential operator

(15) |  | D H: J ~ ∗, m ⟶ J ~ ∗ + 2, m. D_{H}:\widetilde{J}_{\ast,m}{\ \longrightarrow\ }\widetilde{J}_{\ast+2,m}. |  |

This is the classical Heat operator as found in [EZ85], [DMZ12], [GK09].

Consider now the space J ~ 2 ∗, m \widetilde{J}_{2\ast,m} of even-weight weak Jacobi forms. Under ( 13), J ~ 2 ∗, m \widetilde{J}_{2\ast,m} is isomorphic to the space 𝕍 2 ​ m even {\mathbb{V}}_{2m}^{\text{even}} of even functions in 𝕍 2 ​ m {\mathbb{V}}_{2m}. Therefore, to find an operator J ~ 2 ∗, m ⟶ J ~ 2 ∗, m \widetilde{J}_{2\ast,m}{\ \longrightarrow\ }\widetilde{J}_{2\ast,m} of degree 2 2, we only need to consider the action of our 3 operators on the single monomial 1 / ( w 2 ​ m) 1/(w^{2m}), and not on 1 / w 2 ​ m − 1 1/w^{2m-1}. We obtain a second independent operator

 | T τ = D τ + n ​ K 2, T_{\tau}=D_{\tau}+nK_{2}, |  |

that, by ( 14) again, defines an operator on weak Jacobi forms,

(16) |  | T τ: J ~ 2 ∗, m ⟶ J ~ 2 ∗ + 2, m. T_{\tau}:\widetilde{J}_{2\ast,m}{\ \longrightarrow\ }\widetilde{J}_{2\ast+2,m}. |  |

It is known, that D H D_{H} preserves not only weak, but also (full) Jacobi forms. We check the same for T τ T_{\tau}.

###### Proposition 11.

T τ T_{\tau} defines an operator 𝒥 2 ​ k, m ⟶ 𝒥 2 ​ k + 2, m {\mathcal{J}}_{2k,m}{\ \longrightarrow\ }{\mathcal{J}}_{2k+2,m}.

###### Proof.

Let F F be an even weight Jacobi form of weight 2 ​ k 2k and index m m and let F ~ = F / ϕ m \widetilde{F}=F/\phi^{m}. From before, we deduce that T τ ​ F T_{\tau}F is a holomorphic function and satisfies the elliptic and modular transformation equations. We need to show that T τ ​ F T_{\tau}F has a Fourier expansion of the form

 | ∑ n ≥ 0 ∑ r ∈ ℤ r 2 ≤ 4 ​ n ​ m c ⁡ ( n, r) ​ p r ​ q n. \sum_{n\geq 0}\sum_{\begin{subarray}{c}r\in{\mathbb{Z}}\\ r^{2}\leq 4nm\end{subarray}}c(n,r)p^{r}q^{n}. |  |

Equivalently, see [DMZ12], we need to show that ∀ α, β ∈ ℚ \forall\alpha,\beta\in{\mathbb{Q}},

 | q m ​ α 2 ​ T τ ​ ( F) ​ ( α ​ τ + β, τ) q^{m\alpha^{2}}T_{\tau}(F)(\alpha\tau+\beta,\tau) |  |

is bounded for τ → ∞ \tau\rightarrow\infty. We split this into two cases.

Case A. Assume α ∈ ℚ ​ ╲ ​ ℤ \alpha\in{\mathbb{Q}}\diagdown{\mathbb{Z}} or β ∈ ℚ ​ ╲ ​ ℤ \beta\in{\mathbb{Q}}\diagdown{\mathbb{Z}}. Then θ 1 ​ ( α ​ τ + β, τ) ≠ 0 \theta_{1}(\alpha\tau+\beta,\tau)\neq 0 and F ~ ​ ( α ​ τ + β, τ) \widetilde{F}(\alpha\tau+\beta,\tau) is a well defined function of ℍ {\mathbb{H}}. As θ 1 ​ ( α ​ τ + β, τ) \theta_{1}(\alpha\tau+\beta,\tau) is a modular form, it vanishes to a fixed order at τ = ∞ \tau=\infty and hence so does F ~ \widetilde{F}. When applying T τ T_{\tau} to F ~ \widetilde{F}, we take derivatives with respect to τ \tau and multiply with functions of the form J i J_{i}. The first does at most increase the order of convergence at τ = ∞ \tau=\infty. To see that this is true also for the second, note two things: a) we may restrict to 0 ≤ α, β < 1 0\leq\alpha,\beta<1 (with α, β = 0 \alpha,\beta=0 is excluded) and b) by the Fourier expansion of J i J_{i}, J i ​ ( α ​ τ + β, τ) J_{i}(\alpha\tau+\beta,\tau) is bounded for τ → ∞ \tau\rightarrow\infty. Therefore, T τ ​ ( F ~) T_{\tau}(\widetilde{F}) converges not worse then F ~ \widetilde{F} for τ ↦ ∞ \tau\mapsto\infty. Applying ϕ m \phi^{m}, the claim follows.

Case B. Assume α, β ∈ ℤ \alpha,\beta\in{\mathbb{Z}}. Then we can equally well assume α = β = 0 \alpha=\beta=0 and we need to show that T q ​ ( F) ​ ( 0, τ) T_{q}(F)(0,\tau) is bounded for τ → ∞ \tau\rightarrow\infty. Let F = F 0 + w 2 ​ F 2 + O ⁡ ( w 4) F=F_{0}+w^{2}F_{2}+O(w^{4}), with F 0, F 2 F_{0},F_{2} quasi modular forms. Then

 | ( T q ​ F) ​ ( 0, τ) = F 0 ′ + ( m 6 − k 12) ​ E 2 ​ F 0 − 2 ​ F 2 (T_{q}F)(0,\tau)=F_{0}^{\prime}+\Big(\frac{m}{6}-\frac{k}{12}\Big)E_{2}F_{0}-2F_{2} |  |

which is bounded for τ → ∞ \tau\rightarrow\infty. ∎

###### Proof of Theorem 1.

Define

 | ∂ J = 1 1 − 4 ​ m ( T τ − D H). \partial^{J}=\frac{1}{1-4m}(T_{\tau}-D_{H}). |  |

By the previous proposition, ∂ J \partial^{J} is an operator on Jacobi forms, 𝒥 2 ​ k, m ⟶ 𝒥 2 ​ k + 2, m {\mathcal{J}}_{2k,m}{\ \longrightarrow\ }{\mathcal{J}}_{2k+2,m}. The claims of the Theorems follow now from direct calculations. ∎

###### Remark 12.

The case of higher degree works completely analog; see [GK09] for a list of operators on all Jacobi forms. With the above method, one can find additional operators defined only on even or odd Jacobi forms.

### 2.3. Ramanujan’s equations

Let E 2, 1 ​ ( z, τ) E_{2,1}(z,\tau) be defined as in Definition 2. The following is derived by straightforward means.

###### Lemma 13.

E 2, 1 E_{2,1} satisfies the following properties:

1. (a)

holomorphic on ℂ × ℍ {\mathbb{C}}\times\mathbb{H}

2. (b)

has a Fourier expansion E 2, 1 ​ ( z, τ) = ∑ n ≥ 0 ∑ r ∈ ℤ r 2 ≤ 4 ​ n c ⁡ ( n, r) ​ p r ​ q n E_{2,1}(z,\tau)=\sum_{n\geq 0}\sum_{\begin{subarray}{c}r\in{\mathbb{Z}}\\ r^{2}\leq 4n\end{subarray}}c(n,r)p^{r}q^{n}. In particular c ⁡ ( n, r) = 0 c(n,r)=0 for 4 ​ n − r 2 < 0 4n-r^{2}<0.

3. (c)

satisfies the elliptic transformation equation, while the modular equation reads

 | E 2, 1 ( z / τ, − 1 / τ) = e 2 ​ π ​ i ​ z 2 τ τ 2 E 2, 1 + 1 2 ​ π ​ i e 2 ​ π ​ i ​ z 2 τ τ ϕ 0, 1 E_{2,1}(z/\tau,-1/\tau)=e^{\frac{2\pi iz^{2}}{\tau}}\tau^{2}E_{2,1}+\frac{1}{2\pi i}e^{\frac{2\pi iz^{2}}{\tau}}\tau\phi_{0,1} |  |

4. (d)

E 2, 1 ​ ( 0, τ) = E 2 ​ ( τ) E_{2,1}(0,\tau)=E_{2}(\tau).

The first Fourier coefficients c ⁡ ( n, r) c(n,r) of E 2, 1 E_{2,1} are given by

 | − 4 -4 | − 3 -3 | − 2 -2 | − 1 -1 | 0 0 | 1 1 | 2 2 | 3 3 | 4 4 |

0 0 | 0 0 | 0 0 | 0 0 | 0 0 | 1 1 | 0 0 | 0 0 | 0 0 | 0 0 |

1 1 | 0 0 | 0 0 | 1 1 | − 28 -28 | 30 30 | − 28 -28 | 1 1 | 0 0 | 0 0 |

2 2 | 0 0 | 0 0 | 30 30 | − 264 -264 | 396 396 | − 264 -264 | 30 30 | 0 0 | 0 0 |

3 3 | 0 0 | − 28 -28 | 396 396 | − 1620 -1620 | 2408 2408 | − 1620 -1620 | 396 396 | − 28 -28 | 0 0 |

4 4 | 1 1 | − 264 -264 | 2408 2408 | − 7944 -7944 | 11430 11430 | − 7944 -7944 | 2408 2408 | − 264 -264 | 1 1 |

###### Proof of Corollary 3.

A direct check. ∎

## 3. The relation to theta functions

### 3.1. Proof of Theorem 4

Define functions h ~ n ​ ( τ) \widetilde{h}_{n}(\tau) by

(17) |  | 1 θ 1 ​ ( z, τ) = 1 w ​ ∑ n ≥ 0 h ~ n ​ ( τ) ​ w n, \frac{1}{\theta_{1}(z,\tau)}=\frac{1}{w}\sum_{n\geq 0}\widetilde{h}_{n}(\tau)w^{n}, |  |

where as before w = 2 ​ π ​ i ​ z w=2\pi iz and let

 | h n:= n! ⋅ h ~ n ​ ( τ) ​ θ 1 ∙ ​ ( 0, τ). h_{n}:=n!\cdot\widetilde{h}_{n}(\tau)\theta_{1}^{\bullet}(0,\tau). |  |

Here 0! = 1 0!=1 and h 0 = 1 h_{0}=1. As θ 1 ​ ( z, τ) \theta_{1}(z,\tau) is odd, h n = 0 h_{n}=0 for all odd n n.

For n ≥ 0 n\geq 0, set

 | F n ( z, τ) = 1 θ 1 ( ∑ k = 0 n ( n k) h n − k θ 1 k ∙), F_{n}(z,\tau)=\frac{1}{\theta_{1}}\Big(\sum_{k=0}^{n}\binom{n}{k}h_{n-k}\theta_{1}^{k\bullet}\Big), |  |

where we let θ i k ∙ \theta_{i}^{k\bullet} (resp. θ i k ′ \theta_{i}^{k^{\prime}}) be the k k ’th derivative of θ i \theta_{i} with respect to z z (resp. τ \tau).

###### Theorem 14.

F n = J n F_{n}=J_{n} for all n ≥ 0 n\geq 0.

Note that Theorem 14 directly implies Theorem 4.

###### Proof.

Differentiationg the equation

 | θ 1 ​ ( z + λ ​ τ, τ) = − e − 2 ​ π ​ i ​ ( λ ​ z + 1 2 ​ λ 2 ​ τ) ​ θ 1 ​ ( z, τ) \theta_{1}(z+\lambda\tau,\tau)=-e^{-2\pi i(\lambda z+\frac{1}{2}\lambda^{2}\tau)}\theta_{1}(z,\tau) |  |

we find

 | θ 1 k ∙ ( z + λ τ, τ) = − ∑ l = 0 k ( − 1) l + k ( k l) e − 2 ​ π ​ i ​ ( λ ​ z + 1 2 ​ λ 2 ​ τ) λ k − l θ 1 l ∙. \theta_{1}^{k\bullet}(z+\lambda\tau,\tau)=-\sum_{l=0}^{k}(-1)^{l+k}\binom{k}{l}e^{-2\pi i(\lambda z+\frac{1}{2}\lambda^{2}\tau)}\lambda^{k-l}\theta_{1}^{l\bullet}. |  |

Therefore, independent of h k h_{k},

 | F n ​ ( z + λ ​ τ) \displaystyle F_{n}(z+\lambda\tau) | = 1 θ 1 ( ∑ k = 0 n ( n k) h n − k ∑ l = 0 k ( − 1) l + k ( k l) λ k − l θ 1 l ∙) \displaystyle=\frac{1}{\theta_{1}}\left(\sum_{k=0}^{n}\binom{n}{k}h_{n-k}\sum_{l=0}^{k}(-1)^{l+k}\binom{k}{l}\lambda^{k-l}\theta_{1}^{l\bullet}\right) |  |

 |  | = 1 θ 1 ( ∑ k = 0 n ∑ l = 0 k ( n n − k + l) ( n − k + l l) ( − 1) n − k h k − l λ n − k θ 1 l ∙) \displaystyle=\frac{1}{\theta_{1}}\left(\sum_{k=0}^{n}\sum_{l=0}^{k}\binom{n}{n-k+l}\binom{n-k+l}{l}(-1)^{n-k}h_{k-l}\lambda^{n-k}\theta_{1}^{l\bullet}\right) |  |

 |  | = 1 θ 1 ( ∑ k = 0 n ( − 1) n + k λ n − k ( n k) ∑ l = 0 k ( k l) h k − l θ 1 l ∙) \displaystyle=\frac{1}{\theta_{1}}\left(\sum_{k=0}^{n}(-1)^{n+k}\lambda^{n-k}\binom{n}{k}\sum_{l=0}^{k}\binom{k}{l}h_{k-l}\theta_{1}^{l\bullet}\right) |  |

 |  | = ∑ k = 0 n ( − 1) n + k ​ ( n k) ​ λ n − k ​ F k. \displaystyle=\sum_{k=0}^{n}(-1)^{n+k}\binom{n}{k}\lambda^{n-k}F_{k}. |  |

We proceed by induction on n n. For n = 0 n=0 nothing is to prove and n = 1 n=1 follows from ( 7). Assume now, that the claim of the theorem is true for all k < n k<n, with n ≥ 2 n\geq 2. Let

 | K n ~ = ∑ k = 0 n ( − 1) n + k ​ ( n k) ​ F k ​ F 1 n − k \widetilde{K_{n}}=\sum_{k=0}^{n}(-1)^{n+k}\binom{n}{k}F_{k}F_{1}^{n-k} |  |

and note that the recursion relation ( 11) holds for K n ~ \widetilde{K_{n}} as well.

Let n = 2 ​ m n=2m be even. Then, for a fixed τ \tau, F 2 ​ m ​ ( z, τ) F_{2m}(z,\tau) doesn’t have any poles for z ∈ { λ + μ τ ∣ 0 ≤ λ, μ < 1 } z\in\{\lambda+\mu\tau\mid 0\leq\lambda,\mu<1\}. Indeed, θ 1 2 k ∙ = 2 k θ 1 k ′ \theta_{1}^{2k\bullet}=2^{k}\theta_{1}^{k^{\prime}} has a zero of order 1 at z = 0 z=0 and hence θ 1 2 k ∙ / θ 1 \theta_{1}^{2k\bullet}/\theta_{1} extends to a holomorphic function at z = 0 z=0. By induction we conclude that the principal part of K n ~ \widetilde{K_{n}} equals the principal part of K n K_{n}. Therefore it is left to show that F 2 ​ m ​ ( 0) = J 2 ​ m ​ ( 0) = B 2 ​ m ​ E 2 ​ m F_{2m}(0)=J_{2m}(0)=B_{2m}E_{2m}. This is equivalent to the identity,

(18) |  | ∑ k = 0 m ( 2 ​ m 2 ​ k) ​ h 2 ​ m − 2 ​ k ​ θ 1 2 k ∙ θ 1 ​ ( 0) = B 2 ​ m ​ E 2 ​ m. \sum_{k=0}^{m}\binom{2m}{2k}h_{2m-2k}\frac{\theta_{1}^{2k\bullet}}{\theta_{1}}(0)=B_{2m}E_{2m}. |  |

As θ 1 2 k ∙ / θ 1 \theta_{1}^{2k\bullet}/\theta_{1} is an even holomorphic function,

 | ( θ 1 2 k ∙ θ 1) ∙ = θ 1 ( 2 k + 1) ∙ θ 1 − θ 1 2 k ∙ θ 1 ​ θ 1 ∙ θ 1 \Big(\frac{\theta_{1}^{2k\bullet}}{\theta_{1}}\Big)^{\bullet}=\frac{\theta_{1}^{(2k+1)\bullet}}{\theta_{1}}-\frac{\theta_{1}^{2k\bullet}}{\theta_{1}}\frac{\theta_{1}^{\bullet}}{\theta_{1}} |  |

vanishes to first order at 0 0. Comparing poles and using θ 1 ∙ / θ 1 = 1 / w + O ⁡ ( w) \theta_{1}^{\bullet}/\theta_{1}=1/w+O(w), we obtain

(19) |  | ( θ 1 2 k ∙ / θ 1) ( 0, τ) = Res w = 0 ( θ 1 ( 2 k + 1) ∙ θ 1) = θ 1 ( 2 k + 1) ∙ ( 0, τ) θ 1 ∙ ​ ( 0, τ), (\theta_{1}^{2k\bullet}/\theta_{1})(0,\tau)=\text{Res}_{w=0}\Big(\frac{\theta_{1}^{(2k+1)\bullet}}{\theta_{1}}\Big)=\frac{\theta_{1}^{(2k+1)\bullet}(0,\tau)}{\theta_{1}^{\bullet}(0,\tau)}, |  |

where we used the Taylor expansion θ 1 = ∑ k ≥ 0 θ 1 ( 2 k + 1) ∙ ( 0) ( 2 ​ k + 1)! ​ w 2 ​ k + 1 \theta_{1}=\sum_{k\geq 0}\frac{\theta_{1}^{(2k+1)\bullet}(0)}{(2k+1)!}w^{2k+1} for the second equation and Res denotes the residuum.

Therefore ( 18) reduces to

 | ∑ k = 0 m ( 2 ​ m 2 ​ k) ( 2 m − 2 k)! h ~ 2 ​ ( m − k) θ 1 ( 2 k + 1) ∙ ( 0) = B 2 ​ m E 2 ​ m, \sum_{k=0}^{m}\binom{2m}{2k}(2m-2k)!\widetilde{h}_{2(m-k)}\theta_{1}^{(2k+1)\bullet}(0)=B_{2m}E_{2m}, |  |

which follows from comparing the 2 ​ m − 1 2m-1 -th Taylor coefficient of the left and right hand side of 1 θ 1 ​ ( z, τ) ⋅ θ 1 ​ ( z, τ) ∙ = J 1 \frac{1}{\theta_{1}(z,\tau)}\cdot\theta_{1}(z,\tau)^{\bullet}=J_{1}.

The case n = 2 ​ m + 1 n=2m+1 odd is similar and ommited. ∎

###### Remark 15.

Comparing the w 2 ​ n w^{2n} coefficient of 1 / θ 1 ​ ( z, τ) ⋅ θ 1 ​ ( z, τ) = 1 1/\theta_{1}(z,\tau)\cdot\theta_{1}(z,\tau)=1 using ( 17), we obtain the relation

(20) |  | ∑ k = 0 m h ~ 2 ​ m − 2 ​ k ​ ( τ) ​ θ 1 ( 2 k + 1) ∙ ( 0, τ) ( 2 ​ k + 1)! = 0. \sum_{k=0}^{m}\widetilde{h}_{2m-2k}(\tau)\frac{\theta_{1}^{(2k+1)\bullet}(0,\tau)}{(2k+1)!}=0. |  |

By ( 19),

 | θ 1 ( 2 k + 1) ∙ ( 0, τ) = θ 1 ∙ ( 0, τ) ⋅ ( θ 1 2 k ∙ / θ 1) ( 0, τ) = θ 1 ∙ ( 0, τ) ⋅ ( θ 1 k ′ / θ 1) ( 0, τ). \theta_{1}^{(2k+1)\bullet}(0,\tau)=\theta_{1}^{\bullet}(0,\tau)\cdot(\theta_{1}^{2k\bullet}/\theta_{1})(0,\tau)=\theta_{1}^{\bullet}(0,\tau)\cdot(\theta_{1}^{k\prime}/\theta_{1})(0,\tau). |  |

Let P k = ( θ 1 k ′ / θ 1) ( 0, τ) P_{k}=(\theta_{1}^{k\prime}/\theta_{1})(0,\tau). Then using ( 6), P 1 = E 2 / 8 P_{1}=E_{2}/8 and taking the derivative of P n P_{n},

(21) |  | P n + 1 = P n ′ + 1 8 ​ E 2 ​ P n. P_{n+1}=P_{n}^{\prime}+\frac{1}{8}E_{2}P_{n}. |  |

By ( 20) and ( 21), we obtain a recursion relation for the function h n h_{n}.

The first few non-trivial identities given by Theorem 14 then read,

 | J 2 \displaystyle J_{2} | = 1 θ 1 ​ ( θ 1 ∙ ⁣ ∙ − 1 12 ​ E 2 ​ θ 1) \displaystyle=\frac{1}{\theta_{1}}(\theta_{1}^{\bullet\bullet}-\frac{1}{12}E_{2}\theta_{1}) |  |

 | J 3 \displaystyle J_{3} | = 1 θ 1 ( θ 1 ∙ ∙ ∙ − 1 4 E 2 θ 1 ∙) \displaystyle=\frac{1}{\theta_{1}}(\theta_{1}^{\bullet\bullet\bullet}-\frac{1}{4}E_{2}\theta_{1}^{\bullet}) |  |

 | J 4 \displaystyle J_{4} | = 1 θ 1 ( θ 1 ∙ ∙ ∙ ∙ − 1 2 E 2 θ 1 ∙ ⁣ ∙ + ( − 1 10 E 2 ′ + 7 240 E 2 2) θ 1. \displaystyle=\frac{1}{\theta_{1}}(\theta_{1}^{\bullet\bullet\bullet\bullet}-\frac{1}{2}E_{2}\theta_{1}^{\bullet\bullet}+(-\frac{1}{10}E_{2}^{\prime}+\frac{7}{240}E_{2}^{2})\theta_{1}. |  |

### 3.2. Applications

Let J = ∑ n ≥ 0 J n ​ x n / n! \curly{J}=\sum_{n\geq 0}J_{n}x^{n}/n! as in ( 8). By ( 9),

 | ∂ τ J = ( ∂ ∂ x − 1 x) ​ ∂ z J, \partial_{\tau}\curly{J}=\Big(\frac{\partial}{\partial x}-\frac{1}{x}\Big)\partial_{z}\curly{J}, |  |

where ∂ τ = 1 2 ​ π ​ i ∂ ∂ τ \partial_{\tau}=\frac{1}{2\pi i}\frac{\partial}{\partial\tau} and ∂ z = 1 2 ​ π ​ i ∂ ∂ z \partial_{z}=\frac{1}{2\pi i}\frac{\partial}{\partial z}. By Theorem 4, this implies relation among differentials of θ 1 ​ ( z, τ) \theta_{1}(z,\tau). For example extracting the x 3 x^{3} coefficient, we have

###### Corollary 16.

 | θ 1 ∙ ∙ ∙ ∙ θ 1 − 4 θ 1 ∙ ∙ ∙ θ 1 ∙ + 3 θ 1 ∙ ⁣ ∙ θ 1 ∙ ⁣ ∙ − θ 1 θ 1 ∙ ⁣ ∙ E 2 + ( θ 1 ∙) 2 E 2 + 1 2 θ 1 2 E 2 ′ = 0 \theta_{1}^{\bullet\bullet\bullet\bullet}\theta_{1}-4\theta_{1}^{\bullet\bullet\bullet}\theta_{1}^{\bullet}+3\theta_{1}^{\bullet\bullet}\theta_{1}^{\bullet\bullet}-\theta_{1}\theta_{1}^{\bullet\bullet}E_{2}+(\theta_{1}^{\bullet})^{2}E_{2}+\frac{1}{2}\theta_{1}^{2}E_{2}^{\prime}=0 |  |

### 3.3. The other theta functions

We consider an analog of deformed Eisenstein series corresponding to the theta functions θ 2, θ 3, θ 4 \theta_{2},\theta_{3},\theta_{4}. For n ≥ 1 n\geq 1, define

 | J 2, n \displaystyle J_{2,n} | = 2 ​ J n ​ ( 2 ​ z, 2 ​ τ) − J n ​ ( z, τ) \displaystyle=2J_{n}(2z,2\tau)-J_{n}(z,\tau) |  |

 | J 3, n \displaystyle J_{3,n} | = 2 2 − n ​ J n ​ ( 2 ​ z, τ) − 2 ​ J n ​ ( 2 ​ z, 2 ​ τ) + J n ​ ( z, τ) − 2 1 − n ​ J n ​ ( z, τ / 2) \displaystyle=2^{2-n}J_{n}(2z,\tau)-2J_{n}(2z,2\tau)+J_{n}(z,\tau)-2^{1-n}J_{n}(z,\tau/2) |  |

 | J 4, n \displaystyle J_{4,n} | = 1 2 n − 1 ​ J n ​ ( z, τ / 2) − J n ​ ( z, τ). \displaystyle=\frac{1}{2^{n-1}}J_{n}(z,\tau/2)-J_{n}(z,\tau). |  |

Concretely, we have

(22) |  | J 2, n ​ ( z, τ) \displaystyle J_{2,n}(z,\tau) | = δ n, 1 ​ p p + 1 + B n − n ​ ∑ k, r ≥ 1 ( − 1) k ​ r n − 1 ​ ( p k + p − k) ​ q k ​ r \displaystyle=\delta_{n,1}\frac{p}{p+1}+B_{n}-n\sum_{k,r\geq 1}(-1)^{k}r^{n-1}(p^{k}+p^{-k})q^{kr} |  |

 | J 3, n ​ ( z, τ) \displaystyle J_{3,n}(z,\tau) | = − B n ​ ( 1 − 1 2 n − 1) − n ​ ∑ k, r ≥ 1 ( r − 1 2) n − 1 ​ ( − 1) k ​ ( p k + ( − 1) n ​ p − k) ​ q k ⁡ ( r − 1 2) \displaystyle=-B_{n}(1-\frac{1}{2^{n-1}})-n\sum_{k,r\geq 1}(r-\frac{1}{2})^{n-1}(-1)^{k}(p^{k}+(-1)^{n}p^{-k})q^{k(r-\frac{1}{2})} |  |

 | J 4, n ​ ( z, τ) \displaystyle J_{4,n}(z,\tau) | = − B n ​ ( 1 − 1 2 n − 1) − n ​ ∑ k, r ≥ 1 ( r − 1 2) n − 1 ​ ( p k + ( − 1) n ​ p − k) ​ q k ⁡ ( r − 1 2). \displaystyle=-B_{n}(1-\frac{1}{2^{n-1}})-n\sum_{k,r\geq 1}(r-\frac{1}{2})^{n-1}(p^{k}+(-1)^{n}p^{-k})q^{k(r-\frac{1}{2})}. |  |

The statements of section 1 apply with minor modifications also to the J i, n J_{i,n}. In particular we can define periodic K i, n K_{i,n}, find relations and express the derivatives of J i, n J_{i,n} in terms of J i, n J_{i,n} itself.

Let

 | θ 2 ​ ( z, τ) \displaystyle\theta_{2}(z,\tau) | = θ 1 ​ ( z + 1 2, τ) \displaystyle=\theta_{1}(z+\frac{1}{2},\tau) |  |

 | θ 3 ​ ( z, τ) \displaystyle\theta_{3}(z,\tau) | = q 1 / 8 ​ p 1 / 2 ​ θ 1 ​ ( z + 1 2 ​ τ + 1 2, τ) \displaystyle=q^{1/8}p^{1/2}\theta_{1}(z+\frac{1}{2}\tau+\frac{1}{2},\tau) |  |

 | θ 4 ​ ( z, τ) \displaystyle\theta_{4}(z,\tau) | = θ 3 ​ ( z + 1 / 2, τ) = − i ​ q 1 / 8 ​ p 1 / 2 ​ θ 1 ​ ( z + 1 / 2 ​ τ, τ) \displaystyle=\theta_{3}(z+1/2,\tau)=-iq^{1/8}p^{1/2}\theta_{1}(z+1/2\tau,\tau) |  |

be the other theta functions. We state the analog of Theorem 4.

###### Theorem 17.

We have

 | ∑ n ≥ 0 J i, n ​ ( z, τ) ​ x n n! = x ​ θ 1 ∙ ​ ( 0, τ) θ 1 ​ ( x 2 ​ π ​ i) ​ exp ( x ∂ p) ⋅ θ i ( z, τ) θ i ​ ( z, τ). \sum_{n\geq 0}J_{i,n}(z,\tau)\frac{x^{n}}{n!}=x\ \frac{\theta_{1}^{\bullet}(0,\tau)}{\theta_{1}(\frac{x}{2\pi i})}\ \frac{\exp(x\partial_{p})\cdot\theta_{i}(z,\tau)}{\theta_{i}(z,\tau)}. |  |

###### Proof.

With ( 22) one proves the formulas

 | J 2, n ​ ( z, τ) \displaystyle J_{2,n}(z,\tau) | = J n ​ ( z + 1 2) \displaystyle=J_{n}(z+\frac{1}{2}) |  |

 | J 3, n ​ ( z, τ) \displaystyle J_{3,n}(z,\tau) | = ∑ l = 0 n ( n l) ​ 1 2 n − l ​ J l ​ ( z + 1 2 + 1 2 ​ τ) \displaystyle=\sum_{l=0}^{n}\binom{n}{l}\frac{1}{2^{n-l}}J_{l}(z+\frac{1}{2}+\frac{1}{2}\tau) |  |

 | J 4, n ​ ( z, τ) \displaystyle J_{4,n}(z,\tau) | = ∑ l = 0 n ( n l) ​ 1 2 n − l ​ J l ​ ( z + 1 2 ​ τ). \displaystyle=\sum_{l=0}^{n}\binom{n}{l}\frac{1}{2^{n-l}}J_{l}(z+\frac{1}{2}\tau). |  |

The claims then reduces directly to Theorem 4. ∎

## References

- [Cho97] Y. Choie, Correspondence among Eisenstein series E 2, 1 ​ ( τ, z) E_{2,1}(\tau,z), H 3 / 2 ​ ( τ) H_{3/2}(\tau) and E 2 ​ ( τ) E_{2}(\tau), Manuscripta Math. 93 (2), 177–187 (1997).
- [DMZ12] A. Dabholkar, S. Murthy and D. Zagier, Quantum Black Holes, Wall Crossing, and Mock Modular Forms, (2012), arXiv:1208.4074.
- [EZ85] M. Eichler and D. Zagier, The theory of Jacobi forms, volume 55 of Progress in Mathematics, Birkhäuser Boston Inc., Boston, MA, 1985.
- [FP97] W. Fulton and R. Pandharipande, Notes on stable maps and quantum cohomology, in Algebraic geometry—Santa Cruz 1995, volume 62 of Proc. Sympos. Pure Math., pages 45–96, Amer. Math. Soc., Providence, RI, 1997.
- [GK09] M. R. Gaberdiel and C. A. Keller, Differential operators for elliptic genera, Commun. Number Theory Phys. 3 (4), 593–618 (2009).
- [MPT10] D. Maulik, R. Pandharipande and R. P. Thomas, Curves on K3 surfaces and modular forms, J.Topol.3:937-996,2010, 2010.
- [MTZ08] G. Mason, M. P. Tuite and A. Zuevsky, Torus n n -point functions for ℝ \mathbb{R} -graded vertex operator superalgebras and continuous fermion orbifolds, Comm. Math. Phys. 283 (2), 305–342 (2008).
- [Obe14] G. Oberdieck, Gromov-Witten invariants of the Hilbert scheme of points of a K3 surface, 2014, arXiv:1406.1139.
- [PT14] R. Pandharipande and R. P. Thomas, The Katz-Klemm-Vafa conjecture for K3 surfaces, 2014, arXiv:1404.6698.
- [Ram00] S. Ramanujan, On certain arithmetical functions [Trans. Cambridge Philos. Soc. 22 (1916), no. 9, 159–184], in Collected papers of Srinivasa Ramanujan, pages 136–162, AMS Chelsea Publ., Providence, RI, 2000.

Departement Mathematik
ETH Zürich
georgo@math.ethz.ch


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
