<!-- source: https://en.wikipedia.org/wiki/Hilbert%27s_seventeenth_problem | converted from HTML -->

Hilbert's seventeenth problem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Expression of polynomials as sum of squares

**Hilbert's seventeenth problem**is one of the 23 of [Hilbert's problems][1] set out in a celebrated list compiled in 1900 by [David Hilbert][2]. It concerns the expression of [positive definite][3] [rational functions][4] as [sums][5] of [quotients][6] of [squares][7]. The original question may be reformulated as:

- Given a multivariate polynomial that takes only non-negative values over the reals, can it be represented as a sum of squares of rational functions?

Hilbert's question can be restricted to [homogeneous polynomials][8] of even degree, since a polynomial of odd degree changes sign, and the [homogenization of a polynomial][9] takes only nonnegative values if and only if the same is true for the polynomial.

## Original statement

[[edit][10]]

In one English translation, Hilbert's seventeenth problem is stated as follows: [1]

A rational integral function or form in any number of variables with real coefficients such that it becomes negative for no real values of these variables, is said to be definite. The system of all definite forms is invariant with respect to the operations of addition and multiplication, but the quotient of two definite forms—in case it should be an integral function of the variables—is also a definite form. The square of any form is evidently always a definite form. But since, as I have shown, [2] not every definite form can be compounded by addition from squares of forms, the question arises—which I have answered affirmatively for ternary forms [3] —whether every definite form may not be expressed as a quotient of sums of squares of forms. At the same time it is desirable, for certain questions as to the possibility of certain geometrical constructions, to know whether the coefficients of the forms to be used in the expression may always be taken from the realm of rationality given by the coefficients of the form represented.

## Motivation

[[edit][11]]

Main article: [Polynomial SOS][12]

The formulation of the question takes into account that there are [non-negative polynomials][13], for example [4]

f ( x, y, z) = z 6 + x 4 y 2 + x 2 y 4 − 3 x 2 y 2 z 2, {\displaystyle f(x,y,z)=z^{6}+x^{4}y^{2}+x^{2}y^{4}-3x^{2}y^{2}z^{2},}[image: {\displaystyle f(x,y,z)=z^{6}+x^{4}y^{2}+x^{2}y^{4}-3x^{2}y^{2}z^{2},}]

which cannot be represented as a [sum of squares of other polynomials][12]. In 1888, Hilbert showed that every non-negative homogeneous polynomial in *n*variables and degree 2*d*can be represented as sum of squares of other polynomials if and only if either (a) *n*= 2 or (b) 2*d*= 2 or (c) *n*= 3 and 2*d*= 4. [2] Hilbert's proof did not exhibit any explicit counterexample: only in 1967 the first explicit counterexample was constructed by [Motzkin][14]. [5] Furthermore, if the polynomial has a degree 2*d*greater than two, there are significantly many more non-negative polynomials that cannot be expressed as sums of squares. [6]

The following table summarizes in which cases every non-negative homogeneous polynomial (or a polynomial of even degree) can be represented as a sum of squares:

**Any homogeneous polynomial of degree 2*d*and *n*variables can be represented as sum of squares?** | 2*d*(Degree) |  | **Any polynomial of degree 2*d*and *n*variables can be represented as sum of squares?** | 2*d*(Degree) |

2 | 4 | ≥6 | 2 | 4 | ≥6 |

*n*(Number of variables) | 1 | Yes | Yes | Yes | *n*(Number of variables) | 1 | Yes | Yes | Yes |

2 | Yes | Yes | Yes | 2 | Yes | Yes | No |

3 | Yes | Yes | No | 3 | Yes | No | No |

≥4 | Yes | No | No | ≥4 | Yes | No | No |

## Solution and generalizations

[[edit][15]]

The particular case of *n*= 2 was already solved by Hilbert in 1893. [3] The general problem was solved in the affirmative, in 1927, by [Emil Artin][16], [7] for positive semidefinite functions over the reals or more generally [real-closed fields][17]. An algorithmic solution was found by [Charles Delzell][18] in 1984. [8] A result of [Albrecht Pfister][19] [9] shows that a positive semidefinite form in *n*variables can be expressed as a sum of 2*n*squares. [10]

Dubois showed in 1967 that the answer is negative in general for [ordered fields][20]. [11] In this case one can say that a positive polynomial is a sum of weighted squares of rational functions with positive coefficients. [12] McKenna showed in 1975 that all positive semidefinite polynomials with coefficients in an ordered field are sums of weighted squares of rational functions with positive coefficients only if the field is dense in its real closure in the sense that any interval with endpoints in the real closure contains elements from the original field. [13]

