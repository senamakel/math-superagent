<!-- source: https://mathworld.wolfram.com/HappyEndProblem.html | converted from HTML -->

Happy End Problem -- from Wolfram MathWorld

# Happy End Problem

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: HappyEndProblem]

The happy end problem, also called the "happy ending problem," is the problem of determining for [image: n>=3] the smallest number of [points][2][image: g(n)] in [general position][3] in the [plane][4] (i.e., no three of which are [collinear][5]), such that every possible arrangement of [image: g(n)] [points][2] will always contain at least one [set][6] of [image: n] [points][2] that are the [vertices][7] of a [convex polygon][8] of [image: n] sides. The problem was so-named by Erdős when two investigators who first worked on the problem, Ester Klein and George Szekeres, became engaged and subsequently married (Hoffman 1998, p. 76).

Since three non [collinear][5] [points][2] always determine a [triangle][9], [image: g(3)=3].

[image: HappyEndProblem4]

Random arrangements of [image: n=4] [points][2] are illustrated above. Note that no convex [quadrilaterals][10] are possible for the arrangements shown in the fifth and eighth figures above, so [image: g(4)] must be greater than 4. E. Klein proved that [image: g(4)=5] by showing that any arrangement of five [points][2] must fall into one of the three cases (left top figure; Hoffman 1998, pp. 75-76).

[image: HappyEndProblem8]

Random arrangements of [image: n=8] [points][2] are illustrated above. Note that no convex [pentagons][11] are possible for the arrangement shown in the fifth figure above, so [image: g(5)] must be greater than 8. E. Makai proved [image: g(5)=9] after demonstrating that a [counterexample][12] could be found for eight [points][2] (right top figure; Hoffman 1998, pp. 75-76).

As the number of [points][2][image: n] increases, the number of **[k -subsets][13] of [image: n] that must be examined to see if they form convex [image: k] - [gons][14] increases as [image: (n; k)], so combinatorial explosion prevents cases much bigger than [image: n=5] from being easily studied. Furthermore, the parameter space becomes so large that searching for a [counterexample][12] at random even for the case [image: n=6] with [image: k=12] [points][2] takes an extremely long time. For these reasons, the general problem remains open.

[image: g(6)=17] was demonstrated by Szekeres and Peters (2006) using a 1500 CPU-hour computer search that eliminated all possible [configurations][15] of 17 [points][2] that lacked convex [hexagons][16] while examining only a tiny fraction of all [configurations][15]. Marić (2019) and Scheucher (2020) independently verified [image: g(6)=17] using [satisfiability][17] (SAT) solving in a few CPU hours, a time later reduced to 10 CPU-minutes by Scheucher (2023) and to 8.53 CPU-seconds by Heule and Scheucher (2024).

The first few values of [image: g(n)] for [image: n=3], 4, 5, and 6 are therefore 3, 5, 9, 17, which happen to be exactly [image: 2^(n-2)+1]. However, the values of [image: g(n)] for [image: n>=7] are unknown.

[image: HappyEndProblem81632]

The [lower bound][18] construction of Erdős and Szekeres (1961) gives, for every [image: n>=3], a [point set][19] of [image: 2^(n-2)] [points][2] in [general position][3] containing no [set][6] of [image: n] [points][2] that forms a [convex polygon][8]. Examples with 8, 16, and 32 [points][2] containing no [convex polygon][8] with 5, 6, and 7 [vertices][7], respectively, are illustrated above. The 32- [point][2] integer-coordinate realization lies in a [image: 230×310] [grid][20] (Duque *et al. *2018).

Combining this construction with the [upper bound][21] of Erdős and Szekeres (1935) gives

[image:  2^(n-2)+1<=g(n)<=(2n-4; n-2)+1, ] |

(1)

 |

where [image: (n; k)] is a [binomial coefficient][22]. For [image: n>=4], this has since been reduced to [image: g(n)<=g_1(n)] for

[image:  g_1(n)=(2n-4; n-2) ] |

(2)

 |

by Chung and Graham (1998), [image: g(n)<=g_2(n)] for

[image:  g_2(n)=(2n-4; n-2)+7-2n ] |

(3)

 |

by Kleitman and Pachter (1998), and [image: g(n)<=g_3(n)] for

[image:  g_3(n)=(2n-5; n-2)+2 ] |

(4)

 |

by T&oacute;th and Valtr (1998).

---

## See also

[Convex Hull][23], [Convex Polygon][8], [Point Set][19]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [(2*3 + 3*4 + 4*5) / (10 - 5)][24]
- [diagonalize {{1,2},{3,4}}][25]
- [New Mexico lottery][26]

## References

