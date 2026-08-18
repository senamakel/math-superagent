<!-- source: https://ar5iv.labs.arxiv.org/html/2510.02770 | converted from HTML -->

[2510.02770] On entry-exit formulas for degenerate turning point problems in planar slow-fast systems

# On entry-exit formulas for degenerate turning point problems in planar slow-fast systems

R. Huzak Address: Hasselt University, Campus Diepenbeek, Agoralaan Gebouw D, 3590 Diepenbeek, Belgium and K. Uldall Kristiansen Address: Department of Applied Mathematics and Computer Science, Technical University of Denmark, 2800 Kgs. Lyngby, Denmark

###### Abstract.

In this paper, we study degenerate entry-exit problems associated with planar slow-fast systems having an invariant line { ( x, y): y = 0 } \{(x,y)\,:\,y=0\} with a turning point at x = 0 x=0. The degeneracy stems from the fact that the slow flow has a saddle-node of even order 2 ​ n 2n, n ∈ ℕ n\in\mathbb{N}, at the turning point, i.e. x ′ = − x 2 ​ n ​ ( 1 + o ⁡ ( 1)) x^{\prime}=-x^{2n}(1+o(1)) for ϵ = 0 \epsilon=0. We are motivated by the appearance of such turning point problems (for n = 1 n=1) in the graphics ( I 2 1) (I_{2}^{1}) and ( I 4 1) (I_{4}^{1}), through a nilpotent saddle-node singularity at infinity, in the Dumortier-Roussarie-Rousseau program (for solving the finiteness part of Hilbert’s 16th problem for quadratic polynomial systems). Our results show, under additional hypothesis, that in the case n = 1 n=1 there is a well-defined entry-exit relation for ϵ → 0 \epsilon\to 0. The associated Dulac map is smooth w.r.t. ( ϵ, ϵ ​ log ⁡ ϵ − 1) (\epsilon,\epsilon\log\epsilon^{-1}). On the other hand for the cases n ≥ 2 n\geq 2, we show that the entry-exit relation requires additional control parameters. Our approach follows the one used by De Maesschalck, P. and Schecter, S. (JDE 2016) for a different type of degenerate entry-exit problem. In particular, we apply blow-up after having first performed a singular coordinate transformation of y y. The degeneracy at x = 0 x=0 requires an additional blow-up. We finally apply the result for n = 1 n=1 to a normal form for the unfolding of the relevant graphics in the Dumortier-Roussarie-Rousseau program. Here we also demonstrate that the singular transformation of y y due to De Maesschalck, P. and Schecter, S. (JDE 2016) has practical significance in numerical computations.

keywords. Entry-exit, GSPT, blowup, the Dumortier-Roussarie-Rousseau program, Hilbert’s 16th problem.

## 1. Introduction

Consider a planar slow-fast system

(1.1) |  | x ˙ \displaystyle\dot{x} | = ϵ ​ f ​ ( x, y, ϵ), \displaystyle=\epsilon f(x,y,\epsilon), |  |

 | y ˙ \displaystyle\dot{y} | = y ​ h ​ ( x, y, ϵ), \displaystyle=yh(x,y,\epsilon), |  |

where ϵ ≥ 0 \epsilon\geq 0 is a singular perturbation parameter kept small and f f and h h are ( C ∞ C^{\infty} -)smooth functions. We suppose the following:

(1.2) |  | x ​ h ​ ( x, 0, 0) < 0 ∀ x ∈ I \ { 0 }, \displaystyle xh(x,0,0)<0\quad\forall\,x\in I\backslash\{0\}, |  |

where I ⊂ ℝ I\subset\mathbb{R} is a compact interval. Then x = 0 x=0 is a turning point where the stability of the invariant line { y = 0 } \{y=0\} changes from normally attracting for x > 0 x>0 to normally repelling for x < 0 x<0.

If f ⁡ ( x, 0, 0) < 0 f(x,0,0)<0 for all x ∈ I x\in I, then we deal with the well-known entry-exit problem studied by many authors (see [6, 8, 13, 14] and references therein). The entry-exit problem consists of describing the transition map Σ in → Σ out \Sigma_{\text{in}}\rightarrow\Sigma_{\text{out}}, ( x in, δ) ↦ ( Δ ⁡ ( x in, ϵ), δ) (x_{\text{in}},\delta)\mapsto(\Delta(x_{\text{in}},\epsilon),\delta) where

 | Σ in \displaystyle\Sigma_{\text{in}}\, | : y = δ, x in ∈ I in, \displaystyle:\,y=\delta,\,x_{\text{in}}\in I_{\text{in}}, |  |

 | Σ out \displaystyle\Sigma_{\text{out}}\, | : y = δ, x out ∈ I out, \displaystyle:\,y=\delta,\,x_{\text{out}}\in I_{\text{out}}, |  |

with δ > 0 \delta>0 small, I in ⊂ I ∩ ( 0, ∞) I_{\text{in}}\subset I\cap(0,\infty) and I out ⊂ I ∩ ( − ∞, 0) I_{\text{out}}\subset I\cap(-\infty,0) compact intervals. It is well known that the problem with the intervals I in I_{\text{in}} and I out I_{\text{out}} is well defined for all 0 < ϵ ≪ 1 0<\epsilon\ll 1 if for every x in ∈ I in x_{\text{in}}\in I_{\text{in}}, there is an x out = Δ 0 ​ ( x in) ∈ I out x_{\text{out}}=\Delta_{0}(x_{\text{in}})\in I_{\text{out}} such that

(1.3) |  | ∫ x in x out h ⁡ ( s, 0, 0) f ⁡ ( s, 0, 0) ​ 𝑑 s = 0. \displaystyle\int_{x_{\text{in}}}^{x_{\text{out}}}\frac{h(s,0,0)}{f(s,0,0)}ds=0. |  |

In particular, the Dulac map Δ ⁡ ( ⋅, ϵ): I in → ℝ \Delta(\cdot,\epsilon):I_{\text{in}}\rightarrow\mathbb{R}, ϵ ∈] 0, ϵ 0 [)] \epsilon\in]0,\epsilon_{0}[)], takes the following form

 | Δ ⁡ ( x in, ϵ) = Δ 0 ​ ( x in) + 𝒪 ⁡ ( ϵ), \displaystyle\Delta(x_{\text{in}},\epsilon)=\Delta_{0}(x_{\text{in}})+{\color[rgb]{0,0,0}{\mathcal{O}(\epsilon)}}, |  |

where 𝒪 ⁡ ( ϵ) {\color[rgb]{0,0,0}{\mathcal{O}(\epsilon)}} is a smooth function of ( x in, ϵ) (x_{\text{in}},{\color[rgb]{0,0,0}{\epsilon}}) and is identically zero when ϵ = 0 \epsilon=0. Notice that the trajectory leaves y = 0 y=0 after it has become unstable at x = 0 x=0. This phenomena is also known as Pontryagin delay or bifurcation delay, see [2, 13].

On the other hand, if there is an x in ∈ I in x_{\text{in}}\in I_{\text{in}} so that there is no x out ∈ I out x_{\text{out}}\in I_{\text{out}} satisfying ( 1.3), then the entry-exit problem with the intervals I in I_{\text{in}} and I out I_{\text{out}} is not well-defined for all ϵ > 0 \epsilon>0 sufficiently small. For details, we refer to [6] where the entry-exit problem is studied using a novel blow-up technique based upon writing the equations in terms of ( x, z) (x,z) where z z is related to y y through

 | y = e − z − 1, \displaystyle y={\mathrm{e}}^{-z^{-1}}, |  |

see [6, Corollary 1.2]. We will follow this approach in the present paper, see Section 3 for further details. The entry-exit formula ( 1.3) plays an important role in the study of relaxation oscillations in predator-prey systems (see, e.g. [1, 9, 16] and references therein). We also refer to [12, 15] for some other more degenerate entry-exit problems and applications in ℝ 2 \mathbb{R}^{2} and ℝ 3 \mathbb{R}^{3}.

More precisely, if we assume h x ′ ​ ( 0, 0, 0) < 0 h^{\prime}_{x}(0,0,0)<0 and use ( 1.2), then, up to smooth equivalence, system ( 1.1) has the following form

(1.4) |  | x ˙ \displaystyle\dot{x} | = ϵ ​ f 0 ​ ( x, ϵ) + y ​ g 0 ​ ( x, y, ϵ), \displaystyle=\epsilon f_{0}(x,\epsilon)+yg_{0}(x,y,\epsilon), |  |

 | y ˙ \displaystyle\dot{y} | = − x ​ y, \displaystyle=-xy, |  |

for some smooth functions f 0 f_{0} and g 0 g_{0} and g 0 ​ ( 0, 0, 0) = 0 g_{0}(0,0,0)=0 (see Lemma 2.1 in Section 2.1). Here, h x ′ h^{\prime}_{x} denotes the partial derivative of h h w.r.t. x x. In this paper, we focus on the system ( 1.4) and assume that g 0 g_{0} is an arbitrary smooth function ( g 0 ​ ( 0, 0, 0) g_{0}(0,0,0) is not necessarily zero) and that f 0 ​ ( x, 0) f_{0}(x,0) has a zero of even multiplicity 2 ​ n 2n, n ∈ ℕ n\in\mathbb{N}, at x = 0 x=0:

 | ∂ k f 0 ∂ x k ​ ( 0, 0) = 0 ∀ k ∈ { 0, 1, …, 2 ​ n − 1 }, ∂ 2 ​ n f 0 ∂ x 2 ​ n ​ ( 0, 0) < 0. \displaystyle\frac{\partial^{k}f_{0}}{\partial x^{k}}(0,0)=0\quad\forall\,k\in\{0,1,\ldots,2n-1\},\quad\frac{\partial^{2n}f_{0}}{\partial x^{2n}}(0,0)<0. |  |

Since the multiplicity is even, the entry-exit problem may still be well defined.

###### Remark 1.1.

When f 0 ​ ( x, 0) < 0 f_{0}(x,0)<0, the entry-exit problem associated with ( 1.4), with an arbitrary smooth function g 0 g_{0}, has been studied in [9, Section 5].

[image: Refer to caption] Figure 1. A limit periodic set after desingularization of the graphic ( I 2 1) (I_{2}^{1}) through a nilpotent saddle-node at infinity in the Dumortier-Roussarie-Rousseau program.

The case n = 1 n=1 is relevant to the analysis of the graphics ( I 2 1) (I_{2}^{1}) and ( I 4 1) (I_{4}^{1}) through a nilpotent saddle-node singularity at infinity in the Dumortier-Roussarie-Rousseau program (see [7, Figure 8]). The main goal of this program is to solve the finiteness part of Hilbert’s 16th problem for quadratic polynomial systems. After a blow-up at the singular point at infinity one can detect all possible limit periodic sets related to ( I 2 1) (I_{2}^{1}) and ( I 4 1) (I_{4}^{1}) whose finite cyclicity needs to be studied. Such a limit periodic set is given in Fig. 1. Here the invariant line { y = 0 } \{y=0\} corresponds to infinity in a Poincaré compactification and one needs to deal with the entry-exit problem ( 1.4) where f 0 ​ ( x, 0) f_{0}(x,0) has a zero of multiplicity 2 2 and g 0 ≠ 0 g_{0}\neq 0. For more details, we refer to Section 6 and [10]. The case n ≥ 2 n\geq 2 is similarly relevant for the general version of Hilbert’s 16th problem. Besides this purely mathematical question, we believe that the entry-exit problem treated in this paper could also be important when one studies relaxation oscillations in predator-prey systems and other applied slow-fast models.

The upper bounds for the number of canard limit cycles of ( 1.4) with g 0 ​ ( 0, 0, 0) ≠ 0 g_{0}(0,0,0)\neq 0 (and more general slow-fast systems without presence of an invariant line) have been studied in [3, 4] using the notion of the slow divergence integral [5, Chapter 5]. We point out that the entry-exit problem of ( 1.4) has not been treated in [3, 4].

The paper is organized as follows. In Section 2 we define our slow-fast model and state the main results. We introduce a blow-up in Section 3. In Sections 4 and 5 we prove our main results. Section 6 is devoted to the entry-exit problem of the graphics ( I 2 1) (I_{2}^{1}) and ( I 4 1) (I_{4}^{1}). Here we also illustrate our results further by performing some numerical computations.

## 2. Slow-fast model and statement of results

### 2.1. Normal form

We start this section with the following lemma.

###### Lemma 2.1.

Consider system ( 1.1) and assume that h x ′ ​ ( 0, 0, 0) < 0 h^{\prime}_{x}(0,0,0)<0 and ( 1.2) are satisfied. Then there exists a smooth ϵ \epsilon -family of coordinate changes bringing ( 1.1), near I × { 0 } ⊂ ℝ 2 I\times\{0\}\subset\mathbb{R}^{2}, in ( 1.4), up to multiplication by a smooth positive function.

###### Proof.

The conditions h x ′ ​ ( 0, 0, 0) < 0 h^{\prime}_{x}(0,0,0)<0 and ( 1.2) imply that, after an ϵ \epsilon -dependent shift of x x, we can write h h in ( 1.1) as

 | h ⁡ ( x, y, ϵ) = x ​ h 0 ​ ( x, ϵ) + y ​ h 1 ​ ( x, y, ϵ), \displaystyle h(x,y,\epsilon)=xh_{0}(x,\epsilon)+yh_{1}(x,y,\epsilon), |  |

where

 | h 0 ​ ( x, 0) ≤ − c < 0 ∀ x ∈ I, \displaystyle h_{0}(x,0)\leq-c<0\quad\forall\,x\in I, |  |

for some c > 0 c>0 small enough. Upon dividing the right-hand side by the positive factor − h 0 ​ ( x, ϵ) -h_{0}(x,\epsilon) we can achieve that h 0 ​ ( x, ϵ) = − 1 h_{0}(x,\epsilon)=-1 for all x ∈ I x\in I and ϵ ≥ 0 \epsilon\geq 0 small enough. Now define a new coordinate

 | x ~ = x − y ​ h 1 ​ ( x, y, ϵ). \displaystyle\tilde{x}=x-yh_{1}(x,y,\epsilon). |  |

By the implicit function theorem this induces a smooth ϵ \epsilon -family of coordinate changes ( x, y) ↦ ( x ~, y) (x,y)\mapsto(\tilde{x},y) for x ∈ I x\in I and y y kept close to zero. After applying the coordinate change we obtain ( 1.4) with smooth functions f 0 f_{0} and g 0 g_{0} and g 0 ​ ( 0, 0, 0) = 0 g_{0}(0,0,0)=0 (we drop the tildes). ∎

In this paper, we will consider an arbitrary smooth function g 0 g_{0} and a generic unfolding f λ f_{\lambda} of f 0 f_{0} in ( 1.4) :

(2.1) |  | f λ ​ ( x, ϵ) = λ 0 + λ 1 ​ x + ⋯ + λ 2 ​ n − 1 ​ x 2 ​ n − 1 + x 2 ​ n ​ ζ 2 ​ n ​ ( x, ϵ), \displaystyle f_{\lambda}(x,\epsilon)=\lambda_{0}+\lambda_{1}x+\cdots+\lambda_{2n-1}x^{2n-1}+x^{2n}\zeta_{2n}(x,\epsilon), |  |

where λ = ( λ 0, …, λ 2 ​ n − 1) \lambda=(\lambda_{0},\ldots,\lambda_{2n-1}) are the unfolding parameters kept close to zero, ζ 2 ​ n \zeta_{2n} is a smooth function and ζ 2 ​ n ​ ( x, 0) < 0 \zeta_{2n}(x,0)<0 for all x ∈ I x\in I. By redefining ϵ \epsilon, we can easily achieve that

 | ζ 2 ​ n ​ ( 0, 0) = − 1. \zeta_{2n}(0,0)=-1. |  |

It is natural to consider a blow-up of parameters

(2.2) |  | ϵ = r ​ ϵ ¯, λ i = r 2 ​ n − i ​ λ ¯ i, i ∈ { 0, …, 2 ​ n − 1 }, ( ϵ ¯, λ ¯ 0, …, λ ¯ 2 ​ n − 1) ∈ 𝕊 2 ​ n, ϵ ¯ ≥ 0. \displaystyle\epsilon=r\bar{\epsilon},\quad\lambda_{i}=r^{2n-i}\overline{\lambda}_{i},\quad i\in\{0,\ldots,2n-1\},\ (\bar{\epsilon},\overline{\lambda}_{0},\ldots,\overline{\lambda}_{2n-1})\in\mathbb{S}^{2n},\ \bar{\epsilon}\geq 0. |  |

We will only focus on the single chart ϵ ¯ = 1 \bar{\epsilon}=1, setting

 | λ i = ϵ 2 ​ n − i ​ λ ~ i, i ∈ { 0, …, 2 ​ n − 1 }, \displaystyle\lambda_{i}=\epsilon^{2n-i}\widetilde{\lambda}_{i},\quad i\in\{0,\ldots,2n-1\}, |  |

with λ ~ = ( λ ~ 0, …, λ ~ 2 ​ n − 1) \widetilde{\lambda}=(\widetilde{\lambda}_{0},\ldots,\widetilde{\lambda}_{2n-1}) kept in a compact subset Λ \Lambda of ℝ 2 ​ n \mathbb{R}^{2n}, so that

(2.3) |  | f λ ~ ​ ( x, ϵ):= f ( ϵ 2 ​ n ​ λ ~ 0, …, ϵ ​ λ ~ 2 ​ n − 1) ​ ( x, ϵ) = ϵ 2 ​ n ​ P λ ~ ​ ( ϵ − 1 ​ x) + x 2 ​ n ​ ( ζ 2 ​ n ​ ( x, ϵ) + 1), \displaystyle f_{\widetilde{\lambda}}(x,\epsilon):=f_{(\epsilon^{2n}\widetilde{\lambda}_{0},\ldots,\epsilon\widetilde{\lambda}_{2n-1})}(x,\epsilon)=\epsilon^{2n}P_{\widetilde{\lambda}}(\epsilon^{-1}x)+x^{2n}(\zeta_{2n}(x,\epsilon)+1), |  |

with

(2.4) |  | P λ ~ ​ ( x 2):= λ ~ 0 + λ ~ 1 ​ x 2 + ⋯ + λ ~ 2 ​ n − 1 ​ x 2 2 ​ n − 1 − x 2 2 ​ n, \displaystyle P_{\widetilde{\lambda}}(x_{2}):=\widetilde{\lambda}_{0}+\widetilde{\lambda}_{1}x_{2}+\cdots+\widetilde{\lambda}_{2n-1}x_{2}^{2n-1}-x_{2}^{2n}, |  |

For simplicity we drop the tildes and write f λ, P λ f_{\lambda},P_{\lambda} instead of f λ ~, P λ ~ f_{\widetilde{\lambda}},P_{\widetilde{\lambda}}.

Finally, we consider n ∈ ℕ n\in\mathbb{N} and

(2.5) |  | x ˙ \displaystyle\dot{x} | = ϵ ​ f λ ​ ( x, ϵ) + y ​ g ​ ( x, y, ϵ), \displaystyle=\epsilon f_{\lambda}(x,\epsilon)+yg(x,y,\epsilon), |  |

 | y ˙ \displaystyle\dot{y} | = − x ​ y, \displaystyle=-xy, |  |

with f λ f_{\lambda} given by ( 2.3) with λ ∈ Λ \lambda\in\Lambda and ζ 2 ​ n ​ ( 0, 0) = − 1 \zeta_{2n}(0,0)=-1. We will suppose that f λ f_{\lambda} and g g are C ∞ C^{\infty} -smooth functions.

The following lemma provides conditions for the existence of a regular passage along the invariant line { y = 0 } \{y=0\} of ( 2.5), for ϵ > 0 \epsilon>0.

###### Lemma 2.2.

Suppose that

(2.6) |  | ζ 2 ​ n ​ ( x, 0) ≤ − c, ∀ x ∈ I, \displaystyle\zeta_{2n}(x,0)\leq-c,\quad\forall\,x\in I, |  |

and that

(2.7) |  | P λ ​ ( x 2) ≤ − c ∀ x 2 ∈ ℝ, λ ∈ Λ, \displaystyle P_{\lambda}(x_{2})\leq-c\quad\forall\,x_{2}\in\mathbb{R},\ \lambda\in\Lambda, |  |

