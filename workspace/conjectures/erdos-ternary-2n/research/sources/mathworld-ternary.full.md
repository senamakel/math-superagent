<!-- source: https://mathworld.wolfram.com/Ternary.html | converted from HTML -->

Ternary -- from Wolfram MathWorld

# Ternary

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

The [base][2] -3 method of counting in which only the digits 0, 1, and 2 are used. Ternary numbers arise in a number of problems in mathematics, including some problems of [weighing][3]. However, according to Knuth (1998), "no substantial application of balanced ternary notation has been made" (balanced ternary uses digits [image: -1], 0, and 1 instead of 0, 1, and 2).

[image: Ternary]

The illustration above shows a graphical representation of the numbers 0 to 25 in ternary, and the following table gives the ternary equivalents of the first few decimal numbers. The concatenation of the ternary digits of the consecutive numbers 0, 1, 2, 3, ... gives (0), (1), (2), (1, 0), (1, 1), (1, 2), (2, 0), ... (OEIS [A054635][4]).

1 | 1 | 11 | 102 | 21 | 210 |

2 | 2 | 12 | 110 | 22 | 211 |

3 | 10 | 13 | 111 | 23 | 212 |

4 | 11 | 14 | 112 | 24 | 220 |

5 | 12 | 15 | 120 | 25 | 221 |

6 | 20 | 16 | 121 | 26 | 222 |

7 | 21 | 17 | 122 | 27 | 1000 |

8 | 22 | 18 | 200 | 28 | 1001 |

9 | 100 | 19 | 201 | 29 | 1002 |

10 | 101 | 20 | 202 | 30 | 1010 |

Ternary digits have the following [multiplication table][5].

[image: ×] | 0 | 1 | 2 |

0 | 0 | 0 | 0 |

1 | 0 | 1 | 2 |

2 | 0 | 2 | 11 |

A ternary representation can be used to uniquely identify [totalistic cellular automaton][6] rules, where the three colors (white, gray, and black) correspond to the three numbers 0, 1 and 2 (Wolfram 2002, pp. [60][7] -70 and [886][8]). For example, the ternary digits [image: 0211020_3], lead to the code 600 [totalistic cellular automaton][6].

Every [even number][9] represented in ternary has an [even number][9] (possibly 0) of 1s. This is true since a number is congruent mod [image: (b-1)] to the sum of its [base][2] -[image: b] [digits][10]. In the case [image: b=3], there is only one digit (1) which is not a multiple of [image: b-1], so all we have to do is "cast out twos" and count the number of 1s in the base-3 representation.

The following table gives [image: 2^n] for [image: n=1], 2, ... in ternary.

[image: 2^1] | [image: =] | [image: 2_3] |

(1)

 |

[image: 2^2] | [image: =] | [image: 11_3] |

(2)

 |

[image: 2^3] | [image: =] | [image: 22_3] |

(3)

 |

[image: 2^4] | [image: =] | [image: 121_3] |

(4)

 |

[image: 2^5] | [image: =] | [image: 1012_3] |

(5)

 |

[image: 2^6] | [image: =] | [image: 2101_3] |

(6)

 |

[image: 2^7] | [image: =] | [image: 11202_3.] |

(7)

 |

N. J. A. Sloane conjectured that for any integer [image: n>15], [image: 2^n] always has a 0 in its ternary expansion (Sloane 1973; Vardi 1991, p. 28). Known values of [image: n] such that [image: 2^n]*lacks*a 0 are 1, 2, 3, 4, 15 (OEIS [A102483][11]), with no others up to [image: 10^5] (E. W. Weisstein, Apr. 8, 2006). The positions (counting from the least significant ternary digits) of the first 0 digit in [image: (2^1)_3], [image: (2^2)_3], ..., are 0, 0, 0, 0, 3, 2, 2, 4, 4, 5, 4, 2, 2, 4, 0, 3, 4, (OEIS [A117971][12]).

Similarly, [image: 2^n] always has a 1 in its ternary expansion except for [image: n=1], 1, 3, and 9, with no others up to [image: 10^5] (E. W. Weisstein, Apr. 8, 2006).

Erdős and Graham (1980) conjectured that no [power][13] of 2, [image: 2^n], for [image: n>8] is a [sum][14] of distinct powers of 3. This is equivalent to the requirement that the ternary expansion of [image: 2^n] always contains a 2 for [image: n>8]. The fact that the only values not having a two are [image: n=2] and 8 has been verified by Vardi (1991) up to [image: n=2·3^(20)=6.97×10^9]. The positions (counting from the least significant ternary digits) of the first 2 digit in [image: (2^1)_3], [image: (2^2)_3], ..., are 1, 0, 1, 2, 1, 4, 1, 0, 1, 2, 1, 3, 1, 3, ... (OEIS [A117970][15]).

