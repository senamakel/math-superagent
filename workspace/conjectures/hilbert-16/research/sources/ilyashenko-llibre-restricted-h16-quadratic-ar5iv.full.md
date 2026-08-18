<!-- source: https://ar5iv.labs.arxiv.org/html/0910.3443 | converted from HTML -->

[0910.3443] A restricted version of the Hilbert’s 16th problem for quadratic vector fields

# A restricted version of the Hilbert’s 16th problem for quadratic vector fields Thanks: The first author was supported by part by the grants NSF 0700973, RFBR-CNRS 050102801, RFBR 07-01-00017-à. The second author is partially supported by a MCYT/FEDER grant number MTM2008–03437 and by a CIRIT grant number 2005SGR 00550.

Yu Ilyashenko 1 and Jaume Llibre 2 Address: 1 Cornell University, US; Moscow State and Independent Universities, Steklov Math. Institute, Moscow. Email address: [yulij@math.cornell.edu][1] Address: 2 Departament de Matemàtiques, Universitat Autònoma de Barcelona, 08193 Bellaterra, Barcelona, Catalonia, Spain. Email address: [jllibre@mat.uab.cat][2]

###### Abstract.

The restricted version of the Hilbert 16th problem for quadratic vector fields requires an upper estimate of the number of limit cycles through a vector parameter that characterizes the vector fields considered and the limit cycles to be counted. In this paper we give an upper estimate of the number of limit cycles of quadratic vector fields `​ `​ σ ``\sigma –distant from centers and κ \kappa -distant from singular quadratic vector fields” provided that the limit cycles are `​ `​ δ ``\delta –distant from singular points and infinity”.

###### Key words and phrases:

limit cycles, quadratic systems

###### 1991 Mathematics Subject Classification

Primary 34C40, 51F14; Secondary: 14D05, 14D25.

## 1. Introduction and statement of the main result

Hilbert 16th problem asks (see [6]): what may be said about the number and location of limit cycles of a polynomial vector field of degree n n in the real plane? The main contributions in this direction were the works of Écalle [5] and Ilyashenko [7] who proved that any polynomial vector field has finitely many limit cycles, and also the work of Llibre and Rodríguez [13] who showed that any finite location of limit cycles is realized by a polynomial vector field of a convenient degree. But the complete answer to Hilbert 16th problem is unknown even for n = 2. n=2. Even the existence of an uniform upper bound of the number of limit cycles for quadratic vector fields (polynomial vector fields of degree 2 2) is not yet proved. Limit cycles of a quadratic vector field may surround only one singular point, and it is of type focus (for more details see [14]). Moreover, quadratic vector fields have at most two foci (see again [14]). Limit cycles surrounding the same singular point form a nest. Recently Zhang Pingguang [15, 16, 17] proved that only one nest of quadratic vector field may have more than one limit cycle.

The restricted version of the Hilbert 16th problem for quadratic vector fields allows us to introduce a vector parameter that characterizes the vector field and the limit cycles to be counted. The upper bound for the number of limit cycles is expressed through this parameter.

In this paper we give an upper estimate of the number of limit cycles of quadratic vector fields “ σ \sigma –distant from centers and κ \kappa –distant from singular quadratic vector fields” provided that the cycles are `​ `​ δ ``\delta –distant from singular points and infinity”. The precise sense of assumptions in quotation marks is explained below. The upper estimate mentioned above depends on σ, κ \sigma,\kappa and δ. \delta.

### 1.1. Normalized quadratic vector fields

We consider quadratic vector fields with a focus point 0 0 and estimate the number of limit cycles that surround this point. The system has the form

(1) |  | z ˙ = μ ​ z + A ​ z 2 + B ​ z ​ z ¯ + C ​ z ¯ 2, \dot{z}=\mu z+Az^{2}+Bz\bar{z}+C\bar{z}^{2}, |  |

where μ, A, B, C \mu,A,B,C are complex coefficients. Rescaling: z ↦ c ​ z z\mapsto cz and t ↦ c ′ ​ t t\mapsto c^{\prime}t, c ∈ ℂ c\in\mathbb{C}, c ′ ∈ ℝ c^{\prime}\in\mathbb{R} brings it to

 | z ˙ = c ′ ​ ( μ ​ z + A ​ c ​ z 2 + B ​ c ¯ ​ z ​ z ¯ + C ​ c ¯ 2 c ​ z ¯ 2). \dot{z}=c^{\prime}(\mu z+Acz^{2}+B\bar{c}z\bar{z}+C\frac{{\bar{c}}^{2}}{c}{\bar{z}}^{2}). |  |

Hence, after an appropriate normalization, we can take in ( 1): μ = λ 1 + i, max ⁡ ( | A |, | C |) ≤ 1, | B | ≤ 2 \mu=\lambda_{1}+i,\ \max(|A|,|C|)\leq 1,|B|\leq 2. Moreover, the normalized tuple ( A, B, C) (A,B,C) has the form: either A = 1 A=1 and | B | ≤ 2, | C | ≤ 1 |B|\leq 2,\ |C|\leq 1, or B = 2 B=2 and | A | ≤ 1, | C | ≤ 1 |A|\leq 1,|C|\leq 1, or C = 1 C=1 and | A | ≤ 1, | B | ≤ 2 |A|\leq 1,|B|\leq 2. The reason for distinguishing B B will be seen later.

To summarize, the normalized quadratic vector field has the form:

(2) |  | z ˙ = μ ​ z + z 2 + B ​ z ​ z ¯ + C ​ z ¯ 2, | B | ≤ 2, | C | ≤ 1, \dot{z}=\mu z+z^{2}+Bz\bar{z}+C{\bar{z}}^{2},\ |B|\leq 2,|C|\leq 1, |  |

or

(3) |  | z ˙ = μ ​ z + A ​ z 2 + 2 ​ z ​ z ¯ + C ​ z ¯ 2, | A | ≤ 1, | C | ≤ 1, \dot{z}=\mu z+Az^{2}+2z\bar{z}+C{\bar{z}}^{2},\ |A|\leq 1,|C|\leq 1, |  |

or

(4) |  | z ˙ = μ ​ z + A ​ z 2 + B ​ z ​ z ¯ + z ¯ 2, | A | ≤ 1, | B | ≤ 2, \dot{z}=\mu z+Az^{2}+Bz\bar{z}+{\bar{z}}^{2},\ |A|\leq 1,|B|\leq 2, |  |

with μ = λ 1 + i \mu=\lambda_{1}+i.

Moreover, we consider that λ 1 ≥ 0 \lambda_{1}\geq 0. If not, we reverse the time and make a symmetry z ↦ z ¯. z\mapsto\bar{z}.

The tuple of parameters ( λ 1, A, B, C) (\lambda_{1},A,B,C) with ( A, B, C) (A,B,C) normalized as above is denoted by λ \lambda and the corresponding vector field (and equation) is denoted by v λ v_{\lambda}. The space of all these λ \lambda ’s is denoted by Λ \Lambda. It is homeomorphic to the glued union of three copies of ℝ + × 𝔻 2 × 𝔻 2 \mathbb{R}^{+}\times\mathbb{D}^{2}\times\mathbb{D}^{2}, where ℝ + = [0, ∞) \mathbb{R}^{+}=[0,\infty) and 𝔻 2 = { z ∈ ℂ: | z | ≤ 1 } \mathbb{D}^{2}=\{z\in\mathbb{C}:|z|\leq 1\}; the gluing maps identify the boundaries of the cells ℝ + × 𝔻 2 × 𝔻 2 \mathbb{R}^{+}\times\mathbb{D}^{2}\times\mathbb{D}^{2}; we will not need these maps below.

### 1.2. Center conditions

Center conditions for quadratic vector fields are well known; see the works of Dulac [4], Kapteyn [11, 12], Bautin [1]. In the complex form they were found by Zoladek [18], see the next theorem. We will use the latter form of the center conditions.

###### Theorem 1.

A quadratic vector field ( 1) has a center at zero if and only if the following holds:

(5) |  | g 1:= λ 1 = 0, g 2:= Im ⁡ ( A ​ B) = 0, g 3:= Im ⁡ [( 2 ​ A + B ¯) ​ ( A − 2 ​ B ¯) ​ B ¯ ​ C] = 0, g 4:= Im ⁡ [( 2 ​ A + B ¯) ​ ( | B | 2 − | C | 2) ​ B ¯ 2 ​ C] = 0. \begin{array}[]{l}g_{1}:=\lambda_{1}=0,\\ g_{2}:={\rm Im}(AB)=0,\\ g_{3}:={\rm Im}[(2A+\bar{B})(A-2\bar{B})\bar{B}C]=0,\\ g_{4}:={\rm Im}[(2A+\bar{B})(|B|^{2}-|C|^{2}){\bar{B}}^{2}C]=0.\end{array} |  |

###### Definition 2.

A normalized quadratic vector field is called σ \sigma –distant from centers provided that

(6) |  | ∑ j = 1 4 | g j ​ ( λ) | ≥ σ. \sum_{j=1}^{4}|g_{j}(\lambda)|\geq\sigma. |  |

The set of all λ ∈ Λ \lambda\in\Lambda for which v λ v_{\lambda} is σ \sigma –distant from centers is denoted by Λ ⁡ ( σ). \Lambda(\sigma).

### 1.3. δ \delta –tame limit cycles

Now for any δ > 0 \delta>0 we define δ \delta –tame limit cycles of a normalized quadratic vector field. Note that the normalization of a quadratic vector field provides a scale on the phase plane. Thus the following definition makes sense. For any δ ∈ ( 0, 1) \delta\in(0,1) and any λ ∈ Λ \lambda\in\Lambda denote by B ⁡ ( λ, δ) B(\lambda,\delta) the disc | z | ≤ δ − 1 |z|\leq{\delta}^{-1} in ℂ \mathbb{C} minus all the open δ \delta -neighborhoods of the singular points of v λ v_{\lambda}, both real and complex, except for the point 0 0.

###### Definition 3.

A limit cycle of a normalized vector field is called *δ \delta –tame*provided that it belongs to B ⁡ ( λ, δ) B(\lambda,\delta).

### 1.4. Singular quadratic vector fields

A quadratic vector field with a focus at the zero and a line of singular points not passing through zero is called singular. Such a quadratic vector field can be written as

 | z ˙ = μ ​ z ​ l ​ ( z), \dot{z}=\mu zl(z), |  |

where l ⁡ ( z) l(z) is a real polynomial of degree 1 1 of the form l ⁡ ( z) = a ​ z + a ¯ ​ z ¯ + 1 l(z)=az+\bar{a}\bar{z}+1. After normalization, this equation has the form

(7) |  | z ˙ = μ ​ z + z 2 + μ μ ¯ ​ z ​ z ¯:= v s ​ ( z), \dot{z}=\mu z+z^{2}+\frac{\mu}{\bar{\mu}}z\bar{z}:=v_{s}(z), |  |

where μ = λ 1 + i \mu=\lambda_{1}+i. The s s of v s v_{s} is for a singular quadratic vector field. Any normalized quadratic vector field close to a singular one has the form

(8) |  | v = v s + u, u = b ​ z ​ z ¯ + c ​ z ¯ 2; v=v_{s}+u,\qquad u=bz\bar{z}+c{\bar{z}}^{2}; |  |

here v s v_{s} is singular, b b and c c are small. In this expression for v v, its coefficient B B may be greater in modulus than 1 1 but smaller than 2 2 because b b is small. Still the normal form of v v is ( 2). That is why B B is distinguished in the definition of the normal form. To find decomposition ( 8) for a vector field v v in the form ( 2), take v s v_{s} as in ( 7) and u u as in ( 8) with coefficients:

 | b = B − μ μ ¯, c = C. b=B-\frac{\mu}{\bar{\mu}},\ c=C. |  |

Let ∥ ⋅ ∥ 2 \|\cdot\|_{2} denote the L 2 L_{2} norm on a circle. Then

 | ‖ r − 2 ​ u ‖ 2 2 = | b | 2 + | c | 2. ||r^{-2}u||_{2}^{2}={|b|}^{2}+{|c|}^{2}. |  |

###### Definition 4.

A quadratic vector field is *κ \kappa –distant*from the set of singular quadratic vector fields if ‖ r − 2 ​ u ‖ 2 > κ ||r^{-2}u||_{2}>\kappa in ( 8).

### 1.5. Main result

###### Theorem 5 (Main Theorem).

For any { δ, σ, κ } ⊂ ( 0, 0.1) \{\delta,\sigma,\kappa\}\subset(0,0.1), the number of δ \delta –tame limit cycles of a normalized quadratic vector field which is σ \sigma –distant from centers and κ \kappa –distant from singular quadratic vector fields is no greater than

 | H ⁡ ( 2, δ, σ, κ) = | log ⁡ σ | ​ exp ⁡ ( exp ⁡ ( 10 25 ​ δ − 31 ​ κ − 2)). H(2,\delta,\sigma,\kappa)=|\log\sigma|\exp(\exp({10}^{25}\delta^{-31}\kappa^{-2})). |  |

This estimate is irrealistic but this is the only known estimate of this kind.

