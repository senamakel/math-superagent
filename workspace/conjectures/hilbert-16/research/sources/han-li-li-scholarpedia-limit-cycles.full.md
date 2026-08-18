<!-- source: http://www.scholarpedia.org/article/Limit_cycles_of_planar_polynomial_vector_fields | converted from HTML -->

**Notice**: Undefined offset: 5841 in **/var/www/scholarpedia.org/mediawiki/includes/parser/Parser.php**on line **5961**
Limit cycles of planar polynomial vector fields - Scholarpedia

# Limit cycles of planar polynomial vector fields

From Scholarpedia

Maoan Han et al. (2010), Scholarpedia, 5(8):9648. | [doi:10.4249/scholarpedia.9648][1] | revision #137138 [[link to/cite this article][2]] |

Jump to: navigation, search

**Post-publication activity**

Curator: [Chengzhi Li][3]

Contributors:

0.67 -

[Eugene M. Izhikevich][4]

0.33 -

[Maoan Han][5]

0.17 -

[Nick Orbeck][6]

0.17 -

[Jibin Li][7]

0.17 -

[Benjamin Bronner][8]

-

[Prof. Maoan Han, Shanghai Normal University][5]

-

[Prof. Chengzhi Li, Peking University, Beijing, China][3]

-

[Prof. Jibin Li, Zhejiang University and Kunming Institute of Technology, China][7]

## Contents

- 1 Definition and Hilbert's 16th problem

  - 1.1 Limit Cycle for a Planar Polynomial Vector Field
  - 1.2 Hilbert's and Weak Hilbert's 16th Problem

- 2 Quadratic Systems

  - 2.1 Ye's classification
  - 2.2 Some Global Results on Limit Cycles
  - 2.3 Some Bifurcation Results of Limit Cycles

- 3 Polynomial Systems with Higher Degrees

  - 3.1 Polynomial Equivariant Systems
  - 3.2 Analytical property of Abelian integrals
  - 3.3 Methods of Studying the Number of Limit Cycles

- 4 Limit Cycles in Li\({\acute{e}}\)nard Systems

  - 4.1 Existence and Uniqueness of Limit Cycles
  - 4.2 Hopf bifurcation for Polynomial Liénard Systems
  - 4.3 Global Results for Polynomial Li\({\rm \acute{e}}\)nard Systems

- 5 References

 |

## Definition and Hilbert's 16th problem

### [Limit Cycle][9] for a Planar Polynomial [Vector Field][10]

The authors' remark. In this article we would like to provide a comprehensive review on the study of limit cycles of planar polynomial vector fields, closely related to Hilbert's 16th problem. In particular, we reviewed the progress of research on the quadratic systems, higher-degree polynomial systems, as well as Liénard systems. There are so many researches in this area that it is impossible to give a complete review for the study of limit cycles. This article is written with the purpose to mainly include contributions of Chinese scholars.

Let \(P_n\) and \(Q_n\) be polynomials in \((x,y)\) satisfying \(\max\{\deg(P_n),\deg(Q_n)\}=n\ .\) Then the equations \((E_n)\) \[\frac{dx}{dt}=P_n(x,y),\ \ \frac{dy}{dt}=Q_n(x,y) \] define a planar polynomial system which corresponds to a polynomial vector field on the plane. Any nontrivial periodic solution of the system determines a closed curve on the phase plane, called a periodic orbit.

A periodic orbit is called a limit cycle if there is a neighborhood of it such that it is the \(\alpha-\)limit set or \(\omega-\)limit set of all points in the neighborhood. Furthermore, the limit cycle is called [stable][11] if it is the \(\omega-\)limit set of all points in the neighborhood. It is called unstable if not stable.

Using the solutions near a limit cycle one can define a return map or Poincar\({\rm \acute{e}}\) map which can be used to define multiplicity of the limit cycle. A limit cycle is called simple or hyperbolic if it has multiplicity one.

**Example**

[Van der Pol][12] 's system \[ \frac{dx}{dt}=y,\ \ \frac{dy}{dt}=-x+\mu (1-x^2)y,\ \mu>0 \] has a unique limit cycle, which is stable and hyperbolic.

### Hilbert's and Weak Hilbert's 16th Problem

At the Second International Congress of Mathematicians, Paris, in 1900, D. Hilbert posed his 23 mathematical problems. The second part of his 16th problem can be stated as follows (see [53]):

For a given integer \(n\geq 2\ ,\) what is the maximum number of limit cycles of system \((E_n)\) for all possible \(P_n\) and \(Q_n\ ?\) And how about the possible relative positions of the limit cycles?

This problem is still open, but it has been proved by \({\rm \acute{E}}\)calle [27] and Ilyashenko [60] that the number of limit cycle is finite for a given system \((E_n)\ .\)

Note that the problem is trivial for \(n=1\ :\) a linear system may have periodic orbits but has no limit cycle. Let \(H(n)\) denote the maximum number for \(n\geq 2\ ,\) called Hilbert number. Is \(H(n)\) finite? It is also open ever for \(n=2\ .\)

Now consider a near-Hamiltonian polynomial system of the form \[ \frac{dx}{dt}=\frac{\partial H_m}{\partial y}+\varepsilon P_n(x,y),\quad \frac{dy}{dt}=-\frac{\partial H_m}{\partial x}+\varepsilon Q_n(x,y), \] where \(H_m=H_m(x,y)\) is a polynomial in \(x,y\) of degree \(m\) such that the equations \(H_m(x,y)=h\) define a family of closed curves \(L_h\) for \(h\) in an interval. We take a segment \(\sigma\ ,\) transversal to each oval \(L_h\ ,\) and choose the values of the function \(H\) itself to parameterize \(\sigma\ ,\) and denote by \(\gamma(h,\varepsilon)\) a piece of the orbit of the perturbed system between the starting point \(h\) on \(\sigma\) and the next intersection point \(P(h,\varepsilon)\) with \(\sigma\ .\) The ``next intersection*is possible for sufficiently small \(\varepsilon\ ,\)*since \(\gamma(h,\varepsilon)\) is close to \(L_h\ .\) Then the displacement function \(F(h,\varepsilon)=P(h,\varepsilon)-h\) can be expressed as \[ F(h,\varepsilon)=\varepsilon M(h)+O(\varepsilon^2), \] where \[ M(h)=\oint_{L_ h}P_ndy-Q_ndx, \] which is called the first order Melnikov function.

Weak Hilbert's 16th problem posed by V. I. Arnold (1977, 1990) [1,2] is the following.

For given integers \(m\) and \(n\) find the maximum \(Z(m,n)\) of the numbers of isolated zeros of the Abelian integrals \(M(h)\) for all possible \(P_n\ ,\) \(Q_n\) and \(H_m\ .\)

