<!-- source: https://doi.org/10.1007/s00454-014-9578-5 | converted from HTML -->

A Note on Toeplitz’ Conjecture | Discrete & Computational Geometry | Springer Nature Link

Skip to main content

# A Note on Toeplitz’ Conjecture

- Published: 19 February 2014

- Volume 51, pages 722–728 ( 2014)
- Cite this article

[Download PDF][1]

[Save article][2]

[View saved research][3]

[Discrete & Computational Geometry][4] [Aims and scope][5] [Submit manuscript][6]

A Note on Toeplitz’ Conjecture

[Download PDF][1]

## Abstract

In 1911, Toeplitz made a conjecture asserting that every Jordan curve in \(\mathbb{R}^{2}\) contains four points forming the corners of a square. Here Conjecture C is presented, which states that the side length of the largest square on a closed curve that consists of edges of an *n*×*n*grid is at least \(1/\sqrt{2}\) times the side length of the largest axis-aligned square contained inside the curve. Conjecture C implies Toeplitz’ conjecture and is verified computationally for *n*≤13.

### Similar content being viewed by others

### [Curves in \(\mathbb {R}^4\) and Two-Rich Points][7]

Article 13 October 2016

### [Empty Squares in Arbitrary Orientation Among Points][8]

Article 25 July 2022

### [Multiple Structures on Smooth on Singular Varieties][9]

Chapter © 2018

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Computational Mathematics and Numerical Analysis][10]
- [Geometry][11]
- [Mathematics][12]
- [Mathematics Education][13]
- [Number Theory][14]
- [Tiling][15]
- [Numerical Methods in Geometric Function Theory][16]

## 1 Introduction

In 1911, Toeplitz [[6][17]] made the following conjecture regarding Jordan (that is, simple and closed) curves.

### Conjecture T

(Toeplitz’ Conjecture)

*Every Jordan curve in*\(\mathbb{R}^{2}\)*contains four points forming the corners of a square*.

Conjecture T, listed as [[1][18], Problem B2], is still open, but many partial results have been obtained. Already in 1913, Emch [[2][19]] proved that if the Jordan curve is the boundary of a convex set and sufficiently smooth, then Toeplitz’ conjecture is true. In 1916, Emch [[3][20]] proved Toeplitz’ conjecture for a much larger class of Jordan curves, which in particular includes the polygons. We shall not describe the many interesting further partial results here, but recommend the recent survey paper [[4][21]] by Matschke, both for its contents and its extensive list of references.

In this note a conjecture first stated in [[8][22]] is considered. Conjecture C asserts that the side length of the largest square on a closed curve that consists of edges of an *n*×*n*grid—the vertices and edges of which form an (*n*+1)×(*n*+1) *grid graph*—is at least \(1/\sqrt{2}\) times the side length of the largest axis-aligned square contained inside the curve. It is shown that Conjecture C implies Toeplitz’ conjecture. Some evidence is further provided for Conjecture C by carrying out a computational study for small *n*.

The note is organized as follows. In Sect. [2][23], Conjecture C is considered and some useful results are derived. In Sect. [3][24], an algorithm used to obtain computational evidence for Conjecture C is presented. The algorithm is applied to the cases *n*≤13, for which Conjecture C turns out to hold. Some concluding remarks are finally given in Sect. [4][25].

## 2 Conjecture C

We denote the family of all Jordan curves in \(\mathbb{R}^{2}\) by \(\mathcal{J}\). We further denote by \(\mathcal{J}'\) the family of finite Jordan curves that are composed only of segments with endpoints (*x*,*y*) and (*x*+1,*y*) or (*x*,*y*) and (*x*,*y*+1), where *x*and *y*are integers. From here on, any curve considered is assumed to belong to \(\mathcal{J}'\), unless otherwise mentioned.

For a curve *J*, we define *i*(*J*) as the side length of a largest open square with horizontal and vertical sides that is contained in the bounded component of \(\mathbb{R}^{2}\setminus J\), and *o*(*J*) as the side length of a smallest closed square of the aforementioned type that contains *J*. Figure [1][26] illustrates these definitions through a curve *J*in the 9×9 grid. Here *i*(*J*)=6 and the (unique) square corresponding to *i*(*J*) is colored gray. The largest inscribed square has side length \(6/\sqrt{2}\) and is drawn with a dashed line. Moreover, *o*(*J*)=9, and one square corresponding to *o*(*J*) overlaps exactly with the displayed 9×9 grid.

**Fig. 1**

