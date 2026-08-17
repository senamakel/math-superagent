<!-- source: https://arxiv.org/html/2402.12506 | converted from HTML -->

On the monograph ”Finiteness Theorems for limit cycles” and a special case of alternant cycles

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2402.12506v1 [math.DS] 19 Feb 2024

# On the monograph ”Finiteness Theorems for limit cycles” and a special case of alternant cycles

Melvin Yeung

###### Abstract

We provide evidence that the approach of [11] to the proof of Dulac’s theorem has a gap. Although the asymptotics of [11] capture far more than the asymptotics of Dulac, we prove that the arguments for why the asymptotics in [11] are not themselves oscillatory is insufficient. We give an explicit counterexample and we draw confines to which Ilyashenko’s result may be restricted in order to keep the validity.

## 1 Introduction

Dulac’s theorem, asserted in [3] with a heavily flawed proof, states that the number of limit cycles of any given polynomial vector field on the plane is finite. It is a soft version of the second part of the 16th problem of Hilbert, asking for a (sharp) upper bound on the number of limit cycles in terms of the polynomial degree.

Let us sketch a very brief history, firmly restricting to Dulac’s conjecture and not widening the history to the 16th problem of Hilbert. For a more general overview of the 16th problem of Hilbert, including a wide variety of related problems, see [7].

In Dulac’s original paper, [3], several reductions were carried out, the primary reduction being based on Poincaré-Bendixson’s theorem. After compactifying the phase plane to a sphere, he noted that an unbounded sequence of limit cycles should accumulate to either an equilibrium, a periodic orbit, or a graphic (so a finite union of equilibria with orbits connecting them).

Because of compactness one only has to prove that limit cycles cannot accumulate onto any of the sets above. Ruling out the possibility of accumulating onto a periodic orbit is not difficult at all. On the other hand both equilibria and graphics contain an incredibly rich structure which can not immediately be studied. In order to study them anyway we use a version of a blowup at a point desingularizing them to elementary graphics which we will call polycycles. The price to pay here is that our polycycles are defined on 2-dimensional real analytic manifolds instead of just neatly on a sphere. It is worth noting that the fact that this process can be done in a finite number of steps was only proven much later, see e.g. [4].

Polycycles in this context are formed by a finite number of equilibria, all of them being hyperbolic or semi-hyperbolic (so with one nonzero eigenvalue) of the vector field, all of them being connected with regular heteroclinic or homoclinic connections (without additional singularities on the connections themselves). Without loss of generality we will only look at a single side of a polycycle at a time, so for example a cuspidal loop will be studied on the inside and the outside separately.

Dulac then proceeded to study compositions of transition maps defined near hyperbolic saddles or semi-hyperbolic saddles. Next Dulac made an additional, crucial, reduction to so-called balanced cycles. By grouping the semi-hyperbolic passages in groups of two, he showed the existence of an asymptotic expansion for these Dulac maps in terms of ( x, log ⁡ x) (x,\log x) and proved a group property of such maps. The mistake he made was to take the quasi-analyticity for granted: he inferred the triviality of the map from the triviality of its asymptotic expansion.

Ilyashenko in [9] produced a clever counter example, clearly showing why Dulac’s arguments failed and additionally he showed that Dulac’s theorem is valid for hyperbolic polycycles, i.e. polycycles with only hyperbolic equilibria. It is a corner stone in this story and up to date the only result that has not been questioned.

The author would like to thank Dmitry Novikov for helping him understand the quasianalyticity arguments of [11] and for the feedback on this article.

The author is very grateful to Daniel Panazzolo for organizing a workshop for the author to present his findings and for the feedback on this article.

The author thanks his promotor Peter de Maesschalck for introducing him to this problem and for the extensive feedback on this article.

The author is thankful to Yulij S. Ilyashenko for providing feedback on this article.

### 1.1 The known case and the main difficulty

#### 1.1.1 Hyperbolic polycycles

With the notion of almost regular map, Ilyashenko has successfully treated the hyperbolic case, see e.g. the introduction of [11]: almost regular maps are maps that are analytically continuable to a so-called standard quadratic domain, and that are asymptotic to a Dulac-asymptotic series inside this domain.

The size of the domain of the analytic continuation, together with the presence of the asymptotic series gives the quasianalyticity property: an almost regular map that is asymptotic to the identity map up to exponential accuracy, *is*the identity map.

Furthermore, almost regular maps form a group with respect to the composition so any first return map defined near some hyperbolic polycycle is actually an almost regular map. So either it is asymptotic to the identity (and then it is the identity, so near the polycycle all orbits are periodic), or it is not, and then by looking at the most dominant term in the expansion it is easy to conclude that there are no periodic orbits accumulating to the polycycle.

#### 1.1.2 Adding more depth

Semi-hyperbolic singularities present in the polycycle are much more delicate due to the exponential flatness of the Dulac map of a semi-hyperbolic saddle. The standard example being the following:

 | E ⁡ ( x) = e − 1 x E(x)=e^{-\frac{1}{x}} |  |

