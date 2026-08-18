<!-- source: https://encyclopediaofmath.org/wiki/Limit_cycle | converted from HTML -->

Limit cycle - Encyclopedia of Mathematics

[1]

- [Log in][2]

[www.springer.com][3] [The European Mathematical Society][4]

##### Navigation

- [Main page][5]
- [Pages A-Z][6]
- [StatProb Collection][7]
- [Recent changes][8]
- [Current events][9]
- [Random page][10]
- [Help][11]
- [Project talk][12]
- [Request account][13]

##### Tools

- [What links here][14]
- [Related changes][15]
- [Special pages][16]
- Printable version
- [Permanent link][17]
- [Page information][18]

##### Namespaces

- [Page][19]
- [Discussion][20]

##### Variants

##### Views

- [View][19]
- [View source][21]
- [History][22]

##### Actions

# Limit cycle

From Encyclopedia of Mathematics

Jump to: navigation, search

An *isolated*closed trajectory in the phase space of an [autonomous system][23] of ordinary differential equations. A limit cycle corresponds to a periodic non-constant solution of the system.

## Contents

- 1 Dynamics
- 2 Limit cycles of planar vector fields
- 3 Complex limit cycles
- 4 Hilbert 16th problem

  - 4.1 Notes
  - 4.2 References

### Dynamics

Limit cycles represent the simplest (after the steady states) type of behavior of a continuous time [dynamical system][24]. Theoretically all properties of limit cycles (their [stability][25] and [bifurcations][26]) can be reduced to investigation of the associated [Poincaré return map][27] [1]. In practice, however, the Taylor coefficients of the Poincare map can be obtained only in the form of integrals over the cycle, which may require some quite detailed knowledge of the shape of the cycle itself.

