<!-- source: https://mathworld.wolfram.com/MertensFunction.html | converted from HTML -->

Mertens Function -- from Wolfram MathWorld

# Mertens Function

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: MertensFunction]

The Mertens function is the summary function

[image:  M(n)=sum_(k=1)^nmu(k), ] |

(1)

 |

where [image: mu(n)] is the [M&ouml;bius function][2] (Mertens 1897; Havil 2003, p. 208). The first few values are 1, 0, [image: -1], [image: -1], [image: -2], [image: -1], [image: -2], [image: -2], [image: -2], [image: -1], [image: -2], [image: -2], ... (OEIS [A002321][3]). [image: M(n)] is also given by the [determinant][4] of the [image: n×n] [Redheffer matrix][5].

Values of [image: M(10^n)] for [image: n=0], 1, 2, ... are given by 1, [image: -1], 1, 2, [image: -23], [image: -48], 212, 1037, 1928, [image: -222], ... (OEIS [A084237][6]; Del&eacute;glise and Rivat 1996).

The following table summarizes the first few values of [image: n] at which [image: M(n)=k] for various [image: k]

[image: k] | OEIS | [image: n] such that [image: M(n)=k] |

[image: -3] | 13, 19, 20, 30, 33, 43, 44, 45, 47, 48, 49, 50, ... |

[image: -2] | 5, 7, 8, 9, 11, 12, 14, 17, 18, 21, 23, 24, 25, 29, ... |

[image: -1] | 3, 4, 6, 10, 15, 16, 22, 26, 27, 28, 35, 36, 38, ... |

0 | [A028442][7] | 2, 39, 40, 58, 65, 93, 101, 145, 149, 150, ... |

1 | [A118684][8] | 1, 94, 97, 98, 99, 100, 146, 147, 148, 161, ... |

2 | 95, 96, 217, 229, 335, 336, 339, 340, 345, 347, 348, ... |

3 | 218, 223, 224, 225, 227, 228, 341, 342, 343, 344, 346, ... |

An analytic formula for [image: M(x)] is not known, although Titchmarsh (1960) showed that if the [Riemann hypothesis][9] holds and if there are no multiple [Riemann zeta function zeros][10], then there is a sequence [image: T_k] with [image: k<=T_k<=k+1] such that

