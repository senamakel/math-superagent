<!-- source: https://ar5iv.labs.arxiv.org/html/2303.17711 | converted from HTML -->

[2303.17711] When does the Table Theorem imply a solution to the Square Peg Problem?

# When does the Table Theorem imply a solution to the Square Peg Problem?

Stefan Friedl and Kenan Ince

###### Abstract.

We will explain the relationship between one of the most beautiful theorems in topology, namely Fenn’s Table Theorem, and one of the most famous open problems in topology, namely the Square Peg Problem.

## 1. Introduction

To introduce the Square Peg Problem, we need the following definition:

###### Definition 1.1.

The image of an injective continuous map S 1 → ℝ 2 S^{1}\to\mathbb{R}^{2} is called a *Jordan curve*. Given a Jordan curve C C, we say that a rectangle R R is *inscribed in C C*if all vertices of R R lie on C C.

The following problem was first stated by Otto Toeplitz [To1911] in 1911.

###### Problem 1.2.

(Square Peg Problem) Does every Jordan curve admit an inscribed square of side length > 0 >0?

This problem, and interesting variations thereof, have fascinated mathematicians ever since it was formulated. Many partial results have been obtained. For example it is known that it is possible to inscribe a rectangle in every Jordan curve [Me1982], and Lev Schnirelmann [Sc1944] showed it is always possible to inscribe a square if the Jordan curve is C 2 C^{2}, but the general case of the problem is open. A discussion of the question and its history is given in [Ma2014] and [GL2021].

The following theorem was first formulated and proven by Roger Fenn [Fe1970] in 1970 1970. (An alternative write up of the proof is given in [Fr2023, Chapter 133.1].)

###### Theorem 1.3.

*(Table Theorem)*Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be a compact convex non-empty subset. Let f: ℝ 2 → ℝ f\colon\mathbb{R}^{2}\to\mathbb{R} be a continuous map so that f ⁡ ( x) ≥ 0 f(x)\geq 0 for all x ∈ D x\in D and such that f ⁡ ( x) = 0 f(x)=0 for all x ∉ D x\notin D. Let s > 0 s>0 be a real number. Then there exist four points a 1, a 2, a 3, a 4 ∈ ℝ 2 a_{1},a_{2},a_{3},a_{4}\in\mathbb{R}^{2} with the following properties:

1. (1)

the points form a square of side length s s,

2. (2)

the center of the square lies in D D,

3. (3)

we have f ⁡ ( a 1) = f ⁡ ( a 2) = f ⁡ ( a 3) = f ⁡ ( a 4) f(a_{1})=f(a_{2})=f(a_{3})=f(a_{4}).

Figure 1.1. Illustration of the Table Theorem.

In other words, the Table Theorem says that any given square table can be placed on the “ground” defined by the graph of f f such that all four legs of the table lie on the ground, the table is horizontal, and the center of the tabletop lies in D D.

It has been known for a long time that the Table Theorem 1.3 has implications for the Square Peg Problem. It was stated somewhat optimistically in [Ma2014, Ta2017] that the Table Theorem 1.3 implies the Square Peg Problem for convex Jordan curves. But to us it seems like that story is more complicated since, as we will see in Section 2, in many cases the Table Theorem has trivial solutions which do not tell us anything interesting. This leads us to the following definition.

###### Definition 1.4.

We say that a subset D D of ℝ 2 = ℂ \mathbb{R}^{2}=\mathbb{C} is *obtuse *if, for any x ∈ ∂ D x\in\partial D, there exists a v ∈ ℝ 2 ∖ { ( 0, 0) } = ℂ ∖ { 0 } v\in\mathbb{R}^{2}\setminus\{(0,0)\}=\mathbb{C}\setminus\{0\} and an angle θ > π 2 \theta>\frac{\pi}{2} such that

 | T v, θ ​ ( x):= { x + r ⋅ e i ​ ϕ ⋅ v: ϕ ∈ [0, θ] ​ and ​ r ∈ [0, 1] } ⊂ D. T_{v,\theta}(x):=\{x+r\cdot e^{i\phi}\cdot v:\phi\in[0,\theta]\text{ and }r\in[0,1]\}\subset D. |  |

