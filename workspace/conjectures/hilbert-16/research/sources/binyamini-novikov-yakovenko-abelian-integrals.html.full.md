<!-- source: https://arxiv.org/html/0808.2952v3 | converted from HTML -->

On the number of zeros of Abelian integrals

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:0808.2952v3 [math.DS] 06 Oct 2009

# On the number of zeros of Abelian integrals Dedication: To Yulij Sergeevich Ilyashenko, who discovered this problem 40 years ago, for his 65th birthday with gratitude and admiration.

A constructive solution of the Infinitesimal Hilbert Sixteenth Problem

Gal Binyamini Dmitry Novikov Sergei Yakovenko E-mail: [{gal.binyamini, dmitry.novikov, sergei.yakovenko}@weizmann.ac.il][3] Affiliation: Weizmann Institute of Science, Rehovot, Israel Correspondence: Sergei Yakovenko

Posted on August 21, 2008. Revised version Oct 5, 2009.

###### Abstract

We prove that the number of limit cycles generated from nonsingular energy level ovals (periodic trajectories) in a small non-conservative perturbation of a Hamiltonian polynomial vector field on the plane, is bounded by a double exponential of the degree of the fields. This solves the long-standing infinitesimal Hilbert 16th problem.

The proof uses only the fact that Abelian integrals of a given degree are horizontal sections of a regular flat meromorphic connection defined over ℚ {\mathbb{Q}} (the Gauss-Manin connection) with a quasiunipotent monodromy group.

###### Keywords:

Abelian integrals – Fuchsian systems – monodromy – limit cycles.
AMS subject classification: Primary 34C07, 34C08; Secondary 34M10, 34M60, 14Q20, 32S40

## 1 Infinitesimal Hilbert 16th problem

The central result of this paper is an explicit upper bound for the number of limit cycles born from nonsingular (smooth compact) energy level ovals in a non-conservative polynomial perturbation of a polynomial Hamiltonian vector field on the plane. This problem was repeatedly posed in various sources under different names as the weakened, infinitesimal or tangential Hilbert 16th problem. In this introductory section we briefly outline some connections between different problems concerning limit cycles of polynomial vector fields on the plane. Much more complete expositions can be found in the recent surveys Ily 02; Yak 05 and the books Żol 06; IY 08.

### 1.1 Limit cycles born by perturbations of integrable planar vector fields

Limit cycles, *isolated*periodic (compact, nontrivial) trajectories of polynomial vector fields, are one of the most elusive objects of analysis. There are only a handful of tools to establish the (non)existence of such cycles in certain domains, all of them applying to very specific differential equations. D. Hilbert, who included the problem of counting the possible number of limit cycles as the 16th problem in his famous list Hil 00, conjectured implicitly that the problem could be approached by perturbation techniques, first studying vector fields close to those which are “simple” from the point of view of counting their limit cycles. One such natural class is the *integrable fields*which exhibit continuous families of (nonisolated) periodic trajectories (here and below *integrability*means existence of a local or global *first integral*). In PL 57 Petrovskiĭ and Landis attempted to realize this program by a complexification of the problem, but their attempt was not successful Ily 06. Nevertheless, the problem of estimating the number of limit cycles of near-integrable systems became a natural intermediate step towards a possible future solution of the Hilbert problem which still seems to be completely out of reach, see ( Arn 04, Problem 1978-6, pp. 352–363) and, most recently, ( Ily 08, §3.2).

Among the integrable systems the simplest (in many respects) class is that of *Hamiltonian polynomial systems*, vector fields corresponding to a system of autonomous differential equations of the form

 | d ​ x d ​ z = ∂ H ∂ y ​ ( x, y), d ​ y d ​ z = − ∂ H ∂ x ​ ( x, y), \frac{\,\mathrm{d}x}{\,\mathrm{d}z}=\frac{\partial H}{\partial y}(x,y),\qquad\frac{\,\mathrm{d}y}{\,\mathrm{d}z}=-\frac{\partial H}{\partial x}(x,y), |  | (1) |

with a real bivariate polynomial H H called the Hamiltonian; in the Pfaffian form these differential equations can be written as d ​ H = 0 \,\mathrm{d}H=0, and all real level ovals of H H (compact connected components of the level curves of the form { H = t } \{H=t\}) are integral trajectories.

A polynomial perturbation of the Hamiltonian system ( 1) can also be written in the Pfaffian form with a small parameter ε ∈ ( ℝ 1, 0) \varepsilon\in({\mathbb{R}}^{1},0) as follows,

 | d ​ H + ε ​ ω = 0, ω = P ⁡ ( x, y) ​ d ​ x + Q ⁡ ( x, y) ​ d ​ y. \,\mathrm{d}H+\varepsilon\omega=0,\qquad\omega=P(x,y)\,\mathrm{d}x+Q(x,y)\,\mathrm{d}y. |  | (2) |

In general, such perturbations destroy integrability, so that for ε ≠ 0 \varepsilon\neq 0 most integral trajectories will become spirals.

We say that a (smooth) closed oval δ ⊆ { H = t } \delta\subseteq\{H=t\} generates a limit cycle in the perturbation ( 2), if for any sufficiently small annular neighborhood U U of δ \delta one can find arbitrarily small values of the parameter ε \varepsilon such that the corresponding Pfaffian equation exhibits a limit cycle δ ε \delta_{\varepsilon} entirely belonging to U U. If there exists a natural number k ⩾ 1 k\geqslant 1 such that for an arbitrarily narrow U U and an arbitrarily small ε \varepsilon there may coexist k k limit cycles, we say that the oval δ \delta generates ⩾ k \geqslant k limit cycles in the family.

Respectively, we say that an oval δ \delta generates no more than k k limit cycles in perturbation ( 2), k ⩾ 0 k\geqslant 0, if there exists a small annular neighborhood U U of δ \delta on the ( x, y) (x,y) -plane, and a small neighborhood V = ( ℝ 1, 0) V=({\mathbb{R}}^{1},0) of the origin on the parameter axis, such that for any ε ∈ V \varepsilon\in V the foliation defined by the Pfaffian form d ​ H + ε ​ ω \,\mathrm{d}H+\varepsilon\omega, has no more than k k limit cycles in U U. The minimal number k k with this property, denoted by k = k ⁡ ( δ, ω) k=k(\delta;\omega), always exists: one can easily see that for almost all ovals k ⁡ ( δ, ω) = 0 k(\delta;\omega)=0 (the oval is destroyed without generating any limit cycle). In other words, in the sum taken over all smooth ovals of the real level curves { H = const } ⊂ ℝ 2 \{H=\operatorname{const}\}\subset{\mathbb{R}}^{2},

 | 𝒩 ( H, ω) = ∑ δ ⊆ { H = const } k ( δ; ω) ⩽ + ∞ {\mathcal{N}}(H,\omega)=\sum_{\delta\subseteq\{H=\operatorname{const}\}}k(\delta;\omega)\leqslant+\infty |  | (3) |

all but countably many terms mush vanish.

It is well known that k ⁡ ( δ, ω) > 0 k(\delta;\omega)>0 only if the Poincaré integral

 | I = I ⁡ ( δ, ω) = ∮ δ P ​ 𝑑 x + Q ​ 𝑑 y, I=I(\delta,\omega)=\oint_{\delta}P\,\mathrm{d}x+Q\,\mathrm{d}y, |  | (4) |

vanishes (Poincaré–Andronov–Pontryagin criterion ( IY 08, §26A) 1 1 1 For convenience of the reader we give references to the textbook IY 08 whenever possible. References to the original publications can be found in this textbook.). In physical terms, the integral ( 4) is the principal asymptotic term for the dissipation of the energy along one period. The perturbation is called *non-conservative*if I ⁡ ( ⋅, ω) ≢ 0 I(\cdot,\omega)\not\equiv 0. In this case a slight refinement of the Poincaré–Andronov–Pontryagin criterion asserts that k ⁡ ( δ, ω) k(\delta;\omega) does not exceed the multiplicity of the root of the integral I ⁡ ( δ, ω) I(\delta,\omega) as the function of the first argument.

The infinitesimal Hilbert problem requires to *place an upper bound for the number of limit cycles born from nonsingular energy level ovals in non-conservative perturbations*. The answer should depend only on n n, i.e., the bound must be uniform over all Hamiltonians H H of degree 2 2 2 The degrees of the Hamiltonian and the perturbation 1 1 -form are chosen so that both terms in the perturbation ( 2) have the same degree n n. deg ⁡ H ⩽ n + 1 \deg H\leqslant n+1 and polynomial 1 1 -forms ω \omega of degree deg ⁡ ω = max ⁡ ( deg ⁡ P, deg ⁡ Q) ⩽ n \deg\omega=\max(\deg P,\deg Q)\leqslant n. Our main result solves this problem and gives an explicit double exponential upper bound.

###### Theorem 1

The total number of limit cycles 𝒩 ⁡ ( H, ω) {\mathcal{N}}(H,\omega) that can be born from all nonsingular energy level ovals of a Hamiltonian polynomial foliation in a non-conservative perturbation ( 2) of degree ⩽ n \leqslant n, is no greater than 2 2 Poly ⁡ ( n) 2^{2^{\operatorname{\textup{Poly}}(n)}}.

Here the expression Poly ⁡ ( n) = O ⁡ ( n p) \operatorname{\textup{Poly}}(n)=O(n^{p}) stands for an explicit polynomially growing term with the exponent p p not exceeding 61 61.

Besides limit cycles born from nonsingular ovals, limit cycles can be born from separatrix polygons (energy level curves carrying singular points of the Hamiltonian vector field). Theorem 1 does not address the number of these cycles, see Remark 5 below.

### 1.2 Zeros of Abelian integrals

The Poincaré integral for polynomial perturbations is an integral of a rational (in fact, polynomial) 1-form ω \omega over a cycle δ \delta on the real algebraic curve { H = t } \{H=t\}. Such integrals are called *Abelian integrals*and they can be considered as functions of all parameters occurring in the construction (coefficients of the 1-form and the algebraic curve). In particular, we can consider the Hamiltonian H H and the 1-form ω \omega as the parameters and look at the Poincaré integral ( 4) as a continuous branch of a multivalued function I H, ω ​ ( t) I_{H,\omega}(t) of the single variable t t, the value taken by H H on the cycle δ ( t) ⊆ { H ( x, y) = t } \delta(t)\subseteq\{H(x,y)=t\} 3 3 3 If the curve { H = t } \{H=t\} carries several smooth real ovals, we always consider several branches of the integral I I simultaneously.. For a non-conservative perturbation, this function is not identically zero by definition.

In such a context the question about limit cycles born in the perturbation ( 2) reduces to the question about an upper bound for the *total number of isolated zeros of real branches of the Abelian integral I H, ω ​ ( t) I_{H,\omega}(t), counted with multiplicities.*This upper bound should be uniform over arbitrary combinations of the “parameters” H H and ω \omega of degrees not exceeding a given natural number n n.

Theorem 1 is an immediate corollary of the following result on zeros of Abelian integrals. For any finite values n, m ∈ ℕ n,m\in{\mathbb{N}} denote by 𝒩 ⁡ ( n, m) {\mathcal{N}}(n,m) the upper bound for the number of isolated real zeros of the integrals I I counted with multiplicities,

 | 𝒩 ⁡ ( n, m) = sup ω, H 𝒩 ⁡ ( H, ω) = sup ω, H ∑ t ord t ⁡ I H, ω ​ ( ⋅), deg H ⩽ n + 1, deg ω ⩽ m. {\mathcal{N}}(n,m)=\sup_{\omega,H}{\mathcal{N}}(H,\omega)=\sup_{\omega,H}~\sum_{t}\operatorname{ord}_{t}I_{H,\omega}({\,\boldsymbol{\cdot}}\,),\\ \deg H\leqslant n+1,\ \deg\omega\leqslant m. |  | (5) |

Here ord t ⁡ I ⩾ 0 \operatorname{ord}_{t}I\geqslant 0 denotes the order of the root of the integral I I at a real point t t (this order is zero by definition if I ⁡ ( t) ≠ 0 I(t)\neq 0 and 1 for a simple root); if for a given value of t t the algebraic curve { H = t } \{H=t\} carries several real nonsingular ovals, the summation is extended over all corresponding continuous branches of I I.

###### Theorem 2

 | 𝒩 ⁡ ( n, n) ⩽ 2 2 Poly ⁡ ( n), {\mathcal{N}}(n,n)\leqslant 2^{2^{\operatorname{\textup{Poly}}(n)}}, |  |

were the expression Poly ⁡ ( n) = O ⁡ ( n p) \operatorname{\textup{Poly}}(n)=O(n^{p}) stands for an explicit polynomially growing term with the exponent p p not exceeding 61 61.

This result, the first *explicit uniform bound*for the number of isolated zeros of Abelian integrals, is the most recent (hopefully, not the last) step in the long line of research, partly outlined in § 1.4.

###### Remark 1 (notation for polynomial bounds)

Here and below we will deal with explicit bounds which involve simple or double exponentials of polynomially growing terms. In order to avoid cumbersome notation, we will use the following shortcuts.

Everywhere unless explicitly waived, the symbol O ⁡ ( ⋅) O({\,\boldsymbol{\cdot}}\,) refers to an explicit constructive asymptotic; in particular, the notation O ⁡ ( n p) O(n^{p}) means a constructive positive function of an integer argument n n which does not exceed the expression C ​ n p Cn^{p} for some explicit constant C < + ∞ C<+\infty and all n ⩾ 2 n\geqslant 2.

The notation Poly ⁡ ( n) \operatorname{\textup{Poly}}(n) stands for the constructive bound O ⁡ ( n p) O(n^{p}) for some unspecified finite exponent p < + ∞ p<+\infty.

Sometimes the growth rate will be estimated by the “extended polynomial notation” O + ​ ( n p) O^{+}(n^{p}), which by definition means “ O ⁡ ( n p + ε) O(n^{p+\varepsilon}) for any positive ε \varepsilon ”. A typical example is as follows: for any finite q > 0 q>0,

 | n ​ ln q ​ n = O + ​ ( n). n\ln^{q}n=O^{+}(n). |  | (6) |

Of course, the notation O + ​ ( n p) O^{+}(n^{p}) in the upper bound could be replaced by O ⁡ ( n p + 1) O(n^{p+1}), yet when such “rounding errors” are composed, the overall bound gets increased by artificial terms unrelated to the nature of these bounds.

For bounds depending on several arguments, we use the notation O ⁡ ( n p ​ m q) O(n^{p}m^{q}), Poly ⁡ ( n, m) \operatorname{\textup{Poly}}(n,m) and O + ​ ( n p ​ m q) O^{+}(n^{p}m^{q}) in a self-explanatory way.

The introduced notation allows to formulate the improved bounds in Theorems 1 and 2. What we prove in fact is the double exponential bound 2 2 Poly ⁡ ( n) 2^{2^{\operatorname{\textup{Poly}}(n)}} with Poly ⁡ ( n) = O + ​ ( n 60) \operatorname{\textup{Poly}}(n)=O^{+}(n^{60}), see ( 23).

###### Remark 2 (accuracy of the upper bounds)

The double exponential expression cited in Theorem 2 is only an *upper bound*with no claim of accuracy whatsoever. Moreover, some fine tuning of the tools developed in this paper, can apparently help in reducing the power p = 61 p=61 to a much lower value, perhaps, as low as p = 2 p=2 (at the price of clarity of the exposition), see § 4.9. Reducing the bounds to less than two exponential orders would definitely require new ideas.

On the other hand, the only known *lower bounds*are quadratic in n n and linear in the degree of the form m = deg ⁡ ω m=\deg\omega for a fixed n n if the latter is allowed to grow to infinity independently of the degree of the Hamiltonian, cf. with ( 5). Thus far there is no sound conjecture on what might be the true asymptotic behavior of the function 𝒩 ⁡ ( n, m) {\mathcal{N}}(n,m).

### 1.3 Bifurcations of limit cycles *not covered*by Theorem 1

In order to avoid possible ambiguities, we make several remarks on what *is not asserted*in Theorem 1. The remarks below can be considered as a list of open problems.

###### Remark 3 (Conservative and integrable perturbations)

Theorem 1 gives no bound on the number of limit cycles if the perturbation itself is *conservative*, i.e., if the Poincaré integral vanishes *identically*for all ovals δ \delta in the family. For instance, if ω \omega is exact, ω = d ​ F \omega=\,\mathrm{d}F, F ∈ ℝ ⁡ [x, y] F\in{\mathbb{R}}[x,y], then the entire family ( 2) consists of Hamiltonian systems and exhibits no limit cycles for all ε ∈ ( ℝ, 0) \varepsilon\in({\mathbb{R}},0).

On the other hand, the identical vanishing of the Poincaré integral ( 4) in general *does not imply*that all foliations in the family ( 2) are integrable and hence do not have limit cycles at all. Indeed, the integral ( 4) is only the first variation of the Poincaré return map with respect to the parameter ε \varepsilon. If the first variation vanishes, one can compute higher variations in what is sometimes called the *Françoise algorithm*Fra 96; Yak 95, see also ( IY 08, §26B). The number of isolated zeros of the *first not identically vanishing variation*will majorize the number of limit cycles born from smooth ovals of the Hamiltonian field.

For a *generic*polynomial H H, one can show that the higher variations will again be Abelian integrals of certain polynomial 1-forms, yet their degrees are growing together with the order of the variation. Thus the problem of counting the limit cycles in the perturbation ( 2) reduces via Theorem 1 to the question on *how many consecutive higher variations can vanish identically without the family ( 2) being necessarily integrable*. This is a generalization of the famous *Poincaré center problem*whose solution is unknown even in the best of the best cases H ⁡ ( x, y) = x 2 + y 2 H(x,y)=x^{2}+y^{2}.

In the special degenerate (e.g., symmetric) cases the higher variations cannot be expressed as Abelian integrals, only by means of (polynomial expressions in) the so called *iterated integrals*GI 05; Gav 05. Formally these integrals are not covered by Theorem 2 below. However, L. Gavrilov and I. Iliev have shown that the iterated integrals still satisfy a Fuchsian system of equations and very recently it was discovered that the monodromy group of this system is quasiunipotent GN 08. These observations pave a way to application of Theorem 8, our principal result, yet many things remain to be done in order to bridge the gaps. Anyhow, the same question on the maximal order of the nontrivial high variations (an equivalent of the center problem) reappears in this case as well.

###### Remark 4 (Various scenarios of integrability)

Hamiltonian vector fields are only the simplest case of integrable polynomial foliations on the projective plane ℝ ​ P 2 {\mathbb{R}}P^{2}. The question about all possible scenarios of integrability is one notch above the Poincaré center problem (which addresses the question of integrability only locally, near a singular point), hence is challenging and wide open. Still, some possibilities are well known and documented.

One such scenario is the *Darbouxian integrability*, which corresponds to replacing the *exact polynomial*1-form d ​ H \,\mathrm{d}H in ( 2), by a *closed rational*1-form (note that the equations in the Pfaffian form admit multiplication by a rational factor without changing the behavior of the trajectories).

Investigation of limit cycles born by perturbation of Darbouxian integrable systems is a completely new field, where only the first steps are now taken Nov 09; BM 08. One of the main difficulties is the fact that the ovals of Darbouxian integrable systems are in general not algebraic. This circumstance renders practically inapplicable all known tools working for Abelian integrals. In particular, Theorem 1 seems to be of no help in this context, as the Poincaré integrals do not satisfy any finite order linear differential equation.

Besides Hamiltonian and Darbouxian integrability, there are some other known scenarios. The most difficult for analysis seems to be appearance of limit cycle by perturbation of *symmetric systems*, yet the problem is too vague to be discussed here.

###### Remark 5 (Limit cycles born from nonsmooth level curves of the Hamiltonian)

Theorem 1 asserts *nothing*about the number of limit cycles born from *nonsmooth*ovals, corresponding to the *critical level curves*of Hamiltonians.

For a *generic*real Hamiltonian, the only critical level ovals are separatrix loops (homoclinic trajectories of a nondegenerate saddle) and double loops (eight-shaped curves, *butterflies*), pairs of homoclinic orbits of the same saddle, which may generate limit cycles converging uniformly to the union of the two trajectories.

The case of separatrix loops is well understood after the seminal works of R. Roussarie Rou 86; Rou 89. An upper bound for the number of cycles born from a simple loop can be obtained from Theorem 2, yet much weaker results on the maximal multiplicity of zero of Abelian integrals, in the spirit of Mar 91; Mou 03 are sufficient and give much better bounds. A similar bound for the double loops could perhaps be derived using the tools from JM 94.

For singular level curves carrying *more than one*saddle critical point of H H, one cannot in general predict the number of limit cycles based only on the first asymptotic terms of the Abelian integral (a substitute for the order of zero for points of non-analyticity of I I). In DR 06; CDR 07 it is shown that already for perturbations of a Hamiltonian foliation with two nondegenerate critical points on the same level curve, one can obtain limit cycles not related to zeros of Abelian integrals (called *alien cycles*).

The general question about limit cycles born from a critical level curve of an arbitrary polynomial Hamiltonian, is quite challenging and essentially open.

### 1.4 A few milestones

Probably the first to realize that investigation of limit cycles in near-integrable systems may be a path to solution of the Hilbert problem, were I. G. Petrovskiĭ and E. M. Landis PL 55; PL 57; PL 59. Although their direct approach turned out to be unfeasible, these seminal papers stimulated the study of perturbations of Hamiltonian systems.

The first study of Abelian integrals, focused on investigation of their roots in connection with the bifurcation of limit cycles, was undertaken in the dissertation of Yu. Ilyashenko (adviser E. M. Landis), see Ily69b; Ily69a. In this work Ilyashenko introduced very powerful tools from complex analysis and algebraic geometry and implicitly formulated the infinitesimal Hilbert problem in the form we solve it now.

One of the first explicit bounds for the number of zeros of Abelian (elliptic) integrals was obtained by R. Bogdanov Bog 76; soon Yu. Ilyashenko gave a transparent proof this result Ily 78.

Since then the number of papers devoted to investigation of zeros of Abelian integrals counts in the hundreds, and it is impossible to mention even the names of the principal contributors. The overwhelming majority of these papers deal with the low-degree cases n = 3, 4 n=3,4, where the problem is essentially settled by L. Gavrilov, I. Iliev and C. Li (see part 2 of the book CL 07 and references therein).

In the general case of arbitrary degree, however, very little is known. In 1984 A. Khovanskiĭ and A. Varchenko proved that the number of zeros of Abelian integrals is always finite and uniformly bounded over all Hamiltonians and 1-forms of a given degree Kho 84; Var 84, i.e., that 𝒩 ⁡ ( n, m) < + ∞ {\mathcal{N}}(n,m)<+\infty for all finite combinations n, m n,m. Unfortunately, the proof is purely existential and does not give explicit bounds on 𝒩 ⁡ ( n, m) {\mathcal{N}}(n,m) even for small degrees n, m n,m.

After this celebrated result many efforts were focused on obtaining asymptotic constructive bounds for the “counting function” 𝒩 ⁡ ( ⋅) {\mathcal{N}}({\,\boldsymbol{\cdot}}\,). Very soon it became clear that the roles of the form and the Hamiltonian are quite different from the point of view of the difficulty of study. More precisely, for a fixed Hamiltonian H H one may consider forms of arbitrary degree m m growing to infinity, and study the asymptotic of the counting function 𝒩 ⁡ ( H, m) {\mathcal{N}}(H,m) as m → + ∞ m\to+\infty. The first bounds for this restricted setting were double exponential in the degree of the form IY 95, yet very quickly they were replaced by single exponential NY 95 and finally linear Pet 97 bounds. The ultimate result, due to Petrov and Khovanskiĭ, is the following estimate,

 | ∀ n, m ∈ ℕ 𝒩 ⁡ ( n, m) = O n exist ​ ( 1) + O ⁡ ( m). \forall n,m\in{\mathbb{N}}\hskip 18.49988pt{\mathcal{N}}(n,m)=O_{n}^{\text{exist}}(1)+O(m). |  | (7) |

Here the first term O n exist ​ ( 1) O_{n}^{\text{exist}}(1) is a *purely existential*“constant” depending on n n (uniformly over all Hamiltonians of degree ⩽ n + 1 \leqslant n+1) and the second term O ⁡ ( m) O(m) is, as usual, explicit and constructive. For quite some time the proof of this result existed only in the oral tradition, until it was published in the book ( Żol 06, Theorem 6.26). The proof is based on the fact that the Abelian integrals of a 1-form of arbitrarily high degree m m over level ovals of a Hamiltonian H H of degree ⩽ n + 1 \leqslant n+1 can always be represented as a linear combination of integrals of 1-forms of degree not exceeding 2 ​ n 2n with coefficients polynomial in t t of degree O ⁡ ( m / n) O(m/n) (see Theorem 10 below). Based on this observation, one can *conjecture*that there exists an explicit (constructive) bound of the form

 | 𝒩 ⁡ ( n, m) ⩽ 2 2 Poly ⁡ ( n) + O ⁡ ( m) as ​ n, m → + ∞ {\mathcal{N}}(n,m)\leqslant 2^{2^{\operatorname{\textup{Poly}}(n)}}+O(m)\hskip 18.49988pt\text{as }n,m\to+\infty |  | (8) |

(Theorem 2 addresses only the bound for 𝒩 ⁡ ( n, n) {\mathcal{N}}(n,n)). The proof could hopefully be obtained by a combination of the two techniques, since our methods allow placing an explicit upper bound on the first (existential) term in ( 7).

The most recent development in connection with the infinitesimal Hilbert 16th problem is an explicit upper bound for the number of zeros of Abelian integrals, uniform over all 1-forms of degree ⩽ n \leqslant n, finite for *almost all*Hamiltonians H H of degree n + 1 n+1, yet *non-uniform*in H H. In a series of papers Glu 05; Glu 06; GI 06; GI 07 A. Glutsyuk and Yu. Ilyashenko established this type of bound, which grows exponentially as H H approaches an exceptional set of Hamiltonians. This result was improved in BY 10 where a bound growing *polynomially*near the same exceptional set was given.

The only class of Hamiltonians of arbitrarily high degree for which uniform explicit upper bounds were previously known, is the class of *hyperelliptic Hamiltonians*of the form H ⁡ ( x, y) = 1 2 ​ y 2 + Q ⁡ ( x) H(x,y)=\frac{1}{2}y^{2}+Q(x), Q ∈ ℝ ⁡ [x] Q\in{\mathbb{R}}[x]. In NY99a it was proved that the number of isolated zeros of hyperelliptic integrals can be majorized by a *tower function*(iterated exponent) of n = deg ⁡ Q n=\deg Q under the technical assumption that all critical values of the hyperelliptic Hamiltonian are real. However, the height of this tower was much larger than 2 (corresponding to the double exponent).

### 1.5 Hyperelliptic case

The tools developed in this paper are sufficiently flexible to give better results for some more specific classes of Abelian integrals. For instance, if instead of a general bivariate polynomial H ⁡ ( x, y) H(x,y) we consider only the *hyperelliptic*Hamiltonians of the form

 | H ⁡ ( x, y) = 1 2 ​ y 2 + x n + 1 + λ 1 ​ x n − 1 + ⋯ + λ n, λ ∈ ℝ n, H(x,y)=\frac{1}{2}y^{2}+x^{n+1}+\lambda_{1}x^{n-1}+\cdots+\lambda_{n},\qquad\lambda\in{\mathbb{R}}^{n}, |  | (9) |

then some steps of the proof can be skipped or improved, see § 4.9. As a result, we have a better bound for zeros of the corresponding hyperelliptic integrals.

###### Theorem 3

The number of complex isolated zeros of a hyperelliptic Abelian integral associated with the Hamiltonian ( 9), is bounded by the explicit double exponent 2 2 O + ​ ( n) 2^{2^{O^{+}(n)}}.

This result, completely superseding the main result of our previous work NY99a, is explained in § 4.9.

###### Acknowledgements.

We are grateful to S. Basu, J. Bernstein, P. Deligne, V. Hinich and N. Vorobjov for useful conversations, professional consultations and illuminating remarks which turned out to be of key importance for the entire construction. Besides, we feel the need to acknowledge the pioneering work of our colleagues and former collaborators, that is essentially if not always directly used in the proof: G. Petrov, M. Roitman, A. Grigoriev, V. Arnold, A. Khovanskiĭ, A. Gabrielov, L. Gavrilov, H. Żola̧dek and especially Yu. Ilyashenko, who stood at the origin of the problem and suggested its particular case as a subject for the M.Sc. thesis research to one of the authors Yak 84. Finally, we owe many thanks to the two referees for their most attentive reading of the draft: the numerous remarks they made were very helpful in bringing the exposition to its final form. During the work on this project, two of the authors (G.B. and S.Y.) were partially supported by the Minerva Foundation. D.N. gratefully acknowledges the support of Soref New Scientists Start up Fund and Fusfeld Research Fund. S.Y. is the incumbent of the Gershon Kekst Professorial Chair.

## 2 Background, settings, main constructions and strategy

We begin by describing the (standard) complexification of the Abelian integrals and reduce the infinitesimal Hilbert 16th problem to a question about zeros of solutions to an integrable Pfaffian system subject to a condition on its monodromy. The exposition in this section primarily settles the context and notations for the main body; the recent textbook ( IY 08, §26) contains all necessary details.

### 2.1 Complete Abelian integrals depending on parameters

Let Γ = Γ λ ⊂ ℙ 2 \varGamma=\varGamma_{\lambda}\subset{\mathbb{P}}^{2} be the complex projective curve defined in the affine chart ( x 1, x 2) (x_{1},x_{2}) on ℂ 2 ⊂ ℙ 2 {\mathbb{C}}^{2}\subset{\mathbb{P}}^{2} by the equation

 | H ⁡ ( x 1, x 2) = 0, H = H ⁡ ( x, λ) = ∑ 0 ⩽ | α | ⩽ n + 1 λ α ​ x α H(x_{1},x_{2})=0,\qquad H=H(x,\lambda)=\sum_{0\leqslant|\alpha|\leqslant n+1}\lambda_{\alpha}x^{\alpha} |  | (10) |

