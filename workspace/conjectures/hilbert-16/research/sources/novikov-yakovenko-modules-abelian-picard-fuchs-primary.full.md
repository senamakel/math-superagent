<!-- source: https://arxiv.org/html/math/0110126 | converted from HTML -->

Modules of Abelian integrals and Picard-Fuchs systems

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0110126v3 [math.DS] 06 Jun 2002

1 1 1 The research was supported by the Killam grant of P. Milman and by James S. McDonnell Foundation.

# Modules of Abelian integrals and Picard-Fuchs systems

D. Novikov Affiliation: Department of Mathematics, Purdue University, West Lafayette, IN 47907, USA Email: [dmitry@math.purdue.edu][3]

May 27, 2002

###### Abstract

We give a simple proof of an isomorphism between two ℂ ⁡ [t] \mathbb{C}[t] -modules corresponding to bivariate polynomial H H with nondegenerate highest homogeneous part: the module of relative cohomologies Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1} and the module of Abelian integrals. Using this isomorphism, we prove existence and deduce some properties of the corresponding Picard-Fuchs system.

Abelian integral is a result of integration of a polynomial one-form along a cycle lying on level curve (possibly complex) of a bivariate polynomial considered as a function (possibly multivalued) of the value of the polynomial. Abelian integrals appear naturally when studying bifurcations of limit cycles of planar polynomial vector fields. In particular, zeros of Abelian integrals are related to limit cycles appearing in polynomial perturbations of polynomial Hamiltonian vector fields. This is the reason why sometimes the question about the number of zeroes of Abelian integrals is sometimes called infinitesimal Hilbert 16 th problem.

The traditional approach to the investigation of Abelian integrals uses properties of the system of linear ordinary differential equations satisfied by the Abelian integrals, the so-called Picard-Fuchs system. This approach is used both in fundamental general finiteness result of [24, 13] and in exact estimates in the cases of low degree, as in [9]. The existence of such a system can be easily proven due to the very basic properties of branching of Abelian integrals, see [1], and was well known already to Riemann if not Gauss. Nevertheless an effective computation of this system turns out to be a difficult problem. One particular case of this problem (namely of the hyperelliptic integrals) is quite classic, see e.g. [21, 19, 7]. In [18] a generalization of this approach for regular at infinity (see below for exact definition) polynomials in two variables is suggested (in fact, it can be easily generalized for any number of variables). The main idea of [18] is to trade the minimality of the size of the system (thus redundant) for an explicitness of the construction and control on the magnitude of the coefficients. Another, probably not less important, gain is that the resulting system is not only Fuchsian, but also has a hypergeometric form.

The control on the magnitude of coefficients in [18] is very important from the infinitesimal Hilbert 16 th problem point of view. Indeed, recent progress towards its solution is partly based on the principle that solutions of linear ordinary differential equations with bounded coefficients cannot oscillate too wildly, see e.g. [11] (simple proofs of a result of this type can be found in [16] and [23]). Though more complicated, this principle still holds for polynomial systems of differential equations, see [16, 17] (polynomiality is essential, see [14]). In a slightly modified form, this principle allows to give results in an upper bound on the number of zeros of an Abelian integral in terms of the minimal distance between critical values of its (regular at infinity) Hamiltonian, see [18]. As an application of this principle one can also deduce an effective upper bound for the number of zeroes of Abelian integrals corresponding to hyperelliptic Hamiltonians satisfying some additional assumption, see [15].

The Picard-Fuchs systems discussed in this paper is irredundant in the sense that it has the minimal possible dimension (namely the dimension equal to the dimension of the homology group H 1 ( { H ( x, y) = t }, ℂ) H^{1}(\{H(x,y)=t\},\mathbb{C}) of a generic fibre). This minimality allows to guess most of the important information about the system if the critical values of the Hamiltonian are distinct and the Hamiltonian is regular at infinity (so-called Morse-plus Hamiltonians).

We prove existence of such system using decomposition in Petrov modules. It is easy to see that exact forms and forms proportional to d ​ H dH have zero Abelian integrals, so in fact Abelian integrals depend on the class of a form in the so-called Petrov module – the quotient of the space of all forms by a subspace spanned by exact forms and forms proportional to d ​ H dH, considered in [20]. In [5] L.Gavrilov proved that the Petrov module of a generic Hamiltonian is a finitely generated free ℂ ⁡ [t] {\mathbb{C}}[t] -module.The local counterpart of this statement is due to E.Brieskorn and M. Sebastiani [3, 22]. The proof in [5] contains a reference to a general nondegeneracy result (see [1, Theorem 13.6, Ch III]), based on the theory of deformations of Hodge structures. In the recent preprint [8] the involved constant is computed and exact formulae are given. We suggest an elementary proof of this result, see also [25].

The main idea of [18] was to use a connection between division with remainder of polynomials and differentiation of Abelian integrals given by Gelfand-Leray formula. In this work we replace the explicit division with remainder by decomposition in Petrov modules in order to get the same result. This is still enough for the construction of the system, though the result is less explicit. Yet one can still guess all singular points and get some information about coefficients. However, we show that the resulting irredundant system is not always Fuchsian, namely it can have regular but non-Fuchsian point at infinity. Though after a suitable rational gauge transform the irredundant system becomes Fuchsian (see § 5), the nice form of Theorem 1 is then lost.

### 0.1 Acknowledgments

I am grateful to S. Yakovenko for the numerous discussions and help in preparation of this text. I am grateful to Yulij Ilyashenko for an opportunity to read his recent preprint and numerous discussions. I am grateful to anonymous referee for several important remarks.

## 1 Genericity and generalities

In what follows we always assume that our polynomial H ⁡ ( x, y) H(x,y) is regular at infinity, i.e., that its highest homogeneous part H ^ ​ ( x, y) {\widehat{H}}(x,y) is a product of pairwise different linear factors.

One can easily prove that for regular at infinity polynomial H ⁡ ( x, y) H(x,y) of degree n + 1 n+1 the homogeneous polynomial H ^ {\widehat{H}} has an isolated critical point (necessarily of multiplicity μ = n 2 \mu=n^{2}) at the origin ( x, y) = ( 0, 0) (x,y)=(0,0), its level curves { H ^ = c } ⊂ ℂ 2 \{{\widehat{H}}=c\}\subset{\mathbb{C}}^{2} are nonsingular for c ≠ 0 c\not=0. Moreover, the level curves of H H intersect transversally the line at infinity, and foliation of ℂ 2 {\mathbb{C}}^{2} by level curves of H H is locally topologically trivial over ℂ ∖ Σ {\mathbb{C}}\setminus\Sigma, where Σ \Sigma is the set of ≤ ( deg ⁡ H − 1) 2 \leq(\deg H-1)^{2} critical values of H H. In other words, the only atypical values are the critical ones.

