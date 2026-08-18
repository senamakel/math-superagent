<!-- source: https://mathworld.wolfram.com/DehnInvariant.html | converted from HTML -->

Dehn Invariant -- from Wolfram MathWorld

# Dehn Invariant

---

The Dehn invariant is a constant defined using the angles and edge lengths of a three-dimensional [polyhedron][1]. It is significant because it remains constant under [polyhedron dissection][2] and reassembly.

Dehn (1902) showed that two interdissectable polyhedra must have equal Dehn invariants, settling the third of [Hilbert's problems][3]. Later, Sydler (1965) showed that two polyhedra can be dissected into each other [iff][4] they have the same volume and the same Dehn invariant.

Having Dehn invariant zero is [necessary][5] (but not [sufficient][6]) for a polyhedron to be [space-filling][7]. In general, as a result of the above, a polyhedron is either itself space-filling or else can be cut up and reassembled into a space-filling polyhedron [iff][4] its Dehn invariant is zero.

[Zonohedra][8] have Dehn invariant 0.

Every [rational tetrahedron][9] has Dehn invariant zero because all six of its [dihedral angles][10] vanish modulo [rational][11] multiples of [image: pi]. Rational tetrahedra therefore form a special subclass of the Dehn-invariant-zero tetrahedra (Chentouf and Sun 2023).

Conway *et al. *(1999) call an angle [image: theta] a "pure geodetic angle"' if any one (and therefore each) of its six squared trigonometric functions is rational (or infinite), use "mixed geodetic angle" to mean a linear combination of pure geodetic angles with rational coefficients, and define certain angles [image: <p>_d] for prime [image: p] and square-free positive integer [image: d]. They then show that every pure geodetic angle is uniquely expressible as a rational multiple of [image: pi] plus an integral linear combination of the angles [image: <p>_d], meaning the angles [image: <p>_d] supplemented by [image: pi] form a basis for the space of mixed geodetic angles. They then show that if [image: tantheta=bsqrt(d)/a] for integers [image: a], [image: b], [image: d] with square-free positive [image: d] and with relatively prime [image: a] and [image: b], and if the prime factorization of [image: a^2+db^2] is [image: p_1p_2...p_n] (including multiplicity), then

[image:  theta=tpi+/-<p_1>_d+/-<p_2>_d+/-...+/-<p_n>_d, ] |

(1)

 |

for some rational [image: t].

Notable values of [image: <p>_d] include

[image: <3>_2] | [image: =] | [image: sin^(-1)(sqrt(2/3))] |

(2)

 |

 | [image: =] | [image: cos^(-1)(sqrt(1/3))] |

(3)

 |

 | [image: =] | [image: tan^(-1)(sqrt(2))] |

(4)

 |

 | [image: =] | [image: 0.95531...] |

(5)

 |

 | [image: =] | [image: 1/2pi-1/2alpha_t] |

(6)

 |

 | [image: =] | [image: 54 degrees44^'8.2^('')] |

(7)

 |

[image: <3>_5] | [image: =] | [image: 1/2sin^(-1)(sqrt(5/9))] |

(8)

 |

 | [image: =] | [image: tan^(-1)(sqrt(1/5))] |

(9)

 |

 | [image: =] | [image: 0.42053...] |

(10)

 |

 | [image: =] | [image: 1/4pi-1/2alpha_i] |

(11)

 |

 | [image: =] | [image: 24 degrees5^'41.4^('')] |

(12)

 |

[image: <5>_1] | [image: =] | [image: sin^(-1)(sqrt(4/5))] |

(13)

 |

 | [image: =] | [image: cos^(-1)(sqrt(1/5))] |

(14)

 |

 | [image: =] | [image: tan^(-1)(2)] |

(15)

 |

 | [image: =] | [image: 1.10714...] |

(16)

 |

 | [image: =] | [image: pi-alpha_d] |

(17)

 |

 | [image: =] | [image: 63 degrees26^'5.8^('')] |

(18)

 |

(Conway *et al. *1999; OEIS [A195696][12], [A188595][13], and [A105199][14]), where [image: alpha_d] is the [dihedral angle][10] of the [regular dodecahedron][15], [image: alpha_i] of the [regular icosahedron][16], and [image: alpha_t] of the [regular tetrahedron][17].

Using these results, Conway *et al. *(1999) give Dehn invariants in terms of the basis of angles [image: <p>_d] for unit [Platonic][18] and non-snub [Archimedean solids][19].

Precomputed Dehn invariants for many polyhedra are implemented in the [Wolfram Language][20] as [PolyhedronData][21] [*poly*, "DehnInvariant"].

---

## See also

[Dihedral Angle][10], [Dissection][22], [Ehrhart Polynomial][23], [Hilbert's Problems][3], [Polyhedron Dissection][2], [Rational Tetrahedron][9]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [11th Boolean function of 2 variables][24]
- [evolution of Wolfram 2,3 every 10th step][25]
- [limit tan(t) as t->pi/2 from the left][26]

## References

Chentouf, A. A. and Sun, Y. "Dehn Invariant Zero Tetrahedra." Dec. 3, 2023. [https://arxiv.org/abs/2312.01282][27]. Conway, J. H.; Radin, C.; and Sadun, L. "On Angles Whose Squared Trigonometric Functions Are Rational." *Discr. Computat. Geom.***22**, 321-332, 1999. Dehn, M. "&Uuml;ber raumgleiche Polyeder." *Nachr. K&ouml;nigl. Ges. der Wiss. zu G&ouml;ttingen f. d. Jahr 1900*, 345-354, 1900. Dehn, M. "&Uuml;ber den Rauminhalt." *Math. Ann.***55**, 465-478, 1902. Kagan, B. "&Uuml;ber die Transformation der Polyeder." *Math. Ann.***57**, 421-424, 1903. Sloane, N. J. A. Sequences [A105199][14], [A188595][13], and [A195696][12] in "The On-Line Encyclopedia of Integer Sequences." Sydler, J.-P. "Conditions n&eacute;cessaires et suffisantes pour l'&eacute;quivalence des poly&egrave;dres de l'espace euclidean &agrave; trois dimensions." *Comment. Math. Helv.***40**, 43-80, 1965.

## Referenced on Wolfram|Alpha

[Dehn Invariant][28]

## Cite this as:

[Weisstein, Eric W.][29] "Dehn Invariant." From **[MathWorld][30] --A Wolfram Resource. [https://mathworld.wolfram.com/DehnInvariant.html][31]

## Subject classifications


## Links

[1]: /Polyhedron.html
[2]: /PolyhedronDissection.html
[3]: /HilbertsProblems.html
[4]: /Iff.html
[5]: /Necessary.html
[6]: /Sufficient.html
[7]: /Space-FillingPolyhedron.html
[8]: /Zonohedron.html
[9]: /RationalTetrahedron.html
[10]: /DihedralAngle.html
[11]: /RationalNumber.html
[12]: http://oeis.org/A195696
[13]: http://oeis.org/A188595
[14]: http://oeis.org/A105199
[15]: /RegularDodecahedron.html
[16]: /RegularIcosahedron.html
[17]: /RegularTetrahedron.html
[18]: /PlatonicSolid.html
[19]: /ArchimedeanSolid.html
[20]: http://www.wolfram.com/language/
[21]: http://reference.wolfram.com/language/ref/PolyhedronData.html
[22]: /Dissection.html
[23]: /EhrhartPolynomial.html
[24]: https://www.wolframalpha.com/input/?i=11th+Boolean+function+of+2+variables
[25]: https://www.wolframalpha.com/input/?i=evolution+of+Wolfram+2%2C3+every+10th+step
[26]: http://www.wolframalpha.com/input/?i=limit+tan%28t%29+as+t-%3Epi%2F2+from+the+left
[27]: https://arxiv.org/pdf/2312.01282
[28]: https://www.wolframalpha.com/input/?i=dehn+invariant
[29]: /about/author.html
[30]: /
[31]: https://mathworld.wolfram.com/DehnInvariant.html
