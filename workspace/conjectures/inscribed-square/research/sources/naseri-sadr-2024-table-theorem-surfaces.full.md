<!-- source: https://ar5iv.labs.arxiv.org/html/2412.01977 | converted from HTML -->

[2412.01977] A Table Theorem for Surfaces with Odd Euler Characteristic

# A Table Theorem for Surfaces with Odd Euler Characteristic

Ali Naseri Sadr

###### Abstract

We use the square peg problem for smooth curves to prove a generalized table Theorem for real valued functions on Riemannian surfaces with odd Euler characteristic. We then use this result to prove the table conjecture for even functions on the two sphere.

## 1 Introduction

In 1951 1951, Freeman Dyson proved a remarkable result: for every continuous real-valued function on the unit sphere in ℝ 3 \mathbb{R}^{3}, it is possible to find the vertices of a square on a great circle (diameter d = 2 d=2) at which the function takes the same value; see [2] for more details. Dyson conjectures in the paper that the same result holds for some circle with diameter d d, for every 0 < d ≤ 2 0<d\leq 2. This conjecture reappears as The Table Problem in [6, conjecture 16 16]. Roger Fenn proved an analogous result for positive functions defined on a convex disk in the plane; see [3] for more details.

The table problem admits the following natural generalization. Define a square with diameter d > 0 d>0 on a Riemannian surface ( Σ, g) (\Sigma,g) to be the image, under the exponential map exp g: T ​ Σ → Σ \exp_{g}\colon T\Sigma\to\Sigma, of the vertices of a square of diameter d d (with respect to g g) centered at the origin in some tangent plane. A table for a continuous function f f is a square such that f f takes the same value at the four vertices of this square. We establish the following results:

###### Theorem 1.1 ( Table Theorem for Surfaces with Odd Euler Characteristic).

Let ( Σ, g) (\Sigma,g) be a Riemannian surface with χ ⁡ ( Σ) \chi(\Sigma) odd and f f a continuous real valued function on it. Then for every d > 0 d>0, f f admits a table with diameter d d.

As an immediate corollary of this Theorem, we will get the result for even functions on S 2 S^{2} and any Riemannian metric that is invariant under the antipodal map. In particular, this resolves the table problem for even functions.

###### Corollary 1.2.

Let g g be a Riemannian metric on S 2 S^{2} so that the antipodal map is an isometry of this metric and f f an even function on S 2 S^{2}. Then for every positive d d, f f admits a table with diameter d d.

The proof of Theorem 1.1 is based on the following topological idea. By compactness, it suffices to prove the Theorem for positive C 2 C^{2} functions. Now for a fixed diameter d d and a positive C 2 C^{2} function f f, we deform all the circles with diameter d d in T ​ Σ T\Sigma by mapping each vector ( x, v) (x,v) in T ​ Σ T\Sigma to ( x, f ⁡ ( e ​ x ​ p ​ ( x, v)) ⋅ v) (x,f(exp(x,v))\cdot v). The result is a subbundle of T ​ Σ T\Sigma where each fiber is a star-shaped C 2 C^{2} Jordan curve. Let C C be the subspace of T ​ Σ T\Sigma consisting of the center points of the inscribed squares in these curves. Every table for f f with diameter d d is in a one-to-one correspondence with the intersection points of C C and the zero section of T ​ Σ T\Sigma. Within C C is the subspace C 0 C_{0} of center points of gracefully inscribed squares: these are the squares whose vertices appear in the same cyclic order around the square and the curve; see [10] for more details. We use Sard-Smale Theorem for Fredholm maps to prove for a generic choice of f, f, the subspace C 0 C_{0} gives us a ℤ 2 \mathbb{Z}_{2} -cycle representing the non-zero element in H 2 ​ ( T ​ Σ, ℤ 2) H_{2}(T\Sigma;\mathbb{Z}_{2}) since every generic C 2 C^{2} star-shaped curve inscribes an odd number of graceful squares; this is proved for generic PL curves in [10]. Hence, C 0 C_{0} intersects the zero section in at least one point when χ ⁡ ( Σ) \chi(\Sigma) is odd, which yields Theorem 1.1 by a convergence argument.

In section 2 2, we show how our definition of tables for a function on a surface is a generalization of the corresponding one on the two sphere and propose a table problem for Riemannian surfaces. We define the mappings and spaces we need for our proof in section 3 3. In section 4 4, we establish the technical aspects of our proof, while a formal proof for Theorem 1.1 and corollary 1.2 is given in section 5 5. Related transversality arguments appear in [12, 5, 1]. Finally, we reprove the square-peg problem for C 2 C^{2} star-shaped Jordan curves by similar transversality arguments to sections 3 3 and 4 4 in the appendix.

## Acknowledgments

The author is grateful to his advisors, John Baldwin and Josh Greene, for their invaluable guidance, support, and insightful conversations about this work. He would also like to express his gratitude to Peter Feller and Joaquin Lema for inspiring conversations about this work.

## 2 Tables on Riemannian Surfaces

In the following, we will view S 2 S^{2} as the set of points with distance 1 1 from the origin in ℝ 3 \mathbb{R}^{3} and consider the induced Riemannian metric on it.

###### Definition.

For a continuous real-valued function f f on the round two sphere, we say p 1, p 2, p 3, p 4 p_{1},p_{2},p_{3},p_{4} on S 2 S^{2} are the basis of a table for f f if they are four vertices of a square in ℝ 3 \mathbb{R}^{3} and we have

 | f ⁡ ( p 1) = f ⁡ ( p 2) = f ⁡ ( p 3) = f ⁡ ( p 4). f(p_{1})=f(p_{2})=f(p_{3})=f(p_{4}). |  |

For every four vertices of a square p 1, p 2, p 3, p 4 p_{1},p_{2},p_{3},p_{4} on the two sphere, we can find a point x x and vectors v v and w w in T x ​ S 2 T_{x}S^{2} such that

 |  | exp x ⁡ ( v) = p 1, exp x ⁡ ( w) = p 2, \displaystyle\exp_{x}(v)=p_{1},\hskip 2.84526pt\exp_{x}(w)=p_{2}, |  |

 |  | exp x ⁡ ( − v) = p 3, exp x ⁡ ( − w) = p 4, \displaystyle\exp_{x}(-v)=p_{3},\hskip 2.84526pt\exp_{x}(-w)=p_{4}, |  |

 |  | v ⋅ w = 0, ‖ v ‖ = ‖ w ‖. \displaystyle v\cdot w=0,\hskip 2.84526pt\|v\|=\|w\|. |  |

Note that x x lies on the line that goes through the origin and the center of square in ℝ 3 \mathbb{R}^{3}. In particular, there are two points on the two sphere that satisfy the previous equations, but if we also require that ‖ w ‖ = ‖ v ‖ ≤ π 2 \|w\|=\|v\|\leq\frac{\pi}{2}, then x x becomes unique unless the square lies on a great circle. This gives us a way to parameterize all the squares with a fixed side length as pairs of ( x, v) (x,v) in T ​ S 2 TS^{2} where v v has a fixed length. We can also use this observation to define tables for arbitrary closed Riemannian surfaces.

###### Definition.

Let ( Σ, g) (\Sigma,g) be a Riemannian surface and f f a continuous real valued function on Σ \Sigma. We say ( x, v) (x,v) in T ​ Σ T\Sigma is basis of a table for f f if

 | f ⁡ ( exp ⁡ ( x, v)) = f ⁡ ( exp ⁡ ( x, w)) = f ⁡ ( exp ⁡ ( x, − v)) = f ⁡ ( exp ⁡ ( x, − w)), f(\exp(x,v))=f(\exp(x,w))=f(\exp(x,-v))=f(\exp(x,-w)), |  | (1) |

where w w is a vector perpendicular to v v and has the same length as v v.

###### Remark.

There are two choices for w w in the previous definition, but our definition is independent of this choice.

The following is a reformulation of the table problem for S 2 S^{2}.

###### Conjecture 2.1 ( The Table Problem for S 2 S^{2}).

Fix a positive real number a a. A continuous function on the two sphere endowed with the round metric admits a table with ‖ v ‖ = a \|v\|=a.

Using the generalization given in equation ( 1), one can ask a similar question for other Riemannian surfaces. In particular, we have the following problem.

###### Problem 2.1.

Let ( Σ, g) (\Sigma,g) be a closed Riemannian surface and fix a positive real number a a. Does every continuous function on Σ \Sigma admit a table defined by equation ( 1) and ‖ v ‖ = a \|v\|=a?

We note that our main Theorem answers this problem in affirmative for surfaces with odd Euler characteristic.

###### Remark.

