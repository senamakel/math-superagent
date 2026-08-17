<!-- source: https://encyclopediaofmath.org/wiki/Resultant | converted from HTML -->

Resultant - Encyclopedia of Mathematics

[1]

- [Log in][2]

[www.springer.com][3] [The European Mathematical Society][4]

##### Navigation

- [Main page][5]
- [Pages A-Z][6]
- [StatProb Collection][7]
- [Recent changes][8]
- [Current events][9]
- [Random page][10]
- [Help][11]
- [Project talk][12]
- [Request account][13]

##### Tools

- [What links here][14]
- [Related changes][15]
- [Special pages][16]
- Printable version
- [Permanent link][17]
- [Page information][18]

##### Namespaces

- [Page][19]
- [Discussion][20]

##### Variants

##### Views

- [View][19]
- [View source][21]
- [History][22]

##### Actions

# Resultant

From Encyclopedia of Mathematics

Jump to: navigation, search

2020 Mathematics Subject Classification: *Primary:*[12-XX][23] [[MSN][24]][[ZBL][25]]

The *resultant of two polynomials $f(x)$ and $g(x)$*is the element of the field $Q$ defined by the formula:

$$\def\a{ {\alpha}}\def\b{ {\beta}}R(f,g) = a_0^s b_0^n \prod_{i=1}^n\prod_{j=1}^s(\a_i-\b_j),\label{1}$$ where $Q$ is the splitting field of the polynomial $fg$ (cf. [Splitting field of a polynomial][26]), and $\a_i,\b_j$ are the roots (cf. [Root][27]) of the polynomials

$$f(x) = a_0x^n+a_1x^{n-1}+\cdots+a_n$$ and

$$g(x) = b_0x^s+b_1x^{s-1}+\cdots+b_s,$$ respectively. If $a_0b_0 \ne 0$, then the polynomials have a common root if and only if the resultant equals zero. The following equality holds:

$$R(g,f) = (-1)^{ns}R(f,g).$$ The resultant can be written in either of the following ways:

$$R(f,g) = a_0^s\prod_{i=1}^n g(\a_i),\label{2}$$

$$R(f,g) = (-1)^{ns}b_0^n\prod_{j=1}^s f(\b_j),\label{3}$$ The expressions (1)–(3) are inconvenient for computing the resultant, since they contain the roots of the polynomials. Using the coefficients of the polynomials, the resultant can be expressed in the form of the [determinant][28] of the following block matrix $\begin{pmatrix}A\\B\end{pmatrix}$ with $A$ of order $s\times (n+s)$ and $B$ of order $n\times(n+s)$:

$$A= \begin{pmatrix} a_0 & a_1 & \cdots & a_n & & \\ & a_0 & a_1 & \cdots & a_n & \\ & &\cdots&\cdots& &\\ & & a_0 & a_1 & \cdots & a_n \end{pmatrix}, \quad B=\begin{pmatrix} b_0 & b_1 & \cdots & b_s & & \\ & b_0 & b_1 & \cdots & b_s & \\ & &\cdots&\cdots& &\\ & & b_0 & b_1 & \cdots & b_s \end{pmatrix}. \label{4}$$ The rows of $A$ contain the coefficients of the polynomial $f(x)$, the rows of $B$ contain the coefficients of the polynomial $g(x)$, and in the free spaces there are zeros. In the last row of $A$ $a_0$ is in the $s$-th column, in the last row of $B$ $b_0$ is in the $n$-th column.

The resultant of two polynomials $f(x)$ and $g(x)$ with numerical coefficients can be represented in the form of a determinant of order $n$ (or $s$). For this one has to find the remainders from the division of $x^kg(x)$ by $f(x)$, $k=0,\cdots,n-1$. Let these be

$$a_{k0}+ a_{k1}x+\cdots+a_{kn-1}x^{n-1}.$$ Then

$$R(f,g) = a_0^s \det\begin{pmatrix} a_{00} & a_{01} & \cdots & a_{0n-1}\\ a_{10} & a_{11} & \cdots & a_{1n-1}\\ \vdots & \cdots & \cdots & \vdots \\ a_{n-10} & a_{n-11} & \cdots & a_{n-1n-1}\\ \end{pmatrix}.$$ The [discriminant][29] $D(f)$ of the polynomial

$$f(x) = a_0x^n + a_1 x^{n-1} + \cdots + a_n, \quad a_0 \ne 0$$ can be expressed by the resultant of the polynomial $f(x)$ and its derivative $f'(x)$ in the following way:

