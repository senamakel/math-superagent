<!-- source: https://ar5iv.labs.arxiv.org/html/math/0104140 | converted from HTML -->

[math/0104140] Quantitative theory of ordinary differential equations and tangential Hilbert 16 th problem

# Quantitative theory of ordinary differential equations
and tangential Hilbert 16 th {}^{\text{th}} problem The research was supported by the Israeli Science Foundation grant no. 18-00/1.

Sergei Yakovenko Address: Department of Mathematics
Weizmann Institute of Science
P.O.B. 26, Rehovot 76100
Israel Email: [yakov@wisdom.weizmann.ac.il WWW page: http://www.wisdom.weizmann.ac.il/~yakov/index.html][1]

Date: April 2001

###### Abstract.

These highly informal lecture notes aim at introducing and explaining several closely related problems on zeros of analytic functions defined by ordinary differential equations and systems of such equations. The main incentive for this study was its potential application to the tangential Hilbert 16th problem on zeros of complete Abelian integrals.

The exposition consists mostly of examples illustrating various phenomena related to this problem. Sometimes these examples give an insight concerning the proofs, though the complete exposition of the latter is mostly relegated to separate expositions.

###### 2000 Mathematics Subject Classification

Primary 34C07, 34C08, 34M35; Secondary 34C10, 34M15, 34M50, 14Q20, 32S65, 13E05

## Lecture I Hilbert 16th problem: Limit cycles, cyclicity, Abelian integrals

In the first lecture we discuss several possible relaxed formulations of the Hilbert 16th problem on limit cycles of vector fields and related questions from analytic functions theory.

### 1. Zeros of analytic functions

The introductory section presents several possible formulations of the question about the number of zeros of a function of one variable. All functions below are either real or complex analytic in their domains, eventually exhibiting singularities on their boundaries. We would like to stress that only *isolated*zeros of such functions are counted, so that by definition a function *identically vanishing*on an open set, *has no isolated zeros*there.

Exposition goes mostly by examples that are separated from each other by the symbol ◀ \blacktriangleleft. A few demonstrations terminate by the usual symbol ∎.

#### 1.1. Nonaccumulation and individual finiteness

A function f ⁡ ( t) f(t) real analytic on a finite open interval ( a, b) ⊂ ℝ (a,b)\subset{\mathbb{R}} may have an infinite number of *isolated*zeros on this interval only if they accumulate to the boundary points a, b a,b of the latter. Thus the *finiteness problem*of decision whether or not the given function f f has only finitely many zeros in its domain, is reduced to studying the boundary behavior of f f.

In particular, if f f is analytic also at the boundary points a, b a,b, then accumulation of infinitely many zeros to these points is impossible and hence f f has only finitely many roots on the interval ( a, b) (a,b). However, this strong condition of analyticity can be relaxed very considerably.

###### Example 1.1.

Assume that f ⁡ ( t) f(t) defined on ( 0, 1] (0,1] admits a *nontrivial*asymptotic expansion of the form

 | f ⁡ ( t) ∼ ∑ k = 0 ∞ c k ​ t r k as ​ t → 0 +, c k, r k ∈ ℝ, r 0 < r 1 < ⋯ < r k < ⋯ \begin{gathered}f(t)\sim\sum_{k=0}^{\infty}c_{k}t^{r_{k}}\qquad\text{ as }t\to 0^{+},\\ c_{k},r_{k}\in{\mathbb{R}},\qquad r_{0}<r_{1}<\cdots<r_{k}<\cdots\end{gathered} |  | (1.1) |

i.e., the difference between f f and a partial sum decreases faster than the next remaining term (the nontriviality means that not all c k c_{k} are zeros). Then in a sufficiently small semi-neighborhood of t = 0 t=0 the function f f has the same sign as the first nonzero coefficient c k c_{k} (since the functions t r t^{r} are nonvanishing on ℝ + {\mathbb{R}}_{+}), and hence roots of f f cannot accumulate to 0 0 implying that f f has only finitely many zeros on ( 0, 1] (0,1]. ∎

This example can be generalized for functions admitting asymptotic expansion in any system of *mutually comparable*functions f 1, f 2, … f_{1},f_{2},\dots, when f k + 1 = o ⁡ ( f k) f_{k+1}=o(f_{k}), provided that all of them keep constant sign near the boundary point(s).

###### Example 1.2.

Any function on ( 0, a] (0,a], a > 0 a>0, representable as a finite sum of the form

 | ∑ k, r h k ​ r ​ ( t) ​ t r ​ ln k − 1 ​ t, r ∈ ℝ, k ∈ ℕ, \sum_{k,r}h_{kr}(t)\,t^{r}\ln^{k-1}t,\qquad r\in{\mathbb{R}},\ k\in\mathbb{N}, |  |

with the functions h k ​ r ​ ( t) h_{kr}(t) real analytic on [0, a] [0,a] (i.e., including the boundary t = 0 t=0), cannot have infinitely many roots accumulating to t = 0 t=0. Indeed, the above sum expands in the monomials t r ​ ln k ​ t t^{r}\ln^{k}t, r ∈ ℝ r\in{\mathbb{R}}, k ∈ ℤ k\in\mathbb{Z}, that are naturally lexicographically ordered by their growth rates as t → 0 + t\to 0^{+}. Clearly, a function admitting an asymptotic expansion involving terms of such form, also possesses the finiteness property.

In this example we do not exclude the cases when the expansion is trivial. However, the *convergence*assumption on h k ​ r h_{kr} implies than in such cases the function is identically zero and has no isolated roots at all. ∎

#### 1.2. Parametric families of analytic functions, localization and cyclicity

Consider a function f = f ⁡ ( t, λ) = f ⁡ ( t, λ 1, …, λ n) f=f(t,\lambda)=f(t,\lambda_{1},\dots,\lambda_{n}) real analytic in an open domain U U of the space ℝ × ℝ n {\mathbb{R}}\times{\mathbb{R}}^{n} (this means that f f can be expanded in a converging Taylor series centered around any point in U U). The function f f can be considered as an analytic family of functions f λ = f ⁡ ( ⋅, λ) f_{\lambda}=f(\cdot,\lambda) defined in variable domains U λ = U ∩ ( ℝ × { λ }) ⊂ ℝ U_{\lambda}=U\cap({\mathbb{R}}\times\{\lambda\})\subset{\mathbb{R}} depending on λ \lambda.

Our nearest goal is to formulate the parametric finiteness property and establish simple sufficient conditions for it, similar to the non-parametric case.

###### Definition 1.

Let A A be a point set in ℝ {\mathbb{R}} or ℂ {\mathbb{C}}. Everywhere below we denote by #​ A \#A the number of *isolated*points (finite or not) of A A.

###### Definition 2.

We say that the analytic family f = { f λ }: U → ℝ f=\{f_{\lambda}\}\colon U\to{\mathbb{R}} possesses the *uniform finiteness property*, if the number of isolated zeros of all functions f λ f_{\lambda} in their respective domains U λ U_{\lambda} is uniformly bounded by a constant independent of λ \lambda.

In the same way as in the non-parametric context, it would be desirable to derive the uniform finiteness from some local properties of the family f f.

###### Definition 3.

The *cyclicity*of the family f f at a point ( t ∗, λ ∗) ∈ ℝ × ℝ n (t_{*},\lambda_{*})\in{\mathbb{R}}\times{\mathbb{R}}^{n} is the upper limit (finite or not)

 | 𝒩 f ( t ∗, λ ∗) = lim sup ε → 0 + sup ‖ λ − λ ∗ ‖ < ε #{ t ∈ U λ: | t − t ∗ | < ε, f λ ( t) = 0 }. \mathcal{N}_{f}(t_{*},\lambda_{*})=\limsup_{\varepsilon\to 0^{+}}\sup_{\|\lambda-\lambda_{*}\|<\varepsilon}\#\{t\in U_{\lambda}:|t-t_{*}|<\varepsilon,\ f_{\lambda}(t)=0\}. |  | (1.2) |

The term comes from the bifurcation theory (see below).

We stress again that the notation #​ { ⋯ } \#\{\cdots\} above means the number of isolated roots of f λ f_{\lambda}; the upper limit may be infinite even if all these numbers are finite.

If f λ ∗ ≢ 0 f_{\lambda_{*}}\not\equiv 0, then cyclicity of any family containing this function can be majorized in terms of only the function itself.

###### Example 1.3.

Suppose that f f is analytic at an interior point ( 0, 0) ∈ U (0,0)\in U, and f 0 ≢ 0 f_{0}\not\equiv 0. Then the cyclicity of f f at the origin is finite. Moreover, if t = 0 t=0 is an isolated root of *multiplicity*μ \mu, that is, f ⁡ ( t) = c ​ t μ + ⋯ f(t)=ct^{\mu}+\cdots, c ≠ 0 c\neq 0, then the cyclicity is no greater than μ \mu, that is, 𝒩 f ​ ( 0, 0) ⩽ μ \mathcal{N}_{f}(0,0)\leqslant\mu.

This follows from the fact that the μ \mu th derivative of f f is nonvanishing at the origin and hence at all sufficiently close points. But a function whose derivative f ( μ) ​ ( t) f^{(\mu)}(t) has a constant sign on an interval, cannot have more than μ \mu isolated zeros (even counted with multiplicities), as follows from the iterated Rolle theorem.

This example can be easily generalized for the case of *complex analytic functions*defined in a domain U ⊂ ℂ × ℂ n U\subset{\mathbb{C}}\times{\mathbb{C}}^{n}. In the above assumption f 0 ( μ) ​ ( 0) ≠ 0 f^{(\mu)}_{0}(0)\neq 0, the cyclicity of the family will be *exactly*μ \mu. To prove this, one can choose a small circle around the origin and apply the Rouché theorem to it. Another possibility would be to use the Weierstrass preparation theorem. ∎

###### Example 1.4.

If dim λ = 1 \dim\lambda=1, then any function analytic in ( t, λ) (t,\lambda) near t = t ∗ t=t_{*}, λ ∗ = 0 \lambda_{*}=0 can be expanded as f ⁡ ( t, λ) = f 0 ​ ( t) + λ ​ f 1 ​ ( t) + λ 2 ​ f 2 ​ ( t) + ⋯ f(t,\lambda)=f_{0}(t)+\lambda f_{1}(t)+\lambda^{2}f_{2}(t)+\cdots. If f ⁡ ( t, λ) ≢ 0 f(t,\lambda)\not\equiv 0, then for some finite k k necessarily f k ​ ( t) ≢ 0 f_{k}(t)\not\equiv 0, and after division by λ k \lambda^{k} the question about *isolated*zeros of f f can be reduced to the situation when f ⁡ ( t, 0) ≢ 0 f(t,0)\not\equiv 0, discussed earlier. In this case 𝒩 f ​ ( t ∗, 0) \mathcal{N}_{f}(t_{*},0) is no greater than the multiplicity of f k f_{k} at t ∗ t_{*}, where f k f_{k} is the first nonzero term in the expansion. ∎

This example illustrates an absolutely general fact about analytic functions (no matter, real or complex): the cyclicity 𝒩 f ​ ( t, λ) \mathcal{N}_{f}(t,\lambda) takes finite values at all *interior*points of the domain of analyticity U U.

###### Theorem 1

If f f is analytic at a point ( t, λ) ∈ ℝ × ℝ n (t,\lambda)\in{\mathbb{R}}\times{\mathbb{R}}^{n}, then 𝒩 f ​ ( t, λ) < + ∞ \mathcal{N}_{f}(t,\lambda)<+\infty.

This assertion can be derived from general finiteness properties of analytic sets, see [Loj91]. In the present form the theorem was formulated in connection with bifurcations of limit cycles, see [Rou98].

The proof of finiteness of 𝒩 f \mathcal{N}_{f} in the general multiparametric case requires some analytic techniques. One possibility—assuming for simplicity the point to be at the origin ( 0, 0) (0,0) —is to consider the expansion f ⁡ ( t, λ) = ∑ k ⩾ 0 a k ​ ( λ) ​ t k f(t,\lambda)=\sum_{k\geqslant 0}a_{k}(\lambda)t^{k} and the ideal in the ring ℜ \mathfrak{R} of analytic germs at ( ℝ n, 0) ({\mathbb{R}}^{n},0), generated by the coefficients a k ​ ( λ) a_{k}(\lambda). This ideal is called the *Bautin ideal*[Rou98]. Since the ring ℜ \mathfrak{R} is Noetherian, the Bautin ideal is in fact generated by a finite number of the coefficients a k a_{k}. If the germs a 1, …, a ν a_{1},\dots,a_{\nu} generate the Bautin ideal for some finite ν \nu, then one can show that the function f ⁡ ( t, λ) f(t,\lambda) can be represented as ∑ k = 0 ν a k ​ ( λ) ​ t k ​ h k ​ ( t, λ) \sum_{k=0}^{\nu}a_{k}(\lambda)t^{k}h_{k}(t,\lambda) with h k h_{k} analytic in t, λ t,\lambda and h k ​ ( 0, 0) ≠ 0 h_{k}(0,0)\neq 0, see [Rou98]. From this it is already easy to derive that 𝒩 f ​ ( 0, 0) ⩽ ν < ∞ \mathcal{N}_{f}(0,0)\leqslant\nu<\infty. Almost no modification is required to cover the complex analytic case as well: the only difference is that the usual Rolle cannot be applied to holomorphic non-real functions. The alternative is to use the complex Rolle theorem from [KY96]. An example of such use in a situation very similar to that discussed above, can be found in [Yak00].

#### 1.3. Finite cyclicity and uniform finiteness

The main reason for introducing the notion of cyclicity is the following very simple but basic theorem. In applications to bifurcation of limit cycles of analytic vector fields, it was observed by R. Roussarie [Rou88, Rou89, Rou98].

Let f: U → ℝ f\colon U\to{\mathbb{R}} as before be an analytic family of functions and 𝒩 f: U ¯ → ℕ ∪ { + ∞ } \mathcal{N}_{f}\colon\overline{U}\to\mathbb{N}\cup\{+\infty\} its cyclicity function.

###### Theorem 2

If the closure U ¯ \overline{U} is a compact subset of ℝ × ℝ n {\mathbb{R}}\times{\mathbb{R}}^{n}, and cyclicity 𝒩 f \mathcal{N}_{f} is finite everywhere on U ¯ \overline{U}, then the family f = { f λ } f=\{f_{\lambda}\} admits a uniform upper bound on the number of isolated roots:

 | sup λ #⁡ { t ∈ U λ: f λ ​ ( t) = 0 } < + ∞. \sup_{\lambda}\#\{t\in U_{\lambda}\colon f_{\lambda}(t)=0\}<+\infty. |  | (1.3) |

###### Proof.

By definition of the counting function, any point ( t ∗, λ ∗) ∈ U ¯ (t_{*},\lambda_{*})\in\overline{U} can be covered by a sufficiently small cube { | t − t ∗ | < ε, ‖ λ − λ ∗ ‖ < ε } \{|t-t_{*}|<\varepsilon,\ \|\lambda-\lambda_{*}\|<\varepsilon\} such that the number of isolated roots of f f in this cube is no greater than the number 𝒩 f ​ ( t ∗, λ ∗) \mathcal{N}_{f}(t_{*},\lambda_{*}) finite by the assumptions of the theorem. It remains only to choose a finite subcover of the compact U ¯ \overline{U} and add together the corresponding cyclicities. ∎

Theorem 1 asserts that the cyclicity is automatically finite at all *interior*points of the domain U U, so it is again the boundary behavior of a given parametric family that determines whether this family possesses the uniform finiteness or not.

#### 1.4. Terminology: individual *vs*. existential finiteness problems

The arguments proving finiteness of the number of isolated zeros of an individual analytic function f ⁡ ( t) f(t) and the arguments establishing uniform boundedness of this number for parametric families of such functions, are both of the same purely existential nature: neither of them gives any way to *compute*or even *estimate from above*these numbers. However, the parametric claim is definitely stronger than the assertion concerning individual functions of this family (one can easily construct families in which the number of isolated zeros is always finite but not uniformly bounded).

We shall repeatedly encounter the problem on bounding the number of isolated zeros for various classes of analytic functions and finite parameter families of such functions, mostly defined by ordinary differential equations with polynomial right hand sides. For each class one can pose several finiteness-type problems in the increasing order of strength (the gap in the enumeration will be explained below).

1. 1.

*Individual finiteness problem*. Prove that each function from the family possesses only finitely many isolated zeros.

2. 2.

*Existential ( uniform) finiteness problem*. Prove that the number of isolated roots is uniformly bounded over all functions from this family.

3. 4.

*Constructive finiteness problem*. Find an explicit upper bound for the number of isolated roots or at least find an algorithm for computing this bound.

The adjective “existential” stresses the difference between the last two types of problems, whereas the adjective “uniform” will be used to underscore the difference between the first two assertions.

###### Example 1.5.

Consider the class of parametric families of functions real analytic on [0, 1] [0,1] depending analytically on parameters from [0, 1] n ⊂ ℝ n + 1 [0,1]^{n}\subset{\mathbb{R}}^{n+1} (in both cases including the boundary). As was just explained, the individual finiteness for functions from this class follows from the uniqueness theorem for analytic functions while the existential (uniform) finiteness theorem (Theorem 2) follows from Theorem 1. ∎

###### Example 1.6.

Polynomials in one variable of degree ⩽ d \leqslant d for any finite d d form a finite-parameter family. Constructive finiteness theorem for this “toy” class of functions is known as the Principal theorem of Algebra. Less trivial examples can be found in § 8. ∎

#### 1.5. Constructive finiteness

In practice the existential finiteness is always derived from finite cyclicity using Theorem 2. Both steps (finite cyclicity and its globalization) use arguments of existential nature. However, at least theoretically it may happen that the function 𝒩 f \mathcal{N}_{f} is explicitly bounded at all points of the closure U ¯ \overline{U}. This still would not allow to compute explicitly the global uniform bound on the number of isolated zeros of f f, but such *local constructive finiteness*would be clearly a much stronger assertion concerning the family f f. The corresponding finiteness problem occupies an intermediate place between existential and (global) constructive finiteness problems.

1. 3.

*Constructive finite cyclicity problem*. Find an explicit majorant for the counting function 𝒩 f \mathcal{N}_{f}.

Yet it should be remarked that in order to discuss the constructive finiteness problems (global or local), the family should be defined by some algebraic data, otherwise computability does not make sense. We postpone discussion of these question until § 8.

###### Example 1.7.

Let F 1 ​ ( t), …, F n ​ ( t) F_{1}(t),\dots,F_{n}(t) be analytic functions (real or complex), satisfying together a system of polynomial ordinary differential equations

 | d ​ F i d ​ t = ∑ k + | α | ⩽ d c i ​ k ​ α t k F α, F α = F 1 α 1 ⋯ F n α n, i = 1, …, n, \frac{dF_{i}}{dt}=\sum_{k+|\alpha|\leqslant d}c_{ik\alpha}\,t^{k}F^{\alpha},\qquad F^{\alpha}=F_{1}^{\alpha_{1}}\cdots F_{n}^{\alpha_{n}},\quad i=1,\dots,n, |  | (1.4) |

assuming the degree d d and all coefficients c i ​ k ​ α c_{ik\alpha} (real or complex) known. Then for any finite m ∈ ℕ m\in\mathbb{N} the polynomial combinations of these functions constitute a finite-parametric family: the coefficients λ = { λ k ​ α: k + | α | ⩽ m } \lambda=\{\lambda_{k\alpha}\colon k+|\alpha|\leqslant m\} of the polynomial combinations f ⁡ ( t, λ) = ∑ k + | α | ⩽ m λ k ​ α ​ t k ​ F α ​ ( t) f(t,\lambda)=\sum_{k+|\alpha|\leqslant m}\lambda_{k\alpha}\,t^{k}F^{\alpha}(t) being the parameters. The domain of this family is clearly the Cartesian product of the linear space of the appropriate dimension and the common domain U U of the functions F i F_{i}. Though solutions of polynomial systems may blow up in finite time, we will assume for simplicity that all F i F_{i} are analytic on the compact closure U ¯ \overline{U} of U U.

In these assumptions both individual and existential finiteness are guaranteed by Theorem 2 which, as usual, does not provide any bound on the number of zeros. Yet using algebraicity of the system defining these functions, one can derive explicit bounds. In [Gab99] A. Gabrielov found an upper bound for the maximal *order of zero*(*multiplicity of a root*) that a nontrivial (not identically equal to zero) function from the family f m f_{m} may have, in terms of n, d n,d and m m. The answer is given by an expression polynomial in the degrees d, m d,m and exponential in n n (the dimension of the system). Y. Yomdin in [Yom98] derived from this multiplicity bound the corresponding *cyclicity bound*, using arguments involving Bautin ideal and its generators (a subtle generalization of the approach outlined in discussion of Theorem 1). This combination of the two results gives a complete solution for the constructive finite cyclicity problem for polynomial combinations of functions defined by systems of polynomial ordinary differential equations. ∎

The corresponding global problem was settled by D. Novikov and the author [NY97, NY99b]. Unlike the bound for cyclicity, the bound for the total number of zeros depends on the size of the domain ρ = max t ∈ U ⁡ | t | \rho=\max_{t\in U}|t| where they are counted and, rather naturally, on the magnitude of the coefficients R = max i, k, α ⁡ | c i ​ k ​ α | R=\max_{i,k,\alpha}|c_{ik\alpha}| of the system ( 1.4). The answer is polynomial in ρ, R \rho,R but as a function of the other (integer) parameters n, m, d n,m,d is a tower of height 4 4. The detailed explanation of this result is postponed until § 11.

#### 1.6. Paradigm

All the above results on elementary properties of analytic functions and their parametric families, were mentioned in order to set out a paradigm that will be used when discussing much more complicated parallel problems on limit cycles of analytic and polynomial vector fields. In order to make the similarity transparent, all finiteness theorems can be organized in the form of a table with finiteness types labeling the rows and corresponding theories represented by different columns. The first column describes theory of analytic functions as in Example 1.5 above. Cells of this column list the key theorems ensuring each type of finiteness types.

The following section § 2 describes some known results fitting the second column of Table 1: the strongest form of the Hilbert 16th problem should occupy the place where the question marks appear. The parallel non-constructive results for Abelian integrals will be discussed in § 4: their complexity level can be described as intermediate between relatively elementary theorems on analytic functions and transcendentally difficult counterparts on limit cycles.

###### Remark.

In general, the results in the lower part of the table are more difficult than those from the upper part. However, this is not true when comparing existential finiteness with constructive finite cyclicity: while the former deals with boundary behavior, the latter addresses the issues of completely different nature that can be (and indeed sometimes are) simpler. In particular, this is the case with Abelian integrals, where the bound for multiplicity can be be relatively easily obtained, see [Mar91] and § 6.5 below.

 | Category of objects |

Finiteness type \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Finiteness}\\ \text{\bf type}\end{matrix} | Functions analytic on a compact \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\it Functions}\\ \text{\it analytic}\\ \text{\it on a compact}\end{matrix} | Limit cycles of polynomial vector fields \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\it Limit cycles}\\ \text{\it of polynomial}\\ \text{\it vector fields}\end{matrix} | Abelian integrals \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\it Abelian}\\ \text{\it integrals}\end{matrix} |

Individual finiteness \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Individual}\\ \text{\bf finiteness}\end{matrix} | uniqueness theorem \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{uniqueness}\\ \text{theorem}\end{matrix} | Ilyashenko (1991)– Ecalle (1992) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{Ilyashenko (1991)--}\\ \text{Ecalle (1992)}\end{matrix} | easy exercise see § 4.1 \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{easy exercise}\\ \text{see \lx@sectionsign\ref{sec:AI-ind}}\end{matrix} |

Existential finiteness \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Existential}\\ \text{\bf finiteness}\end{matrix} | finite cyclicity Theorems 1 and 2, see § 1.3 \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{finite cyclicity}\\ \text{Theorems \ref{thm:fcyc-anal}}\\ \text{and~\ref{thm:finite-cyclicity}, see \lx@sectionsign\ref{sec:finite-cyclicity}}\end{matrix} | in progress for quadratic case (121 polycycles [DRR94]) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{in progress for}\\ \text{quadratic case (121}\\ \text{polycycles \cite[cite]{[\@@bibref{}{drr:list}{}{}]})}\end{matrix} | Varchenko– Khovanskii (1985) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{Varchenko--}\\ \text{Khovanskii}\\ \text{(1985)}\end{matrix} |

Constructive finite cyclicity \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Constructive}\\ \text{\bf finite}\\ \text{\bf cyclicity}\end{matrix} | Gabrielov– Yomdin (1998) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{Gabrielov--}\\ \text{Yomdin (1998)}\end{matrix} | known for k -generic elementary and few other polycycles \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{known for $k$-generic }\\ \text{elementary and few}\\ \text{other polycycles}\end{matrix} | Mardešić [Mar91] (multiplicity) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{Marde\v{s}i\'{c}}\\ \text{\cite[cite]{[\@@bibref{}{mardesic:multiplicity}{}{}]}}\\ \text{(multiplicity)}\end{matrix} |

Constructive finiteness \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Constructive}\\ \text{\bf finiteness}\end{matrix} | Novikov– Yakovenko (1999) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{Novikov--}\\ \text{Yakovenko}\\ \text{(1999)}\end{matrix} | ??? (nothing in view) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf???}\\ \text{(nothing in view)}\end{matrix} | see Table 2 |

Table 1. Various flavors of the Hilbert 16th problem

### 2. Limit cycles of planar vector fields

This section briefly surveys a few known general finiteness results for limit cycles of vector fields.

#### 2.1. Basic facts

A polynomial differential equation

 | x ˙ = P ( x, y), y ˙ = Q ( x, y), P, Q ∈ ℝ [x, y] \dot{x}=P(x,y),\quad\dot{y}=Q(x,y),\qquad P,Q\in{\mathbb{R}}[x,y] |  | (2.1) |

defines a vector field on the real plane ℝ 2 {\mathbb{R}}^{2}, spanning the distribution (line field) with singularities given by null spaces { ω = 0 } \{\omega=0\} of the polynomial Pfaffian form Ω = Q ​ d ​ x − P ​ d ​ y \Omega=Q\,dx-P\,dy. If P P and Q Q have a nontrivial greatest common divisor R R, then this distribution on the Zariski open set { R ≠ 0 } \{R\neq 0\} coincides with that given by the form R − 1 ​ Ω R^{-1}\Omega and hence extends analytically to all but finitely many points of the curve { R = 0 } \{R=0\}. For the same reasons the distribution extends onto the infinite line ℝ ​ P 1 {\mathbb{R}}P^{1} on the projective plane ℝ ​ P 2 {\mathbb{R}}P^{2}, having at most finitely many isolated singularities on the latter after cancellation of an eventual common factor. In other words, when dealing with an individual differential equation ( 2.1), one can assume that the corresponding distribution has only *isolated singularities*. It is sometimes convenient to talk about *foliations with isolated singularities*defined by the distribution { Ω = 0 } \{\Omega=0\} on ℝ ​ P 2 {\mathbb{R}}P^{2}.

A limit cycle γ \gamma by definition is an isolated periodic trajectory of ( 2.1). Limit cycles of a vector field can be tracked by their intersections with analytic arcs transversal to the field. More precisely, near any intersection p = γ ∩ σ p=\gamma\cap\sigma of a periodic orbit γ \gamma with a transversal arc σ \sigma, the Poincaré first return map Δ σ \Delta_{\sigma}, the transport along integral curves until the next intersection with the transversal, is defined. It has p p as a fixed point, *isolated*if γ \gamma is a limit cycle. Choosing an analytic chart t t on σ \sigma allows to describe p p as a root of the *displacement function*f ⁡ ( t) = Δ σ ​ ( t) − t f(t)=\Delta_{\sigma}(t)-t. All nearby limit cycles must intersect σ \sigma by points that are isolated roots of the displacement f f.

From the general theorem on analytic dependence of solutions of differential equations on initial conditions and parameters, the displacement function f f is analytic near p p. As a corollary, we conclude that an infinite number of limit cycles (corresponding to isolated roots of the displacement function) cannot accumulate to a periodic orbit of the field. In a similar way, if the vector field depends analytically on parameters λ \lambda and exhibits a periodic orbit γ \gamma (isolated or not) for one value λ ∗ \lambda_{*} of the parameters, then there exists a finite upper bound for the number of limit cycles in a small annulus around γ \gamma, uniform over all values of λ \lambda sufficiently close to λ ∗ \lambda_{*}.

In general, one transversal cannot “serve” all limit cycles, and there is no natural way to define the maximal domain of the Poincaré return map unambiguously and globally. However, the discussion in § 1 suggests that it is the boundary behavior that is important for counting isolated zeros of the displacement.

#### 2.2. Polycycles and limit periodic sets

Instead of trying to reduce formally the global investigation of limit cycles to that of return maps for one or several transversal arcs, it is better to study the cycles (compact leaves of the foliation) themselves.

For the non-parametric case, the analogue of a boundary point of the domain of the Poincaré return map is a *polycycle*, an invariant set consisting of one or more *singular points*of the vector field, and a number of bi-infinite trajectories connecting them in a cyclic order (repetitions of singular points allowed). More accurately, one can show that the only sets that can appear as Hausdorff limits of periodic orbits of a vector field having only isolated singular points, are polycycles.

In the parametric case one cannot assume anymore that singularities of the foliation are isolated (the polynomials P P and Q Q may have common factors for some values of the parameters and be mutually prime for the rest). Still one can show [FP86] that the Hausdorff limit of a family of limit cycles occurring for converging values of the parameters, must be a *limit periodic set*(also known as *graphic*), the object differing from a polycycle in only one instance, namely, it may contain analytic arcs of non-isolated singularities.

#### 2.3. Individual finiteness theorem and finite cyclicity

Following the paradigm set out in § 1.3, one can easily formulate counterparts of the individual and existential finiteness problems for limit cycles for vector fields. The individual finiteness theorem (known also as the *Dulac conjecture*after being believed for some 60 years to be the *Dulac theorem*) asserts that *any polynomial vector field can have only finitely many limit cycles*. This is an easy corollary to the highly nontrivial *nonaccumulation theorem*asserting that limit cycles of an analytic vector field cannot accumulate to any polycycle. The latter assertion is the most spectacular and the most general fact established so far in connection with the Hilbert 16th problem, that was independently proved by Ilyashenko [Ily91] and Ecalle [Eca92] by totally different methods. This is a typical example of an assertion on boundary behavior of the Poincaré map.

###### Remark.

It would be appropriate to notice here that Dulac reduced the individual finiteness problem to the situation discussed in Example 1.1. However, he did not notice that the expansion ( 1.1) (only involving logarithms) may well be *trivial*, hence not allowing for so easy treatment. It took both Ilyashenko and Ecalle hundreds of pages to prove that even in this apparently highly degenerate case the nonaccumulation still holds.

The existential finiteness problem for polynomial vector fields arises very naturally, since coefficients of the polynomials P, Q P,Q can be treated as parameters. These parameters can be considered as ranging over the compact projective space of a suitable dimension, since simultaneous multiplication of both P P and Q Q by a nonzero constant does not alter the phase portrait. Existence of a uniform upper bound for the number of limit cycles would mean that *for any degree d d the number of limit cycles for a polynomial vector field of degree ⩽ d \leqslant d is bounded by some number ℋ ⁡ ( d) \mathcal{H}(d) depending only on d d*. According to the Roussarie localization theorem (an analog of Theorem 2 for limit cycles, see [Rou88]), it would be sufficient to prove that any limit periodic set has finite cyclicity within the universal family of polynomial vector fields of degree ⩽ d \leqslant d.

However, even for the simplest nontrivial case of quadratic ( d = 2 d=2) vector fields, this is not proved. Dumortier, Roussarie and Rousseau composed in [DRR94] a list of 121 graphics occurring for quadratic vector fields, and reduced the existential finiteness problem to proving that all these graphics have finite cyclicity. First several cases were studied in the same paper by applying relatively standard tools of bifurcation theory. Since then many other considerably more delicate cases were investigated and their finite cyclicity proved, so that one can hope that the existential finiteness will be ultimately established in the quadratic case. At the same time it is clear that such type of case study is even theoretically impossible for higher degree cases.

On this background the perspective of *computing*or even *explicitly majorizing*the “*Hilbert number*” ℋ ⁡ ( d) \mathcal{H}(d), which is the strongest (constructive) form of the initial Hilbert’s question “on the number and position of limit cycles” [Hil00], looks very remote.

#### 2.4. Digression: constructive solutions of localized problems

As was already noted above, though finiteness of cyclicity for all graphics is not proved, one can independently work towards obtaining constructive bounds for cyclicity in cases when its finiteness is already known. This is possible since cyclicity is very strongly depending on the types of singular points lying on the polycycle (resp., the limit periodic set).

For example, if all singular points on the polycycle are elementary (having non-nilpotent linear parts), then cyclicity of *generic*r r -parametric families can be estimated in terms of the number r r of independent parameters. The corresponding algorithm was suggested by Ilyashenko and the author [IY95b] and improved to a very concise and explicit answer by Kaloshin [IK99]. Some other cases of polycycles (usually carrying one or at most two singular points) also have known cyclicity, see [KS95] and references therein for a synopsis. These results are partly reflected in Table 1.

Yet if the problem is formulated for polynomial vector fields and the bounds are required to be given in terms of the degree, the problem immediately becomes transcendentally difficult. Almost nothing is known, for example, on the maximal multiplicity of a (nonsingular) limit cycle of a polynomial vector field. Cyclicity of singular points is a considerably more “algebraic” problem. For example, when the linear part of the singularity is a nondegenerate rotation, a polynomial algorithm can be suggested which stops at a step number N N if and only if the cyclicity of a singular point is N N. However, the running time of this algorithm is absolutely unknown (see the discussion of a similar problem in § 3.3). Recently M. Briskin, J.-P. Françoise and Y. Yomdin treated in details one problem on Abel equations that may give a clue to understanding some of the phenomena, see e.g., [BFY98a, BFY98b].

The following section describes one very important case when the local (with respect to parameters) constructive finiteness can be reduced to an algebraic context.

### 3. Abelian integrals: appearance and basic properties

Consider a family of analytic vector fields X λ X_{\lambda} analytically depending on parameters λ ∈ ( ℝ n, 0) \lambda\in({\mathbb{R}}^{n},0) (we consider only a sufficiently small neighborhood of the origin in the parameter space). Assume that for λ = 0 \lambda=0 the vector field X 0 X_{0} possesses a limit cycle γ 0 \gamma_{0} of multiplicity μ < + ∞ \mu<+\infty. As illustrated by Example 1.3, the cyclicity of γ 0 \gamma_{0} in this case is at most μ \mu, being thus explicitly bounded.

The problem becomes less trivial if the field X 0 X_{0} possesses an annulus filled by nonisolated periodic orbits, γ 0 \gamma_{0} being one of them. Vector fields with this property are called integrable or conservative. Such behavior, very unlikely for an arbitrary analytic family, becomes an event of finite codimension when *polynomial*vector fields are considered.

To study bifurcations of limit cycles in perturbations of conservative systems, an approach described in Example 1.4 can be used.

#### 3.1. Perturbation of polynomial vector fields

Assume that the form Ω = Q ​ d ​ x − P ​ d ​ y \Omega=Q\,dx-P\,dy defining the polynomial distribution { Ω = 0 } \{\Omega=0\}, is *exact*: Ω = d ​ H \Omega=dH, where H = H ⁡ ( x, y) H=H(x,y) is a bivariate polynomial in two variables. The corresponding vector field is then a Hamiltonian one,

 | x ˙ = − ∂ H ∂ y, y ˙ = ∂ H ∂ x. \dot{x}=-\frac{\partial H}{\partial y},\quad\dot{y}=\frac{\partial H}{\partial x}. |  | (3.1) |

with H H being its *Hamiltonian function*or simply the *Hamiltonian*.

Since d ​ H dH vanishes on the null spaces of the distribution { Ω = 0 } \{\Omega=0\}, each leaf of the corresponding foliation belongs to a level curve of H H. In particular, a periodic orbit must be a compact oval of some level curve and hence all nearby close leaves must be also closed. Hence a Hamiltonian vector field cannot have limit cycles: the corresponding Poincaré return map is identity and the displacement identically zero.

Consider the following *one-parameter family*of polynomial distributions, perturbing the Hamiltonian distribution:

 | d H + ε ω = 0, ε ∈ ( ℝ 1, 0), ω = p d x + q d y, p, q ∈ ℝ [x, y]. dH+\varepsilon\omega=0,\qquad\varepsilon\in({\mathbb{R}}^{1},0),\ \omega=p\,dx+q\,dy,\ p,q\in{\mathbb{R}}[x,y]. |  | (3.2) |

The polynomial 1-form ω \omega can be arbitrary.

Consider an analytic segment σ \sigma transversal to the oval γ ( t ∗) ⊂ { H = t ∗ } \gamma(t_{*})\subset\{H=t_{*}\}. This transversality implies that the Hamiltonian H H restricted on σ \sigma, gives an analytic chart t t on the latter. On the other hand, for all t t sufficiently close to t ∗ t_{*}, one can unambiguously choose an oval γ ( t) ⊂ { H = t } \gamma(t)\subset\{H=t\} so that γ ⁡ ( t) \gamma(t) tends to γ ⁡ ( t ∗) \gamma(t_{*}) as t → t ∗ t\to t_{*}, e.g., in the sense of Hausdorff distance (this choice in a more broad context is discussed below, in § 5).

