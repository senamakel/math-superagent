<!-- source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5535277/ | converted from HTML -->

Arithmetic Progressions on Conics - PMC Skip to main content

**Official websites use .gov**
A **.gov**website belongs to an official government organization in the United States.

**Secure .gov websites use HTTPS**
A **lock**( Lock Locked padlock icon ) or **https://**means you've safely connected to the .gov website. Share sensitive information only on official, secure websites.

[1]

[image: PMC search open icon][image: PMC search close ison]

- [Journal List][2]
- [User Guide][3]

- [image: Open resources icon]
- [image: Download PDF icon] [4]
- [image: Collections icon][image: Collections icon]
- [image: Cite icon]
- [image: Show article permalink icon]

## PERMALINK

[image: Copy icon] Copy

[image: Open article navigation icon]

As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with, the contents by NLM or the National Institutes of Health.
Learn more: [PMC Disclaimer][5] | [PMC Copyright Notice][6]

[image: NIST Author Manuscripts logo]

J Integer Seq

. Author manuscript; available in PMC: 2017 Jul 31.

*Published in final edited form as: *J Integer Seq. 2016 Dec 27;20:17.2.6.

# Arithmetic Progressions on Conics

[Abdoul Aziz Ciss][7]

### Abdoul Aziz Ciss

1 Laboratoire de Traitement de l’Information et Systèmes Intelligents, École Polytechnique de Thiès, BP A10 Thiès, Sénégal

Find articles by [Abdoul Aziz Ciss][7]

1, [Dustin Moody][8]

### Dustin Moody

2 Computer Security Division, National Institute of Standards and Technology (NIST), 100 Bureau Drive, Gaithersburg, MD, 20899-8930

Find articles by [Dustin Moody][8]

2

- Author information
- Article notes
- Copyright and License information

1 Laboratoire de Traitement de l’Information et Systèmes Intelligents, École Polytechnique de Thiès, BP A10 Thiès, Sénégal

2 Computer Security Division, National Institute of Standards and Technology (NIST), 100 Bureau Drive, Gaithersburg, MD, 20899-8930

Issue date 2017.

[PMC Copyright notice][6]

PMCID: PMC5535277 NIHMSID: NIHMS875076 PMID: [28769738][9]

## Abstract

In this paper, we look at long arithmetic progressions on conics. By an arithmetic progression on a curve, we mean the existence of rational points on the curve whose *x*-coordinates are in arithmetic progression. We revisit arithmetic progressions on the unit circle, constructing 3-term progressions of points in the first quadrant containing an arbitrary rational point on the unit circle. We also provide infinite families of three term progressions on the unit hyperbola, as well as conics *ax*2 + *cy*2 = 1 containing arithmetic progressions as long as 8 terms.

**Keywords:**arithemetic progression, conic

## 1 Introduction

Recently, several researchers have explored arithmetic and geometric progressions on various families of plane curves. By a progression on a curve, we mean there is a sequence of rational points on the curve whose *x*-coordinates (or *y*-coordinates) form an arithmetic or geometric progression. The historical motivation for this problem on elliptic curves seems to be an apparent connection between long progressions and high ranks for the corresponding Mordell-Weil groups (see [12, 20] for a lengthier discussion). Perhaps for this reason, much of the work in this area has pertained to elliptic (or hyperelliptic) curves.

Bremner [5], Campbell [8], Garcia-Selfa and Tornero [12], have looked at arithmetic progressions on elliptic curves defined byWeierstrass equations, while Campbell [8], MacLeod [17] and Ulas [21] have investigated progressions on curves represented by quartic models. Alvarado [3] and Ulas [22] extended similar results to genus 2 curves. In addition, Moody [18, 19], Choudhry [9], Bremner [6], and Gonzalez-Jiménez [13] studied longer arithmetic progressions on Edwards and Huff curves.

