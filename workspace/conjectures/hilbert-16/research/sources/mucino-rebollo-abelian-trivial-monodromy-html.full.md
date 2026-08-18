<!-- source: https://arxiv.org/html/2508.15925v1 | converted from HTML -->

Abelian integrals for polynomials with trivial global monodromy on C 2

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-NC-ND 4.0][2]

arXiv:2508.15925v1 [math.DS] 21 Aug 2025

# Abelian integrals for polynomials with trivial global monodromy on ℂ 2 \mathbb{C}^{2} Thanks: The second author is supported by Universidad del Bío-Bío Grant RE2320122

and

###### Abstract.

We consider infinitesimal perturbations of Hamiltonian differential equations d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 on the complex plane ℂ 2 \mathbb{C}^{2}, where H H is a polynomial of degree m + 1 m+1 and ω \omega is a non-exact polynomial 1-form of degree n n. In order to study these perturbed differential equations, the associated Abelian integrals I ⁡ ( c) = ∫ γ ⁡ ( c) ω I(c)=\int_{\gamma(c)}\omega are valuable tools. We assume that the polynomials H H are primitive with trivial global monodromy. For these polynomials, W. D. Neumann and P. Norbury provided a classification in three large families, up to algebraic equivalence. The knowledge of these families allows us to prove as first main result, that the respective Abelian integrals I ⁡ ( c) I(c) are polynomial functions of the variable c c, and to find sharp explicit upper bounds for the number of their zeros. The bounds depend on m m, n n and the number of the generators of the fundamental group of the generic fibers of H H. These upper bounds works for several new families of infinitesimal perturbations of Hamiltonian differential equations. Under trivial global monodromy, there exist canonical global generators B ​ C ​ ( H) = { γ 𝚒 ​ ( c) } BC(H)=\{\gamma_{\tt i}(c)\} of the fundamental groups for all the generic fibers of H H, which are complex cycles of d ​ H = 0 dH=0. As second main result; we compute the number of complex limit cycles of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 which originate from complex cycles in B ​ C ​ ( H) BC(H). Several accurate examples are provided.

###### Key words and phrases:

Abelian integrals, Weak infinitesimal Hilbert’s 16th problem, Limit cycles, Monodromy, Birational equivalence

###### 1991 Mathematics Subject Classification

Primary: 34M45; Secondary: 14K20, 32M25, 37F75

Jesús Muciño-Raymundo a, Salomón Rebollo-Perdomo b

a Centro de Ciencias Matemáticas, UNAM, Campus Morelia, Michoacán México,

muciray@matmor.unam.mx

b Departamento de Matemática, Universidad del Bío-Bío, Concepción, Chile.

srebollo@ubiobio.cl

## 1. Introduction

A complex polynomial function H H on ℂ 2 \mathbb{C}^{2} determines a Hamiltonian differential equation d ​ H = 0 dH=0. Given a complex polynomial 1-form ω \omega and ε ∈ ( ℂ, 0) \varepsilon\in(\mathbb{C},0), we consider the infinitesimal perturbation of the Hamiltonian differential equation

 | d ​ H + ε ​ ω = 0 on ​ ℂ 2. dH+\varepsilon\omega=0\ \ \hbox{ on }\ \mathbb{C}^{2}. |  | (1) |

We denote the bifurcation set of H H as 𝔅 ⁡ ( H) ⊂ ℂ \mathfrak{B}(H)\subset\mathbb{C} and throughout our work each c ∈ ℂ \ 𝔅 ⁡ ( H) {c\in\mathbb{C}\backslash\mathfrak{B}(H)} is a generic value of H H, that is the corresponding L c = { H ( u, v) = c } L_{c}=\{H(u,v)=c\} is a generic fiber of H H (a punctured Riemann surface). A *cycle of d ​ H = 0 dH=0*is a non-contractible closed loop γ ⁡ ( c) \gamma(c) in L c L_{c}. Moreover, recall that H H is *primitive*when its generic fibers L c L_{c} are connected. As usual for the study of Abelian integrals, let c 0 c_{0} be a generic value of H H and let γ ⁡ ( c 0) \gamma(c_{0}) be a cycle of d ​ H = 0 dH=0 in the generic fiber L c 0 L_{c_{0}}. The *Abelian integral*defined by H H, c 0 c_{0}, γ ⁡ ( c 0) \gamma(c_{0}) and ω \omega is the holomorphic function germ

 | I ⁡ ( c) = ∫ γ ⁡ ( c) ω: ( ℂ, c 0) ⟶ ℂ, I(c)=\int_{\gamma(c)}\omega\colon(\mathbb{C},c_{0})\longrightarrow\mathbb{C}, |  | (2) |

where γ ⁡ ( c) \gamma(c) is obtained from γ ⁡ ( c 0) \gamma(c_{0}) by local monodromy, that is, continuous transport of the cycle in the fibers of H H. Abusing the notation, we do not write explicitly the dependence on H H, c 0 c_{0}, γ ⁡ ( c 0) \gamma(c_{0}) and ω \omega in the notation of I ⁡ ( c) I(c).

From a dynamical point of view, the zeros of the integrals ( 2) are related to the bifurcation of limit cycles of equation ( 1). More precisely, recall that ( 1) is *a non-conservative perturbation of d ​ H = 0 dH=0*, when I ⁡ ( c) ≢ 0 I(c)\not\equiv 0. In this case, the well-known Poincaré–Pontryagin–Andronov criterion implies that the number of limit cycles of ( 1) generated from the cycles { γ ⁡ ( c) } \{\gamma(c)\} is bounded by the number of isolated zeros, counting multiplicities, of I ⁡ ( c) I(c), see [19, §26A]. Certainly, there are differential equations ( 1) with limit cycles generated from singular fibers of d ​ H = 0 dH=0 or generated from cycles of d ​ H = 0 dH=0, when I ⁡ ( c) I(c) vanishes identically; see for instance [20, 29, 30].

One of the most general results regarding the maximal number of isolated zeros of Abelian integrals has been achieved by G. Binyamini et al. [5], providing an explicit upper bound in terms of the maximum degree of H H and ω \omega, such upper bound is far from being optimal. This result is actually a strong approach towards a solution to the weak infinitesimal Hilbert’s 16th problem. See [1, 9, 14, 18, 19, 21, 22, 26, 32] and references therein for several aspects of this subject. Naturally, the richness of the weak infinitesimal Hilbert’s 16th problem suggests looking at particular families of polynomials H H, which could be accessible intermediate steps towards accurate upper bounds.

In this work, we consider the family of polynomials H H with trivial global monodromy, see for instance E. Artal-Bartolo *et al.*[3], A. Dimca [10], W. D. Neumann and P. Norbury [24], the accurate concept appears in Definition 3. We will focus on Abelian integrals ( 2) defined by this class of polynomials and their applications to the study of limit cycles of ( 1).

Our main result is as follows.

###### Theorem 1.

Let H H be a primitive polynomial on ℂ 2 \mathbb{C}^{2} with trivial global monodromy, of degree at most m + 1 m+1, suppose dim H 1 ​ ( L c, ℤ) = 𝔯 ≥ 1 \dim H_{1}(L_{c},\mathbb{Z})=\mathfrak{r}\geq 1, and let ω \omega be a polynomial 1-form of degree at most n n.

1. 1)

For each cycle γ ⁡ ( c 0) \gamma(c_{0}) of d ​ H = 0 dH=0 in a generic fiber L c 0 L_{c_{0}}, the Abelian integral ( 2) extends to a polynomial function on ℂ \mathbb{C},

 | I ⁡ ( c) = ∫ γ ⁡ ( c) ω: ℂ ⟶ ℂ. I(c)=\int_{\gamma(c)}\omega\colon\mathbb{C}\longrightarrow\mathbb{C}. |  | (3) |

2. 2)

The degree of I ⁡ ( c) I(c) is bounded from above by 𝒵 ⁡ ( m, n, 𝔯) \mathscr{Z}(m,n,\mathfrak{r}), where

 | 𝒵 ⁡ ( m, n, 𝔯) = { [n + 1 2] if m = 1, ( n + 1) ​ ( m − 1) − 1 if 2 ≤ m ≤ 8, ( ( n + 1) ​ [m − 𝔯 𝔯] − 1) ​ ( m − 𝔯 − 2) − 𝔯 + 1 if m ≥ 9. \mathscr{Z}(m,n,\mathfrak{r})=\begin{cases}\left[\dfrac{n+1}{2}\right]&\mbox{ if $\,m=1$},\\[14.0pt] (n+1)(m-1)-1&\mbox{ if $\,2\leq m\leq 8$,}\\[10.0pt] \left((n+1)\left[\dfrac{m-\mathfrak{r}}{\mathfrak{r}}\right]-1\right)\left(m-\mathfrak{r}-2\right)-\mathfrak{r}+1&\mbox{ if $\,m\geq 9$.}\end{cases} |  | (4) |

Recall that for H H with non-trivial global monodromy, the Abelian integral I ⁡ ( c) I(c) usually extends to a multivalued function on ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H). The significance of this theorem lies in the polynomial nature of the extension on ℂ \mathbb{C} of the Abelian integrals ( 2). Additionally, the theorem provides explicit upper bounds 𝒵 ⁡ ( m, n, 𝔯) \mathscr{Z}(m,n,\mathfrak{r}) for the degrees of the polynomial Abelian integrals, emphasizing the emergence of the homology dimension 𝔯 \mathfrak{r} of the generic fibers of the polynomial H H at these bounds.

The assumption of trivial global monodromy leads to a new landscape for the corresponding weak infinitesimal Hilbert’s 16th problem. We have the following advantages.

First, by a deep result of Neumann–Norbury [25], there exists a *canonical global generators of the fundamental groups π 1 ​ ( L c) \pi_{1}(L_{c}) for all the generic fibers L c L_{c} of H H*, say

 | B ​ C ​ ( H) ≐ { γ 𝚒 ​ ( c) | 1 ≤ 𝚒 ≤ 𝔯 ​ and ​ c ∈ ℂ \ 𝔅 ⁡ ( H) }. BC(H)\doteq\{\,\gamma_{\tt i}(c)\,|\ 1\leq{\tt i}\leq\mathfrak{r}\,\mbox{ and }\,c\in\mathbb{C}\backslash\mathfrak{B}(H)\}. |  | (5) |

The explicit construction of B ​ C ​ ( H) BC(H) is in Proposition 17. In holomorphic foliation theory language, each γ 𝚒 ​ ( c) \gamma_{\tt i}(c) in L c L_{c} is a complex cycle 1 1 1 From now on, we use complex cycle in order to emphasize that they are in the complex leaves of the foliation d ​ H = 0 dH=0. of d ​ H = 0 dH=0, see Definition 1.

Second, given a polynomial 1-form ω \omega, we consider the Abelian integrals

 | I 𝚒 ( c) ≐ ∫ γ 𝚒 ​ ( c) ω, for γ 𝚒 ​ ( c) ∈ B ​ C ​ ( H). I_{\tt i}(c)\doteq\int_{\gamma_{\tt i}(c)}\omega\,,\ \ \ \mbox{ for $\gamma_{\tt i}(c)\in BC(H)$. } |  | (6) |

We say that *ω \omega is non-conservative for B ​ C ​ ( H) BC(H)*, when all the Abelian integrals I 𝚒 ​ ( c) I_{\tt i}(c) in equation ( 6) are non-identically zero. Note that the set of non-conservative 1-forms of degree n n for B ​ C ​ ( H) BC(H) forms an open and dense set in the vector space of polynomial 1-forms of degree at most n n, see Lemma 20.

As a third advantage, each integral I ⁡ ( c) I(c) in Theorem 1 is a integer linear combination of the integrals I 𝚒 ​ ( c) I_{\tt i}(c).

Fourth (dynamical) advantage, for all 𝚒 {\tt i} and all c ∈ ℂ \ 𝔅 ⁡ ( H) c\in\mathbb{C}\backslash\mathfrak{B}(H)), we simultaneously study the complex limit cycles of d ​ H + ε ​ ω = 0 {dH+\varepsilon\omega=0} that are generated from the complex cycles in B ​ C ​ ( H) BC(H).

Summing up, under trivial global monodromy hypothesis for H H and considering ω \omega a non-conservative 1-form for B ​ C ​ ( H) BC(H), we will search for the following novel bounds.

- •

*Z ​ ( I 𝚒 ​ ( c)) Z(I_{\tt i}(c)) is the number of zeros of I 𝚒 ​ ( c) I_{\tt i}(c) in ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H)*, counted with multiplicities, and

- •

*𝒩 B ​ C ​ ( H) ​ ( ω) \mathscr{N}_{BC(H)}(\omega) is the number of complex limit cycles of d ​ H + ε ​ ω = 0 {dH+\varepsilon\omega=0} that are generated from the complex cycles in B ​ C ​ ( H) BC(H). *

Our second result is as follows.

###### Theorem 2.

Let H H be a primitive polynomial on ℂ 2 \mathbb{C}^{2} with trivial global monodromy, of degree at most m + 1 m+1, suppose dim H 1 ​ ( L c, ℤ) = 𝔯 ≥ 1 \dim H_{1}(L_{c},\mathbb{Z})=\mathfrak{r}\geq 1, and let ω \omega be a polynomial 1-form of degree at most n n, non-conservative for B ​ C ​ ( H) BC(H).

1. 1)

Then

 | Z ⁡ ( I 𝚒 ​ ( c)) ≤ 𝒵 ⁡ ( m, n, 𝔯). Z(I_{\tt i}(c))\leq\mathscr{Z}(m,n,\mathfrak{r}). |  | (7) |

2. 2)

By considering all the complex cycles in B ​ C ​ ( H) BC(H), we have

 | 𝒩 B ​ C ​ ( H) ​ ( ω) ≤ Z ⁡ ( I 1 ​ ( c)) + ⋯ + Z ⁡ ( I 𝔯 ​ ( c)) ≤ 𝔯 ​ 𝒵 ​ ( m, n, 𝔯) \mathscr{N}_{BC(H)}(\omega)\leq Z(I_{1}(c))+\cdots+Z(I_{\mathfrak{r}}(c))\leq\mathfrak{r}\,\mathscr{Z}(m,n,\mathfrak{r}) |  | (8) |

3. 3)

If μ \mu is the number of vanishing cycles of H H, then

 | 𝒩 B ​ C ​ ( H) ​ ( ω) ≤ 𝔯 ​ 𝒵 ​ ( m, n, 𝔯) − μ. \mathscr{N}_{BC(H)}(\omega)\leq\mathfrak{r}\,\mathscr{Z}(m,n,\mathfrak{r})-\mu. |  | (9) |

The novelty in our result lies in the use of the canonical global generators B ​ C ​ ( H) BC(H) of the fundamental groups for the generic fibers. As far as we know, only the harmonic oscillator was previously studied from an analogous point of view by I. Iliev [16].

In subsection 5.4, we illustrate the nature of the bounds Z ​ ( I 𝚒 ​ ( c)) Z(I_{\tt i}(c)) and 𝒩 B ​ C ​ ( H) ​ ( ω) \mathscr{N}_{BC(H)}(\omega) in equations ( 7) and ( 8). For certain infinitesimal perturbation of a Hamiltonian differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0, H H of degree 7 7, the generic fiber L c L_{c} is biholomorphic to a Riemann sphere punctured at four points. We consider canonical global generators B C ( H) = { γ 𝚒 ( c) | 𝚒 = 1, 2, 3 } BC(H)=\{\gamma_{\tt i}(c)\,|\,{\tt i}=1,\,2,\,3\} of the fundamental groups for all the generic fibers of H H, and a degree 3 3 non-conservative 1-form ω \omega for B ​ C ​ ( H) BC(H). The computation of I 𝚒 ​ ( c) I_{\tt i}(c) produces

 | deg ⁡ I 𝚒 ​ ( c) ≤ 7 < 𝒵 ⁡ ( 6, 3, 3) = 𝒵 ⁡ ( m, n, 𝔯), for 𝚒 = 1, 2, 3, \deg I_{\tt i}(c)\leq 7<\mathscr{Z}(6,3,3)=\mathscr{Z}(m,n,\mathfrak{r}),\mbox{ for ${\tt i}=1,\,2,\,3,$} |  |

and

 | 𝒩 B ​ C ​ ( H) ​ ( ω) = Z ⁡ ( I 1 ​ ( c)) + Z ⁡ ( I 2 ​ ( c)) + Z ⁡ ( I 3 ​ ( c)) = 6 + 7 + 2 = 15, \mathscr{N}_{BC(H)}(\omega)=Z(I_{1}(c))+Z(I_{2}(c))+Z(I_{3}(c))=6+7+2=15, |  |

see equation ( 80). Thus, there exist 15 complex cycles { γ 𝚒 ​ ( c j ⁡ ( 𝚒)) } \{\gamma_{\tt i}(c_{j({\tt i})})\} in different generic fibers { L c j ⁡ ( 𝚒) } \{L_{c_{j({\tt i})}}\}, where each complex cycle γ 𝚒 ​ ( c j ⁡ ( 𝚒)) \gamma_{\tt i}(c_{j({\tt i})}) generates a complex limit cycle under the perturbation. In our language; 15 is the number of complex limit cycles of d ​ H + ε ​ ω = 0 {dH+\varepsilon\omega=0} that are generated from the complex cycles in B ​ C ​ ( H) BC(H). Certainly, this quantity of complex limit cycles is just a lower bound for the number of complex limit cycles of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 generated from cycles in d ​ H = 0 dH=0; compare with Remark 9.

The approach of this work is constructive. In consequence, a Program for the study of Abelian integrals from polynomials with trivial global monodromy is in §3. Moreover, a large section § 5 of examples is provided. This methodology leads the proofs of the main results at the end of the work.

The work is organized as follows. In Section 2, we recall notations and definitions concerning our problem. As a novel aspect, we introduce the group of algebraic automorphisms Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}), this is a valuable tool for the study of Abelian integrals. As a contribution, the infinitesimal Hilbert’s 16th problem is invariant under algebraic automorphisms, see Corollary 5. This suggests we should study certain families of normal forms ℋ \mathcal{H} for polynomials H H under Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}), see §2.2. Thus, we change the study of the infinitesimal perturbation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 into the study of d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0, where ϑ \vartheta is the push-forward of ω \omega under the algebraic automorphism that transforms H H into its normal form ℋ \mathcal{H}. In order to prove our main results, in Section 3, we propose a Program, which consists of four steps. The first concerns the algebraic classification; to find the normal form ℋ \mathcal{H} of an original primitive polynomial with trivial global monodromy H H. In the second step, we regard a birational map ℛ \mathcal{R} which globally rectifies the Hamiltonian differential equation d ​ ℋ = 0 d\mathcal{H}=0, that allows us to perform a great simplification in our study. The third step recognizes the Abelian integrals for the infinitesimal perturbation of the rectified differential equation. We present an invariance of Abelian integrals under the birational map ℛ \mathcal{R}, see Corollary 15 for complete details. Finally, as a fourth step we compute the Abelian integral ( 2) on the rectified foliation and by using the residue theorem at the punctures. In Section 4, we recall the Neumann–Norbury classification, which provides three families of normal forms ℋ \mathcal{H} of primitive polynomials with trivial global monodromy, as well as a result that controls the degree of the transformed objects ℋ \mathcal{H} and ϑ \vartheta under algebraic equivalence. We give an accurate description of the rectifying maps ℛ \mathcal{R} for the normal form polynomials, which allows us to prove the rational invariance of the infinitesimal Hilbert’s 16th problem. In Proposition 17, we construct canonical global generators of the fundamental groups π 1 ​ ( L c) \pi_{1}(L_{c}) for all the generic fibers of H H, that is B ​ C ​ ( H) BC(H) in ( 5). It allow us to reduce the study of the Abelian integral ( 2) to a integer linear combination of canonical Abelian integrals I 𝚒 ​ ( c) I_{\tt i}(c). In Section 5, we introduce some characteristic examples of the application of our Program. In Section 6, we study the properties of the Abelian integrals defined by the normal form for polynomials with trivial global monodromy. The proofs of Theorems 1 and 2 are given in Section 7.

## 2. Generalities, algebraic equivalence and normal forms

### 2.1. Notations and definitions.

As usual, ℂ ⁡ [u, v] \mathbb{C}[u,v] denotes the vector space of complex polynomials and Ω 1 ​ ( ℂ 2) \varOmega^{1}(\mathbb{C}^{2}) is the vector space of polynomial 1-forms on ℂ 2 \mathbb{C}^{2}.

Because of a classical result of R. Thom [31], given a polynomial H ⁡ ( u, v) H(u,v) its bifurcation set (critical value set) is

 | 𝔅 ⁡ ( H) = 𝔅 f ​ i ​ n ​ ( H) ∪ 𝔅 i ​ n ​ f ​ ( H) ⊂ ℂ. \mathfrak{B}(H)=\mathfrak{B}_{fin}(H)\cup\mathfrak{B}_{inf}(H)\subset\mathbb{C}. |  | (10) |

This includes the subset of finite critical values 𝔅 f ​ i ​ n ​ ( H) \mathfrak{B}_{fin}(H) from critical points in ℂ 2 \mathbb{C}^{2}, as well as the critical values at infinity 𝔅 i ​ n ​ f ​ ( H) \mathfrak{B}_{inf}(H) corresponding to the critical points in the line at infinity. This second subset arises from the extension of H H as a rational function on ℂ 2 ∪ ℂ ​ ℙ ∞ 1 \mathbb{C}^{2}\cup\mathbb{CP}^{1}_{\infty}, see [11]. The map

 | H: ℂ 2 \ H − 1 ​ ( 𝔅 ⁡ ( H)) ⟶ ℂ \ 𝔅 ⁡ ( H) H\colon\mathbb{C}^{2}\backslash H^{-1}(\mathfrak{B}(H))\longrightarrow\mathbb{C}\backslash\mathfrak{B}(H) |  | (11) |

is a locally trivial smooth fibration, see [6, 15]. By definition, c ∈ ℂ \ 𝔅 ⁡ ( H) c\in\mathbb{C}\backslash\mathfrak{B}(H) is a generic value of H H and the associated affine non-singular algebraic curve

 | L c ≐ { H ( u, v) = c } ⊂ ℂ 2 L_{c}\doteq\left\{H(u,v)=c\right\}\subset\mathbb{C}^{2} |  |

is a generic fiber of H H. Moreover, a polynomial H H is *primitive of type*( g, κ) (g,\kappa) when its generic fibers { L c } \{L_{c}\} are irreducible and homeomorphic to a compact Riemann surface of genus g ≥ 0 g\geq 0 which is punctured at κ ≥ 1 \kappa\geq 1 points. In that case, the first homology group H 1 ​ ( L c, ℤ) H_{1}(L_{c},\mathbb{Z}) of any generic fiber L c L_{c} of H H is a free Abelian group of dimension 𝔯 = 2 ​ g + κ − 1 \mathfrak{r}=2g+\kappa-1.

Let H H be a primitive polynomial of type ( g, κ) (g,\kappa) and let ω ∈ Ω 1 ​ ( ℂ 2) \omega\in\varOmega^{1}(\mathbb{C}^{2}) be a complex polynomial 1-form. We consider c 0 ∈ ℂ \ 𝔅 ⁡ ( H) c_{0}\in\mathbb{C}\backslash\mathfrak{B}(H) a generic value of H H and a homotopy cycle γ ⁡ ( c 0) \gamma(c_{0}) of d ​ H = 0 dH=0 in a generic fiber L c 0 L_{c_{0}}. On the one hand, if 𝔻 ⁡ ( c 0, ρ) ⊂ ℂ \ 𝔅 ⁡ ( H) \mathbb{D}(c_{0},\rho)\subset\mathbb{C}\backslash\mathfrak{B}(H) is an open disk of generic values of H H, with center c 0 c_{0} and radius ρ \rho, then γ ⁡ ( c 0) \gamma(c_{0}) can be continuously transported, by using the fibration ( 11) into a unique cycle γ ⁡ ( c) \gamma(c) of d ​ H = 0 dH=0 in L c L_{c} for each c ∈ D ⁡ ( c 0, ρ) c\in D(c_{0},\rho). Thus, the *Abelian integral defined by H H, c 0 c_{0}, γ ⁡ ( c 0) \gamma(c_{0}) and ω \omega*is a holomorphic function germ

 | I ⁡ ( c) = ∫ γ ⁡ ( c) ω, I(c)=\int_{\gamma(c)}\omega, |  |

as in ( 2). For sake of simplicity, we will refer to I ⁡ ( c) I(c) only as an Abelian integral defined by H H and ω \omega.

Let us recall from a dynamical point of view that the study of the zeros of the integrals ( 2) is related to the bifurcation of limit cycles of the infinitesimal perturbation of the Hamiltonian differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0, see ( 1). Indeed, we know that for each ε ∈ ( ℂ, 0) \varepsilon\in(\mathbb{C},0), the differential equation (1) defines a 1-dimensional singular holomorphic foliation ℱ ε \mathcal{F}_{\varepsilon} on ℂ 2 × { ε } \mathbb{C}^{2}\times\{\varepsilon\}.

###### Definition 1 ( [19, §28C]).

A *complex cycle*of the differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 is a free homotopy class [γ] [\gamma] of a cycle γ \gamma in a leaf of the associated singular holomorphic foliation ℱ ε \mathcal{F}_{\varepsilon}. A *complex limit cycle*of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 is a complex cycle with a holonomy (first return) map different from the identity. By simplicity, a complex cycle is denoted by its representative γ \gamma.

In general, the differential equation ( 1), with ε ≠ 0 \varepsilon\neq 0, could have infinitely many complex limit cycles [19, Theorem 28.13], but here we will focus on complex limit cycles that are generated from the complex cycles { γ ⁡ ( c) | c ∈ D ⁡ ( c 0, ρ) } \{\gamma(c)\,|\,c\in D(c_{0},\rho)\} of d ​ H = 0 dH=0; the precise concept is as follows.

###### Definition 2 ( [17, pp. 356-357]).

A *complex cycle γ ⁡ ( c 0) \gamma(c_{0}) of d ​ H = 0 dH=0 generates a complex limit cycle of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0*when there exists a continuous family of complex limit cycles { γ ​ ( c 0 ​ ( ε)) } \{\gamma(c_{0}(\varepsilon))\} of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0, parametrized by ε ∈ ( ℂ, 0) \ { 0 } \varepsilon\in(\mathbb{C},0)\backslash\{0\}, such that { γ ​ ( c 0 ​ ( ε)) } \{\gamma(c_{0}(\varepsilon))\} tend to γ ⁡ ( c 0) \gamma(c_{0}) when ε → 0 \varepsilon\to 0.

In that case, every γ ​ ( c 0 ​ ( ε)) \gamma(c_{0}(\varepsilon)) for ε ≠ 0 \varepsilon\neq 0 is a *complex limit cycle of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 generated from γ ⁡ ( c 0) \gamma(c_{0}) of d ​ H = 0 dH=0*.

In general, the number complex limit cycles of a non-conservative perturbation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 that are generated from the complex cycles { γ ⁡ ( c) | c ∈ D ⁡ ( c 0, ρ) } \{\gamma(c)\,|\,c\in D(c_{0},\rho)\} of d ​ H = 0 dH=0 is bounded from above by the number of zeros of I ⁡ ( c) I(c). Very roughly speaking, this is the content of the Poincaré–Pontryagin–Andronov criterion, see [19, Proposition 26.1], [27, §3]. For our proposes, we use a classical version of Yu. Ilyashenko.

###### Lemma 3 (A sufficient condition for origin of a complex limit cycle, [17, pp. 356-357]).

Assume that c 0 ∈ ℂ \ 𝔅 ⁡ ( H) c_{0}\in\mathbb{C}\backslash\mathfrak{B}(H) is an isolated zero of the Abelian integral I ⁡ ( c) = ∫ γ ⁡ ( c) ω I(c)=\int_{\gamma(c)}\omega as in ( 2), *i.e.*

 | I ⁡ ( c) ≢ 0 and I ⁡ ( c 0) = 0, I(c)\not\equiv 0\quad\mbox{and}\quad I(c_{0})=0, |  |

then the complex cycle γ ⁡ ( c 0) \gamma(c_{0}) of d ​ H = 0 dH=0 generates at least a complex limit cycle of the non-conservative perturbation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0. □ \Box

A more accurate local result in c c is as follows.

###### Proposition 4 ( [19, Proposition 26.1]).

Assume that I ⁡ ( c) I(c) has N N isolated zeros (counted with multiplicities) in a closed disc D ⁡ ( c 0, ρ) ⊂ ℂ \ 𝔅 ⁡ ( H) D(c_{0},\rho)\subset\mathbb{C}\backslash\mathfrak{B}(H), then there exists ε 0 ≠ 0 \varepsilon_{0}\neq 0 such that for every ε ∈ D ⁡ ( 0, | ε 0 |) \varepsilon\in D(0,|\varepsilon_{0}|) the differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 has no more than N N complex limit cycles generated from the complex cycles { γ ⁡ ( c) | c ∈ D ⁡ ( c 0, ρ) } \{\gamma(c)\,|\,c\in D(c_{0},\rho)\}. □ \Box

This means that the number of complex limit cycles of d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0, up to first order in ε \varepsilon, that are generated from complex cycles of d ​ H = 0 dH=0 is bounded from above by the number zeros (counted with multiplicities) of I ⁡ ( c) I(c).

Concerning the study of Abelian integrals, a main ingredient is the monodromy group of a polynomial H H, see for the general case [2, Ch. 1]. If α: [0, 1] → ℂ \ 𝔅 H \alpha:[0,1]\to\mathbb{C}\backslash\mathfrak{B}_{H} is a path with initial point c 0 = α ⁡ ( 0) c_{0}=\alpha(0) and end point c 1 = α ⁡ ( 1) c_{1}=\alpha(1), which are generic values of H H, then there exists a diffeomorphism from the fiber L c 0 L_{c_{0}} into the fiber L c 1 L_{c_{1}}. In particular, each non null-homotopic loop α \alpha based on c 0 c_{0} induces a diffeomorphism

 | h α: L c 0 ⟶ L c 0 h_{\alpha}:L_{c_{0}}\longrightarrow L_{c_{0}} |  |

called monodromy of the loop α. \alpha. In addition, the action h α ∗ h_{\alpha*} on the homology of L c 0 L_{c_{0}} associeted to h α h_{\alpha}, is the *monodromy operator of α \alpha*, we have a group automorphism

 | h α ∗: H 1 ( L c 0, ℤ) ⟶ H 1 ( L c 0, ℤ). h_{\alpha*}:H_{1}(L_{c_{0}},\mathbb{Z})\longrightarrow H_{1}(L_{c_{0}},\mathbb{Z}). |  |

If α \alpha and α ′ \alpha^{\prime} are homotopic loops based on c 0 c_{0}, then h α ∗ = h α ′ ∗ h_{\alpha*}=h_{\alpha^{\prime}*}. Hence, there exists a group homomorphism from the fundamental group π 1 ​ ( ℂ \ 𝔅 H, c 0) \pi_{1}(\mathbb{C}\backslash\mathfrak{B}_{H},c_{0}) to the group of automorphisms Aut ⁡ ( H 1 ​ ( L c 0, ℤ)) {\mathrm{Aut}}(H_{1}(L_{c_{0}},\mathbb{Z})) of H 1 ​ ( L c 0, ℤ) H_{1}(L_{c_{0}},\mathbb{Z}), say

 | ℳ H: π 1 ​ ( ℂ \ 𝔅 H, c 0) ⟶ Aut ⁡ ( H 1 ​ ( L c 0, ℤ)) [α] ⟼ h α ∗. \begin{array}[]{rcl}\mathcal{M}_{H}:\pi_{1}\left(\mathbb{C}\backslash\mathfrak{B}_{H},c_{0}\right)&\longrightarrow&{\mathrm{Aut}}(H_{1}(L_{c_{0}},\mathbb{Z}))\\ \left[\alpha\right]&\longmapsto&h_{\alpha*}\end{array}. |  |

The *monodromy group of H H*is the image of the homeomorphism ℳ H \mathcal{M}_{H}.

###### Remark 1.

In general, by using the monodromy ℳ H \mathcal{M}_{H} the Abelian integral I 𝚒 ​ ( c) I_{\tt i}(c) extends to ℂ \ 𝔅 H \mathbb{C}\backslash\mathfrak{B}_{H} as a multivalued holomorphic function.

###### Definition 3 ( [10, 3, 24]).

A polynomial H H has *trivial global monodromy*when its monodromy group is the identity automorphism in Aut ⁡ ( H 1 ​ ( L c 0, ℤ)) {\mathrm{Aut}}(H_{1}(L_{c_{0}},\mathbb{Z})).

We recall that two complex polynomials H, ℋ ∈ ℂ ⁡ [u, v] H,\mathcal{H}\in\mathbb{C}[u,v] are algebraically equivalent or ( ψ, σ) ∗ (\psi,\sigma)_{*} -equivalent if there are polynomial automorphisms ψ ∈ Aut ⁡ ( ℂ 2) \psi\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2}) and σ ∈ Aut ⁡ ( ℂ) \sigma\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) such that

 | ℋ = σ ∘ H ∘ ψ − 1. \mathcal{H}=\sigma\circ H\circ\psi^{-1}. |  | (12) |

Moreover, we convene the notation

 | σ: ℂ ⟶ ℂ, c ⟼ 𝔠. \sigma:\mathbb{C}\longrightarrow\mathbb{C},\ \ \ c\longmapsto\mathfrak{c}\,. |  | (13) |

Additionally, we say that two complex polynomial 1-forms ω, ϑ ∈ Ω 1 ​ ( ℂ 2) \omega,\vartheta\in\varOmega^{1}(\mathbb{C}^{2}) are algebraically equivalent when

 | ϑ = σ ′ ​ ψ ∗ ​ ( ω), \vartheta=\sigma^{\prime}\psi_{*}(\omega), |  | (14) |

where σ ′ ∈ ℂ ∗ \sigma^{\prime}\in\mathbb{C}^{*} is the derivative of the affine map σ \sigma.

###### Remark 2.

1. Equation ( 12) says that the group Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) = { ( ψ, σ) } \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C})=\{(\psi,\sigma)\} of polynomial automorphisms acts on the space of polynomials as

 | ℂ ⁡ [u, v] × Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) {\lx@inpgf@ignorespaces{\mathbb{C}[u,v]\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C})}} ℂ ⁡ [u, v] {\lx@inpgf@ignorespaces\mathbb{C}[u,v]} ( H, ( ψ, σ)) {\lx@inpgf@ignorespaces\big(H,(\psi,\sigma)\big)} ℋ = σ ∘ H ∘ ψ − 1. {\lx@inpgf@ignorespaces\mathcal{H}=\sigma\circ H\circ\psi^{-1}.} |  |

Thus, each orbit of this action is a family of algebraically equivalent polynomials.

2. Trivial global monodromy is an algebraic invariant property of polynomials in ℂ ⁡ [u, v] \mathbb{C}[u,v].

3. If H H and ℋ \mathcal{H} are algebraically equivalent, then dim H 1 ​ ( L c, ℤ) = dim H 1 ​ ( ℒ 𝔠, ℤ) \dim H_{1}(L_{c},\mathbb{Z})=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z}).

4. Since we must look at generic and critical values of H H or ℋ \mathcal{H}, the convention ( 13) will be useful. In fact, and 𝔅 ⁡ ( ℋ) = σ ⁡ ( 𝔅 ⁡ ( H)) \mathfrak{B}(\mathcal{H})=\sigma(\mathfrak{B}(H)).

### 2.2. Algebraic invariance of the infinitesimal Hilbert’s 16th problem

Let H H and ℋ \mathcal{H} be two algebraically equivalent polynomials as in equation ( 12). Consider a complex polynomial 1-form ω \omega and its algebraically equivalent polynomial 1-form ϑ = σ ′ ​ ψ ∗ ​ ( ω), \vartheta=\sigma^{\prime}\psi_{*}(\omega), as in ( 14). Therefore, equations ( 12)–( 14) allow us to transform the holomorphic germ of the Abelian integral ( 2) into the holomorphic germ

 | ℐ ⁡ ( 𝔠) = ∫ δ ⁡ ( 𝔠) ϑ: ( ℂ, 𝔠 0) ⟶ ℂ, 𝔠 0 = σ ⁡ ( c 0), δ ⁡ ( 𝔠) = ψ ⁡ ( γ ⁡ ( σ − 1 ​ ( 𝔠))). \mathcal{I}(\mathfrak{c})=\displaystyle\int_{\delta(\mathfrak{c})}\vartheta:(\mathbb{C},\mathfrak{c}_{0})\longrightarrow\mathbb{C},\ \ \ \mathfrak{c}_{0}=\sigma(c_{0}),\ \delta(\mathfrak{c})=\psi\big(\gamma(\sigma^{-1}(\mathfrak{c}))\big). |  | (15) |

These algebraic equivalences imply the following result.

###### Corollary 5 (Algebraic invariance of the infinitesimal Hilbert’s 16th problem).

Let H, ℋ ∈ ℂ ⁡ [u, v] H,\mathcal{H}\in\mathbb{C}[u,v] be polynomials as in equation ( 12), and let ω, ϑ ∈ Ω 1 ​ ( ℂ 2) \omega,\vartheta\in\varOmega^{1}(\mathbb{C}^{2}) be polynomial 1-forms as in equation ( 14): algebraic equivalent objects in both cases.

1. 1)

The corresponding infinitesimal perturbed Hamiltonian differential equations are algebraically equivalent 2 2 2 Our equivalence is of 1-forms, which obviously implies the equivalence of the associated differential equations and their singular holomorphic foliations., that is,

 | σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω) = d ​ ℋ + ε ​ ϑ. \sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)=d\mathcal{H}+\varepsilon\vartheta. |  |

2. 2)

The Abelian integrals I ⁡ ( c) I(c) and ℐ ⁡ ( 𝔠) \mathcal{I}(\mathfrak{c}) are algebraically equivalent, that is,

 | I ⁡ ( c) = 1 σ ′ ​ ℐ ​ ( σ ⁡ ( c)), denoted as ​ ( ψ, σ) ∗ ​ I = ℐ, \ \ \ \ \ I(c)=\frac{1}{\sigma^{\prime}}\mathcal{I}(\sigma(c)),\ \ \ \hbox{ denoted as }(\psi,\sigma)_{*}I=\mathcal{I}, |  |

even if they are multivalued functions.

3. 3)

The cardinality of the zeros (counted with multiplicities) of I ⁡ ( c) I(c) in ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H) and of ℐ ⁡ ( 𝔠) \mathcal{I}(\mathfrak{c}) in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}) coincide. In particular, if H H has trivial global monodromy, then

 | Z ⁡ ( I 𝚒 ​ ( c)) = Z ⁡ ( ℐ 𝚒 ​ ( 𝔠)) a ​ n ​ d 𝒩 B ​ C ​ ( H) ​ ( ω) = 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ). Z(I_{\tt i}(c))=Z(\mathcal{I}_{\tt i}(\mathfrak{c}))\quad\quad{and}\quad\mathscr{N}_{BC(H)}(\omega)=\mathscr{N}_{BC(\mathcal{H})}(\vartheta). |  |

###### Proof.

Assertion 1) requires the accurate factor σ ′ \sigma^{\prime} in equation ( 14). Assertions OPEN 2) 2) and OPEN 3) 3) are straightforward. ∎

### 2.3. Normal forms of Hamiltonians with respect to the degree

In order to simplify the study of the infinitesimal Hilbert’s 16th problem, clearly, Corollary 5 suggests searching for a normal form for H ⁡ ( u, v) H(u,v) up to algebraic equivalence and with the property of minimal degree.

###### Lemma 6.

Let H ⁡ ( u, v) H(u,v) be a polynomial and let

 | { σ ∘ H ∘ ψ − 1 | ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) } ⊂ ℂ ⁡ [u, v] \left\{\sigma\circ H\circ\psi^{-1}\ |\ (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C})\right\}\subset\mathbb{C}[u,v] |  |

be its Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) -orbit. A minimum degree is reached in the orbit, that is, there exists a non-unique polynomial ℋ \mathcal{H} in the orbit such that

 | deg ⁡ ( ℋ) ≤ deg ⁡ ( σ ∘ H ∘ ψ − 1). \deg\left(\mathcal{H}\right)\leq\deg\big(\sigma\circ H\circ\psi^{-1}\big). |  |

###### Proof.

In [33, pp. 357-358], P. G. Wightwick studied the behaviour of the degree of polynomials H ∈ ℂ ⁡ [u, v] H\in\mathbb{C}[u,v] under Aut ⁡ ( ℂ 2) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2}). For each H H, Wightwick constructs an algorithm that depends on a finite numbers of choices that reduce the degree. Necessarily, the suitable choices produce the required ℋ \mathcal{H}. The polynomial ℋ \mathcal{H} is not unique, since under the actions of the affine groups Aff ⁡ ( ℂ 2) \mathop{\mbox{Aff}}\nolimits(\mathbb{C}^{2}) and Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}) the degree of ℋ \mathcal{H} remains constant. ∎

By abusing the language, we convene the next concept.

###### Definition 4.

Let H ⁡ ( u, v) H(u,v) be a polynomial and its Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) -orbit. A *normal form*of H ⁡ ( u, v) H(u,v) is a minimal degree polynomial, denoted by ℋ ⁡ ( x, y) \mathcal{H}(x,y), in this orbit.

###### Remark 3.

In all that follows, we reserve variables ( x, y) (x,y) for a normal form ℋ ⁡ ( x, y) \mathcal{H}(x,y) of H ⁡ ( u, v) H(u,v) and use subscripts for ψ \psi in equation ( 12); that is,

 | ψ: ℂ u ​ v 2 ⟶ ℂ x ​ y 2. \psi:\mathbb{C}^{2}_{u\,v}\longrightarrow\mathbb{C}^{2}_{x\,y}. |  |

It will be appropriate for our study of Abelian integrals.

If for a family of polynomials, say { H } ⊂ ℂ ⁡ [u, v] \{H\}\subset\mathbb{C}[u,v], their normal forms can be found, then the properties and bounds of the number of zeros of the Abelian integrals of the family could be probably stated in a simpler way. In this scenario, however, two main difficulties appear:

- D.1

The algebraic classification of polynomials H ∈ ℂ ⁡ [u, v] H\in\mathbb{C}[u,v] is a difficult and challenging open problem, for example J. Fernández de Bobadilla [12].

- D.2

The degrees of H H and ω \omega are not invariant under polynomial automorphisms.

In order to analyze difficulty D.2, we will denote by ℂ ​ [u, v] ≤ m \mathbb{C}[u,v]_{\leq m} the vector spaces of complex polynomials of degree at most m m and the vector space of polynomial 1 1 -forms on ℂ u ​ v 2 \mathbb{C}^{2}_{u\,v} of degree at most n n by

 | Ω 1 ( ℂ u ​ v 2) ≤ n ≐ { ω = A d u + B d v | A, B ∈ ℂ [u, v] ≤ n }. \varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}\doteq\left\{\omega=Adu+Bdv\,|\,A,B\in\mathbb{C}[u,v]_{\leq n}\right\}. |  |

In accordance with the Introduction § 1, we consider

 | H ∈ ℂ ​ [u, v] ≤ m + 1 and ω ∈ Ω 1 ​ ( ℂ u ​ v 2) ≤ n. H\in\mathbb{C}[u,v]_{\leq m+1}\quad\mbox{and}\quad\omega\in\varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}. |  | (16) |

Let ℋ \mathcal{H} be a normal form of H H through ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) and let ϑ = σ ′ ​ ψ ∗ ​ ( ω) \vartheta=\sigma^{\prime}\psi_{*}(\omega) be the associated 1-form. From Definition 4, we have

 | 𝔪 + 1 ≐ deg ⁡ ( ℋ) ≤ deg ⁡ ( H) ≤ m + 1. \mathfrak{m}+1\doteq\deg(\mathcal{H})\leq\deg(H)\leq m+1. |  | (17) |

By definition of ϑ \vartheta and the fact deg ⁡ ( ψ − 1) ≤ deg ⁡ ( ψ) \deg(\psi^{-1})\leq\deg(\psi), as seen in [7], we obtain

 | 𝔫 ≐ deg ⁡ ( ϑ) ≤ ( n + 1) ​ deg ⁡ ( ψ − 1) − 1 ≤ ( n + 1) ​ deg ⁡ ( ψ) − 1. \mathfrak{n}\doteq\deg(\vartheta)\leq(n+1)\deg(\psi^{-1})-1\leq(n+1)\deg(\psi)-1. |  |

The degree of ϑ \vartheta could be greater than the degree of ω \omega, since it depends on the degree of the polynomial automorphism ψ \psi. As an advantage, such a degree could be bound. Indeed, from [12, Proposition 4.17] we know that

 | deg ⁡ ( ψ) ≤ ( m + 1)! ( 𝔪)!. \deg(\psi)\leq\frac{(m+1)!}{(\mathfrak{m})!}. |  |

Thus,

 | 𝔫 = deg ⁡ ( ϑ) ≤ ( n + 1) ​ deg ⁡ ( ψ) − 1 ≤ ( n + 1) ​ ( m + 1)! ( 𝔪)! − 1. \mathfrak{n}=\deg(\vartheta)\leq(n+1)\deg(\psi)-1\leq(n+1)\frac{(m+1)!}{(\mathfrak{m})!}-1. |  | (18) |

Hence, equations ( 17) and ( 18) imply that the set of all ϑ \vartheta coming from Ω 1 ​ ( ℂ u ​ v 2) ≤ n \varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n} through the pairs ( ψ, σ) (\psi,\sigma) is a subset of Ω 1 ​ ( ℂ x ​ y 2) ≤ ( n + 1) ​ ( m + 1)! − 1 \varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq(n+1)(m+1)!-1}. Thus, although the degrees of the original objects H H and ω \omega are not invariant, the degrees of the transformed objects ℋ \mathcal{H} and ϑ \vartheta are well understood.

###### Lemma 7.

Consider H ∈ ℂ ​ [u, v] ≤ m + 1 H\in\mathbb{C}[u,v]_{\leq m+1} and ω ∈ Ω 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}. If ℋ \mathcal{H} is a normal form of H H under ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) and ϑ = σ ′ ​ ψ ∗ ​ ( ω) \vartheta=\sigma^{\prime}\psi_{*}(\omega), then

 | deg ⁡ ( ℋ) ≤ m + 1 and deg ⁡ ( ϑ) ≤ ( n + 1) ​ ( m + 1)! − 1. \deg(\mathcal{H})\leq m+1\quad\mbox{and}\quad\deg(\vartheta)\leq(n+1)(m+1)!-1. |  |

□ \Box

By considering the aforementioned, we have the following result.

###### Proposition 8.

Consider a primitive polynomial H ∈ ℂ ​ [u, v] ≤ m + 1 H\in\mathbb{C}[u,v]_{\leq m+1} and a polynomial 1-form ω ∈ Ω 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}. Then

 | { maximal number of zeros of ​ I ​ ( c) = ∫ γ ⁡ ( c) ω } ≤ { maximal number of zeros of ​ ℐ ​ ( 𝔠) = ∫ δ ⁡ ( 𝔠) ϑ }, \begin{array}[]{rcl}\left\{\begin{array}[]{c}{\hbox{\it maximal number of}}\\ {\hbox{\it zeros of}}\ I(c)=\int_{\gamma(c)}\omega\end{array}\right\}&\leq&\left\{\begin{array}[]{c}{\hbox{\it maximal number of}}\\ {\hbox{\it zeros of }}\mathcal{I}(\mathfrak{c})=\int_{\delta(\mathfrak{c})}\vartheta\end{array}\right\},\end{array} |  |

where the right-hand side considers a normal form ℋ ∈ ℂ ​ [x, y] ≤ 𝔪 + 1 \mathcal{H}\in\mathbb{C}[x,y]_{\leq\mathfrak{m}+1} of H H and all polynomial 1-forms ϑ ∈ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, with 𝔪 = m \mathfrak{m}=m and 𝔫 = ( n + 1) ​ ( m + 1)! − 1 \mathfrak{n}=(n+1)(m+1)!-1. □ \Box

In simple words, for each pair ( m, n) ∈ ℕ × ℕ (m,n)\in\mathbb{N}\times\mathbb{N} and by considering only Abelian integrals in ( 2), defined by primitive polynomials in normal form ℋ \mathcal{H} of degree at most m + 1 m+1 and polynomial 1-forms of degree at most ( n + 1) ​ ( m + 1)! − 1 (n+1)(m+1)!-1; we can always obtain an estimation from above for the maximal number of zeros of the Abelian integrals defined by primitive polynomials H ∈ ℂ ​ [u, v] ≤ m + 1 H\in\mathbb{C}[u,v]_{\leq m+1} and polynomial 1-forms ω ∈ Ω 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}.

Moreover, looking at the family of primitive polynomials with trivial global monodromy, we will have explicit normal forms; see the next two sections.

## 3. The Program

In this work, we restrict ourselves to primitive polynomials H ⁡ ( u, v) H(u,v) with trivial global monodromy. A cornerstone result behind our assertions is due to Neumann and Norbury [25], see Theorem 10 in Section 4. Very roughly speaking, these authors provide us with the following two key facts.

- i)

Each primitive polynomial with trivial global monodromy H ⁡ ( u, v) H(u,v) on ℂ u ​ v 2 \mathbb{C}^{2}_{u\,v} has an explicit normal form polynomial ℋ ⁡ ( x, y) \mathcal{H}(x,y) on ℂ x ​ y 2 \mathbb{C}^{2}_{x\,y} according to Definition 4.

- ii)

Moreover, each normal form polynomial ℋ ⁡ ( x, y) \mathcal{H}(x,y) admits a birational map

 | ℛ: ℂ x ​ y 2 ⟶ ℂ t ​ 𝔠 2 \mathcal{R}:\mathbb{C}^{2}_{x\,y}\longrightarrow\mathbb{C}^{2}_{t\,\mathfrak{c}} |  | (19) |

that sends the generic fibers of ℋ \mathcal{H} into punctured horizontal lines in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}.

Thus, ℛ \mathcal{R} is a rectifying map for ℋ \mathcal{H} and 𝔠 \mathfrak{c} coincides with equation ( 13) according to ℋ ∘ ℛ − 1 ​ ( t, 𝔠) = 𝔠 \mathcal{H}\circ\mathcal{R}^{-1}(t,\mathfrak{c})=\mathfrak{c}. Each map ℛ \mathcal{R} transforms polynomials, 1-forms and differential equations under push-forward denoted as ℛ ∗ \mathcal{R}_{*}. We say that it induces an ℛ \mathcal{R} –equivalence.

As an advantage for studying the Abelian integrals ( 6) and for proving Theorem 1, we propose the following Program.

Let H H be a primitive polynomial on ℂ 2 \mathbb{C}^{2} with trivial global monodromy, of degree at most m + 1 m+1, suppose dim H 1 ​ ( L c, ℤ) = 𝔯 ≥ 1 \dim H_{1}(L_{c},\mathbb{Z})=\mathfrak{r}\geq 1, and let ω \omega be a polynomial 1-form of degree at most n n.

1. Step 1.

According to Corollary 5, a suitable pair ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) allows us to transform the original polynomial differential equation ( 1) into a differential equation

 | d ​ ℋ + ε ​ ϑ = 0 on ​ ℂ x ​ y 2, ϑ ≐ σ ′ ​ ψ ∗ ​ ( ω). d\mathcal{H}+\varepsilon\vartheta=0\ \ \ \hbox{ on }\ \mathbb{C}^{2}_{x\,y},\ \ \vartheta\doteq\sigma^{\prime}\psi_{*}(\omega). |  | (20) |

The pair ( ψ, σ) (\psi,\sigma) is not explicit in general; however, by Proposition 8 we will obtain explicitly tighter upper bounds for the degrees of ψ \psi, ℋ \mathcal{H} and ϑ \vartheta.

2. Step 2.

The corresponding rectifying map ℛ \mathcal{R} in ( 19) transforms this last equation into a *rational*differential equation

 | d ​ 𝔠 + ε ​ η = 0 on ​ ℂ t ​ 𝔠 2, η ≐ ℛ ∗ ​ ( ϑ), d\mathfrak{c}+\varepsilon\eta=0\ \ \hbox{ on }\ \mathbb{C}^{2}_{t\,\mathfrak{c}},\ \ \eta\doteq\mathcal{R}_{*}(\vartheta), |  | (21) |

with the advantage that the foliation of d ​ 𝔠 = 0 d\mathfrak{c}=0 on ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}} is topologically trivial.

3. Step 3.

We consider the infinitesimal perturbed Hamiltonian differential equations ( 1), ( 20) and ( 21). As we will show in Proposition 17, the unperturbed differential equation d ​ 𝔠 = 0 d\mathfrak{c}=0 is endowed with canonical global generators

 | B ​ C ​ ( 𝔠) = { α 𝚒 ​ ( 𝔠) | 1 ≤ 𝚒 ≤ 𝔯 ​ and ​ 𝔠 ∈ ℂ \ 𝔅 ⁡ ( ℋ) } BC(\mathfrak{c})=\{\alpha_{\tt i}(\mathfrak{c})\,|\ 1\leq{\tt i}\leq\mathfrak{r}\,\mbox{ and }\,\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\} |  |

of the fundamental groups for all the generic fibers, where each α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) encloses, with anti-clockwise orientation, exactly one of the punctures in the horizontal lines of the foliation d ​ 𝔠 = 0 d\mathfrak{c}=0 on ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}. Also by Proposition 17, using the rectifying map ℛ \mathcal{R} and the pair ( ψ, σ) (\psi,\sigma) of polynomial automorphisms, we get canonical global bases of cycles of d ​ ℋ = 0 d\mathcal{H}=0 and d ​ H = 0 dH=0, respectively, we have

 | B ​ C ​ ( ℋ) = { δ 𝚒 ​ ( 𝔠) = ℛ − 1 ​ ( α 𝚒 ​ ( 𝔠)) | 1 ≤ 𝚒 ≤ 𝔯 ​ and ​ 𝔠 ∈ ℂ \ 𝔅 ⁡ ( ℋ) }, BC(\mathcal{H})=\big\{\delta_{\tt i}(\mathfrak{c})=\mathcal{R}^{-1}(\alpha_{\tt i}(\mathfrak{c}))\ |\ 1\leq{\tt i}\leq\mathfrak{r}\ \hbox{ and }\ \mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\big\}, |  |

and

 | B C ( H) = { γ 𝚒 ( c) = ψ − 1 ( δ 𝚒 ( σ ( c)) | 1 ≤ 𝚒 ≤ 𝔯 and c ∈ ℂ \ 𝔅 ( H) }. BC(H)=\{\gamma_{\tt i}(c)=\psi^{-1}\big(\delta_{\tt i}(\sigma(c)\big)\,|\,1\leq{\tt i}\leq\mathfrak{r}\ \hbox{ and }\ c\in\mathbb{C}\backslash\mathfrak{B}(H)\}. |  |

The corresponding three families of Abelian integrals are well defined in the corresponding generic value sets in ℂ \mathbb{C} and satisfy

 | I 𝚒 ​ ( c) = ∫ γ 𝚒 ​ ( c) ω = 1 σ ′ ​ ℐ 𝚒 ​ ( 𝔠) = 1 σ ′ ​ ∫ δ 𝚒 ​ ( 𝔠) ϑ = 1 σ ′ ​ J 𝚒 ​ ( 𝔠) = 1 σ ′ ​ ∫ α 𝚒 ​ ( 𝔠) η. I_{\tt i}(c)=\displaystyle\int_{\gamma_{{\tt i}}(c)}\omega\,=\frac{1}{\sigma^{\prime}}\mathcal{I}_{\tt i}(\mathfrak{c})=\frac{1}{\sigma^{\prime}}\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta\,=\frac{1}{\sigma^{\prime}}J_{\tt i}(\mathfrak{c})=\frac{1}{\sigma^{\prime}}\int_{\alpha_{\tt i}(\mathfrak{c})}\eta\,. |  | (22) |

The left equality of the integrals follows from Corollary 5. The right equality of the integrals will be given in Corollary 15.

4. Step 4.

The maximal number of isolated zeros, counted with multiplicities, for each integral in ( 22) is well defined and

 | Z ⁡ ( I 𝚒 ​ ( c)) = Z ⁡ ( ℐ 𝚒 ​ ( 𝔠)) = Z ⁡ ( J 𝚒 ​ ( 𝔠)). Z(I_{\tt i}(c))=Z(\mathcal{I}_{\tt i}(\mathfrak{c}))=Z(J_{\tt i}(\mathfrak{c})). |  | (23) |

Moreover, according to ( 8), we archive the equalities

 | 𝒩 B ​ C ​ ( H) ​ ( ω) = 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) = 𝒩 B ​ C ​ ( 𝔠) ​ ( η). \mathscr{N}_{BC(H)}(\omega)=\mathscr{N}_{BC(\mathcal{H})}(\vartheta)=\mathscr{N}_{BC(\mathfrak{c})}(\eta). |  | (24) |

In fact, the rectifying map ℛ \mathcal{R} and the residue theorem for η \eta, allow us to compute the upper bound given in ( 4).

The following diagram illustrates the Program, to be descriptive, the vertical arrows must be understood as implications:

 | d ​ H + ε ​ ω = 0 {\lx@inpgf@ignorespaces dH+\varepsilon\omega=0\;} d ​ ℋ + ε ​ ϑ = 0 {\lx@inpgf@ignorespaces\;d\mathcal{H}+\varepsilon\vartheta=0\,} d ​ 𝔠 + ε ​ η = 0 {\lx@inpgf@ignorespaces\;d\mathfrak{c}+\varepsilon\eta=0} I 𝚒 ​ ( c) {\lx@inpgf@ignorespaces I_{\tt i}(c)} ℐ 𝚒 ​ ( 𝔠) {\lx@inpgf@ignorespaces\mathcal{I}_{\tt i}(\mathfrak{c})} J 𝚒 ​ ( 𝔠) {\lx@inpgf@ignorespaces J_{\tt i}(\mathfrak{c})} Z ​ ( I 𝚒 ​ ( c)) {\lx@inpgf@ignorespaces Z(I_{\tt i}(c))} Z ​ ( ℐ 𝚒 ​ ( 𝔠)) {\lx@inpgf@ignorespaces Z(\mathcal{I}_{\tt i}(\mathfrak{c}))} Z ​ ( J 𝚒 ​ ( 𝔠)) {\lx@inpgf@ignorespaces Z(J_{\tt i}(\mathfrak{c}))} 𝒩 B ​ C ​ ( H) ​ ( ω) {\lx@inpgf@ignorespaces\mathscr{N}_{BC(H)}(\omega)} 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) {\lx@inpgf@ignorespaces\mathscr{N}_{BC(\mathcal{H})}(\vartheta)} 𝒩 B ​ C ​ ( 𝔠) ​ ( η). {\lx@inpgf@ignorespaces\mathscr{N}_{BC(\mathfrak{c})}(\eta)\,.} ( ψ, σ) ∗ \scriptstyle{\lx@inpgf@ignorespaces(\psi,\sigma)_{*}} ℛ ∗ \scriptstyle{\lx@inpgf@ignorespaces\mathcal{R}_{*}} ( ψ, σ) ∗ \scriptstyle{\lx@inpgf@ignorespaces(\psi,\sigma)_{*}} ℛ ∗ \scriptstyle{\lx@inpgf@ignorespaces\mathcal{R}_{*}} = \scriptstyle{\lx@inpgf@ignorespaces=} = \scriptstyle{\lx@inpgf@ignorespaces=} = \scriptstyle{\lx@inpgf@ignorespaces=} = \scriptstyle{\lx@inpgf@ignorespaces=} |  | (25) |

## 4. Normal forms of polynomials with trivial global monodromy

Concerning the difficulty D.1 in § 2.3, we recall the explicit normal forms of polynomials with trivial global monodromy and their associated birational rectifying maps. These properties allow us to perform our diagram ( 25) of the Program.

### 4.1. Neumann–Norbury algebraic classification

The simplest case for the weak infinitesimal Hilbert’s 16th problem concerns the algebraic classification of primitive polynomials H ⁡ ( u, v) H(u,v) of type ( 0, 2) (0,2), that have generic fiber L c L_{c} bihomolorphic to ℂ ∗ \mathbb{C}^{*}. This classification was archived by M. Miyanishi and T. Sugie [23] and can be stated as follows.

###### Theorem 9 ( [23]).

A primitive polynomial of type ( 0, 2) (0,2) is algebraically equivalent to a polynomial that belongs to the family

 | { ℋ ⁡ ( x, y) = x k ​ ( x l ​ y + P ⁡ ( x)) r | k, r ∈ ℕ, ( k, r) = 1, l ∈ ℕ ∪ { 0 }, deg ( P) ≤ l − 1, P ( 0) ≠ 0 if l > 0, and ​ P ​ ( x) ≡ 0 ​ if ​ l = 0 }. \left\{\mathcal{H}(x,y)=x^{k}\Big(x^{l}y+P(x)\Big)^{r}\,\Bigg|\,\begin{array}[]{l}k,r\in\mathbb{N},\ (k,r)=1,\ l\in\mathbb{N}\cup\{0\},\\ \deg(P)\leq l-1,\ P(0)\not=0\,\textrm{ if }\,l>0,\\ \textrm{and }P(x)\equiv 0\textrm{ if }\,l=0\end{array}\!\!\right\}. |  |

Each polynomial in this family has trivial global monodromy. In general, E. Artal-Bartolo *et al.*[3] proved in [3, Corollary 2] that a primitive polynomial H ∈ ℂ ⁡ [u, v] H\in\mathbb{C}[u,v] has trivial global monodromy if and only if it is “rational of simple type” in the terminology of Miyanishi and Sugie [23]. This result was refined by Neumann and Norbury in [24], where they pointed out a gap in the Miyanishi–Sugie classification of such polynomials, since [23, p. 346, lines 10-11] implicitly assumes trivial geometric monodromy. Trivial geometric monodromy implies *isotriviality*, that is, the generic fibers are pairwise isomorphic as punctured compact Riemann surfaces. In [24] Neumann and Norbury provided non-isotrivial examples. Finally, Neumann and Norbury in [25] gave the algebraic classification of rational polynomials of simple type. A gap in the proof of the main result of [25] was indicated in [8], where it was filled up. It did not modify the algebraic classification. Therefore, the normal forms of primitive polynomials with trivial global monodromy can be expressed as follows.

###### Theorem 10 (Neumann–Norbury algebraic classification [24, 25]).

Each primitive polynomial H H with trivial global monodromy is algebraically equivalent to a polynomial ℋ ι \mathcal{H}_{\iota}, for ι = 1, 2, \iota=1,2, or 3 3, which belongs to one of the following three families:

 | 𝔉 1 = { ℋ 1 ​ ( x, y) = x q 1 ​ 𝒮 ​ ( x, y) q + x p 1 ​ 𝒮 ​ ( x, y) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x q 1 ​ 𝒮 ​ ( x, y) q) a 𝚒 | r ≥ 2 }, 𝔉 2 = { ℋ 2 ​ ( x, y) = x p 1 ​ 𝒮 ​ ( x, y) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x q 1 ​ 𝒮 ​ ( x, y) q) a 𝚒 | r ≥ 1 }, 𝔉 3 = { ℋ 3 ​ ( x, y) = y ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x) a 𝚒 + h ⁡ ( x) | r ≥ 1 }, \begin{array}[]{l}\displaystyle\mathfrak{F}_{1}=\left\{\mathcal{H}_{1}(x,y)=x^{q_{1}}\mathcal{S}(x,y)^{q}+x^{p_{1}}\mathcal{S}(x,y)^{p}\prod_{{\tt i}=1}^{r-1}\big(\beta_{\tt i}-x^{q_{1}}\mathcal{S}(x,y)^{q}\big)^{a_{\tt i}}\,\big|\,{r\geq 2}\right\},\\[18.0pt] \displaystyle\mathfrak{F}_{2}=\left\{\mathcal{H}_{2}(x,y)=x^{p_{1}}\mathcal{S}(x,y)^{p}\prod_{{\tt i}=1}^{r-1}\big(\beta_{\tt i}-x^{q_{1}}\mathcal{S}(x,y)^{q}\big)^{a_{\tt i}}\,\big|\,{r\geq 1}\right\},\\[18.0pt] \displaystyle\mathfrak{F}_{3}=\left\{\mathcal{H}_{3}(x,y)=y\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-x\right)^{a_{\tt i}}+h(x)\,\big|\,{r\geq 1}\right\},\\ \end{array} |  |

where

- •

a 𝟷, …, a r − 1 a_{\tt 1},\ldots,a_{r-1} are positive integers,

- •

β 1, …, β r − 1 \beta_{1},\ldots,\beta_{r-1} are distinct points of ℂ ∗ \mathbb{C}^{*},

- •

h ⁡ ( x) h(x) is a polynomial of degree less than ∑ 𝚒 = 1 r − 1 a 𝚒 \sum_{{\tt i}=1}^{r-1}a_{\tt i},

- •

0 ≤ p 1 < p 0\leq p_{1}<p, 0 ≤ q 1 < q 0\leq q_{1}<q, and ( p ​ q 1 − q ​ p 1) = ± 1 (pq_{1}-qp_{1})=\pm 1,

- •

𝒮 ⁡ ( x, y) = x k ​ y + P ⁡ ( x) \mathcal{S}(x,y)=x^{k}y+P(x), with k ≥ 1 {k}\geq 1 and P ⁡ ( x) ∈ ℂ ​ [x] ≤ k − 1 P(x)\in\mathbb{C}[x]_{\leq{k}-1}.

Moreover, if 𝒢 1 ​ ( x, y) = 𝒢 2 ​ ( x, y) = x q 1 ​ 𝒮 ​ ( x, y) q \mathcal{G}_{1}(x,y)=\mathcal{G}_{2}(x,y)=x^{q_{1}}\mathcal{S}(x,y)^{q} and 𝒢 3 ​ ( x, y) = x \mathcal{G}_{3}(x,y)=x, then

 | ℛ ι = ( 𝒢 ι, ℋ ι): ℂ x ​ y 2 ⟶ ℂ t ​ 𝔠 2 \mathcal{R}_{\iota}=(\mathcal{G}_{\iota},\mathcal{H}_{\iota}):\mathbb{C}_{x\,y}^{2}\longrightarrow\mathbb{C}_{t\,\mathfrak{c}}^{2} |  | (26) |

is a birational map for ι = 1, 2, 3 \iota=1,2,3. In fact, 𝒢 ι ​ ( x, y) \mathcal{G}_{\iota}(x,y) maps a generic fiber ℋ ι − 1 ​ ( 𝔠) \mathcal{H}^{-1}_{\iota}(\mathfrak{c}) biholomorphically to

 | ℂ \ { 0, β 1, …, β r − 1, 𝔠 }, ℂ \ { 0, β 1, …, β r − 1 } or ℂ \ { β 1, …, β r − 1 }, \mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1},\mathfrak{c}\},\ \ \mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1}\}\ \ \hbox{ or }\ \ \mathbb{C}\backslash\{\beta_{1},\ldots,\beta_{r-1}\}, |  | (27) |

according as ι = 1, 2, 3. \iota=1,2,3. Thus, ℋ 1 ∈ 𝔉 1 \mathcal{H}_{1}\in\mathfrak{F}_{1} is not isotrivial, but ℋ 2 ∈ 𝔉 2 \mathcal{H}_{2}\in\mathfrak{F}_{2}, ℋ 3 ∈ 𝔉 3 \mathcal{H}_{3}\in\mathfrak{F}_{3} are isotrivial.

###### Remark 4.

If we consider ℋ 2 ∈ 𝔉 2 \mathcal{H}_{2}\in\mathfrak{F}_{2} and r = 1 r=1, then ℋ 2 ​ ( x, y) = x p 1 ​ ( x k ​ y + P ⁡ ( x)) p \mathcal{H}_{2}(x,y)=x^{p_{1}}\left(x^{k}y+P(x)\right)^{p}. Though the parameters q 1 q_{1} and q q do not appear explicitly in this case, the birational map in ( 26) exists, where q 1 q_{1} and q q are suitable positive integers with q 1 ≤ q q_{1}\leq q such that p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1, that is, the conditions 0 ≤ p 1 < p 0\leq p_{1}<p and ( p 1, p) = 1 (p_{1},p)=1 must be satisfied.

Concerning the concept of normal form given in Definition 4, we have the following result.

###### Lemma 11.

Each polynomial ℋ ι ∈ 𝔉 1 ∪ 𝔉 2 ∪ 𝔉 3 \mathcal{H}_{\iota}\in\mathfrak{F}_{1}\cup\mathfrak{F}_{2}\cup\mathfrak{F}_{3} is a normal form, that is, ℋ ι \mathcal{H}_{\iota} attains the minimum degree in its Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) –orbit.

###### Proof.

Since the degree of a polynomial remains invariant under Aut ⁡ ( ℂ) \mathop{\mbox{Aut}}\nolimits(\mathbb{C}), it is sufficient to prove that for each ψ = ( ψ 1, ψ 2) ∈ Aut ⁡ ( ℂ 2) \psi=(\psi_{1},\psi_{2})\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2}) we have the inequality

 | deg ⁡ ( ℋ ι ∘ ψ) ≥ deg ⁡ ( ℋ ι). \deg(\mathcal{H}_{\iota}\circ\psi)\geq\deg(\mathcal{H}_{\iota}). |  | (28) |

Let n i = deg ⁡ ( ψ i) ≥ 1 n_{i}=\deg(\psi_{i})\geq 1 for i = 1, 2 i=1,2. If ℋ 3 ​ ( x, y) = y ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x) a 𝚒 + h ⁡ ( x) ∈ 𝔉 3, \mathcal{H}_{3}(x,y)=y\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-x\right)^{a_{\tt i}}+h(x)\in\mathfrak{F}_{3}, then

 | ℋ 3 ∘ ψ = ψ 2 ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − ψ 1) a 𝚒 + h ⁡ ( ψ 1). \mathcal{H}_{3}\circ\psi=\psi_{2}\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\psi_{1}\right)^{a_{\tt i}}+h(\psi_{1}). |  |

Since deg ⁡ ( h ⁡ ( x)) < ∑ 𝚒 = 1 r − 1 a 𝚒 \deg(h(x))<\sum_{{\tt i}=1}^{r-1}a_{\tt i} and n 1, n 2 ≥ 1 n_{1},n_{2}\geq 1,

 | deg ⁡ ( ℋ 3 ∘ ψ) = n 2 + n 1 ​ ∑ 𝚒 = 1 r − 1 a 𝚒 ≥ 1 + ∑ 𝚒 = 1 r − 1 a 𝚒 = deg ⁡ ( ℋ 3). \deg(\mathcal{H}_{3}\circ\psi)=n_{2}+n_{1}\sum_{{\tt i}=1}^{r-1}a_{\tt i}\geq 1+\sum_{{\tt i}=1}^{r-1}a_{\tt i}=\deg(\mathcal{H}_{3}). |  |

Now let ℋ 2 ​ ( x, y) = x p 1 ​ ( x k ​ y + P ⁡ ( x)) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x q 1 ​ ( x k ​ y + P ⁡ ( x)) q) a 𝚒 ∈ 𝔉 2. \mathcal{H}_{2}(x,y)=x^{p_{1}}(x^{k}y+P(x))^{p}\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-x^{q_{1}}(x^{k}y+P(x))^{q})^{a_{\tt i}}\in\mathfrak{F}_{2}. Therefore,

 | ℋ 2 ∘ ψ = ψ 1 p 1 ​ ( ψ 1 k ​ ψ 2 + P ⁡ ( ψ 1)) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − ψ 1 q 1 ​ ( ψ 1 k ​ ψ 2 + P ⁡ ( ψ 1)) q) a 𝚒. \mathcal{H}_{2}\circ\psi=\psi_{1}^{p_{1}}\big(\psi_{1}^{k}\psi_{2}+P(\psi_{1})\big)^{p}\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\psi_{1}^{q_{1}}\big(\psi_{1}^{k}\psi_{2}+P(\psi_{1})\big)^{q}\right)^{a_{\tt i}}. |  |

Hence, deg ⁡ ( ℋ 2 ∘ ψ) = p 1 ​ n 1 + p ⁡ ( k ​ n 1 + n 2) + ( q 1 ​ n 1 + q ⁡ ( k ​ n 1 + n 2)) ​ ∑ 𝚒 = 1 r − 1 a 𝚒. \deg(\mathcal{H}_{2}\circ\psi)=p_{1}n_{1}+p(kn_{1}+n_{2})+(q_{1}n_{1}+q(kn_{1}+n_{2}))\sum_{{\tt i}=1}^{r-1}a_{\tt i}. As n 1, n 2 ≥ 1 n_{1},n_{2}\geq 1, we obtain

 | deg ⁡ ( ℋ 2 ∘ ψ) ≥ p 1 + p ⁡ ( k + 1) + ( q 1 + q ⁡ ( k + 1)) ​ ∑ 𝚒 = 1 r − 1 a 𝚒 = deg ⁡ ( ℋ 2). \deg(\mathcal{H}_{2}\circ\psi)\geq p_{1}+p(k+1)+(q_{1}+q(k+1))\sum_{{\tt i}=1}^{r-1}a_{\tt i}=\deg(\mathcal{H}_{2}). |  |

Finally, for ℋ 1 ​ ( x, y) ∈ 𝔉 1 \mathcal{H}_{1}(x,y)\in\mathfrak{F}_{1} we have an analogous computation as in the previous case, which we leave to the reader. ∎

###### Remark 5.

If we consider ℋ 3 ∈ 𝔉 3 \mathcal{H}_{3}\in\mathfrak{F}_{3} with r = 1 r=1, then we have ℋ 3 ​ ( x, y) = y \mathcal{H}_{3}(x,y)=y. This polynomial is of type ( 0, 1) (0,1), that is, dim H 1 ​ ( ℒ 𝔠, ℤ) = 0 \dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=0. Hence, from now on we will consider only polynomials in 𝔉 3 \mathfrak{F}_{3} with r ≥ 2 r\geq 2.

The Miyanishi–Sugie and Neumann–Norbury classifications of primitive polynomials of type ( 0, 2) (0,2) are equivalent, our accurate assertion is as follows.

###### Lemma 12.

The normal forms of primitive polynomials of type ( 0, 2) (0,2) provided by Theorem 9 and Theorem 10 are algebraically equivalent.

###### Proof.

In Theorem 10, the normal forms of polynomials of type ( 0, 2) (0,2) are given by ℋ 2 ∈ 𝔉 2 \mathcal{H}_{2}\in\mathfrak{F}_{2} with r = 1 r=1 and ℋ 3 ∈ 𝔉 3 \mathcal{H}_{3}\in\mathfrak{F}_{3} with r = 2 r=2.

Consider ℋ 2 \mathcal{H}_{2} with r = 1 r=1, thus

 | ℋ 2 ​ ( x, y) = x p 1 ​ ( x k ​ y + P ⁡ ( x)) p. \mathcal{H}_{2}(x,y)=x^{p_{1}}\Big(x^{k}y+P(x)\Big)^{p}. |  | (29) |

We have the following four cases below.

1. Case 1.

Assume that 0 < p 1 < p 0<p_{1}<p and P ⁡ ( x) ≡ 0 P(x)\equiv 0. Then

 | ℋ 2 ​ ( x, y) = x p 1 + p ​ k ​ y p. \mathcal{H}_{2}(x,y)=x^{p_{1}+pk}y^{p}. |  | (30) |

If we rename the parameters p 1 + p ​ k p_{1}+pk and p p by k k and r r, respectively, we then obtain polynomials in Theorem 9 with 1 < r < k 1<r<k and l = 0 l=0. Moreover, each polynomial in Theorem 9 with 1 < r < k 1<r<k and l = 0 l=0 can be obtained from ( 30). Indeed, we have k = μ ​ r + ν > r > 1 k=\mu r+\nu>r>1, with μ ≥ 1 \mu\geq 1 and 0 < ν < r 0<\nu<r, then by using p 1 = ν p_{1}=\nu, p = r p=r and k = μ k=\mu in ( 30), we get the desired polynomial. We note that polynomials x k ​ y r x^{k}y^{r}, with k < r k<r, in Theorem 9 are algebraically equivalent to x k ​ y r x^{k}y^{r}, with r < k r<k, by interchanging the variables.

2. Case 2.

Assume that 0 < p 1 < p 0<p_{1}<p, P ⁡ ( x) ≢ 0 P(x)\not\equiv 0 and P ⁡ ( 0) = 0 P(0)=0. Thus, P ⁡ ( x) = x s ​ P ~ ​ ( x) P(x)=x^{s}\widetilde{P}(x), with 1 ≤ s ≤ k − 1 1\leq s\leq k-1, P ~ ​ ( x) ∈ ℂ ​ [x] ≤ k − s − 1 \widetilde{P}(x)\in\mathbb{C}[x]_{\leq k-s-1} and P ~ ​ ( 0) ≠ 0 \widetilde{P}(0)\neq 0, then

 | ℋ 2 ​ ( x, y) = x p 1 + p ​ s ​ ( x k − s ​ y + P ~ ​ ( x)) p. \mathcal{H}_{2}(x,y)=x^{p_{1}+ps}\Big(x^{k-s}y+\widetilde{P}(x)\Big)^{p}. |  | (31) |

If we rename the parameters p 1 + p ​ s p_{1}+ps, p p, k − s k-s and P ~ ​ ( x) \widetilde{P}(x) as k k, r r, l l and P ⁡ ( x) P(x), respectively, we then obtain polynomials in Theorem 9 with 1 < r < k 1<r<k and l ≠ 0 l\neq 0. Moreover, each polynomial in Theorem 9 with 1 < r < k 1<r<k and l ≠ 0 l\neq 0 can be obtained from ( 31). Indeed, we have k = μ ​ r + ν > r > 1 k=\mu r+\nu>r>1, with μ ≥ 1 \mu\geq 1 and 0 < ν < r 0<\nu<r, and then by using p 1 = ν p_{1}=\nu, p = r p=r, k = l + μ k=l+\mu, s = μ s=\mu and P ~ ​ ( x) = P ​ ( x) \widetilde{P}(x)=P(x) in ( 31), we get the desired polynomial.

3. Case 3.

Assume that 0 < p 1 < p 0<p_{1}<p, P ⁡ ( x) ≢ 0 P(x)\not\equiv 0 and P ⁡ ( 0) ≠ 0 P(0)\neq 0. Then the resulting polynomials in ( 29) are in correspondence with the polynomials in Theorem 9, satisfying 1 ≤ k < r 1\leq k<r and l ≠ 0 l\neq 0, by renaming the parameters p 1, p p_{1},p and k k as k, r k,r and l l, respectively.

4. Case 4.

Assume that 0 = p 1 0=p_{1}, so p = 1 p=1. If P ⁡ ( x) ≡ 0 P(x)\equiv 0, then ℋ 2 ​ ( x, y) = x k ​ y \mathcal{H}_{2}(x,y)=x^{k}y. Thus, we obtain all polynomials in Theorem 9 with 1 = r ≤ k 1=r\leq k and l = 0 l=0. If P ⁡ ( x) ≢ 0 P(x)\not\equiv 0 and P ⁡ ( 0) = 0 P(0)=0, then P ⁡ ( x) = x s ​ P ~ ​ ( x) P(x)=x^{s}\widetilde{P}(x), with 1 ≤ s ≤ k − 1 1\leq s\leq k-1, P ~ ​ ( x) ∈ ℂ ​ [x] ≤ k − s − 1 \widetilde{P}(x)\in\mathbb{C}[x]_{\leq k-s-1} and P ~ ​ ( 0) ≠ 0 \widetilde{P}(0)\neq 0. Thus, ℋ 2 ​ ( x, y) = x s ​ ( x k − s ​ y + P ~ ​ ( x)) \mathcal{H}_{2}(x,y)=x^{s}\left(x^{k-s}y+\widetilde{P}(x)\right). Hence, if we rename s s, k − s k-s and P ~ ​ ( x) \widetilde{P}(x) as k k, l l and P ⁡ ( x) P(x), respectively, then we obtain the polynomials in Theorem 9 with 1 = r ≤ k 1=r\leq k and l ≠ 0 l\neq 0. Finally, if P ⁡ ( x) ≢ 0 P(x)\not\equiv 0 and P ⁡ ( 0) ≠ 0 P(0)\neq 0, then by using the automorphism σ ⁡ ( c) = c − P ⁡ ( 0) \sigma(c)=c-P(0), the normal form ℋ 2 ​ ( x, y) \mathcal{H}_{2}(x,y) reduces to one of the two previous situations considered in this case.

We now consider ℋ 3 ∈ 𝔉 3 \mathcal{H}_{3}\in\mathfrak{F}_{3} with r = 2 r=2, thus

 | ℋ 3 ​ ( x, y) = y ​ ( β 1 − x) a 1 + h ⁡ ( x). \mathcal{H}_{3}(x,y)=y(\beta_{1}-x)^{a_{1}}+h(x). |  |

If we take ℋ 2 ∈ 𝔉 2 \mathcal{H}_{2}\in\mathfrak{F}_{2} with r = 1 r=1, p 1 = 0 p_{1}=0 and p = 1 p=1, then ℋ 2 ​ ( x, y) = x k ​ y + P ⁡ ( x) \mathcal{H}_{2}(x,y)=x^{k}y+P(x). Hence, by taking a 1 = k a_{1}=k and a translation in the x x -axis, these two polynomials ℋ 2 ​ ( x, y) \mathcal{H}_{2}(x,y) and ℋ 3 ​ ( x, y) \mathcal{H}_{3}(x,y) are algebraically equivalent. This completes the proof. ∎

### 4.2. Degree of the transformed polynomials and 1-forms

In order to get upper bounds for Z ⁡ ( I ⁡ ( c)) Z(I(c)) and 𝒩 B ​ C ​ ( H) ​ ( ω) \mathscr{N}_{BC(H)}(\omega) through Z ⁡ ( ℐ ⁡ ( 𝔠)) Z(\mathcal{I}(\mathfrak{c})) and 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) \mathscr{N}_{BC(\mathcal{H})}(\vartheta), we must control the degrees of the transformed ℋ \mathcal{H} and ϑ \vartheta. For primitive polynomials with trivial global monodromy on ℂ 2 \mathbb{C}^{2}, we can control the degree of the transformed objects explicitly. More precisely, we have the next result, which represents an improvement of Lemma 7.

###### Proposition 13.

Let H ⁡ ( u, v) H(u,v) be a primitive polynomial with trivial global monodromy of degree m + 1 m+1, with 𝔯 = dim H 1 ​ ( L c, ℤ) ≥ 1 \mathfrak{r}=\dim H_{1}(L_{c},\mathbb{Z})\geq 1, and let ω ∈ Ω 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}. Consider the normal form ℋ ⁡ ( x, y) ∈ 𝔉 1 ∪ 𝔉 2 ∪ 𝔉 3 \mathcal{H}(x,y)\in\mathfrak{F}_{1}\cup\mathfrak{F}_{2}\cup\mathfrak{F}_{3} of H ⁡ ( u, v) H(u,v) through the automorphisms ( ψ, σ) (\psi,\sigma), and the 1-form ϑ = σ ′ ​ ψ ∗ ​ ( ω) \vartheta=\sigma^{\prime}\psi_{*}(\omega) as in ( 14).

1. 1)

If ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1}, then r + 1 = dim H 1 ​ ( ℒ c, ℤ) = 𝔯 ≥ 3 r+1=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\mathfrak{r}\geq 3 and

 | 7 ≤ deg ⁡ ( ℋ) ≤ m + 1, deg ⁡ ( ϑ) ≤ ( n + 1) ​ [m − 𝔯 𝔯] − 1. 7\leq\deg(\mathcal{H})\leq m+1,\quad\quad\deg(\vartheta)\leq(n+1)\left[\dfrac{m-\mathfrak{r}}{\mathfrak{r}}\right]-1. |  |

2. 2)

If ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2}, then r = dim H 1 ​ ( ℒ c, ℤ) = 𝔯 ≥ 1 r=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\mathfrak{r}\geq 1 and

 | { 2 ≤ deg ( ℋ) ≤ m + 1, deg ( ϑ) ≤ ( n + 1) ( m) − 1, if 𝔯 = 1; 7 ≤ deg ( ℋ) ≤ m + 1, deg ( ϑ) ≤ ( n + 1) [m − 𝔯 − 1 𝔯 + 1] − 1, if 𝔯 ≥ 2. \begin{cases}2\leq\deg(\mathcal{H})\leq m+1,\quad\quad\deg(\vartheta)\leq(n+1)(m)-1,&\mbox{ if \ $\mathfrak{r}=1$};\\[6.0pt] 7\leq\deg(\mathcal{H})\leq m+1,\quad\quad\deg(\vartheta)\leq(n+1)\left[\dfrac{m-\mathfrak{r}-1}{\mathfrak{r}+1}\right]-1,&\mbox{ if \ $\mathfrak{r}\geq 2$}.\end{cases} |  |

3. 3)

If ℋ ∈ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{3}, then r − 1 = dim H 1 ​ ( ℒ c, ℤ) = 𝔯 ≥ 1 r-1=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\mathfrak{r}\geq 1 and

 | 𝔯 + 1 ≤ deg ⁡ ( ℋ) ≤ m + 1, deg ⁡ ( ϑ) ≤ ( n + 1) ​ ( m + 1 − 𝔯) − 1. \mathfrak{r}+1\leq\deg(\mathcal{H})\leq m+1,\quad\quad\deg(\vartheta)\leq(n+1)(m+1-\mathfrak{r})-1. |  |

###### Proof.

Let ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) be a pair of polynomial automorphisms such that

H = σ − 1 ∘ ℋ ∘ ψ, H=\sigma^{-1}\circ\mathcal{H}\circ\psi,

as in equation ( 12). Since σ − 1 \sigma^{-1} is an affine automorphism,

 | m + 1 = deg ⁡ ( H) = deg ⁡ ( ℋ ∘ ψ) m+1=\deg(H)=\deg(\mathcal{H}\circ\psi) |  | (32) |

and

 | deg ⁡ ( ϑ) = deg ⁡ ( ψ ∗ ​ ( ω)) = deg ⁡ ( ω) ​ deg ⁡ ( ψ − 1) + deg ⁡ ( ψ − 1) − 1. \deg(\vartheta)=\deg(\psi_{*}(\omega))=\deg(\omega)\deg(\psi^{-1})+\deg(\psi^{-1})-1. |  | (33) |

Now, let ψ 1 \psi_{1} and ψ 2 \psi_{2} be the two polynomial components of ψ \psi with degrees n 1 ≥ 1 n_{1}\geq 1 and n 2 ≥ 1 n_{2}\geq 1, respectively.

For simplicity, we begin proving statement OPEN 3) 3). Assume that ℋ ⁡ ( x, y) ∈ 𝔉 3 \mathcal{H}(x,y)\in\mathfrak{F}_{3}, then

 | ℋ ∘ ψ = ψ 2 ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − ψ 1) a 𝚒 + h ⁡ ( ψ 1). \mathcal{H}\circ\psi=\psi_{2}\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\psi_{1}\right)^{a_{\tt i}}+h(\psi_{1}). |  | (34) |

Thus, from equations ( 32) and ( 34) we get

 | m + 1 = n 2 + n 1 ​ ∑ 𝚒 = 1 r − 1 a 𝚒. m+1=n_{2}+n_{1}\sum_{{\tt i}=1}^{r-1}a_{\tt i}. |  | (35) |

Since r − 1 = dim H 1 ​ ( ℒ c, ℤ) = dim H 1 ​ ( L c, ℤ) = 𝔯 ≥ 1 r-1=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\dim H_{1}(L_{c},\mathbb{Z})=\mathfrak{r}\geq 1, r ≥ 2. r\geq 2. Thus, ∑ 𝚒 = 1 r − 1 a 𝚒 ≥ 𝔯 ≥ 1. \sum_{{\tt i}=1}^{r-1}a_{\tt i}\geq\mathfrak{r}\geq 1. Moreover, as n 1, n 2 ≥ 1 n_{1},n_{2}\geq 1, from equation ( 35) it follows that

 | m + 1 ≥ 1 + ∑ 𝚒 = 1 r − 1 a 𝚒 = deg ⁡ ( ℋ) ≥ 1 + 𝔯 and m + 1 ≥ n 2 + n 1 ​ 𝔯. m+1\geq 1+\sum_{{\tt i}=1}^{r-1}a_{\tt i}=\deg(\mathcal{H})\geq 1+\mathfrak{r}\qquad\mbox{and}\qquad m+1\geq n_{2}+n_{1}\mathfrak{r}. |  |

Thus, n 1 ≤ m / 𝔯 n_{1}\leq m/\mathfrak{r} and n 2 ≤ m + 1 − 𝔯 n_{2}\leq m+1-\mathfrak{r}. Hence, the degree of ψ \psi is at most m + 1 − 𝔯 m+1-\mathfrak{r}. This implies that deg ⁡ ( ψ − 1) ≤ m + 1 − 𝔯 \deg(\psi^{-1})\leq m+1-\mathfrak{r}; see [4, 7]. Therefore, from ( 33) we have

 | deg ⁡ ( ϑ) ≤ ( n + 1) ​ ( m + 1 − 𝔯) − 1. \deg(\vartheta)\leq(n+1)(m+1-\mathfrak{r})-1. |  |

Now we will prove statement OPEN 2) 2). Assume that ℋ ⁡ ( x, y) ∈ 𝔉 2 \mathcal{H}(x,y)\in\mathfrak{F}_{2}, and then

 | ℋ ∘ ψ = ψ 1 p 1 ​ ( ψ 1 k ​ ψ 2 + P ⁡ ( ψ 1)) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − ψ 1 q 1 ​ ( ψ 1 k ​ ψ 2 + P ⁡ ( ψ 1)) q) a 𝚒. \mathcal{H}\circ\psi=\psi_{1}^{p_{1}}\big(\psi_{1}^{k}\psi_{2}+P(\psi_{1})\big)^{p}\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\psi_{1}^{q_{1}}\big(\psi_{1}^{k}\psi_{2}+P(\psi_{1})\big)^{q}\right)^{a_{\tt i}}. |  |

Hence, from equations ( 32) and ( 34)

 | m + 1 = p 1 ​ n 1 + p ⁡ ( k ​ n 1 + n 2) + ( q 1 ​ n 1 + q ⁡ ( k ​ n 1 + n 2)) ​ ∑ 𝚒 = 1 r − 1 a 𝚒. m+1=p_{1}n_{1}+p(kn_{1}+n_{2})+\big(q_{1}n_{1}+q(kn_{1}+n_{2})\big)\sum_{{\tt i}=1}^{r-1}a_{\tt i}. |  | (36) |

In this case, r = dim H 1 ​ ( ℒ c, ℤ) = dim H 1 ​ ( L c, ℤ) = 𝔯 ≥ 1 r=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\dim H_{1}(L_{c},\mathbb{Z})=\mathfrak{r}\geq 1 implies that r ≥ 1. r\geq 1. We will consider two possibilities: r = 𝔯 = 1 r=\mathfrak{r}=1 and r = 𝔯 ≥ 2 r=\mathfrak{r}\geq 2.

In the former, as n 1 n_{1} and n 2 n_{2} are positive integers, k ≥ 1 k\geq 1 and 0 ≤ p 1 < p 0\leq p_{1}<p, 0 ≤ q 1 < q 0\leq q_{1}<q with p ​ q 1 − q ​ p 1 = ± 1 pq_{1}-qp_{1}=\pm 1, so equation ( 36) then yields

 | m + 1 ≥ p 1 + p ⁡ ( k + 1) = deg ⁡ ( ℋ) ≥ 2 and m + 1 ≥ n 1 + n 2. m+1\geq p_{1}+p(k+1)=\deg(\mathcal{H})\geq 2\quad\mbox{and}\quad m+1\geq n_{1}+n_{2}. |  |

Thus, n 1 ≤ m n_{1}\leq m and n 2 ≤ m n_{2}\leq m. Hence, deg ⁡ ( ψ) ≤ m \deg(\psi)\leq m. This implies that deg ⁡ ( ψ − 1) ≤ m. \deg(\psi^{-1})\leq m. Therefore, from equation ( 33) we have

 | deg ⁡ ( ϑ) ≤ ( n + 1) ​ ( m) − 1. \deg(\vartheta)\leq(n+1)(m)-1. |  |

In the latter, ∑ 𝚒 = 1 r − 1 a 𝚒 ≥ r − 1 = 𝔯 − 1 ≥ 1. \sum_{{\tt i}=1}^{r-1}a_{\tt i}\geq r-1=\mathfrak{r}-1\geq 1. As n 1 n_{1} and n 2 n_{2} are positive integers, k ≥ 1 k\geq 1 and 0 ≤ p 1 < p 0\leq p_{1}<p, 0 ≤ q 1 < q 0\leq q_{1}<q with p ​ q 1 − q ​ p 1 = ± 1 pq_{1}-qp_{1}=\pm 1, then equation ( 36) gives

 | m + 1 ≥ p 1 + p ⁡ ( k + 1) + ( q 1 + q ⁡ ( k + 1)) ​ ( r − 1) = deg ⁡ ( ℋ) ≥ 7. m+1\geq p_{1}+p(k+1)+(q_{1}+q(k+1))(r-1)=\deg(\mathcal{H})\geq 7. |  | (37) |

Moreover, if p 1 = 0 p_{1}=0 or q 1 = 0 q_{1}=0, then from equation ( 36), together with the conditions p ​ q 1 − q ​ p 1 = ± 1 pq_{1}-qp_{1}=\pm 1 and r ≥ 2 r\geq 2, we obtain

 | m + 1 ≥ ( r + 2) ​ n 1 + ( r + 1) ​ n 2. m+1\geq(r+2)n_{1}+(r+1)n_{2}. |  |

Thus, since n 1, n 2 ≥ 1 n_{1},n_{2}\geq 1,

 | n 1 ≤ [m − r r + 2] and n 2 ≤ [m − r − 1 r + 1]. n_{1}\leq\left[\dfrac{m-r}{r+2}\right]\quad\mbox{ and }\quad n_{2}\leq\left[\dfrac{m-r-1}{r+1}\right]. |  |

In addition, by supposing n 1 = n 2 = 1 n_{1}=n_{2}=1, we obtain m ≥ 2 ​ r + 2 m\geq 2r+2, which implies

 | [m − r r + 2] ≤ [m − r − 1 r + 1]. \left[\dfrac{m-r}{r+2}\right]\leq\left[\dfrac{m-r-1}{r+1}\right]. |  |

Now, if p 1 ≥ 1 p_{1}\geq 1 and q 1 ≥ 1 q_{1}\geq 1, then p ≥ 2 p\geq 2 and q ≥ 2 q\geq 2. Thus, from equation ( 36) we get

 | m + 1 ≥ n 1 + 2 ​ ( n 1 + n 2) + ( n 1 + 2 ​ ( n 1 + n 2)) ​ ( r − 1) = 3 ​ n 1 ​ r + 2 ​ n 2 ​ r. m+1\geq n_{1}+2(n_{1}+n_{2})+(n_{1}+2(n_{1}+n_{2}))(r-1)=3n_{1}r+2n_{2}r. |  |

Again, since n 1, n 2 ≥ 1 n_{1},n_{2}\geq 1

 | n 1 ≤ [m + 1 − 2 ​ r 3 ​ r] and n 2 ≤ [m + 1 − 3 ​ r 2 ​ r]. n_{1}\leq\left[\dfrac{m+1-2r}{3r}\right]\quad\mbox{ and }\quad n_{2}\leq\left[\dfrac{m+1-3r}{2r}\right]. |  |

Moreover, by supposing n 1 = n 2 = 1 n_{1}=n_{2}=1, we get m ≥ 5 ​ r ≥ 2 ​ r + 2 m\geq 5r\geq 2r+2. Hence, we have

 | [m + 1 − 2 ​ r 3 ​ r] ≤ [m − r − 1 r + 1] and [m + 1 − 3 ​ r 2 ​ r] ≤ [m − r − 1 r + 1]. \left[\dfrac{m+1-2r}{3r}\right]\leq\left[\dfrac{m-r-1}{r+1}\right]\quad\mbox{and}\quad\left[\dfrac{m+1-3r}{2r}\right]\leq\left[\dfrac{m-r-1}{r+1}\right]. |  |

Therefore, in any case deg ⁡ ( ψ) ≤ [( m − r − 1) / ( r + 1)] \deg(\psi)\leq\left[(m-r-1)/(r+1)\right]. This implies that deg ⁡ ( ψ − 1) ≤ [( m − r − 1) / ( r + 1)] \deg(\psi^{-1})\leq\left[(m-r-1)/(r+1)\right]; see [4, 7]. From ( 33) we obtain

 | deg ⁡ ( ϑ) ≤ ( n + 1) ​ [m − r − 1 r + 1] − 1 = ( n + 1) ​ [m − 𝔯 − 1 𝔯 + 1] − 1. \deg(\vartheta)\leq(n+1)\left[\dfrac{m-r-1}{r+1}\right]-1=(n+1)\left[\dfrac{m-\mathfrak{r}-1}{\mathfrak{r}+1}\right]-1. |  |

Finally, if H ∈ 𝔉 1 H\in\mathfrak{F}_{1}, then we have the same situation as in the second part of the previous case, with r + 1 = 𝔯 r+1=\mathfrak{r}. Thus, the degree of ψ − 1 \psi^{-1} is at most [( m − 𝔯) / 𝔯]. \left[(m-\mathfrak{r})/\mathfrak{r}\right]. Therefore,

 | deg ⁡ ( ϑ) ≤ ( n + 1) ​ [m − 𝔯 𝔯] − 1. \deg(\vartheta)\leq(n+1)\left[\dfrac{m-\mathfrak{r}}{\mathfrak{r}}\right]-1. |  |

This completes the proof. ∎

### 4.3. Rectifying birational maps

The birational map ℛ ι \mathcal{R}_{\iota}, in ( 26), satisfies the commutative diagram

 | ℂ x ​ y 2 {\lx@inpgf@ignorespaces\mathbb{C}_{x\,y}^{2}} ℂ t ​ 𝔠 2 {\lx@inpgf@ignorespaces\mathbb{C}_{t\,\mathfrak{c}}^{2}} ℂ 𝔠 {\lx@inpgf@ignorespaces\mathbb{C}_{\mathfrak{c}}} ℂ 𝔠, {\lx@inpgf@ignorespaces\mathbb{C}_{\mathfrak{c}\,,}} ℛ ι \scriptstyle{\lx@inpgf@ignorespaces\mathcal{R}_{\iota}} ℋ \scriptstyle{\lx@inpgf@ignorespaces\mathcal{H}} 𝔠 \scriptstyle{\lx@inpgf@ignorespaces\mathfrak{c}} i ​ d \scriptstyle{\lx@inpgf@ignorespaces id} |  |

where 𝔠 \mathfrak{c} is the projection in the second component. Thus, ℛ ι \mathcal{R}_{\iota} rectifies the generic fibers of ℋ ι \mathcal{H}_{\iota} into punctured horizontal lines in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}. The accurate study of this property is the next step towards the proofs of Theorems 1 and 2. Furthermore, ℛ ι \mathcal{R}_{\iota} will allow us to establish the equivalence between the Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) defined by the pair ( ℋ ι, ϑ) (\mathcal{H}_{\iota},\vartheta) and the Abelian integral J 𝚒 ​ ( 𝔠) J_{\tt i}(\mathfrak{c}) defined by the pair ( 𝔠, η) (\mathfrak{c},\eta), where η \eta is the corresponding rational 1-form. Owing to the relevance of these consequences in the proofs of our main results, we will state some properties of ℛ ι = ( 𝒢 ι, ℋ ι) \mathcal{R}_{\iota}=(\mathcal{G}_{\iota},\mathcal{H}_{\iota}) as follows.

Notation. For the sake of simplicity, we omit the subscript ι \iota of 𝒢 ι \mathcal{G}_{\iota}, ℋ ι \mathcal{H}_{\iota} and ℛ ι \mathcal{R}_{\iota} when appropriate.

###### Lemma 14.

Let ℛ = ( 𝒢, ℋ) \mathcal{R}=(\mathcal{G},\mathcal{H}) be a birational map, as in ( 26).

1. 1)

There is a suitable algebraic subset 𝔇 \mathfrak{D} of ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}} such that ℛ \mathcal{R} is a biholomorphic map as follows

 | ℂ x ​ y 2 \ Σ ⁡ ( ℛ) → ℛ ℂ t ​ 𝔠 2 \ 𝔇 ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℛ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( M ⁡ ( t, 𝔠) N ⁡ ( t, 𝔠), S ⁡ ( t, 𝔠) T ⁡ ( t, 𝔠)), \begin{array}[]{rcccl}\mathbb{C}^{2}_{x\,y}\backslash\Sigma(\mathcal{R})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\mathfrak{D}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}^{2}_{x\,y}\backslash\Sigma(\mathcal{R})\\ &&&&\\ (x,y)&\longmapsto&(\mathcal{G}(x,y),\mathcal{H}(x,y))&\longmapsto&\left(\frac{M(t,\mathfrak{c})}{N(t,\mathfrak{c})},\frac{S(t,\mathfrak{c})}{T(t,\mathfrak{c})}\right),\end{array} |  | (38) |

where Σ ( ℛ) ≐ { 𝒢 x ℋ y − 𝒢 y ℋ x = 0 } ⊂ ℂ x ​ y 2 \Sigma(\mathcal{R})\doteq\{\mathcal{G}_{x}\mathcal{H}_{y}-\mathcal{G}_{y}\mathcal{H}_{x}=0\}\subset\mathbb{C}^{2}_{x\,y} is the ramification locus of ℛ \mathcal{R}, and M M, N N, S S, T T are suitable polynomials. Moreover,

 | ℋ ⁡ ( Σ ⁡ ( ℛ)) ⊂ 𝔅 ⁡ ( ℋ). \mathcal{H}(\Sigma(\mathcal{R}))\subset\mathfrak{B}(\mathcal{H}). |  | (39) |

2. 2)

On ℂ x ​ y 2 \ Σ ⁡ ( ℛ) \mathbb{C}^{2}_{x\,y}\backslash\Sigma(\mathcal{R}), the map ℛ \mathcal{R} rectifies the singular holomorphic foliations d ​ ℋ = 0 d\mathcal{H}=0 and d ​ 𝒢 = 0 d\mathcal{G}=0, as follows

 | ℛ ∗ ​ ( d ​ ℋ ​ ( x, y)) = d ​ 𝔠 and ℛ ∗ ​ ( d ​ 𝒢 ​ ( x, y)) = d ​ t. \mathcal{R}_{*}(d\mathcal{H}(x,y))=d\mathfrak{c}\quad\hbox{ and }\quad\mathcal{R}_{*}(d\mathcal{G}(x,y))=dt. |  | (40) |

3. 3)

For each generic value 𝔠 ∈ ℂ \ 𝔅 ⁡ ( ℋ) \mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H}) of ℋ \mathcal{H}, the map ℛ \mathcal{R} rectifies the corresponding fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} biholomorphically into the punctured horizontal line

 | ℂ \ { 0, β 1, …, β r − 1, 𝔠 } × { 𝔠 }, ℂ \ { 0, β 1, …, β r − 1 } × { 𝔠 }, or ​ ℂ \ { β 1, …, β r − 1 } × { 𝔠 } \begin{array}[]{c}\mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1},\mathfrak{c}\}\times\{\mathfrak{c}\},\ \ \ \ \mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1}\}\times\{\mathfrak{c}\},\\ \\ \ \hbox{ or }\ \mathbb{C}\backslash\{\beta_{1},\ldots,\beta_{r-1}\}\times\{\mathfrak{c}\}\end{array} |  | (41) |

in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}, associated to the families 𝔉 1 \mathfrak{F}_{1}, 𝔉 2 \mathfrak{F}_{2}, 𝔉 3 \mathfrak{F}_{3}, respectively.

Figure 1 illustrates the rectified foliations on ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}.

###### Proof.

We begin by recalling in Table 1 the expressions ( 𝒢, ℋ) (\mathcal{G},\mathcal{H}) that define the maps ℛ \mathcal{R}.

 | 𝒢 \mathcal{G} | ℋ \mathcal{H} |

ℋ ∈ 𝔉 1, r ≥ 1 \mathcal{H}\in\mathfrak{F}_{1},\ r\geq 1 | x q 1 ​ 𝒮 ​ ( x, y) q x^{q_{1}}\mathcal{S}(x,y)^{q} | 𝒢 ⁡ ( x, y) + x p 1 ​ 𝒮 ​ ( x, y) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − 𝒢 ⁡ ( x, y)) a 𝚒 \mathcal{G}(x,y)+x^{p_{1}}\mathcal{S}(x,y)^{p}\prod_{{\tt i}=1}^{r-1}\big(\beta_{\tt i}-\mathcal{G}(x,y)\big)^{a_{\tt i}} |

ℋ ∈ 𝔉 2, r ≥ 1 \mathcal{H}\in\mathfrak{F}_{2},\ r\geq 1 | x q 1 ​ 𝒮 ​ ( x, y) q x^{q_{1}}\mathcal{S}(x,y)^{q} | x p 1 ​ 𝒮 ​ ( x, y) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − 𝒢 ⁡ ( x, y)) a 𝚒 x^{p_{1}}\mathcal{S}(x,y)^{p}\prod_{{\tt i}=1}^{r-1}\big(\beta_{\tt i}-\mathcal{G}(x,y)\big)^{a_{\tt i}} |

ℋ ∈ 𝔉 3, r ≥ 2 \mathcal{H}\in\mathfrak{F}_{3},\ r\geq 2 | x x | y ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − 𝒢 ⁡ ( x, y)) a 𝚒 − h ⁡ ( x) y\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\mathcal{G}(x,y)\right)^{a_{\tt i}}-h(x) |

Table 1. Components of the rectifying map ℛ = ( 𝒢, ℋ) \mathcal{R}=(\mathcal{G},\mathcal{H}).

Since ℛ \mathcal{R} is a rational map, some fibers of ℋ \mathcal{H} a priori can be contracted, our interest is in the behavior under ℛ \mathcal{R} of the generic fibers. If we prove equation ( 39), then ℛ \mathcal{R} will map each generic fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ \mathcal{H} into a horizontal line in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}, which has punctures because ℋ \mathcal{H} is of type ( 0, κ) (0,\kappa) with κ ≥ 2 \kappa\geq 2. The proof of equation ( 39) is as follows. In Table 2, we provided the expression of the ramification locus Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) of ℛ \mathcal{R}. By using the last column of Tables 1 and 2, we then obtained ℋ ⁡ ( Σ ⁡ ( ℛ)) \mathcal{H}(\Sigma(\mathcal{R})), which appears in Table 3.

 | Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) |

ℋ ∈ 𝔉 1 ∪ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{1}\cup\mathfrak{F}_{2} | { x k + p 1 + q 1 − 1 𝒮 ( x, y) p + q − 1 ∏ 𝚒 = 1 r − 1 ( β 𝚒 − 𝒢 ( x, y)) a 𝚒 = 0 } \big\{x^{k+p_{1}+q_{1}-1}\mathcal{S}(x,y)^{p+q-1}\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\mathcal{G}(x,y)\right)^{a_{\tt i}}=0\big\} |

ℋ ∈ 𝔉 3, r ≥ 2 \mathcal{H}\in\mathfrak{F}_{3},\ r\geq 2 | { ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x) a 𝚒 = 0 } \big\{\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-x\right)^{a_{\tt i}}=0\big\} |

Table 2. Computation of the critical set Σ ⁡ ( ℛ) \Sigma(\mathcal{R}).

 |  | ℋ ⁡ ( Σ ⁡ ( ℛ)) \mathcal{H}(\Sigma(\mathcal{R})) |

ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1} | p 1, q 1 ≥ 1 p_{1},q_{1}\geq 1 | { 0, β 1, …, β r − 1 } \{0,\beta_{1},\ldots,\beta_{r-1}\} |

 | q 1 = 0 q_{1}=0 | { P ⁡ ( 0), 0, β 1, …, β r − 1 } \{P(0),0,\beta_{1},\ldots,\beta_{r-1}\} |

 | p 1 = 0 p_{1}=0 | { P ⁡ ( 0) ​ ∏ 𝚒 = 1 r − 1 β 𝚒 a 𝚒, 0, β 1, …, β r − 1 } \big\{P(0)\prod_{{\tt i}=1}^{r-1}\beta_{\tt i}^{a_{\tt i}},0,\beta_{1},\ldots,\beta_{r-1}\big\} |

ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2} | p 1 ≥ 1 p_{1}\geq 1 | { 0 } \{0\} |

 | p 1 = 0 p_{1}=0 | { P ⁡ ( 0) ​ ∏ 𝚒 = 1 r − 1 β 𝚒 a 𝚒, 0 } \big\{P(0)\prod_{{\tt i}=1}^{r-1}\beta_{\tt i}^{a_{\tt i}},0\big\} |

ℋ ∈ 𝔉 3, r ≥ 2 \mathcal{H}\in\mathfrak{F}_{3},\ r\geq 2 |  | { h ⁡ ( β 1), …, h ⁡ ( β r − 1) } \left\{h(\beta_{1}),\ldots,h(\beta_{r-1})\right\} |

Table 3. Image of Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) under ℋ \mathcal{H}.

Assume that ℋ ⁡ ( x, y) ∈ 𝔉 1. \mathcal{H}(x,y)\in\mathfrak{F}_{1}. Since p, q ≥ 1 p,q\geq 1, the polynomial 𝒮 ⁡ ( x, y) \mathcal{S}(x,y) divides ℋ ⁡ ( x, y) \mathcal{H}(x,y). Moreover, for each 𝚒 = 1, …, r − 1 {\tt i}=1,\ldots,r-1, we have that β 𝚒 − 𝒢 ⁡ ( x, y) \beta_{\tt i}-\mathcal{G}(x,y) divides ℋ ⁡ ( x, y) − β 𝚒 \mathcal{H}(x,y)-\beta_{\tt i}. That implies that { 0, β 1, …, β r − 1 } ⊂ 𝔅 ⁡ ( ℋ) \{0,\beta_{1},\ldots,\beta_{r-1}\}\subset\mathfrak{B}(\mathcal{H}). In addition, if q 1 = 0 q_{1}=0, then p 1 = 1 p_{1}=1. Furthermore, x x divides 𝒢 ⁡ ( x, y) − P ⁡ ( 0) \mathcal{G}(x,y)-P(0), which implies that x x divides ℋ ⁡ ( x, y) − P ⁡ ( 0) \mathcal{H}(x,y)-P(0), whence P ⁡ ( 0) ∈ 𝔅 ⁡ ( ℋ) P(0)\in\mathfrak{B}(\mathcal{H}). If p 1 = 0 p_{1}=0, then p = q 1 = 1 p=q_{1}=1 and x x divides 𝒮 ⁡ ( x, y) ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − 𝒢 ⁡ ( x, y)) a 𝚒 − P ⁡ ( 0) ​ ∏ 𝚒 = 1 r − 1 β 𝚒 a 𝚒 \mathcal{S}(x,y)\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-\mathcal{G}(x,y)\right)^{a_{\tt i}}-P(0)\prod_{{\tt i}=1}^{r-1}\beta_{\tt i}^{a_{\tt i}}, which implies that x x divides ℋ ⁡ ( x, y) − P ⁡ ( 0) ​ ∏ 𝚒 = 1 r − 1 β 𝚒 a 𝚒 \mathcal{H}(x,y)-P(0)\prod_{{\tt i}=1}^{r-1}\beta_{\tt i}^{a_{\tt i}}, from which P ⁡ ( 0) ​ ∏ 𝚒 = 1 r − 1 β 𝚒 a 𝚒 ∈ 𝔅 ⁡ ( ℋ) P(0)\prod_{{\tt i}=1}^{r-1}\beta_{\tt i}^{a_{\tt i}}\in\mathfrak{B}(\mathcal{H}). This proves that if ℋ ⁡ ( x, y) ∈ 𝔉 1 \mathcal{H}(x,y)\in\mathfrak{F}_{1}, then ℋ ⁡ ( Σ ⁡ ( ℛ)) ⊂ 𝔅 ⁡ ( ℋ) \mathcal{H}(\Sigma(\mathcal{R}))\subset\mathfrak{B}(\mathcal{H}).

Analogously, we can prove this last property for ℋ ⁡ ( x, y) ∈ 𝔉 2 \mathcal{H}(x,y)\in\mathfrak{F}_{2} and ℋ ⁡ ( x, y) ∈ 𝔉 3 \mathcal{H}(x,y)\in\mathfrak{F}_{3}.

In order to compute the explicit inverse map ℛ − 1 \mathcal{R}^{-1}, we use t = 𝒢 ⁡ ( x, y) t=\mathcal{G}(x,y) and 𝔠 = ℋ ⁡ ( x, y). \mathfrak{c}=\mathcal{H}(x,y). We start with the simplest case in which ℋ ∈ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{3} and 𝒢 ⁡ ( x, y) = x \mathcal{G}(x,y)=x. We then have t = x t=x and 𝔠 = y ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x) a 𝚒 + h ⁡ ( x) \mathfrak{c}=y\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-x\right)^{a_{\tt i}}+h(x), from which we get

 | x = t and y = 𝔠 − h ⁡ ( t) ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) a 𝚒. x=t\quad\mbox{ and }\quad y=\frac{\mathfrak{c}-h(t)}{\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-t\right)^{a_{\tt i}}}. |  |

In this case, Σ ( ℛ) = { ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x) = 0 } \Sigma(\mathcal{R})=\{\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-x\right)=0\}, 𝔇 = { ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) = 0 } \mathfrak{D}=\{\prod_{{\tt i}=1}^{r-1}\left(\beta_{\tt i}-t\right)=0\} and ℛ − 1 \mathcal{R}^{-1} is well defined in ℂ t ​ 𝔠 2 \ 𝔇 \mathbb{C}^{2}_{t\,\mathfrak{c}}\backslash\mathfrak{D}. In addition, equation ( 38) takes the explicit form

 | ℂ x ​ y 2 \ Σ ⁡ ( ℛ) → ℛ ℂ t ​ 𝔠 2 \ 𝔇 ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℛ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( t, 𝔠 + h ⁡ ( t) ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) a 𝚒). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\mathfrak{D}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})\\ &&&&\\ (x,y)&\longmapsto&(\mathcal{G}(x,y),\mathcal{H}(x,y))&\longmapsto&\left(t,\dfrac{\mathfrak{c}+h(t)}{\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-t)^{a_{\tt i}}}\right).\end{array} |  | (42) |

Thus, each generic fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ \mathcal{H} is biholomorphically mapped into the punctured horizontal line

 | ( ℂ \ { β 1, …, β r − 1 }) × { 𝔠 }. \big(\mathbb{C}\backslash\{\beta_{1},\ldots,\beta_{r-1}\}\big)\times\{\mathfrak{c}\}. |  |

Analogously, straightforward computations show that for ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2} and p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1, we obtain

 | ℂ x ​ y 2 \ Σ ⁡ ( ℛ) → ℛ ℂ t ​ 𝔠 2 \ 𝔇 ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℛ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( t p ​ Π ​ ( t) q 𝔠 q, 𝔠 q ​ S 1 ​ ( t, 𝔠) t p ​ k + p 1 ​ Π ​ ( t) q ​ k + q 1), \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\mathfrak{D}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})\\ &&&&\\ (x,y)&\longmapsto&\big(\mathcal{G}(x,y),\mathcal{H}(x,y)\big)&\longmapsto&\left(\dfrac{t^{p}\Pi(t)^{q}}{\mathfrak{c}^{q}},\dfrac{\mathfrak{c}^{q}S_{1}(t,\mathfrak{c})}{t^{pk+p_{1}}\Pi(t)^{qk+q_{1}}}\right),\end{array} |  | (43) |

where 𝒢 ⁡ ( x, y) \mathcal{G}(x,y) is in Table 1, Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) is in Table 2, whence 𝔇 = { 𝔠 t Π ( t) = 0 }, \mathfrak{D}=\{\mathfrak{c}\,t\,\Pi(t)=0\},

 | Π ⁡ ( t) ≐ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) a 𝚒 \Pi(t)\doteq\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-t)^{a_{\tt i}} |  | (44) |

and

 | S 1 ​ ( t, 𝔠) ≐ 𝔠 q ⁡ ( k − 1) ​ ( 𝔠 q 1 + t p 1 ​ Π ​ ( t) q 1 ​ P ​ ( t p ​ Π ​ ( t) q ​ 𝔠 − q)), S_{1}(t,\mathfrak{c})\doteq\mathfrak{c}^{q(k-1)}\Big(\mathfrak{c}^{q_{1}}+t^{p_{1}}\Pi(t)^{q_{1}}P\left(t^{p}\Pi(t)^{q}\mathfrak{c}^{-q}\right)\Big), |  | (45) |

which is polynomial because P P has degree at most k − 1 k-1. Thus, each generic fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2} is biholomorphically mapped into the punctured horizontal line

 | ( ℂ \ { 0, β 1, …, β r − 1 }) × { 𝔠 }. \big(\mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1}\}\big)\times\{\mathfrak{c}\}. |  |

For ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1} and p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1, we obtain

 | ℂ x ​ y 2 \ Σ ⁡ ( ℛ) → ℛ ℂ t ​ 𝔠 2 \ 𝔇 ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℛ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( t p ​ Π ​ ( t) q ( 𝔠 − t) q, ( 𝔠 − t) q ​ S 2 ​ ( t, 𝔠) t p ​ k + p 1 ​ Π ​ ( t) q ​ k + q 1). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\mathfrak{D}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})\\ &&&&\\ (x,y)&\longmapsto&\big(\mathcal{G}(x,y),\mathcal{H}(x,y)\big)&\longmapsto&\left(\dfrac{t^{p}\Pi(t)^{q}}{(\mathfrak{c}-t)^{q}},\dfrac{(\mathfrak{c}-t)^{q}S_{2}(t,\mathfrak{c})}{t^{pk+p_{1}}\Pi(t)^{qk+q_{1}}}\right).\end{array} |  | (46) |

The elements are 𝒢 ⁡ ( x, y) \mathcal{G}(x,y) in Table 1, Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) in Table 2, 𝔇 = { ( 𝔠 − t) t Π ( t) = 0 } \mathfrak{D}=\{(\mathfrak{c}-t)\,t\,\Pi(t)=0\} and

 | S 2 ​ ( t, 𝔠) ≐ ( 𝔠 − t) q ⁡ ( k − 1) ​ ( ( 𝔠 − t) q 1 + t p 1 ​ Π ​ ( t) q 1 ​ P ​ ( t p ​ Π ​ ( t) q ​ ( 𝔠 − t) − q)), S_{2}(t,\mathfrak{c})\doteq(\mathfrak{c}-t)^{q(k-1)}\Big((\mathfrak{c}-t)^{q_{1}}+t^{p_{1}}\Pi(t)^{q_{1}}P\left(t^{p}\Pi(t)^{q}(\mathfrak{c}-t)^{-q}\right)\Big), |  | (47) |

which is polynomial because P P has degree at most k − 1 k-1. Thus, each generic fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1} is biholomorphically mapped into the punctured horizontal line

 | ( ℂ \ { 0, β 1, …, β r − 1, 𝔠 }) × { 𝔠 }. \big(\mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1},\mathfrak{c}\}\big)\times\{\mathfrak{c}\}. |  |

For ℋ ∈ 𝔉 1 ∪ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{1}\cup\mathfrak{F}_{2} and p ​ q 1 − q ​ p 1 = − 1 pq_{1}-qp_{1}=-1, we obtain expressions similar to ( 43) and ( 46). See ( 96) and ( 99) for details. This completes the proof of statement 1).

Let 𝒳 𝒢 \mathcal{X}_{\mathcal{G}} and 𝒳 ℋ \mathcal{X}_{\mathcal{H}} be the Hamiltonian vector fields associated with 𝒢 \mathcal{G} and ℋ \mathcal{H}, respectively. These vector fields satisfy the following identities:

 | ℛ ∗ ​ ( 𝒳 𝒢 𝒢 x ​ ℋ y − 𝒢 y ​ ℋ x) = 1 𝒢 x ​ ℋ y − 𝒢 y ​ ℋ x ​ ( 𝒢 x 𝒢 y ℋ x ℋ y) ​ ( − 𝒢 y 𝒢 x) = ∂ ∂ 𝔠 \mathcal{R}_{*}\left(\frac{\mathcal{X}_{\mathcal{G}}}{\mathcal{G}_{x}\mathcal{H}_{y}-\mathcal{G}_{y}\mathcal{H}_{x}}\right)=\frac{1}{\mathcal{G}_{x}\mathcal{H}_{y}-\mathcal{G}_{y}\mathcal{H}_{x}}\left(\begin{matrix}\mathcal{G}_{x}&\mathcal{G}_{y}\\ \mathcal{H}_{x}&\mathcal{H}_{y}\end{matrix}\right)\left(\begin{matrix}-\mathcal{G}_{y}\\ \mathcal{G}_{x}\end{matrix}\right)=\frac{\partial}{\partial\mathfrak{c}} |  | (48) |

and

 | ℛ ∗ ​ ( 𝒳 ℋ 𝒢 x ​ ℋ y − 𝒢 y ​ ℋ x) = 1 𝒢 x ​ ℋ y − 𝒢 y ​ ℋ x ​ ( 𝒢 x 𝒢 y ℋ x ℋ y) ​ ( − ℋ y ℋ x) = − ∂ ∂ t. \mathcal{R}_{*}\left(\frac{\mathcal{X}_{\mathcal{H}}}{\mathcal{G}_{x}\mathcal{H}_{y}-\mathcal{G}_{y}\mathcal{H}_{x}}\right)=\frac{1}{\mathcal{G}_{x}\mathcal{H}_{y}-\mathcal{G}_{y}\mathcal{H}_{x}}\left(\begin{matrix}\mathcal{G}_{x}&\mathcal{G}_{y}\\ \mathcal{H}_{x}&\mathcal{H}_{y}\end{matrix}\right)\left(\begin{matrix}-\mathcal{H}_{y}\\ \mathcal{H}_{x}\end{matrix}\right)=-\frac{\partial}{\partial t}. |  | (49) |

Clearly, the above equations ( 48) and ( 49) prove assertion 2).

Finally, statement 3) also follows from identities ( 48) and ( 49), together with the proof of statement 1). ∎

###### Remark 6.

As a fortunate geometric situation, the punctures in the horizontal lines ℛ ⁡ ( ℒ 𝔠) \mathcal{R}(\mathcal{L}_{\mathfrak{c}}) determine an arrangement of lines 𝒜 ι \mathcal{A}_{\iota} for each family 𝔉 ι \mathfrak{F}_{\iota}, as follows:

 | 𝒜 1 ≐ ∪ 𝚒 = 𝟶 r { t = β 𝚒 } ⊂ ℂ t ​ 𝔠 2, with β 0 = 0, β r = 𝔠, \mathcal{A}_{1}\doteq\cup_{\tt i=0}^{r}\{t=\beta_{\tt i}\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}},\quad\mbox{with $\beta_{0}=0$, $\beta_{r}=\mathfrak{c}$}, |  |

 | 𝒜 2 ≐ ∪ 𝚒 = 𝟶 r − 1 { t = β 𝚒 } ⊂ ℂ t ​ 𝔠 2 and 𝒜 3 ≐ ∪ 𝚒 = 𝟷 r − 1 { t = β 𝚒 } ⊂ ℂ t ​ 𝔠 2, \mathcal{A}_{2}\doteq\cup_{\tt i=0}^{r-1}\{t=\beta_{\tt i}\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}\quad\hbox{and}\quad\mathcal{A}_{3}\doteq\cup_{\tt i=1}^{r-1}\{t=\beta_{\tt i}\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}, |  |

see Figure 1. For notational simplicity, we will omit the subscript ι = 1, 2, 3 \iota=1,2,3 in 𝒜 ι \mathcal{A}_{\iota}.

ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1} |  | ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2} |  | ℋ ∈ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{3} |

 |  |  |  |  |

Figure 1. Sketch of the global rectifications of the singular holomorphic foliations d ​ ℋ = 0 d\mathcal{H}=0 under ℛ: ℂ x ​ y 2 ⇢ ℂ t ​ 𝔠 2 \mathcal{R}\colon\mathbb{C}^{2}_{x\,y}\dashrightarrow\mathbb{C}^{2}_{t\,\mathfrak{c}}, for the Neumann–Norbury families 𝔉 1 \mathfrak{F}_{1}, 𝔉 2 \mathfrak{F}_{2} and 𝔉 3 \mathfrak{F}_{3}. The blue horizontal lines are the image under ℛ \mathcal{R} of the generic fibers of ℋ \mathcal{H}. The dashed (red and green) lines have been removed from ℂ t ​ 𝔠 2 \mathbb{C}_{t\,\mathfrak{c}}^{2} so that ℛ − 1 \mathcal{R}^{-1} is well defined. The green lines correspond to the arrangement 𝒜 \mathcal{A} and determine punctures in the blue horizontal lines. The magenta horizontal lines are the image under ℛ \mathcal{R} of some connected components of singular fibers coming from values in the bifurcation set 𝔅 ⁡ ( ℋ) = { 𝔠 1, 𝔠 2, …, 𝔠 h } \mathfrak{B}(\mathcal{H})=\{\mathfrak{c}_{1},\mathfrak{c}_{2},\ldots,\mathfrak{c}_{h}\}.

### 4.4. Rational invariance of the weak infinitesimal Hilbert’s 16th problem

According to our Program, below we provide the accurate statement about the ℛ \mathcal{R} -equivalence between the differential equations given in ( 20) and ( 21), as well as between the corresponding Abelian integrals ( 22) and their number of zeros ( 23). In fact, the following result remains true without the hypothesis of trivial global monodromy.

###### Corollary 15 (Rational invariance of the weak infinitesimal Hilbert’s 16th problem).

Consider ℋ ⁡ ( x, y) ∈ 𝔉 1 ∪ 𝔉 2 ∪ 𝔉 3 \mathcal{H}(x,y)\in\mathfrak{F}_{1}\cup\mathfrak{F}_{2}\cup\mathfrak{F}_{3} a primitive polynomial with trivial global monodromy in normal form and a polynomial 1-form ϑ ∈ Ω 1 ​ ( ℂ x ​ y 2) \vartheta\in\varOmega^{1}(\mathbb{C}_{x\,y}^{2}). Let ℛ \mathcal{R} be the rational rectifying map for ℋ ⁡ ( x, y) \mathcal{H}(x,y) and let η = ℛ ∗ ​ ( ϑ) \eta=\mathcal{R}_{*}(\vartheta).

1. 1)

The corresponding infinitesimal perturbed Hamiltonian differential equations are rationally equivalent, that is,

 | ℛ ∗ ​ ( d ​ ℋ + ε ​ ϑ) = d ​ 𝔠 + ε ​ η. \mathcal{R}_{*}(d\mathcal{H}+\varepsilon\vartheta)=d\mathfrak{c}+\varepsilon\eta. |  |

2. 2)

The Abelian integrals

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ ⁡ ( 𝔠) ϑ: ℂ \ 𝔅 ⁡ ( ℋ) ⟶ ℂ \mathcal{I}_{\tt i}(\mathfrak{c})=\displaystyle\int_{\delta(\mathfrak{c})}\vartheta:\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\longrightarrow\mathbb{C} |  |

and

 | J ( 𝔠) = ∫ α ⁡ ( 𝔠) η: ℂ \ 𝔅 ( ℋ) ⟶ ℂ, η = ℛ ∗ ​ ( ϑ), α ⁡ ( 𝔠) = ℛ ⁡ ( δ ⁡ ( 𝔠)) J(\mathfrak{c})=\displaystyle\int_{\alpha(\mathfrak{c})}\eta:\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\longrightarrow\mathbb{C},\quad\mbox{$\eta=\mathcal{R}_{*}(\vartheta)$, $\quad\alpha(\mathfrak{c})=\mathcal{R}\big(\delta(\mathfrak{c})\big)$} |  | (50) |

are rationally equivalent; moreover,

 | ℐ ⁡ ( 𝔠) = J ⁡ ( 𝔠) for all ​ 𝔠 ∈ ℂ 𝔠 \ 𝔅 ⁡ ( ℋ). \mathcal{I}(\mathfrak{c})=J(\mathfrak{c})\quad\mbox{ for all }\mathfrak{c}\in\mathbb{C}_{\mathfrak{c}}\backslash\mathfrak{B}(\mathcal{H}). |  |

3. 3)

The number of isolated zeros, counted with multiplicities, of ℐ ⁡ ( 𝔠) \mathcal{I}(\mathfrak{c}) and of J ⁡ ( 𝔠) J(\mathfrak{c}) in ℂ 𝔠 \ 𝔅 ⁡ ( ℋ) \mathbb{C}_{\mathfrak{c}}\backslash\mathfrak{B}(\mathcal{H}) is the same

 | Z ⁡ ( ℐ ⁡ ( 𝔠)) = Z ⁡ ( J ⁡ ( 𝔠)). Z(\mathcal{I}(\mathfrak{c}))=Z(J(\mathfrak{c})). |  |

###### Proof.

The first assertion follows immediately from the definition of η \eta and equation ( 40). The second and third assertions follow from the construction of J ⁡ ( 𝔠) J(\mathfrak{c}) and the diagram

 | ℂ 𝔠 {\lx@inpgf@ignorespaces\mathbb{C}_{\mathfrak{c}}\,} ℂ 𝔠 ⊂ ℂ t ​ 𝔠 2 {\lx@inpgf@ignorespaces\;\mathbb{C}_{\mathfrak{c}}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}} ℂ. {\lx@inpgf@ignorespaces\mathbb{C}.} ℐ \scriptstyle{\lx@inpgf@ignorespaces\mathcal{I}} J \scriptstyle{\lx@inpgf@ignorespaces J} |  | (51) |

∎

Therefore, Corollaries 5 and 15 yield our diagram ( 25).

The Abelian integral J ⁡ ( 𝔠) J(\mathfrak{c}), should be understood as a family of integrals of rational 1-forms on the complex lines of the horizontal foliation d ​ 𝔠 = 0 d\mathfrak{c}=0. Thus, we will apply the residue theorem to compute J ⁡ ( 𝔠) J(\mathfrak{c}) explicitly.

### 4.5. Non-exact 1-forms, canonical basis and the associated Abelian integrals

We know that if ϑ ∈ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}} is an exact 1 1 -form, then the infinitesimal perturbed Hamiltonian differential equation d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0 is actually a Hamiltonian differential equation, whose dynamics is well-understood and the corresponding Abelian integrals vanish identically. Hence, the present subject considers non-exact polynomial 1 1 -forms.

As usual, d ​ ℂ ​ [x, y] ≤ 𝔫 + 1 d\,\mathbb{C}[x,y]_{\leq\mathfrak{n}+1} denotes the *vector space of exact polynomial 1-forms with degree at most 𝔫 \mathfrak{n}*, they provide the exact perturbations for the Hamiltonian equations. Hence, it is sufficient to consider Abelian integrals for polynomial 1-forms in the *vector space of non-exact polynomial 1-forms on ℂ x ​ y 2 \mathbb{C}^{2}_{x\,y} of degree at most 𝔫 \mathfrak{n}*, say

 | Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 ≐ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 d ​ ℂ ​ [x, y] ≤ 𝔫 + 1. \varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}\doteq\dfrac{\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}}{d\,\mathbb{C}[x,y]_{\leq\mathfrak{n}+1}}. |  |

###### Lemma 16.

The set

 | B n ​ e 1 ( ℂ x ​ y 2, 𝔫) ≐ { ϑ i ​ j = x i y j d x | j ∈ 1, 2, …, 𝔫; i ∈ 0, 1, …, 𝔫 − j } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})\doteq\left\{\vartheta_{ij}=x^{i}y^{j}\,dx\ |\ j\in 1,2,\ldots,\mathfrak{n};\ i\in 0,1,\ldots,\mathfrak{n}-j\right\} |  | (52) |

is a basis for the vector space of non-exact polynomial 1-forms Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}.

###### Proof.

Let

 | ϑ = ∑ i + j = 0 𝔫 a i ​ j ​ x i ​ y j ​ d ​ x + ∑ i + j = 0 𝔫 b i ​ j ​ x i ​ y j ​ d ​ y ∈ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta=\sum_{i+j=0}^{\mathfrak{n}}a_{ij}x^{i}y^{j}\,dx+\sum_{i+j=0}^{\mathfrak{n}}b_{ij}x^{i}y^{j}\,dy\in\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}} |  |

be a non–exact 1-form. We have that

 | b i ​ j ​ x i ​ y j ​ d ​ y = d ⁡ ( b i ​ j ​ x i ​ y j + 1 j + 1) − i ​ b i ​ j j + 1 ​ x i − 1 ​ y j + 1 ​ d ​ x. b_{ij}x^{i}y^{j}\,dy=d\left(\frac{b_{ij}x^{i}y^{j+1}}{j+1}\right)-\frac{ib_{ij}}{j+1}x^{i-1}y^{j+1}\,dx. |  |

Hence, ϑ \vartheta can be written as

 | ϑ = ∑ i + j = 0 𝔫 a i ​ j ​ x i ​ y j ​ d ​ x + d ⁡ ( ∑ i + j = 0 𝔫 b i ​ j ​ x i ​ y j + 1 j + 1) − ∑ i + j = 0 𝔫 i ​ b i ​ j j + 1 ​ x i − 1 ​ y j + 1 ​ d ​ x. \vartheta=\sum_{i+j=0}^{\mathfrak{n}}a_{ij}x^{i}y^{j}\,dx+d\left(\sum_{i+j=0}^{\mathfrak{n}}\frac{b_{ij}x^{i}y^{j+1}}{j+1}\right)-\sum_{i+j=0}^{\mathfrak{n}}\frac{ib_{ij}}{j+1}x^{i-1}y^{j+1}\,dx. |  |

By reordering terms, we get

 | ϑ = d ​ ( ∑ i = 0 𝔫 a i ​ 0 ​ x i + 1 i + 1 + ∑ i + j = 0 𝔫 b i ​ j ​ x i ​ y j + 1 j + 1) ⏟ Q ⁡ ( x, y) + ∑ j = 1 𝔫 ∑ i = 0 𝔫 − j a ~ i ​ j ​ ( x i ​ y j ​ d ​ x) ⏟ ϑ i ​ j, \vartheta=d\underbrace{\left(\sum_{i=0}^{\mathfrak{n}}\frac{a_{i0}x^{i+1}}{i+1}+\sum_{i+j=0}^{\mathfrak{n}}\frac{b_{ij}x^{i}y^{j+1}}{j+1}\right)}_{Q(x,y)}+\sum_{j=1}^{\mathfrak{n}}\sum_{i=0}^{\mathfrak{n}-j}\tilde{a}_{ij}\underbrace{\Big(x^{i}y^{j}\,dx\Big)}_{\vartheta_{ij}}, |  | (53) |

where Q ⁡ ( x, y) ∈ ℂ ​ [x, y] ≤ 𝔫 + 1 Q(x,y)\in\mathbb{C}[x,y]_{\leq\mathfrak{n}+1}. The classes in the quotient arising from the 1-forms ϑ i ​ j \vartheta_{ij} provide the required basis. ∎

###### Remark 7.

Clearly, the basis in ( 52) is “symmetric” with respect to the choice of the variable x x or y y. Thus, we would also consider the basis

 | { x i y j d y | i ∈ 1, 2, …, 𝔫; j ∈ 0, 1, …, 𝔫 − i }. \left\{x^{i}y^{j}\,dy\ |\ i\in 1,2,\ldots,\mathfrak{n};\ j\in 0,1,\ldots,\mathfrak{n}-i\right\}. |  |

Until now, we know that if H H is primitive polynomial with trivial global monodromy, then the infinitesimal perturbed Hamiltonian differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 is transformed, through a suitable pair ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}), into the differential equation d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0, where ϑ = σ ′ ​ ψ ∗ ​ ( ω) \vartheta=\sigma^{\prime}\psi_{*}(\omega) and ℋ \mathcal{H} is the normal form of H H in the families 𝔉 1 ∪ 𝔉 2 ∪ 𝔉 3 \mathfrak{F}_{1}\cup\mathfrak{F}_{2}\cup\mathfrak{F}_{3}. Moreover, by using the rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} the last differential equation is transformed into the rational differential equation d ​ 𝔠 + ε ​ η = 0, d\mathfrak{c}+\varepsilon\eta=0, with η = ℛ ∗ ​ ( ϑ) \eta=\mathcal{R}_{*}(\vartheta). These simplifications allow us to prove the existence of global generators for the fundamental group of the generic leaves of the singular holomorphic foliations.

Let L c L_{c} be a generic fiber of H H, this is biholomorphic to a generic fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ \mathcal{H}. By recalling diagram ( 25), the rectifying map ℛ \mathcal{R} and equation ( 27), the generic fiber ℒ 𝔠 0 \mathcal{L}_{\mathfrak{c}_{0}} of ℋ \mathcal{H} is biholomorphic to the Riemann sphere ℂ ^ \widehat{\mathbb{C}} with 𝔯 + 1 ≥ 2 \mathfrak{r}+1\geq 2 punctures.

Notation. Fix the generic rectified leaf { 𝔠 = 𝔠 0 } \{\mathfrak{c}=\mathfrak{c}_{0}\} given by ℛ ⁡ ( ℒ 𝔠 0) \mathcal{R}(\mathcal{L}_{\mathfrak{c}_{0}}). We compactify and make the corresponding punctures of { 𝔠 = 𝔠 0 } \{\mathfrak{c}=\mathfrak{c}_{0}\}, obtaining the punctured rectified fiber ℂ ^ \ { 𝔯 + 1 ​ punctures } \widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\}. Let

 | { α 𝚒 ( 𝔠 0) | 𝚒 ∈ 1, …, 𝔯 + 1 } \{\alpha_{\tt i}(\mathfrak{c}_{0})\ |\ {\tt i}\in 1,\ldots,\mathfrak{r}+1\} |  | (54) |

be simple paths in ℂ ^ \ { 𝔯 + 1 ​ punctures } \widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\}, which enclose, with anti-clockwise orientation, exactly one of the punctures. We convene that, α 𝔯 + 1 \alpha_{\mathfrak{r}+1} encloses the puncture at infinity of the punctured rectified fiber.

The associated presentation of the first homotopy group of the punctured rectified fiber (with generators and relations) is

 | π 1 ( ℂ ^ \ { 𝔯 + 1 punctures }) = { α 𝚒 | α 1 ⋯ α 𝔯 = α 𝔯 + 1 − 1, 𝚒 ∈ 1, …, 𝔯 + 1 }, \pi_{1}(\widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\})=\{\,\alpha_{\tt i}\ |\ \alpha_{1}\cdots\alpha_{\mathfrak{r}}=\alpha_{\mathfrak{r+1}}^{-1}\,,\ \ {\tt i}\in 1,\ldots,\mathfrak{r}+1\}, |  |

isomorphic to the free group in 𝔯 \mathfrak{r} generators. Let

𝒜 ​ b: π 1 ​ ( ℂ ^ \ { 𝔯 + 1 ​ punctures }) ⟶ H 1 ​ ( ℂ ^ \ { 𝔯 + 1 ​ punctures }, ℤ) \mathcal{A}b:\pi_{1}\big(\widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\}\big)\longrightarrow H_{1}\big(\widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\},\mathbb{Z}\big)

be the abelianization of the fundamental groups, 𝒜 ​ b \mathcal{A}b is a canonical morphism of groups (an epimorphism when 𝔯 + 1 ≥ 3 \mathfrak{r}+1\geq 3). By abuse of notation, 𝒜 ​ b \mathcal{A}b will denotes the analogous morphism for the fundamental group of any Riemann surface. According to the Program and the Diagram ( 25), we extend the above cycles to all the generic fibers of ℋ \mathcal{H} and H H in an accurate way.

###### Proposition 17 (Canonical global generators).

1. 1)

For the generic values 𝔠 \mathfrak{c},

 | B C ( 𝔠) ≐ { α 𝚒 ( 𝔠) | 𝚒 ∈ 1, …, 𝔯 } BC(\mathfrak{c})\doteq\big\{\alpha_{\tt i}(\mathfrak{c})\ |\ {\tt i}\in 1,\ldots,\mathfrak{r}\big\} |  | (55) |

are canonical global generators for π 1 ​ ( ℂ ^ \ { 𝔯 + 1 ​ punctures }) \pi_{1}\big(\widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\}\big). Where α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) are complex cycles of the rectified holomorphic foliation d ​ 𝔠 = 0 d\mathfrak{c}=0; canonical means that α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) encloses, with anti-clockwise orientation, exactly one of the finite punctures of the rectified fiber.

Moreover, its image { 𝒜 ​ b ​ ( α 𝚒 ​ ( 𝔠)) } \{\mathcal{A}b(\alpha_{\tt i}(\mathfrak{c}))\} is a basis of H 1 ​ ( ℂ ^ \ { 𝔯 + 1 ​ punctures }, ℤ) = ℤ 𝔯 H_{1}\big(\widehat{\mathbb{C}}\backslash\{\mathfrak{r}+1\hbox{ punctures}\},\mathbb{Z}\big)=\mathbb{Z}^{\mathfrak{r}}.

2. 2)

For the generic values 𝔠 \mathfrak{c} of ℋ \mathcal{H},

 | B C ( ℋ) ≐ { δ 𝚒 ( 𝔠) = ℛ − 1 ( α 𝚒 ( 𝔠)) | 𝚒 ∈ 1, …, 𝔯 }, BC(\mathcal{H})\doteq\big\{\delta_{\tt i}(\mathfrak{c})=\mathcal{R}^{-1}(\alpha_{\tt i}(\mathfrak{c}))\ |\ {\tt i}\in 1,\ldots,\mathfrak{r}\big\}, |  | (56) |

are canonical global generators for π 1 ​ ( ℒ 𝔠) \pi_{1}(\mathcal{L}_{\mathfrak{c}}), they are complex cycles of the singular holomorphic foliation d ​ ℋ = 0 d\mathcal{H}=0. The set { 𝒜 ​ b ​ ( δ 𝚒 ​ ( 𝔠)) } \{\mathcal{A}b(\delta_{\tt i}(\mathfrak{c}))\} is a basis of H 1 ​ ( ℒ 𝔠, ℤ) H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z}).

3. 3)

For the generic values c c of H H,

 | B C ( H) ≐ { γ 𝚒 ( c) = ψ − 1 ( δ 𝚒 ( c)) | 𝚒 ∈ 1, …, 𝔯 }, BC(H)\doteq\big\{\gamma_{\tt i}(c)=\psi^{-1}(\delta_{\tt i}(c))\ |\ {\tt i}\in 1,\ldots,\mathfrak{r}\big\}, |  | (57) |

are canonical global generators for π 1 ​ ( L c) \pi_{1}(L_{c}), they are complex cycles of the singular holomorphic foliation d ​ H = 0 dH=0. The set { 𝒜 ​ b ​ ( γ 𝚒 ​ ( c)) } \{\mathcal{A}b(\gamma_{\tt i}(c))\} is a basis of H 1 ​ ( L c, ℤ) H_{1}(L_{c},\mathbb{Z}).

Two essential complex analytic conditions allow the construction of the cycles in the proposition, they are:

∙ \mathchoice{\mathbin{\vbox{\hbox{\scalebox{.8}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{.8}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{.8}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{.8}{$\scriptscriptstyle\bullet$}}}}} There exist canonical orientations in all the fibers of the polynomials H H, ℋ \mathcal{H} and 𝔠 \mathfrak{c}.

∙ \mathchoice{\mathbin{\vbox{\hbox{\scalebox{.8}{$\displaystyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{.8}{$\textstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{.8}{$\scriptstyle\bullet$}}}}}{\mathbin{\vbox{\hbox{\scalebox{.8}{$\scriptscriptstyle\bullet$}}}}} The deep Neumann–Norbury rectification map ℛ \mathcal{R} of the fibers of ℋ \mathcal{H}.

###### Proof.

Recall that, equation ( 27) shows how the number of punctures 𝔯 + 1 \mathfrak{r}+1 depends of the Neumann–Norbury family of H H.

The extension of the homotopy classes in equation ( 54) to ( 55), use that the foliation of d ​ 𝔠 = 0 d\mathfrak{c}=0 is rectified, this shows assertion (1).

The translation from equation ( 55) to ( 56), uses that ℛ \mathcal{R} is a biholomorphism restricted to each generic fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}}. Since ψ \psi is biholomorphism of ℂ 2 \mathbb{C}^{2}, the translation from equation ( 56) to ( 57) follows. ∎

The following extension of the above proposition is useful.

###### Lemma 18.

Let H H be a primitive polynomial with trivial global monodromy. Suppose that L c 0 L_{c_{0}} is a generic fiber of H H and π 1 ​ ( L c 0) ≠ i ​ d \pi_{1}(L_{c_{0}})\neq id. Then, a complex cycle γ ⁡ ( c 0) \gamma(c_{0}) in L c 0 L_{c_{0}} of the singular holomorphic foliation d ​ H = 0 dH=0 uniquely extends to global family of complex cycles { γ ⁡ ( c) | c ∈ ℂ \ 𝔅 ⁡ ( H) } \{\gamma(c)\,|\,c\in\mathbb{C}\backslash\mathfrak{B}(H)\}.

###### Proof.

We use the analogous arguments as in Proposition 17. ∎

The canonical cycle α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) encloses, with anti-clockwise orientation, the puncture ( β 𝚒, 𝔠) ∈ ℂ t ​ 𝔠 2 (\beta_{\tt i},\mathfrak{c})\in\mathbb{C}^{2}_{t\,\mathfrak{c}} in the corresponding punctured rectified line ℛ ⁡ ( ℒ 𝔠) ⊂ ℂ × { 𝔠 } \mathcal{R}(\mathcal{L}_{\mathfrak{c}})\subset\mathbb{C}\times\{\mathfrak{c}\}, see Figure 1. Recall that, ℛ ⁡ ( ℒ 𝔠) \mathcal{R}(\mathcal{L}_{\mathfrak{c}}) assumes one of following shapes

 | ( ℂ \ { 0, β 1, …, β r − 1, 𝔠 }) × { 𝔠 }, ( ℂ \ { 0, β 1, …, β r − 1 }) × { 𝔠 }, or ​ ( ℂ \ { β 1, …, β r − 1 }) × { 𝔠 }. \begin{array}[]{c}\big(\mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1},\mathfrak{c}\}\big)\times\{\mathfrak{c}\},\ \ \ \big(\mathbb{C}\backslash\{0,\beta_{1},\ldots,\beta_{r-1}\}\big)\times\{\mathfrak{c}\},\\ \\ \ \hbox{ or }\ \big(\mathbb{C}\backslash\{\beta_{1},\ldots,\beta_{r-1}\}\big)\times\{\mathfrak{c}\}.\end{array} |  |

Moreover, each cycle α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) induces the canonical cycle

δ 𝚒 ​ ( 𝔠) ≐ ℛ − 1 ​ ( α 𝚒 ​ ( 𝔠)) \delta_{\tt i}(\mathfrak{c})\doteq\mathcal{R}^{-1}(\alpha_{\tt i}(\mathfrak{c}))

of d ​ ℋ = 0 d\mathcal{H}=0. As in equation ( 55), the canonical global generators of the fundamental groups for all the generic fibers are

B C ( 𝔠) ≐ { α 𝚒 ( 𝔠) | 1 ≤ 𝚒 ≤ 𝔯, 𝔠 ∈ ℂ \ 𝔅 ( ℋ) } BC(\mathfrak{c})\doteq\{\alpha_{\tt i}(\mathfrak{c})\,|\,1\leq{\tt i}\leq\mathfrak{r},\,\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\}

they are complex cycles of d ​ 𝔠 = 0 d\mathfrak{c}=0. The canonical global generators of the fundamental groups for all the generic fibers of d ​ ℋ = 0 d\mathcal{H}=0, equation ( 56), depend of the Neumann–Norbury family, and are given by

 | B ​ C ​ ( ℋ) ≐ { { δ 𝚒 ( 𝔠) | 𝚒 = 0, …, r and 𝔠 ∈ ℂ \ 𝔅 ( ℋ) } if ℋ ∈ 𝔉 1, { δ 𝚒 ( 𝔠) | 𝚒 = 0, …, r − 1 and 𝔠 ∈ ℂ \ 𝔅 ( ℋ) } if ℋ ∈ 𝔉 2, { δ 𝚒 ( 𝔠)] | 𝚒 = 1, …, r − 1 and 𝔠 ∈ ℂ \ 𝔅 ( ℋ) } if ℋ ∈ 𝔉 3. BC(\mathcal{H})\doteq\begin{cases}\big\{\delta_{\tt i}(\mathfrak{c})\ |\,{\tt i}=0,\ldots,r\;\mbox{ and }\;\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\big\}&\mbox{if $\mathcal{H}\in\mathfrak{F}_{1}$,}\\[6.0pt] \big\{\delta_{\tt i}(\mathfrak{c})\ |\,{\tt i}=0,\ldots,r-1\;\mbox{ and }\;\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\big\}&\mbox{if $\mathcal{H}\in\mathfrak{F}_{2}$,}\\[6.0pt] \big\{\delta_{\tt i}(\mathfrak{c})]\ |\,{\tt i}=1,\ldots,r-1\;\mbox{ and }\;\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\big\}&\mbox{if $\mathcal{H}\in\mathfrak{F}_{3}$.}\end{cases} |  | (58) |

Summing up, all these constructions allow us to consider simultaneously the Abelian integrals

 | I 𝚒 ( c) = ∫ γ 𝚒 ​ ( c) ω, ℐ 𝚒 ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ and J 𝚒 ( 𝔠) = ∫ α 𝚒 ​ ( 𝔠) η for 1 ≤ 𝚒 ≤ 𝔯. I_{\tt i}(c)=\int_{\gamma_{{\tt i}}(c)}\omega,\quad\mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta\quad\mbox{and}\quad J_{\tt i}(\mathfrak{c})=\int_{\alpha_{\tt i}(\mathfrak{c})}\eta\qquad\mbox{for $1\leq{\tt i}\leq\mathfrak{r}$.} |  |

Corollaries 5 and 15 prove equation ( 22), which show the validity of Step 3 in our Program.

On one hand, it is well-know that he Abelian integral I ⁡ ( c) I(c) in ( 2) depends only on the homology class of the cycle γ ⁡ ( c) \gamma(c). On the other hand, if H H has trivial global monodromy, the homology class of γ ⁡ ( c) \gamma(c) is an integer linear combination of the homology classes of γ 𝚒 ​ ( c) \gamma_{\tt i}(c) in equation ( 57). Therefore, I ⁡ ( c) I(c) is an integer linear combination of the canonical integrals I 𝚒 ​ ( c) I_{\tt i}(c). Furthermore, according to Step 3 of our Program, it is enough to study the Abelian integrals ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) defined by ( ℋ, ϑ) (\mathcal{H},\vartheta), with ϑ \vartheta a non-exact 1 1 -form.

Let ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) 𝔫 \vartheta\in\varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\mathfrak{n}} be an non-exact polynomial 1-form of degree 𝔫. \mathfrak{n}. Lemma 16 implies that

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ = ∑ j = 1 𝔫 ∑ i = 0 𝔫 − j ∫ δ 𝚒 ​ ( 𝔠) ϑ i ​ j. \mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta=\sum_{j=1}^{\mathfrak{n}}\sum_{i=0}^{{\mathfrak{n}}-j}\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta_{ij}. |  | (59) |

The rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} gives the rational 1-form η i ​ j ≐ ℛ ∗ ​ ( ϑ i ​ j) \eta_{ij}\doteq\mathcal{R}_{*}(\vartheta_{ij}), and by using the explicit expression given in ( 38), we have

 | η i ​ j = ( M N) i ​ ( S T) j ​ ( N ​ ∂ M ∂ t − M ​ ∂ N ∂ t N 2 ​ d ​ t + N ​ ∂ M ∂ 𝔠 − M ​ ∂ N ∂ 𝔠 N 2 ​ d ​ 𝔠), \eta_{ij}=\left(\frac{M}{N}\right)^{i}\left(\frac{S}{T}\right)^{j}\left(\frac{N\frac{\partial M}{\partial t}-M\frac{\partial N}{\partial t}}{N^{2}}\,dt+\frac{N\frac{\partial M}{\partial\mathfrak{c}}-M\frac{\partial N}{\partial\mathfrak{c}}}{N^{2}}\,d\mathfrak{c}\right), |  |

which can be written in the form

 | η i ​ j = η i ​ j t + η i ​ j 𝔠 ≐ P ⁡ ( t, 𝔠) N ​ ( t, 𝔠) 2 + i ​ T ​ ( t, 𝔠) j ​ d ​ t + Q ⁡ ( t, 𝔠) N ​ ( t, 𝔠) 2 + i ​ T ​ ( t, 𝔠) j ​ d ​ 𝔠, \eta_{ij}=\eta_{ij}^{t}+\eta_{ij}^{\mathfrak{c}}\doteq\frac{P(t,\mathfrak{c})}{N(t,\mathfrak{c})^{2+i}T(t,\mathfrak{c})^{j}}\,dt+\frac{Q(t,\mathfrak{c})}{N(t,\mathfrak{c})^{2+i}T(t,\mathfrak{c})^{j}}\,d\mathfrak{c}, |  | (60) |

where P ⁡ ( t, 𝔠) P(t,\mathfrak{c}) and Q ⁡ ( t, 𝔠) Q(t,\mathfrak{c}) are polynomials. Recalling the basis for homology ( 58), in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}} the integration of η i ​ j \eta_{ij} is considered along the cycles { α 𝚒 ​ ( 𝔠) } \{\alpha_{\tt i}(\mathfrak{c})\}. In addition, the integral of the second part on the right-hand side of equation ( 60) vanishes identically. Thus,

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ = J 𝚒 ​ ( 𝔠) = ∫ α 𝚒 ​ ( 𝔠) η = ∑ j = 1 𝔫 ∑ i = 0 𝔫 − j ∫ α 𝚒 ​ ( 𝔠) η i ​ j t. \mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta=J_{\tt i}(\mathfrak{c})=\int_{\alpha_{\tt i}(\mathfrak{c})}\eta=\sum_{j=1}^{\mathfrak{n}}\sum_{i=0}^{{\mathfrak{n}}-j}\int_{\alpha_{\tt i}(\mathfrak{c})}\eta_{ij}^{t}. |  | (61) |

The *divisor of poles of the 1-form η i ​ j t \eta_{ij}^{t}*is

 | { N ( t, 𝔠) 2 + i T ( t, 𝔠) j = ∏ 𝚒 = 0 r ( t − β 𝚒) ν ⁡ ( 𝚒) = 0 } ⊂ ℂ t ​ 𝔠 2, \left\{N(t,\mathfrak{c})^{2+i}T(t,\mathfrak{c})^{j}=\prod_{{\tt i}=0}^{r}(t-\beta_{\tt i})^{\nu(\tt i)}=0\right\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}, |  | (62) |

where the appearance of the factors ( t − β 𝚒) ν ⁡ ( 𝚒) (t-\beta_{\tt i})^{\nu(\tt i)} depends on the Neumann–Norbury family 𝔉 ι \mathfrak{F}_{\iota}.

###### Remark 8.

The divisor of poles of η i ​ j t \eta_{ij}^{t} is contained in the arrangement of lines 𝒜 \mathcal{A}; Figure 1 illustrates this.

The exponent ν ⁡ ( 𝚒) \nu({\tt i}), where 𝚒 {\tt i} enumerates the homology classes, is the maximum positive integer value such that ( t − β 𝚒) ν ⁡ ( 𝚒) (t-\beta_{\tt i})^{\nu({\tt i})} divides N ​ ( t, 𝔠) 2 + i ​ T ​ ( t, 𝔠) j N(t,\mathfrak{c})^{2+i}T(t,\mathfrak{c})^{j}; that is, ν ⁡ ( 𝚒) \nu({\tt i}) is the multiplicity of the pole at { t − β 𝚒 = 0 } \{t-\beta_{\tt i}=0\}.

In order to compute the integral of η i ​ j t \eta_{ij}^{t} along α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}), we simplify our notation by using β = β 𝚒 \beta=\beta_{\tt i}, ν = ν ⁡ ( 𝚒) \nu=\nu({\tt i}) and α ​ ( 𝔠) = α 𝚒 ​ ( 𝔠) \alpha(\mathfrak{c})=\alpha_{\tt i}(\mathfrak{c}). Thus, at { t − β = 0 } \{t-\beta=0\} the term η i ​ j t \eta_{ij}^{t} has the following representation:

 | η i ​ j t = R ⁡ ( t, 𝔠) ( t − β) ν ​ d ​ t, \eta_{ij}^{t}=\frac{R(t,\mathfrak{c})}{(t-\beta)^{\nu}}dt, |  | (63) |

where R ⁡ ( t, 𝔠) R(t,\mathfrak{c}) is holomorphic in a small enough two-dimensional polydisc Δ ⁡ ( ( β, 𝔠 0), ( ρ 1, ρ 2)) \Delta((\beta,\mathfrak{c}_{0}),(\rho_{1},\rho_{2})) centered at ( β, 𝔠 0) (\beta,\mathfrak{c}_{0}), where 𝔠 0 \mathfrak{c}_{0} is a generic value of ℋ \mathcal{H}.

###### Proposition 19.

The Abelian integral of η i ​ j t \eta_{ij}^{t} is

 | ∫ α ⁡ ( 𝔠) η i ​ j t = 2 ​ π ​ − 1 ( ν − 1)! ⋅ ∂ ν − 1 R ⁡ ( t, 𝔠) ∂ t ν − 1 | t = β. \int_{\alpha(\mathfrak{c})}\eta_{ij}^{t}=\frac{2\pi\sqrt{-1}}{(\nu-1)!}\cdot\frac{\partial^{\nu-1}R(t,\mathfrak{c})}{\partial t^{\nu-1}}\Big|_{t=\beta}. |  | (64) |

###### Proof.

The function R ⁡ ( t, 𝔠) R(t,\mathfrak{c}) in equation ( 63) is written as

 | R ⁡ ( t, 𝔠) = R 0 ​ ( 𝔠) + R 1 ​ ( 𝔠) ​ ( t − β) + ⋯ + R ν − 1 ​ ( 𝔠) ​ ( t − β) ν − 1 + R ^ ​ ( t, 𝔠) ​ ( t − β) ν, R(t,\mathfrak{c})=R_{0}(\mathfrak{c})+R_{1}(\mathfrak{c})(t-\beta)+\cdots+R_{\nu-1}(\mathfrak{c})(t-\beta)^{\nu-1}+\widehat{R}(t,\mathfrak{c})(t-\beta)^{\nu}, |  |

where R ^ ​ ( t, 𝔠) \widehat{R}(t,\mathfrak{c}) is a holomorphic function. Thus,

 | R ν − 1 ​ ( 𝔠) = 1 ( ν − 1)! ​ ∂ ν − 1 R ⁡ ( t, 𝔠) ∂ t ν − 1 | t = β R_{\nu-1}(\mathfrak{c})=\frac{1}{(\nu-1)!}\frac{\partial^{\nu-1}R(t,\mathfrak{c})}{\partial t^{\nu-1}}\Big|_{t=\beta} |  |

and

 | η i ​ j t = ( R 0 ​ ( 𝔠) ( t − β) ν + R 1 ​ ( 𝔠) ( t − β) ν − 1 + ⋯ + R ν − 1 ​ ( 𝔠) ( t − β)) ​ d ​ t + R ^ ​ ( t, 𝔠) ​ d ​ t. \eta_{ij}^{t}=\left(\frac{R_{0}(\mathfrak{c})}{(t-\beta)^{\nu}}+\frac{R_{1}(\mathfrak{c})}{(t-\beta)^{\nu-1}}+\cdots+\frac{R_{\nu-1}(\mathfrak{c})}{(t-\beta)}\right)dt+\widehat{R}(t,\mathfrak{c})dt. |  |

Hence, by the residue theorem, we obtain equation ( 64). ∎

The following result shows the naturalness of our method.

###### Lemma 20.

Let H ⁡ ( u, v) H(u,v) be a trivial global monodromy polynomial. The set of non-conservative polynomial 1-forms for the canonical global generators B ​ C ​ ( H) BC(H) is an open and dense set in the vector space Ω 1 ​ ( ℂ u ​ v 2) ≤ n \varOmega^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n} of polynomial 1-forms of degree at most n n.

###### Proof.

Recalling the diagram ( 25) in the Program. We assume without loss of generality that H H is a normal form ℋ ⁡ ( x, y) \mathcal{H}(x,y) on ℂ x ​ y 2 \mathbb{C}^{2}_{x\,y}. Given a 1-form ω \omega of degree at most n n, let ϑ \vartheta the corresponding 1-form in ℂ x ​ y 2 \mathbb{C}^{2}_{x\,y}. In fact, the vanishing of the integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}), of ϑ \vartheta for the canonical global section δ 𝚒 ​ ( 𝔠) \delta_{\tt i}(\mathfrak{c}) of B ​ C ​ ( ℋ) BC(\mathcal{H}), is equivalent to the vanishing of the residue of the 1-form η = ℛ ∗ ​ ( ϑ) \eta=\mathcal{R}_{*}(\vartheta) along a line of punctures in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}, as in Figure 1. This last imposes a finite number of analytical equations in the corresponding space Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 = { ϑ } \varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}=\{\vartheta\}, where 𝔫 \mathfrak{n} is provided by Lemma 7. Since B ​ C ​ ( ℋ) BC(\mathcal{H}) has a finite number of global sections, the non-conservative 1-forms in Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}} for B ​ C ​ ( ℋ) BC(\mathcal{H}) are characterized by the complement of the zeros of a finite number of analytic equations. ∎

Now, we provide the meaning of the zeros of global Abelian integrals.

###### Proposition 21.

Let H H be a primitive polynomial on ℂ 2 \mathbb{C}^{2} with trivial global monodromy and let ω \omega be a polynomial 1-form. Let γ 𝚒 ​ ( c 0) \gamma_{\tt i}(c_{0}) be a complex cycle of d ​ H = 0 dH=0 in the canonical global generators B ​ C ​ ( H) BC(H). If the Abelian integral I 𝚒 ​ ( c) = ∫ γ 𝚒 ​ ( c) ω I_{\tt i}(c)=\int_{\gamma_{\tt i}(c)}\omega, is non-identically zero and it has N N isolated zeros (counted with multiplicities) in ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H), then the number of complex limit cycles of the non-conservative perturbation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 that are generated from the global section { γ 𝚒 ​ ( c) | c ∈ ℂ \ 𝔅 ⁡ ( H) } \{\gamma_{\tt i}(c)\,|\,c\in\mathbb{C}\backslash\mathfrak{B}(H)\} is at most N N.

###### Proof.

We assume without loss of generality that H H is a normal form ℋ \mathcal{H} on ℂ 2 \mathbb{C}^{2}, as in diagram 25. Let { 𝔠 ^ 1, …, 𝔠 ^ l } \{\hat{\mathfrak{c}}_{1},\ldots,\hat{\mathfrak{c}}_{l}\} be the different zeros of ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) and let ν i \nu_{i} be the multiplicity of the zero 𝔠 ^ i \hat{\mathfrak{c}}_{i}. Thus, ν 1 + ⋯ + ν l = N \nu_{1}+\cdots+\nu_{l}=N.

By Lemma 18, we have a global transversal section T ⁡ ( ℋ) T(\mathcal{H}), parametrized by 𝔠 ∈ ℂ \ 𝔅 ⁡ ( H) \mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(H), to the global section { γ 𝚒 ​ ( 𝔠) | 𝔠 ∈ ℂ \ 𝔅 ⁡ ( H) } \{\gamma_{\tt i}(\mathfrak{c})\,|\,\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(H)\}. We have a displacement function defined in a small neigborhood D ⁡ ( 0, ρ 0) × U 𝔠 D(0,\rho_{0})\times U_{\mathfrak{c}} of ( 0, 𝔠) (0,\mathfrak{c}) for every 𝔠 ∈ ℂ \ 𝔅 ⁡ ( H) \mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(H), where U 𝔠 ⊂ T ⁡ ( H) U_{\mathfrak{c}}\subset T(H). If ℐ 𝚒 ​ ( 𝔠 ∗) ≠ 0 \mathcal{I}_{\tt i}(\mathfrak{c}^{*})\neq 0, then the displacement function does not vanish in a neigborhood D ⁡ ( 0, ρ 0) × U 𝔠 ∗ D(0,\rho_{0})\times U_{\mathfrak{c}^{*}} of ( 0, 𝔠 ∗) (0,\mathfrak{c}^{*}). Hence γ 𝚒 ​ ( 𝔠 ∗) \gamma_{\tt i}(\mathfrak{c}^{*}) does not generate any complex limit cycle. This implies that the complex limit cycles of d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0 that are generated from the complex cycles in global section { γ 𝚒 ( 𝔠), | 𝔠 ∈ ℂ \ 𝔅 ( ℋ) } \{\gamma_{\tt i}(\mathfrak{c}),|\,\mathfrak{c}\in\mathbb{C}\backslash\mathfrak{B}(\mathcal{H})\}, is bounded from above by the number of complex limit cycles that are generated from the complex cycles γ 𝚒 ​ ( 𝔠 ^ 1), …, γ 𝚒 ​ ( 𝔠 ^ l) \gamma_{\tt i}(\hat{\mathfrak{c}}_{1}),\ldots,\gamma_{\tt i}(\hat{\mathfrak{c}}_{l}) associated to the isolated zeros of ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}). Finally, the assertion follows by applying Proposition 4 in a closed disc D ⁡ ( 𝔠 j, ρ j) ⊂ ℂ \ 𝔅 ⁡ ( ℋ) D(\mathfrak{c}_{j},\rho_{j})\subset\mathbb{C}\backslash\mathfrak{B}(\mathcal{H}) for j = 1, …, l j=1,\dots,l. ∎

## 5. A list of significant examples

### 5.1. The harmonic oscillator

The Hamiltonian differential equation determined by the polynomial

 | H ⁡ ( u, v) = ( u 2 + v 2) / 2 H(u,v)=(u^{2}+v^{2})/2 |  |

is the *harmonic oscillator*. We will apply the four steps of our Program § 3 to study the infinitesimal perturbed Hamiltonian differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0, where ω ∈ Ω n ​ e 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}_{ne}(\mathbb{C}^{2}_{u\,v})_{\leq n}.

Step 1. According to our Program, by using the linear automorphisms

ψ ⁡ ( u, v) = ( 1 2 ​ ( 2 − u − − 1 ​ v), 1 2 ​ ( u − − 1 ​ v)) ​ and ​ σ ​ ( c) = c = 𝔠, \psi(u,v)=\left(\frac{1}{\sqrt{2}}(\sqrt{2}-u-\sqrt{-1}v),\frac{1}{\sqrt{2}}(u-\sqrt{-1}v)\right)\ \hbox{ and }\ \sigma(c)=c=\mathfrak{c},

we get

 | ℋ ⁡ ( x, y) ≐ ( σ ∘ H ∘ ψ − 1) ​ ( x, y) = y ⁡ ( 1 − x). \mathcal{H}(x,y)\doteq\big(\sigma\circ H\circ\psi^{-1}\big)(x,y)=y(1-x). |  |

This shows that H ⁡ ( u, v) H(u,v) is algebraically equivalent to ℋ ⁡ ( x, y) \mathcal{H}(x,y), which belongs to the Neumann–Norbury family 𝔉 3 \mathfrak{F}_{3}, with r = 2 r=2, a 1 = 1 a_{1}=1, β 1 = 1 \beta_{1}=1 and h ⁡ ( x) ≡ 0 h(x)\equiv 0. According to Corollary 5, the corresponding differential equations d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 and d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0 are algebraically equivalent:

 | σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω) = d ​ ℋ + ε ​ ϑ, ϑ = σ ′ ​ ψ ∗ ​ ( ω). \sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)=d\mathcal{H}+\varepsilon\vartheta,\quad\vartheta=\sigma^{\prime}\psi_{*}(\omega). |  | (65) |

Since ψ \psi is linear, the degree of ϑ \vartheta coincides with the degree of ω \omega. Thus

 | ( ψ, σ) ∗ ​ ( Ω n ​ e 1 ​ ( ℂ u ​ v 2) ≤ n) = Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ n and 𝒩 B ​ C ​ ( H) ​ ( ω) = 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ). (\psi,\sigma)_{*}\Big(\varOmega^{1}_{ne}(\mathbb{C}^{2}_{u\,v})_{\leq n}\Big)=\varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq n}\quad\mbox{and}\quad\mathscr{N}_{BC(H)}(\omega)=\mathscr{N}_{BC(\mathcal{H})}(\vartheta). |  |

Step 2. We now use the rectification technique. From Lemma 14, if 𝒢 ⁡ ( x, y) = x \mathcal{G}(x,y)=x, then ℛ = ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) \mathcal{R}=(\mathcal{G}(x,y),\mathcal{H}(x,y)) is a rectifying map for ℋ \mathcal{H}. In this case, Σ ( ℛ) = { 1 − x = 0 } \Sigma(\mathcal{R})=\{1-x=0\} and equation ( 42) becomes

 | ℂ x ​ y 2 \ { 1 − x = 0 } → ℛ ℂ t ​ 𝔠 2 \ { 1 − t = 0 } ⟶ ℛ − 1 ℂ x ​ y 2 \ { 1 − x = 0 } ( x, y) ⟼ ( x, y ⁡ ( 1 − x)) ⟼ ( t, 𝔠 1 − t). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\{1-x=0\}&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\{1-t=0\}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\{1-x=0\}\\ &&&&\\ (x,y)&\longmapsto&(x,y(1-x))&\longmapsto&\big(t,\frac{\mathfrak{c}}{1-t}\big).\end{array} |  |

Thus, equation ( 65) is transformed into

 | ℛ ∗ ​ ( σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω)) = ℛ ∗ ​ ( d ​ ℋ + ε ​ ϑ) = d ​ 𝔠 + ε ​ η, η = ℛ ∗ ​ ( ϑ). \mathcal{R}_{*}\big(\sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)\big)=\mathcal{R}_{*}\big(d\mathcal{H}+\varepsilon\vartheta\big)=d\mathfrak{c}+\varepsilon\eta,\quad\eta=\mathcal{R}_{*}(\vartheta). |  | (66) |

In this way and by using that 𝔠 = σ ⁡ ( c) = c \mathfrak{c}=\sigma(c)=c, each fiber L c L_{c} of H H, with c ≠ 0 c\neq 0, is biholomorphically mapped by ( ψ, σ) (\psi,\sigma) into the fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ \mathcal{H}; which through ℛ \mathcal{R} is biholomorphically mapped into the horizontal line OPEN ( ℂ \ { 1 }) × 𝔠) (\mathbb{C}\backslash\{1\})\times\mathfrak{c}) in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}} with one puncture. See Figure 2. Hence, H H is of type ( 0, 2) (0,2). This implies that for c = 𝔠 ≠ 0 c=\mathfrak{c}\neq 0,

 | dim H 1 ​ ( L c, ℤ) = dim H 1 ​ ( ℒ 𝔠, ℤ) = dim H 1 ​ ( ( ℂ \ { 1 }) × { 𝔠 }, ℤ) = 1. \dim H_{1}(L_{c},\mathbb{Z})=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=\dim H_{1}\left(\big(\mathbb{C}\backslash\{1\}\big)\times\{\mathfrak{c}\},\mathbb{Z}\right)=1. |  | (67) |

Moreover, H H has a unique critical point at ( 0, 0) (0,0) and H ⁡ ( 0, 0) = 0 H(0,0)=0. Thus, 𝔅 f ​ i ​ n ​ ( H) = 𝔅 f ​ i ​ n ​ ( ℋ) = { 0 } \mathfrak{B}_{fin}(H)=\mathfrak{B}_{fin}(\mathcal{H})=\{0\} and 𝔅 i ​ n ​ f ​ ( H) = 𝔅 i ​ n ​ f ​ ( ℋ) = ∅ \mathfrak{B}_{inf}(H)=\mathfrak{B}_{inf}(\mathcal{H})=\emptyset. Hence, 𝔅 ⁡ ( H) = 𝔅 ⁡ ( ℋ) = { 0 } \mathfrak{B}(H)=\mathfrak{B}(\mathcal{H})=\{0\}. See Figure 2.

Step 3. Recalling the existence canonical global bases for the unperturbed differential equations, as in equation ( 5), in this case

B ​ C ​ ( H) = { γ 𝟷 ​ ( c) } BC(H)=\{\gamma_{\tt 1}(c)\}, B ​ C ​ ( ℋ) = { δ 𝟷 ​ ( 𝔠) } BC(\mathcal{H})=\{\delta_{\tt 1}(\mathfrak{c})\} and B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c})\}.

Therefore, there exists only one Abelian integral I 1 ​ ( c) I_{1}(c) defined by the pair ( H, ω) (H,\omega), which is algebraically equivalent to a unique Abelian integral ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) defined by the pair ( ℋ, ϑ) (\mathcal{H},\vartheta). Moreover, ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) is rationally equivalent to a unique Abelian integral J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) defined by the pair ( 𝔠, η) (\mathfrak{c},\eta). Thus,

 | Z ⁡ ( I 1 ​ ( c)) = Z ⁡ ( ℐ 1 ​ ( 𝔠)) = Z ⁡ ( J 1 ​ ( 𝔠)). Z(I_{1}(c))=Z(\mathcal{I}_{1}(\mathfrak{c}))=Z(J_{1}(\mathfrak{c})). |  |

We choose the canonical global generators of d ​ 𝔠 = 0 d\mathfrak{c}=0 as B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c})\}, where α 𝟷 ​ ( 𝔠) \alpha_{\tt 1}(\mathfrak{c}) is a small cycle around the puncture ( 1, 𝔠) (1,\mathfrak{c}) in the line ( ℂ \ { 1 }) × { 𝔠 } \big(\mathbb{C}\backslash\{1\}\big)\times\{\mathfrak{c}\}. We have the Abelian integral

 | J 1 ​ ( 𝔠) = ∫ α 𝟷 ​ ( 𝔠) η. J_{1}(\mathfrak{c})=\int_{\alpha_{\tt 1}(\mathfrak{c})}\eta. |  |

Therefore, we have obtained that

 | I 1 ​ ( c) = ℐ 1 ​ ( 𝔠) = J 1 ​ ( 𝔠), 𝔠 = σ ⁡ ( c) = c. I_{1}(c)=\mathcal{I}_{1}(\mathfrak{c})=J_{1}(\mathfrak{c}),\quad\mathfrak{c}=\sigma(c)=c. |  |

Figure 2. Let H ⁡ ( u, v) = ( u 2 + v 2) / 2 H(u,v)=(u^{2}+v^{2})/2, we sketch of the leaves of the foliations d ​ H = 0 dH=0, d ​ ℋ = 0 d\mathcal{H}=0 and d ​ 𝔠 = 0 d\mathfrak{c}=0. In OPEN a) a) the blue curves correspond to the generic fibers of H H and the magenta curve is the connected component { v − − 1 u = 0 } \{v-\sqrt{-1}u=0\} of the singular fiber L 0 L_{0} of H H. In OPEN b) b) and OPEN c) c) the blue and magenta curves are the image under ( ψ, σ) (\psi,\sigma) and ℛ \mathcal{R}, respectively, of the blue and magenta curves in OPEN a) a). In OPEN a) a), b b and OPEN c) c), the dashed red curves mean that they have been removed from the respective planes.

Step 4. From Lemma 16, for computing ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) it is sufficient to consider the basis B n ​ e 1 ( ℂ x ​ y 2, n) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},n)=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most n n. Then

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = t i ​ ( 𝔠 1 − t) j ​ [1 ​ d ​ t + 0 ​ d ​ 𝔠] = ( − 1) j ​ t i ​ 𝔠 j ( t − 1) j ​ d ​ t. \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=t^{i}\left(\frac{\mathfrak{c}}{1-t}\right)^{j}\left[1\,dt+0\,d\mathfrak{c}\right]=\frac{(-1)^{j}t^{i}\mathfrak{c}^{j}}{(t-1)^{j}}dt. |  |

By using the criterion given in equation ( 64), we obtain

 | ∫ α 1 ​ ( 𝔠) η i ​ j = ( ( 2 ​ π ​ − 1) ( j − 1)! ​ ∂ j − 1 ( − 1) j ​ t i ∂ t j − 1 | t = 1) ​ 𝔠 j. \int_{\alpha_{1}(\mathfrak{c})}\eta_{ij}=\left(\frac{\left(2\pi\sqrt{-1}\right)}{(j-1)!}\,\frac{\partial^{j-1}(-1)^{j}t^{i}}{\partial t^{j-1}}\Big|_{t=1}\right)\mathfrak{c}^{j}. |  |

Thus, the last expression is a polynomial function in 𝔠 \mathfrak{c}, of degree j j if and only if i ≥ j − 1 i\geq j-1. This condition and i + j ≤ n i+j\leq n imply that 2 ​ j − 1 ≤ n 2j-1\leq n, or equivalently

 | j ≤ [n + 1 2]. j\leq\left[\frac{n+1}{2}\right]. |  |

Hence, J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) is a polynomial of degree at most [n + 1 2] \left[\frac{n+1}{2}\right]. Moreover, 𝔠 = 0 ∈ 𝔅 ⁡ ( ℋ) \mathfrak{c}=0\in\mathfrak{B}(\mathcal{H}) always is a zero of J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}). Therefore, according to equation ( 61) and diagram ( 25), we have

 | Z ⁡ ( I 1 ​ ( c)) = Z ⁡ ( ℐ 1 ​ ( 𝔠)) = Z ⁡ ( J 1 ​ ( 𝔠)) ≤ [n − 1 2]. Z(I_{1}(c))=Z(\mathcal{I}_{1}(\mathfrak{c}))=Z(J_{1}(\mathfrak{c}))\leq\left[\frac{n-1}{2}\right]. |  |

If ω \omega is non-conservative for B ​ C ​ ( H) BC(H), then we have

 | 𝒩 B ​ C ​ ( H) ​ ( ω) = 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) = 𝒩 B ​ C ​ ( 𝔠) ​ ( η) ≤ [n − 1 2]. \mathscr{N}_{BC(H)}(\omega)=\mathscr{N}_{BC(\mathcal{H})}(\vartheta)=\mathscr{N}_{BC(\mathfrak{c})}(\eta)\leq\left[\frac{n-1}{2}\right]. |  |

In order to find the optimal upper bound for Z ​ ( I 1 ​ ( c)) Z(I_{1}(c)), let c 1, …, c s ∈ ℂ ∗ c_{1},\ldots,c_{s}\in\mathbb{C}^{*} be different generic values of H H. We define A ( c) = μ ( c − c 1) ⋯ ( c − c s) A(c)=\mu(c-c_{1})\cdots(c-c_{s}), μ ∈ ℂ ∗ \mu\in\mathbb{C}^{*}, and the polynomial 1-form ω s ≐ ψ ∗ ​ ( A ⁡ ( y ⁡ ( 1 − x)) ​ y ​ d ​ x) \omega_{s}\doteq\psi^{*}\left(A\big(y(1-x)\big)\,y\,dx\right) of degree n = 2 ​ s + 1 n=2s+1. The corresponding integral

 | ∫ γ 1 ​ ( c) ω s = − ∫ α 1 ​ ( c) A ⁡ ( c) t − 1 d t = − ( 2 π − 1) c ( c − c 1) ⋯ ( c − c s) \int_{\gamma_{1}(c)}\omega_{s}=-\int_{\alpha_{1}(c)}\frac{A(c)}{t-1}\,dt=-\left(2\pi\sqrt{-1}\right)c(c-c_{1})\cdots(c-c_{s}) |  |

has s = [( n − 1) / 2] s=[(n-1)/2] different simple zeros in ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H).

In conclusion, if H ⁡ ( u, v) = ( u 2 + v 2) / 2 H(u,v)=(u^{2}+v^{2})/2 and ω \omega is a polynomial 1-form of degree n n, then the maximal number of zeros of the Abelian integral

 | I 1 ​ ( c) = ∫ γ 𝟷 ​ ( c) ω: ℂ \ 𝔅 H ⟶ ℂ I_{1}(c)=\int_{\gamma_{\tt 1}(c)}\omega:\mathbb{C}\backslash\mathfrak{B}_{H}\longrightarrow\mathbb{C} |  |

is

 | Z ⁡ ( I 1 ​ ( c)) = [deg ⁡ ( ω) − 1 deg ⁡ ( H)] = [n − 1 2]. Z(I_{1}(c))=\left[\frac{\deg(\omega)-1}{\deg(H)}\right]=\left[\frac{n-1}{2}\right]. |  | (68) |

We recall that, 𝒩 B ​ C ​ ( H) ​ ( ω) = Z ⁡ ( I 1 ​ ( c)) \mathscr{N}_{BC(H)}(\omega)=Z(I_{1}(c)) is the number of limit cycles, generated from the cycles in the generic fibers of H H, of a non-conservative infinitesimal perturbation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0 of the harmonic oscillator. This coincides with previous results in [13, 16].

### 5.2. Broughton’s polynomial

Let

 | H ⁡ ( u, v) = u ⁡ ( u ​ v − 1) H(u,v)=u(uv-1) |  |

be the polynomial given by S. A. Broughton in [6], and let ω ∈ Ω n ​ e 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}_{ne}(\mathbb{C}^{2}_{u\,v})_{\leq n}. We apply the four steps of our Program § 3 to study the infinitesimal perturbed Hamiltonian differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0.

Step 1. By using the linear automorphisms ψ ⁡ ( u, v) = ( 1 − u, v) \psi(u,v)=(1-u,v) and σ ⁡ ( c) = 𝔠 \sigma(c)=\mathfrak{c}, whose inverses are where ψ − 1 ​ ( x, y) = ( 1 − x, y) \psi^{-1}(x,y)=(1-x,y), and σ − 1 ​ ( 𝔠) \sigma^{-1}(\mathfrak{c}) the identity, we get

 | ℋ ⁡ ( x, y) ≐ ( σ ∘ H ∘ ψ − 1) ​ ( x, y) = y ​ ( 1 − x) 2 + ( x − 1). \mathcal{H}(x,y)\doteq\big(\sigma\circ H\circ\psi^{-1}\big)(x,y)=y(1-x)^{2}+(x-1). |  |

This proves that H ⁡ ( u, v) H(u,v) is algebraically equivalent to ℋ ⁡ ( x, y) \mathcal{H}(x,y), which belongs to the family 𝔉 3 \mathfrak{F}_{3}, with r = 2 r=2, a 1 = 2 a_{1}=2, β 1 = 1 \beta_{1}=1 and h ⁡ ( x) = x − 1 h(x)=x-1. According to Corollary 5

 | σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω) = d ​ ℋ + ε ​ ϑ, ϑ = σ ′ ​ ψ ∗ ​ ( ω). \sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)=d\mathcal{H}+\varepsilon\vartheta,\quad\vartheta=\sigma^{\prime}\psi_{*}(\omega). |  | (69) |

Moreover, since ψ \psi is linear, the degrees of ℋ \mathcal{H} and ϑ \vartheta are the same as the degrees of H H and ω \omega, thus

 | ( ψ, σ) ∗ ​ Ω n ​ e 1 ​ ( ℂ u ​ v 2) ≤ n = Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ n and 𝒩 B ​ C ​ ( H) ​ ( ω) = 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ). (\psi,\sigma)_{*}\,\varOmega_{ne}^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n}=\varOmega_{ne}^{1}(\mathbb{C}^{2}_{x\,y})_{\leq n}\quad\mbox{and}\quad\mathscr{N}_{BC(H)}(\omega)=\mathscr{N}_{BC(\mathcal{H})}(\vartheta). |  |

Step 2. We now use the rectification technique. From Lemma 14 and according to the Tables 1 and 2, equation ( 42) becomes

 | ℂ x ​ y 2 \ { 1 − x = 0 } → ℛ ℂ t ​ 𝔠 2 \ { 1 − t = 0 } ⟶ ℛ − 1 ℂ x ​ y 2 \ { 1 − x = 0 } ( x, y) ⟼ ( x, y ​ ( 1 − x) 2 + ( x − 1)) ⟼ ( t, 𝔠 + 1 − t ( 1 − t) 2). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\{1-x=0\}&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\{1-t=0\}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\{1-x=0\}\\ &&&&\\ (x,y)&\longmapsto&(x,y(1-x)^{2}+(x-1))&\longmapsto&\big(t,\frac{\mathfrak{c}+1-t}{(1-t)^{2}}\big).\end{array} |  |

In addition, equation ( 69) transforms to

 | ℛ ∗ ​ ( σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω)) = ℛ ∗ ​ ( d ​ ℋ + ε ​ ϑ) = d ​ 𝔠 + ε ​ η, η = ℛ ∗ ​ ( ϑ). \mathcal{R}_{*}\big(\sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)\big)=\mathcal{R}_{*}\big(d\mathcal{H}+\varepsilon\vartheta\big)=d\mathfrak{c}+\varepsilon\eta,\quad\eta=\mathcal{R}_{*}(\vartheta). |  | (70) |

In this way, each original fiber L c L_{c} of H H, with c ≠ 0 c\neq 0, is mapped through ( ψ, σ) (\psi,\sigma) into the fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ \mathcal{H}, with 𝔠 = σ ⁡ ( c) = c \mathfrak{c}=\sigma(c)=c, which is biholomorphically mapped under ℛ \mathcal{R} into the puntured horizontal line ( ℂ \ { 1 }) × { 𝔠 } ⊂ ℂ t ​ 𝔠 2 \big(\mathbb{C}\backslash\{1\}\big)\times\{\mathfrak{c}\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}. See Figure 3. Hence, H H is of type ( 0, 2) (0,2). Thus, for c = 𝔠 ≠ 0 c=\mathfrak{c}\neq 0,

 | dim H 1 ​ ( L c, ℤ) = dim H 1 ​ ( ℒ 𝔠, ℤ) = dim H 1 ​ ( ( ℂ \ { 1 }) × { 𝔠 }, ℤ) = 1. \dim H_{1}(L_{c},\mathbb{Z})=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=\dim H_{1}\left(\big(\mathbb{C}\backslash\{1\}\big)\times\{\mathfrak{c}\},\mathbb{Z}\right)=1. |  | (71) |

Moreover, the polynomial H H does not have finite critical points, that is, 𝔅 f ​ i ​ n ​ ( H) = ∅ \mathfrak{B}_{fin}(H)=\emptyset. The fiber L 0 = { u ( u v − 1) = 0 } L_{0}=\{u(uv-1)=0\} has a critical point at infinity, thus 𝔅 i ​ n ​ f ​ ( H) = { 0 } \mathfrak{B}_{inf}(H)=\{0\}. Hence, 𝔅 ⁡ ( H) = 𝔅 ⁡ ( ℋ) = { 0 } \mathfrak{B}(H)=\mathfrak{B}(\mathcal{H})=\{0\}. See Figure 3.

Step 3. There are canonical global bases for the unperturbed differential equations, as in equation ( 5), as in equation ( 5), in this case

B ​ C ​ ( H) = { γ 𝟷 ​ ( c) } BC(H)=\{\gamma_{\tt 1}(c)\}, B ​ C ​ ( ℋ) = { δ 𝟷 ​ ( 𝔠) } BC(\mathcal{H})=\{\delta_{\tt 1}(\mathfrak{c})\} and B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c})\}.

Therefore, there exists only one Abelian integral I 1 ​ ( c) I_{1}(c) defined by the pair ( H, ω) (H,\omega), which is algebraically equivalent to a unique Abelian integral ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) defined by the pair ( ℋ, ϑ) (\mathcal{H},\vartheta). Moreover, ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) is rationally equivalent to a unique Abelian integral J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) defined by the pair ( 𝔠, η) (\mathfrak{c},\eta). Thus,

 | Z ⁡ ( I 1 ​ ( c)) = Z ⁡ ( ℐ 1 ​ ( 𝔠)) = Z ⁡ ( J 1 ​ ( 𝔠)). Z(I_{1}(c))=Z(\mathcal{I}_{1}(\mathfrak{c}))=Z(J_{1}(\mathfrak{c})). |  |

We choose the canonical global generators B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c})\} of d ​ 𝔠 = 0 d\mathfrak{c}=0, where α 𝟷 ​ ( 𝔠) \alpha_{\tt 1}(\mathfrak{c}) is the cycle around the puncture ( 1, 𝔠) (1,\mathfrak{c}) of the line ( ℂ \ { 1 }) × { 𝔠 } \big(\mathbb{C}\backslash\{1\}\big)\times\{\mathfrak{c}\}. We have the Abelian integral

 | J 1 ​ ( 𝔠) = ∫ α 𝟷 ​ ( 𝔠) η. J_{1}(\mathfrak{c})=\int_{\alpha_{\tt 1}(\mathfrak{c})}\eta. |  |

Clearly,

 | I 1 ​ ( c) = ℐ 1 ​ ( 𝔠) = J 1 ​ ( 𝔠), 𝔠 = c. I_{1}(c)=\mathcal{I}_{1}(\mathfrak{c})=J_{1}(\mathfrak{c}),\quad\mathfrak{c}=c. |  |

Figure 3. Let H ⁡ ( u, v) = u ⁡ ( u ​ v − 1) H(u,v)=u(uv-1), we sketch the leaves of the foliations d ​ H = 0 dH=0, d ​ ℋ = 0 d\mathcal{H}=0 and d ​ 𝔠 = 0 d\mathfrak{c}=0. The singular fiber is L 0 = { u ( u v − 1) = 0 } L_{0}=\{u(uv-1)=0\}. We follow the conventions given in Figure 2. The magenta curves arise from the irreducible component { u v − 1 = 0 } \{uv-1=0\}. The dashed red curve { u = 0 } \{u=0\} and its images have been removed from the respective planes.

Step 4. From Lemma 16, for computing ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) it is sufficient to consider the basis B n ​ e 1 ( ℂ x ​ y 2, n) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},n)=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most n n. Then

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = t i ​ ( 𝔠 + 1 − t ( 1 − t) 2) j ​ d ​ t = ∑ μ = 0 j ( j μ) ​ ( − 1) μ ​ t i ​ 𝔠 j − μ ( t − 1) 2 ​ j + μ ​ d ​ t. \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=t^{i}\left(\frac{\mathfrak{c}+1-t}{(1-t)^{2}}\right)^{j}\,dt=\sum_{\mu=0}^{j}{j\choose\mu}\frac{(-1)^{\mu}t^{i}\mathfrak{c}^{j-\mu}}{(t-1)^{2j+\mu}}\,dt\,. |  | (72) |

Since 2 ​ j + μ ≥ 1 2j+\mu\geq 1, t 1 = 1 t_{1}=1 is a pole of η i ​ j \eta_{ij}, then the evaluation is

 | ∫ α 𝟷 ​ ( 𝔠) ( − 1) μ ​ t i ​ 𝔠 j − μ ( 1 − t) 2 ​ j − μ ​ 𝑑 t = ( − 1) μ ​ ( 2 ​ π ​ − 1) ( 2 ​ j − μ − 1)! ​ ∂ 2 ​ j − μ − 1 ( t i ​ 𝔠 j − μ) ∂ t 2 ​ j − μ − 1 | t = 1, \int_{\alpha_{\tt 1}(\mathfrak{c})}\frac{(-1)^{\mu}t^{i}\mathfrak{c}^{j-\mu}}{(1-t)^{2j-\mu}}\,dt=\frac{(-1)^{\mu}(2\pi\sqrt{-1})}{(2j-\mu-1)!}\,\frac{\partial^{2j-\mu-1}\left(t^{i}\mathfrak{c}^{j-\mu}\right)}{\partial t^{2j-\mu-1}}\Big|_{t=1}, |  |

by applying the criterion of equation ( 64). This integral is a polynomial function in 𝔠 \mathfrak{c} of degree j − μ j-\mu if and only if i ≥ 2 ​ j − μ − 1 i\geq 2j-\mu-1.

The maximum of j − μ j-\mu is reached if and only if μ = 0 \mu=0 and i ≥ 2 ​ j − 1 i\geq 2j-1. This last condition and i + j ≤ n i+j\leq n imply 3 ​ j − 1 ≤ n 3j-1\leq n, or equivalently

 | j ≤ [n + 1 3]. j\leq\left[\frac{n+1}{3}\right]. |  |

The polynomial J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) is of degree at most [n + 1 3] \left[\frac{n+1}{3}\right]. In conclusion, according to ( 61) and diagram ( 25), we have

 | Z ⁡ ( I 1 ​ ( c)) = Z ⁡ ( ℐ 1 ​ ( 𝔠)) = Z ⁡ ( J 1 ​ ( 𝔠)) ≤ [n + 1 3]. Z(I_{1}(c))=Z(\mathcal{I}_{1}(\mathfrak{c}))=Z(J_{1}(\mathfrak{c}))\leq\left[\frac{n+1}{3}\right]. |  |

If ω \omega is non-conservative for B ​ C ​ ( H) BC(H), then we have

 | 𝒩 B ​ C ​ ( H) ​ ( ω) = 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) = 𝒩 B ​ C ​ ( 𝔠) ​ ( η) ≤ [n + 1 3]. \mathscr{N}_{BC(H)}(\omega)=\mathscr{N}_{BC(\mathcal{H})}(\vartheta)=\mathscr{N}_{BC(\mathfrak{c})}(\eta)\leq\left[\frac{n+1}{3}\right]. |  |

We show that this bound is optimal. Let s ≐ [( n + 1) / 3] s\doteq\left[(n+1)/3\right]. If we consider the polynomial 1-form

 | ω n = − ( v n − s ⁡ ( u 2 ​ s − 1 ​ v s − v)) ​ d ​ u \omega_{n}=-\Big(v^{n}-s\left(u^{2s-1}v^{s}-v\right)\Big)\,du |  |

of degree n n, then

 | ϑ n = σ ′ ​ ψ ∗ ​ ( ω) = ( y n − s ⁡ ( ( 1 − x) 2 ​ s − 1 ​ y s − y)) ​ d ​ x \vartheta_{n}=\sigma^{\prime}\psi_{*}(\omega)=\Big(y^{n}-s\left((1-x)^{2s-1}y^{s}-y\right)\Big)\,dx |  |

and

 | η n = ℛ ∗ ​ ( ϑ n) = ( ( 𝔠 + 1 − t) n ( 1 − t) 2 ​ n − s ⁡ ( ( 𝔠 + 1 − t) s 1 − t − ( 𝔠 + 1 − t) ( 1 − t) 2)) ​ d ​ t. \eta_{n}=\mathcal{R}_{*}(\vartheta_{n})=\left(\frac{(\mathfrak{c}+1-t)^{n}}{(1-t)^{2n}}-s\left(\frac{(\mathfrak{c}+1-t)^{s}}{1-t}-\frac{(\mathfrak{c}+1-t)}{(1-t)^{2}}\right)\right)\,dt. |  |

By using the criterion given in equation ( 64), we obtain

 | ∫ α 1 ​ ( 𝔠) ( 𝔠 + 1 − t) n ( 1 − t) 2 ​ n = 2 ​ π ​ − 1 ( 2 ​ n − 1)! ​ ∂ 2 ​ n − 1 ( 𝔠 + 1 − t) n ∂ t 2 ​ n − 1 | t = 1 = 0, \int_{\alpha_{\\ 1}(\mathfrak{c})}\frac{(\mathfrak{c}+1-t)^{n}}{(1-t)^{2n}}=\frac{2\pi\sqrt{-1}}{(2n-1)!}\,\frac{\partial^{2n-1}\left(\mathfrak{c}+1-t\right)^{n}}{\partial t^{2n-1}}\Big|_{t=1}=0, |  |

 | ∫ α 𝟷 ​ ( 𝔠) ( 𝔠 + 1 − t) s 1 − t = − ( 2 ​ π ​ − 1) ​ ( 𝔠 + 1 − t) s | t = 1 = − 2 ​ π ​ − 1 ​ 𝔠 s \int_{\alpha_{\tt 1}(\mathfrak{c})}\frac{(\mathfrak{c}+1-t)^{s}}{1-t}=-\left(2\pi\sqrt{-1}\right)\,\left(\mathfrak{c}+1-t\right)^{s}\,\Big|_{t=1}=-2\pi\sqrt{-1}\,\mathfrak{c}^{s} |  |

and

 | ∫ α 𝟷 ​ ( 𝔠) ( 𝔠 + 1 − t) ( 1 − t) 2 = ( 2 ​ π ​ − 1) ​ ∂ ( 𝔠 + 1 − t) ∂ t | t = 1 = − 2 ​ π ​ − 1. \int_{\alpha_{\tt 1}(\mathfrak{c})}\frac{(\mathfrak{c}+1-t)}{(1-t)^{2}}=\left(2\pi\sqrt{-1}\right)\,\frac{\partial\,\left(\mathfrak{c}+1-t\right)}{\partial t}\Big|_{t=1}=-2\pi\sqrt{-1}. |  |

Therefore,

 | I 1 ​ ( c) = ∫ γ 1 ​ ( c) ω n = ( 2 ​ π ​ − 1) ​ s ​ ( c s − 1) I_{1}(c)=\int_{\gamma_{1}(c)}\omega_{n}=\left(2\pi\sqrt{-1}\right)\,s\left(c^{s}-1\right) |  |

has s = [( n + 1) / 3] s=[(n+1)/3] zeros in ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H). We have obtained the following result.

###### Lemma 22.

Let H ⁡ ( u, v) = u ⁡ ( u ​ v − 1) H(u,v)=u(uv-1) and let ω \omega be a polynomial 1-form of degree n n. The maximal number of zeros of the polynomial Abelian integral

 | I 1 ​ ( c) = ∫ γ 1 ​ ( c) ω: ℂ ⟶ ℂ in ℂ \ 𝔅 H I_{1}(c)=\int_{\gamma_{1}(c)}\omega:\mathbb{C}\longrightarrow\mathbb{C}\ \ \hbox{ in }\ \ \mathbb{C}\backslash\mathfrak{B}_{H} |  |

is

 | Z ⁡ ( I 1 ​ ( c)) = [deg ⁡ ( ω) + 1 deg ⁡ ( H)] = [n + 1 3]. Z(I_{1}(c))=\left[\frac{\deg(\omega)+1}{\deg(H)}\right]=\left[\frac{n+1}{3}\right]. |  |

∎

### 5.3. An isotrivial polynomial of type ( 0, 3) (0,3) in family 𝔉 2 \mathfrak{F}_{2}

We consider the polynomial

 | ℋ ⁡ ( x, y) = ( x ​ y − 1) ​ ( 1 − x ​ ( x ​ y − 1) 2), \mathcal{H}(x,y)=(xy-1)(1-x(xy-1)^{2}), |  |

which belongs to the Neumann–Norbury family 𝔉 2 \mathfrak{F}_{2}, with r = 2 r=2, a 1 = 1 a_{1}=1, β 1 = 1 \beta_{1}=1, p 1 = 0 p_{1}=0, p = 1 p=1, q 1 = 1 q_{1}=1, q = 2 q=2, and 𝒮 ⁡ ( x, y) = x ​ y − 1 \mathcal{S}(x,y)=xy-1. We will apply Steps 2-4 of the Program § 3 for the study of the infinitesimal perturbed Hamiltonian differential equation d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0, where ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}.

Step 2. From Lemma 14 and according to Tables 1, 2, equation ( 43) becomes

 | ℂ x ​ y 2 \ Σ ⁡ ( ℛ) → ℛ ℂ t ​ 𝔠 2 \ { 𝔠 t ( 1 − t) = 0 } ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℛ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( t ​ ( 1 − t) 2 𝔠 2, 𝔠 2 ​ ( 𝔠 + 1 − t) t ​ ( 1 − t) 3). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\{\mathfrak{c}\,t(1-t)=0\}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})\\ &&&&\\ (x,y)&\longmapsto&(\mathcal{G}(x,y),\mathcal{H}(x,y))&\longmapsto&\Big(\frac{t(1-t)^{2}}{\mathfrak{c}^{2}},\frac{\mathfrak{c}^{2}(\mathfrak{c}+1-t)}{t(1-t)^{3}}\Big).\end{array} |  |

Hence,

 | ℛ ∗ ​ ( d ​ ℋ + ε ​ ϑ) = d ​ 𝔠 + ε ​ η, η = ℛ ∗ ​ ( ϑ). \mathcal{R}_{*}\big(d\mathcal{H}+\varepsilon\vartheta\big)=d\mathfrak{c}+\varepsilon\eta,\ \ \ \eta=\mathcal{R}_{*}(\vartheta). |  | (73) |

The polynomial ℋ \mathcal{H} has a unique finite critical point at ( 0, − 1) (0,-1), with critical value ℋ ⁡ ( 0, − 1) = − 1 \mathcal{H}(0,-1)=-1, and its fiber ℒ 0 \mathcal{L}_{0} is the disjoint union of the algebraic curves { x y − 1 = 0 } \{xy-1=0\} and { 1 − x ( x y − 1) 2 = 0 } \{1-x(xy-1)^{2}=0\}, thus 𝔅 f ​ i ​ n ​ ( ℋ) = { − 1 } \mathfrak{B}_{fin}(\mathcal{H})=\{-1\} and 0 ∈ 𝔅 i ​ n ​ f ​ ( ℋ) 0\in\mathfrak{B}_{inf}(\mathcal{H}).

In addition, from the rectification step, each fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}}, with 𝔠 ∉ { 0, − 1 } \mathfrak{c}\not\in\{0,-1\}, of ℋ \mathcal{H} is biholomorphically mapped, through ℛ \mathcal{R}, into the horizontal line ( ℂ ∖ { 0, 1 }) × { 𝔠 } ⊂ ℂ t ​ 𝔠 2 \big(\mathbb{C}\setminus\{0,1\}\big)\times\{\mathfrak{c}\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}, with punctures ( 0, 𝔠) (0,\mathfrak{c}) and ( 1, 𝔠) (1,\mathfrak{c}). Figure 4 illustrates this. Thus, 𝔅 ⁡ ( ℋ) = { 0, − 1 } \mathfrak{B}(\mathcal{H})=\{0,-1\}. Hence, ℋ \mathcal{H} is of type ( 0, 3) (0,3) and for 𝔠 ≠ { 0, − 1 } \mathfrak{c}\neq\{0,-1\},

 | dim H 1 ​ ( ℒ 𝔠, ℤ) = dim H 1 ​ ( ( ℂ ∖ { 0, 1 }) × { 𝔠 }, ℤ) = 2. \dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=\dim H_{1}\left(\big(\mathbb{C}\setminus\{0,1\}\big)\times\{\mathfrak{c}\},\mathbb{Z}\right)=2. |  | (74) |

Step 3. In this case, the canonical global generators of the unperturbed differential equations are of the form

B ​ C ​ ( ℋ) = { δ 𝟷 ​ ( 𝔠), δ 𝟸 ​ ( 𝔠) } BC(\mathcal{H})=\{\delta_{\tt 1}(\mathfrak{c}),\delta_{\tt 2}(\mathfrak{c})\} and B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠), α 𝟸 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c}),\alpha_{\tt 2}(\mathfrak{c})\}.

Therefore, there are two Abelian integrals ℐ 1 ​ ( c) \mathcal{I}_{1}(c) and ℐ 2 ​ ( c) \mathcal{I}_{2}(c) defined by the pair ( ℋ, ϑ) (\mathcal{H},\vartheta), which are rationally equivalent to two Abelian integral J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) and J 2 ​ ( 𝔠) J_{2}(\mathfrak{c}) defined by the pair ( 𝔠, η) (\mathfrak{c},\eta). Thus,

 | Z ⁡ ( ℐ 1 ​ ( 𝔠)) = Z ⁡ ( J 1 ​ ( 𝔠)) and Z ⁡ ( ℐ 2 ​ ( 𝔠)) = Z ⁡ ( J 2 ​ ( 𝔠)). Z(\mathcal{I}_{1}(\mathfrak{c}))=Z(J_{1}(\mathfrak{c}))\quad\mbox{and}\quad Z(\mathcal{I}_{2}(\mathfrak{c}))=Z(J_{2}(\mathfrak{c})). |  |

We choose the canonical global generators B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠), α 𝟸 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c}),\alpha_{\tt 2}(\mathfrak{c})\} of d ​ 𝔠 = 0 d\mathfrak{c}=0, where α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) is a small cycle around the puncture ( t 𝚒, 𝔠) (t_{\tt i},\mathfrak{c}) in the line ( ℂ ∖ { 0, 1 }) × { 𝔠 } ⊂ ℂ t ​ 𝔠 2 \big(\mathbb{C}\setminus\{0,1\}\big)\times\{\mathfrak{c}\}\subset\mathbb{C}^{2}_{t\,\mathfrak{c}}, with t 1 = 0 t_{1}=0, t 2 = 1 t_{2}=1. We have the Abelian integrals

 | ℐ 𝚒 ​ ( 𝔠) = J 𝚒 ​ ( 𝔠) = ∫ α 𝚒 ​ ( 𝔠) η, 𝚒 ∈ { 1, 2 }. \mathcal{I}_{\tt i}(\mathfrak{c})=J_{\tt i}(\mathfrak{c})=\int_{\alpha_{\tt i}(\mathfrak{c})}\eta,\quad{\tt i}\in\{1,2\}. |  |

Figure 4. Let ℋ ⁡ ( x, y) = ( x ​ y − 1) ​ ( 1 − x ​ ( x ​ y − 1) 2) \mathcal{H}(x,y)=(xy-1)(1-x(xy-1)^{2}), we sketch the leaves of the foliations d ​ ℋ = 0 d\mathcal{H}=0 and d ​ 𝔠 = 0 d\mathfrak{c}=0. On the left, the blue curves correspond to the generic fibers of ℋ \mathcal{H} and the magenta curve is the connected component { y + ( 1 − x y) 3 = 0 } \{y+(1-xy)^{3}=0\} of the singular fiber ℒ − 1 \mathcal{L}_{-1} of ℋ \mathcal{H}. On the right, the blue and magenta straight lines are the image under ℛ \mathcal{R} of the blue and the magenta curves in the left, respectively. The dashed red curves mean that they have been removed from the respective planes.

Step 4. From Lemma 16 we know that for computing ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) it is sufficient to consider the basis B n ​ e 1 ( ℂ x ​ y 2, 𝔫) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most 𝔫 \mathfrak{n}. Then

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = ( t ​ ( 1 − t) 2 𝔠 2) i ​ ( 𝔠 2 ​ ( 𝔠 + 1 − t) t ​ ( 1 − t) 3) j ​ [( 1 − t) ​ ( 1 − 3 ​ t) 𝔠 2 ​ d ​ t − t ​ ( 1 − t) 2 𝔠 4 ​ d ​ 𝔠]. \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=\left(\frac{t(1-t)^{2}}{\mathfrak{c}^{2}}\right)^{i}\left(\frac{\mathfrak{c}^{2}(\mathfrak{c}+1-t)}{t(1-t)^{3}}\right)^{j}\left[\frac{(1-t)(1-3t)}{\mathfrak{c}^{2}}\,dt-\frac{t(1-t)^{2}}{\mathfrak{c}^{4}}\,d\mathfrak{c}\right]. |  |

Thus, we get

 | ∫ α 𝚒 ​ ( 𝔠) η i ​ j = ∫ α 𝚒 ​ ( 𝔠) η i ​ j t = ∫ α 𝚒 ​ ( 𝔠) ( − 1) 3 ​ j ​ 𝔠 2 ​ ( j − i − 1) ​ ( 𝔠 + 1 − t) j ​ ( 3 ​ t − 1) t j − i ​ ( t − 1) 3 ​ j − 2 ​ i − 1 ​ 𝑑 t. \int_{\alpha_{\tt i}(\mathfrak{c})}\eta_{ij}=\int_{\alpha_{\tt i}(\mathfrak{c})}\eta_{ij}^{t}=\int_{\alpha_{\tt i}(\mathfrak{c})}\frac{(-1)^{3j}\mathfrak{c}^{2(j-i-1)}(\mathfrak{c}+1-t)^{j}(3t-1)}{t^{j-i}(t-1)^{3j-2i-1}}\,dt. |  | (75) |

Case 𝚒 = 1 {\tt i}=1. If j − i ≤ 0 j-i\leq 0, then t 1 = 0 t_{1}=0 is not a pole of η i ​ j t \eta_{ij}^{t}. Hence, ∫ α 𝟷 ​ ( 𝔠) η i ​ j ≡ 0. \int_{\alpha_{\tt 1}(\mathfrak{c})}\eta_{ij}\equiv 0. If j − i ≥ 1 j-i\geq 1, then t 1 = 0 t_{1}=0 is a pole of η i ​ j t \eta_{ij}^{t} and it is clear that ∫ α 𝟷 ​ ( 𝔠) η i ​ j \int_{\alpha_{\tt 1}(\mathfrak{c})}\eta_{ij} a polynomial function in 𝔠 \mathfrak{c} of degree at most 3 ​ j − 2 ​ i − 2 ≤ 3 ​ j − 2 ≤ 3 ​ 𝔫 − 2 3j-2i-2\leq 3j-2\leq 3\mathfrak{n}-2. Hence, J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) is a polynomial of degree at most 3 ​ 𝔫 − 2 3\mathfrak{n}-2.

Case 𝚒 = 2 {\tt i}=2. If 3 ​ j − 2 ​ i − 1 ≤ 0 3j-2i-1\leq 0, then t 2 = 1 t_{2}=1 is not a pole of η i ​ j t \eta_{ij}^{t}. Hence, ∫ α 𝟸 ​ ( 𝔠) η i ​ j ≡ 0. \int_{\alpha_{\tt 2}(\mathfrak{c})}\eta_{ij}\equiv 0. If 3 ​ j − 2 ​ i − 1 > 0 3j-2i-1>0, then t 2 = 1 t_{2}=1 is a pole of η i ​ j t \eta_{ij}^{t}. Hence, from ( 75) and the criterion given in ( 64), we have

 | ∫ α 𝟸 ​ ( 𝔠) η i ​ j = ( − 1) 3 ​ j ​ ( 2 ​ π ​ − 1) ​ 𝔠 2 ​ ( j − i − 1) ( 3 ​ j − 2 ​ i − 2)! ​ ∂ 3 ​ j − 2 ​ i − 2 ∂ t 3 ​ j − 2 ​ i − 2 ​ ( 𝔠 + 1 − t) j ​ ( 3 ​ t − 1) t j − i | t = 1. \int_{\alpha_{\tt 2}(\mathfrak{c})}\eta_{ij}=\frac{(-1)^{3j}\left(2\pi\sqrt{-1}\right)\,\mathfrak{c}^{2(j-i-1)}}{(3j-2i-2)!}\frac{\partial^{3j-2i-2}}{\partial t^{3j-2i-2}}\frac{(\mathfrak{c}+1-t)^{j}(3t-1)}{t^{j-i}}\Big|_{t=1}. |  |

It is clear that that

 | ∂ 3 ​ j − 2 ​ i − 2 ∂ t 3 ​ j − 2 ​ i − 2 ​ ( 𝔠 + 1 − t) j ​ ( 3 ​ t − 1) t j − i | t = 1 = ∑ μ = 0 j ( j μ) ​ 𝔠 μ ​ ∂ 3 ​ j − 2 ​ i − 2 ∂ t 3 ​ j − 2 ​ i − 2 ​ ( 3 ​ t − 1) ​ ( 1 − t) j − μ t j − i | t = 1. \frac{\partial^{3j-2i-2}}{\partial t^{3j-2i-2}}\frac{(\mathfrak{c}+1-t)^{j}(3t-1)}{t^{j-i}}\Big|_{t=1}=\sum_{\mu=0}^{j}{j\choose\mu}\mathfrak{c}^{\mu}\,\frac{\partial^{3j-2i-2}}{\partial t^{3j-2i-2}}\frac{(3t-1)(1-t)^{j-\mu}}{t^{j-i}}\Big|_{t=1}. |  |

From the general Leibniz rule, we know that the derivative

 | ∂ 3 ​ j − 2 ​ i − 2 ∂ t 3 ​ j − 2 ​ i − 2 ​ ( 3 ​ t − 1) ​ ( 1 − t) j − μ t j − i | t = 1 \frac{\partial^{3j-2i-2}}{\partial t^{3j-2i-2}}\frac{(3t-1)(1-t)^{j-\mu}}{t^{j-i}}\Big|_{t=1} |  | (76) |

can be written as

 | ∑ ν = 0 3 ​ j − 2 ​ i − 2 ( 3 ​ j − 2 ​ i − 2 ν) ​ ( ( 1 − t) j − μ) ( ν) ​ ( ( 3 ​ t − 1) ​ ( t i − j)) ( 3 ​ j − 2 ​ i − 2 − ν) | t = 1, \sum_{\nu=0}^{3j-2i-2}{3j-2i-2\choose\nu}\left((1-t)^{j-\mu}\right)^{(\nu)}\left((3t-1)(t^{i-j})\right)^{(3j-2i-2-\nu)}\Big|_{t=1}, |  |

which is different from zero only if

 | ν = j − μ and 3 ​ j − 2 ​ i − 3 − ν ≤ i − j \nu=j-\mu\quad\mbox{and}\quad 3j-2i-3-\nu\leq i-j |  |

or equivalently

 | − 2 ​ ( j − i − 1) ≤ μ ≤ 3 ​ ( i − j + 1). -2(j-i-1)\leq\mu\leq 3(i-j+1). |  |

Thus, we have two cases: j − i − 1 ≥ 0 j-i-1\geq 0 and i − j + 1 > 0 i-j+1>0. In the first one, analogously to the previous paragraph, ∫ α 𝟸 ​ ( 𝔠) η i ​ j \int_{\alpha_{\tt 2}(\mathfrak{c})}\eta_{ij} is a polynomial of degree at most 3 ​ 𝔫 − 2 3\mathfrak{n}-2. In the second one, we obtain that 𝔠 \mathfrak{c} in ∫ α 𝟸 ​ ( 𝔠) η i ​ j \int_{\alpha_{\tt 2}(\mathfrak{c})}\eta_{ij} has degree 2 ​ ( j − i − 1) + μ 2(j-i-1)+\mu and according to previous equation

 | 0 ≤ 2 ​ ( j − i − 1) + μ ≤ i − j + 1. 0\leq 2(j-i-1)+\mu\leq i-j+1. |  |

Hence, also in this case ∫ α 𝟸 ​ ( 𝔠) η i ​ j \int_{\alpha_{\tt 2}(\mathfrak{c})}\eta_{ij} is a polynomial function of maximum degree [( 𝔫 + 2) / 6] [(\mathfrak{n}+2)/6], which can be deduced from the conditions 3 ​ j − 2 ​ i − 1 > 0 3j-2i-1>0, i − j + 1 > 0 i-j+1>0 and i + j ≤ 𝔫 i+j\leq\mathfrak{n}. Therefore, J 2 ​ ( 𝔠) J_{2}(\mathfrak{c}) is a polynomial of degree at most 3 ​ 𝔫 − 2 3\mathfrak{n}-2. In conclusion,

 | Z ⁡ ( ℐ 𝚒 ​ ( 𝔠)) = Z ⁡ ( J 𝚒 ​ ( 𝔠)) ≤ 3 ​ 𝔫 − 2, 𝚒 ∈ { 1, 2 }. Z(\mathcal{I}_{\tt i}(\mathfrak{c}))=Z(J_{\tt i}(\mathfrak{c}))\leq 3\mathfrak{n}-2,\quad{\tt i}\in\{1,2\}. |  |

If ϑ \vartheta is non-conservative for B ​ C ​ ( ℋ) BC(\mathcal{H}), then we have

 | 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) = 𝒩 B ​ C ​ ( 𝔠) ​ ( η) = ≤ 2 ​ ( 3 ​ 𝔫 − 2). \mathscr{N}_{BC(\mathcal{H})}(\vartheta)=\mathscr{N}_{BC(\mathfrak{c})}(\eta)=\leq 2(3\mathfrak{n}-2). |  |

As an explicit example we take the polynomial 1-form

 | ϑ 0 = y ⁡ ( y 2 − 108 ​ x ​ y − 66) ​ d ​ x \vartheta_{0}=y(y^{2}-108xy-66)\,dx |  |

of degree 𝔫 = 3 \mathfrak{n}=3, which is non-conservative for B ​ C ​ ( ℋ) BC(\mathcal{H}) because

 | ℐ 1 ​ ( 𝔠) = J 1 ​ ( 𝔠) \displaystyle\mathcal{I}_{1}(\mathfrak{c})=J_{1}(\mathfrak{c}) | = 3 ​ ( 2 ​ π ​ − 1) ​ ( 𝔠 + 1) ​ ( 4 ​ 𝔠 6 + 3 ​ 𝔠 5 − 36 ​ 𝔠 − 58), \displaystyle=3\left(2\pi\sqrt{-1}\right)(\mathfrak{c}+1)(4\mathfrak{c}^{6}+3\mathfrak{c}^{5}-36\mathfrak{c}-58), |  |

 | ℐ 2 ​ ( 𝔠) = J 2 ​ ( 𝔠) \displaystyle\mathcal{I}_{2}(\mathfrak{c})=J_{2}(\mathfrak{c}) | = − 3 ​ ( 2 ​ π ​ − 1) ​ ( 𝔠 − 1) ​ ( 𝔠 + 2) ​ ( 4 ​ 𝔠 5 + 3 ​ 𝔠 4 + 8 ​ 𝔠 3 − 2 ​ 𝔠 2 + 18 ​ 𝔠 − 58). \displaystyle=-3\left(2\pi\sqrt{-1}\right)(\mathfrak{c}-1)(\mathfrak{c}+2)(4\mathfrak{c}^{5}+3\mathfrak{c}^{4}+8\mathfrak{c}^{3}-2\mathfrak{c}^{2}+18\mathfrak{c}-58). |  |

Hence, ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) has 6 = 3 ​ 𝔫 − 3 6=3\mathfrak{n}-3 zeros in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}) and ℐ 2 ​ ( 𝔠) \mathcal{I}_{2}(\mathfrak{c}) has 7 = 3 ​ 𝔫 − 2 7=3\mathfrak{n}-2 zeros in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}). The zeros of ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) are different from the zeros of ℐ 2 ​ ( 𝔠) \mathcal{I}_{2}(\mathfrak{c}). Therefore, we have

 | 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ 0) = 6 + 7 = 13. \mathscr{N}_{BC(\mathcal{H})}(\vartheta_{0})=6+7=13. |  |

### 5.4. A non-isotrivial polynomial of type ( 0, 4) (0,4) in family 𝔉 1 \mathfrak{F}_{1}

We consider the polynomial

 | ℋ ⁡ ( x, y) = x ​ ( x ​ y − 1) 2 + ( x ​ y − 1) ​ ( 1 − x ​ ( x ​ y − 1) 2), \mathcal{H}(x,y)=x(xy-1)^{2}+(xy-1)(1-x(xy-1)^{2}), |  |

which belongs to the Neumann–Norbury family 𝔉 1 \mathfrak{F}_{1}, with r = 2 r=2, a 1 = 1 a_{1}=1, β 1 = 1 \beta_{1}=1, p 1 = 0 p_{1}=0, p = 1 p=1, q 1 = 1 q_{1}=1, q = 2 q=2 and 𝒮 ⁡ ( x, y) = x ​ y − 1 \mathcal{S}(x,y)=xy-1. Again, we will apply Steps 2–4 of the Program for the study of the infinitesimal perturbed Hamiltonian differential equation d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0, where ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}.

From Lemma 14 and ( 26), let 𝒢 ⁡ ( x, y) = x ​ ( x ​ y − 1) 2 \mathcal{G}(x,y)=x(xy-1)^{2}, then ℛ = ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) \mathcal{R}=(\mathcal{G}(x,y),\mathcal{H}(x,y)) is a rectifying map for ℋ \mathcal{H}. In this case, Σ ( ℛ) = { x ( x y − 1) 2 ( 1 − x ( x y − 1) 2) = 0 } \Sigma(\mathcal{R})=\{x(xy-1)^{2}\left(1-x(xy-1)^{2}\right)=0\} and ( 46) becomes

 | ℂ x ​ y 2 \ Σ ⁡ ( ℛ) → ℛ ℂ t ​ 𝔠 2 \ { t ( 1 − t) ( 𝔠 − t) = 0 } ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℛ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( t ​ ( 1 − t) 2 ( 𝔠 − t) 2, ( 𝔠 + 1 − 2 ​ t) ​ ( 𝔠 − t) 2 t ​ ( 1 − t) 3). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\{t(1-t)(\mathfrak{c}-t)=0\}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{R})\\ &&&&\\ (x,y)&\longmapsto&(\mathcal{G}(x,y),\mathcal{H}(x,y))&\longmapsto&\Big(\frac{t(1-t)^{2}}{(\mathfrak{c}-t)^{2}},\frac{(\mathfrak{c}+1-2t)(\mathfrak{c}-t)^{2}}{t(1-t)^{3}}\Big).\end{array} |  |

Thus,

 | ℛ ∗ ​ ( d ​ ℋ + ε ​ ϑ) = d ​ 𝔠 + ε ​ η = 0, η = ℛ ∗ ​ ( ϑ). \mathcal{R}_{*}\big(d\mathcal{H}+\varepsilon\vartheta\big)=d\mathfrak{c}+\varepsilon\eta=0,\quad\eta=\mathcal{R}_{*}(\vartheta). |  | (77) |

The polynomial ℋ \mathcal{H} has only two finite critical points at ( 0, − 1) (0,-1) and ( 1, 2) (1,2), with critical values ℋ ⁡ ( 0, − 2) = − 1 \mathcal{H}(0,-2)=-1 and ℋ ⁡ ( 1, 2) = 1 \mathcal{H}(1,2)=1, and its fiber ℒ 0 \mathcal{L}_{0} is the disjoint union of two algebraic curves , thus 𝔅 f ​ i ​ n ​ ( ℋ) = { − 1, 1 } \mathfrak{B}_{fin}(\mathcal{H})=\{-1,1\} and 0 ∈ 𝔅 i ​ n ​ f ​ ( ℋ) 0\in\mathfrak{B}_{inf}(\mathcal{H}).

In addition, each fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}}, with 𝔠 ∉ { 0, − 1, 1 } \mathfrak{c}\not\in\{0,-1,1\}, of ℋ \mathcal{H} is biholomorphically mapped, through ℛ \mathcal{R}, into the horizontal line ( ℂ ∖ { 0, 1, 𝔠 }) × { 𝔠 } ⊂ ℂ t, 𝔠 2 \big(\mathbb{C}\setminus\{0,1,\mathfrak{c}\}\big)\times\{\mathfrak{c}\}\subset\mathbb{C}^{2}_{t,\,\mathfrak{c}}, with the points ( 0, 𝔠) (0,\mathfrak{c}), ( 1, 𝔠) (1,\mathfrak{c}) and ( 𝔠, 𝔠) (\mathfrak{c},\mathfrak{c}) removed. See Figure 5. Thus, 𝔅 ⁡ ( ℋ) = { 0, − 1, 1 } \mathfrak{B}(\mathcal{H})=\{0,-1,1\}. Hence, H H is of type ( 0, 4) (0,4) and for 𝔠 ∉ { 0, − 1, 1 } \mathfrak{c}\not\in\{0,-1,1\}, we have

 | dim H 1 ​ ( ℒ 𝔠, ℤ) = dim H 1 ​ ( ( ℂ ∖ { 0, 1, 𝔠 }) × { 𝔠 }, ℤ) = 3. \dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=\dim H_{1}\left(\big(\mathbb{C}\setminus\{0,1,\mathfrak{c}\}\big)\times\{\mathfrak{c}\},\mathbb{Z}\right)=3. |  | (78) |

Figure 5. Let ℋ ⁡ ( x, y) = x ​ ( x ​ y − 1) 2 + ( x ​ y − 1) ​ ( 1 − x ​ ( x ​ y − 1) 2) \mathcal{H}(x,y)=x(xy-1)^{2}+(xy-1)(1-x(xy-1)^{2}), we sketch of the leaves of the foliations d ​ ℋ = 0 d\mathcal{H}=0 and d ​ 𝔠 = 0 d\mathfrak{c}=0. The magenta curves correspond to (complex) connected components of the singular fibers of ℋ \mathcal{H}. The dashed red curves mean that they have been removed from the respective planes.

In this case, the canonical global generators of the unperturbed differential equations are of the form

B ​ C ​ ( ℋ) = { δ 𝟷 ​ ( 𝔠), δ 𝟸 ​ ( 𝔠), δ 𝟹 ​ ( 𝔠) } BC(\mathcal{H})=\{\delta_{\tt 1}(\mathfrak{c}),\delta_{\tt 2}(\mathfrak{c}),\delta_{\tt 3}(\mathfrak{c})\} and B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠), α 𝟸 ​ ( 𝔠), α 𝟹 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c}),\alpha_{\tt 2}(\mathfrak{c}),\alpha_{\tt 3}(\mathfrak{c})\}.

Therefore, there are three Abelian integrals ℐ 1 ​ ( c) \mathcal{I}_{1}(c), ℐ 2 ​ ( c) \mathcal{I}_{2}(c) and ℐ 3 ​ ( c) \mathcal{I}_{3}(c) defined by the pair ( ℋ, ϑ) (\mathcal{H},\vartheta), which are rationally equivalent to three Abelian integral J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}), J 2 ​ ( 𝔠) J_{2}(\mathfrak{c}) and J 3 ​ ( 𝔠) J_{3}(\mathfrak{c}) defined by the pair ( 𝔠, η) (\mathfrak{c},\eta). Thus,

 | Z ⁡ ( ℐ 𝚒 ​ ( 𝔠)) = Z ⁡ ( J 𝚒 ​ ( 𝔠)) 𝚒 ∈ { 1, 2, 3 }. Z(\mathcal{I}_{\tt i}(\mathfrak{c}))=Z(J_{\tt i}(\mathfrak{c}))\quad{\tt i}\in\{1,2,3\}. |  |

We choose the canonical global generators B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠), α 𝟸 ​ ( 𝔠), α 𝟹 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c}),\alpha_{\tt 2}(\mathfrak{c}),\alpha_{\tt 3}(\mathfrak{c})\} of d ​ 𝔠 = 0 d\mathfrak{c}=0, where α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) is a small cycle around the puncture ( t 𝚒, 𝔠) (t_{\tt i},\mathfrak{c}) in the line ( ℂ ∖ { 0, 1, 𝔠 }) × { 𝔠 } \big(\mathbb{C}\setminus\{0,1,\mathfrak{c}\}\big)\times\{\mathfrak{c}\}, with t 1 = 0 t_{1}=0, t 2 = 1 t_{2}=1 and t 3 = 𝔠 t_{3}=\mathfrak{c}. We have the Abelian integrals

 | ℐ 𝚒 ​ ( 𝔠) = J 𝚒 ​ ( 𝔠) = ∫ α 𝚒 ​ ( 𝔠) η, 𝚒 ∈ { 1, 2, 3 }. \mathcal{I}_{\tt i}(\mathfrak{c})=J_{\tt i}(\mathfrak{c})=\int_{\alpha_{\tt i}(\mathfrak{c})}\eta,\quad{\tt i}\in\{1,2,3\}. |  |

For computing ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) it is sufficient to consider the basis B n ​ e 1 ( ℂ x ​ y 2, 𝔫) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most 𝔫 \mathfrak{n}, by Lemma 16. The push-forward ℛ ∗ ​ ( ϑ i ​ j) \mathcal{R}_{*}(\vartheta_{ij}) is then

 | η i ​ j = t i ​ ( 1 − t) 2 ​ i ( 𝔠 − t) 2 ​ i ​ ( 𝔠 + 1 − 2 ​ t) j ​ ( 𝔠 − t) 2 ​ j t j ​ ( 1 − t) 3 ​ j ​ [( 1 − t) ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) ( 𝔠 − t) 3 ​ d ​ t − 2 ​ t ​ ( 1 − t) 2 ( 𝔠 − t) 3 ​ d ​ 𝔠]. \eta_{ij}=\frac{t^{i}(1-t)^{2i}}{(\mathfrak{c}-t)^{2i}}\,\frac{(\mathfrak{c}+1-2t)^{j}(\mathfrak{c}-t)^{2j}}{t^{j}(1-t)^{3j}}\left[\frac{(1-t)(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{(\mathfrak{c}-t)^{3}}\,dt-\frac{2t(1-t)^{2}}{(\mathfrak{c}-t)^{3}}\,d\mathfrak{c}\right]. |  |

Thus,

 | η i ​ j t = ( 𝔠 + 1 − 2 ​ t) j ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t j − i ​ ( 1 − t) 3 ​ j − 2 ​ i − 1 ​ ( 𝔠 − t) 2 ​ i − 2 ​ j + 3 ​ d ​ t. \eta_{ij}^{t}=\frac{(\mathfrak{c}+1-2t)^{j}(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t^{j-i}(1-t)^{3j-2i-1}(\mathfrak{c}-t)^{2i-2j+3}}\,dt. |  |

By applying Newton’s binomial theorem, we have

 | η i ​ j t = ∑ μ = 0 j ( j μ) ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t j − i ​ ( t − 1) 2 ​ j − 2 ​ i − 1 + μ ​ ( t − 𝔠) 2 ​ i − 2 ​ j + 3 − μ ​ d ​ t. \eta_{ij}^{t}=\sum_{\mu=0}^{j}{j\choose\mu}\frac{(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t^{j-i}(t-1)^{2j-2i-1+\mu}(t-\mathfrak{c})^{2i-2j+3-\mu}}\,dt. |  | (79) |

Case 𝚒 = 1 {\tt i}=1. If j − i ≤ 0 j-i\leq 0, then t 1 = 0 t_{1}=0 is not a pole of η i ​ j 1 \eta_{ij}^{1}. Thus, ∫ α 𝟷 ​ ( 𝔠) η i ​ j ≡ 0. \int_{\alpha_{\tt 1}(\mathfrak{c})}\eta_{ij}\equiv 0. If j − i = 1 j-i=1, then t 1 = 0 t_{1}=0 is a pole of order one of η i ​ j 1 \eta_{ij}^{1} and form ( 79), we get

 | ∫ α 𝟷 ​ ( 𝔠) η i, i + 1 = ∑ μ = 0 i + 1 ( i + 1 μ) ​ ∫ α 𝟷 ​ ( 𝔠) ( t − 𝔠) μ − 1 ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t ​ ( t − 1) 1 + μ ​ 𝑑 t. \int_{\alpha_{\tt 1}(\mathfrak{c})}\eta_{i,i+1}=\sum_{\mu=0}^{i+1}{i+1\choose\mu}\int_{\alpha_{\tt 1}(\mathfrak{c})}\frac{(t-\mathfrak{c})^{\mu-1}(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t(t-1)^{1+\mu}}\,dt. |  |

It is clear that for μ ≥ 1 \mu\geq 1, every integral on the right-hand side is a polynomial function in 𝔠 \mathfrak{c}. Moreover, for μ = 0 \mu=0 and according to the criterion given in ( 64), we have

 | ∫ α 𝟷 ​ ( 𝔠) ( t − 𝔠) − 1 ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t ⁡ ( t − 1) ​ 𝑑 t = ( 2 ​ π ​ − 1) ​ t 2 + t + 𝔠 − 3 ​ t ​ 𝔠 ( t − 1) ​ ( t − 𝔠) | t = 0 = 2 ​ π ​ − 1. \int_{\alpha_{\tt 1}(\mathfrak{c})}\frac{(t-\mathfrak{c})^{-1}(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t(t-1)}\,dt=\left(2\pi\sqrt{-1}\right)\,\frac{t^{2}+t+\mathfrak{c}-3t\mathfrak{c}}{(t-1)(t-\mathfrak{c})}\Big|_{t=0}=2\pi\sqrt{-1}. |  |

Hence, ∫ α 𝟷 ​ ( 𝔠) η i, i + 1 \int_{\alpha_{\tt 1}(\mathfrak{c})}\eta_{i,i+1} is a polynomial function of degree at most i + 1 = [( 𝔫 + 1) / 2] i+1=[(\mathfrak{n}+1)/2]. If j − i > 1 j-i>1, then 2 ​ i − 2 ​ j + 3 − μ ≤ 0 2i-2j+3-\mu\leq 0. Thus, from ( 79) is clear that in this case ∫ α 𝟷 ​ ( 𝔠) η i ​ j \int_{\alpha_{\tt 1}(\mathfrak{c})}\eta_{ij} is a polynomial, of degree at most 3 ​ j − 2 ​ i − 2 ≤ 3 ​ j − 2 ≤ 3 ​ 𝔫 − 2 3j-2i-2\leq 3j-2\leq 3\mathfrak{n}-2. Hence, we have that J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) is a polynomial function of degree at most 3 ​ 𝔫 − 2 3\mathfrak{n}-2.

Case 𝚒 = 2 {\tt i}=2. If 2 ​ j − 2 ​ i − 1 + μ ≤ 0 2j-2i-1+\mu\leq 0, then t 2 = 1 t_{2}=1 is not a pole of the corresponding term in ( 79). Thus, ∫ α 𝟸 ​ ( 𝔠) η i ​ j ≡ 0 \int_{\alpha_{\tt 2}(\mathfrak{c})}\eta_{ij}\equiv 0. If 2 ​ j − 2 ​ i − 1 + μ = 1 2j-2i-1+\mu=1, then t 2 = 1 t_{2}=1 is a pole of order one of the corresponding term in ( 79), whence

 | ∫ α 𝟸 ​ ( 𝔠) ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t 1 − μ / 2 ​ ( t − 1) ​ ( t − 𝔠) ​ 𝑑 t = ( 2 ​ π ​ − 1) ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t 1 − μ / 2 ​ ( t − 𝔠) | t = 1 = 4 ​ π ​ − 1, \int_{\alpha_{\tt 2}(\mathfrak{c})}\frac{(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t^{1-\mu/2}(t-1)(t-\mathfrak{c})}\,dt=\left(2\pi\sqrt{-1}\right)\,\frac{(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t^{1-\mu/2}(t-\mathfrak{c})}\Big|_{t=1}=4\pi\sqrt{-1}, |  |

by applying the criterion given in ( 64). If 2 ​ j − 2 ​ i − 1 + μ > 1 2j-2i-1+\mu>1, then 2 ​ i − 2 ​ j + 3 − μ < 1 2i-2j+3-\mu<1. Thus, the integral of the corresponding term in ( 79) is a polynomial function of degree at most 2 ​ j − 2 ​ i − 2 + μ ≤ 3 ​ j − 2 ≤ 3 ​ 𝔫 − 2 2j-2i-2+\mu\leq 3j-2\leq 3\mathfrak{n}-2. Hence, J 2 ​ ( 𝔠) J_{2}(\mathfrak{c}) is a polynomial function of degree at most 3 ​ 𝔫 − 2 3\mathfrak{n}-2.

Case 𝚒 = 3 {\tt i}=3. If 2 ​ i − 2 ​ j + 3 − μ ≤ 0 2i-2j+3-\mu\leq 0, then t 3 = 𝔠 t_{3}=\mathfrak{c} is not a pole of the corresponding term in ( 79). Thus, ∫ α 𝟹 ​ ( 𝔠) η i ​ j ≡ 0 \int_{\alpha_{\tt 3}(\mathfrak{c})}\eta_{ij}\equiv 0. If 2 ​ i − 2 ​ j + 3 − μ = 1 2i-2j+3-\mu=1, then μ \mu is even and t 3 = 𝔠 t_{3}=\mathfrak{c} is a pole of order one of the corresponding term in ( 79), whose integral is

 | ∫ α 𝟹 ​ ( 𝔠) ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t 1 − μ / 2 ​ ( t − 1) ​ ( t − 𝔠) ​ 𝑑 t = ( 2 ​ π ​ − 1) ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) t 1 − μ / 2 ​ ( t − 1) | t = 𝔠 = 4 ​ π ​ − 1 ​ c μ 2, \int_{\alpha_{\tt 3}(\mathfrak{c})}\frac{(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t^{1-\mu/2}(t-1)(t-\mathfrak{c})}\,dt=\left(2\pi\sqrt{-1}\right)\,\frac{(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})}{t^{1-\mu/2}(t-1)}\Big|_{t=\mathfrak{c}}=4\pi\sqrt{-1}c^{\frac{\mu}{2}}, |  |

applying the criterion given in ( 64) and it is a polynomial of degree at most [𝔫 / 2] [\mathfrak{n}/2]. If 2 ​ i − 2 ​ j + 3 − μ > 1 2i-2j+3-\mu>1, then 2 ​ j − 2 ​ i − 1 + μ < 1 2j-2i-1+\mu<1 and 2 ​ ( i − j) > μ − 2 2(i-j)>\mu-2. Thus 2 ​ j − 2 ​ i − 1 + μ ≤ 0 2j-2i-1+\mu\leq 0 and i − j ≥ 0 i-j\geq 0. Moreover, t 3 = 𝔠 t_{3}=\mathfrak{c} is a pole of order greater than one of the corresponding term in ( 79), whose integral is

 | ∫ α 𝟹 ​ ( 𝔠) ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) ​ t i − j ​ ( t − 1) 2 ​ i − 2 ​ j + 1 − μ ( t − 𝔠) 2 ​ i − 2 ​ j + 3 − μ ​ 𝑑 t. \int_{\alpha_{\tt 3}(\mathfrak{c})}\frac{(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})t^{i-j}(t-1)^{2i-2j+1-\mu}}{(t-\mathfrak{c})^{2i-2j+3-\mu}}\,dt. |  |

By the criterion given in ( 64), the previous integral is equal to

 | 2 ​ π ​ − 1 ( 2 ​ i − 2 ​ j + 2 − μ)! ​ ∂ 2 ​ i − 2 ​ j + 2 − μ ∂ t 2 ​ i − 2 ​ j + 2 − μ ​ ( t 2 + t + 𝔠 − 3 ​ t ​ 𝔠) ​ t i − j ​ ( t − 1) 2 ​ i − 2 ​ j + 1 − μ | t = 𝔠, \frac{2\pi\sqrt{-1}}{(2i-2j+2-\mu)!}\frac{\partial^{2i-2j+2-\mu}}{\partial t^{2i-2j+2-\mu}}(t^{2}+t+\mathfrak{c}-3t\mathfrak{c})t^{i-j}(t-1)^{2i-2j+1-\mu}\Big|_{t=\mathfrak{c}}, |  |

which is a polynomial function of degree at most i − j + 1 ≤ i ≤ 𝔫 − 1 i-j+1\leq i\leq\mathfrak{n}-1. Therefore, J 3 ​ ( 𝔠) J_{3}(\mathfrak{c}) is a polynomial function of degree at most 𝔫 − 1 \mathfrak{n}-1.

In conclusion,

 | Z ⁡ ( ℐ 𝚒 ​ ( 𝔠)) = Z ⁡ ( J 𝚒 ​ ( 𝔠)) ≤ 3 ​ 𝔫 − 2, 𝚒 ∈ { 1, 2 } Z(\mathcal{I}_{\tt i}(\mathfrak{c}))=Z(J_{\tt i}(\mathfrak{c}))\leq 3\mathfrak{n}-2,\quad{\tt i}\in\{1,2\} |  |

and

 | Z ⁡ ( ℐ 3 ​ ( 𝔠)) = Z ⁡ ( J 3 ​ ( 𝔠)) ≤ 𝔫 − 1. Z(\mathcal{I}_{3}(\mathfrak{c}))=Z(J_{3}(\mathfrak{c}))\leq\mathfrak{n}-1. |  |

If ϑ \vartheta is non-conservative for B ​ C ​ ( ℋ) BC(\mathcal{H}), the we have

 | 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) = 𝒩 B ​ C ​ ( 𝔠) ​ ( η) = ≤ 2 ​ ( 3 ​ 𝔫 − 2) + 𝔫 − 1. \mathscr{N}_{BC(\mathcal{H})}(\vartheta)=\mathscr{N}_{BC(\mathfrak{c})}(\eta)=\leq 2(3\mathfrak{n}-2)+\mathfrak{n}-1. |  |

As an explicit example, we take the polynomial 1-form

 | ϑ 0 = y ⁡ ( y 2 − 96 ​ x 2 + 1008) ​ d ​ x \vartheta_{0}=y(y^{2}-96x^{2}+1008)\,dx |  |

of degree 𝔫 = 3 \mathfrak{n}=3, which is non-conservative for B ​ C ​ ( ℋ) BC(\mathcal{H}) because

 | ℐ 1 ​ ( 𝔠) = J 1 ​ ( 𝔠) \displaystyle\mathcal{I}_{1}(\mathfrak{c})=J_{1}(\mathfrak{c}) | = 6 ​ ( 2 ​ π ​ − 1) ​ ( 𝔠 + 1) ​ ( 2 ​ 𝔠 6 − 2 ​ 𝔠 5 − 𝔠 4 + 𝔠 3 + 168), \displaystyle=6\left(2\pi\sqrt{-1}\right)(\mathfrak{c}+1)(2\mathfrak{c}^{6}-2\mathfrak{c}^{5}-\mathfrak{c}^{4}+\mathfrak{c}^{3}+168), |  |

 | ℐ 2 ​ ( 𝔠) = J 2 ​ ( 𝔠) \displaystyle\mathcal{I}_{2}(\mathfrak{c})=J_{2}(\mathfrak{c}) | = − 6 ​ ( 2 ​ π ​ − 1) ​ ( 𝔠 − 2) ​ ( 2 ​ 𝔠 6 + 4 ​ 𝔠 5 + 5 ​ 𝔠 4 + 10 ​ 𝔠 3 + 21 ​ 𝔠 2 + 42 ​ 𝔠 + 252), \displaystyle=-6\left(2\pi\sqrt{-1}\right)(\mathfrak{c}-2)(2\mathfrak{c}^{6}+4\mathfrak{c}^{5}+5\mathfrak{c}^{4}+10\mathfrak{c}^{3}+21\mathfrak{c}^{2}+42\mathfrak{c}+252), |  |

 | ℐ 3 ​ ( 𝔠) = J 3 ​ ( 𝔠) \displaystyle\mathcal{I}_{3}(\mathfrak{c})=J_{3}(\mathfrak{c}) | = 96 ​ ( 2 ​ π ​ − 1) ​ ( 2 ​ 𝔠 + 5) ​ ( 𝔠 − 4). \displaystyle=96\left(2\pi\sqrt{-1}\right)(2\mathfrak{c}+5)(\mathfrak{c}-4). |  |

Hence, ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) has 6 = 3 ​ 𝔫 − 3 6=3\mathfrak{n}-3 zeros in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}), ℐ 2 ​ ( 𝔠) \mathcal{I}_{2}(\mathfrak{c}) has 7 = 3 ​ 𝔫 − 2 7=3\mathfrak{n}-2 zeros in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}) and ℐ 3 ​ ( 𝔠) \mathcal{I}_{3}(\mathfrak{c}) has 2 = 𝔫 − 1 2=\mathfrak{n}-1 zeros in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}). The zeros of the three Abelian integrals are different. Therefore, we have

 | 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ 0) = 6 + 7 + 2 = 15. \mathscr{N}_{BC(\mathcal{H})}(\vartheta_{0})=6+7+2=15. |  | (80) |

###### Remark 9.

For each l ∈ ℤ l\in\mathbb{Z}, we consider the homology cycles

 | β l ​ ( 𝔠) ≐ l ​ α 𝟷 ​ ( 𝔠) + l ​ α 𝟸 ​ ( 𝔠) + α 𝟹 ​ ( 𝔠), \beta_{l}(\mathfrak{c})\doteq l\,\alpha_{\tt 1}(\mathfrak{c})+l\,\alpha_{\tt 2}(\mathfrak{c})+\alpha_{\tt 3}(\mathfrak{c}), |  |

and obtain

 | ∫ β l ​ ( 𝔠) ϑ 0 = l ​ ∫ α 𝟷 ​ ( 𝔠) ϑ 0 + l ​ ∫ α 𝟸 ​ ( 𝔠) ϑ 0 + ∫ α 𝟹 ​ ( 𝔠) ϑ 0 = 96 ​ ( 2 ​ π ​ − 1) ​ ( 2 ​ 𝔠 + 5) ​ ( 𝔠 − 4) + 4032 ​ l. \int_{\beta_{l}(\mathfrak{c})}\vartheta_{0}=l\int_{\alpha_{\tt 1}(\mathfrak{c})}\vartheta_{0}+l\int_{\alpha_{\tt 2}(\mathfrak{c})}\vartheta_{0}+\int_{\alpha_{\tt 3}(\mathfrak{c})}\vartheta_{0}=96\left(2\pi\sqrt{-1}\right)(2\mathfrak{c}+5)(\mathfrak{c}-4)+4032\,l. |  |

This polynomial has two different zeros 𝔠 ^ l \hat{\mathfrak{c}}_{l} and 𝔠 ~ l \tilde{\mathfrak{c}}_{l}. Thus, both β ^ l ​ ( 0) ≐ β l ​ ( 𝔠 ^ l) \hat{\beta}_{l}(0)\doteq\beta_{l}(\hat{\mathfrak{c}}_{l}) and β ~ l ​ ( 0) ≐ β l ​ ( 𝔠 ~ l) \tilde{\beta}_{l}(0)\doteq\beta_{l}(\tilde{\mathfrak{c}}_{l}) generate a limit cycle of the perturbed infinitesimal Hamiltonian differential equation d ​ ℋ + ε ​ ϑ 0 = 0 d\mathcal{H}+\varepsilon\vartheta_{0}=0. Therefore, this differential equation has an infinite number of limit cycles { β ^ l ( ε), β ~ l ( ε) | l ∈ ℤ } \{\hat{\beta}_{l}(\varepsilon),\tilde{\beta}_{l}(\varepsilon)\ |\ l\in\mathbb{Z}\}.

### 5.5. Primitive polynomials of type ( 0, 2) (0,2)

Recall that the simplest non-trivial case for the study of Abelian integrals is when the polynomial H H is primitive of type ( 0, 2) (0,2). The Abelian integrals for the family of these polynomial were studied in [28]. In order to show the advantage of the Program § 3, we will finish this section by studying this family of polynomials.

Let H ⁡ ( u, v) H(u,v) be a primitive polynomial of type ( 0, 2) (0,2) of degree m + 1 m+1. Consider a polynomial 1-form ω ∈ Ω n ​ e 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega_{ne}^{1}(\mathbb{C}^{2}_{u\,v})_{\leq n} and the infinitesimal perturbed Hamiltonian differential equation d ​ H + ε ​ ω = 0 dH+\varepsilon\omega=0.

By using the notation of the Neumann–Norbury families, the Miyanishi–Sugie classification given in Theorem 9 can be expressed as

 | { ℋ ⁡ ( x, y) = x p 1 ​ ( x k ​ y + P ⁡ ( x)) p | p 1, p ∈ ℕ, ( p 1, p) = 1, k ∈ ℕ 0, P ⁡ ( x) ∈ ℂ ​ [x] ≤ k − 1, P ⁡ ( 0) ≠ 0 if k > 0, and P ⁡ ( x) ≡ 0 if k = 0 }. \left\{\mathcal{H}(x,y)=x^{p_{1}}\Big(x^{k}y+P(x)\Big)^{p}\,\Big|\,\begin{array}[]{l}p_{1},p\in\mathbb{N},\,(p_{1},p)=1,\,k\in\mathbb{N}_{0},\,P(x)\in\mathbb{C}[x]_{\leq k-1},\\ \textrm{$P(0)\not=0$ if $k>0$, and $P(x)\equiv 0$ if $k=0$}\end{array}\!\!\right\}. |  |

We know from Theorem 9 and Lemma 12 that the polynomials of the previous family are normal forms of the primitive polynomials of type ( 0, 2) (0,2).

Step 1. There exists a pair ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}) such that H ⁡ ( u, v) H(u,v) and

 | ℋ ⁡ ( x, y) = x p 1 ​ ( x k ​ y + P ⁡ ( x)) p \mathcal{H}(x,y)=x^{p_{1}}\big(x^{k}y+P(x)\big)^{p} |  |

are algebraically equivalent. Since H H and ℋ \mathcal{H} are of type ( 0, 2) (0,2), there exists a unique Abelian integral I 1 ​ ( c) I_{1}(c) defined by H H and ω \omega, which is algebraically equivalent to the unique Abelian integral ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) defined by ℋ \mathcal{H} and ϑ \vartheta. Thus, the two first columns of diagram ( 25) hold. In particular, according to Corollary 5 and ( 14),

 | σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω) = d ​ ℋ + ε ​ ϑ, ϑ = σ ′ ​ ψ ∗ ​ ( ω). \sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)=d\mathcal{H}+\varepsilon\vartheta,\qquad\vartheta=\sigma^{\prime}\psi_{*}(\omega). |  |

From Lemma 12 and Proposition 13, we get that

 | deg ⁡ ( ϑ) ≤ ( n + 1) ​ ( m) − 1. \deg(\vartheta)\leq(n+1)(m)-1. |  |

Thus,

 | ( ψ, σ) ∗ ​ ( Ω n ​ e 1 ​ ( ℂ u ​ v 2) ≤ n) ⊂ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ ( n + 1) ​ ( m) − 1. (\psi,\sigma)_{*}\Big(\varOmega^{1}_{ne}(\mathbb{C}^{2}_{u\,v})_{\leq n}\Big)\subset\varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq(n+1)(m)-1}. |  |

Step 2. We now suppose that ℋ \mathcal{H} is of degree 𝔪 + 1 \mathfrak{m}+1 and that the polynomial 1-form ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}_{ne}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}. Of course, we have 2 ≤ 𝔪 + 1 ≤ m + 1 2\leq\mathfrak{m}+1\leq m+1 and 𝔫 ≤ ( n + 1) ​ ( m) − 1 \mathfrak{n}\leq(n+1)(m)-1.

From Lemmas 12 and 14, there exists a rectifying map for ℋ \mathcal{H}. Since ( p 1, p) = 1, (p_{1},p)=1, there are positive integers q 1 q_{1} and q q such that p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1. Moreover, by Remark 4, if we take 𝒢 ⁡ ( x, y) = x q 1 ​ ( x l ​ y + P ⁡ ( x)) q \mathcal{G}(x,y)=x^{q_{1}}\left(x^{l}y+P(x)\right)^{q}, then ( 38) becomes

 | ℂ x ​ y 2 \ { ℋ = 0 } → ℛ ℂ t ​ 𝔠 2 \ { t 𝔠 = 0 } ⟶ ℛ − 1 ℂ x ​ y 2 \ { ℋ = 0 } ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( t p 𝔠 q, 𝔠 q ​ k ​ ( 𝔠 q 1 − t p 1 ​ P ​ ( t p ​ 𝔠 − q)) t p 1 + p ​ k). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\{\mathcal{H}=0\}&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\{t\mathfrak{c}=0\}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\{\mathcal{H}=0\}\\ &&&&\\ (x,y)&\longmapsto&(\mathcal{G}(x,y),\mathcal{H}(x,y))&\longmapsto&\left(\dfrac{t^{p}}{\mathfrak{c}^{q}},\dfrac{\mathfrak{c}^{qk}\left(\mathfrak{c}^{q_{1}}-t^{p_{1}}P(t^{p}\mathfrak{c}^{-q})\right)}{\displaystyle t^{p_{1}+pk}}\right).\end{array} |  |

Since P ⁡ ( x) ∈ ℂ ​ [x] ≤ k − 1 P(x)\in\mathbb{C}[x]_{\leq k-1}, 𝔠 q ​ k ​ ( 𝔠 q 1 − t p 1 ​ P ​ ( t p ​ 𝔠 − q)) \mathfrak{c}^{qk}\left(\mathfrak{c}^{q_{1}}-t^{p_{1}}P(t^{p}\mathfrak{c}^{-q})\right) is a polynomial. Moreover, we have

 | ℛ ∗ ​ ( σ ′ ​ ψ ∗ ​ ( d ​ H + ε ​ ω)) = ℛ ∗ ​ ( d ​ ℋ + ε ​ ϑ) = d ​ 𝔠 + ε ​ η, η = ℛ ∗ ​ ( ϑ). \mathcal{R}_{*}\big(\sigma^{\prime}\psi_{*}(dH+\varepsilon\omega)\big)=\mathcal{R}_{*}\big(d\mathcal{H}+\varepsilon\vartheta\big)=d\mathfrak{c}+\varepsilon\eta,\ \ \ \eta=\mathcal{R}_{*}(\vartheta). |  |

For k > 0 k>0, the fiber ℒ 0 \mathcal{L}_{0} of ℋ \mathcal{H} is the disjoint union of the algebraic curves { x = 0 } \{x=0\} and { x k y + P ( x) = 0 } \{x^{k}y+P(x)=0\}, thus 0 0 is a critical value. If k = 0 k=0, then ( 0, 0) (0,0) is a critical point of ℋ \mathcal{H}, with critical value ℋ ⁡ ( 0, 0) = 0 \mathcal{H}(0,0)=0. Hence, in any case, 0 ∈ 𝔅 ⁡ ( ℋ) 0\in\mathfrak{B}(\mathcal{H}). Moreover, ℛ \mathcal{R} maps biholomorphically each fiber ℒ 𝔠 \mathcal{L}_{\mathfrak{c}} of ℋ \mathcal{H}, with 𝔠 ≠ 0 \mathfrak{c}\neq 0, into the horizontal line ℂ ∗ × { 𝔠 } \mathbb{C}^{*}\times\{\mathfrak{c}\} in ℂ t ​ 𝔠 2 \mathbb{C}^{2}_{t\,\mathfrak{c}}. Thus 𝔅 ⁡ ( ℋ) = { 0 } \mathfrak{B}(\mathcal{H})=\{0\} and

 | dim H 1 ​ ( L c, ℤ) = dim H 1 ​ ( ℒ 𝔠, ℤ) = dim H 1 ​ ( ℂ ∗ × { 𝔠 }, ℤ) = 1. \dim H_{1}(L_{c},\mathbb{Z})=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=\dim H_{1}(\mathbb{C}^{*}\times\{\mathfrak{c}\},\mathbb{Z})=1. |  |

In this case,

B ​ C ​ ( H) = { γ 𝟷 ​ ( c) } BC(H)=\{\gamma_{\tt 1}(c)\}, B ​ C ​ ( ℋ) = { δ 𝟷 ​ ( 𝔠) } BC(\mathcal{H})=\{\delta_{\tt 1}(\mathfrak{c})\} and B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c})\}.

Therefore, there exists only one Abelian integral I 1 ​ ( c) I_{1}(c) defined by ( H, ω) (H,\omega), which is algebraically equivalent to a unique Abelian integral ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) defined by ( ℋ, ϑ) (\mathcal{H},\vartheta). Moreover, ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) is rationally equivalent to a unique Abelian integral J 1 ​ ( 𝔠) J_{1}(\mathfrak{c}) defined by ( 𝔠, η) (\mathfrak{c},\eta).

Step 3. Let α 𝟷 ​ ( 𝔠) \alpha_{\tt 1}(\mathfrak{c}) be a small cycle around the puncture ( 0, 𝔠) (0,\mathfrak{c}) in the line ℂ ∗ × { 𝔠 } \mathbb{C}^{*}\times\{\mathfrak{c}\}. In this way, B ​ C ​ ( 𝔠) = { α 𝟷 ​ ( 𝔠) } BC(\mathfrak{c})=\{\alpha_{\tt 1}(\mathfrak{c})\} is a canonical global generators of d ​ 𝔠 = 0 d\mathfrak{c}=0 and we obtain

 | ℐ 1 ​ ( 𝔠) = J 𝟷 ​ ( 𝔠) = ∫ α 𝟷 ​ ( 𝔠) η. \mathcal{I}_{1}(\mathfrak{c})=J_{\tt 1}(\mathfrak{c})=\int_{\alpha_{\tt 1}(\mathfrak{c})}\eta. |  |

According to Corollary 5,

 | I 1 ​ ( c) = 1 σ ′ ​ ℐ 1 ​ ( 𝔠) = 1 σ ′ ​ J 1 ​ ( 𝔠), 𝔠 = σ ⁡ ( c), I_{1}(c)=\frac{1}{\sigma^{\prime}}\mathcal{I}_{1}(\mathfrak{c})=\frac{1}{\sigma^{\prime}}J_{1}(\mathfrak{c}),\quad\mathfrak{c}=\sigma(c), |  |

as in diagram ( 25).

Step 4. From Lemma 16, we know that for computing ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) it is sufficient to consider the basis B n ​ e 1 ( ℂ x ​ y 2, n) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},n)=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most n n. Then

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = ( t p 𝔠 q) i ​ ( 𝔠 q ​ k ​ ( 𝔠 q 1 − t p 1 ​ P ​ ( t p ​ 𝔠 − q)) t p 1 + p ​ k) j ​ [p ​ t p − 1 𝔠 q ​ d ​ t − q ​ t p 𝔠 q + 1 ​ d ​ 𝔠]. \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=\left(\frac{t^{p}}{\mathfrak{c}^{q}}\right)^{i}\left(\frac{\mathfrak{c}^{qk}\left(\mathfrak{c}^{q_{1}}-t^{p_{1}}P(t^{p}\mathfrak{c}^{-q})\right)}{t^{p_{1}+pk}}\right)^{j}\left[\frac{p\,t^{p-1}}{\mathfrak{c}^{q}}\,dt-\frac{q\,t^{p}}{\mathfrak{c}^{q+1}}\,d\mathfrak{c}\right]. |  |

Thus,

 | η i ​ j t = p ​ 𝔠 q ⁡ ( j ​ k − i − 1) ​ ( 𝔠 q 1 − t p 1 ​ P ​ ( t p ​ 𝔠 − q)) j t p ⁡ ( j ​ k − i − 1) + p 1 ​ j + 1 ​ d ​ t. \eta_{ij}^{t}=\frac{p\,\mathfrak{c}^{q(jk-i-1)}\left(\mathfrak{c}^{q_{1}}-t^{p_{1}}P(t^{p}\mathfrak{c}^{-q})\right)^{j}}{t^{p(jk-i-1)+p_{1}j+1}}\,dt. |  |

The binomial theorem implies

 | ( 𝔠 q 1 − t p 1 ​ P ​ ( t p ​ 𝔠 − q)) j = ∑ μ = 0 j ( j μ) ​ 𝔠 q 1 ​ ( j − μ) ​ t p 1 ​ μ ​ P ​ ( t p ​ 𝔠 − q) μ. \left(\mathfrak{c}^{q_{1}}-t^{p_{1}}P(t^{p}\mathfrak{c}^{-q})\right)^{j}=\sum_{\mu=0}^{j}{j\choose\mu}\mathfrak{c}^{q_{1}(j-\mu)}t^{p_{1}\mu}P\left(t^{p}\mathfrak{c}^{-q}\right)^{\mu}. |  |

We can assume that P ⁡ ( x) = λ 0 + ⋯ + λ s ​ x s P(x)=\lambda_{0}+\cdots+\lambda_{s}x^{s}, with s ≤ k − 1 s\leq k-1 and λ s ≠ 0 \lambda_{s}\not=0, then the multinomial theorem gives

 | P ( t p 𝔠 − q) μ = ∑ μ! n 0! ⋯ n s! λ 0 n 0 ⋯ λ s n s t p ​ N s 𝔠 − q ​ N s, P\left(t^{p}\mathfrak{c}^{-q}\right)^{\mu}=\sum\frac{\mu!}{n_{0}!\cdots n_{s}!}\lambda_{0}^{n_{0}}\cdots\lambda_{s}^{n_{s}}t^{pN_{s}}\mathfrak{c}^{-qN_{s}}, |  |

where the sum is over all lists of s + 1 s+1 non-negative integers ( n 0, …, n s) (n_{0},\ldots,n_{s}) such that

 | n 0 + ⋯ + n s = μ and N s = n 1 + ⋯ + s ​ n s. n_{0}+\cdots+n_{s}=\mu\quad\mbox{and}\quad N_{s}=n_{1}+\cdots+sn_{s}. |  | (81) |

Therefore, by simplifying we obtain

 | η i ​ j t = ∑ μ = 0 j ∑ A n 0 ⋯ n s μ p ​ 𝔠 q 1 ​ ( j − μ) − q ​ N ~ s t p 1 ​ ( j − μ) − p ​ N ~ s + 1 d t, \eta_{ij}^{t}=\sum_{\mu=0}^{j}\sum A_{n_{0}\cdots n_{s}}^{\mu}\frac{p\,\mathfrak{c}^{q_{1}(j-\mu)-q\widetilde{N}_{s}}}{t^{p_{1}(j-\mu)-p\widetilde{N}_{s}+1}}\,dt, |  | (82) |

where

 | A n 0 ​ … ​ n s μ = j! n 0! ⋯ n s! ( j − μ)! λ 0 n 0 ⋯ λ s n s and N ~ s = N s − j k + i + 1. A_{n_{0}...n_{s}}^{\mu}=\frac{j!}{n_{0}!\cdots n_{s}!(j-\mu)!}\lambda_{0}^{n_{0}}\cdots\lambda_{s}^{n_{s}}\quad\text{and}\quad\widetilde{N}_{s}=N_{s}-jk+i+1. |  | (83) |

The integral along α 𝟷 ​ ( 𝔠) \alpha_{\tt 1}(\mathfrak{c}) of each term in the sum on the right-hand side of ( 82) is different from zero if and only if p 1 ​ ( j − μ) = p ​ N ~ s p_{1}(j-\mu)=p\widetilde{N}_{s}. Since ( p 1, p) = 1 (p_{1},p)=1, there exists a positive integer q s ​ μ q_{s\mu} such that N ~ s = p 1 ​ q s ​ μ \widetilde{N}_{s}=p_{1}q_{s\mu} and j − μ = p ​ q s ​ μ. j-\mu=pq_{s\mu}. We have,

 | q s ​ μ ​ ( p 1 + p ⁡ ( k + 1)) = N ~ s + ( k + 1) ​ ( j − μ). q_{s\mu}(p_{1}+p(k+1))=\widetilde{N}_{s}+(k+1)(j-\mu). |  |

Moreover, N ~ s = N s − j ​ k + i + 1 ≤ ( k − 1) ​ μ − j ​ k + i + 1 \widetilde{N}_{s}=N_{s}-jk+i+1\leq(k-1)\mu-jk+i+1, it follows that

 | N ~ s + ( k + 1) ​ ( j − μ) ≤ i + j + 1 − 2 ​ μ. \widetilde{N}_{s}+(k+1)(j-\mu)\leq i+j+1-2\mu. |  |

Thus q s ​ μ ​ ( p 1 + p ⁡ ( k + 1)) ≤ i + j + 1 ≤ 𝔫 + 1 q_{s\mu}(p_{1}+p(k+1))\leq i+j+1\leq\mathfrak{n}+1, whence

 | q s ​ μ ≤ [𝔫 + 1 p 1 + p ⁡ ( k + 1)] = [𝔫 + 1 𝔪 + 1]. q_{s\mu}\leq\left[\frac{\mathfrak{n}+1}{p_{1}+p(k+1)}\right]=\left[\frac{\mathfrak{n}+1}{\mathfrak{m}+1}\right]. |  | (84) |

In addition, the degree of 𝔠 \mathfrak{c} is

 | q 1 ​ ( j − μ) − q ​ N ~ s = q 1 ​ ( p ​ q s ​ μ) − q ⁡ ( p 1 ​ q s ​ μ) = q s ​ μ. q_{1}(j-\mu)-q\widetilde{N}_{s}=q_{1}(pq_{s\mu})-q(p_{1}q_{s\mu})=q_{s\mu}. |  |

Hence, according to ( 61) and ( 84), the Abelian integral ℐ 1 ​ ( 𝔠) \mathcal{I}_{1}(\mathfrak{c}) is a polynomial of degree at most [( 𝔫 + 1) / ( 𝔪 + 1)] \left[(\mathfrak{n}+1)/(\mathfrak{m}+1)\right], because of ( 84). Therefore

 | Z ⁡ ( ℐ 1 ​ ( 𝔠)) = Z ⁡ ( J 1 ​ ( 𝔠)) ≤ [𝔫 + 1 𝔪 + 1]. Z(\mathcal{I}_{1}(\mathfrak{c}))=Z(J_{1}(\mathfrak{c}))\leq\left[\dfrac{\mathfrak{n}+1}{\mathfrak{m}+1}\right]. |  | (85) |

Since 2 ≤ 𝔪 + 1 ≤ m + 1 2\leq\mathfrak{m}+1\leq m+1 and 𝔫 ≤ ( n + 1) ​ ( m) − 1 \mathfrak{n}\leq(n+1)(m)-1,

 | Z ⁡ ( I 1 ​ ( c)) ≤ [( n + 1) ​ ( m) 2]. Z(I_{1}(c))\leq\left[\frac{(n+1)(m)}{2}\right]. |  |

In conclusion, we have proven the following result.

###### Theorem 23 ( [28]).

Let H ⁡ ( u, v) H(u,v) be a primitive polynomial of type ( 0, 2) (0,2) of degree m + 1 m+1 and let ω \omega be a polynomial 1-form of degree n n on ℂ 2 \mathbb{C}^{2}.

1. 1)

The Abelian integral I 1 ​ ( c) = ∫ γ 1 ​ ( c) ω: ℂ ⟶ ℂ \displaystyle I_{1}(c)=\int_{\gamma_{1}(c)}\omega\colon\mathbb{C}\longrightarrow\mathbb{C} is a polynomial.

2. 2)

Morever, I 1 ​ ( c) I_{1}(c) has at most [( n + 1) ​ m 2] \left[\frac{(n+1)\,m}{2}\right] isolated zeros in ℂ \ 𝔅 ⁡ ( H) \mathbb{C}\backslash\mathfrak{B}(H). □ \Box

## 6. Abelian integrals for the Neumann–Norbury classification

In this section, we provide general properties of Abelian integrals for the Neumann–Norbury algebraic classification, that is, for the normal forms of primitive polynomials with trivial global monodromy given in the families 𝔉 1 \mathfrak{F}_{1}, 𝔉 2 \mathfrak{F}_{2} and 𝔉 3 \mathfrak{F}_{3} of Theorem 10. In order to establish the result on this issue, we split the Neumann–Norbury families 𝔉 1 \mathfrak{F}_{1} and 𝔉 2 \mathfrak{F}_{2} into disjoint families:

 | 𝔉 ι + ≐ { ℋ ⁡ ( x, y) ∈ 𝔉 ι | p ​ q 1 − q ​ p 1 = 1 } a ​ n ​ d 𝔉 ι − ≐ { ℋ ⁡ ( x, y) ∈ 𝔉 ι | p ​ q 1 − q ​ p 1 = − 1 }, \mathfrak{F}_{\iota}^{+}\doteq\{\mathcal{H}(x,y)\in\mathfrak{F}_{\iota}\ |\ pq_{1}-qp_{1}=1\}\quad and\quad\mathfrak{F}_{\iota}^{-}\doteq\{\mathcal{H}(x,y)\in\mathfrak{F}_{\iota}\ |\ pq_{1}-qp_{1}=-1\}, |  |

where ι = 1, 2 \iota=1,2. For the sake of brevity, in all that follows

- •

B ​ C ​ ( ℋ) = { δ 𝚒 ​ ( 𝔠) } BC(\mathcal{H})=\{\delta_{\tt i}(\mathfrak{c})\} denotes the canonical global generators of the fundamental group for the generic fibers of d ​ ℋ = 0 d\mathcal{H}=0, as in equation ( 58), and

- •

ϑ \vartheta is a non-exact polynomial 1-form in Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \varOmega_{ne}^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, recall equation ( 52).

Our main result concerning the Abelian integrals for normal forms of polynomials with trivial global monodromy is the following.

###### Theorem 24.

Let ℋ ⁡ ( x, y) \mathcal{H}(x,y) be a polynomial of degree 𝔪 + 1 \mathfrak{m}+1 in the Neumann–Norbury families 𝔉 1, 𝔉 2 \mathfrak{F}_{1},\mathfrak{F}_{2} or 𝔉 3 \mathfrak{F}_{3}. If ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega_{ne}^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, then for each cycle δ 𝚒 ​ ( 𝔠) \delta_{\tt i}(\mathfrak{c}) the Abelian integral

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ: ℂ ⟶ ℂ \mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta\colon\mathbb{C}\longrightarrow\mathbb{C} |  |

is a polynomial, in addition:

1. 1)

If ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1}, then r + 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 3 r+1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 3 and

 | deg ( ℐ 𝚒 ( 𝔠)) ≤ { 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2 for ℋ ∈ 𝔉 1 + and 0 ≤ 𝚒 ≤ r − 1, ( 𝔫 − 1) ​ [𝔪 − r − 2 2] for ℋ ∈ 𝔉 1 + and 𝚒 = r, ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)] for ℋ ∈ 𝔉 1 − and 0 ≤ 𝚒 ≤ r − 1, 𝔫 ⁡ ( 𝔪 − 1 − r) − r for ℋ ∈ 𝔉 1 − and 𝚒 = r. \deg(\mathcal{I}_{\tt i}(\mathfrak{c}))\leq\begin{cases}\mathfrak{n}\left(\left[\dfrac{\mathfrak{m}-1}{r-1}\right]-2\right)-2&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{1}^{+}$ and $\,0\leq{\tt i}\leq r-1$,}\\[12.0pt] (\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-r-2}{2}\right]&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{1}^{+}$ and $\,{\tt i}=r$, }\\[12.0pt] (\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{1}^{-}$ and $\,0\leq{\tt i}\leq r-1$,}\\[12.0pt] \mathfrak{n}\left(\mathfrak{m}-1-r\right)-r&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{1}^{-}$ and $\,{\tt i}=r$.}\end{cases} |  | (86) |

2. 2)

If ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2}, then r = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 1 r=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 1 and

 | deg ( ℐ 𝚒 ( 𝔠)) ≤ { [𝔫 + 1 𝔪 + 1] for r = 1, 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2 for ℋ ∈ 𝔉 2 + and r > 1, ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)] for ℋ ∈ 𝔉 2 − and r > 1. \deg(\mathcal{I}_{\tt i}(\mathfrak{c}))\leq\begin{cases}\left[\dfrac{\mathfrak{n}+1}{\mathfrak{m}+1}\right]&\mbox{\; for $\,r=1$,}\\[12.0pt] \,\mathfrak{n}\left(\left[\dfrac{\mathfrak{m}-1}{r-1}\right]-2\right)-2&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{2}^{+}$ and $\,r>1$, }\\[12.0pt] \,(\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{2}^{-}$ and $\,r>1$.}\end{cases} |  | (87) |

3. 3)

If ℋ ∈ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{3}, then r − 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 0 r-1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 0 and

 | deg ⁡ ( ℐ 𝚒 ​ ( 𝔠)) ≤ { 0 for r = 1, [𝔫 + 1 𝔪 + 1] for r = 2, 𝔫 for r > 2. \deg(\mathcal{I}_{\tt i}(\mathfrak{c}))\leq\begin{cases}\,0&\mbox{\; for $\,r=1$},\\[6.0pt] \left[\dfrac{\mathfrak{n}+1}{\mathfrak{m}+1}\right]&\mbox{\; for $\,r=2$},\\[12.0pt] \,\mathfrak{n}&\mbox{\; for $\,r>2$}.\end{cases} |  | (88) |

Before we give a proof, let us recall diagram ( 25) in the Program, 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) \mathscr{N}_{BC(\mathcal{H})}(\vartheta) denoting the number of limit cycles of d ​ ℋ + ε ​ ϑ = 0 d\mathcal{H}+\varepsilon\vartheta=0 that are generated from cycles in B ​ C ​ ( ℋ) BC(\mathcal{H}), where ϑ \vartheta is non-conservative for B ​ C ​ ( ℋ) BC(\mathcal{H}).

###### Corollary 25.

Let ℋ ⁡ ( x, y) \mathcal{H}(x,y) be a polynomial of degree 𝔪 + 1 \mathfrak{m}+1 in the Neumann–Norbury families 𝔉 1, 𝔉 2 \mathfrak{F}_{1},\mathfrak{F}_{2} or 𝔉 3 \mathfrak{F}_{3} and let ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega_{ne}^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}} be non-conservative for B ​ C ​ ( ℋ) BC(\mathcal{H}). The following assertions hold.

1. 1)

If ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1}, then r + 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 3 r+1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 3 and

 | 𝒩 B ​ C ​ ( ℋ) ( ϑ) ≤ { r ⁡ ( 𝔫 ⁡ [𝔪 + 1 − 2 ​ r r − 1] − 2) + ( 𝔫 − 1) ​ [𝔪 − r − 2 2] for ℋ ∈ 𝔉 1 +, 𝔫 ⁡ ( 𝔪 − r − 1) + r ⁡ ( ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)] − 1) for ℋ ∈ 𝔉 1 −. \mathscr{N}_{BC(\mathcal{H})}(\vartheta)\leq\begin{cases}r\left(\mathfrak{n}\left[\dfrac{\mathfrak{m}+1-2r}{r-1}\right]-2\right)+(\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-r-2}{2}\right]&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{1}^{+}$},\\[12.0pt] \mathfrak{n}\left(\mathfrak{m}-r-1\right)+r\left((\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]-1\right)&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{1}^{-}$}.\end{cases} |  | (89) |

2. 2)

If ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2}, then r = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 1 r=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 1 and

 | 𝒩 B ​ C ​ ( ℋ) ( ϑ) ≤ { [𝔫 + 1 𝔪 + 1] for r = 1, r ⁡ ( 𝔫 ⁡ [𝔪 + 1 − 2 ​ r r − 1] − 2) for ℋ ∈ 𝔉 1 + and r > 1, r ​ ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)] for ℋ ∈ 𝔉 1 − and r > 1. \mathscr{N}_{BC(\mathcal{H})}(\vartheta)\leq\begin{cases}\left[\dfrac{\mathfrak{n}+1}{\mathfrak{m}+1}\right]&\mbox{\; for $\,r=1$,}\\[12.0pt] r\left(\mathfrak{n}\left[\dfrac{\mathfrak{m}+1-2r}{r-1}\right]-2\right)&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{1}^{+}$ and $\,r>1$,}\\[12.0pt] r(\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]&\mbox{\; for $\mathcal{H}\in\mathfrak{F}_{1}^{-}$ and $\,r>1$.}\end{cases} |  | (90) |

3. 3)

If ℋ ∈ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{3}, then r − 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 0 r-1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 0 and

 | 𝒩 B ​ C ​ ( ℋ) ( ϑ) ≤ { 0 for r = 1, [𝔫 + 1 𝔪 + 1] for r = 2, ( r − 1) ​ 𝔫, for r > 2. \mathscr{N}_{BC(\mathcal{H})}(\vartheta)\leq\begin{cases}0&\mbox{\; for $\,r=1$},\\[6.0pt] \left[\dfrac{\mathfrak{n}+1}{\mathfrak{m}+1}\right]&\mbox{\; for $\,r=2$},\\[12.0pt] (r-1)\mathfrak{n},&\mbox{\; for $\,r>2$}.\end{cases} |  | (91) |

###### Proof.

The computation of the number 𝒩 B ​ C ​ ( ℋ) ​ ( ϑ) \mathscr{N}_{BC(\mathcal{H})}(\vartheta) requires the addition over the number of global families of cycles { γ 𝚒 ​ ( c) } \{\gamma_{\tt i}(c)\}, 1 ≤ 𝚒 ≤ 𝔯 = dim H 1 ​ ( ℒ 𝔠, ℤ) 1\leq{\tt i}\leq\mathfrak{r}=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z}), in B ​ C ​ ( ℋ) BC(\mathcal{H}). Thus, equations ( 89), ( 90) and ( 91) follow from equations ( 86), ( 87) and ( 88), respectively. ∎

*Scheme for the proof of Theorem 24*: The upper bound in ( 88) for case r = 1 r=1, that is, dim H 1 ​ ( ℒ 𝔠, ℤ) = 0 \dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=0, follows from Remark 5. The upper bounds in ( 88) for r = 2 r=2 and in ( 87) for r = 1 r=1, that is, dim H 1 ​ ( ℒ 𝔠, ℤ) = 1 \dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})=1, follow from ( 85). Therefore, to complete the proof, it is sufficient to consider ℋ ∈ 𝔉 1 ∪ 𝔉 2 ∪ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{1}\cup\mathfrak{F}_{2}\cup\mathfrak{F}_{3} with dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 2 \dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 2. The rest of the proof follows from the next three propositions. More precisely, Proposition 26 will give the upper bound in ( 88) for r > 2 r>2. Proposition 27 will provide the upper bounds in ( 87) for r > 1 r>1, and finally Proposition 28 will give the the upper bounds in ( 86).

###### Proposition 26.

Let ℋ ⁡ ( x, y) \mathcal{H}(x,y) be a polynomial of degree 𝔪 + 1 \mathfrak{m}+1 in Neumann–Norbury family 𝔉 3 \mathfrak{F}_{3}, with r − 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 2 r-1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 2. If ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega_{ne}^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, then for each global section { δ 𝚒 ​ ( 𝔠) } \{\delta_{\tt i}(\mathfrak{c})\} the Abelian integral

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ: ℂ ⟶ ℂ \mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta\colon\mathbb{C}\longrightarrow\mathbb{C} |  |

is a polynomial of degree at most 𝔫 \mathfrak{n}. Moreover, this upper bound is reached.

###### Proof.

Consider ℋ ∈ 𝔉 3 \mathcal{H}\in\mathfrak{F}_{3} of degree 𝔪 + 1 \mathfrak{m}+1 and r − 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 2 r-1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 2, that is,

 | ℋ ⁡ ( x, y) = y ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x) a 𝚒 − h ⁡ ( x), \mathcal{H}(x,y)=y\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-x)^{a_{\tt i}}-h(x)\,, |  |

where r ≥ 3 r\geq 3, a 1, …, a r − 1 a_{1},\ldots,a_{r-1} are positive integers, β 1, …, β r − 1 \beta_{1},\ldots,\beta_{r-1} are distinct points in ℂ ∗ \mathbb{C}^{*}, and h ⁡ ( x) h(x) is a polynomial of degree at most 𝔪 = a 1 + ⋯ + a r − 1 \mathfrak{m}=a_{1}+\cdots+a_{r-1}.

Consider the rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} given in ( 42) and the basis B n ​ e 1 ( ℂ x ​ y 2, 𝔫) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most 𝔫 \mathfrak{n}. Then,

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = η i ​ j t = t i ​ ( 𝔠 + h ⁡ ( t)) j ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) j ​ a 𝚒 ​ d ​ t. \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=\eta_{ij}^{t}=\dfrac{t^{i}\left(\mathfrak{c}+h(t)\right)^{j}}{\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-t)^{ja_{\tt i}}}\,dt. |  |

Thus, η i ​ j t \eta_{ij}^{t} admits a representation at t = β 𝚒 t=\beta_{\tt i} of the form ( 63) as follows

 | η i ​ j t = R 1 ​ ( t, 𝔠) ( t − β 𝚒) j ​ a 𝚒 ​ d ​ t, where R 1 ​ ( t, 𝔠) = ( − 1) j ​ a 𝚒 ​ t i ​ ( 𝔠 + h ⁡ ( t)) j ∏ s = 1, s ≠ 𝚒 r − 1 ( β s − t) j ​ a s. \eta_{ij}^{t}=\dfrac{R_{1}(t,\mathfrak{c})}{(t-\beta_{\tt i})^{ja_{\tt i}}}\,dt,\qquad\mbox{where}\quad R_{1}(t,\mathfrak{c})=\frac{(-1)^{ja_{\tt i}}t^{i}\left(\mathfrak{c}+h(t)\right)^{j}}{\prod_{\begin{subarray}{c}s=1,s\neq\tt i\end{subarray}}^{r-1}(\beta_{s}-t)^{ja_{s}}}. |  |

We use the criterion given in ( 64) to obtain

 | ∫ α 𝚒 ​ ( 𝔠) η i ​ j t = 2 ​ π ​ − 1 ( j ​ a 𝚒 − 1)! ⋅ ∂ j ​ a 𝚒 − 1 ∂ t j ​ a 𝚒 − 1 ​ ( ( − 1) j ​ a 𝚒 ​ t i ​ ( 𝔠 + h ⁡ ( t)) j ∏ ν = 1, ν ≠ 𝚒 r − 1 ( β ν − t) j ​ a ν) | t = β 𝚒, \int_{\alpha_{\tt i}(\mathfrak{c})}\eta_{ij}^{t}=\frac{2\pi\sqrt{-1}}{(ja_{\tt i}-1)!}\cdot\frac{\partial^{ja_{\tt i}-1}}{\partial t^{ja_{\tt i}-1}}\left(\dfrac{(-1)^{ja_{\tt i}}t^{i}\left(\mathfrak{c}+h(t)\right)^{j}}{\prod_{\begin{subarray}{c}\nu=1,\nu\neq\tt i\end{subarray}}^{r-1}(\beta_{\nu}-t)^{ja_{\nu}}}\right)\Big|_{t=\beta_{\tt i}}, |  |

which is a polynomial in 𝔠 \mathfrak{c} of degree at most j j.

Hence, according to ( 61), the Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is a polynomial of degree at most 𝔫 \mathfrak{n}. This completes the proof of the first part of the proposition.

We now show that the upper bound is reached. For each integer 𝔪 ≥ 2, \mathfrak{m}\geq 2, the polynomial ℋ ⁡ ( x, y) = y ⁡ ( − 1 − x) ​ ( 1 − x) 𝔪 − 1 \mathcal{H}(x,y)=y(-1-x)(1-x)^{\mathfrak{m}-1} of degree 𝔪 + 1 \mathfrak{m}+1 belongs to family 𝔉 3 \mathfrak{F}_{3} and equation ( 42) becomes

 | ℂ x ​ y 2 \ { 1 − x 2 = 0 } → ℛ ℂ t ​ 𝔠 2 \ { 1 − t 2 = 0 } ⟶ ℛ − 1 ℂ x ​ y 2 \ { 1 − x 2 = 0 } ( x, y) ⟼ ( x, ℋ ⁡ ( x, y)) ⟼ ( t, ( − 1) 𝔪 ​ 𝔠 ( t + 1) ​ ( t − 1) 𝔪 − 1). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\{1-x^{2}=0\}&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\{1-t^{2}=0\}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\{1-x^{2}=0\}\\ &&&&\\ (x,y)&\longmapsto&(x,\mathcal{H}(x,y))&\longmapsto&\left(t,\dfrac{(-1)^{\mathfrak{m}}\mathfrak{c}}{(t+1)(t-1)^{\mathfrak{m}-1}}\right).\end{array} |  | (92) |

We consider the polynomial 1-form ϑ = ( 𝔞 1 ​ y + 𝔞 2 ​ y 2 + ⋯ + 𝔞 𝔫 ​ y 𝔫) ​ d ​ x \vartheta=(\mathfrak{a}_{1}y+\mathfrak{a}_{2}y^{2}+\cdots+\mathfrak{a}_{\mathfrak{n}}y^{\mathfrak{n}})\,dx of degree 𝔫 \mathfrak{n}. Thus,

 | η = ℛ ∗ ​ ( ϑ) = ∑ ν = 1 𝔫 𝔞 ν ​ ( ( − 1) ν ​ 𝔪 ​ 𝔠 ν ( t + 1) ν ​ ( t − 1) ν ⁡ ( 𝔪 − 1)) ​ d ​ t \eta=\mathcal{R}_{*}(\vartheta)=\sum_{\nu=1}^{\mathfrak{n}}\mathfrak{a}_{\nu}\left(\frac{(-1)^{\nu\mathfrak{m}}\,\mathfrak{c}^{\nu}}{(t+1)^{\nu}(t-1)^{\nu(\mathfrak{m}-1)}}\right)\,dt |  |

and

 | ∫ δ 𝚒 ​ ( 𝔠) ϑ = ∫ α 𝚒 ​ ( 𝔠) η = ∑ ν = 1 𝔫 𝔞 ν ​ ( ∫ α 𝚒 ​ ( 𝔠) ( − 1) ν ​ 𝔪 ​ d ​ t ( t + 1) ν ​ ( t − 1) ν ⁡ ( 𝔪 − 1)) ​ 𝔠 ν. \int_{\delta_{{\tt i}}(\mathfrak{c})}\vartheta=\int_{\alpha_{\tt i}(\mathfrak{c})}\eta=\sum_{\nu=1}^{\mathfrak{n}}\mathfrak{a}_{\nu}\left(\int_{\alpha_{\tt i}(\mathfrak{c})}\frac{(-1)^{\nu\mathfrak{m}}\,dt}{(t+1)^{\nu}(t-1)^{\nu(\mathfrak{m}-1)}}\right)\,\mathfrak{c}^{\nu}. |  |

By criterion ( 64), we have

 | ξ 1, ν ≐ ∫ α 𝟷 ​ ( 𝔠) ( − 1) ν ​ 𝔪 ​ d ​ t ( t + 1) ν ​ ( t − 1) ν ⁡ ( 𝔪 − 1) = 2 ​ π ​ − 1 ( ν − 1)! ​ ∂ ν − 1 ∂ t ν − 1 ​ ( ( − 1) ν ​ 𝔪 ( t − 1) ν ⁡ ( 𝔪 − 1)) | t = − 1 \xi_{1,\nu}\doteq\int_{\alpha_{\tt 1}(\mathfrak{c})}\frac{(-1)^{\nu\mathfrak{m}}\,dt}{(t+1)^{\nu}(t-1)^{\nu(\mathfrak{m}-1)}}=\frac{2\pi\sqrt{-1}}{(\nu-1)!}\frac{\partial^{\nu-1}}{\partial t^{\nu-1}}\left(\frac{(-1)^{\nu\mathfrak{m}}}{(t-1)^{\nu(\mathfrak{m}-1)}}\right)\Big|_{t=-1} |  |

and

 | ξ 2, ν ≐ ∫ α 𝟸 ​ ( 𝔠) ( − 1) ν ​ 𝔪 ​ d ​ t ( t + 1) ν ​ ( t − 1) ν ⁡ ( 𝔪 − 1) = 2 ​ π ​ − 1 ( ν ⁡ ( 𝔪 − 1) − 1)! ​ ∂ ν ⁡ ( 𝔪 − 1) − 1 ∂ t ν ⁡ ( 𝔪 − 1) − 1 ​ ( ( − 1) ν ​ 𝔪 ( t + 1) ν) | t = 1. \xi_{2,\nu}\doteq\int_{\alpha_{\tt 2}(\mathfrak{c})}\frac{(-1)^{\nu\mathfrak{m}}\,dt}{(t+1)^{\nu}(t-1)^{\nu(\mathfrak{m}-1)}}=\frac{2\pi\sqrt{-1}}{(\nu(\mathfrak{m}-1)-1)!}\frac{\partial^{\nu(\mathfrak{m}-1)-1}}{\partial t^{\nu(\mathfrak{m}-1)-1}}\left(\frac{(-1)^{\nu\mathfrak{m}}}{(t+1)^{\nu}}\right)\Big|_{t=1}. |  |

A straightforward computation gives

 | ξ 𝚒, ν = ( 2 ​ π ​ − 1) ​ ( − 1) ν + 1 − 𝚒 2 ν ​ 𝔪 − 1 ​ ( ν ​ 𝔪 − 2 ν ⁡ ( 𝔪 − 1) − 1) ≠ 0. \xi_{{\tt i},\nu}=\dfrac{\left(2\pi\sqrt{-1}\right)(-1)^{\nu+1-{\tt i}}}{2^{\nu\mathfrak{m}-1}}{{\nu\mathfrak{m}-2}\choose{\nu(\mathfrak{m}-1)-1}}\not=0. |  |

Therefore, for 𝚒 = 1, 2 {\tt i}=1,2, the Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is the polynomial of degree 𝔫 \mathfrak{n}

 | 𝔠 ⁡ ( 𝔞 1 ​ ξ 𝚒, 1 + 𝔞 2 ​ ξ 𝚒, 2 ​ 𝔠 + ⋯ + 𝔞 𝔫 ​ ξ 𝚒, 𝔫 ​ 𝔠 𝔫 − 1). \mathfrak{c}\left(\mathfrak{a}_{1}{\xi}_{{\tt i},1}+\mathfrak{a}_{2}{\xi}_{{\tt i},2}\mathfrak{c}+\cdots+\mathfrak{a}_{\mathfrak{n}}{\xi}_{{\tt i},\mathfrak{n}}\mathfrak{c}^{\mathfrak{n}-1}\right). |  |

Furthermore, we can find suitable values of 𝔞 1, 𝔞 2, …, 𝔞 𝔫 \mathfrak{a}_{1},\mathfrak{a}_{2},\ldots,\mathfrak{a}_{\mathfrak{n}} such that the respective integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) has zeros at 0, 𝔠 1, 𝔠 2, …, 𝔠 𝔫 − 1 ∈ ℂ. 0,\mathfrak{c}_{1},\mathfrak{c}_{2},\ldots,\mathfrak{c}_{\mathfrak{n}-1}\in\mathbb{C}. ∎

###### Remark 10.

There are polynomials in 𝔉 3 \mathfrak{F}_{3} of degree 𝔪 + 1 ≥ 3 \mathfrak{m}+1\geq 3, which do not reach the upper bound of the previous result. For instance, the polynomial ℋ ⁡ ( x, y) = y ​ ( 1 − x) 𝔪, \mathcal{H}(x,y)=y(1-x)^{\mathfrak{m}}, with 𝔪 ≥ 2 \mathfrak{m}\geq 2, belongs to the family 𝔉 3 \mathfrak{F}_{3} and is clearly algebraically equivalent to y ​ x 𝔪. yx^{\mathfrak{m}}. Thus, from [28, Theorem 2], we know that the Abelian integral defined by ℋ \mathcal{H} and a polynomial 1-form of degree 𝔫 \mathfrak{n} has at most [( 𝔫 + 1) / ( 𝔪 + 1)] [(\mathfrak{n}+1)/(\mathfrak{m}+1)] isolated zeros in ℂ \ 𝔅 ⁡ ( ℋ) \mathbb{C}\backslash\mathfrak{B}(\mathcal{H}).

###### Proposition 27.

Let ℋ ⁡ ( x, y) \mathcal{H}(x,y) be a polynomial of degree 𝔪 + 1 \mathfrak{m}+1 in Neumann–Norbury family 𝔉 2 \mathfrak{F}_{2}, with r = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 2 r=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 2. If ϑ ∈ Ω n ​ e 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega_{ne}^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, then for each global section { δ 𝚒 ​ ( 𝔠) } \{\delta_{\tt i}(\mathfrak{c})\} the Abelian integral

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ: ℂ ⟶ ℂ \mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta\colon\mathbb{C}\longrightarrow\mathbb{C} |  |

is a polynomial of degree at most

 | { 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2 for ℋ ∈ 𝔉 2 +, ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)] for ℋ ∈ 𝔉 2 −. \begin{cases}\mathfrak{n}\left(\left[\dfrac{\mathfrak{m}-1}{r-1}\right]-2\right)-2&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{2}^{+}$,}\\[12.0pt] (\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{2}^{-}$.}\end{cases} |  |

###### Proof.

Consider ℋ ∈ 𝔉 2 \mathcal{H}\in\mathfrak{F}_{2} of degree 𝔪 + 1 \mathfrak{m}+1, with r = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 2 r=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 2, that is,

 | ℋ ⁡ ( x, y) = x p 1 ​ 𝒮 ​ ( x, y) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x q 1 ​ 𝒮 ​ ( x, y) q) a 𝚒, \mathcal{H}(x,y)=x^{p_{1}}\mathcal{S}(x,y)^{p}\prod_{{\tt i}=1}^{r-1}\big(\beta_{\tt i}-x^{q_{1}}\mathcal{S}(x,y)^{q}\big)^{a_{\tt i}}, |  |

where 0 ≤ p 1 < p 0\leq p_{1}<p, 0 ≤ q 1 < q 0\leq q_{1}<q and p ​ q 1 − q ​ p 1 = ± 1 pq_{1}-qp_{1}=\pm 1, r ≥ 2 r\geq 2, a 1, …, a r − 1 a_{1},\ldots,a_{r-1} are positive integers, β 1, …, β r − 1 \beta_{1},\ldots,\beta_{r-1} are distinct points of ℂ ∗ \mathbb{C}^{*}, 𝒮 ⁡ ( x, y) = x k ​ y − P ⁡ ( x) \mathcal{S}(x,y)=x^{k}y-P(x), with k k a positive integer and P ⁡ ( x) ∈ ℂ ​ [x] ≤ k − 1 P(x)\in\mathbb{C}[x]_{\leq k-1}, and

 | 𝔪 + 1 = p 1 + p ⁡ ( k + 1) + ( q 1 + q ⁡ ( k + 1)) ​ ( a 1 + ⋯ + a r − 1). \mathfrak{m}+1=p_{1}+p(k+1)+(q_{1}+q(k+1))(a_{1}+\cdots+a_{r-1}). |  | (93) |

Case p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1. We use the rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} given in ( 43) and the basis B n ​ e 1 ( ℂ x ​ y 2, 𝔫) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most 𝔫 \mathfrak{n}. Then,

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = t p ​ i ​ Π ​ ( t) q ​ i 𝔠 q ​ i ​ 𝔠 j ​ q ​ S 1 ​ ( t, 𝔠) j t j ⁡ ( p ​ k + p 1) ​ Π ​ ( t) j ⁡ ( q ​ k + q 1) ​ d ​ ( t p ​ Π ​ ( t) q 𝔠 q). \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=\dfrac{t^{pi}\Pi(t)^{qi}}{\mathfrak{c}^{qi}}\,\dfrac{\mathfrak{c}^{jq}S_{1}(t,\mathfrak{c})^{j}}{t^{j(pk+p_{1})}\Pi(t)^{j(qk+q_{1})}}\,d\left(\dfrac{t^{p}\Pi(t)^{q}}{\mathfrak{c}^{q}}\right). |  |

Thus,

 | η i ​ j t = 𝔠 q ⁡ ( j − i − 1) S 1 ( t, 𝔠) j ( q t Π ′ ( t) + p Π ( t)) t j ⁡ ( p ​ k + p 1) − p ⁡ ( i + 1) + 1 ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) ( j ⁡ ( q ​ k + q 1) − q ⁡ ( i + 1) + 1) ​ a 𝚒 ​ d ​ t. \eta_{ij}^{t}=\dfrac{\mathfrak{c}^{q(j-i-1)}S_{1}(t,\mathfrak{c})^{j}\big(qt\Pi^{{}^{\prime}}(t)+p\Pi(t)\big)}{t^{j(pk+p_{1})-p(i+1)+1}\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-t)^{(j(qk+q_{1})-q(i+1)+1)a_{\tt i}}}\,dt. |  |

Recall that Π ⁡ ( t) \Pi(t) and S 1 ​ ( t, 𝔠) S_{1}(t,\mathfrak{c}) are given in ( 44) and ( 45). The binomial theorem then yields

 | S 1 ​ ( t, 𝔠) j = 𝔠 j ​ q ​ ( k − 1) ​ ∑ μ = 0 j ( j μ) ​ 𝔠 q 1 ​ ( j − μ) ​ t p 1 ​ μ ​ Π ​ ( t) q 1 ​ μ ​ P ​ ( t p ​ Π ​ ( t) q ​ 𝔠 − q) μ. S_{1}(t,\mathfrak{c})^{j}=\mathfrak{c}^{jq(k-1)}\sum_{\mu=0}^{j}{j\choose\mu}\mathfrak{c}^{q_{1}(j-\mu)}t^{p_{1}\mu}\Pi(t)^{q_{1}\mu}P\left(t^{p}\Pi(t)^{q}\mathfrak{c}^{-q}\right)^{\mu}. |  |

Following the same idea as in subsection 5.5, we get

 | P ( t p Π ( t) q 𝔠 − q) μ = ∑ μ! n 0! ⋯ n s! λ 0 n 0 ⋯ λ s n s t p ​ N s Π ( t) q ​ N s 𝔠 − q ​ N s, P\left(t^{p}\Pi(t)^{q}\mathfrak{c}^{-q}\right)^{\mu}=\sum\frac{\mu!}{n_{0}!\cdots n_{s}!}\lambda_{0}^{n_{0}}\cdots\lambda_{s}^{n_{s}}t^{pN_{s}}\Pi(t)^{qN_{s}}\mathfrak{c}^{-qN_{s}}, |  |

where the sum is over all lists of s + 1 s+1 non-negative integers ( n 0, …, n s) (n_{0},\ldots,n_{s}) that satisfy ( 81). Therefore, by using the two previous equalities and simplifying, we obtain

 | η i ​ j t = ∑ μ = 0 j ∑ A n 0 ⋯ n s μ 𝔠 q 1 ​ ( j − μ) − q ​ N ~ s ( q t Π ′ ( t) + p Π ( t)) t p 1 ​ ( j − μ) − p ​ N ~ s + 1 ​ Π ​ ( t) q 1 ​ ( j − μ) − q ​ N ~ s + 1 d t, \eta_{ij}^{t}=\sum_{\mu=0}^{j}\sum A_{n_{0}\cdots n_{s}}^{\mu}\frac{\mathfrak{c}^{q_{1}(j-\mu)-q\widetilde{N}_{s}}\big(qt\Pi^{{}^{\prime}}(t)+p\Pi(t)\big)}{t^{p_{1}(j-\mu)-p\widetilde{N}_{s}+1}\Pi(t)^{q_{1}(j-\mu)-q\widetilde{N}_{s}+1}}\,dt, |  | (94) |

where A n 0 ​ … ​ n s μ A_{n_{0}...n_{s}}^{\mu} and N ~ s \widetilde{N}_{s} are the same as in ( 83).

We will now prove that if q 1 ​ ( j − μ) − q ​ N ~ s < 0 q_{1}(j-\mu)-q\widetilde{N}_{s}<0, then the integral along α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) of the corresponding term in the sum on the right-hand side of ( 94) vanishes identically, which implies, according to ( 61) and the criterion given in ( 64), that the Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is a polynomial of degree at most

 | q 1 ​ ( j − μ) − q ​ N ~ s = j ⁡ ( q ​ k + q 1) − q 1 ​ μ − q ⁡ ( N s + i + 1) ≤ j ⁡ ( q ​ k + q 1) − q ≤ 𝔫 ⁡ ( q ​ k + q 1) − q. q_{1}(j-\mu)-q\widetilde{N}_{s}=j(qk+q_{1})-q_{1}\mu-q(N_{s}+i+1)\leq j(qk+q_{1})-q\leq\mathfrak{n}(qk+q_{1})-q. |  | (95) |

Indeed, if q 1 ​ ( j − μ) − q ​ N ~ s < 0 q_{1}(j-\mu)-q\widetilde{N}_{s}<0 and p ​ N ~ s − p 1 ​ ( j − μ) ≤ 0 p\widetilde{N}_{s}-p_{1}(j-\mu)\leq 0, then by using that p > 0 p>0 and q > 0 q>0, we get

 | p ​ q 1 ​ ( j − μ) − p ​ q ​ N ~ s < 0 and p ​ q ​ N ~ s − q ​ p 1 ​ ( j − μ) ≤ 0, pq_{1}(j-\mu)-pq\widetilde{N}_{s}<0\quad\mbox{and}\quad pq\widetilde{N}_{s}-qp_{1}(j-\mu)\leq 0, |  |

whence ( p ​ q 1 − q ​ p 1) ​ ( j − μ) < 0 (pq_{1}-qp_{1})(j-\mu)<0, which is a contradiction because p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1 and j − μ ≥ 0 j-\mu\geq 0. Hence, if q 1 ​ ( j − μ) − q ​ N ~ s < 0 q_{1}(j-\mu)-q\widetilde{N}_{s}<0, then p ​ N ~ s − p 1 ​ ( j − μ) > 0 p\widetilde{N}_{s}-p_{1}(j-\mu)>0. This implies that

 | p 1 ​ ( j − μ) − p ​ N ~ s + 1 ≤ 0 and q 1 ​ ( j − μ) − q ​ N ~ s + 1 ≤ 0. p_{1}(j-\mu)-p\widetilde{N}_{s}+1\leq 0\quad\mbox{and}\quad q_{1}(j-\mu)-q\widetilde{N}_{s}+1\leq 0. |  |

Hence, the 1-form in the sum on the right-hand side of ( 94) does not have any pole. This proves our assertion.

From ( 93) it follows that q ​ k + q 1 ≤ [( 𝔪 − 1) / ( r − 1)] − q qk+q_{1}\leq\left[(\mathfrak{m}-1)/(r-1)\right]-q. Thus, according to ( 95), the degree of ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is at most

 | 𝔫 ⁡ ( [𝔪 − 1 r − 1] − q) − q ≤ 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2. \mathfrak{n}\left(\left[\frac{\mathfrak{m}-1}{r-1}\right]-q\right)-q\leq\mathfrak{n}\left(\left[\frac{\mathfrak{m}-1}{r-1}\right]-2\right)-2. |  |

Case p ​ q 1 − q ​ p 1 = − 1 pq_{1}-qp_{1}=-1. The rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} and its inverse are

 | ℂ x ​ y 2 \ Σ ⁡ ( ℋ) → ℛ ℂ t ​ 𝔠 2 \ 𝔇 2 ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℋ) ( x, y) ⟼ ( G ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( 𝔠 q t p ​ Π ​ ( t) q, t p ​ Π ​ ( t) q ​ S 1 − ​ ( t, 𝔠) 𝔠 q ​ k + q 1). \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{H})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\mathfrak{D}_{2}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{H})\\ &&&&\\ (x,y)&\longmapsto&\big(G(x,y),\mathcal{H}(x,y)\big)&\longmapsto&\left(\dfrac{\mathfrak{c}^{q}}{t^{p}\Pi(t)^{q}},\dfrac{t^{p}\Pi(t)^{q}S_{1}^{-}(t,\mathfrak{c})}{\mathfrak{c}^{qk+q_{1}}}\right).\end{array} |  | (96) |

where 𝒢 ⁡ ( x, y) \mathcal{G}(x,y), ℋ ⁡ ( x, y) \mathcal{H}(x,y) and Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) are according to Tables 1 and 2, 𝔇 2 = { 𝔠 t Π ( t) = 0 }, \mathfrak{D}_{2}=\{\mathfrak{c}\,t\,\Pi(t)=0\}, Π ⁡ ( t) \Pi(t) as in ( 44) and

 | S 1 − ​ ( t, 𝔠) = t p ⁡ ( k − 1) ​ Π ​ ( t) q ⁡ ( k − 1) ​ ( t p 1 ​ Π ​ ( t) q 1 + 𝔠 q 1 ​ P ​ ( 𝔠 q ​ t − p ​ Π ​ ( t) − q)), S_{1}^{-}(t,\mathfrak{c})=t^{p(k-1)}\Pi(t)^{q(k-1)}\Big(t^{p_{1}}\Pi(t)^{q_{1}}+\mathfrak{c}^{q_{1}}P\left(\mathfrak{c}^{q}t^{-p}\Pi(t)^{-q}\right)\Big), |  |

which is polynomial because P P has degree at most k − 1 k-1.

Consider the basis B n ​ e 1 ( ℂ x ​ y 2, 𝔫) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most 𝔫 \mathfrak{n}. As a result,

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = 𝔠 q ​ i t p ​ i ​ Π ​ ( t) q ​ i ​ t j ​ p ​ Π ​ ( t) j ​ q ​ S 1 − ​ ( t, 𝔠) j 𝔠 j ⁡ ( q ​ k + q 1) ​ d ​ ( 𝔠 q t p ​ Π ​ ( t) q). \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=\dfrac{\mathfrak{c}^{qi}}{t^{pi}\Pi(t)^{qi}}\,\dfrac{t^{jp}\Pi(t)^{jq}S_{1}^{-}(t,\mathfrak{c})^{j}}{\mathfrak{c}^{j(qk+q_{1})}}\,d\left(\dfrac{\mathfrak{c}^{q}}{t^{p}\Pi(t)^{q}}\right). |  |

Thus,

 | η i ​ j t = − 𝔠 q ⁡ ( i − j ​ k + 1) − j ​ q 1 S 1 − ( t, 𝔠) j ( q t Π ′ ( t) + p Π ( t)) t p ⁡ ( i − j + 1) + 1 ​ Π ​ ( t) q ⁡ ( i − j + 1) + 1 ​ d ​ t. \eta_{ij}^{t}=-\dfrac{\mathfrak{c}^{q(i-jk+1)-jq_{1}}S_{1}^{-}(t,\mathfrak{c})^{j}\big(qt\Pi^{{}^{\prime}}(t)+p\Pi(t)\big)}{t^{p(i-j+1)+1}\Pi(t)^{q(i-j+1)+1}}\,dt. |  |

Analogously to the previous case, after applying the binomial theorem to S 1 − ​ ( t, 𝔠) j S_{1}^{-}(t,\mathfrak{c})^{j} and the multinomial theorem to P ​ ( 𝔠 q ​ t − p ​ Π ​ ( t) − q) μ P\left(\mathfrak{c}^{q}t^{-p}\Pi(t)^{-q}\right)^{\mu}, we obtain

 | η i ​ j t = − ∑ μ = 0 j ∑ A n 0 ⋯ n s μ 𝔠 q ​ N ~ s − q 1 ​ ( j − μ) ( q t Π ′ ( t) + p Π ( t)) t p ​ N ~ s + 1 − p 1 ​ ( j − μ) ​ Π ​ ( t) q ​ N ~ s + 1 − q 1 ​ ( j − μ) d t, \eta_{ij}^{t}=-\sum_{\mu=0}^{j}\sum A_{n_{0}\cdots n_{s}}^{\mu}\frac{\mathfrak{c}^{q\widetilde{N}_{s}-q_{1}(j-\mu)}\big(qt\Pi^{{}^{\prime}}(t)+p\Pi(t)\big)}{t^{p\widetilde{N}_{s}+1-p_{1}(j-\mu)}\Pi(t)^{q\widetilde{N}_{s}+1-q_{1}(j-\mu)}}\,dt, |  |

where A n 0 ​ … ​ n s μ A_{n_{0}...n_{s}}^{\mu} and N ~ s \widetilde{N}_{s} are the same as in ( 83). We can prove that if q ​ N ~ s − q 1 ​ ( j − μ) < 0 q\widetilde{N}_{s}-q_{1}(j-\mu)<0, then the integral along α 𝚒 ​ ( 𝔠) \alpha_{\tt i}(\mathfrak{c}) of the corresponding term in the sum on the right-hand side of previous equation vanishes identically, which implies, according to ( 61) and ( 64), that the Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is a polynomial of degree at most

 | q ​ N ~ s − q 1 ​ ( j − μ) ≤ q ⁡ ( N s − j ​ k + i + 1) ≤ q ⁡ ( ( k − 1) ​ j − j ​ k + i + 1) ≤ q ⁡ ( 𝔫 − 1). q\widetilde{N}_{s}-q_{1}(j-\mu)\leq q(N_{s}-jk+i+1)\leq q((k-1)j-jk+i+1)\leq q(\mathfrak{n}-1). |  | (97) |

Since from ( 93) it follows that q ≤ [( 𝔪 − 4) / ( 2 ​ ( r − 1))] q\leq\left[(\mathfrak{m}-4)/(2(r-1))\right], we obtain that the degree of ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is at most

 | ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)]. (\mathfrak{n}-1)\left[\frac{\mathfrak{m}-4}{2(r-1)}\right]. |  |

We are done. ∎

###### Proposition 28.

Let ℋ ⁡ ( x, y) \mathcal{H}(x,y) be a polynomial of degree 𝔪 + 1 \mathfrak{m}+1 in Neumann–Norbury family 𝔉 1 \mathfrak{F}_{1}, with r + 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 3 r+1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 3. If ϑ ∈ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, then for each global section { δ 𝚒 ​ ( 𝔠) } \{\delta_{\tt i}(\mathfrak{c})\} the Abelian integral

 | ℐ 𝚒 ​ ( 𝔠) = ∫ δ 𝚒 ​ ( 𝔠) ϑ: ℂ ⟶ ℂ \mathcal{I}_{\tt i}(\mathfrak{c})=\int_{\delta_{\tt i}(\mathfrak{c})}\vartheta\colon\mathbb{C}\longrightarrow\mathbb{C} |  |

is a polynomial of degree at most

 | { 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2 for ℋ ∈ 𝔉 1 + and 0 ≤ 𝚒 ≤ r − 1, ( 𝔫 − 1) ​ [𝔪 − r − 2 2] for ℋ ∈ 𝔉 1 + and 𝚒 = r, ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)] for ℋ ∈ 𝔉 1 − and 0 ≤ 𝚒 ≤ r − 1, 𝔫 ⁡ ( 𝔪 − 1 − r) − r for ℋ ∈ 𝔉 1 − and 𝚒 = r. \begin{cases}\mathfrak{n}\left(\left[\dfrac{\mathfrak{m}-1}{r-1}\right]-2\right)-2&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{1}^{+}$ and $\,0\leq{\tt i}\leq r-1$,}\\[12.0pt] (\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-r-2}{2}\right]&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{1}^{+}$ and $\,{\tt i}=r$,}\\[12.0pt] (\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{1}^{-}$ and $\,0\leq{\tt i}\leq r-1$,}\\[12.0pt] \mathfrak{n}\left(\mathfrak{m}-1-r\right)-r&\mbox{\; for $\,\mathcal{H}\in\mathfrak{F}_{1}^{-}$ and $\,{\tt i}=r$.}\end{cases} |  |

###### Proof.

Consider ℋ ∈ 𝔉 1 \mathcal{H}\in\mathfrak{F}_{1} of degree 𝔪 + 1 \mathfrak{m}+1, with r + 1 = dim H 1 ​ ( ℒ 𝔠, ℤ) ≥ 3 r+1=\dim H_{1}(\mathcal{L}_{\mathfrak{c}},\mathbb{Z})\geq 3, that is,

 | H ⁡ ( x, y) = x q 1 ​ 𝒮 ​ ( x, y) q + x p 1 ​ 𝒮 ​ ( x, y) p ​ ∏ 𝚒 = 1 r − 1 ( β 𝚒 − x q 1 ​ 𝒮 ​ ( x, y) q) a 𝚒 H(x,y)=x^{q_{1}}\mathcal{S}(x,y)^{q}+x^{p_{1}}\mathcal{S}(x,y)^{p}\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-x^{q_{1}}\mathcal{S}(x,y)^{q})^{a_{\tt i}} |  |

where; 0 ≤ p 1 < p 0\leq p_{1}<p, 0 ≤ q 1 < q 0\leq q_{1}<q and p ​ q 1 − q ​ p 1 = ± 1 pq_{1}-qp_{1}=\pm 1; r ≥ 2 r\geq 2, a 1, …, a r − 1 a_{1},\ldots,a_{r-1} are positive integers; β 1, …, β r − 1 \beta_{1},\ldots,\beta_{r-1} are distinct points of ℂ ∗ \mathbb{C}^{*}; 𝒮 ⁡ ( x, y) = x k ​ y − P ⁡ ( x) \mathcal{S}(x,y)=x^{k}y-P(x), with k k a positive integer, P ⁡ ( x) ∈ ℂ ​ [x] ≤ k − 1 P(x)\in\mathbb{C}[x]_{\leq k-1}; and 𝔪 + 1 = p 1 + p ⁡ ( k + 1) + ( q 1 + q ⁡ ( k + 1)) ​ ( a 1 + ⋯ + a r − 1) \mathfrak{m}+1=p_{1}+p(k+1)+(q_{1}+q(k+1))(a_{1}+\cdots+a_{r-1}).

Case p ​ q 1 − q ​ p 1 = 1 pq_{1}-qp_{1}=1. We can use the rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} given in ( 46) and the basis B n ​ e 1 ( ℂ x ​ y 2, 𝔫) = { ϑ i ​ j = x i y j d x } B_{ne}^{1}(\mathbb{C}^{2}_{x\,y},\mathfrak{n})=\{\vartheta_{ij}=x^{i}y^{j}dx\} of non-exact 1-forms of degree at most 𝔫 \mathfrak{n}. Then,

 | η i ​ j = ℛ ∗ ​ ( ϑ i ​ j) = t p ​ i ​ Π ​ ( t) q ​ i ( c − t) q ​ i ​ ( c − t) j ​ q ​ S 2 ​ ( t, c) j t j ⁡ ( p ​ k + p 1) ​ Π ​ ( t) j ⁡ ( q ​ k + q 1) ​ d ​ ( t p ​ Π ​ ( t) q ( c − t) q). \eta_{ij}=\mathcal{R}_{*}(\vartheta_{ij})=\dfrac{t^{pi}\Pi(t)^{qi}}{(c-t)^{qi}}\,\dfrac{(c-t)^{jq}S_{2}(t,c)^{j}}{t^{j(pk+p_{1})}\Pi(t)^{j(qk+q_{1})}}\,d\left(\dfrac{t^{p}\Pi(t)^{q}}{(c-t)^{q}}\right). |  |

Thus,

 | η i ​ j t = S 2 ( t, c) j ( q t Π ( t) + ( c − t) ( q t Π ′ ( t) + p Π ( t))) t j ⁡ ( p ​ k + p 1) − p ⁡ ( i + 1) + 1 ​ Π ​ ( t) j ⁡ ( q ​ k + q 1) − q ⁡ ( i + 1) + 1 ​ ( c − t) q ⁡ ( i − j + 1) + 1 ​ d ​ t. \eta_{ij}^{t}=\dfrac{S_{2}(t,c)^{j}\big(qt\Pi(t)+(c-t)(qt\Pi^{{}^{\prime}}(t)+p\Pi(t))\big)}{t^{j(pk+p_{1})-p(i+1)+1}\Pi(t)^{j(qk+q_{1})-q(i+1)+1}(c-t)^{q(i-j+1)+1}}\,dt. |  |

Recall that S 2 ​ ( t, 𝔠) S_{2}(t,\mathfrak{c}) is given in ( 47). Therefore, by following the same idea as in subsection 5.5 and the same steps as in the proof of Proposition 27, we obtain

 | η i ​ j t = ∑ μ = 0 j ∑ A n 0 ⋯ n s μ ( 𝔠 − t) q 1 ​ ( j − μ) − q ​ N ~ s − 1 ( q t Π ( t) + ( c − t) ( q t Π ′ ( t) + p Π ( t))) t p 1 ​ ( j − μ) − p ​ N ~ s + 1 ​ Π ​ ( t) q 1 ​ ( j − μ) − q ​ N ~ s + 1 d t, \eta_{ij}^{t}=\sum_{\mu=0}^{j}\sum A_{n_{0}\cdots n_{s}}^{\mu}\frac{(\mathfrak{c}-t)^{q_{1}(j-\mu)-q\widetilde{N}_{s}-1}\big(qt\Pi(t)+(c-t)(qt\Pi^{{}^{\prime}}(t)+p\Pi(t))\big)}{t^{p_{1}(j-\mu)-p\widetilde{N}_{s}+1}\Pi(t)^{q_{1}(j-\mu)-q\widetilde{N}_{s}+1}}\,dt, |  |

where the second sum is over all lists of s + 1 s+1 non-negative integers ( n 0, …, n s) (n_{0},\ldots,n_{s}) that satisfy ( 81), and A n 0 ​ … ​ n s μ A_{n_{0}...n_{s}}^{\mu}, N ~ s \widetilde{N}_{s} are the same as in ( 83). Hence, η i ​ j t \eta_{ij}^{t} could have poles at t = β 𝚒 t=\beta_{\tt i}, with 𝚒 = 0, 1, …, r {\tt i}=0,1,\ldots,r.

As in the proof of Proposition 27, if q 1 ​ ( j − μ) − q ​ N ~ s < 0 q_{1}(j-\mu)-q\widetilde{N}_{s}<0, then η i ​ j t \eta_{ij}^{t} does not have poles at t = β 𝚒 t=\beta_{\tt i}, for 𝚒 = 0, 1, …, r − 1 {\tt i}=0,1,\ldots,r-1 because

 | p 1 ​ ( j − μ) − p ​ N ~ s + 1 ≤ 0 and q 1 ​ ( j − μ) − q ​ N ~ s + 1 ≤ 0. p_{1}(j-\mu)-p\widetilde{N}_{s}+1\leq 0\quad\mbox{and}\quad q_{1}(j-\mu)-q\widetilde{N}_{s}+1\leq 0. |  |

Hence, according to ( 61) and the criterion given in ( 64), that for 𝚒 = 0, 1, …, r − 1 {\tt i}=0,1,\ldots,r-1 each Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is a polynomial of degree at most

 | q 1 ​ ( j − μ) − q ⁡ ( N s − j ​ k + i + 1) ≤ j ⁡ ( q ​ k + q 1) − q ≤ 𝔫 ⁡ ( q ​ k + q 1) − q. q_{1}(j-\mu)-q(N_{s}-jk+i+1)\leq j(qk+q_{1})-q\leq\mathfrak{n}(qk+q_{1})-q. |  | (98) |

In the remaining case 𝚒 = r {\tt i}=r, each term in the sum on the right-hand side of the previous equation for η i ​ j t \eta_{ij}^{t} admits the following representation at t = 𝔠 t=\mathfrak{c},

 | η i ​ j t ​ ( μ, n 0, …, n s) ≐ ( − 1) q ​ N ~ s − q 1 ​ ( j − μ) ​ R ​ ( t, 𝔠) ( t − 𝔠) q ​ N ~ s − q 1 ​ ( j − μ) + 1 ​ d ​ t, \eta_{ij}^{t}(\mu,n_{0},\ldots,n_{s})\doteq\dfrac{(-1)^{q\widetilde{N}_{s}-q_{1}(j-\mu)}\,R(t,\mathfrak{c})}{(t-\mathfrak{c})^{q\widetilde{N}_{s}-q_{1}(j-\mu)+1}}\,dt, |  |

where R ( t, 𝔠) = t p ​ N ~ s − p 1 ​ ( j − μ) − 1 Π ( t) q ​ N ~ s − q 1 ​ ( j − μ) − 1 ( q t Π ( t) + ( 𝔠 − t) ( q t Π ′ ( t) + p Π ( t))) R(t,\mathfrak{c})=t^{p\widetilde{N}_{s}-p_{1}(j-\mu)-1}\Pi(t)^{q\widetilde{N}_{s}-q_{1}(j-\mu)-1}\big(qt\Pi(t)+(\mathfrak{c}-t)(qt\Pi^{{}^{\prime}}(t)+p\Pi(t))\big).

Hence, if q ​ N ~ s − q 1 ​ ( j − μ) + 1 ≤ 0 q\widetilde{N}_{s}-q_{1}(j-\mu)+1\leq 0, then t = 𝔠 t=\mathfrak{c} is not a pole of η i ​ j t ​ ( μ, n 0, …, n s) \eta_{ij}^{t}(\mu,n_{0},\ldots,n_{s}), whence the integral ∫ α r ​ ( 𝔠) η i ​ j t ​ ( μ, n 0, …, n s) \int_{\alpha_{r}(\mathfrak{c})}\eta_{ij}^{t}(\mu,n_{0},\ldots,n_{s}) vanishes identically. If q ​ N ~ s − q 1 ​ ( j − μ) + 1 ≥ 1 q\widetilde{N}_{s}-q_{1}(j-\mu)+1\geq 1, then R ⁡ ( t, 𝔠) R(t,\mathfrak{c}) is a polynomial. Thus, according to the criterion given in ( 64), we have

 | ∫ α r ​ ( 𝔠) η i ​ j t ​ ( μ, n 0, …, n s) = ( 2 ​ π ​ − 1) ( q ​ N ~ s − q 1 ​ ( j − μ))! ⋅ ∂ q ​ N ~ s − q 1 ​ ( j − μ) ∂ t q ​ N ~ s − q 1 ​ ( j − μ) ​ ( R ⁡ ( t, 𝔠)) | t = 𝔠, \int_{\alpha_{r}(\mathfrak{c})}\eta_{ij}^{t}(\mu,n_{0},\ldots,n_{s})=\frac{\left(2\pi\sqrt{-1}\right)}{(q\widetilde{N}_{s}-q_{1}(j-\mu))!}\cdot\frac{\partial^{q\widetilde{N}_{s}-q_{1}(j-\mu)}}{\partial t^{q\widetilde{N}_{s}-q_{1}(j-\mu)}}\left(R(t,\mathfrak{c})\right)\Big|_{t=\mathfrak{c}}, |  |

which is a polynomial function in 𝔠 \mathfrak{c}. Moreover, by recalling from equation ( 44) that Π ⁡ ( t) = ∏ 𝚒 = 1 r − 1 ( β 𝚒 − t) a 𝚒 \Pi(t)=\prod_{{\tt i}=1}^{r-1}(\beta_{\tt i}-t)^{a_{\tt i}}, then the degree of t t in R ⁡ ( t, 𝔠) R(t,\mathfrak{c}) is at most

 | p ​ N ~ s − p 1 ​ ( j − μ) + ( q ​ N ~ s − q 1 ​ ( j − μ)) ​ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒). p\widetilde{N}_{s}-p_{1}(j-\mu)+\left(q\widetilde{N}_{s}-q_{1}(j-\mu)\right)\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}\Big). |  |

Thus, the maximum degree of t t in the previous derivative of R ⁡ ( t, 𝔠) R(t,\mathfrak{c}) is

 | p ​ N ~ s − p 1 ​ ( j − μ) + ( q ​ N ~ s − q 1 ​ ( j − μ)) ​ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1), p\widetilde{N}_{s}-p_{1}(j-\mu)+\left(q\widetilde{N}_{s}-q_{1}(j-\mu)\right)\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big), |  |

which is then the maximum degree of 𝔠 \mathfrak{c} in ∫ α r ​ ( 𝔠) η i ​ j t ​ ( μ, n 0, …, n s) \int_{\alpha_{r}(\mathfrak{c})}\eta_{ij}^{t}(\mu,n_{0},\ldots,n_{s}).

The previous expression can be written as

 | ( p + q ⁡ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1)) ​ N ~ s − ( j − μ) ​ ( p 1 + q 1 ​ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1)). \bigg(p+q\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big)\bigg)\widetilde{N}_{s}-(j-\mu)\bigg(p_{1}+q_{1}\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big)\bigg). |  |

Thus, it is bounded from above by

 | ( p + q ⁡ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1)) ​ N ~ s, \bigg(p+q\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big)\bigg)\widetilde{N}_{s}, |  |

which, following ( 97), is bounded by

 | ( p + q ⁡ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1)) ​ ( i − j + 1) + 1 ≤ ( 𝔫 − 1) ​ ( p + q ⁡ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1)). \bigg(p+q\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big)\bigg)(i-j+1)+1\leq(\mathfrak{n}-1)\bigg(p+q\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big)\bigg). |  |

The degree of ℋ \mathcal{H} is the same as in ( 93), from which we obtain

 | q ​ k + q 1 ≤ [𝔪 − 1 r − 1] − q and p + q ⁡ ( ∑ 𝚒 = 𝟷 r − 1 a 𝚒 − 1) ≤ [𝔪 − r − 2 2]. qk+q_{1}\leq\left[\frac{\mathfrak{m}-1}{r-1}\right]-q\quad\mbox{and}\quad p+q\Big(\sum_{\tt i=1}^{r-1}a_{\tt i}-1\Big)\leq\left[\frac{\mathfrak{m}-r-2}{2}\right]. |  |

Therefore, according to ( 98), for each 𝚒 = 0, …, r − 1 {\tt i}=0,\ldots,r-1 the Abelian integral ℐ 𝚒 ​ ( 𝔠) \mathcal{I}_{\tt i}(\mathfrak{c}) is a polynomial of degree at most

 | 𝔫 ⁡ ( q ​ k + q 1) − q ≤ 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2 \mathfrak{n}(qk+q_{1})-q\leq\mathfrak{n}\left(\left[\frac{\mathfrak{m}-1}{r-1}\right]-2\right)-2 |  |

and the Abelian integral ℐ r ​ ( 𝔠) \mathcal{I}_{r}(\mathfrak{c}) is a polynomial of degree at most

 | ( 𝔫 − 1) ​ [𝔪 − r − 2 2]. (\mathfrak{n}-1)\left[\frac{\mathfrak{m}-r-2}{2}\right]. |  |

Case p ​ q 1 − q ​ p 1 = − 1 pq_{1}-qp_{1}=-1. The rectifying map ℛ \mathcal{R} for ℋ \mathcal{H} and its inverse are

 | ℂ x ​ y 2 \ Σ ⁡ ( ℋ) → ℛ ℂ t ​ 𝔠 2 \ 𝔇 2 ⟶ ℛ − 1 ℂ x ​ y 2 \ Σ ⁡ ( ℋ) ( x, y) ⟼ ( 𝒢 ⁡ ( x, y), ℋ ⁡ ( x, y)) ⟼ ( ( 𝔠 − t) q t p ​ Π ​ ( t) q, t p ​ Π ​ ( t) q ​ S 2 − ​ ( t, 𝔠) ( 𝔠 − t) k ​ q + q 1), \begin{array}[]{rcccl}\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{H})&\xrightarrow{\ \mathcal{R}\ }&\mathbb{C}_{t\,\mathfrak{c}}^{2}\backslash\mathfrak{D}_{2}&\stackrel{{\scriptstyle\mathcal{R}^{-1}}}{{\longrightarrow}}&\mathbb{C}_{x\,y}^{2}\backslash\Sigma(\mathcal{H})\\ &&&&\\ (x,y)&\longmapsto&\big(\mathcal{G}(x,y),\mathcal{H}(x,y)\big)&\longmapsto&\left(\dfrac{(\mathfrak{c}-t)^{q}}{t^{p}\Pi(t)^{q}},\dfrac{t^{p}\Pi(t)^{q}S_{2}^{-}(t,\mathfrak{c})}{(\mathfrak{c}-t)^{kq+q_{1}}}\right),\end{array} |  | (99) |

where 𝒢 ⁡ ( x, y) \mathcal{G}(x,y), ℋ ⁡ ( x, y) \mathcal{H}(x,y) and Σ ⁡ ( ℛ) \Sigma(\mathcal{R}) agree with Tables 1 and 2,

 | 𝔇 2 = { ( 𝔠 − t) t Π ( t) = 0 }, \mathfrak{D}_{2}=\{(\mathfrak{c}-t)\,t\,\Pi(t)=0\}, |  |

and

 | S 2 − ​ ( t, 𝔠) = ( t p ​ Π ​ ( t) q) k − 1 ​ ( t p 1 ​ Π ​ ( t) q 1 + ( 𝔠 − t) q 1 ​ P ​ ( ( 𝔠 − t) q t p ​ Π ​ ( t) q)) S_{2}^{-}(t,\mathfrak{c})=\left(t^{p}\Pi(t)^{q}\right)^{k-1}\left(t^{p_{1}}\Pi(t)^{q_{1}}+(\mathfrak{c}-t)^{q_{1}}P\bigg(\dfrac{(\mathfrak{c}-t)^{q}}{t^{p}\Pi(t)^{q}}\bigg)\right) |  |

which is polynomial because P P has degree at most k − 1 k-1. The rest of the proof is analogous to the previous case. ∎

## 7. Proof of Theorems 1 and 2

###### Proof of Theorem 1.

The result follows in a rather straightforward way from Proposition 13, which deals with the relationship between the degrees of the original pair ( H, ω) (H,\omega) and the degree of the transformed ( ℋ, ϑ) (\mathcal{H},\vartheta), and Theorem 24, concerning the maximal number of zeros of Abelian integrals defined by ( ℋ, ϑ) (\mathcal{H},\vartheta), with ℋ \mathcal{H} in the Neumann–Norbury families.

We consider H ∈ ℂ ​ [u, v] ≤ m + 1 H\in\mathbb{C}[u,v]_{\leq m+1} and ω ∈ Ω 1 ​ ( ℂ u ​ v 2) ≤ n \omega\in\varOmega^{1}(\mathbb{C}_{u\,v}^{2})_{\leq n}, where H H is a primitive polynomial with trivial global monodromy and 𝔯 = dim H 1 ​ ( L c, ℤ) ≥ 1. \mathfrak{r}=\dim H_{1}(L_{c},\mathbb{Z})\geq 1.

Let γ ⁡ ( c 0) \gamma(c_{0}) be a complex cycle of d ​ H = 0 dH=0 in the generic leaf L c 0 L_{c_{0}}. By Lemma 18, γ ⁡ ( c 0) \gamma(c_{0}) uniquely extends to global family of complex cycles { γ ⁡ ( c) | c ∈ ℂ \ 𝔅 ⁡ ( H) } \{\gamma(c)\,|\,c\in\mathbb{C}\backslash\mathfrak{B}(H)\}. Hence, the Abelian integral I ( c) = ∫ γ ⁡ ( c) I(c)=\int_{\gamma(c)} is a univalued holomorphic function on ℂ \ 𝔅 ( H) } \mathbb{C}\backslash\mathfrak{B}(H)\}. Since I ⁡ ( c) I(c) depends only on the homology class of γ ⁡ ( c) \gamma(c), it is enough to consider the canonical set of cycles { γ 1 ​ ( c 0), …, γ 𝔯 ​ ( c 0) } \{\gamma_{1}(c_{0}),\ldots,\gamma_{\mathfrak{r}}(c_{0})\} of H 1 ​ ( L c 0, ℤ) H_{1}(L_{c_{0}},\mathbb{Z}) and prove the theorem for the Abelian integrals I 𝚒 ​ ( c) I_{\tt i}(c) induced by the canonical global generators

B C ( H) = { γ 𝚒 ( c) | 1 ≤ 𝚒 ≤ 𝔯, c ∈ ℂ \ 𝔅 ( H) } BC(H)=\{\gamma_{\tt i}(c)\,|\,\ 1\leq{\tt i}\leq\mathfrak{r},\,c\in\mathbb{C}\backslash\mathfrak{B}(H)\} of d ​ H = 0 dH=0;

because I ⁡ ( c) I(c) is an integer linear combination of the integrals I 𝚒 ​ ( c) I_{\tt i}(c), 1 ≤ 𝚒 ≤ 𝔯 1\leq{\tt i}\leq\mathfrak{r}.

The first two steps of our Program are guaranteed by Theorem 10, Proposition 13 and Lemma 14. Hence, let ℋ ⁡ ( x, y) \mathcal{H}(x,y) be a normal form of H ⁡ ( u, v) H(u,v), through the pair ( ψ, σ) ∈ Aut ⁡ ( ℂ 2) × Aut ⁡ ( ℂ) (\psi,\sigma)\in\mathop{\mbox{Aut}}\nolimits(\mathbb{C}^{2})\times\mathop{\mbox{Aut}}\nolimits(\mathbb{C}), and let ϑ \vartheta be the 1-form as in ( 14), that is, ϑ = σ ′ ​ ψ ∗ ​ ( ω) \vartheta=\sigma^{\prime}\psi_{*}(\omega). Since ℋ \mathcal{H} belongs to one of the Neumann–Norbury families 𝔉 1 \mathfrak{F}_{1}, 𝔉 2 \mathfrak{F}_{2} or 𝔉 3 \mathfrak{F}_{3}, the assertion OPEN 1) 1) of Theorem 1 follows directly from Corollary 5, first part of Theorem 24, and previous paragraph.

Regarding the assertion OPEN 2) 2) of Theorem 1, we will consider the following cases.

Case 1. If ℋ ⁡ ( x, y) ∈ 𝔉 3 \mathcal{H}(x,y)\in\mathfrak{F}_{3} with r = 2 r=2 or ℋ ⁡ ( x, y) ∈ 𝔉 2 \mathcal{H}(x,y)\in\mathfrak{F}_{2} with r = 1 r=1, then ℋ \mathcal{H} and H H are of type ( 0, 2) (0,2). Hence, from Theorem 23, we obtain the upper bound given in assertion 2) for m = 1 m=1.

Case 2. If ℋ ⁡ ( x, y) ∈ 𝔉 3 \mathcal{H}(x,y)\in\mathfrak{F}_{3} with r > 2 r>2, then r − 1 = 𝔯 = dim H 1 ​ ( ℒ c, ℤ) = dim H 1 ​ ( L c, ℤ) ≥ 2 r-1=\mathfrak{r}=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\dim H_{1}(L_{c},\mathbb{Z})\geq 2 and 𝔪 + 1 = deg ⁡ ( ℋ) ≥ 3 \mathfrak{m}+1=\deg(\mathcal{H})\geq 3. Hence, from Corollary 5, Theorem 24.3) and Proposition 13.3), we obtain that each Abelian integral I 𝚒 ​ ( c) I_{\tt i}(c), 1 ≤ 𝚒 ≤ dim H 1 ​ ( L c, ℤ) 1\leq{\tt i}\leq\dim H_{1}(L_{c},\mathbb{Z}), satisfies

 | deg ⁡ ( I 𝚒 ​ ( c)) = deg ⁡ ( ℐ 𝚒 ​ ( σ ⁡ ( c))) = deg ⁡ ( ℐ 𝚒 ​ ( 𝔠)) ≤ ( n + 1) ​ ( m + 1 − 𝔯) − 1. \deg(I_{\tt i}(c))=\deg(\mathcal{I}_{\tt i}(\sigma(c)))=\deg(\mathcal{I}_{\tt i}(\mathfrak{c}))\leq(n+1)(m+1-\mathfrak{r})-1. |  |

Case 3. If ℋ ⁡ ( x, y) ∈ 𝔉 2 \mathcal{H}(x,y)\in\mathfrak{F}_{2} with r ≥ 2 r\geq 2, then r = 𝔯 = dim H 1 ​ ( ℒ c, ℤ) = dim H 1 ​ ( L c, ℤ) ≥ 2 r=\mathfrak{r}=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\dim H_{1}(L_{c},\mathbb{Z})\geq 2 and 𝔪 + 1 = deg ⁡ ( ℋ) ≥ 7 \mathfrak{m}+1=\deg(\mathcal{H})\geq 7. In addition, we have that r ≤ [𝔪 / 2] − 1 r\leq[\mathfrak{m}/2]-1, which follows from equation ( 93). A simple but cumbersome computation shows that for 𝔪 ≥ 6 \mathfrak{m}\geq 6, and 𝔫 ≥ 1 \mathfrak{n}\geq 1, we have

 | 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2 ≥ ( 𝔫 − 1) ​ [𝔪 − 4 2 ​ ( r − 1)]. \mathfrak{n}\left(\left[\frac{\mathfrak{m}-1}{r-1}\right]-2\right)-2\geq(\mathfrak{n}-1)\left[\dfrac{\mathfrak{m}-4}{2(r-1)}\right]. |  |

Thus, if ϑ ∈ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, then from Theorem 24.2) we conclude that

 | deg ⁡ ( ℐ 𝚒 ​ ( 𝔠)) ≤ 𝔫 ⁡ ( [𝔪 − 1 r − 1] − 2) − 2. \deg(\mathcal{I}_{\tt i}(\mathfrak{c}))\leq\mathfrak{n}\left(\left[\dfrac{\mathfrak{m}-1}{r-1}\right]-2\right)-2. |  |

Therefore, this inequality, Corollary 5 and Proposition 13.2) imply

 | deg ⁡ ( I 𝚒 ​ ( c)) ≤ ( ( n + 1) ​ [m − 𝔯 − 1 𝔯 + 1] − 1) ​ ( [m − 1 𝔯 − 1] − 2) − 2. \deg(I_{\tt i}(c))\leq\left((n+1)\left[\dfrac{m-\mathfrak{r}-1}{\mathfrak{r}+1}\right]-1\right)\left(\left[\dfrac{m-1}{\mathfrak{r}-1}\right]-2\right)-2. |  |

Case 4. If ℋ ⁡ ( x, y) ∈ 𝔉 1 \mathcal{H}(x,y)\in\mathfrak{F}_{1}, then r + 1 = 𝔯 = dim H 1 ​ ( ℒ c, ℤ) = dim H 1 ​ ( L c, ℤ) ≥ 3 r+1=\mathfrak{r}=\dim H_{1}(\mathcal{L}_{c},\mathbb{Z})=\dim H_{1}(L_{c},\mathbb{Z})\geq 3, 𝔪 + 1 = deg ⁡ ( ℋ) ≥ 7 \mathfrak{m}+1=\deg(\mathcal{H})\geq 7, and as in the previous case r ≤ [𝔪 / 2] − 1 r\leq[\mathfrak{m}/2]-1. Again, simple but cumbersome computations show that in this case and for 𝔫 ≥ 1 \mathfrak{n}\geq 1, the number 𝔫 ⁡ ( 𝔪 − 1 − r) − r \mathfrak{n}\left(\mathfrak{m}-1-r\right)-r is the biggest of the four upper bounds given in Theorem 24.1). Thus, if ϑ ∈ Ω 1 ​ ( ℂ x ​ y 2) ≤ 𝔫 \vartheta\in\varOmega^{1}(\mathbb{C}^{2}_{x\,y})_{\leq\mathfrak{n}}, then from Theorem 24.1) we conclude that

 | deg ⁡ ( ℐ 𝚒 ​ ( 𝔠)) ≤ 𝔫 ⁡ ( 𝔪 − 1 − r) − r = 𝔫 ⁡ ( 𝔪 − 𝔯 − 2) − 𝔯 + 1. \deg(\mathcal{I}_{\tt i}(\mathfrak{c}))\leq\mathfrak{n}\left(\mathfrak{m}-1-r\right)-r=\mathfrak{n}\left(\mathfrak{m}-\mathfrak{r}-2\right)-\mathfrak{r}+1. |  |

Therefore, this inequality, Corollary 5 and Proposition 13.1) imply

 | deg ⁡ ( I 𝚒 ​ ( c)) ≤ ( ( n + 1) ​ [m − 𝔯 𝔯] − 1) ​ ( m − 𝔯 − 2) − 𝔯 + 1. \deg(I_{\tt i}(c))\leq\left((n+1)\left[\dfrac{m-\mathfrak{r}}{\mathfrak{r}}\right]-1\right)\left(m-\mathfrak{r}-2\right)-\mathfrak{r}+1. |  |

Simple computations show that for m = 6, 7, 8 m=6,7,8 the upper bound given in Case 2 is the biggest one of the last three cases, which yields the upper bound given in assertion 2) for 2 ≤ m ≤ 8 2\leq m\leq 8. Finally, by comparing the upper bounds given in Cases 2, 3 and 4, it is clear that for m ≥ 9 m\geq 9, the biggest bound is the provided in the last case, which gives the remainder upper bound of assertion 2). ∎

###### Proof of Theorem 2.

Statement 1) follows from second part of Theorem 1, whereas Proposition 21 implies statements 2) and 3). ∎

Acknowledgements. The authors would like to thank the Referee for his suggestions which have helped to improve the work.

## References

- [1] V. I. Arnold, Sur quelques problèmes de la théorie des systèmes dynamiques. [Some problems of the theory of dynamical systems] Topol. Methods Nonlinear Anal., 4 (1994), no. 2, 209-225. [https://projecteuclid.org/journals/topological-methods-in-nonlinear-analysis/volume-4/issue-2/Sur-quelques-probl%c3%a8mes-de-la-th%c3%a9orie-des-syst%c3%a8mes-dynamiques/tmna/1479287045.full][3]
- [2] V. I. Arnold, S. M. Gusein-Zade, A. N. Varchenko, Singularities of Differentiable Maps Vol. 2, Monodromy and asymptotics of integrals. Birkhauser/Springer, New York, (2012). [https://doi.org/10.1007/978-0-8176-8343-6][4]
- [3] E. Artal-Bartolo, P. Cassou-Noguès, A. Dimca, Sur la topologie des polynômes complexes. Singularities (Oberwolfach, 1996), Progr. Math., 162, Birkhäuser, Basel, (1998) 317-343. [https://link.springer.com/content/pdf/10.1007/978-3-0348-8770-0_16.pdf][5]
- [4] H. Bass, E. Connell, D. Wright, The Jacobian conjecture: reduction of degree and formal expansion of the inverse. Bull. Amer. Math. Soc. (N.S.) 7 no.2 (1982) 287-330. [https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-7/issue-2/The-Jacobian-conjecture--Reduction-of-degree-and-formal-expansion/bams/1183549636.full][6]
- [5] G. Binyamini, D. Novikov, S. Yakovenko, On the number of zeros of Abelian integrals, Invent. Math. 181 (2010), no. 2, 227-289. [https://doi.org/10.1007/s00222-010-0244-0][7]
- [6] S. A. Broughton, On the topology of polynomial hypersurfaces, Singularities, Part 1 (Arcata, Calif., 1981), Proc. Sympos. Pure Math., 40, Amer. Math. Soc., Providence, RI, (1983) 167-178.
- [7] S. Brusadin, G. Gorni, The degree of the inverse of a polynomial automorphism, Univ. lagel. Acta Math. no. 44 (2006) 15-19. [https://www.emis.de/journals/UIAM/PDF/44-15-19.pdf][8]
- [8] P. Cassou-Noguès, D. Daigle, Rational polynomials of simple type: a combinatorial proof, Algebraic varieties and automorphism groups, Adv. Stud. Pure Math., 75, Math. Soc. Japan, Tokyo, (2017) 7–28. [https://doi.org/10.2969/aspm/07510007][9]
- [9] C. Christopher, C. Li, J. Torregrosa, Limit Cycles of Differential Equations, Advanced Courses in Mathematics - CRM Barcelona. Birkhäuser Verlag, Basel. [https://doi.org/10.1007/978-3-030-59656-9][10]
- [10] A. Dimca, Monodromy at infinity for polynomials in two variables, J. Algebraic Geom., 7 (1998) 771–779.
- [11] A. H. Durfee, Five definitions of critical point at infinity. Singularities (Oberwolfach, 1996), Progr. Math. 162, Birkhäuser, Basel (1998), 345-360. [https://doi.org/10.1007/978-3-0348-8770-0_17][11]
- [12] J. Fernández de Bobadilla, Moduli Spaces of Polynomials of Two Variables, Memoirs AMS 817 (2005). [https://bookstore.ams.org/memo-173-817][12]
- [13] J. P. Françoise, Successive derivatives of a first return map, application to the study of quadratic vector fields, Ergodic Theory Dynam. Systems 16 (1996), no. 1, 87-96. [https://doi.org/10.1017/S0143385700008725][13]
- [14] L. Gavrilov, Abelian integrals related to Morse polynomials and perturbations of plane Hamiltonian vector fields, Ann. Inst. Fourier (Grenoble) 49 (1999), no. 2, 611-652. [http://www.numdam.org/article/AIF_1999__49_2_611_0.pdf][14]
- [15] H. Huy Vui, L. Dũng Tráng, Sur la topologie des polynômes complexes, Acta Math. Vietnam. 9 , N ∘ N^{\circ} 1, (1984) 21-32. [http://journals.math.ac.vn/acta/pdf/198401021.pdf][15]
- [16] I. D. Iliev, The number of limit cycles due to polynomial perturbations of the harmonic oscillator, Math. Proc. Cambridge Phil. Soc. 127 (1999) 317-322. [https://doi.org/10.1017/S0305004199003795][16]
- [17] Y. Ilyashenko, The origin of limit cycles under perturbation of the equation d w / d z = − R z / R w dw/dz=-R_{z}/R_{w}, where R ⁡ ( z, w) R(z,w) is a polynomial, Math. USSR Sbornik 7 (1969), no. 3, 353-202. [https://www.mathnet.ru/links/d98bc1a88cb5ebeed21be5c2aae975f5/sm3561_eng.pdf11][17]
- [18] Y. Ilyashenko, Centennial history of Hilbert’s 16th problem, Bulletin (New Series) of the American Mathematical Society 39 (2002), no. 3, 301-354. [https://doi.org/10.1090/S0273-0979-02-00946-1][18]
- [19] Y. Ilyashenko, S. Yakovenko, Lectures on Analytic Differential Equations, Graduate Studies in Mathematics, vol. 86, American Mathematical Society, Providence, RI, 2008. [https://bookstore.ams.org/gsm-86][19]
- [20] A. Jebrane, P. Mardesić, M. Pelletier, A note on a generalization of Françoise’s algorithm for calculating higher order Melnikov functions, Bull. Sci. Math. 128 (2004), no. 9, 749-760. [https://doi:10.1016/j.bulsci.2004.03.012][20]
- [21] I. A. Khovanskaya (Pushkar’), The weakened infinitesimal Hilbert 16th problem, (Russian) Tr. Mat. Inst. Steklova 254 (2006), Nelineĭn. Anal. Differ. Uravn., 215–246 ISBN: 5-02-034087-1; translation in Proc. Steklov Inst. Math. (2006) no. 3(254), 201-230. [https://doi.org/10.1134/S0081543806030102][21]
- [22] A. G. Khovanskiĭ, Real analytic manifolds with the property of finiteness, and complex abelian integrals, (Russian) Funktsional. Anal. i Prilozhen. 18 (1984) no. 2, 40-50. [https://doi.org/10.1007/BF01077822][22]
- [23] M. Miyanishi, T. Sugie, Generically rational polynomials, Osaka J. Math. 17 (1980), no. 2, 339-362. [https://projecteuclid.org/journals/osaka-journal-of-mathematics/volume-17/issue-2/Generically-rational-polynomials/ojm/1200773130.full][23]
- [24] W. D. Neumann, P. Norbury, Monodromy and vanishing cycles of complex polynomials, Duke Math. J. 101 (2000), 487-497. [https://doi.org/10.1215/S0012-7094-00-10134-2][24]
- [25] W. D. Neumann, P. Norbury, Rational polynomials of simple type, Pacific J. Math. 204 (2002) no. 1, 177-207. [https://msp.org/pjm/2002/204-1/pjm-v204-n1-p10-s.pdf][25]
- [26] D. Novikov, S. Yakovenko, Simple exponential estimate for the number of real zeros of complete Abelian integrals, Ann. Inst. Fourier (Grenoble) 45 (1995), no. 4, 897-927. [http://eudml.org/doc/75150][26]
- [27] S. Rebollo-Perdomo, The infinitesimal Hilbert’s 16th problem in the real and complex planes, Qual. Theory Dyn. Syst. 7 (2009), 467–500.
- [28] S. Rebollo-Perdomo, Complete Abelian integrals for polynomials whose generic fiber is biholomorphic to ℂ ∗ \mathbb{C}^{*}, J. Math. Anal. Appl. 394 (2012), 562-570. [https://doi.org/10.1016/j.jmaa.2012.05.014][27]
- [29] S. Rebollo-Perdomo, Medium amplitude limit cycles of some classes of generalized Liénard systems, Internat. J. Bifur. Chaos Appl. Sci. Engrg. 25 (2015) no. 10, 1550128, 8. [https://doi.org/10.1142/S021812741550128X][28]
- [30] S. Rebollo-Perdomo, V. Salas-Mendoza, Medium amplitude limit cycles in second order perturbed polynomial Liénard systems, J. Math. Anal. Appl. 473 (2019) no. 1, 609-621. [https://doi.org/10.1016/j.jmaa.2018.12.079][29]
- [31] R. Thom, Ensembles et morphismes stratifiés, Bull. Amer. Math. Soc. 75 (1969) 240-284. [https://projecteuclid.org/download/pdf_1/euclid.bams/1183530285][30]
- [32] A. N. Varchenko, Estimation of the number of zeros of an Abelian integral depending on a parameter and limit cycles, (Russian) Funktsional. Anal. Prolozhen 18 (1984) no. 2, 14-25. [https://doi.org/10.1007/BF01077820][31]
- [33] P. G. Wightwick, Equivalence of polynomials under automorphisms of ℂ 2 \mathbb{C}^{2}, Journal of Pure and Applied Algebra 157 (2001) 341-367. [https://doi.org/10.1016/S0022-4049(00)00014-1][32]


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://projecteuclid.org/journals/topological-methods-in-nonlinear-analysis/volume-4/issue-2/Sur-quelques-probl%c3%a8mes-de-la-th%c3%a9orie-des-syst%c3%a8mes-dynamiques/tmna/1479287045.full
[4]: https://doi.org/10.1007/978-0-8176-8343-6
[5]: https://link.springer.com/content/pdf/10.1007/978-3-0348-8770-0_16.pdf
[6]: https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-7/issue-2/The-Jacobian-conjecture--Reduction-of-degree-and-formal-expansion/bams/1183549636.full
[7]: https://doi.org/10.1007/s00222-010-0244-0
[8]: https://www.emis.de/journals/UIAM/PDF/44-15-19.pdf
[9]: https://doi.org/10.2969/aspm/07510007
[10]: https://doi.org/10.1007/978-3-030-59656-9
[11]: https://doi.org/10.1007/978-3-0348-8770-0_17
[12]: https://bookstore.ams.org/memo-173-817
[13]: https://doi.org/10.1017/S0143385700008725
[14]: http://www.numdam.org/article/AIF_1999__49_2_611_0.pdf
[15]: http://journals.math.ac.vn/acta/pdf/198401021.pdf
[16]: https://doi.org/10.1017/S0305004199003795
[17]: https://www.mathnet.ru/links/d98bc1a88cb5ebeed21be5c2aae975f5/sm3561_eng.pdf11
[18]: https://doi.org/10.1090/S0273-0979-02-00946-1
[19]: https://bookstore.ams.org/gsm-86
[20]: https://doi:10.1016/j.bulsci.2004.03.012
[21]: https://doi.org/10.1134/S0081543806030102
[22]: https://doi.org/10.1007/BF01077822
[23]: https://projecteuclid.org/journals/osaka-journal-of-mathematics/volume-17/issue-2/Generically-rational-polynomials/ojm/1200773130.full
[24]: https://doi.org/10.1215/S0012-7094-00-10134-2
[25]: https://msp.org/pjm/2002/204-1/pjm-v204-n1-p10-s.pdf
[26]: http://eudml.org/doc/75150
[27]: https://doi.org/10.1016/j.jmaa.2012.05.014
[28]: https://doi.org/10.1142/S021812741550128X
[29]: https://doi.org/10.1016/j.jmaa.2018.12.079
[30]: https://projecteuclid.org/download/pdf_1/euclid.bams/1183530285
[31]: https://doi.org/10.1007/BF01077820
[32]: https://doi.org/10.1016/S0022-4049(00)00014-1