for some c > 0 c>0 and Λ ⊂ ℝ 2 ​ n \Lambda\subset\mathbb{R}^{2n} a compact set. Then there is an ϵ 0 > 0 \epsilon_{0}>0 such that

 | f λ ​ ( x, ϵ) < 0 ∀ x ∈ I, ϵ ∈] 0, ϵ 0 [, λ ∈ Λ. \displaystyle f_{\lambda}(x,\epsilon)<0\quad\forall\,x\in I,\,\epsilon\in]0,\epsilon_{0}[,\ \lambda\in\Lambda. |  |

###### Proof.

Let γ > 0 \gamma>0 and ϵ > 0 \epsilon>0.

For x ∈ I \ [− ϵ ​ γ − 1, ϵ ​ γ − 1] x\in I\backslash[-\epsilon\gamma^{-1},\epsilon\gamma^{-1}], we use ( 2.3) and estimate:

 | f λ ​ ( x, ϵ) \displaystyle f_{\lambda}(x,\epsilon) | = x 2 ​ n ​ ( ϵ 2 ​ n ​ x − 2 ​ n ​ λ 0 + ϵ 2 ​ n − 1 ​ x − 2 ​ n + 1 ​ λ 1 + ⋯ + ϵ ​ x − 1 ​ λ 2 ​ n − 1) + x 2 ​ n ​ ζ 2 ​ n ​ ( x, ϵ) \displaystyle=x^{2n}\left(\epsilon^{2n}x^{-2n}\lambda_{0}+\epsilon^{2n-1}x^{-2n+1}\lambda_{1}+\cdots+\epsilon x^{-1}\lambda_{2n-1}\right)+x^{2n}\zeta_{2n}(x,\epsilon) |  |

 |  | < x 2 ​ n ​ ( γ 2 ​ n ​ | λ 0 | + γ 2 ​ n − 1 ​ | λ 1 | + ⋯ + γ ​ | λ 2 ​ n − 1 | + ζ 2 ​ n ​ ( x, ϵ)) \displaystyle<x^{2n}\left(\gamma^{2n}|\lambda_{0}|+\gamma^{2n-1}|\lambda_{1}|+\cdots+\gamma|\lambda_{2n-1}|+\zeta_{2n}(x,\epsilon)\right) |  |

 |  | ≤ x 2 ​ n ​ ( 𝒪 ⁡ ( γ) − C) < 0, \displaystyle\leq x^{2n}\left(\mathcal{O}(\gamma)-C\right)<0, |  |

for a constant C > 0 C>0, for all γ > 0 \gamma>0 small enough, λ ∈ Λ \lambda\in\Lambda and for all ϵ ∈] 0, ϵ 0 [\epsilon\in]0,\epsilon_{0}[, with ϵ 0 > 0 \epsilon_{0}>0 small. Here we have used ( 2.6). We fix such a γ > 0 \gamma>0.

Using ( 2.3) again, we can write

 | f λ ​ ( x, ϵ) = ϵ 2 ​ n ​ ( P λ ​ ( ϵ − 1 ​ x) + ( x ϵ) 2 ​ n ​ ( ζ 2 ​ n ​ ( x, ϵ) + 1)), \displaystyle f_{\lambda}(x,\epsilon)=\epsilon^{2n}\left(P_{\lambda}(\epsilon^{-1}x)+\left(\frac{x}{\epsilon}\right)^{2n}(\zeta_{2n}(x,\epsilon)+1)\right), |  |

for ϵ > 0 \epsilon>0. This, together with ( 2.7) and ζ 2 ​ n ​ ( 0, 0) = − 1 \zeta_{2n}(0,0)=-1, implies that f λ ​ ( x, ϵ) < 0 f_{\lambda}(x,\epsilon)<0 for all x ∈ [− ϵ ​ γ − 1, ϵ ​ γ − 1] x\in[-\epsilon\gamma^{-1},\epsilon\gamma^{-1}], λ ∈ Λ \lambda\in\Lambda and all ϵ ∈] 0, ϵ 0 [\epsilon\in]0,\epsilon_{0}[, up to shrinking ϵ 0 \epsilon_{0} if necessary. This completes the proof of the lemma. ∎

It is clear from ( 2.4) that Λ \Lambda with the property ( 2.7) exists. For the rest of the paper, we assume that ( 2.6) and ( 2.7) are satisfied.

###### Remark 2.3.

For a complete analysis of the unfolding ( 2.1), one would have to study the remaining charts associated with the blow-up ( 2.2). We leave this to the interested reader, but we believe that these cases can be covered through a combination of the present work (in the chart ϵ ¯ = 1 \bar{\epsilon}=1) with standard results on entry-exit, e.g. [6].

### 2.2. Statement of the main results

In this section, we state the main results (Theorem 2.4 for n = 1 n=1 and Theorem 2.7 for n ≥ 2 n\geq 2).

For ϵ = 0 \epsilon=0, system ( 2.5) becomes

 | x ˙ \displaystyle\dot{x} | = y ​ g ​ ( x, y, 0), \displaystyle=yg(x,y,0), |  |

 | y ˙ \displaystyle\dot{y} | = − x ​ y, \displaystyle=-xy, |  |

or written as as an equation or y = y ⁡ ( x) y=y(x) for y ≠ 0 y\neq 0

(2.8) |  | d ​ x d ​ y = − x − 1 ​ g ​ ( x, y, 0). \displaystyle\frac{dx}{dy}=-x^{-1}g(x,y,0). |  |

Notice that ( 2.8) is well defined and regular for all y ∈ [0, δ] y\in[0,\delta], δ ∈ ( 0, 1) \delta\in(0,1) small enough, and x ∈ I in x\in I_{\text{in}} where I in ⊂ ( 0, ∞) I_{\text{in}}\subset(0,\infty) is a compact interval. More precisely, let x = ψ ⁡ ( x in, y), y ∈ [0, δ] x=\psi(x_{\text{in}},y),\,y\in[0,\delta], denote the C ∞ C^{\infty} -smooth solution of ( 2.8) with the initial condition ψ ⁡ ( x in, δ) = x in ∈ I in \psi(x_{\text{in}},\delta)=x_{\text{in}}\in I_{\text{in}} at y = δ y=\delta. We then define ( x in b, 0) (x_{\text{in}}^{b},0) as the base point of ( x in, δ) ∈ Σ in (x_{\text{in}},\delta)\in\Sigma_{\text{in}} on y = 0 y=0:

(2.9) |  | x in b:= ψ ⁡ ( x in, 0). \displaystyle x_{\text{in}}^{b}:=\psi(x_{\text{in}},0). |  |

We suppose that x in b ∈ I ∩ ( 0, ∞) x_{\text{in}}^{b}\in I\cap(0,\infty), with I I fixed in Lemma 2.2. Finally, x out b = x out b ​ ( x out) ∈ I ∩ ( − ∞, 0) x_{\text{out}}^{b}=x_{\text{out}}^{b}(x_{\text{out}})\in I\cap(-\infty,0) is defined completely analogously for x out ∈ I out x_{\text{out}}\in I_{\text{out}}, see Fig. 2.

[image: Refer to caption]

in in out out in out

Figure 2. Illustration of the base point ( x in / out b, 0) (x_{\text{in}/\text{out}}^{b},0) of ( x in / out, δ) ∈ Σ in / out (x_{\text{in}/\text{out}},\delta)\in\Sigma_{\text{in}/\text{out}}.

First, we assume that n = 1 n=1 in ( 2.5). We then consider the Cauchy principal values

(2.10) |  | p.v. ​ ∫ x out b x in b 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s:= lim ρ → 0 + ( ∫ x out b − ρ 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + ∫ ρ x in b 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s) \displaystyle\text{p.v.}\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{1}{s\zeta_{2}(s,0)}ds:=\lim_{\rho\to 0^{+}}\left(\int_{x_{\text{out}}^{b}}^{-\rho}\frac{1}{s\zeta_{2}(s,0)}ds+\int_{\rho}^{x_{\text{in}}^{b}}\frac{1}{s\zeta_{2}(s,0)}ds\right) |  |

and

(2.11) |  | p.v. ​ ∫ − ∞ + ∞ s P λ ​ ( s) ​ 𝑑 s:= lim ρ → ∞ ∫ − ρ ρ s P λ ​ ( s) ​ 𝑑 s. \displaystyle\text{p.v.}\int_{-\infty}^{+\infty}\frac{s}{P_{\lambda}(s)}ds:=\lim_{\rho\to\infty}\int_{-\rho}^{\rho}\frac{s}{P_{\lambda}(s)}ds. |  |

We then have the following result.

###### Theorem 2.4.

Fix any k ∈ ℕ k\in\mathbb{N} and consider system ( 2.5) with n = 1 n=1 and P λ ​ ( x 2) = λ 0 + λ 1 ​ x 2 − x 2 2 P_{\lambda}(x_{2})=\lambda_{0}+\lambda_{1}x_{2}-x_{2}^{2}. Suppose that ( 2.6) and ( 2.7) are satisfied and that for every x in ∈ I in x_{\text{in}}\in I_{\text{in}} there is a x out = Δ 0 ​ ( x in) ∈ I out x_{\text{out}}=\Delta_{0}(x_{\text{in}})\in I_{\text{out}} so that

(2.12) |  | p.v. ​ ∫ x out b x in b 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + p.v. ​ ∫ − ∞ + ∞ s P λ ​ ( s) ​ 𝑑 s = 0, \displaystyle\text{p.v.}\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{1}{s\zeta_{2}(s,0)}ds+\text{p.v.}\int_{-\infty}^{+\infty}\frac{s}{P_{\lambda}(s)}ds=0, |  |

with x in b = x in b ​ ( x in) x_{\text{in}}^{b}=x_{\text{in}}^{b}(x_{\text{in}}) and x out b = x out b ​ ( x out) x_{\text{out}}^{b}=x_{\text{out}}^{b}(x_{\text{out}}) defined above. Then the Dulac map Δ ⁡ ( ⋅, ϵ): I in → ℝ \Delta(\cdot,\epsilon):I_{\text{in}}\rightarrow{\color[rgb]{0,0,0}{\mathbb{R}}} is well-defined for all ϵ ∈] 0, ϵ 0 [\epsilon\in]0,\epsilon_{0}[, with ϵ 0 > 0 \epsilon_{0}>0 small, and takes the following form

 | Δ ⁡ ( x in, ϵ) = Δ 0 ​ ( x in) + ϕ ⁡ ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1), \displaystyle\Delta(x_{\text{in}},\epsilon)=\Delta_{0}(x_{\text{in}})+\phi(x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}), |  |

where ϕ: I in × [0, ϵ 0) × [0, ϵ 0 ​ log ⁡ ϵ 0 − 1) → ℝ \phi:I_{\text{in}}\times[0,\epsilon_{0})\times[0,\epsilon_{0}\log\epsilon_{0}^{-1})\rightarrow\mathbb{R} is C k C^{k} -smooth and satisfies ϕ ⁡ ( x in, 0, 0) = 0 \phi(x_{\text{in}},0,0)=0 for all x in ∈ I in x_{\text{in}}\in I_{\text{in}}.

We prove Theorem 2.4 in Section 4. The smoothness w.r.t. ( ϵ, ϵ ​ log ⁡ ϵ − 1) (\epsilon,\epsilon\log\epsilon^{-1}) is natural since we will deal with the passage near a line of saddle singularities with positive and negative eigenvalues of equal magnitude (see Lemma 3.1). However, it might be possible (although we do not expect it) that the final transition map is in fact smooth w.r.t. ϵ \epsilon (as in [6]). We have not pursued this in the present work since (a) it is not expected to be important for the cyclicity results of ( I 2 1) (I_{2}^{1}) and ( I 4 1) (I_{4}^{1}) and (b) it does not seem like a trivial task. Notice in particular w.r.t. (b) that logarithms also appear due to resonances associated with a separate blow-up transformation (see e.g. ( 4.9) below).

###### Remark 2.5.

From ( 2.10), ζ 2 ​ ( 0, 0) = − 1 \zeta_{2}(0,0)=-1 and

 | 1 s ​ ζ 2 ​ ( s, 0) = ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) − 1 s, \displaystyle\frac{1}{s\zeta_{2}(s,0)}=\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}-\frac{1}{s}, |  |

it follows that

 | p.v. ​ ∫ x out b x in b 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s = ∫ x out b x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + log ⁡ ( − x out b x in b). \text{p.v.}\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{1}{s\zeta_{2}(s,0)}ds=\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds+\log\left(-\frac{x_{\text{out}}^{b}}{x_{\text{in}}^{b}}\right). |  |

Using ( 2.11) and P λ ​ ( s) = λ 0 + λ 1 ​ s − s 2 P_{\lambda}(s)=\lambda_{0}+\lambda_{1}s-s^{2}, it is not difficult to see that

 | p.v. ​ ∫ − ∞ + ∞ s P λ ​ ( s) ​ 𝑑 s \displaystyle\text{p.v.}\int_{-\infty}^{+\infty}\frac{s}{P_{\lambda}(s)}ds | = ∫ − 1 1 s P λ ​ ( s) d s + ( ∫ − ∞ − 1 + ∫ 1 ∞) P λ ​ ( s) + s 2 s ​ P λ ​ ( s) d s \displaystyle=\int_{-1}^{1}\frac{s}{P_{\lambda}(s)}ds+\left(\int_{-\infty}^{-1}+\int_{1}^{\infty}\right)\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds |  |

 |  | = − λ 1 ​ π − 4 ​ λ 0 − λ 1 2. \displaystyle=-\frac{\lambda_{1}\pi}{\sqrt{-4\lambda_{0}-\lambda_{1}^{2}}}. |  |

If we now plug in these expressions into ( 2.12), we get the following entry-exit formula

(2.13) |  | ∫ x out b x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + log ⁡ ( − x out b x in b) = λ 1 ​ π − 4 ​ λ 0 − λ 1 2. \displaystyle\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds+\log\left(-\frac{x_{\text{out}}^{b}}{x_{\text{in}}^{b}}\right)=\frac{\lambda_{1}\pi}{\sqrt{-4\lambda_{0}-\lambda_{1}^{2}}}. |  |

###### Remark 2.6.

(a) The first (resp. second) integral on the right hand side in ( 2.10) is the slow divergence integral [5, Chapter 5] of ( 2.5), with n = 1 n=1, associated with the normally repelling (resp. attracting) segment [x out b, − ρ] [x_{\text{out}}^{b},-\rho] (resp. [ρ, x in b] [\rho,x_{\text{in}}^{b}]) of the curve of singularities { y = 0 } \{y=0\}. These are integrals of the divergence of the vector field ( 2.5), for ϵ = 0 \epsilon=0 and calculated along { y = 0 } \{y=0\}, where the integration variable is the time variable τ \tau of the flow of the slow vector field [5, Chapter 3]

 | d ​ x d ​ τ = x 2 ​ ζ 2 ​ ( x, 0). \frac{dx}{d\tau}=x^{2}\zeta_{2}(x,0). |  |

Note that the integral in the classical entry-exit formula ( 1.3) is equal to the slow divergence integral of system ( 1.1) computed along the segment [x out, x in] [x_{\text{out}},x_{\text{in}}].

(b) The Cauchy principal value in ( 2.11) is related to the divergence integral on the second cylinder (see Section 3), defined in terms of P λ P_{\lambda}. For more details, we refer the reader to Section 4 (see Remark 4.7).

When n ≥ 2 n\geq 2 in ( 2.5), we have the following result.

###### Theorem 2.7.

Fix any k ∈ ℕ k\in\mathbb{N} and consider the system ( 2.5) with n ≥ 2 n\geq 2. Suppose that ( 2.6) and ( 2.7) are satisfied. Then ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v \int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv is well-defined and we suppose that:

(2.14) |  | ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v ≠ 0. \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv\neq 0. |  |

Then the entry-exit problem I in ∋ x in ↦ Δ ⁡ ( x in, ϵ) ∈ I out I_{\text{in}}\ni x_{\text{in}}\mapsto\Delta(x_{\text{in}},\epsilon)\in I_{\text{out}} is not well-defined for all 0 < ϵ ≪ 1 0<\epsilon\ll 1. In further details, let ( 0, e − 1 / z in/out) (0,{\mathrm{e}}^{-1/z_{\text{in/out}}}) denote the intersection points of the forward and backward flow of ( x in, δ) ∈ Σ in (x_{\text{in}},\delta)\in\Sigma_{\text{in}} and ( x out, δ) ∈ Σ out (x_{\text{out}},\delta)\in\Sigma_{\text{out }}, respectively, with { x = 0 } \{x=0\}. Then

(2.15) |  | z in = z in ​ ( x in, ϵ) \displaystyle z_{\text{in}}=z_{\text{in}}(x_{\text{in}},\epsilon) | = ϵ 2 ​ n − 1 ​ ( 1 − ∫ 0 ∞ v P λ ​ ( v) d v + ϕ in ​ ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1)), \displaystyle=\epsilon^{2n-1}\left(\frac{1}{-\int_{0}^{\infty}\frac{v}{P_{\lambda}(v)}dv}+\phi_{\text{in}}({\color[rgb]{0,0,0}{x_{\text{in}}}},\epsilon,\epsilon\log\epsilon^{-1})\right), |  |

 | z out = z out ​ ( x out, ϵ) \displaystyle z_{\text{out}}=z_{\text{out}}(x_{\text{out}},\epsilon) | = ϵ 2 ​ n − 1 ​ ( 1 ∫ − ∞ 0 v P λ ​ ( v) ​ 𝑑 v + ϕ out ​ ( x out, ϵ, ϵ ​ log ⁡ ϵ − 1)), \displaystyle=\epsilon^{2n-1}\left(\frac{1}{\int_{-\infty}^{0}\frac{v}{P_{\lambda}(v)}dv}+\phi_{\text{out}}({\color[rgb]{0,0,0}{x_{\text{out}}}},\epsilon,\epsilon\log\epsilon^{-1})\right), |  |

with each ϕ in/out: I in/out × [0, ϵ 0) × [0, ϵ 0 ​ log ⁡ ϵ 0 − 1) → ℝ \phi_{\text{in/out}}:I_{\text{in/out}}\times[0,\epsilon_{0})\times[0,\epsilon_{0}\log\epsilon_{0}^{-1})\rightarrow\mathbb{R} being C k C^{k} smooth and ϕ in/out ​ ( x, 0, 0) = 0 \phi_{\text{in/out}}(x,0,0)=0 for all x ∈ I in/out x\in I_{\text{in/out}}. Therefore if ( 2.14) holds true, then z in ≠ z out z_{\text{in}}\neq z_{\text{out}} for all x in ∈ I in, x out ∈ I out x_{\text{in}}\in I_{\text{in}},x_{\text{out}}\in I_{\text{out}}, 0 < ϵ ≪ 1 0<\epsilon\ll 1.

We prove Theorem 2.7 in Section 5.

###### Remark 2.8.

In contrast to Theorem 2.4, the contraction/expansion towards y = 0 y=0 is dominated by the passage near x = 0 x=0 for n ≥ 2 n\geq 2. Indeed, on either side of x = 0 x=0, transition maps y ↦ y + y\mapsto y_{+} between different sections { x = x 0 } \{x=x_{0}\} and { x = x 1 } \{x=x_{1}\}, x 0 ​ x 1 > 0 x_{0}x_{1}>0, are to leading order given by y + = exp ⁡ ( ϵ − 1 ​ I) y_{+}=\exp(\epsilon^{-1}I) with

 | I = ∫ x 0 x 1 − x f λ ​ ( x, 0) d x. \displaystyle{\color[rgb]{0,0,0}{I=\int_{x_{0}}^{x_{1}}-\frac{x}{f_{\lambda}(x,0)}dx}}. |  |

This follows from the theory of slow-divergence integrals, see [5]. On the other hand, if we put x = ϵ ​ x 2 x=\epsilon x_{2}, then on either side of x 2 = 0 x_{2}=0, transition maps y ↦ y + y\mapsto y_{+} between different sections { x 2 = x 20 } \{x_{2}=x_{20}\} and { x 2 = x 21 } \{x_{2}=x_{21}\}, x 20 ​ x 21 > 0 x_{20}x_{21}>0, are to leading order given by exp ⁡ ( ϵ − 2 ​ n + 1 ​ I 2) \exp(\epsilon^{-2n+1}I_{2}) with

 | I 2 = ∫ x 20 x 21 − x 2 P λ ​ ( x 2) d x 2. \displaystyle I_{2}=\int_{x_{20}}^{x_{21}}-\frac{x_{2}}{P_{\lambda}(x_{2})}dx_{2}. |  |

We obtain this by substituting x = ϵ ​ x 2 x=\epsilon x_{2} into ( 2.5); for the purpose of this remark, we have just retained the dominating terms (and ignored g g in ( 2.5)). Since − 2 ​ n + 1 < − 1 -2n+1<-1 for n ≥ 2 n\geq 2 this illustrates our claim. For n = 1 n=1, the contractions/expansions for x = 𝒪 ⁡ ( 1) x=\mathcal{O}(1) and x = 𝒪 ⁡ ( ϵ) x=\mathcal{O}(\epsilon) are comparable.

The sign of the integral ( 2.14) determines the sign of z in − z out z_{\text{in}}-z_{\text{out}}. In particular, if

 | ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v < 0, \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv<0, |  |

then

 | 0 < z in < z out, \displaystyle 0<z_{\text{in}}<z_{\text{out}}, |  |

recall ( 2.15), for all 0 < ϵ ≪ 1 0<\epsilon\ll 1, x in / out ∈ I in / out x_{\text{in}/\text{out}}\in I_{\text{in}/\text{out}}. This follows from ( 2.15) using P λ ​ ( x 2) < 0 P_{\lambda}(x_{2})<0. Since the problem is planar, a simple corollary of this fact is that the forward orbit of ( x in, δ) ∈ Σ in (x_{\text{in}},\delta)\in\Sigma_{\text{in}} for any x in ∈ I in x_{\text{in}}\in I_{\text{in}} intersects { x = x out } \{x=x_{\text{out}}\} with y = 𝒪 ⁡ ( e − c ​ ϵ − 2 ​ n + 1) y=\mathcal{O}({\mathrm{e}}^{-c\epsilon^{-2n+1}}), c > 0 c>0, for ϵ → 0 \epsilon\to 0 for any x out ∈ I out x_{\text{out}}\in I_{\text{out}}.

