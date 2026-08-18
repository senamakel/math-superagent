<!-- source: https://doi.org/10.4213/sm10206e | converted from HTML -->

A. V. Dukov, “Lower bound for the cyclicity of hyperbolic polycycles”, Sb. Math., 216:7 (2025), 902–947

Sbornik: Mathematics  |

[RUS][1] [ENG][2] | [3] [4] [5] --> [6] | [JOURNALS][7] [PEOPLE][8] [ORGANISATIONS][9] [CONFERENCES][10] [SEMINARS][11] [VIDEO LIBRARY][12] [PACKAGE AMSBIB][13] |  |

 | [General information][14] |

 | [Latest issue][15] |

 | [Forthcoming papers][16] |

 | [Archive][17] |

 | [Impact factor][18] |

 | [Guidelines for authors][19] |

 | [License agreement][20] |

 | [Submit a manuscript][21] |

 |

 | [Search papers][22] |

 | [Search references][23] |

 |

 | [RSS][24] |

 | [Latest issue][25] |

 | [Current issues][26] |

 | [Archive issues][27] |

 | [What is RSS][28] |

---

---

---

[image: Powered by MathJax] [29] [30]

 |

---

*Sbornik: Mathematics, 2025, [Volume 216][31], [Issue 7][32], Pages 902–947
DOI: [https://doi.org/10.4213/sm10206e][33] [33]*(Mi sm10206) | [34] |  | [35] |

---

Lower bound for the cyclicity of hyperbolic polycycles

[A. V. Dukov][36]**

****[Steklov Mathematical Institute of Russian Academy of Sciences, Moscow, Russia][37]

[English version PDF (898 kB)][38] HTML full-text [Russian version article][39]

**References:**

[PDF][40]

[HTML][41]

**DOI:**[https://doi.org/10.4213/sm10206e][33] [33]

**Abstract:**Consider a monodromic hyperbolic polycycle formed by $n$ saddles and $n$ separatrix connections. Let the product of the characteristic numbers of these saddles be equal to 1. It is shown that for any positive integer $n$, in a perturbation of this polycycle in a generic $(n+1)$ -parameter family at least $n+1$ limit cycles appear.
Bibliography: 26 titles.

**Keywords:**limit cycles, cyclicity, polycycles, multiple fixed points, bifurcations.

**Funding agency** | **Grant number ** |

[Foundation for the Advancement of Theoretical Physics and Mathematics BASIS][42] [43] |  |

The research was carried out with the support of the Foundation for the Development of Theoretical Physics and Mathematics “Basis”. |

**Received:**26.09.2024 and 14.10.2024

**Published**: 19.09.2025

**Bibliographic databases:**[44] [45] [46] [47]

**Document Type:**Article

**MSC:**Primary [37G15][48]; Secondary [37C15][49], [37G20][50]

**Language:**English

**Original paper language:**Russian

### &sect; 1. Introduction

Let $\mathcal{M}$ be an infinitely smooth two-dimensional orientable Riemannian manifold. We denote by $\operatorname{Vect}^{\infty}(\mathcal{M})$ the space of infinitely smooth vector fields on $\mathcal{M}$.

**Definition 1.**By a *hyperbolic polycycle*of a vector field we mean an arbitrary finite directed graph $\gamma$ embedded in $\mathcal{M}$ that satisfies the following requirements:

- $\bullet$ vertices of $\gamma$ are hyperbolic saddles of the field;
- $\bullet$ edges of $\gamma$ are separatrix connections of saddles; the orientation is given by time;
- $\bullet$ the graph $\gamma$ is Eulerian (there is a cycle that traverses every edge once).

Let the field $v_0 \!\in\! \operatorname{Vect}^\infty(\mathcal{M})$ contain a hyperbolic polycycle $\gamma$. Consider a $k$-parameter family $V=\{v_\delta\}$ perturbing $v_0$, $\delta\in B=(\mathbb{R}^k, 0)$.

**Definition 2.**The *Poincar&eacute; map*$\Delta(\delta,x)$ of a polycycle (including a perturbed one) is the monodromy map of an arbitrary transversal to the polycycle onto itself along the whole polycycle that corresponds to the vector field. A polycycle is said to be *monodromic*if the Poincar&eacute; map is defined for the unperturbed polycycle (Figure 1).

[image: GRAPHIC]

Zoom in Zoom out

**Figure 1.**An example of a monodromic hyperbolic polycycle with six vertices.

**Definition 3.**Corresponding to every limit cycle close to the polycycle $\gamma$ is a fixed point $x_0$ of the Poincar&eacute; map: $\Delta(\delta,x_0)=x_0$. By the *multiplicity of a limit cycle*one means the multiplicity of this fixed point (for more details, see &sect; 2.2), that is, the least integer $m$ such that

$$ \begin{equation*} \bigl(\Delta(\delta,x)-x \bigr)^{(m)}\big|_{x=x_0} \neq 0. \end{equation*} \notag $$

**Definition 4.**When a polycycle $\gamma$ of a vector field $v_0$ is destroyed we say that a *limit cycle*(of multiplicity $m$)*is born*in a family $V$ if there exists a sequence of values of the parameters $\{\delta_\alpha\}_{\alpha \in \mathbb{N}}$ that tends to zero (to which the field $v_0$ corresponds) and such that for each $\alpha$ the field $v_{\delta_\alpha}$ has a limit cycle $\operatorname{LC}(\delta_\alpha)$ (of multiplicity $m$), and the sequence of limit cycles $\operatorname{LC}(\delta_\alpha)$ tends to the polycycle $\gamma$ in the Hausdorff metric as $\delta_\alpha \to 0$.

**Definition 5.**Let the polycycle $\gamma$ of a field $v_0$ be perturbed in a finite-parameter family $V=\{v_\delta\}$, $\delta\in B=(\mathbb{R}^k, 0)$. Let $\mu$ be the minimum integer for which there exist neighbourhoods $U$ and $W$ such that $\gamma \subset U$, $0 \in W \subset B$, and for every $\delta \in W$ the field $v_\delta$ has at most $\mu$ limit cycles in $U$. Then the number $\mu$ is called the *cyclicity*of the polycycle $\gamma$ in the family $V$.

We stress that the definition of cyclicity takes into account not only the limit cycles born from the whole polycycle $\gamma$ but also tho ones born from smaller polycycles, that is, from the ones that are subgraphs of the polycycle $\gamma$ in the sense of Definition 1.

**Definition 6.**A property of points in a topological space is said to be *generic*if there exists a countable intersection of open dense subsets whose points possess this property.

We denote by $\operatorname{HC}(n,k)$ (from &lsquo;hyperbolic&rsquo; and &lsquo;cyclicity&rsquo;) the maximum cyclicity that a hyperbolic polycycle of $n$ separatrix connections perturbed in a generic $k$-parameter family can have.

The following bounds for the quantity $\operatorname{HC}(n,k)$ are currently available.

1. $n=1$. A separatrix loop (Figure 2). The only fully analyzed case. The equality $\operatorname{HC}(1,k)=k$ was first proved by Leontovich in her D.Sc. dissertation [16] in 1946. Subsequently, the result was re-proved by Russari [24] and Ilyashenko and Yakovenko [10].

[image: GRAPHIC]

Zoom in Zoom out

**Figure 2.**A separatrix loop.

2. $n=2$. There are three topologically distinct hyperbolic polycycles formed by two separatrix connections: a &lsquo;lune&rsquo;, a &lsquo;heart&rsquo; (Figure 3) and a &lsquo;figure-eight&rsquo; (Figure 4). Each of these polycycles was studied by different mathematicians: Cherkas [3], Rein [23], Murtada [19], Zhebran [12], Roitenberg [22] and this author [6]. As a result of their joint work, the equality $\operatorname{HC}(2,2)=2$ was obtained. The inequality $\operatorname{HC}(2,3) \leqslant 3$ was proved by Trifonov [25] (see examples after Theorem 1 below).

[image: GRAPHIC]

Zoom in Zoom out

**Figure 3.**A &lsquo;lune&rsquo; (a) and a &lsquo;heart&rsquo; (b) polycycles.

[image: GRAPHIC]

Zoom in Zoom out

**Figure 4.**A &lsquo;figure-eight&rsquo; polycycle.

3. $n=3$. In 1980 Reyn [23] considered a monodromic separatrix triangle and obtained the bound $\operatorname{HC}(3,3) \geqslant 3$, and in 1997 Trifonov [25] investigated all hyperbolic (and not only hyperbolic) polycycles formed by three connections and proved the equality $\operatorname{HC}(3,3)=3$.

4. $n=4$. At this step, the apparent law prescribing that $\operatorname{HC}(n,n)$ must be equal to $n$ is violated: Murtada [20] proved the bound $\operatorname{HC}(4,4) \geqslant 5$ for a monodromic separatrix square.

5. $n \geqslant 5$. In [7] this author considered a monodromic polycycle of $n$ saddles and proved the inequality $\operatorname{HC}(n,n) \geqslant n$ (the idea of the proof was due to Reyn [23]). Upper bounds for $\operatorname{HC}(n,k)$ can be found in the following papers: Murtada [21], Ilyashenko and Yakovenko [11], Kaloshin [13], Kaleda and Shchurov [14], but all of them feature exponential behaviour and are therefore unlikely to be sharp.

**Definition 7.**The *characteristic number*of a hyperbolic saddle is the modulus of the ratio of eigenvalues, where the negative eigenvalue is in the numerator.

Let the field $v_0$ contain a monodromic hyperbolic polycycle $\gamma_M$ ( $M$ is from &lsquo;monodromic&rsquo;) formed by $n$ (different) saddles $S_1, \dots, S_n$ and $n$ separatrix connections (see Figure 1). Among the polycycles considered above, these are a loop (see Figure 2), a &lsquo;lune&rsquo; (see Figure 3), and also a separatrix triangle and a square, mentioned in bounds 3 and 4. We denote the characteristic numbers of the saddles $S_1, \dots, S_n$ by $\lambda_1, \dots, \lambda_n$, respectively.

Our main result is the following theorem.

**Theorem 1.**Let $V$ be a generic $C^\infty$-smooth family perturbing a polycycle $\gamma_M$. Let $\lambda_1\dotsb\lambda_n=1$. Then an $(n+1)$-multiple limit cycle ( $n+1$ limit cycles) is born in the family $V$.

To describe the genericity conditions in this theorem, we need to define several objects.

**Definition 8.**Consider a subset $\mathcal{X}$ of some normed space. The set $\mathcal{X}$ is called a $C^r$-smooth $(r\geqslant 1)$*Banach submanifold of codimension *$k \geqslant 0$**if for each point $x\in \mathcal{X}$ there exist a neighbourhood $W$ in the ambient space and a $C^r$-smooth function $\mathbf{F}\colon W\to \mathbb{R}^k$ such that

- $\bullet$ $\mathbf{F}^{-1}(0)=\mathcal{X} \cap W$;
- $\bullet$ $d\mathbf{F}(y)$ is a surjection for each point $y \in \mathcal{X} \cap W$.

According to the following proposition, vector fields with a hyperbolic polycycle form a smooth Banach submanifold, which we denote by $\mathcal{X}$.

**Proposition 1**(Dukov [7], Proposition 1). Suppose that a vector field $v_0 \in \operatorname{Vect}^r(\mathcal{M})$, $r \geqslant 3$, on a $C^{r+1}$-smooth oriented manifold $\mathcal{M}$ has $n$ saddle connections $\operatorname{SC}_1,\dots,\operatorname{SC}_n$. Then the vector fields $\widetilde v \in \operatorname{Vect}^r(\mathcal{M})$ close to $v_0$, with saddle connections $\widetilde{\operatorname{SC}}_1, \dots, \widetilde{\operatorname{SC}}_n$ close to the connections $\operatorname{SC}_1,\dots,\operatorname{SC}_n$, form a $C^{r-1}$-smooth Banach submanifold $\mathcal{X}$ of codimension $n$ in the space $\operatorname{Vect}^r(\mathcal{M})$.

We denote by $\widetilde{\mathcal{X}} \subset \mathcal{X}$ the Banach submanifold of codimension $n+1$ formed by the fields for which the product of the characteristic numbers of the saddles of the polycycle is equal to 1.

**Proposition 2**(Cherkas [4]). The Poincar&eacute; map of the unperturbed polycycle $\gamma_M$ has the asymptotic behaviour $\Delta(x)=c x^{\lambda_1\dotsb\lambda_n}(1+o(1))$ as $x \to 0+$; here $\lambda_1,\dots,\lambda_n$ are the characteristic numbers of the saddles and $c>0$.

Thus, the *genericity conditions*are as follows:

- (1) the family $V$ must intersect the Banach submanifold $\widetilde{\mathcal X}$ transversally;
- (2) $c \neq 1$, where $c$ is the coefficient mentioned in Proposition 2;
- (3) $\widetilde{R}_n(\lambda_1,\dots,\lambda_n) \neq 0$.

Here $\widetilde{R}_n$ is a polynomial in the characteristic numbers that is not identically equal to zero. It can be expressed in terms of the resultant of some polynomial system (for more details, see &sect; 3.4).

**Corollary 1.**For any positive integer $n$,

$$ \begin{equation*} \operatorname{HC}(n,n+1) \geqslant n+1. \end{equation*} \notag $$

Let us show an application of Theorem 1 to the cases $n=1,2$.

**Example 1.**The simplest monodromic polycycle is the separatrix loop of a hyperbolic saddle (see Figure 2). Theorem 1 for a loop implies that if the characteristic number $\lambda_1$ is $1$, then at least two limit cycles are born under a perturbation of the loop in a generic two-parameter family. This is a classical theorem due to Andronov and Leontovich (see [1], Theorem 50).

**Example 2.**Consider a &lsquo;lune&rsquo; polycycle (see Figure 3). It follows from Theorem 1 that, if the product of the characteristic numbers $\lambda_1$ and $\lambda_2$ of the saddles is equal to $1$, then at least three limit cycles are born under a perturbation of the &lsquo;lune&rsquo; in a generic three-parameter family. This result transforms the inequality due to Trifonov [25] into the equality $\operatorname{HC}(2,3)=3$.

In the following cases Theorem 1 is not applicable.

**Example 3.**A &lsquo;heart&rsquo; polycycle (see Figure 3) is not monodromic. In [25] Trifonov proved that, when a &lsquo;heart&rsquo; is perturbed in a generic three-parameter family at most two limit cycles are born.

**Example 4.**A &lsquo;figure-eight&rsquo; polycycle (see Figure 4) is monodromic but, unlike a &lsquo;lune&rsquo;, it has only one saddle. In the same paper [25], Trifonov showed that when a &lsquo;figure-eight&rsquo; is perturbed, at most two limit cycles are born in a generic three-parameter family.

Thus, the requirements imposed on the polycycle in Theorem 1 cannot be relaxed.

Note that this paper is a continuation of the paper [5], devoted to estimates for the multiplicity of limit cycles born in a decomposition of a hyperbolic polycycle. In &sect; 2 the main definitions and necessary constructions are given. Almost all of them coincide with the definitions and constructions in [5]. In &sect; 3 Theorem 1 is proved. In &sect; 4 the most technically complicated auxiliary statements are collected. In &sect; 5 we reformulate Theorem 1 for functions on the line.

### &sect; 2. A sufficient condition for the creation of limit cycles

As noted above, this paper is a development of the results in [5]. Therefore, before we proceed to the proofs of the main theorems, we must recall the notation used there and also cite a number of statements from it that are needed in the present work.

Although Theorem 1 is formulated for a very specific polycycle (the monodromic polycycle $\gamma_M$), we formulate and prove all statements under the following more general assumptions.

- 1. $\gamma$ is an arbitrary hyperbolic polycycle formed by $n$ separatrice connections, and there can be fewer than $n$ saddles (as in a &lsquo;figure-eight&rsquo; polycycle).
- 2. The polycycle $\gamma$ is perturbed in the family $V=\{v_{\delta,\theta}\}_{\delta, \theta}$, $(\delta, \theta) \in B=B_\delta \times B_\theta=(\mathbb{R}^n, 0) \times B_\theta$, where, in contrast to Theorem 1, the additional parameter $\theta= (\theta_1,\dots,\theta_s)$ is multidimensional and ranges over some open subset $B_\theta \subset \mathbb{R}^s$ containing the point 0 (we assume that $v_{0,0}=v_0$).
- 3. There is only one genericity condition imposed on the family $V$: the family must intersect transversally the Banach submanifold $\mathcal{X}$ of codimension $n$ (see Proposition 1).

These generalizations do not affect Theorems 1 and 2 (the latter is formulated in &sect; 2.3 below). These minor generalizations do not complicate the proof and are useful for the further development of the theory presented here.

### 2.1. Saddle correspondence maps

We draw a $C^\infty$-smooth transversal to every separatrix connection of a polycycle $\gamma$ of a field $v_0$: for $i=1, \dots, n$ we denote the transversal to the connection of saddles $S_i$ and $S_{i+1}$ by $\Gamma_i$ (Figure 5, a). We also assume that for $i=1, \dots, n$ the transversal $\Gamma_i$ does not depend on the parameters $\delta$ and $\theta$ and for any values of the parameters $\delta$ and $\theta$ each $\Gamma_i$ remains transversal to the perturbed vector field $v_{\delta,\theta}$.

[image: GRAPHIC]

Zoom in Zoom out

**Figure 5.**An unperturbed polycycle (a) and a limit cycle born from it (b).

In the unperturbed field $v_0$, consider an arbitrary saddle $S_i$ and two adjacent transversals $\Gamma_{i-1}$ and $\Gamma_i$ (we assume that $\Gamma_0=\Gamma_n$). The point of intersection of the transversal $\Gamma_{i-1}$ and the incoming separatrix of $S_i$ is denoted by $s_i$ (from &lsquo;stable&rsquo;). The point of intersection of $\Gamma_i$ and the outgoing separatrix of the saddle $S_i$ is denoted by $u_i$ (from &lsquo;unstable&rsquo;). Since the separatrices of the unperturbed field $v_0$ do not open up, the points $u_{i-1}$ and $s_i$ on the transversal $\Gamma_{i-1}$ coincide for any $i=1, \dots, n$.

For $i=1, \dots, n$ the saddle $S_i$ has a unique hyperbolic sector bounded by parts of the transversals $\Gamma_{i-1}$ and $\Gamma_i$. We denote these parts by $\Gamma_{i-1}^-$ and $\Gamma_i^+$. Then for $i=1, \dots, n$ the *correspondence map*$\Delta_i\colon \Gamma_{i-1}^- \to \Gamma_i^+$ of the saddle $S_i$ is defined.

Now consider the perturbed field $v_{\delta, \theta}$. By analogy, for any saddle $S_i= S_i(\delta, \theta)$ we introduce the points $s_i(\delta, \theta)$ and $u_i(\delta, \theta)$, the semitransversals $\Gamma_{i-1}^-(\delta, \theta)$ and $\Gamma_i^+(\delta, \theta)$, and the correspondence map $\Delta_i(\delta, \theta, \cdot)\colon \Gamma_{i-1}^-(\delta, \theta) \to \Gamma_i^+(\delta, \theta)$. In this case, generally speaking, the points $s_i(\delta, \theta)$ and $u_{i-1}(\delta, \theta)$ on the transversal $\Gamma_{i-1}$ may not coincide, which means that the connection between the saddles $S_{i-1}(\delta, \theta)$ and $S_i(\delta, \theta)$ opens up.

Since the manifold $\mathcal{M}$ is Riemannian, any smooth curve can be parameterized by the natural parameter (thus choosing a chart on it): the difference of the coordinates of any two points in this chart is equal in the absolute value to the length of the curve segment between these two points. On the transversal $\Gamma_{i-1}$ we choose a natural parameter (chart) so that the point $s_i(\delta, \theta)$ has coordinate 0, and every point on the semi-transversal $\Gamma_{i-1}^-(\delta, \theta)$ has a positive coordinate. At the same time, on the transversal $\Gamma_i$ we choose a natural parameter (chart) so that the point $u_i(\delta, \theta)$ has coordinate 0, and every point on the semi-transversal $\Gamma_i^+(\delta, \theta)$ has a positive coordinate.

Thus, we have chosen two charts on every transversal $\Gamma_i$. We denote the coordinate of the point $u_i(\delta, \theta)$ in the chart corresponding to the semi-transversal $\Gamma_i^-(\delta, \theta)$ by $\delta_i$. We assume that the quantity $\delta_i$ is the $i$th component of the parameter $\delta$ of the family $V$. This assumption is possible because of genericity condition 3 (see the beginning of &sect; 2). Then the transition from the chart corresponding to the semi-transversal $\Gamma_i^+(\delta, \theta)$ to the chart corresponding to $\Gamma_i^-(\delta, \theta)$ is carried out by the map

$$ \begin{equation} x \mapsto \delta_i \pm x. \end{equation} \tag{1} $$

If in the unperturbed field $v_0$ the hyperbolic sectors under consideration of the saddles $S_i$ and $S_{i+1}$ lie on the same side of the common separatrix connection of these saddles, then there is a plus sign in formula (1) (Figure 6, a). and if these sides are different, then there is a minus sign (Figure 6, b).

[image: GRAPHIC]

Zoom in Zoom out

**Figure 6.**The hyperbolic sectors of the saddles $S_i$ and $S_{i+1}$, in which the correspondence maps $\Delta_i$ and $\Delta_{i+1}$ are introduced. These hyperbolic sectors can lie on the same side (a) or on different sides (b) of the separatrix connection.

In the above coordinates on $\Gamma_{i-1}^-(\delta, \theta)$ and $\Gamma_i^+(\delta, \theta)$, the map $\Delta_i(\delta, \theta, \cdot)$ takes the form $\Delta_i(\delta, \theta, \cdot)\colon (\mathbb{R}_{>0},0) \to (\mathbb{R}_{>0},0)$. This map is $C^\infty$-smooth both with respect to the argument $x$ and with respect to the parameters $\delta$ and $\theta$.

For $i=1, \dots, n$ consider the following map:

$$ \begin{equation} f_i(\delta, \theta, \cdot)\colon \Gamma_{i-1}^-(\delta, \theta) \to \Gamma_i, \qquad f_i(\delta, \theta, x)=\delta_i \pm \Delta_i(\delta, \theta, x). \end{equation} \tag{2} $$

This is the composition of the correspondence map $\Delta_i(\delta, \theta, \cdot)$ and the map (1). In addition, we denote by $\Delta(\delta, \theta, \cdot)\colon \Gamma_n^-(\delta, \theta) \to \Gamma_n$ the Poincar&eacute; map (see Definition 2) representable as the composition

$$ \begin{equation} \Delta(\delta, \theta, \cdot) =f_n(\delta, \theta, \cdot) \circ \dotsb \circ f_1(\delta, \theta, \cdot). \end{equation} \tag{3} $$

### 2.2. Equations for multiple limit cycles

For some value of the parameters $\delta$ and $\theta$ let the field $v_{\delta, \theta}$ have a limit cycle $\operatorname{LC}(\delta, \theta)$, born in the decomposition of an original polycycle $\gamma$ (see Figure 5, b). Let this cycle intersect the semitransversal $\Gamma_n^-(\delta, \theta)$ at a point with coordinate $x_0$. Then the Poincar&eacute; map has a fixed point, that is, the triple $(\delta, \theta, x_0)$ is a solution of the equation

$$ \begin{equation} \Delta(\delta, \theta, x)=x. \end{equation} \tag{4} $$

If the limit cycle has multiplicity $n+1$ or greater, then for $x=x_0$ the following equalities are also satisfied:

$$ \begin{equation} \Delta'(\delta, \theta, x)=1 \end{equation} \tag{5} $$

and

$$ \begin{equation} \Delta^{(l+1)}(\delta, \theta, x)=0, \qquad l=1, \dots, n-1. \end{equation} \tag{6} $$

Throughout the paper, by the derivatives $(\cdot)'$ and $(\cdot)^{(l)}$ we mean the ones with respect to the variable $x$. Consider the function

$$ \begin{equation} \mathcal{D}(\delta, \theta, x)=\log\Delta'(\delta, \theta, x) \end{equation} \tag{7} $$

and the following system of equations associated with it:

$$ \begin{equation} \mathcal{D}^{(l)}(\delta, \theta, x)=0, \qquad l=0, \dots, n-1. \end{equation} \tag{8} $$

Since the manifold $\mathcal{M}$ is orientable, the Poincar&eacute; map $\Delta(\delta, \theta, \cdot)$ is an orientation-preserving diffeomorphism. Therefore, its derivative is always positive, which allows us to apply the logarithm to the function $\Delta'$ in the definition of the function $\mathcal{D}$.

We note that the system of equations (5), (6) is equivalent to (8). This follows from the fact that the following relation holds in a small neighbourhood of any solution $x_0$:

$$ \begin{equation*} \mathcal{D}(\delta, \theta, x)=\log \Delta'(\delta, \theta, x) =\log \bigl(1+ o((x-x_0)^{n-1})\bigr) =o\bigl((x-x_0)^{n-1}\bigr) \end{equation*} \notag $$

as $x \to x_0$. Therefore, instead of studying multiple fixed points of the Poincar&eacute; map, we can study multiple roots of $\mathcal{D}$, which is what we will do.

We introduce the notation

$$ \begin{equation} F_i=f_i \circ \dotsb \circ f_0, \qquad f_0=\mathrm{id}, \quad i=0, \dots, n, \end{equation} \tag{9} $$

and

$$ \begin{equation} Z_i=\frac{F_{i-1}'}{F_{i-1}}, \qquad i=1,\dots,n, \end{equation} \tag{10} $$

where the functions $f_i$ are defined by (2). In particular, $F_0(\delta, \theta, x)=x$ and $Z_1(\delta, \theta, x)={1}/{x}$. Here and below the composition of two arbitrary functions $g(\delta, \theta, x)$ and $h(\delta, \theta, x)$ is understood as follows: $g \circ h(\delta, \theta, x)=g\bigl(\delta, \theta, h(\delta, \theta, x)\bigr)$. We denote such a composition by $g \circ h=g(h)$ for short.

In addition, we define the functions $\mu_{iq}(\delta,\theta,x)$ and their limit values $\mu_{iq}^0(\theta)$, $i=1,\dots,n$, $q \in \mathbb{N}$:

$$ \begin{equation} \mu_{iq}(\delta, \theta, x)=y^q\frac{d^q}{dy^q}\log |f_i'(y)| \bigg|_{y=F_{i-1}} \to \mu_{iq}^0(\theta) : =(-1)^{q-1}(q-1)!\,(\lambda_i(\theta)-1) \end{equation} \tag{11} $$

as $\delta, x \to 0$. Throughout the paper, by $\lambda_i(\theta)$ we mean the quantity $\lambda_i(\theta)=\lambda_i(0, \theta)$. The existence of the limit in (11) was proved in [5], Lemma 1.

It turns out that the derivatives of the function $\mathcal{D}$ can be written in a convenient form.

**Proposition 3**([5], Proposition 1). For each $l \in \mathbb{N}$ there exists a polynomial $P_{nl}(\mu_{iq}, z_i)$, $i=1, \dots, n$, $q=1, \dots, l$, with integer coefficients such that the $l$th derivative of the function $\mathcal{D}$ defined by (7) is of the form

$$ \begin{equation*} \mathcal{D}^{(l)}=P_{nl}\bigl(\mu_{iq}(\delta,\theta,x),Z_i(\delta,\theta,x)\bigr), \qquad i=1, \dots, n, \quad q=1, \dots, l, \end{equation*} \notag $$

where the functions $Z_i(\delta,\theta,x)$ and $\mu_{iq}(\delta,\theta,x)$ are given by formulae (10) and (11), respectively. The polynomial $P_{nl}(\mu_{iq}, z_i)$ is a homogeneous polynomial of degree $l$ in the variables $z_1, \dots, z_n$.

Now consider the polynomials $Q_{nl}$:

$$ \begin{equation} Q_{nl}(\lambda_1,\dots,\lambda_n, z_1, \dots, z_n)=P_{nl}(\mu_{iq}^0, z_i), \qquad i=1, \dots, n, \quad q=1, \dots, l. \end{equation} \tag{12} $$

There is a simple recurrence formula for the polynomials $Q_{nl}$, which we do not need in this paper (for more details, see [5], Proposition 3). Like the polynomial $P_{nl}$, $Q_{nl}$ is a homogeneous polynomial of degree $l$ in $z_1,\dots,z_n$. In what follows, we treat $P_{nl}$ and $Q_{nl}$ as functions on the projective space $\mathbb{R}P^{n-1}$, regarding the projective coordinates $(z_1 : \dotsb : z_n)$ of points in $\mathbb{R}P^{n-1}$ as the variables $z_1, \dots, z_n$.

### 2.3. A sufficient condition for the birth of a multiple cycle

In this section, we formulate the key assertion of the paper: a sufficient condition for the birth of multiple limit cycles for hyperbolic polycycles whose product of characteristic numbers is equal to 1.

Consider the map

$$ \begin{equation} \mathcal{Z}\colon (\delta, \theta, x) \mapsto \bigl(Z_1(\delta, \theta, x) : \dotsb : Z_n(\delta, \theta, x)\bigr) \end{equation} \tag{13} $$

with values in the space $\mathbb{R}P^{n-1}$, where $Z_1, \dots, Z_n$ are the functions defined by (10).

**Definition 9.**We say that a *pair *$(\widehat{z}, \widehat{\theta}) \in \mathbb{R}P^{n-1} \times B_\theta$*corresponds to a limit cycle of multiplicity *$m$**if there is a sequence of points $(\delta_k, \theta_k, x_k) \to (0, \widehat{\theta},0)$ in the space $B_\delta \times B_\theta \times (\mathbb{R}_{>0},0)$ such that for $k\in \mathbb{N}$ the field $v_{\delta_k, \theta_k}$ contains a limit cycle of multiplicity $m$ passing through a point with coordinate $x_k$ on the semitransversal $\Gamma_n^+(\delta_k, \theta_k)$, and the function $\mathcal{Z}$, defined by (13), tends to $\widehat{z}$ on this subsequence.

Since the projective space is compact, in the case of $B_\theta=({\mathbb R}^s,0)$ it follows that corresponding to every limit cycle born in the family $V$ from the polycycle $\gamma$ there is at least one pair $(\widehat{z},0)\in\mathbb{R}P^{n-1} \times B_\theta$.

**Proposition 4**([5], Proposition 4). Let an arbitrary hyperbolic polycycle formed by $n$ separatrix connections with characteristic numbers $\lambda=(\lambda_1,\dots,\lambda_n)$ be perturbed within a $C^\infty$-smooth family with base $B=B_\delta \times B_\theta=(\mathbb{R}^n, 0) \times (\mathbb{R}^s, 0)$. Let the pair $(\widehat{z},0)\in \mathbb{R}P^{n-1} \times B_\theta$ correspond to a limit cycle of multiplicity $n+1$ or more born in this family. Then the pair $(\lambda,\widehat{z})$ is a solution of the polynomial system

$$ \begin{equation} Q_{nl}(\lambda, z)=0, \qquad l=1, \dots, n-1, \end{equation} \tag{14} $$

where the polynomials $Q_{nl}$ are given by (12).

It follows from Proposition 4 that not every point $\widehat{z} \in \mathbb{R}P^{n-1}$ corresponds to some limit cycle of prescribed multiplicity. It turns out that not every solution of (14) corresponds to a limit cycle either.

For an arbitrary hyperbolic polycycle $\gamma$ formed by $n$ connectives, we denote by $U=U(\gamma)$ the set of points $z=(z_1: \dotsb: z_n) \in \mathbb{R}P^{n-1}$ such that for $i=1, \dots, n$ the component $z_i$ is not equal to zero and for $i=1, \dots, n-1$ the ratio ${z_{i+1}}/{z_i}$ has the sign equal to $\operatorname{sign}f_i'$, where the function $f_i$ is given by (2). It is easy to see that, depending on the polycycle $\gamma$, the set $U$ is one of the open simplices (orthants) bounded by coordinate hyperplanes in $\mathbb{R}P^{n-1}$.

*Only the pairs *$(\widehat z, \widehat \theta)$*, where *$\widehat z$*belongs to the closure of the simplex *$U$*, can correspond to limit cycles*. Indeed, from (10) we obtain the equality

$$ \begin{equation} Z_i=\frac{1}{F_{i-1}}\prod_{j=1}^{i-1}f_j'(F_j). \end{equation} \tag{15} $$

Since the limit cycle exists only for the values of $\delta$, $\theta$ and $x$ such that for each $i=1,\dots,n-1$ the inequality $F_i(\delta, \theta, x) > 0$ holds (for more details, see &sect; 2.4), the sign of the expression ${Z_{i+1}}/{Z_i}$ coincides with the sign of the function $f_i'$. Moreover, in &sect; 2.5 we prove that the set of values of the map $\mathcal{Z}$ coincides precisely with the simplex $U$.

Thus, depending on the signs of the functions $f_i'$, we obtain $2^{n-1}$ disjoint domains in the projective space $\mathbb{R}P^{n-1}$, whose union is open and dense (Figure 7) and which can play the role of a simplex $U$ for some polycycle. This is just the number of hyperbolic polycycles with pairwise distinct vertices up to a homeomorphism preserving the orientation of the phase space. This follows from the fact that the sign $\operatorname{sign}f_i'$ is determined by the position of the sectors of the saddles $S_i$ and $S_{i+1}$ with respect to their common connection (see &sect; 2.1). Consequently, the simplex $U$ is uniquely determined by the topology of the polycycle.

[image: GRAPHIC]

Zoom in Zoom out

**Figure 7.**The simplex $U$ in the projective plane $\mathbb{R}P^2$ shown as a sphere with identified diametrically opposite points.

In the case of a monodromic polycycle $\gamma_M$ the simplex $U(\gamma_M)$ is the first orthant of the space $\mathbb{R}P^{n-1}$, that is, it consists of the points $z=(z_1: \dotsb : z_n)$ such that $z_i z_j >0$ for all $i,j=1,\dots,n$.

It turns out that for a hyperbolic polycycle whose product of characteristic numbers is equal to 1 the converse of Proposition 4 holds.

**Theorem 2**(sufficient condition for the birth of a multiple cycle). Let the $C^\infty$-smooth generic $(n+1)$-parametric family $V$ perturb a hyperbolic polycycle $\gamma$ with characteristic numbers $\lambda_1, \dots, \lambda_n$, where $\lambda_1\dotsb\lambda_n=1$. Let the point $\widehat{z}$ belong to the simplex $U(\gamma)$ and be a non-degenerate solution to system (14).

Then there exists a $C^\infty$-smooth curve $\tau\colon (\mathbb{R}_{>0},0) \to B$ such that for each $x>0$ the Poincar&eacute; map $\Delta$ of the field $v_{\tau(x)}$ has a fixed point $x$ of multiplicity at least $n+1$.

**Remark 1.**The multiplicity of a fixed point $x$ can be infinite. In this case the periodic trajectory corresponding to the point need not be isolated, that is, it may not be a limit cycle. Moreover, in &sect; 3.1 we present a family $V$ and a point $\widehat{z}$ satisfying the conditions of Theorem 2, but such that the map $\Delta$ is equal to identity for some values of the parameters.

The genericity condition imposed in Theorem 2 on the family $V$ is unique, and it coincides with the first genericity condition for the family $V$ in Theorem 1. In particular, we assume that the family $V$ has a base $B= B_\delta \times B_\theta=(\mathbb{R}^n,0) \times (\mathbb{R}, 0)$ with an $n$-dimensional parameter $\delta$ and a one-dimensional additional parameter $\theta$, for which the following condition holds:

$$ \begin{equation} \frac{\partial \bigl(\lambda_1(\delta, \theta) \dotsb \lambda_n(\delta, \theta)\bigr)}{\partial \theta} \bigg|_{\delta, \theta=0} \neq 0. \end{equation} \tag{16} $$

Theorem 2 is proved in &sect; 2.5.

### 2.4. The substitution $\delta=\delta(F, \theta, x)$. Eliminating one of the parameters

The main difficulty in the proof of Theorem 2 is that in this theorem we must construct a curve $\tau$ in the parameter base $B$, while the conditions for nondegeneracy of the solution of (14) are defined on the projective space $\mathbb{R}P^{n-1}$. Our aim is to find a diffeomorphism connecting these two spaces. Then, using this diffeomorphism, we can transfer the system of equations (8) to the projective space $\mathbb{R}P^{n-1}$.

As such a diffeomorphism connecting both spaces, it is tempting to take the map $\mathcal{Z}$ defined by (13). Unfortunately, $\mathcal{Z}$ is not a diffeomorphism, for instance, because it is defined on some open subset of the $(n+s+1)$-dimensional space $B_\delta \times B_\theta \times (\mathbb{R}_{>0}, 0)$ and takes values in the $(n-1)$-dimensional space $\mathbb{R}P^{n-1}$. Nevertheless, this obstacle can be circumvented by changing the map $\mathcal{Z}$ slightly. In this section we describe the first step of the construction of the required diffeomorphism, which consists in restricting the map $\mathcal{Z}$ to the surface of fixed points of the Poincar&eacute; map.

Consider the functions $F_1(\delta, \theta, x), \dots, F_n(\delta, \theta, x)$ defined by (9). Generally speaking, these functions can take positive and negative values alike. However, if the triple $(\delta, \theta, x)$ corresponds to a vector field $v_{\delta, \theta}$ containing a limit cycle, then for each $i=1, \dots, n$ the value of the function $F_i$ at the point $(\delta, \theta, x)$ is positive. Indeed, if for some values of the variables $\delta$, $\theta$, $x$ and some index $i$ we had $F_i(\delta, \theta, x) \leqslant 0$, then the function $f_{i+1}$, whose domain is $(\mathbb{R}_{>0},0)$, could not be applied to the point $F_i(\delta, \theta, x)$. Geometrically, this would mean that the phase curve from the point $x$ on the semi-transversal $\Gamma_n^+(\delta, \theta)$ does not intersect the semi-transversal $\Gamma_{i+1}^- (\delta, \theta)$, but leaves the neighbourhood of the polycycle instead.

Therefore, we are interested only in triples $(\delta,\theta,x)$ that belong to the set $E_0=\bigcap_{i=1}^n F_i^{-1}(\mathbb{R}_{>0})$.

**Lemma 1.**The map

$$ \begin{equation} \mathbf{F}\colon (\delta, \theta, x) \mapsto \bigl(F_1(\delta, \theta, x), \dots, F_n(\delta, \theta, x), \theta, x\bigr), \end{equation} \tag{17} $$

where the functions $F_1, \dots, F_n$ are given by (9), is a diffeomorphism of the domains $E_0$ and $(\mathbb{R}_{>0}^n, 0) \times B_\theta \times (\mathbb{R}_{>0},0)$, and its Jacobian tends to 1 as $\delta, x \to 0$. Moreover, $\mathbf{F}$ tends to the origin on some sequence if and only if this sequence tends to the origin in $E_0$.

This lemma enables us to consider the new parameters $F_1, \dots, F_n$ of the family $V$ instead of $\delta_1, \dots, \delta_n$, that is, to make the substitution $(\mkern-1mu\delta,\theta\mkern-1mu, x\mkern-1mu)\!=\!\mathbf{F}^{-1}\mkern-1mu(\mkern-1muF_1, \dots, F_n, \theta\mkern-1mu, x\mkern-1mu)$.

**Corollary 2.**The set of solutions of equation (4) for (not necessarily multiple) fixed points of the Poincar&eacute; map is a nonempty $C^\infty$-smooth surface

$$ \begin{equation*} \mathcal{C}_{\mathrm{Fix}}=\{ (\delta,\theta,x)\mid \Delta(\delta,\theta,x)=x\} \end{equation*} \notag $$

of codimension 1 in the space $B \times (\mathbb{R}_{>0},0)$.

**Proof.**Since $\Delta=F_n$, it follows that, according to (4), the surface $\mathcal{C}_{\mathrm{Fix}}$ can be represented in the form $\mathcal{C}_{\mathrm{Fix}} =\mathbf{F}^{-1}(\{F_n=x\})$. It is smooth by Lemma 1. This completes the proof of the corollary.

Corollary 2 enables us to assume that a system of coordinates is fixed on the surface $\mathcal{C}_{\mathrm{Fix}}$, namely, the parameters $(F_1, \dots, F_{n-1})\in B_F= (\mathbb{R}_{>0}^{n-1}, 0)$, the parameter $\theta$, and the variable $x$. The restriction to the surface $\mathcal{C}_{\mathrm{Fix}}$ means that the parameter $F_n$ can be eliminated by replacing it by the variable $x$. More formally, instead of any function of the form $g(\delta, \theta, x)$, we can consider the function

$$ \begin{equation*} g(F, \theta, x)=g\bigl(\delta, \theta, x\bigr)\big|_{(\delta,\theta,x) =\mathbf{F}^{-1}(F_1, \dots, F_n, \theta, x)}\big|_{F_n=x}. \end{equation*} \notag $$

This change with the subsequent substitution $F_n=x$ will be denoted by $\delta=\delta(F, \theta, x)$, where $F=(F_1, \dots, F_{n-1})$. For example, the definition (10) of the functions $Z_i(\delta, \theta, x)$, $i=1, \dots, n$, involves the derivative $F_{i-1}'$, which loses its meaning when we go over to the new parameters. Therefore, we take the expression (15) as the definition of the function $Z_i(F, \theta, x)$.

The functions obtained by the substitution of $\delta=\delta(F, \theta, x)$ into the function $\mathcal{D}(\delta, \theta, x)$ defined by (7) and into its derivatives $\mathcal{D}^{(l)}(\delta, \theta, x)$, $l \in \mathbb{N}$, will be denoted by $\mathcal{D}(F, \theta, x)$ and $\mathcal{D}_l(F, \theta, x)$, respectively. In particular, from now on, instead of fixed points of the Poincar&eacute; map $\Delta(\delta, \theta, x)$, we study common zeros of the functions $\mathcal{D}(F, \theta, x)$ and $\mathcal{D}_l(F, \theta, x)$. We note that the functions $\mathcal{D}_l(F, \theta, x)$ are no longer derivatives of $\mathcal{D}(F, \theta, x)$ with respect to $x$. Nevertheless, it will be convenient to keep this name for them.

### 2.5. A blow-up. The proof of Theorem 2

According to &sect; 2.4, by $\mathcal{Z}(F, \theta, x)$ we denote the map $\mathcal{Z}$ defined by formula (13) after the change $\delta= \delta(F, \theta, x)$. Consider the following map:

$$ \begin{equation} \begin{gathered} \, \notag \widehat{\mathcal{Z}}\colon B_F \times B_\theta \times (\mathbb{R}_{>0}, 0) \to \mathbb{R}P^{n-1} \times B_\theta \times (\mathbb{R}_{>0}, 0), \\ \widehat{\mathcal{Z}}\colon (F, \theta, x) \mapsto \bigl(\mathcal{Z}(F, \theta, x), \theta, x \bigr). \end{gathered} \end{equation} \tag{18} $$

It turns out that this is a diffeomorphism onto some domain.

**Proposition 5.**There is an open set

$$ \begin{equation*} W \subset B_F \times B_\theta \times (\mathbb{R}_{>0}, 0), \end{equation*} \notag $$

with the following properties:

(1) $\{0\} \times B_\theta \times \{0\} \subset \overline{W}$;

(2) the map $\widehat{\mathcal{Z}}\big|_W$ is a diffeomorphism onto its image;

(3) for $z \in U$ and $\theta \in B_\theta$ any sequence of points in the space $U \times B_\theta \times (\mathbb{R}_{>0}, 0)$ that tends to the point $(z,\theta,0)$ lies in $\widehat{\mathcal{Z}}(W)$ starting from some element;

(4) any point $(z, \theta, x) \in \widehat{\mathcal{Z}}(W)$ has a unique preimage under the action of the map $\widehat{\mathcal{Z}}$;

(5) there is a continuous function $a\colon U \times B_\theta \to \mathbb{R} \setminus \{0\}$ such that the Jacobian of the map $\widehat{\mathcal{Z}}^{-1}\colon (z, \theta, x) \mapsto (F,\theta, x)$ inverse to $\widehat{\mathcal{Z}}\big|_W$ is equal to $a(z, \theta) F_1 \dotsb F_{n-1}(1+o(1))$ as $x \to 0$.

This proposition is proved in &sect; 4.8. The domain $\widehat{\mathcal{Z}}(W)$ is called a &lsquo;hat&rsquo;, and the set $U \times B_\theta \times \{0\}$ is called the &lsquo;base&rsquo; of this &lsquo;hat&rsquo;. The diagram in Figure 8 shows that the derivative $\mathcal{D}^{(l)}$ can be factorized into a composition of the maps $\widehat{\mathcal{Z}}$ and $P_{nl}$, the first of which is a diffeomorphism onto some domain $W$ on the surface $\mathcal{C}_{\mathrm{Fix}}$, identified with the space $B_F \times B_\theta \times (\mathbb{R}_{>0},0)$ (see Corollary 2). The bullet shows a solution to the polynomial system (14) which can be extended from the &lsquo;base&rsquo; $U \times B_\theta \times \{0\}$ to the &lsquo;hat&rsquo; $\widehat{\mathcal{Z}}(W)$.

[image: GRAPHIC]

Zoom in Zoom out

**Figure 8.**The diagram of the factorization of $\mathcal{D}^{(l)}$ into the composition of $\widehat{\mathcal{Z}}$ and $P_{nl}$. The bullet in the base of the &lsquo;hat&rsquo; indicates the solution of the polynomial system (14) which extends from the base $U \times B_\theta \times \{0\}$ to the &lsquo;hat&rsquo; $\widehat{\mathcal{Z}}(W)$.

**Corollary 3.**The set of values of the map $\mathcal{Z}(\delta, \theta, x)\big|_{\mathcal{Z}_{\mathrm{Fix}}}$ defined by (13) is the whole simplex $U$. In particular, corresponding to any pair $(z, \theta) \in \overline{U} \times B_\theta$ is a limit cycle (see Definition 9).

So far, we defined points in $\mathbb{R}P^{n-1}$ by projective coordinates $z=(z_1: \dotsb : z_n)$. But it is more convenient to perform calculations in standard charts on $\mathbb{R}P^{n-1}$. Namely, consider the chart $\{ z=(z_1 : \dotsb : z_n)\mid z_1 \neq 0 \}$ in $\mathbb{R}P^{n-1}$; we denote it below by $\{z_1 \neq 0 \}$. We denote coordinates in this chart by $u_i= {z_i}/{z_1}$, $i=2, \dots, n$. Note that for any hyperbolic polycycle $\gamma$ the simplex $U(\gamma)$ is fully contained in this chart. In the chart $\{ z_1 \neq 0 \}$ the map $\mathcal{Z}$ defined by (13) takes the form

$$ \begin{equation} u\colon (F, \theta, x) \mapsto \bigl(u_2(F, \theta, x), \dots, u_n(F, \theta, x) \bigr), \end{equation} \tag{19} $$

where $u_i(F, \theta, x)={Z_i(F,\theta,x)}/{Z_1(F,\theta,x)}$ for any $i=2, \dots, n$.

**Definition 10.**Let $g\colon B_F \times B_\theta \times (\mathbb{R}_{>0}, 0) \to \mathbb{R}$. Then we call the function ${g \circ \widehat{\mathcal{Z}}^{-1}}$ defined on the set $\widehat{\mathcal{Z}}(W)$ the *blow-up*of the function $g(F, \theta, x)$ and denote it by $g(u, \theta, x)$.

The meaning of the term is that we &lsquo;blow up&rsquo; the set $\{0\} \times B_\theta \times \{0\}$ contained in the boundary of the domain $W$ to a set $U \times B_\theta \times \{0\}$ contained in the boundary of the domain $\widehat{\mathcal{Z}}(W)$. Now, instead of investigating the behaviour of the function $g(F,\theta,x)$ as $F,x \to 0$, we can investigate the behaviour of the function $g$ as the parameters tend to an arbitrary separate point in $U \times B_\theta \times \{0\}$.

**Proposition 6.**The following blown-up functions can be extended $C^1$-smoothly with respect to the variables $u$ and $\theta$ from the &lsquo;hat&rsquo; $\widehat{\mathcal{Z}}(W)$ to the &lsquo;base&rsquo; $U \times B_\theta \times \{0\}$:

- &bull; $\frac{\mathcal{D}(u,\theta,x)}{\log x} \to \lambda_1(\theta)\dotsb\lambda_n(\theta)- 1$;
- &bull; $x^l \mathcal{D}_l(u, \theta, x) \to Q_{nl}(\lambda(\theta), 1, u_2,\dots,u_n)$, $l\in \mathbb{N}$;

as $x \to 0$, where the polynomials $Q_{nl}$ are given by the formula (12).

Let us describe the idea of the proof (a rigorous proof of Proposition 6 is given in &sect; 4.9). Indeed, according to Proposition 3, in the chart $\{z_1 \neq 0\}$, after blowing up, the functions $\mathcal{D}_l$ take the form

$$ \begin{equation} \begin{gathered} \, x^l\mathcal{D}_l(u,\theta,x)=P_{nl}\bigl(\mu_{iq}(u,\theta,x), 1, u_2, \dots, u_n)\bigr), \\ i=1,\dots,n,\quad l \in \mathbb{N},\quad q=1,\dots,l. \end{gathered} \end{equation} \tag{20} $$

According to (11), the function $\mu_{iq}(\delta, \theta, x)$ has a limit $\mu_{iq}^0(\theta)$ as $\delta, x \to 0$, and therefore the blown-up function $\mu_{iq}(u,\theta,x)$ has the same limit as $x \to 0$. From the definition (12) of the polynomials $Q_{nl}$ and the homogeneity of the polynomials $P_{nl}$ we obtain the second assertion.

The first assertion of Proposition 6 follows from the fact that on the level surface $\mathcal{Z}(\delta, \theta, x)=\mathrm{const} \in U$ the parameter $\delta$ is small in comparison to the variable $x$ (that is, the separatrix connections are weakly discontinuous), the Poincar&eacute; map $\Delta(\delta, \theta, x)$ takes the form

$$ \begin{equation*} \Delta(\delta, \theta,x)=c(\delta, \theta) x^{\lambda_1(\delta, \theta) \dotsb\lambda_n(\delta, \theta)}(1+o(1)), \end{equation*} \notag $$

and the function $\mathcal{D}=\log \Delta'$ has the asymptotic representation

$$ \begin{equation*} \mathcal{D}(\delta, \theta, x)= \bigl(\lambda_1(\delta, \theta) \dotsb\lambda_n(\delta, \theta)-1\bigr)\log x+O(1) \end{equation*} \notag $$

as $\delta, x \to 0$. For more details, see &sect; 4.9.

Now we can proceed directly to the proof of the sufficient condition for the birth of a multiple limit cycle.

**Proof**of Theorem 2. The matrix of the gradients of the maps ${\mathcal{D}(u,\theta,x)}/{\log x}$ and $x^l \mathcal{D}_l(u, \theta, x)$, $l=1,\dots, n-1$, with respect to the variables $\theta$ and $u$ on the set $U \times B_\theta \times \{0\}$ takes the following form according to Proposition 6:

$$ \begin{equation} \begin{pmatrix} \dfrac{\partial \bigl(\lambda_1(\theta)\dotsb\lambda_n(\theta)\bigr)}{\partial \theta} & 0 & \cdots & 0 \\ \dfrac{\partial Q_{n1}}{\partial \theta} & \dfrac{\partial Q_{n1}}{\partial u_2} & \cdots & \dfrac{\partial Q_{n1}}{\partial u_n} \\ \vdots & & & \vdots \\ \dfrac{\partial Q_{n,n-1}}{\partial \theta} & \dfrac{\partial Q_{n,n-1}}{\partial u_2} & \cdots & \dfrac{\partial Q_{n,n-1}}{\partial u_n} \end{pmatrix}. \end{equation} \tag{21} $$

If we remove the first row and first column, then we obtain the Jacobian matrix of the polynomial system (14). By assumption there exists a point $\widehat{z} \in U$ that is a nondegenerate solution of the polynomial system (14) for $\theta=0$. At the same time, according to (16) the expression in the upper left corner of (21) is not equal to zero for $\theta=0$. Therefore, the matrix (21) is nonsingular.

Therefore, by the implicit function theorem there exists a $C^1$-smooth curve $(u(x), \theta(x), x)$, $x \in (\mathbb{R}_{\geqslant, 0}, 0)$, on which the functions $\mathcal{D}(u, \theta, x)$ and $\mathcal{D}_l(u, \theta, x)$, $l=1, \dots, n-1$, are identically equal to zero (see Figure 8). We lift this curve to the original space $B \times (\mathbb{R}_{>0},0)$ by the diffeomorphisms $\mathbf{F}^{-1}$ and $\widehat{\mathcal{Z}}^{-1}$ defined by (17) and (18). The resulting curve $\bigl(\tau(x), x\bigr)$ lies fully in $\mathcal{C}_{\mathrm{Fix}}$ (see Corollary 2), and each point on the curve satisfies (8). Thus, the pair $(\widehat{z},0) \in U \times B_\theta$ corresponds to a limit cycle of multiplicity at least $n+1$.

Theorem 2 is proved modulo Lemma 1 and Propositions 5 and 6.

### &sect; 3. Proof of Theorem 1

Theorem 2 enables us to construct, given a point $\widehat{z} \in \mathbb{R}P^{n-1}$ with certain properties, a smooth curve in the parameter base which corresponds to fields with a multiple limit cycle (in the worst case, with a periodic trajectory of infinite multiplicity; see Remark 1). The only thing left to do in order to prove Theorem 1 is to produce the required point $\widehat{z}$ and prove that the resulting multiple limit cycle falls into precisely $n+1$ limit cycles. In &sect; 3.1 we present a point $\widehat{z}$ satisfying the polynomial system (14). In &sect; 3.2 we prove that this solution is nondegenerate. In &sect; 3.5 we prove Theorem 1 itself.

### 3.1. Multiple fixed points on the real line

Proposition 4 can also be generalized to functions on the real line. Namely, the existence of a solution of the polynomial system (14) follows from the existence of a multiple fixed point of the function. Let us formulate this rigorously.

Let $f_i(\delta, \cdot)\colon \mathbb{R}_{>0} \to \mathbb{R}$, $i=1, \dots, n$, be $C^r$-smooth functions on the positive half-axis, $r \geqslant 1$. We assume that the $f_i$ depend continuously on the parameter $\delta$ ranging over an arbitrary topological space $B$ with some distinguished point $0$. Let there exist positive numbers $\lambda_1, \dots, \lambda_n$ such that the following relations hold:

$$ \begin{equation} \lim_{\delta, x \to 0} f_i(\delta, x)=0 \end{equation} \tag{22} $$

and

$$ \begin{equation} \lim_{\delta, x \to 0} x^q \frac{\partial^q}{\partial x^q}\log|f_i'(x)|= (-1)^{q-1}(q-1)!\,(\lambda_i-1), \qquad q=1, \dots, r-1. \end{equation} \tag{23} $$

In other words, the functions $f_i$ behave like power-law functions with exponents $\lambda_i$.

By analogy with (9), (10) and (13) we introduce the notation

$$ \begin{equation} F_i=f_i \circ \dotsb \circ f_0, \qquad f_0=\mathrm{id}, \quad i=0, \dots, n, \end{equation} \tag{24} $$

$$ \begin{equation} Z_i=\frac{F_{i-1}'}{F_{i-1}}, \qquad i=1,\dots,n, \end{equation} \tag{25} $$

and

$$ \begin{equation} \mathcal{Z}\colon (\delta, x) \mapsto \bigl(Z_1(\delta, x) : \dotsb : Z_n(\delta, x)\bigr). \end{equation} \tag{26} $$

Consider the function

$$ \begin{equation*} \Delta(\delta, x)=f_n \circ \dotsb \circ f_1(\delta, x). \end{equation*} \notag $$

Then the following theorem holds.

**Theorem 3**(see [5], Theorem 4). Let $\mathcal{F}$ be the set of all pairs $(\delta, x)$ corresponding to the fixed points of the function $\Delta$ of multiplicity $2 < m \leqslant r+1$, where $r$ denotes the smoothness class of the functions $f_i$, $i=1,\dots,n$. Then any limit point ${z\in \mathbb{R}P^{n-1}}$ of the map $\mathcal{Z}\big|_{\mathcal{F}}$ as $\delta, x \to 0$ satisfies the system

$$ \begin{equation*} Q_{nl}(\lambda, z)=0, \qquad l=1, \dots, m-2, \end{equation*} \notag $$

where $\lambda=(\lambda_1,\dots,\lambda_n)$, and the polynomials $Q_{nl}$ are given by (12).

**Proposition 7.**Let $\lambda_1, \dots, \lambda_n$ be arbitrary positive numbers, where $\lambda_1\dotsb \lambda_n=1$. Then $Q_{nl}(\lambda, \widehat{z})=0$ for any positive integer $l$, where

$$ \begin{equation} \widehat{z}=(1: \lambda_1: \lambda_1\lambda_2 : \dotsb : \lambda_1\dotsb \lambda_{n-1}). \end{equation} \tag{27} $$

**Proof.**Consider the family $\widetilde{V}$ of infinitely smooth functions

$$ \begin{equation} f_i(\delta,x)=\delta_i+x^{\lambda_i}, \qquad i=1, \dots, n, \end{equation} \tag{28} $$

depending on the parameter $\delta=(\delta_1,\dots,\delta_n) \in B=(\mathbb{R}^n,0)$. It is easy to see that these functions satisfy (22) and (23). Moreover, for $\delta=0$ the function $\Delta(\delta, x)$ is the identity:

$$ \begin{equation} \Delta(0, x)=f_n \circ \dotsb \circ f_1(0, x)=x^{\lambda_1 \dotsb \lambda_n}=x. \end{equation} \tag{29} $$

Thus, for $\delta=0$ each point $x>0$ has an infinite multiplicity. It follows from Theorem 3 that any limit point of the map $\mathcal{Z}$ defined by (26) is a solution of (14).

By the smoothness of the $f_i$ calculations can be performed for $\delta=0$. In particular, according to (24), we have

$$ \begin{equation} F_i(0, x)=x^{\lambda_1\dotsb\lambda_i}. \end{equation} \tag{30} $$

From (25) we find that

$$ \begin{equation} Z_i(0, x)=\frac{d}{dx} \log F_{i-1}(0, x)=\lambda_1 \dotsb b\lambda_{i-1} \frac{1}{x}, \end{equation} \tag{31} $$

from which we obtain the required point $\widehat{z}$.

This completes the proof of the proposition.

### 3.2. The nondegeneracy of the solution $\widehat{z}$

In fact, the results in our paper can also be formulated for functions on a line. For example, Propositions 5 and 6 are also valid for the family of functions $\widetilde V$ defined by (28). Let us use them to prove the nondegeneracy of the solution to the polynomial system found in Proposition 7. The transfer of our results to the case of functions on a line is discussed in detail in &sect; 5.

**Proposition 8.**Let $\lambda_1\dotsb\lambda_n=1$, and let the following inequalities hold:

$$ \begin{equation} \lambda_{i_1} \dotsb \lambda_{i_k} \neq 1 \quad \forall\, 1 \leqslant i_1 < \dotsb < i_k \leqslant n, \quad 1 \leqslant k < n. \end{equation} \tag{32} $$

Then the point $\widehat{z}$ defined by (27) is a nondegenerate solution to the polynomial system (14).

**Proof.**Consider the family of functions $\widetilde{V}$ defined by (28). By analogy with (7) we define the function $\mathcal{D}(\delta,x)=\log \Delta'(\delta,x)$.

The idea of the proof is to find the differentials with respect to the parameter $\delta$ of the derivatives $\mathcal{D}^{(l)}$, $l=0,\dots,n-1$, and to take the limit as $\delta,x \to 0$. We note that the Jacobian of the diffeomorphism $\mathbf{F}$ (see Lemma 1) tends to 1 as $\delta, x \to 0$, and the asymptotic behaviour of the Jacobian of the diffeomorphism $\widehat{\mathcal{Z}}^{-1}$ is described in property (5) in Proposition 5. Both diffeomorphisms preserve the variable $x$, and thus it suffices to calculate the Jacobian with respect to the parameters $\delta_1,\dots,\delta_{n-1}$, since the parameter $\delta_n$ is eliminated (see &sect; 2.4). Therefore, if we find the Jacobian of the map

$$ \begin{equation} (\delta, x) \to (x^l\mathcal{D}^{l}(\delta,x))_{l=1}^{n-1} \end{equation} \tag{33} $$

with respect to the parameters $\delta_1, \dots, \delta_{n-1}$, then, according to Proposition 6 on a smooth extension, we can also find the Jacobian of system (14) in the chart $\{z_1 \neq 0\}$.

First we prove by induction on $i=0,\dots,n$ that the functions $F_i(\delta,x)$ defined by (24) satisfy the relation

$$ \begin{equation} \lim_{\delta \to 0} \frac{d_\delta F_i}{F_i}=\sum_{j=1}^i \lambda_{j+1} \dotsb \lambda_i \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_i}}. \end{equation} \tag{34} $$

The base of induction is obvious: $\frac{d_\delta F_0}{F_0}=0$. Let the statement hold for $i-1$. Then we have

$$ \begin{equation*} \frac{d_\delta F_i}{F_i}=\frac{d_\delta f_i(F_{i-1})}{F_i} =\frac{d\delta_i+ f_i'(F_{i-1})d_\delta F_{i-1}}{F_i} =\frac{d\delta_i}{F_i}+\frac{Z_{i+1}}{Z_i}\frac{d_\delta F_{i-1}}{F_{i-1}}, \end{equation*} \notag $$

where for $i<n$ the function $Z_i$ is given by (25), and for $i=n$ we set

$$ \begin{equation*} Z_{n+1}=\frac{f_n'(F_{n-1})F_{n-1}'}{F_n}=\frac{F_n'}{F_n}=(\log \Delta)' \to \frac{1}{x} \quad\text{for } \delta \to 0. \end{equation*} \notag $$

From the induction assumption and equalities (30) and (31) we find that

$$ \begin{equation*} \lim_{\delta \to 0} \frac{d_\delta F_i}{F_i}=\frac{d\delta_i}{x^{\lambda_1\dotsb\lambda_i}}+ \lambda_i \lim_{\delta \to 0} \frac{dF_{i-1}}{F_{i-1}}= \frac{d\delta_i}{x^{\lambda_1\dotsb\lambda_i}} +\lambda_i\biggl(\sum_{j=1}^{i-1} \lambda_{j+1} \dotsb \lambda_{i-1}\frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j}}\biggr), \end{equation*} \notag $$

from which (34) follows. In particular, for $i=n$ we have

$$ \begin{equation} \lim_{\delta \to 0} \frac{d_\delta F_n}{F_n}=\sum_{j=1}^n \lambda_{j+1} \dotsb\lambda_n \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j}}. \end{equation} \tag{35} $$

