<!-- source: https://arxiv.org/html/2607.13785v2 | converted from HTML -->

Local Uniform Finite Cyclicity of the H 14 3 Semihyperbolic Hemicycle

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2607.13785v2 [math.DS] 17 Jul 2026

# Local Uniform Finite Cyclicity of the H 14 3 H_{14}^{3} Semihyperbolic Hemicycle

Haibo Lu Affiliation: Shanghai Institute of Technology Email: [luhaibo1985@gmail.com][3]

###### Abstract

We prove local uniform finite cyclicity for the labelled H 14 3 H_{14}^{3} semihyperbolic hemicycle of a quadratic vector field. More precisely, in one fixed annular neighborhood of the compactified graphic, the number of isolated limit cycles is uniformly bounded for all sufficiently small values of the full five-parameter source-normalized quotient unfolding. This is the case left open in the corresponding quadratic-hemicycle analysis because a noncompact source, two semihyperbolic endpoints, and an upper-equatorial degeneration occur simultaneously. The proof constructs a finite atlas of stopped first hits before forming any full-lap return. An intersection argument represents each counted cycle by exactly one retained itinerary. The resulting analytic equations are treated by a matched source estimate, a direct Liénard–Dulac argument on the exact mixed face, and hyperbolic, central, strict-lips, middle, and root-scale zero theorems on the remaining regimes. A finite specialization argument includes coefficient, boundary, collapse, and identity values. The distinctive point is that all estimates remain uniform in the five original parameters. The resulting bound is existential.

2020 Mathematics Subject Classification. 34C07, 34C23, 37G15

Keywords. quadratic vector field, limit cycle, finite cyclicity, semihyperbolic hemicycle, saddle-node, Hilbert’s sixteenth problem

## Part I Geometry, exhaustive classification, and proof of the main theorem

### 1 Introduction

The local form of Hilbert’s sixteenth problem asks for uniform control of the limit cycles born near a fixed graphic in a finite-parameter family of planar vector fields. Even for quadratic systems, compactification can place several different singular mechanisms on the same boundary graphic. The graphic studied here is a particularly sharp instance: a noncompact period annulus meets two semihyperbolic horizontal endpoints and a degenerate upper vertical point.

The starting example is the source-normalized field

 | X 0: x ˙ = − y, y ˙ = x + x ​ y. X_{0}:\qquad\dot{x}=-y,\qquad\dot{y}=x+xy. |  | (1.1) |

On the half-plane y > − 1 y>-1 it has the first integral

 | H ⁡ ( x, y) = x 2 2 + y − log ⁡ ( 1 + y). H(x,y)=\frac{x^{2}}{2}+y-\log(1+y). |  | (1.2) |

Its regular positive levels form the period annulus around the origin. Their outer compactified limit is the labelled set Γ H ​ 14 3 \Gamma_{H14^{3}}, consisting of the finite invariant line y = − 1 y=-1, two horizontal points at infinity, the oriented upper equatorial arcs, and the positive vertical point at infinity. The labels and orientation specify the graphic throughout the paper.

The unfolding studied here is

 | x ˙ = − y + B ​ x 2 + μ 2 ​ y 2 + ( μ 4 + B ​ μ 5) ​ x, y ˙ = x + x ​ y + μ 3 ​ y 2 + ( 1 − 2 ​ B) ​ μ 5 ​ y, λ = ( B, μ 2, μ 3, μ 4, μ 5). \begin{aligned} \dot{x}&=-y+Bx^{2}+\mu_{2}y^{2}+(\mu_{4}+B\mu_{5})x,\\ \dot{y}&=x+xy+\mu_{3}y^{2}+(1-2B)\mu_{5}y,\end{aligned}\qquad\lambda=(B,\mu_{2},\mu_{3},\mu_{4},\mu_{5}). |  | (1.3) |

This is the five-parameter family displayed in Roussarie–Rousseau [4, Theorem 3.1]; in that classification the value B = 0 B=0 is precisely the labelled H 14 3 H_{14}^{3} case. The earlier DRR94 work supplies the quadratic classification program and the nomenclature [1]. We use those references to identify the problem, while all calculations below concern the displayed source-normalized family and the labelled orientation just fixed. All five parameters remain active throughout. Let U U be a fixed, sufficiently small, two-sided annular neighborhood of Γ H ​ 14 3 \Gamma_{H14^{3}} on the Poincaré sphere. For a small parameter value λ \lambda, write N H ​ 14 3 ​ ( λ, U) N_{H14^{3}}(\lambda;U) for the number of isolated limit cycles of ( 1.3) contained in U U.

###### Theorem 1 (Local uniform finite cyclicity).

There exist a sufficiently small fixed two-sided annular neighborhood U U of Γ H ​ 14 3 \Gamma_{H14^{3}}, a sufficiently small neighborhood Λ ⊂ ℝ 5 \Lambda\subset\mathbb{R}^{5} of the origin, and a finite constant B H ​ 14 3 B_{H14^{3}} such that

 | N H ​ 14 3 ​ ( λ, U) ≤ B H ​ 14 3 N_{H14^{3}}(\lambda;U)\leq B_{H14^{3}} |  | (1.4) |

for every λ ∈ Λ \lambda\in\Lambda, where the left-hand side counts isolated limit cycles of the full five-parameter source-normalized quotient unfolding ( 1.3) contained in U U.

The theorem is local and nonnumerical: it retains the full five-parameter dependence, counts isolated limit cycles in one fixed geometric collar, and makes no reduction to fewer parameters. It claims no explicit or optimal cyclicity number. No global return map is assumed in advance; its domain is instead produced by the stopped first-hit construction below.

#### 1.1 The three coupled difficulties

At the source, the horizontal endpoints are semihyperbolic and the upper vertical point undergoes a separate resolved degeneration. Under perturbation, the first orbit segment leaving a fixed section may reach a regular next cut, a singular gate, a passive side, or the collar boundary. Thus the existence and domain of a full-lap return cannot be assumed before first-hit geometry is settled. A second difficulty is noncompactness: source-regime fixed points can move toward the boundary of the period annulus while the parameters tend to zero. A third difficulty is the merger of two-central lips regimes with the source and with a persistent endpoint. Pointwise finite cyclicity at a fixed graphic does not by itself give an ambient bound through these coalescing faces.

The proof separates these tasks. Geometry first produces finitely many physical itineraries. Analysis then gives a locally uniform zero theorem in each analytic regime. Only after boundary and identity specializations have been assigned to terminal regimes does compactness supply finitely many numerical bounds. This order turns a finite geometric classification into one uniform number.

#### 1.2 Ideas of the proof and relation to earlier work

Two established analytic tools enter the proof, but neither one supplies the theorem directly. Roussarie–Rousseau explicitly leave the B = 0 B=0 H 14 3 H_{14}^{3} case outside their finite-cyclicity result and identify the two semihyperbolic equatorial points as the additional difficulty [4, pp. 1–4]. Marín and Villadelprat study hemicycles with hyperbolic saddles at infinity [5]. Their 2025 result does not cover the present semihyperbolic graphic. The saddle-node results of Dumortier–Ilyashenko–Rousseau [2] apply only after the actual central or lips graphic, its strong and parabolic connections, and the required boundary incidence have been certified in the physical family. Mourtada’s quasi-regular Hilbert theorem applies only to an analytic all-hyperbolic word after its sections, connectors, Hilbert derivation, integral fibers, and closing germ have been realized on one common positive-corner neighborhood [3]. At Γ H ​ 14 3 \Gamma_{H14^{3}}, the noncompact source return, the semihyperbolic endpoints, and the upper vertical degeneration meet in the same five-parameter problem. The proof must first decide which physical itinerary exists and which analytic regime contains it.

The DRR94 designation supplies the historical classification and the nomenclature; the exact family and the B = 0 B=0 identification used here come from the later statement just cited. Throughout we work with the displayed source-normalized representative, so no coordinate comparison with another printed model is needed. DIR finite-cyclicity and Mourtada’s quasi-regular Hilbert (QRH) results are imported with their stated hypotheses; ordinary analytic coefficient division and Weierstrass preparation control bounded analytic words. The H14-specific work is the physical stopped atlas, the source and coalescing-scale estimates, the two-central exhaustion, and their ambient assembly. Finite derivative and case enumerations in Parts II and III are computer-assisted, while their physical exhaustiveness and every theorem-applicability argument remain part of the mathematical proof.

The paper’s contribution is the mechanism that performs this decision without losing the boundary cases. A fixed physical collar is cut into regular strips and three singular slabs. Stopped first hits give a finite itinerary family, and annular intersection turns every counted cycle into exactly one full-lap fixed point. Each itinerary lies in one theorem neighborhood, including the source and mixed zero-scale faces. A finite specialization induction then treats coefficient, collapse, gate, and identity values. Compactness is used only after these neighborhoods have been constructed.

Part I constructs the stopped atlas, proves the exact-once reduction, exhausts the geometric regimes, and assembles Theorem 1. Part II proves the matched source estimate and the exact mixed persistent-endpoint theorem. Part III proves the hyperbolic, central, strict-lips, middle, and positive-root zero theorems and verifies their applicability. The appendices collect the longer coordinate calculations and finite algebraic checks.

### 2 The source system and labelled compactified graphic

We first identify the oriented compactified graphic and fix a physical collar, radial cut, and finite face skeleton. These parameter-independent objects provide the common domain for all stopped first-hit relations below.

The first integral ( 1.2) is strictly convex on y > − 1 y>-1: its Hessian is

 | D 2 ​ H = ( 1 0 0 ( 1 + y) − 2), D^{2}H=\begin{pmatrix}1&0\\ 0&(1+y)^{-2}\end{pmatrix}, |  |

and its only critical point is the origin. Since H H tends to + ∞ +\infty both at y = − 1 y=-1 and at affine infinity, every level H = h > 0 H=h>0 is one periodic oval. As h → ∞ h\to\infty, these ovals converge on the Poincare sphere to

 | Γ H ​ 14 3 = L − ∪ { p + } ∪ E + ∪ { q } ∪ E − ∪ { p − }, \Gamma_{H14^{3}}=L_{-}\cup\{p_{+}\}\cup E_{+}\cup\{q\}\cup E_{-}\cup\{p_{-}\}, |  |

where L − = { y = − 1 } L_{-}=\{y=-1\}, p ± p_{\pm} are the horizontal endpoints, q q is the positive vertical point, and E ± E_{\pm} are the two upper equatorial arcs.

The orientation is part of the label. Along L − L_{-} one has x ˙ = 1 \dot{x}=1, so p − → p + p_{-}\to p_{+}. In the upper chart y = 1 / r y=1/r, x = w / r x=w/r, after the positive degree-two desingularization,

 | r ˙ = − r ​ w − r 2 ​ w, w ˙ = − w 2 − r ⁡ ( 1 + w 2). \dot{r}=-rw-r^{2}w,\qquad\dot{w}=-w^{2}-r(1+w^{2}). |  |

Thus the upper arcs are oriented p + → q → p − p_{+}\to q\to p_{-}. Equivalently, in the positive endpoint coordinates x = 1 / r x=1/r, z = 1 + y z=1+y,

 | r ′ = − r 3 ​ ( 1 − z), z ′ = z, r^{\prime}=-r^{3}(1-z),\qquad z^{\prime}=z, |  |

whereas at the negative endpoint x = − 1 / r x=-1/r,

 | r ′ = r 3 ​ ( 1 − z), z ′ = − z. r^{\prime}=r^{3}(1-z),\qquad z^{\prime}=-z. |  |

These formulas fix the cyclic order

 | L − ⟶ p + ⟶ E + ⟶ q ⟶ E − ⟶ p − ⟶ L −. L_{-}\longrightarrow p_{+}\longrightarrow E_{+}\longrightarrow q\longrightarrow E_{-}\longrightarrow p_{-}\longrightarrow L_{-}. |  | (2.1) |

p − p_{-} p + p_{+} q q L − = { y = − 1 } L_{-}=\{y=-1\} E + E_{+} E − E_{-} periodic ovals of H H approach the boundary graphic fixed collar U U Figure 1: The labelled source graphic Γ H ​ 14 3 \Gamma_{H14^{3}} and its orientation. The picture is schematic; the endpoint and upper-chart coordinates used in the proof are given in Sections 2 and 4.

We now choose the counting region before perturbing. Put z = 1 + y z=1+y and fix X L > 1 X_{L}>1. For z L > 0 z_{L}>0 and the parameter ball sufficiently small,

 | B L = { | x | ≤ X L, | z | ≤ z L }, x ˙ = 1 − z + B ​ x 2 + μ 2 ​ ( z − 1) 2 + a ​ x > 1 2, B_{L}=\{|x|\leq X_{L},\ |z|\leq z_{L}\},\qquad\dot{x}=1-z+Bx^{2}+\mu_{2}(z-1)^{2}+ax>\frac{1}{2}, |  | (2.2) |

where

 | a = μ 4 + B ​ μ 5, c = ( 1 − 2 ​ B) ​ μ 5. a=\mu_{4}+B\mu_{5},\qquad c=(1-2B)\mu_{5}. |  | (2.3) |

The proper radial cut is

 | Σ = { x = − X L, | z | < z L }. \Sigma=\{x=-X_{L},\ |z|<z_{L}\}. |  | (2.4) |

The finite-line strip is two-sided: it includes both z > 0 z>0 and z < 0 z<0. Indeed the former invariant line may be crossed because

 | z ˙ | z = 0 = μ 3 − c = μ 3 − ( 1 − 2 ​ B) ​ μ 5. \dot{z}\big|_{z=0}=\mu_{3}-c=\mu_{3}-(1-2B)\mu_{5}. |  | (2.5) |

The strict coordinate is x x; the source energy is never evaluated on a perturbed orbit below z = 0 z=0.

Choose disjoint fixed neighborhoods of p + p_{+}, q q, and p − p_{-}, and cover the remaining compact regular arcs by finitely many analytic flow boxes. Their constant flow-coordinate levels are transverse cuts; the two transverse levels of each flow box are collar sides and are not promoted to passage sections. Gluing these finitely many pieces gives a fixed two-sided open annulus U U, disjoint from the finite center and the lower equator. All five parameters in ( 1.3) remain active on this same U U.

###### Proposition 2 (Fixed physical skeleton).

There is a finite list ℱ 0 \mathcal{F}_{0} of cross-cuts, collar faces, box faces, and chart-overlap faces, fixed before gate classification. Every cross-cut has a uniform signed transverse normal for small λ \lambda. Every collar face retains its complete tangency equation X λ ​ f = 0 X_{\lambda}f=0 and is treated as an exit side. Pullback through the finite endpoint and upper-vertical resolutions produces another finite face list.

###### Remark 3.

The skeleton is chosen once for a sufficiently small ball in all five parameters. Cross-cut normals retain their sign throughout that ball, while every collar tangency remains an explicit exit equation. In particular, collar sides are never silently promoted to passage sections.

###### Proof.

Take B L B_{L}, fixed endpoint rectangles, a fixed upper rectangle, and finitely many flow-box overlap levels as above. Compactness of each selected cross-cut and the strict source normal give a positive margin that persists for small parameters. No such claim is made for a collar side; for example X 0 ​ ( z − z L) = x ​ z L X_{0}(z-z_{L})=xz_{L} vanishes at x = 0 x=0, so this tangency is kept explicitly. The endpoint incidence, source-core, and parameter-dominated blow-ups are finite maps with finitely many coordinate faces. Pulling back the already fixed equations therefore preserves finiteness. Later invariant axes are introduced only inside their named normal-form boxes and meet another box through a preassigned member of ℱ 0 \mathcal{F}_{0}. ∎

### 3 A stopped-return model and geometric overview

The following elementary model isolates the order and no-Zeno mechanism later verified uniformly in the H 14 3 H_{14}^{3} charts. It starts with a cut-open annular collar, finitely many singular boxes, and their physical first ports.

We begin with the small model that governs the full construction. Cut an annular collar at one proper radial section Σ \Sigma. Suppose the cut-open collar contains three disjoint singular boxes B + B_{+}, B q B_{q}, and B − B_{-}, joined in this order by regular flow strips. Each box has one incoming arc, one next-cut arc, finitely many singular gate arcs, and collar sides. The question is not initially whether a return map has a zero. It is whether a point on an incoming arc reaches the next cut before any competing port.

For a point s s on an incoming interval I I, follow its orbit only until its first physical boundary contact. The outcome is either a transverse next cut, a named singular gate, a previous-side port, or a collar exit. Boundaries between outcome intervals are called *divider points*. They are backward first hits of fixed corners or tangencies, or intersections with a stable or center half-branch. When two divider labels coincide, the intervening interval is a collapsed interval and carries no phase point.

###### Proposition 4 (Three-box stopped-return principle).

Assume that every regular strip has a strict flow coordinate, each singular box has finitely many equilibria and local sectors, and every nonexiting orbit in a singular box tends to one of those sectors. Assume also that each labelled corner orbit and invariant half-branch meets the incoming arc at most once. Then every incoming arc is divided by finitely many labelled points into open intervals with one first outcome. Every through outcome is an order-preserving first-hit diffeomorphism. After Σ \Sigma is deleted, through edges strictly increase the box/cut index; hence there are finitely many cut-open paths and finitely many full-lap words after Σ \Sigma is restored.

###### Proof.

For an open port J J, the set of points whose first contact lies in J J is open by transversality and continuous dependence. A boundary point of this set cannot first hit the interior of a transverse port. If its contact time is finite, it therefore lies on a listed corner, tangency, or invariant side. If the contact time diverges, the planar limit set lies in the finite equilibrium/sector list. The one-intersection hypothesis assigns at most one divider to each label. Removing these finitely many points leaves intervals on which the outcome label is locally constant, hence constant. Planar orbit uniqueness makes a through map order preserving.

Number the successive physical cuts in the positive collar orientation. A through map goes to the next cut; all other outcomes are terminal. The cut number is therefore a strict integer rank, so the cut-open directed graph is finite and acyclic. Restoring the deleted cut closes only complete laps. The full H14 proof below verifies these hypotheses uniformly through every root and gate collision; the model explains why stopping must precede return-map formation. ∎

#### 3.1 From stopped paths to finite sums

For an isolated cycle in the fixed collar, the reductions occur in a fixed order: stopped first hits, a retained full-lap itinerary, a local zero theorem, and finally the compact finite sum. In particular, compactness and full-lap equations are used only after the stopped atlas has supplied their domains.

Figure 2 shows the elementary mechanism. The solid chain becomes a return equation only after all competing first contacts have been excluded.

Σ \Sigma B + B_{+} B q B_{q} B − B_{-} Σ \Sigma first hit one lap singular gate passive side collar exit The solid chain is the interior through itinerary. A dashed first contact either hands the orbit to its prelabelled adjacent boundary itinerary or is independently terminal; only the latter ends the return construction. Figure 2: A stopped itinerary through the three singular boxes. The diagram records first-contact alternatives, not the detailed shape of the local phase portraits; a dashed arrow stops the current local relation but need not terminate the physical orbit.

There are three logically distinct classification stages. First, Part I rejects candidates that do not carry a retained full-lap itinerary. Second, each retained itinerary enters one relative-interior analytic regime. Third, proper specializations descend inside a finite specialization graph. In particular, an ordinary coefficient face need not be an identity; it is sent to its terminal minimal-face regime. Only an identity interval, including an all-zero coefficient stratum that produces such an identity, contributes no isolated member.

### 4 Endpoint and upper-vertical boxes

The fixed skeleton leaves three singular neighborhoods unresolved. We derive representative equations at the horizontal endpoints and the upper vertical point, classify their retained passages, and obtain a finite singular alphabet with physical sections and fixed-original-parameter descent.

The local equations are derived from the full family, not from a reduced representative. At the positive horizontal endpoint, x = 1 / r x=1/r, y = z − 1 y=z-1,

 | r ˙ = − r ⁡ { B + a ​ r + r 2 ​ [1 − z + μ 2 ​ ( z − 1) 2] }, z ˙ = z + r ⁡ [μ 3 ​ ( z − 1) 2 + c ⁡ ( z − 1)]. \dot{r}=-r\{B+ar+r^{2}[1-z+\mu_{2}(z-1)^{2}]\},\qquad\dot{z}=z+r[\mu_{3}(z-1)^{2}+c(z-1)]. |  | (4.1) |

At the negative endpoint, x = − 1 / r x=-1/r,

 | r ˙ = r ⁡ { B − a ​ r + r 2 ​ [1 − z + μ 2 ​ ( z − 1) 2] }, z ˙ = − z + r ⁡ [μ 3 ​ ( z − 1) 2 + c ⁡ ( z − 1)]. \dot{r}=r\{B-ar+r^{2}[1-z+\mu_{2}(z-1)^{2}]\},\qquad\dot{z}=-z+r[\mu_{3}(z-1)^{2}+c(z-1)]. |  | (4.2) |

Solving the transverse zero graph analytically and restricting the radial numerator to it gives

 | P + ​ ( r, λ) = B + a ​ r + r 2 ​ U + ​ ( r, λ), P − ​ ( r, λ) = B − a ​ r + r 2 ​ U − ​ ( r, λ), P_{+}(r,\lambda)=B+ar+r^{2}U_{+}(r,\lambda),\qquad P_{-}(r,\lambda)=B-ar+r^{2}U_{-}(r,\lambda), |  | (4.3) |

with U ± ​ ( 0, 0) ≠ 0 U_{\pm}(0,0)\neq 0. Degree-two preparation therefore gives only a simple hyperbolic root, a double saddle-node root, or the critical multiplicity-three layer B = a = 0 B=a=0 after the persistent factor r r is restored. There is no uniform factorization as r 3 r^{3} away from that layer.

For a prescribed finite differentiability order, the joint endpoint normal form may be written, after the required local time reversal, as

 | x ′ = q α ​ ( x), y ′ = − y, x^{\prime}=q_{\alpha}(x),\qquad y^{\prime}=-y, |  | (4.4) |

with at most three weak roots. The function

 | ℒ α ​ ( x, y) = ∫ 0 x q α ​ ( v) ​ 𝑑 v − y 2 2 \mathcal{L}_{\alpha}(x,y)=\int_{0}^{x}q_{\alpha}(v)\,dv-\frac{y^{2}}{2} |  | (4.5) |

satisfies

 | ℒ ˙ α = q α ​ ( x) 2 + y 2. \dot{\mathcal{L}}_{\alpha}=q_{\alpha}(x)^{2}+y^{2}. |  | (4.6) |

It excludes recurrence inside the fixed endpoint slab. Root lines, the strong axis, and backward corner orbits form its finite divider alphabet. The normalizer transports fixed model sections; it is not used to define a global analytic stratification.

At the upper vertical point use y = 1 / r y=1/r, x = w / r x=w/r. Set

 | F ⁡ ( r, w) = ( 1 + r) ​ w + μ 3 + r ​ c, F(r,w)=(1+r)w+\mu_{3}+rc, |  | (4.7) |

 | Q ⁡ ( r, w) = μ 2 − μ 3 ​ w + ( B − 1) ​ w 2 + r ⁡ [− 1 + ( a − c) ​ w − w 2]. Q(r,w)=\mu_{2}-\mu_{3}w+(B-1)w^{2}+r[-1+(a-c)w-w^{2}]. |  | (4.8) |

Then r ˙ = − r ​ F \dot{r}=-rF and w ˙ = Q \dot{w}=Q. Choose fixed δ, r ∗ > 0 \delta,r_{*}>0 so that

 | Q ( r, ± δ) < 0, F ( r, δ) > 0, F ( r, − δ) < 0 ( 0 ≤ r ≤ r ∗). Q(r,\pm\delta)<0,\qquad F(r,\delta)>0,\qquad F(r,-\delta)<0\quad(0\leq r\leq r_{*}). |  | (4.9) |

Thus w = δ w=\delta is the physical entry, w = − δ w=-\delta the next cut, and r = r ∗ r=r_{*} the collar side. On F = 0 F=0 the graph

 | w s ​ ( r) = − μ 3 + r ​ c 1 + r w_{s}(r)=-\frac{\mu_{3}+rc}{1+r} |  |

has S ⁡ ( r):= Q ⁡ ( r, w s ​ ( r)) S(r):=Q(r,w_{s}(r)) with S ′ ( r) ≤ − 1 / 2 S^{\prime}(r)\leq-1/2. Moreover

 | F w = 1 + r > 0, Q r < − 1 2, F ˙ | F = 0 = ( 1 + r) ​ Q, sgn ⁡ Q ˙ | Q = 0 = sgn ⁡ F. F_{w}=1+r>0,\qquad Q_{r}<-\frac{1}{2},\quad\dot{F}|_{F=0}=(1+r)Q,\quad\operatorname{sgn}\dot{Q}|_{Q=0}=\operatorname{sgn}F. |  | (4.10) |

These signs give a directed four-cell graph. Every nonexiting orbit is coordinatewise monotone until it reaches one of finitely many equilibria; there is no internal recurrent set.

On the equator the gate equation is

 | E ⁡ ( w, λ) = μ 2 − μ 3 ​ w + ( B − 1) ​ w 2 = 0, E(w,\lambda)=\mu_{2}-\mu_{3}w+(B-1)w^{2}=0, |  | (4.11) |

so there are at most two equatorial roots. The graph F = 0 F=0 supplies at most one interior root, and its determinant is negative. The only joint collisions are the equatorial discriminant collision, the equatorial/interior collision, and the source core. In the source core,

 | r = θ 2, w = θ ​ W, μ 2 = θ 2 ​ m ¯ 2, μ 3 = θ ​ m ¯ 3, r=\theta^{2},\quad w=\theta W,\quad\mu_{2}=\theta^{2}\bar{m}_{2},\quad\mu_{3}=\theta\bar{m}_{3}, |  | (4.12) |

and the exceptional equation has W ˙ = − 1 − W 2 / 2 \dot{W}=-1-W^{2}/2 at the source point. Thus W W is a direct passage coordinate, while θ 2 ​ m ¯ 2 = μ 2 \theta^{2}\bar{m}_{2}=\mu_{2} and θ ​ m ¯ 3 = μ 3 \theta\bar{m}_{3}=\mu_{3} keep the lifted flow on the original five-parameter fiber.

The signed substitutions, source cancellations, and auxiliary endpoint-scale identities used in this section are collected in Appendix A. The simultaneous degeneration of an endpoint root and its section coordinate, including the fixed-fiber clock estimates, is proved in Appendix D.1.

###### Proposition 5 (Finite singular alphabet).

After a finite resolved cover, every retained vertex in the endpoint and upper slabs is a direct regular passage, a separated hyperbolic saddle, or a simple saddle-node with fixed sector type. Same-sign node cores, stable-center sectors, wrong orientations, and collar exits are terminal labels. The source core is the direct passage ( 4.12); no unresolved double-zero vertex remains.

###### Remark 6.

The classification is uniform on the finite endpoint-incidence and upper-vertical resolved cover. Root and gate collisions remain in their joint boxes; wrong orientations, stable-center sides, nodes, and collar contacts are terminal first outcomes.

###### Proof.

Equation ( 4.3) gives the complete endpoint root list. For the upper box, F = 0 F=0 has at most one interior singular point because S ′ < 0 S^{\prime}<0, and its linear determinant is negative. On r = 0 r=0, equation ( 4.11) is quadratic. A single zero eigenvalue has a nonzero quadratic center term; simultaneous vanishing forces μ 2 = μ 3 = 0 \mu_{2}=\mu_{3}=0 in the normalized chart and therefore belongs to the source core ( 4.12). The sign of the two nonzero eigenvalues separates saddles from nodes. The fixed model sections and the monotonicity identities above then give the stated retained and terminal sector list. ∎

### 5 Fixed sections and stopped first hits

We next decide the first outcome for every point of every incoming interval, including limits with unbounded flight time. The fixed face skeleton and the finite singular alphabet yield a finite physical first-port relation on common domains; no full-lap map is formed at this stage.

###### Definition 7 (Stopped first port).

Fix one block and one incoming physical section. The stopped first port of an entry point is its first physical boundary contact with the complete named port union. A trajectory that remains in the block and converges to a named root, axis, saddle-node, or node sector is assigned that terminal port. No trajectory is continued through such a limit in order to define a remote landing coordinate.

The port union contains the next transverse cut, every competing transverse side, invariant root/axis/center sides inside their owning box, previous-side faces, fixed corners, and collar sides. Resolved chart overlaps identify the same physical point and are not competing ports. This convention is what makes the first-hit relation stable when flight time tends to infinity.

###### Proposition 8 (Uniform stopped first-hit theorem).

On every fixed regular strip, endpoint slab, and upper slab, and on every resolved parameter face attached to it, the incoming interval has a uniformly bounded finite divider set. Every complementary open interval has exactly one first-port label. A next-cut interval carries an order-preserving C K C^{K} first-hit diffeomorphism for any prescribed finite K K. A gate, previous-side, stable-center, node-core, wrong-orientation, or collar label is terminal. Coincident divider labels delete the interval between them.

###### Remark 9.

For each prescribed finite differentiability order K K, the conclusion is uniform on every closed resolved endpoint, upper, source-core, and transported normal-form face. Unbounded flights stop at named singular outer sections, label collisions delete the interval between them, and collar contacts are exits.

###### Proof.

The ordinary strips have an analytic coordinate θ \theta with X λ ​ θ ≥ c > 0 X_{\lambda}\theta\geq c>0. Their only outcome boundaries are backward orbits of fixed cut/collar corners. In an endpoint slab, ( 4.6) is a strict Lyapunov function away from the finitely many roots, and the invariant root lines and strong axis give a finite sector list. In the upper slab, ( 4.9)–( 4.10) give strict outer normals and a directed four-cell graph. The only tangency on r = r ∗ r=r_{*} is a strict local minimum of r r, hence cannot be a first outer contact from the interior. The source core has − W ˙ ≥ 1 / 2 -\dot{W}\geq 1/2 after shrinking. Separated saddle, node, and simple saddle-node boxes use fixed model sections with certified normal or Lyapunov margins.

For one open port J J, let E J E_{J} be the entry points whose first contact is in J J. This set is relatively open. If s ∗ s_{*} lies on its boundary and its contact time stays bounded, the limiting contact is a fixed corner, tangency, or outer section of a named singular box. If the time diverges, the strict coordinates above force the orbit into a named singular sector; the regular flight has already been stopped at that box’s outer section. Thus s ∗ s_{*} is the stopped backward intersection of one element of a finite label list. Each such orbit meets the one-way entry face at most once. There are therefore finitely many divider points, uniformly through the joint root and gate boxes.

On a complementary interval the outcome is locally constant, hence constant. Uniqueness of planar trajectories preserves order, and the implicit hit equation gives the claimed C K C^{K} map. The resolved phase–parameter flow preserves θ 2 ​ m ¯ 2 = μ 2 \theta^{2}\bar{m}_{2}=\mu_{2} and θ ​ m ¯ 3 = μ 3 \theta\bar{m}_{3}=\mu_{3} in the source core, so the lifted relation descends to the same original parameter fiber. On an overlap, orbit uniqueness gives

 | P χ ′ = ψ out ∘ P χ ∘ ψ in − 1; P_{\chi^{\prime}}=\psi_{\rm out}\circ P_{\chi}\circ\psi_{\rm in}^{-1}; |  | (5.1) |

both sides stop at the same physical contact and therefore carry the same port label. ∎

### 6 Finite itineraries

The stopped relations are local and may share divider points. Gluing them on fixed cuts, rejecting terminal sectors, and proving a strict global order produces the finite closed family of retained full-lap itineraries used by the later zero theorems.

Let C 0 = Σ, C 1, …, C m C_{0}=\Sigma,C_{1},\ldots,C_{m} be the fixed cuts in the oriented order ( 2.1). Refine each C i C_{i} by the union of the divider sets from its two adjacent stopped relations. On each finite ordering chart write

 | e π ⁡ ( 1) ≤ ⋯ ≤ e π ⁡ ( n), π ∈ 𝔖 n. e_{\pi(1)}\leq\cdots\leq e_{\pi(n)},\qquad\pi\in\mathfrak{S}_{n}. |  | (6.1) |

Equality in ( 6.1) records a collapsed interval. Images and inverse images of divider points under an order-preserving through map add only finitely many labels. This finite sorting operation is performed on fixed one-dimensional cuts; it does not assert that a zero set of arbitrary transported finite-smooth faces has finitely many components.

Before words are formed, we remove the terminal outcomes. A wrong-oriented upper cell cannot reach the next larger − w -w level. A stable-center sector tends to its singular point or returns to a previous face. A same-sign node has a Lyapunov core which can be entered only for a sink, or left only for a source; the core is not an incoming-to-next-cut passage. A regular corridor outside that node core is retained precisely when its strict coordinate joins consecutive cuts. Collar exits leave U U. These are geometric rejections, not zero-count conclusions.

###### Theorem 10 (Finite stopped word theorem).

The retained primitive section components form a finite directed graph. With C 0 C_{0} deleted, every retained edge goes from a subinterval of C i C_{i} to a subinterval of C i + 1 C_{i+1} and therefore strictly increases

 | I ⁡ ( v) = i ( v ⊂ C i). I(v)=i\qquad(v\subset C_{i}). |  | (6.2) |

The cut-open graph is acyclic and has finitely many paths. Restoring Σ \Sigma gives a finite family of stopped full-lap words. Every degeneration of a retained word is another labelled word face, a terminal no-passage face, or a collapsed interval; no extra boundary word appears.

###### Remark 11.

The same finite directed graph works on the complete resolved parameter ball, including root, divider, gate, and overlap limits. Every proper limit is an adjacent labelled itinerary, a no-passage face, or a collapsed interval; no remote boundary itinerary is introduced.

###### Proof.

Proposition 8 gives a uniformly finite vertex and edge list. By construction, only a next-cut outcome is retained, so ( 6.2) is strict. A directed path therefore visits at most the number of retained vertices. Root or divider collisions do not enlarge the graph: they identify labels or delete an interval.

For closure, take a convergent sequence of segments. Fix a box, ordering, and first-port label after passing to a subsequence. Bounded flight times give the same transverse hit or a named corner limit. Unbounded times enter a named singular isolating block, where the regular relation was already stopped. At a nonsingular accumulation point one flow box contains the whole tail; at a singular point one of finitely many sectors contains it. Hence there is no infinite switching, or Zeno, alternative. The finite incidence complex is exhaustive. ∎

### 7 Exact-once reduction

To count physical cycles without omission or duplication, we combine the stopped itinerary family with the positive radial cut. Annular intersection then gives an injective cycle-to-itinerary fixed-point representation.

###### Proposition 12 (Exact-once full-lap reduction).

After U U and the parameter ball are sufficiently small, every limit cycle contained in U U is essential in that annulus, crosses Σ \Sigma exactly once in positive orientation, and is represented by one retained stopped full-lap word. It is a fixed point of that word on its physical section. Minimal-face and half-open conventions identify overlap descriptions and assign every boundary lift once.

###### Remark 13.

The representation is uniform in the fixed collar and in one sufficiently small ball of the full five-parameter family. Minimal faces and the half-open convention identify overlap descriptions; terminal and collapsed faces carry no represented cycle.

###### Proof.

By ( 2.2), every crossing of Σ \Sigma has positive sign. A periodic orbit cannot miss Σ \Sigma: otherwise its retained cut index would increase strictly around a loop, or the orbit would lie in one regular strip or singular slab, where the strict coordinates and Lyapunov functions above exclude recurrence.

A limit cycle is an embedded closed curve. If it were contractible in the annulus, its algebraic intersection with a proper radial cut would be zero, contradicting the existence and common positive sign of its intersections with Σ \Sigma. Thus it is essential. An embedded essential circle represents a primitive generator of the annulus, so its algebraic intersection with Σ \Sigma is + 1 +1. Since every geometric intersection is positive,

 | #⁡ ( γ ∩ Σ) = 1. \#(\gamma\cap\Sigma)=1. |  | (7.1) |

Starting at this unique point, the cycle chooses one next-cut interval at every stage. A gate, previous-side, node-core, stable-center, wrong-oriented, or collar outcome would be terminal and is impossible on the cycle. Hence the itinerary is one retained stopped full-lap word and the starting point is its fixed point. Overlap charts describe the same physical orbit by ( 5.1). At a resolved boundary, choose the unique minimal face and the fixed half-open priority; a collapsed interval has no point. These conventions remove duplicate representations without introducing a proper-subarc return. ∎

### 8 Analytic regimes and theorem package

The physical recognition data of a retained itinerary determine one relative-interior analytic regime. Table 1 records this exhaustive decomposition before proper faces are specialized.

The recognition data in Table 1 are physical: section normals, eigenvalue margins, actual first ports, and complete pp/hh incidence. A theorem name is not used to manufacture the word to which it will later be applied.

We use the standard saddle-node sector letters throughout. A lower-case h h or p p denotes, respectively, a local hyperbolic (strong) or parabolic (central) separatrix sector. Thus an hh connection is an actual strong-separatrix connection between the two selected saddle-nodes, whereas a pp strip is a nonempty interval of complete orbits with those saddle-nodes as its alpha- and omega-limits. PP and BP denote the two physical boundary graphics admitted by the DIR lips theorem: the principal-endpoint boundary and the center-side boundary, respectively. “Attractivity” is the sign of the nonzero transverse eigenvalue after the one common local time orientation. In the middle chart, QBF and QHH abbreviate the buffered finite-phase region and the unbounded hyperbolic-corner region, respectively; these regions are defined in Section 26.

The strict/coalescing cutoff is fixed before any theorem neighborhood is chosen. Select nested finite tubular covers of the source-coalescing face. In every signed chart of the inner cover let t ≥ 0 t\geq 0 be its defining function, and choose one regular value 0 < t str < t 0 0<t_{\rm str}<t_{0} in the overlap. The strict regime contains the exterior of the inner tube and the equality t = t str t=t_{\rm str}; only 0 < t < t str 0<t<t_{\rm str} enters the middle/root comparison.

The latter comparison is half-open at the source/root corner. On the finite signed cover of the selected upper D D -double root write w = − q w=-q, q = σ ​ t q=\sigma t, with σ ∈ { ± 1 } \sigma\in\{\pm 1\} away from t = 0 t=0, and set

 | b m = B t 2, A m = a t, ϱ w = ( b m 2 + A m 4) 1 / 4. b_{m}=\frac{B}{t^{2}},\qquad A_{m}=\frac{a}{t},\qquad\varrho_{w}=(b_{m}^{2}+A_{m}^{4})^{1/4}. |  | (8.1) |

Under the weight- ( 2, 1) (2,1) root blow-up b m = κ 2 ​ b b_{m}=\kappa^{2}b, A m = σ ​ κ ​ A A_{m}=\sigma\kappa A,

 | ϱ w = κ ​ ( b 2 + A 4) 1 / 4. \varrho_{w}=\kappa(b^{2}+A^{4})^{1/4}. |  | (8.2) |

The angular factor is bounded above and away from zero. Choose a regular value ϱ #\varrho_{\#} in the doubled middle/root overlap and a fixed positive root-chart bound κ 0 \kappa_{0}. These definitions make every scale appearing in Table 1 available before the decomposition is stated.

Table 1: Decomposition into analytic regimes.

Region | Recognition data | Zero theorem | Boundary behavior |

Noncompact source | Complete center-compatible word and phase dominance after all effective-scale thresholds | Part II matched source theorem | A failed threshold is reclassified by its actual resolved gate labels as compact, hyperbolic, central, mixed, or terminal. |

Compact regular | Bounded jointly analytic transverse word | Compact analytic / Weierstrass theorem | Identity coefficients remain in the same ambient analytic neighborhood. |

Separated hyperbolic | Positive eigenvalue, connector, section, and word margins | Part III Mourtada QRH theorem | First margin loss stops at a named adjacent regime. |

One central block | Exactly one retained internal saddle-node and hyperbolic complement | One-central no-pp theorem | A complementary loss is classified before the theorem is used. |

Two central blocks, no pp | Both possible internal central blocks, same attractivity, and no complete pp connection | Two-central no-pp theorem | A certified pp strip moves to a lips regime. |

Positive-margin lips | Actual hh connection, complete pp strip, PP/BP boundary, positive margins, and outside the inner source-coalescing tube | Strict DIR lips theorem | The fixed tube boundary belongs to the strict regime; a lost physical margin is sent to its first-port regime. |

Middle coalescing scale | 0 < t < t str 0<t<t_{\rm str}, fixed half-open QBF/QHH split and ϱ w ≥ ϱ #\varrho_{w}\geq\varrho_{\#} in the weighted middle/root overlap | Middle QBF/QHH theorem | Equality ϱ w = ϱ #\varrho_{w}=\varrho_{\#} belongs to the middle case; named landing, identity, coefficient, and first-port faces are controlled or handed off. |

Positive root merger | 0 < t < t str 0<t<t_{\rm str}, 0 < ϱ w < ϱ #0<\varrho_{w}<\varrho_{\#}, represented by finite relative-interior root charts 0 < κ < κ #​ ( angle) 0<\kappa<\kappa_{\#}(\mathrm{angle}) | Positive root merger theorem | The theorem remains valid on 0 < κ ≤ κ 0 0<\kappa\leq\kappa_{0}, with κ #​ ( angle) ≤ κ 0 \kappa_{\#}(\mathrm{angle})\leq\kappa_{0}; the regime-cutoff equality and the two zero-scale faces use the middle and next two rows. |

Exact mixed face | t > 0, κ = 0 t>0,\ \kappa=0, equivalently B = a = 0 B=a=0 off the source face | Exact mixed face theorem | Its split complement is passive, regular, or hyperbolic. |

Source face | t = 0 t=0, including t = κ = 0 t=\kappa=0 | Matched source theorem | This priority removes the source/mixed corner overlap. |

Pre-word zero contribution | Passive, exit, node-core, wrong orientation, or a collapsed interval before word formation | Part I geometry | No return equation is formed. |

Here “parameter-dominated” names a resolved coordinate regime, not an additional zero-theorem case. At the first failed effective source threshold, the finite parameter-dominated gate classification is evaluated on the same physical lift. A transverse bounded word goes to the compact row; separated nonzero eigenvalues go to the hyperbolic row; one or two central gates go to the corresponding central/two-central routing; a persistent B = a = 0 B=a=0 endpoint goes to the mixed row; and a sink, wrong orientation, stable-center side, or exit is a pre-word zero contribution. These are exactly rows already present in the table. The table becomes exhaustive through one routing result that is not itself an additional analytic case. The Two-Central Exhaustion Theorem sends every retained itinerary carrying both possible central blocks to the two-central no-pp, strict lips, middle, positive-root, exact-mixed, or source row. Its first-port trichotomy and the nonaffineness argument leave no residual affine regime. This routing occurs after pre-word rejection and before the final analytic classification.

The half-open rules can now be read directly from the table. Middle contains 0 < t < t str 0<t<t_{\rm str} with ϱ w ≥ ϱ #\varrho_{w}\geq\varrho_{\#}, including equality, and the relative-interior root regime has 0 < t < t str 0<t<t_{\rm str} and 0 < ϱ w < ϱ #0<\varrho_{w}<\varrho_{\#}. The source face is t = 0 t=0, including t = κ = 0 t=\kappa=0, while t > 0, κ = 0 t>0,\ \kappa=0 is the mixed face. The root theorem is valid on 0 < κ ≤ κ 0 0<\kappa\leq\kappa_{0}; on each angular chart its regime stops at a fixed κ #​ ( angle) ≤ κ 0 \kappa_{\#}(\mathrm{angle})\leq\kappa_{0} determined by ϱ #\varrho_{\#}. It is never extrapolated to either zero-scale face, and the regime-cutoff equality belongs to middle. A zero of any other strict-lips margin is assigned to its named adjacent port before a later theorem neighborhood is chosen.

t t κ \kappa source face t = 0 t=0 mixed face κ = 0 \kappa=0 root middle strict t = t str t=t_{\rm str} Figure 3: The half-open parameter handoff. The source and exact mixed faces are controlled by independent estimates; positive root, middle, and strict regions occupy disjoint theorem neighborhoods. Curves and proportions are schematic.

#### 8.1 Zero theorems used in the assembly

The finite itineraries fall into the following analytic regimes. We record here only the conclusions needed for the assembly; their proofs and precise coordinate constructions are given in Parts II and III.

- •

The matched source theorem, Theorem 30, controls a center-compatible source itinerary on one common physical action tube, uniformly in all five parameters. It includes the two open lower-gate limits and the identity center return.

- •

The exact mixed theorem, Theorem 32, applies on B = a = 0 B=a=0 for every value of the forced ratio. It treats the face t > 0 t>0, κ = 0 \kappa=0; the corner t = 0 t=0 belongs to the source theorem.

- •

The all-hyperbolic theorem, Theorem 36, gives a locally uniform bound on each compact certified analytic word with separated eigenvalues, sections, and connectors. Coefficient and identity fibers stay in the same quasi-regular Hilbert neighborhood.

- •

Theorems 38 and 43 treat, respectively, one retained central saddle-node and two same-attractivity central saddle-nodes without a complete pp connection. Split, lost-port, and persistent-endpoint boundaries are assigned before either theorem is applied.

- •

The positive-margin lips theorem, Theorem 46, treats a certified hh connection, complete pp strip, and PP/BP boundary away from the source-coalescing tube.

- •

The middle and root theorems, Theorems 49 and 51, cover the two positive coalescing scales with the half-open convention displayed in Figure 3. Neither theorem is continued to the source or exact mixed face.

- •

Finally, Theorem 41 proves that every retained itinerary carrying both possible central blocks belongs to the no-pp, strict, middle, root, mixed, or source alternative. Thus no additional analytic regime remains.

### 9 Two-central geometric exhaustion

The regime table is disjoint except, a priori, for itineraries carrying both possible internal central blocks. Theorem 41 classifies precisely that case and eliminates the residual affine label.

We now apply Theorem 41; it is not used to construct the atlas. A retained two-central word has no third internal central gate. If no complete pp connection exists, Theorem 43 applies. Otherwise the signed gate count and center intersection identify two actual opposite saddle-nodes. The physical strong landing equation certifies the hh connection, and the stopped first-port relation either supplies a complete pp strip with PP/BP boundary or stops at a named port. On the complete strip the first-port trichotomy leaves the hh chain and the endpoint–upper chain as its two boundary graphics. The latter has hyperbolicity ratio outside the unresolved ratio-one range.

C 1 C_{1} C 2 C_{2} hh boundary complete pp strip entry exit no complete pp connection ⇒ \Rightarrow central no-pp estimate certified complete pp strip ⇒ \Rightarrow strict, middle, or root regime Figure 4: Schematic two-central incidence. The theorem uses the actual retained gates, sector ordering, and same-attractivity condition; the drawing only summarizes the resulting no-pp/lips alternative.

The formerly possible residual class consisted of a complete two-gate hh/pp word whose pp transition was declared affine before a PP/BP boundary was known. Physical order carries every point of the selected endpoint interval through the regular strips and upper cooperative squeeze to the second saddle-node; there is no intervening root, previous-side, or collar port. The non-hh endpoint is therefore the complete PP chain. The certified boundary theorem makes its transition nonaffine, and hence

 | 𝔄 aff = ∅. \mathfrak{A}_{\mathrm{aff}}=\varnothing. |  | (9.1) |

No additional analytic regime is needed.

###### Proposition 14 (Disjoint regime assignment).

Every retained word of Theorem 10 belongs to exactly one relative-interior row of Table 1. The assignment is exhaustive and disjoint. After the fixed strict cutoff t ≥ t str t\geq t_{\rm str} has been assigned, the inner coalescing resolution 0 < t < t str 0<t<t_{\rm str} uses the weighted radius ( 8.1), and its half-open priority is

 | t = 0 ⟶ source, t > 0, ϱ w = 0 ⟶ exact mixed, t > 0, 0 < ϱ w < ϱ #⟶ root merger, t > 0, ϱ w ≥ ϱ #⟶ middle. \begin{array}[]{rcl}t=0&\longrightarrow&\text{source},\\ t>0,\ \varrho_{w}=0&\longrightarrow&\text{exact mixed},\\ t>0,\ 0<\varrho_{w}<\varrho_{\#}&\longrightarrow&\text{root merger},\\ t>0,\ \varrho_{w}\geq\varrho_{\#}&\longrightarrow&\text{middle}.\end{array} |  | (9.2) |

Equality in the last line belongs to the middle case.

###### Remark 15.

The assignment is made on the finite resolved first-port, gate, coalescing-scale, and coefficient cover. Minimal faces and the half-open partition above count every overlap and zero-scale value once; proper specializations are treated in Section 11.

###### Proof.

First separate source words and bounded analytic words. Among the remaining words, the singular alphabet of Proposition 5 distinguishes all-hyperbolic, exactly one central, and two-central cases. Theorem 41 resolves the last class into no-pp or certified lips behavior and then into strict, middle, root, source, or mixed scale. The fixed cutoff above sends t ≥ t str t\geq t_{\rm str} to strict and sends 0 < t < t str 0<t<t_{\rm str} to ( 9.2), so this decision is pointwise and half-open. Formula ( 9.1) removes the only residual label. The minimal-face convention assigns a resolved boundary point once, and ( 9.2) assigns both zero-scale faces independently of the punctured root theorem. Terminal first ports were removed before this classification. ∎

### 10 Compact analytic words

Some retained itineraries remain in bounded transverse analytic tubes and need none of the singular theorems above. Finite coefficient division and Weierstrass preparation give a local zero bound for each such jointly analytic itinerary, including its identity coefficient fibers.

###### Theorem 16 (Compact analytic word theorem).

Let ω \omega be a bounded stopped full-lap word whose primitive first hits are jointly analytic on nested transverse physical tubes. Then its displacement

 | D ω ​ ( s, λ) = P ω ​ ( s, λ) − s D_{\omega}(s,\lambda)=P_{\omega}(s,\lambda)-s |  | (10.1) |

has a locally uniform finite number of isolated zeros. The same ambient neighborhood controls coefficient and identity fibers.

###### Remark 17.

The bound is uniform on one analytic phase–parameter neighborhood and then on a finite cover of the compact section closure. Coefficient and identity strata remain in the same preparation; an identity fiber has no isolated member.

###### Proof.

The finite composition defining P ω P_{\omega} is analytic on a common bounded phase–parameter tube. At a base parameter, expand ( 10.1) in the phase coordinate. The coefficient germs generate a finitely generated analytic ideal by Noetherianity of the local analytic ring. The Noetherian and Hilbert-basis ingredients, together with the associated preparation–division machinery, are given in Chapter II of Hervé [7, Chapter II, Theorems 1–2]. Principalize that ideal by blowing up its finite generator list. This is the explicit finite generator blow-up used here, not an application of Weierstrass preparation and not an imported global principalization theorem. On each standard coefficient chart the pulled-back ideal has one generator ε \varepsilon and every coefficient is ε \varepsilon times a projective coefficient vector, with at least one projective coordinate nonzero. Divide ( 10.1) by ε \varepsilon. The normalized displacement is not identically zero in s s on that projective direction. Complexify the normalized real-analytic germ in the section and parameter variables. The holomorphic Weierstrass preparation theorem [7, Chapter II, Theorem 1] writes it as a distinguished polynomial of fixed finite degree times a unit. Uniqueness and conjugation invariance make both factors real on the real locus, and hence give the same uniform local zero bound there. For comparison, Krantz–Parks [6, Theorem 6.1.3] gives the corresponding direct real-analytic preparation theorem; the argument here uses the complex form from Hervé just cited. On the face ε = 0 \varepsilon=0 the original displacement is identically zero on the section interval; that fiber is a period annulus and has no isolated member, while the same resolved coefficient chart controls neighboring fibers. A finite cover of the compact section and projective coefficient closures proves the assertion. When complete center slices are present, the common factor is the reduced center ideal supplied by Part II; otherwise it is the principalized local analytic ideal of this word. ∎

### 11 Specializations and identity strata

The preceding classification first applies to relative interiors. We now follow every proper specialization in the finite incidence complex. A strictly decreasing integer complexity proves termination, and the half-open priority assigns a terminal analytic regime or a genuine zero-contribution face.

The regime of a relative-interior word does not by itself determine every proper face. We therefore form a finite specialization graph. Its vertices record the box, divider ordering, first-port, primitive, fixed regime-scale status, and radial–projective coefficient labels. A proper arrow occurs when consecutive dividers coincide; a transverse port becomes a named singular port; one of the fixed source/strict/middle/root scale inequalities reaches its assigned equality face; a nonzero normalized coefficient reaches a projective face; or the coefficient radius reaches its all-zero apex. Overlap identifications are the same physical map and are not arrows.

Let n sc ​ ( v) n_{\rm sc}(v) be the number of active regime-scale inequalities at v v which have not yet been specialized to a named equality, and let n rad ​ ( v) ∈ { 0, 1 } n_{\rm rad}(v)\in\{0,1\} be one off the all-zero coefficient apex and zero at that apex. These labels are finite because the stopped atlas and all half-open cutoffs were fixed in advance.

For a vertex v v, define

 | 𝔠 ⁡ ( v) = \displaystyle\mathfrak{c}(v)={} | ( number of nonempty labelled intervals) \displaystyle\bigl(\text{number of nonempty labelled intervals}\bigr) |  | (11.1) |

 |  | + ( number of unspecialized ports) \displaystyle+\bigl(\text{number of unspecialized ports}\bigr) |  |

 |  | + n sc ​ ( v) \displaystyle+n_{\rm sc}(v) |  |

 |  | + ( number of nonzero projective coefficients) \displaystyle+\bigl(\text{number of nonzero projective coefficients}\bigr) |  |

 |  | + n rad ​ ( v). \displaystyle+n_{\rm rad}(v). |  |

Termination and regime assignment use different data. The integer 𝔠 \mathfrak{c} proves only that specialization cannot continue indefinitely. The terminal regime is fixed independently by the following canonical priority. A physical lift is first placed on the unique minimal resolved face containing it. On that face, its first stopped event precedes every remote description; a collapse face precedes its parent word; source-threshold equality uses the post-threshold primitive vector and the explicit compact/hyperbolic/central/mixed/terminal reclassification above; and a persistent B = 0 B=0 endpoint uses the mixed row before a generic hyperbolic or one-central closure row. Certified lips faces use the strict/middle/root/source/mixed half-open rules, including ( 9.2), and the internal QBF/QHH boundary belongs to the fixed earlier side. Coefficient faces use their unique minimal projective face, while an identity is retained under the ambient theorem that controls its neighboring fibers. Chart overlaps identify the same physical lift and do not enter this priority.

###### Proposition 18 (Finite specialization induction).

Every proper specialization lowers 𝔠 \mathfrak{c}. Consequently every specialization chain terminates. The canonical priority above assigns its endpoint to a unique minimal-face regime carrying one of the ambient theorems in Section 8.1, Theorem 16, or a zero-contribution terminal label. This includes every boundary, coefficient, collapse, separatrix, and identity value of every full-lap word.

###### Remark 19.

The finite specialization graph includes divider, port, scale, projective coefficient, and radial-apex faces. The radial apex is a graph vertex rather than a projective direction. Identity intervals contribute no isolated member, while neighboring fibers retain the theorem neighborhood attached to their terminal regime.

###### Proof.

A divider equality deletes one nonempty interval. A port specialization replaces an unspecialized passage by its already constructed root-clock, hyperbolic, central, regular, previous-side, or exit label. A coefficient face deletes a nonzero projective coefficient. A fixed source threshold, the strict cutoff t = t str t=t_{\rm str}, a middle/root equality, or a zero-scale face resolves one active scale slot and lowers n sc n_{\rm sc}. Passing from a punctured coefficient cone to its all-zero apex lowers n rad n_{\rm rad}. Thus every proper arrow strictly lowers one summand of ( 11.1) and increases none; the finite graph has no infinite descending chain.

The terminal regime is not inferred from this decrease. Evaluate all final face, first-event, scale, and coefficient labels on the terminal physical lift, then apply the canonical priority fixed above. These labels depend only on that lift, not on the order in which equalities were imposed. In particular, the globally fixed values t str t_{\rm str}, ϱ #\varrho_{\#}, and the QBF/QHH cutoff decide every scale equality, while coefficient radius zero decides the apex before any projective direction is read. The unique minimal resolved face and these half-open rules therefore give the same regime for every specialization path. This is the required confluence statement.

At a terminal transverse word, use its source, mixed, hyperbolic, central, strict, middle, root, or compact analytic neighborhood. A critical d d -port is passive, while its split side is hyperbolic or regular. A collapsed interval carries no section point, and a collar exit cannot lie on a cycle contained in the open collar. If a displacement is identically zero on a relative open interval, that interval is a period annulus and has no isolated member. This last observation is not used to bound nearby fibers: the ambient theorem attached to the same minimal face supplies that bound. A general coefficient face is likewise treated by its terminal theorem and is not declared an identity. Backward induction on 𝔠 \mathfrak{c} proves the proposition without an induction on the dimension or number of connected components of a parameter status set. ∎

### 12 Compact theorem neighborhoods and completion of the proof

The preceding sections give finitely many itineraries and local theorem neighborhoods, but not yet one number. We compactify the normalized carrier only after every point has such a neighborhood, and then obtain the finite sum that proves Theorem 1.

Let 𝔎 \mathfrak{K} be the finite disjoint union of closed normalized phase–parameter carriers for all minimal-face-assigned word lifts, with overlap lifts of the same physical point identified. Its factors are closed resolved parameter charts, closed physical sections, the compact source action intervals, buffered QBF/QHH and pp intervals, and compact radial–projective coefficient cones, represented by a radial interval times the projective sphere with all directions identified at radius zero. Zero-length intervals enter only as collapse labels and have no phase factor. Hence 𝔎 \mathfrak{K} is compact.

###### Proposition 20 (Finite assembly from the local zero theorems).

Assume the local zero theorems summarized in Section 8.1. Then every ζ ∈ 𝔎 \zeta\in\mathfrak{K} has a relatively open product neighborhood 𝒪 ζ \mathcal{O}_{\zeta} and an integer N ζ < ∞ N_{\zeta}<\infty bounding all isolated zeros represented there. A finite subcover gives a uniform finite bound for every stopped full-lap word, including all proper specializations.

###### Remark 21.

The compact normalized carrier covers the closed resolved five-parameter ball and every physical phase endpoint. Near a meeting face we may sum the bounds from finitely many incident theorem neighborhoods, while the half-open priority represents its physical lift once. Collapse, passive, exit, and identity members contribute no isolated cycle themselves.

###### Proof.

The minimal regime at ζ \zeta selects its ambient theorem. If finitely many theorem neighborhoods have closures meeting at that face, shrink to a common product neighborhood and sum their finitely many constants. This numerical enlargement controls both sides of the face; it does not change the unique physical regime assigned to ζ \zeta. Proposition 18 ensures that no untreated face remains. Compactness now gives

 | 𝔎 ⊂ 𝒪 ζ 1 ∪ ⋯ ∪ 𝒪 ζ A. \mathfrak{K}\subset\mathcal{O}_{\zeta_{1}}\cup\cdots\cup\mathcal{O}_{\zeta_{A}}. |  | (12.1) |

Order this cover and assign each lift to its first cover member. The assigned sets need not be connected or analytic, because the bound on an open neighborhood restricts to every subset. For each chart–word pair,

 | M χ, ω ≤ ∑ a = 1 A N a < ∞. M_{\chi,\omega}\leq\sum_{a=1}^{A}N_{a}<\infty. |  | (12.2) |

This is the numerical compactness step; finiteness of the word labels alone would not imply ( 12.2). ∎

###### Assembly of Theorem 1 from the local zero theorems.

Theorem 10 and Proposition 12 assign every isolated cycle in U U to one full-lap word exactly once. The source and exact mixed regimes are treated by Theorems 30 and 32. The positive-scale regimes are treated by Theorems 36, 38, 43, 46, 49, and 51; Theorem 41 proves that the two-central geometric alternatives reach this list with no residual affine case. Proposition 14 then makes the resulting regime partition exhaustive and disjoint. Theorem 16 handles bounded analytic words, and Proposition 18 handles every proper face. Thus Proposition 20 applies to these results.

Write the resulting disjoint partition as

 | 𝔓 src ⊔ 𝔓 str ⊔ 𝔓 mid ⊔ 𝔓 rt ⊔ 𝔓 mix ⊔ 𝔓 reg ⊔ 𝔓 ∂. \mathfrak{P}_{\rm src}\sqcup\mathfrak{P}_{\rm str}\sqcup\mathfrak{P}_{\rm mid}\sqcup\mathfrak{P}_{\rm rt}\sqcup\mathfrak{P}_{\rm mix}\sqcup\mathfrak{P}_{\rm reg}\sqcup\mathfrak{P}_{\partial}. |  | (12.3) |

Here the regular class contains compact analytic, all-hyperbolic, one-central, and two-central no-pp relative interiors; the boundary class contains proper specializations after their terminal theorem regime is fixed. For each class sum the finitely many numbers ( 12.2), assigning zero to identity, collapse, passive, and exit contributions. Exact-once counting then gives

 | N H ​ 14 3 ​ ( λ, U) ≤ B src + B str + B mid + B rt + B mix + B reg + B ∂ =: B H ​ 14 3 < ∞ N_{H14^{3}}(\lambda;U)\leq B_{\rm src}+B_{\rm str}+B_{\rm mid}+B_{\rm rt}+B_{\rm mix}+B_{\rm reg}+B_{\partial}=:B_{H14^{3}}<\infty |  |

for every sufficiently small value of all five original parameters. The collar U U and the parameter neighborhood were fixed before this finite sum, so the bound is locally uniform. This proves the theorem. ∎

## Part II Noncompact source return and exact mixed endpoint

### 13 The matched source equation

For a source-regime stopped itinerary from Part I, fixed points are zeros of the exact nonlinear equation stated below. Its derivation requires a common physical domain, a justified center division, control of the moving first-hit maps, and a two-step Rolle estimate; these ingredients occupy the following sections.

Retain the parameter coordinates

 | a = μ 4 + B ​ μ 5, c = ( 1 − 2 ​ B) ​ μ 5, d = μ 3, m = μ 2 a=\mu_{4}+B\mu_{5},\qquad c=(1-2B)\mu_{5},\qquad d=\mu_{3},\qquad m=\mu_{2} |  |

and put

 | τ = a + c, ℓ = d − c, t c = B + m, σ 0 = c ​ t c. \tau=a+c,\qquad\ell=d-c,\qquad t_{c}=B+m,\qquad\sigma_{0}=ct_{c}. |  | (13.1) |

On the lower physical section Σ 0 = { x = 0, z = 1 + y = s } \Sigma_{0}=\{x=0,z=1+y=s\}, set

 | h = s − 1 − log s, L = − log s, θ = h − 1 / 2, k = ℓ s. h=s-1-\log s,\qquad L=-\log s,\qquad\theta=h^{-1/2},\qquad k=\frac{\ell}{s}. |  | (13.2) |

The variable k k, not ℓ \ell alone, records the forced lower displacement. It will remain an independent bounded variable on every zero-carrying source cell.

Choose the physical strong sections

 | S + = { z = 1, x > 0 }, S − = { z = 1, x < 0 }. S_{+}=\{z=1,x>0\},\qquad S_{-}=\{z=1,x<0\}. |  |

The selected word factors into actual first-hit maps

 | P ℓ = J − ℓ ∘ M ℓ ∘ J + ℓ, P^{\ell}=J_{-}^{\ell}\circ M^{\ell}\circ J_{+}^{\ell}, |  | (13.3) |

where the two J J ’s contain the complete lower tails and horizontal endpoint passages, while M ℓ: S + → S − M^{\ell}:S_{+}\to S_{-} is precisely the upper passage. No auxiliary endpoint clock is included in M ℓ M^{\ell}.

Compare each forced lower map with its unforced map on the same physical sections:

 | s + = ( J + 0) − 1 ​ J + ℓ ​ ( s), s − = J − 0 ​ ( J − ℓ) − 1 ​ ( s). s_{+}=(J_{+}^{0})^{-1}J_{+}^{\ell}(s),\qquad s_{-}=J_{-}^{0}(J_{-}^{\ell})^{-1}(s). |  | (13.4) |

On the open survivor interval these levels have the exact secant form

 | C + = s + s = 1 + k ​ Γ +, C − = s − s = 1 − k ​ Γ −, C_{+}=\frac{s_{+}}{s}=1+k\Gamma_{+},\qquad C_{-}=\frac{s_{-}}{s}=1-k\Gamma_{-}, |  | (13.5) |

with Γ ± > 0 \Gamma_{\pm}>0. The faces C + = 0 C_{+}=0 and C − = 0 C_{-}=0 are the two named lower first-port gates. They are not values at which a return map is continued. Define

 | λ + = log ⁡ C + − s ⁡ ( C + − 1), λ − = − log ⁡ C − + s ⁡ ( C − − 1). \lambda_{+}=\log C_{+}-s(C_{+}-1),\qquad\lambda_{-}=-\log C_{-}+s(C_{-}-1). |  | (13.6) |

The elementary identity

 | h ⁡ ( s ​ C) − h ⁡ ( s) = s ⁡ ( C − 1) − log ⁡ C h(sC)-h(s)=s(C-1)-\log C |  | (13.7) |

shows that 1 − λ + / h 1-\lambda_{+}/h and 1 + λ − / h 1+\lambda_{-}/h are the incoming and outgoing normalized actions.

Use the unforced lower maps themselves to define the two action coordinates

 | e + ​ ( u) = h ⁡ ( ( J + 0) − 1 ​ u) h ⁡ ( s), e − ​ ( v) = h ⁡ ( J − 0 ​ v) h ⁡ ( s) e_{+}(u)=\frac{h((J_{+}^{0})^{-1}u)}{h(s)},\qquad e_{-}(v)=\frac{h(J_{-}^{0}v)}{h(s)} |  | (13.8) |

and the physical middle action map

 | T s, β, k = e − ∘ M ℓ ∘ e + − 1, β = ( B ​ h, m ​ h, a ​ h, c ​ h). T_{s,\beta,k}=e_{-}\circ M^{\ell}\circ e_{+}^{-1},\qquad\beta=(Bh,mh,a\sqrt{h},c\sqrt{h}). |  | (13.9) |

Then P ℓ ​ ( s) = s P^{\ell}(s)=s is exactly equivalent, with multiplicity, to

 | T s, β, k ​ ( 1 − λ + / h) = 1 + λ − / h. T_{s,\beta,k}(1-\lambda_{+}/h)=1+\lambda_{-}/h. |  | (13.10) |

On the unforced face k = 0 k=0, put P 0 = P 0 P_{0}=P^{0} and G 0 = h ⁡ ( P 0) − h ⁡ ( s) G_{0}=h(P_{0})-h(s). The two center components proved below give the exact reduced division

 | G 0 = τ ​ L 3 / 2 ​ A + σ 0 ​ L 5 / 2 ​ C, G_{0}=\tau L^{3/2}A+\sigma_{0}L^{5/2}C, |  | (13.11) |

where A, C > 0 A,C>0 and, for j = 0, 1, 2 j=0,1,2,

 | L j ​ | 𝔇 j ​ ( A 4 ​ 2 / 3 − 1) | + L j ​ | 𝔇 j ​ ( C 8 ​ 2 / 15 − 1) | ≤ C 0 ​ ϵ + η ⁡ ( ϵ, s). L^{j}\left|\mathfrak{D}^{j}\left(\frac{A}{4\sqrt{2}/3}-1\right)\right|+L^{j}\left|\mathfrak{D}^{j}\left(\frac{C}{8\sqrt{2}/15}-1\right)\right|\leq C_{0}\epsilon+\eta(\epsilon,s). |  | (13.12) |

Here 𝔇 = d / d ​ L \mathfrak{D}=d/dL keeps the five original parameters fixed.

For a scalar λ \lambda, define the action secant and the forced middle remainder by

 | 𝒯 s, β ​ ( λ) = h ⁡ { T s, β, 0 ​ ( 1) − T s, β, 0 ​ ( 1 − λ / h) }, \mathcal{T}_{s,\beta}(\lambda)=h\{T_{s,\beta,0}(1)-T_{s,\beta,0}(1-\lambda/h)\}, |  | (13.13) |

 | ℛ = h ​ { T s, β, 0 − T s, β, k } ​ ( 1 − λ + / h). \mathcal{R}=h\{T_{s,\beta,0}-T_{s,\beta,k}\}(1-\lambda_{+}/h). |  | (13.14) |

Subtracting ( 13.10) from its unforced counterpart yields the decisive identity.

###### Theorem 22 (Matched source preparation).

On every unforced-center-complete zero-carrying source word, after the finite first-port and action refinement, the physical fixed-point equation is exactly

 | τ ​ L 3 / 2 ​ A + σ 0 ​ L 5 / 2 ​ C = 𝒯 s, β ​ ( λ +) + λ − + ℛ. \boxed{\;\tau L^{3/2}A+\sigma_{0}L^{5/2}C=\mathcal{T}_{s,\beta}(\lambda_{+})+\lambda_{-}+\mathcal{R}.\;} |  | (13.15) |

All terms are defined on one common physical product tube. The two lower factors are exact, the only middle error is ℛ \mathcal{R}, and the equivalence preserves zero multiplicity. The equation is not asserted on either gate face C ± = 0 C_{\pm}=0.

The proof is completed in Section 20. Its dependencies are deliberately forward:

 | Sections 14 – 15: legal domains, center division, and bounded ​ k, Sections 17 – 18: moving maps and differentiated estimates, Section 19: noncircular localization of every possible zero, Section 20: exact derivation of ( 13.15) and Rolle zero count. \begin{array}[]{ccl}\text{Sections~\ref{sec:part-ii-center}--\ref{sec:part-ii-lower}}&:&\text{legal domains, center division, and bounded }k,\\ \text{Sections~\ref{sec:part-ii-six-jet}--\ref{sec:part-ii-variation}}&:&\text{moving maps and differentiated estimates},\\ \text{Section~\ref{sec:part-ii-action}}&:&\text{noncircular localization of every possible zero},\\ \text{Section~\ref{sec:part-ii-source}}&:&\text{exact derivation of \eqref{eq:part-ii-matched} and Rolle zero count}.\end{array} |  | (13.16) |

This order excludes both failed shortcuts: division on an unproved outer word and replacement of ( 13.15) by a linear combination of source energy asymptotics.

### 14 Center geometry, legal division, and common word domains

We identify the two complete center components and prove the reduced division used in ( 13.11). The division is carried out for a physical stopped itinerary, not for an unspecified return germ, on a three-contraction unforced domain where both center identities hold throughout the section interval.

###### Theorem 23 (Center set and reduced ideal).

Near the source the center set is the union

 | 𝒞 R = { τ = 0, a = 0, d = 0 }, 𝒞 Q = { τ = 0, t c = B + m = 0, d + a = 0 }, \mathcal{C}_{R}=\{\tau=0,a=0,d=0\},\qquad\mathcal{C}_{Q}=\{\tau=0,t_{c}=B+m=0,d+a=0\}, |  | (14.1) |

and its reduced analytic ideal is

 | ℐ 𝒞 = ( τ, ℓ, d ⁡ ( B + m)). \mathcal{I}_{\mathcal{C}}=(\tau,\ell,d(B+m)). |  | (14.2) |

On the unforced face ℓ = 0 \ell=0, let σ 0 = c ⁡ ( B + m) = ( τ − a) ​ t c \sigma_{0}=c(B+m)=(\tau-a)t_{c}. If a C K C^{K} displacement F 0 F_{0}, K ≥ 2 K\geq 2, is defined on a word domain star-shaped under the successive contractions τ ↦ 0 \tau\mapsto 0, a ↦ 0 a\mapsto 0, and t c ↦ 0 t_{c}\mapsto 0, and vanishes on both complete center slices, then

 | F 0 = τ ​ F 0, τ + σ 0 ​ F 0, σ, F 0, j ∈ C K − 2. F_{0}=\tau F_{0,\tau}+\sigma_{0}F_{0,\sigma},\qquad F_{0,j}\in C^{K-2}. |  | (14.3) |

No continuation in ℓ \ell and no division of a finite-smooth saddle-node normalizer occurs.

###### Proof.

A center first has zero trace, hence τ = 0 \tau=0 and c = − a c=-a. Put

 | u = x − a ​ y, v = 1 − a 2 ​ y, ω = 1 − a 2. u=x-ay,\qquad v=\sqrt{1-a^{2}}\,y,\qquad\omega=\sqrt{1-a^{2}}. |  |

After a positive time division the system is

 | u ′ = − v + A ​ u 2 + C ​ u ​ v + D ​ v 2, v ′ = u + E ​ u ​ v + F ​ v 2, u^{\prime}=-v+Au^{2}+Cuv+Dv^{2},\qquad v^{\prime}=u+Euv+Fv^{2}, |  | (14.4) |

where

 | A = B ω, C = a ⁡ ( 2 ​ B − 1) ω 2, D = a 2 ​ ( B − 1) + m − a ​ d ω 3, E = 1 ω, F = a + d ω 2. A=\frac{B}{\omega},\quad C=\frac{a(2B-1)}{\omega^{2}},\quad D=\frac{a^{2}(B-1)+m-ad}{\omega^{3}},\quad E=\frac{1}{\omega},\quad F=\frac{a+d}{\omega^{2}}. |  | (14.5) |

The focal calculation is finite and can be reproduced without a black-box center theorem. Write V n = ∑ j = 0 n c n, j ​ u n − j ​ v j V_{n}=\sum_{j=0}^{n}c_{n,j}u^{n-j}v^{j} and G n = ( Q 1 ∂ u + Q 2 ∂ v) V n − 1 = ∑ g n, j u n − j v j G_{n}=(Q_{1}\partial_{u}+Q_{2}\partial_{v})V_{n-1}=\sum g_{n,j}u^{n-j}v^{j}. The coefficients obey

 | g n, j = \displaystyle g_{n,j}={} | [A ⁡ ( n − 1 − j) + E ​ j] ​ c n − 1, j \displaystyle[A(n-1-j)+Ej]c_{n-1,j} |  | (14.6) |

 |  | + [C ⁡ ( n − j) + F ⁡ ( j − 1)] ​ c n − 1, j − 1 + D ⁡ ( n − j + 1) ​ c n − 1, j − 2, \displaystyle+[C(n-j)+F(j-1)]c_{n-1,j-1}+D(n-j+1)c_{n-1,j-2}, |  |

and the homological equation is

 | 0 = \displaystyle 0={} | ( j + 1) ​ c n, j + 1 − ( n − j + 1) ​ c n, j − 1 + g n, j \displaystyle(j+1)c_{n,j+1}-(n-j+1)c_{n,j-1}+g_{n,j} |  | (14.7) |

 |  | − 𝟏 { n, j ​ even } ​ ( n / 2 j / 2) ​ L n / 2 − 1. \displaystyle-\mathbf{1}_{\{n,j\ \mathrm{even}\}}\binom{n/2}{j/2}L_{n/2-1}. |  |

For odd n n this system is invertible; for even n n, the gauge c n, 0 = 0 c_{n,0}=0 determines the coefficients and the single obstruction. At degree four,

 | 8 ​ L 1 = A ​ C + C ​ D + 2 ​ D ​ F − E ​ F. 8L_{1}=AC+CD+2DF-EF. |  | (14.8) |

After multiplication by the positive unit ω 5 \omega^{5}, this becomes

 | ℓ 1 = \displaystyle\ell_{1}={} | 2 ​ B 2 ​ a + 2 ​ B ​ a ​ m − B ​ a − 2 ​ a 2 ​ d + a ​ m − 2 ​ a ​ d 2 − a + 2 ​ m ​ d − d. \displaystyle 2B^{2}a+2Bam-Ba-2a^{2}d+am-2ad^{2}-a+2md-d. |  | (14.9) |

Since ∂ d ℓ 1 ​ ( 0) = − 1 \partial_{d}\ell_{1}(0)=-1, its zero set is one analytic graph. Put e = d + a e=d+a. On that graph the degree-six recurrence ( 14.6)–( 14.7), equivalently angular averaging of G 6 G_{6}, gives

 | L 2 = a ⁡ ( B + m) ​ U ​ ( a, B, m), U ⁡ ( 0) = 1 48. L_{2}=a(B+m)U(a,B,m),\qquad U(0)=\frac{1}{48}. |  | (14.10) |

For completeness, exact divisibility in ( 14.10) is not inferred from its quadratic jet. The first obstruction is the polynomial equation

 | e ⁡ ( 2 ​ a 2 + 2 ​ t c − 2 ​ B − 1) − 2 ​ a ​ e 2 + a ⁡ ( 2 ​ B − 1) ​ t c = 0. e(2a^{2}+2t_{c}-2B-1)-2ae^{2}+a(2B-1)t_{c}=0. |  | (14.11) |

Its unique root e = ψ ⁡ ( a, t c, B) e=\psi(a,t_{c},B) vanishes identically on a = 0 a=0 and on t c = 0 t_{c}=0, hence ψ = a ​ t c ​ V \psi=at_{c}V by two Hadamard integrals. Substitution in the degree-six polynomial obtained from ( 14.6)–( 14.7) vanishes on the same two slices, so a second two-variable integral gives ( 14.10); the degree-two term is a ​ t c / 48 at_{c}/48, proving that U U is a unit. The finite rational recurrence is also checked electronically, but the proof is the displayed recurrence together with the slice cancellations and the unit coefficient.

Thus L 1 = L 2 = 0 L_{1}=L_{2}=0 gives either a = e = 0 a=e=0 or t c = e = 0 t_{c}=e=0. On the first branch the transformed field is reversible. On the second branch m = − B, d = c = − a m=-B,d=c=-a, and

 | K Q = \displaystyle K_{Q}={} | B 2 ​ x 2 − B 2 ​ y 2 + B ​ a ​ x ​ y + 2 ​ B ​ a ​ x − B ​ x 2 − 2 ​ B ​ y \displaystyle B^{2}x^{2}-B^{2}y^{2}+Baxy+2Bax-Bx^{2}-2By |  | (14.12) |

 |  | + a 2 ​ y + a 2 − a ​ x − 1, 𝒱 Q = ( 1 + y) ​ K Q a 2 − 1 \displaystyle+a^{2}y+a^{2}-ax-1,\qquad\mathcal{V}_{Q}=\frac{(1+y)K_{Q}}{a^{2}-1} |  |

satisfies

 | X ⁡ ( 𝒱 Q) = ( div ⁡ X) ​ 𝒱 Q. X(\mathcal{V}_{Q})=(\operatorname{div}X)\mathcal{V}_{Q}. |  | (14.13) |

Since 𝒱 Q ​ ( 0, 0) = 1 \mathcal{V}_{Q}(0,0)=1, division by it gives a closed analytic one-form with definite quadratic part. Both branches are therefore centers, and the preceding necessity excludes a third branch.

In the coordinates ( τ, ℓ, a, t c, B) (\tau,\ell,a,t_{c},B), the union ( 14.1) is

 | { τ = ℓ = a = 0 } ∪ { τ = ℓ = t c = 0 }, \{\tau=\ell=a=0\}\cup\{\tau=\ell=t_{c}=0\}, |  |

whose reduced ideal is ( τ, ℓ, a ​ t c) (\tau,\ell,at_{c}). Since d = ℓ + τ − a d=\ell+\tau-a,

 | a ​ t c = τ ​ t c + ℓ ​ t c − d ​ t c, at_{c}=\tau t_{c}+\ell t_{c}-dt_{c}, |  |

which proves ( 14.2). On ℓ = 0 \ell=0, Hadamard division first in τ \tau and then in ( a, t c) (a,t_{c}) gives F 0 = τ ​ A + a ​ t c ​ C F_{0}=\tau A+at_{c}C. Because c = τ − a c=\tau-a, a ​ t c = τ ​ t c − c ​ t c at_{c}=\tau t_{c}-ct_{c}, yielding ( 14.3). The three integral segments are exactly the contractions stated in the theorem. ∎

Appendix C records the finite focal recurrence, one representative coefficient calculation, the two global center-domain identities, and the exact boundary between the symbolic checks and the human division argument. The raw symbolic expansion is not part of the main reading path.

The center identities must hold on the whole physical word interval. Their outer barriers can differ. On 𝒞 R \mathcal{C}_{R}, with z = 1 + y z=1+y,

 | H R ​ ( x, z) = 1 2 ​ z − 2 ​ B ​ x 2 + V R ​ ( z), V R ′ ​ ( z) = z − 2 ​ B − 1 ​ { ( z − 1) − m ​ ( z − 1) 2 }. H_{R}(x,z)=\frac{1}{2}z^{-2B}x^{2}+V_{R}(z),\qquad V_{R}^{\prime}(z)=z^{-2B-1}\{(z-1)-m(z-1)^{2}\}. |  | (14.14) |

For m > 0 m>0 the only additional finite critical point is the saddle S R = ( 0, 1 + 1 / m) S_{R}=(0,1+1/m). When B < 0 B<0, comparison with the boundary z = 0 z=0 is exact:

 | V R ​ ( 0) − V R ​ ( 1 + 1 / m) = 2 ​ ( B + m) ( − 2 ​ B) ​ ( 1 − 2 ​ B) ​ ( 2 − 2 ​ B) ​ ( 1 + m m) 1 − 2 ​ B. V_{R}(0)-V_{R}(1+1/m)=\frac{2(B+m)}{(-2B)(1-2B)(2-2B)}\left(\frac{1+m}{m}\right)^{1-2B}. |  | (14.15) |

On 𝒞 Q \mathcal{C}_{Q}, the component of { 𝒱 Q ≠ 0 } ∩ { y > − 1 } \{\mathcal{V}_{Q}\neq 0\}\cap\{y>-1\} containing the origin carries the analytic first integral. Its only extra finite singularity is

 | S Q = ( − a / B, − 1 / B) ( B < 0), S_{Q}=(-a/B,-1/B)\quad(B<0), |  | (14.16) |

a saddle on K Q = 0 K_{Q}=0. Hence a center return is the identity exactly on the connected section interval inside its maximal period annulus; its endpoint is one of

 | y = − 1, K Q = 0, S R, S Q y=-1,\qquad K_{Q}=0,\qquad S_{R},\qquad S_{Q} |  | (14.17) |

or a named compactification face.

###### Proposition 24 (Common unforced center-word domain).

Every source word admitted to Theorem 22 has nested physical domains 𝒲 − ⋐ 𝒲 + \mathcal{W}^{-}\Subset\mathcal{W}^{+}. On ℓ = 0 \ell=0, 𝒲 + \mathcal{W}^{+} is star-shaped under

 | ( τ, 0, a, t c, B) ⟼ ( q 1 ​ τ, 0, q 3 ​ a, q 4 ​ t c, B), q ∈ [0, 1] 3, (\tau,0,a,t_{c},B)\longmapsto(q_{1}\tau,0,q_{3}a,q_{4}t_{c},B),\qquad q\in[0,1]^{3}, |  | (14.18) |

every contraction has the same first-port word and positive section and all-port margins, and the two terminal faces belong to the complete center domains above. A loss at ( 14.17), a root, a previous side, or a collar side is a separately named gate cell; the return is not continued across it.

###### Proof.

For every primitive, take the complete finite union of target and competing ports fixed in Part I. On the open set where one transverse target is the first contact, minimize the entry interval widths, the strict flow coordinates along the stopped arc, the signed distances to every competing port, and both endpoint section normals. A positive minimum gives nested domains with margins 4 ​ η 4\eta and 2 ​ η 2\eta. If the minimum vanishes, its first zero is precisely a listed divider, root, center barrier, previous side, overlap, or exit face. Pulling these domains successively through the finite word gives a common first-hit domain without transporting a divider through a singular box.

It remains to check ( 14.18). With

 | β B = B ​ h, β m = m ​ h, β a = a ​ h, β c = c ​ h \beta_{B}=Bh,\quad\beta_{m}=mh,\quad\beta_{a}=a\sqrt{h},\quad\beta_{c}=c\sqrt{h} |  |

and ℓ = 0 \ell=0, the contractions satisfy

 | β B ′ = β B, β m ′ = q 4 ​ β m − ( 1 − q 4) ​ β B, β a ′ = q 3 ​ β a, β c ′ = q 1 ​ β c + ( q 1 − q 3) ​ β a. \beta_{B}^{\prime}=\beta_{B},\qquad\beta_{m}^{\prime}=q_{4}\beta_{m}-(1-q_{4})\beta_{B},\qquad\beta_{a}^{\prime}=q_{3}\beta_{a},\qquad\beta_{c}^{\prime}=q_{1}\beta_{c}+(q_{1}-q_{3})\beta_{a}. |  | (14.19) |

Thus the whole cube remains in one small scaled box. On the finite lower pieces z = s ​ Z z=sZ tends uniformly to Z x = x ​ Z Z_{x}=xZ. At the endpoints the weak bracket keeps its source sign and ± log ⁡ z \pm\log z is a strict coordinate; in the upper box the normalized equation gives W ′ ≤ − ( W 2 + R) / 2 < 0 W^{\prime}\leq-(W^{2}+R)/2<0. The finitely many overlap and regular pieces have fixed margins. Finally ( 14.14)–( 14.17) put both complete center faces inside their actual period-annulus domains. This proves the proposition. ∎

### 15 The forced lower scale and its two gate endpoints

The center division used only k = 0 k=0. We now retain the true forced variable k = ℓ / s k=\ell/s, prove that every source fixed point has bounded k k, and construct the two fixed-data survivor intervals used in ( 13.4).

###### Lemma 25 (Lower-scale localization).

There are C ℓ > 1 C_{\ell}>1 and s 1 > 0 s_{1}>0 such that every fixed point of a retained source word with 0 < s < s 1 0<s<s_{1} satisfies

 | | ℓ | ≤ C ℓ ​ s. |\ell|\leq C_{\ell}s. |  | (15.1) |

With z = s ​ Z z=sZ and ℓ = s ​ k \ell=sk, the exact lower equation is

 | d ​ Z d ​ x = k + ( x − c − 2 ​ s ​ k) ​ Z + s ⁡ ( c + s ​ k) ​ Z 2 F 0 ​ ( x) − ( 1 + 2 ​ m) ​ s ​ Z + m ​ s 2 ​ Z 2, F 0 = 1 + m + B ​ x 2 + a ​ x. \frac{dZ}{dx}=\frac{k+(x-c-2sk)Z+s(c+sk)Z^{2}}{F_{0}(x)-(1+2m)sZ+ms^{2}Z^{2}},\qquad F_{0}=1+m+Bx^{2}+ax. |  | (15.2) |

The outgoing fixed-initial and returning fixed-terminal survivor sets are intervals containing k = 0 k=0. Their intersection ℐ low \mathcal{I}_{\rm low} is an interval whose only open source-regime endpoints are the two named lower gates.

###### Proof.

On fixed lower segments the full equations give

 | x ˙ = F 0 − ( 1 + 2 ​ m) ​ z + m ​ z 2, z ˙ = ℓ + ( x − c − 2 ​ ℓ) ​ z + ( c + ℓ) ​ z 2, \dot{x}=F_{0}-(1+2m)z+mz^{2},\qquad\dot{z}=\ell+(x-c-2\ell)z+(c+\ell)z^{2}, |  |

and, after shrinking,

 | d ​ z d ​ x = ℓ + x ​ z + O ⁡ ( ϵ ⁡ ( | ℓ | + z) + z 2). \frac{dz}{dx}=\ell+xz+O(\epsilon(|\ell|+z)+z^{2}). |  | (15.3) |

For ℓ < 0 \ell<0, comparison with z x ≤ ℓ / 2 + C ​ z z_{x}\leq\ell/2+Cz forces the outgoing orbit from z ⁡ ( 0) = s z(0)=s to hit z = 0 z=0 when − ℓ > C − ​ s -\ell>C_{-}s. For ℓ > 0 \ell>0, the reversed lower piece gives

 | P ⁡ ( s, λ) ≥ e − C ​ δ ​ z ​ ( − δ) + ℓ 2 ​ C ​ ( 1 − e − C ​ δ) ≥ c δ ​ ℓ, P(s,\lambda)\geq e^{-C\delta}z(-\delta)+\frac{\ell}{2C}(1-e^{-C\delta})\geq c_{\delta}\ell, |  |

so P = s P=s is impossible when ℓ > C + ​ s \ell>C_{+}s. This proves ( 15.1).

Substitution gives ( 15.2), whose denominator is uniformly positive on the fixed lower boxes. If its right side is ℱ \mathcal{F}, direct differentiation yields

 | ∂ k ℱ = ( 1 − s ​ Z) 2 F 0 − ( 1 + 2 ​ m) ​ s ​ Z + m ​ s 2 ​ Z 2 ≥ 1 2. \partial_{k}\mathcal{F}=\frac{(1-sZ)^{2}}{F_{0}-(1+2m)sZ+ms^{2}Z^{2}}\geq\frac{1}{2}. |  | (15.4) |

The outgoing variational equation with fixed initial value is therefore strictly increasing in k k; the reversed equation with fixed terminal value has the opposite order. Each survivor set is an interval, and both contain zero. Their finite endpoints are first hits of a lower side or a fixed transfer port. Refining transfer-port faces away leaves exactly the two gate endpoints claimed. No monotonicity is asserted for a k k -dependent output of the upper map. ∎

### 16 Fold-transverse clocks and moving-boundary calculus

The naive x x -clock can vanish between a scaled lower cut and a strong section. This section supplies graph coordinates that cross that fold and records the moving entry, cut, and terminal-hit formulas required by the six-jet induction.

Put X = θ ​ x X=\theta x and u = − θ 2 ​ log ⁡ z u=-\theta^{2}\log z. On an unforced tail, the fold-transverse graph is

 | d ​ X d ​ u = − F β ​ ( X) − z + θ 2 ​ β m ​ ( 1 − z) 2 X + θ 2 ​ β c ​ ( z − 1), F β = 1 + β a ​ X + β B ​ X 2. \frac{dX}{du}=-\frac{F_{\beta}(X)-z+\theta^{2}\beta_{m}(1-z)^{2}}{X+\theta^{2}\beta_{c}(z-1)},\qquad F_{\beta}=1+\beta_{a}X+\beta_{B}X^{2}. |  | (16.1) |

Where the denominator in ( 16.1) becomes small, use the reciprocal graph

 | d ​ u d ​ X = − X + θ 2 ​ β c ​ ( z − 1) F β ​ ( X) − z + θ 2 ​ β m ​ ( 1 − z) 2. \frac{du}{dX}=-\frac{X+\theta^{2}\beta_{c}(z-1)}{F_{\beta}(X)-z+\theta^{2}\beta_{m}(1-z)^{2}}. |  | (16.2) |

The overlap cuts are fixed and transverse. On the forced tail the strict clock is instead

 | D k = X + θ 2 ​ β c ​ ( z − 1) + θ ​ s ​ k ​ ( 1 − z) 2 z. D_{k}=X+\theta^{2}\beta_{c}(z-1)+\theta sk\frac{(1-z)^{2}}{z}. |  | (16.3) |

On every radial k k -segment in the differentiated wedge, ± D k ≥ d ∗ / 2 \pm D_{k}\geq d_{*}/2. Thus the fold is a zero of the discarded x x -clock, not a singularity of the physical orbit.

###### Proposition 26 (Finite source/parameter overlap).

Before any source localization or fixed-point equation, refine a coefficient shell by the finite signed weighted charts

 | B = ρ 2 ​ B ¯, m = ρ 2 ​ m ¯, a = ρ ​ a ¯, c = ρ ​ c ¯, d = ρ ​ d ¯, q = θ ρ, B=\rho^{2}\bar{B},\quad m=\rho^{2}\bar{m},\quad a=\rho\bar{a},\quad c=\rho\bar{c},\quad d=\rho\bar{d},\qquad q=\frac{\theta}{\rho}, |  | (16.4) |

where one of | B ¯ |, | m ¯ |, | a ¯ |, | c ¯ |, | d ¯ | |\bar{B}|,|\bar{m}|,|\bar{a}|,|\bar{c}|,|\bar{d}| equals (1), with its sign retained, and q q lies in a fixed compact overlap interval. There are ten primary sign charts and finitely many tie faces. Put

 | B ^ = B θ 2, m ^ = m θ 2, a ^ = a θ, c ^ = c θ, d ^ = d θ. \widehat{B}=\frac{B}{\theta^{2}},\quad\widehat{m}=\frac{m}{\theta^{2}},\quad\widehat{a}=\frac{a}{\theta},\quad\widehat{c}=\frac{c}{\theta},\quad\widehat{d}=\frac{d}{\theta}. |  | (16.5) |

Substitution in the already fixed endpoint and upper blocks gives the exact source-normalized rows

 | N ^ e = R ⁡ { B ^ + a ^ ​ R + R 2 ​ [1 − z + θ 2 ​ m ^ ​ ( z − 1) 2] }, \widehat{N}_{e}=R\{\widehat{B}+\widehat{a}R+R^{2}[1-z+\theta^{2}\widehat{m}(z-1)^{2}]\}, |  | (16.6) |

 | z ′ = ± z + θ 2 ​ R ​ { d ^ ​ ( z − 1) 2 + c ^ ​ ( z − 1) }, z^{\prime}=\pm z+\theta^{2}R\{\widehat{d}(z-1)^{2}+\widehat{c}(z-1)\}, |  | (16.7) |

 | R ′ \displaystyle R^{\prime} | = − R ⁡ { W + d ^ + θ 2 ​ R ​ ( W + c ^) }, \displaystyle=-R\{W+\widehat{d}+\theta^{2}R(W+\widehat{c})\}, |  | (16.8) |

 | W ′ \displaystyle W^{\prime} | = m ^ − d ^ ​ W − W 2 − R \displaystyle=\widehat{m}-\widehat{d}W-W^{2}-R |  |

 |  | + θ 2 ​ { B ^ ​ W 2 + R ⁡ [( a ^ − c ^) ​ W − W 2] }. \displaystyle+\theta^{2}\{\widehat{B}W^{2}+R[(\widehat{a}-\widehat{c})W-W^{2}]\}. |  |

Consequently every coefficient shell is a restriction of one of the finite endpoint or upper-vertical regimes already listed by Proposition 5, not a case created by the source zero argument. Equations ( 16.4)–( 16.8) are coordinate substitutions of the same values ( B, m, a, c, d) (B,m,a,c,d). On chart overlaps the time multiplier is positive, and orbit uniqueness identifies the same physical first hit. The overlap therefore preserves both the original parameter and the physical point.

###### Proposition 27 (Common forced physical domain).

Fix

 | δ a = 1 8192, E − = [1 − δ a, 1 + δ a], E + = [1 − 2 ​ δ a, 1 + 2 ​ δ a]. \delta_{a}=\frac{1}{8192},\qquad E^{-}=[1-\delta_{a},1+\delta_{a}],\qquad E^{+}=[1-2\delta_{a},1+2\delta_{a}]. |  | (16.9) |

After a finite first-loss refinement, every direct phase-dominant source cell satisfies

 | | β B | + | β m | + | β a | + | β c | ≤ ϵ src, | k | ≤ C ℓ, |\beta_{B}|+|\beta_{m}|+|\beta_{a}|+|\beta_{c}|\leq\epsilon_{\rm src},\qquad|k|\leq C_{\ell}, |  | (16.10) |

and has one nested physical product tube on which the two fixed-data lower cores and tails, their inverses, the unforced action graphs, the two upper layers, the compact upper bulk, and all moving hits and cuts used below are simultaneously defined. The only domain functions allowed to vanish on a direct cell are C + C_{+} and C − C_{-}; their zero faces are no-passage faces.

At the fixed scaled cuts X = ± 1 X=\pm 1, let A ±, ∗ A_{\pm,*} denote the forced lower label expressed in the corresponding unforced label coordinate. Put

 | S β ′ ​ ( X) = X F β ​ ( X), S β ​ ( 0) = 0, σ ∗:= min β ⁡ { S β ​ ( 1), S β ​ ( − 1) } ≥ 3 8. S_{\beta}^{\prime}(X)=\frac{X}{F_{\beta}(X)},\qquad S_{\beta}(0)=0,\qquad\sigma_{*}:=\min_{\beta}\{S_{\beta}(1),S_{\beta}(-1)\}\geq\frac{3}{8}. |  | (16.11) |

Then

 | A ±, ∗ = C ± + Δ ±, ∗, | D I Δ ±, ∗ | ≤ C I θ − p n e − σ ∗ / θ 2 A_{\pm,*}=C_{\pm}+\Delta_{\pm,*},\qquad|D_{I}\Delta_{\pm,*}|\leq C_{I}\theta^{-p_{n}}e^{-\sigma_{*}/\theta^{2}} |  | (16.12) |

for every normalized derivative word D I D_{I} of total order n ≤ 6 n\leq 6, where this total includes at most two fixed-original successors. More precisely, differentiation of the ratio produces only

 | | D I ( A ±, ∗ C ± − 1) | ≤ C I θ − p n C ± − q I e − σ ∗ / θ 2, q I ≤ n + 1. \left|D_{I}\left(\frac{A_{\pm,*}}{C_{\pm}}-1\right)\right|\leq C_{I}\theta^{-p_{n}}C_{\pm}^{-q_{I}}e^{-\sigma_{*}/\theta^{2}},\qquad q_{I}\leq n+1. |  | (16.13) |

Thus every inverse gate factor is attached to a Gaussian-flat carrier; no positive lower bound for A ±, ∗ A_{\pm,*} is asserted independently of C ± C_{\pm}. On

 | 𝒲 δ a = { C + ≥ s 2 ​ δ a, C − ≥ s 2 ​ δ a } \mathcal{W}_{\delta_{a}}=\{C_{+}\geq s^{2\delta_{a}},\ C_{-}\geq s^{2\delta_{a}}\} |  | (16.14) |

the forced clocks in ( 16.3) have their stated signed margin on every radial k k -segment. Failure of ( 16.10), a section margin, or a first-port margin is assigned at its first loss to the named compact, root, side, or parameter-dominated regime; it is not retained as a direct source cell.

###### Proof.

At β = 0, k = 0 \beta=0,k=0, the lower action is X 2 / 2 X^{2}/2, the upper principal orbit is X 2 / 2 + Y = e X^{2}/2+Y=e, and fixed inner/outer graph overlaps and two fixed upper layers may be chosen for every e ∈ E + e\in E^{+}. Their graph denominators, section normals, bulk sides, and competing-port gaps have strict principal margins. Shrinking one outer normalized box and then an inner box preserves half of every one of these finitely many margins. The source-specific first-loss classification used here is the following finite list; it refines, but does not replace, the physical Part I port label.

First lost condition | Exact event | Previously constructed destination |

compact/coefficient | H = H 0 H=H_{0}, or one or more normalized coefficients first reach their fixed shell | compact analytic regime, or the finite signed overlap of Proposition 26 followed by the corresponding endpoint or upper-vertical outcome |

lower outer/inner graph | a denominator in ( 16.1)–( 16.2) vanishes, or a fixed graph side is first | endpoint root, axis, tangency, endpoint-corner, fixed overlap, or compact port |

action inverse/image | an action derivative vanishes, or its image reaches a fixed interval endpoint | the corresponding endpoint section or corner, or adjacent action shell |

entry/exit layer | a factored layer denominator, X X -side, or layer corner is first | upper-vertical nullcline or gate, ordinary port, or corner regime |

upper bulk/return | a fixed bulk side precedes return, or the return normal vanishes | upper-vertical previous-side, local-singular, collar, tangency, or equilibrium sector regime |

competing physical port | another member of the complete finite port union is first | its preassigned physical-port or local-sector regime |

divergent flight | no finite contact occurs | the endpoint root/axis or upper-vertical source-core/projective/local-sector status determined by the fixed slab |

lower survivor/simultaneous | C + = 0 C_{+}=0, C − = 0 C_{-}=0, or any nonempty subset of the preceding equalities occurs together | lower no-passage, or the labelled intersection of the same finite regime faces |

This list includes graph, denominator, layer, bulk, first-port, divergent-flight, and simultaneous losses; coefficient thresholds alone do not exhaust it. Proposition 8 supplies the finite contact alternatives and assigns every unbounded singular-sector flight its named local status. Theorem 10 then supplies the finite fixed word, status, and divider-order labels. For a sequence leaving the direct tube, pass to one such label. A bounded first stopped time converges to one of the displayed finite contacts; an unbounded time has the endpoint or upper-vertical local status supplied by Proposition 8; and simultaneous first zeros retain their finite subset label. At a coefficient shell, Proposition 26 identifies the same physical point and the same original parameter in a finite endpoint or upper-vertical chart. No connected-component finiteness is asserted. The construction uses only the physical field, fixed ports, strict margins, and that finite physical overlap, not a differentiated wedge or a fixed-point equation. This proves the product-tube assertion and the exhaustive complement policy in the statement.

It remains to justify the noncompact lower tail, where a compactness argument would be invalid. Let ρ ± \rho_{\pm} be the unforced source label on the two oriented tails and put a ± = − θ 2 ​ log ⁡ ρ ± a_{\pm}=-\theta^{2}\log\rho_{\pm}. Direct division of the unforced field in the u u -clock gives

 | a ± = u + S β ( X) + R ± ( X, u), ρ ± z = e − S β ( X) / θ 2 e − R ± ( X, u) / θ 2, | R ± | ≤ C θ 2. a_{\pm}=u+S_{\beta}(X)+R_{\pm}(X,u),\qquad\frac{\rho_{\pm}}{z}=e^{-S_{\beta}(X)/\theta^{2}}e^{-R_{\pm}(X,u)/\theta^{2}},\qquad|R_{\pm}|\leq C\theta^{2}. |  | (16.15) |

The same differentiated graph equations bound every required finite jet of R ± R_{\pm} by a power of θ − 1 \theta^{-1}. At X = ± 1 X=\pm 1, ( 16.11) therefore makes ∂ z ρ ± \partial_{z}\rho_{\pm} a polynomial factor times e − σ ∗ / θ 2 e^{-\sigma_{*}/\theta^{2}}.

Fix z b = 1 / 2 z_{b}=1/2. On z b ≤ z ≤ 1 z_{b}\leq z\leq 1, the forced perturbation of the clock is at most 2 ​ C ℓ ​ θ ​ s 2C_{\ell}\theta s, so the unforced signed margin gives ± D k ≥ 3 ​ d ∗ / 4 \pm D_{k}\geq 3d_{*}/4. Along oriented time d ​ τ = ± d ​ t d\tau=\pm dt, the exact forced-label equation is

 | d ​ A d ​ τ = ± k ( 1 − z) 2 ∂ z ρ ±, d ​ τ d ​ u = ∓ 1 θ ​ D k. \frac{dA}{d\tau}=\pm k(1-z)^{2}\partial_{z}\rho_{\pm},\qquad\frac{d\tau}{du}=\mp\frac{1}{\theta D_{k}}. |  | (16.16) |

Integrating ( 16.16) from the scaled cut to z b z_{b}, and then using the orientation-preserving fixed- x x lower hit on z ≤ z b z\leq z_{b}, gives ( 16.12). On the same radial k k -segment the gate-facing factor lies between its final value and one, and ( 16.15) gives

 | s z ≤ C θ − 8 C ± − 1 e − σ ∗ / θ 2 ≤ C θ − 8 e − ( σ ∗ − 2 δ a) / θ 2. \frac{s}{z}\leq C\theta^{-8}C_{\pm}^{-1}e^{-\sigma_{*}/\theta^{2}}\leq C\theta^{-8}e^{-(\sigma_{*}-2\delta_{a})/\theta^{2}}. |  | (16.17) |

Consequently | D k − D 0 | ≤ C ℓ ​ θ ​ s / z = o ⁡ ( 1) |D_{k}-D_{0}|\leq C_{\ell}\theta s/z=o(1), proving the forced clock margin on ( 16.14). The fixed-data variational equation is transverse at either gate, so C ± C_{\pm} is a one-sided boundary coordinate and an order- n n derivative of its reciprocal has pole order at most n + 1 n+1. Differentiating ( 16.12) now gives ( 16.13). This also proves that no inverse gate factor occurs without the flat factor displayed there. ∎

For a moving hit T ⁡ ( p) T(p) defined by Ψ ⁡ ( T ⁡ ( p), p) = 0 \Psi(T(p),p)=0, with | Ψ T | ≥ c hit > 0 |\Psi_{T}|\geq c_{\rm hit}>0, every mixed derivative satisfies the exact recursion

 | 0 = ∂ p ν [Ψ ⁡ ( T ⁡ ( p), p)] = Ψ T ​ T ν + ℬ ν, T ν = − ℬ ν Ψ T, 0=\partial_{p}^{\nu}[\Psi(T(p),p)]=\Psi_{T}T_{\nu}+\mathcal{B}_{\nu},\qquad T_{\nu}=-\frac{\mathcal{B}_{\nu}}{\Psi_{T}}, |  | (16.18) |

where ℬ ν \mathcal{B}_{\nu} contains only lower-order hit/flow derivatives. If a core/tail cut x ∗ ​ ( p) x_{*}(p) moves, differentiation of ∫ 0 x ∗ ​ ( p) K ⁡ ( x, p) ​ 𝑑 x \int_{0}^{x_{*}(p)}K(x,p)\,dx retains ( ∂ p x ∗) ​ K ​ ( x ∗) (\partial_{p}x_{*})K(x_{*}); the second derivative also retains 2 ​ ( ∂ p x ∗) ​ ( ∂ p K) ​ ( x ∗) 2(\partial_{p}x_{*})(\partial_{p}K)(x_{*}), ( ∂ p x ∗) 2 ​ K x ​ ( x ∗) (\partial_{p}x_{*})^{2}K_{x}(x_{*}), and ( ∂ p 2 x ∗) ​ K ​ ( x ∗) (\partial_{p}^{2}x_{*})K(x_{*}). These terms are exponentially flat in the weighted norms below, but they are not zero. Equations ( 16.1)–( 16.18) are the moving-boundary calculus used at every order.

### 17 Normalized six-jet closure

The common graph cover and moving-boundary calculus generate a finite derivative class through the order required by the source Rolle argument. The proof defines its alphabet and proves closure; a separate finite enumeration checks the resulting list but supplies none of the analytic estimates.

The exact source field in ( x, z) (x,z) is

 | x ˙ = 1 − z + B ​ x 2 + a ​ x + m ​ ( 1 − z) 2, z ˙ = z ⁡ { x + c ⁡ ( z − 1) } + ℓ ​ ( 1 − z) 2. \dot{x}=1-z+Bx^{2}+ax+m(1-z)^{2},\qquad\dot{z}=z\{x+c(z-1)\}+\ell(1-z)^{2}. |  | (17.1) |

On the direct phase-dominant cells of Proposition 27, retain

 | B = θ 2 ​ β B, m = θ 2 ​ β m, a = θ ​ β a, c = θ ​ β c, ℓ = s ​ k. B=\theta^{2}\beta_{B},\qquad m=\theta^{2}\beta_{m},\qquad a=\theta\beta_{a},\qquad c=\theta\beta_{c},\qquad\ell=sk. |  | (17.2) |

The commuting graph generators are

 | 𝒢 = { θ ∂ θ, ∂ k, ∂ e, ∂ β B, ∂ β m, ∂ β a, ∂ β c }. \mathcal{G}=\{\theta\partial_{\theta},\partial_{k},\partial_{e},\partial_{\beta_{B}},\partial_{\beta_{m}},\partial_{\beta_{a}},\partial_{\beta_{c}}\}. |  | (17.3) |

For a mixed word I I, put

 | κ I ​ ( k) = { | k |, I contains no ∂ k, 1, I contains ∂ k. \kappa_{I}(k)=\begin{cases}|k|,&I\text{ contains no }\partial_{k},\\ 1,&I\text{ contains }\partial_{k}.\end{cases} |  | (17.4) |

This distinction is decisive: a value or fixed-original derivative keeps the small factor | k | |k|, whereas the auxiliary derivative used in Hadamard division need not.

The finite primitive alphabet consists of:

 | LC, LT: lower fixed-initial and fixed-terminal cores, FT: fold-transverse tails in the ​ u ​ -clock, AO, AI: outer action graphs and inverse graphs, UL, UB: upper ​ Y = 0 ​ layers and compact bulk, MH, MC: moving hits and moving artificial cuts, CP: finite compositions and inverses. \begin{array}[]{ll}\mathrm{LC},\mathrm{LT}:&\text{lower fixed-initial and fixed-terminal cores},\\ \mathrm{FT}:&\text{fold-transverse tails in the }u\text{-clock},\\ \mathrm{AO},\mathrm{AI}:&\text{outer action graphs and inverse graphs},\\ \mathrm{UL},\mathrm{UB}:&\text{upper }Y=0\text{ layers and compact bulk},\\ \mathrm{MH},\mathrm{MC}:&\text{moving hits and moving artificial cuts},\\ \mathrm{CP}:&\text{finite compositions and inverses}.\end{array} |  | (17.5) |

An edge in the derivative DAG records one use of a graph equation, variation of constants, inverse differentiation, ( 16.18), Leibniz at a moving cut, or finite composition. There are 35 typed nodes and maximum depth seven. Since the derivative order is at most six and the alphabet is finite, the family of canonical commuting words is finite.

###### Theorem 28 (Six-jet closure).

On the common physical domains and the differentiated wedge

 | C + ≥ s 2 ​ δ a, C − ≥ s 2 ​ δ a, C_{+}\geq s^{2\delta_{a}},\qquad C_{-}\geq s^{2\delta_{a}}, |  | (17.6) |

all primitives in ( 17.5) close through total order six in weighted sup and L 1 L^{1} norms. In particular, with

 | p 0 = 8, p n + 1 = ( n + 2) ​ p n + 8, p_{0}=8,\qquad p_{n+1}=(n+2)p_{n}+8, |  | (17.7) |

every order- n n lower kernel is bounded by a polynomial ( 1 + x) p n (1+x)^{p_{n}} times a fixed Gaussian, every forced upper defect carries

 | s ​ κ I ​ ( k) ​ θ − p n ​ Y 2 Y + θ 2, s\kappa_{I}(k)\theta^{-p_{n}}\frac{Y^{2}}{Y+\theta^{2}}, |  | (17.8) |

and every inverse gate power is absorbed by the exponentially flat tail. All moving hits and moving cuts are included.

###### Proof.

Each graph equation has an analytic right side on one of the fixed-margin tubes. Differentiate an order- n n word. Faa di Bruno partitions it into products of lower-order state derivatives and one coefficient derivative. The coefficient table has only the following denominator types: a fixed graph normal, Y + θ 2 Y+\theta^{2}, one of the two lower factors C ± C_{\pm}, or an analytic unit. Fixed normals cost no weight. Every Euler derivative of θ 2 / ( Y + θ 2) \theta^{2}/(Y+\theta^{2}) is bounded by a constant times the same integrable kernel. A derivative of C ± − 1 C_{\pm}^{-1} has pole order at most one more than its order.

We use one weighted variational estimate repeatedly. If v ′ = A ⁡ ( t) ​ v v^{\prime}=A(t)v, W ⁡ ( t) W(t) is an invertible diagonal weight, and

 | B W = W ​ A ​ W − 1 + W ′ ​ W − 1, Λ W = ∫ ‖ B W ​ ( t) ‖ ​ 𝑑 t, B_{W}=WAW^{-1}+W^{\prime}W^{-1},\qquad\Lambda_{W}=\int\|B_{W}(t)\|\,dt, |  | (17.9) |

then the weighted fundamental matrix Z = W ​ Φ ​ W ​ ( a) − 1 Z=W\Phi W(a)^{-1} and its inverse satisfy

 | sup t { ‖ Z ⁡ ( t) ‖ + ‖ Z ​ ( t) − 1 ‖ } ≤ 2 ​ e Λ W. \sup_{t}\{\|Z(t)\|+\|Z(t)^{-1}\|\}\leq 2e^{\Lambda_{W}}. |  | (17.10) |

Indeed Z = I + ∫ B W ​ Z Z=I+\int B_{W}Z, and the same Volterra calculation applies to the inverse. Thus every appeal to variation of constants below is reduced to a displayed L 1 L^{1} coefficient bound; no unweighted compactness estimate is being substituted.

For the lower core, variation of constants gives kernels of the form

 | K ± ​ ( x) = ( 1 − z x) 2 F ⁡ ( x, z x) ​ J 0 ​ ( x, s ​ A ± ​ ( x)), ∂ x J 0 = ( ∂ z f 0) ​ J 0, K_{\pm}(x)=\frac{(1-z_{x})^{2}}{F(x,z_{x})J_{0}(x,sA_{\pm}(x))},\qquad\partial_{x}J_{0}=(\partial_{z}f_{0})J_{0}, |  | (17.11) |

and induction yields

 | | D I ​ K ± ​ ( x) | ≤ C I ​ ( 1 + x) p n ​ e − c ∗ ​ x 2. |D_{I}K_{\pm}(x)|\leq C_{I}(1+x)^{p_{n}}e^{-c_{*}x^{2}}. |  | (17.12) |

To see the required coefficient mass, put z = s ​ Z z=sZ and

 | a 0 ​ ( x) = x − c 1 + m + B ​ x 2 + a ​ x. a_{0}(x)=\frac{x-c}{1+m+Bx^{2}+ax}. |  |

Direct differentiation of the exact quotient gives

 | | ∂ Z ℱ low − a 0 ​ ( x) | \displaystyle|\partial_{Z}\mathcal{F}_{\rm low}-a_{0}(x)| | ≤ C ​ ( 1 + x) 8 ​ { z ⁡ ( x) + s ​ | k | }, \displaystyle\leq C(1+x)^{8}\{z(x)+s|k|\}, |  | (17.13) |

 | | ∂ z f 0 − a 0 ​ ( x) | \displaystyle|\partial_{z}f_{0}-a_{0}(x)| | ≤ C ​ ( 1 + x) 4 ​ z ​ ( x). \displaystyle\leq C(1+x)^{4}z(x). |  |

Conjugation by the unforced scalar fundamental factor and the Gaussian lower label imply

 | ∫ 0 θ − 1 C ​ ( 1 + x) 8 ​ { z ⁡ ( x) + s ​ | k | } ​ 𝑑 x ≤ C. \int_{0}^{\theta^{-1}}C(1+x)^{8}\{z(x)+s|k|\}\,dx\leq C. |  | (17.14) |

This is the human L 1 L^{1} estimate behind the first primitive row.

The recurrence ( 17.7) dominates one coefficient differentiation, one product partition, and the eight reserved powers at every step. The fixed-terminal system is equally explicit. For a signed tail ε ∈ { ± 1 } \varepsilon\in\{\pm 1\}, let 0 ≤ r ≤ 1 0\leq r\leq 1, put

 | u ( r) = ( 1 − r) u ε, ∗, z = e − u / θ 2, F = 1 − z + β B ​ X 2 + β a ​ X + θ 2 ​ β m ​ ( 1 − z) 2, D k = X + θ 2 ​ β c ​ ( z − 1) + θ ​ s ​ k ​ ( 1 − z) 2 z, \begin{gathered}u(r)=(1-r)u_{\varepsilon,*},\qquad z=e^{-u/\theta^{2}},\\ F=1-z+\beta_{B}X^{2}+\beta_{a}X+\theta^{2}\beta_{m}(1-z)^{2},\\ D_{k}=X+\theta^{2}\beta_{c}(z-1)+\theta sk\frac{(1-z)^{2}}{z},\end{gathered} |  | (17.15) |

and augment the orbit by

 | u r \displaystyle u_{r} | = − u ε, ∗, \displaystyle=-u_{\varepsilon,*}, | X r \displaystyle X_{r} | = u ε, ∗ ​ F D k, \displaystyle=u_{\varepsilon,*}\frac{F}{D_{k}}, | τ r \displaystyle\tau_{r} | = ε ​ u ε, ∗ θ ​ D k, \displaystyle=\frac{\varepsilon u_{\varepsilon,*}}{\theta D_{k}}, |  | (17.16) |

 | ( I 0) r \displaystyle(I_{0})_{r} | = ε ​ u ε, ∗ θ ​ D k ​ ( 1 − z) 2 ​ ∂ z ρ ε, \displaystyle=\frac{\varepsilon u_{\varepsilon,*}}{\theta D_{k}}(1-z)^{2}\partial_{z}\rho_{\varepsilon}, | ( 𝒜 T) r \displaystyle(\mathcal{A}_{T})_{r} | = ε ​ k ​ ( I 0) r. \displaystyle=\varepsilon k(I_{0})_{r}. |  |

Here u ε, ∗ > 0 u_{\varepsilon,*}>0 is the fixed terminal clock length and

 | A ε, ∗ = ρ ε ​ ( ε, u ε, ∗, p) / s. A_{\varepsilon,*}=\rho_{\varepsilon}(\varepsilon,u_{\varepsilon,*};p)/s. |  | (17.17) |

The complete entry state is

 | ( u, X, τ, I 0, 𝒜 T) ​ ( 0) = ( u ε, ∗, ε, 0, 0, A ε, ∗). (u,X,\tau,I_{0},\mathcal{A}_{T})(0)=(u_{\varepsilon,*},\varepsilon,0,0,A_{\varepsilon,*}). |  | (17.18) |

Consequently every nonempty labelled parameter word D I D_{I} starts with

 | D I ​ ( u, X, τ, I 0, 𝒜 T) ​ ( 0) = ( D I ​ u ε, ∗, 0, 0, 0, D I ​ A ε, ∗), D_{I}(u,X,\tau,I_{0},\mathcal{A}_{T})(0)=(D_{I}u_{\varepsilon,*},0,0,0,D_{I}A_{\varepsilon,*}), |  | (17.19) |

so no moving-entry jet is omitted. The weighted state

 | ( u, X, θ ​ τ, θ 3 ​ e 3 / ( 8 ​ θ 2) ​ I 0, 𝒜 T) (u,X,\theta\tau,\theta^{3}e^{3/(8\theta^{2})}I_{0},\mathcal{A}_{T}) |  | (17.20) |

turns the terminal integral into a bounded state. Differentiating ( 17.15)–( 17.16) gives the same triangular induction. Formula ( 16.18) adds only lower-order rows divided by a fixed section normal, and the exact Leibniz formulas listed after ( 16.18) add Gaussian-flat boundary rows. With the same u ε, ∗ > 0 u_{\varepsilon,*}>0, the two noncompact masses which make this weighting effective are

 | ∫ 0 u ε, ∗ θ − 2 e − u / θ 2 d u ≤ 1, | H ± | + θ 2 | ∂ X, u H ± | ≤ C e − 3 / ( 8 θ 2), \int_{0}^{u_{\varepsilon,*}}\theta^{-2}e^{-u/\theta^{2}}\,du\leq 1,\qquad|H_{\pm}|+\theta^{2}|\partial_{X,u}H_{\pm}|\leq Ce^{-3/(8\theta^{2})}, |  | (17.21) |

where H ± = ( 1 − z) 2 ​ ∂ z ρ ± H_{\pm}=(1-z)^{2}\partial_{z}\rho_{\pm}. After multiplication by the weight in ( 17.20), every tail coefficient has bounded L 1 L^{1} mass.

For completeness, if I I is a labelled derivative word and Π ⁡ ( I) \Pi(I) its set partitions, exact differentiation of any graph system Y ′ = 𝒱 ⁡ ( Y, p) Y^{\prime}=\mathcal{V}(Y,p) gives

 | ( D I Y) ′ = 𝒱 Y D I Y + 𝒱 p D I p + ∑ π ∈ Π ⁡ ( I) | π | ≥ 2 D | π | 𝒱 [Z B: B ∈ π]. (D_{I}Y)^{\prime}=\mathcal{V}_{Y}D_{I}Y+\mathcal{V}_{p}D_{I}p+\sum_{\begin{subarray}{c}\pi\in\Pi(I)\\ |\pi|\geq 2\end{subarray}}D^{|\pi|}\mathcal{V}[Z_{B}:B\in\pi]. |  | (17.22) |

Reciprocal differentiation is included by the same partition formula. If all lower words through order n n cost at most r n = p n − 4 r_{n}=p_{n}-4, a Bell term with b ≤ n + 1 b\leq n+1 lower blocks costs at most

 | b ​ r n + 8 ​ ( b + 1) ≤ ( n + 2) ​ p n + 4 = r n + 1. br_{n}+8(b+1)\leq(n+2)p_{n}+4=r_{n+1}. |  | (17.23) |

Equations ( 17.10) and ( 17.23) close the induction rather than merely count its words.

At order six at most 14 inverse gate factors occur. We retain the larger declared reserve q 6 = 448 q_{6}=448. From ( 17.6),

 | C + − q + C − − q − e − 3 / ( 8 θ 2) ≤ C e − 17 / ( 64 θ 2) ( q + + q − ≤ 448), C_{+}^{-q_{+}}C_{-}^{-q_{-}}e^{-3/(8\theta^{2})}\leq Ce^{-17/(64\theta^{2})}\quad(q_{+}+q_{-}\leq 448), |  | (17.24) |

so every inverse is paid by the same flat tail rather than declared bounded. On the upper layers, direct subtraction of forced and unforced graphs gives exactly the carrier ( 17.8); in the compact bulk ordinary variational equations preserve it. Finite compositions close the induction. The two layer kernels have literal masses

 | ∫ 0 δ θ 2 Y + θ 2 ​ 𝑑 Y = O ⁡ ( θ 2 ​ ( 1 + | log ⁡ θ |)), ∫ 0 δ Y 2 Y + θ 2 ​ 𝑑 Y ≤ C. \int_{0}^{\delta}\frac{\theta^{2}}{Y+\theta^{2}}\,dY=O(\theta^{2}(1+|\log\theta|)),\qquad\int_{0}^{\delta}\frac{Y^{2}}{Y+\theta^{2}}\,dY\leq C. |  | (17.25) |

Together with the fixed hit normal in ( 16.18), these estimates cover every layer, bulk, inverse, composition, moving-hit, and moving-cut operation in ( 17.5). Hence every primitive in the actual source word belongs to one of the 35 typed nodes listed above.

A finite computer calculation enumerates the 35 typed nodes and 167115 canonical commuting words and checks the recurrence, depth, denominator assignment, and worst exponents. It does not prove the physical domains, clock signs, Gaussian estimate ( 17.12), gate reserve ( 17.24), or first-port exhaustiveness; those are proved above and in Sections 15 – 16. ∎

Appendix B records the finite recurrence and a representative estimate. The complete enumeration is included in the electronic supplement.

### 18 Physical variational majorants

Six-jet closure is a formal operator statement until it is applied to the actual lower labels and upper passage. This section converts it into the differentiated coefficient and remainder estimates required by ( 13.15).

Let ρ + \rho_{+} be the unforced source level through a point of the outgoing lower tail, and define ρ − \rho_{-} by the reversed returning hit. Since the forced and unforced fields differ there by ℓ ( 1 − z) 2 ∂ z \ell(1-z)^{2}\partial_{z}, the exact additive labels are

 | Γ + = ∫ γ + ℓ ( 1 − z) 2 ​ ∂ z ρ + ​ 𝑑 t, Γ − = ∫ γ − ℓ reversed ( 1 − z) 2 ​ ∂ z ρ − ​ | 𝑑 t |. \Gamma_{+}=\int_{\gamma_{+}^{\ell}}(1-z)^{2}\partial_{z}\rho_{+}\,dt,\qquad\Gamma_{-}=\int_{\gamma_{-}^{\ell}}^{\rm reversed}(1-z)^{2}\partial_{z}\rho_{-}\,|dt|. |  | (18.1) |

They contain the complete endpoint tails and never divide by C ± C_{\pm}. Split each integral at x ∗ = θ − 1 x_{*}=\theta^{-1}. On the core, ( 17.12) converges with two fixed-original successors to e − x 2 / 2 e^{-x^{2}/2}. On the tail, ( 16.1)–( 16.3), ( 17.20), and ( 17.24) give a polynomial times e − 17 / ( 64 θ 2) e^{-17/(64\theta^{2})}. The moving-cut terms are bounded by the same tail. Hence, for j = 0, 1, 2 j=0,1,2,

 | | 𝔇 j ​ ( Γ ± π / 2 − 1) | ≤ η src ​ ( s), η src ​ ( s) → 0, \left|\mathfrak{D}^{j}\left(\frac{\Gamma_{\pm}}{\sqrt{\pi/2}}-1\right)\right|\leq\eta_{\rm src}(s),\qquad\eta_{\rm src}(s)\to 0, |  | (18.2) |

uniformly through either open gate side.

In the upper passage, with x = X / θ x=X/\theta, y = Y / θ 2 y=Y/\theta^{2}, the exact field is

 | X ξ \displaystyle X_{\xi} | = Y ⁡ ( β m ​ Y − 1) + θ 2 ​ ( β B ​ X 2 + β a ​ X), \displaystyle=Y(\beta_{m}Y-1)+\theta^{2}(\beta_{B}X^{2}+\beta_{a}X), |  | (18.3) |

 | Y ξ \displaystyle Y_{\xi} | = ( Y + θ 2) ​ ( X + β c ​ Y) + s ​ k θ ​ Y 2. \displaystyle=(Y+\theta^{2})(X+\beta_{c}Y)+\frac{sk}{\theta}Y^{2}. |  |

The norm used below is not an unspecified smooth norm. Let 𝒬 4, 2 \mathcal{Q}_{4,2} be the finite collection obtained from ∂ ( e, β) ν \partial_{(e,\beta)}^{\nu}, | ν | ≤ 4 |\nu|\leq 4, by applying at most two fixed-original successors and expanding them in the normalized generators by ( 18.5). Every resulting word has total order at most six. Set

 | ‖ F ‖ 4, 2:= max Q ∈ 𝒬 4, 2 ⁡ ‖ Q ​ F ‖ ∞. \|F\|_{4,2}:=\max_{Q\in\mathcal{Q}_{4,2}}\|QF\|_{\infty}. |  | (18.4) |

At fixed original parameters,

 | 𝔇 s = − s, 𝔇 h = 1 − s, 𝔇 k = k, 𝔇 = 1 − s 2 ​ h ℰ + k ∂ k, [𝔇, ∂ k] = − ∂ k, \mathfrak{D}s=-s,\quad\mathfrak{D}h=1-s,\quad\mathfrak{D}k=k,\qquad\mathfrak{D}=\frac{1-s}{2h}\mathcal{E}+k\partial_{k},\quad[\mathfrak{D},\partial_{k}]=-\partial_{k}, |  | (18.5) |

where

 | ℰ = − θ ∂ θ + 2 β B ∂ β B + 2 β m ∂ β m + β a ∂ β a + β c ∂ β c. \mathcal{E}=-\theta\partial_{\theta}+2\beta_{B}\partial_{\beta_{B}}+2\beta_{m}\partial_{\beta_{m}}+\beta_{a}\partial_{\beta_{a}}+\beta_{c}\partial_{\beta_{c}}. |  | (18.6) |

On the two Y = 0 Y=0 layers, division by Y + θ 2 Y+\theta^{2} gives an integrable unforced defect O ⁡ ( θ 2 / ( Y + θ 2)) O(\theta^{2}/(Y+\theta^{2})) and a forced defect with carrier ( 17.8). On Y ≥ δ Y Y\geq\delta_{Y}, divide time by Y > 0 Y>0; the bulk system is regular and both moving hits have fixed normals. Applying ( 16.18) through order six and composing with the action graphs yields

 | ‖ T s, β, 0 − T β ‖ 4, 2 ≤ C ​ θ 2 ​ ( 1 + | log ⁡ θ |), \|T_{s,\beta,0}-T_{\beta}\|_{4,2}\leq C\theta^{2}(1+|\log\theta|), |  | (18.7) |

 | ‖ T s, β, k − T s, β, 0 ‖ 4, 2 ≤ C ​ s ​ | k | ​ θ − 69998. \|T_{s,\beta,k}-T_{s,\beta,0}\|_{4,2}\leq Cs|k|\theta^{-69998}. |  | (18.8) |

Hadamard division in k k is legal on the survivor interval from Lemma 25. Explicitly,

 | T ~ s, β, k = T s, β, k − T s, β, 0 k = ∫ 0 1 ∂ k T s, β, t ​ k ​ 𝑑 t, max j ≤ 2 ⁡ ‖ 𝔇 j ​ T ~ s, β, k ‖ C e 4 ≤ C ​ s ​ θ − 69998. \widetilde{T}_{s,\beta,k}=\frac{T_{s,\beta,k}-T_{s,\beta,0}}{k}=\int_{0}^{1}\partial_{k}T_{s,\beta,tk}\,dt,\qquad\max_{j\leq 2}\|\mathfrak{D}^{j}\widetilde{T}_{s,\beta,k}\|_{C_{e}^{4}}\leq Cs\theta^{-69998}. |  | (18.9) |

The bare ∂ k \partial_{k} row uses κ I ​ ( k) = 1 \kappa_{I}(k)=1 in ( 17.4), while fixed-original rows retain | k | |k|. Applying ( 18.5) under the integral accounts for every commutator term; in particular no division by a vanishing k k is performed after differentiation. Since the parenthesis in ( 13.14) denotes evaluation at the moving action,

 | ℛ = − h ​ k ​ T ~ s, β, k ​ ( 1 − λ + / h), \mathcal{R}=-hk\,\widetilde{T}_{s,\beta,k}(1-\lambda_{+}/h), |  | (18.10) |

exactly. The moving argument belongs to the localized common action tube; its first two fixed-original derivatives are among the action rows in the C e 4 C_{e}^{4} norm in ( 18.9). Multiplication by h = θ − 2 h=\theta^{-2} spends the two reserved powers and gives, for j ≤ 2 j\leq 2,

 | | 𝔇 j ​ ℛ | ≤ η ⁡ ( ϵ, s) ​ ∑ i = 0 j ( | 𝔇 i ​ λ + | + | 𝔇 i ​ λ − |). |\mathfrak{D}^{j}\mathcal{R}|\leq\eta(\epsilon,s)\sum_{i=0}^{j}(|\mathfrak{D}^{i}\lambda_{+}|+|\mathfrak{D}^{i}\lambda_{-}|). |  | (18.11) |

Finally, on k = 0 k=0 apply the two Hadamard contractions of Theorem 23 to q h = [h ⁡ ( P 0) − h ⁡ ( s)] / h q_{h}=[h(P_{0})-h(s)]/h. The six-jet bounds pass under their integral formulas. The principal scaled action map vanishes on the two center faces, so its reduced rows tend to

 | A ⟶ 4 ​ 2 3, C ⟶ 8 ​ 2 15 A\longrightarrow\frac{4\sqrt{2}}{3},\qquad C\longrightarrow\frac{8\sqrt{2}}{15} |  | (18.12) |

with the two weighted successors in ( 13.12). This proves every analytic estimate used in ( 13.15).

### 19 Rebased action tubes and global fixed-point localization

The local estimates above apply only on a compact action segment. We now construct that segment before using the fixed-point equation, and prove that every source-regime fixed point lies in it. This prevents a circular appeal to derivatives near an unproved gate.

For an arbitrary positive action e e, put

 | H e = e ​ h ​ ( s), λ e = H e − 1, β ^ ​ ( e) = ( B ​ H e, m ​ H e, a ​ H e, c ​ H e, d ​ H e). H_{e}=e\,h(s),\qquad\lambda_{e}=H_{e}^{-1},\qquad\widehat{\beta}(e)=(BH_{e},mH_{e},a\sqrt{H_{e}},c\sqrt{H_{e}},d\sqrt{H_{e}}). |  | (19.1) |

Choose fixed nested intervals

 | E − ⋐ E + ⋐ E + ⁣ + ⋐ E + + + E^{-}\Subset E^{+}\Subset E^{++}\Subset E^{+++} |  | (19.2) |

around one. Here e > 0 e>0 is the arbitrary base action, whereas 𝔢 ∈ E + + + \mathfrak{e}\in E^{+++} is the local action ratio: the physical action represented in the rebased tube is e ​ 𝔢 e\mathfrak{e}. The lower action graphs and inverses are defined on fixed outer/inner graph rectangles, and the upper map on two fixed layers and a compact bulk, whenever

 | 0 < λ e ≤ λ 0, | β ^ ( e) | ≤ ϵ g, 𝔢 ∈ E + + +. 0<\lambda_{e}\leq\lambda_{0},\qquad|\widehat{\beta}(e)|\leq\epsilon_{g},\qquad\mathfrak{e}\in E^{+++}. |  | (19.3) |

Their common estimates are

 | ‖ 𝒜 ±, H − S β ^, ± ‖ C 1 + ‖ 𝒰 β ^, λ e − ℬ β ^ ‖ C 1 ≤ C ​ λ e ​ ( 1 + | log ⁡ λ e |), \|\mathcal{A}_{\pm,H}-S_{\widehat{\beta},\pm}\|_{C^{1}}+\|\mathcal{U}_{\widehat{\beta},\lambda_{e}}-\mathcal{B}_{\widehat{\beta}}\|_{C^{1}}\leq C\lambda_{e}(1+|\log\lambda_{e}|), |  | (19.4) |

with positive derivative and inverse margins. All graph denominators, section normals, side distances, and first-port distances in ( 19.3) are independent of C ± C_{\pm}. The exact rebased identity is

 | T s, β, k ​ ( e) e = ( 𝒜 −, H e ∘ 𝒰 β ^ ​ ( e), λ e ∘ 𝒜 +, H e − 1) ​ ( 1). \frac{T_{s,\beta,k}(e)}{e}=\left(\mathcal{A}_{-,H_{e}}\circ\mathcal{U}_{\widehat{\beta}(e),\lambda_{e}}\circ\mathcal{A}_{+,H_{e}}^{-1}\right)(1). |  | (19.5) |

Indeed, on the outer lower graph use u = − λ e ​ log ⁡ z u=-\lambda_{e}\log z; on the inner graph use X X. Their denominators have fixed opposite margins on the chosen overlap. On an upper layer, the only nonuniform integral is

 | ∫ 0 δ λ e Y + λ e ​ 𝑑 Y = O ⁡ ( λ e ​ ( 1 + | log ⁡ λ e |)). \int_{0}^{\delta}\frac{\lambda_{e}}{Y+\lambda_{e}}\,dY=O(\lambda_{e}(1+|\log\lambda_{e}|)). |  |

In the bulk the limiting system is X ′ = − 1 X^{\prime}=-1, Y ′ = X Y^{\prime}=X. A Gronwall estimate preserves every side buffer and gives exactly one transverse exit. These estimates prove ( 19.4) and the common product tube.

###### Proposition 29 (Global source localization).

After a finite source/parameter refinement, either a middle orbit first enters a named compact or parameter-dominated regime, or it remains direct and

 | | T s, β, k ​ ( e) e − 1 | ≤ η g, η g → 0. \left|\frac{T_{s,\beta,k}(e)}{e}-1\right|\leq\eta_{g},\qquad\eta_{g}\to 0. |  | (19.6) |

For every fixed point of the direct source word,

 | e in = 1 − λ + / h, e out = 1 + λ − / h e_{\rm in}=1-\lambda_{+}/h,\qquad e_{\rm out}=1+\lambda_{-}/h |  |

satisfy

 | | e in − 1 | + | e out − 1 | < δ a / 2. |e_{\rm in}-1|+|e_{\rm out}-1|<\delta_{a}/2. |  | (19.7) |

Moreover

 | C + ≥ s 2 ​ δ a, C − ≥ s 2 ​ δ a. C_{+}\geq s^{2\delta_{a}},\qquad C_{-}\geq s^{2\delta_{a}}. |  | (19.8) |

The statements are uniform as either open gate is approached; on the gate itself the corresponding strong first hit is absent.

###### Proof.

The refinement in the statement is made before any differentiated fixed-point estimate. For every base action e > 0 e>0, follow the same original-parameter stopped flight and take the first of the alternatives

 | ( i) H e < H 0, ( ii) H e ≥ H 0 and one scaled coefficient threshold, side, root, or first-port status is reached, ( iii) H e ≥ H 0, | β ^ ( e) | < ϵ g, and the direct stopped status persists. \begin{array}[]{ll}\mathrm{(i)}&H_{e}<H_{0},\\ \mathrm{(ii)}&H_{e}\geq H_{0}\text{ and one scaled coefficient threshold, side, root, or first-port status is reached},\\ \mathrm{(iii)}&H_{e}\geq H_{0},\ |\widehat{\beta}(e)|<\epsilon_{g},\text{ and the direct stopped status persists}.\end{array} |  | (19.9) |

This is the pre-SAL regime refinement supplied by the stopped first-hit and finite singular-alphabet results, Propositions 8 and 5, together with the explicit primitive regime rows ( 17.1)–( 17.5) of Theorem 28. Its post-threshold destinations are exactly the compact, hyperbolic, central, mixed, and terminal regimes listed after the regime table at the start of Part I. This refinement uses neither the differentiated wedge ( 17.6) nor a fixed-point equation. For fixed original parameters, H e = e ​ h ​ ( s) H_{e}=e\,h(s) and the five moduli in β ^ ​ ( e) \widehat{\beta}(e) are monotone in e e or e \sqrt{e}, unless identically zero, so each displayed threshold is crossed at most once. Cases (i) and (ii) are named compact or parameter-dominated chart–words.

In case (iii), apply the rebased product tube with base action e e and local ratio 𝔢 = 1 \mathfrak{e}=1. The fixed graph, side, section-normal, and first-port margins used in ( 19.4) were established directly from the rebased lower layers and upper bulk; none depends on C ± C_{\pm}. Thus ( 19.5) and ( 19.4) give ( 19.6) for arbitrary base e e, without assuming that e e is already near one.

At a fixed point, T ⁡ ( e in) = e out T(e_{\rm in})=e_{\rm out}. The elementary gate relations imply, for k > 0 k>0,

 | 1 ≤ e out ≤ 1 + η g, 1 1 + η g ≤ e in ≤ 1, 1\leq e_{\rm out}\leq 1+\eta_{g},\qquad\frac{1}{1+\eta_{g}}\leq e_{\rm in}\leq 1, |  |

and the reversed inequalities hold for k < 0 k<0. Shrinking η g \eta_{g} proves ( 19.7). Since λ ± = ± log ⁡ C ± + O ⁡ ( s ​ | C ± − 1 |) \lambda_{\pm}=\pm\log C_{\pm}+O(s|C_{\pm}-1|), ( 19.7) gives | log ⁡ C ± | ≤ δ a ​ h + O ⁡ ( 1) |\log C_{\pm}|\leq\delta_{a}h+O(1), and hence ( 19.8) after shrinking. Thus localization is logically prior to every use of the wedge ( 17.6). ∎

### 20 Proof of the matched preparation and the source zero theorem

We now derive ( 13.15) from the physical maps, then prove the ambient source bound stated in Theorem 30. The argument uses exact gate variables throughout; no fixed approximate denominator is substituted near a gate.

###### Proof of Theorem 22.

Every map in ( 13.3) is an orientation-preserving first hit on the common domains. The monotonicity ( 15.4), applied only to the outgoing fixed-initial problem and the reversed fixed-terminal problem, proves the signs and exact Hadamard formulas ( 13.5). It is never applied to an output of M ℓ M^{\ell}. Equation ( 13.7) then gives

 | e + ​ ( J + ℓ ​ ( s)) = 1 − λ + / h, e − ​ ( ( J − ℓ) − 1 ​ ( s)) = 1 + λ − / h, e_{+}(J_{+}^{\ell}(s))=1-\lambda_{+}/h,\qquad e_{-}((J_{-}^{\ell})^{-1}(s))=1+\lambda_{-}/h, |  |

and therefore ( 13.10). Proposition 29 places the whole action secant inside the domain of ( 18.7)–( 18.11).

For k = 0 k=0, the return is the identity on both complete center slices. Theorem 23, applied under the common contractions, gives ( 13.11), and Section 18 gives ( 13.12). Subtract ( 13.10) from T s, β, 0 ​ ( 1) = 1 + G 0 / h T_{s,\beta,0}(1)=1+G_{0}/h, add and subtract T s, β, 0 ​ ( 1 − λ + / h) T_{s,\beta,0}(1-\lambda_{+}/h), and multiply by h h. The result is exactly ( 13.15). Since h ′ ​ ( s) ≠ 0 h^{\prime}(s)\neq 0 and every map in ( 13.3) is a local diffeomorphism, multiplicity is preserved. ∎

Put

 | Φ = 𝒯 s, β ​ ( λ +) + λ − + ℛ. \Phi=\mathcal{T}_{s,\beta}(\lambda_{+})+\lambda_{-}+\mathcal{R}. |  | (20.1) |

The lower estimate ( 18.2) must be used at the actual gates. Set

 | a + = k ​ Γ +, a − = k ​ Γ −, C + = 1 + a + > 0, C − = 1 − a − > 0. a_{+}=k\Gamma_{+},\qquad a_{-}=k\Gamma_{-},\qquad C_{+}=1+a_{+}>0,\qquad C_{-}=1-a_{-}>0. |  | (20.2) |

With u ± = 𝔇 ​ Γ ± / Γ ± u_{\pm}=\mathfrak{D}\Gamma_{\pm}/\Gamma_{\pm} and v ± = 𝔇 2 ​ Γ ± / Γ ± v_{\pm}=\mathfrak{D}^{2}\Gamma_{\pm}/\Gamma_{\pm}, ( 18.2) makes | u ± | + | v ± | |u_{\pm}|+|v_{\pm}| arbitrarily small. Direct differentiation gives

 | 𝔇 ​ log ⁡ C + = a + ​ ( 1 + u +) C +, 𝔇 ⁡ ( − log ⁡ C −) = a − ​ ( 1 + u −) C −, \mathfrak{D}\log C_{+}=\frac{a_{+}(1+u_{+})}{C_{+}},\qquad\mathfrak{D}(-\log C_{-})=\frac{a_{-}(1+u_{-})}{C_{-}}, |  | (20.3) |

and

 | 𝔇 2 ​ log ⁡ C + = a + C + 2 ​ { 1 + 2 ​ u + + v + + a + ​ ( v + − u + 2) }, \mathfrak{D}^{2}\log C_{+}=\frac{a_{+}}{C_{+}^{2}}\{1+2u_{+}+v_{+}+a_{+}(v_{+}-u_{+}^{2})\}, |  | (20.4) |

 | 𝔇 2 ​ ( − log ⁡ C −) = a − C − 2 ​ { 1 + 2 ​ u − + v − + a − ​ ( u − 2 − v −) }. \mathfrak{D}^{2}(-\log C_{-})=\frac{a_{-}}{C_{-}^{2}}\{1+2u_{-}+v_{-}+a_{-}(u_{-}^{2}-v_{-})\}. |  | (20.5) |

In exact gate variables,

 | λ + = log ⁡ ( 1 + a +) − s ​ a +, λ − = − log ⁡ ( 1 − a −) − s ​ a −. \lambda_{+}=\log(1+a_{+})-sa_{+},\qquad\lambda_{-}=-\log(1-a_{-})-sa_{-}. |  | (20.6) |

If b ± = 𝔇 ​ a ± b_{\pm}=\mathfrak{D}a_{\pm} and c ± = 𝔇 2 ​ a ± c_{\pm}=\mathfrak{D}^{2}a_{\pm}, direct differentiation gives

 | 𝔇 ​ λ + \displaystyle\mathfrak{D}\lambda_{+} | = b + 1 + a + + s ⁡ ( a + − b +), \displaystyle=\frac{b_{+}}{1+a_{+}}+s(a_{+}-b_{+}), | 𝔇 2 ​ λ + \displaystyle\mathfrak{D}^{2}\lambda_{+} | = c + 1 + a + − b + 2 ( 1 + a +) 2 + s ⁡ ( − a + + 2 ​ b + − c +), \displaystyle=\frac{c_{+}}{1+a_{+}}-\frac{b_{+}^{2}}{(1+a_{+})^{2}}+s(-a_{+}+2b_{+}-c_{+}), |  | (20.7) |

 | 𝔇 ​ λ − \displaystyle\mathfrak{D}\lambda_{-} | = b − 1 − a − + s ⁡ ( a − − b −), \displaystyle=\frac{b_{-}}{1-a_{-}}+s(a_{-}-b_{-}), | 𝔇 2 ​ λ − \displaystyle\mathfrak{D}^{2}\lambda_{-} | = c − 1 − a − + b − 2 ( 1 − a −) 2 + s ⁡ ( − a − + 2 ​ b − − c −). \displaystyle=\frac{c_{-}}{1-a_{-}}+\frac{b_{-}^{2}}{(1-a_{-})^{2}}+s(-a_{-}+2b_{-}-c_{-}). |  |

Because s ​ k = ℓ sk=\ell is fixed by 𝔇 \mathfrak{D}, the corrections are exactly

 | 𝔇 ⁡ ( − s ​ a ±) = − s ​ a ± ​ u ±, 𝔇 2 ​ ( − s ​ a ±) = − s ​ a ± ​ v ±. \mathfrak{D}(-sa_{\pm})=-sa_{\pm}u_{\pm},\qquad\mathfrak{D}^{2}(-sa_{\pm})=-sa_{\pm}v_{\pm}. |  | (20.8) |

Thus they spend the same actual denominator reserve as ( 20.3)–( 20.5), with the correct sign at both gates. After the lower-kernel modulus in ( 18.2) is fixed sufficiently small, all three rows have the sign of k k and satisfy

 | | λ ± | ≤ 5 2 ​ | 𝔇 ​ λ ± |, | 𝔇 ​ λ ± | ≤ 5 2 ​ | 𝔇 2 ​ λ ± |, | 𝔇 ​ λ ± | 2 | 𝔇 2 ​ λ ± | ≤ 5 4. |\lambda_{\pm}|\leq\frac{5}{2}|\mathfrak{D}\lambda_{\pm}|,\qquad|\mathfrak{D}\lambda_{\pm}|\leq\frac{5}{2}|\mathfrak{D}^{2}\lambda_{\pm}|,\qquad\frac{|\mathfrak{D}\lambda_{\pm}|^{2}}{|\mathfrak{D}^{2}\lambda_{\pm}|}\leq\frac{5}{4}. |  | (20.9) |

These comparisons remain uniform as the allowed exact denominator tends to zero.

Write

 | 𝒯 s, β ​ ( λ +) = λ + ​ U, U = ∫ 0 1 ( T s, β, 0) e ​ ( 1 − t ​ λ + / h) ​ 𝑑 t. \mathcal{T}_{s,\beta}(\lambda_{+})=\lambda_{+}U,\qquad U=\int_{0}^{1}(T_{s,\beta,0})_{e}(1-t\lambda_{+}/h)\,dt. |  | (20.10) |

Put q + = λ + / h q_{+}=\lambda_{+}/h, and let a dot denote the total fixed-original derivative of T = T s, β, 0 T=T_{s,\beta,0} at fixed action. The moving evaluation has the exact derivatives

 | 𝔇 ​ q + = 𝔇 ​ λ + h − ( 1 − s) ​ λ + h 2, \mathfrak{D}q_{+}=\frac{\mathfrak{D}\lambda_{+}}{h}-\frac{(1-s)\lambda_{+}}{h^{2}}, |  | (20.11) |

 | 𝔇 2 ​ q + = 𝔇 2 ​ λ + h − 2 ​ ( 1 − s) ​ 𝔇 ​ λ + h 2 − s ​ λ + h 2 + 2 ​ ( 1 − s) 2 ​ λ + h 3, \mathfrak{D}^{2}q_{+}=\frac{\mathfrak{D}^{2}\lambda_{+}}{h}-\frac{2(1-s)\mathfrak{D}\lambda_{+}}{h^{2}}-\frac{s\lambda_{+}}{h^{2}}+\frac{2(1-s)^{2}\lambda_{+}}{h^{3}}, |  | (20.12) |

and

 | 𝔇 ​ U = ∫ 0 1 { T ˙ e − t ​ T e ​ e ​ 𝔇 ​ q + } ​ 𝑑 t, \mathfrak{D}U=\int_{0}^{1}\{\dot{T}_{e}-tT_{ee}\mathfrak{D}q_{+}\}\,dt, |  | (20.13) |

 | 𝔇 2 ​ U = ∫ 0 1 { T ¨ e − 2 ​ t ​ T ˙ e ​ e ​ 𝔇 ​ q + − t ​ T e ​ e ​ 𝔇 2 ​ q + + t 2 ​ T e ​ e ​ e ​ ( 𝔇 ​ q +) 2 } ​ 𝑑 t. \mathfrak{D}^{2}U=\int_{0}^{1}\{\ddot{T}_{e}-2t\dot{T}_{ee}\mathfrak{D}q_{+}-tT_{ee}\mathfrak{D}^{2}q_{+}+t^{2}T_{eee}(\mathfrak{D}q_{+})^{2}\}\,dt. |  | (20.14) |

In particular, the T e ​ e ​ e ​ ( 𝔇 ​ q +) 2 T_{eee}(\mathfrak{D}q_{+})^{2} term, both derivatives of h − 1 h^{-1}, and both moving-evaluation terms are present. Equations ( 18.7), ( 19.7), and the prescribed limit order make

 | max ⁡ { | T e − 1 |, | T e ​ e |, | T e ​ e ​ e |, L ​ | T ˙ e |, L ​ | T ˙ e ​ e |, L 2 ​ | T ¨ e | } ≤ 10 − 3. \max\{|T_{e}-1|,|T_{ee}|,|T_{eee}|,L|\dot{T}_{e}|,L|\dot{T}_{ee}|,L^{2}|\ddot{T}_{e}|\}\leq 10^{-3}. |  | (20.15) |

Combining ( 20.9)–( 20.15) in the product rules for E 𝒯 = λ + ​ ( U − 1) E_{\mathcal{T}}=\lambda_{+}(U-1) gives

 | | E 𝒯 | ≤ 10 − 3 ​ | λ + |, | 𝔇 ​ E 𝒯 | ≤ 2 ⋅ 10 − 3 ​ | 𝔇 ​ λ + |, | 𝔇 2 ​ E 𝒯 | ≤ 3 ⋅ 10 − 3 ​ | 𝔇 2 ​ λ + |. |E_{\mathcal{T}}|\leq 10^{-3}|\lambda_{+}|,\quad|\mathfrak{D}E_{\mathcal{T}}|\leq 2\cdot 10^{-3}|\mathfrak{D}\lambda_{+}|,\quad|\mathfrak{D}^{2}E_{\mathcal{T}}|\leq 3\cdot 10^{-3}|\mathfrak{D}^{2}\lambda_{+}|. |  | (20.16) |

Equation ( 18.11) gives the same relative smallness for ℛ \mathcal{R}. Consequently, after the normalized parameter box is shrunk, the fixed Gaussian cutoff is chosen, and only then s 0 s_{0} is chosen,

 | sign ⁡ ( Φ, 𝔇 ​ Φ, 𝔇 2 ​ Φ) = sign ⁡ k, | 𝔇 2 ​ Φ | ≥ 1 3 ​ | 𝔇 ​ Φ | ≥ 1 9 ​ | k |. \operatorname{sign}(\Phi,\mathfrak{D}\Phi,\mathfrak{D}^{2}\Phi)=\operatorname{sign}k,\qquad|\mathfrak{D}^{2}\Phi|\geq\frac{1}{3}|\mathfrak{D}\Phi|\geq\frac{1}{9}|k|. |  | (20.17) |

All constants are independent of C + − 1 C_{+}^{-1} and C − − 1 C_{-}^{-1}.

###### Theorem 30 (Matched source zero theorem).

Every unforced-center-complete direct source chart–word has at most two isolated fixed points, counted with multiplicity, on each noncompact normalized-action cell. This bound is locally uniform in all five original parameters and as either lower factor tends to its open gate. The gate face has no full-lap word. A bounded section piece has an independent analytic Weierstrass bound, and an exact center face is an identity with no isolated member.

###### Proof.

Divide ( 13.15) by the positive function f 1 = L 3 / 2 ​ A f_{1}=L^{3/2}A, and put

 | q = L 5 / 2 ​ C L 3 / 2 ​ A = L ​ C A, g = Φ L 3 / 2 ​ A. q=\frac{L^{5/2}C}{L^{3/2}A}=L\frac{C}{A},\qquad g=\frac{\Phi}{L^{3/2}A}. |  |

The rate estimate ( 13.12) gives

 | 𝔇 ​ q > c q > 0, 𝔇 2 ​ q = O ⁡ ( ( ϵ + o ⁡ ( 1)) / L). \mathfrak{D}q>c_{q}>0,\qquad\mathfrak{D}^{2}q=O((\epsilon+o(1))/L). |  | (20.18) |

Equation ( 20.17) and two differentiations give

 | 𝔇 2 ​ g = 1 L 7 / 2 ​ A ​ { L 2 ​ 𝔇 2 ​ Φ − 3 ​ L ​ 𝔇 ​ Φ + 15 4 ​ Φ + E div }, \mathfrak{D}^{2}g=\frac{1}{L^{7/2}A}\{L^{2}\mathfrak{D}^{2}\Phi-3L\mathfrak{D}\Phi+\tfrac{15}{4}\Phi+E_{\rm div}\}, |  | (20.19) |

where | E div | ≤ C ⁡ ( ϵ + o ⁡ ( 1)) ​ { L ​ | 𝔇 ​ Φ | + | Φ | } |E_{\rm div}|\leq C(\epsilon+o(1))\{L|\mathfrak{D}\Phi|+|\Phi|\}. Hence

 | d 2 ​ g d ​ q 2 = ( 𝔇 2 ​ g) ​ ( 𝔇 ​ q) − ( 𝔇 ​ g) ​ ( 𝔇 2 ​ q) ( 𝔇 ​ q) 3 \frac{d^{2}g}{dq^{2}}=\frac{(\mathfrak{D}^{2}g)(\mathfrak{D}q)-(\mathfrak{D}g)(\mathfrak{D}^{2}q)}{(\mathfrak{D}q)^{3}} |  | (20.20) |

is nonzero and has the sign of k k for large L L. After division, ( 13.15) is

 | τ + σ 0 ​ q − g = 0. \tau+\sigma_{0}q-g=0. |  |

Three zeros would give, by two Rolle steps in the monotone coordinate q q, a zero of ( 20.20), a contradiction. If k = 0 k=0, then Φ = 0 \Phi=0 and the equation is affine in q q, unless τ = σ 0 = 0 \tau=\sigma_{0}=0; the latter is one of the two center identities. The compact range of L L is a jointly analytic physical tube and is covered by Weierstrass preparation. This proves the theorem. ∎

### 21 The exact mixed persistent endpoint

We consider a retained itinerary with a persistent nonhyperbolic horizontal endpoint and at most the upper vertical D D -collision as an internal central label. The result is uniform in the resolved parameters and named specializations within the face B = a = 0 B=a=0, but does not assert a direct Dulac estimate on an open five-parameter neighborhood. Its proof is intrinsic to that face; it is not obtained by taking κ ↓ 0 \kappa\downarrow 0 in the positive root theorem.

First consider B = 0 B=0, a ≠ 0 a\neq 0. In the two horizontal endpoint charts, with K = 1 − z + m ​ ( z − 1) 2 > 0 K=1-z+m(z-1)^{2}>0, the exact radial equations are

 | p +: r ′ = − a ​ r 2 − r 3 ​ K, z ′ = z + O ⁡ ( r), p −: r ′ = − a ​ r 2 + r 3 ​ K, z ′ = − z + O ⁡ ( r). \begin{array}[]{lll}p_{+}:&r^{\prime}=-ar^{2}-r^{3}K,&z^{\prime}=z+O(r),\\ p_{-}:&r^{\prime}=-ar^{2}+r^{3}K,&z^{\prime}=-z+O(r).\end{array} |  | (21.1) |

For one sign of a a, the positive endpoint has the required weak entry and strong exit while the negative endpoint points toward its corner; for the other sign the roles reverse. A source-order lap uses both boxes, so no retained full lap exists. We henceforth take B = a = 0 B=a=0.

Put m = − p m=-p. The exact family in z = 1 + y > 0 z=1+y>0 is

 | x ˙ = − y − p ​ y 2, y ˙ = ( 1 + y) ​ ( x + d ​ y) − ℓ ​ y. \dot{x}=-y-py^{2},\qquad\dot{y}=(1+y)(x+dy)-\ell y. |  | (21.2) |

The following physical lemma supplies the zero count on the complete collision/no-root cone.

###### Lemma 31 (Full-ratio Lienard–Dulac bound).

There are d 0 > 0 d_{0}>0, 0 < p 0 < 1 0<p_{0}<1, and

 | 2 9 < q 0 < 1 4, p 0 + 2 ​ d 0 2 9 < 1, \frac{2}{9}<q_{0}<\frac{1}{4},\qquad p_{0}+\frac{2d_{0}^{2}}{9}<1, |  | (21.3) |

such that, whenever

 | | d | < d 0, 0 < p < p 0, p ≥ q 0 ​ d 2, |d|<d_{0},\qquad 0<p<p_{0},\qquad p\geq q_{0}d^{2}, |  | (21.4) |

the field ( 21.2) has at most one isolated periodic orbit in z > 0 z>0, for every real ℓ \ell. The statement is uniform through p = d 2 / 4 p=d^{2}/4, both adjacent sides, and every value of ℓ / d \ell/d.

###### Proof.

Set

 | v = x + d ​ y − ℓ ​ y 1 + y, d ​ τ = ( 1 + y) ​ d ​ t, g ⁡ ( y) = y ⁡ ( 1 + p ​ y) 1 + y. v=x+dy-\frac{\ell y}{1+y},\qquad d\tau=(1+y)dt,\qquad g(y)=\frac{y(1+py)}{1+y}. |  |

The time change is positive, and direct differentiation gives

 | y τ = v, v τ = − g ⁡ ( y) + ( d − ℓ ( 1 + y) 2) ​ v. y_{\tau}=v,\qquad v_{\tau}=-g(y)+\left(d-\frac{\ell}{(1+y)^{2}}\right)v. |  | (21.5) |

For E = v 2 / 2 + ∫ 0 y g ⁡ ( r) ​ 𝑑 r E=v^{2}/2+\int_{0}^{y}g(r)\,dr,

 | E τ = ( d − ℓ ( 1 + y) 2) ​ v 2. E_{\tau}=\left(d-\frac{\ell}{(1+y)^{2}}\right)v^{2}. |  | (21.6) |

The involution ( x, t, d, ℓ, p) ↦ ( − x, − t, − d, − ℓ, p) (x,t,d,\ell,p)\mapsto(-x,-t,-d,-\ell,p) allows d ≥ 0 d\geq 0. Equation ( 21.6) excludes periodic orbits when d ​ ℓ ≤ 0 d\ell\leq 0, except that d = ℓ = 0 d=\ell=0 gives period annuli and no isolated member. It remains to take d, ℓ > 0 d,\ell>0 and set

 | ϵ = ℓ d, δ = d 2. \epsilon=\frac{\ell}{d},\qquad\delta=d^{2}. |  | (21.7) |

If ϵ ≥ 1 \epsilon\geq 1, the positive multiplier ℬ 0 = e 2 ​ d ​ x / ( 1 + y) \mathcal{B}_{0}=e^{2dx}/(1+y) satisfies

 | div ⁡ ( ℬ 0 ​ X) ℬ 0 = d ⁡ ( 1 − y − ϵ 1 + y − 2 ​ p ​ y 2) ≤ 0, \frac{\operatorname{div}(\mathcal{B}_{0}X)}{\mathcal{B}_{0}}=d\left(1-y-\frac{\epsilon}{1+y}-2py^{2}\right)\leq 0, |  | (21.8) |

and is not identically zero on any open set. When ϵ = 1 \epsilon=1, equality holds on the line y = 0 y=0, but the divergence is strictly negative off that line; Green’s formula still excludes a periodic orbit. Suppose 0 < ϵ < 1 0<\epsilon<1. Put

 | H ⁡ ( y) = d ​ y − ℓ ​ y 1 + y, u = v − H ⁡ ( y), F = − H. H(y)=dy-\frac{\ell y}{1+y},\qquad u=v-H(y),\qquad F=-H. |  |

Then

 | y τ = u − F ⁡ ( y), u τ = − g ⁡ ( y). y_{\tau}=u-F(y),\qquad u_{\tau}=-g(y). |  | (21.9) |

Writing ζ = 1 + y \zeta=1+y, define

 | ϕ ⁡ ( ζ) = ( ζ − 1) ​ ( ϵ ζ − 1), F = d ​ ϕ, \phi(\zeta)=(\zeta-1)\left(\frac{\epsilon}{\zeta}-1\right),\qquad F=d\phi, |  |

 | G ⁡ ( y) = ∫ 0 y g ⁡ ( r) ​ 𝑑 r = ( 1 − p) ​ { ζ − 1 − log ⁡ ζ } + p 2 ​ ( ζ − 1) 2. G(y)=\int_{0}^{y}g(r)\,dr=(1-p)\{\zeta-1-\log\zeta\}+\frac{p}{2}(\zeta-1)^{2}. |  | (21.10) |

Now set

 | 𝒱 = u 2 − 2 3 ​ u ​ F − 1 9 ​ F 2 + 2 ​ G. \mathcal{V}=u^{2}-\frac{2}{3}uF-\frac{1}{9}F^{2}+2G. |  | (21.11) |

A direct expansion, retaining the divergence term, gives

 | X ​ 𝒱 − 2 3 ​ ( div ⁡ X) ​ 𝒱 = 4 ​ d 3 ​ 𝒦, X\mathcal{V}-\frac{2}{3}(\operatorname{div}X)\mathcal{V}=\frac{4d}{3}\mathcal{K}, |  | (21.12) |

where

 | 𝒦 = W + δ 9 ​ ϕ 2 ​ ϕ ′, W = G ​ ϕ ′ − ϕ ​ g, ϕ ′ = ϵ ζ 2 − 1. \mathcal{K}=W+\frac{\delta}{9}\phi^{2}\phi^{\prime},\qquad W=G\phi^{\prime}-\phi g,\qquad\phi^{\prime}=\frac{\epsilon}{\zeta^{2}}-1. |  | (21.13) |

The function W W is affine separately in p p and ϵ \epsilon. Its four corner values on the unit square are

 | ϵ = 0 ϵ = 1 p = 0 log ⁡ ζ − 1 + ζ − 1 ( ζ − 1) ​ { ( ζ + 1) ​ log ⁡ ζ − 2 ​ ( ζ − 1) } / ζ 2 p = 1 ( ζ − 1) 2 / 2 ( ζ − 1) 4 / ( 2 ​ ζ 2). \begin{array}[]{c|c|c}&\epsilon=0&\epsilon=1\\ \hline\cr p=0&\log\zeta-1+\zeta^{-1}&(\zeta-1)\{(\zeta+1)\log\zeta-2(\zeta-1)\}/\zeta^{2}\\[2.84526pt] p=1&(\zeta-1)^{2}/2&(\zeta-1)^{4}/(2\zeta^{2}).\end{array} |  | (21.14) |

All are positive away from ζ = 1 \zeta=1. For the only nonimmediate entry, differentiate log ⁡ ζ − 2 ​ ( ζ − 1) / ( ζ + 1) \log\zeta-2(\zeta-1)/(\zeta+1); its derivative is ( ζ − 1) 2 / [ζ ​ ( ζ + 1) 2] (\zeta-1)^{2}/[\zeta(\zeta+1)^{2}]. Multi-affine interpolation gives

 | W ≥ p ​ ( ζ − 1) 2 2 ​ ζ 2 ​ { ζ 2 − 2 ​ ϵ ​ ζ + ϵ }. W\geq\frac{p(\zeta-1)^{2}}{2\zeta^{2}}\{\zeta^{2}-2\epsilon\zeta+\epsilon\}. |  | (21.15) |

When ζ 2 > ϵ \zeta^{2}>\epsilon, use

 |  | ζ 2 ​ ( ζ 2 − 2 ​ ϵ ​ ζ + ϵ) − ( ζ − ϵ) 2 ​ ( ζ 2 − ϵ) \displaystyle\zeta^{2}(\zeta^{2}-2\epsilon\zeta+\epsilon)-(\zeta-\epsilon)^{2}(\zeta^{2}-\epsilon) |  | (21.16) |

 |  | = ϵ ⁡ { ( 2 − ϵ) ​ ζ 2 − 2 ​ ϵ ​ ζ + ϵ 2 } ≥ 0. \displaystyle=\epsilon\{(2-\epsilon)\zeta^{2}-2\epsilon\zeta+\epsilon^{2}\}\geq 0. |  |

Equations ( 21.4), ( 21.15), and ( 21.16) imply 𝒦 > 0 \mathcal{K}>0 for ζ ≠ 1 \zeta\neq 1. This is the full-ratio estimate; no boundedness of ℓ / d \ell/d was used.

Completing the square,

 | 𝒱 = ( u − F / 3) 2 + Q ⁡ ( ζ), Q = 2 ​ G − 2 ​ δ 9 ​ ϕ 2. \mathcal{V}=(u-F/3)^{2}+Q(\zeta),\qquad Q=2G-\frac{2\delta}{9}\phi^{2}. |  | (21.17) |

The inequalities in ( 21.3)–( 21.4) give Q > 0 Q>0 for ζ ≥ ϵ \zeta\geq\epsilon, ζ ≠ 1 \zeta\neq 1. On 0 < ζ < ϵ 0<\zeta<\epsilon, Q → − ∞ Q\to-\infty at zero, and at a zero of Q Q direct differentiation gives Q ′ > 0 Q^{\prime}>0. Indeed this reduces to

 | 2 ​ G − ( 1 − ζ) 2 ​ { 1 − p ⁡ ( 1 − ζ) } > 0, 2G-(1-\zeta)^{2}\{1-p(1-\zeta)\}>0, |  |

which follows from

 | ( 1 − p) ​ { 2 ​ ( ζ − 1 − log ⁡ ζ) − ( 1 − ζ) 2 } + p ​ ( 1 − ζ) 3 > 0. (1-p)\{2(\zeta-1-\log\zeta)-(1-\zeta)^{2}\}+p(1-\zeta)^{3}>0. |  | (21.18) |

Thus { 𝒱 = 0 } \{\mathcal{V}=0\} is the isolated origin together with one proper arc tending to opposite infinities; it creates no bounded hole.

On the proper arc { 𝒱 = 0 } ∖ { ( 0, 0) } \{\mathcal{V}=0\}\setminus\{(0,0)\}, ( 21.12) gives X ​ 𝒱 > 0 X\mathcal{V}>0, so a periodic orbit cannot cross it. The omitted point is the equilibrium. On each complementary component use ℬ ^ = | 𝒱 | − 3 / 2 \widehat{\mathcal{B}}=|\mathcal{V}|^{-3/2}:

 | div ( ℬ ^ X) = − 3 2 sign ( 𝒱) | 𝒱 | − 5 / 2 4 ​ d 3 𝒦. \operatorname{div}(\widehat{\mathcal{B}}X)=-\frac{3}{2}\operatorname{sign}(\mathcal{V})|\mathcal{V}|^{-5/2}\,\frac{4d}{3}\mathcal{K}. |  | (21.19) |

Green’s theorem excludes a cycle in every component without a hole and excludes two in the unique one-hole component by integrating over the annulus between them. Outside the integrable corner there is at most one periodic orbit; including that period-annulus corner, there is at most one isolated periodic orbit. ∎

###### Theorem 32 (Exact mixed persistent-endpoint theorem).

Every retained word in the mixed class has a locally uniform finite number of isolated fixed points. More precisely, B = 0, a ≠ 0 B=0,a\neq 0 carries no source-order full lap; on B = a = 0 B=a=0, the collision/no-root cone has at most one isolated periodic orbit by Lemma 31, and the complementary split cone has a fixed sink/no-passage first port. The assignment is uniform through the D D -collision, both adjacent sides, the source overlap, and all lower first-port faces. If t mer t_{\rm mer} denotes the merger scale of the root chart, its subface t mer = 0 t_{\rm mer}=0, including t mer = κ = 0 t_{\rm mer}=\kappa=0, belongs to the source regime.

###### Remark 33.

The theorem concerns a retained full-lap itinerary in the fixed collar U U whose orbit arcs between certified first-hit sections remain in z = 1 + y > 0 z=1+y>0 until a named lower first port. Its bound is uniform on B = a = 0 B=a=0 for all values of ℓ / d \ell/d, throughout the no-root cone, adjacent split collar, complementary split cases, source overlap, and lower first-port faces. On the direct Dulac cone there is at most one isolated orbit. No open-neighborhood Dulac estimate in B B or a a is asserted. The face t mer = 0 t_{\rm mer}=0 is treated by Theorem 30; a split root reaches its first sink, hyperbolic, passive, or regular port, and loss of a lower hit is no-passage.

###### Proof.

The orientation calculation ( 21.1) handles B = 0, a ≠ 0 B=0,a\neq 0. On B = a = 0 B=a=0, choose for example q 0 = 31 / 128 q_{0}=31/128 and split first by

 | p = − m ≥ q 0 ​ d 2. p=-m\geq q_{0}d^{2}. |  | (21.20) |

This closed cone contains the collision p = d 2 / 4 p=d^{2}/4, the adjacent split collar q 0 ​ d 2 ≤ p < d 2 / 4 q_{0}d^{2}\leq p<d^{2}/4, and the whole no-root side. A periodic orbit represented by the word stays in z > 0 z>0: on z = 0 z=0, z ˙ = ℓ \dot{z}=\ell, so crossings have one orientation when ℓ ≠ 0 \ell\neq 0, while the line is invariant when ℓ = 0 \ell=0. Lemma 31 therefore applies to every possible orbit in this cone.

The source overlap is not recognized from d / θ d/\theta alone. Its full effective vector contains

 | Ξ src = max ⁡ { p θ 2, | d | θ, | c | θ }. \Xi_{\rm src}=\max\left\{\frac{p}{\theta^{2}},\frac{|d|}{\theta},\frac{|c|}{\theta}\right\}. |  | (21.21) |

The direct Dulac estimate is independent of Ξ src \Xi_{\rm src}, so it controls both sides of every finite source/parameter threshold. At the exact source subface, the assignment nevertheless follows the half-open priority of Table 1; Theorem 30 supplies its ambient neighborhood.

On the complementary split cone use the same involution as in the lemma to take d ≥ 0 d\geq 0, and set

 | Δ = d 2 + 4 ​ m > 0, w + = − d + Δ 2. \Delta=d^{2}+4m>0,\qquad w_{+}=\frac{-d+\sqrt{\Delta}}{2}. |  | (21.22) |

For m = − p < 0 m=-p<0 with p < q 0 ​ d 2 p<q_{0}d^{2}, Δ > d 2 / 32 \Delta>d^{2}/32; for m ≥ 0 m\geq 0, Δ / ( d + m) \sqrt{\Delta}/(d+\sqrt{m}) also has a fixed positive lower bound. Define

 | ρ = { d, m < 0, d + m, m ≥ 0. \rho=\begin{cases}d,&m<0,\\ d+\sqrt{m},&m\geq 0.\end{cases} |  | (21.23) |

Use w = ρ ​ W w=\rho W, r = ρ 2 ​ R r=\rho^{2}R, and divide time by ρ \rho. The two normalized eigenvalues at the first source-oriented root are

 | λ w ρ = − Δ ρ < 0, λ r ρ = − d + Δ 2 ​ ρ < 0. \frac{\lambda_{w}}{\rho}=-\frac{\sqrt{\Delta}}{\rho}<0,\qquad\frac{\lambda_{r}}{\rho}=-\frac{d+\sqrt{\Delta}}{2\rho}<0. |  | (21.24) |

If m = − p < 0 m=-p<0, then p < q 0 ​ d 2 p<q_{0}d^{2} gives Δ / d ≥ 1 / 32 \sqrt{\Delta}/d\geq 1/\sqrt{32}, while the second quotient has modulus at least 1 / 2 1/2. If m ≥ 0 m\geq 0, then d 2 + 4 ​ m / ( d + m) ≥ 2 / 3 \sqrt{d^{2}+4m}/(d+\sqrt{m})\geq 2/3, and the second quotient again has modulus at least 1 / 2 1/2. Thus the normalized family has a fixed two-negative-eigenvalue margin. Moreover the equatorial polynomial is negative for w > w + w>w_{+}, so this is the first root met by the source-oriented flow. To record the isolating block quantitatively, translate W W to the normalized root and write ζ = ( R, U) \zeta=(R,U). The compact normalized family of linear parts is uniformly Hurwitz by ( 21.24), including the repeated-eigenvalue face m = 0 m=0. The Lyapunov equation therefore supplies positive forms ℒ α ​ ( ζ) = ζ T ​ P α ​ ζ \mathcal{L}_{\alpha}(\zeta)=\zeta^{T}P_{\alpha}\zeta and uniform constants c 0, C 0, C 1 > 0 c_{0},C_{0},C_{1}>0 such that

 | c 0 ​ | ζ | 2 ≤ ℒ α ​ ( ζ) ≤ C 0 ​ | ζ | 2, ℒ ˙ α ≤ − | ζ | 2 + C 1 ​ | ζ | 3. c_{0}|\zeta|^{2}\leq\mathcal{L}_{\alpha}(\zeta)\leq C_{0}|\zeta|^{2},\qquad\dot{\mathcal{L}}_{\alpha}\leq-|\zeta|^{2}+C_{1}|\zeta|^{3}. |  | (21.25) |

One fixed sufficiently small positive level of ℒ α \mathcal{L}_{\alpha}, intersected with R ≥ 0 R\geq 0, is thus inward pointing; the face R = 0 R=0 is invariant. This gives a uniform sink isolating block, in the form of a half-block, without choosing eigenvectors across the repeated face. An orbit arriving from w > w + w>w_{+} cannot leave it in forward time and cannot belong to a periodic lap. The case m = 0 m=0 is included after rescaling; the sole corner d = m = 0 d=m=0 belongs to the source regime.

There are only finitely many threshold, root, and lower-port charts. Every specialization either remains in the direct one-cycle estimate, enters the matched source neighborhood, reaches the split sink/hyperbolic/regular regime, or loses a first hit. Compactness of this already named finite cover gives the asserted locally uniform bound. ∎

### 22 The zero-scale handoff

Part II has established two ambient results. Theorem 30 holds on the common source action tube, including its open-gate no-passage and center-identity conclusions. Theorem 32 holds on the retained physical full-lap domain in U ∩ { z > 0 } U\cap\{z>0\}, including the collision/no-root cone, the split-cone first-port classification, and the lower first-port faces.

Part I invokes these theorems only after the stopped-itinerary and exact-once reductions: they treat the classes 𝔓 src \mathfrak{P}_{\rm src} and 𝔓 mix \mathfrak{P}_{\rm mix}, respectively, and their boundary conclusions feed the finite specialization induction. Part III treats the complementary positive-scale regimes. In its middle/root priority, t mer = 0 t_{\rm mer}=0, including t mer = κ = 0 t_{\rm mer}=\kappa=0, is treated by the source theorem, whereas t mer > 0, κ = 0 t_{\rm mer}>0,\ \kappa=0 is treated by the mixed theorem. These are ambient boundary theorems proved here, not continuity limits of the positive-root theorem.

## Part III Hyperbolic, central, lips, middle, and root-scale zero theorems

### 23 Hyperbolic words and the QRH theorem

We begin with an exact-once itinerary already shown in Part I to contain only separated hyperbolic saddles and regular first hits. We first construct its physical analytic system, then verify QRH membership and a common admissible representative, and only then invoke Mourtada’s local finiteness theorem. We use Mourtada’s principal-orbit and integral-projection framework, the local rational and quasi-resonant construction in Appendix VA and the proof of Theorem 0, the QRH inverse result VB4, and the local finiteness theorem IVC1 along an admissible Hilbert derivation [3]. None of these results constructs an H14 section, connector, or physical itinerary. For the central and lips cases we use Theorem 3, Theorems 3.1–3.2, and Corollary 3.6 of Dumortier–Ilyashenko–Rousseau [2], only after their geometric hypotheses have been verified in the physical family.

The precise imported scopes are the following. The displayed proof of VA1 applies near the resonant ratio one to an analytic hyperbolic saddle form

 | u ​ d ​ v + v ⁡ { r ⁡ ( α) + a ⁡ ( u, v, α) } ​ d ​ u = 0, a ⁡ ( 0, 0, α) = 0, r ⁡ ( α) = 1 + μ ⁡ ( α), u\,dv+v\{r(\alpha)+a(u,v,\alpha)\}\,du=0,\qquad a(0,0,\alpha)=0,\quad r(\alpha)=1+\mu(\alpha), |  | (23.1) |

and places its Dulac correction in the one-variable QRH algebra. The paragraph preceding VA1 explicitly separates the remaining local scope: a fixed rational ratio follows by positive double ramification, whereas the quasi-resonant case is treated directly. The proof of Theorem 0 then uses a Q ​ R ​ H 1 QRH_{1} Dulac germ at every hyperbolic vertex of the analytic unfolding. We import that stated all-hyperbolic local scope; we do not manufacture it from density of rational ratios. IVC1 gives finite local degree only for a QRH closing germ along an admissible derivation χ ∈ Ξ ​ H k ​ [Q ​ R ​ H] \chi\in\Xi H_{k}[QRH], on one common admissible positive-corner representative. It is not a finiteness theorem for an arbitrary C p C^{p} functional system. DIR2002, Theorem 3, gives a prescribed finite smooth orbital normal form for a finite-multiplicity analytic saddle-node. The proof of Theorem 3.1 uses those coordinates to obtain linear strong-central maps and chooses the normalizing charts so that the already certified hh connector is a parameter-dependent translation. This proof-level import is used only after an actual lips ensemble has already been constructed. Theorem 3.2 supplies the finite-cyclicity result for its certified pp/bp bordering cases. Separately, the proof of Theorem 3.2 supplies the nonaffine infinity-jet of the critical analytic transition under those alternatives; analyticity then gives the finite first nonzero derivative required by Theorem 3.1. Corollary 3.6 supplies the one-central and multi-central no-pp clauses. None of these DIR statements infers hh, pp, PP/BP, or first-port data from a normal form.

Mourtada’s VB4 is used only in the QRH diagonal reduction: a QRH germ x ⁡ ( 1 + O ⁡ ( x)) x(1+O(x)) has a unique inverse of the same QRH form. The ordinary analytic connector inverses below are already covered by the analytic inverse theorem.

More explicitly, Theorem 3.1 starts with two saddle-nodes of opposite attractivity, one hh connection, a continuum of complete pp connections, and a regular pp transition having some nonzero derivative of order n ≥ 2 n\geq 2; it then bounds the selected graphic by n n. Under the listed PP/BP alternatives, the argument in the proof of Theorem 3.2 yields that nonaffine jet throughout the connected lips ensemble: for a PP boundary the hyperbolic saddle has ratio different from one (or no analytic first integral), while the BP argument is unconditional. Corollary 3.6 is used here only in its no-pp case: all selected saddle-nodes are traversed centrally, have the same attractivity, and the cyclicity is one. For completeness, let K ⋐ ( 0, ∞) K\Subset(0,\infty) be the compact ratio set of one H14 hyperbolic word cell. At a rational center r 0 = n / m r_{0}=n/m, the positive double ramification x = X m, y = Y n x=X^{m},\ y=Y^{n} changes the principal one-form, after division by a positive monomial, to one with characteristic ratio

 | r ~ = m ​ r n = 1 + μ, r ~ ​ ( r 0) = 1. \widetilde{r}=\frac{mr}{n}=1+\mu,\qquad\widetilde{r}(r_{0})=1. |  | (23.2) |

It is one-to-one on the positive quadrant and preserves isolated positive solutions. At a quasi-resonant center we use the direct branch stated in the same Appendix VA scope paragraph; the proof of Theorem 0 is the source’s equation-level use of these local Q ​ R ​ H 1 QRH_{1} germs at all hyperbolic vertices. Thus every fixed r 0 ∈ K r_{0}\in K has a source-supplied local ratio chart. Those charts form an open cover of the already certified compact set K K, and only now does compactness select a finite subcover. No rational-density argument, and no extension of VA1 across a zero eigenvalue, is used. IVC1 says that the QRH algebra is locally χ \chi -finite; the uniform orbitwise component bound comes from the local degree on one admissible representative and only then from a finite cover of the compact H14 word cell.

###### Proposition 34 (Certified analytic hyperbolic word).

Every retained all-hyperbolic H14 word has a finite cover by compact analytic word cells. On each cell, every used saddle has analytic separatrix coordinates and fixed one-sided analytic sections such that, after one fixed local time orientation,

 | u ˙ j = u j A j ( u j, v j, α), v ˙ j = − v j B j ( u j, v j, α), A j, B j ≥ λ ∗ > 0. \dot{u}_{j}=u_{j}A_{j}(u_{j},v_{j},\alpha),\qquad\dot{v}_{j}=-v_{j}B_{j}(u_{j},v_{j},\alpha),\qquad A_{j},B_{j}\geq\lambda_{*}>0. |  | (23.3) |

The ratios r j = B j ​ ( 0, 0, α) / A j ​ ( 0, 0, α) r_{j}=B_{j}(0,0,\alpha)/A_{j}(0,0,\alpha) remain in one compact subset of ( 0, ∞) (0,\infty). Every connector between consecutive sections is the actual jointly analytic first hit

 | s j + 1 = T j ​ ( t j, α), 0 < c T ≤ ∂ t j T j ≤ C T, s_{j+1}=T_{j}(t_{j},\alpha),\qquad 0<c_{T}\leq\partial_{t_{j}}T_{j}\leq C_{T}, |  | (23.4) |

on one common interval, with positive section-normal, all-port, and word-existence margins. The same original five parameters are used at every vertex and connector.

A zero eigenvalue, node, multiple endpoint root, missing connector, changed first port, or collar exit is not a boundary of this analytic cell. It is a separately named adjacent regime reached at the first lost margin. No DIR endpoint coordinate and no finite-smooth saddle-node normalizer occurs here.

###### Proof.

The finite root, sector, and port cover of Part I first separates every used saddle from the equatorial-discriminant and equatorial/interior joint-collision boxes of ( 4.11), multiple horizontal roots, and same-sign node cells. On a closed separated cell both eigenvalues have a fixed nonzero margin. The analytic stable-manifold theorem straightens the two invariant curves; analytic Hadamard division then gives ( 23.3). Fixed small levels of u j u_{j} and v j v_{j} are transverse sections with fixed normal signs.

Delete these saddle boxes from the stopped word. Every remaining arc is a finite concatenation of regular flow boxes. Analytic dependence of the ODE and the implicit-hit theorem give T j T_{j}, while planar order preservation in the oriented section coordinates gives ∂ T j > 0 \partial T_{j}>0. Inner and outer word domains with positive competing-port margins give the two-sided bounds in ( 23.4). The first vanishing normal, interval width, or competing-port distance is exactly one of the already numbered faces, proving the finite cover and the stated passage to adjacent regimes. ∎

Fix one certified cell and retain every intermediate outgoing value x 1, …, x k x_{1},\ldots,x_{k}. Let δ j \delta_{j} be the actual local Dulac map in the sections of Proposition 34. The local orbit one-form is

 | u j ​ d ​ v j + v j ​ B j ​ ( u j, v j, α) A j ​ ( u j, v j, α) ​ d ​ u j = 0, B j A j = r j + a j, a j ​ ( 0, 0, α) = 0. u_{j}\,dv_{j}+v_{j}\frac{B_{j}(u_{j},v_{j},\alpha)}{A_{j}(u_{j},v_{j},\alpha)}\,du_{j}=0,\qquad\frac{B_{j}}{A_{j}}=r_{j}+a_{j},\quad a_{j}(0,0,\alpha)=0. |  | (23.5) |

On each local ratio chart described above, Mourtada’s Appendix VA result places the analytic Dulac correction in Q ​ R ​ H 1 QRH_{1}: by descent from ( 23.2) at a rational center, and directly on a quasi-resonant chart. In the physical section coordinate this gives

 | δ j ​ ( x j, α) = x j r j ​ ( α) ​ { 1 + D j ​ ( x j, α) }, D j ∈ Q ​ R ​ H 1, D j ​ ( 0, α) = 0. \delta_{j}(x_{j},\alpha)=x_{j}^{r_{j}(\alpha)}\{1+D_{j}(x_{j},\alpha)\},\qquad D_{j}\in QRH_{1},\quad D_{j}(0,\alpha)=0. |  | (23.6) |

This is an exact membership statement for the analytic saddle cell, not a formal linearization and not a claim at a zero eigenvalue.

The regular connectors, including the closing connector, are retained before normalization. Orient every target coordinate so that T j ′ > 0 T_{j}^{\prime}>0, and put

 | f j + 1 ​ ( u, α) = T j − 1 ​ ( u, α) − T j − 1 ​ ( 0, α), λ j ​ ( α) = T j − 1 ​ ( 0, α), 1 ≤ j ≤ k. f_{j+1}(u,\alpha)=T_{j}^{-1}(u,\alpha)-T_{j}^{-1}(0,\alpha),\qquad\lambda_{j}(\alpha)=T_{j}^{-1}(0,\alpha),\qquad 1\leq j\leq k. |  | (23.7) |

Use the cyclic convention x k + 1 = x 1 x_{k+1}=x_{1}. Here T k T_{k} is the actual regular first hit from the last outgoing section to the first incoming section; it is not an inferred translation. The physical cycle equations are then

 | δ j ​ ( x j, α) − f j + 1 ​ ( x j + 1, α) = λ j ​ ( α), 1 ≤ j ≤ k. \delta_{j}(x_{j},\alpha)-f_{j+1}(x_{j+1},\alpha)=\lambda_{j}(\alpha),\qquad 1\leq j\leq k. |  | (23.8) |

Thus no connector, including the closing one, is silently replaced by a guessed translation.

###### Proposition 35 (QRH realization on the physical fibers).

After the permitted diagonal analytic section changes, the zero-based functions

 | g j 0 = δ j ​ ( x j, α) − f j + 1 ​ ( x j + 1, α), 1 ≤ j < k, g_{j}^{0}=\delta_{j}(x_{j},\alpha)-f_{j+1}(x_{j+1},\alpha),\qquad 1\leq j<k, |  | (23.9) |

are first integrals of one Hilbert derivation χ ω ∈ Ξ ​ H k ​ [Q ​ R ​ H] \chi_{\omega}\in\Xi H_{k}[QRH]. The physical splittings are precisely the integral-projection values g j 0 = λ j ​ ( α) g_{j}^{0}=\lambda_{j}(\alpha). After adjoining ordinary passive affine coefficients, the complete closing equation is the QRH germ. Write the two zero-based analytic closing-section coordinates as

 | Φ out ​ ( u, α):= u, Φ in ​ ( u, α):= T k − 1 ​ ( u, α) − T k − 1 ​ ( 0, α). \Phi_{\rm out}(u,\alpha):=u,\qquad\Phi_{\rm in}(u,\alpha):=T_{k}^{-1}(u,\alpha)-T_{k}^{-1}(0,\alpha). |  | (23.10) |

Then that germ is

 | F A, B, C = A ​ Φ out ​ ( δ k ​ ( x k, α), α) − B ​ Φ in ​ ( x 1, α) − C. F_{A,B,C}=A\Phi_{\rm out}(\delta_{k}(x_{k},\alpha),\alpha)-B\Phi_{\rm in}(x_{1},\alpha)-C. |  | (23.11) |

The unnormalized physical coefficient triple is ( A, B, C) = ( 1, 1, λ k) (A,B,C)=(1,1,\lambda_{k}). Its positive projective representative is

 | ( A, B, C) = ( 1, 1, λ k) 2 + λ k 2, (A,B,C)=\frac{(1,1,\lambda_{k})}{\sqrt{2+\lambda_{k}^{2}}}, |  | (23.12) |

with λ k = T k − 1 ​ ( 0, α) \lambda_{k}=T_{k}^{-1}(0,\alpha), equation ( 23.11) is equivalent, after multiplication by its positive denominator, to δ k ​ ( x k) − T k − 1 ​ ( x 1) = 0 \delta_{k}(x_{k})-T_{k}^{-1}(x_{1})=0, which is exactly the closing equation in ( 23.8). Thus the inverse connector acts on the incoming coordinate, not on the outgoing Dulac value.

On a finite refinement of the compact word cell times

 | 𝒫 = { ( A, B, C): A, B ≥ 0, A 2 + B 2 + C 2 = 1 }, {\cal P}=\{(A,B,C):A,B\geq 0,\ A^{2}+B^{2}+C^{2}=1\}, |  | (23.13) |

there is one common admissible positive-corner representative and one physical invariant fiber set on which zeros of ( 23.11) are exactly solutions of the actual retained H14 word. Connection and separatrix values, projective coefficient faces, coordinate-corner faces, and identity closing fibers remain in this representative.

###### Proof.

The alternating-minor vector field annihilating the k − 1 k-1 functions in ( 23.9), normalized by its QRH unit so that its corner component is x 1 ⋯ x k x_{1}\cdots x_{k}, defines χ ω \chi_{\omega}. The decisive derivative is

 | x j ​ δ j ′ = x j r j ​ { r j ​ ( 1 + D j) + x j ​ ∂ x j D j } ∈ Q ​ R ​ H 1, x_{j}\delta_{j}^{\prime}=x_{j}^{r_{j}}\{r_{j}(1+D_{j})+x_{j}\partial_{x_{j}}D_{j}\}\in QRH_{1}, |  | (23.14) |

and analytic inverse closure applies to the f j f_{j}; VB4 is reserved for the QRH diagonal inverses in the imported reduction. Hence the normalized derivation, its first integrals, and ( 23.11) satisfy the recursive QRH definitions. The coefficients ( A, B, C) (A,B,C) are first passive variables in ordinary open charts and are restricted to ( 23.13) only after membership has been proved.

For fixed projection values, ( 23.8) recursively gives

 | x j + 1 = f j + 1 − 1 ​ ( δ j ​ ( x j, α) − λ j ​ ( α)). x_{j+1}=f_{j+1}^{-1}\bigl(\delta_{j}(x_{j},\alpha)-\lambda_{j}(\alpha)\bigr). |  | (23.15) |

Monotonicity and the common word inequalities make every nonempty physical fiber one connected graph and hence one orbit of χ ω \chi_{\omega}. This proves the zero/first-hit correspondence required by IVC1. The corner is invariant because χ ω ​ x j / x j ∈ Q ​ R ​ H \chi_{\omega}x_{j}/x_{j}\in QRH; a point on a coordinate axis itself represents a separatrix value, not a limit cycle. Compactness of the certified cell and ( 23.13) now gives finitely many admissible representatives. An identity closing fiber contributes no isolated zero, while the same representative controls its neighboring fibers. ∎

###### Theorem 36 (All-hyperbolic QRH theorem).

On every compact certified analytic H14 word cell satisfying Propositions 34 and 35, the complete retained-variable system has a locally uniform finite number of isolated positive solutions. This includes nonzero ratio-one saddles, with or without an analytic first integral, and all projective coefficient and connection faces in ( 23.13).

###### Remark 37.

Uniformity holds after a finite refinement of the compact physical itinerary cell times the projective coefficient set ( 23.13), with one admissible representative on each member. Connection, separatrix, coefficient, and identity values remain within that representative. A zero eigenvalue, multiple root, node, missing connector, changed first port, lost section normal, or exit is stopped at its named adjacent regime before QRH is invoked.

###### Proof.

Mourtada’s IVC1 theorem applies to every common admissible representative in Proposition 35. It gives a finite local degree for the zero set of ( 23.11) along the physical invariant fibers. The exact fiber/first-hit correspondence turns that degree into the required H14 zero count. Taking the maximum over the finite refinement gives one bound for the cell. On A = 0 A=0 or B = 0 B=0 the equation is monotone or constant and has at most one isolated solution; the zero coefficient triple is excluded by ( 23.13). An identity fiber has no isolated member. No compactness step crosses a zero-eigenvalue or changed-word face, because those faces were removed in Proposition 34. ∎

### 24 Central words and Two-Central Exhaustion

This section starts with a stopped, exact-once physical itinerary from Part I. It does not construct the atlas and it does not infer an orbit from a formal normal form. We first treat the unique-central case, then prove an exhaustive geometric classification of every retained two-central itinerary. Only after that classification do we invoke the no-pp clause of DIR; the pp alternatives are treated by the strict, middle, and root theorems below.

For this section, S h S_{h} denotes the selected nonpersistent horizontal saddle-node and S v S_{v} the selected upper D D -saddle-node. The finite signed endpoint cover writes the upper double root as w = − q w=-q, q = σ ​ t q=\sigma t, with t = | q | ≥ 0 t=|q|\geq 0. The label E σ E_{\sigma} is the selected regular equatorial arc, p σ p_{\sigma} its persistent principal endpoint, and ξ \xi is the oriented endpoint-section coordinate for which 0 < ξ < ξ h 0<\xi<\xi_{h} lies between the equatorial boundary and the selected hh separatrix. These are physical labels from the stopped atlas, not normal-form objects.

#### 24.1 A single central block

Let G G be the sole central vertex selected by a retained word ω \omega. The required uniform nondegeneracy condition is

 | | λ tr ​ ( G) |, | q G ′′ ​ ( 0) | ≥ m c, min v ∈ 𝒱 ⁡ ( ω) ∖ { G } ⁡ min ⁡ { | λ v s |, | λ v u | } ≥ m h > 0. |\lambda_{\rm tr}(G)|,\ |q_{G}^{\prime\prime}(0)|\geq m_{c},\qquad\min_{v\in\mathcal{V}(\omega)\setminus\{G\}}\min\{|\lambda_{v}^{s}|,|\lambda_{v}^{u}|\}\geq m_{h}>0. |  | (24.1) |

Thus the local weak equation has a genuine quadratic saddle-node term and every other singular vertex, including both principal endpoints, is hyperbolic. Merely having one internal label would not imply ( 24.1).

###### Theorem 38 (One-central no-pp theorem).

On a compact family of retained exact-once words satisfying ( 24.1), with an actual retained passage through the central sector, fixed sections, and the Part I all-port margins, the number of isolated cycles is locally uniformly finite; in fact the corresponding elementary graphic has cyclicity at most one.

###### Remark 39.

The bound is uniform in a full five-parameter neighborhood of a compact certified family, provided the constants in ( 24.1), section normals, and first-port margins stay uniformly positive. If the central root splits, the itinerary becomes all-hyperbolic; a second central block enters the exhaustion theorem below; and a persistent B = 0 B=0 endpoint enters the mixed regime. Wrong orientation, stable-center passage, changed first port, collapse, and exit are stopped before a return equation is formed.

###### Proof.

The finite-smooth central normal form is applied only to the actual saddle-node in ( 24.1). The remaining sections and connectors are the physical hyperbolic first hits certified in Part I. The resulting graphic is therefore exactly the one-central, no-parabolic-connection alternative of the DIR central theorem, whose unconditional clause gives cyclicity one. The lower bounds in ( 24.1) and the fixed-port margins persist on one open neighborhood in the original parameters. A finite cover of the compact base family yields the uniform statement. If one of these inequalities or passage conditions is lost, the itinerary enters the adjacent case described in the preceding remark. ∎

#### 24.2 The finite two-central alphabet

There are at most two internal central gates. In signed reciprocal endpoint coordinate u u, the horizontal equation has the prepared form

 | X ^ ​ u = − u ​ P ​ ( u, λ), P ⁡ ( u, λ) = U ⁡ ( u, λ) ​ ( u 2 + A 1 ​ u + A 0), U ≠ 0. \widehat{X}u=-uP(u,\lambda),\qquad P(u,\lambda)=U(u,\lambda)(u^{2}+A_{1}u+A_{0}),\quad U\neq 0. |  | (24.2) |

The quadratic factor has at most one multiple root across the two signed endpoint charts; the persistent root u = 0 u=0 is an endpoint passage rather than an internal gate. The only other central label is the unique upper D D -collision. Hence a retained word has zero, one, or precisely these two internal central gates.

The intersection with the center variety is also explicit. On the quadratic center component,

 | μ 2 = − B, c = μ 3 = − a, \mu_{2}=-B,\qquad c=\mu_{3}=-a, |  | (24.3) |

and the horizontal and vertical root polynomials

 | f Q ​ ( x) = 1 − B + a ​ x + B ​ x 2, E Q ​ ( w) = − B + a ​ w − ( 1 − B) ​ w 2 f_{Q}(x)=1-B+ax+Bx^{2},\qquad E_{Q}(w)=-B+aw-(1-B)w^{2} |  | (24.4) |

have common discriminant a 2 − 4 ​ B ​ ( 1 − B) a^{2}-4B(1-B). Their double-root locus is

 | B = t 2 1 + t 2, 0 < t < t 0, a = 2 ​ ϵ ​ t 1 + t 2, c = μ 3 = − a, ϵ ∈ { ± 1 }. B=\frac{t^{2}}{1+t^{2}},\qquad 0<t<t_{0},a=\frac{2\epsilon t}{1+t^{2}},\qquad c=\mu_{3}=-a,\qquad\epsilon\in\{\pm 1\}. |  | (24.5) |

We call this the explicit invariant-center component. The reversible center component has no nonpersistent horizontal double root. The discriminant calculation alone does not certify a physical lips ensemble. On the invariant-center component, however, direct substitution in the H14 field gives the invariant strong line

 | L ϵ = t ​ x − ϵ ​ t 2 ​ z + ϵ = 0, X λ ​ L ϵ = K ϵ ​ L ϵ, L_{\epsilon}=tx-\epsilon t^{2}z+\epsilon=0,\qquad X_{\lambda}L_{\epsilon}=K_{\epsilon}L_{\epsilon}, |  | (24.6) |

and the signed first-port computation of Proposition 40 supplies the complete pp strip and its PP boundary through p − ϵ p_{-\epsilon}. Thus every two-central parameter on the invariant-center component carries the required physical configuration. At this stage the conclusion is only that the residual affine class is empty on this center component; it is not yet its global elimination.

For completeness, away from this invariant-center component the strong connection is tested physically. On c = d c=d, write

 | L = x + d 2 ​ ( 1 − B) ​ z + a 2 ​ B, X λ ​ L = ( B ​ x + a 2 + d 2 ​ z) ​ L − κ inv ​ z, κ inv = 4 ​ B ​ ( 1 − B) + a ​ d 4 ​ B ​ ( 1 − B). L=x+\frac{d}{2(1-B)}z+\frac{a}{2B},\quad X_{\lambda}L=\left(Bx+\frac{a}{2}+\frac{d}{2}z\right)L-\kappa_{\rm inv}z,\quad\kappa_{\rm inv}=\frac{4B(1-B)+ad}{4B(1-B)}. |  | (24.7) |

The symbol κ inv \kappa_{\rm inv} is an invariance defect, not the root-scale coordinate used later. Equation ( 24.7) recovers the invariant-center component when κ inv = 0 \kappa_{\rm inv}=0, but a general curved connection is accepted only when its actual landing difference vanishes on the enlarged stopped-word domain.

###### Proposition 40 (Complete physical lips configurations).

Every retained two-central pp candidate admits a finite refinement. On each subfamily carrying a complete physical lips configuration, the following conditions hold:

1. (i)

there are two distinct simple physical saddle-nodes;

2. (ii)

their nonzero transverse eigenvalues have opposite signs;

3. (iii)

the weak and strong sections are fixed and have positive normals;

4. (iv)

the actual strong landing difference is zero;

5. (v)

there is a nonempty interval of complete pp orbits;

6. (vi)

the other boundary is a complete PP or BP incidence;

7. (vii)

no extra root, gate, port, or collar side meets the retained interval;

8. (viii)

on a PP boundary, r bd ∉ [1 / 2, 2] r_{\rm bd}\notin[1/2,2]; no ratio condition is required on a BP boundary.

Let δ hh \delta_{\rm hh} denote the actual strong landing difference on the fixed physical sections, so condition (iv) is δ hh = 0 \delta_{\rm hh}=0. A punctured landing-split fiber near such a configuration is not a failed first port: it is retained as the connection, hence constant, coefficient in the same strict, middle, or root affine comparison. On a closed subcell | δ hh | ≥ η > 0 |\delta_{\rm hh}|\geq\eta>0, no sequence of isolated fixed points can approach the two-central face. Thus every refined subfamily is either a complete physical lips configuration satisfying (i) – (viii), one of its landing-split coefficient subfamilies, a landing-gap-separated subcell with zero contribution to the local two-central limit, or a named geometric first-port outcome.

Condition (v) means complete orbits whose alpha- and omega-limits are the two saddle-nodes, not merely a finite section-to-section hit. Sector ordering is part of the refinement: if an opposite-sign adjacency has no parabolic next-port word, it first reaches a stable-center, previous-side, or exit port and is not retained. Consequently every retained no-pp word has the same-attractivity required by Theorem 43. If a parabolic next-port interval is nonempty, its maximal survivor component is followed until its non-hh endpoint first reaches PP, BP, another gate, a passive side, a collapsed interval, or the collar. The first two complete conditions (vi) – (viii); the middle outcomes are already named adjacent regimes, and the collar possibility is eliminated below by ( 24.29).

###### Proof.

For each ordered sign/port label, the actual strong first hit is defined on an enlarged positive-margin domain and its landing difference δ hh \delta_{\rm hh} certifies the hh incidence. On the adjacent parabolic side, recursive survivor intervals select finitely many maximal first-port words. Near either saddle-node the local equations have the form

 | x ˙ = x 2 U ( x), y ˙ = − γ ( x, y) y, U, γ ≥ c 0 > 0. \dot{x}=x^{2}U(x),\qquad\dot{y}=-\gamma(x,y)y,\qquad U,\gamma\geq c_{0}>0. |  | (24.8) |

The weak travel time diverges while the strong variable contracts exponentially. Appending these two semiorbits converts every retained first-hit interval into a continuum of complete pp orbits.

The landing alternatives in the statement follow on the same physical word. Suppose isolated fixed points approach two internal critical boxes. The finite cyclic-word alphabet and compact physical sections give a subsequence with one fixed sector word. If it has a pp passage, the complementary limiting arcs are the two selected strong branches, and continuity of every actual first hit gives δ hh → 0 \delta_{\rm hh}\to 0. Hence a closed subcell | δ hh | ≥ η |\delta_{\rm hh}|\geq\eta contains no such fixed point near the two-central face. On the punctured neighborhood of δ hh = 0 \delta_{\rm hh}=0, the landing split changes only the constant connection coefficient C 0 C_{0}. It is retained in the strict comparison ( 25.5), the middle comparison ( 26.37) under the coefficient-cone convention ( 26.1), and the root comparison ( 27.42). Those coefficient fibers therefore stay inside the same strict, middle, or root theorem neighborhood; they are neither new regimes nor failures of the complete-lips hypotheses.

The sector alternatives preceding this construction are exhaustive. With no parabolic next-port word, cyclic sector order leaves only central transitions. An opposite-sign central adjacency necessarily meets the stable-center divider, the previous-side cut, or the collar exit before the next gate; these are terminal Part I labels. Hence the only retained no-pp alternative has same attractivity. With a nonempty parabolic word, planar order makes each maximal survivor set an interval, and its non-hh endpoint is followed through the finite cut order. It either supplies the boundary field below or first hits one of the already numbered terminal or adjacent outcomes.

The other endpoint is retained only if both physical axis landings and a positive boundary-arc margin give a complete PP incidence, or if the actual center-side axis gives a complete BP incidence. Write the selected upper double root as w = − q w=-q. On the two-central sheet, after shrinking,

 | S ⁡ ( 0) = − ( 1 − B) ​ q 2 ​ ( 1 − 2 ​ B) 2 < 0, S ′ ​ ( R) ≤ − 1 2, S(0)=-(1-B)q^{2}(1-2B)^{2}<0,\qquad S^{\prime}(R)\leq-\tfrac{1}{2}, |  | (24.9) |

so S ⁡ ( R) < 0 S(R)<0 for R > 0 R>0 and there is no interior boundary saddle. The only PP saddle is consequently a persistent principal endpoint, with ratio

 | r bd = | B 1 − B | or its reciprocal. r_{\rm bd}=\left|\frac{B}{1-B}\right|\quad\hbox{or its reciprocal}. |  | (24.10) |

After | B | < 1 / 4 |B|<1/4, this ratio lies outside [1 / 2, 2] [1/2,2].

It remains to prove that no unlisted divider truncates the pp interval. Let w = − q w=-q denote the selected upper double root. On that sheet,

 | m = − ( 1 − B) ​ q 2, d = 2 ​ ( 1 − B) ​ q, E ⁡ ( w) = − ( 1 − B) ​ ( w + q) 2. m=-(1-B)q^{2},\qquad d=2(1-B)q,\qquad E(w)=-(1-B)(w+q)^{2}. |  | (24.11) |

Let σ \sigma denote the signed source-arc record selected by the stopped word; for q > 0 q>0 it is (+), and reflection treats q < 0 q<0. On the invariant-center component one has σ = − ϵ \sigma=-\epsilon. In physical endpoint coordinates,

 | ξ ˙ = − ρ ( ξ, α) ξ ( ξ − ξ h) 2, η ˙ = η, ρ ≥ ρ 0 > 0, J 0 = { 0 < ξ < ξ h }. \dot{\xi}=-\rho(\xi,\alpha)\xi(\xi-\xi_{h})^{2},\qquad\dot{\eta}=\eta,\qquad\rho\geq\rho_{0}>0,\qquad J_{0}=\{0<\xi<\xi_{h}\}. |  | (24.12) |

Every orbit in J 0 J_{0} has alpha-limit S h S_{h}; its two boundary paths are the selected hh orbit and S h → p σ → E σ S_{h}\to p_{\sigma}\to E_{\sigma}. The fixed cut order prevents a reset, extra lap, or opposite source arc, so the only macro itinerary is

 | S h ⟶ E σ ⟶ S v S_{h}\longrightarrow E_{\sigma}\longrightarrow S_{v} |  | (24.13) |

through a finite ordered list of regular tiles. Before using order, record the complete list of physical boundary faces:

 | piece boundary faces possible divider endpoint η = η 0, η 1, ξ = 0, ξ h ξ = 0, ξ h E σ ​ tube θ = θ j, θ j + 1, n = n j −, n j + backward exit-corner orbit upper box I +, I −, r = r ∗, ∂ B S v stable/central equilibrium branch. \begin{array}[]{c|c|c}\text{piece}&\text{boundary faces}&\text{possible divider}\\ \hline\cr\text{endpoint}&\eta=\eta_{0},\eta_{1},\ \xi=0,\xi_{h}&\xi=0,\xi_{h}\\ E_{\sigma}\text{ tube}&\theta=\theta_{j},\theta_{j+1},\ n=n_{j}^{-},n_{j}^{+}&\text{backward exit-corner orbit}\\ \text{upper box}&I_{+},I_{-},\ r=r_{*},\ \partial B_{S_{v}}&\text{stable/central equilibrium branch}.\end{array} |  | (24.14) |

The endpoint row is exhaustive by ( 24.12), while the middle row consists of fixed nonsingular flow boxes. In such a tile,

 | d ​ n d ​ θ = f j ​ ( θ, n), X λ ​ θ ≥ 2 ​ c 0, n j − < n e, j < n h, j < n j +, \frac{dn}{d\theta}=f_{j}(\theta,n),\qquad X_{\lambda}\theta\geq 2c_{0},\qquad n_{j}^{-}<n_{e,j}<n_{h,j}<n_{j}^{+}, |  | (24.15) |

where n e, j n_{e,j} and n h, j n_{h,j} are the equatorial and hh solution graphs. Let C j ≥ 1 C_{j}\geq 1 be a bi-Lipschitz constant for the fixed physical tile coordinate, and let η h ​ h > 0 \eta_{hh}>0 be one quarter of the minimum all-port distance of the compact selected hh subword in the original physical metric. Define the physical collar distances in this tile by

 | ρ j e \displaystyle\rho_{j}^{e} | = min θ ⁡ { n e, j ​ ( θ) − n j −, n j + − n e, j ​ ( θ) } > 0, \displaystyle=\min_{\theta}\{n_{e,j}(\theta)-n_{j}^{-},\,n_{j}^{+}-n_{e,j}(\theta)\}>0, |  | (24.16) |

 | ρ j h \displaystyle\rho_{j}^{h} | = min θ ⁡ { n h, j ​ ( θ) − n j −, n j + − n h, j ​ ( θ) } ≥ 4 ​ η h ​ h C j > 0. \displaystyle=\min_{\theta}\{n_{h,j}(\theta)-n_{j}^{-},\,n_{j}^{+}-n_{h,j}(\theta)\}\geq\frac{4\eta_{hh}}{C_{j}}>0. |  |

The first inequality follows from the fixed nonzero widths of the equatorial tube; the second is precisely the hh all-port margin transported by the bi-Lipschitz chart. Put Δ j = θ j + 1 − θ j \Delta_{j}=\theta_{j+1}-\theta_{j}. For N = n − n e, j N=n-n_{e,j}, scalar uniqueness gives the literal difference equation

 | d ​ N d ​ θ = A j ​ ( θ, N) ​ N, | A j | ≤ L j. \frac{dN}{d\theta}=A_{j}(\theta,N)N,\qquad|A_{j}|\leq L_{j}. |  | (24.17) |

If 𝒟 j = ( d j −, d j +) {\cal D}_{j}=(d_{j}^{-},d_{j}^{+}) is the interval of entry values reaching the next cut, Gronwall gives neighborhoods of the two boundary entries of radii

 | m j e = ρ j e 2 ​ e − L j ​ Δ j, m j h = ρ j h 2 ​ e − L j ​ Δ j. m_{j}^{e}=\frac{\rho_{j}^{e}}{2}e^{-L_{j}\Delta_{j}},\qquad m_{j}^{h}=\frac{\rho_{j}^{h}}{2}e^{-L_{j}\Delta_{j}}. |  | (24.18) |

Since 𝒟 j {\cal D}_{j} is one interval and its endpoints are exactly the two backward exit-corner orbits in ( 24.14), the whole segment between n e, j ​ ( θ j) n_{e,j}(\theta_{j}) and n h, j ​ ( θ j) n_{h,j}(\theta_{j}) lies at positive distance from every divider. More explicitly, on the closed order band

 | K j = { ( θ, n): n e, j ​ ( θ) ≤ n ≤ n h, j ​ ( θ) } K_{j}=\{(\theta,n):n_{e,j}(\theta)\leq n\leq n_{h,j}(\theta)\} |  | (24.19) |

one has pointwise

 | n − n j − ≥ ρ j e, n j + − n ≥ ρ j h. n-n_{j}^{-}\geq\rho_{j}^{e},\qquad n_{j}^{+}-n\geq\rho_{j}^{h}. |  | (24.20) |

Thus neither collar, either collar corner, nor a previous-side face can be the first port. Since X λ ​ θ > 0 X_{\lambda}\theta>0, every intermediate graph reaches the next θ \theta -face. Induction over the finite tile list carries all of J 0 J_{0} to the upper entry as

 | w = δ, 0 < r < r h, w=\delta,\qquad 0<r<r_{h}, |  | (24.21) |

with equator and hh orbit as endpoints.

Put v = − w v=-w. The exact upper equations are

 | r ˙ = r ⁡ { ( 1 + r) ​ v − d − r ​ c }, v ˙ = − m − d ​ v + ( 1 − B) ​ v 2 + r ⁡ { 1 + ( a − c) ​ v + v 2 }. \dot{r}=r\{(1+r)v-d-rc\},\qquad\dot{v}=-m-dv+(1-B)v^{2}+r\{1+(a-c)v+v^{2}\}. |  | (24.22) |

There is no unrecorded gate because

 | S ⁡ ( 0) = − ( 1 − B) ​ q 2 ​ ( 1 − 2 ​ B) 2 < 0, S ′ ​ ( r) ≤ − 1 2. S(0)=-(1-B)q^{2}(1-2B)^{2}<0,\qquad S^{\prime}(r)\leq-\frac{1}{2}. |  | (24.23) |

Before their first target-block entry, the compact equatorial and hh arcs have positive distance from I − I_{-}, r = r ∗ r=r_{*}, and their corners. Let C up ≥ 1 C_{\rm up}\geq 1 dominate both bi-Lipschitz comparisons from the original physical metric to the upper ( r, w) (r,w) chart and from that chart to the fixed target saddle-node chart. Choose the target block itself disjoint from I − ∪ { r = r ∗ } I_{-}\cup\{r=r_{*}\}. A common upper-coordinate margin is therefore

 | ε up = min { r ∗, 3 ​ δ 4, 2 ​ η h ​ h C up, dist ( B S v ¯, I − ∪ { r = r ∗ }) } > 0. \varepsilon_{\rm up}=\min\left\{r_{*},\frac{3\delta}{4},\frac{2\eta_{hh}}{C_{\rm up}},\operatorname{dist}(\overline{B_{S_{v}}},I_{-}\cup\{r=r_{*}\})\right\}>0. |  | (24.24) |

Moreover the oriented system is cooperative,

 | ∂ v r ˙ = r ⁡ ( 1 + r) ≥ 0, ∂ r v ˙ = 1 + ( a − c) ​ v + v 2 ≥ 1 2. \partial_{v}\dot{r}=r(1+r)\geq 0,\qquad\partial_{r}\dot{v}=1+(a-c)v+v^{2}\geq\frac{1}{2}. |  | (24.25) |

Every intermediate path therefore remains between the two boundary paths and keeps the margin ( 24.24). Here the comparison is at a common value of the positive desingularized upper-chart time: start all solutions on w = δ w=\delta, write v = − w v=-w, and denote the equatorial and hh solutions by ( r e, v e) (r_{e},v_{e}), ( r h, v h) (r_{h},v_{h}). The quasimonotone system ( 24.25) preserves the positive quadrant, so

 | r e ​ ( t) ≤ r ⁡ ( t) ≤ r h ​ ( t), v e ​ ( t) ≤ v ⁡ ( t) ≤ v h ​ ( t) r_{e}(t)\leq r(t)\leq r_{h}(t),\qquad v_{e}(t)\leq v(t)\leq v_{h}(t) |  | (24.26) |

throughout their common maximal interval. Consequently

 | r ∗ − r ⁡ ( t) ≥ r ∗ − r h ​ ( t), w ⁡ ( t) + δ = δ − v ⁡ ( t) ≥ δ − v h ​ ( t), r_{*}-r(t)\geq r_{*}-r_{h}(t),\qquad w(t)+\delta=\delta-v(t)\geq\delta-v_{h}(t), |  | (24.27) |

and ( 24.24) excludes the collar, I − I_{-}, and their corners for every intermediate solution, not only at its endpoints.

The two boundary solutions enter the target block

 | B S v = { − X 0 ≤ x ≤ 0, 0 ≤ y ≤ Y 0 }, x ˙ = x 2 U ( x), y ˙ = − γ ( x, y) y, U, γ ≥ c v > 0, B_{S_{v}}=\{-X_{0}\leq x\leq 0,\ 0\leq y\leq Y_{0}\},\qquad\dot{x}=x^{2}U(x),\quad\dot{y}=-\gamma(x,y)y,\qquad U,\gamma\geq c_{v}>0, |  | (24.28) |

with invariant inner axes and strictly inward outer sides, and therefore both converge to S v S_{v}. This is all that is needed from the target coordinates: the common-time inequalities ( 24.26) are in the upper ( r, v) (r,v) chart, and both their lower and upper bounds converge to the same physical point S v S_{v}. Coordinate-wise squeezing gives ( r ⁡ ( t), v ⁡ ( t)) → S v (r(t),v(t))\to S_{v} for every intermediate solution. No monotonicity of the target coordinate change is assumed. The whole interval is one pp component, whose second boundary is S h → p σ → S v S_{h}\to p_{\sigma}\to S_{v}, not an unrecorded collar limit. A purported residual affine/collar class is already the PP case of Proposition 40. Hence

 | 𝔄 aff = ∅. \mathfrak{A}_{\rm aff}=\varnothing. |  | (24.29) |

All statements above concern one of the finitely many physical stopped words; no connected-component finiteness for a landing-zero set is used. The complete face and port classification, the representative Gronwall estimates, and the finite algebraic identities used above are collected in Appendix D.2. ∎

###### Theorem 41 (Two-Central Exhaustion).

In a sufficiently small full five-parameter neighborhood, every retained exact-once full-lap word on a minimal face and carrying both possible internal central blocks is assigned exactly once to one of

 | two-central no-pp, positive-margin strict lips, middle QBF/QHH, positive root merger, matched source, exact mixed persistent endpoint. \begin{split}&\text{two-central no-pp},\quad\text{positive-margin strict lips},\quad\text{middle QBF/QHH},\quad\text{positive root merger},\\ &\text{matched source},\qquad\text{exact mixed persistent endpoint}.\end{split} |  | (24.30) |

There is no residual analytic regime.

On the complete candidate cover, a passive side, collar exit, wrong-orientation sector, node core, or interval collapse is a terminal pre-word outcome before ( 24.30) is entered. Thus the classification is also exhaustive at the candidate level: terminal passive/exit outcomes remain in the Part I classification, while every actual retained itinerary enters exactly one of the six regimes in ( 24.30).

A landing-gap-separated subcell has zero contribution to the local two-central limit before regime selection. A punctured landing-split fiber near δ hh = 0 \delta_{\rm hh}=0 is not another outcome: its connection constant remains an ambient coefficient of the selected strict, middle, or root row.

###### Remark 42.

The classification is uniform on the finite signed gate, sector, and first-port cover in all five original parameters, including divider collisions and both endpoint charts. A retained itinerary without a complete pp connection enters the no-pp case. A pp itinerary enters the complete-lips case only when the hypotheses of Proposition 40 hold; nearby landing-split fibers remain in the same ambient coefficient cone, whereas a landing-gap-separated cell has no approaching two-central fixed point. In the source/root resolution, t = 0 t=0 enters the source regime, t > 0 t>0, ϱ w = 0 \varrho_{w}=0 the mixed regime, ϱ w ≥ ϱ #\varrho_{w}\geq\varrho_{\#} the middle regime, and 0 < ϱ w < ϱ #0<\varrho_{w}<\varrho_{\#} the root regime; equality belongs to the middle regime. This theorem classifies only itineraries already retained by Part I and plays no role in constructing the stopped atlas.

###### Proof.

Equation ( 24.2) and the unique upper D D -collision give the finite gate alphabet. The sector refinement in Proposition 40 first proves that a retained word with no parabolic connection has same attractivity; an opposite-sign adjacency without a parabolic next-port word is already a stable-center, previous-side, or exit nonword. The retained no-pp words are therefore exactly the two-central no-pp case. Every remaining opposite-sign word has a selected maximal parabolic survivor interval. Proposition 40 refines it into a complete physical lips configuration with its ambient landing-coefficient fibers, a landing-gap-separated cell with zero contribution to the local two-central limit, or a named geometric first-port outcome. On the globally fixed nested tubes of Part I, a complete-lips point outside the inner tube or with t ≥ t str t\geq t_{\rm str} belongs to the strict regime, including equality. Only the pointwise region 0 < t < t str 0<t<t_{\rm str} proceeds to the middle/root weighted split.

It remains to cover a vanishing source/root margin. The finite resolution uses t ≥ 0 t\geq 0 and, for t > 0 t>0, the weighted middle variables

 | b m = B t 2, A m = a t, ϱ w = ( b m 2 + A m 4) 1 / 4. b_{m}=\frac{B}{t^{2}},\qquad A_{m}=\frac{a}{t},\qquad\varrho_{w}=(b_{m}^{2}+A_{m}^{4})^{1/4}. |  | (24.31) |

The weight- ( 2, 1) (2,1) blow-up of the punctured ( b m, A m) (b_{m},A_{m}) -plane has finitely many compact angular charts. In a chart that can retain the horizontal central gate, the leading weak bracket is

 | b + A ​ R ¯ + R ¯ 2. b+A\bar{R}+\bar{R}^{2}. |  | (24.32) |

The double-root equations are b + A ​ R ¯ + R ¯ 2 = 0 b+A\bar{R}+\bar{R}^{2}=0 and A + 2 ​ R ¯ = 0 A+2\bar{R}=0. For a positive retained root, radial normalization therefore puts the angular pair in the signed neighborhoods of ( b, A) = ( 1, − 2) (b,A)=(1,-2) used in ( 26.39) and ( 27.1). On every other angular chart the same quadratic has only simple roots, no positive root, or the wrong crossing sign. The first two alternatives are respectively hyperbolic/one-central or no-passage; the last is passive or exit. At the upper vertex the prepared weak quadratic has only four outcomes: a retained double root, separated simple roots, no root in the retained side, or a root with the wrong transverse sign. These are, respectively, the present D D -gate, hyperbolic boxes, one-central/no-passage, and passive/exit first ports from the finite gate table. Thus an opposite projective chart cannot carry an unlisted two-central pp word.

On the surviving angular charts, ϱ w ≥ ϱ #\varrho_{w}\geq\varrho_{\#}, including equality, is exactly the fixed middle overlap; the parameters have form ( 26.39). For 0 < ϱ w < ϱ #0<\varrho_{w}<\varrho_{\#}, equations ( 27.45)–( 27.46) introduce the positive radial coordinate κ \kappa and give precisely the root chart ( 27.1). The face ϱ w = 0 \varrho_{w}=0 is B = a = 0 B=a=0 and is the exact mixed persistent-endpoint regime. The face t = 0 t=0, including their corner, belongs to the source regime. These four sets cover the weighted resolution and are half-open by construction.

Every failed complete-lips hypothesis or first-port condition is already a named stopped alternative, while the landing coefficient stays in the ambient strict/middle/root coefficient cone; ( 24.29) removes the sole former collar residual. Minimal-face priority assigns the face t = 0 t=0 to source. On t > 0 t>0, it assigns strict first, then middle (including the overlap equality), root, and finally the ϱ w = 0 \varrho_{w}=0 face to mixed. Hence each retained word reaches exactly one row of ( 24.30), while passive, exit, wrong-orientation, node, and collapsed cases remain pre-word outcomes. ∎

###### Theorem 43 (Two-central no-pp theorem).

Let a retained word contain the nonpersistent horizontal and upper D D simple saddle-nodes, both traversed through their central sectors, with same attractivity and no complete pp connection. If all remaining physical sections, connectors, and vertices are certified, the graphic has cyclicity one and an ambient locally uniform finite zero bound.

###### Remark 44.

The theorem is applied only after Theorem 41 has certified the no-pp alternative. Its bound is uniform on an open full-parameter neighborhood of each certified elementary graphic and hence, by a finite cover, on compact families. A complete pp component leaves this case; a split gate becomes hyperbolic or one-central, a persistent endpoint enters the mixed regime, and wrong-attractivity or failed-port outcomes are stopped nonwords.

###### Proof.

The physical sector classification supplies exactly the same-attractivity, no-parabolic-connection hypothesis of the unconditional no-pp clause of DIR2002, Corollary 3.6. That clause gives cyclicity one. We do not use its generic one-pp or two-pp alternatives. Persistence of the certified elementary graphic supplies the ambient neighborhood; faces on which its hypotheses fail have already been assigned to the adjacent regimes. ∎

### 25 The positive-margin strict lips theorem

We now consider complete physical lips configurations from Proposition 40 whose geometric and analytic margins remain positive on a compact base family. DIR coordinates are introduced only at this point: they simplify the already certified central maps and hh connector but create none of the physical hypotheses.

###### Lemma 45 (Physical closing equation in the direct gauges).

Fix a retained complete-lips word with positive coalescence scale in one of the strict, middle, or positive-root regimes. On each fixed parameter fiber, let q ~, v ~ \widetilde{q},\widetilde{v} be the DIR strong-section coordinates and let q, v q,v be the direct action coordinates used in the resolved connector. Then the physical full-lap closing equation is, in the direct coordinates,

 | A 0 ​ 𝒯 ​ ( q) − B 0 ​ q − C 0 = 0. A_{0}{\cal T}(q)-B_{0}q-C_{0}=0. |  | (25.1) |

The changes between the two pairs of section coordinates are affine, and zeros and their multiplicities are preserved. This assertion is fiberwise on the positive-scale regimes; no joint DIR chart through the source or exact mixed face is asserted.

###### Proof.

The section-coordinate reduction in the proof of DIR2002, Theorem 3.1, makes the two central passages q ~ ↦ M ⁡ ( α) ​ q ~ \widetilde{q}\mapsto M(\alpha)\widetilde{q} and v ~ ↦ m ⁡ ( α) ​ v ~ \widetilde{v}\mapsto m(\alpha)\widetilde{v}, with M ​ m ≠ 0 Mm\neq 0, and makes the already certified hh connector v ~ ↦ v ~ + δ ⁡ ( α) \widetilde{v}\mapsto\widetilde{v}+\delta(\alpha). If 𝒯 ~ \widetilde{\cal T} is the pp transition, composing these four actual first hits around the exact-once word gives the physical equation

 | 𝒯 ~ ​ ( q ~) − m − 1 ​ M − 1 ​ q ~ + m − 1 ​ δ = 0. \widetilde{\cal T}(\widetilde{q})-m^{-1}M^{-1}\widetilde{q}+m^{-1}\delta=0. |  | (25.2) |

The direct action coordinates also make the same two strong equations linear. Consequently, on their common fixed-parameter sections,

 | q ~ = a h ​ q + b h, v ~ = a v ​ v + b v, a h ​ a v ≠ 0, \widetilde{q}=a_{h}q+b_{h},\qquad\widetilde{v}=a_{v}v+b_{v},\qquad a_{h}a_{v}\neq 0, |  | (25.3) |

where the four coefficients depend only on the parameter. Hence 𝒯 ~ ​ ( q ~) = a v ​ 𝒯 ​ ( ( q ~ − b h) / a h) + b v \widetilde{\cal T}(\widetilde{q})=a_{v}{\cal T}((\widetilde{q}-b_{h})/a_{h})+b_{v}. Substitution in ( 25.2), followed by the affine change of input, gives ( 25.1), for example with

 | A 0 = a v, B 0 = m − 1 ​ M − 1 ​ a h, C 0 = m − 1 ​ M − 1 ​ b h − m − 1 ​ δ − b v, A_{0}=a_{v},\qquad B_{0}=m^{-1}M^{-1}a_{h},\qquad C_{0}=m^{-1}M^{-1}b_{h}-m^{-1}\delta-b_{v}, |  |

up to multiplication of the triple by a common nonzero factor.

The input change has derivative a h ≠ 0 a_{h}\neq 0, and multiplication of the closing equation by a nonzero parameter factor does not change an isolated zero or its multiplicity. In particular,

 | 𝒯 ~ ′′ ​ ( q ~) = a v a h 2 ​ 𝒯 ′′ ​ ( q ~ − b h a h), \widetilde{\cal T}^{\prime\prime}(\widetilde{q})=\frac{a_{v}}{a_{h}^{2}}{\cal T}^{\prime\prime}\left(\frac{\widetilde{q}-b_{h}}{a_{h}}\right), |  | (25.4) |

so the curvature/Rolle count in the direct gauges counts precisely the physical cycles. On a punctured coefficient chart a common coefficient factor may be divided out; at its radial apex the original displacement is identically zero and has no isolated member. The faces t = 0 t=0 and κ = 0 \kappa=0 are not obtained by extending these gauges: they retain their independent source and exact-mixed assignments. ∎

###### Theorem 46 (Positive-margin strict lips theorem).

Fix one complete physical lips configuration and a compact family K str K_{\rm str} on which the transverse eigenvalues, quadratic weak coefficients, section normals, all-port distances, hh and pp margins, boundary-arc margin, and, only in the PP case, the PP ratio margin are positive. Assume also positive separation from the source and root-merger faces. Then the complete compactified pp phase interval, including its hh and PP/BP endpoints, has a locally uniform finite zero bound for

 | A 0 ​ ( α) ​ R α ​ ( y) − B 0 ​ ( α) ​ y − C 0 ​ ( α) = 0, A_{0}(\alpha)R_{\alpha}(y)-B_{0}(\alpha)y-C_{0}(\alpha)=0, |  | (25.5) |

where

 | ( A 0, B 0, C 0) = ε ( A ^, B ^, C ^), [A ^: B ^: C ^] ∈ ℝ ℙ 2 ( ε ≠ 0). (A_{0},B_{0},C_{0})=\varepsilon(\widehat{A},\widehat{B},\widehat{C}),\qquad[\widehat{A}:\widehat{B}:\widehat{C}]\in\mathbb{RP}^{2}\quad(\varepsilon\neq 0). |  | (25.6) |

The projective direction controls the punctured coefficient neighborhood; ε = 0 \varepsilon=0 is the identity coefficient apex. No certified nonzero direction gives an identity return.

###### Remark 47.

The hypotheses describe two actual opposite saddle-nodes, fixed physical sections, a positive-margin hh itinerary, a nonempty maximal complete pp strip, its complete PP/BP boundary, isolation, and, in the PP case, ( 24.10). The bound is uniform on nested physical tubes and phase intervals in open neighborhoods of all five original parameters; a finite subcover of K str K_{\rm str} gives one constant. The hh and PP/BP phase endpoints are included. Source coalescence, root merger, loss of a section or a complete-lips hypothesis, and a changed first port enter their named adjacent regimes rather than being reached by continuation of this theorem.

###### Proof.

At a base-phase pair ( b, a) (b,a), let m b, a > 0 m_{b,a}>0 be the minimum of all margins listed in the statement. Choose nested physical tubes and phase intervals

 | T b, a − ⋐ T b, a +, I b, a − ⋐ I b, a +, T^{-}_{b,a}\Subset T^{+}_{b,a},\qquad I^{-}_{b,a}\Subset I^{+}_{b,a}, |  | (25.7) |

and an open neighborhood 𝒰 b, a ⊂ ℝ 5 {\cal U}_{b,a}\subset\mathbb{R}^{5} on which every orbit from the inner tube follows the same physical word inside the outer tube.

DIR2002, Theorem 3, gives finite-smooth fibered saddle-node normal forms to any prescribed finite order. Lemma 45 applied in those coordinates gives the physical equation ( 25.5). The proof of Theorem 3.2 makes the critical analytic transition R b R_{b} nonaffine under the certified PP/BP alternatives. Hence at every interior phase point some finite n ≥ 2 n\geq 2 satisfies, after shrinking ( 25.7),

 | inf I b, a + | R b ( n) | ≥ 4 ​ c b, a > 0, ‖ R α ( n) − R b ( n) ‖ C 0 ​ ( I b, a +) < 2 ​ c b, a. \inf_{I^{+}_{b,a}}|R_{b}^{(n)}|\geq 4c_{b,a}>0,\qquad\|R_{\alpha}^{(n)}-R_{b}^{(n)}\|_{C^{0}(I^{+}_{b,a})}<2c_{b,a}. |  | (25.8) |

For ε ≠ 0 \varepsilon\neq 0, divide ( 25.5) by ε \varepsilon. If A ^ ≠ 0 \widehat{A}\neq 0, work only on that projective chart. The affine terms in ( 25.5) vanish after n n derivatives, and multiplicity Rolle gives at most n n zeros on I b, a − I^{-}_{b,a}. On the complementary chart A ^ = 0 \widehat{A}=0, a nonzero affine equation has at most one zero (and a nonzero constant has none), uniformly up to its projective boundary.

At the hh endpoint, analytic continuation of the pp transition supplies a one-sided version of ( 25.8); otherwise R b R_{b} would be affine on the entire connected component. At the natural PP/BP endpoint, the proof-level nonaffine-jet argument in the proof of Theorem 3.2 gives respectively the hyperbolic power/logarithmic asymptotic or the BP length contradiction. Thus both endpoints have their own theorem neighborhoods and are not extrapolated from an interior jet. Finite phase and base subcovers complete the uniform bound. If a nonzero projective direction made ( 25.5) an identity, R b R_{b} would be affine, contradicting the same proof-level nonaffine-jet argument. At ε = 0 \varepsilon=0 the original displacement is identically zero and has no isolated zeros. Since every punctured fiber is controlled by the compact projective-direction cover, the same ambient coefficient cone controls its apex. ∎

### 26 The middle QBF/QHH theorem

The strict theorem cannot be compactified through simultaneous source coalescence. The middle theorem resolves that loss while the horizontal nonpersistent-root scale and the upper D D -gate scale remain comparable. The invariant-center component supplies an exact model, not a perturbation theorem. Uniformity is proved separately on a buffered finite-phase region (QBF) and on an unbounded hyperbolic corner (QHH), then extended in a fixed- γ \gamma resolved frame to the entire middle regime.

Every middle and root comparison below uses the coefficient-cone convention

 | ( A 0, B 0, C 0) = ε c ( A ^ 0, B ^ 0, C ^ 0), [A ^ 0: B ^ 0: C ^ 0] ∈ ℝ ℙ 2 ( ε c ≠ 0). (A_{0},B_{0},C_{0})=\varepsilon_{c}(\widehat{A}_{0},\widehat{B}_{0},\widehat{C}_{0}),\qquad[\widehat{A}_{0}:\widehat{B}_{0}:\widehat{C}_{0}]\in\mathbb{RP}^{2}\quad(\varepsilon_{c}\neq 0). |  | (26.1) |

The projective direction controls the punctured coefficient neighborhood; ε c = 0 \varepsilon_{c}=0 is the identity apex and contributes no isolated zero. Statements below about a zero triple always mean this radial apex, not a point of projective space.

###### Lemma 48 (Scalar first-hit jet and inverse lemma).

Let x ′ = f ⁡ ( τ, x, λ) x^{\prime}=f(\tau,x,\lambda) be a scalar clock equation on a doubled first-hit tube. Suppose the clock normal is separated from zero, every coefficient word of total order at most four has a finite L 1 ​ ( d ​ τ) L^{1}(d\tau) majorant, and the clock endpoints, entry value, entry section, and target section depend mixed C 4 C^{4} -smoothly on the phase and resolved parameters, with all tensors through order four uniformly bounded. Assume also that the entry and target normal determinants, including the oriented phase determinant, are separated from zero on the closed doubled tube. Then the first-hit map and its inverse have uniform mixed C 4 C^{4} bounds and fixed oriented margins 0 < m ≤ P ′ ≤ M 0<m\leq P^{\prime}\leq M.

###### Proof.

For every mixed derivative word I I, differentiation of the scalar flow gives the triangular recurrence

 | ( D I ​ X) ′ = f x ​ D I ​ X + ℬ I, (D_{I}X)^{\prime}=f_{x}D_{I}X+{\cal B}_{I}, |  | (26.2) |

where ℬ I {\cal B}_{I} is the finite Bell-polynomial sum of coefficient derivatives and strictly lower solution jets. Variation of constants and the L 1 L^{1} majorants bound these words inductively. If entry clock a a, target clock b b, entry state x 0 x_{0}, and parameters vary in a direction D D, the first derivative is exactly

 | D ​ P = J ⁡ { D ​ x 0 − f ⁡ ( a, x 0) ​ D ​ a } + Z D + f ⁡ ( b, P) ​ D ​ b, DP=J\{Dx_{0}-f(a,x_{0})Da\}+Z_{D}+f(b,P)Db, |  | (26.3) |

where J = exp ∫ f x d τ J=\exp\int f_{x}\,d\tau and Z D Z_{D} is the fixed-endpoint parameter variation. Differentiating ( 26.3) three more times gives all moving- endpoint tensors; the unique top-order solution jet remains linear.

If C j C_{j} bounds the j j -th mixed tensor of P P and m ≤ P ′ m\leq P^{\prime}, differentiating P ⁡ ( P − 1 ​ ( y, λ), λ) = y P(P^{-1}(y,\lambda),\lambda)=y gives

 | I 1 \displaystyle I_{1} | = m − 1 ​ ( 1 + C 1), \displaystyle=m^{-1}(1+C_{1}), |  | (26.4) |

 | I 2 \displaystyle I_{2} | = m − 1 ​ C 2 ​ ( 1 + I 1) 2, \displaystyle=m^{-1}C_{2}(1+I_{1})^{2}, |  |

 | I 3 \displaystyle I_{3} | = m − 1 ​ { C 3 ​ ( 1 + I 1) 3 + 3 ​ C 2 ​ ( 1 + I 1) ​ I 2 }, \displaystyle=m^{-1}\{C_{3}(1+I_{1})^{3}+3C_{2}(1+I_{1})I_{2}\}, |  |

 | I 4 \displaystyle I_{4} | = m − 1 ​ { C 4 ​ ( 1 + I 1) 4 + 6 ​ C 3 ​ ( 1 + I 1) 2 ​ I 2 + 3 ​ C 2 ​ I 2 2 + 4 ​ C 2 ​ ( 1 + I 1) ​ I 3 }. \displaystyle=m^{-1}\{C_{4}(1+I_{1})^{4}+6C_{3}(1+I_{1})^{2}I_{2}+3C_{2}I_{2}^{2}+4C_{2}(1+I_{1})I_{3}\}. |  |

Finally ( 26.3), multiplied by the clock normal, is the physical entry- section determinant. The two section-normal margins and J J give the two-sided phase bound. ∎

#### 26.1 The invariant-center anchor and its exact transition

For 0 < t < t 0 < 1 / 2 0<t<t_{0}<1/2 and ϵ = ± 1 \epsilon=\pm 1, take the parameters on the invariant-center component

 | B = t 2 1 + t 2, m = − B, a = 2 ​ ϵ ​ t 1 + t 2, c = d = − a. B=\frac{t^{2}}{1+t^{2}},\quad m=-B,\quad a=\frac{2\epsilon t}{1+t^{2}},\quad c=d=-a. |  | (26.5) |

There are two actual simple saddle-nodes

 | S h = ( − ϵ / t, − 1), S v = { r = 0, w = ϵ t }, S_{h}=(-\epsilon/t,-1),\qquad S_{v}=\{r=0,w=\epsilon t\}, |  | (26.6) |

with opposite transverse signs. Their strong separatrices lie on

 | L ϵ = t ​ x − ϵ ​ t 2 ​ z + ϵ = 0. L_{\epsilon}=tx-\epsilon t^{2}z+\epsilon=0. |  | (26.7) |

The component on the side opposite the finite center is a complete pp continuum; its other boundary passes through the single principal endpoint p − ϵ p_{-\epsilon}. Its boundary ratio is t 2 t^{2} or t − 2 t^{-2}, hence is outside [1 / 2, 2] [1/2,2] after shrinking t 0 t_{0}. These assertions follow by substitution in the physical H14 field and by the first-port argument of Proposition 40; no zero count is claimed yet.

Choose analytic strong normalizing coordinates q h, q v q_{h},q_{v} on fixed weak sections at the two saddle-nodes. Along the exact invariant-center pp component the saddle-node first integrals give

 | R t ​ ( q h) = K t ​ q h t 2, K t > 0. R_{t}(q_{h})=K_{t}q_{h}^{t^{2}},\qquad K_{t}>0. |  | (26.8) |

At a reference phase q 0 q_{0}, normalize the value and first derivative:

 | R t ​ ( q 0 ​ ( 1 + u)) − R t ​ ( q 0) q 0 ​ R t ′ ​ ( q 0) = ( 1 + u) t 2 − 1 t 2, \frac{R_{t}(q_{0}(1+u))-R_{t}(q_{0})}{q_{0}R_{t}^{\prime}(q_{0})}=\frac{(1+u)^{t^{2}}-1}{t^{2}}, |  | (26.9) |

with removable value log ⁡ ( 1 + u) \log(1+u) at t = 0 t=0. Uniformly for 0 ≤ t ≤ 1 / 2 0\leq t\leq 1/2 and | u | ≤ 1 / 2 |u|\leq 1/2,

 | d 2 d ​ u 2 ​ ( 1 + u) t 2 − 1 t 2 = ( t 2 − 1) ​ ( 1 + u) t 2 − 2 ≤ − 1 3. \frac{d^{2}}{du^{2}}\frac{(1+u)^{t^{2}}-1}{t^{2}}=(t^{2}-1)(1+u)^{t^{2}-2}\leq-\frac{1}{3}. |  | (26.10) |

Thus the exact model affine comparison has at most two zeros on each normalizing interval. The rest of the section establishes that the relevant concavity survives on physical neighboring words.

#### 26.2 Buffered finite phase and the resolved connector

First use relative parameters

 | B = t 2 ​ b, m = t 2 ​ M, a = t ​ A, c = t ​ C, d = t ​ D, B=t^{2}b,\qquad m=t^{2}M,\qquad a=tA,\qquad c=tC,\qquad d=tD, |  | (26.11) |

with normalized coefficients in a fixed compact neighborhood of either signed invariant-center branch. On the finite-phase region 0 < R = r / t 2 ≤ R L 0<R=r/t^{2}\leq R_{L}, require the same physical first-hit word on the larger buffer R ≤ R L + R\leq R_{L}^{+}. In coherent strong coordinates the transition factors as

 | 𝒯 ⁡ ( q) = H ⁡ ( t 2 ​ log ⁡ q ∗ q), | H ′′ H ′ | ≤ K L. {\cal T}(q)=H\left(t^{2}\log\frac{q_{*}}{q}\right),\qquad\left|\frac{H^{\prime\prime}}{H^{\prime}}\right|\leq K_{L}. |  | (26.12) |

The map H H is the composition of the residual physical regular factors, not an unspecified germ. On the doubled QBF tube every such factor has a scalar clock with denominator and entry/target section normals separated from zero. All coefficient words through order four are bounded on fixed clock intervals. Lemma 48 and the finite Faà di Bruno composition recurrence therefore bound H, H − 1 H,H^{-1} in C 4 C^{4} and bound H ′ H^{\prime} away from zero. This proves the displayed H ′′ / H ′ H^{\prime\prime}/H^{\prime} estimate from the same physical buffers used to define the word. Consequently, for small t t,

 | q ​ 𝒯 ′′ ​ ( q) 𝒯 ′ ​ ( q) = − 1 − t 2 ​ H ′′ H ′ ≤ − 1 2. \frac{q{\cal T}^{\prime\prime}(q)}{{\cal T}^{\prime}(q)}=-1-t^{2}\frac{H^{\prime\prime}}{H^{\prime}}\leq-\frac{1}{2}. |  | (26.13) |

Two applications of multiplicity Rolle show that an affine comparison has at most two isolated zeros on each QBF component.

Large R R is not sent to the source theorem. On every buffered QHH through component the physical connector is decomposed, in the order met by the orbit, as

 | G = P 4 ∘ P 3 ∘ P 2 ∘ P 1 ∘ P 0. G=P_{4}\circ P_{3}\circ P_{2}\circ P_{1}\circ P_{0}. |  | (26.14) |

Here P 0 P_{0} is the horizontal moving-entry bridge, P 1 P_{1} the fixed reciprocal flight, P 2 P_{2} the complete long weighted flight, P 3 P_{3} the fixed core flight, and P 4 P_{4} the moving-entry vertical tail. Moving sections are part of these definitions. In the signed coordinate ξ = − ϵ ​ t ​ x \xi=-\epsilon tx, with s = t 2 ​ z s=t^{2}z, the long factor is resolved by h = s − t 2 = ρ 2 h=s-t^{2}=\rho^{2} and t = ρ ​ T t=\rho T. Put

 | A ^ = − ϵ ​ A, C ^ = − ϵ ​ C, D ^ = − ϵ ​ D. \widehat{A}=-\epsilon A,\qquad\widehat{C}=-\epsilon C,\qquad\widehat{D}=-\epsilon D. |  | (26.15) |

Its exact weighted field is

 | ξ ′ \displaystyle\xi^{\prime} | = ρ 2 ​ B w, \displaystyle=\rho^{2}B_{w}, | ρ ′ \displaystyle\rho^{\prime} | = ρ 2 ​ A w, \displaystyle=\frac{\rho}{2}A_{w}, | T ′ \displaystyle T^{\prime} | = − T 2 ​ A w, \displaystyle=-\frac{T}{2}A_{w}, |  | (26.16) |

 | B w \displaystyle B_{w} | = − 1 + T 2 ​ ξ ​ ( b ​ ξ + A ^) + M ​ ρ 2, \displaystyle=-1+T^{2}\xi(b\xi+\widehat{A})+M\rho^{2}, | A w \displaystyle A_{w} | = ξ ⁡ ( 1 + T 2) + ρ 2 ​ ( T 2 ​ C ^ + D ^). \displaystyle=\xi(1+T^{2})+\rho^{2}(T^{2}\widehat{C}+\widehat{D}). |  |

The resolved norm of a section map is

 | ∥ P ∥ C res 4 = max a + | ν | ≤ 4 sup | ∂ x a 𝒟 ν P |, 𝒟 ∈ { ℰ, ∂ b, ∂ M, ∂ A ^, ∂ C ^, ∂ D ^ }, \|P\|_{C^{4}_{\rm res}}=\max_{a+|\nu|\leq 4}\sup|\partial_{x}^{a}{\mathcal{D}}^{\nu}P|,\qquad{\mathcal{D}}\in\{\mathcal{E},\partial_{b},\partial_{M},\partial_{\widehat{A}},\partial_{\widehat{C}},\partial_{\widehat{D}}\}, |  | (26.17) |

where ℰ \mathcal{E} is the Euler lift on the current section; ordinary unweighted ∂ t \partial_{t} is not in this norm. On the long chart the commuting interior frame is

 | ∂ ξ, 𝒱 2 = ρ ∂ ρ − T ∂ T, ℰ 2 = T ∂ T | ρ, ∂ b, M, A ^, C ^, D ^. \partial_{\xi},\qquad{\cal V}_{2}=\rho\partial_{\rho}-T\partial_{T},\qquad{\cal E}_{2}=T\partial_{T}|_{\rho},\qquad\partial_{b,M,\widehat{A},\widehat{C},\widehat{D}}. |  | (26.18) |

At its moving endpoints the exact lifts are

 | ℰ − = ℰ 2 + 𝒱 2, ℰ + = ℰ 2 − T + 2 ​ 𝒱 2, {\cal E}_{-}={\cal E}_{2}+{\cal V}_{2},\qquad{\cal E}_{+}={\cal E}_{2}-T_{+}^{2}{\cal V}_{2}, |  | (26.19) |

and every resolved derivative word through order four obeys

 | | 𝒲 ⁡ ( 2 ​ ρ ​ B w A w) | ≤ C 𝒲 ​ ρ, ∫ ρ − ρ + C 𝒲 ​ ρ ​ 𝑑 ρ ≤ C 𝒲 ​ s − 2. \left|{\cal W}\left(2\rho\frac{B_{w}}{A_{w}}\right)\right|\leq C_{\cal W}\rho,\qquad\int_{\rho_{-}}^{\rho_{+}}C_{\cal W}\rho\,d\rho\leq\frac{C_{\cal W}s_{-}}{2}. |  | (26.20) |

This integrable estimate, rather than compact convergence in unscaled coordinates, controls the long flight and all moving-endpoint terms.

The other four factors have the following exact clocks. Put σ = − ϵ \sigma=-\epsilon. The horizontal bridge uses z z as clock:

 | R ˙ \displaystyle\dot{R} | = − σ ​ t 2 ​ R ​ { b + σ ​ A ​ R + R 2 ​ [1 − z + t 2 ​ M ​ ( z − 1) 2] } =: N 0, \displaystyle=-\sigma t^{2}R\{b+\sigma AR+R^{2}[1-z+t^{2}M(z-1)^{2}]\}=:N_{0}, |  | (26.21) |

 | z ˙ \displaystyle\dot{z} | = σ z + t 2 R { D ( z − 1) 2 + C ( z − 1) } =: Q 0, d ​ R d ​ z = N 0 Q 0. \displaystyle=\sigma z+t^{2}R\{D(z-1)^{2}+C(z-1)\}=:Q_{0},\qquad\frac{dR}{dz}=\frac{N_{0}}{Q_{0}}. |  |

It starts on the moving strong-section curve ( R 0 ​ ( p), z 0 ​ ( p)) (R_{0}(p),z_{0}(p)), ends at fixed z = z a z=z_{a}, and outputs R − 1 R^{-1}. On the doubled bridge R − ≤ R ≤ R + R_{-}\leq R\leq R_{+}, | Q 0 | ≥ d 0 |Q_{0}|\geq d_{0}, and

 | χ 0 = R 0, p − N 0 Q 0 ​ z 0, p \chi_{0}=R_{0,p}-\frac{N_{0}}{Q_{0}}z_{0,p} |  | (26.22) |

is the physical entry-section determinant divided by Q 0 Q_{0}. Hence 0 < χ 0, − ≤ | χ 0 | ≤ χ 0, + 0<\chi_{0,-}\leq|\chi_{0}|\leq\chi_{0,+}, and every resolved coefficient word in N 0 / Q 0 N_{0}/Q_{0} has an L 1 ​ ( d ​ z) L^{1}(dz) majorant C j ​ t 2 C_{j}t^{2}.

On fixed reciprocal levels v a ≤ v ≤ v b v_{a}\leq v\leq v_{b},

 | d ​ ξ d ​ v = t 2 ​ − v + ξ ⁡ ( b ​ ξ + A ^) + t 2 ​ M ​ v 2 ξ ⁡ ( 1 + v) + t 2 ​ ( C ^ ​ v + D ^ ​ v 2), Q 1 ≥ d 1 > 0. \frac{d\xi}{dv}=t^{2}\frac{-v+\xi(b\xi+\widehat{A})+t^{2}Mv^{2}}{\xi(1+v)+t^{2}(\widehat{C}v+\widehat{D}v^{2})},\qquad Q_{1}\geq d_{1}>0. |  | (26.23) |

Both endpoints are fixed and every coefficient word is L 1 ​ ( d ​ v) L^{1}(dv) -bounded by C j ​ t 2 C_{j}t^{2}. For the compact core put U = ξ + s − 1 U=\xi+s-1. Its exact clock is

 | d ​ U d ​ s = N 3 Q 3, s − ≤ s ≤ s +, Q 3 ≥ c s > 0, \frac{dU}{ds}=\frac{N_{3}}{Q_{3}},\qquad s_{-}\leq s\leq s_{+},\qquad Q_{3}\geq c_{s}>0, |  | (26.24) |

where

 | N 3 = \displaystyle N_{3}={} | s ​ U + ( M + D ^ − 1) ​ s 2 \displaystyle sU+(M+\widehat{D}-1)s^{2} |  | (26.25) |

 |  | + t 2 ​ { 1 + b ​ ( U − s + 1) 2 + A ^ ​ ( U − s + 1) + ( C ^ − 2 ​ D ^ − 2 ​ M) ​ s } \displaystyle+t^{2}\{1+b(U-s+1)^{2}+\widehat{A}(U-s+1)+(\widehat{C}-2\widehat{D}-2M)s\} |  |

 |  | + t 4 ​ ( M + D ^ − C ^), \displaystyle+t^{4}(M+\widehat{D}-\widehat{C}), |  |

 | Q 3 = \displaystyle Q_{3}={} | s ⁡ { U + 1 + ( D ^ − 1) ​ s } + t 2 ​ ( C ^ − 2 ​ D ^) ​ s + t 4 ​ ( D ^ − C ^). \displaystyle s\{U+1+(\widehat{D}-1)s\}+t^{2}(\widehat{C}-2\widehat{D})s+t^{4}(\widehat{D}-\widehat{C}). |  |

This fixed clock interval gives finite L 1 ​ ( d ​ s) L^{1}(ds) bounds for every fourth-order quotient word.

At s = s + s=s_{+}, the exact overlap with the vertical box is

 | R v, 0 = ( s + − t 2) − 1, W 0 = − ϵ ⁡ ( U − s + + 1) ​ ( s + − t 2) − 1. R_{v,0}=(s_{+}-t^{2})^{-1},\qquad W_{0}=-\epsilon(U-s_{+}+1)(s_{+}-t^{2})^{-1}. |  | (26.26) |

In the direct vertical coordinates supplied by the graph transform, write u 0 ​ ( U) u_{0}(U), ℓ 0 ​ ( U) = log ⁡ | v 0 ​ ( U) | \ell_{0}(U)=\log|v_{0}(U)|. The final clock and target are

 | d ​ u d ​ ℓ = F v ​ ( u), ℓ 0 ​ ( U) ⟶ ℓ ∗:= log ⁡ v v ∗. \frac{du}{d\ell}=F_{v}(u),\qquad\ell_{0}(U)\longrightarrow\ell_{*}:=\log v_{v}^{*}. |  | (26.27) |

The entry bracket χ 4 = u 0, U − F v ​ ( u 0) ​ ℓ 0, U \chi_{4}=u_{0,U}-F_{v}(u_{0})\ell_{0,U} is the transported physical s = s + s=s_{+} section-normal determinant. The vertical coordinate Jacobian, the normal eigenvalue, Q 3 Q_{3}, and | v 0 | |v_{0}| all have fixed two-sided margins, and therefore

 | 0 < χ 4, − ≤ | χ 4 | ≤ χ 4, +. 0<\chi_{4,-}\leq|\chi_{4}|\leq\chi_{4,+}. |  | (26.28) |

All coefficient words in F v F_{v} have finite L 1 ​ ( d ​ ℓ) L^{1}(d\ell) bounds on the fixed vertical clock interval.

For P 2 P_{2}, ( 26.20) is the corresponding L 1 L^{1} estimate in logarithmic clock d ​ log ⁡ ρ d\log\rho, with profile C j ​ ρ 2 C_{j}\rho^{2}. Thus the five profiles, in their physical order, are

 | C j ​ t 2 ​ d ​ z, C j ​ t 2 ​ d ​ v, C j ​ ρ 2 ​ d ​ log ⁡ ρ, C j ​ d ​ s, C j ​ d ​ ℓ. C_{j}t^{2}\,dz,\quad C_{j}t^{2}\,dv,\quad C_{j}\rho^{2}\,d\log\rho,\quad C_{j}\,ds,\quad C_{j}\,d\ell. |  | (26.29) |

They are uniformly integrable. Equations ( 26.19), ( 26.22), and ( 26.26)–( 26.28) include every moving endpoint and phase-entry term. Reorient the intermediate local phase coordinates coherently, flipping a shared source/target pair whenever necessary, so that physical order gives P j ′ > 0 P_{j}^{\prime}>0 for all five factors. These flips do not change a first-hit word or an absolute section-normal margin. The absolute derivative bounds above may therefore be multiplied with one common sign. Applying Lemma 48 to the five rows, composing by Faà di Bruno, and using ( 26.4) now gives

 | ‖ G ‖ C res 4 + ‖ G − 1 ‖ C res 4 ≤ C G, 0 < g 0 ≤ G ′ ≤ g 1. \|G\|_{C^{4}_{\rm res}}+\|G^{-1}\|_{C^{4}_{\rm res}}\leq C_{G},\qquad 0<g_{0}\leq G^{\prime}\leq g_{1}. |  | (26.30) |

These are lifted Euler bounds through t = 0 t=0; no ordinary unweighted ∂ t j \partial_{t}^{j} estimate is asserted. The exact local clocks can be chosen as

 | p ˙ = ς h ​ t 2 ​ F h ​ ( p), q ˙ = ς h ​ q, u ˙ = ς v ​ F v ​ ( u), v ˙ = ς v ​ v, \dot{p}=\varsigma_{h}t^{2}F_{h}(p),\quad\dot{q}=\varsigma_{h}q,\qquad\dot{u}=\varsigma_{v}F_{v}(u),\quad\dot{v}=\varsigma_{v}v, |  | (26.31) |

with

 | F v ′′ ≥ c v, | F v ′ ​ ( u) | ≤ L v ​ ( | u | + η), u = G ⁡ ( p). F_{v}^{\prime\prime}\geq c_{v},\qquad|F_{v}^{\prime}(u)|\leq L_{v}(|u|+\eta),\qquad u=G(p). |  | (26.32) |

Let 𝒯 ⁡ ( Q h ​ ( p)) = Q v ​ ( G ⁡ ( p)) {\cal T}(Q_{h}(p))=Q_{v}(G(p)). The curvature numerator is

 | 𝒦 = t 2 ​ F h ​ G ′ − F v ​ ( G) + t 2 ​ F h ​ F v ​ ( G) ​ G ′′ G ′ − t 2 ​ F h ​ F v ′ ​ ( G) ​ G ′ + t 2 ​ F v ​ ( G) ​ F h ′. \begin{split}{\cal K}={}&t^{2}F_{h}G^{\prime}-F_{v}(G)+t^{2}F_{h}F_{v}(G)\frac{G^{\prime\prime}}{G^{\prime}}\\ &-t^{2}F_{h}F_{v}^{\prime}(G)G^{\prime}+t^{2}F_{v}(G)F_{h}^{\prime}.\end{split} |  | (26.33) |

It satisfies

 | d d ​ p ​ log ⁡ d ​ 𝒯 d ​ Q h = 𝒦 t 2 ​ F h ​ F v ​ ( G), 𝒦 ′′ = − F v ′′ ​ ( G) ​ ( G ′) 2 − F v ′ ​ ( G) ​ G ′′ + t 2 ​ ℛ K, | ℛ K | ≤ C K. \frac{d}{dp}\log\frac{d{\cal T}}{dQ_{h}}=\frac{\cal K}{t^{2}F_{h}F_{v}(G)},\quad{\cal K}^{\prime\prime}=-F_{v}^{\prime\prime}(G)(G^{\prime})^{2}-F_{v}^{\prime}(G)G^{\prime\prime}+t^{2}{\cal R}_{K},\quad|{\cal R}_{K}|\leq C_{K}. |  | (26.34) |

Choose the inner vertical interval first, then the parameter radius, and finally t 0 t_{0}, so that

 | | F v ′ ​ ( G) ​ G ′′ | ≤ c v ​ g 0 2 4, t 0 2 ​ C K ≤ c v ​ g 0 2 4. |F_{v}^{\prime}(G)G^{\prime\prime}|\leq\frac{c_{v}g_{0}^{2}}{4},\qquad t_{0}^{2}C_{K}\leq\frac{c_{v}g_{0}^{2}}{4}. |  | (26.35) |

Equations ( 26.32)–( 26.35) imply

 | 𝒦 ′′ ≤ − 1 2 ​ c v ​ g 0 2 < 0. {\cal K}^{\prime\prime}\leq-\frac{1}{2}c_{v}g_{0}^{2}<0. |  | (26.36) |

Hence 𝒦 {\cal K}, and therefore 𝒯 ′′ {\cal T}^{\prime\prime}, has at most two zeros with multiplicity. By Lemma 45, the middle affine comparison is the physical full-lap closing equation

 | A 0 ​ 𝒯 ​ ( q) − B 0 ​ q − C 0 = 0. A_{0}{\cal T}(q)-B_{0}q-C_{0}=0. |  | (26.37) |

If A 0 ≠ 0 A_{0}\neq 0, two more Rolle steps give at most four zeros. If A 0 = 0 A_{0}=0 and B 0 ≠ 0 B_{0}\neq 0, there is at most one; if A 0 = B 0 = 0 A_{0}=B_{0}=0 and C 0 ≠ 0 C_{0}\neq 0, there is none. The zero triple is an identity apex with no isolated zeros. A nonzero projective direction cannot give an identity, since with A 0 ≠ 0 A_{0}\neq 0 that would make 𝒯 {\cal T} affine, contrary to ( 26.36). The horizontal and vertical weak brackets are prepared quadratics on the fixed signed cell. Each contributes at most two divider roots. Four ordered divider points, together with the two side endpoints, cut the input interval into at most five nonempty intervals; scalar uniqueness makes the preimage of every through interval an interval. Hence there are at most five through components, so 20 20 is a valid QHH aggregate bound per signed local word; the number four is per component.

The overlap is assigned once. With R L = 2 ​ R ∗ R_{L}=2R_{*} and R L + = 3 ​ R ∗ R_{L}^{+}=3R_{*},

 | QBF: 0 < R ≤ 3 ​ R ∗ 2, including equality; QHH: R > 3 ​ R ∗ 2. \text{QBF: }0<R\leq\frac{3R_{*}}{2}\text{, including equality};\qquad\text{QHH: }R>\frac{3R_{*}}{2}. |  | (26.38) |

#### 26.3 The full fixed-gamma middle regime

The theorem below uses

 | B = t 2 ​ b, m = t 2 ​ M, a = t ​ A, d = t ​ D, c = γ, B=t^{2}b,\qquad m=t^{2}M,\qquad a=tA,\qquad d=tD,\qquad c=\gamma, |  | (26.39) |

where ( b, M, A, D) (b,M,A,D) stays in a fixed compact signed QL neighborhood and | γ | ≤ γ 0 |\gamma|\leq\gamma_{0}. There is no bound on γ / t \gamma/t. One cannot deduce this case by putting e = t 2 e=t^{2} in ( 26.11), since t ​ γ = γ ​ e t\gamma=\gamma\sqrt{e} is not C 1 C^{1} in e e at zero. Instead the oriented horizontal field, with all outer factors retained, is

 | R ′ = t 2 ​ f ​ ( R, N, t, β γ), N ′ = σ ​ N + t ​ γ s ​ R ​ ( N − R) + t 2 ​ G 0 ​ ( R, N, t, β γ), R^{\prime}=t^{2}f(R,N,t,\beta_{\gamma}),\qquad N^{\prime}=\sigma N+t\gamma_{s}R(N-R)+t^{2}G_{0}(R,N,t,\beta_{\gamma}), |  | (26.40) |

where G 0 G_{0} is polynomial with bounded derivatives and γ s \gamma_{s} is the fixed signed copy of γ \gamma. Writing N = t ​ η N=t\eta gives the regular invariance equation

 | η + t 2 ​ f ​ ( R, t ​ η, t, β γ) ​ η R = γ s ​ R ​ ( t ​ η − R) + t ​ G 0 ​ ( R, t ​ η, t, β γ). \eta+t^{2}f(R,t\eta,t,\beta_{\gamma})\eta_{R}=\gamma_{s}R(t\eta-R)+tG_{0}(R,t\eta,t,\beta_{\gamma}). |  | (26.41) |

The time-one graph transform on a fixed doubled box has limiting weak linear part e − 1 e^{-1}. Shrink t 0, γ 0 t_{0},\gamma_{0} so its phase-jet contraction is at most 3 / 4 3/4. When the fixed-point equation is differentiated with

 | ∂ R, t ∂ t | γ, ∂ b, ∂ M, ∂ A, ∂ D, ∂ γ. \partial_{R},\quad t\partial_{t}|_{\gamma},\quad\partial_{b},\partial_{M},\partial_{A},\partial_{D},\partial_{\gamma}. |  | (26.42) |

the only highest graph jet is multiplied by I − D ​ 𝔗 I-D\mathfrak{T}, whose inverse has norm at most 4 4; all right-hand terms contain bounded coefficient jets and lower graph jets. Induction through order six gives the required entry and normalizer jets and the physical graph N = t ​ η = O ⁡ ( t ​ | γ | + t 2) N=t\eta=O(t|\gamma|+t^{2}). The vertical oriented field is likewise

 | R v ′ \displaystyle R_{v}^{\prime} | = − R v ​ { W + D + t 2 ​ R v ​ W + t ​ γ s ​ R v }, \displaystyle=-R_{v}\{W+D+t^{2}R_{v}W+t\gamma_{s}R_{v}\}, |  | (26.43) |

 | W ′ \displaystyle W^{\prime} | = M − D ​ W − ( 1 − t 2 ​ b) ​ W 2 − R v + t 2 ​ R v ​ ( A ​ W − W 2) − t ​ γ s ​ R v ​ W. \displaystyle=M-DW-(1-t^{2}b)W^{2}-R_{v}+t^{2}R_{v}(AW-W^{2})-t\gamma_{s}R_{v}W. |  |

Its weak polynomial at R v = 0 R_{v}=0 is independent of γ \gamma; the same separated-normal graph, foliation, and fiber recurrences therefore retain ( 26.32) and the moving-entry margin ( 26.28). In the weighted long chart the denominator is

 | A w γ = ξ ⁡ ( 1 + T 2) + ρ ​ T ​ γ + ρ 2 ​ D. A_{w}^{\gamma}=\xi(1+T^{2})+\rho T\gamma+\rho^{2}D. |  | (26.44) |

A ∂ γ \partial_{\gamma} -derivative contributes ρ ​ T = t ≤ C ​ ρ \rho T=t\leq C\rho, so ( 26.20) and hence the five-factor closure remain valid in this frame. The finite core differs from the relative chart by bounded t ​ γ t\gamma -terms. Consequently each of the five rows ( 26.21)–( 26.29) satisfies the hypotheses of Lemma 48 in the fixed- γ \gamma frame; this proves ( 26.30) without an ordinary e = t 2 e=t^{2} derivative.

Finally, the chart must contain every actual middle hh base, not merely a formal neighborhood of the invariant-center component. Construct first the nearby upper-double-root sheet, before imposing the hh landing. Put

 | B = b ​ t 2, a = − t ​ C, c = τ + t ​ C. B=bt^{2},\qquad a=-tC,\qquad c=\tau+tC. |  | (26.45) |

At t = 0 t=0 the three horizontal saddle-node equations are the regular IFT system

 | 1 + b ​ X 2 − C ​ X = 0, X ​ Z h − τ = 0, X ⁡ ( 2 ​ b ​ X − C) = 0. 1+bX^{2}-CX=0,\qquad XZ_{h}-\tau=0,\qquad X(2bX-C)=0. |  | (26.46) |

On the opposite-attractivity branch X = b − 1 / 2 X=b^{-1/2}, C = 2 ​ b C=2\sqrt{b}, Z h = τ ​ b Z_{h}=\tau\sqrt{b}, and the IFT determinant is nonzero. Hence b b is a genuine local coordinate on this two-gate sheet; all remaining endpoint coefficients and entries vary analytically with ( b, t, τ) (b,t,\tau).

It remains to prove that every source-accumulating hh branch enters this local sheet. In the horizontal overlap put

 | U = t ​ x + t 2 ​ z − 1 + t ​ τ, 𝒵 = t 2 ​ z. U=tx+t^{2}z-1+t\tau,\qquad{\cal Z}=t^{2}z. |  | (26.47) |

On each fixed compact ( U, 𝒵) (U,{\cal Z}) -rectangle the exact scaled field and all derivatives needed below converge as t → 0 t\to 0 to

 | U ′ = U ​ 𝒵, 𝒵 ′ = 𝒵 ⁡ ( U + 𝒵 + 1), U^{\prime}=U{\cal Z},\qquad{\cal Z}^{\prime}={\cal Z}(U+{\cal Z}+1), |  | (26.48) |

and the horizontal strong point converges to ( b − 1 / 2 − 1, 0) (b^{-1/2}-1,0). At the upper vertex, with r = t 2 ​ R r=t^{2}R, w = t ​ W w=tW, and η = W + 1 \eta=W+1, the limiting field is

 | R ′ = − R ⁡ ( 1 + η), η ′ = − R − η 2, R^{\prime}=-R(1+\eta),\qquad\eta^{\prime}=-R-\eta^{2}, |  | (26.49) |

whose strong graph is η = R \eta=R. On the common fixed section R = R 0 R=R_{0}, the overlap has 𝒵 = t 2 + R 0 − 1 {\cal Z}=t^{2}+R_{0}^{-1}, and its vertical strong landing converges to U = 0 U=0.

Choose a fixed first-exit rectangle for ( 26.48) with vertical sides U = ± K U=\pm K, then shrink the physical doubled tubes so that the same sides remain transverse for the exact fields. A retained hh branch cannot leave through either side and later re-enter without first taking the named previous-side port. Hence every source-accumulating retained hh sequence has a compact limiting branch ending on U = 0 U=0. Since U = 0 U=0 is invariant for ( 26.48), uniqueness forces that whole limiting branch to be this axis. Its horizontal endpoint therefore satisfies b − 1 / 2 − 1 = 0 b^{-1/2}-1=0, so b → 1 b\to 1. Thus all such hh branches eventually lie inside the common IFT neighborhood above; the local landing computation below is exhaustive, not merely local near a selected base.

We now display the finite- t t system behind that IFT. On the selected upper double-root sheet,

 | m = − t 2 ​ ( 1 − b ​ t 2), d = 2 ​ t ​ ( 1 − b ​ t 2). m=-t^{2}(1-bt^{2}),\qquad d=2t(1-bt^{2}). |  | (26.50) |

In the positive horizontal endpoint chart ( 4.1), put r = t / X r=t/X, z = t ​ Z z=tZ, and set

 | K t ​ ( Z) \displaystyle K_{t}(Z) | = 1 − t ​ Z − t 2 ​ ( 1 − b ​ t 2) ​ ( t ​ Z − 1) 2, \displaystyle=1-tZ-t^{2}(1-bt^{2})(tZ-1)^{2}, |  | (26.51) |

 | F 1 \displaystyle F_{1} | = b ​ X 2 − C ​ X + K t ​ ( Z), \displaystyle=bX^{2}-CX+K_{t}(Z), |  |

 | F 2 \displaystyle F_{2} | = X ​ Z + 2 ​ t ​ ( 1 − b ​ t 2) ​ ( t ​ Z − 1) 2 + ( τ + t ​ C) ​ ( t ​ Z − 1), \displaystyle=XZ+2t(1-bt^{2})(tZ-1)^{2}+(\tau+tC)(tZ-1), |  |

 | F 3 \displaystyle F_{3} | = det D ( X, Z) ​ ( F 1, F 2). \displaystyle=\det D_{(X,Z)}(F_{1},F_{2}). |  |

The exact horizontal saddle-node equations are F 1 = F 2 = F 3 = 0 F_{1}=F_{2}=F_{3}=0. Indeed, F 1 = F 2 = 0 F_{1}=F_{2}=0 are exactly the two equilibrium equations after multiplication by nonvanishing factors, and the determinant condition is preserved by the analytic change ( r, z) = ( t / X, t ​ Z) (r,z)=(t/X,tZ). At t = 0 t=0, ( 26.51) is precisely ( 26.46). Thus the finite- t t equations, not only their limiting system, supply the analytic three-variable IFT.

Put D t = 1 + t 2 D_{t}=1+t^{2}. At b 0 = D t − 1 b_{0}=D_{t}^{-1}, direct differentiation of ( 26.51), with x h = r h − 1 x_{h}=r_{h}^{-1}, gives

 | d d ​ B ​ ( x h + t ​ z h) = − D t 3 2 ​ t 3, ∂ b U ⁡ ( p h) = − D t 3 2. \frac{d}{dB}(x_{h}+tz_{h})=-\frac{D_{t}^{3}}{2t^{3}},\qquad\partial_{b}U(p_{h})=-\frac{D_{t}^{3}}{2}. |  | (26.52) |

This is the derivative of the moving physical strong endpoint. Along the exact invariant line U = 0 U=0, the connector equations reduce to

 | 𝒵 ′ = 1 − t 2 D t ​ ( 1 + 𝒵) ​ ( 𝒵 − 𝒵 h), ∂ U U ′ = 1 − t 2 D t ​ ( 𝒵 − 𝒵 h). {\cal Z}^{\prime}=\frac{1-t^{2}}{D_{t}}(1+{\cal Z})({\cal Z}-{\cal Z}_{h}),\qquad\partial_{U}U^{\prime}=\frac{1-t^{2}}{D_{t}}({\cal Z}-{\cal Z}_{h}). |  | (26.53) |

Along the moving two-gate sheet C = C ⁡ ( b, t, τ) C=C(b,t,\tau), the total parameter derivative is ℬ b = ∂ b + ( ∂ b C) ∂ C \mathcal{B}_{b}=\partial_{b}+(\partial_{b}C)\partial_{C}. Before imposing the hh value, direct substitution in the exact scaled field gives, after removal of its nonvanishing orbital factor,

 | U ′ | U = 0 = − t ⁡ ( − 2 ​ 𝒵 + 1 + t 2 − t ​ τ) ​ Ξ, Ξ = C + b ⁡ ( t 2 + t ​ τ − 1) − 1. U^{\prime}\big|_{U=0}=-t(-2{\cal Z}+1+t^{2}-t\tau)\,\Xi,\qquad\Xi=C+b(t^{2}+t\tau-1)-1. |  | (26.54) |

At b 0 b_{0}, the endpoint IFT values displayed in ( 26.58) give

 | Ξ = 0, ℬ b ​ Ξ = ( 1 − t 2 − t ​ τ) + ( t 2 + t ​ τ − 1) = 0. \Xi=0,\qquad\mathcal{B}_{b}\Xi=(1-t^{2}-t\tau)+(t^{2}+t\tau-1)=0. |  |

The derivative of the omitted orbital factor is multiplied by Ξ = 0 \Xi=0. Thus it is this explicit total cancellation, not a fixed- C C invariance claim, that makes the forcing vanish:

 | ℬ b ​ U ′ | U = 0, b = b 0 = 0. \mathcal{B}_{b}U^{\prime}\big|_{U=0,b=b_{0}}=0. |  | (26.55) |

Thus the normal variation u = ℬ b ​ U u=\mathcal{B}_{b}U, including the ∂ b C \partial_{b}C contribution, satisfies the homogeneous equation

 | d ​ u d ​ 𝒵 = u 1 + 𝒵, u ⁡ ( 𝒵) = u ⁡ ( 𝒵 0) ​ 1 + 𝒵 1 + 𝒵 0. \frac{du}{d{\cal Z}}=\frac{u}{1+{\cal Z}},\qquad u({\cal Z})=u({\cal Z}_{0})\frac{1+{\cal Z}}{1+{\cal Z}_{0}}. |  | (26.56) |

For the vertical branch write its compactified strong graph as η = R ​ H v ​ ( R, b, t, τ) \eta=RH_{v}(R;b,t,\tau). Its exact endpoint slope is

 | h v:= H v ​ ( 0, b, t, τ) = 2 ​ C ​ t 2 − t 2 + t ​ τ − 1 2 ​ b ​ t 2 − 1. h_{v}:=H_{v}(0;b,t,\tau)=\frac{2Ct^{2}-t^{2}+t\tau-1}{2bt^{2}-1}. |  | (26.57) |

At b = b 0 b=b_{0}, the same IFT gives

 | C 0 = 2 − t ​ τ D t, ∂ b C = 1 − t 2 − t ​ τ, h v = 1 − t ​ τ − t 2, ∂ b h v = 0. C_{0}=\frac{2-t\tau}{D_{t}},\qquad\partial_{b}C=1-t^{2}-t\tau,\qquad h_{v}=1-t\tau-t^{2},\qquad\partial_{b}h_{v}=0. |  | (26.58) |

The overlap identities 𝒵 = t 2 + R − 1 {\cal Z}=t^{2}+R^{-1} and U = η / R − 1 + t ​ τ + t 2 U=\eta/R-1+t\tau+t^{2} show that the vertical normal variation has finite endpoint value zero. Every nonzero solution of ( 26.56) is a nonzero multiple of 1 + 𝒵 1+{\cal Z} and is unbounded as R ↓ 0 R\downarrow 0; therefore the admissible vertical variation is identically zero.

Let 𝒵 h = t 2 ​ z h {\cal Z}_{h}=t^{2}z_{h} be the scaled horizontal strong-entry level, and fix the vertical comparison section R = R 0 R=R_{0}, so that M t = t 2 + R 0 − 1 M_{t}=t^{2}+R_{0}^{-1}. Denote by Δ ⁡ ( b, t, τ) \Delta(b,t,\tau) the horizontal strong landing minus the vertical strong landing on this same physical section. At b 0 = ( 1 + t 2) − 1 b_{0}=(1+t^{2})^{-1}, the line

 | x + t ​ z − t − 1 + τ = 0 x+tz-t^{-1}+\tau=0 |  | (26.59) |

is invariant and Δ = 0 \Delta=0. The finite- t t endpoint calculation ( 26.51)–( 26.58), followed by transport along the invariant line, gives

 | ∂ b U h ​ ( M t) | b 0 \displaystyle\partial_{b}U_{h}(M_{t})\big|_{b_{0}} | = − ( 1 + t 2) 3 2 ​ 1 + M t 1 + 𝒵 h, \displaystyle=-\frac{(1+t^{2})^{3}}{2}\frac{1+M_{t}}{1+{\cal Z}_{h}}, |  | (26.60) |

 | ∂ b U v ​ ( M t) | b 0 \displaystyle\partial_{b}U_{v}(M_{t})\big|_{b_{0}} | = 0. \displaystyle=0. |  |

Subtracting the two rows yields

 | ∂ b Δ ⁡ ( b 0, t, τ) = − ( 1 + t 2) 3 2 ​ 1 + M t 1 + 𝒵 h. \partial_{b}\Delta(b_{0},t,\tau)=-\frac{(1+t^{2})^{3}}{2}\frac{1+M_{t}}{1+{\cal Z}_{h}}. |  | (26.61) |

On the two fixed clock intervals the first two b b -variations satisfy

 | v ′ = Φ U ​ v + Φ b, w ′ = Φ U ​ w + Φ U ​ U ​ v 2 + 2 ​ Φ U ​ b ​ v + Φ b ​ b. v^{\prime}=\Phi_{U}v+\Phi_{b},\qquad w^{\prime}=\Phi_{U}w+\Phi_{UU}v^{2}+2\Phi_{Ub}v+\Phi_{bb}. |  | (26.62) |

Their entry jets and all coefficients are bounded, while the vertical graph normal eigenvalue is separated from zero. Gronwall and the bounded overlap therefore give | ∂ b 2 Δ | ≤ C Δ |\partial_{b}^{2}\Delta|\leq C_{\Delta}. On the compact doubled sections, ( 1 + M t) / ( 1 + 𝒵 h) (1+M_{t})/(1+{\cal Z}_{h}) has a fixed positive lower bound, so ( 26.61) gives − ∂ b Δ ( b 0, t, τ) ≥ c Δ > 0 -\partial_{b}\Delta(b_{0},t,\tau)\geq c_{\Delta}>0. Choose the common b b -radius smaller than c Δ / ( 2 ​ C Δ) c_{\Delta}/(2C_{\Delta}). Then ∂ b Δ < − c Δ / 2 \partial_{b}\Delta<-c_{\Delta}/2 throughout the box, and the mean-value theorem proves Δ = 0 \Delta=0 if and only if b = b 0 b=b_{0}.

Substitution of this unique hh value in the two-gate sheet gives the actual base family

 | B = t 2 1 + t 2, m = − t 2 1 + t 2, d = 2 ​ t 1 + t 2, a = − 2 ​ t + t 2 ​ τ 1 + t 2, c = γ = 2 ​ t + τ 1 + t 2. B=\frac{t^{2}}{1+t^{2}},\quad m=-\frac{t^{2}}{1+t^{2}},\quad d=\frac{2t}{1+t^{2}},\quad a=\frac{-2t+t^{2}\tau}{1+t^{2}},\quad c=\gamma=\frac{2t+\tau}{1+t^{2}}. |  | (26.63) |

Thus τ = a + c \tau=a+c is the exact unscaled center departure. The fixed- γ \gamma chart contains the entire source-accumulating middle base locus, including unbounded ( a + c) / t (a+c)/t.

###### Theorem 49 (Middle QBF/QHH theorem).

On every retained complete-lips itinerary in the middle chart ( 26.39), for 0 < t < t 0 0<t<t_{0}, every actual affine pp comparison has at most two isolated zeros on each QBF component and at most four on each QHH component. The estimates are uniform on the full compact normalized base and all | γ | ≤ γ 0 |\gamma|\leq\gamma_{0}, with no restriction on γ / t \gamma/t.

###### Remark 50.

The hypotheses comprise a complete physical lips configuration from Proposition 40, comparable horizontal and upper-gate scales, the parameters ( 26.39), and doubled QBF/QHH physical buffers. The bounds are uniform for 0 < t < t 0 0<t<t_{0} on a fixed compact ( b, M, A, D) (b,M,A,D) -tube, for all allowed γ \gamma, and on the half-open phase split ( 26.38). On coefficient faces we use the cone ( 26.1): for ε c ≠ 0 \varepsilon_{c}\neq 0, curvature applies when A ^ 0 ≠ 0 \widehat{A}_{0}\neq 0, the case A ^ 0 = 0 \widehat{A}_{0}=0, B ^ 0 ≠ 0 \widehat{B}_{0}\neq 0 is affine, and A ^ 0 = B ^ 0 = 0 \widehat{A}_{0}=\widehat{B}_{0}=0, C ^ 0 ≠ 0 \widehat{C}_{0}\neq 0 has no zero. The apex ε c = 0 \varepsilon_{c}=0 is an identity and contributes no isolated zero. A collapsed through interval contributes no isolated point, while neighboring nonempty intervals retain the same estimates. Failure of a denominator, root, clock, side, section normal, target-section landing normal, or first-hit condition stops at its named port; this is loss of the target first-hit tube, not an hh landing split. The outer endpoint-root merger is treated in the next section.

###### Proof.

The QBF estimate is ( 26.13). Equations ( 26.14)–( 26.36) prove the QHH estimate on every actual through component; doubled boxes ensure that the analysis is performed before a first port is reached. The fixed- γ \gamma graph and flow recurrences ( 26.42)–( 26.44) reproduce these estimates uniformly without ordinary e e -smoothness. Equation ( 26.61) supplies physical base exhaustiveness, and Proposition 40 supplies the complete pp strip and boundary. The half-open assignment ( 26.38) covers all phases once. Finite prepared root alphabets give finitely many components, so the component bounds sum to a uniform word bound. ∎

### 27 The positive root-scale triple merger

The final positive-scale regime is the merger of the nonpersistent horizontal double root with the persistent B = a = 0 B=a=0 triple endpoint, while the upper D D -gate remains on its normalized scale. The object is again a complete physical lips itinerary, not merely a weighted polynomial chart. We obtain an explicit bound of 24 24 per signed angular itinerary. The exact source and mixed faces remain the independent theorems of Part II.

Fix σ ∈ { ± 1 } \sigma\in\{\pm 1\} and write

 | B = t 2 ​ κ 2 ​ b, m = t 2 ​ M, a = σ ​ t ​ κ ​ A, d = σ ​ t ​ D, c = σ ​ γ, B=t^{2}\kappa^{2}b,\qquad m=t^{2}M,\qquad a=\sigma t\kappa A,\qquad d=\sigma tD,\qquad c=\sigma\gamma, |  | (27.1) |

where ( b, A, M, D) (b,A,M,D) lies in a compact neighborhood of ( 1, − 2, − 1, 2) (1,-2,-1,2),

 | 0 < t ≤ t 0, 0 < κ ≤ κ 0, | γ | ≤ γ 0. 0<t\leq t_{0},\qquad 0<\kappa\leq\kappa_{0},\qquad|\gamma|\leq\gamma_{0}. |  | (27.2) |

No condition is imposed on γ / t \gamma/t, t / κ t/\kappa, or κ / t \kappa/t. Off the double-root sheet, κ \kappa is the radial variable of the weight- ( 2, 1) (2,1) blow-up of ( B / t 2, a / t) (B/t^{2},a/t); its angular coordinates ( b, A) (b,A) are not simultaneously zero. Thus all five original parameters remain fixed along each physical orbit.

At the horizontal endpoint put

 | u = σ ​ t ​ κ ​ R ¯, N ¯ = R ¯ ​ z. u=\sigma t\kappa\bar{R},\qquad\bar{N}=\bar{R}z. |  | (27.3) |

The prepared weak bracket is

 | H = b + A ​ R ¯ + R ¯ 2 − R ¯ ​ N ¯ + t 2 ​ M ​ ( N ¯ − R ¯) 2, H=b+A\bar{R}+\bar{R}^{2}-\bar{R}\bar{N}+t^{2}M(\bar{N}-\bar{R})^{2}, |  | (27.4) |

so the exact weak factor is

 | e = ( t ​ κ) 2 > 0. e=(t\kappa)^{2}>0. |  | (27.5) |

The exact oriented endpoint field is

 | R ¯ ′ \displaystyle\bar{R}^{\prime} | = − σ ​ t 2 ​ κ 2 ​ R ¯ ​ H, \displaystyle=-\sigma t^{2}\kappa^{2}\bar{R}H, |  | (27.6) |

 | N ¯ ′ \displaystyle\bar{N}^{\prime} | = σ ⁡ { N ¯ + κ ​ t ​ γ ​ R ¯ ​ ( N ¯ − R ¯) + κ ​ t 2 ​ D ​ ( N ¯ − R ¯) 2 − t 2 ​ κ 2 ​ N ¯ ​ H }. \displaystyle=\sigma\{\bar{N}+\kappa t\gamma\bar{R}(\bar{N}-\bar{R})+\kappa t^{2}D(\bar{N}-\bar{R})^{2}-t^{2}\kappa^{2}\bar{N}H\}. |  |

Its time-one graph transform on a fixed doubled box has contraction at most 3 / 4 3/4. The invariant graph is

 | N ¯ = κ ​ η ​ ( R ¯, t, κ, b, M, A, D, γ), \bar{N}=\kappa\eta(\bar{R},t,\kappa,b,M,A,D,\gamma), |  | (27.7) |

and differentiating its fixed-point equation in

 | ∂ R ¯, t ∂ t, κ ∂ κ, ∂ b, ∂ M, ∂ A, ∂ D, ∂ γ \partial_{\bar{R}},\quad t\partial_{t},\quad\kappa\partial_{\kappa},\quad\partial_{b},\partial_{M},\partial_{A},\partial_{D},\partial_{\gamma} |  | (27.8) |

again isolates the highest graph jet under an operator with inverse norm at most 4 4. Thus its mixed jets through order six are bounded. On this graph,

 | H gr = b + A ​ R ¯ + ( 1 + t 2 ​ M) ​ R ¯ 2 − κ ⁡ ( 1 + 2 ​ t 2 ​ M) ​ R ¯ ​ η + κ 2 ​ t 2 ​ M ​ η 2, H_{\rm gr}=b+A\bar{R}+(1+t^{2}M)\bar{R}^{2}-\kappa(1+2t^{2}M)\bar{R}\eta+\kappa^{2}t^{2}M\eta^{2}, |  | (27.9) |

so ∂ R ¯ 2 ( H gr − b − A ​ R ¯) > c h > 0 \partial_{\bar{R}}^{2}(H_{\rm gr}-b-A\bar{R})>c_{h}>0. The graph, foliation, and finite fiber-linearization recurrences have denominators

 | | k ​ ς h − j ​ e ​ F h ′ ​ ( p) | ≥ 1 2, k ≥ 1, 0 ≤ j ≤ 6, |k\varsigma_{h}-jeF_{h}^{\prime}(p)|\geq\tfrac{1}{2},\qquad k\geq 1,\quad 0\leq j\leq 6, |  | (27.10) |

and supply the direct weak coordinates used below, with bounded inverses. The physical connector has five factors

 | G rt = P 4 rt ∘ P 3 out ∘ P 2 rt ∘ P 1 rt ∘ P 0 rt. G_{\rm rt}=P_{4}^{\rm rt}\circ P_{3}^{\rm out}\circ P_{2}^{\rm rt}\circ P_{1}^{\rm rt}\circ P_{0}^{\rm rt}. |  | (27.11) |

Here u = 1 / x = σ ​ t ​ κ ​ R ¯ u=1/x=\sigma t\kappa\bar{R} and ξ = σ ​ t ​ x = σ ​ t / u = X / κ \xi=\sigma tx=\sigma t/u=X/\kappa is the signed scaled horizontal coordinate; s = t 2 ​ z s=t^{2}z is the physical overlap coordinate. The first bridge uses X = κ ​ ξ = 1 / R ¯ X=\kappa\xi=1/\bar{R}, the second fixed reciprocal levels, and the long overlap uses h = s − t 2 = ρ 2 h=s-t^{2}=\rho^{2}, t = ρ ​ T t=\rho T. The first three factor clocks are exact. From the moving horizontal strong section to fixed z = z a > 1 z=z_{a}>1,

 | d ​ R ¯ d ​ z = − e ​ R ¯ ​ H z + κ ​ t ​ γ ​ R ¯ ​ ( z − 1) + κ ​ t 2 ​ D ​ R ¯ ​ ( z − 1) 2, Q 0 ≥ d 0 > 0. \frac{d\bar{R}}{dz}=-\frac{e\bar{R}H}{z+\kappa t\gamma\bar{R}(z-1)+\kappa t^{2}D\bar{R}(z-1)^{2}},\qquad Q_{0}\geq d_{0}>0. |  | (27.12) |

The moving-entry phase bracket is again ( 26.3), and after multiplication by Q 0 Q_{0} it is the physical section-normal determinant. The direct normalizer and fixed strong-section normal therefore give 0 < m 0 ≤ | ( P 0 rt) ′ | ≤ M 0 0<m_{0}\leq|(P_{0}^{\rm rt})^{\prime}|\leq M_{0}. On fixed reciprocal levels,

 | d ​ X d ​ v = e ​ − v + X ⁡ ( b ​ X + A) + t 2 ​ M ​ v 2 X ⁡ ( 1 + v) + κ ​ t ​ γ ​ v + κ ​ t 2 ​ D ​ v 2, Q 1 ≥ d 1 > 0. \frac{dX}{dv}=e\,\frac{-v+X(bX+A)+t^{2}Mv^{2}}{X(1+v)+\kappa t\gamma v+\kappa t^{2}Dv^{2}},\qquad Q_{1}\geq d_{1}>0. |  | (27.13) |

Both endpoints are fixed. On the long overlap,

 | d ​ X d ​ ρ = 2 ​ κ 2 ​ ρ ​ − 1 + T 2 ​ X ​ ( b ​ X + A) + M ​ ρ 2 X ⁡ ( 1 + T 2) + κ ​ ρ ​ T ​ γ + κ ​ ρ 2 ​ D, A κ ≥ a κ > 0. \frac{dX}{d\rho}=2\kappa^{2}\rho\,\frac{-1+T^{2}X(bX+A)+M\rho^{2}}{X(1+T^{2})+\kappa\rho T\gamma+\kappa\rho^{2}D},\qquad A_{\kappa}\geq a_{\kappa}>0. |  | (27.14) |

Its endpoints and Euler lifts are

 | ρ − = t v b, ρ + = s − − t 2, ℰ t − = ℰ t, 2 + ρ ∂ ρ − T ∂ T, ℰ t + = ℰ t, 2 − t 2 s − − t 2 ( ρ ∂ ρ − T ∂ T). \begin{gathered}\rho_{-}=t\sqrt{v_{b}},\qquad\rho_{+}=\sqrt{s_{-}-t^{2}},\\ {\cal E}^{t}_{-}={\cal E}_{t,2}+\rho\partial_{\rho}-T\partial_{T},\qquad{\cal E}^{t}_{+}={\cal E}_{t,2}-\frac{t^{2}}{s_{-}-t^{2}}(\rho\partial_{\rho}-T\partial_{T}).\end{gathered} |  | (27.15) |

All κ \kappa - and γ \gamma -derivatives of these geometric endpoints vanish. Resolved coefficient words in ( 27.12), ( 27.13), and ( 27.14) have the respective L 1 L^{1} profiles

 | C j ​ e ​ d ​ z, C j ​ e ​ d ​ v, C j ​ κ 2 ​ ρ ​ d ​ ρ. C_{j}e\,dz,\qquad C_{j}e\,dv,\qquad C_{j}\kappa^{2}\rho\,d\rho. |  | (27.16) |

Thus Lemma 48 gives direct and inverse C res 4 C^{4}_{\rm res} bounds and two-sided phase margins for P 0 rt, P 1 rt, P 2 rt P_{0}^{\rm rt},P_{1}^{\rm rt},P_{2}^{\rm rt}, uniformly at every imbalance allowed by ( 27.2). The genuinely phase-dependent outer transfer is written

 | S = κ ​ s, Y = κ ⁡ ( ξ + s), X = Y − S, κ = S ​ K, S=\kappa s,\qquad Y=\kappa(\xi+s),\qquad X=Y-S,\qquad\kappa=SK, |  | (27.17) |

and the final factor lands in the upper variables

 | R v = ( s − t 2) − 1 = κ ​ R ¯ v, W = σ ​ ξ s − t 2. R_{v}=(s-t^{2})^{-1}=\kappa\bar{R}_{v},\qquad W=\frac{\sigma\xi}{s-t^{2}}. |  | (27.18) |

These coordinates preserve the essential product S ​ K SK; the proof never estimates the outer factor on an inadmissible independent ( S, K) (S,K) -box. More precisely, with X = Y − S X=Y-S,

 | P ~ = \displaystyle\widetilde{P}={} | X + ( M + D) ​ S + S ​ K ​ { − 1 + t ​ γ − 2 ​ t 2 ​ ( M + D) } \displaystyle X+(M+D)S+SK\{-1+t\gamma-2t^{2}(M+D)\} |  | (27.19) |

 |  | + S ​ K 2 ​ { t 2 ​ ( 1 + b ​ X 2 + A ​ X) + t 4 ​ ( M + D) − t 3 ​ γ }, \displaystyle+SK^{2}\{t^{2}(1+bX^{2}+AX)+t^{4}(M+D)-t^{3}\gamma\}, |  |

 | Q ~ = \displaystyle\widetilde{Q}={} | X + D ​ S + S ​ K ​ ( t ​ γ − 2 ​ t 2 ​ D) + S ​ K 2 ​ ( t 4 ​ D − t 3 ​ γ), \displaystyle X+DS+SK(t\gamma-2t^{2}D)+SK^{2}(t^{4}D-t^{3}\gamma), |  |

and the exact desingularized outer field is

 | Y ′ = S ​ P ~, S ′ = S ​ Q ~, K ′ = − K ​ Q ~, ( S ​ K) ′ = 0. Y^{\prime}=S\widetilde{P},\qquad S^{\prime}=S\widetilde{Q},\qquad K^{\prime}=-K\widetilde{Q},\qquad(SK)^{\prime}=0. |  | (27.20) |

The doubled physical wedge is chosen so that Q ~ ≥ q 0 > 0 \widetilde{Q}\geq q_{0}>0; hence S S is a valid clock and the physical quotient is

 | d ​ Y d ​ S = P ~ Q ~. \frac{dY}{dS}=\frac{\widetilde{P}}{\widetilde{Q}}. |  | (27.21) |

Thus the outer map is a first hit on the fixed original- κ \kappa leaf, not a map on an independent ( S, K) (S,K) -rectangle.

Here is the promised first-exit and landing estimate. The physical wedge is

 | 𝒲 3 = { 0 ≤ S ≤ S ∗, 0 ≤ K ≤ K ∗:= s − − 1, 0 ≤ S K = κ ≤ κ 0 }. {\cal W}_{3}=\{0\leq S\leq S_{*},\ 0\leq K\leq K_{*}:=s_{-}^{-1},\ 0\leq SK=\kappa\leq\kappa_{0}\}. |  | (27.22) |

Thus every derivative descendant containing K K retains either S ​ K SK or S ​ K 2 = ( S ​ K) ​ K SK^{2}=(SK)K; these products are bounded on 𝒲 3 {\cal W}_{3}. At the reference face κ = 0 \kappa=0, M = − 1 M=-1, D = 2 D=2, the quotient is

 | d ​ Y d ​ S = Y Y + S, S = Y ​ log ⁡ Y X 0, 0 < X − ≤ X 0 ≤ X +, \frac{dY}{dS}=\frac{Y}{Y+S},\qquad S=Y\log\frac{Y}{X_{0}},\qquad 0<X_{-}\leq X_{0}\leq X_{+}, |  | (27.23) |

and Q ~ = Y + S ≥ X − > 0 \widetilde{Q}=Y+S\geq X_{-}>0. Choose the finite target S ∗ S_{*} so this compact reference family enters the interior of the fixed vertical weak buffer, and choose a doubled tube around it with distance δ ∗ > 0 \delta_{*}>0 from every nontarget side.

On that tube the explicit polynomials ( 27.19) give constants C ∗, L ∗ C_{*},L_{*} such that

 | | P ~ Q ~ − Y Y + S | ≤ C ∗ ​ η ∗, | ∂ Y P ~ Q ~ | ≤ L ∗, \left|\frac{\widetilde{P}}{\widetilde{Q}}-\frac{Y}{Y+S}\right|\leq C_{*}\eta_{*},\qquad\left|\partial_{Y}\frac{\widetilde{P}}{\widetilde{Q}}\right|\leq L_{*}, |  | (27.24) |

where η ∗ \eta_{*} is the radius of the angular, t t, κ \kappa, and γ \gamma neighborhood. Fix those radii so that

 | C ∗ ​ η ∗ ​ S ∗ ​ e L ∗ ​ S ∗ < δ ∗ / 2, Q ~ ≥ X − / 2. C_{*}\eta_{*}S_{*}e^{L_{*}S_{*}}<\delta_{*}/2,\qquad\widetilde{Q}\geq X_{-}/2. |  | (27.25) |

Gronwall then keeps every flight in the doubled wedge until its first hit of S = S ∗ S=S_{*}, and its endpoint remains inside the vertical buffer. Therefore no nontarget side is crossed and the landing is a genuine first hit. The phase variation is exp ∫ 0 S ∗ ∂ Y ( P ~ / Q ~) d S \exp\int_{0}^{S_{*}}\partial_{Y}(\widetilde{P}/\widetilde{Q})\,dS, so it has fixed positive upper and lower bounds. At S = 0 S=0 the exceptional K K -segment is the identity in Y Y; at K = 0 K=0 ( 27.23) is the limiting scalar flight. No derivative across these two faces is introduced.

At the target, the exact upper entry is

 | R ¯ v, 0 = 1 S ∗ − κ ​ t 2, W 0 = σ ​ X ∗ S ∗ − κ ​ t 2. \bar{R}_{v,0}=\frac{1}{S_{*}-\kappa t^{2}},\qquad W_{0}=\frac{\sigma X_{*}}{S_{*}-\kappa t^{2}}. |  | (27.26) |

The outer landing derivative is positive by ( 27.24)–( 27.25), so we may use the landing value X ∗ X_{*} itself as the local phase coordinate. Its target phase tangent is therefore

 | η Y:= ∂ X ∗ ( R ¯ v, 0, W 0) = ( 0, σ S ∗ − κ ​ t 2). \eta_{Y}:=\partial_{X_{*}}(\bar{R}_{v,0},W_{0})=\left(0,\frac{\sigma}{S_{*}-\kappa t^{2}}\right). |  | (27.27) |

With D s = σ ​ D D_{s}=\sigma D, A s = σ ​ A A_{s}=\sigma A, and γ s = σ ​ γ \gamma_{s}=\sigma\gamma, the vertical field is

 | R ¯ v ′ \displaystyle\bar{R}_{v}^{\prime} | = − R ¯ v ​ { W + D s + κ ​ t 2 ​ R ¯ v ​ W + κ ​ t ​ γ s ​ R ¯ v }, \displaystyle=-\bar{R}_{v}\{W+D_{s}+\kappa t^{2}\bar{R}_{v}W+\kappa t\gamma_{s}\bar{R}_{v}\}, |  | (27.28) |

 | W ′ \displaystyle W^{\prime} | = M − D s ​ W − ( 1 − t 2 ​ κ 2 ​ b) ​ W 2 − κ ​ R ¯ v \displaystyle=M-D_{s}W-(1-t^{2}\kappa^{2}b)W^{2}-\kappa\bar{R}_{v} |  |

 |  | + κ ​ t 2 ​ R ¯ v ​ ( κ ​ A s ​ W − W 2) − κ ​ t ​ γ s ​ R ¯ v ​ W. \displaystyle+\kappa t^{2}\bar{R}_{v}(\kappa A_{s}W-W^{2})-\kappa t\gamma_{s}\bar{R}_{v}W. |  |

At κ = 0 \kappa=0 its weak polynomial is M − D s ​ W − W 2 M-D_{s}W-W^{2}, while the transverse normal W c + D s W_{c}+D_{s} is separated from zero on the D D -collision cell. The same 3 / 4 3/4 graph-transform and finite fiber recurrences therefore give direct coordinates

 | u ′ = ς v ​ F v ​ ( u), v ¯ ′ = ς v ​ v ¯, F v ′′ ≥ c v > 0, | F v ′ ​ ( u) | ≤ L v ​ ( | u | + η v). u^{\prime}=\varsigma_{v}F_{v}(u),\qquad\bar{v}^{\prime}=\varsigma_{v}\bar{v},\qquad F_{v}^{\prime\prime}\geq c_{v}>0,\qquad|F_{v}^{\prime}(u)|\leq L_{v}(|u|+\eta_{v}). |  | (27.29) |

If Q v Q_{v} denotes the full brace in the first row of ( 27.28), the phase tangent of ( 27.26) has exact physical determinant

 | det ( η Y, X v) = σ ​ Q v ( S ∗ − κ ​ t 2) 2. \det(\eta_{Y},X_{v})=\frac{\sigma Q_{v}}{(S_{*}-\kappa t^{2})^{2}}. |  | (27.30) |

The direct-coordinate Jacobian, Q v Q_{v}, the target normal v ¯ v ∗ \bar{v}_{v}^{*}, and S ∗ − κ ​ t 2 S_{*}-\kappa t^{2} have fixed two-sided margins. Formula ( 26.3) therefore gives

 | 0 < m 4 ≤ | ( P 4 rt) ′ | ≤ M 4, P 4 rt, ( P 4 rt) − 1 ∈ C res 4. 0<m_{4}\leq|(P_{4}^{\rm rt})^{\prime}|\leq M_{4},\qquad P_{4}^{\rm rt},(P_{4}^{\rm rt})^{-1}\in C^{4}_{\rm res}. |  | (27.31) |

For root factors, C res 4 C^{4}_{\rm res} means all phase derivatives and all words of total length at most four in

 | t ∂ t, κ ∂ κ, ∂ b, ∂ M, ∂ A, ∂ D, ∂ γ. t\partial_{t},\quad\kappa\partial_{\kappa},\quad\partial_{b},\partial_{M},\partial_{A},\partial_{D},\partial_{\gamma}. |  | (27.32) |

On the long chart this is represented by

 | ∂ X, ρ ∂ ρ − T ∂ T, T ∂ T | ρ, κ ∂ κ, ∂ b, M, A, D, γ, \partial_{X},\quad\rho\partial_{\rho}-T\partial_{T},\quad T\partial_{T}|_{\rho},\quad\kappa\partial_{\kappa},\quad\partial_{b,M,A,D,\gamma}, |  | (27.33) |

and on the outer wedge by

 | ∂ Y, S ∂ S − K ∂ K, K ∂ K, t ∂ t, ∂ b, M, A, D, γ. \partial_{Y},\quad S\partial_{S}-K\partial_{K},\quad K\partial_{K},\quad t\partial_{t},\quad\partial_{b,M,A,D,\gamma}. |  | (27.34) |

The overlap matrices and moving-endpoint lifts are bounded on the doubled wedges. Every nonzero derivative descendant containing K K retains the factor S ​ K = κ SK=\kappa, which is the closure needed for ( 27.36).

For the outer factor the exact entry and target data are

 | S in = κ ​ s −, K in = s − − 1, Y in = X + κ ​ s −, S out = S ∗, K out = κ S ∗. S_{\rm in}=\kappa s_{-},\quad K_{\rm in}=s_{-}^{-1},\quad Y_{\rm in}=X+\kappa s_{-},\qquad S_{\rm out}=S_{*},\quad K_{\rm out}=\frac{\kappa}{S_{*}}. |  | (27.35) |

All resolved endpoint words are bounded. On ( 27.22), every fourth-order word in P ~ / Q ~ \widetilde{P}/\widetilde{Q} is bounded in L 1 ​ ( d ​ S) L^{1}(dS) because Q ~ ≥ X − / 2 \widetilde{Q}\geq X_{-}/2 and the only K K -terms occur through the bounded products S ​ K, S ​ K 2 SK,SK^{2}. Lemma 48, ( 27.25), and ( 27.35) therefore give direct and inverse C res 4 C^{4}_{\rm res} bounds and a two-sided phase margin for P 3 out P_{3}^{\rm out}, including its two limiting faces. Equation ( 27.31) gives the same conclusion for P 4 rt P_{4}^{\rm rt}.

Reorient the five local phase coordinates coherently along the retained physical word. Flipping a shared source/target pair preserves every absolute determinant estimate and makes each factor orientation preserving. Thus the two-sided absolute margins above imply positive derivatives for all five factors simultaneously, rather than five unrelated signs.

Thus all five factors satisfy the scalar first-hit lemma. Their coefficient profiles are O ⁡ ( e) O(e), O ⁡ ( e) O(e), O ⁡ ( κ 2 ​ ρ) O(\kappa^{2}\rho), O ⁡ ( 1) O(1), and O ⁡ ( 1) O(1) on the five displayed finite or integrable clocks. Faà di Bruno composition through order four and the inverse recurrence ( 26.4) give

 | ‖ G rt ‖ C res 4 + ‖ G rt − 1 ‖ C res 4 ≤ C G, 0 < g 0 ≤ G rt ′ ≤ g 1. \|G_{\rm rt}\|_{C^{4}_{\rm res}}+\|G_{\rm rt}^{-1}\|_{C^{4}_{\rm res}}\leq C_{G},\qquad 0<g_{0}\leq G_{\rm rt}^{\prime}\leq g_{1}. |  | (27.36) |

Here g 0 = ∏ j = 0 4 m j g_{0}=\prod_{j=0}^{4}m_{j} and g 1 = ∏ j = 0 4 M j g_{1}=\prod_{j=0}^{4}M_{j}. The bound is uniform on the compact angular base and under all imbalances allowed in ( 27.2). The finite symbolic calculation expands derivative words only for the displayed polynomial numerator/denominator factors; the physical order ( 27.11), first-port margins, and through-component construction are proved analytically here.

Let F h, F v F_{h},F_{v} be the prepared horizontal and vertical weak polynomials in the direct coordinates, with F v ′′ ≥ c v > 0 F_{v}^{\prime\prime}\geq c_{v}>0, and set G = G rt G=G_{\rm rt}. The transition obeys

 | Q h ′ Q h = 1 e ​ F h, Q v ′ Q v = 1 F v, 𝒯 ⁡ ( Q h ​ ( p)) = Q v ​ ( G ⁡ ( p)). \frac{Q_{h}^{\prime}}{Q_{h}}=\frac{1}{eF_{h}},\qquad\frac{Q_{v}^{\prime}}{Q_{v}}=\frac{1}{F_{v}},\qquad{\cal T}(Q_{h}(p))=Q_{v}(G(p)). |  | (27.37) |

Define

 | 𝒦 rt = e ​ F h ​ G ′ − F v ​ ( G) + e ​ F h ​ F v ​ ( G) ​ G ′′ G ′ − e ​ F h ​ F v ′ ​ ( G) ​ G ′ + e ​ F v ​ ( G) ​ F h ′. \begin{split}{\cal K}_{\rm rt}={}&eF_{h}G^{\prime}-F_{v}(G)+eF_{h}F_{v}(G)\frac{G^{\prime\prime}}{G^{\prime}}\\ &-eF_{h}F_{v}^{\prime}(G)G^{\prime}+eF_{v}(G)F_{h}^{\prime}.\end{split} |  | (27.38) |

Then

 | d d ​ p ​ log ⁡ d ​ 𝒯 d ​ Q h = 𝒦 rt e ​ F h ​ F v ​ ( G), \frac{d}{dp}\log\frac{d{\cal T}}{dQ_{h}}=\frac{{\cal K}_{\rm rt}}{eF_{h}F_{v}(G)}, |  | (27.39) |

and exact differentiation gives

 | 𝒦 rt ′′ = − F v ′′ ​ ( G) ​ ( G ′) 2 − F v ′ ​ ( G) ​ G ′′ + e ​ ℛ rt, | ℛ rt | ≤ C K. {\cal K}_{\rm rt}^{\prime\prime}=-F_{v}^{\prime\prime}(G)(G^{\prime})^{2}-F_{v}^{\prime}(G)G^{\prime\prime}+e{\cal R}_{\rm rt},\qquad|{\cal R}_{\rm rt}|\leq C_{K}. |  | (27.40) |

Choose the fixed vertical inner interval first so that | F v ′ ​ ( G) ​ G ′′ | ≤ c v ​ g 0 2 / 4 |F_{v}^{\prime}(G)G^{\prime\prime}|\leq c_{v}g_{0}^{2}/4, and then shrink t 0, κ 0 t_{0},\kappa_{0} until ( t 0 ​ κ 0) 2 ​ C K ≤ c v ​ g 0 2 / 4 (t_{0}\kappa_{0})^{2}C_{K}\leq c_{v}g_{0}^{2}/4. It follows that

 | 𝒦 rt ′′ ≤ − 1 2 ​ c v ​ g 0 2 < 0. {\cal K}_{\rm rt}^{\prime\prime}\leq-\frac{1}{2}c_{v}g_{0}^{2}<0. |  | (27.41) |

Thus 𝒯 ′′ {\cal T}^{\prime\prime} has at most two zeros with multiplicity. By Lemma 45, the affine comparison is the physical full-lap closing equation; two further Rolle steps give at most four zeros on each through component. Strict convexity of each prepared horizontal and vertical weak bracket gives at most two roots. Their inverse images contribute at most four internal divider points. The persistent side contributes at most one additional divider; scalar uniqueness preserves their order and makes each surviving preimage an interval. Hence at most five divider points cut a signed angular word into at most six through components.

###### Theorem 51 (Positive root-scale triple-merger theorem).

For every retained complete-lips physical root-scale word ( 27.1)–( 27.2), with the doubled five-factor first-hit buffers used above, every comparison

 | A 0 ​ 𝒯 ​ ( q) − B 0 ​ q − C 0 = 0 A_{0}{\cal T}(q)-B_{0}q-C_{0}=0 |  | (27.42) |

has at most four isolated zeros, counted with multiplicity, on each connected through component. Consequently there are at most

 | 6 ⋅ 4 = 24 6\cdot 4=24 |  | (27.43) |

isolated zeros per signed angular word. The bound is ambient under positive t t, positive κ \kappa split-root, landing-split, no-root, coefficient, and identity specializations in the same stopped word.

###### Remark 52.

The bound is uniform on the compact angular base for all 0 < t ≤ t 0 0<t\leq t_{0}, 0 < κ ≤ κ 0 0<\kappa\leq\kappa_{0}, and | γ | ≤ γ 0 |\gamma|\leq\gamma_{0}, without a hidden bound on any ratio of these variables. On ε c ≠ 0 \varepsilon_{c}\neq 0 we use the projective direction in ( 26.1). If A ^ 0 ≠ 0 \widehat{A}_{0}\neq 0, ( 27.41) gives strict curvature; if A ^ 0 = 0 \widehat{A}_{0}=0, B ^ 0 ≠ 0 \widehat{B}_{0}\neq 0, ( 27.42) has at most one isolated zero; and if A ^ 0 = B ^ 0 = 0 \widehat{A}_{0}=\widehat{B}_{0}=0, C ^ 0 ≠ 0 \widehat{C}_{0}\neq 0, it has none. The apex ε c = 0 \varepsilon_{c}=0 is an identity with no isolated zeros, while ( 27.41) excludes an identity in a nonzero projective direction. At the boundary, loss of a denominator, section normal, weak box, target-section landing normal, or first hit stops at the named adjacent regime. A collapsed interval or changed itinerary is not continued through ( 27.11).

###### Proof.

Equations ( 27.3)–( 27.36) construct the five factors on the same actual physical word and provide the uniform direct and inverse phase bounds. Equations ( 27.37)–( 27.41) give strict curvature. Multiplicity Rolle and the six-component prepared-root count yield ( 27.43). Coefficient and identity faces are handled in the ambient comparison as stated. Every physical loss of the five-factor word is stopped before the analytic estimate is invoked, so no non-through component is counted as a root-scale cycle. ∎

Before subtracting the outer middle overlap, the zero-scale theorem-validity handoff is half-open and exact:

 | t = 0 ( including ​ t = κ = 0) ⟶ matched source theorem, t > 0, κ = 0 ⟶ exact mixed persistent- ​ D ​ theorem, t > 0, 0 < κ ≤ κ 0 ⟶ positive root theorem. \begin{array}[]{rcl}t=0\quad(\text{including }t=\kappa=0)&\longrightarrow&\text{matched source theorem},\\ t>0,\ \kappa=0&\longrightarrow&\text{exact mixed persistent-}D\text{ theorem},\\ t>0,\ 0<\kappa\leq\kappa_{0}&\longrightarrow&\text{positive root theorem}.\end{array} |  | (27.44) |

At κ = 0 \kappa=0, ( 27.1) gives exactly B = a = 0 B=a=0, where the persistent triple endpoint changes the physical transition. At t = 0 t=0, the return is the matched noncompact source problem. Neither face follows by continuity from a positive- e e curvature estimate; they are the independent mixed and source theorems proved in Part II.

For clarity, the positive-scale regime partition is fixed before any zero theorem is applied. Use the nested coalescing tubes and the fixed value t str t_{\rm str} chosen in Part I. After named first-port losses are removed, a complete-lips point outside the inner tube or with t ≥ t str t\geq t_{\rm str} is in the strict regime, including equality. On the pointwise region 0 < t < t str 0<t<t_{\rm str} use the middle variables b m = B / t 2 b_{m}=B/t^{2}, A m = a / t A_{m}=a/t and the weighted radius

 | ϱ w = ( b m 2 + A m 4) 1 / 4. \varrho_{w}=(b_{m}^{2}+A_{m}^{4})^{1/4}. |  | (27.45) |

On a root chart b m = κ 2 ​ b b_{m}=\kappa^{2}b, A m = σ ​ κ ​ A A_{m}=\sigma\kappa A, hence

 | ϱ w = κ ​ ( b 2 + A 4) 1 / 4. \varrho_{w}=\kappa(b^{2}+A^{4})^{1/4}. |  | (27.46) |

The angular factor is bounded above and away from zero. Choose ϱ #\varrho_{\#} inside the common doubled domains. Assign 0 < t < t str 0<t<t_{\rm str}, ϱ w ≥ ϱ #\varrho_{w}\geq\varrho_{\#}, including equality, to the middle theorem, and assign 0 < t < t str 0<t<t_{\rm str}, 0 < ϱ w < ϱ #0<\varrho_{w}<\varrho_{\#} to the root theorem. Equivalently, on each member of the finite root-chart cover the root regime occupies a half-open interval 0 < κ < κ #​ ( angle) 0<\kappa<\kappa_{\#}(\text{angle}). The root theorem itself is valid through the outer value 0 < κ ≤ κ 0 0<\kappa\leq\kappa_{0}, and the fixed regime cutoff satisfies κ #​ ( angle) ≤ κ 0 \kappa_{\#}(\text{angle})\leq\kappa_{0}; its equality face is used by the earlier middle regime. Assign κ = 0 \kappa=0 to the mixed theorem and t = 0 t=0 to the source theorem. Opposite projective charts terminate, by their first physical port, in the strict, hyperbolic, one-central, passive, or exit row. On a common physical overlap the earlier regime in this order contains the boundary. Every cutoff is fixed before a theorem neighborhood is selected. Thus the partition is by finite resolved faces and first ports, not by zeros of a landing function or by the size of a subsequently chosen closure.

### 28 Completion of the analytic classification

The preceding six zero theorems and the geometric Two-Central Exhaustion Theorem complete the analytic classification used in Part I. They are applied only after the stopped atlas, first ports, and exact-once reduction have been constructed.

Theorem | Physical regime | First loss or zero face |

36 | retained analytic hyperbolic word | zero eigenvalue, multiple root, changed connector, or exit |

38 | one simple central block and hyperbolic complement | split root, second central block, mixed endpoint, or stopped nonword |

41 | retained two-central word | disjoint routing to no-pp, strict, middle, root, source, or mixed |

43 | same-attractivity two-central word without pp | complete pp, split gate, persistent endpoint, or stopped nonword |

46 | positive-margin complete physical lips configuration | source, middle/root, lost hypothesis, or changed first port |

49 | comparable source-coalescing complete-lips itinerary | outer root merger or named physical first port |

51 | retained complete-lips positive t, κ t,\kappa triple-merger itinerary with doubled five-factor first-hit buffers | t = 0 t=0 to source, κ = 0 \kappa=0 to mixed, or named physical first port |

###### Proposition 53 (Part III handoff).

For every Part I exact-once itinerary in a positive-scale regime, the regime table selects exactly one row of the preceding table. The selected theorem supplies an open theorem neighborhood in all five original parameters, includes its stated coefficient, identity, and phase-boundary specializations, and sends every remaining first loss to a strictly lower node of the finite specialization graph. The only zero-scale alternatives are the source and mixed theorems of Part II.

###### Proof.

For zero central blocks, Part I chooses the compact analytic theorem or Theorem 36. For one central block, ( 24.1) chooses Theorem 38. For two blocks, Theorem 41 first removes all geometric ambiguity and selects the no-pp, strict, middle, root, source, or mixed alternative. The strict/middle/root domains are disjoint by the fixed cutoff t = t str t=t_{\rm str}, the weighted regime partition ( 27.45)–( 27.46), and the half-open zero-scale rule ( 27.44). Each theorem statement records its coefficient and identity policy before a boundary descent is started. Every other first loss is one of the faces already numbered by Part I, so the minimal-face rank decreases. Finiteness of that rank proves termination. This argument imports the theorems only after exact-once reduction and hence does not feed back into construction of their physical words. ∎

### Appendix A Signed chart and endpoint variants

We collect here the signed compactification formulas and the auxiliary endpoint identities used in Proposition 5. The orientation is the one fixed in Section 2. Only one chart is derived in detail; the remaining signed variants follow by the displayed substitutions. The construction of physical passages and the proof that these charts exhaust the counted collar remain in Part I.

Write

 | a = μ 4 + B ​ μ 5, c = ( 1 − 2 ​ B) ​ μ 5, d = μ 3, m = μ 2, a=\mu_{4}+B\mu_{5},\qquad c=(1-2B)\mu_{5},\qquad d=\mu_{3},\qquad m=\mu_{2}, |  |

and

 | P = − y + B ​ x 2 + m ​ y 2 + a ​ x, Q = x ⁡ ( 1 + y) + d ​ y 2 + c ​ y. P=-y+Bx^{2}+my^{2}+ax,\qquad Q=x(1+y)+dy^{2}+cy. |  |

#### A.1 Representative derivation and signed formulas

In the positive horizontal chart put x = r − 1 x=r^{-1}, y = z − 1 y=z-1, and use d / d ​ τ = r ​ d / d ​ t d/d\tau=r\,d/dt. Since d ​ r / d ​ t = − r 2 ​ P dr/dt=-r^{2}P, direct substitution gives

 | d ​ r d ​ τ = − r ⁡ { B + a ​ r + r 2 ​ [1 − z + m ​ ( z − 1) 2] }, \frac{dr}{d\tau}=-r\{B+ar+r^{2}[1-z+m(z-1)^{2}]\}, |  |

whereas d ​ z / d ​ τ = r ​ Q dz/d\tau=rQ gives

 | d ​ z d ​ τ = z + r ⁡ [d ​ ( z − 1) 2 + c ⁡ ( z − 1)]. \frac{dz}{d\tau}=z+r[d(z-1)^{2}+c(z-1)]. |  |

Restricting the radial factor to the analytic transverse nullcline produces the prepared germ

 | P + ​ ( r, λ) = B + a ​ r + r 2 ​ U + ​ ( r, λ), U + ​ ( 0, 0) ≠ 0. P_{+}(r,\lambda)=B+ar+r^{2}U_{+}(r,\lambda),\qquad U_{+}(0,0)\neq 0. |  | (A.1) |

This is the representative derivation.

###### Signed chart formulas.

The reflected substitution and the upper directional substitution are recorded in the following finite list:

 | x = 1 / r, y = z − 1: r ˙ \displaystyle x=1/r,y=z-1:\qquad\dot{r} | = − r ⁡ { B + a ​ r + r 2 ​ [1 − z + m ​ ( z − 1) 2] }, \displaystyle=-r\{B+ar+r^{2}[1-z+m(z-1)^{2}]\}, |  | (A.2) |

 | z ˙ \displaystyle\dot{z} | = z + r ⁡ [d ​ ( z − 1) 2 + c ⁡ ( z − 1)]; \displaystyle=z+r[d(z-1)^{2}+c(z-1)]; |  |

 | x = − 1 / r, y = z − 1: r ˙ \displaystyle x=-1/r,y=z-1:\qquad\dot{r} | = r ⁡ { B − a ​ r + r 2 ​ [1 − z + m ​ ( z − 1) 2] }, \displaystyle=r\{B-ar+r^{2}[1-z+m(z-1)^{2}]\}, |  |

 | z ˙ \displaystyle\dot{z} | = − z + r ⁡ [d ​ ( z − 1) 2 + c ⁡ ( z − 1)]; \displaystyle=-z+r[d(z-1)^{2}+c(z-1)]; |  |

 | y = 1 / r, x = w / r: r ˙ \displaystyle y=1/r,x=w/r:\qquad\dot{r} | = − r ⁡ [w + d + r ⁡ ( w + c)], \displaystyle=-r[w+d+r(w+c)], |  |

 | w ˙ \displaystyle\dot{w} | = m − d ​ w + ( B − 1) ​ w 2 + r ⁡ [− 1 + ( a − c) ​ w − w 2]. \displaystyle=m-dw+(B-1)w^{2}+r[-1+(a-c)w-w^{2}]. |  |

The first two rows use the same physical root r = 0 r=0, with opposite transverse orientation. Their radial preparations are

 | P + ​ ( r, λ) = B + a ​ r + r 2 ​ U + ​ ( r, λ), P − ​ ( r, λ) = B − a ​ r + r 2 ​ U − ​ ( r, λ). P_{+}(r,\lambda)=B+ar+r^{2}U_{+}(r,\lambda),\qquad P_{-}(r,\lambda)=B-ar+r^{2}U_{-}(r,\lambda). |  |

Thus a simple root, a double root, and the critical B = a = 0 B=a=0 layer are kept as distinct labels. No full parameter block is replaced by an r 3 r^{3} unit. In the upper chart the equatorial gate equation is the literal quadratic

 | E ⁡ ( w, λ) = m − d ​ w + ( B − 1) ​ w 2, E(w,\lambda)=m-dw+(B-1)w^{2}, |  |

so it contributes at most two equatorial roots. Direct symbolic expansion checks the three rows of ( A.2) and the source first integral. The directional endpoint rows in the overlap cover follow by the same elementary substitutions.

At the source, H = x 2 / 2 + y − log ⁡ ( 1 + y) H=x^{2}/2+y-\log(1+y) satisfies X 0 ​ H = 0 X_{0}H=0. This identity fixes the labelled limiting ovals but is not evaluated on perturbed points with 1 + y ≤ 0 1+y\leq 0. Transversality, entry/exit orientation, and exact-once stopping are supplied by Part I, not by the cancellation X 0 ​ H = 0 X_{0}H=0.

#### A.2 Auxiliary pp and endpoint scale identities

Put u = log ⁡ ( 1 + y) u=\log(1+y), g = e u − 1 g=e^{u}-1, and

 | W ⁡ ( u) = e 2 ​ u 2 − 2 ​ e u + u + 3 2. W(u)=\frac{e^{2u}}{2}-2e^{u}+u+\frac{3}{2}. |  |

Then W ′ = g 2 W^{\prime}=g^{2}. With H u = g H_{u}=g, H x = x H_{x}=x,

 | H 1 = x ​ g + x 3 3, ω r = x ​ d ​ u + g ​ d ​ x, H_{1}=xg+\frac{x^{3}}{3},\qquad\omega_{r}=x\,du+g\,dx, |  |

one has the exact cohomological relation

 | d ​ H 1 = ω r + x ​ d ​ H. dH_{1}=\omega_{r}+x\,dH. |  |

The same direct calculation verifies the pp basis bridge and the equality of the second-order time integrands. These are algebraic identities on source ovals; they do not by themselves give a common perturbed return domain.

For the endpoint three-scale comparison let 𝒟 ​ F = q ​ F \mathcal{D}F=qF, 𝒟 ​ ρ = − ρ \mathcal{D}\rho=-\rho, and write q 1:= 𝒟 ​ q q_{1}:=\mathcal{D}q. The Wronskian of 1, F, F ​ ρ 1,F,F\rho is exactly

 | W 3 = F 2 ​ ρ ​ { q 1 + q ⁡ ( 1 − q) }. W_{3}=F^{2}\rho\{q_{1}+q(1-q)\}. |  | (A.3) |

For a D 2 D_{2} factor with q = ν + 2 ​ κ / r 2 q=\nu+2\kappa/r^{2}, the bracket in ( A.3) has leading coefficient − 4 κ 2 / r 4 -4\kappa^{2}/r^{4}. Finally, in source endpoint coordinates,

 | e − H = e z e − z e − 1 / ( 2 r 2). e^{-H}=e\,ze^{-z}e^{-1/(2r^{2})}. |  |

These identities can also be checked by direct symbolic expansion. The joint parameter/section uniformity of the true passage is proved separately in Appendix D.1.

#### A.3 A numerical consistency check

As a consistency check, we numerically integrate the exact physical source field on the section x = 0 x=0. Writing the full physical return as P ⁡ ( s, B, m, a, c, d) P(s;B,m,a,c,d), we keep B, m, a, c, d B,m,a,c,d fixed when taking finite differences in L = − log ⁡ s L=-\log s, and record

 | E 0 = P | d = c s, V = P − P | d = c d − c, W = V 1 + E 0. E_{0}=\frac{P|_{d=c}}{s},\qquad V=\frac{P-P|_{d=c}}{d-c},\qquad W=\frac{V}{1+E_{0}}. |  |

The finite sample ranges over several scaled parameter directions and values of s s. It is useful for detecting sign, scaling, and fixed-parameter implementation errors, but it is not interval arithmetic and is not used to prove exhaustiveness, uniformity, a limiting exponent, or a zero count.

#### A.4 Role of the computations

The computer algebra checks only the polynomial substitutions, source cancellations, cohomological identities, basis bridge, Wronskian, and source D 2 D_{2} boundary coordinate displayed above. It does not choose physical sections, prove coverage of the collar, establish a transverse normal, classify a first port, preserve the cut order, or show that every counted orbit enters one listed chart. Those assertions are proved in Parts I–III; the electronic supplement contains the code and complete numerical data.

### Appendix B The finite source six-jet recurrence

This appendix records the finite recurrence underlying Theorem 28. It is formulated on the common physical source domain constructed in Section 17, with its moving sections, cuts, hits, and positive gate margins C ± C_{\pm}. The recurrence controls every derivative of total order at most six. Existence of the physical source itinerary and the eventual zero count are proved in Part II, not by the combinatorial enumeration below.

#### B.1 Finite alphabet and closure operations

The seven commuting graph directions are

 | θ ∂ θ, ∂ k, ∂ e, ∂ β B, ∂ β m, ∂ β a, ∂ β c. \theta\partial_{\theta},\quad\partial_{k},\quad\partial_{e},\quad\partial_{\beta_{B}},\quad\partial_{\beta_{m}},\quad\partial_{\beta_{a}},\quad\partial_{\beta_{c}}. |  |

The primitive types are the lower fixed-initial and fixed-terminal cores ( LC, LT) (\mathrm{LC},\mathrm{LT}), fold-transverse tails FT \mathrm{FT}, outer action and inverse graphs ( AO, AI) (\mathrm{AO},\mathrm{AI}), upper layers and compact bulk ( UL, UB) (\mathrm{UL},\mathrm{UB}), moving hits and cuts ( MH, MC) (\mathrm{MH},\mathrm{MC}), and finite compositions/inverses CP \mathrm{CP}. Splitting these types by sign, forced/unforced status, graph orientation, and terminal role gives exactly 35 typed nodes. Their dependency graph has depth at most seven.

For a labelled derivative word I I, exact differentiation of a graph system Y ′ = 𝒱 ⁡ ( Y, p) Y^{\prime}=\mathcal{V}(Y,p) gives

 | ( D I Y) ′ = 𝒱 Y D I Y + 𝒱 p D I p + ∑ π ∈ Π ⁡ ( I) | π | ≥ 2 D | π | 𝒱 [Z A: A ∈ π], (D_{I}Y)^{\prime}=\mathcal{V}_{Y}D_{I}Y+\mathcal{V}_{p}D_{I}p+\sum_{\begin{subarray}{c}\pi\in\Pi(I)\\ |\pi|\geq 2\end{subarray}}D^{|\pi|}\mathcal{V}[Z_{A}:A\in\pi], |  | (B.1) |

where Π ⁡ ( I) \Pi(I) is the set of labelled set partitions and every Z A Z_{A} has strictly smaller order. The same formula applied to q ​ q − 1 = 1 qq^{-1}=1 gives the reciprocal rows. A moving hit T ⁡ ( p) T(p) defined by Ψ ⁡ ( T ⁡ ( p), p) = 0 \Psi(T(p),p)=0 satisfies

 | T I = − ℬ I Ψ T, T_{I}=-\frac{\mathcal{B}_{I}}{\Psi_{T}}, |  | (B.2) |

with ℬ I \mathcal{B}_{I} formed from lower-order hit and flow derivatives. At a moving integration cut, ordinary Leibniz differentiation adds the endpoint rows; none is discarded as “flat” before its weighted estimate is proved.

The polynomial reserve is generated by

 | p 0 = 8, p n + 1 = ( n + 2) ​ p n + 8. p_{0}=8,\qquad p_{n+1}=(n+2)p_{n}+8. |  | (B.3) |

Indeed, if an order- n n lower word costs at most r n = p n − 4 r_{n}=p_{n}-4, then a Bell term with b ≤ n + 1 b\leq n+1 blocks costs

 | b ​ r n + 8 ​ ( b + 1) ≤ ( n + 2) ​ p n + 4 = r n + 1. br_{n}+8(b+1)\leq(n+2)p_{n}+4=r_{n+1}. |  |

This is a closure estimate, not merely a count of formal words. The only nonunit denominators are fixed graph normals, Y + θ 2 Y+\theta^{2}, and the two gate factors C ± C_{\pm}. Through order six the recurrence produces at most 14 inverse gate factors. The declared reserve is the larger value q 6 = 448 q_{6}=448, and the differentiated wedge gives

 | C + − q + C − − q − e − 3 / ( 8 θ 2) ≤ C e − 17 / ( 64 θ 2), q + + q − ≤ 448. C_{+}^{-q_{+}}C_{-}^{-q_{-}}e^{-3/(8\theta^{2})}\leq Ce^{-17/(64\theta^{2})},\qquad q_{+}+q_{-}\leq 448. |  |

Thus every inverse row is paid by a displayed exponentially flat tail.

The fixed-terminal tail illustrates why moving data belong to the alphabet. With u = ( 1 − r) ​ u ε, ∗ u=(1-r)u_{\varepsilon,*} and z = e − u / θ 2 z=e^{-u/\theta^{2}}, the augmented state contains ( u, X, τ, I 0, 𝒜 T) (u,X,\tau,I_{0},\mathcal{A}_{T}) and starts at

 | ( u ε, ∗, ε, 0, 0, A ε, ∗). (u_{\varepsilon,*},\varepsilon,0,0,A_{\varepsilon,*}). |  |

Consequently a nonempty parameter word starts with

 | ( D I ​ u ε, ∗, 0, 0, 0, D I ​ A ε, ∗), (D_{I}u_{\varepsilon,*},0,0,0,D_{I}A_{\varepsilon,*}), |  |

so the moving terminal clock and entry action are not silently frozen. The weight

 | ( u, X, θ ​ τ, θ 3 ​ e 3 / ( 8 ​ θ 2) ​ I 0, 𝒜 T) (u,X,\theta\tau,\theta^{3}e^{3/(8\theta^{2})}I_{0},\mathcal{A}_{T}) |  |

reduces the tail equations to bounded L 1 L^{1} coefficient mass, exactly as in the proof of Theorem 28.

#### B.2 A representative estimate and the finite count

For example, the first nontrivial forced lower-core derivative has total order one, normalized numerator degree 11 11, fixed denominator power 4 4, bounded-atom count 11 11, and carrier

 | θ − 21 ​ ( 1 + x) 16 ​ ( z + s ​ | k |). \theta^{-21}(1+x)^{16}(z+s|k|). |  |

This representative estimate follows from the lower flow recurrence and its fixed denominator margins.

Canonicalization uses the commutativity of the seven graph generators and retains the ordered multiplicity of each canonical word. Across all nodes and orders zero through six, the result is 167115 canonical commuting words. The resulting finite family has maximum dependency depth 7 7, numerator degree 28 28, fixed denominator power 17 17, and bounded-atom count 28 28. Every primitive in an actual source word reaches a named node by one of ( B.1), ( B.2), moving-cut Leibniz, variation of constants, reciprocal differentiation, or finite composition. Thus no additional primitive is required.

#### B.3 Computer verification of the enumeration

Physical exhaustiveness follows from the common physical graph cover, the lower/fold/upper passage decomposition, fixed section normals, and the first-loss analysis proved in Part II. A finite computer check verifies the combinatorial consequences of that proof: registration of the 35 nodes, dependency acyclicity and depth, all canonical words through order six, partition and inverse bookkeeping, denominator assignment, carrier labels, and the declared worst exponents.

The computation does not prove the existence of a stopped orbit, fold transversality, the Gaussian kernel estimate, gate positivity, the exponential reserve, source localization, or the two-step Rolle argument. Those are mathematical arguments in Part II. The complete enumeration and its verification data are included in the electronic supplement rather than printed here.

### Appendix C Focal recurrence and the reduced center ideal

We give the finite rational calculation behind the center set and the reduced Bautin ideal used in Theorem 23. The calculation starts from the trace-zero normalized quadratic field, identifies the two center components, and then uses their global first integrals to justify division on the common physical return domain. The last point is essential: the local focal recurrence alone does not show that a return map is defined on a complete center annulus.

#### C.1 The degree-four and degree-six obstructions

Write the normalized field as

 | u ′ = − v + A ​ u 2 + C ​ u ​ v + D ​ v 2, v ′ = u + E ​ u ​ v + F ​ v 2. u^{\prime}=-v+Au^{2}+Cuv+Dv^{2},\qquad v^{\prime}=u+Euv+Fv^{2}. |  |

For V n = ∑ j = 0 n c n, j ​ u n − j ​ v j V_{n}=\sum_{j=0}^{n}c_{n,j}u^{n-j}v^{j} and G n = ( Q 1 ∂ u + Q 2 ∂ v) V n − 1 = ∑ j g n, j u n − j v j G_{n}=(Q_{1}\partial_{u}+Q_{2}\partial_{v})V_{n-1}=\sum_{j}g_{n,j}u^{n-j}v^{j}, direct coefficient comparison gives

 | g n, j = \displaystyle g_{n,j}={} | [A ⁡ ( n − 1 − j) + E ​ j] ​ c n − 1, j \displaystyle[A(n-1-j)+Ej]c_{n-1,j} |  | (C.1) |

 |  | + [C ⁡ ( n − j) + F ⁡ ( j − 1)] ​ c n − 1, j − 1 + D ⁡ ( n − j + 1) ​ c n − 1, j − 2. \displaystyle+[C(n-j)+F(j-1)]c_{n-1,j-1}+D(n-j+1)c_{n-1,j-2}. |  |

The homological equation is

 | 0 = \displaystyle 0={} | ( j + 1) ​ c n, j + 1 − ( n − j + 1) ​ c n, j − 1 + g n, j \displaystyle(j+1)c_{n,j+1}-(n-j+1)c_{n,j-1}+g_{n,j} |  | (C.2) |

 |  | − 𝟏 { n, j ​ even } ​ ( n / 2 j / 2) ​ L n / 2 − 1. \displaystyle-\mathbf{1}_{\{n,j\ \mathrm{even}\}}{\binom{n/2}{j/2}}L_{n/2-1}. |  |

For odd n n the system is invertible. For even n n, the gauge c n, 0 = 0 c_{n,0}=0 fixes the coefficients and leaves one radial obstruction. At degree four, one obtains the representative identity

 | 8 ​ L 1 = A ​ C + C ​ D + 2 ​ D ​ F − E ​ F. 8L_{1}=AC+CD+2DF-EF. |  | (C.3) |

At degree six, if g 6, j g_{6,j} are the coefficients from ( C.1), angular averaging gives

 | L 2 = 1 16 ​ ( 5 ​ g 6, 0 + g 6, 2 + g 6, 4 + 5 ​ g 6, 6). L_{2}=\frac{1}{16}(5g_{6,0}+g_{6,2}+g_{6,4}+5g_{6,6}). |  |

The expanded universal numerator has 30 monomials. The expansion is useful for exact symbolic regression, but the logical mechanism is the finite recurrence ( C.1)–( C.2).

Return now to the H14 parameters and put e = d + a e=d+a and t c = B + m t_{c}=B+m. After a positive unit is removed, the first obstruction is

 | e ⁡ ( 2 ​ a 2 + 2 ​ t c − 2 ​ B − 1) − 2 ​ a ​ e 2 + a ⁡ ( 2 ​ B − 1) ​ t c = 0. e(2a^{2}+2t_{c}-2B-1)-2ae^{2}+a(2B-1)t_{c}=0. |  | (C.4) |

Its derivative with respect to e e is nonzero at the source. Its analytic root e = ψ ⁡ ( a, t c, B) e=\psi(a,t_{c},B) vanishes on both a = 0 a=0 and t c = 0 t_{c}=0, hence two one-variable Hadamard integrals give ψ = a ​ t c ​ V \psi=at_{c}V. Substitution in the degree-six recurrence vanishes on the same two slices and yields

 | L 2 = a ⁡ ( B + m) ​ U ​ ( a, B, m), U ⁡ ( 0) = 1 48. L_{2}=a(B+m)U(a,B,m),\qquad U(0)=\frac{1}{48}. |  | (C.5) |

The coefficient 1 / 48 1/48 is the degree-two term after imposing the first obstruction, so U U is a unit. This slice argument is the human proof of exact divisibility; a quadratic-jet calculation alone would not suffice.

#### C.2 Center components, ideal, and complete domains

The two branches are

 | 𝒞 R = { τ = 0, a = 0, d = 0 }, 𝒞 Q = { τ = 0, t c = 0, d + a = 0 }. \mathcal{C}_{R}=\{\tau=0,a=0,d=0\},\qquad\mathcal{C}_{Q}=\{\tau=0,t_{c}=0,d+a=0\}. |  |

On 𝒞 R \mathcal{C}_{R} the field is reversible. On 𝒞 Q \mathcal{C}_{Q}, the polynomial K Q K_{Q} displayed in the proof of Theorem 23 gives the inverse integrating factor

 | 𝒱 Q = ( 1 + y) ​ K Q a 2 − 1, X ⁡ ( 𝒱 Q) = ( div ⁡ X) ​ 𝒱 Q, 𝒱 Q ​ ( 0, 0) = 1. \mathcal{V}_{Q}=\frac{(1+y)K_{Q}}{a^{2}-1},\qquad X(\mathcal{V}_{Q})=(\operatorname{div}X)\mathcal{V}_{Q},\qquad\mathcal{V}_{Q}(0,0)=1. |  |

Thus both necessary branches are centers. In coordinates ( τ, ℓ, a, t c, B) (\tau,\ell,a,t_{c},B) their union has reduced ideal ( τ, ℓ, a ​ t c) (\tau,\ell,at_{c}). Since d = ℓ + τ − a d=\ell+\tau-a,

 | a ​ t c = τ ​ t c + ℓ ​ t c − d ​ t c, at_{c}=\tau t_{c}+\ell t_{c}-dt_{c}, |  |

and therefore

 | ℐ 𝒞 = ( τ, ℓ, d ⁡ ( B + m)). \mathcal{I}_{\mathcal{C}}=(\tau,\ell,d(B+m)). |  | (C.6) |

The algebraic ideal is not yet a license to divide a return map. Part II constructs a common word domain star-shaped under the successive contractions in τ \tau, a a, and t c t_{c}. On that domain the full return is the identity on the two complete center slices, so integral Hadamard division yields the decomposition stated in Theorem 23 without continuing in ℓ \ell or dividing a finite-smooth normalizer.

Completeness of the slices is checked by explicit global objects. On 𝒞 R \mathcal{C}_{R}, the first integral is

 | H R ​ ( x, z) = 1 2 ​ z − 2 ​ B ​ x 2 + V R ​ ( z), V R ′ ​ ( z) = z − 2 ​ B − 1 ​ { ( z − 1) − m ​ ( z − 1) 2 }. H_{R}(x,z)=\frac{1}{2}z^{-2B}x^{2}+V_{R}(z),\qquad V_{R}^{\prime}(z)=z^{-2B-1}\{(z-1)-m(z-1)^{2}\}. |  |

The only additional finite critical point is S R = ( 0, 1 + 1 / m) S_{R}=(0,1+1/m). The exact barrier difference displayed after Theorem 23 controls the comparison with z = 0 z=0. On 𝒞 Q \mathcal{C}_{Q}, the component of { 𝒱 Q ≠ 0 } ∩ { y > − 1 } \{\mathcal{V}_{Q}\neq 0\}\cap\{y>-1\} containing the origin carries the analytic first integral; its only additional finite singularity is S Q = ( − a / B, − 1 / B) S_{Q}=(-a/B,-1/B) on K Q = 0 K_{Q}=0. These barriers identify the connected section interval on which each center return is the identity. They provide the common physical domain required before the division above.

#### C.3 Computer algebra checks

Computer algebra verifies the generator bridge, the Darboux cofactor identities, the degree-four and degree-six recurrences, vanishing on both parameter branches, the coefficient U ⁡ ( 0) = 1 / 48 U(0)=1/48, and the displayed first-integral, barrier, and invariant-conic identities. These finite checks do not prove that the two slices exhaust the physical center domains, that the stopped return is defined on a common star-shaped tube, or that Hadamard division is valid there. Those assertions are established by the geometric arguments in Part II and above. The code and complete outputs are included in the electronic supplement.

### Appendix D Endpoint joint uniformity and two-central incidence

We give two calculations that would otherwise interrupt the main proof: the simultaneous root and section degeneration at either semihyperbolic endpoint, and the first-port analysis for a retained two-central itinerary. Starting from the physical endpoint preparations of Part I and the complete-lips coordinates of Part III, we obtain a finite exact-clock cover and the complete physical face classification used in the Two-Central Exhaustion theorem.

#### D.1 Joint endpoint uniformity

##### D.1.1 Physical preparation and the model coefficient bridge

After the local time reversal required at one endpoint, write the physical field as

 | X λ = F ( r, z, λ) ∂ r + G ( r, z, λ) ∂ z. X_{\lambda}=F(r,z,\lambda)\partial_{r}+G(r,z,\lambda)\partial_{z}. |  |

The transverse equation has a unique analytic nullcline z = h ⁡ ( r, λ) z=h(r,\lambda), and the radial numerator on that nullcline is

 | N ± ph ​ ( r, λ) = r ⁡ { B ​ 𝒰 1 + ( a ​ 𝒰 2 + B ​ 𝒰 3) ​ r + 𝒞 ​ r 2 }, 𝒰 1 ​ ( 0) ​ 𝒰 2 ​ ( 0) ​ 𝒞 ​ ( 0) ≠ 0. N^{\rm ph}_{\pm}(r,\lambda)=r\{B\mathcal{U}_{1}+(a\mathcal{U}_{2}+B\mathcal{U}_{3})r+\mathcal{C}r^{2}\},\qquad\mathcal{U}_{1}(0)\mathcal{U}_{2}(0)\mathcal{C}(0)\neq 0. |  |

Thus ( B, a) (B,a) is locally equivalent to the first two prepared coefficients. The root-incidence cover has at most three lifts over one original parameter.

For a prescribed finite order K K, the DIR saddle-node normal form gives fibered C K C^{K} orbital coordinates

 | x ˙ = q α ​ ( x), y ˙ = − y, q α ​ ( x) = b 0 + b 1 ​ x + x 3 1 + α ​ x 2. \dot{x}=q_{\alpha}(x),\qquad\dot{y}=-y,\qquad q_{\alpha}(x)=b_{0}+b_{1}x+\frac{x^{3}}{1+\alpha x^{2}}. |  |

Let Φ λ \Phi_{\lambda} be the orbital equivalence and τ λ \tau_{\lambda} its time unit. Restricting only the first component of D Φ λ X λ = τ λ ( q α ∂ x − y ∂ y) ∘ Φ λ D\Phi_{\lambda}X_{\lambda}=\tau_{\lambda}(q_{\alpha}\partial_{x}-y\partial_{y})\circ\Phi_{\lambda} to the physical nullcline gives

 | q α ​ ( ϕ λ ​ ( r)) = v ⁡ ( r, λ) ​ N ± ph ​ ( r, λ), v ≠ 0, ϕ λ ′ ≠ 0. q_{\alpha}(\phi_{\lambda}(r))=v(r,\lambda)N^{\rm ph}_{\pm}(r,\lambda),\qquad v\neq 0,\quad\phi_{\lambda}^{\prime}\neq 0. |  |

Consequently the model and physical prepared coefficients are related by a triangular unit matrix:

 | ( A ξ B 1, ξ C ξ) mod = ( u 11 0 0 u 21 u 22 0 u 31 u 32 u 33) ​ ( a ξ b ξ c ξ) ph, u 11 ​ u 22 ​ u 33 ≠ 0. \begin{pmatrix}A_{\xi}\\ B_{1,\xi}\\ C_{\xi}\end{pmatrix}_{\rm mod}=\begin{pmatrix}u_{11}&0&0\\ u_{21}&u_{22}&0\\ u_{31}&u_{32}&u_{33}\end{pmatrix}\begin{pmatrix}a_{\xi}\\ b_{\xi}\\ c_{\xi}\end{pmatrix}_{\rm ph},\qquad u_{11}u_{22}u_{33}\neq 0. |  |

This bridge is why all root sheets and discriminants are resolved first in the analytic physical preparation, rather than in coefficients created by a finite-smooth normalizer.

For one labelled root ξ \xi, put s = x − ξ s=x-\xi. If

 | N α ​ ( x) = b 0 + b 1 ​ x + α ​ b 0 ​ x 2 + ( 1 + α ​ b 1) ​ x 3, N_{\alpha}(x)=b_{0}+b_{1}x+\alpha b_{0}x^{2}+(1+\alpha b_{1})x^{3}, |  |

Taylor’s formula is exact:

 | N α ​ ( ξ + s) = s ⁡ ( A ξ + B 1, ξ ​ s + C ξ ​ s 2), C ξ = 1 + α ​ b 1. N_{\alpha}(\xi+s)=s(A_{\xi}+B_{1,\xi}s+C_{\xi}s^{2}),\qquad C_{\xi}=1+\alpha b_{1}. |  |

Thus the same finite cover contains a simple root A ξ ≠ 0 A_{\xi}\neq 0, a D 1 D_{1} root A ξ = 0, B 1, ξ ≠ 0 A_{\xi}=0,\ B_{1,\xi}\neq 0, and a D 2 D_{2} root A ξ = B 1, ξ = 0 A_{\xi}=B_{1,\xi}=0.

##### D.1.2 Exact clock and the mixed root/section cover

On a retained one-sided component the exact model clock is

 | Θ ξ ​ ( s, α) = ∫ s ∗ s U ξ ​ ( v, α) v ⁡ ( A ξ + B 1, ξ ​ v + C ξ ​ v 2) ​ 𝑑 v, \Theta_{\xi}(s,\alpha)=\int_{s_{*}}^{s}\frac{U_{\xi}(v,\alpha)}{v(A_{\xi}+B_{1,\xi}v+C_{\xi}v^{2})}\,dv, |  | (D.1) |

and y ​ e Θ ξ ye^{\Theta_{\xi}} is a first integral of the model. The joint degeneration ( s, B 1, ξ, A ξ) → 0 (s,B_{1,\xi},A_{\xi})\to 0 is resolved with weights ( 1, 1, 2) (1,1,2). The finite signed cover consists of

 | s = ρ S, B 1, ξ = ± ρ, A ξ = ρ 2 A ¯, s = ρ S, B 1, ξ = ρ B ¯ 1, A ξ = ± ρ 2, B 1, ξ = s ​ B ¯ 1, A ξ = s 2 ​ A ¯ (phase-dominant chart). \begin{array}[]{ll}s=\rho S,\ B_{1,\xi}=\pm\rho,\ A_{\xi}=\rho^{2}\bar{A},&s=\rho S,\ B_{1,\xi}=\rho\bar{B}_{1},\ A_{\xi}=\pm\rho^{2},\\[2.84526pt] B_{1,\xi}=s\bar{B}_{1},\ A_{\xi}=s^{2}\bar{A}&\text{(phase-dominant chart).}\end{array} |  |

Here ρ \rho is constant on each original-parameter fiber. In the phase-dominant chart the fixed-fiber lift of s ∂ s s\partial_{s} is

 | ℒ = s ∂ s − B ¯ 1 ∂ B ¯ 1 − 2 A ¯ ∂ A ¯, ℒ Θ ξ = U ξ s 2 ​ ( A ¯ + B ¯ 1 + C ξ). \mathcal{L}=s\partial_{s}-\bar{B}_{1}\partial_{\bar{B}_{1}}-2\bar{A}\partial_{\bar{A}},\qquad\mathcal{L}\Theta_{\xi}=\frac{U_{\xi}}{s^{2}(\bar{A}+\bar{B}_{1}+C_{\xi})}. |  |

After the finite normalized quadratic is split into sign/root cells, the last denominator is a unit. On a phase-dominant cone,

 | | A ξ | ≤ ε ​ v 2, | B 1, ξ | ≤ ε ​ v, |A_{\xi}|\leq\varepsilon v^{2},\qquad|B_{1,\xi}|\leq\varepsilon v, |  |

and hence

 | c 1 v 3 ≤ | U ξ ​ ( v) v ⁡ ( A ξ + B 1, ξ ​ v + C ξ ​ v 2) | ≤ c 2 v 3. \frac{c_{1}}{v^{3}}\leq\left|\frac{U_{\xi}(v)}{v(A_{\xi}+B_{1,\xi}v+C_{\xi}v^{2})}\right|\leq\frac{c_{2}}{v^{3}}. |  |

Integration gives a uniform D 2 D_{2} comparison

 | − C 2 s 2 + C 3 ≤ σ χ ​ Θ ξ ​ ( s) ≤ − C 1 s 2 + C 4 -\frac{C_{2}}{s^{2}}+C_{3}\leq\sigma_{\chi}\Theta_{\xi}(s)\leq-\frac{C_{1}}{s^{2}}+C_{4} |  |

on the retained orientation. A zero of the normalized quadratic is not discarded: it is relabelled as a simple-root chart, a D 1 D_{1} chart, or a named boundary/no-passage face. This proves that the cover is joint in section and parameter variables rather than an iterated limit.

For reference, integrating ( D.1) gives the three specializations

 | A ξ ≠ 0 | s | ν ​ times a nonvanishing factor, A ξ = 0, B 1, ξ ≠ 0 | s | ν e − κ 1 / s times a nonvanishing factor, A ξ = B 1, ξ = 0 | s | ν e − κ 2 / s 2 − κ 1 / s times a nonvanishing factor. \begin{array}[]{c|c}A_{\xi}\neq 0&|s|^{\nu}\text{ times a nonvanishing factor},\\ A_{\xi}=0,\ B_{1,\xi}\neq 0&|s|^{\nu}e^{-\kappa_{1}/s}\text{ times a nonvanishing factor},\\ A_{\xi}=B_{1,\xi}=0&|s|^{\nu}e^{-\kappa_{2}/s^{2}-\kappa_{1}/s}\text{ times a nonvanishing factor}.\end{array} |  |

Indeed, for U = u 0 + u 1 ​ s + u 2 ​ s 2 U=u_{0}+u_{1}s+u_{2}s^{2}, the D 1 D_{1} partial fractions are

 | ∫ U ​ d ​ s s 2 ​ ( B 1, ξ + C ξ ​ s) = − u 0 B 1, ξ ​ s + B 1, ξ ​ u 1 − C ξ ​ u 0 B 1, ξ 2 ​ log ⁡ | s | + B 1, ξ 2 ​ u 2 − B 1, ξ ​ C ξ ​ u 1 + C ξ 2 ​ u 0 B 1, ξ 2 ​ C ξ ​ log ⁡ | B 1, ξ + C ξ ​ s |, \begin{split}\int\frac{U\,ds}{s^{2}(B_{1,\xi}+C_{\xi}s)}={}&-\frac{u_{0}}{B_{1,\xi}s}+\frac{B_{1,\xi}u_{1}-C_{\xi}u_{0}}{B_{1,\xi}^{2}}\log|s|\\ &+\frac{B_{1,\xi}^{2}u_{2}-B_{1,\xi}C_{\xi}u_{1}+C_{\xi}^{2}u_{0}}{B_{1,\xi}^{2}C_{\xi}}\log|B_{1,\xi}+C_{\xi}s|,\end{split} |  |

up to a constant. At D 2 D_{2},

 | ∫ U ​ d ​ s C ξ ​ s 3 = − u 0 2 ​ C ξ ​ s 2 − u 1 C ξ ​ s + u 2 C ξ ​ log ⁡ | s |. \int\frac{U\,ds}{C_{\xi}s^{3}}=-\frac{u_{0}}{2C_{\xi}s^{2}}-\frac{u_{1}}{C_{\xi}s}+\frac{u_{2}}{C_{\xi}}\log|s|. |  |

At the H14 source endpoint this yields e − 1 / ( 2 s 2) e^{-1/(2s^{2})}, up to the named regular coordinate factors.

The physical first hit is the composition

 | R out ∘ D ξ ∘ R in, R_{\rm out}\circ D_{\xi}\circ R_{\rm in}, |  |

not the bare exponential. The regular maps are recorded separately, and overlapping weighted charts project to the same physical first hit. Direct symbolic calculation verifies the cubic root translation, the displayed D 1 D_{1} partial fractions, the D 2 D_{2} primitive, and the source first integral. DIR applicability, the physical-to-model transfer, fixed-fiber derivative bounds, overlap compatibility, inverse-flat avoidance, and the uniform exponential comparison are proved in the text.

#### D.2 Two-central incidence and first-port rigidity

##### D.2.1 Finite algebraic family and physical boundary faces

The two possible internal central gates are the selected nonpersistent horizontal saddle-node S h S_{h} and the unique upper D D -saddle-node S v S_{v}. The persistent principal endpoint is not counted as a third central gate. For a signed parameter q ≠ 0 q\neq 0, set D = 1 + q 2 D=1+q^{2} and consider the exact transverse family

 | B = q 2 D, m = − q 2 D, d = 2 ​ q D, a = − 2 ​ q + q 2 ​ s D, c = 2 ​ q + s D. \begin{gathered}B=\frac{q^{2}}{D},\qquad m=-\frac{q^{2}}{D},\qquad d=\frac{2q}{D},\\ a=\frac{-2q+q^{2}s}{D},\qquad c=\frac{2q+s}{D}.\end{gathered} |  |

In z = 1 + y z=1+y, put

 | F = 1 − z + B ​ x 2 + m ​ ( z − 1) 2 + a ​ x, G = x ​ z + d ​ ( z − 1) 2 + c ⁡ ( z − 1), L = x + q ​ z − q − 1 + s. \begin{split}F&=1-z+Bx^{2}+m(z-1)^{2}+ax,\\ G&=xz+d(z-1)^{2}+c(z-1),\\ L&=x+qz-q^{-1}+s.\end{split} |  |

A representative exact identity is

 | F + q ​ G = q ⁡ ( q ​ x + z − 1) D ​ L. F+qG=\frac{q(qx+z-1)}{D}\,L. |  | (D.2) |

Thus L = 0 L=0 is invariant in this finite family. Its center generators are τ = s \tau=s, ℓ = − s / D \ell=-s/D, and d ⁡ ( B + m) = 0 d(B+m)=0. Direct expansion also gives the double upper factor

 | E ⁡ ( w) = − ( w + q) 2 D, E(w)=-\frac{(w+q)^{2}}{D}, |  |

the horizontal double-root branch, its weak coefficient, and the corresponding divergence residual. These identities identify algebraic candidate gates; they do not by themselves prove a complete pp strip.

Before any order argument, the retained word has the following complete physical face classification:

 | piece boundary faces possible divider endpoint η = η 0, η 1, ξ = 0, ξ h ξ = 0, ξ h regular tube θ = θ j, θ j + 1, n = n j −, n j + backward exit-corner orbit upper box I +, I −, r = r ∗, ∂ B S v stable/central equilibrium branch. \begin{array}[]{c|c|c}\text{piece}&\text{boundary faces}&\text{possible divider}\\ \hline\cr\text{endpoint}&\eta=\eta_{0},\eta_{1},\ \xi=0,\xi_{h}&\xi=0,\xi_{h}\\ \text{regular tube}&\theta=\theta_{j},\theta_{j+1},\ n=n_{j}^{-},n_{j}^{+}&\text{backward exit-corner orbit}\\ \text{upper box}&I_{+},I_{-},\ r=r_{*},\ \partial B_{S_{v}}&\text{stable/central equilibrium branch}.\end{array} |  | (D.3) |

The endpoint row follows from the exact weak equation and strong-axis orientation. The middle row is a fixed nonsingular flow box, so no unnamed gate can appear there. The upper row is closed by the gate equation and the cooperative comparison below.

##### D.2.2 Representative first-port estimate

In one regular tile,

 | d ​ n d ​ θ = f j ​ ( θ, n), X λ ​ θ ≥ 2 ​ c 0 > 0. \frac{dn}{d\theta}=f_{j}(\theta,n),\qquad X_{\lambda}\theta\geq 2c_{0}>0. |  |

Let n e, j < n h, j n_{e,j}<n_{h,j} be the equatorial and hh solution graphs and let ρ j e, ρ j h > 0 \rho_{j}^{e},\rho_{j}^{h}>0 be their minimum physical distances from both collar faces. With N = n − n e, j N=n-n_{e,j},

 | d ​ N d ​ θ = A j ​ ( θ, N) ​ N, | A j | ≤ L j. \frac{dN}{d\theta}=A_{j}(\theta,N)N,\qquad|A_{j}|\leq L_{j}. |  |

If Δ j = θ j + 1 − θ j \Delta_{j}=\theta_{j+1}-\theta_{j}, Gronwall gives the explicit entry buffers

 | m j e = ρ j e 2 ​ e − L j ​ Δ j, m j h = ρ j h 2 ​ e − L j ​ Δ j. m_{j}^{e}=\frac{\rho_{j}^{e}}{2}e^{-L_{j}\Delta_{j}},\qquad m_{j}^{h}=\frac{\rho_{j}^{h}}{2}e^{-L_{j}\Delta_{j}}. |  |

The next-cut domain is one interval. Since it contains neighborhoods of both boundary graphs, it contains the whole order band between them. This excludes both collar faces, their corners, and the previous-side port at every intermediate time, not merely at the two limiting orbits.

At upper entry put v = − w v=-w. On the two-gate sheet the exact upper equations have

 | ∂ v r ˙ = r ⁡ ( 1 + r) ≥ 0, ∂ r v ˙ = 1 + ( a − c) ​ v + v 2 ≥ 1 2. \partial_{v}\dot{r}=r(1+r)\geq 0,\qquad\partial_{r}\dot{v}=1+(a-c)v+v^{2}\geq\frac{1}{2}. |  |

The common-time comparison therefore preserves

 | r e ​ ( t) ≤ r ⁡ ( t) ≤ r h ​ ( t), v e ​ ( t) ≤ v ⁡ ( t) ≤ v h ​ ( t). r_{e}(t)\leq r(t)\leq r_{h}(t),\qquad v_{e}(t)\leq v(t)\leq v_{h}(t). |  |

The equatorial and hh boundary solutions enter the same target saddle-node block and converge to S v S_{v}; every intermediate solution does the same. Hence the entire endpoint interval is one pp component. Its non-hh boundary is the complete chain S h → p σ → S v S_{h}\to p_{\sigma}\to S_{v}, whose saddle ratio is | B / ( 1 − B) | |B/(1-B)| or its reciprocal. The purported residual class is therefore

 | 𝔄 aff = ∅. \mathfrak{A}_{\rm aff}=\varnothing. |  |

Computer algebra verifies ( D.2), the invariant family, eigenslope, weak coefficient, center-generator and divergence identities, as well as the middle/upper rescalings, overlap, gate variation, homogeneous normal variational equation, log-ratio monotonicity, and endpoint eigenslope formulas.

These finite checks do not prove an hh connection, a nonempty pp continuum, transversality of physical sections, survival of the whole order band, same-component landing, completeness of the PP/BP boundary, or exhaustion of the possible regimes. Those assertions follow from the physical face classification, scalar uniqueness, Gronwall buffers, upper comparison, and exact-once cut order in Part III. Code and complete outputs are included in the electronic supplement.

### Appendix E Algebraic checks for the mixed, middle, and root estimates

This appendix records representative finite calculations used in the mixed, middle, and root-scale zero estimates. The physical hypotheses, complete first-hit itineraries, boundary assignments, topological arguments, and Rolle counts are established in Parts I–III. The calculations below verify the algebraic identities and finite derivative recurrences invoked there.

#### E.1 Exact mixed Lienard–Dulac identities

On the exact face B = a = 0 B=a=0, write m = − p m=-p, t = 1 + y > 0 t=1+y>0, ϵ = ℓ / d \epsilon=\ell/d, and

 | G = ( 1 − p) ​ ( t − 1 − log ⁡ t) + p 2 ​ ( t − 1) 2, ϕ = ( t − 1) ​ ( ϵ t − 1), F = d ​ ϕ. G=(1-p)(t-1-\log t)+\frac{p}{2}(t-1)^{2},\qquad\phi=(t-1)\left(\frac{\epsilon}{t}-1\right),\qquad F=d\phi. |  |

For the exact Lienard system y τ = u − F ⁡ ( y) y_{\tau}=u-F(y), u τ = − g ⁡ ( y) u_{\tau}=-g(y), where g = G ′ g=G^{\prime}, put

 | 𝒱 = u 2 − 2 3 ​ u ​ F − 1 9 ​ F 2 + 2 ​ G. {\cal V}=u^{2}-\frac{2}{3}uF-\frac{1}{9}F^{2}+2G. |  |

The finite symbolic calculation expands the weighted Lie derivative to

 | ℳ = ( u − F) ​ 𝒱 y − g ​ 𝒱 u − 2 3 ​ div ⁡ ( X) ​ 𝒱 = 4 ​ d 3 𝒦, 𝒦 = G ϕ ′ − ϕ g + d 2 9 ϕ 2 ϕ ′. \begin{split}{\cal M}&=(u-F){\cal V}_{y}-g{\cal V}_{u}-\frac{2}{3}\operatorname{div}(X){\cal V}\\ &=\frac{4d}{3}{\cal K},\qquad{\cal K}=G\phi^{\prime}-\phi g+\frac{d^{2}}{9}\phi^{2}\phi^{\prime}.\end{split} |  | (E.1) |

The first summand W = G ​ ϕ ′ − ϕ ​ g W=G\phi^{\prime}-\phi g is affine separately in p p and ϵ \epsilon. Its four corner identities are

 | ϵ = 0 ϵ = 1 p = 0 log ⁡ t − 1 + t − 1 ( t − 1) ​ ( ( t + 1) ​ log ⁡ t − 2 ​ ( t − 1)) t 2 p = 1 ( t − 1) 2 / 2 ( t − 1) 4 / ( 2 ​ t 2). \begin{array}[]{c|cc}&\epsilon=0&\epsilon=1\\ \hline\cr p=0&\log t-1+t^{-1}&\frac{(t-1)((t+1)\log t-2(t-1))}{t^{2}}\\[2.84526pt] p=1&(t-1)^{2}/2&(t-1)^{4}/(2t^{2}).\end{array} |  |

The comparison used for the possibly negative last term is the exact identity

 | t 2 ​ ( t 2 − 2 ​ ϵ ​ t + ϵ) − ( t − ϵ) 2 ​ ( t 2 − ϵ) = ϵ ⁡ { ( 2 − ϵ) ​ t 2 − 2 ​ ϵ ​ t + ϵ 2 }. t^{2}(t^{2}-2\epsilon t+\epsilon)-(t-\epsilon)^{2}(t^{2}-\epsilon)=\epsilon\{(2-\epsilon)t^{2}-2\epsilon t+\epsilon^{2}\}. |  | (E.2) |

Finally, for the physical field and the positive multiplier ℬ 0 = e 2 ​ d ​ x / ( 1 + y) {\cal B}_{0}=e^{2dx}/(1+y), direct expansion gives

 | div ⁡ ( ℬ 0 ​ X) ℬ 0 = d ⁡ ( 1 − y) − ℓ 1 + y − 2 ​ d ​ p ​ y 2. \frac{\operatorname{div}({\cal B}_{0}X)}{{\cal B}_{0}}=d(1-y)-\frac{\ell}{1+y}-2dpy^{2}. |  |

These cancellations are only the finite algebraic spine of the proof. The argument proves positivity of the four corner functions, interpolates that positivity on 0 ≤ p, ϵ ≤ 1 0\leq p,\epsilon\leq 1, and combines ( E.2) with the cone p ≥ q 0 ​ d 2 p\geq q_{0}d^{2}. It then proves that the zero set of 𝒱 {\cal V} consists of the isolated origin and one proper arc, and applies Green’s theorem to | 𝒱 | − 3 / 2 X |{\cal V}|^{-3/2}X. It also proves that every counted orbit lies in the full-lap physical domain z = 1 + y > 0 z=1+y>0, treats B = 0, a ≠ 0 B=0,a\neq 0 by the incompatible endpoint orientations, and sends the split complement to its uniform sink/no-passage block. Here t = 1 + y t=1+y is the Lienard coordinate, whereas t sc t_{\rm sc} denotes the scale used in the final handoff. At t sc = 0 t_{\rm sc}=0 the source theorem is used; in the root notation the face t sc > 0, κ = 0 t_{\rm sc}>0,\ \kappa=0 is precisely the persistent mixed regime.

The computer algebra check does not prove that the physical cone is exhaustive, determine the topology of { 𝒱 = 0 } \{{\cal V}=0\}, exclude omitted roots, construct uniform first-hit domains, or establish the zero count. Code and complete outputs are included in the electronic supplement.

#### E.2 The unscaled-c middle QBF/QHH extension

The middle regime uses

 | B = t 2 ​ b, m = t 2 ​ M, a = t ​ A, d = t ​ D, c = γ, B=t^{2}b,\qquad m=t^{2}M,\qquad a=tA,\qquad d=tD,\qquad c=\gamma, |  |

with no bound on γ / t \gamma/t. In the older bounded- C C formulas this is the substitution C = γ / t C=\gamma/t. Direct expansion verifies that every apparent negative power cancels. For example the finite and upper fields become

 | ξ ′ \displaystyle\xi^{\prime} | = M ​ s 2 − s + t 2 ​ ( 1 + b ​ ξ 2 + A ​ ξ − 2 ​ M ​ s) + t 4 ​ M, \displaystyle=Ms^{2}-s+t^{2}(1+b\xi^{2}+A\xi-2Ms)+t^{4}M, |  | (E.3) |

 | s ′ \displaystyle s^{\prime} | = ξ ​ s + D ​ s 2 + ( t ​ γ − 2 ​ t 2 ​ D) ​ s + t 4 ​ D − t 3 ​ γ, \displaystyle=\xi s+Ds^{2}+(t\gamma-2t^{2}D)s+t^{4}D-t^{3}\gamma, |  |

 | R ′ \displaystyle R^{\prime} | = − R ⁡ { W + D + t 2 ​ R ​ W + t ​ γ ​ R }. \displaystyle=-R\{W+D+t^{2}RW+t\gamma R\}. |  |

On h = s − t 2 = ρ 2 h=s-t^{2}=\rho^{2}, t = ρ ​ T t=\rho T, the weighted clock denominator is

 | A w γ = ξ ⁡ ( 1 + T 2) + ρ ​ T ​ γ + ρ 2 ​ D, A_{w}^{\gamma}=\xi(1+T^{2})+\rho T\gamma+\rho^{2}D, |  |

and in v = h / t 2 v=h/t^{2} the reciprocal denominator is

 | ξ ⁡ ( 1 + v) + t ​ γ ​ v + t 2 ​ D ​ v 2. \xi(1+v)+t\gamma v+t^{2}Dv^{2}. |  |

These are polynomial in the resolved variables. The same calculation gives the exact H14 two-gate family

 | b = 1 1 + t 2, M = − 1 1 + t 2, A = − 2 + t ​ τ 1 + t 2, D = 2 1 + t 2, γ = 2 ​ t + τ 1 + t 2, b=\frac{1}{1+t^{2}},\quad M=-\frac{1}{1+t^{2}},\quad A=\frac{-2+t\tau}{1+t^{2}},\quad D=\frac{2}{1+t^{2}},\quad\gamma=\frac{2t+\tau}{1+t^{2}}, |  |

which tends to ( 1, − 1, − 2, 2, 0) (1,-1,-2,2,0) whenever t, τ → 0 t,\tau\to 0, without a restriction on τ / t \tau/t.

For the QHH connector, use the signed QL coefficient vector β = ( b, M, A ^, C ^, D ^) \beta=(b,M,\widehat{A},\widehat{C},\widehat{D}). The five commuting derivation alphabets are

 | 𝔄 0 = \displaystyle\mathfrak{A}_{0}={} | { ∂ R, ∂ z, ℰ 0, ∂ b, ∂ M, ∂ A ^, ∂ C ^, ∂ D ^ }, \displaystyle\{\partial_{R},\partial_{z},{\cal E}_{0},\partial_{b},\partial_{M},\partial_{\widehat{A}},\partial_{\widehat{C}},\partial_{\widehat{D}}\}, |  | (E.4) |

 | 𝔄 1 = \displaystyle\mathfrak{A}_{1}={} | { ∂ ξ, 𝒱 1, ℰ 1, ∂ b, ∂ M, ∂ A ^, ∂ C ^, ∂ D ^ }, \displaystyle\{\partial_{\xi},{\cal V}_{1},{\cal E}_{1},\partial_{b},\partial_{M},\partial_{\widehat{A}},\partial_{\widehat{C}},\partial_{\widehat{D}}\}, |  |

 | 𝔄 2 = \displaystyle\mathfrak{A}_{2}={} | { ∂ ξ, 𝒱 2, ℰ 2, ∂ b, ∂ M, ∂ A ^, ∂ C ^, ∂ D ^ }, \displaystyle\{\partial_{\xi},{\cal V}_{2},{\cal E}_{2},\partial_{b},\partial_{M},\partial_{\widehat{A}},\partial_{\widehat{C}},\partial_{\widehat{D}}\}, |  |

 | 𝔄 3 = \displaystyle\mathfrak{A}_{3}={} | { ∂ U, ∂ s, ℰ 3, ∂ b, ∂ M, ∂ A ^, ∂ C ^, ∂ D ^ }, \displaystyle\{\partial_{U},\partial_{s},{\cal E}_{3},\partial_{b},\partial_{M},\partial_{\widehat{A}},\partial_{\widehat{C}},\partial_{\widehat{D}}\}, |  |

 | 𝔄 4 = \displaystyle\mathfrak{A}_{4}={} | { ∂ u, ∂ ℓ, ℰ v, ∂ b, ∂ M, ∂ A ^, ∂ C ^, ∂ D ^ }. \displaystyle\{\partial_{u},\partial_{\ell},{\cal E}_{v},\partial_{b},\partial_{M},\partial_{\widehat{A}},\partial_{\widehat{C}},\partial_{\widehat{D}}\}. |  |

Every P 4 P_{4} coefficient word containing ∂ ℓ \partial_{\ell} is zero. For j = 0, …, 4 j=0,\ldots,4, all ordered words in 𝔄 j \mathfrak{A}_{j} of length at most four are included. There are 1 + 8 + 8 2 + 8 3 + 8 4 = 4681 1+8+8^{2}+8^{3}+8^{4}=4681 such ordered words, or 495 495 commuting multiindices, per expanded factor. Labeled-set Faà di Bruno, quotient, endpoint, composition, and inverse recurrences cover the resulting section-map jets. Equations ( 26.14)–( 26.30) give the physical factor order and show why these alphabets are exhaustive.

The proof does substantially more. It constructs the horizontal and vertical graph transforms in the fixed- γ \gamma resolved frame, checks the moving endpoint terms, and composes the five physical factors P 0, …, P 4 P_{0},\ldots,P_{4} on doubled first-hit buffers. It proves

 | ‖ G ‖ C res 4 + ‖ G − 1 ‖ C res 4 ≤ C G, 0 < g 0 ≤ G ′ ≤ g 1, \|G\|_{C^{4}_{\rm res}}+\|G^{-1}\|_{C^{4}_{\rm res}}\leq C_{G},\qquad 0<g_{0}\leq G^{\prime}\leq g_{1}, |  |

and, on every QHH component, obtains

 | 𝒦 ′′ = − F v ′′ ​ ( G) ​ ( G ′) 2 − F v ′ ​ ( G) ​ G ′′ + t 2 ​ ℛ K ≤ − 1 2 ​ c v ​ g 0 2 < 0. {\cal K}^{\prime\prime}=-F_{v}^{\prime\prime}(G)(G^{\prime})^{2}-F_{v}^{\prime}(G)G^{\prime\prime}+t^{2}{\cal R}_{K}\leq-\frac{1}{2}c_{v}g_{0}^{2}<0. |  |

The five commuting resolved alphabets and the labeled-set Faà di Bruno, quotient, moving-endpoint, composition, and inverse recurrences are displayed in Part III. They form a finite, formula-defined proof of the five-factor C 4 C^{4} closure. No standalone generated QHH derivative table is used as evidence for that closure.

The substitution check alone does not construct the finite QBF/QHH phase split, prove the complete through components and denominator/section-normal margins, or obtain the two-zero QBF and four-zero-per-QHH-component Rolle bounds.

The half-open QBF/QHH overlap is assigned once. Loss of a root, landing, coefficient direction, denominator, side, or first hit stops at the strict-lips, root-scale, mixed-face, passive, or exit regime specified in Part I. The face t = 0 t=0 belongs to the source theorem, while the exact persistent face t > 0, κ = 0 t>0,\kappa=0 belongs to the mixed theorem. No positive-margin theorem is continued across either face.

The finite algebraic check does not prove the graph-transform contraction, the five-factor physical order, complete through components, coefficient margins, phase connectors, or the curvature/Rolle count. Those arguments appear in Part III; code and complete outputs are included in the electronic supplement.

#### E.3 The positive root-scale derivative recurrence

In a signed root chart the physical parameters are

 | B = t 2 ​ κ 2 ​ b, m = t 2 ​ M, a = σ ​ t ​ κ ​ A, d = σ ​ t ​ D, c = σ ​ γ. B=t^{2}\kappa^{2}b,\qquad m=t^{2}M,\qquad a=\sigma t\kappa A,\qquad d=\sigma tD,\qquad c=\sigma\gamma. |  |

We first check the exact reciprocal endpoint substitution. With u = σ ​ t ​ κ ​ R ¯ u=\sigma t\kappa\bar{R}, N ¯ = R ¯ ​ z \bar{N}=\bar{R}z, and

 | H = b + A ​ R ¯ + R ¯ 2 − R ¯ ​ N ¯ + t 2 ​ M ​ ( N ¯ − R ¯) 2, H=b+A\bar{R}+\bar{R}^{2}-\bar{R}\bar{N}+t^{2}M(\bar{N}-\bar{R})^{2}, |  |

the two components are exactly

 | R ¯ ′ \displaystyle\bar{R}^{\prime} | = − σ ​ t 2 ​ κ 2 ​ R ¯ ​ H, \displaystyle=-\sigma t^{2}\kappa^{2}\bar{R}H, |  |

 | N ¯ ′ \displaystyle\bar{N}^{\prime} | = σ ⁡ { N ¯ + κ ​ t ​ γ ​ R ¯ ​ ( N ¯ − R ¯) + κ ​ t 2 ​ D ​ ( N ¯ − R ¯) 2 − t 2 ​ κ 2 ​ N ¯ ​ H }. \displaystyle=\sigma\{\bar{N}+\kappa t\gamma\bar{R}(\bar{N}-\bar{R})+\kappa t^{2}D(\bar{N}-\bar{R})^{2}-t^{2}\kappa^{2}\bar{N}H\}. |  |

It also checks the outer transfer

 | S = κ ​ s, Y = κ ⁡ ( ξ + s), X = Y − S, κ = S ​ K. S=\kappa s,\qquad Y=\kappa(\xi+s),\qquad X=Y-S,\qquad\kappa=SK. |  |

For the displayed polynomials P ~, Q ~ \widetilde{P},\widetilde{Q}, the exact desingularized field satisfies

 | Y ′ = S ​ P ~, S ′ = S ​ Q ~, K ′ = − K ​ Q ~, ( S ​ K) ′ = 0. Y^{\prime}=S\widetilde{P},\qquad S^{\prime}=S\widetilde{Q},\qquad K^{\prime}=-K\widetilde{Q},\qquad(SK)^{\prime}=0. |  |

Thus the substitution preserves the original κ \kappa -fiber; S S and K K are not independent physical parameters.

We next expand the eight numerator/denominator polynomials for the first four polynomial factors and exhaust all ordered derivative words of length at most four. Its finite summary is

 | monomials letters words/monomial pairs multipliers, orders ​ 0 ​ – ​ 4 N 0 7 9 7381 51667 1, 4, 16, 64, 256 Q 0 6 9 7381 44286 1, 2, 4, 8, 16 N 1 4 9 7381 29524 1, 4, 16, 64, 256 Q 1 4 9 7381 29524 1, 2, 4, 8, 16 N 2 4 11 16105 64420 1, 3, 9, 27, 81 Q 2 4 11 16105 64420 1, 2, 4, 8, 16 N 3 17 9 7381 125477 1, 4, 16, 64, 256 Q 3 7 9 7381 51667 1, 4, 16, 64, 256. \begin{array}[]{c|rrrr|c}&\text{monomials}&\text{letters}&\text{words/monomial}&\text{pairs}&\text{multipliers, orders }0\text{--}4\\ \hline\cr N_{0}&7&9&7381&51667&1,4,16,64,256\\ Q_{0}&6&9&7381&44286&1,2,4,8,16\\ N_{1}&4&9&7381&29524&1,4,16,64,256\\ Q_{1}&4&9&7381&29524&1,2,4,8,16\\ N_{2}&4&11&16105&64420&1,3,9,27,81\\ Q_{2}&4&11&16105&64420&1,2,4,8,16\\ N_{3}&17&9&7381&125477&1,4,16,64,256\\ Q_{3}&7&9&7381&51667&1,4,16,64,256.\end{array} |  |

The total is 460985 460985 monomial–ordered-word pairs, including zero descendants. The outer rows are first rewritten with S ​ K = ϰ SK=\varkappa and S ​ K 2 = ϰ ​ K SK^{2}=\varkappa K; hence every surviving descendant containing K K retains the essential ϰ \varkappa -factor. A representative quotient recurrence, obtained from Q ​ f = N Qf=N, is

 | c 0 = n 0 d, c k = n k + ∑ j = 1 k ( k j) ​ q j ​ c k − j d, 1 ≤ k ≤ 4, c_{0}=\frac{n_{0}}{d},\qquad c_{k}=\frac{n_{k}+\sum_{j=1}^{k}\binom{k}{j}q_{j}c_{k-j}}{d},\qquad 1\leq k\leq 4, |  |

where d > 0 d>0 is the denominator margin proved in Part III.

The proof constructs all five physical factors in their actual order, proves the fixed-product wedge, first-exit landing, denominator and section normal margins, the full vertical determinant, and the direct/inverse C res 4 C^{4}_{\rm res} bounds. The four polynomial factors covered by the 460985 460985 -pair enumeration are P 0 rt, P 1 rt, P 2 rt P_{0}^{\rm rt},P_{1}^{\rm rt},P_{2}^{\rm rt}, and P 3 out P_{3}^{\rm out}. The fifth physical factor P 4 rt P_{4}^{\rm rt} is handled by the separate formula-defined graph, normal, entry, vertical-flight, output, and inverse rows in the proof; it is not silently counted in the table. The argument then proves the at-most-six through components and the four-zero affine Rolle bound on each.

The theorem-validity handoff is half-open:

 | t = 0 ⟶ source theorem, t > 0, κ = 0 ⟶ mixed persistent- D theorem, t > 0, 0 < κ ≤ κ 0 ⟶ root theorem. \begin{array}[]{rcl}t=0&\longrightarrow&\text{source theorem},\\ t>0,\ \kappa=0&\longrightarrow&\text{mixed persistent-$D$ theorem},\\ t>0,\ 0<\kappa\leq\kappa_{0}&\longrightarrow&\text{root theorem}.\end{array} |  |

The middle/root angular equality belongs to the middle regime, and every other lost denominator, section, landing, or first hit stops at its named adjacent regime.

The finite enumeration does not prove existence of a retained complete-lips itinerary, the physical five-factor order, the fixed wedge, landing, vertical determinant, through-component topology, boundary assignment, or Rolle counting. Those are proved in Part III; code and complete outputs are included in the electronic supplement.

### Appendix F Computer-assisted calculations and data availability

Several finite algebraic calculations were checked by computer. For the source estimate, the calculation enumerates the 35 35 primitive derivative types and all 167115 167115 canonical commuting words of total order at most six. Appendix E.1 records the exact Liénard–Dulac identities used on the mixed face. For the middle QHH regime, the calculation checks the finite derivative alphabets and the polynomial substitutions recorded in Appendix E.2. For the root-scale regime, it expands the first four polynomial factors and checks the 460985 460985 monomial–derivative pairs described in Appendix E.3. Further symbolic calculations verify the compactification formulas, center ideal, endpoint identities, and mixed Liénard–Dulac cancellations in the preceding appendices.

These computations concern finite identities and enumerations. They do not construct a physical orbit, choose a transverse section, prove that the stopped atlas is exhaustive, establish the topology of a through component, or replace any compactness or Rolle argument. Each of those steps is proved in Parts I–III. Conversely, the long finite tables are not needed for reading the proof and are therefore omitted from the printed paper.

The electronic supplement contains the source code, input data, complete outputs, environment description, and checksums for the computations cited above. It also provides a single clean-room replay procedure. The manuscript and supplement are distributed together with the arXiv source package.

### References

- [1] F. Dumortier, R. Roussarie, and C. Rousseau, *Hilbert’s 16th problem for quadratic vector fields*, J. Differential Equations 110 (1994), 86–133, doi:10.1006/jdeq.1994.1061.
- [2] F. Dumortier, Y. Ilyashenko, and C. Rousseau, *Normal forms near a saddle-node and applications to finite cyclicity of graphics*, Ergodic Theory Dynam. Systems 22 (2002), 783–818, doi:10.1017/S0143385702000391.
- [3] A. Mourtada, *Action de dérivations irréductibles sur les algèbres quasi-régulières d’Hilbert*, arXiv:0912.1560.
- [4] R. Roussarie and C. Rousseau, *Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems*, Trans. Moscow Math. Soc. 76 (2015), 181–218, doi:10.1090/mosc/248; arXiv:1506.07104.
- [5] D. Marín and J. Villadelprat, *The cyclicity of hyperbolic hemicycles*, J. Differential Equations 433 (2025), article 113281, doi:10.1016/j.jde.2025.113281; arXiv:2501.16924.
- [6] S. G. Krantz and H. R. Parks, *A Primer of Real Analytic Functions*, 2nd ed., Birkhäuser, 2002, doi:10.1007/978-0-8176-8134-0.
- [7] M. Hervé, *Several Complex Variables: Local Theory*, Tata Institute of Fundamental Research Studies in Mathematics, no. 1, Oxford University Press, 1963.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