By Abelian integral we mean a result of integration of a one-form ω \omega along a continuous family of cycles δ ( t) ⊂ { H = t } \delta(t)\subset\{H=t\} considered as a function of t t:

 | I ω, δ ​ ( t) = ∮ δ ⁡ ( t) ω. I_{\omega,\delta}(t)=\oint_{\delta(t)}\omega. |  |

Basic properties of Abelian integrals can be found in [1]. We will need the following ones. First, Abelian integral depends not on δ \delta itself but on its class of homology [δ] ∈ H 1 ( { H = t }, ℤ) [\delta]\in H_{1}(\{H=t\},{\mathbb{Z}}) only. Also, the Abelian integral corresponding to a form ω \omega is identically zero if ω = f ​ d ​ H + d ​ g \omega=fdH+dg, i.e. Abelian integrals depend in fact on the relative cohomology class of [d ​ ω] ∈ Λ 1 / d ​ H ∧ Λ 0 + d ​ Λ 0 [d\omega]\in\Lambda^{1}/dH\land\Lambda^{0}+d\Lambda^{0} only. This quotient module – the so-called Petrov module – is a ℂ ⁡ [t] \mathbb{C}[t] -module with respect to a standard multiplication t ⁡ [ω] = [H ⁡ ( x, y) ​ ω] t[\omega]=[H(x,y)\omega].

Second, the Abelian integrals are holomorphic multivalued functions of a complex variable t t branching at the critical values of H H only (for H H regular at infinity). So the space of all Abelian integrals is also a ℂ ⁡ [t] \mathbb{C}[t] -module with respect to a natural multiplication by t t.

We will prove that these two modules coincide for a regular at infinity polynomial H ⁡ ( x, y) H(x,y). We prove existence of the corresponding Picard-Fuchs system using this isomorphism, and find out some of its properties.

## 2 Nondegeneracy of the principal determinant

Here we prove that the homogeneous forms generating the ℂ ⁡ [t] \mathbb{C}[t] -module Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1}, also generate the first cohomology group of a generic level curve of H H. Note that this ℂ ⁡ [t] \mathbb{C}[t] -module is isomorphic to ℂ ⁡ [x, y] / ⟨ H x, H y ⟩ \mathbb{C}[x,y]/\left<H_{x},H_{y}\right>. Indeed, Q ​ d ​ x ∧ d ​ y = R ​ d ​ x ∧ d ​ y + ( H x ​ d ​ x + H y ​ d ​ y) ∧ ( A ​ d ​ x + B ​ d ​ y) Qdx\land dy=Rdx\land dy+(H_{x}dx+H_{y}dy)\land(Adx+Bdy) is equivalent to Q = R + B ​ H x − A ​ H y Q=R+BH_{x}-AH_{y}.

Recall that nonsingular level curves of a regular at infinity polynomial H H of degree n + 1 n+1 carry μ = n 2 \mu=n^{2} vanishing cycles δ j ​ ( t) \delta_{j}(t) that generate the whole first homology group of all regular curves { H = t } \{H=t\} [1, 5]. For any collection of μ \mu polynomial 1-forms ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} the period matrix X ω ​ ( t) X_{\omega}(t) formed by integrals of ω i \omega_{i} over δ j \delta_{j} (integrals of the same form occur in the same row, the same cycle corresponds to entries of the same column) has the same monodromy. The monodromy transformations act on X ⁡ ( t) X(t) as multiplications from the right by constant monodromy matrices that are unimodular by virtue of Picard–Lefschetz formulas [1]. Thus det X ⁡ ( t) \det X(t) is a single-valued function that must have zeros at all critical values t = t j t=t_{j}, j = 1, …, μ j=1,\dots,\mu, counting multiplicities, since the columns corresponding to the cycles vanishing at t j t_{j} become zero at t j t_{j} (we use the fact that to any critical value of multiplicity ν \nu correspond ν \nu linearly independent cycles vanishing at this critical value). As the growth of X X at infinity is at most polynomial, det X ⁡ ( t) \det X(t) is a polynomial divisible by Δ H ​ ( t) = ∏ j = 1 μ ( t − t j) \Delta_{H}(t)=\prod_{j=1}^{\mu}(t-t_{j}).

###### Lemma 1 (cf. with [5], Lemma 2.2)

If the 2 2 -forms d ​ ω i d\omega_{i} generate Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1} and

 | ∑ i = 1 μ deg ⁡ ω i = μ ​ deg ⁡ H, \sum_{i=1}^{\mu}\deg\omega_{i}=\mu\deg H, |  |

then det X ω ​ ( t) = c ⁡ ( t − t 1) ​ … ​ ( t − t μ) \det X_{\omega}(t)=c(t-t_{1})\dots(t-t_{\mu}) with c ≠ 0 c\neq 0 (some t i t_{i} may coincide).

The constant c c depends both on the choice of ω i \omega_{i} and on the choice of the cycles δ j ​ ( t) \delta_{j}(t). Its actual calculation is a difficult task, see [8].

Remark. The condition on the degrees of the forms in the Lemma 1 is automatically satisfied if the Hamiltonian H ⁡ ( x, y) H(x,y) and the forms d ​ ω i d\omega_{i} are homogeneous, see [1]. For non-homogeneous Hamiltonian this condition is essential. Among other things, this condition implies that the highest homogeneous parts ω ^ i \widehat{\omega}_{i} of d ​ ω i d\omega_{i} form a basis of Λ 2 / d ​ H ^ ∧ Λ 1 \Lambda^{2}/d{\widehat{H}}\land\Lambda^{1}. Vice versa, any monomial basis of Λ 2 / d ​ H ^ ∧ Λ 1 \Lambda^{2}/d{\widehat{H}}\land\Lambda^{1} is a basis of Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1} satisfying this condition (and this is a standard way to get a basis of Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1}).

The proof is based on the calculation of the “principal term” of the asymptotic of X ⁡ ( t) X(t) at infinity.

###### Lemma 2

