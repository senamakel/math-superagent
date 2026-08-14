<!-- source: https://mathworld.wolfram.com/VisiblePoint.html | converted from HTML -->

Visible Point -- from Wolfram MathWorld

# Visible Point

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: VisiblePoints]

Two [lattice points][2][image: (x,y)] and [image: (x^',y^')] are mutually visible if the line segment joining them contains no further [lattice points][2]. This corresponds to the requirement that [image: (x^'-x,y^'-y)=1], where [image: (m,n)] denotes the [greatest common divisor][3]. The plots above show the first few points visible from the [origin][4].

[image: VisiblePoints1]

 |

[image: VisiblePoints1]

 |

If a [lattice point][2] is selected at random in two dimensions, the probability that it is visible from the origin is [image: 6/pi^2]. This is also the probability that two [integers][5] picked at random are [relatively prime][6]. If a [lattice point][2] is picked at random in [image: n] dimensions, the probability that it is visible from the [origin][4] is [image: 1/zeta(n)], where [image: zeta(n)] is the [Riemann zeta function][7].

[image: InvisibleSquares]

An invisible figure is a [polygon][8] all of whose vertices (with possibly degenerate edges when restricted on a grid) are invisible from the origin. There are invisible sets of every finite shape. The lower left-hand corner of the invisible squares on a square grid with [image: 0<x<y] having smallest [image: x] -coordinate and side lengths 1 and 2 are (20, 14) and (54, 20), respectively. The first [image: 3×3] invisible square has lower left-hand corner at (42273, 35397) (E. Weisstein, Mar. 1, 2009).

[image: InvisibleSquarePositions]

The first few [image: 1×1] invisible squares occur at [image: (20,14)], [image: (35,14)], [image: (35,20)], [image: (54,44)], [image: (65,39)], ... (OEIS [A157426][9] and [A157427][10]). The first few [image: 2×2] invisible squares occur at [image: (54,20)], [image: (174,98)], [image: (550,114)], [image: (574,368)], [image: (588,494)], ... (OEIS [A157428][11] and [A157429][12]). Both of these sets are plotted above for the first 1000 such squares.

[image: InvisibleBox]

The filled square with lower left-hand corner at (1308, 1274) is the first [image: 2×2] square with [image: 0<x<y] which is completely invisible since its interior point is invisible in addition to its edge midpoints and vertices.

---

## See also

[Euclid's Orchard][13], [Lattice Point][2], [Orchard-Planting Problem][14], [Orchard Visibility Problem][15], [Relatively Prime][6], [Riemann Zeta Function][7]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [Bravais lattice][16]
- [12 by 12 multiplication table][17]
- [find the area between sinx and cosx from 0 to pi][18]

## References

Apostol, T. &sect;3.8 in *[Introduction to Analytic Number Theory.][19]*New York: Springer-Verlag, 1976. Asano, T.; Ghosh, S. K.; and Shermer, T. C. "Visibility in the Plane." Ch. 19 in *[Handbook of Computational Geometry][20]*(Ed. J.-R. Sack and J. Urrutia). Amsterdam, Netherlands: North-Holland, pp. 829-876, 2000. Baake, M.; Grimm, U.; and Warrington, D. H. "Some Remarks on the Visible Points of a Lattice." *J. Phys. A: Math. General***27**, 2669-2674, 1994. Baake, M.; Moody, R. V.; and Pleasants, P. A. B. "Diffraction from Visible Lattice Points and [image: k] th Power Free Integers." 19 Jun 1999. [https://arxiv.org/abs/math/9906132][21]. Gardner, M. *[The Sixth Book of Mathematical Games from Scientific American.][22]*Chicago, IL: University of Chicago Press, pp. 208-210, 1984. Gosper, R. W. and Schroeppel, R. Item 48 in Beeler, M.; Gosper, R. W.; and Schroeppel, R. *HAKMEM.*Cambridge, MA: MIT Artificial Intelligence Laboratory, Memo AIM-239, p. 17, Feb. 1972. [https://www.inwap.com/pdp10/hbaker/hakmem/number.html#item48][23]. Herzog, F. and Stewart, B. M. "Patterns of Visible and Nonvisible Lattice Points." *Amer. Math. Monthly***78**, 487-496, 1971. Mosseri, R. "Visible Points in a Lattice." *J. Phys. A: Math. Gen.***25**, L25-L29, 1992. Schroeder, M. R. "A Simple Function and Its Fourier Transform." *Math. Intell.***4**, 158-161, 1982. Schroeder, M. R. *[Number Theory in Science and Communication, 2nd ed.][24]*New York: Springer-Verlag, 1990. Sloane, N. J. A. Sequences [A157426][9], [A157427][10], [A157428][11], and [A157429][12] in "The On-Line Encyclopedia of Integer Sequences." Steinhaus, H. *[Mathematical Snapshots, 3rd ed.][25]*New York: Dover, pp. 100-101, 1999.

## Referenced on Wolfram|Alpha

[Visible Point][26]

## Cite this as:

[Weisstein, Eric W.][27] "Visible Point." From **[MathWorld][28] --A Wolfram Resource. [https://mathworld.wolfram.com/VisiblePoint.html][29]

## Subject classifications


## Links

[1]: /notebooks/ComputationalGeometry/VisiblePoint.nb
[2]: /LatticePoint.html
[3]: /GreatestCommonDivisor.html
[4]: /Origin.html
[5]: /Integer.html
[6]: /RelativelyPrime.html
[7]: /RiemannZetaFunction.html
[8]: /Polygon.html
[9]: http://oeis.org/A157426
[10]: http://oeis.org/A157427
[11]: http://oeis.org/A157428
[12]: http://oeis.org/A157429
[13]: /EuclidsOrchard.html
[14]: /Orchard-PlantingProblem.html
[15]: /OrchardVisibilityProblem.html
[16]: https://www.wolframalpha.com/input/?i=Bravais+lattice
[17]: https://www.wolframalpha.com/input/?i=12+by+12+multiplication+table
[18]: https://www.wolframalpha.com/input/?i=find+the+area+between+sinx+and+cosx+from+0+to+pi
[19]: http://www.amazon.com/exec/obidos/ASIN/0387901639/ref=nosim/ericstreasuretro
[20]: http://www.amazon.com/exec/obidos/ASIN/0444825371/ref=nosim/ericstreasuretro
[21]: https://arxiv.org/pdf/math/9906132
[22]: http://www.amazon.com/exec/obidos/ASIN/0226282503/ref=nosim/ericstreasuretro
[23]: https://www.inwap.com/pdp10/hbaker/hakmem/number.html#item48
[24]: http://www.amazon.com/exec/obidos/ASIN/3540620060/ref=nosim/ericstreasuretro
[25]: http://www.amazon.com/exec/obidos/ASIN/0486409147/ref=nosim/ericstreasuretro
[26]: https://www.wolframalpha.com/input/?i=visible+point
[27]: /about/author.html
[28]: /
[29]: https://mathworld.wolfram.com/VisiblePoint.html
