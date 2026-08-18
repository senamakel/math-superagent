<!-- source: https://en.wikipedia.org/wiki/Hilbert%27s_third_problem | converted from HTML -->

Hilbert's third problem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

On dissections between polyhedra

[1] Two polyhedra of equal volume, cut into two pieces which can be reassembled into either polyhedron

The third of [Hilbert's problems][2] presented in 1900 was the first to be solved. The problem asks the following:

Given any two [polyhedra][3] of equal [volume][4], is it always possible to cut the first into finitely many polyhedral pieces which can be reassembled to yield the second?

Based on earlier writings by [Carl Friedrich Gauss][5], [1] [David Hilbert][6] conjectured that this was not always possible. His student [Max Dehn][7] confirmed the conjecture with a counterexample. [2]

## History and motivation

[[edit][8]]

The formula for the volume of a [pyramid][9], one-third of the product of base area and height, had been known to [Euclid][10]. Still, all proofs of it involve some form of [limiting process][11] or [calculus][12], notably the [method of exhaustion][13] or, in more modern form, [Cavalieri's principle][14]. Similar formulas in plane geometry can be proven with more elementary means. Gauss regretted this defect in two of his letters to [Christian Ludwig Gerling][15], who proved that two symmetric tetrahedra are [equidecomposable][16]. [3]

Gauss's letters were the motivation for [David Hilbert][6]: Is it possible to prove the equality of volume using elementary "cut-and-glue" methods, for arbitrary polyhedra or for the specific cases studied by Euclid? [4] Another motivation for Hilbert dates from the [Wallace–Bolyai–Gerwien theorem][17] in the early 19th century, according to which any two [polygons][18] of equal area can be cut up into polygonal pieces and reassembled into each other. He used it as a way to axiomatize the [area][19] of two-dimensional polygons, in connection with [Hilbert's axioms][20] for [Euclidean geometry][21]. [5] He later formulated a 20th-century influential [set of 23 mathematical problems][2] in 1900 at the [International Congress of Mathematicians][22]. In his set, he addressed the third problem on the axiomatization of solid volume, whether every two polyhedra of equal volumes can always be cut into polyhedral pieces and reassembled into each other. [6] T_1 </math> and <math> T_2 </math> with equal base area and equal height, hence equal volume, is it always possible to find a finite number of tetrahedra, so that when these tetrahedra are glued in some way to <math> T_1 </math> and also glued to <math> T_2 </math>, the resulting polyhedra are scissors-congruent?\"<ref name=\"hilbert\">{{cite journal\n | last = Hilbert | first = David | author-link = David Hilbert\n | title = Mathematical Problems\n | journal = Bulletin of the American Mathematical Society\n | volume = 8 | issue = 10 | pages = 437–479\n | year = 1902\n | doi = 10.1090/S0002-9904-1902-00923-3\n | mr = 1557926\n | doi-access = free\n}} Earlier publications (in the original German) appeared in ''Göttinger Nachrichten'', 1900, pp. 253–297, and ''Archiv der Mathematik und Physik'', 3rd series, vol. 1 (1901), pp. 44-63, 213–237.</ref>"}},"i":0}}]}'> [a]

Two polyhedra are called [scissors-congruent][23] if one can be cut into finitely many polyhedral pieces that can be reassembled to form the other. Any two scissors-congruent polyhedra have the same volume. Hilbert asks about the [converse][24].

## Solution

[[edit][25]]

Main article: [Dehn invariant][26]

