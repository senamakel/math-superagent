<!-- source: https://arxiv.org/html/1602.05862v1 | converted from HTML -->

On sequences of consecutive squares on elliptic curves

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1602.05862v1 [math.NT] 18 Feb 2016

# On sequences of consecutive squares on elliptic curves

Mohamed Kamel Address: Department of Mathematics, Faculty of Science, Cairo University, Giza, Egypt Email address: [mohgamal@sci.cu.edu.eg][3] and Mohammad Sadek Address: American University in Cairo, Mathematics and Actuarial Science Department, AUC Avenue, New Cairo, Egypt Email address: [mmsadek@aucegypt.edu][4]

###### Abstract.

Let C C be an elliptic curve defined over ℚ {\mathbb{Q}} by the equation y 2 = x 3 + A ​ x + B y^{2}=x^{3}+Ax+B where A, B ∈ ℚ A,B\in{\mathbb{Q}}. A sequence of rational points ( x i, y i) ∈ C ( ℚ), i = 1, 2, …, (x_{i},y_{i})\in C({\mathbb{Q}}),\,i=1,2,\ldots, is said to form a sequence of consecutive squares on C C if the sequence of x x -coordinates, x i, i = 1, 2, … x_{i},i=1,2,\ldots, consists of consecutive squares. We produce an infinite family of elliptic curves C C with a 5 5 -term sequence of consecutive squares. Furthermore, this sequence consists of five independent rational points in C ⁡ ( ℚ) C({\mathbb{Q}}). In particular, the rank r r of C ⁡ ( ℚ) C({\mathbb{Q}}) satisfies r ≥ 5 r\geq 5.

## 1. Introduction

In [5], Bremner initiated the discussion of certain arithmetic questions on rational points of elliptic curves attempting to relate the group structure on an elliptic curve E E to the addition group operation on the rational line. He raised the question of the existence of a sequence of rational points in E ⁡ ( ℚ) E({\mathbb{Q}}) whose x x -coordinates form an arithmetic progression in ℚ {\mathbb{Q}}. Such sequence is called an arithmetic progression sequence in E ⁡ ( ℚ) E({\mathbb{Q}}). A variety of questions may be posed. For instance, how long these sequences can be and how many elliptic curves would have such long sequences of rational points. The existence of infinitely many elliptic curves with length 8 arithmetic progressions was proved. Several authors introduced different approaches to find infinitely many elliptic curves with longer arithmetic progression sequences, see [2, 7, 9, 12].

In [6], the study of sequences of rational points on elliptic curves whose x x -coordinates form a geometric progression in ℚ {\mathbb{Q}} was initiated. An infinite family of elliptic curves having geometric progression sequences of length 4 was exhibited. It was remarked that infinitely many elliptic curves with 5 5 -term geometric progression sequences can be constructed.

In this note, we discuss sequences of rational points on elliptic curves whose x x -coordinates form a sequence of consecutive squares. We consider elliptic curves defined by the equation y 2 = a ​ x 3 + b ​ x + c y^{2}=ax^{3}+bx+c over ℚ {\mathbb{Q}}. We show that elliptic curves defined by the latter equation with 5-term sequences of rational points whose x x -coordinates are elements in a sequence of consecutive squares in ℚ {\mathbb{Q}} are parametrized by an elliptic surface whose rank is positive. Hence, one deduces the existence of infinitely many such elliptic curves. Moreover, we show that the five rational points forming the sequence are linearly independent in the group of rational points of the elliptic curve they lie on. In particular, we introduce an infinite family of elliptic curves of rank ≥ 5 \geq 5.

## 2. Sequences of Consecutive Squares

###### Definition 2.1.

Let C C be an elliptic curve defined over a number field K K by the Weierstrass equation y 2 + a 1 ​ x ​ y + a 3 ​ y = x 3 + a 2 ​ x 2 + a 4 ​ x + a 6, a i ∈ K y^{2}+a_{1}xy+a_{3}y=x^{3}+a_{2}x^{2}+a_{4}x+a_{6},\,a_{i}\in K. The sequence ( x i, y i) ∈ C ⁡ ( K) (x_{i},y_{i})\in C(K) is said to be a sequence of consecutive squares on C C if there is a u ∈ K u\in K such that x i = ( u + i) 2 x_{i}=(u+i)^{2}, i = 1, 2, … i=1,2,\ldots.

The following proposition ensures the finiteness of the sequence of consecutive squares on an elliptic curve.

###### Proposition 2.2.

Let C C be an elliptic curve defined over a number field K K by a Weierstrass equation of the form

 | y 2 + a 1 ​ x ​ y + a 3 ​ y = x 3 + a 2 ​ x 2 + a 4 ​ x + a 6, a i ∈ K. y^{2}+a_{1}xy+a_{3}y=x^{3}+a_{2}x^{2}+a_{4}x+a_{6},\,a_{i}\in K. |  |

Let ( x i, y i) ∈ C ⁡ ( K) (x_{i},y_{i})\in C(K) be a sequence of consecutive squares on C C. Then the sequence ( x i, y i) (x_{i},y_{i}) is finite.