[image: Fig. 1]

[Full size image][27]

A Jordan curve in the 9×9 grid

We shall now make a formal statement of Conjecture C.

### Conjecture C

*A Jordan curve*\(J \in \mathcal{J}'\)*contains four points of the integer lattice that form the corners of a square of side length at least*\(i(J)/\sqrt{2}\).

In the even case, *i*(*J*)=2*m*, the side length is at least \(m\sqrt{2}\). In the odd case, *i*(*J*)=2*m*+1, the side length is at least \(\sqrt{m^{2}+(m+1)^{2}}\), which is the smallest distance greater than or equal to \((2m+1)/\sqrt{2}\) that can occur between points in an integer lattice.

### Theorem 1

*Conjecture *C *implies Conjecture *T.

### Proof

Consider a Jordan curve \(J\in\mathcal{J}\). Many well-known proofs for the Jordan Curve Theorem include a lemma asserting that any Jordan curve \(J \in \mathcal{J}\) can be approximated arbitrarily well with polygons with respect to, say, the Hausdorff metric *d**H*. Such a proof can be found in, for example, [[7][28]]. Polygons can, in turn, be approximated with scaled versions of curves in \(\mathcal{J}'\). Thus, there exists a sequence of curves in \(\mathcal{J}'\): *J*1,*J*2,*J*3,…, such that *J*1,*J*2 /2,*J*3 /3,… converges to *J*, where *J**n*/*n*is the curve *J**n*scaled by a factor of 1/*n*.

Let *S**n*on *J**n*/*n*be a square with side length at least \(i(J_{n}/n)/\sqrt{2}\) as guaranteed by Conjecture C. A simple compactness argument shows that there must be a sequence *n*1 <*n*2 <*n*3 <⋯ such that \(S_{n_{1}},S_{n_{2}},S_{n_{3}},\ldots\) converges to a square *S*. Since each corner \(S_{n_{i}}\) is in \(J_{n_{i}}/n_{i}\), which converges to *J*, it follows that each corner of *S*is on *J*.

Furthermore, since *i*(*J**n*/*n*) converges toward *i*(*J*), the side length of *S*is at least \(i(J)/\sqrt{2}\). In particular, since \(i(J)/\sqrt{2} > 0\), the side length is greater than zero, and *S*is not degenerate. □

We know by [[3][20]] that some four points of a curve \(J \in \mathcal{J}'\) are the corners of a square, but they need not be lattice points. We will now show that the corners of the square can be chosen as lattice points. This result will be very useful for the computer work to be discussed in Sect. [3][24].

### Theorem 2

*At least one inscribed square of maximum size on a curve*\(J\in \mathcal{J}'\)*has all four corners on lattice points*.

### Proof

It suffices to show that for any square on *J*, there is a square on the lattice points of *J*whose side length is not smaller. Let the corners of a square on *J*(in anticlockwise order) be *A*,*B*,*C*,*D*, where *A*=(*x*0,*y*0) is a leftmost one (and a lowest one if *AD*is vertical). Then the other three corners can be represented as *B*=(*x*0 +*a*,*y*0 −*b*), *C*=(*x*0 +*a*+*b*,*y*0 −*b*+*a*), and *D*=(*x*0 +*b*,*y*0 +*a*), where \(a,b \in \mathbb{R}\) are nonnegative.

By the definition of \(\mathcal{J}'\), each of the four corners *A*,*B*,*C*,*D*has at least one integral coordinate. Assume that three out the four corners—w.l.o.g., *A*,*B*,*C*—have an integral second coordinate. Now *y*0, *a*, and *b*are all integers, whereby *y*0 +*a*, the second coordinate of *D*, is also an integer. A translation through adding ⌈*x*0 ⌉−*x*0 (which is less than 1) to the first coordinate of all four corners now gives a square that has all corners on lattice points and on *J*.

We are now left with the case of two corners with the first coordinate integral and two corners with the second coordinate integral. This gives us two subcases to consider: The two corners with integral first coordinates are (i) adjacent or (ii) nonadjacent.

In case (i), we can assume w.l.o.g. that the first two corners correspond to *A*and *B*, and the last two correspond to *C*and *D*. Now *x*0, *x*0 +*a*, *y*0 −*b*+*a*, and *y*0 +*a*are integers, whereby (*x*0 +*a*)−*x*0 =*a*and *y*0 +*a*−(*y*0 +*a*−*b*)=*b*are also integers. Furthermore, *x*0 and *y*0 are integers, and thus all four corners are lattice points. In case (ii), the first two corners correspond to *A*and *C*, and one finds that the square can be continuously rotated, with the corners following *J*, until they simultaneously become lattice points. (The square changes its size during that process of course). One can rotate clockwise or counterclockwise, and one of these directions will result in an increase of the size of the square. In more detail, rotating the square in this way corresponds to adding (0,*δ*),(−*δ*,0),(0,−*δ*), and (*δ*,0) to *A*,*B*,*C*, and *D*, respectively, for some \(\delta \in \mathbb{R}\). Since *x*0, *y*0 −*b*, *x*0 +*a*+*b*, and *y*0 +*a*are integers, setting *δ*=⌈*b*⌉−*b*for clockwise rotation or *δ*=⌊*b*⌋−*b*for anticlockwise rotation moves the corners of the square to lattice points. □

## 3 The Computation

As a preamble to the description of the computer work, we present a theorem that, in addition to the obvious symmetries in the problem, gives a significant speedup in the computations. In the following, we denote the side length of the largest square having its corners on *J*by *s*(*J*).

### Theorem 3

*If a curve**J**has a chord**AB**of length*1, *with**A**and**B**lattice points*, *then**J**is not a counterexample to Conjecture *C *of minimal length*.

### Proof

We will use proof by contradiction. Assume *J*to be a counterexample to Conjecture C of minimal length, with a chord of length 1. Conjecture C asserts that \(s(J) \geq i(J)/\sqrt{2}\), so for a counterexample, we have \(s(J) < i(J)/\sqrt{2}\). To give a contradiction on the minimality of *J*, it suffices to find a shorter *J*′ for which *s*(*J*′)≤*s*(*J*) and *i*(*J*′)≥*i*(*J*). We consider two cases.

(i) The line segment *AB*is an inner chord. As the open segment *AB*is contained in the bounded component of \(\mathbb{R}^{2} \setminus J\), it follows that *J*∖{*A*,*B*} has two components, *C*1 and *C*2. By adding *AB*to *C*1 and *C*2 we get two Jordan curves *J*1 and *J*2, respectively, both of which are shorter than *J*. Since the open segment *AB*does not contain lattice points, the lattice points of *J*1 and *J*2 all belong to *J*, and by Theorem 2 we have *s*(*J*1),*s*(*J*2)≤*s*(*J*). If a square attaining *i*(*J*) contains the open segment *AB*, then the side length of the square is 1 and *i*(*J*1)=*i*(*J*2)=*i*(*J*)=1, which contradicts the minimality of *J*. On the other hand, if it does not contain *AB*, then it is contained in either \(\mathbb{R}^{2} \setminus J_{1}\) or \(\mathbb{R}^{2} \setminus J_{2}\). Without loss of generality, it is included in the former, and *i*(*J*1)=*i*(*J*). Now *J*1 is a counterexample to Conjecture C, contradicting the minimality of *J*.

(ii) The line segment *AB*is an outer chord. We proceed as in (i) and choose *J*1 so that the bounded component of \(\mathbb{R}^{2} \setminus J_{1}\) contains the bounded component of \(\mathbb{R}^{2} \setminus J\); thereby *i*(*J*1)≥*i*(*J*). Since the lattice points of *J*1 are all on *J*, *s*(*J*1)≤*s*(*J*). Hence, *J*1 is a counterexample to C, shorter than *J*; once again a contradiction to the minimality of *J*. □

In the computations for an *n*×*n*grid, we consider an (*n*+1)×(*n*+1) grid graph. In the framework of graph theory, we use the term *cycle*instead of *closed curve*. Our aim is to construct all chordless cycles *J*that are counterexamples to Conjecture C. This can be done with depth-first search and appropriate pruning rules. If no counterexamples are found, the conjecture has been verified for the given value of *n*=*o*(*J*). The subtasks of computing *i*(*J*) and *s*(*J*) for a given *J*are straightforward.

In the depth-first search, we first choose one vertex *v*of the grid graph as a starting point and then try to build a cycle in all possible ways. The following pruning rules were used:

-

If a chord is created, then the search can be pruned.

-

Symmetry is taken into account via the automorphism group of the grid graph—the dihedral group of order 8—and translation, i.e., moving the cycle along the axes.

-

With some order defined on the vertices of the grid graph, the starting point *v*is required to be the smallest vertex in the cycle.

-

If the cycle cannot be completed without creating a chord at some later stage, then the search can be pruned.

-

Let *I*be an upper bound on *i*(*J*), and *S*a lower bound on *s*(*J*). If \(S \geq I/\sqrt{2}\), then no counterexample can be found by completing the cycle, and the search can be pruned.

With this algorithm and these pruning rules, the cases *n*≤13 could be settled using less than 30 core-years of CPU-time on a cluster of computers with Intel Core i7 870 processors. It turns out that there are no counterexamples to Conjecture C for *n*≤13.

### Theorem 4

*Conjecture *C *holds for every*\(J \in \mathcal{J}'\)*with**o*(*J*)≤13.

For 8≤*n*≤13, many cycles are found for which the conjecture is sharp, that is, the side length of the largest square is exactly \(i(J)/\sqrt{2}\). Examples of such cycles are shown in Fig. [2][29].

**Fig. 2**

[image: Fig. 2]

[Full size image][30]

Extremal cycles

No counterexamples were found by searching a tiny fraction of the search space for the case *n*=14. Completing the case *n*=14 with the current algorithm would require more than 1000 core-years of CPU-time.

The method and its implementation were partially validated by listing all chordless cycles *J*for which *o*(*J*)≤8 and \(s(J) < (3/2) i(J)/\sqrt{2}\) and then comparing these with the output of a simple brute force method. It turns out that there are 327 812 equivalence classes of such cycles, where equivalence is defined as above via the dihedral group and translation.

## 4 Final Remarks

The computational approach in this paper is to exhaustively verify Conjecture C for *n*×*n*grids for as large values of *n*as possible. An alternative approach for larger values of *n*is to carry out (a multitude of) partial searches. Such an approach can obviously be successful only if Conjecture C does not hold and if one is lucky to find a counterexample.

The paper [[5][31]] contains a result that might allow one to carry the exhaustive verification further: Conjecture T holds for any curve \(J \in \mathcal{J}\) that is contained in the annulus with radii 1 and \(1+\sqrt{2}\). Furthermore, some square with corners on such a curve *J*has side length at least \(\sqrt{2}\). Another consequence of this result is that if one chooses *J*0 as a curve with the shape of a square—that is, *i*(*J*0)=*o*(*J*0)=*n*—one gets a positive answer to a natural question related to Conjecture C: If *U*is the closed 1-neighborhood of *J*0 in the space of all curves \(J \in \mathcal{J}\), with the Hausdorff metric derived from the norm on \(\mathbb{R}^{2}\) given by max{|*x*|,|*y*|}, does Conjecture C hold in *U*? The positive answer holds for all values of *n*, but we have not been able to find a simpler proof of that and have to rely on [[5][31]].

It should be noted that Conjecture C is probably not sharp for curves *J*for which *i*(*J*)≤4. For example, it is relatively easy to show that if *i*(*J*)=2, then *s*(*J*)≥2 (details omitted).

Let us finally mention another feature of our approach, in addition to its possible heuristic value; it may encourage someone to try the time-tested method of induction on Conjecture T (via Conjecture C).

## References

1.

Croft, H.T., Falconer, K.J., Guy, R.K.: Unsolved Problems in Geometry. Springer, New York (1991)

[Book][32] [MATH][33] [Google Scholar][34]

2.

Emch, A.: Some properties of closed convex curves in a plane. Am. J. Math. **35**, 407–412 (1913)

[Article][35] [MATH][36] [MathSciNet][37] [Google Scholar][38]

3.

Emch, A.: On some properties of the medians of closed continuous curves formed by analytic arcs. Am. J. Math. **38**, 6–18 (1916)

[Article][39] [MATH][40] [MathSciNet][41] [Google Scholar][42]

4.

Matschke, B.: A survey on the square peg problem. Notices Am. Math. Soc., to appear

5.

Matschke, B.: On the square peg problem and some relatives II, submitted

6.

Toeplitz, O.: Ueber einige Aufgaben der Analysis Situs. Verhandlungen der Schweizerischen Naturforschenden Gesellschaft in Solothurn, vol. 4, p. 197 (1911)

[Google Scholar][43]

7.

Tverberg, H.: A proof of the Jordan curve theorem. Bull. Lond. Math. Soc. **12**, 34–38 (1980)

[Article][44] [MATH][45] [MathSciNet][46] [Google Scholar][47]

8.

Tverberg, H.: A conjecture on polyominoes, with consequences for Toeplitz’ “square on a Jordan curve” problem (1911). Oberwolfach Rep. **8**(1), 362–363 (2011)

[Google Scholar][48]

[Download references][49]

## Acknowledgements

The work of the first author was supported in part by the Academy of Finland under Grant No. 132122, the GETA Graduate School, the Nokia Foundation, and the Finnish Foundation for Technology Promotion. The work of the third author was supported in part by the Academy of Finland under Grant No. 132122.

## Author information

### Authors and Affiliations

1.

Department of Communications and Networking, Aalto University School of Electrical Engineering, P.O. Box 13000, 00076, Aalto, Finland

Ville H. Pettersson & Patric R. J. Östergård

2.

Department of Mathematics, University of Bergen, Johs. Bruns gate 12, 5008, Bergen, Norway

Helge A. Tverberg

Authors

1. Ville H. Pettersson

[View author publications][50]

Search author on: [PubMed][51] [Google Scholar][52]

2. Helge A. Tverberg

[View author publications][53]

Search author on: [PubMed][54] [Google Scholar][55]

3. Patric R. J. Östergård

[View author publications][56]

Search author on: [PubMed][57] [Google Scholar][58]

### Corresponding author

Correspondence to [Ville H. Pettersson][59].

## Rights and permissions

[Reprints and permissions][60]

## About this article

### Cite this article

Pettersson, V.H., Tverberg, H.A. & Östergård, P.R.J. A Note on Toeplitz’ Conjecture. *Discrete Comput Geom***51**, 722–728 (2014). https://doi.org/10.1007/s00454-014-9578-5

[Download citation][61]

-

Received: 10 September 2013

-

Revised: 03 February 2014

-

Accepted: 04 February 2014

-

Published: 19 February 2014

-

Issue date: April 2014

-

DOI: https://doi.org/10.1007/s00454-014-9578-5

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Chordless cycle][62]
- [Depth-first search][63]
- [Grid graph][64]
- [Inscribed square][65]
- [Jordan curve][66]
- [Toeplitz’ conjecture][67]


## Links

[1]: /content/pdf/10.1007/s00454-014-9578-5.pdf
[2]: /article/10.1007/s00454-014-9578-5/save-research?_csrf=FWeFHfaw_i__H3xWU3x75iw-GG3hLBcR
[3]: /saved-research
[4]: /journal/454
[5]: /journal/454/aims-and-scope
[6]: https://www.editorialmanager.com/dcge
[7]: https://link.springer.com/10.1007/s00454-016-9833-z?fromPaywallRec=false
[8]: https://link.springer.com/10.1007/s00453-022-01002-1?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/978-3-319-96827-8_15?fromPaywallRec=false
[10]: /subjects/computational-mathematics-and-numerical-analysis
[11]: /subjects/geometry
[12]: /subjects/mathematics
[13]: /subjects/mathematics-education
[14]: /subjects/number-theory
[15]: /subjects/tiling
[16]: /subjects/numerical-methods-in-geometric-function-theory
[17]: /article/10.1007/s00454-014-9578-5#ref-CR6
[18]: /article/10.1007/s00454-014-9578-5#ref-CR1
[19]: /article/10.1007/s00454-014-9578-5#ref-CR2
[20]: /article/10.1007/s00454-014-9578-5#ref-CR3
[21]: /article/10.1007/s00454-014-9578-5#ref-CR4
[22]: /article/10.1007/s00454-014-9578-5#ref-CR8
[23]: /article/10.1007/s00454-014-9578-5#Sec2
[24]: /article/10.1007/s00454-014-9578-5#Sec3
[25]: /article/10.1007/s00454-014-9578-5#Sec4
[26]: /article/10.1007/s00454-014-9578-5#Fig1
[27]: /article/10.1007/s00454-014-9578-5/figures/1
[28]: /article/10.1007/s00454-014-9578-5#ref-CR7
[29]: /article/10.1007/s00454-014-9578-5#Fig2
[30]: /article/10.1007/s00454-014-9578-5/figures/2
[31]: /article/10.1007/s00454-014-9578-5#ref-CR5
[32]: https://link.springer.com/doi/10.1007/978-1-4612-0963-8
[33]: http://www.emis.de/MATH-item?0748.52001
[34]: http://scholar.google.com/scholar_lookup?amp;title=Unsolved%20Problems%20in%20Geometry&amp;doi=10.1007%2F978-1-4612-0963-8&amp;publication_year=1991&amp;author=Croft%2CH.T.&amp;author=Falconer%2CK.J.&amp;author=Guy%2CR.K.
[35]: https://doi.org/10.2307%2F2370404
[36]: http://www.emis.de/MATH-item?JFM%2044.0561.01
[37]: http://www.ams.org/mathscinet-getitem?mr=1506193
[38]: http://scholar.google.com/scholar_lookup?amp;title=Some%20properties%20of%20closed%20convex%20curves%20in%20a%20plane&amp;journal=Am.%20J.%20Math.&amp;doi=10.2307%2F2370404&amp;volume=35&amp;pages=407-412&amp;publication_year=1913&amp;author=Emch%2CA.
[39]: https://doi.org/10.2307%2F2370541
[40]: http://www.emis.de/MATH-item?JFM%2046.0832.03
[41]: http://www.ams.org/mathscinet-getitem?mr=1506274
[42]: http://scholar.google.com/scholar_lookup?amp;title=On%20some%20properties%20of%20the%20medians%20of%20closed%20continuous%20curves%20formed%20by%20analytic%20arcs&amp;journal=Am.%20J.%20Math.&amp;doi=10.2307%2F2370541&amp;volume=38&amp;pages=6-18&amp;publication_year=1916&amp;author=Emch%2CA.
[43]: http://scholar.google.com/scholar_lookup?amp;title=Ueber%20einige%20Aufgaben%20der%20Analysis%20Situs&amp;publication_year=1911&amp;author=Toeplitz%2CO.
[44]: https://doi.org/10.1112%2Fblms%2F12.1.34
[45]: http://www.emis.de/MATH-item?0432.54032
[46]: http://www.ams.org/mathscinet-getitem?mr=565480
[47]: http://scholar.google.com/scholar_lookup?amp;title=A%20proof%20of%20the%20Jordan%20curve%20theorem&amp;journal=Bull.%20Lond.%20Math.%20Soc.&amp;doi=10.1112%2Fblms%2F12.1.34&amp;volume=12&amp;pages=34-38&amp;publication_year=1980&amp;author=Tverberg%2CH.
[48]: http://scholar.google.com/scholar_lookup?amp;title=A%20conjecture%20on%20polyominoes%2C%20with%20consequences%20for%20Toeplitz%E2%80%99%20%E2%80%9Csquare%20on%20a%20Jordan%20curve%E2%80%9D%20problem%20%281911%29&amp;journal=Oberwolfach%20Rep.&amp;volume=8&amp;issue=1&amp;pages=362-363&amp;publication_year=2011&amp;author=Tverberg%2CH.
[49]: https://citation-needed.springer.com/v2/references/10.1007/s00454-014-9578-5?format=refman&amp;flavour=references
[50]: /search?sortBy=newestFirst&amp;contributor=Ville%20H.%20Pettersson
[51]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Ville%20H.%20Pettersson
[52]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Ville%20H.%20Pettersson%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[53]: /search?sortBy=newestFirst&amp;contributor=Helge%20A.%20Tverberg
[54]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Helge%20A.%20Tverberg
[55]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Helge%20A.%20Tverberg%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[56]: /search?sortBy=newestFirst&amp;contributor=Patric%20R.%20J.%20%C3%96sterg%C3%A5rd
[57]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Patric%20R.%20J.%20%C3%96sterg%C3%A5rd
[58]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Patric%20R.%20J.%20%C3%96sterg%C3%A5rd%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[59]: mailto:ville.pettersson@aalto.fi
[60]: https://s100.copyright.com/AppDispatchServlet?title=A%20Note%20on%20Toeplitz%E2%80%99%20Conjecture&amp;author=Ville%20H.%20Pettersson%20et%20al&amp;contentID=10.1007%2Fs00454-014-9578-5&amp;copyright=Springer%20Science%2BBusiness%20Media%20New%20York&amp;publication=0179-5376&amp;publicationDate=2014-02-19&amp;publisherName=SpringerNature&amp;orderBeanReset=true
[61]: https://citation-needed.springer.com/v2/references/10.1007/s00454-014-9578-5?format=refman&amp;flavour=citation
[62]: /search?query=Chordless%20cycle&amp;facet-discipline=#34;Mathematics&#34;
[63]: /search?query=Depth-first%20search&amp;facet-discipline=#34;Mathematics&#34;
[64]: /search?query=Grid%20graph&amp;facet-discipline=#34;Mathematics&#34;
[65]: /search?query=Inscribed%20square&amp;facet-discipline=#34;Mathematics&#34;
[66]: /search?query=Jordan%20curve&amp;facet-discipline=#34;Mathematics&#34;
[67]: /search?query=Toeplitz%E2%80%99%20conjecture&amp;facet-discipline=#34;Mathematics&#34;
