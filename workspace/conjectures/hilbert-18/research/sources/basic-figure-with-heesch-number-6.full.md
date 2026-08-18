<!-- source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7812982/ | converted from HTML -->

A Figure with Heesch Number 6: Pushing a Two-Decade-Old Boundary - PMC Skip to main content

**Official websites use .gov**
A **.gov**website belongs to an official government organization in the United States.

**Secure .gov websites use HTTPS**
A **lock**( Lock Locked padlock icon ) or **https://**means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.

[1]

[image: PMC search open icon][image: PMC search close ison]

- [Journal List][2]
- [User Guide][3]

- [image: Open resources icon]
- [image: View on publisher site icon] [4]
- [image: Download PDF icon] [5]
- [image: Collections icon][image: Collections icon]
- [image: Cite icon]
- [image: Show article permalink icon]

## PERMALINK

[image: Copy icon] Copy

[image: Open article navigation icon]

As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with, the contents by NLM or the National Institutes of Health.
Learn more: [PMC Disclaimer][6] | [PMC Copyright Notice][7]

[image: Springer Nature - PMC COVID-19 Collection logo]

Math Intell

. 2021 Jan 18;43(3):50–53. doi: [10.1007/s00283-020-10034-w][4]

# A Figure with Heesch Number 6: Pushing a Two-Decade-Old Boundary

[Bojan Bašić][8]

### Bojan Bašić

1 Department of Mathematics and Informatics, University of Novi Sad, Trg Dositeja Obradovića 4, Novi Sad, 21000 Serbia

Find articles by [Bojan Bašić][8]

1, ✉

- Author information
- Article notes
- Copyright and License information

1 Department of Mathematics and Informatics, University of Novi Sad, Trg Dositeja Obradovića 4, Novi Sad, 21000 Serbia

✉

Corresponding author.

Accepted 2020 Nov 23; Issue date 2021.

© The Author(s), under exclusive licence to Springer Science+Business Media, LLC part of Springer Nature 2021

This article is made available via the PMC Open Access Subset for unrestricted research re-use and secondary analysis in any form or by any means with acknowledgement of the original source. These permissions are granted for the duration of the World Health Organization (WHO) declaration of COVID-19 as a global pandemic.

[PMC Copyright notice][7]

PMCID: PMC7812982 PMID: [34934265][9]

---

Problems about tilings arise in recreational mathematics and various research areas such as those in [5, 7, 9]. Recall that we say that a figure *T*(for us, a figure is a closed topological disk) tiles the Euclidean plane E 2 if there exists a collection T of figures congruent to *T*such that ⋃ T = E 2 and every pair of distinct figures from T have disjoint interiors. The collection T is called a tiling, and its elements are called tiles.

The Heesch number of a given figure *T*(introduced in [4]) is defined as the maximal nonnegative integer *n*such that (speaking somewhat informally) *T*can be completely surrounded by congruent copies of itself *n*times; if such a maximal number does not exist, we say that the Heesch number is infinite. The motivation behind this definition is that the Heesch number measures how “far” we can advance toward a tiling of the whole plane using the given figure (the greater the Heesch number, the “farther” we can advance; and the Heesch number is infinite if and only if the figure tiles the plane).

Arguably, the main open problem regarding the Heesch number (referred to as Heesch’s problem) poses the question whether the set of finite values of Heesch numbers of plane figures has an upper bound. The following versions of the problem have been solved:

-

In the hyperbolic plane H 2, the Heesch number is unbounded [8].

-

In the Euclidean plane E 2, it has been proved, in a version in which more than one figure is used, that for each fixed integer *k*greater than 2, there exist sets consisting of *k*figures with arbitrarily large Heesch numbers [1].

-

In the asymptotic sense, in E d for d → ∞, it has been proved that for every nonnegative integer *n*, there exists a dimension *d*, depending on *n*, in which there exists a hypersolid whose Heesch number is finite and greater than *n*[2].

However, in its basic formulation as stated above, the problem is still open. Since the problem was first posed, there has been moderate progress on it, mainly in the discovery of figures with larger and larger Heesch numbers, which reached its peak in 2001. That year, in his PhD thesis, Casey Mann [6] conducted a systematic study of some (quite large) families of figures and discovered a figure whose Heesch number is 5, which became the largest known Heesch number since then. For almost two decades, this “record” has defied all attacks. In this note we announce a result that finally pushes this boundary further: we present a figure whose Heesch number is 6. A forthcoming article will contain additional new results on the notion of the Heesch number in which, among other things, all the details omitted here will be included, and the construction of the figure presented here will be put in a more general context.