(here and below we use the standard multiindex notation denoting by α ∈ ℤ + 2 \alpha\in{\mathbb{Z}}_{+}^{2} the multiindex, | α | = α 1 + α 2 |\alpha|=\alpha_{1}+\alpha_{2}, x α = x 1 α 1 ​ x 2 α 2 x^{\alpha}=x_{1}^{\alpha_{1}}x_{2}^{\alpha_{2}}). The parameters λ \lambda of this equation naturally vary over the *complex projective*space ℙ m {\mathbb{P}}^{m} of dimension m = 1 2 ​ ( n + 3) ​ ( n + 2) − 1 = O ⁡ ( n 2) m=\tfrac{1}{2}(n+3)(n+2)-1=O(n^{2}).

For a generic combination of the parameters λ \lambda the curve Γ λ \varGamma_{\lambda} is a nonsingular (smooth) Riemann surface of genus g = 1 2 ​ n ​ ( n − 1) g=\frac{1}{2}n(n-1), transversal to the infinite line 𝕀 = ℙ 2 ​ – ​ ℂ 2 {\mathbb{I}}={\mathbb{P}}^{2}{\,\text{--}\,}{\mathbb{C}}^{2}. The (first) homology group of Γ λ ​ – ​ 𝕀 \varGamma_{\lambda}{\,\text{--}\,}{\mathbb{I}} in this case has the rank ℓ = n 2 \ell=n^{2}, see ( IY 08, Theorem 26.31). The combination of the parameters corresponding to the exceptional (non-smooth or non-transversal to 𝕀 {\mathbb{I}}) curves Γ λ \varGamma_{\lambda}, is a projective algebraic subset that will be denoted by Σ ∗ \varSigma_{*}. For an arbitrary point λ ∗ ∉ Σ ∗ \lambda_{*}\notin\varSigma_{*} one can fix a system of cycles δ 1, …, δ ℓ \delta_{1},\dots,\delta_{\ell} generating the homology H 1 ​ ( Γ λ ∗, ℤ) H_{1}(\varGamma_{\lambda_{*}},{\mathbb{Z}}) with integer coefficients and transport them horizontally in the sense of the Gauss–Manin connexion. The result is a multivalued framing of the fibers H 1 ​ ( Γ λ, ℤ) H_{1}(\varGamma_{\lambda},{\mathbb{Z}}) associated with the topological bundle Γ λ ↦ λ \varGamma_{\lambda}\mapsto\lambda over ℙ m ​ – ​ Σ ∗ {\mathbb{P}}^{m}{\,\text{--}\,}\varSigma_{*}, ramified over Σ ∗ \varSigma_{*} ( IY 08, Corollary 26.28).

The cohomology of a generic fiber (curve) Γ λ \varGamma_{\lambda} is generated by restrictions of polynomial 1-forms on this curve. Let ω α = x 1 α 1 + 1 ⋅ x α ​ d ​ x 2 \omega_{\alpha}=\frac{x_{1}}{\alpha_{1}+1}\cdot x^{\alpha}\,\mathrm{d}x_{2} be monomial 1-forms which are primitives of the 2-forms μ α = x α ​ d ​ x 1 ∧ d ​ x 2 \mu_{\alpha}=x^{\alpha}\,\mathrm{d}x_{1}\land\!\,\mathrm{d}x_{2} with 0 ⩽ α 1, α 2 ⩽ n − 1 0\leqslant\alpha_{1},\alpha_{2}\leqslant n-1, i.e. d ​ ω α = μ α \,\mathrm{d}\omega_{\alpha}=\mu_{\alpha}. The number of such forms is exactly equal to ℓ = n 2 \ell=n^{2}, and it is known (see Appendix A for details and references) that the ω α \omega_{\alpha} generate the cohomology of a *generic*fiber Γ λ \varGamma_{\lambda} with λ ∉ Σ ∗ \lambda\notin\varSigma_{*} over ℂ {\mathbb{C}}. However, for some exceptional fibers the forms ω α \omega_{\alpha} become linear dependent after restriction on Γ λ \varGamma_{\lambda}: the corresponding set is a proper algebraic subvariety, whose union with Σ ∗ \varSigma_{*} will be denoted by Σ ⊂ ℙ m \varSigma\subset{\mathbb{P}}^{m}.

###### Definition 6

The *period*matrix X ⁡ ( λ) X(\lambda) is the ( ℓ × ℓ) (\ell\times\ell) -square (multivalued) analytic matrix function on ℙ m {\mathbb{P}}^{m},

 | X ⁡ ( ⋅) = ( ∮ δ 1 ​ ( ⋅) ω 1 ⋯ ∮ δ ℓ ​ ( ⋅) ω 1 ⋱ ∮ δ 1 ​ ( ⋅) ω ℓ ⋯ ∮ δ ℓ ​ ( ⋅) ω ℓ), X({\,\boldsymbol{\cdot}}\,)=\begin{pmatrix}\displaystyle\oint_{\delta_{1}({\,\boldsymbol{\cdot}}\,)}\kern-15.0pt\omega_{1}&\cdots&\displaystyle\oint_{\delta_{\ell}({\,\boldsymbol{\cdot}}\,)}\kern-15.0pt\omega_{1}\\ \vdots&\ddots&\vdots\\ \displaystyle\oint_{\delta_{1}({\,\boldsymbol{\cdot}}\,)}\kern-15.0pt\omega_{\ell}&\cdots&\displaystyle\oint_{\delta_{\ell}({\,\boldsymbol{\cdot}}\,)}\kern-15.0pt\omega_{\ell}\end{pmatrix}, |  | (11) |

ramified over the locus Σ ∗ \varSigma_{*} and nondegenerate on ℙ m ​ – ​ Σ {\mathbb{P}}^{m}{\,\text{--}\,}\varSigma.

###### Remark 7 (From projective spaces to pencils of lines)

In the formulation of Theorem 2 the Abelian integral occurs as a function of a distinguished variable t t, whereas all other coefficients of the Hamiltonian H H are treated as parameters. In the definition of the period matrix all coefficients of H H play the same role. However, this difference is only superficial, and one can consider X ⁡ ( λ) X(\lambda) as a parametric family of functions of one (complex) variable, so that their isolated zeros can be counted.

If in the expression for H H in ( 10) all parameters λ ^ = { λ α: α ≠ ( 0, 0) } {\hat{\lambda}}=\{\lambda_{\alpha}:\alpha\neq(0,0)\} are fixed except for the free term λ 0, 0 \lambda_{0,0}, we obtain a (complex projective) line L λ ^ ≅ ℙ 1 L_{{\hat{\lambda}}}\cong{\mathbb{P}}^{1}. These lines corresponding to different values of λ ^ ∈ ℙ m − 1 {\hat{\lambda}}\in{\mathbb{P}}^{m-1} form a *pencil of lines*, a family of lines in ℙ m {\mathbb{P}}^{m} passing through the point in ℙ m {\mathbb{P}}^{m} with the homogeneous coordinates ( 0, …, 0, 1) (0,\dots,0,1).

The space ℙ m {\mathbb{P}}^{m} is birationally equivalent to the product ℙ m − 1 × ℙ 1 {\mathbb{P}}^{m-1}\times{\mathbb{P}}^{1}. Moreover, the equivalence can be chosen to map the lines from the above pencil to the lines of the form ℙ λ ^ 1 = { λ ^ } × ℙ 1 {\mathbb{P}}^{1}_{{\hat{\lambda}}}=\{{\hat{\lambda}}\}\times{\mathbb{P}}^{1}. In suitable affine charts, the equivalence is represented by the natural identification ℂ m ≅ ℂ m − 1 × ℂ 1 {\mathbb{C}}^{m}\cong{\mathbb{C}}^{m-1}\times{\mathbb{C}}^{1}, λ ≅ ( λ ^, t) \lambda\cong({\hat{\lambda}},t). After such identification the period matrix ( 11) can be indeed considered as a multivalued matrix function X ⁡ ( λ ^, t) X({\hat{\lambda}},t)*with singularities*, defined on ℙ 1 {\mathbb{P}}^{1} and depending on the parameters λ ^ ∈ ℙ m − 1 {\hat{\lambda}}\in{\mathbb{P}}^{m-1} which vary over a compact parameter space.

### 2.2 Integrable Pfaffian systems with singularities

Consider a smooth (nonsingular) algebraic variety 𝕄 \mathbb{M} and let Ω \Omega be a rational ( ℓ × ℓ) (\ell\times\ell) -matrix-valued 1-form on 𝕄 \mathbb{M} with a singular locus Σ ⊂ 𝕄 \varSigma\subset\mathbb{M} which is an algebraic hypersurface (eventually, itself singular and reducible).

The form Ω \Omega is *integrable*if d ​ Ω − Ω ∧ Ω = 0 \,\mathrm{d}\Omega-\Omega\land\Omega=0. The integrability condition is necessary and sufficient for the *local*existence of a holomorphic nondegenerate matrix solution X ⁡ ( ⋅) X({\,\boldsymbol{\cdot}}\,) for the Pfaffian system of equations

 | d ​ X = Ω ⋅ X, Ω ∈ Mat ⁡ ( ℓ, Λ 1 ​ ( 𝕄)) \,\mathrm{d}X=\Omega\cdot X,\qquad\Omega\in\operatorname{Mat}\bigl(\ell,\varLambda^{1}(\mathbb{M})\bigr) |  | (12) |

near each nonsingular point a ∉ Σ a\notin\varSigma. The local solution admits analytic continuation along any path γ \gamma avoiding the singular locus. If the path γ \gamma is closed, the result of continuation Δ γ ​ X \Delta_{\gamma}X differs from the initial solution X X by a constant nondegenerate matrix factor M γ ∈ GL ⁡ ( ℓ, ℂ) M_{\gamma}\in\operatorname{GL}(\ell,{\mathbb{C}}), called the *monodromy*associated with this path: Δ γ ​ X = X ​ M γ \Delta_{\gamma}X=XM_{\gamma}.

###### Definition 8

Let τ: ( ℂ 1, 0) → ( 𝕄, Σ) \tau\colon({\mathbb{C}}^{1},0)\to(\mathbb{M},\varSigma), be the germ of a holomorphic curve, not entirely belonging to Σ \varSigma, and a = τ ⁡ ( 0) a=\tau(0).

A *small loop around the point a a*is a closed path which is the image τ ⁡ ( S ε) \tau(S_{\varepsilon}) of any sufficiently small circle S ε = { | s | = ε } ⊂ ( ℂ, 0) S_{\varepsilon}=\{|s|=\varepsilon\}\subset({\mathbb{C}},0). Here the smallness means that the image of the punctured disk { 0 < | s | ⩽ ε } \{0<|s|\leqslant\varepsilon\} is disjoint with Σ \varSigma.

A loop freely homotopic to a small loop will also be referred to as the small loop. All small loops “supported” by the same holomorphic curve τ \tau are freely homotopic to each other. The integrability assumption implies that the corresponding monodromy operators are conjugate to each other, and in particular they have the same spectrum.

###### Definition 9

The integrable form Ω \Omega is called *quasiunipotent*at a point a ∈ 𝕄 a\in\mathbb{M}, if all eigenvalues of each monodromy operator associated with any small loop around a a, are roots of unity. Clearly, *any*integrable form is quasiunipotent at a nonsingular point a ∉ Σ a\notin\varSigma, since the corresponding monodromy is the identity. The form is (globally) *quasiunipotent*, if it is quasiunipotent at every point of the singular locus of Ω \Omega.

###### Remark 10

If dim 𝕄 = 1 \dim\mathbb{M}=1, i.e., the system is one-dimensional, then the quasiunipotence condition means that the monodromy operators along any sufficiently small loop around each singular point are quasiunipotent. This condition can be effectively verified if the system is Fuchsian (has a first order pole) by inspection of the spectrum of the corresponding residue matrix: all eigenvalues of this matrix should be *rational*.

However, a loop that encircles several singularities is not small, thus quasiunipotence does not impose any conditions on the corresponding “large” monodromy.

The system ( 12) (and the corresponding matrix 1-form Ω \Omega) is called *regular*on 𝕄 \mathbb{M}, if for any *real analytic*path γ: ( ℝ, 0) → ( 𝕄, Σ) \gamma\colon({\mathbb{R}},0)\to(\mathbb{M},\varSigma) the solution grows no faster than polynomially near the singular locus,

 | | X ⁡ ( γ ⁡ ( s)) | ± 1 ⩽ c ​ | s | − p ∀ s ∈ ( ℝ 1, 0), |X(\gamma(s))|^{\pm 1}\leqslant c|s|^{-p}\qquad\forall s\in({\mathbb{R}}^{1},0), |  | (13) |

for some real numbers c, p < + ∞ c,p<+\infty, eventually depending on the path γ \gamma. Analyticity of the path γ \gamma intends to rule out spiraling along the singular locus. One can show that regularity is sufficient to verify only along (real) line segments.

The following result can be considered as a “*removable singularity assertion*” for regular quasiunipotent systems.

###### Theorem 4 ( Kashiwara theorem Kas 81)

A regular integrable system that is quasiunipotent at each point outside an algebraic subset of codimension ⩾ 2 \geqslant 2, is globally quasiunipotent.

###### Remark 11 (important)

If in the definition of the quasiunipotence (local and global) we replace the assumption on the spectrum to consist solely of roots of unity by a *weaker*assumption that all these eigenvalues have modulus 1, then Theorem 4 remains valid as well as all other assertions, including our main result (Theorem 8 below). It is in this stronger form that the results on general Fuchsian systems are formulated in BY 10. However, we are not aware of any naturally arising system that satisfies this weaker assumption and is not quasiunipotent in the usual (stronger) sense.

###### Theorem 5 ( folklore)

The period matrix X X of Abelian integrals ( 11) satisfies an *integrable*, *regular*and *quasiunipotent*system of equations of the form ( 12) on ℙ m {\mathbb{P}}^{m}.

###### Proof

This is a classical “well-known fact” whose proofs are scattered over a number of classical sources. We outline only the principal arguments.

The period matrix X X described in ( 11), is *monodromic*: the result of its continuation Δ γ ​ X \Delta_{\gamma}X along any closed path γ \gamma avoiding the ramification locus Σ ∗ \varSigma_{*}, differs from the initial value X X by a constant monodromy matrix which describes the parallel transport of the cycles δ j \delta_{j} along the path ( IY 08, Corollary 26.28).

This implies that the *logarithmic derivative*Ω = d ​ X ⋅ X − 1 \Omega=\,\mathrm{d}X\cdot X^{-1} is a single-valued matrix function defined on the complement ℙ m ​ – ​ Σ {\mathbb{P}}^{m}{\,\text{--}\,}\varSigma.

The growth of X X near the singular locus is at most polynomial: indeed, the length of any cycle of the integration δ j ​ ( λ) \delta_{j}(\lambda) is growing no faster then polynomially along any curve and so does the integrand. Hence all entries of Ω \Omega grow no faster than polynomially near Σ \varSigma. Being single-valued, Ω \Omega is necessarily a *rational*matrix 1-form. The integrability condition follows immediately from the local representation of Ω \Omega as a logarithmic derivative.

The properties of the monodromy group of Ω \Omega were studied in great detail. The fact that the system is quasiunipotent was proved by Brieskorn Bri 70 and Clemens Cle 69 by completely different methods; the proofs were re-exposed a number of times AGV 88; Żol 06.

The shortest way to prove the quasiunipotence is using the Kashiwara theorem. A generic point of Σ \varSigma corresponds to a simple normal crossing of the curve Γ λ \varGamma_{\lambda} or to a quadratic tangency of this curve with the infinite line (which is a polar locus for ω \omega). In the first case the monodromy along a small loop γ \gamma around a a is described by the *Picard–Lefschetz formulas*( IY 08, §26I): the corresponding monodromy matrix M γ M_{\gamma} has a Jordan block of size 2 × 2 2\times 2 with the eigenvalue 1 1. In the second case M γ 2 = 1 M_{\gamma}^{2}=1, hence all eigenvalues of M γ M_{\gamma} are necessarily ± 1 \pm 1. Both cases are clearly quasiunipotent. By the Kashiwara theorem, we conclude that Ω \Omega is globally quasiunipotent.

###### Definition 12

Throughout this paper the Pfaffian system ( 12) satisfied by the period matrix ( 11) will be referred to as *the Picard–Fuchs system*.

### 2.3 Polynomial norms

When dealing with polynomials (both univariate and multivariate), we will always use the ℓ 1 \ell^{1} -norm.

###### Definition 13

The *norm*of a multivariate polynomial P ∈ ℂ ⁡ [z 1, …, z n] P\in{\mathbb{C}}[z_{1},\dots,\allowbreak z_{n}], P ⁡ ( z) = ∑ α c α ​ z α P(z)=\sum_{\alpha}c_{\alpha}z^{\alpha}, c α ∈ ℂ c_{\alpha}\in{\mathbb{C}} (in the standard multiindex notation) is the sum of absolute values of its coefficients, ‖ P ‖ = ∑ | c α | \|P\|=\sum|c_{\alpha}|. Clearly, this norm is multiplicative,

 | ‖ P ​ Q ‖ ⩽ ‖ P ‖ ⋅ ‖ Q ‖. \|PQ\|\leqslant\|P\|\cdot\|Q\|. |  | (14) |

### 2.4 Algebraic objects defined over ℚ {\mathbb{Q}} and their complexity

Complexification, replacing integrals over real ovals by the complex analytic period matrix ( 11), was one of the first tools of investigation of Abelian integrals Ily 78. In this section we describe an opposite (in a sense) step and introduce the class of differential equations defined over ℚ {\mathbb{Q}}, the subfield of rational numbers in the field ℂ {\mathbb{C}}.

Speaking informally, an object (a polynomial, rational fraction, variety, Pfaffian form, differential operator, semialgebraic set *etc*.) is defined over ℚ {\mathbb{Q}}, if it can be effectively constructed from the ring ℤ ⁡ [z 1, …, z n] {\mathbb{Z}}[z_{1},\dots,z_{n}] of *lattice polynomials*. For objects defined over ℚ {\mathbb{Q}}, besides the standard algebraic characteristics like degree and dimension, one can always measure its *size*, roughly understood as the *magnitude of the integer numbers occurring in the explicit formulas*describing the objects.

Perhaps the term “size” is not very successful, since the size of a small reciprocal 1 / n ∈ ℚ 1/n\in{\mathbb{Q}} with n ∈ ℕ n\in{\mathbb{N}} would be essentially equal to the large number n n. The term “complexity” would better suit our purposes, but this term is too overloaded. As a compromise, the reader may think of the size as (the exponent of) the *bit*size of the explicit representation of the given objects. The formal definitions follow.

###### Definition 14

The *size*𝐒 ⁡ ( R) \mathbf{S}\left(R\right) of a lattice (integer) polynomial P ∈ ℤ ⁡ [z 1, …, z n] P\in{\mathbb{Z}}[z_{1},\dots,z_{n}] is set to be equal to its norm, 𝐒 ⁡ ( P) = ‖ P ‖ \mathbf{S}\left(P\right)=\|P\|.

The *size*of a rational fraction R ∈ ℚ ⁡ ( z 1, …, z n) R\in{\mathbb{Q}}(z_{1},\dots,z_{n}) is

 | 𝐒 ( R) = min P, Q { ∥ P ∥ + ∥ Q ∥: R = P / Q, P, Q ∈ ℤ [z 1, …, z n] }, \mathbf{S}\left(R\right)=\min_{P,Q}\{\|P\|+\|Q\|\colon R={P}/{Q},\ P,Q\in{\mathbb{Z}}[z_{1},\dots,z_{n}]\}, |  | (15) |

the minimum being taken over all possible representations of R = P / Q R=P/Q with P, Q ∈ ℤ ⁡ [z 1, …, z n] P,Q\in{\mathbb{Z}}[z_{1},\dots,z_{n}].

The size of a (polynomial or rational) 1-form on ℙ m {\mathbb{P}}^{m} defined over ℚ {\mathbb{Q}}, is the sum of sizes of its coefficients in the standard affine chart ℂ m ⊂ ℙ m {\mathbb{C}}^{m}\subset{\mathbb{P}}^{m}.

The size of a vector or matrix rational function (resp., 1-form) defined over ℚ {\mathbb{Q}}, is the sum of the sizes of its components.

A *parametric family*of objects is defined over ℚ {\mathbb{Q}}, if it is defined over ℚ {\mathbb{Q}} on the product space ℙ m − 1 × ℙ 1 {\mathbb{P}}^{m-1}\times{\mathbb{P}}^{1} birationally equivalent to ℙ m {\mathbb{P}}^{m} (cf. with Remark 7). The size of the parametric family is defined via the corresponding equivalence.

One can easily continue this series of definitions, extending it for any class of algebraic objects and their parametric families algebraically depending on auxiliary parameters. In the future we will need to define the size of ordinary differential operators, see § 3.

###### Remark 15

The size is associated not so much with an object, but rather with a specific formula representing it. For instance, the polynomial 1 + t + t 2 + ⋯ + t n − 1 1+t+t^{2}+\cdots+t^{n-1} of size n n in ℤ ⁡ [t] {\mathbb{Z}}[t] can be represented as a rational function ( t n − 1) / ( t − 1) (t^{n}-1)/(t-1) of size only 4 4 in ℚ ⁡ ( t) {\mathbb{Q}}(t). Yet for our purposes this ambiguity will not be important, since we will deal only with *explicit upper bounds*for the size which means construction of *formulas*(representations) not involving excessively large natural numbers.

The most important feature of the size of formulas defined over ℚ {\mathbb{Q}} is its *controlled increase in any algorithmically defined construction*. For instance, the size of a sum and product of two rational fractions of sizes s 1, s 2 s_{1},s_{2}, can be estimated as follows,

 | 𝐒 ⁡ ( p 1 q 1 + p 2 q 2) ⩽ 𝐒 ⁡ ( p 1 ​ q 2 + p 2 ​ q 1 q 1 ​ q 2) ⩽ 3 ​ s 1 ​ s 2, 𝐒 ⁡ ( p 1 q 1 ⋅ p 2 q 2) ⩽ 2 ​ s 1 ​ s 2. \mathbf{S}\left(\frac{p_{1}}{q_{1}}+\frac{p_{2}}{q_{2}}\right)\leqslant\mathbf{S}\left(\frac{p_{1}q_{2}+p_{2}q_{1}}{q_{1}q_{2}}\right)\leqslant 3s_{1}s_{2},\quad\mathbf{S}\left(\frac{p_{1}}{q_{1}}\cdot\frac{p_{2}}{q_{2}}\right)\leqslant 2s_{1}s_{2}. |  | (16) |

Composition of maps defined over ℚ {\mathbb{Q}} is also an operation that increases the size (complexity) in a limited way.

###### Example 16

The projective space ℙ m + n {\mathbb{P}}^{m+n} is birationally equivalent to the product ℙ m × ℙ n {\mathbb{P}}^{m}\times{\mathbb{P}}^{n}, e.g., via the standard identification ℂ m + n ≅ ℂ m × ℂ n {\mathbb{C}}^{m+n}\cong{\mathbb{C}}^{m}\times{\mathbb{C}}^{n} in the affine charts. Such transformations do not result in a substantial change of the complexity of objects, in particular, the above equivalence does not change the complexity of rational functions defined on the corresponding birationally equivalent varieties.

An example of effective complexity control is the following explicit bound on solutions of linear systems of algebraic equations.

###### Example 17

Consider a parametric family of systems of linear algebraic equations of the form

 | A ⁡ ( λ) ​ z = b ⁡ ( λ), λ ∈ ℙ m, z = ( z 1, …, z n), A(\lambda)z=b(\lambda),\qquad\lambda\in{\mathbb{P}}^{m},\quad z=(z_{1},\dots,z_{n}), |  | (17) |

and assume that this system is defined over ℚ {\mathbb{Q}}, that is, the entries a i ​ j, b j a_{ij},b_{j} of the matrix A A and the right hand side vector b b are elements from the field ℚ ⁡ ( λ) {\mathbb{Q}}(\lambda) of known degrees not exceeding d d, and their size does not exceed s s.

The system may well be non-solvable over ℚ ⁡ ( λ) {\mathbb{Q}}(\lambda), but in case it is known to have a solution, such a solution can always be found of size not exceeding O ⁡ ( n n) ​ s n O(n^{n})\,s^{n}.

Indeed, after eliminating all equations that are linearly dependent over the field ℚ ⁡ ( λ) {\mathbb{Q}}(\lambda), we can represent components of some solution as ratios of suitable minors by the Cramer rule. Each of these minors is the sum of at most n! n! products of n n entries of A ⁡ ( λ) A(\lambda), all of them in the field ℚ ⁡ ( λ) {\mathbb{Q}}(\lambda), so that the degree is no greater than d n d^{n} and the size is no greater than n! ​ ( 6 ​ s) n n!(6s)^{n} by ( 16).

### 2.5 “Quantization principle”

The following general principle is the primary reason why objects defined over ℚ {\mathbb{Q}} appear in a construction which initially has no such structure: *Any finite bound for objects defined over ℚ {\mathbb{Q}}, is explicitly computable in terms of their size*. We give two illustrations of this principle.

###### Example 18 (algebraic, continuation of Example 17)

A non-homogeneous system A ​ z = b Az=b of linear algebraic equations defined over ℚ {\mathbb{Q}} may have no solution, but if the solution exists, there exists also a solution of norm bounded in terms of the dimension n n and size s s (complexity) of the system, | z | ⩽ n! ​ s n |z|\leqslant n!s^{n}.

Indeed, without loss of generality we may assume that all entries of the matrix A A and the free terms b b are *integer*not exceeding s n s^{n} in the absolute value. Then, as explained in Example 17, for some particular solution each component can be represented as the ratio of some minors. The numerator does not exceed n! ​ s n 2 n!s^{n^{2}} (again using the Laplace expansion with obvious estimates), while the denominator, being a nonzero *integer*, is no smaller than 1 1.

###### Example 19 (geometric)

Assume that K ⊆ ℝ n K\subseteq{\mathbb{R}}^{n} is a basic semialgebraic set defined by finitely many polynomial equalities and inequalities of the form p α ​ ( x) = 0 p_{\alpha}(x)=0 (resp., p α ⩽ 0 p_{\alpha}\leqslant 0), where p α p_{\alpha} are polynomials defined over ℚ {\mathbb{Q}} of degree ⩽ d \leqslant d and size no greater than s s.

The set K K may well be non-compact (e.g., a half-space), but if it is known to be compact, its diameter can be explicitly bounded as follows.

###### Theorem 6 ( BPR 03; BV 07)

If a basic semialgebraic set

 | K = ⋂ α { x: p α ​ ( x) ⩽ 0 }, p α ∈ ℤ ⁡ [x], deg ⁡ p α ⩽ d, ‖ p α ‖ ⩽ s, K=\bigcap_{\alpha}\{x\colon p_{\alpha}(x)\leqslant 0\},\quad p_{\alpha}\in{\mathbb{Z}}[x],\ \deg p_{\alpha}\leqslant d,\ \|p_{\alpha}\|\leqslant s, |  | (18) |

is bounded, then it belongs to the ball of radius R R centered at the origin, with R = s d O ⁡ ( n) R=s^{d^{O(n)}}. The constant in O ⁡ ( n) O(n) is explicit.

The same result holds for semialgebraic sets defined by polynomials from ℚ ⁡ [x] {\mathbb{Q}}[x], if s s is the upper bound for their size 𝐒 ⁡ ( p α) \mathbf{S}\left(p_{\alpha}\right).

This claim, rather obvious for the one-dimensional case n = 1 n=1, can be proved for arbitrary n n by the algorithmic quantifier elimination technique (corresponding to the projection of K K to ℝ n − 1 ⊂ ℝ n {\mathbb{R}}^{n-1}\subset{\mathbb{R}}^{n}). The quantifier elimination process can be made constructive, which results in a controlled increase of the complexity in each step.

Of course, the “quantization principle” is only a guiding line, not a theorem; in each instance we will have to address a specific question on effective bounds either directly (as in Example 17) or indirectly, using tools of effective real algebraic geometry (as in Example 19).

The “quantization principle” was already implicitly used in the proof of the general result on meandering of trajectories of arbitrary polynomial vector fields NY99b. In application to linear systems this principle was introduced in Gri 01; Gri 03 and later in a more transparent and general form in Yak 06.

### 2.6 Counting zeros of multivalued matrix functions of several variables

The period matrix X ⁡ ( λ) X(\lambda), the solution of the Pfaffian system ( 12), is ramified over the singular locus Σ \varSigma. We introduce the *counting function*which generalizes the number of isolated zeros of functions of one variable to the class of multivalued matrix-functions of several complex variables.

Let ℙ 1 ≅ L ⊂ ℙ m {\mathbb{P}}^{1}\cong L\subset{\mathbb{P}}^{m} be an arbitrary projective line *not entirely belonging*to the singular locus Σ \varSigma of the Pfaffian system ( 12) on 𝕄 = ℙ m \mathbb{M}={\mathbb{P}}^{m}. The intersection L ∩ Σ L\cap\varSigma in this case consists of finitely many isolated points, and the restriction of the matrix function X ⁡ ( λ) X(\lambda) on L L will be ramified over these points.

Let T ⊂ L ​ – ​ Σ T\subset L{\,\text{--}\,}\varSigma be an arbitrary *triangle*, an open domain bounded by three circular arcs eventually degenerating into line segments or points. Since T T is simply connected, one can unambiguously choose a continuous holomorphic branch of the matrix function X ⁡ ( t) = ( x i ​ j ​ ( t)) i, j = 1 ℓ X(t)=\bigl(x_{ij}(t)\bigr)_{i,j=1}^{\ell}, t ∈ T t\in T.