Proof: We can assume without loss of generality that x i = ( u + i) 2 x_{i}=(u+i)^{2}, i = 1, 2, … i=1,2,\ldots, u ∈ K u\in K. This sequence gives rise to a sequence of rational points on the genus 2 2 hyperelliptic curve

 | 𝒞: y 2 + a 1 ​ x 2 ​ y + a 3 ​ y = x 6 + a 2 ​ x 4 + a 4 ​ x 2 + a 6. \operatorname{\mathcal{C}}:y^{2}+a_{1}x^{2}y+a_{3}y=x^{6}+a_{2}x^{4}+a_{4}x^{2}+a_{6}. |  |

Namely, the points ( u + i, y) ∈ 𝒞 ⁡ ( K) (u+i,y)\in\operatorname{\mathcal{C}}(K). According to Faltings’ Theorem, [8], one knows that 𝒞 ⁡ ( K) \operatorname{\mathcal{C}}(K) is finite, hence the sequence is finite. □ \Box

Based on the above proposition, one may present the following definition.

###### Definition 2.3.

Let C C be an elliptic curve over ℚ {\mathbb{Q}} defined by a Weierstrass equation. Let ( x i, y i) ∈ C ( ℚ), i = 1, 2, …, n, (x_{i},y_{i})\in C({\mathbb{Q}}),\,i=1,2,\ldots,n, be a sequence of consecutive squares on C C. Then n n is said to be the length of the sequence.

## 3. Constructing elliptic curves with long sequences of consecutive squares

In this note, we focus our attention on the family of elliptic curves given by the affine equation C: y 2 = a ​ x 3 + b ​ x + c C:y^{2}=ax^{3}+bx+c over ℚ {\mathbb{Q}}. We will show that there are infinitely many elliptic curves defined by the latter equation containing 5-term sequences of consecutive squares.

One observes that if ( t 2, d), ( ( t + 1) 2, e) (t^{2},d),((t+1)^{2},e), and ( ( t + 2) 2, f) ((t+2)^{2},f) lie in C ⁡ ( ℚ) C({\mathbb{Q}}), where t ∈ ℚ t\in{\mathbb{Q}}, then these rational points form a 3-term sequence of consecutive squares. Indeed, one has

 | d 2 \displaystyle d^{2} | = \displaystyle= | a ​ t 6 + b ​ t 2 + c \displaystyle at^{6}+bt^{2}+c |  |

 | e 2 \displaystyle e^{2} | = \displaystyle= | a ​ ( t + 1) 6 + b ​ ( t + 1) 2 + c \displaystyle a(t+1)^{6}+b(t+1)^{2}+c |  |

 | f 2 \displaystyle f^{2} | = \displaystyle= | a ​ ( t + 2) 6 + b ​ ( t + 2) 2 + c. \displaystyle a(t+2)^{6}+b(t+2)^{2}+c. |  |

It is a standard linear algebra exercise to show that

 | a \displaystyle a | = \displaystyle= | ( 3 + 2 ​ t) ​ d 2 − 4 ​ ( 1 + t) ​ e 2 + ( 1 + 2 ​ t) ​ f 2 4 ​ ( 15 + 73 ​ t + 135 ​ t 2 + 125 ​ t 3 + 60 ​ t 4 + 12 ​ t 5) \displaystyle\frac{(3+2t)d^{2}-4(1+t)e^{2}+(1+2t)f^{2}}{4(15+73t+135t^{2}+125t^{3}+60t^{4}+12t^{5})} |  |

 | b \displaystyle b | = \displaystyle= | ( 3 + 2 ​ t) ​ ( 3 + 3 ​ t + t 2) ​ ( 7 + 9 ​ t + 3 ​ t 2) ​ d 2 + ( 1 + t) ​ ( − 4 ​ ( 4 + 2 ​ t + t 2) ​ ( 4 + 6 ​ t + 3 ​ t 2) ​ e 2) 4 ​ ( 1 + 2 ​ t) ​ ( 15 + 43 ​ t + 49 ​ t 2 + 27 ​ t 3 + 6 ​ t 4) \displaystyle\frac{(3+2t)(3+3t+t^{2})(7+9t+3t^{2})d^{2}+(1+t)(-4(4+2t+t^{2})(4+6t+3t^{2})e^{2})}{4(1+2t)(15+43t+49t^{2}+27t^{3}+6t^{4})} |  |

 |  | + \displaystyle+ | ( 1 + t) ​ ( 4 + 2 ​ t + t 2) ​ ( 4 + 6 ​ t + 3 ​ t 2) ​ f 2 4 ​ ( 1 + 2 ​ t) ​ ( 15 + 43 ​ t + 49 ​ t 2 + 27 ​ t 3 + 6 ​ t 4) \displaystyle\frac{(1+t)(4+2t+t^{2})(4+6t+3t^{2})f^{2}}{4(1+2t)(15+43t+49t^{2}+27t^{3}+6t^{4})} |  |

 | c \displaystyle c | = \displaystyle= | ( 2 + t) 2 ​ ( 15 + 43 ​ t + 46 ​ t 2 + 22 ​ t 3 + 4 ​ t 4) ​ d 2 − 8 ​ t 2 ​ ( 2 + t) 2 ​ ( 2 + 2 ​ t + t 2) ​ e 2 + t 2 ​ ( 1 + 5 ​ t + 10 ​ t 2 + 10 ​ t 3 + 4 ​ t 4) ​ f 2 4 ​ ( 1 + 2 ​ t) ​ ( 15 + 28 ​ t + 21 ​ t 2 + 6 ​ t 3). \displaystyle\frac{(2+t)^{2}(15+43t+46t^{2}+22t^{3}+4t^{4})d^{2}-8t^{2}(2+t)^{2}(2+2t+t^{2})e^{2}+t^{2}(1+5t+10t^{2}+10t^{3}+4t^{4})f^{2}}{4(1+2t)(15+28t+21t^{2}+6t^{3})}. |  |