On the other hand, if

 | ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v > 0, \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv>0, |  |

then

 | z in > z out > 0, \displaystyle z_{\text{in}}>z_{\text{out}}>0, |  |

and the forward orbit of ( x in, δ) ∈ Σ in (x_{\text{in}},\delta)\in\Sigma_{\text{in}} for any x in ∈ I in x_{\text{in}}\in I_{\text{in}} intersects { y = δ } \{y=\delta\} with x = o ⁡ ( 1) < 0 x=o(1)<0 for ϵ → 0 \epsilon\to 0.

The remaining case

 | ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v = 0, \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv=0, |  |

is similar to classical canard situation, see [5], when we treat λ \lambda as control parameters. Indeed, we have the following.

###### Corollary 2.9.

Consider as in Theorem 2.7 any k ∈ ℕ k\in\mathbb{N}, n ≥ 2 n\geq 2 and denote Δ ⁡ ( x, ϵ) \Delta(x,\epsilon) by Δ ⁡ ( x, ϵ, λ) \Delta(x,\epsilon;\lambda) to emphasize its dependency on λ = ( λ 0, …, λ 2 ​ n − 1) ∈ Λ \lambda=(\lambda_{0},\ldots,\lambda_{2n-1})\in\Lambda. Now, let l ∈ { 0, …, 2 ​ n − 1 } l\in\{0,\ldots,2n-1\} and λ 0 ∈ Λ \lambda^{0}\in\Lambda be such that

(2.16) |  | ∫ − ∞ ∞ v P λ 0 ​ ( v) ​ 𝑑 v = 0 and ∂ ∂ λ l ​ ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v | λ = λ 0 ≠ 0. \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda^{0}}(v)}dv=0\quad\mbox{and}\quad\frac{\partial}{\partial\lambda_{l}}\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv\bigg|_{\lambda=\lambda^{0}}\neq 0. |  |

Then there is an ( x in, x out, ϵ) (x_{\text{in}},x_{\text{out}},\epsilon) -dependent local embedding defined by

 | Λ ^ ∋ λ ^ ↦ λ = λ ¯ ​ ( x in, x out, ϵ, λ ^) ∈ ℝ 2 ​ n, \widehat{\Lambda}\ni\widehat{\lambda}\mapsto\lambda=\overline{\lambda}(x_{\text{in}},x_{\text{out}},\epsilon,\widehat{\lambda})\in\mathbb{R}^{2n}, |  |

with Λ ^ ⊂ ℝ 2 ​ n − 1 \widehat{\Lambda}\subset\mathbb{R}^{2n-1} being a sufficiently small neighborhood of the origin in ℝ 2 ​ n − 1 \mathbb{R}^{2n-1}, and where λ ¯ \overline{\lambda} is C k C^{k} -smooth w.r.t.

 | ( x in, x out, ϵ, ϵ ​ log ⁡ ϵ − 1, λ ^) ∈ I in × I out × [0, ϵ 0) × [0, ϵ 0 ​ log ⁡ ϵ 0 − 1) × Λ ^, 0 < ϵ 0 ≪ 1, {\color[rgb]{0,0,0}{(x_{\text{in}},x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1},\widehat{\lambda})\in I_{\text{in}}\times I_{\text{out}}\times[0,\epsilon_{0})\times[0,\epsilon_{0}\log\epsilon_{0}^{-1})\times\widehat{\Lambda},\quad 0<\epsilon_{0}\ll 1}}, |  |

such that

 | λ ¯ ​ ( x in, x out, 0, 0) = λ 0 ∀ x in ∈ I in, x out ∈ I out, \displaystyle\overline{\lambda}(x_{\text{in}},x_{\text{out}},0,0)=\lambda^{0}\quad\forall\,x_{\text{in}}\in I_{\text{in}},\,x_{\text{out}}\in I_{\text{out}}, |  |

and

 | Δ ⁡ ( x in, ϵ, λ ¯ ​ ( x in, x o ​ u ​ t, ϵ, λ ^)) = x out ∀ ( x in, x out, ϵ, λ ^) ∈ I in × I out × [0, ϵ 0) × Λ ^. \displaystyle\Delta(x_{\text{in}},\epsilon;\overline{\lambda}(x_{\text{in}},x_{out},\epsilon,\widehat{\lambda}))=x_{\text{out}}\quad\forall\,(x_{\text{in}},x_{\text{out}},\epsilon,\widehat{\lambda})\in I_{\text{in}}\times I_{\text{out}}\times[0,\epsilon_{0})\times\widehat{\Lambda}. |  |

###### Proof.

We have x out = Δ ⁡ ( x in, ϵ, λ) x_{\text{out}}=\Delta(x_{\text{in}},\epsilon;\lambda) if and only if z in ​ ( x in, ϵ) = z out ​ ( x out, ϵ) z_{\text{in}}(x_{\text{in}},\epsilon)=z_{\text{out}}(x_{\text{out}},\epsilon). From ( 2.15), this reduces to

 | ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v = o ⁡ ( 1). \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv=o(1). |  |

Here o ⁡ ( 1) o(1) is a C k C^{k} -smooth function w.r.t. x in, x out, ϵ, ϵ ​ log ⁡ ϵ − 1 x_{\text{in}},x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1} and λ ∈ Λ \lambda\in\Lambda, which vanishes for ϵ = 0 \epsilon=0. This follows from the proof of Theorem 2.7. The result then follows from a simple application of the implicit function theorem. ∎

###### Remark 2.10.

Let λ 0 = ( λ 0 0, …, λ 2 ​ n − 1 0) ∈ Λ \lambda^{0}=(\lambda_{0}^{0},\ldots,\lambda_{2n-1}^{0})\in\Lambda be so that λ j 0 = 0 \lambda_{j}^{0}=0 for all odd j ∈ { 1, 3, …, 2 ​ n − 1 } j\in\{1,3,\ldots,2n-1\}. Then the first condition in ( 2.16) clearly holds since the integrand is an odd function. Moreover, for any odd l ∈ { 1, 3, …, 2 ​ n − 1 } l\in\{1,3,\ldots,2n-1\}, we find that

 | ∂ ∂ λ l ∫ − ∞ ∞ v P λ ​ ( v) d v | λ = λ 0 = − ∫ − ∞ ∞ v 1 + l P λ 0 ​ ( v) 2 d v, \displaystyle\frac{\partial}{\partial\lambda_{l}}\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv\bigg|_{\lambda=\lambda^{0}}=-\int_{-\infty}^{\infty}\frac{v^{1+l}}{P_{\lambda^{0}}(v)^{2}}dv, |  |

which is negative since the integrand is an even function of v v.

## 3. Blow-up

Following [6], we define z ≥ 0 z\geq 0 through

