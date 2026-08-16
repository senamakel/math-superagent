<!-- source: https://arxiv.org/html/2604.20120v1 | converted from HTML -->

Combinatorial Geometry of Erdős–Szekeres Type Problems: SAT/ASP Modeling and Linear Subreduction

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2604.20120v1 [math.CO] 22 Apr 2026

# Combinatorial Geometry of Erdős–Szekeres Type Problems: SAT/ASP Modeling and Linear Subreduction

Vitalii Koshelev Alexey Koshka Affiliation: Independent Researchers, e-mail: koshelev@mccme.ru, biocheshire@yandex.ru

###### Abstract

This paper investigates several classical and novel variations of the Erdős–Szekeres problem, including multicolored point sets, convex hexagons with a given number of interior points, and polygons with constraints on edge colors. We propose a comprehensive computational framework combining combinatorial modeling within the SAT/ASP paradigms with the geometric realization of configurations. To determine point coordinates, we developed the linear subreduction method. The core idea consists of combining the complete logical model of the problem with a system of geometric inequalities, followed by fixing the abscissae to linearize the constraints. This approach enables a simultaneous search for a realization across the entire space of admissible abstract configurations (signotopes) rather than examining them individually, while linearization significantly accelerates the SMT solving process. Using this framework, we established new exact values for several functions; in particular, we proved h n ​ c ​ ( 4, 0, 4, 0) = 26 h_{nc}(4,0;4,0)=26: any bicolored set of 26 points in general position must contain the vertices of an empty monochromatic quadrilateral.

Keywords: Erdős–Szekeres problem, combinatorial geometry, Answer Set Programming, linear subreduction, signotopes, SMT solving.

## 1 Introduction and Statement of Results

In 1935, Erdős and Szekeres formulated the following problem (see [1], [2]).

The First Erdős–Szekeres Problem. For any integer n ⩾ 3 n\geqslant 3, find the smallest positive integer g ⁡ ( n) g(n) such that any set of at least g ⁡ ( n) g(n) points in the plane in general position contains a subset of n n points that form the vertices of a convex n n -gon.

Recall that a set of points is in general position if no three of its elements are collinear.

In 1978, Erdős proposed a modification of the first problem (see [3]).

The Second Erdős–Szekeres Problem. For any integer n ⩾ 3 n\geqslant 3, find the smallest positive integer h ⁡ ( n) h(n) such that any set 𝒳 {\cal X} of at least h ⁡ ( n) h(n) points in the plane in general position contains a subset of n n points that form the vertices of a convex and empty n n -gon, i.e., an n n -gon containing no points of 𝒳 {\cal X} in its interior.

These problems are classical in combinatorial geometry and Ramsey theory (see [4], [5], [6], [7]). Both can be generalized as follows.

The Third Erdős–Szekeres-type Problem. For any integers n ⩾ 3 n\geqslant 3 and k ⩾ 0 k\geqslant 0, find the smallest positive integer h ⁡ ( n, k) h(n,k) such that any set 𝒳 {\cal X} of at least h ⁡ ( n, k) h(n,k) points in the plane in general position contains a subset C C of size n n forming the vertices of a convex n n -gon C C with | ( conv ⁡ ( C) ∩ 𝒳) ∖ C | ⩽ k |(\operatorname{conv}(C)\cap{\cal X})\setminus C|\leqslant k, i.e., this n n -gon contains at most k k other points of 𝒳 {\cal X} in its interior.

Devillers, Hurtado, Károlyi, and Seara [8] proposed a generalization of the first two problems by considering multicolored point sets in the plane. In our work, we study the following formulation.

Erdős–Szekeres-type Problem for Bicolored Sets. For any integers n 1 ⩾ 3, k 1 ⩾ 0, n 2 ⩾ 3 n_{1}\geqslant 3,k_{1}\geqslant 0,n_{2}\geqslant 3, and k 2 ⩾ 0 k_{2}\geqslant 0, find the smallest positive integer h ⁡ ( n 1, k 1, n 2, k 2) h(n_{1},k_{1};n_{2},k_{2}) such that any bicolored set 𝒳 {\cal X} of at least h ⁡ ( n 1, k 1, n 2, k 2) h(n_{1},k_{1};n_{2},k_{2}) points in general position contains either a subset of size n 1 n_{1} forming a convex n 1 n_{1} -gon of the first color with at most k 1 k_{1} interior points, or a subset of size n 2 n_{2} forming a convex n 2 n_{2} -gon of the second color with at most k 2 k_{2} interior points. We also define h n ​ c ​ ( n 1, k 1, n 2, k 2) h_{nc}(n_{1},k_{1};n_{2},k_{2}) for the case where the convexity condition is not required.

While we assumed n 1, n 2 ⩾ 3 n_{1},n_{2}\geqslant 3, the problem remains well-defined for n 1 = 2 n_{1}=2 or n 2 = 2 n_{2}=2, where a 2-gon is simply a pair of points. Finally, one can consider an arbitrary number of colors, defining the values h ⁡ ( n 1, k 1, n 2, k 2, n 3, k 3, …) h(n_{1},k_{1};n_{2},k_{2};n_{3},k_{3};\dots) and h n ​ c ​ ( n 1, k 1, n 2, k 2, n 3, k 3, …) h_{nc}(n_{1},k_{1};n_{2},k_{2};n_{3},k_{3};\dots).

Additionally, we define h i ​ s ​ l ​ ( n 1, k 1, n 2, k 2, n 3, k 3, …) h_{isl}(n_{1},k_{1};n_{2},k_{2};n_{3},k_{3};\dots) for monochromatic n n -islands with at most k k interior points, where an n n -island is an arbitrary subset C ⊂ 𝒳 C\subset{\cal X} such that | C | = n |C|=n and | ( conv ⁡ ( C) ∩ 𝒳) ∖ C | ⩽ k |(\operatorname{conv}(C)\cap{\cal X})\setminus C|\leqslant k.

For convenience, we introduce the generalized notation h ∗ ​ ( ⋯) h_{*}(\cdots) to refer to any of the above functions ( h, h n ​ c, h i ​ s ​ l h,h_{nc},h_{isl}) unless the context dictates otherwise.

For the first Erdős–Szekeres problem, it is known that:

 | g ⁡ ( 3) = 3, g ⁡ ( 4) = 5, g ⁡ ( 5) = 9 ​ [1], g ⁡ ( 6) = 17 ​ [9]. g(3)=3,\quad g(4)=5,\quad g(5)=9\text{ \cite[cite]{[\@@bibref{}{ES}{}{}]}},\quad g(6)=17\text{ \cite[cite]{[\@@bibref{}{SL}{}{}]}}. |  |

The latter result was first proved by Szekeres and Peters in 2006 using an exhaustive computer search that took 1500 hours. In 2019–2020, Marić [10] and Scheucher [11] applied SAT solvers to reduce the verification time to one hour.

For arbitrary n n, the upper bound has been repeatedly improved. We have summarized all known results in the following table. Ultimately:

 | [2] ​ 2 n − 2 + 1 ⩽ g ⁡ ( n) ⩽ 2 n + O ⁡ ( n ​ log ⁡ n) ​ [20]. \text{\cite[cite]{[\@@bibref{}{Low}{}{}]} }2^{n-2}+1\leqslant g(n)\leqslant 2^{n+O(\sqrt{n\log n})}\text{ \cite[cite]{[\@@bibref{}{HMPT20}{}{}]}}. |  |

Year, Authors | Formula | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

1935, Erdős–Szekeres [1] | ( 2 ​ n − 4 n − 2) + 1 \binom{2n-4}{n-2}+1 | 3 | 7 | 21 | 71 | 253 | 925 | 3433 | 12871 | 48621 | 184757 |

1998, Chung–Graham [12] | ( 2 ​ n − 4 n − 2) \binom{2n-4}{n-2} |  | 6 | 20 | 70 | 252 | 924 | 3432 | 12870 | 48620 | 184756 |

1998, Kleitman–Pachter [13] | ( 2 ​ n − 4 n − 2) − 2 ​ n + 7 \binom{2n-4}{n-2}-2n+7 | 3 | 5 | 17 | 65 | 245 | 915 | 3421 | 12857 | 48605 | 184739 |

1998, Tóth–Valtr [14] | ( 2 ​ n − 5 n − 2) + 2 \binom{2n-5}{n-2}+2 |  | 5 | 12 | 37 | 128 | 464 | 1718 | 6437 | 24312 | 92380 |

2005, Tóth–Valtr [15] | ( 2 ​ n − 5 n − 2) + 1 \binom{2n-5}{n-2}+1 |  |  | 11 | 36 | 127 | 463 | 1717 | 6436 | 24311 | 92379 |

2015, Vlachos [16] | ( 29 32 + o ⁡ ( 1)) ​ ( 2 ​ n − 5 n − 2) (\frac{29}{32}+o(1))\binom{2n-5}{n-2} |  |  |  | 33 | 114 | 414 | 1536 | 5765 | 21804 | 82942 |

2015, Mojarrad–Vlachos [17] | ( 2 ​ n − 5 n − 2) − ( 2 ​ n − 8 n − 3) + 2 \binom{2n-5}{n-2}-\binom{2n-8}{n-3}+2 |  |  | 11 | 33 | 113 | 408 | 1508 | 5645 | 21309 | 80490 |

2015, Norin–Yuditsky [18] | ( 7 8 + o ⁡ ( 1)) ​ ( 2 ​ n − 5 n − 2) (\frac{7}{8}+o(1))\binom{2n-5}{n-2} |  |  | 10 | 28 | 92 | 324 | 1178 | 4358 | 16304 | 61492 |

2017, Suk [19] | 2 n + O ⁡ ( n 2 / 3 ​ log ⁡ n) 2^{n+O(n^{2/3}\log n)} | asymptotic bound |

2020, Holmsen et al. [20] | 2 n + O ⁡ ( n ​ log ⁡ n) 2^{n+O(\sqrt{n\log n})} | asymptotic bound |

1935, Conjecture | 2 n − 2 + 1 2^{n-2}+1 | 3 | 5 | 9 | 17 | 33 | 65 | 129 | 257 | 513 | 1025 |

Table 1: Comparison of known upper bounds for g ⁡ ( n) g(n) for the Erdős–Szekeres convex polygon problem. Empty cells correspond to n n values outside the applicability of the methods.

The second problem is completely solved. The following results have been proven:

 | h ⁡ ( 3) = 3, h ⁡ ( 4) = 5, h ⁡ ( 5) = 10 ​ [21]. h(3)=3,\quad h(4)=5,\quad h(5)=10\text{ \cite[cite]{[\@@bibref{}{Harb}{}{}]}}. |  |

The history of finding the value of h ⁡ ( 6) h(6) evolved from early analytical investigations into rigorous formal verification. The first lower bounds were obtained through computer search: in 1989, Overmars, Scholten, and Vincent [22] presented configurations of 26 points without empty hexagons. In 2003, Overmars [23], using an optimized algorithm for finding empty polygons, improved this result by constructing a set of 29 points, establishing the bound h ⁡ ( 6) ⩾ 30 h(6)\geqslant 30.

The question of whether h ⁡ ( 6) h(6) is finite remained open for nearly thirty years until independent proofs of existence were published in 2007–2008. Nicolas [24] presented a proof with an upper bound of h ⁡ ( 6) ⩽ g ⁡ ( 25) h(6)\leqslant g(25), and Gerken [25] with h ⁡ ( 6) ⩽ g ⁡ ( 9) h(6)\leqslant g(9). Soon after, Valtr [26] proposed a simplified version of Gerken’s argument, giving h ⁡ ( 6) ⩽ g ⁡ ( 15) h(6)\leqslant g(15). However, these values were orders of magnitude larger than the known lower bound 1 1 1 In 2007, one of the authors announced an estimate h ⁡ ( 6) ⩽ g ⁡ ( 8) h(6)\leqslant g(8). The work was planned in two parts, the first of which was published in 2009 [27]. However, during the preparation of the second part, technical gaps in the proof were identified. Since the exact value h ⁡ ( 6) = 30 h(6)=30 has now been established by computational methods, the publication of the corrected second part was deemed unnecessary..

The exact value was only established in 2024 by Scheucher and Heule [28]: by combining geometric theory with the power of SAT solvers (CaDiCaL [29]), they proved that any set of 30 points in general position contains a convex empty hexagon. The definitive result on this matter was given in the work by Subercaseaux et al. [30]. The authors presented a full formal verification of Scheucher and Heule’s result in the Lean 4 system, mathematically proving the correctness of the geometric encoding and verifying the logical inference. This elevated the result from the category of computer calculations to the status of a formally proven theorem.

For n ⩾ 7 n\geqslant 7, the value h ⁡ ( n) h(n) does not exist, as proven by Horton in 1983 (see [31]). This leads to the third Erdős–Szekeres type problem and, in particular, the question of the existence of h ⁡ ( n, k) h(n,k) for n > 7 n>7.

For this problem, the obvious inequalities g ⁡ ( n) ⩽ h ⁡ ( n, k) ⩽ h ⁡ ( n) g(n)\leqslant h(n,k)\leqslant h(n) hold if the corresponding values exist. Furthermore:

 | h ⁡ ( n) = h ⁡ ( n, 0) ⩾ h ⁡ ( n, 1) ⩾ h ⁡ ( n, 2) ⩾ ⋯ ⩾ g ⁡ ( n). h(n)=h(n,0)\geqslant h(n,1)\geqslant h(n,2)\geqslant\dots\geqslant g(n). |  |

There exists a maximum value k ¯ = k ¯ ​ ( n) \overline{k}=\overline{k}(n) such that h ⁡ ( n, k ¯) > g ⁡ ( n) h(n,\overline{k})>g(n), while for all k > k ¯ k>\overline{k}, h ⁡ ( n, k) = g ⁡ ( n) h(n,k)=g(n) (for example, it is obvious that h ⁡ ( n, g ⁡ ( n) − n) = g ⁡ ( n) h(n,g(n)-n)=g(n)).

For small values of n n, the following results are known:

 | h ⁡ ( 3, k) = 3, h ⁡ ( 4, k) = 5, h ⁡ ( 5, 0) = 10, h ⁡ ( 5, k ⩾ 1) = 9. h(3,k)=3,\quad h(4,k)=5,\quad h(5,0)=10,\quad h(5,k\geqslant 1)=9. |  |

The last equality is due to the fact that any convex pentagon containing two or more points of the set in its interior always contains a smaller convex and empty pentagon.

Deeper results on the third problem were obtained in the works of Sendov [32] and Nyklova [33]. Using Horton constructions [31], these papers prove the non-existence of h ⁡ ( n, k) h(n,k) for certain values of k k when n > 7 n>7. If k ¯ ​ ( n) \underline{k}(n) denotes the maximum value of k k for which h ⁡ ( n, k) h(n,k) does not exist for a given n n, Sendov and Nyklova obtained the estimate k ¯ ​ ( n) ⩾ ( 2 4 + o ⁡ ( 1)) n \underline{k}(n)\geqslant(\sqrt[4]{2}+o(1))^{n}. One of the authors established a significantly stronger exponential estimate: k ¯ ​ ( n) ⩾ ( 2 + o ⁡ ( 1)) n \underline{k}(n)\geqslant(2+o(1))^{n} (see [34]). Specifically, it was shown that for odd n n, the following does not exist:

 | h ⁡ ( n, ( n − 7 n − 7 2) − 1), h\left(n,\binom{n-7}{\frac{n-7}{2}}-1\right), |  |

and for even n n:

 | h ⁡ ( n, 2 ​ ( n − 8 n − 8 2) − 1). h\left(n,2\binom{n-8}{\frac{n-8}{2}}-1\right). |  |

In Nyklova’s paper [33], it was also proven that h ⁡ ( 6, 6) = g ⁡ ( 6) = 17 h(6,6)=g(6)=17 and the estimate h ⁡ ( 6, 5) ⩽ 19 h(6,5)\leqslant 19 was obtained 2 2 2 In several prior publications, including those of one of the authors, it was erroneously claimed that the result h ⁡ ( 6, 5) = 19 h(6,5)=19 in [33] was due to a computational error. This misunderstanding arose from the ambiguity of the author’s notation: in the original work [33], the value 19 is given only as an upper bound, although it is formally written with an equals sign. This clarification is intended to correct the tradition of incorrect citation and interpretation of this result in the literature..

In 2008, one of the authors showed that h ⁡ ( 6, 1) ⩽ g ⁡ ( 7) ⩽ 127 h(6,1)\leqslant g(7)\leqslant 127 (see [35]). In 2010, using a modification of the Szekeres-McKay-Peters algorithm [9], the same author found the exact values of h ⁡ ( 6, 2) h(6,2) and h ⁡ ( 6, 1) h(6,1) (see [36]). In the present study, we present a new computer proof obtained by the method of Answer Set Programming (ASP). The verification time for these cases has been significantly reduced to 70 and 190 minutes, respectively.

###### Theorem 1.

The following equalities hold: h ( 6, ⩾ 2) = 17 h(6,\geqslant 2)=17, h ⁡ ( 6, 1) = 18 h(6,1)=18.

Now let us discuss the version of Erdős–Szekeres problem for bicolored sets. It is easy to see that h ⁡ ( n 1, ∞, n 2, ∞) = g ⁡ ( n 1) + g ⁡ ( n 2) − 1 h(n_{1},\infty;n_{2},\infty)=g(n_{1})+g(n_{2})-1. Devillers et al. in [8] proved that among N ⩾ 5 N\geqslant 5 points of two colors, there must be ⌈ N / 4 ⌉ − 2 \lceil N/4\rceil-2 monochromatic disjoint triangles (i.e., triangles intersecting at most by a common edge). From this, it follows that:

 | h ⁡ ( 3, 0, 3, 0) = 9, h ⁡ ( 3, 0, 3, 0, 2, 0) = 13 + 1 = 14, h(3,0;3,0)=9,\quad h(3,0;3,0;2,0)=13+1=14, |  |

 | h ⁡ ( 3, 0, 3, 0, 2, 0, 2, 0) = h ⁡ ( 3, 0, 3, 0, 3, ∞) = h ⁡ ( 3, 0, 3, 0, 3, 8) = 17 + 2 = 19, h(3,0;3,0;2,0;2,0)=h(3,0;3,0;3,\infty)=h(3,0;3,0;3,8)=17+2=19, |  |

 | h ⁡ ( 3, 0, 3, 0, 2, 0; …; 2, 0 ⏟ t) = 5 ​ t + 9. h(3,0;3,0;\underbrace{2,0;\dots;2,0}_{t})=5t+9. |  |

Also, using Horton set colorings, the authors of [8] proved that h ⁡ ( 3, 0, 3, 0, 3, 0) h(3,0;3,0;3,0) and h ⁡ ( 5, 0, 5, 0) h(5,0;5,0) do not exist. Furthermore, their proof implies that h ⁡ ( 3, 0, 5, 0) h(3,0;5,0) does not exist. However, h ⁡ ( 3, 0, 4, 0) ⩽ h ⁡ ( 6) h(3,0;4,0)\leqslant h(6) exists, since coloring the vertices of an empty hexagon in two colors always forms the required convex triangle or quadrilateral. The question of the existence of h ⁡ ( 4, 0, 4, 0) h(4,0;4,0) and h i ​ s ​ l ​ ( 4, 0, 4, 0) h_{isl}(4,0;4,0) remains open.

Lower bounds for h ⁡ ( 4, 0, 4, 0) h(4,0;4,0) have been repeatedly improved: from 18 points in [8] to the results of Brass (20 points [37]), Friedman (30 points [38]), van Gulik (32 points [39]), Huemer and Seara (36 points [40]). Finally, one of the authors of the present work established that h ⁡ ( 4, 0, 4, 0) ⩾ 47 h(4,0;4,0)\geqslant 47 by constructing an example with 46 points [41].

In 2016, Basu et al. [42] found the values:

 | h ⁡ ( 3, 1, 3, 1) = 6, h ⁡ ( 3, 1, 3, 1, 3, 1) = 13, h(3,1;3,1)=6,\quad h(3,1;3,1;3,1)=13, |  |

and proved that h ⁡ ( 3, c − 1, …, 3, c − 1) ⩽ max ⁡ { c 2 + 1, 6 } h(3,c-1;\ldots;3,c-1)\leqslant\max\{c^{2}+1,6\}, h ⁡ ( 3, c − 2, …, 3, c − 2) ⩽ c 2 + c + 1 h(3,c-2;\ldots;3,c-2)\leqslant c^{2}+c+1, while the value h ⁡ ( 3, ⌊ c − 3 2 ⌋, …, 3, ⌊ c − 3 2 ⌋) h(3,\lfloor\frac{c-3}{2}\rfloor;\ldots;3,\lfloor\frac{c-3}{2}\rfloor) does not exist.

In 2019, Cravioto-Lagos et al. [43] showed that:

 | h ⁡ ( 3, c − 3, …, 3, c − 3) ⩽ ⌊ 2 ​ c ​ ( c + 1 c − 2) c − 2 c − 1 − 2 ​ c − 3 ( c − 1) ​ ( c − 2) 2 ⌋ + 1, h(3,c-3;\ldots;3,c-3)\leqslant\left\lfloor\frac{2c(c+\frac{1}{c-2})}{\frac{c-2}{c-1}-\frac{2c-3}{(c-1)(c-2)^{2}}}\right\rfloor+1, |  |

 | h ⁡ ( 4, 2 ​ c − 3, …, 4, 2 ​ c − 3) ⩽ c ⋅ g ⁡ ( 4 ​ c + 1). h(4,2c-3;\ldots;4,2c-3)\leqslant c\cdot g(4c+1). |  |

Due to the complexity of the existence problem for h ⁡ ( 4, 0, 4, 0) h(4,0;4,0), Aichholzer et al. considered in 2010 its simplification (see [44]), where the convexity condition is not mandatory, and proved that h n ​ c ​ ( 4, 0, 4, 0) ⩽ 2760 h_{nc}(4,0;4,0)\leqslant 2760. The example for the convex case from [8], consisting of 18 points, applies here as well.

