<!-- source: https://encyclopediaofmath.org/wiki/Schubert_calculus | converted from HTML -->

Schubert calculus - Encyclopedia of Mathematics

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

# Schubert calculus

From Encyclopedia of Mathematics

Jump to: navigation, search

2020 Mathematics Subject Classification: *Primary:*[14M15][23] [[MSN][24]][[ZBL][25]]

The Schubert calculus or *Schubert enumerative calculus*is a formal calculus of symbols representing geometric conditions used to solve problems in enumerative geometry. This originated in work of M. Chasles [Ch] on conics and was systematized and used to great effect by H. Schubert in [Sc]. The justification of Schubert's enumerative calculus and the verification of the numbers he obtained was the contents of Hilbert's 15th problem (cf. also [Hilbert problems][26]).

Justifying Schubert's enumerative calculus was a major theme of twentieth century [algebraic geometry][27], and [intersection theory][28] provides a satisfactory modern framework. Enumerative geometry deals with the second part of Hilbert's problem. See [Fu2] for a complete reference on intersection theory; for historical surveys and a discussion of enumerative geometry, see [Kl], [Kl2].

The Schubert calculus also refers to mathematics arising from the following class of enumerative geometric problems: Determine the number of linear subspaces of projective space that satisfy incidence conditions imposed by other linear subspaces. For a survey, see [KlLa]. For example, how many lines in projective $3$-space meet $4$ given lines? These problems are solved by studying both the geometry and the cohomology or Chow rings of Grassmann varieties (cf. also [Chow ring][29]; [Grassmann manifold][30]). This field of Schubert calculus enjoys important connections not only to algebraic geometry and [algebraic topology][31], but also to algebraic combinatorics, representation theory, differential geometry, linear algebraic groups, and symbolic computation, and has found applications in numerical homotopy continuation [HuSoSt], linear algebra [Fu] and systems theory [By].

The Grassmannian $G_{m,n}$ of $m$-dimensional subspaces ($m$-planes) in $\def\P{\mathbb{P}}\P^n$ over a field $k$ has distinguished Schubert varieties

$$\def\O{\Omega}\def\a{\alpha}\O_{a_0,\dots,a_m}V_*:= \{W\in G_{m,n} : W\cap V_{a_j}\ge j\},$$ where $V_*:V_0\subset\cdots\subset V_n=\P^n$ is a [flag][32] of linear subspaces with $\dim V_j = j$. The [Schubert cycle][33] $\def\s{\sigma}\s_{a_0,\dots,a_n}$ is the cohomology class Poincaré dual to the fundamental homology cycle of $\O_{a_0,\dots,a_m} V_*$ (cf. also [Homology][34]). The basis theorem asserts that the Schubert cycles form a basis of the Chow ring $A^* G_{m,n}$ (when $k$ is the complex number field, these are the integral cohomology groups $H^* G_{m,n}$) of the Grassmannian with

$$\s_{a_0,\dots,a_m}\in A^{(m+1)(n+1)-{m+1\choose n+1} -a_0-\cdots -a_m} G_{m.n},$$ (see also [Grassmann manifold][30]). The duality theorem asserts that the basis of Schubert cycles is self-dual under the intersection pairing

$$\def\b{\beta} (\a,\b) \in H^* G_{m,n} \otimes H^* G_{m,n} \to\deg(\a \cdot \b) = \int_{G_{m,n}} \a\cdot\b$$ with $\s_{a_0,\dots,a_m}$ dual to $\s_{n-a_m,\dots,n-a_0}$.

Let $\def\t{\tau}\t_b := \s_{n-m-b,n-m+1,\dots,n}$ be a special Schubert cycle (cf. [Schubert cycle][33]). Then

$$\s_{a_0,\dots,a_m}\cdot \t_b = \sum \s_{c_0,\dots,c_m},$$ the sum running over all $(c_0,\dots,c_m)$ with $0\le c_0\le a_0\le c_1\le a_1\cdots\le c_m\le a_m$ and $b = \sum_i(a_i-c_i)$. This Pieri formula determines the ring structure of cohomology; an algebraic consequence is the Giambelli formula for expressing an arbitrary Schubert cycle in terms of special Schubert cycles. Define $\t_b = 0$ if $B<0$ or $B>m$, and $\t_0 = 1$. Then Giambelli's formula is