$$D(f) = (-1)^{n(n-1)/2} a_0^{-1} R(f,f').$$

## Application to solving a system of equations.

Let there be given a system of two algebraic equations with coefficients from a field $P$:

$$f(x,y) = 0,\ g(x,y) = 0.\label{5}$$ The polynomials $f$ and $g$ are written as polynomials in $x$:

$$f(x,y) = a_0(y) x^k+ a_1(y)x^{k-1}+\cdots+a_k(y),$$

$$g(x,y) = b_0(y) x^l+ b_1(y)x^{l-1}+\cdots+b_l(y),$$ and according to formula (4) the resultant of these polynomials (as polynomials in $x$) is calculated. This yields a polynomial that depends only on $y$:

$$R(f,g) = F(y).$$ One says that the polynomial $F(y)$ is obtained by eliminating $x$ from the polynomials $f(x,y)$ and $g(x,y)$. If $\def\a{ {\alpha}}\def\b{ {\beta}} x=\a$ and $y=\b$ is a solution of the system (5), then $F(\b) = 0$, and, conversely, if $F(\b) = 0$, then either the polynomials $f(x,\b)$ or $g(x,\b)$ have a common root (which must be looked for among the roots of their greatest common divisor), or $a_0(\b) = b_0(\b) = 0$. Solving system (5) is thereby reduced to the computation of the roots of the polynomial $F(y)$ and of the common roots of the polynomials $f(x,\b)$ and $g(x,\b)$ in one indeterminate.

By analogy, systems of equations with any number of unknowns can be solved; however, this problem leads to extremely cumbersome calculations (see also [Elimination theory][30]).

#### References

[HoPe] | W.V.D. Hodge, D. Pedoe, "Methods of algebraic geometry", **1–3**, Cambridge Univ. Press (1947–1954) [MR1288307][31] [MR1288306][32] [MR1288305][33] [MR0061846][34] [MR0048065][35] [MR0028055][36] [Zbl 0796.14002][37] [Zbl 0796.14003][38] [Zbl 0796.14001][39] [Zbl 0157.27502][40] [Zbl 0157.27501][41] [Zbl 0055.38705][42] [Zbl 0048.14502][43] |

[Ku] | A.G. Kurosh, "Higher algebra", MIR (1972) (Translated from Russian) [MR0945393][44] [MR0926059][45] [MR0778202][46] [MR0759341][47] [MR0628003][48] [MR0384363][49] [Zbl 0237.13001][50] |

[La] | S. Lang, "Algebra", Addison-Wesley (1984) [MR0783636][51] [Zbl 0712.00001][52] |

[Ok] | L.Ya. Okunev, "Higher algebra", Moscow-Leningrad (1979) (In Russian) [Zbl 0154.26401][53] |

[Wa] | B.L. van der Waerden, "Algebra", **1–2**, Springer (1967–1971) (Translated from German) [MR1541390][54] [Zbl 1032.00002][55] [Zbl 1032.00001][56] [Zbl 0903.01009][57] [Zbl 0781.12003][58] [Zbl 0781.12002][59] [Zbl 0724.12002][60] [Zbl 0724.12001][61] [Zbl 0569.01001][62] [Zbl 0534.01001][63] [Zbl 0997.00502][64] [Zbl 0997.00501][65] [Zbl 0316.22001][66] [Zbl 0297.01014][67] [Zbl 0221.12001][68] [Zbl 0192.33002][69] [Zbl 0137.25403][70] [Zbl 0136.24505][71] [Zbl 0087.25903][72] [Zbl 0192.33001][73] [Zbl 0067.00502][74] |

**How to Cite This Entry:**
Resultant. *Encyclopedia of Mathematics.*URL: http://encyclopediaofmath.org/index.php?title=Resultant&oldid=52356

This article was adapted from an original article by I.V. Proskuryakov (originator), which appeared in Encyclopedia of Mathematics - ISBN 1402006098. [See original article][75]

Retrieved from " [https://encyclopediaofmath.org/index.php?title=Resultant&oldid=52356][76] "

[Categories][77]:

- [Algebra][78]
- [Field theory and polynomials][79]
- [TeX done][80]

- This page was last edited on 12 May 2022, at 11:30.

- [Privacy policy][81]
- [About Encyclopedia of Mathematics][82]
- [Disclaimers][83]

- [Copyrights][84]
- [Impressum-Legal][85]

Manage Cookies


## Links

[1]: /
[2]: /index.php?title=Special:UserLogin&returnto=Resultant
[3]: http://www.springer.com
[4]: http://www.euro-math-soc.eu/
[5]: /wiki/Main_Page
[6]: /wiki/Special:AllPages
[7]: /wiki/Category:Statprob
[8]: /wiki/Special:RecentChanges
[9]: /wiki/Encyclopedia_of_Mathematics:Current_events
[10]: /wiki/Special:Random
[11]: /wiki/Help:Contents
[12]: /wiki/Talk:EoM:This_project
[13]: /wiki/Special:RequestAccount
[14]: /wiki/Special:WhatLinksHere/Resultant
[15]: /wiki/Special:RecentChangesLinked/Resultant
[16]: /wiki/Special:SpecialPages
[17]: /index.php?title=Resultant&amp;oldid=52356
[18]: /index.php?title=Resultant&amp;action=info
[19]: /wiki/Resultant
[20]: /index.php?title=Talk:Resultant&amp;action=edit&amp;redlink=1
[21]: /index.php?title=Resultant&amp;action=edit
[22]: /index.php?title=Resultant&amp;action=history
[23]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=12-XX
[24]: https://mathscinet.ams.org/mathscinet/freetools/msc-search?text=12
[25]: https://zbmath.org/classification/?q=12
[26]: /wiki/Splitting_field_of_a_polynomial
[27]: /wiki/Root
[28]: /wiki/Determinant
[29]: /wiki/Discriminant
[30]: /wiki/Elimination_theory
[31]: https://mathscinet.ams.org/mathscinet/article?mr=1288307
[32]: https://mathscinet.ams.org/mathscinet/article?mr=1288306
[33]: https://mathscinet.ams.org/mathscinet/article?mr=1288305
[34]: https://mathscinet.ams.org/mathscinet/article?mr=0061846
[35]: https://mathscinet.ams.org/mathscinet/article?mr=0048065
[36]: https://mathscinet.ams.org/mathscinet/article?mr=0028055
[37]: https://zbmath.org/?q=an%3A0796.14002
[38]: https://zbmath.org/?q=an%3A0796.14003
[39]: https://zbmath.org/?q=an%3A0796.14001
[40]: https://zbmath.org/?q=an%3A0157.27502
[41]: https://zbmath.org/?q=an%3A0157.27501
[42]: https://zbmath.org/?q=an%3A0055.38705
[43]: https://zbmath.org/?q=an%3A0048.14502
[44]: https://mathscinet.ams.org/mathscinet/article?mr=0945393
[45]: https://mathscinet.ams.org/mathscinet/article?mr=0926059
[46]: https://mathscinet.ams.org/mathscinet/article?mr=0778202
[47]: https://mathscinet.ams.org/mathscinet/article?mr=0759341
[48]: https://mathscinet.ams.org/mathscinet/article?mr=0628003
[49]: https://mathscinet.ams.org/mathscinet/article?mr=0384363
[50]: https://zbmath.org/?q=an%3A0237.13001
[51]: https://mathscinet.ams.org/mathscinet/article?mr=0783636
[52]: https://zbmath.org/?q=an%3A0712.00001
[53]: https://zbmath.org/?q=an%3A0154.26401
[54]: https://mathscinet.ams.org/mathscinet/article?mr=1541390
[55]: https://zbmath.org/?q=an%3A1032.00002
[56]: https://zbmath.org/?q=an%3A1032.00001
[57]: https://zbmath.org/?q=an%3A0903.01009
[58]: https://zbmath.org/?q=an%3A0781.12003
[59]: https://zbmath.org/?q=an%3A0781.12002
[60]: https://zbmath.org/?q=an%3A0724.12002
[61]: https://zbmath.org/?q=an%3A0724.12001
[62]: https://zbmath.org/?q=an%3A0569.01001
[63]: https://zbmath.org/?q=an%3A0534.01001
[64]: https://zbmath.org/?q=an%3A0997.00502
[65]: https://zbmath.org/?q=an%3A0997.00501
[66]: https://zbmath.org/?q=an%3A0316.22001
[67]: https://zbmath.org/?q=an%3A0297.01014
[68]: https://zbmath.org/?q=an%3A0221.12001
[69]: https://zbmath.org/?q=an%3A0192.33002
[70]: https://zbmath.org/?q=an%3A0137.25403
[71]: https://zbmath.org/?q=an%3A0136.24505
[72]: https://zbmath.org/?q=an%3A0087.25903
[73]: https://zbmath.org/?q=an%3A0192.33001
[74]: https://zbmath.org/?q=an%3A0067.00502
[75]: http://encyclopediaofmath.org/index.php?title=Resultant&oldid=15841
[76]: https://encyclopediaofmath.org/index.php?title=Resultant&amp;oldid=52356
[77]: /wiki/Special:Categories
[78]: /wiki/Category:Algebra
[79]: /wiki/Category:Field_theory_and_polynomials
[80]: /wiki/Category:TeX_done
[81]: /wiki/Encyclopedia_of_Mathematics:Privacy_policy
[82]: /wiki/Encyclopedia_of_Mathematics:About
[83]: /wiki/Encyclopedia_of_Mathematics:General_disclaimer
[84]: /index.php/Encyclopedia_of_Mathematics:Copyrights
[85]: /index.php/Encyclopedia_of_Mathematics:Legal
