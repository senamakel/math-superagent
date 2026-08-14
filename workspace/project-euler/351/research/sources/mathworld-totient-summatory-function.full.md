<!-- source: https://mathworld.wolfram.com/TotientSummatoryFunction.html | converted from HTML -->

Totient Summatory Function -- from Wolfram MathWorld

# Totient Summatory Function

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: TotientSummatoryFunction]

The [summatory function][2][image: Phi(n)] of the [totient function][3][image: phi(n)] is defined by

[image: Phi(n)] | [image: =] | [image: sum_(k=1)^(n)phi(k)] |

(1)

 |

 | [image: =] | [image: sum_(m=1)^(n)msum_(d|m)(mu(d))/d] |

(2)

 |

 | [image: =] | [image: sum_(d=1)^(n)mu(d)sum_(d^'=1)^(|_n/d_|)d^'] |

(3)

 |

 | [image: =] | [image: 1/2sum_(d=1)^(n)mu(d)|_n/d_|(1+|_n/d_|)] |

(4)

 |

(Hardy and Wright 1979, p. 268), plotted as the red curve above. The first values of [image: Phi(n)] are 1, 2, 4, 6, 10, 12, 18, 22, 28, ... (OEIS [A002088][4]).

[image: Phi(n)] has the asymptotic series

[image: Phi(x)] | [image: &sim;] | [image: 1/(2zeta(2))x^2+O(xlnx)] |

(5)

 |

 | [image: &sim;] | [image: 3/(pi^2)x^2+O(xlnx),] |

(6)

 |

where [image: zeta(z)] is the [Riemann zeta function][5] (Perrot 1881; Nagell 1951, p. 131; Hardy and Wright 1979, p. 268; blue curve above). An improved asymptotic estimate due to Walfisz (1963) is given by

[image:  Phi(x)&sim;(3x^2)/(pi^2)+O[x(lnx)^(2/3)(lnlnx)^(4/3)]. ] |

(7)

 |

[image: TotientInverseSummatory]

Consider the [summatory function][2] of [image: 1/phi(n)],

[image:  S(N)=sum_(n=1)^N1/(phi(n)), ] |

(8)

 |

plotted as the red curve above. For [image: N=1], 2, ..., the first few terms are 1, 2, 5/2, 3, 13/4, 15/4, 47/12, 25/6, ... (OEIS [A028415][6] and [A048049][7]). The sum diverges as [image: N->infty], but Landau (1900) showed that the asymptotic behavior is given by

[image:  S(N)&sim;A(gamma+lnN)+B+O((lnN)/N), ] |

(9)

 |

where [image: gamma] is the [Euler-Mascheroni constant][8],

[image: A] | [image: =] | [image: sum_(k=1)^(infty)([mu(k)]^2)/(kphi(k))] |

(10)

 |

 | [image: =] | [image: (zeta(2)zeta(3))/(zeta(6))] |

(11)

 |

 | [image: =] | [image: (315)/(2pi^4)zeta(3)] |

(12)

 |

 | [image: =] | [image: 1.9435964368...] |

(13)

 |

[image: B] | [image: =] | [image: sum_(k=1)^(infty)([mu(k)]^2lnk)/(kphi(k))] |

(14)

 |

 | [image: =] | [image: 1.18244...] |

(15)

 |

(OEIS [A082695][9]), [image: mu(k)] is the [M&ouml;bius function][10], [image: zeta(z)] is the [Riemann zeta function][5], and [image: p_k] is the [image: k] th prime (Landau 1900; Halberstam and Richert 1974, pp. 110-111; DeKoninck and Ivić 1980, pp. 1-3; Finch 2003, p. 116; Havil 2003, p. 115; Dickson 2005).

[image: A] and [image: B] can also be written as

[image: A] | [image: =] | [image: product_(k=1)^(infty)(1-p_k^(-6))/((1-p_k^(-2))(1-p_k^(-3)))] |

(16)

 |

 | [image: =] | [image: product_(k=1)^(infty)[1+1/(p_k(p_k-1))]] |

(17)

 |

and

[image: B] | [image: =] | [image: Aproduct_(k=1)^(infty)(lnp_k)/(p_k^2-p_k+1)] |

(18)

 |

 | [image: =] | [image: (315)/(2pi^4)zeta(3)product_(k=1)^(infty)(lnp_k)/(p_k^2-p_k+1),] |

(19)

 |

respectively, making these constants similar in form to [Artin's constant][11] (Finch 2003, pp. 116-117).

The sum

[image: C_(totient)] | [image: =] | [image: sum_(n=1)^(infty)1/(nphi(n))] |

(20)

 |

 | [image: =] | [image: zeta(2)product_(p)[1+1/(p^2(p-1))]] |

(21)

 |

 | [image: =] | [image: 2.20386...] |

(22)

 |

(OEIS [A118262][12]) is sometimes known as the totient constant (Niklasch), where

[image:  product_(p)[1+1/(p^2(p-1))]=1.33978... ] |

(23)

 |

(OEIS [A065483][13]) and the products are taken over the primes [image: p].

---

## See also

[Prime Products][14], [Totient Function][3], [Totient Valence Function][15]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [Euler's totient theorem][16]
- [area of an equilateral triangle with side length a][17]
- [d/dx(e^(ax))][18]

## References

DeKoninck, J.-M. and Ivić, A. *[Topics in Arithmetical Functions: Asymptotic Formulae for Sums of Reciprocals of Arithmetical Functions and Related Fields.][19]*Amsterdam, Netherlands: North-Holland, 1980. Dickson, L. E. *[History of the Theory of Numbers, Vol. 1: Divisibility and Primality.][20]*New York: Dover, pp. 113-158, 2005. Finch, S. R. "Euler Totient Constants." &sect;2.7 in *[Mathematical Constants.][21]*Cambridge, England: Cambridge University Press, pp. 115-119, 2003. Halberstam, H. and Richert, H.-E. *[Sieve Methods.][22]*New York: Academic Press, 1974. Hardy, G. H. and Wright, E. M. "The Average Order of [image: phi(n)]." &sect;18.5 in *[An Introduction to the Theory of Numbers, 5th ed.][23]*Oxford, England: Clarendon Press, pp. 268-269, 1979. Havil, J. *[Gamma: Exploring Euler's Constant.][24]*Princeton, NJ: Princeton University Press, 2003. Landau, E. "&Uuml;ber die zahlentheoretische Function [image: phi(n)] und ihre Beziehung zum Goldbachschen Satz." *Nachr. K&ouml;niglichen Ges. Wiss. G&ouml;ttingen, Math.-Phys. Klasse*, 177-186, 1900. *Werke, Vol. 1*(Ed. L. Mirsky, I. J. Schoenberg, W. Schwarz, and H. Wefelscheid). Thales Verlag, pp. 106-115, 1983. Mitrinović, D. S. and S&aacute;ndor, J. &sect;I.27 in *[Handbook of Number Theory.][25]*Dordrecht, Netherlands: Kluwer, 1995. Nagell, T. "Relatively Prime Numbers. Euler's [image: phi] -Function." &sect;8 in *[Introduction to Number Theory.][26]*New York: Wiley, pp. 23-26, 1951. Niklasch, G. "Some Number-Theoretical Constants." [https://guests.mpim-bonn.mpg.de/moree/Moree.en.html][27]. Perrot, J. 1811. Quoted in Dickson, L. E. *[History of the Theory of Numbers, Vol. 1: Divisibility and Primality.][20]*New York: Dover, p. 126, 2005. Sloane, N. J. A. Sequences [A028415][6], [A048049][7], [A065483][13], [A082695][9], [A085609][28], [A098468][29], and [A118262][12] in "The On-Line Encyclopedia of Integer Sequences." Stephens, P. J. "Prime Divisor of Second-Order Linear Recurrences, I." *J. Number Th.***8**, 313-332, 1976. Walfisz, A. Ch. 5 in *Weyl'sche Exponentialsummen in der neueren Zahlentheorie.*Berlin: Deutscher Verlag der Wissenschaften, 1963.

## Referenced on Wolfram|Alpha

[Totient Summatory Function][30]

## Cite this as:

[Weisstein, Eric W.][31] "Totient Summatory Function." From **[MathWorld][32] --A Wolfram Resource. [https://mathworld.wolfram.com/TotientSummatoryFunction.html][33]

## Subject classifications


## Links

[1]: /notebooks/NumberTheoreticFunctions/TotientSummatoryFunction.nb
[2]: /SummatoryFunction.html
[3]: /TotientFunction.html
[4]: http://oeis.org/A002088
[5]: /RiemannZetaFunction.html
[6]: http://oeis.org/A028415
[7]: http://oeis.org/A048049
[8]: /Euler-MascheroniConstant.html
[9]: http://oeis.org/A082695
[10]: /MoebiusFunction.html
[11]: /ArtinsConstant.html
[12]: http://oeis.org/A118262
[13]: http://oeis.org/A065483
[14]: /PrimeProducts.html
[15]: /TotientValenceFunction.html
[16]: https://www.wolframalpha.com/input/?i=Euler%27s+totient+theorem
[17]: https://www.wolframalpha.com/input/?i=area+of+an+equilateral+triangle+with+side+length+a
[18]: https://www.wolframalpha.com/input/?i=d%2Fdx%28e%5E%28ax%29%29
[19]: http://www.amazon.com/exec/obidos/ASIN/0444860495/ref=nosim/ericstreasuretro
[20]: http://www.amazon.com/exec/obidos/ASIN/0486442322/ref=nosim/ericstreasuretro
[21]: http://www.amazon.com/exec/obidos/ASIN/0521818052/ref=nosim/ericstreasuretro
[22]: http://www.amazon.com/exec/obidos/ASIN/0123182506/ref=nosim/ericstreasuretro
[23]: http://www.amazon.com/exec/obidos/ASIN/0198531710/ref=nosim/ericstreasuretro
[24]: http://www.amazon.com/exec/obidos/ASIN/0691099839/ref=nosim/ericstreasuretro
[25]: http://www.amazon.com/exec/obidos/ASIN/0792338235/ref=nosim/ericstreasuretro
[26]: http://www.amazon.com/exec/obidos/ASIN/0828401632/ref=nosim/ericstreasuretro
[27]: https://guests.mpim-bonn.mpg.de/moree/Moree.en.html
[28]: http://oeis.org/A085609
[29]: http://oeis.org/A098468
[30]: https://www.wolframalpha.com/input/?i=totient+summatory+function
[31]: /about/author.html
[32]: /
[33]: https://mathworld.wolfram.com/TotientSummatoryFunction.html