Consider the *linear span*,

 | ℒ X ( T) = { f ∈ 𝒪 ( T): f = ∑ i, j = 1 ℓ c i ​ j x i ​ j ( t), c i ​ j ∈ ℂ }. \mathscr{L}_{X}(T)=\{f\in\mathscr{O}(T)\colon f=\sum_{i,j=1}^{\ell}c_{ij}x_{ij}(t),\ c_{ij}\in{\mathbb{C}}\}. |  | (19) |

a finite-dimensional subspace in the space of functions of one complex variable (recall that T T is a triangle in a complex projective line), holomorphic in T T.

Replacing the matrix function X ⁡ ( ⋅) X(\cdot) by a different solution X ⁡ ( ⋅) ​ M X(\cdot)M, M ∈ GL ⁡ ( ℓ, ℂ) M\in\operatorname{GL}(\ell,{\mathbb{C}}) (in particular, by another branch of analytic continuation of X X), does not affect the subspace ℒ X ​ ( T) \mathscr{L}_{X}(T), thus the latter depends only on the Pfaffian matrix 1-form Ω \Omega.

We define the *counting function*as the supremum

 | 𝒩 ⁡ ( Ω) = sup T ⊂ ℙ m ​ – ​ Σ sup f ∈ ℒ X ​ ( T) #⁡ { t ∈ T: f ⁡ ( t) = 0 } ⩽ + ∞, {\mathcal{N}}(\Omega)=\sup_{T\subset{\mathbb{P}}^{m}{\,\text{--}\,}\varSigma}~\sup_{f\in\mathscr{L}_{X}(T)}\#\{t\in T\colon f(t)=0\}\leqslant+\infty, |  | (20) |

taken over all triangles T T disjoint with Σ \varSigma and all nonzero functions from ℒ X ​ ( T) \mathscr{L}_{X}(T).

###### Remark 20

The requirement that T T is a triangle is aimed at excluding simply connecting domains spiraling around the singular locus. Easy examples show that spiraling domains may contain arbitrarily large number of isolated zeros of very simple functions.

###### Remark 21

Knowing the bounding function 𝒩 ⁡ ( ⋅) {\mathcal{N}}(\cdot), one can use triangulation to estimate the number of isolated roots 𝒩 ⁡ ( Ω / U) {\mathcal{N}}(\Omega/U) of any linear combination in any polygonal domain U ⊆ L ​ – ​ Σ U\subseteq L{\,\text{--}\,}\varSigma in any line L ⊄ Σ L\not\subset\varSigma. In particular, the number of real zeros 𝒩 ⁡ ( Ω / Re ⁡ L) {\mathcal{N}}(\Omega/\operatorname{Re}L) can be at most d ⋅ 𝒩 ⁡ ( Ω) d\cdot{\mathcal{N}}(\Omega), where d d is the degree of Ω \Omega. Indeed, the intersection L ∩ Σ L\cap\varSigma consists of no more than d d points which may subdivide the real (projective) line into to no more than d d intervals. Each interval lies inside a triangle T T free from points of Σ \varSigma, hence the number of isolated zeros on it does not exceed 𝒩 ⁡ ( Ω) {\mathcal{N}}(\Omega).

Conversely, if there is a tiling L ​ – ​ Σ = ⋃ U ¯ i L{\,\text{--}\,}\varSigma=\bigcup\overline{U}_{i} by simply connected polygonal domains U i U_{i} and for each domain the maximal number of zeros 𝒩 ⁡ ( Ω / U i) = sup f ∈ ℒ X ​ ( U i) #⁡ { t: f ⁡ ( t) = 0 } {\mathcal{N}}(\Omega/U_{i})=\sup_{f\in\mathscr{L}_{X}(U_{i})}\#\{t\colon f(t)=0\} is finite, then one can easily produce an upper bound for 𝒩 ⁡ ( Ω) {\mathcal{N}}(\Omega) by simply adding these bounds, 𝒩 ⁡ ( Ω) ⩽ ∑ i 𝒩 ⁡ ( Ω / U i) {\mathcal{N}}(\Omega)\leqslant\sum_{i}{\mathcal{N}}(\Omega/U_{i}).

###### Remark 22 (semicontinuity)

When counting zeros, one can easily pass from open to closed polygons disjoint from Σ \varSigma, provided that the bound for the number of zeros remains uniform.

Indeed, assuming that the number of zeros in *any*closed triangle T ¯ ⊂ L ​ – ​ Σ \overline{T}\subset L{\,\text{--}\,}\varSigma does not exceed some N N, one can immediately see that the same bound holds also for an arbitrary open triangle T T. If T T contains N + 1 N+1 roots of some linear combination, one can construct a closed triangle T ¯ ⋐ T \overline{T}\Subset T which contains all these roots, in contradiction with the initial assumption.

By the same token, in the definition of the counting function ( 20) it is sufficient to consider only closed triangles T ¯ \overline{T} from a dense subset 𝒯 ′ \mathscr{T}^{\prime} in the space of all triangles 𝒯 ⁡ ( ℙ m ​ – ​ Σ) \mathscr{T}({\mathbb{P}}^{m}{\,\text{--}\,}\varSigma) disjoint with Σ \varSigma. If

 | sup T ¯ ∈ 𝒯 ′ sup f ∈ ℒ X ​ ( T) #⁡ { t ∈ T: f ⁡ ( t) = 0 } = N < + ∞, \sup_{\overline{T}\in\mathscr{T}^{\prime}}~\sup_{f\in\mathscr{L}_{X}(T)}\#\{t\in T\colon f(t)=0\}=N<+\infty, |  |

then 𝒩 ⁡ ( Ω) {\mathcal{N}}(\Omega) is also finite and equal to N N. Indeed, if some linear combination f f has N + 1 N+1 roots in an “excluded” open triangle T ∉ 𝒯 ′ T\notin\mathscr{T}^{\prime}, then one can find an arbitrarily close closed triangle T ¯ ∈ 𝒯 ′ \overline{T}\in\mathscr{T}^{\prime}, eventually belonging to a different line L ′ ⊂ ℙ m L^{\prime}\subset{\mathbb{P}}^{m}, which contains at least N + 1 N+1 roots counted with multiplicity in contradiction with the initial assumption. This follows from the fact that isolated complex roots of holomorphic functions cannot disappear by small perturbations by the Weierstrass preparation theorem.

### 2.7 Main theorem in the abstract form and discussion

The constructive solution of the infinitesimal Hilbert 16th problem (Theorem 2) is obtained as a corollary to the following general fact about solutions of systems of differential equations.

###### Theorem 7 ( existential bound)

Let Ω \Omega be a rational matrix 1-form of degree d d on the projective space 𝕄 = ℙ m \mathbb{M}={\mathbb{P}}^{m}, and ( 12) the corresponding linear system of size ℓ × ℓ \ell\times\ell. Assume that:

1. (I)

Ω \Omega is integrable;

2. (R)

Ω \Omega is regular;

3. (U)

Ω \Omega is quasiunipotent.

Then the value of the counting function 𝒩 ⁡ ( Ω) {\mathcal{N}}(\Omega) is finite,

 | 𝒩 ⁡ ( Ω) < + ∞. {\mathcal{N}}(\Omega)<+\infty. |  |

###### Theorem 8 ( constructive bound)

In the assumptions of Theorem 7 and the additional assumption,

1. (Q)

Ω \Omega is defined over ℚ {\mathbb{Q}} and its size is s = 𝐒 ⁡ ( Ω) s=\mathbf{S}\left(\Omega\right),

the above finiteness is explicit:

 | 𝒩 ⁡ ( Ω) ⩽ s 2 Poly ⁡ ( d, ℓ, m). {\mathcal{N}}(\Omega)\leqslant s^{2^{\operatorname{\textup{Poly}}(d,\ell,m)}}. |  | (21) |

Here Poly ⁡ ( d, ℓ, m) ⩽ O + ​ ( ( d ​ ℓ 4 ​ m) 5) \operatorname{\textup{Poly}}(d,\ell,m)\leqslant O^{+}\bigl((d\ell^{4}m)^{5}\bigr).

Recall that the O + ​ ( ⋅) O^{+}({\,\boldsymbol{\cdot}}\,) -notation was introduced in Remark 1. The reduction from Theorem 8 to Theorem 2 is made possible by virtue of the following observation which improves the “folklore” Theorem 5.

###### Theorem 9 ( constructive derivation)

The logarithmic derivative Ω = d ​ X ⋅ X − 1 \Omega=\,\mathrm{d}X\cdot X^{-1} of the period matrix for Abelian integrals ( 11), and hence the corresponding Picard–Fuchs system ( 12) is defined over ℚ {\mathbb{Q}}.

The size s = 𝐒 ⁡ ( Ω) s=\mathbf{S}\left(\Omega\right), dimension ℓ \ell and the degree d = deg ⁡ Ω d=\deg\Omega of the corresponding rational matrix function are explicitly bounded from above as follows,

 | s ⩽ 2 Poly ⁡ ( n), d ⩽ O ⁡ ( n 2), m ⩽ O ⁡ ( n 2), ℓ = n 2, s\leqslant 2^{\operatorname{\textup{Poly}}(n)},\quad d\leqslant O(n^{2}),\quad m\leqslant O(n^{2}),\quad\ell=n^{2}, |  | (22) |

where n + 1 n+1 is the degree of the Hamiltonians.

*Proof of Theorem 2*. Plugging the estimates ( 22) into the bound ( 21), we obtain the bound for the number of zeros of Abelian integrals,

 | 𝒩 ⁡ ( n, n) ⩽ 2 Poly ⁡ ( n) ⋅ 2 O ⁡ ( n ( 2 + 8 + 2) ⋅ 5) ⩽ 2 2 O ⁡ ( n 60 ​ ln ⁡ n) ⩽ 2 2 O + ​ ( n 60). {\mathcal{N}}(n,n)\leqslant 2^{\operatorname{\textup{Poly}}(n)\cdot\,2^{O\left(n^{(2+8+2)\cdot 5}\right)}}\leqslant 2^{2^{O(n^{60}\ln n)}}\leqslant 2^{2^{O^{+}(n^{60})}}. |  | (23) |

It remains to notice that O + ​ ( n 60) ⩽ O ⁡ ( n 61) O^{+}(n^{60})\leqslant O(n^{61}). This calculation illustrates the need for the O + O^{+} -notation, as similar estimates will appear in the future.

In fact, Theorem 7 can be relatively easily proved by the application of tools from the Fewnomial theory developed by A. Khovanskiĭ Kho 91 and finiteness results for analytic functions achieved by A. Gabrielov Gab 68. Unfortunately, this straightforward approach does not allow for application of the “quantization principle” mentioned in § 2.5.

We give an alternative proof of Theorem 7 that admits the required “quantization” and ultimately yields Theorem 8. The main ideas of this proof are outlined below in § 2.8.

The conditions of Theorem 8 are very close to optimal. Indeed, without the integrability assumption the system has no well-defined solutions. Omission of the regularity assumption allows to construct a linear system on ℙ 1 {\mathbb{P}}^{1} (i.e., in the smallest dimension), with infinitely many zeros of solutions on a real interval accumulating to a singular point, see Yak 05.

The assumption of quasiunipotence also cannot be considerably relaxed beyond the limits indicated in Remark 11: without the assumption zeros of solutions also can accumulate to a singular point along the real line Yak 05.

### 2.8 Strategy of the proof

In this section we briefly outline the strategy of the proof of Theorems 7, 8 and 9.

#### 2.8.1 The analytic core: de la Vallée Poussin theorem and its generalizations.

The basic tool for the estimates of the number of isolated zeros is a complex analog of the classical de la Vallée Poussin theorem dlVP 29. This theorem asserts that for a homogeneous *monic*linear ordinary differential equation with holomorphic coefficients

 | y ( k) + a 1 ​ ( t) ​ y ( k − 1) + ⋯ + a k ​ ( t) ​ y = 0, t ∈ γ ⊂ ℂ, y^{(k)}+a_{1}(t)\,y^{(k-1)}+\cdots+a_{k}(t)\,y=0,\hskip 18.49988ptt\in\gamma\subset{\mathbb{C}}, |  |

the variation of argument of any solution y ⁡ ( t) y(t) along a circular arc γ \gamma of known length can be explicitly bounded in terms of the *uniform upper bounds*A i = sup t ∈ γ | a i ​ ( t) | A_{i}=\sup_{t\in\gamma}|a_{i}(t)|, i = 1, …, k i=1,\dots,k, of the non-principal coefficients of this equation along the arc ( Yak 99, Theorem 2.6, Corollary 2.7). This property of high order differential equations is in stark contrast with *systems*of first order linear equations with bounded coefficients, as was discovered in Nov 01. The assumption that the equation is monic (i.e., its principal coefficient is identically equal to 1 1) is not an obstruction as long as the arc does not pass near singular points of the equation, which correspond to zeros of the leading coefficient of a general homogeneous equation

 | a 0 ​ ( t) ​ y ( k) + ⋯ + a k ​ ( t) ​ y = 0. a_{0}(t)\,y^{(k)}+\cdots+a_{k}(t)\,y=0. |  | (24) |

Computing variation of argument of solutions along an arc that passes through (or very close to) a singular point (a root of a 0 ​ ( ⋅) a_{0}({\,\boldsymbol{\cdot}}\,)) is impossible in general.

#### 2.8.2 From a Pfaffian integrable system to an isomonodromic family of homogeneous linear ordinary differential equations.

The system of Pfaffian equations ( 12) can be reduced to a scalar equation of order k ⩽ ℓ 2 k\leqslant\ell^{2} in two steps. First, we note that the phase space 𝕄 = ℙ m \mathbb{M}={\mathbb{P}}^{m} of the system ( 12) is birationally equivalent to the product ℙ m − 1 × ℙ 1 {\mathbb{P}}^{m-1}\times{\mathbb{P}}^{1}, cf. with Remark 7; moreover, this equivalence can be chosen so that any given projective line ℙ 1 ≅ L ⊂ ℙ m {\mathbb{P}}^{1}\cong L\subset{\mathbb{P}}^{m} becomes a member of the pencil of projective lines. Denoting the parameters of the pencil by λ ^ ∈ ℙ m − 1 {\hat{\lambda}}\in{\mathbb{P}}^{m-1} and the corresponding lines by ℙ λ ^ 1 = { λ ^ } × ℙ 1 {\mathbb{P}}^{1}_{\hat{\lambda}}=\{{\hat{\lambda}}\}\times{\mathbb{P}}^{1}, we can restrict the Pfaffian systems on the lines from this pencil to obtain a parametric family of Pfaffian equations on the projective line ℙ 1 {\mathbb{P}}^{1} as in Remark 7. Since the latter space is one-dimensional, choosing an affine chart t t on ℙ 1 {\mathbb{P}}^{1} allows to re-write ( 12) as a linear system of first order ordinary differential equations. Namely, the matrix Pfaffian 1-form restricted on each line ℙ λ ^ 1 = { λ ^ } × ℙ 1 {\mathbb{P}}^{1}_{{\hat{\lambda}}}=\{{\hat{\lambda}}\}\times{\mathbb{P}}^{1} in the fixed chart t t takes the form

 | Ω | { λ ^ } × ℙ 1 = A ⁡ ( λ ^) ​ d ​ t, λ ^ ∈ ℙ m − 1. \Omega|_{\{{\hat{\lambda}}\}\times{\mathbb{P}}^{1}}=A({\hat{\lambda}})\,\mathrm{d}t,\hskip 18.49988pt{\hat{\lambda}}\in{\mathbb{P}}^{m-1}. |  | (25) |

The system ( 12) becomes in this chart a system of linear equations

 | d ​ X d ​ t = A ⁡ ( λ ^) ⋅ X, X = X ⁡ ( λ ^, t), \frac{\,\mathrm{d}X}{\,\mathrm{d}t}=A({\hat{\lambda}})\cdot X,\hskip 18.49988ptX=X({\hat{\lambda}},t), |  | (26) |

with the singular loci Σ λ ^ = Σ ∩ ℙ λ ^ 1 \varSigma_{{\hat{\lambda}}}=\varSigma\cap{\mathbb{P}}^{1}_{{\hat{\lambda}}} (the matrix A ⁡ ( λ ^, ⋅) A({\hat{\lambda}},{\,\boldsymbol{\cdot}}\,) is not defined if the entire line ℙ λ ^ 1 {\mathbb{P}}^{1}_{{\hat{\lambda}}} belongs to Σ \varSigma, yet such values of the parameter constitute a proper semialgebraic set in ℙ m − 1 {\mathbb{P}}^{m-1}). Clearly, the regularity of the initial system ( 12) implies the regularity of all systems in the family ( 26).

The condition of integrability of the initial system (either on ℙ m {\mathbb{P}}^{m} or on ℙ m − 1 × ℙ 1 {\mathbb{P}}^{m-1}\times{\mathbb{P}}^{1}, as the two are equivalent) implies that the family of the equations ( 26) is *isomonodromic*in the following sense.

Let γ ⊂ ℙ λ ^ 0 1 \gamma\subset{\mathbb{P}}^{1}_{{\hat{\lambda}}_{0}} be an arbitrary closed path in the projective line, disjoint with the singular locus Σ λ ^ \varSigma_{{\hat{\lambda}}}. Then by continuity there exists a small neighborhood U U of λ ^ 0 {\hat{\lambda}}_{0} in ℙ m − 1 {\mathbb{P}}^{m-1} such that for all values of the parameter from this neighborhood, the corresponding singular loci Σ λ ^ \varSigma_{{\hat{\lambda}}} are still disjoint with γ \gamma, and hence for all such λ ^ {\hat{\lambda}} the monodromy of the system ( 26) along γ \gamma is still well defined. The isomonodromy condition means that the corresponding operators M γ, λ ^ M_{\gamma,{\hat{\lambda}}} do not depend on λ ^ ∈ U {\hat{\lambda}}\in U, or, more precisely, remain in the same conjugacy class.

This condition will be especially important when the singular locus Σ λ ^ \varSigma_{{\hat{\lambda}}} undergoes a “bifurcation” at λ ^ 0 {\hat{\lambda}}_{0}, e.g., Σ λ ^ 0 \varSigma_{{\hat{\lambda}}_{0}} contains an isolated singularity of high multiplicity at t 0 ∈ ℂ t_{0}\in{\mathbb{C}} (a pole of order k ⩾ 2 k\geqslant 2 for the corresponding matrix A ⁡ ( λ ^ 0, ⋅) A({\hat{\lambda}}_{0},\cdot)), while all nearby matrices have simple singularities (poles) at k k nearby points t i ​ ( λ ^) t_{i}({\hat{\lambda}}), i = 1, …, k i=1,\dots,k. The monodromy around the circle encompassing all these points (the so called *classical monodromy*of a singularity, AGV 88) is conjugated to the monodromy of a small loop around t 0 t_{0}.

###### Remark 23

From now on we work only with the product space ℙ m − 1 × ℙ 1 {\mathbb{P}}^{m-1}\times{\mathbb{P}}^{1} and parametric equations and systems of equations on this product. To simplify the notation, we replace the parameter space ℙ m − 1 {\mathbb{P}}^{m-1} by ℙ m {\mathbb{P}}^{m} and denote the coordinates on it by λ \lambda instead of λ ^ {\hat{\lambda}}.

On the second step we reduce the parametric system of linear ordinary differential equations ( 26) to a family of scalar high order equations in the most straightforward way, by successive derivations and linear elimination. As a result, we obtain a linear equation with coefficients that are polynomials in t t and the parameters λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m},

 | a 0 ​ ( λ, t) ​ y ( k) + ⋯ + a k ​ ( λ, t) ​ y = 0, t ∈ ℂ, λ ∈ ℂ m. a_{0}(\lambda,t)\,y^{(k)}+\cdots+a_{k}(\lambda,t)\,y=0,\hskip 18.49988ptt\in{\mathbb{C}},\ \lambda\in{\mathbb{C}}^{m}. |  | (27) |

Integrability and regularity of the initial system means that each equation in the family ( 27) is Fuchsian and the family as a whole is isomonodromic and quasiunipotent. In what follows we call this family the *derived equation*(s). However, two problems arise in connection with this process:

1. (1)

The leading coefficient of the derived equation ( 27) has isolated zeros, in general much more numerous than the singular points of the original system.

2. (2)

For specific values of the parameters belonging to a proper algebraic subset 𝒮 ⊂ ℙ m {\mathscr{S}}\subset{\mathbb{P}}^{m}, the leading coefficient may degenerate identically, a 0 ​ ( λ, ⋅) ≡ 0 a_{0}(\lambda,{\,\boldsymbol{\cdot}}\,)\equiv 0 for λ ∈ 𝒮 \lambda\in{\mathscr{S}}.

The second problem implies that as λ → 𝒮 \lambda\to{\mathscr{S}}, the equation undergoes what is usually referred to as a *singular perturbation*, the situation when the coefficient of the highest order derivative tends to zero. Behavior of solutions of singularly perturbed equations may be extremely complicated, and this scenario, if it indeed occurs, renders the entire approach via de la Vallée Poussin’s theorem unworkable, since after reducing to the monic form the coefficients of the corresponding linear equations would be large on the entire plane (or most of it), not just near singular points. Note that we can ignore the exceptional value of parameters λ ∈ 𝒮 \lambda\in{\mathscr{S}} itself by virtue of the Remark 22, provided that the bound for the number of zeros remains uniform.

Somewhat miraculously, the “singular perturbation” that occurs in the reduction of a *regular*system to the derived equation, is only apparent: together with the leading coefficient, all other coefficients of the equation ( 27) necessarily vanish for the same values of the parameter 𝒮 {\mathscr{S}}. This phenomenon was first discovered (in a simpler context) by A. Grigoriev Gri 01; Gri 03.

The analysis carried out in BY 10 is reproduced and generalized in § 3 to show that if we consider the norms of these coefficients ‖ a i ​ ( λ, ⋅) ‖ \|a_{i}(\lambda,{\,\boldsymbol{\cdot}}\,)\| (in the sense of Definition 13), then the maximum of the ratios of these norms, called the *slope*of the linear homogeneous equation, is uniformly bounded,

 | max ⁡ sup λ ∈ ℙ m ​ – ​ 𝒮 i = 1, …, k ⁡ ‖ a i ​ ( λ, ⋅) ‖ ‖ a 0 ​ ( λ, ⋅) ‖ < + ∞. \max_{i=1,\dots,k}\sup_{\lambda\in{\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}}}\frac{\|a_{i}(\lambda,{\,\boldsymbol{\cdot}}\,)\|}{\|a_{0}(\lambda,{\,\boldsymbol{\cdot}}\,)\|}<+\infty. |  | (28) |

We note that the finiteness of this uniform bound depends crucially on the *regularity*of the original system, and does not hold in the more general context of BY 10.

Finiteness of this supremum for a general regular family ( 26) implies, by the “quantization principle”, an explicit computable bound provided that the initial system ( 26) is defined over ℚ {\mathbb{Q}}.

#### 2.8.3 Invariant slope.

The constructions described in § 2.8.2, along with the techniques of BY 10, provide a uniform bound for the number of zeros of solutions as long as the singular points remain well apart. A substantial difficulty which needs to be addressed (and cannot be circumvented for general Fuchsian systems) is the study of colliding singular points.

However, under the regularity and integrability assumptions, this problem can be resolved. It turns out that for *Fuchsian equations*(operators) the slope as it is defined in ( 28) remains uniformly bounded from above even when one is allowed to replace the original affine chart by an arbitrary different affine (and more generally, even a conformally equivalent) chart on ℙ 1 {\mathbb{P}}^{1}. This fact, somewhat surprising (it seems to have gone unnoticed until now), means that the collision of singularities can be treated by a proper resolution of singularities, as explained in § 2.8.4.

In Definition 29 we introduce the notion of the *invariant slope*of a linear operator, and subsequently show that it is finite and uniformly bounded. For technical reasons we need to consider not only conformal changes of the independent variable, but also symmetrization of differential operators with respect to an arbitrary circle or line in ℙ 1 {\mathbb{P}}^{1}. The corresponding inequality is asserted in Principal Lemma 33, whose proof is presented in section § 3.

#### 2.8.4 Scale invariance and construction of an admissible configuration of slits.

The bounds on the slope discussed in § 2.8.3, imply that without loss of generality one may assume that the leading coefficient of the derived equation ( 27) is of unit norm with the remaining (non-leading) coefficients uniformly bounded. By the de la Vallée Poussin theorem, this means that the variation of argument of any solution can be explicitly majorized along any arc (circular or rectilinear), which does not pass near the singular points where the leading coefficient vanishes. The meaning of this dangerous proximity can be made precise using the scale invariance of the invariant slope: the upper bounds for the variation of arguments of an arbitrary solution of the differential equation are possible for *arcs whose length is not very large relative to the distance to the singular locus*. This scale invariance is one of the the key tools in the subsequent construction. For brevity we refer to such arcs as “short arcs”. For instance, any sufficiently small circular arc centered at an isolated singular point, is “short” in this sense.

One may attempt to slit the plane with deleted singular points of the derived equation by such “short arcs” into finitely many simply connected domains U i U_{i} and apply to each domain the argument principle. This would imply an explicit upper bound for the counting function 𝒩 ⁡ ( Ω / U i) {\mathcal{N}}(\Omega/U_{i}), see Remark 21. Unfortunately, such simplistic solution is impossible, since any arc with an endpoint at a singular point is necessarily “long”.

To resolve this problem, we show that one can bound the number of zeros of (multivalued) solutions of the derived equation in punctured disks around singular points, and more generally in annuli, under the assumption that the monodromy of this equation along the equator of the annuli has eigenvalues of unit modulus only, and that the bounding circles are “short”. Our approach goes back to the work RY 96 and is based on the idea called *the Petrov trick*after the pioneering work by G. Petrov Pet 90.

On the second step of the construction (in § 4) we construct a system of “short arcs” subdividing the nonsingular set into simply connected domains and *annuli*bounded by nested circles. This comes in the form of a suitable clustering: we need to identify groups of singular points, such that distance between them is much smaller compared to distances to other singular points (outside the cluster). Then after a suitable “magnification” one can treat points from the same cluster as “being well apart”. However, the construction needs to be iterated, since much smaller clusters can be parts of the larger clusters. The accurate construction involves ideas in the spirit of the Fulton-MacPherson compactification of the configuration space (see FM 94).

The main difficulty to deal with in this second step is an effective construction of the system of slits so that all annuli that appear at the end will have the required monodromy, and the explicit calculation of the “normalized length” of these slits. The source of difficulty is, among other things, the apparent non-algebraicity of the monodromy as a function of the parameters: in general, the monodromy of solutions of linear systems cannot be written in closed form. The way around this obstacle is to use the quasiunipotence and integrability. The quasiunipotence guarantees that the monodromy is quasiunipotent along the *small loops*which may encircle *several*colliding singularities. The integrability (isomonodromy) allows to conclude that the monodromy remains quasiunipotent as long as the topological configuration of slits and singular points remains unchanged. The latter condition is topological (selection of a connected component in a suitable configuration space), and it is known that all connected components of semialgebraic sets are themselves semialgebraic and effectively constructible BPR 03. This allows the application of the “quantization principle”, transforming the existential finite bound for the “normalized length” of the admissible system of slits into an explicit upper bound for systems originally defined over ℚ {\mathbb{Q}} in exactly the same way as was done in the first step.

Knowing the explicit length of admissible system of slits along “short” arcs (the “cluster diameter” as it is introduced in Definition 50) and the invariant slope of the equations allows to complete the proof of Theorem 8. This program is realized in § 4.

#### 2.8.5 Effective derivation of the Picard–Fuchs system.

To derive Theorem 2 from Theorem 8, we need to show that the Picard–Fuchs system provided by Theorem 5, is in fact defined over ℚ {\mathbb{Q}} for a suitably chosen parameter space. The arguments used in the “proof” of Theorem 5, as well as some other standard approaches Gav 98; Gav 99, do not allow to estimate the size (complexity) of the Picard–Fuchs system ( 12).

The necessary bounds follow from the explicit derivation of the Picard–Fuchs system, suggested in Yak 02 and based on an earlier work NY 01. We reproduce it below in Appendix A and derive all the required complexity estimates.

## 3 From an integrable Pfaffian system to an isomonodromic family of Fuchsian linear equations

In this section we work with an integrable rational Pfaffian system ( 12) of dimension ℓ × ℓ \ell\times\ell and degree d d on the product space ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1}, defined over ℚ {\mathbb{Q}}, of known complexity (size) s = 𝐒 ⁡ ( Ω) s=\mathbf{S}\left(\Omega\right).

Because of the integrability, we may consider the system as an isomonodromic family of linear systems on ℙ 1 {\mathbb{P}}^{1}, parameterized by the parameters λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m}, and write

 | d ​ X | ℙ λ 1 = Ω λ ​ X, Ω λ = A ⁡ ( λ, t) ​ d ​ t, λ ∈ ℙ m, \,\mathrm{d}X|_{{\mathbb{P}}^{1}_{\lambda}}=\Omega_{\lambda}X,\qquad\Omega_{\lambda}=A(\lambda,t)\,\mathrm{d}t,\quad\lambda\in{\mathbb{P}}^{m}, |  | (29) |

in an affine chart t t on ℙ λ 1 {\mathbb{P}}^{1}_{\lambda}. Denote the singular locus of the system ( 29) by Σ λ ⊂ ℙ λ 1 ≅ ℙ 1 \varSigma_{\lambda}\subset{\mathbb{P}}^{1}_{\lambda}\cong{\mathbb{P}}^{1}.

The main result proved in this section is the effective transformation of the family of linear systems ( 29) to a parametric family of scalar equations of a high order,

 | D λ = ∂ k + R 1 ( λ, t) ∂ k − 1 + ⋯ + R k ( λ, t), R j ∈ ℚ ( λ, t), D_{\lambda}=\partial^{k}+R_{1}(\lambda,t)\,\partial^{k-1}+\cdots+R_{k}(\lambda,t),\qquad R_{j}\in{\mathbb{Q}}(\lambda,t), |  | (30) |