The following elementary computation gives the *first variation*of the displacement function f ⁡ ( t, ε) = Δ σ ​ ( t) − t f(t,\varepsilon)=\Delta_{\sigma}(t)-t with respect to the small parameter ε \varepsilon at ε = 0 \varepsilon=0.

###### Lemma 1 (Poincaré–Pontryagin)

 | f ( t, 0) ≡ 0, d d ​ ε | ε = 0 f ( t, ε) = − ∮ γ ⁡ ( t) ω. f(t,0)\equiv 0,\quad\left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0}f(t,\varepsilon)=-\oint_{\gamma(t)}\omega. |  | (3.3) |

###### Proof.

Consider the leaf (analytic curve) of the foliation { d H + ε ω = 0 } \{dH+\varepsilon\omega=0\} passing through the point t t on the transversal, and denote by γ ⁡ ( t, ε) \gamma({t,\varepsilon}) the (oriented) segment of this leaf between the the initial point and the next intersection with σ \sigma. By definition of the chart t t, the displacement function measured in the chart t t, is the difference of H H between the endpoints of γ ⁡ ( t, ε) \gamma(t,\varepsilon), hence

 | f ⁡ ( t, ε) = ∫ γ ⁡ ( t, ε) 𝑑 H f(t,\varepsilon)=\int_{\gamma({t,\varepsilon})}dH |  |

(the equality is exact). The form d ​ H + ε ​ ω dH+\varepsilon\omega vanishes on γ ⁡ ( t, ε) \gamma({t,\varepsilon}), therefore the integral above is equal to the integral of − ε ​ ω -\varepsilon\omega along γ ⁡ ( t, ε) {\gamma({t,\varepsilon})} and, since γ ⁡ ( t, ε) \gamma({t,\varepsilon}) converges uniformly to the *closed*curve γ ( t) = γ ( t, 0) ⊂ { H = t } \gamma(t)=\gamma({t,0})\subset\{H=t\} as ε → 0 \varepsilon\to 0, we conclude that

 | f ( t, ε) = − ε ∮ γ ⁡ ( t) ω + o ( ε) as ε → 0, f(t,\varepsilon)=-\varepsilon\oint_{\gamma(t)}\omega+o(\varepsilon)\qquad\text{as }\varepsilon\to 0, |  |

with o ⁡ ( ε) o(\varepsilon) uniform and analytic in t t and ε \varepsilon. This yields the formula ( 3.3) for the derivative. ∎

Recall that an *Abelian integral*is the integral of a polynomial 1-form along any algebraic oval (i.e., the closed oval of a real algebraic curve). Clearly, Abelian integrals can be considered as *functions of the parameters*, the coefficients of the form and the algebraic equation defining the curve. However, in applications to the bifurcation theory, one coefficient is clearly distinguished and plays the role of the argument, while others are treated as “true” parameters. Making a minor abuse of language, we shall always consider Abelian integrals as analytic functions in the following sense.

###### Definition 4.

A *real*Abelian integral corresponding to a Hamiltonian H H and a polynomial 1-form ω = p ⁡ ( x, y) ​ d ​ x + q ⁡ ( x, y) ​ d ​ y \omega=p(x,y)\,dx+q(x,y)\,dy, H, p, q ∈ ℝ ⁡ [x, y] H,p,q\in{\mathbb{R}}[x,y], is a multivalued function I ⁡ ( t) I(t) of the real variable t t defined by integration of ω \omega over a real oval γ ⁡ ( t) \gamma(t) of the algebraic curve { H ( x, y) = t } ⊂ ℝ 2 \{H(x,y)=t\}\subset{\mathbb{R}}^{2}.

The reason for multivaluedness is obvious, since there can be several ovals lying on the same level curve { H = t } \{H=t\}. In § 5 we describe the branching of the Abelian integral I ⁡ ( t) I(t) after analytic continuation into the complex domain. This complexification of Abelian integrals explains connections between different branches of these functions, see § 5.

#### 3.2. Bifurcation of limit cycles from periodic orbits of Hamiltonian systems

Limit cycles appearing in the one-parametric system ( 3.2), correspond to isolated zeros of the displacement function f ⁡ ( t, ε) f(t,\varepsilon), real analytic in t t and ε \varepsilon, whose first Taylor term was just computed:

 | f ( t, ε) = I 0 ( t) + ε I 1 ( t) + ε 2 I 2 ( t) + ⋯, I 0 ( t) ≡ 0, I 1 ( t) = − ∮ γ ⁡ ( t) ω. f(t,\varepsilon)=I_{0}(t)+\varepsilon I_{1}(t)+\varepsilon^{2}I_{2}(t)+\cdots,\quad I_{0}(t)\equiv 0,\ I_{1}(t)=-\oint_{\gamma(t)}\omega. |  | (3.4) |

This is exactly the situation treated in Example 1.4: if the first variation is nontrivial, I 1 ​ ( t) ≢ 0 I_{1}(t)\not\equiv 0, then the number of isolated roots of f ⁡ ( t, ε) f(t,\varepsilon) on any interval of analyticity (i.e., not containing singularities at the endpoints) is no greater than the number of (necessary isolated) roots of the Abelian integral I 1 I_{1} defined by the polynomial H H and the polynomial 1-form ω \omega. Computing or majorizing the number of isolated zeros of Abelian integrals is the central theme of these notes: under the name *Tangential Hilbert problem*it is discussed below.

The first variation method does not work if I 1 ​ ( t) ≡ 0 I_{1}(t)\equiv 0. In this case higher variations I k ​ ( ⋅) I_{k}(\cdot), k = 2, 3, … k=2,3,\dots, have to be computed and analyzed.

The computation of higher variations is relatively simple. It follows from results of Ilyashenko [Ily69] and Gavrilov [Gav98] that for almost all Hamiltonians H H (and certainly for Hamiltonians with isolated critical points, pairwise different critical values and transversal to infinity as defined below in § 6), the condition I 1 ≡ 0 I_{1}\equiv 0 implies that there exist two polynomials G, F ∈ ℝ ⁡ [x, y] G,F\in{\mathbb{R}}[x,y] such that

 | ω = G ⁡ ( x, y) ​ d ​ H + d ​ F ​ ( x, y), hence d ​ ω = d ​ G ∧ d ​ H. \omega=G(x,y)\,dH+dF(x,y),\quad\text{hence}\quad d\omega=dG\land dH. |  | (3.5) |

(the inverse statement is obvious).

###### Example 3.1 (see [Fra96]).

Consider the Hamiltonian H ⁡ ( x, y) = 1 2 ​ ( x 2 + y 2) H(x,y)=\tfrac{1}{2}(x^{2}+y^{2}). In the complex coordinates z = x + i ​ y z=x+iy, z ¯ = x − i ​ y \bar{z}=x-iy we have H = 1 2 ​ z ​ z ¯ H=\tfrac{1}{2}z\bar{z}. One can easily verify that the polynomial 1-form ω = A ⁡ ( z, z ¯) ​ d ​ z + B ⁡ ( z, z ¯) ​ d ​ z ¯ \omega=A(z,\bar{z})\,dz+B(z,\bar{z})\,d\bar{z} has identically vanishing integral over the circles { H = t } \{H=t\} if and only if the differential d ​ ω = ( − A z ¯ + B z) ​ d ​ z ∧ d ​ z ¯ d\omega=(-A_{\bar{z}}+B_{z})\,dz\land d\bar{z} contains no monomial terms of the form ( z ​ z ¯) k ​ d ​ z ∧ d ​ z ¯ (z\bar{z})^{k}\,dz\land d\bar{z}. Any other monomial can obviously be represented in the form ( 3.5): z i ​ z ¯ j ​ d ​ z ∧ d ​ z ¯ = d ​ G ∧ d ​ H z^{i}\bar{z}^{j}\,dz\land d\bar{z}=dG\land dH with G = z i ​ z ¯ j / ( i − j) G={z^{i}\bar{z}^{j}}/{(i-j)}. ∎

Using the representation ( 3.5), the formula for the second variation of the displacement map can be expressed as an Abelian integral again.

###### Lemma 2 ( [Yak95, Fra96])

Assume that for the perturbation ( 3.2) the first variation vanishes identically, so that

 | I 1 ​ ( t) = ∮ γ ⁡ ( t) ω ≡ 0, I_{1}(t)=\oint_{\gamma(t)}\omega\equiv 0, |  |

and G G is any polynomial satisfying the condition ( 3.5). Then the second variation of the displacement map is given by the following Abelian integral,

 | I 2 ( t) = d 2 d ​ ε 2 | ε = 0 f ( t, ε) = − ∮ γ ⁡ ( t) G ω. I_{2}(t)=\left.\frac{d^{2}}{d\varepsilon^{2}}\right|_{\varepsilon=0}f(t,\varepsilon)=-\oint_{\gamma(t)}G\omega. |  | (3.6) |

This construction can be further iterated [Fra96] as long as necessary to obtain a variation that is not identically vanishing. If, on the other hand, all integrals obtained in this recurrent process, turn out to be identically zero, then the displacement function itself is identically zero and hence the perturbation ( 3.2) consists of integrable systems for all ε \varepsilon.

###### Remark.

The exact conditions on the Hamiltonian H H for the identity ( 3.5) to hold for any form whose integral is identically zero, involve connectedness of the complex affine level curves H − 1 ​ ( t) H^{-1}(t) for almost all t ∈ ℂ t\in{\mathbb{C}} [Gav98]. Discussion of the multidimensional situation can be found in [BD00]. As soon as these conditions fail (even because of coinciding critical values, for example), then computation of higher variations may involve integration of non-polynomial forms, see [Ili96].

#### 3.3. Open problems: bifurcation of limit cycles from Hamiltonian polycycles and generalized Poincaré center–focus problem

It would be wrong to think that the above approach based on computing consecutive variations, *completely*reduces the question on limit cycles born by perturbation of Hamiltonian systems, to investigation of Abelian integrals.

First, even assuming the simplest case I 1 ≢ 0 I_{1}\not\equiv 0, we cannot in general say anything about limit cycles born from *critical*level curves (corresponding to polycycles of the unperturbed Hamiltonian system). In the particular case of *separatrix loops*(level curves homeomorphic to the circle and carrying only one nondegenerate saddle point), the problem was settled by R. Roussarie [Rou89]. He estimated how many derivatives of the Abelian integral I ⁡ ( t) I(t) should have zero limits as t → t ∗ t\to t_{*} in order for the perturbation ( 3.2) to produce n n or more limit cycles close to the separatrix loop on the critical level curve { H = t ∗ } \{H=t_{*}\}. This result yields an upper bound for the cyclicity of the separatrix loop in terms of the “multiplicity of the root” of the Abelian integral I 1 I_{1} at the point t ∗ t_{*} where I 1 I_{1} in fact loses its analyticity. The only other type of critical level curve that can occur for a generic polynomial H H, if the eight-shaped curve (also carrying a nondegenerate saddle). The answer in this case is not yet known.

The second, apparently much more difficult problem, appears in connection with the natural question, *How many consecutive variations I k I_{k} should be computed in order to guarantee that the perturbation is non-conservative?*

The inductive process described in Lemma 2, is algebraic in the following sense. Starting from the perturbation ( 3.2) given by the form ω = ω 1 \omega=\omega_{1}, we construct a sequence of the polynomial 1-forms ω 2, ω 3, … \omega_{2},\omega_{3},\dots which express the higher variations I k ​ ( t) I_{k}(t) ( 3.4), assuming that all previous variations vanish identically, I 1 ≡ ⋯ ≡ I k − 1 ≡ 0 I_{1}\equiv\cdots\equiv I_{k-1}\equiv 0. Coefficients of the forms ω k \omega_{k} are given by algebraic (polynomial) expressions involving coefficients of the initial form ω \omega. Vanishing of their integrals implies an infinite number of polynomial identities between coefficients of the initial form ω \omega. By the Hilbert basis theorem, all these infinitely many identities are corollaries to only finitely many of them. Thus only finitely many steps of the inductive process must be performed (their number N < + ∞ N<+\infty depends on the *degree*of the initial form ω \omega and, naturally, on the Hamiltonian H H). If all integrals ∮ ω k \oint\omega_{k}, k = 1, …, N k=1,\dots,N are identically zeros, then all higher variations are necessarily zeros and the entire family ( 3.2) is integrable.

However, the problem of finding an upper bound for the number N N in terms of ω \omega and H H is overtly open: even for the most simple case H = 1 2 ​ ( x 2 + y 2) H=\tfrac{1}{2}(x^{2}+y^{2}) considered in Example 3.1 above, the answer is unknown, moreover, it constitutes the challenging problem on distinguishing between center and focus, posed by Poincaré a century ago and still open. A similar though apparently more simple problem was recently studied in [BFY99].

###### Remark.

A polynomial vector field can be integrable but not Hamiltonian: it is sufficient that the corresponding form Ω \Omega possess an integrating factor. A typical example is that of *Darboux integrable*vector fields. Let λ 1, …, λ n ∈ ℝ \lambda_{1},\dots,\lambda_{n}\in{\mathbb{R}} be a collection of real numbers and H 1, …, H n ∈ ℝ ⁡ [x, y] H_{1},\dots,H_{n}\in{\mathbb{R}}[x,y] polynomials. The rational 1-form

 | Ω ′ = ∑ i = 1 n λ i d ​ H i H i = d ​ F F, F = H 1 λ 1 ⋯ H n λ n, \Omega^{\prime}=\sum_{i=1}^{n}\lambda_{i}\frac{dH_{i}}{H_{i}}=\frac{dF}{F},\qquad F=H_{1}^{\lambda_{1}}\cdots H_{n}^{\lambda_{n}}, |  |

determines a conservative (integrable) singular foliation, since its null spaces { Ω ′ = 0 } \{\Omega^{\prime}=0\} are tangent to the real level curves { F ( x, y) = t } ⊂ ℝ 2 \{F(x,y)=t\}\subset{\mathbb{R}}^{2} which are all closed unless beginning and ending at infinity. The form Ω ′ \Omega^{\prime} is not polynomial (only rational), but the form Ω = R ​ Ω ′ \Omega=R\Omega^{\prime} already will be, if R = gcd ⁡ ( H 1, …, H n) ∈ ℝ ⁡ [x, y] R=\gcd(H_{1},\dots,H_{n})\in{\mathbb{R}}[x,y] is the common divisor of all H i H_{i}.

Appearance of limit cycles in polynomial perturbations of the form

 | Ω + ε ω = 0, ω = p d x + q d y, p, q ∈ ℝ [x, y], \Omega+\varepsilon\omega=0,\qquad\omega=p\,dx+q\,dy,\quad p,q\in{\mathbb{R}}[x,y], |  |

is determined by the same mechanisms as in the Hamiltonian case, in particular, the first variation of the Poincaré displacement map measured in units of ln ⁡ F = ∑ λ i ​ ln ⁡ H i \ln F=\sum\lambda_{i}\ln H_{i}, is equal to the integral

 | I ⁡ ( t) = ∮ F = t 1 R ⁡ ( x, y) ​ ω I(t)=\oint_{F=t}\frac{1}{R(x,y)}\,\omega |  |

of the *rational*1-form R − 1 ​ ω R^{-1}\omega along closed level curves of the *transcendental*function F F.

As was noted on several occasions by V. Arnold, the problem on Abelian integrals should be posed also for such “pseudo-Abelian” integrals. Nevertheless, there are practically no results of general nature pertinent to this problem, even in the simplest cases n = 2 n=2 and n = 3 n=3. In particular, *all*results described below (derivation of the Picard–Fuchs system, monodromy properties etc) fail for this generalized class of integrals.

### 4. Finiteness problems for Abelian integrals: tangential Hilbert problem

Despite its ambivalent nature, the connection between limit cycles of polynomial vector fields and isolated zeros of Abelian integrals justifies formulation of several finiteness problems for the latter. As suggested above, we refer to this problem as the tangential Hilbert problem, distinguishing between several finiteness types according to the paradigm laid out before.

#### 4.1. Individual finiteness

For any fixed combination of the Hamiltonian H H and the 1-form ω \omega the Abelian integral appearing in ( 3.3) as a function of the real variable t t can be shown to be real analytic except for finitely many values of t t. According to § 1, it may have only finitely many isolated zeros unless they accumulate to one of these exceptional values. The *individual finiteness problem for Abelian integrals*is to prove that such accumulation is in fact impossible. This assertion turns out to be a simple corollary to a general theorem describing ramification of Abelian integrals after analytic continuation into the complex domain. The key step in the proof of individual finiteness for Abelian integrals is the following representation.

###### Lemma 3

Any Abelian integral near any exceptional point t ∗ t_{*} admits a *converging*representation of the form

 | I ⁡ ( t) = ∑ r, k h k ​ r ​ ( t) ​ ( t − t ∗) r ​ ln k − 1 ⁡ ( t − t ∗) I(t)=\sum_{r,k}h_{kr}(t)\,(t-t_{*})^{r}\ln^{k-1}(t-t_{*}) |  | (4.1) |

with finitely many terms, where all exponents r r are rational numbers, the powers k k take only finitely many natural values, and all functions h k ​ r h_{kr} are real analytic at the point t = t ∗ t=t_{*}.

This Lemma is explained in § 5. As soon as the representation ( 4.1) is established, the rest of the proof is as described in Example 1.2. It remains only to notice that the convergence of the expansion ( 4.1) is crucial: if all terms in this expansion are zeros, then the integral itself is identically zero and hence has no isolated roots at all (compare with the Remark in § 2.3).

#### 4.2. Existential finiteness

Abelian integrals depend on the choice of the Hamiltonian and the form; in order to make the parameter space finite-dimensional, one has to restrict their degrees. Then the coefficients of the Hamiltonian H H and the form ω \omega become the natural parameters of the problem.

The parameter space is intrinsically compact: indeed, replacing H H and ω \omega by c 1 ​ H c_{1}H and c 2 ​ ω c_{2}\omega with c 1, c 2 c_{1},c_{2} nonzero constants, clearly does not affect the number of isolated roots of the corresponding integral. Hence the parameter spaces are in fact projective spaces of appropriate dimensions.

Fix any two integer numbers n n and d d and consider all Hamiltonians of degree ⩽ n \leqslant n and all polynomial forms of degree ⩽ d \leqslant d. The existence of *uniform*upper bounds for the number of isolated zeros of the Abelian integrals subject to the above restrictions on the degrees, was proved by Varchenko [Var84] and Khovanskii [Kho84].

###### Theorem 3 (A. Varchenko–A. Khovanskii, 1984)

For any n, d < + ∞ n,d<+\infty, the number of ovals γ ⊂ { H = const } \gamma\subset\{H=\operatorname{const}\} yielding isolated zeros to the Abelian integral ∮ γ ω \oint_{\gamma}\omega, is bounded by a constant N = N ⁡ ( n, d) N=N(n,d) uniformly over all Hamiltonians of degree ⩽ n \leqslant n and all polynomial 1-forms of degree ⩽ d \leqslant d.

One key tool in their proof is again the same Lemma 3 properly generalized to cover the parametric construction. The second principal ingredient is the *Pfaffian elimination*technique [Kho91]. The latter is a method allowing to reduce the question on zeros of functions involving real powers, logarithms, arctangents and other functions that can be defined using Pfaffian equations with algebraic right hand sides, to the question on zeros of certain auxiliary systems of equations involving only algebraic functions. Application of the generalized Lemma 3 allows to derive the existential finiteness theorem for Abelian integrals, using in the standard way the compactness and localization arguments, from the similar existential finiteness assertion for converging multivariate expressions of the form ( 4.1). The latter assertion can in turn be derived, using the Pfaffian elimination technique, from the existential finiteness theorem for analytic families of functions as introduced in § 1. This last case was already settled by Theorem 1, and this completes the proof.

However, since both Theorem 1 and its corollary, Theorem 2 do not give any information on the *number*of isolated roots of functions, Theorem 3 inherits this quality as a purely existential statement.

 | *Degree of the form* |

Hamiltonian H H | Low degree ( deg ⁡ ω ⩽ 2) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Low degree}\\ \text{($\deg\omega\leqslant 2$)}\end{matrix} | Arbitrary d = deg ⁡ ω (asymptotic) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Arbitrary}\\ \text{\bf$d=\deg\omega$}\\ \text{\bf(asymptotic)}\end{matrix} | Arbitrary degree (constructive) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Arbitrary}\\ \text{\bf degree}\\ \text{\bf(constructive)}\end{matrix} |

Quadratic: H = x 2 + y 2 \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Quadratic:}\\ \text{$H=x^{2}+y^{2}$}\end{matrix} | Integrals are polynomial functions of t t |

Elliptic H = y 2 + x 3 − 3 ​ x \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Elliptic}\\ \text{$H=y^{2}+x^{3}-3x$}\end{matrix} | ⩽ 1 root Petrov [Pet86] \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{$\leqslant 1$ root}\\ \text{Petrov \cite[cite]{[\@@bibref{}{petrov:cubic-real}{}{}]}}\end{matrix} |  | nonoscillation theorem Petrov [Pet88] \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{nonoscillation}\\ \text{theorem}\\ \text{Petrov \cite[cite]{[\@@bibref{}{petrov:cubic-nonosc}{}{}]}}\end{matrix} |

General cubic H \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf General}\\ \text{\bf cubic $H$}\end{matrix} | numerous results in particular, Gavrilov [Gav01] \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{numerous results}\\ \text{in particular,}\\ \text{Gavrilov \cite[cite]{[\@@bibref{}{gavrilov:quadratic}{}{}]}}\end{matrix} |  | 5 ​ ( d + 2) Horozov–Iliev [HI98] \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{$5(d+2)$}\\ \text{Horozov--Iliev}\\ \text{\cite[cite]{[\@@bibref{}{horozov-iliev:linear}{}{}]}}\end{matrix} |

Hyperelliptic H = y 2 + P n ​ ( x) \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf Hyperelliptic}\\ \text{$H=y^{2}+P_{n}(x)$}\end{matrix} | — | Petrov [Pet90] | tower function, Novikov–Yako- venko [NY99a] \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{tower function,}\\ \text{Novikov--Yako-}\\ \text{venko \cite[cite]{[\@@bibref{}{era-99}{}{}]}}\end{matrix} |

General n th degree polynomial \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{\bf General}\\ \text{$n$th \bf degree}\\ \text{\bf polynomial}\end{matrix} | — | C ⁡ ( n) ​ d + O ⁡ ( 1), Khovanskii [Kho95] \begin{matrix}\vskip 3.0pt plus 1.0pt minus 1.0pt\cr\text{$C(n)d+O(1)$,}\\ \text{Khovanskii}\\ \text{\cite[cite]{[\@@bibref{}{asik:unpub}{}{}]}}\end{matrix} | ??? |

Table 2. Constructive tangential Hilbert 16th problem: partial synopsis

Dashes in the cells mark irrelevant (artificial) problems. Blank cells indicate that the corresponding problem possesses no specific (more accurate) solution other than the one implied by stronger versions appearing to the right or down in the Table.

#### 4.3. Constructive finiteness

The simplest (trivial) case when constructive bounds for the tangential Hilbert problem can be easily produced, is the case of quadratic Hamiltonians. In this case all Abelian integrals can be explicitly computed, being actually *polynomial*functions of t t.

The constructive finite cyclicity problem for Abelian integrals is also a relatively simple assertion: the maximal multiplicity of an isolated zero of an Abelian integral admits an upper bound in terms of deg ⁡ ω \deg\omega and deg ⁡ H \deg H found by P. Mardešić in [Mar91].

Historically the first nontrivial problem concerning zeros of Abelian integrals appeared in connection with what later became known as the Takens–Bogdanov bifurcation. In order to prove that no more than one limit cycle appears by deformation of the generic cuspidal singular point on the plane, one has to verify that for any 1-form ω = ( α + β ​ x) ​ y ​ d ​ x \omega=(\alpha+\beta x)y\,dx its integral over the closed ovals of the Hamiltonian H ⁡ ( x, y) = y 2 + x 3 − 3 ​ x H(x,y)=y^{2}+x^{3}-3x has no more than one isolated zero. R. Bogdanov in [Bog76] proved this claim, achieving one of the first results on Abelian integrals. Later his proof was considerably simplified by Ilyashenko in the paper [Ily78] which introduced some very important tools, among them the idea of complexification of the Abelian integrals.

There are numerous studies treating other low-degree cases that mostly appeared in connection with bifurcations of polynomial vector fields of low degrees. Starting from the paper by Bogdanov, this direction was pursued, among other, by F. Dumortier, A. Gasull, L. Gavrilov, F. Girard, E. Horozov, I. Iliev, Yu. Ilyashenko, A. Jebrane, B. Li, C. Li, J. Llibre, P. Mardešić, G. Petrov, R. Roussarie, C. Rousseau, Z. Zhang, Y. Zhao, H. Zoladek, to mention only some names and the most recent works. Among these accurate bounds, the following result is remarkable by its succinct formulation and difficult proof.

###### Theorem 4 (L. Gavrilov–E.Horozov–I.Iliev [Gav01])

For any cubic Hamiltonian H H with four distinct critical values, and any quadratic 1-form ω \omega, the corresponding Abelian integral has no more than two isolated roots.

Moreover, in the perturbation ( 3.2) no more than 2 limit cycles may appear, including those born from separatrix polygons.

This settles the localized version of the Hilbert 16th problem for quadratic vector fields arbitrary close to Hamiltonian quadratic vector fields with the specified Hamiltonians (cubic with 4 distinct critical values). The bound is accurate.

Another remarkable result is due to G. Petrov [Pet88] who studied completely the *elliptic case*H ⁡ ( x, y) = y 2 + P 3 ​ ( x) H(x,y)=y^{2}+P_{3}(x), where P 3 ∈ ℝ ⁡ [x] P_{3}\in{\mathbb{R}}[x] is a cubic univariate polynomial: by affine transformations one can always reduce P 3 P_{3} to the form P 3 ​ ( x) = x 3 − 3 ​ x P_{3}(x)=x^{3}-3x. Petrov proved that the Abelian integrals of forms of arbitrary degree form a *non-oscillating*(in other languages *disconjugate*, or *Chebyshev*) family: *the number of isolated roots never becomes equal or exceeds the dimension of the linear space of all such integrals*.

###### Remark.

One can easily verify that any linear space spanned by d d linear independent analytic functions f 1 ​ ( t), …, f d ​ ( t) f_{1}(t),\dots,f_{d}(t) contains a nontrivial linear combination c 1 ​ f 1 + ⋯ + c d ​ f d c_{1}f_{1}+\cdots+c_{d}f_{d} exhibiting a root of multiplicity d − 1 d-1 at any preassigned point.

Methods introduced by Petrov were further elaborated and refined. The following bound obtained by E. Horozov and I. Iliev, though not sharp, covers the case of Abelian integrals of arbitrary polynomial forms over level curves of any cubic Hamiltonians.

###### Theorem 5 ( [HI98])

For any cubic Hamiltonian H ⁡ ( x, y) H(x,y) the Abelian integral of a form of degree d d cannot have more than 5 ​ ( d + 2) 5(d+2) isolated zeros.

By similar methods the *quartic*Hamiltonians (of degree 4) with *elliptic*level curves were studied in [GJ98]. The case of quartic elliptic Hamiltonians perturbed within the Liénard equation was a subject of four recent preprints of C. Li and F. Dumortier.

#### 4.4. Asymptotic bounds

Results of the different type, asymptotic bounds, take advantage of the asymmetry of the roles played by 1-forms and Hamiltonians. Unlike the original Hilbert 16th problem, in which the coefficients of the polynomials P, Q P,Q all enjoy equal rights as parameters, the roles of the Hamiltonian H H and the form ω \omega in the definition of the Abelian integrals are fairly different (e.g., the integral depends on ω \omega linearly, whereas even small variations of H H can result in drastic changes of the domain of definition). Thus it makes complete sense to separate these two parameters and study first the dependence on ω \omega, treating H H as fixed (“individual”).

The corresponding “semiconstructive” problem was addressed in a number of recent publications. First, very excessive (double exponential in d d) upper bounds were obtained in [IY95a] and almost immediately improved to simple exponential expression in [NY95] by Ilyashenko, Novikov and the author. The ultimate result in this direction, a *linear*upper bound of the form C 1 ​ ( n) ⋅ d + C 2 ​ ( n) C_{1}(n)\cdot d+C_{2}(n), was obtained by Khovanskii [Kho95] using some ideas developed earlier by G. Petrov [Pet90]. Here the constant C 1 ​ ( n) C_{1}(n) is absolutely explicit (e.g., does not exceed a double exponential of n n), while the second constant C 2 ​ ( n) C_{2}(n) is purely existential though uniform over all Hamiltonians of degree ⩽ n \leqslant n.

#### 4.5. Hyperelliptic integrals

The only particular case covering Hamiltonians of arbitrarily high degrees, for which constructive solution of the tangential Hilbert problem is known, is that of *hyperelliptic*Hamiltonians,

 | H ⁡ ( x, y) = y 2 + P n + 1 ​ ( x), P n + 1 = x n + 1 + a 1 ​ x n − 1 + ⋯ + a n − 1 ​ x + a n. H(x,y)=y^{2}+P_{n+1}(x),\quad P_{n+1}=x^{n+1}+a_{1}x^{n-1}+\cdots+a_{n-1}x+a_{n}. |  | (4.2) |

Singular points of the corresponding Hamiltonian system correspond to critical points of the polynomial P P, called *potential*. The reason why the class of hyperelliptic polynomials is especially simple, one can vaguely attribute to the fact that from many points of view, hyperelliptic polynomials behave like their univariate potentials. In particular, this concerns topology of the bundles defined by complexification of H H.

Under the addition assumption (believed to be technical, though it occurs independently and persistently in several related problems) that *all critical points of the potential P P are real*, the tangential Hilbert problem turns out to be *constructively solvable*. More precisely, as shown by D. Novikov and the author [NY99a], there exists an algorithm defining an elementary function C ⁡ ( n, d) C(n,d) of two integer arguments n n and d d, such that for any form of degree ⩽ d \leqslant d and any hyperelliptic Hamiltonian n n of degree ⩽ n \leqslant n having only real critical points, the corresponding hyperelliptic Abelian integral has no more than C ⁡ ( n, d) C(n,d) isolated roots.

The algorithm involves several nested inductive constructions, resulting in an *extremely excessive*bound: it is given by a *tower function*(an iterated exponential) of height greater than 5 but probably smaller than 10.

The proof is based on the fact that Abelian integrals satisfy a system of first order linear ordinary differential equations with rational coefficients, called the *Picard–Fuchs*system.

#### 4.6. Quantitative theory of ordinary differential equations as a tool for constructive solution of the tangential Hilbert problem

The method used for constructive solution of the tangential Hilbert problem in the hyperelliptic case, is fairly general. In [Yak99] one can find an introduction to the general theory allowing to investigate zeros of functions defined by ordinary differential equations with polynomial and rational coefficients. Basics of this theory were developed in a series of joint works by D. Novikov and the author; they are briefly recalled below.

The principal goal of these lecture notes is twofold. First, we show that the Picard–Fuchs system of differential equations can be *explicitly*written down for an arbitrary generic Hamiltonian (not necessarily a hyperelliptic one), at least at the price of certain *redundancy*. Some additional information may be extracted from the explicit derivation procedure. In particular, we show that for almost any Hamiltonian H H (chosen for convenience of degree n + 1 n+1):

1. (1)

there exist μ \mu different Abelian integrals I k = ∮ ω k I_{k}=\oint\omega_{k} of monomial 1-forms ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu}, μ = n 2 \mu=n^{2}, satisfying together a *Fuchsian system*of linear ordinary differential equations with rational coefficients of the form

 | d ​ x d ​ t = A ( t) x, A ( t) = ∑ j = 1 μ A j t − t j, x ∈ ℂ μ, A j ∈ Mat μ × μ ( ℂ), t ∈ ℂ, t 1, …, t μ ∈ ℂ, \begin{gathered}\frac{dx}{dt}=A(t)x,\qquad A(t)=\sum_{j=1}^{\mu}\frac{A_{j}}{t-t_{j}},\\ x\in{\mathbb{C}}^{\mu},\quad A_{j}\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}),\quad t\in{\mathbb{C}},t_{1},\dots,t_{\mu}\in{\mathbb{C}},\end{gathered} |  | (4.3) |

such that

2. (2)

integral I ⁡ ( t) I(t) of any other form ω \omega can be represented as a linear combination of the integrals I 1, …, I μ I_{1},\dots,I_{\mu},

 | I ⁡ ( t) = q 1 ​ ( t) ​ I 1 ​ ( t) + ⋯ + q μ ​ ( t) ​ I μ ​ ( t), I(t)=q_{1}(t)I_{1}(t)+\cdots+q_{\mu}(t)I_{\mu}(t), |  | (4.4) |

with polynomial coefficients q j ∈ ℂ ⁡ [t] q_{j}\in{\mathbb{C}}[t], deg ⁡ q j ⩽ deg ⁡ ω / deg ⁡ H \deg q_{j}\leqslant\deg\omega/\deg H.

The residue matrices A j A_{j} can be sufficiently completely described, in particular, upper bounds on their norms can be placed.

The second goal is to introduce several results on the number of zeros of functions defined by systems of ordinary linear equations with polynomial and rational coefficients, and polynomial combinations of such functions. We start with the simplest case of one n n th order linear equation and show that isolated zeros of its solutions can be described in terms of the magnitude of coefficients of this equation. In the simplest real case this is a classical theorem by de la Vallée Poussin [dlVP29], which we generalize for the complex analytic context. Afterwards we study systems of polynomial ODE’s in the real and complex space of arbitrary dimension; here for the first time appear explicit bounds given by tower functions. Finally, we discuss the case of Fuchsian systems of the form ( 4.3) and show that under certain natural restrictions on the monodromy group of this equation, a global upper bound on the number of zeros can be given in terms of norms of the residue matrices A j A_{j}.

One can hope that combination of these two techniques ultimately would allow to construct an explicit bound for the tangential Hilbert problem in the general case, filling the right bottom corner of the Table 2.

## Lecture II Abelian integrals and differential equations

In this lecture we explain the connection between Abelian integrals and linear ordinary differential equations.

### 5. Complexification of Abelian integrals: topological approach

#### 5.1. General scheme

We recall here the basic construction of complexification of Abelian integrals. All details can be found in various textbooks, [AGV88] being the principal source.

A bivariate polynomial H ∈ ℂ ⁡ [x, y] H\in{\mathbb{C}}[x,y] defines a map from ℂ 2 {\mathbb{C}}^{2} to ℂ 1 {\mathbb{C}}^{1} with preimages of points being affine algebraic curves. It turns out that the map H H is a *topological bundle*over a complement to finitely many points Σ = { t 1, …, t r } ⊂ ℂ \varSigma=\{t_{1},\dots,t_{r}\}\subset{\mathbb{C}}. This allows to identify in a canonical way the homology groups of all fibers H − 1 ​ ( t) H^{-1}(t) sufficiently close to H − 1 ​ ( t ∗) H^{-1}(t_{*}), which in turn allows to extend integrals over 1-cycles of polynomial 1-forms as complex analytic functions of t t in U U, ramified over the singular locus Σ \varSigma. Geometrically this can be expressed as introducing a locally flat connexion on the (co)homological bundles over the punctured sphere.

From the same topological arguments it follows that for any polynomial 1-form ω \omega the linear space generated by integrals ∮ δ i ω \oint_{\delta_{i}}\omega over any family δ 1 ​ ( t), …, δ μ ​ ( t) \delta_{1}(t),\dots,\delta_{\mu}(t) of cycles forming a basis in the first homology group of the fiber X t = H − 1 ​ ( t) X_{t}=H^{-1}(t), is invariant by analytic continuation along the loops avoiding the locus Σ \varSigma. The monodromy group consisting of all automorphisms of this space occurring as the result of continuation over all loops, is independent of the choice of the form ω \omega and depends only on the Hamiltonian H H.

These fairly general topological considerations already imply that the Abelian integrals form a finitely generated module over the ring of polynomial functions of t t, and generators of this module satisfy a system of first order linear ordinary differential equations with rational (in t t) coefficients, called *Picard–Fuchs*equations.

However, in order to apply methods described in subsequent sections, it is necessary to obtain *quantitative*characteristics of these equations, in particular their dimension, degree and the magnitude of coefficients. Part of this information (e.g., the dimension) can be easily achieved from the above construction. To obtain upper bounds on the degrees, some other more refined considerations are required, but it is practically impossible to derive bounds for the coefficients using only topological arguments as above.

The current section contains a brief exposition of well-known facts leading to derivation of Picard–Fuchs equations and representation of the space of Abelian integrals as the Picard–Vessiot extension. In the next section we suggest an alternative approach based on elementary algebraic consideration, that allows to derive explicitly the Picard–Fuchs system at the price of certain redundancy.

#### 5.2. Topological bundles defined by proper maps

Let f: M → N f\colon M\to N be a smooth map between two manifolds. Recall that a point b ∈ N b\in N is a regular value for f f, if the rank of the differential f ∗: T x ​ M → T b ​ N f_{*}\colon T_{x}M\to T_{b}N is maximal (equal to dim N \dim N) at all points x ∈ X b x\in X_{b} of the preimage. Complement to the set of regular values consists of *critical values*and is denoted crit ⁡ f \operatorname{crit}f.

