<!-- source: https://mathworld.wolfram.com/PascalsTriangle.html | converted from HTML -->

Pascal's Triangle -- from Wolfram MathWorld

# Pascal's Triangle

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

Pascal's triangle is a [number triangle][2] with numbers arranged in staggered rows such that

[image:  a_(nr)=(n!)/(r!(n-r)!)=(n; r), ] |

(1)

 |

where [image: (n; r)] is a [binomial coefficient][3]. The triangle was studied by B. Pascal, in whose posthumous work it appeared in 1665 (Pascal 1665). However, it had been previously investigated my many other mathematicians, including Italian algebraist Niccol&ograve; Tartaglia, who published the first six rows of the triangle in 1556. It was also described centuries earlier by Chinese mathematician Yang Hui and the Persian astronomer-poet Omar Khayy&aacute;m. As a result, it is known as the Yang Hui triangle in China, the Khayyam triangle in Persia, and Tartaglia's triangle in Italy.

Starting with [image: n=0], the [triangle][4] is

[image:  1
1  1
1  2  1
1  3  3  1
1  4  6  4  1
1  5  10  10  5  1
1  6  15  20  15  6  1 ] |

(2)

 |

(OEIS [A007318][5]). [Pascal's formula][6] shows that each subsequent row is obtained by adding the two entries diagonally above,

[image:  (n; r)=(n!)/((n-r)!r!)=(n-1; r)+(n-1; r-1). ] |

(3)

 |

Replacing the binomial coefficients in Pascal's triangle by [multinomial coefficients][7] in three indices gives [Pascal's tetrahedron][8], a three-dimensional analog in which each interior entry is the sum of the three adjacent entries above it.

