<!-- source: https://link.springer.com/article/10.1007/s10817-017-9423-7 | converted from HTML -->

Fast Formal Proof of the Erdős–Szekeres Conjecture for Convex Polygons with at Most 6 Points | Journal of Automated Reasoning | Springer Nature Link

Skip to main content

# Fast Formal Proof of the Erdős–Szekeres Conjecture for Convex Polygons with at Most 6 Points

- Published: 05 September 2017

- Volume 62, pages 301–329 ( 2019)
- Cite this article

[Save article][1]

[View saved research][2]

[Journal of Automated Reasoning][3] [Aims and scope][4] [Submit manuscript][5]

## Abstract

A conjecture originally made by Klein and Szekeres in 1932 (now commonly known as “Erdős–Szekeres” or “Happy Ending” conjecture) claims that for every \(m \ge 3\), every set of \(2^{m-2}+1\) points in a general position (none three different points are collinear) contains a convex *m*-gon. The conjecture has been verified for \(m \le 6\). The case \(m=6\) was solved by Szekeres and Peters and required a huge computer enumeration that took “more than 3000 GHz hours”. In this paper we improve the solution in several directions. By changing the problem representation, by employing symmetry-breaking and by using modern SAT solvers, we reduce the proving time to around only a half of an hour on an ordinary PC computer (i.e., our proof requires only around 1 GHz hour). Also, we formalize the proof within the Isabelle/HOL proof assistant, making it significantly more reliable.

This is a preview of subscription content, [log in via an institution][6] to check access.

## Access this article

[Log in via an institution][6]

## Subscribe and save

Springer+

from €37.37 /Month

- Starting from 10 chapters or articles per month
- Access and download chapters and articles from more than 300k books and 2,500 journals
- Cancel anytime

[View plans][7]

## Buy Now

Price includes VAT (Kuwait)

Instant access to the full article PDF.

[Institutional subscriptions][8]

**Fig. 1**

**Fig. 2**

**Fig. 3**

**Fig. 4**

### Similar content being viewed by others

### [Erdős–Szekeres-Type Problems in the Real Projective Plane][9]

Article 09 September 2024

### [On Erdős–Szekeres-Type Problems for k-convex Point Sets][10]

Chapter © 2019

### [Holes in 2-Convex Point Sets][11]

Chapter © 2018

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Combinatorics][12]
- [Combinatorial Geometry][13]
- [Convex and Discrete Geometry][14]
- [Geometry][15]
- [Number Theory][16]
- [Polytopes][17]
- [Combinatorial Structures and Intersection Theorems][18]

## Notes

1.

The name was coined by Paul Erdős, since the original problem posed for \(m=4\) and \(n=5\) by Esther Klein led to her marriage to George Szekeres.

2.

This is the standard input format for SAT solvers.

3.