(3.1) |  | y = { e − 1 / z for z > 0, 0 for z = 0. \displaystyle y=\begin{cases}{\mathrm{e}}^{-1/z}&\mbox{for $z>0$},\\ 0&\mbox{for $z=0$}.\end{cases} |  |

Then ( 2.5) becomes

(3.2) |  | x ˙ \displaystyle\dot{x} | = ϵ f λ ( x, ϵ) + e − 1 / z g ( x, e − 1 / z, ϵ), \displaystyle=\epsilon f_{\lambda}(x,\epsilon)+{\mathrm{e}}^{-1/z}g(x,{\mathrm{e}}^{-1/z},\epsilon), |  |

 | z ˙ \displaystyle\dot{z} | = − x ​ z 2, \displaystyle=-xz^{2}, |  |

 | ϵ ˙ \displaystyle\dot{\epsilon} | = 0, \displaystyle=0, |  |

after augmenting a trivial equation for ϵ \epsilon. Notice that ( x, 0, 0) (x,0,0) defines a line of degenerate singularities, the linearization having only zero eigenvalues. The transformation ( 3.1) enables the use of blow-up for the entry-exit problem. In particular, we consider the cylindrical blow-up transformation

(3.3) |  | ρ ≥ 0, ( z ¯, ϵ ¯) ∈ 𝕊 1 ↦ { z = ρ ​ z ¯, ϵ = ρ ​ ϵ ¯, \displaystyle\rho\geq 0,\,(\bar{z},\bar{\epsilon})\in\mathbb{S}^{1}\mapsto\begin{cases}z&=\rho\bar{z},\\ \epsilon&=\rho\bar{\epsilon},\end{cases} |  |

leaving x x fixed, and use a desingularization corresponding to division of the pull-back vector field by ρ \rho. Note that z ¯ ≥ 0 \bar{z}\geq 0 and ϵ ¯ ≥ 0 \bar{\epsilon}\geq 0. We use two separate charts z ¯ = 1 \bar{z}=1 and ϵ ¯ = 1 \bar{\epsilon}=1 with chart-specific coordinates ( ρ 1, ϵ 1) (\rho_{1},\epsilon_{1}) and ( z 2, ρ 2) (z_{2},\rho_{2}) defined by

 | z ¯ = 1: { z = ρ 1, ϵ = ρ 1 ​ ϵ 1, \displaystyle\bar{z}=1:\quad\begin{cases}z&=\rho_{1},\\ \epsilon&=\rho_{1}\epsilon_{1},\end{cases} |  |

(3.4) |  | ϵ ¯ = 1: { z = ρ 2 ​ z 2, ϵ = ρ 2. \displaystyle\bar{\epsilon}=1:\quad\begin{cases}z&=\rho_{2}z_{2},\\ \epsilon&=\rho_{2}.\end{cases} |  |

Here, the desingularization is achieved by division of the vector field by ρ 1 \rho_{1} resp. ρ 2 \rho_{2}. The change of coordinates is well-defined for z 2 > 0 z_{2}>0 and are given by the expressions

(3.5) |  | { ρ 1 = ρ 2 ​ z 2, ϵ 1 = z 2 − 1. \displaystyle\begin{cases}\rho_{1}&=\rho_{2}z_{2},\\ \epsilon_{1}&=z_{2}^{-1}.\end{cases} |  |

Figure 3. Cylindrical blowup of the degenerate line ( x, z, ϵ) = ( x, 0, 0) (x,z,\epsilon)=(x,0,0) by ( 3.3).

### 3.1. Chart z ¯ = 1 \bar{z}=1

In this chart, we obtain the desingularized vector field defined by

(3.6) |  | x ˙ \displaystyle\dot{x} | = ϵ 1 f λ ( x, ρ 1 ϵ 1) + ρ 1 − 1 e − 1 / ρ 1 g ( x, e − 1 / ρ 1, ρ 1 ϵ 1), \displaystyle=\epsilon_{1}f_{\lambda}(x,\rho_{1}\epsilon_{1})+\rho_{1}^{-1}{\mathrm{e}}^{-1/\rho_{1}}g(x,{\mathrm{e}}^{-1/\rho_{1}},\rho_{1}\epsilon_{1}), |  |

 | ρ ˙ 1 \displaystyle\dot{\rho}_{1} | = − x ​ ρ 1, \displaystyle=-x\rho_{1}, |  |

 | ϵ ˙ 1 \displaystyle\dot{\epsilon}_{1} | = x ​ ϵ 1, \displaystyle=x\epsilon_{1}, |  |

which extends smoothly to ρ 1 = 0 \rho_{1}=0. In particular, the last term in the equation for x x is C ∞ C^{\infty} flat w.r.t. ρ 1 = 0 \rho_{1}=0, uniformly w.r.t. x x and ϵ 1 \epsilon_{1}. The point ( x, 0, 0) (x,0,0), with x ≠ 0 x\neq 0, is therefore a semi-hyperbolic singularity of ( 3.6), the linearization having eigenvalues 0, − x, x 0,-x,x. Moreover, ϵ 1 = 0 \epsilon_{1}=0 and ρ 1 = 0 \rho_{1}=0 define two invariant sets of ( 3.6). Within the latter, we find that

 | x ˙ \displaystyle\dot{x} | = ϵ 1 ​ f λ ​ ( x, 0) = ϵ 1 ​ x 2 ​ n ​ ζ 2 ​ n ​ ( x, 0), \displaystyle=\epsilon_{1}f_{\lambda}(x,0)=\epsilon_{1}x^{2n}\zeta_{2n}(x,0), |  |

 | ϵ ˙ 1 \displaystyle\dot{\epsilon}_{1} | = x ​ ϵ 1, \displaystyle=x\epsilon_{1}, |  |

or as a first order system for ϵ 1 ≠ 0 \epsilon_{1}\neq 0

(3.7) |  | d ​ x d ​ ϵ 1 \displaystyle\frac{dx}{d\epsilon_{1}} | = x 2 ​ n − 1 ​ ζ 2 ​ n ​ ( x, 0), \displaystyle={x^{2n-1}\zeta_{2n}(x,0)}, |  |

which extends smoothly to ϵ 1 = 0 \epsilon_{1}=0. Let x out, 1 = x out, 1 ​ ( x in b, ϵ 1) x_{\text{out},1}=x_{\text{out},1}(x_{\text{in}}^{b},\epsilon_{1}), ϵ 1 > 0 \epsilon_{1}>0, denote the unique solution to ( 3.7) with the initial condition x out, 1 ​ ( x in b, 0) = x in b x_{\text{out},1}(x_{\text{in}}^{b},0)=x_{\text{in}}^{b}, where x in b > 0 x_{\text{in}}^{b}>0 is defined in Section 2.2. From ( 2.6) and ( 3.7) it follows that x out, 1 x_{\text{out},1} is a decreasing function in ϵ 1 \epsilon_{1}. By the separation of variables, x out, 1 x_{\text{out},1} is implicitly defined by

(3.8) |  | ϵ 1 = ∫ x in b x out, 1 1 s 2 ​ n − 1 ​ ζ 2 ​ n ​ ( s, 0) ​ 𝑑 s. \displaystyle\epsilon_{1}=\int_{x_{\text{in}}^{b}}^{x_{\text{out},1}}\frac{1}{s^{2n-1}\zeta_{2n}(s,0)}ds. |  |

We now define the following sections:

 | Σ in, 1 \displaystyle\Sigma_{\text{in},1}\, | : x ∈ I in, ρ 1 = δ 1, ϵ 1 ∈ [0, ν), \displaystyle:\quad x\in I_{\text{in}},\,\rho_{1}=\delta_{1},\,\epsilon_{1}\in[0,\nu), |  |

 | Σ out, 1 \displaystyle\Sigma_{\text{out},1}\, | : x ∈ I out, 1, ρ 1 ∈ [0, ν), ϵ 1 = δ 1, \displaystyle:\quad x\in I_{\text{out},1},\,\rho_{1}\in[0,\nu),\,\epsilon_{1}=\delta_{1}, |  |

where I in I_{\text{in}} is defined in Section 2.2, I out, 1 I_{\text{out},1} is an appropriate interval, δ 1 = − 1 / log δ \delta_{1}=-1/\log\delta, with δ ∈ ( 0, 1) \delta\in(0,1) small and fixed in Section 2.2, and ν > 0 \nu>0 is small enough. Notice that y = δ y=\delta corresponds to ρ 1 = δ 1 \rho_{1}=\delta_{1}, due to ( 3.1).

###### Lemma 3.1.

Fix any k ∈ ℕ k\in\mathbb{N}. Then the transition map

 | Σ in, 1 \displaystyle\Sigma_{\textnormal{in},1} | → Σ out, 1, \displaystyle\rightarrow\Sigma_{\textnormal{out},1}, |  |

 | ( x in, δ 1, ϵ 1) \displaystyle(x_{\text{in}},\delta_{1},\epsilon_{1}) | ↦ ( x + ​ ( x in, ϵ 1), ϵ 1, δ 1), \displaystyle\mapsto(x_{+}(x_{\text{in}},\epsilon_{1}),\epsilon_{1},\delta_{1}), |  |

given by the forward flow of ( 3.6), is well-defined for all ϵ 1 ∈] 0, ϵ 0 [\epsilon_{1}\in]0,\epsilon_{0}[with ϵ 0 > 0 \epsilon_{0}>0 small enough. In particular, x + x_{+} takes the following form:

 | x + ​ ( x in, ϵ 1) = x out, 1 ​ ( x in b ​ ( x in), δ 1) + o ⁡ ( 1), \displaystyle x_{+}(x_{\text{in}},\epsilon_{1})=x_{\textnormal{out},1}(x_{\text{in}}^{b}(x_{\text{in}}),\delta_{1})+o(1), |  |

where o ⁡ ( 1) o(1) is C k C^{k} -smooth w.r.t. ( x in, ϵ 1, ϵ 1 ​ log ⁡ ϵ 1) (x_{\text{in}},\epsilon_{1},\epsilon_{1}\log\epsilon_{1}) and is zero for all x in ∈ I in x_{\text{in}}\in I_{\text{in}} when ϵ 1 = 0 \epsilon_{1}=0.

###### Proof.

Since we deal with the passage near the line of saddle singularities with positive and negative eigenvalues of equal magnitude, this result follows from [6]. ∎

### 3.2. Chart ϵ ¯ = 1 \bar{\epsilon}=1

In this chart, we obtain the desingularized vector field defined by

(3.9) |  | x ˙ \displaystyle\dot{x} | = f λ ( x, ρ 2) + ρ 2 − 1 e − 1 / ( ρ 2 z 2) g ( x, e − 1 / ( ρ 2 z 2), ρ 2), \displaystyle=f_{\lambda}(x,\rho_{2})+\rho_{2}^{-1}{\mathrm{e}}^{-1/(\rho_{2}z_{2})}g(x,{\mathrm{e}}^{-1/(\rho_{2}z_{2})},\rho_{2}), |  |

 | z ˙ 2 \displaystyle\dot{z}_{2} | = − x ​ z 2 2, \displaystyle=-xz_{2}^{2}, |  |

 | ρ ˙ 2 \displaystyle\dot{\rho}_{2} | = 0. \displaystyle=0. |  |

The invariant behavior on the plane z 2 = 0 z_{2}=0 is given by

 | x ˙ \displaystyle\dot{x} | = f λ ​ ( x, ρ 2), \displaystyle=f_{\lambda}(x,\rho_{2}), |  |

 | ρ ˙ 2 \displaystyle\dot{\rho}_{2} | = 0. \displaystyle=0. |  |

The solutions are horizontal lines in the ( x, ρ 2) (x,\rho_{2}) -plane and f λ ​ ( x, ρ 2) < 0 f_{\lambda}(x,\rho_{2})<0 for x ∈ I x\in I, λ ∈ Λ \lambda\in\Lambda and ρ 2 > 0 \rho_{2}>0 small enough (see Lemma 2.2).

Notice that within ρ 2 = 0 \rho_{2}=0 we have

 | − z 2 − 2 ​ d ​ z 2 d ​ x = 1 x 2 ​ n − 1 ​ ζ 2 ​ n ​ ( x, 0), \displaystyle-z_{2}^{-2}\frac{dz_{2}}{dx}=\frac{1}{x^{2n-1}\zeta_{2n}(x,0)}, |  |

for z 2 ≠ 0 z_{2}\neq 0. Here we have used f λ ​ ( x, 0) = x 2 ​ n ​ ζ 2 ​ n ​ ( x, 0) f_{\lambda}(x,0)=x^{2n}\zeta_{2n}(x,0). We can solve this equation for z 2 = z 2 ​ ( x) z_{2}=z_{2}(x):

 | z 2 ​ ( x) = 1 z 2 ​ ( x 0) − 1 + ∫ x 0 x 1 s 2 ​ n − 1 ​ ζ 2 ​ n ​ ( s, 0) ​ 𝑑 s, \displaystyle z_{2}(x)=\frac{1}{z_{2}(x_{0})^{-1}+\int_{x_{0}}^{x}\frac{1}{s^{2n-1}\zeta_{2n}(s,0)}ds}, |  |

using an initial condition at x = x 0 x=x_{0}. The specific solution

(3.10) |  | z 2 ​ ( x) = 1 ∫ x in b x 1 s 2 ​ n − 1 ​ ζ 2 ​ n ​ ( s, 0) ​ 𝑑 s, \displaystyle z_{2}(x)=\frac{1}{\int_{x_{\text{in}}^{b}}^{x}\frac{1}{s^{2n-1}\zeta_{2n}(s,0)}ds}, |  |

corresponds to ( 3.8) (cf. ( 3.5)) with z 2 ​ ( x) → ∞ z_{2}(x)\rightarrow\infty as x → ( x in b) − x\rightarrow(x_{\text{in}}^{b})^{-}. Notice also that z 2 ​ ( x) z_{2}(x) in ( 3.10) tends to 0 as x → 0 + x\to 0^{+}. In fact, one can easily show (using ζ 2 ​ n ​ ( 0, 0) = − 1 \zeta_{2n}(0,0)=-1) that lim x → 0 + z 2 ​ ( x) ​ log ⁡ x − 1 = 1 \lim_{x\to 0^{+}}z_{2}(x)\log x^{-1}=1 for n = 1 n=1 whereas lim x → 0 + z 2 ​ ( x) ​ x − 2 ​ ( n − 1) = 2 ​ ( n − 1) \lim_{x\to 0^{+}}z_{2}(x)x^{-2(n-1)}=2(n-1) for n ≥ 2 n\geq 2, see Fig. 4. (This is the first indication that n = 1 n=1 and n ≥ 2 n\geq 2 are different.)

Figure 4. Sketch of ( 3.10) for n = 1 n=1 (red) and n ≥ 2 n\geq 2 (blue).

The point ( 0, 0, 0) (0,0,0) is a degenerate singularity of ( 3.9), the linearization having only zero eigenvalues. We therefore introduce a spherical blow-up for any n ≥ 2 n\geq 2:

(3.11) |  | r ≥ 0, ( x ¯, z ¯ 2, ρ ¯ 2) ∈ 𝕊 2 ↦ { x = r ​ x ¯, z 2 = r 2 ​ ( n − 1) ​ z ¯ 2, ρ 2 = r ​ ρ ¯ 2, \displaystyle r\geq 0,\,(\bar{x},\bar{z}_{2},\bar{\rho}_{2})\in\mathbb{S}^{2}\mapsto\begin{cases}x&=r\bar{x},\\ z_{2}&=r^{2(n-1)}\bar{z}_{2},\\ \rho_{2}&=r\bar{\rho}_{2},\end{cases} |  |

and use a desingularization corresponding to division of the right hand side by r 2 ​ n − 1 r^{2n-1}, see Fig. 5.

For n = 1 n=1, we use a cylindrical blow-up:

(3.12) |  | r ≥ 0, ( x ¯, ρ ¯ 2) ∈ 𝕊 1 ↦ { x = r ​ x ¯, ρ 2 = r ​ ρ ¯ 2, \displaystyle r\geq 0,\,(\bar{x},\bar{\rho}_{2})\in\mathbb{S}^{1}\mapsto\begin{cases}x&=r\bar{x},\\ \rho_{2}&=r\bar{\rho}_{2},\end{cases} |  |

leaving z 2 z_{2} fixed, and a desingularization corresponding to division of the right hand side by r r.

Figure 5. Illustration of the spherical blow-up ( 3.11) for n ≥ 2 n\geq 2.

We consider two separate charts for any n ∈ ℕ n\in\mathbb{N}: x ¯ = 1 \bar{x}=1 and ρ ¯ 2 = 1 \bar{\rho}_{2}=1 with chart-specific coordinates ( r 1, z 21, ρ 21) (r_{1},z_{21},\rho_{21}) and ( x 2, z 22, r 2) (x_{2},z_{22},r_{2}), respectively, defined by

 | x ¯ = 1: { x = r 1, z 2 = r 1 2 ​ ( n − 1) ​ z 21, ρ 2 = r 1 ​ ρ 21, \displaystyle\bar{x}=1:\quad\begin{cases}x&=r_{1},\\ z_{2}&=r_{1}^{2(n-1)}z_{21},\\ \rho_{2}&=r_{1}\rho_{21},\end{cases} |  |

 | ρ ¯ 2 = 1: { x = r 2 ​ x 2, z 2 = r 2 2 ​ ( n − 1) ​ z 22, ρ 2 = r 2. \displaystyle\bar{\rho}_{2}=1:\quad\begin{cases}x&=r_{2}x_{2},\\ z_{2}&=r_{2}^{2(n-1)}z_{22},\\ \rho_{2}&=r_{2}.\end{cases} |  |

In each chart, the desingularization is achieved through division of the right hand side by r i 2 ​ n − 1 r_{i}^{2n-1}, i = 1, 2 i=1,2. Notice that for n = 1 n=1, z 2 = z 21 = z 22 z_{2}=z_{21}=z_{22} is fixed. The change of coordinates between x ¯ = 1 \bar{x}=1 and ρ ¯ 2 = 1 \bar{\rho}_{2}=1 is well-defined for x 2 > 0 x_{2}>0 and given by the expressions:

(3.13) |  | { r 1 = r 2 ​ x 2, z 21 = z 22 ​ x 2 − 2 ​ ( n − 1), ρ 21 = x 2 − 1. \displaystyle\begin{cases}r_{1}&=r_{2}x_{2},\\ z_{21}&=z_{22}x_{2}^{-2(n-1)},\\ \rho_{21}&=x_{2}^{-1}.\end{cases} |  |

We divide the analysis into n = 1 n=1 (Section 4) and n ≥ 2 n\geq 2 (Section 5).

## 4. Proof of Theorem 2.4

In this section, we prove Theorem 2.4. We therefore consider the system ( 3.2), with n = 1 n=1 and P λ ​ ( x 2) = λ 0 + λ 1 ​ x 2 − x 2 2 P_{\lambda}(x_{2})=\lambda_{0}+\lambda_{1}x_{2}-x_{2}^{2}, and assume that ( 2.6) and ( 2.7) are satisfied.

Using ( 2.3) and ( 3.9), the desingularization of ( 3.2) in the chart ϵ ¯ = 1 \bar{\epsilon}=1 yields

 | x ˙ \displaystyle\dot{x} | = ρ 2 2 P λ ( ρ 2 − 1 x) + x 2 ( ζ 2 ( x, ρ 2) + 1) + ρ 2 − 1 e − 1 / ( ρ 2 z 2) g ( x, e − 1 / ( ρ 2 z 2), ρ 2), \displaystyle=\rho_{2}^{2}P_{\lambda}(\rho_{2}^{-1}x)+x^{2}(\zeta_{2}(x,\rho_{2})+1)+\rho_{2}^{-1}{\mathrm{e}}^{-1/(\rho_{2}z_{2})}g(x,{\mathrm{e}}^{-1/(\rho_{2}z_{2})},\rho_{2}), |  |

 | z ˙ 2 \displaystyle\dot{z}_{2} | = − x ​ z 2 2, \displaystyle=-xz_{2}^{2}, |  |

 | ρ ˙ 2 \displaystyle\dot{\rho}_{2} | = 0. \displaystyle=0. |  |

We apply now the blow-up ( 3.12), working in the charts x ¯ = 1 \bar{x}=1 and ρ ¯ 2 = 1 \bar{\rho}_{2}=1. Recall that z 2 z_{2} is not transformed under ( 3.12) for n = 1 n=1 and in this situation it is in fact more useful to define y 2 y_{2} by

(4.1) |  | y 2 = e − 1 / z 2. \displaystyle y_{2}={\mathrm{e}}^{-1/z_{2}}. |  |

###### Remark 4.1.

Notice that ( 4.1) corresponds to y 2 = y ϵ y_{2}=y^{\epsilon} (by ( 3.4) and ( 3.1)). Moreover, since z 2 ​ ( x) ​ log ⁡ x − 1 → 1 z_{2}(x)\log x^{-1}\to 1 as x → 0 + x\to 0^{+} in ( 3.10) for n = 1 n=1 and ϵ = 0 \epsilon=0, we have y 2 ​ ( x) ​ x − 1 → 1 y_{2}(x)x^{-1}\to 1 as x → 0 + x\to 0^{+} for ϵ = 0 \epsilon=0 in terms of y 2 y_{2}.

One of the reasons why we use y 2 y_{2} instead of z 2 z_{2} is that in the chart x ¯ = 1 \bar{x}=1, we then deal with passage near a hyperbolic saddle at ( r 1, y 2, ρ 21) = ( 0, 0, 0) (r_{1},y_{2},\rho_{21})=(0,0,0) (see system ( 4.3)) and use normal forms from [11, 17]. Working with the original variable z 2 z_{2}, one would have a semi-hyperbolic singularity at ( r 1, z 2, ρ 21) = ( 0, 0, 0) (r_{1},z_{2},\rho_{21})=(0,0,0) with eigenvalues of the linearization − 1, 0, 1 -1,0,1. We have not found suitable normal forms to deal with this semi-hyperbolic case.

This gives

(4.2) |  | x ˙ \displaystyle\dot{x} | = ρ 2 2 ​ P λ ​ ( ρ 2 − 1 ​ x) + x 2 ​ ( ζ 2 ​ ( x, ρ 2) + 1) + ρ 2 − 1 ​ y 2 1 / ρ 2 ​ g ​ ( x, y 2 1 / ρ 2, ρ 2), \displaystyle=\rho_{2}^{2}P_{\lambda}(\rho_{2}^{-1}x)+x^{2}(\zeta_{2}(x,\rho_{2})+1)+\rho_{2}^{-1}y_{2}^{1/\rho_{2}}g(x,y_{2}^{1/\rho_{2}},\rho_{2}), |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = − x ​ y 2, \displaystyle=-xy_{2}, |  |

 | ρ ˙ 2 \displaystyle\dot{\rho}_{2} | = 0, \displaystyle=0, |  |

In the chart ϵ ¯ = 1 \bar{\epsilon}=1, we consider z 2 ∈ [0, μ] z_{2}\in[0,\mu], with μ > 0 \mu>0, and therefore work with y 2 ∈ [0, e − 1 / μ] ⊂ [0, 1) y_{2}\in[0,{\mathrm{e}}^{-1/\mu}]\subset[0,1).

### 4.1. The chart x ¯ = 1 \bar{x}=1

In this chart, we use x = r 1, ρ 2 = r 1 ​ ρ 21 x=r_{1},\rho_{2}=r_{1}\rho_{21} and obtain the desingularized vector-field defined by

(4.3) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1 ​ F 21 ​ ( r 1, y 2, ρ 21), \displaystyle=-r_{1}F_{21}(r_{1},y_{2},\rho_{21}), |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = − y 2, \displaystyle=-y_{2}, |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21 ​ F 21 ​ ( r 1, z 21, ρ 21), \displaystyle=\rho_{21}F_{21}(r_{1},z_{21},\rho_{21}), |  |

where

 | F 21 ​ ( r 1, y 2, ρ 21) = − Q λ ​ ( ρ 21) − ζ 2 ​ ( r 1, r 1 ​ ρ 21) − 1 + G 21 ​ ( r 1, r 1 − 3 ​ ρ 21 − 1 ​ y 2 1 / ( r 1 ​ ρ 21), ρ 21), \displaystyle F_{21}(r_{1},y_{2},\rho_{21})=-Q_{\lambda}(\rho_{21})-\zeta_{2}(r_{1},r_{1}\rho_{21})-1+G_{21}(r_{1},r_{1}^{-{\color[rgb]{0,0,0}{3}}}\rho_{21}^{-1}y_{2}^{1/(r_{1}\rho_{21})},\rho_{21}), |  |

with

(4.4) |  | Q λ ​ ( ρ 21):= ρ 21 2 ​ P λ ​ ( ρ 21 − 1), \displaystyle Q_{\lambda}(\rho_{21}):=\rho_{21}^{2}P_{\lambda}(\rho_{21}^{-1}), |  |

and

 | G 21 ​ ( r 1, q, ρ 21):= − q ​ g ​ ( r 1, r 1 3 ​ ρ 21 ​ q, r 1 ​ ρ 21). \displaystyle G_{21}(r_{1},q,\rho_{21}):={\color[rgb]{0,0,0}{-}}qg(r_{1},r_{1}^{{\color[rgb]{0,0,0}{3}}}\rho_{21}q,r_{1}\rho_{21}). |  |

Notice that F 21 ​ ( 0, y 2, 0) = 1 F_{21}(0,y_{2},0)=1 and ( r 1, y 2, ρ 21) = ( 0, 0, 0) (r_{1},y_{2},\rho_{21})=(0,0,0) is a hyperbolic saddle for ( 4.3).

In the following we fix N ∈ ℕ N\in\mathbb{N} large enough. Then by working in a sufficiently small neighborhood of ( r 1, y 2, ρ 21) = ( 0, 0, 0) (r_{1},y_{2},\rho_{21})=(0,0,0), we may assume that F 21 ∈ C N F_{21}\in C^{N}. We divide the right hand side of ( 4.3) by F 21 F_{21} to obtain the equivalent system

(4.5) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = − y 2 F 21 ​ ( r 1, y 2, ρ 21), \displaystyle=-\frac{y_{2}}{F_{21}(r_{1},y_{2},\rho_{21})}, |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21, \displaystyle=\rho_{21}, |  |

in a small neighborhood of the origin, which we now proceed to normalize. Since we are interested in an explicit entry-exit relation, we will need detailed information about the normal form transformations. Our strategy is therefore based upon first considering partial linearizations within the two invariant planes r 1 = 0 r_{1}=0 and ρ 21 = 0 \rho_{21}=0. Within the former, we find

 | y ˙ 2 \displaystyle\dot{y}_{2} | = y 2 Q λ ​ ( ρ 21), \displaystyle=\frac{y_{2}}{Q_{\lambda}(\rho_{21})}, |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

We see that ( y 2, ρ 21) = ( 0, 0) (y_{2},\rho_{21})=(0,0) is a (resonant) hyperbolic saddle, with eigenvalues − 1 -1 and 1 1. There are no resonant terms and the system can be linearized explicitly by ( Y, ρ 21) ↦ ( y 2, ρ 21) (Y,\rho_{21})\mapsto(y_{2},\rho_{21}) defined by

 | y 2 \displaystyle y_{2} | = e ∫ 0 ρ 21 Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s ​ Y, \displaystyle={\mathrm{e}}^{\int_{0}^{\rho_{21}}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds}Y, |  |

so that Y ˙ = − Y \dot{Y}=-Y. This follows from a simple calculation. Notice that the integral is well-defined since Q λ ​ ( 0) = − 1 Q_{\lambda}(0)=-1.

Now, within ρ 21 = 0 \rho_{21}=0 we find

 | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = y 2 ζ 2 ​ ( r 1, 0). \displaystyle=\frac{y_{2}}{\zeta_{2}(r_{1},0)}. |  |

We see that ( r 1, y 2) = ( 0, 0) (r_{1},y_{2})=(0,0) is a (resonant) hyperbolic node, with eigenvalues − 1 -1 and − 1 -1. However, there are no resonant terms and the system can be linearized explicitly by ( r 1, Y) ↦ ( r 1, y 2) (r_{1},Y)\mapsto(r_{1},y_{2}) defined by

 | y 2 \displaystyle y_{2} | = e − ∫ 0 r 1 ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) d s Y, \displaystyle={\mathrm{e}}^{-\int_{0}^{r_{1}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds}Y, |  |

so that Y ˙ = − Y \dot{Y}=-Y. This follows from a simple calculation. Notice that the integral is again well-defined since ζ 2 ​ ( 0, 0) = − 1 \zeta_{2}(0,0)=-1.

Before we combine these transformations, notice that

 | − 1 F 21 = 1 Q λ ​ ( ρ 21) + 1 ζ 2 ​ ( r 1, 0) + 1 + r 1 ​ ρ 21 ​ R 0 ​ ( r 1, ρ 21) + R 1 ​ ( r 1, y 2, ρ 21), \displaystyle-\frac{1}{F_{21}}=\frac{1}{Q_{\lambda}(\rho_{21})}+\frac{1}{\zeta_{2}(r_{1},0)}+1+r_{1}\rho_{21}R_{0}(r_{1},\rho_{21})+R_{1}(r_{1},y_{2},\rho_{21}), |  |

where R 0 R_{0} is C ∞ C^{\infty} -smooth and R 1 R_{1} is C N C^{N} -flat w.r.t. r 1 ​ ρ 21 r_{1}\rho_{21}. Then the C ∞ C^{\infty} diffeomorphism ( r 1, Y, ρ 21) ↦ ( r 1, y 2, ρ 21) (r_{1},Y,\rho_{21})\mapsto(r_{1},y_{2},\rho_{21}) defined by

(4.6) |  | y 2 \displaystyle y_{2} | = Θ ⁡ ( r 1, Y, ρ 21):= e ∫ 0 ρ 21 Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s − ∫ 0 r 1 ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s ​ Y, \displaystyle=\Theta(r_{1},Y,\rho_{21}):={\mathrm{e}}^{\int_{0}^{\rho_{21}}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds-\int_{0}^{r_{1}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds}Y, |  |

brings ( 4.5) into the following system

(4.7) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | Y ˙ \displaystyle\dot{Y} | = Y ⁡ ( − 1 + r 1 ​ ρ 21 ​ R 0 ​ ( r 1, ρ 21) + R 1 ​ ( r 1, Θ ⁡ ( r 1, Y, ρ 21), ρ 21)), \displaystyle=Y\left(-1+r_{1}\rho_{21}R_{0}(r_{1},\rho_{21})+R_{1}(r_{1},\Theta(r_{1},Y,\rho_{21}),\rho_{21})\right), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

We can then apply normal form theory (see e.g. [17, Proposition 4.6]) to simplify ( 4.7) further.

###### Lemma 4.2.

Fix any k ∈ ℕ k\in\mathbb{N}. Then there exists a C k C^{k} -diffeomorphism ( r 1, Y ^, ρ 21) ↦ ( r 1, Y, ρ 21) (r_{1},\widehat{Y},\rho_{21})\mapsto(r_{1},Y,\rho_{21}) defined by

(4.8) |  | Y = Y ^ ​ ( 1 + 𝒪 ⁡ ( r 1 ​ ρ 21)) \displaystyle Y=\widehat{Y}(1+\mathcal{O}(r_{1}\rho_{21})) |  |

that brings ( 4.7), locally in a sufficiently small neighborhood of ( r 1, Y, ρ 21) = ( 0, 0, 0) (r_{1},Y,\rho_{21})=(0,0,0), into the normal form

(4.9) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | Y ^ ˙ \displaystyle\dot{\widehat{Y}} | = − Y ^ ​ ( 1 + α 0 ​ ( r 1 ​ ρ 21)), \displaystyle=-\widehat{Y}(1+\alpha_{0}(r_{1}\rho_{21})), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

Here α 0 \alpha_{0} is C k C^{k} -smooth and satisfies α 0 ​ ( 0) = 0 \alpha_{0}(0)=0.

###### Proof.

The result follows from [17, Proposition 4.6] (see also [11]). Notice in particular in comparison with [17, Proposition 4.6] that α i = 0 \alpha_{i}=0 for all i ∈ { 1, …, N ⁡ ( k) } i\in\{1,\ldots,N(k)\} (using the notation of [17]) since these resonant terms are absent in ( 4.7). ∎

We now define the following sections:

 | Σ in, 21 \displaystyle\Sigma_{\text{in},21}\, | : y 2 ∈ [0, μ ~], r 1 = δ, ρ 21 ∈ [0, ν), \displaystyle:\quad y_{2}\in[0,\tilde{\mu}],\,r_{1}=\delta,\,\rho_{21}\in[0,\nu), |  |

 | Σ out, 21 \displaystyle\Sigma_{\text{out},21}\, | : y 2 ∈ [0, e − 1 / μ], r 1 ∈ [0, ν), ρ 21 = δ, \displaystyle:\quad y_{2}\in[0,{\mathrm{e}}^{-1/\mu}],\,r_{1}\in[0,\nu),\,\rho_{21}=\delta, |  |

where μ ~, ν > 0 \tilde{\mu},\nu>0 are small enough and δ > 0 \delta>0 is introduced in Section 2.2 (we can shrink δ \delta if necessary). We have the following.

###### Lemma 4.3.

Fix any k ∈ ℕ k\in\mathbb{N} and δ > 0 \delta>0 small enough. Then the transition map

 | Σ in, 21 \displaystyle\Sigma_{\textnormal{in},21} | → Σ out, 21, \displaystyle\rightarrow\Sigma_{\textnormal{out},21}, |  |

 | ( δ, y 2, ρ 21) \displaystyle(\delta,y_{2},\rho_{21}) | ↦ ( ρ 21, y 2 + ​ ( y 2, ρ 21), δ), \displaystyle\mapsto(\rho_{21},y_{2+}({\color[rgb]{0,0,0}{y_{2}}},\rho_{21}),\delta), |  |

given by the forward flow of ( 4.5), is well-defined for all ρ 21 ∈ [0, ρ 210) \rho_{21}\in[0,\rho_{210}) with ρ 210 > 0 \rho_{210}>0 small enough. In particular, y 2 + y_{2+} takes the following from:

 | y 2 + ​ ( y 2, ρ 21) = ρ 21 δ ​ e ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s + ∫ 0 δ ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s ​ y 2 ​ ( 1 + o ⁡ ( 1)) \displaystyle y_{2+}(y_{2},\rho_{21})=\frac{\rho_{21}}{\delta}{\mathrm{e}}^{\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds+\int_{0}^{\delta}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds}y_{2}(1+{\color[rgb]{0,0,0}{o(1)}}) |  |

where o ⁡ ( 1) {\color[rgb]{0,0,0}{o(1)}} is C k C^{k} -smooth w.r.t. ( y 2, ρ 21, ρ 21 ​ log ⁡ ρ 21 − 1) (y_{2},\rho_{21},\rho_{21}\log\rho_{21}^{-1}) and zero for all y 2 ∈ [0, μ ~] y_{2}\in[0,\tilde{\mu}] when ρ 21 = 0 \rho_{21}=0.

###### Proof.

We simply integrate the normal form ( 4.9) and use the changes of coordinates ( 4.6) and ( 4.8). ∎

###### Remark 4.4.

We are now in a position to describe the mapping ( x in, δ) ↦ ( r 1, y 2 + ​ ( x in, ϵ), δ) (x_{\text{in}},\delta)\mapsto(r_{1},y_{2+}(x_{\text{in}},\epsilon),\delta) (with r 1 = ϵ ​ δ − 1 r_{1}=\epsilon\delta^{-1}) from Σ in \Sigma_{\text{in}} to Σ out, 21 \Sigma_{\text{out},21}, with Σ in \Sigma_{\text{in}} defined in Section 2.2. Indeed, upon using Lemma 3.1, ( 3.10), the change of coordinates y 2 = e − 1 / z 2 y_{2}={\mathrm{e}}^{-1/z_{2}} and Lemma 4.3 we find that

 | y 2 + = ρ 21 δ ​ e ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s + ∫ 0 δ ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + ∫ δ x in b 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s ​ ( 1 + o ⁡ ( 1)), \displaystyle y_{2+}=\frac{\rho_{21}}{\delta}{\mathrm{e}}^{\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds+\int_{0}^{\delta}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds+\int_{\delta}^{x_{\text{in}}^{b}}\frac{1}{s\zeta_{2}(s,0)}ds}(1+o(1)), |  |

where o ⁡ ( 1) o(1) is C k C^{k} -smooth w.r.t. ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1) (x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}) and is identically zero when ϵ = 0 \epsilon=0. We can simplify this further by writing

 | 1 s ​ ζ 2 ​ ( s, 0) = ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) − 1 s, \displaystyle\frac{1}{s\zeta_{2}(s,0)}=\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}-\frac{1}{s}, |  |

and by noticing that ρ 21 \rho_{21} here is the value of ρ 21 \rho_{21} at the section Σ in, 21 \Sigma_{\text{in},21}. Therefore ρ 21 = ϵ ​ δ − 1 \rho_{21}=\epsilon\delta^{-1} since r 1 = δ r_{1}=\delta there. This gives

 | y 2 + \displaystyle y_{2+} | = ϵ δ 2 ​ e ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s − ∫ δ x in b s − 1 ​ 𝑑 s ​ ( 1 + o ⁡ ( 1)) \displaystyle=\frac{\epsilon}{\delta^{2}}{\mathrm{e}}^{\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\int_{\delta}^{x_{\text{in}}^{b}}s^{-1}ds}(1+o(1)) |  |

 |  | = ϵ δ 2 ​ e ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + log ⁡ δ x in b ​ ( 1 + o ⁡ ( 1)) \displaystyle=\frac{\epsilon}{\delta^{2}}{\mathrm{e}}^{\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds+\log\frac{\delta}{x_{\text{in}}^{b}}}(1+o(1)) |  |

 |  | = ϵ δ ​ e ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s − log ⁡ x in b ​ ( 1 + o ⁡ ( 1)), \displaystyle=\frac{\epsilon}{\delta}{\mathrm{e}}^{\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log x_{\text{in}}^{b}}(1+o(1)), |  |

where o ⁡ ( 1) o(1) has the same property as above.

### 4.2. Chart ρ ¯ 2 = 1 \bar{\rho}_{2}=1

Consider again the system ( 4.2). In this chart, we use x = r 2 ​ x 2, ρ 2 = r 2 x=r_{2}x_{2},\rho_{2}=r_{2} (see Section 3.2) and obtain the desingularized vector-field defined by

(4.10) |  | x ˙ 2 \displaystyle\dot{x}_{2} | = P λ ​ ( x 2) + x 2 2 ​ ( ζ 2 ​ ( r 2 ​ x 2, r 2) + 1) + r 2 − 3 ​ y 2 1 / r 2 ​ g ​ ( r 2 ​ x 2, y 2 1 / r 2, r 2), \displaystyle=P_{\lambda}(x_{2})+x_{2}^{2}(\zeta_{2}(r_{2}x_{2},r_{2})+1)+{\color[rgb]{0,0,0}{r_{2}^{-3}}}y_{2}^{1/r_{2}}g(r_{2}x_{2},y_{2}^{1/r_{2}},r_{2}), |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = − x 2 ​ y 2, \displaystyle=-x_{2}y_{2}, |  |

and r ˙ 2 = 0 \dot{r}_{2}=0. We consider x 2 ∈ [− δ − 1, δ − 1] x_{2}\in[-\delta^{-1},\delta^{-1}], y 2 ∈ [0, e − 1 / μ] ⊂ [0, 1) y_{2}\in[0,{\mathrm{e}}^{-1/\mu}]\subset[0,1) and 0 ≤ r 2 ≪ 1 0\leq r_{2}\ll 1. On this compact set, ( 4.10) is regular (we use ( 2.7) and ζ 2 ​ ( 0, 0) = − 1 \zeta_{2}(0,0)=-1) with y 2 = 0 y_{2}=0 being an invariant set. Within r 2 = 0 r_{2}=0, we therefore find

 | d ​ y 2 d ​ x 2 = − x 2 ​ y 2 P λ ​ ( x 2), \displaystyle\frac{dy_{2}}{dx_{2}}=-\frac{x_{2}y_{2}}{P_{\lambda}(x_{2})}, |  |

with the solution:

(4.11) |  | y 2 ( x 2) = e − ∫ x 20 x 2 s P λ ​ ( s) d s y 2 ( x 20), \displaystyle y_{2}(x_{2})={\mathrm{e}}^{-\int_{x_{20}}^{x_{2}}\frac{s}{P_{\lambda}(s)}ds}y_{2}(x_{20}), |  |

using an initial condition at x 2 = x 20 x_{2}=x_{20}.

We now define the following transverse sections: Σ in, 22: x 2 = δ − 1, y 2 ∈ [0, e − 1 / μ] \Sigma_{\text{in},22}\,:\,x_{2}=\delta^{-1},y_{2}\in[0,{\mathrm{e}}^{-1/\mu}] and Σ final, 22: x 2 = 0, y 2 ∈ [0, e − 1 / μ] \Sigma_{\text{final},22}\,:\,x_{2}=0,y_{2}\in[0,{\mathrm{e}}^{-1/\mu}] for all 0 ≤ r 2 ≪ 1 0\leq r_{2}\ll 1. We then have the following

###### Lemma 4.5.

The transition map Σ in, 22 → Σ final, 22 \Sigma_{\text{in},22}\rightarrow\Sigma_{\text{final},22}, ( δ − 1, y 2) ↦ ( 0, y 2 + ​ ( y 2, r 2)) (\delta^{-1},y_{2})\mapsto(0,y_{2+}(y_{2},r_{2})) associated with ( 4.10) is well-defined for all 0 ≤ r 2 ≪ 1 0\leq r_{2}\ll 1. In particular,

 | y 2 + ​ ( y 2, r 2) = e ∫ 0 δ − 1 s P λ ​ ( s) ​ 𝑑 s ​ y 2 ​ ( 1 + 𝒪 ⁡ ( r 2)), \displaystyle y_{2+}(y_{2},r_{2})={\mathrm{e}}^{\int_{0}^{\delta^{-1}}\frac{s}{P_{\lambda}(s)}ds}y_{2}(1+\mathcal{O}(r_{2})), |  |

where 𝒪 ⁡ ( r 2) \mathcal{O}(r_{2}) is C ∞ C^{\infty} -smooth w.r.t. ( y 2, r 2) (y_{2},r_{2}) and equals zero for r 2 = 0 r_{2}=0.

###### Proof.

We use ( 4.11), regular perturbation theory and the invariance of y 2 = 0 y_{2}=0. ∎

Notice that x 2 = δ − 1 x_{2}=\delta^{-1} corresponds to ρ 21 = δ \rho_{21}=\delta (see ( 3.13)). Finally, we get the following.

###### Proposition 4.6.

The transition map ( x in, δ) ↦ ( 0, y 2 + ​ ( x in, ϵ)) (x_{\text{in}},\delta)\mapsto(0,y_{2+}(x_{\text{in}},\epsilon)) from the original section Σ in: x ∈ I in, y = δ \Sigma_{\text{in}}\,:x\in I_{\text{in}},\,y=\delta to the section Σ final, 22 \Sigma_{\text{final},22} is well-defined for all 0 < ϵ ≪ 1 0<\epsilon\ll 1. In particular,

(4.12) |  | y 2 + = ϵ ​ exp ⁡ ( CLOSE \displaystyle y_{2+}=\epsilon\exp\bigg( | ∫ 0 1 s P λ ​ ( s) ​ 𝑑 s + ∫ 1 ∞ P λ ​ ( s) + s 2 s ​ P λ ​ ( s) ​ 𝑑 s + ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s \displaystyle{\displaystyle\int_{0}^{1}\frac{s}{P_{\lambda}(s)}ds+\int_{1}^{\infty}\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds}+\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds |  |

 |  | OPEN − log ⁡ x in b + ϕ in ​ ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1)), \displaystyle-\log x_{\text{in}}^{b}+\phi_{\text{in}}(x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1})\bigg), |  |

with ϕ in: I in × [0, ϵ 0) × [0, ϵ 0 ​ log ⁡ ϵ 0 − 1) → ℝ \phi_{\text{in}}:I_{\text{in}}\times[0,\epsilon_{0})\times[0,\epsilon_{0}\log\epsilon_{0}^{-1})\rightarrow\mathbb{R} being C k C^{k} -smooth and satisfying ϕ in ​ ( x in, 0, 0) = 0 \phi_{\text{in}}(x_{\text{in}},0,0)=0.

###### Proof.

By combining Lemma 4.5 and Remark 4.4 we find that

 | y 2 + = ϵ δ ​ e ∫ 0 δ − 1 s P λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s − log ⁡ x in b ​ ( 1 + o ⁡ ( 1)), \displaystyle y_{2+}=\frac{\epsilon}{\delta}{\mathrm{e}}^{\int_{0}^{\delta^{-1}}\frac{s}{P_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log x_{\text{in}}^{b}}(1+{\color[rgb]{0,0,0}{o(1)}}), |  |

where o ⁡ ( 1) o(1) is C k C^{k} -smooth w.r.t. ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1) (x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}) and equal to zero when ϵ = 0 \epsilon=0. Recall that r 2 = ρ 2 = ϵ r_{2}=\rho_{2}=\epsilon. We now use ( 4.4) and rewrite

 | ∫ 0 δ Q λ ​ ( s) + 1 s ​ Q λ ​ ( s) ​ 𝑑 s = ∫ δ − 1 ∞ v − 1 ​ P λ ​ ( v) + v P λ ​ ( v) ​ 𝑑 v, \displaystyle\int_{0}^{\delta}\frac{Q_{\lambda}(s)+1}{sQ_{\lambda}(s)}ds=\int_{\delta^{-1}}^{\infty}\frac{v^{-1}P_{\lambda}(v)+v}{P_{\lambda}(v)}dv, |  |

upon using the substitution s = v − 1 s=v^{-1}. In combination with

 | s P λ ​ ( s) = s − 1 ​ P λ ​ ( s) + s P λ ​ ( s) − s − 1, \displaystyle\frac{s}{P_{\lambda}(s)}=\frac{s^{-1}P_{\lambda}(s)+s}{P_{\lambda}(s)}-s^{-1}, |  |

this leads to

 | y 2 + \displaystyle y_{2+} | = ϵ δ ​ e ∫ 0 δ − 1 s P λ ​ ( s) ​ 𝑑 s + ∫ δ − 1 ∞ s − 1 ​ P λ ​ ( s) + s P λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s − log ⁡ x in b ​ ( 1 + o ⁡ ( 1)) \displaystyle=\frac{\epsilon}{\delta}{\mathrm{e}}^{\int_{0}^{\delta^{-1}}\frac{s}{P_{\lambda}(s)}ds+\int_{\delta^{-1}}^{\infty}\frac{s^{-1}P_{\lambda}(s)+s}{P_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log x_{\text{in}}^{b}}(1+{\color[rgb]{0,0,0}{o(1)}}) |  |

 |  | = ϵ ​ e ∫ 0 1 s P λ ​ ( s) ​ 𝑑 s + ∫ 1 ∞ P λ ​ ( s) + s 2 s ​ P λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s − log ⁡ x in b ​ ( 1 + o ⁡ ( 1)). \displaystyle=\epsilon{\mathrm{e}}^{\int_{0}^{1}\frac{s}{P_{\lambda}(s)}ds+\int_{1}^{\infty}\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log x_{\text{in}}^{b}}(1+{\color[rgb]{0,0,0}{o(1)}}). |  |

Each of the integrals are convergent since P λ ​ ( s) + s 2 = λ 0 + s ​ λ 1 P_{\lambda}(s)+s^{2}=\lambda_{0}+s\lambda_{1}, cf. ( 2.4). By writing 1 + o ⁡ ( 1) = e ϕ in ​ ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1) 1+{\color[rgb]{0,0,0}{o(1)}}={\mathrm{e}}^{\phi_{\text{in}}(x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1})} the result follows. ∎

We now consider the map ( x out, δ) ↦ ( 0, y 2 −) (x_{\text{out}},\delta)\mapsto(0,y_{2-}) from Σ out \Sigma_{\text{out}} to Σ final, 22 \Sigma_{\text{final},22} defined by the backward flow. For this we replace x x by − x -x and t t by − t -t. This gives ( 2.5) with P λ ​ ( x) P_{\lambda}(x) and ζ 2 ​ ( x, ϵ) \zeta_{2}(x,\epsilon) in ( 2.3) replaced by P λ ​ ( − x) P_{\lambda}(-x) and ζ 2 ​ ( − x, ϵ) \zeta_{2}(-x,\epsilon), respectively. We then obtain the following expression for y 2 − y_{2-} by using ( 4.12) :

 | y 2 − \displaystyle y_{2-} | = ϵ ​ e ∫ 0 1 s P λ ​ ( − s) ​ 𝑑 s + ∫ 1 ∞ P λ ​ ( − s) + s 2 s ​ P λ ​ ( − s) ​ 𝑑 s ​ e ∫ 0 − x out b ζ 2 ​ ( − s, 0) + 1 s ​ ζ 2 ​ ( − s, 0) ​ 𝑑 s − log ⁡ ( − x out b) ​ e ϕ out ​ ( x out, ϵ, ϵ ​ log ⁡ ϵ − 1) \displaystyle=\epsilon{\mathrm{e}}^{\int_{0}^{1}\frac{s}{P_{\lambda}(-s)}ds+\int_{1}^{\infty}\frac{P_{\lambda}(-s)+s^{2}}{sP_{\lambda}(-s)}ds}{\mathrm{e}}^{\int_{0}^{-x_{\text{out}}^{b}}\frac{\zeta_{2}(-s,0)+1}{s\zeta_{2}(-s,0)}ds-\log(-x_{\text{out}}^{b})}{\mathrm{e}}^{\phi_{\text{out}}(x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1})} |  |

 |  | = ϵ ​ e ∫ 0 − 1 s P λ ​ ( s) ​ 𝑑 s + ∫ − 1 − ∞ P λ ​ ( s) + s 2 s ​ P λ ​ ( s) ​ 𝑑 s ​ e ∫ 0 x out b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s − log ⁡ ( − x out b) ​ e ϕ out ​ ( x out, ϵ, ϵ ​ log ⁡ ϵ − 1), \displaystyle=\epsilon{\mathrm{e}}^{\int_{0}^{-1}\frac{s}{P_{\lambda}(s)}ds+\int_{-1}^{-\infty}\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds}{\mathrm{e}}^{\int_{0}^{x_{\text{out}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log(-x_{\text{out}}^{b})}{\mathrm{e}}^{\phi_{\text{out}}(x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1})}, |  |

for some new ϕ out \phi_{\text{out}} with ϕ out ​ ( x out, 0, 0) = 0 \phi_{\text{out}}(x_{\text{out}},0,0)=0, upon using the substitution s = − v s=-v in the second equality. Here x out b = x out b ​ ( x out) < 0 x_{\text{out}}^{b}=x_{\text{out}}^{b}(x_{\text{out}})<0 and x out ∈ I out x_{\text{out}}\in I_{\text{out}}.

To solve the entry-exit problem we consider y 2 + = y 2 − y_{2+}=y_{2-} as an equation for ( x in, x out, ϵ) (x_{\text{in}},x_{\text{out}},\epsilon). This gives the following equation

 |  | ∫ 0 1 s P λ ​ ( s) ​ 𝑑 s + ∫ 1 ∞ P λ ​ ( s) + s 2 s ​ P λ ​ ( s) ​ 𝑑 s \displaystyle{\int_{0}^{1}\frac{s}{P_{\lambda}(s)}ds+\int_{1}^{\infty}\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds} |  |

 |  | + ∫ 0 x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) d s − log x in b + ϕ in ( x in, ϵ, ϵ log ϵ − 1) \displaystyle\qquad\qquad\qquad+\int_{0}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log x_{\text{in}}^{b}+\phi_{\text{in}}(x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}) |  |

 |  | = ∫ 0 − 1 s P λ ​ ( s) ​ 𝑑 s + ∫ − 1 − ∞ P λ ​ ( s) + s 2 s ​ P λ ​ ( s) ​ 𝑑 s \displaystyle={\int_{0}^{-1}\frac{s}{P_{\lambda}(s)}ds+\int_{-1}^{-\infty}\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds} |  |

 |  | + ∫ 0 x out b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) d s − log ( − x out b) + ϕ out ( x out, ϵ, ϵ log ϵ − 1), \displaystyle\qquad\qquad\qquad+\int_{0}^{x_{\text{out}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds-\log(-x_{\text{out}}^{b})+\phi_{\text{out}}(x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1}), |  |

or simply

(4.13) |  | ∫ − 1 1 s P λ ​ ( s) ​ 𝑑 s \displaystyle\int_{-1}^{1}\frac{s}{P_{\lambda}(s)}ds | + ( ∫ − ∞ − 1 + ∫ 1 ∞) P λ ​ ( s) + s 2 s ​ P λ ​ ( s) d s \displaystyle+{\color[rgb]{0,0,0}{\left(\int_{-\infty}^{-1}+\int_{1}^{\infty}\right)\frac{P_{\lambda}(s)+s^{2}}{sP_{\lambda}(s)}ds}} |  |

 |  | + ∫ x out b x in b ζ 2 ​ ( s, 0) + 1 s ​ ζ 2 ​ ( s, 0) d s + log ( − x out b x in b) = ϕ ( x in, x out, ϵ, ϵ log ϵ − 1), \displaystyle+\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{\zeta_{2}(s,0)+1}{s\zeta_{2}(s,0)}ds+\log\left(-\frac{x_{\text{out}}^{b}}{x_{\text{in}}^{b}}\right)=\phi(x_{\text{in}},x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1}), |  |