###### Lemma 4

If b b is a regular value of a proper map f: M → N f\colon M\to N, then there exists a neighborhood U ∋ b U\owns b such that all preimages X y = f − 1 ​ ( y) ⊂ M X_{y}=f^{-1}(y)\subset M are diffeomorphic to X b = f − 1 ​ ( b) X_{b}=f^{-1}(b) so that f − 1 ​ ( U) ≃ X b × U f^{-1}(U)\simeq X_{b}\times U.

###### Proof.

Consider an arbitrary vector v 0 ∈ T b ​ N v_{0}\in T_{b}N and embed it into a vector field v v on N N. We claim that in a sufficiently small neighborhood of the preimage X b X_{b} one can construct a smooth vector field w w such that f ∗ ​ w = v f_{*}w=v, that is, w w and v v are f f -related. Such a field obviously exists near each point x ∈ X b x\in X_{b}, since f ∗ f_{*} is surjective (and takes the form of a parallel projection in suitably chosen local coordinates by virtue of the theorem on rank). Now it remains to choose a finite covering of X b X_{b} by these neighborhoods and patch together the corresponding vector fields, using the appropriate partition of unity.

To conclude the proof, notice that the (local) flows of v v and w w are conjugate by f f (by construction), hence the local flow of w w, defined in some neighborhood of X b X_{b}, takes the latter preimage into preimage of the corresponding point y y on the flow curve of b b. Since the initial vector v 0 v_{0} can be chosen pointing to any direction, this proves that all sufficiently close preimages are diffeomorphic to each other. ∎

###### Remark.

The diffeomorphism between close preimages is not canonically defined, but any two such diffeomorphisms are homotopically equivalent, since the vector field w w from the proof of the Lemma is homotopically unique.

###### Corollary 1

If M M is compact, then f f is a topological bundle over N ∖ crit ⁡ f N\smallsetminus\operatorname{crit}f.∎

###### Remark.

Assertion of this lemma for the case N = ℝ N={\mathbb{R}} is the fundamental principle of the Morse theory.

#### 5.3. Homology bundle and flat connexion on it

A locally trivial topological bundle f: M → N f\colon M\to N defines in a canonical way the associated homology bundle over N N with the fibers being the homology groups H i ​ ( X y, ℤ) H_{i}(X_{y},\mathbb{Z}) (we will be only interested in the case i = 1 i=1) together with a flat connexion on this bundle. This means that any 1-cycle on any particular fiber X a X_{a} can be transported to any other fiber X b X_{b} along any path γ \gamma connecting a a and b b in N N. Flatness means that continuation along any sufficiently small loop beginning and ending at a a, returns any 1-cycle to its initial position. However, transport along “long” loops (not contractible in N N) can result in a nontrivial transformation of the homology, called the *monodromy transformation*.

Fix a point a ∈ N a\in N and choose a basis δ 1, …, δ μ \delta_{1},\dots,\delta_{\mu} of 1-cycles in the group H 1 ​ ( X a, ℤ) H_{1}(X_{a},\mathbb{Z}), where μ \mu is the rank of the homology group. Then the monodromy transformation corresponding to any loop γ \gamma from the fundamental group π 1 ​ ( N, a) \pi_{1}(N,a) can be described by the corresponding *monodromy matrix*M = M γ ∈ Mat μ × μ ⁡ ( ℤ) M=M_{\gamma}\in\operatorname{Mat}_{\mu\times\mu}(\mathbb{Z}) with integral entries m i ​ j m_{ij}:

 | Δ γ δ j = ∑ i = 1 μ δ i m i ​ j, i = 1, …, μ. \Delta_{\gamma}\delta_{j}=\sum_{i=1}^{\mu}\delta_{i}m_{ij},\qquad i=1,\dots,\mu. |  | (5.1) |

In the matrix form the monodromy transformation acts on the row vector 𝜹 = ( δ 1, …, δ μ) \boldsymbol{\delta}=(\delta_{1},\dots,\delta_{\mu}) as multiplication by the matrix M γ M_{\gamma} from the right, Δ γ ​ 𝜹 = 𝜹 ⋅ M γ \Delta_{\gamma}\boldsymbol{\delta}=\boldsymbol{\delta}\cdot M_{\gamma}.

The integer-valued matrix M γ M_{\gamma} is obviously invertible. Moreover, the correspondence γ ↦ M γ \gamma\mapsto M_{\gamma} is an (anti)representation of the fundamental group π 1 ​ ( N, a) \pi_{1}(N,a) in GL ⁡ ( n, ℤ) \mathrm{GL}(n,\mathbb{Z}). This implies, in particular, that det M γ = ± 1 \det M_{\gamma}=\pm 1 for all loops γ \gamma.

The flat connexion on the homology bundle defines a connexion on the cohomology bundle which makes it possible to compute the covariant derivative of 1-forms: any smooth 1-form ω \omega on M M can be restricted on any fiber X a X_{a} and integrated along a continuous (horizontal, locally constant) family of 1-cycles δ ⁡ ( y) \delta(y), resulting in a function I ⁡ ( y) I(y). The result of continuation of this function along closed paths in N N is completely determined by the monodromy group and does not depend on the choice of the form ω \omega. More precisely, integrating the form ω \omega over each of the 1-cycles 𝜹 ⁡ ( t) = ( δ 1 ​ ( y), …, δ μ ​ ( y)) \boldsymbol{\delta}(t)=(\delta_{1}(y),\dots,\delta_{\mu}(y)), we obtain a tuple of continuous functions I j ​ ( y) = ∮ δ j ​ ( y) ω I_{j}(y)=\oint_{\delta_{j}(y)}\omega, j = 1, …, μ j=1,\dots,\mu, which after continuation along a path γ ∈ π 1 ​ ( N, a) \gamma\in\pi_{1}(N,a) undergo the transformation

 | Δ γ ​ 𝑰 = 𝑰 ⋅ M γ, 𝑰 = ( I 1, …, I μ), I j = I j ​ ( y) \Delta_{\gamma}\boldsymbol{I}=\boldsymbol{I}\cdot M_{\gamma},\qquad\boldsymbol{I}=(I_{1},\dots,I_{\mu}),\ I_{j}=I_{j}(y) |  | (5.2) |

with the same matrices M γ M_{\gamma} independently of the form ω \omega. This basic fact lies in the core of the topological theory outlined below.

#### 5.4. Topological bundles defined by polynomial maps

Our goal is to apply the previous construction to the polynomial map H: ℂ 2 → ℂ H\colon{\mathbb{C}}^{2}\to{\mathbb{C}} considered as a smooth map between smooth manifolds. Since compactness of the preimages is crucial for these arguments, we need to compactify the domain (and the range) of H H.

In contrast with the one-dimensional case, it is in general impossible to extend H H as a map between the natural compactifications ℂ ​ P 2 {\mathbb{C}}P^{2} and ℂ ​ P 1 {\mathbb{C}}P^{1} respectively, since on the infinite line ℂ ​ P ∞ 1 ⊂ ℂ ​ P 2 {\mathbb{C}}P^{1}_{\infty}\subset{\mathbb{C}}P^{2} one has several *points of indeterminacy*: they occur at the intersections between compactified preimages H − 1 ​ ( t) H^{-1}(t) and the infinite line. Algebraically this can be seen as the indeterminacy of the rational expression H ⁡ ( 1 / z, y / z) = P ⁡ ( y, z) / z d H(1/z,y/z)=P(y,z)/z^{d}, d = deg ⁡ H d=\deg H, at the points where P ⁡ ( y, 0) = 0 P(y,0)=0 (at all other points of the infinite line { z = 0 } \{z=0\} one can assign the value H = ∞ H=\infty to this ratio).

The problem can be resolved by blowing up these indeterminacy points, in the same way as blowing up the origin allows to assign values from ℂ ​ P 1 = ℂ ∪ { ∞ } {\mathbb{C}}P^{1}={\mathbb{C}}\cup\{\infty\} to the rational expression R ⁡ ( x, y) = y / x R(x,y)=y/x that is initially indeterminate. After a series of blow-ups at indeterminacy points one arrives at a *compact*two-dimensional complex manifold M M and a map (still denoted by H H) from M M to ℂ ​ P 1 {\mathbb{C}}P^{1}, called *determination*of the initial polynomial map.

Now one can apply Lemma 4. Since the determination H: M → ℂ ​ P 1 H\colon M\to{\mathbb{C}}P^{1} is algebraic, it has only a finite number of critical values Σ H = { t 1, …, t s } ⊂ ℂ ​ P 1 \varSigma_{H}=\{t_{1},\dots,t_{s}\}\subset{\mathbb{C}}P^{1} and we conclude that it defines a topological bundle over the complement of these *exceptional values*. Any 1-cycle δ ​ ( a) ⊂ H − 1 ​ ( a) \delta(a)\subset H^{-1}(a) on a fiber of this bundle can be embedded into a continuous horizontal family δ ⁡ ( t) \delta(t) of 1-cycles, ramified over the exceptional locus. A polynomial 1-form ω \omega extends as a meromorphic 1-form on ℂ ​ P 2 {\mathbb{C}}P^{2} with the polar divisor ℂ ​ P ∞ 1 {\mathbb{C}}P^{1}_{\infty} that after the blowing up becomes an algebraic hypersurface D D in M M. Let Σ \varSigma be the union of Σ H \varSigma_{H} and the critical values of the projection H H restricted on D D (including the images of the non-smooth points of D D).

The pullback of ω \omega on M M can be integrated along the family δ ⁡ ( t) \delta(t): by the Cauchy–Stokes theorem, the result depends only on the homology class of the cycle. It can be easily shown that the result of this integration is an analytic function of t t, ramified over Σ \varSigma. Its monodromy (the result of analytic continuation along closed loops avoiding the exceptional locus Σ \varSigma) is as before determined only by H H.

This construction proves the following result.

###### Proposition 1 (cf. with [AGV88])

For any polynomial H: ℂ 2 → ℂ H\colon{\mathbb{C}}^{2}\to{\mathbb{C}}, any 1-cycle δ \delta on a nonsingular level curve X ∗ = { H = t ∗ } ⊂ ℂ 2 X_{*}=\{H=t_{*}\}\subset{\mathbb{C}}^{2} and any polynomial 1-form ω \omega the Abelian integral I ⁡ ( t) = ∮ δ ω I(t)=\oint_{\delta}\omega can be extended as an analytic multivalued function ramified over a finite number of points depending only on H H.∎

Behavior of the integrals near the ramification locus is relatively tame: it can be seen that any integral can grow no faster than polynomially in | t − t j | − 1 |t-t_{j}|^{-1} as t t tends to some t j ∈ Σ t_{j}\in\varSigma remaining in any sector with the vertex at t j t_{j}.

#### 5.5. Picard–Fuchs system

Let as before 𝜹 ⁡ ( t) = ( δ 1 ​ ( t), …, δ μ ​ ( t)) \boldsymbol{\delta}(t)=(\delta_{1}(t),\dots,\delta_{\mu}(t)) be a continuous family of 1-cycles forming a basis (frame) of the first homology group of the respective fibers H − 1 ​ ( t) H^{-1}(t), arranged as a row vector. One can show that there exist μ \mu polynomial 1-forms ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} such that the *period matrix*

 | X ⁡ ( t) = ( ∮ δ 1 ω 1 ⋯ ∮ δ μ ω 1 ⋱ ∮ δ 1 ω μ ⋯ ∮ δ μ ω μ) X(t)=\begin{pmatrix}\oint_{\delta_{1}}\omega_{1}&\cdots&\oint_{\delta_{\mu}}\omega_{1}\\ \vdots&\ddots&\vdots\\ \oint_{\delta_{1}}\omega_{\mu}&\cdots&\oint_{\delta_{\mu}}\omega_{\mu}\end{pmatrix} |  | (5.3) |

is not identically degenerate, det X ⁡ ( t) ≢ 0 \det X(t)\not\equiv 0. From ( 5.2) it follows that

 | Δ γ ​ X ​ ( t) = X ⁡ ( t) ​ M γ, ∀ γ ∈ π 1 ​ ( ℂ ​ P 1 ∖ Σ, a). \Delta_{\gamma}X(t)=X(t)M_{\gamma},\qquad\forall\gamma\in\pi_{1}({\mathbb{C}}P^{1}\smallsetminus\varSigma,a). |  | (5.4) |

Differentiating the identity ( 5.4), we see that the derivative X ˙ ​ ( t) \dot{X}(t) has the same monodromy (i.e., X ˙ \dot{X} is multiplied by the same matrix factors M γ M_{\gamma}). Therefore the “logarithmic derivative” A ⁡ ( t) = X ˙ ​ ( t) ⋅ X − 1 ​ ( t) A(t)=\dot{X}(t)\cdot X^{-1}(t) is single-valued (invariant by all monodromy transformations) meromorphic matrix function having poles of finite order at the points of Σ \varSigma and eventually at the points of degeneracy of X ⁡ ( ⋅) X(\cdot):

 | Δ γ ​ A ​ ( t) = X ˙ ​ ( t) ​ M γ ⋅ M γ − 1 ​ X − 1 ​ ( t) = X ˙ ​ ( t) ⋅ X − 1 ​ ( t) = A ⁡ ( t) \Delta_{\gamma}A(t)=\dot{X}(t)M_{\gamma}\cdot M^{-1}_{\gamma}X^{-1}(t)=\dot{X}(t)\cdot X^{-1}(t)=A(t) |  |

for any loop γ ∈ π 1 ​ ( ℂ ∖ Σ, t ∗) \gamma\in\pi_{1}({\mathbb{C}}\smallsetminus\varSigma,t_{*}). From this we conclude that A ⁡ ( t) A(t) is a rational matrix function while the period matrix X ⁡ ( t) X(t) is a fundamental matrix solution to the system of linear ordinary differential equations with rational coefficients on ℂ ​ P 1 {\mathbb{C}}P^{1},

 | X ˙ = A ⁡ ( t) ​ X, A ⁡ ( ⋅) ∈ Mat μ × μ ⁡ ( ℂ ⁡ ( t)). \dot{X}=A(t)X,\qquad A(\cdot)\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}(t)). |  | (5.5) |

The common name for various such systems satisfied by Abelian integrals, is the *Picard–Fuchs system*(or Picard–Fuchs equation).

Integrals of any other form ω \omega can be expressed as linear combinations of integrals of the framing forms ω i \omega_{i}, i = 1, …, μ i=1,\dots,\mu, with coefficients from the field ℂ ⁡ ( t) {\mathbb{C}}(t) of rational functions. Indeed, multiplying the row vector 𝑰 ⁡ ( t) = ( I 1 ​ ( t), …, I μ ​ ( t)) \boldsymbol{I}(t)=(I_{1}(t),\dots,I_{\mu}(t)), I j = ∮ δ j ω I_{j}=\oint_{\delta_{j}}\omega, by X − 1 ​ ( t) X^{-1}(t), we obtain (for the same reasons as above) a single-valued hence rational row-vector function 𝒓 ⁡ ( t) = ( r 1 ​ ( t), …, r μ ​ ( t)) \boldsymbol{r}(t)=(r_{1}(t),\dots,r_{\mu}(t)), that is,

 | ∮ δ ⁡ ( t) ω = ∑ j = 1 μ r j ​ ( t) ​ ∮ δ ⁡ ( t) ω j, r j ∈ ℂ ⁡ ( t). \oint_{\delta(t)}\omega=\sum_{j=1}^{\mu}r_{j}(t)\oint_{\delta(t)}\omega_{j},\qquad r_{j}\in{\mathbb{C}}(t). |  | (5.6) |

for any cycle δ ⁡ ( t) \delta(t) continuously depending on t t. Note that the space of functions representable as ( 5.6), is closed by derivation.

We summarize this as follows. Recall that a *Picard–Vessiot extension*is a differential field of analytic multivalued functions obtained by adjoining to the field ℂ ⁡ ( t) {\mathbb{C}}(t) all components of a fundamental matrix solution of a system of linear ordinary differential equations with rational coefficients.

###### Theorem 6

Abelian integrals belong to a Picard–Vessiot extension for some system of linear ordinary differential equations with rational coefficients.

Later we discuss this formulation and relevant issues in more details. However, it is important to stress here that neither entries of the rational matrix A ⁡ ( t) A(t) nor the rational coefficients r j ​ ( t) r_{j}(t) can be computed explicitly from the above construction without additional considerations.

### 6. Hamiltonians transversal to infinity

#### 6.1. Definition

For an arbitrary Hamiltonian H H, even location of the ramification points t j t_{j} is difficult to describe without effectively resolving all the indeterminacy points at infinity. However, under some natural and generic assumptions one may guarantee that no new critical points will appear after compactification and blowing up the indeterminacy points on the infinite line ℂ ​ P ∞ 1 ⊂ ℂ ​ P 2 {\mathbb{C}}P^{1}_{\infty}\subset{\mathbb{C}}P^{2}. This will immediately imply that the set Σ \varSigma of exceptional values must be a subset of crit ⁡ H \operatorname{crit}H, the set of critical values corresponding to *finite*critical points in ℂ 2 {\mathbb{C}}^{2} only.

###### Definition 5.

A polynomial H ∈ ℂ ⁡ [x, y] H\in{\mathbb{C}}[x,y] is said to be *transversal to infinity*, if its principal homogeneous part L = ∑ i + j = d a i ​ j ​ x i ​ y j L=\sum_{i+j=d}a_{ij}x^{i}y^{j}, d = deg ⁡ H d=\deg H, factors as a product of pairwise different linear forms.

Equivalent conditions follow.

1. (1)

The principal homogeneous part has an isolated critical point at the origin;

2. (2)

The partial derivatives ∂ L ∂ x \frac{\partial L}{\partial x}, ∂ L ∂ y \frac{\partial L}{\partial y} are mutually prime;

3. (3)

H H has exactly μ = ( deg ⁡ H − 1) 2 \mu=(\deg H-1)^{2} critical points in ℂ 2 {\mathbb{C}}^{2} if counted with multiplicities;

4. (4)

Each level curve { H = t } \{H=t\} intersects transversely the infinite line ℂ ​ P ∞ 1 ⊂ ℂ ​ P 2 {\mathbb{C}}P^{1}_{\infty}\subset{\mathbb{C}}P^{2} after projective compactification.

#### 6.2. Topology of polynomials transversal to infinity

We prove now that for H H transversal to infinity, Σ = crit ⁡ H \varSigma=\operatorname{crit}H.

###### Proposition 2

A polynomial H: ℂ 2 → ℂ 1 H\colon{\mathbb{C}}^{2}\to{\mathbb{C}}^{1} transversal to infinity is a topological bundle over the set crit ⁡ H \operatorname{crit}H of critical values of H H.

Instead of proving this by resolving the indeterminacy points at infinity, one may modify the proof of Lemma 4 sketched above, and construct the vector field w w near an arbitrary infinite point p ∈ ℂ ​ P ∞ 1 p\in{\mathbb{C}}P^{1}_{\infty} on ℂ ​ P 2 {\mathbb{C}}P^{2} with the property H ∗ ​ w = ∂ ∂ t H_{*}w=\frac{\partial}{\partial t}.

###### Proof.

It will be shown below in § 7.1 that if H H of degree n + 1 n+1 is transversal to infinity, then there exist two polynomials a, b ∈ ℂ ⁡ [x, y] a,b\in{\mathbb{C}}[x,y] of degree n − 1 n-1 such that

 | a ​ ∂ H ∂ x + b ​ ∂ H ∂ y = x 2 ​ n − 1 + ⋯, a\frac{\partial H}{\partial x}+b\frac{\partial H}{\partial y}=x^{2n-1}+\cdots, |  |

where the dots stand for a bivariate polynomial of degree ⩽ 2 ​ n − 2 \leqslant 2n-2. One can easily check that the rational vector field

 | w = a ⁡ ( x, y) x 2 ​ n − 1 + ⋯ ​ ∂ ∂ x + b ⁡ ( x, y) x 2 ​ n − 1 + ⋯ ​ ∂ ∂ y, w=\frac{a(x,y)}{x^{2n-1}+\cdots}\frac{\partial}{\partial x}+\frac{b(x,y)}{x^{2n-1}+\cdots}\frac{\partial}{\partial y}, |  |

H H -related to the field ∂ ∂ t \frac{\partial}{\partial t}, in the chart ( 1 / x, y / x) (1/x,y/x) is regular (smooth) *on the infinite line*1 / x = 0 1/x=0 (more precisely, on its affine part covered by this chart). The other affine part is covered by the field that is obtained in a similar way from solution of the equation a ​ ∂ H ∂ x + b ​ ∂ H ∂ y = y 2 ​ n − 1 + ⋯ a\frac{\partial H}{\partial x}+b\frac{\partial H}{\partial y}=y^{2n-1}+\cdots.

Thus near each point of the compactified level curve X ¯ a ⊂ ℂ ​ P 2 \overline{X}_{a}\subset{\mathbb{C}}P^{2} one has a smooth vector field H H -related to ∂ ∂ t \frac{\partial}{\partial t} in the finite part ℂ 2 ⊂ ℂ ​ P 2 {\mathbb{C}}^{2}\subset{\mathbb{C}}P^{2} (in particular, this implies that this field vanishes at all points of indeterminacy of H H on ℂ ​ P ∞ 1 {\mathbb{C}}P^{1}_{\infty}). The rest of the proof is the same as in Lemma 4. ∎

#### 6.3. Module of Abelian integrals, Gavrilov and Novikov theorems

For Hamiltonians transversal to infinity, the constructions of § 5 can be further refined. In particular, the choice of the forms ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} can be made much more explicit.

###### Lemma 5 (L. Gavrilov [Gav98])

Let H H be a Hamiltonian of degree n + 1 n+1 transversal to infinity, with distinct critical values t 1, …, t μ t_{1},\dots,t_{\mu}, μ = n 2 \mu=n^{2}. Then one can choose n 2 n^{2} monomial 1-forms ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} of degrees ⩽ 2 ​ n \leqslant 2n so that the respective period matrix has the determinant det X ( t) = c ( t − t 1) ⋯ ( t − t μ) \det X(t)=c(t-t_{1})\cdots(t-t_{\mu}) with c ≠ 0 c\neq 0.

In this assertion we use the convention on degrees of polynomial k k -forms formulated in § 7.1. As a corollary, one can derive the following result that refines the assertion of Theorem 6.

###### Corollary 2

Abelian integral of a 1-form ω \omega of degree d d can be represented as

 | ∮ δ ⁡ ( t) ω = ∑ j = 1 μ p j ​ ( t) ​ ∮ δ ⁡ ( t) ω j, p j ( t) ∈ ℂ [t], deg ω j + deg H ⋅ deg p j ⩽ deg ω. \begin{gathered}\oint_{\delta(t)}\omega=\sum_{j=1}^{\mu}p_{j}(t)\oint_{\delta(t)}\omega_{j},\\ p_{j}(t)\in{\mathbb{C}}[t],\qquad\deg\omega_{j}+\deg H\cdot\deg p_{j}\leqslant\deg\omega.\end{gathered} |  | (6.1) |

In other words, Abelian integrals constitute a module over the ring ℂ ⁡ [t] {\mathbb{C}}[t] that is generated by integrals of the basic forms ω j \omega_{j}.

The constant c c from Lemma 5 depends on the choice of the monomial forms and the Hamiltonian. Its value was explicitly computed by A. Glutsuk [Glu00] following some ideas of Yu. Ilyashenko, and a simple elementary proof of the inequality c ≠ 0 c\neq 0 for an appropriate choice of the monomial forms was obtained by D. Novikov [Nov01a]. In the same paper [Nov01a] it is proved, using some of the methods described below, that the period matrix satisfies a system of linear ordinary differential equations

 | X ˙ = 1 ( t − t 1) ⋯ ( t − t μ) ​ P ​ ( t) ​ X, P ⁡ ( t) = ∑ j = 0 μ t j ​ P j, \dot{X}=\frac{1}{(t-t_{1})\cdots(t-t_{\mu})}P(t)X,\qquad P(t)=\sum_{j=0}^{\mu}t^{j}P_{j}, |  | (6.2) |

with a matrix polynomial P ⁡ ( t) P(t) of degree μ \mu, in general having Fuchsian singularities at all points t j t_{j} of the ramification locus Σ \varSigma, but a *non-*Fuchsian singularity at t = ∞ t=\infty.

As yet another corollary, one can derive a Picard–Fuchs system for the period matrix. Let ω j \omega_{j} be as in Corollary 2. Consider the closed 2 2 -forms d ​ H ∧ ω j dH\land\omega_{j} and let Ω j \Omega_{j} be any polynomial primitives satisfying the conditions

 | d Ω j = d H ∧ ω j, j = 1, …, μ. d\Omega_{j}=dH\land\omega_{j},\qquad j=1,\dots,\mu. |  |

Each Ω i \Omega_{i} can be expanded as in Corollary 2, yielding an identity between the integrals,

 | ∮ Ω i = ∑ j = 1 μ p i ​ j ​ ( t) ​ ∮ ω j \oint\Omega_{i}=\sum_{j=1}^{\mu}p_{ij}(t)\oint\omega_{j} |  |

valid for any choice of a continuous family of cycles of integration δ ⁡ ( t) \delta(t). On the other hand, as will be shown in § 7.2, the derivative of each integral ∮ Ω i \oint\Omega_{i} is exactly the integral ∮ ω i \oint\omega_{i}. Differentiating the above identities, we arrive to the matrix differential equation

 | X = P ˙ ​ X + P ​ X ˙, P = P ⁡ ( t) = ‖ p i ​ j ​ ( t) ‖ ∈ Mat μ × μ ⁡ ( ℂ ⁡ [t]) X=\dot{P}X+P\dot{X},\qquad P=P(t)=\|p_{ij}(t)\|\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}[t]) |  |

with a matrix polynomial P ⁡ ( t) P(t) of some known degree. If required, this identity can be resolved to the form ( 5.5).

#### 6.4. Commentaries

The proof of Lemma 5 and Corollary 2 is based on a finer than before analysis of topology of the bundle H H for polynomials transversal to infinity. In particular, in assumptions of the Lemma, one can choose a special framing of the homology bundle by *vanishing cycles*δ j ​ ( t) \delta_{j}(t), represented by loops on the preimage X t X_{t} that shrinks to a point when t → t j t\to t_{j} (a special precaution is required to avoid problems with multivaluedness). For such choice of the cycles, the period matrix X ⁡ ( t) X(t) must have a vanishing column at each of the points t j t_{j}, for any collection of the framing forms. Next, in this case the determinant det X \det X is a single-valued function that therefore must be a polynomial (being locally bounded everywhere on ℂ {\mathbb{C}}). Its growth as t → ∞ t\to\infty depends on the degrees of the framing forms, since the “size” of the cycles δ j ​ ( t) \delta_{j}(t) grows in a known way (depending only on H H).

All this implies that the determinant of any period matrix det X ⁡ ( t) \det X(t) is a polynomial in t t divisible by ∏ j = 1 μ ( t − t j) \prod_{j=1}^{\mu}(t-t_{j}). The coefficients p j ​ ( t) p_{j}(t) of representation ( 6.1) can be found by solving a system of linear algebraic equations. When solved by the Cramer rule, this system yields p j ​ ( t) p_{j}(t) as a ratio of two determinants, the determinant of the period matrix for the basic forms ω 1, …, ω μ \omega_{1},\dots,\omega_{\mu} in the denominator, and that of a similar period matrix for the collection of 1-forms with ω j \omega_{j} replaced by ω \omega in the numerator. By Lemma 5, these ratios are polynomials in t t and their degrees can be easily majorized in terms of d = deg ⁡ ω d=\deg\omega.

#### 6.5. Multiplicity of the roots of Abelian integrals: constructive finite cyclicity

A similar construction allows to majorize the order of a zero of any Abelian integral, at least under the assumption that H H is transversal to infinity and has only Morse critical points [Mar91]. Instead of the period matrix X X, consider the matrix function J ⁡ ( t) J(t) whose entry J i ​ j ​ ( t) J_{ij}(t) is the ( i − 1) (i-1) -st derivative of the integral I j ​ ( t) = ∮ δ j ​ ( t) ω I_{j}(t)=\oint_{\delta_{j}(t)}\omega.

For the same reasons as before, its determinant w ⁡ ( t) = det J ⁡ ( t) w(t)=\det J(t), the Wronskian of the integrals I 1, …, I μ I_{1},\dots,I_{\mu}, is a single-valued hence rational function of t t. Its poles may occur only at the points t j t_{j} and t = ∞ t=\infty. The assumption on finite singular points implies that all integrals I j ​ ( t) I_{j}(t) have at worst logarithmic growth near each t j t_{j}, and this growth rate allows for differentiation so that I j ( i − 1) ​ ( t) I_{j}^{(i-1)}(t) grows no faster than | t − t j | 1 − j |t-t_{j}|^{1-j} as t → t j t\to t_{j} without spiraling. These estimates imply an upper bound on the total order of all poles of w w at all finite points. The growth rate of w w as t → ∞ t\to\infty depends on deg ⁡ ω \deg\omega and can be easily estimated. This gives an upper bound on the degree ν = deg ⁡ w ⁡ ( t) \nu=\deg w(t) of the rational function (the total number of its poles on ℂ ​ P 1 {\mathbb{C}}P^{1} including those at infinity). This degree is obviously an upper bound for the order of any nontrivial zero of w w. Since the order of the Wronskian w w is equal to μ \mu, the number ν + μ − 1 \nu+\mu-1 is an upper bound for the order of any root of any integral I j ​ ( t) I_{j}(t) at any point t ≠ t j t\neq t_{j}.

#### 6.6. Reservations

Despite more detailed constructions and more accurate considerations, the approach based only on topological ideas cannot provide many important data. For example, even the “constant” c c from Lemma 5 depends in a rather nontrivial way on both H H and the choice of the framing forms ω j \omega_{j}, see [Glu00] and [Nov01a]. Among other things, this means practical impossibility of majorizing the polynomial coefficients p j p_{j} in ( 6.1). The same refers to the derivation of the Picard–Fuchs system: after an accurate computation, it can be reduced to the form determined by three constant matrices P 1, P 2, P 3 P_{1},P_{2},P_{3},

 | ( P 0 + t ​ P 1) ​ X ˙ = P 2 ​ X, P i ∈ Mat μ × μ ⁡ ( ℂ) (P_{0}+tP_{1})\dot{X}=P_{2}X,\qquad P_{i}\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}) |  |

but no bounds on the norms of these matrices (or their inverses) can be obtained except for some especially simple cases.

In short, it is combinatorial parameters like degrees, dimensions, ranks and so on that can be more or less easily derived from even the most explicit topological constructions. In contrast, all magnitude-like parameters (norms, absolute values, diameters of point sets etc.), require additional arguments. Some of them can be obtained using rather elementary algebraic considerations.

### 7. Elementary derivation of the Picard–Fuchs system

In this section we derive yet another Picard–Fuchs system by explicit linear algebraic considerations. The advantage of this approach (besides its transparency) is that it allows to bound explicitly the magnitude of coefficients of the system. In addition, the Picard–Fuchs system obtained this way possesses a nice *hypergeometric*form, exhibiting only Fuchsian singularities (though this fact was not yet fully exploited). However, this transparency and explicitness is achieved at the price of a certain redundancy: the dimension of the system obtained this way, is two times bigger than the minimal possible one.

#### 7.1. Division by the gradient ideal

Division with remainder by an ideal can be expressed in the language of polynomial differential forms. In what follows we consider k k -forms Λ k \Lambda^{k}, k = 0, 1, 2 k=0,1,2, with polynomial coefficients on the plane ℂ 2 {\mathbb{C}}^{2}. The degree of a k k -form *by definition*is the maximum of degrees of its coefficients, plus k k. Under such convention, deg ⁡ ( ξ ∧ η) ⩽ deg ⁡ ξ + deg ⁡ η \deg(\xi\land\eta)\leqslant\deg\xi+\deg\eta for all admissible combination of ranks of ξ \xi and η \eta between 0 0 and 2 2, and also

 | deg ⁡ d ​ ω ⩽ deg ⁡ ω ∀ ω ∈ Λ k, \deg d\omega\leqslant\deg\omega\qquad\forall\omega\in\Lambda^{k}, |  |

for any rank k = 0, 1 k=0,1. The linear space of forms of rank k k and degree d d will be denoted by Λ d k \Lambda_{d}^{k}, and we denote Λ ⩽ d k = Λ 0 k + Λ 1 k + ⋯ + Λ d k \Lambda^{k}_{\leqslant d}=\Lambda^{k}_{0}+\Lambda^{k}_{1}+\cdots+\Lambda^{k}_{d}.

Consider ω = a ​ d ​ x + b ​ d ​ y ∈ Λ 1 \omega=a\,dx+b\,dy\in\Lambda^{1} with only isolated singularities. This implies that the ideal ( a, b) (a,b) generated by the polynomials a, b ∈ ℂ ⁡ [x, y] ≃ Λ 0 a,b\in{\mathbb{C}}[x,y]\simeq\Lambda^{0} has a finite codimension μ \mu in ℂ ⁡ [x, y] {\mathbb{C}}[x,y], that is, there exist μ \mu polynomials r 1, …, r μ ∈ ℂ ⁡ [x, y] r_{1},\dots,r_{\mu}\in{\mathbb{C}}[x,y] such that any polynomial q q from this ring can be represented as

 | q = a ​ v − b ​ u + ∑ 1 μ c i ​ r i, u, v ∈ ℂ ⁡ [x, y], c 1, …, c μ ∈ ℂ. q=av-bu+\sum_{1}^{\mu}c_{i}r_{i},\qquad u,v\in{\mathbb{C}}[x,y],\ c_{1},\dots,c_{\mu}\in{\mathbb{C}}. |  |

Introducing 2-forms Ω = q ​ d ​ x ∧ d ​ y \Omega=q\,dx\land dy, R i = r i ​ d ​ x ∧ d ​ y R_{i}=r_{i}\,dx\land dy, i = 1, …, μ i=1,\dots,\mu, and 1-form η = u ​ d ​ x + v ​ d ​ y \eta=u\,dx+v\,dy the above identity can be rewritten as *division with remainder*,

 | ∀ Ω ∈ Λ 2 ∃ η ∈ Λ 1: Ω = ω ∧ η + R, R = ∑ i = 1 μ c i ​ R i ∈ Λ 2. \forall\Omega\in\Lambda^{2}\quad\exists\eta\in\Lambda^{1}:\qquad\Omega=\omega\land\eta+R,\quad R=\sum_{i=1}^{\mu}c_{i}R_{i}\in\Lambda^{2}. |  | (7.1) |

In particular, any 2-form Ω \Omega can be divided with remainder by the differential d ​ H dH of any polynomial H ∈ Λ 0 H\in\Lambda^{0}. Note that the space of remainders may be arbitrarily enlarged if necessary: the uniqueness of the division ( 7.1) will be lost then, but in exchange one may get better norms of the ratio and remainder.

In general the procedure of division can be very delicate. However, if H H is transversal to infinity, then one can easily describe the outcome, explicitly majorizing the *degrees*of the remainder R ∈ Λ 2 R\in\Lambda^{2} and the incomplete ratio η ∈ Λ 1 \eta\in\Lambda^{1}.

###### Lemma 6 (see [NY01b])

If the polynomial H ∈ Λ 0 H\in\Lambda^{0} of degree n + 1 n+1 is transversal to infinity, then any 2-form Ω \Omega can be divided by d ​ H dH with the incomplete ratio η \eta of degree ⩽ deg ⁡ Ω − deg ⁡ H \leqslant\deg\Omega-\deg H and the remainder R R of degree ⩽ 2 ​ n \leqslant 2n.

###### Proof.

If L ∈ Λ 0 L\in\Lambda^{0} is a homogeneous polynomial of degree n + 1 n+1 without multiple linear factors, then the map between subspaces of homogeneous forms,

 | 𝔍 = 𝔍 L: Λ n 1 → Λ 2 ​ n + 1 2, η ↦ d ​ L ∧ η, \mathfrak{J}=\mathfrak{J}_{L}\colon\Lambda^{1}_{n}\to\Lambda^{2}_{2n+1},\qquad\eta\mapsto dL\land\eta, |  | (7.2) |

is an isomorphism. Indeed, in the bases consisting of all monomial forms of the given degrees, the matrix of 𝔍 \mathfrak{J} is the *Sylvester matrix*whose determinant is the *resultant*of the two partial derivatives L x L_{x} and L y L_{y}. The assumption on H H implies that this resultant is nonzero.

Therefore any homogeneous form Ω \Omega of degree exactly 2 ​ n + 1 2n+1 is divisible by d ​ L dL. Any monomial form of degree greater than 2 ​ n + 1 2n+1 can be represented as a monomial 1-form of degree 2 ​ n + 1 2n+1 times a monomial function and hence is divisible by d ​ L dL*without remainder*with the same relation between the degrees,

 | deg ⁡ Ω ⩾ 2 ​ n + 1 ⟹ Ω = d ​ L ∧ η, deg ⁡ η ⩽ deg ⁡ Ω − deg ⁡ L. \deg\Omega\geqslant 2n+1\implies\Omega=dL\land\eta,\qquad\deg\eta\leqslant\deg\Omega-\deg L. |  |

