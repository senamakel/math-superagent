<!-- source: https://franksottile.github.io/research/pages/ERAG/S5/1.html | converted from HTML -->

Enumerative Real Algebraic Geometry: The Conjecture of Shapiro and Shapiro for Grassmannians[image: next] [1][image: up] [2]
**Next:**[5.ii. Rational functions with real critical points][1]
**Up:**[5. The Conjecture of Shapiro and Shapiro: Table of Contents][2]

---

# 5.i. The Conjecture of Shapiro and Shapiro for Grassmannians for Grassmannians

The results of Section [4][3] were inspired by a remarkable conjecture of Boris Shapiro and Michael Shapiro. Let *g*: **R**--> **R***n*be the rational normal curve

*g*(*t*) := (1, *t*, *t*2 /2, ..., *t**n*-1 /(*n*-1)!) =  |  | *t**i*-1*e i*/(*i*-1)! ,  |

the sum from *i*= 1 to *n*. For *t*in **R**, define the flag *F***.**(*t*) by any of the three equivalent ways. The *i*th subspace *F i*(*t*) of the flag is

linear span of *g*(t), *g*'(*t*), ..., *g*(*i*-1) |  | (5.1)

Row space of the *i*by *n*matrix whose (*j*,*l*)-entry is *t**l*-*j*/(*l*-*j*)! |  | (5.2) |

The *i*-plane osculating the rational normal curve *g*at *g*(*t*).  |  | (5.3) |

This makes sense for *t*in **C**and is extended to **P**1 by setting *F i*( infinity ) to be the row space of the last *i*rows of the *n*by *n*identity matrix.

**Conjecture 5.1**(Shapiro-Shapiro) Let *a*1, *a*2, ..., *a s*in *C**n*,*k*be such that |*a*1 |+|*a*2 |+...+|*a s*| = *k*(*n*-*k*). Then, for every distinct *t*1, *t*2, ..., *t s*in **R**, the intersection of the Schubert varieties

*Y**a*1*F***.**(*t*1), *Y**a*2*F***.**(*t*2), ..., *Y a s**F***.**(*t s*),  | (5.4) |

is (a) transverse, and (b) consists only of real points.

Eisenbud's and Harris's dimensional transversality result [[EH][4], Theorem 2.3] guarantees that the intersection ( 5.4) is zero-dimensional. Not only does Conjecture 5.1 state that the classical Schubert calculus is fully real, but it also proposes flags witnessing this full reality. This conjecture has been central to subsequent developments in the real Schubert calculus and it has direct connections to other parts of mathematics, including linear systems theory and linear series on **P**1 (see Remark [5.8][5]). The article [[So7][6]] and the web page [[So4][7]] give a more complete discussion.

One aspect of this conjecture which we relate is the following.

**Theorem 5.2**([[So7][6], Theorem 3.3) For a given *k*and *n*, the general case of Conjecture 5.1 follows from the special case when each Schubert condition is simple, that is, when each *a*=(1,2,...,*k*-1,*k*+1).

Consider these osculating flags *F***.**(*t*) in more detail. If the *i*th row of the matrix ( 5.2) is multiplied by *t i*(which does not affect its row space when *t*is non zero), then the entry in position (*i*,*j*) is *t j*/(*j*-*i*)!, and so we have

*F i*(*t*) = *t*.*F i*(0) ,

where *t*.*F i*(0) is given by the action ( [4.10][8]) of **R**x on **R***n*. The *a*th Plücker coordinate of *F i*(0) is

*p a*(*F i*(0)) =  |  | (*a j*- *a l*)/(*j*- *l*) ,  |

(5.5) |

product over all *l*j*. This Pl&uuml;cker coordinate is non-vanishing. Thus Theorem [4.6][9] has the following corollary.

**Theorem 5.3**([[So5][10], Theorem 1]) There exist *t*1, *t*2, ..., *t**k*(*n*-*k*) in **R**such that there are exactly *d*(*n*,*k*) *k*-planes meeting each (*n*-*k*)-plane *F**n*-*k*(*t i*) non-trivially, and all are real. Equivalently, if *a*=(1,2,...,*k*-1,*k*+1) so that |*a*|=1, then the intersection of the Schubert varieties

*Y a**F***.**(*t*1), *Y a**F***.**(*t*2), ..., *Y a**F***.**(*t*(*n*-*k*),  | (5.6) |

is transverse with all points real.

This establishes a weak form of Conjecture 5.1 for simple Schubert conditions, replacing the quantifier **for all***t i*in **R**by **there exists***t i*in **R**.

If the parameters *t i*in ( 5.6) vary, then the number of real points in that intersection could change, but only if two points first collide (prior to spawning a complex conjugate pair of solutions). This is the reverse of the progression in Dietmaier's algorithm, as displayed in Figure [6][11]. This situation cannot occur if the intersection remains transverse. Together with Theorems 5.2 and 5.3 we deduce the following result.

**Theorem 5.4**([[So5][10], Theorem 6]) Part (a) of Conjecture 5.1 for simple conditions implies part (b) for arbitrary Schubert conditions.

If *t*> 0, then by ( 5.5) the Plücker coordinates of *F i*(*t*) are strictly positive. An upper triangular *n*by *n*-matrix *g*is *totally positive*if every *i*by *i*subdeterminant of *g*is non-negative, and vanishes only if that subdeterminant vanishes on all upper triangular matrices. For example, when *t*> 0 and *i*=*n*, the matrix ( 5.2) is totally positive. Write *G*(*t*) for this matrix. It has the form exp(*th*) where *h*is the principal nilpotent matrix *G*'(*t*). Observe that if *t*1 t*2 t s*, then

*F***.**(*t i*) = *G*(*t i*- *t**i*-1) . *F***.**(*t**i*-1) .

Conjecture 5.1 has a more general version involving totally positive matrices.

**Conjecture 5.5**(Shapiro-Shapiro [[So7][6], Conjecture 4.1]) Let *a*1, *a*2, ..., *a s*in *C**n*,*k*be such that |*a*1 |+|*a*2 |+...+|*a s*| and suppose *g*2, *g*3, ..., *g s*are totally positive matrices. Given any real flag *F***.**, define *F***.***i*recursively for *i*>1 by *F***.***i*:= *g i*.*F***.***i*-1. Then the intersection of Schubert varieties

*Y**a*1*F***.**1, *Y**a*2*F***.**2, ..., *Y a s**F***.***s*,

is transverse with all points real.

There is some experimental evidence for this version of Conjecture 5.1. Subsequent conjectures involving osculating flags have versions involving totally positive matrices. We leave their statements to the reader, they will be explored more fully in [[So11][12]].

---

[image: next] [1][image: up] [2]
**Next:**[5.ii. Rational functions with real critical points][1]
**Up:**[5. The Conjecture of Shapiro and Shapiro: Table of Contents][2]

---


## Links

[1]: 2.html
[2]: index.html
[3]: ../S4/index.html#sec:SchubertCalculus
[4]: ../bibliography.html#EH83
[5]: 2.html#rem:MIC
[6]: ../bibliography.html#So00b
[7]: ../bibliography.html#So_shapiro-www
[8]: ../S4/2.3.html#eq:action
[9]: ../S4/2.3.html#thm:real-trans
[10]: ../bibliography.html#So99a
[11]: ../S3/3.html#fig:Dietmaier
[12]: ../bibliography.html#Sottile_Exp