For every polyhedron P {\displaystyle P}[image: {\displaystyle P}], [Max Dehn][7] defines a value, now known as the [Dehn invariant][26] D ⁡ ( P) {\displaystyle \operatorname {D} (P)}[image: {\displaystyle \operatorname {D} (P)}], with the property that, if P {\displaystyle P}[image: {\displaystyle P}] is cut into polyhedral pieces P 1, P 2, … P n {\displaystyle P_{1},P_{2},\dots P_{n}}[image: {\displaystyle P_{1},P_{2},\dots P_{n}}], then D ⁡ ( P) = D ⁡ ( P 1) + D ⁡ ( P 2) + ⋯ + D ⁡ ( P n). {\displaystyle \operatorname {D} (P)=\operatorname {D} (P_{1})+\operatorname {D} (P_{2})+\cdots +\operatorname {D} (P_{n}).}[image: {\displaystyle \operatorname {D} (P)=\operatorname {D} (P_{1})+\operatorname {D} (P_{2})+\cdots +\operatorname {D} (P_{n}).}] In particular, if two polyhedra are scissors-congruent, then they have the same Dehn invariant. Dehn then shows that every cube has Dehn invariant zero while every [regular tetrahedron][27] has a non-zero Dehn invariant. Therefore, these two shapes cannot be scissors-congruent. [2] [8] This implies that not all polyhedra can be dissected into cubes, hence the answer is negative. [6]

A polyhedron's invariant is defined based on the lengths of its edges and the angles between its faces. If a polyhedron is cut into two, some edges are cut into two, and the corresponding contributions to the Dehn invariants should therefore be additive in the edge lengths. Similarly, if a polyhedron is cut along an edge, the corresponding angle is cut into two. Cutting a polyhedron typically also introduces new edges and angles; their contributions must cancel out. The angles introduced when a cut passes through a face add to π {\displaystyle \pi }[image: {\displaystyle \pi }], and the angles introduced around an edge interior to the polyhedron add to 2 π {\displaystyle 2\pi }[image: {\displaystyle 2\pi }]. Therefore, the Dehn invariant is defined in such a way that integer multiples of angles of π {\displaystyle \pi }[image: {\displaystyle \pi }] give a net contribution of zero. [9]

All of the above requirements can be met by defining D ⁡ ( P) {\displaystyle \operatorname {D} (P)}[image: {\displaystyle \operatorname {D} (P)}] as an element of the [tensor product][28] of the [real numbers][29] R {\displaystyle \mathbb {R} }[image: {\displaystyle \mathbb {R} }] (representing lengths of edges) and the [quotient space][30] R / ( Q π) {\displaystyle \mathbb {R} /(\mathbb {Q} \pi )}[image: {\displaystyle \mathbb {R} /(\mathbb {Q} \pi )}] (representing angles, with all rational multiples of π {\displaystyle \pi }[image: {\displaystyle \pi }] replaced by zero). [9] For some purposes, this definition can be made using the [tensor product of modules][31] over Z {\displaystyle \mathbb {Z} }[image: {\displaystyle \mathbb {Z} }] (or equivalently of [abelian groups][32]), while other aspects of this topic make use of a [vector space][33] structure on the invariants, obtained by considering the two factors R {\displaystyle \mathbb {R} }[image: {\displaystyle \mathbb {R} }] and R / ( Q π) {\displaystyle \mathbb {R} /(\mathbb {Q} \pi )}[image: {\displaystyle \mathbb {R} /(\mathbb {Q} \pi )}] to be vector spaces over Q {\displaystyle \mathbb {Q} }[image: {\displaystyle \mathbb {Q} }] and taking the [tensor product of vector spaces][28] over Q {\displaystyle \mathbb {Q} }[image: {\displaystyle \mathbb {Q} }]. This choice of structure in the definition does not make a difference in whether two Dehn invariants, defined in either way, are equal or unequal.

