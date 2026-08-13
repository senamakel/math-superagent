<!-- source: https://en.wikipedia.org/wiki/Superelliptic_curve | converted from HTML -->

Superelliptic curve - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

In mathematics, a **superelliptic curve**is an [algebraic curve][1] defined by an equation of the form

y m = f ( x), {\displaystyle y^{m}=f(x),}[image: {\displaystyle y^{m}=f(x),}]

where m ≥ 2 {\displaystyle m\geq 2}[image: {\displaystyle m\geq 2}] is an integer and *f*is a [polynomial][2] of degree d ≥ 3 {\displaystyle d\geq 3}[image: {\displaystyle d\geq 3}] with coefficients in a field k {\displaystyle k}[image: {\displaystyle k}]; more precisely, it is the [smooth][3] [projective curve][4] whose [function field][5] defined by this equation. The case m = 2 {\displaystyle m=2}[image: {\displaystyle m=2}] and d = 3, 4 {\displaystyle d=3,4}[image: {\displaystyle d=3,4}] is an *[elliptic curve][6]*, the case m = 2 {\displaystyle m=2}[image: {\displaystyle m=2}] and d ≥ 5 {\displaystyle d\geq 5}[image: {\displaystyle d\geq 5}] is a *[hyperelliptic curve][7]*, and the case m = 3 {\displaystyle m=3}[image: {\displaystyle m=3}] and d ≥ 4 {\displaystyle d\geq 4}[image: {\displaystyle d\geq 4}] is an example of a *[trigonal curve][8]*.

Some authors impose additional restrictions, for example, that the integer m {\displaystyle m}[image: {\displaystyle m}] should not be divisible by the [characteristic][9] of k {\displaystyle k}[image: {\displaystyle k}], that the polynomial f {\displaystyle f}[image: {\displaystyle f}] should be [square free][10], that the integers *m*and *d*should be [coprime][11], or some combination of these. [1]

## Definition

[[edit][12]]

More generally, a *superelliptic curve*is a cyclic [branched covering][13]

C → P 1 {\displaystyle C\to \mathbb {P} ^{1}}[image: {\displaystyle C\to \mathbb {P} ^{1}}]

of the projective line of degree m ≥ 2 {\displaystyle m\geq 2}[image: {\displaystyle m\geq 2}] coprime to the characteristic of the field of definition. The degree m {\displaystyle m}[image: {\displaystyle m}] of the covering map is also referred to as the degree of the curve. By *cyclic covering*we mean that the [Galois group][14] of the covering (i.e., the corresponding [function field][15] extension) is [cyclic][16].

The fundamental theorem of [Kummer theory][17] implies [*[citation needed][18]*] that a superelliptic curve of degree m {\displaystyle m}[image: {\displaystyle m}] defined over a field k {\displaystyle k}[image: {\displaystyle k}] has an affine model given by an equation

y m = f ( x) {\displaystyle y^{m}=f(x)}[image: {\displaystyle y^{m}=f(x)}]

for some polynomial f ∈ k [x] {\displaystyle f\in k[x]}[image: {\displaystyle f\in k[x]}] of degree m {\displaystyle m}[image: {\displaystyle m}] with each root having order < m {\displaystyle <m}[image: {\displaystyle <m}], provided that C {\displaystyle C}[image: {\displaystyle C}] has a point defined over k {\displaystyle k}[image: {\displaystyle k}], that is, if the set C ( k) {\displaystyle C(k)}[image: {\displaystyle C(k)}] of k {\displaystyle k}[image: {\displaystyle k}] -rational points of C {\displaystyle C}[image: {\displaystyle C}] is not empty. For example, this is always the case when k {\displaystyle k}[image: {\displaystyle k}] is [algebraically closed][19]. In particular, function field extension k ( C) / k ( x) {\displaystyle k(C)/k(x)}[image: {\displaystyle k(C)/k(x)}] is a [Kummer extension][20].

## Ramification

[[edit][21]]

