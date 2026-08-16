<!-- source: https://en.wikipedia.org/wiki/Happy_ending_problem | converted from HTML -->

Happy ending problem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Five coplanar points have a subset forming a convex quadrilateral

For the Fred Frith album, see [The Happy End Problem][1].

"Erdős–Szekeres conjecture" redirects here. For their theorem on monotonic subsequences, see [Erdős–Szekeres theorem][2].

[3] The happy ending problem: every set of five points in general position contains the vertices of a convex quadrilateral

In [mathematics][4], the "**happy ending problem**" (so named by [Paul Erdős][5] because it led to the marriage of mathematicians [George Szekeres][6] and [Esther Klein][7]) [1] [2] [3] is the following statement:

In this context, general position means that no two points coincide and no three points are collinear.</ref> has a subset of four points that form the [[Vertex (graph theory)|vertices]] of a [[convex polygon|convex]] [[quadrilateral]]."}},"i":0}}]}'>

**Theorem**— any set of five points in the plane in [general position][8] [4] has a subset of four points that form the [vertices][9] of a [convex][10] [quadrilateral][11].

This was one of the original results that led to the development of [Ramsey theory][12].

The happy ending theorem can be proven by a simple case analysis: if four or more points are vertices of the [convex hull][13], any four such points can be chosen. If on the other hand, the convex hull has the form of a [triangle][14] with two points inside it, the two inner points and one of the triangle sides can be chosen. See Peterson (2000) for an illustrated explanation of this proof, and Morris & Soltan (2000) for a more detailed survey of the problem.

The **Erdős–Szekeres conjecture**states precisely a more general relationship between the number of points in a general-position point set and its largest subset forming a convex [polygon][15], namely that the smallest number of points for which any general position arrangement contains a convex subset of n {\displaystyle n}[image: {\displaystyle n}] points is 2 n − 2 + 1 {\displaystyle 2^{n-2}+1}[image: {\displaystyle 2^{n-2}+1}]. It remains unproven, but less precise bounds are known.

## Larger polygons

[[edit][16]]

[17] A set of eight points in general position with no convex pentagon

Erdős & Szekeres (1935) proved the following generalisation:

**Theorem**— for any positive [integer][18] N, any sufficiently large finite set of points in the plane in general position has a subset of N points that form the vertices of a convex polygon.

The proof appeared in the same paper that proves the [Erdős–Szekeres theorem][2] on monotonic subsequences in sequences of numbers.

Let *f*(*N*) denote the minimum M for which any set of M points in general position must contain a convex *N*-gon. It is known that

- *f*(3) = 3, trivially.
- *f*(4) = 5. [5]
- *f*(5) = 9. [6] A set of eight points with no convex [pentagon][19] is shown in the illustration, demonstrating that 8"}},"i":0}}]}'>*f*(5) > 8; the more difficult part of the proof is to show that every set of nine points in general position contains the vertices of a convex pentagon.
- *f*(6) = 17. [7]
- The value of *f*(*N*) is unknown for all 6"}},"i":0}}]}'>*N*> 6. By the result of Erdős & Szekeres (1935), *f*(*N*) is known to be finite for all finite *N*.

On the basis of the known values of *f*(*N*) for *N*= 3, 4 and 5, Erdős and Szekeres [conjectured][20] in their original paper that

[image: A set of sixteen points in general position with no convex hexagon] [21] A set of sixteen points in general position with no convex hexagon

f ( N) = 1 + 2 N − 2 for all N ≥ 3. {\displaystyle f(N)=1+2^{N-2}\quad {\text{for all }}N\geq 3.}[image: {\displaystyle f(N)=1+2^{N-2}\quad {\text{for all }}N\geq 3.}] They proved later, by constructing explicit examples, that [8] f ( N) ≥ 1 + 2 N − 2. {\displaystyle f(N)\geq 1+2^{N-2}.}[image: {\displaystyle f(N)\geq 1+2^{N-2}.}] In 2016 Andrew Suk [9] showed that for *N*≥ 7 f ( N) ≤ 2 N + o ( N). {\displaystyle f(N)\leq 2^{N+o(N)}.}[image: {\displaystyle f(N)\leq 2^{N+o(N)}.}]

Suk actually proves, for N sufficiently large, f ( N) ≤ 2 N + 6 N 2 / 3 log ⁡ N. {\displaystyle f(N)\leq 2^{N+6N^{2/3}\log N}.}[image: {\displaystyle f(N)\leq 2^{N+6N^{2/3}\log N}.}]