By the definition of the functions $\mathcal{D}$ and $\Delta$ we have $\mathcal{D}=\log \Delta'=\log F_n'$. We obtain

$$ \begin{equation} d_\delta\mathcal{D}=d_\delta \log \Delta'=\frac{d_\delta F_n'}{F_n'}= \frac{1}{F_n'}\frac{\partial}{\partial x} \biggl(F_n \frac{d_\delta F_n}{F_n}\biggr) = \frac{d_\delta F_n}{F_n}+\frac{F_n}{F_n'}\frac{\partial}{\partial x} \biggl(\frac{d_\delta F_n}{F_n}\biggr). \end{equation} \tag{36} $$

In the third equality we transposed the operators of differentiation and taking the differential with respect to the parameter $\delta$. In addition, multiplying and dividing by the function $F_n$ we find the limit of the expression $\frac{\partial}{\partial x} \bigl(\frac{d_\delta F_n}{F_n}\bigr)$ as $\delta \to 0$. Transposing again the operators of differentiation and taking the limit with respect to the parameter $\delta$, and also using the (35) we obtain

$$ \begin{equation*} \begin{aligned} \, \lim_{\delta \to 0} \frac{\partial}{\partial x} \frac{d_\delta F_n}{F_n} &= \frac{\partial}{\partial x} \lim_{\delta \to 0}\frac{d_\delta F_n}{F_n} =\frac{\partial}{\partial x} \sum_{j=1}^n \lambda_{j+1} \dotsb \lambda_n \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j}} \\ &=\sum_{j=1}^n \lambda_{j+1} \dotsb \lambda_n (-\lambda_1 \dotsb \lambda_j)\frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j+1}}=- \sum_{j=1}^n \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j+1}}. \end{aligned} \end{equation*} \notag $$