In particular, one has the following result.

###### Remark 3.1.

The above argument indicates that given d, e, f ∈ ℚ ⁡ ( t) d,e,f\in{\mathbb{Q}}(t), there exist a, b, c ∈ ℚ ⁡ ( t) a,b,c\in{\mathbb{Q}}(t) such that the ordered pairs ( t 2, d), ( ( t + 1) 2, e) (t^{2},d),((t+1)^{2},e) and ( ( t + 2) 2, f) ((t+2)^{2},f) are three rational points on the elliptic surface y 2 = a ​ x 3 + b ​ x + c y^{2}=ax^{3}+bx+c.

Now, if ( ( t + 3) 2, g) ∈ C ⁡ ( ℚ) ((t+3)^{2},g)\in C({\mathbb{Q}}), then one has a 4-term sequence of consecutive squares on C C. In fact, using the above values for a, b, c a,b,c, one then sees that

 | g 2 = ( 5 + 2 ​ t) ​ ( ( 2 + t) ​ ( 14 + 12 ​ t + 3 ​ t 2) ​ d 2 − 3 ​ ( 1 + t) ​ ( 13 + 10 ​ t + 3 ​ t 2) ​ e 2) + 3 ​ ( 2 + t) ​ ( 1 + 2 ​ t) ​ ( 10 + 8 ​ t + 3 ​ t 2) ​ f 2 ( 1 + t) ​ ( 1 + 2 ​ t) ​ ( 5 + 6 ​ t + 3 ​ t 2). \displaystyle g^{2}=\frac{(5+2t)((2+t)(14+12t+3t^{2})d^{2}-3(1+t)(13+10t+3t^{2})e^{2})+3(2+t)(1+2t)(10+8t+3t^{2})f^{2}}{(1+t)(1+2t)(5+6t+3t^{2})}. |  |