This was subsequently improved to: [10]

f ( N) ≤ 2 N + O ( N log ⁡ N). {\displaystyle f(N)\leq 2^{N+O({\sqrt {N\log N}})}.}[image: {\displaystyle f(N)\leq 2^{N+O({\sqrt {N\log N}})}.}]

## Empty convex polygons

[[edit][22]]

There is also the question of whether any sufficiently large set of points in general position has an "empty" convex quadrilateral, pentagon, etc., that is, one that contains no other input point. The original solution to the happy ending problem can be adapted to show that any five points in general position have an empty convex quadrilateral, as shown in the illustration, and any ten points in general position have an empty convex pentagon. [11] However, there exist arbitrarily large sets of points in general position that contain no empty convex [heptagon][23]. [12]

Let N {\displaystyle N}[image: {\displaystyle N}] be the minimum number of points, such that any N {\displaystyle N}[image: {\displaystyle N}] points in general position contains an empty hexagon. For a long time it is open whether N {\displaystyle N}[image: {\displaystyle N}] exists. The question is now solved:

- Overmars (2003) showed that if it exists, then N ≥ 30 {\displaystyle N\geq 30}[image: {\displaystyle N\geq 30}], by constructing an example with 29 points.
- Nicolás (2007) showed that N ≤ f ( 25) {\displaystyle N\leq f(25)}[image: {\displaystyle N\leq f(25)}].
- Gerken (2008) showed that N ≤ f ( 9) {\displaystyle N\leq f(9)}[image: {\displaystyle N\leq f(9)}].
- Valtr (2008) made a simpler but looser version of Gerken (2008), to show that N ≤ f ( 15) {\displaystyle N\leq f(15)}[image: {\displaystyle N\leq f(15)}].
- Heule & Scheucher (2024) showed, by using a [SAT solving][24] approach, that N = 30 {\displaystyle N=30}[image: {\displaystyle N=30}].

## Related problems

[[edit][25]]

The problem of finding sets of *n*points minimizing the number of convex quadrilaterals is equivalent to minimizing the [crossing number][26] in a straight-line [drawing][27] of a [complete graph][28]. The number of quadrilaterals must be proportional to the fourth power of *n*, but the precise constant is not known. [13]

It is straightforward to show that, in higher-dimensional [Euclidean spaces][29], sufficiently large sets of points will have a subset of *k*points that forms the vertices of a [convex polytope][30], for any *k*greater than the dimension: this follows immediately from existence of convex *k*-gons in sufficiently large planar point sets, by projecting the higher-dimensional point set into an arbitrary two-dimensional subspace. However, the number of points necessary to find *k*points in [convex position][31] may be smaller in higher dimensions than it is in the plane, and it is possible to find subsets that are more highly constrained. In particular, in *d*dimensions, every *d*+ 3 points in general position have a subset of *d*+ 2 points that form the vertices of a [cyclic polytope][32]. [14] More generally, for every *d*and *k*>*d*there exists a number *m*(*d*, *k*) such that every set of *m*(*d*, *k*) points in general position has a subset of *k*points that form the vertices of a [neighborly polytope][33]. [15]

## "Happy ending"

[[edit][34]]

According to [George Szekeres][6], who discussed the problem with his future wife [Esther Klein][7] early in their relationship, "it was Paul Erdös who called it the 'Happy Ending'". They became friends in 1933 and married in 1937, and Szekeres says the reason they got married was not entirely because of their work on the problem. [16]

## Notes

[[edit][35]]