---

## See also

[Base][2], [Binary][16], [Champernowne Constant][17], [Decimal][18], [Hexadecimal][19], [Octal][20], [Quaternary][21], [Totalistic Cellular Automaton][6]

*Portions of this entry contributed by [Vincenzo Origlio][22]*

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [ternary][23]
- [12 in base 3][24]
- [1221 in base 4 to decimal][25]

## References

Erdős, P. and Graham, R. L. *[Old and New Problems and Results in Combinatorial Number Theory.][26]*Geneva, Switzerland: L'Enseignement Math&eacute;matique Universit&eacute; de Gen&egrave;ve, Vol. 28, 1980. Gardner, M. "The Ternary System." Ch. 11 in *[The Sixth Book of Mathematical Games from Scientific American.][27]*Chicago, IL: University of Chicago Press, pp. 104-112, 1984. Knuth, D. E. *[The Art of Computer Programming. Vol. 2: Seminumerical Algorithms, 3rd ed.][28]*Reading, MA: Addison-Wesley, pp. 173-175, 1998. Lauwerier, H. *[Fractals: Endlessly Repeated Geometric Figures.][29]*Princeton, NJ: Princeton University Press, pp. 10-11, 1991. Sloane, N. J. A. "The Persistence of a Number." *J. Recr. Math.***6**, 97-98, 1973. Sloane, N. J. A. Sequences [A054635][4], [A102483][11], [A117970][15], and [A117970][15] in "The On-Line Encyclopedia of Integer Sequences." Vardi, I. "The Digits of [image: 2^n] in Base Three." *[Computational Recreations in Mathematica.][30]*Reading, MA: Addison-Wesley, pp. 20-25, 1991. Wolfram, S. *[A New Kind of Science.][31]*Champaign, IL: Wolfram Media, pp. [60][7] -70 and [886][8], 2002.

## Referenced on Wolfram|Alpha

[Ternary][23]

## Cite this as:

[Weisstein, Eric W.][32], with contributions by [Vincenzo Origlio][22]. "Ternary." From **[MathWorld][33] --A Wolfram Resource. [https://mathworld.wolfram.com/Ternary.html][34]

## Subject classifications


## Links

[1]: /notebooks/Numbers/Ternary.nb
[2]: /Base.html
[3]: /Weighing.html
[4]: http://oeis.org/A054635
[5]: /MultiplicationTable.html
[6]: /TotalisticCellularAutomaton.html
[7]: https://www.wolframscience.com/nks/p60--more-cellular-automata/
[8]: https://www.wolframscience.com/nks/notes-3-2--numbers-of-cellular-automaton-rules/
[9]: /EvenNumber.html
[10]: /Digit.html
[11]: http://oeis.org/A102483
[12]: http://oeis.org/A117971
[13]: /Power.html
[14]: /Sum.html
[15]: http://oeis.org/A117970
[16]: /Binary.html
[17]: /ChampernowneConstant.html
[18]: /Decimal.html
[19]: /Hexadecimal.html
[20]: /Octal.html
[21]: /Quaternary.html
[22]: /topics/Origlio.html
[23]: https://www.wolframalpha.com/input/?i=ternary
[24]: https://www.wolframalpha.com/input/?i=12+in+base+3
[25]: https://www.wolframalpha.com/input/?i=1221+in+base+4+to+decimal
[26]: http://www.amazon.com/exec/obidos/ASIN/B0006E5L5O/ref=nosim/ericstreasuretro
[27]: http://www.amazon.com/exec/obidos/ASIN/0226282503/ref=nosim/ericstreasuretro
[28]: http://www.amazon.com/exec/obidos/ASIN/0201896850/ref=nosim/ericstreasuretro
[29]: http://www.amazon.com/exec/obidos/ASIN/0691024456/ref=nosim/ericstreasuretro
[30]: http://www.amazon.com/exec/obidos/ASIN/0685479412/ref=nosim/ericstreasuretro
[31]: http://www.amazon.com/exec/obidos/ASIN/1579550088/ref=nosim/ericstreasuretro
[32]: /about/author.html
[33]: /
[34]: https://mathworld.wolfram.com/Ternary.html
