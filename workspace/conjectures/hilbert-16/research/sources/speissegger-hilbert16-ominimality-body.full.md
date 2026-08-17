<!-- source: https://ar5iv.labs.arxiv.org/html/1804.03585 | converted from HTML -->

[1804.03585] Limit cycles of planar vector fields: Hilbert’s 16th problem and o-minimality

# Limit cycles of planar vector fields: Hilbert’s 16th problem and o-minimality Thanks: Supported by NSERC of Canada grant RGPIN 261961 and the Zukunftskolleg of Universität Konstanz. This note will appear in the Oberwolfach “Snapshots of Modern Mathematics” series. I thank Zeinab Galal and Tobias Kaiser for vetting earlier versions of this note.

Patrick Speissegger Address: Department of Mathematics and Statistics, McMaster University, 1280 Main Street West, Hamilton, Ontario L8S 4K1, Canada Email address: [speisseg@math.mcmaster.ca][1]

Date: August 8, 2026 at \currenttime

###### Abstract.

I discuss some recent work linking certain aspects of the second part of Hilbert’s 16th problem to the theory of o-minimality. These notes are adapted from a lecture I gave in the Jour fixe seminar series at the Zukunftskolleg of Universität Konstanz in June 2017.

##

A vector field is a map, denoted by F F below, that assigns to every point in the plane (or more generally in n n -space) a vector, which codes a direction and a length. Two common examples of vector fields are force fields (where the length represents acceleration) or fluid flow (where the length represents speed). Vector fields may or may not be time dependent; we assume here that F F is time independent.

The path traversed by an object following the vector field is called its trajectory. It is obtained by solving the differential equation P ′ ​ ( t) = F ⁡ ( p ⁡ ( t)) P^{\prime}(t)=F(p(t)), and it depends on the position P ⁡ ( t 0) P(t_{0}) of the object at a given initial time t 0 t_{0}, called the initial condition. The branch of mathematics tasked with studying phenomena arising from vector fields is called dynamical systems (see Perko [4] for an introduction). Here is the fundamental theorem for trajectories of vector fields:

Theorem [4, Section 2.2]. Under very mild assumptions on the vector field, each trajectory is uniquely determined by its initial condition.

Knowing the position P ⁡ ( t 0) P(t_{0}) at time t 0 t_{0} of an object following the vector field, and given a later time t 1 t_{1}, we would like to be able to predict the position P ⁡ ( t 1) P(t_{1}) of this object at time t 1 t_{1} ( quantitative phenomena) or give a general description of its long-term behaviour ( qualitative phenomena).

For instance, if the vector field is linear, that is, F ⁡ ( a) = A ​ a + b F(a)=Aa+b, where b b is a fixed point in n n -space and A A is an n × n n\times n matrix, then one can find explicit solutions in terms of the elementary functions + +, ⋅ \cdot, exp \exp, log \log, sin \sin, cos \cos and a few related functions and using complex numbers.

However, for almost all other vector fields, no such explicit solutions exist. One might say that the vocabulary of elementary mathematics is too small to describe the phenomena coded by vector fields. In this sense, the goal of the field of dynamical systems can be stated as “developing a mathematical vocabulary” to describe such phenomena.

Quantitative phenomena are usually studied using Numerical Analysis, which is concerned with computing approximations to such phenomena. This is done, for example, in models of weather or climate systems, of the burning processes in combustion engines, and many others. However, numerical methods are not able to discern different qualitative phenomena, because the longer a model is run, the larger its inherent errors become.

### Some vocabulary to describe qualitative phenomena

A singularity of F F is a point p p such that F ⁡ ( p) = 0 F(p)=0. An object located at a singularity stays there forever; so its trajectory is a point. The trajectory of an object is a cycle (or periodic trajectory), if the object revisits the same points periodically. It follows from the theorem above that the trajectory of an object either visits every point at most once, or it is a cycle. A trajectory spirals if it is not a cycle but turns infinitely often around a fixed set of points called a limit set.

A limit cycle (see Figure 1) is a cycle such that every nearby trajectory spirals around it (in effect, either towards or away from it). Thus, a limit cycle is the limit set of all trajectories near it.