Therefore, in view of Remark 3.1, one needs to find the elements d, e, f d,e,f and g g in ℚ ⁡ ( t) {\mathbb{Q}}(t) satisfying the latter equation in order to construct an elliptic curve C C with a 4-term sequence of consecutive squares. In fact, since ( d, e, f, g) = ( 1, 1, 1, 1) (d,e,f,g)=(1,1,1,1) is a solution for equation ( 3), the general solution ( d, e, f, g) (d,e,f,g) is given by the following parametrization:

 | d \displaystyle d | = \displaystyle= | ( 2 + t) ​ ( 5 + 2 ​ t) ​ ( 14 + 12 ​ t + 3 ​ t 2) ​ p 2 + 3 ​ ( 1 + t) ​ ( 5 + 2 ​ t) ​ ( 13 + 10 ​ t + 3 ​ t 2) ​ q 2 − 3 ​ ( 2 + t) ​ ( 1 + 2 ​ t) ​ ( 10 + 8 ​ t + 3 ​ t 2) ​ w 2 \displaystyle(2+t)(5+2t)(14+12t+3t^{2})p^{2}+3(1+t)(5+2t)(13+10t+3t^{2})q^{2}-3(2+t)(1+2t)(10+8t+3t^{2})w^{2} |  |

 |  | − \displaystyle- | 6 ​ ( 65 + 141 ​ t + 111 ​ t 2 + 41 ​ t 3 + 6 ​ t 4) ​ p ​ q + 6 ​ ( 20 + 66 ​ t + 66 ​ t 2 + 31 ​ t 3 + 6 ​ t 4) ​ p ​ w, \displaystyle 6(65+141t+111t^{2}+41t^{3}+6t^{4})pq+6(20+66t+66t^{2}+31t^{3}+6t^{4})pw, |  |

 | e \displaystyle e | = \displaystyle= | − ( 2 + t) ​ ( 5 + 2 ​ t) ​ ( 14 + 12 ​ t + 3 ​ t 2) ​ p 2 − 3 ​ ( 1 + t) ​ ( 5 + 2 ​ t) ​ ( 13 + 10 ​ t + 3 ​ t 2) ​ q 2 − 3 ​ ( 2 + t) ​ ( 1 + 2 ​ t) ​ ( 10 + 8 ​ t + 3 ​ t 2) ​ w 2 \displaystyle-(2+t)(5+2t)(14+12t+3t^{2})p^{2}-3(1+t)(5+2t)(13+10t+3t^{2})q^{2}-3(2+t)(1+2t)(10+8t+3t^{2})w^{2} |  |

 |  | + \displaystyle+ | 2 ​ ( 140 + 246 ​ t + 166 ​ t 2 + 51 ​ t 3 + 6 ​ t 4) ​ p ​ q + 6 ​ ( 20 + 66 ​ t + 66 ​ t 2 + 31 ​ t 3 + 6 ​ t 4) ​ q ​ w, \displaystyle 2(140+246t+166t^{2}+51t^{3}+6t^{4})pq+6(20+66t+66t^{2}+31t^{3}+6t^{4})qw, |  |

 | f \displaystyle f | = \displaystyle= | − ( 2 + t) ​ ( 5 + 2 ​ t) ​ ( 14 + 12 ​ t + 3 ​ t 2) ​ p 2 + 3 ​ ( 1 + t) ​ ( 5 + 2 ​ t) ​ ( 13 + 10 ​ t + 3 ​ t 2) ​ q 2 + 3 ​ ( 2 + t) ​ ( 1 + 2 ​ t) ​ ( 10 + 8 ​ t + 3 ​ t 2) ​ w 2 \displaystyle-(2+t)(5+2t)(14+12t+3t^{2})p^{2}+3(1+t)(5+2t)(13+10t+3t^{2})q^{2}+3(2+t)(1+2t)(10+8t+3t^{2})w^{2} |  |

 |  | − \displaystyle- | 6 ​ ( 1 + t) ​ ( 5 + 2 ​ t) ​ ( 13 + 10 ​ t + 3 ​ t 2) ​ q ​ w + 2 ​ ( 2 + t) ​ ( 5 + 2 ​ t) ​ ( 14 + 12 ​ t + 3 ​ t 2) ​ p ​ w, \displaystyle 6(1+t)(5+2t)(13+10t+3t^{2})qw+2(2+t)(5+2t)(14+12t+3t^{2})pw, |  |

 | g \displaystyle g | = \displaystyle= | − p 2 ​ ( 140 + 246 ​ t + 166 ​ t 2 + 51 ​ t 3 + 6 ​ t 4) + 3 ​ ( q 2 ​ ( 65 + 141 ​ t + 111 ​ t 2 + 41 ​ t 3 + 6 ​ t 4) CLOSE \displaystyle-p^{2}(140+246t+166t^{2}+51t^{3}+6t^{4})+3(q^{2}(65+141t+111t^{2}+41t^{3}+6t^{4}) |  |

 |  | − \displaystyle- | OPEN ( 20 + 66 ​ t + 66 ​ t 2 + 31 ​ t 3 + 6 ​ t 4) ​ w 2). \displaystyle(20+66t+66t^{2}+31t^{3}+6t^{4})w^{2}). |  |

Consult [10, §7] for finding parametric rational solutions of a homogeneous polynomial of degree 2 2 in several variables.

###### Remark 3.2.

The points ( t 2, d), ( ( t + 1) 2, e), ( ( t + 2) 2, f), ( ( t + 3) 2, g) (t^{2},d),((t+1)^{2},e),((t+2)^{2},f),((t+3)^{2},g), where d, e, f, g ∈ ℚ ⁡ ( t, p, q, w) d,e,f,g\in{\mathbb{Q}}(t,p,q,w) are given as above, are rational points on the elliptic surface y 2 = a ​ x 3 + b ​ x + c y^{2}=ax^{3}+bx+c, where a, b, c a,b,c are defined in ( 3).

Now, we assume that ( ( t + 4) 2, h) ((t+4)^{2},h) is a rational point on the elliptic curve y 2 = a ​ x 3 + b ​ x + c y^{2}=ax^{3}+bx+c. In particular, there exists a 5 5 -term sequence of consecutive squares on the latter curve. Then one has

(4) |  | h 2 = A ​ p 4 + B ​ p 3 + C ​ p 2 + D ​ p + E \displaystyle h^{2}=Ap^{4}+Bp^{3}+Cp^{2}+Dp+E |  |