Figure 1.2. An obtuse set D D together with a picture of T v, θ ​ ( x) T_{v,\theta}(x).

In this short note we will show in the Main Lemma 2.2 that the Table Theorem 1.3 has a non-trivial solution if and only if D D is obtuse. We will use the Table Theorem 1.3 to give a new proof for the following theorem.

###### Theorem 1.5.

*(Main Theorem)*Let J J be a Jordan curve which is the boundary of a compact convex subset D ⊂ ℝ 2 D\subset\mathbb{R}^{2}. If D D is obtuse, then J J admits an inscribed square.

Note though that the Square Peg Problem 1.2 for convex curves has been known for a long time; in fact, it was proved by K. Zindler [Zi1921] and C. M. Christensen [Chr1950].

## 2. Preliminaries

We return to the context of the Table Theorem. Note that given a compact convex non-empty subset D ⊂ ℝ 2 D\subset\mathbb{R}^{2}, for s s very large, we can simply place the legs of the table outside of D D (in fact, by continuity of f f, outside the interior of D D) while keeping the center of the table in D D, since then f ⁡ ( a 1) = f ⁡ ( a 2) = f ⁡ ( a 3) = f ⁡ ( a 4) = 0 f(a_{1})=f(a_{2})=f(a_{3})=f(a_{4})=0. Motivated by such a “trivial solution” to the Table Theorem, we make the following definition:

###### Definition 2.1.

Let D D be a subset of ℝ 2 \mathbb{R}^{2} and let s ∈ ℝ s\in\mathbb{R}. We say D D is *s s -trivial *if there exists a square in ℝ 2 \mathbb{R}^{2} with side length t ∈ ( 0, s] t\in(0,s] such that the vertices of the square lie outside the interior of D D while the center of the square lies in D D. Otherwise, we say that D D is *s s -nontrivial.*In other words, D D is s s -nontrivial if, for all squares with side length t ∈ ( 0, s] t\in(0,s] with center in D D, at least one vertex of the square lies in the interior of D D.

Note that, by our definition, if D D is s s -trivial for some s s, then certainly D D is s ′ s^{\prime} -trivial for all s ′ > s s^{\prime}>s. Moreover, every non-empty compact set D D is s s -trivial for all sufficiently large s s; for example, one may take s ≥ diam ⁡ ( D) s\geq\operatorname{diam}(D) and center the trivial square of side length s s at any point in D D.

Figure 2.1. Example of a subset D ⊂ ℂ D\subset\mathbb{C} that is s s -trival for all s > 0 s>0.

The following lemma is the main technical result we prove in this note.

###### Lemma 2.2.

*(Main Lemma)*Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be a compact, convex, non-empty set. Then D D is obtuse if and only if D D is s s -nontrivial for some s > 0 s>0.

Thus, Lemma 2.2 is precisely the condition needed for the Table Theorem to imply a *nontrivial*solution to the Square Peg Problem, in the sense that we do not simply make the square huge enough that all of its vertices lie outside of D D.

The next section will be devoted to a proof of the Main Lemma 2.2. In Section 4, we will show that the Main Lemma 2.2 implies Theorem 1.5.

## 3. Proof of the Main Lemma 2.2

###### Definition 3.1.

Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be compact and convex. We consider the function

 | f D: D → ℝ ≥ 0 x ↦ sup { ‖ v ‖: v ∈ ℝ 2 such that there exists a γ > π 2 with T v, γ ​ ( x) ⊂ D }. \begin{array}[]{rcl}f_{D}\colon D&\to&\mathbb{R}_{\geq 0}\\ x&\mapsto&\sup\{\|v\|:\mbox{ $v\in\mathbb{R}^{2}$ such that there exists a $\gamma>\frac{\pi}{2}$ with $T_{v,\gamma}(x)\subset D$}\}.\end{array} |  |

Note that we can always take v = 0 v=0, i.e. we take the supremum over a non-empty set.