For any edge e {\displaystyle e}[image: {\displaystyle e}] of a polyhedron P {\displaystyle P}[image: {\displaystyle P}], let ℓ ( e) {\displaystyle \ell (e)}[image: {\displaystyle \ell (e)}] be its length and let θ ( e) {\displaystyle \theta (e)}[image: {\displaystyle \theta (e)}] denote the [dihedral angle][34] of the two faces of P {\displaystyle P}[image: {\displaystyle P}] that meet at e {\displaystyle e}[image: {\displaystyle e}], measured in [radians][35] and considered modulo rational multiples of π {\displaystyle \pi }[image: {\displaystyle \pi }]. The Dehn invariant is then defined as D ⁡ ( P) = ∑ e ℓ ( e) ⊗ θ ( e) {\displaystyle \operatorname {D} (P)=\sum _{e}\ell (e)\otimes \theta (e)}[image: {\displaystyle \operatorname {D} (P)=\sum _{e}\ell (e)\otimes \theta (e)}] where the sum is taken over all edges e {\displaystyle e}[image: {\displaystyle e}] of the polyhedron P {\displaystyle P}[image: {\displaystyle P}]. [9] It is a [valuation][36].

## Further information

[[edit][37]]

In light of Dehn's theorem above, one might ask "which polyhedra are scissors-congruent"? In 1965, [Jean-Pierre Sydler][38] showed that two polyhedra are scissors-congruent if and only if they have the same volume and the same Dehn invariant. [10] [Børge Jessen][39] later extended Sydler's results to four dimensions. [11] In 1990, Dupont and Sah provided a simpler proof of Sydler's result by reinterpreting it as a theorem about the [homology][40] of certain [classical groups][41]. [12]

Debrunner showed in 1980 that the Dehn invariant of any polyhedron with which all of [three-dimensional space][42] can be [tiled][43] periodically is zero. [13]

Unsolved problem in mathematics

In spherical or hyperbolic geometry, must polyhedra with the same volume and Dehn invariant be scissors-congruent?

[More unsolved problems in mathematics][44]

Jessen also posed the question of whether the analogue of Jessen's results remained true for [spherical geometry][45] and [hyperbolic geometry][46]. In these geometries, Dehn's method continues to work, and shows that when two polyhedra are scissors-congruent, their Dehn invariants are equal. However, it remains an [open problem][47] whether pairs of polyhedra with the same volume and the same Dehn invariant, in these geometries, are always scissors-congruent. [14]

Hilbert's third problem was also proposed independently by Władysław Kretkowski for a math contest in 1882 by the Academy of Arts and Sciences of [Kraków][48], and was solved by [Ludwik Antoni Birkenmajer][49] using a different method than Dehn's. Birkenmajer did not publish the result, and the original manuscript containing his solution was rediscovered years later. [3]

## See also

[[edit][50]]

- [Hill tetrahedron][51]
- [Onorato Nicoletti][52]

## Notes

[[edit][53]]

1. ↑ His original problem asked, "for two tetrahedra T 1 {\displaystyle T_{1}}[image: {\displaystyle T_{1}}] and T 2 {\displaystyle T_{2}}[image: {\displaystyle T_{2}}] with equal base area and equal height, hence equal volume, is it always possible to find a finite number of tetrahedra, so that when these tetrahedra are glued in some way to T 1 {\displaystyle T_{1}}[image: {\displaystyle T_{1}}] and also glued to T 2 {\displaystyle T_{2}}[image: {\displaystyle T_{2}}], the resulting polyhedra are scissors-congruent?" [7]

## References

[[edit][54]]