It is easy to see that \(Z(2,n)=[\frac{n-1}{2}]\) since \(M(h)\) is a polynomial in this case. In 1984 it has been proved \(Z(m,n)<\infty\) (Khovansky [64], Varchenko [108]). During 1994-2002 it has been proved that in generic cases \(Z(3,2)=2\) (Horozov and Iliev [55], Zhang and Li [124], Gavrilov [30] and Li and Zhang [71], and in degenerate cases \(Z(3,2)=3\) ( [31], [56], [57], [127], [128] and [11]). Also see the second part of the book by Christopher and Li(2007)[14].

## Quadratic Systems

### Ye's classification

Any quadratic system with a center or focus can be transformed into one of the following systems

(I) \(\frac{dx}{dt}=-y+dx+lx^2+mxy+ny^2,\) \(\frac{dy}{dt}=x;\)

(II) \(\frac{dx}{dt}=-y+dx+lx^2+mxy+ny^2,\) \(\frac{dy}{dt}=x(1+ax),\,\,\,a\neq 0;\)

(III) \(\frac{dx}{dt}=-y+dx+lx^2+mxy+ny^2,\) \(\frac{dy}{dt}=x(1+ax+by),\,\,\,b\neq 0,\)

which is called Ye's classification, made by Yanqian Ye in 1960s. Many researches were done by using the classification, see Ye(1986)[112] and the following.

### Some Global Results on Limit Cycles

L. Chen and Y. Ye(1975)[8], X. Yang and Y. Ye(1978)[111] proved that any system in class I has at most one limit cycle. Then Cherkas and Zhilevich [13], [6] and Ryckov [93] proved that any system in class III with \(a=0\) has at most one limit cycle. Hence, a quadratic system with a straight line solution has at most one limit cycle. There are some studies on the non-existence of limit cycles around a third order focus of quadratic systems between 1976 and 1986. The conclusion was completely proved in 1986 by Li(1986) [65] and Cherkas(1986)[12].

Many people have their contribution to the uniqueness of limit cycles, showing that any quadratic system has at most one limit cycle around a second order weak focus and it is hyperbolic if exists, including S. Cai, Z. Wang, W. Chen, M. Han, P. Zhang, W. Li, S. Gao, X. Wang, X. Huang and J. Reyn, investigating various particular cases under different conditions. The final proof for general quadratic systems was given by Zhang(1999) in [120].

In 1955, Petrovsky and Landis [90] attempted to prove \(H(2)=3\ .\) Unfortunately, their proof contained errors. Then in 1979, L. Chen and M. Wang [7] and S. Shi (1980) found respectively examples of quadratic systems having 4 limit cycles, giving \(H(2)\geq 4\ .\) It is widely conjectured that \(H(2)=4\ .\)

In 1959 T. Tung [99] found out some important properties of quadratic systems: a closed orbit is convex; there is a unique singularity in the interior of it; two closed orbits are similarly (resp. oppositely) oriented if their interiors have (resp. do not have) common points. Hence, the distribution of limit cycles of quadratic systems have only one or two nests. Around 2000 P. Zhang [121,122] proved that in two nests case at least one nest contains a unique limit cycle. Therefore, (2,2)-distribution of limit cycles for a quadratic system is impossible.

P. Zhang and S. Cai [123] and D. Zhu [129] respectively proved that a quadratic system with a second or third order weak saddle point does not have a limit cycle. P. Zhang [119] further proved that a quadratic system with a first order saddle point has at most one limit cycle. The global geometry of quadratic systems is also an interesting topic, for studies in this aspect see D. Schlomiuk [94,95,96], for example.

There are many more other results on the non-existence, uniqueness of limit cycles, existence of two limit cycles and global phase analysis. See Ye(1986) [112] and Reyn(2007) [91].

### Some [Bifurcation][13] Results of Limit Cycles

In 1952, Bautin [3] studied the [Hopf bifurcation][14] for quadratic systems and proved that there are at most 3 limit cycles bifurcated from a weak focus or center of such a system, and 3 limit cycles can appear.

Zhu(1989) [129], Joyal and Rousseau(1989) [63] and Cai and Guo(1990) [5] respectively proved that in quadratic systems there are at most 3 limit cycles bifurcated from an isolated homoclinic loop. However, it is still open if the number 3 can be achieved. Horozov and Iliev(1994) [54] proved that in quadratic systems the maximum number of limit cycles that can appear near a homoclinic loop of a nondegenerate [Hamiltonian system][15] is 2 under small perturbations with a single parameter, where a Hamiltonian system is called nondegenerate if the perturbed system is [Hamiltonian][16] when \(M(h)\equiv 0\ .\) From their proof the conclusion is also true under small perturbation with arbitrary parameters. Then Iliev [56] proved that the maximum number of limit cycles near a homoclinic loop of a degenerate Hamiltonian system is 2 under small perturbation with a single parameter by using up to the fourth order Melnikov functions. Han, Ye and Zhu [47] further proved that this conclusion is also true for the case of degenerate Hamiltonian systems under small perturbation with arbitrary parameters. Thus, in quadratic systems the maximum number of limit cycles near a homoclinic loop of any Hamiltonian system is 2 under arbitrary small perturbations. There are also some studies on the number of limit cycles near a homoclinic loop of an integrable non-Hamiltonian system under quadratic perturbations, see He and Li [52], Han(1997) [32]. The results obtained positively suggest that 2 is also the maximum number for the integrable case.

There may appear a polycycle or heteroclinic loop with two or three elementary saddles in quadratic systems. The results obtained by Dumortier, Roussarie and Rousseau [24], Zoladek [130] and Han-Yang [45] show that at most (resp, three) two limit cycles can be bifurcated from a polycycle with two (resp., three) saddles. Also, in the both cases, two limit cycles can appear.

It seems very difficult even impossible to find an example of quadratic systems having three limit cycles near a polycycle with 3 saddles.

## Polynomial Systems with Higher Degrees

### Polynomial Equivariant Systems

We consider polynomial plane systems with some symmetry. For convenience, we write the system \(E_n\) into the vector form \[ \frac{du}{dt}=V(u), \] where \(u=(x,y)\) and \(V(u)=(P_n(x,y),Q_n(x,y))\ .\) Let \(S\ :\) \( {R}^{2}\rightarrow {R}^{2}\) be an invertible differentiable map. We say that \(S\) is a symmetry of the above system or the system is \(S-\) *equivariant*if \[ DS(u)\cdot V(u)=V(S(u)),\quad u\in {R}^{2}. \] It is easy to see that the system is \(S-\) equivariant if and only if it is invariant under the transformation \(S\ .\)

If \(S\) is linear, then the above becomes \[ SV(u)=V(S(u)),\quad u\in {R}^{2}. \] For example, if \(S\) is the reflection: \[ S=\left( \begin{array}{cc} 1&0\\0&-1 \end{array}\right)=\rm diag (1,-1), \] then the \(S-\) equivariance means \[ P_n(x,y)=P_n(x,-y),\quad Q_n(x,y)=-Q_n(x,-y). \] In this case, the flow is symmetric with respect to the \(x\)-axis.

Now let \(S\) be a rotation by angle \(2\pi/q\) for an integer \(q\geq 2\ .\) Then \[ S=\left( \begin{array}{cc} \cos\frac{2\pi}{q}&-\sin\frac{2\pi}{q}\\ \sin\frac{2\pi}{q}&\cos\frac{2\pi}{q} \end{array} \right)\equiv Z_{q}. \]

Let \[ F(z,\bar{z})=P_n(\frac{z+\bar{z}}{2},\frac{z- \bar{z}}{2i})+i\,Q_n(\frac{z+\bar{z}}{2},\frac{z-\bar{z}}{2i}). \]

Then J. Li and X. Zhao (1989) [84] proved that the system \(\frac{du}{dt}=V(u)\) is \(Z_{q}\)-equivariant if and only if the function \(F\) has the form \[ F(z,\bar{z})=\sum_{l\geq 1}p\,_{l}(|z|^{2})\bar{z}\,^{lq-1}+\sum_{l\geq 0}h\,_{l}(|z|^{2})z\,^{lq+1}, \] where \(p_{l}\) and \(h_{l}\) are complex polynomials. For the discussion of \(Z_{q}\)-equivariant, also see F. Takens(1974) [98] and V. I. Arnold(1977) [1].

In particular, for a polynomial system of degree \(5\ ,\) it is \(Z_2\)-equivariant if and only if \(V(-u)=-V(u)\ ;\) it is \(Z_q\)-equivariant \((3\leq q\leq 6)\) if and only if the function \(F\) has the following form \[ \begin{array}{ccl} (1)&q=3,&F(z,\bar{z})=(A_{0}+A_{1}|z|^{2}+A_{2}|z|^{4})z+(A_{3}+A_{4}|z|^{2})\bar{z}^{2}+A_{5}z^{4}+A_{6}\bar{z}^{5},\\ (2)&q=4,&F(z,\bar{z})=(A_{0}+A_{1}|z|^{2}+A_{2}|z|^{4})z+(A_{3}+A_{4}|z|^{2})\bar{z}^{3}+A_{5}{z}^{5},\\ (3)&q=5,&F(z,\bar{z})=(A_{0}+A_{1}|z|^{2}+A_{2}|z|^{4})z+A_{3}\bar{z}^{4},\\ (4)&q=6,&F(z,\bar{z})=(A_{0}+A_{1}|z|^{2}+A_{2}|z|^{4})z+A_{3}\bar{z}^{5}. \end{array} \]

There have been many studies on the limit cycles of \(Z_q\)-equivariant polynomial systems, see [73,78,74,75,80,81,82].

### Analytical property of Abelian integrals

As before, let \[M(h)=\oint_{L_ h}P_ndy-Q_ndx, \] where \(L_h\) denotes a closed orbit defined by \(H_m(x,y)=h\) for \(h\in (h_1,h_2)\ .\) Obviously, \(M\) is analytic at each \(h\in (h_1,h_2)\ .\) There have been some studies on the analytical property of \(M\) at the endpoints \(h_1,h_2.\) Let \(h_0\in \{h_1,h_2\},\) and \(L_{h_0}\) denote the limit of \(L_h\) as \(h\rightarrow h_0\ .\) If \(L_{h_0}\) is an elementary center, it was proved in M. Han(2000) [35] and W. Li(2000) [85] (Theorem 3.9 in Chapter 4) that \(M\) is analytic at \(h=h_0\ .\) Thus, for \(h\) near \(h_0\) \(M\) has the following expansion \[M(h)=\sum_{i\geq 0}b_i(h-h_0)^{i+1}.\] A program was established in Han, Yang and Yu (2009)[46] for computing the coefficients \(b_i\) in the above expansion. If \(L_{h_0}\) is a homoclinic loop passing through a hyperbolic saddle, it was proved in Roussarie(1986) [92] that \(M\) has the expansion \[M(h)=\sum_{i\geq 0}[c_{2i}(h-h_0)^{i}+c_{2i+1}(h-h_0)^{i}\ln|h-h_0|].\] For the explicit formulas of the coefficients \(c_0\ ,\) \(c_1\ ,\) \(c_2\) and \(c_3\ ,\) see Han, Yang, Alina and Gao (2008)[44]. Jiang and Han(1999)[62] proved that the above expansion remains true if \(L_{h_0}\) is a heteroclinic loop passing through two or more hyperbolic saddles. Recently, Han etc. [38,48,118] considered the cases of \(L_0\) being a nilpotent center or homoclinic loop passing through a cusp or nilpotent saddles, and obtained expansions of \(M\ .\) All of those expansions have an important application: one can use the coefficients appeared in the expansions to produce zeros of \(M\) near both endpoints and hence to study the number of limit cycles in Hopf bifurcation and homoclinic bifurcation etc.. For example, one can give an explicit condition which ensures the existence of 7 limit cycles near a double homoclinic loop, see Han and Zhang(2006)[49].

### Methods of Studying the Number of Limit Cycles

There are three main aspects in studying the number of limit cycles. The first is Hopf bifurcation. There have been many results in this aspect. The main technique is to compute focus values or Liapunov constants, see for example [28] and [113]. By this method, P. Yu and M. Han [115,116, 114] studied Hopf bifurcations of \(Z_2\)-equivariant cubic systems, proving \(H(3)\geq 12\ .\) Then \(Z_2\)-equivariant cubic systems were further studied by J. Li and Y. Liu in [79] proving \(H(3)\geq 13\) (a different cubic system showing \(H(3)\geq 13\) was given by C. Li, C. Liu and J. Yang [66] in the same year, using Abelian integral and [21]). The Hopf bifurcation of \(Z_5\) and \(Z_6\)-equivariant planar polynomial vector field of degree 5 was studied in [79] in detail, and obtained 25 and 24 limit cycles respectively. Another method is to compute the first coefficients appearing in the expansion of the first order Melnikov function at a center, say, it is proved in [46] that a center of Hamiltonian quadratic system generates at most 5 limit cycles under perturbations of cubic polynomials.

The second aspect is limit cycle bifurcation from a family of periodic orbits for near-Hamiltonian or near-integrable systems. The main idea is to estimate the number of zeros of the Melnikov function \(M(h)\ .\) In many cases the function can be written into the form \[M(h)=I(h)[\lambda-P(h)].\] Then in order to analyze the zeros of \(M(h)\) one needs to study the geometrical property of the curve \(\lambda=P(h)\) on the \(\lambda-P\) plane. The function \(P(h)\) is called detection function. This method was first introduced by J. Li etc. in 1990s, and is very valid in many applications to polynomial systems. See [73] for more details. By this detection function method J. Li and Q. Huang(1987)[77] obtained \(H(3)\geq 11\ .\)

There are many papers concerning the weak Hilbert's 16th problem, by using the Picard-Fuchs equations, the Argument Principle, the [averaging][17] method, the Picard-Lefschetz formula and by using some techniques, see for example [9,10,17,11,22,25,26,30,55,58,59,67,68, 69,70,71,127,128] etc..

The third aspect is limit cycle bifurcation near a homoclinic loop or a poly-cycle for near-Hamiltonian or near-integrable systems. One way is to use the expansion of the Melnikov function at the loop, discussing the number of limit cycles near the loop. The method was originated by Roussarie(1986) [92] for the case of homoclinic loop and developed in [62,44,40,109] for the cases of double homoclinic loops and poly-cycles. The other way is to produce limit cycles by changing the stability of a homoclinic loop originated by Han(1997)[33] and developed with many applications to polynomial systems in [47,37,45,39,49,51,50,41,42,103,102,29,105,106,107,104,43] etc.. From [39], \(H(4)\geq 20\ .\) From [103], \(H(5)\geq 28\ .\) From [101], \(H(6)\geq 35\ .\) From [83], \(H(7)\geq 50\ .\) Otrokov [89] proved that \(H(n) \geq (n^2 + 5n-20-6(-1)^n)/2\) for \(n \geq 6.\) Christopher and Lloyd [15] proved that \[ H(n)\geq \frac{1}{2\ln 2}(n+1)^2\ln (n+1)-\frac{35}{24}(n+1)^2+3n+\frac{4}{3} \] for \(n=2^k-1,\,k\geq 2\ .\) Then Li, Chan and Chung [76] obtained \[ H(n)\geq \frac{1}{4\ln 2}(n+1)^2\ln (n+1)-\frac{1}{4}\left(\frac{\ln3}{\ln2}-\frac{25}{27}\right)(n+1)^2+n+\frac{2}{3} \] for \(n=3\cdot2^k-1,\,k\geq 1\ .\)

Recently, Han [36] obtained the following: For any sufficiently small \(\varepsilon>0\) there exists a positive number \(n^*\ ,\) depending on \(\varepsilon\ ,\) such that \[ H(n)>\left(\frac{1}{2\ln2}-\varepsilon\right)(n+2)^2\ln(n+2)\quad {\rm for}\quad n>n^*. \] Hence, \[ \lim_{n\rightarrow\infty}\inf \frac{H(n)}{(n+2)^2\ln(n+2)}\geq \frac{1}{2\ln2}. \] That is to say, \(H(n)\) grows at least as rapidly as \(\frac{1}{2\ln2}(n+2)^2\ln(n+2)\ .\)

## Limit Cycles in Li\({\acute{e}}\)nard Systems

### Existence and Uniqueness of Limit Cycles

In 1926, B. van der Pol [100] investigated the triode vacuum tube and found a phenomenon of stable self-excited oscillations of constant amplitude, producing a second order differential equation of the form \[x''+\mu(x^2-1)x'+x=0.\] The stable self-excited oscillations correspond to a stable limit cycle. Then in 1928 Li\({\acute{e}}\)nard [86] studied the following equation \[x''+f(x)x'+g(x)=0,\] where \(f\) is even and \(g\) odd. The equation is equivalent to a plane system of the form \[\dot{x}=y, \dot{y}=-f(x)y-g(x)\] or of the form \[\dot{x}=y-F(x), \dot{y}=-g(x), F(x)=\int_0^xfdx\] which is called a Li\({\acute{e}}\)nard system. A more general system of the form \[\dot{x}=h(y)-F(x), \dot{y}=-g(x), F(x)=\int_0^xfdx\] is called a generalized Li\({ \acute{e}}\)nard system, where \(f\ ,\) \(g\) and \(h\) are continuous functions. There are many studies on the nonexistence and uniqueness of limit cycles and the existence of one or more limit cycles. For details, see [112] and [126]. There are different methods for proving the uniqueness of limit cycles. One of them is to compare the integrals of the divergence of the system along two limit cycles, which was originated by Zhang Zhifen in 1958 (see [125]). She proved the following which is called Zhang Zhifen's theorem:

Let \(G\) denote a rectangle containing the origin. If \(xg(x)>0\ ,\) \(yh(y)>0\) and the functions \(f(x)/g(x)\) and \(h(y)\) are strictly monotone in their variable for all \((x,y) \in G\) with \(x\neq0\ ,\) \(y\neq0\ ,\) then the generalized Li\({\rm \acute{e}}\)nard system has at most one limit cycle in \(G\ .\)

### Hopf bifurcation for Polynomial Liénard Systems

Consider the Liénard system \[\dot x = y,\ \dot y = -f_m(x)y-g_n(x),\] where \(f_m\) and \(g_n\) are polynomials in \(x\) of degree \(m\) and \(n\) respectively. Let \({H}(m, n)\) denote the maximum number of limit cycles for all possible \(f_m\) and \(g_n\ ,\) and let \(\hat{H}(m, n)\) denote the maximum number of small-amplitude limit cycles of the above system that can be bifurcated from a focus. We have obviously \({H}(m, n)\geq \hat{H}(m, n)\ .\)

In 1984, Blows and Lloyd [4] proved \(\hat H(m, 1)=\left[\frac{m}{2}\right]\ .\) Han [34] proved \(\hat H(m, 2)=\left[\frac{2m+1}{3}\right]\) for all \(m\geq 1\ .\) Christopher and Lynch [16] obtained \(\hat H(m, 2)=\hat H(2, m)=\left[\frac{2m+1}{3}\right]\) for all \(m\geq 1\ ,\) and \(\hat H(m, 3)=\hat H(3, m)=2\left[\frac{3m+6}{8}\right]\) for all \(1<m\leq 50\ .\) The authors [16] also gave a table of \(\hat{H}(m, n)\) for some specific values of \(m\) and \(n\ .\) The table was complemented in Yu and Han [117] for some more values of \(m\) and \(n\ .\) If \(f\) is even and \(g\) is odd with \(n=3\ ,\) then \(\hat H(m,3)=m\) for all \(m\geq 2\) (see [61]). The ultimate aim is to establish a general formula for \(\hat H (m,n)\) as a function of \(m\) and \(n\ .\)

### Global Results for Polynomial Li\({\rm \acute{e}}\)nard Systems

We have seen that the number \(\hat{H}(m, n)\) gives a lower bound of \({H}(m, n)\ .\) Finding \({H}(m, n)\) is the Hilbert 16th problem for the Li\'enard System. We call \({H}(m, n)\) the Hilbert's number for the system.

It is easy to see that \(H(1,1)=0\ .\) In 1977, Lins, de Melo and Pugh [87] proved that \(H(2,1)=1\ .\) They also made a conjecture \( H(m,1)=\left[\frac{m}{2}\right]\ .\) A counterexample was found in [23] with 4 limit cycles for the case \(m=6\ ,\) \(n=1\ .\) In 1988, Coppel [18] proved that \(H(1,2)=1\ .\) In 1986, Li [72] proved \(H(2,2)=1\) which was then reproved by Dumortier and Li [19] in 1997 and Luo, Wang, Zhu and Han [88] in 1997 by using Zhang Zhifen's theorem. In 1996, Dumortier and Li [20] proved that \(H(1,3)=1\ .\) What is the Hilbert's number for all other cases is still open. Then an interesting problem is to find a better lower bound of it than \(\hat{H}(m, n)\ .\) It is conjectured that \(H(3,1)=1\ .\) From Dumortier and Li [21] we know \(H(2,3)\geq 5.\) Recently, Yang, Han and Romanovski [110] obtained \[H(m,3)\geq \left[\frac{3m+14}{4}\right], \ m=3,4,5,6,7,8. \]

## References

[1] V. I. Arnold, Loss of stability of self-oscillations close to [resonance][18] and versal deformations of equivariant vector fields, Funct. Anal. Appl. 11 (1977), 85-92.

[2] V. I. Arnold, Ten problems, Adv. Soviet Math. 1 (1990), 1-8.

[3] N. N. Bautin, On the number of limit cycles which appear with the variation of coefficients from an [equilibrium][19] position of center type, Mathem. Sbornik (N.S)30(72)(1952), 181-196. Translated into English by F.V.Atkinson and published by the AMS in 1954 as Translation Number 100, 396-413; reprint as AMS Transl.(1)5(1962), 396-413.

[4] T. R. Blows and N. G. Lloyd, The number of small-amplitude limit cycles of Li¨¦nard equations, Math. Proc. Cambridge Philos. Soc., 95 (1984), 359-366.

[5] S. Cai and G. Guo, Saddle values and limit cycles generated by separatrix of quadratic systems. Proceedings of Asian Mathematical Conference, 1990 (Hong Kong, 1990), 25-31, World Sci. Publ., River Edge, NJ, 1992.

[6] L. A. Cerkasand L. I. Zhilevich, The limit cycles of certain differential equations, (Russian), Diff. Uravn. 8(7)(1972),1207-1213. (Engl. Transl. 924-929).

[7] L. Chen and M. Wang, Relative position and number of limit cycles of a quadratic differential system, (Chinese), Acta Math.Sinica 22(1979), 751-758.

[8] L. Chen and Y. Ye, Uniqueness of limit cycle of the systems of equations \(dx/dt = -y + dx + lx^2 +xy + ny^2, dy/dt = x\ ,\) Acta Math. Sinica 18 (1975), 219-222 (Chinese).

[9] G. Chen, C. Li, C. Liu and J. Llibre, The cyclicity of period annuli of some classes of reversible quadratic systems. Disc. & Contin. Dyn. Sys. 16 (2006), 157-177.

[10] F. Chen, C. Li, J. Llibre and Z. Zhang, A uniform proof on the weak Hilbert's 16th problem for \(n=2\ .\) J. Diff. Eqns. 221 (2006), 309-342.

[11] S.-N. Chow, C. Li and Y. Yi, The cyclicity of period annulus of degenerate quadratic Hamiltonian system with elliptic segment loop. Erg. Th. Dyn. Syst. 22 (2002), 1233-1261.

[12] L. A. Cherkas, Absence of limit cycles around a triple focus in a quadratic system in a plane, (Russian), Diff.Uravn.,22 (ll)(1986), 2015-2017, 2024.

[13] L. A. Cherkas and L. I. Zhilevich, Some criteria for the absence of limit cycles and for the existence of a single limit cycle, (Russian), Different. Uravn., 6(7)(1970), 1170-1178. (Eng.Transl. 891-897).

[14] C. Christopher and C. Li, Limit Cycles of Differential Equations, Birkh\"auser Verlag, 2007, Basel-Boston-Berlin.

[15] C. Christopher and N .G. Lloyd, Polynomial systems: A lower bound for the Hilbert numbers, Proc. Royal Soc. London Ser. A450(1995), 219-224.

[16] C. J. Christopher and S. Lynch, Small-amplitude limit cycle bifurcations for Li¨¦nard systems with quadratic or cubic damping or restoring forces, Nonlinearity, 12 (1999), 1099-1112.

[17] B. Coll, C. Li and R. Prohence, Quadratic perturbations of a class of quadratic reversible systems with two centers. Disc. & Contin. Dyn. Sys. 24 (2009), 699-729.

[18] W. A. Coppel, Some quadratic systems with at most one limit cycle, in U. Kirchgraber and H. O. Walther, eds., Dynamics Reported, Vol. 2, Wiley/ Teubner, New York, Stuttgart, 1988, 61-68.

[19] F. Dumortier and C. Li, Quadratic Li¨¦nard equations with quadratic damping, J. Differential Equations, 139 (1997), 41-59.

[20] F. Dumortier and C. Li, On the uniqueness of limit cycles surrounding one or more singularities for Li¨¦nard equations, Nonlinearity, 9(1996), 1489-1500.

[21] F. Dumortier and C. Li, Perturbation from an elliptic Hamiltonian of degree four: (IV) Figure eight-loop. J. Diff. Eqns. 188(2003), 512-554.

[22] F. Dumortier, C. Li and Z. Zhang, [Unfolding][20] of a quadratic integrable system with two centers and two unbounded heteroclinic loops. J. Diff. Eqns. 139(1997),146-193.

[23] F. Dumortier, D. Panazzolo, and R. Roussarie, More limit cycles than expected in Li\'enard equations, Proc. Amer. Math. Soc., 135:6 (2007), 1895-1904.

[24] F. Dumortier, R. Roussarie and C. Rousseau, Elementary graphics of cyclicity 1 and 2, Nonlinearity 7(1994), 1001-1043.

[25] F. Dumortier, R. Roussarie and J. Sotomayor, Generic 3-parameter family of vector fields on the plane, unfolding a singularity with nilpotent linear part. The cusp case of codimension 3. Ergod. Theor. & Dyn. Sys. 7 (1987), 375-413.

[26] F. Dumortier, R. Roussarie and J. Sotomayor, Generic 3-parameter families of planar vector fields: Unfoldings of saddle, focus and elliptic singularites with nilpotent linear parts. Lecture Notes in Math. 1480, Springer-Verlag Berlin Heidelberg, 1991, 1-164.

[27] J. \({\rm \acute{E}}\)calle, Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac, Actualiti\'ees Math., Hermann, Paris, 1992.

[28] W. W. Farr, C. Li, I. S. Labouriau and W. F. Langford, Degenerate Hopf bifurcation formulas and Hilbert 16-th problem. SIAM J. Math. Anal., 20 (1989), 13-30.

[29] Y. Gao, Y. Wu and L. Tian, Bifurcation of limit cycles in a perturbed quintic Hamiltonian system with six double homoclinic loops. Acta Math. Appl. Sin. Engl. Ser. 24:2(2008), 313-328.

[30] L. Gavrilov, The infinitesimal 16th Hilbert problem in the quadratic case. Invent. Math. 143 (2001), 449-497.

[31] L. Gavrilov and I. D. Iliev, Second order analysis in polynomially perturbed reversible quadratic Hamiltonian systems. Erg. Th. & Dyn. Syst. 20 (2000), 1671-1686.

[32] M. Han, Cyclicity of planar homoclinic loops and quadratic integrable systems. Sci. China Ser. A 40(12) (1997), 1247-1258.

[33] M. Han, Cyclicity of planar homoclinic loops and quadratic integrable systems. Sci. China Ser. A 40(12)(1997), 1247-1258.

[34] M. Han, Liapunov constants and Hopf cyclicity of Liénard systems, Ann. of Diff. Eqs. 15:2(1999), 113-126.

[35] M. Han, On Hopf cyclicity of planar systems. J. Math. Anal. Appl. 245(2) (2000), 404-422.

[36] M. Han, Lower bounds for the Hilbert number of polynomial systems. Preprint, 2008.

[37] M. Han and J. Chen, The number of limit cycles bifurcating from a pair of homoclinic loops. Sci. China Ser. A 30(5)(2000), 401-414.

[38] M. Han, J. Jiang and H. Zhu, Limit cycle bifurcations in near-Hamiltonian systems by perturbing a nilpotent center. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 18(10) (2008), 3013-3027.

[39] M. Han, D. Shang, Z. Wang and P. Yu, Bifurcation of limit cycles in a fourth-order near-Hamiltonian system. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 17:11 (2007), 4117-4144.

[40] M. Han, Z. Wang and H. Zang, Limit cycles by Hopf and homoclinic bifurcations for near-Hamiltonian systems. (Chinese) Chinese Ann. Math. Ser. A 28 (2007), no. 5, 679-690; translation in Chinese J. Contemp. Math. 28 (2007), no. 4, 423-434.

[41] M. Han and Y. Wu, The stability of double homoclinic loops. Appl. Math. Lett. 17:11(2004), 1291-1298.

[42] M. Han, Y. Wu and P. Bi, Bifurcation of limit cycles near polycycles with \(n\) vertices. Chaos [Solitons][21] [Fractals][22] 22:2 (2004), 383-394.

[43] M. Han, Y. Wu and P. Bi, A new cubic system having eleven limit cycles. Discrete Contin. Dyn. Syst. 12:4(2005), 675-686.

[44] M. Han, J. Yang, T.A. Alina and Y. Gao, Limit cycles near homoclinic and heteroclinic loops. J. Dynam. Differential Equations 20(4) (2008), 923-944.

[45] M. Han and C. Yang, On the cyclicity of a 2-polycycle for quadratic systems. Chaos, Solitons Fract. 23(2005), 1787-1794.

[46] M. Han, J. Yang and P. Yu, Hopf bifurcations for near-Hamiltonian systems, to appear in IJBC.

[47] M. Han, Y. Ye and D. Zhu, Cyclicity of homoclinic loops and degenerate cubic Hamiltonians. Sci. China Ser. A 42:6(1999), 605-617.

[48] M. Han, H. Zang and J. Yang, Limit cycle bifurcations by perturbing a cuspidal loop in a Hamiltonian system. J. Differential Equations 246(1)(2009), 129-163.

[49] M. Han and T. Zhang, Some bifurcation methods of finding limit cycles. Math. Biosci. Eng. 3(1)(2006), 67-77

[50] M. Han, T. Zhang and H. Zang, Bifurcation of limit cycles near equivariant compound cycles. Sci. China Ser. A 50:4 (2007), 503-514.

[51] M. Han and H. Zhu, The loops qualities and bifurcations of homoclinic loops. J. Diff. Eqns. 234 (2007), 339-359

[52] Y. He and C. Li, On the number of limit cycles arising from perturbations of homoclinic loops of quadratic integrable systems. Planar nonlinear dynamical systems (Delft, 1995). Differential Equations Dynam. Systems 5(3-4) (1997), 303-316.

[53] D. Hilbert, Mathematical problems. M. Newton, Transl. Bull. Amer. Math. Soc. 8 (1902), 437-479. reprinted, Bull. Amer. Math. Soc. (N.S.) 37 (2000), 407-436.

[54] E. Horozov and I.D. Iliev, On saddle-loop bifurcations of limit cycles in perturbations of quadratic Hamiltonian systems. J. Differential Equations 113(1) (1994), 84-105.

[55] E. Horozov and I. D. Iliev, On the number of limit cycles in perturbations of quadratic Hamiltonian systems. Proc. London Math. Soc. 69 (1994), 198-224.

[56] I. D. Iliev, High-order Melnikov functions for degenerate cubic Hamiltonians. Adv. Diff. Eqns. 1 (1996), 689-708.

[57] I. D. Iliev, The cyclicity of the period annulus of the quadratic Hamiltonian triangle. J. Diff. Eqns. 128 (1996), 309-326.

[58] I. D. Iliev, Perturbations of quadratic centers. Bull. Sci. Math. 122 (1998), 107-161.

[59] Yu. S. Ilyashenko, Appearance of limit cycles by perturbation of the equation \(dw/dz=Rz/Rw\ ,\) where \(R(z,w)\) is a polynomia. Mat. Sbornik (New Series) 78 (120) (1969), 360-373.

[60] Yu. S. Ilyashenko, Finiteness theorems for limit cycles, Uspekhi Mat. Nauk 45 (1990), no. 2(272), 143-200 (Russian); English transl. Russian Math. Surveys 45 (1990), 129-203.

[61] J. Jiang, M. Han, P. Yu and S. Lynch, Limit cycles in two types of symmetric Li¨¦nard systems, Internat. J. Bifurcation Chaos, 17:6 (2007), 2169-2174.

[62] Q. Jiang and M. Han, Melnikov functions and perturbation of a planar Hamiltonian system. Chin. Ann. Math. Ser. B 20(2) (1999), 233-246.

[63] P. Joyal and C. Rousseau, Saddle quantities and applications. J. Differential Equations 78(2) (1989), 374-399.

[64] A. G. Khovansky, Real analytic manifolds with finiteness properties and complex Abelian integrals, Funct. Anal. Appl. 18 (1984), 119-128.

[65] C. Li, Non existence of limit cycles around a weak focus of order three for any quadratic system, Chin. Ann. Math. Ser. B 7(2)(1986), 174-190. (Chinese summary in Chin. Ann. MAth. Ser. A 7,no.2, 239).

[66] C. Li, C. Liu and J. Yang, A cubic system with thirteen limit cycles, J. Diff. Eqns. 246 (2009), 3609-3619.

[67] C. Li and J. Llibre, A unified study on the cyclicity of period annulus of the reversible quadratic Hamiltonian systems. J. Dyn. and Diff. Eqns. 16 (2004), 271-295.

[68] C. Li, P. Mardesic and R. Roussarie, Perturbations of symmetric elliptic Hamiltonians of degree four. J. Diff. Eqns. 231 (2006), 78-91.

[69] C. Li and C. Rousseau, A system with three limit cycles appearing in a Hopf bifurcation and dying in a homoclinic bifurcation, the cusp of order 4. J. Diff. Eqns. 79 (1989), 132-167.

[70] C. Li and Z. Zhang, A criterion for determining the monotonicity of ratio of two Abelian integrals. J. Diff. Eqns. 124 (1996), 407-424.

[71] C. Li and Z.-H. Zhang, Remarks on 16th weak Hilbert problem for \(n=2\ .\) Nonlinearity 15 (2002), 1975-1992.

[72] Chongxiao Li, The global bifurcation on the nonlinear oscillator \(\ddot{x}+(a_1+2a_2x+ 3a_3x^2)\dot{x} + b_1x+b_2x^2 = 0\ ,\) J. Yunnan Polytechnic University 1986, No. 2, 18-29.

[73] J. Li, Hilbert's 16th problem and bifurcations of planar vector fields, Inter. J. Bifur. and Chaos 13 (2003), 47-106.

[74] J. Li, H. Chan and K. Chung, Bifurcations of limit cycles in a Z6.equivariant planar vector field of degree 5, Sci. in China Ser. A 45 (7)(2002), 817-826.

[75] J. Li, H. Chan and K. Chung, Investigations of bifurcations of limit cycles in a \(Z_2\)-equivariant planar vector field of degree 5, Int. J. Bifurcation and Chaos, 12(10)(2002), 2137-2157.

[76] J. Li, H. Chan and K. Chung, Some lower bounds for \(H(n)\) in Hilbert's 16th problem, Qualitative Theory of Dynamical Systems, 3(2003), 345-360.

[77] J. Li and Q. Huang, Bifurcations of limit cycles forming compound eyes in the cubic system,¡± Chin. Ann. Math., 8B(1987), 391-403.

[78] J. Li and Y. Lin, Global bifurcations in a perturbed cubic system with Z2.symmetry, Acta Math. Appl. Sinica (English Ser.) 8(2)(1992), 131-143.

[79] J. Li and Y. Liu, New results on the study of \(Z_q\)-equivariant planar polynomial vector fields, to appear in Qualitative Theory of Dynamical Systems.

[80] J. Li and M. Zhang, Bifurcations of limit cycles of Z8-equivariant planar vector field of degree 7, J.Dynamics And Differentil Equations, 16(4)(2004),1123- 1139.

[81] J. Li and H. Zhou, On the Control of Parameters of Distributions of Limit Cycles for a \(Z_2\)-Equivariant Perturbed Planar Hamiltonian Polynomial Vector Field, Int. J. Bifurcation and Chaos, 15(1)(2004), 137-155.

[82] J. Li and M. Zhang, Bifurcations of limit cycles in a \(Z_2\)-equivariant planar polynomial vector field of degree 7, Int. J. Bifurcation and Chaos, 16(2006), 925-943.

[83] J. Li, M. Zhang and S. Li, Bifurcations of limit cycles in a \(Z_2\)-equivariant planar polynomial vector field of degree 7, Int. J. Bifurcation and Chaos 16:4(2006), 925-943.

[84] J. Li and X. Zhao, Rotation symmetry groups of planar Hamiltonian systems. Ann. Differential Equations 5(1) (1989), 25-33.

[85] W. Li, Theory of [Normal Forms][23] and its Applications. Science Press, Beijing, 2000 (Chinese).

[86] A. Li\({\rm \acute{e}}\)nard, \({\rm \acute{e}}\)tude des oscillations entrenues, Rev. G\({\rm \acute{e}}\)n. \({\rm \acute{e}}\)lectricit\({\rm \acute{e}}\ ,\) 23 (1928), 946-954.

[87] A. Lins, W. de Melo, and C. Pugh, On Li¨¦nards equation with linear damping, in J. Palis and M. do Carno, eds., Geometry and Topology, Lecture Notes in Mathematics, Vol. 597, Springer-Verlag, Berlin, 1977, 335-357.

[88] D. Luo, X. Wang, D. Zhu and M. Han, Bifurcation theory and methods of dynamical systems, Advanced Series in Dynamical Systems 15, World Scientic Publishing Co., Inc., River Edge, NJ, 1997.

[89] N.T. Otrokov, On the number of limit cycles of a differential equation in a neighbourhood of a singular point (in Russian), Mat. Sb. 34(1954), 127-144.

[90] I. G. Petrovskii and E. M. Landis, On the number of limit cycles of the equation \(\frac{dy}{dx}=\frac{P(x,y)}{Q(x,y)}\) where P and Q are polynomials of the 2nd degree, Mat. Sbornik (N.S) 37(79), 209-250, 1955. (There is an early announcement in D.A.N. SSSR (NS)102, 29-35, 1955.) Translated into English by Edwin Hewitt and published as AMS Translations, Series 2, Vol. 10, 177-221, 1958.

[91] J. Reyn, [Phase portraits][24] of planar quadratic systems. Mathematics and Its Applications (Springer), 583. Springer, New York, 2007.

[92] R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix loop of planar vector fields. Bol. Soc. Brasil. Mat. 17(2)(1986), 67-101.

[93] G. S. Ryckov, The limit cycles of the equation \(u(x+l)du=(x+ax^2-hbxy -hcu+du^2)dx\ ,\) (Russian), Diff. Uravn. 8(1972), 2257-2259. (Engl.Transl. 1748-1750).

[94] D. Schlomiuk, Algebraic and geometric aspects of the theory of polynomial vector fields. in ``Bifurcations and Periodic Orbits of Vector Fields*(Montreal, PQ, 1992), 429-467, Kluwer Acad. Publ.*Dordrecht, 1993.

[95] D. Schlomiuk (ed.), Bifurcations and Periodic Orbits of Vector Fields. Kluwer Acad. Publ., Dordrecht, 1993.

[96] D. Schlomiuk, Aspects of planar polynomial vector fields: global versus local, real versus comples, analytic versus algebraic and geometric, In ¡°Normal Forms and Bifurcations and Finiteness Problem in Differential Equations¡± (Montreal 2002), Yu. Ilyashenko and C. Rousseau eds., NATO Sci. Ser. II Math. Phys. Chem.Vol 134, Kluwer Acad. Publ., Dordrecht, 2004, 471-509.

[97] S. Shi, A concrete example of the existence of four limit cycles for plane quadratic systems, Scientia Sinica, 23(2)(1980), 153-158. Appeared in Chinese in Sc. Sin. Vol. 11, 1051-1056.

[98] F. Takens, Forced oscillations and bifurcations: Applications of global analysis. In Commun. Math. Vol 3, Inst. Rijksuniv. Utrecht., 1974; also in ``Global Analysis of Dynamical Systems", Edited by H.W.Broer, B.Krauskopf and G.Vegter, IOP Publishing Ltd, London, 2001.

[99] C. Tung, Positions of limit cycles of the system \(dx/dt=\sum\limits_{0\leq i+k\leq 2} a_{ik}x^iy^k,\) \(dy/dt=\sum\limits_{0\leq i+k\leq 2} b_{ik}x^iy^k\ .\) Sci. Sinica, 8 (1959), 151-171.

[100] B. van der Pol, On relaxation oscillations, Philos. Magazine, 7 (1926), 901-912, 946-954.

[101] S. Wang and P. Yu, Bifurcation of limit cycles in a quintic Hamiltonian system under a sixth-order perturbation. Chaos Solitons Fractals 26:5(2005), 1317-1335.

[102] Y. Wu, Y. Gao and M. Han, Bifurcations of the limit cycles in a \(Z_3\)-equivariant quartic planar vector field. Chaos Solitons Fractals 38:4(2008), 1177-1186.

[103] Y. Wu, Y. Gao and M. Han, On the number and distributions of limit cycles in a quintic planar vector field. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 18:7 (2008), 1939-1955.

[104] Y. Wu and M. Han, On the bifurcations of a Hamiltonian having three homoclinic loops under \(Z_3\) invariant quintic perturbations. Acta Math. Sin. (Engl. Ser.) 23:5 (2007), 869-878.

[105] Y.Wu and M. Han, New configurations of 24 limit cycles in a quintic system. Comput. Math. Appl. 55:9(2008), 2064-2075.

[106] Y. Wu, M. Han and X. Chen, On the bifurcation of double homoclinic loops of a cubic system. Nonlinear Anal. 68:8(2008), 2487-2494.

[107] Y. Wu, L. Tian and M. Han, On the limit cycles of a quintic planar vector field. Sci. China Ser. A 50:7(2007), 925-940.

[108] A. N. Varchenko, An estimate of the number of zeros of an Abelian integral depending on a parameter and limiting cycles, Funct. Anal. Appl. 18 (1984), 98-108.

[109] J. Yang and M. Han, Limit cycles near a double homoclinic loop. Ann. Differential Equations 23:4 (2007), 536-545.

[110] J. Yang, M. Han, V.G. Romanovski, Limit cycle bifurcations of some Li\({\rm \acute{e}}\)nard systems, Preprint(2009).

[111] X. Yang and Y. Ye, Uniqueness of limit cycle of the equation \(dx/dt = -y+dx+ lx^2 +xy +ny^2, dy/dt = x\ ,\) J. Fuzhou Univ., (2)(1978), 122-127 (Chinese).

[112] Y. Ye and others, Theory of Limit Cycles, Transl. Math. Monographs, Vol. 66 Amer. Math. Soc., Providence RI, 1986.

[113] P. Yu and R. Corless, Symbolic computation of limit cycles associated with Hilbert¡¯s 16th problem. Communications in Nonlinear Science and Numerical Simulation 14(12), 4041-4056, 2009.

[114] P. Yu and M. Han, Small limit cycles bifurcating from fine focus points in cubic order \(Z_2\)-equivariant vector fields. Chaos, Solitons and Fractals 24, 329-348, 2005.

[115] P. Yu and M. Han, Twelve limit cycles in a cubic order planar system with \(Z_2\)-symmetry. Communications on Pure and Applied Analysis 3, 515-526, 2004.

[116] P. Yu and M. Han, Twelve limit cycles in a cubic case of the 16th Hilbert problem. Int. J. Bifurcation and Chaos 15(7), 2191-2205, 2005.

[117] P. Yu, M. Han, Limit cycles in generalized \({\rm Li\acute{e}nard}\) systems, Chaos, Solitons and Fractals, 30:5(2006), 1048-1068.

[118] H. Zang, M. Han and D. Xiao, On Melnikov functions of a homoclinic loop through a nilpotent saddle for planar near-Hamiltonian systems. J. Differential Equations 245(4) (2008), 1086-1111.

[119] P. Zhang, On the uniqueness of limit cycle and stability of separatrix cycles for a quadratic system with a weak saddle, Northeastern Mathematical Journal, 6(2)(1990), 243-252.

[120] P. Zhang, Uniqueness of the limit cycles of quadratic systems with a second order weak focus,(Chinese),Acta Math.Sinica 41(2)(1999), 289-304.

[121] P. Zhang, On the distribution and number of limit cycles for quadratic systems with two foci. Acta Math. Sinica 44 (2001), 37-44 (Chinese).

[122] P. Zhang, On the distribution and number of limit cycles for quadratic systems with two foci. Qual. Theory Dyn. Syst. 3 (2002), 437-463.

[123] P. Zhang and S. Cai, Quadratic systems with second and third order weak saddle points, (Chinese), Acta Math. Sinica 30(4)(1987), 560-565.

[124] Z. Zhang and C. Li, On the number of limit cycles of a class of quadratic Hamiltonian systems under quadratic perturbations. Res. Rep. 33 (1993); Adv. Math. 26(5) (1997), 445-460.

[125] Z. Zhang, Proof of the uniqueness theorem of limit cycles of generalized Li\({\rm \acute{e}}\)nard equations, Appl. Anal. 23 (1986) 1-2, 63-76.

[126] Z. Zhang, T. Ding, W. Huang and Z. Dong, Qualitative Theory of Differential Equations, Translation of Mathematical Monographs, Vol. 102, American Mathematical Society, Providence, RI, 1992.

[127] Y. Zhao, Z. Liang and G. Lu, The cyclicity of period annulus of the quadratic Hamiltonian systems with non-Morsean point. J. Diff. Eqns. 162 (2000), 199-223.

[128] Y. Zhao and S. Zhu, Perturbations of the non-generic quadratic Hamiltonian vector fields with hyperbolic segment. Bull.\,Sci.\,Math. 125 (2001), 109-138.

[129] D. Zhu, A general property of the quadratic differential systems. Chinese Ann. Math. Ser. B 10(1) (1989), 26-32.

[130] H. Zoladek, The cyclicity of triangles and segments in quadratic systems, Journal of Differential Equations, 122(l)(1995), 137-159.

**Internal references**

- Yuri A. Kuznetsov (2006) [Andronov-Hopf bifurcation][25]. [Scholarpedia][26], 1(10):1858.

- Jan A. Sanders (2006) [Averaging][17]. Scholarpedia, 1(11):1760.

- John Guckenheimer (2007) [Bifurcation][13]. Scholarpedia, 2(6):1517.

- James Meiss (2007) [Dynamical systems][27]. Scholarpedia, 2(2):1629.

- James Meiss (2007) [Hamiltonian systems][28]. Scholarpedia, 2(8):1943.

- Jeff Moehlis, Kresimir Josic, Eric T. Shea-Brown (2006) [Periodic orbit][29]. Scholarpedia, 1(7):1358.

- Philip Holmes and Eric T. Shea-Brown (2006) [Stability][11]. Scholarpedia, 1(10):1838.

- Takashi Kanamaru (2007) [Van der Pol oscillator][12]. Scholarpedia, 2(1):2202.

Sponsored by: [Eugene M. Izhikevich, Editor-in-Chief of Scholarpedia, the peer-reviewed open-access encyclopedia][4] |

[Reviewed by][30]: [Anonymous][31] |

Accepted on: [2010-07-06 09:35:51 GMT][32] |

Retrieved from " [http://www.scholarpedia.org/w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&oldid=137138][33] "

[Categories][34]:

- [Dynamical Systems][35]
- [Multiple Curators][36]

##### Personal tools

- [Log in][37]

##### Namespaces

- [Page][38]
- [Discussion][39]

####

##### Variants

##### Views

- [Read][38]
- [View source][40]
- [View history][41]

##### Actions

##### Search

[42]

##### Navigation

- [Main page][42]
- [About][43]
- [Propose a new article][44]
- [Instructions for Authors][45]
- [Random article][46]
- [FAQs][47]
- [Help][48]

##### Focal areas

- [Astrophysics][49]
- [Celestial mechanics][50]
- [Computational neuroscience][51]
- [Computational intelligence][52]
- [Dynamical systems][53]
- [Physics][54]
- [Touch][55]
- [More topics][56]

##### Activity

- [Recently published articles][57]
- [Recently sponsored articles][58]
- [Recent changes][59]
- [All articles][60]
- [List all Curators][61]
- [List all users][62]
- [Scholarpedia Journal][63]

##### Tools

- [What links here][64]
- [Related changes][65]
- [Special pages][66]
- [Printable version][67]
- [Permanent link][68]

- [69]
- [70]
- [71]
- [72]

- [image: Powered by MediaWiki] [73][image: Powered by MathJax] [74][image: Creative Commons License] [75]

- This page was last modified on 26 October 2013, at 17:02.
- This page has been accessed 70,154 times.
- "Limit cycles of planar polynomial vector fields" by [Maoan Han, Chengzhi Li and Jibin Li][76] is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License][75]. Permissions beyond the scope of this license are described in the [Terms of Use][77]