with

 | A \displaystyle A | = \displaystyle= | ( 140 + 246 ​ t + 166 ​ t 2 + 51 ​ t 3 + 6 ​ t 4) 2 \displaystyle(140+246t+166t^{2}+51t^{3}+6t^{4})^{2} |  |

 | B \displaystyle B | = \displaystyle= | 4 ​ ( 5 + 2 ​ t) 2 ​ ( 196 + 322 ​ t + 202 ​ t 2 + 57 ​ t 3 + 6 ​ t 4) ​ ( ( 87 + 83 ​ t + 27 ​ t 2 + 3 ​ t 3) ​ q − 3 ​ ( 52 + 58 ​ t + 22 ​ t 2 + 3 ​ t 3) ​ w) 3 + 2 ​ t \displaystyle\frac{4(5+2t)^{2}(196+322t+202t^{2}+57t^{3}+6t^{4})((87+83t+27t^{2}+3t^{3})q-3(52+58t+22t^{2}+3t^{3})w)}{3+2t} |  |

 | C \displaystyle C | = \displaystyle= | 2 ​ ( 5 + 2 ​ t) 3 + 2 ​ t ​ ( 5 ​ ( 78330 + 250402 ​ t + 346118 ​ t 2 + 271991 ​ t 3 + 132943 ​ t 4 + 41217 ​ t 5 + 7851 ​ t 6 + 828 ​ t 7 CLOSE CLOSE \displaystyle\frac{2(5+2t)}{3+2t}(5(78330+250402t+346118t^{2}+271991t^{3}+132943t^{4}+41217t^{5}+7851t^{6}+828t^{7} |  |

 |  | + \displaystyle+ | OPEN 36 ​ t 8) ​ q 2 − 12 ​ ( 41580 + 154358 ​ t + 243358 ​ t 2 + 217563 ​ t 3 + 121708 ​ t 4 + 43727 ​ t 5 + 9852 ​ t 6 + 1272 ​ t 7 CLOSE \displaystyle 36t^{8})q^{2}-12(41580+154358t+243358t^{2}+217563t^{3}+121708t^{4}+43727t^{5}+9852t^{6}+1272t^{7} |  |

 |  | + \displaystyle+ | OPEN OPEN 72 ​ t 8) ​ q ​ w + 15 ​ ( 2 + t) 2 ​ ( − 2828 − 2552 ​ t + 784 ​ t 2 + 2364 ​ t 3 + 1395 ​ t 4 + 360 ​ t 5 + 36 ​ t 6) ​ w 2) \displaystyle 72t^{8})qw+15(2+t)^{2}(-2828-2552t+784t^{2}+2364t^{3}+1395t^{4}+360t^{5}+36t^{6})w^{2}) |  |

 | D \displaystyle D | = \displaystyle= | 12 ​ ( 35 + 24 ​ t + 4 ​ t 2) 3 + 2 ​ t ​ ( ( 5655 + 17662 ​ t + 23115 ​ t 2 + 16782 ​ t 3 + 7345 ​ t 4 + 1938 ​ t 5 + 285 ​ t 6 + 18 ​ t 7) ​ q 3 CLOSE \displaystyle\frac{12(35+24t+4t^{2})}{3+2t}((5655+17662t+23115t^{2}+16782t^{3}+7345t^{4}+1938t^{5}+285t^{6}+18t^{7})q^{3} |  |

 |  | + \displaystyle+ | ( 6660 + 18502 ​ t + 22620 ​ t 2 + 15567 ​ t 3 + 6515 ​ t 4 + 1683 ​ t 5 + 255 ​ t 6 + 18 ​ t 7) ​ q 2 ​ w − 5 ​ ( 3708 + 11842 ​ t CLOSE \displaystyle(6660+18502t+22620t^{2}+15567t^{3}+6515t^{4}+1683t^{5}+255t^{6}+18t^{7})q^{2}w-5(3708+11842t |  |

 |  | + \displaystyle+ | OPEN 16104 ​ t 2 + 12237 ​ t 3 + 5651 ​ t 4 + 1593 ​ t 5 + 255 ​ t 6 + 18 ​ t 7) ​ q ​ w 2 + 3 ​ ( 2 + t) 2 ​ ( 260 + 888 ​ t + 972 ​ t 2 + 544 ​ t 3 CLOSE \displaystyle 16104t^{2}+12237t^{3}+5651t^{4}+1593t^{5}+255t^{6}+18t^{7})qw^{2}+3(2+t)^{2}(260+888t+972t^{2}+544t^{3} |  |

 |  | + \displaystyle+ | OPEN OPEN 153 ​ t 4 + 18 ​ t 5) ​ w 3) \displaystyle 153t^{4}+18t^{5})w^{3}) |  |

 | E \displaystyle E | = \displaystyle= | 9 ​ ( ( 65 + 141 ​ t + 111 ​ t 2 + 41 ​ t 3 + 6 ​ t 4) 2 ​ q 4 + 8 ​ ( 22750 + 79965 ​ t + 121251 ​ t 2 + 105282 ​ t 3 + 57708 ​ t 4 CLOSE CLOSE \displaystyle 9((65+141t+111t^{2}+41t^{3}+6t^{4})^{2}q^{4}+8(22750+79965t+121251t^{2}+105282t^{3}+57708t^{4} |  |

 |  | + \displaystyle+ | OPEN 20529 ​ t 5 + 4643 ​ t 6 + 612 ​ t 7 + 36 ​ t 8) ​ w ​ q 3 − 2 ​ ( 120300 + 457050 ​ t + 737244 ​ t 2 + 678163 ​ t 3 + 394077 ​ t 4 CLOSE \displaystyle 20529t^{5}+4643t^{6}+612t^{7}+36t^{8})wq^{3}-2(120300+457050t+737244t^{2}+678163t^{3}+394077t^{4} |  |

 |  | + \displaystyle+ | OPEN 149001 ​ t 5 + 35957 ​ t 6 + 5088 ​ t 7 + 324 ​ t 8) ​ w 2 ​ q 2 + 8 ​ ( 2 + t) 2 ​ ( 1750 + 6380 ​ t + 7959 ​ t 2 + 5294 ​ t 3 + 1987 ​ t 4 CLOSE \displaystyle 149001t^{5}+35957t^{6}+5088t^{7}+324t^{8})w^{2}q^{2}+8(2+t)^{2}(1750+6380t+7959t^{2}+5294t^{3}+1987t^{4} |  |

 |  | + \displaystyle+ | OPEN OPEN 408 ​ t 5 + 36 ​ t 6) ​ q ​ w 3 + ( 20 + 66 ​ t + 66 ​ t 2 + 31 ​ t 3 + 6 ​ t 4) 2 ​ w 4). \displaystyle 408t^{5}+36t^{6})qw^{3}+(20+66t+66t^{2}+31t^{3}+6t^{4})^{2}w^{4}). |  |