which is the Dulac map of:

 | { x ˙ = x 2 y ˙ = − y \begin{cases}\dot{x}=x^{2}\\ \dot{y}=-y\end{cases} |  |

from a section { y = 1 e } \left\{y=\frac{1}{e}\right\} transverse to the hyperbolic separatrix to a section { x = 1 } \{x=1\} transverse to the center separatrix, phase plane restricted to the positive quadrant. The point is that conjugation of a function f f with E E allows us to make flatter and flatter asymptotics, which may no longer be picked up if your asymptotics is not sensitive enough. Let us write a function:

 | f ⁡ ( x) = x + x 2 ​ f 1 ​ ( x). f(x)=x+x^{2}f_{1}(x). |  |

Then:

 | E − 1 ​ ( f ​ ( E ​ ( x)) CLOSE \displaystyle E^{-1}(f(E(x)) | = − 1 ln ⁡ ( E ⁡ ( x) + E ​ ( x) 2 ​ f 1 ​ ( E ⁡ ( x))) \displaystyle=\frac{-1}{\ln\left(E(x)+E(x)^{2}f_{1}(E(x))\right)} |  |

 |  | = − 1 − 1 x + ln ⁡ ( 1 + E ⁡ ( x) ​ f 1 ​ ( E ⁡ ( x))) \displaystyle=-\frac{1}{-\frac{1}{x}+\ln(1+E(x)f_{1}(E(x)))} |  |

 |  | = x ​ 1 1 − x ​ ln ⁡ ( 1 + E ⁡ ( x) ​ f 1 ​ ( E ⁡ ( x))). \displaystyle=x\frac{1}{1-x\ln(1+E(x)f_{1}(E(x)))}. |  |

This function is identity + + flat terms, thus having Dulac series x x but nonetheless not being equal to x x. More complicated examples are certainly possible, think for example of a cycle giving first return map:

 | E − 1 ∘ f ∘ E ∘ g ∘ E − 1 ∘ E − 1 ∘ h ∘ E ∘ E. E^{-1}\circ f\circ E\circ g\circ E^{-1}\circ E^{-1}\circ h\circ E\circ E. |  |

Note that by glueing as in [11, §0.3 C] such a polycycle should definitely exist on some 2-dimensional real analytic manifold.

Now we see an interplay of three levels of asymptotics: level 0 coming from g g, level 1 coming from E − 1 ∘ f ∘ E E^{-1}\circ f\circ E and level 2 coming from E − 2 ∘ h ∘ E 2 E^{-2}\circ h\circ E^{2}. It should however by clear by now why so-called unbalanced cycles are easily dealt with: either they are flat or inverse to flat. While in specific situations a clever choice of transversal or looking at the difference map with respect to two transversals instead of the return map can resolve some issues, in general no level of flatness can be ignored.

### 1.2 Current state of the proofs

#### 1.2.1 Commonalities

Before diving into the differences of the two proofs in [5] and the main subject of the article today [11] we will first talk in broad terms about what both approaches share.

The consensus holds that the spirit of the proof of Dulac was correct, what one should do is to find sufficiently accurate asymptotics for first return maps of polycycles in order to determine the whole map.

Note that it is in the first place not clear what asymptotics should mean in this context, for example the previous section makes clear that it should be necessary to know what it means for a map to be asymptotic to:

 | ( ∑ n ≥ 0 n! ​ x n) + e − 1 x. \left(\sum_{n\geq 0}n!x^{n}\right)+e^{-\frac{1}{x}}. |  |

The consensus between [5] and [11] is also that (in the real analytic context) formal information should be enough to determine these asymptotics in the following sense: Suppose given a semihyperbolic saddle, then there are formal coordinates (i.e. a coordinate transform in terms of diverging power series) such that it is orbitally equivalent to a semihyperbolic saddle of the form:

 | { x ˙ = x k + 1 1 + a ​ x k y ˙ = − y \begin{cases}\dot{x}=\frac{x^{k+1}}{1+ax^{k}}\\ \dot{y}=-y\end{cases} |  |

they agree that what one should do is compose the asymptotics coming from the formal normalization maps, the transit maps of the normal forms above, the usual Dulac series for the hyperbolic saddles and the Taylor series for the transit maps.

This gives an expression called a transseries, a formal object that is able to represent asymptotic information “at different depths”. The notion of transseries is defined explicitly in [5] and contained implicitly in [11] under the name STAR-series. A STAR-series is not exactly the same as a transseries, it is a mix of both the asymptotic information above and the way to construct a sensible asymptotic series for the first return map of a polycycle.

Transseries has been the center of quite vibrant research including a recent result linking this to O-minimality, see [1], offering a road forward to the 16th problem of Hilbert once the roadblock of understanding these proofs have passed. It is also worth noting that transseries have been used in contexts more explicitly related to the problem of Dulac, for example in [6]. An older result in the same vein [12] in fact gives uniform bounds for limit cycles close to a polycycle with only nonresonant hyperbolic saddles.

The strategy in [5] and [11] is to recast the transserial formal asymptotics in a form which says something meaningful about the functions they are describing, i.e. return maps of polycycles. There should be at minimum two properties of these asymptotics:

1. 1.

If they are nonzero they should give a leading term.

2. 2.

If they are zero they should only describe the zero function, i.e. the quasianalyticity property.

#### 1.2.2 Ecalle’s approach

In their essence, the asymptotic objects of Ecalle are simple, they are the transseries we spoke of. Thus simply assuming compatibility with the addition, we can just take out the leading term in any nonzero transseries by standard theory, see e.g. [1], giving leading terms for nonzero transseries.

The part that remains difficult is the claims of quasianalyticity. From what the author understands of the matter the claim is that [5] provides an injection from a certain class of transseries, called accelero-summable transseries, into germs of functions near infinity (the polycycle return maps being brought there under the coordinate transform 1 x \frac{1}{x}). It is worth noting that transseries in [5] are not exactly the same as in [1] but are instead more general, see [5, p 149, (4.1.59)] for a transseries not included in [1].

Again, from what the author understands, in [5, Chapter 5], something called cryptolinear formulas are introduced which split up transseries into blocks which are individually amenable to a generalized version of a Borel transform, which after a change of coordinates is amenable to a Laplace transform which needs to be ‘accelerated back into the right time’ and then everything can be summed back up, this process should then be accelero-summation, giving the injection above.

While at the time of writing, Ecalle’s proof, [5] is still not being debated, the proof has not been digested by the community either, and although many of Ecalle’s claims have meanwhile been properly proved by others using his methods, see e.g. [2], [14], his proof of Dulac’s theorem is still waiting for an accessible and detailed version.

Considering the amount of effort put into this problem, it is hard to believe that in all this time no one has been able to draw a detailed proof from the texts provided by Ecalle. In some sense, this calls for a following conjecture:

###### Conjecture 1.1.

[5] can be worked out to a fully detailed proof without additional difficulties.

In particular looking at [5, page 157-158] the case of convergent normalizing maps is mentioned and in this case the claim is that this can be ‘naively summed’ as described in [5, pp. 142-143] which seems a much more conventional definition. Perhaps it would be interesting to work out this case first.

#### 1.2.3 Ilyashenko’s approach

Conversely the proof in [11] has a very good answer for why the quasianalyticity should hold, in an extension of his proof in the hyperbolic case the answer is simply that the return maps of polycycle can be decomposed into function which have small Stokes phenomena on a large domain, the domains being large enough and the Stokes phenomena being small enough that it implies quasi-analyticity.

Seeing as this is the main subject of the current article we will refrain from technical detail in this part.

Recently, Ilyashenko has come to realize a flaw in his proof himself, and he communicated openly on this matter during a conference at the Fields institute in 2021. The flaw communicated by Ilyashenko lies in the fact that while any semihyperbolic saddle can be analytically conjugated to a system of the form:

 | { x ˙ = x k + 1 1 + a ​ x k y ˙ = − y \begin{cases}\dot{x}=\frac{x^{k+1}}{1+ax^{k}}\\ \dot{y}=-y\end{cases} |  |

this conjugation does not necessarily map the real axis to the real axis. In particular in the cases where the domain is large enough to complete his quasianalyticity arguments, it is known that the conjugation maps in general do not map the real axis to the real axis. In fact, as is shown in [13], reality is the exception rather than the norm.

This results in the fact that the asymptotics in [11] are complex valued. In order to try to keep closer to the ordered field of the reals and get leading terms anyway [11] essentially uses the construction that for any complex analytic function f f on the real axis the function:

 | z ↦ f ⁡ ( z) + f ⁡ ( z ¯) ¯ 2 z\mapsto\frac{f(z)+\overline{f(\bar{z})}}{2} |  |

is a real analytic function which is Re ⁡ ( f) \re(f) on the real axis. The problem Ilyashenko has communicated is that this can not be done while preserving the needed quasi-analyticity properties.

In 2020, the author took on the challenge to attempt to both salvage the problem and to make Ilyashenko’s proof more accessible. (In fact, the challenge first consisted solely of the second part, but the communication of the flaw in the proof added an extra level.) He succeeded in giving an easier presentation, immediately restricting to the case where the real axis gets normalized to the real axis.

Nevertheless the author was able to verify that the quasi-analyticity argument of [11] holds even in full generality for all polycycles, it was the existence of a leading term which was an issue.

Shortly after the author communicated his findings at a workshop in Mulhouse, France, he found an additional mistake of Ilyashenko’s proof (which corresponds to a gap in his own version of the proof). This mistake pertains to the existence of a leading term coming from the asymptotics given in [11]. In some sense unlike the conjecture before which was possibly born of insufficient understanding, we have been able to understand enough of [11] to prove in this article that:

###### Statement 1.2.

The proof for Dulac’s theorem, provided by Ilyashenko in [11], cannot be worked out to full detail without additional difficulties.

In particular here the difficulties lie in the existence of a leading term for a nonzero asymptotic series.

It is a new element that casts a shadow on all proofs. What is worse is that the presence of two independent proofs of Dulac’s result blocked any further development on the matter, except for some spurious cases. Partial results, for example for polycycles with exactly two semi-hyperbolic points (see [10]), have therefore not had the amount of attention that they should have had.

Even so, just like [11] and [5] saw it fit to continue the approach of [3] and try to fill in the gaps because of the inherent value of the arguments of [3], the author feels that [11] is valuable. Specifically the entire approach laid out in [11] working towards the Additive Decomposition Theorem [11, p 73] using Shift Lemma’s should be worked out to completion, filling in as much as possible the gap laid out in this article. This roughly corresponds to the arguments in Sections 3 and 4 of this article.

In a personal communication with Ilyashenko, he announced a work in progress, [8], aiming to cover the so-called depth 1 or alternant case (more on this later) with a new method that avoids the arguments of [11, §4.10] as a possible answer to the reality issues mentioned earlier. Instead choosing an approach based on normal forms, Ilyashenko is aiming at addressing the extra difficulties announced in Statement 1.2 and bypassing Statement 2.1 as well, in the alternant case.

## 2 Goals

###### Statement 2.1.

At the core of the existence of a leading term for a Dulac map we have identified and isolated the following incorrect claim at the end of [11, p 198] that (calculation error corrected in the last term):

 | a 1 ′ ​ a 2 − a 1 ​ a 2 ′ + 𝐞 ′ ​ a 1 ​ a 2 ∈ 𝒦 ℝ m, r a_{1}^{\prime}a_{2}-a_{1}a_{2}^{\prime}+\mathbf{e}^{\prime}a_{1}a_{2}\in\mathscr{K}^{m,r}_{\mathbb{R}} |  |

which is at the core of the existence of a leading term for a Dulac map in the way the proof goes in [11].

The statement above may seem banal at a glance, yet here we make the claim that it is at the core of the existence of a leading term, so we will first dedicate most of the text to explaining why this is at the core of the proof.

We will do this restriction to a much simpler class of polycycles than the general case and simplifying the arguments of [11] to this context.

###### Statement 2.2.

The problem isolated in Statement 2.1 already occurs in polycycles satisfying the following conditions:

1. 1.

All equilibria in the polycycle are for some k ≥ 1 k\geq 1, locally real analytically orbitally equivalent to the following system at the origin (in forward or backward time):

 | { x ˙ = x k + 1 y ˙ = − y. \begin{cases}\dot{x}=x^{k+1}\\ \dot{y}=-y.\end{cases} |  |

2. 2.

The equilibria ‘alternate’ in the following sense, suppose that one equilibrium is traversed going from the hyperbolic side to the center side, i.e. in the system above coming from y > 0, x y>0,x small positive going to to x > 0, y x>0,y small positive, then the next orbit in forward time will be traversed going from the center side to the hyperbolic side.

This is a special case of so-called alternant polycycles, term coined by Ilyashenko, where all semihyperbolic saddles/saddle nodes in the polycycle satisfy the second condition.

Therefore we will call these polycycles simple alternant polycycles.

###### Remark 2.3.

Alternant polycycles are exactly the depth 1 case that the article in preparation [8] will cover.

In the simplification of these arguments we will deviate from [11] in the sense that we will talk in terms of minimal conditions for the arguments of [11] to work, i.e. for the central result, the additive decomposition theorem ( [11, p 73]) to work rather than the explicit classes that are given in [11].

We want to show that complications as in point 1 1 are absolutely impossible to avoid in the methods of [11].

Then we will present our counterexample in section 6.

Next we will restrict a bit further, nonetheless to a case not covered by the well-known arguments of [11], i.e. the hyperbolic case, and we will show that these arguments do work in this case.

###### Statement 2.4.

For simple alternating polycycles where every equilibrium is real analytically orbitally equivalent to:

 | { x ˙ = x 2 y ˙ = − y. \begin{cases}\dot{x}=x^{2}\\ \dot{y}=-y.\end{cases} |  |

The difficulty with statement 2.1 disappears and the proof of [11] is valid.

Let us describe the structure of the article. Sketching out the proof of [11] will take in the next three sections coinciding roughly with the three large parts of the proof of [11]:

1. 1.

In Section 3 we will prove the Structural Theorem which can be roughly considered all the ‘dynamics’ of [11], after this section we might as well forget we are talking about polycycles.

2. 2.

In Section 4 we will present all of the formal manipulations in [11], roughly corresponding to [11, §1.11].

3. 3.

In Section 5 we will define what in our case would be the 𝒦 ℝ m, r \mathscr{K}^{m,r}_{\mathbb{R}} of Statement 2.1 and we will explain why Statement 2.1 is crucial in the existence of a leading term, essentially expositing the arguments in [11, §4.10].

Then we will provide the counterexample to Statement 2.1 in Section 6, followed by proving Statement 2.4 in Section 7, even though most of the work happens in Section 6.

## 3 Splitting up the return map and the logarithmic chart

The first step in the proof following [11] is to split up the return map into transit maps. By definition of simple alternant polycycle near each equilibrium E i E_{i} there exists real analytic sections Σ i ​ 1, Σ i ​ 2 \Sigma_{i1},\Sigma_{i2} transversally crossing the separatrices for which the transition map T i T_{i} is either given by:

 | z ↦ e − 1 z k i z\mapsto e^{-\frac{1}{z^{k_{i}}}} |  |

for some k i ≥ 1 k_{i}\geq 1 or its inverse:

 | z ↦ ( 1 − ln ⁡ ( z)) 1 k i. z\mapsto\left(\frac{1}{-\ln\left(z\right)}\right)^{\frac{1}{k_{i}}}. |  |

Suppose the equilibria ordered from 1 1 to N N in order of which we encounter them. We will assume the transversal Σ \Sigma relative to which we take the Dulac map to be Σ N ​ 2 \Sigma_{N2}.

Figure 1: Decomposition of a first return map of a simple alternant polycycle. The arrows on the separatrices are double for a hyperbolic separatrix and single for a center separatrix.

Let f i, j f_{i,j} be the analytic flow box map from Σ i ​ 2 \Sigma_{i2} to Σ j ​ 1 \Sigma_{j1}, then the return map Δ \Delta is given by

 | Δ = T N ∘ f N − 1, N ∘ T N − 1 ∘ ⋯ ∘ T 1 ∘ f N, 1. \Delta=T_{N}\circ f_{N-1,N}\circ T_{N-1}\circ\cdots\circ T_{1}\circ f_{N,1}. |  |

Now we may assume without loss of generality (by rechoosing Σ \Sigma) we start on a hyperbolic separatrix, i.e. T 1 = e − 1 z k 1 T_{1}=e^{-\frac{1}{z^{k_{1}}}}.

The next step is to introduce the so-called logarithmic chart, basically because the maps e − 1 z e^{-\frac{1}{z}} and 1 − ln ⁡ ( z) \frac{1}{-\ln(z)} are very complicated, the second one even implying a branch cut of the logarithm. In order to simplify these we introduce the logarithmic chart:

 | ζ = − ln ⁡ ( z). \zeta=-\ln(z). |  |

For a function g g in the usual z z chart we denote its counterpart in the logarithmic chart by g log g^{\log}, more concretely:

 | g log ​ ( ζ) = − ln ⁡ ( g ⁡ ( e − ζ)). g^{\log}(\zeta)=-\ln(g(e^{-\zeta})). |  |

Now note that ( z ↦ e − 1 z) log = ζ ↦ e ζ \left(z\mapsto e^{-\frac{1}{z}}\right)^{\log}=\zeta\mapsto e^{\zeta} and ( z ↦ 1 − ln ⁡ ( z)) log = ζ ↦ ln ⁡ ( ζ) \left(z\mapsto\frac{1}{-\ln(z)}\right)^{\log}=\zeta\mapsto\ln(\zeta).

As for transit maps between transversals on the same orbit, they are holomorphic maps with zero constants, by flow box they are even analytic functions with nonzero positive derivative let f ⁡ ( z) = α ​ z + ∑ q ≥ 0 a q ​ z q + 2 f(z)=\alpha z+\sum_{q\geq 0}a_{q}z^{q+2}, α > 0 \alpha>0:

 | f log ​ ( ζ) = − ln ⁡ ( α ​ e − ζ + ∑ q ≥ 0 a q ​ e − ( q + 2) ​ ζ) = ζ − ln ⁡ ( α) − ln ⁡ ( 1 + ∑ q ≥ 0 a q α ​ e − ( q + 1) ​ ζ). f^{\log}(\zeta)=-\ln\left(\alpha e^{-\zeta}+\sum_{q\geq 0}a_{q}e^{-(q+2)\zeta}\right)=\zeta-\ln(\alpha)-\ln\left(1+\sum_{q\geq 0}\frac{a_{q}}{\alpha}e^{-(q+1)\zeta}\right). |  |

Thus f log f^{\log} has an expansion in terms of e − k ​ ζ e^{-k\zeta} with constant coefficients. Let R R be the radius of convergence of f f, then this expansion is valid for a a large enough in:

 | ℂ a + ≔ { ζ ∈ ℂ ∣ Re ⁡ ( z) ≥ a }. \mathbb{C}_{a}^{+}\coloneqq\{\zeta\in\mathbb{C}\mid\re(z)\geq a\}. |  |

Indeed, note that going into the logarithmic chart turns small discs around the origin into half planes of the form ℂ a + \mathbb{C}_{a}^{+}.

As for the map h: z ↦ z α h:z\mapsto z^{\alpha}:

 | h log ​ ( ζ) = α ​ ζ. h^{\log}(\zeta)=\alpha\zeta. |  |

This means that going through an equilibrium from the hyperbolic side is given in the logarithmic chart first by multiplication by k k, then by the exponential function, and for going through an equilibrium from the center side it is division by k k composed with the logarithm.

Based on these two calculations we introduce two classes of functions:

###### Definition 3.1.

Let us define 𝒜 ​ ff \Aff to be the set of all maps of the form:

 | ζ ↦ α ​ ζ + β \zeta\mapsto\alpha\zeta+\beta |  |

with α, β ∈ ℝ \alpha,\beta\in\mathbb{R} and α > 0 \alpha>0.

###### Definition 3.2.

Let us define ℋ \mathcal{H} to be the set of analytic functions f f for which there exists some series:

 | ζ + ∑ q ≥ 0 b q ​ e − c q ​ ζ \zeta+\sum_{q\geq 0}b_{q}e^{-c_{q}\zeta} |  |

b k, c k ∈ ℝ b_{k},c_{k}\in\mathbb{R}, c k > 0 c_{k}>0 and strictly increasing to + ∞ +\infty, such that for some a ≥ 0 a\geq 0, for any ζ ∈ ℂ a + \zeta\in\mathbb{C}^{+}_{a} and for any N > 0 N>0 and any ϵ ∈ ( 0, c N + 1 − c N) \epsilon\in(0,c_{N+1}-c_{N}) we have:

 | | f ⁡ ( ζ) − ( id + ∑ q = 0 N b k ​ e − c q ​ ζ) | ≤ e − ( c N + ϵ) ​ Re ⁡ ( ζ). \left|f(\zeta)-\left(\id+\sum_{q=0}^{N}b_{k}e^{-c_{q}\zeta}\right)\right|\leq e^{-(c_{N}+\epsilon)\re(\zeta)}. |  |

We call the series above the Dulac series of f f. (It is in fact true as we will elaborate on later, that this series is unique if it exists.)

Obviously we need these definitions because any Dulac map can be decomposed into these maps together with exp \exp and ln \ln.

## 4 Strategy of proof

Let us take a closer look at the structure of these return maps Δ \Delta. We made the condition that the transit map of any equilibrium we pass is either of exponential type or of logarithmic type and that they alternate.

We also made the condition that these types alternate, there are an even amount of equilibria and we assumed the first type we encountered was of exponential type. Let ⟨. ⟩ \langle.\rangle be the group of germs of real analytic functions generated by the functions between the brackets under composition, then:

 | Δ ∈ ⟨ 𝒜 ​ ff, ℋ, ln ∘ 𝒜 ​ ff ∘ ℋ ∘ exp ⟩. \Delta\in\langle\Aff,\mathcal{H},\ln\circ\Aff\circ\mathcal{H}\circ\exp\rangle. |  |

We can simplify this a bit further by noting that:

 | ln ∘ 𝒜 ​ ff ∘ ℋ ∘ exp = ln ∘ 𝒜 ​ ff ∘ exp ∘ ln ∘ ℋ ∘ exp. \ln\circ\Aff\circ\mathcal{H}\circ\exp=\ln\circ\Aff\circ\exp\circ\ln\circ\mathcal{H}\circ\exp. |  |

And let a ∈ 𝒜 ​ ff, a ⁡ ( x) = α ​ x + β a\in\Aff,a(x)=\alpha x+\beta, then:

 | ln ⁡ ( a ⁡ ( e ζ)) = ln ⁡ ( α ​ e ζ + β) = ζ + ln ⁡ ( α) + ln ⁡ ( 1 + β α ​ e − ζ) \ln(a(e^{\zeta}))=\ln(\alpha e^{\zeta}+\beta)=\zeta+\ln(\alpha)+\ln\left(1+\frac{\beta}{\alpha}e^{-\zeta}\right) |  |

thus ln ∘ 𝒜 ​ ff ∘ exp ∈ ℋ \ln\circ\Aff\circ\exp\in\mathcal{H}. Thus we have:

###### Theorem 4.1 (Structural Theorem, specific case).

Let A A stand for conjugation by exp \exp, i.e.:

 | A ( h) = ln ∘ h ∘ exp. A(h)=\ln\circ h\circ\exp. |  |

All Dulac maps of the polycycles we study are contained in:

 | ⟨ 𝒜 ​ ff, ℋ, A ​ ℋ ⟩. \langle\Aff,\mathcal{H},A\mathcal{H}\rangle. |  |

###### Remark 4.2.

This is a specific case of [11, §1.3 Proposition 3].

The idea of [11] is this: 𝒜 ​ ff \Aff is far from identity, but ℋ \mathcal{H} is close to identity and A ⁡ ( ℋ) A(\mathcal{H}) is even closer to identity. More concretely, any element of ℋ \mathcal{H} can be written as id + ϕ \id+\phi with ϕ \phi exponentially small and any element of A ⁡ ( ℋ) A(\mathcal{H}) can be written as id + ψ ∘ exp \id+\psi\circ\exp with ψ \psi exponentially small, simply by applying A A to the Dulac series of an element in ℋ \mathcal{H}.

The set of elements ϕ \phi and ψ \psi we are willing to allow will be called functional cochains, the set of ϕ \phi will be F ​ C 0 FC^{0}, functional cochains of level 0 0 and the set of ψ \psi will be F ​ C 1 FC^{1}, functional cochains of level 1 1.

###### Remark 4.3.

In [11] there is a further distinction between F ​ C 0 n FC^{n}_{0} and F ​ C 1 n FC^{n}_{1} which has to do with general semihyperbolic saddles/saddle nodes not being real analytically orbitally equivalent to the system we have here. This messes with domains as soon as you encounter n + 1 n+1 more exponential type saddles than logarithmic type at some point along the Dulac map. In some sense the F ​ C 0 n FC^{n}_{0} are the ones with large domain and F ​ C 1 n FC^{n}_{1} are the ones with small domain.

The idea is this, it is possible to expand all these compositions into sums using a lot of Taylor expansions and if we had a sum such as:

 | a + ϕ + ψ ∘ exp a+\phi+\psi\circ\exp |  |

then a a could not interfere with ϕ \phi, ϕ \phi could not interfere with ψ \psi, because they are all of intrisically different sizes, so we could look in this sum for leading terms because we have separated the ‘levels of asymptotics’ which we talked about in the introduction. So what we are looking for is a way to expand these compositions into sums ‘split by levels of asymptotics’ indeed roughly corresponding to how 𝒜 ​ ff \Aff is far from the identity, ℋ \mathcal{H} is close to the identity and A ​ ℋ A\mathcal{H} is even much closer. This is the point of the so-called additive decomposition theorem [11, p 73].

For this idea there are five crucial properties we want F ​ C 0 FC^{0} to satisfy:

1. 1.

ℋ ⊆ id + F ​ C 0 \mathcal{H}\subseteq\id+FC^{0}.

2. 2.

Let a ∈ 𝒜 ​ ff a\in\Aff, then:

 | a ∘ ( id + F ​ C 0) ∘ a − 1 ⊆ id + F ​ C 0. a\circ(\id+FC^{0})\circ a^{-1}\subseteq\id+FC^{0}. |  |

3. 3.

Let a ∈ 𝒜 ​ ff a\in\Aff, then:

 | a ∘ ( id + F ​ C 0) ⊆ a + F ​ C 0. a\circ(\id+FC^{0})\subseteq a+FC^{0}. |  |

4. 4.

( id + F ​ C 0) (\id+FC^{0}) forms a group under composition.

5. 5.

Let ϕ ∈ F ​ C 0 \phi\in FC^{0} be nonzero then there exists some λ > 0 \lambda>0 such that for x ∈ ℝ x\in\mathbb{R} large enough:

 | | ϕ ⁡ ( x) | ≥ e − λ ​ x. |\phi(x)|\geq e^{-\lambda x}. |  |

The F ​ C 0 FC^{0} proposed in [11] simplifies down to the following:

###### Definition 4.4.

The set F ​ C 0 FC^{0} is the set of analytic functions satisfying the same conditions as ℋ \mathcal{H} with Dulac series of the form:

 | ∑ q ≥ 0 b q ​ e − c q ​ ζ. \sum_{q\geq 0}b_{q}e^{-c_{q}\zeta}. |  |

###### Remark 4.5.

In [11] there could also be hyperbolic equilibria in the polycycle, this complicates both the domain and the asymptotics, we will not get into the domain, as for the asymptotics, the b q b_{q} are replaced by (complex) polynomials in ζ \zeta.

###### Remark 4.6.

We will for ease of notation restrict ourselves to the F ​ C n FC^{n} which are exponentially decreasing themselves. This is not the case in [11], but wherever that is relevant we will instead choose to write out very concretely what happens in [11].

More specifically if we were to follow the notation of [11] then F ​ C 0 FC^{0} would be the above set without the restriction that c 0 > 0 c_{0}>0 and the set we describe here would be F ​ C + 0 FC^{0}_{+}.

By some routine calculation it is possible to verify all five conditions, upon being given the following (see e.g. [11, §3.1 Corollary 1])

###### Theorem 4.7.

Let f f be a bounded holomorphic function on ℂ 0 + \mathbb{C}^{+}_{0} decreasing faster than any exponential on the real axis, then f f is identically zero.

The argument essentially being the following, suppose ϕ ∈ F ​ C 0 \phi\in FC^{0} has a nonzero series, then by leading term we get the exponential lower bound we want. Suppose this asymptotic series is zero, then ϕ \phi is smaller than any exponential on the real axis and bounded, thus identically zero.

The way we get the promised sum out of these properties is the following, suppose that we have a particularly nice Δ \Delta, in the sense that it is inside ⟨ 𝒜 ​ ff, ℋ ⟩ \langle\Aff,\mathcal{H}\rangle, then using these properties we can conjugate elements of 𝒜 ​ ff \Aff past elements of ( id + F ​ C 0) ⊃ ℋ (\id+FC^{0})\supset\mathcal{H} and expand in order to write:

 | Δ ∈ 𝒜 ​ ff + FC 0. \Delta\in\Aff+FC^{0}. |  |

###### Remark 4.8.

This is a version of the central Theorem that [11] works towards, it is a consequence of A ​ D ​ T 1 ADT_{1} as stated in [11, p 73]

Then Δ − id \Delta-\id is in the same set and either 𝒜 ​ ff − id \Aff-\id is nonzero, giving a zero free region because an element of F ​ C 0 FC^{0} is much smaller, or F ​ C 0 FC^{0} is nonzero and 𝒜 ​ ff − id \Aff-\id is zero, giving by the lower bound of F ​ C 0 FC^{0} a zero free region, or Δ − id ≡ 0 \Delta-\id\equiv 0, thus it having no isolated zeroes.

This is essentially a leading term argument dating back in a flawed form to the arguments of Dulac.

We now want to continue this story of rearranging by conjugation and writing out as a sum, where we replace A ​ ℋ A\mathcal{H} by id + F C 1 ∘ exp \id+FC^{1}\circ\exp, this is exactly what we do with elements of ( id + F ​ C 0) (\id+FC^{0}), but with 𝒜 ​ ff \Aff the story is slightly different.

Taking an element f ∈ A ​ ℋ f\in A\mathcal{H} we can quickly calculate the series it has:

 | f ⁡ ( ζ) \displaystyle f(\zeta) | = ln ⁡ ( e ζ + ∑ q ≥ 0 b q ​ e − q ​ e ζ) \displaystyle=\ln\left(e^{\zeta}+\sum_{q\geq 0}b_{q}e^{-qe^{\zeta}}\right) |  |

 |  | = ζ + ln ⁡ ( 1 + ∑ q ≥ 0 b q ​ e − ζ ​ e − q ​ e ζ) \displaystyle=\zeta+\ln\left(1+\sum_{q\geq 0}b_{q}e^{-\zeta}e^{-qe^{\zeta}}\right) |  |

 |  | = ζ + ∑ q ≥ 0 P q ​ ( e − ζ) ​ e − c q ​ e ζ \displaystyle=\zeta+\sum_{q\geq 0}P_{q}(e^{-\zeta})e^{-c_{q}e^{\zeta}} |  |

with P k P_{k} being polynomials, c k > 0 c_{k}>0, strictly increasing to + ∞ +\infty. The last step going by Taylor expansion, which is fine as soon as we restrict the domain to some ln ⁡ ( ℂ a +) \ln(\mathbb{C}_{a}^{+}). Then f − id f-\id is roughly of order e − λ ​ exp ⁡ ( ζ) e^{-\lambda\exp(\zeta)} for some λ > 0 \lambda>0. Let a ∈ 𝒜 ​ ff a\in\Aff, a ⁡ ( ζ) = α ​ ζ + β a(\zeta)=\alpha\zeta+\beta, then:

 | ( a − 1 ∘ f ∘ a) ​ ( ζ) = ζ + ∑ k ≥ 0 P ~ k ​ ( e − α ​ ζ) ​ e − c ~ k ​ e α ​ ζ. (a^{-1}\circ f\circ a)(\zeta)=\zeta+\sum_{k\geq 0}\tilde{P}_{k}(e^{-\alpha\zeta})e^{-\tilde{c}_{k}e^{\alpha\zeta}}. |  |

So if α ≠ 1 \alpha\neq 1, then this is roughly of size e − λ ​ e α ​ ζ e^{-\lambda e^{\alpha\zeta}} for some λ > 0 \lambda>0, which is of essentially different size than e − μ ​ e ζ e^{-\mu e^{\zeta}} for all μ > 0 \mu>0. So should we want as in [11] that F ​ C 1 FC^{1} has exponential upper and lower bound, then:

 | a − 1 ∘ ( id + F C 1 ∘ exp) ∘ a ⊈ id + F C 1 ∘ exp. a^{-1}\circ(\id+FC^{1}\circ\exp)\circ a\not\subseteq\id+FC^{1}\circ\exp. |  |

At best we can expect the following, let m α m_{\alpha} be the map ζ ↦ α ​ ζ \zeta\mapsto\alpha\zeta, then we can ask for:

 | a − 1 ∘ ( id + F C 1 ∘ exp) ∘ a ⊆ id + F C 1 ∘ exp ∘ m α. a^{-1}\circ(\id+FC^{1}\circ\exp)\circ a\subseteq\id+FC^{1}\circ\exp\circ m_{\alpha}. |  |

###### Remark 4.9.

This choice to hold on to the exponential lower and upper bound instead of making one big F ​ C 1 FC^{1} is something intimately related to the quasianalyticity properties.

The reason the quasianalyticity property in [11] works is that after extending using small Stokes phenomena we get control of the functions in F ​ C n FC^{n} up to a a domain of ‘essentially the same size as ℂ a + \mathbb{C}^{+}_{a} ’, in the sense that Theorem 4.7 holds for the domain. The point is then that because the Stokes phenomena are so small, essentially ‘one level of asymptotics lower’ then any element of F ​ C n FC^{n} smaller than any exponential on the real axis will be identically zero on the real axis.

In the case we were to let go of the exponential lower bound and merge all the F ​ C 1 FC^{1} we would have functions of size e − x α e^{-x^{\alpha}} for all α > 0 \alpha>0, in particular for α > 1 \alpha>1 we would have things smaller than any exponential, so we would ruin all quasianalyticity arguments.

Then the minimal list of conditions on F ​ C 1 FC^{1} is the following, essentially taken from the conditions needed in [11, §1.11]:

1. 1.

A ℋ ⊆ id + F C 1 ∘ exp A\mathcal{H}\subseteq\id+FC^{1}\circ\exp.

2. 2.

Let α > 0 \alpha>0 and m α m_{\alpha} be multiplication with α \alpha. Then:

  1. (a)

id + F C 1 ∘ exp ∘ m α \id+FC^{1}\circ\exp\circ m_{\alpha} is a group under composition.

  2. (b)

Let f ∈ id + F ​ C 0 f\in\id+FC^{0}, then:

 | f − 1 ∘ ( id + F C 1 ∘ exp ∘ m α) ∘ f ⊆ id + F C 1 ∘ exp ∘ m α. f^{-1}\circ(\id+FC^{1}\circ\exp\circ m_{\alpha})\circ f\subseteq\id+FC^{1}\circ\exp\circ m_{\alpha}. |  |

  3. (c)

Let a ∈ 𝒜 ​ ff a\in\Aff:

 | a ∘ ( id + F C 1 ∘ exp ∘ m α) ⊆ a + F C 1 ∘ exp ∘ m α. a\circ(\id+FC^{1}\circ\exp\circ m_{\alpha})\subseteq a+FC^{1}\circ\exp\circ m_{\alpha}. |  |

  4. (d)

Let ϕ ∈ F ​ C 0 \phi\in FC^{0}:

 | ϕ ∘ ( id + F C 1 ∘ exp ∘ m α) ⊆ ϕ + F C 1 ∘ exp ∘ m α. \phi\circ(\id+FC^{1}\circ\exp\circ m_{\alpha})\subseteq\phi+FC^{1}\circ\exp\circ m_{\alpha}. |  |

3. 3.

Let α 1 > α 2 > 0 \alpha_{1}>\alpha_{2}>0 and let m α i m_{\alpha_{i}} be multiplication with α i \alpha_{i}. Then:

  1. (a)

Let f ∈ id + F C 1 ∘ exp ∘ m α 2 f\in\id+FC^{1}\circ\exp\circ m_{\alpha_{2}}, then:

 | f − 1 ∘ ( id + F C 1 ∘ exp ∘ m α 1) ∘ f ⊆ id + F C 1 ∘ exp ∘ m α 1. f^{-1}\circ(\id+FC^{1}\circ\exp\circ m_{\alpha_{1}})\circ f\subseteq\id+FC^{1}\circ\exp\circ m_{\alpha_{1}}. |  |

  2. (b)

Let g ∈ F C 1 ∘ exp ∘ m α 2 g\in FC^{1}\circ\exp\circ m_{\alpha_{2}}, then:

 | g ∘ ( id + F C 1 ∘ exp ∘ m α 1) ⊆ g + F C 1 ∘ exp ∘ m α 1. g\circ(\id+FC^{1}\circ\exp\circ m_{\alpha_{1}})\subseteq g+FC^{1}\circ\exp\circ m_{\alpha_{1}}. |  |

  3. (c)

Let i, j = 1, 2 i,j=1,2, let a ∈ 𝒜 ​ ff a\in\Aff, a ⁡ ( ζ) = α i ​ ζ + β a(\zeta)=\alpha_{i}\zeta+\beta, then:

 | a − 1 ∘ ( id + F C 1 ∘ exp ∘ m α j) ∘ a ⊆ id + F C 1 ∘ exp ∘ m α j ∘ m α i. a^{-1}\circ(\id+FC^{1}\circ\exp\circ m_{\alpha_{j}})\circ a\subseteq\id+FC^{1}\circ\exp\circ m_{\alpha_{j}}\circ m_{\alpha_{i}}. |  |

4. 4.

Let ψ ∈ F ​ C 1 \psi\in FC^{1} be nonzero then there exists some λ > 0 \lambda>0 such that for x ∈ ℝ x\in\mathbb{R} large enough:

 | | ψ ⁡ ( x) | ≥ e − λ ​ x. |\psi(x)|\geq e^{-\lambda x}. |  |

The idea is the same, you conjugate past and expand until you can write every Dulac map Δ \Delta as:

 | Δ ∈ 𝒜 ​ ff + FC 0 + ∑ p = 1 q FC 1 ∘ exp ∘ m α p \Delta\in\Aff+FC^{0}+\sum_{p=1}^{q}FC^{1}\circ\exp\circ m_{\alpha_{p}} |  |

each of the α p \alpha_{p} different and dependent on Δ \Delta (obviously q q also depends on Δ \Delta).

###### Remark 4.10.

This is the full importance of A ​ D ​ T 1 ADT_{1} in [11, p 73] in this context.

Note that by our earlier remark that for α ≠ 1 \alpha\neq 1 a function of size e − λ ​ exp α ​ ζ e^{-\lambda\exp^{\alpha\zeta}}, is of essentially different size than e − μ ​ exp μ ​ ζ e^{-\mu\exp^{\mu\zeta}}, the elements in different F C 1 ∘ exp ∘ m α p FC^{1}\circ\exp\circ m_{\alpha_{p}} can not have any overlap. So this gives us a leading term for Δ − id \Delta-\id or Δ ≡ id \Delta\equiv\id.

The problem in [11] lies in its proof of property 3 3, more specifically 2 ​ b 2b significantly complicates the asymptotics of F ​ C 1 FC^{1} and the proof that these asymptotics are ordered is problematic.

## 5 Sketch of definition of F ​ C 1 FC^{1} and ordering of asympotics

In [11, §1.7], F ​ C 1 FC^{1} is defined as the union of F ​ C 1, p FC^{1,p} which are defined by inductive process as follows (again some simplification are made appropriately for the context):

First define the set of exponents E 1 E^{1} to be the set of all functions 𝐞 \mathbf{e} which on some ℂ a + \mathbb{C}^{+}_{a} admits asymptotics of the form:

 | 𝐞 ⁡ ( ζ) = ν ⁡ ( 𝐞) ⋅ e ζ + ∑ q ≥ 0 b q ​ e ( 1 − c q) ​ ζ \mathbf{e}(\zeta)=\nu(\mathbf{e})\cdot e^{\zeta}+\sum_{q\geq 0}b_{q}e^{(1-c_{q})\zeta} |  |

again, all c q > 0 c_{q}>0, strictly increasing, going to + ∞ +\infty. We call ν ⁡ ( 𝐞) ∈ ℝ \nu(\mathbf{e})\in\mathbb{R} the principal exponent of 𝐞 \mathbf{e}.

We define K 1, 0 K_{1,0} to be sums of F ​ C 0 FC^{0} multiplied by some exponential e λ ​ ζ e^{\lambda\zeta}, λ > 0 \lambda>0 (i.e. the F ​ C 0 FC^{0} in the notation of [11] as explained in Remark 4.6).

We proceed by induction, suppose K 1, p K_{1,p} defined, then we define F ​ C 1, p FC^{1,p} to be the set of all analytic functions ψ \psi with ψ ∘ exp \psi\circ\exp admitting double exponentially accurate asymptotics on some ln ⁡ ( ℂ a +) \ln(\mathbb{C}^{+}_{a}) of the form:

 | ∑ q ≥ 0 k q ​ e 𝐞 q \sum_{q\geq 0}k_{q}e^{\mathbf{e}_{q}} |  |

with k q ∈ K 1, p k_{q}\in K_{1,p} and 𝐞 q ∈ E 1 \mathbf{e}_{q}\in E^{1}. I.e. for a given λ > 0 \lambda>0 any initial segment after a given point approximates the element in F ​ C 1, p FC^{1,p} closer than e − λ ​ Re ⁡ ( e ζ) e^{-\lambda\re(e^{\zeta})} on the real axis. We also demand that:

 | lim q → ∞ ν ⁡ ( 𝐞 q) = − ∞. \lim_{q\to\infty}\nu(\mathbf{e}_{q})=-\infty. |  |

It is worth noting that multiple 𝐞 q \mathbf{e}_{q} can have the same principle exponent, we just assume them ordered in some (not necessarily strictly) descending order.

Then K 1, p + 1 K_{1,p+1} is a sum of the following form:

 | ϕ + ∑ q = 1 N ψ q ∘ exp ∘ m α q \phi+\sum_{q=1}^{N}\psi_{q}\circ\exp\circ m_{\alpha_{q}} |  |

with ϕ ∈ K 1, 0 \phi\in K_{1,0}, ψ q ∈ F ​ C 1, p \psi_{q}\in FC^{1,p}, each of the m α q m_{\alpha_{q}} multiplication with α q \alpha_{q} with 0 < α q < 1 0<\alpha_{q}<1. Then as said before F ​ C 1 FC^{1} is the union of all the F ​ C 1, p FC^{1,p}.

###### Remark 5.1.

An expression of the form:

 | ∑ q ≥ 0 k q ​ e 𝐞 q \sum_{q\geq 0}k_{q}e^{\mathbf{e}_{q}} |  |

is called a STAR \STAR -series. This notion is less well behaved than one might expect, in particular it is possible to have a nontrivial finite sum of the form above which is nontheless zero, indeed for example e − e ζ − 1 e^{-e^{\zeta}}-1 can be expanded into Taylor series to give an element of F ​ C 0 FC^{0}.

The focus is nonetheless on finite sums which are nonzero.

Let us unwrap the proof that a nonzero element ψ \psi of F ​ C 1 FC^{1} has an exponential lower bound as done in [11].

The first step is to use asymptotics to create a dichotomy: either ψ \psi is smaller than any exponential on the real axis, or it has the lower bound (this is the problematic part) and then we prove that if ψ \psi is smaller than any exponential on the real axis it is identically zero, see [11, pp 74–75], [11, Chapter III] is dedicated to the statement that if ψ \psi is smaller than any exponential, it is identically zero, but in this case it is the same Theorem as before.

The way to create this dichotomy is essentially found in [11, §4.10 G]. The point is to prove by induction on p p that any nonzero finite sum:

 | ∑ q = 1 N k q ​ e 𝐞 q \sum_{q=1}^{N}k_{q}e^{\mathbf{e}_{q}} |  |

has a (sharp) exponential lower bound of exactly the same type demanded with k q ∈ K 1, p k_{q}\in K_{1,p}. So if we have a series approximating an element of F C 1, p ∘ exp FC^{1,p}\circ\exp, either eventually this lower bound is higher than the accuracy by which it is supposed to approximate this element of F C 1, p ∘ exp FC^{1,p}\circ\exp, implying this lower bound for the element of F ​ C 1, p FC^{1,p} or the element of F ​ C 1, p FC^{1,p} is smaller than any exponential on the real axis, making it zero.

Here we proceed by induction on N N, i.e. the amount of terms in such a sum. The core of this is a divide and differentiate argument. The case N = 1 N=1 is easy because an element of K 1, p K_{1,p} is intrinsically smaller than an element of exp ⁡ ( E 1) \exp(E^{1}) (remembering that elements of F ​ C 1 FC^{1} are supposed to be exponentially small).

Then by ordering already proven one can assume that k 1 ​ e 𝐞 1 k_{1}e^{\mathbf{e}_{1}} is the largest and one can consider:

 | S ⁡ ( x) ≔ 1 + ∑ q = 2 N k q k 1 ​ e 𝐞 q − 𝐞 1. S(x)\coloneqq 1+\sum_{q=2}^{N}\frac{k_{q}}{k_{1}}e^{\mathbf{e}_{q}-\mathbf{e}_{1}}. |  |

Then assuming this has a limit as x x goes to infinity (this is the first problematic part) we can consider this limit which has to be ≤ 1 \leq 1 in absolute value, if it is nonzero we are done because this is roughly a nonzero constant times something already having the lower bound we want.

Suppose it does go to zero, then:

 | S ⁡ ( x) = ∫ x ∞ S ′ ​ ( y) ​ 𝑑 y. S(x)=\int_{x}^{\infty}S^{\prime}(y)dy. |  |

And S ′ ​ ( y) S^{\prime}(y) is the same kind of finite sum with N − 1 N-1 terms (this is also problematic), so a lower bound for S ′ ​ ( y) S^{\prime}(y) implies by some elementary integral estimates a lower bound for S S and thus one for the original sum we started with.

## 6 The problem and a counterexample

The problem here is that both of the passages where we say it is problematic make the following calculation:

 | d d ​ ζ ​ k q k 1 ​ e 𝐞 q − 𝐞 1 = k q ′ ​ k 1 − k 1 ′ ​ k q + k q ​ k 1 ​ ( 𝐞 q ′ − 𝐞 1 ′) k 1 2 ​ e 𝐞 q − 𝐞 1. \frac{d}{d\zeta}\frac{k_{q}}{k_{1}}e^{\mathbf{e}_{q}-\mathbf{e}_{1}}=\frac{k_{q}^{\prime}k_{1}-k_{1}^{\prime}k_{q}+k_{q}k_{1}(\mathbf{e}_{q}^{\prime}-\mathbf{e}_{1}^{\prime})}{k_{1}^{2}}e^{\mathbf{e}_{q}-\mathbf{e}_{1}}. |  |

And then claim that k q ′ ​ k 1 − k 1 ′ ​ k q + k q ​ k 1 ​ ( 𝐞 q ′ − 𝐞 1 ′) k_{q}^{\prime}k_{1}-k_{1}^{\prime}k_{q}+k_{q}k_{1}(\mathbf{e}_{q}^{\prime}-\mathbf{e}_{1}^{\prime}) is in K 1, p K_{1,p}, see [11, p198 last line], calculation slightly corrected (technically [11] also claims falsely in the same line that k 1 2 k_{1}^{2} is in K 1, p K_{1,p} but that part is not essential to the argument).

###### Remark 6.1.

To make this explicit, in [11, p198 last line] it talks about 𝒦 ℝ m, r \mathscr{K}^{m,r}_{\mathbb{R}}. We have:

 | K 1, p ⊂ 𝒦 ℝ 1, p K_{1,p}\subset\mathscr{K}^{1,p}_{\mathbb{R}} |  |

moreover the same arguments we will employ will indeed also work to show that in the counterexample we have:

 | k q ′ ​ k 1 − k 1 ′ ​ k q + k q ​ k 1 ​ ( 𝐞 q ′ − 𝐞 1 ′) ∉ 𝒦 ℝ 1, p k_{q}^{\prime}k_{1}-k_{1}^{\prime}k_{q}+k_{q}k_{1}(\mathbf{e}_{q}^{\prime}-\mathbf{e}_{1}^{\prime})\notin\mathscr{K}^{1,p}_{\mathbb{R}} |  |

This is true for p = 0 p=0. We will show that this can not be the case for p = 1 p=1 using maps coming from concrete polycycles in order to show that this difficulty is incircumventable in this approach. What we mean with this is the following: Our example will show that:

1. 1.

This F ​ C 1, p FC^{1,p} construction is inevitable, i.e. we will show that we naturally get an element of F ​ C 1, 1 FC^{1,1}.

2. 2.

For elements k 2, k 1 k_{2},k_{1} of K 1, 1 K_{1,1} coming from this example we will show that:

 | k 2 ′ ​ k 1 − k 1 ′ ​ k 2 ∉ K 1, 1, k_{2}^{\prime}k_{1}-k_{1}^{\prime}k_{2}\notin K_{1,1}, |  |

giving a counterexample to the claims made in proving the ordering of F ​ C 1 FC^{1} and thus the existence of leading terms, or the lower bound needed.

The crux of the entire thing is that you forcibly have that F C 1, p ∘ exp ⋅ F C 1, 0 ∘ exp ∘ m α ⊆ F C 1, p + 1 FC^{1,p}\circ\exp\cdot FC^{1,0}\circ\exp\circ m_{\alpha}\subseteq FC^{1,p+1} with α < 1 \alpha<1 because any approximation you try to give the element of F C 1, 0 ∘ exp ∘ m α FC^{1,0}\circ\exp\circ m_{\alpha} will be off by something larger than e − x e^{-x} so you have no choice but to use the entire element of F C 1, 0 ∘ exp ∘ m α FC^{1,0}\circ\exp\circ m_{\alpha} in your coefficients, raising the p p by one.

Let us get to the counterexample. We take a polycycle with 4 4 equilibria E 1, …, E 4 E_{1},...,E_{4} in order in forward time. Let us take the section Σ \Sigma around which to take a return map. Let Σ i, 1 \Sigma_{i,1} and Σ i, 2 \Sigma_{i,2} be two sections around E i E_{i} as in section 2 with a transit map going from Σ i, 1 \Sigma_{i,1} to Σ i, 2 \Sigma_{i,2}.

Figure 2: Counterexample notation

Let us prescribe all the transit maps by gluing. What this means is that for each equilibrium we have a concrete system on ℝ 2 \mathbb{R}^{2} with the equilibrium, say at the origin, with the correct transit map. Then it is possible to use flow box theorem to glue both the manifolds and the vector field at the same time and we can use a biholomorphism in the direction perpendicular to the orbits of the flow box to prescribe the transit maps between different equilibria:

1. 1.

Σ → Σ 1, 1: id. \Sigma\to\Sigma_{1,1}:\id.

2. 2.

Σ 1, 1 → Σ 1, 2: z ↦ e − 1 z 2. \Sigma_{1,1}\to\Sigma_{1,2}:z\mapsto e^{-\frac{1}{z^{2}}}.

3. 3.

Σ 1, 2 → Σ 2, 1: z ↦ z + z 2. \Sigma_{1,2}\to\Sigma_{2,1}:z\mapsto z+z^{2}.

4. 4.

Σ 2, 1 → Σ 2, 2: z ↦ ( 1 − ln ⁡ ( z)) 1 2. \Sigma_{2,1}\to\Sigma_{2,2}:z\mapsto\left(\frac{1}{-\ln(z)}\right)^{\frac{1}{2}}.

5. 5.

Σ 2, 2 → Σ 3, 1: id \Sigma_{2,2}\to\Sigma_{3,1}:\id.

6. 6.

Σ 3, 1 → Σ 3, 2: z ↦ e − 1 z \Sigma_{3,1}\to\Sigma_{3,2}:z\mapsto e^{-\frac{1}{z}}.

7. 7.

Σ 3, 2 → Σ 4, 1: z ↦ z + z 2 \Sigma_{3,2}\to\Sigma_{4,1}:z\mapsto z+z^{2}.

8. 8.

Σ 4, 1 → Σ 4, 2: z ↦ 1 − ln ⁡ ( z) \Sigma_{4,1}\to\Sigma_{4,2}:z\mapsto\frac{1}{-\ln(z)}.

9. 9.

Σ 4, 2 → Σ: id \Sigma_{4,2}\to\Sigma:\id.

Let us try to convert these maps into the logarithmic chart. Let us first consider the map f ⁡ ( z) = z + z 2 f(z)=z+z^{2}:

 | f log ​ ( ζ) = ζ − ln ⁡ ( 1 + e − ζ) = ζ − ∑ q > 0 ( − 1) q ​ e − q ​ ζ q f^{\log}(\zeta)=\zeta-\ln(1+e^{-\zeta})=\zeta-\sum_{q>0}(-1)^{q}\frac{e^{-q\zeta}}{q} |  |

 | A ⁡ ( f log) ​ ( ζ) = ζ − ln ⁡ ( 1 − ∑ q > 0 ( − 1) q ​ e − ζ ​ e − q ​ e ζ q) = ζ + ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − ζ ​ e − q ​ e ζ q) r r A(f^{\log})(\zeta)=\zeta-\ln\left(1-\sum_{q>0}(-1)^{q}e^{-\zeta}\frac{e^{-qe^{\zeta}}}{q}\right)=\zeta+\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-\zeta}\frac{e^{-qe^{\zeta}}}{q}\right)^{r}}{r} |  |

 | ( m 2 − 1 ∘ A ⁡ ( f log) ∘ m 2) ​ ( ζ) = ζ + 1 2 ​ ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − 2 ​ ζ ​ e − q ​ e 2 ​ ζ q) r r. (m_{2}^{-1}\circ A(f^{\log})\circ m_{2})(\zeta)=\zeta+\frac{1}{2}\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-2\zeta}\frac{e^{-qe^{2\zeta}}}{q}\right)^{r}}{r}. |  |