[image: Binary plot for Pascal's triangle]

The plot above shows the binary representations for the first 255 (top figure) and 511 (bottom figure) terms of a flattened Pascal's triangle.

The first number after the 1 in each row divides all other numbers in that row [iff][9] it is a [prime][10].

The sums [image: P_n] of the number of odd entries in the first [image: n] rows of Pascal's triangle for [image: n=0], 1, ... are 0, 1, 3, 5, 9, 11, 15, 19, 27, 29, 33, 37, 45, 49, ... (OEIS [A006046][11]). It is then true that

[image:  0.812...<P_nn^(-theta)<=1 ] |

(4)

 |

(Harborth 1976, Le Lionnais 1983), with equality for [image: n] a power of 2, and the power of [image: n] given by the constant

[image:  theta=(ln3)/(ln2)=log_23=1.58496250072115... ] |

(5)

 |

(OEIS [A020857][12]). The sequence of cumulative counts of odd entries has some amazing properties, and the minimum possible value [image: beta=0.812...] (OEIS [A077464][13]) is known as the [Stolarsky-Harborth constant][14].

Pascal's triangle contains the [figurate numbers][15] along its diagonals, as can be seen from the identity

[image: sum_(i=1)^(n)(i; j)] | [image: =] | [image: (n+1)/(j+1)(n; j)] |

(6)

 |

 | [image: =] | [image: (n+1; j+1).] |

(7)

 |

In addition, the sum of the elements of the [image: i] th row is

[image:  sum_(j=0)^i(i; j)=2^i, ] |

(8)

 |

so the sum of the first [image: k] rows (i.e., rows 0 to [image: k-1]) is the [Mersenne number][16]

[image:  sum_(i=0)^(k-1)2^i=2^k-1. ] |

(9)

 |

[image: FibonacciShallowDiags]

The shallow diagonals of Pascal's triangle sum to [Fibonacci numbers][17], i.e.,

[image: 1] | [image: =] | [image: 1] |

(10)

 |

[image: 1] | [image: =] | [image: 1] |

(11)

 |

[image: 2] | [image: =] | [image: 1+1] |

(12)

 |

[image: 3] | [image: =] | [image: 2+1] |

(13)

 |

[image: 5] | [image: =] | [image: 1+3+1] |

(14)

 |

[image: 8] | [image: =] | [image: 3+4+1] |

(15)

 |

and, in general,

[image:  sum_(k=0)^(|_n/2_|)(n-k; k)=F_(n+1). ] |

(16)

 |

The numbers of times that the numbers 2, 3, 4, ... occur in Pascal's triangle are given by 1, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 2, 2, 4, ... (OEIS [A003016][18]; Ogilvy 1972, p. 96, Comtet 1974, p. 93, Singmaster 1971). Similarly, the numbers of rows in which the numbers 2, 3, 4, ... occur are 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, ... (OEIS [A059233][19]).

By row 210, the numbers

[image: 120] | [image: =] | [image: (10; 3)=(10; 7)=(16; 2)=(16; 14)=(120; 1)=(120; 119)] |

(17)

 |

[image: 210] | [image: =] | [image: (10; 4)=(10; 6)=(21; 2)=(21; 19)=(210; 1)=(210; 209)] |

(18)

 |

[image: 3003] | [image: =] | [image: (14; 6)=(14; 8)=(15; 5)=(15; 10)=(78; 2)=(78; 76)] |

(19)

 |

have appeared six times, more than any other number (excluding 1). By row 1540,

[image:  1540=(22; 3)=(22; 19)=(56; 2)=(56; 54)=(1540; 1)
 =(1540; 1539)   ] |

(20)

 |

has now occurred six times, by row 3003,

[image:  3003=(14; 6)=(14; 8)=(15; 5)=(15; 10)=(78; 2)
 =(78; 76)=(3003; 1)=(3003; 3002)   ] |

(21)

 |

has now occurred 8 times, and by row 7140, 7140 has appeared six times as well. In fact, the numbers that occur five or more times in Pascal's triangle are 1, 120, 210, 1540, 3003, 7140, 11628, 24310, ... (OEIS [A003015][20]), with no others up to [image: 33×10^(16)].

It is known that there are infinitely many numbers that occur at least 6 times in Pascal's triangle, namely the solutions to

[image:  r=(n; m-1)=(n-1; m) ] |

(22)

 |

given by

[image: m] | [image: =] | [image: F_(2k-1)F_(2k)] |

(23)

 |

[image: n] | [image: =] | [image: F_(2k)F_(2k+1),] |

(24)

 |

where [image: F_i] is the [image: i] th [Fibonacci number][17] (Singmaster 1975). The first few such values of [image: r] for [image: k=1], 2, ... are 1, 3003, 61218182743304701891431482520, ... (OEIS [A090162][21]).

There is an unexpected connection between Pascal's triangle and the [Delannoy numbers][22] via [Cholesky decomposition][23] (G. Helms, pers. comm., Aug. 29, 2005). What's more, despite the two being mathematically unrelated, there's also a topical connection between Pascal's triangle and the so-called [rascal triangle][24]; this relationship also provides a tangential relation to the [cake cutting][25] problem and hence to the [cake numbers][26].

Pascal's triangle (mod 2) turns out to be equivalent to the [Sierpiński sieve][27] (Wolfram 1984, Crandall and Pomerance 2001, Borwein and Bailey 2003, pp. 46-47). Guy (1990) gives several other unexpected properties of Pascal's triangle.

---

## See also

[Bell Triangle][28], [Bernoulli Triangle][29], [Binomial Coefficient][3], [Binomial Theorem][30], [Brianchon's Theorem][31], [Cake Cutting][25], [Catalan's Triangle][32], [Christmas Stocking Theorem][33], [Clark's Triangle][34], [Cylinder Cutting][35], [Euler's Number Triangle][36], [Fibonacci Number][17], [Figurate Number Triangle][37], [Leibniz Harmonic Triangle][38], [Losanitsch's Triangle][39], [Number Triangle][2], [Pascal Matrix][40], [Pascal's Formula][6], [Pascal's Tetrahedron][8], [Polygon][41], [Rascal Triangle][24], [Seidel-Entringer-Arnold Triangle][42], [Sierpiński Sieve][27], [Space Division by Planes][43], [Square Division by Lines][44], [Star of David Theorem][45], [Stolarsky-Harborth Constant][14], [Trinomial Triangle][46] [Explore this topic in the MathWorld classroom][47]

*Portions of this entry contributed by [Christopher Stover][48]*

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [pascal's triangle][49]
- [pascal's triangle mod 3][50]
- [pascal's triangle mod 4][51]

## References

Borwein, J. and Bailey, D. "Pascal's Triangle." &sect;2.1 in *[Mathematics by Experiment: Plausible Reasoning in the 21st Century.][52]*Wellesley, MA: A K Peters, pp. 45-48, 2003. Comtet, L. *[Advanced Combinatorics: The Art of Finite and Infinite Expansions, rev. enl. ed.][53]*Dordrecht, Netherlands: Reidel, p. 93, 1974. Conway, J. H. and Guy, R. K. "Pascal's Triangle." In *[The Book of Numbers.][54]*New York: Springer-Verlag, pp. 68-70, 1996. Courant, R. and Robbins, H. *[What Is Mathematics?: An Elementary Approach to Ideas and Methods, 2nd ed.][55]*Oxford, England: Oxford University Press, p. 17, 1996. Crandall, R. and Pomerance, C. Research Problem 8.22 in *[Prime Numbers: A Computational Perspective.][56]*New York: Springer-Verlag, 2001. de Weger, B. M. M. "Equal Binomial Coefficients: Some Elementary Considerations." *J. Number Theory***63**, 373-386, 1997. [https://doi.org/10.1006/jnth.1997.2109][57]. Gardner, M. "Pascal's Triangle." Ch. 15 in *[Mathematical Carnival: A New Round-Up of Tantalizers and Puzzles from Scientific American.][58]*New York: Vintage Books, pp. 194-207, 1977. Guy, R. K. "The Second Strong Law of Small Numbers." *Math. Mag.***63**, 3-20, 1990. Guy, R. K. and Klee, V. "Monthly Research Problems, 1969-1971." *Amer. Math. Monthly***78**, 1113-1122, 1971. Harborth, H. "Number of Odd Binomial Coefficients." *Not. Amer. Math. Soc.***23**, 4, 1976. Le Lionnais, F. *[Les nombres remarquables.][59]*Paris, France: Hermann, p. 31, 1983. Ogilvy, C. S. *[Tomorrow's Math: Unsolved Problems for the Amateur, 2nd ed.][60]*New York: Oxford University Press, 1972. Pappas, T. "Pascal's Triangle, the Fibonacci Sequence & Binomial Formula," "Chinese Triangle," and "Probability and Pascal's Triangle." *[The Joy of Mathematics.][61]*San Carlos, CA: Wide World Publ./Tetra, pp. 40-41, 88, and 184-186, 1989. Pascal, B. *Trait&eacute; du triangle arithm&eacute;tique, avec quelques autres petits traitez sur la mesme mati&egrave;re at gallica.*Paris, France: G. Desprez, 1665. Pickover, C. A. "Beauty, Symmetry, and Pascal's Triangle." Ch. 54 in *[Wonders of Numbers: Adventures in Mathematics, Mind, and Meaning.][62]*Oxford, England: Oxford University Press, pp. 130-133, 2001. Singmaster, D. "How Often Does an Integer Occur as a Binomial Coefficient?" *Amer. Math. Monthly***78**, 385-386, 1971. Singmaster, D. "Repeated Binomial Coefficients and Fibonacci Numbers." *Fib. Quart.***13**, 295-298, 1975. Sloane, N. J. A. Sequences [A003015][20] /M5374, [A003016][18] /M0227, [A006046][11] /M2445, [A007318][5] /M0082, [A020857][12], [A059233][19], [A077464][13], and [A090162][21] in "The On-Line Encyclopedia of Integer Sequences." Smith, D. E. *[A Source Book in Mathematics.][63]*New York: Dover, p. 86, 1984. Steinhaus, H. *[Mathematical Snapshots, 3rd ed.][64]*New York: Dover, pp. 284-285, 1999. Wells, D. *[The Penguin Dictionary of Curious and Interesting Geometry.][65]*London, England: Penguin, pp. 174-175, 1991. Wolfram, S. "Computation Theory of Cellular Automata." *Comm. Math. Phys.***96**, 15-57, 1984. Wolfram, S. *[A New Kind of Science.][66]*Champaign, IL: Wolfram Media, pp. [870][67] and [931][68] -932, 2002.

## Referenced on Wolfram|Alpha

[Pascal's Triangle][69]

## Cite this as:

[Stover, Christopher][48] and [Weisstein, Eric W.][70] "Pascal's Triangle." From **[MathWorld][71] --A Wolfram Resource. [https://mathworld.wolfram.com/PascalsTriangle.html][72]

## Subject classifications


## Links

[1]: /notebooks/Combinatorics/PascalsTriangle.nb
[2]: /NumberTriangle.html
[3]: /BinomialCoefficient.html
[4]: /Triangle.html
[5]: http://oeis.org/A007318
[6]: /PascalsFormula.html
[7]: /MultinomialCoefficient.html
[8]: /PascalsTetrahedron.html
[9]: /Iff.html
[10]: /PrimeNumber.html
[11]: http://oeis.org/A006046
[12]: http://oeis.org/A020857
[13]: http://oeis.org/A077464
[14]: /Stolarsky-HarborthConstant.html
[15]: /FigurateNumber.html
[16]: /MersenneNumber.html
[17]: /FibonacciNumber.html
[18]: http://oeis.org/A003016
[19]: http://oeis.org/A059233
[20]: http://oeis.org/A003015
[21]: http://oeis.org/A090162
[22]: /DelannoyNumber.html
[23]: /CholeskyDecomposition.html
[24]: /RascalTriangle.html
[25]: /CakeCutting.html
[26]: /CakeNumber.html
[27]: /SierpinskiSieve.html
[28]: /BellTriangle.html
[29]: /BernoulliTriangle.html
[30]: /BinomialTheorem.html
[31]: /BrianchonsTheorem.html
[32]: /CatalansTriangle.html
[33]: /ChristmasStockingTheorem.html
[34]: /ClarksTriangle.html
[35]: /CylinderCutting.html
[36]: /EulersNumberTriangle.html
[37]: /FigurateNumberTriangle.html
[38]: /LeibnizHarmonicTriangle.html
[39]: /LosanitschsTriangle.html
[40]: /PascalMatrix.html
[41]: /Polygon.html
[42]: /Seidel-Entringer-ArnoldTriangle.html
[43]: /SpaceDivisionbyPlanes.html
[44]: /SquareDivisionbyLines.html
[45]: /StarofDavidTheorem.html
[46]: /TrinomialTriangle.html
[47]: /classroom/PascalsTriangle.html
[48]: /topics/Stover.html
[49]: https://www.wolframalpha.com/input/?i=pascal%27s+triangle
[50]: https://www.wolframalpha.com/input/?i=pascal%27s+triangle+mod+3
[51]: https://www.wolframalpha.com/input/?i=pascal%27s+triangle+mod+4
[52]: http://www.amazon.com/exec/obidos/ASIN/1568812116/ref=nosim/ericstreasuretro
[53]: http://www.amazon.com/exec/obidos/ASIN/9027703809/ref=nosim/ericstreasuretro
[54]: http://www.amazon.com/exec/obidos/ASIN/038797993X/ref=nosim/ericstreasuretro
[55]: http://www.amazon.com/exec/obidos/ASIN/0195105192/ref=nosim/ericstreasuretro
[56]: http://www.amazon.com/exec/obidos/ASIN/0387252827/ref=nosim/ericstreasuretro
[57]: https://doi.org/10.1006/jnth.1997.2109
[58]: http://www.amazon.com/exec/obidos/ASIN/039472349X/ref=nosim/ericstreasuretro
[59]: http://www.amazon.com/exec/obidos/ASIN/2705614079/ref=nosim/ericstreasuretro
[60]: http://www.amazon.com/exec/obidos/ASIN/0195015088/ref=nosim/ericstreasuretro
[61]: http://www.amazon.com/exec/obidos/ASIN/0933174659/ref=nosim/ericstreasuretro
[62]: http://www.amazon.com/exec/obidos/ASIN/0195133420/ref=nosim/ericstreasuretro
[63]: http://www.amazon.com/exec/obidos/ASIN/0486646904/ref=nosim/ericstreasuretro
[64]: http://www.amazon.com/exec/obidos/ASIN/0486409147/ref=nosim/ericstreasuretro
[65]: http://www.amazon.com/exec/obidos/ASIN/0140118136/ref=nosim/ericstreasuretro
[66]: http://www.amazon.com/exec/obidos/ASIN/1579550088/ref=nosim/ericstreasuretro
[67]: https://www.wolframscience.com/nks/notes-2-1--pascals-triangle-and-rule-90/
[68]: https://www.wolframscience.com/nks/notes-5-4--sierpinski-pattern/
[69]: https://www.wolframalpha.com/input/?i=pascals+triangle
[70]: /about/author.html
[71]: /
[72]: https://mathworld.wolfram.com/PascalsTriangle.html
