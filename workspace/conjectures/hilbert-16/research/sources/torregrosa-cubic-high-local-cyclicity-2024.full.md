<!-- source: https://doi.org/10.1007/s40863-024-00486-9 | converted from HTML -->

Cubic planar vector fields with high local cyclicity | São Paulo Journal of Mathematical Sciences | Springer Nature Link

Skip to main content

# Cubic planar vector fields with high local cyclicity

- Stability and Bifurcation - Memorial Issue Dedicated to Jorge Sotomayor
- [Open access][1]
- Published: 28 December 2024

- Volume 19, article number 4 ( 2025)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[São Paulo Journal of Mathematical Sciences][5] [Aims and scope][6] [Submit manuscript][7]

Cubic planar vector fields with high local cyclicity

[Download PDF][2]

## Abstract

In this paper, we present two new one-parameter families of cubic systems exhibiting twelve small-amplitude limit cycles for exceptional parameter values.

### Similar content being viewed by others

### [Analytically Integrable Centers of Perturbations of Cubic Homogeneous Systems][8]

Article 22 April 2021

### [Explicit Formulas for Two Limit Cycles of a Family of Planar Differential Systems][9]

Article 01 April 2025

### **[Centroaffine T -Umbilical Hypersurfaces and Pseudo-Parallel Cubic Form][10]

Article 18 November 2023

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algebraic Geometry][11]
- [Dynamical Systems][12]
- [Element cycles][13]
- [Field Theory and Polynomials][14]
- [General Algebraic Systems][15]
- [Nonlinear Dynamics and Chaos Theory][16]
- [Dynamical Systems and Bifurcation Theory][17]

## 1 Introduction

From the seminal work “Mémoire sur les courbes définies par une équation différentielle” by Poinca ré, limit cycles (isolated periodic orbits) have been a central concept of study from the late 19th century to the present day. Poincaré initially presented this discovery primarily in the context of celestial mechanics, but it soon evolved into a comprehensive theory of planar autonomous systems. The exploration of limit cycles gained further momentum in the 1930 s through the contributions of van der Pol and Andronov’s school. They shown that limit cycles provided a valuable understanding of mathematical models for self-sustained oscillations in electrical circuits. This groundwork paved the way for the analysis of periodic phenomena modeled by differential equations across various scientific disciplines, establishing the theory as a cornerstone of applied mathematics. Among others, the works of Andronov, Lyapunov, and Poincaré inspired other research directions. It is reasonable to assert that the study of limit cycles was a pivotal milestone in the development of dynamical systems. While the theory has flourished within applied mathematics, it has also maintained a dedicated following in pure mathematics since its inception. This dual focus is largely influenced by the second part of Hilbert’s 16th problem, which inquires about the number and configuration of limit cycles for a planar autonomous polynomial system of degree \(N\). The problem remains unsolved even for \(N=2\).

A seemingly simpler task is the study of the number of limit cycles bifurcating from a monodromic equilibrium point. However, this is not the case, as, for example, the monodromy conditions are not fully understood. For instance, see [1, 2, 3, [4][18]], or the more recent works [[5][19], [6][20]], where the return map near a nilpotent monodromic equilibrium point is analyzed. From these references, it is natural to think that the easiest case arises when considering non-degenerate monodromic equilibrium points, that is, when the eigenvalues of the Jacobian matrix at the equilibrium point are complex with a nonvanishing imaginary part.

When we restrict the analysis to polynomial (or analytic) vector fields, the finiteness problem is not an issue due to the analyticity of the return map, which allows us to study the number of small amplitude limit cycles as the number of zeros of the displacement map. Although this problem appears simpler, there are relatively few works that provide a conclusive answer. Only few (complete with respect to the degree) families have been analyzed thoroughly; in particular the ones defined by quadratic or cubic vector fields having an equilibrium at the origin of center-focus type and homogeneous nonlinearities. The maximum number of limit cycles emerging from an equilibrium is known as the local cyclicity, which is the focus of the present work. The works of Bautin and Sibirskiĭ, [[7][21], [8][22]], provide exact values for the local cyclicity for the quadratic and cubic families respectively, when the nonlinearities are homogeneous and the equilibria are non-degenerate monodromic. They respectively prove that 3 and 5 limit cycles of small amplitude arise from an equilibrium using a degenerate Hopf bifurcation.

The cubic family is one of the most studied, and to date, the local cyclicity of the entire family is not fully understood. The aim of this work is to provide new evidence for the existence of twelve limit cycles bifurcating from an equilibrium. This is currently the highest lower bound for such a number. The usual method to obtain this lower bound is through the analysis of a degenerate Hopf point. In this paper, we will recall the main technique for addressing this after presenting the state of the art and our main results. In recent years, the best examples, from the perspective of the highest lower bound for the cyclicity, are obtained considering perturbations of specific centers. Therefore, it is necessary to have a mechanism to identify “good centers” or, alternatively, to have a comprehensive list of families for studying this problem. In all the studies presented to date, the simpler families exhibiting centers, such as Hamiltonian and reversible systems, are not sufficient to address this problem effectively. As we will see, we think that some Darboux centers are more interesting, in particular, the ones defined by the existence of a rational first integral. This is a challenging task because there are not many works offering complete studies, and the center problem for the cubic family is not fully solved.

To our knowledge, the first lists of cubic centers were conducted by Zoladek in [[9][23], [10][24]]. In the first work only reversible centers appear. In the second, the initial list was increased adding some Darboux centers. From these works, one can think that the higher number of limit cycles appearing with simpler bifurcation analysis will be the ones with the lowest number of free parameters. With this idea in mind, Zoladek stated in 1995 [[11][25]] the first result providing a system exhibiting, after perturbing inside the cubic complete class, eleven limit cycles of small amplitude. However, the proof has some gaps, as he explain in a subsequent work [[12][26]]. In it, he detailed that a higher-order analysis was necessary to obtain the announced lower bound. This issue was recently revisited in [[13][27], [14][28]], where it is shown that there exists cubic perturbations of such center exhibiting 11 limit cycles. But a higher-order analysis was necessary due to the family being much more degenerate than initially predicted. A simpler proof of this lower bound was provided in 2005 by Christopher [[15][29]] using another cubic system also appearing in [[10][24]] and labeled as \(CD_{31}^{12}\). Few years later, in 2008, Bondar and Sadovskiĭ [[16][30]] presented another cubic system yielding the same conclusion.

These systems are cubic perturbations of 1-parameter families of cubic centers, and only a first-order analysis is necessary to present a simpler proof of the existence of eleven limit cycles of small amplitude bifurcating from one equilibrium. For some specific values, the 1-parameter family \(CD_{31}^{12}\) presents a higher degeneracy, and twelve limit cycles of small amplitude can be obtained. This fact was discovered by Yu and Tian in [[17][31]]. The proof was not completed until [[18][32]], where an accurate analysis using singularity classification theory was employed. This phenomenon cannot be observed for the 1-parameter family discovered in [[16][30]], where only 11 limit cycles can bifurcate.

In this paper, we will present two new families where this specific bifurcation phenomenon occurs. For completeness, the previous results are also recovered. See [[18][32]] for more details. Almost all cubic systems presented in [[10][24]] labeled as codimension 12 were studied in [[13][27]]. A more elaborate analysis is necessary to guarantee that, generically, they exhibit 11 small limit cycles. This involves high-order Taylor developments and parallelization of the computations. For more details on this concept, see [[19][33]]. Although it is probably true that some of these families can exhibit specific parameter values such that twelve limit cycles also appear, the required analysis would be very difficult.

The main challenge in addressing the existence of center families with high local cyclicity lies in the unsolved center problem for the cubic family. One obstacle is the complexity of the algebraic systems to be solved, as described in [[20][34]]. Another challenge is the need to confine the analysis to real numbers, as the presence of more degenerate families is prevalent working with complex numbers. In [[21][35]], the existence of curves of weak-foci points in the complex plane with high-order is proved, including one of order 12 and another of order 13. These curves emerge after calculations in \(\mathbb {Z}\) modulo \(p\), ensuring the nearby presence of a complex curve. In this complex context, the most notable and simplified degenerate object was discovered by Sadovskiĭ, as shown in [[22][36]], where a system with a weak focus of order 14 is explicitly presented.

The technique used in this paper and developed in [[18][32]] was applied to prove that, to our knowledge, the best lower bound for the local cyclicity of a quartic planar vector field is 21. For higher values of the degree *N*, the reader is referred to [[13][27], [23][37]]. In the former, it is shown that the best lower bound for \(N=6\) is 48. In the latter, the best lower bounds for \(N=5,7,8,9\) are given as 33, 61, 76, and 88, respectively. However, in the last referenced works, due to computational difficulties, we have not analyzed the existence of exceptional parameter values for the center families.

Other works have explored vector fields of degree three and have shown the existence of more limit cycles, although not all within a single nest. Typically, a higher number of limit cycles appears when multiple nests are considered. Symmetric configurations of twelve limit cycles, in a \(6:6\) arrangement, are discussed in [[24][38], [25][39]]. The highest lower bound for the number of limit cycles in a global context for cubic systems was discovered in 2009 by Li, Liu, and Yang [[26][40]]. In that seminal work, thirteen limit cycles bifurcate from different level curves of a cubic Hamiltonian vector field. The bifurcation technique used is the so-called Poincaré–Poyntriaguin–Melnikov method; for more details, we refer the reader to [27, 28, [29][41]]. The configuration of these limit cycles is denoted as \((5:1|1:5)\) with an additional cycle surrounding all of them. Subsequent works confirming this lower bound were published in [30, 31, [32][42]]. For higher degrees, the reader is referred to [[33][43]].

The main tools used to find our new families are the Cremona transformations. These are birational transformations, which means they transform polynomial vector fields into polynomial vector fields, possibly after a time rescaling. Consequently, the degree is not always preserved. This idea was previously utilized in [[34][44]] to discover new quadratic vector fields with invariant algebraic curves of degrees different from those previously found. Birational transformations are commonly employed in Melnikov perturbation theory because the closed curves of the unperturbed systems are parametrized by rational functions, and in most cases, the integrals can be explicitly obtained. Although one might think that these transformations provide an equivalence in the projective plane, this is not the case in the affine plane. Thus, the local cyclicity can change even if the limit cycles are transformed from one system to another. For example, the local cyclicity of quadratic centers that linearize is one or two [[35][45]], but after a change of variables, the center becomes linear and, as mentioned, the cyclicity becomes three, see again [[7][21]]. This is because the perturbation changes from polynomial to rational or analytic, and therefore, the systems are not equivalent as quadratic vector fields.