The return map is then:

 | A ⁡ ( f log) ∘ ( m 2 − 1 ∘ A ⁡ ( f log) ∘ m 2). A(f^{\log})\circ(m_{2}^{-1}\circ A(f^{\log})\circ m_{2}). |  |

Note that this could only be identity if A ⁡ ( f log) ∘ m 2 = m 2 ∘ A ​ ( f log) − 1 A(f^{\log})\circ m_{2}=m_{2}\circ A(f^{\log})^{-1} which is clearly not the case, they are of size 2 ​ ζ + e − λ ​ e 2 ​ ζ 2\zeta+e^{-\lambda e^{2\zeta}} and 2 ​ ζ + e − μ ​ e ζ 2\zeta+e^{-\mu e^{\zeta}} respectively for some λ, μ > 0 \lambda,\mu>0. We now promised that this example would illustrate two things, so let us prove this.

Part 1: the F ​ C 1, p FC^{1,p} construction is necessary

The explicit form of the return map means that by property 2 ​ b 2b of F ​ C 1 FC^{1}:

 | ( ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − ζ ​ e − q ​ e ζ q) r r) ∘ ( ζ + 1 2 ​ ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − 2 ​ ζ ​ e − q ​ e 2 ​ ζ q) r r) − − ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − ζ ​ e − q ​ e ζ q) r r ∈ F C 1 ∘ exp ∘ m 2. \left(\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-\zeta}\frac{e^{-qe^{\zeta}}}{q}\right)^{r}}{r}\right)\circ\left(\zeta+\frac{1}{2}\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-2\zeta}\frac{e^{-qe^{2\zeta}}}{q}\right)^{r}}{r}\right)-\\ -\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-\zeta}\frac{e^{-qe^{\zeta}}}{q}\right)^{r}}{r}\in FC^{1}\circ\exp\circ m_{2}. |  |