###### Theorem 3.3.

The curve 𝒞: Y 2 = A ​ X 4 + B ​ X 3 + C ​ X 2 + D ​ X + E \operatorname{\mathcal{C}}:Y^{2}=AX^{4}+BX^{3}+CX^{2}+DX+E defined over ℚ ⁡ ( t) {\mathbb{Q}}(t) is birationally equivalent over ℚ ⁡ ( t, p, q, w) {\mathbb{Q}}(t,p,q,w) to an elliptic curve ℰ {\mathcal{E}} with rank ⁡ ℰ ⁡ ( ℚ ⁡ ( t, p, q, w)) ≥ 1 \operatorname{rank}{\mathcal{E}}({\mathbb{Q}}(t,p,q,w))\geq 1.

Proof: After homogenizing the equation describing 𝒞 \operatorname{\mathcal{C}}, one obtains Y 2 = A ​ X 4 + B ​ X 3 ​ Z + C ​ X 2 ​ Z 2 + D ​ X ​ Z 3 + E ​ Z 4 Y^{2}=AX^{4}+BX^{3}Z+CX^{2}Z^{2}+DXZ^{3}+EZ^{4} with a rational point R = ( X: Y: Z) = ( 1: 140 + 246 t + 166 t 2 + 51 t 3 + 6 t 4: 0) R=(X:Y:Z)=(1:140+246t+166t^{2}+51t^{3}+6t^{4}:0). The curve 𝒞 \operatorname{\mathcal{C}} is birationally equivalent to the cubic curve ℰ {\mathcal{E}} defined by the equation V 2 = U 3 − 27 ​ I ​ U − 27 ​ J V^{2}=U^{3}-27IU-27J, [11], where I = 12 ​ A ​ E − 3 ​ B ​ D + C 2 I=12AE-3BD+C^{2} and J = 72 ​ A ​ C ​ E + 9 ​ B ​ C ​ D − 27 ​ A ​ D 2 − 27 ​ B 2 ​ E − 2 ​ C 3 J=72ACE+9BCD-27AD^{2}-27B^{2}E-2C^{3}. The discriminant Δ ⁡ ( ℰ) \Delta({\mathcal{E}}) of ℰ {\mathcal{E}} is given by ( 4 ​ I 3 − J 2) / 27 (4I^{3}-J^{2})/27, and the specialization of ℰ {\mathcal{E}} is singular only if Δ ⁡ ( ℰ) = 0 \Delta({\mathcal{E}})=0. Moreover, the point P = ( 3 ​ 3 ​ B 2 − 8 ​ A ​ C 4 ​ A, 27 ​ B 3 + 8 ​ A 2 ​ D − 4 ​ A ​ B ​ C 8 ​ A 3 / 2) P=\displaystyle\left(3\frac{3B^{2}-8AC}{4A},27\frac{B^{3}+8A^{2}D-4ABC}{8A^{3/2}}\right) lies in ℰ ⁡ ( ℚ ⁡ ( t, p, q, w)) {\mathcal{E}}({\mathbb{Q}}(t,p,q,w)) since A A is a square. One considers the specialization t = 1, q = 81 40, w = 1 \displaystyle t=1,q=\frac{81}{40},w=1 to obtain the specialization P ~ = ( − 4786935489 100, − 56568093052527 50) \displaystyle\widetilde{P}=\left(\frac{-4786935489}{100},\frac{-56568093052527}{50}\right) of the point P P on the specialized elliptic curve

 | ℰ ~: y 2 = x 3 − 147183268996968521373 10000 ​ x + 171278570868444028577352480093 250000. \widetilde{{\mathcal{E}}}:y^{2}=x^{3}-\frac{147183268996968521373}{10000}x+\frac{171278570868444028577352480093}{250000}. |  |