We would like to mention here that Heesch’s problem is tightly connected to some other well-known and important problems in the theory of tilings. Two such problems are whether there exists an algorithm to decide whether a given figure tiles the plane (the so-called domino problem for monotiles) and whether there exists a figure that tiles the plane but admits no periodic tiling (the so-called Einstein problem). Up to some (relatively mild) restrictions on how the tiles may be matched (for example, if only vertex-to-vertex tilings are allowed), it turns out that a negative answer to the domino problem implies both that the Heesch number is unbounded and that there exists an aperiodic tile. For a nice treatment of these (as well as many other) connections between various problems on tilings, we refer the reader to [3].

We begin our analysis with some necessary definitions.

## **Definition 1.**

We say that a figure *T*in the plane can be *surrounded n times*if there exist finite collections of figures C 1, C 2, …, C n in the plane such that the following conditions hold:

-

For each *i*, 1 ≤ i ≤ n, every figure from C i is congruent to *T*.

-

Every pair of distinct figures from { T } ∪ ⋃ i = 1 n C i have disjoint interiors.

-

For each *i*, 1 ≤ i ≤ n, every figure from C i has a common boundary point with some figure from C i - 1 (where by convention, we let C 0 = { T }).

-

For each *i*, 1 ≤ i ≤ n, ⋃ ⋃ j = 0 i C j is a closed topological disk such that ⋃ ⋃ j = 0 i - 1 C j is completely contained in its interior.

The collection C i is called the *i*th *corona*. 1

## **Definition 2.**

The *Heesch number*of a figure *T*is the maximal nonnegative integer *n*such that *T*can be surrounded *n*times. If such a maximum does not exist, then we define the Heesch number to be infinite.

We are now ready to exhibit a figure whose Heesch number is 6.

Our figure is presented in Figure 1. Note that it can be obtained by gluing together 6 regular hexagons, 11 equilateral triangles, and half an equilateral triangle. In Figure 2 (a) we show the white figure in the middle surrounded by six coronas. (There is a total of 169 figures here: the white one in the middle and 168 more surrounding it.) The individual coronas are shown in Figure 2 (b) (for each corona, the figures forming it are colored with the same color—bluish gray for C 1, tan for C 2, ..., cyan for C 6).

### Figure 1.

[image: Figure 1]

[Open in a new tab][10]

A figure with Heesch number 6.

### Figure 2.

[image: Figure 2] [11]

[Open in a new tab][12]

(a) The 169 congruent figures comprising the white figure in the middle surrounded by six coronas. (b) The six individual coronas, each a different color.

We show first that if it were possible to tile the plane, then all the tiles would have to be placed matching the gridlines shown in Figure 3 (in Figure 3 (a), ignore the thick line and the fact that some of the hexagons are colored gray, all of which will be needed in the following paragraph; Figure 3 (b) shows a magnified detail of the grid in Figure 3 (a)). The argument is rather straightforward (though not too elegant; it reduces to considering a few cases), and we omit it here.

### Figure 3.

[image: Figure 3] [13]

[Open in a new tab][14]

The tiles must match these gridlines.

The observation from the preceding paragraph that a tiling of the plane would require the tiles to be placed on the gridlines makes the problem amenable to a brute-force attack by computer (systematically checking all the possible ways to build coronas), which gives that 6 is the maximum number of coronas that can be formed. However, the (weaker) assertion that the described figure does not tile the plane can be shown without computer assistance. (Note that this weaker assertion is still enough for the theorem formulated at the end of this section. Namely, since the figure does not tile the plane, its Heesch number is finite, and by Figure 2, we know that it is greater than or equal to 6.) We sketch the proof. Look at Figure 3 again (for the sake of simplicity, we shall assume that all the hexagons, as well as all the equilateral triangles between them, are of unit side). The figure enclosed by the thick line contains three unit hexagons in a row in each direction on the boundary and 24 unit triangles. If we enclose a larger concentric region containing *N*unit hexagons in a row, the total number of enclosed unit triangles will be of order 6 N 2 (more precisely, it will equal 6 ( N - 1) 2). We now estimate the total number of tiles that cover all these triangles. Note that each such tile can cover only gray hexagons (for a general *N*, gray hexagons are those enclosed by the thick line and an additional ring around it whose “thickness” is five hexagons; this is so because each tile that covers an enclosed equilateral triangle also covers at least one enclosed hexagon, and therefore, since the tile contains six hexagons in total, it cannot reach any nongray hexagon). Since there is a total of ∼ 3 N 2 gray hexagons (the exact value is 3 ( N + 5) ( N + 4) + 1), the total number of the considered tiles is no more than ∼ N 2 / 2. Finally, since each tile covers 11 1 2 unit triangles, all the considered tiles together cover no more than ∼ 23 / 4 N 2 unit triangles. Therefore, for a large enough *N*, not all the unit triangles inside the thick line can be covered, which means that our figure cannot tile the plane.