Since we work with compact surfaces and solving problem 2.1 for a function f f is the same as solving it for f + c f+c where c c is a constant real number, we only need to solve the problem for positive functions. The other important point is that in contrast to peg problems for Jordan curves in the plane, this problem can be proved using a convergence argument because we fix the diameter of our table beforehand. Therefore, if one wants to prove problem 2.1 for a surface Σ \Sigma, it suffices to prove it for a dense subset of positive functions on Σ \Sigma.

## 3 A Submersion

In this section, we will assume that ( Σ, g) (\Sigma,g) is a fixed Riemannian surface. Consider a positive real number a a and let

 | U a ​ ( Σ) ≔ { ( x, v) ∈ T ​ Σ: ‖ v ‖ = a }. U_{a}(\Sigma)\coloneqq\{(x,v)\in T\Sigma:\|v\|=a\}. |  |

We are going to work with the fourth symmetric product of each fiber in U a ​ ( Σ) U_{a}(\Sigma); this space is a manifold itself, but we prefer to work with an open submanifold of it; see [9] for more details.

Let X X be a topological space and consider s ​ y ​ m 4 ​ ( X) sym^{4}(X); we define the fat diagonal Δ \Delta to be the subset of points in s ​ y ​ m 4 ​ ( X) sym^{4}(X) for which at least two of the coordinates are equal. We define K a ​ ( Σ) K_{a}(\Sigma) to be a fiber bundle over Σ \Sigma where each fiber over a point x x is the fourth symmetric product of the circle with radius a a in T x ​ Σ T_{x}\Sigma minus its fat diagonal. Note that the fibers are open non-orientable four manifolds. By abuse of notation, we let s ​ y ​ m 4 ​ ( T ​ Σ) sym^{4}(T\Sigma) denote the fiber bundle where each fiber over a point x x is s ​ y ​ m 4 ​ ( T x ​ Σ) sym^{4}(T_{x}\Sigma); we cut out the fat diagonal from each fiber and denote the resulting fiber bundle by Q ⁡ ( Σ) Q(\Sigma). The fibers of Q ⁡ ( Σ) Q(\Sigma) are open orientable eight dimensional manifolds and K a ​ ( Σ) K_{a}(\Sigma) is a subbundle of Q ⁡ ( Σ) Q(\Sigma).

Let C 2 ​ ( U a ​ ( Σ)) C^{2}(U_{a}(\Sigma)) denote the space of C 2 C^{2} functions on U a ​ ( Σ) U_{a}(\Sigma). This function space can be endowed with a norm that makes it a Banach space; see [8] for more details. We will work with the open subset of positive functions in C 2 ​ ( U a ​ ( Σ)) C^{2}(U_{a}(\Sigma)) and denote it by C + 2 ​ ( U a ​ ( Σ)) C^{2}_{+}(U_{a}(\Sigma)).

###### Definition.

Define a map Ψ: C + 2 ​ ( U a ​ ( Σ)) × K a ​ ( Σ) → Q ⁡ ( Σ) \Psi\colon C_{+}^{2}(U_{a}(\Sigma))\times K_{a}(\Sigma)\to Q(\Sigma) by

 | ( h, [θ 1, θ 2, θ 3, θ 4]) ↦ [h ⁡ ( θ 1) ⋅ θ 1, h ⁡ ( θ 2) ⋅ θ 2, h ⁡ ( θ 3) ⋅ θ 3, h ⁡ ( θ 4) ⋅ θ 4]. (h,[\theta_{1},\theta_{2},\theta_{3},\theta_{4}])\mapsto[h(\theta_{1})\cdot\theta_{1},h(\theta_{2})\cdot\theta_{2},h(\theta_{3})\cdot\theta_{3},h(\theta_{4})\cdot\theta_{4}]. |  | (2) |

This map is well defined and the image avoids the diagonal in s ​ y ​ m 4 ​ ( T ​ Σ) sym^{4}(T\Sigma) because we are working with positive functions. In particular, this is a smooth map from a Banach manifold to a finite dimensional manifold.

###### Remark.

Fix a positive function h h in C + 2 ​ ( U a ​ Σ) C^{2}_{+}(U_{a}\Sigma) and let Ψ h \Psi_{h} denote the restriction of Ψ \Psi to { h } × K a ​ ( Σ) ≅ K a ​ ( Σ) → Q ⁡ ( Σ) \{h\}\times K_{a}(\Sigma)\cong K_{a}(\Sigma)\to Q(\Sigma); this map covers the identity on Σ \Sigma and it is an embedding since we are only considering positive functions. Moreover, this map scales each fiber of K a ​ ( Σ) K_{a}(\Sigma) according to the function h h; thus the image of Ψ h \Psi_{h} in each fiber of Q ⁡ ( Σ) Q(\Sigma) over a point x x is the fourth symmetric product of a star-shaped curve in T x ​ Σ T_{x}\Sigma minus its fat diagonal.

###### Lemma 3.1.

The map Ψ \Psi is a submersion.

###### Proof.

Consider a pair ( h, θ) (h,\theta) in C + 2 ​ ( U a ​ ( Σ)) × K a ​ ( Σ) C_{+}^{2}(U_{a}(\Sigma))\times K_{a}(\Sigma) and let ξ \xi be its image under Ψ \Psi. Since Ψ h \Psi_{h} covers the identity map on Σ \Sigma, if ℋ θ \mathcal{H}_{\theta} is a horizontal subspace of T θ ​ K a ​ ( Σ) T_{\theta}K_{a}(\Sigma), then d ​ Ψ h ​ ( ℋ θ) d\Psi_{h}(\mathcal{H}_{\theta}) is also a horizontal subspace of T ξ ​ Q ​ ( Σ) T_{\xi}Q(\Sigma). Therefore, we only need to check that Ψ \Psi is a submersion when we restrict the map to a fiber over an arbitrary point x x. Let θ i \theta_{i} denote the components of θ \theta. Fix all the θ i ′ ​ s \theta_{i}^{\prime}s except θ 1 \theta_{1} and change θ 1 \theta_{1} along a curve δ ⁡ ( t) \delta(t) in U a ​ ( Σ) U_{a}(\Sigma) such that the curve γ ⁡ ( t) = [δ ⁡ ( t), θ 2, θ 3, θ 4] \gamma(t)=[\delta(t),\theta_{2},\theta_{3},\theta_{4}] avoids the diagonal in s ​ y ​ m 4 ​ ( T ​ Σ) sym^{4}(T\Sigma). We have

 | Ψ ⁡ ( h, γ ⁡ ( t)) = [h ⁡ ( δ ⁡ ( t)) ​ δ ​ ( t), h ⁡ ( θ 2) ​ θ 2, h ⁡ ( θ 3) ​ θ 3, h ⁡ ( θ 4) ​ θ 4]. \Psi(h,\gamma(t))=[h(\delta(t))\delta(t),h(\theta_{2})\theta_{2},h(\theta_{3})\theta_{3},h(\theta_{4})\theta_{4}]. |  |

Hence, we get

 | d ​ Ψ ​ ( 0, γ ˙ ​ ( 0)) = [h ⁡ ( θ 1) ⋅ δ ˙ ​ ( 0) + d ⁡ ( h ⁡ ( δ ⁡ ( t))) d ​ t | t = 0 ⋅ θ 1, 0, 0, 0] ∈ Im ​ ( d ​ Ψ), d\Psi(0,\dot{\gamma}(0))=[h(\theta_{1})\cdot\dot{\delta}(0)+\frac{d(h(\delta(t)))}{dt}\Big|_{t=0}\cdot\theta_{1},0,0,0]\in\text{Im}(d\Psi), |  |

where we used δ ⁡ ( 0) = θ 1 \delta(0)=\theta_{1}. Since δ ⁡ ( t) \delta(t) has constant length, δ ˙ ​ ( 0) \dot{\delta}(0) is a non-zero vector orthogonal to θ 1 \theta_{1}. Repeating this argument for the other coordinates proves we have vectors of the previous form in the image of d ​ Ψ d\Psi where all the components are zero except one and the non-zero component is of the form r i ⋅ ω i + s i ⋅ θ i r_{i}\cdot\omega_{i}+s_{i}\cdot\theta_{i} with r i = h ⁡ ( θ i) r_{i}=h(\theta_{i}) greater than zero, ω i \omega_{i} a vector orthogonal to θ i \theta_{i}, and s i s_{i} some arbitrary real number. Now fix the four-tuple θ \theta and pick a function g g such that g ⁡ ( θ 1) = 1 g(\theta_{1})=1 and g g vanishes on the other three coordinates. Let g t = h + t ​ g g_{t}=h+tg and note that for t t small enough all the functions g t g_{t} are positive. We get

 | d ​ Ψ ​ ( g, 0) = [g ⁡ ( θ 1) ⋅ θ 1, g ⁡ ( θ 2) ⋅ θ 2, g ⁡ ( θ 3) ⋅ θ 3, g ⁡ ( θ 4) ⋅ θ 4] = [θ 1, 0, 0, 0] ∈ Im ​ ( d ​ Ψ). d\Psi(g,0)=[g(\theta_{1})\cdot\theta_{1},g(\theta_{2})\cdot\theta_{2},g(\theta_{3})\cdot\theta_{3},g(\theta_{4})\cdot\theta_{4}]=[\theta_{1},0,0,0]\in\text{Im}(d\Psi). |  |

