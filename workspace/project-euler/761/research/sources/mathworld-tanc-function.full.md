<!-- source: https://mathworld.wolfram.com/TancFunction.html | converted from HTML -->

Tanc Function -- from Wolfram MathWorld

# Tanc Function

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: Tanc]

[image: TancReIm]

[image: TancContours]

By analogy with the [sinc function][2], define the tanc function by

[image:  tanc(z)={(tanz)/z   for z!=0; 1   for z=0. ] |

(1)

 |

Since [image: tanz/z] is not a [cardinal function][3], the "analogy" with the [sinc function][2] is one of functional structure, not mathematical properties. It is quite possible that a better term than [image: tanc(z)], as introduced here, could be coined, although there appears to be no name previously assigned to this function.

The [derivative][4] is given by

[image:  (dtanc(z))/(dz)=(sec^2z)/z-(tanz)/(z^2). ] |

(2)

 |

The [indefinite integral][5] can apparently not be done in [closed form][6] in terms of conventionally defined functions.

[image: TancRoots]

This function commonly arises in problems in physics, where it is desired to determine values of [image: x] for which [image: tanx=x], i.e., [image: tanc(x)=1]. This is a transcendental equation whose first few solutions are given in the following table and illustrated above.

[image: n] | OEIS | root |

0 | 0 |

1 | [A115365][7] | 4.4934094579090641753... |

2 | 7.7252518369377071642... |

3 | 10.904121659428899827... |

4 | 14.066193912831473480... |

5 | 17.220755271930768739... |

The first of these solutions can be given in closed form as

[image:  r_1=j_(3/2,1), ] |

(3)

 |

where [image: j_(n,k)] is the [image: k] th positive root of the [Bessel function of the first kind][8][image: J_n(x)].

The positive solutions can be written explicitly in series form as

[image:  x=q-q^(-1)-2/3q^(-3)-(13)/(15)q^(-5)-(146)/(105)q^(-7)-... ] |

(4)

 |

(OEIS [A079330][9] and [A088989][10]), where the series in [image: q^(-1)] can be found by [series reversion][11] of the series for [image: x+cotx] and

[image:  q=1/2(2k+1)pi ] |

(5)

 |

for [image: k] a [positive integer][12] (D. W. Cantrell, pers. comm., Jan. 3, 2003). In practice, the first three terms of the series often suffice for obtaining approximate solutions.

[image: TancIntegers]

Because of the vertical asymptotes of [image: tanx] as odd multiples of [image: pi/2], this function is much less well-behaved than the [sinc function][2], even as [image: x->infty]. The plot above shows [image: tanc(n)] for integers [image: n]. The values of [image: n] giving incrementally smallest values of [image: tanc(n)] are [image: n=2], 11, 1317811389848379909481978463177998812826691414678853402757616, ...(OEIS [A079331][13]), corresponding to values of [image: -1.09252], [image: -20.541], [image: -54.5197], [image: -74.7721], .... Similarly, the values of [image: n] giving incrementally largest values of [image: tanc(n)] are [image: n=1], 122925461, 534483448, 3083975227, 214112296674652, ... (OEIS [A079332][14]), corresponding to 1.55741, 2.65934, 3.58205, 4.3311, 18.0078, 18.0566, 556.306, ... (D. W. Cantrell, pers. comm., Jan. 3, 2002). The following table (P. Carmody, pers. comm., Nov. 21, 2003) extends these results up through the 194,000 term of the continued fraction. All these extrema correspond to numerators of the continued fraction expansion of [image: pi/2]. In addition, since they must be near an odd multiple of [image: pi/2] in order for [image: tanx] to be large, the corresponding denominators must be odd. There is also a very strong correlation between [image: tanc(n)] and the value of the subsequent term in the continued fraction expansion (i.e., a high value there implies the prior convergent was a good approximation to [image: pi/2]).

smallest | convergent | largest |

1 | 1.55741 |

[image: -1.09252] | 2 |

[image: -20.541] | 4 |

15 | 2.659341 |

17 | 3.582052 |

19 | 4.331096 |

29 | 18.007800 |

[image: -54.519653] | 118 |

[image: -74.772130] | 136 |

233 | 18.056613 |

315 | 556.306227 |

[image: -92.573200] | 1134 |

[image: -103.160192] | 1568 |

[image: -121.345309] | 1718 |

[image: -155.444947] | 2154 |

[image: -246.744810] | 2468 |

[image: -415.804875] | 3230 |

3727 | 2750.202396 |

3763 | 10539.847388 |

[image: -529.446126] | 5187 |

[image: -829.712489] | 8872 |

[image: -958.007133] | 9768 |

[image: -2534.645599] | 11282 |

[image: -5430.634611] | 12284 |

15503 | 24263.751532 |

[image: -12702.238257] | 24604 |

[image: -43181.130288] | 153396 |

156559 | 228085.415076 |

The sequences of maxima and minima are almost certainly unbounded, but it is not known how to prove this fact.

---

## See also

[du Bois-Reymond Constants][15], [Sinc Function][2], [Sinhc Function][16], [Tangent][17]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [tangent][18]
- [1000 to Babylonian][19]
- [cos(x) + 1/2 cos(2x) + 1/4 cos(4x)][20]

## References

Sloane, N. J. A. Sequences [A079330][9], [A088989][10], and [A115365][7] in "The On-Line Encyclopedia of Integer Sequences."

## Referenced on Wolfram|Alpha

[Tanc Function][21]

## Cite this as:

[Weisstein, Eric W.][22] "Tanc Function." From **[MathWorld][23] --A Wolfram Resource. [https://mathworld.wolfram.com/TancFunction.html][24]

## Subject classifications


## Links

[1]: /notebooks/SpecialFunctions/TancFunction.nb
[2]: /SincFunction.html
[3]: /CardinalFunction.html
[4]: /Derivative.html
[5]: /IndefiniteIntegral.html
[6]: /ClosedForm.html
[7]: http://oeis.org/A115365
[8]: /BesselFunctionoftheFirstKind.html
[9]: http://oeis.org/A079330
[10]: http://oeis.org/A088989
[11]: /SeriesReversion.html
[12]: /PositiveInteger.html
[13]: http://oeis.org/A079331
[14]: http://oeis.org/A079332
[15]: /duBois-ReymondConstants.html
[16]: /SinhcFunction.html
[17]: /Tangent.html
[18]: https://www.wolframalpha.com/input/?i=tangent
[19]: https://www.wolframalpha.com/input/?i=1000+to+Babylonian
[20]: https://www.wolframalpha.com/input/?i=cos%28x%29+%2B+1%2F2+cos%282x%29+%2B+1%2F4+cos%284x%29
[21]: https://www.wolframalpha.com/input/?i=tanc+function
[22]: /about/author.html
[23]: /
[24]: https://mathworld.wolfram.com/TancFunction.html