also defined over ℚ {\mathbb{Q}}, with an explicit control on the *size*of the family (defined as the sum of the sizes of all rational coefficients R j ∈ ℚ ⁡ ( λ, t) R_{j}\in{\mathbb{Q}}(\lambda,t), cf. with Definition 14). For a family of regular operators this turns out to be sufficient for explicitly controlling the *slope*(see ( 28)) of the operators ( 30) *uniformly over all admissible λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m}*.

The rationale behind this step is the stark difference between systems of first order equations and scalar high order equations in what concerns zeros of their solutions, see Nov 01. To formulate the result more precisely, we need to elaborate the definition of the slope from ( 28) and make it conformally invariant.

### 3.1 Differential operators of higher order and their affine slope

We will work with *homogeneous*linear ordinary differential equations with rational coefficients in the *monic*form

 | y ( k) + R 1 ​ ( t) ​ y ( k − 1) + ⋯ + R k − 1 ​ ( t) ​ y ′ + R k ​ ( t) ​ y = 0, R 1, …, R k ∈ ℂ ⁡ ( t), y^{(k)}+R_{1}(t)\,y^{(k-1)}+\cdots+R_{k-1}(t)\,y^{\prime}+R_{k}(t)y=0,\\ R_{1},\dots,R_{k}\in{\mathbb{C}}(t), |  | (31) |

(so that the leading coefficient is identically 1) and their parametric families. Because of the homogeneity, the monic equation ( 31) can be re-written in the form D ​ y = 0 Dy=0, where D D is a differential operator

 | D = a 0 ( t) ∂ k + a 1 ( t) ∂ k − 1 + ⋯ + a k − 1 ( t) ∂ + a 0 ( t), ∂ = d d ​ t, D=a_{0}(t)\,\partial^{k}+a_{1}(t)\,\partial^{k-1}+\cdots+a_{k-1}(t)\,\partial+a_{0}(t),\quad\partial=\frac{\,\mathrm{d}}{\,\mathrm{d}t}, |  | (32) |

with *polynomial coefficients*a 0, a 1, …, a k ∈ ℂ ⁡ [t] a_{0},a_{1},\dots,a_{k}\in{\mathbb{C}}[t], a 0 ≢ 0 a_{0}\not\equiv 0 (we denote symbolically this fact by writing D ∈ ℂ [∂, t] D\in{\mathbb{C}}[\partial,t]). Under the assumption

 | gcd ⁡ ( a 0, ⋯, a k) ℂ ⁡ [t] = 1 \gcd(a_{0},\cdots,a_{k})_{{\mathbb{C}}[t]}=1 |  | (33) |

the coefficients a i a_{i} are determined uniquely modulo a *scalar*common factor. This makes the following definition self-consistent.

###### Definition 24

The (*affine*) *slope*∠ ​ D \angle D of a linear ordinary differential operator D ∈ ℂ [t, ∂] D\in{\mathbb{C}}[t,\partial] with polynomial coefficients as in ( 32), is the finite number

 | ∠ ​ D = max j = 1, …, k ⁡ ‖ a j ‖ ‖ a 0 ‖ < + ∞. \angle D=\max_{j=1,\dots,k}\frac{\|a_{j}\|}{\|a_{0}\|}<+\infty. |  | (34) |

The *slope*of a homogeneous linear ordinary differential equation with *rational*coefficients ( 31) is by definition the slope of the linear operator D D with polynomial coefficients ( 32)–( 33), such that ( 31) is equivalent to the equation D ​ y = 0 Dy=0.

The affine slope of an operator is a numeric measure of proximity of the corresponding equation to the “singular limit”, the result of perturbing a linear equation so that the highest derivative enters with a small parameter. Knowing the slope of a homogeneous equation suffices to place an explicit upper bound for the variation of argument of any nontrivial solution of this equation along an arc that does not pass through the singular points of this equation.

###### Lemma 25 ( Lemma 8 from BY 10)

Let D D be a differential operator ( 32) of order k k with polynomial coefficients of degree ⩽ d \leqslant d and the slope S = ∠ ​ D S=\angle D, and γ \gamma a closed circular arc or line segment disjoint with the singular locus Σ = { a 0 = 0 } ⊂ ℂ \varSigma=\{a_{0}=0\}\subset{\mathbb{C}}, which belongs to the disk of radius R R centered at the origin.

Then the variation of argument of any nonzero solution of the homogeneous equation D ​ y = 0 Dy=0 along the arc γ \gamma is explicitly bounded,

 | Var ⁡ Arg ⁡ y ⁡ ( t) | γ ⩽ k ​ S ​ | γ | ​ ( R / r) O ⁡ ( d). \operatorname{Var}\operatorname{Arg}y(t)|_{\gamma}\leqslant kS\,|\gamma|\,(R/r)^{O(d)}. |  | (35) |

where | γ | |\gamma| is the length of the arc, r = dist ⁡ ( γ, Σ) r=\operatorname{dist}(\gamma,\varSigma).

###### Remark 26

Homogeneous linear differential equations with rational coefficients are the natural means of describing finite dimensional linear subspaces of holomorphic functions on ℙ {\mathbb{P}}, invariant by monodromy around a finite locus Σ \varSigma. For instance, if ( 12) is a regular Pfaffian system on the projective line ℙ 1 {\mathbb{P}}^{1} with a singular locus Σ \varSigma, then for any open set U ⊆ ℙ ​ – ​ Σ U\subseteq{\mathbb{P}}{\,\text{--}\,}\varSigma the linear space ℒ X ​ ( U) \mathscr{L}_{X}(U) spanned by components of any fundamental matrix solution X X of the system ( 12) is invariant by the monodromy, and can be defined by the homogeneous linear equation

 | det ( y x 1 ​ ( t) ⋯ x ℓ ​ ( t) d d ​ t ​ y d d ​ t ​ x 1 ​ ( t) ⋯ d d ​ t ​ x ℓ ​ ( t) ⋱ d ℓ d ​ t ℓ ​ y d ℓ d ​ t ℓ ​ x 1 ​ ( t) ⋯ d ℓ d ​ t ℓ ​ x ℓ ​ ( t)) = 0, \det\begin{pmatrix}y&x_{1}(t)&\cdots&x_{\ell}(t)\\ \frac{\,\mathrm{d}}{\,\mathrm{d}t}y&\frac{\,\mathrm{d}}{\,\mathrm{d}t}x_{1}(t)&\cdots&\frac{\,\mathrm{d}}{\,\mathrm{d}t}x_{\ell}(t)\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\,\mathrm{d}^{\ell}}{\,\mathrm{d}t^{\ell}}y&\frac{\,\mathrm{d}^{\ell}}{\,\mathrm{d}t^{\ell}}x_{1}(t)&\cdots&\frac{\,\mathrm{d}^{\ell}}{\,\mathrm{d}t^{\ell}}x_{\ell}(t)\end{pmatrix}=0, |  | (36) |

where x 1 ​ ( ⋅), …, x ℓ ​ ( ⋅) x_{1}({\,\boldsymbol{\cdot}}\,),\dots,x_{\ell}({\,\boldsymbol{\cdot}}\,) is a basis of ℒ X ​ ( U) \mathscr{L}_{X}(U). When expanded in the elements of the first column and reduced to the monic form, the identity ( 36) yields a Fuchsian 4 4 4 Recall that a linear higher order differential operator is Fuchsian if it is regular, i.e., its solutions, multivalued functions on ℂ ​ – ​ Σ F {\mathbb{C}}{\,\text{--}\,}\varSigma_{F}, exhibit polynomial growth as in ( 13). As is well-known, Fuchsian operators admit explicit description in terms of the order of zeros of their coefficients at the singular locus ( IY 08, Proposition 19.18). differential operator of order ℓ \ell with rational coefficients, provided that the functions x i ​ ( t) x_{i}(t) have moderate growth near all points of the singular locus Σ \varSigma ( IY 08, Proposition 19.19).

This observation allows to define the slope of *any*finite-dimensional subspace ℒ ⊂ 𝒪 ⁡ ( U) \mathscr{L}\subset\mathscr{O}(U), U ⊆ ℙ ​ – ​ Σ U\subseteq{\mathbb{P}}{\,\text{--}\,}\varSigma, invariant by the monodromy transformations associated with the fundamental group π 1 ​ ( ℙ ​ – ​ Σ, t 0) \pi_{1}({\mathbb{P}}{\,\text{--}\,}\varSigma,t_{0}), t 0 ∈ U t_{0}\in U, assuming that functions from ℒ \mathscr{L} grow moderately near Σ \Sigma. The slope ∠ ​ ℒ \angle\mathscr{L} is then defined as the slope of the corresponding differential operator D = D ℒ D=D_{\mathscr{L}}, the differential operator with rational coefficients of the minimal order ord ⁡ D = dim ℂ ℒ \operatorname{ord}D=\dim_{\mathbb{C}}\mathscr{L}, which vanishes on ℒ \mathscr{L}:

 | ∠ ℒ = ∠ D ℒ, D ℒ ∈ ℂ [t, ∂], ord D ℒ = dim ℂ ℒ, ∀ f ∈ ℒ D ℒ f = 0. \begin{gathered}\angle\mathscr{L}=\angle D_{\mathscr{L}},\qquad D_{\mathscr{L}}\in{\mathbb{C}}[t,\partial],\\ \operatorname{ord}D_{\mathscr{L}}=\dim_{\mathbb{C}}\mathscr{L},\qquad\forall f\in\mathscr{L}\quad D_{\mathscr{L}}f=0.\end{gathered} |  | (37) |

Note that this *does not depend*on the choice of operator D ℒ D_{\mathscr{L}}, as any two linear differential operators with identical kernels agree up to multiplication of the coefficients by a common factor. The slope *does*however depend on the choice of the affine chart t t.

###### Remark 27

The exact choice of the simply connected domain U U is not important as long as it is open and disjoint with the singular locus Σ \varSigma, since the rational coefficients of the differential equation are uniquely determined by their values in any open subset of ℙ {\mathbb{P}}. This allows us to omit the indication of the domain in the notations.

### 3.2 Conformal invariance and symmetrization

The notion of a slope as it is defined in ( 34) and ( 37) suffers from several drawbacks, the most serious being its dependence on the chart with respect to which the norms of the polynomial coefficients are computed. Applications of different conformal automorphisms (changes of the independent variable) of the form

 | φ: t ⟼ α ​ t + β γ ​ t + δ, det ( α β γ δ) ≠ 0, \varphi\colon t\longmapsto\frac{\alpha t+\beta}{\gamma t+\delta},\qquad\det\begin{pmatrix}\alpha&\beta\\ \gamma&\delta\end{pmatrix}\neq 0, |  | (38) |

transform any linear subspace ℒ ⊂ 𝒪 ⁡ ( U) \mathscr{L}\subset\mathscr{O}(U) into another subspace

 | φ ∗ ​ ℒ = { φ ∗ ​ f: f ∈ ℒ } ⊂ 𝒪 ⁡ ( φ − 1 ​ ( U)), φ ∗ ​ f = f ∘ φ. \varphi^{*}\mathscr{L}=\{\varphi^{*}f\colon f\in\mathscr{L}\}\subset\mathscr{O}(\varphi^{-1}(U)),\qquad\varphi^{*}f=f\circ\varphi. |  | (39) |

having the same dimension and invariant by the monodromy operators around the transformed singular locus Σ ′ = φ − 1 ​ ( Σ) \varSigma^{\prime}=\varphi^{-1}(\varSigma). We will modify the definition of the slope so that it will become invariant under the actions of the conformal isomorphisms ( 39).

Besides the action of conformal isomorphisms, we will need yet another operator on linear spaces of functions, the *symmetrization*(or *conjugacy*) with respect to a circle/line. The need for symmetrization will become clear in the context of Lemma 44. Recall that by the Schwarz symmetry principle, for any function f ∈ 𝒪 ⁡ ( U) f\in\mathscr{O}(U) holomorphic in a domain U ⊆ ℂ U\subseteq{\mathbb{C}}, the function f † f^{\dagger} defined in the domain U † U^{\dagger} by the formula

 | f † ​ ( t) = f ⁡ ( t ¯) ¯, U † = { t ¯: t ∈ U }, f^{\dagger}(t)=\overline{f(\bar{t})},\qquad U^{\dagger}=\{\bar{t}\colon t\in U\}, |  | (40) |

is also holomorphic. We will refer to f † f^{\dagger} as the *reflection*of f f in the real axis ℝ {\mathbb{R}}.

If U = U † U=U^{\dagger} is itself a domain symmetric with respect to ℝ {\mathbb{R}}, then a ℂ {\mathbb{C}} -linear subspace ℒ ⊂ 𝒪 ⁡ ( U) \mathscr{L}\subset\mathscr{O}(U) will be called *real*(on ℝ {\mathbb{R}}), if its reflection ℒ † = { f †: f ∈ ℒ } \mathscr{L}^{\dagger}=\{f^{\dagger}\colon f\in\mathscr{L}\} coincides with ℒ \mathscr{L}. A finite-dimensional real subspace admits a basis (over ℂ {\mathbb{C}}) of functions, real (i.e., taking real values) on U ∩ ℝ U\cap{\mathbb{R}}: it is sufficient to consider functions of the form 1 2 ​ ( f + f †) \frac{1}{2}(f+f^{\dagger}).

Any linear subspace ℒ ⊂ 𝒪 ⁡ ( U) \mathscr{L}\subset\mathscr{O}(U) can be *symmetrized*as follows,

 | ℒ ⊖ = ( ℒ + ℒ †) | U ∩ U †, \mathscr{L}^{\ominus}=(\mathscr{L}+\mathscr{L}^{\dagger})|_{U\cap U^{\dagger}}, |  | (41) |

(note that the functions from ℒ ⊖ \mathscr{L}^{\ominus} need to be restricted on the *symmetrization*U ⊖ = U ∩ U † U^{\ominus}=U\cap U^{\dagger}).

The role of the real axis can be played by any circle or real line γ ⊂ ℙ \gamma\subset{\mathbb{P}} equivalent to the “standard” real axis ℝ ⊂ ℙ {\mathbb{R}}\subset{\mathbb{P}} by a conformal automorphism φ ∈ Aut ⁡ ( ℙ 1) \varphi\in\operatorname{Aut}({\mathbb{P}}^{1}). The conformal equivalence will be denoted by the relation γ ≍ ℝ \gamma\asymp{\mathbb{R}}. If φ \varphi is an automorphism which transforms γ \gamma to the real axis ℝ {\mathbb{R}}, then the *reflection in γ \gamma*is defined by the formula

 | f † ​ ( φ ⁡ ( t)) = f ⁡ ( φ ⁡ ( t) ¯) ¯. f^{\dagger}(\varphi(t))=\overline{f(\overline{\varphi(t)})}. |  | (42) |

Modifying all constructions above accordingly, we arrive at the notion of a *symmetrization*of a linear subspace of functions ℒ \mathscr{L}. Such symmetrization will be denoted by ℒ γ ⊖ \mathscr{L}^{\ominus}_{\gamma}. An subspace ℒ \mathscr{L} such that ℒ γ ⊖ = ℒ \mathscr{L}^{\ominus}_{\gamma}=\mathscr{L} is called *real on γ \gamma*.

The dimension dim ℂ ℒ γ ⊖ \dim_{\mathbb{C}}\mathscr{L}^{\ominus}_{\gamma} of the symmetrization depends, in general, on the arc γ \gamma. For instance, if a space ℒ \mathscr{L} is a real on ℝ {\mathbb{R}}, then ℒ = ℒ ℝ ⊖ \mathscr{L}=\mathscr{L}^{\ominus}_{\mathbb{R}}, hence its symmetrization with respect to ℝ {\mathbb{R}} has the same dimension, yet for a generic line γ ε = e i ​ ε ​ ℝ \gamma_{\varepsilon}=e^{\mathrm{i}\varepsilon}{\mathbb{R}}, 0 < ε ≪ 1 0<\varepsilon\ll 1, arbitrarily close to ℝ {\mathbb{R}}, the dimension of the symmetrization ℒ γ ε ⊖ \mathscr{L}^{\ominus}_{\gamma_{\varepsilon}} will be twice the dimension of ℒ \mathscr{L}.

###### Definition 28

The *invariant slope*of a finite-dimensional monodromic subspace ℒ ⊂ 𝒪 ⁡ ( U) \mathscr{L}\subset\mathscr{O}(U), U ⊂ ℙ ​ – ​ Σ U\subset{\mathbb{P}}{\,\text{--}\,}\varSigma a simply connected polygon, is the supremum of slopes of all symmetrized conformal images of L L:

 | ∢ ​ ℒ = sup φ, γ ∠ ​ ( φ ∗ ​ ℒ) γ ⊖, φ ∈ Aut ⁡ ( ℙ 1), γ ≍ ℝ. \sphericalangle\mathscr{L}=\sup_{\varphi,\gamma}\angle(\varphi^{*}\mathscr{L})^{\ominus}_{\gamma},\qquad\varphi\in\operatorname{Aut}({\mathbb{P}}^{1}),\ \gamma\asymp{\mathbb{R}}. |  | (43) |

Here the supremum is taken over all conformal automorphisms f f and all circular arcs/lines γ ⊂ ℙ \gamma\subset{\mathbb{P}}, conformally equivalent to ℝ {\mathbb{R}}.

By the natural duality between finite-dimensional monodromic subspaces of holomorphic functions and linear ordinary differential operators with rational coefficients (modulo a common factor), described in Remark 26, the conformal isomorphisms and symmetrization can be defined also on differential operators with rational coefficients on ℙ 1 {\mathbb{P}}^{1}. More precisely, for a given operator D D of order ℓ \ell with a singular locus Σ \varSigma, we denote by φ ∗ ​ D \varphi^{*}D the operator of order ℓ \ell (unique modulo multiplication by a rational function) whose null space is φ ∗ ​ ℒ \varphi^{*}\mathscr{L}, where ℒ = { D y = 0 } ⊂ 𝒪 ( U) \mathscr{L}=\{Dy=0\}\subset\mathscr{O}(U) is the null space of D D in any simply connected domain U ⊂ ℙ ​ – ​ Σ U\subset{\mathbb{P}}{\,\text{--}\,}\varSigma. In the same way we denote by D γ ⊖ D^{\ominus}_{\gamma} the *symmetrization*of D D with respect to an arc γ ≍ ℝ \gamma\asymp{\mathbb{R}}, the operator of order ⩽ 2 ​ ℓ \leqslant 2\ell with the null space ℒ γ ⊖ \mathscr{L}^{\ominus}_{\gamma}. As was already noted, the specific choice of the domain U U is not important by Remark 27. An operator equal to its symmetrization, D = D γ ⊖ D=D^{\ominus}_{\gamma}, will be called *real on γ \gamma*, though this does not mean in general that the coefficients of this operator (in the monic representation) indeed take real values on the “axis of symmetry” γ \gamma.

###### Definition 29

The *invariant slope*∢ ​ D \sphericalangle D of a linear ordinary differential operator D D with rational coefficients on ℙ 1 {\mathbb{P}}^{1} is the supremum

 | ∢ ​ D = sup φ, γ ∠ ​ ( φ ∗ ​ D) γ ⊖, φ ∈ Aut ⁡ ( ℙ 1), γ ≍ ℝ. \sphericalangle D=\sup_{\varphi,\gamma}\angle(\varphi^{*}D)^{\ominus}_{\gamma},\qquad\varphi\in\operatorname{Aut}({\mathbb{P}}^{1}),\ \gamma\asymp{\mathbb{R}}. |  | (44) |

###### Remark 30

The group Aut ⁡ ( ℙ 1) ≅ PGL ⁡ ( 2, ℂ) \operatorname{Aut}({\mathbb{P}}^{1})\cong\operatorname{PGL}(2,{\mathbb{C}}) of conformal automorphisms of the projective line is noncompact, therefore the slope ∠ ​ φ ∗ ​ D \angle\varphi^{*}D may be unbounded as φ \varphi varies over this group. Similarly, the procedure of symmetrization may affect the slope in an uncontrollable way.

###### Example 31

Let φ μ: t ↦ μ ​ t \varphi_{\mu}\colon t\mapsto\mu t be the linear rescaling map and D ∈ ℂ [∂] D\in{\mathbb{C}}[\partial] a linear operator with *constant*coefficients. Then the slope ∠ ​ φ μ ∗ ​ D \angle\varphi_{\mu}^{*}D is unbounded as μ \mu varies over all nonzero complex (and even real) numbers.

However, for *Fuchsian*operators the supremum in ( 44) is always finite.

###### Proposition 32

The invariant slope of any Fuchsian operator is finite.

We will give an indirect proof of this statement later, in Remark 39.

The invariant slope of an operator is a semialgebraic function of its coefficients, yet it is very difficult to control: its value requires division by quantities which can be arbitrarily small. Our first main result circumvents this difficulty and shows that the straightforward reduction of a parametric linear system ( 29) to a parametric high order equation ( 30) results in an explicitly bounded slope.

###### Principal Lemma 33

A. Let Ω \Omega be a rational ( ℓ × ℓ) (\ell\times\ell) -matrix Pfaffian system of degree d d on ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1} with the following properties ( cf. with the assumptions of Theorems 7, 8),

1. (I)

Ω \Omega is integrable;

2. (R)

Ω \Omega is regular.

Then for any simply connected polygon U ⊂ ℙ ​ – ​ Σ λ U\subset{\mathbb{P}}{\,\text{--}\,}\varSigma_{\lambda} the linear spaces ℒ λ ⊂ 𝒪 ⁡ ( U) \mathscr{L}_{\lambda}\subset\mathscr{O}(U) generated by all components x p ​ q ​ ( λ, t) x_{pq}(\lambda,t) of any fundamental matrix solution X X of the system ( 12) in this domain, are defined by a family of linear ordinary differential equations of the form D λ ​ y = 0 D_{\lambda}y=0, where D = { D λ } D=\{D_{\lambda}\} are Fuchsian operators as in ( 30).

The family D D does not depend on U U and satisfies the following constraints:

- (i)

the order k = ord ⁡ D k=\operatorname{ord}D is no greater than ℓ 2 \ell^{2},

- (ii)

the degree max j ⁡ deg ⁡ R j \max_{j}\deg R_{j} is bounded by an explicit polynomial in ℓ \ell and d = deg ⁡ Ω d=\deg\Omega,

- (iii)

the invariant slope ∢ ​ D λ \sphericalangle D_{\lambda} of the operators is uniformly bounded over all values of the parameter λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m} outside a proper algebraic subset 𝒮 ⫋ ℙ m {\mathscr{S}}\subsetneqq{\mathbb{P}}^{m}.

B. Under the additional assumption

1. (Q)

Ω \Omega is defined over ℚ {\mathbb{Q}} and its size ( complexity) is s = 𝐒 ⁡ ( Ω) s=\mathbf{S}\left(\Omega\right),

the bound for the invariant slope is explicit and double exponential,

 | ∀ λ ∈ ℙ m ​ – ​ 𝒮 ∢ ​ D λ ⩽ s ( d ​ ℓ) O ⁡ ( m). \forall\lambda\in{\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}}\qquad\sphericalangle D_{\lambda}\leqslant s^{(d\ell)^{O(m)}}. |  | (45) |

Note that in the proof of this result we did not use the quasiunipotence assumption.

###### Definition 34

The family of equations { D λ y = 0 } \{D_{\lambda}y=0\} constructed in Principal Lemma 33, will be referred to as the *derived equation(s)*.

### 3.3 Formal derivation

In this section we recall a (fairly standard) reduction of the parametric system ( 29) to a parametric family of linear ordinary differential equations, paying attention to the complexity of the algorithm.

###### Lemma 35

Under the assumptions (I), (R) of the Principal Lemma 33 all components y = x p ​ q ​ ( λ, t) y=x_{pq}(\lambda,t) of any fundamental matrix solution X X of the system ( 12) on 𝕄 = ℙ m × ℙ 1 \mathbb{M}={\mathbb{P}}^{m}\times{\mathbb{P}}^{1} satisfy a parametric linear ordinary differential equation of the form D λ ​ y = 0 D_{\lambda}y=0 as in ( 30).

The family D = { D λ } λ ∈ ℙ m D=\{D_{\lambda}\}_{\lambda\in{\mathbb{P}}^{m}} satisfies the following constraints:

1. (1)

the order k = ord ⁡ D k=\operatorname{ord}D is no greater than ℓ 2 \ell^{2},

2. (2)

the degrees deg ⁡ R j \deg R_{j} do not exceed O ⁡ ( ℓ 4 ​ d) O(\ell^{4}d).

Under the additional assumption (Q) of the Principal Lemma 33,

1. (3)

the family D D is defined over ℚ {\mathbb{Q}} and its size is bounded by a simple exponential,

 | 𝐒 ⁡ ( D) ⩽ s O ⁡ ( ℓ 4 ​ d), s = 𝐒 ⁡ ( Ω). \mathbf{S}\left(D\right)\leqslant s^{O(\ell^{4}d)},\qquad s=\mathbf{S}\left(\Omega\right). |  |

###### Proof

This claim coincides (modulo notation) with Lemma 5 from BY 10, where one can find the accurate (albeit transparent) estimates. To make the exposition self-contained, we recall the main ideas of the proof.

The system ( 12) is defined on the product space ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1}. Choosing an affine chart t t on the second factor, we can consider it as a parametric family of linear differential equations of the following form (cf. with ( 29)),

 | ∂ X ∂ t = A ⁡ ( λ, t) ​ X. \frac{\partial X}{\partial t}=A(\lambda,t)\,X. |  | (46) |

By induction, one can instantly see that the higher order derivatives ∂ j ∂ t j ​ X \frac{\partial^{j}}{\partial t^{j}}X of the matrix X X which satisfies the linear system ( 46), satisfy the identities

 | ∂ j X ∂ t j = A j ( λ, t) ⋅ X, A j + 1 = ∂ A j ∂ t + A j ⋅ A, j = 0, 1, 2, …, \frac{\partial^{j}X}{\partial t^{j}}=A_{j}(\lambda,t)\cdot X,\hskip 18.49988ptA_{j+1}=\frac{\partial A_{j}}{\partial t}+A_{j}\cdot A,\hskip 18.49988ptj=0,1,2,\dots, |  | (47) |

where A 0 = E A_{0}=E is the identity matrix. Since A A is defined over ℚ {\mathbb{Q}}, all matrix functions in this sequence are also defined over ℚ {\mathbb{Q}}.

Derivation and matrix multiplication result in a controlled growth of the degrees and sizes of the rational matrix functions A 1, A 2, … A_{1},A_{2},\dots: the degree grows no faster than linearly in j j, deg ⁡ A j ⩽ j ​ d \deg A_{j}\leqslant jd, while the sizes 𝐒 ⁡ ( A j) \mathbf{S}\left(A_{j}\right) grow no faster than exponentially.

The rational matrix ( ℓ × ℓ) (\ell\times\ell) -functions over ℚ {\mathbb{Q}} form a linear space of dimension ℓ 2 \ell^{2} over the field ℚ ⁡ ( λ, t) {\mathbb{Q}}(\lambda,t) of rational functions on ℙ m × ℙ {\mathbb{P}}^{m}\times{\mathbb{P}}. Thus after k ⩽ ℓ 2 k\leqslant\ell^{2} steps the matrices A j A_{j} will exhibit a linear dependence over this field of the form

 | A k + R 1 ​ A k − 1 + ⋯ + R k ​ A 0 = 0, R j ∈ ℚ ⁡ ( λ, t). A_{k}+R_{1}A_{k-1}+\cdots+R_{k}A_{0}=0,\hskip 18.49988ptR_{j}\in{\mathbb{Q}}(\lambda,t). |  | (48) |

The identity ( 48) can be considered as a system of ℓ 2 \ell^{2} linear algebraic equations over the field ℚ ⁡ ( λ, t) {\mathbb{Q}}(\lambda,t). Solutions of this system (after elimination of all linear dependencies between equations) can be effectively computed using the Cramer rule as ratios of suitable determinants formed by entries of the matrices A 1, …, A k A_{1},\dots,A_{k}. This allows to place an upper bound for the sizes 𝐒 ⁡ ( R j) \mathbf{S}\left(R_{j}\right) in terms of s s and the parameters d, ℓ d,\ell.

The differential operator D = ∂ k + ∑ 1 k R k − j ∂ j D=\partial^{k}+\sum_{1}^{k}R_{k-j}\partial^{j}, ∂ = ∂ ∂ t \partial=\frac{\partial}{\partial t} by construction vanishes on X X: D ​ X ≡ 0 DX\equiv 0. Read componentwise, this matrix identity proves the Lemma.

### 3.4 Existential bounds for the slope of the derived family

The family of differential operators D = { D λ } D=\{D_{\lambda}\} which is constructed in Lemma 35, can be always reduced to a form with polynomial coefficients, which will be referred to as the *standard form*,

 | D = p 0 ( λ, t) ∂ k + ⋯ + p k − 1 ( λ, t) ∂ + p k ( λ, t), p j ∈ ℤ [λ, t], gcd ℤ ⁡ [λ, t] ( p 0, …, p k) = 1, \begin{gathered}D=p_{0}(\lambda,t)\,\partial^{k}+\cdots+p_{k-1}(\lambda,t)\,\partial+p_{k}(\lambda,t),\\ p_{j}\in{\mathbb{Z}}[\lambda,t],\qquad\gcd\nolimits_{{\mathbb{Z}}[\lambda,t]}(p_{0},\dots,p_{k})=1,\end{gathered} |  | (49) |