The same argument shows we have vectors of the form [0, …, θ i, …, 0] [0,\dots,\theta_{i},\dots,0] in the image of d ​ Ψ d\Psi. We conclude the lemma because the set of vectors

 |  | [0, …, θ i, …, 0], \displaystyle[0,\dots,\theta_{i},\dots,0], |  |

 |  | [0, …, ω i, …, 0] \displaystyle[0,\dots,\omega_{i},\dots,0] |  |

generate all the vertical vectors over x x in Q ⁡ ( Σ) Q(\Sigma). ∎

Let A ⁡ ( Σ) A(\Sigma) denote the subbundle of Q ⁡ ( Σ) Q(\Sigma) where over each point x x, A ⁡ ( Σ) | x A(\Sigma)\big|_{x} is the set of four tuples of vectors that are vertices of a square in T x ​ Σ T_{x}\Sigma with respect to the metric on Σ \Sigma. This subbundle has codimension four in Q ⁡ ( Σ) Q(\Sigma).

###### Corollary 3.2.

Let 𝒮 \mathcal{S} denote Ψ − 1 ​ ( A ​ ( Σ)) \Psi^{-1}(A(\Sigma)). Then 𝒮 \mathcal{S} is a codimension four smooth submanifold of C + 2 ​ ( U a ​ ( Σ)) × K a ​ ( Σ) C_{+}^{2}(U_{a}(\Sigma))\times K_{a}(\Sigma).

###### Proof.

This follows from the fact that Ψ \Psi is a submersion and A ⁡ ( Σ) A(\Sigma) is a codimension 4 4 submanifold. ∎

We will call 𝒮 \mathcal{S} the space of star-shaped squares since if we consider ξ = Ψ ⁡ ( h, θ) \xi=\Psi(h,\theta) for a point ( h, θ) (h,\theta) in 𝒮 \mathcal{S}, then ξ i \xi_{i} ’s are vertices of a square in the fiber of T ​ Σ T\Sigma over a point x x and the four points lie on a star-shaped curve around the origin in T x ​ Σ T_{x}\Sigma; this curve is defined by sending each ( x, v) (x,v) in U a ​ ( Σ) U_{a}(\Sigma) to ( x, h ⁡ ( x, v) ⋅ v) (x,h(x,v)\cdot v) in T x ​ Σ T_{x}\Sigma.

## 4 Star-Shaped Squares

###### Definition.

We define a map F: 𝒮 → C + 2 ​ ( U a ​ ( Σ)) F\colon\mathcal{S}\to C_{+}^{2}(U_{a}(\Sigma)) by restricting the first projection map on C + 2 ​ ( U a ​ ( Σ)) × K a ​ ( Σ) C_{+}^{2}(U_{a}(\Sigma))\times K_{a}(\Sigma) to 𝒮 \mathcal{S}. This is a smooth map on 𝒮 \mathcal{S} since 𝒮 \mathcal{S} is a smooth submanifold of C + 2 ​ ( U a ​ ( Σ)) × K a ​ ( Σ) C_{+}^{2}(U_{a}(\Sigma))\times K_{a}(\Sigma).

###### Remark.

For simplicity, we will denote C + 2 ​ ( U a ​ ( Σ)) × K a ​ ( Σ) C_{+}^{2}(U_{a}(\Sigma))\times K_{a}(\Sigma) by 𝒩 \mathcal{N} and C + 2 ​ ( U a ​ ( Σ)) C_{+}^{2}(U_{a}(\Sigma)) by ℱ \mathcal{F} in the following sections.

###### Lemma 4.1.

The map F F is Fredholm.

###### Proof.

Fix a point ( h, θ) (h,\theta) in 𝒮 \mathcal{S} and consider d ​ F: T ( h, θ) ​ 𝒮 → T h ​ ℱ dF\colon T_{(h,\theta)}\mathcal{S}\to T_{h}\mathcal{F}. We need to show ker ⁡ ( d ​ F) \ker(dF) and coker ​ ( d ​ F) \text{coker}(dF) are finite dimensional. Let p ​ r 1 pr_{1} denote the first projection map on 𝒩 \mathcal{N} and note that ker ⁡ ( d ​ p ​ r 1) \ker(dpr_{1}) at ( h, θ) (h,\theta) is T θ ​ K a ​ ( Σ) T_{\theta}K_{a}(\Sigma) which has dimension 6 6; we conclude that dim ( ker ⁡ ( d ​ F)) \dim(\ker(dF)) is finite. Let W W denote T ( h, θ) ​ 𝒩 T_{(h,\theta)}\mathcal{N} and V V denote T ( h, θ) ​ 𝒮 T_{(h,\theta)}\mathcal{S}. We define a map L: W / V → coker ​ ( d ​ F) L\colon W/V\to\text{coker}(dF) by

 | [w] ↦ [d ​ p ​ r 1 ​ ( w)]. [w]\mapsto[dpr_{1}(w)]. |  |

This map is surjective because p ​ r 1 pr_{1} is a submersion and we know dim ( W / V) = codim ​ ( 𝒮) = 4 \dim(W/V)=\text{codim}(\mathcal{S})=4. Hence, dim ( coker ​ ( d ​ F)) \dim(\text{coker}(dF)) is finite. ∎

Our next step is to compute the index of F F and since index is constant on each connected component of 𝒮 \mathcal{S}, we need to compute the index on each connected component. Fortunately, we only need one of these connected components to prove our Theorem.

###### Definition.

Let ξ \xi be a square inscribed in a curve γ \gamma. We say ξ \xi is graceful if we orient the curve γ \gamma and consider the induced order on the vertices of ξ \xi, this order agrees with the one induced from the circle inscribing ξ \xi. Consider ( h, θ) (h,\theta) in 𝒮 \mathcal{S} and let ξ = Ψ ⁡ ( h, θ) \xi=\Psi(h,\theta). We say ( h, θ) (h,\theta) is graceful if ξ \xi is a graceful square inscribed inside the corresponding curve to h h in T ​ Σ T\Sigma over π ⁡ ( θ) \pi(\theta), where π: K a ​ ( Σ) → Σ \pi\colon K_{a}(\Sigma)\to\Sigma is the bundle projection map.

We denote the subset of graceful squares in 𝒮 \mathcal{S} by 𝒮 0 \mathcal{S}_{0}. We will prove 𝒮 0 \mathcal{S}_{0} is a connected component of 𝒮 \mathcal{S}. Then we find the index of F F over this component. We expect the index to be two because 𝒮 \mathcal{S} has codimension four and K a ​ ( Σ) K_{a}(\Sigma) is six dimensional and indeed, this is what we will show.

###### Lemma 4.2.

Assume ( h 1, θ 1) (h_{1},\theta_{1}) is in 𝒮 0 \mathcal{S}_{0} and there is a path γ \gamma in 𝒮 \mathcal{S} from ( h 1, θ 1) (h_{1},\theta_{1}) to ( h 2, θ 2) (h_{2},\theta_{2}). Then ( h 2, θ 2) (h_{2},\theta_{2}) is also graceful.

###### Proof.

Since the square corresponding to ( h 1, θ 1) (h_{1},\theta_{1}) is graceful, if we consider this square in the fiber of T ​ Σ T\Sigma over π ⁡ ( θ 1) \pi(\theta_{1}), the origin cannot lie in the regions A, B, C, A,B,C, and D D determined by this square in figure 1 1.

A A B B C C D D Figure 1: The four regions that cannot contain the origin

Suppose γ ⁡ ( s) = ( h s, θ s) \gamma(s)=(h_{s},\theta_{s}) is a path in 𝒮 \mathcal{S} starting from ( h 1, θ 1) (h_{1},\theta_{1}) and ending at ( h 2, θ 2) (h_{2},\theta_{2}). By contradiction, assume the square corresponding to ( h 2, θ 2) (h_{2},\theta_{2}) is not graceful. Hence, the origin will enter one of the regions A, B, C, A,B,C, or D D. Without loss of generality, let this region be A A. Then there is a time s 0 s_{0} in between the two ends where the origin lies on the line l l given in figure 2 2.