- [Privacy policy][78]
- [About Scholarpedia][43]
- [Disclaimers][79]


## Links

[1]: http://dx.doi.org/10.4249/scholarpedia.9648
[2]: /w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;action=cite&amp;rev=137138
[3]: /article/User:Chengzhi_Li
[4]: /article/User:Eugene_M._Izhikevich
[5]: /article/User:Maoan_Han
[6]: /article/User:Nick_Orbeck
[7]: /article/User:Jibin_Li
[8]: /article/User:Benjamin_Bronner
[9]: /article/Periodic_Orbit
[10]: /article/Dynamical_Systems
[11]: /article/Stability
[12]: /article/Van_der_Pol_oscillator
[13]: /article/Bifurcation
[14]: /article/Andronov-Hopf_Bifurcation
[15]: /article/Hamiltonian_Systems
[16]: /article/Hamiltonian
[17]: /article/Averaging
[18]: /article/Resonance
[19]: /article/Equilibrium
[20]: /article/Unfoldings
[21]: /article/Soliton
[22]: /article/Fractals
[23]: /article/Normal_Forms
[24]: /article/State_Space
[25]: /article/Andronov-Hopf_bifurcation
[26]: /article/Scholarpedia
[27]: /article/Dynamical_systems
[28]: /article/Hamiltonian_systems
[29]: /article/Periodic_orbit
[30]: //www.scholarpedia.org/w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;oldid=74348
[31]: /article/User:Anonymous
[32]: //www.scholarpedia.org/w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;oldid=78466
[33]: http://www.scholarpedia.org/w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;oldid=137138
[34]: /article/Special:Categories
[35]: /article/Category:Dynamical_Systems
[36]: /article/Category:Multiple_Curators
[37]: /w/index.php?title=Special:UserLogin&amp;returnto=Limit+cycles+of+planar+polynomial+vector+fields
[38]: /article/Limit_cycles_of_planar_polynomial_vector_fields
[39]: /article/Talk:Limit_cycles_of_planar_polynomial_vector_fields
[40]: /w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;action=edit
[41]: /w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;action=history
[42]: /article/Main_Page
[43]: /article/Scholarpedia:About
[44]: /article/Special:ProposeArticle
[45]: /article/Scholarpedia:Instructions_for_Authors
[46]: /article/Special:Random
[47]: /article/Help:Frequently_Asked_Questions
[48]: /article/Scholarpedia:Help
[49]: /article/Encyclopedia:Astrophysics
[50]: /article/Encyclopedia:Celestial_Mechanics
[51]: /article/Encyclopedia:Computational_neuroscience
[52]: /article/Encyclopedia:Computational_intelligence
[53]: /article/Encyclopedia:Dynamical_systems
[54]: /article/Encyclopedia:Physics
[55]: /article/Encyclopedia:Touch
[56]: /article/Scholarpedia:Topics
[57]: /article/Special:RecentlyPublished
[58]: /article/Special:RecentlySponsored
[59]: /article/Special:RecentChanges
[60]: /article/Special:AllPages
[61]: /article/Special:ListCurators
[62]: /article/Special:ListUsers
[63]: /article/Special:Journal
[64]: /article/Special:WhatLinksHere/Limit_cycles_of_planar_polynomial_vector_fields
[65]: /article/Special:RecentChangesLinked/Limit_cycles_of_planar_polynomial_vector_fields
[66]: /article/Special:SpecialPages
[67]: /w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;printable=yes
[68]: /w/index.php?title=Limit_cycles_of_planar_polynomial_vector_fields&amp;oldid=137138
[69]: https://twitter.com/scholarpedia
[70]: https://plus.google.com/112873162496270574424
[71]: http://www.facebook.com/Scholarpedia
[72]: http://www.linkedin.com/groups/Scholarpedia-4647975/about
[73]: https://www.mediawiki.org/
[74]: https://www.mathjax.org/
[75]: http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US
[76]: http://www.scholarpedia.org/article/Limit_cycles_of_planar_polynomial_vector_fields
[77]: http://www.scholarpedia.org/article/Scholarpedia:Terms_of_use
[78]: /article/Scholarpedia:Privacy_policy
[79]: /article/Scholarpedia:General_disclaimer