A generalization to the matrix case (matrices with polynomial function entries that are always positive semidefinite can be expressed as sum of squares of symmetric matrices with rational function entries) was given by Gondard, [Ribenboim][21] [14] and Procesi, Schacher, [15] with an [elementary proof][22] given by Hillar and Nie. [16]

In [complex analysis][23] and [complex geometry][24], the Hermitian analogue, requiring the squares to be squared norms of holomorphic polynomials, was proven for strictly positive polynomials by [Quillen][25] using techniques based on [elliptic partial differential equations][26]. [17] The sum-of-squares representation is unique if it exists, which was first observed by Putinar in the context of optimization. [18]

## Minimum number of square rational terms

[[edit][27]]

Unsolved problem in mathematics

What is the minimum number of rational functions needed to represent any non-negative n-variate, degree d polynomial?

[More unsolved problems in mathematics][28]

It is an open question what is the smallest number

v ( n, d), {\displaystyle v(n,d),}[image: {\displaystyle v(n,d),}]

such that any *n*-variate, non-negative polynomial of degree *d*can be written as sum of at most v ( n, d) {\displaystyle v(n,d)}[image: {\displaystyle v(n,d)}] square rational functions over the reals. An [upper bound][29] due to Pfister in 1967 is: [9]

v ( n, d) ≤ 2 n, {\displaystyle v(n,d)\leq 2^{n},}[image: {\displaystyle v(n,d)\leq 2^{n},}]

In the other direction, a conditional lower bound can be derived from [computational complexity theory][30]. An *n*-variable instance of [3-SAT][31] can be realized as a positivity problem on a polynomial with *n*variables and *d=4*. This proves that positivity testing is [NP-hard][32]. More precisely, assuming the [exponential time hypothesis][33] to be true, v ( n, d) = 2 Ω ( n) {\displaystyle v(n,d)=2^{\Omega (n)}}[image: {\displaystyle v(n,d)=2^{\Omega (n)}}].

The result of Pfister fails in the Hermitian case, that is there is no bound on the number of squares required, see D'Angelo–Lebl. [19]

## See also

[[edit][34]]

- [Krivine–Stengle Positivstellensatz][35]
- [Polynomial SOS][12]
- [Positive polynomial][13]
- [Sum-of-squares optimization][36]
- [SOS-convexity][37]

## Notes

[[edit][38]]

