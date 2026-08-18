<!-- source: https://arxiv.org/html/2109.07759 | converted from HTML -->

The number of limit cycles for regularized piecewise polynomial systems is unbounded

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2109.07759v2 [math.DS] 13 Oct 2022

# The number of limit cycles for regularized piecewise polynomial systems is unbounded

R. Huzak Address: Hasselt University, Campus Diepenbeek, Agoralaan Gebouw D, 3590 Diepenbeek, Belgium and K. Uldall Kristiansen Address: Department of Applied Mathematics and Computer Science, Technical University of Denmark, 2800 Kgs. Lyngby, Denmark

###### Abstract.

In this paper, we extend the slow divergence-integral from slow-fast systems, due to De Maesschalck, Dumortier and Roussarie, to smooth systems that limit onto piecewise smooth ones as ϵ → 0 \epsilon\rightarrow 0. In slow-fast systems, the slow divergence-integral is an integral of the divergence along a canard cycle with respect to the slow time and it has proven very useful in obtaining good lower and upper bounds of limit cycles in planar polynomial systems. In this paper, our slow divergence-integral is based upon integration along a generalized canard cycle for a piecewise smooth two-fold bifurcation (of type visible-invisible called V ​ I 3 VI_{3}). We use this framework to show that the number of limit cycles in regularized piecewise smooth polynomial systems is unbounded.

keywords. Slow divergence-integral, canards, piecewise smooth systems, two-folds, GSPT

## 1. Introduction

In this paper, we consider smooth systems of the form

(1.1) |  | z ˙ \displaystyle\dot{z} | = Z ⁡ ( z, ϕ ⁡ ( h ⁡ ( z) ​ ϵ − 1)), \displaystyle=Z(z,\phi(h(z)\epsilon^{-1})), |  |

for z ∈ ℝ n z\in\mathbb{R}^{n}, 0 < ϵ ≪ 1 0<\epsilon\ll 1 and where h: ℝ n → ℝ h:\mathbb{R}^{n}\rightarrow\mathbb{R} is regular, ϕ \phi is a regularization function:

(1.2) |  | ϕ ′ ​ ( s) > 0 ​ for all ​ s ∈ ℝ, ϕ ⁡ ( s) → { 1 for ​ s → ∞ 0 for ​ s → − ∞ \displaystyle\phi^{\prime}(s)>0\mbox{ for all }s\in\mathbb{R},\quad\phi(s)\rightarrow\begin{cases}1&\text{for}\,\,s\rightarrow\infty\\ 0&\text{for}\,\,s\rightarrow-\infty\end{cases} |  |

and where Z Z is affine in its second component:

(1.3) |  | Z ⁡ ( z, p) = Z + ​ ( z) ​ p + Z − ​ ( z) ​ ( 1 − p). \displaystyle Z(z,p)=Z_{+}(z)p+Z_{-}(z)(1-p). |  |

These systems have recently received a great deal of attention [8, 9, 36, 35, 39, 40, 41, 42, 43]. The motivation is three-fold. Firstly, in the limit ϵ → 0 \epsilon\rightarrow 0 the system ( 1.1) becomes piecewise smooth (PWS)

(1.4) |  | z ˙ \displaystyle\dot{z} | = { Z + ​ ( z) ​ for ​ h ​ ( z) > 0, Z − ​ ( z) ​ for ​ h ​ ( z) < 0, \displaystyle=\begin{cases}Z_{+}(z)\text{ for }h(z)>0,\\ Z_{-}(z)\text{ for }h(z)<0,\end{cases} |  |

with Σ:= { z: h ⁡ ( z) = 0 } \Sigma:=\{z:h(z)=0\} being a discontinuity/switching manifold, see Fig. 1.

Figure 1. A planar piecewise smooth system ( 1.4), having Σ \Sigma as a switching manifold. Here regular orbits of Z + Z_{+} and Z − Z_{-} reach Σ \Sigma in finite time. The point Σ T \Sigma_{T} is a tangency point of Z + Z_{+} (a visible fold if the tangency is quadratic). In the present case, where Z − Z_{-} is transverse to Σ \Sigma it divides Σ \Sigma into sliding (to the left of Σ T \Sigma_{T}) where Z ± Z_{\pm} are in opposition relative to Σ \Sigma and crossing (to the right of Σ T \Sigma_{T}) where Z ± Z_{\pm} point in the same direction relative to Σ \Sigma. The situation is different if Z − Z_{-} also has a fold at Σ T \Sigma_{T} (called a two-fold). Then there can be sliding (stable and unstable) on each side of Σ T \Sigma_{T}, see Fig. 2.

For 0 < ϵ ≪ 1 0<\epsilon\ll 1, the system ( 1.1) is therefore a regularized PWS system [18, 28]. The reason for restricting to ( 1.3) is that in this case, one can show [55] that the singular limit system is a Filippov system [18, 28]. Lately, there has been a growing interest in understanding how PWS phenomena (folds, grazing, boundary equilibria,… [45]) unfold in the smooth version [35, 36, 40, 41, 42]. For this purpose methods from Geometric Singular Perturbation Theory (GSPT) and blowup have been refined to deal with resolving the special singular limit of ( 1.1) [40, 41]. Finally, the interest in systems of the form ( 1.1) is also motivated by applications. For example, in biology switches [18, 43] are frequently modeled by functions ( 1.2) and friction is also inherently piecewise smooth [3].

Mathematically, piecewise smooth system has also received a great deal of attention over the past decades. Starting from the groundbreaking work of Filippov [28] and Utkin [57], there was an effort to extend Peixito’s program of structural stability to PWS systems [10, 55]. Subsequently, there has been a focus on characterizing and interpreting the lack of uniqueness of solutions in PWS systems [34].

Parallel to this effort, there has been an attempt to bound the number limit cycles in PWS systems in the plane where n = 2 n=2. In contrast to the smooth linear setting, limit cycles can exist for piecewise linear systems and J. Llibre and co-workers have obtained upper bounds for a number of cases [26, 49, 52]. Of course, the interest in bounding the number of limit cycles, comes from Hilbert’s 16th problem [48] which seeks to bound the number of limit cycles of polynomial systems:

(1.5) |  | x ˙ \displaystyle\dot{x} | = P N ​ ( x, y), \displaystyle=P_{N}(x,y), |  |

 | y ˙ \displaystyle\dot{y} | = Q N ​ ( x, y), \displaystyle=Q_{N}(x,y), |  |

with P N P_{N} and Q N Q_{N} of fixed degree N N. Hilbert’s 16th problem remains unsolved to this day. Whereas general progress has been made on N = 2 N=2 [1, 4, 5, 20, 24, 25, 31, 53] and on Smale’s version of the problem where ( 1.5) is restricted to classical Liénard type: P N ​ ( x, y) = y − p N ​ ( x), Q N = − x P_{N}(x,y)=y-p_{N}(x),\,Q_{N}=-x, see [11, 46, 50, 54], there has been an emphasis on obtaining good lower bounds on the number of limit cycles (see [12, 29, 30, 51] and references therein). Following the work of De Maesschalck, Dumortier and Roussarie, see [14, 15, 19, 22, 23], a key tool in this effort has been the slow divergence-integral from slow-fast systems and canard theory; in particular, the roots of the slow divergence-integral provide candidates for limit cycles. For example, using this tool good lower bounds on the number of limit cycles in Liénard equations can be found (see [16, 17, 21, 33, 59]).

### 1.1. Main result

In this paper, we work at the interface of these research fields. In particular, we consider ( 1.1) with n = 2 n=2, put z = ( x, y) z=(x,y) and restrict attention to the case h ⁡ ( z) = y h(z)=y so that the switching manifold is Σ = { ( x, y): y = 0 } \Sigma=\{(x,y):y=0\} and then ask the following question:

Does there exist polynomial vector-fields Z ± Z_{\pm} such that the number of limit cycles of Z Z is unbounded?

We prove that this is in fact true, even for quadratic vector-fields. More precisely we prove the following.

###### Theorem 1.1.

There exists a quadratic vector-field Z + ​ ( ⋅, λ) Z_{+}(\cdot,\lambda) and a linear vector-field Z − ​ ( ⋅, λ) Z_{-}(\cdot,\lambda), depending smoothly on a parameter λ ∈ ℝ \lambda\in\mathbb{R}, such that the following holds true in a compact domain U U:

For every k ∈ ℕ k\in\mathbb{N} there exist: (a) ϵ k > 0 \epsilon_{k}>0, (b) a regularization function ϕ k: ℝ → ℝ \phi_{k}:\mathbb{R}\rightarrow\mathbb{R}, and (c) a continuous function λ c k: [0, ϵ k [→ ℝ \lambda_{c}^{k}:[0,\epsilon_{k}[\rightarrow\mathbb{R} such that the regularized vector-field:

 | Z ⁡ ( z) = Z + ​ ( z, λ c k ​ ( ϵ)) ​ ϕ k ​ ( y ​ ϵ − 1) + Z − ​ ( z, λ c k ​ ( ϵ)) ​ ( 1 − ϕ k ​ ( y ​ ϵ − 1)), \displaystyle Z(z)=Z_{+}(z,\lambda_{c}^{k}(\epsilon))\phi_{k}(y\epsilon^{-1})+Z_{-}(z,\lambda_{c}^{k}(\epsilon))(1-\phi_{k}(y\epsilon^{-1})), |  |

has at least k k limit cycles contained in U U for all ϵ ∈] 0, ϵ k [\epsilon\in]0,\epsilon_{k}[.

We give examples of Z + Z_{+} and Z − Z_{-} later on, see ( 4.13)( 4.14). We emphasize that the unboundedness of limit cycles stems from the regularization and not from the vector-fields Z ± Z_{\pm}. We use smooth regularization functions in order to find an unbounded number of limit cycles. It is known that boundedness of limit cycles is closely related to the notion of o-minimality in function spaces (see e.g. [37]). Our smoothings are taken from a family that does not have this o-minimality property. From this viewpoint it is not surprising that we find that the number of limit cycles is unbounded.

At the same time, Theorem 1.1 also illustrates a certain degree of deficiency with smoothing piecewise smooth systems (since the result may depend upon how we regularize). On the other hand, there are other complementary results, see [9, 35, 36, 40], that show that smoothing play little role (at least on a macroscopic-level, i.e. at 𝒪 ⁡ ( 1) \mathcal{O}(1)) for different types of PWS singularities and bifurcations. In [40] for example, it was shown that the regularization of the visible-invisible fold in ℝ 3 \mathbb{R}^{3}, with Σ \Sigma being two-dimensional, is independent of the smoothing function. In fact, for the system in Theorem 1.1 it is also only in an exponentially small parameter regime that a different number of limit cycles can be realized for different regularization functions.

To prove Theorem 1.1, we will follow the approach of [14] and use a slow divergence-integral. But seeing that our system is nonsmooth (as opposed to slow-fast) in the singular limit ϵ → 0 \epsilon\rightarrow 0 we will first have to develop this framework within the setting of ( 1.1). For slow-fast systems, the slow divergence-integral is defined along a canard trajectory, i.e. along a folded critical manifold with an equilibrium at the fold in such way that the reduced problem goes from the attracting sheet to the repelling one with nonzero speed. In the setting of ( 1.1), our slow divergence-integral will be based upon the PWS two-fold bifurcation [7, 42], which is reminiscent of the standard canard [22, 44]. In particular, Z ± Z_{\pm} in Theorem 1.1 will be chosen so that the PWS system has a two-fold bifurcation (of type visible-invisible called V ​ I 3 VI_{3} [45]). Proposition 3.2 then describes the structure of the difference map near the associated canard-like limit periodic sets (see Section 3.2).

Proposition 3.2 is not only relevant and important for proving Theorem 1.1, but also for studying bifurcations of limit cycles inside such visible-invisible two-folds (see Remark 3.4). This proposition is therefore also one of our main results, but we delay the detailed statement to later sections after having introduced the two-fold bifurcation model (see Section 2).

Our approach for constructing an unbounded number of limit cycles, does not work for the piecewise linear case. It would be interesting to study the linear case more carefully in future work.

### 1.2. Overview

The paper is organized as follows: In Section 2, we define a planar PWS two-fold and revisit some results from [7, 42] on canards of ( 1.1) for 0 < ϵ ≪ 1 0<\epsilon\ll 1. Next in Section 3 we define the slow divergence-integral and prove that simple roots of this function lead to hyperbolic limit cycles (Theorem 3.1). In the proof of Theorem 3.1, we describe the difference map in terms of the slow divergence integral in Proposition 3.2. For the proof of this statement, we also use Appendix A and Appendix B. In Section 4 we then prove Theorem 1.1, using Theorem 3.1, see also Theorem 4.3, and finally in Section 5 we illustrate our approach with numerical examples.

## 2. The two-fold bifurcation

We consider ( 1.1) with h ⁡ ( z) = y h(z)=y:

(2.1) |  | z ˙ \displaystyle\dot{z} | = Z ⁡ ( z, ϕ ⁡ ( y ​ ϵ − 2), λ), \displaystyle=Z(z,\phi(y\epsilon^{-2}),\lambda), |  |

for z = ( x, y) ∈ ℝ 2 z=(x,y)\in\mathbb{R}^{2}. In comparison with ( 1.1) we have also included λ ∼ λ 0 ∈ ℝ \lambda\sim\lambda_{0}\in\mathbb{R} as an additional unfolding parameter. Notice also that we write ϵ − 2 \epsilon^{-2} in ( 2.1) rather than just ϵ − 1 \epsilon^{-1}, since this will be convenient later on (see Section 3.1). The basic assumption is that the right hand side Z Z is smooth in each entry (in this paper, by “smooth” we mean differentiable of class C ∞ C^{\infty}). In particular we suppose that it is affine in the second component, i.e.,

 | Z ⁡ ( z, p, λ) = Z + ​ ( z, λ) ​ p + Z − ​ ( z, λ) ​ ( 1 − p), \displaystyle Z(z,p,\lambda)=Z_{+}(z,\lambda)p+Z_{-}(z,\lambda)(1-p), |  |

where Z ± = ( X ±, Y ±) Z_{\pm}=(X_{\pm},Y_{\pm}) are smooth in ( z, λ) (z,\lambda). The function ϕ: ℝ → ℝ \phi:\mathbb{R}\to\mathbb{R} is a smooth sigmoidal function satisfying the following assumptions:

1. (A1)

The function ϕ \phi has the following asymptotics when s → ± ∞ s\to\pm\infty:

 | ϕ ⁡ ( s) → { 1 for s → ∞, 0 for s → − ∞. \displaystyle\phi(s)\rightarrow\begin{cases}1&\text{for}\quad s\rightarrow\infty,\\ 0&\text{for}\quad s\rightarrow-\infty.\end{cases} |  |

2. (A2)

The function ϕ \phi is strictly monotone, i.e., ϕ ′ ​ ( s) > 0 \phi^{\prime}(s)>0 for all s ∈ ℝ s\in\mathbb{R}.

3. (A3)

The function ϕ \phi is smooth at ± ∞ \pm\infty in the following sense: Each of the functions

 | ϕ + ​ ( s):= { 1 for s = 0, ϕ ⁡ ( s − 1) for s > 0,, ϕ − ​ ( s):= { ϕ ⁡ ( − s − 1) for s > 0, 0 for s = 0, \displaystyle\phi_{+}(s):=\begin{cases}1&\text{for}\quad s=0,\\ \phi(s^{-1})&\text{for}\quad s>0,\end{cases},\quad\phi_{-}(s):=\begin{cases}\phi(-s^{-1})&\text{for}\quad s>0,\\ 0&\text{for}\quad s=0,\end{cases} |  |

are smooth at s = 0 s=0.

By assumption (A1), the system ( 2.1) is piecewise smooth (PWS) in the limit ϵ → 0 \epsilon\rightarrow 0:

(2.2) |  | z ˙ = { Z + ​ ( z, λ) for y > 0, Z − ​ ( z, λ) for y < 0, \displaystyle\dot{z}=\begin{cases}Z_{+}(z,\lambda)&\text{for}\quad y>0,\\ Z_{-}(z,\lambda)&\text{for}\quad y<0,\end{cases} |  |

the set Σ \Sigma defined by ( x, 0) (x,0) being the discontinuity set/switching manifold, for each λ ∼ λ 0 \lambda\sim\lambda_{0}. In fact, from assumption (A3) we have that ( 2.1) is a regular perturbation of Z + Z_{+} or Z − Z_{-} outside any fixed neighborhood of y = 0 y=0. In particular:

###### Lemma 2.1.

Suppose that there is a smallest k ∈ ℕ k\in\mathbb{N} such that ϕ + ( k) ​ ( 0) ≠ 0 \phi_{+}^{(k)}(0)\neq 0. Then within y ≥ c y\geq c, with c > 0 c>0 fixed

 | Z = Z + + 𝒪 ⁡ ( ϵ 2 ​ k), \displaystyle Z=Z_{+}+\mathcal{O}(\epsilon^{2k}), |  |

smoothly and uniformly with respect to ϵ → 0 \epsilon\rightarrow 0.

A similar result obviously holds for Z − Z_{-} (in terms of ϕ − ( k) ≠ 0 \phi_{-}^{(k)}\neq 0). In PWS theory [18] we divide Σ \Sigma into different subsets Σ c ​ r ​ ( λ) \Sigma_{cr}(\lambda), Σ s ​ l ​ ( λ) \Sigma_{sl}(\lambda) and Σ T ​ ( λ) \Sigma_{T}(\lambda), each depending upon on λ \lambda, which are defined as follows:

- (1)

The subset Σ c ​ r ​ ( λ) ⊂ Σ \Sigma_{cr}(\lambda)\subset\Sigma consisting of all points q = ( x, 0) q=(x,0) where

 | Y + ​ ( q, λ) ​ Y − ​ ( q, λ) > 0, \displaystyle Y_{+}(q,\lambda)Y_{-}(q,\lambda)>0, |  |

is called “crossing”.

- (2)

The subset Σ s ​ l ​ ( λ) ⊂ Σ \Sigma_{sl}(\lambda)\subset\Sigma consisting of all points q = ( x, 0) q=(x,0) where

 | Y + ​ ( q, λ) ​ Y − ​ ( q, λ) < 0. \displaystyle Y_{+}(q,\lambda)Y_{-}(q,\lambda)<0. |  |

is called “sliding”. It is said to be stable (resp. unstable) if Y + < 0 Y_{+}<0 and Y − > 0 Y_{-}>0, (resp. Y + > 0 Y_{+}>0 and Y − < 0 Y_{-}<0).

- (3)

The subset Σ T ​ ( λ) ⊂ Σ \Sigma_{T}(\lambda)\subset\Sigma where either Y + ​ ( q, λ) = 0 Y_{+}(q,\lambda)=0 or Y − ​ ( q, λ) = 0 Y_{-}(q,\lambda)=0 is called the PWS singularities.

It is well-known [55], that once assumption (A2) holds, sliding for ( 2.2) implies existence of an invariant manifold for ( 2.1).

###### Theorem 2.2.

Suppose that (A1) and (A2) hold true and that the PWS system ( 2.2) has stable/unstable sliding along some subset Σ s ​ l ⊂ Σ \Sigma_{sl}\subset\Sigma, i.e. Y + ​ ( x, 0, λ) ​ Y − ​ ( x, 0, λ) < 0 Y_{+}(x,0,\lambda)Y_{-}(x,0,\lambda)<0 for ( x, 0) ∈ Σ s ​ l (x,0)\in\Sigma_{sl}. Let I I be a compact interval so that I × { 0 } ⊂ Σ s ​ l I\times\{0\}\subset\Sigma_{sl}. Then for all 0 < ϵ ≪ 1 0<\epsilon\ll 1, there is a locally invariant manifold of ( 2.1) with foliation by stable/unstable fibers, respectively, of the following graph form y = ϵ 2 ​ h ​ ( x, ϵ 2) y=\epsilon^{2}h(x,\epsilon^{2}), x ∈ I x\in I. The reduced dynamics for ϵ → 0 \epsilon\rightarrow 0 on this manifold is given by:

(2.3) |  | x ˙ \displaystyle\dot{x} | = X s ​ l ​ ( x, λ):= X + ​ ( x, 0, λ) ​ p + X − ​ ( x, 0, λ) ​ ( 1 − p), \displaystyle=X_{sl}(x,\lambda):=X_{+}(x,0,\lambda)p+X_{-}(x,0,\lambda)(1-p), |  |

where p = p ⁡ ( x) ∈] 0, 1 [p=p(x)\in]0,1[solves Y + ​ ( x, 0, λ) ​ p + Y − ​ ( x, 0, λ) ​ ( 1 − p) = 0 Y_{+}(x,0,\lambda)p+Y_{-}(x,0,\lambda)(1-p)=0.

###### Proof.

The proof is elementary so we include it. Define y 2 y_{2} by y = ϵ 2 ​ y 2 y=\epsilon^{2}y_{2}. Then

(2.4) |  | x ′ \displaystyle x^{\prime} | = ϵ 2 ​ X ​ ( x, ϵ 2 ​ y 2, ϕ ⁡ ( y 2), λ), \displaystyle=\epsilon^{2}X(x,\epsilon^{2}y_{2},\phi(y_{2}),\lambda), |  |

 | y 2 ′ \displaystyle y_{2}^{\prime} | = Y ⁡ ( x, ϵ 2 ​ y 2, ϕ ⁡ ( y 2), λ), \displaystyle=Y(x,\epsilon^{2}y_{2},\phi(y_{2}),\lambda), |  |

i.e. a slow-fast system with Y ⁡ ( x, 0, ϕ ⁡ ( y 2), λ) = Y + ​ ( x, 0, λ) ​ ϕ ​ ( y 2) + Y − ​ ( x, 0, λ) ​ ( 1 − ϕ ⁡ ( y 2)) = 0 Y(x,0,\phi(y_{2}),\lambda)=Y_{+}(x,0,\lambda)\phi(y_{2})+Y_{-}(x,0,\lambda)(1-\phi(y_{2}))=0 defining a critical manifold for ϵ = 0 \epsilon=0. Linearization around any point on this manifold for ϵ = 0 \epsilon=0 produces a single nontrivial eigenvalue ( Y + ​ ( x, 0, λ) − Y − ​ ( x, 0, λ)) ​ ϕ ′ ​ ( y 2) \left(Y_{+}(x,0,\lambda)-Y_{-}(x,0,\lambda)\right)\phi^{\prime}(y_{2}) which is nonzero since Y + ​ Y − < 0 Y_{+}Y_{-}<0 and since (A2) holds. In fact, its sign is only determined by Y + Y_{+} and Y − Y_{-}. Hence the critical manifold, which takes a graph form

 | y 2 = ϕ − 1 ​ ( − Y − Y + − Y − ​ ( x, 0, λ)), ( x, 0) ∈ Σ s ​ l ​ ( λ), \displaystyle y_{2}=\phi^{-1}\left(\frac{-Y_{-}}{Y_{+}-Y_{-}}(x,0,\lambda)\right),\,(x,0)\in\Sigma_{sl}(\lambda), |  |

is hyperbolic and attracting/repelling whenever the associated sliding is stable/unstable. The result therefore follows by Fenichel’s theory [27]. ∎

By plugging the expression for

 | p ⁡ ( x, λ) = − Y − Y + − Y − ​ ( x, 0, λ), p(x,\lambda)=\frac{-Y_{-}}{Y_{+}-Y_{-}}(x,0,\lambda), |  |

into ( 2.3), we may write X s ​ l X_{sl} as

(2.5) |  | X s ​ l ​ ( x, λ) = det ​ Z Y + − Y − ​ ( x, 0, λ), \displaystyle X_{sl}(x,\lambda)=\frac{\text{det}\,Z}{Y_{+}-Y_{-}}(x,0,\lambda), |  |

where

 | det ​ Z ​ ( x, 0, λ):= ( X − ​ Y + − X + ​ Y −) ​ ( x, 0, λ) \displaystyle\text{det}\,Z(x,0,\lambda):=(X_{-}Y_{+}-X_{+}Y_{-})(x,0,\lambda) |  |

The vector-field ( 2.5) is known as the Filippov sliding vector-field [28] and PWS systems with this vector-field prescribed on Σ s ​ l \Sigma_{sl} are called Filippov systems.

### 2.1. Folds

Clearly, Σ = Σ s ​ l ​ ( λ) ∪ Σ T ​ ( λ) ∪ Σ c ​ r ​ ( λ) \Sigma=\Sigma_{sl}(\lambda)\cup\Sigma_{T}(\lambda)\cup\Sigma_{cr}(\lambda) for each λ \lambda. We further classify the points in Σ T \Sigma_{T} as follows (see also [18]):

- (4)

A point q ∈ Σ T ​ ( λ) q\in\Sigma_{T}(\lambda) is a fold point from “above” if the orbit of Z + ​ ( ⋅, λ) Z_{+}(\cdot,\lambda) through q q has a quadratic tangency with Σ \Sigma at q q. In terms of Lie-derivatives Z ± ​ ( h) ​ ( ⋅, λ):= ∇ h ⋅ Z ± ​ ( ⋅, λ) Z_{\pm}(h)(\cdot,\lambda):=\nabla h\cdot Z_{\pm}(\cdot,\lambda), with h ⁡ ( x, y) = y h(x,y)=y, the last condition becomes:

 | { Z + ​ ( q, λ) ≠ 0, Z + ​ ( h) ​ ( q, λ) = 0, Z + 2 ​ ( h) ​ ( q, λ) ≠ 0. \displaystyle\begin{cases}Z_{+}(q,\lambda)&\neq 0,\\ Z_{+}(h)(q,\lambda)&=0,\\ Z_{+}^{2}(h)(q,\lambda)&\neq 0.\end{cases} |  |

We define a fold point from “below” in terms of Z − Z_{-} in a similar way.

- (5)

A fold point q ∈ Σ T ​ ( λ) q\in\Sigma_{T}(\lambda) from “above” is said to be visible, if the orbit of Z + ​ ( ⋅, λ) Z_{+}(\cdot,\lambda) through q q is contained within y > 0 y>0 in neighborhood of q q. It is said to be invisible otherwise. In terms of Lie-derivatives, we clearly have Z + 2 ​ ( h) ​ ( q, λ) > 0 Z_{+}^{2}(h)(q,\lambda)>0 iff q q satisfying Z + ​ ( q, λ) ≠ 0 Z_{+}(q,\lambda)\neq 0, Z + ​ ( h) ​ ( q, λ) = 0 Z_{+}(h)(q,\lambda)=0 is visible. Fold points from below are classified in a similar way. In particular, Z − 2 ​ ( h) ​ ( z) < 0 Z_{-}^{2}(h)(z)<0 iff q q satisfying Z − ​ ( q, λ) ≠ 0 Z_{-}(q,\lambda)\neq 0, Z − ​ ( h) ​ ( q, λ) = 0 Z_{-}(h)(q,\lambda)=0 is visible.

Fold points that are only PWS singularities on one side of Σ \Sigma are persistent by the implicit function theorem, in the following sense: If Σ T ​ ( λ 0) \Sigma_{T}(\lambda_{0}) consists of a fold point q ⁡ ( λ 0) q(\lambda_{0}) (from above or below), then Σ T ​ ( λ) \Sigma_{T}(\lambda) also consists of a fold point q ⁡ ( λ) q(\lambda) (from above or below, respectively) for any λ ∼ λ 0 \lambda\sim\lambda_{0}. In fact, q ⁡ ( λ) q(\lambda) then also depends smoothly on λ ∼ λ 0 \lambda\sim\lambda_{0}.

### 2.2. Two-folds

Now, we finally arrive at the concept of two-folds in PWS systems, which will play the role of a canard point in our analysis of ( 2.1).

- (6)

A two-fold q ∈ Σ T ​ ( λ) q\in\Sigma_{T}(\lambda) is a point with quadratic tangencies from above and from below. In terms of Lie-derivatives we have:

(2.6) |  | { Z ± ​ ( q, λ) ≠ 0, Z ± ​ ( h) ​ ( q, λ) = 0, Z ± 2 ​ ( h) ​ ( q, λ) ≠ 0, \displaystyle\begin{cases}Z_{\pm}(q,\lambda)&\neq 0,\\ Z_{\pm}(h)(q,\lambda)&=0,\\ Z_{\pm}^{2}(h)(q,\lambda)&\neq 0,\end{cases} |  |

with these equations understood to hold for both ± \pm.

- (7)

A two-fold is said to be visible-visible, visible-invisible, invisible-invisible according to the “visibility” of the fold from above and below, respectively, see item (5) above.

The three distinct cases are illustrated in Fig. 2. The further details depend on the direction of the flow. In fact, according to [45] there are 7 cases, two visible-visible cases (called V ​ V 1, 2 VV_{1,2}), three visible-invisible cases (called V ​ I 1 − 3 VI_{1-3}) and two invisible-invisible cases I ​ I 1, 2 II_{1,2}). We refer to [45] as well as [7, 42] for further details here. They will not be needed in the present manuscript.

In contrast to a fold, a two-fold is a co-dimension one (PWS) bifurcation [7]. Consequently, if q ∈ Σ T ​ ( λ 0) q\in\Sigma_{T}(\lambda_{0}) is a two-fold then generically there is a neighborhood U U of q q such that Z ± ​ ( ⋅, λ) Z_{\pm}(\cdot,\lambda) for λ ≠ λ 0 \lambda\neq\lambda_{0}, λ ∼ λ 0 \lambda\sim\lambda_{0} does not have any two-folds in U U. Upon writing Z ± ​ ( ⋅, λ) = Z ± ​ ( ⋅, λ 0) + ( λ − λ 0) ​ Z ~ ± ​ ( ⋅) + 𝒪 ⁡ ( ( λ − λ 0) 2) Z_{\pm}(\cdot,\lambda)=Z_{\pm}(\cdot,\lambda_{0})+(\lambda-\lambda_{0})\widetilde{Z}_{\pm}(\cdot)+\mathcal{O}((\lambda-\lambda_{0})^{2}), [7, Theorem 2.6] showed that the unfolding is versal if

(2.7) |  | Y ~ − ​ Y + ′ ≠ Y ~ + ​ Y − ′. \displaystyle\widetilde{Y}_{-}Y_{+}^{\prime}\neq\widetilde{Y}_{+}Y^{\prime}_{-}. |  |

Here we denote by () ′ ()^{\prime} the partial derivative with respect to x x, a convention we will continue to adopt in the following.

Figure 2. The three two-folds: visible-visible (a), visible-invisible (b) and invisible-invisible (c). We have deliberately not put arrows on the orbits of Z − Z_{-} (red) and Z + Z_{+} (green), because Σ s ​ l \Sigma_{sl} and Σ c ​ r \Sigma_{cr} depend on this direction. Notice Σ \Sigma (orange) is the x x -axis in all figures. Following [45] there are 7 cases, two visible-visible cases (called V ​ V 1, 2 VV_{1,2}), three visible-invisible cases (called V ​ I 1 − 3 VI_{1-3}) and two invisible-invisible cases I ​ I 1, 2 II_{1,2}). The case V ​ I 3 VI_{3}, which will be our main focus, is illustrated separately in Fig. 3.

In the present paper, we will focus on the visible-invisible two-fold. In this case, [7, Lemma 2.8] shows that if q q is a visible-invisible two-fold for λ = λ 0 \lambda=\lambda_{0}, then locally

 | Σ ⁡ ( λ 0) = Σ s ​ l ​ ( λ 0) ∪ { q } \displaystyle\Sigma(\lambda_{0})=\Sigma_{sl}(\lambda_{0})\cup\{q\} |  |

whenever

(2.8) |  | X + ​ ( q, λ 0) ​ X − ​ ( q, λ 0) < 0. \displaystyle X_{+}(q,\lambda_{0})X_{-}(q,\lambda_{0})<0. |  |

Consequently, X s ​ l ​ ( x, λ 0) X_{sl}(x,\lambda_{0}) is in this case locally defined for all points on Σ ⁡ ( λ 0) \Sigma(\lambda_{0}) except q q (see Theorem 2.2). Notice in particular from the form ( 2.5) that X s ​ l ​ ( x, λ 0) X_{sl}(x,\lambda_{0}) has a “0/0” at the two-fold. However, by ( 2.6) and ( 2.8) we also have that

(2.9) |  | Y + ′ − Y − ′ ≠ 0, \displaystyle Y_{+}^{\prime}-Y_{-}^{\prime}\neq 0, |  |

at ( q, λ 0) (q,\lambda_{0}), and consequently from ( 2.5) we see that X s ​ l ​ ( x, λ 0) X_{sl}(x,\lambda_{0}) can be extended locally to all of Σ \Sigma by L’Hospital in this case. We collect the findings in the following proposition (fixing q = 0 q=0 for simplicity).

###### Proposition 2.3.

Consider a PWS system ( 2.2) in a sufficiently small neighborhood of the origin. Suppose furthermore that

(2.10) |  | { X + ​ ( 0, λ 0) > 0, Y + ​ ( 0, λ 0) = 0, Y + ′ ​ ( 0, λ 0) > 0, { X − ​ ( 0, λ 0) < 0, Y − ​ ( 0, λ 0) = 0, Y − ′ ​ ( 0, λ 0) < 0. \displaystyle\begin{cases}X_{+}(0,\lambda_{0})&>0,\\ Y_{+}(0,\lambda_{0})&=0,\\ Y_{+}^{\prime}(0,\lambda_{0})&>0,\end{cases}\quad\begin{cases}X_{-}(0,\lambda_{0})&<0,\\ Y_{-}(0,\lambda_{0})&=0,\\ Y_{-}^{\prime}(0,\lambda_{0})&<0.\end{cases} |  |

Then the following holds about system ( 2.2) for λ = λ 0 \lambda=\lambda_{0}:

- (i)

The origin is a visible-invisible two-fold.

- (ii)

Σ = Σ s ​ l ​ ( λ 0) ¯ \Sigma=\overline{\Sigma_{sl}(\lambda_{0})} with stable sliding for x < 0 x<0 and unstable sliding for x > 0 x>0.

- (iii)

X s ​ l ​ ( x, λ 0) X_{sl}(x,\lambda_{0}) is well-defined for all x ∈ Σ x\in\Sigma.

- (iv)

( Y + ′ − Y − ′) ​ ( 0, 0, λ 0) > 0 (Y_{+}^{\prime}-Y_{-}^{\prime})(0,0,\lambda_{0})>0.

Henceforth, we suppose that ( 2.10) holds and that X s ​ l ​ ( x, λ 0) > 0 X_{sl}(x,\lambda_{0})>0 for all x ∈ Σ x\in\Sigma, so that the flow of X s ​ l X_{sl} takes points from stable sliding to unstable sliding. These conditions – which following Proposition 2.3 item (iv) and ( 2.5) imply that

(2.11) |  | det ​ Z ′ > 0 \displaystyle\text{det}\,Z^{\prime}>0 |  |

– correspond to the specific visible-invisible two-fold called V ​ I 3 VI_{3} in [45]. See an illustration of this case in Fig. 3.

Figure 3. The V ​ I 3 VI_{3} visible-invisible two-fold where X s ​ l ​ ( x, λ 0) > 0 X_{sl}(x,\lambda_{0})>0 (in magenta) for all x x locally so that the stable sliding region x < 0 x<0 is connected to the unstable sliding region by the flow of X s ​ l X_{sl} (extended through x = 0 x=0). ξ \xi and ξ ± \xi_{\pm} are used in relation to the slow divergence-integral in Section 3.

.

We collect these assumptions and ( 2.7) into the following hypothesis.

1. (4)

Suppose that ( 2.7) and ( 2.10) both hold and that there are μ − < 0 \mu_{-}<0 and μ + > 0 \mu_{+}>0 such that the PWS system ( 2.2) for λ = λ 0 \lambda=\lambda_{0} has stable sliding for all x ∈ [μ −, 0 [x\in[\mu_{-},0[and unstable sliding for x ∈] 0, μ +] x\in]0,\mu_{+}] and that X s ​ l ​ ( x, λ 0) > 0 X_{sl}(x,\lambda_{0})>0 for all x ∈ [μ −, μ +] x\in[\mu_{-},\mu_{+}]. Moreover, we assume that ξ ( x) ∈ [μ −, 0 [\xi(x)\in[\mu_{-},0[, for each x ∈] 0, μ +] x\in]0,\mu_{+}], where ξ ⁡ ( x) \xi(x) is the x x -value of the first intersection with the x x -axis of the forward flow of ( x, 0) (x,0) following Z − Z_{-} for λ = λ 0 \lambda=\lambda_{0}.

### 2.3. Canards of ( 2.1)

In [7, 42], it was independently shown that under the assumption 4, the two invariant manifolds for x < 0 x<0 and x > 0 x>0 (which are slow manifolds within the scaling regime defined by y = ϵ 2 ​ y 2 y=\epsilon^{2}y_{2}, recall the proof of Theorem 2.2) intersect along some λ ∼ λ 0 \lambda\sim\lambda_{0} for all 0 < ϵ ≪ 1 0<\epsilon\ll 1. Such orbits are also called canards. The reference [42] used the blowup method, which will also form the basis of our analysis.

## 3. The slow divergence-integral and canard limit cycles

Consider ( 2.1) satisfing (A1) - 4. For λ = λ 0 \lambda=\lambda_{0} the singular limit (Filippov) system is shown in Fig. 3. The situation is clearly reminiscent of the classical canard situation. In particular, at the level λ = λ 0 \lambda=\lambda_{0}, we denote by Γ x \Gamma_{x} for x ∈] 0, μ +] x\in]0,\mu_{+}], the limit periodic set consisting of the segment [ξ ⁡ ( x), x] ⊂ Σ [\xi(x),x]\subset\Sigma and the regular orbit of Z − Z_{-} connecting ( x, 0) (x,0) and ( ξ ⁡ ( x), 0) (\xi(x),0). We call Γ x \Gamma_{x} a canard cycle. We then define the associated slow divergence-integral along the segment [ξ ⁡ ( x), x] [\xi(x),x]:

(3.1) |  | I ⁡ ( x) = ∫ ξ ⁡ ( x) x ( Y + − Y −) 2 det ​ Z ​ ( u, 0, λ 0) ​ ϕ ′ ​ ( ϕ − 1 ​ ( − Y − Y + − Y − ​ ( u, 0, λ 0))) ​ 𝑑 u, \displaystyle I(x)=\int_{\xi(x)}^{x}\frac{(Y_{+}-Y_{-})^{2}}{\text{det}\,Z}(u,0,\lambda_{0})\phi^{\prime}\left(\phi^{-1}\left(\frac{-Y_{-}}{Y_{+}-Y_{-}}(u,0,\lambda_{0})\right)\right)du, |  |

for x ∈] 0, μ +] x\in]0,\mu_{+}]. The slow divergence-integral is the integral of the divergence of the vector field ( 2.4), for ϵ = 0 \epsilon=0, computed along the critical manifold w.r.t. the slow time τ \tau defined by d ​ τ = d ​ x X s ​ l ​ ( x, λ 0) d\tau=\frac{dx}{X_{sl}(x,\lambda_{0})}. It follows from 4 that I I in ( 3.1) is well-defined.

The following result plays a crucial role in proving Theorem 1.1.

###### Theorem 3.1.

Let the regularized system ( 2.1) satisfy (A1) - 4. Suppose that I ⁡ ( x) I(x) has exactly k − 1 k-1 simple zeros x 1 < ⋯ < x k − 1 x_{1}<\dots<x_{k-1} in ] 0, μ + []0,\mu_{+}[. If x k ∈] x k − 1, μ +] x_{k}\in]x_{k-1},\mu_{+}], then there is a smooth function λ = λ c ​ ( ϵ) \lambda=\lambda_{c}(\epsilon), with λ c ​ ( 0) = λ 0 \lambda_{c}(0)=\lambda_{0}, such that Z ⁡ ( z, ϕ ⁡ ( y ​ ϵ − 2), λ c ​ ( ϵ)) Z(z,\phi(y\epsilon^{-2}),\lambda_{c}(\epsilon)) has k k periodic orbits 𝒪 1 ϵ, … ​ 𝒪 k ϵ \mathcal{O}_{1}^{\epsilon},\dots\mathcal{O}_{k}^{\epsilon}, for each ϵ ∼ 0 \epsilon\sim 0 and ϵ > 0 \epsilon>0. The periodic orbit 𝒪 i ϵ \mathcal{O}_{i}^{\epsilon} is isolated, hyperbolic and Hausdorff close to the canard cycle Γ x i \Gamma_{x_{i}}, for each i = 1, … ​ k i=1,\dots k.