The problem of finding long arithmetic progressions on conics has not been explored quite as extensively. Alvarado and Goins [4] gave a generalization of 3-term arithmetic progressions on an arbitrary conic section *C*. Allison [1, 2], Bremner [7], and González-Jiménez/Xarles [15] all looked at progressions on parabolas, with infinitely many with 8 term progressions found. More recently, Choudhry and Juyal [10] parameterized infinitely many arithmetic progressions of three rational points on the unit circle, such that the three points all lie in the first quadrant. They also used these progressions to derive infinitely many arithmetic progressions on the ellipse *x*2 /*a*2 + *y*2 /*b*2 = 1.

In this work, we look at finding arithmetic progressions on the unit circle, as well as on the unit hyperbola and conics of the form *ax*2 + *cy*2 = 1. We give a slightly more general result on 3-term arithmetic progressions on the unit circle *x*2 + *y*2 = 1, and similarly on the unit hyperbola *x*2 − *y*2 = 1. We also provide infinitely many conics *C: ax*2 +*cy*2 = 1 having 8-term arithmetic progressions. This matches the highest known length of a progression on conics.

## 2 Arithmetic Progressions on the Unit Circle

Consider the unit circle *x*2 + *y*2 = 1. Trivially, the points (−1, 0), (0, 1), and (1, 0) are always on the circle yielding a progression of length 3. Similarly, given any rational point (*x*, *y*), there is the progression obtained from the points (−*x*, *y*), (0, 1), and (*x*, *y*). However, Choudhry and Juyal sought to find a progression of length 3 whose points were all in the first quadrant. That is, the *x*-coordinates *x i*all satisfied 0 < *x i*< 1. We will work under the same restriction, and present a different approach to finding a 3-term progression.

We begin by parameterizing the rational points on the unit circle by setting

x ( t) = 2 t t 2 + 1, y ( t) = t 2 - 1 t 2 + 1. |

To find a progression of length 3 in the first quadrant, we need to find rational *t*0, *t*1, *t*2 such that 0 < *x*(*t*0), *x*(*t*1), *x*(*t*2) < 1 and *x*(*t*2) − *x*(*t*1) = *x*(*t*1) − *x*(*t*0). An easy calculation shows this will be possible if the following quadratic equation in *t*2 has rational solutions:

( 2 t 0 t 1 2 - 4 t 0 2 t 1 + 2 t 0 - 4 t 1) t 2 2 + 2 ( t 0 2 + 1) ( t 1 2 + 1) t 2 + 2 t 0 t 1 2 - 4 t 0 2 t 1 + 2 t 0 - 4 t 1 = 0. | (1) |

We obtain rational solutions to the quadratic if the resulting discriminant

D = 4 ( t 0 2 - 1) 2 t 1 4 + 64 t 0 ( t 0 2 + 1) t 1 3 - ( 56 t 0 4 + 144 t 0 2 + 56) t 1 2 + 64 t 0 ( t 0 2 + 1) t 1 + 4 ( t 0 2 - 1) |

is square. As the coefficient of t 1 4 is square, we can use a trick from Fermat in [11, p. 639] to make the entire quartic in *t*1 be equal to a square by setting

t 1 = 8 t 0 ( t 0 - 1) 2 ( t 0 + 1) 2 ( t 0 2 + 1) ( 3 t 0 4 + 2 t 0 2 + 3) ( t 0 4 + 6 t 0 2 + 1). |

Substituting in this value of *t*1, the quadratic ( 1) factors, resulting in the roots

t 2 = t 0 3 t 0 8 + 4 t 0 6 - 30 t 0 4 - 28 t 0 2 - 13 13 t 0 8 + 28 t 0 6 + 30 t 0 4 - 4 t 0 2 - 3, |

and it’s inverse. A three term arithmetic progression on the unit circle is thus given by *x*(*t*0), *x*(*t*1), and *x*(*t*2) with the above values of *t*1 and *t*2.

We next find conditions under which the corresponding points will be in the first quadrant. As x ( t) = 2 t t 2 + 1 is always an *x*-coordinate on the unit circle, then clearly 0 < *x*(*t*) < 1 exactly when *t*> 0, *t*≠ 1. We therefore assume that *t*0 > 0. We see that *t*1 > 0 if and only if ( 3 t 0 4 + 2 t 0 2 + 3) ( t 0 4 + 6 t 0 2 + 1) > 0, which is always true. An easy analysis shows that if *t*0 > 1.8 then the expression for *t*2 > 0. Thus, when *t*0 > 1.8, we see that the points with *x*-coordinates *x*(*t*0), *x*(*t*1), and *x*(*t*2) can all be taken to lie in the first quadrant. As an example, when *t*= 2 we obtain the progression 4/5, 3483360/6369961, 9353756/31849805.

An interesting property of the progression above is that given any rational point (*x **, *y **) ≠ (0,±1) on the unit circle, we can find a 3-term progression in the first quadrant containing it. Set *t*0 = (1 ± *y **)/*x **, and then an easy calculation verifies that *x*(*t*0) = *x **. The three term progressions on the unit circle found by Choudhry and Juyal do not have this property. We note the property cannot be extended to two arbitrary rational points on the unit circle. For example, with the points (7/25, 24/25) and (3/5, 4/5) the progression would need to have third term −1/25, 11/25, or 23/25. However none of these values are *x*-coordinates of rational points on the unit circle.

We remark that if we allow circles which are not the unit circle, it is possible to have progressions of length 4, although the points do not all lie in the first quadrant. A simple example is the circle *x*2 +*y*2 = 5/2 which has *x*= −3/2,−1/2, 1/2, 3/2. Any such symmetric progression of length 4 of the form {−3*x*1,−*x*1, *x*1, 3*x*1 } requires finding rational points satisfying

x 1 2 + y 1 2 = R, 9 x 1 2 + y 2 2 = R, |

where the circle has equation *x*2 + *y*2 = *R*. These simultaneous quadratic equations can be transformed into more common models for an elliptic curve. For example, when *R*= 5/2, we parameterize solutions to the first quadratic by setting *x*(*t*) = (−3*t*2 +4*t*+12)/(2*t*2 +8). Substituting this expression into the second quadratic yields the curve *C*:= *z*2 = −71*t*4 + 216*t*3 + 584*t*2 − 864*t*− 1136. The points (*t*, *z*) = (−1, 5) and (2, 8) are on *C*. We then have *x*(−1) = *x*(2) = 1/2, leading to the progression −3/2,−1/2, 1/2, 3/2. It is not hard to find other values of *R*which lead to similar 4-term progressions.

## 3 Progressions on the Unit Hyperbola

It is simple to extend this approach to the unit hyperbola *x*2 − *y*2 = 1. We parameterize the rational points on the hyperbola by setting *x*(*t*) = (*t*2 + 1)/(2*t*). Following the exact same procedure as above, we find that for any rational *t*2 we can set

t 0 = 3 t 2 t 2 2 + 1, t 1 = 2 ( t 2 2 + 1) t 3 t 2. |

The resulting three term progression is *x*(*t*0), *x*(*t*1), and *x*(*t*2):

x ( t 0) = t 2 4 + 11 t 2 2 + 1 6 t 2 ( t 2 2 + 1), x ( t 1) = ( t 2 2 + 4) ( 4 t 2 2 + 1) 12 t 2 ( t 2 2 + 1), x ( t 2) = t 2 2 + 1 2 t 2. |

We attempted to extend these progressions to four terms for both the unit circle, as well as the unit hyperbola. If we let *d*= *x*(*t*2)−*x*(*t*1) be the common difference of a progression, a fourth term would come from either *x*(*t*0) − *d*or *x*(*t*2) + *d*being a valid *x*-coordinate on the corresponding curve. Upon simplfying the resulting equations, they all lead to needing a rational point on certain quartic equations. Transforming these quartics into elliptic curves, we found that none of them have positive rank. Thus, we do not get four term progressions from this approach.

## 4 Arithmetic Progressions on General Conics

The general conic is of the form *ax*2 + *bxy*+ *cy*2 + *dx*+ *ey*+ *f*= 0. We assume the conic is not degenerate, meaning it is not the product of two linear equations. If we were to consider degenerate conics, we would trivially obtain progressions of infinite length as every rational value is a valid *x*-coordinate for a linear equation.

Considering *ax*2 + *bxy*+ *cy*2 + *dx*+ *ey*+ *f*= 0, then we can complete the square (in *y*) to transform the equation into the form

( c y + b 2 x + e 2) 2 = ( b 2 4 - a c) x 2 + ( b e 2 - c d) x + e 2 4 - c f. |

Thus, any arithmetic progression on the general conic will become a progression on a conic of the form *y*2 = *ax*2 + *bx*+ *c*. As mentioned in the introduction, arithmetic progressions on parabolas have been considered by a few authors [1, 2, 7, 15]. Allison found infinitely many parabolas with eight points in arithmetic progression, while González-Jiménez and Xarles were able to show that there does not exist integer arithmetic progressions with nine or more terms on parabolas with both integral coefficients and axis of symmetry. They note without the restrictions requiring integers, an upper bound on the length of progressions on parabolas is not known.

For the remainder of this section, we consider conic sections in standard form, i.e., those for which *b*= 0. We may complete the square, to write the conic equation as

a ( x - d / ( 2 a)) 2 + c ( y - e / ( 2 c)) 2 + f - d 2 / ( 4 a) - e 2 / ( 4 c) = 0. |

An arithmetic progression shifted by *x*−*b*/(2*a*) is still an arithmetic progression, and similarly shifting by *y*− *d*/(2*c*) does not affect the progression. Thus we can rewrite the equation as