For instance, in the linear approximation if $\gamma:[0,T]\to\R^n$, $t\mapsto\gamma(t)$, is a limit cycle of period $T>0$ for the vector field $v(x)$ associated with the differential equation $\dot x=v(x)$, $x\in\R^n$, one obtains a linear (non-autonomous) system of differential equations $$ \dot z=A(t)z,\qquad z\in\R^n, \quad A(t)=\biggl(\frac{\partial v}{\partial x}(\gamma(t)\biggr),\ t\in [0,T]. $$ The corresponding *[Cauchy][28] -- [Floquet][29]*linear operator $M:\R^n\to\R^n$ maps a vector $a\in\R_n$ into the vector $Ma=z_a(T)$, where $z_a$ is the solution of the above system with the initial value $z_a(0)=a$. If this operator is [hyperbolic][30], i.e., has no modulus one eigenvalues (" [characteristic exponents][31] "), then the stability pattern of the cycle (dimensions of the corresponding stable and unstable [invariant manifolds][32]) is completely determined (and coincides with that of the iterations $M^k$, $k\in\Z$).

### Limit cycles of planar vector fields

On the two-dimensional sphere (and plane) the topological restrictions which forbid intersection of phase trajectories, make limit cycles the only possible limit motion not directly related to singular points (steady states, also known as stationary solutions). More precisely, if the $\Omega$-limit set of a non-periodic point $a\in \R^2$ [2] contains no singular point of the field $v$, then it must be a limit cycle ( [Poincare-Bendixson][33], 1886 [3], 1901 [4]).

If the presence of singular points cannot be excluded, the situation becomes slightly more complicate. Under the assumption of analyticity one can show that the only possible limit sets for vector fields on the sphere [5] are singular points, limit cycles and [separatrix polygons][34], also known as [polycycles][35], which consist of singular points and connecting them arcs of [separatrices][34].

For the same reasons [bifurcations][26] of limit cycles, topological changes of the number of limit cycles, are possible only in annular neighborhoods of existing (multiple) cycles, singular points or polycycles.

### Complex limit cycles

A polynomial planar vector field after [complexification][36] defines a holomorphic singular [foliation][37] $\mathscr F$ on the complex [projective plane][38] $\C P^2$. Solutions of the differential equation correspond to leaves of this foliation, yet unlike in the real case, the leaves are topologically two-dimensional and can have much richer topological structure.

A limit cycle after complexification corresponds to a nontrivial loop on a leaf of the foliation $\mathscr F$ with a non-identical [holonomy][39] map. This observation may motivate one of the possible generalizations of the notion of limit cycle for complex ordinary differential equations.

A *complex limit cycle*is a noncontractible closed loop on the leaf of a singular holomorphic foliation on $\C P^2$ with a non-identical holonomy. Note that according to this definition, the same leaf may carry many different limit cycles: for instance, generically the infinite line (with deleted singular points) is a multiply connected leaf of a polynomial foliation, and each small loop around the deleted singularity is a complex limit cycle. However, these limit cycles are [homologically dependent][40]: their sum is zero.

### Hilbert 16th problem

One of the most challenging problems which remains open for over 120 years, is the Hilbert's question on the number and position of limit cycles of a polynomial vector field on the plane ( [Problem 16, second part][41]). Despite considerable progress in the last 25 years, the only known general result states that each polynomial vector field may have only finitely limit cycles (independently Yu. Ilyashenko and J. Ecalle, 1991). It is not known whether this number is uniformly bounded over all polynomial fields of degree $\le d$, even for $d=2$ (fields of degree $1$ cannot exhibit limit cycles at all).

It is worth noting that the Hilbert 16th problem has no nontrivial complex version. A generic polynomial vector field after complexification has countably many homologically independent complex limit cycles, see [IY, Sect. 28C].

---

#### Notes

1. ↑ Sometimes also the terms *monodromy*or *holonomy*are used as synonyms to the "first return map".
2. ↑ A closed invariant subset of the plane, defined as $$ \Omega(a)=\bigcap_{T<+\infty}\overline{\{g^t(a)|t\ge T\}},\qquad g^t(a)=\text{the flow map, }\left.\frac{\rd g^t(a)}{\rd t}\right|_{t=0}=v(a). $$
3. ↑ H. Poincaré, *Memoire sur les courbes définiés par des équations différentielles*, J. de Math. , **7**(1881) pp. 375–422, ibid., **8**(1882) pp. 251–296, ibid., **1**(1885) pp. 167–244, ibid., **2**(1886) pp. 151–217.
4. ↑ I. Bendixson, *Sur les courbes définiés par des équations différentielles*, Acta Math., **24**(1901) pp. 1–88.
5. ↑ Polynomial vector fields on the plane also satisfy this assertion.

#### References

[E] | Écalle, J. *Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac*, Actualités Mathématiques. Hermann, Paris, 1992. [MR1399559][42] |

[H] | Hilbert, D. *Mathematical problems*Reprinted from Bull. Amer. Math. Soc. **8**(1902), 437–479. Bull. Amer. Math. Soc. (N.S.) 37 (2000), no. 4, 407--436. [MR1779412][43] |

[I91] | Ilyashenko, Yu. S. *Finiteness theorems for limit cycles*, Translations of Mathematical Monographs, **94**. American Mathematical Society, Providence, RI, 1991. [MR1133882][44] |

[I02] | Ilyashenko, Yu. *Centennial history of Hilbert's 16th problem*Bull. Amer. Math. Soc. (N.S.) **39**(2002), no. 3, 301--354. [MR1898209][45] |

[IY] | Ilyashenko, Yu. and Yakovenko, S. *Lectures on analytic differential equations*, Graduate Studies in Mathematics, **86**. American Mathematical Society, Providence, RI, 2008. [MR2363178][46] |

[R] | R. Roussarie, *Bifurcation of planar vector fields and Hilbert's sixteenth problem*, Birkhäuser (1998). [MR1628014][47].  |

**How to Cite This Entry:**
Limit cycle. *Encyclopedia of Mathematics.*URL: http://encyclopediaofmath.org/index.php?title=Limit_cycle&oldid=54065

This article was adapted from an original article by L.A. Cherkas (originator), which appeared in Encyclopedia of Mathematics - ISBN 1402006098. [See original article][48]

Retrieved from " [https://encyclopediaofmath.org/index.php?title=Limit_cycle&oldid=54065][49] "

[Category][50]:

- [TeX done][51]

- This page was last edited on 1 October 2023, at 09:14.

- [Privacy policy][52]
- [About Encyclopedia of Mathematics][53]
- [Disclaimers][54]

- [Copyrights][55]
- [Impressum-Legal][56]

Manage Cookies


## Links

[1]: /
[2]: /index.php?title=Special:UserLogin&returnto=Limit+cycle
[3]: http://www.springer.com
[4]: http://www.euro-math-soc.eu/
[5]: /wiki/Main_Page
[6]: /wiki/Special:AllPages
[7]: /wiki/Category:Statprob
[8]: /wiki/Special:RecentChanges
[9]: /wiki/Encyclopedia_of_Mathematics:Current_events
[10]: /wiki/Special:Random
[11]: /wiki/Help:Contents
[12]: /wiki/Talk:EoM:This_project
[13]: /wiki/Special:RequestAccount
[14]: /wiki/Special:WhatLinksHere/Limit_cycle
[15]: /wiki/Special:RecentChangesLinked/Limit_cycle
[16]: /wiki/Special:SpecialPages
[17]: /index.php?title=Limit_cycle&amp;oldid=54065
[18]: /index.php?title=Limit_cycle&amp;action=info
[19]: /wiki/Limit_cycle
[20]: /index.php?title=Talk:Limit_cycle&amp;action=edit&amp;redlink=1
[21]: /index.php?title=Limit_cycle&amp;action=edit
[22]: /index.php?title=Limit_cycle&amp;action=history
[23]: /wiki/Autonomous_system
[24]: /wiki/Dynamical_system
[25]: /wiki/Stability
[26]: /wiki/Bifurcation
[27]: /wiki/Poincar%C3%A9_return_map
[28]: /wiki/Cauchy_operator
[29]: /wiki/Floquet_theory
[30]: /wiki/Hyperbolic_point
[31]: /wiki/Characteristic_exponent
[32]: /index.php?title=Invariant_manifolds&amp;action=edit&amp;redlink=1
[33]: /wiki/Poincare-Bendixson_theory
[34]: /wiki/Separatrix
[35]: /index.php?title=Polycycle&amp;action=edit&amp;redlink=1
[36]: /index.php?title=Complexification&amp;action=edit&amp;redlink=1
[37]: /wiki/Foliation
[38]: /wiki/Projective_plane
[39]: /index.php?title=Holonomy&amp;action=edit&amp;redlink=1
[40]: /wiki/Homology
[41]: /wiki/Hilbert_problems#Hilbert.27s_sixteenth_problem.
[42]: https://mathscinet.ams.org/mathscinet/article?mr=1399559
[43]: https://mathscinet.ams.org/mathscinet/article?mr=1779412
[44]: https://mathscinet.ams.org/mathscinet/article?mr=1133882
[45]: https://mathscinet.ams.org/mathscinet/article?mr=1898209
[46]: https://mathscinet.ams.org/mathscinet/article?mr=2363178
[47]: https://mathscinet.ams.org/mathscinet/article?mr=1628014
[48]: http://encyclopediaofmath.org/index.php?title=Limit_cycle&oldid=15601
[49]: https://encyclopediaofmath.org/index.php?title=Limit_cycle&amp;oldid=54065
[50]: /wiki/Special:Categories
[51]: /wiki/Category:TeX_done
[52]: /wiki/Encyclopedia_of_Mathematics:Privacy_policy
[53]: /wiki/Encyclopedia_of_Mathematics:About
[54]: /wiki/Encyclopedia_of_Mathematics:General_disclaimer
[55]: /index.php/Encyclopedia_of_Mathematics:Copyrights
[56]: /index.php/Encyclopedia_of_Mathematics:Legal