[image: Refer to caption] Figure 1. A limit cycle (black) with nearby spiraling trajectories (blue). The corresponding Poincaré first return map r ⁡ ( x) r(x) is defined using a transverse segment.

Predicting the qualitative phenomena of a time-independent vector field means answering the following question: if a particle is dropped at a specific point in n n -space, then what is the nature of its trajectory? To answer this question, we need to know where the singular points and the limit sets of the vector field are and, in the latter case, what their nature is (are all limit sets limit cycles, or are there other limit sets?). A first step towards knowing the latter is to determine how many singular points and limit cycles there are.

### Counting singular points and limit cycles

We restrict our attention from now on to planar vector fields ( n = 2 n=2).

Example 1. The planar vector field F ⁡ ( x, y) = ( y, − x) F(x,y)=(y,-x) has one singularity, the origin. All other trajectories are circles centered at the origin, hence cycles. In particular, none of the trajectories are limit cycles.

The vector field in the previous example is linear, which is the simplest kind of vector field there is. It is the only kind of vector field where we know how to count limit cycles–because there aren’t any.

Linear vector fields are examples of polynomial vector fields: a polynomial of degree d d in the variables x x and y y is an expression of the form

 | a 0, 0 + a 1, 0 ​ x + a 0, 1 ​ y + a 2, 0 ​ x 2 + a 1, 1 ​ x ​ y + ⋯ + a d, 0 ​ x d + ⋯ + a 0, d ​ y d, a_{0,0}+a_{1,0}x+a_{0,1}y+a_{2,0}x^{2}+a_{1,1}xy+\cdots+a_{d,0}x^{d}+\cdots+a_{0,d}y^{d}, |  |

where the a i, j a_{i,j} are real numbers.

Note: “polynomial of degree 1” is the same as “linear”.

The vector field F F is polynomial of degree d d, if each of the two components of F F is given by a polynomial of degree d d.

Example 2. F ⁡ ( x, y) = ( x 2 + y 2, x − y 3) F(x,y)=\left(x^{2}+y^{2},x-y^{3}\right) is polynomial of degree 3.

After counting singularities and limit cycles of linear vector fields, which is easy, we could try counting singularities and limit cycles of polynomial vector fields. Since, in this case, singularities are just zeroes of polynomials, their study falls under the well-developed subject of real algebraic geometry, and I will not pursue it further here. As to counting their limit cycles, the following was suggested by David Hilbert in his famous address given at the first International Congress of Mathematics in the year 1900:

Hilbert’s 16th problem (second part). If the vector field F F on the plane is polynomial of degree d d, there exists a number H ⁡ ( d) H(d) such that F F has at most H ⁡ ( d) H(d) limit cycles.

### A very brief history of Hilbert’s 16th problem

This problem remains open to this day. The timeline below is taken from Ilyashenko’s more technical account [1] of Hilbert’s 16th problem; I refer the reader there for detailed references.

1923: Dulac proves that every polynomial vector field has only finitely many limit cycles ( Dulac’s problem). His proof does not clarify if H ⁡ ( d) H(d) exists, but his method proved to be useful for the study of dynamical systems in general.

1955–57: Petrovskii and Landis publish a solution of Hilbert’s 16th problem. It implies, in particular, that H ⁡ ( 2) = 3 H(2)=3.

1963: Ilyashenko and Novikov produce the first counterexamples to Petrovskii and Landis’s solution (so their proof was wrong).

1979–80: Chen, Wang and Shi give examples of quadratic (i.e., d = 2 d=2) vector fields with 4 limit cycles; in particular, H ⁡ ( 2) ≥ 4 H(2)\geq 4.

1981: Ilyashenko, in lectures given on Dulac’s problem, discovers a previously overlooked gap in Dulac’s proof. In Ilyashenko’s own words: “Thus, after eighty years of development, our knowledge of Hilbert’s 16th problem was almost the same as at the time when the problem was stated.”

1991–92: Ecalle and Ilyashenko independently publish papers that fill the gap in Dulac’s proof. Both of these gap-filling proofs are much longer than Dulac’s original proof, but show that Dulac’s original argument was right in principle, “just” incomplete.

### Poincaré’s idea of how to count limit cycles

The idea is to reduce the two-dimensional counting problem (counting limit cycles in the plane) to a one-dimensional counting problem (counting certain points on a line).