A result similar to Theorem 3.1 for smooth planar slow-fast systems can be found in [17, 19].

Notice that the statement of Theorem 3.1 deals only with limit cycles of size 𝒪 ⁡ ( 1) \mathcal{O}(1) in the ( x, y) (x,y) -phase space. Once the positive simple zeros of the slow divergence integral I I are detected, the related canard cycles Γ x 1, … \Gamma_{x_{1}},\dots (and hence the limit cycles 𝒪 1 ϵ, … \mathcal{O}_{1}^{\epsilon},\dots) are of size 𝒪 ⁡ ( 1) \mathcal{O}(1). Thus, the limit cycles born from the origin ( x, y) = ( 0, 0) (x,y)=(0,0) are not covered by Theorem 3.1.

We divide the proof of Theorem 3.1 into three parts. In the first part we consider the extended fast-time system ( z ′, ϵ ′) = ( ϵ 2 ​ Z, 0) (z^{\prime},\epsilon^{\prime})=(\epsilon^{2}Z,0) and then gain smoothness by applying a cylindrical blow-up (see Section 3.1). Using the cylindrical blow-up we replace the discontinuity line Σ \Sigma of the PWS system ( 2.2) with a half-cylinder and we show that near the canard trajectories on the top of the cylinder, we are in the framework of [14]. In [14] a very general smooth planar slow-fast model has been studied containing a normally attracting branch of singularities, a normally repelling branch of singularities and a turning point between them (an additional critical curve passing through the turning point is possible). One usually uses the results of [14] for specific slow-fast families by checking the assumptions in [14] (see for example [25, 32, 47]). We do the same here. In the second part (Section 3.2) we find the structure of the difference map of ( 2.1) near Γ x \Gamma_{x} using [14] and Proposition B.1 (Appendix B) near the hyperbolic edge of the cylinder. In the third part (Section 3.3) we establish a one-to-one correspondence between simple zeros of the slow divergence-integral ( 3.1) and simple zeros of the difference map by choosing a suitable control function λ = λ c ​ ( ϵ) \lambda=\lambda_{c}(\epsilon), following [2, 14].

### 3.1. Cylindrical blow-up

First we introduce the following scaling:

 | λ = λ 0 + ϵ ​ λ ~ \lambda=\lambda_{0}+\epsilon\widetilde{\lambda} |  |

where λ ~ ∼ 0 \widetilde{\lambda}\sim 0 is called a regular breaking parameter. We study the system Z Z given in ( 2.1) in nonsmooth limit ε → 0 \varepsilon\rightarrow 0 in the classical way, see e.g. [40]. We consider the extended fast-time system ( z ′, ϵ ′) = ( ϵ 2 ​ Z, 0) (z^{\prime},\epsilon^{\prime})=(\epsilon^{2}Z,0) and apply the cylindrical blow-up

(3.2) |  | ( r, ( y ¯, ϵ ¯)) ↦ { y = r 2 ​ y ¯, ϵ = r ​ ϵ ¯, \displaystyle(r,(\bar{y},\bar{\epsilon}))\mapsto\begin{cases}y&=r^{2}\bar{y},\\ \epsilon&=r\bar{\epsilon},\end{cases} |  |

with r ≥ 0 r\geq 0, ( y ¯, ϵ ¯) ∈ 𝕊 1 (\bar{y},\bar{\epsilon})\in\mathbb{S}^{1} and ϵ ¯ ≥ 0 \bar{\epsilon}\geq 0. Let F ¯ \overline{F} denote the vector field on ( x, r, ( y ¯, ϵ ¯)) (x,r,(\bar{y},\bar{\epsilon})), i.e. the pullback of ( ϵ 2 ​ Z, 0) (\epsilon^{2}Z,0) under ( 3.2). We then perform desingularization by division of the right hand side by ϵ ¯ 2 \bar{\epsilon}^{2}. In other words, it is F ^:= ϵ ¯ − 2 ​ F ¯ \widehat{F}:=\bar{\epsilon}^{-2}\overline{F} that we shall study. To study the dynamics of F ^ \widehat{F} in a neighborhood of the cylinder, we use different charts. Based upon Section 3.1.1 and Section 3.1.2, we illustrate the transformation and the properties of F ^ \widehat{F} in Fig. 4 (a).

Figure 4. The two consecutive blowup transformations. In (a): Under the assumptions (A1) - (A3) we gain smoothness of y = 0 y=0 at ϵ = 0 \epsilon=0 through a cylindrical blowup transformation. On the blow-up cylinder we find two critical sets C ¯ \overline{C} and H ¯ \overline{H}, the former being normally hyperbolic away from the intersection with H ¯ \overline{H}. The section S i S_{i}, i = 0, …, 3 i=0,\ldots,3 are used in the proof of Proposition 3.2. In (b): We blowup H ¯ \overline{H} through another cylindrical blowup transformation. In this way, we gain hyperbolicity of C ¯ \overline{C}. Hyperbolic directions are indicated by double-headed arrows whereas single headed arrows are slow or nonhyperbolic directions.

#### 3.1.1. Dynamics in the scaling chart ϵ ¯ = 1 \bar{\epsilon}=1

We consider the chart-specific coordinate y 2 y_{2} defined by y = ϵ 2 ​ y 2 y=\epsilon^{2}y_{2}, with ( x, y 2) (x,y_{2}) kept in a large compact subset of ℝ 2 \mathbb{R}^{2}, ϵ > 0 \epsilon>0 and ϵ ∼ 0 \epsilon\sim 0. Inserting this into the extended system ( z ′, ϵ ′) = ( ϵ 2 ​ Z, 0) (z^{\prime},\epsilon^{\prime})=(\epsilon^{2}Z,0) produces the following equations:

(3.3) |  | x ˙ \displaystyle\dot{x} | = ϵ 2 ​ ( X + ​ ( x, ϵ 2 ​ y 2, λ 0 + ϵ ​ λ ~) ​ ϕ ​ ( y 2) + X − ​ ( x, ϵ 2 ​ y 2, λ 0 + ϵ ​ λ ~) ​ ( 1 − ϕ ⁡ ( y 2))), \displaystyle=\epsilon^{2}\left(X_{+}(x,\epsilon^{2}y_{2},\lambda_{0}+\epsilon\widetilde{\lambda})\phi(y_{2})+X_{-}(x,\epsilon^{2}y_{2},\lambda_{0}+\epsilon\widetilde{\lambda})(1-\phi(y_{2}))\right), |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = Y + ​ ( x, ϵ 2 ​ y 2, λ 0 + ϵ ​ λ ~) ​ ϕ ​ ( y 2) + Y − ​ ( x, ϵ 2 ​ y 2, λ 0 + ϵ ​ λ ~) ​ ( 1 − ϕ ⁡ ( y 2)). \displaystyle=Y_{+}(x,\epsilon^{2}y_{2},\lambda_{0}+\epsilon\widetilde{\lambda})\phi(y_{2})+Y_{-}(x,\epsilon^{2}y_{2},\lambda_{0}+\epsilon\widetilde{\lambda})(1-\phi(y_{2})). |  |

When ϵ = 0 \epsilon=0, system ( 3.3) becomes

(3.4) |  | x ˙ \displaystyle\dot{x} | = 0, \displaystyle=0, |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = Y + ​ ( x, 0, λ 0) ​ ϕ ​ ( y 2) + Y − ​ ( x, 0, λ 0) ​ ( 1 − ϕ ⁡ ( y 2)). \displaystyle=Y_{+}(x,0,\lambda_{0})\phi(y_{2})+Y_{-}(x,0,\lambda_{0})(1-\phi(y_{2})). |  |

The critical set of ( 3.4) is given by the union of two critical manifolds:

 | H ¯:= { ( 0, y 2): y 2 ∈ ℝ } \overline{H}:=\{(0,y_{2}):y_{2}\in\mathbb{R}\} |  |

and the curve C ¯ \overline{C} given by

 | y 2 = ϕ − 1 ​ ( − Y − Y + − Y − ​ ( x, 0, λ 0)). y_{2}=\phi^{-1}\left(\frac{-Y_{-}}{Y_{+}-Y_{-}}(x,0,\lambda_{0})\right). |  |

Notice that at the point

 | p 0 = ( 0, ϕ − 1 ​ ( − Y − ′ Y + ′ − Y − ′ ​ ( 0, 0, λ 0))) p_{0}=\left(0,\phi^{-1}\left(\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}}(0,0,\lambda_{0})\right)\right) |  |

an intersection of H ¯ \overline{H} and C ¯ \overline{C} appears. All the singularities on H ¯ \overline{H} are nilpotent except for p 0 p_{0} which is linearly zero. In the rest of this section we show that the slow-fast system ( 3.3) satisfies Assumptions T0–T6 in [14] along the critical curve C ¯ \overline{C}. Then we can use [14, Theorem 4] and prove Proposition 3.2 in Section 3.2. Theorem 4 says that the leading term of the integral of divergence of the vector field ( 3.3), computed along canard orbits near C ¯ \overline{C} between ξ ⁡ ( x) < 0 \xi(x)<0 and x > 0 x>0, is I ⁡ ( x) ϵ 2 \frac{I(x)}{\epsilon^{2}} with I I defined in ( 3.1) (see for example the exponent of the exponential term in ( 3.10)). This term remains dominant in the expression for the difference map of ( 2.1) near Γ x \Gamma_{x}, see ( 3.8).

The singularities on C ¯ \overline{C} are normally attracting when x < 0 x<0, normally repelling when x > 0 x>0 and the slow dynamics X s ​ l ​ ( x, λ 0) X_{sl}(x,\lambda_{0}) – given in ( 2.5) – is regular, pointing from the attracting part to the repelling part of C ¯ \overline{C}. Thus, if we denote the vector field in ( 3.3) by F ^ S \widehat{F}_{S} and if M x M_{x} is any local C n C^{n} center manifold of F ^ S 1:= F ^ S + 0 ​ ∂ ∂ ϵ \widehat{F}_{S}^{1}:=\widehat{F}_{S}+0\frac{\partial}{\partial\epsilon} at normally hyperbolic singularity x ∈ C ¯ x\in\overline{C}, then 1 ϵ 2 ​ F ^ S 1 | M x \frac{1}{\epsilon^{2}}\widehat{F}_{S}^{1}|_{M_{x}} is a local flow box containing C ¯ \overline{C} and pointing from the left to the right. (The exponent 2 2 in the term ϵ 2 \epsilon^{2} is often called the order of degeneracy.) This implies that Assumptions T0–T2 of [14] are satisfied. It remains to show that ( 3.3) satisfies Assumptions T3–T6 of [14] in an ( ϵ, λ ~) (\epsilon,\widetilde{\lambda}) -uniform neighborhood of the turning point p 0 p_{0}. In order to do that, we have to blow up the degenerate line H ¯ = { x = 0 } \overline{H}=\{x=0\}, inside the slow-fast system ( 3.3), to a half-cylinder (see Fig. 4 (b)). For the sake of readability of Section 3, we prove that Assumptions T3–T6 are satisfied in Appendix A.

#### 3.1.2. Dynamics in the phase directional charts y ¯ = ± 1 \bar{y}=\pm 1

We keep x ∈ [μ −, μ +] x\in[\mu_{-},\mu_{+}] uniformly away from x = 0 x=0. In the chart y ¯ = − 1 \bar{y}=-1 associated with ( 3.2) and the chart-specific coordinates ( r 1, ϵ 1) (r_{1},\epsilon_{1}) such that ( y, ϵ) = ( − r 1 2, r 1 ​ ϵ 1) (y,\epsilon)=(-r_{1}^{2},r_{1}\epsilon_{1}) the extended system ( z ′, ϵ ′) = ( ϵ 2 ​ Z, 0) (z^{\prime},\epsilon^{\prime})=(\epsilon^{2}Z,0) becomes (after division by ϵ 1 2 > 0 \epsilon_{1}^{2}>0):

(3.5) |  | x ˙ \displaystyle\dot{x} | = r 1 2 ​ ( X + ​ ( x, − r 1 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ϕ − ​ ( ϵ 1 2) + X − ​ ( x, − r 1 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ( 1 − ϕ − ​ ( ϵ 1 2))), \displaystyle=r_{1}^{2}\left(X_{+}(x,-r_{1}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})\phi_{-}(\epsilon_{1}^{2})+X_{-}(x,-r_{1}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})(1-\phi_{-}(\epsilon_{1}^{2}))\right), |  |

 | r ˙ 1 \displaystyle\dot{r}_{1} | = − 1 2 ​ r 1 ​ ( Y + ​ ( x, − r 1 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ϕ − ​ ( ϵ 1 2) + Y − ​ ( x, − r 1 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ( 1 − ϕ − ​ ( ϵ 1 2))), \displaystyle=-\frac{1}{2}r_{1}\left(Y_{+}(x,-r_{1}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})\phi_{-}(\epsilon_{1}^{2})+Y_{-}(x,-r_{1}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})(1-\phi_{-}(\epsilon_{1}^{2}))\right), |  |

 | ϵ ˙ 1 \displaystyle\dot{\epsilon}_{1} | = 1 2 ​ ϵ 1 ​ ( Y + ​ ( x, − r 1 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ϕ − ​ ( ϵ 1 2) + Y − ​ ( x, − r 1 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ( 1 − ϕ − ​ ( ϵ 1 2))) \displaystyle=\frac{1}{2}\epsilon_{1}\left(Y_{+}(x,-r_{1}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})\phi_{-}(\epsilon_{1}^{2})+Y_{-}(x,-r_{1}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})(1-\phi_{-}(\epsilon_{1}^{2}))\right) |  |

where ϕ − \phi_{-} is defined in (A3). The edge of the cylinder, corresponding to r 1 = ϵ 1 = 0 r_{1}=\epsilon_{1}=0, consists of semi-hyperbolic singularities of ( 3.5). The eigenvalues of the linearization at ( x, 0, 0) (x,0,0) are given by ( 0, − Y − ​ ( x, 0, λ 0) 2, Y − ​ ( x, 0, λ 0) 2) (0,-\frac{Y_{-}(x,0,\lambda_{0})}{2},\frac{Y_{-}(x,0,\lambda_{0})}{2}). Let’s recall that Y − ​ ( x, 0, λ 0) < 0 Y_{-}(x,0,\lambda_{0})<0 when x > 0 x>0 and Y − ​ ( x, 0, λ 0) > 0 Y_{-}(x,0,\lambda_{0})>0 when x < 0 x<0. The form of the transition map near the edge of the cylinder, with x < 0 x<0 (resp. x > 0 x>0), by following the orbits of ( 3.5) in forward (resp. backward) time is given in Proposition B.1 in Appendix B.

