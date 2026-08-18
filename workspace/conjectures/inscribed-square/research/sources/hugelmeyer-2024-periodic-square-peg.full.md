<!-- source: https://ar5iv.labs.arxiv.org/html/2407.20412 | converted from HTML -->

[2407.20412] A solution to the periodic square peg problem

# A solution to the periodic square peg problem

Cole Hugelmeyer

###### Abstract.

We resolve the periodic square peg problem using a simple Lagrangian Floer homology argument. Inscribed squares are interpreted as intersections between two non-displaceable Lagrangian sub-manifolds of a symplectic 4-torus.

## 1. Introduction

The Toeplitz square peg conjecture is the long-standing open problem of whether every planar Jordan curve has an inscribed square [7] [4]. Much recent progress has been made on this problem and its variants through the use of symplectic geometry [2] [3] [5] [6]. In this paper, we utilize this approach to solve the periodic square peg conjecture, discussed by Tao in [8].

We prove the following.

###### Theorem 1 (Periodic Square Peg Problem).

Suppose f f and g g are injective continuous functions ℝ → ℝ 2 \mathbb{R}\to\mathbb{R}^{2} with disjoint images, satisfying f ⁡ ( x + 1) = f ⁡ ( x) + ( 0, 1) f(x+1)=f(x)+(0,1) and g ⁡ ( x + 1) = g ⁡ ( x) + ( 0, 1) g(x+1)=g(x)+(0,1) for all x ∈ ℝ x\in\mathbb{R}. Then there exists a set of four distinct points in im ​ ( f) ∪ im ​ ( g) \text{im}(f)\cup\text{im}(g) that form the corners of a square in the plane.

In particular, we will prove the following result, from which the above theorem is a corollary.

###### Theorem 2.

Let f f and g g be smooth embeddings S 1 → ℂ / ℤ ⁡ [i] S^{1}\to\mathbb{C}/\mathbb{Z}[i], both isotopic to the circle ℝ / ℤ \mathbb{R}/\mathbb{Z} and with disjoint images. Then there exist a 1, a 2, b 1, b 2 a_{1},a_{2},b_{1},b_{2} in S 1 S^{1} such that f ⁡ ( a 2) = f ⁡ ( a 1) + i ⋅ ( g ⁡ ( b 1) − f ⁡ ( a 1)) f(a_{2})=f(a_{1})+i\cdot(g(b_{1})-f(a_{1})) and g ⁡ ( b 2) = g ⁡ ( b 1) + i ⋅ ( g ⁡ ( b 1) − f ⁡ ( a 1)) g(b_{2})=g(b_{1})+i\cdot(g(b_{1})-f(a_{1})).

## 2. The symplectic setup

Let ω \omega denote the symplectic area form on ℂ / ℤ ⁡ [i] \mathbb{C}/\mathbb{Z}[i] that is induced by the standard symplectic form on ℂ \mathbb{C}. We then define a symplectic form on ( ℂ / ℤ ⁡ [i]) 2 (\mathbb{C}/\mathbb{Z}[i])^{2} by the formula ω ± = π 1 ∗ ​ ω − π 2 ∗ ​ ω \omega_{\pm}=\pi_{1}^{*}\omega-\pi_{2}^{*}\omega, where π 1 \pi_{1} and π 2 \pi_{2} are the projections onto the first and second coordinates respectively.

Now, we let τ: ( ( ℂ / ℤ ⁡ [i]) 2, ω ±) → ( ( ℂ / ℤ ⁡ [i]) 2, ω ±) \tau:((\mathbb{C}/\mathbb{Z}[i])^{2},\omega_{\pm})\to((\mathbb{C}/\mathbb{Z}[i])^{2},\omega_{\pm}) be given by the formula

 | τ ⁡ ( a, b) = ( a + i ⁡ ( b − a), b + i ⁡ ( b − a)). \tau(a,b)=(a+i(b-a),b+i(b-a)). |  |

We see that this map is a symplectomorphism, because

 | τ ∗ ​ ω ± = | 1 − i | 2 ​ π 1 ∗ ​ ω + | i | 2 ​ π 2 ∗ ​ ω − ( | 1 + i | 2 ​ π 2 ∗ ​ ω + | − i | 2 ​ π 1 ∗ ​ ω) = π 1 ∗ ​ ω − π 2 ∗ ​ ω = ω ±. \tau^{*}\omega_{\pm}=|1-i|^{2}\pi_{1}^{*}\omega+|i|^{2}\pi_{2}^{*}\omega-(|1+i|^{2}\pi_{2}^{*}\omega+|-i|^{2}\pi_{1}^{*}\omega)=\pi_{1}^{*}\omega-\pi_{2}^{*}\omega=\omega_{\pm}. |  |