###### Lemma 3.2.

Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be compact and convex. The function f D: D → ℝ f_{D}\colon D\to\mathbb{R} defined above is lower semicontinuous. That is, for any x ∈ D x\in D and any ϵ > 0 \epsilon>0, there exists a δ > 0 \delta>0 such that, for all y ∈ D y\in D with ‖ x − y ‖ < δ \|x-y\|<\delta, f D ​ ( y) > f D ​ ( x) − ϵ f_{D}(y)>f_{D}(x)-\epsilon.

###### Proof.

Let x ∈ D x\in D and ϵ > 0 \epsilon>0 be arbitrary. If f D ​ ( x) = 0 f_{D}(x)=0, then there is nothing to show. Thus we can now assume that f D ​ ( x) > 0 f_{D}(x)>0. By the definition of f D f_{D} as a supremum there exists a non-zero vector v ∈ ℝ 2 v\in\mathbb{R}^{2} such that ‖ v ‖ > f D ​ ( x) − ϵ 2 \|v\|>f_{D}(x)-\frac{\epsilon}{2} and an angle γ ∈ ( π 2, π) \gamma\in(\frac{\pi}{2},\pi) with T v, γ ​ ( x) ⊂ D T_{v,\gamma}(x)\subset D.

It suffices to show that there exists δ > 0 \delta>0 such that, for all y ∈ D y\in D with ‖ x − y ‖ < δ \|x-y\|<\delta, we can find a w ∈ ℝ 2 w\in\mathbb{R}^{2} with ‖ w ‖ > f D ​ ( x) − ϵ \|w\|>f_{D}(x)-\epsilon and an angle β ∈ ( π 2, π) \beta\in(\frac{\pi}{2},\pi) with T w, β ​ ( y) ⊂ D T_{w,\beta}(y)\subset D.

We set A:= x + v A:=x+v and B:= x + e i ​ γ ⋅ v B:=x+e^{i\gamma}\cdot v. We consider the map

 | g: D ∖ { A, B } → [0, π] y ↦ ∢ A ​ y ​ B:= arccos ⁡ ( ⟨ A − y, B − y ⟩ ‖ A − y ‖ ⋅ ‖ B − y ‖). \begin{array}[]{rcl}g\colon D\setminus\{A,B\}&\to&[0,\pi]\\ y&\mapsto&\sphericalangle_{AyB}:=\arccos\bigg(\mbox{\small$\displaystyle\frac{\langle A-y,B-y\rangle}{\|A-y\|\cdot\|B-y\|}$}\bigg).\end{array} |  |

It is clear that g g is continuous. Since g ⁡ ( x) = γ > π 2 g(x)=\gamma>\frac{\pi}{2} we see that there exists a μ > 0 \mu>0 such that g ⁡ ( y) > π 2 g(y)>\frac{\pi}{2} for all y ∈ D y\in D with ‖ x − y ‖ < μ \|x-y\|<\mu. We set δ:= min ⁡ { μ, ϵ 2 } \delta:=\operatorname{min}\{\mu,\frac{\epsilon}{2}\}. We claim that δ \delta has the desired property.

Let y ∈ D y\in D with ‖ x − y ‖ < δ \|x-y\|<\delta. We claim that w:= A − y w:=A-y and β:= g ⁡ ( y) \beta:=g(y) have the desired properties. First note that it follows from δ ≤ μ \delta\leq\mu that ∢ A ​ y ​ B = g ⁡ ( y) > π 2 \sphericalangle_{AyB}=g(y)>\frac{\pi}{2}.

By convexity of D D we know that for each φ ∈ [0, γ] \varphi\in[0,\gamma] the segment from y y to z = x + e i ​ φ ⋅ v z=x+e^{i\varphi}\cdot v is contained in D D. Furthermore note that since δ < ϵ 2 \delta<\frac{\epsilon}{2} we see that for each z = x + e i ​ φ ⋅ v z=x+e^{i\varphi}\cdot v we have ‖ z − y ‖ ≥ ‖ z − x ‖ − ‖ y − x ‖ > f D ​ ( x) − ϵ 2 − ϵ 2 = f D ​ ( x) − ϵ \|z-y\|\geq\|z-x\|-\|y-x\|>f_{D}(x)-\frac{\epsilon}{2}-\frac{\epsilon}{2}=f_{D}(x)-\epsilon. It follows from this discussion that T w, β ​ ( y) ⊂ D T_{w,\beta}(y)\subset D. ∎

