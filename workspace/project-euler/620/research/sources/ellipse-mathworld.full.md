<!-- source: https://mathworld.wolfram.com/Ellipse.html | converted from HTML -->

Ellipse -- from Wolfram MathWorld

# Ellipse

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: EllipseBipolar]

 |

[image: Ellipse construction]

 |

An ellipse is a curve that is the [locus][2] of all points in the [plane][3] the [sum][4] of whose distances [image: r_1] and [image: r_2] from two fixed points [image: F_1] and [image: F_2] (the [foci][5]) separated by a distance of [image: 2c] is a given [positive][6] constant [image: 2a] (Hilbert and Cohn-Vossen 1999, p. 2). This results in the two-center [bipolar coordinate][7] equation

[image:  r_1+r_2=2a, ] |

(1)

 |

where [image: a] is the [semimajor axis][8] and the [origin][9] of the coordinate system is at one of the [foci][5]. The corresponding parameter [image: b] is known as the [semiminor axis][10].

The ellipse is a [conic section][11] and a [Lissajous curve][12].

An ellipse can be specified in the [Wolfram Language][13] using [Circle][14] [[image: {]*x*, *y*[image: }], [image: {]*a*, *b*[image: }]].

If the endpoints of a segment are moved along two intersecting lines, a fixed point on the segment (or on the line that prolongs it) describes an arc of an ellipse. This is known as the trammel construction of an ellipse (Eves 1965, p. 177).

[image: Elliptic gears]

It is possible to construct elliptical gears that rotate smoothly against one another (Brown 1871, pp. 14-15; Reuleaux and Kennedy 1876, p. 70; Clark and Downward 1930; KMODDL).

The ellipse was first studied by Menaechmus, investigated by Euclid, and named by Apollonius. The [focus][5] and [conic section directrix][15] of an ellipse were considered by Pappus. In 1602, Kepler believed that the orbit of Mars was [oval][16]; he later discovered that it was an ellipse with the Sun at one [focus][5]. In fact, Kepler introduced the word " [focus][5] " and published his discovery in 1609. In 1705 Halley showed that the comet now named after him moved in an elliptical orbit around the Sun (MacTutor Archive). An ellipse rotated about its minor axis gives an [oblate spheroid][17], while an ellipse rotated about its major axis gives a [prolate spheroid][18].

A ray of light passing through a [focus][5] will pass through the other focus after a single bounce (Hilbert and Cohn-Vossen 1999, p. 3). Reflections not passing through a [focus][5] will be tangent to a confocal [hyperbola][19] or ellipse, depending on whether the ray passes between the [foci][5] or not.

Let an ellipse lie along the **[x -axis][20] and find the equation of the figure ( 1) where [image: F_1] and [image: F_2] are at [image: (-c,0)] and [image: (c,0)]. In [Cartesian coordinates][21],

[image:  sqrt((x+c)^2+y^2)+sqrt((x-c)^2+y^2)=2a. ] |

(2)

 |

Bring the second term to the right side and square both sides,

[image:  (x+c)^2+y^2=4a^2-4asqrt((x-c)^2+y^2)+(x-c)^2+y^2. ] |

(3)

 |

Now solve for the [square root][22] term and simplify

[image: sqrt((x-c)^2+y^2)] | [image: =] | [image: -1/(4a)(x^2+2xc+c^2+y^2-4a^2-x^2+2xc-c^2-y^2)] |

(4)

 |

 | [image: =] | [image: -1/(4a)(4xc-4a^2)] |

(5)

 |

 | [image: =] | [image: a-c/ax.] |

(6)

 |

Square one final time to clear the remaining [square root][22],

[image:  x^2-2xc+c^2+y^2=a^2-2cx+(c^2)/(a^2)x^2. ] |

(7)

 |

Grouping the [image: x] terms then gives

[image:  x^2(a^2-c^2)/(a^2)+y^2=a^2-c^2, ] |

(8)

 |

which can be written in the simple form

[image:  (x^2)/(a^2)+(y^2)/(a^2-c^2)=1. ] |

(9)

 |

Defining a new constant

[image:  b^2=a^2-c^2 ] |

(10)

 |

puts the equation in the particularly simple form