The new two cubic families of centers with the highest local cyclicity found up to now are stated in the following.

### Theorem 1.1

Let \(\alpha\) be one of the only two real and simple solutions of

$$\begin{aligned} 315 \alpha ^{14}+4144 \alpha ^{12}+4425 \alpha ^{10}-9630 \alpha ^8+1485 \alpha ^6+5580 \alpha ^4-1713 \alpha ^2-510=0. \end{aligned}$$

Then, there exist polynomial perturbations of degree three of system

$$\begin{aligned} \begin{aligned} x'=&\, y+(\alpha ^2+3) x^2+\alpha (3 \alpha ^2+17) x y-2( \alpha ^2+3) y^2+\alpha (\alpha ^2+3) (3 \alpha ^2+1) x^3\\&+(13 \alpha ^2-1) (\alpha ^2+3) x^2 y-5 \alpha (\alpha ^2+3)^2 x y^2+(\alpha ^2+3)^2 y^3,\\ y'=&-x-\alpha (3 \alpha ^2+1) x^2+5(3 \alpha ^2+1) x y+2 \alpha (\alpha ^2-1) y^2\\ &+4 \alpha (\alpha ^2+3) (3 \alpha ^2+1) x^2 y-2 (7 \alpha ^2+1) (\alpha ^2+3) x y^2-2 \alpha (\alpha ^2-1) (\alpha ^2+3) y^3, \end{aligned} \end{aligned}$$

(1)

such that, twelve limit cycles of small amplitude bifurcate from the origin.

### Theorem 1.2

There exist only two values of \(\beta\) and polynomial perturbations of degree three of system

$$\begin{aligned} \begin{aligned} x'&=10 x (3+9 x-8 \beta y+6 x^2+12 y^2),\\ y'&=30 y-16 \beta x^2+105 x y-96 \beta y^2+24 \beta x^3+150 x^2 y+180 y^3, \end{aligned} \end{aligned}$$

(2)

such that, twelve limit cycles of small amplitude bifurcate from the equilibrium point located at

$$\begin{aligned} (x_0,y_0)=\left( \frac{32 \beta ^2-75}{6(8 \beta ^2+25)},\frac{35 \beta }{3(8 \beta ^2+25)}\right) . \end{aligned}$$

The paper is structured as follows: a first technical Sect. [2][46] with a short introduction about the degenerated Hopf bifurcation to provide lower bounds for the local cyclicity. The key point is based on an accurate analysis of the linear Taylor developments of the (Lyapunov) coefficients of the return map near monodromic non-degenerate equilibria when we perturb center families. In particular, the local cyclicity is, in general, non-constant for all parameter values of a fixed family. Section [3][47] is devoted to proving the main results, Theorems [1.1][48] and [1.2][49], and how the new centers with high cyclicity come from previously known families. We note that all the computations are made with a computer algebra system because the Lyapunov coefficients are polynomials with rational coefficients. No numerical analysis is employed throughout the full article. In fact, the values of \(\beta\) can be obtained as simple roots of a polynomial with rational coefficients and localized, by accurate Sturm analysis, in intervals with arbitrary precision.

## 2 Preliminaries

The Hopf bifurcation for planar differential equations is a well-known mechanism for studying the limit cycles that arise from an equilibrium of monodromic type, associated with a Jacobian matrix having purely imaginary eigenvalues. In this paper, we will analyze the degenerated case, where we obtain multiple limit cycles of small amplitude because the difference map has a zero of high multiplicity. More concretely, the usual way to study this bifurcation is for a planar perturbed system written as

$$\begin{aligned} \begin{aligned} x'&=\omega x-y+\sum \limits _{i\ge 2}P_i(x,y,\lambda ),\\ y'&=x+\omega y+\sum \limits _{i\ge 2}Q_i(x,y,\lambda ), \end{aligned} \end{aligned}$$

(3)

where \(P_i\) and \(Q_i\) are homogeneous polynomials of degree *i*in (*x*, *y*). The perturbation parameters \(\lambda\) are defined by the coefficients of \(P_i,Q_i\). In polar coordinates it writes as

$$\begin{aligned} \begin{aligned} r'&=\omega r+\sum \limits _{i\ge 2}r^i R_{i+1}(\theta ,\lambda ),\\ \theta '&=1+\sum \limits _{i\ge 1}r^i\Theta _{i+2}(\theta ,\lambda ), \end{aligned} \end{aligned}$$

where \(R_i\) and \(\Theta _i\) are homogeneous trigonometric polynomials of degree *i*. This differential equation can be transformed in a nonautonomous periodic differential equation of first order

$$\begin{aligned} \frac{dr}{d\theta }=\omega r+\sum \limits _{i\ge 2}r^i S_i(\theta ), \end{aligned}$$

(4)

being \(S_i\) trigonometric polynomials in the usual \(\sin \theta ,\cos \theta\) functions. Usually the *x*-axis is considered as the transversal section and, consequently, the initial condition is taken of the form \((\rho ,0).\) Hence, we can take the solution \(r(\theta ,\rho )\) of ( [4][50]) such that \(r(0,\rho )=\rho\) and write it as a power series in the initial condition \(\rho\),

$$\begin{aligned} r(\theta ,\rho )={{\,\textrm{e}\,}}^{\theta \omega }\rho +\sum \limits _{i\ge 2}r_i(\theta )\rho ^i. \end{aligned}$$

Using the return map, defined by the solution evaluated after one turn, that is at \(\theta =2\pi\), we introduce the difference map

$$\begin{aligned} \Delta (\rho )=({{\,\textrm{e}\,}}^{2\pi \omega }-1)\rho +\sum \limits _{i\ge 2}r_i(2\pi )\rho ^i. \end{aligned}$$

(5)

From this expression, it is clear that the stability of the origin is determined by the sign of the trace at the origin, denoted by \(\omega\). The origin is an attractor (resp. repellor) when \(\omega\) is negative (resp. positive). When \(\omega\) vanishes, we need to compute the first non-vanishing coefficient of the Taylor series of \(\Delta\) in ( [5][51]), which can be shown to always have an odd subscript \(2k+1\). We refer to this coefficient as the \(k\) -Lyapunov quantity, denoted by \(\hat{L}_k\). For consistency, we define \(L_0 = \omega\). See [[29][41], [36][52]] for further details.

Then, the periodic solutions of small amplitude can be analyzed by studying the number of zeros of the difference map. When all \({\hat{L}}_k\) vanish, we say that we have a center at the origin. Consequently, we can also consider \({\hat{L}}_k\) as the conditions for breaking a center. In fact, if the first non-vanishing \({\hat{L}}_k\) is negative, then we have a local Lyapunov function and the origin becomes stable.

An alternative or equivalent way to compute the coefficients \(L_k\) is by looking for the existence (or not) of a first integral in the Taylor series expansion. This involves searching for a formal solution of ( [3][53]) when \(\omega =0\), of the form

$$\begin{aligned} H(x,y)=x^2+y^2+\sum \limits _{i\ge 3}H_i(x,y) \end{aligned}$$

(6)

where \(H_i\) are homogeneous polynomials of degree *i*. In fact, such first integral does not exist in general, so we will look for a function *H*such that the Lie derivative with respect to ( [3][53]) writes, when \(\omega =0\), as

$$\begin{aligned} H'=\frac{\partial H}{\partial x} x'+\frac{\partial H}{\partial y} y'=\sum \limits _{k\ge 1} L_k(x^2+y^2)^{2k}. \end{aligned}$$

(7)

Both mechanisms are equivalent, and the coefficients \({\hat{L}}_k\) and \(L_k\) differ only by a non-vanishing constant. See [[37][54]] for more details.

In some cases, such as when the linear part of ( [3][53]) is not in the usual real Jordan normal form, we can adapt ( [6][55]) and ( [7][56]) by considering \(a_{20}x^2+a_{11}xy+a_{02}y^2\) as the first integral of the linear part instead of \(x^2+y^2\). Additionally, following [[15][29]], we can use any nonnegative polynomial of even degree that multiplies \(L_k\), such as \(x^{2k}\). All methods yield equivalent results, and we can choose the simplest one suited to our differential system. In this work, we computed \(L_k\) and referred to them as Lyapunov quantities.

In this paper we focus on the limit cycles of small amplitude that emerge from non degenerate centers of polynomial families of planar vector fields, \((x',y')=(P_c(x,y,\mu ),Q_c(x,y,\mu )),\) where the equilibrium point can be expressed as ( [3][53]) after a linear change of coordinates. As mentioned in the introduction, the number of limit cycles can vary with the parameter \(\mu\). We now recall a crucial result that provides the technique to prove our main results. Consider the perturbed system

$$\begin{aligned} \begin{aligned} x'&=P_c(x,y,\mu )+\omega x +\sum \limits _{i\ge 2}P_i(x,y,\lambda ),\\ y'&=Q_c(x,y,\mu )+\omega y +\sum \limits _{i\ge 2}Q_i(x,y,\lambda ), \end{aligned} \end{aligned}$$

(8)

where \(P_i\) and \(Q_i\) are homogeneous polynomials of degree *i*in (*x*, *y*) and \(P_i(x,y,0)=Q_i(x,y,0)=0\), for \(i,j\ge 2.\) We can use the above described algorithm for computing the Lyapunov quantities, \(L_k(\mu ,\lambda )\), for the perturbed system ( [8][57]) taking \(\omega =0\). These quantities are polynomials in \(\lambda\) and satisfy \(L_k(\mu ,0)=0.\) Thus, using the Implicit Function Theorem, we can perform a linear expansion with respect to \(\lambda\), denoting the terms by \(L_k^{[1]}(\mu ,\lambda )\), and provide a lower bound for the number of limit cycles. This approach, which appears in some previous works of Chicone and Jacobs [[38][58]] and of Han [[39][59]], was further elaborated by Christopher in [[15][29]] who utilized it to establish a higher lower bound for the local cyclicity of cubics, using first and second order developments. In essence, this method stipulates that fixing a generic value, \(\mu ,\) in the center variety, if the ordered set \(\{L_1^{[1]}(\mu ,\lambda ),L_2^{[1]}(\mu ,\lambda ),\ldots ,L_k^{[1]}(\mu ,\lambda )\}\) has rank *k*, after introducing the trace parameter \(\omega\), we can get *k*limit cycles of small amplitude bifurcating from the center. In certain special families, non-generic critical values of \(\mu\) exist, where the cyclicity can be increased considering the smallness of \(\mu\) relative to \(\lambda\). The following result deals with this special bifurcation degeneration.

