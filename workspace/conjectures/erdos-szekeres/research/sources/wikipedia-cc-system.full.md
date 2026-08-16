<!-- source: https://en.wikipedia.org/wiki/CC_system | converted from HTML -->

CC system - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Ternary relation on points in the plane

In [computational geometry][1], a **CC system**or **counterclockwise system**is a [ternary relation][2]*pqr*introduced by [Donald Knuth][3] to model the clockwise ordering of triples of points in [general position][4] in the [Euclidean plane][5]. [1]

## Axioms

[[edit][6]]

A CC system is required to satisfy the following axioms, for all distinct points *p*, *q*, *r*, *s*, and *t*: [2]

1. Cyclic symmetry: If *pqr*then *qrp*.
2. Antisymmetry: If *pqr*then not *prq*.
3. Nondegeneracy: Either *pqr*or *prq*.
4. Interiority: If *tqr*and *ptr*and *pqt*, then *pqr*.
5. Transitivity: If *tsp*and *tsq*and *tsr*, and *tpq*and *tqr*, then *tpr*.

Triples of points that are not distinct are not considered as part of the relation.

## Construction from planar point sets

[[edit][7]]

A CC system may be defined from any set of points in the [Euclidean plane][5], with no three of the points collinear, by including in the relation a triple *pqr*of distinct points whenever the triple lists these three points in counterclockwise order around the triangle that they form. Using the [Cartesian coordinates][8] of the points, the triple *pqr*is included in the relation exactly when [3]

0."}}'> 0.}"> det ( x p y p 1 x q y q 1 x r y r 1) > 0. {\displaystyle \det \left({\begin{array}{ccc}x_{p}&y_{p}&1\\x_{q}&y_{q}&1\\x_{r}&y_{r}&1\end{array}}\right)>0.} 0.}"/>

The condition that the points are in general position is equivalent to the requirement that this matrix [determinant][9] is never zero for distinct points *p*, *q*, and *r*.

However, not every CC system comes from a Euclidean point set in this way. [4]

## Equivalent notions

[[edit][10]]

CC systems can also be defined from [pseudoline arrangements][11], or from [sorting networks][12] in which the compare-exchange operations only compare adjacent pairs of elements (as in for instance [bubble sort][13]), and every CC system can be defined in this way. [5] This relation is not one-to-one, but the numbers of nonisomorphic CC systems on *n*points, of pseudoline arrangements with *n*lines, and of sorting networks on *n*values, are within polynomial factors of each other. [6]

There exists a two-to-one correspondence between CC systems and uniform acyclic [oriented matroids][14] of [rank][15] 3. [7] These matroids in turn have a 1-1 correspondence to topological equivalence classes of pseudoline arrangements with one marked cell. [6]

## Algorithmic applications

[[edit][16]]

The information given by a CC system is sufficient to define a notion of a [convex hull][17] within a CC system. The convex hull is the set of ordered pairs *pq*of distinct points with the property that, for every third distinct point *r*, *pqr*belongs to the system. It forms a cycle, with the property that every three points of the cycle, in the same cyclic order, belong to the system. [8] By adding points one at a time to a CC system, and maintaining the convex hull of the points added so far in its cyclic order using a [binary search tree][18], it is possible to construct the convex hull in time *O*(*n*log*n*), matching the known time bounds for [convex hull algorithms][19] for Euclidean points. [9]

It is also possible to find a single convex hull vertex, as well as the combinatorial equivalent of a bisecting line through a system of points, from a CC system in [linear time][20]. The construction of an extreme vertex allows the [Graham scan][21] algorithm for convex hulls to be generalized from point sets to CC systems, with a number of queries to the CC system that matches (to within lower-order terms) the number of comparisons needed in [comparison sorting][22]. [10]

## Combinatorial enumeration

[[edit][23]]

The number of non-isomorphic CC systems on *n*points is [6] [11]

1, 1, 1, 2, 3, 20, 242, 6405, 316835, 28627261 ... (sequence [A006246][24] in the [OEIS][25])

These numbers grow exponentially in *n*2; [12] in contrast, the number of realizable CC systems grows exponentially only in Θ(*n*log*n*). [7]

More precisely, the number *C n*of non-isomorphic CC systems on *n*points is at most [13]

3 ( n 2). {\displaystyle 3^{\binom {n}{2}}.}[image: {\displaystyle 3^{\binom {n}{2}}.}]

Knuth conjectures more strongly that these numbers obey the recursive inequality

C n ≤ n 2 n − 2 C n − 1. {\displaystyle C_{n}\leq n2^{n-2}C_{n-1}.}[image: {\displaystyle C_{n}\leq n2^{n-2}C_{n-1}.}]

## Notes

[[edit][26]]

1. ↑ Knuth (1992).
2. ↑ Knuth (1992), p. 4.
3. ↑ Knuth (1992), p. 3.
4. ↑ Knuth (1992), pp. 25–26.
5. ↑ Knuth (1992), pp. 29–35.
6. 1 2 3 Knuth (1992), p. 35.
7. 1 2 Knuth (1992), p. 40.
8. ↑ Knuth (1992), pp. 45–46.
9. ↑ Knuth (1992), p. 47.
10. ↑ Aichholzer, Miltzow & Pilz (2013).
11. ↑ Beygelzimer & Radziszowski (2002).
12. ↑ Knuth (1992), p. 37.
13. ↑ Knuth (1992), p. 39.