Borwein, J. and Bailey, D. *[Mathematics by Experiment: Plausible Reasoning in the 21st Century.][27]*Wellesley, MA: A K Peters, p. 78, 2003. Chung, F. R. K. and Graham, R. L. "Forced Convex [image: n] -gons in the Plane." *Discr. Comput. Geom.***19**, 367-371, 1998. Duque, F.; Fabila-Monroy, R.; and Hidalgo-Toscano, C. "Point Sets with Small Integer Coordinates and no Large Convex Polygons." *Discr. Comput. Geom.***59**, 461-476, 2018. [https://doi.org/10.1007/s00454-017-9931-6][28]. Erdős, P. and Szekeres, G. "A Combinatorial Problem in Geometry." *Compositio Math.***2**, 463-470, 1935. Erdős, P. and Szekeres, G. "On Some Extremum Problems in Elementary Geometry." *Ann. Univ. Sci. Budapest Eőtvős Soc. Math.***3-4**, 53-62, 1961. Heule, M. J. H. and Scheucher, M. "Happy Ending: An Empty Hexagon in Every Set of 30 Points." 1 Mar 2024. [https://arxiv.org/abs/2403.00737][29]. Hoffman, P. *[The Man Who Loved Only Numbers: The Story of Paul Erdős and the Search for Mathematical Truth.][30]*New York: Hyperion, pp. 75-78, 1998. Kleitman, D. and Pachter, L. "Finding Convex Sets among Points in the Plane." *Discr. Comput. Geom.***19**, 405-410, 1998. Lov&aacute;sz, L.; Pelik&aacute;n, J.; and Vesztergombi, K. *[Discrete Mathematics, Elementary and Beyond.][31]*New York: Springer-Verlag, 2003. Marić, F. "Fast Formal Proof of the Erdős-Szekeres Conjecture for Convex Polygons with at Most 6 Points." *J. Automated Reasoning***62**, 301-329, 2019. Scheucher, M. "Two Disjoint 5-Holes in Point Sets." *Comput. Geom.***91**, 101670, 2020. Scheucher, M. "A SAT Attack on Erdős-Szekeres Numbers in Rd and the Empty Hexagon Theorem." *Computing in Geometry and Topology***2**, 2:1-2:13, 2023. Soifer, A. "The Happy End Problem." Ch. 31 in *[The New Mathematical Coloring Book: Mathematics of Coloring and the Colorful Life of Its Creators, 2nd ed.][32]*New York: Springer, pp. 321-337, 2024. Szekeres, G. and Peters, L. "Computer Solution to the 17-Point Erdős-Szekeres Problem." *ANZIAM J.***48**, 151-164, 2006. T&oacute;th, G. and Valtr, P. "Note on the Erdős-Szekeres Theorem." *Discr. Comput. Geom.***19**, 457-459, 1998.

## Referenced on Wolfram|Alpha

[Happy End Problem][33]

## Cite this as:

[Weisstein, Eric W.][34] "Happy End Problem." From **[MathWorld][35] --A Wolfram Resource. [https://mathworld.wolfram.com/HappyEndProblem.html][36]

## Subject classifications


## Links

[1]: /notebooks/ComputationalGeometry/HappyEndProblem.nb
[2]: /Point.html
[3]: /GeneralPosition.html
[4]: /Plane.html
[5]: /Collinear.html
[6]: /Set.html
[7]: /Vertex.html
[8]: /ConvexPolygon.html
[9]: /Triangle.html
[10]: /Quadrilateral.html
[11]: /Pentagon.html
[12]: /Counterexample.html
[13]: /k-Subset.html
[14]: /Polygon.html
[15]: /Configuration.html
[16]: /Hexagon.html
[17]: /SatisfiabilityProblem.html
[18]: /LowerBound.html
[19]: /PointSet.html
[20]: /Grid.html
[21]: /UpperBound.html
[22]: /BinomialCoefficient.html
[23]: /ConvexHull.html
[24]: https://www.wolframalpha.com/input/?i=%282*3+%2B+3*4+%2B+4*5%29+%2F+%2810+-+5%29
[25]: https://www.wolframalpha.com/input/?i=diagonalize+%7B%7B1%2C2%7D%2C%7B3%2C4%7D%7D
[26]: http://www.wolframalpha.com/input/?i=New+Mexico+lottery
[27]: http://www.amazon.com/exec/obidos/ASIN/1568812116/ref=nosim/ericstreasuretro
[28]: https://doi.org/10.1007/s00454-017-9931-6
[29]: https://arxiv.org/pdf/2403.00737
[30]: http://www.amazon.com/exec/obidos/ASIN/0786863625/ref=nosim/ericstreasuretro
[31]: http://www.amazon.com/exec/obidos/ASIN/0387955852/ref=nosim/ericstreasuretro
[32]: http://www.amazon.com/exec/obidos/ASIN/1071635964/ref=nosim/ericstreasuretro
[33]: https://www.wolframalpha.com/input/?i=happy+end+problem
[34]: /about/author.html
[35]: /
[36]: https://mathworld.wolfram.com/HappyEndProblem.html