### Proposition 2.1

[[13][27]] We denote by \(L_{j}^{[1]}(\lambda ,\mu )\) the first-order development, with respect to \(\lambda \in \mathbb {R}^{l},\) of the *j*-Lyapunov quantity of system ( [8][57]) when \(\omega =0\). We assume that, after a change of variables in the parameter space if necessary, we can write

$$\begin{aligned} W_j={\left\{ \begin{array}{ll} & \lambda _j + O_2(\lambda ), \text { for } j=1,\ldots ,k-1,\\ & \sum \limits _{l=1}^{k-1} g_{j,l}(\mu ) \lambda _l+f_{j-k}(\mu )\lambda _{k}+ O_2(\lambda ), \text { for } j=k,\ldots ,k+\ell , \end{array}\right. } \end{aligned}$$

where with \(O_2(\lambda )\) we denote all the monomials of degree higher or equal than 2 in \(\lambda\) with coefficients analytic functions in \(\mu\). If there exists a point \(\mu ^*\) such that \(f_0(\mu ^*)=\cdots =f_{\ell -1}(\mu ^*)=0,\) \(f_{\ell }(\mu ^*)\ne 0,\) and the Jacobian matrix of \((f_{0},\ldots ,f_{\ell -1})\) with respect to \(\mu\) has rank \(\ell\) at \(\mu ^*,\) then system ( [8][57]) has \(k+\ell\) hyperbolic limit cycles of small amplitude bifurcating from the origin.

The above result can be thought as that, in fact, we are computing the second order developments of \(L_k\) of ( [8][57]) at \(\mu ^*\). This phenomenon appears in the singularities unfolding analysis, because we are studying the transversal (after blowing up if necessary) local intersection of varieties, that is the solution of \(\{L_1=L_2=\cdots =L_k=0\}.\) The main obstruction here is that we have chosen the development of \(\lambda\) near generic \(\mu\) instead of considering \((\lambda ,\mu )\) as parameters. As we will see the difficulties in the computations are due to the fact that the critical values are not obtained explicitly. This can be easily visualized in [[40][60]] where the critical value is a rational number. The reader can think that this phenomenon only appears in high degree systems, but it is also present in the quadratic reversible family, as it is recently proved in [[27][61]].

## 3 Proofs of the main results

This section is devoted to proving the two main results presented in the introduction. For completeness and to clarify how the unperturbed systems were obtained, we will present two previous systems with centers and how the new ones were derived. These systems, with only one satisfying conditions similar to those presented in the introduction, exhibit the same lower bound for the local cyclicity. This has also been detailed in the introduction. The proofs are based on a precise application of the Implicit Function Theorem, commonly used in the analysis of singularities in Algebraic Geometry. As we have already mentioned, this method was first well used and described in [[18][32]]. In the following, we closely follow the scheme provided in [[18][32]]. For completeness, we present a complete proof instead of directly using Proposition [2.1][62].

### Proof of Theorem 1.1

The origin of system ( [1][63]) is a center, having a first integral of Darboux type. More precisely, the following rational function

$$\begin{aligned} H(x,y)=\dfrac{f_1(x,y)[(\alpha ^2+3)(3\alpha x-y)+1]^2}{[f_2(x,y)]^3f_3(x,y)}, \end{aligned}$$

(9)

where

$$\begin{aligned} \begin{aligned} f_1(x,y)=&\,(3 \alpha ^2+1)[4 \alpha ^2 (\alpha ^2+3) (3 \alpha ^2+1) x^2 y-32 \alpha ^3 (\alpha ^2+3) x y^2+4 \alpha ^2 (\alpha ^2+3)^2 y^3\\&-\alpha ^2 (3 \alpha ^2+1) x^2+2 \alpha (11 \alpha ^2+9) x y-9 (3 \alpha ^2+1) y^2-2 \alpha x+6 y]-1,\\ f_2(x,y)=&\,\alpha ^2 (\alpha ^2+3)[ (3 \alpha ^2+1) x^2-8 \alpha x y+(\alpha ^2+3) y^2]+4 \alpha (\alpha ^2+1) x\\&-2(3 \alpha ^2+1) y+1,\\ f_3(x,y)=&\,(\alpha ^2+3) [(3 \alpha ^2+1) x^2-8 \alpha x y+(\alpha ^2+3) y^2-2 y]+8 \alpha x+1. \end{aligned} \end{aligned}$$

The perturbation parameters are ordered as

$$\begin{aligned} \lambda =(a_{20},a_{11},a_{02},a_{30},a_{21},a_{12},a_{03},b_{11},b_{02},b_{03},b_{20},b_{30},b_{21},b_{12}). \end{aligned}$$

We start obtaining the linear parts of the first 12 Lyapunov quantities using the algorithm detailed in Sect. [2][46]. Straightforward computations show that the linear parts of the first 10 Lyapunov quantities are linearly independent with respect to the first 10 coordinates of \(\lambda\), the Implicit Function Theorem allows us to express them, in a neighborhood of the origin of the parameters space, as \(L_i = u_i\) for \(i = 1, \ldots , 10\), being \((u_1, \ldots , u_{10}, b_{20}, b_{30}, b_{21}, b_{12})\) the new parameters. By restricting the computation of the next two Lyapunov quantities under the vanishing condition \((u_1, \ldots , u_{10}) = 0\), we get

$$\begin{aligned} \begin{aligned} L_{11}^{[1]}&=\frac{1048576}{7429}\frac{\alpha ^{11} (3 \alpha ^2+1)^7 (\alpha ^2+3)^8 (\alpha ^2-1)^{11} }{G(\alpha )} F_{11}(\alpha )U_{11},\\ L_{12}^{[1]}&=-\frac{2097152}{557175}\frac{\alpha ^{11}(3\alpha ^2+1)^7(\alpha ^2+3)^8(\alpha ^2-1)^{11}}{G(\alpha )}F_{12}(\alpha )U_{11}, \end{aligned} \end{aligned}$$

(10)

being \(F_{11}(\alpha )\) the polynomial of degree 14 in the statement and

$$\begin{aligned} \begin{aligned} F_{12}(\alpha )=&\,5368860 \alpha ^{20}+103903345 \alpha ^{18}+563207724 \alpha ^{16}+959461452 \alpha ^{14}\\&-278311344 \alpha ^{12}-1253097450 \alpha ^{10}+759337440 \alpha ^8+697600812 \alpha ^6\\&-303800364 \alpha ^4-86992767 \alpha ^2-1906380,\\ G(\alpha )=&\,124960563 \alpha ^{34}+4933223190 \alpha ^{32}+66458793852 \alpha ^{30}\\&+270672319320 \alpha ^{28}+131714469744 \alpha ^{26}-741905829192 \alpha ^{24}\\&+664449714700 \alpha ^{22}+1877961589672 \alpha ^{20}+203589288270 \alpha ^{18}\\&-124073192476 \alpha ^{16}+1960162856052 \alpha ^{14}-556573973592 \alpha ^{12}\\&+174415427592 \alpha ^{10}-32697898056 \alpha ^8+8809519236 \alpha ^6\\&+239029080 \alpha ^4+128307591 \alpha ^2+11633814,\\ U_{11}=&\,12 \alpha (21 \alpha ^4+2 \alpha ^2+1) (\alpha ^2+3)^2 b_{20}+3 \alpha ^2 (3 \alpha ^2+1) (3 \alpha ^4+26 \alpha ^2+3) b_{12}\\&+(75 \alpha ^8+506 \alpha ^6+232 \alpha ^4-14 \alpha ^2-15) b_{30}\\&+3 \alpha (21 \alpha ^6+125 \alpha ^4+27 \alpha ^2+3)b_{21}. \end{aligned} \end{aligned}$$

It is straightforward to check, using Sturm theory, that \(F_{11}\) has only two real roots, denoted by \(\alpha _\pm\). Moreover, computing the resultant with respect to its derivative with respect to \(\alpha\), both are simple. Additionally, \(F_{12}\) and \(G\) do not vanish at these roots. This can be easily verified by computing their respective resultants with \(F_{11}\) with respect to \(\alpha\), which are non-zero integer numbers. The specific values of such simple roots are not necessary to be obtained, only its existence is enough for proving the result.

For the last step we need to consider the perturbation restricted, for example, to \(b_{12}=b_{30}=b_{12}=0\) and denoting \(u_{11}=b_{20}\). Then, from ( [10][64]) we can write

$$\begin{aligned} \begin{aligned} L_{11}(u_{11},\alpha )&=G_{11}(\alpha )u_{11}F_{11}(\alpha )+O_2(u_{11}),\\ L_{12}(u_{11},\alpha )&=G_{12}(\alpha )u_{11}F_{12}(\alpha )+O_2(u_{11}). \end{aligned} \end{aligned}$$

(11)

We remark that we have not indicated the dependence on \(\alpha\) for the higher order terms \(O_2(u_{11})\) because the relevant part is that they are analytic but starting with degree two in \(u_{11}.\) After translating \((\alpha _{+}, 0)\) to the origin by setting \(\alpha = \alpha _{+} + u_{12}\), the Taylor series of the above expressions near the origin write as

$$\begin{aligned} \begin{aligned} L_{11}(u_{11}, u_{12})&= \gamma _{11} u_{11} (u_{12} + O_2(u_{11}, u_{12})), \\ L_{12}(u_{11}, u_{12})&= \gamma _{12} u_{11} (1 + O_2(u_{11}, u_{12})), \end{aligned} \end{aligned}$$

for some non-vanishing real numbers \(\gamma _{11}\) and \(\gamma _{12}\). Finally, the Implicit Function Theorem guarantees that we can find a curve \(u_{12}=\varphi (u_{11})\) such that \(L_{11} = 0\) but \(L_{12} \ne 0\). Hence, we have proved the existence of a curve in the parameter space of weak foci of order 12, which, after adding the trace parameter, unfolds 12 limit cycles of small amplitude, and the proof is complete. Clearly, the same is valid at \((\alpha _{-}, 0)\). \(\square\)

### Remark 3.1

We observe that, since the linear parts of the last two Lyapunov quantities depend on four parameters, an accurate analysis is necessary to ensure that the complete \(L_{11}\) vanishes. It is not at all clear that the proof could be completed without considering the restriction to the variety \(b_{12} = b_{30} = b_{21} = 0\), because the second-order terms of ( [11][65]), which are analytic in all parameters, must depend on only one variable to be factored out in order to apply the usual Implicit Function Theorem.

Before proving the second main theorem of this paper, we recall a result that allows us to discover the existence of the cubic vector field ( [1][63]). For completeness and in order to understand better the differences between both cubic vector fields, we will add an sketch of the proof which follows closely the one provided for Theorem [1.1][48]. We will see why this new vector field unfolds 12 limit cycles of small amplitude, unlike the one provided by Bondar and Sadovskiĭ.

### Proposition 3.2

[[16][30]] For each \(\alpha\), there exist cubic perturbations such that the vector field

$$\begin{aligned} \begin{aligned} x'=&\,y-2 \alpha (3 \alpha ^2+5) xy+(\alpha ^2+3) (3 \alpha ^2+1)^2 x^2y,\\ y'=&-x+\alpha (3 \alpha ^2+17) x^2+4(3 \alpha ^2-1) x y-\alpha (\alpha ^2+11) y^2\\&-(\alpha ^2+3)\big (24 \alpha ^2 x^3+2 \alpha (15 \alpha ^2-7) x^2 y- (3 \alpha ^4+22 \alpha ^2-1) x y^2-2 \alpha (\alpha ^2-1) y^3\big ), \end{aligned} \end{aligned}$$

(12)

has eleven limit cycles of small amplitude bifurcating from the origin.

### Proof

We will only detail the differences with the proof of Theorem [1.1][48]. System ( [12][66]) has a center at the origin because it is Darboux integrable using the rational first integral

$$\begin{aligned} H(x,y)= \dfrac{[( \alpha ^2 +3 )(3\alpha x-y)-1]^3f_1(x,y)}{ [ (\alpha ^2+3)(3\alpha ^2+1)^2x^2-2(3 \alpha ^2+5 )\alpha x+1][f_2(x,y)]^3}, \end{aligned}$$

(13)

where

$$\begin{aligned} \begin{aligned} f_1(x,y)=&\, 12(\alpha ^2+3)\alpha \big [16 \alpha ^2 x^3+8 (3 \alpha ^2-1) \alpha x^2 y+ (\alpha ^2-1) (9 \alpha ^2-1) x y^2\\&+ (\alpha ^2-1)^2 \alpha y^3\big ] -16 (3 \alpha ^2+13) \alpha ^2 x^2-12 (3 \alpha ^4+18 \alpha ^2-5) \alpha x y\\&-48 (\alpha ^2-1) \alpha ^2 y^2+(3 \alpha ^2+25) \alpha x+3(5 \alpha ^2-1) y-1,\\ f_2(x,y)=&\, (\alpha ^2+3)\big [16 \alpha ^2 x^2+8 (\alpha ^2-1) \alpha x y+ (\alpha ^2-1)^2 y^2\big ]\\&-2 (\alpha ^2+7) \alpha x-4 (\alpha ^2-1) y+1. \end{aligned} \end{aligned}$$

Using the Implicit Function Theorem we can write the first 10 Lyapunov quantities as new parameters obtaining \(L_i=u_i\) for \(i=1,\ldots ,10\) changing the perturbation parameters by \(\{a_{20},_{a11},a_{02},a_{30},a_{21},a_{12},a_{03},b_{11},b_{02},b_{03}\}\) the parameters that remain are again \(\{b_{20},b_{30},b_{21},b_{12}\}\) which appear in the expression *U*of the following Lyapunov quantity, which linear Taylor development writes as

$$\begin{aligned} L_{11}^{[1]}=-\frac{188743680}{52003} \frac{ \alpha ^{11} ( \alpha ^2+3)^8 (3 \alpha ^2+1)^8 ( \alpha ^2-1)^{11}}{G(\alpha )}F_{11}(\alpha )U_{11},\\ \end{aligned}$$

where

$$\begin{aligned} \begin{aligned} F_{11}(\alpha )=&\, 63 \alpha ^{12}+868 \alpha ^{10}+1407 \alpha ^8-1232 \alpha ^6-803 \alpha ^4+588 \alpha ^2+133,\\ G(\alpha )=&\, 31067946819 \alpha ^{34}+941881265856 \alpha ^{32}+10931182143840 \alpha ^{30}\\ &+33831496469880 \alpha ^{28}-83205933249492 \alpha ^{26}-100165976291592 \alpha ^{24}\\ &-100791559275408 \alpha ^{22}+61653376741080 \alpha ^{20}+44269968690378 \alpha ^{18}\\ &-264767150547368 \alpha ^{16}+341738613732928 \alpha ^{14}+19116783617384 \alpha ^{12}\\ &-25511606325924 \alpha ^{10}+5729233769704 \alpha ^8+394479066224 \alpha ^6\\ &+126858994760 \alpha ^4+14151148011 \alpha ^2+355946760,\\ U_{11}=&\, 4 \alpha (189 \alpha ^6+3147 \alpha ^4-917 \alpha ^2+13)( \alpha ^2+3)^2b_{20}\\ &-(639 \alpha ^8-8038 \alpha ^6-9040 \alpha ^4+4486 \alpha ^2-15)b_{30}\\ &+2 \alpha (549 \alpha ^6-431 \alpha ^4+15 \alpha ^2-69)b_{21}\\ &-2 \alpha ^2(189 \alpha ^6+465 \alpha ^4+943 \alpha ^2+483)b_{12}. \end{aligned} \end{aligned}$$

As \(F_{11}\) is non vanishing because it has no real roots, adding the trace parameter, the unfolding of 11 limit cycles of small amplitude is guaranteed and the proof follows. We remark that, as in the previous proof, the function ( [6][55]) can be computed directly starting as \(x^2+y^2\). \(\square\)

We remark that as \(F_{11}\) has no real roots, we can not use the next Lyapunov quantity, as in the proof of the first main theorem, to provide the existence of a curve of weak-foci of order 12. Even thought, we could compute it and write the linear Taylor development as

$$\begin{aligned} \begin{aligned} L_{12}^{[1]}=&\frac{12582912}{260015} \frac{ \alpha ^{11} ( \alpha ^2+3)^8 (3 \alpha ^2+1)^8 ( \alpha ^2-1)^{11}}{G(\alpha )} F_{12}(\alpha )U_{11},\\ F_{12}(\alpha )=&\, 3268503 \alpha ^{18}+65020277 \alpha ^{16}+378210168 \alpha ^{14}\\&+792055208 \alpha ^{12}+231304910 \alpha ^{10}-804545046 \alpha ^8\\ &-185976160 \alpha ^6+319040736 \alpha ^4+63104643 \alpha ^2+85785. \end{aligned} \end{aligned}$$

Of course, we could say that using complex values we have such curve of higher (complex) cyclicity. As we are only interested in real unfolding phenomena, we have to discard this example. But, as we have commented, following an idea of Cremona transformations appearing in [[34][44]] we have found system ( [1][63]).

It is clear, from the expression of the first integral ( [13][67]), that system ( [12][66]) has the invariant straight line \(( \alpha ^2 +3 )(3\alpha x- y)-1=0.\) Then, we will do the birational change of coordinates

$$\begin{aligned} (x,y)\rightarrow \left( \frac{x}{(\alpha ^2+3)(3\alpha x-y)+1},\frac{y}{(\alpha ^2+3)(3\alpha x-y)+1}\right) . \end{aligned}$$

to put it at the new infinity. We also notice that ( [12][66]) has two more invariant straight lines but, as they are complex, we can not use them for, via a Cremona birational transformation, providing more cubic examples.

The system in the following result was introduced by Zoladek in [[10][24]], and Christopher in [[15][29]] demonstrated that for a particular value of \(\alpha\), eleven small-amplitude limit cycles bifurcate from an equilibrium point in a degenerate Hopf bifurcation using linear expansions of the Lyapunov quantities, as indicated in ( [13][67]). The existence of twelve limit cycles was first reported in [[25][39]]. The original proof was not enough detailed and was recently clarified in [[18][32]].

### Proposition 3.3

[[18][32]] There exist values of \(\beta\) and cubic perturbations for system

$$\begin{aligned} \begin{aligned} x'=&\,10 x(6+9 x+3 x^2-8 \beta x y+12 y^2),\\ y'=&-24 \beta +16 \beta x-90 y-15 x y+16 \beta x y^2-60 y^3, \end{aligned} \end{aligned}$$

such that 12 limit cycles of small amplitude bifurcate from

$$\begin{aligned} (x_0,y_0)=\left( \frac{6 (8 \beta ^2+25)}{32 \beta ^2-75},\frac{70 \beta }{32 \beta ^2-75}\right) . \end{aligned}$$

### Proof

The proof follows closely the previous proofs. Hence, we will only detail the expressions for the first integral *H*and the polynomials of the numerators and denominators of \(L_{11}^{[1]}\) and \(L_{12}^{[1]}\). They write as

$$\begin{aligned} H(x,y)=\frac{(xy^2+x+1)^5}{x^3(8xy^5+20xy^3+20y^3+15xy+30y+8\beta )^2} \end{aligned}$$

(14)

and

$$\begin{aligned} \begin{aligned} L_{11}^{[1]}&=\frac{(32\beta ^2-75)^{30}}{\beta ^{13} (4\beta ^2-5)^{12}(8\beta ^2+25)^{12}G_1(\beta )} {F}_{11}(\beta )U_{11},\\ L_{12}^{[1]}&=\frac{(32\beta ^2-75)^{32}}{\beta ^{17} (4\beta ^2-5)^{16}(8\beta ^2+25)^{14}G_1(\beta )G_2(\beta )G_3(\beta )}{F}_{12}(\beta ) U_{11},\\ U_{11}&=56\beta b_{30}+15 b_{21}, \end{aligned} \end{aligned}$$

where \(F_{11},\) \(F_{12},\) and \(G_1\) are polynomials with integer coefficients of degree 26, 37, and 28 in \(\beta ^2\), respectively. The remaining two polynomials are \(G_2(\beta )=8192\beta ^4-16000\beta ^2+84375\) and \(G_3(\beta )=16384\beta ^6-14400\beta ^4+165000\beta ^2+84375.\) Using an accurate Sturm analysis and straightforward computations, the reader can check that the polynomial \(F_{11}\) has exactly six simple roots, \(\{\pm \beta _{1}, \pm \beta _2\) \(\pm \beta _3\},\) where \(F_{12},G_1,G_2,\) and \(G_3\) do not vanish. The nonvanishing conditions, adding also the first derivative of \(F_{11}\) for proving that the roots are simple, can be checked by computing their resultants with \(F_{11}\) with respect to \(\beta\). Although it is not relevant in the proof, the reader can found in [[18][32]] that the six simple roots of \(F_{11}\) are approximately \(\pm 2.020, \pm 7.444,\) and \(\pm 15.626.\) \(\square\)

### Remark 3.4

It is important to mention that, after translation of the equilibrium point \((x_0,y_0)\) to the origin, the computation of the Lyapunov quantities is simpler if we write ( [6][55]) using the first integral of the linear terms of the translated one:

$$\begin{aligned} \frac{ \beta (8192 \beta ^4-16000 \beta ^2+84375)}{2880(8 \beta ^2+25)}x^2-\frac{960 \beta ^2+13500}{2880}xy+ \beta (4 \beta ^2-5) y^2. \end{aligned}$$

That is, without doing the transformation to the Jordan normal form.

We finish proving the second main result of this paper.

### Proof of Theorem 1.2

As previously, we will closely follow the steps of the proof of Theorem [1.1][48], detailing only the main differences. System ( [2][68]) has the following rational first integral:

$$\begin{aligned} H(x,y)=\frac{(x^3+x^2+y^2)^5}{(8\beta x^6+30x^5y+20x^3y^3+15x^4y+20x^2y^3+8y^5)^2}. \end{aligned}$$

(15)

By using the Implicit Function Theorem to ensure that the first ten Lyapunov quantities vanish, due to the linear independence of the linear developments, we obtain the following two linear parts of the Lyapunov quantities:

$$\begin{aligned} \begin{aligned} L_{11}^{[1]}&=\frac{(8\beta ^2+25)^{29}}{\beta ^{12}(4\beta ^2-5)^{12}(32\beta ^2-75)^{12}G_1(\beta )} F_{11}(\beta )U_{11},\\ L_{12}^{[1]}&=\frac{(8\beta ^2+25)^{31}}{\beta ^{16}(4\beta ^2-5)^{16}(32\beta ^2-75)^{14}G_1(\beta )G_2(\beta )[G_3(\beta )]^2} F_{12}(\beta )U_{11}, \end{aligned} \end{aligned}$$

where \(F_{11}\), \(F_{12}\), and \(G_1\) are polynomials with integer coefficients of degrees 35, 40, and 35 in \(\beta ^2\), having no common roots. Using Sturm analysis and computing resultants with respect to \(\beta ,\) it is not difficult to check that the polynomial \(F_{11}\) has exactly two simple real roots which are not roots of \(F_{12}\) or \(G_1.\) The polynomials \(G_2(\beta )=16384\beta ^6-14400\beta ^4+165000\beta ^2+84375\) and \(G_3(\beta )=2048\beta ^4+53400\beta ^2+24375\) have no real roots. The polynomial \(U_{11}\) is a linear combination of the remaining parameters \(\{b_{20},b_{30},b_{21},b_{12}\}\) being the coefficients also polynomials with rational coefficients in \(\beta ^2.\)

Although it is not relevant in the proof, the two simple roots of \(F_{11}\) are approximately \(\beta _{\pm }\approx \pm 1.3352\), \(\square\)

Due to the size of the expressions we have not added here the polynomials appearing in the above proofs. As in Remark [3.4][69], the computations for obtaining the Lyapunov quantities in the last proof are simpler if we use directly

$$\begin{aligned} \frac{\beta (2048 \beta ^4+53400 \beta ^2+24375)}{2(32 \beta ^2-75)} x^2-5(136\beta ^2+75) y x+40 \beta (4 \beta ^2-5) y^2 \end{aligned}$$

in ( [6][55]) as the first integral of linear terms of the translated system using the equilibrium point \((x_0,y_0)\) given in the statement.

The last comment is devoted to show how we can obtain ( [15][70]) from ( [14][71]). We only need to do the birational change \((x,y)\rightarrow (y/x,1/x)\) that moves the invariant straight line \(x=0\) to infinity. This is also a Cremona map, much simpler than the one presented before to get from ( [13][67]) to ( [9][72]).

## References

1.

Álvarez, M.J., Gasull, A.: Monodromy and stability for nilpotent critical points. Internat. J. Bifur. Chaos. Appl. Sci. Eng. **15**(4), 1253–1265 (2005)

[Article][73] [MathSciNet][74] [Google Scholar][75]

2.

García, I.A., Giné, J., Grau, M.: A necessary condition in the monodromy problem for analytic differential equations on the plane. J. Symbolic Comput. **41**(9), 943–958 (2006)

[Article][76] [MathSciNet][77] [Google Scholar][78]

3.

Gasull, A., Llibre, J., Mañosa, V., Mañosas, F.: The focus-centre problem for a type of degenerate system. Nonlinearity **13**(3), 699–729 (2000)

[Article][79] [MathSciNet][80] [Google Scholar][81]

4.

Medvedeva, N.B., Mazaeva, E.V.: A sufficient focus condition for a monodromic singular point. Tr. Mosk. Mat. Obs. **63**, 87–114 (2002)

[MathSciNet][82] [Google Scholar][83]

5.

García, I.A., Giné, J.: The Poincaré map of degenerate monodromic singularities with Puiseux inverse integrating factor. Adv. Nonlinear Anal. **12**(1), 20220314 (2023)

[Article][84] [Google Scholar][85]

6.

García, I.A., Giné, J.: The linear term of the Poincaré map at singularities of planar vector fields. J. Differ. Equ. **396**, 44–67 (2024)

[Article][86] [Google Scholar][87]

7.

Bautin, N.N.: On the number of limit cycles which appear with the variation of coefficients from an equilibrium position of focus or center type. Amer. Math. Soc. Trans. **1954**(100), 19 (1954)

[MathSciNet][88] [Google Scholar][89]

8.

Sibirskiĭ, K.S.: On the number of limit cycles in the neighborhood of a singular point. Differ. Uravnenija **1**, 53–66 (1965)

[MathSciNet][90] [Google Scholar][91]

9.

Zoladek, H.: The classification of reversible cubic systems with center. Topol. Methods Nonlinear Anal. **4**(1), 79–136 (1994)

[Article][92] [MathSciNet][93] [Google Scholar][94]

10.

Zoladek, H.: Remarks on: the classification of reversible cubic systems with center. Topol. Methods Nonlinear Anal. **8**(2), 335–342 (1996)

[Article][95] [MathSciNet][96] [Google Scholar][97]

11.

Zoladek, H.: Eleven small limit cycles in a cubic vector field. Nonlinearity **8**(5), 843–860 (1995)

[Article][98] [MathSciNet][99] [Google Scholar][100]

12.

Zoladek, H.: The CD45 case revisited. In: Toni, B. (ed.) Mathematical Sciences with Multidisciplinary Applications, pp. 596–625. Springer International Publishing, Cham (2016)

[Google Scholar][101]

13.

Gouveia, L.F.S., Torregrosa, J.: Lower bounds for the local cyclicity of centers using high order developments and parallelization. J. Differ. Equ. **271**, 447–479 (2021)

[Article][102] [MathSciNet][103] [Google Scholar][104]

14.

Tian, Y., Yu, P.: Bifurcation of small limit cycles in cubic integrable systems using higher-order analysis. J. Differ. Equ. **264**(9), 5950–5976 (2018)

[Article][105] [MathSciNet][106] [Google Scholar][107]

15.

Christopher, C.: Estimating limit cycle bifurcations from centers. In: Differential Equations with Symbolic Computation, Trends in Mathematics, 23–35, Birkhäuser, Basel (2005)

16.

Bondar, Y.L., Sadovskiĭ, A.P.: On a theorem of Zoladek. Differ. Uravn. **44**(2), 263–265 (2008)

[MathSciNet][108] [Google Scholar][109]

17.

Yu, P., Tian, Y.: Twelve limit cycles around a singular point in a planar cubic-degree polynomial system. Commun. Nonlinear Sci. Numer. Simul. **19**(8), 2690–2705 (2014)

[Article][110] [MathSciNet][111] [Google Scholar][112]

18.

Giné, J., Gouveia, L.F.S., Torregrosa, J.: Lower bounds for the local cyclicity for families of centers. J. Differential Equations **275**, 309–331 (2021)

[Article][113] [MathSciNet][114] [Google Scholar][115]

19.

Liang, H., Torregrosa, J.: Parallelization of the Lyapunov constants and cyclicity for centers of planar polynomial vector fields. J. Differ. Equ. **259**(11), 6494–6509 (2015)

[Article][116] [MathSciNet][117] [Google Scholar][118]

20.

Sánchez-Sánchez, I., Torregrosa, J.: New advances on the Lyapunov constants of some families of planar differential systems. In: Extended Abstracts Spring 2018—Singularly Perturbed Systems, Mmultiscale Phenomena and Hysteresis: Theory and Applications, vol. 11, CRM Barc., p. 161–167. Birkhäuser/Springer, Cham (2019)

21.

Graf, H.C., Kröker, J.: Focal values of plane cubic centers. Qual. Theory Dyn. Syst. **9**(1–2), 319–324 (2010)

[Article][119] [MathSciNet][120] [Google Scholar][121]

22.

Sadovskiĭ, A.P.: Existence of complex cubic systems with a 14th-order focus. Differ. Equ. **56**(1), 140–142 (2020)

[Article][122] [MathSciNet][123] [Google Scholar][124]

23.

Bastos, J.L.R., Buzzi, C.A., Torregrosa, J.: Orbitally symmetric systems with applications to planar centers. Commun. Pure Appl. Anal. **20**(10), 3319–3347 (2021)

[Article][125] [MathSciNet][126] [Google Scholar][127]

24.

Li, J., Liu, Y.: New results on the study of \(Z_q\) -equivariant planar polynomial vector fields. Qual. Theory Dyn. Syst. **9**(1–2), 167–219 (2010)

[Article][128] [MathSciNet][129] [Google Scholar][130]

25.

Yu, P., Han, M.: Twelve limit cycles in a cubic case of the 16th Hilbert problem. Internat. J. Bifur. Chaos. Appl. Sci. Eng. **15**(7), 2191–2205 (2005)

[Article][131] [MathSciNet][132] [Google Scholar][133]

26.

Li, C., Liu, C., Yang, J.: A cubic system with thirteen limit cycles. J. Differ. Equ. **246**(9), 3609–3619 (2009)

[Article][134] [MathSciNet][135] [Google Scholar][136]

27.

Christopher, C., Li, C., Torregrosa, J.: Limit cycles of differential equations, 2nd edn. Advanced Courses in Mathematics. CRM Barcelona. Birkhäuser/Springer, Cham (2024)

28.

Han, M.: Bifurcation theory of limit cycles of planar systems. In: Canada, A., DrÁbek, P., Fonda, A. (eds.) Handbook of differential equations: ordinary differential equations, vol. III, pp. 341–433. Elsevier/North-Holland, Amsterdam (2006)

[Google Scholar][137]

29.

Roussarie, R.: Bifurcation of planar vector fields and Hilbert’s sixteenth problem. Progress in Mathematics, 164, Birkhäuser Verlag, Basel (1998)

30.

Liu, Y., Li, J.: \(Z_2\) -equivariant cubic system which yields 13 limit cycles. Acta Math. Appl. Sin. Engl. Ser. **30**(3), 781–800 (2014)

[Article][138] [MathSciNet][139] [Google Scholar][140]

31.

Yang, J., Han, M., Li, J., Yu, P.: Existence conditions of thirteen limit cycles in a cubic system. Internat. J. Bifur. Chaos. Appl. Sci. Eng. **20**(8), 2569–2577 (2010)

[Article][141] [MathSciNet][142] [Google Scholar][143]

32.

Zhao, L.Q.: A new configuration of thirteen limit cycles for a cubic system. Beijing Shifan Daxue Xuebao **48**(3), 231–234 (2012)

[MathSciNet][144] [Google Scholar][145]

33.

Prohens, R., Torregrosa, J.: New lower bounds for the Hilbert numbers using reversible centers. Nonlinearity **32**(1), 331–355 (2019)

[Article][146] [MathSciNet][147] [Google Scholar][148]

34.

Alberich-Carramiñana, M., Ferragut, A., Llibre, J.: Quadratic planar differential systems with algebraic limit cycles via quadratic plane Cremona maps. Adv. Math. **389**, 107924 (2021)

[Article][149] [MathSciNet][150] [Google Scholar][151]

35.

Chicone, C., Jacobs, M.: Bifurcation of limit cycles from quadratic isochrones. J. Differ. Equ. **91**(2), 268–326 (1991)

[Article][152] [MathSciNet][153] [Google Scholar][154]

36.

Andronov, A. A., Leontovich, E. A., Gordon, I. I., Maĭer, A. G.: Theory of bifurcations of dynamic systems on a plane. Israel Program for Scientific Translations, Jerusalem-London, Translated from the Russian. Halsted Press, John Wiley & Sons, New York-Toronto (1973)

37.

Romanovski, V.G., Shafer, D.S.: The center and cyclicity problems: a computational algebra approach. Birkhäuser Boston Ltd, Boston, MA (2009)

[Google Scholar][155]

38.

Chicone, C., Jacobs, M.: Bifurcation of critical periods for plane vector fields. Trans. Amer. Math. Soc. **312**(2), 433–486 (1989)

[Article][156] [MathSciNet][157] [Google Scholar][158]

39.

Han, M.: Liapunov constants and Hopf cyclicity of Liénard systems. Ann. Differ. Equ. **15**(2), 113–126 (1999)

[Google Scholar][159]

40.

Sánchez-Sánchez, I., Torregrosa, J.: New lower bounds of the number of critical periods in reversible centers. J. Differ. Equ. **292**, 427–460 (2021)

[Article][160] [MathSciNet][161] [Google Scholar][162]

[Download references][163]

## Acknowledgements

This work has been realized thanks to the Catalan AGAUR Agency (grant 2021 SGR 00113); the Spanish AEI agency (grants PID2022-136613NB-I00 and CEX2020-001084-M); and the Brazilian FAPESP 2023/09466-4 grant. The author expresses gratitude for the kind hospitality of Universidade Estadual Paulista (UNESP), São José do Rio Preto campus, where this work was completed. The author also thanks Maria Alberich and Antoni Ferragut for their valuable discussions during the preliminary preparation of this manuscript.

## Funding

Open Access Funding provided by Universitat Autonoma de Barcelona.

## Author information

### Authors and Affiliations

1.

Departament de Matemàtiques, Universitat Autònoma de Barcelona, 08193, Bellaterra, Barcelona, Spain

Joan Torregrosa

2.

Centre de Recerca Matemàtica, Campus de Bellaterra, 08193, Bellaterra, Barcelona, Spain

Joan Torregrosa

Authors

1. Joan Torregrosa

[View author publications][164]

Search author on: [PubMed][165] [Google Scholar][166]

### Corresponding author

Correspondence to [Joan Torregrosa][167].

## Ethics declarations

### Conflict of interest

The author certifies that there are no conflict of interest.

## Additional information

Communicated by Marco Antonio Teixeira.

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][168].