[image:  (x^2)/(a^2)+(y^2)/(b^2)=1. ] |

(11)

 |

The parameter [image: b] is called the [semiminor axis][10] by analogy with the parameter [image: a], which is called the [semimajor axis][8] (assuming [image: b<a]). The fact that [image: b] as defined above is actually the [semiminor axis][10] is easily shown by letting [image: r_1] and [image: r_2] be equal. Then two [right triangles][23] are produced, each with [hypotenuse][24][image: a], base [image: c], and height [image: b=sqrt(a^2-c^2)]. Since the largest distance along the minor axis will be achieved at this point, [image: b] is indeed the [semiminor axis][10].

If, instead of being centered at (0, 0), the [center][25] of the ellipse is at ([image: x_0], [image: y_0]), equation ( 11) becomes

[image:  ((x-x_0)^2)/(a^2)+((y-y_0)^2)/(b^2)=1. ] |

(12)

 |

As can be seen from the [Cartesian equation][21] for the ellipse, the curve can also be given by a simple parametric form analogous to that of a [circle][26], but with the [image: x] and [image: y] coordinates having different scalings,

[image: x] | [image: =] | [image: acost] |

(13)

 |

[image: y] | [image: =] | [image: bsint.] |

(14)

 |

The general [quadratic curve][27]

[image:  ax^2+2bxy+cy^2+2dx+2fy+g=0 ] |

(15)

 |

is an ellipse when, after defining

[image: Delta] | [image: =] | [image: |a b d; b c f; d f g|] |

(16)

 |

[image: J] | [image: =] | [image: |a b; b c|] |

(17)

 |

[image: I] | [image: =] | [image: a+c,] |

(18)

 |

[image: Delta!=0], [image: J>0], and [image: Delta/I<0]. Also assume the ellipse is nondegenerate (i.e., it is not a [circle][26], so [image: a!=c], and we have already established is not a point, since [image: J=ac-b^2!=0]). In that case, the center of the ellipse [image: (x_0,y_0)] is given by

[image: x_0] | [image: =] | [image: (cd-bf)/(b^2-ac)] |

(19)

 |

[image: y_0] | [image: =] | [image: (af-bd)/(b^2-ac),] |

(20)

 |

the semi-axis lengths are