Example 3 [4, Section 3.4]: to count limit cycles near a cycle (drawn in black in Figure 1), draw a line segment crossing the cycle that is not tangent to any trajectory. Introduce a coordinate x x on this segment such that the intersection of the segment with the cycle is a x = 0 x=0; so the line segment corresponds to an interval ( a, b) (a,b) for some a < 0 < b a<0<b.

On this segment, define a map r: ( a, b) ⟶ ( a, b) r:(a,b)\longrightarrow(a,b) such that, for x ∈ ( a, b) x\in(a,b), the point r ⁡ ( x) r(x) is the first intersection point of the trajectory going through x x with the segment that lies no farther to 0 than x x; this map is called the Poincaré first return map, see Figure 1.

The point of this map is that counting cycles near a cycle corresponds to counting fixed points of the associated map r ⁡ ( x) r(x), i.e., points x x such that r ⁡ ( x) = x r(x)=x, near x = 0 x=0. Therefore, counting limit cycles near a cycle corresponds to counting isolated fixed points of the map r ⁡ ( x) r(x) near x = 0 x=0, i.e., fixed points x 0 x_{0} of r ⁡ ( x) r(x) for which there exists an open interval about x 0 x_{0} that contains no other fixed points of r ⁡ ( x) r(x).

The problem is that, while this reduces the dimension of the counting problem, it also takes us out of the realm of differential equations: the Poincaré map r ⁡ ( x) r(x) is not itself solution of any reasonably simple differential equation.

Poincaré overcame this problem by showing that the map r ⁡ ( x) r(x) is analytic at x = 0 x=0, that is, it has a Taylor series expansion

 | r ^ ​ ( x) = ∑ n = 0 ∞ a n ​ x n = a 0 + a 1 ​ x + a 2 ​ x 2 + ⋯ \hat{r}(x)=\sum_{n=0}^{\infty}a_{n}x^{n}=a_{0}+a_{1}x+a_{2}x^{2}+\cdots |  |

at x = 0 x=0, and this Taylor series converges. The latter implies that r ⁡ ( x) r(x) can be approximately computed, to arbitrary precision, by computing a finite sum a 0 + a 1 ​ x + ⋯ + a n ​ x n a_{0}+a_{1}x+\cdots+a_{n}x^{n} for sufficiently large n n. (For instance, all elementary functions mentioned earlier are analytic.) The key observation about functions that are analytic at 0 is that their isolated fixed points cannot accumulate at 0. Therefore:

Poincaré’s corollary. The map r ⁡ ( x) r(x) has only finitely many isolated fixed points near 0, so there are only finitely many limit cycles near a given cycle.

### Dulac’s strategy for counting limit cycles

Dulac showed that the general problem of counting limit cycles of polynomial vector fields can be reduced to a situation similar to that studied by Poincaré. Here the cycle in Poincaré’s situation is replaced by what is called a polycycle, which is a closed curve consisting of finitely many singular points connected by trajectories as in Figure 2. Using the transverse segment with coordinate x = x 1 x=x_{1} in this figure, one can again define a corresponding first return map r ⁡ ( x) r(x). (The reason for the multiple segments in the figure will be explained later.)

[image: Refer to caption] Figure 2. A polycycle with associated transition maps f i f_{i} and g i g_{i}

Thus, Dulac needed to prove that such a first return map r ⁡ ( x) r(x) of a polycycle has finitely many isolated fixed points. Similar to Poincaré’s example, this can be done by showing the following:

1. (1)

these return maps r ⁡ ( x) r(x) have asymptotic expansions r ^ ​ ( x) \hat{r}(x) at x = 0 x=0 (albeit more general than convergent Taylor series expansions);

2. (2)

each such return map r ⁡ ( x) r(x) is uniquely determined by its asymptotic expansion r ^ ​ ( x) \hat{r}(x).

While Dulac completed Point 1, Point 2 was the gap left unproved by him and proved 70 years later by Ecalle and Ilyashenko.

### What else is needed for Hilbert’s 16th problem?

For each degree d d, let 𝒮 d \mathcal{S}_{d} be the collection of all polynomial vector fields in the plane of degree d d. Each vector field in 𝒮 d \mathcal{S}_{d} is denoted by F μ F_{\mu}, where μ \mu is a tuple of real numbers representing all the coefficients of the polynomials used in the definition of F μ F_{\mu}.