For any collection of polynomial 1-forms ω i \omega_{i} the period matrix X ω ​ ( t) X_{\omega}(t) admits a converging expansion

 | X ω ( t) = t D C ( t), C ( t) = ∑ k = 0 ∞ C k t − k / ( n + 1), X_{\omega}(t)=t^{D}C(t),\qquad C(t)=\sum_{k=0}^{\infty}C_{k}t^{-k/(n+1)}, |  | (2.1) |

where D D is the diagonal matrix with the entries d i = deg ⁡ ω i / ( n + 1) d_{i}=\deg\omega_{i}/(n+1), C 0, C 1, … C_{0},C_{1},\dots are constant matrices and C 0 = C ⁡ ( ∞) C_{0}=C(\infty) is the matrix of integrals of the highest homogeneous parts ω ^ i \widehat{\omega}_{i} of forms ω i \omega_{i} over vanishing cycles lying on the level curve { H ^ = 1 } \{{\widehat{H}}=1\}.

Proof of Lemma 2. The level curve { H ( x, y) = t } \{H(x,y)=t\} in the variables x = t 1 / ( n + 1) ​ x ^ x=t^{1/(n+1)}\widehat{x}, y = t 1 / ( n + 1) ​ y ^ y=t^{1/(n+1)}\widehat{y} becomes a family of the curves

 | H ^ ( x ^, y ^) + t − 1 / ( n + 1) H n ( x ^, y ^) + ⋯ = 1, {\widehat{H}}(\widehat{x},\widehat{y})+t^{-1/(n+1)}H_{n}(\widehat{x},\widehat{y})+\cdots=1, |  |

where the left hand side is a polynomial in x ^, y ^ \widehat{x},\widehat{y} and t − 1 / ( n + 1) t^{-1/(n+1)}. In other words, we have an analytic in t − 1 / ( n + 1) t^{-1/(n+1)} perturbation of the limit curve { H ^ ( x ^, y ^) = 1 } ⊂ ℂ 2 \{{\widehat{H}}(\widehat{x},\widehat{y})=1\}\subset{\mathbb{C}}^{2} that is nonsingular (since H ^ {\widehat{H}} has no multiple factors). Integrals of any (constant or analytic in t − 1 / ( n + 1) t^{-1/(n+1)}) 1-form over any continuous family of cycles on such family will be also analytic in t − 1 / ( n + 1) t^{-1/(n+1)}.

The forms ω i \omega_{i} after rescaling become t d i ( θ i + t − 1 / ( n + 1) η i) t^{d_{i}}(\theta_{i}+t^{-1/(n+1)}\eta_{i}), where d i = deg ⁡ ω i / ( n + 1) d_{i}={\deg\omega_{i}/(n+1)}, θ i \theta_{i} is a new independent of t t homogeneous polynomial form (corresponding to the highest homogeneous part ω ^ i \widehat{\omega}_{i} of ω i \omega_{i}) and η i \eta_{i} is another polynomial form. Therefore the integrals of ω i \omega_{i} over cycles δ j ​ ( t) \delta_{j}(t) on the level curves { H = t } \{H=t\} can be expanded in the converging series in t − 1 / ( n + 1) t^{-1/(n+1)} of the form

 | ∮ δ j ​ ( t) ω i = t d i ( c 0, i ​ j + c 1, i ​ j t − 1 / ( n + 1) + ⋯), \oint_{\delta_{j}(t)}\omega_{i}=t^{d_{i}}(c_{0,ij}+c_{1,ij}t^{-1/(n+1)}+\cdots), |  |

if c 0, i ​ j c_{0,ij} is the integral of ω ^ i \widehat{\omega}_{i} over the cycle δ j ⊂ { H ^ = 1 } \delta_{j}\subset\{{\widehat{H}}=1\}. □

Remark. The representation ( 2.1) is unique only if we fix the diagonal matrix D D. Otherwise the power t D t^{D} may itself be expanded as a series in powers of t − 1 / ( n + 1) t^{-1/(n+1)}, thus yielding an essentially different representation.

###### Corollary 1

The determinant of the period matrix X ω ​ ( t) X_{\omega}(t) is a polynomial of degree at most m = m ⁡ ( ω) = tr ⁡ D = ∑ i deg ⁡ ω i / ( n + 1) m=m(\omega)=\tr D=\sum_{i}\deg\omega_{i}/(n+1). If this number is not integer, then automatically det C 0 = 0 \det C_{0}=0 for this choice of the forms, otherwise the leading term t m t^{m} of detX ω ​ ( t) \rm{det}X_{\omega}(t) enters with the coefficient det C 0 \det C_{0}.

Proof of the Lemma 1. Given the assumption on the degrees deg ⁡ ω i \deg\omega_{i}, the determinant det X ω ​ ( t) \det X_{\omega}(t) is a polynomial of degree ≤ μ \leq\mu, and hence (by the divisibility property noted above) it must have a form c ​ ∏ ( t − t j) c\prod(t-t_{j}). We need only to verify that c ≠ 0 c\neq 0, and from the asymptotic formulas we see that c = det C 0 c=\det C_{0}, so our goal is to prove that C 0 C_{0} is a nondegenerate matrix.

The calculation above shows that the matrix X ^ ​ ( t) \widehat{X}(t) of periods of ω ^ i \widehat{\omega}_{i} over the level curves of a homogeneous part H ^ {\widehat{H}}, can be represented as t D ​ C 0 t^{D}C_{0} (the same expansion without inferior terms). Thus if C 0 C_{0} is degenerate, then there exists a linear combination δ ^ ​ ( t) = ∑ 1 μ r j ​ δ j ​ ( t) \widehat{\delta}(t)=\sum_{1}^{\mu}r_{j}\delta_{j}(t), r j ∈ ℂ r_{j}\in{\mathbb{C}}, of vanishing cycles on the level curves of H ^ {\widehat{H}}, such that integrals of all forms ω ^ i \widehat{\omega}_{i} over the cycle δ ^ ​ ( t) \widehat{\delta}(t) are identically zeros.

Take any polynomial 2-form d ​ ω d\omega. Since the forms d ​ ω ^ i d\widehat{\omega}_{i} form a basis of Λ 2 / d ​ H ^ ∧ Λ 1 \Lambda^{2}/d{\widehat{H}}\land\Lambda^{1}, the form d ​ ω d\omega can be divided out by d ​ H ^ d\widehat{H} with remainder in the span of d ​ ω ^ i d\widehat{\omega}_{i}, i.e.,

 | d ​ ω = d ​ H ^ ∧ η + ∑ 1 μ c i ​ d ​ ω ^ i, c i ∈ ℂ, d\omega=d{\widehat{H}}\land\eta+\sum_{1}^{\mu}c_{i}d\widehat{\omega}_{i},\qquad c_{i}\in{\mathbb{C}}, |  |