Using 𝖬𝖠𝖦𝖬𝖠 {\sf MAGMA}, [4], the point P ~ \widetilde{P} is a point of infinite order on ℰ ~ \widetilde{{\mathcal{E}}}. Therefore, according to Silverman’s specialization Theorem, the point P P is of infinite order on ℰ {\mathcal{E}}. □ \Box

###### Corollary 3.4.

For any nontrivial sequence of consecutive rational squares t 0 2, ( t 0 + 1) 2, ( t 0 + 2) 2, ( t 0 + 3) 2, ( t 0 + 4) 2 t_{0}^{2},(t_{0}+1)^{2},(t_{0}+2)^{2},(t_{0}+3)^{2},(t_{0}+4)^{2}, there exist infinitely many elliptic curves E m: y 2 = a m ​ x 3 + b m ​ x + c m, m ∈ ℤ ∖ { 0 }, E_{m}:y^{2}=a_{m}x^{3}+b_{m}x+c_{m},\;m\in{\mathbb{Z}}\setminus\{0\}, such that ( t 0 + i) 2, i = 0, 1, 2, 3, 4, (t_{0}+i)^{2},i=0,1,2,3,4, is the x x -coordinate of a rational point on E m E_{m}. Moreover, these five rational points are independent.

Proof: We fix t = t 0 t=t_{0}, q = q 0 q=q_{0}, and w = w 0 w=w_{0} in ℚ {\mathbb{Q}}. Substituting these values into ( 4), one obtains the elliptic curve

 | 𝒞 t 0, q 0, w 0: h 2 = A ​ p 4 + B ​ p 3 + C ​ p 2 + D ​ p + E, A, B, C, D ∈ ℚ, \operatorname{\mathcal{C}}_{t_{0},q_{0},w_{0}}:h^{2}=Ap^{4}+Bp^{3}+Cp^{2}+Dp+E,\;A,B,C,D\in{\mathbb{Q}}, |  |

with positive rank, see Theorem 3.3. Now, one fixes a point P = ( p, h) P=(p,h) of infinite order in 𝒞 t 0, q 0, w 0 ⁡ ( ℚ) \operatorname{\mathcal{C}}_{t_{0},q_{0},w_{0}}({\mathbb{Q}}). For any nonzero integer m m, we set m ​ P = ( p m, h m) mP=(p_{m},h_{m}) to be the m m -th multiple of the point P P in 𝒞 t 0, q 0, w 0 ⁡ ( ℚ) \operatorname{\mathcal{C}}_{t_{0},q_{0},w_{0}}({\mathbb{Q}}).

Now, one substitutes t = t 0, q = q 0, w = w 0 t=t_{0},q=q_{0},w=w_{0}, and p = p m p=p_{m} into the formulas for d, e, f, g ∈ ℚ ⁡ ( t, p, q, w) d,e,f,g\in{\mathbb{Q}}(t,p,q,w) in ( 3) in order to obtain the rational numbers d m, e m, f m, g m d_{m},e_{m},f_{m},g_{m}, respectively. Then one substitutes d m, e m, f m d_{m},e_{m},f_{m} into the formulas for a, b, c ∈ ℚ ⁡ ( t, d, e, f) a,b,c\in{\mathbb{Q}}(t,d,e,f) in ( 3) to get the rational numbers a m, b m, c m a_{m},b_{m},c_{m}, respectively.

To sum up, one constructed an infinite family of elliptic curves E m: y 2 = a m ​ x 3 + b m ​ x + c m E_{m}:y^{2}=a_{m}x^{3}+b_{m}x+c_{m}, where m m is a nonnegative integer. The latter infinite family E m E_{m} of elliptic curves satisfies the property that the points ( t 0 2, d m), ( ( t 0 + 1) 2, e m), ( ( t 0 + 2) 2, f m), ( ( t 0 + 3) 2, g m), ( ( t 0 + 4) 2, h m) ∈ E m ​ ( ℚ) (t_{0}^{2},d_{m}),((t_{0}+1)^{2},e_{m}),((t_{0}+2)^{2},f_{m}),((t_{0}+3)^{2},g_{m}),((t_{0}+4)^{2},h_{m})\in E_{m}({\mathbb{Q}}). Thus, one obtains an infinite family of elliptic curves with a 5 5 -term sequence of rational points whose x x -coordinates form a sequence of consecutive squares in ℚ {\mathbb{Q}}.