It is easy to calculate this out using Taylor expansion:

 | ∑ s ≥ 1 1 s! ​ d s ​ ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − ζ ​ e − q ​ e ζ q) r r d ​ ζ s ​ ( 1 2 ​ ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − 2 ​ ζ ​ e − q ​ e 2 ​ ζ q) r r) s \sum_{s\geq 1}\frac{1}{s!}\frac{d^{s}\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-\zeta}\frac{e^{-qe^{\zeta}}}{q}\right)^{r}}{r}}{d\zeta^{s}}\left(\frac{1}{2}\sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-2\zeta}\frac{e^{-qe^{2\zeta}}}{q}\right)^{r}}{r}\right)^{s} |  |

has to be in F C 1 ∘ exp ∘ m 2 FC^{1}\circ\exp\circ m_{2}. Now the important part here is that the first factor, the entire thing being derived, has asymptotics of accuracy e − λ ​ e ζ e^{-\lambda e^{\zeta}} while the definition of asymptotics for F ​ C 1, p FC^{1,p} needs accuracy up to e − λ ​ e 2 ​ ζ e^{-\lambda e^{2\zeta}} so we have no choice but to take the entire thing as a coefficient. Put differently, what we have here is an element of F C 1, 1 ∘ exp ∘ m 2 FC^{1,1}\circ\exp\circ m_{2}. So F ​ C 1, 0 FC^{1,0} definitely does not cover everything. So in the approach of [11] it is actually necessary that for k 1, k 2 ∈ K 1, 1 k_{1},k_{2}\in K_{1,1}:

 | k 2 ′ ​ k 1 − k 1 ′ ​ k 2 ∈ K 1, 1 k_{2}^{\prime}k_{1}-k_{1}^{\prime}k_{2}\in K_{1,1} |  | (1) |