setting ϕ ⁡ ( x in, x out, ϵ, ϵ ​ log ​ ϵ − 1):= ϕ out ​ ( x out, ϵ, ϵ ​ log ​ ϵ − 1) − ϕ in ​ ( x in, ϵ, ϵ ​ log ​ ϵ − 1) \phi(x_{\text{in}},x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1}):=\phi_{\text{out}}(x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1})-\phi_{\text{in}}(x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}).

Using Remark 2.5, it is clear that when ϵ → 0 \epsilon\rightarrow 0 ( 4.13) reduces to the entry-exit formula ( 2.12) (which we write again)

 | p.v. ​ ∫ x out b x in b 1 s ​ ζ 2 ​ ( s, 0) ​ 𝑑 s + p.v. ​ ∫ − ∞ + ∞ s P λ ​ ( s) ​ 𝑑 s = 0. \text{p.v.}\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{1}{s\zeta_{2}(s,0)}ds+\text{p.v.}\int_{-\infty}^{+\infty}\frac{s}{P_{\lambda}(s)}ds=0. |  |

Assume that for every x in ∈ I in x_{\text{in}}\in I_{\text{in}} there exists x out ∈ I out x_{\text{out}}\in I_{\text{out}} such that ( 2.12) is satisfied. From x out b ​ ( x out) < 0 x_{\text{out}}^{b}(x_{\text{out}})<0, ( x out b) ′ ​ ( x out) > 0 (x_{\text{out}}^{b})^{\prime}(x_{\text{out}})>0 and the assumption ( 2.6) for n = 1 n=1 it follows that the partial derivative of the left-hand side in ( 2.12) w.r.t. x out x_{\text{out}} is negative. Now, the implicit function theorem and ( 4.13) imply Theorem 2.4.

###### Remark 4.7.

Let us explain the meaning of the Cauchy principal value defined by ( 2.11).

When r 2 = 0 r_{2}=0, the system ( 4.10) becomes

(4.14) |  | x ˙ 2 \displaystyle\dot{x}_{2} | = P λ ​ ( x 2), \displaystyle=P_{\lambda}(x_{2}), |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = − x 2 ​ y 2. \displaystyle=-x_{2}y_{2}. |  |