Furthermore, if f f and g g are smooth embeddings S 1 → ℂ / ℤ ⁡ [i] S^{1}\to\mathbb{C}/\mathbb{Z}[i], then we have a Lagrangian sub-manifold f × g: S 1 × S 1 → ( ℂ / ℤ ⁡ [i]) 2 f\times g:S^{1}\times S^{1}\to(\mathbb{C}/\mathbb{Z}[i])^{2}. We then see that the set of 4-tuples ( a 1, a 2, b 1, b 2) (a_{1},a_{2},b_{1},b_{2}) of points in S 1 S^{1} such that f ⁡ ( a 2) = f ⁡ ( a 1) + i ⋅ ( g ⁡ ( b 1) − f ⁡ ( a 1)) f(a_{2})=f(a_{1})+i\cdot(g(b_{1})-f(a_{1})) and g ⁡ ( b 2) = g ⁡ ( b 1) + i ⋅ ( g ⁡ ( b 1) − f ⁡ ( a 1)) g(b_{2})=g(b_{1})+i\cdot(g(b_{1})-f(a_{1})), is in bijective correspondence with the intersection between the Lagrangian sub-manifolds f × g f\times g and τ ⁡ ( f × g) \tau(f\times g). We will utilize an abuse of notation where f × g f\times g represents a map, but also the torus it parameterizes.

Viewing the symplectic manifold ( ( ℂ / ℤ ⁡ [i]) 2, ω ±) ((\mathbb{C}/\mathbb{Z}[i])^{2},\omega_{\pm}) as the Cartesian product ℂ / ℤ ⁡ [i] × ℂ / ℤ ⁡ [i] ¯ \mathbb{C}/\mathbb{Z}[i]\times\overline{\mathbb{C}/\mathbb{Z}[i]}, we see that we can induce a Hamiltonian isotopy of f × g f\times g by choosing a Hamiltionian isotopy for f f and for g g within ℂ / ℤ ⁡ [i] \mathbb{C}/\mathbb{Z}[i]. Thus, we see that if f f and g g have disjoint images, then the Lagrangian sub-manifold f × g f\times g is Hamiltonian isotopic to f 0 × g 0 f_{0}\times g_{0}, where f 0 ​ ( t) = t + α ​ i f_{0}(t)=t+\alpha i and g 0 ​ ( t) = t + β ​ i g_{0}(t)=t+\beta i for some choice of α \alpha and β \beta in ℝ / ℤ \mathbb{R}/\mathbb{Z} with α ≠ β \alpha\neq\beta. Applying our symplectomorphism τ \tau, we have that τ ⁡ ( f × g) \tau(f\times g) is Hamiltonian isotopic to τ ⁡ ( f 0 × g 0) \tau(f_{0}\times g_{0}).

Therefore, to prove Theorem 2, it suffices to prove the following lemma.

###### Lemma 1.

Let f 0 ​ ( t) = t + α ​ i f_{0}(t)=t+\alpha i and g 0 ​ ( t) = t + β ​ i g_{0}(t)=t+\beta i for some choice of α \alpha and β \beta in ℝ / ℤ \mathbb{R}/\mathbb{Z}. Then the Lagrangian sub-manifolds f 0 × g 0 f_{0}\times g_{0} and τ ⁡ ( f 0 × g 0) \tau(f_{0}\times g_{0}) are non-displaceable.

###### Proof.