1. ↑ [Carl Friedrich Gauss][5]: *Werke*, vol. 8, pp. 241 and 244
2. 1 2 Dehn, Max (1901). ["Ueber den Rauminhalt"][55]. *[Mathematische Annalen][56]*. **55**(3): 465– 478. [doi][57]: [10.1007/BF01448001][58]. [S2CID][59] [120068465][60].
3. 1 2 Ciesielska, Danuta; Ciesielski, Krzysztof (2018-05-29). ["Equidecomposability of Polyhedra: A Solution of Hilbert's Third Problem in Kraków before ICM 1900"][61]. *The Mathematical Intelligencer*. **40**(2): 55– 63. [doi][57]: [10.1007/s00283-017-9748-4][61]. [ISSN][62] [0343-6993][63].
4. ↑ [Zeeman, E. C.][64] (July 2002). "On Hilbert's third problem". *[The Mathematical Gazette][65]*. **86**(506): 241– 247. [doi][57]: [10.2307/3621846][66]. [JSTOR][67] [3621846][68].
5. ↑ Giovannini, Eduardo N. (2021). ["David Hilbert and the foundations of the theory of plane area"][69]. *[Archive for History of Exact Sciences][70]*. **75**(6): 649– 698. [doi][57]: [10.1007/s00407-021-00278-z][69]. [MR][71] [4324749][72].
6. 1 2 Gruber, Peter M. (2007). "Chapter 16: Volume of Polytopes and Hilbert's Third Problem". *Convex and Discrete Geometry*. Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Vol. 336. Springer, Berlin. pp. 280– 291. [doi][57]: [10.1007/978-3-540-71133-9][73]. [ISBN][74] [978-3-540-71132-2][75]. [MR][71] [2335496][76]..
7. ↑ [Hilbert, David][6] (1902). ["Mathematical Problems"][77]. *Bulletin of the American Mathematical Society*. **8**(10): 437– 479. [doi][57]: [10.1090/S0002-9904-1902-00923-3][77]. [MR][71] [1557926][78]. Earlier publications (in the original German) appeared in *Göttinger Nachrichten*, 1900, pp. 253–297, and *Archiv der Mathematik und Physik*, 3rd series, vol. 1 (1901), pp. 44-63, 213–237.
8. ↑ [Zeeman, E. C.][64] (July 2002). "On Hilbert's third problem". *[The Mathematical Gazette][65]*. **86**(506): 241– 247. [doi][57]: [10.2307/3621846][66]. [JSTOR][67] [3621846][68]..
9. 1 2 3 [Hazewinkel, M.][79] (2001) [1994], ["Dehn invariant"][80], *[Encyclopedia of Mathematics][81]*, EMS Press
10. ↑ Sydler, J.-P. (1965). "Conditions nécessaires et suffisantes pour l'équivalence des polyèdres de l'espace euclidien à trois dimensions". *[Comment. Math. Helv.][82]***40**: 43– 80. [doi][57]: [10.1007/bf02564364][83]. [S2CID][59] [123317371][84].
11. ↑ Jessen, Børge (1972). "Zur Algebra der Polytope". *Nachrichten der Akademie der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse, Fachgruppe II: Nachrichten aus der Physik, Astronomie, Geophysik, Technik*: 47– 53. [MR][71] [0353150][85]. [Zbl][86] [0262.52004][87].
12. ↑ Dupont, Johan; Sah, Chih-Han (1990). ["Homology of Euclidean groups of motions made discrete and Euclidean scissors congruences"][88]. *[Acta Math.][89]***164**( 1– 2): 1– 27. [doi][57]: [10.1007/BF02392750][88].
13. ↑ Debrunner, Hans E. (1980). "Über Zerlegungsgleichheit von Pflasterpolyedern mit Würfeln". *[Arch. Math.][90]***35**(6): 583– 587. [doi][57]: [10.1007/BF01235384][91]. [S2CID][59] [121301319][92].
14. ↑ Dupont, Johan L. (2001). **[Scissors congruences, group homology and characteristic classes][93]. Nankai Tracts in Mathematics. Vol. 1. World Scientific Publishing Co., Inc., River Edge, NJ. p. 6. [doi][57]: [10.1142/9789812810335][94]. [ISBN][74] [978-981-02-4507-8][95]. [MR][71] [1832859][96]. Archived from [the original][97] on 2016-04-29..

## Further reading

[[edit][98]]

- Benko, D. (2007). "A New Approach to Hilbert's Third Problem". *[The American Mathematical Monthly][99]*. **114**(8): 665– 676. [doi][57]: [10.1080/00029890.2007.11920458][100]. [S2CID][59] [7213930][101].
- Schwartz, Rich (2010). ["The Dehn–Sydler Theorem Explained"][102] (PDF).
- Koji, Shiga; [Toshikazu Sunada][103] (2005). *A Mathematical Gift, III: The Interplay Between Topology, Functions, Geometry, and Algebra*. American Mathematical Society.