To prove Hilbert’s 16th problem, it is not enough to count the number of limit cycles near a polycycle of each vector field F μ F_{\mu} separately. Instead, given a parameter μ \mu and a polycycle Γ \Gamma of F μ F_{\mu}, one needs to count all limit cycles near Γ \Gamma of all vector fields F μ ′ F_{\mu^{\prime}} for μ ′ \mu^{\prime} close to μ \mu (where “close” is to be understood in the sense of the usual topology on Euclidean spaces). Moreover, more general limit periodic sets (not defined here; it is sufficient for the purpose of this exposition to continue thinking of them as polycycles) need to be considered instead of polycycles. Indeed, Roussarie [5, Prop. 1 of Chapter 2] shows that Hilbert’s 16th problem follows if the following holds for every parameter μ \mu and every limit periodic set Γ \Gamma of F μ F_{\mu}:

Finite cyclicity conjecture (Roussarie). There exist a natural number N N and open neighborhoods U U of μ \mu and V V of Γ \,\Gamma such that for every μ ′ ∈ U \mu^{\prime}\in U, the vector field F μ ′ F_{\mu^{\prime}} has at most N N limit cycles contained in V V.

Given a parameter μ \mu and a limit periodic set Γ \Gamma of F μ F_{\mu}, what makes the finite cyclicity conjecture difficult to prove (apart from the somewhat obscure nature of limit periodic sets in general) is that the return map r μ ′ ​ ( x) r_{\mu^{\prime}}(x) of F μ ′ F_{\mu^{\prime}} around the limit periodic set Γ \Gamma is not necessarily well defined for all parameters μ ′ \mu^{\prime} close to μ \mu (because of so-called bifurcation phenomena, see [4, Chapter 4]).

Assuming Γ \Gamma is a polycycle of F μ F_{\mu}, one possible way to deal with this problem is to decompose r μ ​ ( x) r_{\mu}(x) into the transition maps y i = g μ, i ​ ( x i) y_{i}=g_{\mu,i}(x_{i}) and x i + 1 = f μ, i ​ ( y i) x_{i+1}=f_{\mu,i}(y_{i}) for i = 1, …, k i=1,\dots,k as in Figure 2, where k k is the number of singularities on the polycycle Γ \Gamma (equal to 5 in the figure) and we convene that x k + 1 = x 1 x_{k+1}=x_{1}. One recovers the first return map from the transition maps as

 | r μ ( x) = ( f μ, k ∘ g μ, k ∘ ⋯ ∘ f μ, 1 ∘ g μ, 1) ( x), r_{\mu}(x)=(f_{\mu,k}\circ g_{\mu,k}\circ\cdots\circ f_{\mu,1}\circ g_{\mu,1})(x), |  |

the successive composition of the f μ, i f_{\mu,i} and g μ, i g_{\mu,i}. By a general theorem on the dependence on initial conditions and parameters [4, Section 2.3], there are open neighbourhoods U U of μ \mu and V V of Γ \Gamma such that the transition maps f μ ′, i f_{\mu^{\prime},i} and g μ, i g_{\mu,i} are well defined for all parameters μ ′ ∈ U \mu^{\prime}\in U and segment coordinates x i, y i ∈ V x_{i},y_{i}\in V (although their composition may not be well defined if μ ′ ≠ μ \mu^{\prime}\neq\mu). These parametric transition maps can be used, in place of the return maps, to describe the limit cycles of F μ ′ F_{\mu^{\prime}} near Γ \Gamma: x ∈ V x\in V corresponds to a limit cycle of F μ ′ F_{\mu^{\prime}} near Γ \Gamma, with μ ′ ∈ U \mu^{\prime}\in U, if and only if x x belongs to the set A μ ′ A_{\mu^{\prime}} of all isolated points of the set

 | { x 1 ∈ V: ∃ x 2, …, x k, y 1, …, y k such that y i = g μ ′, i ( x i) and x i + 1 = f μ ′, i ( y i) for each i }. \big\{x_{1}\in V:\ \exists x_{2},\dots,x_{k},y_{1},\dots,y_{k}\text{ such that }\\ y_{i}=g_{\mu^{\prime},i}(x_{i})\text{ and }x_{i+1}=f_{\mu^{\prime},i}(y_{i})\text{ for each }i\big\}. |  |