o o l l A A v 1 v_{1} v 2 v_{2} Figure 2: Line l l and origin o o

Now the two vertices v 1 v_{1} and v 2 v_{2} of the square corresponding to ( h s 0, θ s 0) (h_{s_{0}},\theta_{s_{0}}) lie on the same side of the origin in l l and this contradicts the fact that the curve inscribing this square is star-shaped (this follows from positivity of h s 0 h_{s_{0}}). ∎

###### Proposition 4.3.

The space 𝒮 0 \mathcal{S}_{0} is connected. In particular, it is a connected component of 𝒮 \mathcal{S}; therefore, it is a Banach manifold of codimension four in 𝒩 \mathcal{N}.

###### Proof.

Consider a point ( g, θ) (g,\theta) in 𝒮 0 \mathcal{S}_{0}. This point corresponds to a graceful square that is inscribed in a star-shaped curve around the origin in some fiber T x ​ Σ T_{x}\Sigma. We can also consider the constant function 1 1 and four vertices of a square δ x \delta_{x} on the circle with radius a a around the origin in T x ​ Σ T_{x}\Sigma. This gives us a point ( 1, δ x) (1,\delta_{x}) in 𝒮 0 \mathcal{S}_{0} and all the points of this form in 𝒮 0 \mathcal{S}_{0} can be connected to each other by parallel transport and rotation in their corresponding fibers. Hence, it suffices to prove there is a path between ( g, θ) (g,\theta) and ( 1, δ x) (1,\delta_{x}) in 𝒮 0 \mathcal{S}_{0}.

Since ( g, θ) (g,\theta) corresponds to a graceful square, the origin in T x ​ Σ T_{x}\Sigma cannot lie in the four region defined in terms of this square given in figure 1 1. For any point outside of these four regions, we can find a sufficiently large ellipse going through the four vertices of the square such that the point is inside the ellipse. Consider such an ellipse for the origin; see the figure below.

o o Figure 3: The blue curve is our star-shaped curve.

There is a positive function h h defined on the circle with radius a a around the origin so that the map

 | η ↦ h ⁡ ( η) ⋅ η \eta\mapsto h(\eta)\cdot\eta |  |

takes the circle into the ellipse; extend this function to a positive function on U a ​ ( Σ) U_{a}(\Sigma) and note that g g restricted to the circle of radius a a in T x ​ Σ T_{x}\Sigma will give us the corresponding function for our original curve in T x ​ Σ T_{x}\Sigma. We define a path of positive functions by h t = t ​ h + ( 1 − t) ​ g h_{t}=th+(1-t)g. Note that h t h_{t} is constant for each θ i \theta_{i} in θ \theta because we have fixed the square and only move the curves. Hence, ( h t, θ) (h_{t},\theta) gives a path from ( g, θ) (g,\theta) to ( h, θ) (h,\theta). Now we can translate the ellipse to an ellipse centered around the origin. This gives us a continuous path of functions g t g_{t} and tuples of points θ t \theta_{t} with g 0 = h g_{0}=h and θ 0 = θ \theta_{0}=\theta because each ellipse inscribes a unique square and all the ellipses in the translation contain the origin. Thus we get a path from ( g, θ) (g,\theta) to ( u, σ) (u,\sigma) where Ψ ⁡ ( u, σ) \Psi(u,\sigma) is a square inscribed inside an ellipse centered around the origin in T x ​ Σ T_{x}\Sigma. Now we can take ( u, σ) (u,\sigma) to ( 1, δ x) (1,\delta_{x}) by first a homotopy fixing the four vertices of ( u, σ) (u,\sigma) and then scaling and rotation.

∎

We will need the two following lemmas for computing the index and the transversality argument after that.

###### Lemma 4.4.

Fix a point ( h, θ) (h,\theta) in 𝒮 \mathcal{S}. The space Ψ h ​ ( K a ​ ( Σ)) \Psi_{h}(K_{a}(\Sigma)) is a six dimensional submanifold of Q ⁡ ( Σ) Q(\Sigma) and A ⁡ ( Σ) A(\Sigma) is also a six dimensional submanifold of Q ⁡ ( Σ) Q(\Sigma). There is a one to one correspondence between the kernel of d ​ F: T ( h, θ) ​ 𝒮 → T h ​ ℱ dF\colon T_{(h,\theta)}\mathcal{S}\to T_{h}\mathcal{F} and T ξ ​ Ψ h ​ ( K a ​ ( Σ)) ∩ T ξ ​ A ​ ( Σ) T_{\xi}\Psi_{h}(K_{a}(\Sigma))\cap T_{\xi}A(\Sigma) where ξ = Ψ ⁡ ( h, θ) \xi=\Psi(h,\theta).

###### Proof.

Suppose v v is a vector in the kernel of d ​ F dF over ( h, θ) (h,\theta). Then we can write v v as a pair ( 0, η) (0,\eta) where η \eta is a vector in T θ ​ K a ​ ( Σ) T_{\theta}K_{a}(\Sigma) since F F is restriction of the first projection map to 𝒮 \mathcal{S}. Now since v v lies in the tangent space of 𝒮 \mathcal{S} over ( h, θ) (h,\theta), we have

 | d ​ Ψ ( h, θ) ​ [( 0, η)] = d ​ Ψ h ​ [η] ∈ T ξ ​ A. d\Psi_{(h,\theta)}[(0,\eta)]=d\Psi_{h}[\eta]\in T_{\xi}A. |  |

A similar argument shows if a vector δ \delta is in T ξ ​ Ψ h ​ ( K a ​ ( Σ)) ∩ T ξ ​ A T_{\xi}\Psi_{h}(K_{a}(\Sigma))\cap T_{\xi}A, then δ = d ​ Ψ h ​ [η] \delta=d\Psi_{h}[\eta] for some vector η \eta in T θ ​ K a ​ ( Σ) T_{\theta}K_{a}(\Sigma) and ( 0, η) (0,\eta) lies in the kernel of d ​ F dF. ∎

###### Lemma 4.5.

Let ( h, θ) (h,\theta) be a point in 𝒮 \mathcal{S} and assume ξ = Ψ ⁡ ( h, θ) \xi=\Psi(h,\theta) is a transverse intersection point of Ψ h ​ ( K a ​ ( Σ)) \Psi_{h}(K_{a}(\Sigma)) and A ⁡ ( Σ) A(\Sigma). Then d ​ F: T ( h, θ) ​ 𝒮 → T h ​ ℱ dF\colon T_{(h,\theta)}\mathcal{S}\to T_{h}\mathcal{F} is surjective.

###### Proof.

We can identify T h ​ ℱ T_{h}\mathcal{F} with the space of all C 2 C^{2} functions on U a ​ ( Σ) U_{a}(\Sigma); let g g be an arbitrary function in T h ​ ℱ T_{h}\mathcal{F}. Consider v = ( g, 0) v=(g,0) in T ( h, θ) ​ 𝒩 T_{(h,\theta)}\mathcal{N} and define w = d ​ Ψ ( h, θ) ​ [v] w=d\Psi_{(h,\theta)}[v] to be its image in T ξ ​ Q a ​ ( Σ) T_{\xi}Q_{a}(\Sigma). We can write w w as w A + w K w_{A}+w_{K} where w A w_{A} is in T ξ ​ A ​ ( Σ) T_{\xi}A(\Sigma) and w K w_{K} is in T ξ ​ K a ​ ( Σ) T_{\xi}K_{a}(\Sigma) because we assumed ξ \xi is a transverse intersection point. There exists a vector η \eta in T θ ​ K a ​ ( Σ) T_{\theta}K_{a}(\Sigma) such that w K = d ​ Ψ h ​ [η] w_{K}=d\Psi_{h}[\eta]. Now consider the vector v ~ = ( g, − η) \tilde{v}=(g,-\eta) in T ( h, θ) ​ 𝒩 T_{(h,\theta)}\mathcal{N}; we get

 | d ​ Ψ ​ [v ~] = d ​ Ψ ​ [v] + d ​ Ψ ​ [( 0, − η)] = w − w K = w A ∈ T ξ ​ A ​ ( Σ). d\Psi[\tilde{v}]=d\Psi[v]+d\Psi[(0,-\eta)]=w-w_{K}=w_{A}\in T_{\xi}A(\Sigma). |  |

Hence, v ~ \tilde{v} lies in T ( h, θ) ​ 𝒮 T_{(h,\theta)}\mathcal{S} and we have d ​ F ​ [v ~] = g dF[\tilde{v}]=g. ∎

###### Proposition 4.6.

