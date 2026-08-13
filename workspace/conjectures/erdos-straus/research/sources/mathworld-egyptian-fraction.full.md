<!-- source: https://mathworld.wolfram.com/EgyptianFraction.html | converted from HTML -->

Egyptian Fraction -- from Wolfram MathWorld

# Egyptian Fraction

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

An Egyptian fraction is a sum of positive (usually) distinct [unit fractions][2]. The famous [Rhind papyrus][3], dated to around 1650 BC contains a table of representations of [image: 2/n] as Egyptian fractions for [odd][4][image: n] between 5 and 101. The reason the Egyptians chose this method for representing fractions is not clear, although Andr&eacute; Weil characterized the decision as "a wrong turn" (Hoffman 1998, pp. 153-154). The unique fraction that the Egyptians did not represent using unit fractions was 2/3 (Wells 1986, p. 29).

Egyptian fractions are almost always required to exclude repeated terms, since representations such as [image: 1/5+1/5+1/5] are trivial. Any [rational number][5] has representations as an Egyptian fraction with arbitrarily many terms and with arbitrarily large [denominators][6], although for a given fixed number of terms, there are only finitely many. Fibonacci proved that *any*fraction can be [represented as][7] a sum of distinct unit fractions (Hoffman 1998, p. 154). An infinite chain of unit fractions can be constructed using the identity

[image:  1/a=1/(a+1)+1/(a(a+1)). ] |

(1)

 |

Martin (1999) showed that for every positive [rational number][5], there exist Egyptian fractions whose largest [denominator][6] is at most [image: N] and whose [denominators][6] form a positive proportion of the integers up to [image: N] for sufficiently large [image: N]. Each [fraction][8][image: x/y] with [image: y] [odd][4] has an Egyptian fraction in which each [denominator][6] is [odd][4] (Breusch 1954; Guy 1994, p. 160). Every [image: x/y] has a [image: t] -term representation where [image: t=O(sqrt(logy))] (Vose 1985).

No algorithm is known for producing unit fraction representations having either a minimum number of terms or smallest possible denominator (Hoffman 1998, p. 155). However, there are a number of [algorithms][9] (including the [binary remainder method][10], [continued fraction unit fraction algorithm][11], generalized remainder method, [greedy algorithm][12], [reverse greedy algorithm][13], [small multiple method][14], and splitting algorithm) for decomposing an arbitrary [fraction][8] into unit fractions. In 1202, Fibonacci published an algorithm for constructing unit fraction representations, and this algorithm was subsequently rediscovered by Sylvester (Hoffman 1998, p. 154; Martin 1999).

Taking the fractions 1/2, 1/3, 2/3, 1/4, 2/4, 3/4, ... (the numerators of which are OEIS [A002260][15], and the denominators of which are [image: n-1] copies of the integer [image: n]), the unit fraction representations using the [greedy algorithm][12] are

[image: 1/2] | [image: =] | [image: 1/2] |

(2)

 |

[image: 1/3] | [image: =] | [image: 1/3] |

(3)

 |

[image: 2/3] | [image: =] | [image: 1/2+1/6] |

(4)

 |

[image: 1/4] | [image: =] | [image: 1/4] |

(5)

 |

[image: 2/4] | [image: =] | [image: 1/2] |

(6)

 |

[image: 3/4] | [image: =] | [image: 1/2+1/4] |

(7)

 |

[image: 1/5] | [image: =] | [image: 1/5] |

(8)

 |

[image: 2/5] | [image: =] | [image: 1/3+1/(15)] |

(9)

 |

[image: 3/5] | [image: =] | [image: 1/2+1/(10)] |

(10)

 |

[image: 4/5] | [image: =] | [image: 1/2+1/4+1/(20).] |

(11)

 |

The number of terms in these representations are 1, 1, 2, 1, 1, 2, 1, 2, 2, 3, 1, ... (OEIS [A050205][16]). The minimum denominators for each representation are given by 2, 3, 2, 4, 2, 2, 5, 3, 2, 2, 6, 3, 2, ... (OEIS [A050206][17]), and the maximum denominators are 2, 3, 6, 4, 2, 4, 5, 15, 10, 20, 6, 3, 2, ... (OEIS [A050210][18]).