## External links

[[edit][104]]

- [Proof of Dehn's Theorem at Everything2][105]
- [Weisstein, Eric W.][106] ["Dehn Invariant"][107]. *[MathWorld][108]*.
- [Dehn Invariant at Everything2][109]
- Hazewinkel, M. (2001) [1994], ["Dehn invariant"][110], *[Encyclopedia of Mathematics][81]*, EMS Press

- [v][111]
- [t][112]
- [e][113]

[Hilbert's problems][2]

 |

- [1][114]
- [2][115]
- [3][116]
- [4][117]
- [5][118]
- [6][119]
- [7][120]
- [8][121]
- [9][122]
- [10][123]
- [11][124]
- [12][125]
- [13][126]
- [14][127]
- [15][128]
- [16][129]
- [17][130]
- [18][131]
- [19][132]
- [20][133]
- [21][134]
- [22][135]
- [23][136]
- ( [24][137])

 |

[Authority control databases][138][image: Edit this at Wikidata] [139] |

- [GND][140]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Hilbert%27s_third_problem&oldid=1334861812][141] "

[Categories][142]:

- [Hilbert's problems][143]
- [Euclidean solid geometry][144]
- [Geometric dissection][145]
- [Geometry problems][146]

Hidden categories:

- [Articles with short description][147]
- [Short description is different from Wikidata][148]

Search

Hilbert's third problem

13 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Cube_and_prism_from_two_bricks.svg
[2]: https://en.wikipedia.org/wiki/Hilbert's_problems
[3]: https://en.wikipedia.org/wiki/Polyhedron
[4]: https://en.wikipedia.org/wiki/Volume
[5]: https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss
[6]: https://en.wikipedia.org/wiki/David_Hilbert
[7]: https://en.wikipedia.org/wiki/Max_Dehn
[8]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=1
[9]: https://en.wikipedia.org/wiki/Pyramid_(geometry)
[10]: https://en.wikipedia.org/wiki/Euclid
[11]: https://en.wikipedia.org/wiki/Limit_of_a_sequence
[12]: https://en.wikipedia.org/wiki/Calculus
[13]: https://en.wikipedia.org/wiki/Method_of_exhaustion
[14]: https://en.wikipedia.org/wiki/Cavalieri's_principle
[15]: https://en.wikipedia.org/wiki/Christian_Ludwig_Gerling
[16]: https://en.wikipedia.org/wiki/Equidecomposable
[17]: https://en.wikipedia.org/wiki/Wallace–Bolyai–Gerwien_theorem
[18]: https://en.wikipedia.org/wiki/Polygon
[19]: https://en.wikipedia.org/wiki/Area
[20]: https://en.wikipedia.org/wiki/Hilbert's_axioms
[21]: https://en.wikipedia.org/wiki/Euclidean_geometry
[22]: https://en.wikipedia.org/wiki/International_Congress_of_Mathematicians
[23]: https://en.wikipedia.org/wiki/Scissors-congruent
[24]: https://en.wikipedia.org/wiki/Converse_(logic)
[25]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=2
[26]: https://en.wikipedia.org/wiki/Dehn_invariant
[27]: https://en.wikipedia.org/wiki/Regular_tetrahedron
[28]: https://en.wikipedia.org/wiki/Tensor_product
[29]: https://en.wikipedia.org/wiki/Real_number
[30]: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
[31]: https://en.wikipedia.org/wiki/Tensor_product_of_modules
[32]: https://en.wikipedia.org/wiki/Abelian_group
[33]: https://en.wikipedia.org/wiki/Vector_space
[34]: https://en.wikipedia.org/wiki/Dihedral_angle
[35]: https://en.wikipedia.org/wiki/Radian
[36]: https://en.wikipedia.org/wiki/Valuation_(geometry)
[37]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=3
[38]: https://en.wikipedia.org/wiki/Jean-Pierre_Sydler
[39]: https://en.wikipedia.org/wiki/Børge_Jessen
[40]: https://en.wikipedia.org/wiki/Homology_(mathematics)
[41]: https://en.wikipedia.org/wiki/Classical_group
[42]: https://en.wikipedia.org/wiki/Three-dimensional_space
[43]: https://en.wikipedia.org/wiki/Honeycomb_(geometry)
[44]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[45]: https://en.wikipedia.org/wiki/Spherical_geometry
[46]: https://en.wikipedia.org/wiki/Hyperbolic_geometry
[47]: https://en.wikipedia.org/wiki/Open_problem
[48]: https://en.wikipedia.org/wiki/Kraków
[49]: https://en.wikipedia.org/wiki/Ludwik_Birkenmajer
[50]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=4
[51]: https://en.wikipedia.org/wiki/Hill_tetrahedron
[52]: https://en.wikipedia.org/wiki/Onorato_Nicoletti
[53]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=5
[54]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=6
[55]: https://zenodo.org/record/2327856
[56]: https://en.wikipedia.org/wiki/Mathematische_Annalen
[57]: https://en.wikipedia.org/wiki/Doi_(identifier)
[58]: https://doi.org/10.1007%2FBF01448001
[59]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[60]: https://api.semanticscholar.org/CorpusID:120068465
[61]: https://doi.org/10.1007%2Fs00283-017-9748-4
[62]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[63]: https://search.worldcat.org/issn/0343-6993
[64]: https://en.wikipedia.org/wiki/Christopher_Zeeman
[65]: https://en.wikipedia.org/wiki/The_Mathematical_Gazette
[66]: https://doi.org/10.2307%2F3621846
[67]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[68]: https://www.jstor.org/stable/3621846
[69]: https://doi.org/10.1007%2Fs00407-021-00278-z
[70]: https://en.wikipedia.org/wiki/Archive_for_History_of_Exact_Sciences
[71]: https://en.wikipedia.org/wiki/MR_(identifier)
[72]: https://mathscinet.ams.org/mathscinet-getitem?mr=4324749
[73]: https://doi.org/10.1007%2F978-3-540-71133-9
[74]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[75]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-71132-2
[76]: https://mathscinet.ams.org/mathscinet-getitem?mr=2335496
[77]: https://doi.org/10.1090%2FS0002-9904-1902-00923-3
[78]: https://mathscinet.ams.org/mathscinet-getitem?mr=1557926
[79]: https://en.wikipedia.org/wiki/Michiel_Hazewinkel
[80]: https://www.encyclopediaofmath.org/index.php?title=Dehn_invariant
[81]: https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics
[82]: https://en.wikipedia.org/wiki/Commentarii_Mathematici_Helvetici
[83]: https://doi.org/10.1007%2Fbf02564364
[84]: https://api.semanticscholar.org/CorpusID:123317371
[85]: https://mathscinet.ams.org/mathscinet-getitem?mr=0353150
[86]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[87]: https://zbmath.org/?format=complete&amp;q=an:0262.52004
[88]: https://doi.org/10.1007%2FBF02392750
[89]: https://en.wikipedia.org/wiki/Acta_Mathematica
[90]: https://en.wikipedia.org/wiki/Archiv_der_Mathematik
[91]: https://doi.org/10.1007%2FBF01235384
[92]: https://api.semanticscholar.org/CorpusID:121301319
[93]: https://web.archive.org/web/20160429152252/http://home.math.au.dk/dupont/scissors.ps
[94]: https://doi.org/10.1142%2F9789812810335
[95]: https://en.wikipedia.org/wiki/Special:BookSources/978-981-02-4507-8
[96]: https://mathscinet.ams.org/mathscinet-getitem?mr=1832859
[97]: http://home.math.au.dk/dupont/scissors.ps
[98]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=7
[99]: https://en.wikipedia.org/wiki/The_American_Mathematical_Monthly
[100]: https://doi.org/10.1080%2F00029890.2007.11920458
[101]: https://api.semanticscholar.org/CorpusID:7213930
[102]: https://www.math.brown.edu/~res/Papers/dehn_sydler.pdf
[103]: https://en.wikipedia.org/wiki/Toshikazu_Sunada
[104]: /w/index.php?title=Hilbert%27s_third_problem&amp;action=edit&amp;section=8
[105]: http://everything2.com/e2node/Proof%2520for%2520Hilbert%2527s%2520third%2520problem
[106]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[107]: https://mathworld.wolfram.com/DehnInvariant.html
[108]: https://en.wikipedia.org/wiki/MathWorld
[109]: http://everything2.com/e2node/Dehn%2520invariant
[110]: https://www.encyclopediaofmath.org/index.php?title=Dehn_invariant&amp;oldid=13481
[111]: https://en.wikipedia.org/wiki/Template:Hilbert's_problems
[112]: https://en.wikipedia.org/wiki/Template_talk:Hilbert's_problems
[113]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Hilbert's_problems
[114]: https://en.wikipedia.org/wiki/Hilbert's_first_problem
[115]: https://en.wikipedia.org/wiki/Hilbert's_second_problem
[116]: https://en.wikipedia.org/wiki/Hilbert's_third_problem
[117]: https://en.wikipedia.org/wiki/Hilbert's_fourth_problem
[118]: https://en.wikipedia.org/wiki/Hilbert's_fifth_problem
[119]: https://en.wikipedia.org/wiki/Hilbert's_sixth_problem
[120]: https://en.wikipedia.org/wiki/Hilbert's_seventh_problem
[121]: https://en.wikipedia.org/wiki/Hilbert's_eighth_problem
[122]: https://en.wikipedia.org/wiki/Hilbert's_ninth_problem
[123]: https://en.wikipedia.org/wiki/Hilbert's_tenth_problem
[124]: https://en.wikipedia.org/wiki/Hilbert's_eleventh_problem
[125]: https://en.wikipedia.org/wiki/Hilbert's_twelfth_problem
[126]: https://en.wikipedia.org/wiki/Hilbert's_thirteenth_problem
[127]: https://en.wikipedia.org/wiki/Hilbert's_fourteenth_problem
[128]: https://en.wikipedia.org/wiki/Hilbert's_fifteenth_problem
[129]: https://en.wikipedia.org/wiki/Hilbert's_sixteenth_problem
[130]: https://en.wikipedia.org/wiki/Hilbert's_seventeenth_problem
[131]: https://en.wikipedia.org/wiki/Hilbert's_eighteenth_problem
[132]: https://en.wikipedia.org/wiki/Hilbert's_nineteenth_problem
[133]: https://en.wikipedia.org/wiki/Hilbert's_twentieth_problem
[134]: https://en.wikipedia.org/wiki/Hilbert's_twenty-first_problem
[135]: https://en.wikipedia.org/wiki/Hilbert's_twenty-second_problem
[136]: https://en.wikipedia.org/wiki/Hilbert's_twenty-third_problem
[137]: https://en.wikipedia.org/wiki/Hilbert's_twenty-fourth_problem
[138]: https://en.wikipedia.org/wiki/Help:Authority_control
[139]: https://www.wikidata.org/wiki/Q2667025#identifiers
[140]: https://d-nb.info/gnd/4159863-5
[141]: https://en.wikipedia.org/w/index.php?title=Hilbert%27s_third_problem&amp;oldid=1334861812
[142]: /wiki/Help:Category
[143]: /wiki/Category:Hilbert%27s_problems
[144]: /wiki/Category:Euclidean_solid_geometry
[145]: /wiki/Category:Geometric_dissection
[146]: /wiki/Category:Geometry_problems
[147]: /wiki/Category:Articles_with_short_description
[148]: /wiki/Category:Short_description_is_different_from_Wikidata