(here we have taken the previous exponents equal to each other).

Part 2: the argument for ordering does not work: theoretical example

So we want to prove that Equation 1 does not hold in a case relevant to proving finiteness of limit cycles. We will get to a case actually related to polycycles later.

Let us first illustrate the problem in a much simpler context removed from the problem of Dulac. Let:

 | k 1 ( ζ) = e − e 1 3 ​ ζ 1 − e − e 1 3 ​ ζ ∈ F C 1, 0 ∘ exp ∘ m 1 3 ⊆ K 1, 1, k_{1}(\zeta)=\frac{e^{-e^{\frac{1}{3}\zeta}}}{1-e^{-e^{\frac{1}{3}\zeta}}}\in FC^{1,0}\circ\exp\circ m_{\frac{1}{3}}\subseteq K_{1,1}, |  |

 | k 2 ( ζ) = e − e 1 2 ​ ζ ∈ F C 1, 0 ∘ exp ∘ m 1 2 ⊆ K 1, 1. k_{2}(\zeta)=e^{-e^{\frac{1}{2}\zeta}}\in FC^{1,0}\circ\exp\circ m_{\frac{1}{2}}\subseteq K_{1,1}. |  |

In fact for these it also holds that k 2 ′ ​ k 1 − k 1 ′ ​ k 2 ∉ K 1, 1 k_{2}^{\prime}k_{1}-k_{1}^{\prime}k_{2}\notin K_{1,1} by the same issue we will talk about now but let us prove that k 1 ​ k 2 ∉ K 1, 1 k_{1}k_{2}\notin K_{1,1} to keep calculation to a minimum. It is worth noting that Equation 1 would be very extraordinary if K 1, 1 K_{1,1} were not at least a differential algebra, so in some sense it is also expected that k 1 ​ k 2 ∈ K 1, 1 k_{1}k_{2}\in K_{1,1}:

 | k 1 ​ ( ζ) ​ k 2 ​ ( ζ) = e − e 1 3 ​ ζ 1 − e − e 1 3 ​ ζ ​ e − e 1 2 ​ ζ. k_{1}(\zeta)k_{2}(\zeta)=\frac{e^{-e^{\frac{1}{3}\zeta}}}{1-e^{-e^{\frac{1}{3}\zeta}}}e^{-e^{\frac{1}{2}\zeta}}. |  |