There is a 4-fold covering map c: ( ℂ / ℤ ⁡ [i]) 2 → ( ℂ / ℤ ⁡ [i]) 2 c:(\mathbb{C}/\mathbb{Z}[i])^{2}\to(\mathbb{C}/\mathbb{Z}[i])^{2} given by c ⁡ ( x, y) = ( x + y ¯, x ¯ − y) c(x,y)=(x+\overline{y},\overline{x}-y). Deck transformations come from translating by 1 / 2 1/2, i / 2 i/2, or ( 1 + i) / 2 (1+i)/2 in both coordinates. Given f 0 ​ ( t) = t + α ​ i f_{0}(t)=t+\alpha i and g 0 ​ ( t) = t + β ​ i g_{0}(t)=t+\beta i, we choose μ ∈ ℝ / ℤ \mu\in\mathbb{R}/\mathbb{Z} so that μ + μ = α − β \mu+\mu=\alpha-\beta, and we let δ = α − μ \delta=\alpha-\mu. Then, we define maps m, p, q: S 1 → ℂ / ℤ ⁡ [i] m,p,q:S^{1}\to\mathbb{C}/\mathbb{Z}[i] given by m ⁡ ( t) = t + μ ​ i m(t)=t+\mu i and p ⁡ ( t) = t − δ ​ i p(t)=t-\delta i and q ⁡ ( t) = ( 1 + 2 ​ i) ​ t − δ ​ i q(t)=(1+2i)t-\delta i. Then mapped under c c, we have that m × p m\times p double covers f 0 × g 0 f_{0}\times g_{0}, and m × q m\times q double covers τ ⁡ ( f 0 × g 0) \tau(f_{0}\times g_{0}). Furthermore, we have that c ∗ ​ ( ω ±) = 4 ​ ω ± c^{*}(\omega_{\pm})=4\omega_{\pm}. Since a Hamiltonian isotopy in the base space will induce a Hamiltonian isotopy in the covering space, we see that it suffices to prove that m × p m\times p and m × q m\times q are non-displaceable in ( ( ℂ / ℤ ⁡ [i]) 2, ω ±) ((\mathbb{C}/\mathbb{Z}[i])^{2},\omega_{\pm}). In this situation, Floer homology is unobstructed because π 2 ​ ( ( ℂ / ℤ ⁡ [i]) 2) \pi_{2}((\mathbb{C}/\mathbb{Z}[i])^{2}), π 2 ​ ( ( ℂ / ℤ ⁡ [i]) 2, m × p) \pi_{2}((\mathbb{C}/\mathbb{Z}[i])^{2},m\times p), and π 2 ​ ( ( ℂ / ℤ ⁡ [i]) 2, m × q) \pi_{2}((\mathbb{C}/\mathbb{Z}[i])^{2},m\times q) are all trivial [1]. Furthermore, due to the product structure, we can compute the Lagrangian intersection Floer homology of these sub-manifolds by reducing to a computation of the Lagrangian Floer homology of circles within the constituent 2-tori. We have

 | dim ( H ​ F ​ ( m × p, m × q, Λ)) = dim ( H ​ F ​ ( m, m, Λ)) ⋅ dim ( H ​ F ​ ( p, q, Λ)) = 2 ∗ 2 = 4. \dim(HF(m\times p,m\times q;\Lambda))=\dim(HF(m,m;\Lambda))\cdot\dim(HF(p,q;\Lambda))=2*2=4. |  |

Where Λ \Lambda is the Novikov field. Therefore, m × p m\times p and m × q m\times q are non-displaceable, so f 0 × g 0 f_{0}\times g_{0} and τ ⁡ ( f 0 × g 0) \tau(f_{0}\times g_{0}) are also non-displaceable. ∎

Now that we have Lemma 1, Theorem 2 follows from the prior remarks.

## 3. proving the final result

All that remains is to show that Theorem 2 implies Theorem 1.

###### Proof of Theorem 1.

