<!-- source: https://en.wikipedia.org/wiki/Enumerative_geometry | converted from HTML -->

Enumerative geometry - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Branch of algebraic geometry concerned with counting solutions

See also: [Intersection theory][1]

 |

This article includes a list of [general references][2]**but lacks sufficient corresponding [inline citations][3]**. Please help [improve this article][4] by [introducing][5] more precise citations.*( September 2012)**( [Learn how and when to remove this message][6])*

 |

In [mathematics][7], **enumerative geometry**is the branch of [algebraic geometry][8] concerned with counting numbers of solutions to geometric questions, mainly by means of [intersection theory][1]. [*[citation needed][9]*]

While mathematicians mostly lost interest in the field, popular with the Ancient Greeks and afterward, in the mid-1900s, it has experienced a recent reawakening as methods have been discovered to apply [motivic homotopy theory][10] to the problems. [1]

## History

[[edit][11]]

[12] [Circles of Apollonius][13]

The [problem of Apollonius][13] is an early example of an enumerative geometry problem, which were popular with the Ancient Greeks. [1] This problem asks for the number and construction of circles that are tangent to three given circles, points or lines. [1] In general, the problem for three given circles has eight solutions, [1] which can be seen as 2 3, each tangency condition imposing a quadratic condition on the space of circles. [*[citation needed][9]*] However, for special arrangements of the given circles, the number of solutions may also be any integer from 0 (no solutions) to six; there is no arrangement for which there are seven solutions to Apollonius' problem. [*[citation needed][9]*]

Enumerative geometry got much more complicated over time, with questions becoming more complicated: for example, the number of lines on a cubic surface, or the number of quadratic curves on a quintic surface. [1]

By about 1900, mathematicians had figured out how to solve any enumerative geometry problem over the complex numbers, but these methods failed to apply to any other number systems. [1] At the time, some believed that studying enumerative geometry problems over other number systems, such as the integers, would reveal fundamental properties of the number systems and lead to new areas of mathematics. [1] Hilbert, one of these people, included an enumerative geometry problem in the [Hilbert problems][14]. [1]

By the mid-1900s, the field had become much less popular, with mathematicians beginning to focus on more abstract topics. [1] There was a brief reawakening of interest in the 1990s. [1]