By the previous paragraph, the sets A μ ′ A_{\mu^{\prime}} are well defined for μ ′ ∈ U \mu^{\prime}\in U, even if the composition of the transition maps is not well defined. Similar parametric transition maps and corresponding sets A μ ′ A_{\mu^{\prime}} can be defined near every limit periodic set (not just polycycles).

In Kaiser et al. [2], this observation is used to formulate a criterion for these parametric transition maps that implies the corresponding finite cyclicity conjecture. The new ingredient in this formulation comes from model theory, a branch of mathematical logic.

### From Dulac’s proof to Hilbert’s 16th problem with … logic?

In the 1930s, Gödel established some surprising implications of logic for the general study of mathematics, known as Gödel’s completeness and incompleteness theorems. Out of these theorems, a new branch of mathematics called model theory arose, started by Robinson in the 1950s. It studies the implications of Gödel’s theorems for particular situations in mathematics; see Marker [3] for an introduction to model theory.

A crucial concept from model theory is that of definability: given a set ℒ \mathcal{L} of relations and functions on Euclidean space of various arities (the language), we call ℒ \mathcal{L} -formula any expression formed from symbols in ℒ \mathcal{L}, variables, the logical connectives ∧ \wedge (“and”), ∨ \vee (“or”), → \to (“implies”) and ¬ \neg (“not”), as well as the logical quantifiers ∃ \exists (“there exists”) and ∀ \forall (“for all”), following the syntactic rules of first-order predicate logic [3, Section 1.1]. Of particular importance are the free variables of an ℒ \mathcal{L} -formula ϕ \phi, that is, those variables in ϕ \phi that are not bound by any quantifier in ϕ \phi. A set S ⊆ ℝ n S\subseteq\mathbb{R}^{n} is definable from ℒ \mathcal{L} if there exists an ℒ \mathcal{L} -formula ϕ ⁡ ( x 1, …, x n) \phi(x_{1},\dots,x_{n}) with free variables among x 1, …, x n x_{1},\dots,x_{n} such that

 | S = { ( a 1, …, a n) ∈ ℝ n: ϕ ⁡ ( a 1, …, a n) ​ holds }. S=\left\{(a_{1},\dots,a_{n})\in\mathbb{R}^{n}:\ \phi(a_{1},\dots,a_{n})\text{ holds}\right\}. |  |

The collection of all sets definable from ℒ \mathcal{L} is referred to as an ℒ \mathcal{L} -structure (on the real numbers). For instance, zerosets of polynomials are definable from the language ℒ or:= { +, −, ⋅, 0, 1, =, < } \mathcal{L}_{\text{or}}:=\{+,-,\cdot,0,1,=,<\} of ordered rings. Of interest to this paper is the following:

Example 4. If ℒ \mathcal{L} is a language that contains ℒ or \mathcal{L}_{\text{or}} as well as the transition maps f i ​ ( μ ′, x i):= f μ ′, i ​ ( x i) f_{i}(\mu^{\prime},x_{i}):=f_{\mu^{\prime},i}(x_{i}) and g i ​ ( μ ′, y i):= g μ ′, i ​ ( y i) g_{i}(\mu^{\prime},y_{i}):=g_{\mu^{\prime},i}(y_{i}) defined on the set U × V U\times V for the polycycle Γ \Gamma above, then the set

 | A:= { ( μ ′, x) ∈ U × V: x ∈ A μ ′ } A:=\left\{(\mu^{\prime},x)\in U\times V:\ x\in A_{\mu^{\prime}}\right\} |  |

is definable from ℒ \mathcal{L}. This follows easily from the definition of A A above and the observation that x x is an isolated point of a set S ⊆ ℝ S\subseteq\mathbb{R} if and only if there exists an ϵ > 0 \epsilon>0 such that S ∩ ( x − ϵ, x + ϵ) = { x } S\cap(x-\epsilon,x+\epsilon)=\{x\}.