The operator D λ D_{\lambda} has order k k for almost all values of λ ∈ ℙ \lambda\in{\mathbb{P}}. Moreover, by the Bertini–Sard theorem, the subset of the parameter values λ \lambda,

 | 𝒮 = { λ: p 0 ​ ( λ, ⋅) = 0 } ∪ { λ: deg ⁡ gcd ℂ ⁡ [t] ​ ( p 0 ​ ( λ, ⋅), …, p k ​ ( λ, ⋅)) > 0 }. {\mathscr{S}}=\{\lambda\colon p_{0}(\lambda,{\,\boldsymbol{\cdot}}\,)=0\}\\ \cup\{\lambda\colon\deg\gcd\nolimits_{{\mathbb{C}}[t]}\bigl(p_{0}(\lambda,{\,\boldsymbol{\cdot}}\,),\dots,p_{k}(\lambda,{\,\boldsymbol{\cdot}}\,)\bigr)>0\}. |  | (50) |

is a proper algebraic subvariety, 𝒮 ⫋ ℙ m {\mathscr{S}}\subsetneqq{\mathbb{P}}^{m}, which is nowhere dense in ℙ m {\mathbb{P}}^{m}.

For all λ ∉ 𝒮 \lambda\notin{\mathscr{S}}, denote by σ ⁡ ( λ) = ∠ ​ D λ \sigma(\lambda)=\angle D_{\lambda} the *affine*slope of the operator D λ D_{\lambda}. By construction, it is a *semialgebraic function*on the parameter space.

###### Lemma 36

If the initial integrable system ( 46) is regular, the affine slope of the derived family D λ D_{\lambda} is globally bounded,

 | sup ℙ m ​ – ​ 𝒮 ∠ ​ D λ < + ∞. \sup_{{\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}}}\angle D_{\lambda}<+\infty. |  |

###### Proof

We will prove that the function σ: ℙ m ​ – ​ 𝒮 → ℝ + \sigma\colon{\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}}\to{\mathbb{R}}_{+} is *locally bounded*near each point a ∈ ℙ m a\in{\mathbb{P}}^{m}, i.e., that there exists such neighborhood U U of a a, such that sup λ ∈ U ​ – ​ 𝒮 σ ⁡ ( λ) < + ∞ \sup_{\lambda\in U{\,\text{--}\,}{\mathscr{S}}}\sigma(\lambda)<+\infty. By compactness of ℙ m {\mathbb{P}}^{m}, this would imply that σ \sigma is globally bounded. Clearly, it is sufficient to consider only the points a ∈ 𝒮 a\in{\mathscr{S}}, i.e., the values of the parameters λ \lambda for which the leading coefficient of the operator D λ D_{\lambda} vanishes identically: at all other points σ \sigma is continuous.

Moreover, we can assume without loss of generality that the parameter λ \lambda varies along a real analytic curve,

 | λ = γ ⁡ ( s), s ∈ ( ℝ 1, 0); γ ⁡ ( s) ∉ 𝒮 ⇔ s ≠ 0. \lambda=\gamma(s),\quad s\in({\mathbb{R}}^{1},0);\qquad\gamma(s)\notin{\mathscr{S}}\iff s\neq 0. |  |

Indeed, if the function σ \sigma were not locally bounded, then the point ( a, 0) ∈ U × ℝ + 1 (a,0)\in U\times{\mathbb{R}}^{1}_{+} would be the limit point for the open semialgebraic set S = { ( λ, z): λ ∉ 𝒮, σ ( λ) > 1 / z } S=\{(\lambda,z):\allowbreak\lambda\notin{\mathscr{S}},\sigma(\lambda)>1/z\}. By the curve selection lemma Mil 68, the point ( a, 0) (a,0) can be reached from inside S S by a real analytic curve s ↦ ( γ ⁡ ( s), z ⁡ ( s)) s\mapsto(\gamma(s),z(s)), which means that the function σ ⁡ ( λ ⁡ ( s)) \sigma(\lambda(s)) grows to infinity as s → 0 s\to 0.

Thus we need to consider only the particular case of a differential operator D ∈ 𝒪 ( ℝ 1, 0) [t, ∂] D\in\mathscr{O}({\mathbb{R}}^{1},0)[t,\partial] depending on a single parameter,

 | D = p 0 ( s, t) ∂ k + ⋯ + p k ( s, t), s ∈ ( ℝ 1, 0), t ∈ ℂ, ∂ = ∂ ∂ t, D=p_{0}(s,t)\,\partial^{k}+\cdots+p_{k}(s,t),\qquad s\in({\mathbb{R}}^{1},0),\ t\in{\mathbb{C}},\ \partial=\tfrac{\partial}{\partial t}, |  | (51) |

with coefficients p j p_{j} polynomial in t t, real analytic in s ∈ ( ℝ 1, 0) s\in({\mathbb{R}}^{1},0) and having no common factor for all s ≠ 0 s\neq 0. Because of the real analyticity, we can complexify ( 51) to become a family of differential operators D s = D | s = const D_{s}=D|_{s=\operatorname{const}} defined for all sufficiently small complex s ∈ ( ℂ 1, 0) s\in({\mathbb{C}}^{1},0).

The singular locus of this family is the analytic curve { ( s, t) ∈ ( ℂ, 0) × ℂ: p 0 ​ ( s, t) = 0 } \{(s,t)\in({\mathbb{C}},0)\times{\mathbb{C}}\colon p_{0}(s,t)=0\}. Apart from the axis { s = 0 } \{s=0\} corresponding to the identically vanishing leading coefficient, each axis { s } × ℂ \{s\}\times{\mathbb{C}} intersects this curve by finitely many points corresponding to singularities of the equation D λ s ​ y = 0 D_{\lambda_{s}}y=0. These points lie on branches of the above analytic curve, therefore one can always find a disk 𝔻 ⊂ ℂ \mathbb{D}\subset{\mathbb{C}} of radius 1 1, such that the product ( ℂ, 0) × 𝔻 ({\mathbb{C}},0)\times\mathbb{D} intersects the singular locus only by the disk { 0 } × 𝔻 \{0\}\times\mathbb{D}.

Consider a fundamental system of solutions x 1 ​ ( s, t), …, x k ​ ( s, t) x_{1}(s,t),\dots,x_{k}(s,t) of the equation D s ​ y = 0 D_{s}y=0 in the product ( ℂ 1, 0) × 𝔻 ({\mathbb{C}}^{1},0)\times\mathbb{D}, which consists of the linearly independent components of a matrix solution X ⁡ ( λ ⁡ ( s), t) X(\lambda(s),t) of the initial system ( 46). By the choice of 𝔻 \mathbb{D}, these functions are holomorphic outside { s = 0 } \{s=0\} and linearly independent, but may well be ramified with a nontrivial monodromy Δ \Delta corresponding to a loop around the axis { s = 0 } \{s=0\},

 | Δ ⁡ ( x 1, …, x k) = ( x 1, …, x k) ⋅ M, M ∈ GL ⁡ ( k, ℂ). \Delta(x_{1},\dots,x_{k})=(x_{1},\dots,x_{k})\cdot M,\qquad M\in\operatorname{GL}(k,{\mathbb{C}}). |  |

Fix a constant matrix A A such that exp ⁡ 2 ​ π ​ i ​ A = M \exp 2\pi\mathrm{i}A=M (such a matrix always exists, since M M is invertible). Then the tuple of functions

 | ( x 1 ′, …, x k ′) = ( x 1, …, x k) ⋅ s A (x_{1}^{\prime},\dots,x_{k}^{\prime})=(x_{1},\dots,x_{k})\cdot s^{A} |  |

is single-valued in ( ℂ 1, 0) × 𝔻 ({\mathbb{C}}^{1},0)\times\mathbb{D}. Because of the regularity of the initial system the new tuple of functions has at most poles of finite order on the axis { s = 0 } \{s=0\}. After replacing A A by A + q ​ E A+qE for sufficiently large q ∈ ℕ q\in{\mathbb{N}}, we construct a tuple of functions x j ′ ​ ( s, t) x_{j}^{\prime}(s,t), still forming a fundamental system of solutions for the family { D s } \{D_{s}\} in ( ℂ, 0) × 𝔻 ({\mathbb{C}},0)\times\mathbb{D} for all s ≠ 0 s\neq 0, such that x j ′ x^{\prime}_{j} are *holomorphic*on the axis { s = 0 } \{s=0\}. Note that the restrictions of these functions on the axis itself may well become degenerate (linearly dependent, e.g., identical zeros).

Consider the ℂ {\mathbb{C}} -linear subspaces ℒ s ⊆ ( 𝔻) \mathscr{L}_{s}\subseteq\mathscr{(}\mathbb{D}) spanned by the functions x 1 ′ ​ ( ⋅, s), …, x k ′ ​ ( ⋅, s) x_{1}^{\prime}({\,\boldsymbol{\cdot}}\,,s),\dots,x_{k}^{\prime}({\,\boldsymbol{\cdot}}\,,s). These subspaces depend holomorphically (in the natural sense) on s ∈ ( ℂ 1, 0) s\in({\mathbb{C}}^{1},0) as long as s ≠ 0 s\neq 0. The above mentioned degeneracy theoretically means that the analyticity breaks down at s = 0 s=0.

One of the keystone results, Lemma 7 from Yak 06 (cf. with Proposition 18.18 from IY 08), contends that this is not the case, and *the application s ↦ ℒ s s\mapsto\mathscr{L}_{s} is a holomorphic curve in the “Grassmanian” of k k -dimensional subspaces in the Banach space 𝒪 ⁡ ( 𝔻) \mathscr{O}(\mathbb{D}).*This result can be seen as a removable singularity-type theorem. One can avoid technical difficulties of dealing with infinite-dimensional Grassmanians by stating that *one can choose different bases in the subspaces ℒ s \mathscr{L}_{s} which would depend analytically on s s for all s ∈ ( ℂ 1, 0) s\in({\mathbb{C}}^{1},0) and remain linear independent as s = 0 s=0*.

###### Lemma 37 ( Lemma 7 from Yak 06)

For any collection of holomorphic functions x 1 ′, …, x k ′ ∈ 𝒪 ⁡ ( ( ℂ 1, 0) × 𝔻) x_{1}^{\prime},\dots,x_{k}^{\prime}\in\mathscr{O}\bigl(({\mathbb{C}}^{1},0)\times\mathbb{D}\bigr) such that x j ′ ​ ( s, ⋅) x_{j}^{\prime}(s,{\,\boldsymbol{\cdot}}\,) are linear independent in 𝒪 ⁡ ( 𝔻) \mathscr{O}(\mathbb{D}) for all s ≠ 0 s\neq 0, one can construct a meromorphic matrix function R ⁡ ( s) R(s), nondegenerate and holomorphic for s ≠ 0 s\neq 0, such that the tuple of functions f j = f j ​ ( s, t) f_{j}=f_{j}(s,t),

 | ( f 1, …, f k) = ( x 1 ′, …, x k ′) ⋅ R ⁡ ( s) (f_{1},\dots,f_{k})=(x_{1}^{\prime},\dots,x_{k}^{\prime})\cdot R(s) |  |

is holomorphic in ( s, t) (s,t) and linearly independent on each fiber { s = const } \{s=\operatorname{const}\}, *including the axis*{ s = 0 } \{s=0\}. ∎

By construction, D s ​ f j = 0 D_{s}f_{j}=0 for all s ∈ ( ℂ 1, 0) s\in({\mathbb{C}}^{1},0) and all j = 1, …, k j=1,\dots,k.

In a standard way, one can construct a family of *monic*differential operators L = { L s } L=\{L_{s}\} of order k k with coefficients holomorphic in ( ℂ 1, 0) × 𝔻 ({\mathbb{C}}^{1},0)\times\mathbb{D},

 | L = ∂ k + q 1 ( s, t) ∂ k − 1 + ⋯ + q k − 1 ( s, t) ∂ + q k ( s, t), q j ∈ 𝒪 ( ( ℂ 1, 0) × 𝔻), j = 1, …, k, \begin{gathered}L=\partial^{k}+q_{1}(s,t)\,\partial^{k-1}+\cdots+q_{k-1}(s,t)\,\partial+q_{k}(s,t),\\ q_{j}\in\mathscr{O}\bigl(({\mathbb{C}}^{1},0)\times\mathbb{D}\bigr),\qquad j=1,\dots,k,\end{gathered} |  |

which is also annulled by the same tuple: L s ​ f j = 0 L_{s}f_{j}=0 for all s ∈ ( ℂ 1, 0) s\in({\mathbb{C}}^{1},0) and all j = 1, …, k j=1,\dots,k. Since the orders of the two operators L s L_{s} and D s D_{s} are the same and the functions f j f_{j} are linearly independent on all fibers { s = const } \{s=\operatorname{const}\}, we conclude that the operators D s D_{s} and L s L_{s} must be proportional,

 | p j ​ ( s, ⋅) p 0 ​ ( s, ⋅) = q j ​ ( s, ⋅) 1, ∀ s ≠ 0, ∀ j = 1, …, k. \frac{p_{j}(s,{\,\boldsymbol{\cdot}}\,)}{p_{0}(s,{\,\boldsymbol{\cdot}}\,)}=\frac{q_{j}(s,{\,\boldsymbol{\cdot}}\,)}{1},\qquad\forall s\neq 0,\quad\forall j=1,\dots,k. |  | (52) |

Since q j q_{j} are holomorphic, this implies that the ratios in the left hand side of ( 52) are holomorphic *also*on the axis { s = 0 } \{s=0\}. We show that this implies the finiteness of the ratios of the norms in ℂ ⁡ [t] {\mathbb{C}}[t] as function of s → 0 s\to 0.

Let ν j ⩾ 0 \nu_{j}\geqslant 0 be the vanishing orders of the polynomial coefficients p j p_{j} on the axis { s = 0 } \{s=0\}: this means that p j = s ν j ​ p j ′ p_{j}=s^{\nu_{j}}p_{j}^{\prime}, while p j ′ ∈ 𝒪 ⁡ ( ℂ 1, 0) ​ [t] p_{j}^{\prime}\in\mathscr{O}({\mathbb{C}}^{1},0)[t] and p j ′ ​ ( 0, ⋅) ≠ 0 p_{j}^{\prime}(0,{\,\boldsymbol{\cdot}}\,)\neq 0. From ( 52) it follows that ν j ⩾ ν 0 \nu_{j}\geqslant\nu_{0} for all j = 1, …, k j=1,\dots,k. Besides, since the limit denominator p 0 ′ ​ ( 0, ⋅) p_{0}^{\prime}(0,{\,\boldsymbol{\cdot}}\,) is nonzero, its norm ‖ p 0 ′ ​ ( s, ⋅) ‖ ℂ ⁡ [t] \|p_{0}^{\prime}(s,{\,\boldsymbol{\cdot}}\,)\|_{{\mathbb{C}}[t]} is strictly positive. As a result, we conclude that the slope σ ⁡ ( s) = ∠ ​ D s \sigma(s)=\angle D_{s} is continuous at s = 0 s=0:

 | σ ⁡ ( s) = max j = 1, …, k ⁡ s ν j − ν 0 ⋅ ‖ p j ′ ​ ( s, ⋅) ‖ ℂ ⁡ [t] ‖ p 0 ′ ​ ( s, ⋅) ‖ ℂ ⁡ [t]. \sigma(s)=\max_{j=1,\dots,k}s^{\nu_{j}-\nu_{0}}\cdot\frac{\|p_{j}^{\prime}(s,{\,\boldsymbol{\cdot}}\,)\|_{{\mathbb{C}}[t]}}{\|p_{0}^{\prime}(s,{\,\boldsymbol{\cdot}}\,)\|_{{\mathbb{C}}[t]}}. |  |

This proves the local boundedness of the slope ∠ ​ D s \angle D_{s} along the real analytic curve γ \gamma, concluding the proof of the Lemma.

### 3.5 Embedding in a conformally complete symmetric family

The assertion of the Principal Lemma 33 concerns the *invariant*slope of the derived operator, whereas the finiteness achieved in Lemma 36 is established only for the *affine*slope. Besides, bounding the invariant slope involves symmetrization, whose explicit construction may lead to an uncontrollable growth of the slope, see ( BY 10, Example 6).

To fill the gap, we embed the initial parametric family of Pfaffian systems ( 29) into a larger family of systems of larger dimension, whose derived equation will contain all symmetrizations of all conformal transforms of the initial derived family. The uniform bound for the affine slope in this new family gives a bound for the invariant slope of the original one.

The embedding is rather straightforward in terms of the linear spaces. Denote by X ⁡ ( λ, t) X(\lambda,t) the matrix solution of the system ( 12) on ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1} and φ ∈ Aut ( ℙ 1) ≅ PGL ( 2, ℂ) ≅ ℙ 3 – { a quadric } \varphi\in\operatorname{Aut}({\mathbb{P}}^{1})\cong\operatorname{PGL}(2,{\mathbb{C}})\cong{\mathbb{P}}^{3}{\,\text{--}\,}\{\text{a quadric}\} a variable conformal isomorphism. Then the components of the matrix function 𝑿 ( λ, φ, ⋅) = X ( λ, φ ( ⋅)) \boldsymbol{X}(\lambda,\varphi,{\,\boldsymbol{\cdot}}\,)=X(\lambda,\varphi({\,\boldsymbol{\cdot}}\,)) span for each admissible value value ( λ, φ) ∈ ℙ m × ℙ 3 (\lambda,\varphi)\in{\mathbb{P}}^{m}\times{\mathbb{P}}^{3} of the parameters the linear space ℒ λ, φ = φ ∗ ​ ℒ λ \mathscr{L}_{\lambda,\varphi}=\varphi^{*}\mathscr{L}_{\lambda} which is a conformal transform ( 39) of the linear space ℒ λ \mathscr{L}_{\lambda} spanned by the components of the initial matrix function X ⁡ ( λ, ⋅) X(\lambda,{\,\boldsymbol{\cdot}}\,). In other words, considered as a parametric family with the parameter space ℙ m × ℙ 3 {\mathbb{P}}^{m}\times{\mathbb{P}}^{3}, the Pfaffian system with the matrix 1-form 𝛀 = d ​ 𝑿 ⋅ 𝑿 − 1 \boldsymbol{\Omega}=\,\mathrm{d}\boldsymbol{X}\cdot\boldsymbol{X}^{-1} contains all conformal transforms of the initial system.

The dimension and the degree of the system 𝛀 \boldsymbol{\Omega} obviously remain the same as that of the system Ω \Omega. It is almost as easy to see that the size (complexity) 𝐒 ⁡ ( 𝛀) \mathbf{S}\left(\boldsymbol{\Omega}\right) differs from 𝐒 ⁡ ( Ω) \mathbf{S}\left(\Omega\right) by involving into a constant power, s ↦ s O ⁡ ( 1) s\mapsto s^{O(1)}. Indeed, the derivatives of 𝑿 \boldsymbol{X} with respect to the variables φ ∈ ℙ 3 \varphi\in{\mathbb{P}}^{3} can be expressed over ℚ {\mathbb{Q}} through entries of Ω \Omega, t t and φ \varphi using the chain rule, and it remains to apply a few times the inequalities ( 16). Clearly, the new family is also regular, integrable and quasiunipotent.

It remains to embed the family of linear spaces ℒ λ, φ \mathscr{L}_{\lambda,\varphi} into a larger family (still defined over ℚ {\mathbb{Q}} albeit on a larger space) which would contain symmetrizations of all these spaces. Since the family ℒ λ, φ \mathscr{L}_{\lambda,\varphi} is already conformally complete (e.g., contains together with each space its conformal transforms), it is sufficient to symmetrize only with respect to a single axis, the real line ℝ {\mathbb{R}}.

The reflected matrix function 𝑿 † ​ ( μ, ψ, t) = 𝑿 ⁡ ( μ ¯, ψ ¯, t ¯) ¯ \boldsymbol{X}^{\dagger}(\mu,\psi,t)=\overline{\boldsymbol{X}(\bar{\mu},\bar{\psi},\bar{t})} is a holomorphic matrix function which satisfies the rational integrable Pfaffian system d ​ 𝑿 † = 𝛀 † ​ 𝑿 † \,\mathrm{d}\boldsymbol{X}^{\dagger}=\boldsymbol{\Omega}^{\dagger}\boldsymbol{X}^{\dagger} on ℙ m × ℙ 3 × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{3}\times{\mathbb{P}}^{1}. This reflection does not affect neither degree, nor the dimension or the size of the Pfaffian system (obviously keeping it defined over ℚ {\mathbb{Q}}). The block-diagonal matrix function

 | X ^ ​ ( λ, φ, μ, ψ, t) = diag ⁡ { 𝑿 ⁡ ( λ, φ, t), 𝑿 † ​ ( μ, ψ, t) } \widehat{X}(\lambda,\varphi,\mu,\psi,t)=\operatorname{diag}\{\boldsymbol{X}(\lambda,\varphi,t),\boldsymbol{X}^{\dagger}(\mu,\psi,t)\} |  |

satisfies the integrable Pfaffian system of dimension 2 ​ ℓ 2\ell on the product space birationally equivalent to ℙ 2 ​ m + 6 × ℙ 1 {\mathbb{P}}^{2m+6}\times{\mathbb{P}}^{1} with the coordinates ( λ, φ, μ, ψ, t) (\lambda,\varphi,\mu,\psi,t),

 | d ​ X ^ = Ω ^ ​ X ^, X ^ = ( 𝑿 𝑿 †), Ω ^ = ( 𝛀 𝛀 †). \mathrm{d}\widehat{X}=\widehat{\Omega}\widehat{X},\qquad\widehat{X}=\begin{pmatrix}\boldsymbol{X}&\\ &\boldsymbol{X}^{\dagger}\end{pmatrix},\quad\widehat{\Omega}=\begin{pmatrix}\boldsymbol{\Omega}&\\ &\boldsymbol{\Omega}^{\dagger}\end{pmatrix}. |  | (53) |

The corresponding family of subspaces ℒ ^ λ, φ, μ, ψ \widehat{\mathscr{L}}_{\lambda,\varphi,\mu,\psi} contains all sums ℒ λ, φ + ℒ μ, ψ † \mathscr{L}_{\lambda,\varphi}+\mathscr{L}_{\mu,\psi}^{\dagger}, in particular, all symmetrizations of the conformal transforms ( φ ∗ ​ ℒ λ) γ ⊖ (\varphi^{*}\mathscr{L}_{\lambda})^{\ominus}_{\gamma}.

By its explicit construction, the family ( 53) (considered as a Pfaffian system on ℙ 2 ​ m + 6 × ℙ 1 {\mathbb{P}}^{2m+6}\times{\mathbb{P}}^{1}) is integrable, rational and regular. Applied to a system defined over ℚ {\mathbb{Q}} on ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1}, the construction results in a system again defined over ℚ {\mathbb{Q}} on the larger subspace. The dimension is increased by the factor of 2 2 from ℓ \ell to 2 ​ ℓ 2\ell, and the size (complexity) is increased by an explicit constant factor O ⁡ ( 1) O(1). To check that the above doubling preserves quasiunipotence, note that a small loop (in the sense of Definition 8) in the product space ℙ 2 ​ m + 6 × ℙ 1 {\mathbb{P}}^{2m+6}\times{\mathbb{P}}^{1} projects as a small loop on each of the components ℙ m + 3 × ℙ 1 {\mathbb{P}}^{m+3}\times{\mathbb{P}}^{1}; the corresponding monodromy is block diagonal with quasiunipotent (or identical) blocks.

Thus for any Pfaffian system ( 12) with the matrix Ω = { Ω λ } \Omega=\{\Omega_{\lambda}\} one can effectively construct its embedding (as a family) into a larger family with the Pfaffian matrix form Ω ^ = { Ω ^ η } \widehat{\Omega}=\{\widehat{\Omega}_{\eta}\}, η ∈ ℙ 2 ​ m + 6 \eta\in{\mathbb{P}}^{2m+6} with the following characteristic property.

###### Lemma 38

For any parameter value λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m} there exists a parameter value η ∈ ℙ 2 ​ m + 6 \eta\in{\mathbb{P}}^{2m+6} such that the invariant slope of the derived operator D λ D_{\lambda} is equal to the affine slope of the corresponding derived operator D ^ η \widehat{D}_{\eta},

 | ∀ λ ∈ ℙ m ∃ η ∈ ℙ 2 ​ m + 6 ∢ ​ D λ = ∠ ​ D ^ η. \forall\lambda\in{\mathbb{P}}^{m}\quad\exists\eta\in{\mathbb{P}}^{2m+6}\qquad\sphericalangle D_{\lambda}=\angle\widehat{D}_{\eta}. |  |

Thus a uniform bound for the affine slope ∠ ​ D ^ η \angle\widehat{D}_{\eta} of the family of operators D ^ η \widehat{D}_{\eta} is at the same time the uniform upper bound for the invariant slope ∢ ​ D λ \sphericalangle D_{\lambda} of the operators D λ D_{\lambda} derived from the initial family.

### 3.6 Proof of the Principal Lemma 33

#### 3.6.1 Proving the qualitative part.

To prove the existential finiteness of the latter (Part A of the Principal Lemma 33), we need to consider together with the initial family { Ω λ } \{\Omega_{\lambda}\}, λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m}, and the corresponding family D λ D_{\lambda} of derived operators the conformal completion { Ω ^ η } \{\widehat{\Omega}_{\eta}\}, η ∈ ℙ 2 ​ m + 6 \eta\in{\mathbb{P}}^{2m+6}, and the respective family { D ^ η } \{\widehat{D}_{\eta}\} as described in § 3.5.

Lemma 36 applied to the family { D ^ η } \{\widehat{D}_{\eta}\}, guarantees that the affine slope of these operators is bounded uniformly over η ∈ ℙ 2 ​ m + 6 \eta\in{\mathbb{P}}^{2m+6}. By Lemma 38, this means that the invariant slope of the operators D λ D_{\lambda} is bounded by the same constant.

#### 3.6.2 From qualitative to quantitative bounds.

It remains to prove Part B of the Principal Lemma and show that if the regular family ( 12) is defined over ℚ {\mathbb{Q}}, then the bound for the invariant slope can be made explicit as follows,

 | ∀ λ ∈ ℙ m ​ – ​ 𝒮 ∢ ​ D λ ⩽ s ( d ​ ℓ) O ⁡ ( m), s = 𝐒 ⁡ ( D), d = deg ⁡ D. \forall\lambda\in{\mathbb{P}}_{m}{\,\text{--}\,}{\mathscr{S}}\qquad\sphericalangle D_{\lambda}\leqslant s^{(d\ell)^{O(m)}},\quad s=\mathbf{S}\left(D\right),\ d=\deg D. |  | (54) |

Indeed, in this case the derived equation D ^ η \widehat{D}_{\eta} is also defined over ℚ {\mathbb{Q}} and its size is explicitly bounded by the assertion (3) of Lemma 35 (replacing s s by its finite power s O ⁡ ( 1) s^{O(1)} and ℓ \ell by 2 ​ ℓ 2\ell because of the difference between the families D D and D ^ \widehat{D} does not affect the asymptotic). This means that the subgraph of the affine slope function σ ⁡ ( ⋅) \sigma({\,\boldsymbol{\cdot}}\,) is a semialgebraic set defined over ℚ {\mathbb{Q}}, exactly as in Example 19. Since the slope σ ⁡ ( η) = ∠ ​ D ^ η \sigma(\eta)=\angle\widehat{D}_{\eta} is bounded by Lemma 36 (cf. with § 3.6.1), Theorem 6 gives then the double exponential upper bound of the form s ( O ⁡ ( 1) ⋅ d ​ ℓ) O ⁡ ( 2 ​ m + 6) = s ( d ​ ℓ) O ⁡ ( m) s^{(O(1)\cdot d\ell)^{O(2m+6)}}=s^{(d\ell)^{O(m)}} for the slope σ ⁡ ( ⋅) \sigma({\,\boldsymbol{\cdot}}\,) on ℙ 2 ​ m + 6 {\mathbb{P}}^{2m+6}. By Lemma 38, this gives the explicit uniform bound for the invariant slope ∠ ​ D λ \angle D_{\lambda} and thus completes the proof of Principal Lemma 33.

###### Remark 39 (Proof of Proposition 32)

Let D D be an arbitrary Fuchsian operator. Its conformal transforms φ ∗ ​ D \varphi^{*}D, and their symmetrizations ( φ ∗ ​ D) γ ⊖ (\varphi^{*}D)^{\ominus}_{\gamma} with respect to all arcs γ = ψ ⁡ ( ℝ) ≍ ℝ \gamma=\psi({\mathbb{R}})\asymp{\mathbb{R}}, φ, ψ ∈ Aut ⁡ ( ℙ) ⊂ ℙ 3 \varphi,\psi\in\operatorname{Aut}({\mathbb{P}})\subset{\mathbb{P}}^{3}, constitute a parametric family D λ D_{\lambda}, λ ∈ ℙ 3 × ℙ 3 \lambda\in{\mathbb{P}}^{3}\times{\mathbb{P}}^{3}, which is a regular family of operators with compact base ≅ ℙ 6 \cong{\mathbb{P}}^{6} (not necessarily defined over ℚ {\mathbb{Q}}). Application of Lemma 36 to this family proves that the invariant slope ∢ ​ D \sphericalangle D is always finite; this gives a (very indirect) proof of Proposition 32.

It would be interesting to achieve a direct proof together with an explicit bound on the invariant slope, e.g., in terms of the order of the equation, the number of Fuchsian singularities and the absolute value of the respective characteristic exponents ( IY 08, Example 19.21).

## 4 Counting zeros of functions defined by Fuchsian equations

A linear ordinary differential equation of bounded affine slope admits an explicit upper bound for the variation of argument of its nontrivial solutions along paths of bounded length, sufficiently distant from the singular points of the equation. For Fuchsian equations, because of the finiteness of the invariant slope (Proposition 32), such paths can be drawn with very few restrictions. One can then try and slit the projective line ℙ 1 {\mathbb{P}}^{1} along suitably chosen paths into “polygonal” simply connected domains, to which the argument principle can be applied. A similar approach, also based on the idea of suitable clustering, was suggested in NY 03, yet its implementation there was conditioned on the spectral condition imposed on the monodromy group of the equation. Unfortunately, this condition is algebraically unverifiable (one cannot, in general, algebraically compute the monodromy of a regular system along an arbitrary closed loop). Moreover, this condition in the form required in NY 03 does not hold for the Picard–Fuchs system in general: there are some “large loops” whose monodromy does not possess the necessary spectral properties.

