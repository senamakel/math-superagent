<!-- source: https://www.cut-the-knot.org/Curriculum/Geometry/EllipseInArbelos.shtml | converted from HTML -->

Ellipse in Arbelos

- Site

  - [What's new][1]
  - [Content page][2]
  - [Front page][3]
  - [Index page][4] [CTK wiki-math][5] -->
  - [About][6]
  - [Privacy policy][7]
  - [Help with math][8]

- Subjects

  - [Arithmetic][9]
  - [Algebra][10]
  - [Geometry][11]
  - [Probability][12]
  - [Trigonometry][13]
  - [Visual illusions][14]

- Articles

  - [Cut the knot!][15]
  - [What is what?][16] [Manifesto][17] -->
  - [Inventor's paradox][18]
  - [Math as language][19] [CTK Insights blog][20] -->
  - [Problem solving][21]

- Collections

  - [Outline mathematics][22]
  - [Book reviews][23]
  - [Interactive activities][24]
  - [Did you know?][25]
  - [Eye opener][26]
  - [Analogue gadgets][27] [Math Olympiads][28] -->
  - [Proofs in mathematics][29]
  - [Things impossible][30]
  - [Index/Glossary][31]

- Simple math

  - [Fast Arithmetic Tips][32]
  - [Stories for young][33]
  - [Word problems][34]
  - [Games and puzzles][35]
  - [Our logo][36]
  - [Make an identity][37]
  - [Elementary geometry][38]

Misc

  - [CutTheKnotMath facebook page][39]
  - [CutTheKnotMath twitter account][40]
  - [CTK Insights blog][41]
  - [Tell a friend][42]
  - Talk about it --> [image: facebook.png] [43] --> -->

[image: facebook.png] [44][image: tweeter.png] [40] --> [image: ctklogo.png] [45]

# Ellipse in Arbelos

Here is a problem (E 762) from the 1947 *American Mathematical Monthly*. It was proposed by J. R. Van Andel, Naval Air Experimental Station, Philadelphia, Pa. (The solution below is by Norman Anning, Ann Arbor, Michigan):

 |

Let A 1 and A 2 be two circles with radii a 1 and a 2 and centers (a 1, 0) and (a 2, 0), respectively, with a 2 > a 1 > 0. Let C be any circle in the crescent shaped area M between A 1 and A 2, and tangent to both A 1 and A 2.

  1.

The locus of the center of C as it sweeps out M is an ellipse with semiaxes the [arithmetic mean][46] (a 1 + a 2)/2 and the [geometric mean][46] &radic; (a 1 a 2) of the radii a 1 and a 2.

  2.

If C t is a circle of radius r t and center P t (x t, y t) where

    - &phi; t = a 1 a 2 + t&sup2; (a 2 - a 1)&sup2;,
    - r t = a 1 a 2 (a 2 - a 1) / &phi; t,
    - x t = a 1 a 2 (a 2 + a 1) / &phi; t,
    - y t = 2t r t.

then, for any real value of t, C t lies in M and is tangent to A 1, A 2, and C t-1.

 |

 |

---

### This applet requires Sun's Java VM 2 which your browser may perceive as a popup. Which it is not. If you want to see the applet work, visit Sun's website at https://www.java.com/en/download/index.jsp, download and install Java VM and enjoy the applet.

---

 |

Buy this applet
--> [What if applet does not run?][47] |

Solution

### References

  1. J. R. Van Andel,; Norman Anning, *American Mathematical Monthly*, Vol. 54, No. 9. (Nov., 1947), pp. 547-548.

[|Activities|][48] [|Contact|][49] [|Front page|][50] [|Contents|][51] [|Geometry|][52]

Copyright &copy; 1996-2018 [Alexander Bogomolny][53]

Part (a) is elementary. A glance at a figure shows that the center of C is always in such a position that the sum of its distances from (a 1, 0) and (a 2 0) is a 1 + a 2.

 |  |

That the major semiaxis of the ellipse is (a 1 + a 2)/2 is indeed rather obvious. To determine the minor semiaxis, consider circle C with the center at the topmost point of the ellipse. The triangle of the centers of the three circles will then be isosceles, with the legs equal to (a 1 + a 2)/2 and the base a 2 - a 1. The altitude h of the triangle is found from the [Pythagorean theorem][54]:

 | h&sup2; = [(a 1 + a 2)/2]&sup2; - [(a 2 - a 1)/2]&sup2;,  |

so that indeed, h&sup2; = a 1 a 2. (These two facts are easily [extended to a more general shape][55].)

 |

---

### This applet requires Sun's Java VM 2 which your browser may perceive as a popup. Which it is not. If you want to see the applet work, visit Sun's website at https://www.java.com/en/download/index.jsp, download and install Java VM and enjoy the applet.

---

 |

Buy this applet
--> [What if applet does not run?][47] |

For part (b), let (X, Y) be a generic point on C t. Then

(1) | (X&sup2; + Y&sup2;)&middot;&phi; t - 2a 1 a 2 (a 1 + a 2)X - 4t a 1 a 2 (a 2 - a 1)Y + 4(a 1 a 2)&sup2; = 0.  |

Apply to C t the [inversion][56]

 | X = 4a 1 a 2 x / (x&sup2; + y&sup2;),
Y = 4a 1 a 2 y / (x&sup2; + y&sup2;).  |

Then (1) becomes

 | x&sup2; + y&sup2; - 2(a 1 + a 2)x - 4t(a 2 - a 1)y + 4&phi; t = 0,  |

which may be rewritten as

(2) | (x - a 1 - a 2)&sup2; + (y - 2ta 2 + 2ta 1)&sup2; = (a 2 - a 1)&sup2;.  |

With t as parameter, (2) is the family of equal circles which touch the parallel lines x = 2a 1 and x = 2a 2. In this family, for every t, the circle C t is tangent to C t-1 because the distance between their centers, 2(a 2 - a 1), is equal to the diameter of either.

Now invert again. Circle C 0 inverts into itself and (2) inverts into (1). The line x = 2a 2 inverts into the circle A 1, the inner boundary of the arbelos. Similarly, x = 2a 1 inverts into A 2, the outer boundary. Since it is well known that inversion turns circles into circles and preserves contacts, the proof of the stated theorem is complete.

The solution in the *Monthly*is followed by the following note:

One tracing the history of the problem would find it under arbelos. See R. Johnson's *Modern Geometry*, for instance. The [neatest of the properties][57], y t = 2tr t, appears in book 4 of Pappus's Collection. See Ivor Thomas, **[Greek Mathematical Works][58], II (Loeb Classical Library, No. 362), p. 578.

The proposer pointed out that J. Steiner in *Geometrische Betrachtungen*(1826) discussed, in particular, the chains of circles corresponding to the sequences t = 0, 1, 2, ... and t = 1/2, 3/2, 5/2, ... Williams mentioned several additional properties of the figure which easily follow from the inversion. For instance, the line joining the points of contact of C t with A 1 and A 2 passes through the fixed point (2a 1 a 2 /(a 1 + a 2), 0); the common internal tangent of C t and C t-1 passes through this same point; the four points consisting of the origin, the centers of A 1 and A 2, and the above point form a [harmonic set][59]. If the diameter of A 1 is taken as two-thirds that of A 2, then r 1 is one-seventh the diameter of A 2. Of this particular figure Victor Th&eacute;bault has stated a very pretty property. Let the diameter of A 2 taken along the line of centers of A 1 and A 2 be OB, and let BM be the tangent from B to the circle A 1. Then the circle on BM as diameter is tangent to the circle C 1.

    - [Arbelos - the Shoemaker's Knife][60]
    - [7 = 2 + 5 Sangaku][61]
    - [Another Pair of Twins in Arbelos][62]
    - [Archimedes' Quadruplets][63]
    - [Archimedes' Twin Circles and a Brother][64]
    - [Book of Lemmas: Proposition 5][65]
    - [Book of Lemmas: Proposition 6][66]
    - [Chain of Inscribed Circles][57]
    - [Concurrency in Arbelos][67]
    - [Concyclic Points in Arbelos][68]
    - Ellipse in Arbelos
    - [Gothic Arc][69]
    - [Pappus Sangaku][70]
    - [Rectangle in Arbelos][71]
    - [Squares in Arbelos][72]
    - [The Area of Arbelos][73]
    - [Twin Segments in Arbelos][74]
    - [Two Arbelos, Two Chains][75]
    - [A Newly Born Pair of Siblings to Archimedes' Twins][76]
    - [Concurrence in Arbelos][77]
    - [Arbelos' Morsels][78]

## Ellipse

### [Conic Sections][79] > Ellipse

    - [What Is Ellipse?][80]
    - [Analog device simulation for drawing ellipses][81]
    - [Angle Bisectors in Ellipse][82]
    - [Angle Bisectors in Ellipse II][83]
    - [Between Major and Minor Circles][84]
    - [Brianchon in Ellipse][85]
    - [Butterflies in Ellipse][86]
    - [Concyclic Points of Two Ellipses with Orthogonal Axes][87]
    - [Conic in Hexagon][88]
    - [Conjugate Diameters in Ellipse][89]
    - [Dynamic construction of ellipse and other curves][90]
    - [Ellipse Between Two Circles][55]
    - Ellipse in Arbelos
    - [Ellipse Touching Sides of Triangle at Midpoints][91]
    - [Euclidean Construction of Center of Ellipse][92]
    - [Euclidean Construction of Tangent to Ellipse][93]
    - [Focal Definition of Ellipse][94]
    - [Focus and Directrix of Ellipse][95]
    - [From Foci to a Tangent in Ellipse][96]
    - [Gergonne in Ellipse][97]
    - [Pascal in Ellipse][98]
    - [La Hire's Theorem in Ellipse][99]
    - [Maximum Perimeter Property of the Incircle][100]
    - [Optical Property of Ellipse][101]
    - [Parallel Chords in Ellipse][102]
    - [Poncelet Porism in Ellipses][103]
    - [Reflections in Ellipse][104]
    - [Three Squares and Two Ellipses][105]
    - [Three Tangents, Three Chords in Ellipse][106]
    - [Van Schooten's Locus Problem][107]
    - [Two Circles, Ellipse, and Parallel Lines][108]

[|Activities|][48] [|Contact|][49] [|Front page|][50] [|Contents|][51] [|Geometry|][52]

Copyright &copy; 1996-2018 [Alexander Bogomolny][53]

74474541

[image: Cut the knot: learn to enjoy mathematics] -->

-->


## Links

[1]: /changes.shtml
[2]: /content.shtml
[3]: /front.shtml
[4]: /index.shtml
[5]: https://www.cut-the-knot.org/wiki-math/index.php
[6]: /wanted.shtml
[7]: /Privacy.shtml
[8]: /MathHelp.shtml
[9]: /arithmetic.shtml
[10]: /algebra.shtml
[11]: /geometry.shtml
[12]: /probability.shtml
[13]: /WhatIs/WhatIsTrigonometry.shtml
[14]: /VisualIllusions.shtml
[15]: /ctk/index.shtml
[16]: /WhatIs/index.shtml
[17]: /manifesto/index.shtml
[18]: /Generalization/epairs.shtml
[19]: /language/index.shtml
[20]: http://www.mathteacherctk.com/blog/
[21]: /m/ProblemSolving.shtml
[22]: /Outline/index.shtml
[23]: /books/Reviews/index.shtml
[24]: /Curriculum/index.shtml
[25]: /do_you_know/index.shtml
[26]: /pythagoras/tricky.shtml
[27]: /pythagoras/ellipse.shtml
[28]: https://www.cut-the-knot.org/wiki-math/index.php?n=MathematicalOlympiads.MathematicalOlympiads
[29]: /proofs/index.shtml
[30]: https://www.cut-the-knot.org/impossible/index.shtml
[31]: /glossary/atop.shtml
[32]: /arithmetic/rapid/index.shtml
[33]: /ForYoung/Introduction.shtml
[34]: /arithmetic/WProblem.shtml
[35]: /games.shtml
[36]: /logo.shtml
[37]: /Curriculum/Arithmetic/MakeIdentity/index.shtml
[38]: /Curriculum/index.shtml#ElementaryGeometry
[39]: https://www.facebook.com/CutTheKnotMath/
[40]: https://twitter.com/CutTheKnotMath
[41]: http://mathteacherctk.com/blog
[42]: /PHP/SpeakLoud.php
[43]: https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Fwww.cut-the-knot.org%2F%23.VNvfpq1i_NQ.facebook&p[title]=CutTheKnotMath&display=popup
[44]: https://www.facebook.com/CutTheKnotMath
[45]: https://www.cut-the-knot.org/
[46]: https://www.cut-the-knot.org/Generalization/means.shtml
[47]: https://www.cut-the-knot.org/HelpWithJava.shtml
[48]: https://www.cut-the-knot.org/Curriculum/index.shtml
[49]: https://www.cut-the-knot.org/MailNotificationPage.shtml
[50]: https://www.cut-the-knot.org/front.shtml
[51]: https://www.cut-the-knot.org/content.shtml
[52]: https://www.cut-the-knot.org/geometry.shtml
[53]: https://www.cut-the-knot.org
[54]: https://www.cut-the-knot.org/pythagoras/index.shtml
[55]: https://www.cut-the-knot.org/Curriculum/Geometry/EllipseBetweenCircles.shtml
[56]: https://www.cut-the-knot.org/Curriculum/Geometry/InversionDemo.shtml
[57]: https://www.cut-the-knot.org/Curriculum/Geometry/InversionInArbelos.shtml
[58]: https://www.amazon.com/exec/obidos/ISBN=0674993993/ctksoftwareincA/
[59]: https://www.cut-the-knot.org/pythagoras/HarmonicRatio.shtml#hrcq
[60]: https://www.cut-the-knot.org/proofs/arbelos.shtml
[61]: https://www.cut-the-knot.org/pythagoras/725Sangaku.shtml
[62]: https://www.cut-the-knot.org/Curriculum/Geometry/OtherTwins.shtml
[63]: https://www.cut-the-knot.org/Curriculum/Geometry/ArchimedesQuadruplets.shtml
[64]: https://www.cut-the-knot.org/Curriculum/Geometry/CircleTriplet.shtml
[65]: https://www.cut-the-knot.org/Curriculum/Geometry/BookOfLemmas/BOL5.shtml
[66]: https://www.cut-the-knot.org/Curriculum/Geometry/BookOfLemmas/BOL6.shtml
[67]: https://www.cut-the-knot.org/Curriculum/Geometry/ArbelosIncircle.shtml
[68]: https://www.cut-the-knot.org/Curriculum/Geometry/ArbelosConcyclic.shtml
[69]: https://www.cut-the-knot.org/Curriculum/Geometry/GothicArc.shtml
[70]: https://www.cut-the-knot.org/pythagoras/SteinerSangaku.shtml
[71]: https://www.cut-the-knot.org/Curriculum/Geometry/ArbelosRect.shtml
[72]: https://www.cut-the-knot.org/Curriculum/Geometry/SquaresInArbelos.shtml
[73]: https://www.cut-the-knot.org/Curriculum/Geometry/ArbelosPWW.shtml
[74]: https://www.cut-the-knot.org/Curriculum/Geometry/TwoSegmentsInArbelos.shtml
[75]: https://www.cut-the-knot.org/pythagoras/ChainsInDoubleArbelos.shtml
[76]: https://www.cut-the-knot.org/Curriculum/Geometry/ArbelosBui.shtml
[77]: https://www.cut-the-knot.org/m/Geometry/GarciaArbelos.shtml
[78]: https://www.cut-the-knot.org/proofs/ArbelosMorsel.shtml
[79]: https://www.cut-the-knot.org/proofs/conics.shtml
[80]: https://www.cut-the-knot.org/WhatIs/WhatIsEllipse.shtml
[81]: https://www.cut-the-knot.org/pythagoras/ellipse.shtml
[82]: https://www.cut-the-knot.org/Curriculum/Geometry/AngleBisectorsInEllipse.shtml
[83]: https://www.cut-the-knot.org/Curriculum/Geometry/AngleBisectorsInEllipse2.shtml
[84]: https://www.cut-the-knot.org/Curriculum/Geometry/EllipseDescartes.shtml
[85]: https://www.cut-the-knot.org/Curriculum/Geometry/BrianchonInEllipse.shtml
[86]: https://www.cut-the-knot.org/Curriculum/Geometry/ButterflyInEllipse.shtml
[87]: https://www.cut-the-knot.org/m/Geometry/EllipsesWithOrthogonalAxes.shtml
[88]: https://www.cut-the-knot.org/m/Geometry/ConicInHexagon.shtml
[89]: https://www.cut-the-knot.org/Curriculum/Geometry/ConjugateDiameters.shtml
[90]: https://www.cut-the-knot.org/Curriculum/Geometry/DynoEllipse.shtml
[91]: https://www.cut-the-knot.org/Curriculum/Geometry/GeoGebra/TriangleThreeCirclesEllipse.shtml
[92]: https://www.cut-the-knot.org/Curriculum/Geometry/TangentTriangleToEllipse.shtml
[93]: https://www.cut-the-knot.org/Curriculum/Geometry/TangentToEllipse.shtml
[94]: https://www.cut-the-knot.org/Curriculum/Geometry/EllipseFocal.shtml
[95]: https://www.cut-the-knot.org/Curriculum/Geometry/EllipseFocusDirectrix.shtml
[96]: https://www.cut-the-knot.org/Curriculum/Geometry/ProductInEllipse.shtml
[97]: https://www.cut-the-knot.org/Curriculum/Geometry/GergonneInEllipse.shtml
[98]: https://www.cut-the-knot.org/Curriculum/Geometry/PascalInEllipse.shtml
[99]: https://www.cut-the-knot.org/Curriculum/Geometry/LaHireOnEllipse.shtml
[100]: https://www.cut-the-knot.org/Curriculum/Geometry/TripolarOptimization.shtml
[101]: https://www.cut-the-knot.org/Curriculum/Geometry/ReflectionInEllipse.shtml
[102]: https://www.cut-the-knot.org/Curriculum/Geometry/ParallelChordsInEllipse.shtml
[103]: https://www.cut-the-knot.org/Curriculum/Geometry/PonceletInEllipse.shtml
[104]: https://www.cut-the-knot.org/Curriculum/Geometry/EnvelopesInEllipse.shtml
[105]: https://www.cut-the-knot.org/Curriculum/Geometry/TwoEllipsesThreeSquares.shtml
[106]: https://www.cut-the-knot.org/Curriculum/Geometry/TTTSinEllipse.shtml
[107]: https://www.cut-the-knot.org/Curriculum/Geometry/EllipseByVanSchooten.shtml
[108]: https://www.cut-the-knot.org/pythagoras/CircleCircleEllipse.shtml