a x 2 + c y 2 = 1, |

for some constants *a*, *c*, ∈ ℚ. Note, by multiplying the entire equation by a suitable rational, we can scale so that the constant coefficient is 1. If we wish the progression to be of the form {−2*x*1,−*x*1, 0, *x*1, 2*x*1 }, then we need that *c*is a square and the equation reduces to *ax*2 + *y*2 = 1.

Now given any rational *m*, let *a*= −*m*4 +10*m*2 −9 and x ∗ = 1 4 m. Then a straightforward calculation shows that the points ( ± 2 x ∗, m 2 - 3 2 m), ( ± x ∗, - m 2 + 3 4 m), and (0, 1) all lie on *ax*2 +*y*2 = 1 and hence yield infinitely many 5-term progressions. If 1 < |*m*| < 3, then *a*> 0 and the conic will be a circle, while otherwise *a*< 0 and the conic is a hyperbola. It is also possible to instead fix a value of *a*, which would then require −1/*a*(*m*4 − 10*m*2 + 9) to be square. Such an equation defines an elliptic curve. If the curve has positive rank then the curve will yield an infinite number of progressions for that fixed *a*. For example, if *a*= 15/64 then the quartic is isomorphic to the curve *Y*2 = *X*3 − 63897600*X*− 146800640000, which is a rank 1 curve with generator (−4864, 221184).

We can further improve the results for *ax*2 + *cy*2 = 1, and obtain progressions of length greater than five. Set

a = t ( t + 1) ( t - 2) t ( t - 1) ( 2 t - 1) ( t + 4) ( t + 2), c = 2 ( t - 1) ( 2 t - 1) ( t + 4) ( t + 2), |

for any *t*= 1/2, 1, 2,−1,−2,−4. Then the rational points (±1,±(*t*2 +2*t*−*t*)), (±3,±(*t*2 +2)), and (±5,±(*t*2 − 4*t*− 2)) all satisfy *ax*2 + *y*2 = 1. Thus, there are infinitely many conics of this form with 6 terms in progression. In order for there to be a point with *x*-coordinate ±7, then there needs to be a rational solution to the equation

s 2 = t 4 - 20 t 3 + 24 t 2 + 40 t + 4. |

The curve defined is birationally equivalent to the elliptic curve *E: Y*2 = *X*3 −1008*X*+10368. The curve *E*is a rank 1 curve with generator (−12,−144), and hence has infinitely many rational points. Given any such point (*X*, *Y*), we set *t*= (40*X*−480+4*Y*)/(*X*2 −16*X*+48). For these values of *t*, then *x*= ±7 is a valid *x*-coordinate, showing we have an infinite number of conics with 8 points in progression. As a concrete example, the point (28, 64) is on *E*, and leads to *t*= 7/3. When *t*= 7/3, the conic (105/5434)*x*2 + (81/5434)*y*2 = 1 has eight points in progression with *x*-coordinates {−7,−5,−3,−1, 1, 3, 5, 7}.

## 5 Conclusion and Future Work

In this work, we have studied long arithmetic progression on conics. We gave a more general result on finding progressions on the unit circle, and similarly provided infinitely many unit hyperbolas with 3-term arithmetic progressions. We also constructed infinitely many conics in standard form having 8-term arithmetic progressions. Future work would be to improve the length of these progressions. It might also be possible to use the techniques of [14] to prove upper bounds on the maximum length of (integer) progressions on the unit circle, hyperbola, or conics in standard form. It would be interesting to study long geometric progressions on conics as well.

## Acknowledgments

We would like to thank the anonymous reviewer for their valuable comments and suggestions, and in particular for pointing us to some of the previous results in the literature which we were not aware of.

## Contributor Information

Abdoul Aziz Ciss, Laboratoire de Traitement de l’Information et Systèmes Intelligents, École Polytechnique de Thiès, BP A10 Thiès, Sénégal.

Dustin Moody, Computer Security Division, National Institute of Standards and Technology (NIST), 100 Bureau Drive, Gaithersburg, MD, 20899-8930.

## References

- 1. Allison D. On certain simultaneous Diophantine equations. Math Colloq Univ Cape Town. 1977;11:117–133. [[Google Scholar][10]]
- 2. Allison D. On square values of quadratics. Math Proc Cambridge Philos Soc. 1986;99:381–383. [[Google Scholar][11]]
- 3. Alvarado A. An arithmetic progression on quintic curves. J Integer Seq. 2009;12 Article 09.7.3. [[Google Scholar][12]]
- 4. Alvarado A, Goins EH. Arithmetic progressions on conic sections. Int J Number Theory. 2013;9:1379–1393. [[Google Scholar][13]]
- 5. Bremner A. On arithmetic progressions on elliptic curves. Experiment Math. 1999;8:409–413. [[Google Scholar][14]]
- 6. Bremner A. Arithmetic progressions on Edwards curves. J Integer Seq. 2013;16 Article 13.8.5. [[Google Scholar][15]]
- 7. Bremner A. On square values of quadratics. Acta Arith. 2003;108:95–111. [[Google Scholar][16]]
- 8. Campbell G. A note on arithmetic progressions on elliptic curves. J Integer Seq. 2003;6 Article 03.1.3. [[Google Scholar][17]]
- 9. Choudhry A. Arithmetic progressions on Huff curves. J Integer Seq. 2015;18 Article 15.5.2. [[PMC free article][18]] [[PubMed][9]] [[Google Scholar][19]]
- 10. Choudhry A, Juyal A. Rational points in arithmetic progression on the unit circle. J Integer Seq. 2016;19 Article 16.4.1. [[Google Scholar][20]]
- 11. Dickson LE. History of the Theory of Numbers. Vol. 2. Chelsea Publishing Co; 1920. [[Google Scholar][21]]
- 12. Garcia-Selfa I, Tornero J. Searching for simultaneous arithmetic progressions on elliptic curves. Bull Austral Math Soc. 2005;71:417–424. [[Google Scholar][22]]
- 13. González-Jiménez E. On arithmetic progressions on Edwards curves. Acta Arith. 2015;167:117–132. [[Google Scholar][23]]
- 14. González-Jiménez E. Covering techniques and rational points on some genus 5 curves. Contemp Math. 2015;649:89–105. [[Google Scholar][24]]
- 15. González-Jiméz E, Xarles X. On symmetric square values of quadratic polynomials. Acta Arith. 2011;149:145–159. [[Google Scholar][25]]
- 16. Huff GB. Diophantine problems in geometry and elliptic ternary forms. Duke Math J. 1948;15:443–453. [[Google Scholar][26]]
- 17. MacLeod A. 14-term arithmetic progressions on quartic elliptic curves. J Integer Seq. 2006;9(9) Article 06.1.2. [[Google Scholar][27]]
- 18. Moody D. Arithmetic progressions on Edwards curves. J Integer Seq. 2011;38 Article 11.1.7. [[PMC free article][18]] [[PubMed][9]] [[Google Scholar][28]]
- 19. Moody D. Arithmetic progressions on Huff curves. Ann Math Inform. 2011;38:111–116. [[Google Scholar][29]]
- 20. Moody D, Zargar AS. On the Rank of Elliptic Curves with Long Arithmetic Progressions, to appear in. Coloql Math. 2016 [[Google Scholar][30]]
- 21. Ulas M. A note on arithmetic progressions on quartic elliptic curves. J Integer Seq. 2005;8 Article 05.3.1. [[Google Scholar][31]]
- 22. Ulas M. On arithmetic progressions on genus two curves. Rocky Mountain J Math. 2009;39:971–980. [[Google Scholar][32]]

[image: Close]

## ACTIONS

- [image: Download PDF icon] [PDF (375.4 KB)][4]
- [image: Cite icon] Cite
- [image: Collections icon][image: Collections icon] Collections
- [image: Permalink icon] Permalink

## PERMALINK

[image: Copy icon] Copy

## RESOURCES

### Similar articles

### Cited by other articles

### Links to NCBI Databases

## Cite

[image: Close icon]

- [image: Copy icon] Copy
- [image: Download icon] Download .nbib.nbib
-

Format: AMA APA MLA NLM

## Add to Collections

Back to Top[image: back to top icon]


## Links

[1]: /
[2]: /journals/
[3]: /about/userguide/
[4]: pdf/nihms875076.pdf
[5]: /about/disclaimer/
[6]: /about/copyright/
[7]: https://pubmed.ncbi.nlm.nih.gov/?term="Ciss%20AA"[Author]
[8]: https://pubmed.ncbi.nlm.nih.gov/?term="Moody%20D"[Author]
[9]: https://pubmed.ncbi.nlm.nih.gov/28769738/
[10]: https://scholar.google.com/scholar_lookup?journal=Math%20Colloq%20Univ%20Cape%20Town&amp;title=On%20certain%20simultaneous%20Diophantine%20equations&amp;author=D%20Allison&amp;volume=11&amp;publication_year=1977&amp;pages=117-133&amp;
[11]: https://scholar.google.com/scholar_lookup?journal=Math%20Proc%20Cambridge%20Philos%20Soc&amp;title=On%20square%20values%20of%20quadratics&amp;author=D%20Allison&amp;volume=99&amp;publication_year=1986&amp;pages=381-383&amp;
[12]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=An%20arithmetic%20progression%20on%20quintic%20curves&amp;author=A%20Alvarado&amp;volume=12&amp;publication_year=2009&amp;
[13]: https://scholar.google.com/scholar_lookup?journal=Int%20J%20Number%20Theory&amp;title=Arithmetic%20progressions%20on%20conic%20sections&amp;author=A%20Alvarado&amp;author=EH%20Goins&amp;volume=9&amp;publication_year=2013&amp;pages=1379-1393&amp;
[14]: https://scholar.google.com/scholar_lookup?journal=Experiment%20Math&amp;title=On%20arithmetic%20progressions%20on%20elliptic%20curves&amp;author=A%20Bremner&amp;volume=8&amp;publication_year=1999&amp;pages=409-413&amp;
[15]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=Arithmetic%20progressions%20on%20Edwards%20curves&amp;author=A%20Bremner&amp;volume=16&amp;publication_year=2013&amp;
[16]: https://scholar.google.com/scholar_lookup?journal=Acta%20Arith&amp;title=On%20square%20values%20of%20quadratics&amp;author=A%20Bremner&amp;volume=108&amp;publication_year=2003&amp;pages=95-111&amp;
[17]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=A%20note%20on%20arithmetic%20progressions%20on%20elliptic%20curves&amp;author=G%20Campbell&amp;volume=6&amp;publication_year=2003&amp;
[18]: /articles/PMC5535277/
[19]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=Arithmetic%20progressions%20on%20Huff%20curves&amp;author=A%20Choudhry&amp;volume=18&amp;publication_year=2015&amp;pmid=28769738&amp;
[20]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=Rational%20points%20in%20arithmetic%20progression%20on%20the%20unit%20circle&amp;author=A%20Choudhry&amp;author=A%20Juyal&amp;volume=19&amp;publication_year=2016&amp;
[21]: https://scholar.google.com/scholar_lookup?title=History%20of%20the%20Theory%20of%20Numbers&amp;author=LE%20Dickson&amp;publication_year=1920&amp;
[22]: https://scholar.google.com/scholar_lookup?journal=Bull%20Austral%20Math%20Soc&amp;title=Searching%20for%20simultaneous%20arithmetic%20progressions%20on%20elliptic%20curves&amp;author=I%20Garcia-Selfa&amp;author=J%20Tornero&amp;volume=71&amp;publication_year=2005&amp;pages=417-424&amp;
[23]: https://scholar.google.com/scholar_lookup?journal=Acta%20Arith&amp;title=On%20arithmetic%20progressions%20on%20Edwards%20curves&amp;author=E%20Gonz%C3%A1lez-Jim%C3%A9nez&amp;volume=167&amp;publication_year=2015&amp;pages=117-132&amp;
[24]: https://scholar.google.com/scholar_lookup?journal=Contemp%20Math&amp;title=Covering%20techniques%20and%20rational%20points%20on%20some%20genus%205%20curves&amp;author=E%20Gonz%C3%A1lez-Jim%C3%A9nez&amp;volume=649&amp;publication_year=2015&amp;pages=89-105&amp;
[25]: https://scholar.google.com/scholar_lookup?journal=Acta%20Arith&amp;title=On%20symmetric%20square%20values%20of%20quadratic%20polynomials&amp;author=E%20Gonz%C3%A1lez-Jim%C3%A9z&amp;author=X%20Xarles&amp;volume=149&amp;publication_year=2011&amp;pages=145-159&amp;
[26]: https://scholar.google.com/scholar_lookup?journal=Duke%20Math%20J&amp;title=Diophantine%20problems%20in%20geometry%20and%20elliptic%20ternary%20forms&amp;author=GB%20Huff&amp;volume=15&amp;publication_year=1948&amp;pages=443-453&amp;
[27]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=14-term%20arithmetic%20progressions%20on%20quartic%20elliptic%20curves&amp;author=A%20MacLeod&amp;volume=9&amp;issue=9&amp;publication_year=2006&amp;
[28]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=Arithmetic%20progressions%20on%20Edwards%20curves&amp;author=D%20Moody&amp;volume=38&amp;publication_year=2011&amp;pmid=28769738&amp;
[29]: https://scholar.google.com/scholar_lookup?journal=Ann%20Math%20Inform&amp;title=Arithmetic%20progressions%20on%20Huff%20curves&amp;author=D%20Moody&amp;volume=38&amp;publication_year=2011&amp;pages=111-116&amp;
[30]: https://scholar.google.com/scholar_lookup?journal=Coloql%20Math&amp;title=On%20the%20Rank%20of%20Elliptic%20Curves%20with%20Long%20Arithmetic%20Progressions,%20to%20appear%20in&amp;author=D%20Moody&amp;author=AS%20Zargar&amp;publication_year=2016&amp;
[31]: https://scholar.google.com/scholar_lookup?journal=J%20Integer%20Seq&amp;title=A%20note%20on%20arithmetic%20progressions%20on%20quartic%20elliptic%20curves&amp;author=M%20Ulas&amp;volume=8&amp;publication_year=2005&amp;
[32]: https://scholar.google.com/scholar_lookup?journal=Rocky%20Mountain%20J%20Math&amp;title=On%20arithmetic%20progressions%20on%20genus%20two%20curves&amp;author=M%20Ulas&amp;volume=39&amp;publication_year=2009&amp;pages=971-980&amp;
