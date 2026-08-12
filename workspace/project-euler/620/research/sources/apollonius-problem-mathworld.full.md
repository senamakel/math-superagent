<!-- source: https://mathworld.wolfram.com/ApolloniusProblem.html | converted from HTML -->

Apollonius' Problem -- from Wolfram MathWorld

# Apollonius' Problem

---

[image: ApolloniusCircles]

[image: ApolloniusCircles8]

Given three objects, each of which may be a [point][1], [line][2], or [circle][3], draw a [circle][3] that is [tangent][4] to each. There are a total of ten cases. The two easiest involve three points or three [lines][2], and the hardest involves three [circles][3]. Euclid solved the two easiest cases in his *Elements*, and the others (with the exception of the three [circle][3] problem), appeared in the *Tangencies*of Apollonius which was, however, lost. The general problem is, in principle, solvable by [straightedge][5] and [compass][6] alone.

[image: ApolloniusCircleConstr]

The three- [circle][3] problem was solved by Vi&egrave;te (Boyer 1968), and the solutions are called [Apollonius circles][7]. There are eight total solutions. The simplest solution is obtained by solving the three simultaneous quadratic equations

[image:  (x-x_1)^2+(y-y_1)^2-(r+/-r_1)^2=0 ] |

(1)

 |

[image:  (x-x_2)^2+(y-y_2)^2-(r+/-r_2)^2=0 ] |

(2)

 |

[image:  (x-x_3)^2+(y-y_3)^2-(r+/-r_3)^2=0 ] |

(3)

 |

in the three [unknowns][8][image: x], [image: y], [image: r] for the eight triplets of signs (Courant and Robbins 1996). Expanding the equations gives

[image:  (x^2+y^2-r^2)-2xx_i-2yy_i∓2rr_i+(x_i^2+y_i^2-r_i^2)=0 ] |

(4)

 |

for [image: i=1], 2, 3. Since the first term is the same for each equation, taking [image: (2)-(1)] and [image: (3)-(1)] gives

[image:  ax+by+cr=d ] |

(5)

 |

[image:  a^'x+b^'y+c^'r=d^', ] |

(6)

 |

where

[image: a] | [image: =] | [image: 2(x_1-x_2)] |

(7)

 |

[image: b] | [image: =] | [image: 2(y_1-y_2)] |

(8)

 |

[image: c] | [image: =] | [image: 2(+/-r_1+/-r_2)] |

(9)

 |

[image: d] | [image: =] | [image: (x_1^2+y_1^2-r_1^2)-(x_2^2+y_2^2-r_2^2)] |

(10)

 |

and similarly for [image: a^'], [image: b^'], [image: c^'] and [image: d^'] (where the 2 subscripts are replaced by 3s). Solving these two simultaneous linear equations gives

[image: x] | [image: =] | [image: (b^'d-bd^'-b^'cr+bc^'r)/(ab^'-ba^')] |

(11)

 |

[image: y] | [image: =] | [image: (-a^'d+ad^'+a^'cr-ac^'r)/(ab^'-a^'b),] |

(12)

 |

which can then be plugged back into the [quadratic equation][9] (1) and solved using the [quadratic formula][10].

Perhaps the most elegant solution is due to Gergonne. It proceeds by locating the six [homothetic centers][11] (three internal and three external) of the three given [circles][3]. These lie three by three on four lines (illustrated above). Determine the [inversion poles][12] of one of these with respect to each of the three [circles][3] and connect the [inversion poles][12] with the [radical center][13] of the [circles][3]. If the connectors meet, then the three pairs of intersections are the points of tangency of two of the eight circles (Petersen 1879, Johnson 1929, D&ouml;rrie 1965). To determine *which*two of the eight Apollonius circles are produced by the three pairs, simply take the two which [intersect][14] the original three [circles][3] only in a single point of tangency. The procedure, when repeated, gives the other three pairs of [circles][3].

If the three [circles][3] are mutually tangent, then the eight solutions collapse to two, known as the [Soddy circles][15].

Larmor (1891) and Lachlan (1893, pp. 244-251) consider the problem of four circles having a common tangent circle.

---

## See also

[Apollonius Point][16], [Apollonius Pursuit Problem][17], [Bend][18], [Casey's Theorem][19], [Circular Triangle][20], [Descartes Circle Theorem][21], [Four Coins Problem][22], [Hart Circle][23], [Hart's Theorem][24], [Soddy Circles][15]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [circle squaring][25]
- [cissoid of Diocles][26]
- [12 by 12 multiplication table][27]

## References