Altogether, the preceding discussion leads to the following result.

## **Theorem 3.**

The upper bound on finite Heesch numbers in the Euclidean plane is at least 6.

## Acknowledgments

The author was supported by the Ministry of Education, Science and Technological Development of Serbia (grant no. 451-03-68/2020-14/200125).

## Footnotes

1

This does not have anything to do with the SARS-CoV-2 coronavirus, though this research was indeed finished during the Covid-19 pandemic.

**Publisher's Note**

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## References

- [1]. Bašić B. The Heesch number for multiple prototiles is unbounded. C. R. Math. Acad. Sci. Paris. 2015;353:665–667. doi: 10.1016/j.crma.2015.05.002. [[DOI][15]] [[Google Scholar][16]]
- [2]. B. Bašić and A. Slivková. Asymptotical unboundedness of the Heesch number in E d for d → ∞. To appear in *Discrete Comput. Geom.*, 10.1007/s00454-020-00254-4, 2020.
- [3]. C. Goodman-Strauss. Open Questions in Tiling. Available online at [https://strauss.hosted.uark.edu/papers/survey.pdf][17], 2000.
- [4]. H. Heesch. *Reguläres Parkettierungsproblem*. Westdeutscher Verlag, 1968.
- [5]. C. S. Kaplan, *Introductory Tiling Theory for Computer Graphics*. Morgan & Claypool, 2009.
- [6]. C. Mann. *Heesch’s Problem and Other Tiling Problems*. PhD thesis, University of Arkansas, 2001.
- [7]. S. K. Stein and S. Szabó, *Algebra and Tiling: Homomorphisms in the Service of Geometry*. Mathematical Association of America, 1994.
- [8]. A. S. Tarasov. On the Heesch number for the Lobachevsky plane, *Mat. Zametki*88 (2010), 97–104 (in Russian). English translation: On the Heesch number for the hyperbolic plane. *Math. Notes*88 (2010), 97–102.
- [9]. W. P. Thurston. *Groups, Tilings and Finite State Automata*. Summer 1989 AMS Colloquium Lectures, Res. Rep., Geometry Computing Group, Minneapolis, MN, 1989.

[image: Close]

## ACTIONS

- [image: View on publisher site icon] [View on publisher site][4]
- [image: Download PDF icon] [PDF (399.8 KB)][5]
- [image: Cite icon] Cite
- [image: Collections icon][image: Collections icon] Collections
- [image: Permalink icon] Permalink

## PERMALINK

[image: Copy icon] Copy

## RESOURCES

### Similar articles

### Cited by other articles

### Links to NCBI Databases

## Cite

[image: Close icon]

- [image: Copy icon] Copy
- [image: Download icon] Download .nbib.nbib
-

Format: AMA APA MLA NLM

## Add to Collections

Back to Top[image: back to top icon]


## Links

[1]: /
[2]: /journals/
[3]: /about/userguide/
[4]: https://doi.org/10.1007/s00283-020-10034-w
[5]: pdf/283_2020_Article_10034.pdf
[6]: /about/disclaimer/
[7]: /about/copyright/
[8]: https://pubmed.ncbi.nlm.nih.gov/?term="Ba%C5%A1i%C4%87%20B"[Author]
[9]: https://pubmed.ncbi.nlm.nih.gov/34934265/
[10]: figure/Fig1/
[11]: https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&amp;p=PMC3&amp;id=7812982_283_2020_10034_Fig2_HTML.jpg
[12]: figure/Fig2/
[13]: https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&amp;p=PMC3&amp;id=7812982_283_2020_10034_Fig3_HTML.jpg
[14]: figure/Fig3/
[15]: https://doi.org/10.1016/j.crma.2015.05.002
[16]: https://scholar.google.com/scholar_lookup?journal=C.%20R.%20Math.%20Acad.%20Sci.%20Paris&amp;title=The%20Heesch%20number%20for%20multiple%20prototiles%20is%20unbounded&amp;author=B%20Ba%C5%A1i%C4%87&amp;volume=353&amp;publication_year=2015&amp;pages=665-667&amp;doi=10.1016/j.crma.2015.05.002&amp;
[17]: https://strauss.hosted.uark.edu/papers/survey.pdf