Let f f and g g be as in the statement of Theorem 1. Let f 1, f 2, … f_{1},f_{2},... and g 1, g 2, … g_{1},g_{2},... be sequences of periodic smooth embeddings that limit in the C 0 C^{0} topology to f f and g g respectively, such that f n f_{n} and g n g_{n} have disjoint images for all n n. Then, let λ \lambda be such that [− λ, λ] × ℝ [-\lambda,\lambda]\times\mathbb{R} contains im ​ ( f n) \text{im}(f_{n}) and im ​ ( g n) \text{im}(g_{n}) for all n n, and let ε = inf x ∈ ℝ, y ∈ ℝ, n ∈ ℤ > 0 d ⁡ ( f n ​ ( x), g n ​ ( y)) \varepsilon=\inf_{x\in\mathbb{R},y\in\mathbb{R},n\in\mathbb{Z}_{>0}}d(f_{n}(x),g_{n}(y)) be a lower bound for the distance between the images of the f f and g g functions. Let N N be an integer greater than 16 ​ λ 16\lambda. Then, applying Theorem 2 to the pair f ~ n ​ ( t) = 1 N ​ f n ​ ( N ​ t) + ℤ ⁡ [i] \tilde{f}_{n}(t)=\frac{1}{N}f_{n}(Nt)+\mathbb{Z}[i] and g ~ n ​ ( t) = 1 N ​ g n ​ ( N ​ t) + ℤ ⁡ [i] \tilde{g}_{n}(t)=\frac{1}{N}g_{n}(Nt)+\mathbb{Z}[i], we get a 1, a 2, b 1, b 2 a_{1},a_{2},b_{1},b_{2} such that f ~ n ​ ( a 2) = f ~ n ​ ( a 1) + i ⋅ ( g ~ n ​ ( b 1) − f ~ n ​ ( a 1)) \tilde{f}_{n}(a_{2})=\tilde{f}_{n}(a_{1})+i\cdot(\tilde{g}_{n}(b_{1})-\tilde{f}_{n}(a_{1})) and g ~ n ​ ( b 2) = g ~ n ​ ( b 1) + i ⋅ ( g ~ n ​ ( b 1) − f ~ n ​ ( a 1)) \tilde{g}_{n}(b_{2})=\tilde{g}_{n}(b_{1})+i\cdot(\tilde{g}_{n}(b_{1})-\tilde{f}_{n}(a_{1})). Since im ​ ( f ~ n) \text{im}(\tilde{f}_{n}) and im ​ ( g ~ n) \text{im}(\tilde{g}_{n}) live in a strip of radius 1 / 16 1/16 around ℝ / ℤ \mathbb{R}/\mathbb{Z}, we can choose planar representatives of f ~ n ​ ( a 1), f ~ n ​ ( a 2), g ~ n ​ ( b 1), \tilde{f}_{n}(a_{1}),\tilde{f}_{n}(a_{2}),\tilde{g}_{n}(b_{1}), and g ~ n ​ ( b 2) \tilde{g}_{n}(b_{2}) that live on 1 N ​ im ​ ( f n) ∪ 1 N ​ im ​ ( g n) \frac{1}{N}\text{im}(f_{n})\cup\frac{1}{N}\text{im}(g_{n}) and are all within distance 1 / 4 1/4 of each other, and which therefore form a square in the plane. This gives us an inscribed square on im ​ ( f n) ∪ im ​ ( g n) \text{im}(f_{n})\cup\text{im}(g_{n}) of side length at least ε \varepsilon. We can also assume that this square lives within [− N, N] × [− N, N] [-N,N]\times[-N,N]. Thus, we can apply compactness to find a sequence of inscribed squares on im ​ ( f n) ∪ im ​ ( g n) \text{im}(f_{n})\cup\text{im}(g_{n}) that converge to an inscribed square on im ​ ( f) ∪ im ​ ( g) \text{im}(f)\cup\text{im}(g). The lower bound on side length guarantees that the resulting square is nondegenerate. This completes the proof. ∎

## References

- [1] Kenji Fukaya, Yong-Geun Oh, Hiroshi Ohta, and Kaoru Ono. Lagrangian intersection Floer theory: anomaly and obstruction. Part I, volume 46.1 of AMS/IP Studies in Advanced Mathematics. American Mathematical Society, Providence, RI; International Press, Somerville, MA, 2009.
- [2] Joshua Evan Greene and Andrew Lobb. The rectangular peg problem. Ann. of Math. (2), 194(2):509–517, 2021.
- [3] Joshua Evan Greene and Andrew Lobb. Cyclic quadrilaterals and smooth Jordan curves. Invent. Math., 234(3):931–935, 2023.
- [4] H. B. Griffiths. The topology of square pegs in round holes. Proc. London Math. Soc. (3), 62(3):647–672, 1991.
- [5] Andrew Lobb Joshua Greene. Floer homology and square pegs. arXiv:2404.05179 [math.SG], 2024.
- [6] Andrew Lobb Joshua Greene. Square pegs between two graphs. arXiv:2407.07798 [math.SG], 2024.
- [7] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc., 61(4):346–352, 2014.
- [8] Terence Tao. An integration approach to the Toeplitz square peg problem. Forum Math. Sigma, 5:Paper No. e30, 63, 2017.

*

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2407.20411
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2407.20412
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2407.20412
[7]: https://arxiv.org/pdf/2407.20412
[8]: /html/2407.20413