This paper is the first in a series of papers aimed to estimate the number of δ \delta –tame limit cycles of quadratic vector fields. In a subsequent paper we prove that for κ \kappa sufficiently small: κ ≤ κ 0 ​ ( δ, σ) \kappa\leq\kappa_{0}(\delta,\sigma), the vector field ( 8) has only one δ \delta –tame limit cycle. A similar result, without a quantitative estimate on the value of κ 0 ​ ( δ, σ) \kappa_{0}(\delta,\sigma), is obtained in the preprint [3].

### 1.6. Growth–and–Zeros Theorem

Limit cycles correspond to the fixed points of the Poincaré map . For normalized quadratic vector field v λ v_{\lambda} consider the Poincaré map P λ P_{\lambda} of a segment of a positive semiaxes ℝ + \mathbb{R}^{+} with the left endpoint 0 0 into ℝ + \mathbb{R}^{+}; the right endpoint will be specified later.

The number of the fixed points of this map will be estimated with the use of the theorem named in the title of the subsection; for its proof see [7], [10].

###### Theorem 6.

Let U ⊂ ℂ U\subset\mathbb{C} be a connected and simply connected domain and K ⊂ U K\subset U be a path connected compact set. Let D D be the internal diameter of K K, and

 | gap ​ ( K, U):= ρ ⁡ ( K, ∂ U) ≥ ε, \text{gap }(K,U):=\rho(K,\partial U)\geq{\varepsilon}, |  |

where ρ ⁡ ( K, ∂ U) = min a ∈ K, b ∈ ∂ U ⁡ | a − b |. \rho(K,\partial U)=\displaystyle\min_{a\in K,b\in\partial U}|a-b|. Let f: U ¯ → ℂ f:{\overline{U}}\to\mathbb{C} be a holomorphic function. Then

(9) |  | #⁡ { z ∈ K ∣ f ⁡ ( z) = 0 } ≤ B K, U ​ ( f) ​ exp ⁡ ( 2 ​ D ε), \#\{z\in K\mid f(z)=0\}\leq B_{K,U}(f)\exp\left(\frac{2D}{{\varepsilon}}\right), |  |

where

(10) |  | B K, U ​ ( f) = log ⁡ max U ¯ ⁡ | f | max K ⁡ | f |. B_{K,U}(f)=\log\frac{\max_{\overline{U}}|f|}{\max_{K}|f|}. |  |

As usual U ¯ \overline{U} denotes the closure of U U. The expression B K, U ​ ( f) B_{K,U}(f) is called the Bernstein index of f f for K, U K,U. The exponential in ( 9) is called *the geometric factor.*We will often write:

 | M = max U ¯ ⁡ | f |, m = max K ⁡ | f |. M=\max_{\bar{U}}|f|,\qquad m=\max_{K}|f|. |  |

This theorem will be applied to bound the number of zeros of the displacement function

 | f λ = P λ − i ​ d f_{\lambda}=P_{\lambda}-id |  |

of the Poincaré map P λ P_{\lambda} of v λ v_{\lambda}; these zeros correspond to limit cycles of v λ. v_{\lambda}.

There are the following steps in the application of this theorem:

- choice of K K and finding the lower estimate for m = max K ⁡ | f λ | m=\displaystyle\max_{K}|f_{\lambda}|;

- choice of U U and finding the upper estimate for M = max U ¯ ⁡ | f λ | M=\displaystyle\max_{\bar{U}}|f_{\lambda}|.

## 2. The lower estimate of the maximum of the displacement

### 2.1. Normalized quadratic vector fields in polar coordinates

To write equation ( 1) in polar coordinates ( r, θ) (r,\theta) note that

 | ( log ⁡ z) ⋅ = r ˙ r + i ​ θ ˙ = v ⁡ ( z) z. {(\log z)}^{\cdot}=\frac{\dot{r}}{r}+i\dot{\theta}=\frac{v(z)}{z}. |  |

Hence,

(11) |  | r ˙ = r ​ Re ​ v ⁡ ( z) z = r ⁡ ( λ 1 + r ​ f λ ​ ( θ)), θ ˙ = Im ​ v ⁡ ( z) z = 1 + r ​ g λ ​ ( θ), \begin{array}[]{l}\dot{r}=r\mbox{Re }\dfrac{v(z)}{z}=r(\lambda_{1}+rf_{\lambda}(\theta)),\\ \dot{\theta}=\mbox{Im }\dfrac{v(z)}{z}=1+rg_{\lambda}(\theta),\end{array} |  |

where f λ f_{\lambda} and g λ g_{\lambda} are trigonometric polynomials of degree 3 3:

 | f λ ​ ( θ) = Re ​ h λ ​ ( θ), g λ ​ ( θ) = Im ​ h λ ​ ( θ), f_{\lambda}(\theta)=\mbox{Re }h_{\lambda}(\theta),\qquad g_{\lambda}(\theta)=\mbox{Im }h_{\lambda}(\theta), |  |

(12) |  | h λ ​ ( θ) = A ​ e i ​ θ + B ​ e − i ​ θ + C ​ e − 3 ​ i ​ θ. h_{\lambda}(\theta)=Ae^{i\theta}+Be^{-i\theta}+Ce^{-3i\theta}. |  |

For the normalized equations, | h λ ​ ( θ) | ≤ 4 |h_{\lambda}(\theta)|\leq 4. Hence,

(13) |  | | f λ ​ ( θ) | ≤ 4, | g λ ​ ( θ) | ≤ 4. |f_{\lambda}(\theta)|\leq 4,\ |g_{\lambda}(\theta)|\leq 4. |  |

### 2.2. Compactification

###### Lemma 7.

If a system v λ v_{\lambda} has at least one δ \delta –tame limit cycle, then | λ 1 | ≤ 4 / δ |\lambda_{1}|\leq 4/\delta.

###### Proof.

Let λ 1 > 4 δ \lambda_{1}>\frac{4}{\delta}. Recall that r ≤ δ − 1 r\leq\delta^{-1} in B ⁡ ( λ, δ) B(\lambda,\delta). Then in B ⁡ ( λ, δ) B(\lambda,\delta), r ˙ ≥ 0 \dot{r}\geq 0 by ( 11) and ( 13). Hence, the vector field v λ v_{\lambda} has no limit cycles in B ⁡ ( λ, δ) B(\lambda,\delta). ∎

### 2.3. Complex extension of the Poincaré map near zero

We will complexify nonautonomous equation corresponding to the system ( 11) making r r complex and denoting it by w w and keeping θ \theta real. We get:

(14) |  | d ​ w d ​ θ = w ​ λ 1 + w ​ f λ ​ ( θ) 1 + w ​ g λ ​ ( θ):= F λ ​ ( w, θ), w ∈ ℂ, θ ∈ 𝕊 1. \frac{dw}{d\theta}=w\frac{\lambda_{1}+wf_{\lambda}(\theta)}{1+wg_{\lambda}(\theta)}:=F_{\lambda}(w,\theta),\quad w\in\mathbb{C},\quad\theta\in\mathbb{S}^{1}. |  |

Recall that ‖ f λ ‖ ≤ 4 ||f_{\lambda}||\leq 4 and ‖ g λ ‖ ≤ 4 ||g_{\lambda}||\leq 4. When the norm is not specified, it is the C C –norm of a function on the circle.

For any value of λ 1 \lambda_{1}, we will find R R and ε {\varepsilon} in such a way that the orbit that starts in a cross–section D ε:= { | w | ≤ ε } × { 0 } D_{\varepsilon}:=\{|w|\leq{\varepsilon}\}\times\{0\} keeps inside W:= { | w | ≤ R } × 𝕊 1 W:=\{|w|\leq R\}\times\mathbb{S}^{1} when θ \theta ranges over [0, 2 ​ π] [0,2\pi]. We call this *property (*) of ( 14).*

###### Lemma 8.

Equation ( 14) satisfies property (*) for R = 0.01 R=0.01 and