At the last step we used the equality $\lambda_1\dotsb\lambda_n=1$.

We substitute the expression thus obtained and (35) into (36). We note that, according to (29), the expression ${F_n}/{F_n'}={\Delta}/{\Delta'}$ tends to $x$ as $\delta \to 0$. Therefore, after taking the limit, from (36) we obtain

$$ \begin{equation} \begin{aligned} \, \notag \lim_{\delta \to 0} d_\delta\mathcal{D} &=\sum_{j=1}^n \lambda_{j+1} \dotsb\lambda_n \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j}}-x \sum_{j=1}^n \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j+1}} \\ &=\sum_{j=1}^n (\lambda_{j+1} \dotsb\lambda_n-1) \frac{d\delta_j}{x^{\lambda_1\dotsb\lambda_j}}. \end{aligned} \end{equation} \tag{37} $$

Let us denote by $J(x)$ the Jacobian of (33) with respect to the parameters $\delta_1,\dots,\delta_{n-1}$ at the point $(0, x)$. To find this Jacobian it is convenient to apply the operator $x\, \frac{\partial}{\partial x}$ rather than $\frac{\partial}{\partial x}$ to the function in (37).

From (37) we obtain

$$ \begin{equation*} \lim_{\delta \to 0} \biggl(x\,\frac{\partial}{\partial x}\biggr)^l d_\delta \mathcal{D}= \sum_{j=1}^n (\lambda_{j+1}\dotsb\lambda_n-1)(-\lambda_1 \dotsb \lambda_j)^l\frac{d\delta_{j-1}}{x^{\lambda_1\dotsb\lambda_j}}. \end{equation*} \notag $$

This implies that

$$ \begin{equation} J(x)=\det \mathbf{W} \cdot \prod_{j=1}^{n-1} \frac{\lambda_{j+1}\dotsb\lambda_n-1}{x^{\lambda_1\dotsb\lambda_j}}, \end{equation} \tag{38} $$

where the matrix $\mathbf{W}$ has the form

$$ \begin{equation*} \mathbf{W}=\bigl((-\lambda_{j+1} \dotsb \lambda_n)^l \bigr)_{j,l=1}^{n-1}. \end{equation*} \notag $$

It is easy to see that this is a Vandermonde matrix, with the only difference that the $l$th row contains $l$th powers instead of ( $l-1$)st (see [15], Ch. 1, &sect; 6). Consequently, its determinant is equal to zero if and only if either $\lambda_j=0$ for some $j$ (which is impossible since $\lambda_1\dotsb\lambda_n = 1$ by assumption), or $-\lambda_{i+1} \dotsb \lambda_n=-\lambda_{j+1} \dotsb \lambda_n$ for some $i > j$, or, which is the same, $\lambda_{j+1} \dotsb \lambda_i=1$ (which is also impossible by (32)).

Thus, from (38) we obtain

$$ \begin{equation} J(x)=b \prod_{j=1}^{n-1} \frac{1}{x^{\lambda_1\dotsb\lambda_j}}, \end{equation} \tag{39} $$

where $b=b(\lambda_1,\dots,\lambda_n) \neq 0$.

It is obvious that after the blow-up the line $\delta=0$ in the space $B \times (\mathbb{R}_{>0},0)$ goes to the line $u=\widehat u$ in the space $U \times (\mathbb{R}_{>0},0)$, where $\widehat{u}$ denotes the coordinates of the point $\widehat{z}$ given by formula (27) in the chart $\{z_1 \neq 0\}$ (see &sect; 2.5). Let us express the Jacobian $J(u,x)$ at the point $(\widehat{u},x)$ with respect to the variable $u$ of the blown-up map

$$ \begin{equation*} (u, x) \to (x^l\mathcal{D}^{l}(u,x))_{l=1}^{n-1} \end{equation*} \notag $$

in terms of the Jacobian $J(x)$. By property (5) in Proposition 5 (also see the argument at the beginning of the current proof) we have

$$ \begin{equation*} J(\widehat{u},x)=J(x) a F_1(\widehat{u},x) \dotsb F_{n-1}(\widehat{u},x)\bigl(1+o(1)\bigr) \end{equation*} \notag $$

as $x \to 0$, where $a \neq 0$ and the $F_j(u,x)$ are the blown-up functions $F_j(\delta, x)$, $j=1,\dots, n-1$. From (30) and (39) we obtain

$$ \begin{equation*} J(\widehat{u},x)=a b \prod_{j=1}^{n-1} \frac{F_j(\widehat{u},x)}{x^{\lambda_1\dotsb\lambda_j}}\bigl(1+o(1)\bigr)=a b \bigl(1+o(1)\bigr) \neq 0 \end{equation*} \notag $$

as $x \to 0$. By Proposition 6 on smooth continuation, the Jacobian $J(\widehat{u},x)$ tends to the Jacobian of the polynomial system (14) written in the chart $\{z_1 \,{\neq}\, 0\}$. Therefore, the point $\widehat{z}$ is a nondegenerate solution of this polynomial system.

This completes the proof of Proposition 8.

### 3.3. A perturbation of multiple roots

Theorem 2 presents a sufficient condition for the birth of a multiple limit cycle. However, for $n+1$ limit cycles to be born in the family $V$ it is necessary to show that, under a perturbation in the family $V$, the multiple cycle decomposes into the required number of hyperbolic cycles.

For $C^\infty$-smooth functions this follows from classical results, like the Morin normal form [17], [2] or Malgrange&rsquo;s preparatory theorem [18]. And this is sufficient to prove Theorem 1. However, in &sect; 5 we reformulate the main results for finitely smooth functions on the line. And to this end we must prove the following proposition in the finitely smooth case.

**Proposition 9.**Let the $C^{n+1}$-smooth function $g(\beta,x)$, $\beta \in \mathbb{R}^m$ and $x \in \mathbb{R}$ satisfy the following conditions:

$$ \begin{equation*} \frac{\partial^k g}{\partial x^k}(0,0)=0, \quad k=0,\dots,n, \quad\textit{and} \quad \frac{\partial^{n+1} g}{\partial x^{n+1}}(0,0) \neq 0, \end{equation*} \notag $$

and let the differentials

$$ \begin{equation*} d_\beta\,\frac{\partial^k g}{\partial x^k}(0,0), \qquad k=0, \dots, n-1, \end{equation*} \notag $$

be linearly independent.

Then for any $\varepsilon > 0$ there exists $\widehat \beta \in (\mathbb{R}^m,0)$ such that the function $g(\widehat \beta,x)$ has precisely $n+1$ simple roots on the interval $(-\varepsilon, \varepsilon)$.

**Proof.**If $m > n$, that is, the dimension of the parameter base is greater than $n$, then we can consider a $C^{n+1}$-smooth subfamily with an $n$-dimensional base for which the condition on the linear independence of the differentials $d_\beta \frac{\partial^k g(\beta,0)}{\partial x^k}$ is also satisfied. Therefore, without loss of generality, we assume that $m=n$.

We expand the function $g(\beta,x)$ in the Taylor series:

$$ \begin{equation*} g(\beta,x)=\sum _{k=0,\dots,n} \alpha_k(\beta)x^k+\alpha_{n+1}(\beta)x^{n+1}+r(\beta,x), \end{equation*} \notag $$

where $r(\beta,x)=o(x^{n+1})$ as $y\to 0$ is a finitely smooth remainder. We divide the function $g(\beta,x)$ by $\alpha_{n+1}(\beta,x) \neq 0$. After the linear change $y(\beta,x)=x+ \frac{1}{n+1}\alpha_n(\beta)$ the $n$th term disappears:

$$ \begin{equation*} g(\beta,y)=\frac{1}{\alpha_{n+1}(\beta)}g(\beta,x(y))=\sum _{k=0,\dots,n-1} a_k(\beta)y^k + a_{n+1}(\beta)y^{n+1}+r(\beta,y). \end{equation*} \notag $$

We make the change of parameter $a_k=a_k(\beta)$. By the condition on the linear independence of differentials, this substitution is nondegenerate. In particular, it is invertible: $\beta= \beta(a)$. We obtain

$$ \begin{equation*} g(a,y)=\sum _{k=0,\dots,n-1} a_k y^k+y^{n+1}+r(a,y), \end{equation*} \notag $$