Applying this observation to all homogeneous components of a 2-form Ω = Ω 0 + ⋯ + Ω 2 ​ n + Ω 2 ​ n + 1 + ⋯ + Ω d = R + Ω 2 ​ n + 1 + ⋯ + Ω d \Omega=\Omega_{0}+\cdots+\Omega_{2n}+\Omega_{2n+1}+\cdots+\Omega_{d}=R+\Omega_{2n+1}+\cdots+\Omega_{d}, we prove the assertion of the Lemma for homogeneous polynomials.

To divide a 2-form Ω \Omega of degree ⩾ 2 ​ n + 1 \geqslant 2n+1 by a nonhomogeneous differential d ​ H = d ​ L + ξ dH=dL+\xi, where L L is the principal homogeneous part of H H, deg ⁡ ξ < deg ⁡ L \deg\xi<\deg L, we divide it by d ​ L dL first, and then transform the result as follows,

 | Ω = d ​ L ∧ η + R = ( d ​ H − ξ) ∧ η + R = d ​ H ∧ η + Ω ′, Ω ′ = R − ξ ∧ η, deg Ω ′ ⩽ max ( deg Ω − deg ξ + deg L, deg R) < deg Ω, \begin{gathered}\Omega=dL\land\eta+R=(dH-\xi)\land\eta+R=dH\land\eta+\Omega^{\prime},\\ \Omega^{\prime}=R-\xi\land\eta,\qquad\deg\Omega^{\prime}\leqslant\max(\deg\Omega-\deg\xi+\deg L,\deg R)<\deg\Omega,\end{gathered} |  |

reducing division of Ω \Omega by d ​ H dH to division of another form Ω ′ \Omega^{\prime} of strictly inferior degree. Iterating this step, we prove the Lemma in the general case. Notice that this is essentially the algorithm of division with remainder of univariate polynomials. ∎

###### Remark.

Lemma 6 is an example of the *redundant*division. For a Hamiltonian H H of degree n + 1 n+1 transversal to infinity, the gradient ideal (ideal of 2-forms divisible by d ​ H dH) has codimension n 2 n^{2}. Indeed, the codimension is equal to the number μ \mu of critical points of H H in ℂ 2 {\mathbb{C}}^{2}, counted with their multiplicities. This latter number is exactly n 2 n^{2} by virtue of Bézout theorem, since no critical points are allowed to “escape to infinity” by the assumption on H H.

On the other hand, the linear space of bivariate monomials of degree ⩽ 2 ​ n − 2 \leqslant 2n-2 (the space of 2-forms Λ ⩽ 2 ​ n 2 \Lambda^{2}_{\leqslant 2n}) is ν = 2 ​ n ​ ( 2 ​ n − 1) / 2 ≈ 2 ​ n 2 \nu=2n(2n-1)/2\approx 2n^{2}, roughly two times greater than μ \mu.

The irredundant analog of this theorem can be easily restored if necessary. However, the choice of monomial 2-forms generating the remainder, will depend on the principal homogeneous part L L of H H.

#### 7.2. Gelfand–Leray residue and derivative

###### Lemma 7

Let ω, η ∈ Λ 1 \omega,\eta\in\Lambda^{1} be two polynomial 1-forms such that

 | d ​ ω = d ​ H ∧ η. d\omega=dH\land\eta. |  |

Then for any continuous family δ ⁡ ( t) \delta(t) of 1-cycles on the level curves H − 1 ​ ( t) H^{-1}(t),

 | d d ​ t ​ ∮ δ ⁡ ( t) ω = ∮ δ ⁡ ( t) η. \frac{d}{dt}\oint_{\delta(t)}\omega=\oint_{\delta(t)}\eta. |  |

The proof in the real case (assuming only smoothness of the forms) can be achieved by integration of d ​ ω d\omega over the annulus between δ ⁡ ( t) \delta(t) and δ ⁡ ( t + Δ ​ t) \delta(t+\Delta t) and passing to limit as Δ ​ t → 0 \Delta t\to 0.

This formula allows to differentiate explicitly Abelian integrals of a form ω \omega, expressing the result as an Abelian integral once again if d ​ ω d\omega is divisible by d ​ H dH. In fact, η \eta can be a *rational*1-form having all zero residues after restriction on each level curve H − 1 ​ ( t) H^{-1}(t).

###### Example 7.1.

Let H ⁡ ( x, y) = x 2 + y 2 H(x,y)=x^{2}+y^{2} and ω = y ​ d ​ x \omega=y\,dx. Then ∮ H = t ω = − π ​ t \oint_{H=t}\omega=-\pi t (consider only the real values of t t and use the Stokes formula for the circle positively oriented). Clearly, the form η = 1 2 ​ y − 1 ​ d ​ x \eta=\tfrac{1}{2}y^{-1}\,dx satisfies the assumption of the Lemma, and indeed

 | ∮ H = t η = ∫ 0 2 ​ π 1 2 ⋅ d ​ cos ⁡ s sin ⁡ s = − π. \oint_{H=t}\eta=\int_{0}^{2\pi}\frac{1}{2}\cdot\frac{d\cos s}{\sin s}=-\pi. |  |

This example helps to memorize the order of the wedge multiplication in the Gelfand–Leray formula. ∎

#### 7.3. Derivation of the redundant Picard–Fuchs system

The linear space Λ ⩽ 2 ​ n 2 \Lambda^{2}_{\leqslant 2n} of possible remainders occurring in the division ( 7.1), is spanned by monomial forms x r ​ y s ​ d ​ x ∧ d ​ y x^{r}y^{s}\,dx\land dy, r + s ⩽ 2 ​ n − 2 r+s\leqslant 2n-2. Denote its dimension ( 2 ​ n − 1) ​ n (2n-1)n by ν \nu and choose any monomial primitives ω i \omega_{i}, i = 1, …, ν i=1,\dots,\nu, so that d ​ ω i d\omega_{i} span the quotient space Λ ⩽ 2 ​ n 2 / d ​ Λ ⩽ 2 ​ n 1 \Lambda^{2}_{\leqslant 2n}/d\Lambda^{1}_{\leqslant 2n} (modulo exact forms). Below we refer to ω i \omega_{i} as the *basic*forms.

Consider the 2-forms H ​ d ​ ω i ∈ Λ ⩽ 3 ​ n + 1 2 H\,d\omega_{i}\in\Lambda^{2}_{\leqslant 3n+1} and divide them with remainder by d ​ H dH:

 | H d ω i = d H ∧ η i + R i, i = 1, …, ν. H\,d\omega_{i}=dH\land\eta_{i}+R_{i},\qquad i=1,\dots,\nu. |  | (7.3) |

By the assertion on the degrees, deg ⁡ η i ⩽ deg ⁡ ω i + deg ⁡ H − deg ⁡ d ​ H ⩽ deg ⁡ ω i ⩽ 2 ​ n \deg\eta_{i}\leqslant\deg\omega_{i}+\deg H-\deg dH\leqslant\deg\omega_{i}\leqslant 2n, therefore each of the forms can be represented (modulo an exact polynomial form) as a linear combination of the basic forms,

 | η i = ∑ j = 1 ν b i ​ j ​ ω j + d ​ F i, b i ​ j ∈ ℂ, F i ∈ Λ ⩽ 2 ​ n 0. \eta_{i}=\sum_{j=1}^{\nu}b_{ij}\omega_{j}+dF_{i},\qquad b_{ij}\in{\mathbb{C}},\ F_{i}\in\Lambda^{0}_{\leqslant 2n}. |  |

Similarly, being all of degree ⩽ 2 ​ n \leqslant 2n, the remainders R i ∈ Λ ⩽ 2 ​ n 2 R_{i}\in\Lambda^{2}_{\leqslant 2n} can be represented as linear combinations of the forms d ​ ω i d\omega_{i}:

 | R i = ∑ j = 1 ν a i ​ j ​ d ​ ω j, a i ​ j ∈ ℂ. R_{i}=\sum_{j=1}^{\nu}a_{ij}\,d\omega_{j},\qquad a_{ij}\in{\mathbb{C}}. |  |

Let δ ⁡ ( t) \delta(t) be any continuous family of cycles. Then for any t ∉ Σ t\notin\varSigma the forms

 | H ​ d ​ ω i − ∑ j = 1 ν a i ​ j ​ d ​ ω j, ∀ i = 1, …, ν, H\,d\omega_{i}-\sum_{j=1}^{\nu}a_{ij}d\omega_{j},\qquad\forall i=1,\dots,\nu, |  |

are all divisible by d ​ H dH with the ratios being cohomologous to ∑ j = 1 ν b i ​ j ​ ω j \sum_{j=1}^{\nu}b_{ij}\omega_{j}. Denote

 | X i ( t) = ∮ δ ⁡ ( t) ω i, i = 1, …, ν. X_{i}(t)=\oint_{\delta(t)}\omega_{i},\qquad i=1,\dots,\nu. |  |

Note that integration of a form H ​ ω H\omega over any cycle δ ⊂ { H = t } \delta\subset\{H=t\} yields t ​ ∮ δ ω t\oint_{\delta}\omega, since H H is constant on the cycle. Integrating both sides over the oval δ ⁡ ( t) \delta(t) and using the Gelfand–Leray formula, we arrive to the identities

 | t ​ X ˙ i ​ ( t) − ∑ j = 1 ν a i ​ j ​ X ˙ j ​ ( t) = ∑ j = 1 ν b i ​ j ​ X j ​ ( t), t\dot{X}_{i}(t)-\sum_{j=1}^{\nu}a_{ij}\dot{X}_{j}(t)=\sum_{j=1}^{\nu}b_{ij}X_{j}(t), |  | (7.4) |

which means that the *column*vector ( X 1, …, X ν) (X_{1},\dots,X_{\nu}) of Abelian integrals satisfies the system of linear ordinary differential equations

 | ( t E − A) X ˙ = B X, X ∈ ℂ ν, A, B ∈ Mat ν × ν ( ℂ), (tE-A)\dot{X}=BX,\qquad X\in{\mathbb{C}}^{\nu},\quad A,B\in\operatorname{Mat}_{\nu\times\nu}({\mathbb{C}}), |  | (7.5) |

with the constant matrices A = ‖ a i ​ j ‖ A=\|a_{ij}\|, B = ‖ b i ​ j ‖ B=\|b_{ij}\| as parameters ( E E is the identity matrix). Writing

 | ( t ​ E − A) − 1 = 1 χ ⁡ ( t) ⋅ P ⁡ ( t), P = ∑ k = 0 ν − 1 P k ​ t k, χ ⁡ ( t) = det ( t ​ E − A), (tE-A)^{-1}=\frac{1}{\chi(t)}\cdot P(t),\qquad P=\sum_{k=0}^{\nu-1}P_{k}t^{k},\ \chi(t)=\det(tE-A), |  | (7.6) |

where P ⁡ ( t) P(t) is a matrix polynomial of degree ν − 1 \nu-1, the adjugate matrix for t ​ E − A tE-A, one sees immediately that ( 7.5) is a system of linear ordinary differential equations with rational coefficients.

#### 7.4. Hypergeometric systems

The form ( 7.5) is rather specific: for instance, all singular points of this system are Fuchsian (simple poles), including the point at t = ∞ t=\infty. This is obvious if the spectrum of A A is simple, but holds true in the general case as well, as follows from the explicit formula for ( t ​ E − A) − 1 (tE-A)^{-1} for A A in the Jordan normal form.

It would be appropriate to remark here that the residues A j A_{j} of the Fuchsian system ( 4.2) are invariant by any conformal change of the independent variable t t. In the case of hypergeometric systems ( 7.5) the point t = ∞ t=\infty is distinguished: the residues A j A_{j} at all finite points t j ∈ Spec ⁡ A t_{j}\in\operatorname{Spec}A have rank 1 1 for a generic matrix A A, whereas the rank of the residue A ∞ = − ∑ 1 μ A j A_{\infty}=-\sum_{1}^{\mu}A_{j} at infinity is generically full. Thus the natural symmetry group of hypergeometric systems is not the full group of conformal automorphisms of ℂ ​ P 1 {\mathbb{C}}P^{1}, but rather the affine group of transformations t ↦ a ​ t + b t\mapsto at+b, a, b ∈ ℂ a,b\in{\mathbb{C}} fixing the point t = ∞ t=\infty. Making an affine transformation transforms the system ( 7.5) into the system ( t ​ E + A ′) ​ X ˙ = B ′ ​ X (tE+A^{\prime})\dot{X}=B^{\prime}X with the same matrix B ′ = B B^{\prime}=B and A ′ = a − 1 ​ ( A − b ​ E) A^{\prime}=a^{-1}(A-bE).

In the subsequent sections it will be shown that in order to estimate the number of isolated zeros of solutions to Fuchsian systems, it is sufficient to know the norms of the residue matrices. As follows from the explicit inversion formula ( 7.6), norms of the residues can be bounded if the norm ‖ A ‖ \|A\| is bounded from above and pairwise distances between the critical points t j t_{j} are bounded *from below*. Of course, choosing a suitable affine transformation as above, one can change the norm ‖ A ‖ \|A\|, but at the same rate the distances between the singular points (eigenvalues of A A) will be affected. In other words, the norm of the matrix ‖ A ‖ \|A\| should be majorized relative to the spread of its eigenvalues.

#### 7.5. Explicitness and bounds

The above derivation does not involve any existential assertion: all constructions are completely transparent and allow for explicit bounds, say, on the norms of the matrices A, B A,B from ( 7.5). To do this, we introduce the norms on the ring of polynomials, letting ‖ p ‖ \|p\| being the sum of absolute values of all its coefficients. This norm is multiplicative, ‖ p ​ q ‖ ⩽ ‖ p ‖ ​ ‖ q ‖ \|pq\|\leqslant\|p\|\,\|q\|, and extends on polynomial k k -forms, remaining multiplicative with respect to the wedge product. The exterior derivative is a bounded operator on forms of bounded degrees.

The entries of the matrices A, B A,B appear as coefficients of linear expansion of a known 1 1 -form in the chosen basis. But since the basic forms ω i \omega_{i} are *monomial*with coefficients equal to 1 1, to majorize these entries it is sufficient to majorize the norms of the 2-forms R i R_{i} (the remainders) and 1-forms η i \eta_{i} (incomplete ratios). In other words, one has to control only the division step, since multiplication by H H is an operator whose norm is no greater than ‖ H ‖ \|H\|.

The division step is also rather transparent, its well-posedness being determined by the norm of the inverse Sylvester matrix 𝔍 L \mathfrak{J}_{L} from ( 7.2) and the norm of the non-principal terms ‖ H − L ‖ \|H-L\|, where L L is the principal homogeneous part of H H. The group of affine transformations of the complex plane ℂ 2 {\mathbb{C}}^{2} naturally acts on the space of all Hamiltonians of degree n + 1 n+1 not affecting the critical values of H H. By an appropriate transformation of this group, one can always achieve the normalizing condition ‖ 𝔍 L − 1 ‖ = 1 \|\mathfrak{J}_{L}^{-1}\|=1 that is a condition on the principal homogeneous part L L. The problem on bounding the norm ‖ A ‖ \|A\| is reduced therefore to studying how the magnitude of the non-principal coefficients of H − L H-L may affect configuration of the critical values of H H subject to the above normalizing condition on the principal part L L. The problem can be explicitly solved for the univariate polynomials, implying an answer in the hyperelliptic case as well [NY01b]. Moreover, one can show that if all critical values of a bivariate polynomial transversal to infinity coincide, then necessarily the polynomial H H must coincide with its principal part, being thus homogeneous, eventually after a suitable parallel translation in the ( x, y) (x,y) -plane. The inequality between the non-homogeneity of a bivariate polynomial and the spread of its critical values is still unknown, see [NY01b] for partial results.

#### 7.6. Preliminary conclusion

The tangential Hilbert problem for generic Hamiltonians, gets reduced to the question about the number of isolated zeros of linear combinations of functions satisfying together a system of linear ordinary differential equations with rational coefficients.

The procedure of derivation of this system is very transparent. In particular, it can be written in the hypergeometric form ( 7.5) with explicit bounds on the norms of the corresponding matrices A A and B B. These bounds in turn imply that when reduced to the Fuchsian form ( 4.3), the system will have the residue matrices A j A_{j} bounded (as usual, in the sense of the norms) in terms of the inverse distance max i ≠ j ⁡ { | t i − t j | − 1, | t i | } \max_{i\neq j}\left\{|t_{i}-t_{j}|^{-1},|t_{i}|\right\} between singular points of the system.

When this inverse distance tends to infinity (which corresponds to confluence of singular points), the resulting bounds on the norms ‖ A j ‖ \|A_{j}\| of the residues in ( 4.3) explode. However, this explosion is of a very specific nature: the monodromy group of the system with one or several confluent singularities, remains the same. In particular, the spectral data of the residues remain bounded.

In the subsequent lectures we will find out how far away are these conditions from sufficient conditions allowing for an explicit solution of the tangential Hilbert problem.

## Lecture III Quasialgebraicity of function fields

Starting from this moment, we will pursue the same path towards the tangential Hilbert problem, but this time in the opposite direction. Namely, we will establish conditions on Fuchsian systems guaranteeing that their solutions are similar to algebraic functions, in particular, admit explicit bounds for the number of isolated zeros.

### 8. Functional fields and their quasialgebraicity

The main objects of study in this section are functional fields obtained by adjoining one or several analytic (in general, multivalued) functions to the field ℂ {\mathbb{C}} of complex numbers (or slightly more generally to that of rational functions ℂ ⁡ ( t) {\mathbb{C}}(t)). Such fields admit filtration (grading) by degrees.

The goal is to obtain conditions on the field (in terms of properties of the adjoined functions) guaranteeing that the question on the *global*number of isolated zeros of functions from this field can be *algorithmically*(effectively) solved. An accurate definition will be given at an appropriate moment, after explaining all technicalities pertinent to the problem. We begin by examples illustrating the goals.

#### 8.1. Algebraic functions

The field of rational functions ℂ ⁡ ( t) {\mathbb{C}}(t) in one variable t t possesses the following obvious but nevertheless remarkable property:

1. (1)

any element f ⁡ ( t) = p ⁡ ( t) / q ⁡ ( t) f(t)=p(t)/q(t), p, q ∈ ℂ ⁡ [t] p,q\in{\mathbb{C}}[t] from this field has a well defined degree deg ⁡ f = max ⁡ ( deg ⁡ p, deg ⁡ q) \deg f=\max(\deg p,\deg q) (assuming that the representation is irreducible), and

2. (2)

the number of isolated zeros of f f on the whole projective line ℂ ​ P 1 = ℂ ∪ { ∞ } {\mathbb{C}}P^{1}={\mathbb{C}}\cup\{\infty\} is no greater than deg ⁡ f \deg f (actually, equal to it if counted with multiplicities).

In other words, there is a direct relationship between the combinatorial complexity of representation of f f in the field (i.e., the number of field operations necessary to produce f f from constants and the independent variable t t), and its analytic complexity measured by the number of isolated zeros.

This example can be easily generalized by considering fields generated by one or several algebraic functions.

Let f i ​ ( t) f_{i}(t), i = 1, …, n i=1,\dots,n be algebraic functions of one variable, defined implicitly by the polynomial equations

 | P i ( t, x i) = 0, P i ∈ ℂ [t, x i], deg P i = d i, i = 1, …, n, P_{i}(t,x_{i})=0,\qquad P_{i}\in{\mathbb{C}}[t,x_{i}],\quad\deg P_{i}=d_{i},\quad i=1,\dots,n, |  |

with respect to x i x_{i}. Consider the ring ℂ ⁡ [f 1, …, f n] {\mathbb{C}}[f_{1},\dots,f_{n}] formed by polynomial combinations of the functions f i f_{i}, and the corresponding field of fractions ℂ ⁡ ( f 1, …, f n) {\mathbb{C}}(f_{1},\dots,f_{n}). Both consist of analytic multivalued functions ramified over a finite point set on the projective line ℂ ​ P 1 {\mathbb{C}}P^{1}, though the number of distinct branches of every function is finite (no more than d 1 ⋯ d n d_{1}\cdots d_{n}).

One can define unambiguously the degree of functions in this ring and the respective field as the degree d d of the *minimal*representation

 | f = ∑ | α | ⩽ d c α ​ f α, α = ( α 1, …, α n) ∈ ℤ + n, c α ∈ ℂ, f α = ∏ 1 n f i α i. f=\sum_{|\alpha|\leqslant d}c_{\alpha}f^{\alpha},\qquad\alpha=(\alpha_{1},\dots,\alpha_{n})\in\mathbb{Z}^{n}_{+},\ c_{\alpha}\in{\mathbb{C}},\ f^{\alpha}=\prod_{1}^{n}f_{i}^{\alpha_{i}}. |  |

###### Proposition 3

The total number of isolated zeros of a polynomial combination f ⁡ ( t) = P ⁡ ( f 1 ​ ( t), …, f n ​ ( t)) f(t)=P(f_{1}(t),\dots,f_{n}(t)), f ∈ ℂ ⁡ [f 1, …, f n] f\in{\mathbb{C}}[f_{1},\dots,f_{n}] of degree ⩽ d \leqslant d on all branches of this function, does not exceed d ⋅ d 1 ⋯ d n d\cdot d_{1}\cdots d_{n}.

###### Proof.

This is an immediate corollary to the Bézout theorem applied to the system of algebraic equations

 | { P 1 ​ ( t, x 1) = 0, ⋮ P n ​ ( t, x n) = 0, P ⁡ ( x 1, …, x n) = 0. \left\{\begin{aligned} P_{1}(t,x_{1})&=0,\\ \vdots\qquad&\\ P_{n}(t,x_{n})&=0,\\ P(x_{1},\dots,x_{n})&=0.\end{aligned}\right. |  |

The same proof actually works for a more general case of functions f i f_{i} defined by a system of algebraic equations P i ​ ( t, x 1, …, x n) = 0 P_{i}(t,x_{1},\dots,x_{n})=0, i = 1, …, n i=1,\dots,n, involving all functions *simultaneously*. ∎

###### Remark.

The function f 0 ​ ( t) = t f_{0}(t)=t is clearly algebraic, and if required, we can always assume it being among the collection of the functions f i f_{i}, thus avoiding particular cases and awkward notation. This agreement will allow us to assume that all functional fields are extensions of the field ℂ ⁡ ( t) {\mathbb{C}}(t).

#### 8.2. Existential quasialgebraicity

Some parts of the above construction can be reproduced in a completely general context. Let U ⊂ ℂ U\subset{\mathbb{C}} be an open domain (for simplicity assume it to be bounded, connected and simply connected).

Consider an arbitrary collection of n n functions F = { f 1 ​ ( t), …, f n ​ ( t) } F=\{f_{1}(t),\dots,f_{n}(t)\} analytic in U U. They define the ring ℂ ⁡ [F] {\mathbb{C}}[F] and the corresponding field ℂ ⁡ ( F) {\mathbb{C}}(F) of functions meromorphic in U U. As before, for any function f ∈ ℂ ⁡ [F] f\in{\mathbb{C}}[F] one can define its degree as the minimal possible degree of the polynomial P ∈ ℂ ⁡ [x 1, …, x n] P\in{\mathbb{C}}[x_{1},\dots,x_{n}] realizing the given function f ⁡ ( t) = P ⁡ ( F ⁡ ( t)) = P ⁡ ( f 1 ​ ( t), …, f n ​ ( t)) f(t)=P(F(t))=P(f_{1}(t),\dots,f_{n}(t)) (there can be algebraically dependent functions among the generators). This grading extends naturally for rational combinations from ℂ ⁡ ( F) {\mathbb{C}}(F).

###### Proposition 4

For any compact K ⋐ U K\Subset U there exists a counting function C = C K: ℕ → ℕ C=C_{K}\colon\mathbb{N}\to\mathbb{N}, taking only finite values C K ​ ( d) < + ∞ C_{K}(d)<+\infty for any finite d d, such that the number of isolated zeros of any function f f in K K can be at most C K ​ ( d) C_{K}(d):

 | deg ⁡ f ⩽ d ⟹ #⁡ { t ∈ K: f ⁡ ( t) = 0 } ⩽ C K ​ ( d). \deg f\leqslant d\implies\#\{t\in K\colon f(t)=0\}\leqslant C_{K}(d). |  |

###### Proof.

First we show that under the assumptions of the Theorem, the number of isolated zeros of any *linear*combination f c ​ ( t) = ∑ c i ​ f i ​ ( t) f_{c}(t)=\sum c_{i}f_{i}(t) with complex constant coefficients c 1, …, c n ∈ ℂ c_{1},\dots,c_{n}\in{\mathbb{C}}, is bounded in any compact K K uniformly over all such linear combinations. Indeed, without loss of generality we may assume that the functions f i f_{i} are linear independent—this does not affect the supply of all linear combinations. Next, it is sufficient to consider only combinations with coefficients on the unit sphere, satisfying the equality ∑ j | c j | 2 = 1 \sum_{j}|c_{j}|^{2}=1. The functions f c f_{c} for such c c are all different from identical zero, hence each of them has only a finite number of isolated zeros in the compact K K (accumulation of roots to the boundary of K K is forbidden). Now the standard semicontinuity arguments using compactness of the unit sphere, prove that the number of zeros of all f c f_{c} is uniformly bounded.

To deal with arbitrarily polynomial combinations, we can treat them as linear combinations of *monomials*f α ​ ( t) f^{\alpha}(t), | α | ⩽ d |\alpha|\leqslant d, reducing the general case to the already studied one. ∎

###### Remark.

One can easily recognize in this demonstration some minor variations on the theme already exposed in § 1. Of course, Proposition 4 follows from Theorem 2, since the parameters c α c_{\alpha} can be considered varying over the compact sphere. Here we could explicitly avoid dealing with functions vanishing identically for some values of the parameters, simplifying considerably the proof.

#### 8.3. Comparison

Two above finiteness assertions, Propositions 3 and 4, differ in two important instances:

1. (1)

the bounds on roots of algebraic functions are *global*, i.e., valid on the maximal domain of definition of the functions from the field ℂ ⁡ ( F) {\mathbb{C}}(F), whereas the bounds on the roots of arbitrary analytic functions in general depend on the choice of the compact K K and can in many cases blow up as the compact approaches the boundary of the maximal domain U U;

2. (2)

the bounds on roots of algebraic functions are given by an explicit formula involving some basic parameters defining the field, whereas the function C K ​ ( d) C_{K}(d) is totally existential (see below).

The nature of the counting function C K ​ ( d) C_{K}(d) from Proposition 4 remains totally non-effective. One can easily construct examples of functions (even entire functions) such that the growth of C K ​ ( d) C_{K}(d) will be arbitrarily fast [IY96].

#### 8.4. In search of quasialgebraicity: reappearance of Picard–Vessiot extensions

Our goal is to provide sufficient conditions on the functions f i f_{i} guaranteeing that the corresponding field will be similar to the field obtained by adjoining algebraic functions. This condition, still understood informally until made precise in § 10, will be referred to as *quasialgebraicity*of the function field. The accurate definition is postponed since it involves some technical details.

However, even prior to giving any accurate formulation, the class of function fields among which one could hope to find nontrivial cases of quasialgebraicity, can be substantially restricted.

First, *the generating functions f 1, …, f n f_{1},\dots,f_{n} must be multivalued*(ramified). Indeed, a single-valued function having at most polar singularities on the projective line ℂ ​ P 1 {\mathbb{C}}P^{1} (recall that we are looking for *global*bounds, hence the functions should be defined globally), must be rational. Any field generated by such functions, is a subfield of ℂ ⁡ ( t) {\mathbb{C}}(t) and hence we get nothing new.

On the other hand, if one of the functions f i f_{i} has an essential singularity on ℂ ​ P 1 {\mathbb{C}}P^{1}, then by classical theorems of complex analysis this function near such point must take infinitely many times almost all values, hence one can easily construct an *individual*polynomial combination having infinitely many roots accumulating to the essential singularity. This precludes quasialgebraicity whatever exact meaning it may be assigned.

Thus any field (or ring, what is almost the same for our purposes) exhibiting nontrivial quasialgebraicity, must consist of functions ramified over some finite set Σ ⊂ ℂ ​ P 1 \varSigma\subset{\mathbb{C}}P^{1}. As above, globality means that functions should be analytically continuable along any path avoiding the ramification locus Σ \varSigma.

The possibility of analytic continuation along paths (and loops) introduces an additional structure, the monodromy group action. Choose arbitrarily a nonsingular point a ∉ Σ a\notin\varSigma. Then any element from the ring ℂ ⁡ [F] {\mathbb{C}}[F] can be identified with the full analytic continuation of its germ at a a. Denote as in § 5 the monodromy operator associated with a loop γ ∈ π 1 ​ ( ℂ ∖ Σ, a) \gamma\in\pi_{1}({\mathbb{C}}\smallsetminus\varSigma,a) by Δ γ \Delta_{\gamma}. Then it would be natural to assume that ℂ ⁡ [F] {\mathbb{C}}[F] is closed (invariant) by analytic continuations, that is,

 | Δ γ ​ f i ∈ ℂ ⁡ [f 1, …, f μ] ∀ γ ∈ π 1 ​ ( ℂ ​ P 1 ∖ Σ, a). \Delta_{\gamma}f_{i}\in{\mathbb{C}}[f_{1},\dots,f_{\mu}]\qquad\forall\gamma\in\pi_{1}({\mathbb{C}}P^{1}\smallsetminus\varSigma,a). |  | (8.1) |

Moreover, since the filtration of the ring ℂ ⁡ [F] {\mathbb{C}}[F] by degrees should be well-defined, it must be preserved by analytic continuations, that is, continuation of a polynomial f = P ⁡ ( f 1, …, f μ) f=P(f_{1},\dots,f_{\mu}) (of minimal degree among all polynomials representing the given f f) along any loop should again be a polynomial of the same degree. In particular, *the ℂ {\mathbb{C}} -linear span of the germs f 1, …, f μ f_{1},\dots,f_{\mu} in the space of all analytic germs must be invariant by all monodromy operators*. In other words, there should exist invertible square matrices M γ M_{\gamma} such that

 | Δ γ ​ ( f 1, …, f n) = ( f 1, …, f n) ⋅ M γ. \Delta_{\gamma}(f_{1},\dots,f_{n})=(f_{1},\dots,f_{n})\cdot M_{\gamma}. |  |

In the same way as in § 5, this implies that the functions f 1, …, f μ f_{1},\dots,f_{\mu} must be solutions of a linear ordinary differential equation with single-valued coefficients on ℂ ​ P 1 ∖ Σ {\mathbb{C}}P^{1}\smallsetminus\varSigma. As before, allowing essential singularities of the coefficients would immediately relinquish any control over nonaccumulation of roots of solutions, hence we arrive to the following important conclusion: *To be quasialgebraic, the field ℂ ⁡ ( F) = ℂ ⁡ ( f 1, …, f μ) {\mathbb{C}}(F)={\mathbb{C}}(f_{1},\dots,f_{\mu}) must be a Picard–Vessiot extension of ℂ {\mathbb{C}} or ℂ ⁡ ( t) {\mathbb{C}}(t) obtained by adjoining solutions of a linear ordinary differential equation with rational coefficients*.

This fact, in particular, implies that adding to the generating tuple of functions ( f 1, …, f n) (f_{1},\dots,f_{n}) their derivatives of orders ⩽ n − 1 \leqslant n-1 will make the field ℂ ⁡ ( t, f 1, …, f n) {\mathbb{C}}(t,f_{1},\dots,f_{n}) a *differential field*(closed by differentiation). Without loss of generality we can assume that such completion was already done and we deal with the differential field ℂ ⁡ ( X) {\mathbb{C}}(X) (and the corresponding ring ℂ ⁡ [X] {\mathbb{C}}[X]) obtained by adjoining to ℂ {\mathbb{C}} all entries of a fundamental matrix solution X ⁡ ( t) X(t) for a system of first order linear ordinary differential equations with rational coefficient matrix,

 | X ˙ ​ ( t) = A ⁡ ( t) ​ X ​ ( t), A ⁡ ( t) ∈ Mat μ × μ ⁡ ( ℂ ⁡ ( t)). \dot{X}(t)=A(t)X(t),\qquad A(t)\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}(t)). |  | (8.2) |

In the particular case we are discussing, one can take X X to be the Wronskian matrix of the collection { f i } \{f_{i}\}, X i ​ j ​ ( t) = f j ( i − 1) ​ ( t) X_{ij}(t)=f_{j}^{(i-1)}(t), i, j = 1, …, n i,j=1,\dots,n.

#### 8.5. Quasialgebraicity of Fuchsian systems: examples and counterexamples

As in the case of single-valued functions, a precondition for quasialgebraicity is nonaccumulation of roots of solutions to singular points. Singularities of linear systems ( 8.2) can be easily described: they occur only at the poles of the coefficients matrix A ⁡ ( t) A(t) or rather at the poles of the matrix-valued differential 1-form A ⁡ ( t) ​ d ​ t A(t)\,dt on the Riemann sphere ℂ ​ P 1 {\mathbb{C}}P^{1}. The corresponding classical theory [Har82] distinguishes between two types of singularities:

- •

those exhibiting at most polynomial growth of entries of the fundamental matrix X ⁡ ( t) X(t) and its inverse X − 1 ​ ( t) X^{-1}(t) and called *regular singularities*, and

- •

those exhibiting abnormally fast (faster than polynomial) growth of solutions, called *irregular singularities*.

###### Remark.

In order to measure growth rate of multivalued functions near a ramification point, they should be restricted on a sector bounded by two rectilinear rays with the vertex at this point. Otherwise one can construct a curve approaching the singular point while spiraling around it in such a way that the growth in terms of the distance to the singularity will be arbitrarily fast even for the most innocent multivalued function ln ⁡ t \ln t.

The dichotomy between regular and irregular singularities is closely related to dichotomy between poles and essential singularities for single-valued functions. Consider a neighborhood of a singular point t ∗ ∈ Σ t_{*}\in\varSigma, assuming for simplicity that t ∗ = 0 t_{*}=0. Let M M be the monodromy operator associated with a small loop around the origin, so that

 | Δ γ ​ X ​ ( t) = X ⁡ ( t) ​ M, det M ≠ 0. \Delta_{\gamma}X(t)=X(t)M,\qquad\det M\neq 0. |  | (8.3) |

Let A ∈ Mat μ × μ ⁡ ( ℂ) A\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}) be any matrix logarithm of M M, so that

 | exp ⁡ 2 ​ π ​ i ​ A = M. \exp 2\pi iA=M. |  |

Then the multivalued matrix function t A = exp ⁡ ( A ​ ln ⁡ t) t^{A}=\exp(A\ln t) also has the same monodromy,

 | Δ γ ​ t A = exp ⁡ ( A ​ Δ γ ​ ln ⁡ t) = exp ⁡ ( A ⁡ ( ln ⁡ t + 2 ​ π ​ i)) = t A ​ M = M ​ t A. \Delta_{\gamma}\,t^{A}=\exp(A\Delta_{\gamma}\ln t)=\exp(A(\ln t+2\pi i))=t^{A}M=Mt^{A}. |  |

Therefore the matrix ratio H ⁡ ( t) = X ⁡ ( t) ​ t − A H(t)=X(t)t^{-A} is single-valued in a small punctured neighborhood of 0 0. If the origin is a regular singularity, then H ⁡ ( t) H(t) has at most a pole and hence by choosing a different valuation of the logarithm and replacing t A t^{A} by t k ​ E + A t^{kE+A} for sufficiently large natural k k, one can make H ⁡ ( t) H(t) holomorphic at the origin. By explicit elementary formulas for matrix exponents, one can derive from this a local representation of entries of the matrix X ⁡ ( t) X(t) in the form

 | ∑ k, λ h k ​ λ ​ ( t) ​ t λ ​ ln k − 1 ​ t \sum_{k,\lambda}h_{k\lambda}(t)\,t^{\lambda}\ln^{k-1}t |  |

with the exponents λ \lambda ranging over the spectrum of A A, the natural k k being no greater than the maximal size of Jordan blocks of A A and h k ​ λ ​ ( t) h_{k\lambda}(t) holomorphic at t = 0 t=0. Notice the remarkable coincidence with ( 4.1) and Exercise 1.2: the latter implies that at least in the situation when all functions h k ​ λ h_{k\lambda} and all eigenvalues of A A are real, isolated zeros cannot accumulate to the regular singularity at the origin.

If, on the other hand, the singularity is irregular, then at least some entries of the matrix H ⁡ ( t) H(t) must exhibit essential singularity at the origin. In the same way as with single-valued function, one can in this case construct functions from ℂ ⁡ ( X) {\mathbb{C}}(X) that would have infinitely many roots accumulating to the origin.

###### Example 8.1.