where η \eta is a suitable polynomial 1-form.

This representation is not unique. However, since H H is regular at infinity, one can construct such representation with degree of η \eta being less than deg ⁡ ω \deg\omega (in fact, less or equal to deg ⁡ ω − deg ⁡ H \deg\omega-\deg H, see [18]).

Recall that the derivative of an Abelian integral of a form ω \omega with respect to t t is again an Abelian integral of the Gelfand-Leray residue θ = d ​ ω d ​ H \theta=\frac{d\omega}{dH} of the form ω \omega:

 | d d ​ t ​ ∮ δ ⁡ ( t) ω = ∮ δ ⁡ ( t) θ, \frac{d}{dt}\oint_{\delta(t)}\omega=\oint_{\delta(t)}\theta, |  |

if d ​ H ∧ θ = d ​ ω dH\land\theta=d\omega.

Return to the division with remainder of the form d ​ ω d\omega by d ​ H ^ d{\widehat{H}}. Integrating over the cycle δ ^ ​ ( t) \widehat{\delta}(t) and using the Gelfand–Leray formula, we see that

 | d d ​ t ​ ∮ δ ^ ​ ( t) ω = ∮ δ ^ ​ ( t) η, \frac{d}{dt}\oint_{\widehat{\delta}(t)}\omega=\oint_{\widehat{\delta}(t)}\eta, |  |

since integrals of d ​ ω ^ i d ​ H ^ \frac{d\widehat{\omega}_{i}}{d{\widehat{H}}} over δ ^ ​ ( t) \widehat{\delta}(t) all vanish. In other words, the derivative of any Abelian integral of a polynomial form over the cycle δ ^ ​ ( t) \widehat{\delta}(t) is again an Abelian integral of a polynomial form. Since the cycle δ ^ ​ ( t) \widehat{\delta}(t) is also vanishing at t = 0 t=0 (recall that we deal with the homogeneous case and all δ i ​ ( t) \delta_{i}(t) vanish at the same value t = 0 t=0), the limit of ∮ δ ^ ​ ( t) η \oint_{\widehat{\delta}(t)}\eta is zero for any polynomial form η \eta as t → 0 t\to 0.

As the Gelfand–Leray derivative η \eta is a polynomial form of smaller degree, the above argument can be repeated, showing that some derivative of the initial integral ∮ δ ^ ​ ( t) ω \oint_{\widehat{\delta}(t)}\omega is zero. Since the integral itself and all its derivatives tend to zero as t → 0 t\to 0, we conclude that the initial Abelian integral is identically zero. Since ω \omega was arbitrary, this proves that integrals of all polynomial forms over the cycle δ ^ ​ ( t) \widehat{\delta}(t) are identically zeros.

But this is clearly impossible unless δ ^ ≡ 0 \widehat{\delta}\equiv 0 in H 1 ( { H ^ = 1 }, ℂ) H_{1}(\{{\widehat{H}}=1\},\mathbb{C}). The shortest way to show this is to refer to [1], where the following statement is proved.

###### Lemma 3 ( [1])

For an isolated singularity with Milnor number μ \mu one can always construct μ \mu holomorphic 1-forms θ 1, …, θ μ \theta_{1},\dots,\theta_{\mu} such that the period matrix X θ ​ ( t) X_{\theta}(t) (integrals of ω i \omega_{i} over all vanishing cycles) will have the determinant det X θ ​ ( t) = t μ + ⋯ \det X_{\theta}(t)=t^{\mu}+\cdots. □

This lemma can be applied to the homogeneous germ H ^ {\widehat{H}} and the forms in [1] are in fact constructed polynomial (of course, of sufficiently high degrees). Namely, for an arbitrary nonzero cycle (in particular, for δ ^ ​ ( t) \widehat{\delta}(t)) a suitable linear combination of θ i \theta_{i} has integral not identically zero, which contradicts the choice of δ ^ ​ ( t) \widehat{\delta}(t). □

Remark. The assertion of the above Lemma is by far much stronger than required to complete the proof: it would be sufficient to find just one polynomial form in ℂ 2 \mathbb{C}^{2} such that the integral of its restriction to the affine curve { H ^ = t } \{{\widehat{H}}=t\} along δ ^ ​ ( t) ≠ 0 \widehat{\delta}(t)\neq 0 would be non-zero. This can be done using the fact that { H ^ = 1 } \{{\widehat{H}}=1\} is a Stein manifold, and therefore each element of its cohomology group can be realized as a restriction of a holomorphic one-form on ℂ 2 {\mathbb{C}}^{2}. More exact, let ω \omega be a holomorphic form on { H ^ = 1 } \{{\widehat{H}}=1\} such that its integral along δ ^ \widehat{\delta} is nonzero. One can find a holomorphic form ω ~ \tilde{\omega} on ℂ 2 \mathbb{C}^{2} which restriction to { H ^ = 1 } \{{\widehat{H}}=1\} is cohomologous to ω \omega. Since the cycles generating H 1 ( { H ^ = 1 }, ℂ) H_{1}(\{{\widehat{H}}=1\},{\mathbb{C}}) have compact representatives, a polynomial one-form sufficiently close approximating ω ~ \tilde{\omega} on a sufficiently big compact will also produce nonzero integral along δ ^ ​ ( t) \widehat{\delta}(t) (since analytic in ℂ 2 \mathbb{C}^{2} coefficients of the form ω ~ \tilde{\omega} can be uniformly approximated by polynomials on any compact set).

## 3 Module of the Abelian integrals

Now, after Lemma 1 is proved, we can immediately prove that integrals of the forms d ​ ω i d\omega_{i} generate over ℂ ⁡ [t] {\mathbb{C}}[t] the entire module of Abelian integrals. The proof appears in [5] and is a straightforward application of the Cramer rule. We reproduce this proof here for reader’s convenience.

###### Proposition 1 (Gavrilov theorem [5])

Let ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} be one-forms such that ∑ i = 1 μ deg ⁡ ω i = μ ​ deg ⁡ H \sum_{i=1}^{\mu}\deg\omega_{i}=\mu\deg H, and suppose that the polynomials d ​ ω i d ​ x ∧ d ​ y \frac{d\omega_{i}}{dx\land dy} are linearly independent modulo the gradient ideal < H x, H y > <H_{x},H_{y}> in ℂ ⁡ [x, y] {\mathbb{C}}[x,y].