In this section we suggest a way to circumvent this obstacle for isomonodromic families, and establish explicit upper bounds for the number of zeros under a weaker condition: the monodromy is required to be quasiunipotent only around *small loops*(cf. Definition 8).

### 4.1 Normalized length

We start by introducing some metric characteristics of finite configurations of l l points on the plane ℂ {\mathbb{C}}, which are invariant under the action of the affine group.

Let T T be a fixed finite point subset in ℂ {\mathbb{C}}.

###### Definition 40

The *normalized length*of a closed circular arc γ ⊂ ℂ ​ – ​ T \gamma\subset{\mathbb{C}}{\,\text{--}\,}T relative to the finite point set T ⊂ ℂ T\subset{\mathbb{C}} is the finite positive number

 | | γ / T | = 1 2 ​ π ⋅ | γ | dist ⁡ ( γ, T) |\gamma/T|=\frac{1}{2\pi}\cdot\frac{|\gamma|}{\operatorname{dist}(\gamma,T)} |  | (55) |

where | ⋅ | |\cdot| denotes the usual Euclidean length in ℂ {\mathbb{C}} and dist ⁡ ( ⋅, ⋅) \operatorname{dist}(\cdot,\cdot) the Euclidean distance.

The *normalized length*of a line segment γ \gamma disjoint with T T is defined as the similar ratio

 | | γ / T | = | γ | dist ⁡ ( γ, T), |\gamma/T|=\frac{|\gamma|}{\operatorname{dist}(\gamma,T)}, |  |

differing only by the numeric factor 2 ​ π ≈ 6.283 ​ … 2\pi\approx 6.283\dots.

The normalized length clearly is an affine invariant: for any affine automorphism φ ∈ Aut ⁡ ( ℂ) \varphi\in\operatorname{Aut}({\mathbb{C}}), we have | γ / T | = | φ ⁡ ( γ) / φ ⁡ ( T) | |\gamma/T|=|\varphi(\gamma)/\varphi(T)|.

###### Example 41

The normalized length of all sufficiently small circles { | t − a | = ε } \{|t-a|=\varepsilon\}, a ∈ T a\in T, 0 < ε ≪ 1 0<\varepsilon\ll 1, is 1 1.

The normalized length is a crude substitute for the length of a segment in the hyperbolic (Poincaré) metric on the unit disk considered as the universal covering space for the multiply connected domain ℂ ​ – ​ T {\mathbb{C}}{\,\text{--}\,}T. However, this substitute will be more convenient for our purposes than the genuine hyperbolic length, among other things because of the semialgebraicity of the former.

### 4.2 Affine invariant bounds for zeros of solutions of differential equations

The notion of normalized length allows to place bounds on the variation of argument and the number of isolated zeros for solutions of homogeneous ordinary differential equations in *affine invariant terms*.

The following statement gives an affine invariant generalization of Lemma 25 in terms of the normalized length.

###### Lemma 42

Let D D be a Fuchsian differential operator of order k k with coefficients of degree ⩽ d \leqslant d and the singular locus Σ \varSigma, and γ \gamma a closed circular arc or line segment disjoint with Σ \varSigma.

Then the variation of argument of any nonzero solution of the homogeneous equation D ​ y = 0 Dy=0 along the arc γ \gamma is explicitly bounded,

 | Var ⁡ Arg ⁡ y ⁡ ( t) | γ ⩽ k ​ L O ⁡ ( d) ⋅ ∢ ​ D, \operatorname{Var}\operatorname{Arg}y(t)|_{\gamma}\leqslant kL^{O(d)}\cdot\sphericalangle D, |  | (56) |

where L = | γ / Σ | L=|\gamma/\varSigma| is the normalized length of the arc (see ( 55)), and ∢ ​ D \sphericalangle D the invariant slope of the operator D D.

###### Proof

One can always apply an affine transformation of the affine plane so that the distance between γ \gamma and the singular locus of the operator will be exactly 1 1 and the curve itself passes through the origin. Then the Euclidean length of the curve will not exceed L L by the definition of the normalized length, and it will belong to the circle of radius L L by the triangle inequality. The affine slope S S of the operator D D in the new chart still is no greater than ∢ ​ D \sphericalangle D by definition of the invariant slope. Applying ( 35) with S = ∢ ​ D S=\sphericalangle D, R = | γ | = L R=|\gamma|=L and r = 1 r=1, we obtain the inequality ( 56).

In the same way as in the proof of Lemma 42, we may generalize the “Petrov trick” to count zeros of solutions of differential operators in annuli with quasiunipotent monodromy in affine invariant terms. The starting point is the following Lemma which is borrowed from BY 10.

###### Lemma 43 ( Lemma 10 from BY 10)

If the monodromy of a *real*differential operator D D along the equator of a symmetric annulus K = { ρ − < | t | < ρ + } K=\{\rho_{-}<|t|<\rho_{+}\} has all eigenvalues on the unit circle, then the number of zeros of any solution in K K is explicitly bounded,

 | 𝒩 ⁡ ( D, K) ⩽ ( 2 ​ k + 1) ​ ( 2 ​ B + 1), {\mathcal{N}}(D,K)\leqslant(2k+1)(2B+1), |  | (57) |

where k k is the order of the operator and B = B ⁡ ( D, K) B=B(D,K) the upper bound for the variation of arguments of any solution of D ​ y = 0 Dy=0 along the boundary circles C ± = { | t | = ρ ± } C_{\pm}=\{|t|=\rho_{\pm}\}.

Together with Lemma 42 above, this estimate proves the following explicit bound for the number of zeros of solutions in annuli.

###### Lemma 44

Let D D be a Fuchsian operator of order k k, degree ⩽ d \leqslant d and the singular locus Σ \varSigma, and K ⊆ ℂ ​ – ​ Σ K\subseteq{\mathbb{C}}{\,\text{--}\,}\varSigma a topological annulus bounded by two disjoint circles C ± C_{\pm} (one of which may degenerate to a point).

If the monodromy of D D along the equator of K K is quasiunipotent, then the number of isolated zeros of any solution of D ​ y = 0 Dy=0 in K K is explicitly bounded:

 | 𝒩 ⁡ ( D, K) ⩽ k 2 ​ L O ⁡ ( d) ⋅ ∢ ​ D, {\mathcal{N}}(D,K)\leqslant k^{2}L^{O(d)}\cdot\sphericalangle D, |  | (58) |

where L L is the normalized length of the boundary, L = | C − / Σ | + | C + / Σ | L=|C_{-}/\varSigma|+|C_{+}/\varSigma|.

###### Proof

We can always make a conformal automorphism which transforms the annulus K K into the annulus bounded by two circles centered at the origin. Without loss of generality, replacing if necessary D D by its symmetrization around the real axis ℝ {\mathbb{R}}, we may assume that D D is real. The variation of argument of any solution of the equation D ​ y = 0 Dy=0 along the boundary circles is bounded by k ​ | C ± / Σ | O ⁡ ( d) ​ ∢ ​ D ⩽ k ​ L O ⁡ ( d) ​ ∢ ​ D k|C_{\pm}/\varSigma|^{O(d)}\sphericalangle D\leqslant kL^{O(d)}\sphericalangle D by Lemma 42. The inequality ( 57) then implies the bound ( 58).

### 4.3 Admissible systems of slits

In this section we describe systems of arcs such that slitting the plane along these arcs subdivides it into components allowing for application of the counting tools (Lemmas 42 and 44 from § 4.2).

###### Definition 45

The normalized length of a *union*of circular arcs and line segments S = γ 1 ⊔ ⋯ ⊔ γ k S=\gamma_{1}\sqcup\cdots\sqcup\gamma_{k}, S ⊂ ℂ ​ – ​ T S\subset{\mathbb{C}}{\,\text{--}\,}T, is by definition the sum of the normalized length of all components,

 | | S / T | = | γ 1 / T | + ⋯ + | γ k / T |. |S/T|=|\gamma_{1}/T|+\cdots+|\gamma_{k}/T|. |  |

###### Remark 46

Note that for each term γ i \gamma_{i} above, the normalized length involves the distance from the set T T to γ i \gamma_{i} and not to their union S S. Thus the normalized length *depends*on the way the set S S is represented as a finite union of arcs and segments. In our constructions, however, this representation will always be clear from the context.

###### Example 47

Let T T be any two-point set and S S the union of two equal circles γ 1, 2 \gamma_{1,2} centered at these points and the shortest line segment γ 0 \gamma_{0} connecting these circles.

If the radii of these circles are equal to 1 / 3 1/3 of the distance between the points of T T, then the normalized length | S / T | |S/T| is equal to 3 3. This length can be further reduced to almost 2 2 if the radii tend to half the distance between the points. On the contrary, the normalized length S / T S/T tends to infinity if the radii of the circles tend to 0 0: in this case | γ 0 / T | |\gamma_{0}/T| tends to infinity.

Let, as before, T ⊂ ℂ T\subset{\mathbb{C}} be a finite point set, and S = S a, r ⊂ ℂ S=S_{a,r}\subset{\mathbb{C}} a finite union of circles of the form S a, r = ⋃ i { | t − a i | = r i } S_{a,r}=\bigcup_{i}\{|t-a_{i}|=r_{i}\}, a i ∈ ℂ a_{i}\in{\mathbb{C}}, r i > 0 r_{i}>0, i = 1, …, k i=1,\dots,k.

###### Definition 48

The union of circles S S is called a *clustering*of the finite point set T T, if all these circles are disjoint with T T and pairwise disjoint with each other.

A clustering subdivides points from T T into *nested subsets*, some (or most) of which in principle may be empty or singletons.

Let S = ⨆ i S i ⊂ ℂ ​ – ​ T S=\bigsqcup_{i}S_{i}\subset{\mathbb{C}}{\,\text{--}\,}T be a clustering of T T.

###### Definition 49

A finite union S ′ = S ⊔ γ 1 ⊔ ⋯ ⊔ γ k S^{\prime}=S\sqcup\gamma_{1}\sqcup\cdots\sqcup\gamma_{k} of circles s i s_{i} and line segments γ i \gamma_{i} connecting them so that the circles and segments have only endpoints in common, is called *admissible system of slits*for a finite point set T T, if the complement ℂ ​ – ​ { S ′ ∪ T } {\mathbb{C}}{\,\text{--}\,}\{S^{\prime}\cup T\} consists only of simply connected domains (of arbitrary shape) and topological annuli bounded by two circles (which may degenerate to a circular disk punctured at a point from T T).

[image: Refer to caption]

Figure 1: Admissible system of slits around a finite point set.

Clearly, any clustering can be completed to an admissible system of slits by infinitely many ways. The number of possibilities can be reduced to finite, if each segment γ i \gamma_{i} realizes the shortest path connecting the two respective circles (provided the latter are not concentric).

###### Definition 50 (principal)

The *cluster diameter*of a finite point set T ⊂ ℂ T\subset{\mathbb{C}} is the infimum of normalized lengths of an admissible system of slits S ′ S^{\prime} as in Definition 49, involving no more than a given number c c of circular arcs:

 | cdiam ⁡ ( T ∣ c) = inf S ′ { | S ′ / T |: S ′ = ⨆ i = 1 c S i ​ ⨆ j γ j ​ admissible for ​ T }. \operatorname{cdiam}(T\mid c)=\inf_{S^{\prime}}\biggl\{\,|S^{\prime}/T|\colon S^{\prime}=\bigsqcup_{i=1}^{c}S_{i}\bigsqcup_{j}\gamma_{j}\text{ admissible for }T\biggr\}. |  |

By this definition, cdiam ⁡ ( T ∣ c) \operatorname{cdiam}(T\mid c) may well be infinite, if the number of circular slits is too small compared to the number of points. On the other hand, it is obviously finite if c c is sufficiently large (see the proof of Lemma 53).

### 4.4 Admissible system of slits for differential equations

Let L = p 0 ( t) ∂ k + ⋯ + p k − 1 ( t) ∂ + p k ( t) ∈ ℂ [∂, t] L=p_{0}(t)\partial^{k}+\cdots+p_{k-1}(t)\partial+p_{k}(t)\in{\mathbb{C}}[\partial,t] be a differential operator with polynomial coefficients p i ∈ ℂ ⁡ [t] p_{i}\in{\mathbb{C}}[t]. Its singular locus Σ L = { p 0 = 0 } \varSigma_{L}=\{p_{0}=0\} is a finite point set which will be denoted by T T.

If S ′ S^{\prime} is an admissible system of slits for the point set T = Σ L T=\varSigma_{L} in the sense of Definition 49, then for any topological annulus A ⊂ ℂ ​ – ​ S ′ A\subset{\mathbb{C}}{\,\text{--}\,}S^{\prime} the monodromy operator M = M A M=M_{A} associated with the equatorial loop (the positively oriented loop in A A which generates π 1 ​ ( A) \pi_{1}(A)) is defined uniquely modulo conjugacy M ↦ C − 1 ​ M ​ C M\mapsto C^{-1}MC, det C ≠ 0 \det C\neq 0.

###### Definition 51

A system of slits S ′ S^{\prime} is *admissible for the operator*L L, if it is admissible for the *singular locus*T = Σ L T=\varSigma_{L} and in addition the monodromy of L L along the equatorial loop of each annulus A A appearing in ℂ ​ – ​ S ′ {\mathbb{C}}{\,\text{--}\,}S^{\prime} is quasiunipotent (cf. with the assumptions of Lemma 44).

The admissible system of slits for a linear system of Pfaffian equations d ​ x = Ω λ ​ x \,\mathrm{d}x=\Omega_{\lambda}x on a projective line, is defined analogously. Obviously, the additional constraint imposed by the requirement on the monodromy map is determined by the solutions, so that a system of slits is admissible at the same time both for a regular integrable rational system Ω λ \Omega_{\lambda} on ℙ 1 {\mathbb{P}}^{1} as in ( 29) and for the corresponding derived operator D λ D_{\lambda} as in ( 49).

As before, we define the *cluster diameter of the singular locus*of the operator L L as the infimum over all admissible systems of slits involving no more than c c circles,

 | cdiam ( L ∣ c) = inf S ′ { | S ′ / Σ L |: S ′ = ⨆ i = 1 c S i ⨆ j γ j admissible for L }. \operatorname{cdiam}(L\mid c)=\inf_{S^{\prime}}\biggl\{\,|S^{\prime}/\varSigma_{L}|\colon S^{\prime}=\bigsqcup_{i=1}^{c}S_{i}\bigsqcup_{j}\gamma_{j}\text{ admissible for }L\biggr\}. |  |

By construction, cdiam ⁡ ( L ∣ c) ⩾ cdiam ⁡ ( Σ L ∣ c) \operatorname{cdiam}(L\mid c)\geqslant\operatorname{cdiam}(\varSigma_{L}\mid c), since not all slits admissible for the point set T = Σ L T=\varSigma_{L} are necessarily admissible also for L L: some annuli may have non-quasiunipotent monodromy.

Let Ω \Omega be an integrable Pfaffian system on ℙ m × ℙ {\mathbb{P}}^{m}\times{\mathbb{P}} and D = { D λ } λ ∈ ℙ m D=\{D_{\lambda}\}_{\lambda\in{\mathbb{P}}^{m}} the associated isomonodromic family of linear ordinary differential operators in the standard form ( 49), equivalent to Ω \Omega in the sense explained in Lemma 35. Denote, as before, by p 0 ∈ ℂ ⁡ [λ, t] p_{0}\in{\mathbb{C}}[\lambda,t] the leading coefficient of the family D D and by 𝒮 = { λ: p 0 ​ ( λ, ⋅) = 0 } ⊂ ℙ m {\mathscr{S}}=\{\lambda\colon p_{0}(\lambda,{\,\boldsymbol{\cdot}}\,)=0\}\subset{\mathbb{P}}^{m} the degeneracy locus.

Then for any λ ∉ 𝒮 \lambda\notin{\mathscr{S}} we have a uniquely defined finite point set

 | T ⁡ ( λ) = { t ∈ ℂ: p 0 ​ ( t, λ) = 0 } ⊂ ℂ, λ ∉ 𝒮, T(\lambda)=\{t\in{\mathbb{C}}\colon p_{0}(t,\lambda)=0\}\subset{\mathbb{C}},\qquad\lambda\notin{\mathscr{S}}, |  | (59) |

which consists of at most l = deg ⁡ p 0 ⩽ O ⁡ ( ℓ 4 ​ d) l=\deg p_{0}\leqslant O(\ell^{4}d) points (some of which may escape to infinity for particular values of the parameter λ \lambda). The linear differential operator D λ D_{\lambda} is nonsingular on ℂ ​ – ​ T ​ ( λ) {\mathbb{C}}{\,\text{--}\,}T(\lambda), and we can introduce the function

 | Φ c ​ ( λ) = cdiam ⁡ ( D λ ∣ c), λ ∉ 𝒮. {\varPhi}_{c}(\lambda)=\operatorname{cdiam}(D_{\lambda}\mid c),\qquad\lambda\notin{\mathscr{S}}. |  | (60) |

###### Principal Lemma 52

A. Let Ω \Omega be an integrable rational Pfaffian system on ℙ m × ℙ {\mathbb{P}}^{m}\times{\mathbb{P}} and D = { D λ } D=\{D_{\lambda}\} the corresponding derived isomonodromic family of differential operators.

If Ω \Omega is quasiunipotent and c ⩾ O ⁡ ( ℓ 4 ​ d) c\geqslant O(\ell^{4}d), then the function Φ c {\varPhi}_{c} introduced in ( 60), is globally bounded everywhere on ℙ m {\mathbb{P}}^{m}.

B. If in addition Ω \Omega is defined over ℚ {\mathbb{Q}} and 𝐒 ⁡ ( Ω) ⩽ s \mathbf{S}\left(\Omega\right)\leqslant s, then Φ c {\varPhi}_{c} is defined over ℚ {\mathbb{Q}} and admits an explicit upper bound,

 | Φ c ​ ( λ) ⩽ s 2 O ​ ( d ​ ℓ 4 ​ m) 5 ∀ λ ∈ ℙ m ​ – ​ 𝒮. {\varPhi}_{c}(\lambda)\leqslant s^{2^{O(d\ell^{4}m)^{5}}}\qquad\forall\lambda\in{\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}}. |  | (61) |

In this formulation, as before, ℓ \ell is the dimension of the Pfaffian system Ω \Omega, d d its degree and m m the number of parameters. The proof of this Lemma occupies sections § 4.5 –§ 4.7.

### 4.5 Semialgebraicity of the cluster diameter

We start by observing that the cluster diameter of an isomonodromic family of linear operators is (bounded by) a semialgebraic function of the parameters. This would be fairly easy to prove using the technique of quantifier elimination if the requirement on the monodromy was absent in the definition, since the cluster diameter of a point set is determined by an explicit algorithmic formula. We show that the isomonodromy is the key to restoring the semialgebraicity.

###### Lemma 53

In the assumptions of Lemma 52 A the function Φ c {\varPhi}_{c} is everywhere finite on ℙ m ​ – ​ 𝒮 {\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}} and semialgebraic. The subgraph of Φ c {\varPhi}_{c} in ℙ m × ℝ + {\mathbb{P}}^{m}\times{\mathbb{R}}_{+} is a semialgebraic set defined by polynomial equalities and inequalities of degree not exceeding ( ℓ ​ d) O ​ ( c ​ m) 5 (\ell d)^{O(cm)^{5}}.

In the assumptions of Lemma 52 B, the function Φ c {\varPhi}_{c} is defined over ℚ {\mathbb{Q}} and has size explicitly bounded by a double exponent, i.e., its graph is defined by real polynomial (in)equalities with integer coefficients not exceeding

 | 𝐒 ⁡ ( Φ) ⩽ s ( ℓ ​ d) O ​ ( c ​ m) 5. \mathbf{S}\left({\varPhi}\right)\leqslant s^{(\ell d)^{O(cm)^{5}}}. |  | (62) |

###### Proof

Denote by l l the upper bound for the degree of the coefficients of the derived equation D D: by Lemma 35, l l is bounded by O ⁡ ( ℓ 4 ​ d) O(\ell^{4}d).

The clusterings of the set T = { t 1, …, t l } T=\{t_{1},\dots,t_{l}\} by c c circles S 1, …, S c S_{1},\dots,S_{c} can be parameterized by an open subset of the Euclidean space

 | 𝒞 3 ​ c = ℂ c × ℝ + c = { ( a 1, …, a c, r 1, …, r c) }, {\mathscr{C}}^{3c}={\mathbb{C}}^{c}\times{\mathbb{R}}_{+}^{c}=\{(a_{1},\dots,a_{c},r_{1},\dots,r_{c})\}, |  | (63) |

(each circle S i S_{i} is defined by the equations { | t − a i | = r i } \{|t-a_{i}|=r_{i}\}, i = 1, …, c i=1,\dots,c).

Consider the product ℙ m × 𝒞 3 ​ c {\mathbb{P}}^{m}\times{\mathscr{C}}^{3c}. The conditions ensuring that the circles form a clustering of the singular locus T ⁡ ( λ) = Σ D λ T(\lambda)=\varSigma_{D_{\lambda}} are semialgebraic: the singular points t 1, …, t l t_{1},\dots,t_{l}, which are algebraic functions of λ \lambda, should satisfy the inequalities

 | | t i − a j | ≠ r j, | a j − a k | > r j + r k or | a j − a k | < | r j − r k | |t_{i}-a_{j}|\neq r_{j},\qquad|a_{j}-a_{k}|>r_{j}+r_{k}\quad\text{or}\quad|a_{j}-a_{k}|<|r_{j}-r_{k}| |  |

for all roots t i t_{i} of the leading coefficient p 0 ​ ( t, λ) p_{0}(t,\lambda) and all pairs j ≠ k j\neq k, j, k = 1, …, c j,k=1,\dots,c. The latter conditions mean that the circles are disjoint and non-nested (resp., disjoint and nested). We add to these conditions the inequalities a i ≠ a j a_{i}\neq a_{j} which will guarantee that the shortest slits connecting any two given circles, are uniquely defined (as no two circles are concentric), and the conditions that the ratios ( t i − a j) / ( t i − a k) (t_{i}-a_{j})/(t_{i}-a_{k}) are non-real (this will guarantee that the shortest slits will not pass through the singular point t i t_{i}).

The points t i t_{i} themselves are defined by the equation p 0 ​ ( λ, t i) = 0 p_{0}(\lambda,t_{i})=0 (roots of the leading coefficient of the differential operator D λ D_{\lambda}) and the degree of that leading coefficient should be maximal (equal to l l) to avoid escape of the roots at infinity.

Altogether we have O ​ ( c + l) 3 O(c+l)^{3} real algebraic equalities/inequalities of degree ⩽ l \leqslant l and size ⩽ s \leqslant s in the space of 3 ​ c + 2 ​ m = O ⁡ ( c + m) 3c+2m=O(c+m) real variables ℙ m × 𝒞 3 ​ c {\mathbb{P}}^{m}\times{\mathscr{C}}^{3c}.

Admissible clusterings (defined by collections of circles, without any reference to the monodromy yet) form a semialgebraic open subset of the total space ℙ m × 𝒞 3 ​ c {\mathbb{P}}^{m}\times{\mathscr{C}}^{3c}, which consists of a large number of connected components (different topological configurations of singular points and circles). Each component C α C_{\alpha} is a semialgebraic set by ( BPR 03, Theorem 16.13). Moreover, its algebraic complexity can be explicitly bounded: each connected component can be defined over ℚ {\mathbb{Q}} by polynomial (in)equalities of degree not exceeding l O ​ ( c + m) 3 l^{O(c+m)^{3}} and size (complexity) at most s l O ​ ( c + m) 3 s^{l^{O(c+m)^{3}}}.

The admissible system of slits S ′ S^{\prime} based on a given clustering S ∈ 𝒞 3 ​ c S\in{\mathscr{C}}^{3c}, can be achieved by a finite number of choices (the number does not exceed O ⁡ ( c 2) O(c^{2})) of the segments γ j \gamma_{j}. Indeed, one can always assume that the segments γ j \gamma_{j} realize the shortest distance between each pair of circles of the clustering (see Fig. 1), and by construction this choice is uniquely defined over each connected component C α ⊂ ℙ m × 𝒞 3 ​ c C_{\alpha}\subset{\mathbb{P}}^{m}\times{\mathscr{C}}^{3c}. For any choice the normalized length of the resulting system will be a semialgebraic function on the position of the singularities and the clustering parameters (the coordinates of the corresponding point in 𝒞 3 ​ c {\mathscr{C}}^{3c}). In other words, the normalized length of any system of slits | S ′ / T ⁡ ( λ) | |S^{\prime}/T(\lambda)| can be considered as a multivalued semialgebraic function

 | Φ c ​ ( λ, S) = { | S ′ / T ⁡ ( λ) |: S ′ = S ⊔ γ 1 ⊔ ⋯ ⊔ γ 2 ​ l }, γ j ​ shortest slits, {\varPhi}_{c}(\lambda,S)=\{|S^{\prime}/T(\lambda)|\colon S^{\prime}=S\sqcup\gamma_{1}\sqcup\cdots\sqcup\gamma_{2l}\},\\ \quad\gamma_{j}\text{ shortest slits}, |  | (64) |

on ℙ m × 𝒞 {\mathbb{P}}^{m}\times{\mathscr{C}}. Each of the finitely many continuous branches of this function is semialgebraic on each connected component C α ⊂ ℙ m × 𝒞 C_{\alpha}\subset{\mathbb{P}}^{m}\times{\mathscr{C}}.

Moreover, each continuous branch of this function can be majorized by a function defined over ℚ {\mathbb{Q}}, if the initial system is defined over ℚ {\mathbb{Q}}. Indeed, the distance between a point t i t_{i} and the circle S j = { | t − a i | = r i } S_{j}=\{|t-a_{i}|=r_{i}\} is | r i − | t − a i | | \bigl|r_{i}-|t-a_{i}|\bigr|, the distance between two circles is given by a similar formula, all of them involving only the coordinate variables, the absolute value and the coefficients 0, ± 1 0,\pm 1. Thus the normalized length of all segments is defined over ℚ {\mathbb{Q}}. In the same manner the normalized length of the circles is defined over ℚ {\mathbb{Q}} (this is the reason why the factor 2 ​ π 2\pi appears in Definition 40 of the normalized length). The complexity of the formula defining Φ c ​ ( λ, S) {\varPhi}_{c}(\lambda,S) is at most polynomial in m + c m+c, since all coefficients are bounded by a common constant O ⁡ ( 1) O(1) (for brevity we denote the majorant by the same symbol as the initial function Φ c {\varPhi}_{c}).

It remains to take into account the requirement on the monodromy of the system (equation). In general, the *monodromy of a linear equation depends in a non-algebraic way on the equation*, thus the admissibility of a system of slits *cannot be defined by an algebraic condition*. However, since the initial system is integrable, *the monodromy is constant along any continuous branch ( system of slits) based on the clustering varying over a connected component*C α C_{\alpha}. In other words, the requirement of quasiunipotence reduces to a *branch selection of the function Φ c ​ ( λ, S) {\varPhi}_{c}(\lambda,S), defined on ℙ m × 𝒞 {\mathbb{P}}^{m}\times{\mathscr{C}}*: some of the branches give the normalized length of an admissible system of slits, while others do not.

It may well happen that for a given clustering S S there is no admissible system of slits based on this clustering, in which case we set Φ c ​ ( λ, S) = + ∞ {\varPhi}_{c}(\lambda,S)=+\infty. In the case where several systems of slits based on the same clustering are admissible, we can choose any of them to evaluate Φ c ​ ( λ, S) {\varPhi}_{c}(\lambda,S), or use the minimal value. This will not affect the complexity of the function Φ c ​ ( λ, S) {\varPhi}_{c}(\lambda,S).

Ultimately we can express the (majorant for the) cluster diameter ( 60) as an infimum of a semialgebraic function,

 | Φ c ​ ( λ) = inf S { Φ c ​ ( λ, S): ( λ, S) ∈ ℙ m × 𝒞 3 ​ c } ⩽ + ∞, {\varPhi}_{c}(\lambda)=\inf_{S}\{{\varPhi}_{c}(\lambda,S)\colon(\lambda,S)\in{\mathbb{P}}^{m}\times{\mathscr{C}}^{3c}\}\leqslant+\infty, |  | (65) |

which itself is semialgebraic by the Tarski–Seidenberg theorem (quantifier elimination principle). Moreover, since the complexity of the quantifier elimination algorithm is known, we can guarantee that the polynomial (inequalities) defining the graph of Φ c ​ ( λ) {\varPhi}_{c}(\lambda) over ℚ {\mathbb{Q}}, have degree at most l O ​ ( c + m) 3 ​ O ​ ( c) ​ O ​ ( m) ⩽ l O ​ ( c ​ m) 5 l^{O(c+m)^{3}O(c)O(m)}\leqslant l^{O(cm)^{5}} and size (complexity) at most s l O ​ ( c ​ m) 5 s^{l^{O(cm)^{5}}}. Substituting the value l = O ⁡ ( ℓ 4 ​ d) l=O(\ell^{4}d), we obtain the bound ( 62).

It remains to show that the function Φ c {\varPhi}_{c} takes finite values for all values of the parameter λ ∉ 𝒮 \lambda\notin{\mathscr{S}}, i.e., for matrices Ω λ \Omega_{\lambda} (resp., operators D λ D_{\lambda}) with finite singular locus, provided that c ⩾ l c\geqslant l.