[Reprints and permissions][169]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [170]

### Cite this article

Torregrosa, J. Cubic planar vector fields with high local cyclicity. *São Paulo J. Math. Sci.***19**, 4 (2025). https://doi.org/10.1007/s40863-024-00486-9

[Download citation][171]

-

Accepted: 25 September 2024

-

Published: 28 December 2024

-

Version of record: 28 December 2024

-

DOI: https://doi.org/10.1007/s40863-024-00486-9

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Center-focus][172]
- [Cyclicity][173]
- [Limit cycles][174]
- [Weak-focus order][175]
- [Lyapunov quantities][176]

### Mathematics Subject Classification

- [Primary 34C07][177]
- [34C23][178]
- [37C27][179]

### Profiles

1. Joan Torregrosa [View author profile][180]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s40863-024-00486-9.pdf
[3]: /article/10.1007/s40863-024-00486-9/save-research?_csrf=ax2K3PbOwhJ4Kqgpkgl_L-5bpRXBCYyi
[4]: /saved-research
[5]: /journal/40863
[6]: /journal/40863/aims-and-scope
[7]: https://www.editorialmanager.com/spjm
[8]: https://link.springer.com/10.1007/s12346-021-00479-5?fromPaywallRec=false
[9]: https://link.springer.com/10.3103/S1066369X25700331?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s00025-023-02045-8?fromPaywallRec=false
[11]: /subjects/algebraic-geometry
[12]: /subjects/dynamical-systems
[13]: /subjects/element-cycles
[14]: /subjects/field-theory-and-polynomials
[15]: /subjects/general-algebraic-systems
[16]: /subjects/nonlinear-dynamics-and-chaos-theory
[17]: /subjects/dynamical-systems-and-bifurcation-theory
[18]: /article/10.1007/s40863-024-00486-9#ref-CR4
[19]: /article/10.1007/s40863-024-00486-9#ref-CR5
[20]: /article/10.1007/s40863-024-00486-9#ref-CR6
[21]: /article/10.1007/s40863-024-00486-9#ref-CR7
[22]: /article/10.1007/s40863-024-00486-9#ref-CR8
[23]: /article/10.1007/s40863-024-00486-9#ref-CR9
[24]: /article/10.1007/s40863-024-00486-9#ref-CR10
[25]: /article/10.1007/s40863-024-00486-9#ref-CR11
[26]: /article/10.1007/s40863-024-00486-9#ref-CR12
[27]: /article/10.1007/s40863-024-00486-9#ref-CR13
[28]: /article/10.1007/s40863-024-00486-9#ref-CR14
[29]: /article/10.1007/s40863-024-00486-9#ref-CR15
[30]: /article/10.1007/s40863-024-00486-9#ref-CR16
[31]: /article/10.1007/s40863-024-00486-9#ref-CR17
[32]: /article/10.1007/s40863-024-00486-9#ref-CR18
[33]: /article/10.1007/s40863-024-00486-9#ref-CR19
[34]: /article/10.1007/s40863-024-00486-9#ref-CR20
[35]: /article/10.1007/s40863-024-00486-9#ref-CR21
[36]: /article/10.1007/s40863-024-00486-9#ref-CR22
[37]: /article/10.1007/s40863-024-00486-9#ref-CR23
[38]: /article/10.1007/s40863-024-00486-9#ref-CR24
[39]: /article/10.1007/s40863-024-00486-9#ref-CR25
[40]: /article/10.1007/s40863-024-00486-9#ref-CR26
[41]: /article/10.1007/s40863-024-00486-9#ref-CR29
[42]: /article/10.1007/s40863-024-00486-9#ref-CR32
[43]: /article/10.1007/s40863-024-00486-9#ref-CR33
[44]: /article/10.1007/s40863-024-00486-9#ref-CR34
[45]: /article/10.1007/s40863-024-00486-9#ref-CR35
[46]: /article/10.1007/s40863-024-00486-9#Sec2
[47]: /article/10.1007/s40863-024-00486-9#Sec3
[48]: /article/10.1007/s40863-024-00486-9#FPar1
[49]: /article/10.1007/s40863-024-00486-9#FPar2
[50]: /article/10.1007/s40863-024-00486-9#Equ4
[51]: /article/10.1007/s40863-024-00486-9#Equ5
[52]: /article/10.1007/s40863-024-00486-9#ref-CR36
[53]: /article/10.1007/s40863-024-00486-9#Equ3
[54]: /article/10.1007/s40863-024-00486-9#ref-CR37
[55]: /article/10.1007/s40863-024-00486-9#Equ6
[56]: /article/10.1007/s40863-024-00486-9#Equ7
[57]: /article/10.1007/s40863-024-00486-9#Equ8
[58]: /article/10.1007/s40863-024-00486-9#ref-CR38
[59]: /article/10.1007/s40863-024-00486-9#ref-CR39
[60]: /article/10.1007/s40863-024-00486-9#ref-CR40
[61]: /article/10.1007/s40863-024-00486-9#ref-CR27
[62]: /article/10.1007/s40863-024-00486-9#FPar3
[63]: /article/10.1007/s40863-024-00486-9#Equ1
[64]: /article/10.1007/s40863-024-00486-9#Equ10
[65]: /article/10.1007/s40863-024-00486-9#Equ11
[66]: /article/10.1007/s40863-024-00486-9#Equ12
[67]: /article/10.1007/s40863-024-00486-9#Equ13
[68]: /article/10.1007/s40863-024-00486-9#Equ2
[69]: /article/10.1007/s40863-024-00486-9#FPar10
[70]: /article/10.1007/s40863-024-00486-9#Equ15
[71]: /article/10.1007/s40863-024-00486-9#Equ14
[72]: /article/10.1007/s40863-024-00486-9#Equ9
[73]: https://doi.org/10.1142%2FS0218127405012740
[74]: http://www.ams.org/mathscinet-getitem?mr=2152073
[75]: http://scholar.google.com/scholar_lookup?amp;title=Monodromy%20and%20stability%20for%20nilpotent%20critical%20points&amp;journal=Internat.%20J.%20Bifur.%20Chaos.%20Appl.%20Sci.%20Eng.&amp;doi=10.1142%2FS0218127405012740&amp;volume=15&amp;issue=4&amp;pages=1253-1265&amp;publication_year=2005&amp;author=%C3%81lvarez%2CMJ&amp;author=Gasull%2CA
[76]: https://doi.org/10.1016%2Fj.jsc.2006.04.007
[77]: http://www.ams.org/mathscinet-getitem?mr=2251812
[78]: http://scholar.google.com/scholar_lookup?amp;title=A%20necessary%20condition%20in%20the%20monodromy%20problem%20for%20analytic%20differential%20equations%20on%20the%20plane&amp;journal=J.%20Symbolic%20Comput.&amp;doi=10.1016%2Fj.jsc.2006.04.007&amp;volume=41&amp;issue=9&amp;pages=943-958&amp;publication_year=2006&amp;author=Garc%C3%ADa%2CIA&amp;author=Gin%C3%A9%2CJ&amp;author=Grau%2CM
[79]: https://doi.org/10.1088%2F0951-7715%2F13%2F3%2F311
[80]: http://www.ams.org/mathscinet-getitem?mr=1758996
[81]: http://scholar.google.com/scholar_lookup?amp;title=The%20focus-centre%20problem%20for%20a%20type%20of%20degenerate%20system&amp;journal=Nonlinearity&amp;doi=10.1088%2F0951-7715%2F13%2F3%2F311&amp;volume=13&amp;issue=3&amp;pages=699-729&amp;publication_year=2000&amp;author=Gasull%2CA&amp;author=Llibre%2CJ&amp;author=Ma%C3%B1osa%2CV&amp;author=Ma%C3%B1osas%2CF
[82]: http://www.ams.org/mathscinet-getitem?mr=2030221
[83]: http://scholar.google.com/scholar_lookup?amp;title=A%20sufficient%20focus%20condition%20for%20a%20monodromic%20singular%20point&amp;journal=Tr.%20Mosk.%20Mat.%20Obs.&amp;volume=63&amp;pages=87-114&amp;publication_year=2002&amp;author=Medvedeva%2CNB&amp;author=Mazaeva%2CEV
[84]: https://doi.org/10.1515%2Fanona-2022-0314
[85]: http://scholar.google.com/scholar_lookup?amp;title=The%20Poincar%C3%A9%20map%20of%20degenerate%20monodromic%20singularities%20with%20Puiseux%20inverse%20integrating%20factor&amp;journal=Adv.%20Nonlinear%20Anal.&amp;doi=10.1515%2Fanona-2022-0314&amp;volume=12&amp;issue=1&amp;publication_year=2023&amp;author=Garc%C3%ADa%2CIA&amp;author=Gin%C3%A9%2CJ
[86]: https://doi.org/10.1016%2Fj.jde.2024.02.055
[87]: http://scholar.google.com/scholar_lookup?amp;title=The%20linear%20term%20of%20the%20Poincar%C3%A9%20map%20at%20singularities%20of%20planar%20vector%20fields&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2Fj.jde.2024.02.055&amp;volume=396&amp;pages=44-67&amp;publication_year=2024&amp;author=Garc%C3%ADa%2CIA&amp;author=Gin%C3%A9%2CJ
[88]: http://www.ams.org/mathscinet-getitem?mr=59426
[89]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20limit%20cycles%20which%20appear%20with%20the%20variation%20of%20coefficients%20from%20an%20equilibrium%20position%20of%20focus%20or%20center%20type&amp;journal=Amer.%20Math.%20Soc.%20Trans.&amp;volume=1954&amp;issue=100&amp;publication_year=1954&amp;author=Bautin%2CNN
[90]: http://www.ams.org/mathscinet-getitem?mr=188542
[91]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20limit%20cycles%20in%20the%20neighborhood%20of%20a%20singular%20point&amp;journal=Differ.%20Uravnenija&amp;volume=1&amp;pages=53-66&amp;publication_year=1965&amp;author=Sibirski%C4%AD%2CKS
[92]: https://doi.org/10.12775%2FTMNA.1994.024
[93]: http://www.ams.org/mathscinet-getitem?mr=1321810
[94]: http://scholar.google.com/scholar_lookup?amp;title=The%20classification%20of%20reversible%20cubic%20systems%20with%20center&amp;journal=Topol.%20Methods%20Nonlinear%20Anal.&amp;doi=10.12775%2FTMNA.1994.024&amp;volume=4&amp;issue=1&amp;pages=79-136&amp;publication_year=1994&amp;author=Zoladek%2CH
[95]: https://doi.org/10.12775%2FTMNA.1996.037
[96]: http://www.ams.org/mathscinet-getitem?mr=1483632
[97]: http://scholar.google.com/scholar_lookup?amp;title=Remarks%20on%3A%20the%20classification%20of%20reversible%20cubic%20systems%20with%20center&amp;journal=Topol.%20Methods%20Nonlinear%20Anal.&amp;doi=10.12775%2FTMNA.1996.037&amp;volume=8&amp;issue=2&amp;pages=335-342&amp;publication_year=1996&amp;author=Zoladek%2CH
[98]: https://doi.org/10.1088%2F0951-7715%2F8%2F5%2F011
[99]: http://www.ams.org/mathscinet-getitem?mr=1355046
[100]: http://scholar.google.com/scholar_lookup?amp;title=Eleven%20small%20limit%20cycles%20in%20a%20cubic%20vector%20field&amp;journal=Nonlinearity&amp;doi=10.1088%2F0951-7715%2F8%2F5%2F011&amp;volume=8&amp;issue=5&amp;pages=843-860&amp;publication_year=1995&amp;author=Zoladek%2CH
[101]: http://scholar.google.com/scholar_lookup?amp;title=The%20CD45%20case%20revisited&amp;pages=596-625&amp;publication_year=2016&amp;author=Zoladek%2CH
[102]: https://doi.org/10.1016%2Fj.jde.2020.08.027
[103]: http://www.ams.org/mathscinet-getitem?mr=4151565
[104]: http://scholar.google.com/scholar_lookup?amp;title=Lower%20bounds%20for%20the%20local%20cyclicity%20of%20centers%20using%20high%20order%20developments%20and%20parallelization&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2Fj.jde.2020.08.027&amp;volume=271&amp;pages=447-479&amp;publication_year=2021&amp;author=Gouveia%2CLFS&amp;author=Torregrosa%2CJ
[105]: https://doi.org/10.1016%2Fj.jde.2018.01.022
[106]: http://www.ams.org/mathscinet-getitem?mr=3765771
[107]: http://scholar.google.com/scholar_lookup?amp;title=Bifurcation%20of%20small%20limit%20cycles%20in%20cubic%20integrable%20systems%20using%20higher-order%20analysis&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2Fj.jde.2018.01.022&amp;volume=264&amp;issue=9&amp;pages=5950-5976&amp;publication_year=2018&amp;author=Tian%2CY&amp;author=Yu%2CP
[108]: http://www.ams.org/mathscinet-getitem?mr=2436621
[109]: http://scholar.google.com/scholar_lookup?amp;title=On%20a%20theorem%20of%20Zoladek&amp;journal=Differ.%20Uravn.&amp;volume=44&amp;issue=2&amp;pages=263-265&amp;publication_year=2008&amp;author=Bondar%2CYL&amp;author=Sadovski%C4%AD%2CAP
[110]: https://doi.org/10.1016%2Fj.cnsns.2013.12.014
[111]: http://www.ams.org/mathscinet-getitem?mr=3168063
[112]: http://scholar.google.com/scholar_lookup?amp;title=Twelve%20limit%20cycles%20around%20a%20singular%20point%20in%20a%20planar%20cubic-degree%20polynomial%20system&amp;journal=Commun.%20Nonlinear%20Sci.%20Numer.%20Simul.&amp;doi=10.1016%2Fj.cnsns.2013.12.014&amp;volume=19&amp;issue=8&amp;pages=2690-2705&amp;publication_year=2014&amp;author=Yu%2CP&amp;author=Tian%2CY
[113]: https://doi.org/10.1016%2Fj.jde.2020.11.035
[114]: http://www.ams.org/mathscinet-getitem?mr=4191324
[115]: http://scholar.google.com/scholar_lookup?amp;title=Lower%20bounds%20for%20the%20local%20cyclicity%20for%20families%20of%20centers&amp;journal=J.%20Differential%20Equations&amp;doi=10.1016%2Fj.jde.2020.11.035&amp;volume=275&amp;pages=309-331&amp;publication_year=2021&amp;author=Gin%C3%A9%2CJ&amp;author=Gouveia%2CLFS&amp;author=Torregrosa%2CJ
[116]: https://doi.org/10.1016%2Fj.jde.2015.07.027
[117]: http://www.ams.org/mathscinet-getitem?mr=3397329
[118]: http://scholar.google.com/scholar_lookup?amp;title=Parallelization%20of%20the%20Lyapunov%20constants%20and%20cyclicity%20for%20centers%20of%20planar%20polynomial%20vector%20fields&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2Fj.jde.2015.07.027&amp;volume=259&amp;issue=11&amp;pages=6494-6509&amp;publication_year=2015&amp;author=Liang%2CH&amp;author=Torregrosa%2CJ
[119]: https://link.springer.com/doi/10.1007/s12346-010-0031-8
[120]: http://www.ams.org/mathscinet-getitem?mr=2737371
[121]: http://scholar.google.com/scholar_lookup?amp;title=Focal%20values%20of%20plane%20cubic%20centers&amp;journal=Qual.%20Theory%20Dyn.%20Syst.&amp;doi=10.1007%2Fs12346-010-0031-8&amp;volume=9&amp;issue=1%E2%80%932&amp;pages=319-324&amp;publication_year=2010&amp;author=Graf%2CHC&amp;author=Kr%C3%B6ker%2CJ
[122]: https://doi.org/10.1134%2FS0012266120010164
[123]: http://www.ams.org/mathscinet-getitem?mr=4071976
[124]: http://scholar.google.com/scholar_lookup?amp;title=Existence%20of%20complex%20cubic%20systems%20with%20a%2014th-order%20focus&amp;journal=Differ.%20Equ.&amp;doi=10.1134%2FS0012266120010164&amp;volume=56&amp;issue=1&amp;pages=140-142&amp;publication_year=2020&amp;author=Sadovski%C4%AD%2CAP
[125]: https://doi.org/10.3934%2Fcpaa.2021107
[126]: http://www.ams.org/mathscinet-getitem?mr=4342173
[127]: http://scholar.google.com/scholar_lookup?amp;title=Orbitally%20symmetric%20systems%20with%20applications%20to%20planar%20centers&amp;journal=Commun.%20Pure%20Appl.%20Anal.&amp;doi=10.3934%2Fcpaa.2021107&amp;volume=20&amp;issue=10&amp;pages=3319-3347&amp;publication_year=2021&amp;author=Bastos%2CJLR&amp;author=Buzzi%2CCA&amp;author=Torregrosa%2CJ
[128]: https://link.springer.com/doi/10.1007/s12346-010-0024-7
[129]: http://www.ams.org/mathscinet-getitem?mr=2737366
[130]: http://scholar.google.com/scholar_lookup?amp;title=New%20results%20on%20the%20study%20of%20%24%24Z_q%24%24%20Z%20q%20-equivariant%20planar%20polynomial%20vector%20fields&amp;journal=Qual.%20Theory%20Dyn.%20Syst.&amp;doi=10.1007%2Fs12346-010-0024-7&amp;volume=9&amp;issue=1%E2%80%932&amp;pages=167-219&amp;publication_year=2010&amp;author=Li%2CJ&amp;author=Liu%2CY
[131]: https://doi.org/10.1142%2FS0218127405013289
[132]: http://www.ams.org/mathscinet-getitem?mr=2165061
[133]: http://scholar.google.com/scholar_lookup?amp;title=Twelve%20limit%20cycles%20in%20a%20cubic%20case%20of%20the%2016th%20Hilbert%20problem&amp;journal=Internat.%20J.%20Bifur.%20Chaos.%20Appl.%20Sci.%20Eng.&amp;doi=10.1142%2FS0218127405013289&amp;volume=15&amp;issue=7&amp;pages=2191-2205&amp;publication_year=2005&amp;author=Yu%2CP&amp;author=Han%2CM
[134]: https://doi.org/10.1016%2Fj.jde.2009.01.038
[135]: http://www.ams.org/mathscinet-getitem?mr=2515170
[136]: http://scholar.google.com/scholar_lookup?amp;title=A%20cubic%20system%20with%20thirteen%20limit%20cycles&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2Fj.jde.2009.01.038&amp;volume=246&amp;issue=9&amp;pages=3609-3619&amp;publication_year=2009&amp;author=Li%2CC&amp;author=Liu%2CC&amp;author=Yang%2CJ
[137]: http://scholar.google.com/scholar_lookup?amp;title=Bifurcation%20theory%20of%20limit%20cycles%20of%20planar%20systems&amp;pages=341-433&amp;publication_year=2006&amp;author=Han%2CM
[138]: https://link.springer.com/doi/10.1007/s10255-014-0420-x
[139]: http://www.ams.org/mathscinet-getitem?mr=3285975
[140]: http://scholar.google.com/scholar_lookup?amp;title=%24%24Z_2%24%24%20Z%202%20-equivariant%20cubic%20system%20which%20yields%2013%20limit%20cycles&amp;journal=Acta%20Math.%20Appl.%20Sin.%20Engl.%20Ser.&amp;doi=10.1007%2Fs10255-014-0420-x&amp;volume=30&amp;issue=3&amp;pages=781-800&amp;publication_year=2014&amp;author=Liu%2CY&amp;author=Li%2CJ
[141]: https://doi.org/10.1142%2FS0218127410027209
[142]: http://www.ams.org/mathscinet-getitem?mr=2738718
[143]: http://scholar.google.com/scholar_lookup?amp;title=Existence%20conditions%20of%20thirteen%20limit%20cycles%20in%20a%20cubic%20system&amp;journal=Internat.%20J.%20Bifur.%20Chaos.%20Appl.%20Sci.%20Eng.&amp;doi=10.1142%2FS0218127410027209&amp;volume=20&amp;issue=8&amp;pages=2569-2577&amp;publication_year=2010&amp;author=Yang%2CJ&amp;author=Han%2CM&amp;author=Li%2CJ&amp;author=Yu%2CP
[144]: http://www.ams.org/mathscinet-getitem?mr=2985691
[145]: http://scholar.google.com/scholar_lookup?amp;title=A%20new%20configuration%20of%20thirteen%20limit%20cycles%20for%20a%20cubic%20system&amp;journal=Beijing%20Shifan%20Daxue%20Xuebao&amp;volume=48&amp;issue=3&amp;pages=231-234&amp;publication_year=2012&amp;author=Zhao%2CLQ
[146]: https://doi.org/10.1088%2F1361-6544%2Faae94d
[147]: http://www.ams.org/mathscinet-getitem?mr=3893729
[148]: http://scholar.google.com/scholar_lookup?amp;title=New%20lower%20bounds%20for%20the%20Hilbert%20numbers%20using%20reversible%20centers&amp;journal=Nonlinearity&amp;doi=10.1088%2F1361-6544%2Faae94d&amp;volume=32&amp;issue=1&amp;pages=331-355&amp;publication_year=2019&amp;author=Prohens%2CR&amp;author=Torregrosa%2CJ
[149]: https://doi.org/10.1016%2Fj.aim.2021.107924
[150]: http://www.ams.org/mathscinet-getitem?mr=4290137
[151]: http://scholar.google.com/scholar_lookup?amp;title=Quadratic%20planar%20differential%20systems%20with%20algebraic%20limit%20cycles%20via%20quadratic%20plane%20Cremona%20maps&amp;journal=Adv.%20Math.&amp;doi=10.1016%2Fj.aim.2021.107924&amp;volume=389&amp;publication_year=2021&amp;author=Alberich-Carrami%C3%B1ana%2CM&amp;author=Ferragut%2CA&amp;author=Llibre%2CJ
[152]: https://doi.org/10.1016%2F0022-0396%2891%2990142-V
[153]: http://www.ams.org/mathscinet-getitem?mr=1111177
[154]: http://scholar.google.com/scholar_lookup?amp;title=Bifurcation%20of%20limit%20cycles%20from%20quadratic%20isochrones&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2F0022-0396%2891%2990142-V&amp;volume=91&amp;issue=2&amp;pages=268-326&amp;publication_year=1991&amp;author=Chicone%2CC&amp;author=Jacobs%2CM
[155]: http://scholar.google.com/scholar_lookup?amp;title=The%20center%20and%20cyclicity%20problems%3A%20a%20computational%20algebra%20approach&amp;publication_year=2009&amp;author=Romanovski%2CVG&amp;author=Shafer%2CDS
[156]: https://doi.org/10.1090%2FS0002-9947-1989-0930075-2
[157]: http://www.ams.org/mathscinet-getitem?mr=930075
[158]: http://scholar.google.com/scholar_lookup?amp;title=Bifurcation%20of%20critical%20periods%20for%20plane%20vector%20fields&amp;journal=Trans.%20Amer.%20Math.%20Soc.&amp;doi=10.1090%2FS0002-9947-1989-0930075-2&amp;volume=312&amp;issue=2&amp;pages=433-486&amp;publication_year=1989&amp;author=Chicone%2CC&amp;author=Jacobs%2CM
[159]: http://scholar.google.com/scholar_lookup?amp;title=Liapunov%20constants%20and%20Hopf%20cyclicity%20of%20Li%C3%A9nard%20systems&amp;journal=Ann.%20Differ.%20Equ.&amp;volume=15&amp;issue=2&amp;pages=113-126&amp;publication_year=1999&amp;author=Han%2CM
[160]: https://doi.org/10.1016%2Fj.jde.2021.05.013
[161]: http://www.ams.org/mathscinet-getitem?mr=4260011
[162]: http://scholar.google.com/scholar_lookup?amp;title=New%20lower%20bounds%20of%20the%20number%20of%20critical%20periods%20in%20reversible%20centers&amp;journal=J.%20Differ.%20Equ.&amp;doi=10.1016%2Fj.jde.2021.05.013&amp;volume=292&amp;pages=427-460&amp;publication_year=2021&amp;author=S%C3%A1nchez-S%C3%A1nchez%2CI&amp;author=Torregrosa%2CJ
[163]: https://citation-needed.springer.com/v2/references/10.1007/s40863-024-00486-9?format=refman&amp;flavour=references
[164]: /search?sortBy=newestFirst&amp;contributor=Joan%20Torregrosa
[165]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Joan%20Torregrosa
[166]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Joan%20Torregrosa%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[167]: mailto:joan.torregrosa@uab.cat
[168]: http://creativecommons.org/licenses/by/4.0/
[169]: https://s100.copyright.com/AppDispatchServlet?title=Cubic%20planar%20vector%20fields%20with%20high%20local%20cyclicity&amp;author=Joan%20Torregrosa&amp;contentID=10.1007%2Fs40863-024-00486-9&amp;copyright=The%20Author%28s%29&amp;publication=1982-6907&amp;publicationDate=2024-12-28&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[170]: https://crossmark.crossref.org/dialog/?doi=10.1007/s40863-024-00486-9
[171]: https://citation-needed.springer.com/v2/references/10.1007/s40863-024-00486-9?format=refman&amp;flavour=citation
[172]: /search?query=Center-focus&amp;facet-discipline=#34;Mathematics&#34;
[173]: /search?query=Cyclicity&amp;facet-discipline=#34;Mathematics&#34;
[174]: /search?query=Limit%20cycles&amp;facet-discipline=#34;Mathematics&#34;
[175]: /search?query=Weak-focus%20order&amp;facet-discipline=#34;Mathematics&#34;
[176]: /search?query=Lyapunov%20quantities&amp;facet-discipline=#34;Mathematics&#34;
[177]: /search?query=Primary%2034C07&amp;facet-discipline=#34;Mathematics&#34;
[178]: /search?query=34C23&amp;facet-discipline=#34;Mathematics&#34;
[179]: /search?query=%2037C27&amp;facet-discipline=#34;Mathematics&#34;
[180]: /researchers/13587833SN