Recall that P λ P_{\lambda} is negative (see ( 2.7)). The divergence integral of ( 4.14) along the regular orbit y 2 = 0 y_{2}=0 between x 2 = ρ x_{2}=\rho and x 2 = − ρ x_{2}=-\rho, with ρ > 0 \rho>0, is given by

 | ∫ ρ − ρ P λ ′ ​ ( x 2) − x 2 P λ ​ ( x 2) ​ d ​ x 2 = log ⁡ ( P λ ​ ( − ρ) P λ ​ ( ρ)) + ∫ − ρ ρ x 2 P λ ​ ( x 2) ​ d ​ x 2. \displaystyle\int_{\rho}^{-\rho}\frac{P_{\lambda}^{\prime}(x_{2})-x_{2}}{P_{\lambda}(x_{2})}dx_{2}=\log\left(\frac{P_{\lambda}(-\rho)}{P_{\lambda}(\rho)}\right)+\int_{-\rho}^{\rho}\frac{x_{2}}{P_{\lambda}(x_{2})}dx_{2}. |  |

Notice that the divergence of the vector field ( 4.14) is P λ ′ ​ ( x 2) − x 2 P_{\lambda}^{\prime}(x_{2})-x_{2} and d ​ t = d ​ x 2 P λ ​ ( x 2) dt=\frac{dx_{2}}{P_{\lambda}(x_{2})}. Since P λ P_{\lambda} is a quadratic polynomial, the logarithmic term tends to 0 0 as ρ → ∞ \rho\to\infty. We conclude that

 | lim ρ → ∞ ∫ ρ − ρ P λ ′ ​ ( x 2) − x 2 P λ ​ ( x 2) ​ d ​ x 2 = p.v. ​ ∫ − ∞ + ∞ x 2 P λ ​ ( x 2) ​ d ​ x 2. \lim_{\rho\to\infty}\int_{\rho}^{-\rho}\frac{P_{\lambda}^{\prime}(x_{2})-x_{2}}{P_{\lambda}(x_{2})}dx_{2}=\text{p.v.}\int_{-\infty}^{+\infty}\frac{x_{2}}{P_{\lambda}(x_{2})}dx_{2}. |  |

## 5. Proof of Theorem 2.7

In this section, we proof Theorem 2.7. We consider the system ( 3.2), with n ≥ 2 n\geq 2, and assume that ( 2.6) and ( 2.7) are satisfied.

In the chart ϵ ¯ = 1 \bar{\epsilon}=1, we obtain ( 3.9) repeated here for convenience (see also ( 2.3)):

(5.1) |  | x ˙ \displaystyle\dot{x} | = ρ 2 2 ​ n P λ ( ρ 2 − 1 x) + x 2 ​ n ( ζ 2 ​ n ( x, ρ 2) + 1) + ρ 2 − 1 e − 1 / ( ρ 2 z 2) g ( x, e − 1 / ( ρ 2 z 2), ρ 2), \displaystyle=\rho_{2}^{2n}P_{\lambda}(\rho_{2}^{-1}x)+x^{2n}(\zeta_{2n}(x,\rho_{2})+1)+\rho_{2}^{-1}{\mathrm{e}}^{-1/(\rho_{2}z_{2})}g(x,{\mathrm{e}}^{-1/(\rho_{2}z_{2})},\rho_{2}), |  |

 | z ˙ 2 \displaystyle\dot{z}_{2} | = − x ​ z 2 2, \displaystyle=-xz_{2}^{2}, |  |

 | ρ ˙ 2 \displaystyle\dot{\rho}_{2} | = 0, \displaystyle=0, |  |

and apply the blow-up ( 3.11), working in the charts x ¯ = 1 \bar{x}=1 and ρ ¯ 2 = 1 \bar{\rho}_{2}=1.

### 5.1. Chart x ¯ = 1 \bar{x}=1

In this chart, we use x = r 1, z 2 = r 1 2 ​ ( n − 1) ​ z 21, ρ 2 = r 1 ​ ρ 21 x=r_{1},z_{2}=r_{1}^{2(n-1)}z_{21},\rho_{2}=r_{1}\rho_{21} and obtain the desingularized vector-field defined by

 | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1 ​ F 21 ​ ( r 1, z 21, ρ 21), \displaystyle=-r_{1}F_{21}(r_{1},z_{21},\rho_{21}), |  |

 | z ˙ 21 \displaystyle\dot{z}_{21} | = z 21 ​ F 21 ​ ( r 1, z 21, ρ 21) ​ ( 2 ​ ( n − 1) − z 21 F 21 ​ ( r 1, z 21, ρ 21)), \displaystyle=z_{21}F_{21}(r_{1},z_{21},\rho_{21})\left(2(n-1)-\frac{z_{21}}{F_{21}(r_{1},z_{21},\rho_{21})}\right), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21 ​ F 21 ​ ( r 1, z 21, ρ 21), \displaystyle=\rho_{21}F_{21}(r_{1},z_{21},\rho_{21}), |  |

after division of the right hand side by r 1 2 ​ n − 1 r_{1}^{2n-1}, where

 | F 21 ​ ( r 1, z 21, ρ 21) = − Q λ ​ ( ρ 21) − ζ 2 ​ n ​ ( r 1, r 1 ​ ρ 21) − 1 + r 1 2 ​ n − 3 ​ ρ 21 ​ z 21 2 ​ G 21 ​ ( r 1, r 1 2 ​ n − 1 ​ ρ 21 ​ z 21, r 1 ​ ρ 21), \displaystyle F_{21}(r_{1},z_{21},\rho_{21})=-Q_{\lambda}(\rho_{21})-\zeta_{2n}(r_{1},r_{1}\rho_{21})-1+r_{1}^{2n-3}\rho_{21}z_{21}^{2}G_{21}(r_{1},r_{1}^{2n-1}\rho_{21}z_{21},r_{1}\rho_{21}), |  |

with

 | Q λ ​ ( ρ 21): \displaystyle Q_{\lambda}(\rho_{21}): | = ρ 21 2 ​ n ​ P λ ​ ( ρ 21 − 1) = ρ 21 2 ​ n ​ λ 0 + ⋯ + ρ 21 ​ λ 2 ​ n − 1 − 1 \displaystyle=\rho_{21}^{2n}P_{\lambda}(\rho_{21}^{-1})=\rho_{21}^{2n}\lambda_{0}+{\color[rgb]{0,0,0}{\cdots+}}\rho_{21}\lambda_{2n-1}-1 |  |

and

 | G 21 ( x, z, ϵ):= − z − 2 e − 1 / z g ( x, e − 1 / z, ϵ). \displaystyle G_{21}(x,z,\epsilon):=-z^{-2}{\mathrm{e}}^{-1/z}g(x,{\mathrm{e}}^{-1/z},\epsilon). |  |

In particular, G 21 G_{21} is C ∞ C^{\infty} -flat w.r.t. the second argument.

Since Q λ ​ ( 0) = − 1 Q_{\lambda}(0)=-1 and ζ 2 ​ n ​ ( 0, 0) = − 1 \zeta_{2n}(0,0)=-1, it follows that F 21 ​ ( 0, z 21, 0) = 1 {\color[rgb]{0,0,0}{F_{21}}}(0,z_{21},0)=1 for all z 21 z_{21}. We therefore divide the right hand side by F 21 F_{21} to obtain the equivalent system:

(5.2) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | z ˙ 21 \displaystyle\dot{z}_{21} | = z 21 ​ ( 2 ​ ( n − 1) − z 21 F 21 ​ ( r 1, z 21, ρ 21)), \displaystyle=z_{21}\left(2(n-1)-\frac{z_{21}}{F_{21}(r_{1},z_{21},\rho_{21})}\right), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21, \displaystyle=\rho_{21}, |  |

for z 21 ≥ 0 z_{21}\geq 0 in a large compact set and for all ( r 1, ρ 21) (r_{1},\rho_{21}) sufficiently small. System ( 5.2) has a hyperbolic saddle at ( r 1, z 21, ρ 21) = ( 0, 2 ​ ( n − 1), 0) (r_{1},z_{21},\rho_{21})=(0,2(n-1),0), where the linearization has eigenvalues − 1, − 2 ​ ( n − 1), 1 -1,-2(n-1),1, and a hyperbolic saddle at ( r 1, z 21, ρ 21) = ( 0, 0, 0) (r_{1},z_{21},\rho_{21})=(0,0,0), where the eigenvalues of the linear part are given by − 1, 2 ​ ( n − 1), 1 -1,2(n-1),1. We refer to Fig. 5.

###### Remark 5.1.

Using the change of coordinates x = r 1, z 2 = r 1 2 ​ ( n − 1) ​ z 21 x=r_{1},z_{2}=r_{1}^{2(n-1)}z_{21}, it can be easily seen that z 2 ​ ( x) z_{2}(x) in ( 3.10) tends to the hyperbolic saddle at ( r 1, z 21, ρ 21) = ( 0, 2 ​ ( n − 1), 0) (r_{1},z_{21},\rho_{21})=(0,2(n-1),0) as x = r 1 → 0 + x=r_{1}\to 0^{+}, recall the discussion below ( 3.10). Notice also that I in ⊂ ( 0, ∞) I_{\text{in}}\subset(0,\infty) is kept in a compact interval. This implies that the passage near the hyperbolic saddle at ( r 1, z 21, ρ 21) = ( 0, 0, 0) (r_{1},z_{21},\rho_{21})=(0,0,0) and the passage near the end point of the line of singularities x = 0 x=0 of ( 5.1) with ρ 2 = 0 \rho_{2}=0 on the blow up locus, visible in the chart z ¯ 2 = 1 \bar{z}_{2}=1 of ( 3.11), are not relevant for the proof of Theorem 2.7. We refer to Fig. 5.

We now seek to normalize ( 5.2). We focus on the passage near the hyperbolic saddle at ( r 1, z 21, ρ 21) = ( 0, 2 ​ ( n − 1), 0) (r_{1},z_{21},\rho_{21})=(0,2(n-1),0). Our strategy will again be based upon partial linearizations within the two invariant planes r 1 = 0 r_{1}=0 and ρ 21 = 0 \rho_{21}=0.

First, we use that

 | − 1 F 21 \displaystyle-\frac{1}{F_{21}} | = 1 Q λ ​ ( ρ 21) + 1 ζ 2 ​ n ​ ( r 1, 0) + 1 \displaystyle=\frac{1}{Q_{\lambda}(\rho_{21})}+\frac{1}{\zeta_{2n}(r_{1},0)}+1 |  |

(5.3) |  |  | − r 1 ​ ρ 21 ​ R 0 ​ ( r 1, ρ 21) − R 1 ​ ( r 1, z 21, r 1 2 ​ n − 1 ​ ρ 21 ​ z 21, ρ 21), \displaystyle-r_{1}\rho_{21}R_{0}(r_{1},\rho_{21})-R_{1}(r_{1},z_{21},r_{1}^{2n-1}\rho_{21}z_{21},\rho_{21}), |  |

with R 0 R_{0} and R 1 R_{1} C ∞ C^{\infty} -smooth. This follows from a simple calculation combined with a Taylor expansion (see also Section 4). In particular, R 1 R_{1} is C ∞ C^{\infty} -flat w.r.t. its third argument. We then consider a change of coordinates ( r 1, Z, ρ 21) ↦ ( r 1, z 21, ρ 21) (r_{1},Z,\rho_{21})\mapsto(r_{1},z_{21},\rho_{21}) defined by

 | z 21 = Θ ⁡ ( r 1, Z, ρ 21):= 1 Z + L ⁡ ( r 1, ρ 21), L ⁡ ( 0, 0) = 1 2 ​ ( n − 1), \displaystyle z_{21}{\color[rgb]{0,0,0}{=\Theta(r_{1},Z,\rho_{21}):}}=\frac{1}{Z+L(r_{1},\rho_{21})},\quad L(0,0)=\frac{1}{2(n-1)}, |  |

with L ∈ C 1 L\in C^{1}. Notice that ( r 1, z 21, ρ 21) = ( 0, 2 ​ ( n − 1), 0) (r_{1},z_{21},\rho_{21})=(0,2(n-1),0) corresponds to ( r 1, Z, ρ 21) = ( 0, 0, 0) (r_{1},Z,\rho_{21})=(0,0,0). Then the z 21 z_{21} -component of ( 5.2) changes into

 | Z ˙ \displaystyle\dot{Z} | = − 2 ​ ( n − 1) ​ Z + R 1 ​ ( r 1, Θ ⁡ ( r 1, Z, ρ 21), r 1 2 ​ n − 1 ​ ρ 21 ​ Θ ​ ( r 1, Z, ρ 21), ρ 21) \displaystyle=-2(n-1)Z+R_{1}(r_{1},\Theta(r_{1},Z,\rho_{21}),r_{1}^{{\color[rgb]{0,0,0}{2n-1}}}\rho_{21}\Theta(r_{1},Z,\rho_{21}),\rho_{21}) |  |

 |  | + { − L ˙ − 2 ​ ( n − 1) ​ L − 1 Q λ ​ ( ρ 21) − 1 ζ 2 ​ n ​ ( r 1, 0) − 1 + r 1 ​ ρ 21 ​ R 0 ​ ( r 1, ρ 21) }, \displaystyle+\left\{-\dot{L}-2(n-1)L-\frac{1}{Q_{\lambda}(\rho_{21})}-\frac{1}{\zeta_{2n}(r_{1},0)}-1+r_{1}\rho_{21}R_{0}(r_{1},\rho_{21})\right\}, |  |

where L ˙ = − ∂ L ∂ r 1 ​ r 1 + ∂ L ∂ ρ 21 ​ ρ 21 \dot{L}=-\frac{\partial L}{\partial r_{1}}r_{1}+{\color[rgb]{0,0,0}{\frac{\partial L}{\partial\rho_{21}}}}\rho_{21}. We will select L L so that the curly bracket is zero and therefore look for an invariant manifold L ∈ C 1 L\in C^{1}, L ⁡ ( 0, 0) = 1 2 ​ ( n − 1) L(0,0)=\frac{1}{2(n-1)}, of the following first order system

(5.4) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | L ˙ \displaystyle\dot{L} | = − 2 ​ ( n − 1) ​ L − 1 Q λ ​ ( ρ 21) − 1 ζ 2 ​ n ​ ( r 1, 0) − 1 + r 1 ​ ρ 21 ​ R 0 ​ ( r 1, ρ 21), \displaystyle=-2(n-1)L-\frac{1}{Q_{\lambda}(\rho_{21})}-\frac{1}{\zeta_{2n}(r_{1},0)}-1+r_{1}\rho_{21}R_{0}(r_{1},\rho_{21}), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

We first consider the invariant subspaces r 1 = 0 r_{1}=0 and ρ 21 = 0 \rho_{21}=0. For r 1 = 0 r_{1}=0, we set J ⁡ ( ρ 21) = L ⁡ ( 0, ρ 21) J(\rho_{21})=L(0,\rho_{21}) and find

(5.5) |  | J ˙ \displaystyle\dot{J} | = − 2 ​ ( n − 1) ​ J − 1 Q λ ​ ( ρ 21), \displaystyle=-2(n-1)J-\frac{1}{Q_{\lambda}(\rho_{21})}, |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

Since Q λ ​ ( 0) = − 1 Q_{\lambda}(0)=-1, ( J, ρ 21) = ( 1 2 ​ ( n − 1), 0) (J,\rho_{21})=(\frac{1}{2(n-1)},0) is a hyperbolic saddle of ( 5.5), the linearization having eigenvalues − 2 ​ ( n − 1), 1 -2(n-1),1, and there exists a unique local unstable manifold given as the C ∞ C^{\infty} graph:

(5.6) |  | J ( ρ 21) = − ρ 21 − 2 ​ ( n − 1) ∫ 0 ρ 21 v 2 ​ n − 3 Q λ ​ ( v) d v = − ∫ 0 1 v 2 ​ n − 3 Q λ ​ ( ρ 21 ​ v) d v, ρ 21 ≥ 0. \displaystyle J(\rho_{21})=-\rho_{21}^{-2(n-1)}\int_{0}^{\rho_{21}}\frac{v^{2n-3}}{Q_{\lambda}(v)}dv=-\int_{0}^{1}\frac{v^{2n-3}}{Q_{\lambda}(\rho_{21}v)}dv,\quad\rho_{21}\geq 0. |  |

This is a simple calculation. Notice that 2 ​ n − 3 ≥ 1 2n-3\geq 1 for n ≥ 2 n\geq 2 and J ⁡ ( 0) = 1 2 ​ ( n − 1) J(0)=\frac{1}{2(n-1)}.

Next, we consider ρ 21 = 0 \rho_{21}=0 and set K ⁡ ( r 1) = L ⁡ ( r 1, 0) K(r_{1})=L(r_{1},0). Then we find that

(5.7) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | K ˙ \displaystyle\dot{K} | = − 2 ​ ( n − 1) ​ K − 1 ζ 2 ​ n ​ ( r 1, 0), \displaystyle=-2(n-1)K-\frac{1}{\zeta_{2n}(r_{1},0)}, |  |

Since ζ 2 ​ n ​ ( 0, 0) = − 1 \zeta_{2n}(0,0)=-1, we conclude that ( r 1, K) = ( 0, 1 2 ​ ( n − 1)) (r_{1},K)=(0,\frac{1}{2(n-1)}) is a hyperbolic stable node of ( 5.7) with the linearization having eigenvalues − 1 -1 and − 2 ​ ( n − 1) -2(n-1). Therefore there is no smooth invariant manifold solution K = K ⁡ ( r 1) K=K(r_{1}) in general, but we will fix δ > 0 \delta>0 and consider

(5.8) |  | K ⁡ ( r 1) = r 1 2 ​ ( n − 1) ​ ∫ δ r 1 v 1 − 2 ​ n ζ 2 ​ n ​ ( v, 0) ​ 𝑑 v. \displaystyle K(r_{1})=r_{1}^{2(n-1)}\int_{\delta}^{r_{1}}\frac{v^{1-2n}}{\zeta_{2n}(v,0)}dv. |  |

It is a simple calculation to show that this defines an invariant manifold solution of ( 5.7). Moreover, we have the following:

###### Lemma 5.2.

The function K K given by ( 5.8) is C ∞ C^{\infty} -smooth w.r.t. ( r 1, r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1) (r_{1},r_{1}^{2(n-1)}\log r_{1}^{-1}) and equals 1 2 ​ ( n − 1) \frac{1}{2(n-1)} for r 1 = 0 r_{1}=0.

###### Proof.

We expand the smooth function ζ 2 ​ n ​ ( r 1, 0) − 1 \zeta_{2n}(r_{1},0)^{-1} as follows

 | ζ 2 ​ n ​ ( r 1, 0) − 1 =: − 1 + ∑ k = 1 2 ​ n − 3 a k ​ r 1 k + a 2 ​ ( n − 1) ​ r 1 2 ​ ( n − 1) + r 1 2 ​ n − 1 ​ E ​ ( r 1), \displaystyle\zeta_{2n}(r_{1},0)^{-1}=:-1+\sum_{k=1}^{2n-3}a_{k}r_{1}^{k}+{a_{2(n-1)}}r_{1}^{2(n-1)}+r_{1}^{2{n}-1}E(r_{1}), |  |

with E ∈ C ∞ E\in C^{\infty}. Then we have

 | K ⁡ ( r 1) \displaystyle K(r_{1}) | = 1 2 ​ ( n − 1) − r 1 2 ​ ( n − 1) ​ δ 2 ​ ( 1 − n) 2 ​ ( n − 1) + ∑ k = 1 2 ​ n − 3 a k ​ r 1 k − r 1 2 ​ ( n − 1) ​ δ 2 ​ ( 1 − n) + k 2 ​ ( 1 − n) + k \displaystyle=\frac{1}{2(n-1)}-\frac{r_{1}^{2(n-1)}\delta^{2(1-n)}}{2(n-1)}+\sum_{k=1}^{2n-3}a_{k}\frac{r_{1}^{k}-r_{1}^{2(n-1)}\delta^{2(1-n)+k}}{{\color[rgb]{0,0,0}{2(1-n)+k}}} |  |

 |  | + a 2 ​ ( n − 1) ​ r 1 2 ​ ( n − 1) ​ log ⁡ r 1 δ + r 1 2 ​ ( n − 1) ​ ∫ δ r 1 E ⁡ ( v) ​ 𝑑 v. \displaystyle+{a_{2(n-1)}}r_{1}^{2(n-1)}\log\frac{r_{1}}{\delta}+{\color[rgb]{0,0,0}{r_{1}^{2(n-1)}}}\int_{\delta}^{r_{1}}E(v)dv. |  |

This completes the proof. ∎

###### Remark 5.3.

By slight abuse of notation, we will write K K given by ( 5.8) as

 | K ⁡ ( r 1, r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1), K(r_{1},r_{1}^{2(n-1)}\log r_{1}^{-1}), |  |

where K K denotes a C ∞ C^{\infty} -smooth function.

We now write L L in the following form:

 | L ⁡ ( r 1, ρ 21) = J ⁡ ( ρ 21) + K ⁡ ( r 1, r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1) − 1 2 ​ ( n − 1) + L ~ ​ ( r 1, ρ 21), \displaystyle L(r_{1},\rho_{21})=J(\rho_{21})+K(r_{1},r_{1}^{2(n-1)}\log r_{1}^{-1})-\frac{1}{2(n-1)}+\widetilde{L}(r_{1},\rho_{21}), |  |