where $r(a,y)=r(\beta(a),y)=o(y^{n+1})$ as $y \to 0$.

We make another substitution: for $\nu \neq 0$ we set $y=\nu z$ and $a_k=b_k \nu ^{n-k+1}$, $k=0,\dots,n-1$. We denote this substitution by $a=a(b)$ and $y=y(z)$. Consider the following function:

$$ \begin{equation*} g(\nu,b,z)=\frac{1}{\nu^{n+1}} g(a(b),\nu z)=\sum _{k=0,\dots,n-1} b_k z^k+z^{n+1}+r(\nu, b,z), \end{equation*} \notag $$

where $r(\nu, b, z)=\frac{1}{\nu^{n+1}} r(a(b),\nu z)$.

Fix a value $\widehat b$ of the parameter $b=(b_0,\dots,b_{n-1})$ such that the polynomial $\widetilde{g}(\widehat b,z)=\sum _{k=0,\dots,n-1} \widehat b_k z^k+z^{n+1}$ has $n+1$ simple real zeros, namely, as the values of the parameters $\widehat b_k$ we can take the coefficients of the polynomial $\prod_{i=1}^{n+1} (z-z_i)$, where all zeros $z_1 < \dotsb < z_{n+1}$ are distinct and $\sum_{i=1}^{n+1} z_i=0$. We take $n+2$ points $\xi_i$, $i=0,\dots,n+1$, such that for $i=1,\dots,n+1$ the inequalities $\xi_{i-1} < z_i < \xi_i$ hold. Since all zeros of the polynomial are simple, the signs of the numbers $\widetilde g(b_0,\xi_i)$ alternate. Let

$$ \begin{equation*} M=\min_{i=0,\dots,n+1} |\widetilde g(b_0, \xi_i)|. \end{equation*} \notag $$

Fix an arbitrary number $\varepsilon > 0$. Let $\nu > 0$ be sufficiently small so that for each $i=0,\dots,n+1$ the point $\xi_i$ belongs to the interval $(-{\varepsilon}/{\nu}, {\varepsilon}/{\nu})$. Since $r(a,y)=o(y^{n+1})$ as $y \to 0$, for each $b$ the remainder $r(\nu, b, z)$ tends to zero as $\nu \to 0$ uniformly on the interval $[\xi_0, \xi_{n+1}]$. Therefore, there exists $\nu > 0$ such that $r(\nu,\widehat b,z) < M$ for any $z \in [\xi_0, \xi_{n+1}]$. Hence, for $i=0,\dots,n+1$ the number $g(\nu, \widehat b, \xi_i)$ has the same sign as $\widetilde g (\widehat b,\xi_i)$. Since the signs of the numbers $\widetilde g(\widehat b,\xi_i)$ alternate, the function $g(\nu, \widehat b, z)$ has $n+1$ zeros on the interval $(-{\varepsilon}/{\nu}, {\varepsilon}/{\nu})$.

Moreover, the derivative

$$ \begin{equation*} \frac{\partial r(\nu,\widehat b, z)}{\partial z}=\frac{1}{\nu^n} \frac{\partial r(a(\widehat b),y)}{\partial y}\bigg|_{y=\nu z} \end{equation*} \notag $$

also tends to zero as $\nu \to 0$. Consequently, the parameter $\nu$ can be taken sufficiently small so that all the zeros of $g(\nu, \widehat b, z)$ are simple, as are those of the polynomial $\widetilde g(\widehat b, z)$. Thus, we see that the original function $g(\beta,x)$ has $n+1$ simple zeros on the interval $(-\varepsilon, \varepsilon)$ for $\widehat \beta= \beta(a(\widehat b))$.

This completes the proof of Proposition 9.

### 3.4. The resultant. The verification of genericity conditions

In &sect;&sect; 3.2 and 3.3 we found a point $\widehat{z}$ which is a solution of (14) and proved that this solution is nondegenerate in the generic case. It follows from Theorem 2 that a limit cycle of multiplicity $n+1$ or greater is born in the family $V$. It remains to prove that its multiplicity is precisely $n+1$.

Recall that the *resultant*of a system of homogeneous polynomials over a field $K$ is a polynomial $R$ in the coefficients of the system such that $R$ is equal to zero if and only if the system has a nontrivial solution in the algebraic closure of $K$. Such a polynomial always exists for a system of $n$ homogeneous equations in $n$ variables. This is called the &lsquo;fundamental theorem of the theory of elimination of variables from polynomial ideals&rsquo; (see [8], &sect; 14.1).

In [5], Lemma 3, it was proved that the resultant $R_n(\lambda)$ of the system

$$ \begin{equation} Q_{nl}(\lambda, z)=0, \qquad l=1,\dots,n, \end{equation} \tag{40} $$

is not identically equal to zero. There are $n$ equations in (40), but the point $z$ ranges over the $(n-1)$-dimensional projective space $\mathbb{R}P^{n-1}$. Therefore, we say that system (40) is *redundant*, in contrast to the polynomial system (14). In this section we consider the $Q_{nl}(\lambda,z)$ as polynomials on the projective space $\mathbb{R}P^{n-1}$ with coefficients in the ring $\mathbb{Z}[\lambda_1,\dots,\lambda_n]$.

It follows from Proposition 7 that the resultant $R_n(\lambda)$ is divisible by the factor $\lambda_1\dotsb\lambda_n-1$. However, a stronger assertion can be proved.

**Proposition 10.**For any positive integer $n$ the resultant $R_n(\lambda)$ is divisible by the factor $\lambda_{i_1} \dotsb \lambda_{i_k}-1$ for any indices $1 \leqslant i_1 < \dotsb < i_k \leqslant n$, $1 \leqslant k \leqslant n$.

**Proof.**Let the set $\widetilde{\lambda}=\widetilde{\lambda}_1, \dots, \widetilde{\lambda}_n$ be such that $\widetilde{\lambda}_{i_1}\dotsb\widetilde{\lambda}_{i_k}=1$. Consider a point $\widetilde{z}=(\widetilde{z}_1 : \dotsb : \widetilde{z}_n)\in \mathbb{R}P^{n-1}$, where $\widetilde{z}_{i_j}=\widetilde{\lambda}_{i_1}\dotsb \widetilde{\lambda}_{i_{j-1}}$ for $j=1,\dots,k$ and $\widetilde{z}_i=0$ for the remaining indices $i$.

The polynomials $Q_{nl}$ have the following useful property (see [5], &sect; 2.5). For all positive integers $n$ and $l$ and each $j=1,\dots,n$ the following equality holds:

$$ \begin{equation*} Q_{nl}(\lambda, z) \big|_{z_j=0}=Q_{n-1,l}(\lambda', z'), \end{equation*} \notag $$

where $\lambda'=\lambda_1, \dots, \widehat{\lambda}_j, \dots, \lambda_n$ and $z'=z_1, \dots, \widehat{z}_j, \dots, z_n$. We have used the symbol $\widehat{\phantom{a}}$ to denote a variable missing from the sequence.

Therefore, substituting the pair $(\widetilde{\lambda},\widetilde{z})$ into the redundant system (40) yields

$$ \begin{equation*} Q_{nl}(\widetilde{\lambda}, \widetilde{z}) =Q_{kl}(\widetilde \lambda_{i_1},\dots,\widetilde \lambda_{i_k}, \widetilde z_{i_1}, \dots, \widetilde z_{i_k})=0 \end{equation*} \notag $$

for every $l=1, \dots, n$. The last equality holds by Proposition 7 for $n=k$. Therefore, the pair $(\widetilde{\lambda}, \widetilde{z})$ is a solution of the redundant system (40). Thus, the resultant $R_n(\lambda)$ is divisible by $\lambda_{i_1} \dotsb \lambda_{i_k}-1$. The proof is complete.

We extract from the resultant $R_n(\lambda)$ the factor $\lambda_1\dotsb\lambda_n-1$ in the maximum possible power:

$$ \begin{equation} R_n(\lambda)=(\lambda_1\dotsb \lambda_n-1)^d \widetilde{R}_n(\lambda), \end{equation} \tag{41} $$

where $d \geqslant 1$. The polynomial $\widetilde{R}_n$ is the same polynomial that occurs in the genericity conditions for Theorem 1. By Proposition 10 the inequality $\widetilde{R}_n \neq 0$ implies (32). Since the resultant $R_n(\lambda)$ is not identically equal to zero, the variables $\lambda_1,\dots,\lambda_n$ are independent (by assumption the polycycle is formed by precisely $n$ saddles), and the polynomial $\widetilde{R}_n$ is not divisible by $\lambda_1\dotsb \lambda_n-1$; then the polynomial $\widetilde{R}_n$ is not identically equal to zero and the condition $\widetilde{R}_n(\lambda) \neq 0$ is indeed a genericity condition.

### 3.5. An outline of the proof of Theorem 1

Now we can proceed to the proof of the main theorem.

**Proof**of Theorem 1. Since the polycycle $\gamma_M$ is monodromic, the simplex $U(\gamma_M) \subset \mathbb{R}P^{n-1}$ (see &sect; 2.3) consists of the points $z=(z_1 : \dotsb : z_n)$ such that all components $z_i$ have the same sign. In particular, the point $\widehat{z}$ defined by (27) belongs to the simplex $U(\gamma_M)$. By Propositions 8 and 10, by the genericity condition $\widetilde{R}_n \neq 0$ the point $\widehat{z}$ is a nondegenerate solution to the polynomial system (14). Consequently, by Theorem 2 there exists a $C^\infty$-smooth curve $\tau\colon (\mathbb{R}_{>0},0) \to B$ such that $\mathcal{D}^{(l)}(\tau(x), x)=0$ for each $l=0, \dots, n-1$ for any small $x>0$.

We claim that on this curve the derivative $\mathcal{D}^{(n)}(\delta, \theta, x)$ is not equal to zero for any small $x>0$. Assume that this is not the case. According to Proposition 3, the derivative of the Poincar&eacute; map $\mathcal{D}^{(l)}$ is expressed in terms of a polynomial $P_{nl}(\mu_{iq}, z_i)$, $i=1, \dots,n$, $q=1, \dots, l$, which is homogeneous in the variables $z_1, \dots, z_n$. Therefore, the polynomial system of equations

$$ \begin{equation} P_{nl}(\mu_{iq}, z_i)=0, \qquad l=1,\dots, n, \end{equation} \tag{42} $$

has a nontrivial solution $(z_1: \dotsb: z_n) \in \mathbb{R}P^{n-1}$ for some values of the variables $\mu_{iq}$ which are arbitrarily close to the $\mu_{iq}^0$, $i,q=1,\dots,n$ (see (11)). Regarding the $\mu_{iq}$ as the coefficients of system (42), we denote its resultant by $R_n(\mu_{iq})$, $i,q=1,\dots,n$. Therefore, $R_n(\mu_{iq})=0$ for some $\mu_{iq}$ close to $\mu_{iq}^0$, $i,q=1,\dots,n$. We claim that this fails to hold in a generic case.

According to the definition (12) of the polynomials $Q_{nl}$, system (42) turns to (40) for $\mu_{iq}=\mu_{iq}^0$. Hence the resultant $R_n(\mu_{iq}^0)$, $i,q=1,\dots, n$, is equal to the resultant $R_n(\lambda)$ of the redundant system (40). Since the polynomial $R_n(\lambda)$ is distinct from identical zero, the resultant $R_n(\mu_{iq})$ is not identically equal to zero.

To find the asymptotic behaviour of the resultant $R_n(\mu_{iq})$ on the curve $\tau(x)$ we need the following two lemmas.

**Lemma 2.**Let the assumptions of Theorem 2 be satisfied. Then after the blow-up the function $\mathcal{D}$ defined by (7) has the asymptotic behaviour

$$ \begin{equation*} \mathcal{D}(u, \theta, x)=\bigl(\lambda_1(u, \theta, x) \dotsb \lambda_n(u, \theta, x)-1 \bigr) \log x +\log c+o(1) \end{equation*} \notag $$

as $u \to \widehat{u}$ and $\theta, x \to 0$, where $\widehat{u}$ is the coordinate of the point $\widehat{z}$ defined by (27) in the chart $\{z_1\neq 0\}$; the constant $c$ is the same as in the genericity conditions for Theorem 1 (see &sect; 1).

**Lemma 3.**For all $i,q=1,\dots, n$ and each point $u$ in the simplex $U$ the blown-up functions $\mu_{iq}$ can be represented in the form

$$ \begin{equation*} \mu_{iq}(u, \theta, x)=(-1)^{q-1}(q-1)!\,\lambda_i(u, \theta, x)+o(1) \end{equation*} \notag $$

as $x\to 0$. The remainder $o(1)$ is H&ouml;lder continuous with respect to the variable $x$, and the H&ouml;lder coefficients depend continuously on $u$ and $\theta$.

These two lemmas are proved in &sect; 4.4 and &sect; 4.9, respectively.

Throughout the proof of Theorem 1 the restriction of an arbitrary function $g(\delta, \theta, x)$ to the curve $\tau(x)$ is denoted by $g(x)$. It follows from the system of equations (8) and Lemma 2 that after restricting to the curve $\tau(x)$ we obtain the asymptotic formula

$$ \begin{equation} \lambda_1(x)\dotsb\lambda_n(x) -1=- \frac{\log c}{\log x}\bigl(1+o(1)\bigr) \end{equation} \tag{43} $$

as $x \to 0$. At the same time, it follows from Lemma 3 that the resultant $R_n\bigl(\mu_{iq}(\delta, \theta, x)\bigr)$, as restricted to $\tau(x)$, can be represented in the form

$$ \begin{equation} R_n\bigl(\mu_{iq}(x)\bigr)=R_n\bigl(\lambda(x)\bigr)+\Phi(x), \end{equation} \tag{44} $$

where the function $\Phi(x)$ is H&ouml;lder continuous and tends to zero as $x \to 0$. Substituting the expressions (41) and (43) into (44) we obtain

$$ \begin{equation*} \begin{aligned} \, R_n\bigl(\mu_{iq}(x)\bigr) &=\bigl(\lambda_1(x)\dotsb\lambda_n(x)-1\bigr)^d \widetilde{R}_n\bigl(\lambda(x)\bigr)+\Phi(x) \\ &=\biggl(-\frac{\log c}{\log x}\biggr)^d \widetilde{R}_n(\lambda)\bigl(1+o(1)\bigr)+\Phi(x) \end{aligned} \end{equation*} \notag $$

as $x \to 0$. Since $c \neq 1$ and $\widetilde{R}_n(\lambda) \neq 0$ by the genericity conditions and since the function $\Phi(x)$ is H&ouml;lder continuous, we see that on the curve $\tau(x)$ the resultant

$$ \begin{equation*} R_n\bigl(\mu_{iq}(x)\bigr) =\biggl(-\frac{\log c}{\log x}\biggr)^d \widetilde{R}_n(\lambda)\bigl(1+o(1)\bigr) \end{equation*} \notag $$

is distinct from zero for sufficiently small $x>0$, which leads to a contradiction with the assumption.

Consequently, the curve $\tau(x)$ corresponds to limit cycles of multiplicity precisely ${n+1}$. We apply Proposition 9 to the function $\Delta(\delta, \theta, x)- x$. The linear independence of the differentials follows from the nondegeneracy of the curve $\tau$. From this proposition we see that at least $n+1$ limit cycles are born in the family $V$.

Theorem 1 is proved modulo Theorem 2 and Lemmas 2 and 3.

**Example 5.**According to [5], in the case $n=2$ the polynomial system (14) turns into the system of one equation

$$ \begin{equation*} Q_{2,1}(\lambda,z)=(\lambda_1-1)z_1+(\lambda_2-1)z_2=0. \end{equation*} \notag $$

If both characteristic numbers are different from 1, then this equation has a unique solution. It is easy to see that when $\lambda_1\lambda_2=1$, this solution is the point $\widehat{z}=(1 : \lambda_1)$. Thus, under the perturbation of a &lsquo;lune&rsquo; polycycle (Example 2), for which the simplex $U$ is the set $\{z \in \mathbb{R}P^1\mid z_1z_2 > 0\} \ni \widehat{z}$ (see &sect; 2.3), a 3-fold limit cycle is born. The simplex $U= \{z \in \mathbb{R}P^1\mid z_1z_2 < 0\}$ for a &lsquo;heart&rsquo; polycycle (Example 3) does not contain roots of the equation $Q_{2,1}(\lambda,z) =0$ for $\lambda_1\lambda_2=1$, and therefore when it is perturbed, a 3-fold limit cycle is not born in a generic three-parameter family. The simplex $U$ for a &lsquo;figure-eight&rsquo; polycycle (Example 4) is the same as for a &lsquo;lune&rsquo; polycycle, but now both characteristic numbers coincide ( $\lambda_1=\lambda_2= 1$). Therefore, for $\lambda_1\lambda_2=1$ the polynomial $Q_{2,1}(\lambda, z)$ is identically equal to zero, in particular, the polynomial system cannot have a nondegenerate solution. Therefore, the above arguments are not applicable to a &lsquo;figure-eight&rsquo; polycycle.

### &sect; 4. Proof of auxiliary statements

The previous sections contain only the main ideas of the proofs of Theorems 1 and 2. All technical issues were omitted. In this section we prove auxiliary statements, thereby completing the proofs of both theorems.

### 4.1. Normal forms

To describe the properties of the correspondence maps of hyperbolic saddles, we need some information from the theory of normal forms.

**Proposition 11**([10]). In the space $\operatorname{Vect}^\infty(\mathcal{M})$ there exists a class of fields $I_\infty$ of infinite codimension such that the following assertion holds for each field ${v_0 \in \operatorname{Vect}^\infty(\mathcal{M}) \setminus I_\infty}$ containing a hyperbolic saddle $S$.

Let a $C^\infty$-smooth family $V=\{v_\beta\}$, $\beta \in B_\beta=(\mathbb{R}^s, 0)$, perturb the field $v_0$. Then for each $r \in \mathbb{N}$ there exists a neighbourhood of the saddle and a $C^r$-smooth change of coordinates in it such that after this change and an appropriate choice of semitransversals, the correspondence map $\Delta_S(\beta, x)$ of the saddle $S$ can be represented in one of the following three forms.

- $\bullet$ For $\lambda \notin \mathbb{Q}$,

$$ \begin{equation} \Delta_S^{\lambda \notin \mathbb{Q}}(\beta, x)=x^{\lambda(\beta)}. \end{equation} \tag{45} $$

- $\bullet$ For $\lambda=1$,

$$ \begin{equation} \Delta_S^{\lambda=1}(\beta, x) =x+L_{\alpha_0}\sum_{i=0}^K \alpha_i x^{i+1} A_i(x, x L_{\alpha_0}, \beta) \end{equation} \tag{46} $$

for some $K$. Here $\alpha_i=\alpha_i(\beta)$, for $i=0, \dots, K$, $A_i$ is an analytic function, and ${A_i(0, 0, \beta) \equiv 1}$. The function $L_\varepsilon(x)$ (so-called &lsquo;Leontovich monomial&rsquo;) has the form

$$ \begin{equation} L_\varepsilon(x)= \begin{cases} \dfrac{x^{-\varepsilon}-1}{\varepsilon} & \textit{for } \varepsilon \neq 0, \\ - \log x & \textit{for } \varepsilon=0. \end{cases} \end{equation} \tag{47} $$

- $\bullet$ For $\lambda={m}/{k} \in \mathbb{Q}$,

$$ \begin{equation} \Delta_S^{\lambda \in \mathbb{Q}}(\beta, x)= \bigl(\Delta_S^{\lambda=1}(x^m)\bigr)^{{1}/{k}}. \end{equation} \tag{48} $$

This is probably the first case when the result is formulated in the above form. Equalities (45) and (48) obviously follow from the corresponding normal forms, which we do not present here (see [10]). The most complicated case (46) was considered in [10], Lemma 12.

**Lemma 4.**The Leontovich monomial (47) has the following properties:

(1) $x\,\frac{\partial L_{\pm\varepsilon}}{\partial x}=\mp \varepsilon L_{\pm\varepsilon}-1$;

(2) for $x > 0$ the Leontovich monomial is an analytic function, and its series in $\varepsilon$ has the form

$$ \begin{equation*} L_\varepsilon(x)=\sum_{m=1}^{+\infty} (-1)^m\frac{\log^m x}{m!} \varepsilon^{m-1}; \end{equation*} \notag $$

for each $x>0$ the radius of convergence is infinite;

(3) for all $\alpha > 0$ and $k \in \mathbb{N} \cup \{0\}$ $x^\alpha \,\frac{\partial^k L_\varepsilon(x)}{\partial \varepsilon^k} \to 0$ as $x \to 0+$ uniformly on the interval $[-\varepsilon_0, \varepsilon_0]$ for any $\varepsilon_0 < \alpha$.

**Proof.**Statement (1) follows directly from the definition (47) of the Leontovich monomial. Statement (2) is obtained from the expansion of the exponential in a series in powers of $\varepsilon$: $\varepsilon L_\varepsilon(x)=e^{-\varepsilon \log x}-1$. To prove (3), let us differentiate the above series. We have

$$ \begin{equation} \frac{\partial^k L_\varepsilon(x)}{\partial \varepsilon^k} =\log^k x \sum_{m=1}^{+\infty} (-1)^{m+k}\frac{\log^m x}{m!\,(m+k)} \varepsilon^{m-1}. \end{equation} \tag{49} $$

It is obvious that for all $\alpha >0$ and $k$ the function $x^\alpha \log^k x$ tends to zero as $x \to 0+$. Therefore, we claim that for all $\alpha > 0$ the series in (49), multiplied by $x^\alpha$, converges uniformly with respect to $x \in (0,1]$.

For any $m$ the function $x^\alpha \log^m x$ is equal to zero at $x=1$ and tends to zero as $x\to 0$. Consequently, the maximum of the modulus of this function is achieved at some intermediate point $x_m \in (0,1)$. Let us find this point:

$$ \begin{equation*} (x^\alpha \log ^m x)'=x^{\alpha-1}\log^{m-1}x(\alpha \log x+ m). \end{equation*} \notag $$

Hence $x_m=e^{-m/\alpha}$. Consequently, the uniform norm of the function $x^\alpha \log ^m x$ on the half-open interval $(0,1]$ is equal to

$$ \begin{equation*} |x_m^\alpha \log ^ m x_m|= \frac{1}{\alpha^m}\biggl(\frac{m}{e}\biggr)^m. \end{equation*} \notag $$

From Stirling&rsquo;s formula

$$ \begin{equation*} m!=\sqrt{2\pi m}\biggl(\frac{m}{e}\biggr)^m(1+o(1)) \end{equation*} \notag $$

(see [26], Supplement, paragraph (e)) we see that

$$ \begin{equation*} \frac{1}{m!} \, x^\alpha \log ^ m x=\frac{1}{\alpha^m} \, o(1) \quad\text{for } m \to+\infty \end{equation*} \notag $$

uniformly with respect to $x\in(0,1]$.

It follows from the relation thus obtained that there exists a positive constant $C$ (independent of $x$) such that the series in (49), multiplied by $x^\alpha$, is majorized by the series $C\sum_{m=1}^{+\infty} \frac{\varepsilon^{m-1}}{\alpha^m}$, independent of $x$, which implies the uniform convergence of the former series with radius of convergence $\alpha$. However, it follows from the representation (49) that the coefficients of the expansion of $x^\alpha \frac{\partial ^ k L_\varepsilon(x)}{\partial \varepsilon^k}$ in powers of $\varepsilon$ tend to zero as $x \to 0+$. Thus, the function itself tends to zero as $x \to 0+$ uniformly with respect to $\varepsilon$ ranging over any compact set in the convergence interval.

This completes the proof of Lemma 4.

It is inconvenient to consider all three representations (45), (46) and (48) for the correspondence map each time whet we prove a statement. The following proposition gives a universal representation for the saddle correspondence map.

**Proposition 12.**Under the assumptions of Proposition 11, for any value of the characteristic number $\lambda$ the correspondence map of the saddle $S$ has the form

$$ \begin{equation} \Delta_S(\beta, x)=x^{\lambda(\beta)}\bigl(1+x H(x, L_{\alpha_0}, L_{-\alpha_0}, \beta)\bigr), \end{equation} \tag{50} $$

where $H$ and $\lambda(\beta)$ are analytic functions, and $\lambda(0)=\lambda$.