## References

[[edit][27]]

- Aichholzer, Oswin; Miltzow, Tillmann; Pilz, Alexander (2013), "Extreme point and halving edge search in abstract order types", *Computational Geometry*, **46**(8): 970– 978, [doi][28]: [10.1016/j.comgeo.2013.05.001][29], [MR][30] [3061458][31], [PMC][32] [3688538][33], [PMID][34] [24092953][35].
- Beygelzimer, Alina; Radziszowski, Stanisław (2002), "On halving line arrangements", *Discrete Mathematics*, **257**( 2– 3): 267– 283, [doi][28]: [10.1016/S0012-365X(02)00430-2][36], [MR][30] [1935728][37].
- [Knuth, Donald E.][3] (1992), **[Axioms and hulls][38], Lecture Notes in Computer Science, vol. 606, Heidelberg: Springer-Verlag, pp. ix+109, [doi][28]: [10.1007/3-540-55611-7][39], [ISBN][40] [3-540-55611-7][41], [MR][30] [1226891][42], [S2CID][43] [5452191][44], archived from [the original][45] on 20 June 2017, retrieved 5 May 2011.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=CC_system&oldid=1183439166][46] "

[Categories][47]:

- [Computational geometry][48]
- [Oriented matroids][49]
- [Euclidean plane geometry][50]

Hidden categories:

- [Articles with short description][51]
- [Short description matches Wikidata][52]

Search

CC system

Add languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Computational_geometry
[2]: https://en.wikipedia.org/wiki/Ternary_relation
[3]: https://en.wikipedia.org/wiki/Donald_Knuth
[4]: https://en.wikipedia.org/wiki/General_position
[5]: https://en.wikipedia.org/wiki/Euclidean_plane
[6]: /w/index.php?title=CC_system&amp;action=edit&amp;section=1
[7]: /w/index.php?title=CC_system&amp;action=edit&amp;section=2
[8]: https://en.wikipedia.org/wiki/Cartesian_coordinate
[9]: https://en.wikipedia.org/wiki/Determinant
[10]: /w/index.php?title=CC_system&amp;action=edit&amp;section=3
[11]: https://en.wikipedia.org/wiki/Arrangement_of_lines
[12]: https://en.wikipedia.org/wiki/Sorting_network
[13]: https://en.wikipedia.org/wiki/Bubble_sort
[14]: https://en.wikipedia.org/wiki/Oriented_matroid
[15]: https://en.wikipedia.org/wiki/Matroid_rank
[16]: /w/index.php?title=CC_system&amp;action=edit&amp;section=4
[17]: https://en.wikipedia.org/wiki/Convex_hull
[18]: https://en.wikipedia.org/wiki/Binary_search_tree
[19]: https://en.wikipedia.org/wiki/Convex_hull_algorithms
[20]: https://en.wikipedia.org/wiki/Linear_time
[21]: https://en.wikipedia.org/wiki/Graham_scan
[22]: https://en.wikipedia.org/wiki/Comparison_sort
[23]: /w/index.php?title=CC_system&amp;action=edit&amp;section=5
[24]: //oeis.org/A006246
[25]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[26]: /w/index.php?title=CC_system&amp;action=edit&amp;section=6
[27]: /w/index.php?title=CC_system&amp;action=edit&amp;section=7
[28]: https://en.wikipedia.org/wiki/Doi_(identifier)
[29]: https://doi.org/10.1016%2Fj.comgeo.2013.05.001
[30]: https://en.wikipedia.org/wiki/MR_(identifier)
[31]: https://mathscinet.ams.org/mathscinet-getitem?mr=3061458
[32]: https://en.wikipedia.org/wiki/PMC_(identifier)
[33]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3688538
[34]: https://en.wikipedia.org/wiki/PMID_(identifier)
[35]: https://pubmed.ncbi.nlm.nih.gov/24092953
[36]: https://doi.org/10.1016%2FS0012-365X%2802%2900430-2
[37]: https://mathscinet.ams.org/mathscinet-getitem?mr=1935728
[38]: https://web.archive.org/web/20170620062425/http://www-cs-faculty.stanford.edu/~uno/aah.html
[39]: https://doi.org/10.1007%2F3-540-55611-7
[40]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[41]: https://en.wikipedia.org/wiki/Special:BookSources/3-540-55611-7
[42]: https://mathscinet.ams.org/mathscinet-getitem?mr=1226891
[43]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[44]: https://api.semanticscholar.org/CorpusID:5452191
[45]: http://www-cs-faculty.stanford.edu/~uno/aah.html
[46]: https://en.wikipedia.org/w/index.php?title=CC_system&amp;oldid=1183439166
[47]: /wiki/Help:Category
[48]: /wiki/Category:Computational_geometry
[49]: /wiki/Category:Oriented_matroids
[50]: /wiki/Category:Euclidean_plane_geometry
[51]: /wiki/Category:Articles_with_short_description
[52]: /wiki/Category:Short_description_matches_Wikidata