1. ↑ [A world of teaching and numbers - times two][36], [Michael Cowling][37], [The Sydney Morning Herald][38], 2005-11-07, cited 2014-09-04
2. ↑ Hartnett, Kevin (2017-05-30). ["A Puzzle of Clever Connections Nears a Happy End"][39]. *Quanta Magazine*. Retrieved 2026-07-13.
3. ↑ Hoffman, Paul (1998). *The man who loved only numbers: the story of Paul Erdos and the search for mathematical truth*. New York: Hyperion. p. 76. [ISBN][40] [978-0-7868-6362-4][41].
4. ↑ In this context, general position means that no two points coincide and no three points are collinear.
5. ↑ This was the original problem, proved by Esther Klein.
6. ↑ According to Erdős & Szekeres (1935), this was first proved by Endre Makai (1915–1987);(see ["The Hidden Order: A Painting"][42]. *www.sfu.ca*. Retrieved 2026-02-09., **[Fizikusok és matematikusok az Eötvös Collegiumban 1895–1950][43] (PDF) (in Hungarian). pp. 231– 232.) the first published proof appeared in Kalbfleisch, Kalbfleisch & Stanton (1970).
7. ↑ This has been proved by Szekeres & Peters (2006). They carried out a computer search which eliminated all possible configurations of 17 points without convex hexagons while examining only a tiny fraction of all configurations.
8. ↑ Erdős & Szekeres (1961)
9. ↑ Suk (2016). See [binomial coefficient][44] and [big O notation][45] for notation used here and [Catalan numbers][46] or [Stirling's approximation][47] for the asymptotic expansion.
10. ↑ Holmsen et al. (2020).
11. ↑ Harborth (1978).
12. ↑ Horton (1983)
13. ↑ Scheinerman & Wilf (1994)
14. ↑ Grünbaum (2003), Ex. 6.5.6, p.120. Grünbaum attributes this result to a private communication of Micha A. Perles.
15. ↑ Grünbaum (2003), Ex. 7.3.6, p. 126. This result follows by applying a Ramsey-theoretic argument similar to Szekeres's original proof together with Perles's result on the case *k*=*d*+ 2.
16. ↑ ["Professor George Szekeres (1911-2005), mathematician | Australian Academy of Science"][48]. *science.org.au*. Retrieved 2026-07-13.

## References

[[edit][49]]

- [Chung, F.R.K.][50]; [Graham, R.L.][51] (1998), "Forced convex n-gons in the plane", *[Discrete and Computational Geometry][52]*, **19**(3): 367– 371, [doi][53]: [10.1007/PL00009353][54]
- [Erdős, P.][5]; [Szekeres, G.][6] (1935), ["A combinatorial problem in geometry"][55], *[Compositio Mathematica][56]*, **2**: 463– 470 reprinted in Gessel, Ira; Rota, Gian-Carlo (1987). Gessel, Ira; Rota, Gian-Carlo (eds.). *Classic Papers in Combinatorics*. Boston, MA: Birkhäuser Boston Inc. pp. 49– 56.
- [Erdős, P.][5]; [Szekeres, G.][6] (1961), "On some extremum problems in elementary geometry", *Ann. Univ. Sci. Budapest. Eötvös Sect. Math.*, **3– 4**: 53– 62; reprinted in [Erdős, P.][5] (1973), Spencer, J. (ed.), *The Art of Counting: Selected Writings*, Cambridge, MA: MIT Press, pp. 680– 689
- Gerken, Tobias (2008), "Empty convex hexagons in planar point sets", *[Discrete and Computational Geometry][52]*, **39**( 1– 3): 239– 272, [doi][53]: [10.1007/s00454-007-9018-x][57]
- [Grünbaum, Branko][58] (2003), Kaibel, Volker; [Klee, Victor][59]; [Ziegler, Günter M.][60] (eds.), **[Convex Polytopes][61], Graduate Texts in Mathematics, vol. 221 (2nd ed.), [Springer-Verlag][62], [ISBN][40] [0-387-00424-6][63]
- Harborth, Heiko (1978), "Konvexe Fünfecke in ebenen Punktmengen", *[Elemente der Mathematik][64]*, **33**(5): 116– 118
- Heule, Marijn J. H.; Scheucher, Manfred (2024), "Happy Ending: An Empty Hexagon in Every Set of 30 Points", in Finkbeiner, Bernd; Kovács, Laura (eds.), *Tools and Algorithms for the Construction and Analysis of Systems*, Lecture Notes in Computer Science, vol. 14570, Springer-Verlag, pp. 61– 80, [arXiv][65]: [2403.00737][66], [doi][53]: [10.1007/978-3-031-57246-3_5][67], [ISBN][40] [978-3-031-57245-6][68]
- Holmsen, Andreas F.; Mojarrad, Hossein Nassajian; [Pach, János][69]; Tardos, Gábor (2020), "Two extensions of the Erdős–Szekeres problem", *Journal of the European Mathematical Society*, **22**(12): 3981– 3995, [arXiv][65]: [1710.11415][70], [doi][53]: [10.4171/jems/1000][71], [MR][72] [4176784][73]
- Horton, J. D. (1983), "Sets with no empty convex 7-gons", *[Canadian Mathematical Bulletin][74]*, **26**(4): 482– 484, [doi][53]: [10.4153/CMB-1983-077-8][75], [S2CID][76] [120267029][77]
- Kalbfleisch, J.D.; [Kalbfleisch, J.G.][78]; Stanton, R.G. (1970), "A combinatorial problem on convex regions", *Proc. Louisiana Conf. Combinatorics, Graph Theory and Computing*, Congressus Numerantium, vol. 1, Baton Rouge, La.: Louisiana State Univ., pp. 180– 188
- [Kleitman, D.J.][79]; [Pachter, L.][80] (1998), "Finding convex sets among points in the plane", *[Discrete and Computational Geometry][52]*, **19**(3): 405– 410, [doi][53]: [10.1007/PL00009358][81]
- Morris, W.; Soltan, V. (2000), "The Erdős-Szekeres problem on points in convex position—A survey", *[Bulletin of the American Mathematical Society][82]*, **37**(4): 437– 458, [doi][53]: [10.1090/S0273-0979-00-00877-6][83]
- Nicolás, Carlos M. (2007), "The empty hexagon theorem", *[Discrete and Computational Geometry][52]*, **38**(2): 389– 397, [doi][53]: [10.1007/s00454-007-1343-6][84]
- [Overmars, M.][85] (2003), "Finding sets of points without empty convex 6-gons", *[Discrete and Computational Geometry][52]*, **29**(1): 153– 158, [doi][53]: [10.1007/s00454-002-2829-x][86]
- [Peterson, Ivars][87] (2000), ["Planes of Budapest"][88], *MAA Online*, archived from [the original][89] on 2013-07-02
- [Scheinerman, Edward R.][90]; [Wilf, Herbert S.][91] (1994), "The rectilinear crossing number of a complete graph and Sylvester's "four point problem" of geometric probability", *[American Mathematical Monthly][92]*, **101**(10), Mathematical Association of America: 939– 943, [doi][53]: [10.2307/2975158][93], [JSTOR][94] [2975158][95]
- Suk, Andrew (2016), "On the Erdős–Szekeres convex polygon problem", *J. Amer. Math. Soc.*, **30**(4): 1047– 1053, [arXiv][65]: [1604.08657][96], [doi][53]: [10.1090/jams/869][97], [S2CID][76] [15732134][98]
- [Szekeres, G.][6]; Peters, L. (2006), "Computer solution to the 17-point Erdős-Szekeres problem", *[ANZIAM Journal][99]*, **48**(2): 151– 164, [doi][53]: [10.1017/S144618110000300X][100]
- Tóth, G.; Valtr, P. (1998), "Note on the Erdős-Szekeres theorem", *[Discrete and Computational Geometry][52]*, **19**(3): 457– 459, [doi][53]: [10.1007/PL00009363][101]
- Tóth, G.; Valtr, P. (2005), "The Erdős-Szekeres theorem: upper bounds and related results", in [Goodman, Jacob E.][102]; [Pach, János][69]; [Welzl, Emo][103] (eds.), **[Combinatorial and Computational Geometry][104] (PDF), Mathematical Sciences Research Institute Publications, vol. 52, Cambridge University Press, pp. 557– 568, archived from [the original][105] (PDF) on 2019-07-28, retrieved 2015-02-28
- Valtr, P. (2008), "On empty hexagons", in [Goodman, Jacob E.][102]; [Pach, János][69]; [Pollack, Richard][106] (eds.), **[Surveys on Discrete and Computational Geometry: Twenty Years Later: AMS-IMS-SIAM Joint Summer Research Conference, June 18-22, 2006, Snowbird, Utah][107], Contemporary Mathematics, vol. 453, American Mathematical Society, pp. 433– 442, [ISBN][40] [9780821842393][108]

## External links

[[edit][109]]

- [Happy ending problem][110] and [Ramsey-theoretic proof of the Erdős-Szekeres theorem][111] on [PlanetMath][112]
- [Weisstein, Eric W.][113], ["Happy End Problem"][114], *[MathWorld][115]*

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Happy_ending_problem&oldid=1368870559][116] "