1. ↑ Hilbert, David, "Mathematische Probleme" [Göttinger Nachrichten][39], (1900), pp. 253–297, and in [Archiv der Mathematik und Physik][40], (3) **1**(1901), 44–63 and 213–237. Published in English translation by Dr. Maby Winton Newson, [Hilbert, David][2] (1902). ["Mathematical Problems"][41]. *[Bulletin of the American Mathematical Society][42]*. **8**(10): 437– 479. [doi][43]: [10.1090/S0002-9904-1902-00923-3][41].. [A fuller title of the journal Göttinger Nachrichten is Nachrichten von der Königl. Gesellschaft der Wiss. zu Göttingen.]
2. 1 2 Hilbert, David (September 1888). ["Ueber die Darstellung definiter Formen als Summe von Formenquadraten"][44]. *Mathematische Annalen*. **32**(3): 342– 350. [doi][43]: [10.1007/bf01443605][45]. [S2CID][46] [177804714][47].
3. 1 2 Hilbert, David (December 1893). ["Über ternäre definite Formen"][48]. *Acta Mathematica*. **17**(1): 169– 197. [doi][43]: [10.1007/bf02391990][49].
4. ↑ [Marie-Françoise Roy][50]. The role of Hilbert's problems in real algebraic geometry. Proceedings of the ninth EWM Meeting, Loccum, Germany 1999
5. ↑ Motzkin, T. S. (1967). "The arithmetic-geometric inequality". In Shisha, Oved (ed.). *Inequalities*. Academic Press. pp. 205– 224.
6. ↑ Blekherman, Grigoriy (2006). ["There are significantly more nonegative polynomials than sums of squares"][51]. *[Israel Journal of Mathematics][52]*. **153**(1): 355– 380. [doi][43]: [10.1007/BF02771790][51]. [ISSN][53] [0021-2172][54].
7. ↑ Artin, Emil (1927). "Über die Zerlegung definiter Funktionen in Quadrate". *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg*. **5**(1): 100– 115. [doi][43]: [10.1007/BF02952513][55]. [S2CID][46] [122607428][56].
8. ↑ Delzell, C.N. (1984). "A continuous, constructive solution to Hilbert's 17th problem". *[Inventiones Mathematicae][57]*. **76**(3): 365– 384. [Bibcode][58]: [1984InMat..76..365D][59]. [doi][43]: [10.1007/BF01388465][60]. [S2CID][46] [120884276][61]. [Zbl][62] [0547.12017][63].
9. 1 2 [Pfister, Albrecht][19] (1967). "Zur Darstellung definiter Funktionen als Summe von Quadraten". *[Inventiones Mathematicae][57]*(in German). **4**(4): 229– 237. [Bibcode][58]: [1967InMat...4..229P][64]. [doi][43]: [10.1007/bf01425382][65]. [S2CID][46] [122180608][66]. [Zbl][62] [0222.10022][67].
10. ↑ Lam (2005) p.391
11. ↑ Dubois, D.W. (1967). ["Note on Artin's solution of Hilbert's 17th problem"][68]. *Bull. Am. Math. Soc*. **73**(4): 540– 541. [doi][43]: [10.1090/s0002-9904-1967-11736-1][68]. [Zbl][62] [0164.04502][69].
12. ↑ Lorenz (2008) p.16
13. ↑ McKenna, K. (1975). *New facts about Hilbert's seventeenth problem*. Model Theory and Algebra, Lecture Notes in Mathematics. Vol. 498. Springer, Berlin, Heidelberg. pp. 220– 230.
14. ↑ Gondard, Danielle; [Ribenboim, Paulo][21] (1974). "Le 17e problème de Hilbert pour les matrices". *Bull. Sci. Math. (2)*. **98**(1): 49– 56. [MR][70] [0432613][71]. [Zbl][62] [0298.12104][72].
15. ↑ Procesi, Claudio; Schacher, Murray (1976). "A non-commutative real Nullstellensatz and Hilbert's 17th problem". *Ann. of Math*. 2. **104**(3): 395– 406. [doi][43]: [10.2307/1970962][73]. [JSTOR][74] [1970962][75]. [MR][70] [0432612][76]. [Zbl][62] [0347.16010][77].
16. ↑ Hillar, Christopher J.; Nie, Jiawang (2008). "An elementary and constructive solution to Hilbert's 17th problem for matrices". *Proc. Am. Math. Soc*. **136**(1): 73– 76. [arXiv][78]: [math/0610388][79]. [doi][43]: [10.1090/s0002-9939-07-09068-5][80]. [S2CID][46] [119639574][81]. [Zbl][62] [1126.12001][82].
17. ↑ Quillen, Daniel G. (1968). "On the representation of hermitian forms as sums of squares". *Invent. Math*. **5**(4): 237– 242. [Bibcode][58]: [1968InMat...5..237Q][83]. [doi][43]: [10.1007/bf01389773][84]. [S2CID][46] [119774934][85]. [Zbl][62] [0198.35205][86].
18. ↑ Putinar, Mihai (2012). "Chapter 9: Sums of Hermitian Squares: Old and New". **[Semidefinite Optimization and Convex Algebraic Geometry][87]. Philadelphia, PA: Society for Industrial and Applied Mathematics. p. 407–446. [doi][43]: [10.1137/1.9781611972290.ch9][88]. [ISBN][89] [978-1-61197-228-3][90]. Retrieved 2025-12-16.
19. ↑ [D'Angelo, John P.][91]; Lebl, Jiri (2012). "Pfister's theorem fails in the Hermitian case". *Proc. Am. Math. Soc*. **140**(4): 1151– 1157. [arXiv][78]: [1010.3215][92]. [doi][43]: [10.1090/s0002-9939-2011-10841-4][93]. [S2CID][46] [92993604][94]. [Zbl][62] [1309.12001][95].

## References

[[edit][96]]

- [Pfister, Albrecht][19] (1976). "Hilbert's seventeenth problem and related problems on definite forms". In [Felix E. Browder][97] (ed.). *Mathematical Developments Arising from Hilbert Problems*. [Proceedings of Symposia in Pure Mathematics][98]. Vol. XXVIII.2. [American Mathematical Society][99]. pp. 483– 489. [ISBN][89] [0-8218-1428-1][100].
- [Lam, Tsit-Yuen][101] (2005). *Introduction to Quadratic Forms over Fields*. [Graduate Studies in Mathematics][102]. Vol. 67. American Mathematical Society. [ISBN][89] [0-8218-1095-2][103]. [Zbl][62] [1068.11023][104].
- Lorenz, Falko (2008). *Algebra. Volume II: Fields with Structure, Algebras and Advanced Topics*. [Springer-Verlag][105]. pp. 15– 27. [ISBN][89] [978-0-387-72487-4][106]. [Zbl][62] [1130.12001][107].
- Rajwade, A. R. (1993). *Squares*. London Mathematical Society Lecture Note Series. Vol. 171. [Cambridge University Press][108]. [ISBN][89] [0-521-42668-5][109]. [Zbl][62] [0785.11022][110].

- [v][111]
- [t][112]
- [e][113]

[Hilbert's problems][1]

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

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Hilbert%27s_seventeenth_problem&oldid=1369579819][138] "

[Categories][139]:

- [Real algebraic geometry][140]
- [Hilbert's problems][141]

Hidden categories:

- [Articles with short description][142]
- [Short description is different from Wikidata][143]
- [CS1 German-language sources (de)][144]
- [CS1: long volume value][145]

Search

Hilbert's seventeenth problem

9 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Hilbert's_problems
[2]: https://en.wikipedia.org/wiki/David_Hilbert
[3]: https://en.wikipedia.org/wiki/Positive-definite_function
[4]: https://en.wikipedia.org/wiki/Rational_function
[5]: https://en.wikipedia.org/wiki/Summation
[6]: https://en.wikipedia.org/wiki/Quotient
[7]: https://en.wikipedia.org/wiki/Square_(algebra)
[8]: https://en.wikipedia.org/wiki/Homogeneous_polynomial
[9]: https://en.wikipedia.org/wiki/Homogenization_of_a_polynomial
[10]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=1
[11]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=2
[12]: https://en.wikipedia.org/wiki/Polynomial_SOS
[13]: https://en.wikipedia.org/wiki/Positive_polynomial
[14]: https://en.wikipedia.org/wiki/Theodore_Motzkin
[15]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=3
[16]: https://en.wikipedia.org/wiki/Emil_Artin
[17]: https://en.wikipedia.org/wiki/Real-closed_field
[18]: https://en.wikipedia.org/wiki/Charles_Neal_Delzell?action=edit&amp;redlink=1
[19]: https://en.wikipedia.org/wiki/Albrecht_Pfister_(mathematician)
[20]: https://en.wikipedia.org/wiki/Ordered_field
[21]: https://en.wikipedia.org/wiki/Paulo_Ribenboim
[22]: https://en.wikipedia.org/wiki/Elementary_proof
[23]: https://en.wikipedia.org/wiki/Complex_analysis
[24]: https://en.wikipedia.org/wiki/Complex_geometry
[25]: https://en.wikipedia.org/wiki/Daniel_Quillen
[26]: https://en.wikipedia.org/wiki/Elliptic_partial_differential_equation
[27]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=4
[28]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[29]: https://en.wikipedia.org/wiki/Upper_bound
[30]: https://en.wikipedia.org/wiki/Computational_complexity_theory
[31]: https://en.wikipedia.org/wiki/3-SAT
[32]: https://en.wikipedia.org/wiki/NP-hard
[33]: https://en.wikipedia.org/wiki/Exponential_time_hypothesis
[34]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=5
[35]: https://en.wikipedia.org/wiki/Krivine–Stengle_Positivstellensatz
[36]: https://en.wikipedia.org/wiki/Sum-of-squares_optimization
[37]: https://en.wikipedia.org/wiki/SOS-convexity
[38]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=6
[39]: https://en.wikipedia.org/wiki/Göttinger_Nachrichten?action=edit&amp;redlink=1
[40]: https://en.wikipedia.org/wiki/Archiv_der_Mathematik_und_Physik?action=edit&amp;redlink=1
[41]: https://doi.org/10.1090%2FS0002-9904-1902-00923-3
[42]: https://en.wikipedia.org/wiki/Bulletin_of_the_American_Mathematical_Society
[43]: https://en.wikipedia.org/wiki/Doi_(identifier)
[44]: https://zenodo.org/record/1428214
[45]: https://doi.org/10.1007%2Fbf01443605
[46]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[47]: https://api.semanticscholar.org/CorpusID:177804714
[48]: https://zenodo.org/record/1428402
[49]: https://doi.org/10.1007%2Fbf02391990
[50]: https://en.wikipedia.org/wiki/Marie-Françoise_Roy
[51]: https://doi.org/10.1007%2FBF02771790
[52]: https://en.wikipedia.org/wiki/Israel_Journal_of_Mathematics
[53]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[54]: https://search.worldcat.org/issn/0021-2172
[55]: https://doi.org/10.1007%2FBF02952513
[56]: https://api.semanticscholar.org/CorpusID:122607428
[57]: https://en.wikipedia.org/wiki/Inventiones_Mathematicae
[58]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[59]: https://ui.adsabs.harvard.edu/abs/1984InMat..76..365D
[60]: https://doi.org/10.1007%2FBF01388465
[61]: https://api.semanticscholar.org/CorpusID:120884276
[62]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[63]: https://zbmath.org/?format=complete&amp;q=an:0547.12017
[64]: https://ui.adsabs.harvard.edu/abs/1967InMat...4..229P
[65]: https://doi.org/10.1007%2Fbf01425382
[66]: https://api.semanticscholar.org/CorpusID:122180608
[67]: https://zbmath.org/?format=complete&amp;q=an:0222.10022
[68]: https://doi.org/10.1090%2Fs0002-9904-1967-11736-1
[69]: https://zbmath.org/?format=complete&amp;q=an:0164.04502
[70]: https://en.wikipedia.org/wiki/MR_(identifier)
[71]: https://mathscinet.ams.org/mathscinet-getitem?mr=0432613
[72]: https://zbmath.org/?format=complete&amp;q=an:0298.12104
[73]: https://doi.org/10.2307%2F1970962
[74]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[75]: https://www.jstor.org/stable/1970962
[76]: https://mathscinet.ams.org/mathscinet-getitem?mr=0432612
[77]: https://zbmath.org/?format=complete&amp;q=an:0347.16010
[78]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[79]: https://arxiv.org/pdf/math/0610388
[80]: https://doi.org/10.1090%2Fs0002-9939-07-09068-5
[81]: https://api.semanticscholar.org/CorpusID:119639574
[82]: https://zbmath.org/?format=complete&amp;q=an:1126.12001
[83]: https://ui.adsabs.harvard.edu/abs/1968InMat...5..237Q
[84]: https://doi.org/10.1007%2Fbf01389773
[85]: https://api.semanticscholar.org/CorpusID:119774934
[86]: https://zbmath.org/?format=complete&amp;q=an:0198.35205
[87]: http://epubs.siam.org/doi/10.1137/1.9781611972290.ch9
[88]: https://doi.org/10.1137%2F1.9781611972290.ch9
[89]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[90]: https://en.wikipedia.org/wiki/Special:BookSources/978-1-61197-228-3
[91]: https://en.wikipedia.org/wiki/John_D'Angelo
[92]: https://arxiv.org/pdf/1010.3215
[93]: https://doi.org/10.1090%2Fs0002-9939-2011-10841-4
[94]: https://api.semanticscholar.org/CorpusID:92993604
[95]: https://zbmath.org/?format=complete&amp;q=an:1309.12001
[96]: /w/index.php?title=Hilbert%27s_seventeenth_problem&amp;action=edit&amp;section=7
[97]: https://en.wikipedia.org/wiki/Felix_Browder
[98]: https://en.wikipedia.org/wiki/Proceedings_of_Symposia_in_Pure_Mathematics
[99]: https://en.wikipedia.org/wiki/American_Mathematical_Society
[100]: https://en.wikipedia.org/wiki/Special:BookSources/0-8218-1428-1
[101]: https://en.wikipedia.org/wiki/Tsit_Yuen_Lam
[102]: https://en.wikipedia.org/wiki/Graduate_Studies_in_Mathematics
[103]: https://en.wikipedia.org/wiki/Special:BookSources/0-8218-1095-2
[104]: https://zbmath.org/?format=complete&amp;q=an:1068.11023
[105]: https://en.wikipedia.org/wiki/Springer-Verlag
[106]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-72487-4
[107]: https://zbmath.org/?format=complete&amp;q=an:1130.12001
[108]: https://en.wikipedia.org/wiki/Cambridge_University_Press
[109]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-42668-5
[110]: https://zbmath.org/?format=complete&amp;q=an:0785.11022
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
[138]: https://en.wikipedia.org/w/index.php?title=Hilbert%27s_seventeenth_problem&amp;oldid=1369579819
[139]: /wiki/Help:Category
[140]: /wiki/Category:Real_algebraic_geometry
[141]: /wiki/Category:Hilbert%27s_problems
[142]: /wiki/Category:Articles_with_short_description
[143]: /wiki/Category:Short_description_is_different_from_Wikidata
[144]: /wiki/Category:CS1_German-language_sources_(de)
[145]: /wiki/Category:CS1:_long_volume_value