with J J and K K given above and L ~ ​ ( 0, 0) = 0 \widetilde{L}(0,0)=0. Inserting this into ( 5.4) gives

(5.9) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | L ~ ˙ \displaystyle\dot{\widetilde{L}} | = − 2 ​ ( n − 1) ​ L ~ + r 1 ​ ρ 21 ​ R 0 ​ ( r 1, ρ 21), \displaystyle=-2(n-1)\widetilde{L}+r_{1}\rho_{21}R_{0}(r_{1},\rho_{21}), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

For this system, we use normal form theory, see e.g. [17, Proposition 4.6]: Fix any k ∈ ℕ k\in\mathbb{N}. Then there exists a locally defined C k C^{k} -smooth change of coordinates ( r 1, L ~, ρ 21) ↦ ( r 1, L ^, ρ 21) (r_{1},\widetilde{L},\rho_{21})\mapsto(r_{1},\widehat{L},\rho_{21}), which is 𝒪 ⁡ ( r 1 ​ ρ 21) \mathcal{O}(r_{1}\rho_{21}) -close to the identity, such that ( 5.9) becomes

(5.10) |  | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | L ^ ˙ \displaystyle\dot{\widehat{L}} | = − 2 ​ ( n − 1) ​ L ^ + κ ⁡ ( r 1 ​ ρ 21) ​ r 1 2 ​ ( n − 1), \displaystyle=-2(n-1)\widehat{L}+\kappa(r_{1}\rho_{21})r_{1}^{2(n-1)}, |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21, \displaystyle=\rho_{21}, |  |

with κ \kappa smooth, satisfying κ ⁡ ( 0) = 0 \kappa(0)=0. Notice in particular in comparison with [17, Proposition 4.6] that α i = 0 \alpha_{i}=0 for all i ∈ { 0, …, N ⁡ ( k) } i\in\{0,\ldots,N(k)\} (using the notation of [17]) since these resonant terms are absent in ( 5.9). It is easy to see that

 | L ^ ​ ( r 1, ρ 21) = κ ⁡ ( r 1 ​ ρ 21) ​ r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1, \displaystyle\widehat{L}(r_{1},\rho_{21})={\kappa}(r_{1}\rho_{21})r_{1}^{2(n-1)}\log r_{1}^{-1}, |  |

defines an invariant manifold for ( 5.10). We summarize our findings in the following Lemma.

###### Lemma 5.4.

Fix any k ∈ ℕ k\in\mathbb{N} and let δ > 0 \delta>0 be sufficiently small. Then there exists a C k C^{k} smooth function

 | L ¯: [0, δ) × [0, δ 2 ​ ( n − 1) ​ log ⁡ δ − 1) × [0, δ) → ℝ \overline{L}:[0,\delta)\times[0,\delta^{2(n-1)}\log\delta^{-1})\times[0,\delta)\rightarrow\mathbb{R} |  |

satisfying

 | L ¯ ​ ( r 1, r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1, 0) \displaystyle\overline{L}(r_{1},r_{1}^{2(n-1)}\log r_{1}^{-1},0) | = r 1 2 ​ ( n − 1) ∫ δ r 1 v 1 − 2 ​ n ζ 2 ​ n ​ ( v, 0) d v, L ¯ ( 0, 0, ρ 21) = − ∫ 0 1 v 2 ​ n − 3 Q λ ​ ( ρ 21 ​ v) d v, \displaystyle=r_{1}^{2(n-1)}\int_{\delta}^{r_{1}}\frac{v^{1-2n}}{\zeta_{2n}(v,0)}dv,\quad\overline{L}(0,0,\rho_{21})=-\int_{0}^{1}\frac{v^{2n-3}}{Q_{\lambda}(\rho_{21}v)}dv, |  |

in particular, L ¯ ​ ( 0, 0, 0) = 1 2 ​ ( n − 1) \overline{L}(0,0,0)=\frac{1}{2(n-1)}, so that

(5.11) |  | z 21 = Θ ⁡ ( r 1, Z, ρ 21) = 1 Z + L ¯ ​ ( r 1, r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1, ρ 21), \displaystyle z_{21}{\color[rgb]{0,0,0}{=\Theta(r_{1},Z,\rho_{21})}}=\frac{1}{Z+\overline{L}(r_{1},r_{1}^{2(n-1)}\log r_{1}^{-1},\rho_{21})}, |  |

defines a C 1 C^{1} -smooth change of coordinates that brings ( 5.2) into the (almost linearized) form:

 | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

(5.12) |  | Z ˙ \displaystyle\dot{Z} | = − 2 ​ ( n − 1) ​ Z + R 1 ​ ( r 1, Θ ⁡ ( r 1, Z, ρ 21), r 1 2 ​ n − 1 ​ ρ 21 ​ Θ ​ ( r 1, Z, ρ 21), ρ 21), \displaystyle=-2(n-1)Z+R_{1}(r_{1},\Theta(r_{1},Z,\rho_{21}),r_{1}^{{\color[rgb]{0,0,0}{2n-1}}}\rho_{21}\Theta(r_{1},Z,\rho_{21}),\rho_{21}), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21, \displaystyle=\rho_{21}, |  |

where R 1 R_{1} is C ∞ C^{\infty} -flat w.r.t. the third argument (see ( 5.1)).

In other words, we have obtained a linearization ( 5.11) of ( 5.2), which is C k C^{k} -smooth w.r.t.

 | ( r 1, r 1 2 ​ ( n − 1) ​ log ⁡ r 1 − 1, ρ 21), (r_{1},r_{1}^{2(n-1)}\log r_{1}^{-1},\rho_{21}), |  |

up to C ∞ C^{\infty} -flat terms (in the sense described in the lemma). Fix any l ∈ ℕ l\in\mathbb{N}. Then upon increasing k k, it is subsequently possible to remove R 1 R_{1} in ( 5.4) by a subsequent C l C^{l} -smooth change of coordinates ( r 1, Z ^, ρ 21) ↦ ( r 1, Z, ρ 21) (r_{1},\widehat{Z},\rho_{21})\mapsto(r_{1},Z,\rho_{21}) with

 | Z = Z ^ + ϕ ⁡ ( r 1, Z ^, ρ 21), \displaystyle Z=\widehat{Z}+\phi(r_{1},\widehat{Z},\rho_{21}), |  |

where ϕ ⁡ ( r 1, Z ^, ρ 21) = 𝒪 ⁡ ( ( r 1 ​ ρ 21) l) \phi(r_{1},\widehat{Z},\rho_{21})=\mathcal{O}((r_{1}\rho_{21})^{l}), so that

 | Z ^ ˙ = − 2 ​ ( n − 1) ​ Z ^. \dot{\widehat{Z}}=-2(n-1)\widehat{Z}. |  |

This again follows from normal form theory (due to the absence of resonance terms, see e.g. [17, Proposition 4.6]).

We now define the following sections

 | Σ in, 21 \displaystyle\Sigma_{\text{in},21}\, | : z 21 ∈ I 21, r 1 = δ, ρ 21 ∈ [0, ν), \displaystyle:\quad z_{21}\in I_{21},\,r_{1}=\delta,\,\rho_{21}\in[0,\nu), |  |

 | Σ out, 21 \displaystyle\Sigma_{\text{out},21}\, | : z 21 ∈ I 21, r 1 ∈ [0, ν), ρ 21 = δ, \displaystyle:\quad z_{21}\in I_{21},\,r_{1}\in[0,\nu),\,\rho_{21}=\delta, |  |

with I 21 I_{21} an (appropriate) closed interval that contains 2 ​ ( n − 1) ∈ I 21 2(n-1)\in I_{21}, and where δ, ν > 0 \delta,\nu>0 are small enough. After putting all the information together, we easily get the following.

###### Lemma 5.5.

Fix any k ∈ ℕ k\in\mathbb{N}, k ≫ 2 ​ ( n − 1) k\gg 2(n-1), and δ > 0 \delta>0 small enough. Then the transition map

 | Σ in, 21 \displaystyle\Sigma_{\textnormal{in},21} | → Σ out, 21, \displaystyle\rightarrow\Sigma_{\textnormal{out},21}, |  |

 | ( δ, z 21, ρ 21) \displaystyle(\delta,z_{21},\rho_{21}) | ↦ ( ρ 21, z 21 + ​ ( z 21, ρ 21), δ), \displaystyle\mapsto(\rho_{21},z_{21+}(z_{21},\rho_{21}),\delta), |  |

given by the forward flow of ( 5.2), is well-defined for all ρ 21 ∈ [0, ρ 210) \rho_{21}\in[0,\rho_{210}) with ρ 210 > 0 \rho_{210}>0 small enough. In particular, z 21 + z_{21+} takes the following from:

 | z 21 + ​ ( z 21, ρ 21) = 1 ( ρ 21 δ) 2 ​ ( n − 1) ​ Z ^ 0 + L ¯ ​ ( ρ 21, ρ 21 2 ​ ( n − 1) ​ log ⁡ ρ 21 − 1, δ) + ϕ ⁡ ( ρ 21, ( ρ 21 δ) 2 ​ ( n − 1) ​ Z ^ 0, δ), \displaystyle z_{21+}(z_{21},\rho_{21})=\frac{1}{\left(\frac{\rho_{21}}{\delta}\right)^{2(n-1)}\widehat{Z}_{0}+\overline{L}(\rho_{21},\rho_{21}^{2(n-1)}\log\rho_{21}^{-1},\delta)+\phi(\rho_{21},{\color[rgb]{0,0,0}{\left(\frac{\rho_{21}}{\delta}\right)^{2(n-1)}}}\widehat{Z}_{0},\delta)}, |  |

with ϕ ∈ C k \phi\in C^{k}, ϕ ⁡ ( r 1, Z ^, ρ 21) = 𝒪 ⁡ ( ( r 1 ​ ρ 21) k) \phi(r_{1},\widehat{Z},\rho_{21})=\mathcal{O}((r_{1}\rho_{21})^{k}) uniformly w.r.t. Z ^ \widehat{Z}, and where Z ^ 0 \widehat{Z}_{0} is a C k C^{k} -smooth function of z 21 z_{21} and ρ 21 \rho_{21} defined implicitly by

 | z 21 = 1 Z ^ 0 + L ¯ ​ ( δ, δ 2 ​ ( n − 1) ​ log ⁡ δ − 1, ρ 21) + ϕ ⁡ ( δ, Z ^ 0, ρ 21) \displaystyle z_{21}=\frac{1}{\widehat{Z}_{0}+\overline{L}(\delta,\delta^{2(n-1)}\log\delta^{-1},\rho_{21})+\phi(\delta,\widehat{Z}_{0},\rho_{21})} |  |

### 5.2. The chart ρ ¯ 2 = 1 \bar{\rho}_{2}=1

Consider again the system ( 5.1). In the chart ρ ¯ 2 = 1 \bar{\rho}_{2}=1, we have x = r 2 ​ x 2, z 2 = r 2 2 ​ ( n − 1) ​ z 22, ρ 2 = r 2 x=r_{2}x_{2},z_{2}=r_{2}^{2(n-1)}z_{22},\rho_{2}=r_{2} and obtain the desingularized vector-field defined by

(5.13) |  | x ˙ 2 \displaystyle\dot{x}_{2} | = P λ ​ ( x 2) + x 2 2 ​ n ​ ( ζ 2 ​ n ​ ( r 2 ​ x 2, r 2) + 1) + r 2 2 ​ n − 3 ​ z 22 2 ​ G 22 ​ ( r 2 ​ x 2, r 2 2 ​ n − 1 ​ z 22, r 2), \displaystyle=P_{\lambda}(x_{2})+x_{2}^{2n}\left(\zeta_{2n}(r_{2}x_{2},r_{2})+1\right)+r_{2}^{2n-3}z_{22}^{2}G_{22}(r_{2}x_{2},r_{2}^{2n-1}z_{22},r_{2}), |  |

 | z ˙ 22 \displaystyle\dot{z}_{22} | = − x 2 ​ z 22 2, \displaystyle=-x_{2}z_{22}^{2}, |  |

 | r ˙ 2 \displaystyle\dot{r}_{2} | = 0, \displaystyle=0, |  |

with G 22 ( x, z, ϵ) = z − 2 e − 1 / z g ( x, e − 1 / z, ϵ) G_{22}(x,z,\epsilon)=z^{-2}{\mathrm{e}}^{-1/z}g(x,{\mathrm{e}}^{-1/z},\epsilon), after division of the right hand side by r 2 2 ​ n − 1 r_{2}^{2n-1}. Here G 22 G_{22} is C ∞ C^{\infty} -flat w.r.t. its second argument.

For r 2 = 0 r_{2}=0, we obtain

 | x ˙ 2 \displaystyle\dot{x}_{2} | = P λ ​ ( x 2), \displaystyle=P_{\lambda}(x_{2}), |  |

 | z ˙ 22 \displaystyle\dot{z}_{22} | = − x 2 ​ z 22 2, \displaystyle=-x_{2}z_{22}^{2}, |  |

which by the assumption P λ ​ ( x 2) < 0 P_{\lambda}(x_{2})<0 for all x 2 ∈ ℝ x_{2}\in\mathbb{R}, see ( 2.7), is regular. By eliminating time, we have

 | − 1 z 22 2 ​ d ​ z 22 d ​ x 2 \displaystyle-\frac{1}{z_{22}^{2}}\frac{dz_{22}}{dx_{2}} | = x 2 P λ ​ ( x 2), \displaystyle=\frac{x_{2}}{P_{\lambda}(x_{2})}, |  |

so that

 | z 22 ​ ( x 2) = 1 z 22 ​ ( x 20) − 1 + ∫ x 20 x 2 v P λ ​ ( v) ​ 𝑑 v, \displaystyle z_{22}(x_{2})=\frac{1}{z_{22}(x_{20})^{-1}+\int_{x_{20}}^{x_{2}}\frac{v}{P_{\lambda}(v)}dv}, |  |

using an initial condition at x 2 = x 20 x_{2}=x_{20}.

Within the invariant plane r 1 = 0 r_{1}=0 of ( 5.2), we have the following dynamics:

 | z ˙ 21 \displaystyle\dot{z}_{21} | = z 21 ​ ( 2 ​ ( n − 1) + z 21 Q λ ​ ( ρ 21)), \displaystyle=z_{21}\left(2(n-1)+\frac{z_{21}}{Q_{\lambda}(\rho_{21})}\right), |  |

 | ρ ˙ 21 \displaystyle\dot{\rho}_{21} | = ρ 21. \displaystyle=\rho_{21}. |  |

It is not difficult to see that the (local) unstable manifold of this system at the hyperbolic saddle ( z 21, ρ 21) = ( 2 ​ ( n − 1), 0) (z_{21},\rho_{21})=(2(n-1),0) is the graph of

 | z 21 = J ​ ( ρ 21) − 1, ρ 21 ≥ 0, z_{21}=J(\rho_{21})^{-1},\ \rho_{21}\geq 0, |  |

where J J is defined in ( 5.6). Now, we have the following.

###### Lemma 5.6.

The unstable manifold z 21 = J ​ ( ρ 21) − 1, ρ 21 ≥ 0 z_{21}=J(\rho_{21})^{-1},\rho_{21}\geq 0, from the chart x ¯ = 1 \bar{x}=1 takes the following form

 | z 22 ​ ( x 2) = 1 − ∫ x 2 ∞ v P λ ​ ( v) d v \displaystyle z_{22}(x_{2})=\frac{1}{-\int_{x_{2}}^{\infty}\frac{v}{P_{\lambda}(v)}dv} |  |

in the chart ρ ¯ 2 = 1 \bar{\rho}_{2}=1. It intersects x 2 = 0 x_{2}=0 in the point z 22 = 1 − ∫ 0 ∞ v P λ ​ ( v) d v z_{22}=\frac{1}{-\int_{0}^{\infty}\frac{v}{P_{\lambda}(v)}dv}.

###### Proof.

This follows directly using Q λ ​ ( ρ 21) = ρ 21 2 ​ n ​ P λ ​ ( ρ 21 − 1) Q_{\lambda}(\rho_{21})=\rho_{21}^{2n}P_{\lambda}(\rho_{21}^{-1}), ( 5.6) and the change of coordinates in ( 3.13). ∎

We now define the transverse section Σ final, 22: x 2 = 0, z 22 ∈ [0, μ] \Sigma_{\text{final},22}\,:\,x_{2}=0,z_{22}\in[0,\mu] for μ > 0 \mu>0 fixed and for all 0 ≤ r 2 ≪ 1 0\leq r_{2}\ll 1. We then combine the previous results to obtain the following:

###### Proposition 5.7.

The transition map ( x in, δ) ↦ ( 0, z 22 + ​ ( x in, ϵ)) (x_{\text{in}},\delta)\mapsto(0,z_{22+}(x_{\text{in}},\epsilon)) from the original section Σ in: x ∈ I in, y = δ \Sigma_{\text{in}}\,:x\in I_{\text{in}},\,y=\delta to the section Σ final, 22 \Sigma_{\text{final},22} is well-defined for all 0 ≤ ϵ ≪ 1 0\leq\epsilon\ll 1. In particular,

 | z 22 + = 1 − ∫ 0 ∞ v P λ ​ ( v) d v + o ⁡ ( 1), \displaystyle z_{22+}=\frac{1}{-\int_{0}^{\infty}\frac{v}{P_{\lambda}(v)}dv}+{\color[rgb]{0,0,0}{o(1)}}, |  |

where o ⁡ ( 1) {\color[rgb]{0,0,0}{o(1)}} is C k C^{k} -smooth w.r.t. ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1) (x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}) and is zero for ϵ = 0 \epsilon=0.

###### Proof.

From Lemma 3.1 and Section 3.2 it follows that the z 21 z_{21} -component of the transition map from the original section Σ in \Sigma_{\text{in}} to the section Σ in, 21 \Sigma_{\text{in},21} (defined before Lemma 5.5) is C k C^{k} -smooth w.r.t. ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1) (x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}). This combined with Lemma 5.5 implies that the z 21 z_{21} -component of the transition map from the section Σ in \Sigma_{\text{in}} to the section Σ out, 21 \Sigma_{\text{out},21} is again C k C^{k} -smooth w.r.t. ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1) (x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}) and it is equal to 1 / J ⁡ ( δ) 1/J(\delta) when ϵ = 0 \epsilon=0. Finally, using Lemma 5.6 and the fact that the passage from Σ out, 21 \Sigma_{\text{out},21} to Σ final, 22 \Sigma_{\text{final},22} is regular, we obtain the property of z 22 + z_{22+}. ∎

By replacing x x by − x -x and t t by − t -t, we obtain ( 2.5) with P λ ​ ( x) P_{\lambda}(x) and ζ 2 ​ n ​ ( x, ϵ) \zeta_{2n}(x,\epsilon) in ( 2.3) replaced by P λ ​ ( − x) P_{\lambda}(-x) and ζ 2 ​ n ​ ( − x, ϵ) \zeta_{2n}(-x,\epsilon), respectively. We therefore obtain the following expression for z 22 − z_{22-} in backward time:

 | z 22 − \displaystyle z_{22-} | = 1 − ∫ 0 ∞ v P λ ​ ( − v) d v + o ⁡ ( 1) = 1 − ∫ 0 − ∞ v P λ ​ ( v) d v + o ⁡ ( 1). \displaystyle=\frac{1}{-\int_{0}^{\infty}\frac{v}{P_{\lambda}(-v)}dv}+{\color[rgb]{0,0,0}{o(1)}}=\frac{1}{-\int_{0}^{-\infty}\frac{v}{P_{\lambda}(v)}dv}+{\color[rgb]{0,0,0}{o(1)}}. |  |

Using the expressions for z 22 + z_{22+} and z 22 − z_{22-} and the change of coordinates y = e − 1 ϵ 2 ​ n − 1 ​ z 22 y=e^{-\frac{1}{\epsilon^{2n-1}z_{22}}} (see Section 3), we finally get ( 2.15).

Setting z 22 + = z 22 − z_{22+}=z_{22-} gives

 | ∫ − ∞ ∞ v P λ ​ ( v) ​ 𝑑 v = o ⁡ ( 1), \displaystyle\int_{-\infty}^{\infty}\frac{v}{P_{\lambda}(v)}dv={\color[rgb]{0,0,0}{o(1)}}, |  |

where o ⁡ ( 1) {\color[rgb]{0,0,0}{o(1)}} is C k C^{k} -smooth w.r.t. ( x in, x out, ϵ, ϵ ​ log ⁡ ϵ − 1) (x_{\text{in}},x_{\text{out}},\epsilon,\epsilon\log\epsilon^{-1}) and is zero for ϵ = 0 \epsilon=0. Therefore, if ( 2.14) holds true, then the entry-exit problem I in ∋ x in ↦ Δ ⁡ ( x in, ϵ) ∈ I out I_{\text{in}}\ni x_{\text{in}}\mapsto\Delta(x_{\text{in}},\epsilon)\in I_{\text{out}} is not well-defined for all 0 < ϵ ≪ 1 0<\epsilon\ll 1. This completes the proof of Theorem 2.7.