The Egyptian fractions for various constants using the [greedy algorithm][12] are summarized in the following table.

constant [image: x] | OEIS | Egyptian fraction for [image: frac(x)] |

[image: sqrt(2)] | [A006487][19] | 3, 13, 253, 218201, 61323543802, ... |

[image: sqrt(3)] | [A118325][20] | 2, 5, 32, 1249, 5986000, 438522193400489, ... |

[image: 2^(-1/2)] | [A069139][21] | 2, 5, 141, 68575, 32089377154, ... |

[image: e] | [A006525][22] | 2, 5, 55, 9999, 3620211523, 25838201785967533906, ... |

[image: e^(-1)] | [A006526][23] | 3, 29, 15786, 513429610, 339840390654894740, ... |

[image: gamma] | [A110820][24] | 2, 13, 3418, 52016149, 153922786652714666, ... |

[image: K] | [A118323][25] | 2, 3, 13, 176, 36543, ... |

[image: phi] | [A117116][26] | 2, 9, 145, 37986, 2345721887, ... |

[image: ln2] | [A118324][27] | 2, 6, 38, 6071, 144715221, ... |

[image: pi] | [A001466][28] | 8, 61, 5020, 128541455, 162924332716605980, ... |

[image: pi^(-1)] | [A006524][29] | 4, 15, 609, 845029, 1010073215739, ... |

Any fraction with odd denominator can be [represented as][7] a finite sum of unit fractions, each having an odd denominator (Starke 1952, Breusch 1954). Graham proved that infinitely many fractions with a certain range can be represented as a sum of units fractions with square denominators (Hoffman 1998, p. 156).

Paul Erdős and E. G. Straus have conjectured that the [Diophantine equation][30]

[image:  4/n=1/a+1/b+1/c ] |

(12)

 |

always can be solved, an assertion sometimes known as the [Erdős-Straus conjecture][31], and Sierpiński (1956) conjectured that

[image:  5/n=1/a+1/b+1/c ] |

(13)

 |

can be solved (Guy 1994).

The [harmonic number][32][image: H_n] is never an [integer][33] except for [image: H_1]. This result was proved in 1915 by Taeisinger, and the more general results that any number of consecutive terms not necessarily starting with 1 never sum to an integer was proved by K&uuml;rsch&aacute;k in 1918 (Hoffman 1998, p. 157). In 1932, Erdős proved that the sum of the reciprocals of any number of equally spaced integers is never a reciprocal.

Nontrivial sets of integers are known whose reciprocals sum to small integers. For example, there exists a set of 366 positive integers (with maximum 992) whose sum of reciprocals is exactly 2 (Mackenzie 1997; Martin). A similar set of 453 small positive integers is known that sums to 6 (Martin).

---

## See also