The map F F has index 2 2 over 𝒮 0 \mathcal{S}_{0}.

###### Proof.

Let x x be a point on Σ \Sigma. Assume e 1, e 2 e_{1},e_{2} are an orthonormal basis for T ​ Σ T\Sigma in a disk D D around x x and let v 1 v_{1} and v 2 v_{2} denote the corresponding coordinates for T ​ Σ T\Sigma above D D. Define a local fiber bundle of ellipses around x x by

 | E ≔ { ( y, v 1, v 2) | v 1 2 + 2 ⋅ v 2 2 = 1 }. E\coloneqq\{(y,v_{1},v_{2})|v_{1}^{2}+2\cdot v_{2}^{2}=1\}. |  |

There is a positive function h h defined on U a ​ ( S 2) U_{a}(S^{2}) above D D such that the map

 | η ↦ h ⁡ ( η) ⋅ η \eta\mapsto h(\eta)\cdot\eta |  |

takes U a ​ ( S 2) U_{a}(S^{2}) for each point in D D to the ellipse above that point. Extend h h to a positive function h ~ \tilde{h} in ℱ \mathcal{F} and let θ \theta be the four-tuple of points in K a ​ ( Σ) K_{a}(\Sigma) over x x that corresponds to the unique graceful square inscribed in E x E_{x}. Then ξ = Ψ ⁡ ( h ~, θ) \xi=\Psi(\tilde{h},\theta) is a transverse intersection point of Ψ h ~ ​ ( K a ​ ( Σ)) \Psi_{\tilde{h}}(K_{a}(\Sigma)) and A ⁡ ( Σ) A(\Sigma) because around x x all the corresponding curves are ellipses and these meet the space of squares transversely; in fact, Ψ h ~ ​ ( K a ​ ( Σ)) ∩ A ⁡ ( Σ) \Psi_{\tilde{h}}(K_{a}(\Sigma))\cap A(\Sigma) is locally a two dimensional disk around ξ \xi. Therefore, by Lemma 4.4, we know ker ⁡ ( d ​ F) \ker(dF) has dimension two at ( h ~, θ) (\tilde{h},\theta) and by Lemma 4.5, we know d ​ F dF is surjective at this point. We conclude that F F has index two since 𝒮 0 \mathcal{S}_{0} is connected. ∎

###### Lemma 4.7.

The map F F restricted to 𝒮 0 \mathcal{S}_{0} is surjective.

###### Proof.

Consider a function h h in ℱ \mathcal{F}. We know Ψ h ​ ( K a ​ ( Σ)) ∩ A ⁡ ( Σ) \Psi_{h}(K_{a}(\Sigma))\cap A(\Sigma) is non-empty and at least on of these intersection points corresponds to a graceful square since each of the star-shaped curves corresponding to h h in fibers of T ​ Σ T\Sigma inscribes at least one graceful square. We prove this Theorem in the appendix (Theorem A.5); see also [12, 4] for other versions of this result. Hence, there is a θ ∈ K a ​ ( Σ) \theta\in K_{a}(\Sigma) such that ( h, θ) (h,\theta) lies in 𝒮 0 \mathcal{S}_{0}. ∎

###### Proposition 4.8.

If h h is a regular value of F F restricted to 𝒮 0 \mathcal{S}_{0}, then Ψ h ​ ( K a ​ ( Σ)) \Psi_{h}(K_{a}(\Sigma)) and A ⁡ ( Σ) A(\Sigma) intersect transversely in Q ⁡ ( Σ) Q(\Sigma) at graceful intersection points; in particular, the subset of graceful squares in Ψ h ​ ( K a ​ ( Σ)) ∩ A ⁡ ( Σ) \Psi_{h}(K_{a}(\Sigma))\cap A(\Sigma) is a two dimensional manifold.

###### Proof.

Consider ( h, θ) (h,\theta) in 𝒮 0 \mathcal{S}_{0} and ξ = Ψ ⁡ ( h, θ) \xi=\Psi(h,\theta) in A ⁡ ( Σ) A(\Sigma). Since h h is a regular value of F F, the kernel of d ​ F dF at ( h, θ) (h,\theta) is two dimensional and this proves T ξ ​ Ψ h ​ ( K a ​ ( Σ)) ∩ T ξ ​ A ​ ( Σ) T_{\xi}\Psi_{h}(K_{a}(\Sigma))\cap T_{\xi}A(\Sigma) is two dimensional by Lemma 4.4. Both T ξ ​ Ψ h ​ ( K a ​ ( Σ)) T_{\xi}\Psi_{h}(K_{a}(\Sigma)) and T ξ ​ A ​ ( Σ) T_{\xi}A(\Sigma) are six dimensional subspaces of T ξ ​ Q a ​ ( Σ) T_{\xi}Q_{a}(\Sigma) which has dimension ten. We conclude the two subspaces meet transversely because their intersection has dimension two so the subset of graceful squares in Ψ h ​ ( K a ​ ( Σ)) ∩ A ⁡ ( Σ) \Psi_{h}(K_{a}(\Sigma))\cap A(\Sigma) is a surface. ∎

###### Corollary 4.9.

There exists a dense subset of functions in ℱ \mathcal{F} such that Ψ h ​ ( K a ​ ( Σ)) \Psi_{h}(K_{a}(\Sigma)) intersects A ⁡ ( Σ) A(\Sigma) transversely at graceful squares for every function h h in this subset.

###### Proof.

Consider the regular values of F F; by Proposition 4.8, we know the intersection is transverse at graceful squares for every element in this subset. The map F F is a surjective C ∞ C^{\infty} Fredholm map of index two between connected second countable Banach manifolds. Thus its regular values are dense in ℱ \mathcal{F} by Sard-Smale Theorem; see [11] for more details. ∎

## 5 Proof of the Main Theorem

###### Lemma 5.1.

Suppose h h is a regular value of F F restricted to 𝒮 0 \mathcal{S}_{0}. Then the subset of graceful squares in Ψ h ​ ( K a ​ ( Σ)) ∩ A ⁡ ( Σ) \Psi_{h}(K_{a}(\Sigma))\cap A(\Sigma) is a compact surface.

###### Proof.

Let Σ h \Sigma_{h} denote the subset of graceful squares in Ψ h ​ ( K a ​ ( Σ)) ∩ A ⁡ ( Σ) \Psi_{h}(K_{a}(\Sigma))\cap A(\Sigma) and note that this is a surface by proposition 4.8. Now consider a sequence a n = Ψ h ​ ( θ n) a_{n}=\Psi_{h}(\theta_{n}) in Σ h \Sigma_{h} and since θ n \theta_{n} is in K a ​ ( Σ) K_{a}(\Sigma), we can assume θ n \theta_{n} converges to a point θ \theta in s ​ y ​ m 4 ​ ( T ​ Σ) sym^{4}(T\Sigma) after passing to a subsequence. The point θ \theta is not in the fat diagonal of s ​ y ​ m 4 ​ ( T ​ Σ) sym^{4}(T\Sigma) because the function h h is C 2 C^{2} and we can uniformly bound the curvature of all the star-shaped curves corresponding to h h; thus there is a positive lower bound for the side length of all the squares a n a_{n} and Ψ h ​ ( θ) \Psi_{h}(\theta) is a non-degenerate square. The square Ψ h ​ ( θ) \Psi_{h}(\theta) is graceful since it is the limit of a sequence of graceful squares. ∎

###### Remark.

Note that for a function h h in regular values of F | 𝒮 0 F\big|_{\mathcal{S}_{0}}, the surface Σ h \Sigma_{h} is not necessarily orientable because K a ​ ( Σ) K_{a}(\Sigma) is non-orientable.

###### Proposition 5.2.

Assume h h is a regular value of F | 𝒮 0 F\big|_{\mathcal{S}_{0}}. Then [Σ h] [\Sigma_{h}] is non-zero in H 2 ​ ( s ​ y ​ m 4 ​ ( T ​ Σ), ℤ 2) ≅ ℤ 2 H_{2}(sym^{4}(T\Sigma);\mathbb{Z}_{2})\cong\mathbb{Z}_{2}.

###### Proof.