Let C: y m = f ( x) {\displaystyle C:y^{m}=f(x)}[image: {\displaystyle C:y^{m}=f(x)}] be a superelliptic curve defined over an algebraically closed field k {\displaystyle k}[image: {\displaystyle k}], and B ′ ⊂ k {\displaystyle B'\subset k}[image: {\displaystyle B'\subset k}] denote the set of roots of f {\displaystyle f}[image: {\displaystyle f}] in k {\displaystyle k}[image: {\displaystyle k}]. Define set B = { B ′ if m divides deg ⁡ ( f), B ′ ∪ { ∞ } otherwise. {\displaystyle B={\begin{cases}B'&{\text{ if }}m{\text{ divides }}\deg(f),\\B'\cup \{\infty \}&{\text{ otherwise.}}\end{cases}}}[image: {\displaystyle B={\begin{cases}B'&{\text{ if }}m{\text{ divides }}\deg(f),\\B'\cup \{\infty \}&{\text{ otherwise.}}\end{cases}}}] Then B ⊂ P 1 ( k) {\displaystyle B\subset \mathbb {P} ^{1}(k)}[image: {\displaystyle B\subset \mathbb {P} ^{1}(k)}] is the set of branch points of the covering map C → P 1 {\displaystyle C\to \mathbb {P} ^{1}}[image: {\displaystyle C\to \mathbb {P} ^{1}}] given by x {\displaystyle x}[image: {\displaystyle x}].

For an affine branch point α ∈ B {\displaystyle \alpha \in B}[image: {\displaystyle \alpha \in B}], let r α {\displaystyle r_{\alpha }}[image: {\displaystyle r_{\alpha }}] denote the order of α {\displaystyle \alpha }[image: {\displaystyle \alpha }] as a root of f {\displaystyle f}[image: {\displaystyle f}]. As before, we assume that 1 ≤ r α < m {\displaystyle 1\leq r_{\alpha }<m}[image: {\displaystyle 1\leq r_{\alpha }<m}]. Then e α = m ( m, r α) {\displaystyle e_{\alpha }={\frac {m}{(m,r_{\alpha })}}}[image: {\displaystyle e_{\alpha }={\frac {m}{(m,r_{\alpha })}}}] is the ramification index e ( P α, i) {\displaystyle e(P_{\alpha ,i})}[image: {\displaystyle e(P_{\alpha ,i})}] at each of the ( m, r α) {\displaystyle (m,r_{\alpha })}[image: {\displaystyle (m,r_{\alpha })}] ramification points P α, i {\displaystyle P_{\alpha ,i}}[image: {\displaystyle P_{\alpha ,i}}] of the curve lying over α ∈ A 1 ( k) ⊂ P 1 ( k) {\displaystyle \alpha \in \mathbb {A} ^{1}(k)\subset \mathbb {P} ^{1}(k)}[image: {\displaystyle \alpha \in \mathbb {A} ^{1}(k)\subset \mathbb {P} ^{1}(k)}] (that is actually true for any α ∈ k {\displaystyle \alpha \in k}[image: {\displaystyle \alpha \in k}]).

For the point at infinity, define integer 0 ≤ r ∞ < m {\displaystyle 0\leq r_{\infty }<m}[image: {\displaystyle 0\leq r_{\infty }<m}] as follows. If s = min { t ∈ Z ∣ m t ≥ deg ⁡ ( f) }, {\displaystyle s=\min\{t\in \mathbb {Z} \mid mt\geq \deg(f)\},}[image: {\displaystyle s=\min\{t\in \mathbb {Z} \mid mt\geq \deg(f)\},}] then r ∞ = m s − deg ⁡ ( f) {\displaystyle r_{\infty }=ms-\deg(f)}[image: {\displaystyle r_{\infty }=ms-\deg(f)}]. Note that ( m, r ∞) = ( m, deg ⁡ ( f)) {\displaystyle (m,r_{\infty })=(m,\deg(f))}[image: {\displaystyle (m,r_{\infty })=(m,\deg(f))}]. Then analogously to the other ramification points, e ∞ = m ( m, r ∞) {\displaystyle e_{\infty }={\frac {m}{(m,r_{\infty })}}}[image: {\displaystyle e_{\infty }={\frac {m}{(m,r_{\infty })}}}] is the ramification index e ( P ∞, i) {\displaystyle e(P_{\infty ,i})}[image: {\displaystyle e(P_{\infty ,i})}] at the ( m, r ∞) {\displaystyle (m,r_{\infty })}[image: {\displaystyle (m,r_{\infty })}] points P ∞, i {\displaystyle P_{\infty ,i}}[image: {\displaystyle P_{\infty ,i}}] that lie over ∞ {\displaystyle \infty }[image: {\displaystyle \infty }]. In particular, the curve is unramified over infinity if and only if its degree m {\displaystyle m}[image: {\displaystyle m}] divides deg ⁡ ( f) {\displaystyle \deg(f)}[image: {\displaystyle \deg(f)}].

Curve C {\displaystyle C}[image: {\displaystyle C}] defined as above is connected precisely when m {\displaystyle m}[image: {\displaystyle m}] and r α {\displaystyle r_{\alpha }}[image: {\displaystyle r_{\alpha }}] are relatively prime (not necessarily pairwise), which is assumed to be the case.

## Genus

[[edit][22]]

By the [Riemann-Hurwitz formula][23], the genus of a superelliptic curve is given by

g = 1 2 ( m ( | B | − 2) − ∑ α ∈ B ( m, r α)) + 1. {\displaystyle g={\frac {1}{2}}\left(m(|B|-2)-\sum _{\alpha \in B}(m,r_{\alpha })\right)+1.}[image: {\displaystyle g={\frac {1}{2}}\left(m(|B|-2)-\sum _{\alpha \in B}(m,r_{\alpha })\right)+1.}]

## Diophantine Problem

[[edit][24]]

The [Diophantine problem][25] of finding integer points on a superelliptic curve can be solved by a method similar to one used for the resolution of hyperelliptic equations: a [Siegel identity][26] is used to reduce to a [Thue equation][27]. [2]

Stronger results are known. For a given polynomial *f*with rational coefficients and at least two distinct roots, the above equation has only finitely many integer solutions *m*, *x*, *y*with m ≥ 3, | y | ≥ 2 {\displaystyle m\geq 3,\vert y\vert \geq 2}[image: {\displaystyle m\geq 3,\vert y\vert \geq 2}] and *m*, *x*, *y*are bounded by an effectively computable constant depending only on *f*. Furthermore, the condition m ≥ 3 {\displaystyle m\geq 3}[image: {\displaystyle m\geq 3}] can be replaced by m ≥ 2 {\displaystyle m\geq 2}[image: {\displaystyle m\geq 2}] in the case *f*has at least three distinct roots. [3]

More generally, let F ( X, Y) {\displaystyle F(X,Y)}[image: {\displaystyle F(X,Y)}] be a binary form such that F ( X, 1) {\displaystyle F(X,1)}[image: {\displaystyle F(X,1)}] has at least two distinct roots and all of them belongs to a finite extension k {\displaystyle k}[image: {\displaystyle k}] of Q {\displaystyle \mathbb {Q} }[image: {\displaystyle \mathbb {Q} }], *O*be the ring of integers of k {\displaystyle k}[image: {\displaystyle k}], *S*be the set of integers which are composed only of non-unit elements from a fixed set in *O*. Moreover, take an ideal *I*from k {\displaystyle k}[image: {\displaystyle k}]. Then then equation

w z m = F ( x, y) {\displaystyle wz^{m}=F(x,y)}[image: {\displaystyle wz^{m}=F(x,y)}]

with w, y ∈ S, x, z ∈ O, m ≥ 3 {\displaystyle w,y\in S,x,z\in O,m\geq 3}[image: {\displaystyle w,y\in S,x,z\in O,m\geq 3}], and ( x, y) = I {\displaystyle (x,y)=I}[image: {\displaystyle (x,y)=I}] implies that heights of *w*, *x*, *y*, *z*, and *m*are bounded by an effectively computable constant depending only on *f*, k {\displaystyle k}[image: {\displaystyle k}], and *I*. Furthermore, the condition m ≥ 3 {\displaystyle m\geq 3}[image: {\displaystyle m\geq 3}] can be replaced by m ≥ 2 {\displaystyle m\geq 2}[image: {\displaystyle m\geq 2}] in the case F ( X, 1) {\displaystyle F(X,1)}[image: {\displaystyle F(X,1)}] has at least three distinct roots. [4]

## See also

[[edit][28]]

- [Hyperelliptic curve][7]
- [Branched covering][13]
- [Artin-Schreier curve][29]
- [Kummer theory][17]
- [Superellipse][30]

## References

[[edit][31]]

1. ↑ Galbraith, S.D.; Paulhus, S.M.; Smart, N.P. (2002). ["Arithmetic on superelliptic curves"][32]. *[Mathematics of Computation][33]*. **71**: 394– 405. [doi][34]: [10.1090/S0025-5718-00-01297-7][32]. [MR][35] [1863009][36].
2. ↑ Shorey and Tijdeman (1986), Theorem 6.1
3. ↑ Shorey and Tijdeman (1986), Theorem 10.2
4. ↑ Shorey and Tijdeman (1986), Theorems 10.6 and 10.7, see also [Shorey, T.N.][37]; [van der Poorten, A. J.][38]; [Tijdeman, R.][39]; [Schinzel, A.][40] (1977). "Applications of the Gel'fond-Baker Method to Diophantine Equations". In [Baker, A.][41]; [Masser, D.W.][42] (eds.). *Transcendence Theory: Advances and Applications, Proceedings of a conference held in Cambridge in 1976*. [Academic Press][43]. pp. 59--77.

- Hindry, Marc; [Silverman, Joseph H.][44] (2000). *Diophantine Geometry: An Introduction*. [Graduate Texts in Mathematics][45]. Vol. 201. [Springer-Verlag][46]. p. 361. [ISBN][47] [0-387-98981-1][48]. [Zbl][49] [0948.11023][50].
- \\mathbb{C}</math>"},"url":{"wt":""},"journal":{"wt":"Bull. Austral. Math. Soc."},"publisher":{"wt":""},"volume":{"wt":"43"},"issue":{"wt":"3"},"pages":{"wt":"399–405"},"doi":{"wt":"10.1017/S0004972700029245"},"doi-access":{"wt":"free"}},"i":0}}]}'/> Koo, Ja Kyung (1991). [image: {\displaystyle \mathbb {C} }] ["On holomorphic differentials of some algebraic function field of one variable over C {\displaystyle \mathbb {C} } "][51]. *Bull. Austral. Math. Soc*. **43**(3): 399– 405. [doi][34]: [10.1017/S0004972700029245][51].
- [Lang, Serge][52] (1978). *Elliptic Curves: Diophantine Analysis*. Grundlehren der mathematischen Wissenschaften. Vol. 231. [Springer-Verlag][46]. [ISBN][47] [0-387-08489-4][53].
- Malmendier, A.; Shaska, T. (2019-06-15). ["From hyperelliptic to superelliptic curves"][54]. *Albanian Journal of Mathematics*. **13**(1). [arXiv][55]: [1906.02373][56]. [doi][34]: [10.51286/albjm/1575612673][57]. [ISSN][58] [1930-1235][59].
- [Shorey, T.N.][37]; [Tijdeman, R.][39] (1986). *Exponential Diophantine equations*. Cambridge Tracts in Mathematics. Vol. 87. [Cambridge University Press][60]. [doi][34]: [10.1017/CBO9780511566042][61]. [ISBN][47] [0-521-26826-5][62]. [Zbl][49] [0606.10011][63].
- [Smart, N. P.][64] (1998). *The Algorithmic Resolution of Diophantine Equations*. London Mathematical Society Student Texts. Vol. 41. [Cambridge University Press][60]. [ISBN][47] [0-521-64633-2][65].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Superelliptic_curve&oldid=1354785137][66] "

