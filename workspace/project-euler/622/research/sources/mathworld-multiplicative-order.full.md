<!-- source: https://mathworld.wolfram.com/MultiplicativeOrder.html | converted from HTML -->

Multiplicative Order -- from Wolfram MathWorld

# Multiplicative Order

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

Let [image: n] be a positive number having [primitive roots][2]. If [image: g] is a [primitive root][2] of [image: n], then the numbers 1, [image: g], [image: g^2], ..., [image: g^(phi(n)-1)] form a [reduced residue system][3] modulo [image: n], where [image: phi(n)] is the [totient function][4]. In this set, there are [image: phi(phi(n))] [primitive roots][2], and these are the numbers [image: g^c], where [image: c] is [relatively prime][5] to [image: phi(n)].

The smallest exponent [image: e] for which [image: b^e=1 (mod n)], where [image: b] and [image: n] are given numbers, is called the multiplicative order (or sometimes haupt-exponent or modulo order) of [image: b] (mod [image: n]).

The multiplicative order is implemented in the [Wolfram Language][6] as [MultiplicativeOrder][7] [*g*, *n*].

The number of bases having multiplicative order [image: e] is [image: phi(e)], where [image: phi(e)] is the [totient function][4]. Cunningham (1922) published the multiplicative order for primes to 25409 and bases 2, 3, 5, 6, 7, 10, 11, and 12.

Multiplicative orders exist for [image: n] that are [relatively prime][5] to [image: b]. For example, the multiplicative order of 10 (mod 7) is 6, since

[image:  10^6=1 (mod 7). ] |

(1)

 |

The multiplicative order of 10 mod an integer [image: n] relatively prime to 10 gives the period of the [decimal expansion][8] of the reciprocal of [image: n] (Glaisher 1878, Lehmer 1941). For example, the haupt-exponent of 10 (mod 13) is 6, and

[image:  1/(13)=0.076923^_, ] |

(2)

 |

which has period 6.

The following table gives the first few multiplicative orders for bases [image: b] (mod [image: n]), where [image: n] is the series of numbers [relatively prime][5] to [image: b].

[image: b] | OEIS | haupt-exponents |

2 | [A002326][9] | 2, 4, 3, 6, 10, 12, 4, 8, 18, 6, 11, 20, 18, ... |

3 | [A050975][10] | 1, 2, 4, 6, 2, 4, 5, 3, 6, 4, 16, 18, 4, 5, ... |

4 | [A050976][11] | 1, 2, 3, 3, 5, 6, 2, 4, 9, 3, 11, 10, 9, 14, ... |

5 | [A050977][12] | 1, 2, 1, 2, 6, 2, 6, 5, 2, 4, 6, 4, 16, 6, 9, ... |

6 | [A050978][13] | 1, 2, 10, 12, 16, 9, 11, 5, 14, ... |

7 | [A050979][14] | 1, 1, 2, 4, 1, 2, 3, 4, 10, 2, 12, 4, 2, 16, ... |

8 | [A050980][15] | 2, 4, 1, 2, 10, 4, 4, 8, 6, 2, 11, 20, 6, 28, ... |

9 | [A050981][16] | 1, 1, 2, 3, 1, 2, 5, 3, 3, 2, 8, 9, 2, 5, 11, ... |

10 | [A002329][17] | 1, 6, 1, 2, 6, 16, 18, 6, 22, 3, 28, ... |

If [image: a] is an arbitrary integer [relatively prime][5] to [image: n], then there exists among the numbers 0, 1, 2, ..., [image: phi(n)-1] [exactly one][18] number [image: mu] such that

[image:  a=g^mu (mod n). ] |

(3)

 |

The number [image: mu] is then called the generalized multiplicative order (or [discrete logarithm][19]; Schneier 1996, p. 501) of [image: a] with respect to the base [image: g] modulo [image: n]. Note that Nagell (1951, p. 112) instead uses the term "index" and writes

[image:  mu=ind_ga (mod n). ] |

(4)

 |

For example, the number 7 is the least positive [primitive root][2] of [image: n=41], and since [image: 15=7^3 (mod 41)], the number 15 has multiplicative order 3 with respect to base 7 (modulo 41) (Nagell 1951, p. 112).

The generalized multiplicative order is implemented in the [Wolfram Language][6] as [MultiplicativeOrder][7] [*g*, *n*, [image: {]*a1*[image: }]], or more generally as [MultiplicativeOrder][7] [*g*, *n*, [image: {]*a1*, *a2*, ...[image: }]].