Suppose by contradiction it were in K 1, 1 K_{1,1}, thus it could be written as:

 | ϕ + ∑ q = 1 N ψ q ∘ exp ∘ m α q \phi+\sum_{q=1}^{N}\psi_{q}\circ\exp\circ m_{\alpha_{q}} |  |

with ϕ ∈ K 1, 0 \phi\in K_{1,0}, ψ q ∈ F ​ C 1, p \psi_{q}\in FC^{1,p}, each of the m α q m_{\alpha_{q}} multiplication with α q \alpha_{q} with 0 < α q < 1 0<\alpha_{q}<1. Then clearly because k 1 ​ k 2 k_{1}k_{2} has both an upper and lower bound of the form e − λ ​ e 1 2 ​ ζ e^{-\lambda e^{\frac{1}{2}\zeta}} we would have to have that this is a sum of F C 1, 0 ∘ exp ∘ m α q FC^{1,0}\circ\exp\circ m_{\alpha_{q}} with α q ≤ 1 2 \alpha_{q}\leq\frac{1}{2}.

So by construction of K 1, 0 K_{1,0} there has to be some element of F C 1, 0 ∘ exp ∘ m 1 2 FC^{1,0}\circ\exp\circ m_{\frac{1}{2}} which approximates k 1 ​ k 2 k_{1}k_{2} with accuracy e − λ ​ e 1 2 ​ ζ e^{-\lambda e^{\frac{1}{2}\zeta}} for all λ \lambda. Now an element of F C 1, 0 ∘ exp FC^{1,0}\circ\exp looks like:

 | ∑ q = 1 N h q ​ e 𝐞 q. \sum_{q=1}^{N}h_{q}e^{\mathbf{e}_{q}}. |  |