**Proof.**In the case of an irrational characteristic number the statement is trivial. Consider the case $\lambda=1$. The case of an arbitrary rational characteristic number follows from (48).

We note that by isolating the zero term from the sum in formula (46) and taking into account that $A_0(x, xL_{\alpha_0},\beta)=1+o(1)$, we can write the expression (46) as follows:

$$ \begin{equation*} \Delta_S^{\lambda=1}(\beta, x)=x+\alpha_0 x L_{\alpha_0}+x^2 \widetilde{H}(x, L_{\alpha_0}, \beta) =x^{1-\alpha_0}+x^2\widetilde{H}(x, L_{\alpha_0}, \beta), \end{equation*} \notag $$

where $\widetilde{H}$ is an analytic function. Moving $x^{1-\alpha_0}$ out of brackets and taking into account that $x^{\alpha_0}=-\alpha_0 L_{-\alpha_0}+1$ we obtain representation (50), where ${\lambda(\beta)=1-\alpha_0(\beta)}$.

This completes the proof of the proposition.

### 4.2. The properties of the saddle correspondence map

Now we proceed to the description of the properties of the correspondence map $\Delta_S$. Let $\vartheta$ denote the class of functions of the form $H(x, L_{\alpha_0}, L_{-\alpha_0}, \beta)$, where $H$ is an arbitrary analytic function. In particular, it follows from Lemma 12 that $x^{-\lambda(\beta)} \Delta_S(\beta, x) \in 1+x\vartheta$.

**Lemma 5.**For any function $g(\beta, x) \in \vartheta$ the following relations hold:

$$ \begin{equation} x\, \frac{\partial g(\beta, x)}{\partial x} \in \vartheta \end{equation} \tag{51} $$

and

$$ \begin{equation} x^\alpha \, \frac{\partial^i g(\beta, x)}{\partial \beta^i} \to 0 \quad \forall\, \alpha > 0, \quad \forall\, i=(i_1, \dots, i_s) \end{equation} \tag{52} $$

as $x \to 0$. All limit procedures are uniform with respect to $\beta$ in an arbitrary compact subset of $B_\beta$.

**Proof.**The function $g$ belongs to the class $\vartheta$, and thus it can be represented in the form $g(\beta, x)= H(x, L_{\alpha_0}, L_{-\alpha_0}, \beta)$, where $H$ is an analytic function. Let us differentiate $g$ with respect to $x$. Then we have

$$ \begin{equation*} \frac{\partial g}{\partial x}=\frac{\partial H}{\partial x} +\frac{\partial H}{\partial L_{\alpha_0}} \frac{\partial L_{\alpha_0}}{\partial x}+\frac{\partial H}{\partial L_{-\alpha_0}} \frac{\partial L_{-\alpha_0}}{\partial x}. \end{equation*} \notag $$

From assertion (1) of Lemma 4 we obtain the property (51).

We denote by $\mathcal{A}$ the class of infinitely smooth functions $a(\beta,x)$ such that for all $\alpha > 0$ and $i=(i_1,\dots,i_s)$ we have $x^\alpha \frac{\partial^i a(\beta,x)}{\partial \beta^i} \to 0$ as $x \to 0$ uniformly with respect to $\beta$ ranging over an arbitrary compact subset of $B_\beta$. Clearly, the sum and product of functions in the class $\mathcal A$ belong to $\mathcal A$ again. Note that $g(\beta,x)=g(\beta,x)\cdot 1 \in \vartheta \cdot \mathcal{A}$. For any function of the form $g a \in \vartheta \cdot \mathcal A$ and $j=1,\dots,s$ we have

$$ \begin{equation*} \frac{\partial}{\partial \beta_j} \bigl(g(\beta,x)a(\beta,x)\bigr) =\biggl(\frac{\partial H}{\partial \beta_j}+\frac{\partial H}{\partial L_{\alpha_0}}\frac{\partial L_{\alpha_0}}{\partial \alpha_0} \frac{\partial \alpha_0}{\partial \beta_j}+\frac{\partial H}{\partial L_{-\alpha_0}} \frac{\partial L_{-\alpha_0}}{\partial \alpha_0} \frac{\partial \alpha_0}{\partial \beta_j}\biggr)a+g\,\frac{\partial a}{\partial \beta_j}. \end{equation*} \notag $$

By assertion (3) of Lemma 4 the Leontovich monomial and its derivative with respect to $\beta_j$ belong to the class $\mathcal{A}$. The function $a(\beta,x)$ and its derivative also belong to $\mathcal A$. All other functions in the expression obtained above belong to the class $\vartheta$. Thus, for any function of the form $g a \in \vartheta \cdot \mathcal A$ the derivative with respect to the parameter $\beta_j$, $j=1,\dots,s$, can be represented as a sum of functions in the class $\vartheta \cdot \mathcal A$. But for $\alpha > 0$ we have

$$ \begin{equation*} x^\alpha g(\beta,x)a(\beta,x)=\bigl( x^{{\alpha}/{2}} g(\beta,x)\bigr) \bigl(x^{{\alpha}/{2}} a(\beta,x)\bigr) \to 0 \quad\text{as } x \to 0 \end{equation*} \notag $$

uniformly on every compact set in $B_\beta$. The second factor tends to zero by the definition of the class $\mathcal A$, while the first tends to zero by assertion (3) of Lemma 4 and the uniform convergence of the Taylor series of the analytic function $H$ on any compact set in the disc of convergence. Thus, we have proved (52).

This completes the proof of Lemma 5.

The following well-known proposition is a simple consequence of Proposition 12 and Lemma 5. For the first derivatives of $C^3$-smooth vector fields its proof is given in [9], Lemma 6. Also see [25], Proposition 3.1, where the property (53) was proved.

**Proposition 13.**Let the field $v_0\in \operatorname{Vect}^\infty(\mathbb{R}^2)$, containing a hyperbolic saddle $S$, be perturbed by a $C^\infty$-smooth family $V=\{v_\beta\}$, $\beta \in B_\beta=(\mathbb{R}^s, 0)$. Then for any positive integer $r$ and $k\in \mathbb{N} \cup \{0\}$ the correspondence map $\Delta_S$ is $C^\infty$-smooth for $x>0$ and has the following properties:

$$ \begin{equation} \Delta_S^{(k)}(\beta, x)=\lambda(\beta)\bigl(\lambda(\beta)-1\bigr) \dotsb \bigl(\lambda(\beta)-k+1\bigr) c(\beta) x^{\lambda(\beta)-k}\bigl(1+x g_k(\beta,x)\bigr), \end{equation} \tag{53} $$

$$ \begin{equation} \frac{\partial^i\Delta_S^{(k)}(\beta, x)}{\partial \beta^i} =O(x^{\lambda(\beta)-k}\log^{|i|} x), \qquad i=(i_1, \dots, i_s), \end{equation} \tag{54} $$

as $x \to 0+$, where $\lambda(\beta)$ is the characteristic number of the saddle $S(\beta)$, $c(\beta)>0$ is a $C^r$-smooth function, and $x^\alpha g_k(\beta,x) \to 0$ as $x \to 0+$ for all $k \in \mathbb N \cup \{0\}$ and $\alpha>0$. All limits are uniform with respect to the parameter $\beta$ ranging over an arbitrary compact subset of $B_\beta$.

Here and below, for a multi-index $i=(i_1,\dots,i_s)$ the symbol $|i|$ means the sum $|i|=i_1+ \dotsb+i_s$. For any $r\in \mathbb{N}$ the function $c(\beta)$ is $C^r$-smooth in some neighbourhood of the origin, and these neighbourhoods decrease with the increasing smoothness of $r$. Therefore, we cannot claim that this function is $C^\infty$-smooth.

**Proof**of Proposition 13. The properties (53) and (54) of the map $\Delta_S$ follow directly from the Proposition 12 and Lemma 5. The infinite smoothness for $x > 0$ follows from the infinite smoothness of the monodromy map of the $C^\infty$-smooth field away from singular points.

In (50) the coefficient $c(\beta)$ is identically equal to 1, because in all previous statements the correspondence map $\Delta_S(\beta, x)$ was considered in a special $C^r$-smooth chart and on special semitransversals. Since in the original chart the transitions between $C^\infty$-smooth transversals along the original vector field are $C^\infty$-smooth diffeomorphisms $g$ and $h$ of the form $a(\beta)x(1+o(1))$, $a(\beta)>0$, it follows that the correspondence map $\widetilde{\Delta}_S=g \circ \Delta_S \circ h$ defined on other transversals also satisfies (53) and (54) for some other coefficient $\widetilde{c}(\beta)$.

This completes the proof of the proposition.

Consider the saddles $S_i$, $i=1, \dots, n$, which are vertices of the hyperbolic polycycle $\gamma$. Here we are mainly concerned with the logarithms of derivatives of their correspondence maps $\Delta_i(\delta,\theta,x)$ (see &sect; 2.1), rather than with the maps themselves. Thus, we need the following representation for the correspondence maps.

**Proposition 14.**Let the field $v_0\in \operatorname{Vect}^\infty(\mathbb{R}^2)$ containing a hyperbolic saddle $S$ be perturbed by a $C^\infty$-smooth family $V=\{v_\beta\}$, $\beta \in B_\beta=(\mathbb{R}^k, 0)$. Let $\Delta_S(\beta,x)$ be the correspondence map of the saddle $S=S(\beta)$ with characteristic number $\lambda(\beta)$. Then there exists a function $\Psi(\beta,x)$ such that

$$ \begin{equation} \Delta_S'(\beta,x)=x^{\lambda(\beta)-1}e^{\Psi(\beta,x)}. \end{equation} \tag{55} $$

The function $\Psi$ is continuous on the set $B_\beta \times (\mathbb{R}_{\geqslant 0},0)$, $C^\infty$-smooth on $B_\beta \times (\mathbb{R}_{>0},0)$, $\Psi(\beta,0)=\log \lambda(\beta)+\log c(\beta)$, and for every $\alpha \in [0,1)$ and every positive integer $q$ the function $\Psi$ satisfies the relations

$$ \begin{equation} x^q \, \frac{\partial^i\Psi^{(q)}(\beta,x)}{\partial \beta^i}=O(x^\alpha) \to 0 \quad \textit{as } x \to 0, \quad i=(i_1, \dots, i_s). \end{equation} \tag{56} $$

All limits are uniform with respect to $\beta$ ranging over an arbitrary compact subset of $B_\beta$.

**Proof.**From Proposition 12 and the property (51) we obtain

$$ \begin{equation*} \Delta_S'(\beta, x) \in x^{\lambda(\beta)-1}(\lambda(\beta)+x\vartheta). \end{equation*} \notag $$

Therefore, $\Psi(\beta,x) \in \log\lambda(\beta)+x\vartheta$. Then relation (56) follows from Lemma 5.

Going over to arbitrary $C^\infty$-smooth transversals is similar to what we considered in the proof of Proposition 13. In particular, it follows from (53) that

$$ \begin{equation*} \Psi(\beta,0)=\log \lambda(\beta)+\log c(\beta). \end{equation*} \notag $$

This completes the proof of the proposition.

### 4.3. Eliminating one of the parameters

**Proof**of Lemma 1. The map (17) can be viewed as a change of variables from $\delta_1, \dots, \delta_n$ to $F_1, \dots, F_n$. We note that this change can be done stepwise, where at the $i$th step the parameter $\delta_i$ is replaced by the new parameter $F_i$.

In other words, the map $\mathbf{F}$ is represented by the composition $\mathbf{F}= \mathbf{F}_n \circ \dotsb \circ \mathbf{F}_1$, where the maps $\mathbf{F}_i$ are defined as follows:

$$ \begin{equation*} \begin{gathered} \, \mathbf{F}_i\colon E_{i-1} \to (\mathbb{R}^i_{>0},0) \times \mathbb{R}^{n-i} \times B_\theta \times (\mathbb{R}_{>0},0), \\ \mathbf{F}_i\colon (F_1, \dots, F_{i-1}, \delta_i, \dots, \delta_n, \theta, x) \mapsto \bigl(F_1, \dots, F_{i-1}, F_i(\dots), \delta_{i+1}, \dots, \delta_n, \theta, x\bigr), \end{gathered} \end{equation*} \notag $$

where $F_i(\dots)=F_i(F_1, \dots, F_{i-1}, \delta_i, \dots, \delta_n, \theta, x)$. We denote by $E_0$ the domain $E_0=\bigcap_{j=1}^n F_j^{-1}(\mathbb{R}_{>0})$. The other domains $E_i$, $i>0$, are defined recursively: $E_i=\mathbf{F}_i(E_{i-1})$. We claim that the map $\mathbf{F}_i$ is a diffeomorphism for each $i=1, \dots, n$.

According to (2) and (9), for $i=1, \dots, n$ we have

$$ \begin{equation} F_i=\delta_i \pm \Delta_i(F_{i-1}). \end{equation} \tag{57} $$

For $k=i, \dots, n$ we find the partial derivatives of the map $F_i(\dots)=F_i(F_1, \dots, F_{i-1}, \delta_i, \dots, \delta_n, \theta, x)$:

$$ \begin{equation} \frac{\partial F_i}{\partial \delta_k}=\frac{\partial \delta_i}{\partial\delta_k} \pm \frac{\partial \Delta_i}{\partial \delta_k}(F_{i-1}) \to \begin{cases} 1, & i=k, \\ 0, & i < k, \end{cases} \end{equation} \tag{58} $$

as $F_{i-1} \to 0$. The last transition follows from Proposition 13.

Therefore, the Jacobian matrix of the map $\mathbf{F}_i(F_1, \dots, F_{i-1}, \delta_i, \dots, \delta_n, \theta, x)$ with respect to the variables $F_1, \dots, F_{i-1}, \delta_{i+1}, \dots, \delta_n$ is of the form

$$ \begin{equation*} i\text{th row} \begin{pmatrix} 1 & 0 & \cdots & & & \cdots & 0 \\ 0 & \ddots & \ddots & & & & \vdots \\ 0 & 0 & 1 & 0 & \cdots & & 0 \\ * & \cdots & * & 1+o(1) & o(1) & \cdots & o(1) \\ 0 & & \cdots & 0 & 1 & 0 & 0 \\ \vdots & & & & \ddots & \ddots & 0 \\ 0 & \cdots & & & \cdots & 0 & 1 \end{pmatrix}, \end{equation*} \notag $$

where asterisks denote the values of partial derivatives that are not important to us. This matrix differs from the lower triangular matrix with ones on the diagonal by an infinitesimal matrix. Therefore, the map $\mathbf{F}_i$ is a diffeomorphism onto its image for every $i=1,\dots,n$. Hence $\mathbf{F}$ is also a diffeomorphism onto its image.

It remains only to verify the surjectivity of the map $\mathbf{F}$. Using induction on $i=0, \dots, n$ we show that for any fixed values of the parameters $\delta_{i+1}, \dots, \delta_n$, the image of the map $\mathbf{F}_i \circ \dotsb \circ \mathbf{F}_1$ is the set

$$ \begin{equation*} (\mathbb{R}_{>0}^i, 0) \times \mathbb{R}^{n-i} \times B_\theta \times (\mathbb{R}_{>0},0). \end{equation*} \notag $$

In particular, for $i=n$ the required assertion follows from this fact.

The induction base $i=0$ (the identity map) is trivial. Let the assertion be proved for $i-1$. From relation (58) for $k=i$ we obtain that, when the parameter $\delta_i$ is variable and the other variables are fixed, the function $F_i$ takes arbitrarily small positive values.

The final statement of the lemma follows from (57) and Proposition 13.

This completes the proof of Lemma 1.

### 4.4. Identity connecting the variables $F$ and $u$

In this subsection we obtain an identity connecting the coordinates $F_1,\dots,F_{n-1}$ with the coordinates $u_2, \dots, u_n$ on the projective space $\mathbb{R}P^{n-1}$ (see &sect; 2.5).

According to Proposition 14, for $i=1, \dots, n$ there exist functions $\Psi_i(\delta,\theta,x)$ and $c_i(\delta, \theta)$ such that the function $f_i$ defined by (2) satisfies the relation

$$ \begin{equation} \log | f_i'(\delta,\theta,x)|=\log \Delta_i'(\delta,\theta,x) =(\lambda_i(\delta, \theta)-1)\log x+\Psi_i(\delta,\theta,x) \end{equation} \tag{59} $$

and $\Psi_i(\delta, \theta, 0)=\log \lambda_i(\delta, \theta)+\log c_i(\delta, \theta)$.

According to &sect; 2.4, after the change $\delta=\delta(F, \theta, x)$ the functions $\lambda_i(\delta, \theta)$ and $\Psi_i(\delta, \theta, F_{i-1})$, $i=1, \dots, n$, turn to smooth functions $\lambda_i(F, \theta, x)$ and $\Psi_i(F, \theta, x)$ defined on $B_F \times B_\theta \times (\mathbb{R}_{>0},0)$. We note that, although the characteristic numbers $\lambda_i(\delta, \theta)$, $i=1, \dots, n$, do not *a priori*depend on the variable $x$, such a dependence arises after the substitution $\delta=\delta(F, \theta, x)$.

**Lemma 6.**For $i=0, \dots, n-1$ the following identity holds:

$$ \begin{equation} F_i=\frac{x^{\lambda_1 \dotsb \lambda_i}}{|u_{i+1}|}\prod_{j=1}^i \bigl(|u_j|^{\lambda_j-1} e^{-\Psi_j}\bigr)^{-\lambda_{j+1} \dotsb \lambda_i}, \end{equation} \tag{60} $$

where $u_j=u_j(F, \theta, x)$, $\lambda_j=\lambda_j(F, \theta, x)$ and $\Psi_j=\Psi_j(F, \theta, x)$.

Formula (60) expresses the parameters $F_i$, $i=1, \dots, n-1$, in terms of the components $u_j$, $j=2, \dots, n$, of the map $\mathcal{Z}$ (see &sect; 2.5) and the quantity ${u_1(F,\theta,x) \equiv 1}$. In this way we formally &lsquo;invert&rsquo; the map $\widehat{\mathcal{Z}}$ defined by (18) in a certain sense. But this (provisional) &lsquo;inverse&rsquo; is not a genuine inverse of the map $\widehat{\mathcal{Z}}$, since the functions $\lambda_i$ and $\Psi_i$ on the right-hand side of (60) depend on the parameter $F$.

**Proof**of Lemma 6. For short, we omit the dependence on the variables $F, \theta$ and $ x$ throughout the proof.

We prove the relation (60) by induction on $i=0, \dots, n-1$.

*The base of induction*is obvious: according to (9), $F_0=x$.

*The induction step.*Let the statement be proved for $i-1$. According to (15) and the definition of the coordinates $u_i$, we obtain