The patch was taken from the SAT 2014 competition website [http://www.satcompetition.org/2014/description.shtml][19].

## References

1.

Aehlig, K., Haftmann, F., Nipkow, T.: A compiled implementation of normalization by evaluation. In: Mohamed, O.A., Munoz, C., Tahar, S. (eds.) Theorem Proving in Higher Order Logics (TPHOLs 2008), LNCS, vol. 5170, pp. 39–54. Springer, Berlin (2008)

[Chapter][20] [Google Scholar][21]

2.

Avigad, J., Harrison, J.: Formally verified mathematics. Commun. ACM **57**(4), 66–75 (2014)

[Article][22] [Google Scholar][23]

3.

Ballarin, C.: Interpretation of locales in Isabelle: theories and proof contexts. In: Proceedings of Mathematical Knowledge Management, MKM, pp. 31–43 (2006)

4.

Biere, A., Biere, A., Heule, M., van Maaren, H., Walsh, T.: Handbook of Satisfiability. IOS Press, Amsterdam (2009)

[MATH][24] [Google Scholar][25]

5.

Bonnice, W.E.: On convex polygons determined by a finite planar set. Am. Math. Mon. **81**, 749752 (1974)

[Article][26] [MathSciNet][27] [MATH][28] [Google Scholar][29]

6.

Cruz-Filipe, L., Marques-Silva, J., Schneider-Kamp, P.: Efficient certified resolution proof checking. In: Proceedings of Automated Deduction—CADE-26—26th International Conference on Automated Deduction, Gothenburg, Sweden, LNCS. Springer (2017)

7.

Dehnhardt, K., Harborth, H., Längi, Z.: A partial proof of the Erdős–Szekeres conjecture for hexagons. J. Pure Appl. Math. Adv. Appl. **2**, 6986 (2009)

[MATH][30] [Google Scholar][31]

8.

Erdős, P., Szekeres, G.: A combinatorial problem in geometry. Compos. Math. **2**, 463–470 (1935)

[MathSciNet][32] [MATH][33] [Google Scholar][34]

9.

Hales, T.C. (ed.): Notices of the AMS: Special Issue on Formal Proof, vol. 55(11). American Mathematical Society (2008)

10.

Harrison, J.: HOL light: a tutorial introduction. In: Proceedings of Formal Methods in Computer-Aided Design, First International Conference, FMCAD’96, Palo Alto, California, USA, pp. 265–269 (1996)

11.

Hölldobler, S., Manthey, N., Philipp, T., Steinke, P.: Generic CDCL—a formalization of modern propositional satisfiability solvers. In: POS@ SAT, pp. 89–102 (2014)

12.

Huet, G., Herbelin, H.: 30 years of research and development around Coq. In: Principles of Programming Languages, POPL, pp. 249–250 (2014)

13.

Kalbfleisch, J.D., Kalbfleisch, J.G., Stanton, R.G.: A combinatorial problem on convex n-gons. In: Proceedings of Louisiana Conference on Combinational Graph Theory Computing, Louisiana State University, Baton Rouge (1970)

14.

Knuth, D.E.: Axioms and Hulls, LNCS, vol. 606. Springer, Berlin (1992)

[Book][35] [MATH][36] [Google Scholar][37]

15.

Lammich, P.: Efficient verified (un)sat certificate checking. In: Proceedings of Automated Deduction—CADE-26—26th International Conference on Automated Deduction, Gothenburg, Sweden, LNCS. Springer (2017)

16.

Marić, F.: Formalization and implementation of modern SAT solvers. J. Autom. Reason. **43**(1), 81–119 (2009)

[Article][38] [MathSciNet][39] [MATH][40] [Google Scholar][41]

17.

Marić, F.: Formal verification of a modern SAT solver by shallow embedding into Isabelle/HOL. Theor. Comput. Sci. **411**(50), 4333–4356 (2010)

[Article][42] [MathSciNet][43] [MATH][44] [Google Scholar][45]

18.

Marić, F.: A survey of interactive theorem proving. Zb. Rad. **18**, 173–223 (2015)

[MathSciNet][46] [Google Scholar][47]

19.

Morris, W., Soltan, V.: The Erdős–Szekeres problem on points in convex position—a survey. Bull. Am. Math. Soc. **37**, 437–458 (2000)

[Article][48] [MATH][49] [Google Scholar][50]

20.

Morris, W., Soltan, V.: The Erdős–Szekeres Problem. Springer, Cham (2016)

[MATH][51] [Google Scholar][52]

21.

Nipkow, T., Paulson, L.C., Wenzel, M.: Isabelle/HOL—A Proof Assistant for Higher-Order Logic, LNCS, vol. 2283. Springer (2002)

22.

Pichardie, D., Bertot, Y.: Formalizing convex hull algorithms. In: Boulton, R.J., Jackson, P.B. (eds.) Proceedings of Theorem Proving in Higher Order Logics: 14th International Conference, TPHOLs 2001 Edinburgh, Scotland, UK, pp. 346–361. Springer, Berlin (2001)

23.

Shankar, N., Vaucher, M.: The mechanical verification of a DPLL-based satisfiability solver. Electron. Notes Theor. Comput. Sci. **269**, 3–17 (2011)

[Article][53] [MathSciNet][54] [MATH][55] [Google Scholar][56]

24.

Suk, A.: On the Erdős-Szekeres convex polygon problem. J. Am. Math. Soc. **30**, 1047–1053 (2017)

[Article][57] [MATH][58] [Google Scholar][59]

25.

Szekeres, G., Peters, L.: Computer solution to the 17-point Erdős–Szekeres problem. ANZIAM J. **48**(2), 151–164 (2006)

[Article][60] [MathSciNet][61] [MATH][62] [Google Scholar][63]

26.

Weber, T.: Efficiently checking propositional resolution proofs in Isabelle/HOL. In: Benzmüller, C., Fischer, B., Sutcliffe, G. (eds.) Proceedings of the 6th International Workshop on the Implementation of Logics, CEUR Workshop Proceedings, vol. 212, pp. 44–62 (2006)

27.

Weber, T.: Integrating a SAT solver with an LCF-style theorem prover. Electr. Notes Theor. Comput. Sci. **144**(2), 67–78 (2006)

[Article][64] [MATH][65] [Google Scholar][66]

28.

Wenzel, M.: Isabelle/Isar—a generic framework for human-readable proof documents. In: Matuszewski, R., Zalewska, A. (eds.) From Insight to Proof—Festschrift in Honour of Andrzej Trybulec, Studies in Logic, Grammar, and Rhetoric, vol. 10(23). University of Bialystok (2007)

29.

Wetzler, N., Heule, M.J.H., Hunt, W.A.: Drat-trim: Efficient checking and trimming using expressive clausal proofs. In: Sinz, C., Egly, U. (eds.) Theory and Applications of Satisfiability Testing—SAT 2014: 17th International Conference, Held as Part of the Vienna Summer of Logic, VSL 2014, Vienna, Austria, Proceedings, pp. 422–429. Springer, Cham (2014)

30.

Wetzler, N.D., et al.: Efficient, mechanically-verified validation of satisfiability solvers. Ph.D. thesis, University of Texas, Austin, USA (2015)

[Download references][67]

## Author information

### Authors and Affiliations

1.

Faculty of Mathematics, University of Belgrade, Studentski Trg 16, Belgrade, Serbia

Filip Marić

Authors

1. Filip Marić

[View author publications][68]

Search author on: [PubMed][69] [Google Scholar][70]

### Corresponding author

Correspondence to [Filip Marić][71].

## Additional information

This work has been partially supported by the Grant 174021 of the Ministry of Science of Serbia.

## Rights and permissions

[Reprints and permissions][72]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [73]

### Cite this article

Marić, F. Fast Formal Proof of the Erdős–Szekeres Conjecture for Convex Polygons with at Most 6 Points. *J Autom Reasoning***62**, 301–329 (2019). https://doi.org/10.1007/s10817-017-9423-7

[Download citation][74]

-

Received: 01 April 2017

-

Accepted: 27 July 2017

-

Published: 05 September 2017

-

Issue date: 15 March 2019

-

DOI: https://doi.org/10.1007/s10817-017-9423-7

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Erdős–Szekeres conjecture][75]
- [Happy ending problem][76]
- [Convex polygons][77]
- [Interactive theorem proving][78]
- [SAT solving][79]
- [Isabelle/HOL][80]