To show that the points ( t 0 2, d m), ( ( t 0 + 1) 2, e m), ( ( t 0 + 2) 2, f m), ( ( t 0 + 3) 2, g m), ( ( t 0 + 4) 2, h m) ∈ E m ​ ( ℚ) (t_{0}^{2},d_{m}),((t_{0}+1)^{2},e_{m}),((t_{0}+2)^{2},f_{m}),((t_{0}+3)^{2},g_{m}),((t_{0}+4)^{2},h_{m})\in E_{m}({\mathbb{Q}}) are independent, one specializes t = 1, q = 81 / 40, w = 1 \displaystyle t=1,q=81/40,w=1 which yields the existence of the infinite point ( p, h) = ( 2201 2320, − 62736289 18852320) ∈ 𝒞 1, 81 / 40, 1 ⁡ ( ℚ) \displaystyle(p,h)=\left(\frac{2201}{2320},\frac{-62736289}{18852320}\right)\in\operatorname{\mathcal{C}}_{1,81/40,1}({\mathbb{Q}}). Therefore, the specialization t = 1, q = 81 / 40, w = 1, p = 2201 / 2320 t=1,q=81/40,w=1,p=2201/2320 gives us the specialized elliptic curve

 | E 1: y 2 = 42674183 52786496000 ​ x 3 − 612989889 7540928000 ​ x + 1180698375893607 2487869785676800 E_{1}:{\footnotesize y^{2}=\frac{42674183}{52786496000}x^{3}-\frac{612989889}{7540928000}x+\frac{1180698375893607}{2487869785676800}} |  |

with the following set of rational points in E 1 ​ ( ℚ) E_{1}({\mathbb{Q}}):

 | ( 1, − 2367005 3770464), ( 2 2, 8455597 18852320), ( 3 2, − 10868031 18852320), ( 4 2, − 29720351 18852320), ( 5 2, − 62736289 18852320). \left(1,\frac{-2367005}{3770464}\right),\left(2^{2},\frac{8455597}{18852320}\right),\left(3^{2},\frac{-10868031}{18852320}\right),\\ \left(4^{2},\frac{-29720351}{18852320}\right),\left(5^{2},\frac{-62736289}{18852320}\right). |  |

Using 𝖬𝖠𝖦𝖬𝖠 {\sf MAGMA}, [4], these rational points are independent.

According to Silverman’s Specialization Theorem, it follows that the points ( t 0 2, d m), ( ( t 0 + 1) 2, e m), ( ( t 0 + 2) 2, f m), ( ( t 0 + 3) 2, g m), ( ( t 0 + 4) 2, h m) (t_{0}^{2},d_{m}),((t_{0}+1)^{2},e_{m}),((t_{0}+2)^{2},f_{m}),((t_{0}+3)^{2},g_{m}),((t_{0}+4)^{2},h_{m}) are independent in E m E_{m} over ℚ ⁡ ( t 0, q 0, w 0, p m) {\mathbb{Q}}(t_{0},q_{0},w_{0},p_{m}). □ \Box

###### Remark 3.5.

Corollary 3.4 implies the existence of an infinite family of elliptic curves whose rank r ≥ 5 r\geq 5.

###### Remark 3.6.

One notices that a sequence of consecutive squares on an elliptic curve gives rise to a set of rational points on some hyperelliptic curve of genus 2 2, see the proof of Proposition 2.2. Therefore, according to Corollary 3.4, we are able to construct an infinite family of hyperelliptic curves 𝒞 \operatorname{\mathcal{C}} such that | 𝒞 ⁡ ( ℚ) | ≥ 5 |\operatorname{\mathcal{C}}({\mathbb{Q}})|\geq 5.

*Acknowledgements.*We would like to thank Professor Nabil Youssef, Cairo University, for his support, thorough reading of the manuscript, and several useful suggestions.

## References

- [1]
- [2] A. Alvarado, An arithmetic progression on quintic curves, J. Integer Seq., 12 (2009), Article 09.7.3.
- [3] A. O. L. Atkin and F. Morain, Finding suitable curves for the elliptic curve method of factorization, Mathematics of Computation, 60 (1993), 399–405.
- [4] W. Bosma and J. Cannon and C. Playoust, MAGMA 2.14-1, available at http://magma.maths.usyd.edu.au.
- [5] A. Bremner, On arithmetic progressions on elliptic curves, Experiment. Math., 8 (1999), 409-–413.
- [6] A. Bremner and M. Ulas, Rational points in geometric progressions on certain hyperelliptic curves, Publicationes Mathematica, 82 (2013), 669–683.
- [7] G. Campbell, A note on arithmetic progressions on elliptic curves, J. Integer Seq., 6 (2003), Article 03.1.3.
- [8] G. Faltings, Endlichkeitssätze für abelsche Varietäten über Zahlkörpern, Invent. Math. 73 (1983), 349-–366.
- [9] A. J. MacLeod, 14-term arithmetic progressions on quartic elliptic curves, J. Integer Seq., 9 (2006), Article 06.1.2.
- [10] L. J. Mordell, Diophantine Equations, Academic Press, New York, 1969.
- [11] M. Stoll and J. E. Cremona, Minimal models for 2-coverings of elliptic curve, LMS J. Comput. Math., 5 (2002), 220–243.
- [12] M. Ulas, A note on arithmetic progressions on quartic elliptic curves, J. Integer Seq., 8 (2005), Article 05.3.1.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:mohgamal@sci.cu.edu.eg
[4]: mailto:mmsadek@aucegypt.edu