In this case the clustering S λ S_{\lambda} which consists of exactly l l circles centered at each singular point t i ∈ T λ t_{i}\in T_{\lambda} and having sufficiently small radius r i ≪ 1 r_{i}\ll 1, can be completed by finitely many segments to an admissible system of slits. Indeed, one has to connect the small disks in an arbitrary way with each other and with a large circle “centered at infinity” (the circle whose exterior contains only one singular point at t = ∞ t=\infty): the only annuli that are formed by these slits, are punctured disks around singularities, and their monodromy is quasiunipotent by the quasiunipotence assumption on the initial system Ω \Omega (cf. with Remark 10). Thus Φ c ​ ( λ, S λ) < + ∞ {\varPhi}_{c}(\lambda,S_{\lambda})<+\infty, hence Φ c ​ ( λ) < + ∞ {\varPhi}_{c}(\lambda)<+\infty.

Note, however, that the finiteness of values of the function Φ c ​ ( λ) {\varPhi}_{c}(\lambda) for λ ∉ 𝒮 \lambda\notin{\mathscr{S}} does not imply yet its local boundedness. This last step is achieved in the next section.

### 4.6 Local boundedness of the cluster diameter in one-parametric quasiunipotent families

The cluster diameter of a finite point set T = T ⁡ ( λ) T=T(\lambda) (resp. a family D λ D_{\lambda} of equations) depending on a parameter, remains a continuous (hence locally bounded) function of λ \lambda as long as the points of T ⁡ ( λ) T(\lambda) (resp. the singular points of D λ D_{\lambda}) do not collide. In an analytic collision of two or more points the topological structure of the underlying clusters must be chosen depending on the relative “speed” of the colliding points. An explicit choice of this structure is possible in one-parametric families.

###### Lemma 54

Let Ω = { Ω λ } λ ∈ ( ℂ 1, 0) \Omega=\{\Omega_{\lambda}\}_{\lambda\in({\mathbb{C}}^{1},0)} be an integrable meromorphic quasiunipotent system on ( ℂ 1, 0) × ℙ 1 ({\mathbb{C}}^{1},0)\times{\mathbb{P}}^{1} and D = { D λ } D=\{D_{\lambda}\} the corresponding derived equations with rational coefficients of degree ⩽ l \leqslant l.

Then the function Φ c ​ ( λ) = cdiam ⁡ ( D λ ∣ c) {\varPhi}_{c}(\lambda)=\operatorname{cdiam}(D_{\lambda}\mid c) is bounded over all λ ∈ ( ℂ 1, 0) \lambda\in({\mathbb{C}}^{1},0), if c ⩾ 3 ​ l c\geqslant 3l.

###### Proof

Consider the singular locus of the system: in the coordinates ( λ, t) ∈ ( ℂ 1, 0) × ℂ 1 ⊂ ( ℂ 1, 0) × ℙ 1 (\lambda,t)\in({\mathbb{C}}^{1},0)\times{\mathbb{C}}^{1}\subset({\mathbb{C}}^{1},0)\times{\mathbb{P}}^{1} it is given by an equation p ⁡ ( λ, t) = 0 p(\lambda,t)=0, polynomial in t t with coefficients, holomorphic on λ \lambda of degree ⩽ l \leqslant l. Without loss of generality we may assume that p ⁡ ( 0, ⋅) ≠ 0 p(0,{\,\boldsymbol{\cdot}}\,)\neq 0 (otherwise divide p p by a suitable power of λ \lambda).

The equation has l l roots t 1 ​ ( λ), …, t l ​ ( λ) t_{1}(\lambda),\dots,t_{l}(\lambda), which are algebraic functions on λ \lambda and, as such, can be expressed by converging Puiseaux series. Passing to a fractional power of the parameter λ 1 / d = ε \lambda^{1/d}=\varepsilon, we may assume that each root is a holomorphic function, t j = t j ​ ( ε) t_{j}=t_{j}(\varepsilon), of the parameter ε \varepsilon. The quasiunipotence of the system is preserved by such re-parametrization.

We will construct a clustering S ε = { ( a i ​ ( ε), r i ​ ( ε)) } ∈ 𝒞 S_{\varepsilon}=\{(a_{i}(\varepsilon),r_{i}(\varepsilon))\}\in{\mathscr{C}} of all sets T ⁡ ( ε) = { t 1 ​ ( ε), …, t l ​ ( ε) } T(\varepsilon)=\{t_{1}(\varepsilon),\dots,t_{l}(\varepsilon)\} for all sufficiently small values of ε \varepsilon and an associated admissible system of slits for S ε S_{\varepsilon} (a continuous branch of the function Φ c ​ ( ε) {\varPhi}_{c}(\varepsilon) in the terminology of § 4.5) such that the function Φ c ​ ( ε, S ε) {\varPhi}_{c}(\varepsilon,S_{\varepsilon}) will be finite as ε → 0 \varepsilon\to 0 (see ( 64)).

[image: Refer to caption]

Figure 2: Construction of the admissible system of slits.

1. The outermost circle C 0 C_{0} of the clustering is the circle which contains all points of the set T ⁡ ( 0) T(0) and is of distance at least 1 1 from them.

The next embedded level is the union of circles C j C_{j} of radius ρ / 2 \rho/2 centered at all distinct points of the set T ⁡ ( 0) T(0), where

 | ρ = min t i ≠ t j { | t i − t j |, t i ∈ T ( 0) }. \rho=\min_{t_{i}\neq t_{j}}\{\left|t_{i}-t_{j}\right|,\quad t_{i}\in T(0)\}. |  | (66) |

Clearly, all these circles will be disjoint with T ⁡ ( ε) T(\varepsilon) for all sufficiently small ε \varepsilon, and the normalized length relative to T ⁡ ( ε) T(\varepsilon) of these circles remains bounded as ε → 0 \varepsilon\to 0. We can add shortest slits between the outermost circle C 0 C_{0} and some of the first level circles C 1 C_{1} to make the complement simply connected.

Construction of the next level circles is organized in the same way relative to circles of the first level, so we will explain it only for the circle C 1 C_{1} around one of the points t 1 ​ ( 0) ∈ T ​ ( 0) t_{1}(0)\in T(0), assuming for simplicity that this point is at the origin, t 1 ​ ( 0) = 0 t_{1}(0)=0, so that C 0 = { | t | = 1 } C_{0}=\{|t|=1\}.

2. If among the roots t j ​ ( ε) t_{j}(\varepsilon) there is only one such that t j ​ ( 0) = 0 t_{j}(0)=0, i.e., if the origin is a “simple” (non-multiple) point of T 0 T_{0}, then the construction in this circle stops, and the (degenerate) annulus { 0 < | t | < 1 } \{0<|t|<1\} has finite relative length for all small ε \varepsilon. The monodromy along this annulus is quasiunipotent by Remark 10.

3. If there is more than one root t j t_{j} with t j ​ ( 0) = 0 t_{j}(0)=0, then several holomorphic functions t j: ( ℂ 1, 0) → ℂ t_{j}\colon({\mathbb{C}}^{1},0)\to{\mathbb{C}} have the same 0 0 -jet. Assume that these functions are labeled as t 1 ​ ( ε), …, t p ​ ( ε) t_{1}(\varepsilon),\dots,t_{p}(\varepsilon), p ⩾ 2 p\geqslant 2. Let k ⩾ 1 k\geqslant 1 be the first natural number such that k k -jets of t 1, …, t p t_{1},\dots,t_{p} (in ε \varepsilon) are *not all equal*between themselves.

After the rescaling t ↦ s = ( t − t 1 ​ ( ε)) / ε k t\mapsto s=(t-t_{1}(\varepsilon))/\varepsilon^{k} in the new local chart s s we will obtain p p functions s 1 ​ ( ε), …, s p ​ ( ε) s_{1}(\varepsilon),\dots,s_{p}(\varepsilon), still holomorphic in ε \varepsilon, but with the limits s j ​ ( 0) s_{j}(0) not all coinciding.

Construct a circle C 0 ′ C^{\prime}_{0} which in the chart ( ε, s) (\varepsilon,s) is large enough to encircle all points s j ​ ( 0) s_{j}(0) and has distance at least 1 1 from them, and the smaller circles C j ′ C_{j}^{\prime} of the form { | s − s j ( 0) | = 1 3 ρ ′ } \{|s-s_{j}(0)|=\tfrac{1}{3}\rho^{\prime}\} centered at each distinct point of the set T ′ = { s 1 ​ ( 0), …, s p ​ ( 0) } T^{\prime}=\{s_{1}(0),\dots,s_{p}(0)\}, where

 | ρ ′ = min s i ≠ s j { | s i − s j |, s i ∈ T ′ }. \rho^{\prime}=\min_{s_{i}\neq s_{j}}\{\left|s_{i}-s_{j}\right|,\quad s_{i}\in T^{\prime}\}. |  | (67) |

In the original chart t t these will be very small circles (of radius O ⁡ ( ε k) O(\varepsilon^{k})). By construction, the normalized length of C 0 ′, C 1 ′, …, C p ′ C_{0}^{\prime},C_{1}^{\prime},\dots,C_{p}^{\prime} depends only on the position of the points inside C 1 C_{1}, since all other points of T ⁡ ( ε) T(\varepsilon) are incomparably far. On the other hand, because the normalized length is affine invariant, it can be computed in the chart s s, in which it is finite uniformly over all ε → 0 \varepsilon\to 0 by the same arguments as in the step 1 of the proof.

The circles C 0 ′, C 1 ′, … ​ C p ′ C_{0}^{\prime},C_{1}^{\prime},\dots C_{p}^{\prime} will be included in the clustering; the admissible system of slits is complemented by the slits between C 0 ′ C_{0}^{\prime} and some of the C j ′ C_{j}^{\prime} to make the slit interior of C 0 ′ ​ – ​ ⋃ j = 1 p D j ′ C_{0}^{\prime}{\,\text{--}\,}\bigcup_{j=1}^{p}D_{j}^{\prime} simply connected (here D j ′ D_{j}^{\prime} are the disks bounded by the circles C j ′ C_{j}^{\prime}). As in step 1, these extra slits will have uniformly finite normalized length as ε → 0 \varepsilon\to 0.

4. We need to show that the annulus bounded by C 1 C_{1} and C 0 ′ C_{0}^{\prime} has an admissible (quasiunipotent) monodromy. This is evident if the fiber { ε = 0 } \{\varepsilon=0\} is not in the singular locus of Ω \Omega, since then this monodromy coincides with the monodromy of C 1 C_{1}, which is admissible by the Kashiwara theorem 4. In the opposite case one needs slightly more involved arguments.

[image: Refer to caption]

Figure 3: Quasiunipotence of the loops encircling a cluster.

###### Lemma 55

The annulus bounded by C 1 C_{1} and C 0 ′ C_{0}^{\prime} on { ε = ε 1 } \{\varepsilon=\varepsilon_{1}\}, with sufficiently small ε 1 \varepsilon_{1}, has an admissible (quasiunipotent) monodromy.

Note that this is not an immediate corollary of the Kashiwara theorem, as the circle C 0 ′ C_{0}^{\prime} has zero linking number with { ε = 0 } \{\varepsilon=0\}, so it cannot be boundary of a holomorphic disc with center at the origin.

###### Proof

First, applying the translation t → t − t 1 ​ ( ε) t\to t-t_{1}(\varepsilon), we can assume that one of our curves coincides with the axis { t = 0 } \{t=0\}.

Consider first the case where the number k k which appeared on Step 3 above is equal to 1 1: this means that among the singularities forming the cluster, there are at least two points strictly O ⁡ ( ε) O(\varepsilon) -distant from each other as ε → 0 \varepsilon\to 0, | t j ​ ( ε) − t i ​ ( ε) | − 1 = O ⁡ ( ε − 1) |t_{j}(\varepsilon)-t_{i}(\varepsilon)|^{-1}=O(\varepsilon^{-1}).

Consider the blow-up ϕ \phi given in the affine chart ε ≠ 0 \varepsilon\neq 0 by ( t, ε) → ( ε, s = t / ε) (t,\varepsilon)\to(\varepsilon,s=t/\varepsilon), and denote by D ≅ ℙ 1 D\cong{\mathbb{P}}^{1} the corresponding exceptional divisor, see Fig. 3. The lifting of each curve t = t j ​ ( ε) t=t_{j}(\varepsilon) is the curve s = s j ​ ( ε) s=s_{j}(\varepsilon), with curves corresponding to our cluster (i.e. for j = 1, …, p j=1,\dots,p) tending to some well-defined limit on D D as ε → 0 \varepsilon\to 0, and other curves not intersecting some neighborhood U U of D D. The lifting of C 0 ′ C_{0}^{\prime} is a circle on { ε = ε 1 } \{\varepsilon=\varepsilon_{1}\} (still denoted by C 0 ′ C^{\prime}_{0}) encompassing all points ( s j ​ ( ε 1), ε 1) (s_{j}(\varepsilon_{1}),\varepsilon_{1}).

Now, C 0 ′ C_{0}^{\prime} is homotopic along the leaf ε = ε 1 \varepsilon=\varepsilon_{1} and inside U U to a small circle around s = ∞ s=\infty. Consider the second affine chart of the blow-up covering the neighborhood of ε = 0 \varepsilon=0. In this affine chart the blow-up is given by the formulas ( t, ε) → ( t, d = ε / t) (t,\varepsilon)\to(t,d=\varepsilon/t), the leaf { ε = ε 1 } \{\varepsilon=\varepsilon_{1}\} is defined by the equation { t d = ε 1 } \{td=\varepsilon_{1}\}, and C 0 ′ C_{0}^{\prime} is homotopic to the curve γ = { ( t = exp ⁡ ( 2 ​ π ​ i ​ θ), d = ε 1 ​ exp ⁡ ( − 2 ​ π ​ i ​ θ)), θ ∈ [0, 1] } \gamma=\{\left(t=\exp(2\pi i\theta),\,\mathrm{d}=\varepsilon_{1}\exp(-2\pi i\theta)\right),\ \theta\in[0,1]\}. Again, this curve has linking numbers of different signs with the t t -axis and d d -axis, so it cannot be a boundary of a holomorphic disc passing through the point ( t, d) = ( 0, 0) (t,d)=(0,0), i.e. it is not a small loop. In fact, if we denote by γ D = { ( t = exp ⁡ ( 2 ​ π ​ i ​ θ), d = d 0) } \gamma_{D}=\{(t=\exp(2\pi i\theta),d=d_{0})\} and γ E = { ( t = t 0, d = ε 1 k exp ( 2 π i θ)) \gamma_{E}=\{\left(t=t_{0},d=\varepsilon_{1}^{k}\exp(2\pi i\theta)\right) the two small loops encircling D = { t = 0 } D=\{t=0\} and E = { d = 0 } E=\{d=0\}, then γ = γ D ​ γ E − 1 \gamma=\gamma_{D}\gamma_{E}^{-1} in π 1 ( V – { t d = 0 }) \pi_{1}(V{\,\text{--}\,}\{td=0\}), where V V is a small neighborhood of the point ( t, d) = ( 0, 0) (t,d)=(0,0).

Consider the lifting ϕ ∗ ​ Ω \phi^{*}\Omega of the connection Ω \Omega. This lifting has admissible monodromy along small loops around the strict transform of the singular locus of Ω \Omega. It also has admissible monodromy along small loops around D D, since their projections are still small loops, so their monodromy is still admissible by Kashiwara theorem. This in means particular that the monodromies M D M_{D} and M E M_{E} of ϕ ∗ ​ Ω \phi^{*}\Omega along γ D \gamma_{D} and γ E \gamma_{E} respectively, are quasiunipotent. But M D M_{D} and M E M_{E} commute since D D and E E form a normal crossing, so that π 1 ( V ∖ { t d = 0 }) \pi_{1}(V\setminus\{td=0\}) is commutative. Thus the monodromy along γ \gamma is equal to the product M D ​ M E − 1 M_{D}M_{E}^{-1}, which is quasiunipotent as asserted.

For k > 1 k>1 one should perform k k blow-ups in order to get the same situation near the last exceptional divisor. Again, the only curves whose strict transforms will intersect the last divisor D D will be the curves corresponding to our cluster, and, deforming the loop encircling them to a neighborhood V V of the point of intersection of D D with the previous exceptional divisor, we represent it as a product of two monodromies. Both monodromies are quasiunipotent due to the Kashiwara theorem, and they commute for topological reasons, so their product is again quasiunipotent.

5. One can further iterate this construction, applying it to multiple points of the set T ′ ​ ( 0) T^{\prime}(0), if any, and constructing circles of the second level of embedding. Clearly, the maximal multiplicity goes down by at least one in each descent step, thus the tree-like clustering process terminates (in each branch) no later than after l l steps, the total number of the circles in the clustering being at most 3 ​ l 3l. Thus for c ⩾ 3 ​ l c\geqslant 3l the conformal diameter Φ c ​ ( λ) {\varPhi}_{c}(\lambda) is bounded over all λ ∈ ( ℂ 1, 0) \lambda\in({\mathbb{C}}^{1},0) as claimed.

###### Remark 56

The construction of the admissible system of slits for a quasiunipotent integrable system is completely classical. The reader will easily recognize in it the “screens” of Fulton and MacPherson FM 94 and/or the desingularization algorithm used in the proof of the Kashiwara theorem Kas 81. Definition 50 of the cluster diameter which is affine invariant was constructed in light of these two proofs.

### 4.7 Demonstration of the Principal Lemma 52

Consider an integrable rational family of quasiunipotent systems Ω = { Ω λ } \Omega=\{\Omega_{\lambda}\} on ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1} with the deleted indeterminacy locus 𝒮 ⊂ ℙ {\mathscr{S}}\subset{\mathbb{P}}.

The cluster diameter Φ c ​ ( λ) {\varPhi}_{c}(\lambda) is a semialgebraic function on ℙ m ​ – ​ 𝒮 {\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}}, continuous (hence locally bounded) outside 𝒮 {\mathscr{S}}, by Lemma 53.

We show that this function is locally bounded at each point of ℙ m {\mathbb{P}}^{m} (including points of 𝒮 {\mathscr{S}}) for c ⩾ 3 ​ l c\geqslant 3l. Indeed, assuming that Φ c {\varPhi}_{c} is unbounded, by the Curve Selection Lemma we can assume that Φ c {\varPhi}_{c} grows to infinity along some real analytic (even algebraic) curve in ℙ m ​ – ​ 𝒮 {\mathbb{P}}^{m}{\,\text{--}\,}{\mathscr{S}} with an endpoint in 𝒮 {\mathscr{S}} (cf. with the proof of Lemma 36). However, this is impossible by virtue of Lemma 54.

Thus Φ {\varPhi} is locally bounded near each point of ℙ m {\mathbb{P}}^{m}. Because of the compactness of the latter, we conclude that the cluster diameter is globally bounded, as asserted in Part A of the Lemma.

To prove Part B, note that by the second assertion of Lemma 53, the function Φ c {\varPhi}_{c} is defined over ℚ {\mathbb{Q}} by polynomial (in)equalities of degree not exceeding ( ℓ ​ d) O ​ ( l ​ m) 5 (\ell d)^{O(lm)^{5}} and its complexity is explicitly bounded by the double exponent s ( ℓ ​ d) O ​ ( l ​ m) 5 s^{(\ell d)^{O(lm)^{5}}} as in ( 62), where l = O ⁡ ( ℓ 4 ​ d) l=O(\ell^{4}d). By the “quantization principle” (Theorem 6, cf. with Example 19), the uniform maximum of Φ c {\varPhi}_{c} does not exceed the double exponential expression

 | ( s ( ℓ ​ d) O ​ ( l ​ m) 5) ( ℓ ​ d) O ​ ( l ​ m) 5 = s ( ℓ ​ d) O + ​ ( d ​ ℓ 4 ​ m) 5 = s 2 O + ​ ( d ​ ℓ 4 ​ m) 5, \biggl(s^{(\ell d)^{O(lm)^{5}}}\biggr)^{(\ell d)^{O(lm)^{5}}}=s^{(\ell d)^{O^{+}(d\ell^{4}m)^{5}}}=s^{2^{O^{+}(d\ell^{4}m)^{5}}}, |  |

which coincides with ( 61).∎

### 4.8 Proof of Theorems 7 and 8

Consider the Pfaffian system ( 12) on ℙ m × ℙ 1 {\mathbb{P}}^{m}\times{\mathbb{P}}^{1} and the corresponding derived family D D of homogeneous differential equations ( 30), and fix an arbitrary value of the parameters λ ∉ 𝒮 \lambda\notin{\mathscr{S}}.

The invariant slope of the corresponding operator D λ D_{\lambda} is explicitly bounded by the Principal Lemma 33, by a double exponential expression ( 45):

 | ∢ ​ D λ ⩽ s ( d ​ ℓ) O ⁡ ( m). \sphericalangle D_{\lambda}\leqslant s^{(d\ell)^{O(m)}}. |  | (68) |

In addition, the cluster diameter of the family D λ D_{\lambda} with c = 3 ​ l = O ⁡ ( ℓ 4 ​ d) c=3l=O(\ell^{4}d) circular slits is uniformly bounded, and does not exceed the double exponential bound ( 61)

 | L = cdiam ⁡ ( D λ ∣ c) ⩽ s 2 O + ​ ( ℓ 4 ​ d ​ m) 5, L=\operatorname{cdiam}(D_{\lambda}\mid c)\leqslant s^{2^{O^{+}(\ell^{4}dm)^{5}}}, |  | (69) |

by Principal Lemma 52.

For each of the simply connected domains U i U_{i} formed by the admissible slits, the variation of argument does not exceed the product ( 56) (Lemma 42) which, after substitution of the bounds ( 68) and ( 69) and k = O ⁡ ( ℓ 2) k=O(\ell^{2}) yields the double exponential bound s 2 O + ​ ( d ​ ℓ 4 ​ m) 5 s^{2^{O^{+}(d\ell^{4}m)^{5}}} which absorbs all other terms in the product. This places an upper bound for the number of zeros 𝒩 ⁡ ( Ω / U i) {\mathcal{N}}(\Omega/U_{i}). By the same token, the same bound holds for the number of zeros 𝒩 ⁡ ( Ω / U j) {\mathcal{N}}(\Omega/U_{j}) in each annulus U j U_{j} formed by the admissible slits: this follows from Lemma 44.

Since any triangle T T may intersect at most O ⁡ ( l) O(l) different domains (recall that l l measures the topological complexity of the singular locus and hence the number of simply connected domains/annuli, appearing by admissible slits) the total number of zeros 𝒩 ⁡ ( Ω) {\mathcal{N}}(\Omega) is bounded by the double exponent as asserted.

### 4.9 Concluding remarks

The growth of the upper bound for L L (the cluster diameter), which is the fastest of the three terms in the products ( 56) and ( 58), is determined by the complexity of the clustering algorithm. The asymptotics can be improved at the cost of transparency.

For instance, among the l = O ⁡ ( ℓ 4 ​ d) l=O(\ell^{4}d) singular points of the derived equation, almost all (except for d d) are *apparent singularities*at which solutions of the equation are non-ramified (and even remain holomorphic). Clearly, the location of such apparent points cannot affect the quasiunipotence of the monodromy along an annulus. On the other hand, the normalized distance from these points to the slits of an admissible system is important. Thus instead of the 3 ​ l 3l slits used in the proof, one can use only 3 ​ d 3d slits, while the corresponding normalized length will be given by a formula which is considerably more complex (involving distance between roots of an equation and a given circle). Yet since the complexity plays much less crucial role than the number of variables, the overall result will be ultimately better.

Other more subtle modifications can be made in order to prove a bound which is double exponential only in the number of parameters of the original system. However, for the purpose of preserving the clarity of exposition, we shall not investigate the necessary modifications in this paper.

Another interesting example is that of hyperelliptic integrals. In this case the monodromy of *any*annulus free from the singular points, is quasiunipotent. This follows from the Lyashko–Looijenga theorem Loo 74 asserting that any deformation of critical values of a univariate polynomial can be achieved by a suitable deformation of its coefficients (a fact which is wrong for multivariate polynomials). Thus any k < n = deg ⁡ H k<n=\deg H singular points of a hyperelliptic Picard–Fuchs system can be isomonodromically deformed into a degenerate singularity, so any loop is homotopic to a small loop.

This observation means that in the construction of the admissible system of slits one can drop the monodromy condition and hence skip the step of isolating a connected component C α C_{\alpha} in the proof of Lemma 53. The problem of optimizing the admissible system of slits becomes the problem from the elementary Euclidean geometry on the plane, namely the computation of the cluster diameter of a point set T T without additional restrictions. Using elementary arguments, one can estimate the cluster diameter by a simple exponent of l = #​ T l=\#T: cdiam ⁡ ( T ∣ 3 ​ l) ⩽ 2 O ⁡ ( l) \operatorname{cdiam}(T\mid 3l)\leqslant 2^{O(l)}.

Given that the hyperelliptic Hamiltonian of degree n + 1 n+1 has n n coefficients (and not O ⁡ ( n 2) O(n^{2}), as a bivariate polynomial), we have a better bound for the invariant slope of the corresponding derived equation. The corresponding double exponent 2 2 O + ​ ( n) 2^{2^{O^{+}(n)}} absorbs all other dependencies and altogether the mentioned improvements give the bound described in Theorem 3. We leave the details to the reader.

## Appendix A Appendix. Complexity of the Picard–Fuchs system

In this appendix we show that the Picard–Fuchs system of linear Pfaffian equations satisfied by the periods of monomial forms is defined over ℚ {\mathbb{Q}} and has an explicitly bounded complexity (size) and prove Theorem 9.

This proof can be achieved by inspection of the effective derivation of the Picard–Fuchs system in Yak 02, see also NY 01 for an earlier version. For the readers’ convenience, we reproduce the construction here together with all required estimates.

### A.1 Effective decomposition in the Petrov module

In what follows we fix a natural number n ∈ ℕ n\in{\mathbb{N}} and denote by H H the polynomial

 | H ⁡ ( x, λ) = ∑ 0 ⩽ | α | ⩽ n + 1 λ α ​ x α ∈ ℤ ⁡ [x, λ], x = ( x 1, x 2), λ ∈ ℂ m + 1 H(x,\lambda)=\sum_{0\leqslant|\alpha|\leqslant n+1}\lambda_{\alpha}x^{\alpha}\in{\mathbb{Z}}[x,\lambda],\qquad x=(x_{1},x_{2}),\ \lambda\in{\mathbb{C}}^{m+1} |  |

(we use the standard multiindex notation, x = ( x 1, x 2) x=(x_{1},x_{2}), α = ( α 1, α 2) ∈ ℤ + 2 \alpha=(\alpha_{1},\alpha_{2})\in{\mathbb{Z}}_{+}^{2}). For each specification of λ ∈ ℂ m + 1 \lambda\in{\mathbb{C}}^{m+1} we obtain a complex polynomial H ⁡ ( ⋅, λ) ∈ ℂ ⁡ [x] H({\,\boldsymbol{\cdot}}\,,\lambda)\in{\mathbb{C}}[x], which for a generic value of λ \lambda is a Morse function with the principal homogeneous part H ^ ​ ( ⋅, λ) \widehat{H}({\,\boldsymbol{\cdot}}\,,\lambda) having an isolated critical point of multiplicity n 2 n^{2} at the origin, where

 | H ^ ​ ( x, λ) = ∑ | α | = n + 1 λ α ​ x α \widehat{H}(x,\lambda)=\sum_{|\alpha|=n+1}\lambda_{\alpha}x^{\alpha} |  |

(the latter condition occurs if and only if H ^ ​ ( ⋅, λ) \widehat{H}({\,\boldsymbol{\cdot}}\,,\lambda) is square-free in ℂ ⁡ [x] {\mathbb{C}}[x]).

It is well-known that the monomials x α x^{\alpha}, 0 ⩽ α 1, 2 ⩽ n − 1 0\leqslant\alpha_{1,2}\leqslant n-1, constitute a basis in the quotient space

 | Q λ = ℂ ⁡ [x] / I λ, I λ = ⟨ ∂ H ^ ∂ x 1 ​ ( x, λ), ∂ H ^ ∂ x 2 ​ ( x, λ) ⟩ ⊂ ℂ ⁡ [x 1, x 2] Q_{\lambda}={\mathbb{C}}[x]/I_{\lambda},\qquad I_{\lambda}=\biggl<\frac{\partial\widehat{H}}{\partial x_{1}}(x,\lambda),\frac{\partial\widehat{H}}{\partial x_{2}}(x,\lambda)\biggr>\subset{\mathbb{C}}[x_{1},x_{2}] |  | (70) |

by the gradient ideal I λ I_{\lambda} for almost all (though not all) λ \lambda such that H ^ ​ ( ⋅, λ) \widehat{H}({\,\boldsymbol{\cdot}}\,,\lambda) is square-free. For such values of the parameters λ \lambda the forms μ α = x α ​ d ​ x 1 ∧ d ​ x 2 \mu_{\alpha}=x^{\alpha}\,\mathrm{d}x_{1}\land\mathrm{d}x_{2} form the basis of the module of the Brieskorn lattice and their (monomial) primitives generate the so called Petrov module ( IY 08, §26E). More precisely, we have the following result ( IY 08, Theorem 26.21).

Let ω α ∈ Λ 1 ​ ( ℂ 2) \omega_{\alpha}\in\varLambda^{1}({\mathbb{C}}^{2}) be the monomial 1-forms such that d ​ ω α = μ α \,\mathrm{d}\omega_{\alpha}=\mu_{\alpha}, 0 ⩽ α 1, 2 ⩽ n − 1 0\leqslant\alpha_{1,2}\leqslant n-1, and ω \omega any other monomial form.

###### Theorem 10 ( see IY 08)