[image:  M_0(x)=lim_(k->infty)sum_(rho; |gamma|<T_k)(x^rho)/(rhozeta^'(rho))-2
 +sum_(n=1)^infty((-1)^(n-1))/((2n)!nzeta(2n+1))((2pi)/x)^(2n),   ] |

(2)

 |

where [image: zeta(z)] is the [Riemann zeta function][11],

[image:  M_0(x)={M(x)-1/2mu(x)   if x in Z^+; M(x)   otherwise, ] |

(3)

 |

and [image: rho=1/2+igamma] runs over all [nontrivial zeros][12] of the [Riemann zeta function][11] (Odlyzko and te Riele 1985).

The Mertens function is related to the number of [squarefree][13] integers up to [image: n], which is the sum from 1 to [image: n] of the absolute value of [image: mu(k)],

[image:  sum_(k=1)^n|mu(k)|&sim;6/(pi^2)n+O(sqrt(n)). ] |

(4)

 |

The Mertens function also obeys

[image:  sum_(n=1)^xM(x/n)=1 ] |

(5)

 |

(Lehman 1960).

Mertens (1897) verified that [image: |M(x)|<=sqrt(x)] for [image: x<10000] and conjectured that this inequality holds for all nonnegative [image: x]. The statement

[image:  |M(x)|<x^(1/2) ] |

(6)

 |

is therefore known as the [Mertens conjecture][14], although it has since been disproved.

Lehman (1960) gives an algorithm for computing [image: M(x)] with [image: O(x^(2/3+epsilon))] operations, while the Lagarias-Odlyzko (1987) algorithm for computing the [prime counting function][15][image: pi(x)] can be modified to give [image: M(x)] in [image: O(x^(3/5+epsilon))] operations. Del&eacute;glise and Rivat 1996) described an elementary method for computing isolated values of [image: M(x)] with time complexity [image: O(x^(2/3)(lnlnx)^(1/3))] and space complexity [image: O(x^(1/3)(lnlnx)^(2/3))].

---

## See also

[Mertens Conjecture][14], [M&ouml;bius Function][2], [Redheffer Matrix][5], [Squarefree][13]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [birthday problem 35 people][16]
- [CNF (P && ~Q) || (R && S) || (Q && R && ~S)][17]
- [integrate 1/sqrt(1-u^4)][18]

## References

Del&eacute;glise, M. and Rivat, J. "Computing the Summation of the M&ouml;bius Function." *Experiment. Math.***5**, 291-295, 1996. Derbyshire, J. *[Prime Obsession: Bernhard Riemann and the Greatest Unsolved Problem in Mathematics.][19]*New York: Penguin, p. 250, 2004. Havil, J. *[Gamma: Exploring Euler's Constant.][20]*Princeton, NJ: Princeton University Press, pp. 208-210, 2003. Lagarias, J. and Odlyzko, A. "Computing [image: pi(x)]: An Analytic Method." J. Algorithms **8**, 173-191, 1987. Lehman, R. S. "On Liouville's Function." *Math. Comput.***14**, 311-320, 1960. Lehmer, D. H. *[Guide to Tables in the Theory of Numbers.][21]*Bulletin No. 105. Washington, DC: National Research Council, pp. 7-10, 1941. Mertens, F. "&Uuml;ber einige asymptotische Gesetze der Zahlentheorie." *J. reine angew. Math.***77**, 46-62, 1874. Mertens, F. "&Uuml;ber eine zahlentheoretische Funktion." *Akad. Wiss. Wien Math.-Natur. Kl. Sitzungsber. IIa***106**, 761-830, 1897. Odlyzko, A. M. and te Riele, H. J. J. "Disproof of the Mertens Conjecture." *J. reine angew. Math.***357**, 138-160, 1985. Sloane, N. J. A. Sequences [A002321][3] /M0102, [A028442][7], [A084237][6], and [A118684][8] in "The On-Line Encyclopedia of Integer Sequences." Sterneck, R. D. von. "Empirische Untersuchung &uuml;ber den Verlauf der zahlentheoretischer Function [image: sigma(n)=sum_(x=1)^(n)mu(x)] im Intervalle von 0 bis 150 000." *Sitzungsber. der Kaiserlichen Akademie der Wissenschaften Wien, Math.-Naturwiss. Klasse 2a***106**, 835-1024, 1897. Titchmarsh, E. C. *[The Theory of Functions, 2nd ed.][22]*Oxford, England: Oxford University Press, 1960.

## Referenced on Wolfram|Alpha

[Mertens Function][23]

## Cite this as:

[Weisstein, Eric W.][24] "Mertens Function." From **[MathWorld][25] --A Wolfram Resource. [https://mathworld.wolfram.com/MertensFunction.html][26]

## Subject classifications


## Links

[1]: /notebooks/NumberTheoreticFunctions/MertensFunction.nb
[2]: /MoebiusFunction.html
[3]: http://oeis.org/A002321
[4]: /Determinant.html
[5]: /RedhefferMatrix.html
[6]: http://oeis.org/A084237
[7]: http://oeis.org/A028442
[8]: http://oeis.org/A118684
[9]: /RiemannHypothesis.html
[10]: /RiemannZetaFunctionZeros.html
[11]: /RiemannZetaFunction.html
[12]: /NontrivialZero.html
[13]: /Squarefree.html
[14]: /MertensConjecture.html
[15]: /PrimeCountingFunction.html
[16]: https://www.wolframalpha.com/input/?i=birthday+problem+35+people
[17]: https://www.wolframalpha.com/input/?i=CNF+%28P+%26%26+%7EQ%29+%7C%7C+%28R+%26%26+S%29+%7C%7C+%28Q+%26%26+R+%26%26+%7ES%29
[18]: http://www.wolframalpha.com/input/?i=integrate+1%2Fsqrt%281-u%5E4%29
[19]: http://www.amazon.com/exec/obidos/ASIN/0452285259/ref=nosim/ericstreasuretro
[20]: http://www.amazon.com/exec/obidos/ASIN/0691099839/ref=nosim/ericstreasuretro
[21]: http://www.amazon.com/exec/obidos/ASIN/B0007EB62K/ref=nosim/ericstreasuretro
[22]: http://www.amazon.com/exec/obidos/ASIN/0198533497/ref=nosim/ericstreasuretro
[23]: https://www.wolframalpha.com/input/?i=mertens+function
[24]: /about/author.html
[25]: /
[26]: https://mathworld.wolfram.com/MertensFunction.html