The latest lower bounds for h n ​ c ​ ( 4, 0, 4, 0) h_{nc}(4,0;4,0) and h i ​ s ​ l ​ ( 4, 0, 4, 0) h_{isl}(4,0;4,0) were obtained within the EuroGIGA ComPoSe project under Aichholzer’s leadership. Specifically, the computer search conducted by project participants allowed the construction of a set of 22 points for h n ​ c ​ ( 4, 0, 4, 0) h_{nc}(4,0;4,0) and an example of 35 points for h i ​ s ​ l ​ ( 4, 0, 4, 0) h_{isl}(4,0;4,0) 3 3 3 [https://www.eurogiga-compose.eu/posezo.php][3] 4 4 4 In his Ph.D. thesis, Scheucher [11] claimed to have found examples of 48, 36, and 24 points for h ⁡ ( 4, 0, 4, 0) h(4,0;4,0), h i ​ s ​ l ​ ( 4, 0, 4, 0) h_{isl}(4,0;4,0), and h n ​ c ​ ( 4, 0, 4, 0) h_{nc}(4,0;4,0) respectively. However, at the time of writing, the original web repository of the project [https://page.math.tu-berlin.de/~scheuch/research/sat_vs_bicolored_point_sets/][4] is unavailable, and the thesis does not provide full sets of coordinates, making independent verification of these results impossible..

We have constructed an example of a set with 25 points containing no empty monochromatic quadrilaterals and proved the absence of such configurations for N ⩾ 26 N\geqslant 26, establishing the exact value h n ​ c ​ ( 4, 0, 4, 0) = 26 h_{nc}(4,0;4,0)=26.

In 2018, Liu and Zhang [45] established that:

 | h n ​ c ​ ( 4, 2, 4, 2) = 9, h n ​ c ​ ( 4, 1, 4, 1) = 11, h_{nc}(4,2;4,2)=9,\quad h_{nc}(4,1;4,1)=11, |  |

 | h n ​ c ​ ( 4, 2, 4, 2, 4, 2) ⩽ 120, h n ​ c ​ ( 4, 2 ​ c − 3, …, 4, 2 ​ c − 3) ⩽ 4 ​ c 2 + 1 h_{nc}(4,2;4,2;4,2)\leqslant 120,\quad h_{nc}(4,2c-3;\ldots;4,2c-3)\leqslant 4c^{2}+1 |  |

and that the value h n ​ c ​ ( 4, 2 ​ ⌊ c − 1 2 ⌋ − 1, …, 4, 2 ​ ⌊ c − 1 2 ⌋ − 1) h_{nc}(4,2\lfloor\frac{c-1}{2}\rfloor-1;\ldots;4,2\lfloor\frac{c-1}{2}\rfloor-1) does not exist.

Note that monochromatic variants of the problem for h n ​ c h_{nc} and h i ​ s ​ l h_{isl} are trivial, since h n ​ c ​ ( n, 0) = h i ​ s ​ l ​ ( n, 0) = n h_{nc}(n,0)=h_{isl}(n,0)=n.

The main results of this study are formulated below. The values of the functions h ∗ ​ ( ⋯) h_{*}(\cdots) obtained through computer modeling and analytical derivation are presented in the following statements.

###### Theorem 2.

The values of the functions h n ​ c ​ ( 4, k 1, 4, k 2) h_{nc}(4,k_{1};4,k_{2}), h i ​ s ​ l ​ ( 4, k 1, 4, k 2) h_{isl}(4,k_{1};4,k_{2}), and h ⁡ ( 4, k 1, 4, k 2) h(4,k_{1};4,k_{2}) are given in the tables:

h n ​ c ​ ( 4, k 1, 4, k 2) h_{nc}(4,k_{1};4,k_{2}) |  | h i ​ s ​ l ​ ( 4, k 1, 4, k 2) h_{isl}(4,k_{1};4,k_{2}) |  | h ⁡ ( 4, k 1, 4, k 2) h(4,k_{1};4,k_{2}) |

 | 0 | 1 | 2 | 3 |  |  | 0 | 1 | 2 | 3 |  |  | 0 | 1 | 2 | 3 | 4 |

0 | 26 | 15 | 14 | 12 |  | 0 | 36- | 22 | 16 | 13 |  | 0 | 47- | 29- | 23-25 | 20-21 | 17 |

1 | 15 | 11 | 10 | 9 |  | 1 | 22 | 13 | 11 | 9 |  | 1 | 29- | 18 | 16 | 15 | 13 |

2 | 14 | 10 | 9 | 9 |  | 2 | 16 | 11 | 9 | 9 |  | 2 | 23-25 | 16 | 12 | 12 | 11 |

3 | 12 | 9 | 9 | 7 |  | 3 | 13 | 9 | 9 | 7 |  | 3 | 20-21 | 15 | 12 | 11 | 11 |

 | 4 | 17 | 13 | 11 | 11 | 9 |

###### Theorem 3.

Values of h n ​ c ​ ( 4, k 1, 3, k 2) h_{nc}(4,k_{1};3,k_{2}), h i ​ s ​ l ​ ( 4, k 1, 3, k 2) h_{isl}(4,k_{1};3,k_{2}), h ⁡ ( 4, k 1, 3, k 2) h(4,k_{1};3,k_{2}), and h n ​ c ​ ( 5, k 1, 3, k 2) h_{nc}(5,k_{1};3,k_{2}) are given in the tables below. Table rows correspond to the parameter k 1 k_{1}, and columns to k 2 k_{2}.

h n ​ c ​ ( 4, k 1, 3, k 2) h_{nc}(4,k_{1};3,k_{2}) |  | h i ​ s ​ l ​ ( 4, k 1, 3, k 2) h_{isl}(4,k_{1};3,k_{2}) |  | h ⁡ ( 4, k 1, 3, k 2) h(4,k_{1};3,k_{2}) |  | h n ​ c ​ ( 5, k 1, 3, k 2) h_{nc}(5,k_{1};3,k_{2}) |

 | 0 | 1 | 2 | 3 |  |  | 0 | 1 | 2 | 3 |  |  | 0 | 1 | 2 | 3 | 4 |  |  | 0 | 1 | 2 | 3 | 4 |

0 | 14 | 10 | 10 | 9 |  | 0 | 17 | 11 | 11 | 9 |  | 0 | 26 | 14 | 13 | 12 | 11 |  | 0 | 20 | 13 | 12 | 12 | 11 |

1 | 11 | 8 | 8 | 8 |  | 1 | 12 | 9 | 8 | 8 |  | 1 | 14 | 11 | 9 | 9 | 9 |  | 1 | 15 | 11 | 10 | 10 | 10 |

2 | 9 | 7 | 7 | 6 |  | 2 | 10 | 7 | 7 | 6 |  | 2 | 11 | 9 | 8 | 8 | 7 |  | 2 | 11 | 9 | 8 | 8 | 7 |

###### Theorem 4.

The values of the function h ⁡ ( 3, k 1, 3, k 2, 3, k 3) h(3,k_{1};3,k_{2};3,k_{3}) are presented in the tables. The index k 1 k_{1} determines the block number (from left to right, k 1 = 0, 1, 2, 3, 4 k_{1}=0,1,2,3,4), the rows correspond to k 2 k_{2}, and the columns correspond to k 3 k_{3}.

 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

0 | − - | 33- | 26- | 23 | 21 | 20 | 20 | 20 | 19 |  |  | 1 | 2 | 3 | 4 |  |  |  |  |  |  |  |  |  |  |  |  |

1 | 33- | 19 | 17 | 16 | 15 | 15 | 15 | 14 | 14 |  | 1 | 13 | 12 | 12 | 11 |  |  | 2 | 3 | 4 |  |  |  |  |  |  |  |

2 | 26- | 17 | 15 | 14 | 14 | 14 | 13 | 13 | 13 |  | 2 | 12 | 11 | 11 | 10 |  | 2 | 10 | 9 | 9 |  |  | 3 | 4 |  |  |  |

3 | 23 | 16 | 14 | 13 | 13 | 13 | 12 | 12 | 12 |  | 3 | 12 | 11 | 10 | 10 |  | 3 | 9 | 9 | 9 |  | 3 | 8 | 8 |  |  | 4 |

4 | 21 | 15 | 14 | 13 | 12 | 12 | 12 | 12 | 12 |  | 4 | 11 | 10 | 10 | 9 |  | 4 | 9 | 9 | 8 |  | 4 | 8 | 8 |  | 4 | 7 |

5 | 20 | 15 | 14 | 13 | 12 | 12 | 12 | 12 | 12 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

6 | 20 | 15 | 13 | 12 | 12 | 12 | 11 | 11 | 11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

7 | 20 | 14 | 13 | 12 | 12 | 12 | 11 | 11 | 11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

8 | 19 | 14 | 13 | 12 | 12 | 12 | 11 | 11 | 11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

###### Theorem 5.

The table below presents additional values for multicolored homogeneous configurations. A dash indicates the non-existence of the required value (follows from [8, 43]).

k k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

h ⁡ ( 3, k, 3, k, 3, k, 3, k) h(3,k;3,k;3,k;3,k) | – | 29- | 18 | 13 | 12 | 10 | 9 | 9 | 9 |

h n ​ c ​ ( 4, k, 4, k, 4, k) h_{nc}(4,k;4,k;4,k) | – | – | 21-22 | 16 | 14 | 12 | 10 | 10 | 10 |

h i ​ s ​ l ​ ( 4, k, 4, k, 4, k) h_{isl}(4,k;4,k;4,k) | – | – | 24- | 19- | 16 | 12 | 10 | 10 | 10 |

h ⁡ ( 3, k, 3, k, 3, k, 3, k, 3, k) h(3,k;3,k;3,k;3,k;3,k) | – | – | 27- | 22- | 18 | 16 | 14 | 12 | 11 |

## 2 Structure of the Paper

The paper is organized as follows. Section 3 introduces basic definitions, formalizes the concept of a signotope, and describes the connection between the combinatorial properties of sets and their geometric realizability. Section 4 is dedicated to describing the logical architecture of the research: it presents the CNF encoding of geometric predicates and algorithms for reducing Erdős–Szekeres type problems to the Boolean satisfiability problem (SAT) and Satisfiability Modulo Theories (SMT).

In Section 5, the developed linear subreduction method is described in detail, which allowed for significant optimization of the search for geometric realizations in computationally intensive cases. Sections 8 and 9 provide proofs of the main theorems formulated in the introduction, including the verification of new lower bounds. Finally, in Section 11, open questions and perspectives for applying the proposed approach to related problems in combinatorial geometry are discussed.

## 3 Combinatorial Model and SAT Formulation

### 3.1 Basic Definitions

In this paper, we consider configurations of points in the plane in general position. To discretize the problem, we use the framework of order types and signotopes.

###### Definition 1 (Order Type).

The order type of a finite set of points 𝒳 = { p 1, …, p n } ⊂ ℝ 2 \mathcal{X}=\{p_{1},\dots,p_{n}\}\subset\mathbb{R}^{2} is a mapping χ: ( [n] 3) → { − 1, 1 } \chi\colon\binom{[n]}{3}\to\{-1,1\} that assigns to each ordered triple of indices ( i, j, k) (i,j,k) the orientation of the triangle p i ​ p j ​ p k p_{i}p_{j}p_{k}:

 | χ ( i, j, k) = sgn det ( 1 x i y i 1 x j y j 1 x k y k). \chi(i,j,k)=\operatorname{sgn}\det\begin{pmatrix}1&x_{i}&y_{i}\\ 1&x_{j}&y_{j}\\ 1&x_{k}&y_{k}\end{pmatrix}. |  |

###### Definition 2 (Monotone Signotope).

A monotone signotope of rank 3 on n n elements is a mapping σ: ( [n] 3) → { − 1, 1 } \sigma\colon\binom{[n]}{3}\to\{-1,1\} such that for any indices 1 ⩽ i < j < k < l ⩽ n 1\leqslant i<j<k<l\leqslant n, the sequence of signs

 | ( σ ⁡ ( i, j, k), σ ⁡ ( i, j, l), σ ⁡ ( i, k, l), σ ⁡ ( j, k, l)) (\sigma(i,j,k),\sigma(i,j,l),\sigma(i,k,l),\sigma(j,k,l)) |  |

has exactly one sign change.

The connection between abstract combinatorial structures and Euclidean geometry is established through the concept of realization.

###### Definition 3 (Geometric Realization).

A geometric realization of a signotope σ \sigma is a set of points 𝒳 = { p 1, …, p n } ⊂ ℝ 2 \mathcal{X}=\{p_{1},\dots,p_{n}\}\subset\mathbb{R}^{2} such that its order type χ \chi coincides with σ \sigma, i.e., χ ⁡ ( i, j, k) = σ ⁡ ( i, j, k) \chi(i,j,k)=\sigma(i,j,k) for all 1 ⩽ i < j < k ⩽ n 1\leqslant i<j<k\leqslant n. A signotope is called realizable if there exists at least one geometric realization for it.

### 3.2 Motivation and the function h ~ ​ ( ⋯) \tilde{h}(\cdots)

Calculating the classical function h ∗ ​ ( n 1, k 1, …, n c, k c) h_{*}(n_{1},k_{1};\dots;n_{c},k_{c}) in Euclidean space is difficult because the set of all point sets to be checked has the cardinality of the continuum. However, key geometric properties (convexity, a point lying inside a polygon) are invariant with respect to the order type. This allows mapping the problem onto the domain of abstract signotopes, the number of which for a fixed n n is large but finite.

The use of rank-3 monotone signotopes allows the geometric problem to be translated into the language of Boolean logic. This provides two key advantages:

1. 1.

Discretization: The infinite coordinate space is replaced by a finite space of Boolean variables L a ​ b ​ c ∈ { true, false } L_{abc}\in\{\text{true, false}\}.

2. 2.

Efficiency: Modern SAT solvers use powerful heuristics to prune classes of configurations that certainly cannot contain the sought substructures.

Hereafter in the text, the term signotope implies monotone signotope of rank 3 unless explicitly stated otherwise.

By analogy with the classical case, let h ~ ​ ( n 1, k 1, …) \tilde{h}(n_{1},k_{1};\dots), h ~ n ​ c ​ ( n 1, k 1, …) \tilde{h}_{nc}(n_{1},k_{1};\dots), and h ~ i ​ s ​ l ​ ( n 1, k 1, …) \tilde{h}_{isl}(n_{1},k_{1};\dots) be the minimum integer N N such that any c c -colored signotope on N N elements contains the corresponding monochromatic n i n_{i} -configuration (convex, non-convex, or island) with at most k i k_{i} interior points.

Note that for the case n i = 3 n_{i}=3, the concepts of convex/arbitrary polygon and island are equivalent; therefore, we will use the general term triangle for them in the following text.

###### Definition 4 (Maximal Signotope).

A signotope on ( N − 1) (N-1) elements is called maximal if it does not contain any of the mentioned monochromatic n i n_{i} -polygons with the given constraint on the number of interior points, where N = h ~ ∗ ​ ( ⋯) N=\tilde{h}_{*}(\cdots).

The relationship between geometric and combinatorial functions is expressed by the fundamental inequality:

 | h ∗ ​ ( n 1, k 1, …, n c, k c) ⩽ h ~ ∗ ​ ( n 1, k 1, …, n c, k c). h_{*}(n_{1},k_{1};\dots;n_{c},k_{c})\leqslant\tilde{h}_{*}(n_{1},k_{1};\dots;n_{c},k_{c}). |  |

If it is possible to construct a configuration of ( N − 1) (N-1) points that is a geometric realization of at least one maximal signotope, then the equality h ∗ ​ ( ⋯) = h ~ ∗ ​ ( ⋯) h_{*}(\cdots)=\tilde{h}_{*}(\cdots) is achieved. In the course of our research, such realizations were successfully found for almost all cases considered.

It is known that for N ⩽ 8 N\leqslant 8 points, all signotopes are realizable, which guarantees that the functions coincide. Starting from N = 9 N=9, non-realizable signotopes emerge. However, within the framework of the problem under consideration, as a rule, there exists not just one, but a whole family of different maximal signotopes. The value h ∗ ​ ( ⋯) h_{*}(\cdots) will be strictly less than h ~ ∗ ​ ( ⋯) \tilde{h}_{*}(\cdots) only if all signotopes from this family simultaneously turn out to be non-realizable. Given that checking the realizability of an arbitrary signotope is an NP-hard problem, such examples have not yet been discovered in the literature. In the general case, h ~ ∗ ​ ( ⋯) \tilde{h}_{*}(\cdots) provides an upper bound.

Open Question. Does the equality h ∗ ​ ( n 1, k 1, …, n c, k c) = h ~ ∗ ​ ( n 1, k 1, …, n c, k c) h_{*}(n_{1},k_{1};\dots;n_{c},k_{c})=\tilde{h}_{*}(n_{1},k_{1};\dots;n_{c},k_{c}) always hold for arbitrary sets of parameters n i n_{i} and k i k_{i}?

## 4 Logical Architecture and CNF Encoding

Since in our model the points are initially ordered by the x x -coordinate ( x 0 < x 1 < ⋯ < x N − 1 x_{0}<x_{1}<\dots<x_{N-1}), the geometric conditions on the orientation of triples (variables L a ​ b ​ c L_{abc}) and point inclusion are substantially simplified. We associate a Boolean formula ℱ N \mathcal{F}_{N} in conjunctive normal form (CNF) with each configuration of N N points based on the following Boolean variables:

- •

C i ​ ( a) ∈ { true, false } C_{i}(a)\in\{\text{true, false}\} — point a a has color i ∈ { 1, …, c } i\in\{1,\dots,c\}.

- •

L a ​ b ​ c ∈ { true, false } L_{abc}\in\{\text{true, false}\} — orientation of the triple ( a, b, c) (a,b,c), where true ⇔ σ ⁡ ( a, b, c) = + 1 \text{true}\iff\sigma(a,b,c)=+1.

- •

E ​ X ​ T a ​ b ​ c ​ ( z) ∈ { true, false } EXT_{abc}(z)\in\{\text{true, false}\} — point z z lies outside the triangle ( a, b, c) (a,b,c).

- •

T ​ R a ​ b ​ c ​ ( q) ∈ { true, false } TR_{abc}(q)\in\{\text{true, false}\} — the triangle ( a, b, c) (a,b,c) contains no more than q q interior points.

### 4.1 Coloring and Inverse Color Encoding

For each point a ∈ 𝒳 a\in\mathcal{X}, a set of Boolean variables { C 1 ​ ( a), C 2 ​ ( a), …, C c ​ ( a) } \{C_{1}(a),C_{2}(a),\dots,C_{c}(a)\} is introduced. Our implementation uses inverse logic for color assignment: the value C i ​ ( a) = false C_{i}(a)=\text{false} means that point a a is colored with color i i, and C i ​ ( a) = true C_{i}(a)=\text{true} means that the point is of a different color.

This approach significantly simplifies the CNF representation of conditions on monochromatic figures, minimizing the number of negation operations. The conditions for correct coloring take the form:

1. Color Existence Condition: a point must be colored in at least one color (i.e., at least one variable must be false):

 | C 1 ​ ( a) ¯ ∨ C 2 ​ ( a) ¯ ∨ ⋯ ∨ C c ​ ( a) ¯ \overline{C_{1}(a)}\lor\overline{C_{2}(a)}\lor\dots\lor\overline{C_{c}(a)} |  | (1) |

2. Uniqueness Condition (for c > 1 c>1): a point cannot have more than one color. This means that for any two distinct colors i i and j j, both variables cannot be simultaneously false:

 | ∀ i < j: C i ​ ( a) ∨ C j ​ ( a) \forall_{i<j}:C_{i}(a)\lor C_{j}(a) |  | (2) |

### 4.2 Geometric Axioms of the Signotope

To ensure that the variables L a ​ b ​ c L_{abc} correspond to a monotone signotope, for each quadruple of indices a < b < c < d a<b<c<d, constraints are imposed that guarantee exactly one sign change in the sequence ( L a ​ b ​ c, L a ​ b ​ d, L a ​ c ​ d, L b ​ c ​ d) (L_{abc},L_{abd},L_{acd},L_{bcd}). In terms of forbidden configurations (negation of a conjunction), one of such conditions looks like this:

 | L a ​ b ​ c ∧ L a ​ c ​ d ¯ ∧ L b ​ c ​ d ¯ ∧ L a ​ b ​ c ¯ ∧ L a ​ c ​ d ∧ L b ​ c ​ d ¯ ¯ \overline{L_{abc}\land\overline{L_{acd}}\land L_{bcd}}\land\overline{\overline{L_{abc}}\land L_{acd}\land\overline{L_{bcd}}} |  | (3) |

After expansion using De Morgan’s laws, we obtain CNF clauses:

 | ( L a ​ b ​ c ¯ ∨ L a ​ c ​ d ∨ L b ​ c ​ d ¯) ∧ ( L a ​ b ​ c ∨ L a ​ c ​ d ¯ ∨ L b ​ c ​ d) (\overline{L_{abc}}\lor L_{acd}\lor\overline{L_{bcd}})\land(L_{abc}\lor\overline{L_{acd}}\lor L_{bcd}) |  | (4) |

The complete system of four such conditions (8 clauses) fully defines the required structure.

### 4.3 Exterior Point and Density Variables

Point z z can lie inside △ ​ a ​ b ​ c \triangle abc only under the condition a < z < c a<z<c. We define the conditions under which a point is external ( E ​ X ​ T EXT). Without loss of generality, consider the case a < b < z < c a<b<z<c. Point z z is external if the orientations of triangles a ​ z ​ c azc and b ​ z ​ c bzc coincide:

 | ( L a ​ z ​ c ⇔ L b ​ z ​ c) ⟹ E ​ X ​ T a ​ b ​ c ​ ( z) (L_{azc}\iff L_{bzc})\implies EXT_{abc}(z) |  | (5) |

Expanding the equivalence:

 | ( ( L a ​ z ​ c ∧ L b ​ z ​ c) ⟹ E ​ X ​ T a ​ b ​ c ​ ( z)) ∧ ( ( L a ​ z ​ c ¯ ∧ L b ​ z ​ c ¯) ⟹ E ​ X ​ T a ​ b ​ c ​ ( z)) ((L_{azc}\land L_{bzc})\implies EXT_{abc}(z))\land((\overline{L_{azc}}\land\overline{L_{bzc}})\implies EXT_{abc}(z)) |  | (6) |

In CNF format:

 | ( L a ​ z ​ c ¯ ∨ L b ​ z ​ c ¯ ∨ E ​ X ​ T a ​ b ​ c ​ ( z)) ∧ ( L a ​ z ​ c ∨ L b ​ z ​ c ∨ E ​ X ​ T a ​ b ​ c ​ ( z)) (\overline{L_{azc}}\lor\overline{L_{bzc}}\lor EXT_{abc}(z))\land(L_{azc}\lor L_{bzc}\lor EXT_{abc}(z)) |  | (7) |

Density variables T ​ R a ​ b ​ c ​ ( q) TR_{abc}(q) encode the statement: ”there are no more than q q points inside triangle a ​ b ​ c abc “. Let P a ​ b ​ c = { z: a < z < c, z ≠ b } P_{abc}=\{z:a<z<c,z\neq b\} be the set of all potential points that, by virtue of their x x -coordinates, could be inside triangle a ​ b ​ c abc. The density condition is formulated as follows: if in the set P a ​ b ​ c P_{abc} there exists a subset Z Z of size | P a ​ b ​ c | − q |P_{abc}|-q consisting exclusively of exterior points, then the total number of interior points does not exceed q q.

 | ( ⋁ Z ⊂ P a ​ b ​ c | Z | = | P a ​ b ​ c | − q ( ⋀ z ∈ Z E ​ X ​ T a ​ b ​ c ​ ( z))) ⟹ T ​ R a ​ b ​ c ​ ( q) \left(\bigvee_{\begin{subarray}{c}Z\subset P_{abc}\\ |Z|=|P_{abc}|-q\end{subarray}}\left(\bigwedge_{z\in Z}EXT_{abc}(z)\right)\right)\implies TR_{abc}(q) |  | (8) |

Expanding the implication yields a system of clauses for each T ​ R a ​ b ​ c ​ ( q) TR_{abc}(q):

 | ⋀ Z ⊂ P a ​ b ​ c | Z | = | P a ​ b ​ c | − q ( ⋁ z ∈ Z E ​ X ​ T a ​ b ​ c ​ ( z) ¯ ∨ T ​ R a ​ b ​ c ​ ( q)) \bigwedge_{\begin{subarray}{c}Z\subset P_{abc}\\ |Z|=|P_{abc}|-q\end{subarray}}\left(\bigvee_{z\in Z}\overline{EXT_{abc}(z)}\lor TR_{abc}(q)\right) |  | (9) |

### 4.4 Conditions on Monochromatic Figures in Inverse Color Logic

For each color i i and corresponding limit k i k_{i}, we introduce a prohibition on the existence of a convex n i n_{i} -gon containing no more than k i k_{i} points inside.

By using inverse color encoding, the condition that all vertices of a potential polygon { a, b, c } \{a,b,c\} or { a, b, c, d } \{a,b,c,d\} have the same color i i is written as a disjunction of variables without negation signs.

For the case n i = 3 n_{i}=3 and a triple of points a < b < c a<b<c of the same color i i, the forbidden configuration (empty or almost empty triangle) takes the form:

 | C i ​ ( a) ¯ ∧ C i ​ ( b) ¯ ∧ C i ​ ( c) ¯ ∧ T ​ R a ​ b ​ c ​ ( k i) ¯ \overline{\overline{C_{i}(a)}\land\overline{C_{i}(b)}\land\overline{C_{i}(c)}\land TR_{abc}(k_{i})} |  | (10) |

In CNF representation:

 | C i ​ ( a) ∨ C i ​ ( b) ∨ C i ​ ( c) ∨ T ​ R a ​ b ​ c ​ ( k i) ¯ C_{i}(a)\lor C_{i}(b)\lor C_{i}(c)\lor\overline{TR_{abc}(k_{i})} |  | (11) |

For n i = 4 n_{i}=4 and a quadruple of points a < b < c < d a<b<c<d of the same color i i, configurations forming a convex quadrilateral with a total number of interior points not exceeding k i k_{i} are forbidden. Within the monotone signotope model, this condition breaks down into two geometric scenarios:

1. Case 4-cup / 4-cap: L a ​ b ​ c ⇔ L b ​ c ​ d L_{abc}\iff L_{bcd}. For all admissible combinations q 1 + q 2 = k i q_{1}+q_{2}=k_{i}, the forbidden configuration is described as:

 | C i ​ ( a) ¯ ∧ C i ​ ( b) ¯ ∧ C i ​ ( c) ¯ ∧ C i ​ ( d) ¯ ∧ ( L a ​ b ​ c ⇔ L b ​ c ​ d) ∧ T ​ R a ​ b ​ c ​ ( q 1) ∧ T ​ R a ​ c ​ d ​ ( q 2) ¯ \overline{\overline{C_{i}(a)}\land\overline{C_{i}(b)}\land\overline{C_{i}(c)}\land\overline{C_{i}(d)}\land(L_{abc}\iff L_{bcd})\land TR_{abc}(q_{1})\land TR_{acd}(q_{2})} |  | (12) |

In CNF format, this is represented by a pair of clauses (for positive and negative orientation, respectively):

 | C i ​ ( a) ∨ C i ​ ( b) ∨ C i ​ ( c) ∨ C i ​ ( d) ∨ L a ​ b ​ c ¯ ∨ L b ​ c ​ d ¯ ∨ T ​ R a ​ b ​ c ​ ( q 1) ¯ ∨ T ​ R a ​ c ​ d ​ ( q 2) ¯ C_{i}(a)\lor C_{i}(b)\lor C_{i}(c)\lor C_{i}(d)\lor\overline{L_{abc}}\lor\overline{L_{bcd}}\lor\overline{TR_{abc}(q_{1})}\lor\overline{TR_{acd}(q_{2})} |  | (13) |

 | C i ​ ( a) ∨ C i ​ ( b) ∨ C i ​ ( c) ∨ C i ​ ( d) ∨ L a ​ b ​ c ∨ L b ​ c ​ d ∨ T ​ R a ​ b ​ c ​ ( q 1) ¯ ∨ T ​ R a ​ c ​ d ​ ( q 2) ¯ C_{i}(a)\lor C_{i}(b)\lor C_{i}(c)\lor C_{i}(d)\lor{L_{abc}}\lor{L_{bcd}}\lor\overline{TR_{abc}(q_{1})}\lor\overline{TR_{acd}(q_{2})} |  | (14) |

2. Case 3-cup + 3-cap: L a ​ b ​ d ⇔ L a ​ c ​ d ¯ L_{abd}\iff\overline{L_{acd}}. In CNF format, these conditions are written as follows:

 | C i ​ ( a) ∨ C i ​ ( b) ∨ C i ​ ( c) ∨ C i ​ ( d) ∨ L a ​ b ​ d ∨ L a ​ c ​ d ¯ ∨ T ​ R a ​ b ​ c ​ ( q 1) ¯ ∨ T ​ R b ​ c ​ d ​ ( q 2) ¯ C_{i}(a)\lor C_{i}(b)\lor C_{i}(c)\lor C_{i}(d)\lor{L_{abd}}\lor\overline{L_{acd}}\lor\overline{TR_{abc}(q_{1})}\lor\overline{TR_{bcd}(q_{2})} |  | (15) |

 | C i ​ ( a) ∨ C i ​ ( b) ∨ C i ​ ( c) ∨ C i ​ ( d) ∨ L a ​ b ​ d ¯ ∨ L a ​ c ​ d ∨ T ​ R a ​ b ​ c ​ ( q 1) ¯ ∨ T ​ R b ​ c ​ d ​ ( q 2) ¯ C_{i}(a)\lor C_{i}(b)\lor C_{i}(c)\lor C_{i}(d)\lor\overline{L_{abd}}\lor{L_{acd}}\lor\overline{TR_{abc}(q_{1})}\lor\overline{TR_{bcd}(q_{2})} |  | (16) |

### 4.5 Generalization to the Non-convex Case ( h n ​ c h_{nc})

To calculate the function h n ​ c h_{nc}, where the convexity condition is not mandatory, the algorithm generates an expanded set of clauses. In this case, a prohibition is imposed on any subset of 4 points of color i i if the total number of points inside the union of triangles forming the triangulation of the given quadruple does not exceed k i k_{i}. This is implemented through an exhaustive search of orientation combinations L L and imposing corresponding constraints on the density variables T ​ R TR.

### 4.6 Generalization to 4-islands ( h i ​ s ​ l h_{isl})

When searching for islands, the criterion for prohibition is also the total number of points inside the convex hull of a quadruple of points of color i i. Depending on the relative positions, this condition is formulated as follows:

1. 1.

If the quadruple is in a convex position, the sum of interior points in the two triangles making up its triangulation is taken into account.

2. 2.

If one point is inside the triangle formed by the other three, the number of points inside this (outer) triangle is considered, and the limit of interior points is increased by one (accounting for the innermost point of the quadruple itself).

### 4.7 Symmetry Breaking

To significantly optimize the search space, we fix the orientation of all triples containing the point with the smallest index:

 | ∀ 0 < b < c < n: L 0 ​ b ​ c = true \forall_{0<b<c<n}:\quad L_{0bc}=\text{true} |  | (17) |

According to Scheucher’s results [11], any finite set of points in the plane in general position can be renumbered such that the condition L 0 ​ b ​ c = true L_{0bc}=\text{true} is satisfied for all b < c b<c, and then affinely transformed into an order-type equivalent set whose points are ordered by the x x -coordinate. Thus, this constraint does not narrow the search space and is applicable to all abstract monotone signotopes.

## 5 Geometric Realization and Search for Extremal Configurations

To confirm the equality h ∗ ​ ( …) = h ~ ∗ ​ ( …) h_{*}(\dots)=\tilde{h}_{*}(\dots), it is necessary to demonstrate the existence of a point set 𝒳 \mathcal{X} realizing at least one maximal signotope. In this work, we applied two complementary methods for finding coordinates.

### 5.1 Local Stochastic Search Method

This iterative approach is based on the direct variation of point coordinates in ℝ 2 \mathbb{R}^{2}. The process begins with the generation of a random distribution of N N points in the plane. At each step, the algorithm calculates the number of forbidden structures (for example, monochromatic convex n i n_{i} -polygons with no more than k i k_{i} interior points) to be excluded.

The algorithm selects a random point and moves it to a new, randomly chosen position. If the modified configuration is characterized by a smaller or equal number of forbidden figures compared to the previous state, the movement is fixed; otherwise, the point returns to its original position. The process is repeated until the undesirable structures are fully eliminated.

The advantage of the method is the possibility of searching for high-symmetry realizations (by coordinated movement of groups of points while preserving the symmetry group). The disadvantage is the low convergence rate in the vicinity of local minima. Note that the efficiency of the approach can be significantly improved using the simulated annealing algorithm, where the probability of accepting a worse step decreases exponentially with a drop in the temperature parameter, allowing the system to escape local optima.

### 5.2 Linear Subreduction Method

Synthesis of Boolean signotope constraints with linear arithmetic theory within the SMT framework proved to be the most effective method. The Z3 SMT solver from Microsoft [46] was used as the primary tool.

The general task of finding coordinates for a given signotope reduces to solving a system of non-linear inequalities. In our model, the connection between logic variables L a ​ b ​ c L_{abc} and point coordinates p i = ( x i, y i) p_{i}=(x_{i},y_{i}) is specified in the form of disjunctive conditions:

 | L a ​ b ​ c ∨ ( x b − x a) ​ y c + ( x a − x c) ​ y b + ( x c − x b) ​ y a ⩾ 1 L_{abc}\penalty\ \penalty\ \lor\penalty\ \penalty\ (x_{b}-x_{a})y_{c}+(x_{a}-x_{c})y_{b}+(x_{c}-x_{b})y_{a}\geqslant 1 |  | (18) |

 | L a ​ b ​ c ¯ ∨ ( x b − x a) ​ y c + ( x a − x c) ​ y b + ( x c − x b) ​ y a ⩽ − 1 \overline{L_{abc}}\penalty\ \penalty\ \lor\penalty\ \penalty\ (x_{b}-x_{a})y_{c}+(x_{a}-x_{c})y_{b}+(x_{c}-x_{b})y_{a}\leqslant-1 |  | (19) |

Since these conditions are quadratic relative to variables x x and y y, SMT solvers effectively find solutions only for small values of N N. We optimized the task by fixing the abscissae of the points (using a uniform distribution x i = i x_{i}=i or an exponential spacing x i ∈ { …, − C 2, − C, − 1, [0], 1, C, C 2, … } x_{i}\in\{\dots,-C^{2},-C,-1,[0],1,C,C^{2},\dots\}, where the entry [0] [0] denotes the presence of a central point only for configurations with an odd N N). This turns quadratic inequalities into linear ones relative to the ordinates y i y_{i}. With such a linearized problem, the SMT solver performs orders of magnitude faster.

The fundamental difference between our approach and classical verification methods (e.g., [11]) is that we do not look for a realization of a specific, pre-determined signotope. The full logic formula of the problem is fed to the SMT solver. Thus, the solver looks for coordinates for any of the entire set of admissible signotopes, satisfying both combinatorial and geometric constraints simultaneously. This significantly expands the search area and allows for finding realizations even in cases where the space of admissible signotopes is extremely limited.

Note that for searching the ordinates y i y_{i} in the SMT model, we utilized the integer data type ( Int) instead of the real type ( Real). From the perspective of the Z3 solver’s architecture, this allows the use of specialized linear integer arithmetic (LIA) algorithms, which in some cases demonstrate better convergence on dense systems of inequalities.

Although point coordinates in the plane are a priori real numbers, transitioning to integers in our problem does not limit the generality of the search. Since the orientation function L a ​ b ​ c L_{abc} is invariant under positive scaling, any real solution to the system of linear inequalities can be approximated by a rational one due to the openness of the feasible region, and then brought to integer form by multiplying by a common denominator. Thus, the use of the Int type not only makes the sought coordinates more representative but also optimizes the computational load on the SMT solver.

It is worth noting that fixing the abscissae x i x_{i} imposes additional constraints on the geometry of the set 𝒳 \mathcal{X}, which theoretically could lead to the loss of some realizations. Strictly speaking, an equivalent point set with a given set of x x -coordinates does not exist for every realizable signotope. Nevertheless, this approach is dictated by the need to achieve an acceptable computation speed.

The motivations for choosing fixed x i x_{i} values are as follows:

1. 1.

Exponential Spacing: Using the grid x i ∈ { …, − C 2, − C, − 1, 0, 1, C, C 2, … } x_{i}\in\{\dots,-C^{2},-C,-1,0,1,C,C^{2},\dots\} allows for the imitation of stretched configurations, which are often found in extremal examples of order type theory.

2. 2.

Density of Realizations: Empirical evidence suggests the space of geometric realizations for most signotopes is sufficiently vast, allowing the sought configuration to be found even in a limited subspace with fixed x i x_{i}.

3. 3.

Empirical Completeness: In almost all cases we considered where the SAT solver confirmed the existence of an abstract signotope, the SMT solver successfully found its integer realization even with the simplest distribution x i = i x_{i}=i.

Thus, the linear subreduction method is a powerful tool for fast verification, allowing the automated confirmation of the equality h ∗ ​ ( ⋯) = h ~ ∗ ​ ( ⋯) h_{*}(\cdots)=\tilde{h}_{*}(\cdots) for the majority of configurations.

## 6 The ES_color.py Software Package

To conduct numerical experiments and automatically generate logical formulas, a specialized software package was developed in the Python language — ES_color.py. The program supports generating output data in DIMACS (for SAT solvers) and SMT-LIB v2 (for SMT solvers) formats.

### 6.1 Configuration Parameters

The script is executed from the command line using the following key parameters:

- •

n=N — total number of points N N in the sought configuration.

- •

tr_i=k_i — constraint on the maximum number of interior points for triangles of color i i. For example, the parameters tr1=0 tr2=0 initiate the prohibition of empty triangles of the first and second colors, respectively.

- •

cv_i=k_i — exclusion of configurations containing convex quadrilaterals of color i i considering the limit k i k_{i} (problem h h).

- •

nc_i=k_i — exclusion of any (not necessarily convex) quadrilaterals of color i i containing no more than k i k_{i} points inside (problem h n ​ c h_{nc}).

- •

is_i=k_i — exclusion of monochromatic 4-islands (problem h i ​ s ​ l h_{isl}).

- •

sb=off — deactivation of symmetry breaking algorithms.

- •

xgrid=C — switching to the mode of generating an SMT2 formula to search for a geometric realization. If C = 1 C=1, a linear grid of abscissae x i = i x_{i}=i is used. If C > 1 C>1, the base of an exponential grid is set: x i ∈ { …, − C 2, − C, − 1, [0], 1, C, C 2, … } x_{i}\in\{\dots,-C^{2},-C,-1,[0],1,C,C^{2},\dots\}. This mode automatically deactivates the sb option.

### 6.2 Usage Examples and Integration with Solvers

To search for an abstract signotope, the result is directed to a SAT solver. Below is an example of verifying the equality h ~ n ​ c ​ ( 4, 0, 3, 0) = 14 \tilde{h}_{nc}(4,0;3,0)=14:

[⬇][5]

./ ES_color. py nc1 =0 tr2 =0 n =13 | kissat

SATISFIABLE

./ ES_color. py nc1 =0 tr2 =0 n =14 | kissat

UNSATISFIABLE

To confirm geometric realizability and calculate the ordinates y i y_{i}, the xgrid mode is used. The generated SMT2 formula is passed to the Z3 solver via the standard stream (pipe):

[⬇][6]

./ ES_color. py nc1 =0 tr2 =0 n =13 xgrid =1 | z3 - in | sed ':a;N;s/)\n (/) (/g;ba'

sat

(( x0 0) ( y0 (- 278)) ( k1 true) ( k14 false))

(( x1 1) ( y1 (- 172)) ( k2 false) ( k15 true))

...

(( x11 11) ( y11 186) ( k12 false) ( k25 true))

(( x12 12) ( y12 208) ( k13 true) ( k26 false))

The Z3 output in this case contains not only the verdict sat/unsat but also, in the case of sat, the specific values of the coordinates y i y_{i} and the color distribution C i ​ ( a) C_{i}(a) for all points, allowing for instant verification and visualization of the found example.

## 7 Answer Set Programming

For independent verification of the results obtained using the imperative SAT generator in Python, an alternative logical model was developed in a declarative programming language. Using the clingo system [47] allows the description of geometric constraints in terms of predicate logic, which ensures a high level of abstraction.

The fundamental advantage of this approach lies in the exceptional conciseness of the code: the entire logic of the problem — including signotope axioms, point inclusion predicates, and conditions on forbidden configurations — is implemented in a few dozen lines. Such transparency significantly simplifies the audit of the algorithm and minimizes the likelihood of introducing implementation errors that may occur during the manual formation of complex CNF structures.

Below is the full text of the ASP model used for cross-checking the calculations:

[⬇][7]

pt (0.. n -1).

% --- SELECT TARGET POLYGONS ---

% Format: ins(Type, ColorID, MaxInteriorPoints)

ins ( pr, p1, pr1;

tr, t1, tr1; tr, t2, tr2; tr, t3, tr3; tr, t4, tr4; tr, t5, tr5;

cv, c1, cv1; cv, c2, cv2; cv, c3, cv3;

cv, i1, is1; cv, i2, is2; cv, i3, is3;

is, i1, is1 +1; is, i2, is2 +1; is, i3, is3 +1;

( nc; cv), n1, nc1; ( nc; cv), n2, nc2; ( nc; cv), n3, nc3).

#const is1 =-2. #const is2 =-2. #const is3 =-2.

% --- GENERATORS ---

% Assign exactly one color to each point

1{ c ( A, Z): ins ( _, Z, I), I =0..99}1:- pt ( A).

#heuristic c ( A, Z): pt ( A), ins ( _, Z, I), I =0..99. [10, level]

% Assign exactly one rotation to each triplet (Chirotope base)

1{ l ( A, B, C, R): R =(-1;1)}1:- pt ( A), pt ( B), pt ( C), A < B, B < C.

% --- GEOMETRIC CONSTRAINTS (Axioms for Signotope) ---

% These ensure that the relative positions of points are physically possible

:- l ( A, B, C, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( A, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( B, C, D, R).

:- l ( A, B, D, R), l ( A, C, D,- R), l ( B, C, D, R).

% Symmetry breaking: fix orientation of the first triplets to avoid rotated solutions

:- l (0, B, C,-1), sb!= off.

% --- INTERIOR POINTS LOGIC ---

% Define if point X is inside triangle (A,B,C) based on relative orientations

i ( A, B, C, X):- l ( A, X, B, R), l ( A, X, C,- R), B < C.

i ( A, B, C, X):- l ( B, X, C, R), l ( A, X, C,- R), A < B.

% Calculate if triangle (A,B,C) contains no more than J interior points

tr ( A, B, C, J):- pt ( A), pt ( B), pt ( C), A < B, B < C, { i ( A, B, C, X)}<= J, J =0.. I, ins ( _, _, I), I =0..99.

% --- SHAPE INTEGRITY CONSTRAINTS ---

% Pairs

:- ins ( pr, Z, _), c ( A, Z), c ( B, Z), A < B.

% Triangles

:- ins ( tr, Z, I), c ( A, Z), c ( B, Z), c ( C, Z), A < B, B < C, tr ( A, B, C, I).

% Convex quadrilaterals

:- ins ( cv, Z, I), l ( A, B, C, R), l ( B, C, D, R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, C, I1), tr ( A, C, D, I2), I1 + I2 = I.

:- ins ( cv, Z, I), l ( A, B, D, R), l ( A, C, D,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, C, I1), tr ( B, C, D, I2), I1 + I2 = I.

% Non-convex quadrilaterals

:- ins ( nc, Z, I), l ( A, B, D, R), l ( A, B, C,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, C, I1), tr ( A, B, D, I2), I1 + I2 = I.

:- ins ( nc, Z, I), l ( A, B, D, R), l ( A, B, C,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, C, I1), tr ( B, C, D, I2), I1 + I2 = I.

:- ins ( nc, Z, I), l ( A, B, D, R), l ( A, B, C,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, D, I1), tr ( B, C, D, I2), I1 + I2 = I.

:- ins ( nc, Z, I), l ( A, C, D, R), l ( B, C, D,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, C, I1), tr ( A, C, D, I2), I1 + I2 = I.

:- ins ( nc, Z, I), l ( A, C, D, R), l ( B, C, D,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, C, I1), tr ( B, C, D, I2), I1 + I2 = I.

:- ins ( nc, Z, I), l ( A, C, D, R), l ( B, C, D,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, C, D, I1), tr ( B, C, D, I2), I1 + I2 = I.

% 4-islands

:- ins ( is, Z, I), l ( A, B, D, R), l ( A, B, C,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, C, D, I).

:- ins ( is, Z, I), l ( A, C, D, R), l ( B, C, D,- R), c ( A, Z), c ( B, Z), c ( C, Z), c ( D, Z), A < B, B < C, C < D, tr ( A, B, D, I).

#show c /2.

#show l /4.

### 7.1 Dynamic Parameterization and Constraint Activation Mechanism

A feature of the presented ASP model is the use of the ins(Type, ColorID, MaxPoints) predicate as a system registry of active constraints. This allows for the dynamic determination of the number of colors involved and the types of geometric prohibitions without modifying the program’s source code.

1. 1.

Parameter Activation Mechanism: The key logic of the model is embedded in the rule for generating the coloring:

[⬇][8]

1{ c ( A, Z): ins ( _, Z, I), I =0..99}1:- pt ( A).

This rule uses the matching method with the interval I=0..99. When a parameter is set via the command line (for example, -c nc1=0), the constant nc1 receives a specific integer value. The condition ins(nc, n1, I), I=0..99 becomes true, as the value of I falls within the specified range, which activates the color identifier n1 for the generator c(A,Z).

If a parameter for a specific color (for example, tr5) is not passed, the corresponding constant remains undefined, and the ins predicate for that color is not evaluated. As a result, the generator c(A,Z) excludes this color from the search space when coloring points. Thus, the number of active colors in the model strictly corresponds to the number of given external constraints.

1. 2.

Constraint Selectivity: Each exclusion rule (lines 29–50 of the listing) is associated with the corresponding type from the ins predicate. This ensures that the logic, for example, of non-convex quadrilaterals ( nc), is applied exclusively to those points whose color Z was activated through the corresponding parameter. This approach allows combining diverse geometric requirements for different color classes within a single program.

2. 3.

Exhaustive Search Optimization: For Erdős–Szekeres type problems, the proof of the absence of solutions ( UNSAT verdict) is critical, as it serves as strict confirmation of the exact value of the function h ~ ∗ \tilde{h}_{*}. For complex configurations, the verification procedure may require significant computational resources.

The #heuristic directive instructs the solver to prioritize decisions regarding the coloring variables c(A,Z). Setting a high priority ( 10, level) forces the system to distribute points by color first, which significantly accelerates the Unit Propagation procedure and allows for more efficient pruning of search tree branches that do not contain valid configurations. This is a decisive factor for obtaining the UNSAT result in an acceptable time.

Additionally, to speed up the verification process, specific settings for the clingo solver are used:

  - •

--configuration=frumpy — activation of a mode oriented towards intensive depth-first search with frequent conflicts. This preset demonstrated the highest efficiency when analyzing problems with a small number of colors (1–2), where the constraint density is high and the search tree requires rigid and fast pruning of non-promising branches.

  - •

--configuration=crafty — a preset that proved to be most effective for problems with three or more colors. Its advantage in multicolored configurations is due to a more flexible restart mechanism and conflict-learning heuristics, which allow for faster structure finding in a more sparse and multidimensional search space.

  - •

--sat-p=3 — use of a SAT-level preprocessor to simplify the logical formula directly during the search process (on the fly).

  - •

--heuristic=Domain — prioritization of variable selection based on their domain structure (in combination with the author’s #heuristic directive), which is critically important for the prompt pruning of unsatisfiable search tree branches.

Example of a run to verify the value h ~ n ​ c ​ ( 4, 0, 3, 0) = 14 \tilde{h}_{nc}(4,0;3,0)=14 for bicolored sets:

[⬇][9]

clingo ES_color. lp -- configuration = frumpy -- sat - p =3 -- heuristic = Domain - c nc1 =0 - c tr2 =0 - c n =13

SATISFIABLE

clingo ES_color. lp -- configuration = frumpy -- sat - p =3 -- heuristic = Domain - c nc1 =0 - c tr2 =0 - c n =14

UNSATISFIABLE

In this scenario, the solver activates two colors ( n1 and t2), applies the corresponding types of geometric constraints to them, and performs an exhaustive search to formally prove the absence of solutions.

### 7.2 Finding Coordinates Using the clingo-lpx Solver

As an alternative method for finding geometric coordinates, the clingo-lpx solver was investigated. This extension integrates the simplex method directly into the Answer Set Programming (ASP) search process, allowing the formulation of linear constraints over rational numbers within the logical program.

To implement the linear subreduction method, an additional module was developed, formalizing the connection between signotope orientations and point ordinates y i y_{i} with fixed abscissae x i x_{i}:

Listing 1: lpx — extension for linking logic variables with coordinates

[⬇][10]

#const sb = off.

#const xgrid =1.

x ( N, N):- pt ( N), xgrid =1.

x (0, n /2):- xgrid >1, n \2=1.

x (-( xgrid **( n /2- N -1)), N):- pt ( N), N < n /2, xgrid >1.

x ( xgrid **( N -( n -1)/2-1), N):- pt ( N), N >( n -1)/2, xgrid >1.

& sum { KA *y ( XA); KB *y ( XB); KC *y ( XC)} >= 1:- l ( A, B, C,1), x ( XA, A), x ( XB, B), x ( XC, C), KA = XC - XB, KB = XA - XC, KC = XB - XA, xgrid >0.

& sum { KA *y ( XA); KB *y ( XB); KC *y ( XC)} <= -1:- l ( A, B, C,-1), x ( XA, A), x ( XB, B), x ( XC, C), KA = XC - XB, KB = XA - XC, KC = XB - XA, xgrid >0.

#### 7.2.1 Features and Performance

The clingo-lpx solver allows for finding exact rational values of the ordinates y i y_{i} (in the form of common fractions) that satisfy the given signotope. Below is an example of the work for the problem h n ​ c ​ ( 4, 0, 3, 0) = 14 h_{nc}(4,0;3,0)=14 at N = 13 N=13:

[⬇][11]

clingo - lpx lpx ES_color. lp - c nc1 =0 - c tr2 =0 - c n =13 - c xgrid =1

...

y (0)=4719/224 y (1)=11 y (2)=7801/448 y (3)=-323/112 y (4)=-10833/448 y (5)=-10411/224

y (6)=4143/224 y (7)=-3489/112 y (8)=-1231/32 y (9)=4591/896 y (10)=1 y (11)=0 y (12)=0

SATISFIABLE

Despite the deep integration of arithmetic and logic, empirical tests have shown that the clingo-lpx solver almost always lags behind the Z3 SMT solver in terms of performance. This is likely due to the fact that Z3 implements more aggressive conflict-driven clause learning (CDCL) strategies for mixed (logic-arithmetic) problems.

Nevertheless, the use of clingo-lpx remains promising for configurations with small N N, as it allows the full model to be described within a single declarative language without the need for external CNF generators and intermediate data formats. This makes the clingo-lpx -based approach an effective and convenient extension of the main ASP code for the rapid verification of new geometric hypotheses.

## 8 Computational Experiment Results

### 8.1 Methodology and Tools

To verify combinatorial configurations in this study, SAT solvers representing various stages of the development of logical inference search algorithms were used. MiniSat [48] and Glucose [49] were chosen as baselines. These classical representatives of the CDCL architecture have been the industry standard for the past decades due to their stability and predictability when working with high-density combinatorial problems.

As a modern high-performance solution (State-of-the-Art), the Kissat solver [50] (version 4.0.4) was used, which demonstrated the best results in recent international SAT Competitions. Unlike universal SMT systems such as Z3, which are optimized to support a wide range of logical theories and carry additional computational overhead for their processing, Kissat is extremely specialized exclusively in Boolean satisfiability problems. The high efficiency of this tool is achieved through aggressive inprocessing formula simplification methods and the dynamic adaptation of heuristics to the structure of a specific instance.

### 8.2 Computationally Simple Cases

This category includes all scenarios for which the value of the function h ~ ∗ ​ ( …) \tilde{h}_{*}(\dots) does not exceed 20, with the exception of three specific cases:

 | h ~ ​ ( 3, 2, 3, 2, 3, 2, 3, 2) = 17, h ~ ​ ( 3, 4, 3, 4, 3, 4, 3, 4, 3, 4) = 17, h ~ i ​ s ​ l ​ ( 4, 3, 4, 3, 4, 3) = 19, \tilde{h}(3,2;3,2;3,2;3,2)=17,\quad\tilde{h}(3,4;3,4;3,4;3,4;3,4)=17,\quad\tilde{h}_{isl}(4,3;4,3;4,3)=19, |  |

a detailed analysis of which is presented in the next section.

The running time of SAT/ASP solvers for all configurations with up to N = 14 N=14 points were below 12 seconds. As the set size increased to N = 17 N=17, the verification time generally did not exceed 1000 seconds. The only exception was the case h ~ n ​ c ​ ( 3, 3, 3, 3, 3, 3) = 16 \tilde{h}_{nc}(3,3;3,3;3,3)=16, which required approximately 52,000 CPU seconds. For problems with N = 20 N=20 points, the search time was less than 70,000 seconds.

A comparative analysis of the performance of various tools is available in the project repository 5 5 5 [https://github.com/koshelevv/Erdos-Szekeres/tree/main/colored_points][12]; Kissat proved to be the most effective solver for these problems in practice.

For all specified cases, the linear subreduction method allowed the construction of extremal point configurations on a linear abscissa grid ( x i = i x_{i}=i). In most cases, the coordinate search time ranged from a few seconds to 750 seconds.

For three computationally intensive tasks:

 | h i ​ s ​ l ​ ( 4, 0, 4, 2) = 16, h ⁡ ( 4, 1, 4, 2) = 16, h ⁡ ( 4, 0, 4, 4) = 17 h_{isl}(4,0;4,2)=16,\quad h(4,1;4,2)=16,\quad h(4,0;4,4)=17 |  | (20) |

the time required to generate the realization was 4, 2.6, and 3 hours, respectively.

### 8.3 Computationally Complex Cases

This section presents the results for the most resource-intensive configurations. Summary data on solver runtimes and parameters of the found realizations are provided in the table below.

Computational results for complex cases; verification time is given in CPUh. |

 |  |  | clingo –heuristic |  | Linear Subreduction Method |

Parameters | 𝐡 ~ ​ ( ⋯) \mathbf{\tilde{h}(\cdots)} | kissat | Default | Domain | Decomp. | 𝐡 ~ − 𝟏 \mathbf{\tilde{h}-1} | | 𝒳 | \mathbf{|\mathcal{X}|} | 𝐭 𝒳 \mathbf{t_{\mathcal{X}}} |

h ⁡ ( 3, 2, 3, 2, 3, 2, 3, 2) h(3,2;3,2;3,2;3,2) | 18 | ∘ \circ | 447 | 294 | 37 G 37^{G} | 17 | 17 ( 4) 17^{(4)} | 8.8 |

h ⁡ ( 3, 4, 3, 4, 3, 4, 3, 4, 3, 4) h(3,4;3,4;3,4;3,4;3,4) | 18 | 29 | ∘ \circ | 324 | ∘ \circ | 17 | 17 ( 4) 17^{(4)} | 4.5 |

h ⁡ ( 3, 0, 3, 0, 3, 4) h(3,0;3,0;3,4) | 21 | 43 | 67 | 73 | ∘ \circ | 20 | 20 | 4.2 |

h ⁡ ( 3, 0, 3, 0, 3, 3) h(3,0;3,0;3,3) | 23 | ∘ \circ | 884 | 1067 | ∘ \circ | 22 | 22 | 5.8 |

h ⁡ ( 4, 0, 4, 3) h(4,0;4,3) | 21 | 5.6 | 8.7 | 8.7 | ∘ \circ | 20 | 19 | 17 |

h i ​ s ​ l ​ ( 4, 0, 4, 1) h_{isl}(4,0;4,1) | 22 | 57 | 55 | 100 | ∘ \circ | 21 | 21 | 33 |

h ⁡ ( 4, 0, 4, 2) h(4,0;4,2) | 25 | ∘ \circ | 1619 | ∘ \circ | 563 G 563^{G} | 24 | 22 ( 4) 22^{(4)} | 1783 |

h ⁡ ( 4, 0, 3, 0) h(4,0;3,0) | 26 | ∘ \circ | 1193 | ∘ \circ | 353 G 353^{G} | 25 | 25 | LSS |

h n ​ c ​ ( 4, 0, 4, 0) h_{nc}(4,0;4,0) | 26 | ∘ \circ | 1583 | ∘ \circ | 350 G 350^{G} | 25 | 25 | 97 |

h n ​ c ​ ( 4, 2, 4, 2, 4, 2) h_{nc}(4,2;4,2;4,2) | 22 | ∘ \circ | ∘ \circ | ∘ \circ | 880 M 880^{M} | 21 | 20 | 543 |

h i ​ s ​ l ​ ( 4, 3, 4, 3, 4, 3) h_{isl}(4,3;4,3;4,3) |  | 18 ∗ 18^{*} | 18 | 5 |

h i ​ s ​ l ​ ( 4, 2, 4, 2, 4, 2) h_{isl}(4,2;4,2;4,2) |  | 27 ∗ 27^{*} | 24 ( 4) 24^{(4)} | 61 |

h ⁡ ( 3, 0, 3, 0, 3, 2) h(3,0;3,0;3,2) | Experiments in progress | 25 ∗ 25^{*} | 25 | 1 |

h ⁡ ( 3, 0, 3, 0, 3, 1) h(3,0;3,0;3,1) | (decomposition and significant resources required) | 34 ∗ 34^{*} | 32 | 855 |

h ⁡ ( 4, 0, 4, 1) h(4,0;4,1) |  | 33 ∗ 33^{*} | 28 | 756 |

h ⁡ ( 3, 1, 3, 1, 3, 1, 3, 1) h(3,1;3,1;3,1;3,1) |  | 35 ∗ 35^{*} | 28 | LSS |

h ⁡ ( 3, 3, 3, 3, 3, 3, 3, 3, 3, 3) h(3,3;3,3;3,3;3,3;3,3) |  | 22 ∗ 22^{*} | 21 ( 4) 21^{(4)} | 8302 |

h ⁡ ( 3, 2, 3, 2, 3, 2, 3, 2, 3, 2) h(3,2;3,2;3,2;3,2;3,2) |  | 32 ∗ 32^{*} | 26 | 821 |

h i ​ s ​ l ​ ( 4, 0, 4, 0) h_{isl}(4,0;4,0) | Existence of h ~ \tilde{h} and h h is open; | 48 ∗ ⁣ ∗ 48^{**} | 35 | manual |

h ⁡ ( 4, 0, 4, 0) h(4,0;4,0) | current lower bounds are presented. | 90 ∗ ⁣ ∗ 90^{**} | 46 | manual |

∘ \circ — experiment in progress or not conducted due to data sufficiency;
∗ — size of the largest signotope found (we assume these are maximal);
∗∗ — size of the largest signotope found without a guarantee of maximality;
G / M — use of Glucose / Minisat solvers on subformulas after decomposition;
(4) — use of abscissa grid No. 4 instead of the default grid No. 1;
| 𝒳 | |\mathcal{X}| — cardinality (number of points) of the found geometric realization;
t 𝒳 t_{\mathcal{X}} — coordinate search time using the linear subreduction method;
LSS — Local Stochastic Search method;
manual — solution found manually, computer used only for visualization.

To verify the most labor-intensive cases, we applied a method of decomposing the original logical formula into subproblems by fixing the coloring of the initial segment of points. In several cases (particularly for homogeneous multicolored problems), we utilized the color equivalence property, which allows, without loss of generality, fixing the color of the first point or specific combinations of initial colorings to reduce the number of subproblems:

- •

For h ~ ​ ( 3, 2, 3, 2, 3, 2, 3, 2) = 18 \tilde{h}(3,2;3,2;3,2;3,2)=18, the symmetry of the four colors allowed us to consider only five variants of fixing the colors of the first three points: 123,122,121,112 123,122,121,112, and 111 111, instead of the theoretically possible 4 3 = 64 4^{3}=64 initial colorings. The case 111 111 was immediately excluded due to the obvious presence of a monochromatic empty triangle. The Glucose solver (2023) completed the calculations in 24, 0.5, 7, and 5 CPUh, respectively.

- •

The value h ~ ​ ( 4, 0, 4, 2) = 25 \tilde{h}(4,0;4,2)=25 was obtained by decomposition into 2981 subformulas with fixed colors for the first 12 points. Trivial sets (e.g., 5 consecutive points of the same color) were excluded from the search. The solution time for the subproblems varied from fractions of a second to 41,240 seconds, with total costs amounting to 563 CPUh.

- •

For h ~ ​ ( 4, 0, 3, 0) = 26 \tilde{h}(4,0;3,0)=26, the problem was divided into 2387 subformulas (fixing colors for the first 13 points). Configurations with five consecutive points of the first color or three consecutive points of the second color were excluded. With a maximum time per subproblem of 34,600 seconds, the total costs for the Glucose solver were 353 CPUh.

- •

The proof of h ~ n ​ c ​ ( 4, 0, 4, 0) = 26 \tilde{h}_{nc}(4,0;4,0)=26 required decomposition into 1706 subproblems (fixing colors for the first 13 points). Due to color symmetry, the first point was always assigned color 1. Sets with four consecutive points of the same color were excluded. The final time ( Glucose) was 350 CPUh, with a maximum per subproblem of 48,600 seconds.

- •

Verification of h ~ n ​ c ​ ( 4, 2, 4, 2, 4, 2) = 22 \tilde{h}_{nc}(4,2;4,2;4,2)=22 was performed through 23,907 subproblems (fixing colors for the first 12 points). Using symmetry for the first point and filtering trivial sets (6 consecutive points, 4 of which are monochromatic) allowed for optimization of the search. The MiniSat solver utilized 880 CPUh (maximum 13,670 seconds).

For the critical cases mentioned above, the Glucose and MiniSat solvers do not reach an UNSAT result on the original formula without decomposition, even when significantly exceeding the total time limit. Modern latest-generation SAT solvers, such as CaDiCaL and Kissat, which use advanced inprocessing methods, are potentially capable of processing such problems without prior partitioning. Tests on lower-power instances confirm their high efficiency; however, the full verification of the most complex formulas in a single pass remains a subject of current research.

The application of the ASP approach enabled the direct verification of several labor-intensive cases. Unlike the Glucose and MiniSat solvers, which required partitioning the problem into thousands of subproblems, the clingo system successfully handled the analysis of the original formulas in their entirety. Although the total runtime of clingo in some scenarios exceeded the cumulative CPU time of parallel runs, the ability to verify without manual intervention in the search structure significantly increases the reliability and transparency of the experiment.

A comparison of the ultimate computational capabilities demonstrates a significant asymmetry: while for two-color problems modern solvers allow the verification of configurations up to N = 26 N=26 points, the transition to four or more colors substantially constrains the scope of accessible computations to N = 18 N=18. Such a sharp decrease in the threshold confirms that multi-coloring is a critical factor exponentially influencing the complexity of geometric models of this type.

Our experience confirms that the choice of the optimal preset in clingo directly correlates with the number of colors: frumpy is most effective for 1–2 colors, while for 3 or more colors, crafty maintains a stable advantage.

Part of the results presented in the table was obtained at a stage before the implementation of the --heuristic=Domain optimization. Nevertheless, the achieved computational correctness allowed for the fixing of the sought values. Ongoing recalculations with the Domain parameter are aimed at refining the performance boundaries of the method. The only case that retained its exceptional laboriousness and required decomposition even within the ASP approach remains the configuration h ~ n ​ c ​ ( 4, 2, 4, 2, 4, 2) \tilde{h}_{nc}(4,2;4,2;4,2).

#### 8.3.1 Search for Coordinates: Linear Subreduction Method and Alternative Approaches

For the case h n ​ c ​ ( 4, 0, 4, 0) h_{nc}(4,0;4,0), a geometric realization of 25 points was constructed using the linear subreduction method:

(0, − - 746538137,B), (1, − - 3046660,A), (2, − - 646999721,A), (3,3839774366,A), (4,3093155294,B), (5,7276998680,B), (6,5993695355,A), (7,8,B), (8,106660406,A), (9, − - 1386562914,B), (10, − - 2879830757,A), (11,18199678130,A), (12,16147587405,B), (13,639962389,B), (14, − - 2228740740,A), (15, − - 8,A), (16,12743409974,A), (17,11892365617,B), (18,12428608367,A), (19,24846857556,B), (20,27927600703,A), (21,35677096872,A), (22,38225025694,B), (23, − - 15821880854,B), (24, − - 16319040999,B).

For the function h ⁡ ( 4, 0, 3, 0) h(4,0;3,0), a configuration of 25 points exhibiting 3-fold symmetry was found using the local stochastic search method; the linear subreduction method was not applied in this case. Coordinates:

(0,0,A), (126, − - 151,B), ( − - 193, − - 33,B), (67,184,B), (130, − - 123,A), ( − - 171, − - 51,A), (41,174,A), (62,249,A), (184, − - 178,A), ( − - 246, − - 70,A), (126, − - 163,A), ( − - 204, − - 27,A), (78,190,A), ( − - 30,195,B), (183, − - 71,B), ( − - 153, − - 123,B), (87,266,B), (185, − - 208,B), ( − - 273, − - 57,B), ( − - 492, − - 73,A), (183,463,A), (309, − - 390,A), ( − - 353, − - 127,A), (67,369,A), (286, − - 242,A).

The obtained results conclusively confirm the equalities:

 | h ⁡ ( 4, 0, 3, 0) = 26, h n ​ c ​ ( 4, 0, 4, 0) = 26. h(4,0;3,0)=26,\quad h_{nc}(4,0;4,0)=26. |  | (21) |

For the instances h ⁡ ( 4, 0, 4, 3) h(4,0;4,3), h ⁡ ( 4, 0, 4, 2) h(4,0;4,2), and h n ​ c ​ ( 4, 2, 4, 2, 4, 2) h_{nc}(4,2;4,2;4,2), the upper bound of the signotope was not reached, resulting in only interval estimates:

 | 20 ⩽ h ⁡ ( 4, 0, 4, 3) ⩽ 21, 23 ⩽ h ⁡ ( 4, 0, 4, 2) ⩽ 25, 21 ⩽ h n ​ c ​ ( 4, 2, 4, 2, 4, 2) ⩽ 22. 20\leqslant h(4,0;4,3)\leqslant 21,\quad 23\leqslant h(4,0;4,2)\leqslant 25,\quad 21\leqslant h_{nc}(4,2;4,2;4,2)\leqslant 22. |  | (22) |

For instances with a large number of points N N, where the exact value of h ~ ​ ( …) \tilde{h}(\dots) and the upper bound remain unknown (lower part of the table), the gap between the estimates may be significantly higher.

In the search for realizations, priority was given to the linear grid of abscissae ( x i = i x_{i}=i, parameter xgrid=1) to obtain less cumbersome integer solutions. However, in several cases, this strategy proved to be suboptimal. For instance, for the configurations h ⁡ ( 3, 2, 3, 2, 3, 2, 3, 2) h(3,2;3,2;3,2;3,2) and h ⁡ ( 3, 4, 3, 4, 3, 4, 3, 4, 3, 4) h(3,4;3,4;3,4;3,4;3,4), no realization of 17 points was found over several months of computation using the linear grid, whereas the solutions were obtained within a few hours upon switching to grid No. 4.

Similarly, in the analysis of h ⁡ ( 4, 0, 4, 2) h(4,0;4,2) and h ⁡ ( 3, 3, 3, 3, 3, 3, 3, 3, 3, 3) h(3,3;3,3;3,3;3,3;3,3), two instances of the solver were run in parallel for the first and fourth grids, respectively. In both cases, the computations on grid No. 4 were successful, while the processes on the linear grid were terminated due to timeout. The following section provides a theoretical justification for why the abscissa grid x i = i x_{i}=i demonstrates low efficiency in some scenarios.

Despite the fact that the average complexity of the problem grows exponentially with increasing N N, the distribution of search time is characterized by high variance. Cases of anomalously fast finding of answers at large N N are explained by the algorithm hitting narrow satisfiability zones in the early stages of the search tree traversal, which allows avoiding exhaustive analysis of conflicting configurations.

All found sets of coordinates are available in the project repository 6 6 6 [https://github.com/koshelevv/Erdos-Szekeres/tree/main/colored_points][12].

### 8.4 clingo-lpx and Comparative Analysis of Abscissa Grids

Although the clingo-lpx solver is inferior in performance to Z3, its use is considered appropriate in at least two scenarios:

- •

the application of cardinal constraints in the logical program (for example, specifying a fixed or minimum number of monochromatic empty triangles in the target configuration);

- •

the need to generate the full solution space to collect statistical data (option -n0).

For illustration, let us introduce the notations S 3 ​ ( N) S_{3}(N), S 4 ​ ( N) S_{4}(N), S 5 ​ ( N) S_{5}(N) for the sets of signotopes that minimize the number of convex and empty 3-, 4-, and 5-gons on N N points, respectively (within the monochromatic model).

Below is the logical program for searching for elements of these sets, as well as their intersections and differences:

Listing 2: Program for analyzing extremal properties of signotopes

[⬇][13]

pt (0.. n -1).

min_p3 (3,1; 4,3; 5,7; 6,13; 7,21; 8,31; 9,43; 10,58; 11,75; 12,94; 13,114).

min_p4 (3,0; 4,0; 5,1; 6,3; 7,6; 8,10; 9,15; 10,23; 11,32; 12,42; 13,51).

min_p5 (9,0; 10,1; 11,2; 12,3; 13,3; 14,6; 15,9; 16,11).

1{ l ( A, B, C, R): R =(-1;1)}1:- pt ( A), pt ( B), pt ( C), A < B, B < C.

:- l ( A, B, C, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( A, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( B, C, D, R).

:- l ( A, B, D, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l (1, B, C,-1), sb!= off.

i ( A, B, C, X):- l ( A, X, B, R), l ( A, X, C,- R), B < C.

i ( A, B, C, X):- l ( B, X, C, R), l ( A, X, C,- R), A < B.

ne ( A, B, C):- i ( A, B, C, X).

p3 ( A, B, C):- pt ( A), pt ( B), pt ( C), A < B, B < C, not ne ( A, B, C).

:- #count { A, B, C: p3 ( A, B, C)}= M, min_p3 ( n, M), p3 =-1.

:- #count { A, B, C: p3 ( A, B, C)}> M, min_p3 ( n, M), p3 = 1.

p4 ( A, B, C, D):- l ( A, B, C, R), l ( B, C, D, R), A < B, B < C, C < D, not ne ( A, B, C), not ne ( A, C, D).

p4 ( A, B, C, D):- l ( A, B, D, R), l ( A, C, D,- R), A < B, B < C, C < D, not ne ( A, B, C), not ne ( B, C, D).

:- #count { A, B, C, D: p4 ( A, B, C, D)}= M, min_p4 ( n, M), p4 =-1.

:- #count { A, B, C, D: p4 ( A, B, C, D)}> M, min_p4 ( n, M), p4 = 1.

p5 ( A, B, C, D, E):- l ( A, B, C, R), l ( B, C, D, R), l ( C, D, E, R), A < B, B < C, C < D, D < E, not ne ( A, B, C), not ne ( A, C, D), not ne ( A, D, E).

p5 ( A, B, C, D, E):- l ( A, B, C, R), l ( B, C, E, R), l ( A, D, E,- R), A < B, B < C, C < D, D < E, not ne ( A, B, C), not ne ( A, C, E), not ne ( A, D, E).

p5 ( A, B, C, D, E):- l ( A, B, D, R), l ( B, D, E, R), l ( A, C, E,- R), A < B, B < C, C < D, D < E, not ne ( A, B, D), not ne ( A, D, E), not ne ( A, C, E).

p5 ( A, B, C, D, E):- l ( A, C, D, R), l ( C, D, E, R), l ( A, B, E,- R), A < B, B < C, C < D, D < E, not ne ( A, C, D), not ne ( A, D, E), not ne ( A, B, E).

:- #count { A, B, C, D, E: p5 ( A, B, C, D, E)}= M, min_p5 ( n, M), p5 =-1.

:- #count { A, B, C, D, E: p5 ( A, B, C, D, E)}> M, min_p5 ( n, M), p5 = 1.

One of the central tasks in this field is the determination of the value X k ​ ( n) X_{k}(n) — the minimum number of empty k k -gons among all possible configurations of n n points in general position.

A significant milestone in studying this problem was the work of Dehnhardt [51], which first attempted to systematize the search for minimum values for small n n and formulated several hypotheses on the relationship between optimal point sets. In particular, the so-called Dehnhardt question was actively discussed in the literature: must a set of points that minimizes the number of convex and empty k k -gons ( X k X_{k}) also be minimizing for j j -gons ( X j X_{j}) when k ≠ j k\neq j? Dehnhardt assumed the existence of universal extremal configurations; however, his hypotheses regarding the exact values for n = 12 n=12 (specifically, X 3 ​ ( 12) = 95 X_{3}(12)=95 and X 4 ​ ( 12) = 44 X_{4}(12)=44) were subsequently adjusted.

With the development of computational geometry and the creation of the Order Type Database by Aichholzer and colleagues [52, 53], the verification of these assumptions on full samples became possible. It was proved that for n = 12 n=12, the direct connection between minima is broken: there exists a configuration that minimizes the number of pentagons ( X 5 ​ ( 12) = 3 X_{5}(12)=3), but is not optimal for triangles ( X 3 ​ ( 12) = 94 X_{3}(12)=94) and quadrilaterals ( X 4 ​ ( 12) = 42 X_{4}(12)=42).

###### Theorem 6.

For 3 ⩽ N ⩽ 11 3\leqslant N\leqslant 11, the equality S 3 ​ ( N) = S 4 ​ ( N) S_{3}(N)=S_{4}(N) holds. Furthermore, the relationship S 3 ​ ( 9) = S 4 ​ ( 9) = S 5 ​ ( 9) S_{3}(9)=S_{4}(9)=S_{5}(9) is true.

###### Proof.

To verify this statement, we calculate the differences of the specified pairs of sets using the developed logical program:

[⬇][14]

for n in `seq 3 11`; do

clingo minimize. lp -- configuration = crafty - c p3 =1 - c p4 =-1 - c n = $n;

clingo minimize. lp -- configuration = crafty - c p3 =-1 - c p4 =1 - c n = $n;

done

clingo minimize. lp -- configuration = crafty - c p4 =1 - c p5 =-1 - c n =9

clingo minimize. lp -- configuration = crafty - c p4 =-1 - c p5 =1 - c n =9

For all instances, the verdict UNSATISFIABLE was obtained, indicating the emptiness of the corresponding differences. Thus, any configuration of 3 ⩽ N ⩽ 11 3\leqslant N\leqslant 11 points that minimizes the number of empty triangles is also minimizing for convex and empty quadrilaterals, and vice versa. ∎

Verification of this fact for N > 11 N>11 requires significant computational resources and was not conducted within the scope of this study. Nevertheless, local stochastic search, run for N = 12 N=12 and N = 13 N=13 over several days, did not reveal any counterexamples.

For the cases N = 10 N=10 and N = 11 N=11, a strict inclusion S 4 ​ ( N) ⊊ S 5 ​ ( N) S_{4}(N)\subsetneq S_{5}(N) was established. Using the clingo-lpx extension, we found the coordinates of configurations that achieve the minimum number of convex and empty pentagons ( X 5 ​ ( 10) = 1 X_{5}(10)=1 and X 5 ​ ( 11) = 2 X_{5}(11)=2, respectively), while the number of triangles and quadrilaterals is not optimal: for N = 10 N=10, 59 and 24 were obtained (instead of X 3 = 58 X_{3}=58 and X 4 = 23 X_{4}=23), and for N = 11 N=11 — 76 and 33 (instead of X 3 = 75 X_{3}=75 and X 4 = 32 X_{4}=32).

[⬇][15]

clingo minimize. lp -- configuration = crafty - c p5 =-1 - c p4 =1 - c n =10

UNSATISFIABLE

clingo - lpx lpx minimize. lp -- configuration = crafty - c p5 =1 - c p4 =-1 - c n =10 - c xgrid =1

SATISFIABLE

y (0)=2023/3 y (1)=3673/6 y (2)=551 y (3)=459 y (4)=359 y (5)=525/2 y (6)=1577/8 y (7)=90 y (8)=0 y (9)=0

clingo minimize. lp -- configuration = crafty - c p5 =-1 - c p4 =1 - c n =11

UNSATISFIABLE

clingo - lpx lpx minimize. lp -- configuration = crafty - c p5 =1 - c p4 =-1 - c n =11 - c xgrid =1

SATISFIABLE

y (0)=47081/5 y (1)=-169/5 y (2)=361/3 y (3)=2261591/420 y (4)=1 y (5)=-7001731/420

y (6)=-2260751/210 y (7)=45 y (8)=15692/15 y (9)=0 y (10)=0

To conclude this section, we use the problem of minimizing empty polygons for a comparative analysis of the efficiency of various abscissa grids. Using the clingo-lpx solver, we calculated the number of signotopes from the set S 3 ​ ( N) = S 4 ​ ( N) S_{3}(N)=S_{4}(N) that possess a geometric realization for each grid with the xgrid parameter from 1 to 12 for 4 ⩽ N ⩽ 10 4\leqslant N\leqslant 10. The results are presented in Table 2.

[⬇][16]

for n in `seq 4 10`; do

for xgrid in `seq 0 12`; do

clingo - lpx minimize. lp lpx -- configuration = crafty - n0 -- quiet =2 -- enum - mode = bt - c p4 =1 - c n = $n - c xgrid = $xgrid;

done;

done

N | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

xgrid=0 | 4 | 22 | 224 | 2604 | 21408 | 31884 | 1937396 |

xgrid=1 | 4 | 22 | 212 | 2056 | 11876 | 7144 | 165048 |

xgrid=2 | 4 | 22 | 212 | 2064 | 13128 | 11000 | 335908 |

xgrid=3 | 4 | 22 | 212 | 2220 | 15304 | 17964 | 598560 |

xgrid=4 | 4 | 22 | 220 | 2408 | 16640 | 20524 | 688088 |

xgrid=5 | 4 | 22 | 220 | 2416 | 17076 | 21104 | 718560 |

xgrid=6 | 4 | 22 | 220 | 2420 | 17160 | 21344 | 725812 |

xgrid=7 | 4 | 22 | 220 | 2424 | 17164 | 21372 | 727884 |

xgrid=8 | 4 | 22 | 220 | 2424 | 17172 | 21388 | 729004 |

xgrid=9 | 4 | 22 | 220 | 2424 | 17172 | 21376 | 729196 |

xgrid=10 | 4 | 22 | 220 | 2424 | 17172 | 21376 | 729528 |

xgrid=11 | 4 | 22 | 220 | 2424 | 17172 | 21376 | 729580 |

xgrid=12 | 4 | 22 | 220 | 2424 | 17172 | 21376 | 729588 |

x ​ g ​ r ​ i ​ d = 0 xgrid=0 — corresponds to the total number of abstract signotopes (without abscissa constraints).

Table 2: Number of realizable signotopes from S 4 ​ ( N) S_{4}(N) depending on the choice of abscissa grid.

According to the data obtained, the uniform abscissa grid ( x ​ g ​ r ​ i ​ d = 1 xgrid=1) possesses the lowest realizability coverage (realizes the minimum number of signotopes). As the exponential spacing parameter of the grid increases, the number of successfully found realizations monotonically increases, confirming the advantage of non-linear grids in verifying complex configurations.

## 9 Convex Hexagons

In this section, the notation ⬡ k \varhexagon_{k} is used for a convex hexagon containing exactly k k points of the set 𝒳 \mathcal{X} in its interior. The study of the properties of such configurations was conducted using Answer Set Programming (ASP) methods.

###### Proof of Theorem 1.

To establish the equalities h ⁡ ( 6, 2) = 17 h(6,2)=17 and h ⁡ ( 6, 1) = 18 h(6,1)=18, we used the ASP model presented below. Technical optimization in this case consisted of checking the number of interior points not in the entire hexagon A ​ B ​ C ​ D ​ E ​ F ABCDEF, but only in one of its base triangles (for example, △ ​ A ​ C ​ E \triangle ACE). The running time of the program for parameters ( k = 2, n = 17) (k=2,n=17) and ( k = 1, n = 18) (k=1,n=18) was 70 and 190 minutes, respectively.

Listing 3: ASP code for verifying the values of h ⁡ ( 6, k) h(6,k)

[⬇][17]

pt (1.. n).

1{ l ( A, B, C, R): R =(-1;1)}1:- pt ( A), pt ( B), pt ( C), A < B, B < C.

% GEOMETRIC CONSTRAINTS

:- l ( A, B, C, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( A, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( B, C, D, R).

:- l ( A, B, D, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l (1, B, C,-1), sb!= off.

% DEFINITION OF INTERIOR POINTS

i ( A, B, C, X):- l ( A, X, B, R), l ( A, X, C,- R), B < C.

i ( A, B, C, X):- l ( B, X, C, R), l ( A, X, C,- R), A < B.

tr ( A, B, C):- pt ( A), pt ( B), pt ( C), A < B, B < C, { i ( A, B, C, X)}<= k.

:- l ( A, B, C, R), l ( B, C, D, R), l ( C, D, E, R), l ( D, E, F, R), A < B, B < C, C < D, D < E, E < F, tr ( A, C, E).

:- l ( A, B, C, R), l ( B, C, D, R), l ( C, D, F, R), l ( A, E, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( B, D, E).

:- l ( A, B, C, R), l ( B, C, E, R), l ( C, E, F, R), l ( A, D, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( B, D, E).

:- l ( A, B, D, R), l ( B, D, E, R), l ( D, E, F, R), l ( A, C, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( B, C, E).

:- l ( A, C, D, R), l ( C, D, E, R), l ( D, E, F, R), l ( A, B, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( B, C, E).

:- l ( A, B, C, R), l ( B, C, F, R), l ( A, D, E,- R), l ( D, E, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( A, C, E).

:- l ( A, B, D, R), l ( B, D, F, R), l ( A, C, E,- R), l ( C, E, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( A, D, E).

:- l ( A, C, D, R), l ( C, D, F, R), l ( A, B, E,- R), l ( B, E, F,- R), A < B, B < C, C < D, D < E, E < F, tr ( A, D, E).

#show l /4.

Listing 4: Verification logs in clingo

[⬇][18]

clingo ES_hexagons. lp -- configuration = frumpy -- sat - p =3 - c k =2 - c n =16

SATISFIABLE

clingo ES_hexagons. lp -- configuration = frumpy -- sat - p =3 - c k =2 - c n =17

UNSATISFIABLE

clingo ES_hexagons. lp -- configuration = frumpy -- sat - p =3 - c k =1 - c n =17

SATISFIABLE

clingo ES_hexagons. lp -- configuration = frumpy -- sat - p =3 - c k =1 - c n =18

UNSATISFIABLE

Using the linear subreduction method (with x i = i x_{i}=i), we successfully constructed an example of 17 points containing neither ⬡ 0 \varhexagon_{0} nor ⬡ 1 \varhexagon_{1} in just a few minutes. A similar example was provided in [36], but its manual search at that time took several weeks. The coordinates of the found configuration:

(0, − - 114449), (1, − - 193125), (2, − - 98112), (3, − - 90290), (4, − - 102071), (5, − - 496), (6, − - 769), (7,115376), (8,96152), (9, − - 8702), (10,662056), (11,347088), (12,32056), (13,0), (14,0), (15,8206), (16,192)

∎

Note that from the proven equality h ⁡ ( 6, 2) = 17 h(6,2)=17, the values h ⁡ ( 6, k) = 17 h(6,k)=17 follow immediately for all k > 2 k>2, since the condition of having exactly k k points inside a hexagon for k ⩽ 2 k\leqslant 2 is a more rigid constraint for a set of 17 points.

Since h ⁡ ( 6, 2) = 17 h(6,2)=17, any set of 17 points in the plane must contain at least one hexagon ⬡ k \varhexagon_{k} for k ∈ { 0, 1, 2 } k\in\{0,1,2\}. We studied the question of the existence of configurations of 17 points containing a unique convex hexagon of a specific type:

- •

For the case ⬡ 0 \varhexagon_{0}, the answer is positive; an example is easily constructed based on the classical configuration for g ⁡ ( 6) = 17 g(6)=17: (0,0), (9,1), (20,2), (30,2), (41,1), (50,0), (60,48), (65,49), (70,48), (80,52), (85,51), (90,52), (0,99), (9,98), (20,97), (30,97), (41,98)

- •

For the case ⬡ 1 \varhexagon_{1}, the answer is also positive. The configuration was found by us using the proposed method: (0, − - 6091), (1, − - 1), (2,0), (3, − - 4504), (4,315), (5,109787), (6, − - 1771), (7,73098), (8, − - 2), (9,48726), (10,44), (11, − - 276), (12,22), (13, − - 13), (14,1881), (15,2339), (16, − - 18).

- •

For the case ⬡ 2 \varhexagon_{2}, the answer is negative, which strictly follows from the structural results provided below.

Below are the coordinates of configurations containing only the specified types of hexagons:

{ ⬡ 1, ⬡ 2 } \{\varhexagon_{1},\varhexagon_{2}\} — 18 points: (0,1905), (1,1419), (2,937), (3, − - 13196), (4, − - 12255), (5, − - 1422), (6, − - 1383), (7, − - 1341), (8, − - 38634), (9,0), (10, − - 6802), (11, − - 3412), (12, − - 78970), (13, − - 4077), (14, − - 99211), (15, − - 1268), (16, − - 971), (17,0).

{ ⬡ 1, ⬡ 2, ⬡ 3 } \{\varhexagon_{1},\varhexagon_{2},\varhexagon_{3}\} — 19 points: (172, − - 83), (170,112), (82, − - 123), (36, − - 42), ( − - 191,29), (250, − - 294), (135, − - 69), (249,160), (15, − - 58), (89, − - 115), (102,9), (209, − - 208), ( − - 260,32), (135,20), (239,153), (114,117), (296,204), ( − - 110,32), (35, − - 41).

{ ⬡ 1, ⬡ 2, ⬡ 3, ⬡ 4 } \{\varhexagon_{1},\varhexagon_{2},\varhexagon_{3},\varhexagon_{4}\} — 20 points: (140,33), ( − - 194,95), ( − - 29, − - 30), (209, − - 218), (106,115), (31,28), (79,166), (204,228), (140,56), (201,191), ( − - 250,100), (165,12), (229,266), ( − - 167,88), (124,69), (232, − - 273), (154, − - 139), (94,137), (194,188), (186,186).

### 9.1 The Fourth Erdős–Szekeres-type Problem

The Fourth Erdős–Szekeres-type Problem. For integers n ⩾ 3 n\geqslant 3 and q ⩾ 2 q\geqslant 2, find the smallest positive integer h m ​ o ​ d ​ ( n, q) h_{mod}(n,q) such that any set of points 𝒳 {\cal X} in the plane in general position with cardinality | 𝒳 | ⩾ h m ​ o ​ d ​ ( n, q) |{\cal X}|\geqslant h_{mod}(n,q) contains the vertices of a convex n n -gon C C for which | ( C ∖ ∂ C) ∩ 𝒳 | ≡ 0 ( mod q) |(C\setminus\partial C)\cap{\cal X}|\equiv 0\pmod{q}.

The Bialostocki–Dierker–Voxman conjecture [54] states that the value h m ​ o ​ d ​ ( n, q) h_{mod}(n,q) exists for all n ⩾ 3, q ⩾ 2 n\geqslant 3,q\geqslant 2. The authors proved it for the case n ⩾ q + 2 n\geqslant q+2, establishing an upper bound via Ramsey numbers:

 | h m ​ o ​ d ​ ( n, q) ⩽ g ⁡ ( R 3 ​ ( n ′, n ′, …, n ′)), h_{mod}(n,q)\leqslant g(R_{3}(n^{\prime},n^{\prime},\dots,n^{\prime})), |  | (23) |

where n ′ ⩾ n n^{\prime}\geqslant n and n ′ ≡ 2 ( mod q) n^{\prime}\equiv 2\pmod{q}.

The bound obtained by Caro [55] for points with weights from an Abelian group, applied to this problem, also exhibits a tower of exponents character due to its dependence on the Ramsey numbers R 2 R_{2}:

 | h m ​ o ​ d ​ ( n, q) ⩽ g ⁡ ( ( R 2 ​ ( 3 ​ q − 3, …, 3 ​ q − 3) + 1) ​ ( ⌊ n q ⌋ + 1) ​ q). h_{mod}(n,q)\leqslant g\left(\left(R_{2}(3q-3,\dots,3q-3)+1\right)\left(\left\lfloor\frac{n}{q}\right\rfloor+1\right)q\right). |  | (24) |

Further research aimed to refine these estimates and relax the condition n ⩾ q + 2 n\geqslant q+2. Károlyi, Pach, and Tóth [56] showed the existence of h m ​ o ​ d ​ ( n, q) h_{mod}(n,q) for n ⩾ 5 ​ q / 6 + O ⁡ ( 1) n\geqslant 5q/6+O(1), although this result did not improve the exponential nature of the bounds.

In 2011, one of the authors [57] improved the technique of Bialostocki, Dierker, and Voxman:

###### Theorem 7.

If n ⩾ q + 2 n\geqslant q+2, then for even and odd q q, respectively:

 | h m ​ o ​ d ​ ( n, q) ⩽ R 3 ​ ( n, n, …, n), h m ​ o ​ d ​ ( n, q) ⩽ R 3 ​ ( g ⁡ ( n), n, …, n). h_{mod}(n,q)\leqslant R_{3}(n,n,\dots,n),\quad h_{mod}(n,q)\leqslant R_{3}(g(n),n,\dots,n). |  |

The main result of [57] was the complete elimination of the dependence on Ramsey numbers under a slightly stronger constraint on n n:

###### Theorem 8.

If n ⩾ 2 ​ q − 1 n\geqslant 2q-1, then h m ​ o ​ d ​ ( n, q) ⩽ g ⁡ ( q ⁡ ( n − 4) + 4) h_{mod}(n,q)\leqslant g(q(n-4)+4).

Since g ⁡ ( q ⁡ ( n − 4) + 4) ⩽ 2 q ​ n + O ⁡ ( 1) g(q(n-4)+4)\leqslant 2^{qn+O(1)}, this theorem is significantly more efficient than all previous results, as it removes the multiple exponents from the final expression.

#### 9.1.1 New Results

To prove stronger statements and optimize logical programs (by transitioning from counting points in hexagons to analyzing their constituent quadrilaterals), we formulate two auxiliary problems:

1. 1.

h e ​ x ​ ( n, Q) h_{ex}(n,Q) — the minimum number of points guaranteeing the existence of a convex n n -gon whose number of interior points belongs to the set Q ⊂ ℕ Q\subset\mathbb{N} ( 0 ∈ Q 0\in Q).

2. 2.

h s ​ u ​ b ​ ( 6, q) h_{sub}(6,q) — the minimum number of points guaranteeing the existence of a convex hexagon in which at least one of the three quadrilaterals, obtained by removing a pair of opposite vertices, contains exactly 0 0 or q q interior points.

For signotopes, the corresponding functions are denoted as h ~ m ​ o ​ d ​ ( n, q), h ~ e ​ x ​ ( n, Q), h ~ s ​ u ​ b ​ ( 6, q) \tilde{h}_{mod}(n,q),\tilde{h}_{ex}(n,Q),\tilde{h}_{sub}(6,q). The following chains of inequalities are obvious:

 | h m ​ o ​ d ​ ( 6, q) ⩽ h e ​ x ​ ( 6, { 0, q }) ⩽ h s ​ u ​ b ​ ( 6, q) ⩽ h ⁡ ( 6) = 30; \displaystyle h_{mod}(6,q)\leqslant h_{ex}(6,\{0,q\})\leqslant h_{sub}(6,q)\leqslant h(6)=30; |  |

 | h ~ m ​ o ​ d ​ ( 6, q) ⩽ h ~ e ​ x ​ ( 6, { 0, q }) ⩽ h ~ s ​ u ​ b ​ ( 6, q) ⩽ h ~ ​ ( 6) = 30. \displaystyle\tilde{h}_{mod}(6,q)\leqslant\tilde{h}_{ex}(6,\{0,q\})\leqslant\tilde{h}_{sub}(6,q)\leqslant\tilde{h}(6)=30. |  |

###### Theorem 9.

h s ​ u ​ b ​ ( 6, 2) = h ~ s ​ u ​ b ​ ( 6, 2) = 18, h s ​ u ​ b ​ ( 6, 3) = h ~ s ​ u ​ b ​ ( 6, 3) = 20, h s ​ u ​ b ​ ( 6, 4) = h ~ s ​ u ​ b ​ ( 6, 4) = 21 h_{sub}(6,2)=\tilde{h}_{sub}(6,2)=18,\quad h_{sub}(6,3)=\tilde{h}_{sub}(6,3)=20,\quad h_{sub}(6,4)=\tilde{h}_{sub}(6,4)=21.

###### Proof.

The logical program for verifying the values of h ~ s ​ u ​ b ​ ( 6, q) \tilde{h}_{sub}(6,q) and the logs of the runs with the status UNSATISFIABLE are available in the project repository 7 7 7 [https://github.com/koshelevv/Erdos-Szekeres/tree/main/hexagons/original_sub4][19]. The total computation time (in CPU Hours) was:

[⬇][20]

hexagons. sub4. q2.18. log: CPU Time: 16.70 h

hexagons. sub4. q3.20. log: CPU Time: 313.95 h

hexagons. sub4. q4.21. log: CPU Time: 5135.51 h

Based on the analysis of the previously constructed example of 17 points with a unique hexagon of type ⬡ 1 \varhexagon_{1}, the equality h m ​ o ​ d ​ ( 6, 2) = h e ​ x ​ ( 6, { 0, 2 }) = h s ​ u ​ b ​ ( 6, 2) = 18 h_{mod}(6,2)=h_{ex}(6,\{0,2\})=h_{sub}(6,2)=18 is established.

To confirm that h s ​ u ​ b ​ ( 6, 3) = 20 h_{sub}(6,3)=20 and h s ​ u ​ b ​ ( 6, 4) = 21 h_{sub}(6,4)=21, the linear subreduction method was applied on an exponential abscissa grid. The coordinates of geometric realizations for the corresponding extremal configurations were found:

19 points ( q = 3 q=3): ( − - 65536, − - 6779576), ( − - 16384, − - 1705174), ( − - 4096, − - 426607), ( − - 1024, − - 306602), ( − - 256, − - 29548), ( − - 64, 18492168), ( − - 16, 564027), ( − - 4, 565381), ( − - 1, 566107), (0, − - 301884), (1, − - 2975), (4, − - 1), (16, − - 1421), (64, 3569), (256, − - 256602), (1024, − - 120759), (4096, 422606), (16384, 0), (65536, 7);

20 points ( q = 4 q=4): ( − - 262144, − - 110327839), ( − - 65536, 131072), ( − - 16384, 47544316), ( − - 4096, 39608554), ( − - 1024, 36175252), ( − - 256, 63101785), ( − - 64, 36914751), ( − - 16, 36929496), ( − - 4, 35620882), ( − - 1, 36952837), (1, 72112362), (4, 94007251), (16, 21270346), (64, 36989358), (256, 37133021), (1024, 36301986), (4096, 34612949), (16384, 26548716), (65536, 0), (262144, − - 110761442). ∎

Using the ASP solver, abstract signotopes on 19 elements were found containing the subset of types { ⬡ 1, ⬡ 2, ⬡ 4 } \{\varhexagon_{1},\varhexagon_{2},\varhexagon_{4}\}, and on 20 elements, containing { ⬡ 1, ⬡ 2, ⬡ 3, ⬡ 5 } \{\varhexagon_{1},\varhexagon_{2},\varhexagon_{3},\varhexagon_{5}\}. These examples allow establishing the following exact values of the combinatorial functions:

 | h ~ m ​ o ​ d ​ ( 6, 3) = h ~ e ​ x ​ ( 6, { 0, 3 }) = h ~ s ​ u ​ b ​ ( 6, 3) = 20, \displaystyle\tilde{h}_{mod}(6,3)=\tilde{h}_{ex}(6,\{0,3\})=\tilde{h}_{sub}(6,3)=20, |  |

 | h ~ m ​ o ​ d ​ ( 6, 4) = h ~ e ​ x ​ ( 6, { 0, 4 }) = h ~ s ​ u ​ b ​ ( 6, 4) = 21. \displaystyle\tilde{h}_{mod}(6,4)=\tilde{h}_{ex}(6,\{0,4\})=\tilde{h}_{sub}(6,4)=21. |  |

Since during the computational experiment (totaling more than 12 months of CPU time), the linear subreduction method failed to construct geometric realizations for signotopes excluding both { ⬡ 0, ⬡ 3 } \{\varhexagon_{0},\varhexagon_{3}\} at N = 19 N=19 and { ⬡ 0, ⬡ 4 } \{\varhexagon_{0},\varhexagon_{4}\} at N = 20 N=20, only interval estimates are currently valid for the plane:

 | 19 ⩽ h m ​ o ​ d ​ ( 6, 3) ⩽ 20, 20 ⩽ h m ​ o ​ d ​ ( 6, 4) ⩽ 21. 19\leqslant h_{mod}(6,3)\leqslant 20,\quad 20\leqslant h_{mod}(6,4)\leqslant 21. |  |

###### Theorem 10.

The following values hold for the existence functions of convex hexagons with a given set of interior points:

 | h ~ e ​ x ​ ( 6, { 0, 1, 2 }) = h ~ e ​ x ​ ( 6, { 0, 1, 3 }) = h ~ e ​ x ​ ( 6, { 0, 1, 4 }) = g ⁡ ( 6) = 17; \displaystyle\tilde{h}_{ex}(6,\{0,1,2\})=\tilde{h}_{ex}(6,\{0,1,3\})=\tilde{h}_{ex}(6,\{0,1,4\})=g(6)=17; |  |

 | h e ​ x ​ ( 6, { 0, 3, 4 }) = h ~ e ​ x ​ ( 6, { 0, 3, 4 }) = 19, h e ​ x ​ ( 6, { 0, 4, 5 }) = h ~ e ​ x ​ ( 6, { 0, 4, 5 }) = 20. \displaystyle h_{ex}(6,\{0,3,4\})=\tilde{h}_{ex}(6,\{0,3,4\})=19,\quad h_{ex}(6,\{0,4,5\})=\tilde{h}_{ex}(6,\{0,4,5\})=20. |  |

###### Proof.

The logical program for verifying h ~ e ​ x ​ ( 6, Q) \tilde{h}_{ex}(6,Q) and the corresponding logs ( UNSATISFIABLE) are presented in the project repository 8 8 8 [https://github.com/koshelevv/Erdos-Szekeres/tree/main/hexagons/original_ex][21]:

[⬇][22]

hexagons. Q_012.17 pt. log: CPU Time: 4.13 h

hexagons. Q_013.17 pt. log: CPU Time: 6.07 h

hexagons. Q_014.17 pt. log: CPU Time: 10.86 h

hexagons. Q_034.19 pt. log: CPU Time: 188.42 h

hexagons. Q_045.20 pt. log: CPU Time: 2227.30 h

∎

An analysis of the signotope space and the found realizations allows us to formulate a structural theorem describing the mandatory presence of certain types of hexagons depending on the cardinality of the set 𝒳 \mathcal{X}.

###### Theorem 11 (on the structure of small configurations).

Let 𝒳 \mathcal{X} be a set of points in the plane in general position. Then the following statements hold:

1. 1.

If | 𝒳 | = 17 |\mathcal{X}|=17, then 𝒳 \mathcal{X} contains either ⬡ 0 \varhexagon_{0}, or ⬡ 1 \varhexagon_{1}, or simultaneously { ⬡ 2, ⬡ 3, ⬡ 4 } \{\varhexagon_{2},\varhexagon_{3},\varhexagon_{4}\}.

2. 2.

If | 𝒳 | = 18 |\mathcal{X}|=18, then 𝒳 \mathcal{X} contains either ⬡ 0 \varhexagon_{0}, or simultaneously { ⬡ 1, ⬡ 2 } \{\varhexagon_{1},\varhexagon_{2}\}.

3. 3.

If | 𝒳 | = 19 |\mathcal{X}|=19, then 𝒳 \mathcal{X} contains either ⬡ 0 \varhexagon_{0}, or simultaneously { ⬡ 1, ⬡ 2 } \{\varhexagon_{1},\varhexagon_{2}\} and at least one hexagon from { ⬡ 3, ⬡ 4 } \{\varhexagon_{3},\varhexagon_{4}\}.

4. 4.

If | 𝒳 | = 20 |\mathcal{X}|=20, then 𝒳 \mathcal{X} contains either ⬡ 0 \varhexagon_{0}, or simultaneously { ⬡ 1, ⬡ 2, ⬡ 3 } \{\varhexagon_{1},\varhexagon_{2},\varhexagon_{3}\} and at least one hexagon from { ⬡ 4, ⬡ 5 } \{\varhexagon_{4},\varhexagon_{5}\}.

5. 5.

If | 𝒳 | = 21 |\mathcal{X}|=21, then 𝒳 \mathcal{X} contains either ⬡ 0 \varhexagon_{0}, or simultaneously { ⬡ 1, ⬡ 2, ⬡ 3, ⬡ 4 } \{\varhexagon_{1},\varhexagon_{2},\varhexagon_{3},\varhexagon_{4}\}.

Corollary. There is no set of 17 points in general position containing ⬡ 2 \varhexagon_{2} as the unique convex hexagon.

Note. The formulated theorems are strictly proven for abstract signotopes. The fact that, during an extensive computational experiment, we failed to find a geometric realization of anomalous signotopes (for example, those containing ⬡ 4 \varhexagon_{4} in the absence of ⬡ 0 \varhexagon_{0} and ⬡ 3 \varhexagon_{3} for N = 19 N=19) indicates that stronger statements may hold for point sets in the plane. In particular, we conjecture the mandatory presence of either ⬡ 0 \varhexagon_{0} or ⬡ 3 \varhexagon_{3} as early as N = 19 N=19. Investigating this gap between the combinatorial structure of abstract and realizable configurations remains an open problem.

#### 9.1.2 Symmetric Configurations and Lower Bounds for h m ​ o ​ d ​ ( 6, q) h_{mod}(6,q)

In concluding this section, let us consider symmetric point sets. We have established that any set of N ⩾ 18 N\geqslant 18 points possessing axial symmetry is guaranteed to contain a convex empty hexagon ⬡ 0 \varhexagon_{0}. The low value of this upper bound makes axially symmetric configurations ineffective when searching for extremal examples for the function h m ​ o ​ d ​ ( 6, q) h_{mod}(6,q).

To verify this fact, we use our logical program for h ⁡ ( 6, k) h(6,k), adding a single line that restricts the search space to only axially symmetric signotopes:

[⬇][23]

for n in 17 18 19; do

( cat ES_hexagons. lp; echo ':- l(A,B,C,R), l(n+1-C,n+1-B,n+1-A,-R).') | clingo - c k =0 - c n = $n - c sb = off;

done

SATISFIABLE

UNSATISFIABLE

UNSATISFIABLE

To construct examples with a larger number of points, more flexible structures were used, particularly configurations with k k -fold symmetry. Using the local stochastic search method, symmetric sets for large N N were found containing exclusively hexagons of types { ⬡ 1, …, ⬡ q − 1 } \{\varhexagon_{1},\dots,\varhexagon_{q-1}\}. The corresponding coordinates and visualizations are available in the project repository 9 9 9 [https://github.com/koshelevv/Erdos-Szekeres/tree/main/hexagons][24]. These examples allow us to establish lower bounds for the function h m ​ o ​ d ​ ( 6, q) h_{mod}(6,q), presented in the table below. For these examples, we do not guarantee that N N is the maximum possible for a fixed q q.

{ ⬡ 1, …, ⬡ 6 } \{\varhexagon_{1},\dots,\varhexagon_{6}\} — 21 points: ( − - 76, − - 26) (15,78) (60, − - 52) ( − - 22,229) (209, − - 95) ( − - 187, − - 133) ( − - 26,218) (201, − - 86) ( − - 175, − - 131) ( − - 35,182) (175, − - 60) ( − - 140, − - 121) ( − - 209, − - 217) ( − - 83,289) (292, − - 72) ( − - 300, − - 249) ( − - 65,384) (365, − - 135) ( − - 174, − - 127) ( − - 22,214) (196, − - 87).

{ ⬡ 1, …, ⬡ 7 } \{\varhexagon_{1},\dots,\varhexagon_{7}\} — 22 points: (0,0) ( − - 2, − - 117) ( − - 100,60) (102,56) (4, − - 169) ( − - 148,81) (144,87) (17, − - 78) ( − - 76,24) (59,53) ( − - 107,40) (88,72) (18, − - 112) ( − - 252, − - 223) ( − - 67,329) (319, − - 106) ( − - 273, − - 241) ( − - 72,356) (345, − - 115) (1, − - 83) ( − - 72,40) (71,42).

q q | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |

h m ​ o ​ d ​ ( 6, q) ⩾ h_{mod}(6,q)\geqslant | 18 | 19 | 20 | 21 | 21 | 22 | 23 | 23 | 23 | 23 | 23 | 23 | 26 | 26 | 26 | 26 | 30 |

Table 3: Lower bounds for the fourth Erdős–Szekeres type problem ( n = 6 n=6).

It should be noted that the value of 26 for 14 ⩽ q ⩽ 17 14\leqslant q\leqslant 17 is due to the example we found of 25 points with 3-fold symmetry for the problem h n ​ c ​ ( 4, 0, 3, 0) h_{nc}(4,0;3,0), containing only types { ⬡ 1, …, ⬡ 13 } \{\varhexagon_{1},\dots,\varhexagon_{13}\}. For q ⩾ 18 q\geqslant 18, the estimates coincide with the classical value h ⁡ ( 6) = 30 h(6)=30, as the well-known Overmars configuration of 29 points [23] contains only hexagons of types { ⬡ 1, …, ⬡ 17 } \{\varhexagon_{1},\dots,\varhexagon_{17}\}.

## 10 Geometric Ramsey Numbers

Research in this area was initiated by Bárány and Károlyi [58], who formulated the following fundamental problem:

Is it true that for any integer c c, there exists a minimum positive integer N N such that for any set of N N points in the plane in general position and an arbitrary c c -coloring of the edges of the complete graph with vertices at these points, there necessarily exists a monochromatic empty triangle?

Batista-Santiago et al. in [59] gave a comprehensive negative answer for the case c ⩾ 3 c\geqslant 3, proving that the sought number R E ​ C ​ ( 3, 3, 3) R_{EC}(3,3,3) (and above) does not exist. For two colors ( c = 2 c=2), they established the interval 17 ⩽ R E ​ C ​ ( 3, 3) ⩽ h ⁡ ( 6) = 30 17\leqslant R_{EC}(3,3)\leqslant h(6)=30. They also proposed a generalization of the problem for polygons of arbitrary size: finding the minimum number R E ​ C ​ ( s, t) R_{EC}(s,t) guaranteeing, in any two-color edge coloring, the existence of an empty convex s s -gon of the first color or an empty convex t t -gon of the second color. The authors obtained the lower bound 57 ⩽ R E ​ C ​ ( 4, 4) 57\leqslant R_{EC}(4,4).

In the present study, we introduce additional values for further classification of conditions: R C ​ ( s, t) R_{C}(s,t) (where the emptiness condition is not mandatory), as well as R E ​ N ​ C ​ ( s, t) R_{ENC}(s,t) and R N ​ C ​ ( s, t) R_{NC}(s,t) (where the convexity condition is not mandatory). From the definitions, the following relations follow directly:

 | R E ​ C ​ ( 2, t) = h ⁡ ( t), R C ​ ( 2, t) = g ⁡ ( t), R E ​ N ​ C ​ ( 2, t) = R N ​ C ​ ( 2, t) = t, R C ​ ( 3, 3) = R N ​ C ​ ( 3, 3) = 6. R_{EC}(2,t)=h(t),\quad R_{C}(2,t)=g(t),\quad R_{ENC}(2,t)=R_{NC}(2,t)=t,\quad R_{C}(3,3)=R_{NC}(3,3)=6. |  | (25) |

Calculating the value of R N ​ C ​ ( s, t) R_{NC}(s,t) is equivalent to the problem in ordered graph theory of searching for monochromatic cycles without self-intersections. The exact value R N ​ C ​ ( s, t) = 2 ​ s ​ t − 3 ​ s − 3 ​ t + 6 R_{NC}(s,t)=2st-3s-3t+6 was established in [60] (upper bound) and [61] (lower bound). We have noticed that the argumentation from [60] allows extending this result to broader structures — kipas graphs — while maintaining the original formula.

Using the linear subreduction method, we obtained new lower bounds for the case of monochromatic convex polygons without the additional emptiness condition: R C ​ ( 3, 4) ⩾ 11 R_{C}(3,4)\geqslant 11, R C ​ ( 4, 4) ⩾ 23 R_{C}(4,4)\geqslant 23, and R C ​ ( 3, 5) ⩾ 25 R_{C}(3,5)\geqslant 25. The corresponding point configurations are presented below:

Example for R C ​ ( 3, 4) R_{C}(3,4) (10 points):
(0,0) (1,0) (2, − 211 -211) (3, − 421 -421) (4, − 671 -671) (5, − 839 -839) (6, − 1044 -1044) (7, − 1248 -1248) (8, − 1458 -1458) (9, − 1655 -1655)

Example for R C ​ ( 4, 4) R_{C}(4,4) (22 points):

(0,605219576) (1,547491917) (2, − 38432236 -38432236) (3, − 37864720 -37864720) (4, − 8094 -8094) (5,327037131) (6, − 22919212 -22919212) (7, − 19069521 -19069521) (8, − 35026470 -35026470) (9, − 43780784 -43780784) (10, − 7497592 -7497592) (11, − 3645043 -3645043) (12,218931) (13,0) (14, − 3332 -3332) (15,13464851) (16,17507537) (17, − 4512052 -4512052) (18,23345651) (19, − 15231 -15231) (20, − 1528709 -1528709) (21,0)

Example for R C ​ ( 3, 5) R_{C}(3,5) (24 points):

(0, − 184 -184) (1, − 5 -5) (2,71) (3,19085) (4,45983) (5,588939) (6,0) (7, − 176 -176) (8,153581) (9,8474) (10,7536) (11, − 281760 -281760) (12,5655) (13,4707) (14, − 717104 -717104) (15,3346) (16,2669) (17,1995) (18,1325) (19, − 774 -774) (20, − 12 -12) (21, − 2886 -2886) (22,12) (23,22)

Calculating signotopic upper bounds for these problems is an extremely labor-intensive process. During the computational experiment using the clingo system, we were only able to verify the value R C ​ ( 3, 4) = 11 R_{C}(3,4)=11. Regarding the other two values, no solution was obtained even after 12 months of continuous solver operation, which leads us to put forward the following hypothesis: R C ​ ( 4, 4) = 24 R_{C}(4,4)=24, 23 ⩽ R C ​ ( 3, 5) ⩽ 25 23\leqslant R_{C}(3,5)\leqslant 25.

The central result of this section is the following theorem.

###### Theorem 12.

R E ​ C ​ ( 3, 3) = 21 R_{EC}(3,3)=21.

###### Proof.

To prove the upper bound, the following logical program was used:

[⬇][25]

pt (1.. n).

ins ( tr, t1, tr1; tr, t2, tr2; tr, t3, tr3).

1{ c ( A, B, Z): ins ( _, Z, I), I =0..99}1:- pt ( A), pt ( B), A < B.

1{ l ( A, B, C, R): R =(-1;1)}1:- pt ( A), pt ( B), pt ( C), A < B, B < C.

% GEOMETRIC CONSTRAINTS

:- l ( A, B, C, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( A, C, D, R).

:- l ( A, B, C, R), l ( A, B, D,- R), l ( B, C, D, R).

:- l ( A, B, D, R), l ( A, C, D,- R), l ( B, C, D, R).

:- l (1, B, C,-1), sb!= off.

% DEFINITION OF INTERIOR POINTS

i ( A, B, C, X):- l ( A, X, B, R), l ( A, X, C,- R), B < C.

i ( A, B, C, X):- l ( B, X, C, R), l ( A, X, C,- R), A < B.

tr ( A, B, C, I):- pt ( A), pt ( B), pt ( C), A < B, B < C, { i ( A, B, C, X)}<= I, ins ( _, _, I), I =0..99.

:- ins ( tr, Z, I), A < B, B < C, c ( A, B, Z), c ( A, C, Z), c ( B, C, Z), tr ( A, B, C, I).

#show l /4.

#show c /3.

[⬇][26]

clingo ES_Ramsey. lp -- configuration = frumpy -- sat - p =3 - c tr1 =0 - c tr2 =0 - c n =21

UNSATISFIABLE

CPU Time: 1356782.996 s

We found a configuration of 20 points exhibiting 5-fold symmetry. For this set, there exists a symmetric edge coloring that does not contain monochromatic empty triangles. Below are the obtained integer coordinates 10 10 10 the edge coloring is available on [https://github.com/koshelevv/Erdos-Szekeres/tree/main/geometric_Ramsey_numbers][27]:

( − - 1583, − - 2563) (1948, − - 2298) (2787,1143) ( − - 226,3004) ( − - 2927,714)

( − - 787, − - 966) (676, − - 1047) (1204,319) (69,1244) ( − - 1162,450)

( − - 661,731) ( − - 899, − - 403) (105, − - 980) (964, − - 203) (491,855)

( − - 381,110) ( − - 222, − - 328) (244, − - 313) (373,135) ( − - 13,396).

∎

Further development of the problem involves relaxing the emptiness condition for monochromatic triangles. Let R E ​ C ​ ( 3, k 1, 3, k 2) R_{EC}(3,k_{1};3,k_{2}) be the minimum number of points guaranteeing the presence of either a first-color triangle with at most k 1 k_{1} interior points or a second-color triangle with at most k 2 k_{2} interior points. The case k = 0 k=0 corresponds to the classical emptiness condition, while k = ∞ k=\infty completely removes the restriction on the number of interior points.

We have established the following exact values for these quantities:

- •

R E ​ C ​ ( 3, 0, 3, 1) = R E ​ C ​ ( 3, 0, 3, ∞) = 17 R_{EC}(3,0;3,1)=R_{EC}(3,0;3,\infty)=17;

- •

R E ​ C ​ ( 3, 1, 3, 1) = 8 R_{EC}(3,1;3,1)=8;

- •

R E ​ C ​ ( 3, 1, 3, 2) = R E ​ C ​ ( 3, 1, 3, ∞) = 7 R_{EC}(3,1;3,2)=R_{EC}(3,1;3,\infty)=7;

- •

R E ​ C ​ ( 3, 2, 3, 2) = R ⁡ ( 3, 3) = 6 R_{EC}(3,2;3,2)=R(3,3)=6.

It should be noted that the value R E ​ C ​ ( 3, 2, 3, 2) = 6 R_{EC}(3,2;3,2)=6 expectedly coincides with the classical Ramsey number R ⁡ ( 3, 3) R(3,3). It is known that in any two-color edge coloring of K 6 K_{6}, there are at least two monochromatic triangles. In this case, only one of them can contain the maximum possible 3 interior points, while the second is guaranteed to contain no more than two.

[⬇][28]

clingo - lpx ES_Ramsey. lp lpx -- configuration = frumpy -- sat - p =3 - c tr1 =0 - c tr2 =99 - c n =16

SATISFIABLE

y (1)=-2833/2 y (2)=-10409/8 y (3)=-4739/4 y (4)=1 y (5)=-954 y (6)=-43327/56 y (7)=-4818/7 y (8)=-4815/8

y (9)=-607 y (10)=8509/3 y (11)=59563/18 y (12)=2476273/648 y (13)=-801/4 y (14)=-1581/16 y (15)=0 y (16)=0

clingo - lpx ES_Ramsey. lp lpx -- configuration = frumpy -- sat - p =3 - c tr1 =1 - c tr2 =1 - c n =7

SATISFIABLE

y (1)=3/2 y (2)=1 y (3)=-1 y (4)=-13 y (5)=-6 y (6)=0 y (7)=0

clingo - lpx ES_Ramsey. lp lpx -- configuration = frumpy -- sat - p =3 - c tr1 =1 - c tr2 =99 - c n =6

SATISFIABLE

y (1)=5 y (2)=7/2 y (3)=-1 y (4)=3/2 y (5)=0 y (6)=0

clingo ES_Ramsey. lp -- configuration = frumpy -- sat - p =3 - c tr1 =0 - c tr2 =1 - c n =17

UNSATISFIABLE

clingo ES_Ramsey. lp -- configuration = frumpy -- sat - p =3 - c tr1 =1 - c tr2 =1 - c n =8

UNSATISFIABLE

clingo ES_Ramsey. lp -- configuration = frumpy -- sat - p =3 - c tr1 =1 - c tr2 =2 - c n =7

UNSATISFIABLE

## 11 Conclusion

In this paper, we have presented a comprehensive study of Erdős–Szekeres type problems using modern computational combinatorial analysis methods. The main result of the study is the establishment of several new exact values for the functions h, h n ​ c h,h_{nc}, and h i ​ s ​ l h_{isl} for bicolored and multicolored point sets. In particular, the equality h n ​ c ​ ( 4, 0, 4, 0) = 26 h_{nc}(4,0;4,0)=26 was proven for the first time.

Special attention was given to the convex hexagon problem. New exact values and coordinates were found for configurations with specific constraints on the number of interior points (functions h m ​ o ​ d h_{mod}, h e ​ x h_{ex}, and h s ​ u ​ b h_{sub}).

An important achievement in the field of geometric Ramsey numbers was the establishment of the exact value R E ​ C ​ ( 3, 3) = 21 R_{EC}(3,3)=21. The discovered configuration of 20 points with 5-fold symmetry and the verification of the upper bound using a SAT solver eliminate the previously existing gap within this range. Furthermore, we have obtained new lower bounds for Ramsey numbers without the emptiness condition: R C ​ ( 4, 4) ⩾ 23 R_{C}(4,4)\geqslant 23 and R C ​ ( 3, 5) ⩾ 25 R_{C}(3,5)\geqslant 25, expanding the understanding of the structure of extremal planar sets.

The theoretical analysis of the sets S k ​ ( N) S_{k}(N) allowed for the refinement of Dehnhardt’s hypotheses regarding universal extremal configurations. We established the coincidence of configuration sets minimizing the number of convex and empty 3- and 4-gons for N ⩽ 11 N\leqslant 11 and their divergence from analogous sets for 5-gons for N ⩾ 10 N\geqslant 10.

The methodological value of the work lies in the testing and comparison of different approaches to the logical encoding of geometric constraints. We have shown that the use of the ASP system clingo in combination with specialized heuristics (presets frumpy and crafty) allows for the effective verification of complex configurations in their entirety, minimizing the need for manual decomposition. The developed linear subreduction method using exponential abscissa grids proved its efficiency, enabling the discovery of geometric realizations for the vast majority of found maximal signotopes.

Despite the progress achieved, the question of the existence and exact values of h ⁡ ( 4, 0, 4, 0) h(4,0;4,0) and h i ​ s ​ l ​ ( 4, 0, 4, 0) h_{isl}(4,0;4,0) remains open. We see the further development of the proposed approach in the automation of decomposition processes and the integration of more powerful conflict-learning methods into SMT models, which could potentially overcome the current computational barriers for problems with N > 30 N>30 points.

## References

- [1] P. Erdős, G. Szekeres, A combinatorial problem in geometry, Compositio Math., 2 (1935), 463–470.
- [2] P. Erdős, G. Szekeres, On some extremum problems in elementary geometry, Ann. Univ. Sci. Budapest Eötvös Sect. Math., 3–4 (1961), 53–62.
- [3] P. Erdős, Some more problems in elementary geometry, Austral. Math. Soc. Gaz., 5 (1978), 52–54.
- [4] W. Morris, V. Soltan, The Erdős–Szekeres problem on points in convex position, Bulletin of the Amer. Math. Soc., 37 (2000), N4, 437–458.
- [5] F. P. Ramsey, On a problem of formal logic, Proc. London Math. Soc. Ser. 2, 30 (1930), 264–286.
- [6] R. L. Graham, B. L. Rothschild, J. H. Spencer, Ramsey Theory, 2nd ed., John Wiley & Sons, NY, 1990.
- [7] M. Hall, Jr., Combinatorial Theory, Blaisdell, Waltham, Mass. 1967; Mir, Moscow, 1970.
- [8] O. Devillers, F. Hurtado, G. Károlyi, C. Seara, Chromatic variants of the Erdős–Szekeres theorem, Comput. Geom., 26 (2003), 193–208.
- [9] G. Szekeres, L. Peters, Computer solution to the 17-point Erdős–Szekeres problem, ANZIAM J., 48 (2006), 151–164.
- [10] F. Marić, Fast formal proof of the Erdős–Szekeres conjecture for convex polygons with at most 6 points, J. Autom. Reason., 62 (2019), 301–329.
- [11] M. Scheucher, Points, Lines, and Circles. Some Contributions to Combinatorial Geometry, Ph.D. thesis, TU Berlin, 2020.
- [12] F. R. K. Chung, R. L. Graham, Forced convex n n -gons in the plane, Discrete Comput. Geom., 19(3) (1998), 367–371.
- [13] D. Kleitman, L. Pachter, Finding convex sets among points in the plane, Discrete Comput. Geom., 19(3) (1998), 405–410.
- [14] G. Tóth, P. Valtr, Note on the Erdős–Szekeres theorem, Discrete Comput. Geom., 19(3) (1998), 457–459.
- [15] G. Tóth, P. Valtr, The Erdős–Szekeres theorem: upper bounds and related results, Combinatorial and Computational Geometry, MSRI Publications, 52 (2005), 557–568.
- [16] G. Vlachos, On a conjecture of Erdős and Szekeres, arXiv:1505.07549 [math.CO], 2015.
- [17] H. N. Mojarrad, G. Vlachos, An improved upper bound for the Erdős–Szekeres theorem, arXiv:1510.06255 [math.CO], 2015.
- [18] S. Norin, Y. Yuditsky, Erdős–Szekeres without induction, Discrete Comput. Geom., 55 (2016), 963–971.
- [19] A. Suk, On the Erdős–Szekeres convex polygon problem, J. Amer. Math. Soc., 30(4) (2017), 1047–1053.
- [20] A. F. Holmsen, H. Mojarrad, J. Pach, G. Tardos, Two extensions of the Erdős–Szekeres theorem, J. Combin. Theory Ser. A, 170 (2020), 105132.
- [21] H. Harborth, Konvexe Fünfecke in ebenen Punktmengen, Elem. Math., 33 (1978), 116–118.
- [22] M. Overmars, B. Scholten, I. Vincent, Sets without empty convex 6-gons, Bull. EATCS, 7 (1989), 160–168.
- [23] M. Overmars, Finding sets of points without empty convex 6-gons, Discrete Comput. Geom., 29 (2003), 153–158.
- [24] C. Nicolas, The empty hexagon theorem, Discrete Comput. Geom., 38(2) (2007), 389–397.
- [25] T. Gerken, On empty convex hexagons in planar point sets, Discrete Comput. Geom., 39 (2008), 239–272.
- [26] P. Valtr, On the empty hexagons, Manuscript, 2006. URL: http://cuni.cz
- [27] V. A. Koshelev, The Erdős–Szekeres problem on empty hexagons in the plane, Modeling and Analysis of Information Systems, 16:2 (2009), 22–74 (in Russian).
- [28] M. J. H. Heule, M. Scheucher, Happy ending: An empty hexagon in every set of 30 points, arXiv:2403.00737 [math.CO], 2024.
- [29] A. Biere, K. Fazekas, M. Fleury, N. Heisinger, CaDiCaL, Kissat, Paracooba at the SAT Competition 2020, SAT Competition (2020), 51–53.
- [30] B. Subercaseaux, W. Nawrocki, J. Gallicchio, C. Codel, M. Carneiro, M. J. H. Heule, Formal Verification of the Empty Hexagon Number, arXiv:2403.17370 [cs.LO], 2024.
- [31] J. D. Horton, Sets with no empty 7-gons, Canad. Math. Bull., 26 (1983), 482–484.
- [32] Bl. Sendov, Compulsory configurations of points in the plane, Fundam. Appl. Math., 1:2 (1995), 491–516 (in Russian).
- [33] H. Nyklova, Almost empty polygons, Studia Sci. Math. Hungar., 40(3) (2003), 269–286.
- [34] V. A. Koshelev, Interior Points in the Erdős–Szekeres Theorems, Math. Notes, 91:4 (2012), 542–557.
- [35] V. A. Koshelev, Almost empty hexagons, J. Math. Sci., 164:1 (2010), 60–81.
- [36] V. A. Koshelev, Computer Solution of the Almost Empty Hexagon Problem, Math. Notes, 89:3 (2011), 455–458.
- [37] P. Brass, Empty monochromatic fourgons in two-colored point sets, Geombinatorics, 14(2) (2004), 5–7.
- [38] E. Friedman, 30 two-colored points with no empty monochromatic convex fourgons, Geombinatorics, 14(2) (2004), 53–54.
- [39] R. Van Gulik, 32 two-colored points with no empty monochromatic convex fourgons, Geombinatorics, 15(1) (2005), 32–33.
- [40] C. Huemer, C. Seara, 36 two-colored points with no empty monochromatic convex fourgons, Geombinatorics, 19(1) (2009), 5–6.
- [41] V. Koshelev, On Erdős–Szekeres problem and related problems, 2009, [https://arxiv.org/abs/0910.2700][29]
- [42] D. Basu, K. Basu, B. B. Bhattacharya, S. Das, Almost empty monochromatic triangles in planar point sets, Discrete Appl. Math., 210 (2016), 207–213.
- [43] J. Cravioto-Lagos, A. C. González-Martínez, T. Sakai, J. Urrutia, On almost empty monochromatic triangles and convex quadrilaterals in colored point sets, Graphs Combin., 35 (2019), 1475–1493.
- [44] O. Aichholzer, T. Hackl, C. Huemer, F. Hurtado, B. Vogtenhuber, Large bichromatic point sets admit empty monochromatic 4-gons, SIAM J. Discrete Math., 23(4):2147–2155, 2010.
- [45] L. Liu, Y. Zhang, Almost empty monochromatic quadrilaterals in planar point sets, Math. Notes, 103:3 (2018), 415–429.
- [46] L. de Moura, N. Bjørner, Z3: An efficient SMT solver, Proc. TACAS (2008), 337–340.
- [47] M. Gebser, R. Kaminski, B. Schaub, M. Ostrowski, Clingo = ASP + Control, Technical Report, Univ. Potsdam, 2024.
- [48] N. Eén, N. Sörensson, An extensible SAT-solver, Proc. SAT (2003), 502–518.
- [49] G. Audemard, L. Simon, Predicting learnt clauses quality in modern SAT solvers, Proc. IJCAI (2009), 399–404.
- [50] A. Biere, Kissat at the SAT Competition 2020, SAT Competition (2020), 54.
- [51] H. Dehnhardt, Leere konvexe Vielecke in ebenen Punktmengen, Ph.D. Thesis, TU Braunschweig, 1987.
- [52] O. Aichholzer, F. Aurenhammer, H. Krasser, On the dual span of the order types, Discrete Comput. Geom., 28 (2002), 467–484.
- [53] O. Aichholzer, The order type database, http://tugraz.at, 2013.
- [54] A. Bialostocki, P. Dierker, B. Voxman, Some notes on the Erdős–Szekeres theorem, Discrete Mathematics, Vol. 91, No. 3, pp. 231–238, 1991.
- [55] Y. Caro, On the generalized Erdős–Szekeres conjecture — a new upper bound, Discrete Mathematics, Vol. 160, No. 1-3, pp. 229–233, 1996.
- [56] G. Károlyi, J. Pach, G. Tóth. A modular version of the Erdős–Szekeres theorem, Studia Scientiarum Mathematicarum Hungarica, Vol. 38, pp. 245–259, 2001.
- [57] V. A. Koshelev, The Erdős–Szekeres Theorem and Congruences, Math. Notes, 87:4 (2010), 537–542.
- [58] I. Bárány, G. Károlyi, Problems and results around the Erdős–Szekeres theorem, Discrete and Computational Geometry, Japanese Conference (JCDCG 2000), Lecture Notes in Computer Science, Vol. 2098, pp. 199–205, 2001.
- [59] C. Bautista-Santiago, J. Cano, R. Fabila-Monroy, C. Hidalgo Toscano, C. Huemer, J. Leaños, T. Sakai, J. Urrutia, Ramsey numbers for empty convex polygons, EuroCG. Ljubljana, Slovenia, March 16–18, 2015.
- [60] Gy. Károlyi, J. Pach, G. Tóth, P. Valtr, Ramsey-type results for geometric graphs, II, Discrete Comput. Geom. 20(3) (1998), 375–388.
- [61] M. Balko, J. Cibulka, K. Král, J. Kynčl. Ramsey numbers of ordered graphs, Electron. J. Combin., 27:P1.16, 2020.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://www.eurogiga-compose.eu/posezo.php
[4]: https://page.math.tu-berlin.de/~scheuch/research/sat_vs_bicolored_point_sets/
[5]: data:text/plain;base64,Li9FU19jb2xvci5weSBuYzE9MCB0cjI9MCBuPTEzIHwga2lzc2F0ClNBVElTRklBQkxFCi4vRVNfY29sb3IucHkgbmMxPTAgdHIyPTAgbj0xNCB8IGtpc3NhdApVTlNBVElTRklBQkxF
[6]: data:text/plain;base64,Li9FU19jb2xvci5weSBuYzE9MCB0cjI9MCBuPTEzIHhncmlkPTEgfCB6MyAtaW4gfCBzZWQgJzphO047cy8pXG4gKC8pICgvZztiYScKc2F0CigoeDAgMCkgKHkwICgtIDI3OCkpIChrMSB0cnVlKSAoazE0IGZhbHNlKSkKKCh4MSAxKSAoeTEgKC0gMTcyKSkgKGsyIGZhbHNlKSAoazE1IHRydWUpKQouLi4KKCh4MTEgMTEpICh5MTEgMTg2KSAoazEyIGZhbHNlKSAoazI1IHRydWUpKQooKHgxMiAxMikgKHkxMiAyMDgpIChrMTMgdHJ1ZSkgKGsyNiBmYWxzZSkp
[7]: data:text/plain;base64,cHQoMC4ubi0xKS4KCiUgIC0tLSBTRUxFQ1QgVEFSR0VUIFBPTFlHT05TIC0tLQolICBGb3JtYXQ6IGlucyhUeXBlLCBDb2xvcklELCBNYXhJbnRlcmlvclBvaW50cykKaW5zKHByLHAxLHByMTsKICAgIHRyLHQxLHRyMTsgdHIsdDIsdHIyOyB0cix0Myx0cjM7IHRyLHQ0LHRyNDsgdHIsdDUsdHI1OwogICAgY3YsYzEsY3YxOyBjdixjMixjdjI7IGN2LGMzLGN2MzsKICAgIGN2LGkxLGlzMTsgY3YsaTIsaXMyOyBjdixpMyxpczM7CiAgICBpcyxpMSxpczErMTsgaXMsaTIsaXMyKzE7IGlzLGkzLGlzMysxOwogICAgKG5jO2N2KSxuMSxuYzE7IChuYztjdiksbjIsbmMyOyAobmM7Y3YpLG4zLG5jMykuCiNjb25zdCBpczE9LTIuICNjb25zdCBpczI9LTIuICNjb25zdCBpczM9LTIuCgolICAtLS0gR0VORVJBVE9SUyAtLS0KJSAgQXNzaWduIGV4YWN0bHkgb25lIGNvbG9yIHRvIGVhY2ggcG9pbnQKMXtjKEEsWik6IGlucyhfLFosSSksST0wLi45OX0xIDotIHB0KEEpLgojaGV1cmlzdGljIGMoQSxaKTogcHQoQSksIGlucyhfLFosSSksIEk9MC4uOTkuIFsxMCwgbGV2ZWxdCiUgIEFzc2lnbiBleGFjdGx5IG9uZSByb3RhdGlvbiB0byBlYWNoIHRyaXBsZXQgKENoaXJvdG9wZSBiYXNlKQoxe2woQSxCLEMsUik6IFI9KC0xOzEpfTEgOi0gcHQoQSkscHQoQikscHQoQyksIEE8QixCPEMuCgolICAtLS0gR0VPTUVUUklDIENPTlNUUkFJTlRTIChBeGlvbXMgZm9yIFNpZ25vdG9wZSkgLS0tCiUgIFRoZXNlIGVuc3VyZSB0aGF0IHRoZSByZWxhdGl2ZSBwb3NpdGlvbnMgb2YgcG9pbnRzIGFyZSBwaHlzaWNhbGx5IHBvc3NpYmxlCjotIGwoQSxCLEMsUiksIGwoQSxDLEQsLVIpLCBsKEIsQyxELFIpLgo6LSBsKEEsQixDLFIpLCBsKEEsQixELC1SKSwgbChBLEMsRCxSKS4KOi0gbChBLEIsQyxSKSwgbChBLEIsRCwtUiksIGwoQixDLEQsUikuCjotIGwoQSxCLEQsUiksIGwoQSxDLEQsLVIpLCBsKEIsQyxELFIpLgolICBTeW1tZXRyeSBicmVha2luZzogZml4IG9yaWVudGF0aW9uIG9mIHRoZSBmaXJzdCB0cmlwbGV0cyB0byBhdm9pZCByb3RhdGVkIHNvbHV0aW9ucwo6LSBsKDAsQixDLC0xKSwgc2IhPW9mZi4KCiUgIC0tLSBJTlRFUklPUiBQT0lOVFMgTE9HSUMgLS0tCiUgIERlZmluZSBpZiBwb2ludCBYIGlzIGluc2lkZSB0cmlhbmdsZSAoQSxCLEMpIGJhc2VkIG9uIHJlbGF0aXZlIG9yaWVudGF0aW9ucwppKEEsQixDLFgpIDotIGwoQSxYLEIsUiksIGwoQSxYLEMsLVIpLCBCPEMuCmkoQSxCLEMsWCkgOi0gbChCLFgsQyxSKSwgbChBLFgsQywtUiksIEE8Qi4KCiUgIENhbGN1bGF0ZSBpZiB0cmlhbmdsZSAoQSxCLEMpIGNvbnRhaW5zIG5vIG1vcmUgdGhhbiBKIGludGVyaW9yIHBvaW50cwp0cihBLEIsQyxKKSA6LSBwdChBKSxwdChCKSxwdChDKSwgQTxCLEI8Qywge2koQSxCLEMsWCl9PD1KLCBKPTAuLkksIGlucyhfLF8sSSksIEk9MC4uOTkuCgolICAtLS0gU0hBUEUgSU5URUdSSVRZIENPTlNUUkFJTlRTIC0tLQoKJSAgUGFpcnMKOi0gaW5zKHByLFosXyksICBjKEEsWiksYyhCLFopLCBBPEIuCgolICBUcmlhbmdsZXMKOi0gaW5zKHRyLFosSSksICBjKEEsWiksYyhCLFopLGMoQyxaKSwgIEE8QixCPEMsICB0cihBLEIsQyxJKS4KCiUgIENvbnZleCBxdWFkcmlsYXRlcmFscwo6LSBpbnMoY3YsWixJKSwgIGwoQSxCLEMsUiksIGwoQixDLEQsUiksICAgYyhBLFopLGMoQixaKSxjKEMsWiksYyhELFopLCAgQTxCLEI8QyxDPEQsICB0cihBLEIsQyxJMSksIHRyKEEsQyxELEkyKSwgSTErSTI9SS4KOi0gaW5zKGN2LFosSSksICBsKEEsQixELFIpLCBsKEEsQyxELC1SKSwgIGMoQSxaKSxjKEIsWiksYyhDLFopLGMoRCxaKSwgIEE8QixCPEMsQzxELCAgdHIoQSxCLEMsSTEpLCB0cihCLEMsRCxJMiksIEkxK0kyPUkuCgolICBOb24tY29udmV4IHF1YWRyaWxhdGVyYWxzCjotIGlucyhuYyxaLEkpLCAgbChBLEIsRCxSKSwgbChBLEIsQywtUiksICBjKEEsWiksYyhCLFopLGMoQyxaKSxjKEQsWiksICBBPEIsQjxDLEM8RCwgIHRyKEEsQixDLEkxKSwgdHIoQSxCLEQsSTIpLCBJMStJMj1JLgo6LSBpbnMobmMsWixJKSwgIGwoQSxCLEQsUiksIGwoQSxCLEMsLVIpLCAgYyhBLFopLGMoQixaKSxjKEMsWiksYyhELFopLCAgQTxCLEI8QyxDPEQsICB0cihBLEIsQyxJMSksIHRyKEIsQyxELEkyKSwgSTErSTI9SS4KOi0gaW5zKG5jLFosSSksICBsKEEsQixELFIpLCBsKEEsQixDLC1SKSwgIGMoQSxaKSxjKEIsWiksYyhDLFopLGMoRCxaKSwgIEE8QixCPEMsQzxELCAgdHIoQSxCLEQsSTEpLCB0cihCLEMsRCxJMiksIEkxK0kyPUkuCjotIGlucyhuYyxaLEkpLCAgbChBLEMsRCxSKSwgbChCLEMsRCwtUiksICBjKEEsWiksYyhCLFopLGMoQyxaKSxjKEQsWiksICBBPEIsQjxDLEM8RCwgIHRyKEEsQixDLEkxKSwgdHIoQSxDLEQsSTIpLCBJMStJMj1JLgo6LSBpbnMobmMsWixJKSwgIGwoQSxDLEQsUiksIGwoQixDLEQsLVIpLCAgYyhBLFopLGMoQixaKSxjKEMsWiksYyhELFopLCAgQTxCLEI8QyxDPEQsICB0cihBLEIsQyxJMSksIHRyKEIsQyxELEkyKSwgSTErSTI9SS4KOi0gaW5zKG5jLFosSSksICBsKEEsQyxELFIpLCBsKEIsQyxELC1SKSwgIGMoQSxaKSxjKEIsWiksYyhDLFopLGMoRCxaKSwgIEE8QixCPEMsQzxELCAgdHIoQSxDLEQsSTEpLCB0cihCLEMsRCxJMiksIEkxK0kyPUkuCgolICA0LWlzbGFuZHMKOi0gaW5zKGlzLFosSSksIGwoQSxCLEQsUiksIGwoQSxCLEMsLVIpLCAgIGMoQSxaKSxjKEIsWiksYyhDLFopLGMoRCxaKSwgIEE8QixCPEMsQzxELCAgdHIoQSxDLEQsSSkuCjotIGlucyhpcyxaLEkpLCBsKEEsQyxELFIpLCBsKEIsQyxELC1SKSwgICBjKEEsWiksYyhCLFopLGMoQyxaKSxjKEQsWiksICBBPEIsQjxDLEM8RCwgIHRyKEEsQixELEkpLgoKI3Nob3cgYy8yLgojc2hvdyBsLzQu
[8]: data:text/plain;base64,MXtjKEEsWikgOiBpbnMoXyxaLEkpLCBJPTAuLjk5fTEgOi0gcHQoQSku
[9]: data:text/plain;base64,Y2xpbmdvIEVTX2NvbG9yLmxwIC0tY29uZmlndXJhdGlvbj1mcnVtcHkgLS1zYXQtcD0zIC0taGV1cmlzdGljPURvbWFpbiAtYyBuYzE9MCAtYyB0cjI9MCAtYyBuPTEzClNBVElTRklBQkxFCmNsaW5nbyBFU19jb2xvci5scCAtLWNvbmZpZ3VyYXRpb249ZnJ1bXB5IC0tc2F0LXA9MyAtLWhldXJpc3RpYz1Eb21haW4gLWMgbmMxPTAgLWMgdHIyPTAgLWMgbj0xNApVTlNBVElTRklBQkxF
[10]: data:text/plain;base64,I2NvbnN0IHNiPW9mZi4KI2NvbnN0IHhncmlkPTEuCgp4KE4sTikgOi0gcHQoTiksIHhncmlkPTEuCgp4KDAsbi8yKSA6LSB4Z3JpZD4xLCBuXDI9MS4KeCgtKHhncmlkKioobi8yLU4tMSkpLE4pIDotIHB0KE4pLCBOPG4vMiwgeGdyaWQ+MS4KeCggeGdyaWQqKihOLShuLTEpLzItMSksIE4pIDotIHB0KE4pLCBOPihuLTEpLzIsIHhncmlkPjEuCgomc3VtIHtLQSp5KFhBKTsgS0IqeShYQik7IEtDKnkoWEMpfSA+PSAxIDotIGwoQSxCLEMsMSksICB4KFhBLEEpLHgoWEIsQikseChYQyxDKSwgS0E9WEMtWEIsIEtCPVhBLVhDLCBLQz1YQi1YQSwgeGdyaWQ+MC4KJnN1bSB7S0EqeShYQSk7IEtCKnkoWEIpOyBLQyp5KFhDKX0gPD0gLTE6LSBsKEEsQixDLC0xKSwgeChYQSxBKSx4KFhCLEIpLHgoWEMsQyksIEtBPVhDLVhCLCBLQj1YQS1YQywgS0M9WEItWEEsIHhncmlkPjAu
[11]: data:text/plain;base64,Y2xpbmdvLWxweCBscHggRVNfY29sb3IubHAgLWMgbmMxPTAgLWMgdHIyPTAgLWMgbj0xMyAtYyB4Z3JpZD0xCi4uLgp5KDApPTQ3MTkvMjI0IHkoMSk9MTEgeSgyKT03ODAxLzQ0OCB5KDMpPS0zMjMvMTEyIHkoNCk9LTEwODMzLzQ0OCB5KDUpPS0xMDQxMS8yMjQKeSg2KT00MTQzLzIyNCB5KDcpPS0zNDg5LzExMiB5KDgpPS0xMjMxLzMyIHkoOSk9NDU5MS84OTYgeSgxMCk9MSB5KDExKT0wIHkoMTIpPTAKU0FUSVNGSUFCTEU=
[12]: https://github.com/koshelevv/Erdos-Szekeres/tree/main/colored_points
[13]: data:text/plain;base64,cHQoMC4ubi0xKS4KCm1pbl9wMygzLDE7IDQsMzsgNSw3OyA2LDEzOyA3LDIxOyA4LDMxOyA5LDQzOyAxMCw1ODsgMTEsNzU7IDEyLDk0OyAxMywxMTQpLgptaW5fcDQoMywwOyA0LDA7IDUsMTsgNiwzOyA3LDY7IDgsMTA7IDksMTU7IDEwLDIzOyAxMSwzMjsgMTIsNDI7IDEzLDUxKS4KCm1pbl9wNSg5LDA7IDEwLDE7IDExLDI7IDEyLDM7IDEzLDM7IDE0LDY7IDE1LDk7IDE2LDExKS4KCjF7bChBLEIsQyxSKTogUj0oLTE7MSl9MSA6LSBwdChBKSxwdChCKSxwdChDKSwgQTxCLEI8Qy4KCjotIGwoQSxCLEMsUiksIGwoQSxDLEQsLVIpLCBsKEIsQyxELFIpLgo6LSBsKEEsQixDLFIpLCBsKEEsQixELC1SKSwgbChBLEMsRCxSKS4KOi0gbChBLEIsQyxSKSwgbChBLEIsRCwtUiksIGwoQixDLEQsUikuCjotIGwoQSxCLEQsUiksIGwoQSxDLEQsLVIpLCBsKEIsQyxELFIpLgo6LSBsKDEsQixDLC0xKSwgc2IhPW9mZi4KCmkoQSxCLEMsWCkgOi0gbChBLFgsQixSKSwgbChBLFgsQywtUiksIEI8Qy4KaShBLEIsQyxYKSA6LSBsKEIsWCxDLFIpLCBsKEEsWCxDLC1SKSwgQTxCLgoKbmUoQSxCLEMpIDotIGkoQSxCLEMsWCkuCgpwMyhBLEIsQykgOi0gcHQoQSkscHQoQikscHQoQyksIEE8QixCPEMsIG5vdCBuZShBLEIsQykuCgo6LSAjY291bnR7QSxCLEM6IHAzKEEsQixDKX09TSwgbWluX3AzKG4sTSksIHAzPS0xLgo6LSAjY291bnR7QSxCLEM6IHAzKEEsQixDKX0+TSwgbWluX3AzKG4sTSksIHAzPSAxLgoKcDQoQSxCLEMsRCkgOi0gbChBLEIsQyxSKSwgbChCLEMsRCxSKSwgQTxCLEI8QyxDPEQsIG5vdCBuZShBLEIsQyksIG5vdCBuZShBLEMsRCkuCnA0KEEsQixDLEQpIDotIGwoQSxCLEQsUiksIGwoQSxDLEQsLVIpLCBBPEIsQjxDLEM8RCwgbm90IG5lKEEsQixDKSwgbm90IG5lKEIsQyxEKS4KCjotICNjb3VudHtBLEIsQyxEOiBwNChBLEIsQyxEKX09TSwgbWluX3A0KG4sTSksIHA0PS0xLgo6LSAjY291bnR7QSxCLEMsRDogcDQoQSxCLEMsRCl9Pk0sIG1pbl9wNChuLE0pLCBwND0gMS4KCnA1KEEsQixDLEQsRSkgOi0gbChBLEIsQyxSKSwgbChCLEMsRCxSKSwgbChDLEQsRSxSKSwgQTxCLEI8QyxDPEQsRDxFLCBub3QgbmUoQSxCLEMpLCBub3QgbmUoQSxDLEQpLCBub3QgbmUoQSxELEUpLgpwNShBLEIsQyxELEUpIDotIGwoQSxCLEMsUiksIGwoQixDLEUsUiksIGwoQSxELEUsLVIpLCBBPEIsQjxDLEM8RCxEPEUsIG5vdCBuZShBLEIsQyksIG5vdCBuZShBLEMsRSksIG5vdCBuZShBLEQsRSkuCnA1KEEsQixDLEQsRSkgOi0gbChBLEIsRCxSKSwgbChCLEQsRSxSKSwgbChBLEMsRSwtUiksIEE8QixCPEMsQzxELEQ8RSwgbm90IG5lKEEsQixEKSwgbm90IG5lKEEsRCxFKSwgbm90IG5lKEEsQyxFKS4KcDUoQSxCLEMsRCxFKSA6LSBsKEEsQyxELFIpLCBsKEMsRCxFLFIpLCBsKEEsQixFLC1SKSwgQTxCLEI8QyxDPEQsRDxFLCBub3QgbmUoQSxDLEQpLCBub3QgbmUoQSxELEUpLCBub3QgbmUoQSxCLEUpLgoKOi0gI2NvdW50e0EsQixDLEQsRTogcDUoQSxCLEMsRCxFKX09TSwgbWluX3A1KG4sTSksIHA1PS0xLgo6LSAjY291bnR7QSxCLEMsRCxFOiBwNShBLEIsQyxELEUpfT5NLCBtaW5fcDUobixNKSwgcDU9IDEu
[14]: data:text/plain;base64,Zm9yIG4gaW4gYHNlcSAzIDExYDsgZG8KICBjbGluZ28gbWluaW1pemUubHAgLS1jb25maWd1cmF0aW9uPWNyYWZ0eSAtYyBwMz0xIC1jIHA0PS0xIC1jIG49JG47CiAgY2xpbmdvIG1pbmltaXplLmxwIC0tY29uZmlndXJhdGlvbj1jcmFmdHkgLWMgcDM9LTEgLWMgcDQ9MSAtYyBuPSRuOwpkb25lCgpjbGluZ28gbWluaW1pemUubHAgLS1jb25maWd1cmF0aW9uPWNyYWZ0eSAtYyBwND0xIC1jIHA1PS0xIC1jIG49OQpjbGluZ28gbWluaW1pemUubHAgLS1jb25maWd1cmF0aW9uPWNyYWZ0eSAtYyBwND0tMSAtYyBwNT0xIC1jIG49OQ==
[15]: data:text/plain;base64,Y2xpbmdvIG1pbmltaXplLmxwIC0tY29uZmlndXJhdGlvbj1jcmFmdHkgLWMgcDU9LTEgLWMgcDQ9MSAtYyBuPTEwClVOU0FUSVNGSUFCTEUKY2xpbmdvLWxweCBscHggbWluaW1pemUubHAgLS1jb25maWd1cmF0aW9uPWNyYWZ0eSAtYyBwNT0xIC1jIHA0PS0xIC1jIG49MTAgLWMgeGdyaWQ9MQpTQVRJU0ZJQUJMRQp5KDApPTIwMjMvMyB5KDEpPTM2NzMvNiB5KDIpPTU1MSB5KDMpPTQ1OSB5KDQpPTM1OSB5KDUpPTUyNS8yIHkoNik9MTU3Ny84IHkoNyk9OTAgeSg4KT0wIHkoOSk9MAoKY2xpbmdvIG1pbmltaXplLmxwIC0tY29uZmlndXJhdGlvbj1jcmFmdHkgLWMgcDU9LTEgLWMgcDQ9MSAtYyBuPTExClVOU0FUSVNGSUFCTEUKY2xpbmdvLWxweCBscHggbWluaW1pemUubHAgLS1jb25maWd1cmF0aW9uPWNyYWZ0eSAtYyBwNT0xIC1jIHA0PS0xIC1jIG49MTEgLWMgeGdyaWQ9MQpTQVRJU0ZJQUJMRQp5KDApPTQ3MDgxLzUgeSgxKT0tMTY5LzUgeSgyKT0zNjEvMyB5KDMpPTIyNjE1OTEvNDIwIHkoNCk9MSB5KDUpPS03MDAxNzMxLzQyMAp5KDYpPS0yMjYwNzUxLzIxMCB5KDcpPTQ1IHkoOCk9MTU2OTIvMTUgeSg5KT0wIHkoMTApPTA=
[16]: data:text/plain;base64,Zm9yIG4gaW4gYHNlcSA0IDEwYDsgZG8KICBmb3IgeGdyaWQgaW4gYHNlcSAwIDEyYDsgZG8KICAgIGNsaW5nby1scHggbWluaW1pemUubHAgbHB4IC0tY29uZmlndXJhdGlvbj1jcmFmdHkgLW4wIC0tcXVpZXQ9MiAtLWVudW0tbW9kZT1idCAtYyBwND0xIC1jIG49JG4gLWMgeGdyaWQ9JHhncmlkOwogIGRvbmU7CmRvbmU=
[17]: data:text/plain;base64,cHQoMS4ubikuCjF7bChBLEIsQyxSKTogUj0oLTE7MSl9MSA6LSBwdChBKSxwdChCKSxwdChDKSxBPEIsQjxDLgoKJSBHRU9NRVRSSUMgQ09OU1RSQUlOVFMKOi0gbChBLEIsQyxSKSwgbChBLEMsRCwtUiksIGwoQixDLEQsUikuCjotIGwoQSxCLEMsUiksIGwoQSxCLEQsLVIpLCBsKEEsQyxELFIpLgo6LSBsKEEsQixDLFIpLCBsKEEsQixELC1SKSwgbChCLEMsRCxSKS4KOi0gbChBLEIsRCxSKSwgbChBLEMsRCwtUiksIGwoQixDLEQsUikuCjotIGwoMSxCLEMsLTEpLCBzYiE9b2ZmLgoKJSBERUZJTklUSU9OIE9GIElOVEVSSU9SIFBPSU5UUwppKEEsQixDLFgpIDotIGwoQSxYLEIsUiksIGwoQSxYLEMsLVIpLCBCPEMuCmkoQSxCLEMsWCkgOi0gbChCLFgsQyxSKSwgbChBLFgsQywtUiksIEE8Qi4KCnRyKEEsQixDKSA6LSBwdChBKSwgcHQoQiksIHB0KEMpLCBBPEIsQjxDLCB7aShBLEIsQyxYKX08PWsuCgo6LSBsKEEsQixDLFIpLCBsKEIsQyxELFIpLCBsKEMsRCxFLFIpLCAgbChELEUsRixSKSwgIEE8QixCPEMsQzxELEQ8RSxFPEYsIHRyKEEsQyxFKS4KOi0gbChBLEIsQyxSKSwgbChCLEMsRCxSKSwgbChDLEQsRixSKSwgIGwoQSxFLEYsLVIpLCBBPEIsQjxDLEM8RCxEPEUsRTxGLCB0cihCLEQsRSkuCjotIGwoQSxCLEMsUiksIGwoQixDLEUsUiksIGwoQyxFLEYsUiksICBsKEEsRCxGLC1SKSwgQTxCLEI8QyxDPEQsRDxFLEU8RiwgdHIoQixELEUpLgo6LSBsKEEsQixELFIpLCBsKEIsRCxFLFIpLCBsKEQsRSxGLFIpLCAgbChBLEMsRiwtUiksIEE8QixCPEMsQzxELEQ8RSxFPEYsIHRyKEIsQyxFKS4KOi0gbChBLEMsRCxSKSwgbChDLEQsRSxSKSwgbChELEUsRixSKSwgIGwoQSxCLEYsLVIpLCBBPEIsQjxDLEM8RCxEPEUsRTxGLCB0cihCLEMsRSkuCjotIGwoQSxCLEMsUiksIGwoQixDLEYsUiksIGwoQSxELEUsLVIpLCBsKEQsRSxGLC1SKSwgQTxCLEI8QyxDPEQsRDxFLEU8RiwgdHIoQSxDLEUpLgo6LSBsKEEsQixELFIpLCBsKEIsRCxGLFIpLCBsKEEsQyxFLC1SKSwgbChDLEUsRiwtUiksIEE8QixCPEMsQzxELEQ8RSxFPEYsIHRyKEEsRCxFKS4KOi0gbChBLEMsRCxSKSwgbChDLEQsRixSKSwgbChBLEIsRSwtUiksIGwoQixFLEYsLVIpLCBBPEIsQjxDLEM8RCxEPEUsRTxGLCB0cihBLEQsRSkuCgojc2hvdyBsLzQu
[18]: data:text/plain;base64,Y2xpbmdvIEVTX2hleGFnb25zLmxwIC0tY29uZmlndXJhdGlvbj1mcnVtcHkgLS1zYXQtcD0zIC1jIGs9MiAtYyBuPTE2ClNBVElTRklBQkxFCmNsaW5nbyBFU19oZXhhZ29ucy5scCAtLWNvbmZpZ3VyYXRpb249ZnJ1bXB5IC0tc2F0LXA9MyAtYyBrPTIgLWMgbj0xNwpVTlNBVElTRklBQkxFCmNsaW5nbyBFU19oZXhhZ29ucy5scCAtLWNvbmZpZ3VyYXRpb249ZnJ1bXB5IC0tc2F0LXA9MyAtYyBrPTEgLWMgbj0xNwpTQVRJU0ZJQUJMRQpjbGluZ28gRVNfaGV4YWdvbnMubHAgLS1jb25maWd1cmF0aW9uPWZydW1weSAtLXNhdC1wPTMgLWMgaz0xIC1jIG49MTgKVU5TQVRJU0ZJQUJMRQ==
[19]: https://github.com/koshelevv/Erdos-Szekeres/tree/main/hexagons/original_sub4
[20]: data:text/plain;base64,aGV4YWdvbnMuc3ViNC5xMi4xOC5sb2c6IENQVSBUaW1lIDogMTYuNzAgaApoZXhhZ29ucy5zdWI0LnEzLjIwLmxvZzogQ1BVIFRpbWUgOiAzMTMuOTUgaApoZXhhZ29ucy5zdWI0LnE0LjIxLmxvZzogQ1BVIFRpbWUgOiA1MTM1LjUxIGg=
[21]: https://github.com/koshelevv/Erdos-Szekeres/tree/main/hexagons/original_ex
[22]: data:text/plain;base64,aGV4YWdvbnMuUV8wMTIuMTdwdC5sb2c6IENQVSBUaW1lIDogNC4xMyBoCmhleGFnb25zLlFfMDEzLjE3cHQubG9nOiBDUFUgVGltZSA6IDYuMDcgaApoZXhhZ29ucy5RXzAxNC4xN3B0LmxvZzogQ1BVIFRpbWUgOiAxMC44NiBoCmhleGFnb25zLlFfMDM0LjE5cHQubG9nOiBDUFUgVGltZSA6IDE4OC40MiBoCmhleGFnb25zLlFfMDQ1LjIwcHQubG9nOiBDUFUgVGltZSA6IDIyMjcuMzAgaA==
[23]: data:text/plain;base64,Zm9yIG4gaW4gMTcgMTggMTk7IGRvCiAgICAoY2F0IEVTX2hleGFnb25zLmxwOyBlY2hvICc6LSBsKEEsQixDLFIpLCBsKG4rMS1DLG4rMS1CLG4rMS1BLC1SKS4nKSB8IGNsaW5nbyAtYyBrPTAgLWMgbj0kbiAtYyBzYj1vZmY7CmRvbmUKU0FUSVNGSUFCTEUKVU5TQVRJU0ZJQUJMRQpVTlNBVElTRklBQkxF
[24]: https://github.com/koshelevv/Erdos-Szekeres/tree/main/hexagons
[25]: data:text/plain;base64,cHQoMS4ubikuCgppbnModHIsdDEsdHIxO3RyLHQyLHRyMjt0cix0Myx0cjMpLgoKMXtjKEEsQixaKTogaW5zKF8sWixJKSxJPTAuLjk5fTEgOi0gcHQoQSkscHQoQiksIEE8Qi4KMXtsKEEsQixDLFIpOiBSPSgtMTsxKX0xIDotIHB0KEEpLHB0KEIpLHB0KEMpLCBBPEIsQjxDLgoKJSBHRU9NRVRSSUMgQ09OU1RSQUlOVFMKOi0gbChBLEIsQyxSKSwgbChBLEMsRCwtUiksIGwoQixDLEQsUikuCjotIGwoQSxCLEMsUiksIGwoQSxCLEQsLVIpLCBsKEEsQyxELFIpLgo6LSBsKEEsQixDLFIpLCBsKEEsQixELC1SKSwgbChCLEMsRCxSKS4KOi0gbChBLEIsRCxSKSwgbChBLEMsRCwtUiksIGwoQixDLEQsUikuCjotIGwoMSxCLEMsLTEpLCBzYiE9b2ZmLgoKJSBERUZJTklUSU9OIE9GIElOVEVSSU9SIFBPSU5UUwppKEEsQixDLFgpIDotIGwoQSxYLEIsUiksIGwoQSxYLEMsLVIpLCBCPEMuCmkoQSxCLEMsWCkgOi0gbChCLFgsQyxSKSwgbChBLFgsQywtUiksIEE8Qi4KCnRyKEEsQixDLEkpIDotIHB0KEEpLHB0KEIpLHB0KEMpLCBBPEIsQjxDLCB7aShBLEIsQyxYKX08PUksIGlucyhfLF8sSSksIEk9MC4uOTkuCgo6LSBpbnModHIsWixJKSwgQTxCLEI8QywgYyhBLEIsWiksIGMoQSxDLFopLCBjKEIsQyxaKSwgdHIoQSxCLEMsSSkuCgojc2hvdyBsLzQuCiNzaG93IGMvMy4=
[26]: data:text/plain;base64,Y2xpbmdvIEVTX1JhbXNleS5scCAtLWNvbmZpZ3VyYXRpb249ZnJ1bXB5IC0tc2F0LXA9MyAtYyB0cjE9MCAtYyB0cjI9MCAtYyBuPTIxClVOU0FUSVNGSUFCTEUKQ1BVIFRpbWUgOiAxMzU2NzgyLjk5NnM=
[27]: https://github.com/koshelevv/Erdos-Szekeres/tree/main/geometric_Ramsey_numbers
[28]: data:text/plain;base64,Y2xpbmdvLWxweCBFU19SYW1zZXkubHAgbHB4IC0tY29uZmlndXJhdGlvbj1mcnVtcHkgLS1zYXQtcD0zIC1jIHRyMT0wIC1jIHRyMj05OSAtYyBuPTE2ClNBVElTRklBQkxFCnkoMSk9LTI4MzMvMiB5KDIpPS0xMDQwOS84IHkoMyk9LTQ3MzkvNCB5KDQpPTEgeSg1KT0tOTU0IHkoNik9LTQzMzI3LzU2IHkoNyk9LTQ4MTgvNyB5KDgpPS00ODE1LzgKeSg5KT0tNjA3IHkoMTApPTg1MDkvMyB5KDExKT01OTU2My8xOCB5KDEyKT0yNDc2MjczLzY0OCB5KDEzKT0tODAxLzQgeSgxNCk9LTE1ODEvMTYgeSgxNSk9MCB5KDE2KT0wCgpjbGluZ28tbHB4IEVTX1JhbXNleS5scCBscHggLS1jb25maWd1cmF0aW9uPWZydW1weSAtLXNhdC1wPTMgLWMgdHIxPTEgLWMgdHIyPTEgLWMgbj03ClNBVElTRklBQkxFCnkoMSk9My8yIHkoMik9MSB5KDMpPS0xIHkoNCk9LTEzIHkoNSk9LTYgeSg2KT0wIHkoNyk9MAoKY2xpbmdvLWxweCBFU19SYW1zZXkubHAgbHB4IC0tY29uZmlndXJhdGlvbj1mcnVtcHkgLS1zYXQtcD0zIC1jIHRyMT0xIC1jIHRyMj05OSAtYyBuPTYKU0FUSVNGSUFCTEUKeSgxKT01IHkoMik9Ny8yIHkoMyk9LTEgeSg0KT0zLzIgeSg1KT0wIHkoNik9MAoKY2xpbmdvIEVTX1JhbXNleS5scCAtLWNvbmZpZ3VyYXRpb249ZnJ1bXB5IC0tc2F0LXA9MyAtYyB0cjE9MCAtYyB0cjI9MSAtYyBuPTE3ClVOU0FUSVNGSUFCTEUKY2xpbmdvIEVTX1JhbXNleS5scCAtLWNvbmZpZ3VyYXRpb249ZnJ1bXB5IC0tc2F0LXA9MyAtYyB0cjE9MSAtYyB0cjI9MSAtYyBuPTgKVU5TQVRJU0ZJQUJMRQpjbGluZ28gRVNfUmFtc2V5LmxwIC0tY29uZmlndXJhdGlvbj1mcnVtcHkgLS1zYXQtcD0zIC1jIHRyMT0xIC1jIHRyMj0yIC1jIG49NwpVTlNBVElTRklBQkxF
[29]: https://arxiv.org/pdf/0910.2700