Let π \pi denote the bundle projection map from s ​ y ​ m 4 ​ ( T ​ Σ) sym^{4}(T\Sigma) to Σ \Sigma; this is a deformation retract onto Σ \Sigma. Consider the restriction of π \pi to Σ h \Sigma_{h}; we will show this map has non-zero mod 2 2 degree. Suppose x ∈ Σ x\in\Sigma is a regular value of this map. Then for every θ \theta in π − 1 ​ ( x) ∩ Σ h \pi^{-1}(x)\cap\Sigma_{h}, T θ ​ Σ h T_{\theta}\Sigma_{h} is a horizontal subspace of T θ ​ s ​ y ​ m 4 ​ ( T ​ Σ) T_{\theta}sym^{4}(T\Sigma) by assumption. In particular, T θ ​ Ψ h ​ ( K a ​ ( Σ)) T_{\theta}\Psi_{h}(K_{a}(\Sigma)) and T θ ​ A ​ ( Σ) T_{\theta}A(\Sigma) have no vertical intersection and this proves the manifold of squares in T x ​ Σ T_{x}\Sigma and fourth symmetric product of the star-shaped curve corresponding to h h above x x meet transversely at every θ \theta in π − 1 ​ ( x) ∩ Σ h \pi^{-1}(x)\cap\Sigma_{h}. Therefore, this curve has finitely many graceful squares and the mod 2 2 degree of π \pi is equal to the number of graceful squares inscribed inside this curve mod 2 2. It is proved in the appendix (corollary A.6) that a generic star-shaped curve has an odd number of graceful squares; this was originally proved in [12] for generic smooth curves and it was proved in [10] for generic PL curves. The curve corresponding to h h above x x is a generic one because of the transversal intersection and we conclude the proposition. ∎

We define a map c: s ​ y ​ m 4 ​ ( T ​ Σ) → T ​ Σ c\colon sym^{4}(T\Sigma)\to T\Sigma by

 | [θ 1, θ 2, θ 3, θ 4] ↦ ∑ θ i 4. [\theta_{1},\theta_{2},\theta_{3},\theta_{4}]\mapsto\frac{\sum\theta_{i}}{4}. |  |

We call c c the center map; note that c c is a homotopy equivalence.

###### Proposition 5.3.

Suppose h h is a regular value of F | 𝒮 0 F\big|_{\mathcal{S}_{0}} and Σ \Sigma is a surface with odd Euler characteristic. Then c c vanishes at some point on the surface Σ h = Ψ ⁡ ( F − 1 ​ ( h) ∩ 𝒮 0) \Sigma_{h}=\Psi(F^{-1}(h)\cap\mathcal{S}_{0}).

###### Proof.

By Proposition 5.2, we know [Σ h] [\Sigma_{h}] is a non-zero homology class. Hence, c ∗ ​ [Σ h] c_{*}[\Sigma_{h}] is also a non-zero homology class in T ​ Σ T\Sigma. The mod 2 2 intersection number of such homology classes with the zero section in T ​ Σ T\Sigma is equal to the second Stiefel–Whitney number of Σ \Sigma and this is equal to χ ⁡ ( Σ) \chi(\Sigma) mod 2 2; see [7] for more details. We conclude that this intersection number is non-zero because we assumed Σ \Sigma has odd Euler characteristic. ∎

###### Remark.

Proposition 5.3 shows for every regular value h h of F | 𝒮 0 F\big|_{\mathcal{S}_{0}}, there is a point x x in Σ \Sigma so that the star shaped curve corresponding to h h above x x inscribes a graceful square centered around the origin in T x ​ Σ T_{x}\Sigma.

###### Lemma 5.4.

Consider a positive function h h in regular values of F | 𝒮 0 F\big|_{\mathcal{S}_{0}} and let

 | Ψ ⁡ ( h, θ) = ξ = [ξ 1, ξ 2, ξ 3, ξ 4] \Psi(h,\theta)=\xi=[\xi_{1},\xi_{2},\xi_{3},\xi_{4}] |  |

be a four-tuple in A ⁡ ( Σ) ∩ Ψ h ​ ( K a ​ ( Σ)) A(\Sigma)\cap\Psi_{h}(K_{a}(\Sigma)) over a point x x in Σ \Sigma. Assume we have ξ 1 + ξ 2 + ξ 3 + ξ 4 = 0 \xi_{1}+\xi_{2}+\xi_{3}+\xi_{4}=0. Then we must have

 | h ⁡ ( θ 1) = h ⁡ ( θ 2) = h ⁡ ( θ 3) = h ⁡ ( θ 4) h(\theta_{1})=h(\theta_{2})=h(\theta_{3})=h(\theta_{4}) |  | (3) |

and θ i \theta_{i} ’s are vertices of a square inscribed in U a ​ Σ | x U_{a}\Sigma\big|_{x}.

###### Proof.

After reordering the four-tuple ξ \xi, we can assume

 | ξ 1 = − ξ 3, ξ 2 = − ξ 4, \xi_{1}=-\xi_{3},\hskip 5.69054pt\xi_{2}=-\xi_{4}, |  |

and ξ 1 ⋅ ξ 2 = 0 \xi_{1}\cdot\xi_{2}=0 since ξ i \xi_{i} ’s are vertices of a square centered at the origin. Thus we get

 | θ 1 ⋅ θ 2 = ξ 1 ⋅ ξ 2 h ⁡ ( θ 1) ​ h ​ ( θ 2) = 0. \theta_{1}\cdot\theta_{2}=\frac{\xi_{1}\cdot\xi_{2}}{h(\theta_{1})h(\theta_{2})}=0. |  |

Moreover, we have

 | h ⁡ ( θ 1) ​ θ 1 = ξ 1 = − ξ 3 = − h ⁡ ( θ 3) ​ θ 3. h(\theta_{1})\theta_{1}=\xi_{1}=-\xi_{3}=-h(\theta_{3})\theta_{3}. |  |

Hence, we can write

 | θ 3 = − h ⁡ ( θ 1) h ⁡ ( θ 3) ​ θ 1. \theta_{3}=\frac{-h(\theta_{1})}{h(\theta_{3})}\theta_{1}. |  |

Since θ 1 \theta_{1} and θ 3 \theta_{3} have the same length, we deduce that h ⁡ ( θ 1) = h ⁡ ( θ 3) h(\theta_{1})=h(\theta_{3}) by positivity of h h and θ 1 = − θ 3 \theta_{1}=-\theta_{3}. A similar argument shows h ⁡ ( θ 2) = h ⁡ ( θ 4) h(\theta_{2})=h(\theta_{4}) and θ 2 = − θ 4 \theta_{2}=-\theta_{4}. Therefore, θ i \theta_{i} ’s are vertices of a square on the circle with radius a a around the origin in T x ​ Σ T_{x}\Sigma; two vertices of this square are scaled by h ⁡ ( θ 1) h(\theta_{1}) and the other two by h ⁡ ( θ 2) h(\theta_{2}). Since the scaled shape is also a square by assumption, we conclude that h ⁡ ( θ 1) = h ⁡ ( θ 2) h(\theta_{1})=h(\theta_{2}). ∎

###### Definition.

Assume f f is a positive function on Σ \Sigma. We define a positive function f ~ \tilde{f} on U a ​ ( Σ) U_{a}(\Sigma) by

 | ( x, v) ↦ f ⁡ ( exp ⁡ ( x, v)). (x,v)\mapsto f(\exp(x,v)). |  |

###### Proof of Theorem 1.1.

Since Σ \Sigma is compact, it suffices to prove the Theorem for positive functions. Let f f be a positive continuous function on Σ \Sigma and consider f ~ \tilde{f} on U a ​ Σ U_{a}\Sigma for a = d 2 a=\frac{d}{2}. By Corollary 4.9, we can find a sequence of functions u n u_{n} in regular values of F | 𝒮 0 F\big|_{\mathcal{S}_{0}} such that u n u_{n} converges to f ~ \tilde{f} uniformly on U a ​ Σ U_{a}\Sigma. By Lemma 5.4 and Proposition 5.3, we know there is a sequence of graceful squares θ n \theta_{n} inscribed inside the fibers of U a ​ Σ U_{a}\Sigma such that u n u_{n} takes the same value on the four vertices of θ n \theta_{n} for every n n. After passing to a subsequence, we can assume θ n \theta_{n} converges to θ \theta, a square with the same side length as θ n \theta_{n} ’s and inscribed inside the fiber of U a ​ Σ U_{a}\Sigma over a point x x in Σ \Sigma. All the vertices of θ \theta take the same value under f ~ \tilde{f} by uniform convergence and the assumption on u n u_{n} ’s. Hence, we conclude f f admits a table determined by the four vertices of θ \theta. ∎

###### Proof of Corollary 1.2.

Let f f be an even function on S 2 S^{2} and g g a Riemannian metric invariant under the antipodal map. This gives us a function f ¯ \bar{f} and a Riemannian metric g ¯ \bar{g} on ℝ ​ P 2 \mathbb{R}P^{2}. Now apply Theorem 1.1 to this Riemannian surface and the function f ¯ \bar{f}. The table for f ¯ \bar{f} on ℝ ​ P 2 \mathbb{R}P^{2} lifts to two tables for f f on S 2 S^{2}. ∎

