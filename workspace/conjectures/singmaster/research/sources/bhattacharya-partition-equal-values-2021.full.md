<!-- source: https://link.springer.com/article/10.1007/s40993-021-00293-7 | converted from HTML -->

Equal values of certain partition functions via Diophantine equations | Research in Number Theory | Springer Nature Link

Skip to main content

# Equal values of certain partition functions via Diophantine equations

- Research
- [Open access][1]
- Published: 21 October 2021

- Volume 7, article number 67 ( 2021)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Research in Number Theory][5] [Aims and scope][6] [Submit manuscript][7]

Equal values of certain partition functions via Diophantine equations

[Download PDF][2]

## Abstract

Let \(A\subset \mathbb {N}_{+}\) and by \(P_{A}(n)\) denotes the number of partitions of an integer *n*into parts from the set *A*. The aim of this paper is to prove several result concerning the existence of integer solutions of Diophantine equations of the form \(P_{A}(x)=P_{B}(y)\), where *A*, *B*are certain finite sets.

### Similar content being viewed by others

### [Positive integer solutions of some Diophantine equations in terms of integer sequences][8]

Article 28 September 2018

### [Three simple reduction formulas for the denumerant functions][9]

Article 26 September 2024

### [The Prouhet–Tarry–Escott problem, indecomposability of polynomials and Diophantine equations][10]

Article Open access 11 April 2022

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algebra][11]
- [Combinatorics][12]
- [Computational Number Theory][13]
- [Discrete Mathematics][14]
- [Integral Equations][15]
- [Number Theory][16]
- [Diophantine Equations in Algebraic Number Theory][17]

## 1 Introduction

Let \(\mathbb {N}\) be the set of non-negative integers, \(\mathbb {N}_{+}\) the set of positive integers and for \(k\in \mathbb {N}_{+}\) we write \(\mathbb {N}_{\ge k}\) for the set of integers \(\ge k\).

Let \(A\subset \mathbb {N}_{+}\) be given and take \(n\in \mathbb {N}\). By an *A*-partition \(\lambda =(\lambda _{1},\ldots , \lambda _{k})\), of a non-negative integer *n*with parts in *A*, we mean representation of *n*in the form

$$\begin{aligned} n=\lambda _{1}+\cdots +\lambda _{k}, \end{aligned}$$

where \(\lambda _{i}\in A\). The representations of *n*differing only in order of the terms are counted as a one. We also put

$$\begin{aligned} {\text {Part}}_{A}(n)=\{\lambda :\;\lambda \;\text{ is }\;A\text{-partition } \text{ of }\;n\}, \end{aligned}$$

and consider the corresponding partition function

$$\begin{aligned} P_{A}(n):=\#{\text {Part}}_{A}(n). \end{aligned}$$

It is well know that the ordinary generating function of the sequence \((P_{A}(n))_{n\in \mathbb {N}}\) takes the form

$$\begin{aligned} \prod _{a\in A}\frac{1}{1-x^{a}}=\sum _{n=0}^{\infty }P_{A}(n)x^{n}. \end{aligned}$$

In particular, if \(A=\mathbb {N}_{+}\), then \(P_{A}(n)\), simply denoted as *p*(*n*), is the famous partition function introduced by L. Euler and extensively studied by S. Ramanujan. The function *p*(*n*) counts the number of partitions with parts in \(\mathbb {N}_{+}\), i.e., unrestricted partitions of *n*. Many questions concerning arithmetic properties of *p*(*n*) is still unsolved. Probably, the most famous one, is the question whether the sequence \(\{p(n)\mod m\}_{n\in \mathbb {N}}\) is equidistributed modulo *m*, i.e., whether, for any given \(m\in \mathbb {N}_{\ge 2}\) and each \(r\in \{0,\ldots , m-1\}\), there is an equality