Altshiller-Court, N. *[College Geometry: A Second Course in Plane Geometry for Colleges and Normal Schools, 2nd ed., rev. enl.][28]*New York: Barnes and Noble, p. 226, 1952. Boyer, C. B. *[A History of Mathematics.][29]*New York: Wiley, p. 159, 1968. Courant, R. and Robbins, H. "Apollonius' Problem." &sect;3.3 in *[What Is Mathematics?: An Elementary Approach to Ideas and Methods, 2nd ed.][30]*Oxford, England: Oxford University Press, pp. 117 and 125-127, 1996. D&ouml;rrie, H. "The Tangency Problem of Apollonius." &sect;32 in *[100 Great Problems of Elementary Mathematics: Their History and Solutions.][31]*New York: Dover, pp. 154-160, 1965. F. Gabriel-Marie. *Exercices de g&eacute;om&eacute;trie.*Tours, France: Maison Mame, pp. 18-20 and 663, 1912. Gauss, C. F. *[Werke, Band 4.][32]*New York: George Olms, p. 399, 1981. Gergonne, M. "Recherche du cercle qui en touche trois autres sur une sph&egrave;re." *Ann. math. pures appl.***4**, 1813-1814. Johnson, R. A. *[Modern Geometry: An Elementary Treatise on the Geometry of the Triangle and the Circle.][33]*Boston, MA: Houghton Mifflin, pp. 118-121, 1929. Lachlan, R. "Circles with Touch Three Given Circles" and "Systems of Four Circles Having a Common Tangent Circle." &sect;383-396 in *[An Elementary Treatise on Modern Pure Geometry.][34]*London, England: Macmillian, pp. 241-251, 1893. Larmor, A. "Contacts of Systems of Circles." *Proc. London Math. Soc.***23**, 136-157, 1891. Ogilvy, C. S. *[Excursions in Geometry.][35]*New York: Dover, pp. 48-51, 1990. Pappas, T. *[The Joy of Mathematics.][36]*San Carlos, CA: Wide World Publ./Tetra, p. 151, 1989. Petersen, J. Example 403 in *[Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems.][37]*London, England: Sampson Low, Marston, Searle & Rivington, pp. 94-95, 1879. Rouch&eacute;, E. and de Comberousse, C. *[Trait&eacute; de g&eacute;om&eacute;trie plane.][38]*Paris, France: Gauthier-Villars, pp. 297-303, 1900. Salmon, G. *[Conic Sections, 6th ed.][39]*New York: Chelsea, pp. 88-135, 1960. Simon, M. *&Uuml;ber die Entwicklung der Elementargeometrie im XIX. Jahrhundert.*Leipzig: Teubner, pp. 97-105, 1906. Wells, D. *[The Penguin Dictionary of Curious and Interesting Geometry.][40]*London, England: Penguin, pp. 4-5, 1991.

## Referenced on Wolfram|Alpha

[Apollonius' Problem][41]

## Cite this as:

[Weisstein, Eric W.][42] "Apollonius' Problem." From **[MathWorld][43] --A Wolfram Resource. [https://mathworld.wolfram.com/ApolloniusProblem.html][44]

## Subject classifications


## Links

[1]: /Point.html
[2]: /Line.html
[3]: /Circle.html
[4]: /Tangent.html
[5]: /Straightedge.html
[6]: /Compass.html
[7]: /ApolloniusCircle.html
[8]: /Unknown.html
[9]: /QuadraticEquation.html
[10]: /QuadraticFormula.html
[11]: /HomotheticCenter.html
[12]: /InversionPole.html
[13]: /RadicalCenter.html
[14]: /Intersection.html
[15]: /SoddyCircles.html
[16]: /ApolloniusPoint.html
[17]: /ApolloniusPursuitProblem.html
[18]: /Bend.html
[19]: /CaseysTheorem.html
[20]: /CircularTriangle.html
[21]: /DescartesCircleTheorem.html
[22]: /FourCoinsProblem.html
[23]: /HartCircle.html
[24]: /HartsTheorem.html
[25]: https://www.wolframalpha.com/input/?i=angle+trisection
[26]: https://www.wolframalpha.com/input/?i=cissoid+of+Diocles
[27]: https://www.wolframalpha.com/input/?i=12+by+12+multiplication+table
[28]: http://www.amazon.com/exec/obidos/ASIN/B0007HQ866/ref=nosim/ericstreasuretro
[29]: http://www.amazon.com/exec/obidos/ASIN/0471543977/ref=nosim/ericstreasuretro
[30]: http://www.amazon.com/exec/obidos/ASIN/0195105192/ref=nosim/ericstreasuretro
[31]: http://www.amazon.com/exec/obidos/ASIN/0486613488/ref=nosim/ericstreasuretro
[32]: http://www.amazon.de/exec/obidos/ASIN/3487046326/ref=nosim/mathworld02-21
[33]: http://www.amazon.com/exec/obidos/ASIN/B0007DU7SK/ref=nosim/ericstreasuretro
[34]: http://www.amazon.com/exec/obidos/ASIN/B0008CQ720/ref=nosim/ericstreasuretro
[35]: http://www.amazon.com/exec/obidos/ASIN/0486265307/ref=nosim/ericstreasuretro
[36]: http://www.amazon.com/exec/obidos/ASIN/0933174659/ref=nosim/ericstreasuretro
[37]: http://www.amazon.com/exec/obidos/ASIN/B00086D9EK/ref=nosim/ericstreasuretro
[38]: http://www.amazon.fr/exec/obidos/ASIN/B0000DQV3B/ref=nosim/mathworld09-21
[39]: http://www.amazon.com/exec/obidos/ASIN/0828400997/ref=nosim/ericstreasuretro
[40]: http://www.amazon.com/exec/obidos/ASIN/0140118136/ref=nosim/ericstreasuretro
[41]: https://www.wolframalpha.com/input/?i=apollonius+problem
[42]: /about/author.html
[43]: /
[44]: https://mathworld.wolfram.com/ApolloniusProblem.html