[image: a^'] | [image: =] | [image: sqrt((2(af^2+cd^2+gb^2-2bdf-acg))/((b^2-ac)[sqrt((a-c)^2+4b^2)-(a+c)]))] |

(21)

 |

[image: b^'] | [image: =] | [image: sqrt((2(af^2+cd^2+gb^2-2bdf-acg))/((b^2-ac)[-sqrt((a-c)^2+4b^2)-(a+c)])).] |

(22)

 |

and the counterclockwise angle of rotation from the [image: x] -axis to the major axis of the ellipse is

[image:  phi={0   for b=0 and a<c; 1/2pi   for b=0 and a>c; 1/2cot^(-1)((a-c)/(2b))   for b!=0 and a<c; pi/2+1/2cot^(-1)((a-c)/(2b))   for b!=0 and a>c. ] |

(23)

 |

[image: EllipseDirectrix]

The ellipse can also be defined as the [locus][2] of points whose distance from the [focus][5] is proportional to the horizontal distance from a vertical line known as the [conic section directrix][15], where the ratio is [image: <1]. Letting [image: r] be the ratio and [image: d] the distance from the center at which the directrix lies, then in order for this to be true, it must hold at the extremes of the major and minor axes, so

[image:  r=(a-c)/(d-a)=(sqrt(b^2+c^2))/d. ] |

(24)

 |

Solving gives

[image: d] | [image: =] | [image: (a^2)/(sqrt(a^2-b^2))=(a^2)/c] |

(25)

 |

[image: r] | [image: =] | [image: (sqrt(a^2-b^2))/a=c/a.] |

(26)

 |

The [focal parameter][28] of the ellipse is

[image: p] | [image: =] | [image: (b^2)/(sqrt(a^2-b^2))] |

(27)

 |

 | [image: =] | [image: (a^2-c^2)/c] |

(28)

 |

 | [image: =] | [image: (a(1-e^2))/e,] |

(29)

 |

where [image: e] is a characteristic of the ellipse known as the [eccentricity][29], to be defined shortly.

[image: Ellipse4Points]

An ellipse whose axes are parallel to the coordinate axes is uniquely determined by any four non-concyclic points on it, and the ellipse passing through the four points [image: (x_1,y_1)], [image: (x_2,y_2)], [image: (x_3,y_3)], and [image: (x_4,y_4)] has equation

[image:  |x^2 y^2 x y 1; x_1^2 y_1^2 x_1 y_1 1; x_2^2 y_2^2 x_2 y_2 1; x_3^2 y_3^2 x_3 y_3 1; x_4^2 y_4^2 x_4 y_4 1|=0. ] |

(30)

 |

Let four points on an ellipse with axes parallel to the coordinate axes have angular coordinates [image: t_i] for [image: i=1], 2, 3, and 4. Such points are [concyclic][30] when

[image:  s_1s_2s_3+s_1s_2s_4+s_1s_3s_4+s_2s_3s_4-(s_1+s_2+s_3+s_4)=0, ] |

(31)

 |

where the intermediate variable [image: s_i=tan(t_i/2)] has been defined (Berger *et al. *1984; Trott 2006, pp. 39-40). Rather surprisingly, this same relationship results after simplification of the above where [image: s_i] is now interpreted as [image: s_i=sin(t_i)]. An equivalent, but more complicated, condition is given by

[image:  (s_1^4+s_2^4+s_3^4+s_4^4)+(4s_2^2s_3^2s_1^2+s_2^2s_4^2s_1^2+s_3^2s_4^2s_1^2+s_2^2s_3^2s_4^2)-4(s_2s_3s_4s_1^3+s_2s_3s_4^3s_1+s_2s_3^3s_4s_1+s_2^3s_3s_4s_1)-2(s_2^2s_1^2+s_3^2s_1^2+s_4^2s_1^2+s_2^2s_3^2+s_2^2s_4^2-2s_3^2s_4^2)+8s_2s_3s_4s_1.
=0  ] |

(32)

 |

Like [hyperbolas][19], noncircular ellipses have *two*distinct [foci][5] and two associated [directrices][15], each [conic section directrix][15] being [perpendicular][31] to the line joining the two foci (Eves 1965, p. 275).

Define a new constant [image: 0<=e<1] called the [eccentricity][29] (where [image: e=0] is the case of a [circle][26]) to replace [image: b]

[image:  e=sqrt(1-(b^2)/(a^2)), ] |

(33)

 |

from which it follows that

[image: b] | [image: =] | [image: asqrt(1-e^2)] |

(34)

 |

 | [image: =] | [image: sqrt(a^2-c^2)] |

(35)

 |

[image: c] | [image: =] | [image: sqrt(a^2-b^2)] |

(36)

 |

 | [image: =] | [image: ae] |

(37)

 |

[image: e] | [image: =] | [image: sqrt(1-(b^2)/(a^2))] |

(38)

 |

 | [image: =] | [image: c/a.] |

(39)

 |

The [eccentricity][29] can therefore be interpreted as the position of the [focus][5] as a fraction of the [semimajor axis][8].

[image: EllipseFocus]

If [image: r] and [image: theta] are measured from a [focus][5][image: F] instead of from the center [image: C] (as they commonly are in orbital mechanics) then the equations of the ellipse are

[image: x] | [image: =] | [image: c+rcostheta] |

(40)

 |

[image: y] | [image: =] | [image: rsintheta,] |

(41)

 |

and ( 11) becomes

[image:  ((c+rcostheta)^2)/(a^2)+(r^2sin^2theta)/(b^2)=1. ] |

(42)

 |

Clearing the [denominators][32] gives

[image:  b^2(c^2+2crcostheta+r^2cos^2theta)+a^2r^2sin^2theta=a^2b^2. ] |

(43)

 |

Substituting in [image: sin^2theta=1-cos^2theta] gives

[image:  b^2c^2+2rcb^2costheta+b^2r^2cos^2theta+a^2r^2-a^2r^2cos^2theta=a^2b^2. ] |

(44)

 |

Plugging in to re-express [image: b] and [image: c] in terms of [image: a] and [image: e],

[image:  a^2(1-e^2)a^2e^2+2aea^2(1-e^2)rcostheta+a^2(1-e^2)r^2cos^2theta
 +a^2r^2-a^2r^2cos^2theta=a^2[a^2(1-e^2)].   ] |

(45)

 |

Dividing by [image: -a^2] and simplifying gives

[image:  -r^2+[ercostheta-a(1-e^2)]^2=0, ] |

(46)

 |

which can be solved for [image: r] to obtain

[image:  r=+/-[ercostheta-a(1-e^2)]. ] |

(47)

 |

The sign can be determined by requiring that [image: r] must be [positive][6]. When [image: e=0], ( 47) becomes [image: r=+/-(-a)], but since [image: a] is always [positive][6], we must take the [negative][33] sign, so ( 47) becomes

[image:  r=a(1-e^2)-ercostheta ] |

(48)

 |

[image:  r(1+ecostheta)=a(1-e^2) ] |

(49)

 |

[image:  r=(a(1-e^2))/(1+ecostheta). ] |

(50)

 |

[image: Ellipsex]

The distance from a [focus][5] to a point with horizontal coordinate [image: x] (where the origin is taken to lie at the center of the ellipse) is found from

[image:  costheta=(x-c)/r. ] |

(51)

 |

Plugging this into ( 50) yields

[image:  r+e(x-c)=a(1-e^2) ] |

(52)

 |

[image:  r=a(1-e^2)-e(x-c). ] |

(53)

 |

In [pedal coordinates][34] with the [pedal point][35] at the [focus][5], the equation of the ellipse is

[image:  (b^2)/(p^2)=(2a)/r-1. ] |

(54)

 |

The [arc length][36] of the ellipse is

[image: s(t)] | [image: =] | [image: aE(t,e)] |

(55)

 |

 | [image: =] | [image: aE(t,sqrt(1-(b^2)/(a^2)))] |

(56)

 |

 | [image: =] | [image: bE(t,sqrt(1-(a^2)/(b^2))),] |

(57)

 |

where [image: E(t,e)] is an incomplete [elliptic integral of the second kind][37] with [elliptic modulus][38][image: e] (the eccentricity).

The relationship between the polar angle from the ellipse center [image: theta] and the parameter [image: t] follows from

[image:  theta=tan^(-1)(y/x)=tan^(-1)(b/atant). ] |

(58)

 |

[image: EllipseFunction]

This function is illustrated above with [image: theta] shown as the solid curve and [image: t] as the dashed, with [image: b/a=0.6]. Care must be taken to make sure that the correct branch of the [inverse tangent][39] function is used. As can be seen, [image: theta] weaves back and forth around [image: t], with crossings occurring at multiples of [image: pi/2]. The [curvature][40] and [tangential angle][41] of the ellipse are given by

[image: kappa(t)] | [image: =] | [image: (ab)/((b^2cos^2t+a^2sin^2t)^(3/2))] |

(59)

 |

[image: phi(t)] | [image: =] | [image: tan^(-1)(a/btant).] |

(60)

 |

The entire [perimeter][42][image: p] of the ellipse is given by setting [image: t=2pi] (corresponding to [image: theta=2pi]), which is equivalent to four times the length of one of the ellipse's [quadrants][43],

[image: p] | [image: =] | [image: aE(2pi,e)] |

(61)

 |

 | [image: =] | [image: 4aE(1/2pi,e)] |

(62)

 |

 | [image: =] | [image: 4aE(e),] |

(63)

 |

where [image: E(e)] is a [complete elliptic integral of the second kind][44] with [elliptic modulus][38][image: e] (the eccentricity). The [perimeter][42] can be computed using the rapidly converging [Gauss-Kummer series][45] as

[image: p] | [image: =] | [image: pi(a+b)sum_(n=0)^(infty)(1/2; n)^2h^(2n)] |

(64)

 |

 | [image: =] | [image: pi(a+b)(1+1/4h^2+1/(64)h^4+1/(256)h^6+...)] |

(65)

 |

(OEIS [A056981][46] and [A056982][47]), where [image: (n; k)] is a [binomial coefficient][48] and

[image:  h=(a-b)/(a+b). ] |

(66)

 |

This can also be written analytically as

[image: p] | [image: =] | [image: pi(a+b)_2F_1(-1/2,-1/2;1;h^2)] |

(67)

 |

 | [image: =] | [image: 2(a+b)[2E(h)+2(h^2-1)K(h)],] |

(68)

 |

where [image: _2F_1(a,b;c;z)] is a [hypergeometric function][49], [image: K(k)] is a complete [elliptic integral of the first kind][50].

[image: EllipsePerimeter]

Approximations to the [perimeter][42] include

[image: p] | [image:  approx ] | [image: pisqrt(2(a^2+b^2))] |

(69)

 |

 | [image:  approx ] | [image: pi[3(a+b)-sqrt((a+3b)(3a+b))]] |

(70)

 |

 | [image:  approx ] | [image: pi(a+b)(1+(3h)/(10+sqrt(4-3h))),] |

(71)

 |

where the last two are due to Ramanujan (1913-1914), and ( 71) has a relative error of [image: &sim;3·2^(-17)h^5] for small values of [image: h]. The error surfaces are illustrated above for these functions.

The maximum and minimum distances from the [focus][5] are called the [apoapsis][51] and [periapsis][52], and are given by

[image: r_+] | [image: =] | [image: r_(apoapsis)=a(1+e)] |

(72)

 |

[image: r_-] | [image: =] | [image: r_(periapsis)=a(1-e).] |

(73)

 |

The [area][53] of an ellipse may be found by direct [integration][54]

[image: A] | [image: =] | [image: int_(-a)^aint_(-bsqrt(a^2-x^2)/a)^(bsqrt(a^2-x^2)/a)dydx] |

(74)

 |

 | [image: =] | [image: int_(-a)^a(2b)/asqrt(a^2-x^2)dx] |

(75)

 |

 | [image: =] | [image: (2b)/a{1/2[xsqrt(a^2-x^2)+a^2sin^(-1)(x/(|a|))]}_(x=-a)^a] |

(76)

 |

 | [image: =] | [image: ab[sin^(-1)1-sin^(-1)(-1)]] |

(77)

 |

 | [image: =] | [image: ab[pi/2-(-pi/2)]] |

(78)

 |

 | [image: =] | [image: piab.] |

(79)

 |

The [area][53] can also be computed more simply by making the change of coordinates [image: x^'=(b/a)x] and [image: y^'=y] from the elliptical region [image: R] to the new region [image: R^']. Then the equation becomes

[image:  1/(a^2)(a/bx^')^2+(y^('2))/(b^2)=1, ] |

(80)

 |

or [image: x^('2)+y^('2)=b^2], so [image: R^'] is a [circle][26] of [radius][55][image: b]. Since

[image:  (partialx)/(partialx^')=((partialx^')/(partialx))^(-1)=(b/a)^(-1)=a/b, ] |

(81)

 |

the [Jacobian][56] is

[image: |(partial(x,y))/(partial(x^',y^'))|] | [image: =] | [image: |(partialx)/(partialx^') (partialy)/(partialx^'); (partialx)/(partialy^') (partialy)/(partialy^')|] |

(82)

 |

 | [image: =] | [image: |a/b 0; 0 1|=a/b.] |

(83)

 |

The [area][53] is therefore

[image: intint_(R)dxdy] | [image: =] | [image: intint_(R^')|(partial(x,y))/(partial(x^',y^'))|dx^'dy^'] |

(84)

 |

 | [image: =] | [image: a/bintint_(R^')dx^'dy^'] |

(85)

 |

 | [image: =] | [image: a/b(pib^2)] |

(86)

 |

 | [image: =] | [image: piab,] |

(87)

 |

as before. The [area][53] of an arbitrary ellipse given by the [quadratic equation][57]

[image:  ax^2+bxy+cy^2=1 ] |

(88)

 |

is

[image:  A=(2pi)/(sqrt(4ac-b^2)). ] |

(89)

 |

The [area][53] of an ellipse with semiaxes [image: a] and [image: b] with respect to a [pedal point][35][image: P] is

[image:  A=1/2pi(a^2+b^2+|OP|^2). ] |

(90)

 |

[image: EllipseNormalTangent]

The unit [tangent vector][58] of the ellipse so parameterized is

[image: x_T(t)] | [image: =] | [image: -(asint)/(sqrt(b^2cos^2t+a^2sin^2t))] |

(91)

 |

[image: y_T(t)] | [image: =] | [image: (bcost)/(sqrt(b^2cos^2t+a^2sin^2t)).] |

(92)

 |

A sequence of [normal][59] and [tangent vectors][58] are plotted above for the ellipse.

The [locus][2] of the apex of a variable [cone][60] containing an ellipse fixed in three-space is a [hyperbola][19] through the [foci][5] of the ellipse. In addition, the [locus][2] of the apex of a [cone][60] containing that [hyperbola][19] is the original ellipse. Furthermore, the [eccentricities][29] of the ellipse and [hyperbola][19] are reciprocals. The [locus][2] of centers of a [Pappus chain][61] of [circles][26] is an ellipse. Surprisingly, the locus of the end of a garage door mounted on rollers along a vertical track but extending beyond the track is a quadrant of an ellipse (Wells 1991, p. 66). (The [envelope][62] of the door's positions is an [astroid][63].)

---

## See also

[Circle][26], [Circumellipse][64], [Conic Section][11], [Eccentric Anomaly][65], [Eccentricity][29], [Ellipse Tangent][66], [Elliptic Cone][67], [Elliptic Curve][68], [Elliptic Cylinder][69], [Hyperbola][19], [Inellipse][70], [Lissajous Curve][12], [One-Seventh Ellipse][71], [Oval][16], [Parabola][72], [Paraboloid][73], [Quadratic Curve][27], [Rectellipse][74], [Reflection Property][75], [Rounded Rectangle][76], [Salmon's Theorem][77], [Squircle][78], [Stadium][79], [Steiner Circumellipse][80], [Steiner Inellipse][81] [Explore this topic in the MathWorld classroom][82]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [ellipse][83]
- [arccot x][84]
- [Dynamic][85]

## References

Abbott, P. "On the Perimeter of an Ellipse." *Mathematica J.***11**, 172-185, 2009. Berger, M.; Pansu, P.; Berry, J.-P.; and Saint-Raymond, X. *[Problems in Geometry.][86]*New York: Springer-Verlag, 1984. Beyer, W. H. *[CRC Standard Mathematical Tables, 28th ed.][87]*Boca Raton, FL: CRC Press, pp. 126, 198-199, and 217, 1987. Brown, H. T. *[Five Hundred and Seven Mechanical Movements. Embracing All Those Which Are Most Important in Dynamics, Hydraulics, Hydrostatics, Pneumatics, Steam Engines, Mill and Other Gearing ... and Including Many Movements Never Before Published, and Several Which Have Only Recently Come into Use.][88]*New York: Brown, Coombs & Co., 1871. Casey, J. "The Ellipse." Ch. 6 in *[A Treatise on the Analytical Geometry of the Point, Line, Circle, and Conic Sections, Containing an Account of Its Most Recent Extensions, with Numerous Examples, 2nd ed., rev. enl.][89]*Dublin: Hodges, Figgis, & Co., pp. 201-249, 1893. Clark, W. M. and Downward, V. *Mechanical Models: A Series of Working Models on the Art and Science of Mechanics.*Newark, NJ: Newark Museum, 1930. Courant, R. and Robbins, H. *[What Is Mathematics?: An Elementary Approach to Ideas and Methods, 2nd ed.][90]*Oxford, England: Oxford University Press, p. 75, 1996. Coxeter, H. S. M. "Conics" &sect;8.4 in *[Introduction to Geometry, 2nd ed.][91]*New York: Wiley, pp. 115-119, 1969. Eves, H. *[A Survey of Geometry, rev. ed.][92]*Boston, MA: Allyn & Bacon, 1965. Fukagawa, H. and Pedoe, D. "Ellipses," "Ellipses and One Circle," "Ellipses and Two Circles," "Ellipses and Three Circles," "Ellipses and Many Circles," "Ellipses and Triangles," "Ellipses and Quadrilaterals," "Ellipses, Circles, and Rectangles," and "Ellipses, Circles and Rhombuses." &sect;5.1, 6.1-8.2 in *[Japanese Temple Geometry Problems.][93]*Winnipeg, Manitoba, Canada: Charles Babbage Research Foundation, pp. 50-68, 135-160, 1989. Harris, J. W. and Stocker, H. "Ellipse." &sect;3.8.7 in *[Handbook of Mathematics and Computational Science.][94]*New York: Springer-Verlag, p. 93, 1998. Hilbert, D. and Cohn-Vossen, S. *[Geometry and the Imagination.][95]*New York: Chelsea, pp. 2-3, 1999. Kern, W. F. and Bland, J. R. *[Solid Mensuration with Proofs, 2nd ed.][96]*New York: Wiley, p. 4, 1948. KMODDL: Kinetic Models for Design Digital Library. "Model: 067 Elliptical Gears." [http://kmoddl.library.cornell.edu/model.php?m=557][97]. Lawrence, J. D. *[A Catalog of Special Plane Curves.][98]*New York: Dover, pp. 72-78, 1972. Lockwood, E. H. "The Ellipse." Ch. 2 in *[A Book of Curves.][99]*Cambridge, England: Cambridge University Press, pp. 13-24, 1967. MacTutor History of Mathematics Archive. "Ellipse." [https://mathshistory.st-andrews.ac.uk/Curves/Ellipse/][100]. Ramanujan, S. "Modular Equations and Approximations to [image: pi]." *Quart. J. Pure. Appl. Math.***45**, 350-372, 1913-1914. Reuleaux, F. and Kennedy, A. B. W. (Eds.). *[Kinematics of Machinery: Outlines of a Theory of Machines.][101]*London, England: Macmillan, 1876. Reprinted by New York: Dover, 1976. Sloane, N. J. A. Sequences [A056981][46] and [A056982][47] in "The On-Line Encyclopedia of Integer Sequences." Trott, M. *[The Mathematica GuideBook for Symbolics.][102]*New York: Springer-Verlag, 2006. [https://www.mathematicaguidebooks.org/][103]. Wells, D. *[The Penguin Dictionary of Curious and Interesting Geometry.][104]*London, England: Penguin, pp. 63-67, 1991. Yates, R. C. "Conics." *[A Handbook on Curves and Their Properties.][105]*Ann Arbor, MI: J. W. Edwards, pp. 36-56, 1952.

## Referenced on Wolfram|Alpha

[Ellipse][83]

## Cite this as:

[Weisstein, Eric W.][106] "Ellipse." From **[MathWorld][107] --A Wolfram Resource. [https://mathworld.wolfram.com/Ellipse.html][108]

## Subject classifications


## Links

[1]: /notebooks/PlaneCurves/Ellipse.nb
[2]: /Locus.html
[3]: /Plane.html
[4]: /Sum.html
[5]: /Focus.html
[6]: /Positive.html
[7]: /BipolarCoordinates.html
[8]: /SemimajorAxis.html
[9]: /Origin.html
[10]: /SemiminorAxis.html
[11]: /ConicSection.html
[12]: /LissajousCurve.html
[13]: http://www.wolfram.com/language/
[14]: http://reference.wolfram.com/language/ref/Circle.html
[15]: /ConicSectionDirectrix.html
[16]: /Oval.html
[17]: /OblateSpheroid.html
[18]: /ProlateSpheroid.html
[19]: /Hyperbola.html
[20]: /x-Axis.html
[21]: /CartesianCoordinates.html
[22]: /SquareRoot.html
[23]: /RightTriangle.html
[24]: /Hypotenuse.html
[25]: /Center.html
[26]: /Circle.html
[27]: /QuadraticCurve.html
[28]: /FocalParameter.html
[29]: /Eccentricity.html
[30]: /Concyclic.html
[31]: /Perpendicular.html
[32]: /Denominator.html
[33]: /Negative.html
[34]: /PedalCoordinates.html
[35]: /PedalPoint.html
[36]: /ArcLength.html
[37]: /EllipticIntegraloftheSecondKind.html
[38]: /EllipticModulus.html
[39]: /InverseTangent.html
[40]: /Curvature.html
[41]: /TangentialAngle.html
[42]: /Perimeter.html
[43]: /Quadrant.html
[44]: /CompleteEllipticIntegraloftheSecondKind.html
[45]: /Gauss-KummerSeries.html
[46]: http://oeis.org/A056981
[47]: http://oeis.org/A056982
[48]: /BinomialCoefficient.html
[49]: /HypergeometricFunction.html
[50]: /EllipticIntegraloftheFirstKind.html
[51]: /Apoapsis.html
[52]: /Periapsis.html
[53]: /Area.html
[54]: /Integration.html
[55]: /Radius.html
[56]: /Jacobian.html
[57]: /QuadraticEquation.html
[58]: /TangentVector.html
[59]: /NormalVector.html
[60]: /Cone.html
[61]: /PappusChain.html
[62]: /Envelope.html
[63]: /Astroid.html
[64]: /Circumellipse.html
[65]: /EccentricAnomaly.html
[66]: /EllipseTangent.html
[67]: /EllipticCone.html
[68]: /EllipticCurve.html
[69]: /EllipticCylinder.html
[70]: /Inellipse.html
[71]: /One-SeventhEllipse.html
[72]: /Parabola.html
[73]: /Paraboloid.html
[74]: /Rectellipse.html
[75]: /ReflectionProperty.html
[76]: /RoundedRectangle.html
[77]: /SalmonsTheorem.html
[78]: /Squircle.html
[79]: /Stadium.html
[80]: /SteinerCircumellipse.html
[81]: /SteinerInellipse.html
[82]: /classroom/Ellipse.html
[83]: https://www.wolframalpha.com/input/?i=ellipse
[84]: https://www.wolframalpha.com/input/?i=arccot+x
[85]: https://www.wolframalpha.com/input/?i=Dynamic
[86]: http://www.amazon.com/exec/obidos/ASIN/0387909710/ref=nosim/ericstreasuretro
[87]: http://www.amazon.com/exec/obidos/ASIN/1584882913/ref=nosim/ericstreasuretro
[88]: http://www.amazon.com/exec/obidos/ASIN/1879335638/ref=nosim/ericstreasuretro
[89]: http://www.amazon.com/exec/obidos/ASIN/1418169897/ref=nosim/ericstreasuretro
[90]: http://www.amazon.com/exec/obidos/ASIN/0195105192/ref=nosim/ericstreasuretro
[91]: http://www.amazon.com/exec/obidos/ASIN/0471504580/ref=nosim/ericstreasuretro
[92]: http://www.amazon.com/exec/obidos/ASIN/0205032265/ref=nosim/ericstreasuretro
[93]: http://www.amazon.com/exec/obidos/ASIN/0919611214/ref=nosim/ericstreasuretro
[94]: http://www.amazon.com/exec/obidos/ASIN/0387947469/ref=nosim/ericstreasuretro
[95]: http://www.amazon.com/exec/obidos/ASIN/0821819984/ref=nosim/ericstreasuretro
[96]: http://www.amazon.com/exec/obidos/ASIN/B0007FQY5S/ref=nosim/ericstreasuretro
[97]: http://kmoddl.library.cornell.edu/model.php?m=557
[98]: http://www.amazon.com/exec/obidos/ASIN/0486602885/ref=nosim/ericstreasuretro
[99]: http://www.amazon.com/exec/obidos/ASIN/0521055857/ref=nosim/ericstreasuretro
[100]: https://mathshistory.st-andrews.ac.uk/Curves/Ellipse/
[101]: http://www.amazon.com/exec/obidos/ASIN/0486611248/ref=nosim/ericstreasuretro
[102]: http://www.amazon.com/exec/obidos/ASIN/0387950206/ref=nosim/ericstreasuretro
[103]: https://www.mathematicaguidebooks.org/
[104]: http://www.amazon.com/exec/obidos/ASIN/0140118136/ref=nosim/ericstreasuretro
[105]: http://www.amazon.com/exec/obidos/ASIN/087353039X/ref=nosim/ericstreasuretro
[106]: /about/author.html
[107]: /
[108]: https://mathworld.wolfram.com/Ellipse.html