If the monomials x α x^{\alpha} as before generate the quotient space ( 70) for a given value λ \lambda, then for any monomial form ω \omega there exist univariate polynomials p α ∈ ℂ ⁡ [t] p_{\alpha}\in{\mathbb{C}}[t] and bivariate polynomials u, v ∈ ℂ ⁡ [x 1, x 2] u,v\in{\mathbb{C}}[x_{1},x_{2}] such that

 | ω = ∑ α ( p α ∘ H) ⋅ ω α + u ​ d ​ H + d ​ v 0 ⩽ α 1, 2 ⩽ n − 1, p α ∈ ℂ ⁡ [t], u, v ∈ ℂ ⁡ [x 1, x 2], d ​ H = ∂ H ∂ x 1 ​ d ​ x 1 + ∂ H ∂ x 2 ​ d ​ x 2, { ( n + 1) ​ deg ⁡ p α + deg ⁡ ω α deg ⁡ v n + deg ⁡ u ⩽ deg ω. \begin{gathered}\omega=\sum_{\alpha}(p_{\alpha}\circ H)\cdot\omega_{\alpha}+u\,\mathrm{d}H+\,\mathrm{d}v\quad 0\leqslant\alpha_{1,2}\leqslant n-1,\\ p_{\alpha}\in{\mathbb{C}}[t],\ u,v\in{\mathbb{C}}[x_{1},x_{2}],\quad\,\mathrm{d}H=\frac{\partial H}{\partial x_{1}}\,\mathrm{d}x_{1}+\frac{\partial H}{\partial x_{2}}\,\mathrm{d}x_{2},\\ \left\{\begin{aligned} &(n+1)\deg p_{\alpha}+\deg\omega_{\alpha}\\ &\deg v\\ &n+\deg u\end{aligned}\right.\quad\leqslant\deg\omega.\end{gathered} |  | (71) |

In a similar way, the forms μ α = d ​ ω α \mu_{\alpha}=\,\mathrm{d}\omega_{\alpha} themselves generate all polynomial 2 2 -forms Λ 2 \varLambda^{2} as a module over ℂ ⁡ [t] {\mathbb{C}}[t] modulo the submodule d ​ H ∧ Λ 1 \,\mathrm{d}H\land\varLambda^{1}: any monomial 2-form μ \mu admits a representation

 | μ = ∑ α ( p α ∘ H) ⋅ μ α + d ​ H ∧ η, η ∈ Λ 1, \mu=\sum_{\alpha}(p_{\alpha}\circ H)\cdot\mu_{\alpha}+\,\mathrm{d}H\land\eta,\qquad\eta\in\varLambda^{1}, |  | (72) |

with analogous inequalities between the degrees of the coefficients p α p_{\alpha} and the “incomplete ratio” η \eta.

While the Theorem says nothing about the dependence of the result of the division on λ \lambda, we claim that, as functions of λ \lambda, the polynomials p α p_{\alpha} (the remainders) and the 1-form η \eta are rational and defined over ℚ {\mathbb{Q}} if the left hand sides ω \omega, resp., μ \mu are over ℚ {\mathbb{Q}}. For future calculations we will need only the situation when the expanded forms ω \omega, μ \mu are monomial of degree not exceeding O ⁡ ( n 2) O(n^{2}).

###### Proposition 57

Assume that ω \omega ( resp., μ \mu) is a monomial 1-form ( resp., 2-form) of degree at most O ⁡ ( n 2) O(n^{2}).

Then one can construct an expansion ( 71), resp., ( 72), so that the functions p α ∈ ℂ ​ [t] ​ ( λ) p_{\alpha}\in{\mathbb{C}}[t](\lambda), the polynomials u, v ∈ ℂ ​ [x, y] ​ ( λ) u,v\in{\mathbb{C}}[x,y](\lambda) and the polynomial 1-form η ∈ ℂ ⁡ ( λ) ⊗ Λ 1 ​ [x, y] \eta\in{\mathbb{C}}(\lambda)\otimes\varLambda^{1}[x,y] are all defined over ℚ {\mathbb{Q}}, their degrees are bounded by explicit expressions growing no faster than O ⁡ ( n 2) O(n^{2}) and their sizes do not exceed 2 O ⁡ ( n 3) 2^{O(n^{3})}.

###### Proof

Both systems ( 71), ( 72) are linear with respect to the unknown polynomials p α ​ ( t) p_{\alpha}(t), u ⁡ ( x), v ⁡ ( x) u(x),v(x) and polynomial 1-form η \eta, thus the latter could all be found using the method of indeterminate coefficients.

The degrees of these objects are explicitly bounded by Theorem 10, so we have an explicit control over the number of unknown indeterminate coefficients to be found,

 | deg p α = O ( 1), dim { p α } = O ( n 2), dim u, dim v, dim η = O ( n 2), \deg p_{\alpha}=O(1),\quad\dim\{p_{\alpha}\}=O(n^{2}),\quad\dim u,\dim v,\dim\eta=O(n^{2}), |  |

(where by dim ( ⋅) \dim({\,\boldsymbol{\cdot}}\,) we mean the number of the unknown coefficients in the expansion of these objects as polynomials in t t and x x respectively). Altogether we see that each of the systems ( 71), ( 72) reduces to a system of linear (non-homogeneous) algebraic equations. The number of unknowns N N of this system is at most O ⁡ ( n 2) O(n^{2}), and all entries of the corresponding matrix are polynomials from ℤ ⁡ [λ] {\mathbb{Z}}[\lambda]: these polynomials are computed using the explicit expression for H H and d ​ H \,\mathrm{d}H respectively. The degrees of the entries in λ \lambda are at most deg ⁡ p α ⩽ O ⁡ ( 1) \deg p_{\alpha}\leqslant O(1), since H H is linear in λ \lambda by assumption. The size (complexity) of the entries is also bounded by n n (the biggest natural number that appears in the expansion of d ​ H \,\mathrm{d}H as a function of λ \lambda).

Solutions of such a linear system can be obtained as in Example 17. By construction, the corresponding minors will be polynomials from ℤ ⁡ [λ] {\mathbb{Z}}[\lambda] of degrees not exceeding O ⁡ ( N) = O ⁡ ( n 2) O(N)=O(n^{2}) and the size (complexity) not exceeding N! ​ n N ⩽ 2 O ⁡ ( n 3) N!\,n^{N}\leqslant 2^{O(n^{3})}.

###### Remark 58

A more accurate analysis carried out in Yak 02 shows that the denominators of the rational fractions representing the polynomials p α p_{\alpha} may involve only the parameters λ α \lambda_{\alpha} with | α | = n + 1 |\alpha|=n+1 corresponding to the principal homogeneous part of H H; the dependence on the non-principal coefficients with | α | ⩽ n |\alpha|\leqslant n is always polynomial.

### A.2 Gelfand-Leray derivative

For any fixed (independent of λ \lambda) polynomial 1-form ω ∈ Λ 1 ​ ( ℂ 2) \omega\in\varLambda^{1}({\mathbb{C}}^{2}) and any multiindex α \alpha the derivative

 | ∂ ∂ λ α ∮ δ ω, δ ⊂ { H = 0 }, H = ∑ 0 ⩽ | α | ⩽ n + 1 λ α x α \frac{\partial}{\partial\lambda_{\alpha}}\oint_{\delta}\omega,\qquad\delta\subset\{H=0\},\quad H=\sum_{0\leqslant|\alpha|\leqslant n+1}\lambda_{\alpha}x^{\alpha} |  | (73) |

can be expressed as the integral of another (in general, only rational in x x) 1-form η \eta over the same cycle δ ⊂ { H = 0 } \delta\subset\{H=0\}, if the latter satisfies the identity

 | x α ​ d ​ ω = − d ​ H ∧ η. x^{\alpha}\,\mathrm{d}\omega=-\,\mathrm{d}H\land\eta. |  | (74) |

This follows easily ( Yak 02, Lemma 3) from the “standard” Gelfand–Leray formula which corresponds to α = ( 0, 0) \alpha=(0,0) ( IY 08, Theorem 26.32). We use this observation to express the derivative of the period matrix X X of the monomial 1-forms ω α \omega_{\alpha} forming the basis.

### A.3 Effective derivation of the Picard–Fuchs system

In this section we complete the proof of Theorem 9.

Let X X be the period ℓ × ℓ \ell\times\ell -matrix of monomial 1-forms ω α \omega_{\alpha}, 0 ⩽ α 1, 2 ⩽ n − 1 0\leqslant\alpha_{1,2}\leqslant n-1, ℓ = n 2 \ell=n^{2}, cf. with ( 11). Denote as before μ α = d ​ ω α \mu_{\alpha}=\,\mathrm{d}\omega_{\alpha}.

For any μ α \mu_{\alpha} the multiple H ⋅ μ α H\cdot\mu_{\alpha} is a polynomial (in x x) 2-form of degree ⩽ ( n + 1) + n 2 \leqslant(n+1)+n^{2} with coefficients polynomially depending on λ \lambda. By ( 72), there exist decompositions (the results of division by d ​ H \,\mathrm{d}H with remainder)

 | H ⋅ μ α = ∑ 0 ⩽ | β | ⩽ n + 1 ( P α ​ β ⋆ ∘ H) ⋅ μ β + d ​ H ∧ η α H\cdot\mu_{\alpha}=\sum_{0\leqslant|\beta|\leqslant n+1}(P^{\star}_{\alpha\beta}\circ H)\cdot\mu_{\beta}+\,\mathrm{d}H\land\eta_{\alpha} |  | (75) |

in which 𝐏 ⋆ = { P α ​ β ∗ } α, β \mathbf{P}^{\star}=\{P^{*}_{\alpha\beta}\}_{\alpha,\beta} is an ℓ × ℓ \ell\times\ell -matrix function, with entries in ℚ ​ [t] ​ ( λ) {\mathbb{Q}}[t](\lambda) (polynomial in t t and rational in λ \lambda). Their complexity (degree and size) are bounded by Proposition 57.

Since d ⁡ ( H ​ ω α) = H ​ μ α + d ​ H ∧ ω α \,\mathrm{d}(H\omega_{\alpha})=H\mu_{\alpha}+\,\mathrm{d}H\land\omega_{\alpha} and the entries of the matrix function 𝐏 ⋆ ​ ( t) \mathbf{P}^{\star}(t) do not depend on x x, the previous identities can be transformed to the form

 | d ⁡ ( H ​ ω α − ∑ β ( P α ​ β ⋆ ∘ H) ⋅ ω β) = − d ​ H ∧ ( − ω α − η α), \,\mathrm{d}\biggl(H\omega_{\alpha}-\sum_{\beta}(P^{\star}_{\alpha\beta}\circ H)\cdot\omega_{\beta}\biggr)=-\,\mathrm{d}H\land(-\omega_{\alpha}-\eta_{\alpha}), |  |

where d = ∂ ∂ x 1 ​ d ​ x 1 + ∂ ∂ x 2 ​ d ​ x 2 \,\mathrm{d}=\frac{\partial}{\partial x_{1}}\,\mathrm{d}x_{1}+\frac{\partial}{\partial x_{2}}\,\mathrm{d}x_{2}.

Now one can choose any multiindex s ∈ ℤ + 2 s\in{\mathbb{Z}}_{+}^{2} and apply the Gelfand–Leray formula with α = s \alpha=s to conclude that the partial derivative of the matrix function H ​ X − 𝐏 ⋆ ​ X HX-\mathbf{P}^{\star}X with respect to λ s \lambda_{s} is equal to the period matrix of the forms − x s ​ ( ω α + η α) -x^{s}(\omega_{\alpha}+\eta_{\alpha}):

 | ∂ ∂ λ s ∮ δ ( H ω α − ∑ β ( P α ​ β ⋆ ∘ H) ⋅ ω β) = − ∮ δ x s ( ω α + η α). \frac{\partial}{\partial\lambda_{s}}\oint_{\delta}\biggl(H\,\omega_{\alpha}-\sum_{\beta}(P^{\star}_{\alpha\beta}\circ H)\cdot\omega_{\beta}\biggr)=-\oint_{\delta}x^{s}(\omega_{\alpha}+\eta_{\alpha}). |  | (76) |

It remains to note the polynomial (in x x) 1-forms x s ​ ( ω α + η α) x^{s}(\omega_{\alpha}+\eta_{\alpha}) can be expanded as combinations of the basic forms ω α \omega_{\alpha} with coefficients in ℚ ​ [t] ​ ( λ) {\mathbb{Q}}[t](\lambda) of controlled degree and size by ( 71) and Proposition 57. Denote by 𝐏 s = { P α ​ β s } α, β \mathbf{P}^{s}=\bigl\{P^{s}_{\alpha\beta}\bigr\}_{\alpha,\beta} the corresponding matrix functions with entries from ℚ ​ [t] ​ ( λ) {\mathbb{Q}}[t](\lambda):

 | x s ​ ( ω α + η α) = ∑ β ( P α ​ β s ∘ H) ⋅ ω β + u α ​ d ​ H + d ​ v α. x^{s}(\omega_{\alpha}+\eta_{\alpha})=\sum_{\beta}(P^{s}_{\alpha\beta}\circ H)\cdot\omega_{\beta}+u_{\alpha}\,\mathrm{d}H+\,\mathrm{d}v_{\alpha}. |  |

Substituting these identities in ( 76) and integrating them over the cycle δ ⊂ { H = 0 } \delta\subset\{H=0\}, on which the polynomial H H vanishes identically, we conclude that

 | ∀ s = ( s 1, s 2) ∈ ℤ + 2, 0 ⩽ s 1, 2 ⩽ n − 1, ∂ ∂ λ s ​ ( 𝐏 0 ⋆ ​ X) = 𝐏 0 s ​ X. \forall s=(s_{1},s_{2})\in{\mathbb{Z}}_{+}^{2},\ 0\leqslant s_{1,2}\leqslant n-1,\quad\frac{\partial}{\partial\lambda_{s}}\bigl(\mathbf{P}_{0}^{\star}X\bigr)=\mathbf{P}_{0}^{s}X. |  | (77) |

Here 𝐏 0 ⋆ = 𝐏 ⋆ ​ ( 0) \mathbf{P}_{0}^{\star}=\mathbf{P}^{\star}(0) and 𝐏 0 s = 𝐏 s ​ ( 0) \mathbf{P}^{s}_{0}=\mathbf{P}^{s}(0) are matrices with entries in ℚ ⁡ ( λ) {\mathbb{Q}}(\lambda), obtained by setting t = 0 t=0 in their initial expressions. This is the Pfaffian integrable system on the projective space λ ∈ ℙ m \lambda\in{\mathbb{P}}^{m}.

From Proposition 57 it follows that the entries of the matrix functions 𝐏 0 ⋆, 𝐏 0 s \mathbf{P}_{0}^{\star},\mathbf{P}_{0}^{s} are in ℚ ⁡ ( λ) {\mathbb{Q}}(\lambda) and have degrees growing as Poly ⁡ ( n) \operatorname{\textup{Poly}}(n) and the size (complexity) at most exponential (bounded by 2 Poly ⁡ ( n) 2^{\operatorname{\textup{Poly}}(n)}). This proves Theorem 9.

## References

- AGV (88) V. I. Arnold, S. M. Gusein-Zade, and A. N. Varchenko, *Singularities of differentiable maps*, vol. II, Monodromy and asymptotics of integrals, Birkhäuser Boston Inc., Boston, MA, 1988. MR 89g:58024
- Arn (04) V. I. Arnold, *Arnold’s problems*, Springer-Verlag, Berlin, 2004, Translated and revised edition of the 2000 Russian original, With a preface by V. Philippov, A. Yakivchik and M. Peters. MR2078115 (2005c:58001)
- BM (08) M. Bobieński and P. Mardešić, *Pseudo-Abelian integrals along Darboux cycles*, Proc. Lond. Math. Soc. (3) 97 (2008), no. 3, 669–688. MR2448243 (2009f:34082)
- Bog (76) R. I. Bogdanov, *Bifurcations of a limit cycle of a certain family of vector fields on the plane*, Trudy Sem. Petrovsk. (1976), no. 2, 23–35. MR 56 #1363
- BPR (03) S. Basu, R. Pollack, and M.-F. Roy, *Algorithms in real algebraic geometry*, Algorithms and Computation in Mathematics, vol. 10, Springer-Verlag, Berlin, 2003. MR 2004g:14064
- Bri (70) E. Brieskorn, *Die Monodromie der isolierten Singularitäten von Hyperflächen*, Manuscripta Math. 2 (1970), 103–161. MR 42 #2509
- BV (07) S. Basu and N. Vorobjov, *On the number of homotopy types of fibres of a definable map*, J. Lond. Math. Soc. (2) 76 (2007), no. 3, 757–776. MR2377123
- BY (10) G. Binyamini and S. Yakovenko, *Polynomial bounds for oscillation of solutions of Fuchsian systems*, Annales de l’Institut Fourier 60 (2010), 1–31, available as Preprint ArXiV:0808.2950 [math.DS].
- CDR (07) M. Caubergh, F. Dumortier, and R. Roussarie, *Alien limit cycles in rigid unfoldings of a Hamiltonian 2-saddle cycle*, Commun. Pure Appl. Anal. 6 (2007), no. 1, 1–21. MR2276327 (2008f:34066)
- CL (07) C. Christopher and C. Li, *Limit cycles of differential equations*, Advanced Courses in Mathematics. CRM Barcelona, Birkhäuser Verlag, Basel, 2007. MR2325099 (2008d:34001)
- Cle (69) C. H. Clemens, Jr., *Picard-Lefschetz theorem for families of nonsingular algebraic varieties acquiring ordinary singularities*, Trans. Amer. Math. Soc. 136 (1969), 93–108. MR0233814 (38 #2135)
- dlVP (29) C. de la Valleé Poussin, *Sur l’équation différentielle linéaire du second ordre. détermination d’une intégrale par deux valeurs assignées. extension aux équations d’ordre n n*, J. Math. Pures Appl. 8 (1929), 125–144.
- DR (06) F. Dumortier and R. Roussarie, *Abelian integrals and limit cycles*, J. Differential Equations 227 (2006), no. 1, 116–165. MR2233957 (2007c:34049)
- FM (94) W. Fulton and R. MacPherson, *A compactification of configuration spaces*, Ann. of Math. (2) 139 (1994), no. 1, 183–225. MR1259368 (95j:14002)
- Fra (96) J. P. Françoise, *Successive derivatives of a first return map, application to the study of quadratic vector fields*, Ergodic Theory Dynam. Systems 16 (1996), no. 1, 87–96. MR1375128 (97a:58131)
- Gab (68) A. M. Gabrièlov, *Projections of semianalytic sets*, Functional Anal. Appl. 2 (1968), no. 4, 18–30. MR0245831 (39 #7137)
- Gav (98) L. Gavrilov, *Petrov modules and zeros of Abelian integrals*, Bull. Sci. Math. 122 (1998), no. 8, 571–584. MR 99m:32043
- Gav (99), *Abelian integrals related to Morse polynomials and perturbations of plane Hamiltonian vector fields*, Ann. Inst. Fourier (Grenoble) 49 (1999), no. 2, 611–652. MR 1 697 374
- Gav (05), *Higher order Poincaré-Pontryagin functions and iterated path integrals*, Ann. Fac. Sci. Toulouse Math. (6) 14 (2005), no. 4, 663–682. MR2188587 (2006i:34074)
- GI (05) L. Gavrilov and I. D. Iliev, *The displacement map associated to polynomial unfoldings of planar Hamiltonian vector fields*, Amer. J. Math. 127 (2005), no. 6, 1153–1190. MR2183522 (2006h:34065)
- GI (06) A. Glutsyuk and Yu. Ilyashenko, *The restricted infinitesimal Hilbert 16th problem*, Dokl. Akad. Nauk 407 (2006), no. 2, 154–159. MR2348308
- GI (07), *Restricted version of the infinitesimal Hilbert 16th problem*, Mosc. Math. J. 7 (2007), no. 2, 281–325, 351. MR2337884
- Glu (05) A. Glutsyuk, *Upper bounds of topology of complex polynomials in two variables*, Mosc. Math. J. 5 (2005), no. 4, 781–828, 972. MR2266460
- Glu (06), *An explicit formula for period determinant*, Ann. Inst. Fourier (Grenoble) 56 (2006), no. 4, 887–917. MR2266882 (2007f:32034)
- GN (08) L. Gavrilov and D. Novikov, *On the finite cyclicity of open period annuli*, Preprint ArXiv 0807.0512 (2008), 1–22.
- Gri (01) A. Grigoriev, *Singular perturbations and zeros of Abelian integrals*, Ph. D. thesis, Weizmann Institute of Science (Rehovot), December 2001.
- Gri (03), *Uniform asymptotic bound on the number of zeros of Abelian integrals*, ArXiv preprint math.DS/0305248 (2003).
- Hil (00) D. Hilbert, *Mathematical problems*, Bull. Amer. Math. Soc. (N.S.) 37 (2000), no. 4, 407–436, Reprinted from Bull. Amer. Math. Soc. 8 (1902), 437–479.
- (29) Yu. S. Ilyashenko, *Primer uravnenii vida d w / d z = − R z / R w dw/dz=-R_{z}/R_{w} imeyuwih schetnoe chislo predelp1nyh ciklov i skolp1 ugodno bolp1shoi zhanr po Petrovskomu–Landisu ( An example of equations d ​ w / d ​ z = P n ​ ( z, w) / Q n ​ ( z, w) dw/dz=P_{n}\,(z,\,w)/Q_{n}\,(z,\,w) having a countable number of limit cycles and arbitrarily high Petrovskiĭ-Landis genus)*, Mat. Sb. (N.S.) 80 (122) (1969), 388–404. MR0259239 (41 #3881)
- (30), *Vozniknovenie predelp1nyh ciklov pro vozmuwenii uravneniya d w / d z = − R z / R w dw/dz=-R_{z}/R_{w}, gde R ⁡ ( z, w) R(z,w) —mnogochlen ( Appearance of limit cycles by perturbation of the equation d w / d z = − R z / R w dw/dz=-R_{z}/R_{w}, where R ⁡ ( z, w) R(z,w) is a polynomial)*, Mat. Sbornik (New Series) 78 (120) (1969), no. 3, 360–373.
- Ily (78), *The multiplicity of limit cycles arising by a perturbation of a Hamilton equation of the class d ​ w / d ​ z = P 2 / Q 1 dw/dz=P_{2}/Q_{1}, in real and complex domains.*, Tr. Semin. Im. I.G. Petrovskogo 3 (1978), 49–60 (Russian).
- Ily (02), *Centennial history of Hilbert’s 16th problem*, Bull. Amer. Math. Soc. (N.S.) 39 (2002), no. 3, 301–354 (electronic). MR 1 898 209
- Ily (06), *The qualitative theory of differential equations in the plane*, Mathematical events of the twentieth century, Springer, Berlin, 2006, pp. 101–132. MR2182781 (2006i:34002)
- Ily (08) Yu. Ilyashenko, *Some open problems in real and complex dynamical systems*, Nonlinearity 21 (2008), T101–T107.
- IY (95) Yu. Ilyashenko and S. Yakovenko, *Double exponential estimate for the number of zeros of complete abelian integrals and rational envelopes of linear ordinary differential equations with an irreducible monodromy group*, Invent. Math. 121 (1995), no. 3, 613–650. MR 96g:58157
- IY (08), *Lectures on Analytic Differential Equations*, Graduate Studies in Mathematics, vol. 86, American Mathematical Society, Providence, RI, 2008. MR2363178
- JM (94) M. A. Jebrane and A. Mourtada, *Cyclicité finie des lacets doubles non triviaux*, Nonlinearity 7 (1994), no. 5, 1349–1365. MR1294547 (95h:58110)
- Kas (81) M. Kashiwara, *Quasi-unipotent constructible sheaves*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. 28 (1981), no. 3, 757–773 (1982). MR656052 (84f:32009)
- Kho (84) A. Khovanskiĭ, *Real analytic manifolds with the property of finiteness, and complex abelian integrals*, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 40–50. MR 86a:32024
- Kho (91), *Fewnomials*, American Mathematical Society, Providence, RI, 1991. MR 92h:14039
- Loo (74) E. Looijenga, *The complement of the bifurcation variety of a simple singularity*, Invent. Math. 23 (1974), 105–116. MR 54 #10661
- Mar (91) P. Mardešić, *An explicit bound for the multiplicity of zeros of generic Abelian integrals*, Nonlinearity 4 (1991), no. 3, 845–852. MR1124336 (92h:58163)
- Mil (68) J. Milnor, *Singular points of complex hypersurfaces*, Annals of Mathematics Studies, No. 61, Princeton University Press, Princeton, N.J., 1968. MR 39 #969
- Mou (03) C. Moura, *Bounds for the vanishing order for solutions of a linear differential system*, J. Dynam. Control Systems 9 (2003), no. 1, 73–88. MR 1956445
- Nov (01) D. Novikov, *Systems of linear ordinary differential equations with bounded coefficients may have very oscillating solutions*, Proc. Amer. Math. Soc. 129 (2001), no. 12, 3753–3755 (electronic). MR 1 860 513
- Nov (09), *On limit cycles appearing by polynomial perturbation of Darbouxian integrable systems*, Geom. Funct. Anal. 18 (2009), no. 5, 1750–1773. MR2481741
- NY (95) D. Novikov and S. Yakovenko, *Simple exponential estimate for the number of real zeros of complete Abelian integrals*, Ann. Inst. Fourier (Grenoble) 45 (1995), no. 4, 897–927. MR 97b:14053
- (48), *Tangential Hilbert problem for perturbations of hyperelliptic Hamiltonian systems*, Electron. Res. Announc. Amer. Math. Soc. 5 (1999), 55–65 (electronic). MR 2000a:34065
- (49), *Trajectories of polynomial vector fields and ascending chains of polynomial ideals*, Ann. Inst. Fourier (Grenoble) 49 (1999), no. 2, 563–609. MR 2001h:32054
- NY (01), *Redundant Picard-Fuchs system for Abelian integrals*, J. Differential Equations 177 (2001), no. 2, 267–306. MR 1 876 646
- NY (03), *Quasialgebraicity of Picard–Vessiot fields*, Mosc. Math. J. 3 (2003), no. 2, 551–591.
- Pet (90) G. S. Petrov, *Nonoscillation of elliptic integrals*, Funktsional. Anal. i Prilozhen. 24 (1990), no. 3, 45–50, 96. MR 92c:33036
- Pet (97), *On the nonoscillation of elliptic integrals*, Funktsional. Anal. i Prilozhen. 31 (1997), no. 4, 47–51, 95. MR 99a:34087
- PL (55) I. G. Petrovskiĭ and E. M. Landis, *On the number of limit cycles of the equation d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx={P}(x,y)/{Q}(x,y), where P {P} and Q {Q} are polynomials of 2nd degree*, Mat. Sb. N.S. 37(79) (1955), 209–250. MR 17,364d
- PL (57), *On the number of limit cycles of the equation d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx={P}(x,y)/{Q}(x,y), where P {P} and Q {Q} are polynomials*, Mat. Sb. N.S. 43(85) (1957), 149–168. MR 19,746c
- PL (59), *Corrections to the articles “On the number of limit cycles of the equations d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx={P}(x,\,y)/{Q}(x,\,y), where P {P} and Q {Q} are polynomials of 2 2 nd degree” and “On the number of limit cycles of the equation d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx={P}(x,\,y)/{Q}(x,\,y), where P {P} and Q {Q} are polynomials”*, Mat. Sb. (N.S.) 48 (90) (1959), 253–255. MR 23 #A1099
- Rou (86) R. Roussarie, *On the number of limit cycles which appear by perturbation of separatrix loop of planar vector fields*, Bol. Soc. Brasil. Mat. 17 (1986), no. 2, 67–101. MR 88i:34061
- Rou (89), *Cyclicité finie des lacets et des points cuspidaux*, Nonlinearity 2 (1989), no. 1, 73–117. MR980858 (90m:58169)
- RY (96) M. Roitman and S. Yakovenko, *On the number of zeros of analytic functions in a neighborhood of a Fuchsian singular point with real spectrum*, Math. Res. Lett. 3 (1996), no. 3, 359–371. MR 97d:34004
- Var (84) A. N. Varchenko, *Estimation of the number of zeros of an abelian integral depending on a parameter, and limit cycles*, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 14–25. MR 85g:32033
- Yak (84) S. Yakovenko, *Real zeros of a class of Abelian integrals arising in bifurcation theory*, Methods of the qualitative theory of differential equations (Russian), Gor ′ kov. Gos. Univ., Gorki, 1984, Translated in Selecta Math. Soviet. 9 (1990), no. 3, 255–262, pp. 175–185, 203–204. MR866699 (88b:58100)
- Yak (95), *A geometric proof of the Bautin theorem*, Concerning the Hilbert 16th problem, Amer. Math. Soc., Providence, RI, 1995, pp. 203–219. MR 96j:34056
- Yak (99), *On functions and curves defined by ordinary differential equations*, The Arnoldfest (Toronto, ON, 1997), Amer. Math. Soc., Providence, RI, 1999, pp. 497–525. MR 2001k:34065
- Yak (02), *Bounded decomposition in the Brieskorn lattice and Pfaffian Picard–Fuchs systems for Abelian integrals*, Bull. Sci. Math 126 (2002), no. 7, 535–554.
- Yak (05), *Quantitative theory of ordinary differential equations and the tangential Hilbert 16th problem*, On finiteness in differential equations and Diophantine geometry, CRM Monogr. Ser., vol. 24, Amer. Math. Soc., Providence, RI, 2005, pp. 41–109. MR2180125 (2006g:34062)
- Yak (06), *Oscillation of linear ordinary differential equations: on a theorem of A. Grigoriev*, J. Dyn. Control Syst. 12 (2006), no. 3, 433–449. MR2233029
- Żol (06) H. Żola̧dek, *The monodromy group*, Instytut Matematyczny Polskiej Akademii Nauk. Monografie Matematyczne (New Series) [Mathematics Institute of the Polish Academy of Sciences. Mathematical Monographs (New Series)], vol. 67, Birkhäuser Verlag, Basel, 2006. MR2216496


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:%7Bgal.binyamini,%E2%80%89dmitry.novikov,%E2%80%89sergei.yakovenko%7D@weizmann.ac.il