Appendix

## Appendix A Square Peg for Star-Shaped Curves

Our goal in this appendix is to prove the square peg problem for C 2 C^{2} star-shaped curves (Theorem A.5). We will also prove a generic star-shaped curve has an odd number of squares; this is corollary A.6. Furthermore, we will show that if we orient a generic star-shaped curve, then the curve inscribes an odd number of squares that are consistent with this orientation. The first version of this result was proved in [12] for all smooth curves; see [5] for a modern version of this proof. We will reprove this result for C 2 C^{2} star-shaped curves using similar ideas to [5] in combination with modern transversality arguments.

###### Definition.

Let γ \gamma be an oriented curve in the plane and suppose Q Q is an inscribed square inside γ \gamma. We say Q Q is graceful if γ \gamma induces the same order on the vertices of Q Q as the circle that inscribes this square.

We will prove every star-shaped curve inscribes a graceful square. Let h h be a positive C 2 C^{2} function on S 1 S^{1}; we can define a C 2 C^{2} curve in the plane via the following.

 | θ ↦ h ⁡ ( θ) ⋅ θ, ∀ θ ∈ S 1. \theta\mapsto h(\theta)\cdot\theta,\hskip 8.53581pt\forall\theta\in S^{1}. |  |

Every C 2 C^{2} star-shaped curve can be parametrized by a positive C 2 C^{2} function on S 1 S^{1} in this manner. Let Δ 3 \Delta_{3} denote the three dimensional simplex and consider its interior Δ ̊ 3 \mathring{\Delta}_{3}. Suppose γ \gamma is a star-shaped curve in the plane and it is parametrized by a positive function h h on S 1 S^{1}. We can parametrize all the quadrilaterals inscribed in γ \gamma with S 1 × Δ ̊ 3 S^{1}\times\mathring{\Delta}_{3} in the following way.

 | [x, ( t 0, t 1, t 2, t 3)] ↦ \displaystyle[x,(t_{0},t_{1},t_{2},t_{3})]\mapsto | [f ( x) ⋅ x, f ( e i ​ π ​ t 0 ⋅ x) ⋅ ( e i ​ π ​ t 0 ⋅ x), f ( e i ​ π ​ ( t 0 + t 1) x) ⋅ ( e i ​ π ​ ( t 0 + t 1) ⋅ x), \displaystyle[f(x)\cdot x,f(e^{i\pi t_{0}}\cdot x)\cdot(e^{i\pi t_{0}}\cdot x),f(e^{i\pi(t_{0}+t_{1})}x)\cdot(e^{i\pi(t_{0}+t_{1})}\cdot x), |  |

 |  | f ( e i ​ π ​ ( t 0 + t 1 + t 2) ⋅ x) ⋅ ( e i ​ π ​ ( t 0 + t 1 + t 2) ⋅ x)], \displaystyle f(e^{i\pi(t_{0}+t_{1}+t_{2})}\cdot x)\cdot(e^{i\pi(t_{0}+t_{1}+t_{2})}\cdot x)], |  |

where x x is a point in S 1 S^{1} and t t is an interior point of Δ 3 \Delta_{3}. We will denote S 1 × Δ ̊ 3 S^{1}\times\mathring{\Delta}_{3} by P ~ \tilde{P} and the above equation gives us a map from P ~ \tilde{P} to ℝ 8 \mathbb{R}^{8}. Every positive function h h on S 1 S^{1} gives us such a map and we denote this map by φ h \varphi_{h}

Consider all the four tuples ( x 1, x 2, x 3, x 4) (x_{1},x_{2},x_{3},x_{4}) in ( ℝ 2) 4 ≅ ℝ 8 (\mathbb{R}^{2})^{4}\cong\mathbb{R}^{8} such that

 | ‖ x 1 − x 2 ‖ = \displaystyle\|x_{1}-x_{2}\|= | ‖ x 2 − x 3 ‖ = ‖ x 3 − x 4 ‖ = ‖ x 4 − x 1 ‖, \displaystyle\|x_{2}-x_{3}\|=\|x_{3}-x_{4}\|=\|x_{4}-x_{1}\|, |  |

 |  | ‖ x 1 − x 3 ‖ = ‖ x 2 − x 4 ‖, \displaystyle\|x_{1}-x_{3}\|=\|x_{2}-x_{4}\|, |  |

and all the x i x_{i} ’s are distinct; we denote this subset of ℝ 8 \mathbb{R}^{8} by A ~ \tilde{A}. This space is a non-compact submanifold of dimension 4 4 in ℝ 8 \mathbb{R}^{8}.

###### Remark.

For a fixed positive function h h on S 1 S^{1}, the set φ h ​ ( P ~) ∩ A ~ \varphi_{h}(\tilde{P})\cap\tilde{A} corresponds to graceful squares inscribed inside the star-shaped curve parametrized by h h. Every graceful square of this curve corresponds to four points in this intersection.

###### Remark.

Note that φ h \varphi_{h} is an embedding of P ~ \tilde{P} into ℝ 8 \mathbb{R}^{8} and image of this map avoids the fat diagonal in ℝ 8 ≅ ( ℝ 2) 4 \mathbb{R}^{8}\cong(\mathbb{R}^{2})^{4} for every positive function h h.

There is a free action of ℤ 4 \mathbb{Z}_{4} on P ~ \tilde{P} generated by

 | [x, ( t 0, t 1, t 2, t 3)] ↦ [e i ​ π ​ t 0 ⋅ x, ( t 1, t 2, t 3, t 0)]. [x,(t_{0},t_{1},t_{2},t_{3})]\mapsto[e^{i\pi t_{0}}\cdot x,(t_{1},t_{2},t_{3},t_{0})]. |  |

We denote this generator by ε \varepsilon. There is also a ℤ 4 \mathbb{Z}_{4} action on ℝ 8 ≅ ( ℝ 2) 4 \mathbb{R}^{8}\cong(\mathbb{R}^{2})^{4} generated by

 | ( x 1, x 2, x 3, x 4) ↦ ( x 2, x 3, x 4, x 1). (x_{1},x_{2},x_{3},x_{4})\mapsto(x_{2},x_{3},x_{4},x_{1}). |  |

This action is free away from the fat diagonal in ℝ 8 \mathbb{R}^{8}. Note that φ h \varphi_{h} is equivariant with respect to the cyclic actions on its range and domain. We quotient P ~ \tilde{P} by this action and denote the resulting space by P P; we also quotient complement of the fat diagonal in ℝ 8 ≅ ( ℝ 2) 4 \mathbb{R}^{8}\cong(\mathbb{R}^{2})^{4} by the cyclic action and denote the resulting space by V V. Since φ h \varphi_{h} is equivariant, it descends to a map from P P to V V for every positive function h h; by an abuse of notation, we also denote this map by φ h \varphi_{h}. Let A A be the quotient of A ~ \tilde{A} in V V. Now there is only one intersection point in φ h ​ ( P) ∩ A \varphi_{h}(P)\cap A corresponding to each graceful square inscribed in the star-shaped curve parametrized by h h.

Define a map Φ: C + 2 ​ ( S 1) × P → V \Phi\colon C^{2}_{+}(S^{1})\times P\to V by

 | Φ ⁡ ( h, ( x, t)) = φ h ​ ( x, t). \Phi(h,(x,t))=\varphi_{h}(x,t). |  |

Note that C + 2 ​ ( S 1) C^{2}_{+}(S^{1}) is an open subset of C 2 ​ ( S 1) C^{2}(S^{1}) and in particular, it is a Banach manifold.

###### Lemma A.1.

The map Φ \Phi is a submersion.

###### Proof.

Consider a point ( h, ( x, t)) (h,(x,t)) in C + 2 ​ ( S 1) × P C^{2}_{+}(S^{1})\times P and suppose t = ( t 0, t 1, t 2, t 3) t=(t_{0},t_{1},t_{2},t_{3}). Let δ \delta be a positive number less than t 0 t_{0}. We define a curve γ \gamma in P P given by

 | γ ⁡ ( s) = ( e 2 ​ π ​ i ​ s ⋅ x, t 0 − s, t 1, t 2, t 3 + s) \gamma(s)=(e^{2\pi is}\cdot x,t_{0}-s,t_{1},t_{2},t_{3}+s) |  |