$$\s_{a_0,\dots,a_m} = \det(\t_{n-m+j-a_i})_{i,j=0,\dots,m}.$$ These four results enable computation in the Chow ring of the Grassmannian, and the solution of many problems in enumerative geometry. For instance, the number of $m$-planes meeting $(m+1)(n-m)$ general $(n-m-1)$-planes non-trivially is the coefficient of $\s_{0,\dots,m}$ in the product $(\t_1)^{(m+1)(n-m)}$, which is [Sc2] $$\frac{1!\cdots(n-m-1)!\cdots ((m+1)(n-m))!}{(n-m)!(n-m+1)!\cdots(n!-1)!}.$$ These four results hold more generally for cohomology rings of flag manifolds $G/P$; Schubert cycles form a self-dual basis, the Chevalley formula [Ch2] determines the ring structure (when $P$ is a [Borel subgroup][35]), and the Bernshtein–Gel'fand–Gel'fand formula [BeGeGe] and Demazure formula [De] give the analogue of the Giambelli formula. More explicit Giambelli formulas are provided by [Schubert polynomials][36].

One cornerstone of the Schubert calculus for the Grassmannian is the Littlewood–Richardson rule [LiRi] for expressing a product of Schubert cycles in terms of the basis of Schubert cycles. (This rule is usually expressed in terms of an alternative indexing of Schubert cycles using partitions. A sequence $(a_0,\dots,a_m)$ corresponds to the partition $(n-m-a_0,n-m+1,\dots,n-a_m)$; cf. [Schur functions in algebraic combinatorics][37].) The analogue of the Littlewood–Richardson rule is not known for most other flag varieties $G/P$.

#### References

[BeGeGe] | I.N. Bernshtein, I.M. Gel'fand, S.I. Gel'fand, "Schubert cells and cohomology of the spaces $G/P$" *Russian Math. Surveys*, **28**: 3 (1973) pp. 1–26 [MR0686277][38] |

[By] | C.I. Byrnes, "Algebraic and geometric aspects of the control of linear systems" C.I. Byrnes (ed.) C.F. Martin (ed.), *Geometric Methods in Linear systems Theory*, Reidel (1980) pp. 85–124  |

[Ch] | M. Chasles, "Construction des coniques qui satisfont à cinque conditions" *C.R. Acad. Sci. Paris*, **58**(1864) pp. 297–308  |

[Ch2] | C. Chevalley, "Sur les décompositions cellulaires des espaces $G/B$" W. Haboush (ed.), *Algebraic Groups and their Generalizations: Classical Methods*, *Proc. Symp. Pure Math.*, **56:1**, Amer. Math. Soc. (1994) pp. 1–23 [MR1278698][39] [Zbl 0824.14042][40] |

[De] | M. Demazure, "Désingularization des variétés de Schubert généralisées" *Ann. Sci. École Norm. Sup. (4)*, **7**(1974) pp. 53–88  |

[Fu] | W. Fulton, "Eigenvalues, invariant factors, highest weights, and Schubert calculus" *Bull. Amer. Math. Soc.*, **37**(2000) pp. 209–249 [MR1754641][41] [Zbl 0994.15021][42] |

[Fu2] | W. Fulton, "Intersection theory", *Ergebn. Math.*, **2**, Springer (1998) (Edition: Second) [MR1644323][43] [Zbl 0885.14002][44] |

[HuSoSt] | B. Huber, F. Sottile, B. Sturmfels, "Numerical Schubert calculus" *J. Symbolic Comput.*, **26**: 6 (1998) pp. 767–788 [MR1662035][45] [Zbl 1064.14508][46] |

[Kl] | S. Kleiman, "Problem 15: Rigorous foundation of Schubert's enumerative calculus", *Mathematical Developments arising from Hilbert Problems*, *Proc. Symp. Pure Math.*, **28**, Amer. Math. Soc. (1976) pp. 445–482 [MR429938][47] |

[Kl2] | S. Kleiman, "Intersection theory and enumerative geometry: A decade in review" S. Bloch (ed.), *Algebraic Geometry (Bowdoin, 1985)*, *Proc. Symp. Pure Math.*, **46:2**, Amer. Math. Soc. (1987) pp. 321–370 [MR0927987][48] [Zbl 0664.14031][49] |

[KlLa] | S.L. Kleiman, D. Laksov, "Schubert calculus" *Amer. Math. Monthly*, **79**(1972) pp. 1061–1082 [MR0323796][50] [Zbl 0272.14016][51] |

[LiRi] | D.E. Littlewood, A.R. Richardson, "Group characters and algebra" *Philos. Trans. Royal Soc. London.*, **233**(1934) pp. 99–141 [Zbl 0009.20203][52] [Zbl 60.0896.01][53] |

[Sc] | H. Schubert, "Kalkül der abzählenden Geometrie", Springer (1879) (Reprinted (with an introduction by S. Kleiman): 1979) [MR0555576][54] |