Figure 3.1. Illustration for the proof of Lemma 3.2.

We now turn to the proof of the Main Lemma 2.2. Thus let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be a compact, convex, non-empty set. We want to show the following:

 | D is obtuse ⟺ D is s -nontrivial for some s > 0. \mbox{$D$ is obtuse}\quad\Longleftrightarrow\quad\begin{array}[]{c}\mbox{$D$ is $s$-nontrivial for some $s>0$.}\end{array} |  |

We prove the two directions separately.

###### Proof of the Main Lemma 2.2 ⟹ \Longrightarrow.

Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be a compact, convex, obtuse, non-empty set. We need to show that there exists a real number s > 0 s>0 such that D D is s s -nontrivial. We continue with the above notation; in particular, we consider the function f D: D → ℝ f_{D}\colon D\to\mathbb{R}. Note that for any x x in the interior of D D we evidently have f D ​ ( x) > 0 f_{D}(x)>0. Furthermore note that it follows from the fact that D D is obtuse that for any x ∈ ∂ D x\in\partial D we also have f D ​ ( x) > 0 f_{D}(x)>0. In summary we have shown that f D: D → ℝ ≥ 0 f_{D}\colon D\to\mathbb{R}_{\geq 0} is non-zero everywhere. Recall that every lower semicontinuous function on a non-empty compact subset achieves a global minimum (see e.g. [Cho1966, Theorem II.10.1]). Thus it follows from Lemma 3.2 that f D: D → ℝ f_{D}\colon D\to\mathbb{R} achieves a global minimum. Denote

 | s:= min ⁡ { f D ​ ( x): x ∈ D }. s:=\min\{f_{D}(x):x\in D\}. |  |

As we mentioned above, f D f_{D} is non-zero everywhere, thus we see that s > 0 s>0.

We claim that D D is s s -nontrivial. Let x ∈ D x\in D. We need to show that every square centered at x x of side length ≤ s \leq s has least one vertex lying in int ⁡ ( D) \operatorname{int}(D).

By definition of f D f_{D} and by definition of a supremum, we know that there exists a v ∈ ℝ 2 v\in\mathbb{R}^{2} with length v > 1 2 ⋅ f D ​ ( x) v>\frac{1}{\sqrt{2}}\cdot f_{D}(x) and a β > π 2 \beta>\frac{\pi}{2} such that T ( v, β) ​ ( x) ⊂ D T_{(v,\beta)}(x)\subset D. Since β > π 2 \beta>\frac{\pi}{2}, it follows from elementary geometry that any square centered at x x with side length ≤ 2 ⋅ ‖ v ‖ \leq\sqrt{2}\cdot\|v\| contains a vertex in int ⁡ ( T ( v, β) ​ ( x)) \operatorname{int}(T_{(v,\beta)}(x)). Since 2 ⋅ ‖ v ‖ ≥ f D ​ ( x) ≥ s \sqrt{2}\cdot\|v\|\geq f_{D}(x)\geq s, we see that any square centered at x x of side length ≤ s \leq s admits at least one vertex that lies in int ⁡ ( D) \operatorname{int}(D).

∎

###### Proof of the Main Lemma 2.2 ⟸ \Longleftarrow.

Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be a compact, convex set. We need to show that if D D is non-obtuse, then the subset D D is s s -trivial for all s > 0 s>0.

Thus we assume that D D is non-obtuse. Recall that this means that there exists an x ∈ ∂ D x\in\partial D such that for all v ≠ 0 v\neq 0 and all θ > π 2 \theta>\frac{\pi}{2} we have T v, θ ​ ( x) ⊄ D T_{v,\theta}(x)\not\subset D. After a translation we can assume, without loss of generality, that x = 0 x=0.