[Akhmim Wooden Tablet][34], [Egyptian Mathematical Leather Roll][35], [Egyptian Number][36], [Engel Expansion][37], [Erdős-Straus Conjecture][31], [Harmonic Number][32], [Rhind Papyrus][3], [Unit Fraction][2]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [Archimedes' axiom][38]
- [fractions][39]
- [egyptian fraction 3.1415926535897932384626433832795028841971693993751][40]

## References

Beck, A.; Bleicher, M. N.; and Crowe, D. W. *[Excursions into Mathematics.][41]*New York: Worth Publishers, 1970. Beeckmans, L. "The Splitting Algorithm for Egyptian Fractions." *J. Number Th.***43**, 173-185, 1993. Bleicher, M. N. "A New Algorithm for the Expansion of Continued Fractions." *J. Number Th.***4**, 342-382, 1972. Breusch, R. "A Special Case of Egyptian Fractions." Solution to advanced problem 4512. *Amer. Math. Monthly***61**, 200-201, 1954. Eppstein, D. "Ten Algorithms for Egyptian Fractions." *Mathematica Educ. Res.***4**, 5-15, 1995. Eppstein, D. "Egyptian Fractions." [https://ics.uci.edu/~eppstein/numth/egypt/][42]. Eppstein, D. Egypt.ma Mathematica notebook. [https://ics.uci.edu/~eppstein/numth/egypt/egypt.ma][43]. Gardner, M. "Mathematical Games: In Which a Mathematical Aesthetic Is Applied to Modern Minimal Art." *Sci. Amer.***239**, 22-32, Nov. 1978.[image: Update a link] [44] Gardner, M. "Babylonian and Egyptian Mathematics, an Egyptian Historical Gap, Installments 1-3." [http://www.teleport.com/~ddonahue/phresour.html][45] Golomb, S. W. "An Algebraic Algorithm for the Representation Problems of the Ahmes Papyrus." *Amer. Math. Monthly***69**, 785-786, 1962. Graham, R. "On Finite Sums of Unit Fractions." *Proc. London Math. Soc.***14**, 193-207, 1964. Guy, R. K. "Egyptian Fractions." &sect;D11 in *[Unsolved Problems in Number Theory, 2nd ed.][46]*New York: Springer-Verlag, pp. 158-166, 1994. Hoffman, P. *[The Man Who Loved Only Numbers: The Story of Paul Erdős and the Search for Mathematical Truth.][47]*New York: Hyperion, pp. 153-157, 1998. Ke, Z. and Sun, Q. "On the Representation of 1 by Unit Fractions." *Sichuan Daxue Xuebao***1**, 13-29, 1964. Keith, M. "Egyptian Unit Fractions." [https://www.mathpages.com/home/kmath340/kmath340.htm][48]. Klee, V. and Wagon, S. *[Old and New Unsolved Problems in Plane Geometry and Number Theory.][49]*Washington, DC: Math. Assoc. Amer., pp. 175-177 and 206-208, 1991. Loy, J. "Egyptian Fractions." [https://web.archive.org/web/20040203031114/http://www.jimloy.com/egypt/fraction.htm][50]. Mackenzie, D. "Fractions to Make an Egyptian Scribe Blanch." *Science***278**, 224, 1997. Martin, G. "Dense Egyptian Fractions." *Trans. Amer. Math. Soc.***351**, 3641-3657, 1999. Martin, G. Egyptian fraction summing to 2. [https://personal.math.ubc.ca/~gerg/papers/downloads/recsum2.pdf][51]. Martin, G. Egyptian fraction summing to 6. [https://personal.math.ubc.ca/~gerg/papers/downloads/recsum6.pdf][52]. MathPages. "Egyptian Unit Fractions." [https://www.mathpages.com/home/kmath340/kmath340.htm][48]. Niven, I. and Zuckerman, H. S. *[An Introduction to the Theory of Numbers, 5th ed.][53]*New York: Wiley, p. 200, 1991. S&eacute;roul, R. "Egyptian Fractions." &sect;8.8 in *[Programming for Mathematicians.][54]*Berlin: Springer-Verlag, pp. 181-187, 2000. Sierpiński, W. "Sur les d&eacute;compositiones de nombres rationelles en fractions primaires." *Mathesis***65**, 16-32, 1956. Sloane, N. J. A. Sequences [A001466][28] /M4553, [A002260][15], [A006487][19] /M2962, [A006524][29] /M3509, [A006525][22] /M1553, [A006526][23] /M3122, [A050205][16], [A050206][17], [A050210][18], [A069139][21], [A110820][24], [A118323][25], [A118324][27], and [A118325][20] in "The On-Line Encyclopedia of Integer Sequences." Starke, E. P. "Problem 4512." *Amer. Math. Monthly***59**, 640, 1952. Stewart, I. "The Riddle of the Vanishing Camel." *Sci. Amer.***266**, 122-124, June 1992. Tenenbaum, G. and Yokota, H. "Length and Denominators of Egyptian Fractions." *J. Number Th.***35**, 150-156, 1990. Vose, M. "Egyptian Fractions." *Bull. London Math. Soc.***17**, 21, 1985. Wagon, S. "Egyptian Fractions." &sect;8.6 in *[Mathematica in Action.][55]*New York: W. H. Freeman, pp. 271-277, 1991. Wells, D. *[The Penguin Dictionary of Curious and Interesting Numbers.][56]*Middlesex, England: Penguin Books, p. 29, 1986.

## Referenced on Wolfram|Alpha

[Egyptian Fraction][57]

## Cite this as:

[Weisstein, Eric W.][58] "Egyptian Fraction." From **[MathWorld][59] --A Wolfram Resource. [https://mathworld.wolfram.com/EgyptianFraction.html][60]

## Subject classifications


## Links

[1]: /notebooks/Arithmetic/EgyptianFraction.nb
[2]: /UnitFraction.html
[3]: /RhindPapyrus.html
[4]: /OddNumber.html
[5]: /RationalNumber.html
[6]: /Denominator.html
[7]: /RepresentedAs.html
[8]: /Fraction.html
[9]: /Algorithm.html
[10]: /BinaryRemainderMethod.html
[11]: /ContinuedFractionUnitFractionAlgorithm.html
[12]: /GreedyAlgorithm.html
[13]: /ReverseGreedyAlgorithm.html
[14]: /SmallMultipleMethod.html
[15]: http://oeis.org/A002260
[16]: http://oeis.org/A050205
[17]: http://oeis.org/A050206
[18]: http://oeis.org/A050210
[19]: http://oeis.org/A006487
[20]: http://oeis.org/A118325
[21]: http://oeis.org/A069139
[22]: http://oeis.org/A006525
[23]: http://oeis.org/A006526
[24]: http://oeis.org/A110820
[25]: http://oeis.org/A118323
[26]: http://oeis.org/A117116
[27]: http://oeis.org/A118324
[28]: http://oeis.org/A001466
[29]: http://oeis.org/A006524
[30]: /DiophantineEquation.html
[31]: /Erdos-StrausConjecture.html
[32]: /HarmonicNumber.html
[33]: /Integer.html
[34]: /AkhmimWoodenTablet.html
[35]: /EgyptianMathematicalLeatherRoll.html
[36]: /EgyptianNumber.html
[37]: /EngelExpansion.html
[38]: https://www.wolframalpha.com/input/?i=Archimedes%27+axiom
[39]: https://www.wolframalpha.com/input/?i=fractions
[40]: https://www.wolframalpha.com/input/?i=egyptian+fraction+3.1415926535897932384626433832795028841971693993751
[41]: http://www.amazon.com/exec/obidos/ASIN/0879010045/ref=nosim/ericstreasuretro
[42]: https://ics.uci.edu/~eppstein/numth/egypt/
[43]: https://ics.uci.edu/~eppstein/numth/egypt/egypt.ma
[44]: /contribute/updated_hyperlink.html#EgyptianFraction
[45]: http://www.teleport.com/~ddonahue/phresour.html
[46]: http://www.amazon.com/exec/obidos/ASIN/0387208607/ref=nosim/ericstreasuretro
[47]: http://www.amazon.com/exec/obidos/ASIN/0786863625/ref=nosim/ericstreasuretro
[48]: https://www.mathpages.com/home/kmath340/kmath340.htm
[49]: http://www.amazon.com/exec/obidos/ASIN/0883853159/ref=nosim/ericstreasuretro
[50]: https://web.archive.org/web/20040203031114/http://www.jimloy.com/egypt/fraction.htm
[51]: https://personal.math.ubc.ca/~gerg/papers/downloads/recsum2.pdf
[52]: https://personal.math.ubc.ca/~gerg/papers/downloads/recsum6.pdf
[53]: http://www.amazon.com/exec/obidos/ASIN/0471625469/ref=nosim/ericstreasuretro
[54]: http://www.amazon.com/exec/obidos/ASIN/354066422X/ref=nosim/ericstreasuretro
[55]: http://www.amazon.com/exec/obidos/ASIN/0387753664/ref=nosim/ericstreasuretro
[56]: http://www.amazon.com/exec/obidos/ASIN/0140080295/ref=nosim/ericstreasuretro
[57]: https://www.wolframalpha.com/input/?i=egyptian+fraction
[58]: /about/author.html
[59]: /
[60]: https://mathworld.wolfram.com/EgyptianFraction.html
