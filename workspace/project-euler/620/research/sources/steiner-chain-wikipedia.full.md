<!-- source: https://en.wikipedia.org/wiki/Steiner_chain | converted from HTML -->

Steiner chain - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Set of circles related by tangency

[1] Figure 1: A Steiner chain of twelve black circles (*n*= 12). The given circles are shown in blue and red, which are the outermost and innermost circles, respectively.

In [geometry][2], a **Steiner chain**is a set of n circles, all of which are [tangent][3] to two given non-intersecting [circles][4] (blue and red in Figure 1), where n is finite and each circle in the chain is tangent to the previous and next circles in the chain. In the usual *closed*Steiner chains, the first and last ( n -th) circles are also tangent to each other; by contrast, in *open*Steiner chains, they need not be. The given circles α and β do not intersect, but otherwise are unconstrained; the smaller circle may lie completely inside or outside of the larger circle. In these cases, the centers of Steiner-chain circles lie on an [ellipse][5] or a [hyperbola][6], respectively.

Steiner chains are named after [Jakob Steiner][7], who defined them in the 19th century and discovered many of their properties. A fundamental result is *Steiner's [porism][8]*, which states:

If at least one closed Steiner chain of n circles exists for two given circles α and β, then there is an infinite number of closed Steiner chains of n circles; and any circle tangent to α and β in the same way [a] is a member of such a chain.