Let s > 0 s>0. We need to show that D D is s s -trivial. It suffices to show that there exists a square in ℝ 2 \mathbb{R}^{2} with the following properties:

1. (1)

The center of the square is x = 0 x=0.

2. (2)

The distance from x x to the four vertices equals d:= 1 2 ​ s d:=\frac{1}{\sqrt{2}}s. (Which implies that the side length is s s.)

3. (3)

All four vertices lie outside of the interior of D D.

We set

 | B:= { v ∈ S 1 | ℝ > 0 ⋅ v ∩ D ≠ ∅ }. B:=\{v\in S^{1}\,|\,\mathbb{R}_{>0}\cdot v\cap D\neq\emptyset\}. |  |

Figure 3.2. A depiction of a non-obtuse set D D together with the corresponding set B B.

If B B consists of just two opposite points v, − v v,-v, then the desired square is given by the vertices v ⋅ e i ⁡ ( π / 4 + k ⋅ π / 2) v\cdot e^{i(\pi/4+k\cdot\pi/2)}, k = 0, 1, 2, 3 k=0,1,2,3. Thus in the following we will assume that B B does not just consist of two opposite points.

###### Claim 3.3.

The subset B ⊂ S 1 B\subset S^{1} is path-connected.

Let v ≠ w ∈ B v\neq w\in B. We need to show that v v and w w are connected by a path in B B. First we consider the case that v ≠ − w v\neq-w. We pick r > 0, s > 0 r>0,s>0 such that r ⋅ v, s ⋅ w ∈ D r\cdot v,s\cdot w\in D. We set v ~:= r ⋅ v \tilde{v}:=r\cdot v and w ~:= s ⋅ w \tilde{w}:=s\cdot w. We consider the triangle formed by 0, v ~, w ~ 0,\tilde{v},\tilde{w}. By convexity of D D this triangle is contained in D D. This implies that all points of the form

 | v ~ ⋅ ( 1 − t) + w ~ ⋅ t ‖ v ~ ⋅ ( 1 − t) + w ~ ⋅ t ‖ \frac{\tilde{v}\cdot(1-t)+\tilde{w}\cdot t}{\|\tilde{v}\cdot(1-t)+\tilde{w}\cdot t\|} |  |

are contained in B B. (The fact that v ≠ − w v\neq-w implies that v ~ ⋅ ( 1 − t) + w ~ ⋅ t ≠ 0 \tilde{v}\cdot(1-t)+\tilde{w}\cdot t\neq 0 for all t ∈ [0, 1] t\in[0,1].) Thus v v and w w are connected by a path in B B.

Now assume that v = − w v=-w. It follows from the discussion preceding the claim that there exists a u ∈ B u\in B with u ≠ { v, − w } u\neq\{v,-w\}. But by the above we can connect v v to u u by a path in B B and we can connect u u to w w by a path in B B. Thus we can connect v v to w w by a path in B B. This concludes the proof of the claim.

Since B ⊂ S 1 B\subset S^{1} is connected, there exists an interval I ⊂ ℝ I\subset\mathbb{R} of length ≤ 2 ​ π \leq 2\pi such that

 | B = { e i ​ t | t ∈ I }. B=\{e^{it}\,|\,t\in I\}. |  |

We set φ:= inf ⁡ ( I) \varphi:=\operatorname{inf}(I) and ψ:= sup ⁡ ( I) \psi:=\operatorname{sup}(I).

###### Claim 3.4.

We have ψ − φ ≤ π 2 \psi-\varphi\leq\frac{\pi}{2}.