[Sc2] | H. Schubert, "Anzahl-Bestimmungen für lineare Räume beliebiger Dimension" *Acta Math.*, **8**(1886) pp. 97–118 [Zbl 18.0632.01][55] |

**How to Cite This Entry:**
Schubert calculus. *Encyclopedia of Mathematics.*URL: http://encyclopediaofmath.org/index.php?title=Schubert_calculus&oldid=23715

This article was adapted from an original article by Frank Sottile (originator), which appeared in Encyclopedia of Mathematics - ISBN 1402006098. [See original article][56]

Retrieved from " [https://encyclopediaofmath.org/index.php?title=Schubert_calculus&oldid=23715][57] "

[Categories][58]:

- [Algebra][59]
- [Algebraic geometry][60]
- [TeX done][61]

- This page was last edited on 30 March 2012, at 08:49.

- [Privacy policy][62]
- [About Encyclopedia of Mathematics][63]
- [Disclaimers][64]

- [Copyrights][65]
- [Impressum-Legal][66]

Manage Cookies


## Links

[1]: /
[2]: /index.php?title=Special:UserLogin&returnto=Schubert+calculus
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
[14]: /wiki/Special:WhatLinksHere/Schubert_calculus
[15]: /wiki/Special:RecentChangesLinked/Schubert_calculus
[16]: /wiki/Special:SpecialPages
[17]: /index.php?title=Schubert_calculus&amp;oldid=23715
[18]: /index.php?title=Schubert_calculus&amp;action=info
[19]: /wiki/Schubert_calculus
[20]: /index.php?title=Talk:Schubert_calculus&amp;action=edit&amp;redlink=1
[21]: /index.php?title=Schubert_calculus&amp;action=edit
[22]: /index.php?title=Schubert_calculus&amp;action=history
[23]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=14Mxx
[24]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=14M15
[25]: https://zbmath.org/classification/?q=14M15
[26]: /wiki/Hilbert_problems
[27]: /wiki/Algebraic_geometry
[28]: /wiki/Intersection_theory
[29]: /wiki/Chow_ring
[30]: /wiki/Grassmann_manifold
[31]: /wiki/Algebraic_topology
[32]: /wiki/Flag
[33]: /wiki/Schubert_cycle
[34]: /wiki/Homology
[35]: /wiki/Borel_subgroup
[36]: /wiki/Schubert_polynomials
[37]: /wiki/Schur_functions_in_algebraic_combinatorics
[38]: https://mathscinet.ams.org/mathscinet/article?mr=0686277
[39]: https://mathscinet.ams.org/mathscinet/article?mr=1278698
[40]: https://zbmath.org/?q=an%3A0824.14042
[41]: https://mathscinet.ams.org/mathscinet/article?mr=1754641
[42]: https://zbmath.org/?q=an%3A0994.15021
[43]: https://mathscinet.ams.org/mathscinet/article?mr=1644323
[44]: https://zbmath.org/?q=an%3A0885.14002
[45]: https://mathscinet.ams.org/mathscinet/article?mr=1662035
[46]: https://zbmath.org/?q=an%3A1064.14508
[47]: https://mathscinet.ams.org/mathscinet/article?mr=429938
[48]: https://mathscinet.ams.org/mathscinet/article?mr=0927987
[49]: https://zbmath.org/?q=an%3A0664.14031
[50]: https://mathscinet.ams.org/mathscinet/article?mr=0323796
[51]: https://zbmath.org/?q=an%3A0272.14016
[52]: https://zbmath.org/?q=an%3A0009.20203
[53]: https://zbmath.org/?q=an%3A60.0896.01
[54]: https://mathscinet.ams.org/mathscinet/article?mr=0555576
[55]: https://zbmath.org/?q=an%3A18.0632.01
[56]: http://encyclopediaofmath.org/index.php?title=Schubert_calculus&oldid=15371
[57]: https://encyclopediaofmath.org/index.php?title=Schubert_calculus&amp;oldid=23715
[58]: /wiki/Special:Categories
[59]: /wiki/Category:Algebra
[60]: /wiki/Category:Algebraic_geometry
[61]: /wiki/Category:TeX_done
[62]: /wiki/Encyclopedia_of_Mathematics:Privacy_policy
[63]: /wiki/Encyclopedia_of_Mathematics:About
[64]: /wiki/Encyclopedia_of_Mathematics:General_disclaimer
[65]: /index.php/Encyclopedia_of_Mathematics:Copyrights
[66]: /index.php/Encyclopedia_of_Mathematics:Legal