Then integral of any polynomial 1 1 -form ω \omega can be represented as a linear combination of integrals of the forms ω i \omega_{i} with polynomial in t t coefficients: for any cycle δ ⁡ ( t) \delta(t) on the level curve { H = t } \{H=t\}

 | ∮ δ ⁡ ( t) ω = ∑ i = 1 μ p i ​ ( t) ​ ∮ δ ⁡ ( t) ω i, p i ​ ( t) ∈ ℂ ⁡ [t], ( n + 1) ​ deg ⁡ p i + deg ⁡ ω i ≤ deg ⁡ ω. \oint_{\delta(t)}\omega=\sum_{i=1}^{\mu}p_{i}(t)\oint_{\delta(t)}\omega_{i},\quad p_{i}(t)\in{\mathbb{C}}[t],\ (n+1)\deg p_{i}+\deg\omega_{i}\leq\deg\omega. |  | (3.1) |

Remark. The condition on degrees is again essential: if H ⁡ ( x, y) H(x,y) is not homogeneous, then not every basis of monomial forms of Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1} generates the Petrov module. A (more transparent weight-homogeneous) example is H = y 2 + x 4 − x 2 H=y^{2}+x^{4}-x^{2} and the set of monomial forms d ​ x ∧ d ​ y, x 2 ​ d ​ x ∧ d ​ y, x 5 ​ d ​ x ∧ d ​ y dx\land dy,x^{2}dx\land dy,x^{5}dx\land dy. However,for homogeneous H H and homogeneous ω i \omega_{i} this condition is satisfied automatically, see [1].

Proof. We look for a tuple of real functions p i ​ ( t) p_{i}(t) such that identically over t t and for any vanishing cycle δ ​ ( t) = δ j ​ ( t) \delta(t)=\delta_{j}(t) the equality ( 3.1) holds. These equations for each t t form a linear nonhomogeneous system with the matrix of coefficients X ⁡ ( t) X(t) being the period matrix ∮ δ j ω i \oint_{\delta_{j}}\omega_{i} and the column of right hand sides being periods of the form ω \omega.

Since the matrix X ⁡ ( t) X(t) is nondegenerate (for all t ≠ t j t\neq t_{j}), the solution of this system can be found by the Cramer rule: each p i p_{i} is a ratio of two determinants. The denominator is det X ⁡ ( t) = c ​ ∏ j ( t − t j) \det X(t)=c\prod_{j}(t-t_{j}), whereas the numerator is the determinant of the period matrix obtained by replacing ω i \omega_{i} by ω \omega. By the same arguments as in the beginning of § 2, the numerator should be a polynomial divisible by ∏ 1 μ ( t − t j) \prod_{1}^{\mu}(t-t_{j}), hence the inequality c ≠ 0 c\neq 0 ensures that the ratio is in fact a polynomial function of t t. To estimate the degree of the nominator, we use Corollary to Lemma 2: it is no greater than deg det X ( t) + deg ⁡ ω − deg ⁡ ω i n + 1 \deg\det X(t)+\frac{\deg\omega-\deg\omega_{i}}{n+1}. Therefore deg ⁡ p i ≤ ( deg ⁡ ω − deg ⁡ ω i) / ( n + 1) \deg p_{i}\leq(\deg\omega-\deg\omega_{i})/(n+1). □

Remark. The uniqueness of the representation ( 3.1) follows from a theorem by Gavrilov (see [5, 6]) that a polynomial 1-form with all zero periods must be necessary a ⁡ ( x, y) ​ d ​ H + d ​ b ​ ( x, y) a(x,y)dH+db(x,y), where a, b a,b appropriate polynomials, provided that the Hamiltonian H ⁡ ( x, y) H(x,y) is regular at infinity (the conditions in [5] are even weaker). This result is a generalization of an earlier result of Ilyashenko [10].

The local counterpart of Proposition 1 claims that the ring of relative cohomology is finitely generated as a C ​ { t } C\{t\} -module (Brieskorn–Sebastiani [3, 22]).

## 4 Derivation of the irredundant Picard–Fuchs system and its elementary properties

Let ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} be polynomial 1-forms as in Proposition 1, i.e., they satisfy the condition ∑ 1 μ deg ⁡ ω i = μ ​ deg ⁡ H \sum_{1}^{\mu}\deg\omega_{i}=\mu\deg H and their differentials d ​ ω i d\omega_{i} generate Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1}.

The second assumption guarantees that we may divide out the 2-forms H ⁡ ( x, y) ​ d ​ ω i H(x,y)d\omega_{i} for all i = 1, …, μ i=1,\dots,\mu, obtaining

 | H d ω i = d H ∧ η i + ∑ j = 1 μ a i ​ j d ω j, i = 1, …, μ, H\,d\omega_{i}=dH\land\eta_{i}+\sum_{j=1}^{\mu}a_{ij}d\omega_{j},\qquad i=1,\dots,\mu, |  | (4.1) |

with appropriate polynomial forms η i \eta_{i} of degrees deg ⁡ η i ≤ deg ⁡ ω i ≤ 2 ​ n \deg\eta_{i}\leq\deg\omega_{i}\leq 2n. This by the Gelfand–Leray formula implies that for any cycle δ ⁡ ( t) \delta(t)

 | ( t − A) ​ I ˙ ​ ( t) = J ⁡ ( t), where I = ( ∮ δ ⁡ ( t) ω 1, …, ∮ δ ⁡ ( t) ω μ) T, J = ( ∮ δ ⁡ ( t) η 1, …, ∮ δ ⁡ ( t) η μ) T. (t-A)\dot{I}(t)=J(t),\quad{\rm where}\quad I=(\oint_{\delta(t)}\omega_{1},...,\oint_{\delta(t)}\omega_{\mu})^{T},\quad J=(\oint_{\delta(t)}\eta_{1},\dots,\oint_{\delta(t)}\eta_{\mu})^{T}. |  |

Here occurs the difference with the computations from [18]: we cannot claim that the integrals J i J_{i} are linear combinations of I j I_{j}, since the linear span of the forms d ​ ω i d\omega_{i} does not contain all 2 2 -forms of degrees ≤ 2 ​ n \leq 2n (in [18] this decomposition was written for all monomials of degree ≤ 2 ​ n \leq 2n which resulted in a hypergeometric system of doubled size with a Fuchsian singularity at infinity).