With h q h_{q} having some exponential lower and upper bound, in particular we have:

 | k 1 ​ ( ζ) ​ k 2 ​ ( ζ) = e − e 1 3 ​ ζ 1 − e − e 1 3 ​ ζ ​ e − e 1 2 ​ ζ = ( ∑ q ≥ 1 e − q ​ e 1 3 ​ ζ) ​ e − e 1 2 ​ ζ = ∑ q ≥ 1 e − q ​ e 1 3 ​ ζ − e 1 2 ​ ζ. k_{1}(\zeta)k_{2}(\zeta)=\frac{e^{-e^{\frac{1}{3}\zeta}}}{1-e^{-e^{\frac{1}{3}\zeta}}}e^{-e^{\frac{1}{2}\zeta}}=\left(\sum_{q\geq 1}e^{-qe^{\frac{1}{3}\zeta}}\right)e^{-e^{\frac{1}{2}\zeta}}=\sum_{q\geq 1}e^{-qe^{\frac{1}{3}\zeta}-e^{\frac{1}{2}\zeta}}. |  |

So a finite sum of h q ​ e 𝐞 q h_{q}e^{\mathbf{e}_{q}} has to approximate:

 | ∑ q ≥ 1 e − q ​ e 2 3 ​ ζ − e ζ \sum_{q\geq 1}e^{-qe^{\frac{2}{3}\zeta}-e^{\zeta}} |  |

up to accuracy e − 2 ​ e ζ e^{-2e^{\zeta}}.

Diversion: Some normal forms

Let us introduce some normal forms for h ​ e 𝐞 he^{\mathbf{e}}, h ∈ K 1, 0 h\in K_{1,0}, 𝐞 ∈ E 1 \mathbf{e}\in E^{1} in order to definitively show that this is impossible. Remember that:

 | 𝐞 ⁡ ( ζ) = ν ⁡ ( 𝐞) ⋅ e ζ + ∑ q ≥ 0 b q ​ e ( 1 − c q) ​ ζ. \mathbf{e}(\zeta)=\nu(\mathbf{e})\cdot e^{\zeta}+\sum_{q\geq 0}b_{q}e^{(1-c_{q})\zeta}. |  |

So it is possible to split up a 𝐞 ∈ E 1 \mathbf{e}\in E^{1} as 𝐞 large + 𝐞 small \mathbf{e}_{\Larget}+\mathbf{e}_{\Small} where 𝐞 small \mathbf{e}_{\Small} contains all terms with c q ≥ 1 c_{q}\geq 1 and the important remark here is that by Taylor series:

 | e 𝐞 small ∈ K 1, 0. e^{\mathbf{e}_{\Small}}\in K_{1,0}. |  |

So let E large 1 E^{1}_{\Larget} be the subset of all E 1 E^{1} where the c q c_{q} are all < 1 <1 then any finite sum of h ​ e 𝐞 he^{\mathbf{e}}, h ∈ K 1, 0 h\in K_{1,0}, 𝐞 ∈ E 1 \mathbf{e}\in E^{1} can be rewritten into a finite sum with 𝐞 ∈ E large 1 \mathbf{e}\in E^{1}_{\Larget}. The important thing is the following, because of the exponential lower and upper bound of K 1, 0 K_{1,0}, if we have h 1, h 2 ∈ K 1, 0 h_{1},h_{2}\in K_{1,0} and 𝐞 1 < 𝐞 2 ∈ E large 1 \mathbf{e}_{1}<\mathbf{e}_{2}\in E^{1}_{\Larget} then as we go to + ∞ +\infty on the real axis:

 | h 1 ​ e 𝐞 1 h 2 ​ e 𝐞 2 → 0, \frac{h_{1}e^{\mathbf{e}_{1}}}{h_{2}e^{\mathbf{e}_{2}}}\to 0, |  |