Although the phase directional chart y ¯ = 1 \bar{y}=1 is not relevant to the present study, we include it here for sake of completeness. Writing ( y, ϵ) = ( r 2 2, r 2 ​ ϵ 2) (y,\epsilon)=(r_{2}^{2},r_{2}\epsilon_{2}), the extended system changes (after division by ϵ 2 2 > 0 \epsilon_{2}^{2}>0) into

(3.6) |  | x ˙ \displaystyle\dot{x} | = r 2 2 ​ ( X + ​ ( x, r 2 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ϕ + ​ ( ϵ 2 2) + X − ​ ( x, r 2 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ( 1 − ϕ + ​ ( ϵ 2 2))), \displaystyle=r_{2}^{2}\left(X_{+}(x,r_{2}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})\phi_{+}(\epsilon_{2}^{2})+X_{-}(x,r_{2}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})(1-\phi_{+}(\epsilon_{2}^{2}))\right), |  |

 | r ˙ 2 \displaystyle\dot{r}_{2} | = 1 2 ​ r 2 ​ ( Y + ​ ( x, r 2 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ϕ + ​ ( ϵ 2 2) + Y − ​ ( x, r 2 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ( 1 − ϕ + ​ ( ϵ 2 2))), \displaystyle=\frac{1}{2}r_{2}\left(Y_{+}(x,r_{2}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})\phi_{+}(\epsilon_{2}^{2})+Y_{-}(x,r_{2}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})(1-\phi_{+}(\epsilon_{2}^{2}))\right), |  |

 | ϵ ˙ 2 \displaystyle\dot{\epsilon}_{2} | = − 1 2 ​ ϵ 2 ​ ( Y + ​ ( x, r 2 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ϕ + ​ ( ϵ 2 2) + Y − ​ ( x, r 2 2, λ 0 + r 1 ​ ϵ 1 ​ λ ~) ​ ( 1 − ϕ + ​ ( ϵ 2 2))), \displaystyle=-\frac{1}{2}\epsilon_{2}\left(Y_{+}(x,r_{2}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})\phi_{+}(\epsilon_{2}^{2})+Y_{-}(x,r_{2}^{2},\lambda_{0}+r_{1}\epsilon_{1}\widetilde{\lambda})(1-\phi_{+}(\epsilon_{2}^{2}))\right), |  |

with ϕ + \phi_{+} introduced in (A3). The study of ( 3.6) near r 2 = ϵ 2 = 0 r_{2}=\epsilon_{2}=0 is similar to the study of ( 3.5) near r 1 = ϵ 1 = 0 r_{1}=\epsilon_{1}=0. The points ( x, 0, 0) (x,0,0), for x ≠ 0 x\neq 0, are semi-hyperbolic singularities of ( 3.6) with eigenvalues ( 0, Y + ​ ( x, 0, λ 0) 2, − Y + ​ ( x, 0, λ 0) 2) (0,\frac{Y_{+}(x,0,\lambda_{0})}{2},-\frac{Y_{+}(x,0,\lambda_{0})}{2}).

### 3.2. The difference map

Denote by ξ − ​ ( y) < 0 \xi_{-}(y)<0 (resp. ξ + ​ ( y) > 0 \xi_{+}(y)>0), with y < 0 y<0, the x x -value of the intersection with the x x -axis of the forward (resp. backward) flow of ( 0, y) (0,y) following Z − Z_{-}, for λ = λ 0 \lambda=\lambda_{0}. Let μ 1 < μ 2 < 0 \mu_{1}<\mu_{2}<0 be arbitrary and fixed real numbers such that ξ + ​ ( [μ 1, μ 2]) ⊂] 0, μ + [\xi_{+}([\mu_{1},\mu_{2}])\subset]0,\mu_{+}[(and hence ξ − ​ ( [μ 1, μ 2]) ⊂] μ −, 0 [\xi_{-}([\mu_{1},\mu_{2}])\subset]\mu_{-},0[by 4). We define a section S 0 ⊂ { x = 0 } S_{0}\subset\{x=0\} parametrized by y ∈ [μ 1, μ 2] y\in[\mu_{1},\mu_{2}] and ϵ ∈ [0, ϵ 0] \epsilon\in[0,\epsilon_{0}] where ϵ 0 \epsilon_{0} is a small positive constant. We also define a section S 3 ⊂ { x = 0 } S_{3}\subset\{x=0\}, parametrized by y 2 ∼ ϕ − 1 ​ ( − Y − ′ Y + ′ − Y − ′ ​ ( 0, 0, λ 0)) y_{2}\sim\phi^{-1}\left(\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}}(0,0,\lambda_{0})\right) and ϵ ∈ [0, ϵ 0] \epsilon\in[0,\epsilon_{0}], where the coordinate y 2 y_{2} is introduced in Section 3.1.1. We denote by Δ − \Delta_{-} (resp. Δ + \Delta_{+}) the transition map between S 0 S_{0} and S 3 S_{3} following the trajectories of the blown-up vector field F ^ \widehat{F} in forward (resp. backward) time. It is clear that the zeros of the difference map

(3.7) |  | y 2 = Δ ⁡ ( y, ϵ, λ ~):= Δ − ​ ( y, ϵ, λ ~) − Δ + ​ ( y, ϵ, λ ~), y_{2}=\Delta(y,\epsilon,\widetilde{\lambda}):=\Delta_{-}(y,\epsilon,\widetilde{\lambda})-\Delta_{+}(y,\epsilon,\widetilde{\lambda}), |  |

with ϵ > 0 \epsilon>0, correspond to periodic orbits of ( 2.1).

###### Proposition 3.2.

The transition maps Δ ± \Delta_{\pm} have the following form:

(3.8) |  | Δ ± ​ ( y, ϵ, λ ~) = f ± ​ ( ϵ, λ ~) − exp ⁡ 1 ϵ 2 ​ ( I ± ​ ( y) + o ± ​ ( 1)), y ∈ [μ 1, μ 2], ( ϵ, λ ~) ∼ ( 0, 0), \Delta_{\pm}(y,\epsilon,\widetilde{\lambda})=f_{\pm}(\epsilon,\widetilde{\lambda})-\exp\frac{1}{\epsilon^{2}}\left(I_{\pm}(y)+o_{\pm}(1)\right),\ y\in[\mu_{1},\mu_{2}],\ (\epsilon,\widetilde{\lambda})\sim(0,0), |  |

where f ± f_{\pm} are smooth functions, ( f − − f +) ​ ( 0, 0) = 0 (f_{-}-f_{+})(0,0)=0, ∂ ( f − − f +) ∂ λ ~ ​ ( 0, 0) ≠ 0 \frac{\partial(f_{-}-f_{+})}{\partial\widetilde{\lambda}}(0,0)\neq 0, o ± ​ ( 1) o_{\pm}(1) tend to zero as ϵ → 0 \epsilon\to 0, uniformly in ( y, λ ~) (y,\widetilde{\lambda}), and where

(3.9) |  | I ± ​ ( y) = \displaystyle I_{\pm}(y)= | ∫ ξ ± ​ ( y) 0 ( Y + − Y −) 2 det ​ Z ​ ( x, 0, λ 0) ​ ϕ ′ ​ ( ϕ − 1 ​ ( − Y − Y + − Y − ​ ( x, 0, λ 0))) ​ d x < 0. \displaystyle\int_{\xi_{\pm}(y)}^{0}\frac{(Y_{+}-Y_{-})^{2}}{\textnormal{det}\,Z}(x,0,\lambda_{0})\phi^{\prime}\left(\phi^{-1}\left(\frac{-Y_{-}}{Y_{+}-Y_{-}}(x,0,\lambda_{0})\right)\right)dx<0. |  |

###### Proof.