What makes this last example interesting in connection with Roussarie’s conjecture is a tameness condition for ℒ \mathcal{L} -structures, now called o-minimality, discovered by van den Dries and developed by Pillay and Steinhorn in the early 1980s; see van den Dries [6] for an introduction to o-minimality.

By definition, an ℒ \mathcal{L} -structure is o-minimal if every subset of ℝ \mathbb{R} definable from ℒ \mathcal{L} is a finite union of intervals. Since adding an existential quantifier to an ℒ \mathcal{L} -formula ϕ \phi corresponds to taking a coordinate projection of the set defined by ϕ \phi, the collection of all sets definable from ℒ \mathcal{L} is closed under taking coordinate projections. Therefore, the o-minimality condition has implications for all sets definable from ℒ \mathcal{L} (not just the subsets of ℝ \mathbb{R}). In dimension greater than 1, the role of intervals is played by cells in ℝ n \mathbb{R}^{n}, which are defined by induction on n n: the cells in ℝ \mathbb{R} are the intervals and, if n > 1 n>1, a cell in ℝ n \mathbb{R}^{n} definable from ℒ \mathcal{L} is any of the sets

 | Γ ( f) C:= { ( x, f ( x): x ∈ C }, \Gamma(f)_{C}:=\{(x,f(x):\ x\in C\}, |  |

 | ( f, g) C:= { ( x, y): f ⁡ ( x) < y < g ⁡ ( x) }, (f,g)_{C}:=\{(x,y):\ f(x)<y<g(x)\}, |  |

 | ( − ∞, f) C:= { ( x, y): y < f ⁡ ( x) } (-\infty,f)_{C}:=\{(x,y):\ y<f(x)\} |  |

and

 | ( f, + ∞) C:= { ( x, y): y > f ⁡ ( x) }, (f,+\infty)_{C}:=\{(x,y):\ y>f(x)\}, |  |

where C ⊆ ℝ n − 1 C\subseteq\mathbb{R}^{n-1} is a cell definable from ℒ \mathcal{L} and f, g: C ⟶ ℝ f,g:C\longrightarrow\mathbb{R} are continuous functions such that f ⁡ ( x) < g ⁡ ( x) f(x)<g(x) for x ∈ C x\in C and the graphs of f f and g g are definable from ℒ \mathcal{L}.

Theorem (Pillay and Steinhorn, see [6, Chapter 3]). If an ℒ \mathcal{L} -structure is o-minimal, then every set definable from ℒ \mathcal{L} is a finite union of cells definable from ℒ \mathcal{L}.

The inductive definition of “cell” implies that if C ⊆ ℝ m + n C\subseteq\mathbb{R}^{m+n} is a cell definable from ℒ \mathcal{L} and μ ∈ ℝ m \mu\in\mathbb{R}^{m}, then the fiber C μ:= { x ∈ ℝ n: ( μ, x) ∈ C } C_{\mu}:=\{x\in\mathbb{R}^{n}:\ (\mu,x)\in C\} of C C over μ \mu is also a cell definable from ℒ \mathcal{L}. Thus, if A ⊆ ℝ m + n A\subseteq\mathbb{R}^{m+n} is a union of N N cells, where N ∈ ℕ N\in\mathbb{N}, then for every μ ∈ ℝ m \mu\in\mathbb{R}^{m}, the fiber A μ A_{\mu} is a union of at most N N cells. Since the only finite cells are points, it follows that:

Corollary (uniform finiteness principle). If an ℒ \mathcal{L} -structure is o-minimal, A ⊆ ℝ m + n A\subseteq\mathbb{R}^{m+n} is definable from ℒ \mathcal{L} and the fiber A μ A_{\mu} is finite for every μ ∈ ℝ m \mu\in\mathbb{R}^{m}, then there exists an N ∈ ℕ N\in\mathbb{N} such that each A μ A_{\mu} has at most N N elements.

### Back to Roussarie’s conjecture

One might apply the uniform finiteness principle to the set A A of Example 4 as follows: let ℒ trans \mathcal{L}_{\text{trans}} be the language containing ℒ or \mathcal{L}_{\text{or}} as well as the parametric transition maps associated to every limit periodic set of every F μ F_{\mu} in 𝒮 d \mathcal{S}_{d} as above. Let μ \mu be a parameter and Γ \Gamma a limit periodic set of F μ F_{\mu}; by Example 4, the corresponding set A A is definable from ℒ trans \mathcal{L}_{\text{trans}}, and by Dulac’s problem, each fiber A μ A_{\mu} is finite. Therefore, the corresponding finite cyclicity conjecture conjecture follows from the uniform finiteness principle and the following:

Conjecture (o-minimality). The ℒ trans \mathcal{L}_{\text{trans}} -structure on the real numbers is o-minimal.

This conjecture is open, and proving o-minimality of ℒ \mathcal{L} -structures is a long process. However, a few general methods for doing so are now established and have been successfully used to obtain the following special case of the o-minimality conjecture: let 𝒩 ​ ℛ ​ ℋ d \mathcal{NRH}_{d} be the subset of all vector fields in 𝒮 d \mathcal{S}_{d} that have only non-resonant hyperbolic singularities, as defined in the introduction of Kaiser et al. [2]. Let ℒ nrhyp \mathcal{L}_{\text{nrhyp}} be the sublanguage of ℒ trans \mathcal{L}_{\text{trans}} consisting of all parametric transition maps associated to the vector fields in 𝒩 ​ ℛ ​ ℋ d \mathcal{NRH}_{d}. Then:

Theorem [2]. The ℒ nrhyp \mathcal{L}_{\text{nrhyp}} -structure on the real numbers is o-minimal; in particular, Roussarie’s conjecture holds for 𝒩 ​ ℛ ​ ℋ d \mathcal{NRH}_{d}.

The set 𝒩 ​ ℛ ​ ℋ d \mathcal{NRH}_{d} is arguably a very “small” subset of 𝒮 d \mathcal{S}_{d}; for instance, it is not generic, which means that even if F μ ∈ 𝒩 ​ ℛ ​ ℋ d F_{\mu}\in\mathcal{NRH}_{d} for some μ \mu, there are arbitrarily close μ ′ \mu^{\prime} such that F μ ′ F_{\mu^{\prime}} belongs to 𝒮 d \mathcal{S}_{d}, but not to 𝒩 ​ ℛ ​ ℋ d \mathcal{NRH}_{d}. However, the larger set ℋ d \mathcal{H}_{d} of all vector fields in 𝒮 d \mathcal{S}_{d} that have only hyperbolic singularities (including resonant ones) is a generic subset of 𝒮 d \mathcal{S}_{d}. One simplification for the subfamily ℋ d \mathcal{H}_{d} over the general case is that every limit periodic set is indeed a polycycle in this situation (this follows from [5, Theorem 5 of Chapter 2], because hyperbolic singularities are always isolated). In collaboration with my former student Zeinab Galal and my colleagues Tobias Kaiser, Jean-Philippe Rolin and Tamara Servi, I am currently working on the o-minimality conjecture for the corresponding sublanguage of ℒ trans \mathcal{L}_{\text{trans}}.

## References

- [1] Yulij Ilyashenko, Centennial history of Hilbert’s 16th problem, Bull. Amer. Math. Soc. (N.S.), 39 (2002), 301–354.
- [2] Tobias Kaiser, Jean-Philippe Rolin, and Patrick Speissegger, Transition maps at non-resonant hyperbolic singularities are o-minimal, J. Reine Angew. Math., 636 (2009), 1–45.
- [3] David Marker, Model theory, vol. 217 of Graduate Texts in Mathematics, Springer-Verlag, New York, 2002. An introduction.
- [4] Lawrence Perko, Differential equations and dynamical systems, vol. 7 of Texts in Applied Mathematics, Springer-Verlag, New York, third ed., 2001.
- [5] Robert Roussarie, Bifurcations of planar vector fields and Hilbert’s sixteenth problem, Modern Birkhäuser Classics, Birkhäuser/Springer, Basel, 1998. [2013] reprint of the 1998 edition [MR1628014].
- [6] Lou van den Dries, Tame topology and o-minimal structures, vol. 248 of London Mathematical Society Lecture Note Series, Cambridge University Press, Cambridge, 1998.

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto:speisseg@math.mcmaster.ca
[2]: /html/1804.03584
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/1804.03585
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1804.03585
[8]: https://arxiv.org/pdf/1804.03585
[9]: /html/1804.03586