## 6. Entry-exit problem at infinity in the Dumortier-Roussarie-Rousseau program

In this section, we consider

(6.1) |  | x ˙ \displaystyle\dot{x} | = ϵ ⁡ ( ϵ 2 ​ λ 0 + ϵ ​ λ 1 ​ x + x 2 ​ ζ 2 ​ ( x, ϵ)) + y ⁡ ( − 1 + 𝒪 ⁡ ( ϵ)), \displaystyle=\epsilon\left(\epsilon^{2}\lambda_{0}+\epsilon\lambda_{1}x+x^{2}\zeta_{2}(x,\epsilon)\right)+y\left(-1+\mathcal{O}(\epsilon)\right), |  |

 | y ˙ \displaystyle\dot{y} | = − x ​ y, \displaystyle=-xy, |  |

with ζ 2 ​ ( x, ϵ) = − 1 + β ​ x + ϵ ​ x 2 ​ ζ ~ 2 ​ ( x, ϵ) \zeta_{2}(x,\epsilon)=-1+\beta x+\epsilon x^{2}\widetilde{\zeta}_{2}(x,\epsilon) where β > 0 \beta>0 and ζ ~ 2 \widetilde{\zeta}_{2} is a smooth function. Note that ζ 2 ​ ( x, 0) < 0 \zeta_{2}(x,0)<0 for all x < 1 β x<\frac{1}{\beta}. Clearly, system ( 6.1) is a special case of ( 2.5) with n = 1 n=1 and P λ ​ ( x 2) = λ 0 + λ 1 ​ x 2 − x 2 2 P_{\lambda}(x_{2})=\lambda_{0}+\lambda_{1}x_{2}-x_{2}^{2}. See also ( 2.3) and ( 2.4). We assume that 4 ​ λ 0 + λ 1 2 < 0 4\lambda_{0}+\lambda_{1}^{2}<0 (this implies that P λ P_{\lambda} is negative).

Before we compute the entry-exit function associated with ( 6.1), let us briefly explain the connection between system ( 6.1) and the graphics ( I 2 1) (I_{2}^{1}) and ( I 4 1) (I_{4}^{1}) in the Dumortier-Roussarie-Rousseau program (for more details see [10]).

We define a 5-parameter family of quadratic systems

(6.2) |  | x ˙ \displaystyle\dot{x} | = A ​ x − y + x 2 + ( μ 2 + μ 3) ​ x ​ y + μ 1 ​ y 2, \displaystyle=Ax-y+x^{2}+(\mu_{2}+\mu_{3})xy+\mu_{1}y^{2}, |  |

 | y ˙ \displaystyle\dot{y} | = C ​ x + x 2 + x ​ y + μ 3 ​ y 2, \displaystyle=Cx+x^{2}+xy+\mu_{3}y^{2}, |  |

with A A close to 1 1, C C close to C 0 > 0 C_{0}>0, and μ 1, μ 2, μ 3 \mu_{1},\mu_{2},\mu_{3} kept close to zero. When A = 1 A=1, C = C 0 C=C_{0} and ( μ 1, μ 2, μ 3) = ( 0, 0, 0) (\mu_{1},\mu_{2},\mu_{3})=(0,0,0), the parabola y = 1 2 ​ x 2 − C 0 2 y=\frac{1}{2}x^{2}-\frac{C_{0}}{2} is invariant for system ( 6.2), and ( I 4 1) (I_{4}^{1}) (resp. ( I 2 1) (I_{2}^{1})) contains the parabola and nilpotent saddle-node at infinity and corresponds to C 0 = 1 C_{0}=1 (resp. C 0 > 1 C_{0}>1). The graphic ( I 4 1) (I_{4}^{1}) contains a finite saddle-node located on the parabola. In contrast, the parabola is regular for ( I 2 1) (I_{2}^{1}). (The case C 0 < 1 C_{0}<1 is not relevant since there can be no passage along the parabola.) The full unfolding in quadratic systems of these graphics is given by ( 6.2) (we refer to [10]).

If we apply the transformation ( x, y) = ( v z, 1 z) (x,y)=(\frac{v}{z},\frac{1}{z}) (the positive y y -direction) to system ( 6.2), we obtain

(6.3) |  | v ˙ \displaystyle\dot{v} | = μ 1 + μ 2 ​ v − v 3 − z + A ​ v ​ z − C ​ v 2 ​ z, \displaystyle=\mu_{1}+\mu_{2}v-v^{3}-z+Avz-Cv^{2}z, |  |

 | z ˙ \displaystyle\dot{z} | = − z ⁡ ( μ 3 + v + v 2 + C ​ v ​ z), \displaystyle=-z\left(\mu_{3}+v+v^{2}+Cvz\right), |  |

after multiplying by z z. Notice that the invariant line z = 0 z=0 corresponds to y = ∞ y=\infty. When ( μ 1, μ 2, μ 3) = ( 0, 0, 0) (\mu_{1},\mu_{2},\mu_{3})=(0,0,0), system ( 6.3) has a nilpotent saddle-node of multiplicity 4 at ( v, z) = ( 0, 0) (v,z)=(0,0). We make the rescaling ( μ 1, μ 2, μ 3) = ( ν 2 ​ μ ¯ 1, ν ​ μ ¯ 2, ν ​ μ ¯ 3) (\mu_{1},\mu_{2},\mu_{3})=(\nu^{2}\bar{\mu}_{1},\nu\bar{\mu}_{2},\nu\bar{\mu}_{3}), with ( μ ¯ 1, μ ¯ 2, μ ¯ 3) ∈ 𝕊 2 (\bar{\mu}_{1},\bar{\mu}_{2},\bar{\mu}_{3})\in\mathbb{S}^{2}, ν > 0 \nu>0 small. Then we perform a blow-up of ( 6.3) (with ν ˙ = 0 \dot{\nu}=0 augmented): ( v, z, ν) = ( r ​ v ¯, r 2 ​ z ¯, r ​ ν ¯) (v,z,\nu)=(r\bar{v},r^{2}\bar{z},r\bar{\nu}), with ( v ¯, z ¯, ν ¯) ∈ 𝕊 2 (\bar{v},\bar{z},\bar{\nu})\in\mathbb{S}^{2} and r > 0 r>0. In the family chart ν ¯ = 1 \bar{\nu}=1, we obtain a desingularized system of slow-fast type, with the line of singularities z ¯ = 0 \bar{z}=0 for ( μ ¯ 1, μ ¯ 2, r) = ( 0, 0, 0) (\bar{\mu}_{1},\bar{\mu}_{2},r)=(0,0,0). We refer to Fig. 1. Finally, after additional scaling ( μ ¯ 1, μ ¯ 2, r) = ( ϵ ​ μ ~ 1, ϵ ​ μ ~ 2, ϵ ​ r ~) (\bar{\mu}_{1},\bar{\mu}_{2},r)=(\epsilon\tilde{\mu}_{1},\epsilon\tilde{\mu}_{2},\epsilon\tilde{r}), with ( μ ~ 1, μ ~ 2, r ~) ∈ 𝕊 2 (\tilde{\mu}_{1},\tilde{\mu}_{2},\tilde{r})\in\mathbb{S}^{2} and ϵ > 0 \epsilon>0, it is not difficult to see that this system (with the parameters kept in a suitable region) is analytically equivalent to a slow-fast system of type ( 6.1). (There also exists a region in the parameter space where the classical entry-exit problem [6, 9] occurs.)

The computation of the entry-exit function for ( 6.1) plays a crucial role in detecting limit periodic sets whose cyclicity needs to be studied and in proving finite cyclicity of such sets. We postpone further details on the cyclicity to [10].

The entry-exit formula ( 2.13) for ( 6.1) becomes

 | β ​ ∫ x out b x in b 1 − 1 + β ​ s ​ 𝑑 s + log ⁡ ( − x out b x in b) = λ 1 ​ π − 4 ​ λ 0 − λ 1 2, \displaystyle\beta\int_{x_{\text{out}}^{b}}^{x_{\text{in}}^{b}}\frac{1}{-1+\beta s}ds+\log\left(-\frac{x_{\text{out}}^{b}}{x_{\text{in}}^{b}}\right)=\frac{\lambda_{1}\pi}{\sqrt{-4\lambda_{0}-\lambda_{1}^{2}}}, |  |

or, equivalently,

 | log ⁡ ( − ( 1 − β ​ x in b) ​ x out b ( 1 − β ​ x out b) ​ x in b) = λ 1 ​ π − 4 ​ λ 0 − λ 1 2, \displaystyle\log\left(-\frac{(1-\beta x_{\text{in}}^{b})x_{\text{out}}^{b}}{(1-\beta x_{\text{out}}^{b})x_{\text{in}}^{b}}\right)=\frac{\lambda_{1}\pi}{\sqrt{-4\lambda_{0}-\lambda_{1}^{2}}}, |  |

with x in b ∈ ( 0, 1 β) x_{\text{in}}^{b}\in(0,\frac{1}{\beta}) and x out b < 0 x_{\text{out}}^{b}<0. Using this, we get

(6.4) |  | x out b = e K ​ x in b β ⁡ ( e K + 1) ​ x in b − 1, \displaystyle x_{\text{out}}^{b}=\frac{{\mathrm{e}}^{K}x_{\text{in}}^{b}}{\beta\left({\mathrm{e}}^{K}+1\right)x_{\text{in}}^{b}-1}, |  |

where we write K = λ 1 ​ π − 4 ​ λ 0 − λ 1 2 K=\frac{\lambda_{1}\pi}{\sqrt{-4\lambda_{0}-\lambda_{1}^{2}}}. Since we require x out b < 0 x_{\text{out}}^{b}<0, from ( 6.4) it follows that x in b x_{\text{in}}^{b} has to be kept in the interval ( 0, 1 β ⁡ ( e K + 1)) (0,\frac{1}{\beta\left({\mathrm{e}}^{K}+1\right)}).

When ϵ = 0 \epsilon=0, system ( 6.1) becomes

(6.5) |  | x ˙ \displaystyle\dot{x} | = − y, \displaystyle=-y, |  |

 | y ˙ \displaystyle\dot{y} | = − x ​ y. \displaystyle=-xy. |  |

The fast fibers of ( 6.5) are parabolas y = 1 2 ​ x 2 + C y=\frac{1}{2}x^{2}+C. The parabola passing through ( x in, δ) (x_{\text{in}},\delta) intersects the x x -axis at the base point ( x in b, 0) (x_{\text{in}}^{b},0) with

(6.6) |  | x in b = x in 2 − 2 ​ δ. \displaystyle x_{\text{in}}^{b}=\sqrt{x_{\text{in}}^{2}-2\delta}. |  |

Similarly, the base point ( x out b, 0) (x_{\text{out}}^{b},0) of ( x out, δ) (x_{\text{out}},\delta) is given by

(6.7) |  | x out b = − x out 2 − 2 ​ δ. \displaystyle x_{\text{out}}^{b}=-\sqrt{x_{\text{out}}^{2}-2\delta}. |  |

If we plug the expressions ( 6.6) and ( 6.7) into the formula ( 6.4), we finally get

(6.8) |  | x out = Δ 0 ​ ( x in):= − 2 ​ δ + e 2 ​ K ​ ( x in 2 − 2 ​ δ) ( β ⁡ ( e K + 1) ​ x in 2 − 2 ​ δ − 1) 2. \displaystyle x_{\text{out}}=\Delta_{0}(x_{\text{in}}):=-\sqrt{2\delta+\frac{{\mathrm{e}}^{2K}(x_{\text{in}}^{2}-2\delta)}{\left(\beta\left({\mathrm{e}}^{K}+1\right)\sqrt{x_{\text{in}}^{2}-2\delta}-1\right)^{2}}}. |  |

We suppose that I in I_{\text{in}} is a segment with

 | I in ⊂ ( 2 ​ δ, 2 ​ δ + 1 β 2 ​ ( e K + 1) 2), I_{\text{in}}\subset\left(\sqrt{2\delta},\sqrt{2\delta+\frac{1}{\beta^{2}({\mathrm{e}}^{K}+1)^{2}}}\right), |  |

and I out ⊂ ( − ∞, 0) I_{\text{out}}\subset(-\infty,0) is an appropriate segment. Then the following result is a simple consequence of Theorem 2.4.

###### Theorem 6.1.

Fix any k ∈ ℕ k\in\mathbb{N}. Then the Dulac map Δ ⁡ ( ⋅, ϵ): I in → I out \Delta(\cdot,\epsilon):I_{\text{in}}\rightarrow I_{\text{out}} associated with ( 6.1) is well-defined for all ϵ ∈] 0, ϵ 0 [\epsilon\in]0,\epsilon_{0}[and takes the following form

 | Δ ⁡ ( x in, ϵ) = Δ 0 ​ ( x in) + ϕ ⁡ ( x in, ϵ, ϵ ​ log ⁡ ϵ − 1), \displaystyle\Delta(x_{\text{in}},\epsilon)=\Delta_{0}(x_{\text{in}})+\phi(x_{\text{in}},\epsilon,\epsilon\log\epsilon^{-1}), |  |

where Δ 0 ​ ( x in) \Delta_{0}(x_{\text{in}}) is defined in ( 6.8) and ϕ \phi is C k C^{k} -smooth and satisfies ϕ ⁡ ( x in, 0, 0) = 0 \phi(x_{\text{in}},0,0)=0 for all x in ∈ I in x_{\text{in}}\in I_{\text{in}}.

### 6.1. Numerical computations of Δ \Delta for ( 6.1)

In Fig. 6 (a), we have used Matlab’s ODE15s with low tolerances ( 10 − 12 10^{-12}) to compute x out = Δ ⁡ ( x in, ϵ) x_{\text{out}}=\Delta(x_{\text{in}},\epsilon) for ( 6.1) with 𝒪 ⁡ ( ϵ) \mathcal{O}(\epsilon) and ζ ~ 2 \widetilde{\zeta}_{2} both set to zero, and the following parameter values:

(6.9) |  | λ 0 = − 2, λ 1 = 1, β = 1, δ = 1 2, \displaystyle\lambda_{0}=-2,\quad\lambda_{1}=1,\quad\beta=1,\quad\delta=\frac{1}{2}, |  |

and ϵ = 0.01 \epsilon=0.01 (magenta), ϵ = 0.005 \epsilon=0.005 (red) and ϵ = 0.001 \epsilon=0.001 (blue). The result is clearly in agreement with Theorem 6.1 as we see a convergence towards the theoretical curve x out = Δ 0 ​ ( x in) x_{\text{out}}=\Delta_{0}(x_{\text{in}}) given by ( 6.8) (black and dashed). In order to compute x out x_{\text{out}}, it was crucial to use the corresponding ( x, z) (x,z) -system:

 | x ˙ \displaystyle\dot{x} | = ϵ ( ϵ 2 λ 0 + ϵ λ 1 x + x 2 ( − 1 + β x)) − e − 1 / z, \displaystyle=\epsilon\left(\epsilon^{2}\lambda_{0}+\epsilon\lambda_{1}x+x^{2}(-1+\beta x)\right)-{\mathrm{e}}^{-1/z}, |  |

 | z ˙ \displaystyle\dot{z} | = − x ​ z 2. \displaystyle=-xz^{2}. |  |

Indeed, in the ( x, y) (x,y) -coordinates, y y becomes exponentially small w.r.t. ϵ → 0 \epsilon\to 0 and round-off errors lead to meaningless predictions of x out x_{\text{out}} (without any significant delay; results of this are not shown for simplicity). We therefore speculate that the transformation ( 3.1) has practical significance for numerical computations of entry-exit problems in general.

In Fig. 6 (b), we show trajectories in the ( x, z 2) (x,z_{2}) -plane for fixed x in = 1.016 x_{\text{in}}=1.016 ( x in b = 0.18 x_{\text{in}}^{b}=0.18), recall the definition of z 2 = ϵ − 1 ​ z z_{2}=\epsilon^{-1}z in ( 3.4), and ϵ = 0.01 \epsilon=0.01 (magenta), ϵ = 0.005 \epsilon=0.005 (red) and ϵ = 0.001 \epsilon=0.001 (blue). The theoretical curve for ϵ = 0 \epsilon=0 given by ( 3.10) is shown in dashed and black for comparison. Notice the cusp-like behavior of the trajectories as they pass close to x = 0 x=0 (which is a degenerate line for ϵ = 0 \epsilon=0, recall Fig. 4 and Fig. 3). This is due to the 1 / log ⁡ | x | 1/\log|x| -behavior of z 2 z_{2} near x = 0 x=0, recall the discussion below ( 3.10).

Figure 6. In (a): x out x_{\text{out}} for ( 6.1) with the parameter values ( 6.9) and ϵ = 0.01 \epsilon=0.01 (magenta), ϵ = 0.005 \epsilon=0.005 (red) and ϵ = 0.001 \epsilon=0.001 (blue), computed using Matlab’s ODE15s (on the ( x, z) (x,z) -system) with low tolerances. The dashed black line is the theoretical curve obtained from ( 6.8). In (b): Trajectories in the ( x, z 2) (x,z_{2}) -plane, recall ( 3.4), for the same parameter values as in (a) but with x in = 1.016 x_{\text{in}}=1.016 ( x in b = 0.18 x_{\text{in}}^{b}=0.18) fixed. The dashed black line is again the theoretical curve obtained from ( 3.10).

## Acknowledgments

The authors thank Technical University of Denmark for the hospitality during R. Huzak’s research visit in the spring of 2025. R. Huzak’s stay was facilitated by K. U. Kristiansen’s Danish Research Council (DFF) grant 4283-00014B. Finally, the research of R. Huzak was supported by Croatian Science Foundation (HRZZ) grant IP-2022-10-9820.

## References

- [1] S. Ai and Y. Yi. Relaxation oscillations in predator-prey systems. J. Dyn. Differ. Equations, 36:s77–s104, 2024.
- [2] É. Benoit. Linear dynamic bifurcation with noise. In Dynamic bifurcations (Luminy, 1990), volume 1493 of Lecture Notes in Math., pages 131–150. Springer, Berlin, 1991.
- [3] P. De Maesschalck and F. Dumortier. Singular perturbations and vanishing passage through a turning point. J. Differential Equations, 248(9):2294–2328, 2010.
- [4] P. De Maesschalck and F. Dumortier. Detectable canard cycles with singular slow dynamics of any order at the turning point. Discrete Contin. Dyn. Syst., 29(1):109–140, 2011.
- [5] P. De Maesschalck, F. Dumortier, and R. Roussarie. Canard cycles—from birth to transition, volume 73 of Series of modern surveys in mathematics. Springer, Cham, 2021.
- [6] P. De Maesschalck and S. Schecter. The entry-exit function and geometric singular perturbation theory. J. Differ. Equations, 260(8):6697–6715, 2016.
- [7] F. Dumortier, R. Roussarie, and C. Rousseau. Hilbert’s 16th problem for quadratic vector fields. J. Differential Equations, 110(1):86–133, 1994.
- [8] T.-H. Hsu. On bifurcation delay: an alternative approach using geometric singular perturbation theory. J. Differ. Equations, 262(3):1617–1630, 2017.
- [9] T.-H. Hsu. Number and stability of relaxation oscillations for predator-prey systems with small death rates. SIAM J. Appl. Dyn. Syst., 18(1):33–67, 2019.
- [10] R. Huzak, K.U. Kristiansen, and C. Rousseau. Graphics through a nilpotent saddle-node at infinity in the Dumortier-Roussarie-Rousseau program, work in progress.
- [11] Yu. S. Il’yashenko and S. Yu. Yakovenko. Finitely-smooth normal forms of local families of diffeomorphisms and vector fields. Russ. Math. Surv., 46(1):1–43, 1991.
- [12] P. Kaklamanos, C. Kuehn, N. Popović, and M. Sensi. Entry-exit functions in fast-slow systems with intersecting eigenvalues. J. Dyn. Differ. Equations, 37(1):559–576, 2025.
- [13] E. F. Mishchenko, Yu. S. Kolesov, A. Yu. Kolesov, and N. Kh. Rozov. Asymptotic methods in singularly perturbed systems. Monographs in Contemporary Mathematics. Consultants Bureau, New York, 1994. Translated from the Russian by Irene Aleksanova.
- [14] S. Schecter. Persistent unstable equilibria and closed orbits of a singularly perturbed equation. J. Differ. Equations, 60:131–141, 1985.
- [15] C. Wang and X. Zhang. Stability loss delay and smoothness of the return map in slow-fast systems. SIAM J. Appl. Dyn. Syst., 17(1):788–822, 2018.
- [16] J. Yao, J. Huang, R. Huzak, and S. Ruan. Cyclicity of slow-fast cycles with one self-intersection point and two nilpotent contact points. Nonlinearity, 37(11):30, 2024. Id/No 115007.
- [17] H. Zhu and C. Rousseau. Finite cyclicity of graphics with a nilpotent singularity of saddle or elliptic type. J. Differ. Equations, 178(2):325–436, 2002.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2510.02769
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2510.02770
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2510.02770
[7]: https://arxiv.org/pdf/2510.02770
[8]: /html/2510.02771