However we can use the decomposition provided by Proposition 1 and write

 | J ⁡ ( t) = B ⁡ ( t) ​ I ​ ( t), B ⁡ ( t) = B 0 + t ​ B 1, J(t)=B(t)I(t),\qquad B(t)=B_{0}+tB_{1}, |  |

i.e B ⁡ ( t) B(t) is a matrix polynomial of degree ≤ 1 \leq 1.

This proves the following result.

###### Theorem 1

The period matrix X ⁡ ( t) X(t) of the forms ω i \omega_{i} satisfying the above three conditions, is a nondegenerate solution to the system of first order linear ordinary differential equations

 | ( t − A) ​ X ˙ ​ ( t) = ( B 0 + B 1 ​ t) ​ X ​ ( t), A, B 0, B 1 ∈ Mat μ × μ ​ ( ℂ). (t-A)\dot{X}(t)=(B_{0}+B_{1}t)X(t),\qquad A,B_{0},B_{1}\in\rm{Mat}_{\mu\times\mu}({\mathbb{C}}). |  | (4.2) |

Some properties of the matrices A, B 0, B 1 A,B_{0},B_{1} can be established by a simple inspection. First, after identification of Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1} with ℂ ⁡ [x, y] / < H x, H y > {\mathbb{C}}[x,y]/<H_{x},H_{y}>, the equation ( 4.1) means that A A is a matrix of multiplication by H H in ℂ ⁡ [x, y] / < H x, H y > {\mathbb{C}}[x,y]/<H_{x},H_{y}>.

Suppose for a moment that H ⁡ ( x, y) H(x,y) has μ \mu simple pairwise different critical values. Let ( x j, y j) (x_{j},y_{j}), j = 1, …, μ j=1,\dots,\mu be critical points of H H. Denote by 𝐯 j \mathbf{v}_{j} the μ \mu -dimensional vector, whose components are the coefficients d ​ ω i d ​ x ∧ d ​ y \frac{d\omega_{i}}{dx\land dy} evaluated at the point ( x j, y j) (x_{j},y_{j}). Such vectors form a basis in ℂ μ {\mathbb{C}}^{\mu} by the second condition imposed on the forms. For example, if the coefficients of ω i \omega_{i} are monomials x α ​ y β x^{\alpha}y^{\beta} with 0 ≤ α, β ≤ n − 1 0\leq\alpha,\beta\leq n-1, then together 𝐯 j \mathbf{v}_{j}, j = 1, …, μ j=1,\dots,\mu form a two-dimensional analog of the Vandermonde matrix.

###### Proposition 2

The matrix A A is diagonalizable, its eigenvalues are critical values of H H whereas the eigenvector corresponding to the critical value t j t_{j} is 𝐯 j \mathbf{v}_{j}.

Proof. The right hand side of the expression ( 4.2) has j j -th column zero if evaluated at the point t = t j t=t_{j}, since the corresponding cycle vanishes. The corresponding column of the matrix X ˙ ​ ( t j) \dot{X}(t_{j}) is therefore in the kernel of ( t j − A) (t_{j}-A). Since the number of critical values is equal to the dimension of the system (recall we are dealing with the irredundant case), this proves the assertion about diagonalizability and the spectrum of A A.

To complete the proof we need only to compute the derivatives I ˙ i ​ ( t j) \dot{I}_{i}(t_{j}). The Gelfand–Leray derivative d ​ ω i / d ​ H d\omega_{i}/dH has zero residues on all nonsingular level curves, but restricted on { H = t j } \{H=t_{j}\} it has a nontrivial residue. This can be immediately seen for the normal form when H ⁡ ( x, y) = y 2 − x 2 H(x,y)=y^{2}-x^{2} (note that all considerations are local, so one can use the Morse normal form near the critical point ( x j, y j) (x_{j},y_{j})). Indeed, if d ​ ω = f ⁡ ( x, y) ​ d ​ x ∧ d ​ y d\omega=f(x,y)\,dx\land dy, then d ​ ω / d ​ H d\omega/dH can be chosen as 1 2 ​ f ​ d ​ x / y \frac{1}{2}f\,dx/y, and its restriction on (one of the two smooth branches of) the curve H = 0 H=0, say, y = x y=x, yields a meromorphic 1-form 1 2 ​ f ​ ( x, x) ​ d ​ x / x \frac{1}{2}f(x,x)\,dx/x, whose residue (integral over a small loop around x = 0 x=0) is π ​ i ​ f ​ ( 0, 0) \pi if(0,0). Returning to the initial problem, we see that ∮ H = t j d ​ ω i d ​ H \oint_{H=t_{j}}\frac{d\omega_{i}}{dH} differs from π ​ d ​ ω i d ​ x ∧ d ​ y ​ ( x j, y j) \pi\frac{d\omega_{i}}{dx\land dy}{(x_{j},y_{j})} by a nonzero factor, the Hessian of the transformation taking H H into the Morse form as above. Since this nonzero factor is common for all forms, we see that the vector of residues ( I ˙ 1 ​ ( t j), …, I ˙ μ ​ ( t j)) (\dot{I}_{1}(t_{j}),\dots,\dot{I}_{\mu}(t_{j})) is proportional to the vector 𝐯 j \mathbf{v}_{j} whose coordinates are d ​ ω i d ​ x ∧ d ​ y ​ ( x j, y j) \frac{d\omega_{i}}{dx\land dy}{(x_{j},y_{j})}, i = 1, …, μ i=1,\dots,\mu. □

By continuity one can conclude that

###### Corollary 2

For any regular at infinity Hamiltonian H ⁡ ( x, y) H(x,y) its critical values t j t_{j} counted with multiplicities are the eigenvalues of the matrix A A, and the vectors 𝐯 j \mathbf{v}_{j} are eigenvectors of A A

The matrices B 0 B_{0}, B 1 B_{1} in principle can be computed by evaluating the expansion for X ⁡ ( t) X(t) at infinity, see Lemma 2. One can guess some of their properties just by taking d ​ ω i d\omega_{i} homogeneous and of nondecreasing degree.

###### Proposition 3