The linear system

 | { x ˙ 1 = t − 2 ​ x 1, x ˙ 2 = 0 \left\{\begin{aligned} \dot{x}_{1}&=t^{-2}{x_{1}},\\ \dot{x}_{2}&=0\end{aligned}\right. |  | (8.4) |

generates the field ℂ ⁡ ( X) {\mathbb{C}}(X) containing a function f ( t) = exp ( − 1 / t) − 1 f(t)=\exp(-1/t)-1 whose zeros at the points t m = ( 2 ​ π ​ i ​ m) − 1 t_{m}=(2\pi im)^{-1}, m = ± 1, ± 2, … m=\pm 1,\pm 2,\dots accumulate to two essentially singular points at t = 0 t=0 and t = ∞ t=\infty along the imaginary axis. ∎

Thus occurrence of irregular singularities destroys any hope to achieve quasialgebraicity, and we are left with the class of Picard–Vessiot extensions exhibiting only regular singularities.

There is a simple sufficient condition guaranteeing that a singular point of the linear system ( 8.2) is regular. By the Fuchs theorem [Har82], if A ⁡ ( t) A(t) has a *simple pole*(of the first order) at a point t ∗ t_{*}, then this point is a regular singularity. Such singularities are called *Fuchsian*.

The inverse to the Fuchs theorem is in general not true: there exist regular non-Fuchsian singularities. But a system exhibiting regular singularity at t ∗ t_{*}, by a *meromorphic*(locally near t ∗ t_{*}) linear transformation X ⁡ ( t) ↦ R ⁡ ( t) ​ X ​ ( t) X(t)\mapsto R(t)X(t) can be reduced to the system having a simple pole at t ∗ t_{*}. Thus on the level of *local meromorphic equivalence*there is no difference between Fuchsian and regular singularities.

For a globally defined system exhibiting several regular singularities at finitely many points Σ = { t 1, …, t d } \varSigma=\{t_{1},\dots,t_{d}\} on the projective line, one can ask whether there exists a globally meromorphic (hence *rational*) linear transformation simultaneously taking all regular singularities into Fuchsian ones. The problem (that constitutes a part of the so called Riemann–Hilbert, or 21st Hilbert problem) turns out to be very delicate, the result depending essentially on the structure of the monodromy group of the system, and not always admitting solution, as shown recently by A. Bolibruch [Bol95, Bol90]. However, from the classical result by Plemelj [Ple64, For91] it follows that if an additional singular point is allowed to be created anywhere, then the answer is always positive and a rational matrix function R ⁡ ( t) R(t) can be found such that Y ⁡ ( t) = R ⁡ ( t) ​ X ​ ( t) Y(t)=R(t)X(t) satisfies a system of linear ordinary differential equations having only Fuchsian singularities on the whole projective line ℂ ​ P 1 {\mathbb{C}}P^{1}. Clearly, if t ∈ ℂ ⁡ ( X) t\in{\mathbb{C}}(X) (which we may always assume without loss of generality, as noted above), then ℂ ⁡ ( X) = ℂ ⁡ ( Y) {\mathbb{C}}(X)={\mathbb{C}}(Y) and hence when discussing quasialgebraicity, one can deal with Fuchsian systems only.

A Fuchsian system with d d finite singular points t 1, …, t d t_{1},\dots,t_{d} can always be written in the form

 | d ​ x d ​ t = A ( t) x, A ( t) = ∑ j = 1 d A j t − t j, x ∈ ℂ n, A j ∈ Mat n × n ( ℂ), t ∈ ℂ, t 1, …, t d ∈ ℂ, \begin{gathered}\frac{dx}{dt}=A(t)x,\qquad A(t)=\sum_{j=1}^{d}\frac{A_{j}}{t-t_{j}},\\ x\in{\mathbb{C}}^{n},\quad A_{j}\in\operatorname{Mat}_{n\times n}({\mathbb{C}}),\quad t\in{\mathbb{C}},\quad t_{1},\dots,t_{d}\in{\mathbb{C}},\end{gathered} |  | (8.5) |

explicitly indicating the corresponding residue matrices A j A_{j} (we return to the initial notation X X for the dependent variables). Thus the natural problem arises, *When the Picard–Vessiot extension ℂ ⁡ ( X) {\mathbb{C}}(X) constructed by adjoining all components of the fundamental matrix solution of a Fuchsian system ( 8.5), is quasialgebraic?*Note that this field depends not on the choice of the matrix solution X ⁡ ( t) X(t) but rather on its “logarithmic derivative” A ⁡ ( t) = X ˙ ​ ( t) ​ X − 1 ​ ( t) A(t)=\dot{X}(t)X^{-1}(t) which is a rational matrix function. The Fuchsian system ( 8.5) is determined by its dimension and the collection of algebraic data { A i, t i, i = 1, …, d } \{A_{i},t_{i},\,i=1,\dots,d\}. The bound for the number of zeros should be given in terms of these algebraic data.

###### Example 8.2.

The simplest class of Fuchsian systems is that having only two singularities (one simple pole of the matrix A ⁡ ( t) A(t) on the whole line ℂ ​ P 1 {\mathbb{C}}P^{1} is impossible since the sum of all the residues, including the one at infinity, must be zero). By a conformal transformation of the independent variable the two points can be placed at t = 0 t=0 and t = ∞ t=\infty. The corresponding system will then take the *Euler form*,

 | X ˙ = A t ⋅ X, A ∈ Mat μ × μ ⁡ ( ℂ). \dot{X}=\frac{A}{t}\cdot X,\qquad A\in\operatorname{Mat}_{\mu\times\mu}({\mathbb{C}}). |  | (8.6) |

The Euler system ( 8.6) can be immediately integrated: X ⁡ ( t) = t A X(t)=t^{A}. The associated Picard–Vessiot extension has the form that is already familiar:

 | ℂ ⁡ ( X) = ℂ ⁡ ( { t λ ​ ln k − 1 ​ t } λ, k), λ ∈ Spec ⁡ A, k ⩽ m ⁡ ( λ), {\mathbb{C}}(X)={\mathbb{C}}(\{t^{\lambda}\ln^{k-1}t\}_{\lambda,k}),\qquad\lambda\in\operatorname{Spec}A,\quad k\leqslant m(\lambda), |  | (8.7) |

where m ⁡ ( λ) ⩾ 1 m(\lambda)\geqslant 1 is the maximal size of Jordan cells corresponding to the eigenvalue λ \lambda.

Roots of *real*functions from the field ℂ ⁡ ( X) {\mathbb{C}}(X) cannot accumulate to the origin, if all eigenvalues of A A are real (Example 1.2). We will see that the “Euler field” for a system with only real spectrum is indeed quasialgebraic.

On the other hand, the field ℂ ⁡ ( t − 1, t − − 1) {\mathbb{C}}(t^{\sqrt{-1}},t^{-\sqrt{-1}}) associated with the 2 × 2 2\times 2 -Euler system with non-real spectrum { ± − 1 } \{\pm\sqrt{-1}\}, contains the function cos ⁡ ln ⁡ t \cos\ln t that obviously has infinite number of roots accumulating to t = 0 t=0.

This suggests that quasialgebraicity of the fields ℂ ⁡ ( X) {\mathbb{C}}(X) should be somehow related to spectral properties of the residue matrices. ∎

#### 8.6. Counting zeros of multivalued functions globally

Since functions from the Picard–Vessiot extensions are in general multivalued, counting their zeros “on the whole Riemann sphere” should be supplied with a precise meaning.

###### Example 8.3.

The function f ⁡ ( t) = t λ − 1 f(t)=t^{\lambda}-1 for a real irrational λ \lambda has infinitely many different roots t k = q k t_{k}=q^{k}, q = exp ⁡ 2 ​ π ​ i λ q=\exp\frac{2\pi i}{\lambda}, k ∈ ℤ k\in\mathbb{Z}, lying on different branches of this function.

In order to single out a branch, it is required to choose a simply connected domain U ⊂ ℂ ∖ Σ U\subset{\mathbb{C}}\smallsetminus\varSigma. Usually this choice is done by slitting the complex plane along segments or rays with endpoints in the singular locus Σ \varSigma. In the above example, slitting ℂ {\mathbb{C}} along the negative semiaxis yields a simply connected domain U U with the following property: *any branch of the function t λ − 1 t^{\lambda}-1 in this domain has at most ⌊ λ − 1 ⌋ \lfloor\lambda^{-1}\rfloor roots in it*(the same bound holds also for − U -U). Here and below ⌊ a ⌋ \lfloor a\rfloor stands for the integer part of a real number a a. This explicit bound is global in the sense that U U and − U -U together cover ℂ ∖ Σ {\mathbb{C}}\smallsetminus\varSigma. ∎

However, the choice of the simply connected domain U U can affect even finiteness of bounds on the number of zeros.

###### Example 8.4.

If λ \lambda is a non-real number, then the roots fall on the logarithmic spiral (since | q | ≠ 1 |q|\neq 1 in this case). If U U is chosen by slitting ℂ {\mathbb{C}} along positive or negative semiaxis, then the number of isolated roots on any branch will still be bounded by ⌊ ( Re ⁡ λ) − 1 ⌋ < + ∞ \lfloor(\operatorname{Re}\lambda)^{-1}\rfloor<+\infty for λ ∉ i ​ ℝ \lambda\notin i{\mathbb{R}}.

On the other hand, one can choose a simply connected spiral domain containing the origin on the boundary, so that it would simultaneously contain an infinite number of the points t k = q k t_{k}=q^{k}.

Though the spiral slits are not algebraic (even not analytic) curves, this example can be easily modified to construct *polygonal*simply connected domains containing as many roots of the function t λ − 1 t^{\lambda}-1 as necessary, provided that the number of sides of the polygon can be arbitrary. ∎

These examples motivate the following definition.

###### Definition 6.

An analytic multivalued function f: ℂ ​ P 1 → ℂ f\colon{\mathbb{C}}P^{1}\to{\mathbb{C}} ramified over a finite set Σ ⊂ ℂ ​ P 1 \varSigma\subset{\mathbb{C}}P^{1} is said to admit a *global bound on the number of isolated zeros*, if there exists a natural number N < + ∞ N<+\infty such that the number of isolated zeros of any branch of f f in any *open rectilinear triangle*T ⊂ ℂ ∖ Σ T\subset{\mathbb{C}}\smallsetminus\varSigma has no more than N N isolated zeros, the bound being uniform over all such triangles.

###### Remark.

Having this property, one can place an explicit upper bound on the number of isolated roots of f f in any simply connected domain U U bounded by finitely many algebraic curves of known degrees. The number of curves, their degrees and the number of ramification points will explicitly enter the answer together with the number N N.

Indeed, the domain ℂ ∖ Σ {\mathbb{C}}\smallsetminus\varSigma can be triangulated into finitely many triangles as above. The number of simply connected components of any intersection U ∩ T U\cap T with each triangle of the triangulation can be easily majorized by the Bézout theorem, in terms of the above data. The total number of such components should be multiplied by N N to construct the required upper bound.

###### Example 8.5.

The function t λ − 1 t^{\lambda}-1 admits a global upper bound for the number of isolated roots for all λ \lambda with Re ⁡ λ ≠ 0 \operatorname{Re}\lambda\neq 0. For λ = − 1 \lambda=\sqrt{-1} any real interval ( 0, a) (0,a), a > 0 a>0, contains infinitely many roots of this function. ∎

###### Remark.

In practice, however, we will always choose a convenient system of rectilinear slits as in the textbooks on complex variables: if, for example, an upper bound for the number of zeros is known in both U = ℂ ∖ ℝ + U={\mathbb{C}}\smallsetminus{\mathbb{R}}_{+} and − U = ℂ ∖ ℝ − -U={\mathbb{C}}\smallsetminus{\mathbb{R}}_{-}, then the number of zeros in any triangle not containing the origin, does not exceed the maximum of these two bounds, since such triangle cannot intersect both the positive and negative semiaxes simultaneously.

### 9. Digression on computability

#### 9.1. Hierarchy of computability

The discussion in the previous section addressed the issue of *globality*of bounds on the number of zeros of multivalued functions. Now we pass to a brief discussion of *computability*of these bounds. This would lead us again to functions defined by differential equations with algebraic right hand side parts.

The bounds for functions of the field ℂ ⁡ ( f 1, …, f μ) {\mathbb{C}}(f_{1},\dots,f_{\mu}), besides being dependent on the degree d d of these functions, should obviously depend on the field itself, that is, ultimately, on the choice of the generators f i f_{i}. While computability of functions of natural arguments is a well developed area (several notions of computability can be distinguished, see below), dependence on functional parameters is definitely outside the scope of any theory (e.g., the number of roots of a function is not a computable characteristic *per se*).

An intermediate position occupy “computable” functions of one or several real or complex variables. Here we take the most restrictive attitude, legalizing only *polynomial functions*, the absolute value | ⋅ | |\,\cdot\,| of a real or complex variable, and the integer part ⌊ ⋅ ⌋ \lfloor\cdot\rfloor of a real variable.

Returning to functions of one or several natural arguments, one can classify them in an “increasing order of computability” into:

1. (1)

(general) recursive functions, whose values can be computed for any combination of arguments in a finite time by some deterministic algorithm, Turing machine etc.;

2. (2)

primitive recursive functions, that can be defined by one or several iterated inductive rules of the form

 | ϕ ⁡ ( k + 1, m) = Φ ⁡ ( k, m, ϕ ⁡ ( k, m)), k ∈ ℕ, m ∈ ℕ n, \phi(k+1,m)=\varPhi(k,m,\phi(k,m)),\qquad k\in\mathbb{N},\ m\in\mathbb{N}^{n}, |  | (9.1) |

assuming that the functions Φ \varPhi and ϕ 1 = ϕ ⁡ ( 1, ⋅) \phi_{1}=\phi(1,\cdot) are already known;

3. (3)

elementary functions, given by finite compositions of powers, exponents, algebraic operations *etc*.

###### Example 9.1 (tower functions).

Consider the function τ ⁡ ( k, n) \tau(k,n) of two integer arguments, defined by the recursive rule

 | τ ⁡ ( 0, k) = k, τ ⁡ ( n + 1, k) = 2 τ ⁡ ( n, k). \tau(0,k)=k,\qquad\tau(n+1,k)=2^{\tau(n,k)}. |  | (9.2) |

These rules define *tower functions*(iterated exponents): τ ⁡ ( n, ⋅) \tau(n,\cdot) is a tower of height n n and for each particular n n is an elementary function of the second argument k k:

 | τ ( 1, k) = 2 k, τ ( 2, k) = 2 2 k, τ ( 3, k) = 2 2 2 k, … \tau(1,k)=2^{k},\quad\tau(2,k)=2^{2^{k}},\quad\tau(3,k)=2^{2^{2^{k}}},\quad\dots |  |

However, as a function of the first argument, it is not elementary. ∎

###### Example 9.2 (Ackermann generalized exponential).

Consider the function A ⁡ ( z, x, y) A(z,x,y) of three natural arguments, defined by the recursive rules and initial conditions as follows,

 | A ⁡ ( z + 1, x, y + 1) = A ⁡ ( z, x, A ⁡ ( z + 1, x, y)), A ( 0, x, y) = y + 1, A ( 1, x, 0) = x, A ( 2, x, 0) = 0, A ( z, x, 0) = 0, ∀ z ⩾ 2. \begin{gathered}A(z+1,x,y+1)=A(z,x,A(z+1,x,y)),\\ A(0,x,y)=y+1,\ A(1,x,0)=x,\ A(2,x,0)=0,\\ A(z,x,0)=0,\qquad\forall z\geqslant 2.\end{gathered} |  | (9.3) |

These rules define each function ϕ = A ⁡ ( z + 1, ⋅, ⋅) \phi=A(z+1,\cdot,\cdot\,) for any particular z z unambiguously provided that the function Φ = A ⁡ ( z, ⋅, ⋅) \varPhi=A({z},\cdot,\cdot\,) is already defined, by the *simple*recursive rule ϕ ⁡ ( x, y + 1) = Φ ⁡ ( x, ϕ ⁡ ( x, y)) \phi(x,y+1)=\varPhi(x,\phi(x,y)). In other words, the set of conditions defines A A for all nonnegative combinations of arguments.

One can easily check that

 | A ⁡ ( 1, x, y) = x + 1 + ⋯ + 1 = x + y, A ⁡ ( 2, x, y) = x + x + ⋯ + x = x ​ y, A ⁡ ( 3, x, y) = x x ⋯ x = x y, A ⁡ ( 4, x, y) = x x ⋅ ⋅ ⋅ x ⏟ y ​ times etc. \begin{aligned} A(1,x,y)&=x+1+\cdots+1=x+y,\\ A(2,x,y)&=x+x+\cdots+x=xy,\\ A(3,x,y)&=xx\cdots x=x^{y},\end{aligned}\qquad\begin{gathered}A(4,x,y)=\underset{y\text{ times}}{\underbrace{x^{x^{{\mathinner{\mkern 1.0mu\raise-1.0pt\hbox{$\cdot$}\mkern 2.0mu\raise 2.0pt\hbox{$\cdot$}\mkern 2.0mu\raise 5.0pt\vbox to7.0pt{\vss\kern 7.0pt\hbox{$\cdot$}}\mkern 1.0mu}}^{x}}}}}\\ \text{etc.}\end{gathered} |  |

This suggests that as a function of the first argument, A A is not primitive recursive. The reason is that, unlike in the simple recursive rule ( 9.1), the function A A is applied to itself (this does not prove that A A is not primitive recursive, but the fact remains true and can be rigorously demonstrated). It can be also shown that as a function of the first argument, the Ackermann generalized exponential grows faster than any primitive recursive function. ∎

#### 9.2. Transcendental functions defined by algebraic data

The above brief discussion suggests that in order to speak about computable bounds depending on several analytic functions as parameters, these analytic functions must themselves be defined in terms of finitely many integer, real or complex parameters.

The simplest example of such functions are polynomials (their coefficients play the role of the parameters) and, slightly more generally, algebraic functions. However, this example does not allow to produce nontrivial quasialgebraic fields.

Differentiation of algebraic functions leaves them algebraic. On the contrary, integration (taking primitives) in general results in transcendental functions. Another possibility of constructing transcendental functions from algebraic ones is exponentiation. However, both primitives and exponentials are only particular cases of *functions defined by ordinary differential equations with algebraic coefficients*(e.g., x ( t) = exp ∫ f ( t) d t x(t)=\exp\int f(t)\,dt is a solution to the differential equation x ˙ = f ⁡ ( t) ​ x \dot{x}=f(t)x). This looks as a most general mechanism transforming algebraic input data into transcendental output functions.

Thus we arrive to the following natural conclusion: in order to speak about quasialgebraicity of the function fields ℂ ⁡ ( f 1, …, f μ) {\mathbb{C}}(f_{1},\dots,f_{\mu}), the generating functions f i ​ ( t) f_{i}(t) must be defined by polynomial ordinary differential equations or systems of such equations. Then by computability of any bound we would always assume that this bound can be expressed in terms of the (real or complex) coefficients of these equations and/or integer parameters (dimensions, degrees, etc), so that as functions of real or complex parameters these bounds are polynomial, while being elementary (or at worst primitive recursive) functions of the remaining integer variables.

###### Example 9.3 (principal).

Suppose that the functions f i ​ ( t) f_{i}(t), i = 1, …, μ i=1,\dots,\mu, together satisfy a system of polynomial ordinary differential equations of the form

 | x ˙ i = ∑ | α | ⩽ m c i ​ α x α, i = 1, …, μ, α = ( α 1, …, α μ) ∈ ℤ + μ, \dot{x}_{i}=\sum_{|\alpha|\leqslant m}c_{i\alpha}x^{\alpha},\qquad i=1,\dots,\mu,\quad\alpha=(\alpha_{1},\dots,\alpha_{\mu})\in\mathbb{Z}_{+}^{\mu}, |  |

with complex coefficients c i ​ α ∈ ℂ c_{i\alpha}\in{\mathbb{C}}. Then the expressions

 | C 1 = ( max i, α ⁡ | c i ​ α |) N ⁡ ( μ, m), C 2 = N ⁡ ( μ, m) ⋅ ∑ i, α | c i ​ α | C_{1}=(\max_{i,\alpha}|c_{i\alpha}|)^{N(\mu,m)},\qquad C_{2}=N(\mu,m)\cdot\sum_{i,\alpha}|c_{i\alpha}| |  |

are both computable characteristics of the collection { f 1, …, f μ } \{f_{1},\dots,f_{\mu}\} provided that N N is an elementary or at worst primitive recursive function of two integer arguments m m (the degree) and μ \mu (the dimension of the system). ∎

#### 9.3. Restricted computable bounds

Explicit computability does not imply (neither does it assume) globality of the bounds. In the same way as the parameters defining the functions f i f_{i} may enter the answer, sometimes numeric characteristics of the domain (in our settings, always a triangle T ⊂ ℂ ∖ Σ T\subset{\mathbb{C}}\smallsetminus\varSigma) may enter into the expressions.

###### Definition 7.

Let U ⊂ ℂ U\subset{\mathbb{C}} be a domain (usually polygonal) eventually containing some of the singular points inside. We say that the field ℂ ⁡ ( X) {\mathbb{C}}(X) is *quasialgebraic in U U*, if the number of zeros of any function from this field can be bounded in any triangle T ⊂ U ∖ Σ T\subset U\smallsetminus\varSigma, uniformly on all such triangles, but the bound may depend on U U.

The most commonly occurring form of this dependence is through the distance between ∂ U \partial U and the singular locus Σ \varSigma.

###### Remark.

Since the independent variable ranges over the Riemann sphere ℂ ​ P 1 {\mathbb{C}}P^{1} and the point t = ∞ t=\infty may well belong to the singular locus, the distance from ∂ U \partial U to Σ \varSigma should be defined in such cases as minimum of the above distance to the finite part of Σ \varSigma and the number inf t ∈ ∂ U | t − 1 | \inf_{t\in\partial U}|t^{-1}| measuring the “distance from ∂ U \partial U to infinity”.

### 10. Quasialgebraicity and uniform quasialgebraicity

#### 10.1. Quasialgebraicity of Picard–Vessiot extensions: accurate formulation of the problem

Let X ⁡ ( t) X(t) be a fundamental matrix solution of a Fuchsian system of n n linear ordinary differential equations ( 8.5), and ℂ ⁡ ( X) {\mathbb{C}}(X) (resp., ℂ ⁡ [X] {\mathbb{C}}[X]) the field obtained by adjoining all entries of this matrix to the field ℂ {\mathbb{C}} (resp., the ring of all polynomial combinations of these entries). As was already noted, we always assume that ℂ ⁡ ( X) {\mathbb{C}}(X) contains the subfield of rational functions ℂ ⁡ ( t) {\mathbb{C}}(t).

###### Definition 8.

The field ℂ ⁡ ( X) {\mathbb{C}}(X) is called *quasialgebraic*, if the number of isolated roots of any function f ∈ ℂ ⁡ ( X) f\in{\mathbb{C}}(X) of degree k k in this field, in any triangle T T free from singular points t j t_{j} of the Fuchsian system ( 8.5), is bounded by a number depending only on:

1. (1)

the degree k = deg ℂ ⁡ ( X) ⁡ f k=\deg_{{\mathbb{C}}(X)}f;

2. (2)

the dimension n n and the number d d of (finite) singular points (as an elementary or at worst primitive recursive function);

3. (3)

the entries of the residue matrices A 1, …, A d A_{1},\dots,A_{d} (in an algebraic way);

4. (4)

on the coordinates of the singularities t 1, …, t d t_{1},\dots,t_{d} (also in an algebraic way).

In fact, in all cases when quasialgebraicity of the field will be established, the bounds would depend on the complex (matrix) parameters in a very simple way, via the *residual norm*of the rational matrix function A ⁡ ( t) A(t),

 | R ⁡ ( A ⁡ ( ⋅)) = max j = 1, …, d ⁡ ‖ A j ‖. R(A(\cdot))=\max_{j=1,\dots,d}\|A_{j}\|. |  | (10.1) |

In a similar manner, dependence of the bounds on the position of the singularities t j t_{j} will be expressed via the (inverse) *spread*of these points,

 | ρ ⁡ ( Σ) = max i ≠ j ⁡ { | t i − t j | − 1, | t i | }. \rho(\varSigma)=\max_{i\neq j}\{|t_{i}-t_{j}|^{-1},\ |t_{i}|\}. |  | (10.2) |

(this number is large only when some of the singular points approach each other).

#### 10.2. Uniform quasialgebraicity

According to the above definition, the field is quasialgebraic if the simple algebraic data (parameters) defining it can be used to produce an explicit bound on the number of zeros of any function from this field.

Some of these parameters are always relevant. There is no question why the dimension and the degree must necessarily enter any bound on zeros. It may require some efforts to see that other parameters can also affect the answer.

###### Example 10.1.

The Euler system

 | x ˙ 1 = a ​ t − 1 ​ x 1, x ˙ 2 = 0, a ∈ ℕ, \dot{x}_{1}=a\,t^{-1}x_{1},\quad\dot{x}_{2}=0,\qquad a\in\mathbb{N}, |  |

defines a field containing the function f ⁡ ( t) = t a − 1 f(t)=t^{a}-1 that is of degree *one*in this field (though, as a polynomial, it has degree a a). The number of isolated zeros of the function f f in a triangle can be as large as ⌊ a 2 ⌋ \lfloor\tfrac{a}{2}\rfloor. ∎

This example shows that the magnitude of eigenvalues of the residue matrices clearly affects the number of zeros.

It is not very difficult (see the subsequent sections) to construct upper bounds (global or not) that would involve *rational*expressions of the parameters (in this case, entries of the residue matrices) that have poles, making the bounds exploding for certain combinations of parameters. On the other hand, there are no visible reasons for appearance of the infinite number of zeros for these values of the parameters. It requires considerable efforts to show that in terms of the residue matrices, the bounds can be given by *polynomial*expressions, which is equivalent to expressing them in terms of the residual norm ( 10.1) as above. Finally, it is the most difficult part to prove that under certain additional but rather natural assumptions, the bounds can be given *uniformly over all configurations of singular points*.

#### 10.3. Notes, remarks

We conclude this highly informal discussion by several remarks, also of a very general nature.

As stated in § 4, the ultimate goal of the theory is to establish a constructive bound for the number of zeros of Abelian integrals (tangential Hilbert problem). These integrals were shown to belong to certain Picard–Vessiot extensions. Application of the methods explained in subsequent sections requires repeated algebraic manipulations with the integrals, therefore bringing into play the whole field of functions. Moreover, on the final stage of the construction not one but rather several Picard–Vessiot fields are considered simultaneously, while carrying out induction in the number of ramification points. This explains why the existence of upper bounds on the number of zeros (quasialgebraicity) is defined as a property of the corresponding functional fields (rather than elements constituting these fields).

There was also a special reason for choosing the definition of quasialgebraicity without attempting to specify explicitly the “counting function” measuring the number of isolated zeros. This was done primarily because the bounds that one can obtain on this way are *enormously*excessive. Several nested inductive constructions immediately produce tower-like bounds even from the modest exponential contributions on each inductive step.

Finally, we would like to note that the Fuchsian representation is not the only possible. Actually, the Picard–Fuchs system of differential equations for Abelian integrals is written in the hypergeometric form

 | ( t ​ E + A) ​ X ˙ ​ ( t) = B ​ X ​ ( t) (tE+A)\dot{X}(t)=BX(t) |  |

determined by two constant matrices A, B ∈ Mat n × n ⁡ ( ℂ) A,B\in\operatorname{Mat}_{n\times n}({\mathbb{C}}), and it would be natural to require that quasialgebraicity were expressed in terms of the norms ‖ A ‖ \|A\|, ‖ B ‖ \|B\| rather than in terms of the respective residues after transforming to the Fuchsian form. This type of bounds is not proved (if it were, this would imply constructive solution of the tangential Hilbert problem, as explained in § 7.3).

## Lecture IV Quantitative theory of differential equations

### 11. Bounded meandering principle: explicit bounds on zeros of functions defined by ordinary differential equations

The preceding section contained motivations for introducing the notion of quasialgebraicity. In this section we survey some results of constructive (though not always global) nature, bounding the number of isolated zeros of functions defined by differential equations.

#### 11.1. Linear n th n^{\text{th}} order equations with bounded analytic coefficients

The basis for all other considerations is a classical theorem by de la Vallée Poussin concerning solutions of linear ordinary differential equations with bounded coefficients, not necessarily polynomial or even analytic. It gives a sufficient condition for a linear ordinary differential equation of order n n with *real bounded coefficients*guaranteeing absence of solutions with more than n − 1 n-1 isolated roots on a given real interval I ⊂ ℝ I\subset{\mathbb{R}}. Such equations are called *disconjugate*on I I. In order to stress the difference with the complex case, we denote the independent variable by s s, and consider a linear equation

 | y ( n) + a 1 ​ ( s) ​ y ( n − 1) + ⋯ + a n − 2 ​ ( s) ​ y ′′ + a n − 1 ​ ( s) ​ y ′ + a n ​ ( s) ​ y = 0 y^{(n)}+a_{1}(s)\,y^{(n-1)}+\cdots+a_{n-2}(s)\,y^{\prime\prime}+a_{n-1}(s)y^{\prime}+a_{n}(s)y=0 |  | (11.1) |

on the real interval I = [s 0, s 1] I=[s_{0},s_{1}] of length r r with real bounded coefficients: | a k ​ ( s) | < c k < ∞ |a_{k}(s)|<c_{k}<\infty for all s ∈ I s\in I.

###### Lemma 8 ( [dlVP29])

If

 | ∑ k = 1 n c k ​ r k k! < 1, \sum_{k=1}^{n}\frac{c_{k}\,r^{k}}{k!}<1, |  | (11.2) |

then any C n C^{n} -smooth function f ⁡ ( s) f(s) satisfying a linear equation ( 11.1) may have at most n − 1 n-1 isolated roots on I I, counted with multiplicities.

This result can be seen as a generalization of the Sturm nonoscillation theorem for equations of order greater than 2 2. The inequality can be slightly improved, see [Lev69].

This (simple) statement implies a number of corollaries. First, subdividing any interval into sufficiently short segments satisfying ( 11.2), and adding together the bounds for each segment, one can obtain an explicit bound on zeros valid on any real interval where the coefficients a i ​ ( s) a_{i}(s) are explicitly bounded. Next, one can consider equations of the same form ( 11.1) with *complex-valued*coefficients and solutions. There is no sense to count zeros of such solutions (since in general there are no roots), instead an interesting question is to estimate their *topological index*, the variation of argument Arg ⁡ f ⁡ ( s) \operatorname{Arg}f(s) between the endpoints of the real interval. By a simple modification of the method used in the proof of Lemma 8 one can obtain an upper bound for this topological index, again in terms of the magnitude (uniform upper bounds for the absolute value) of coefficients of the equation ( 11.1), see [Yak99], as follows.

###### Lemma 9

Variation of argument of any solution f ⁡ ( t) f(t) of the equation ( 11.1) with complex-valued coefficients all bounded by C C in the absolute value, along the segment I I of length | I | = s 1 − s 0 |I|=s_{1}-s_{0} is no greater than

 | π ​ ( n + 1) ​ ( 1 + 3 ​ C ​ | I |). \pi(n+1)(1+3C|I|). |  |

If the equation has *analytic*coefficients a i ∈ 𝒪 ⁡ ( U) a_{i}\in\mathcal{O}(U) defined in some domain U ⊂ ℂ U\subset{\mathbb{C}}, then the number of complex isolated zeros inside any polygonal domain can be majorized using the above described bounds for the topological index and the classical argument principle. As a result, the following inequality for the number of isolated zeros can be obtained (we return to the initial notation t t for the complex independent variable).

###### Theorem 7 ( [Yak99])

Suppose f 1 ​ ( t), …, f n ​ ( t) f_{1}(t),\dots,f_{n}(t) solve

 | y ( n) + a 1 ( t) y ( n − 1) + ⋯ + a n − 1 ( t) y ′ + a n ( t) y = 0, t ∈ U, a i ∈ 𝒪 ( U), | a i ( t) | ⩽ R, i = 1, …, n. \begin{gathered}y^{(n)}+a_{1}(t)y^{(n-1)}+\cdots+a_{n-1}(t)y^{\prime}+a_{n}(t)y=0,\qquad t\in U,\\ a_{i}\in\mathcal{O}(U),\quad|a_{i}(t)|\leqslant R,\ i=1,\dots,n.\end{gathered} |  | (11.3) |

Then for any triangle T ⊂ U T\subset U of perimeter ℓ \ell any linear combination f = ∑ 1 n c i ​ f i f=\sum_{1}^{n}c_{i}f_{i} with complex constant coefficients c i c_{i}, has no more than

 | 3 2 ​ ( n + 1) ​ ( 1 + ℓ ​ R) \begin{gathered}\tfrac{3}{2}(n+1)(1+\ell R)\end{gathered} |  | (11.4) |

isolated zeros in T T.

###### Remark.

Analyticity of solutions of the equation ( 11.3) follows from analyticity of its coefficients. However, the theorem apparently can be modified to cover also equations with meromorphic coefficients, provided that the solutions are analytic in U U (the so called apparent singularities).

#### 11.2. Systems of linear equations: Novikov’s counterexample

Motivated by potential applications to Abelian integrals and quasialgebraic fields, we would like to find generalizations of Lemma 8 or Theorem 7 for systems of linear equations, in hope to majorize the number of isolated roots of any linear combination of coordinates c 1 ​ x 1 ​ ( s) + ⋯ + c n ​ x n ​ ( s) c_{1}x_{1}(s)+\cdots+c_{n}x_{n}(s) for a system

 | x ˙ ​ ( s) = A ⁡ ( s) ​ x ​ ( s), s ∈ I ⊂ ℝ, ∀ s ∈ I ‖ A ⁡ ( s) ‖ ⩽ R, \dot{x}(s)=A(s)x(s),\qquad s\in I\subset{\mathbb{R}},\qquad\forall s\in I\quad\|A(s)\|\leqslant R, |  |

in terms of ℓ = | I | \ell=|I| and R R. The following counterexample due to D. Novikov [Nov01b], shows that it is impossible, neither for real nor for complex systems.

###### Example 11.1.

Let t 1, …, t d t_{1},...,t_{d} be collection of different numbers (real or complex) from a real interval I I or a triangle T T (consider only the last case for simplicity). Denote a ⁡ ( t) = ε ⁡ ( t − t 1) ​ … ​ ( t − t d) a(t)=\varepsilon(t-t_{1})...(t-t_{d}) and let ε \varepsilon be so small that | a ⁡ ( t) | + | a ˙ ​ ( t) + a 2 ​ ( t) | < 1 |a(t)|+|\dot{a}(t)+a^{2}(t)|<1 for any t ∈ T t\in T.

Solution ϕ 1 = exp ⁡ ( ∫ a ⁡ ( t) ​ 𝑑 t) \phi_{1}=\exp(\int a(t)dt) of the linear differential equation of the first order x ˙ 1 = a ⁡ ( t) ​ x 1 \dot{x}_{1}=a(t)x_{1}, has no zeroes at all. However, the derivative ϕ 2 = ϕ ˙ 1 = a ⁡ ( t) ​ ϕ 1 \phi_{2}=\dot{\phi}_{1}=a(t)\phi_{1} has the same zeroes as a ⁡ ( t) a(t) and satisfies the equation ϕ ˙ 2 = ( a ˙ + a 2) ​ ϕ 1 \dot{\phi}_{2}=(\dot{a}+a^{2})\phi_{1}.

Together the pair ( ϕ 1, ϕ 2) (\phi_{1},\phi_{2}) satisfies the linear 2 × 2 2\times 2 -system

 | x ˙ 1 = a ​ x 1, x ˙ 2 = ( a ˙ + a 2) ​ x 1, a ⁡ ( t) = ε ​ ∏ 1 d ( t − t j), \dot{x}_{1}=ax_{1},\quad\dot{x}_{2}=(\dot{a}+a^{2})x_{1},\qquad a(t)=\varepsilon\prod_{1}^{d}(t-t_{j}), |  | (11.5) |

whose coefficients are bounded by 1 1 everywhere in T T by the choice of ε \varepsilon. However, the second component has the specified number d d of isolated zeroes there, where d d can be arbitrarily large. ∎

This example suggests that when dealing with systems of linear equations, instead of general analytic (variable) bounded coefficients, only rational or even polynomial coefficients were allowed, so that

 | A ⁡ ( t) = ∑ k = 0 d A k ​ t k, A k ∈ Mat n × n ⁡ ( ℂ), A(t)=\sum_{k=0}^{d}A_{k}t^{k},\qquad A_{k}\in\operatorname{Mat}_{n\times n}({\mathbb{C}}), |  | (11.6) |

and the magnitude of the matrix coefficients, e.g., the total norm R = ∑ k ‖ A k ‖ R=\sum_{k}\|A_{k}\| used to produce upper bounds.

#### 11.3. Reduction of a system to an equation: obstructions

The above example is not very surprising since the standard procedure of reducing a linear n × n n\times n -system

 | x ˙ = A ⁡ ( t) ​ x, x = ( x 1, …, x n) ∈ ℂ n \dot{x}=A(t)x,\qquad x=(x_{1},\dots,x_{n})\in{\mathbb{C}}^{n} |  | (11.7) |

to one n n th order linear equation is discontinuous with respect to parameters. Indeed, without loss of generality one can assume that it is the number of zeros of the first component y = x 1 y=x_{1} in a domain U ⊂ ℂ U\subset{\mathbb{C}} that interests us. Differentiating x 1 x_{1} by virtue of the system, we see that the derivatives are linear combinations:

 | y ( k) ( t) = 𝒒 k ( t) ⋅ x ( t), k = 1, …, n, …, y^{(k)}(t)={\boldsymbol{q}}_{k}(t)\cdot x(t),\qquad k=1,\dots,n,\dots, |  | (11.8) |

where the analytic (co)vector functions 𝒒 k ​ ( t) = ( q k, 1 ​ ( t), …, q k, n ​ ( t)) ∈ ℂ n ∗ {\boldsymbol{q}}_{k}(t)=(q_{k,1}(t),\dots,q_{k,n}(t))\in{{\mathbb{C}}^{n}}^{*} are determined by the recurrent rule

 | 𝒒 0 ​ ( t) = ( 1, 0, …, 0), 𝒒 k + 1 ​ ( t) = 𝒒 ˙ k ​ ( t) + 𝒒 k ​ ( t) ⋅ A ⁡ ( t) {\boldsymbol{q}}_{0}(t)=(1,0,\dots,0),\quad{\boldsymbol{q}}_{k+1}(t)=\dot{{\boldsymbol{q}}}_{k}(t)+{\boldsymbol{q}}_{k}(t)\cdot A(t) |  | (11.9) |

and do not depend on the choice of the trajectory x ⁡ ( t) x(t). (We use the right multiplication to stress that 𝒒 k ​ ( t) {\boldsymbol{q}}_{k}(t) are row vector functions). Consider the field 𝕜 = ℳ ⁡ ( U) \Bbbk=\mathcal{M}(U) of functions meromorphic in U U and the linear n n -space 𝕜 n \Bbbk^{n} over this field.

The functions 𝒒 k ​ ( ⋅) {\boldsymbol{q}}_{k}(\cdot) are vectors in this space. Consider the linear subspaces

 | { 0 } ⊂ L 0 ⊆ L 1 ⊆ ⋯ ⊆ L n − 1 ⊆ L n ⊆ ⋯ ⊆ 𝕜 n, \{0\}\subset L_{0}\subseteq L_{1}\subseteq\cdots\subseteq L_{n-1}\subseteq L_{n}\subseteq\cdots\subseteq\Bbbk^{n}, |  | (11.10) |

each L k L_{k} being spanned by 𝒒 0, 𝒒 1, …, 𝒒 k {\boldsymbol{q}}_{0},{\boldsymbol{q}}_{1},\dots,{\boldsymbol{q}}_{k} over 𝕜 \Bbbk. If all inclusions are strict, the dimensions of L k L_{k} over 𝕜 \Bbbk must strictly increase, while being bounded by n = dim 𝕜 𝕜 n n=\dim_{\Bbbk}\Bbbk^{n}. Hence the ascending chain of subspaces ( 11.10) must stabilize no later than after n n steps, i.e., for some μ ⩽ n \mu\leqslant n the inclusion must be non-strict, 𝒒 μ ∈ L μ − 1 {\boldsymbol{q}}_{\mu}\in L_{\mu-1}, which implies a linear identity over 𝕜 = ℳ ⁡ ( U) \Bbbk=\mathcal{M}(U),

 | 𝒒 μ + a 1 ​ ( t) ​ 𝒒 μ − 1 + ⋯ + a μ − 1 ​ ( t) ​ 𝒒 1 + a μ ​ ( t) ​ 𝒒 0 = 0, a i ∈ 𝕜 = ℳ ⁡ ( U). {\boldsymbol{q}}_{\mu}+a_{1}(t){\boldsymbol{q}}_{\mu-1}+\cdots+a_{\mu-1}(t){\boldsymbol{q}}_{1}+a_{\mu}(t){\boldsymbol{q}}_{0}=0,\quad a_{i}\in\Bbbk=\mathcal{M}(U). |  | (11.11) |

This implies that y = 𝒒 0 ⋅ x y={\boldsymbol{q}}_{0}\cdot x satisfies the equation ( 11.3).

Though the recurrent formulas generating the vectors 𝒒 1, 𝒒 2, … {\boldsymbol{q}}_{1},{\boldsymbol{q}}_{2},\dots are explicit, it is impossible to control the magnitude of the coefficients a i ​ ( ⋅) a_{i}(\cdot), whatever that may mean, from this construction. This can be seen in a simpler settings when the field 𝕜 \Bbbk is replaced by ℂ {\mathbb{C}}.

###### Example 11.2.

Consider a sequence of vectors q 0, q 1, … q_{0},q_{1},\dots, in the n n -dimensional space over ℝ {\mathbb{R}} or ℂ {\mathbb{C}}, that grows at most exponentially in the sense of the norm: ‖ q k ‖ ⩽ c k \|q_{k}\|\leqslant c^{k}, c > 0 c>0.

For the same dimensionality reasons as above, no later that at the n n th step a linear dependence must occur, allowing to express some q k q_{k} as a linear combination of the preceding vectors q 0, …, q k − 1 q_{0},\dots,q_{k-1},

 | − q k + a 1 ​ q k − 1 + ⋯ + a k ​ q 0 = 0, a i ∈ ℂ, -q_{k}+a_{1}q_{k-1}+\cdots+a_{k}q_{0}=0,\qquad a_{i}\in{\mathbb{C}}, |  | (11.12) |

similarly to ( 11.11). However, coefficients of this dependence are out of control and can be arbitrarily large. To see this, consider the situation when the angle between q k − 1 q_{k-1} and L k − 2 L_{k-2} is very small but nonzero so that L k − 2 ⊊ L k − 1 L_{k-2}\subsetneq L_{k-1}, while q k q_{k} belongs to L k − 1 L_{k-1} and is orthogonal to L k − 2 L_{k-2} in L k − 1 L_{k-1}. Even assuming some *lower*bounds on ‖ q k ‖ \|q_{k}\| will not help to improve the situation in this case. ∎

The situation becomes completely different under any of the following two additional assumptions.

###### Example 11.3.

Assume that all the vectors q k q_{k} actually belong to a lattice ℤ n ⊂ ℂ n \mathbb{Z}^{n}\subset{\mathbb{C}}^{n} and their norms are bounded from above as in the preceding example. Then the coefficients of the linear combination ( 11.11) can be explicitly bounded from above: indeed, if q k q_{k} is a linear combination of q 0, …, q k − 1 q_{0},\dots,q_{k-1}, then the coefficients a i a_{i} in ( 11.12) can be found by solving a system of linear nonhomogeneous algebraic equations with integer matrix of coefficients and integer free terms. By the Cramer rule, solutions of this system can be obtained (after elimination of redundant equations and assuming that solutions indeed exist) as ratios of appropriate minors (determinants of some square submatrices). These minors are integer numbers, explicitly bounded from above by virtue of the assumptions on the norms ‖ q i ‖ \|q_{i}\|. Hence in each ratio the numerator is bounded from above, whereas the denominator is no smaller than 1 1 in the absolute value. This clearly implies an upper bound on all the coefficients a i a_{i}. ∎

###### Example 11.4.

Assume that the vectors q k ∈ ℂ n q_{k}\in{\mathbb{C}}^{n} are obtained by iterations of a linear map P: ℂ n → ℂ n P\colon{\mathbb{C}}^{n}\to{\mathbb{C}}^{n}. Then the bounds on the norms will be automatically satisfied with c = ‖ P ‖ c=\|P\|. The *first*linear combination between the vectors still can have very large coefficients, exactly as in Example 11.2. However, instead of looking for the first combination, we may continue until the step number n n. Since any operator P P is a matrix root of its characteristic polynomial χ ⁡ ( z) = z n + a 1 ​ z n − 1 + ⋯ + a n − 1 ​ z + a n \chi(z)=z^{n}+a_{1}z^{n-1}+\cdots+a_{n-1}z+a_{n}, the linear combination of the form ( 11.12) in this case can be obtained via the identity χ ⁡ ( P) ​ q 0 = 0 \chi(P)q_{0}=0. Coefficients a i a_{i} of the characteristic polynomial admit an upper bound in terms of the eigenvalues of P P, each of which is no greater than the norm ‖ P ‖ \|P\|. Finally, we conclude that a linear combination ( 11.11) in this case (iterations of a linear map P P in the finite-dimensional space ℂ n {\mathbb{C}}^{n})) can be constructed with coefficients a i a_{i} explicitly bounded in terms of ‖ P ‖ \|P\| and n n. ∎

#### 11.4. Reduction of a system to an equation: commutative algebra versus linear algebra

The operator 𝒒 ⁡ ( t) ↦ 𝒒 ˙ ​ ( t) + 𝒒 ⁡ ( t) ⋅ A ⁡ ( t) {\boldsymbol{q}}(t)\mapsto\dot{{\boldsymbol{q}}}(t)+{\boldsymbol{q}}(t)\cdot A(t) from the n n -dimensional ℂ ⁡ ( t) {\mathbb{C}}(t) -linear space into itself, describing the iterations ( 11.9), is *not*linear over the field ℂ ⁡ ( t) {\mathbb{C}}(t), since the derivative d / d ​ t d/dt is not ℂ ⁡ ( t) {\mathbb{C}}(t) -linear operator. On the other hand, considered over the field ℂ {\mathbb{C}}, the space of polynomial vector-functions is *not*finite-dimensional unless deg ⁡ A ⁡ ( t) = 0 \deg A(t)=0 (in which case the degrees are uniformly bounded). Thus neither of the above methods can work.

However, a solution can be found in terms of the commutative algebra. It allows to treat in a similar way both linear and nonlinear systems. Before proceeding further, we give a useful technical definition.

###### Definition 9.

The *norm*of a polynomial p ∈ ℂ ⁡ [x 1, …, x n] p\in{\mathbb{C}}[x_{1},\dots,x_{n}] is the sum of absolute values of its coefficients:

 | ‖ ∑ α c α ​ x α ‖ = ∑ α | c α |. \left\|\sum\nolimits_{\alpha}c_{\alpha}x^{\alpha}\right\|=\sum\nolimits_{\alpha}|c_{\alpha}|. |  | (11.13) |

One can easily verify that in addition to the usual triangle inequality, this norm is multiplicative, ‖ p ​ q ‖ ⩽ ‖ p ‖ ​ ‖ q ‖ \|pq\|\leqslant\|p\|\,\|q\| for any two polynomials. The norm of a derivative ‖ ∂ i p ‖ \|\partial_{i}p\| (in any variable) can be easily bounded, ‖ ∂ i p ‖ ⩽ deg ⁡ p ​ ‖ p ‖ \|\partial_{i}p\|\leqslant\deg p\,\|p\|.

Generalization of the construction from § 11.3 is very simple.

###### Example 11.5 (basic).

Consider the linear system ( 11.7) with a *polynomial*matrix of coefficients A ⁡ ( t) A(t) as in ( 11.6). The rule ( 11.9) defines a sequence of *polynomials*q k ​ ( t, x) = 𝒒 k ​ ( t) ⋅ x ∈ ℂ ⁡ [t, x] q_{k}(t,x)={\boldsymbol{q}}_{k}(t)\cdot x\in{\mathbb{C}}[t,x], that are always linear in the variables x = ( x 1, …, x n) x=(x_{1},\dots,x_{n}): the recursive rules allow to estimate the degrees deg t ⁡ q k ​ ( t, x) \deg_{t}q_{k}(t,x) and, if necessary, their norms.

Instead of the linear subspaces L k L_{k} over the field 𝕜 = ℂ ⁡ ( t) \Bbbk={\mathbb{C}}(t) in this case, consider the *polynomial ideals*I k = ( q 0, …, q k) ⊂ ℂ ⁡ [t, x] I_{k}=(q_{0},\dots,q_{k})\subset{\mathbb{C}}[t,x]. The ascending chain

 | { 0 } ⊂ I 0 ⊆ I 1 ⊆ ⋯ ⊆ I n ⊆ ⋯ ⊆ ℂ ⁡ [t, x] \{0\}\subset I_{0}\subseteq I_{1}\subseteq\cdots\subseteq I_{n}\subseteq\cdots\subseteq{\mathbb{C}}[t,x] |  | (11.14) |

of these ideals must eventually stabilize in the sense that some inclusion I ℓ − 1 ⊂ I ℓ I_{\ell-1}\subset I_{\ell} becomes non-strict (an equality). This follows from the fundamental fact that the polynomial ring ℂ ⁡ [t, x] {\mathbb{C}}[t,x] is Noetherian and *any*ascending polynomial chain in it eventually stabilizes.

The above stabilization condition means that ± q ℓ ∈ I ℓ − 1 \pm q_{\ell}\in I_{\ell-1}, hence for appropriate polynomial coefficients h 1, …, h ℓ ∈ ℂ ⁡ [t, x] h_{1},\dots,h_{\ell}\in{\mathbb{C}}[t,x]

 | q ℓ + ∑ i = 1 ℓ h i ​ q ℓ − i = 0. q_{\ell}+\sum_{i=1}^{\ell}h_{i}q_{\ell-i}=0. |  | (11.15) |

*A priori*, the polynomial coefficients h i h_{i} can depend on x x in a nontrivial way. However, since all polynomials q k q_{k} are linear in x x (homogeneous), one can truncate the identity ( 11.15) retaining only constant terms of h i h_{i} (of degree 0 0 in x x) and construct a new identity of exactly the same form ( 11.15) but with coefficients a i ​ ( t) = h i ​ ( t, 0) a_{i}(t)=h_{i}(t,0) from the *univariate*polynomial ring ℂ ⁡ [t] {\mathbb{C}}[t],

 | q ℓ + ∑ i = 1 ℓ a i q ℓ − i = 0, a i ∈ ℂ [t], i = 1, …, ℓ. q_{\ell}+\sum_{i=1}^{\ell}a_{i}q_{\ell-i}=0,\qquad a_{i}\in{\mathbb{C}}[t],\ i=1,\dots,\ell. |  | (11.16) |

The identity ( 11.16) obviously means that the function q 0 ​ ( t, x) = x 1 q_{0}(t,x)=x_{1} satisfies the linear ordinary differential equation

 | y ( ℓ) + ∑ i = 1 ℓ a i ( t) y ( ℓ − i) = 0, a i ( t) = h i ( t, 0) ∈ ℂ [t], i = 1, …, ℓ. y^{(\ell)}+\sum_{i=1}^{\ell}a_{i}(t)\,y^{(\ell-i)}=0,\qquad a_{i}(t)=h_{i}(t,0)\in{\mathbb{C}}[t],\ i=1,\dots,\ell. |  | (11.17) |

In order to apply the results form § 11.1, one has to estimate the absolute values | a i ​ ( t) | |a_{i}(t)| from above. In any disk of known radius { | t | < R } \{|t|<R\} this can be done if the decomposition ( 11.15) is explicitly known, in particular, if the following parameters are explicitly bounded from above:

- •

the length ℓ \ell of the chain (equal to the order of the resulting differential equation);

- •

the degrees of the coefficients h i h_{i} in t t;

- •

the norms ‖ h i ‖ \|h_{i}\|, i = 1, …, ℓ i=1,\dots,\ell.

∎

###### Example 11.6.

The construction involving chains of ideals, is not very degree-specific. Consider a system of *polynomial*ordinary differential equations,

 | x ˙ i = P i ( t, x), i = 1, …, n, P i ∈ ℂ [t, x 1, …, x n]. \dot{x}_{i}=P_{i}(t,x),\qquad i=1,\dots,n,\ P_{i}\in{\mathbb{C}}[t,x_{1},\dots,x_{n}]. |  | (11.18) |

Let f f be a polynomial combination f ⁡ ( t) = Q ⁡ ( t, x 1 ​ ( t), …, x n ​ ( t)) f(t)=Q(t,x_{1}(t),\dots,x_{n}(t)) for some Q = Q ⁡ ( t, x) ∈ ℂ ⁡ [t, x] Q=Q(t,x)\in{\mathbb{C}}[t,x]. Consider the infinite sequence of polynomials q 0 q_{0}, q 1 q_{1}, …, q n, ⋯ ∈ ℂ ⁡ [t, x] q_{n},\dots\in{\mathbb{C}}[t,x] formed by iterations of the Lie derivative, i.e., the recursive rule

 | q 0 = Q, q k + 1 = ∂ q k ∂ t + ∑ i = 1 n ∂ q k ∂ x i ⋅ P i. q_{0}=Q,\quad q_{k+1}=\frac{\partial q_{k}}{\partial t}+\sum_{i=1}^{n}\frac{\partial q_{k}}{\partial x_{i}}\cdot P_{i}. |  | (11.19) |

Let I k = ( q 0, q 1, …, q k) ⊂ ℂ ⁡ [t, x] I_{k}=(q_{0},q_{1},\dots,q_{k})\subset{\mathbb{C}}[t,x] be the polynomial ideals generated by the first k + 1 k+1 polynomials from this sequence in the polynomial ring ℂ ⁡ [t, x] {\mathbb{C}}[t,x]. They obviously form an ascending chain, I k ⊂ I k + 1 I_{k}\subset I_{k+1}. Since the ring ℂ ⁡ [t, x] {\mathbb{C}}[t,x] is Noetherian, this chain must stabilize and hence for some natural ℓ \ell,

 | q ℓ + h 1 ​ q ℓ − 1 + ⋯ + h ℓ − 1 ​ q 1 + h ℓ ​ q 0 = 0, h i ∈ ℂ ⁡ [t, x]. q_{\ell}+h_{1}q_{\ell-1}+\cdots+h_{\ell-1}q_{1}+h_{\ell}q_{0}=0,\qquad h_{i}\in{\mathbb{C}}[t,x]. |  | (11.20) |

As in the linear case, this identity implies a polynomial relationship between the unknown function y = Q ⁡ ( t, x ⁡ ( t)) y=Q(t,x(t)) and its derivatives up to order ℓ \ell. Unlike the linear case, this time the coefficients h i h_{i} may depend on x x explicitly, so that in addition to the data described in the previous example, one needs upper bounds for | x i ​ ( t) | |x_{i}(t)| in U U, which is a non-algebraic piece of information. However, in many cases this information can be easily achieved (or even *a priori*known) and the problem reduces to getting the same information as in the linear case, namely: the length ℓ \ell of the ascending chain of polynomial ideals, the degrees and the norms of the polynomials h i h_{i} appearing in the representation ( 11.20). ∎

#### 11.5. Generalizations and improvements

It is not clear from the very beginning, how replacing ascending chains of linear subspaces by ascending chains of polynomial ideals may resolve the problems related to unboundedness of the coefficients of the decompositions ( 11.11) and ( 11.20) respectively, see Exercise 11.2. We explain it now.

The first advantage of the suggested approach allows to treat systems depending polynomially on additional parameters, without the risk of producing bounds that blow up for certain values of the parameters. Actually, the difference between parameters and phase variables disappears almost completely.

###### Example 11.7.

Assume that the linear system ( 8.2) with a polynomial matrix A ⁡ ( t) A(t) ( 11.6) depends on additional parameters λ = ( λ 1, …, λ p) \lambda=(\lambda_{1},\dots,\lambda_{p}) is a polynomial way: A ∈ Mat n × n ⁡ ( ℂ ⁡ [t, λ]) A\in\operatorname{Mat}_{n\times n}({\mathbb{C}}[t,\lambda]). Then one can consider the chains of ideals in the bigger ring ℂ ⁡ [t, λ] {\mathbb{C}}[t,\lambda] and only minor notation changes are necessary to construct a linear ordinary differential equation ( 11.17) whose coefficients will be in fact polynomial in t t*and*λ \lambda (note that the resulting differential equation is always monic: its leading coefficient before the principal derivative is 1 1).

This polynomiality eliminates the danger that for some values of the parameters the coefficients of the derived equation ( 11.17) will blow up (which was earlier the case). ∎

Another advantage appears as a generalization of Example 11.3.

###### Example 11.8.

Assume that the coefficients matrix A ⁡ ( t) A(t) of the system ( 11.7) is polynomial as in ( 11.6), and in addition all matrix coefficients A k A_{k} have only integer entries: A k ∈ Mat n × n ⁡ ( ℤ) A_{k}\in\operatorname{Mat}_{n\times n}(\mathbb{Z}). Then, since the polynomial q 0 ​ ( t, x) = x 1 q_{0}(t,x)=x_{1} also belongs to the subring ℤ ⁡ [t, x] \mathbb{Z}[t,x], all subsequent polynomials q k q_{k} will also have integer coefficients, and their degrees are growing not faster than linearly in k k. The growth of the norms ‖ q k ‖ \|q_{k}\| can also be easily controlled.

Suppose that the length ℓ \ell of the ascending chain of the corresponding ideals ( 11.14) is already known (in the univariate case it is relatively simple, see [NY99b]). Then one can explicitly compute an upper bound r r for the degrees of polynomial coefficients h i h_{i} in ( 11.15) in terms of ℓ \ell, the degree d = deg ⁡ A ⁡ ( t) d=\deg A(t) and n = dim x n=\dim x. To find the polynomials h i h_{i} themselves (or rather the univariate polynomials a i = h i ​ ( ⋅, 0) a_{i}=h_{i}(\cdot,0)), it is possible now to use the method of indeterminate coefficients: writing each a i a_{i} as ∑ j = 0 r c i ​ j ​ t j \sum_{j=0}^{r}c_{ij}t^{j} and substituting them into the identity ( 11.16), we obtain a system of non-homogeneous linear algebraic equations for the unknown variables { c i ​ j: i = 1, …, ℓ, j = 0, …, r } \{c_{ij}\colon i=1,\dots,\ell,j=0,\dots,r\}, with integral coefficients matrix and the free terms column, all explicitly bounded from below. For the same reason as in Example 11.3, in this “lattice” case explicit bounds for ‖ a i ‖ \|a_{i}\| can be immediately produced in terms of n n, d d and r r. ∎

The lattice polynomial system may look artificial, but in fact their appearance is natural. The explanation is given in the following principal example.

###### Example 11.9 (universal system).

All entries of the matrix coefficients A k A_{k} of the polynomial matrix function ( 11.6) can be considered as parameters and denoted by λ i \lambda_{i}, i = 1, …, ( d + 1) ​ n 2 i=1,\dots,(d+1)n^{2}. With respect to these variables, the “universal matrix polynomial” ∑ k = 0 d A k ​ t k \sum_{k=0}^{d}A_{k}t^{k} is in fact in the “lattice” Mat n × n ⁡ ( ℤ ⁡ [t, λ]) \operatorname{Mat}_{n\times n}(\mathbb{Z}[t,\lambda]), of known degree d + 1 d+1: moreover, all coefficients of A ⁡ ( t) A(t) over the ring ℤ ⁡ [t, λ] \mathbb{Z}[t,\lambda] are zero-one matrices.

In a similar way one can start iterations from the “general linear form” q 0 ​ ( t, x) = ∑ i = 1 n β i ​ x i q_{0}(t,x)=\sum_{i=1}^{n}\beta_{i}x_{i} which becomes a polynomial of degree n + 1 n+1 with zero-one coefficients in ℂ ⁡ [x, β 1, …, β n] {\mathbb{C}}[x,\beta_{1},\dots,\beta_{n}] and add the string of the coefficients { β i } \{\beta_{i}\} to the parameter list. This would allow to treat simultaneously isolated zeros of all nontrivial linear combinations. ∎

#### 11.6. Lengths of ascending chains

Example 11.6 in fact proves that for any dimension n n and degree d d of the matrix polynomial A ⁡ ( t) A(t) from ( 11.6), one can majorize explicitly the number of isolated zeros of any linear combination ∑ β i ​ x i ​ ( t) \sum\beta_{i}x_{i}(t) in terms of n, d n,d, and R = ∑ 0 d ‖ A k ‖ R=\sum_{0}^{d}\|A_{k}\| provided that the length of ascending chain of polynomial ideals ( 11.14) is explicitly known. We claim that this length is a “computable” function.

Notice that for each combination of n, d n,d we have a uniquely defined parameter space { λ } = ℂ ( d + 1) ​ n 2 + n \{\lambda\}={\mathbb{C}}^{(d+1)n^{2}+n} (coefficients of the matrix polynomial A ⁡ ( t) A(t) and the initial linear form q 0 q_{0}), and the uniquely defined chain of ideals in the polynomial ring ℂ ⁡ [t, x, λ] {\mathbb{C}}[t,x,\lambda] generated by polynomials q k q_{k} that in fact belong to the lattice ℤ ⁡ [t, x, λ] \mathbb{Z}[t,x,\lambda].

The construction of the generators q k q_{k} is absolutely explicit. The problem of verifying whether the next polynomial q k q_{k} belongs to the ideal I k − 1 I_{k-1} generated by the previous polynomials, is constructive: there exists an algorithmic procedure allowing to get a positive or negative answer in a finite number of steps for each k k. Thus the length ℓ \ell is a “computable” (in the weakest sense) function of n n and d d: the above description can be transformed into an algorithm computing the value ℓ ⁡ ( n, d) \ell(n,d) for any given combination of n n and d d.

Coupled with the preceding discussion, this computability means that the problem on the number of zeros of functions defined by polynomial ODE’s, is algorithmically solvable. However, the complexity of this algorithm turns out to be very high in the sense that the bound on the growth rate of the function ℓ ⁡ ( n, d) \ell(n,d) is tremendous and higher than any elementary function. In the next section we address this question in details and show what other modifications are necessary in order to produce a “theoretically feasible” upper bound.

### 12. Lengths of chains

#### 12.1. Descending chains of algebraic varieties

The problem on ascending chains of polynomial ideals, belongs entirely to the realm of commutative algebra. However, there is a parallel geometric problem that admits a considerably more transparent solution. Moreover, the construction used in the “geometric” proof, can be adjusted (after introducing appropriate technical tools) to the algebraic case.

Consider a *strictly*decreasing chain of complex algebraic varieties,

 | ℂ n = X 0 ⊃ X 1 ⊃ X 2 ⊃ ⋯ ⊃ X k ⊃ ⋯ {\mathbb{C}}^{n}=X_{0}\supset X_{1}\supset X_{2}\supset\cdots\supset X_{k}\supset\cdots |  | (12.1) |

where each variety X k X_{k} is given by a finite number of polynomial equations in ℂ n {\mathbb{C}}^{n} of degree no greater than d k d_{k} (no restrictions are imposed on the number or the structure of these equations). Without loss of generality we may assume that the sequence d 1, d 2, … d_{1},d_{2},\dots is non-decreasing.

By the same Noetherian property, the chain ( 12.1) must terminate after finitely many steps at some variety X ℓ X_{\ell}. The problem is to compute the length ℓ \ell from the dimension n n and knowing the bounds for the degrees d k d_{k}.

If the degrees d k d_{k} are all bounded, then the problem belongs to linear algebra, since the polynomial equations defining the varieties X k X_{k} will in fact constitute a finite-dimensional linear space, and its dimension will be the natural bound for the length of the chain ( 12.1). In order to avoid technical troubles when talking about computable dependence on *infinite*input data { d 1, d 2, …, } \{d_{1},d_{2},\dots,\}, we will consider *finite-parameter*examples. The most important are the linear growth case, when

 | d k = d + k, k = 1, 2, … d_{k}=d+k,\qquad k=1,2,\dots |  | (12.2) |

or the exponential growth case

 | d k = d k, k = 1, 2, …. d_{k}=d^{k},\qquad k=1,2,\dots. |  | (12.3) |

In both cases the natural number d d is a parameter, and in both cases ℓ \ell should be majorized in terms of n n and d d.

#### 12.2. Lexicographically decreasing sequences of words

The advantage of the “geometric” problem on chains of complex algebraic varieties, is that it can be reduced to a purely combinatorial problem on lexicographically decreasing sequences of words.

Recall that any algebraic variety can be uniquely represented as the union of irreducible algebraic subvarieties of different dimensions varying from 0 0 (isolated points) to n − 1 n-1 (hypersurfaces). Thus with any X ⊂ ℂ n X\subset{\mathbb{C}}^{n} one can associate a vector ν ⁡ ( X) ∈ ℤ + n \nu(X)\in\mathbb{Z}_{+}^{n} with n n integer nonnegative coordinates ( ν n − 1, …, ν 1, ν 0) (\nu^{n-1},\dots,\nu^{1},\nu^{0}), where ν i = ν i ​ ( X) \nu^{i}=\nu^{i}(X) stands for the *number*of irreducible i i -dimensional components of X X.

Denote by ≺ \prec the lexicographic order on ℤ + n \mathbb{Z}_{+}^{n}, letting

 | ( ν n − 1, …, ν 0) ≺ ( ν ¯ n − 1, …, ν ¯ 0) (\nu^{n-1},\dots,\nu^{0})\prec(\bar{\nu}^{n-1},\dots,\bar{\nu}^{0}) |  |

if and only if for some k = 1, …, n k=1,\dots,n

 | ν n − 1 = ν ¯ n − 1, …, ν k = ν ¯ k, but ​ ν k − 1 < ν ¯ k − 1. \nu^{n-1}=\bar{\nu}^{n-1},\ \dots,\ \nu^{k}=\bar{\nu}^{k},\ \text{but}\ \nu^{k-1}<\bar{\nu}^{k-1}. |  |

The following elementary observation is crucial.

###### Lemma 10

If X ⊊ Y ⊂ ℂ n X\subsetneq Y\subset{\mathbb{C}}^{n}, then ν ⁡ ( X) ≺ ν ⁡ ( Y) \nu(X)\prec\nu(Y).

###### Proof.

This holds since:

1. (1)

any irreducible component of X X should belong to an irreducible component of Y Y, and

2. (2)

if A ⊂ B A\subset B is a pair of *irreducible*varieties, then dim A ⩽ dim B \dim A\leqslant\dim B and in the case of equal dimensions necessarily A = B A=B.

In other words, when passing from Y Y to X X each irreducible component either completely survives, or is split into a number of other components of lower dimensions. ∎

The fact that a descending chain of algebraic varieties must stabilize, follows now from the following purely combinatorial claim.

###### Proposition 5

A lexicographically strictly decreasing chain

 | ν 1 ≻ ν 2 ≻ ⋯ ≻ ν k ≻ ⋯, ν k ∈ ℤ + n, \nu_{1}\succ\nu_{2}\succ\cdots\succ\nu_{k}\succ\cdots,\qquad\nu_{k}\in\mathbb{Z}_{+}^{n}, |  | (12.4) |

must be finite.

###### Proof.

For n = 1 n=1 the claim is obvious, since any decreasing sequence of nonnegative integers must be finite. For an arbitrary n n, the first “letters” ν k n − 1 ∈ ℤ + \nu^{n-1}_{k}\in\mathbb{Z}_{+}, k = 1, 2, … k=1,2,\dots, form a non-increasing sequence (it must *not*necessarily be strictly decreasing). However, no more than a finite number of values is taken. Along any interval of constancy of the first letter, the tails ( ν k n − 2, …, ν k 0) (\nu^{n-2}_{k},\dots,\nu^{0}_{k}) also form a lexicographically strictly decreasing sequence in ℤ + n − 1 \mathbb{Z}^{n-1}_{+}. Hence the length of each such segment is finite by the induction assumption, and the length of the whole chain is finite as the sum of finitely many finite numbers. ∎

This proof, being extremely simple, can be supplied by quantitative estimates of the lengths under additional assumptions on the *norms*of the words. Denote ‖ ν ‖ = ν n − 1 + ⋯ + ν 0 \|\nu\|=\nu^{n-1}+\cdots+\nu^{0} the norm on ℤ + n \mathbb{Z}^{n}_{+}.

###### Example 12.1.

Assume that the norms of the words ν k \nu_{k} forming the chain ( 12.4) are bounded:

 | ∥ ν k ∥ ⩽ d + k, ∀ k = 1, 2, … ( d a natural parameter). \|\nu_{k}\|\leqslant d+k,\qquad\forall k=1,2,\dots\ \text{($d$ a natural parameter)}. |  | (12.5) |

Then the length of the chain as a function of n n and d d is bounded by a general recursive (but *not*primitive recursive) function. The explanation is as follows.

Let f ⁡ ( n, d, i) f(n,d,i) be the maximal length of the chain under the additional constraint that the first “letter” of the first word is no greater than i i, ν 1 n − 1 ⩽ i \nu_{1}^{n-1}\leqslant i. Then the restricted function f ⁡ ( n + 1, ⋅, i + 1) f(n+1,\cdot,i+1) can be expressed via f ⁡ ( n, ⋅, ⋅) f(n,\cdot,\cdot) and f ⁡ ( n + 1, ⋯, i) f(n+1,\cdots,i).

Indeed, the length of the *initial*segment of the chain, on which the first letter maintains its initial value i i, can be at most f ⁡ ( n, d, d) f(n,d,d), since the tails start with a word whose first letter can be at most d d. After the first segment is exhausted, the remaining part of the chain begins with a word of length n n, whose first letter is at most i − 1 i-1, and with the restriction on the norms of the words as follows,

 | ‖ ν k ‖ ⩽ d + ( k + f ⁡ ( n, d, d)), \|\nu_{k}\|\leqslant d+(k+f(n,d,d)), |  |

if the words of the remaining chain are numbered after the drop of the first letter. This is tantamount to replacing d d by f ⁡ ( n, d, d) f(n,d,d), therefore we obtain the recurrent inequality

 | f ⁡ ( n + 1, d, i) ⩽ f ⁡ ( n, d, d) + f ⁡ ( n + 1, d + f ⁡ ( n, d, d), i − 1). f(n+1,d,i)\leqslant f(n,d,d)+f(n+1,d+f(n,d,d),i-1). |  | (12.6) |

Coupled with the boundary conditions

 | f ⁡ ( n, d, 0) ⩽ f ⁡ ( n − 1, d, d), f ⁡ ( 1, d, i) ⩽ i, f(n,d,0)\leqslant f(n-1,d,d),\qquad f(1,d,i)\leqslant i, |  |

this determines the upper bound for f f completely. Notice the remarkable similarity between the recurrent rule ( 12.6) for f f and that for the Ackermann generalized exponential ( 9.3). ∎

The growth rate determined by the above recursive function, is enormous: in terms of n n, the dimension of the ambient space, the function f f grows faster than any primitive function. On the other hand, this bound is essentially sharp: for lexicographically ordered chains it is rather obvious, for chains of polynomial ideals it was proved by G. Moreno [MS92, MS91], for chains of algebraic varieties the claim is apparently also true though not written anywhere. In any case the bounds based on such estimate of the length of chains should not be considered as constructive, even theoretically.

However, under rather mild additional assumptions the bounds can be improved very considerably, in fact to become elementary functions of n, d n,d.

#### 12.3. Dynamically generated chains

The chain of ideals ( 11.14) is generated by a dynamical system. More precisely, the rule ( 11.19) for the general case of a polynomial vector field ( 11.18) is a Lie derivative of the ring ℂ ⁡ [t, x] {\mathbb{C}}[t,x], and the ideals I k I_{k} are generated by iterated Lie derivatives of the initial polynomial q 0 ∈ ℂ ⁡ [t, x] q_{0}\in{\mathbb{C}}[t,x].

A parallel construction for chains of algebraic varieties also involves a dynamical ingredient [NY97, NY99b]. Namely, instead of the general chains ( 12.1) with the only restriction on the degrees of the varieties X k X_{k}, one should consider chains generated by a discrete time dynamical system in ℂ n {\mathbb{C}}^{n}.

Let F: ℂ n → ℂ n F\colon{\mathbb{C}}^{n}\to{\mathbb{C}}^{n} be a polynomial map of some known degree d d and X ⊂ ℂ n X\subset{\mathbb{C}}^{n} an algebraic subvariety. Consider the decreasing chain { X k } \{X_{k}\} defined by the recursive rule

 | X 0 = X, X k + 1 = X ∩ F − 1 ( X k), k = 0, 1, 2, …. X_{0}=X,\qquad X_{k+1}=X\cap F^{-1}(X_{k}),\quad k=0,1,2,\dots. |  | (12.7) |

In other words,

 | X k = X ∩ F − 1 ​ ( X) ∩ F − 2 ​ ( X) ∩ ⋯ ∩ F − k ​ ( X), X_{k}=X\cap F^{-1}(X)\cap F^{-2}(X)\cap\cdots\cap F^{-k}(X), |  |

where F k F^{k} stands for the k k times iterated map F ∘ ⋯ ∘ F F\circ\cdots\circ F and F − k ​ ( ⋅) = ( F k) − 1 ​ ( ⋅) F^{-k}(\cdot)=(F^{k})^{-1}(\cdot) denotes the corresponding preimage.

Dynamically X k X_{k} can be described as the set of points a ∈ ℂ n a\in{\mathbb{C}}^{n} such that the point a a itself, together with its F F -orbit F ​ ( a), …, F k ​ ( a) F(a),\dots,F^{k}(a) of length k k, belong to X X. This immediately implies that

 | F ( X k ∖ X k + 1) ⊆ X k − 1 ∖ X k, k = 1, 2, … F(X_{k}\smallsetminus X_{k+1})\subseteq X_{k-1}\smallsetminus X_{k},\qquad k=1,2,\dots |  | (12.8) |

(the differences occurring above consist of initial conditions of orbits that jump off the variety X X*exactly*after the specified number of steps).

The condition ( 12.8) means that the difference X k ∖ X k + 1 X_{k}\smallsetminus X_{k+1} cannot be too large compared with the preceding difference X k − 1 ∖ X k X_{k-1}\smallsetminus X_{k}. For an arbitrary polynomial map this is not true, but under the additional assumption that F F preserves dimensions of semialgebraic sets (i.e., takes curves into curves and not into points, though eventually creating singularities, and the same in higher dimensions), one can conclude that the dimensions of the differences X k ∖ X k + 1 X_{k}\smallsetminus X_{k+1} are non-increasing:

 | dim ( X k ∖ X k + 1) ⩽ dim ( X k − 1 ∖ X k), k = 1, 2, …. \dim(X_{k}\smallsetminus X_{k+1})\leqslant\dim(X_{k-1}\smallsetminus X_{k}),\qquad k=1,2,\dots. |  | (12.9) |

#### 12.4. Dynamically generated chains stabilize fast

Consider a strictly descending chain of varieties ( 12.1) satisfying the additional condition ( 12.9) on the dimensions. Then the associated words ν k = ν ⁡ ( X k) ∈ ℤ + n \nu_{k}=\nu(X_{k})\in\mathbb{Z}_{+}^{n}, in addition to the lexicographic decrease ( 12.4), display stronger monotonicity properties.

Consider the sequence of “heads” (as opposed to “tails”), obtained by truncating the words ν k \nu_{k} to their first s s symbols, [ν k] s = ( ν k n − 1, ⋯, ν k n − s) ∈ ℤ + s [\nu_{k}]_{s}=(\nu_{k}^{n-1},\cdots,\nu_{k}^{n-s})\in\mathbb{Z}_{+}^{s}, for all k = 1, 2, … k=1,2,\dots. For any lexicographically non-increasing sequence, the sequence of heads of any fixed length s s will be again non-increasing (by definition of the lexicographic order). Yet this monotonicity can be non-strict in general.

However, under the additional assumption ( 12.9) any truncated sequence of heads { [ν k] s } k = 1 ∞ \{[\nu_{k}]_{s}\}_{k=1}^{\infty} for the sequence ν k = ν ⁡ ( X k) \nu_{k}=\nu(X_{k}) will be *strictly decreasing*in the following sense:

 | ∀ s = 1, …, n − 1 [ν 1] s ≻ [ν 2] s ≻ ⋯ ≻ [ν k − 1] s = [ν k] s = ⋯ \forall s=1,\dots,n-1\qquad[\nu_{1}]_{s}\succ[\nu_{2}]_{s}\succ\cdots\succ[\nu_{k-1}]_{s}=[\nu_{k}]_{s}=\cdots |  | (12.10) |

In other words, as soon as the first equality between truncated words occurs, the rest of the chain will have the same heads. Indeed, [ν k − 1] s = [ν k] s [\nu_{k-1}]_{s}=[\nu_{k}]_{s} if and only if all irreducible components of X k − 1 X_{k-1} and X k X_{k} of dimensions n − s n-s and higher, are the same, which means that the difference X k − 1 ∖ X k X_{k-1}\smallsetminus X_{k} is at most ( n − s − 1) (n-s-1) -dimensional.

Such type of descent ensures much faster convergence. Indeed, the first letter stabilizes after no more than ‖ ν 1 ‖ \|\nu_{1}\| steps, after which the problem is reduced to that for the tails, which are words of length n − 1 n-1. The corresponding inductive inequality is very simple.

###### Example 12.2.

Denote by g ⁡ ( n, d) g(n,d) the maximal length of decreasing sequence of words of length n n growing no faster than linear in the sense of the norm, ‖ ν k ‖ ⩽ d + k \|\nu_{k}\|\leqslant d+k, with d d being an integer parameter as in ( 12.2), under the additional assumption ( 12.10). Then the above observation implies that the length until stabilization of the first letter is at most d d, whereas the sequence of tails of length n − 1 n-1 starts from the word of norm no greater than d + d = 2 ​ d d+d=2d and hence its length by the induction assumption is no greater than g ⁡ ( n − 1, 2 ​ d) g(n-1,2d), so that finally

 | g ⁡ ( n, d) ⩽ d + g ⁡ ( n − 1, 2 ​ d), g ⁡ ( 1, d) ⩽ d. g(n,d)\leqslant d+g(n-1,2d),\qquad g(1,d)\leqslant d. |  | (12.11) |

This gives an upper bound for the length,

 | g ⁡ ( n, d) ⩽ ( 2 n − 1) ​ d, g(n,d)\leqslant(2^{n}-1)d, |  |

which is much better than in the general case considered in Example 12.1. ∎

###### Example 12.3.

In a similar way the exponential bound ( 12.3) can be treated. In this case the inductive inequality analogous to ( 12.11) takes the form

 | g ⁡ ( n, d) ⩽ d + g ⁡ ( n − 1, d d), g(n,d)\leqslant d+g(n-1,d^{d}), |  | (12.12) |

which gives g ⁡ ( n, d) g(n,d) as a tower function of height n n. Though not elementary, this is obviously a primitive recursive function of both arguments. ∎

These simple examples illustrate the algorithmic complexity of the problem on lengths of lexicographically descending chains. For descending chains of algebraic varieties the answer follows in fact from Example 12.3, since the degrees of equations defining the algebraic varieties X k X_{k} grow exponentially: deg ⁡ F k = d k \deg F^{k}=d^{k}, where d = deg ⁡ F d=\deg F (without loss of generality we may assume that deg ⁡ X = d \deg X=d with the same d d). The bounds for the norms ‖ ν ⁡ ( X k) ‖ \|\nu(X_{k})\| follow from a version of Bézout theorem due to J. Heintz [Hei83].

The most technically difficult case is that of ascending chains of polynomial ideals, mainly since there is no uniqueness in the primary decomposition of such ideals, hence one cannot associate a word ν ⁡ ( I) \nu(I) with an ideal I I, counting the number of primary components of various dimensions. However, the components of the maximal dimensions are correctly defined and may be counted, which allows to implement a similar inductive proof. Details can be found in [NY99b].

### 13. Restricted quasialgebraicity of Picard–Vessiot fields

Quasialgebraicity of a function field was defined as a property allowing for counting zeros globally. However, for technical reasons we need a weaker notion of *restricted quasialgebraicity*. Assuming U ⊂ ℂ U\subset{\mathbb{C}} being a simply connected (usually polygonal or circular) domain containing no singular points on its boundary (but eventually some singularities *inside*U U), we can restrict functions from ℂ ⁡ ( X) {\mathbb{C}}(X) on U U. The result, denoted by ℂ U ​ ( X) {\mathbb{C}}_{U}(X), is another functional field, again consisting of multivalued functions.

###### Definition 10.

We say that ℂ ⁡ ( X) {\mathbb{C}}(X) is *restricted quasialgebraic in U U*, if the upper bounds on the number of isolated zeros in any triangle T ⊂ U ∖ Σ T\subset U\smallsetminus\varSigma can be given in the same terms as before, plus eventually some geometric parameters describing the relative position of Σ \varSigma and U U, most often the distance between Σ \varSigma and the boundary ∂ U \partial U.

#### 13.1. Bounds in the disk for polynomial systems

The above discussion allows to analyze completely the polynomial case.

###### Theorem 8

If the coefficients matrix A ⁡ ( t) A(t) of a linear system ( 8.2) is polynomial as in ( 11.6) with bounded matrix coefficients of known total norm R R, then the corresponding Picard–Vessiot extension ℂ ⁡ ( X) {\mathbb{C}}(X) will be quasialgebraic after restriction on any disk D r ⊂ ℂ D_{r}\subset{\mathbb{C}} of radius r r.

In other words, the bounds on the number of zeros of functions from ℂ D r ​ ( X) {\mathbb{C}}_{D_{r}}(X) will be explicit but depending on r r. As r → + ∞ r\to+\infty, the bounds explode.

Explosion of the bounds occurs for a very simple reason: the singular point at infinity is in general an irregular (and certainly non-Fuchsian) singularity which may be an accumulation point for isolated roots of polynomial combinations (see § 8.4).

#### 13.2. Fuchsian system: reduction to the polynomial case

To apply the previous technique to a Fuchsian system ( 8.5), it is sufficient to introduce the new independent (complex time) variable.

The matrix function A ⁡ ( t) A(t) from ( 8.5) can be reduced to the common denominator,

 | A ⁡ ( t) = 1 χ ⁡ ( t) ​ P ​ ( t), P = ∑ i = 0 d − 1 P i ​ t i, χ ⁡ ( t) = ∏ i = 1 d ( t − t i). A(t)=\tfrac{1}{\chi(t)}P(t),\qquad P=\sum_{i=0}^{d-1}P_{i}t^{i},\qquad\chi(t)=\prod_{i=1}^{d}(t-t_{i}). |  |

The corresponding linear system is *orbitally*equivalent to the *polynomial*system

 | { X ˙ = P ⁡ ( t) ​ X, t ˙ = χ ⁡ ( t), ⋅ = d d ​ τ, \left\{\begin{aligned} \dot{X}&=P(t)X,\\ \dot{t}&=\chi(t),\end{aligned}\right.\qquad\cdot=\frac{d}{d\tau}, |  | (13.1) |

where τ ∈ ℂ \tau\in{\mathbb{C}} is the new time variable. The map

 | t ↦ τ ⁡ ( t) = ∫ 0 t d ​ z χ ⁡ ( z) t\mapsto\tau(t)=\int_{0}^{t}\frac{dz}{\chi(z)} |  |

is defined on the universal covering surface of ℂ ∖ Σ {\mathbb{C}}\smallsetminus\varSigma and takes explicitly bounded values away from Σ \varSigma. The inverse map τ ↦ t ⁡ ( τ) \tau\mapsto t(\tau) covers the complement ℂ ∖ Σ {\mathbb{C}}\smallsetminus\varSigma so that for any triangle T ⋐ ℂ ∖ Σ T\Subset{\mathbb{C}}\smallsetminus\varSigma on distance ε > 0 \varepsilon>0 from Σ \varSigma one can find ρ \rho such that T T is covered by the image of the disk { | τ | < ρ } ⊂ ℂ \{|\tau|<\rho\}\subset{\mathbb{C}}.

Application of Theorem 8 to the system ( 13.1) implies the following corollary (after some preliminary work).

###### Corollary 3

The field ℂ ⁡ ( X) {\mathbb{C}}(X) constructed from the Fuchsian system ( 8.5), is quasialgebraic in any domain containing no singular points from Σ \varSigma. The bounds would depend on r = r ⁡ ( U) = dist ⁡ ( ∂ U, Σ) = dist ⁡ ( U ¯, Σ) r=r(U)=\operatorname{dist}(\partial U,\varSigma)=\operatorname{dist}(\overline{U},\varSigma) and explode as r → 0 + r\to 0^{+}.

#### 13.3. Rational systems with apparent singularities

Actually, not all singular points are dangerous. As was already remarked, Theorem 7 is not about the number of zeros of solutions inside a triangle T T, but rather about the variation of argument of these solutions along the boundary of T T.

This means that the above theorems on restricted quasialgebraicity of Fuchsian systems away from their poles, can be reformulated as assertions on computability of upper bounds for the variation of argument along polygonal paths distant from the singular locus Σ \varSigma.

If the domain U U has only *apparent*singularities inside, then all solutions of the system ( 8.2) are meromorphic in U U and the order of their poles can be explicitly bounded in terms of the corresponding residue norms ‖ A j ‖ \|A_{j}\|. By the argument principle, this together with the bounds on the index along the boundary, implies restricted quasialgebraicity of ℂ U ​ ( X) {\mathbb{C}}_{U}(X).

This remark shows that it is the multivaluedness of solutions rather than any other circumstance, that is an obstruction for the global quasialgebraicity. In the next sections we show how multivalued functions can be treated, first locally and then globally.

## Lecture V Isomonodromic reduction principle and Riemann–Hilbert problem

### 14. Isomonodromic fields: local theory

#### 14.1. Euler field: an example

The Euler field ( 8.7), obtained by adjoining to ℂ {\mathbb{C}} all entries of the (multivalued) matrix function t A = exp ⁡ ( A ​ ln ⁡ t) t^{A}=\exp(A\ln t) solving the system ( 8.6), already occurred as a first example when quasialgebraicity could be expected.

The necessary condition for quasialgebraicity is given in terms of the spectrum of the constant matrix A A (the only residue of the system). We have already seen that if some of the eigenvalues are non-real, then infinitely many real zeros may easily accumulate to the origin. It can be relatively easily seen that *under*this assumption on the spectrum of A A, such accumulation is impossible not only for real, but also for complex zeros. Actually, a stronger assertion holds: the *number*of isolated roots can be explicitly majorized.

The following result (together with explicit bounds that in this case are rather accurate) can be found in [KY96]. Consider a finite *set of exponents*S ⊂ ℂ S\subset{\mathbb{C}} of diameter diam ⁡ S = max λ, λ ′ ∈ S ⁡ | λ − λ ′ | \operatorname{diam}S=\max_{\lambda,\lambda^{\prime}\in S}|\lambda-\lambda^{\prime}| whose points may have non-trivial multiplicities ν ⁡ ( λ) ∈ ℕ \nu(\lambda)\in\mathbb{N}, so that by definition ∑ λ ∈ S ν ⁡ ( λ) = #​ S \sum_{\lambda\in S}\nu(\lambda)=\#S.

###### Theorem 9

If S ⊂ ℝ S\subset{\mathbb{R}}, then the number of isolated roots of any finite sum

 | ∑ λ, k c k ​ λ ​ t λ ​ ln k − 1 ​ t, λ ∈ S, k ⩽ ν ⁡ ( λ), c k ​ λ ∈ ℂ, \sum_{\lambda,k}c_{k\lambda}\,t^{\lambda}\ln^{k-1}t,\qquad\lambda\in S,\ k\leqslant\nu(\lambda),\ c_{k\lambda}\in{\mathbb{C}}, |  | (14.1) |

in any triangle T ⊂ ℂ ∖ { 0 } T\subset{\mathbb{C}}\smallsetminus\{0\} is no greater than #​ S − 1 + 2 ​ diam ⁡ S \#S-1+2\operatorname{diam}S.∎

This theorem implies quasialgebraicity of the Euler field, since any element f f from ℂ ⁡ [t A] {\mathbb{C}}[t^{A}] can be represented in the form ( 14.1) with explicit control over diam ⁡ S \operatorname{diam}S and #​ S \#S expressed in terms of ‖ A ‖ \|A\|, dim A \dim A and deg ⁡ f \deg f.

The assumption of this theorem can be formulated in terms of the spectrum of the (only) monodromy operator.

###### Corollary 4

If the spectrum of the monodromy operator M M corresponding to a small loop around the origin, belongs to the unit circle ( i.e., all eigenvalues have modulus 1 1), then the Euler field ℂ ⁡ ( t A) {\mathbb{C}}(t^{A}) is globally quasialgebraic, and the number of isolated zeros can be bounded in terms of the norm ‖ A ‖ \|A\|.

#### 14.2. Restricted quasialgebraicity near a Fuchsian point

Consider a Fuchsian system ( 8.5) with a singular point t 1 = 0 t_{1}=0 at the origin and all residues of norm ⩽ R \leqslant R. Let ρ \rho be a (sufficiently small) positive number such that all other singularities are at least 2 ​ ρ 2\rho -distant and at most 1 / ρ 1/\rho -distant from the origin.

Let M M be a monodromy matrix corresponding to a small positively oriented loop around the origin (this matrix is defined up to a conjugacy) and S ⊂ ℂ S\subset{\mathbb{C}} the spectrum of M M (i.e., the collection of eigenvalues which is independent of anything but the system and the singular point).

###### Theorem 10

If S ⊂ { | λ | = 1 } S\subset\{|\lambda|=1\}, then the field ℂ ⁡ ( X) {\mathbb{C}}(X) is quasialgebraic in the disk D ρ = { | t | < ρ } D_{\rho}=\{|t|<\rho\}. The bound on the number of isolated zeros can be given in terms of R R and 1 / ρ 1/\rho.

The outline of the proof of this theorem occupies the rest of this section. A similar result was proved in [RY96] for *linear equations*of order n n near a Fuchsian singular point.

#### 14.3. Joint fields

Consider a Fuchsian singular point t 1 = 0 t_{1}=0 of the system ( 8.5) with the corresponding residue matrix A 1 = B A_{1}=B. Then the fundamental matrix solution X ⁡ ( t) X(t) in any disk D D containing no other singularities, can be represented as

 | X ⁡ ( t) = Y ⁡ ( t) ​ t B, t ∈ D, X(t)=Y(t)\,t^{B},\qquad t\in D, |  | (14.2) |

where Y Y is a meromorphic (single-valued) function of t t in D D. Replacing if necessary B B by B + r ​ E B+rE with an appropriate r ∈ ℤ r\in\mathbb{Z}, one can always consider Y ⁡ ( t) Y(t) as a holomorphic function at t = 0 t=0. Expanding all matrix products, we conclude that the field ℂ ⁡ ( X) {\mathbb{C}}(X) belongs to a bigger field ℂ ⁡ ( Z, Y) {\mathbb{C}}(Z,Y) spanned jointly by entries of the two matrix functions, Z ⁡ ( t) = t B Z(t)=t^{B} and Y ⁡ ( t) Y(t). Whereas the field ℂ ⁡ ( Z) {\mathbb{C}}(Z) is a Picard–Vessiot extension for the Euler system, this is not immediately obvious concerning the extension field ℂ ⁡ ( Y) {\mathbb{C}}(Y). However, we claim that the field ℂ ⁡ ( Y) {\mathbb{C}}(Y) is a subfield of a bigger Picard–Vessiot field for some other Fuchsian system having t = 0 t=0 as an apparent singularity. Indeed,

 | Y ˙ = X ˙ ​ t − B − t − 1 ​ X ​ t − B ​ B = A ⁡ ( t) ​ Y − t − 1 ​ Y ​ B. \dot{Y}=\dot{X}\,t^{-B}-t^{-1}Xt^{-B}\,B=A(t)Y-t^{-1}YB. |  | (14.3) |

This is *not*a linear system for Y Y as a matrix function to satisfy (since it involves the matrix multiplication from both sides). But if all entries of Y Y are arranged as one column vector, then ( 14.3) becomes a system of n 2 n^{2} linear ordinary differential equations with rational coefficients, exhibiting a Fuchsian singularity at t = 0 t=0 (actually, at all other poles of A ⁡ ( t) A(t) as well). The residues of this larger-size system can be explicitly constructed and their norms bounded from above.

The joint field ℂ ⁡ ( Z, Y) {\mathbb{C}}(Z,Y) possesses a property that was already used for “single” extension fields.

###### Lemma 11

Variation of argument of any element from the joint field ℂ ⁡ ( X, Y) {\mathbb{C}}(X,Y) along a polygonal path distant from the union of singular loci, is a computable function. The same is true also for sufficiently small circular arcs around each singular point.

Note that t = 0 t=0 by construction is an apparent singularity for this system. Thus the Picard–Vessiot field ℂ ⁡ ( Y) {\mathbb{C}}(Y) is quasialgebraic restricted on D D, as follows from § 13.3.

The problem that we face now, is to prove the *restricted*quasialgebraicity in D D of the joint extension field ℂ D ​ ( Z, Y) {\mathbb{C}}_{D}(Z,Y) containing ℂ D ​ ( X) {\mathbb{C}}_{D}(X) by virtue of ( 14.2), having already established restricted quasialgebraicity of each of the fields ℂ D ​ ( Z) {\mathbb{C}}_{D}(Z) and ℂ D ​ ( Y) {\mathbb{C}}_{D}(Y) separately and the fact that Y Y has only one apparent singularity in D D. This will be done by reducing the question on (restricted) quasialgebraicity of ℂ D ​ ( Z, Y) {\mathbb{C}}_{D}(Z,Y) to that for ℂ ⁡ ( Z) {\mathbb{C}}(Z), using the fact that Y Y has a trivial monodromy in D D. This reduction can be extracted from the papers by Petrov [Pet88, Pet90].

First we need some real analysis.

#### 14.4. Real closedness

Real part of an analytic function f f on an open domain U U is not analytic (unless it is a constant). Yet the real part of the restriction f | γ f|_{\gamma} on an analytic curve γ ⊂ U \gamma\subset U can be extended to a neighborhood of γ \gamma and sometimes to the whole of U U as an analytic function (of course, taking non-real values outside of γ \gamma).

If U = D U=D is a disk centered at the origin and γ \gamma the real line ℝ {\mathbb{R}}, then for any function f f meromorphic in D D one can take

 | Re ⁡ f ⁡ ( t) = 1 2 ​ ( f ⁡ ( t) + f ⁡ ( t ¯) ¯), Im ⁡ f ⁡ ( t) = 1 2 ​ i ​ ( f ⁡ ( t) − f ⁡ ( t ¯) ¯), \operatorname{Re}f(t)=\tfrac{1}{2}(f(t)+\overline{f(\bar{t})}),\qquad\operatorname{Im}f(t)=\tfrac{1}{2i}(f(t)-\overline{f(\bar{t})}), |  | (14.4) |

and then Re ⁡ f \operatorname{Re}f and Im ⁡ f \operatorname{Im}f will again be meromorphic in D D and equal to the real (resp., imaginary) part of f f on ℝ {\mathbb{R}}.

This observation allows to assume without loss of generality that all generators of the field ℂ ⁡ ( Y) {\mathbb{C}}(Y) are real on the real axis. Otherwise, one should take their real and imaginary parts Re ⁡ Y \operatorname{Re}Y and Im ⁡ Y \operatorname{Im}Y as above (both are meromorphic matrix functions real on ℝ ∩ D {\mathbb{R}}\cap D) and consider the field ℂ ⁡ ( Re ⁡ Y, Im ⁡ Y) {\mathbb{C}}(\operatorname{Re}Y,\operatorname{Im}Y) obviously containing ℂ ⁡ ( Y) {\mathbb{C}}(Y). All properties of the field ℂ ⁡ ( Y) {\mathbb{C}}(Y) are inherited by ℂ ⁡ ( Re ⁡ Y, Im ⁡ Y) {\mathbb{C}}(\operatorname{Re}Y,\operatorname{Im}Y).

For a multivalued function f f ramified over the origin t = 0 ∈ D t=0\in D, taking its real or imaginary part on the whole real axis is an ambiguous operation because of the ramification: the real part on the positive semiaxis ℝ + {\mathbb{R}}_{+} can cease to be real after continuation on the negative semiaxis ℝ − {\mathbb{R}}_{-}. Yet one can often guarantee that the field as a whole is closed by taking real/imaginary parts along any segment of the real axis.

###### Lemma 12

Let A ∈ Mat n × n ⁡ ( ℝ) A\in\operatorname{Mat}_{n\times n}({\mathbb{R}}) be a real constant matrix and ℂ ⁡ ( Z) {\mathbb{C}}(Z), Z ⁡ ( t) = t A Z(t)=t^{A}, the corresponding Euler field. Then for any function f ∈ ℂ ⁡ ( Z) f\in{\mathbb{C}}(Z) its real or imaginary part can be extended from the positive semiaxis ℝ + {\mathbb{R}}_{+} or the negative semiaxis ℝ − {\mathbb{R}}_{-} to functions g ± g_{\pm} again belonging to ℂ ⁡ ( Z) {\mathbb{C}}(Z):

 | ∀ f ∈ ℂ ⁡ ( Z) ​ ∃ g ± ∈ ℂ ⁡ ( Z): Re ⁡ f | ℝ ± = g ± | ℝ ±, \forall f\in{\mathbb{C}}(Z)\ \exists g_{\pm}\in{\mathbb{C}}(Z)\colon\quad\operatorname{Re}f|_{{\mathbb{R}}_{\pm}}=g_{\pm}|_{{\mathbb{R}}_{\pm}}, |  |

and the same for the imaginary parts Im ⁡ f | ℝ ± \operatorname{Im}f|_{{\mathbb{R}}_{\pm}}.

We will denote the functions g ± = Re ⁡ f ℝ ± g_{\pm}=\operatorname{Re}f_{{\mathbb{R}}_{\pm}} and their imaginary counterparts by Re ± ⁡ f \operatorname{Re}_{\pm}f and Im ± ⁡ f \operatorname{Im}_{\pm}f respectively.

###### Proof.

The field ℂ ⁡ ( Z) {\mathbb{C}}(Z) is independent of the choice of the fundamental solution, hence for each semiaxis ℝ ± {\mathbb{R}}_{\pm} one can choose a solution Z ± Z_{\pm} of the Euler system t ​ Z ˙ = A ​ Z t\dot{Z}=AZ that is real on that semiaxis (recall that the matrix A A is real so A ⁡ ( t) = t − 1 ​ A A(t)=t^{-1}A is real-valued on ℝ {\mathbb{R}}). Then it remains only to define g ± g_{\pm} using the identities

 | Re ⁡ ( ∑ c α ​ Z ± α) = ∑ α ( Re ⁡ c α) ​ Z ± α ∈ ℂ ⁡ [Z], c α ∈ ℂ, \operatorname{Re}\bigl(\sum c_{\alpha}Z_{\pm}^{\alpha}\bigr)=\sum_{\alpha}(\operatorname{Re}c_{\alpha})Z_{\pm}^{\alpha}\in{\mathbb{C}}[Z],\qquad c_{\alpha}\in{\mathbb{C}}, |  |

and similarly for the imaginary part (with obvious modifications for the field of fractions ℂ ⁡ ( Z) {\mathbb{C}}(Z)). ∎

###### Remark.

The fact that the matrix A A is real, is not a restriction: one can always consider a bigger Euler field of dimension 2 ​ n 2n with the real block-diagonal matrix diag ⁡ ( Re ⁡ A, Im ⁡ A) \operatorname{diag}(\operatorname{Re}A,\operatorname{Im}A).

#### 14.5. Variation of argument and zeros of imaginary part

The following elementary statement will play the central role in the constructions below.

###### Lemma 13

If f: ℝ ⊃ [a, b] → ℂ f\colon{\mathbb{R}}\supset[a,b]\to{\mathbb{C}} is a complex-valued function having no zeros on the real interval [a, b] [a,b], then variation of argument of f f along this interval is no greater than π ( #{ Im f = 0 } + 1) \pi(\#\{\operatorname{Im}f=0\}+1).

Note that here no extension from [a, b] [a,b] is required, hence Im ⁡ f \operatorname{Im}f stands for the usual imaginary part of the restriction.

###### Proof.

If | Arg ⁡ f ⁡ ( t 1) − Arg ⁡ f ⁡ ( t 2) | > π |\operatorname{Arg}f(t_{1})-\operatorname{Arg}f(t_{2})|>\pi, then the imaginary part Im ⁡ f \operatorname{Im}f must vanish somewhere between t 1 t_{1} and t 2 t_{2} on [a, b] [a,b]. ∎

Actually, this result is true for any linear combination α ​ Re ⁡ f + β ​ Im ⁡ f \alpha\operatorname{Re}f+\beta\operatorname{Im}f. The function f f may be allowed to have isolated zeros (but certainly not vanishing identically), provided that zeros of Im ⁡ f \operatorname{Im}f are counted with multiplicities.

#### 14.6. Isomonodromic reduction: the local case

Now everything is ready to prove that quasialgebraicity of ℂ ⁡ ( Z) {\mathbb{C}}(Z) implies the restricted quasialgebraicity of ℂ ⁡ ( Z, Y) {\mathbb{C}}(Z,Y) in D = { | t | < 1 } D=\{|t|<1\}, provided that Y ⁡ ( t) Y(t) is single-valued in D D and satisfies a Fuchsian system with bounded residues and all singularities ε \varepsilon -distant from ∂ D \partial D.

Any function f ∈ ℂ ⁡ ( Z, Y) f\in{\mathbb{C}}(Z,Y) can be written in D D as

 | f ( t) = ∑ 1 N z i ( t) y i ( t), z i ∈ ℂ ( Z), y i ∈ ℂ D ( Y), i = 1, …, N, f(t)=\sum_{1}^{N}z_{i}(t)y_{i}(t),\qquad z_{i}\in{\mathbb{C}}(Z),\ y_{i}\in{\mathbb{C}}_{D}(Y),\ i=1,\dots,N, |  | (14.5) |

where y i y_{i} are *monomials*from the field ℂ ⁡ ( Y) {\mathbb{C}}(Y) and hence real on ℝ {\mathbb{R}}, and the number of terms N N as well as the degrees deg ⁡ z i, deg ⁡ y i \deg z_{i},\deg y_{i} (with respect to the corresponding fields ℂ ⁡ ( Z) {\mathbb{C}}(Z) and ℂ D ​ ( Y) {\mathbb{C}}_{D}(Y)) are explicitly computable in terms of deg ⁡ f \deg f with respect to ℂ ⁡ ( X) ⊂ ℂ ⁡ ( Z, Y) {\mathbb{C}}(X)\subset{\mathbb{C}}(Z,Y). Indeed, for each generator X i ​ j X_{ij} of degree 1 1 in ℂ ⁡ ( X) {\mathbb{C}}(X) such representation can be chosen with no more than n n terms, each being bilinear in Y Y and Z Z.

Assume that the field ℂ ⁡ ( Z) {\mathbb{C}}(Z) is quasialgebraic. Then division by z 1 z_{1} changes the number of zeros by no more than some known number. Hence when counting the number of zeros of f f in any triangle T ⊂ D ∖ { 0 } T\subset D\smallsetminus\{0\}, one can assume that z 1 ​ ( t) ≡ 1 z_{1}(t)\equiv 1, that is, f = y 1 + ∑ 2 N z i ​ y i f=y_{1}+\sum_{2}^{N}z_{i}y_{i}.

Also without loss of generality we may assume that T T does not intersect the real axis (this can be also always achieved by subdividing it into smaller triangles if necessary), and belongs to the upper half-plane. Then the number of zeros of f f in T T is no greater than the sum of four terms, variation of argument of f f along the sufficiently small arc { | t | = ε 0 ≪ 1, Im t > 0 } \{|t|=\varepsilon_{0}\ll 1,\ \operatorname{Im}t>0\} around the origin, and similar contributions from the semicircle { | t | = 1, Im ⁡ t > 0 } \{|t|=1,\ \operatorname{Im}t>0\}, and two rectilinear intervals [− 1, − ε 0) ⊂ ℝ − [-1,-\varepsilon_{0})\subset{\mathbb{R}}_{-} and ( ε 0, 1] ⊂ ℝ + (\varepsilon_{0},1]\subset{\mathbb{R}}_{+} respectively.

The contributions from the two circular arcs are computable functions by Lemma 11. As for the two rectilinear segments, the contribution of each of them is bounded by the number of zeros of Im ⁡ f \operatorname{Im}f on them. By the assumption on the matrix function Y Y, Im ⁡ y i ≡ 0 \operatorname{Im}y_{i}\equiv 0, hence

 | Im ± ⁡ f = Im ⁡ y 1 + ∑ 2 N y i ​ Im ⁡ z i = ∑ 2 N y i ​ Im ± ​ z i. \operatorname{Im}_{\pm}f=\operatorname{Im}y_{1}+\sum_{2}^{N}y_{i}\operatorname{Im}z_{i}=\sum_{2}^{N}y_{i}\operatorname{Im}_{\pm}z_{i}. |  |

By Lemma 12, the field ℂ ⁡ ( Z) {\mathbb{C}}(Z) is closed by taking imaginary parts, hence for all i i the functions Im ± ⁡ z i \operatorname{Im}_{\pm}z_{i} are again in ℂ ⁡ ( Z) {\mathbb{C}}(Z). Thus the question on the number of zeros of f f represented by 14.5 in T T is reduced to that for the number of zeros of two functions Im + ⁡ f, Im − ⁡ f ∈ ℂ ⁡ ( Z, Y) \operatorname{Im}_{+}f,\operatorname{Im}_{-}f\in{\mathbb{C}}(Z,Y) (one for each semiaxis), each of them involving less terms (at most N − 1 N-1). This allows to continue the process inductively, reducing the problem for zeros of f f to that for some 2 N 2^{N} functions from ℂ ⁡ ( Z) {\mathbb{C}}(Z). On the last step the number of isolated zeros of a product z N ​ y N z_{N}y_{N} is majorized by the sum of zeros of each term (known since quasialgebraicity of ℂ ⁡ ( Z) {\mathbb{C}}(Z) and ℂ ⁡ ( Y) {\mathbb{C}}(Y) is already established).

###### Remark.

The above described construction reducing quasialgebraicity of the joint field ℂ D ​ ( Z, Y) {\mathbb{C}}_{D}(Z,Y) to that of ℂ D ​ ( X) {\mathbb{C}}_{D}(X) if Y Y has trivial monodromy in D D, is very similar to the standard differentiation-division scheme (based on the Rolle lemma) used to obtain bounds on the number of isolated zeros of real functions. Here the role of the differentiation is played by the operators Im ± \operatorname{Im}_{\pm}, whereas single-valued functions real on ℝ {\mathbb{R}} play the role of constants killed by differentiation.

#### 14.7. Non-uniform quasialgebraicity

From Theorem 10 one can immediately derive non-uniform quasialgebraicity of Fuchsian systems. Consider such a system with d d singular points.

Notice that the residue matrices A j A_{j} are invariant by conformal automorphisms of the independent variable, hence the residual norm of the corresponding matrix function R = max i = 1, …, d ⁡ ‖ A i ‖ R=\max_{i=1,\dots,d}\|A_{i}\| is also invariant.

Using such conformal automorphisms, one can always place any three poles of A ⁡ ( t) A(t) at any three points, say, 0, 1 0,1 and ∞ \infty, but starting from the fourth pole, one has a nontrivial parameter characterizing the spread of singular points on the sphere. Let ρ \rho be a small positive number such that:

1. (1)

| t i − t j | ⩾ 2 ​ ρ |t_{i}-t_{j}|\geqslant 2\rho, i, j = 1, …, d i,j=1,\dots,d, i ≠ j i\neq j;

2. (2)

| t i | ⩽ 1 / ρ |t_{i}|\leqslant 1/\rho, i = 1, …, d i=1,\dots,d.

Consider the monodromy matrices M j M_{j} corresponding to small loops going around t j t_{j}. As before, their spectra S j S_{j} are uniquely defined.

###### Theorem 11

If all spectra S j S_{j} belong to the unit circle, then the field ℂ ⁡ ( X) {\mathbb{C}}(X) is quasialgebraic. The bound for the number of zeros can be given in terms of R R and ρ \rho.

###### Proof.

Draw disjoint circles of radius ρ \rho around each singularity and of radius 1 / ρ 1/\rho around the origin (this circle bounds a neighborhood of infinity on ℂ ​ P 1 {\mathbb{C}}P^{1}). Restricted on each circle, the field is quasialgebraic by Theorem 10. On the complement there are no singularities, so after triangulation of this multiply connected domain one can apply Corollary 3. ∎

### 15. Uniform quasialgebraicity of Fuchsian systems

In this section we briefly explain additional work to be done in order to obtain the bounds for quasialgebraicity, that would be independent on the relative position of singular points. In other words, we look for bounds that would remain explicit and uniform over ρ \rho as the latter tends to zero.

#### 15.1. Isomonodromic reduction: the general case

The constructions of the previous section can be easily modified for a more general situation. Assume that two Fuchsian systems with fundamental solutions X ⁡ ( t) X(t) and Z ⁡ ( t) Z(t) are *isomonodromic relative to a domain U U*, that is, they have the same singular locus Σ \varSigma in U U and the monodromy matrices M γ M_{\gamma} for all loops entirely belonging to U U, are the same for the two. Next, assume that the residues (all of them, including those at singular points outside U U) are all explicitly bounded. Finally, assume that U U is a polygonal domain (say, a triangle) and the boundary ∂ U \partial U is away from all singularities.

Then one can claim that the two fields ℂ ⁡ ( X) {\mathbb{C}}(X) and ℂ ⁡ ( Z) {\mathbb{C}}(Z) when restricted on U U are both quasialgebraic or not quasialgebraic simultaneously.

The proof in the case when all singularities in U U fall on one straight line, is very similar to the local case. Namely, consider the matrix fraction Y ⁡ ( t) = X ⁡ ( t) ​ Z − 1 ​ ( t) Y(t)=X(t)Z^{-1}(t) possessing trivial monodromy in U U and embed ℂ ⁡ ( X) {\mathbb{C}}(X) into the joint field ℂ ⁡ ( Z, Y) {\mathbb{C}}(Z,Y). Writing elements of this joint field as ∑ y i ​ z i \sum y_{i}z_{i} and applying the above algorithm of alternating division and taking the imaginary parts, the question on the number of zeros of f ∈ ℂ ⁡ ( X) f\in{\mathbb{C}}(X) can be reduced to that for several auxiliary functions from ℂ ⁡ ( Z) {\mathbb{C}}(Z).

#### 15.2. Inductive strategy

The isomonodromic reduction principle as described above, would allow for an inductive proof of the uniform quasialgebraicity of Fuchsian systems if one could always construct a Fuchsian system that would be isomonodromic to a given one in a specified simply connected domain, while having no other singularities outside this domain.

The inductive proof may look as follows. For Fuchsian system with only two singularities (Euler systems) the quasialgebraicity is known. Assume that it is already established for all systems with less than d d finite singularities, and consider a system with d d finite singular points forming the locus Σ ⊂ ℂ \varSigma\subset{\mathbb{C}}.

As was already noticed, it is impossible to make a conformal transformation placing all d d points of Σ \varSigma well apart from each other. However, one can always achieve a situation when all finite singular points form a set of diameter *exactly*1 1 inside the disk of radius 1 1 centered at the origin. In this case one can draw a line that is at least 1 / 2 ​ d 1/2d -distant from all points of Σ \varSigma and such that to each side of this line lies at least one (hence at most d − 1 d-1) point(s) of Σ \varSigma.

Now one can easily construct two polygonal domains each containing no more than d − 1 d-1 points of Σ \varSigma, together covering the whole of Σ \varSigma and with boundaries distant from both Σ \varSigma and the infinity.

Assume that for each such domain U U a Fuchsian system can be found so that it will be isomonodromic with the given one in U U, while still having the residual norm bounded in terms of the residual norm of the initial system.

Then application of the isomonodromic reduction principle would allow to reduce the question on quasialgebraicity of the initial system in U U to that for a Fuchsian system with ⩽ d − 1 \leqslant d-1 finite singular points. By the inductive assumption, the latter question can be explicitly answered.

The only assumption to monitor along this inductive process, is that on eigenvalues of the monodromy operators. Clearly, one should assume that the spectral condition (on unit absolute values of eigenvalues) holds for all small loops around singular points. However, it is not sufficient, since this condition does not survive the above surgery (cutting out part of the singularities inside U U and pasting out the rest). Indeed, after replacing all singularities outside U U by one singular point at infinity, we create a point whose local monodromy coincides with that of the boundary ∂ U \partial U. Thus one must additionally assume that the monodromy along the boundary of U U must also satisfy the spectral condition.

Unfortunately, there is no way to predict how the partition into distant “clusters” of singular points will proceed when carried out inductively. Instead it is sufficient to assume that the spectral condition is satisfied for any simple loops (geometrically non-selfintersecting closed Jordan curves).

This conditional construction would prove the following theorem.

###### Theorem 12

If the monodromy operators along all simple loops have only eigenvalues of modulus 1 1, then the Fuchsian system is uniformly quasialgebraic. Upper bounds for the number of isolated zeros can be given in terms of the number of singular points and the residual norm of the system, uniformly over all configurations of the singularities.

However, the proof above gives only a general idea of how the actual proof is organized. The difficulties are of two kinds, technical and fundamental.

An example of the technical problem is the isomonodromic reduction principle: it was formulated (and is actually proved) for a particular case when all singular points lie on just one straight line (which can then be identified with the real axis). However, it is sufficient for the purposes of the proof after suitable preparation of the initial Fuchsian system.

The fundamental problem concerns the (im)possibility of constructing a Fuchsian system with the prescribed monodromy. It was recently discovered that there exist obstructions to solvability of this problem, that have to be somehow circumvented. In addition, one has to redress the proof of the corresponding positive results so that they would become *constructive*, yielding bounds for the residual norm of the constructed systems.

### 16. Quantitative Riemann–Hilbert problem of matrix factorization

#### 16.1. Riemann–Hilbert problem: background

Given d d distinct points t 1, …, t d t_{1},\dots,t_{d} on the Riemann sphere ℂ ​ P 1 {\mathbb{C}}P^{1} and d d invertible matrices M 1, …, M d M_{1},\dots,M_{d} satisfying the identity M 1 ⋯ M d = E M_{1}\cdots M_{d}=E (the identity matrix), construct a Fuchsian system having singular points at t 1, …, t d t_{1},\dots,t_{d} and only there, for which the matrices M j M_{j} would be monodromy factors for some fundamental solution.

This is the strongest form of the problem known as Hilbert 21st problem or the *Riemann–Hilbert problem*. Here some of many known results concerning its solvability.

Plemelj theorem:

For any collection of points and any monodromy matrices, one can construct a linear system with all but one singularities Fuchsian; the last singular point is regular and can be made Fuchsian if the corresponding monodromy matrix is diagonalizable. As a corollary, one can always construct a Fuchsian system with one extra singular point that would be an apparent singularity [Ple64, AI88].

Bolibruch–Kostov theorem:

If the monodromy group generated by the matrices M j M_{j} is irreducible, then the Riemann–Hilbert problem is solvable [Bol92, Kos92].

Bolibruch counterexamples:

There exists a reducible group generated by three 4 × 4 4\times 4 -matrices, which cannot be realized as a monodromy group of a Fuchsian system [Bol90].

What is missing in all these formulations, is the possibility of placing any upper bound on the norms of the residue matrices of the corresponding Fuchsian system (provided that the problem is solvable).

#### 16.2. Surgery

In this section we formulate an analytic problem that is sufficient to solve in order to construct a system isomonodromic to the given one in a domain with all singularities away from the boundary.

Recall that we have a Fuchsian system that already possesses the poles inside U U at specified points and the monodromy around these poles is as required. What is necessary to do is to remove all finite singularities from ℂ ∖ U {\mathbb{C}}\smallsetminus U, leaving only one singular point at infinity.

For simplicity we assume that U U is the unit disk centered at the origin, and the annulus K = { 1 2 < | t | < 2 } K=\{\tfrac{1}{2}<|t|<2\} is free from singular points (i.e., Σ ∩ K = ∅ \varSigma\cap K=\varnothing). Denote by X ⁡ ( t) X(t) the (multivalued) fundamental matrix solution. In general, X X is multivalued even in K K, however, for an appropriate constant matrix B B the product W ⁡ ( t) = X ​ t − B W(t)=Xt^{-B} is a single-valued matrix function that is holomorphic and holomorphically invertible in K K.

*Suppose*that the matrix function W = X ​ t − B W=Xt^{-B}, holomorphic and invertible in K K can be represented as the matrix ratio of two other matrix functions, H 0 ​ ( t) H_{0}(t) and H ∞ ​ ( t) H_{\infty}(t), so that:

1. (1)

H 0 H_{0} is holomorphic and holomorphically invertible in the disk D 0 = { | t | < 2 } D_{0}=\{|t|<2\};

2. (2)

H ∞ ​ ( t) H_{\infty}(t) is holomorphic and holomorphically invertible in the disk D ∞ = { | t | > 1 2 } D_{\infty}=\{|t|>\tfrac{1}{2}\}, including the point t = ∞ t=\infty;

3. (3)

on the intersection K = D 0 ∩ D ∞ K=D_{0}\cap D_{\infty},

 | X ⁡ ( t) ​ t − B = H 0 − 1 ​ ( t) ​ H ∞ ​ ( t), t ∈ D 0 ∩ D ∞. X(t)\,t^{-B}=H_{0}^{-1}(t)H_{\infty}(t),\qquad t\in D_{0}\cap D_{\infty}. |  | (16.1) |

Then the two expressions, X 0 ​ ( t) = H 0 ​ ( t) ​ X ​ ( t) X_{0}(t)=H_{0}(t)X(t) defined in D 0 D_{0} and X ∞ ​ ( t) = H ∞ ​ ( t) ​ t B X_{\infty}(t)=H_{\infty}(t)\,t^{B} defined on D ∞ D_{\infty}, agree on the intersection and hence their “logarithmic derivatives” B 0 ​ ( t) = X ˙ 0 ​ ( t) ​ X 0 − 1 ​ ( t) B_{0}(t)=\dot{X}_{0}(t)X_{0}^{-1}(t) and B ∞ ​ ( t) = X ˙ ∞ ​ ( t) ​ X ∞ − 1 ​ ( t) B_{\infty}(t)=\dot{X}_{\infty}(t)X^{-1}_{\infty}(t), coincide on K K and together define a single-valued meromorphic function B ⁡ ( t) B(t) on the entire sphere ℂ ​ P 1 {\mathbb{C}}P^{1}.

The poles of B ⁡ ( t) B(t) can be easily described: due to the holomorphic invertibility of H 0, ∞ ​ ( t) H_{0,\infty}(t) they can occur either at the poles of A ⁡ ( t) A(t) that are inside D 0 D_{0}, or at t = ∞ t=\infty. In both cases the residues can be easily computed: for any t j ∈ Σ ∩ D 0 t_{j}\in\varSigma\cap D_{0},

 | B ⁡ ( t) = H 0 ​ ( t j) ⋅ A j t − t j ⋅ H 0 − 1 ​ ( t j) + ⋯, B(t)=H_{0}(t_{j})\cdot\frac{A_{j}}{t-t_{j}}\cdot H_{0}^{-1}(t_{j})+\cdots, |  |

where the dots stand for terms holomorphic at t j t_{j}. In a similar way, at infinity we have

 | B ⁡ ( t) = H ∞ ​ ( ∞) ⋅ B t ⋅ H ∞ − 1 ​ ( ∞) + O ⁡ ( 1 / t 2), B(t)=H_{\infty}(\infty)\cdot\frac{B}{t}\cdot H_{\infty}^{-1}(\infty)+O(1/t^{2}), |  |

where O ⁡ ( 1 / t 2) O(1/t^{2}) stands for a holomorphic matrix function of the corresponding growth. This means that in fact

 | B ⁡ ( t) = ∑ t j ∈ D 0 B j t − t j, B j = H 0 ​ ( t j) ​ A j ​ H 0 − 1 ​ ( t j), B(t)=\sum_{t_{j}\in D_{0}}\frac{B_{j}}{t-t_{j}},\qquad B_{j}=H_{0}(t_{j})\,{A_{j}}\,H_{0}^{-1}(t_{j}), |  | (16.2) |

and ∑ j B j = H ∞ ​ ( ∞) ​ B ​ H ∞ − 1 ​ ( ∞) \sum_{j}B_{j}=H_{\infty}(\infty)\,{B}\,H_{\infty}^{-1}(\infty).

The Fuchsian system with the matrix of coefficients B ⁡ ( t) B(t) given by ( 16.2), would serve our purposes, since its solution H 0 ​ X H_{0}X has the same monodromy in D 0 D_{0} as the initial matrix solution X X.

In order to complete the proof, one would have to obtain upper bounds on the matrices H j = H 0 ​ ( t j) H_{j}=H_{0}(t_{j}) and their inverses H j − 1 H_{j}^{-1} for all singular points t j ∈ Σ ∩ D 0 t_{j}\in\varSigma\cap D_{0}. This would imply an upper bound on the residual norm of the matrix function B ⁡ ( t) B(t) and finally would allow for the inductive proof as explained in § 15.2.

#### 16.3. Birkhoff–Grothendieck factorization

Unfortunately, finding factorization ( 16.1) satisfying all properties above, is impossible.

###### Example 16.1.

One obstruction to holomorphic factorization can be immediately seen. Consider the determinant w ⁡ ( t) = det W ⁡ ( t) w(t)=\det W(t): this is a holomorphic invertible function in the annulus K K, and variation of argument of this function along, say, the middle circle of the annulus is an integer number ν \nu. If this number is nonzero, then either det H 0 \det H_{0} or det H ∞ \det H_{\infty} must have zeros and/or poles in the respective domains D 0 D_{0} resp., D ∞ D_{\infty}.

If n = 1 n=1, i.e., all matrices are of size 1 × 1 1\times 1, then one can always achieve factorization of the form

 | W ⁡ ( t) = H 0 − 1 ​ ( t) ​ t ν ​ H ∞ ​ ( t) W(t)=H_{0}^{-1}(t)\,t^{\nu}\,H_{\infty}(t) |  | (16.3) |

with 1 × 1 1\times 1 -matrices H 0, H ∞ H_{0},H_{\infty} holomorphically invertible in the respective domains. ∎

Both the positive and the negative assertions present in the above example, admit generalization for the general n n -dimensional matrix case.

###### Theorem 13 (see [GK58, GK60])

A matrix function W ⁡ ( t) W(t) holomorphic and invertible in the annulus K K, can be factorized as follows,

 | W ⁡ ( t) = H 0 − 1 ​ t G ​ H ∞ ​ ( t), G = diag ⁡ ( ν 1, …, ν n), ν i ∈ ℤ, W(t)=H_{0}^{-1}\,t^{G}\,H_{\infty}(t),\qquad G=\operatorname{diag}(\nu_{1},\dots,\nu_{n}),\ \nu_{i}\in\mathbb{Z}, |  | (16.4) |

with the matrix factors H 0, H ∞ H_{0},H_{\infty} holomorphic and invertible in D 0 D_{0} resp., D ∞ D_{\infty}.

The integer numbers ν i \nu_{i}, called partial indices, are uniquely determined ( the same for all representations with the above properties).

The decomposition ( 16.4) can be used for surgery, if we incorporate the term t G t^{G} into H ∞ ​ ( t) H_{\infty}(t). Then the matrix function Y ⁡ ( t) Y(t) defined as H 0 ​ X H_{0}X in D 0 D_{0} and as t G ​ H ∞ ​ t B t^{G}H_{\infty}\,t^{B} in D ∞ D_{\infty}, satisfies a linear system of ordinary differential equations with only Fuchsian singular points in D 0 D_{0} and a regular non-Fuchsian point t = ∞ t=\infty. The principal Laurent part of the matrix B ⁡ ( t) = Y ˙ ​ Y − 1 B(t)=\dot{Y}Y^{-1} at y = ∞ y=\infty can be easily described: the multiplicity of the pole at infinity is bounded in terms of ν = ‖ G ‖ = max j ⁡ | ν j | \nu=\|G\|=\max_{j}|\nu_{j}|, and the magnitude (norm) of the Laurent coefficients of B B at t = ∞ t=\infty is bounded in terms of the Taylor coefficients of order ⩽ ν \leqslant\nu of the matrix H ∞ H_{\infty} and its inverse.

Actually, the form of the matrix t G ​ H ∞ ​ ( t) t^{G}H_{\infty}(t) is not important: in order to have a system with a regular singularity at infinity, it is sufficient to have a matrix factorization

 | W ⁡ ( t) = H 0 − 1 ​ H ∞, H ∞ ​ ( t) ± 1 = C ±, 0 ​ ( t) + ∑ j = 1 ν C ±, j ​ t j, W(t)=H_{0}^{-1}H_{\infty},\qquad H_{\infty}(t)^{\pm 1}=C_{\pm,0}(t)+\sum_{j=1}^{\nu}C_{\pm,j}t^{j}, |  | (16.5) |

with holomorphic invertible matrix H 0 H_{0} and meromorphic invertible matrix function H ∞ ​ ( t) H_{\infty}(t) having (together with its inverse H ∞ − 1 H_{\infty}^{-1}) the only pole at t = ∞ t=\infty of order ⩽ ν \leqslant\nu with the Laurent (matrix) coefficients C ±, j C_{\pm,j}.

###### Remark.

The assertion of Theorem 13 is certainly not the strongest known. The matrix function W ⁡ ( t) W(t) can be defined only on the middle circle { | t | = 1 } \{|t|=1\} of the annulus K K and be rather weakly regular on it, still the factorization will be possible then, with the terms H 0, H ∞ H_{0},H_{\infty} holomorphic invertible inside (resp., outside) the circle. Some non-circular contours can be also allowed.

#### 16.4. Modified surgery

One can easily modify the structure of the inductive construction above to cover the case of systems having only Fuchsian finite singular points and a regular eventually non-Fuchsian singularity at t = ∞ t=\infty. Such system has the matrix of coefficients that can be written always as

 | A ⁡ ( t) = ∑ j = 1 d A j t − t j + ∑ i = 0 ν B i ​ t i, A(t)=\sum_{j=1}^{d}\frac{A_{j}}{t-t_{j}}+\sum_{i=0}^{\nu}B_{i}t^{i}, |  | (16.6) |

and the residual norm for such systems should be defined as

 | ‖ A ⁡ ( ⋅) ‖ = ∑ j ‖ A j ‖ + ∑ i ‖ B i ‖. \|A(\cdot)\|=\sum_{j}\|A_{j}\|+\sum_{i}\|B_{i}\|. |  | (16.7) |

The surgery described in § 16.2, using the factorization ( 16.5), allows to pass from one system from such class to another system from the same class, having no finite singularities outside D 0 D_{0}. In order to carry out inductively the bounds for zeros, one has to majorize the magnitude of all Laurent coefficients of the new system in terms of the norm R = ‖ A ⁡ ( ⋅) ‖ R=\|A(\cdot)\| of the initial system.

#### 16.5. Bounds

Suppose that a system from the class ( 16.6) of explicitly bounded norm R = ‖ A ⁡ ( ⋅) ‖ R=\|A(\cdot)\| has no singularities in the annulus K = { 1 2 < | t | < 2 } K=\{\tfrac{1}{2}<|t|<2\}. Then the following bounds can be explicitly computed.

1. (1)

the norm of the monodromy M M corresponding to the circle { | t | = 1 } ⊂ K \{|t|=1\}\subset K and its matrix logarithm B B;

2. (2)

the pointwise upper bound for norm of the fundamental solution X ⁡ ( t) X(t) with X ⁡ ( 1) = E X(1)=E and its inverse X − 1 ​ ( t) X^{-1}(t) in any smaller annulus K ′ K^{\prime}, say, { 2 3 < | t | < 3 2 } \{\frac{2}{3}<|t|<\frac{3}{2}\};

3. (3)

the pointwise upper bound for ‖ W ⁡ ( t) ‖ + ‖ W − 1 ​ ( t) ‖ \|W(t)\|+\|W^{-1}(t)\| in the smaller annulus K ′ K^{\prime}.

In order to estimate the Laurent coefficients at all singular points after the surgery, it would be sufficient to find factorization ( 16.5) and supply the following bounds,

1. (1)

max t ∈ D 0 ⁡ ‖ H 0 ​ ( t) ‖ + ‖ H 0 − 1 ​ ( t) ‖ \max_{t\in D_{0}}\|H_{0}(t)\|+\|H_{0}^{-1}(t)\| (this would allow to estimate the norms of residues at all finite singularities),

2. (2)

the bound ν \nu for the order of the pole of H ∞ ± 1 H^{\pm 1}_{\infty};

3. (3)

max t ∈ D ∞ ⁡ ‖ C +, 0 ​ ( t) ‖ + ‖ C −, 0 ​ ( t) ‖ \max_{t\in D_{\infty}}\|C_{+,0}(t)\|+\|C_{-,0}(t)\| together with

4. (4)

∑ i = 1 ν ‖ C ±, i ‖ \sum_{i=1}^{\nu}\|C_{\pm,i}\| to majorize the norms of all Laurent coefficients at infinity.

#### 16.6. Quantitative matrix factorization

Unfortunately for our purposes, the known methods of constructing the Birkhoff–Grothendieck factorization ( 16.4), based on index theory for integral operators, do not allow for quantitative conclusions. Moreover, in some sense the problem admits no solution. The reason for this is the known *instability*of the partial indices ν 1, …, ν n \nu_{1},\dots,\nu_{n}: an arbitrarily small variation (in the uniform norm) of the function W W can result in a jump of the partial indices. This is clearly incompatible with existence of any bounds that would be continuous in the C 0 C^{0} -norm.

However, if we give up with the uniquely defined Birkhoff–Grothendieck decomposition, then one can satisfy all the above conditions.

###### Theorem 14 (Novikov and Yakovenko [NY01a])

A n × n n\times n -matrix function W ⁡ ( t) W(t) holomorphic and holomorphically invertible in the annulus

 | K = { ( 1 + 2 ε) − 1 < | t | < ( 1 + 2 ε) }, ε > 0, K=\{(1+2\varepsilon)^{-1}<|t|<(1+2\varepsilon)\},\qquad\varepsilon>0, |  | (16.8) |

and bounded together with its inverse there,

 | ‖ W ⁡ ( t) ‖ + ‖ W − 1 ​ ( t) ‖ < R < + ∞, t ∈ K, \|W(t)\|+\|W^{-1}(t)\|<R<+\infty,\qquad t\in K, |  | (16.9) |

can be factorized as W ⁡ ( t) = H 0 − 1 ​ H ∞ ​ ( t) W(t)=H_{0}^{-1}H_{\infty}(t) with the matrix functions H 0, H ∞ H_{0},H_{\infty} satisfying the following conditions.

1. (1)

H 0 ​ ( t) H_{0}(t) is holomorphic invertible in the disk D 0 ′ = { | t | < ( 1 + ε) } D_{0}^{\prime}=\{|t|<(1+\varepsilon)\} and satisfies the inequality ‖ H 0 ​ ( t) ‖ + ‖ H 0 − 1 ​ ( t) ‖ ⩽ R ′ \|H_{0}(t)\|+\|H_{0}^{-1}(t)\|\leqslant R^{\prime} in this disk,

2. (2)

H ∞ ​ ( t) H_{\infty}(t) is holomorphic and holomorphically invertible in the complement D ∞ ′ = { ( 1 + ε) − 1 < | t | < + ∞ } D_{\infty}^{\prime}=\{(1+\varepsilon)^{-1}<|t|<+\infty\} and both H ∞ H_{\infty} and H ∞ − 1 H_{\infty}^{-1} have at most a pole of order ν \nu at t = ∞ t=\infty;

3. (3)

the coefficients C ±, i C_{\pm,i} of the Laurent expansions

 | P ± ​ ( t) = H ∞ ± 1 ​ ( t) = ∑ i = 0 ν C ±, i ​ t i P_{\pm}(t)=H_{\infty}^{\pm 1}(t)=\sum_{i=0}^{\nu}C_{\pm,i}t^{i} |  |

are all bounded by R ′ R^{\prime} in the sense of the matrix norm;

4. (4)

the “regular parts” are bounded uniformly in D ∞ ′ D_{\infty}^{\prime} so that ‖ H ∞ + − P + ​ ( t) ‖ + ‖ H ∞ − − P − ​ ( t) ‖ ⩽ R ′ \|H_{\infty}^{+}-P_{+}(t)\|+\|H_{\infty}^{-}-P_{-}(t)\|\leqslant R^{\prime} there.

The integer parameter ν \nu and real parameter R ′ R^{\prime} can be expressed as explicit elementary functions of n, R n,R and ε \varepsilon, the “width” of the annulus K K.

#### 16.7. Conclusion

Theorem 14 provides the last tool necessary to run the inductive proof and construct an explicit primitive recursive upper bound for the number of isolated roots of solutions to Fuchsian systems. The bounds can be explicitly written down in the sense that all primitive recursions describing them, can be extracted from the constructions above. However, this has not been done, among other things, because of the very excessive bounds that appear on this way. Besides nested inductive constructions, this occurs because of very excessive bounds on the lengths of ascending chains of polynomial ideals (see § 11). However, some very recent works of A. Grigoriev suggest that this crucial step can be considerably improved and instead of a tower of four stories, something like a double exponential bound can be achieved, at least for linear systems with rational coefficients. This improvement may affect all other parts of the global construction as well, resulting in a considerably more realistic quasialgebraicity-type statements.

#### Acknowledgements

The main theme of these lecture notes was surveying several recent results obtained jointly with Dmitry Novikov, who discussed with me the text on numerous occasions and greatly contributed to putting it to the final form.

I am grateful to Dana Schlomiuk who invited me to deliver these lectures on the Workshop organized in Université de Montreal in June–July 2000. Part of these notes was written during my sabbatical stay in University of Toronto. During these periods I tried various ways of exposing parts of these notes and collected remarks and advises from many listeners, among them A. Bolibruch, Yu. Ilyashenko, M. Jakobson, V. Katsnelson, A. Khovanskii, V. Matsaev, Ch. Miller, P. Milman, B. Schapiro, P. Speisegger, Y. Yomdin.

Finally, I am very much indebted to the colleagues who read preliminary versions of these notes and pointed to numerous errors, especially to Christiane Rousseau and Iliya Iliev. Of course, the responsibility for the remaining bugs remains entirely with the author.

### References

- [AGV88] V. I. Arnol ′ d, S. M. Guseĭn-Zade, and A. N. Varchenko, *Singularities of differentiable maps*, vol. II, Monodromy and asymptotics of integrals, Birkhäuser Boston Inc., Boston, MA, 1988. MR 89g:58024
- [AI88] V. I. Arnol ′ d and Yu. S. Ilyashenko, *Ordinary differential equations*, Dynamical systems, I, Springer, Berlin, 1988, translated from Current problems in mathematics. Fundamental directions, Vol. 1, 7–149, Akad. Nauk SSSR, Vsesoyuz. Inst. Nauchn. i Tekhn. Inform., Moscow, 1985, pp. 1–148. MR 970 794
- [BD00] P. Bonnet and A. Dimca, *Relative differential forms and complex polynomials*, Bull. Sci. Math. 124 (2000), no. 7, 557–571. MR 1 793 909
- [BFY98a] M. Briskin, J.-P. Françoise, and Y. Yomdin, *The Bautin ideal of the Abel equation*, Nonlinearity 11 (1998), no. 3, 431–443. MR 99d:58128
- [BFY98b] by same author, *Une approche au problème du centre-foyer de Poincaré*, C. R. Acad. Sci. Paris Sér. I Math. 326 (1998), no. 11, 1295–1298. MR 99j:34030
- [BFY99] M. Briskin, J.-P. Francoise, and Y. Yomdin, *Center conditions, compositions of polynomials and moments on algebraic curves*, Ergodic Theory Dynam. Systems 19 (1999), no. 5, 1201–1220. MR 2000k:34051
- [Bog76] R. I. Bogdanov, *Bifurcations of a limit cycle of a certain family of vector fields on the plane*, Trudy Sem. Petrovsk. (1976), no. 2, 23–35. MR 56 #1363
- [Bol90] A. A. Bolibrukh, *The Riemann-Hilbert problem*, Uspekhi Mat. Nauk 45 (1990), no. 2(272), 3–47, 240. MR 92j:14014
- [Bol92] by same author, *Sufficient conditions for the positive solvability of the Riemann-Hilbert problem*, Mat. Zametki 51 (1992), no. 2, 9–19, 156. MR 93g:34007
- [Bol95] A. A. Bolibruch, *The Riemann-Hilbert problem and Fuchsian differential equations on the Riemann sphere*, Proceedings of the International Congress of Mathematicians, Vol. 1, 2 (Zürich, 1994) (Basel), Birkhäuser, 1995, pp. 1159–1168. MR 98e:32038
- [dlVP29] C. de la Valleé Poussin, *Sur l’équation différentielle linéaire du second ordre. détermination d’une intégrale par deux valeurs assignées. extension aux équations d’ordre n n*, J. Math. Pures Appl. 8 (1929), 125–144.
- [DRR94] F. Dumortier, R. Roussarie, and C. Rousseau, *Hilbert’s 16th problem for quadratic vector fields*, J. Differential Equations 110 (1994), no. 1, 86–133. MR 95g:58179
- [Eca92] J. Ecalle, *Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac*, Hermann, Paris, 1992. MR 97f:58104
- [For91] O. Forster, *Lectures on Riemann surfaces*, Springer-Verlag, New York, 1991. MR 93h:30061
- [FP86] J.-P. Françoise and C. C. Pugh, *Keeping track of limit cycles*, J. Differential Equations 65 (1986), no. 2, 139–157. MR 88a:58162
- [Fra96] J.-P. Francoise, *Successive derivatives of a first return map, application to the study of quadratic vector fields*, Ergodic Theory Dynam. Systems 16 (1996), no. 1, 87–96. MR 97a:58131
- [Gab99] A. Gabrielov, *Multiplicity of a zero of an analytic function on a trajectory of a vector field*, Proceedings of the Arnoldfest (Ed. by E. Bierstone, B. Khesin, A. Khovanskii, J. Marsden), Fields Institute Communications, Amer. Math. Soc., Providence, RI, 1999, pp. 191–200. MR 1 733 576
- [Gav98] L. Gavrilov, *Petrov modules and zeros of Abelian integrals*, Bull. Sci. Math. 122 (1998), no. 8, 571–584. MR 99m:32043
- [Gav01] by same author, *The infinitesimal 16th Hilbert problem in the quadratic case*, Inv. Math. (2001), no. 143, 449 – 497.
- [GJ98] F. Girard and M. Jebrane, *Majorations affines due nombre de zéros d’intégrales abéliennes pour les hamiltoniens quartiques elliptiques*, Ann. Fac. Sci. Toulouse Math. (6) 7 (1998), no. 4, 671–685. MR 1 693 581
- [GK58] I. C. Gohberg and M. G. Kreĭn, *Systems of integral equations on the half-line with kernels depending on the difference of the arguments*, Uspehi Mat. Nauk (N.S.) 13 (1958), no. 2 (80), 3–72. MR 21#1506
- [GK60] by same author, *Systems of integral equations on a half line with kernels depending on the difference of arguments*, Amer. Math. Soc. Transl. (2) 14 (1960), 217–287. MR 22#3954
- [Glu00] A. Glutsuk, *An explicit formula for the determinant of the Abelian integral matrix*, ArXiv Preprint math.DS/0004040, April 2000.
- [Har82] P. Hartman, *Ordinary differential equations*, second (reprinted) ed., Birkhäuser, Boston, Mass., 1982.
- [Hei83] J. Heintz, *Definability and fast quantifier elimination in algebraically closed fields*, Theoret. Comput. Sci. 24 (1983), no. 3, 239–277. MR 85a:68062
- [HI98] E. Horozov and I. D. Iliev, *Linear estimate for the number of zeros of Abelian integrals with cubic Hamiltonians*, Nonlinearity 11 (1998), no. 6, 1521–1537. MR 99j:34036
- [Hil00] D. Hilbert, *Mathematical problems*, Bull. Amer. Math. Soc. (N.S.) 37 (2000), no. 4, 407–436, Reprinted from Bull. Amer. Math. Soc. 8 (1902), 437–479. MR 1 779 412
- [IK99] Yu. S. Ilyashenko and V. Yu. Kaloshin, *Bifurcation of planar and spatial polycycles: Arnold’s program and its development*, The Arnoldfest (Toronto, ON, 1997), Amer. Math. Soc., Providence, RI, 1999, pp. 241–271. MR 2001b:34064
- [Ili96] I. D. Iliev, *Higher-order Melnikov functions for degenerate cubic Hamiltonians*, Adv. Differential Equations 1 (1996), no. 4, 689–708. MR 97k:34039
- [Ily69] Yu. S. Ilyashenko, *Vozniknovenie predelp1nyh ciklov pri vozmuwenii uravneniya d w / d z = − R z / R w dw/dz=-R_{z}/R_{w}, gde R ⁡ ( z, w) R(z,w) —mnogochlen ( Appearance of limit cycles by perturbation of the equation d w / d z = − R z / R w dw/dz=-R_{z}/R_{w}, where R ⁡ ( z, w) R(z,w) is a polynomial)*, Mat. Sbornik (New Series) 78 (120) (1969), no. 3, 360–373.
- [Ily78] by same author, *The multiplicity of limit cycles arising by a perturbation of a Hamilton equation of the class d ​ w / d ​ z = P 2 / Q 1 dw/dz=P_{2}/Q_{1}, in real and complex domains.*, Tr. Semin. Im. I.G. Petrovskogo 3 (1978), 49–60 (Russian).
- [Ily91] by same author, *Finiteness theorems for limit cycles*, American Mathematical Society, Providence, RI, 1991. MR 92k:58221
- [IY95a] Yu. Ilyashenko and S. Yakovenko, *Double exponential estimate for the number of zeros of complete abelian integrals and rational envelopes of linear ordinary differential equations with an irreducible monodromy group*, Invent. Math. 121 (1995), no. 3, 613–650. MR 96g:58157
- [IY95b] by same author, *Finite cyclicity of elementary polycycles in generic families*, Concerning the Hilbert 16th problem, Amer. Math. Soc., Providence, RI, 1995, pp. 21–95. MR 96f:34042
- [IY96] by same author, *Counting real zeros of analytic functions satisfying linear ordinary differential equations*, J. Differential Equations 126 (1996), no. 1, 87–105. MR 97a:34010
- [Kho84] A. Khovanskii, *Real analytic manifolds with the property of finiteness, and complex abelian integrals*, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 40–50. MR 86a:32024
- [Kho91] by same author, *Fewnomials*, American Mathematical Society, Providence, RI, 1991. MR 92h:14039
- [Kho95] by same author, *On zeros of functions from polynomial envelopes*, Personal communication, 1995.
- [Kos92] V. P. Kostov, *Fuchsian linear systems on 𝐂 \mathbf{C} P 1 {P}^{1} and the Riemann-Hilbert problem*, C. R. Acad. Sci. Paris Sér. I Math. 315 (1992), no. 2, 143–148. MR 94a:34007
- [KS95] A. Kotova and V. Stanzo, *On few-parameter generic families of vector fields on the two-dimensional sphere*, Concerning the Hilbert 16th problem, Amer. Math. Soc., Providence, RI, 1995, pp. 155–201. MR 96i:34055
- [KY96] A. Khovanskii and S. Yakovenko, *Generalized Rolle theorem in 𝐑 \mathbf{R} n and 𝐂 \mathbf{C}*, J. Dynam. Control Systems 2 (1996), no. 1, 103–123. MR 97f:26016
- [Lev69] A. Ju. Levin, *The non-oscillation of solutions of the equation x ( n) + p 1 ​ ( t) ​ x ( n − 1) + ⋯ + p n ​ ( t) ​ x = 0 x^{(n)}+p_{1}(t)x^{(n-1)}+\cdots+p_{n}(t)x=0*, Uspehi Mat. Nauk 24 (1969), no. 2 (146), 43–96. MR 40 #7537
- [Loj91] S. Lojasiewicz, *Introduction to complex analytic geometry*, Birkhäuser Verlag, Basel, 1991, Translated from the Polish by Maciej Klimek. MR 92g:32002
- [Mar91] P. Mardešić, *An explicit bound for the multiplicity of zeros of generic Abelian integrals*, Nonlinearity 4 (1991), no. 3, 845–852. MR 92h:58163
- [MS91] G. Moreno Socías, *An Ackermannian polynomial ideal*, Applied algebra, algebraic algorithms and error-correcting codes (New Orleans, LA, 1991), Springer, Berlin, 1991, pp. 269–280. MR 94g:68056
- [MS92] by same author, *Length of polynomial ascending chains and primitive recursiveness*, Math. Scand. 71 (1992), no. 2, 181–205. MR 94d:13019
- [Nov01a] D. Novikov, *Modules of Abelian integrals and Picard–Fuchs systems*, ArXiv preprint math.DS/0110126, October 2001.
- [Nov01b] by same author, *Systems of linear ordinary differential equations with bounded coefficients may have very oscillating solutions*, Proc. Amer. Math. Soc. 129 (2001), no. 12, 3753–3755 (electronic). MR 1 860 513
- [NY95] D. Novikov and S. Yakovenko, *Simple exponential estimate for the number of real zeros of complete Abelian integrals*, Ann. Inst. Fourier (Grenoble) 45 (1995), no. 4, 897–927. MR 97b:14053
- [NY97] by same author, *Meandering of trajectories of polynomial vector fields in the affine n n -space*, Publ. Mat. 41 (1997), no. 1, 223–242. MR 98f:58160
- [NY99a] by same author, *Tangential Hilbert problem for perturbations of hyperelliptic Hamiltonian systems*, Electron. Res. Announc. Amer. Math. Soc. 5 (1999), 55–65 (electronic). MR 2000a:34065
- [NY99b] by same author, *Trajectories of polynomial vector fields and ascending chains of polynomial ideals*, Ann. Inst. Fourier (Grenoble) 49 (1999), no. 2, 563–609. MR 2001h:32054
- [NY01a] by same author, *Constrained-norm matrix factorization problem in the annulus*, in preparation, 2001.
- [NY01b] by same author, *Redundant Picard–Fuchs system for Abelian integrals*, J. Diff. Equations 177 (2001), no. 2, 267–306.
- [Pet86] G. S. Petrov, *Elliptic integrals and their nonoscillation*, Funktsional. Anal. i Prilozhen. 20 (1986), no. 1, 46–49, 96, (Russian). MR 87f:58031
- [Pet88] by same author, *The Chebyshev property of elliptic integrals*, Funktsional. Anal. i Prilozhen. 22 (1988), no. 1, 83–84. MR 89i:33002
- [Pet90] by same author, *Nonoscillation of elliptic integrals*, Funktsional. Anal. i Prilozhen. 24 (1990), no. 3, 45–50, 96. MR 92c:33036
- [Ple64] J. Plemelj, *Problems in the sense of Riemann and Klein*, Interscience Publishers John Wiley & Sons Inc. New York-London-Sydney, 1964, Interscience Tracts in Pure and Applied Mathematics, No. 16. MR 30#5008
- [Rou88] R. Roussarie, *A note on finite cyclicity property and Hilbert’s 16th problem*, Dynamical systems, Valparaiso 1986, Springer, Berlin, 1988, pp. 161–168. MR 90b:58227
- [Rou89] by same author, *Cyclicité finie des lacets et des points cuspidaux*, Nonlinearity 2 (1989), no. 1, 73–117. MR 90m:58169
- [Rou98] by same author, *Bifurcation of planar vector fields and Hilbert’s sixteenth problem*, Birkhäuser Verlag, Basel, 1998. MR 99k:58129
- [RY96] M. Roitman and S. Yakovenko, *On the number of zeros of analytic functions in a neighborhood of a Fuchsian singular point with real spectrum*, Math. Res. Lett. 3 (1996), no. 3, 359–371. MR 97d:34004
- [Var84] A. N. Varchenko, *Estimation of the number of zeros of an abelian integral depending on a parameter, and limit cycles*, Funktsional. Anal. i Prilozhen. 18 (1984), no. 2, 14–25. MR 85g:32033
- [Yak95] S. Yakovenko, *A geometric proof of the Bautin theorem*, Concerning the Hilbert 16th problem, Amer. Math. Soc., Providence, RI, 1995, pp. 203–219. MR 96j:34056
- [Yak99] by same author, *On functions and curves defined by ordinary differential equations*, Proceedings of the Arnoldfest (Ed. by E. Bierstone, B. Khesin, A. Khovanskii, J. Marsden), Fields Institute Communications, 1999, pp. 203–219. MR 2001k:34065
- [Yak00] by same author, *On zeros of functions from Bernstein classes*, Nonlinearity 13 (2000), no. 4, 1087–1094. MR 2001e:30008
- [Yom98] Y. Yomdin, *Oscillation of analytic curves*, Proc. Amer. Math. Soc. 126 (1998), no. 2, 357–364. MR 98d:32033

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto::%0A
[2]: /html/math/0104139
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/math/0104140
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+math/0104140
[8]: https://arxiv.org/pdf/math/0104140
[9]: /html/math/0104141