We treat the forward transition map Δ − \Delta_{-} (the backward transition map Δ + \Delta_{+} can be studied in similar fashion). We split up the forward transition map Δ − \Delta_{-} between S 0 S_{0} and S 3 S_{3} in three parts (see sketch of sections in Fig. 4 (a)):
(a) We define a section S 1 ⊂ { r 1 = r 10 } S_{1}\subset\{r_{1}=r_{10}\} parametrized by x ∈ J ⊂ [μ −, 0 [x\in J\subset[\mu_{-},0[, J J being a segment, and ϵ 1 ∈ [0, ϵ 0 r 10] \epsilon_{1}\in[0,\frac{\epsilon_{0}}{r_{10}}] where r 10 > 0 r_{10}>0 is a small constant and ( x, r 1, ϵ 1) (x,r_{1},\epsilon_{1}) are the coordinates of ( 3.5). The segment J J is chosen large enough such that the transition map x = Δ 01 ​ ( y, ϵ, λ ~) x=\Delta_{01}(y,\epsilon,\widetilde{\lambda}) between S 0 S_{0} and S 1 S_{1} is well defined. Notice that ϵ 1 = ϵ r 10 \epsilon_{1}=\frac{\epsilon}{r_{10}}. Since Z − Z_{-} has no singularities between S 0 S_{0} and S 1 S_{1} and the passage between S 0 S_{0} and S 1 S_{1} is located outside a fixed neighborhood of y = 0 y=0, it is clear that Δ 01 \Delta_{01} is smooth in ( y, ϵ, λ ~) (y,\epsilon,\widetilde{\lambda}) (see also Lemma 2.1).
(b) Define a section S 2 ⊂ { ϵ 1 = ϵ 10 } S_{2}\subset\{\epsilon_{1}=\epsilon_{10}\} parametrized by x ¯ ∈ J ¯ ⊂ [μ −, 0 [\bar{x}\in\bar{J}\subset[\mu_{-},0[, J ¯ \bar{J} being a segment and r ¯ 1 ∈ [0, ϵ 0 ϵ 10] \bar{r}_{1}\in[0,\frac{\epsilon_{0}}{{\epsilon}_{10}}], with a small positive constant ϵ 10 \epsilon_{10}. Following Proposition B.1, the transition map x ¯ = Δ 12 ​ ( x, ϵ 1, λ ~) \bar{x}=\Delta_{12}(x,\epsilon_{1},\widetilde{\lambda}) between S 1 S_{1} and S 2 S_{2} w.r.t. ( 3.5) can be written as

 | Δ 12 ​ ( x, ϵ r 10, λ ~) = g 12 ​ ( x, λ ~) + O ⁡ ( ϵ ​ log ⁡ ϵ − 1), ϵ → 0. \Delta_{12}(x,\frac{\epsilon}{r_{10}},\widetilde{\lambda})=g_{12}(x,\widetilde{\lambda})+O(\epsilon\log\epsilon^{-1}),\ \epsilon\to 0. |  |

Notice that r ¯ 1 = r 10 ​ ϵ 1 ϵ 10 = ϵ ϵ 10 \bar{r}_{1}=\frac{r_{10}\epsilon_{1}}{\epsilon_{10}}=\frac{\epsilon}{\epsilon_{10}}.
(c) The transition map y 2 = Δ 23 ​ ( x ¯, ϵ, λ ~) y_{2}=\Delta_{23}(\bar{x},\epsilon,\widetilde{\lambda}) between S 2 S_{2} and S 3 S_{3} following the trajectories of the smooth slow-fast system ( 3.3) has the following form (see [14, Theorem 4]):

(3.10) |  | Δ 23 ​ ( x ¯, ϵ, λ ~) = f − ​ ( ϵ, λ ~) − exp ⁡ 1 ϵ 2 ​ ( I ¯ ​ ( x ¯) + κ 1 ​ ( x ¯, ϵ, λ ~) + κ 2 ​ ( ϵ, λ ~) ​ ϵ 2 ​ log ⁡ ϵ) \Delta_{23}(\bar{x},\epsilon,\widetilde{\lambda})=f_{-}(\epsilon,\widetilde{\lambda})-\exp\frac{1}{\epsilon^{2}}\left(\bar{I}(\bar{x})+\kappa_{1}(\bar{x},\epsilon,\widetilde{\lambda})+\kappa_{2}(\epsilon,\widetilde{\lambda})\epsilon^{2}\log\epsilon\right) |  |

where f − f_{-}, κ 1 \kappa_{1} and κ 2 \kappa_{2} are smooth, including at ϵ = 0 \epsilon=0, κ 1 = O ⁡ ( ϵ) \kappa_{1}=O(\epsilon) and I ¯ ​ ( x ¯) < 0 \bar{I}(\bar{x})<0 is the slow divergence-integral of the form ( 3.9) computed between x ¯ \bar{x} and 0 0. We have the negative sign in front of the exponential term due to the chosen parametrization of S 2 S_{2} and S 3 S_{3}.

Combining (a), (b) and (c), we obtain ( 3.8). We use that g 12 ​ ( Δ 01 ​ ( y, 0, 0), 0) = ξ − ​ ( y) g_{12}(\Delta_{01}(y,0,0),0)=\xi_{-}(y). Since Assumption T6 of [14] is satisfied (see Section A), the function f − − f + f_{-}-f_{+} has the property given in Proposition 3.2, where f + f_{+} is obtained in a similar way by studying the backward transition map Δ + \Delta_{+}. ∎

### 3.3. Conclusions

Suppose that I ⁡ ( x) I(x), defined in ( 3.1), has exactly k − 1 k-1 simple zeros x 1 < ⋯ < x k − 1 x_{1}<\dots<x_{k-1} in ] 0, μ + []0,\mu_{+}[. Let the segment [μ 1, μ 2] [\mu_{1},\mu_{2}] from Section 3.2 be large enough such that x 1, …, x k − 1 ∈ ξ + ​ ( [μ 1, μ 2]) x_{1},\dots,x_{k-1}\in\xi_{+}([\mu_{1},\mu_{2}]). Using the property of f − − f + f_{-}-f_{+} given in Proposition 3.2 ( λ ~ \widetilde{\lambda} is the breaking parameter) and the implicit function theorem, we find a smooth function λ ~ = λ ~ c ​ ( ϵ) \widetilde{\lambda}=\widetilde{\lambda}_{c}(\epsilon), with λ ~ c ​ ( 0) = 0 \widetilde{\lambda}_{c}(0)=0, such that ( f − − f +) ​ ( ϵ, λ ~ c ​ ( ϵ)) = 0 (f_{-}-f_{+})(\epsilon,\widetilde{\lambda}_{c}(\epsilon))=0 for all small ϵ ≥ 0 \epsilon\geq 0. Now, the difference map Δ \Delta, given in ( 3.7), can be written as

 | Δ ⁡ ( y, ϵ, λ ~ c ​ ( ϵ)) = exp ⁡ 1 ϵ 2 ​ ( I + ​ ( y) + o + ​ ( 1)) − exp ⁡ 1 ϵ 2 ​ ( I − ​ ( y) + o − ​ ( 1)) \Delta(y,\epsilon,\widetilde{\lambda}_{c}(\epsilon))=\exp\frac{1}{\epsilon^{2}}\left(I_{+}(y)+o_{+}(1)\right)-\exp\frac{1}{\epsilon^{2}}\left(I_{-}(y)+o_{-}(1)\right) |  |

for new functions o ± ​ ( 1) o_{\pm}(1) tending to zero as ϵ → 0 \epsilon\to 0, uniformly in y y. This implies that the zeros of Δ ⁡ ( y, ϵ, λ ~ c ​ ( ϵ)) \Delta(y,\epsilon,\widetilde{\lambda}_{c}(\epsilon)) w.r.t. y y are solutions of the equation

(3.11) |  | I − ​ ( y) − I + ​ ( y) + o ⁡ ( 1) = 0, I_{-}(y)-I_{+}(y)+o(1)=0, |  |

where o ⁡ ( 1) → 0 o(1)\to 0 when ϵ → 0 \epsilon\to 0 (uniformly in y y). Notice that ξ ⁡ ( ξ + ​ ( y)) = ξ − ​ ( y) \xi(\xi_{+}(y))=\xi_{-}(y), and therefore I − ​ ( y) − I + ​ ( y) = I ⁡ ( ξ + ​ ( y)) I_{-}(y)-I_{+}(y)=I(\xi_{+}(y)). We conclude that y 1, …, y k − 1 y_{1},\dots,y_{k-1}, defined by ξ + ​ ( y i) = x i \xi_{+}(y_{i})=x_{i}, are simple zeros of I − − I + I_{-}-I_{+} ( ξ + \xi_{+} is a diffeomorphism). Using the implicit function theorem once more, we find that ( 3.11) has k − 1 k-1 simple solutions for each small ϵ > 0 \epsilon>0, perturbing from y 1, …, y k − 1 y_{1},\dots,y_{k-1}. They correspond to hyperbolic canard limit cycles of Z ⁡ ( z, ϕ ⁡ ( y ​ ϵ − 2), λ 0 + ϵ ​ λ ~ c ​ ( ϵ)) Z(z,\phi(y\epsilon^{-2}),\lambda_{0}+\epsilon\widetilde{\lambda}_{c}(\epsilon)) close to Γ x 1, …, Γ x k − 1 \Gamma_{x_{1}},\dots,\Gamma_{x_{k-1}}. It is not difficult to see that using the control function λ ~ c ​ ( ϵ) \widetilde{\lambda}_{c}(\epsilon) we can construct one extra hyperbolic limit cycle, Hausdorff close to Γ x k \Gamma_{x_{k}}, with x k ∈] x k − 1, μ + [x_{k}\in]x_{k-1},\mu_{+}[, surrounding the k − 1 k-1 limit cycles (see [17, 19]). This completes the proof of Theorem 3.1.

###### Remark 3.3.

Notice that the parameter λ \lambda in our model ( 2.1) is one-dimensional and we don’t need additional parameters in the statement of Theorem 3.1 to prove Theorem 1.1. Of course Theorem 3.1 remains true if Z ± Z_{\pm} depend smoothly on finite-dimensional extra parameter.

###### Remark 3.4.

Suppose that the slow divergence-integral I I has a simple zero at x = x 0 ∈] 0, μ +] x=x_{0}\in]0,\mu_{+}]. Then for each small ϵ > 0 \epsilon>0, the λ \lambda -family Z ⁡ ( z, ϕ ⁡ ( y ​ ϵ − 2), λ) Z(z,\phi(y\epsilon^{-2}),\lambda) undergoes a saddle-node bifurcation of limit cycles near Γ x 0 \Gamma_{x_{0}} as we vary λ ∼ λ 0 \lambda\sim\lambda_{0}. Notice that the parameter λ \lambda in this result–as opposed to Theorem 3.1 with unbroken λ \lambda – becomes broken. If the slow divergence-integral I I has a zero of multiplicity l ≥ 1 l\geq 1 at x = x 0 x=x_{0}, then Z ⁡ ( z, ϕ ⁡ ( y ​ ϵ − 2), λ) Z(z,\phi(y\epsilon^{-2}),\lambda) can have at most l + 1 l+1 limit cycles (counting multiplicity) Hausdorff close to Γ x 0 \Gamma_{x_{0}} for each small ϵ > 0 \epsilon>0 and λ ∼ λ 0 \lambda\sim\lambda_{0}, and, if I ⁡ ( x 0) < 0 I(x_{0})<0 (resp. I ⁡ ( x 0) > 0 I(x_{0})>0), then at most one limit cycle can be born from Γ x 0 \Gamma_{x_{0}}. The limit cycle, if it exists, is hyperbolic and attracting (resp. repelling). These results can be proved by using Proposition 3.2. The proof is similar to the proof of [19, Theorem 4.3].

## 4. Proof of Theorem 1.1

To prove Theorem 1.1 we now use Theorem 3.1. We consider Z ± ​ ( ⋅, λ) Z_{\pm}(\cdot,\lambda) and suppose that 4 holds with λ 0 = 0 \lambda_{0}=0. Moreover, we will suppose that Z − Z_{-} is invariant under the symmetry ( x, t) ↦ ( − x, − t) (x,t)\mapsto(-x,-t) for λ = 0 \lambda=0:

1. (5)

Let Γ ⁡ ( x, y) = ( − x, y) \Gamma(x,y)=(-x,y) then we assume D ​ Γ − 1 ​ ( Z − ∘ Γ) = − Z − D\Gamma^{-1}(Z_{-}\circ\Gamma)=-Z_{-} for λ = 0 \lambda=0.

Based upon the following simple result, this leads to a significant simplification of the calculations that follow.

###### Lemma 4.1.

Assume that assumption 5 holds. Then ξ ⁡ ( x) = − x \xi(x)=-x, recall ( 3.1), and I ⁡ ( x) I(x) has a smooth extension onto a neighborhood of x = 0 x=0 which is an odd function in x x.

###### Proof.

From the symmetry, we have that if ( ξ − ​ ( y), 0) (\xi_{-}(y),0) is the first intersection with Σ \Sigma by the forward flow of ( 0, y) (0,y) then ( ξ + ​ ( y), 0) (\xi_{+}(y),0) with ξ + ​ ( y) = − ξ − ​ ( y) \xi_{+}(y)=-\xi_{-}(y) is the first intersection with Σ \Sigma by the backward flow. ∎

In the following, while we continue to use () ′ ()^{\prime} to denote the partial derivative with respect to x x evaluated at ( x, y, λ) = ( 0, 0, 0) (x,y,\lambda)=(0,0,0), we will also use () ′′ ()^{\prime\prime} to indicate the second order partial derivative with respect to x x also evaluated at ( x, y, λ) = ( 0, 0, 0) (x,y,\lambda)=(0,0,0).

We then proceed to Taylor expand I ⁡ ( x) I(x) around x = 0 x=0. Let y 2 ​ c = ϕ − 1 ​ ( − Y − ′ Y + ′ − Y − ′) y_{2c}=\phi^{-1}\left(\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}}\right) and recall that

 | det ​ Z ​ ( x, 0, 0) = ( X − ​ Y + − X + ​ Y −) ​ ( x, 0, 0). \text{det}\,Z(x,0,0)=(X_{-}Y_{+}-X_{+}Y_{-})(x,0,0). |  |

Since Z − Z_{-} is assumed to be Γ \Gamma -symmetric, see 5, we have that x ↦ X − ​ ( x, 0, 0) x\mapsto X_{-}(x,0,0) is even whereas x ↦ Y − ​ ( x, 0, 0) x\mapsto Y_{-}(x,0,0) is odd. Consequently, X − ′ = Y − ′′ = 0 X_{-}^{\prime}=Y_{-}^{\prime\prime}=0 and

 | det ​ Z ′′ = X − ​ Y + ′′ − 2 ​ X + ′ ​ Y − ′. \displaystyle\text{det}\,Z^{\prime\prime}=X_{-}Y_{+}^{\prime\prime}-2X_{+}^{\prime}Y_{-}^{\prime}. |  |

Then from [7, Eq. 4.13] we have that

 | I ⁡ ( x) \displaystyle I(x) | = 2 3 ​ x 3 ​ ( 1 2 ​ ( Y + ′ − Y − ′) ​ ( Y + ′′ det ​ Z ′ − ( Y + ′ − Y − ′) ​ det ​ Z ′′ 2 ​ ( det ​ Z ′) 2) ​ ϕ ′ ​ ( y 2 ​ c) + ϕ ′′ ​ ( y 2 ​ c) ϕ ′ ​ ( y 2 ​ c) ​ Y + ′′ ​ Y − ′ 2 ​ det ​ Z ′) + 𝒪 ⁡ ( x 5), \displaystyle=\frac{2}{3}x^{3}\bigg(\frac{1}{2}(Y_{+}^{\prime}-Y_{-}^{\prime})\left(\frac{Y_{+}^{\prime\prime}}{\text{det}\,Z^{\prime}}-\frac{(Y_{+}^{\prime}-Y_{-}^{\prime})\text{det}\,Z^{\prime\prime}}{2(\text{det}\,Z^{\prime})^{2}}\right)\phi^{\prime}(y_{2c})+\frac{\phi^{\prime\prime}(y_{2c})}{\phi^{\prime}(y_{2c})}\frac{Y_{+}^{\prime\prime}Y_{-}^{\prime}}{2\text{det}\,Z^{\prime}}\bigg)+\mathcal{O}(x^{5}), |  |

under the assumption 5, recall also 4 and ( 2.11).

The regularization function satisfies assumptions (A1) - (A3). In particular, it is invertible and ϕ ′ > 0 \phi^{\prime}>0, but (A1) - (A3) do not impose further restrictions on the higher order partial derivatives ϕ \phi at any point. Suppose:

1. (6)

Y + ′′ ≠ 0 Y_{+}^{\prime\prime}\neq 0.

It then follows (see also 4 and ( 2.11)) that I ( 3) ​ ( 0) I^{(3)}(0) can have either sign, depending on ϕ ′′ ​ ( y 2 ​ c) \phi^{\prime\prime}(y_{2c}). In fact, seeing that I ( 3) ​ ( 0) I^{(3)}(0) depends upon ϕ ′′ ​ ( y 2 ​ c) \phi^{\prime\prime}(y_{2c}) in an affine way – with a coefficient of ϕ ′′ ​ ( y 2 ​ c) \phi^{\prime\prime}(y_{2c}) that is nonzero – there is a unique value of ϕ ′′ ​ ( y 2 ​ c) \phi^{\prime\prime}(y_{2c}) (for every ϕ ′ ​ ( y 2 ​ c) > 0 \phi^{\prime}(y_{2c})>0) for which I ( 3) ​ ( 0) = 0 I^{(3)}(0)=0. The following lemma allow us to generalize this result to any odd derivative of I I at x = 0 x=0.

###### Lemma 4.2.

I ( 2 ​ k + 1) ​ ( 0) I^{(2k+1)}(0) for k ∈ ℕ k\in\mathbb{N} depends upon ϕ ′ ​ ( y 2 ​ c), …, ϕ ( 2 ​ k) ​ ( y 2 ​ c) \phi^{\prime}(y_{2c}),\ldots,\phi^{(2k)}(y_{2c}) and takes the following form:

(4.1) |  | I ( 2 ​ k + 1) ​ ( 0) = J 2 ​ k − 1 ​ ( ϕ ′ ​ ( y 2 ​ c), …, ϕ ( 2 ​ k − 1) ​ ( y 2 ​ c)) + 1 ϕ ′ ​ ( y 2 ​ c) 2 ​ k − 1 ​ C 2 ​ k ​ ϕ ( 2 ​ k) ​ ( y 2 ​ c), \displaystyle I^{(2k+1)}(0)=J_{2k-1}(\phi^{\prime}(y_{2c}),\ldots,\phi^{(2k-1)}(y_{2c}))+\frac{1}{\phi^{\prime}(y_{2c})^{2k-1}}C_{2k}\phi^{(2k)}(y_{2c}), |  |

where J 2 ​ k − 1: ℝ + × ℝ × ⋯ × ℝ ⏟ 2 ​ k − 2 ​ copies → ℝ J_{2k-1}:\mathbb{R}_{+}\times\underbrace{\mathbb{R}\times\cdots\times\mathbb{R}}_{2k-2\,\textnormal{copies}}\rightarrow\mathbb{R} is a smooth function and where

(4.2) |  | C 2 ​ k = 4 ​ k ​ ( Y + ′ − Y − ′) 2 det ​ Z ′ ​ ( Y + ′′ ​ Y − ′ 2 ​ ( Y + ′ − Y − ′) 2) 2 ​ k − 1. \displaystyle C_{2k}=\frac{4k(Y_{+}^{\prime}-Y_{-}^{\prime})^{2}}{\textnormal{det}Z^{\prime}}\left(\frac{Y_{+}^{\prime\prime}Y_{-}^{\prime}}{2(Y_{+}^{\prime}-Y_{-}^{\prime})^{2}}\right)^{2k-1}. |  |

In particular, C 2 ​ k ≠ 0 C_{2k}\neq 0 whenever assumption 4 and 6 hold.

###### Proof.

For simplicity write

 | g ⁡ ( x) = ϕ − 1 ​ ( − Y − Y + − Y − ​ ( x, 0, 0)), h ⁡ ( x) = ( Y + − Y −) 2 det ​ Z ​ ( x, 0, 0). \displaystyle g(x)=\phi^{-1}\left(\frac{-Y_{-}}{Y_{+}-Y_{-}}(x,0,0)\right),\quad h(x)=\frac{(Y_{+}-Y_{-})^{2}}{\text{det}\,Z}(x,0,0). |  |

Then the integrand of I ⁡ ( x) I(x) is

 | i ⁡ ( u):= h ⁡ ( u) ​ ϕ ′ ​ ( g ⁡ ( u)). i(u):=h(u)\phi^{\prime}(g(u)). |  |

Notice that g g and h h both have “ 0 / 0 0/0 ” at x = 0 x=0, but each has a smooth extension to x = 0 x=0 due to the assumption of the two-fold by L’Hospital, recall also Proposition 2.3. In particular,

 | g ⁡ ( 0) = y 2 ​ c:= ϕ − 1 ​ ( − Y − ′ Y + ′ − Y − ′). \displaystyle g(0)=y_{2c}:=\phi^{-1}\left(\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}}\right). |  |

Moreover,

 | g ′ ​ ( 0) = 1 ϕ ′ ​ ( y 2 ​ c) ​ Y + ′′ ​ Y − ′ 2 ​ ( Y + ′ − Y − ′) 2, \displaystyle g^{\prime}(0)=\frac{1}{\phi^{\prime}(y_{2c})}\frac{Y_{+}^{\prime\prime}Y_{-}^{\prime}}{2(Y_{+}^{\prime}-Y_{-}^{\prime})^{2}}, |  |

using assumption 6.

In the same way, h ⁡ ( 0) = 0 h(0)=0 and

 | h ′ ​ ( 0) = ( Y + ′ − Y − ′) 2 det ​ Z ′. \displaystyle h^{\prime}(0)=\frac{(Y_{+}^{\prime}-Y_{-}^{\prime})^{2}}{\text{det}\,Z^{\prime}}. |  |

We compute the partial derivatives of i ⁡ ( x) i(x) of even degree using the Faá di Bruno rule:

(4.3) |  | i ( 2 ​ k) ​ ( 0) = ∑ m = 0 2 ​ k − 1 ( 2 ​ k m) ​ h ( 2 ​ k − m) ​ ( 0) ​ ∑ n = 1 m ϕ ( n + 1) ​ ( y 2 ​ c) ​ B m, n ​ ( g ′ ​ ( 0), …, g ( m − n + 1) ​ ( 0)), \displaystyle i^{(2k)}(0)=\sum_{m=0}^{2k-1}\begin{pmatrix}2k\\ m\end{pmatrix}h^{(2k-m)}(0)\sum_{n=1}^{m}\phi^{(n+1)}(y_{2c})B_{m,n}(g^{\prime}(0),\ldots,g^{(m-n+1)}(0)), |  |

where B m, n B_{m,n} are the Bell polynomials. Here we have used that h ⁡ ( 0) = 0 h(0)=0. Each g ( l) ​ ( 0) g^{(l)}(0) can be written in terms of ϕ ′ ​ ( y 2 ​ c), …, ϕ ( l) ​ ( y 2 ​ c) \phi^{\prime}(y_{2c}),\ldots,\phi^{(l)}(y_{2c}) (as well as the partial derivatives of Y ± Y_{\pm}). This follows from the rule of inverse differentiation. To show the explicit expression for the coefficient of ϕ ( 2 ​ k) ​ ( y 2 ​ c) \phi^{(2k)}(y_{2c}), including the expression for C 2 ​ k C_{2k}, we consider the term in ( 4.3) with n = m = 2 ​ k − 1 n=m=2k-1:

 | ( 2 ​ k 2 ​ k − 1) ​ h ′ ​ ( 0) ​ ϕ ( 2 ​ k) ​ ( y 2 ​ c) ​ B 2 ​ k − 1, 2 ​ k − 1 ​ ( g ′ ​ ( 0)) = 2 ​ k ​ h ′ ​ ( 0) ​ ϕ ( 2 ​ k) ​ ( y 2 ​ c) ​ g ′ ​ ( 0) 2 ​ k − 1 \displaystyle\begin{pmatrix}2k\\ 2k-1\end{pmatrix}h^{\prime}(0)\phi^{(2k)}(y_{2c})B_{2k-1,2k-1}(g^{\prime}(0))=2kh^{\prime}(0)\phi^{(2k)}(y_{2c})g^{\prime}(0)^{2k-1} |  |

using that B n, n ​ ( x) = x n B_{n,n}(x)=x^{n}. By the Leibniz integral rule, the result – including the stated properties of J 2 ​ k − 1 J_{2k-1} – then follows. ∎

We now have the following: If we assume 6 then for each k ∈ ℕ k\in\mathbb{N} there is a unique value:

(4.4) |  | − C 2 ​ k − 1 ​ J 2 ​ k − 1 ​ ( ϕ ′ ​ ( y 2 ​ c), …, ϕ ( 2 ​ k − 1) ​ ( y 2 ​ c)) ​ ϕ ′ ​ ( y 2 ​ c) 2 ​ k − 1, \displaystyle-C_{2k}^{-1}J_{2k-1}(\phi^{\prime}(y_{2c}),\ldots,\phi^{(2k-1)}(y_{2c}))\phi^{\prime}(y_{2c})^{2k-1}, |  |

of ϕ ( 2 ​ k) ​ ( y 2 ​ c) \phi^{(2k)}(y_{2c}) (for fixed values of the derivatives of lower order ϕ ′ ​ ( y 2 ​ c), …, ϕ ( 2 ​ k − 1) ​ ( y 2 ​ c) \phi^{\prime}(y_{2c}),\ldots,\phi^{(2k-1)}(y_{2c})) such that I ( 2 ​ k + 1) ​ ( 0) = 0 I^{(2k+1)}(0)=0.

We can then prove the following result.

###### Theorem 4.3.

Suppose that 6 holds. Then for each k ∈ ℕ k\in\mathbb{N} there is a regularization function ϕ k \phi_{k} satisfying (A1) - (A3) so that I ⁡ ( x) I(x) has k − 1 k-1 simple positive roots.

###### Proof.

For each k ∈ ℕ k\in\mathbb{N}, we first put Φ 1 ( 2 ​ k) = 1 \Phi_{1}^{(2k)}=1 and define the numbers Φ 1 ( 2 ​ i) \Phi_{1}^{(2i)}, i = 1, …, k − 1 i=1,\ldots,k-1 so that the k − 1 k-1 degree polynomial

(4.5) |  | P k − 1 ​ ( x 2) = Φ 1 ( 2) + ⋯ + Φ 1 ( 2 ​ ( k − 1)) ​ x 2 k − 2 + x 2 k − 1, \displaystyle P_{k-1}(x_{2})=\Phi_{1}^{(2)}+\cdots+\Phi_{1}^{(2(k-1))}x_{2}^{k-2}+x_{2}^{k-1}, |  |

has k − 1 k-1 simple roots at the first k − 1 k-1 integers:

(4.6) |  | P k − 1 ​ ( 1) = ⋯ = P k − 1 ​ ( k − 1) = 0. \displaystyle P_{k-1}(1)=\cdots=P_{k-1}(k-1)=0. |  |

Then fix ϕ \phi as any regularization function. Given ϕ ′ ​ ( y 2 ​ c) > 0 \phi^{\prime}(y_{2c})>0 and y 2 ​ c = ϕ − 1 ​ ( − Y − ′ Y + ′ − Y − ′) ∈ ℝ y_{2c}=\phi^{-1}\left(\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}}\right)\in\mathbb{R}, as well as Φ 1 ( 2 ​ i) \Phi_{1}^{(2i)}, i = 1, …, k i=1,\ldots,k, defined above, we proceed to define for each δ > 0 \delta>0 the function ψ k: ℝ → ℝ \psi_{k}:\mathbb{R}\rightarrow\mathbb{R} as the polynomial of degree (at most) 2 ​ k 2k with

 | ψ k ( y 2 ​ c) = − Y − ′ Y + ′ − Y − ′, ψ k ′ ( y 2 ​ c) = ϕ ′ ( y 2 ​ c), ψ k ( 2 ​ i + 1) ( y 2 ​ c) = 0 for all i = 1, …, k − 1, \displaystyle\psi_{k}(y_{2c})=\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}},\quad\psi_{k}^{\prime}(y_{2c})=\phi^{\prime}(y_{2c}),\quad\psi_{k}^{(2i+1)}(y_{2c})=0\mbox{ for all }i=1,\ldots,k-1, |  |