Let d ​ ω i d\omega_{i} be homogeneous and deg ⁡ d ​ ω i ≤ deg ⁡ d ​ ω j \deg d\omega_{i}\leq\deg d\omega_{j} whenever 1 ≤ i < j ≤ μ 1\leq i<j\leq\mu. Then B 0 B_{0} and B 1 B_{1} are both lower triangular. Moreover, the diagonal entries of B 0 B_{0} are just the degrees of the forms divided by deg ⁡ H \deg H, and B 1 2 = 0 B_{1}^{2}=0

Proof. This follows from the careful analysis of the forms η i \eta_{i} in ( 4.2). Indeed, deg ⁡ η i ≤ deg ⁡ ω i \deg\eta_{i}\leq\deg\omega_{i}, so in the decomposition of η i \eta_{i} provided by Proposition 1 appear only forms of degree not greater than d ​ ω i d\omega_{i}. Moreover, it is easy to see (using Euler identity) that the highest homogeneous term of η i \eta_{i} is equivalent in the Petrov module to deg ⁡ ω i deg ⁡ H ​ d ​ ω i \frac{\deg\omega_{i}}{\deg H}d\omega_{i}, see [18]. This together implies that B 0 B_{0} is lower triangular with prescribed diagonal elements. From the same estimates of the Proposition 1 follows that entries ( B 1) i ​ j (B_{1})_{ij} of the matrix B 1 B_{1} can be nonzero only if deg ⁡ ω i − deg ⁡ ω j ≥ deg ⁡ H \deg\omega_{i}-\deg\omega_{j}\geq\deg H, so B 1 B_{1} is lower triangular and, since max i ​ j ⁡ ( deg ⁡ ω i − deg ⁡ ω j) = 2 ​ deg ​ H − 4 < 2 ​ deg ​ H \max_{ij}(\deg\omega_{i}-\deg\omega_{j})=2\deg H-4<2\deg H, already B 1 2 = 0 B_{1}^{2}=0.

###### Corollary 3

The matrix B 0 + t ​ B 1 B_{0}+tB_{1} is invertible for all t t.

## 5 Picard-Fuchs system can be non-Fuchsian

From the analysis above follows that all finite singular points of the system ( 4.2) coincide with the critical values of H H. Moreover, all finite singularities turn out to be Fuchsian for Morse-plus H ⁡ ( x, y) H(x,y) (which, by definition, means that the matrix ( t − A) − 1 ​ ( B 0 + t ​ B 1) (t-A)^{-1}(B_{0}+tB_{1}) of coefficients of the system of the Theorem 1 has poles of the first order). Indeed, the Picard-Fuchs system has a Fuchsian singularity at λ i \lambda_{i} if and only if the matrix ( t − A) − 1 (t-A)^{-1} has a simple pole at λ i \lambda_{i} (due to invertibility of B 0 + t ​ B 1 B_{0}+tB_{1} for all t t). This is equivalent to the diagonalizability of the matrix A A, so is true for Morse-plus Hamiltonian H ⁡ ( x, y) H(x,y).

For a general regular at infinity H ⁡ ( x, y) H(x,y) the finite singular points can be non-Fuchsian. Indeed, the matrix A A is the matrix of multiplication by f f in ℂ ⁡ [x, y] / < H x, H y > {\mathbb{C}}[x,y]/<H_{x},H_{y}>, and this ring is a direct sum over all critical points of H ⁡ ( x, y) H(x,y) of the corresponding local rings ( [4, Max Noether’s A ​ F + B ​ G AF+BG Theorem]). It follows that A A is diagonalizable if and only if the operator of multiplication by H H is diagonalizable in each local ring. This is true if and only if the germ of H ⁡ ( x, y) H(x,y) is (equivalent to) quasi-homogeneous, see [1], so fails in general.

Also, unless B 1 = 0 B_{1}=0, the singular point at infinity is non-Fuchsian. This is also possible, see below an example.

It is easy to see that the Picard-Fuchs system of the Theorem 4 is equivalent to a Fuchsian one. Indeed, due to the regularity at infinity assumption the monodromy of the irredundant system corresponding to a circle around infinity is diagonalizable, so this equivalence is a particular case of a positive solution (essentially due to Plemelj) of the Riemann-Hilbert problem in the case of diagonalizability of one of the local monodromies, see [2]. Moreover, in [12] it is proved, modulo a conjecture due to Bolibruch, that this system is equivalent to a Fuchsian one for any H ⁡ ( x, y) H(x,y), even degenerate ones. However, the equivalent system will not have the fairly simple form of Theorem 4.

Here is an example of a Hamiltonian with a nonzero matrix B 1 B_{1}.

Example. Consider the Hamiltonian H ⁡ ( x, y) = x 5 + y 5 + x 2 ​ y 2 + a ​ x + b ​ y H(x,y)=x^{5}+y^{5}+x^{2}y^{2}+ax+by. For a suitable choice of a, b a,b this Hamiltonian is Morse-plus. As a basis of the quotient Λ 2 / d ​ H ∧ Λ 1 \Lambda^{2}/dH\land\Lambda^{1} we take the forms d ​ ω i ​ j = x i ​ y j ​ d ​ x ∧ d ​ y d\omega_{ij}=x^{i}y^{j}dx\land dy, 0 ≤ i, j ≤ 3 0\leq i,j\leq 3. We will show that any form η \eta defined by the decomposition

 | H ​ d ​ ω 33 = d ​ H ∧ η + ∑ 0 ≤ i, j ≤ 3 a i ​ j ​ d ​ ω i ​ j Hd\omega_{33}=dH\land\eta+\sum_{0\leq i,j\leq 3}a_{ij}d\omega_{ij} |  |

is equivalent to 1 175 ​ t ​ ω 00 + ∑ 0 ≤ i, j ≤ 3 β i ​ j ​ ω i ​ j \frac{1}{175}t\omega_{00}+\sum_{0\leq i,j\leq 3}\beta_{ij}\omega_{ij} in the Petrov module corresponding to H ⁡ ( x, y) H(x,y), with β i ​ j \beta_{ij} being constant (so the matrix B 1 B_{1} has a nonzero entry equal to 1 175 \frac{1}{175}).