$$ \begin{equation} \frac{u_{i+1}}{u_i}=\frac{Z_{i+1}}{Z_i}=\frac{f_i'(F_{i-1})F_{i-1}}{F_i} =\operatorname{sgn}f_i' \, \frac{F_{i-1}^{\lambda_i}}{F_i} e^{\Psi_i}. \end{equation} \tag{61} $$

In the last equality we used Proposition 14. Let us express the parameter $F_i$ from (61):

$$ \begin{equation} F_i=F_{i-1}^{\lambda_i} \frac{|u_i|}{|u_{i+1}|}e^{\Psi_i}. \end{equation} \tag{62} $$

By the induction assumption

$$ \begin{equation*} F_i=\biggl(\frac{x^{\lambda_1 \dotsb \lambda_{i-1}}}{|u_i|}\prod_{j=1}^{i-1} (|u_j|^{\lambda_j-1} e^{-\Psi_j})^{-\lambda_{j+1} \dotsb \lambda_{i-1}}\biggr)^{\lambda_i} \frac{|u_i|}{|u_{i+1}|}e^{\Psi_i}, \end{equation*} \notag $$

from which (60) follows.

This completes the proof of Lemma 6.

**Lemma 7.**The function $\mathcal{D}(F, \theta, x)$ defined by (7) satisfies the following identity:

$$ \begin{equation} \mathcal{D}=(\lambda_1 \dotsb \lambda_n-1) \log x -\sum_{j=1}^n \lambda_{j+1}\dotsb \lambda_n \bigl((\lambda_j-1) \log |u_j|-\Psi_j\bigr). \end{equation} \tag{63} $$

Here, as well as throughout the proof, the dependence $\lambda_i=\lambda_i(F, \theta, x)$ and $\Psi_i=\Psi_i(F, \theta, x)$ is omitted for brevity.

**Proof**of Lemma 7. According to the definition (3) of the Poincar&eacute; map and the representation (15) for the function $Z_n(F,\theta,x)$, we have

$$ \begin{equation*} \Delta'=\prod_{i=1}^n f_i'(F_{i-1})=f_n'(F_{n-1})F_{n-1}Z_n. \end{equation*} \notag $$

From (59) and the equality $u_n={Z_n}/{Z_1}=x Z_n$ (see &sect; 2.5) we obtain

$$ \begin{equation*} \Delta'=F_{n-1}^{\lambda_n}e^{\Psi_n}\frac{|u_n|}{x}. \end{equation*} \notag $$

From Lemma 6 we find that

$$ \begin{equation*} \Delta'=x^{\lambda_1 \dotsb \lambda_i-1}\prod_{j=1}^n (|u_j|^{\lambda_j-1} e^{-\Psi_j})^{-\lambda_{j+1} \dotsb \lambda_n}. \end{equation*} \notag $$

Since $\mathcal{D}=\log \Delta'$ by definition, we obtain the required equality after taking the logarithm.

This completes the proof of the lemma.

**Remark 2.**The proof of both identities, (60) and (63), is purely formal. In particular, these identities hold when the functions $F_i(\delta, \theta, x)$, $u_i(\delta, \theta, x)=x Z_i(\delta, \theta, x)$, $\lambda_i(\delta, \theta)$, $\Psi_i\bigl(\delta, \theta, F_{i-1}(\delta, \theta, x)\bigr)$ and $\mathcal{D}(\delta, \theta, x)$ defined on the space $B_\delta \times B_\theta \times (\mathbb{R}_{>0},0)$ are treated as the variables $F_i$, $u_i$, $\lambda_i$, $\Psi_i$ and $\mathcal{D}$, and in the case when these variables are understood to be the blown-up functions $F_i(u, \theta, x)$, $u_i$, $\lambda_i(u, \theta, x)$, $\Psi_i(u, \theta, x)$ and $\mathcal{D}(u, \theta, x)$ defined in $\widehat{\mathcal{Z}}(W)$ (see &sect; 2.5).

Running ahead slightly and assuming that Proposition 5 on the blow-up has already been proved, let us show how the asymptotic behaviour of the function $\mathcal{D}$ on the curve $\tau(x)$ follows from (63).

**Proof**of Lemma 2. Let us find the value of the linear combination of functions $\log |u_j|$, $j=2,\dots,n$, from formula (63) at the point

$$ \begin{equation*} \widehat{u}=(\widehat{u}_2, \dots, \widehat{u}_n)=(\lambda_1,\lambda_1\lambda_2, \dots, \lambda_1\dotsb \lambda_{n-1}). \end{equation*} \notag $$

Transposing the summation operators we obtain

$$ \begin{equation*} \begin{aligned} \, & \sum_{j=1}^n \lambda_{j+1}\dotsb \lambda_n (\lambda_j-1) \log |\widehat{u}_j| =\sum_{j=1}^n \lambda_{j+1}\dotsb \lambda_n (\lambda_j-1) \sum_{i=1}^{j-1} \log \lambda_i \\ &\qquad =\sum_{i=1}^n \log \lambda_i \sum_{j=i+1}^n \lambda_{j+1}\dotsb \lambda_n (\lambda_j-1)= \sum_{i=1}^n (\lambda_{i+1}\dotsb \lambda_n-1)\log \lambda_i \\ &\qquad =\sum_{i=1}^n \lambda_{i+1}\dotsb \lambda_n\log \lambda_i-\log (\lambda_1\dotsb\lambda_n)= \sum_{i=1}^n \lambda_{i+1}\dotsb \lambda_n\log \lambda_i. \end{aligned} \end{equation*} \notag $$

The last transition follows from the equality $\lambda_1\dotsb\lambda_n=1$. At the same time, according to Proposition 14, the relation $\Psi_i(\delta, \theta, 0)=\log \lambda_i(\delta, \theta)+\log c_i(\delta, \theta)$ holds for $i=1,\dots,n$. Consequently, the equality (63) can be rewritten as

$$ \begin{equation*} \begin{aligned} \, & \mathcal{D}(u, \theta, x)-\bigl(\lambda_1(u, \theta, x) \dotsb \lambda_n(u, \theta, x) - 1\bigr) \log x \\ &\qquad =\sum_{i=1}^n \bigl(-\lambda_{i+1}\dotsb \lambda_n\log \lambda_i+\lambda_{i+1} \dotsb \lambda_n (\log \lambda_i+\log c_i)\bigr)+o(1) \\ &\qquad=\sum_{i=1}^n\lambda_{i+1}\dotsb \lambda_n \log c_i+o(1)=\log c+o(1) \end{aligned} \end{equation*} \notag $$

as $u \to \widehat{u}$ and $x \to 0$. In the last equality we used the obvious relation ${c=\prod_{i=1}^n c_i^{\lambda_{i+1}\dotsb \lambda_n}}$, which connects the constant $c$ (see the genericity conditions for Theorem 1) and the constants $c_i=c_i(0,0)$ (see the beginning of &sect; 4.4).

### 4.5. The domain $W_\varepsilon$

Although in &sect; 2.4 we claimed (and, in &sect; 4.3, proved) that the map $\mathbf{F}$ is a diffeomorphism, some functions depending smoothly on the parameters $\delta$ and $ \theta$, show a poor asymptotic behaviour as $F,x \to 0$ of their partial derivatives with respect to $F$ and $\theta$ after the change $\delta=\delta(F, \theta, x)$. Nevertheless, we can distinguish a domain in $B_F \times B_\theta \times (\mathbb{R}_{>0},0)$ in which this problem does not exist.

We denote by $\Theta(1)$ the class of functions on some topological space with values in $\mathbb{R}$ that are separated from zero and infinity as the argument tends to a given point. By analogy with the classes $o(1)$ and $O(1)$, we write $g=\Theta(h)$, implying the membership relation $g \in h\Theta(1)$.

For every $\varepsilon>0$ let $U_\varepsilon$ denote the following subset of the simplex $U$ (see &sect; 2.3):

$$ \begin{equation} U_\varepsilon=\biggl\{z=(z_1:\dotsb:z_n) \in U\biggm| \forall\, i, j=1, \dots, n \ \biggl|\frac{z_i}{z_j}\biggr| > \varepsilon \biggr\}. \end{equation} \tag{64} $$

The preimage of this set under the action of the map $\mathcal{Z}(F,\theta,x)$ (see &sect; 2.4) is denoted by $W_\varepsilon= \mathcal{Z}^{-1}(U_\varepsilon) \subset B_F \times B_\theta \times (\mathbb{R}_{>0},0)$.

We note that the following relations hold in the domain $W_\varepsilon$ for $i,j=0, \dots, n-1$:

$$ \begin{equation} \log F_i=O(\log F_j) \end{equation} \tag{65} $$

as $F,x \,{\to}\, 0$ uniformly with respect to $\theta$ on an arbitrary compact subset of $B_\theta$. In fact, it follows from the definition of the domain $U_\varepsilon$ that the functions $u_i=u_i(F, \theta, x)\!=\!\frac{Z_i(F, \theta, x)}{Z_1(F, \theta, x)}$ are separated from zero and infinity in this domain. Therefore, according to (60), for $i=0, \dots, n-1$ the equality $F_i= x^{\lambda_1(F,\theta,x)\dotsb\lambda_i(F, \theta,x)} \Theta(1)$ holds as $F,x \to 0$ in $W_\varepsilon$. Thus,

$$ \begin{equation*} \log F_i=\lambda_1(F,\theta,x)\dotsb\lambda_i(F, \theta,x) \log x (1+o(1)) \quad\text{as } F,x \to 0, \end{equation*} \notag $$

from which we obtain (65).

In $W_\varepsilon$ a relation following from (65) also holds for $\alpha \in \mathbb{R}$ and $i,j=0, \dots, n-1$:

$$ \begin{equation} F_i |{\log F_j}|^\alpha=F_i O(|{\log F_i}|^\alpha) \to 0 \end{equation} \tag{66} $$

as $F,x \to 0$ uniformly with respect to $\theta$ in an arbitrary compact set in $B_\theta$.

**Lemma 8.**For $i=1, \dots, n-1$, the function $F_i(\delta, \theta, x)$ defined by (9) (see &sect; 2.4) on the set $\mathbf{F}^{-1}\big|_{F_n=x}(W_\varepsilon)$ satisfies the relations

$$ \begin{equation*} \frac{1}{F_i}\frac{\partial F_i}{\partial\delta_k}= \begin{cases} \Theta\biggl(\dfrac{1}{F_k}\biggr)+O(\log x) & \textit{for } k \leqslant i, \\ O(\log x) & \textit{for } k > i \end{cases} \end{equation*} \notag $$

as $\delta, x \to 0$, $k=1, \dots, n-1$, and

$$ \begin{equation} \frac{1}{F_i}\frac{\partial F_i}{\partial \theta_k}=O(\log x) \end{equation} \tag{67} $$

as $\delta, x \to 0$, $k=1, \dots, s$. All limits are uniform with respect to $\theta$ in an arbitrary compact subset of $B_\theta$.

**Proof.**We find a recurrence relation connecting the expression $\frac{1}{F_i}\frac{\partial F_i}{\partial \delta_k}$ with $\frac{1}{F_{i-1}}\frac{\partial F_{i-1}}{\partial \delta_k}$. According to the definitions (2) and (9) of the functions $f_i$ and $F_i$, we have

$$ \begin{equation} \frac{\partial F_i}{\partial\delta_k}=\frac{\partial f_i(F_{i-1})}{\partial \delta_k}= \frac{\partial \delta_i}{\partial \delta_k} \pm \frac{\partial \Delta_i}{\partial\delta_k}(F_{i-1}) \pm \Delta_i'(F_{i-1}) \, \frac{\partial F_{i-1}}{\partial \delta_k}. \end{equation} \tag{68} $$

By Proposition 13 the derivative of the correspondence map $\Delta_i$ satisfies

$$ \begin{equation*} \frac{\partial \Delta_i}{\partial \delta_k}(F_{i-1}) =O\bigl(F_{i-1}^{\lambda(\delta, \theta)} \log F_{i-1}\bigr) =\Delta_i'(F_{i-1})F_{i-1} O(\log F_{i-1}). \end{equation*} \notag $$

We substitute the expression thus obtained into (68). According to (10) and (61) and also relation (65) for $i=1, \dots, n-1$, we obtain

$$ \begin{equation} \begin{aligned} \, \notag \frac{1}{F_i} \frac{\partial F_i}{\partial \delta_k} &=\frac{1}{F_i} \frac{\partial \delta_i}{\partial \delta_k} \pm \frac{\Delta_i'(F_{i-1})F_{i-1}}{F_i}\biggl(O(\log x)+ \frac{1}{F_{i-1}}\frac{\partial F_{i-1}}{\partial \delta_k} \biggr) \\ \notag &=\frac{1}{F_i} \frac{\partial \delta_i}{\partial \delta_k} \pm \frac{Z_{i+1}}{Z_i} \biggl(O(\log x) +\frac{1}{F_{i-1}}\frac{\partial F_{i-1}}{\partial \delta_k} \biggr) \\ &= \frac{1}{F_i} \frac{\partial \delta_i}{\partial \delta_k}+O(\log x)+ \Theta\biggl(\frac{1}{F_{i-1}}\biggr) \frac{\partial F_{i-1}}{\partial \delta_k}. \end{aligned} \end{equation} \tag{69} $$

The last transition follows from the definition of the domain $U_\varepsilon$.

We prove the statement of the lemma by induction on $i=1, \dots, n-1$.

The *induction base*$i=1$ follows from the recurrence relation (69) and the equality $F_0=x$.

The *induction step*. Let the statement be proved for $i-1$. Since for $k < i$ we have $\frac{\partial \delta_i}{\partial \delta_k}=0$, using the induction assumption and the recurrence relation (69) we find that

$$ \begin{equation*} \frac{1}{F_i}\frac{\partial F_i}{\partial\delta_k}=O(\log x) +\Theta(1)\biggl( \Theta\biggl(\frac{1}{F_k}\biggr)+O(\log x) \biggr)=\Theta\biggl(\frac{1}{F_k}\biggr)+O(\log x) \end{equation*} \notag $$

as $\delta,x \to 0$, uniformly with respect to $\theta$ in an arbitrary compact subset of $B_\theta$. For $k=i$ and $k>i$ the proofs are similar.

The proof for the partial derivative with respect to $\theta_k$ repeats literally the argument for the derivative with respect to $\delta_k$ with the only difference that $\frac{\partial \delta_i}{\partial \theta_k}=0$ for all $i$ and $k$, from which we obtain (67).

This completes the proof of Lemma 8.

**Corollary 4.**Under the assumptions of Lemma 8 the following matrix relation holds:

$$ \begin{equation*} \biggl(\frac{1}{F_i} \frac{\partial F_i}{\partial \delta_k}\biggr)_{i,k=1}^{n-1}=G(\delta, \theta, x) \operatorname{diag}(F_1, \dots, F_{n-1})^{-1}, \end{equation*} \notag $$

where the $(n-1) \times (n-1)$-matrix $G(\delta, \theta, x)$ has the form

$$ \begin{equation} G(\delta, \theta,x)= \begin{pmatrix} \Theta(1) & 0 & 0 \\ \vdots & \ddots & 0 \\ \Theta(1) & \cdots & \Theta(1) \end{pmatrix}+o(1) \end{equation} \tag{70} $$

as $\delta, x \to 0$ uniformly with respect to $\theta$ in an arbitrary compact set in $B_\theta$.

This follows from Lemma 8 and the property (66) of the set $W_\varepsilon$.

### 4.6. Checking smoothness after the substitution $\delta= \delta(F,\theta,x)$

In this subsection we establish some properties of partial derivatives of smooth functions after the substitution $\delta=\delta(F,\theta,x)$.

**Proposition 15.**Let $g(\delta, \theta)$ be a $C^1$-smooth function. Then for $\varepsilon>0$ and each $k=1, \dots, n-1$, after the substitution $\delta=\delta(F, \theta, x)$ (see &sect; 2.4) the limit

$$ \begin{equation} F_k\,\frac{\partial g(F, \theta, x)}{\partial F_k} \to 0 \end{equation} \tag{71} $$

exists in the domain $W_\varepsilon$ as $F,x \to 0$. In addition, for $k=1, \dots, s$,

$$ \begin{equation} \frac{\partial g(F, \theta, x)}{\partial \theta_k}=\frac{\partial g(\delta, \theta, x)}{\partial \theta_k}\bigg|_{\delta=\delta(F,\theta,x)}+o(1) \end{equation} \tag{72} $$

as $F,x \to 0$. All limits are uniform with respect to $\theta$ in an arbitrary compact subset of $B_\theta$. Moreover, the functions (71) are H&ouml;lder continuous at zero with respect to the variables $F$ and $x$, and the H&ouml;lder coefficients do not depend on the parameter $\theta$ in such a compact set.

**Remark 3.**Proposition 15 mentions neither the partial derivative with respect to $\delta_n$ nor the partial derivative with respect to $F_n$. The point is that the change ${\delta=\delta(F, \theta, x)}$ implies not only the application of the diffeomorphism $\mathbf{F}$ to the space $B_\delta \times B_\theta \times (\mathbb{R}_{>0},0)$ but also the restriction to the surface $\mathcal{C}_{\mathrm{Fix}}$, which leads to the elimination of these parameters (see &sect; 2.4).

**Proof**of Proposition 15. For $k=1, \dots, n-1$ it follows from the identity

$$ \begin{equation} g(\delta, \theta, x)=g\bigl(F(\delta, \theta, x), \theta, x\bigr) \end{equation} \tag{73} $$

on the set $\mathbf{F}^{-1}\big|_{F_n=x}(W_\varepsilon)$ that

$$ \begin{equation*} \frac{\partial g(\delta, \theta, x)}{\partial \delta_k} =\sum_{i=1}^{n-1} \frac{\partial g(F, \theta, x)}{\partial F_i} \frac{\partial F_i}{\partial \delta_k}=\sum_{i=1}^{n-1} F_i\,\frac{\partial g(F, \theta, x)}{\partial F_i} \frac{1}{F_i}\frac{\partial F_i}{\partial \delta_k}. \end{equation*} \notag $$

By Corollary 4 this equality can be rewritten in a matrix form:

$$ \begin{equation*} \begin{pmatrix} \dfrac{\partial g(\delta, \theta, x)}{\partial \delta_1} \\ \vdots \\ \dfrac{\partial g(\delta, \theta, x)}{\partial \delta_{n-1}} \end{pmatrix} =\operatorname{diag}(F_1, \dots, F_{n-1})^{-1} G^\top(\delta, \theta, x) \begin{pmatrix} F_1\,\dfrac{\partial g(F, \theta, x)}{\partial F_1} \\ \vdots \\ F_{n-1}\,\dfrac{\partial g(F, \theta, x)}{\partial F_{n-1}} \end{pmatrix} \biggr|_{F=F(\delta, \theta, x)}, \end{equation*} \notag $$

where the nonsingular square matrix $G(\delta, \theta,x)$ is given by (70). After the change $\delta=\delta(F, \theta, x)$ we obtain

$$ \begin{equation*} \begin{pmatrix} F_1\,\dfrac{\partial g(F, \theta, x)}{\partial F_1} \\ \vdots \\ F_{n-1}\,\dfrac{\partial g(F, \theta, x)}{\partial F_{n-1}} \end{pmatrix} G^\top(F, \theta, x)^{-1} \operatorname{diag}(F_1, \dots, F_{n-1}) \begin{pmatrix} \dfrac{\partial g(\delta, \theta, x)}{\partial \delta_1} \\ \vdots \\ \dfrac{\partial g(\delta, \theta, x)}{\partial \delta_{n-1}} \end{pmatrix} \biggr|_{\delta=\delta(F, \theta, x)}. \end{equation*} \notag $$

The matrix $G^\top(F, \theta, x)^{-1}$ is bounded in the domain $W_\varepsilon$. The derivatives $\frac{\partial g(\delta, \theta, x)}{\partial \delta_k}$, $k=1,\dots,n-1$ are also bounded by assumption. Therefore, for every $k=1, \dots, {n-1}$ the function $F_k\frac{\partial g(F,\theta,x)}{\partial F_k}$ is represented as a linear combination of the parameters $F_1,\dots,F_{n-1}$ with bounded coefficients; in particular, it is H&ouml;lder continuous with respect to the variables $F_1,\dots,F_{n-1}$ and tends to zero.

To find the derivative with respect to the parameter $\theta_k$, $k=1, \dots, s$ we differentiate (73) again:

$$ \begin{equation} \frac{\partial g(\delta, \theta, x)}{\partial \theta_k} =\frac{\partial g(F, \theta, x)}{\partial \theta_k}\biggr|_{F=F(\delta, \theta, x)} +\sum_{i=1}^{n-1} F_i\,\frac{\partial g(F, \theta, x)}{\partial F_i}\frac{1}{F_i} \frac{\partial F_i}{\partial \theta_k}\biggr|_{F=F(\delta, \theta, x)}. \end{equation} \tag{74} $$

Here we have again multiplied and divided the $i$th term of the sum by $F_i$. By the property (65), relation (67) and the H&ouml;lder property of the function $F_i \frac{\partial g(F, \theta, x)}{\partial F_i}$, the sum on the right-hand side of (74) tends to zero, which implies the required relation (72).

This completes the proof of Proposition 15.

We will apply Proposition 15 to a certain set of functions only. Let us list them.

**Corollary 5.**For every $i=1,\dots,n$ and any positive integer $q$ the functions $\lambda_i(F,\theta,x)$, $\Psi_i(F, \theta, x)$ and $\mu_{iq}(F, \theta, x)$ in the domain $W_\varepsilon$ satisfy relations (71) and (72).

These functions are obtained after the change $\delta=\delta(F,\theta,x)$ from the characteristic numbers $\lambda_i(\delta, \theta)$ and the functions $\Psi_i(\delta, \theta, F_{i-1})$ and $\mu_{iq}(\delta, \theta, x)$ given by formulae (59) and (11), respectively.

**Proof**of Corollary 5. For the functions $\lambda_i(F,\theta,x)$ and $\Psi_i(F, \theta, x)$ it is sufficient to prove that the functions $\lambda_i(\delta,\theta)$ and $\Psi_i(\delta, \theta, F_{i-1})$ satisfy the assumptions of Proposition 15. For the characteristic number $\lambda_i(\delta,\theta)$ the assumption is obviously satisfied: it depends on the parameters smoothly.

For $q\in \mathbb{N}\cup \{0\}$ let $g_y^q(\delta, \theta)$ denote the function

$$ \begin{equation*} g_y^q(\delta, \theta)=y^q\,\frac{\partial^q\Psi_i(\delta, \theta, y)}{\partial y^q}. \end{equation*} \notag $$

For $q=0$ we obtain $g_y^0(\delta, \theta)=\Psi_i(\delta, \theta, y)$. According to (11) and (59), the function $\mu_i(\delta, \theta, x)$ can be represented as follows:

$$ \begin{equation} \mu_{iq}(\delta, \theta, x)=(-1)^{q-1}(q-1)!\,\bigl(\lambda_i(\delta, \theta)-1\bigr) + g_{F_{i-1}}^q(\delta, \theta). \end{equation} \tag{75} $$

Therefore, it suffices to show that the assumptions of Proposition 15 are satisfied by the function $g_y^q(\delta, \theta)$ for any fixed $y$ and all nonnegative $q$.

By Proposition 14 the function $g_y^q(\delta, \theta)$ is at least $C^1$-smooth with respect to the parameters $\delta$ and $ \theta$ for every fixed $y$, including $y=0$. Hence by Proposition 15, after the change $\delta= \delta(F, \theta, x)$ the function $g_y^q(F, \theta, x)$ satisfies relations (71) and (72) for all $y$. Consequently, the function $g_{F_{i-1}}^q(F, \theta, x)$ also satisfies these relations, with the exception of the derivative with respect to $F_{i-1}$, for which the assertion is verified directly:

$$ \begin{equation*} F_{i-1}\,\frac{\partial g_{F_{i-1}}^q(F, \theta, x)}{\partial F_{i-1}} = F_{i-1}\,\frac{\partial g_y^q(F, \theta, x)}{\partial F_{i-1}} \biggr|_{y=F_{i-1}}+ y\,\frac{\partial g_y^q(F, \theta, x)}{\partial y} \biggr|_{y=F_{i-1}}. \end{equation*} \notag $$

The first term on the right-hand side tends to zero according to what we proved above. The other term is equal to $g^{q+1}_{F_{i-1}}(F,\theta,x)+q g^q_{F_{i-1}}(F,\theta,x)$ and also tends to zero as $F,x \to 0$ by the property (56).

This completes the proof of Corollary 5.

### 4.7. Lemmas

In &sect; 4.8 we prove that the map $\widehat{\mathcal Z}$ defined by (18) is a diffeomorphism onto some domain. To do this we need the following two lemmas.

**Lemma 9.**Let $\mathcal{W}$ and $\mathcal{V}$ be nonempty open sets in $\mathbb{R}^k$, where $\mathcal{V}$ is a simply connected domain. Let the $C^1$-smooth map $h\colon \mathcal{W} \to \mathbb{R}^k$ be nondegenerate on the nonempty compact set $\overline{h^{-1}(\mathcal{V})} \subset \mathcal{W}$. Then for any connected component $X$ of the set $h^{-1}(\mathcal{V})$ the map $h\colon X \to \mathcal{V}$ is a diffeomorphism.

**Proof.**Since $\overline{X} \subset \mathcal{W}$ is a compact set by assumption, it follows from the continuity of $h$ that $h(\overline{X})=\overline{h(X)}$ is closed in $h(\mathcal{W})$. However, no point on the boundary of $X$ can lie in $\mathcal{V}$, and therefore $\overline{h(X)} \cap \mathcal{V}=h(X)$. In other words, the set $h(X)$ is closed in $\overline{V}$. On the other hand $h$ is a local diffeomorphism, in particular, an open map. Consequently, $h(X)$ is also open in $\mathcal{V}$. Since $X$ is connected and $h$ is continuous, $h(X)$ is connected, and this implies that $h(X)=\mathcal{V}$.

Suppose that there exist two points $x_0, x_1 \in X$ such that $x_0 \neq x_1$, but $h(x_0)= h(x_1)=y$, where $y$ is a point in $\mathcal{V}$. Since $X$ is connected, we can join the points $x_0$ and $x_1$ by a curve $x(\tau)$, $\tau \in [0,1]$. As $h$ is a local diffeomorphism, it extends along this curve, and its image $h \circ x(\tau)$ forms a loop in the domain $\mathcal{V}$ beginning and ending at the point $y$. Since $\mathcal{V}$ is simply connected, the loop contracts to $y$. Consequently, the germ of the diffeomorphism $h^{-1}$ at point $y$ and the other germ at $y$ obtained by continuation along the loop, must coincide. It follows that $x_0=h^{-1}(y)=x_1$. Thus, $h\colon X \to \mathcal{V}$ is a diffeomorphism.

This completes the proof of Lemma 9.

**Lemma 10.**Let $\mathcal{W}$ and $\mathcal{V}$ be nonempty open sets in $\mathbb{R}^k$, where $\mathcal{V}$ is a simply connected domain, and let $h_t\colon \mathcal{W} \to \mathbb{R}^k$, $t \in [0,1]$, be a $C^1$-smooth family of $C^1$-smooth maps. Denote the preimage $h_t^{-1}(\mathcal{V})$ by $\mathcal{W}_t$. Let the set $\overline{\mathcal{W}}_t \subset \mathcal{W}$ be compact for each $t \in [0,1]$, and let the map $h_t$ be nondegenerate in $\overline{\mathcal{W}}_t$. Then the set $\mathcal{W}_t$ consists of the same number of components for all $t$.

For some $t$ the set $\mathcal{W}_t$ can consist of an infinite (obviously, countable) number of components. Lemma 10 states that in this case, for any other $t$ the set $\mathcal{W}_t$ consists of countably many components.

**Proof**of Lemma 10. By the continuity of the family the set of values of the parameter $t$ for which a fixed component of the set $\mathcal{W}_t$ exists is open. Let the number of components change, for instance, decrease, as the parameter $t$ crosses some value $\widetilde t$. Since by assumption the set $\mathcal{W}_t$ is compactly contained in the domain of definition $\mathcal{W}$, it follows that this is possible in the following two cases only.

*Case*1. Some component $X_t$ of $\mathcal W_t$ decreased until disappearing for $t= \widetilde t$. By Lemma 9 the map $h_t\colon X_t \to \mathcal{V}$ is a diffeomorphism for each $t$. In particular, there is an inverse map of this diffeomorphism, $h_t^{-1}\colon \mathcal{V} \to X_t$, which depends smoothly on the parameter $t$ (we note that this map is just one of the sheets of the possibly multivalued map $h_t^{-1}\colon \mathcal{V} \to \mathcal W_t$). Since the component $X_t$ decreases, its volume

$$ \begin{equation*} \mu(X_t)=\int_{X_t}dx=\int_{\mathcal{V}}\biggl|\det \frac{\partial h_t^{-1}(y)}{\partial y}\biggr|\,dy \end{equation*} \notag $$

tends to zero as $t \to \widetilde t$. But the Jacobian is a continuous function, and the set $\mathcal W_t$ is by assumption compactly contained in $\mathcal{W}$. Hence there exists $M>0$ such that for all $y \in \overline{\mathcal{V}}$ and each $t$

$$ \begin{equation*} \biggl|\det \frac{\partial h_t(x)}{\partial x}\biggr| < M. \end{equation*} \notag $$

Therefore,

$$ \begin{equation*} \mu(X_t) > \frac{1}{M}\mu(\mathcal{V}) > 0. \end{equation*} \notag $$

This is a contradiction. Thus, Case 1 is impossible.

*Case*2. For some value of the parameter $t$ there are two components $X_{1,t}$ and $X_{2,t}$ of the set $\mathcal{W}_t$ which merge into a single component as $t$ changes further. Let $t\in (0,1)$. By Lemma 9 the map $h_t$ is bijective on each of these components. Hence it is not injective on their union. In particular, the nondegenerate map

$$ \begin{equation*} h\colon \mathcal{W} \times (0,1) \to \mathcal{V} \times (0,1), \qquad h\colon (x,t) \mapsto (h_t(x),t) \end{equation*} \notag $$

is not injective either. We note that the set $\mathcal{V} \times (0,1)$ is a simply connected domain, and so this set and the map $h$ satisfy the assumptions of Lemma 9. Consequently, the map $h$ is a diffeomorphism on any connected component of the set $h^{-1}\bigl(\mathcal{V} \times (0,1)\bigr)$. However, since the components $X_{1,t}$ and $X_{2,t}$ merge into one as the parameter $t \in (0,1)$ varies, it follows that these components are contained in the same component of $h^{-1}\bigl(\mathcal{V} \times (0,1)\bigr)$, which contradicts the bijectivity of $h$. Consequently, for all $t \in (0,1)$ the set $\mathcal{W}_t$ consists of the same number of components.

Now we find the number of components of the set $\mathcal{W}_0$. Consider an arbitrary point $y \in \mathcal{V}$. According to Lemma 9, every component of the set $\mathcal{W}_0$ (there can be infinitely many of them) contains a point that is a preimage of $y$ under the map $h_0$. Since the family $h_t$ is smooth, each of these points is preserved under a small change of $t$. Consequently, if the set $\mathcal{W}_0$ has at least $m \in \mathbb{N}$ connected components, then there exists a small value of $t>0$ such that the set $\mathcal{W}_t$ has at least $m$ connected components. According to what we proved above, for each $t \in (0,1)$ the set $\mathcal{W}_t$ consists of the same number of components and the components themselves do not disappear as $t$ varies, and therefore $\mathcal{W}_0$ consists of the same number of components as the set $\mathcal{W}_t$ for $t \in (0,1)$. The case $t=1$ is analyzed similarly. Thus, for all $t$ the set $\mathcal{W}_t$ consists of the same number of components.

This completes the proof of Lemma 10.

**Corollary 6.**If the map $h_0\colon \mathcal{W}_0 \to \mathcal{V}$ is a diffeomorphism under the assumptions of Lemma 10, then $h_1\colon \mathcal{W}_1 \to \mathcal{V}$ is also a diffeomorphism.

### 4.8. The map $\widehat{\mathcal{Z}}$ is a diffeomorphism

In this section we prove Proposition 5. This proof is based on the lemmas in &sect; 4.7.

**Lemma 11.**Let the set $K$ be compactly contained in $B_\theta$. Then for each $\varepsilon>0$ there is a positive number $x_{\varepsilon,K}$ such that, the map $\widehat{\mathcal{Z}}(F,\theta,x)$ defined by (18) is nondegenerate in the closure of the set

$$ \begin{equation*} W_\varepsilon \cap \{(F,\theta,x) \mid x < x_{\varepsilon,K}, \, \theta \in K\} \subset B_F \times B_\theta \times (\mathbb{R}_{>0},0) \end{equation*} \notag $$

( $W_\varepsilon$ we defined in &sect; 4.5).

**Proof.**Since the map $\widehat{\mathcal{Z}}(F,\theta,x)$ preserves the variables $x$ and $\theta$, it suffices to prove, the nondegeneracy of the map

$$ \begin{equation} F \mapsto \bigl(\log|u_2(F,\theta, x)|, \dots, \log|u_n(F, \theta, x)|\bigr) \end{equation} \tag{76} $$

for all small fixed $x>0$ and all fixed $\theta \in K$. Indeed, since for $i=2, \dots, n$ the functions $u_i(F, \theta, x)$ do not vanish, the nondegeneracy of the map (76) implies the nondegeneracy of $\widehat{\mathcal{Z}}(F,\theta,x)$.

Let us find the Jacobian matrix of the map (76) with respect to $F_1,\dots,F_{n-1}$. From formulae (15) and (59), for $i=2, \dots, n$ we have

$$ \begin{equation} \log |u_i(F,\theta,x)|=\log x -\log F_{i-1}+\sum_{j=1}^{i-1} \bigl(\lambda_j(F,\theta,x) - 1\bigr)\log F_{j-1}+\Psi_j(F, \theta, x). \end{equation} \tag{77} $$

For $k=1, \dots, n-1$ we differentiate this equality with respect to $F_k$ and multiply by $F_k$. Then we obtain

$$ \begin{equation} \frac{F_k}{u_i} \frac{\partial u_i}{\partial F_k}= \begin{cases} \lambda_{k+1}(F, \theta, x)-1+h_{ik}(F, \theta, x) & \text{for } k=1,\dots,i-1, \\ - 1+h_{ik}(F, \theta, x) & \text{for } k=i, \\ h_{ik}(F, \theta, x) & \text{for } k=i+1, \dots, n-1, \end{cases} \end{equation} \tag{78} $$

where

$$ \begin{equation} h_{ik}(F, \theta, x)=\sum_{j=1}^{i-1} F_k \frac{\lambda_j(F,\theta,x)}{\partial F_k} \log F_{j-1} +F_k\frac{\Psi_j(F, \theta, x)}{\partial F_k}. \end{equation} \tag{79} $$

By Proposition 15 and Corollary 5, both terms in (79) are H&ouml;lder continuous with respect to the variables $F$ and $x$, and therefore by (66), for any $i$ and $k$ the function $h_{ik}$ tends to zero uniformly for $\theta \in \overline{K}$ as $F,x \to 0$.

Thus, it follows from (78) that the matrix

$$ \begin{equation*} \biggl( \frac{F_k}{u_i} \frac{\partial u_i}{\partial F_k} \biggr)_{ik}, \qquad i=2,\dots,n, \quad k=1,\dots,n-1, \end{equation*} \notag $$

is represented in the form

$$ \begin{equation} \biggl( \frac{F_k}{u_i} \frac{\partial u_i}{\partial F_k} \biggr)_{ik} =A(\theta)+o(1), \end{equation} \tag{80} $$

where $A(\theta)$ is a lower triangular matrix with determinant $(-1)^{n-1}$ that depends continuously on the parameter $\theta$. Therefore, there exists $x_{\varepsilon,K}>0$ such that for $x \leqslant x_{\varepsilon,K}$ the Jacobian of the map (77) is distinct from zero.

This completes the proof of Lemma 11.

**Lemma 12.**Let $K$ be an arbitrary open ball contained in $B_\theta$ together with its closure. Then there exists $\widetilde x_{\varepsilon,K}>0$ such that for all $0<x'<\widetilde x_{\varepsilon,K}$ the map $\widehat{\mathcal{Z}}(F,\theta,x)$ defined by (18) is a diffeomorphism of the sets $\widehat{\mathcal{Z}}^{-1}(\mathcal{V}_{\varepsilon,K,x'})$ and $\mathcal{V}_{\varepsilon,K,x'}=U_\varepsilon \times K \times (x', \widetilde x_{\varepsilon,K})$, where the domain $U_\varepsilon$ is defined by (64).