Suppose that ψ − φ > π 2 \psi-\varphi>\frac{\pi}{2}. We pick φ ′, ψ ′ \varphi^{\prime},\psi^{\prime} with φ < φ ′ < ψ ′ < ψ \varphi<\varphi^{\prime}<\psi^{\prime}<\psi and such that ψ ′ − φ ′ ∈ ( π 2, π) \psi^{\prime}-\varphi^{\prime}\in(\frac{\pi}{2},\pi). By definition of supremum and infimum, and since I I is an interval, we know that φ ′, ψ ′ ∈ I \varphi^{\prime},\psi^{\prime}\in I, which implies that e i ​ φ ′, e i ​ ψ ′ ∈ B e^{i\varphi^{\prime}},e^{i\psi^{\prime}}\in B, which in turn implies that there exist r > 0 r>0 and s > 0 s>0 such that r ⋅ e i ​ φ ′ ∈ D r\cdot e^{i\varphi^{\prime}}\in D and s ⋅ e i ​ ψ ′ ∈ D s\cdot e^{i\psi^{\prime}}\in D. By convexity of D D, the triangle given by 0, r ⋅ e i ​ φ ′, s ⋅ e i ​ ψ ′ 0,r\cdot e^{i\varphi^{\prime}},s\cdot e^{i\psi^{\prime}} is contained in D D. An elementary geometric argument now shows that there exists a λ > 0 \lambda>0 such that T λ ​ e i ​ φ ′, ψ ′ − φ ′ ​ ( 0) ⊂ D T_{\lambda e^{i\varphi^{\prime}},\psi^{\prime}-\varphi^{\prime}}(0)\subset D. Since ψ ′ − φ ′ > 0 \psi^{\prime}-\varphi^{\prime}>0, this contradicts our choice of x x. This concludes the proof of the claim.

Now we consider the square that is given by the vertices d ⋅ e i ⁡ ( φ + k ⋅ π 2) d\cdot e^{i(\varphi+k\cdot\frac{\pi}{2})}, k = 0, 1, 2, 3 k=0,1,2,3. It is clear that (1) and (2) are satisfied. Thus it remains to prove the following claim.

###### Claim 3.5.

All four vertices lie outside of the interior of D D.

We start out with an observation: if r ⋅ e i ​ β r\cdot e^{i\beta} lies in the interior of D D then, since the interior of D D is open, there exists an ϵ > 0 \epsilon>0 such that r ⋅ e i ⁡ ( β + σ) ∈ D r\cdot e^{i(\beta+\sigma)}\in D for all σ ∈ ( − ϵ, ϵ) \sigma\in(-\epsilon,\epsilon), which implies that ( β − ϵ, β + ϵ) ⊂ I (\beta-\epsilon,\beta+\epsilon)\subset I. The claim follows from this observation and the definition of infimum and supremum. ∎

## 4. Nontriviality implies a solution to the Square Peg Problem

We can now give a proof of the Main Theorem 1.5. The key idea behind the argument we provide is in principle well-known, see e.g. [Ma2014]. But note that the role of the obtuseness has not been elucidated before.

###### Proof.

Let D ⊂ ℝ 2 D\subset\mathbb{R}^{2} be a compact convex obtuse non-empty subset. We need to show that there exist four points a 1, a 2, a 3, a 4 ∈ ∂ D a_{1},a_{2},a_{3},a_{4}\in\partial D which form a square of side length > 0 >0. After a translation we can assume that the origin 0 0 is contained in the interior of D D. Given x ∈ D ∖ { 0 } x\in D\setminus\{0\} we set

 | ρ ⁡ ( x):= sup { ‖ r ⋅ x ‖ | r ∈ ℝ > 0 ​ and ​ r ⋅ x ∈ D } ∈ ℝ > 0. \rho(x)\,\,:=\,\,\sup\big\{\|r\cdot x\|\,\big|\,r\in\mathbb{R}_{>0}\mbox{ and }r\cdot x\in D\big\}\,\,\in\,\mathbb{R}_{>0}. |  |