If the [primitive roots][2][image: g_1=-1] and [image: g_2=1] are chosen, the resulting function is called the [suborder function][20] and is denoted [image: sord_n(a)]. If the single [primitive root][2][image: g_1=1] is chosen, then the function reduces to "the" (i.e., ungeneralized) multiplicative order, denoted [image: ord_n(a)], implemented in the [Wolfram Language][6] as [MultiplicativeOrder][7] [*a*, *n*]. This function is sometimes also known as the discrete logarithm (or, more confusingly, as the "index," a term that Nagell applied to the case of general [image: g]).

---

## See also

[Carmichael Function][21], [Complete Residue System][22], [Congruence][23], [Discrete Logarithm][19], [Full Reptend Prime][24], [Out-Shuffle][25], [Polynomial Order][26], [Primitive Root][2], [Suborder Function][20]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [Artin's constant][27]
- [7^3][28]
- [cone][29]

## References

Burton, D. M. "The Order of an Integer Modulo [image: n]." &sect;8.1 in *[Elementary Number Theory, 4th ed.][30]*Dubuque, IA: William C. Brown Publishers, pp. 184-190, 1989. Cunningham, A. *[Haupt-Exponents, Residue Indices, Primitive Roots.][31]*London, England: F. Hodgson, 1922. Glaisher, J. W. L. "Periods of Reciprocals of Integers Prime to 10." *Proc. Cambridge Philos. Soc.***3**, 185-206, 1878. Lehmer, D. H. "Guide to Tables in the Theory of Numbers." Bulletin No. 105. Washington, DC: National Research Council, pp. 7-12, 1941. Nagell, T. "Exponent of an Integer Modulo [image: n] " and "The Index Calculus." &sect;31 and 33 in *[Introduction to Number Theory.][32]*New York: Wiley, pp. 102-106 and 111-115, 1951. Odlyzko, A. "Discrete Logarithms: The Past and the Future." [https://www-users.cse.umn.edu/~odlyzko/doc/discrete.logs.future.pdf][33]. Schneier, B *[Applied Cryptography: Protocols, Algorithms, and Source Code in C, 2nd ed.][34]*New York: Wiley, 1996. Sloane, N. J. A. Sequences [A002326][9] /M0936, [A002329][17] /M4045, [A050975][10], [A050976][11], [A050977][12], [A050978][13], [A050979][14], [A050980][15], and [A050981][16] in "The On-Line Encyclopedia of Integer Sequences."

## Referenced on Wolfram|Alpha

[Multiplicative Order][35]

## Cite this as:

[Weisstein, Eric W.][36] "Multiplicative Order." From **[MathWorld][37] --A Wolfram Resource. [https://mathworld.wolfram.com/MultiplicativeOrder.html][38]

## Subject classifications


## Links

[1]: /notebooks/NumberTheory/MultiplicativeOrder.nb
[2]: /PrimitiveRoot.html
[3]: /ReducedResidueSystem.html
[4]: /TotientFunction.html
[5]: /RelativelyPrime.html
[6]: http://www.wolfram.com/language/
[7]: http://reference.wolfram.com/language/ref/MultiplicativeOrder.html
[8]: /DecimalExpansion.html
[9]: http://oeis.org/A002326
[10]: http://oeis.org/A050975
[11]: http://oeis.org/A050976
[12]: http://oeis.org/A050977
[13]: http://oeis.org/A050978
[14]: http://oeis.org/A050979
[15]: http://oeis.org/A050980
[16]: http://oeis.org/A050981
[17]: http://oeis.org/A002329
[18]: /ExactlyOne.html
[19]: /DiscreteLogarithm.html
[20]: /SuborderFunction.html
[21]: /CarmichaelFunction.html
[22]: /CompleteResidueSystem.html
[23]: /Congruence.html
[24]: /FullReptendPrime.html
[25]: /Out-Shuffle.html
[26]: /PolynomialOrder.html
[27]: https://www.wolframalpha.com/input/?i=Artin%27s+constant
[28]: https://www.wolframalpha.com/input/?i=7%5E3
[29]: https://www.wolframalpha.com/input/?i=cone
[30]: http://www.amazon.com/exec/obidos/ASIN/0070094667/ref=nosim/ericstreasuretro
[31]: http://www.amazon.com/exec/obidos/ASIN/B00088062Q/ref=nosim/ericstreasuretro
[32]: http://www.amazon.com/exec/obidos/ASIN/0828401632/ref=nosim/ericstreasuretro
[33]: https://www-users.cse.umn.edu/~odlyzko/doc/discrete.logs.future.pdf
[34]: http://www.amazon.com/exec/obidos/ASIN/0471117099/ref=nosim/ericstreasuretro
[35]: https://www.wolframalpha.com/input/?i=multiplicative+order
[36]: /about/author.html
[37]: /
[38]: https://mathworld.wolfram.com/MultiplicativeOrder.html