because it behaves like some e λ ​ x ​ e − μ ​ e α ​ ζ e^{\lambda x}e^{-\mu e^{\alpha\zeta}} with 0 < α < 1 0<\alpha<1 and of course the double exponential will win out.

So we have rewritten this to a form with proper leading terms.

Back to part 2: the theoretical example

From the normal forms it is clear that the only STAR-series one could choose to approximate k 1 ​ k 2 k_{1}k_{2} with coefficients in K 1, 0 K_{1,0} is just:

 | ∑ q ≥ 1 e − q ​ e 2 3 ​ ζ − e ζ. \sum_{q\geq 1}e^{-qe^{\frac{2}{3}\zeta}-e^{\zeta}}. |  |

But here the generalized exponent of − q ​ e 2 3 ​ ζ − e ζ ∈ E large 1 -qe^{\frac{2}{3}\zeta}-e^{\zeta}\in E^{1}_{\Larget} does not go to − ∞ -\infty, in fact it stays 1 1, thus it is not valid as a series expansion, thus k 1 ​ k 2 ∉ K 1, 0 k_{1}k_{2}\notin K_{1,0}.

Part 3: the argument for ordering does not work: practical example

Let us now go back to the example in Part 1 and prove that we can find some k 1, k 2 k_{1},k_{2} relevant to the example such that Equation 1 does not hold.

Let k 1 ∈ F C 1, 0 ∘ exp ∘ m 1 2 ⊆ K 1, 1 k_{1}\in FC^{1,0}\circ\exp\circ m_{\frac{1}{2}}\subseteq K_{1,1} be:

 | ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − 1 2 ​ ζ ​ e − q ​ e 1 2 ​ ζ q) r r \sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-\frac{1}{2}\zeta}\frac{e^{-qe^{\frac{1}{2}\zeta}}}{q}\right)^{r}}{r} |  |

so ( A ⁡ ( f log) − id) ∘ m 1 2 \left(A(f^{\log})-\id\right)\circ m_{\frac{1}{2}}.

Let k 2 ∈ F C 1, 0 ∘ exp ∘ m 1 3 ⊆ K 1, 1 k_{2}\in FC^{1,0}\circ\exp\circ m_{\frac{1}{3}}\subseteq K_{1,1} be:

 | ∑ r > 0 ( ∑ q > 0 ( − 1) q ​ e − 1 3 ​ ζ ​ e − q ​ e 1 3 ​ ζ q) r r \sum_{r>0}\frac{\left(\sum_{q>0}(-1)^{q}e^{-\frac{1}{3}\zeta}\frac{e^{-qe^{\frac{1}{3}\zeta}}}{q}\right)^{r}}{r} |  |

so ( A ⁡ ( f log) − id) ∘ m 1 3 \left(A(f^{\log})-\id\right)\circ m_{\frac{1}{3}}. Then k 1 ′ k_{1}^{\prime} is equal to:

 | ( ∑ q > 0 − 1 2 ( − 1) q e − 1 2 ​ ζ e − q ​ e 1 2 ​ ζ q − 1 2 ( − 1) q e − q ​ e 1 2 ​ ζ) ∑ r > 0 ( ∑ q > 0 ( − 1) q e − 1 2 ​ ζ e − q ​ e 1 2 ​ ζ q) r − 1 \left(\sum_{q>0}-\frac{1}{2}(-1)^{q}e^{-\frac{1}{2}\zeta}\frac{e^{-qe^{\frac{1}{2}\zeta}}}{q}-\frac{1}{2}(-1)^{q}e^{-qe^{\frac{1}{2}\zeta}}\right)\sum_{r>0}\left(\sum_{q>0}(-1)^{q}e^{-\frac{1}{2}\zeta}\frac{e^{-qe^{\frac{1}{2}\zeta}}}{q}\right)^{r-1} |  |

or

 | − 1 2 ( ∑ q > 0 ( − 1) q e − q ​ e 1 2 ​ ζ ( e − 1 2 ​ ζ q + 1)) ∑ r > 0 ( ∑ q > 0 ( − 1) q e − 1 2 ​ ζ e − q ​ e 1 2 ​ ζ q) r − 1. -\frac{1}{2}\left(\sum_{q>0}(-1)^{q}e^{-qe^{\frac{1}{2}\zeta}}\left(\frac{e^{-\frac{1}{2}\zeta}}{q}+1\right)\right)\sum_{r>0}\left(\sum_{q>0}(-1)^{q}e^{-\frac{1}{2}\zeta}\frac{e^{-qe^{\frac{1}{2}\zeta}}}{q}\right)^{r-1}. |  |

So k 2 ′ k_{2}^{\prime} is equal to:

 | − 1 3 ( ∑ q > 0 ( − 1) q e − q ​ e 1 3 ​ ζ ( e − 1 3 ​ ζ q + 1)) ∑ r > 0 ( ∑ q > 0 ( − 1) q e − 1 3 ​ ζ e − q ​ e 1 3 ​ ζ q) r − 1. -\frac{1}{3}\left(\sum_{q>0}(-1)^{q}e^{-qe^{\frac{1}{3}\zeta}}\left(\frac{e^{-\frac{1}{3}\zeta}}{q}+1\right)\right)\sum_{r>0}\left(\sum_{q>0}(-1)^{q}e^{-\frac{1}{3}\zeta}\frac{e^{-qe^{\frac{1}{3}\zeta}}}{q}\right)^{r-1}. |  |

It is then clear that if k 2 ′ ​ k 1 − k 1 ′ ​ k 2 ∈ K 1, 1 k_{2}^{\prime}k_{1}-k_{1}^{\prime}k_{2}\in K_{1,1} by the rough size being e − λ ​ e 1 2 ​ ζ e^{-\lambda e^{\frac{1}{2}\zeta}} the only option is that k 2 ′ k 1 − k 1 ′ k 2 ∈ F C 1, 0 ∘ exp ∘ m 1 2 k_{2}^{\prime}k_{1}-k_{1}^{\prime}k_{2}\in FC^{1,0}\circ\exp\circ m_{\frac{1}{2}}, but clearly you again by these normal forms can not write this as such.

## 7 Statement 2.4

As promised we will talk about the case where every equilibrium is real analytically orbitally equivalent to:

 | { x ˙ = x 2 y ˙ = − y. \begin{cases}\dot{x}=x^{2}\\ \dot{y}=-y.\end{cases} |  |

In this case each of the transit maps is equal to e − 1 z e^{-\frac{1}{z}}. The crucial consequence is the following: we no longer just have that the Dulac maps in the logarithmic chart are contained in ⟨ 𝒜 ​ ff, ℋ, A ​ ℋ ⟩ \langle\Aff,\mathcal{H},A\mathcal{H}\rangle, we can also restrict to the case where every element in 𝒜 ​ ff \Aff has linear part 1 1, i.e. is of the form ζ ↦ ζ + β \zeta\mapsto\zeta+\beta, after all the only multiplications, i.e. the only α \alpha come from the map x ↦ x k x\mapsto x^{k} which is no longer present. This avoids all this frustration with m α, α ≠ 1 m_{\alpha},\alpha\neq 1, allowing us to stay within F ​ C 1, 0 FC^{1,0} and only use K 1, 0 K_{1,0}.

The normal forms above work here to show ordering and even give proper leading terms. In a future article we hope to use these types of normal forms in a more general context.

## 8 Bibliography

## References

- [1] M. Aschenbrenner, L. van den Dries, and J. van der Hoeven. Asymptotic Differential Algebra and Model Theory of Transseries. arXiv e-prints, page arXiv:1509.02588, September 2015.
- [2] O. Costin and G. V. Dunne. Resurgent extrapolation: rebuilding a function from asymptotic data. painlevé i. Journal of Physics A: Mathematical and Theoretical, 52(44):445205, oct 2019.
- [3] H. Dulac. Sur les cycles limites. Bulletin de la Société Mathématique de France, 51:45–188, 1923.
- [4] F. Dumortier. Singularities of vector fields on the plane. Journal of Differential Equations, 23(1):53–106, 1977.
- [5] J. Ecalle. Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac. Actualités mathématiques. Hermann, 1992.
- [6] Z. Galal, T. Kaiser, and P. Speissegger. Ilyashenko algebras based on transserial asymptotic expansions. Advances in Mathematics, 367:107095, 2020.
- [7] Yu. Il’yashenko. Centennial history of hilbert’s 16th problem. Bulletin of the American Mathematical Society, 39:301–354, 2002.
- [8] Yu. S. Ilyashenko. Finiteness theorems for limit cycles, lecture notes, in preparation.
- [9] Yu S Il'yashenko. Dulac's memoir “on limit cycles” and related problems of the local theory of differential equations. Russian Mathematical Surveys, 40(6):1–49, dec 1985.
- [10] Yu. S. Il’yashenko. Separatrix lunes of analytic vector fields of the plane. Mosc. Univ. Math. Bull., 41(4):28–35, 1986.
- [11] Yu. S. Ilyashenko. Finiteness theorems for limit cycles, volume 94 of Translations of Mathematical Monographs. American Math. Society, 1991.
- [12] T. Kaiser, J.-P. Rolin, and P. Speissegger. Transition maps at non-resonant hyperbolic singularities are o-minimal. 2009(636):1–45, 2009.
- [13] J. Martinet and J. Ramis. Problèmes de modules pour des équations différentielles non linéaires du premier ordre. Publications Mathématiques de l’IHÉS, 55:63–164, 1982.
- [14] D. Sauzin. Mould expansions for the saddle-node and resurgence monomials. arXiv e-prints, page arXiv:0712.2337, December 2007.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