## Links

[1]: /article/10.1007/s10817-017-9423-7/save-research?_csrf=U8yqIpTcoqB4nAPPW3yNhxVcu35qxeCr
[2]: /saved-research
[3]: /journal/10817
[4]: /journal/10817/aims-and-scope
[5]: https://submission.nature.com/new-submission/10817/3
[6]: //wayf.springernature.com?redirect_uri#x3D;https%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2Fs10817-017-9423-7%3Ferror%3Dcookies_not_supported%26code%3D6fa25915-3d0f-48cb-b207-ba6059df0c01
[7]: https://link.springer.com/product/springer-plus
[8]: https://www.springernature.com/gp/librarians/licensing/agc/journals
[9]: https://link.springer.com/10.1007/s00454-024-00691-5?fromPaywallRec=true
[10]: https://link.springer.com/10.1007/978-3-030-25005-8_4?fromPaywallRec=true
[11]: https://link.springer.com/10.1007/978-3-319-78825-8_14?fromPaywallRec=true
[12]: /subjects/combinatorics
[13]: /subjects/combinatorial-geometry
[14]: /subjects/convex-and-discrete-geometry
[15]: /subjects/geometry
[16]: /subjects/number-theory
[17]: /subjects/polytopes
[18]: /subjects/combinatorial-structures-and-intersection-theorems
[19]: http://www.satcompetition.org/2014/description.shtml
[20]: https://link.springer.com/doi/10.1007/978-3-540-71067-7_8
[21]: http://scholar.google.com/scholar_lookup?amp;title=A%20compiled%20implementation%20of%20normalization%20by%20evaluation&amp;doi=10.1007%2F978-3-540-71067-7_8&amp;pages=39-54&amp;publication_year=2008&amp;author=Aehlig%2CK&amp;author=Haftmann%2CF&amp;author=Nipkow%2CT
[22]: https://doi.org/10.1145%2F2591012
[23]: http://scholar.google.com/scholar_lookup?amp;title=Formally%20verified%20mathematics&amp;journal=Commun.%20ACM&amp;doi=10.1145%2F2591012&amp;volume=57&amp;issue=4&amp;pages=66-75&amp;publication_year=2014&amp;author=Avigad%2CJ&amp;author=Harrison%2CJ
[24]: http://www.emis.de/MATH-item?1183.68568
[25]: http://scholar.google.com/scholar_lookup?amp;title=Handbook%20of%20Satisfiability&amp;publication_year=2009&amp;author=Biere%2CA&amp;author=Biere%2CA&amp;author=Heule%2CM&amp;author=Maaren%2CH&amp;author=Walsh%2CT
[26]: https://doi.org/10.1080%2F00029890.1974.11993658
[27]: http://www.ams.org/mathscinet-getitem?mr=355827
[28]: http://www.emis.de/MATH-item?0295.52002
[29]: http://scholar.google.com/scholar_lookup?amp;title=On%20convex%20polygons%20determined%20by%20a%20finite%20planar%20set&amp;journal=Am.%20Math.%20Mon.&amp;doi=10.1080%2F00029890.1974.11993658&amp;volume=81&amp;publication_year=1974&amp;author=Bonnice%2CWE
[30]: http://www.emis.de/MATH-item?1187.52015
[31]: http://scholar.google.com/scholar_lookup?amp;title=A%20partial%20proof%20of%20the%20Erd%C5%91s%E2%80%93Szekeres%20conjecture%20for%20hexagons&amp;journal=J.%20Pure%20Appl.%20Math.%20Adv.%20Appl.&amp;volume=2&amp;publication_year=2009&amp;author=Dehnhardt%2CK&amp;author=Harborth%2CH&amp;author=L%C3%A4ngi%2CZ
[32]: http://www.ams.org/mathscinet-getitem?mr=1556929
[33]: http://www.emis.de/MATH-item?0012.27010
[34]: http://scholar.google.com/scholar_lookup?amp;title=A%20combinatorial%20problem%20in%20geometry&amp;journal=Compos.%20Math.&amp;volume=2&amp;pages=463-470&amp;publication_year=1935&amp;author=Erd%C5%91s%2CP&amp;author=Szekeres%2CG
[35]: https://link.springer.com/doi/10.1007/3-540-55611-7
[36]: http://www.emis.de/MATH-item?0777.68012
[37]: http://scholar.google.com/scholar_lookup?amp;title=Axioms%20and%20Hulls%2C%20LNCS&amp;doi=10.1007%2F3-540-55611-7&amp;publication_year=1992&amp;author=Knuth%2CDE
[38]: https://link.springer.com/doi/10.1007/s10817-009-9127-8
[39]: http://www.ams.org/mathscinet-getitem?mr=2507216
[40]: http://www.emis.de/MATH-item?1187.68557
[41]: http://scholar.google.com/scholar_lookup?amp;title=Formalization%20and%20implementation%20of%20modern%20SAT%20solvers&amp;journal=J.%20Autom.%20Reason.&amp;doi=10.1007%2Fs10817-009-9127-8&amp;volume=43&amp;issue=1&amp;pages=81-119&amp;publication_year=2009&amp;author=Mari%C4%87%2CF
[42]: https://doi.org/10.1016%2Fj.tcs.2010.09.014
[43]: http://www.ams.org/mathscinet-getitem?mr=2779359
[44]: http://www.emis.de/MATH-item?1208.68205
[45]: http://scholar.google.com/scholar_lookup?amp;title=Formal%20verification%20of%20a%20modern%20SAT%20solver%20by%20shallow%20embedding%20into%20Isabelle%2FHOL&amp;journal=Theor.%20Comput.%20Sci.&amp;doi=10.1016%2Fj.tcs.2010.09.014&amp;volume=411&amp;issue=50&amp;pages=4333-4356&amp;publication_year=2010&amp;author=Mari%C4%87%2CF
[46]: http://www.ams.org/mathscinet-getitem?mr=3467966
[47]: http://scholar.google.com/scholar_lookup?amp;title=A%20survey%20of%20interactive%20theorem%20proving&amp;journal=Zb.%20Rad.&amp;volume=18&amp;pages=173-223&amp;publication_year=2015&amp;author=Mari%C4%87%2CF
[48]: https://doi.org/10.1090%2FS0273-0979-00-00877-6
[49]: http://www.emis.de/MATH-item?0958.52018
[50]: http://scholar.google.com/scholar_lookup?amp;title=The%20Erd%C5%91s%E2%80%93Szekeres%20problem%20on%20points%20in%20convex%20position%E2%80%94a%20survey&amp;journal=Bull.%20Am.%20Math.%20Soc.&amp;doi=10.1090%2FS0273-0979-00-00877-6&amp;volume=37&amp;pages=437-458&amp;publication_year=2000&amp;author=Morris%2CW&amp;author=Soltan%2CV
[51]: http://www.emis.de/MATH-item?1356.52008
[52]: http://scholar.google.com/scholar_lookup?amp;title=The%20Erd%C5%91s%E2%80%93Szekeres%20Problem&amp;publication_year=2016&amp;author=Morris%2CW&amp;author=Soltan%2CV
[53]: https://doi.org/10.1016%2Fj.entcs.2011.03.002
[54]: http://www.ams.org/mathscinet-getitem?mr=2911448
[55]: http://www.emis.de/MATH-item?1347.68307
[56]: http://scholar.google.com/scholar_lookup?amp;title=The%20mechanical%20verification%20of%20a%20DPLL-based%20satisfiability%20solver&amp;journal=Electron.%20Notes%20Theor.%20Comput.%20Sci.&amp;doi=10.1016%2Fj.entcs.2011.03.002&amp;volume=269&amp;pages=3-17&amp;publication_year=2011&amp;author=Shankar%2CN&amp;author=Vaucher%2CM
[57]: https://doi.org/10.1090%2Fjams%2F869
[58]: http://www.emis.de/MATH-item?1370.52032
[59]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20Erd%C5%91s-Szekeres%20convex%20polygon%20problem&amp;journal=J.%20Am.%20Math.%20Soc.&amp;doi=10.1090%2Fjams%2F869&amp;volume=30&amp;pages=1047-1053&amp;publication_year=2017&amp;author=Suk%2CA
[60]: https://doi.org/10.1017%2FS144618110000300X
[61]: http://www.ams.org/mathscinet-getitem?mr=2291511
[62]: http://www.emis.de/MATH-item?1152.52008
[63]: http://scholar.google.com/scholar_lookup?amp;title=Computer%20solution%20to%20the%2017-point%20Erd%C5%91s%E2%80%93Szekeres%20problem&amp;journal=ANZIAM%20J.&amp;doi=10.1017%2FS144618110000300X&amp;volume=48&amp;issue=2&amp;pages=151-164&amp;publication_year=2006&amp;author=Szekeres%2CG&amp;author=Peters%2CL
[64]: https://doi.org/10.1016%2Fj.entcs.2005.12.007
[65]: http://www.emis.de/MATH-item?1272.68366
[66]: http://scholar.google.com/scholar_lookup?amp;title=Integrating%20a%20SAT%20solver%20with%20an%20LCF-style%20theorem%20prover&amp;journal=Electr.%20Notes%20Theor.%20Comput.%20Sci.&amp;doi=10.1016%2Fj.entcs.2005.12.007&amp;volume=144&amp;issue=2&amp;pages=67-78&amp;publication_year=2006&amp;author=Weber%2CT
[67]: https://citation-needed.springer.com/v2/references/10.1007/s10817-017-9423-7?format=refman&amp;flavour=references
[68]: /search?sortBy=newestFirst&amp;contributor=Filip%20Mari%C4%87
[69]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Filip%20Mari%C4%87
[70]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Filip%20Mari%C4%87%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[71]: mailto:filip@matf.bg.ac.rs
[72]: https://s100.copyright.com/AppDispatchServlet?title=Fast%20Formal%20Proof%20of%20the%20Erd%C5%91s%E2%80%93Szekeres%20Conjecture%20for%20Convex%20Polygons%20with%20at%20Most%206%20Points&amp;author=Filip%20Mari%C4%87&amp;contentID=10.1007%2Fs10817-017-9423-7&amp;copyright=Springer%20Science%2BBusiness%20Media%20B.V.&amp;publication=0168-7433&amp;publicationDate=2017-09-05&amp;publisherName=SpringerNature&amp;orderBeanReset=true
[73]: https://crossmark.crossref.org/dialog/?doi=10.1007/s10817-017-9423-7
[74]: https://citation-needed.springer.com/v2/references/10.1007/s10817-017-9423-7?format=refman&amp;flavour=citation
[75]: /search?query=Erd%C5%91s%E2%80%93Szekeres%20conjecture&amp;facet-discipline=#34;Computer%20Science&#34;
[76]: /search?query=Happy%20ending%20problem&amp;facet-discipline=#34;Computer%20Science&#34;
[77]: /search?query=Convex%20polygons&amp;facet-discipline=#34;Computer%20Science&#34;
[78]: /search?query=Interactive%20theorem%20proving&amp;facet-discipline=#34;Computer%20Science&#34;
[79]: /search?query=SAT%20solving&amp;facet-discipline=#34;Computer%20Science&#34;
[80]: /search?query=Isabelle%2FHOL&amp;facet-discipline=#34;Computer%20Science&#34;