$$\begin{aligned} \limsup _{N\rightarrow +\infty }\frac{\#\{n\le N:\;p(n)\equiv r\pmod {m}\}}{N}=\frac{1}{m}. \end{aligned}$$

For discussion on this topic see [[1][18]].

The literature concerning arithmetic properties of functions counting various partitions is enormous. One of the central problems in partition theory is to obtain partition identities [[3][19]]. More precisely, if \({\mathcal {W}}\) is a certain property which can be applied to the parts of a given *A*-partition \(\lambda \) of a positive integer *n*, then by \(P_{A}({\mathcal {W}},n)\) we denote the number of *A*-partitions of *n*which have the property \({\mathcal {W}}\). Thus, by a partition identity we mean an identity of the form

$$\begin{aligned} P_{A_{1}}({\mathcal {W}}_{1},n)=P_{A_{2}}({\mathcal {W}}_{2},n), \end{aligned}$$

where \(A_{1}, A_{2}\subset \mathbb {N}_{+}\) and \({\mathcal {W}}_{1}, {\mathcal {W}}_{2}\) are given properties. The basic identity of the kind is Euler’s famous identity

$$\begin{aligned} \prod _{n=1}^{\infty }(1+x^{n})=\prod _{n=1}^{\infty }\frac{1}{1-x^{2n-1}}, \end{aligned}$$

which gives the equality between the number of partitions into distinct parts and the number of partitions into odd parts. Equivalently

$$\begin{aligned} P_{\mathbb {N}_{+}}(\text{ distinct } \text{ parts },n)=P_{\mathbb {N}_{+}}(\text{ odd } \text{ parts },n). \end{aligned}$$

Euler’s identity can be proved by a simple manipulation of infinite products. Much deeper partition identities are two (of many known) Rogers–Ramanujan type identities. These identities can be deduced from the equalities of the type: infinite product \(=\) infinite series, i.e.,

$$\begin{aligned} \prod _{n=1}^{\infty }\frac{1}{(1-x^{5n-1})(1-x^{5n-4})}&=\sum _{n=1}^{\infty }\frac{x^{n^{2}}}{(1-x)(1-x^{2})\cdot \ldots \cdot (1-x^{n})},\\ \prod _{n=1}^{\infty }\frac{1}{(1-x^{5n-2})(1-x^{5n-3})}&=\sum _{n=1}^{\infty }\frac{x^{n^{2}+n}}{(1-x)(1-x^{2})\cdot \ldots \cdot (1-x^{n})}. \end{aligned}$$

The first identity implies that the number of partitions of *n*such that the adjacent parts differ by at least 2 is the same as the number of partitions of *n*such that each part is congruent to either 1 or 4 modulo 5, i.e.,

$$\begin{aligned} P_{\mathbb {N}_{+}}(\text{ adjacent } \text{ parts } \text{ differ } \text{ by } \text{ at } \text{ least } \text{2 },n)=P_{\mathbb {N}_{+}}(\text{ parts }\equiv 1, 4\pmod {5},n). \end{aligned}$$

The second one implies that the number of partitions of *n*such that the adjacent parts differ by at least 2 and such that the smallest part is at least 2 is the same as the number of partitions of *n*such that each part is congruent to either 2 or 3 modulo 5. Mentioned identities are only special cases of more general one which can be found in the literature. However, according to our best knowledge nothing is known about identities of the form

$$\begin{aligned} P_{A_{1}}({\mathcal {W}}_{1},n)=P_{A_{2}}({\mathcal {W}}_{2},m)\ne 0, \end{aligned}$$

(1)

where *n*, *m*are *different*positive integers.

Of course, in the above, we are interested in non-trivial identities. More precisely, if the set of values of \(P_{A_{i}}({\mathcal {W}}_{i},n)\) contains all positive integers for some \(i\in \{1,2\}\) then the problem is trivial. For example, if \(A_{1}=\{2^{j}:\;j\in \mathbb {N}\}\) and the property \({\mathcal {W}}_{1}\) says that at least two parts in \(A_{1}\) -partition of *n*are equal, then, for \(s(n):=P_{A_{1}}({\mathcal {W}}_{1},n)\) we clearly have

$$\begin{aligned} \sum _{n=0}^{\infty }s(n)x^{n}=\prod _{n=0}^{\infty }(1+x^{2^{n}}+x^{2^{n+1}}), \end{aligned}$$

and the sequence \(\{s(n)\}_{n\in \mathbb {N}}\) is a famous Stern sequence satisfying the recurrence relations

$$\begin{aligned} s(0)=1,\quad s(2n)=s(n)+s(n-1),\quad s(2n+1)=s(n). \end{aligned}$$

One can easily prove that \(s(2^{n})=n+1\) and thus the sequence \((s(n))_{n\in \mathbb {N}}\) contains all positive integers. Thus the question concerning the existence of positive integer solutions of related equation is trivial.

Of great interests would be the proof of non-existence of \(A_{i}, {\mathcal {W}}_{i}, i=1, 2\) such that the corresponding partition functions \(P_{A_{i}}({\mathcal {W}}_{i},n), i=1, 2,\) have exponential growth and equation ( [1][20]) has infinitely many solutions in positive integers. Note that if \(P_{A_{i}}({\mathcal {W}}_{i},n)\) has an exponential growth then the set \(A_{i}\) is necessarily infinite.

A related question is to whether given partition function takes values in a given infinite set. Especially, in the set of values of a given polynomial. In other words we are interested in the solvability in non-negative integers of the equation

$$\begin{aligned} f(m)=P_{A}({\mathcal {W}},n)\ne 0, \end{aligned}$$

(2)

where \(f\in \mathbb {Q}[x]\) is of positive degree and positive leading coefficient. Again we are interested in non-trivial situations only. Here if *f*is linear, then we enter in the realm of partition congruences. The Ramanujan congruences

$$\begin{aligned} p(5n+4)\equiv & {} 0\pmod {5}, \quad p(7n+5)\equiv 0\pmod {7},\quad \\ p(11n+7)\equiv & {} 0\pmod {11} \end{aligned}$$

and its various generalizations give some non-trivial examples when equation ( [2][21]) has infinitely many solutions in positive integers. Indeed, each equation

$$\begin{aligned} p(n)=5m, \quad p(n)=7m,\quad p(n)=11m \end{aligned}$$

has infinitely many solutions in positive integers. In fact, one can prove that for each prime \(q\ne 3\) the Diophantine equation \(p(n)=qm\) has infinitely many solutions in positive integers. Indeed, Nicolas, Ruzsa and Sárközy [[13][22]] proved this for \(q=2\), and Ono proved that such a statement is true for each \(q\ge 5\) [[18][23]].

In case of equation ( [2][21]) more can be said provided we know some arithmetic properties of the partition function \(P_{A}({\mathcal {W}},n)\). For example, if \(A=\{2^{i}:\;i\in \mathbb {N}\}\) then so called binary partition function \(b(n):=P_{A}(n)\) counting the partitions with all parts being powers of 2, satisfies the recurrence relation

$$\begin{aligned} b(0)=1,\quad b(2n)=b(2n-1)+b(n),\quad b(2n+1)=b(2n). \end{aligned}$$

A classical result of Churchhouse states that \(\nu _{2}(b(n))\in \{1,2\}\) for \(n\in \mathbb {N}_{\ge 2}\) [[7][24]]. Thus, if

$$\begin{aligned} \{1,2\}\cap \{\nu _{2}(f(m)):\;m\in \mathbb {N}_{+}\}=\emptyset \end{aligned}$$

then equation ( [2][21]) has at least \({\text {deg}} f\) solutions possibly coming from the integer solutions of the equation \(f(m)=1\).

Our discussion above shows that the problem of solvability of Eqs. ( [1][20]) or ( [2][21]) is interesting, difficult and worth of further investigations. It is clear that our questions are on the intersection of discrete mathematics, combinatorics and Diophantine equations. This suggest to start investigations with the case of *A*finite. This is reasonable due to the fact that \(p_{A}(n)\) is a quasi polynomial (see for example [[14][25]]). More precisely, if \(A=(a_{1},\ldots , a_{k})\) and \(L_{A}:={\text {lcm}}(a_{1}, \ldots , a_{k})\), then

$$\begin{aligned} p_{A}(L_{A}n+i)\in \mathbb {Q}[n]\quad \text{ for }\quad i=0, 1, \ldots , L_{A}-1. \end{aligned}$$

Thus, if \(A_{1}, A_{2}\) are finite, then solvability in positive integers of equation ( [1][20]) or a more general equation ( [2][21]), is equivalent with the solvability in non-negative integers, of at least one equation of the type

$$\begin{aligned} p_{A_{1}}(L_{A_{1}}m+i)=p_{A_{2}}(L_{A_{2}}n+j), \end{aligned}$$

where \(i\in \{0, 1, \ldots , L_{A_{1}}-1\}, j\in \{0, 1, \ldots , L_{A_{2}}-1\}\), or

$$\begin{aligned} f(m)=p_{A_{1}}(L_{A_{1}}n+i),\quad i\in \{0, 1, \ldots , L_{A_{1}}-1\}, \end{aligned}$$

respectively. Thus, we enter into realm of polynomial Diophantine equations with separable variables where great deal of methods are for our disposal.

In the rest of the paper, in case of the set \(A=\{1,\ldots , m\}\) instead of writing \(P_{A}(x)\) and \({\text {Part}}_{A}(n)\), we will simply write \(P_{m}(x)\) and \({\text {Part}}_{m}(n)\), respectively. Let us describe the content of the paper in some details.

In Sect. [2][26] we prove that for each \(f\in \mathbb {Z}[x]\) with positive degree and positive leading coefficient and \(A=\{a_{1}, a_{2}\}\subset \mathbb {N}_{+}\) with \(\gcd (a_{1},a_{2})=1\), the Diophantine equation \(P_{A}(x)=f(y)\) has infinitely many solutions in positive integers (Theorem [2.1][27]).

Section [3][28] is mainly devoted to the study of the equation \(P_{3}(x)=P_{n}(y)\) for \(n=4, 5\). In particular, we describe all positive integer solutions in both cases and present some related results (Theorems [3.1][29] and [3.2][30]).

In Sect. [4][31] we study some equation involving \(P_{A}(x)\), where \(A=\{1,2,a\}, a\in \mathbb {N}_{\ge 3}\). In particular, we obtain a general result concerning the existence of infinitely many positive integer solutions of the equation \(P_{A}(x)=P_{4}(y)\) (Theorem [4.3][32]). We also obtain, under weak assumptions on \(a, b\in \mathbb {N}_{\ge 3}, a\ne b\), that for \(A=\{1, 2, a\}, B=\{1, 2, b\}\), the Diophantine equation \(P_{A}(x)=P_{B}(y)\) has infinitely many solutions in positive integers (Theorem [4.5][33]).

In Sect. [5][34] we obtain several results concerning the square values of \(P_{A}(x)\). In particular we describe the set of positive integer solutions of the equation \(y^2=P_{n}(x)\) for \(n=3, 4, 5\). We also discuss results of some computations. Finally, in the last section we collect some general questions and conjectures concerning various aspects of the Diophantine equations of the form \(P_{A}(x)=P_{B}(y)\) and report results of various computations.

## 2 The case of \(A=\{a_{1},a_{2}\}\)

In this short section we prove a general result concerning the existence of positive integer solutions of the Diophantine equation

$$\begin{aligned} P_{A}(x)=f(y), \end{aligned}$$

where \(A=\{a_{1}, a_{2}\}, a_{1}<a_{2}\) and \(f\in \mathbb {Z}[y]\) is a non-constant polynomial with positive leading coefficient. More precisely, based on the formula obtained by Sertöz in [[15][35]] we easily prove the following.

### Theorem 2.1

Let \(A=\{a_{1}, a_{2}\}\subset \mathbb {N}_{+}\). Then, for each \(f\in \mathbb {Z}[x]\) with positive leading coefficient, the Diophantine equation \(P_{A}(x)=f(y)\) has infinitely many solutions in positive integers.

### Proof

Without loss of generality we can assume that \(\gcd (a_{1},a_{2})=1\). Then, by Sertöz result [[15][35]], we know that the following formula holds

$$\begin{aligned} P_{A}(n)=\frac{n+a_{1}\cdot a_{1}'+a_{2}\cdot a_{2}'}{a_{1}a_{2}}-1, \end{aligned}$$

where \(a_{i}\cdot a_{i}'\equiv -n\pmod {a_{i+1}}\) and \(1\le a_{i}'(n)\le a_{i+1}\) for \(i=1, 2\) and if \(i=2\), then \(i+1\) is taken modulo 2. In particular, for each \(n\in \mathbb {N}_{+}\)

$$\begin{aligned} P_{A}(n)=\left\lfloor \frac{n}{a_{1}a_{2}}\right\rfloor \quad \text{ or }\quad P_{A}(n)=\left\lfloor \frac{n}{a_{1}a_{2}}\right\rfloor +1. \end{aligned}$$

Thus, let us take \(n=a_{1}a_{2}(f(m)-1)\), with \(m\in \mathbb {N}_{+}\) chosen in such a way that \(f(m)>1\). We thus consider the congruence

$$\begin{aligned} a_{i}\cdot a_{i}'\equiv -n\equiv -a_{1}a_{2}(f(m)-1)\equiv 0\pmod {a_{i+1}} \end{aligned}$$

and due to co-primality condition and the bound for \(a_{1}', a_{2}'\), we get that \(a_{i}'=a_{i+1}\), i.e., we have that \(a_{1}'=a_{2}, a_{2}'=a_{1}\). In consequence

$$\begin{aligned} P_{A}(a_{1}a_{2}(f(m)-1))=\frac{a_{1}a_{2}(f(m)-1)+a_{1}a_{2}+a_{2}a_{1}}{a_{1}a_{2}}-1=f(m) \end{aligned}$$

and our theorem is proved. \(\square \)

## 3 The equation \(P_{3}(x)=P_{n}(y)\) for \(n=4, 5\)

In this section we are interesting in the characterization of positive integer solutions of the Diophantine equation

$$\begin{aligned} P_{3}(x)=P_{n}(y) \end{aligned}$$

for \(n=4, 5\).

### Theorem 3.1

The Diophantine equation \(P_{3}(x)=P_{4}(y)\) has infinitely many solutions in integers.

### Proof

First of all we recall that

$$\begin{aligned} P_{3}(n)&=\left\lfloor \frac{(n+3)^{2}}{12}\right\rceil ,\\ P_{4}(n)&=\left\lfloor \frac{(n+1)(n^2+23n+85)}{144}-\frac{n+4}{8}\left\lfloor \frac{n+1}{2}\right\rfloor \right\rceil , \end{aligned}$$

where \(\lfloor x\rceil \) denotes the nearest integer to *x*. For concise proofs of these two identities see [[2][36], pp. 57–60]. An alternative recent proof of these and related equalities were obtained by Castillo et al. [[5][37]].

From the form of \(P_{3}(n)\) we see that for \(i\in \{0,\ldots , 5\}\) the expression \(P_{3}(6n+i)\) is a polynomial in *n*. More precisely, we define \(P_{i,6,3}(n)=P_{3}(6n+i)\) and observe that

$$\begin{aligned} \begin{array}{ll} P_{0,6,3}(n)=3n^2+3n+1, &{} P_{1,6,3}(n)=(n+1)(3n+1), \\ P_{2,6,3}(n)=(n+1)(3n+2), &{} P_{3,6,3}(n)=3(n+1)^2,\\ P_{4,6,3}(n)=(n+1)(3n+4), &{} P_{5,6,3}(n)=(n+1)(3n+5).\\ \end{array} \end{aligned}$$

We can similar treat the case of \(P_{4}(n)\) and by defining \(P_{2i+1,6,4}(n)=P_{4}(6n+2i+1)\) for \(i=0, 1, 2\) and \(P_{2i,12,4}(n)=P_{4}(12n+2i)\) for \(i=0, 1, \ldots , 5\), we get

$$\begin{aligned} \begin{array}{ll} P_{1,6,4}(n)=\frac{1}{2} (n+1) \left( 3 n^2+6 n+2\right) , &{} P_{3,6,4}(n)=\frac{3}{2} (n+1)^2 (n+2), \\ P_{5,6,4}(n)=\frac{3}{2} (n+1) (n+2)^2, &{} \\ P_{0,12,4}(n)=12n^3+15n^2+6n+1, &{} P_{2,12,4}(n)=12n^3+21n^2+12n+2, \\ P_{4,12,4}(n)=(n+1)(12n^2+15n+5), &{} P_{6,12,4}(n)=3(n+1)^2(4n+3), \\ P_{8,12,4}(n)=3(n+1)^2(4n+5), &{} P_{10,12,4}(n)=(n+1)(12n^2+33n+23). \end{array} \end{aligned}$$

In order to characterize all integers solutions of the Diophantine equation \(P_{3}(x)=P_{4}(y)\) we need to perform case by case analysis. More precisely, we consider all possible combinations of the equations

$$\begin{aligned} \mathrm{(I)}\quad P_{i,6,3}(x)=P_{2j+1,6,4}(y)\quad \quad \text{ or }\quad \quad \mathrm{(II)}\quad P_{i,6,3}(x)=P_{2j,12,4}(y), \end{aligned}$$

i.e., we deal with 54 equations. In each case we deal in the same way. Because the degree of \(P_{i,6,3}\) is 2, each equation of interests can be reduced to the equation of the type \(Y^2=f(X)\) for some \(f\in \mathbb {Z}[X]\) and the degree of *f*is 3. If *f*has no multiple roots, by classical Siegel result, we know that the curve defined by the equation \(Y^2=f(X)\) has only finitely many integral points. On the other hand, if *f*has multiple roots then there is a chance that our equation has infinitely many integral solutions which can be parameterized via polynomials.

In order to see what is going on, let us consider the equation

$$\begin{aligned} P_{1,6,3}(x)=P_{3,6,4}(y),\;\text{ i.e. },\; (x+1)(3x+1)=\frac{3}{2}(y+1)^2(y+2) \end{aligned}$$

(3)

or equivalently \(Y^2=X^3-108X+1728\), where we put \(X=6(3y+4), Y=36(3x+2)\). Our equation represents an elliptic curve, say *E*, in the plane (*X*, *Y*) and standard methods allow to find that the curve *E*has trivial torsion and the rank of *E*is equal to 2, with the generators \((X,Y)=(6, -36), (-2, 44)\). Using internal Magma [[8][38]] procedures

E:=EllipticCurve([-108,1728]);

IntegralPoints(E);

(the background for this latter routine is found in [[11][39]] and [[17][40]]; see also [[19][41]]) we find that the point \((X,Y)\in E(\mathbb {Q})\) has integer coordinates, if and only if

$$\begin{aligned} (X,Y)\in \{&(-12, \pm 36), (-3, \pm 45), (-2, \pm 44), (6, \pm 36), (16, \pm 64), \\&(22, \pm 100), (78, \pm 684), (96, \pm 936), (7926, \pm 705636)\}. \end{aligned}$$

Direct check shows that only the points \(P_{1}=(96, -936)\) and \(P_{2}=(7926, -705636)\) correspond to the solutions of our equation. We thus get that the only integer solutions of equation ( [3][42]) are \((x,y)=(8, 4), (6533, 439)\). We thus get the equalities

$$\begin{aligned} P_{1,6,3}(8)&=P_{3,6,4}(4)=225,\\ P_{1,6,3}(6533)&=P_{3,6,4}(439)=128066400. \end{aligned}$$

Case by case analysis reveals that the solutions exist only in the following cases:

$$\begin{aligned} (i,j)&=(0, 0), (1, 0), (1, 1), (1, 2), (5, 1)\quad \text{ in } \text{ the } \text{ case } \text{(I) }\quad \text{ and }\\ (i,j)&=(0,0), (1,0), (2,1), (3,4), (5,2)\quad \text{ in } \text{ the } \text{ case } \text{(II) }. \end{aligned}$$

In the table below we give all integral solutions in these cases.

#### Table. Values of (*i*, *j*) such that the corresponding equations of types (I), (II) have solutions in non-negative integers.

(*i*, *j*)

 |

integral solutions (*x*, *y*) of \(P_{i,6,3}(x)=P_{2j+1,6,4}(y) \)

 |

(0, 0)

 |

(0, 0)

 |

(0, 1)

 |

(0, 0)

 |

(1, 1)

 |

(8, 4), (6533, 439)

 |

(1, 2)

 |

(293, 54)

 |

(3, 1)

 |

\(((t-1)(2 t^2+2 t+1), 2(t-1)(t+1)), t\in \mathbb {N}_{+}\)

 |

(3, 2)

 |

\((2 t^3+t-1, 2 t^2-1), t\in \mathbb {N}_{+}\)

 |

(5, 1)

 |

(5, 3)

 |

(*i*, *j*)

 |

integral solutions (*x*, *y*) of \(P_{i,6,3}(x)=P_{2j,12,4}(y)\)

 |

(0, 0)

 |

\(((t-1)(2 t^2-t+1), 2 (t-1) t), t\in \mathbb {N}_{+}\)

 |

(1, 0)

 |

(0, 0)

 |

(2, 1)

 |

(0, 0)

 |

(3, 4)

 |

\((2 t^3+3 t^2+t-1, t^2+t-1), t\in \mathbb {N}_{+}\)

 |

(5, 2)

 |

(0, 0)

 |

Having the form of solutions presented in the table above, we can easily back to our original Diophantine equation \(P_{3}(X)=P_{4}(Y)\) and found that solutions take the form \((X,Y)=(6x+i, 6y+2j)\) in the first type equation, and \((X,Y)=(6x+i, 12y+2j+1)\) in the second type equation. \(\square \)

In our next theorem we characterize the set of positive integer solutions of the Diophantine equation \(P_{3}(x)=P_{5}(y)\).

### Theorem 3.2

The equation \(P_{3}(x)=P_{5}(y)\) has only finitely many solutions in positive integers. More precisely, the pair (*x*, *y*) is a solution if and only if \((x,y)\in {\mathcal {A}}\), where

$$\begin{aligned} {\mathcal {A}}=\{&(1, 1), (2, 2), (3, 3), (5, 4), (6, 5), (8, 6), (16, 10), (18, 11), (26, 14), \\&(45, 20), (174, 45), (217, 51), (457, 77), (468, 78), (701, 97), (10093, 388)\}. \end{aligned}$$

### Proof

Direct check reveals that \(P_{5}(60n+i), i\in \{0,\ldots , 59\}\) is a polynomial in variable *n*. Thus, one can perform the same analysis as in the case of the equation \(P_{3}(x)=P_{4}(y)\). However, here the situation is a bit more complicated because, after necessary simplifications, we need to work with the equations of the type \(Y^2=f(X)\), where *f*is a polynomial of degree 4. We need to consider \(6\cdot 60=360\) equations in order to get the result. Here we may apply the Magma procedure IntegralQuarticPoints() based on the paper [[19][41]]. It worked well in all except the 8 cases, where the Magma function failed to determine the complete set of integral solutions. These 8 problematic equations are of the form

$$\begin{aligned} P_{3}(6y+i)=P_{5}(60x+j) \end{aligned}$$

for

$$\begin{aligned} (i,j)\in {\mathcal {A}}=\{(3,9), (3, 12), (3, 21), (3, 24), (3, 33), (3, 36), (3, 48), (3, 57)\}. \end{aligned}$$

The equations corresponding to \((i, j)=(3, 48), (3, 57)\) are of the following form

$$\begin{aligned} Y^2= & {} u(54000u^3 - 16200u^2 + 1410u - 18),\\ Y^2= & {} u(54000u^3 + 16200u^2 + 1410u + 18), \end{aligned}$$

respectively, where \(u=x+1.\) In both cases we obtain that *u*is a square multiplied by a divisor of 18. Therefore we need to handle the equations

$$\begin{aligned} (2\delta ^2 v)^2=(60\delta u)^3 - 18\delta (60\delta u)^2 + 94\delta ^2(60\delta u) - 72\delta ^3, \end{aligned}$$

where \(\delta \in \{\pm 1, \pm 2, \pm 3, \pm 6, \pm 9, \pm 18\}.\) One more time we use the Magma procedure IntegralPoints() to determine the integral points on these elliptic curves. We only need to consider points having first coordinate divisible by \(60\delta .\) It turns out that \(u=0\) is the only solution, that is \((x,Y)=(-1,0).\)

In the remaining 6 cases, we observed that the discriminant of \(P_{3}(6y+i)=P_{5}(60x+j)\) with respect to *y*is equal to

$$\begin{aligned} F(u)=432u^4 + 648u^3 + 282u^2 + 18u, \end{aligned}$$

for suitable substitution of the form \(u=ax+b\) (depending on values of *i*, *j*). The expression for *u*are given below

(*i*, *j*)

 |

(3, 9)

 |

(3, 12)

 |

(3, 21)

 |

(3, 24)

 |

(3, 33)

 |

(3,36)

 |

*u*

 |

\(5x+1\)

 |

\(-5x-2\)

 |

\(5x+2\)

 |

\(-5x-3\)

 |

\(5x+3\)

 |

\(-5x-4\)

 |

Therefore we only need to determine integral points on the curve

$$\begin{aligned} 72u^4 + 108u^3 + 47u^2 + 3u=30v^2. \end{aligned}$$

We obtain that 3 divides *u*, so \(u=3u_1\) for some integer \(u_1.\) We have that

$$\begin{aligned} u_1(648u_1^3+324u_1^2+47u_1+1)=30v_1^2, \text{ where } v=3v_1. \end{aligned}$$

The factorization yields the following elliptic curves

$$\begin{aligned} X^3+324\delta X^2+30456\delta ^2X+419904\delta ^3=Y^2, \text{ where } \delta \in \{1,2,3,5,6,10,15,30\}. \end{aligned}$$

We determined the integral points on these curves and checked if *X*is divisible by \(648\delta ,\) the only such solution corresponds to \(X=0.\) Hence we do not obtain integral solution in case of these six curves. \(\square \)

In the light of the result one can ask for which sequences *A*of the form \(A=\{1, 2, 3, a\}, a\ge 4\), the Diophantine equation \(P_{3}(x)=P_{A}(y)\) has infinitely many solutions in positive integers. It is not difficult to find many values of *a*with this property. Indeed, for a fixed *a*the equation has the form that a quadratic polynomial is equal to a cubic polynomial, hence we may expect a genus 1 curve. However, we for certain values of *a*we may obtain infinitely many integral solutions. The strategy we follow is simple, we determine polynomials \(P_A(6an+k)\) in *n*that are not square-free and then deal with the equation \(P_{3}(6m+3)=3(m+1)^2=P_A(6an+k)\). This works for \(a\in \{4, 6, 12, 14, 20\}\). In these cases the equation \(P_{3}(x)=P_{A}(y)\) has a polynomial solution and hence infinitely many solutions in positive integers.

We close this section with the following

### Conjecture 3.3

There are infinitely many values of \(a\in \mathbb {N}_{\ge 4}\) such that for \(A=\{1, 2, 3, a\}\), the Diophantine equation \(P_{3}(x)=P_{A}(y)\) has infinitely many solutions in positive integers.

## 4 Some properties of \(P_{A}(x)\) for \(A=\{1,2,a\}, a\ge 3\), and related equations

In this section we obtain explicit expression for \(P_{A}(n)\) in case of \(A=\{1, 2, a\}\). As an application we deduce several results concerning Diophantine properties of \(P_{A}(n)\).

### Theorem 4.1

Let \(a\in \mathbb {N}_{\ge 3}\) and put \(A=\{1,2,a\}\). If \(a=2c\) for some \(c\in \mathbb {N}_{\ge 2}\) then

$$\begin{aligned} P_{A}(4cn+i)=2cn^2+\left( c+2\left\lfloor \frac{i}{2}\right\rfloor +2\right) n+{\left\{ \begin{array}{ll}\begin{array}{ll} \left\lfloor \frac{i+2}{2}\right\rfloor , &{} i\in \{0, \ldots , 2c-1\} \\ 2\left\lfloor \frac{i}{2}\right\rfloor +2-a,&{} i\in \{2c, \ldots , 4c-1\} \end{array} \end{array}\right. }. \end{aligned}$$

If \(a=2c+1\) for some \(c\in \mathbb {N}_{+}\) then

$$\begin{aligned} P_{A}(2(2c+1)n&+i)=(2c+1)n^2+(c+i+2)n\\&+{\left\{ \begin{array}{ll}\begin{array}{ll} \left\lfloor \frac{i+2}{2}\right\rfloor , &{} i\in \{0, \ldots , 2c\} \\ i+1-a,&{} i\in \{2c+1, \ldots , 4c+1\} \end{array} \end{array}\right. }. \end{aligned}$$

### Proof

Let \(A=\{1,2,a\}\) and recall that

$$\begin{aligned} \frac{1}{(1-x)(1-x^2)(1-x^a)}=\sum _{n=0}^{\infty }P_{A}(n)x^{n}, \quad \frac{1}{(1-x)(1-x^2)}=\sum _{n=0}^{\infty }\left( \left\lfloor \frac{n}{2}\right\rfloor +1\right) x^{n}. \end{aligned}$$

Thus, using the identity \((1-x^{a})F_{A}(x)=\frac{1}{(1-x)(1-x^2)}\) by comparison of coefficients of like powers on both sides of we get that \(P_{A}(n)\) satisfies the following recurrence relation:

$$\begin{aligned} P_{A}(n)=\left\lfloor \frac{n}{2}\right\rfloor +1, n\le a-1\quad \text{ and }\quad P_{A}(n)=P_{A}(n-a)+\left\lfloor \frac{n}{2}\right\rfloor +1\;\text{ for } \;n\ge a. \end{aligned}$$

Knowing that \(P_{A}(n)\) satisfies recurrence relation of the presented form and using the (conjectural) form of the solution it is easy to perform the rest of the proof by induction. We omit the tiresome details. \(\square \)

There are many papers devoted to the explicit computation of the function \(P_{A}(n)\) for given \(A=\{a_{1},\ldots , a_{k}\}\) under various conditions on \(a_{1}, \ldots , a_{k}\). Although the result above can also be deduced from known results (see for example [[9][43], [16][44]]), the explicit form with exact values of coefficients is very useful in what follows.

Having the explicit form of the \(P_{A}(2an+i), i\in \{0,\ldots , 2a-1\}, A=\{1,2,a\}\) one can obtain certain results concerning polynomial values taken by the partition function \(P_{A}(n), n\in \mathbb {N}_{+}\). We start with the following simple

### Corollary 4.2

Let \(a\in \mathbb {N}_{\ge 3}\) and put \(A=\{1, 2, a\}\).

1. (1)

If \(a\equiv 0\pmod {2}\), then \(P_{A}(2n)=P_{A}(2n+1)\) for each \(n\in \mathbb {N}\).

2. (2)

If \(a\equiv 1\pmod {2}\), then

$$\begin{aligned} P_{A}(n)=P_{A}(n+1)\;\Longleftrightarrow \; n=2j, j\in \left\{ 1,\ldots ,\frac{a-3}{2}\right\} . \end{aligned}$$

### Proof

(1) Let us put \(a=2c, c\in \mathbb {N}_{\ge 2}\). The statement is an immediate consequence of the first formula from Theorem [4.1][45]. Indeed, for each \(i\in \{0,\ldots , 2c-1\}\) and \(m\in \mathbb {N}\) we have the equality

$$\begin{aligned} P_{A}(4c m+2i)=P_{A}(4c m+2i+1). \end{aligned}$$

Because of the equality \(\{4cn+2i:\;n\in \mathbb {N},\;i\in \{0,\ldots , 2c-1\}\}=2\mathbb {N}\) (the set of even non-negative integers) we get the result.

(2) Let us put \(a=2c+1, c\in \mathbb {N}_{+}\). Because \(\{2(2c+1)n+i:\;n\in \mathbb {N},\;i\in \{0,\ldots , 4c+1\}\}=\mathbb {N}\) to get the solutions of \(P_{A}(n)=P_{A}(n+1)\) it is enough to consider the solutions (in \(m\in \mathbb {N}\)) of equations \(P_{A}(2(2c+1)m+2i)=P_{A}(2(2c+1)m+2i+1)\) or \(P_{A}(2(2c+1)m+2i+1)=P_{A}(2(2c+1)m+2i+2)\). We consider the former equation first. If \(i<c\) then we deal with the equation

$$\begin{aligned} (2c+1)m^2+(c+2i+2)m+i+1=(2c+1)m^2+(c+2i+3)m+i+1, \end{aligned}$$

i.e., \(m=0\) and \(n=2i\) for \(i=0,\ldots , c-1=\frac{a-3}{2}\). If \(i=c\) then we work with the equation

$$\begin{aligned} (2c+1)m^2+(c+2i+2)m+i+1=(2c+1)m^2+(c+2i+3)m+2i+2-c, \end{aligned}$$

i.e., \(m=-1\) and we do not get any new solution.

The same analysis can be applied to the equation \(P_{A}(2(2c+1)m+2i+1)=P_{A}(2(2c+1)m+2i+2)\) and we easily get that it has no solutions in \(\mathbb {N}\). We omit the simple details. \(\square \)

### Theorem 4.3

Let \(a\in \mathbb {N}_{\ge 3}\) and put \(A=\{1,2, a\}\).

1. (1)

If \(a\not \equiv 2\pmod {4}\) then the Diophantine equation \(P_{A}(m)=P_{4}(n)\) has infinitely many solutions in positive integers.

2. (2)

If \(a\equiv 2\pmod {4}\) then the Diophantine equation \(P_{A}(m)=P_{4}(n)\) has only finitely many solutions in integers.

### Proof

The general strategy of the proof is the following. The set of integer solutions of the equation \(P_{A}(m)=P_{4}(n)\) is the sum of sets \(U_{i,j}, i\in \{0,\ldots , 2a-1\}, j\in \{0,\ldots , 11\}\), where

$$\begin{aligned} U_{i,j}=\{(2am+i,12n+j):\;P_{A}(2am+i)=P_{4}(12n+j),\;m, n\in \mathbb {N}\}. \end{aligned}$$

Thus, in order to show that the Diophantine equation \(P_{A}(x)=P_{4}(y)\) has infinitely many solutions it is enough to prove that for some \(i\in \{0,\ldots , 2a-1\}, j\in \{0,\ldots , 11\}\) the set \(U_{i,j}\) is infinite. However, because \({\text {deg}}P_{A}(2am+i)\) has degree 2 and \({\text {deg}}P_{4}(12n+j)=3\), the set \(U_{i,j}\) is infinite if and only if the discriminant (with respect to the variable *m*) of the polynomial

$$\begin{aligned} F_{i,j,a}(m,n)=P_{A}(2am+i)-P_{4}(12n+j) \end{aligned}$$

is a square. Here, we treat *i*, *j*and \(n\in \mathbb {N}\) as variables. Moreover, because \(P_{4}(12n+j)\) is o degree three, then the discriminant

$$\begin{aligned} G_{i,j,a}(n)= {\text {Disc}}_{m}(F_{i,j,a}(m,n)) \end{aligned}$$

is a polynomial of degree three in the variable *n*. Thus, the value of \(G_{i,j,a}(n)\) is square for infinitely many values of \(n\in \mathbb {N}\) if and only if \(G_{i,j,a}\), treated as a polynomial in the variable *n*, has double root. This, in turn, is equivalent with the vanishing of the discriminant of \(G_{i,j,a}\). Summing up we get the following implication

$$\begin{aligned} U_{i,j,a}\;\text{ is } \text{ infinite }\;\Longrightarrow \;H_{i,j,a}:={\text {Disc}}_{n}({\text {Disc}}_{m}(F_{i,j,a}(m,n)))=0. \end{aligned}$$

From our discussion it follows that we need to investigate the vanishing of \(H_{i,j,a}\). However, before we will go one, let us note that a priori \(U_{i,j,a}\) can be finite and the condition \(H_{i,j,a}=0\) can be still satisfied (in other words we can not expect to have equivalence between the conditions above). This is clear. Due to the form of the polynomial \(F_{i,j,a}\) to get an element of \(U_{i,j,a}\) some additional congruence conditions need to be satisfied (which are not seen in discriminant computations). Indeed, let us take \(a=9, i=0, j=3\), i.e.,

$$\begin{aligned} F_{0,3,9}(m,n)=9 m^2+6 m-(12 n^3-24 n^2-15 n-2). \end{aligned}$$

Then \(G_{0,3,9}(n)=108(n+1)(2 n+1)^2\). Thus \(G_{0,3,9}(n)\) is a square if and only if \(n=3u^2-1\). However, \(F_{0,3,9}(m,3u^2-1)=(3m-18u^3+3u+1)(3m+18u^3-3u+1)\) and it is clear that our equation has no solutions.

After this discussion let us back to the proof of the statement.

To get the first part of our theorem we perform case by case analysis. If \(a\equiv 0\pmod {4}\), say \(a=4s\), then \(H_{2s-2, 3, 4s}=0\) and we have that

$$\begin{aligned} G_{2s-2,3,4s}(n)=48(n+1)(2n+1)^2s. \end{aligned}$$

Thus, in order to make the above expression a square, we need to take \(n=3su^2-1\). Then

$$\begin{aligned} F_{2s-2,3,4s}(m, 3su^2-1)=s(-2 m+18 s u^3-3 u-1)(2 m+18 s u^3-3 u+1) \end{aligned}$$

and \(m=\frac{1}{2} \left( 18 s u^3-3 u-1\right) \). Summing up: if *u*is odd positive integer then the numbers

$$\begin{aligned} x&=8sm+2s-2=2 \left( 36 s^2 u^3-6 s u-s-1\right) ,\\ y&=12n+3=9 \left( 4 s u^2-1\right) \end{aligned}$$

solve the equation \(P_{A}(x)=P_{4}(y)\).

Because in the case \(a\equiv 1, 3\pmod {4}\) the reasoning goes in exactly the same way we present only the appropriate values of *i*, *j*and the corresponding solutions *x*, *y*.

If \(a\equiv 1\pmod {4}\), i.e., \(a=4s+1\) then we take \(i=2s-1, j=2\) and *u*positive odd number and get

$$\begin{aligned} x&=\frac{1}{2}(9(4s+1)^2u^3-3(4s+1)u-4(s+1)),\\ y&=(9s+4)u^2-7, \end{aligned}$$

positive integers solving the equation \(P_{A}(x)=P_{4}(y)\).

If \(a\equiv 3\pmod {4}\), i.e., \(a=4s+3\) then we take \(i=s+1, j=0\) and *u*positive odd number and get

$$\begin{aligned} x&=\frac{1}{2}(9(4s+3)^2u^3+(4s+3)u-2(2s+3)),\\ y&=3((4s+3)u^2-1), \end{aligned}$$

positive integers solving the equation \(P_{A}(x)=P_{4}(y)\).

To get the second part of our theorem we need to investigate the vanishing of \(H_{i,j,4s+2}\). Because we have exact expression for \(P_{A}(4(2s+1)m+2i)\) (which is equal to \(P_{A}(4(2s+1)m+2i)\)) it is enough to consider \(H_{i,j,4s+2}\) for \(j=0, \ldots , 11\) as a polynomial in two variables: *s*and *i*. Because we need to consider two cases \(i\in \{0,\ldots , 2s\}\) and \(i\in \{2s+1,\ldots , 4s-1\}\) we work with 24 polynomials \(H_{i,j,4s+2}\). It is easy compute these polynomials. Each has the form

$$\begin{aligned} C(i,j)(2s+1)^2Q_{j}(i,s)R_{j}(i,s), \end{aligned}$$

where \(C(i,j)\in \mathbb {Z}\) and \(Q_{j}, R_{j}\) are quadratic inhomogeneous polynomials. In each case the quadratic forms \(Q_{j}, R_{j}\) has no integer zeros. Because in each case the reasoning is the same we present only one typical example. So let us suppose that \(i\in \{0,\ldots , 2s\}\) and take \(j=0\). Then

$$\begin{aligned} H_{i,0,4s+2}= & {} -27648(2s+1)^2(4(i^2+s^2)-4i(2 s-1)+3)(36(i^2+s^2)\\&-36 i (2s-1)-4 s+25) \end{aligned}$$

and quick computation reveals that each factor is non-zero for \(s\in \mathbb {Z}\) and \(i\in \mathbb {N}\). Performing the same analysis for the rest of polynomials we get the statement of our theorem. \(\square \)

The first part of the above result can be further generalized. In order to get the generalization we will need the following simple

### Theorem 4.4

Let \(a\in \mathbb {N}_{\ge 3}\) and put \(A=\{1, 2, a\}\). The Diophantine equation \(y^2=P_{A}(x)\) has infinitely many solutions in positive integers.

### Proof

First we consider the case *a*is not a square.

Let *a*be even, i.e., \(a=2c\) for some *c*. Take \(i=0\) in the first formula in Theorem [4.1][45], i.e., we work with the Diophantine equation

$$\begin{aligned} P_{A}(4cn)=2cn^2+(c+2)n+1=y^2. \end{aligned}$$

In order to show that the equation \(P_{A}(4cn)=y^2\) has infinitely many integral solutions, we will follow the standard argument to parameterize (rational) solutions since we know that \((n,y)=(0,1)\) solves the equation. The lines through (0, 1) can be written as \(y=mn+1.\) Therefore we get that \(2cn^2+(c+2)n+1=\left( mn+1\right) ^2,\) that is \(n=0\) or

$$\begin{aligned} n=\frac{c+2-2m}{m^2-2c}. \end{aligned}$$

Here \(m=u/v\) is a rational parameter, so we have that

$$\begin{aligned} n=\frac{(c+2)v^2-2uv}{u^2-2cv^2}. \end{aligned}$$

For our assumption, \(a=2c\) is not a square, then we consider the Pell-equation \(u^2-2cv^2=1\) and denote the sequence of positive integer solutions by \((u_k,v_k).\) In this case it follows that \(n=(c+2)v_k^2-2u_kv_k\) and \(y=(c+2)u_kv_k-2u_k^2.\)

Let us now consider the case with \(a=2c+1\) odd. Applying the second formula in Theorem [4.1][45] with \(i=0\), we work with the Diophantine equation

$$\begin{aligned} P_{A}(2(2c+1)n)=(2c+1)n^2+(c+2)n+1=y^2. \end{aligned}$$

Again, in order to show that the equation \(P_{A}(4cn)=y^2\) has infinitely many integral solutions, we follow the standard argument. The pair \((n,y)=(0,1)\) solves the equation. The lines through (0, 1) can be written as \(y=mn+1.\) Therefore, we get that \((2c+1)n^2+(c+2)n+1=\left( mn+1\right) ^2,\) that is \(n=0\) or

$$\begin{aligned} n=\frac{c+2-2m}{m^2-2c-1}. \end{aligned}$$

Here \(m=u/v\) is a rational parameter, so we have that

$$\begin{aligned} n=\frac{(c+2)v^2-2uv}{u^2-(2c+1)v^2}. \end{aligned}$$

For our assumption, \(a=2c+1\) is not a square, then we consider the Pell-equation \(u^2-(2c+1)v^2=1\) and denote the sequence of positive integer solutions by \((u_k,v_k).\) In this case it follows that \(n=(c+2)v_k^2-2u_kv_k\) and \(y=(c+2)u_kv_k-2u_k^2\).

Summing up: we proved that if *a*is not a square then the Diophantine equation \(y^2=P_{A}(x)\) has infinitely many solutions in positive integers.

It remains to deal with the case when *a*is a square (even or odd). We follow similar lines, so we only provide details in case of \(a=4t^2\), that is when *a*is an even square. Again, using the first formula from Theorem [4.1][45] with \(c=2t^2, i=2t^2-2<c-1\) we get that

$$\begin{aligned} P_{A}(8t^2n+2t^2-2)=4t^2n^2+4t^2n+t^2=t^2(2n+1)^2, \end{aligned}$$

and for each \(n\in \mathbb {N}_{+}\) the number \(P_{A}(8t^2n+2t^2-2)\) is a square and the Diophantine equation \(y^2=P_{A}(x)\) has infinitely many solutions in positive integers.

If \(a=(2t+1)^2\) is an odd square, then using the second formula from Theorem [4.1][45] with \(c=2t(2t+1)\) and \(i=2t^2-2\) we find that

$$\begin{aligned} P_{A}(2(2t+1)^2n+2t^2-2)=((2t+1)n+t)^2. \end{aligned}$$

For each \(n\in \mathbb {N}\) the number \(P_{A}(2(2t+1)^2n+2t^2-2)\) is a square and our theorem is proved. \(\square \)

### Theorem 4.5

Let \(a, b\in \mathbb {N}_{\ge 3}, a<b\) such that *a*, *b*are divisible by 4 and either *a*/2 or *b*/2 is not a square. Put \(A=\{1, 2, a\}, B=\{1, 2, b\}\). The Diophantine equation \(P_{A}(x)=P_{B}(y)\) has infinitely many solutions in positive integers.

### Proof

Let \(a=2s\) and \(b=2t.\) It follows from Theorem [4.1][45] that

$$\begin{aligned} P_A(4sn)= & {} 2sn^2+(s+2)n+1,\\ P_B(4tm)= & {} 2tm^2+(t+2)m+1. \end{aligned}$$

Suppose that \(a/2=s\) is not a square. We have the solution (0, 0) of the equation \(P_A(4sn)=P_B(4tm)\) so we write \(n=km\) for some rational number \(k=u/v.\) Solving the equation for *m*provides that either \(m=0\) or

$$\begin{aligned} m=\frac{(t+2)v^2-suv-2uv}{2su^2-2v^2}. \end{aligned}$$

Since *s*and *t*are even integers the numerator is divisible by 2 and we obtain the expression

$$\begin{aligned} m=\frac{(s+2)/2uv-(t+2)/2v^2}{v^2-su^2}. \end{aligned}$$

The integer *s*is not a square, hence we consider the sequence of positive solutions \((u_k,v_k)\) of the Pell-equation \(v^2-su^2=1.\) For these solutions we have \(m=(s+2)/2u_kv_k-(t+2)/2v_k^2\) and \(n=(s+2)/2u_k^2-(t+2)/2u_kv_k.\) \(\square \)

In view of theorem above we formulate the following conjecture.

### Conjecture 4.6

Let \(a, b\in \mathbb {N}_{\ge 3}, a<b\) and put \(A=\{1, 2, a\}, B=\{1, 2, b\}\). The Diophantine equation \(P_{A}(x)=P_{B}(y)\) has infinitely many solutions in positive integers.

Let us note that to prove the above conjecture it is enough to find a pair (*i*, *j*) of integers such that \(i\in \{0,\ldots , 2a-1\}, j\in \{0,\ldots , 2b-1\}\) and the Diophantine equation \(P_{A}(2ax+i)=P_{B}(2by+j)\) has infinitely many solutions in integers. Although for any fixed values of *a*, *b*it is easy to find suitable *i*, *j*we were unable to get the general result.

## 5 Remarks on the Diophantine equation \(y^2=P_{A}(x)\)

A difficult and still unsolved question is whether the number *p*(*n*) can be a perfect power. Let us recall that *p*(*n*) counts the number of all partitions of *n*, i.e.,

$$\begin{aligned} \prod _{n=1}^{\infty }\frac{1}{1-x^{n}}=\sum _{n=0}^{\infty }p(n)x^{n}. \end{aligned}$$

In other words, we do not know any example of \(n\ge 2\) such that \(y^k=p(n)\) for some \(k\in \mathbb {N}_{\ge 2}\). In fact Zhi-Wei Sun conjectured that the equation \(y^{k}=p(n)\) has no solutions in positive integers *n*, *y*, *k*with \(k\ge 2\). Let us also note that Alekseyev checked that there are no solutions with \(n\le 10^{8}\) [[20][46]].

A question arises whether some results concerning the equation \(y^2=P_{k}(x)\) can be proved for some values of \(k\in \mathbb {N}_{+}\). We know that the Diophantine equation \(y^2=P_{k}(x)\) has infinitely many solutions in positive integers for \(k\le 4\). Indeed, to get the result for \(k=3\) it is enough to back to the explicit form of \(P_{3}(6n+i)\) presented in the proof of Theorem [3.1][29]. It is easy to see that for \(i\in \{0, 1, 4, 5\}\) the Diophantine equation

$$\begin{aligned} y^2=P_{3}(6n+i) \end{aligned}$$

has infinitely many solutions in positive integer. For example, if \(i=4\) we deal with the equation \(y^2=(n+1)(3n+4)\). Thus, if \((u_{k}, v_{k})\) is a solution of the Pell equation \(v^2-3u^2=1\) then the pair \((n, y)=(u_{k}^2-1, u_{k}v_{k})\) solves our equation.

If \(k=4\) then again we back to the explicit form of \(P_{4}(6n+2i+1)\) for \(i=0, 1, 2\) and \(P_{4}(12n+2i)\) for \(i=0, 1, \ldots , 5\). A quick inspection reveals that the equation \(y^2=P_{4}(6n+2i+1)\) has infinitely many solutions for \(i=1, 2\). For example, if \(i=1\) then it is enough to take \(n=6u^2-2\) and \(y=3u(6u^2-1)\). Similarly, it is easy to see that equation \(y^2=P_{4}(12n+2i)\) has infinitely many solutions for \(i=3, 4\).

The first non-trivial problem is characterization of the positive integer solutions of the Diophantine equation \(y^2=P_{5}(x)\). We prove the following

### Theorem 5.1

The equation \(y^2=P_{5}(x)\) has only finitely many solutions in positive integers. More precisely, the pair (*x*, *y*) is a solution if and only if \((x,y)=(1,1), (2027, 77129)\).

### Proof

We have 60 curves of the form \(y^2=P_{5}(60n+i), i\in \{0,\ldots , 59\}\). If \(i\in \{5, 20, 25, 40\}\) the corresponding quartic has no \({\mathbb {Q}}_{5}\) -rational points, and thus has no rational points at all.

Similarly as in the proof of Theorems [3.1][29] and [3.2][30], we apply the procedure IntegralQuarticPoints() to determine all integral solutions in the remaining 56 cases. In particular, the solution (1, 1) comes from the equation \(y^2=P_{5}(60n+1)\) with \(n=0\). The solution (2027, 77129) comes from the solution \((n,y)=(33, 77129)\) of the equation \(y^2=P_{5}(60n+47)\). The procedure works well, except in 6 special cases. Here we do not get any error message like in the special cases appearing in the proof of Theorem [3.2][30], but warnings about time-consuming final enumerations. The 6 problematic polynomials correspond to \(i\in \{21, 24, 48, 51, 54, 57\}\). The equations (up to multiplication by 16) corresponding to \(i=21, 24\) give the following equations

$$\begin{aligned} 5y^2= & {} u(36u^3+108u^2+34u+12),\quad u=5(2n+1),\\ 5y^2= & {} u(36u^3-108u^2+34u-12),\quad u=2(5n+3), \end{aligned}$$

respectively. Hence we need to resolve the following elliptic equations

$$\begin{aligned} Y^2=X^3+108\delta X^2+3384\delta ^2X+15552\delta ^3, \end{aligned}$$

where \(\delta \) divides 60. We only get the trivial solution given by \(u=0\).

For \(i\in \{48, 51, 54, 57\}\) after the substitution \(u=2(n+1)\) we get the following quartic equations

$$\begin{aligned} y^2= & {} u(4500u^3-2700u^2+470u-12),\\ y^2= & {} u(4500u^3-900u^2-70u+4),\\ y^2= & {} u(4500u^3+900u^2-70u-4),\\ y^2= & {} u(4500u^3+2700u^2+470u+12). \end{aligned}$$

We obtain elliptic equations in a similar way as before, so we omit details. It turns out that we get only the trivial solution with \(u=0\) from these cases. \(\square \)

The case of the equation \(y^2=P_{6}(x)\) is far more difficult. To get the solutions we need to consider 60 genus 2 curves

$$\begin{aligned} C_{i}:\;y^2=P_{6}(60n+i),\quad i=0, \ldots , 59. \end{aligned}$$

Let \(J_{i}={\text {Jac}}(C_{i})\) be the Jacobian of the curve \(C_{i}\) and by \(r_{i}\) denote the rank of \(J_{i}\). We checked that \(r_{i}\le 5\) for \(0\le i\le 59\).

#### Table. Upper bounds for the \(\mathbb {Q}\) -rank of the Jacobian \(J_{i}\) of the curve \(C_{i}:\;y^2=P_{6}(60x+i)\) for \(i=0, \ldots , 59\).

*r*

 |

\(\text{ values } \text{ of }\;i\;\text{ such } \text{ that }\;r_{i}\le r\)

 |

0

 |

3, 14, 34, 47, 50, 51, 55, 59

 |

1

 |

18, 22, 27, 32, 35, 38, 41, 43, 44, 45, 46, 54

 |

2

 |

0, 7, 8, 9, 15, 23, 24, 25, 26, 28, 29, 30, 33, 36, 37, 39, 40, 42, 49, 52, 53, 57, 58

 |

3

 |

2, 5, 6, 11, 17, 31, 48

 |

4

 |

4, 10, 13, 16, 19, 20, 21, 56

 |

5

 |

1, 12

 |

It is curious that the polynomial \(P_{6}(60n+i)\) is reducible (in the ring \(\mathbb {Q}[n]\)) for \(i\in \{40,\ldots , 59\}\) and thus, instead of working with genus two curve we need to play with certain curves of the type \(y^2=Q_{i}(x)\), where \(Q_{i}\) is a quartic polynomial.

If the rank of the Mordell-Weil group is less than the genus of the curve, that is 2 in these cases, then classical Chabauty’s method [[6][47]] may be applied to determine all rational points on the hyperelliptic curves. If the rank is greater than or equal to 2, then there are two different approaches to compute the set of integral points on the curves (see [[4][48], [10][49]]). The difficulty is that one needs a Mordell-Weil basis. Among the above curves there are some for which we were not able to obtain such bases, these are as follows \(C_i\) with

$$\begin{aligned} i\in \{15,16,23,24,27,28,29,31,32,33,35,36,38,39 \}. \end{aligned}$$

The most interesting one may be the hyperelliptic curve given by

$$\begin{aligned} y^2=12x^5 + 1125x^4 + 41960x^3 + 778050x^2 + 7171020x + 26276400, \end{aligned}$$

which, as computed with the help of Magma, is the minimal model of the curve \(C_{27}:~~y^2=P_6(60n+27).\) In this case the rank is 1, however we were unable to found a generator of the Mordell-Weil group.

We finish with the following

### Conjecture 5.2

Let \(n\in \mathbb {N}_{\ge 6}\). The only positive integer solution of the Diophantine equation \(y^2=P_{n}(x)\) is \(x=y=1\).

Motivated by the results above one can ask a more general

### Question 5.3

Let \(A\subset \mathbb {N}_{+}\) and suppose that the Diophantine equation \(y^2=P_{A}(x)\). How large the number \(\#A\) can be?

In case of \(\#A=5\) there is a large number of sets such that \(P_{A}(L_{A}n+i)\) is a square of a polynomial in *n*. More precisely, with the constraint \({\text {max}}(A)\le 15\), there are exactly 119 different pairs (*A*, *i*) such that \(P_{A}(L_{A}n+i)\) is a square of a polynomial with integer coefficients. For example, if \(A=\{1, 2, 8, 10, 15\}\), then \(L_{A}=120\) and for \(i=1, 11, 41, 43, 73, 83, 91, 113\) we have \(P_{A}(L_{A}n+i)\) is a square of a polynomial. In particular,

$$\begin{aligned} P_{A}(120n+1)=(4n+1)^2(15n+1)^2. \end{aligned}$$

In the table below we collect data concerning our search.

#### Table. The sets *A*such that \(\#A=5, {\text {max}}(A)\le 15\) and there is an \(i\in \{0,\ldots , L_{A}-1\}\) such that \(P_{A}(L_{A}n+i)\) is a square of a polynomial in \(\mathbb {Z}[n]\)

*A*

 |

\(L_{A}\)

 |

*i*

 |

{1,2,8,10,15}

 |

120

 |

1,11,41,43,73,83,91,113

 |

{1,4,5,10,12}

 |

60

 |

12,16,36,52

 |

{1,4,8,9,12}

 |

72

 |

1,13,19,25,37,43,49,61,67

 |

{1,5,6,8,10}

 |

120

 |

2,8,13,17,32,37,53,58,73, 77,82,88,97,98,112,113

 |

{2,3,7,8,14}

 |

168

 |

32,102,144,158

 |

{2,4,5,6,10}

 |

60

 |

12,16,17,21,36,41,52,57

 |

{3,4,6,9,12}

 |

36

 |

3,7,11,27,31,35

 |

{3,5,6,9,15}

 |

90

 |

18,23,24,28,29,34,54,59,64,78,83,88

 |

{4,5,6,12,15}

 |

60

 |

27,51

 |

{4,7,9,12,14}

 |

252

 |

58,64,142,148,226,232

 |

{5,6,8,9,10}

 |

360

 |

8,29,53,74,89,98,104,113,128,149,173,194,209,

 |

 |  |

218,224,233,248,269,293,314,329,338, 344,353

 |

{5,7,9,14,15}

 |

630

 |

47,113,173,197,257,323,383,407,467,533,593,617

 |

{7,8,10,14,15}

 |

840

 |

182,212,364,422,574,604,812,814

 |

In case of \(\#A=6\) there is a large number of sets such that \(P_{A}(L_{A}n+i)\) is a square of a polynomial (with rational coefficients) in *n*times a linear factor (note that this is only possibility to get infinitely many square values). However, in each case the values of a corresponding linear factor nor the value of \(P_{A}(L_{A}n+i)\) can be a square of an integer.

We were able to find only the one set *A*with 7 elements, \({\text {max}}(A)\le 10\) and such that \(y^2=P_{A}(x)\) has infinitely many solutions in positive integers. More precisely, if \(A=\{1,2,4,5,8,9,10\}\) then

$$\begin{aligned} P_{A}(360n+95)&=25(3n+1)^2(18n+5)^2(36n+13)(40n+13),\\ P_{A}(360n+226)&=25(3n+2)^2(18n+13)^2(36n+23)(40n+27). \end{aligned}$$

One can easily check that the factor \((36n+13)(40n+13)\) is a square infinitely often. The smallest values of *n*which makes this factor a square, are \(n=0, 494, 712842, \ldots \). However, the factor \((36n+23)(40n+27)\) takes square values for infinitely many values negative values of *n*and thus is not of interests for us.

## 6 Problems, questions and conjectures

Besides the conjectures stated in previous sections, we formulate now several question and conjectures which hopefully will stimulate further research.

### Question 6.1

Let \(k\in \mathbb {N}_{\ge 2}\) and \(f\in \mathbb {Z}[x]\) be given. Does there exist an ascending sequence of sets \(A_{2}=\{a_{1}, a_{2}\}\subset \ldots \subset A_{k}=\{a_{1},\ldots , a_{k}\}\ldots \subset \mathbb {N}_{+}\) such that the Diophantine equation \(P_{A_{k}}(x)=f(y)\) has at least \(C_{k,f}\) solutions in positive integers and \(C_{k,f}\rightarrow +\infty \) as \(k\rightarrow +\infty \)?

Let us observe that without the condition \(C_{k,f}\rightarrow +\infty \) the question is not difficult. Indeed, let us take \(A_{2}=\{a_{1}, a_{2}\}\subset \mathbb {N}_{+}\) and suppose that \(\gcd (a_{1},a_{2})=1\). As we already proved in Theorem [2.1][27] the Diophantine equation \(P_{A_{2}}(x)=f(y)\) has infinitely many solutions in positive integers. If \(C\in \mathbb {N}\) is fixed let us take an increasing sequence \(\{a_{3}, a_{4},\ldots , a_{k}\}\) of positive integers such that \(a_{3}\) is grater then the smallest integer *N*such that there is at least *C*values of *x*for which there is an integer *y*satisfying \(P_{A_{2}}(x)=f(y)\). Then, for \(A_{k}=\{a_{1}, a_{2}, a_{3},\ldots , a_{k}\}\) the Diophantine equation

$$\begin{aligned} P_{A_{k}}(x)=f(y) \end{aligned}$$

has at least *C*solutions in positive integers. Indeed, this is simple consequence of the recurrence relation satisfied by the sequence \(\{P_{A_{k}}(n)\}_{n\in \mathbb {N}}\). Indeed, because \(P_{A_{k}}(n)=P_{A_{k-1}}(n)\) for \(n<a_{k}\), then \(P_{A_{k}}(n)=P_{A_{2}}(n)\) for \(n<\min \{a_{3},\ldots , a_{k}\}=a_{3}\) and hence the result.

We proved that the equation \(P_{3}(x)=P_{5}(x)\) has only finitely many solutions in positive integers and it is quite natural to ask whether there are *A*, *B*satisfying \(\#A=3, \#B=5\), such that the equation \(P_{A}(x)=P_{B}(y)\) has infinitely many solutions in positive integers. To get the result in this direction we will need the following.

### Lemma 6.2

Let \(b\in \mathbb {N}_{\ge 4}\) and put \(B=\{1, 2, 3, 4, b\}\).

1. (1)

If \(b=4(6k+1), j=3(8k-1)\) for some \(k\in \mathbb {N}_{+}\), then \(P_{B}(3bn+j)=(3n+2)((6k+1)n+2k)Q_{1}(k,n)\), where

$$\begin{aligned} Q_{1}(k,n)=3(6k+1)^2n^2+2(9k+1)(6k+1)n+6k(4k+1). \end{aligned}$$

2. (2)

If \(b=4(6k+5), j=24k+13\) for some \(k\in \mathbb {N}_{+}\), then \(P_{B}(3bn+j)=(3n+1)((6k+5)n+4k+3)Q_{2}(k,n)\), where

$$\begin{aligned} Q_{2}(k,n)=3(6k+5)^2n^2+2(6k+5)(9k+7)n+24k^2+36k+1). \end{aligned}$$

3. (3)

If \(b=4(12k+2), j=48k+1\) for some \(k\in \mathbb {N}_{+}\), then \(P_{B}(3bn+j)=(3n+1)(2(6k+1)n+8k+1)Q_{3}(k,n)\), where

$$\begin{aligned} Q_{3}(k,n)=12(6k+1)^2n^2+2(6k+1)(36k+5)n+96k^2+24k+1. \end{aligned}$$

4. (4)

If \(b=4(12k+10), j=48k+1\) for some \(k\in \mathbb {N}_{+}\), then \(P_{B}(3bn+j)=(3n+2)(2(6k+5)n+4k+3)Q_{4}(k,n)\), where

$$\begin{aligned} Q_{4}(k,n)=12(6k+5)^2n^2+2(6k+5)(36k+29)n+3(4k+3)(8k+7). \end{aligned}$$

### Proof

Let us note that the sequence \(\{P_{B}(n)\}_{n\in \mathbb {N}}\) satisfies the following recurrence relation

$$\begin{aligned} P_{B}(n)={\left\{ \begin{array}{ll}\begin{array}{ll} P_{A}(n), &{} n<b, \\ P_{B}(n-b)+P_{A}(n), &{} b\le n, \end{array} \end{array}\right. } \end{aligned}$$

where \(A=\{1, 2, 3, 4\}\). We know the polynomial expressions for \(P_{A}(12n+i), i\in \{0,\ldots , 11\}\) and that \(P_{B}(L_{b}n+j), j\in \{0,\ldots , L_{b}-1\}\), where \(L_{b}={\text {LCM}}(1,2,3,4,b)\), is a polynomial of degree 4 with rational coefficients. Using induction one can obtain the expression for the polynomials of interests. We omit tiresome details. \(\square \)

### Theorem 6.3

Let \(a\in \mathbb {N}_{\ge 3}, b\in \mathbb {N}_{\ge 4}\) and put \(A=\{1, 2, a\}, B=\{1, 2, 3, 4, b\}\). If \(a\equiv 1, 2, 5, 7, 11, 10\pmod {12}\) and \(b=4a\), then the Diophantine equation \(P_{A}(x)=P_{B}(y)\) has infinitely many solutions in positive integers.

### Proof

Note that if \(a\equiv 1, 2, 5, 7, 11, 10\pmod *{12}\), then *a*can be written in one of the following form: \(a=6k+1, a=6k+5, a=12k+2\) \(a=12k+10\). Thus, in each case, the value of \(b=4a\) is exactly the value of *b*considered in Lemma [6.2][50]. Following the idea of proof of Theorem [4.3][32] we present the values of *i*, *j*such that the polynomial \(P_{A}(2am+i)-P_{B}(3bn+j)\) is reducible and the coefficient in of the linear factor (in *m*) near *m*is equal to 1.

Let \(a=6k+1, b=4a, i=11k, j=3(8k-1)\). Then \(P_{A}(2am+i)-P_{B}(3bn+j)=R_{1}(m,n)R_{2}(m,n)\), where

$$\begin{aligned} R_{1}(m,n)&=m-3(6k+5)n^2-2(9k+7)n-4k+1,\\ R_{2}(m,n)&=(6k+1)m+3(6k+1)^2n^2+2(6k+1)(9k+1)n+24k^2+12k+1. \end{aligned}$$

Thus, if \(m=3(6k+5)n^2+2(9k+7)n+4k-1\) then \(P_{A}(2am+i)=P_{B}(3bn+j)\) and our equation has infinitely many solutions.

Because in each case we proceed in the same way we present only the values of *a*, *i*, *b*, *j*and the corresponding solution for *m*.

If \(a=6k+5, i=7k+4, b=4(6k+4), j=24k+13\), then

$$\begin{aligned} m=3(6k+5)n^2+2(9k+7)n+2(2k+1). \end{aligned}$$

If \(a=2(6k+1), i=14k, b=8(6k+1), j=48k+1\), then

$$\begin{aligned} m=6(6k+1)n^2+(36k+5)n+8k. \end{aligned}$$

If \(a=2(6k+5), i=2(11k+8), b=8(6k+5), j=3(16k+11)\), then

$$\begin{aligned} m=6(6k+5)n^2+(36k+29)n+8k+5. \end{aligned}$$

\(\square \)

We proved that for many choices of sequences *A*, *B*, the corresponding Diophantine equation \(P_{A}(x)=P_{B}(y)\) has infinitely many solutions in positive integers. However, in each case under consideration we had \({\text {min}}\{\#A,\#B\}\le 3\). This observation lead us to the following.

### Question 6.4

Let \(A, B\subset \mathbb {N}_{+}\). Let us suppose that the Diophantine equation \(P_{A}(x)=P_{B}(y)\) has infinitely many (non-trivial) solutions in positive integers. How large the number \({\text {min}}\{\#A, \#B\}\) can be?

Let us explain what a trivial solution means. More precisely, if for example \(A=\{1, pa_{2},...,pa_{k}\}\) then if \(P_{A}(pn)\) is a non-zero, then in each representation

$$\begin{aligned} 1\cdot x_{1}+\sum _{i=2}^{k}pa_{i}x_{i}=pn \end{aligned}$$

we need to have \(p|x_{1}\) and thus we get a representation

$$\begin{aligned} 1\cdot y_{1}+\sum _{i=2}^{k}a_{i}x_{i}=n. \end{aligned}$$

It is clear that this mapping can be reversed. Thus, by taking \(B=\{1, a_{2}, ..., a_{k}\}\) we have the boring identity \(P_{A}(pn)=P_{B}(n)\).

Thus, in regards to question above, we considered equations of the form \(P_A(x)=P_B(y),\) where *A*, *B*are sets having 5 elements from \(\{1,2,\ldots ,10\}\) and one of the elements is 1. We searched for reducible polynomials \(P_A(x)-P_B(y)\) having a linear or quadratic factor. We implemented a parallel algorithm and used SageMath on a machine having 16 cores. It took about 10 hours to determine the appropriate polynomials. There are 44982 such cases. Among these polynomials we looked for examples providing infinitely many integral solutions. To reduce the time of computation a timeout was set to be 60 seconds. There are 392 cases for which the 60 seconds were not sufficient to compute the result. There are 2338 quadratic equations that yield infinitely many integral solutions and 2100 linear equations that provide parametric solutions. However, even in the case of reducibility we sometimes get factors without positive integer solutions. We present several examples.

Let \(A=\{1,2,4,5,6\}\) and \(B=\{1,4,6,9,10\}.\) Here we obtain that \(P_A(60m+22)-P_B(180n+111)\) is, up to a constant factor, equal to \(f_{1}(m,n)f_{2}(m,n)\), where

$$\begin{aligned} f_{1}(m,n)= & {} 150m^2 + 450n^2 + 155m + 630n + 259,\\ f_{2}(m,n)= & {} 30m^2 - 90n^2 + 31m - 126n - 36. \end{aligned}$$

The equation \(f_{1}(m,n)=0\) has no solution modulo 5. The equation \(f_{2}(m,n)=0\) has infinitely many integral solutions. However, all are negative and are not of interest for us.

As a second example consider \(A=\{1,2,4,6,10\}\) and \(B=\{1,2,5,6,8\}.\) We get that \(P_A(60m+17)-P_B(120n+17)\) is, up to a constant factor, equal to \(g_{1}(m,n)g_{2}(m,n)g_{3}(m,n)\), where

$$\begin{aligned} g_{1}(m,n)= & {} m-2n\\ g_{2}(m,n)= & {} 15m + 30n + 14,\\ g_{3}(m,n)= & {} 75m^2 + 300n^2 + 70m + 140n + 31. \end{aligned}$$

We obtain infinitely many integral solutions from the equation \(g_{1}(m,n)=0\) (however, these are trivial solutions). The other two equations have no solutions modulo 5.

As a third example let \(A=\{1,2,3,4,6\},B=\{1,2,4,5,10\}.\) It follows that \(P_A(12m+1)-P_B(20n+1)=1/6h_{1}(m,n)h_{2}(m,n)\), where

$$\begin{aligned} h_{1}(m,n)= & {} 6m^2 + 10n^2 + 9m + 12n + 5\\ h_{2}(m,n)= & {} 6m^2 - 10n^2+ 9m - 12n. \end{aligned}$$

The equation \(h_{1}(m,n)=0\) can be written as

$$\begin{aligned} 15(36m+27)^2+(180n+108)^2=6399, \end{aligned}$$

and it follows that the only integral solution is given by \((m,n)=(-1,-1).\) The equation \(h_{2}(m,n)=0\) has infinitely many positive integral solutions, the two smallest being \((m,n)=(2928,2268), (11252256,8715960)\).

For given \(A\in \mathbb {N}_{+}\) the function \(P_{A}(n)\) has a dual nature: from one side it is a quasi-polynomial and hance an algebraic object. On the other side \(P_{A}(n)\) is counting function and thus live in a realm of combinatorics. In this paper we mainly operated on the former side. Thus, it is natural to state the following general question.

### Proposition 6.5

Let \(A, B\subset \mathbb {N}_{+}\). Does there exist combinatorial conditions on *A*and *B*which guarantees non-existence (or finiteness) of integral solutions of the Diophantine equation \(P_{A}(x)=P_{B}(y)\)?

It is clear that the above problem can be stated in a grater generality. More precisely, we can ask whether there are some combinatorial conditions which guarantee that for not necessarily finite sets \(A_{1}, A_{2}\), and corresponding properties \({\mathcal {W}}_{1}, {\mathcal {W}}_{2}\), the equation \(p_{A_{1}}({\mathcal {W}}_{1},x)=p_{A_{2}}({\mathcal {W}}_{2},y)\) has only finitely many solutions in positive integers.

As we mentioned above, the partition functions count combinatorial objects. Thus, equality between different partition functions at certain integer arguments is equivalent with the statement that certain finite sets have the same number of elements. This suggest the following

### Proposition 6.6

Let \(A, B\subset \mathbb {N}_{+}\) and suppose that the Diophantine equation \(p_{A}(x)=p_{B}(y)\) has infinitely many solutions in integers. Moreover, let \(x=\phi (n), y=\psi (n)\) be parametrization of one (of possibly many) infinite part of the solution set, i.e., \(p_{A}(\phi (n))=p_{B}(\psi (n))\) for each \(n\in \mathbb {N}_{+}\). Describe the bijection (in combinatorial or other way) between the sets \({\text {Part}}(\phi (n))={\text {Part}}(\psi (n))\).

Motivated by our findings presented in Theorem [3.2][30] and related results we formulate the following

### Conjecture 6.7

Let \(m, n\in \mathbb {N}_{+}\). If \((m,n)\ne (3, 4)\) and \(3\le m<n\), then the Diophantine equation \(P_{m}(x)=P_{n}(y)\) has only finitely many solutions in non-negative integers.

### Remark 6.8

Let us note that from the recurrence relation satisfied by the sequence \(\{P_{m}(k)\}_{k\in \mathbb {N}}\), i.e.,

$$\begin{aligned} P_{m}(k)=P_{m-1}(k), k<m, \quad P_{m}(k)=P_{m-1}(k)+P_{m}(k-m),\;k\ge m, \end{aligned}$$

we know that the equation \(P_{m}(x)=P_{n}(y)\) has trivial solutions \(x=y=i, i\le m\). So, it is reasonable to consider the set

$$\begin{aligned} C_{m,n}:=\{(x, y)\in \mathbb {Z}\times \mathbb {Z}:\;P_{m}(x)=P_{n}(y)\wedge y\ge n\}. \end{aligned}$$

We believe that much stronger property is true, i.e.,

$$\begin{aligned} \bigcup _{\min \{m, n\}\ge 3, m<n, (m,n)\ne (3,4)}C_{m,n}(\mathbb {N})<+\infty . \end{aligned}$$

## References

1.

Ahlgren, S., Ono, K.: Congruence properties for the partition function. Proc. Natl. Acad. Sci. USA **98**(23), 12882–12884 (2001)

[Article][51] [MathSciNet][52] [Google Scholar][53]

2.

Andrews, G., Eriksson, K.: Integer Partitions. Cambridge University Press, Cambridge (2004)

[Book][54] [Google Scholar][55]

3.

Andrews, G.: Partition identities. Adv. Math. **9**, 10–51 (1972)

[Article][56] [MathSciNet][57] [Google Scholar][58]

4.

Bugeaud, Y., Mignotte, M., Siksek, S., Stoll, M., Tengely, Sz.: Integral points on hyperelliptic curves. Algebra Number Theory **2**(8), 859–885 (2008)

[Article][59] [MathSciNet][60] [Google Scholar][61]

5.

Castillo, A., Flores, S., Hernandez, A., Kronholm, B., Larsen, A., Martinez, A.: Quasipolynomials and maximal coefficients of Gaussian polynomials. Ann. Comb. **23**(3–4), 589–611 (2019)

[Article][62] [MathSciNet][63] [Google Scholar][64]

6.

Chabauty, C.: Sur les points rationnels des courbes algébriques de genre supérieur à l’unité. C. R. Acad. Sci. Paris **212**, 882–885 (1941)

[MathSciNet][65] [MATH][66] [Google Scholar][67]

7.

Churchhouse, R.F.: Congruence properties of the binary partition function. Proc. Camb. Philos. Soc. **66**, 371–376 (1969)

[Article][68] [MathSciNet][69] [Google Scholar][70]

8.

Bosma, W., Cannon, J., Playoust, C.: The Magma algebra system. I. The user language. J. Symb. Comput. **24**, 235–265 (1997)

[Article][71] [MathSciNet][72] [Google Scholar][73]

9.

Ehrhart, E.: Sur un problème de géométrie diophantienne linéaire, II. Systèmes diophantiens linéaires. J. Reine Angew. Math. **227**, 25–49 (1967)

[MathSciNet][74] [Google Scholar][75]

10.

Gallegos-Ruiz, H.R.: Computing integral points on genus 2 curves estimating hyperelliptic logarithms. Acta Arithm. **187**(4), 329–344 (2019)

[Article][76] [MathSciNet][77] [Google Scholar][78]

11.

Gebel, J., Pethő, A., Zimmer, H.G.: Computing integral points on elliptic curves. Acta Arithm. **68**(2), 171–192 (1994)

[Article][79] [MathSciNet][80] [Google Scholar][81]

12.

Komatsu, T.: On the number of solutions of the Diophantine equation of Frobenius—general case. Math. Commun. **8**(2), 195–206 (2003)

[MathSciNet][82] [MATH][83] [Google Scholar][84]

13.

Nicolas, J.-L., Ruzsa, I.Z., Sárközy, A.: On the parity of additive representation functions (with an appendix by J-P. Serre). J. Number Theory **73**, 292–317 (1998)

[Article][85] [MathSciNet][86] [Google Scholar][87]

14.

Rødseth, Ø.J., Sellers, J.A.: Partitions with parts in a finitie set. Int. J. Number Theory **2**(3), 455–468 (2006)

[Article][88] [MathSciNet][89] [Google Scholar][90]

15.

Sertöz, S.: On the number of solutions of a Diophantine equation of Frobenius. Discret. Math. Appl. **8**, 153–162 (1998)

[Article][91] [MathSciNet][92] [Google Scholar][93]

16.

Sertöz, S., Özlük, A.: On the number of representations of an integer by a linear form. İstanbul Üniv. Fen Fak. Mat. Derg. **50**, 67–77 (1993)

[MathSciNet][94] [MATH][95] [Google Scholar][96]

17.

Stroeker, R.J., Tzanakis, N.: Solving elliptic Diophantine equations by estimating linear forms in elliptic logarithms. Acta Arithm. **67**(2), 177–196 (1994)

[Article][97] [MathSciNet][98] [Google Scholar][99]

18.

Ono, K.: Distribution of the partition function modulo \(m\). Ann. Math. **151**, 1–15 (2000)

[Article][100] [MathSciNet][101] [Google Scholar][102]

19.

Tzanakis, N.: Solving elliptic Diophantine equations by estimating linear forms in elliptic logarithms. The case of quartic equations. Acta Arithm. **75**(2), 165–190 (1996)

[Article][103] [MathSciNet][104] [Google Scholar][105]

20.

Sun, Z.-W.: Can the partition function \(p(n)\) take perfect power values?, URL (version: 2018-11-21). [https://mathoverflow.net/q/315828][106] ( [https://mathoverflow.net/users/124654/zhi-wei-sun][107])

[Download references][108]

## Acknowledgements

The authors are grateful to Nikolaos Tzanakis for his ideas to complete the proof of Theorem [3.2][30]. We are also grateful for an anonymous referee for remarks which led to improving the presentation.

## Author information

### Authors and Affiliations

1.

Mathematical Institute, University of Debrecen, P.O.Box 12, 4010, Debrecen, Hungary

Szabolcs Tengely

2.

Faculty of Mathematics and Computer Science, Institute of Mathematics, Jagiellonian University, Łojasiewicza 6, 30-348, Kraków, Poland

Maciej Ulas

Authors

1. Szabolcs Tengely

[View author publications][109]

Search author on: [PubMed][110] [Google Scholar][111]

2. Maciej Ulas

[View author publications][112]

Search author on: [PubMed][113] [Google Scholar][114]

### Corresponding author

Correspondence to [Maciej Ulas][115].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

The research of the first author was supported in part by the NKFIH Grants 115479, 128088 and130909 and by the Project EFOP-3.6.1-16-2016-00022, co-financed by the European Union and the European Social Fund. Research of the second author was supported by a grant of the National Science Centre (NCN), Poland, No. UMO-2019/34/E/ST1/00094.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][116].

[Reprints and permissions][117]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [118]

### Cite this article

Tengely, S., Ulas, M. Equal values of certain partition functions via Diophantine equations. *Res. number theory***7**, 67 (2021). https://doi.org/10.1007/s40993-021-00293-7

[Download citation][119]

-

Received: 22 February 2021

-

Accepted: 19 September 2021

-

Published: 21 October 2021

-

Version of record: 21 October 2021

-

DOI: https://doi.org/10.1007/s40993-021-00293-7

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Partitions][120]
- [Diophantine equation][121]
- [Polynomial][122]
- [Identities][123]

### Mathematics Subject Classification

- [11D41][124]
- [11P83][125]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s40993-021-00293-7.pdf
[3]: /article/10.1007/s40993-021-00293-7/save-research?_csrf=yX__4AEmzv4p4yD6f_VUjD9XQWdfDD1Y
[4]: /saved-research
[5]: /journal/40993
[6]: /journal/40993/aims-and-scope
[7]: https://www.editorialmanager.com/rntb
[8]: https://link.springer.com/10.1007/s13370-018-0632-y?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s11139-024-00955-x?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s11139-022-00555-7?fromPaywallRec=false
[11]: /subjects/algebra
[12]: /subjects/combinatorics
[13]: /subjects/computational-number-theory
[14]: /subjects/discrete-mathematics
[15]: /subjects/integral-equations
[16]: /subjects/number-theory
[17]: /subjects/diophantine-equations-in-algebraic-number-theory
[18]: /article/10.1007/s40993-021-00293-7#ref-CR1
[19]: /article/10.1007/s40993-021-00293-7#ref-CR3
[20]: /article/10.1007/s40993-021-00293-7#Equ1
[21]: /article/10.1007/s40993-021-00293-7#Equ2
[22]: /article/10.1007/s40993-021-00293-7#ref-CR13
[23]: /article/10.1007/s40993-021-00293-7#ref-CR18
[24]: /article/10.1007/s40993-021-00293-7#ref-CR7
[25]: /article/10.1007/s40993-021-00293-7#ref-CR14
[26]: /article/10.1007/s40993-021-00293-7#Sec2
[27]: /article/10.1007/s40993-021-00293-7#FPar1
[28]: /article/10.1007/s40993-021-00293-7#Sec3
[29]: /article/10.1007/s40993-021-00293-7#FPar3
[30]: /article/10.1007/s40993-021-00293-7#FPar5
[31]: /article/10.1007/s40993-021-00293-7#Sec4
[32]: /article/10.1007/s40993-021-00293-7#FPar12
[33]: /article/10.1007/s40993-021-00293-7#FPar16
[34]: /article/10.1007/s40993-021-00293-7#Sec5
[35]: /article/10.1007/s40993-021-00293-7#ref-CR15
[36]: /article/10.1007/s40993-021-00293-7#ref-CR2
[37]: /article/10.1007/s40993-021-00293-7#ref-CR5
[38]: /article/10.1007/s40993-021-00293-7#ref-CR8
[39]: /article/10.1007/s40993-021-00293-7#ref-CR11
[40]: /article/10.1007/s40993-021-00293-7#ref-CR17
[41]: /article/10.1007/s40993-021-00293-7#ref-CR19
[42]: /article/10.1007/s40993-021-00293-7#Equ3
[43]: /article/10.1007/s40993-021-00293-7#ref-CR9
[44]: /article/10.1007/s40993-021-00293-7#ref-CR16
[45]: /article/10.1007/s40993-021-00293-7#FPar8
[46]: /article/10.1007/s40993-021-00293-7#ref-CR20
[47]: /article/10.1007/s40993-021-00293-7#ref-CR6
[48]: /article/10.1007/s40993-021-00293-7#ref-CR4
[49]: /article/10.1007/s40993-021-00293-7#ref-CR10
[50]: /article/10.1007/s40993-021-00293-7#FPar24
[51]: https://doi.org/10.1073%2Fpnas.191488598
[52]: http://www.ams.org/mathscinet-getitem?mr=1862931
[53]: http://scholar.google.com/scholar_lookup?amp;title=Congruence%20properties%20for%20the%20partition%20function&amp;journal=Proc.%20Natl.%20Acad.%20Sci.%20USA&amp;doi=10.1073%2Fpnas.191488598&amp;volume=98&amp;issue=23&amp;pages=12882-12884&amp;publication_year=2001&amp;author=Ahlgren%2CS&amp;author=Ono%2CK
[54]: https://doi.org/10.1017%2FCBO9781139167239
[55]: http://scholar.google.com/scholar_lookup?amp;title=Integer%20Partitions&amp;doi=10.1017%2FCBO9781139167239&amp;publication_year=2004&amp;author=Andrews%2CG&amp;author=Eriksson%2CK
[56]: https://doi.org/10.1016%2F0001-8708%2872%2990028-X
[57]: http://www.ams.org/mathscinet-getitem?mr=306105
[58]: http://scholar.google.com/scholar_lookup?amp;title=Partition%20identities&amp;journal=Adv.%20Math.&amp;doi=10.1016%2F0001-8708%2872%2990028-X&amp;volume=9&amp;pages=10-51&amp;publication_year=1972&amp;author=Andrews%2CG
[59]: https://doi.org/10.2140%2Fant.2008.2.859
[60]: http://www.ams.org/mathscinet-getitem?mr=2457355
[61]: http://scholar.google.com/scholar_lookup?amp;title=Integral%20points%20on%20hyperelliptic%20curves&amp;journal=Algebra%20Number%20Theory&amp;doi=10.2140%2Fant.2008.2.859&amp;volume=2&amp;issue=8&amp;pages=859-885&amp;publication_year=2008&amp;author=Bugeaud%2CY&amp;author=Mignotte%2CM&amp;author=Siksek%2CS&amp;author=Stoll%2CM&amp;author=Tengely%2CSz
[62]: https://link.springer.com/doi/10.1007/s00026-019-00467-2
[63]: http://www.ams.org/mathscinet-getitem?mr=4039553
[64]: http://scholar.google.com/scholar_lookup?amp;title=Quasipolynomials%20and%20maximal%20coefficients%20of%20Gaussian%20polynomials&amp;journal=Ann.%20Comb.&amp;doi=10.1007%2Fs00026-019-00467-2&amp;volume=23&amp;issue=3%E2%80%934&amp;pages=589-611&amp;publication_year=2019&amp;author=Castillo%2CA&amp;author=Flores%2CS&amp;author=Hernandez%2CA&amp;author=Kronholm%2CB&amp;author=Larsen%2CA&amp;author=Martinez%2CA
[65]: http://www.ams.org/mathscinet-getitem?mr=4484
[66]: http://www.emis.de/MATH-item?0025.24902
[67]: http://scholar.google.com/scholar_lookup?amp;title=Sur%20les%20points%20rationnels%20des%20courbes%20alg%C3%A9briques%20de%20genre%20sup%C3%A9rieur%20%C3%A0%20l%E2%80%99unit%C3%A9&amp;journal=C.%20R.%20Acad.%20Sci.%20Paris&amp;volume=212&amp;pages=882-885&amp;publication_year=1941&amp;author=Chabauty%2CC
[68]: https://doi.org/10.1017%2FS0305004100045072
[69]: http://www.ams.org/mathscinet-getitem?mr=248102
[70]: http://scholar.google.com/scholar_lookup?amp;title=Congruence%20properties%20of%20the%20binary%20partition%20function&amp;journal=Proc.%20Camb.%20Philos.%20Soc.&amp;doi=10.1017%2FS0305004100045072&amp;volume=66&amp;pages=371-376&amp;publication_year=1969&amp;author=Churchhouse%2CRF
[71]: https://doi.org/10.1006%2Fjsco.1996.0125
[72]: http://www.ams.org/mathscinet-getitem?mr=1484478
[73]: http://scholar.google.com/scholar_lookup?amp;title=The%20Magma%20algebra%20system.%20I.%20The%20user%20language&amp;journal=J.%20Symb.%20Comput.&amp;doi=10.1006%2Fjsco.1996.0125&amp;volume=24&amp;pages=235-265&amp;publication_year=1997&amp;author=Bosma%2CW&amp;author=Cannon%2CJ&amp;author=Playoust%2CC
[74]: http://www.ams.org/mathscinet-getitem?mr=217010
[75]: http://scholar.google.com/scholar_lookup?amp;title=Sur%20un%20probl%C3%A8me%20de%20g%C3%A9om%C3%A9trie%20diophantienne%20lin%C3%A9aire%2C%20II.%20Syst%C3%A8mes%20diophantiens%20lin%C3%A9aires&amp;journal=J.%20Reine%20Angew.%20Math.&amp;volume=227&amp;pages=25-49&amp;publication_year=1967&amp;author=Ehrhart%2CE
[76]: https://doi.org/10.4064%2Faa170315-16-4
[77]: http://www.ams.org/mathscinet-getitem?mr=3911695
[78]: http://scholar.google.com/scholar_lookup?amp;title=Computing%20integral%20points%20on%20genus%202%20curves%20estimating%20hyperelliptic%20logarithms&amp;journal=Acta%20Arithm.&amp;doi=10.4064%2Faa170315-16-4&amp;volume=187&amp;issue=4&amp;pages=329-344&amp;publication_year=2019&amp;author=Gallegos-Ruiz%2CHR
[79]: https://doi.org/10.4064%2Faa-68-2-171-192
[80]: http://www.ams.org/mathscinet-getitem?mr=1305199
[81]: http://scholar.google.com/scholar_lookup?amp;title=Computing%20integral%20points%20on%20elliptic%20curves&amp;journal=Acta%20Arithm.&amp;doi=10.4064%2Faa-68-2-171-192&amp;volume=68&amp;issue=2&amp;pages=171-192&amp;publication_year=1994&amp;author=Gebel%2CJ&amp;author=Peth%C5%91%2CA&amp;author=Zimmer%2CHG
[82]: http://www.ams.org/mathscinet-getitem?mr=2026397
[83]: http://www.emis.de/MATH-item?1049.11028
[84]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20solutions%20of%20the%20Diophantine%20equation%20of%20Frobenius%E2%80%94general%20case&amp;journal=Math.%20Commun.&amp;volume=8&amp;issue=2&amp;pages=195-206&amp;publication_year=2003&amp;author=Komatsu%2CT
[85]: https://doi.org/10.1006%2Fjnth.1998.2288
[86]: http://www.ams.org/mathscinet-getitem?mr=1657968
[87]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20parity%20of%20additive%20representation%20functions%20%28with%20an%20appendix%20by%20J-P.%20Serre%29&amp;journal=J.%20Number%20Theory&amp;doi=10.1006%2Fjnth.1998.2288&amp;volume=73&amp;pages=292-317&amp;publication_year=1998&amp;author=Nicolas%2CJ-L&amp;author=Ruzsa%2CIZ&amp;author=S%C3%A1rk%C3%B6zy%2CA
[88]: https://doi.org/10.1142%2FS1793042106000644
[89]: http://www.ams.org/mathscinet-getitem?mr=2264602
[90]: http://scholar.google.com/scholar_lookup?amp;title=Partitions%20with%20parts%20in%20a%20finitie%20set&amp;journal=Int.%20J.%20Number%20Theory&amp;doi=10.1142%2FS1793042106000644&amp;volume=2&amp;issue=3&amp;pages=455-468&amp;publication_year=2006&amp;author=R%C3%B8dseth%2C%C3%98J&amp;author=Sellers%2CJA
[91]: https://doi.org/10.1515%2Fdma.1998.8.2.153
[92]: http://www.ams.org/mathscinet-getitem?mr=1673087
[93]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20solutions%20of%20a%20Diophantine%20equation%20of%20Frobenius&amp;journal=Discret.%20Math.%20Appl.&amp;doi=10.1515%2Fdma.1998.8.2.153&amp;volume=8&amp;pages=153-162&amp;publication_year=1998&amp;author=Sert%C3%B6z%2CS
[94]: http://www.ams.org/mathscinet-getitem?mr=1270567
[95]: http://www.emis.de/MATH-item?0797.11031
[96]: http://scholar.google.com/scholar_lookup?amp;title=On%20the%20number%20of%20representations%20of%20an%20integer%20by%20a%20linear%20form&amp;journal=%C4%B0stanbul%20%C3%9Cniv.%20Fen%20Fak.%20Mat.%20Derg.&amp;volume=50&amp;pages=67-77&amp;publication_year=1993&amp;author=Sert%C3%B6z%2CS&amp;author=%C3%96zl%C3%BCk%2CA
[97]: https://doi.org/10.4064%2Faa-67-2-177-196
[98]: http://www.ams.org/mathscinet-getitem?mr=1291875
[99]: http://scholar.google.com/scholar_lookup?amp;title=Solving%20elliptic%20Diophantine%20equations%20by%20estimating%20linear%20forms%20in%20elliptic%20logarithms&amp;journal=Acta%20Arithm.&amp;doi=10.4064%2Faa-67-2-177-196&amp;volume=67&amp;issue=2&amp;pages=177-196&amp;publication_year=1994&amp;author=Stroeker%2CRJ&amp;author=Tzanakis%2CN
[100]: https://doi.org/10.2307%2F121118
[101]: http://www.ams.org/mathscinet-getitem?mr=1745020
[102]: http://scholar.google.com/scholar_lookup?amp;title=Distribution%20of%20the%20partition%20function%20modulo%20%24%24m%24%24%20m&amp;journal=Ann.%20Math.&amp;doi=10.2307%2F121118&amp;volume=151&amp;pages=1-15&amp;publication_year=2000&amp;author=Ono%2CK
[103]: https://doi.org/10.4064%2Faa-75-2-165-190
[104]: http://www.ams.org/mathscinet-getitem?mr=1379397
[105]: http://scholar.google.com/scholar_lookup?amp;title=Solving%20elliptic%20Diophantine%20equations%20by%20estimating%20linear%20forms%20in%20elliptic%20logarithms.%20The%20case%20of%20quartic%20equations&amp;journal=Acta%20Arithm.&amp;doi=10.4064%2Faa-75-2-165-190&amp;volume=75&amp;issue=2&amp;pages=165-190&amp;publication_year=1996&amp;author=Tzanakis%2CN
[106]: https://mathoverflow.net/q/315828
[107]: https://mathoverflow.net/users/124654/zhi-wei-sun
[108]: https://citation-needed.springer.com/v2/references/10.1007/s40993-021-00293-7?format=refman&amp;flavour=references
[109]: /search?sortBy=newestFirst&amp;contributor=Szabolcs%20Tengely
[110]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Szabolcs%20Tengely
[111]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Szabolcs%20Tengely%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[112]: /search?sortBy=newestFirst&amp;contributor=Maciej%20Ulas
[113]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Maciej%20Ulas
[114]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Maciej%20Ulas%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[115]: mailto:Maciej.Ulas@im.uj.edu.pl
[116]: http://creativecommons.org/licenses/by/4.0/
[117]: https://s100.copyright.com/AppDispatchServlet?title=Equal%20values%20of%20certain%20partition%20functions%20via%20Diophantine%20equations&amp;author=Szabolcs%20Tengely%20et%20al&amp;contentID=10.1007%2Fs40993-021-00293-7&amp;copyright=The%20Author%28s%29&amp;publication=2522-0160&amp;publicationDate=2021-10-21&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[118]: https://crossmark.crossref.org/dialog/?doi=10.1007/s40993-021-00293-7
[119]: https://citation-needed.springer.com/v2/references/10.1007/s40993-021-00293-7?format=refman&amp;flavour=citation
[120]: /search?query=Partitions&amp;facet-discipline=#34;Mathematics&#34;
[121]: /search?query=Diophantine%20equation&amp;facet-discipline=#34;Mathematics&#34;
[122]: /search?query=Polynomial&amp;facet-discipline=#34;Mathematics&#34;
[123]: /search?query=Identities&amp;facet-discipline=#34;Mathematics&#34;
[124]: /search?query=11D41&amp;facet-discipline=#34;Mathematics&#34;
[125]: /search?query=11P83&amp;facet-discipline=#34;Mathematics&#34;