The number $\widetilde x_{\varepsilon,K}$ mentioned in this lemma can differ from $x_{\varepsilon,K}$ in Lemma 11.

**Proof**of Lemma 12. Along with the parameter $\theta$, we introduce another additional parameter $t$, which ranges over the interval $[0,1]$. In formula (2) for the function $f_i(\delta,\theta,x)$, $i=1,\dots,n$, we replace the saddle correspondence map $\Delta_i(\delta,\theta,x)$ by the function

$$ \begin{equation*} \Delta_i(\delta,\theta,x,t)=\int_0^x y^{\lambda_i(t\delta, t\theta)-1}e^{\Psi_i(t\delta,t\theta,ty)}dy. \end{equation*} \notag $$

For $t=1$ this function coincides with $\Delta_i(\delta,\theta,x)$ and when $t=0$ we have $\Delta_i(\delta,\theta,x,0)=c_i(0,0)x^{\lambda_i(0,0)}$ (see Proposition 13). For $t \in [0,1]$ and $i=1,\dots,n$ the function $\Delta_i(\delta,\theta,x,t)$ satisfies relations (53) and (54), and the function $\Psi_i(\delta,\theta,x,t)=\Psi_i(t\delta,t\theta,tx)$ satisfies (55) and (56). Therefore, all the previous arguments are applicable to the new family of functions, in particular, Lemma 11, which claims the nondegeneracy of the map $\widehat{\mathcal{Z}}(F,\theta,x,t)$ in the closure of the domain

$$ \begin{equation*} \widehat{\mathcal{Z}}^{-1}(\mathcal{V}_{\varepsilon,K,x'}) =W_\varepsilon \cap \{(F,\theta,x,t)\mid x' < x < \widetilde x_{\varepsilon,K},\, \theta \in K\}, \end{equation*} \notag $$

where the number $\widetilde x_{\varepsilon,K}=x_{\varepsilon,K \times [0,1]}$ is chosen independently of both $\theta \in K$ and the parameter $t \in [0,1]$.

**Remark 4.**Generally speaking, we are not so much dealing with fields and saddle correspondence maps, but rather with functions which have certain properties; thus, all our arguments are valid for such functions, which can have nothing to do with fields and polycycles. (For more details, see &sect; 5.)

Note that for $t=0$ the map $\widehat{\mathcal{Z}}(F,\theta,x,0)$ is a diffeomorphism of the domains $B_F \times B_\theta \times (\mathbb{R}_{>},0)$ and $U \times B_\theta \times (\mathbb{R}_{>0},0)$ and is defined by the functions

$$ \begin{equation*} \log |Z_i|=-\log F_{i-1}+\sum_{j=1}^{i-1} \bigl(\lambda_j-1\bigr)\log F_{j-1}+\Psi_j, \qquad i=1,\dots,n, \end{equation*} \notag $$

where we have $\lambda_i=\lambda_i(0, 0)$ and $\Psi_i=\Psi_i(0, 0, 0)$ (cf. (77)). Its inverse has the form (60), where, again, $\lambda_i=\lambda_i(0, 0)$ and $\Psi_i=\Psi_i(0, 0, 0)$ (see Remark 2).

Note that the set $\mathcal{V}_{\varepsilon,K,x'}$ is a simply connected domain, and for $t \in [0,1]$ its preimage $\widehat{\mathcal{Z}}^{-1}(\mathcal{V}_{\varepsilon,K,x'})$ under the action of the map $\widehat{\mathcal{Z}}(F,\theta,x,t)$ is compactly contained in $B_F \times B_\theta \times (\mathbb{R}_{>0},0)$. Then, according to Corollary 6, we see that the map $\widehat{\mathcal{Z}}(F,\theta,x,1)$ is a diffeomorphism on the set specified in the condition.

This completes the proof of Lemma 12.

**Proof**of Proposition 5. Consider the following set:

$$ \begin{equation*} \mathcal{V}=\bigcup_{\varepsilon>0}\bigcup_{K \subset B_\theta} \bigcup_{0< x' < \widetilde x_{\varepsilon,K}} \mathcal{V}_{\varepsilon,K,x'}, \end{equation*} \notag $$

where the variable $K$ ranges over all open balls compactly contained in $B_\theta$. The preimage of this set under the action of the map $\widehat{\mathcal{Z}}(F,\theta,x)$ is denoted by $W \subset B_F \times B_\theta \times (\mathbb{R}_{>0},0)$. Let us show that $W$ has all properties mentioned in Proposition 5.

Since, according to Lemma 12, the map $\widehat{\mathcal{Z}}^{-1}$ is a diffeomorphism on each set $\mathcal{V}_{\varepsilon,K,x'}$, $\widehat{\mathcal{Z}}$ is surjective on the set $W$. Suppose that the map $\widehat{\mathcal{Z}}$ is not injective on $W$, that is, there exist two points in $W$ such that the values of $\widehat{\mathcal{Z}}$ at these points coincide. We denote by $\mathcal{V}_{\varepsilon_1,K_1,x_1'}$ and $\mathcal{V}_{\varepsilon_2,K_2,x_2'}$ the sets containing the images of these points under the action of the map $\widehat{\mathcal{Z}}$. However, the map $\widehat{\mathcal{Z}}$ preserves the $x$- and $\theta$-coordinates, which implies their equality for both points. Therefore, both points belong to the set $\widehat{\mathcal{Z}}^{-1}(\mathcal{V}_{\varepsilon,K,x'})$, where $\varepsilon= \min(\varepsilon_1,\varepsilon_2)$, $x'=\min(x_1',x_2')$, and $K$ is either of the open balls $K_1$ and $K_2$. But by Lemma 12, the map $\widehat{\mathcal{Z}}$ is bijective on the set $\widehat{\mathcal{Z}}^{-1}(\mathcal{V}_{\varepsilon,K,x'})$. This is a contradiction. Therefore, $\widehat{\mathcal{Z}}$ is a diffeomorphism of the sets $W$ and $\mathcal{V}$. Thus, we have proved assertion (2) of Proposition 5.

For every $\theta \in B_\theta$ there is a point $(u,\theta,x)$ in $\mathcal{V}$ with an arbitrarily small $x$-coordinate. Consequently, the set $W$ also contains points with an arbitrarily small $x$-coordinate. However, by the properties of the sets $W_\varepsilon$ (see &sect; 4.5), the sequence of these points accumulates to $(0,\theta,0) \in B_F \times B_\theta \times (\mathbb{R}_{\geqslant 0},0)$, which implies property (1) in Proposition 5 by virtue of Lemma 1.

For every point $u \in U$ and each $\theta \in B_\theta$ there exists $\varepsilon>0$ and a closed ball $K \subset B_\theta$ with centre $\theta$ such that $u$ belongs to the set $U_\varepsilon$ defined by (64) and the set $\overline{\bigcup_{x'>0}\mathcal{V}_{\varepsilon,K,x'}}$ is a closed neighbourhood of the point $(u,\theta,0) \in U \times B_\theta \times (\mathbb{R}_{\geqslant 0},0)$, which proves property (3).

Property (4) (the uniqueness of the preimage of any point in $\widehat{\mathcal{Z}}(W)=\mathcal{V}$) follows from the definition of $W$ and property (2) proved above.

Let us prove property (5) (the asymptotic behaviour of the Jacobian of $\widehat{\mathcal{Z}}^{-1}$). It follows from (80) that, in the logarithmic chart, the Jacobian of the map $\widehat{\mathcal{Z}}^{-1}$ tends to $(-1)^{n-1}$ as $x \to 0$. Hence, the Jacobian in the chart $U \times (\mathbb{R}_{>0},0)$ has the form

$$ \begin{equation*} J\widehat{\mathcal{Z}}^{-1}=(-1)^{n-1}\frac{F_1 \dotsb F_{n-1}}{u_2 \dotsb u_n}\bigl(1+o(1)\bigr) \end{equation*} \notag $$

as $x \to 0$, where $F_i=F_i(u, \theta, x)$, $i=1,\dots,n-1$. Setting

$$ \begin{equation*} a(u)= \frac{(-1)^{n-1}}{u_2\dotsb u_n}, \end{equation*} \notag $$

we obtain the required asymptotic behaviour.

This completes the proof of Proposition 5.

### 4.9. Smooth extensions of derivatives of the Poincar&eacute; map

In this section we prove that the blown-up derivatives of the Poincar&eacute; map extend $C^1$-smoothly to the &lsquo;base&rsquo; $U \times B_\theta \times \{0\}$ of the &lsquo;hat&rsquo; $\widehat{\mathcal{Z}}(W)$ (see &sect; 2.5).

**Proposition 16.**Let $u$ be a point in $U$ (see &sect; 2.3). Let an arbitrary function $g(\delta, \theta)$ satisfy relations (71) and (72) after the change $\delta=\delta(F, \theta, x)$. Then for all ${k=2,\dots,n}$, the blown-up function $g(u, \theta, x)$ satisfies the relations

$$ \begin{equation} \frac{\partial g(u,\theta,x)}{\partial u_k} \to 0 \end{equation} \tag{81} $$

and for $k=1,\dots,s$ it satisfies

$$ \begin{equation} \frac{\partial g(u,\theta,x)}{\partial \theta_k} =\frac{\partial g(\delta,\theta)}{\partial \theta_k} \biggr|_{\delta=\delta(F,\theta,x)}\bigg|_{(F,\theta,x)= \widehat{\mathcal{Z}}^{-1}(u,\theta,x)}+o(1) \end{equation} \tag{82} $$

for $u$ under consideration as $x \to 0$. All limits are uniform with respect to $\theta$ in an arbitrary compact set $K$ in $B_\theta$. Moreover, the derivatives (81) are H&ouml;lder continuous at zero with respect to the variable $x$, and the H&ouml;lder coefficients do not depend on the variables $u$ and $\theta \in K$.

**Proof.**There exists $\varepsilon > 0$ such that the point $u$ belongs to the domain $U_\varepsilon$ defined by (64). Then the following identity holds in the domain $W_\varepsilon \cap \{(F,\theta,x)\mid x < x_\varepsilon, \theta \in K \}$:

$$ \begin{equation} g(F,\theta,x)=g\bigl(u(F,\theta, x), \theta, x\bigr), \end{equation} \tag{83} $$

where $u(F, \theta, x)$ denotes the map $\mathcal{Z}$ in the chart $\{z_1 \neq 0\}$ (see (19)). We differentiate this identity with respect to the variable $F_k$, $k\,{=}\,1,\dots,n\,{-}\,1$:

$$ \begin{equation} F_k\,\frac{\partial g(F,\theta,x)}{\partial F_k}\biggr|_{(F,\theta,x)= \widehat{\mathcal{Z}}^{-1}(u,\theta,x)}=\sum_{i=2}^n \frac{\partial g(u, \theta, x)}{\partial u_i} F_k\,\frac{\partial u_i(F,\theta,x)}{\partial F_k}\biggr|_{(F,\theta,x)= \widehat{\mathcal{Z}}^{-1}(u,\theta,x)}. \end{equation} \tag{84} $$

According to (80) equality (84) can be rewritten in a matrix form:

$$ \begin{equation*} \begin{pmatrix} F_1 \,\dfrac{\partial g(F, \theta, x)}{\partial F_1} \\ \vdots \\ F_{n-1}\, \dfrac{\partial g(F, \theta, x)}{\partial F_{n-1}} \end{pmatrix}\biggr|_{(F,\theta,x)=\widehat{\mathcal{Z}}^{-1}(u,\theta,x)} =\bigl(A(\theta)+o(1)\bigr) \begin{pmatrix} u_2 \,\dfrac{\partial g(u, \theta, x)}{\partial u_2} \\ \vdots \\ u_n \,\dfrac{\partial g(u, \theta, x)}{\partial u_n} \end{pmatrix} \end{equation*} \notag $$

as $x \to 0$. Since the matrix $A$ is invertible and bounded, we obtain (81). Moreover, since, according to Proposition 15, the partial derivatives $F_k \frac{\partial g(F, \theta, x)}{\partial F_k}$ are H&ouml;lder continuous with respect to $F$ and $ x$ for any $k$ and their H&ouml;lder coefficients do not depend on $\theta \in K$, it follows that for $k=1,\dots, s$ the partial derivatives $\frac{\partial g(u, \theta, x)}{\partial u_k}$ are H&ouml;lder continuous with respect to the variable $x$ by virtue of identity (60).

Now we differentiate (83) with respect to the variable $\theta_k$, $k=1, \dots, s$. We find that

$$ \begin{equation} \begin{aligned} \, \notag &\frac{\partial g(F,\theta,x)}{\partial \theta_k}\biggr|_{(F,\theta,x)= \widehat{\mathcal{Z}}^{-1}(u,\theta,x)} \\ &\qquad =\frac{\partial g(u, \theta, x)}{\partial \theta_k}+ \sum_{i=2}^n \frac{\partial g(u, \theta, x)}{\partial u_i}\frac{\partial u_i(F,\theta,x)}{\partial \theta_k}\biggr|_{(F,\theta,x)= \widehat{\mathcal{Z}}^{-1}(u,\theta,x)}. \end{aligned} \end{equation} \tag{85} $$

To prove that the sum on the right-hand side tends to zero, we find the expression $\frac{\partial u_i(F, \theta, x)}{\partial \theta_k}$. Differentiating (77) with respect to the parameter $\theta_k$, we obtain

$$ \begin{equation*} \frac{1}{u_i}\frac{\partial u_i}{\partial \theta_k} =\frac{1}{Z_i}\frac{\partial Z_i}{\partial \theta_k} =\sum_{j=1}^{i-1} \frac{\partial \lambda_j(F, \theta, x)}{\partial \theta_k} \log F_{j-1} +\frac{\partial \Psi_j(F, \theta, x)}{\partial \theta_k}. \end{equation*} \notag $$

By Corollary 5 the partial derivatives of the functions $\lambda_j(F, \theta, x)$ and $\Psi_j(F, \theta, x)$ with respect to the parameter $\theta_k$ are bounded. Consequently, the expression $\frac{1}{u_i}\frac{\partial u_i}{\partial \theta_k}$ grows no more rapidly than the sum of the logarithms of the variables $x$ and $F_i$, $i=1,\dots,n-1$. However, according to what we proved above, the partial derivative $\frac{\partial g(u, \theta, x)}{\partial u_i}$ is H&ouml;lder continuous in $x$. Consequently, the sum on the right-hand side of (85) tends to zero as $x \to 0$ uniformly in $\theta \in K$. From relation (72) we obtain (82).

This completes the proof of Proposition 16.

**Corollary 7.**For $i=1, \dots, n$ and $q \in \mathbb{N}$ the blown-up functions $\lambda_i(u, \theta, x)$, $\Psi_i(u, \theta, x)$ and $\mu_{iq}(u, \theta, x)$ (see &sect; 4.4) can be extended $C^1$-smoothly with respect to the variables $u$ and $\theta$ from the &lsquo;hat&rsquo; $\widehat{\mathcal{Z}}(W)$ to the &lsquo;base&rsquo; $U \times B_\theta \times \{0\}$, to functions $\lambda_i(\theta)$, $\Psi_i(\theta)$ and $\mu_{iq}(\theta)$ independent of $u$, respectively.

Recall that we denote the value of an arbitrary continuous function $g(\delta, \theta, x)$ for $\delta=0$ and $x=0$ by $g(\theta)$.

**Proof**of Corollary 7. The proof obviously follows from Proposition 16 and Corollary 5. Since before the blow-up these functions had a limit as $F,x \to 0$, after the blow-up their extension to the set $U \times \{0\}$ does not depend on the variable $u$. This completes the proof of the corollary.

We proceed to the proof of the $C^1$-smooth extension of the derivatives of the Poincar&eacute; map.

**Proof**of Proposition 6. By (63) and Remark 2 the blown-up function $\mathcal{D}(u, \theta, x)$ can be expressed in terms of the blown-up functions $\lambda_i(u, \theta, x)$ and $\Psi_i(u, \theta, x)$. In particular, it can be written in the form

$$ \begin{equation*} \mathcal{D}(u, \theta, x)=\bigl(\lambda_1(u, \theta, x) \dotsb \lambda_n(\delta, \theta, x)-1 \bigr) \log x+O(1) \end{equation*} \notag $$

as $x \to 0$. Thus, by Corollary 7, the function $\frac{\mathcal{D}(u, \theta, x)}{\log x}$ extends $C^1$-smoothly to the set $U \times B_\theta \times \{0\}$ as the function $\lambda_1(\theta) \dotsb \lambda_n(\theta)-1$.

It follows from (20) that the inflated derivatives of the Poincar&eacute; map $\mathcal{D}_l(u, \theta, x)$, $l \in \mathbb{N}$ can be expressed in terms of the variables $u_2, \dots, u_n$ and the blown-up functions $\mu_{iq}(u, \theta, x)$. Therefore, according to Corollary 7, after multiplying by $x^l$, they also have a $C^1$-smooth extension to the set $U \times B_\theta \times \{0\}$, where they coincide with the polynomials $Q_{nl}(\lambda,u)$ (this was described in detail in &sect; 2.5).

This completes the proof of the proposition.

Finally, we prove Lemma 3, which describes the inflated function $\mu_{iq}$.

**Proof**of Lemma 3. The required representation for the function $\mu_{iq}(u,\theta,x)$ is obtained from (75) and Corollary 7. The H&ouml;lder property follows from Proposition 16. This completes the proof of the lemma.

The proofs of Theorems 1 and 2 are now complete.

### &sect; 5. On functions on the line

As we repeatedly said above, all proofs in this paper can literally be transferred to the case of functions on the line that have certain properties, but are not connected in any way with vector fields.

Consider a family $V$ of functions of the following form:

$$ \begin{equation*} f_i(\delta,\theta,x)=\delta_i+c_i(\delta,\theta) x^{\lambda_i(\delta,\theta)} \bigl(1+ g_i(\delta,\theta,x)\bigr), \qquad i=1,\dots,n, \end{equation*} \notag $$

where the functions $c_i$, $\lambda_i$ and $g_i$ are $C^r$-smooth and $r \geqslant n+1$. We assume that the parameters $\delta$ and $\theta$ are related to the base $B=B_\delta \times B_\theta=(\mathbb{R}^n, 0) \times (\mathbb{R},0)$. As above, we use the abbreviations $c_i=c_i(0,0)$ and $\lambda_i= \lambda_i(0,0)$. Let $c_i>0$ and $\lambda_i>0$ for $i=1,\dots,n$, and let the function $g_i$ satisfy the relations

$$ \begin{equation*} x^q g_i^{(q)}(\delta,\theta,x) \to 0, \qquad 0 \leqslant q \leqslant r, \end{equation*} \notag $$

and

$$ \begin{equation*} x^q \frac{\partial g_i^{(q)} (\delta,\theta,x)}{\partial \beta_j} \to 0, \qquad 0 \leqslant q \leqslant r-1, \end{equation*} \notag $$

as $\delta,\theta,x \to 0$. We assume that the function $g_i$ itself and all of its indicated derivatives are H&ouml;lder continuous with respect to $x$ and the H&ouml;lder coefficients depend continuously on the parameters. We set

$$ \begin{equation} \Delta(\delta,\theta,x)=f_n \circ \dotsb \circ f_1(\delta,\theta,x). \end{equation} \tag{86} $$

**Theorem 4.**Let

$$ \begin{equation*} \lambda_1 \dotsb \lambda_n=1\quad\textit{and} \quad \frac{\partial \bigl(\lambda_1(\delta,\theta) \dotsb \lambda_n(\delta,\theta)\bigr)}{\partial \theta}\bigg|_{\delta,\theta=0} \neq 0. \end{equation*} \notag $$

Then there exists a $C^1$-smooth curve $\tau\colon (\mathbb{R}_{>0},0) \to B$ such that $\tau(x) \to (0,0)$ as $x \to 0+$, and for every $x$ the function $\Delta$ defined by (86) has a fixed point of multiplicity at least $n+1$ for $(\delta,\theta)=\tau(x)$.

Moreover, let the quantity $c= \prod_{i=1,\dots,n}c_i^{\lambda_1\dotsb\lambda_{i-1}}$ be distinct from 1, and let $\widetilde{R}_n(\lambda_1,\dots,\lambda_n) \neq 0$. Then for sufficiently small $x>0$ the function $\Delta$ for $(\delta,\theta)=\tau(x)$ has a fixed point of multiplicity precisely $n+1$. In particular, there is a sequence of values of the parameters $\delta$ and $\theta$ tending to zero in $B$ such that the function $\Delta(\delta,\theta,x)$ has at least $n+1$ fixed points.

**Proof.**The required result is obtained by repeating our previous considerations here. All derivatives under consideration have an order not exceeding $n+1$. By virtue of the specified properties of the functions $g_i$ we see that for $i=1,\dots,n$, the functions $\Delta_i(\delta,\theta,x)=f_i(\delta,\theta,x)- \delta_i$ and

$$ \begin{equation*} \begin{aligned} \, \Psi_i(\delta,\theta,x) &=\log \Delta_i'(\delta,\theta,x)- \bigl(\lambda_i(\delta,\theta)-1\bigr)\log x \\ &=\log \lambda_i(\delta,\theta)+\log c_i(\delta,\theta)+\log \bigl(1+g_i(\delta,\theta,x) +x g_i'(\delta,\theta,x)\bigr) \end{aligned} \end{equation*} \notag $$

satisfy the relations on the derivatives up to order $n+1$ that are listed in Propositions 13 and 14, respectively.

This completes the proof of the theorem.

---

 |  |

 |

#### **Bibliography**

 |  |

 |

1. | A. A. Andronov, E. A. Leontovich, I. I. Gordon and A. G. Maier, Theory of bifurcations of dynamic systems on a plane, Halsted Press [John Wiley & Sons], New York–Toronto; Israel Program for Scientific Translations, Jerusalem–London, 1973, xiv+482 pp. [image: mathscinet] [51][image: mathscinet] [52][image: zmath] [53] |

2. | V. I. Arnol'd, S. M. Gusein-Zade and A. N. Varchenko, Singularities of differentiable maps, v. I, Monogr. Math., 82, The classification of critical points, caustics and wave fronts, Birkhäuser Boston, Inc., Boston, MA, 1985, xi+382 pp. [image: crossref] [54][image: mathscinet] [55][image: mathscinet] [56][image: zmath] [57][image: zmath] [58] |

3. | L. A. Cherkas, “Structure of a Poincaré map in the neighbourhood of a separatrix cycle of a perturbed analytic autonomous system in the plane”, Differ. Equ., 17:3 (1981), 321–328[image: mathnet] [59][image: mathscinet] [60][image: zmath] [61] |

4. | L. A. Cherkas, “The stability of singular cycles”, Differ. Equ., 4:6 (1972), 524–526[image: mathnet] [62][image: mathscinet] [63][image: zmath] [64] |

5. | A. V. Dukov, “Multiplicities of limit cycles appearing after perturbations of hyperbolic polycycles”, Sb. Math., 214:2 (2023), 226–245[image: mathnet] [65][image: crossref] [66][image: mathscinet] [67][image: zmath] [68][image: adsnasa] [69] |

6. | A. V. Dukov, “Bifurcations of the ‘heart’ polycycle in generic 2-parameter families”, Trans. Moscow Math. Soc., 2018, 209–229[image: mathnet] [70][image: crossref] [71][image: mathscinet] [72][image: zmath] [73] |

7. | A. V. Dukov, “Saddle connections”, Sb. Math., 215:11 (2024), 1523–1548[image: mathnet] [74][image: crossref] [75][image: mathscinet] [76][image: zmath] [77][image: adsnasa] [78] |

8. | D. Eisenbud, Commutative algebra. With a view toward algebraic geometry, Grad. Texts in Math., 150, Springer-Verlag, New York, 1995, xvi+785 pp. [image: crossref] [79][image: mathscinet] [80][image: zmath] [81] |

9. | Yu. Ilyashenko, Yu. Kudryashov and I. Schurov, “Global bifurcations in the two-sphere: a new perspective”, Invent. Math., 213:2 (2018), 461–506[image: crossref] [82][image: mathscinet] [83][image: zmath] [84][image: adsnasa] [85] |

10. | Yu. S. Il'yashenko and S. Yu. Yakovenko, “Finitely-smooth normal forms of local families of diffeomorphisms and vector fields”, Russian Math. Surveys, 46:1 (1991), 1–43[image: mathnet] [86][image: crossref] [87][image: mathscinet] [88][image: zmath] [89][image: adsnasa] [90] |

11. | Yu. Ilyashenko and S. Yakovenko, “Finite cyclicity of elementary polycycles in generic families”, Concerning the Hilbert 16th problem, Amer. Math. Soc. Transl. Ser. 2, 165, Adv. Math. Sci., 23, Amer. Math. Soc., Providence, RI, 1995, 21–95[image: crossref] [91][image: mathscinet] [92][image: zmath] [93] |

12. | M. A. Jebrane and A. Mourtada, “Cyclicté finie des lacets doublets non triviaux”, Nonlinearity, 7:5 (1994), 1349–1365[image: crossref] [94][image: mathscinet] [95][image: zmath] [96][image: adsnasa] [97] |

13. | V. Kaloshin, “The existential Hilbert 16-th problem and an estimate for cyclicity of elementary polycycles”, Invent. Math., 151:3 (2003), 451–512[image: crossref] [98][image: mathscinet] [99][image: zmath] [100][image: adsnasa] [101] |

14. | P. I. Kaleda and I. V. Shchurov (Schurov), “Cyclicity of elementary polycycles with fixed number of singular points in generic $k$ -parameter families”, St. Petersburg Math. J., 22:4 (2011), 557–571[image: mathnet] [102][image: crossref] [103][image: mathscinet] [104][image: zmath] [105] |

15. | A. G. Kurosh, Higher algebra, 19th ed., Lan', St Petersburg, 2013, 432 pp. [image: mathscinet] [106][image: zmath] [107]; English transl of 6th ed., Mir, Moscow, 1972, 428 pp. [image: mathscinet] [108][image: zmath] [109] |

16. | E. A. Leontovich, Creation of limit cycles from a separatrix of a saddle, D.Sc. dissertation, Gor'kii State University, Gor'kii, 1946 (Russian)  |

17. | B. Morin, “Formes canoniques des singularités d'une application différentiable”, C. R. Acad. Sci. Paris, 260 (1965), 5662–5665, 6503–6506[image: mathscinet] [110][image: mathscinet] [111][image: zmath] [112] |

18. | B. Malgrange, Ideals of differentiable functions, Tata Inst. Fundam. Res. Stud. Math., 3, Tata Inst. Fundam. Res., Bombay; Oxford Univ. Press, London, 1967, vii+106 pp. [image: mathscinet] [113][image: zmath] [114] |

19. | A. Mourtada, “Degenerate and non-trivial hyperbolic polycycles with two vertices”, J. Differential Equations, 113:1 (1994), 68–83[image: crossref] [115][image: mathscinet] [116][image: zmath] [117][image: adsnasa] [118] |

20. | A. Mourtada, Polycycles hyperboliques génériques à trois et à quatre sommets, These de Doctorat, Univ. Bourgogne, Dijon, 1990 [https://theses.fr/1990DIJOS028][119] |

21. | A. Mourtada, “Cyclicité finie des polycycles hyperboliques de champs de vecteurs du plan. Algorithme de finitude”, Ann. Inst. Fourier (Grenoble), 41:3 (1991), 719–753[image: crossref] [120][image: mathscinet] [121][image: zmath] [122] |

22. | V. Sh. Roitenberg, Nonlocal two-parameter bifurcations on surfaces, Kandidat dissertation, Yaroslavl' State Technical University, Yaroslavl', 2000, 187 pp. (Russian)  |

23. | J. W. Reyn, “Generation of limit cycles from separatrix polygons in the phase plane”, Geometrical approaches to differential equations (Scheveningen 1979), Lecture Notes in Math., 810, Springer, Berlin, 1980, 264–289[image: crossref] [123][image: mathscinet] [124][image: zmath] [125] |

24. | R. Roussarie, “On the number of limit cycles which appear by perturbation of separatrix loop of planar vector fields”, Bol. Soc. Brasil. Mat., 17:2 (1986), 67–101[image: crossref] [126][image: mathscinet] [127][image: zmath] [128] |

25. | S. I. Trifonov, “Cyclicity of elementary polycycles in generic smooth vector fields”, Proc. Steklov Inst. Math., 213 (1996), 141–199[image: mathnet] [129][image: mathscinet] [130][image: zmath] [131] |

26. | V. A. Zorich, Mathematical analysis, v. 1, 10th ed., Moscow Center for Continuous Mathematical Education, Moscow, 2019, xii+564 pp.; v. 2, 9th ed., 2019, xii+676 pp.; English transl. of 4th and 6th eds., Universitext, I, 2nd ed., Springer-Verlag, Berlin–Heidelberg, 2015, xx+616 pp. [image: crossref] [132][image: mathscinet] [133][image: zmath] [134]; II, 2016, xx+720 pp. [image: crossref] [135][image: mathscinet] [136][image: zmath] [137] |

---

**Citation:**A. V. Dukov, “Lower bound for the cyclicity of hyperbolic polycycles”, Sb. Math., 216:7 (2025), 902–947

**Citation in format ******[AMSBIB][138]**

`\Bibitem{Duk25}
\by A.~V.~Dukov
\paper Lower bound for the cyclicity of hyperbolic polycycles
\jour Sb. Math.
\yr 2025
\vol 216
\issue 7
\pages 902--947
\mathnet{http://mi.mathnet.ru/eng/sm10206}
\crossref{https://doi.org/10.4213/sm10206e}
\mathscinet{https://mathscinet.ams.org/mathscinet-getitem?mr=4961282}
\adsnasa{https://adsabs.harvard.edu/cgi-bin/bib_query?2025SbMat.216..902D}
\isi{https://gateway.webofknowledge.com/gateway/Gateway.cgi?GWVersion=2&SrcApp=Publons&SrcAuth=Publons_CEL&DestLinkType=FullRecord&DestApp=WOS_CPL&KeyUT=001582842800002}
\scopus{https://www.scopus.com/record/display.url?origin=inward&eid=2-s2.0-105017174789}
`

**Linking options:**
- https://www.mathnet.ru/eng/sm10206
- https://doi.org/10.4213/sm10206e
- https://www.mathnet.ru/eng/sm/v216/i7/p28

**Citing articles in Google Scholar:**[Russian citations][139], [English citations][140]
**Related articles in Google Scholar:**[Russian articles][141], [English articles][142]

 | [image: �������������� �������][image: Sbornik: Mathematics]

**Statistics & downloads**: |  |

Abstract page: | 768 |

Russian version PDF: | 1 |

English version PDF: | 81 |

Russian version HTML: | 25 |

English version HTML: | 446 |

References: | 167 |

First page: | 54 |

[143] [��� ����� QR-���?][144]

-->

 |

 |  |

Contact us:
 | [Terms of Use][145] | [Registration to the website][146] | [Logotypes][147] | &copy; [Steklov Mathematical Institute RAS][148], 2026 &copy; [Branch of Mathematical Sciences, Russian Academy of Sciences][149], 2026 -->  |


## Links

[1]: /php/archive.phtml?wshow=paper&jrnid=sm&paperid=10206&option_lang=rus
[2]: /php/archive.phtml?wshow=paper&jrnid=sm&paperid=10206&option_lang=eng
[3]: /?option_lang=eng
[4]: http://m.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=sm&paperid=10206&option_lang=eng
[5]: https://t.me/MathNetRu
[6]: https://www.youtube.com/channel/UC_fq8SDW37l86fdJxlprL1A
[7]: /ej.phtml?option_lang=eng
[8]: /php/person.phtml?option_lang=eng
[9]: /php/organisation.phtml?option_lang=eng
[10]: /php/conference.phtml?option_lang=eng
[11]: /php/seminars.phtml?option_lang=eng
[12]: /php/presentation.phtml?option_lang=eng
[13]: /poffice/mirefmodule.phtml?wshow=mirefmodule&option_lang=eng
[14]: /php/journal.phtml?jrnid=sm&wshow=details&option_lang=eng
[15]: /php/currentissue.phtml?jrnid=sm&option_lang=eng
[16]: /php/forthcom.phtml?jrnid=sm&wshow=forthcom&option_lang=eng
[17]: /php/archive.phtml?jrnid=sm&wshow=contents&option_lang=eng
[18]: /php/ifactor.phtml?jrnid=sm&wshow=IF_details&option_lang=eng
[19]: /supplement/authornotes/sm_eng.pdf?v=15122025
[20]: /supplement/authoragreement/sm.zip?v=16052025
[21]: /php/esubmission.phtml?jrnid=sm&wshow=snote&option_lang=eng
[22]: /php/search.phtml?jrnid=sm&tjrnid=sm&wshow=search&option_lang=eng
[23]: /php/searchrefs.phtml?option_lang=eng
[24]: /rss/rssRecentIssues.phtml?jrnid=sm&option_lang=eng
[25]: /rss/rssLastIssue.phtml?jrnid=sm&option_lang=eng
[26]: /rss/rssRecentIssues.phtml?mode=current&jrnid=sm&option_lang=eng
[27]: /rss/rssRecentIssues.phtml?mode=archive&jrnid=sm&option_lang=eng
[28]: /help.phtml?wshow=rss&option_lang=eng
[29]: http://www.mathjax.org/
[30]: http://www.crossref.org
[31]: /php/archive.phtml?wshow=contents&option_lang=eng&jrnid=sm&yl=2025&vl=216&series=0#showvolume
[32]: /php/contents.phtml?wshow=issue&jrnid=sm&year=2025&volume=216&issue=7&series=0&option_lang=eng
[33]: https://doi.org/10.4213/sm10206e
[34]: /eng/sm10154
[35]: /eng/sm10210
[36]: /php/person.phtml?option_lang=eng&personid=143554
[37]: /php/organisation.phtml?option_lang=eng&orgid=748
[38]: /php/getFT.phtml?jrnid=sm&paperid=10206&what=fullteng&option_lang=eng
[39]: /rus/sm10206
[40]: /php/getRefFromDB.phtml?jrnid=sm&paperid=10206&output=pdf&option_lang=eng
[41]: /php/getRefFromDB.phtml?jrnid=sm&paperid=10206&output=htm&option_lang=eng
[42]: https://basis-foundation.ru/
[43]: https://search.crossref.org/search/funders?id=501100012708&from_ui=yes
[44]: https://mathscinet.ams.org/mathscinet-getitem?mr=4961282
[45]: https://adsabs.harvard.edu/cgi-bin/bib_query?2025SbMat.216..902D
[46]: https://gateway.webofknowledge.com/gateway/Gateway.cgi?GWVersion=2&SrcApp=Publons&SrcAuth=Publons_CEL&DestLinkType=FullRecord&DestApp=WOS_CPL&KeyUT=001582842800002
[47]: https://www.scopus.com/record/display.url?origin=inward&eid=2-s2.0-105017174789
[48]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=37G15
[49]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=37C15
[50]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=37G20
[51]: http://www.ams.org/mathscinet-getitem?mr=0235228
[52]: http://www.ams.org/mathscinet-getitem?mr=0344606
[53]: https://zbmath.org/?q=an:0257.34001
[54]: https://doi.org/10.1007/978-1-4612-5154-5
[55]: http://www.ams.org/mathscinet-getitem?mr=0685918
[56]: http://www.ams.org/mathscinet-getitem?mr=0777682
[57]: https://zbmath.org/?q=an:0513.58001
[58]: https://zbmath.org/?q=an:0554.58001
[59]: http://mi.mathnet.ru/eng/de4208
[60]: http://mathscinet.ams.org/mathscinet-getitem?mr=610508
[61]: https://zbmath.org/?q=an:0503.34019
[62]: http://mi.mathnet.ru/eng/de373
[63]: http://mathscinet.ams.org/mathscinet-getitem?mr=228758
[64]: https://zbmath.org/?q=an:0164.10403|0235.34056
[65]: http://mi.mathnet.ru/eng/sm9747
[66]: https://doi.org/10.4213/sm9747e
[67]: http://mathscinet.ams.org/mathscinet-getitem?mr=4634805
[68]: https://zbmath.org/?q=an:1526.37063
[69]: https://adsabs.harvard.edu/cgi-bin/bib_query?2023SbMat.214..226D
[70]: http://mi.mathnet.ru/eng/mmo615
[71]: https://doi.org/10.1090/mosc/284
[72]: http://mathscinet.ams.org/mathscinet-getitem?mr=3881466
[73]: https://zbmath.org/?q=an:1425.34058
[74]: http://mi.mathnet.ru/eng/sm10096
[75]: https://doi.org/10.4213/sm10096e
[76]: http://mathscinet.ams.org/mathscinet-getitem?mr=4858983
[77]: https://zbmath.org/?q=an:8037677
[78]: https://adsabs.harvard.edu/cgi-bin/bib_query?2024SbMat.215.1523D
[79]: https://doi.org/10.1007/978-1-4612-5350-1
[80]: http://mathscinet.ams.org/mathscinet-getitem?mr=1322960
[81]: https://zbmath.org/?q=an:0819.13001
[82]: https://doi.org/10.1007/s00222-018-0793-1
[83]: http://mathscinet.ams.org/mathscinet-getitem?mr=3827206
[84]: https://zbmath.org/?q=an:1434.34036
[85]: http://adsabs.harvard.edu/cgi-bin/bib_query?2018InMat.213..461I
[86]: http://mi.mathnet.ru/eng/rm4566
[87]: https://doi.org/10.1070/RM1991v046n01ABEH002733
[88]: http://www.ams.org/mathscinet-getitem?mr=1109035
[89]: https://zbmath.org/?q=an:0744.58006|0729.58012
[90]: http://adsabs.harvard.edu/cgi-bin/bib_query?1991RuMaS..46....1I
[91]: https://doi.org/10.1090/trans2/165/01
[92]: http://mathscinet.ams.org/mathscinet-getitem?mr=1334338
[93]: https://zbmath.org/?q=an:0828.34021
[94]: https://doi.org/10.1088/0951-7715/7/5/005
[95]: http://mathscinet.ams.org/mathscinet-getitem?mr=1294547
[96]: https://zbmath.org/?q=an:0806.58041
[97]: http://adsabs.harvard.edu/cgi-bin/bib_query?1994Nonli...7.1349J
[98]: https://doi.org/10.1007/s00222-002-0244-9
[99]: http://mathscinet.ams.org/mathscinet-getitem?mr=1961336
[100]: https://zbmath.org/?q=an:1087.34013
[101]: http://adsabs.harvard.edu/cgi-bin/bib_query?2003InMat.151..451K
[102]: http://mi.mathnet.ru/eng/aa1197
[103]: https://doi.org/10.1090/S1061-0022-2011-01158-6
[104]: http://www.ams.org/mathscinet-getitem?mr=2768961
[105]: https://zbmath.org/?q=an:1230.34034
[106]: http://mathscinet.ams.org/mathscinet-getitem?mr=0070599
[107]: https://zbmath.org/?q=an:0103.25003
[108]: https://mathscinet.ams.org/mathscinet-getitem?mr=0945393
[109]: https://zbmath.org/?q=an:0237.13001
[110]: http://mathscinet.ams.org/mathscinet-getitem?mr=0180982
[111]: https://mathscinet.ams.org/mathscinet-getitem?mr=0190944
[112]: https://zbmath.org/?q=an:0178.26801
[113]: https://mathscinet.ams.org/mathscinet-getitem?mr=0212575
[114]: https://zbmath.org/?q=an:0177.17902
[115]: https://doi.org/10.1006/jdeq.1994.1114
[116]: http://mathscinet.ams.org/mathscinet-getitem?mr=1296161
[117]: https://zbmath.org/?q=an:0810.58027
[118]: http://adsabs.harvard.edu/cgi-bin/bib_query?1994JDE...113...68M
[119]: https://theses.fr/1990DIJOS028
[120]: https://doi.org/10.5802/aif.1271
[121]: http://mathscinet.ams.org/mathscinet-getitem?mr=1136601
[122]: https://zbmath.org/?q=an:0725.58032
[123]: https://doi.org/10.1007/BFb0089983
[124]: http://mathscinet.ams.org/mathscinet-getitem?mr=589213
[125]: https://zbmath.org/?q=an:0437.34025
[126]: https://doi.org/10.1007/BF02584827
[127]: http://mathscinet.ams.org/mathscinet-getitem?mr=0901596
[128]: https://zbmath.org/?q=an:0628.34032
[129]: http://mi.mathnet.ru/eng/tm1052
[130]: http://www.ams.org/mathscinet-getitem?mr=1632245
[131]: https://zbmath.org/?q=an:0906.34023|0878.34021
[132]: https://doi.org/10.1007/978-3-662-48792-1
[133]: http://www.ams.org/mathscinet-getitem?mr=3495809
[134]: https://zbmath.org/?q=an:1332.00009
[135]: https://doi.org/10.1007/978-3-662-48993-2
[136]: http://www.ams.org/mathscinet-getitem?mr=3445604
[137]: https://zbmath.org/?q=an:1331.00005
[138]: /poffice/amsbibpackage.phtml?wshow=amsbibpackage&option_lang=eng
[139]: https://scholar.google.com/scholar?q=link:https://www.mathnet.ru/rus/sm10206
[140]: https://scholar.google.com/scholar?q=link:https://www.mathnet.ru/eng/sm10206
[141]: https://scholar.google.com/scholar?q=related:https://www.mathnet.ru/rus/sm10206
[142]: https://scholar.google.com/scholar?q=related:https://www.mathnet.ru/eng/sm10206
[143]: https://www.mathnet.ru/eng/sm10206
[144]: /help.phtml?wshow=qrcode&option_lang=eng
[145]: /php/agreement.phtml?option_lang=eng
[146]: /php/registration.phtml?option_lang=eng
[147]: /supplement/logo_mathnet.zip
[148]: http://www.mi-ras.ru
[149]: http://omn.ras.ru