Recently, mathematicians have discovered how to apply [motivic homotopy theory][10] to enumerative geometry problems. [1] This allows a quadratic form to be constructed from each problem, which can be used to derive information about the solutions in any number system. [1] For example, in the complex numbers, the number of solutions equals the number of terms, and in the real numbers the signature (# of positive terms - # of negative terms) gave a lower bound for the number of solutions; in other number systems it becomes more complicated, and deriving information from these quadratic forms is an active area of study. [1]

## Key tools

[[edit][15]]

A number of tools, ranging from the elementary to the more advanced, include:

- [Dimension counting][16]
- [Bézout's theorem][17]
- [Schubert calculus][18], and more generally [characteristic classes][19] in [cohomology][20]
- The connection of counting intersections with cohomology is [Poincaré duality][21]
- The study of [moduli spaces][22] of curves, maps and other geometric objects, sometimes via the theory of [quantum cohomology][23]. The study of [quantum cohomology][23], [Gromov–Witten invariants][24] and [mirror symmetry][25] gave significant progress in [Clemens conjecture][26].

Enumerative geometry is very closely tied to [intersection theory][1]. [2]

More recently, [motivic homotopy theory][10] is included. [1]

## Schubert calculus

[[edit][27]]

Enumerative geometry saw spectacular development towards the end of the nineteenth century, at the hands of [Hermann Schubert][28]. [3] He introduced it for the purpose of [Schubert calculus][18], which has proved of fundamental geometrical and [topological][29] value in broader areas. The specific needs of enumerative geometry were not addressed until some further attention was paid to them in the 1960s and 1970s (as pointed out for example by [Steven Kleiman][30]). [Intersection numbers][31] had been rigorously defined (by [André Weil][32] as part of his foundational programme 1942 – 6, [4] and again subsequently), but this did not exhaust the proper domain of enumerative questions.

## Fudge factors and Hilbert's fifteenth problem

[[edit][33]]

Naïve application of dimension counting and Bézout's theorem yields incorrect results, as the following example shows. In response to these problems, algebraic geometers introduced vague " [fudge factors][34] ", which were only rigorously justified decades later.

As an example, count the [conic sections][35] tangent to five given lines in the [projective plane][36]. [5] The conics constitute a [projective space][37] of dimension 5, taking their six coefficients as [homogeneous coordinates][38], and [five points determine a conic][39], if the points are in [general linear position][40], as passing through a given point imposes a linear condition. Similarly, tangency to a given line *L*(tangency is intersection with multiplicity two) is one quadratic condition, so determined a [quadric][41] in *P*5. However the [linear system of divisors][42] consisting of all such quadrics is not without a [base locus][43]. In fact each such quadric contains the [Veronese surface][44], which parametrizes the conics

(*aX*+ *bY*+ *cZ*) 2 = 0

called 'double lines'. This is because a double line intersects every line in the plane, since lines in the projective plane intersect, with multiplicity two because it is doubled, and thus satisfies the same intersection condition (intersection of multiplicity two) as a nondegenerate conic that is *tangent*to the line.

The general [Bézout theorem][45] says 5 general quadrics in 5-space will intersect in 32 = 2 5 points. But the relevant quadrics here are not in [general position][46]. From 32, 31 must be subtracted and attributed to the Veronese, to leave the correct answer (from the point of view of geometry), namely 1. This process of attributing intersections to 'degenerate' cases is a typical geometric introduction of a ' [fudge factor][47] '.

[Hilbert's fifteenth problem][48] was to overcome the apparently arbitrary nature of these interventions; this aspect goes beyond the foundational question of the Schubert calculus itself.

## Clemens conjecture

[[edit][49]]

In 1984 [H. Clemens][50] studied the counting of the number of [rational curves][51] on a [quintic threefold][52] X ⊂ P 4 {\displaystyle X\subset P^{4}}[image: {\displaystyle X\subset P^{4}}] and reached the following conjecture.

Let X ⊂ P 4 {\displaystyle X\subset P^{4}}[image: {\displaystyle X\subset P^{4}}] be a general quintic threefold, d {\displaystyle d}[image: {\displaystyle d}] a positive integer, then there are only a finite number of rational curves with degree d {\displaystyle d}[image: {\displaystyle d}] on X {\displaystyle X}[image: {\displaystyle X}].

This conjecture has been resolved in the case d ≤ 9 {\displaystyle d\leq 9}[image: {\displaystyle d\leq 9}], but is still open for higher d {\displaystyle d}[image: {\displaystyle d}].

In 1991 the paper [6] about mirror symmetry on the quintic threefold in P 4 {\displaystyle P^{4}}[image: {\displaystyle P^{4}}] from the string theoretical viewpoint gives numbers of degree d rational curves on X {\displaystyle X}[image: {\displaystyle X}] for all 0"}}'> 0}"> d > 0 {\displaystyle d>0} 0}"/>. Prior to this, algebraic geometers could calculate these numbers only for d ≤ 5 {\displaystyle d\leq 5}[image: {\displaystyle d\leq 5}].

## Examples

[[edit][53]]

Some of the historically important examples of enumerations in algebraic geometry include:

- 2 The number of lines meeting 4 general lines in space
- 8 The number of circles tangent to 3 general circles (the [problem of Apollonius][13]).
- 27 The number of lines on a smooth [cubic surface][54] ( [Salmon][55] and [Cayley][56])
- 2875 The number of lines on a general [quintic threefold][52]
- 3264 The number of [conics tangent to 5 plane conics][57] in general position ( [Chasles][58])
- 609250 The number of conics on a general [quintic threefold][52]
- 4407296 The number of conics tangent to 8 general quadric surfaces Fulton (1984, p. 193)
- 666841088 The number of quadric surfaces tangent to 9 given quadric surfaces in general position in 3-space ( Schubert 1879, p.106) ( Fulton 1984, p. 193)
- 5819539783680 The number of twisted cubic curves tangent to 12 given quadric surfaces in general position in 3-space ( Schubert 1879, p.184) (S. Kleiman, S. A. Strømme & S. Xambó 1987)

## References

[[edit][59]]

1. 1 2 3 4 5 6 7 8 9 10 11 12 13 14 Howlett, Joseph (2025-09-26). ["New Math Revives Geometry's Oldest Problems"][60]. *Quanta Magazine*. Retrieved 2025-09-26.
2. ↑ [Kleiman, Steven L.][30]; Thorup, Anders (1987). "Intersection Theory and Enumerative Geometry: A Decade in Review". *Algebraic Geometry–Bowdoin 1985, Part 2*. Proceedings of Symposia in Pure Mathematics. Vol. 46.2. American Mathematical Society. pp. 321– 370. [doi][61]: [10.1090/pspum/046.2][62]. [ISBN][63] [978-0-8218-1480-2][64]. [MR][65] [0927987][66].
3. ↑ Schubert, H. (1879). *Kalkül der abzählenden Geometrie*(published 1979).
4. ↑ Weil, Andre (1947). *Foundations of Algebraic Geometry*. American Mathematical Society. [ISBN][63] [9780821874622][67].
5. ↑ [Fulton, William][68] (1984). "10.4". *Intersection Theory*. Springer. [ISBN][63] [0-387-12176-5][69].
6. ↑

  - [Candelas, Philip][70]; de la Ossa, Xenia; Green, Paul; Parks, Linda (1991). "A pair of Calabi-Yau manifolds as an exactly soluble superconformal field theory". *Nuclear Physics B*. **359**(1): 21– 74. [doi][61]: [10.1016/0550-3213(91)90292-6][71].

### Bibliography

[[edit][72]]

- Kleiman, S.; Strømme, S. A.; Xambó, S. (1987), "Sketch of a verification of Schubert's number 5819539783680 of twisted cubics", *Space curves (Rocca di Papa, 1985)*, Lecture Notes in Math., vol. 1266, Berlin: Springer, pp. 156– 180, [doi][61]: [10.1007/BFb0078183][73], [ISBN][63] [978-3-540-18020-3][74], [MR][65] [0908713][75]
- Schubert, Hermann (1979) [1879], Kleiman, Steven L. (ed.), **[Kalkül der abzählenden Geometrie][76], Reprint of the 1879 original (in German), Berlin-New York: Springer-Verlag, [ISBN][63] [3-540-09233-1][77], [MR][65] [0555576][78]

## External links

[[edit][79]]

- Bashelor, Andrew; Ksir, Amy; Traves, Will (2008). ["Enumerative Algebraic Geometry of Conics"][80]. *Amer. Math. Monthly*. **115**(8): 701– 7. [doi][61]: [10.1080/00029890.2008.11920584][81]. [JSTOR][82] [27642583][83]. Archived from [the original][84] on 2023-12-01. Retrieved 2015-01-30.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Enumerative_geometry&oldid=1334490611][85] "

[Categories][86]:

- [Intersection theory][87]
- [Algebraic geometry][88]

Hidden categories:

- [Articles with short description][89]
- [Short description matches Wikidata][90]
- [Articles lacking in-text citations from September 2012][91]
- [All articles lacking in-text citations][92]
- [All articles with unsourced statements][93]
- [Articles with unsourced statements from September 2025][94]
- [CS1 German-language sources (de)][95]

Search

Enumerative geometry

8 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Intersection_theory
[2]: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#General_references
[3]: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources#Inline_citations
[4]: https://en.wikipedia.org/w/index.php?title=Enumerative_geometry&amp;action=edit
[5]: https://en.wikipedia.org/wiki/Wikipedia:When_to_cite
[6]: https://en.wikipedia.org/wiki/Help:Maintenance_template_removal
[7]: https://en.wikipedia.org/wiki/Mathematics
[8]: https://en.wikipedia.org/wiki/Algebraic_geometry
[9]: https://en.wikipedia.org/wiki/Wikipedia:Citation_needed
[10]: https://en.wikipedia.org/wiki/Motivic_homotopy_theory
[11]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=1
[12]: https://en.wikipedia.org/wiki/File:Apollonius8ColorMultiplyV2.svg
[13]: https://en.wikipedia.org/wiki/Problem_of_Apollonius
[14]: https://en.wikipedia.org/wiki/Hilbert_problems
[15]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=2
[16]: https://en.wikipedia.org/wiki/Dimension_counting
[17]: https://en.wikipedia.org/wiki/Bézout's_theorem
[18]: https://en.wikipedia.org/wiki/Schubert_calculus
[19]: https://en.wikipedia.org/wiki/Characteristic_class
[20]: https://en.wikipedia.org/wiki/Cohomology
[21]: https://en.wikipedia.org/wiki/Poincaré_duality
[22]: https://en.wikipedia.org/wiki/Moduli_spaces
[23]: https://en.wikipedia.org/wiki/Quantum_cohomology
[24]: https://en.wikipedia.org/wiki/Gromov–Witten_invariant
[25]: https://en.wikipedia.org/wiki/Mirror_symmetry_(string_theory)
[26]: https://en.wikipedia.org/wiki/Clemens_conjecture
[27]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=3
[28]: https://en.wikipedia.org/wiki/Hermann_Schubert
[29]: https://en.wikipedia.org/wiki/Topological
[30]: https://en.wikipedia.org/wiki/Steven_Kleiman
[31]: https://en.wikipedia.org/wiki/Intersection_number
[32]: https://en.wikipedia.org/wiki/André_Weil
[33]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=4
[34]: https://en.wikipedia.org/wiki/Fudge_factor
[35]: https://en.wikipedia.org/wiki/Conic_section
[36]: https://en.wikipedia.org/wiki/Projective_plane
[37]: https://en.wikipedia.org/wiki/Projective_space
[38]: https://en.wikipedia.org/wiki/Homogeneous_coordinates
[39]: https://en.wikipedia.org/wiki/Five_points_determine_a_conic
[40]: https://en.wikipedia.org/wiki/General_linear_position
[41]: https://en.wikipedia.org/wiki/Quadric
[42]: https://en.wikipedia.org/wiki/Linear_system_of_divisors
[43]: https://en.wikipedia.org/wiki/Base_locus
[44]: https://en.wikipedia.org/wiki/Veronese_surface
[45]: https://en.wikipedia.org/wiki/Bézout_theorem
[46]: https://en.wikipedia.org/wiki/General_position
[47]: https://en.wiktionary.org/wiki/fudge%20factor
[48]: https://en.wikipedia.org/wiki/Hilbert's_fifteenth_problem
[49]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=5
[50]: https://en.wikipedia.org/wiki/Herbert_Clemens
[51]: https://en.wikipedia.org/wiki/Rational_curve
[52]: https://en.wikipedia.org/wiki/Quintic_threefold
[53]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=6
[54]: https://en.wikipedia.org/wiki/Cubic_surface
[55]: https://en.wikipedia.org/wiki/George_Salmon
[56]: https://en.wikipedia.org/wiki/Arthur_Cayley
[57]: https://en.wikipedia.org/wiki/Steiner's_conic_problem
[58]: https://en.wikipedia.org/wiki/Michel_Chasles
[59]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=7
[60]: https://www.quantamagazine.org/new-math-revives-geometrys-oldest-problems-20250926/
[61]: https://en.wikipedia.org/wiki/Doi_(identifier)
[62]: https://doi.org/10.1090%2Fpspum%2F046.2
[63]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[64]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-8218-1480-2
[65]: https://en.wikipedia.org/wiki/MR_(identifier)
[66]: https://mathscinet.ams.org/mathscinet-getitem?mr=0927987
[67]: https://en.wikipedia.org/wiki/Special:BookSources/9780821874622
[68]: https://en.wikipedia.org/wiki/William_Fulton_(mathematician)
[69]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-12176-5
[70]: https://en.wikipedia.org/wiki/Philip_Candelas
[71]: https://doi.org/10.1016%2F0550-3213%2891%2990292-6
[72]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=8
[73]: https://doi.org/10.1007%2FBFb0078183
[74]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-18020-3
[75]: https://mathscinet.ams.org/mathscinet-getitem?mr=0908713
[76]: https://archive.org/details/kalklderabzh00schuuoft
[77]: https://en.wikipedia.org/wiki/Special:BookSources/3-540-09233-1
[78]: https://mathscinet.ams.org/mathscinet-getitem?mr=0555576
[79]: /w/index.php?title=Enumerative_geometry&amp;action=edit&amp;section=9
[80]: https://web.archive.org/web/20231201062154/https://maa.org/programs/maa-awards/writing-awards/enumerative-algebraic-geometry-of-conics
[81]: https://doi.org/10.1080%2F00029890.2008.11920584
[82]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[83]: https://www.jstor.org/stable/27642583
[84]: http://www.maa.org/programs/maa-awards/writing-awards/enumerative-algebraic-geometry-of-conics
[85]: https://en.wikipedia.org/w/index.php?title=Enumerative_geometry&amp;oldid=1334490611
[86]: /wiki/Help:Category
[87]: /wiki/Category:Intersection_theory
[88]: /wiki/Category:Algebraic_geometry
[89]: /wiki/Category:Articles_with_short_description
[90]: /wiki/Category:Short_description_matches_Wikidata
[91]: /wiki/Category:Articles_lacking_in-text_citations_from_September_2012
[92]: /wiki/Category:All_articles_lacking_in-text_citations
[93]: /wiki/Category:All_articles_with_unsourced_statements
[94]: /wiki/Category:Articles_with_unsourced_statements_from_September_2025
[95]: /wiki/Category:CS1_German-language_sources_(de)