for s s in [0, δ) [0,\delta). This curve moves the first vertex of the quadrilateral corresponding to ( x, t) (x,t) and fixes the other three. Now if we consider the curve ( h, γ ⁡ ( s)) (h,\gamma(s)) in C + 2 ​ ( S 1) × P C^{2}_{+}(S^{1})\times P, we have

 | Φ ⁡ ( h, γ ⁡ ( s)) = ( h ⁡ ( e 2 ​ π ​ i ​ s ⋅ x) ⋅ e 2 ​ π ​ i ​ s ⋅ x, h ⁡ ( x 2) ⋅ x 2, h ⁡ ( x 3) ⋅ x 3, h ⁡ ( x 4) ⋅ x 4) \Phi(h,\gamma(s))=(h(e^{2\pi is}\cdot x)\cdot e^{2\pi is}\cdot x,h(x_{2})\cdot x_{2},h(x_{3})\cdot x_{3},h(x_{4})\cdot x_{4}) |  |

where x 2, x 3, x_{2},x_{3}, and x 4 x_{4} are the other three vertices corresponding to ( x, t) (x,t). Hence, if we let v v denote the derivative of ( h, γ ⁡ ( s)) (h,\gamma(s)) at s = 0 s=0, we get

 | d ​ Φ ( h, ( x, t)) ​ [v] = ( h ⁡ ( x) ⋅ 2 ​ π ​ i ⋅ x + h ′ ​ ( x) ⋅ x, 0, 0, 0), d\Phi_{(h,(x,t))}[v]=(h(x)\cdot 2\pi i\cdot x+h^{\prime}(x)\cdot x,0,0,0), |  | (4) |

where h ⁡ ( x) h(x) is a positive number by definition and h ′ ​ ( x) h^{\prime}(x) is an arbitrary real number. Similarly, we can move the other vertices and get vectors of the form in equation ( 4) such that all the coordinates are zero except one of them and the non-zero coordinate is equal to r ⋅ i ⋅ x + a ⋅ x r\cdot i\cdot x+a\cdot x for a positive r r and an arbitrary number a a. Now consider a C 2 C^{2} function g g on S 1 S^{1} so that we have g ⁡ ( x) = 1 g(x)=1 and g ⁡ ( x 2) = g ⁡ ( x 3) = g ⁡ ( x 4) = 0 g(x_{2})=g(x_{3})=g(x_{4})=0. For small real numbers s s, all the functions h + s ⋅ g h+s\cdot g will be in C + 2 ​ ( S 1) C^{2}_{+}(S^{1}) and we have

 | d ​ Φ ( h, ( x, t)) ​ [( g, 0)] = d d ​ s | 0 ​ Φ ​ ( h + s ⋅ g, ( x, t)) = ( g ⁡ ( x) ⋅ x, g ⁡ ( x 2) ⋅ x 2, g ⁡ ( x 3) ⋅ x 3, g ⁡ ( x 4) ⋅ x 4) = ( x, 0, 0, 0). d\Phi_{(h,(x,t))}[(g,0)]=\frac{d}{ds}\Big|_{0}\Phi(h+s\cdot g,(x,t))=(g(x)\cdot x,g(x_{2})\cdot x_{2},g(x_{3})\cdot x_{3},g(x_{4})\cdot x_{4})=(x,0,0,0). |  | (5) |

We conclude the proof since all the vectors of the form given in equations ( 4) and ( 5) generate ℝ 8 ≅ T Φ ⁡ ( h, ( x, t)) ​ V \mathbb{R}^{8}\cong T_{\Phi(h,(x,t))}V. ∎

Now that we know Φ \Phi is a submersion, we conclude that Φ − 1 ​ ( A) \Phi^{-1}(A) is a codimension 4 4 submanifold of C + 2 ​ ( S 1) × P C^{2}_{+}(S^{1})\times P. We denote this submanifold by 𝒬 \mathcal{Q} and let π: 𝒬 → C + 2 ​ ( S 1) \pi\colon\mathcal{Q}\to C^{2}_{+}(S^{1}) be restriction of the first projection map to 𝒬 \mathcal{Q}.

###### Lemma A.2.

The space 𝒬 \mathcal{Q} is connected and the map π \pi is Fredholm. Moreover, π \pi has index 0 0.

###### Proof.

The connectivity of 𝒬 \mathcal{Q} follows the same way we proved 𝒮 0 \mathcal{S}_{0} is connected in Proposition 4.3 and π \pi being Fredholm follows from the same strategy in 4.1. For the index computation, take a function g g such that the curve parametrized by g g is an ellipse. Then we know φ g ​ ( P) \varphi_{g}(P) intersect A A transversely and we can prove π \pi has index zero at this point using an argument similar to the one given in Proposition 4.6. ∎

###### Definition.

Let h h be a positive function on S 1 S^{1}. We say the star-shaped curve corresponding to h h is generic if φ h ​ ( P) \varphi_{h}(P) intersects A A transversely. Note that a C 2 C^{2} generic curve has finitely many graceful squares.

In the following, we call a positive function generic if its corresponding curve is generic.

###### Lemma A.3.

A positive function h h is generic if and only if it is a regular value of π \pi.

###### Proof.

This can be proved using a similar argument as in Lemma 4.4 and 4.5. ∎

###### Corollary A.4.

The set of generic functions are dense in C + 2 ​ ( S 1) C^{2}_{+}(S^{1}).

###### Proof.

This follows from Sard-Smale Theorem. ∎

###### Theorem A.5.

Every star-shaped C 2 C^{2} curve inscribes at least one graceful square.

###### Proof.

By contradiction, assume there is a star-shaped C 2 C^{2} curve that does not admit a graceful square and let h h be the positive function that parametrizes this function. By assumption, h h is not in the image of π \pi so it is a regular value of π \pi by definition. Let g g be a positive function that parametrizes an ellipse; hence g g is in regular values of π \pi and π − 1 ​ ( g) \pi^{-1}(g) is just a point corresponding to the unique square inscribed inside this ellipse. Consider a path of positive functions h s h_{s} in C + 2 ​ ( S 1) C^{2}_{+}(S^{1}) such that

 | h 0 = g, h 1 = h h_{0}=g,\hskip 8.53581pth_{1}=h |  |

and π − 1 ​ ( h s) \pi^{-1}(h_{s}) is a one manifold. We can find such a generic path because both g g and h h are regular values of π \pi. The one manifold π − 1 ​ ( h s) \pi^{-1}(h_{s}) is compact since we can uniformly bound the total curvature of all the curves corresponding to h s h_{s} for each s s. This compact one manifold has only one boundary point corresponding to the square inscribed inside the ellipse which is a contradiction. ∎

We get the following as a corollary of the cobordism argument given in the previous proof.

###### Corollary A.6.

A generic star-shaped curve inscribes an odd number of graceful squares.

## References

- [1] Jason Cantarella, Elizabeth Denne, and John McCleary, *Configuration spaces, multijet transversality, and the square-peg problem*, Illinois J. Math. 66 (2022), no. 3, 385–420. MR 4477422
- [2] F. J. Dyson, *Continuous functions defined on spheres*, Ann. of Math. (2) 54 (1951), 534–536. MR 44620
- [3] Roger Fenn, *The table theorem*, Bull. London Math. Soc. 2 (1970), 73–76. MR 271940
- [4] Joshua Evan Greene and Andrew Lobb, *The rectangular peg problem*, Ann. of Math. (2) 194 (2021), no. 2, 509–517. MR 4298749
- [5] Benjamin Matschke, *Equivariant topology methods in discrete geometry*, (2011).
- [6] Benjamin Matschke, *A survey on the square peg problem*, Notices Amer. Math. Soc. 61 (2014), no. 4, 346–352. MR 3184501
- [7] John W. Milnor and James D. Stasheff, *Characteristic classes*, Annals of Mathematics Studies, vol. No. 76, Princeton University Press, Princeton, NJ; University of Tokyo Press, Tokyo, 1974. MR 440554
- [8] John Douglas Moore, *Introduction to global analysis*, Graduate Studies in Mathematics, vol. 187, American Mathematical Society, Providence, RI, 2017, Minimal surfaces in Riemannian manifolds. MR 3729450
- [9] H. R. Morton, *Symmetric products of the circle*, Proc. Cambridge Philos. Soc. 63 (1967), 349–352. MR 210096
- [10] Richard Evan Schwartz, *Rectangles, curves, and Klein bottles*, Bull. Amer. Math. Soc. (N.S.) 59 (2022), no. 1, 1–17. MR 4340824
- [11] S. Smale, *An infinite dimensional version of Sard’s theorem*, Amer. J. Math. 87 (1965), 861–866. MR 185604
- [12] L. G. Snirelman, *On certain geometrical properties of closed curves*, Uspehi Matem. Nauk 10 (1944), 34–44. MR 12531

Boston College. Massachusetts, USA.

naserisa@bc.edu

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2412.01976
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2412.01977
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2412.01977
[7]: https://arxiv.org/pdf/2412.01977
[8]: /html/2412.01979