Although η \eta is defined non-uniquely by the Gelfand-Leray formula above, its Abelian integrals do (and therefore its class in the Petrov module). So we can use any η \eta we like. Applying the “division with remainder” algorithm of [18] we find the first terms of a form η \eta solving the equation above:

 | η = 1 5 ​ ( x 3 ​ y 3 ​ ( x ​ d ​ y − y ​ d ​ x) + ( 1 175 ​ x ​ y 5 ​ d ​ y − 6 175 ​ x 5 ​ y ​ d ​ x) + η 1 = CLOSE \displaystyle\eta=\frac{1}{5}(x^{3}y^{3}(xdy-ydx)+(\frac{1}{175}xy^{5}dy-\frac{6}{175}x^{5}ydx)+\eta_{1}= |  |

 | = x 3 ​ y 3 5 ​ ( x ​ d ​ y − y ​ d ​ x) + y 5 + x 5 175 ​ x ​ d ​ y − d ⁡ ( x 6 ​ y) 175 + η 1, \displaystyle=\frac{x^{3}y^{3}}{5}(xdy-ydx)+\frac{y^{5}+x^{5}}{175}xdy-\frac{d(x^{6}y)}{175}+\eta_{1}, |  |

where by η 1 \eta_{1} we denote forms of degree less than 7 7. It is easy to see that in the Petrov module the first term is equivalent to 8 5 ​ ω 33 \frac{8}{5}\omega_{33} and the second term is equivalent to 1 175 ​ H ​ x ​ d ​ y + 1 175 ​ ( x 5 + y 5 − H) ​ x ​ d ​ y = t ​ 1 175 ​ x ​ d ​ y + η 2 \frac{1}{175}Hxdy+\frac{1}{175}(x^{5}+y^{5}-H)xdy=t\frac{1}{175}xdy+\eta_{2}. Since the degrees of both η 1 \eta_{1} and η 2 \eta_{2} are less than 7 7, the form η 1 + η 2 \eta_{1}+\eta_{2} is equivalent in the ℂ ⁡ [t] {\mathbb{C}}[t] -module of Abelian integrals to a linear combination with constant coefficients of forms ω i ​ j \omega_{ij}, by virtue of estimates of the Corollary to Lemma 2.□

## References

## References

- [1] Arnold V I, Guseĭn-Zade S M and Varchenko A N, Singularities of differentiable maps. Vol. II, Monodromy and asymptotics of integrals, Birkhäuser Boston, Boston MA, 1988.
- [2] Arnold, V I and Ilyashenko Yu S, Ordinary Differential Equations, in the book: Anosov D V and Arnold.V I (Eds.) Dynamical systems 1, Encyclopaedia Math. Sci., 1, Springer, Berlin, 1988.
- [3] Brieskorn E, Die Monodromie der isolierten Singularitäten von Hyperfläschen, Manuscripta Math., 2 (1970), 103–161.
- [4] P. Griffiths and J. Harris, Principles of algebraic geometry, Wiley-Intersci., New York, 1978.
- [5] Gavrilov L, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math. 122 (1998), 571–584.
- [6] —–, Abelian integrals related to Morse polynomials and perturbations of plane Hamiltonian vector fields, Ann. Inst. Fourier 49 (1999), no. 2, 611–652.
- [7] Givental A B, Sturm’s theorem for hyperelliptic integrals, (Russian) Algebra i Analiz 1 (1989), no. 5, 95–102; translation in Leningrad Math. J. 1 no. 5, 1157–1163.
- [8] A. A.Glutsuk and Yu. S. Ilyashenko, An estimate on the number of zeroes of Abelian integrals for special Hamiltonians of arbitrary degree, preprint 2001, arXiv:math.DS/0112156v1.
- [9] Horozov E and Iliev I D, Linear estimate for the number of zeros of Abelian integrals with cubic Hamiltonians, Nonlinearity 11 (1998), no. 6, 1521–1537.
- [10] Ilyashenko Yu, Appearance of limit cycles in perturbation of the equation d ​ w d ​ z = − R z R w \frac{dw}{dz}=-\frac{R_{z}}{R_{w}} where R ⁡ ( z, w) R(z,w) is a polynomial, USSR Mat. Sb. (N.S.) 78 (1969), 360–373
- [11] Ilyashenko Yu and Yakovenko S, Counting real zeros of analytic functions satisfying linear ordinary differential equations, Journal of Differential equations 126 (1996), no. 1, 87-105.
- [12] Kostov V, Gauss-Manin system of polynomials of two variables can be made Fuchsian, Geometry, Integrability and Quantization, Sept 1-10, 1999, Varna, Bulgaria.
- [13] Khovanskii A, Real analytic manifolds with the property of finiteness, and complex Abelian integrals, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 40–50 (Russian)
- [14] Novikov D, Systems of linear ordinary differential equations with bounded coefficients may have very oscillating solutions, Proc. Amer. Math. Soc., 129 (2001), 3753-3755
- [15] Novikov D and Yakovenko S, Tangential Hilbert problem for perturbations of hyperelliptic Hamiltonian systems, Electronic Res. Announc. AMS, 5 (1999), 55–65
- [16] —–, —–, Trajectories of polynomial vector fields and ascending chains of polynomial ideals, Ann. Inst. Fourier 49 (1999), no. 2, 563–609.
- [17] —–, —–, Meandering of trajectories of polynomial vector fields in the affine n n -space. Proceedings of the Symposium on Planar Vector Fields (Lleida, 1996). Publ. Mat. 41 (1997), no. 1, 223–242.
- [18] —–,—–, Redundant Picard–Fuchs system for Abelian integrals, to appear in Journal of Differential Equations.
- [19] Pham F, Singularités Des Systèmes Différentiels De Gauss–Manin, Progress in Mathematics, vol. 2, Birkhäuser, Boston, 1979.
- [20] Petrov G, Complex zeros of an elliptic integral, Funktsional. Anal. i Prilozhen. 21 (1987), no. 3, 87–88.
- [21] Roussarie R, Bifurcation of planar vector fields and Hilbert’s sixteenth problem, Progr. Math., 164, Birkhäuser, Basel, 1998.
- [22] Sebastiani M, Preuve d’un conjecture de Brieskorn, Manuscripta Math. 2 (1970), 301–308.
- [23] de la Valleé-Poussin, Sur l’équation différentielle linéaire du second ordre. Détermination d’une intégrale par deux valeurs assignées. Extension aux équations d’ordre n n J. Math. Pure Appl., 8 (1929), 125-144.
- [24] Varchenko A, Estimation of the number of zeros of an Abelian integral depending on a parameter, and limit cycles, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 14–25 (Russian)
- [25] Varchenko A, Critical values and the determinant of periods. (Russian) Uspekhi Mat. Nauk 44 (1989), no. 4(268), 235–236; translation in Russian Math. Surveys 44 (1989), no. 4, 209–210


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:dmitry@math.purdue.edu