and where

(4.7) |  | ψ k ( 2 ​ i) ​ ( y 2 ​ c) = Ψ 0 ( 2 ​ i) + ( 2 ​ i + 1)! ​ δ 2 ​ ( k − i) ​ ϕ ′ ​ ( y 2 ​ c) 2 ​ i − 1 ​ C 2 ​ i − 1 ​ Φ 1 ( 2 ​ i), \displaystyle\psi_{k}^{(2i)}(y_{2c})=\Psi_{0}^{(2i)}+(2i+1)!\delta^{2(k-i)}{\phi^{\prime}(y_{2c})^{2i-1}}C_{2i}^{-1}\Phi_{1}^{(2i)}, |  |

for i = 1, …, k i=1,\ldots,k. Here Ψ 0 ( 2 ​ i) \Psi_{0}^{(2i)}, i = 1, …, k i=1,\ldots,k are defined recursively as the values of ϕ ( 2 ​ i) ​ ( y 2 ​ c) \phi^{(2i)}(y_{2c}) such that I ( 2 ​ i + 1) ​ ( 0) = 0 I^{(2i+1)}(0)=0:

 | Ψ 0 ( 2 ​ i) = − C 2 ​ i − 1 ​ J 2 ​ i − 1 ​ ( ψ k ′ ​ ( y 2 ​ c), …, ψ k ( 2 ​ i − 1) ​ ( y 2 ​ c)) ​ ϕ ′ ​ ( y 2 ​ c) 2 ​ i − 1, \displaystyle\Psi_{0}^{(2i)}=-C_{2i}^{-1}J_{2i-1}(\psi_{k}^{\prime}(y_{2c}),\ldots,\psi_{k}^{(2i-1)}(y_{2c}))\phi^{\prime}(y_{2c})^{2i-1}, |  |

recall ( 4.2) and ( 4.4). Then for each δ > 0 \delta>0 these 2 ​ k + 1 2k+1 conditions fix the polynomial ψ k \psi_{k} uniquely and from Lemma 4.2 it follows that

(4.8) |  | I ( 2 ​ i + 1) ​ ( 0) = ( 2 ​ i + 1)! ​ δ 2 ​ ( k − i) ​ Ψ 1 ( 2 ​ i). \displaystyle I^{(2i+1)}(0)=(2i+1)!\delta^{2(k-i)}\Psi_{1}^{(2i)}. |  |

if we replace ϕ \phi by ψ k \psi_{k} in the expression for I ⁡ ( x) I(x).