(15) |  | ε = 2 ​ ε ​ ( λ) = { 0.001 ​ for ​ λ 1 ∈ [0, 0.1] R ​ e − 4 ​ λ 1 ​ π ​ for ​ λ 1 > 0.1. {\varepsilon}=2{\varepsilon}(\lambda)=\begin{cases}0.001\mbox{ for }\lambda_{1}\in[0,0.1]\\ Re^{-4\lambda_{1}\pi}\mbox{ for }\lambda_{1}>0.1.\end{cases} |  |

###### Proof.

The proof is based on the Gronwall inequality that measures the divergence of two solutions of a differential equation. To apply the classical Gronwall inequality to a differential equation with the complex phase space, we simply take the realification of this space. In case when one of the solutions is identically zero, the Gronwall inequality measures the norm of the other solution. For equation ( 14) this inequality has the folowing form. Let

 | L = max W ⁡ | ∂ F λ ∂ w |, L=\max_{W}\left|\frac{\partial F_{\lambda}}{\partial w}\right|, |  |

and | w ⁡ ( 0) | ≤ ε |w(0)|\leq{\varepsilon}. Then the Gronwall inequality claims that

(16) |  | | w ⁡ ( θ) | ≤ ε ​ e L ​ θ ​ for ​ θ ∈ [0, 2 ​ π], |w(\theta)|\leq{\varepsilon}e^{L\theta}\mbox{ for }\theta\in[0,2\pi], |  |

provided that

(17) |  | ε ​ e 2 ​ π ​ L ≤ R. {\varepsilon}e^{2\pi L}\leq R. |  |

To get an upper bound for L L, note that

(18) |  | ∂ F λ ∂ w = λ 1 + 2 ​ w ​ f λ 1 + w ​ g λ − w ⁡ ( λ 1 + w ​ f λ) ( 1 + w ​ g λ) 2 ​ g λ. \frac{\partial F_{\lambda}}{\partial w}=\frac{\lambda_{1}+2wf_{\lambda}}{1+wg_{\lambda}}-\frac{w(\lambda_{1}+wf_{\lambda})}{{(1+wg_{\lambda})}^{2}}g_{\lambda}. |  |

Note that ‖ f λ ‖ ≤ 4, ‖ g λ ‖ ≤ 4 ||f_{\lambda}||\leq 4,\ ||g_{\lambda}||\leq 4. Hence,

(19) |  | L ≤ { 0.2 ​ for ​ λ 1 ≤ 0.1, 2 ​ λ 1 ​ for ​ λ 1 > 0.1. L\leq\begin{cases}0.2\mbox{ for }\lambda_{1}\leq 0.1,\\ 2\lambda_{1}\mbox{ for }\lambda_{1}>0.1.\end{cases} |  |

Now, ( 17) yields Lemma 8. ∎

### 2.4. Description of K λ K_{\lambda}

Let Γ \Gamma be the positive x x semiaxis. Assume that system v λ v_{\lambda} has no δ \delta –tame limit cycles around the origin. Then Theorem 1 holds for this system. In what follows, we consider the opposite case. Let a ⁡ ( λ) a(\lambda) be the intersection point of the outmost tame limit cycle surrounding the origin with Γ \Gamma. Let s λ s_{\lambda} be the segment [0, a ⁡ ( λ)], [0,a(\lambda)], and ε ⁡ ( λ) {\varepsilon}(\lambda) be the same as in ( 15).

###### Lemma 9 (First Main Lemma).

For the set

(20) |  | K λ = s λ ∪ D ε ⁡ ( λ) K_{\lambda}=s_{\lambda}\cup D_{{\varepsilon}(\lambda)} |  |

the following lower estimates hold:

(21) |  | m ( λ):= max w ∈ K λ | P λ ( w) − w | ≥ 10 − 26 σ for λ 1 ≤ 0.1 and m(\lambda):=\max_{w\in K_{\lambda}}|P_{\lambda}(w)-w|\geq 10^{-26}\sigma\mbox{ for }\lambda_{1}\leq 0.1\mbox{ and } |  |

(22) |  | m ( λ) ≥ 10 − 26 / δ for λ 1 > 0.1. m(\lambda)\geq{10}^{-26/\delta}\mbox{ for }\lambda_{1}>0.1. |  |

Note that these estimates do not depend on κ \kappa. The lemma is proved in the next five subsections.

### 2.5. Proof of Lemma 9 for the case of a strong focus

In this subsection when we say that the normalized quadratic vector field has a strong focus we mean that λ 1 > 0.1 \lambda_{1}>0.1.

To prove Lemma 9 in this case, we use the reversed Cauchy inequality for the first derivative: if f f is holomorphic in a disc D ε = { | w | < ε } × { 0 } D_{\varepsilon}=\{|w|<{\varepsilon}\}\times\{0\} and continuous on the boundary of this disc, then

(23) |  | max D ε ⁡ | f | ≥ ε ​ | f ′ ​ ( 0) |. \max_{D_{\varepsilon}}|f|\geq{\varepsilon}|f^{\prime}(0)|. |  |

For f = P λ ​ ( w) − w f=P_{\lambda}(w)-w, and in the case λ 1 > 0.1 \lambda_{1}>0.1, we have:

 | f ′ ​ ( 0) = e 2 ​ π ​ λ 1 − 1 > 0.3 ​ e 2 ​ π ​ λ 1 f^{\prime}(0)=e^{2\pi\lambda_{1}}-1>0.3e^{2\pi\lambda_{1}} |  |

By Lemma 8, f f is well defined in D ε D_{\varepsilon} for ε = 0.005 ​ e − 4 ​ λ 1 ​ π {\varepsilon}=0.005e^{-4\lambda_{1}\pi}. Hence

 | m ≥ max D ε | f | ≥ 0.0015 e − 2 ​ λ 1 ​ π ≥ e − 26 / δ, m\geq\max_{D_{\varepsilon}}|f|\geq 0.0015e^{-2\lambda_{1}\pi}\geq e^{-26/\delta}, |  |

where the last inequality follows from λ 1 ≤ 4 δ \lambda_{1}\leq\frac{4}{\delta} and δ < 0.1 \delta<0.1. This yields ( 22) and proves Lemma 9 for λ 1 > 0.1 \lambda_{1}>0.1. To prove this lemma for λ 1 ≤ 0.1 \lambda_{1}\leq 0.1, we need first to study the case λ 1 = 0 \lambda_{1}=0 and then to perturb it.

### 2.6. Seven–jet of the Poincaré map for linear part a center

The Poincaré map for the point zero of the normalized quadratic vector field v λ v_{\lambda} may be decomposed in a Taylor series

(24) |  | P λ ​ ( w) = ∑ j ≥ 1 a j ​ ( λ) ​ w j. P_{\lambda}(w)=\sum_{j\geq 1}a_{j}(\lambda)w^{j}. |  |

This series converges at least in a neighborhood of the form D 0 = { | w | ≤ r 0 } D^{0}=\{|w|\leq r_{0}\} for a convenient r 0 > 0 r_{0}>0. Consider the case λ 1 = 0 \lambda_{1}=0. For such λ \lambda, the coefficients a j ​ ( λ) a_{j}(\lambda) become functions only of ( A, B, C) (A,B,C) not necessarily normalized.

###### Lemma 10.

Let λ 1 = 0 \lambda_{1}=0. Then for the decomposition ( 24),

 | a 1 ≡ 1, a 2 ≡ 0, a 3 = α 0 g 2, a 4 = α 1 g 2, a 5 = β 0 g 3 + β 1 g 2, a 6 = β 2 g 3 + β 3 g 2, a 7 = γ 0 g 4 + γ 1 g 3 + γ 2 g 2, \begin{array}[]{l}a_{1}\equiv 1,\ a_{2}\equiv 0,\ a_{3}={\alpha}_{0}g_{2},\ a_{4}={\alpha}_{1}g_{2},\\ a_{5}={\beta}_{0}g_{3}+{\beta}_{1}g_{2},\ a_{6}={\beta}_{2}g_{3}+{\beta}_{3}g_{2},\ a_{7}={\gamma}_{0}g_{4}+{\gamma}_{1}g_{3}+{\gamma}_{2}g_{2},\end{array} |  |

where g 2, g 3, g 4 g_{2},g_{3},g_{4} are the polynomials from the center conditions ( 5), α j, β j, γ j \alpha_{j},\beta_{j},\gamma_{j} are polynomials in the variables A, B, C A,B,C, and α 0, β 0, γ 0 \alpha_{0},\beta_{0},\gamma_{0} are constant. Moreover, on the set of λ = ( 0, A, B, C) \lambda=(0,A,B,C) with the tuples A, B, C A,B,C normalized we have:

 | | g 2 | ≤ 2, | g 3 | ≤ 30, | g 4 | ≤ 36; | α 0 | = 2 ​ π, | β 0 | = 2 ​ π 3, | β 1 | ≤ 2 ​ π 9 ( 284 + 108 π):= B 1 < 500, | γ 0 | = 5 ​ π 4, | γ 1 | ≤ π 72 ( 5816 + 1536 π):= C 1 < 500, | γ 2 | ≤ π ⁡ ( 5019144 + 2565120 ​ π + 345600 ​ π 2) 1080:= C 2 ∈ [4 ⋅ 10 4, 10 5]. \begin{array}[]{l}|g_{2}|\leq 2,\quad|g_{3}|\leq 30,\quad|g_{4}|\leq 36;\\ \\ |{\alpha}_{0}|=2\pi,\\ \\ |{\beta}_{0}|=\dfrac{2\pi}{3},\quad|{\beta}_{1}|\leq\dfrac{2\pi}{9}(284+108\pi):=B_{1}<500,\\ \\ |{\gamma}_{0}|=\dfrac{5\pi}{4},\quad|{\gamma}_{1}|\leq\dfrac{\pi}{72}(5816+1536\pi):=C_{1}<500,\\ \\ |{\gamma}_{2}|\leq\dfrac{\pi\left(5019144+2565120\pi+345600\pi^{2}\right)}{1080}:=C_{2}\in[4\cdot{10}^{4},{10}^{5}].\end{array} |  |

Expressions for the α {\alpha} ’s, β {\beta} ’s and γ {\gamma} ’s are given in the appendix.

Lemma 10 has been proved using the algebraic manipulator mathematica and the three normal forms for the quadratic vector fields. The algorithm is sketched in the appendix.

### 2.7. Lower estimate: case of a linear part a center

Denote the normalized tuple λ \lambda with λ 1 = 0 \lambda_{1}=0 by λ ′:= ( 0, A, B, C) \lambda^{\prime}:=(0,A,B,C). Recall that in ( 20), ε ⁡ ( λ ′) = 0.0005. {\varepsilon}(\lambda^{\prime})=0.0005. Let m ⁡ ( λ) m(\lambda) be the same as in ( 21). Recall that Λ ⁡ ( σ) \Lambda(\sigma) appears in Definition 2. The next lemma is one of the main steps in the proof of Theorem 1.

###### Lemma 11.

For the normalized λ ∈ Λ ⁡ ( σ) \lambda\in\Lambda(\sigma) with λ 1 = 0 \lambda_{1}=0, we have:

 | m ⁡ ( λ) ≥ 2 ⋅ 10 − 23 ​ σ:= m 0. m(\lambda)\geq 2\cdot{10}^{-23}\sigma:=m_{0}. |  |

###### Proof.

Let f λ = P λ − i ​ d f_{\lambda}=P_{\lambda}-id. By Lemma 10, for λ 1 = 0, λ = λ ′ \lambda_{1}=0,\lambda=\lambda^{\prime}, we have:

 | f λ ​ ( 0) = f λ ′ ​ ( 0) = f λ ′′ ​ ( 0) = 0. f_{\lambda}(0)=f^{\prime}_{\lambda}(0)=f^{\prime\prime}_{\lambda}(0)=0. |  |

For vector fields σ \sigma –distant from centers, we will prove a lower estimate:

 | | a j ​ ( λ) | ≥ m j ​ ( σ), |a_{j}(\lambda)|\geq m_{j}(\sigma), |  |

with m j m_{j} explicitly written for at least one j ∈ { 3; 5; 7 } j\in\{3;5;7\}. By Lemma 8 the function f λ f_{\lambda} is holomorphic in the disc | w | ≤ 0.001:= 2 ​ ε ​ ( λ ′) |w|\leq 0.001:=2{\varepsilon}(\lambda^{\prime}). Hence, there exists j ∈ { 3, 5, 7 } j\in\{3,5,7\} such that

 | m ⁡ ( λ) ≥ max D ε ⁡ ( λ ′) ⁡ | f λ | ≥ m j ​ ( σ) ⋅ ε ​ ( λ ′) j. m(\lambda)\geq\max_{D_{{\varepsilon}(\lambda^{\prime})}}|f_{\lambda}|\geq m_{j}(\sigma)\cdot{\varepsilon}{(\lambda^{\prime})}^{j}. |  |

The lower bounds for a j a_{j} are found in the following way. For α, β ∈ ( 0, 1) {\alpha},{\beta}\in(0,1) chosen later, the compact set Λ 0 ( σ) = Λ ( σ) ∩ { λ 1 = 0 } \Lambda_{0}(\sigma)=\Lambda(\sigma)\cap\{\lambda_{1}=0\} is split into three parts Σ 2, Σ 3, Σ 4 \Sigma_{2},\Sigma_{3},\Sigma_{4} where

 | Σ 2 = ( | g 2 | ≥ α ​ σ), Σ 3 = ( | g 2 | + | g 3 | ≥ β ​ σ) ∖ Σ 2, Σ 4 = Λ 0 ​ ( σ) ∖ ( Σ 2 ∪ Σ 3). \Sigma_{2}=(|g_{2}|\geq{\alpha}\sigma),\,\,\Sigma_{3}=(|g_{2}|+|g_{3}|\geq{\beta}\sigma)\setminus\Sigma_{2},\,\,\Sigma_{4}=\Lambda_{0}(\sigma)\setminus(\Sigma_{2}\cup\Sigma_{3}). |  |

On Σ j, | a 2 ​ j − 1 ​ ( λ) | \Sigma_{j},\ |a_{2j-1}(\lambda)| is estimated from below. By Lemma 10, on Σ 2 \Sigma_{2}, | a 3 | ≥ α 0 ​ α ​ σ |a_{3}|\geq{\alpha}_{0}{\alpha}\sigma. Let B 1, C 1, C 2 B_{1},C_{1},C_{2} be the same as in Lemma 10. On Σ 3 \Sigma_{3} we have:

 | a 5 = β 0 ​ g 3 + β 1 ​ g 2. a_{5}={\beta}_{0}g_{3}+{\beta}_{1}g_{2}. |  |

Hence,

 | | a 5 | | Σ 3 ≥ β 0 ( β − α) σ − B 1 α σ = β 0 ( β − α ( 1 + B 1 β 0)) σ. \left|a_{5}\left|{}_{\Sigma_{3}}\right.\right|\geq{\beta}_{0}({\beta}-{\alpha})\sigma-B_{1}{\alpha}\sigma={\beta}_{0}\left({\beta}-{\alpha}\left(1+\frac{B_{1}}{{\beta}_{0}}\right)\right)\sigma. |  |

If we choose α {\alpha} so small in comparison with β {\beta} that

(25) |  | α ⁡ ( 1 + B 1 β 0) ≤ β 2, {\alpha}\left(1+\frac{B_{1}}{\beta_{0}}\right)\leq\frac{{\beta}}{2}, |  |

then

 | | a 5 | Σ 3 | ≥ β 0 ​ β ​ σ 2. \left|a_{5}\left|{}_{\Sigma_{3}}\right.\right|\geq\frac{{\beta}_{0}{\beta}\sigma}{2}. |  |

On Σ 4 \Sigma_{4} we have:

 | a 7 = γ 0 ​ g 4 + γ 1 ​ g 3 + γ 2 ​ g 2. a_{7}={\gamma}_{0}g_{4}+{\gamma}_{1}g_{3}+{\gamma}_{2}g_{2}. |  |

As C 2 > C 1 C_{2}>C_{1}, we have:

 | | a 7 | | Σ 4 ≥ γ 0 ( 1 − β) σ − C 2 β σ = γ 0 ( 1 − β ( 1 + C 2 γ 0)) σ. \left|a_{7}\left|{}_{\Sigma_{4}}\right.\right|\geq{\gamma}_{0}(1-{\beta})\sigma-C_{2}{\beta}\sigma={\gamma}_{0}\left(1-{\beta}\left(1+\frac{C_{2}}{{\gamma}_{0}}\right)\right)\sigma. |  |

If β {\beta} is so small that

(26) |  | β ⁡ ( 1 + C 2 γ 0) ≤ 1 2, {\beta}\left(1+\frac{C_{2}}{{\gamma}_{0}}\right)\leq\frac{1}{2}, |  |

then

 | | a 7 | Σ 4 | ≥ γ 0 ​ σ 2. \left|a_{7}\left|{}_{\Sigma_{4}}\right.\right|\geq\frac{{\gamma}_{0}\sigma}{2}. |  |

Now,

 | | m | Σ 4 | ≥ min Σ 4 | a 7 | r 7 0 ≥ γ 0 ​ σ 2 ε ( λ ′) 7:= m 4 σ | m | Σ 3 | ≥ min Σ 3 | a 5 | r 5 0 ≥ β 0 ​ β ​ σ 2 ε ( λ ′) 5:= m 3 σ | m | Σ 2 | ≥ min Σ 2 | a 3 | r 3 0 ≥ α 0 α σ ε ( λ ′) 3:= m 2 σ. \begin{array}[]{l}\left|m\left|{}_{\Sigma_{4}}\right.\right|\geq\displaystyle\min_{\Sigma_{4}}|a_{7}|r^{7}_{0}\geq\dfrac{{\gamma}_{0}\sigma}{2}{\varepsilon}(\lambda^{\prime})^{7}:=m_{4}\sigma\\ \left|m\left|{}_{\Sigma_{3}}\right.\right|\geq\displaystyle\min_{\Sigma_{3}}|a_{5}|r^{5}_{0}\geq\dfrac{{\beta}_{0}{\beta}\sigma}{2}{\varepsilon}(\lambda^{\prime})^{5}:=m_{3}\sigma\\ \left|m\left|{}_{\Sigma_{2}}\right.\right|\geq\displaystyle\min_{\Sigma_{2}}|a_{3}|r^{3}_{0}\geq{\alpha}_{0}{\alpha}\sigma{\varepsilon}(\lambda^{\prime})^{3}:=m_{2}\sigma.\end{array} |  |

Due to Lemma 10, inequalities ( 25), ( 26) hold for β = 10 − 5, α = 2 ⋅ 10 − 8 \beta={10}^{-5},\alpha=2\cdot{10}^{-8}. Again by Lemma 10, m 2 > m 3 > m 4 > 2 ⋅ 10 − 23 m_{2}>m_{3}>m_{4}>2\cdot{10}^{-23}. This proves Lemma 11.

∎

### 2.8. Proof of the First Main Lemma in case of the moderate focus

Recall that m 0 m_{0} is the lower estimate of max D ε ⁡ | P − i ​ d | \max_{D_{\varepsilon}}|P-id| mentioned in Lemma 11. Here we consider the case λ 1 ∈ [m 0, 0.1] \lambda_{1}\in[m_{0},0.1]. In this case, by Lemma 8, the displacement f λ f_{\lambda} of the Poincaré map is holomorphic in a disc | w | ≤ ε = 0.0005 |w|\leq{\varepsilon}=0.0005. We have:

 | | f λ ′ ​ ( 0) | ≥ e 2 ​ π ​ m 0 − 1 ≥ 2 ​ π ​ m 0. |f^{\prime}_{\lambda}(0)|\geq e^{2\pi m_{0}}-1\geq 2\pi m_{0}. |  |

Hence,

 | max | w | ≤ ε ⁡ | f λ | ≥ 0.003 ​ m 0. \max_{|w|\leq{\varepsilon}}|f_{\lambda}|\geq 0.003m_{0}. |  |

This proves the First Main Lemma in the case considered.

### 2.9. Proof of the First Main Lemma in case of the slow focus

We consider here the last remaining case λ 1 ∈ ( 0, m 0] \lambda_{1}\in(0,m_{0}], where m 0 m_{0} is the same as in Lemma 11, i.e. m 0 = 2 ⋅ 10 − 23 ​ σ m_{0}=2\cdot 10^{-23}\sigma. This case is treated as a small perturbation of the case λ 1 = 0 \lambda_{1}=0. Consider two systems ( 14) corresponding to λ 1 = 0 \lambda_{1}=0 and λ 1 ∈ ( 0, m 0] \lambda_{1}\in(0,m_{0}] fixed. Let their right hand sides be F F and G G. We assume that G G corresponds to a normalized quadratic vector field which is σ \sigma -distant from centers. This implies that F F corresponds to a similar field which is at least 0.9 ​ σ 0.9\sigma -distant from centers. Let

 | max W ⁡ | F − G | < Δ, \max_{W}|F-G|<\Delta, |  |

 | max W ⁡ | ∂ F ∂ w | < L, \max_{W}\left|\frac{\partial F}{\partial w}\right|<L, |  |

where as before W = { | w | ≤ R } × 𝕊 1, R = 0.01 W=\{|w|\leq R\}\times\mathbb{S}^{1},\ R=0.01. Let ε = e − 2 ​ π ​ L ​ R {\varepsilon}=e^{-2\pi L}R; clearly, m 0 < R 2 m_{0}<\frac{R}{2}. Then the solutions w F w_{F} and w G w_{G} of the equations d ​ w d ​ z = F \dfrac{dw}{dz}=F and d ​ w d ​ z = G \dfrac{dw}{dz}=G with the same initial condition w ⁡ ( 0): | w ⁡ ( 0) | < ε 2 w(0):|w(0)|<\frac{{\varepsilon}}{2} diverge on the segment 0 ≤ θ ≤ 2 ​ π 0\leq{\theta}\leq 2\pi no more than

(27) |  | | w F ​ ( θ) − w G ​ ( θ) | ≤ 2 ​ π ​ Δ ​ e 2 ​ π ​ L. |w_{F}({\theta})-w_{G}({\theta})|\leq 2\pi{\Delta}e^{2\pi L}. |  |

We apply ( 27) to our F F and G G. We have:

 | Δ = max W ⁡ | w ​ λ 1 1 − w ​ g λ | ≤ m 0 96 {\Delta}=\max_{W}\left|\frac{w\lambda_{1}}{1-wg_{\lambda}}\right|\leq\frac{m_{0}}{96} |  |

in W W. On the other hand, L ≤ 0.2 L\leq 0.2 by ( 19). Hence, for any two solutions w F w_{F} and w G w_{G} with the initial condition w ⁡ ( 0) w(0) and | w ⁡ ( 0) | ≤ ε ⁡ ( 0) = 0.0005 |w(0)|\leq{\varepsilon}(0)=0.0005, we have

 | | w F ​ ( 2 ​ π) − w G ​ ( 2 ​ π) | ≤ 2 ​ π ​ e 0.4 ​ π 96 ​ m 0 < 0.4 ​ m 0. |w_{F}(2\pi)-w_{G}(2\pi)|\leq\frac{2\pi e^{0.4\pi}}{96}m_{0}<0.4\ m_{0}. |  |

Suppose now that w ​ ( 0) = w F ​ ( 0) w(0)=w_{F}(0) corresponds to the solution w F w_{F} for which | w F ​ ( 2 ​ π) − w F ​ ( 0) | ≥ 0.9 ​ m 0 |w_{F}(2\pi)-w_{F}(0)|\geq 0.9\ m_{0}, and w G ​ ( 0) = w F ​ ( 0) w_{G}(0)=w_{F}(0). Then | w G ​ ( 2 ​ π) − w G ​ ( 0) | ≥ m 0 2 |w_{G}(2\pi)-w_{G}(0)|\geq\dfrac{m_{0}}{2}, and Lemma 9 is proved.

## 3. Upper estimate of the displacement of the Poincaré map

In this section we construct a neighborhood U λ U_{\lambda} of the set K λ K_{\lambda} where the Poincaré map P λ P_{\lambda} of equation v λ v_{\lambda} is well defined. We give a lower estimate of the gap ε {\varepsilon} between K λ K_{\lambda} and ∂ U λ \partial U_{\lambda}, and find an upper estimate for f λ = P λ − id. f_{\lambda}=P_{\lambda}-\mbox{id}. To this end, we find a universal gap between δ \delta –tame limit cycles of quadratic vector fields that are κ \kappa –distant from singular quadratic vector fields, and the curve θ ˙ = 0. \dot{\theta}=0.

### 3.1. The universal gap

A well known elementary property of quadratic vector fields ( 1) claims that any closed orbit of these fields that surrounds the singular point zero belongs to the domain θ ˙ > 0 \dot{\theta}>0. It is a simple consequence of the fact that any line has at most two contact points with a quadratic vector field. The boundary of this domain is given by the equation r = − 1 / g λ ( θ) r=-1/g_{\lambda}(\theta).

###### Lemma 12 (Second Main Lemma).

No δ \delta –tame limit cycle of a normalized vector field κ \kappa –distant from singular quadratic vector fields intersects the curvilinear strip

 | Π β = { ( θ, r) ∈ B λ | r ∈ [− 1 g λ ​ ( θ) − β, − 1 g λ ​ ( θ)] } ​ for ​ β = δ 14 ​ κ 10 10. \Pi_{\beta}=\left\{({\theta},r)\in B_{\lambda}|\ r\in\left[-\frac{1}{g_{\lambda}({\theta})}-{\beta},\ -\frac{1}{g_{\lambda}({\theta})}\right]\right\}\,\,{\rm for}\,\,{\beta}=\frac{\delta^{14}\kappa}{{10}^{10}}. |  |

The proof of this lemma is technical. In the rest of this subsection we make the first step of the proof that makes the existence of the gap obvious. The estimates of the size of the gap are presented in Section 4.

Consider a zero isocline Γ {\Gamma}:

 | θ ˙ = 0, r = − 1 g λ ​ ( θ). \dot{\theta}=0,\ r=-\frac{1}{g_{\lambda}({\theta})}. |  |

The restriction of r ˙ \dot{r} to this isocline equals

 | r ˙ | Γ = H ⁡ ( v λ) g λ 2, H ⁡ ( v λ) = λ 1 ​ g λ − f λ. \dot{r}|_{\Gamma}=\frac{H(v_{\lambda})}{g^{2}_{\lambda}},\qquad H(v_{\lambda})=\lambda_{1}g_{\lambda}-f_{\lambda}. |  |

For the proof of Lemma 12, we need a lower estimate of | H ⁡ ( v λ) | Γ ∩ B λ, δ | \left|H(v_{\lambda})|_{{\Gamma}\cap B_{\lambda,\delta}}\right|. First of all, we estimate from below the L 2 L_{2} –norm ‖ H ⁡ ( v λ) ‖ 2 {||H(v_{\lambda})||}_{2} of H ⁡ ( v λ) H(v_{\lambda}) on 𝕊 1 = ℝ / 2 ​ π ​ ℤ \mathbb{S}^{1}=\mathbb{R}/2\pi\mathbb{Z}. By ( 12),

 | H ⁡ ( v λ) = Im ​ μ ¯ ​ h λ. H(v_{\lambda})=\mbox{Im }\bar{\mu}h_{\lambda}. |  |

Note that H ⁡ ( v λ) H(v_{\lambda}) is linear with respect to v λ v_{\lambda}. Let v λ = v s + u λ v_{\lambda}=v_{s}+u_{\lambda} be the decomposition ( 8) for v λ v_{\lambda}. For the singular vector field v s v_{s} we have: H ⁡ ( v s) ≡ 0 H(v_{s})\equiv 0. Hence,

 | H ⁡ ( v λ) = H ⁡ ( u λ) = Im ​ μ ¯ ​ h ~ λ, H(v_{\lambda})=H(u_{\lambda})=\mbox{Im }\bar{\mu}\tilde{h}_{\lambda}, |  |

where h ~ λ = b ​ e − i ​ θ + c ​ e − 3 ​ i ​ θ \tilde{h}_{\lambda}=be^{-i{\theta}}+ce^{-3i{\theta}}.

Consider an arbitrary trigonometric polynomial H H on ℝ / 2 ​ π ​ ℤ \mathbb{R}/2\pi\mathbb{Z}. If H H contains no complex conjugate monomials, that is, for any entry a ​ e i ​ n ​ θ + b ​ e − i ​ n ​ θ ae^{in{\theta}}+be^{-in{\theta}} at least one coefficient is 0 0 (i.e. a ​ b = 0 ab=0), then

 | ‖ Im ​ H ‖ 2 2 = ‖ Re ​ H ‖ 2 2 = 1 2 | | H | | 2 2. {||\mbox{Im }H||}^{2}_{2}={||\mbox{Re }H||}^{2}_{2}=\frac{1}{2}{||H||}^{2}_{2}. |  |

Indeed H = ∑ a n ​ e i ​ n ​ θ H=\sum a_{n}e^{in{\theta}} implies that Re ​ H = 1 2 ​ ( ∑ ( a n ​ e i ​ n ​ θ + a ¯ n ​ e − n ​ θ)) \mbox{Re}H=\frac{1}{2}(\sum(a_{n}e^{in{\theta}}+\bar{a}_{n}e^{-n{\theta}})), and consequently ‖ Re ​ H ‖ 2 2 = 1 4 ​ ∑ ( | a n | 2 + | a ¯ n | 2) = 1 2 ​ ‖ H ‖ 2 2. {||\mbox{Re}H||}^{2}_{2}=\dfrac{1}{4}\sum(|a_{n}|^{2}+|\bar{a}_{n}|^{2})=\frac{1}{2}{||H||}^{2}_{2}. The last conclusion holds because there are no cancelations in the sum for Re ​ H \mbox{Re }H, by assumption. The same argument proves the statement for Im ​ H \mbox{Im }H.

###### Corollary 13.

For v λ v_{\lambda} which is κ \kappa –distant from singular vector fields ‖ H ⁡ ( v λ) ‖ 2 ≥ | μ | 2 ​ κ {||H(v_{\lambda})||}_{2}\geq\dfrac{|\mu|}{\sqrt{2}}\kappa.

Indeed, for equations, κ \kappa -distant from singular ones, we have ‖ H ⁡ ( v λ) ‖ 2 = 1 2 ​ | μ | ​ b 2 + c 2 ≥ | μ | ​ κ 2 {||H(v_{\lambda})||}_{2}=\frac{1}{\sqrt{2}}|\mu|\sqrt{b^{2}+c^{2}}\geq\frac{|\mu|\kappa}{\sqrt{2}}.

We got therefore a uniform lower bound for the L 2 L_{2} –norm of the restriction r ˙ | Γ \dot{r}|_{\Gamma}. It is now clear that a similar bound would exist for min ⁡ r ˙ | Γ ∩ B ⁡ ( δ, λ) \min\dot{r}|_{{\Gamma}\cap B(\delta,\lambda)}. Indeed, zeros of r ˙ | Γ \dot{r}|_{\Gamma} are located at the singular points of v λ v_{\lambda}, and all the points of B ⁡ ( δ, λ) B(\delta,\lambda) are at least δ \delta –distant from these points. After min ⁡ r ˙ | Γ ∩ B ⁡ ( λ, δ) \min\dot{r}|_{\Gamma\cap B(\lambda,\delta)} is estimated, it is easy to prove that the lower boundary of the curvilinear strip Π β \Pi_{\beta} has no contacts with the field v λ v_{\lambda}. ¿From this it follows that the δ \delta -tame limit cycles can not intersect π β \pi_{\beta}. The detailed proof of Lemma 12 is completed in Section 4.

### 3.2. Construction of the larger domain U U in the Growth-and-Zeros Theorem

Let

 | S λ = s λ ∖ D ε ⁡ ( λ) S_{\lambda}=s_{\lambda}\setminus D_{{\varepsilon}(\lambda)} |  |

and

 | 𝔻 = B ( δ, λ) ∩ { r ≤ − 1 g λ ​ ( θ) − β } \mathbb{D}=B(\delta,\lambda)\cap\left\{r\leq\frac{-1}{g_{\lambda}(\theta)}-\beta\right\} |  |

For any λ ∈ Λ \lambda\in\Lambda, consider a ( β ​ δ) / 32 ({\beta}\delta)/32 -neighborhood D ′ D^{\prime} of the domain 𝔻 ⊂ ℝ + × 𝕊 1 \mathbb{D}\subset\mathbb{R}^{+}\times\mathbb{S}^{1} in ℂ × S 1 \mathbb{C}\times S^{1}. We will choose ε {\varepsilon} in such a way that any orbit of v λ v_{\lambda} that starts in U ε × { 0 } U_{\varepsilon}\times\{0\}, where U = U ε U=U_{\varepsilon} is the ε {\varepsilon} –neighborhood of S λ S_{\lambda}, stays in D ′ D^{\prime} while θ \theta ranges in [0, 2 ​ π] [0,2\pi]. Let

 | L = max D ′ ⁡ | ∂ F λ ∂ w |. L=\max_{D^{\prime}}\left|\frac{\partial F_{\lambda}}{\partial w}\right|. |  |

Then, by the Gronwall inequality,

(28) |  | ε = β ​ δ 32 ​ e − 2 ​ π ​ L {\varepsilon}=\frac{{\beta}\delta}{32}e^{-2\pi L} |  |

should be the desired one. Indeed, the largest δ \delta -tame limit cycle keeps in 𝔻 \mathbb{D} by Lemma 12. Hence, all the orbits that start on S λ × { 0 } S_{\lambda}\times\{0\}, keep in D D by definition of S λ S_{\lambda}. Then, for ε {\varepsilon} from ( 28), the orbits that start in U ε × { 0 } U_{\varepsilon}\times\{0\} would not quit D ′ D^{\prime} for θ ∈ [0, 2 ​ π] \theta\in[0,2\pi]. Moreover, they will be β ​ δ 32 \dfrac{{\beta}\delta}{32} –close to the real orbits starting at S λ S_{\lambda}. Hence, the Poincaré map for v λ v_{\lambda} is well defined in U ε U_{\varepsilon}, and

 | max U ε ⁡ | f λ | = max U ε ⁡ | P λ − id | ≤ δ − 1 + β ​ δ 32. \max_{U_{\varepsilon}}|f_{\lambda}|=\max_{U_{\varepsilon}}|P_{\lambda}-\mbox{id}|\leq\delta^{-1}+\frac{{\beta}\delta}{32}. |  |

By Lemma 8, the orbits that start in D 2 ​ ε ​ ( λ) D_{2{\varepsilon}(\lambda)} stay in D R × 𝕊 1 D_{R}\times\mathbb{S}^{1} as θ \theta ranges over [0, 2 ​ π]. [0,2\pi]. So, the set U λ = U ε ∪ D 2 ​ ε ​ ( λ) U_{\lambda}=U_{\varepsilon}\cup D_{2{\varepsilon}(\lambda)} is a neighborhood of K λ K_{\lambda} in which the Poincaré map of v λ v_{\lambda} is holomorphic, and

(29) |  | max U λ ⁡ | f λ | = M ≤ δ − 1 + 1. \max_{U_{\lambda}}|f_{\lambda}|=M\leq\delta^{-1}+1. |  |

### 3.3. The final estimate

We can now estimate the geometric factor in the Growth-and-Zeros Theorem . For this we need to get an upper bound for L L, then a lower bound for ε {\varepsilon}.

To estimate L L, we first get a lower estimate for the denominator in the relation ( 18) for ∂ F ∂ w \dfrac{\partial F}{\partial w}. We have:

 | | w | D ′ ≤ δ − 1 + β ​ δ 32 << 2 ​ δ − 1. |w|_{D^{\prime}}\leq\delta^{-1}+\frac{\beta\delta}{32}<<2\delta^{-1}. |  |

Now, estimate min D ′ ⁡ | l + w ​ g λ | \min_{D^{\prime}}|l+wg_{\lambda}|. If ( w, θ) ∈ D ′ (w,\theta)\in D^{\prime} is such that | g λ ​ ( θ) | ≤ δ 4 |g_{\lambda}(\theta)|\leq\frac{\delta}{4}, then | l + w ​ g λ | ≥ 1 − 2 δ ⋅ δ 4 ≥ 1 2 |l+wg_{\lambda}|\geq 1-\frac{2}{\delta}\cdot\frac{\delta}{4}\geq\frac{1}{2}. Suppose that | g λ ​ ( θ) | |g_{\lambda}(\theta)| is now greater than δ 4 \frac{\delta}{4}. Find a point ( w ′, θ) ∈ 𝔻 (w^{\prime},\theta)\in\mathbb{D} with | w ′ − w | < β ​ δ 32 |w^{\prime}-w|<\frac{{\beta}\delta}{32}. Then

 | | 1 + w ​ g λ | ≥ | 1 g λ + w ′ | ​ | g λ | − | g λ | ​ | w ′ − w | ≥ β ​ δ 4 − 4 ​ β ​ δ 32 ≥ β ​ δ 8. |1+wg_{\lambda}|\geq|\frac{1}{g_{\lambda}}+w^{\prime}||g_{\lambda}|-|g_{\lambda}||w^{\prime}-w|\geq{\beta}\frac{\delta}{4}-4\frac{{\beta}\delta}{32}\geq\frac{{\beta}\delta}{8}. |  |

Hence, min D ′ ⁡ | 1 + w ​ g λ | ≥ β ​ δ 8 \min_{D^{\prime}}|1+wg_{\lambda}|\geq\frac{{\beta}\delta}{8}.

Moreover, by Lemma 7, λ 1 ≤ 4 ​ δ − 1 \lambda_{1}\leq 4\delta^{-1}. Hence, by ( 18),

 | L ≤ 6145 ​ δ − 3 ​ β − 2. L\leq 6145\delta^{-3}\beta^{-2}. |  |

We substitute this L L into ( 28) and get the expression for ε {\varepsilon} through δ \delta and β \beta. Note that the expression of β \beta through δ, σ, κ \delta,\sigma,\kappa is given in Lemma 12.

The intrinsic diameter D ≤ 2 ​ δ − 1 D\leq 2\delta^{-1}. Hence,

 | 2 ​ D ε ≤ 128 ​ δ − 2 ​ β − 1 ​ e ( 10 5 − 2) ​ δ − 3 ​ β − 2. \frac{2D}{{\varepsilon}}\leq 128\delta^{-2}{\beta}^{-1}e^{({10}^{5}-2)\delta^{-3}{\beta}^{-2}}. |  |

This provides a double exponential estimate for the geometric factor exp ⁡ 2 ​ D ε \exp\dfrac{2D}{{\varepsilon}}.

Note that for δ < 0.1 \delta<0.1 and β < 0.1 {\beta}<0.1, increasing the factor 10 5 − 2 {10}^{5}-2 in the exponential by one will compensate well the division by the first factor. Finally,

(30) |  | 2 ​ D ε ≤ e ( 10 5 − 1) ​ δ − 3 ​ β − 2. \frac{2D}{{\varepsilon}}\leq e^{({10}^{5}-1)\delta^{-3}{\beta}^{-2}}. |  |

We can now estimate the Bernstein index of f λ f_{\lambda}. The numerator in ( 10) is estimated in ( 29). The denominator is estimated in the First Main Lemma (Lemma 9). We replace it by even smaller value:

 | m = max K λ ⁡ | f λ | ≥ 10 − 26 δ ​ σ. m=\max_{K_{\lambda}}|f_{\lambda}|\geq{10}^{-\frac{26}{\delta}}\sigma. |  |

Finally, the Bernstein index of f λ f_{\lambda} is:

 | B U λ, K λ ​ ( f λ) = log ⁡ M ⁡ ( Λ) m ⁡ ( λ) ≤ log ⁡ 2 − log ⁡ δ + 26 δ ​ log ​ 10 − log ⁡ σ. B_{U_{\lambda},K_{\lambda}}(f_{\lambda})=\log\frac{M(\Lambda)}{m(\lambda)}\leq\log 2-\log\delta+\frac{26}{\delta}\log 10-\log\sigma. |  |

We see that this index, whose estimate took the main part of the work, is in a sense negligible in comparison with the geometric factor. Replacing of this index by | log ⁡ σ | |\log\sigma| may be well compensated through the increasing by 1 1 the exponential 10 5 − 1 {10}^{5}-1 in ( 30).

Finally, by the Growth-and-Zeros Theorem we have:

 | H ⁡ ( 2, δ, σ, κ) < | log ⁡ σ | ​ e e 10 5 ​ δ − 3 ​ β − 2. H(2,\delta,\sigma,\kappa)<|\log\sigma|e^{e^{{10}^{5}\delta^{-3}{\beta}^{-2}}}. |  |

Substituting here the value of β {\beta} from Lemma 12 (which is not yet proved), we obtain Theorem 5.

## 4. Some lower bounds for trigonometric polynomials

In this subsection we complete the proof of Lemma 12.

### 4.1. Homogeneous polynomials of degree three

###### Lemma 14.

Consider a real homogeneous trigonometric polynomial H H of degree 3, that is, a homogeneous three–form on sin ⁡ θ, cos ⁡ θ \sin\theta,\cos\theta with real coefficients. Let ℝ α \mathbb{R}_{\alpha} be the set of all real θ \theta that are at least α {\alpha} –distant from the complex rots of H H. Then

 | min ℝ α ⁡ | H | ≥ α 3 24 ​ ‖ H ‖ 2. \min_{\mathbb{R}_{{\alpha}}}|H|\geq\frac{{\alpha}^{3}}{24}\|H\|_{2}. |  |

###### Proof.

The polynomial H H has three series of roots counted with multiplicities: θ j + π ​ n, n ∈ ℤ, j = 1, 2, 3. \theta_{j}+\pi n,n\in\mathbb{Z},j=1,2,3. Hence, for some real A A,

 | H = A ​ ∏ 1 3 sin ⁡ ( θ − θ j). H=A\prod_{1}^{3}\sin(\theta-\theta_{j}). |  |

Case 1. All θ j \theta_{j} are real. Then

(31) |  | min ℝ α ⁡ | H | ≥ | A | ​ ( 2 π) 3 ​ α 3. \min_{\mathbb{R}_{\alpha}}|H|\geq|A|\left(\frac{2}{\pi}\right)^{3}{\alpha}^{3}. |  |

On the other hand,

 | | A | ≥ ‖ H ‖ 2 2 ​ π. |A|\geq\frac{\|H\|_{2}}{\sqrt{2\pi}}. |  |

The inequality: 2 2.5 / π 3.5 ≥ 1 / 24 2^{2.5}/\pi^{3.5}\geq 1/24 implies the lemma in Case 1.

Case 2. One root θ 1 \theta_{1} is real, two others are complex: θ 2, 3 = φ ± i ​ ψ, ψ ≠ 0. \theta_{2,3}=\varphi\pm i\psi,\psi\not=0. Then

 | H = A ​ ∏ 1 3 sin ⁡ ( θ − θ j) = A 2 ​ sin ⁡ ( θ − θ 1) ​ ( ch ​ 2 ​ ψ − cos ⁡ 2 ​ ( θ − φ)). H=A\prod_{1}^{3}\sin(\theta-\theta_{j})=\frac{A}{2}\sin(\theta-\theta_{1})(\mbox{ch}2\psi-\cos 2(\theta-\varphi)). |  |

For any a ∈ ℝ, | b | ≤ π a\in\mathbb{R},\ |b|\leq\pi, the following inequality holds:

 | ch ​ a − cos ⁡ b ≥ 1 2 ​ a 2 + ( 2 π) 2 ​ b 2. \mbox{ch}\,a-\cos b\geq\frac{1}{2}a^{2}+\left(\frac{2}{\pi}\right)^{2}b^{2}. |  |

By assumption, ψ 2 + ( θ − φ) 2 ≥ α 2 \psi^{2}+{(\theta-{\varphi})}^{2}\geq{\alpha}^{2}. Hence, once again we have ( 31). This proves the lemma in case 2. ∎

### 4.2. Lower bounds for the distance to the roots

If two points of the disk r ≤ δ − 1 r\leq\delta^{-1} are at least δ \delta –distant in Cartesian coordinates, then they are at least δ 2 \delta^{2} –distant in the polar coordinates. If two points, one in the disk r ≤ δ − 1 r\leq\delta^{-1} in ℝ 2 \mathbb{R}^{2}, another in ℂ 2 \mathbb{C}^{2}, are at least δ \delta -distant in Cartesian coordinates, δ < 0.1 \delta<0.1, then they are at least 2 3 ​ δ 2 \frac{2}{3}\delta^{2} -distant in complex polar coordinates.

###### Proposition 15.

Suppose that the point ( θ 0, r), r ≤ δ − 1 (\theta_{0},r),\ r\leq\delta^{-1} and θ 0 ∈ [0, 2 ​ π] \theta_{0}\in[0,2\pi] is at least 2 3 ​ δ 2 \frac{2}{3}\delta^{2} –distant from the singular points of the system ( 11) with complexified r r and θ \theta in the metric d ​ s 2 = | d ​ r | 2 + | d ​ θ | 2 ds^{2}={|dr|}^{2}+{|d\theta|}^{2}, and

(32) |  | | r + 1 g λ ​ ( θ 0) | < δ 2 2. \left|r+\frac{1}{g_{\lambda}(\theta_{0})}\right|<\frac{\delta^{2}}{2}. |  |

Then

(33) |  | d ( θ 0, { H ( v λ) = 0 }) ≥ δ 4 100. d(\theta_{0},\{H(v_{\lambda})=0\})\geq\frac{\delta^{4}}{100}. |  |

###### Proof.

By contraposition, assume that the converse to ( 33) is true. Then there exists θ 1 {\theta}_{1}, zero of H ⁡ ( v λ) H(v_{\lambda}) such that

 | | θ 0 − θ 1 | < α:= δ 4 100. |{\theta}_{0}-{\theta}_{1}|<{\alpha}:=\frac{\delta^{4}}{100}. |  |

It may happen that θ 1 {\theta}_{1} is non–real. Take two extra points: b = ( θ 0, − 1 g λ ​ ( θ 0)) b=\left({\theta}_{0},-\dfrac{1}{g_{\lambda}({\theta}_{0})}\right) and c = ( θ 1, − 1 g λ ​ ( θ 1)) c=\left({\theta}_{1},-\dfrac{1}{g_{\lambda}({\theta}_{1})}\right); and let a = ( θ 0, r) a=({\theta}_{0},r). Then, by ( 32),

 | | b − a | ≤ δ 2 2. |b-a|\leq\frac{\delta^{2}}{2}. |  |

Let L = max [θ 0, θ 1] ⁡ | ( 1 g λ) ′ | L=\displaystyle\max_{[{\theta}_{0},{\theta}_{1}]}\left|{\left(\dfrac{1}{g_{\lambda}}\right)}^{\prime}\right|. By assumption, | θ 0 − θ 1 | ≤ α |{\theta}_{0}-{\theta}_{1}|\leq{\alpha}. Then, by the Mean Value Theorem,

 | | b − c | ≤ α ​ L 2 + 1. |b-c|\leq{\alpha}\sqrt{L^{2}+1}. |  |

We now estimate L L from above. Recall that g λ = Im ​ h λ, h λ = A ​ e i ​ φ + B ​ e − i ​ φ + C ​ e − 3 ​ i ​ φ, | A | ≤ 1, | B | ≤ 2, | C | ≤ 1 g_{\lambda}=\mbox{Im }h_{\lambda},\ h_{\lambda}=Ae^{i{\varphi}}+Be^{-i{\varphi}}+Ce^{-3i{\varphi}},\ |A|\leq 1,|B|\leq 2,|C|\leq 1. By ( 32) and assumption r ≤ δ − 1 r\leq\delta^{-1}, we have:

 | | g λ ​ ( θ 0) | ≥ 1 δ − 1 + δ 2 2 ≥ δ − δ 4 2 ≥ 0.99 ​ δ. |g_{\lambda}({\theta}_{0})|\geq\dfrac{1}{\delta^{-1}+\dfrac{\delta^{2}}{2}}\geq\delta-\frac{\delta^{4}}{2}\geq 0.99\delta. |  |

Now, by ( 12)

 | g λ = Im ​ h λ, | g λ ′ | ≤ | h λ ′ | ≤ | A | ​ e α + | B | ​ e α + 3 ​ | C | ​ e 3 ​ α ≤ 7. g_{\lambda}=\mbox{Im }h_{\lambda},\qquad|g^{\prime}_{\lambda}|\leq|h^{\prime}_{\lambda}|\leq|A|e^{\alpha}+|B|e^{\alpha}+3|C|e^{3{\alpha}}\leq 7. |  |

Then L < 8 ​ δ − 2 L<8\delta^{-2}. Hence, α ​ L 2 + 1 < δ 2 6 {\alpha}\sqrt{L^{2}+1}<\dfrac{\delta^{2}}{6}. Therefore, | a − c | ≤ | a − b | + | b − c | < 2 3 ​ δ 2 |a-c|\leq|a-b|+|b-c|<\frac{2}{3}\delta^{2}, a contradiction. ∎

### 4.3. Proof of Lemma 12

In order to prove that no limit cycle can cross Π β \Pi_{\beta}, let us first check that the lower bound Γ − {\Gamma}^{-} of Π β \Pi_{\beta} is a curve without contacts with the vector field ( 11). This lower bound has the form:

(34) |  | Γ −: r = − 1 g λ ​ ( θ) − β, ( r, θ) ∈ B ⁡ ( λ, δ), {\Gamma}^{-}:r=-\frac{1}{g_{\lambda}(\theta)}-{\beta},\ (r,\theta)\in B(\lambda,\delta), |  |

Denote by S S the minimal slope of the field ( 11) on Γ − {\Gamma}^{-}:

 | S = min Γ − ⁡ | d ​ r d ​ θ | = min Γ − ⁡ | r ​ λ 1 + r ​ f λ 1 + r ​ g λ |. S=\min_{{\Gamma}^{-}}\left|\frac{dr}{d\theta}\right|=\min_{{\Gamma}^{-}}\left|r\frac{\lambda_{1}+rf_{\lambda}}{1+rg_{\lambda}}\right|. |  |

On Γ − \Gamma^{-} we have:

 | | λ 1 + r ​ f λ | = | 1 g λ ​ ( H ⁡ ( v λ) − β ​ g λ ​ f λ) | ≥ 1 4 ​ ( | H ⁡ ( v λ) | − 16 ​ β). |\lambda_{1}+rf_{\lambda}|=\left|\frac{1}{g_{\lambda}}(H(v_{\lambda})-\beta g_{\lambda}f_{\lambda})\right|\geq\frac{1}{4}(|H(v_{\lambda})|-16{\beta}). |  |

The points of B ⁡ ( λ, δ) B(\lambda,\delta) are at least δ \delta –distant from the singular points of system ( 11). By the remark at the beginning of Subsection 4.2, points of Γ − {\Gamma}^{-} satisfy assumptions of Proposition 15. Hence, for any θ \theta such that ( r, θ) ∈ Γ − (r,\theta)\in{\Gamma}^{-} for some r r, we have ( 33). Now, taking α = δ 4 100 {\alpha}=\dfrac{\delta^{4}}{100} in Lemma 14, we conclude that

 | min Γ − ⁡ | H ⁡ ( v λ) | ≥ α 3 24 ​ ‖ H ⁡ ( v λ) ‖ 2 = δ 12 10 6 ⋅ 24 | | H ⁡ ( v λ) | | 2. \min_{{\Gamma}^{-}}|H(v_{\lambda})|\geq\frac{{\alpha}^{3}}{24}{||H(v_{\lambda})||}_{2}=\frac{\delta^{12}}{{10}^{6}\cdot 24}{||H(v_{\lambda})||}_{2}. |  |

By Corollary 13 we get

 | min Γ − ⁡ | H ⁡ ( v λ) | ≥ δ 12 10 6 ⋅ 24 ​ 2 ​ κ:= κ ′. \min_{{\Gamma}^{-}}|H(v_{\lambda})|\geq\frac{\delta^{12}}{{10}^{6}\cdot 24\sqrt{2}}\kappa:=\kappa^{\prime}. |  |

Hence

 | min Γ − ⁡ | λ 1 + r ​ f λ | ≥ κ ′ 4 − 4 ​ β. \min_{{\Gamma}^{-}}|\lambda_{1}+rf_{\lambda}|\geq\frac{\kappa^{\prime}}{4}-4{\beta}. |  |

Moreover, on Γ − \Gamma^{-}

 | | 1 + r ​ g λ | = − β ​ g λ ≤ 4 ​ β. |1+rg_{\lambda}|=-{\beta}g_{\lambda}\leq 4{\beta}. |  |

At last, r | Γ − ≥ 1 5 r|{\Gamma}^{-}\geq\dfrac{1}{5}. Hence

 | S ≥ κ ′ 80 ​ β − 1 5. S\geq\frac{\kappa^{\prime}}{80{\beta}}-\frac{1}{5}. |  |

Denote by π ​ Γ − \pi{\Gamma}^{-} the projection of Γ − {\Gamma}^{-} to r = 0 r=0 along the r r –axis; π Γ − ⊂ { − g λ − 1 ≤ δ − 1 + β } \pi{\Gamma}^{-}\subset\{-g^{-1}_{\lambda}\leq\delta^{-1}+{\beta}\}. We estimate the maximal slope of Γ − {\Gamma}^{-}. It is equal to

 | s = max π ​ Γ − ⁡ | ( 1 g λ) ′ | ≤ 6 min π ​ Γ − ⁡ | g λ | 2 ≤ 7 ​ δ − 2. s=\displaystyle\max_{\pi{\Gamma}^{-}}\left|{\left(\frac{1}{g_{\lambda}}\right)}^{\prime}\right|\leq\frac{6}{\min_{\pi{\Gamma}^{-}}{|g_{\lambda}|}^{2}}\leq 7\delta^{-2}. |  |

The inequality S > s S>s follows from the definition of β {\beta} in Lemma 12.

We now prove that no δ \delta –tame limit cycle that surrounds zero can cross Π β \Pi_{\beta}. On the contrary, let a cycle γ {\gamma} contain a point q ∈ Π β q\in\Pi_{\beta}. As γ {\gamma} surrounds 0 0, it must enter and quit Π β \Pi_{\beta}. The connected component Π q \Pi^{q} of Π β \Pi_{\beta} that contains q q is bounded by an arc γ β, q {\gamma}_{{\beta},q} of the curve ( 34) and by the part of ∂ B ⁡ ( λ, δ) \partial B(\lambda,\delta). As S > s S>s, the cycle can enter Π q \Pi^{q} through γ β, q {\gamma}_{{\beta},q} (in positive or negative time) but cannot quit Π q \Pi^{q} through γ β, q {\gamma}_{{\beta},q}. Hence, it quits Π q \Pi^{q} through ∂ B ⁡ ( λ, δ) \partial B(\lambda,\delta). This contradicts to the assumption that γ {\gamma} is δ \delta –tame and proves Lemma 12.

## 5. Acknowledgment

We are grateful to Alexey Fishkin who read several versions of the manuscript and made many fruitful comments.

## 6. The appendix

In this appendix we provide the values of the α {\alpha} ’s, β {\beta} ’s and γ {\gamma} ’s of Lemma 10.

We shall compute the Poincaré map P λ P_{\lambda} associated to the differential equation ( 14) in complex polar coordinates ( w, θ) (w,{\theta}). Let P λ: { θ = 0 } → { θ = 0 } P_{\lambda}:\{{\theta}=0\}\to\{{\theta}=0\} be the Poincaré map defined by the flow of system ( 14); i.e. P λ P_{\lambda} is the 2 ​ π 2\pi –time Poincaré map that brings an initial value of any solution r ⁡ ( θ, x) r({\theta},x) of system ( 14) with initial condition r ⁡ ( 0, x) = x r(0,x)=x on the half–axis { θ = 0 } \{{\theta}=0\} to the value of the same solution at θ = 2 ​ π {\theta}=2\pi, whenever defined. We know that the limit cycles surrounding the origin of system ( 1) correspond to real isolated zeros of the displacement function P λ ​ ( x) − x P_{\lambda}(x)-x.

The power series expansion for the displacement function P λ ​ ( x) − x P_{\lambda}(x)-x associated to a quadratic system ( 1) in a neighborhood of the origin is found in the following classical way. The right hand side of equation ( 14) may be decomposed in a power series in r r with the θ \theta -dependent coefficients:

(35) |  | d ​ w d ​ θ = ∑ i = 1 ∞ R i ​ ( θ) ​ w i, \frac{dw}{d{\theta}}=\sum_{i=1}^{\infty}R_{i}({\theta})w^{i}\,, |  |

where R 1 = λ 1 R_{1}=\lambda_{1},

(36) |  | R i ​ ( θ) = ( − 1) i ​ [f λ ​ ( θ) − λ 1 ​ g λ ​ ( θ)] ​ g λ ​ ( θ) i − 2 for i = 2, 3, … R_{i}({\theta})=(-1)^{i}[f_{\lambda}({\theta})-\lambda_{1}g_{\lambda}({\theta})]g_{\lambda}({\theta})^{i-2}\quad\mbox{for}\quad i=2,3,\ldots |  |

The modification of the Bautin result in [18] implies that the coefficients of the displacement map

(37) |  | P λ ​ ( x) − x = ∑ j = 1 ∞ a j ​ ( λ) ​ x j, P_{\lambda}(x)-x=\sum_{j=1}^{\infty}a_{j}(\lambda)\,x^{j}, |  |

belong to the ideal generated by g j ​ ( λ), j = 1, …, 4 g_{j}(\lambda),j=1,...,4, where g j g_{j} are the same as in Theorem 1. For λ 1 = 0 \lambda_{1}=0, the coefficients a j ​ ( λ) a_{j}(\lambda) are polynomial.

We use the algorithm due to Bautin for computing explicitly P λ ​ ( x) P_{\lambda}(x) in powers of x x up to order 7 7, see also [2]. We do the computations for the case λ 1 = 0 \lambda_{1}=0; otherwise v 7 ​ ( θ, λ) v_{7}({\theta},\lambda), which is necessary for computing v 7 ​ ( 2 ​ π, λ) v_{7}(2\pi,\lambda) and consequently P λ ​ ( x) P_{\lambda}(x) in powers of x x up to order 7 7, would need more than thousand pages. For doing these computations we have used the algebraic manipulator mathematica.

We know that the series of ( 35) converges if w w is small enough, and that the solution w ⁡ ( θ) w({\theta}) of differential equation ( 35) satisfying the initial condition w ⁡ ( 0) = x w(0)=x can be expanded as

(38) |  | w ⁡ ( θ, λ) = ∑ i = 1 ∞ v i ​ ( θ, λ) ​ x i, w({\theta},\lambda)=\sum_{i=1}^{\infty}v_{i}({\theta},\lambda)x^{i}\,, |  |

where the v i ​ ( θ, λ) v_{i}({\theta},\lambda) ’s satisfy the conditions

(39) |  | v 1 ​ ( 0, λ) = 1 and v i ​ ( 0, λ) = 0 for i = 2, 3, …. v_{1}(0,\lambda)=1\quad\mbox{and}\quad v_{i}(0,\lambda)=0\quad\mbox{for}\quad i=2,3,\ldots\,. |  |

Substituting ( 38) in ( 35), taking λ 1 = 0 \lambda_{1}=0, and looking for the coefficients of the powers of x x, we obtain the equations for determining all the v i v_{i} ’s:

 | d ​ v 1 d ​ θ \displaystyle\frac{dv_{1}}{d{\theta}} | = \displaystyle= | 0, \displaystyle 0\,, |  |

 | d ​ v 2 d ​ θ \displaystyle\frac{dv_{2}}{d{\theta}} | = \displaystyle= | v 1 2 ​ R 2, \displaystyle v_{1}^{2}R_{2}\,, |  |

 | d ​ v 3 d ​ θ \displaystyle\frac{dv_{3}}{d{\theta}} | = \displaystyle= | 2 ​ v 1 ​ v 2 ​ R 2 + v 1 3 ​ R 3, \displaystyle 2v_{1}v_{2}R_{2}+v_{1}^{3}R_{3}\,, |  |

 | d ​ v 4 d ​ θ \displaystyle\frac{dv_{4}}{d{\theta}} | = \displaystyle= | ( 2 ​ v 1 ​ v 3 + v 2 2) ​ R 2 + 3 ​ v 1 2 ​ v 2 ​ R 3 + v 1 4 ​ R 4, \displaystyle(2v_{1}v_{3}+v_{2}^{2})R_{2}+3v_{1}^{2}v_{2}R_{3}+v_{1}^{4}R_{4}\,, |  |

 | d ​ v 5 d ​ θ \displaystyle\frac{dv_{5}}{d{\theta}} | = \displaystyle= | 2 ​ ( v 1 ​ v 4 + v 2 ​ v 3) ​ R 2 + 3 ​ v 1 ​ ( v 1 ​ v 3 + v 2 2) ​ R 3 + 4 ​ v 1 3 ​ v 2 ​ R 4 + v 1 5 ​ R 5, \displaystyle 2(v_{1}v_{4}+v_{2}v_{3})R_{2}+3v_{1}(v_{1}v_{3}+v_{2}^{2})R_{3}+4v_{1}^{3}v_{2}R_{4}+v_{1}^{5}R_{5}\,, |  |

 | d ​ v 6 d ​ θ \displaystyle\frac{dv_{6}}{d{\theta}} | = \displaystyle= | ( 2 ​ v 1 ​ v 5 + 2 ​ v 2 ​ v 4 + v 3 2) ​ R 2 + ( 3 ​ v 1 2 ​ v 4 + 6 ​ v 1 ​ v 2 ​ v 3 + v 2 3) ​ R 3 + \displaystyle(2v_{1}v_{5}+2v_{2}v_{4}+v_{3}^{2})R_{2}+(3v_{1}^{2}v_{4}+6v_{1}v_{2}v_{3}+v_{2}^{3})R_{3}+ |  |

 |  |  | 2 ​ v 1 2 ​ ( 2 ​ v 1 ​ v 3 + 3 ​ v 2 2) ​ R 4 + 5 ​ v 1 4 ​ v 2 ​ R 5 + v 1 5 ​ R 6, \displaystyle 2v_{1}^{2}(2v_{1}v_{3}+3v_{2}^{2})R_{4}+5v_{1}^{4}v_{2}R_{5}+v_{1}^{5}R_{6}\,, |  |

 | d ​ v 7 d ​ θ \displaystyle\frac{dv_{7}}{d{\theta}} | = \displaystyle= | 2 ​ ( v 1 ​ v 6 + v 2 ​ v 5 + v 3 ​ v 4) ​ R 2 + \displaystyle 2(v_{1}v_{6}+v_{2}v_{5}+v_{3}v_{4})R_{2}+ |  |

 |  |  | 3 ​ ( v 1 2 ​ v 5 + 2 ​ v 1 ​ v 2 ​ v 4 + v 1 ​ v 3 2 + v 2 2 ​ v 3) ​ R 3 + \displaystyle 3(v_{1}^{2}v_{5}+2v_{1}v_{2}v_{4}+v_{1}v_{3}^{2}+v_{2}^{2}v_{3})R_{3}+ |  |

 |  |  | 4 ​ v 1 ​ ( v 1 2 ​ v 4 + 3 ​ v 1 ​ v 2 ​ v 3 + v 2 3) ​ R 4 + \displaystyle 4v_{1}(v_{1}^{2}v_{4}+3v_{1}v_{2}v_{3}+v_{2}^{3})R_{4}+ |  |

 |  |  | 5 ​ v 1 3 ​ ( 2 ​ v 2 2 + v 1 ​ v 3) ​ R 5 + 6 ​ v 1 5 ​ v 2 ​ R 6 + v 1 7 ​ R 7. \displaystyle 5v_{1}^{3}(2v_{2}^{2}+v_{1}v_{3})R_{5}+6v_{1}^{5}v_{2}R_{6}+v_{1}^{7}R_{7}\,. |  |

All these differential equations are solved recursively computing an integral with respect to θ {\theta} and taking into account the initial conditions ( 39). Thus, we get that v 1 ​ ( θ, λ) = 1 v_{1}({\theta},\lambda)=1, and

 | v 2 ​ ( θ, λ) = 1 3 ​ ( − 3 ​ a 2 + 3 ​ b 2 + c 2) + a 2 ​ cos ⁡ θ − b 2 ​ cos ⁡ θ − 1 3 ​ c 2 ​ cos ⁡ ( 3 ​ θ) + a 1 ​ sin ⁡ θ + b 1 ​ sin ⁡ θ + 1 3 ​ c 1 ​ sin ⁡ ( 3 ​ θ), \begin{array}[]{ll}v_{2}({\theta},\lambda)=&\dfrac{1}{3}(-3a_{2}+3b_{2}+c_{2})+a_{2}\cos{\theta}-b_{2}\cos{\theta}-\dfrac{1}{3}c_{2}\cos(3{\theta})+\\ &a_{1}\sin{\theta}+b_{1}\sin{\theta}+\dfrac{1}{3}c_{1}\sin(3{\theta})\,,\end{array} |  |

here we denote A = a 1 + i ​ a 2 A=a_{1}+ia_{2}, B = b 1 + i ​ b 2 B=b_{1}+ib_{2} and C = c 1 + i ​ c 2 C=c_{1}+ic_{2}. The expressions for v i ​ ( θ, λ) v_{i}({\theta},\lambda) for i = 3, 4, 5, 6, 7 i=3,4,5,6,7 need approximately 1 / 2 1/2, 2 2, 7 7, 18 18 and 42 42 pages, respectively. Once we know v i ​ ( θ, λ) v_{i}({\theta},\lambda) for i = 3, 4, 5, 6, 7 i=3,4,5,6,7, evaluating v i ​ ( 2 ​ π, λ) v_{i}(2\pi,\lambda) we get the displacement function

(40) |  | P λ ​ ( x) = w ⁡ ( 2 ​ π, λ) = ∑ i = 1 ∞ v j ​ ( 2 ​ π, λ) ​ x j = ∑ j = 1 ∞ a j ​ ( λ) ​ x j, P_{\lambda}(x)=w(2\pi,\lambda)=\sum_{i=1}^{\infty}v_{j}(2\pi,\lambda)x^{j}=\sum_{j=1}^{\infty}a_{j}(\lambda)\,x^{j}\,, |  |

with the explicit formulas for the polynomials a j ​ ( λ), j = 1, …, 7. a_{j}(\lambda),j=1,...,7. After that we decompose these polynomials in the ideal with generators g j, j = 1, …, 4 g_{j},j=1,...,4. This is done with the use of the manipulator mathematica again. The results of these computations presented below imply Lemma 10. The coeficients of the decompositions mentioned above are the following:

 | α 0 = − 2 ​ π, β 0 = − 2 ​ π 3, β 1 = − 2 ​ π 9 ​ ( 9 ​ a 2 2 − 9 ​ b 2 ​ a 2 − 6 ​ c 2 ​ a 2 − 27 ​ π ​ b 1 ​ a 2 + 27 ​ b 2 2 + 21 ​ c 2 2 + 18 ​ b 1 2 + CLOSE OPEN 20 ​ c 1 2 + 6 ​ b 2 ​ c 2 − 27 ​ b 2 ​ π ​ a 1 − 9 ​ a 1 ​ b 1), γ 0 = − 5 ​ π 4, γ 1 = − π 72 ​ ( 300 ​ a 2 2 − 558 ​ b 2 ​ a 2 − 240 ​ c 2 ​ a 2 − 384 ​ π ​ b 1 ​ a 2 + 528 ​ b 2 2 + 204 ​ c 2 2 − CLOSE 36 ​ a 1 2 + 288 ​ b 1 2 + 188 ​ c 1 2 + 168 ​ b 2 ​ c 2 − 384 ​ b 2 ​ π ​ a 1 − 18 ​ a 1 ​ b 1 + OPEN 48 ​ a 1 ​ c 1 + 24 ​ b 1 ​ c 1), γ 2 = − π 1080 ​ ( 2160 ​ a 2 4 − 360 ​ b 2 ​ a 2 3 − 1296 ​ c 2 ​ a 2 3 − 25920 ​ π ​ b 1 ​ a 2 3 + CLOSE 17100 ​ b 2 2 ​ a 2 2 + 27864 ​ c 2 2 ​ a 2 2 + 21600 ​ π 2 ​ b 1 2 ​ a 2 2 + 10260 ​ b 1 2 ​ a 2 2 + 24648 ​ c 1 2 ​ a 2 2 + 7236 ​ b 2 ​ c 2 ​ a 2 2 − 25920 ​ b 2 ​ π ​ a 1 ​ a 2 2 − 8280 ​ a 1 ​ b 1 ​ a 2 2 + 34560 ​ b 2 ​ π ​ b 1 ​ a 2 2 + 17280 ​ c 2 ​ π ​ b 1 ​ a 2 2 − 4752 ​ a 1 ​ c 1 ​ a 2 2 − 1740 ​ b 1 ​ c 1 ​ a 2 2 − 34200 ​ b 2 3 ​ a 2 − 19824 ​ c 2 3 ​ a 2 − 34560 ​ π ​ b 1 3 ​ a 2 − 37368 ​ b 2 ​ c 2 2 ​ a 2 + 4680 ​ b 2 ​ a 1 2 ​ a 2 − 144 ​ c 2 ​ a 1 2 ​ a 2 − 33480 ​ b 2 ​ b 1 2 ​ a 2 − 9954 ​ c 2 ​ b 1 2 ​ a 2 + 17280 ​ π ​ a 1 ​ b 1 2 ​ a 2 − 38472 ​ b 2 ​ c 1 2 ​ a 2 − 20976 ​ c 2 ​ c 1 2 ​ a 2 − 38400 ​ π ​ b 1 ​ c 1 2 ​ a 2 − 22806 ​ b 2 2 ​ c 2 ​ a 2 + 34560 ​ b 2 2 ​ π ​ a 1 ​ a 2 + 17280 ​ b 2 ​ c 2 ​ π ​ a 1 ​ a 2 + 5040 ​ b 2 ​ a 1 ​ b 1 ​ a 2 + 8280 ​ c 2 ​ a 1 ​ b 1 ​ a 2 + 43200 ​ b 2 ​ π 2 ​ a 1 ​ b 1 ​ a 2 − 60480 ​ b 2 2 ​ π ​ b 1 ​ a 2 − 41280 ​ c 2 2 ​ π ​ b 1 ​ a 2 − 17280 ​ b 2 ​ c 2 ​ π ​ b 1 ​ a 2 − 7608 ​ b 2 ​ a 1 ​ c 1 ​ a 2 − 1440 ​ c 2 ​ a 1 ​ c 1 ​ a 2 − 14628 ​ b 2 ​ b 1 ​ c 1 ​ a 2 − 2112 ​ c 2 ​ b 1 ​ c 1 ​ a 2 + 36900 ​ b 2 4 + 13040 ​ c 2 4 + 14580 ​ b 1 4 + 11200 ​ c 1 4 + 16152 ​ b 2 ​ c 2 3 − 9720 ​ a 1 ​ b 1 3 + 2640 ​ a 1 ​ c 1 3 + 1320 ​ b 1 ​ c 1 3 + 70758 ​ b 2 2 ​ c 2 2 − 4140 ​ b 2 2 ​ a 1 2 + 648 ​ c 2 2 ​ a 1 2 + 2124 ​ b 2 ​ c 2 ​ a 1 2 + 21600 ​ b 2 2 ​ π 2 ​ a 1 2 + 50760 ​ b 2 2 ​ b 1 2 + 42498 ​ c 2 2 ​ b 1 2 − 1620 ​ a 1 2 ​ b 1 2 − 25596 ​ b 2 ​ c 2 ​ b 1 2 − 34560 ​ b 2 ​ π ​ a 1 ​ b 1 2 + 67074 ​ b 2 2 ​ c 1 2 + 24000 ​ c 2 2 ​ c 1 2 + 120 ​ a 1 2 ​ c 1 2 + 41670 ​ b 1 2 ​ c 1 2 + 15288 ​ b 2 ​ c 2 ​ c 1 2 − 38400 ​ b 2 ​ π ​ a 1 ​ c 1 2 − 17400 ​ a 1 ​ b 1 ​ c 1 2 + 30996 ​ b 2 3 ​ c 2 − 60480 ​ b 2 3 ​ π ​ a 1 − 41280 ​ b 2 ​ c 2 2 ​ π ​ a 1 − 17280 ​ b 2 2 ​ c 2 ​ π ​ a 1 + 1080 ​ a 1 3 ​ b 1 + 17280 ​ b 2 ​ π ​ a 1 2 ​ b 1 − 11880 ​ b 2 2 ​ a 1 ​ b 1 − 19080 ​ c 2 2 ​ a 1 ​ b 1 + 540 ​ b 2 ​ c 2 ​ a 1 ​ b 1 − 720 ​ a 1 3 ​ c 1 − 11220 ​ b 1 3 ​ c 1 + 3690 ​ a 1 ​ b 1 2 ​ c 1 + 1950 ​ b 2 2 ​ a 1 ​ c 1 + 2448 ​ c 2 2 ​ a 1 ​ c 1 + 1344 ​ b 2 ​ c 2 ​ a 1 ​ c 1 + 44028 ​ b 2 2 ​ b 1 ​ c 1 + 1224 ​ c 2 2 ​ b 1 ​ c 1 + 1500 ​ a 1 2 ​ b 1 ​ c 1 + OPEN 1368 ​ b 2 ​ c 2 ​ b 1 ​ c 1). \begin{array}[]{ll}{\alpha}_{0}=&-2\pi,\\ &\\ {\beta}_{0}=&-\dfrac{2\pi}{3},\\ &\\ {\beta}_{1}=&-\dfrac{2\pi}{9}(9a_{2}^{2}-9b_{2}a_{2}-6c_{2}a_{2}-27\pi b_{1}a_{2}+27b_{2}^{2}+21c_{2}^{2}+18b_{1}^{2}+\\ &\qquad 20c_{1}^{2}+6b_{2}c_{2}-27b_{2}\pi a_{1}-9a_{1}b_{1}),\\ &\\ {\gamma}_{0}=&-\dfrac{5\pi}{4},\\ &\\ {\gamma}_{1}=&-\dfrac{\pi}{72}(300a_{2}^{2}-558b_{2}a_{2}-240c_{2}a_{2}-384\pi b_{1}a_{2}+528b_{2}^{2}+204c_{2}^{2}-\\ &\quad\quad 36a_{1}^{2}+288b_{1}^{2}+188c_{1}^{2}+168b_{2}c_{2}-384b_{2}\pi a_{1}-18a_{1}b_{1}+\\ &\quad\quad 48a_{1}c_{1}+24b_{1}c_{1}),\\ &\\ {\gamma}_{2}=&-\dfrac{\pi}{1080}(2160a_{2}^{4}-360b_{2}a_{2}^{3}-1296c_{2}a_{2}^{3}-25920\pi b_{1}a_{2}^{3}+\\ &\qquad\quad 17100b_{2}^{2}a_{2}^{2}+27864c_{2}^{2}a_{2}^{2}+21600\pi^{2}b_{1}^{2}a_{2}^{2}+10260b_{1}^{2}a_{2}^{2}+\\ &\qquad\quad 24648c_{1}^{2}a_{2}^{2}+7236b_{2}c_{2}a_{2}^{2}-25920b_{2}\pi a_{1}a_{2}^{2}-8280a_{1}b_{1}a_{2}^{2}+\\ &\qquad\quad 34560b_{2}\pi b_{1}a_{2}^{2}+17280c_{2}\pi b_{1}a_{2}^{2}-4752a_{1}c_{1}a_{2}^{2}-\\ &\qquad\quad 1740b_{1}c_{1}a_{2}^{2}-34200b_{2}^{3}a_{2}-19824c_{2}^{3}a_{2}-34560\pi b_{1}^{3}a_{2}-\\ &\qquad\quad 37368b_{2}c_{2}^{2}a_{2}+4680b_{2}a_{1}^{2}a_{2}-144c_{2}a_{1}^{2}a_{2}-33480b_{2}b_{1}^{2}a_{2}-\\ &\qquad\quad 9954c_{2}b_{1}^{2}a_{2}+17280\pi a_{1}b_{1}^{2}a_{2}-38472b_{2}c_{1}^{2}a_{2}-\\ &\qquad\quad 20976c_{2}c_{1}^{2}a_{2}-38400\pi b_{1}c_{1}^{2}a_{2}-22806b_{2}^{2}c_{2}a_{2}+\\ &\qquad\quad 34560b_{2}^{2}\pi a_{1}a_{2}+17280b_{2}c_{2}\pi a_{1}a_{2}+5040b_{2}a_{1}b_{1}a_{2}+\\ &\qquad\quad 8280c_{2}a_{1}b_{1}a_{2}+43200b_{2}\pi^{2}a_{1}b_{1}a_{2}-60480b_{2}^{2}\pi b_{1}a_{2}-\\ &\qquad\quad 41280c_{2}^{2}\pi b_{1}a_{2}-17280b_{2}c_{2}\pi b_{1}a_{2}-7608b_{2}a_{1}c_{1}a_{2}-\\ &\qquad\quad 1440c_{2}a_{1}c_{1}a_{2}-14628b_{2}b_{1}c_{1}a_{2}-2112c_{2}b_{1}c_{1}a_{2}+36900b_{2}^{4}+\\ &\qquad\quad 13040c_{2}^{4}+14580b_{1}^{4}+11200c_{1}^{4}+16152b_{2}c_{2}^{3}-9720a_{1}b_{1}^{3}+\\ &\qquad\quad 2640a_{1}c_{1}^{3}+1320b_{1}c_{1}^{3}+70758b_{2}^{2}c_{2}^{2}-4140b_{2}^{2}a_{1}^{2}+648c_{2}^{2}a_{1}^{2}+\\ &\qquad\quad 2124b_{2}c_{2}a_{1}^{2}+21600b_{2}^{2}\pi^{2}a_{1}^{2}+50760b_{2}^{2}b_{1}^{2}+42498c_{2}^{2}b_{1}^{2}-\\ &\qquad\quad 1620a_{1}^{2}b_{1}^{2}-25596b_{2}c_{2}b_{1}^{2}-34560b_{2}\pi a_{1}b_{1}^{2}+67074b_{2}^{2}c_{1}^{2}+\\ &\qquad\quad 24000c_{2}^{2}c_{1}^{2}+120a_{1}^{2}c_{1}^{2}+41670b_{1}^{2}c_{1}^{2}+15288b_{2}c_{2}c_{1}^{2}-\\ &\qquad\quad 38400b_{2}\pi a_{1}c_{1}^{2}-17400a_{1}b_{1}c_{1}^{2}+30996b_{2}^{3}c_{2}-60480b_{2}^{3}\pi a_{1}-\\ &\qquad\quad 41280b_{2}c_{2}^{2}\pi a_{1}-17280b_{2}^{2}c_{2}\pi a_{1}+1080a_{1}^{3}b_{1}+17280b_{2}\pi a_{1}^{2}b_{1}-\\ &\qquad\quad 11880b_{2}^{2}a_{1}b_{1}-19080c_{2}^{2}a_{1}b_{1}+540b_{2}c_{2}a_{1}b_{1}-720a_{1}^{3}c_{1}-\\ &\qquad\quad 11220b_{1}^{3}c_{1}+3690a_{1}b_{1}^{2}c_{1}+1950b_{2}^{2}a_{1}c_{1}+2448c_{2}^{2}a_{1}c_{1}+\\ &\qquad\quad 1344b_{2}c_{2}a_{1}c_{1}+44028b_{2}^{2}b_{1}c_{1}+1224c_{2}^{2}b_{1}c_{1}+1500a_{1}^{2}b_{1}c_{1}+\\ &\qquad\quad 1368b_{2}c_{2}b_{1}c_{1}).\end{array} |  |

## References

- [1] N.N. Bautin, On the number of limit cycles which appear with the variation of the coefficients from an equilibrium position of focus or center type, Math. USSR-Sb. 100 (1954), 397–413.
- [2] C. Chicone and M. Jacobs, Bifurcation of limit cycles from quadratic isochrones, J. of Differential Equations 91 (1991), 268–326.
- [3] F. Dumortier, Ch. Rousseau Study of the cyclicity of some degenerate graphics inside quadratic systems, preprint 2008.
- [4] H. Dulac, Détermination et integration d’une certaine classe d’équations différentielle ayant par point singulier un centre, Bull. Sci. Math. Sér. (2) 32 (1908), 230–252.
- [5] J. Ecalle, Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac, Hermann, 1992.
- [6] D. Hilbert, Mathematische Problem (lecture), Second Internat. Congress Math. Paris, 1900, Nachr. Ges. Wiss. Göttingen Math.–Phys. Kl. 1900, pp 253–297.
- [7] Yu. Ilyashenko, Finiteness theorems for limit cycles, Translations of Math. Monographs 94, Amer. Math. Soc., 1991.
- [8] Yu. Ilyashenko, S. Yakovenko Counting real zeros of function satisfying linear differential equations, J. Differential Equations 126 (1996), 87–105.
- [9] Yu. Ilyashenko, Hilbert–type numbers for Abel equations, growth and zeros of holomorphic functions, Nonlinearity 13 (2000), 1337–1342.
- [10] Yu. Ilyashenko and A. Panov, Some upper estimates of the number of limit cycles of planar vector fields with applications to Liénard equations, Moscow Math. J. 1 (2001), 583–599.
- [11] W. Kapteyn, On the midpoints of integral curves of differential equations of the first degree, Nederl. Akad. Wetensch. Verslag. Afd. Natuurk. Konikl. Nederland (1911), 1446–1457 (Dutch).
- [12] W. Kapteyn, New investigations on the midpoints of integrals of differential equations of the first degree, Nederl. Akad. Wetensch. Verslag Afd. Natuurk. 20 (1912), 1354–1365; 21, 27–33 (Dutch).
- [13] J. Llibre and G. Rodríguez, Configurations of limit cycles and planar polynomial vector fields, J. of Differential Equations 198 (2004), 374–380.
- [14] Ye Yanquian, Theory of limit cycles, Transl. Math. Monographs, Vol. 66, Amer. Math. Soc., Providence, R.I., 1986.
- [15] Zhang Pingguang, Quadratic systems with two foci (in Chinese), Appl. Math. J. Chinese Univ 14A (1999), 247–253.
- [16] Zhang Pingguang, On the distribution and number of limit cycles for quadratic systems with two foci (in Chinese), Acta Math. Sinica 44 (2001), 37–44.
- [17] Zhang Pingguang, On the distribution and number of limit cycles for quadratic systems with two foci, Qualitative Theory of Dynamical Systems 3 (2002), 437–463.
- [18] H. Zoladek, Quadratic systems with center and their perturbations, J. Differential Equations 109 (1994), 223–273.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:yulij@math.cornell.edu
[2]: mailto:jllibre@mat.uab.cat
[3]: /html/0910.3442
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/0910.3443
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0910.3443
[9]: https://arxiv.org/pdf/0910.3443
[10]: /html/0910.3444