The method of [circle inversion][9] is helpful in treating Steiner chains. Since it preserves tangencies, angles and circles, inversion transforms one Steiner chain into another of the same number of circles. One particular choice of inversion transforms the given circles α and β into concentric circles; in this case, all the circles of the Steiner chain have the same size and can "roll" around in the [annulus][10] between the circles similar to [ball bearings][11]. This standard configuration allows several properties of Steiner chains to be derived, e.g., its points of tangencies always lie on a circle. Several generalizations of Steiner chains exist, most notably [Soddy's hexlet][12] and [Pappus chains][13]. [1]

## Definitions and types of tangency

[[edit][14]]

- Steiner chains with different internal/external tangencies
-

[image: The 7 circles of this Steiner chain (black) are externally tangent to the inner given circle (red) but internally tangent to the outer given circle (blue).] [15]

The 7 circles of this Steiner chain (black) are externally tangent to the inner given circle (red) but internally tangent to the outer given circle (blue).

-

[image: The 7 circles of this Steiner chain (black) are externally tangent to both given circles (red and blue), which lie outside one another.] [16]

The 7 circles of this Steiner chain (black) are externally tangent to both given circles (red and blue), which lie outside one another.

-

[image: Seven of the 8 circles of this Steiner chain (black) are externally tangent to both given circles (red and blue); the 8th circle is internally tangent to both.] [17]

Seven of the 8 circles of this Steiner chain (black) are externally tangent to both given circles (red and blue); the 8th circle is internally tangent to both.

The two given circles *α*and *β*cannot intersect; hence, the smaller given circle must lie inside or outside the larger. The circles are usually shown as an [annulus][10], i.e., with the smaller given circle inside the larger one. In this configuration, the Steiner-chain circles are externally tangent to the inner given circle and internally tangent to the outer circle. However, the smaller circle may also lie completely outside the larger one (Figure 2). The black circles of Figure 2 satisfy the conditions for a closed Steiner chain: they are all tangent to the two given circles and each is tangent to its neighbors in the chain. In this configuration, the Steiner-chain circles have the same type of tangency to both given circles, either externally or internally tangent to both. If the two given circles are tangent at a point, the Steiner chain becomes an infinite [Pappus chain][13], which is often discussed in the context of the [arbelos][18] (*shoemaker's knife*), a geometric figure made from three circles. There is no general name for a sequence of circles tangent to two given circles that intersect at two points.

## Closed, open and multi-cyclic

[[edit][19]]

- Closed, open and multi-cyclic Steiner chains
-

[image: Closed Steiner chain of nine circles. The 1st and 9th circles are tangent.] [20]

Closed Steiner chain of nine circles. The 1st and 9th circles are tangent.

-

[image: Open Steiner chain of nine circles. The 1st and 9th circles overlap.] [21]

Open Steiner chain of nine circles. The 1st and 9th circles overlap.

-

[image: Multicyclic Steiner chain of 17 circles in 2 wraps. The 1st and 17th circles touch.] [22]

Multicyclic Steiner chain of 17 circles in 2 wraps. The 1st and 17th circles touch.

The two given circles *α*and *β*touch the *n*circles of the Steiner chain, but each circle *C**k*of a Steiner chain touches only four circles: *α*, *β*, and its two neighbors, *C**k*− 1 and *C**k*+1. By default, Steiner chains are assumed to be *closed*, i.e., the first and last circles are tangent to one another. By contrast, an *open*Steiner chain is one in which the first and last circles, *C*1 and *C**n*, are not tangent to one another; these circles are tangent only to *three*circles. Multicyclic Steiner chains wrap around the inner circle more than once before closing, i.e., before being tangent to the initial circle.

Closed Steiner chains are the systems of circles obtained as the [circle packing theorem][23] representation of a [bipyramid][24].

## Annular case and feasibility criterion

[[edit][25]]

- Annular Steiner chains
-

[image: n = 3] [26]

*n*= 3

-

[image: n = 6] [27]

*n*= 6

-

[image: n = 9] [20]

*n*= 9

-

[image: n = 12] [28]

*n*= 12

-

[image: n = 20] [29]

*n*= 20

[30] The radius of the Steiner circles is *ρ*whereas those of the inner and outer given circles are *r*and *R*, respectively. The distance from the center of the inner circle to the center of a Steiner circle is *r*+ *ρ*(hypotenuse of pink triangle).

The simplest type of Steiner chain is a closed chain of *n*circles of equal size surrounding an inscribed circle of radius *r*; the chain of circles is itself surrounded by a [circumscribed circle][31] of radius *R*. The inscribed and circumscribed given circles are concentric, and the Steiner-chain circles lie in the [annulus][10] between them. By symmetry, the angle 2*θ*between the centers of the Steiner-chain circles is 360°/*n*. Because Steiner chain circles are tangent to one another, the distance between their centers equals the sum of their radii, here twice their radius *ρ*. The bisector (green in Figure) creates two right triangles, with a [central angle][32] of *θ*= 180°/*n*. The [sine][33] of this angle can be written as the length of its opposite segment, divided by the [hypotenuse][34] of the [right triangle][35]

sin ⁡ θ = ρ r + ρ {\displaystyle \sin \theta ={\frac {\rho }{r+\rho }}}[image: {\displaystyle \sin \theta ={\frac {\rho }{r+\rho }}}]

Since *θ*is known from *n*, this provides an equation for the unknown radius *ρ*of the Steiner-chain circles

ρ = r sin ⁡ θ 1 − sin ⁡ θ {\displaystyle \rho ={\frac {r\sin \theta }{1-\sin \theta }}}[image: {\displaystyle \rho ={\frac {r\sin \theta }{1-\sin \theta }}}]

The tangent points of a Steiner chain circle with the inner and outer given circles lie on a line that pass through their common center; hence, the outer radius *R*= *r*+ 2*ρ*.

These equations provide a criterion for the feasibility of a Steiner chain for two given concentric circles. A closed Steiner chain of *n*circles requires that the ratio of radii *R*/*r*of the given circles equal exactly

R r = 1 + 2 sin ⁡ θ 1 − sin ⁡ θ = 1 + sin ⁡ θ 1 − sin ⁡ θ = [sec ⁡ θ + tan ⁡ θ] 2 {\displaystyle {\frac {R}{r}}=1+{\frac {2\sin \theta }{1-\sin \theta }}={\frac {1+\sin \theta }{1-\sin \theta }}=\left[\sec \theta +\tan \theta \right]^{2}}[image: {\displaystyle {\frac {R}{r}}=1+{\frac {2\sin \theta }{1-\sin \theta }}={\frac {1+\sin \theta }{1-\sin \theta }}=\left[\sec \theta +\tan \theta \right]^{2}}]

As shown below, this ratio-of-radii criterion for concentric given circles can be extended to all types of given circles by the [inversive distance][36]*δ*of the two given circles. For concentric circles, this distance is defined as a [logarithm][37] of their ratio of radii

δ = ln ⁡ R r {\displaystyle \delta =\ln {\frac {R}{r}}}[image: {\displaystyle \delta =\ln {\frac {R}{r}}}]

Using the solution for concentric circles, the general criterion for a Steiner chain of *n*circles can be written

δ = 2 ln ⁡ ( sec ⁡ θ + tan ⁡ θ). {\displaystyle \delta =2\ln \left(\sec \theta +\tan \theta \right).}[image: {\displaystyle \delta =2\ln \left(\sec \theta +\tan \theta \right).}]

If a multicyclic annular Steiner chain has *n*total circles and wraps around *m*times before closing, the angle between Steiner-chain circles equals

θ = m n 180 ∘ {\displaystyle \theta ={\frac {m}{n}}180^{\circ }}[image: {\displaystyle \theta ={\frac {m}{n}}180^{\circ }}]

In other respects, the feasibility criterion is unchanged.

## Properties under inversion

[[edit][38]]

- Inversive properties of Steiner chains
-

[image: Two circles (pink and cyan) that are internally tangent to both given circles and whose centers are collinear with the center of the given circles intersect at the angle 2θ.] [39]

Two circles (pink and cyan) that are internally tangent to both given circles and whose centers are collinear with the center of the given circles intersect at the angle 2*θ*.

-

[image: Under inversion, these lines and circles become circles with the same intersection angle, 2θ. The gold circles intersect the two given circles at right angles, i.e., orthogonally.] [40]

Under inversion, these lines and circles become circles with the same intersection angle, 2*θ*. The gold circles intersect the two given circles at right angles, i.e., orthogonally.

-

[image: The circles passing through the mutual tangent points of the Steiner-chain circles are orthogonal to the two given circles and intersect one another at multiples of the angle 2θ.] [41]

The circles passing through the mutual tangent points of the Steiner-chain circles are orthogonal to the two given circles and intersect one another at multiples of the angle 2*θ*.

-

[image: The circles passing through the tangent points of the Steiner-chain circles with the two given circles are orthogonal to the latter and intersect at multiples of the angle 2θ.] [42]

The circles passing through the tangent points of the Steiner-chain circles with the two given circles are orthogonal to the latter and intersect at multiples of the angle 2*θ*.

[Circle inversion][9] transforms one Steiner chain into another with the same number of circles.

In the transformed chain, the tangent points between adjacent circles of the Steiner chain all lie on a circle, namely the concentric circle midway between the two fixed concentric circles. Since tangencies and circles are preserved under inversion, this property of all tangencies lying on a circle is also true in the original chain. This property is also shared with the [Pappus chain][13] of circles, which can be construed as a special limiting case of the Steiner chain.

In the transformed chain, the tangent lines from **O**to the Steiner chain circles are separated by equal angles. In the original chain, this corresponds to equal angles between the tangent circles that pass through the center of inversion used to transform the original circles into a concentric pair.

In the transformed chain, the *n*lines connecting the pairs of tangent points of the Steiner circles with the concentric circles all pass through **O**, the common center. Similarly, the *n*lines tangent to each pair of adjacent circles in the Steiner chain also pass through **O**. Since lines through the center of inversion are invariant under inversion, and since tangency and concurrence are preserved under inversion, the 2*n*lines connecting the corresponding points in the original chain also pass through a single point, **O**.

## Infinite family

[[edit][43]]

[44] If even one closed Steiner chain is possible for two given circles (blue), then infinitely many Steiner chains are possible, all related by rotation. Their points of tangency always fall on a circle (orange). If the two given circles are nested, one inside the other, the centers of the Steiner chain circles (black) fall on an [ellipse][5] (red); otherwise, they fall on a [hyperbola][6].

A Steiner chain between two non-intersecting circles can always be transformed into another Steiner chain of equally sized circles sandwiched between two concentric circles. Therefore, any such Steiner chain belongs to an infinite family of Steiner chains related by rotation of the transformed chain about **O**, the common center of the transformed bounding circles.

## Elliptical/hyperbolic locus of centers

[[edit][45]]

The centers of the circles of a Steiner chain lie on a [conic section][46]. For example, if the smaller given circle lies within the larger, the centers lie on an [ellipse][5]. This is true for any set of circles that are internally tangent to one given circle and externally tangent to the other; such systems of circles appear in the [Pappus chain][13], the [problem of Apollonius][47], and the three-dimensional [Soddy's hexlet][12]. Similarly, if some circles of the Steiner chain are externally tangent to both given circles, their centers must lie on a hyperbola, whereas those that are internally tangent to both lie on a different hyperbola.

The circles of the Steiner chain are tangent to two fixed circles, denoted here as *α*and *β*, where *β*is enclosed by*α*. Let the radii of these two circles be denoted as *r**α*and *r**β*, respectively, and let their respective centers be the points **A**and **B**. Let the radius, diameter and center point of the *k*th circle of the Steiner chain be denoted as *r**k*, *d**k*and **P***k*, respectively.

All the centers of the circles in the Steiner chain are located on a common [ellipse][5], for the following reason. [2] The sum of the distances from the center point of the *k*th circle of the Steiner chain to the two centers **A**and **B**of the fixed circles equals a constant

P k A ¯ + P k B ¯ = ( r α − r k) + ( r β + r k) = r α + r β {\displaystyle {\overline {\mathbf {P} _{k}\mathbf {A} }}+{\overline {\mathbf {P} _{k}\mathbf {B} }}=(r_{\alpha }-r_{k})+\left(r_{\beta }+r_{k}\right)=r_{\alpha }+r_{\beta }}[image: {\displaystyle {\overline {\mathbf {P} _{k}\mathbf {A} }}+{\overline {\mathbf {P} _{k}\mathbf {B} }}=(r_{\alpha }-r_{k})+\left(r_{\beta }+r_{k}\right)=r_{\alpha }+r_{\beta }}]

Thus, for all the centers of the circles of the Steiner chain, the sum of distances to **A**and **B**equals the same constant, *r**α*+*r**β*. This defines an ellipse, whose two [foci][48] are the points **A**and **B**, the centers of the circles, *α*and *β*, that sandwich the Steiner chain of circles.

The sum of distances to the foci equals twice the [semi-major axis][49]*a*of an ellipse; hence,

2 a = r α + r β {\displaystyle 2a=r_{\alpha }+r_{\beta }}[image: {\displaystyle 2a=r_{\alpha }+r_{\beta }}]

Let *p*equal the distance between the foci, **A**and **B**. Then, the [eccentricity][50]*e*is defined by 2 *ae*= *p*, or

e = p 2 a = p r α + r β {\displaystyle e={\frac {p}{2a}}={\frac {p}{r_{\alpha }+r_{\beta }}}}[image: {\displaystyle e={\frac {p}{2a}}={\frac {p}{r_{\alpha }+r_{\beta }}}}]

From these parameters, the [semi-minor axis][51]*b*and the [semi-latus rectum][52]*L*can be determined

b 2 = a 2 ( 1 − e 2) = a 2 − p 2 4 {\displaystyle b^{2}=a^{2}\left(1-e^{2}\right)=a^{2}-{\frac {p^{2}}{4}}}[image: {\displaystyle b^{2}=a^{2}\left(1-e^{2}\right)=a^{2}-{\frac {p^{2}}{4}}}] L = b 2 a = a − p 2 4 a {\displaystyle L={\frac {b^{2}}{a}}=a-{\frac {p^{2}}{4a}}}[image: {\displaystyle L={\frac {b^{2}}{a}}=a-{\frac {p^{2}}{4a}}}]

Therefore, the ellipse can be described by an equation in terms of its distance *d*to one focus

d = L 1 − e cos ⁡ θ {\displaystyle d={\frac {L}{1-e\cos \theta }}}[image: {\displaystyle d={\frac {L}{1-e\cos \theta }}}]

where *θ*is the angle with the line joining the two foci.

## Conjugate chains

[[edit][53]]

- Conjugate Steiner chains with *n*= 4
-

[image: Steiner chain with the two given circles shown in red and blue.] [54]

Steiner chain with the two given circles shown in red and blue.

-

[image: Same set of circles, but with a different choice of given circles.] [55]

Same set of circles, but with a different choice of given circles.

-

[image: Same set of circles, but with yet another choice of given circles.] [56]

Same set of circles, but with yet another choice of given circles.

If a Steiner chain has an even number of circles, then any two diametrically opposite circles in the chain can be taken as the two given circles of a new Steiner chain to which the original circles belong. If the original Steiner chain has *n*circles in *m*wraps, and the new chain has *p*circles in *q*wraps, then the equation holds

m n + p q = 1 2. {\displaystyle {\frac {m}{n}}+{\frac {p}{q}}={\frac {1}{2}}.}[image: {\displaystyle {\frac {m}{n}}+{\frac {p}{q}}={\frac {1}{2}}.}]

A simple example occurs for Steiner chains of four circles (*n*= 4) and one wrap (*m*= 1). In this case, the given circles and the Steiner-chain circles are equivalent in that both types of circles are tangent to four others; more generally, Steiner-chain circles are tangent to four circles, but the two given circles are tangent to *n*circles. In this case, any pair of opposite members of the Steiner chain may be selected as the given circles of another Steiner chain that involves the original given circles. Since *m*=*p*= 1 and *n*=*q*= 4, Steiner's equation is satisfied:

1 4 + 1 4 = 1 2. {\displaystyle {\frac {1}{4}}+{\frac {1}{4}}={\frac {1}{2}}.}[image: {\displaystyle {\frac {1}{4}}+{\frac {1}{4}}={\frac {1}{2}}.}]

## Generalizations

[[edit][57]]

[58] [Soddy's hexlet][12] is a three-dimensional analog of the Steiner chain.

The simplest generalization of a Steiner chain is to allow the given circles to touch or intersect one another. In the former case, this corresponds to a [Pappus chain][13], which has an infinite number of circles.

[Soddy's hexlet][12] is a three-dimensional generalization of a Steiner chain of six circles. The centers of the six spheres (the *hexlet*) travel along the same ellipse as do the centers of the corresponding Steiner chain. The envelope of the hexlet spheres is a [Dupin cyclide][59], the inversion of a [torus][60]. The six spheres are not only tangent to the inner and outer sphere, but also to two other spheres, centered above and below the plane of the hexlet centers.

Multiple rings of Steiner chains are another generalization. An ordinary Steiner chain is obtained by inverting an annular chain of tangent circles bounded by two concentric circles. This may be generalized to inverting three or more concentric circles that sandwich annular chains of tangent circles.

Hierarchical Steiner chains are yet another generalization. If the two given circles of an ordinary Steiner chain are nested, i.e., if one lies entirely within the other, then the larger given circle circumscribes the Steiner-chain circles. In a hierarchical Steiner chain, each circle of a Steiner chain is itself the circumscribing given circle of another Steiner chain within it; this process may be repeated indefinitely, forming a [fractal][61].

## See also

[[edit][62]]

- [Poncelet porism][63]
- [Ford circles][64]
- [Apollonian gasket][65]

## Notes

[[edit][66]]

1. ↑ meaning that the arbitrary circle is internally or externally tangent in the same way as a circle of the original Steiner chain

## References

[[edit][67]]

1. ↑ Ogilvy, p. 60.
2. ↑ Ogilvy, p. 57.

## Bibliography

[[edit][68]]

- [Ogilvy, C. S.][69] (1990). **[Excursions in Geometry][70]. Dover. pp. [51–54][70]. [ISBN][71] [0-486-26530-7][72].
- [Coxeter, H.S.M.][73]; [Greitzer, S.L.][74] (1967). *Geometry Revisited*. New Mathematical Library. Vol. 19. [Washington][75]: [MAA][76]. pp. 123– 126, 175– 176, 180. [ISBN][71] [978-0-88385-619-2][77]. [Zbl][78] [0166.16402][79].
- Johnson RA (1960). *Advanced Euclidean Geometry: An elementary treatise on the geometry of the triangle and the circle*(reprint of 1929 edition by Houghton Mifflin ed.). New York: Dover Publications. pp. 113– 115. [ISBN][71] [978-0-486-46237-0][80].`{{ [cite book][81] }}`: ISBN / Date incompatibility ( [help][82])
- Wells D (1991). **[The Penguin Dictionary of Curious and Interesting Geometry][83]. New York: Penguin Books. pp. [244–245][83]. [ISBN][71] [0-14-011813-6][84].

## Further reading

[[edit][85]]

- Eves H (1972). *A Survey of Geometry*(revised ed.). Boston: Allyn and Bacon. pp. 134– 135. [ISBN][71] [978-0-205-03226-6][86].
- [Pedoe D][87] (1970). *A Course of Geometry for Colleges and Universities*. Cambridge University Press. pp. 97– 101. [ISBN][71] [978-0-521-07638-8][88].
- Coolidge JL (1916). **[A Treatise on the Circle and the Sphere][89]. Oxford: Clarendon Press. pp. 31– 37.

## External links

[[edit][90]]

[image: Wikimedia Commons logo] [91]

Wikimedia Commons has media related to [Steiner chains][92].

- [Weisstein, Eric W.][93] ["Steiner Chain"][94]. *[MathWorld][95]*.
- [Interactive animation of a Steiner chain][96], [CodePen][97]
- [Interactive Applet][98] by Michael Borcherds showing an animation of Steiner's Chain with a variable number of circles made with [GeoGebra][99].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Steiner_chain&oldid=1353686089][100] "

[Categories][101]:

- [Circles][102]
- [Inversive geometry][103]
- [Circle packing][104]

Hidden categories:

- [Articles with short description][105]
- [Short description is different from Wikidata][106]
- [CS1 errors: ISBN date][107]
- [Commons category link is on Wikidata][108]

Search

Steiner chain

10 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Steiner_chain_12mer.svg
[2]: https://en.wikipedia.org/wiki/Geometry
[3]: https://en.wikipedia.org/wiki/Tangent
[4]: https://en.wikipedia.org/wiki/Circle
[5]: https://en.wikipedia.org/wiki/Ellipse
[6]: https://en.wikipedia.org/wiki/Hyperbola
[7]: https://en.wikipedia.org/wiki/Jakob_Steiner
[8]: https://en.wikipedia.org/wiki/Porism
[9]: https://en.wikipedia.org/wiki/Circle_inversion
[10]: https://en.wikipedia.org/wiki/Annulus_(mathematics)
[11]: https://en.wikipedia.org/wiki/Ball_bearing
[12]: https://en.wikipedia.org/wiki/Soddy's_hexlet
[13]: https://en.wikipedia.org/wiki/Pappus_chain
[14]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=1
[15]: https://en.wikipedia.org/wiki/File:Steiner_chain_7mer.svg
[16]: https://en.wikipedia.org/wiki/File:Steiner_chain_7mer_all_external.svg
[17]: https://en.wikipedia.org/wiki/File:Steiner_chain_8mer_all_but_one_external.svg
[18]: https://en.wikipedia.org/wiki/Arbelos
[19]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=2
[20]: https://en.wikipedia.org/wiki/File:Steiner_chain_9mer_annular.svg
[21]: https://en.wikipedia.org/wiki/File:Steiner_chain_open_9mer.svg
[22]: https://en.wikipedia.org/wiki/File:Steiner_chain_double_17mer.svg
[23]: https://en.wikipedia.org/wiki/Circle_packing_theorem
[24]: https://en.wikipedia.org/wiki/Bipyramid
[25]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=3
[26]: https://en.wikipedia.org/wiki/File:Steiner_chain_3mer_annular.svg
[27]: https://en.wikipedia.org/wiki/File:Steiner_chain_6mer_annular.svg
[28]: https://en.wikipedia.org/wiki/File:Steiner_chain_12mer_annular.svg
[29]: https://en.wikipedia.org/wiki/File:Steiner_chain_20mer_annular.svg
[30]: https://en.wikipedia.org/wiki/File:Steiner_chain_annular_angle.svg
[31]: https://en.wikipedia.org/wiki/Circumscribed_circle
[32]: https://en.wikipedia.org/wiki/Central_angle
[33]: https://en.wikipedia.org/wiki/Sine
[34]: https://en.wikipedia.org/wiki/Hypotenuse
[35]: https://en.wikipedia.org/wiki/Right_triangle
[36]: https://en.wikipedia.org/wiki/Inversive_distance
[37]: https://en.wikipedia.org/wiki/Logarithm
[38]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=4
[39]: https://en.wikipedia.org/wiki/File:Steiner_chain_9mer_annular_angle2.svg
[40]: https://en.wikipedia.org/wiki/File:Steiner_chain_9mer_annular_angle4.svg
[41]: https://en.wikipedia.org/wiki/File:Steiner_chain_6mer_tangent_circles.svg
[42]: https://en.wikipedia.org/wiki/File:Steiner_chain_6mer_orthogonal_circles.svg
[43]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=5
[44]: https://en.wikipedia.org/wiki/File:Steiner_chain_animation-50dpi.gif
[45]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=6
[46]: https://en.wikipedia.org/wiki/Conic_section
[47]: https://en.wikipedia.org/wiki/Problem_of_Apollonius
[48]: https://en.wikipedia.org/wiki/Focus_(geometry)
[49]: https://en.wikipedia.org/wiki/Semi-major_axis
[50]: https://en.wikipedia.org/wiki/Eccentricity_(mathematics)
[51]: https://en.wikipedia.org/wiki/Semi-minor_axis
[52]: https://en.wikipedia.org/wiki/Semi-latus_rectum
[53]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=7
[54]: https://en.wikipedia.org/wiki/File:Steiner_chain_4mer_outside3.svg
[55]: https://en.wikipedia.org/wiki/File:Steiner_chain_4mer_outside2.svg
[56]: https://en.wikipedia.org/wiki/File:Steiner_chain_4mer_outside.svg
[57]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=8
[58]: https://en.wikipedia.org/wiki/File:Rotating_hexlet_equator_opt.gif
[59]: https://en.wikipedia.org/wiki/Dupin_cyclide
[60]: https://en.wikipedia.org/wiki/Torus
[61]: https://en.wikipedia.org/wiki/Fractal
[62]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=9
[63]: https://en.wikipedia.org/wiki/Poncelet_porism
[64]: https://en.wikipedia.org/wiki/Ford_circles
[65]: https://en.wikipedia.org/wiki/Apollonian_gasket
[66]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=10
[67]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=11
[68]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=12
[69]: https://en.wikipedia.org/wiki/C._Stanley_Ogilvy
[70]: https://archive.org/details/excursionsingeom0000ogil/page/51
[71]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[72]: https://en.wikipedia.org/wiki/Special:BookSources/0-486-26530-7
[73]: https://en.wikipedia.org/wiki/Harold_Scott_MacDonald_Coxeter
[74]: https://en.wikipedia.org/wiki/S._L._Greitzer
[75]: https://en.wikipedia.org/wiki/Washington,_D.C.
[76]: https://en.wikipedia.org/wiki/Mathematical_Association_of_America
[77]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-88385-619-2
[78]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[79]: https://zbmath.org/?format=complete&amp;q=an:0166.16402
[80]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-486-46237-0
[81]: https://en.wikipedia.org/wiki/Template:Cite_book
[82]: https://en.wikipedia.org/wiki/Help:CS1_errors#invalid_isbn_date
[83]: https://archive.org/details/penguindictionar0000well/page/244
[84]: https://en.wikipedia.org/wiki/Special:BookSources/0-14-011813-6
[85]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=13
[86]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-205-03226-6
[87]: https://en.wikipedia.org/wiki/Daniel_Pedoe
[88]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-07638-8
[89]: https://en.wikipedia.org/wiki/A_Treatise_on_the_Circle_and_the_Sphere
[90]: /w/index.php?title=Steiner_chain&amp;action=edit&amp;section=14
[91]: https://en.wikipedia.org/wiki/File:Commons-logo.svg
[92]: https://commons.wikimedia.org/wiki/Category:Steiner%20chains
[93]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[94]: https://mathworld.wolfram.com/SteinerChain.html
[95]: https://en.wikipedia.org/wiki/MathWorld
[96]: https://codepen.io/yukulele/pen/OVOEdX/
[97]: https://en.wikipedia.org/wiki/CodePen
[98]: https://www.geogebra.org/m/QrqPQAGX
[99]: http://www.geogebra.org/
[100]: https://en.wikipedia.org/w/index.php?title=Steiner_chain&amp;oldid=1353686089
[101]: /wiki/Help:Category
[102]: /wiki/Category:Circles
[103]: /wiki/Category:Inversive_geometry
[104]: /wiki/Category:Circle_packing
[105]: /wiki/Category:Articles_with_short_description
[106]: /wiki/Category:Short_description_is_different_from_Wikidata
[107]: /wiki/Category:CS1_errors:_ISBN_date
[108]: /wiki/Category:Commons_category_link_is_on_Wikidata