ψ k \psi_{k} is, however, not a regularization function. Instead, we construct the regularization function ϕ k \phi_{k} by modifying ϕ \phi such that it agrees with ψ k \psi_{k} on a small neighborhood of y 2 ​ c y_{2c} and, in particular, has the prescribed derivatives ψ k ( i) ​ ( y 2 ​ c) \psi_{k}^{(i)}(y_{2c}), i = 0, 1, …, 2 ​ k i=0,1,\ldots,2k at y 2 = y 2 ​ c y_{2}=y_{2c}. For this purpose, let B: ℝ → ℝ B:\mathbb{R}\rightarrow\mathbb{R} be a smooth “bump function” with support on ] − 2, 2 []-2,2[that is 1 1 on the domain [− 1, 1] [-1,1]. Let υ > 0 \upsilon>0 and define B υ ​ ( x) = B ⁡ ( υ − 1 ​ x) B_{\upsilon}(x)=B(\upsilon^{-1}x). Then B υ B_{\upsilon} is a bump function with support on ] − 2 υ, 2 υ []-2\upsilon,2\upsilon[that is 1 1 on the domain [− υ, υ] [-\upsilon,\upsilon]. Clearly,

 | | B υ ′ ​ ( x) | ≤ υ − 1 ​ sup ​ | B ′ |, |B_{\upsilon}^{\prime}(x)|\leq\upsilon^{-1}\text{sup}|B^{\prime}|, |  |

for all x ∈ ℝ x\in\mathbb{R}. We then define ϕ k \phi_{k} as follows:

(4.9) |  | ϕ k ​ ( y 2):= ϕ ⁡ ( y 2) ​ ( 1 − B υ ​ ( y 2 − y 2 ​ c)) + ψ k ​ ( y 2) ​ B υ ​ ( y 2 − y 2 ​ c). \displaystyle\phi_{k}(y_{2}):=\phi(y_{2})(1-B_{\upsilon}(y_{2}-y_{2c}))+\psi_{k}(y_{2})B_{\upsilon}(y_{2}-y_{2c}). |  |

Notice that ϕ k ​ ( y 2) = ψ k ​ ( y 2) \phi_{k}(y_{2})=\psi_{k}(y_{2}) on [y 2 ​ c − υ, y 2 ​ c + υ] [y_{2c}-\upsilon,y_{2c}+\upsilon] whereas ϕ k ​ ( y 2) = ϕ ⁡ ( y 2) \phi_{k}(y_{2})=\phi(y_{2}) outside ] y 2 ​ c − 2 υ, y 2 ​ c + 2 υ []y_{2c}-2\upsilon,y_{2c}+2\upsilon[. It is clear that ϕ k \phi_{k} satisfies (A1) and (A3). Therefore to verify that ϕ k \phi_{k} is a regularization function we just need to show (A2). By taking υ > 0 \upsilon>0 small enough, we have that

(4.10) |  | ψ k ′ ​ ( y 2) > 0 ​ for ​ y 2 ∈ [y 2 ​ c − υ, y 2 ​ c + υ]. \displaystyle\psi_{k}^{\prime}(y_{2})>0\mbox{ for }y_{2}\in[y_{2c}-\upsilon,y_{2c}+\upsilon]. |  |

and consequently, it suffices to verify (A2) on [y 2 ​ c − 2 ​ υ, y 2 ​ c − υ] ∪ [y 2 ​ c + υ, y 2 ​ c + 2 ​ υ] [y_{2c}-2\upsilon,y_{2c}-\upsilon]\cup[y_{2c}+\upsilon,y_{2c}+2\upsilon]. We have

(4.11) |  | ϕ k ′ ​ ( y 2) \displaystyle\phi_{k}^{\prime}(y_{2}) | = ϕ ′ ​ ( y 2) ​ ( 1 − B υ ​ ( y 2 − y 2 ​ c)) + ψ k ′ ​ ( y 2) ​ B υ ​ ( y 2 − y 2 ​ c) \displaystyle=\phi^{\prime}(y_{2})(1-B_{\upsilon}(y_{2}-y_{2c}))+\psi_{k}^{\prime}(y_{2})B_{\upsilon}(y_{2}-y_{2c}) |  |

 |  | + ( ψ k ​ ( y 2) − ϕ ⁡ ( y 2)) ​ B υ ′ ​ ( y 2 − y 2 ​ c). \displaystyle+(\psi_{k}(y_{2})-\phi(y_{2}))B_{\upsilon}^{\prime}(y_{2}-y_{2c}). |  |

Seeing that ϕ ′ ​ ( y 2 ​ c) = ψ k ′ ​ ( y 2 ​ c) \phi^{\prime}(y_{2c})=\psi_{k}^{\prime}(y_{2c}), the first two terms can be bounded by Taylor’s theorem from below by 1 2 ​ ϕ ′ ​ ( y 2 ​ c) \frac{1}{2}\phi^{\prime}(y_{2c}) on the relevant domain by taking υ \upsilon small enough. Similarly, using also that ϕ ⁡ ( y 2 ​ c) = ψ k ​ ( y 2 ​ c) \phi(y_{2c})=\psi_{k}(y_{2c}) we have that

 | ψ k ​ ( y 2) − ϕ ⁡ ( y 2) = 1 2 ​ D ​ ( y 2) ​ ( y 2 − y 2 ​ c) 2, \displaystyle\psi_{k}(y_{2})-\phi(y_{2})=\frac{1}{2}D(y_{2})(y_{2}-y_{2c})^{2}, |  |

for some smooth D D. Hence on [y 2 ​ c − 2 ​ υ, y 2 ​ c + 2 ​ υ] [y_{2c}-2\upsilon,y_{2c}+2\upsilon] we have for all υ > 0 \upsilon>0 that

 | | ψ k ​ ( y 2) − ϕ ⁡ ( y 2) | ≤ C ​ υ 2, \displaystyle|\psi_{k}(y_{2})-\phi(y_{2})|\leq C\upsilon^{2}, |  |

for some constant C > 0 C>0 independent of υ > 0 \upsilon>0. This allow us to bound the final term in ( 4.11) from below by − C ​ sup ​ | B ′ | ​ υ -C\text{sup}|B^{\prime}|\upsilon for all υ > 0 \upsilon>0 small enough and consequently we have specifically shown that

 | ϕ k ′ ​ ( y 2) > 0, \displaystyle\phi_{k}^{\prime}(y_{2})>0, |  |

for all υ > 0 \upsilon>0 small enough. Notice this holds uniformly for δ > 0 \delta>0 small enough.

We now apply Lemma 4.2 with the regularization function ϕ k \phi_{k}. Using ( 4.7), Taylor’s theorem and setting x = δ ​ x 2 x=\delta x_{2} for δ > 0 \delta>0, we obtain the following expression

 | I ⁡ ( x) = δ 2 ​ k + 1 ​ x 2 3 ​ ( P k − 1 ​ ( x 2 2) + 𝒪 ⁡ ( δ)), \displaystyle I(x)=\delta^{2k+1}x_{2}^{3}\left(P_{k-1}(x_{2}^{2})+\mathcal{O}(\delta)\right), |  |

for the slow divergence-integral, where P k − 1 P_{k-1} is precisely the polynomial ( 4.5) of degree k − 1 k-1. This is a simple calculation based upon ( 4.1), see also ( 4.8). On [y 2 ​ c − υ, y 2 ​ c + υ] [y_{2c}-\upsilon,y_{2c}+\upsilon] where ϕ k = ψ k \phi_{k}=\psi_{k} we then consider

(4.12) |  | I 2 ​ ( x 2, δ) = δ − 2 ​ k − 1 ​ x 2 − 3 ​ I ​ ( δ ​ x 2). \displaystyle I_{2}(x_{2},\delta)=\delta^{-2k-1}x_{2}^{-3}I(\delta x_{2}). |  |

By construction, recall ( 4.6), we have I 2 ​ ( x 2, 0) = P 1 ​ ( x 2) = 0 I_{2}(x_{2},0)=P_{1}(x_{2})=0 for each x 2 = 1, …, k − 1 x_{2}=1,\ldots,\sqrt{k-1}, and each root perturbs to a simple root of I 2 ​ ( ⋅, δ) I_{2}(\cdot,\delta) (and consequently a positive root of I I at x ≈ δ, …, δ ​ k − 1 x\approx\delta,\ldots,\delta\sqrt{k-1}) by the implicit function theorem for δ > 0 \delta>0 small enough. This completes the proof. ∎

Suppose that

 | β > χ > 0, ξ ≠ 0. \beta>\chi>0,\quad\xi\neq 0. |  |

Then it is a simple calculation to show that assumptions 4, 5 and 6 all hold true for Z ± Z_{\pm} with Z + Z_{+} being quadratic of the form

(4.13) |  | Z + ​ ( z, λ) \displaystyle Z_{+}(z,\lambda) | = ( 1 x + 1 2 ​ ξ ​ x 2), \displaystyle=\begin{pmatrix}1\\ x+\frac{1}{2}\xi x^{2}\end{pmatrix}, |  |

whereas Z − Z_{-} is linear of the form

(4.14) |  | Z − ​ ( z, λ) \displaystyle Z_{-}(z,\lambda) | = ( − χ − β ⁡ ( x − λ)). \displaystyle=\begin{pmatrix}-\chi\\ -\beta(x-\lambda)\end{pmatrix}. |  |

Upon invoking Theorem 3.1, we then conclude that for each k ∈ ℕ k\in\mathbb{N} Theorem 4.3 gives the existence of k k limit cycles of z ′ = Z ⁡ ( z, ϕ k ​ ( y ​ ϵ − 2), λ c k ​ ( ϵ)) z^{\prime}=Z(z,\phi_{k}(y\epsilon^{-2}),\lambda^{k}_{c}(\epsilon)) for all 0 < ϵ ≪ 1 0<\epsilon\ll 1. In turn, this then completes the proof of Theorem 1.1.

## 5. Numerical examples

To illustrate and quantify some of the aspects of our general approach, we consider ( 4.13) and ( 4.14) with

(5.1) |  | β = 2, χ = ξ = 1, \displaystyle\beta=2,\,\chi=\xi=1, |  |

and use the general procedure in the proof of Theorem 1.1 in Section 4 to find three different ϕ k \phi_{k} -functions (tuning the parameters δ \delta and υ \upsilon) so that I I has 3 3, 5 5 and 7 7 simple zeros. We define our bump function B B in the following classical way. Let

 | B 0 ​ ( x) = { 0 for ​ x ≤ 0, e − 1 / x for ​ x > 0, \displaystyle B_{0}(x)=\begin{cases}0&\text{for}\,x\leq 0,\\ e^{-1/x}&\text{for}\,x>0,\end{cases} |  |

and put B 1 ​ ( x) = B 0 ​ ( x) B 0 ​ ( x) + B 0 ​ ( 1 − x) B_{1}(x)=\frac{B_{0}(x)}{B_{0}(x)+B_{0}(1-x)}, B 2 ​ ( x) = B 1 ​ ( x − 1) B_{2}(x)=B_{1}(x-1), B 3 ​ ( x) = B 2 ​ ( x 2) B_{3}(x)=B_{2}(x^{2}), and then finally B ⁡ ( x):= 1 − B 3 ​ ( x) B(x):=1-B_{3}(x).

For simplicity we use

 | ϕ ⁡ ( y 2) = 1 2 + 1 π ​ arctan ⁡ ( y 2), \displaystyle\phi(y_{2})=\frac{1}{2}+\frac{1}{\pi}\arctan(y_{2}), |  |

as our reference regularization function. Then with the parameters ( 5.1) we find that

 | y 2 ​ c = ϕ − 1 ​ ( 2 3) = 1 3, ϕ ′ ​ ( y 2 ​ c) = 3 4 ​ π. \displaystyle y_{2c}=\phi^{-1}\left(\frac{2}{3}\right)=\frac{1}{\sqrt{3}},\quad\phi^{\prime}(y_{2c})=\frac{3}{4\pi}. |  |

For each k = 4 k=4, k = 6 k=6 and k = 8 k=8 we then fix the polynomial ψ k \psi_{k} by ψ k ​ ( y 2 ​ c) = 2 3 \psi_{k}(y_{2c})=\frac{2}{3}, ψ k ′ ​ ( y 2 ​ c) = 3 4 ​ π \psi_{k}^{\prime}(y_{2c})=\frac{3}{4\pi} and by setting ψ k ( 2 ​ i) \psi_{k}^{(2i)}, i = 1, …, k i=1,\ldots,k equal to the expressions in ( 4.7); the quantities Φ 1 ( 2 ​ i) \Phi_{1}^{(2i)}, i = 1, …, k i=1,\ldots,k in ( 4.7) are chosen so that P k − 1 P_{k-1} ( 4.5) has its roots at 1, …, k − 1 1,\ldots,k-1. As outlined above we set all the odd higher order derivatives ψ k ( 2 ​ i + 1) ​ ( y 2 ​ c) = 0 \psi_{k}^{(2i+1)}(y_{2c})=0, i ≥ 1 i\geq 1. For k = 4 k=4 with δ = 10 − 3 \delta=10^{-3} we obtain

(5.2) |  | ψ 4 ​ ( y 2) \displaystyle\psi_{4}(y_{2}) | = 2 3 + 3 4 ​ π ​ ( y 2 − 1 3) + 0.2137243716 ​ ( y 2 − 1 3) 2 + 0.306956879 ​ ( y 2 − 1 3) 4 \displaystyle=\frac{2}{3}+\frac{3}{4\pi}\left(y_{2}-\frac{1}{\sqrt{3}}\right)+0.2137243716\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{2}+0.306956879\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{4} |  |

 |  | + 1.442372260 ​ ( y 2 − 1 3) 6 − 25.33517649 ​ ( y 2 − 1 3) 8. \displaystyle+1.442372260\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{6}-25.33517649\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{8}. |  |

The resulting ϕ 4 \phi_{4} ( 4.9) k=4 is shown in Fig. 5 (a) for υ = 0.05 \upsilon=0.05 (in red) together with ϕ \phi (blue) and ψ 4 \psi_{4} (green). For this ϕ 4 \phi_{4} we then proceed to accurately compute the slow divergence integral (using Taylor expansions up to terms of order x 25 x^{25} computed in MAPLE with Digits set to 100 100). The result is shown in Fig. 6 (a). Here υ > 0 \upsilon>0 is fixed so that ϕ 4 \phi_{4} satisfies (A1) - (A3), whereas the value of δ \delta is taken small enough to ensure that I I has (at least) 3 3 simple zeros. We use the same method for k = 6 k=6 and k = 8 k=8 and find

(5.3) |  | ψ 6 ​ ( y 2) \displaystyle\psi_{6}(y_{2}) | = 2 3 + 3 4 ​ π ​ ( y 2 − 1 3) + 0.2137243716 ​ ( y 2 − 1 3) 2 − 0.3069568794 ​ ( y 2 − 1 3) 4 \displaystyle=\frac{2}{3}+\frac{3}{4\pi}\left(y_{2}-\frac{1}{\sqrt{3}}\right)+0.2137243716\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{2}-0.3069568794\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{4} |  |

 |  | + 1.44235445 ​ ( y 2 − 1 3) 6 − 12.12351865 ​ ( y 2 − 1 3) 8 \displaystyle+1.44235445\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{6}-12.12351865\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{8} |  |

 |  | + 154.2008391 ​ ( y 2 − 1 3) 10 − 3015.15236 ​ ( y 2 − 1 3) 12, \displaystyle+154.2008391\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{10}-3015.15236\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{12}, |  |

and

(5.4) |  | ψ 8 ​ ( y 2) \displaystyle\psi_{8}(y_{2}) | = 2 3 + 3 4 ​ π ​ ( y 2 − 1 3) + 0.2137243716 ​ ( y 2 − 1 3) 2 − 0.3069568794 ​ ( y 2 − 1 3) 4 \displaystyle=\frac{2}{3}+\frac{3}{4\pi}\left(y_{2}-\frac{1}{\sqrt{3}}\right)+0.2137243716\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{2}-0.3069568794\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{4} |  |

 |  | + 1.442354453 ​ ( y 2 − 1 3) 6 − 12.12351865 ​ ( y 2 − 1 3) 8 \displaystyle+1.442354453\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{6}-12.12351865\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{8} |  |

 |  | + 154.2008302 ​ ( y 2 − 1 3) 10 − 2744.019283 ​ ( y 2 − 1 3) 12 + 65135.03549 ​ ( y 2 − 1 3) 14 \displaystyle+154.2008302\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{10}-2744.019283\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{12}+65135.03549\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{14} |  |

 |  | − 1.998886089 × 10 6 ( y 2 − 1 3) 16 \displaystyle-1.998886089\times 10^{6}\left(y_{2}-\frac{1}{\sqrt{3}}\right)^{16} |  |

for δ = 10 − 4 \delta=10^{-4} resp. δ = 10 − 5 \delta=10^{-5}. The result is shown in Fig. 6 (b) resp. (c), still with υ = 0.05 \upsilon=0.05.

The roots are very sensitive with respect to δ \delta; increasing δ \delta only slightly in each of our cases k = 4, 6 k=4,6, and 8 8 lead to fewer roots. For example for k = 8 k=8 we only find 5 5 roots for δ ≳ 9.449 × 10 − 5 \delta\gtrsim 9.449\times 10^{-5}. In any case, δ > 0 \delta>0 has to be taken quite small to realize the desired number of roots. In turn, this implies that I I is extremely small on the relevant domains; for k = 8 k=8 for example, we find (see Fig. 6 (c)) that I ⁡ ( x) ∼ 10 − 82 − 10 − 85 I(x)\sim 10^{-82}-10^{-85}! We therefore expect – in line with [13] – that the desired number of limit cycles for 0 < ϵ ≪ 1 0<\epsilon\ll 1 can also only be realized for extremely small values of ϵ > 0 \epsilon>0 and that these are therefore extremely difficult (if not impossible) to detect in numerical computations.

[image: Refer to caption]

[image: Refer to caption]

Figure 5. In (a): Graph of the regularization function ϕ 4 \phi_{4} (in red) used for generating an example with 3 3 simple zeros of I I, see Fig. 6 (a). The function ϕ \phi is in blue whereas ψ 4 \psi_{4} is in green. In (b): A zoom around y 2 = y 2 ​ c y_{2}=y_{2c} showing the three values of y 2 y_{2} on the critical manifold corresponding to the x x -point where I ⁡ ( x) = 0 I(x)=0. Notice that these points lie inside the region where ϕ 4 = ψ 4 \phi_{4}=\psi_{4}.

Figure 6. The graphs of (scaled versions of) the slow divergence integral I I, see ( 4.12), for ψ k \psi_{k} given by ( 5.2) (a), ( 5.3) (b), ( 5.4) (c). Notice that in each case, I I has roots close to δ ​ i \delta\sqrt{i}, i = 1, …, k − 1 i=1,\ldots,k-1 as desired.

## Appendix A Blowing up the degenerate line H ¯ \overline{H}

In this section we show that the system ( 3.3) from Section 3.1.1 satisfies Assumptions T3–T6 of [14] near the intersection p 0 p_{0} of H ¯ \overline{H} with C ¯ \overline{C}. We write

(A.1) |  | Z ± ​ ( ⋅, λ 0 + ϵ ​ λ ~) = Z ± ​ ( ⋅, λ 0) + ϵ ​ λ ~ ​ Z ~ ± ​ ( ⋅) + 𝒪 ⁡ ( ϵ 2) Z_{\pm}(\cdot,\lambda_{0}+\epsilon\widetilde{\lambda})=Z_{\pm}(\cdot,\lambda_{0})+\epsilon\widetilde{\lambda}\widetilde{Z}_{\pm}(\cdot)+\mathcal{O}(\epsilon^{2}) |  |

where Z ~ ± = ( X ~ ±, Y ~ ±) \widetilde{Z}_{\pm}=(\widetilde{X}_{\pm},\widetilde{Y}_{\pm}), like in Section 2.2, and λ ~ ∼ 0 \widetilde{\lambda}\sim 0 is introduced in Section 3.1. We blow up H ¯ \overline{H} to a cylinder through the following blow-up transformation

 | ρ ≥ 0, ( x ~, ϵ ~) ↦ { x = ρ ​ x ~, ϵ = ρ ​ ϵ ~, \displaystyle\rho\geq 0,\,(\tilde{x},\tilde{\epsilon})\mapsto\begin{cases}x&=\rho\tilde{x},\\ \epsilon&=\rho\tilde{\epsilon},\end{cases} |  |

where ( x ~, ϵ ~) ∈ 𝕊 1 (\tilde{x},\tilde{\epsilon})\in\mathbb{S}^{1} and ϵ ~ ≥ 0 \tilde{\epsilon}\geq 0. Again we will work with different charts. Let’s first consider the end points of the normally attracting part and the normally repelling part of C ¯ \overline{C} on the edge of the cylinder { ρ = ϵ ~ = 0 } \{\rho=\tilde{\epsilon}=0\}.

### A.1. Dynamics in the phase directional charts x ~ = ± 1 \tilde{x}=\pm 1

In the phase directional chart x ~ = 1 \tilde{x}=1 we have ( x, ϵ) = ( ρ, ρ ​ ϵ ~) (x,\epsilon)=(\rho,\rho\tilde{\epsilon}). In these coordinates system ( 3.3) becomes, after division by ρ > 0 \rho>0,

(A.2) |  | y ˙ 2 \displaystyle\dot{y}_{2} | = Y + ′ ​ ( 0, 0, λ 0) ​ ϕ ​ ( y 2) + Y − ′ ​ ( 0, 0, λ 0) ​ ( 1 − ϕ ⁡ ( y 2)) + 𝒪 ⁡ ( ρ, ϵ ~), \displaystyle=Y_{+}^{\prime}(0,0,\lambda_{0})\phi(y_{2})+Y_{-}^{\prime}(0,0,\lambda_{0})(1-\phi(y_{2}))+\mathcal{O}(\rho,\tilde{\epsilon}), |  |

 | ρ ˙ \displaystyle\dot{\rho} | = ρ ​ ϵ ~ 2 ​ ( X + ​ ( 0, 0, λ 0) ​ ϕ ​ ( y 2) + X − ​ ( 0, 0, λ 0) ​ ( 1 − ϕ ⁡ ( y 2)) + 𝒪 ⁡ ( ρ)), \displaystyle=\rho\tilde{\epsilon}^{2}\left(X_{+}(0,0,\lambda_{0})\phi(y_{2})+X_{-}(0,0,\lambda_{0})(1-\phi(y_{2}))+\mathcal{O}(\rho)\right), |  |

 | ϵ ~ ˙ \displaystyle\dot{\tilde{\epsilon}} | = − ϵ ~ 3 ​ ( X + ​ ( 0, 0, λ 0) ​ ϕ ​ ( y 2) + X − ​ ( 0, 0, λ 0) ​ ( 1 − ϕ ⁡ ( y 2)) + 𝒪 ⁡ ( ρ)). \displaystyle=-\tilde{\epsilon}^{3}\left(X_{+}(0,0,\lambda_{0})\phi(y_{2})+X_{-}(0,0,\lambda_{0})(1-\phi(y_{2}))+\mathcal{O}(\rho)\right). |  |

When ρ = ϵ ~ = 0 \rho=\tilde{\epsilon}=0, system ( A.2) has a semi-hyperbolic singularity

 | y 2 = y 2 ​ c:= ϕ − 1 ​ ( − Y − ′ Y + ′ − Y − ′ ​ ( 0, 0, λ 0)). y_{2}=y_{2c}:=\phi^{-1}\left(\frac{-Y_{-}^{\prime}}{Y_{+}^{\prime}-Y_{-}^{\prime}}(0,0,\lambda_{0})\right). |  |

The eigenvalues of the linearization are

 | ( ( Y + ′ − Y − ′) ​ ( 0, 0, λ 0) ​ ϕ ′ ​ ( y 2), 0, 0), ((Y_{+}^{\prime}-Y_{-}^{\prime})(0,0,\lambda_{0})\phi^{\prime}(y_{2}),0,0), |  |

the first eigenvalue being positive by Proposition 2.3 item (iv). Two-dimensional center manifolds of ( A.2) at this singularity are transverse to the unstable manifold given by the y 2 y_{2} -axis. Thus, the end point of the repelling part of C ¯ \overline{C} is normally hyperbolic (Assumption T3). Moreover, each center manifold of ( A.2) at the singularity is the graph of

 | y 2 = y 2 ​ c + 𝒪 ⁡ ( ρ, ϵ ~). y_{2}=y_{2c}+\mathcal{O}(\rho,\tilde{\epsilon}). |  |

Using the ( ρ, ϵ ~) (\rho,\tilde{\epsilon}) -component of ( A.2) we easily find the center behavior:

 | { ρ ˙ = ρ ​ ϵ ~ 2 ​ ( X s ​ l ​ ( 0, λ 0) + 𝒪 ⁡ ( ρ, ϵ ~)), ϵ ~ ˙ = − ϵ ~ 3 ​ ( X s ​ l ​ ( 0, λ 0) + 𝒪 ⁡ ( ρ, ϵ ~)) }. \left\{\dot{\rho}=\rho\tilde{\epsilon}^{2}\left(X_{sl}(0,\lambda_{0})+\mathcal{O}(\rho,\tilde{\epsilon})\right),\dot{\tilde{\epsilon}}=-\tilde{\epsilon}^{3}\left(X_{sl}(0,\lambda_{0})+\mathcal{O}(\rho,\tilde{\epsilon})\right)\right\}. |  |

Since X s ​ l ​ ( 0, λ 0) > 0 X_{sl}(0,\lambda_{0})>0, this system has, after division by ϵ ~ 2 \tilde{\epsilon}^{2}, an isolated hyperbolic saddle ( ρ, ϵ ~) = ( 0, 0) (\rho,\tilde{\epsilon})=(0,0) (Assumption T4). Notice that the exponent in ϵ ~ 2 \tilde{\epsilon}^{2} is equal to the order of degeneracy mentioned in Section 3.1.1. Notice also that the center manifold, restricted to ρ = 0 \rho=0, is unique because ( A.2) is of saddle type inside ρ = 0 \rho=0.

The chart x ~ = − 1 \tilde{x}=-1 can be covered by applying ( t, ρ, ϵ ~) ↦ ( − t, − ρ, − ϵ ~) (t,\rho,\tilde{\epsilon})\mapsto(-t,-\rho,-\tilde{\epsilon}) to ( A.2).

###### Remark A.1.

In the framework of [14] a turning point is usually replaced with a sphere 𝕊 2 \mathbb{S}^{2} and Assumptions T3-T4 have to be satisfied at the end points of normally hyperbolic branches of the critical curve on the equator of the sphere. In our slow-fast setting ( 3.3) it is more convenient to use a cylindrical blow-up. This is not a problem because locally near the end points, located on the edge of the cylinder, one can use the normal linearization theorem of [6], like in [14].

### A.2. Dynamics in the family chart ϵ ~ = 1 \tilde{\epsilon}=1

In the scaling chart we obtain x = ϵ ​ x 2 x=\epsilon x_{2}. The system ( 3.3) changes into

(A.3) |  | x ˙ 2 \displaystyle\dot{x}_{2} | = X + ​ ( 0, 0, λ 0) ​ ϕ ​ ( y 2) + X − ​ ( 0, 0, λ 0) ​ ( 1 − ϕ ⁡ ( y 2)), \displaystyle=X_{+}(0,0,\lambda_{0})\phi(y_{2})+X_{-}(0,0,\lambda_{0})(1-\phi(y_{2})), |  |

 | y ˙ 2 \displaystyle\dot{y}_{2} | = ( x 2 ​ Y + ′ ​ ( 0, 0, λ 0) + λ ~ ​ Y ~ + ​ ( 0, 0)) ​ ϕ ​ ( y 2) + ( x 2 ​ Y − ′ ​ ( 0, 0, λ 0) + λ ~ ​ Y ~ − ​ ( 0, 0)) ​ ( 1 − ϕ ⁡ ( y 2)), \displaystyle=\left(x_{2}Y_{+}^{\prime}(0,0,\lambda_{0})+\widetilde{\lambda}\widetilde{Y}_{+}(0,0)\right)\phi(y_{2})+\left(x_{2}Y_{-}^{\prime}(0,0,\lambda_{0})+\widetilde{\lambda}\widetilde{Y}_{-}(0,0)\right)(1-\phi(y_{2})), |  |

upon desingularization (dividing the right hand side by ϵ \epsilon) and (subsequently) setting ϵ = 0 \epsilon=0. We used ( A.1). For λ ~ = 0 \widetilde{\lambda}=0, ( A.3) has an invariant line γ \gamma defined by y 2 = y 2 ​ c y_{2}=y_{2c} with the dynamics x ˙ 2 = X s ​ l ​ ( 0, λ 0) \dot{x}_{2}=X_{sl}(0,\lambda_{0}) on it. The line γ \gamma is a heteroclinic connection on the cylinder connecting the end point of the attracting part of C ¯ \overline{C} to the end point of the repelling part of C ¯ \overline{C} (Assumption T5). See also Fig. 4 (b).

To show that the invariant line γ \gamma breaks in a regular way as we vary λ ~ ∼ 0 \widetilde{\lambda}\sim 0 (Assumption T6), we follow [42, section 6.2] and extend the system by augmenting λ ~ ˙ = 0 \dot{\widetilde{\lambda}}=0. In this formulation the center manifolds from x ~ = ± 1 \tilde{x}=\pm 1 – that extend the attracting and repelling parts of C ¯ \overline{C} onto H ¯ \overline{H} – become two-dimensional and γ \gamma belongs to the intersection of these within ρ = 0 \rho=0 (where the manifolds are overflowing and unique). Write { ( A.3), λ ~ ˙ = 0 } \{\mbox{(\ref{eq:x2y2})},\dot{\widetilde{\lambda}}=0\} in terms of d ​ y 2 d ​ x 2, d ​ λ ~ d ​ x 2 \frac{dy_{2}}{dx_{2}},\frac{d\widetilde{\lambda}}{dx_{2}} and consider the variational equations around the solution y 2 = y 2 ​ c y_{2}=y_{2c}, λ ~ = 0 \widetilde{\lambda}=0 (corresponding to γ \gamma):

(A.4) |  | d ​ u d ​ x 2 \displaystyle\frac{du}{dx_{2}} | = A ​ x 2 ​ u + B ​ v, \displaystyle=Ax_{2}u+Bv, |  |

 | d ​ v d ​ x 2 \displaystyle\frac{dv}{dx_{2}} | = 0, \displaystyle=0, |  |

where

 | A:= Y + ′ − Y − ′ X s ​ l ​ ( 0, 0, λ 0) ​ ϕ ′ ​ ( y 2 ​ c), B:= Y ~ − ​ Y + ′ − Y ~ + ​ Y − ′ X s ​ l ​ ( Y + ′ − Y − ′) ​ ( 0, 0, λ 0). \displaystyle A:=\frac{Y_{+}^{\prime}-Y_{-}^{\prime}}{X_{sl}}(0,0,\lambda_{0})\phi^{\prime}(y_{2c}),\quad B:=\frac{\widetilde{Y}_{-}Y_{+}^{\prime}-\widetilde{Y}_{+}Y_{-}^{\prime}}{X_{sl}(Y^{\prime}_{+}-Y^{\prime}_{-})}(0,0,\lambda_{0}). |  |

Notice that A > 0 A>0, see Proposition 2.3 item (iv), and that B ≠ 0 B\neq 0 by 4, see specifically ( 2.7). It is then straightforward to show, using the asymptotics of the error-function erf, see also [42, Lemma 6.2], that there are two linearly independent solutions of ( A.4):

 | ( u, v) \displaystyle(u,v) | = ( B ​ 2 ​ π A ​ e A ​ x 2 2 / 2 ​ ( erf ​ ( A 2 ​ x 2) ± 1), 1), \displaystyle=\left(B\sqrt{\frac{2\pi}{A}}e^{Ax_{2}^{2}/2}\left(\text{erf}\left(\sqrt{\frac{A}{2}}x_{2}\right)\pm 1\right),1\right), |  |

with exponential growth for x 2 → ∞ x_{2}\rightarrow\infty (resp. − ∞ -\infty) and algebraic growth for x 2 → − ∞ x_{2}\rightarrow-\infty (resp. ∞ \infty). By [56, Proposition 4.2] the extended center manifolds therefore intersect transversally along γ \gamma, which completes the verification of Asssumption T6.

## Appendix B Transition maps near the hyperbolic edges

In this section we study the transition map near the line of singularities { r 1 = ϵ 1 = 0 } \{r_{1}=\epsilon_{1}=0\} of

(B.1) |  | x ˙ \displaystyle\dot{x} | = r 1 2 ​ X ​ ( x, r 1, ϵ 1), \displaystyle=r_{1}^{2}X(x,r_{1},\epsilon_{1}), |  |

 | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1 ​ Y ​ ( x, r 1, ϵ 1), \displaystyle=-r_{1}Y(x,r_{1},\epsilon_{1}), |  |

 | ϵ ˙ 1 \displaystyle\dot{\epsilon}_{1} | = ϵ 1 ​ Y ​ ( x, r 1, ϵ 1), \displaystyle=\epsilon_{1}Y(x,r_{1},\epsilon_{1}), |  |

where X X and Y Y are smooth functions. We assume that Y ⁡ ( x, 0, 0) > 0 Y(x,0,0)>0 for each x ∈ J x\in J, J J being a compact set. Notice that ( x, 0, 0) (x,0,0) is a set of equilibria and the linearization has ∓ Y ⁡ ( x, 0, 0) \mp Y(x,0,0) as two nonzero eigenvalues.

We now describe a transition map near this line of partially hyperbolic equilibria. We consider the transition map Q 1 Q_{1} from Σ i ​ n:= { ( x, r 1, ϵ 1): r 1 = r 10 } \Sigma_{in}:=\{(x,r_{1},\epsilon_{1}):r_{1}=r_{10}\} to Σ o ​ u ​ t:= { ( x, r 1, ϵ 1): ϵ 1 = ϵ 10 } \Sigma_{out}:=\{(x,r_{1},\epsilon_{1}):\epsilon_{1}=\epsilon_{10}\} along the trajectories of ( B.1) where r 10, ϵ 10 r_{10},\epsilon_{10} are small positive constants. Let π x ​ Q 1 \pi_{x}Q_{1} denote the x x -component of Q 1 Q_{1}.

###### Proposition B.1.

Fix n ∈ ℕ n\in\mathbb{N} then there are constants r 10 > 0 r_{10}>0 and ϵ 10 > 0 \epsilon_{10}>0 small enough such that

 | x ↦ π x ​ Q 1 ​ ( x, r 10, ϵ 1) \displaystyle x\mapsto\pi_{x}Q_{1}(x,r_{10},\epsilon_{1}) |  |

is C n C^{n} uniformly and continuously in ϵ 1 \epsilon_{1}. In particular,

 | π x ​ Q 1 ​ ( x, r 10, ϵ 1) = g 0 ​ ( x) + 𝒪 ⁡ ( ϵ 1 ​ log ⁡ ϵ 1 − 1), ϵ 1 → 0, \displaystyle\pi_{x}Q_{1}(x,r_{10},\epsilon_{1})=g_{0}(x)+\mathcal{O}(\epsilon_{1}\log\epsilon_{1}^{-1}),\ \epsilon_{1}\to 0, |  |

with g 0 g_{0} smooth and this expression can be differentiated with respect to x x without changing the order of the remainder.

###### Proof.

We work with the equivalent field ( B.1) divided by Y > 0 Y>0 on J × [0, r 10] × [0, ϵ 10] J\times[0,r_{10}]\times[0,\epsilon_{10}]. We denote this vector field by F ~ \widetilde{F}. First we prove the following lemma.

###### Lemma B.2.

For r 10 r_{10} sufficiently small, there exists a diffeomorphism Φ \Phi

 | Φ ⁡ ( x, r 1, ϵ 1) = ( h ⁡ ( x, r 1) r 1 ϵ 1), \displaystyle\Phi(x,r_{1},\epsilon_{1})=\begin{pmatrix}h(x,r_{1})\\ r_{1}\\ \epsilon_{1}\end{pmatrix}, |  |

with h x ​ ( x, r 1) ≠ 0 h_{x}(x,r_{1})\neq 0 for all x ∈ J, r 1 ∈ [0, r 10] x\in J,\,r_{1}\in[0,r_{10}], such that F ~ \widetilde{F} changes into

(B.2) |  | ξ ˙ \displaystyle\dot{\xi} | = r 1 2 ​ ϵ 1 ​ G ​ ( ξ, r 1, ϵ 1), \displaystyle=r_{1}^{2}\epsilon_{1}G(\xi,r_{1},\epsilon_{1}), |  |

 | r ˙ 1 \displaystyle\dot{r}_{1} | = − r 1, \displaystyle=-r_{1}, |  |

 | ϵ ˙ 1 \displaystyle\dot{\epsilon}_{1} | = ϵ 1, \displaystyle=\epsilon_{1}, |  |

for some smooth G G.

###### Proof.

The map Φ \Phi is obtained by straightening out the stable manifolds of points ( ξ, 0, 0) (\xi,0,0). These manifolds are contained within ϵ 1 = 0 \epsilon_{1}=0 and are graphs over r 1 r_{1}:

 | x = g ⁡ ( ξ, r 1) \displaystyle x=g(\xi,r_{1}) |  |

In particular, g ⁡ ( ξ, 0) = ξ g(\xi,0)=\xi, g ξ ​ ( ξ, 0) ≠ 0 g_{\xi}(\xi,0)\neq 0 and we can invert this expression for ξ \xi:

 | ξ = h ⁡ ( x, r 1) \displaystyle\xi=h(x,r_{1}) |  |

with h ⁡ ( ⋅, r 1) = g − 1 ​ ( ⋅, r 1) h(\cdot,r_{1})=g^{-1}(\cdot,r_{1}). Seeing that ξ ˙ = 0 \dot{\xi}=0 for ϵ 1 = 0 \epsilon_{1}=0 we obtain the result by smoothness of the right hand side. ∎

We then proceed to work on the normal form ( B.2), describing the transition map Q 1 Q_{1} from Σ i ​ n = { ( ξ, r 1, ϵ 1): r 1 = r 10 } \Sigma_{in}=\{(\xi,r_{1},\epsilon_{1}):r_{1}=r_{10}\} to Σ o ​ u ​ t = { ( ξ, r 1, ϵ 1): ϵ 1 = ϵ 10 } \Sigma_{out}=\{(\xi,r_{1},\epsilon_{1}):\epsilon_{1}=\epsilon_{10}\}. Let π ξ ​ Q 1 \pi_{\xi}Q_{1} denote the ξ \xi -component.

First we realize that r 1 ​ ϵ 1 = c ​ o ​ n ​ s ​ t. r_{1}\epsilon_{1}=const. is conserved. Integrating the last two equations from r 1 ​ ( 0) = r 10 r_{1}(0)=r_{10}, ϵ 1 ​ ( 0) = `​ `​ ϵ 1 ​ " \epsilon_{1}(0)=``\epsilon_{1}" and inserting this into the first one, we obtain

(B.3) |  | ξ ⁡ ( T) = ξ ⁡ ( 0) + r 10 ​ ϵ 1 ​ ∫ 0 T e − s ​ r 10 ​ G ​ ( ξ ⁡ ( s), e − s ​ r 10, e s ​ ϵ 1) ​ 𝑑 s, \displaystyle\xi(T)=\xi(0)+r_{10}\epsilon_{1}\int_{0}^{T}e^{-s}r_{10}G(\xi(s),e^{-s}r_{10},e^{s}\epsilon_{1})ds, |  |

where the transition time T = log ⁡ ( ϵ 1 − 1 ​ ϵ 10) T=\log(\epsilon_{1}^{-1}\epsilon_{10}). From here we directly obtain that

 | π ξ ​ Q 1 ​ ( ξ, r 10, ϵ 1) = ξ + 𝒪 ⁡ ( ϵ 1 ​ log ⁡ ϵ 1 − 1), ϵ 1 → 0 \displaystyle\pi_{\xi}Q_{1}(\xi,r_{10},\epsilon_{1})=\xi+\mathcal{O}(\epsilon_{1}\log\epsilon_{1}^{-1}),\ \epsilon_{1}\to 0 |  |

because the integrand in ( B.3) is bounded on the segment [0, T] [0,T]. We handle the derivatives of π ξ ​ Q 1 \pi_{\xi}Q_{1} with respect to ξ \xi in a similar way by considering the higher variational equations of ( B.2). We skip the details because it is standard, see e.g. [38] or [58, Proposition 3.3]. ∎

If X X and Y Y in ( B.1) depend smoothly on a parameter α \alpha, then π x ​ Q 1 \pi_{x}Q_{1} will also depend C n C^{n} -smoothly on this parameter. This also follows from studying ( B.2). We simply study the variational equations obtained by differentiating with respect to α \alpha and apply a similar estimation.

## References

- [1] J. C. Artés, F. Dumortier, and J. Llibre. Limit cycles near hyperbolas in quadratic systems. J. Differential Equations, 246(1):235–260, 2009.
- [2] É. Benoit. Équations différentielles: relation entrée–sortie. C. R. Acad. Sci. Paris Sér. I Math., 293(5):293–296, 1981.
- [3] E. J. Berger. Friction modeling for dynamic system simulation. Applied Mechanics Reviews, 55(6):535–577, 2002.
- [4] M. Bobieński and L. Gavrilov. Finite cyclicity of slow-fast Darboux systems with a two-saddle loop. Proc. Amer. Math. Soc., 144(10):4205–4219, 2016.
- [5] M. Bobieński, P. Mardesic, and D. Novikov. Pseudo-abelian integrals on slow-fast Darboux systems. Ann. Inst. Fourier (Grenoble), 63(2):417–430, 2013.
- [6] P. Bonckaert. Partially hyperbolic fixed points with constraints. Trans. Amer. Math. Soc., 348(3):997–1011, 1996.
- [7] C. Bonet-Reves, J. Larrosa, and T. M-Seara. Regularization around a generic codimension one fold-fold singularity. Journal of Differential Equations, 265(5):1761–1838, 2018.
- [8] E. Bossolini, M. Brøns, and K. U. Kristiansen. Singular limit analysis of a model for earthquake faulting. Nonlinearity, 30(7):2805–2834, 2017.
- [9] E. Bossolini, M. Brøns, and K. U. Kristiansen. A stiction oscillator with canards: On piecewise smooth nonuniqueness and its resolution by regularization using geometric singular perturbation theory. SIAM Review, 62(4):869–897, 2020.
- [10] M. E. Broucke, C. C. Pugh, and S. N. Simic. Structural stability of piecewise smooth systems. Computational and Applied Mathematics, 20(1-2):51–89, 2001.
- [11] M. Caubergh. Hilbert’s sixteenth problem for polynomial liénard equations. Qualitative Theory of Dynamical Systems, 11(1):3–18, 2012.
- [12] C. J. Christopher and N. G. Lloyd. Polynomial systems: a lower bound for the Hilbert numbers. Proc. Roy. Soc. London Ser. A, 450(1938):219–224, 1995.
- [13] P. De Maesschalck and M. Desroches. Numerical continuation techniques for planar slow-fast systems. SIAM Journal on Applied Dynamical Systems, 12(3):1159–1180, 2013.
- [14] P. De Maesschalck and F. Dumortier. Time analysis and entry-exit relation near planar turning points. J. Differential Equations, 215(2):225–267, 2005.
- [15] P. De Maesschalck and F. Dumortier. Canard cycles in the presence of slow dynamics with singularities. Proc. Roy. Soc. Edinburgh Sect. A, 138(2):265–299, 2008.
- [16] P. De Maesschalck and F. Dumortier. Classical Liénard equations of degree n ≥ 6 n\geq 6 can have [n − 1 2] + 2 [\frac{n-1}{2}]+2 limit cycles. J. Differential Equations, 250(4):2162–2176, 2011.
- [17] P. De Maesschalck and R. Huzak. Slow divergence integrals in classical Liénard equations near centers. J. Dynam. Differential Equations, 27(1):177–185, 2015.
- [18] M. di Bernardo, C. J. Budd, A. R. Champneys, and P. Kowalczyk. Piecewise-smooth Dynamical Systems: Theory and Applications. Springer Verlag, 2008.
- [19] F. Dumortier. Slow divergence integral and balanced canard solutions. Qualitative Theory of Dynamical Systems, 10(1):65–85, 2011.
- [20] F. Dumortier, M. El Morsalani, and C. Rousseau. Hilbert’s 16th problem for quadratic systems and cyclicity of elementary graphics. Nonlinearity, 9(5):1209–1261, 1996.
- [21] F. Dumortier, D. Panazzolo, and R. Roussarie. More limit cycles than expected in Liénard equations. Proc. Amer. Math. Soc., 135(6):1895–1904 (electronic), 2007.
- [22] F. Dumortier and R. Roussarie. Canard cycles and center manifolds. Mem. Amer. Math. Soc., 121:1–96, 1996.
- [23] F. Dumortier and R. Roussarie. Multiple canard cycles in generalized Liénard equations. Journal of Differential Equations, 174(1):1–29, 2001.
- [24] F. Dumortier, R. Roussarie, and C. Rousseau. Hilbert’s 16th problem for quadratic vector fields. Journal of Differential Equations, 110(110):86–133, 1994.
- [25] F. Dumortier and C. Rousseau. Study of the cyclicity of some degenerate graphics inside quadratic systems. Commun. Pure Appl. Anal., 8(4):1133–1157, 2009.
- [26] M. Esteban, J. Llibre, and C. Valls. The 16th Hilbert problem for discontinuous piecewise isochronous centers of degree one or two separated by a straight line. Chaos, 31(4):043112, 2021.
- [27] N. Fenichel. Geometric singular perturbation theory for ordinary differential equations. J. Diff. Eq., 31:53–98, 1979.
- [28] A.F. Filippov. Differential Equations with Discontinuous Righthand Sides. Mathematics and its Applications. Kluwer Academic Publishers, 1988.
- [29] M. Han and V. G. Romanovski. On the number of limit cycles of polynomial Liénard systems. Nonlinear Anal. Real World Appl., 14(3):1655–1668, 2013.
- [30] M. Han, Y. Tian, and P. Yu. Small-amplitude limit cycles of polynomial Liénard systems. Sci. China Math., 56(8):1543–1556, 2013.
- [31] R. Huzak. Cyclicity of degenerate graphic D ​ F 2 ​ a DF_{2a} of Dumortier-Roussarie-Rousseau program. Commun. Pure Appl. Anal., 17(3):1305–1316, 2018.
- [32] R. Huzak. Predator-prey systems with small predator’s death rate. Electron. J. Qual. Theory Differ. Equ., pages Paper No. 86, 16, 2018.
- [33] R. Huzak and P. De Maesschalck. Slow divergence integrals in generalized Liénard equations near centers. Electron. J. Qual. Theory Differ. Equ., pages No. 66, 10, 2014.
- [34] M. R. Jeffrey. Hidden dynamics: The mathematics of switches, decisions and other discontinuous behaviour. Springer International Publishing, 2018.
- [35] S. Jelbart, K. U. Kristiansen, and M. Wechselberger. Singularly perturbed boundary-focus bifurcations. Journal of Differential Equations, 296:412–492, 2021.
- [36] Samuel Jelbart, Kristian Uldall Kristiansen, and Martin Wechselberger. Singularly perturbed boundary-equilibrium bifurcations. Nonlinearity, 34(11):7371–7314, 2021.
- [37] T. Kaiser, J.-P. Rolin, and P. Speissegger. Transition maps at non-resonant hyperbolic singularities are o-minimal. J. Reine Angew. Math., 636:1–45, 2009.
- [38] I. Kosiuk and P. Szmolyan. Geometric singular perturbation analysis of an autocatalator model. Discrete and Continuous Dynamical Systems - Series S, 2(4):783–806, 2009.
- [39] I. Kosiuk and P. Szmolyan. Geometric analysis of the goldbeter minimal model for the embryonic cell cycle. Journal of Mathematical Biology, 72(5):1337–1368, 2016.
- [40] K. U. Kristiansen and S. J. Hogan. Resolution of the piecewise smooth visible-invisible two-fold singularity in R3 using regularization and blowup. Journal of Nonlinear Science, 29(2):723–787, 2018.
- [41] K. Uldall Kristiansen. The regularized visible fold revisited. Journal of Nonlinear Science, 30(6):2463–2511, 2020.
- [42] K. Uldall Kristiansen and S. J. Hogan. Regularizations of two-fold bifurcations in planar piecewise smooth systems using blowup. SIAM Journal on Applied Dynamical Systems, 14(4):1731–1786, 2015.
- [43] K. Uldall Kristiansen and P. Szmolyan. Relaxation oscillations in substrate-depletion oscillators close to the nonsmooth limit. Nonlinearity, 34(2):1030–1083, 2021.
- [44] M. Krupa and P. Szmolyan. Relaxation oscillation and canard explosion. Journal of Differential Equations, 174(2):312–368, 2001.
- [45] Yu. A. Kuznetsov, S. Rinaldi, and A. Gragnani. One parameter bifurcations in planar Filippov systems. Int. J. Bif. Chaos, 13:2157–2188, 2003.
- [46] C. Li and J. Llibre. Uniqueness of limit cycles for Liénard differential equations of degree four. J. Differential Equations, 252(4):3142–3162, 2012.
- [47] C.i Li and H. Zhu. Canard cycles for predator-prey systems with Holling types of functional response. J. Differential Equations, 254(2):879–910, 2013.
- [48] J. Li. Hilbert’s 16th problem and bifurcations of planar polynomial vector fields. International Journal of Bifurcation and Chaos in Applied Sciences and Engineering, 13(1):47–106, 2003.
- [49] T. Li and J. Llibre. On the 16th Hilbert Problem for Discontinuous Piecewise Polynomial Hamiltonian Systems. Journal of Dynamics and Differential Equations, pages 1–16, 2021.
- [50] A. Lins, W. de Melo, and C. C. Pugh. On Liénard’s equation. In Geometry and topology (Proc. III Latin Amer. School of Math., Inst. Mat. Pura Aplicada CNPq, Rio de Janeiro, 1976), pages 335–357. Lecture Notes in Math., Vol. 597. Springer, Berlin, 1977.
- [51] J. Llibre, A. C. Mereu, and M. A. Teixeira. Limit cycles of the generalized polynomial Liénard differential equations. Math. Proc. Cambridge Philos. Soc., 148(2):363–383, 2010.
- [52] J. Llibre, M. A. Teixeira, and J. Torregrosa. Lower bounds for the maximum number of limit cycles of discontinuous piecewise linear differential systems with a straight line of separation. International Journal of Bifurcation and Chaos, 23(4):1350066, 2013.
- [53] R. Roussarie and C. Rousseau. Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems. Trans. Moscow Math. Soc., pages 181–218, 2015.
- [54] S. Smale. Mathematical problems for the next century. In Mathematics: frontiers and perspectives, pages 271–294. Amer. Math. Soc., Providence, RI, 2000.
- [55] J. Sotomayor and M. A. Teixeira. Regularization of discontinuous vector fields. In Proceedings of the International Conference on Differential Equations, Lisboa, pages 207–223, 1996.
- [56] P. Szmolyan and M. Wechselberger. Canards in ℝ 3 \mathbb{R}^{3}. J. Diff. Eq., 177(2):419–453, December 2001.
- [57] V. I. Utkin. Variable structure systems with sliding modes. IEEE Trans. Automatic Control, 22:212–222, 1977.
- [58] C. Wang and X. Zhang. Stability loss delay and smoothness of the return map in slow-fast systems. SIAM J. Appl. Dyn. Syst., 17(1):788–822, 2018.
- [59] M. J. Álvarez, B. Coll, P. De Maesschalck, and R. Prohens. Asymptotic lower bounds on hilbert numbers using canard cycles. Journal of Differential Equations, 268(7):3370–3391, 2020.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