[Category][67]:

- [Algebraic curves][68]

Hidden categories:

- [All articles with unsourced statements][69]
- [Articles with unsourced statements from February 2014][70]
- [Pages that use a deprecated format of the math tags][71]

Search

Superelliptic curve

Add languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Algebraic_curve
[2]: https://en.wikipedia.org/wiki/Polynomial
[3]: https://en.wikipedia.org/wiki/Smooth_scheme
[4]: https://en.wikipedia.org/wiki/Projective_curve
[5]: https://en.wikipedia.org/wiki/Algebraic_function_field
[6]: https://en.wikipedia.org/wiki/Elliptic_curve
[7]: https://en.wikipedia.org/wiki/Hyperelliptic_curve
[8]: https://en.wikipedia.org/wiki/Trigonal_curve
[9]: https://en.wikipedia.org/wiki/Characteristic_(algebra)
[10]: https://en.wikipedia.org/wiki/Square_free
[11]: https://en.wikipedia.org/wiki/Coprime
[12]: /w/index.php?title=Superelliptic_curve&amp;action=edit&amp;section=1
[13]: https://en.wikipedia.org/wiki/Branched_covering
[14]: https://en.wikipedia.org/wiki/Galois_group
[15]: https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety
[16]: https://en.wikipedia.org/wiki/Cyclic_group
[17]: https://en.wikipedia.org/wiki/Kummer_theory
[18]: https://en.wikipedia.org/wiki/Wikipedia:Citation_needed
[19]: https://en.wikipedia.org/wiki/Algebraically_closed_field
[20]: https://en.wikipedia.org/wiki/Kummer_extension
[21]: /w/index.php?title=Superelliptic_curve&amp;action=edit&amp;section=2
[22]: /w/index.php?title=Superelliptic_curve&amp;action=edit&amp;section=3
[23]: https://en.wikipedia.org/wiki/Riemann-Hurwitz_formula
[24]: /w/index.php?title=Superelliptic_curve&amp;action=edit&amp;section=4
[25]: https://en.wikipedia.org/wiki/Diophantine_problem
[26]: https://en.wikipedia.org/wiki/Siegel_identity
[27]: https://en.wikipedia.org/wiki/Thue_equation
[28]: /w/index.php?title=Superelliptic_curve&amp;action=edit&amp;section=5
[29]: https://en.wikipedia.org/wiki/Artin-Schreier_curve
[30]: https://en.wikipedia.org/wiki/Superellipse
[31]: /w/index.php?title=Superelliptic_curve&amp;action=edit&amp;section=6
[32]: https://doi.org/10.1090%2FS0025-5718-00-01297-7
[33]: https://en.wikipedia.org/wiki/Mathematics_of_Computation
[34]: https://en.wikipedia.org/wiki/Doi_(identifier)
[35]: https://en.wikipedia.org/wiki/MR_(identifier)
[36]: https://mathscinet.ams.org/mathscinet-getitem?mr=1863009
[37]: https://en.wikipedia.org/wiki/Tarlok_Nath_Shorey
[38]: https://en.wikipedia.org/wiki/Alfred_van_der_Poorten
[39]: https://en.wikipedia.org/wiki/Robert_Tijdeman
[40]: https://en.wikipedia.org/wiki/Andrzej_Schinzel
[41]: https://en.wikipedia.org/wiki/Alan_Baker_(mathematician)
[42]: https://en.wikipedia.org/wiki/David_Masser
[43]: https://en.wikipedia.org/wiki/Academic_Press
[44]: https://en.wikipedia.org/wiki/Joseph_H._Silverman
[45]: https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics
[46]: https://en.wikipedia.org/wiki/Springer-Verlag
[47]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[48]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-98981-1
[49]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[50]: https://zbmath.org/?format=complete&amp;q=an:0948.11023
[51]: https://doi.org/10.1017%2FS0004972700029245
[52]: https://en.wikipedia.org/wiki/Serge_Lang
[53]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-08489-4
[54]: https://projecteuclid.org/journals/albanian-journal-of-mathematics/volume-13/issue-1/FROM-HYPERELLIPTIC-TO-SUPERELLIPTIC-CURVES/10.51286/albjm/1575612673.full
[55]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[56]: https://arxiv.org/abs/1906.02373
[57]: https://doi.org/10.51286%2Falbjm%2F1575612673
[58]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[59]: https://search.worldcat.org/issn/1930-1235
[60]: https://en.wikipedia.org/wiki/Cambridge_University_Press
[61]: https://doi.org/10.1017%2FCBO9780511566042
[62]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-26826-5
[63]: https://zbmath.org/?format=complete&amp;q=an:0606.10011
[64]: https://en.wikipedia.org/wiki/Nigel_Smart_(cryptographer)
[65]: https://en.wikipedia.org/wiki/Special:BookSources/0-521-64633-2
[66]: https://en.wikipedia.org/w/index.php?title=Superelliptic_curve&amp;oldid=1354785137
[67]: /wiki/Help:Category
[68]: /wiki/Category:Algebraic_curves
[69]: /wiki/Category:All_articles_with_unsourced_statements
[70]: /wiki/Category:Articles_with_unsourced_statements_from_February_2014
[71]: /wiki/Category:Pages_that_use_a_deprecated_format_of_the_math_tags