[Categories][117]:

- [Discrete geometry][118]
- [Euclidean plane geometry][119]
- [Quadrilaterals][120]
- [Polygons][121]
- [Mathematical problems][122]
- [Ramsey theory][123]
- [Paul Erdős][124]

Hidden categories:

- [Articles with short description][125]
- [Short description is different from Wikidata][126]
- [CS1 Hungarian-language sources (hu)][127]

Search

Happy ending problem

16 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/The_Happy_End_Problem
[2]: https://en.wikipedia.org/wiki/Erdős–Szekeres_theorem
[3]: https://en.wikipedia.org/wiki/File:Happy-End-problem.svg
[4]: https://en.wikipedia.org/wiki/Mathematics
[5]: https://en.wikipedia.org/wiki/Paul_Erdős
[6]: https://en.wikipedia.org/wiki/George_Szekeres
[7]: https://en.wikipedia.org/wiki/Esther_Szekeres
[8]: https://en.wikipedia.org/wiki/General_position
[9]: https://en.wikipedia.org/wiki/Vertex_(graph_theory)
[10]: https://en.wikipedia.org/wiki/Convex_polygon
[11]: https://en.wikipedia.org/wiki/Quadrilateral
[12]: https://en.wikipedia.org/wiki/Ramsey_theory
[13]: https://en.wikipedia.org/wiki/Convex_hull
[14]: https://en.wikipedia.org/wiki/Triangle
[15]: https://en.wikipedia.org/wiki/Polygon
[16]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=1
[17]: https://en.wikipedia.org/wiki/File:8-points-no-pentagon.svg
[18]: https://en.wikipedia.org/wiki/Integer
[19]: https://en.wikipedia.org/wiki/Pentagon
[20]: https://en.wikipedia.org/wiki/Conjecture
[21]: https://en.wikipedia.org/wiki/File:16nohexagon.svg
[22]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=2
[23]: https://en.wikipedia.org/wiki/Heptagon
[24]: https://en.wikipedia.org/wiki/SAT_solver
[25]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=3
[26]: https://en.wikipedia.org/wiki/Crossing_number_(graph_theory)
[27]: https://en.wikipedia.org/wiki/Graph_drawing
[28]: https://en.wikipedia.org/wiki/Complete_graph
[29]: https://en.wikipedia.org/wiki/Euclidean_space
[30]: https://en.wikipedia.org/wiki/Convex_polytope
[31]: https://en.wikipedia.org/wiki/Convex_position
[32]: https://en.wikipedia.org/wiki/Cyclic_polytope
[33]: https://en.wikipedia.org/wiki/Neighborly_polytope
[34]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=4
[35]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=5
[36]: http://www.smh.com.au/news/obituaries/a-world-of-teaching-and-numbers--times-two/2005/11/06/1131211943674.html
[37]: https://en.wikipedia.org/wiki/Michael_Cowling
[38]: https://en.wikipedia.org/wiki/The_Sydney_Morning_Herald
[39]: https://www.quantamagazine.org/a-puzzle-of-clever-connections-nears-a-happy-end-20170530/
[40]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[41]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-7868-6362-4
[42]: https://www.sfu.ca/~vjungic/RamseyProjects/sec_Pr_30.html
[43]: https://honlap.eotvos.elte.hu/wp-content/uploads/2016/02/fizikusok.pdf
[44]: https://en.wikipedia.org/wiki/Binomial_coefficient
[45]: https://en.wikipedia.org/wiki/Big_O_notation
[46]: https://en.wikipedia.org/wiki/Catalan_number
[47]: https://en.wikipedia.org/wiki/Stirling's_approximation
[48]: https://science.org.au/our-focus/history-australian-science/conversations-australian-scientists/professor-george-szekeres-1911-2005-mathematician
[49]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=6
[50]: https://en.wikipedia.org/wiki/Fan_Chung
[51]: https://en.wikipedia.org/wiki/Ronald_Graham
[52]: https://en.wikipedia.org/wiki/Discrete_and_Computational_Geometry
[53]: https://en.wikipedia.org/wiki/Doi_(identifier)
[54]: https://doi.org/10.1007%2FPL00009353
[55]: http://www.numdam.org/item?id=CM_1935__2__463_0
[56]: https://en.wikipedia.org/wiki/Compositio_Mathematica
[57]: https://doi.org/10.1007%2Fs00454-007-9018-x
[58]: https://en.wikipedia.org/wiki/Branko_Grünbaum
[59]: https://en.wikipedia.org/wiki/Victor_Klee
[60]: https://en.wikipedia.org/wiki/Günter_M._Ziegler
[61]: https://en.wikipedia.org/wiki/Convex_Polytopes
[62]: https://en.wikipedia.org/wiki/Springer-Verlag
[63]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-00424-6
[64]: https://en.wikipedia.org/wiki/Elemente_der_Mathematik
[65]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[66]: https://arxiv.org/pdf/2403.00737
[67]: https://doi.org/10.1007%2F978-3-031-57246-3_5
[68]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-031-57245-6
[69]: https://en.wikipedia.org/wiki/János_Pach
[70]: https://arxiv.org/pdf/1710.11415
[71]: https://doi.org/10.4171%2Fjems%2F1000
[72]: https://en.wikipedia.org/wiki/MR_(identifier)
[73]: https://mathscinet.ams.org/mathscinet-getitem?mr=4176784
[74]: https://en.wikipedia.org/wiki/Canadian_Mathematical_Bulletin
[75]: https://doi.org/10.4153%2FCMB-1983-077-8
[76]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[77]: https://api.semanticscholar.org/CorpusID:120267029
[78]: https://en.wikipedia.org/wiki/James_G._Kalbfleisch
[79]: https://en.wikipedia.org/wiki/Daniel_Kleitman
[80]: https://en.wikipedia.org/wiki/Lior_Pachter
[81]: https://doi.org/10.1007%2FPL00009358
[82]: https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society
[83]: https://doi.org/10.1090%2FS0273-0979-00-00877-6
[84]: https://doi.org/10.1007%2Fs00454-007-1343-6
[85]: https://en.wikipedia.org/wiki/Mark_Overmars
[86]: https://doi.org/10.1007%2Fs00454-002-2829-x
[87]: https://en.wikipedia.org/wiki/Ivars_Peterson
[88]: https://web.archive.org/web/20130702060326/http://www.maa.org/mathland/mathtrek_10_3_00.html
[89]: http://www.maa.org/mathland/mathtrek_10_3_00.html
[90]: https://en.wikipedia.org/wiki/Ed_Scheinerman
[91]: https://en.wikipedia.org/wiki/Herbert_Wilf
[92]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[93]: https://doi.org/10.2307%2F2975158
[94]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[95]: https://www.jstor.org/stable/2975158
[96]: https://arxiv.org/pdf/1604.08657
[97]: https://doi.org/10.1090%2Fjams%2F869
[98]: https://api.semanticscholar.org/CorpusID:15732134
[99]: https://en.wikipedia.org/wiki/ANZIAM_Journal
[100]: https://doi.org/10.1017%2FS144618110000300X
[101]: https://doi.org/10.1007%2FPL00009363
[102]: https://en.wikipedia.org/wiki/Jacob_E._Goodman
[103]: https://en.wikipedia.org/wiki/Emo_Welzl
[104]: https://web.archive.org/web/20190728224026/http://library.msri.org/books/Book52/files/30toth.pdf
[105]: http://library.msri.org/books/Book52/files/30toth.pdf
[106]: https://en.wikipedia.org/wiki/Richard_M._Pollack
[107]: http://kam.mff.cuni.cz/~valtr/h.ps
[108]: https://en.wikipedia.org/wiki/Special:BookSources/9780821842393
[109]: /w/index.php?title=Happy_ending_problem&amp;action=edit&amp;section=7
[110]: https://web.archive.org/web/20060925032614/http://planetmath.org/encyclopedia/HappyEndingProblem.html
[111]: https://web.archive.org/web/20060925032736/http://planetmath.org/encyclopedia/RamseyTheoreticProofOfTheErdHosSzekeresTheorem.html
[112]: https://en.wikipedia.org/wiki/PlanetMath
[113]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[114]: https://mathworld.wolfram.com/HappyEndProblem.html
[115]: https://en.wikipedia.org/wiki/MathWorld
[116]: https://en.wikipedia.org/w/index.php?title=Happy_ending_problem&amp;oldid=1368870559
[117]: /wiki/Help:Category
[118]: /wiki/Category:Discrete_geometry
[119]: /wiki/Category:Euclidean_plane_geometry
[120]: /wiki/Category:Quadrilaterals
[121]: /wiki/Category:Polygons
[122]: /wiki/Category:Mathematical_problems
[123]: /wiki/Category:Ramsey_theory
[124]: /wiki/Category:Paul_Erd%C5%91s
[125]: /wiki/Category:Articles_with_short_description
[126]: /wiki/Category:Short_description_is_different_from_Wikidata
[127]: /wiki/Category:CS1_Hungarian-language_sources_(hu)