It follows from an elementary argument, see e.g. [Be2009, Chapter 11.3], that ρ \rho is continuous. We consider the map

 | f: ℝ 2 → [0, 1] x ↦ { 1 − ‖ x ‖ ⋅ 1 ρ ⁡ ( x), if ​ x ∈ D ∖ { 0 }, 1, if ​ x = 0, 0, if ​ x ∉ D. \begin{array}[]{rcl}f\colon\mathbb{R}^{2}&\to&[0,1]\\ x&\mapsto&\left\{\begin{array}[]{ll}1-\|x\|\cdot\mbox{\large$\frac{1}{\rho(x)}$},&\mbox{ if }x\in D\setminus\{0\},\\ 1,&\mbox{ if }x=0,\\ 0,&\mbox{ if }x\not\in D.\end{array}\right.\end{array} |  |

Since ρ \rho is continuous one can easily verify that f f is continuous. Since D D is obtuse we obtain from the Main Lemma 2.2 that there exists a d > 0 d>0 such that D D is d d -non trivial. By the Table Theorem 1.3 there exist four points b 1, b 2, b 3, b 4 ∈ ℝ 2 b_{1},b_{2},b_{3},b_{4}\in\mathbb{R}^{2} with the following properties:

1. (1)

the points form a square of side length d d,

2. (2)

the center of the square lies in D D,

3. (3)

we have f ⁡ ( b 1) = f ⁡ ( b 2) = f ⁡ ( b 3) = f ⁡ ( b 4) f(b_{1})=f(b_{2})=f(b_{3})=f(b_{4}).

Since D D is d d -non trivial, we see that at least one vertex lies in the interior of D D. But since f f is non-zero on the interior of D D, we see that the common f f -value, let’s call it y y, lies in the open interval ( 0, 1) (0,1). It follows immediately from the definition of f f that the four points b 1, b 2, b 3, b 4 b_{1},b_{2},b_{3},b_{4} lie on the subset ( 1 − y) ⋅ ∂ D (1-y)\cdot\partial D. In other words, if we multiply these four points by 1 1 − y \frac{1}{1-y}, then we obtain the desired four points a 1, a 2, a 3, a 4 a_{1},a_{2},a_{3},a_{4} on ∂ D \partial D. ∎

###### Acknowledgement.

The first author was supported by the CRC 1085 “Higher Invariants” at the University of Regensburg. The second author would like to acknowledge the Westminster College Gore Individual Summer Grant and the University of Regensburg for funding to support this collaboration.

## References

- [Be2009] M. Berger. Geometry. I., Universitext, Springer Verlag (2009).
- [Cho1966] G. Choquet. Topology, Pure and Applied Mathematics. A Series of Monographs and Textbooks 19. New York and London: Academic Press (1966).
- [Chr1950] C. M. Christensen. A square inscribed in a convex figure, Matematisk Tidsskrift B 1950 (1950), 22–26.
- [Fe1970] R. Fenn. The table theorem, Bull. Lond. Math. Soc. 2 (1970), 73–76.
- [Fr2023] S. Friedl. Topology, lecture notes, University of Regensburg
[https://friedl.app.uni-regensburg.de/][1]
- [GL2021] J. Greene and A. Lobb. The rectangular peg problem, Ann. Math. (2) 194, No. 2 (2021), 509–517.
- [Ma2014] B. Matschke. A survey on the square peg problem, Notices Am. Math. Soc. 61, No. 4 (2014), 346–352.
- [Me1982] M. Meyerson. Balancing acts. Topology, Proc. Conf., Vol. 6, No.1, Blacksburg/Va. 1981 (1982), 59–75.
- [Ta2017] T. Tao. An integration approach to the Toeplitz square peg problem, Forum Math. Sigma 5, Paper No. e30, 63 p. (2017).
- [Sc1944] L. G. Schnirelman. On some geometric properties of closed curves, Usp. Mat. Nauk 10 (1944), 34–44.
- [To1911] O. Toeplitz. Über einige Aufgaben der Analysis situs, Verhandlungen der Schweizerischen Naturforschenden Gesellschaft in Solothurn 4 (1911), 197.
- [Zi1921] K. Zindler. Über konvexe Gebilde, Monatshefte f ür Mathematik und Physik 31 (1921), 25–56.

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: https://friedl.app.uni-regensburg.de/
[2]: /html/2303.17710
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/2303.17711
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2303.17711
[8]: https://arxiv.org/pdf/2303.17711
[9]: /html/2303.17712
